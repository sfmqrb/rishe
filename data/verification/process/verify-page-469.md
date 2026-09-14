# Verification process log — verify-page-469


## [2026-09-14T02:27:56.564Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 469 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-469.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-469.json. Write /home/sfmqrb/git/rishe/data/verification/page-469.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 469` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:57.432Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:58.217Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:58.231Z] TOOL RESULT

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


## [2026-09-14T02:27:58.783Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-469.txt"
}
```


### [2026-09-14T02:27:58.799Z] TOOL RESULT

```
1	=== PDF page 469 (book page 439) ===
2	--- entry 0 ---
3	ROOT [Greek] Sphallein : cause to fall, slip. From an unknown Semitic root  (refs KLN:114; AHD:78)
4	#1 (parent #0) [Greek] refs=AHD:78 | a-sphallein : not slippery, a bonding agent ☞Ne 1 ; asphaltos : tar
5	  #2 (parent #1) [Persian] refs=BQT:1024 | zeft «زفت» : tar
6	  #3 (parent #1) [Latin] refs=AHD | 
7	    #4 (parent #3) [French] refs=None | 
8	      #5 (parent #4) [Persian] refs=MON:264; VOP:12 | âsfâlt «آسفالت» | extra: اسفالت ، آسفالته
9	    #6 (parent #3) [English] refs=AHD | asphalt
10	--- entry 1 ---
11	ROOT [Indo-European] Sphel : to split  (refs POK:985)
12	#1 (parent #0) [Avestan] refs=POK:985 | spâra : shield
13	  #2 (parent #1) [Persian] refs=HRN:155 | separ «سپر» : shield
14	#3 (parent #0) [Sanskrit] refs=POK:985 | sphal : to open
15	  #4 (parent #3) [Persian] refs=BQT:1085 | spâr «سپار» : the cutting tip of plow
16	#5 (parent #0) [Latin] refs=POK:986 | spelta : split ore
17	  #6 (parent #5) [English] refs=None | spelter : zinc ore ; pewter : tin alloys
18	--- entry 2 ---
19	ROOT Sphelghen -> redirect to Spelgh
20	
```


## [2026-09-14T02:28:01.377Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-469.json",
 "description": "Read source JSON for page 469"
}
```


### [2026-09-14T02:28:01.426Z] TOOL RESULT

```
{
  "pdf_page": 469,
  "book_page": 439,
  "entries": [
    {
      "root": {
        "name": "Sphallein",
        "lang": "Greek",
        "refs": "KLN:114; AHD:78",
        "gloss": "cause to fall, slip. From an unknown Semitic root"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:78",
          "words": [
            {
              "translit": "a-sphallein",
              "gloss": "not slippery, a bonding agent",
              "script": null,
              "see": [
                "Ne 1"
              ]
            },
            {
              "translit": "asphaltos",
              "gloss": "tar",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1024",
          "words": [
            {
              "translit": "zeft",
              "gloss": "tar",
              "script": "زفت"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:264; VOP:12",
          "words": [
            {
              "translit": "âsfâlt",
              "gloss": null,
              "script": "آسفالت"
            }
          ],
          "script_extra": "اسفالت ، آسفالته",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "asphalt",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sphel",
        "lang": "Indo-European",
        "refs": "POK:985",
        "gloss": "to split"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:985",
          "words": [
            {
              "translit": "spâra",
              "gloss": "shield",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:155",
          "words": [
            {
              "translit": "separ",
              "gloss": "shield",
              "script": "سپر"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:985",
          "words": [
            {
              "translit": "sphal",
              "gloss": "to open",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1085",
          "words": [
            {
              "translit": "spâr",
              "gloss": "the cutting tip of plow",
              "script": "سپار"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:986",
          "words": [
            {
              "translit": "spelta",
              "gloss": "split ore",
              "script": null
            }
          ],
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
              "translit": "spelter",
              "gloss": "zinc ore",
              "script": null
            },
            {
              "translit": "pewter",
              "gloss": "tin alloys",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sphelghen",
        "redirect": "Spelgh"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:28:03.451Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','POK','HRN','BQT','MON','VOP','WLD','IEC','SYN','BRT','PHD','NYB','HUB','CHEUNG','ARY','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T02:28:04.692Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-14T02:28:08.490Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T02:28:08.569Z] TOOL RESULT

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
KNT_full.txt
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T02:28:09.428Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-14T02:28:10.379Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "w
```


## [2026-09-14T02:28:46.383Z] AGENT

Now let me research the sources. Starting with the local library.


## [2026-09-14T02:28:48.444Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK sphel / spel ===\"; grep -n \"sp(h)el\" POK_full.txt | head -30; echo \"=== POK 985 area ===\"; grep -n \"spalten, abspalten\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:28:48.515Z] TOOL RESULT

```
=== POK sphel / spel ===
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79943:fltextension sp(h)el-g-, nasalized (s)p(h)leng-: 
=== POK 985 area ===
```


## [2026-09-14T02:28:50.048Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN asphalt ===\"; grep -n -i \"asphalt\" KLN_1966.txt | head -20; echo \"=== KLN sphallein ===\"; grep -n -i \"sphallein\" KLN_1966.txt | head -20; echo \"=== AHD watkins sphal ===\"; grep -n -i \"sphal\\|asphalt\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:28:50.213Z] TOOL RESULT

```
=== KLN asphalt ===
2192:Alhambra,  n.,  the  palace  of  the  Moorish  kings  at Granada.  —  Sp.,  fr.  Arab.  ( al-kal'at )  al-hamrd’, ‘the  red  (castle)’,  fern,  of  ahmaru,  ‘red’,  rel.  to hammara,  ‘he  dyed  red’,  humrah,  ‘redness’,  Heb. hemdr.  ‘bitumen,  asphalt’  (so  called  because  of its  reddish  color),  hamdr,  ‘he  covered  or  smear¬ ed  with  asphalt’,  hdmer,  ‘mortar,  clay’  (so  called from  its  color),  Heb.  hdmdr,  Arab,  himdr, Aram.-Syr.  ijamard,  Akkad,  imeru,  ‘ass’,  lit.  ‘the reddish  brown  animal’,  Heb.  yahmdr,  Aram. yalfmurd,  Arab,  yahmdr,  ‘roebuck’  (also  named from  its  color).  The  Alhambra  was  called  ‘the
3656:L.  asper,  ‘rough’.  See  asperity, asphalt  also  asphaltum,  n.  —  F.  asphalte,  fr.  Late L.  asphaltus,  fr.  Gk.  HayoXxoc,,  which  is  of  un¬ certain,  possibly  Sem.,  origin.  See  Heinrich Lewy,  Die  semitischen  Fremdworter  im  Grie- chischen,  Berlin,  1895,  p.53.
3657:Derivatives:  asphalt,  tr.  v.,  asphalt-ine,  asphalt¬ ic,  adjs.
5090:bitumen,  n.,  1)  asphalt ;  2)  an  inflammable  mineral substance.  —  L.  bitumen,  ‘mineral  pitch’,  an Osco-Umbrian  loan  word  (the  genuine  Latin form  would  have  been  *vetumen,  fr.  *gwetu- meri)  of  Celtic  origin;  cogn.  with  OI .  jatu,  ‘lac, gum’,  ON.  kvada,  ‘resin’,  OE.  ewidu,  cudu, ‘mastic,  cud’.  See  cud  and  cp.  beton.  Cp.  also Be  tula.
=== KLN sphallein ===
=== AHD watkins sphal ===
```


## [2026-09-14T02:29:00.782Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Root / lemma: (s)p(h)el\\|Root / lemma: sp(h)el\\|Root / lemma: spel\" POK_full.txt | head -20; echo \"=== pages 985 ===\"; grep -n \"Page(s): 985\\|Page(s): 986\\|Page(s): 985-\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:29:00.851Z] TOOL RESULT

```
79800:Root / lemma: (s)p(h)elg- 
79821:Root / lemma: sp(h)elgh(en, -a), splengh-, splegh- 
79838:Root / lemma: (s)p(h)el-1 
79931:Root / lemma: (s)p(h)el-2 
=== pages 985 ===
79516:Page(s): 985 
79927:Page(s): 985-987
```


## [2026-09-14T02:29:02.632Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<4000 && /\\[page/ {print NR\": \"$0}' KLN_1966.txt | head -5; grep -n \"^\\s*114\\s*$\\|page 114\" KLN_1966.txt | head; echo \"--- context around 3656 ---\"; sed -n '3640,3660p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-14T02:29:03.752Z] TOOL RESULT

```
3646:114
--- context around 3656 ---
asor,  n.,  a  Hebrew  ten-stringed  instrument.  — Heb.  'asdr,  fr.  'eser  (masc.),  ‘ asardh  (fem.), ‘ten’,  which  is  rel.  to  Aram,  'dsar  (masc.),  asra (fem.),  Ugar.  ‘shr  (mas
Derivative:  asp-ish,  adj. asp,  n.  —  Poetic  form  of  aspen.
Derivative:  asp-en,  adj.
asparagus,  n.  —  L.,  fr.  Gk.  danapaycx;,  Att
Aspasia
assert
114
dctKpapayo?,  ‘asparagus,’  which  prob.  means  lit.
‘a  sprout’,  and  is  rel.  to  amxpyav,  ‘to  swell,  be ripe',  fr.  I.-E.  base  *sper(e)g,  *spher(e)g-,  ‘to sprout,  swell,  burst’,  whence  also  L.  spargere , ‘to  scatter’.  
Aspasia,  fern.  PN.  —  L.,  fr.  Gk.  ’  A<jtowj(S,  fem. of  aoizaaioc;,  ‘welcome’,  which  is  rel.  to  acrmx- ^eahai,  ‘to  welcome’;  of  uncertain  origin, aspect,  n.  —  L.  a
aspect,  tr.  v.  —  L.  aspectare,  freq.  formed  fr. aspectus,  pp.  of  aspicere.  See  aspect,  n. aspen,  n.,  a  variety  of  poplar.  —  Orig.  an  adj. formed  with  suff.  -en  (cp.  ash
asperate,  tr.  v.,  to  make  rough.  —  L.  asperatus, pp.  of  asperdre.  See  asperity  and  verbal  suff.  -ate. asperges,  n.,  the  ceremony  of  sprinkling  (R.C.Ch.) —  L.  asperges,  sec
Aspergillus,  n.,  a  genus  of  fungi  (bot.)  —  ModL., a  diminutive  formed  fr.  L.  aspergere.  See asperges.
asperifoliate,  also  asperifolious,  adj.,  having  rough leaves.  —  Compounded  of  L.  asper,  ‘rough’, and  folium,  ’leaf’.  See  next  word  and  foliate, asperity,  n.,  roughness.  
Derivatives:  aspers-ed,  adj.,  aspers-er,  n.,  aspers- ive,  adj.,  aspers-ive-ly,  adv. aspersion,  n.  —  L.  aspersio,  gen.  -dnis,  fr.  asper¬ sus,  pp.  of  aspergere.  See  prec.  word  
family  (bot)  —  L.  asperugo,  ‘a  plant  with  prick¬ ly  leaves’,  fr.  asper,  ‘rough’.  See  asperity. Asperula,  n.  a  genus  of  plants  of  the  madder family  (bot)  —  ModL., 
L.  asper,  ‘rough’.  See  asperity, asphalt  also  asphaltum,  n.  —  F.  asphalte,  fr.  Late L.  asphaltus,  fr.  Gk.  HayoXxoc,,  which  is  of  un¬ certain,  possibly  Sem.,  origin.  See 
Derivatives:  asphalt,  tr.  v.,  asphalt-ine,  asphalt¬ ic,  adjs.
asphodel,  n.  —  L.  asphodelus,  fr.  Gk.  da<po8eXos, a  foreign  word  of  uncertain  origin.  Cp.  daffodil, which  is  a  doublet  of  asphodel. asphyxia,  n..  suspended  animation  (med)  �
fr.  A-  (see  priv.  pref.  a-)  and  orffy.',  ‘pulsation’, which  is  rel.  to  cnpuyfio 9,  ‘pulsation’,  mpu^eiv (for  *atpijy-ieiv),  ‘to  beat,  pulsate’.  See  sphyg- mus  and  -ia
asphyxiant,  adj.,  asphyxiating;  n.,  an  asphyxiat¬ ing  agent.  —  See  prec.  word  and  -ant. asphyxiate,  tr.  v.,  to  suffocate.  —  See  asphyxia and  verbal  suff.  -ate.
```


## [2026-09-14T02:29:12.199Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '79838,79935p' POK_full.txt"
}
```


### [2026-09-14T02:29:12.257Z] TOOL RESULT

```
Root / lemma: (s)p(h)el-1 



Meaning: to split, cut off, tear off; board 

Material: Old Indie sphafaf/ {Dhatup.) 'reiftt, springt auf, S/0/75///5-"gesprungen, zerfetzt', 
sp/7a///r5-'Bergkristair ('sich blattrig abspaltend'), *sphafayaf/ ^spWts', covered das 
participle sphatita-, sphutat/ ^spWts sich, springt auf, platzt, reiftt' (sek. sphotati); besides 
diesen /- present (: Old High German spaltan) das /c»-participle S/0/7^/5-'aufgebluht, open ' 
(: Gothic spilda); Old Indie /05/5//"splits sich, cracks', patayati^ sp\\\.s, breaks, rips' (: patu- 
"sharp', gr. nAaruc; ' salty '? s. under *pltu-s)\ 

yO/75/5//" cracks, springt divided ', phalakam ^ {*c\oyev\ wood) board, lath, leaf, shield, 
Holzbank', phala-xx\. ' plowshare ' ('zugespitztes AststiJck'?); Old pers. Glosse anapa- 
papai oi Ysppocpopoi Hes. 'schildtragend', npers. ispar, s/psA'shield' (Old Indie /0/7a/'a/77, 
spharam^s\\\e\6\ uncovered, probably from dem Iran, and in aniaut afteryC>/7a/a/r5/77 
directed); 

gr. ocpaAaaasiv tsijvsiv, ksvtsTv Hes., ocpaAa^ 'Stechdorn', oanaAaGoc; m. ds. ("*whereof 
man sich reiftt, scarifies '), ocpaAa^, aacpaAa^, anaAa^, aanaAa^ ' mole ' ('die Erde 
aufreiftend'), anaAuaasTai anapaaasTai, TapaaasTai Hes., aanaAov gkutoc; Hes., 
onaAauGpov "SchiJreisen'; anoAia ra napariAAotJSva spiSia ano tu)v oksAwv tu)v 
npopQTCjov Hes. (: Latin spolium), Attic anoAac; 'abgezogenes fell, fur' and "Uberwurf from 
Leder, breastplate, mantle', Aeolic anaAic;, Attic HJaAic; 'scissors'; to acpaAaaasiv also 
GcpaAoc; TuftblockforGefangene; Wurfscheibe' and ocpaAAu) 'throw (originally with 
'Prijgeln'), toss, fling, bump, poke' and '(at first beim Ringen) ein leg place, in fight, 
struggle hinder', from which 'bring to collapse, injure, hurt, deceive, cheat, deceive', Med. 
'waver, fall, sich irren', aa(paAr|(; 'unerschijtterlich, ohne sich fortstoften to let' - ' peaceful, 
certainly', ocpaAspoc; ' slippery ', ocpaAjja 'falscher footstep '; acpsAac; 'wooden log, club, 
cudgel; ausgehohlter block, bench '; 

from Alb. perhaps yoa/e'side, party ' ( *polna, compare Old Church Slavic pol-b 'side, 
bank, border, shore, gender, sex, half); yOOyoe/e'FelsstiJck, plaice', plis {*pli-tio-) 'clod of 
earth', plish^ reed ' {*pli-sio-)\ 

Latin spc»//^/77 'abgezogene orabgelegte Tierhaut; dem Feinde abgenommene RiJstung, 
booty'; 

with /-Erweit.: Old High German spaltan. Middle Low German spalden 'split', Gothic 
spilda {* spelta) 'Schreibtafel', Old Icelandic spjald {*speltos) 'board'. Old English speld 
'splint; bit of wood'. Middle High German spelte' cleaved bit of wood, Handgerat the 
Weberei'; Old Icelandic spjall, speZ/'damage' {*spell=>a-, -/■), Old English splld, splld' 
annihilation. Ruin', whereof Old Icelandic spllla, spella'spoW, slay' {* spell=>jan, *spell=>dn). 



Old Saxon spildian, Old English spMan' destroy', Old High German spildan, spilden 
"waste, spread', Old Saxon spildT generous '; Germanic /in Middle Low German spelte^ 
cloven piece'. East Frisian spa/terds., Germanic *spe/td {out of it Latin spelta) in Old High 
German spe/za Vulgar Latin spe/ta {irom which:) " spelt '; engl. spe/fer'Z\nk' {* spaldiz-); 
Old English Syoa/o'^/'' Balsam' {*spalduz- " effluence from cloven plant '); />present Old 
EnglishSyC»///a/7, Middle High German SyO///e/7 'split' {*spelljan), wherefore without s- Swedish 
^a7/"Schinnen in Haar'; Old Icelandic spglr^t\\\v\ flache shaft, pole'. Middle English spale 
ds.. Middle High German spale^ rung, horizontal step on a ladder'; probably (as "thin, flat 
bit of wood') Old High German spuolom., isl. 5/0o/e"Weberschiffchen', Norwegian spole 
"coil, spool' (Germanic *spdlan-)\ Old High German S/O^o/5 (Germanic *spdldn-) 'coil, 
spool', "duct, tube, pipe, quill '; without ani. s-\ Old Icelandic ^ip/"board' {*pela); 

with /-Erweit., but without s- probably Irish alta(i)n, cymr. ellyn, acymr. elinn' shearing 
knife ', abret. altln<^\. ' ferula ', Middle Breton autenn, nbret. aotenn' shearing knife ' 
{*paltlnS); mcymr. allaw'shave' {*alta-mu-); J. Loth RC. 45, 173. 

Lithuanian spalls, PI. spallal, Latvian 5pa//"Flachsschaben'; Latvian S/05/s "handle, hold, 
grasp'; Old Prussian 5pe/a/7A'//5 "splinter'; 

Old Church Slavic ras-platltr spWt' {*poltltl, compare Modern High German spalten. Old 
Indie sphatati), platb'^dKoc,, scrap, shred', poleno'p'\ece of wood wood', /OC»//ic5 "board', 
palica. Old Russian paltka'stScV!, russ. ras-polotb "entzweischneiden', polotb, poltb 
"(abgeschnittene) Speckseite', poltlna'haW, Old Church Slavic po/b. Gen. -^"half, side, 
bank, border, shore, gender, sex'; Old Bulgarian plevg, pletl {russ. polotb) " weed ', plevelb 
"weed'; *o-pelnb\r\ Czech opien, c»/0///7"Gipfstock, Rungenstock', sloven, opien 
"Wagengipfenholz' etc.; 

with dem i/from plevg {* peluo) is zusammenzuhalten: Latvian spalva' feather, 
Gefieder, hair', 5/0/7i/5"husk, Samenwolle, Wollgras', SyO//i/^/7s'Bettkissen' etc.; 

Tocharian A spaltk-, B spalk-^s\cV\ anstrengen'; 

References: WP. II 677 ff., WH. II 571 f., 577 f., Trautmann 204, Vasmer 2, 398, Flasdieck 

Zink under Zinn, 1 57 ff. 

See also: with {s)p{h)el- "split' hang possibly together: pel-'sk\r\, fell, fur', S/oe/g- "split', 

sp/e/- "split', yo/e/- "naked, bald, bleak', piek- plelk- ' rend ', pleu{s-, -k-) "ausrupfen', plas- 

"abspalten'. 

Page(s): 985-987 



Root / lemma: (s)p(h)el-2 

Meaning: to shine, shimmer 

Material: Old Indie sphulirjga-m. 'spark' (Erweiter. eines *sphuli= Armenian p'ail, Indo
```


## [2026-09-14T02:29:43.193Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT spara/spar ===\"; grep -n \"spāra\\|spara-\\|spar-\" BRT.txt | head -30"
}
```


### [2026-09-14T02:29:43.247Z] TOOL RESULT

```
=== BRT spara/spar ===
22691:vayaspara-  1358
26841:spar-
```


## [2026-09-14T02:29:43.952Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN sipar ===\"; grep -n -i \"sipar\\|separ\\|Schild\" HRN.txt | head -30"
}
```


### [2026-09-14T02:29:44.007Z] TOOL RESULT

```
=== HRN sipar ===
6143:700. sljßer, isper *Schild'.
6145:'Schild* in sparö.\dästa' ; phlv. spar (Men.); skr. phara-,
7456:856. feesß/ ^Schildkröte ; Krebs (Zodiac, Sahn. I, 77 Vers
7458:aw. kasyapu' 'Schildkröte' oder *Krebs' (Geldner,
7459:KZ. 25, 503, 5()6j ; skr. (Brhm.) kagydpa- 'Schildkröte .
7460:af/. kasy 'Schildkröte'; bei. käsib (190).
```


## [2026-09-14T02:29:47.427Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6138,6155p' HRN.txt; echo \"=== which printed page? leaf = printed + 21; find nearest page marker ===\"; awk 'NR<=6143 && /^\\[?[0-9]{1,3}\\]?$/ {ln=NR; v=$0} END{}' HRN.txt; grep -n \"^155$\\|^154$\\|^156$\" HRN.txt | head"
}
```


## [2026-09-14T02:29:48.054Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26835,26860p' BRT.txt"
}
```


### [2026-09-14T02:29:48.527Z] TOOL RESULT

```
pers. HNDID (Is. 13, 4).
ap. Ta/ma]späda- ; aw. spaöa- *Heer ; phlv. späh,
spühpat, arm. LW. späh, aspalmhet-),
oss. d. t. afsady t. ä/sud grosse Menge, xVbteilung
von Personen, Heer, Regiment* (40).
700. sljßer, isper *Schild'.
ap. anaoa^ßdgai' oi ye()()0(p6(}0i Hesyeh ; aw. spüra-
'Schild* in sparö.\dästa' ; phlv. spar (Men.); skr. phara-,
phalaka- (Mbh.) 'SchikV, daneben LW. sphara-^spharaka-
(Nöldeke, Monatsber. BAW. 1883, 1100).
arm. LW. aspar.
701. seperden, siperden auf etwas treten*.
aw. l^spar-^ vi\spara; phlv. spurtan (Bund.); ai.
[^sphur-^ sphurdti 'schnellen, treten; plötzlich er-
scheinen* (in letzter Bedeutung spät).
Nicht durchaus einwandsfrei.
wa/. na-spar-am, §i;'n. ni-^par-am, sar. na-xitor-am
^stampfen, treten*.
=== which printed page? leaf = printed + 21; find nearest page marker ===
```


### [2026-09-14T02:29:48.605Z] TOOL RESULT

```
•  j.,  g.  spanyah-,  spainyah-"  Adj.  'der beiligere';  i)  von  Göttern:  mainyü  . . yaya  'yä  uHl  mrava^  ySm  angnm  "von den  beiden  Geistern  . .,  von  denen  der heiligere  also  sprach  zu  dem  aigen"  Y. 43.  i;  —  frä  mi  "yh  *maimva  vavaia vispqm  aiaonB  stTm  Y.  ig.  9.  2)  von Menschen:  ava^a  ^ankä  'yä  yai  mqm paiti.p)r)sar3he  "so  wirst  du  heiliger  werden, wenn  .  ."  V. /<?.  7;  —  ''poumjiartm  tBm kirMBsi  "yaalum  V. /o.  13".
Kompar.  zu  sptnta-;  sd.,  auch  zEt  —  mp. spenäk  (mit  i  aus  ar.  aiyj.  —  Pü.  {lu  V.): awiütäilum,  (sonst):  miiaünli,  fa  aaaüniiiA.  — ')  Mit  sfaiii'  nur  Y.  10.  13.
•  g.  spayaOra-  n.  'Gedeihen,  Erfolg, Glück':  ada  sl  ava  drüjö  [ai/j]"  bai-aitl skgndB  '%rahya  a^  asiitä  yaojaittl  (sd.)  . . yBi  sasmil{sü.)  vatihau  sravakS  "alsdann ja  wird  fiit  die  Welt  der  I>rug  die  Zei^ Störung  des  Glücks  erfolgen '>,  aber.." Y.^.  10.
Zu  einem  Praei.  ir.  *{^d- gebildet  3>,  in  ^m ar.  *ii/aia-  Pracs.  24  -  in  imi;  Sp.  1 56 1 0  - and   *ifiA^a;   Praes.  4  oder  37  —  id  i^fä-  -
db,Google
i6i3
spar-
lusammengefallen  sein  kännen.  —  PQ. :  späh 'Heer'  -  Sü. ;  'paläkmikah  -,  wegen  des  Ad- klangs.  —  ')  S.  bav  No.'  14.  —  »)  iSt.  vgl.  Y. $3.  6  unter  fräday.  —  3)  Wie  ai.  gäyalri-, täruira;  iritidlra--a.a.;s.  nochNo.4.  —  4)  Dann vll.  mit  ai.  svälrä-  n.  {im  Nsigh.  'ähanam',  bei Olsenberg  SSE.  46.  26  'power')  lusunmen- gebörig,  das  ein  ar.  Praes.  21  'sgä-  voraus- setien  würde,  oder  -  was  das  selbe  ist  -  eine 'WurielcrwcileninB'  durcli  li;  vgl.  !irv:Ara:
•  j.  Spar- V. 'schnellen,  treten'.  Praes.  3'»
1)  'treten,  stossen';  ma  %wä  dasna mäzdayasnii  aspake  sparSit  sparmaini  (sd.) Vyt..?5-
mit/r,j  'hervorschnellen',  intrans.: /wj (sd.)  aya»h5  frasparai  Y.p.  11.
mit  Vi  'auseinandertreten,  -stampfen'; aiAhh  z^mS  (sd.)  pasnäbya  vTspara  V, 2.31;  32  {wo  visparai).
ai.   ifharäüi     np.   lipardaa.     —     Fü.  (dRn.) :
laiigandaH,   spiirtan,   sfarlan.    —    ')  So  nach
dem  ai.  Praesens.
•  j.  sparaj-a-  m.  'Spross',  von  den  Wider- haken unterhalb  der  Pfeilspitze:  asti  yä *ayat3kama  °ya  "es  kommt  vor,  dass eiserne  Sprossen  (dran,  am  Pfeil)  sind" YLjo.  129  Gl.
KompE.  —  Zum  ai.  -V.  sphhtjati  'es  bricht hervor")  lit.  sfht^as  -(Pflftnieniauge',
•  p.  sparda-  m.  Name  eines  Lands*': imn  dahyäva^  iyä  adam  *adarsiy  .  . artninJ'  katpaluk^  'da"  yauna  D.  5.  2 ; 6.  3,  Bh.  /.  6.
•)  Lydien  nach  GMeVer  IF.  /.  336;  sÄ  auch JuSTI  GltPb.  2.  254.
•  j.  sparaha-  n,  'Zahnfleisch'  (mit  den Alveolen):  "/la  Y.36..
EL?  ah  steht  für  ng,  vgl.  ta  'haoha-  Es stellt  »ich  somit  sp'  seiner  Bildung  nach  zu ai.  ^Ä^B-  n.  (woiu  Johansson  Beilr.  13,  IF. a.  24.  Bthi,-  IF.  3.  j68).  —  Fa.:  ha^aiar  i dandän,  übers,  mit  np.  :;>  i  dandan  'unter- halb der  Zähne'.
•  j.  sparman-  n.  etwa  'Tritt,  Stoss';  mü '^iwil  dalna  m/lzdayas'iis  aspaÄe''  sparSit 'maini  "damit  dich  nicht  die  tiasd.  Reli- gion stosse  mit  dem  Stoss  eines  Rosses" Vyt.ji(?).  '
Zum  V.  spar;  —  Pü. :  a:iij;aniin.  —  •)  Nach  Pü. (laagih)  gehörte  aspaht  lu  'aspä-.
•  g.  sparsz-  V.,  nur  mit  ä  'bestrebt  sein'. Praes.  3  sp^nza-.
mit  Inf:  y!  ,  .  dtmanakya  xh'i-rsm  .  . asil /rada>iJi  (sd.)  aspir?zai3  Y.^^/.  16. aL  vgl.  sffhäyati   'er   begehrt    eifrig  nach  -' (Dat.),  mp.  apl  spurzUan  'to  oppose'  (SBE.  4y.
72).  —  Pü. ;  aiöSitar,  a\.:  hii  ..  nie  käSft,  also a  als  Neg.  (daher  DsT.  ZA.  /.  331  'qui  ne jalouse  point');  vgl.  aipirtw.*.
```


## [2026-09-14T02:30:01.466Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== formfeed count before 6143 in HRN ===\"; head -6143 HRN.txt | tr -cd '\\f' | wc -c; echo \"=== grep sparo dasta in BRT ===\"; grep -n -i \"spar..dašta\\|sparo\\.\\|sparö\\|dašta-\\|dasta-\" BRT.txt | head -20"
}
```


### [2026-09-14T02:30:01.534Z] TOOL RESULT

```
=== formfeed count before 6143 in HRN ===
176
=== grep sparo dasta in BRT ===
28005:Ableit.  ans  larjtva-.  —  Pia.:  lanjäi, •  i-,  g.  zasta-,  p,  dasta-  m.  'Hand',  uzw, uÄKnscher  Wesen"';  i)  in  eigentlicher  Be- deutung, von  Menschen  und  Göttern:  in yazaiU  .  .  gaomata  °ta  (IS.)  Yt.y.  50;  — tara%ustrS . .  asünS  'la  draiimnB  V.  ip.  4; 19;  —  mtknm  ..yS ..vazr?m  °taya[lS.) ^draiimnB    Yt. /O.  96;  Y,57.  31,  V.  /p.  ig;
```


## [2026-09-14T02:30:02.653Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v2 zeft ===\"; grep -n \"زفت\" BQT_v2_pages.txt | head -20; echo \"=== BQT v2 sepār ===\"; grep -n \"سپار\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T02:30:02.734Z] TOOL RESULT

```
=== BQT v2 zeft ===
1760:                    ‫بکزفته اند‪ .‬ب‬                           ‫دوغ را بدان زنند تامکه برآبد ‪.‬‬
1897:‫به اآزفتاب و ماه‬
3322: ‫آن ‪ -‬و خاریشت بزرکه را یکزفته اند س‬
15731: ‫باشدھ ‪ -‬وتظلم‌ووارسیدن‪٩‬‏ وبهرمرا نکیزفتها‬                                 ‫در گاه یادشاهانر | گوبند ‪1‬‬
25825:                                                  ‫و ژوزفت‬   ‫در گذشت‬   ‫‪۶۲۹۱‬‬     ‫لن در‬
28174:                                                             ‫وودبازفت که اکزاشب‬
28827: ‫همين معنی دارده وآن سه‌نوع است ‪ :‬یکی زفت‬                                     ‫و بعربی لخاونانند ‪. ۴‬‬
28829:  ‫هیآ وزلد و بعضی گوشد همی زفت است هاش‬
28831: ‫زفت تر وآن‬      ‫برومی شهرت دارد » و دبگری‬                  ‫است » و آن چیزی است که در مان شاهین‬
28834: ‫ونوع سيم زفت خشك است وآلرا بیشترازینبوت‬
28861:          ‫شدش کالبد از زاری وز فرقت زفت‬                        ‫ساعتی با اولششت و یاسود نوضفت‬
30686:‫جدولهای ابنکتاب ظاهر میگردد " وممرب آن‬                           ‫لگ = بروزن قیف » زفت را گوبند‪.‬‬
30706:                                                                                         ‫زفت‬
31095:                                                                                                    ‫زفت‬
39524:    ‫کفت که اکزفت خود ماز لمیتوالم کشت ‪ ,‬ولی رسوایی ترا درئیمی از ماه پوشیده خواهم داشت‬
=== BQT v2 sepār ===
17420:                                                                                             ‫دمر‪-‬سپار‬
30776: ‫زین کوده افسترکیهوی و بلندی پیش زین‬                        ‫از خرق وخالت عنی حرفی را بکسی بسپارند‬
32601:  ‫‪( 1205 - 2۵۰‬بازکردن)؛سر یکلی]‪( 15‬خیش) «اسشق ‪«:۹۹۹6‬سپار ‪,‬کارآه نکه زمین‪‎‬‬
32602:            ‫‪« - ۴‬سپار آلت خاله بود ‪ .‬فرخی (سیمتالی) کفت‪: ‎‬‬             ‫شکافند » «لفت فرس‪. ۷۲۱٩ ‎‬‬
32603:      ‫کزآن مزاح ذخیره‌است رزین مزاج سپار»‪-‬‬                ‫بهاله جوبد برحالخوش وهمت خوش‬
32610:                ‫مپرده زبر پای اسر سپارا“ ‪.‬‬            ‫از آن جان توز لختی خون رز ده‬
32613:      ‫‪ - ۱‬مراداسم فاعل است ‪ .‬رك ‪ :‬سیاردن » سپردن‪+‬‬                ‫‪ :‬سپاردن » سپردن‪.‬‬   ‫رك‬    ‫®‬
32661:   ‫زندمغان کجا رسدیر ورق‌سپاره‌ای ؟!‬                ‫‪- ۴‬هرسقطی‌بمپد تولاف‌هنر زندولی‬     ‫‪-‬رك‪ :‬سارو‪.۵‬‬       ‫‪۱‬‬
32680:       ‫‪ #‬سپاردن ‪ -‬بکر اول و فتح پنجم مخفف اسپاردن (ه‪.‬م‪ ).‬؛ پهلوی ‪021۳205208‬‬
32742:      ‫‪ _¥‬از‪:‬سیر(رك‪:‬سیار) ‪ +‬دن (یسوندمصدری) رك‪:‬سپاردن ‪ ۰‬اسیاردن»سبردن‪‎.‬‬             ‫‪ - ۷‬رکه‪:‬سیردن‪.‬‬
```


## [2026-09-14T02:30:08.867Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 30686 30706 31095 32601 32680; do echo \"--- line $L ---\"; awk -v L=$L 'NR<=L && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' BQT_v2_pages.txt; done"
}
```


## [2026-09-14T02:30:09.482Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-14T02:30:09.970Z] TOOL RESULT

```
--- line 30686 ---
: 
--- line 30706 ---
: 
--- line 31095 ---
: 
--- line 32601 ---
: 
--- line 32680 ---
:
```


### [2026-09-14T02:30:10.031Z] TOOL RESULT

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


## [2026-09-14T02:30:12.643Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb; python3 tools/ref_page.py BQT:1024 --image 2>&1 | head -60"
}
```


## [2026-09-14T02:30:13.237Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb; python3 tools/ref_page.py BQT:1085 --image 2>&1 | head -60"
}
```


### [2026-09-14T02:30:14.028Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/ref_page.py': [Errno 2] No such file or directory
```


### [2026-09-14T02:30:15.161Z] TOOL RESULT

```
python3: can't open file '/home/sfmqrb/tools/ref_page.py': [Errno 2] No such file or directory
```


## [2026-09-14T02:30:17.121Z] TOOL CALL #22: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1024 --image 2>&1 | head -70"
}
```


### [2026-09-14T02:30:18.100Z] TOOL RESULT

```
no scan of BQT covers printed page 1024 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:30:22.782Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" BQT_v2_pages.txt | head -5; echo \"---\"; head -3 BQT_v2_pages.txt; echo \"=== formfeeds ===\"; head -30706 BQT_v2_pages.txt | tr -cd '\\f' | wc -c; head -32601 BQT_v2_pages.txt | tr -cd '\\f' | wc -c; echo \"=== total ff ===\"; tr -cd '\\f' < BQT_v2_pages.txt | wc -c; wc -l BQT_v2_pages.txt"
}
```


### [2026-09-14T02:30:24.112Z] TOOL RESULT

```
---
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
=== formfeeds ===
515
547
=== total ff ===
683
41070 BQT_v2_pages.txt
```


## [2026-09-14T02:30:27.242Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:30:28.893Z] TOOL RESULT

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


## [2026-09-14T02:30:39.993Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 30686 30706 31095 28827 32601 32610; do printf \"line %s -> leaf %s\\n\" $L \"$(head -$L BQT_v2_pages.txt | tr -cd '\\f' | wc -c)\"; done"
}
```


### [2026-09-14T02:30:41.095Z] TOOL RESULT

```
line 30686 -> leaf 515
line 30706 -> leaf 515
line 31095 -> leaf 522
line 28827 -> leaf 486
line 32601 -> leaf 547
line 32610 -> leaf 547
```


## [2026-09-14T02:30:46.141Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==485 || NR==486 || NR==487' BQT_v2_pages.txt | sed -n '1,200p'"
}
```


### [2026-09-14T02:30:47.228Z] TOOL RESULT

```
                                              ‫بیان نهم‬
                ‫أت‬     ‫نقطه دار با غىن نقطه دار مشتمل در ست‬                               ‫دررای‬


                        ‫ات‬   ‫وضم رابع هم اه‬           ‫رغار = بروزن بهار ‪ ۰‬به‌عنی زهین‬
                                                      ‫و طمام را‬     ‫لماك باشد ‪٩‬‏ ‪ -‬و لوعی از خوردنی‬
‫رغاره ‪ -‬بر وزن شراره ‪ .‬بان ( ‪) ۱‬‬
‫و‬    ‫و ارزن باشد ‪ - 9‬و بمعنی گاوری‬         ‫کاوری‬      ‫فيز گویند ‪ -‬و بمهء‌نی سختی و راج و محنت‌هم‬

‫ارزن هم آمده است ‪ -‬و گلگونه و غازه زناترا‬             ‫که زنگ بهم رسانیده‬              ‫چز‬    ‫و هر‬       ‫‪۱‬‬   ‫هت‬
                                                       ‫ویمعدی‬     ‫ویره‪-‬‬
                                                                      ‫آنه و شمتیر غ‬               ‫باشد ‪ ۱‬هجو‬
 ‫نیز گویند؛وبه‌عنی‌اول با زای لذطه دار هم‌هست‬
                                                                    ‫فرباد و فغان حم آمده ای ‪۰ ۳‬‬
                          ‫که بروزن ملازه باشد‪.‬‬
                                                      ‫رغار چه ‪ ۱‬بروزن نغارچه ‪ .‬کیاهی‬
‫رغال = بفتح‌اول بروزن مغاك »شاج‬
                                                       ‫است بهاری و باسرکه خورند بفایت لذین است‬
                      ‫درخت انکور زا گوند ‪#.‬‬
                                                       ‫و آنرا بعربی رجل الفراب خوانند چه شداحتی‬
‫زغاو ‪ ۲‬د بنتح اول و الی بالف‬                          ‫بیای کلاغ دارد و بخ آن فولاج را نافماست‪.‬‬
    ‫کشد‪ .‬و بواو زده‪ .‬زن فاحشه وفحبه رگاوشد‬            ‫رغار کرم ک‪۳‬ر‪-‬می‌است که آنرا‬
    ‫ریسی‬
       ‫ازا‬
         ‫و قحبه خاله را گیفزته اند » وفبا‬
                                                       ‫خراطین و امعاء الارش کونند » و آن کرم‬
                                    ‫هم امده است ‪.‬‬
                                                       ‫سرخیاست که در ميان کل هرم مکونب‌شود‬
 ‫اریر بابای ابجد بر وزن جعفر »مرو‬                               ‫مارپبغهابی درد کوش را نافع است ‪.‬‬
                                                                                               ‫ب‬
‫ننی باشد دوایی‬    ‫ر‪.‬سوتآی‬‫باند ‪۸‬‬     ‫ور‬‫کید‬
                                        ‫سف‬             ‫رغارو = بفتح اول و رابع بر وزن‬
         ‫که اکثر امراض پلغمیرا نافع است ‪.‬‬             ‫روارو ‪ ,‬خانهةٌ فواحش و قحه خاله را گونند ؛‬

                                                                        ‫‪۰‬‬   ‫نام )‪(۱‬‬   ‫‪:‬‬    ‫چش‬    ‫(‪)۱‬‬



                                      ‫برآورده بود » کاعر گوید ؛‬    ‫زمن لمناك وزنگ‬               ‫‪0-۰‬‬

               ‫زمن داده مرایشان را زغارا >‬                     ‫توشان زیر زمن‌فرحوده کر دی‬
    ‫*لفت فرس ‪۱۵۱٩‬‏ ‪.‬‬
    ‫از ‪ :‬زغاز (زمن نمناك) ‪ +‬کرم ؛ رك‪ :‬چپار مقاله‬           ‫‪۴‬‬                ‫= زعاره (ه ع‪).‬‬         ‫‪۳‬‬

                                                    ‫رك ‪ :‬ژغار ‪:‬‬     ‫‪۴‬‬             ‫چاپ نگارنده ص ‪. 6۱‬‬
         ‫منجيك‌ترمذی‬      ‫ماند بزغار و در کنده ری‬                 ‫خانة احمدطی‬         ‫‪۰‬‬      ‫از قحیه و‬

     ‫«لفت فرس ‪. 4۰ ۶۲‬‬
                                                                ‫= زعاله (ه‪.‬م‪).‬‬            ‫=غارم‬
                                                                                              ‫‪ ۵‬ز‬
                                            ‫برشکر (‪-‬کنه ‪ -‬دهخدا) من‌نکك تك‬                 ‫بزن دست‬
     ‫‪۷۳4٩‬‏ ‪.‬‬    ‫‪ ۵‬لفترس‬         ‫‪.‬‬     ‫لرو‬
                                        ‫بدامپ‬
                                            ‫چنان چون زغاره پز‬
     ‫=غار (ه‪.‬م‪ ).‬ورك ‪ :‬زغارو ‪.‬‬
                             ‫‪ ۷‬ز‬              ‫ازغ » آزغ » آژغ » زخاره ‪.‬‬           ‫‪:‬قایزع‬
                                                                                       ‫‪- ۱‬‬
                                                      ‫=‪ ۵۵۱۲۵‬لك ‪۲‬ص ‪. ۲۱۲‬‬ ‫‪۳ ۸‬‬
     ‫(برهان اطع‪)۴۳۱‬‬                            ‫‪.‬ك‪ :‬زکال ‪.‬‬
                                                        ‫ل ر‬ ‫=ز‬‫کزا‬
                                                                ‫٭غال ‪ -‬جم او‬
                                                                           ‫ر‬

 ‫زفیر‬                                                                                                    ‫—‬   ‫هن‬       ‫مب‬




                                  ‫‪.‬‬    ‫‪۴‬‬   ‫ات‬   ‫صاه‬
                                                          ‫قمر » نام دختر لوط‬                    ‫رو=زن‬
                                                                                                    ‫ربعر‬
‫زغناد = بن‌اول و نون بالف کشید‪.‬‬
‫بروزن کرلزوارن»ای را کوبند‪ .‬وآن کیاهی‬                     ‫باو‪ .‬گوبند چون آن خشك شود علامت قدامت‬
            ‫باشد که چزها بدان رنگك کنند ‪.‬‬                 ‫است و دجال ظہور کند ‪ -‬و طعام و خوردلی‌را‬
‫‪٠‬‏ از جای‬   ‫سمند‬   ‫بروزن‬      ‫‪۳‬‬       ‫رغند‬                                                            ‫لىز گفته اند ‪.‬‬

‫برجستن باشد بر مثال آهو ‪ -‬و بمعنی آواز و‬                  ‫‪۰‬‬
                                                                   ‫‪E‬‬
                                                                   ‫س‬          ‫ورن‬    ‫بر‬    ‫ت‬
                                                                                                  ‫‪:‬غ‪‎‬‬
                                                                                                  ‫رعر اس‬
‫بلئد هم آهفه است چه زغند زدن فرباد‬
                                   ‫صدای‬
                                                              ‫ریزهای پوست باشد که پوستین دوزان بدور‬
‫کردن را کویند ‏ و آواز میاه کوش و بوز را‬                                                                         ‫انداز ند ‪.‬‬
                                  ‫یز کفته اند ‪.‬‬                                                  ‫‪۲۹‬‬          ‫‪۰‬‬    ‫‪۰‬‬



                                                          ‫رغر یماش ؟ = بفتح اول و سکون‬
‫‪ - ۲‬بروزن پلنکه» بر جتن‬               ‫رغنگ‬
                                                          ‫م بالف کشیده‬
                                                                     ‫مدهی و‬
                                                                          ‫ثالی و الث بتحتالی رس‬
 ‫کلو باشد که بعربی فواق‪ ,‬کویند و‪۷‬ب‪-‬معتی‬                   ‫است که‬            ‫شین نقطه دار زده » بمعنی زغراش‬                 ‫و‬

 ‫لمحه هم آمده است بکقهدر بچكشم زدن‬                            ‫بدور‬    ‫خرده (‪ )۱‬ریزهای پوستین باشد که‬
                                             ‫باشد ‪.‬‬                                                              ‫انداز ند ‪.‬‬
 ‫رغو ه ‪ -‬بفتح اول و ثالی بواو‬
                                                              ‫رغگك۔ بقتح اول و ثالی کواف‌فارسی‬
‫رحو‪۰‬هة رسمان خام‬    ‫کتو‬
                      ‫رسیده و فوقالی مف‬
‫بیچیده شود ‪ ,‬و بجای فوقالی‬            ‫که بر دوک‬
                                                              ‫بروزن هوسك »جتن کلو باشد ؛ و آثرابعربی‬
                                                                                                       ‫فواق کونند ‪.‬‬
‫نون همبنظر آمده است ‪ -‬و مخفف زاغونه هم‬
                           ‫اشوره باشد ‪.‬‬
                                      ‫که‬‫ه«ست م‬                ‫کون‬     ‫و فتح الی و‬          ‫امول‬
                                                                                              ‫رعم هه ن‬
 ‫رعیكه = بفتح اول بر وزن چکیده ‪.‬‬                                      ‫هیم » به‌عنی زور توعدی و زیادتی‌باشد ‪.‬‬
                   ‫باشد ‪.‬‬   ‫یمعتی اقثرده و فشارده‬
                                                              ‫‪ ۰‬کوشت رباو‬            ‫چمن‬        ‫رو=زن‬
                                                                                                    ‫بعن‬
                                                                                                      ‫ر‬
‫بر وزن شعیر » تخم کتادرا‬          ‫ز عبر ‪-‬‬                     ‫‪ ۰‬گونند ششماه ار وششماه ماده‬              ‫‪,‬غلیواج باشد؟‬


‫کویند ‪ -‬و لوعی از طعام هم هست ؛ و بمعتی‬                        ‫است » و بعضی کویند یکال نر و کال‬
                                                                   ‫کهنجشك‬
                                                                        ‫نک‬‫غاند‬
                                                                             ‫زته‌‬
                                                                                ‫بدع‪.‬ضی کف‬
                                                                                        ‫وباش‬
                                                                                           ‫ماده می‬



                                                                            ‫‪«< :‬ورده ‌‬     ‫چش‬    ‫)‪ (۱‬جك‬


   ‫‪ - ۴‬از ‪00‬ع‪ .92‬از ‪020۳82‬‬                       ‫‪.‬‬    ‫رك‪ :‬زغراش‬       ‫؟ ‏‬             ‫‪ - ۱‬رك‪:‬زغره‌اش‪.‬‬
                                                              ‫در‬     ‫مر کزی ۾‬       ‫رك ‪ ۱‬هذینگه ‪ :‬دولغت آسای‬

         ‫‪Philological Society. Hertford 1946 , ۵ . 159, note 1 ۰‬‬
   ‫‪97‎ 10۰ ۰‬و ‪BSOS., X,‬‬                                          ‫ورك ‪:‬‬
             ‫_زغن وخاد (هم‪ ).‬مرخ گوشت ریای بود ‪ .‬رود کی (سمرقندی) کوبد ِ‬
                                                                       ‫‪« ۳‬‬

        ‫ماچو صموه مرکهبرسان زغن؟‪.‬‬                                    ‫جمله صبد ابن چهانيم ای پسر‬
   ‫«لفت فری ‪۱۹۳٩‬‏ ‪.‬‬
                            ‫‪ = ۹‬ژفنکه «لفت لامه» ‪.‬‬                    ‫ژغند(ه م‪۰ )۰‬‬        ‫® ‪ -‬اسم صوت =‬

                                       ‫رك ‪ :‬زعیر ‪.‬‬      ‫‪- ۸‬‬                 ‫رك ‪ :‬لفت فری ‪۹۹۲۰‬‬                ‫‪۲‬‬

                                                  ‫يان دهم‬
                          ‫در زای نقطه دار بافا مشتمل برده لغت‬

 ‫سياه و‬   ‫چویآزنیست‬
                  ‫® »‬             ‫شد‬
                                   ‫ایر‬
                                     ‫بزق‬
                                       ‫ا‬        ‫نوعی‬        ‫زقاك ‪ -‬بفتح اول بروزن هلاك ‪ ۰‬ابر‬
  ‫چبنده که از درخت صنوبر حاصل شود وبرس‬                                                 ‫ند ‪۰‬‬
                                                                                          ‫وهیرا‬
                                                                                              ‫باگرند‬
 ‫عرمی لز بکسر اول‬         ‫ور‬
                           ‫کجلان چ‌بانند » د‬                 ‫زفان ‪ ۱‬ا‪-‬بوال مضموم» زبانرا کویند‬
 ‫همين معنی دارده وآن سه‌نوع است ‪ :‬یکی زفت‬                                     ‫و بعربی لخاونانند ‪. ۴‬‬
 ‫ر فا نه ‪ = ۴‬بروزن ومعتی زبانهباشد رومی و آن براق وصاف واملی میباشد و ازروم‬
  ‫هیآ وزلد و بعضی گوشد همی زفت است هاش‬
                                                            ‫که زبانة آنش ‪ -‬زوبانة چوب اومثال آن‬
 ‫زفت تر وآن‬      ‫برومی شهرت دارد » و دبگری‬                  ‫است » و آن چیزی است که در مان شاهین‬
 ‫آیکی و روان میداشد و آنرا درمرهمها بکار برند‬                                            ‫ترازو میباشد ‪.‬‬
‫وآن از فبیل قیراست و از الواع صتوبر کیرند‬                    ‫ز قت» بنتح اول و سکون ثالی وفوفالی‪:‬‬
 ‫ونوع سيم زفت خشك است وآلرا بیشترازینبوت‬
                                                             ‫بمعنی درشت وفربه باشد و گنده و سطبر ‪- ۴‬‬
 ‫ورز گیرند که بوتهٌ کبر و صنوبر لر باشد و‬
                                        ‫ا‬                   ‫وسفت وهنگفت را لیز کفته‌اند ‪ -‬و بمعنی پر‬
 ‫آن گونند که باری ندارد »‬              ‫صنویر نبرجهت‬
                                                            ‫ومالامال هم آمده‌است و طعم تیز و هز نیز را‬
                  ‫ومطلق آکنرم وخشك‌است ‪.‬‬                    ‫بگزد ‪ -‬و م اول بععنی‬       ‫را‬
                                                                                        ‫ادنکه‬
                                                                                            ‫بوبن‬
                                                                                               ‫ززک‬
                                                                                                 ‫ای‬
 ‫فر د بفتح اول ثوالی بروزن سفر »‬                            ‫بخیل و مسك ولتم ‪ -‬و گرفته و ترش روی و‬
 ‫دهانرا گوبند ‪ ۷‬وبعربی‌فم خوانند‪ -‬و کلج‌دهافرا‬                 ‫م‬
                                                               ‫‪-‬و‬‫طدع‬
                                                                   ‫ستیزه خوی و خشوت کناده باش‬
  ‫ندان‬
     ‫دد‬‫هک‌ون‬
           ‫هم گفته‌اند و استخوالی را نکیز‬                   ‫ولذت زمخت را نز گویند مانند مازو و هلله‬
 ‫ازآن روید و برآ بد‪ ۲‬؛ و بقتح اول و سکون‬                     ‫اومثالآن وبعربی عفص خوانند ‪ -‬وبکراول‬

  ‫چدم بررحوار بون‌نهاد (عیسی) وزفان‬         ‫‪9 ۳‬‬
                                                                       ‫‪ = ۱‬ربان («م‪ ).‬ز‬
                                                            ‫>وان (ح م‪.).‬‬
   ‫زباه‬     ‫‪۴‬‬             ‫؟‪.‬‬   ‫ص‪۸6‬‬     ‫«انجیل فارسی‬    ‫‪۴:‬‬
                                                            ‫بگشاد وبدیشان تعلیم و پندمی داد وم گفت‬
                                                                                ‫( م( = زوایه (ه‪.‬م‪: ).‬‬
          ‫وآنچ مصثوقة اورادل و دنده شکت‬                        ‫‪ ۴‬اینهمه زاری عاشق بنمود وننهفت‬
          ‫شدش کالبد از زاری وز فرقت زفت‬                        ‫ساعتی با اولششت و یاسود نوضفت‬
          ‫بفتاده براه ‪.‬‬        ‫صیناد‬     ‫معود‬   ‫شاه‬            ‫اینچنین سنگدلی ‪.‬بیحق‌وبیحرمت‌جفت‬
   ‫‪ ۶‬مذوچهری دامفالی ‪۶۵۱٩‬‏ ‪.‬‬
  ‫بعضی نرا از بونالی ‪( 5001/5۸‬فیر) ماخوذ‬     ‫‪( 100 = ۵‬فر) «لك ‪ ۲‬ص‪۲۱۲‬‬
   ‫‪ - ۱‬اوستا ‪( ۲2122 -‬کلو)‪ .‬پهلوی ‪« 72122‬اسشق ‪۳٩5+.‬‏ هوبشمان‬    ‫دالته‌اند «نفی) ‪.‬‬
   ‫و ‪ 82122‬فارسی را پامان‌کریت ‪( 102‬گرفتن » بایوزه گرفتن ) » و ‪29-‬حاصطهز‬                           ‫‪7‬‬
  ‫چه‬   ‫مراد فك است»‬   ‫‪-‬‬    ‫‪۷‬‬                ‫»لو ) متعاق میداند «هوبشمان ‪. ۳+4‬‬
                                                                            ‫( دندان » اسنان ک‬
   ‫«* زفر زیرین» فك اسفل است و «زفر زبرین» فك اءلی ‪ « :‬هر حیوالی بوقت خاییدن زفرزبرین‬
```


## [2026-09-14T02:31:08.048Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la | grep -i \"BQT\"; ls incoming/BQT/ 2>/dev/null; ls ocr/ 2>/dev/null | head"
}
```


### [2026-09-14T02:31:08.157Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r--  1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r--  1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-14T02:31:19.812Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; for n in 486; do curl -s -L -o bqt469-n$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n$n.jpg\" ; file bqt469-n$n.jpg; ls -la bqt469-n$n.jpg; done"
}
```


### [2026-09-14T02:31:24.430Z] TOOL RESULT

```
bqt469-n486.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 620205 Sep 13 22:31 bqt469-n486.jpg
```


## [2026-09-14T02:31:29.397Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt469-n486.jpg')\nw,h=im.size\nim.crop((0,int(h*0.70),w,h)).resize((int(w*0.7),int(h*0.30*0.7))).save('bqt469-n486-bottom.png')\nim.crop((0,0,w,int(h*0.15))).save('bqt469-n486-top.png')\nprint(im.size)\""
}
```


### [2026-09-14T02:31:31.532Z] TOOL RESULT

```
(2569, 3970)
```


## [2026-09-14T02:31:33.348Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n486-bottom.png"
}
```


### [2026-09-14T02:31:33.366Z] TOOL RESULT

```

```


## [2026-09-14T02:31:44.274Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n486-top.png"
}
```


### [2026-09-14T02:31:44.398Z] TOOL RESULT

```

```


## [2026-09-14T02:31:44.395Z] INPUT

[Image: original 2569x595, displayed at 2000x463. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:32:00.205Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==548' BQT_v2_pages.txt | tail -40"
}
```


### [2026-09-14T02:32:01.271Z] TOOL RESULT

```
   ‫ندووا‬
       ‫آارن‬
          ‫حووضیکه درآن شیر انگور بفش‬                 ‫سار = بضم اولبروزن دچار ‪,‬آهن‌جفت‬
 ‫بعربی معصر خوانند ‪ - ۴‬و مطلق ظروف واوالی‬           ‫راکوبند وآن آهنی باشد سرتیز که زمین‌بآن‬
 ‫راکوبند عموماً » وظرفیکه درآن الگور کرده‬
                                                     ‫شیار کنند ‪ - ۴‬و بکسر اول‪,‬اسباب و مایحتاج‬
‫ازجابی بجایی برند خصوصاً ؛ و باين ممالی تم‬
‫ده امت خصوصاً آلات وادوات‌خانه ‪۴‬‬
                               ‫اآولمهم‬               ‫وآلات وادوات خاله باشد ازهرنوعی ‪- ۴‬وچرخی‬
          ‫فاعل سپردن ‪۷‬‬   ‫امر بپردن © _ و‬     ‫‪ -‬و‬
                                                     ‫را پگیوزنند که بدان شیر انکور گیرند ‪- ۴‬‬

                                                                      ‫)‪ (۱‬چك ‪ :‬بقتح حا ‪.‬‬


  ‫‪-‬‬       ‫‪ ( 414010‬دستهٌ خیش ) » از رة‪‎‬‬   ‫هندی باستان ‪-‬‬    ‫‪- ۴‬‬           ‫‪.‬‬   ‫رك‪ :‬سوی‬      ‫‪٩‬‬

  ‫‪( 1205 - 2۵۰‬بازکردن)؛سر یکلی]‪( 15‬خیش) «اسشق ‪«:۹۹۹6‬سپار ‪,‬کارآه نکه زمین‪‎‬‬
            ‫‪« - ۴‬سپار آلت خاله بود ‪ .‬فرخی (سیمتالی) کفت‪: ‎‬‬             ‫شکافند » «لفت فرس‪. ۷۲۱٩ ‎‬‬
      ‫کزآن مزاح ذخیره‌است رزین مزاج سپار»‪-‬‬                ‫بهاله جوبد برحالخوش وهمت خوش‬
   ‫« لفت فری ‪۵۵۱٩‬‏ ‪.‬‬
                                               ‫‪ - ۴‬ارزبشة ‪ ۲9۳8‬بمعنیلکدمال کردن ‪:‬‬
                ‫‪Henning,‬‬     ‫‪Sogdian‬‬      ‫‪loan - words..., BSOS,X,1I, p.‬‬                  ‫‏‪۰‬‬
                   ‫‪۵‬پار ‪ .‬بزبان ماوراهالنهر چرخشت بود و بعرمی هعصر > رودکی(سمرقندی) گفت ‪:‬‬
                                                                                        ‫س‬

                ‫مپرده زبر پای اسر سپارا“ ‪.‬‬            ‫از آن جان توز لختی خون رز ده‬
      ‫‪.‬‬     ‫« لت فرس ‪۷۲۱‬‬

      ‫‪ - ۱‬مراداسم فاعل است ‪ .‬رك ‪ :‬سیاردن » سپردن‪+‬‬                ‫‪ :‬سپاردن » سپردن‪.‬‬   ‫رك‬    ‫®‬

   ‫‪2‬ی‪ . 1606‬سطنزی ‪1101688‬‬    ‫‪5‬رن‬
                               ‫‪ #‬سیل ‪ -‬بکراول »کیلکی ‪» 162۹‬فریزندی وب‬
   ‫‪۱. ۰‬ص ‪ > ۸۸۲‬؛ سمنالی اأتاق‪ . 9‬سنگری و سرخه‌یی ولاسگردی ‪ . 11088‬شهمیرزادی‬
   ‫تاه « ك ‪۲ .‬ص ‪ ۸۱+‬؛ مأخون از «سبلقه (عر) م؛وحابی که بر زبر لب بالاروبد » یروت‬
                                                                             ‫‪.‬‬   ‫ملت‪).‬‬
                                                                                     ‫‪.‬سب‬
                                                                                       ‫ه»‬‫(رب‬
                                                                                           ‫شا‬
```


## [2026-09-14T02:32:03.223Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; curl -s -L -o bqt469-n547.jpg \"https://archive.org/download/borhan-ghate-v2/page/n547.jpg\"; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt469-n547.jpg'); w,h=im.size; print(im.size)\nim.crop((0,int(h*0.72),w,h)).save('bqt469-n547-bottom.png')\nim.crop((0,0,w,int(h*0.10))).save('bqt469-n547-top.png')\""
}
```


### [2026-09-14T02:32:06.385Z] TOOL RESULT

```
(2569, 3970)
```


## [2026-09-14T02:32:16.025Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n547-bottom.png"
}
```


### [2026-09-14T02:32:16.264Z] TOOL RESULT

```

```


## [2026-09-14T02:32:16.259Z] INPUT

[Image: original 2569x1112, displayed at 2000x866. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:32:21.447Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt469-n547.jpg'); w,h=im.size\nim.crop((0,int(h*0.58),w,int(h*0.76))).save('bqt469-n547-mid.png')\""
}
```


### [2026-09-14T02:32:22.759Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:32:25.074Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n547-mid.png"
}
```


### [2026-09-14T02:32:25.240Z] TOOL RESULT

```

```


## [2026-09-14T02:32:25.232Z] INPUT

[Image: original 2569x715, displayed at 2000x557. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:32:30.186Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt469-n547.jpg'); w,h=im.size\nim.crop((0,int(h*0.52),w,int(h*0.61))).save('bqt469-n547-fn2.png')\""
}
```


### [2026-09-14T02:32:31.721Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:32:33.913Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n547-fn2.png"
}
```


### [2026-09-14T02:32:34.013Z] TOOL RESULT

```

```


## [2026-09-14T02:32:34.011Z] INPUT

[Image: original 2569x357, displayed at 2000x278. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:32:44.378Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n547-top.png"
}
```


### [2026-09-14T02:32:44.515Z] TOOL RESULT

```

```


## [2026-09-14T02:32:44.512Z] INPUT

[Image: original 2569x397, displayed at 2000x309. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:32:47.640Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt469-n547.jpg'); w,h=im.size\nim.crop((0,int(h*0.09),w,int(h*0.16))).save('bqt469-n547-hdr.png')\""
}
```


### [2026-09-14T02:32:48.887Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:32:51.247Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt469-n547-hdr.png"
}
```


### [2026-09-14T02:32:51.318Z] TOOL RESULT

```

```


## [2026-09-14T02:32:51.316Z] INPUT

[Image: original 2569x278, displayed at 2000x216. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-14T02:33:04.892Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf 176/177 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==177' HRN.txt | head -6; echo \"...end...\"; awk 'BEGIN{RS=\"\\f\"} NR==177' HRN.txt | tail -4; echo \"=== MON asfalt ===\"; grep -n \"آسفالت\" MON_part1.txt | head -10"
}
```


### [2026-09-14T02:33:05.880Z] TOOL RESULT

```
=== HRN leaf 176/177 head ===
— 155 —
Also zu aw. [/^spas'y spast/eiti *spälien'? Sehr un-
sicher, Hübschmann, Armen. Stud., S. 50, No. 257^).
699. »ipah *Heer , sipeh^ ispeh\hed (arab. isbah[hu(/), jüd.-
pers. HNDID (Is. 13, 4).
ap. Ta/ma]späda- ; aw. spaöa- *Heer ; phlv. späh,
...end...
ursprünglicher a, 6 in u ~ veranlasst, KZ. 32, 572 folg. dem Altpersischen
den r- Vokal abzusprechen. Ich möchte jetzt jedoch an dieser Meinung
nicht mehr festhalten, zumal da auch das Beläcl noch deutliche Spuren
eines einstigen Besitzes des r- Vokals aufweist.
=== MON asfalt ===
46568:که آسفالت نشده؛ راه خاکی. (تد. .عم. 0( پیاده 
86806:مخلوط شوند تولید آسفالت کنند. درشتی
```


## [2026-09-14T02:33:06.491Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB sipar ===\"; grep -n -i \"sipar\\|ispar\" HUB.txt | head -10; echo \"=== PHD spar ===\"; grep -n \"spar\" PHD.txt | head -20; echo \"=== NYB spar ===\"; grep -n \"spar\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:33:06.624Z] TOOL RESULT

```
=== HUB sipar ===
355:78. T^p.isparud „ein kleiner Vogel" (vom Sperling unter-
2559:dem Praesens sipdram (und siparam Sal. Shuk.
2571:sipari = phi. *spartk; phi. spur = ap. *spma-; arm*
5261:*Thiir', 2!ar 'Gold', *6reis', ^ard gelb*, sipar *Schild', sar *Kopf ,
6053:c) Vorschlag von i in: isparud *ein kleiner Vogel'
6055:(siehe oben); ispar {sipar) 'Schild*, afgh. spar, phi. spar;
6056:isparl (= sipart) Vollendet', phi. spurlk (oben p. 73) ; isped
6075:siparam ubergebe* (inf. supurdan), Wrzl. spar; sipar 'Schild*—
6077:spaeta- ; sitara 'Stern' = zd. star- ; siparl Vollendet*, paz. spur
6100:siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
=== PHD spar ===
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
386:e--rób [-lwp | N jārē(b)] broom. geän [HY A < А hy’; yn! | M gy’n, N jan] soul, ghost. ~ kandan: give up the ghost; moment of death. ~-abespar [-^5sp?! | N jān-sipār] reckless, desperate; devoted. ~ig [-yk! | M -yg] spiritual; vital. | ~war [-wl | (P -br), N jánwar] animate; animal.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
1397:core mādayān, uruspar.
1578:desperate gyan-abespar.
1594:devoted gyan-abespar.
1801:essence ¢éih, čihr(ag), gēhr(ag), mādag, mādayān, xwadih, uruspar.
2355:idolater uzdésparist. i
2471:intestine(s) ródig, uruspar.
3629:shield magind, spar.
4335:womb a$kamb(ag), aškom(b), burdār, gabr, grāb, pusyān, uruspar, zahār.
4773:spéd spēdag spēdbāg spenāg spóxtan spandan Spandarmad sabuk spul spurrigih spurrig spurdan spūz spēz- spinjānagīh spozgar spūzišn sabz spazg spazgīh spar spar- sprahm sprahmag
=== NYB spar ===
435:anä-vinast [ZK. "HRN. ?wnst'] uncor- rupted, guiltless 64?” sq. — The neg. pref. anā- characteristic of the NW languages + vinast, SW form (with -st < -št) of vi + Av. (1055 sg.) nas- (v. vinds, vinàsi- tan), MPrth wnštg ‘destroyed’ (MHC). an- of anü- was written ZK, which was then explained by the other ideogr. for an: CHEN, v.s.v. lan. — Paz. a-gunast ‘un- polluted, transparent, clear’ (SGV V, 5).
593:api-spartan ['psp'ltn'], often with bé: to hand over (6 to) 147. 3213; to consign to, to lay down in (6) 111°; to give up (one’s honour) 4?!; to give (one’s life, rad for) 1119; to commit (oneself to death)
595:api-spartan
596:113-6, (another to death and torment) 7721, — Olr *upa-spar- and apa-spar-, and then *upa- remodelled to api- (v. apa-): MPrth ’byspwrd, pres. ?bysp?r-, Ghilain 75; Arm. lw. apspar-em (= aps- spar- < api-spar-); Paz. awa-spārdan; NP only simplex swpurdan sipdr- ‘to entrust'.
702:asp-rēs ['splys] race-course 16’. — Arm. lw. asparēs, -rēz, Syr ’aspresa, NP asp- raz; Telegdi 255.
973:. 6 kēft sar nišinend did not find foot- hold except if they perched 2018-19; 2115-16; 65?! (v. pätixsäi); — b) in frame preposi- tions: bē... ēnyā, v. Enya; — be... tài: be man tài an kas nē mand estet no one except mehas been spared 15?’ ; be Zartuxšt
1585:frče [plyc] a surplus, or a remainder, a rest: martom (indir. obj.) — pat nēvakē- keh <i> hàn kunēnd i-šan andar gehän apäyisniktar veh dit to mankind they (the gods) will make a surplus above the felicity which in this world was seen by them as the most exquisite and the very best 10025-26 i. e., mankind will be given a felicity above the most exquisite and the very best felicity they experienced in this world. — Paz. fréz-, fréz- (v. next group) = BP /réc < *fraréc (haplology) < Olr *fra-raica- (from fra + ratk-, v. rertan), cf Skr prarecana- ‘surplus’, pra- reka- ‘abundance’, properly ‘what is pro- jecting’. To it belongs the vb. frčatan fréc- l. ‘to be over, to be left, after necessary expenses, as a gain or a rest’, 2. ‘to put aside what is surplus, to save’, or, ‘to increase by a surplus’. Cf (Paz.) ne neki frežašni . .. rà ‘not in order to add to the well-being’ SGV III, 24, Skr. v. subhasya visphitaye; har cé frēcēt hac all that is left of, or after BdA p. 1107 (plycyt' with the first y marked) = BdJ 397; PY 687; frčat ‘savings’ PVd. 379%. 1888 (comm.). Bthl., followed by others, read paréc- < *pari-raica-, identifying it with Sogd p’r’yc- ‘to leave, to abandon? (ZairWb 52; MIrM I, 14. II, 11.38 sq.) and adducing as a parallel Gr repuhehevujuevoc. However, the Paz. reading frēž is firm, unimpeachable and transparent, and as representing a living WIr tradition it 1s preferable to any reading based on Elr material (besides, Sogd p'r'yc- seems to
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
3471:spāh-pat [sp'hpt'] army leader, general, passim; pl. cas. obl. ~-dn 28. 1113; — 72 ~ twelve leaders, of the twelve signs of the zodiac 7718, 794; 7 ~ the seven planets 7712, 7916, — Arm. lw. from Prth sparapet < *späda-pati-, v.s. v. späh; NP sipahbad.
3482:spar [spl] shield 855. — Paz. spar, NP sipar.
```


## [2026-09-14T02:33:16.709Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:33:16.716Z] TOOL RESULT

```


```


## [2026-09-14T02:33:18.809Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB 6090-6105 ===\"; sed -n '6095,6105p' HUB.txt; echo \"=== HUB supar ===\"; grep -n \"supār\\|supar\\|Pflug\" HUB.txt | head -15; echo \"=== HRN Pflug/supar ===\"; grep -n -i \"Pflug\\|supar\" HRN.txt | head -15"
}
```


### [2026-09-14T02:33:18.923Z] TOOL RESULT

```
=== HUB 6090-6105 ===
'Hahn*, xuros 'Larm', skr. kroc ; furod {firod) *hinunter', paz.
fro$, skr. pravdtd; ftiroxtan Verkaufen* aus fra-^-vaxs;
surod 'Gesang, Lied' = zd. sraota-; surudan (pr. sardyam)
singen', zd. srdvayeiti ; siiru {saru) 'Horn* = zd. srvd- ; surun
[surtfi] 'Hinterbacken*, bal. saren, zd.sraoni-; supurdan (pr.
siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
*Laus' (auch sipis u. s. w.) = zd. spis; supoxtan [sip^xtan)
'heraustreiben = paz. spuxtan, arm. spuzel : sutudan (sitdyam)
'loben*, zd. stw, sutor ^Ross' = zd. staora-; siitun Saiile*
= zd. stuna-; sunudan (sinavam) *horen' (auch sinldan, as^
=== HUB supar ===
2350:kratzen, glatten, rasieren*, rallum *Pflugreute', rast-
2727:*Pflug, *Ring', Tfeir und frz. 'sceau iibersetzt).
4725:*Pflug8terz*')r g. mdtk, arm. mad?; ydftan *erlangen* = paz.
6100:siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
6101:fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
6289:pand *Raute* H. 80, gospand Kleinvieh' H. 942 ; supar Tflug
7812:supurz 'Milz' = zd. spereza, skr. pllhan-; supar 'Pflug =
8083:vivad- (oben p. 104) ; amdj 'Pflugsterz , g. mCLtk, arm. mac (?);
9253:dkainf]^, arm. aluBs ; supar Tflug* = skr. phala-, afgh. spara
9514:xism Gl. and Ind. 68 = zd. aesma-; xEs, ka§. is, xis *Pflug*
=== HRN Pflug/supar ===
820:45. ätnäj 'Pflugsterz'.
3947:Pfluge befestigende Lederriemen' (H.-Sch.); bei. Jöy
4652:515. -^f^en (dialektisch yec) 'Pflug'.
4670:Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
5703:644. ^U", Praefix, w-2-, vergl. suparden (No. 697), siperT
6117:sar. spur 'Pflug .
6444:aw. \/saoi)' in sufrä- 'Pflug, die Geiger unter
6610:758. sTilT, snl 'Pflug* (unbelegt, nur im FS).
6612:'Pflug* zusammengebracht, was aber nicht vorkommt
```


## [2026-09-14T02:33:24.346Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '6106,6125p' HRN.txt; echo \"=== HUB 9245-9258 ===\"; sed -n '9248,9258p' HUB.txt; echo \"=== HUB 7808-7816 ===\"; sed -n '7808,7816p' HUB.txt"
}
```


### [2026-09-14T02:33:24.420Z] TOOL RESULT

```
LW. kuid. säriy z. B. kH\sän *öü; wie?', va]suna auf
diese Weise'; afy. San; bei. sang (236).
Np. -sä^) hat das auslautende n verloren, wie äsuid,
a (No. 52), senrjso (Käs. Z. zu 1. süh) u. a. ni. Gehört
np. 'äsan 'äsä gleich, ähnlich* auch hierher?
695. säf/e 'Schatten, Schutz'.
ai. chayd' 'Schatten'; plilv. sayak,
kurd. se^ si\ bei. säig, n. saJ (340); wa;^. LW. sayd,
sar. suyä,
696. supär Tflug .
ai. phdla- Tflugscliar*, zu l^phal-, splial- *aufreissen'.
sar. spur 'Pflug .
697. Hiipävden anvertrauen, übergeben*, jüd.-pers. p1N?10,
supiirden, sipäris (sifärls).
g. vaspartmün.
aw. tis-\- 2. l/'par-; phlv. avspärtan, avspurtan. (vd. 5
(77)), spiirtltan (AV.); ai. iid -{- "lA^par- 'hinüber-
führen', utpdrana- 'Übersetzen*; vergl. lat. portäre.
af/. späral übergeben'; kurd. sipärtin.
Die Etymologie stammt von de Lagarde, ist aber
=== HUB 9245-9258 ===
§ 155. Ap. r (= idg. r und I) = np. r, z. B. roz
*Tag* = ap. raudah-; vast recht, wahr = ap. rasta-; abr
*Wolke* = zd. awra- u. s. w.
Np. r = skr. 7: risk *Nisse' = skr. liksa^, afgh. rica,
osset. l^sk; robah *Fuchs* = phi. ropas, skr. Wpdga-, gr.
dkainf]^, arm. aluBs ; supar Tflug* = skr. phala-, afgh. spara
Tflugschar*.
Lautgruppen mit r.
§ 156. Ap. rn bleibt als rn oder wird assimilirt zu
rr, das zu r vereinfacht werden kann.
a) rn bleibt in: burna, barnd *Jungling', zd. apere-
=== HUB 7808-7816 ===
gleich behandelt, also zu s oder ^ wurden. Da nun letz-
teres im Np. durch h vertreten ist, fiihre ich np. mahl auf
ap. *ma&iya- zuriick.
f) Idg. sp und kh = iran. und ap. sp = np. $p:
supurz 'Milz' = zd. spereza, skr. pllhan-; supar 'Pflug =
skr. phala- ; asp Tferd' = zd. ap. aspa- u. s. w., vgl. oben
§ 71 und Horn Nr. 696—708. In sipis, supus u. s.w. 'Laus'
fur supus etc. = zd. spis ist das anlautende s an das aus-
lautende s assimilirt, vgl. sus Xunge aus *su$ (oben p. 80).
```


## [2026-09-14T02:33:38.012Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek ἄσφαλτος: is it from ἀ- + σφάλλω, or is it considered a loanword (Semitic / pre-Greek)? Quote Beekes or any cited authority verbatim. Also give the definition."
}
```


## [2026-09-14T02:33:40.425Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CF%86%CE%AC%CE%BB%CE%BB%CF%89",
 "prompt": "Give the full etymology and definitions of Ancient Greek σφάλλω (sphallō): what PIE root, what cognates (Sanskrit skhalate? Latin fallo?), and any note about Pokorny's (s)p(h)el- connection. Quote verbatim."
}
```


### [2026-09-14T02:33:44.416Z] TOOL RESULT

```
# Etymology of ἄσφαλτος

**Definition:** "asphalt, bitumen"

**Etymology - Two Competing Theories:**

The document presents two competing etymological accounts:

1. **Traditional derivation:** "Generally taken as deriving from ἀ- (a-, 'not') +‎ σφάλλω (sphállō, 'to fall, cast down'), under the assumption that it denoted the material that protects walls from tumbling down."

2. **Beekes's position:** "However, according to Beekes, the word is rather Pre-Greek."

The Beekes citation comes from his *Etymological Dictionary of Greek* (2010), though the document does not provide a verbatim quote from Beekes himself—only a reference noting his view that the term derives from a Pre-Greek substrate rather than from Greek morphological components.
```


### [2026-09-14T02:33:46.746Z] TOOL RESULT

```
# Etymology of Ancient Greek σφάλλω (sphallō)

**PIE Root:**
The word derives from Proto-Indo-European *"(s)gʷʰh₂el-" meaning "to stumble."

**Cognates:**
The entry lists several related words across Indo-European languages:

- Old Armenian: "սխալեմ" (sxalem, "to err")
- Sanskrit: "स्खलति" (skhalati, "to stumble")
- Latin: "fallō" (possibly related)

**Note on Pokorny:**
The provided content does not mention Pokorny or reference the root as "(s)p(h)el-". The etymology section simply states the PIE reconstruction as *"(s)gʷʰh₂el-" with the gloss "to stumble," citing Beekes' *Etymological Dictionary of Greek*.

**Meanings (Ancient Greek):**
Active voice forms include "to topple, overthrow," "to kill," and "to baffle." Passive voice forms mean "to be foiled," "to fall," and "to stagger."
```


## [2026-09-14T02:33:54.193Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/asphalt",
 "prompt": "Full etymology of asphalt: Middle English/Old French/Late Latin/Greek chain, dates, and the a- + sphallein explanation. Quote verbatim."
}
```


## [2026-09-14T02:33:56.691Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1",
 "prompt": "Give the Persian entry سپر (separ) 'shield': full etymology (Middle Persian, Proto-Iranian, Avestan, Sanskrit cognates), and any mention of Old Persian *spara- / sparabara or Avestan spāra-. Quote verbatim."
}
```


### [2026-09-14T02:33:59.517Z] TOOL RESULT

```
# Etymology of Asphalt

The word "asphalt" entered English in the early 14th century, originating from Late Latin *asphaltum*, which derived from Greek *asphaltos*.

## The Etymology Chain

The proposed Greek origin involves a negative prefix combined with a verb form: Greek *a-* (meaning "not") plus *\*sphaltos* (understood as a verbal adjective from *sphallein*, "to throw down"). As the source explains, this etymology was theorized "under the assumption that it denoted the material that protects walls from tumbling down," though scholars consider this explanation "weak."

An alternative theory suggests the word may derive from Semitic languages or another non-Greek source entirely.

## Modern Usage Shift

Originally referring to "hard, resinous mineral pitch found originally in Biblical lands," the meaning evolved significantly. In 1847, "asphalt" began describing a "paving composition of tar and gravel," which became the dominant modern sense. This new usage eventually displaced earlier English forms like *asphaltum* and *asphaltos*. The verb form, meaning "to cover with asphalt," emerged in 1872.
```


### [2026-09-14T02:34:02.827Z] TOOL RESULT

```
# Persian Etymology for سپر (sipar/separ)

Based on the Wiktionary entry provided, here is the Persian etymology:

**Full Etymology Chain:**
The word is inherited from Middle Persian *spl* (spar, "shield"), which derives from Old Persian *\*sparah*. The entry notes it is "akin to Old Armenian ասպար (aspar), an Iranian borrowing."

**Verbatim Quote:**
"Inherited from Middle Persian spl (spar, "shield"), from Old Persian *sparah. Akin to Old Armenian ասպար (aspar), an Iranian borrowing."

**Notable Limitation:**
The provided Wiktionary article does not include information about Proto-Iranian, Avestan cognates, Sanskrit cognates, or Old Persian spāra-/sparabara forms. The etymological section stops at Old Persian *sparah and mentions only the Armenian cognate relationship.
```


## [2026-09-14T02:34:09.312Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Schild\" BRT.txt | head -20"
}
```


### [2026-09-14T02:34:09.373Z] TOOL RESULT

```
4936:•  j.  ayö.v^raBra-  Adj.  (fem.  °rä-)  'mit metallenem  (eisernem)  Schild':  frava^ayö ..  ay5.xa<kä  ayö.saya  '%ra  Yt. /^.  45.
5481:*)  Vgl.  Yt.  5.  Ans  dem  Flus»  A,,  der  nach Yt.5.3  von  der  Höhe  Haiairya  mm  .See  Vcuru- iasa  tliesät  (doch  5.  90),  stammt  alles  Wasser der  Erde;  s.  auch  Bd.  12.  5,  13.  I,  5 f.  Die Göilin  A.  wird  als  ein  schönes  Mädchen  ge- dacht, von  dem  Yt.  5.  64,  78,  u6  IT.  eine  auf- (allig  ins  Einielne  gehende  Schilderung  geben. Vgl.  DsT.  ZA.  2.  316,  363,  wo  weitere  Litt.
9423:lat    mqm    mairyS    äkaiat    "darauf  er-  •  j.   kasyapa-    m.   'Schildkröte',    die    als
10001:*)  Kne  Schilderung  des  G.  und  seiner  Er- legung findet  sich  SEE.  iS.  37s ;  vgl.  »uch tonStackzlberg  IF.  4-  I49i    WZKM.  it.   239.
10736:tritt  Ai.  nur  wenig  hervor.  Die  Metalle  stehen unter  seinem  Schutz.  Bei  den  letzten  Dingen kämpft  er  nach  Bd.  jo.  29  mit  dem  Dämon Sautva.  Auf  Münien  erscheint  Sala-niar  (PAO- PHOPO,  PAOPHOAP;  s.  Stein  Or&BabRec. iSS^.  I59ff.)  als  Kriegsgott  mit  Helm,  Schild und  Speer.  Vgl.  im  Übrigen  Tikle  Godsdiensl' 2.  136,  JusTi  PrJ.  SS.  75.  JN.  GlrPh.  2.  637, femer  die  bei  DsT.  ZA,  2.  313  übersetite  Stelle des  GrBd.
11897:auf  diese  Weise',  zurückweisend;  a)  avavat kavaim  ^armd  ya%a  yat  .  .  us./ravayBit (sd.)  . .  f  asti  kavalm  ifarmS  %rä^nm  . . Yt.  ig.  6Bi  b)  als  Korrelat  von  iya^ 'wie':  s?rao^  ita  astü  .  .  hyaf  paour- vXm  f  ust3mfm(sd.)cyt  Y.  56.  i,  Vr.  g. 7.  c)  bei  elliptischer  Ausdrucksweise im  Sinn  von  'das  (Gesagte)  gilt  ,  .':  Aaea hä  vaxiat  [.  .]  mailyai  xsape  palrisacäiti t°  Aatna  t°  *ami.gäme  ".  .  das  gilt  im Winter,  das  im  Sommer"  N.ji;  48',  103Q); —  tat^giiniakva  %rigamlm  f  lkaesaAe{sA.) f  *vtkayehe  f  arüaAe  f  arikavanS  F. 2jb.  7)  wie  unser  schwach  toniges  (zeit- liches und  räumliches)  'da'  zur  Belebung einer  Schilderung  (usw.):  na  t°  para.- irihyeiti  avi  jqfnavS  raonqm  a  f  mirTy^m .tisvazaitcupa  tarn  kiArptm  fratauAaraiü \..3t°  msnyim  utvazaite  ,  .  avi  bar^i- navs  gairinam  . .  nä  f  frasusaUi  .  .  upa
14147:Et.?').  —  Pü.  (luV.  2):  drdpk  {Tranistr.), erl. :  ii  darl  ätaaret,  (zu  V.  /.  l) :  atanärai darimil,  erl.;  darim  5  darin  patioail  islel.  — >)  Wegen  JusTis  driwi-  EN.  (NB.  86)  s.  West SBE.  j.  132  No.  6.  —  ')  Cto.s  Hinwei*  auf ai.  dfmbhh-  (GGA.  iSgj.  400)  hilft  nicht  weiter. —  3)  zBed.  vgl.  At.  /?.  12,  wo  aianärai darim  lut  Schilderung  eines  häsilichen  Weibes verwendet  wird;  etwa  'voller  Mutter-  oder Pockenmale'.    S.  noch  'raeia-  No.  2.
22707:NB.  34a,  FoY  KZ.  3S-  Ö3  ('»childfl«chtend' ; aber  'Schild'  wäre  ap.  *sparar,  i.  np.  npat; auch   anapaßäpat   bei  Mesvch  dürfte  anf  ap.
23658:•  j.  'varwära-n.  'Wehr,  Schild':  tal söi'öis' .  tattm  Ytf.Sö;  /o.33,  JJ-34,  43;  —  ■■«*& (sd.)/fl/°«ffj  dad^maidl  hyat  mmS'V.58.1.  \ahura%aia  Yt/0.67; —  'nahecafaiti  aku-
25372:Pü. :  Tänpän,  erl.:  sfarfak  'kleines  Schild',  s. West  ZDMG.  43.  49,  Jn.  Her.  119  und unter  'iarana-  No,  2.  —  ")  S  4^4  Ntr.
25651:s.  noch  No.  7.  — —  >)  Hds.  urvuni  stall  urunf.  —  3)  Die  Hds. lassen  umnä  was,  daa  aber  auch  durch  Pü. verbürgt  wird.  —  4)  H.  3.  1-18  betchreibt das  Geschick,  das  die  Seele  des  Gläubigen, n.  3.  19-36  jenes,  das  die  Seele  des  Ungläu- bigen erfährt.  Die  denWörtem  von  H.  a.  iff. entsprechenden  von  H.  3.  l<)f[.  sind  dahinter in  -()-  beigefügt;  s.  noch  No.  5.  —  a  Die entsprechende  Schilderung  für  die  Seele  des Ungläubigen  fehlt;  s.  aber  die  mp.  IJtt.,  Sa. 666*).    —    6)  Vgl.  V.  13.  jo,  Sp.  919  m.  -
25750:')  Vgl.   die  Abbildung   des  Helms    und   des Schild»  au«  Kirmättiäk  in  ZDMG.  36.  655. j,  uroilyeiH  P.  £6:  lies  urvity*.
25753:•  j.  urvi-varflSra-  Adj.  'des  Schild  (in
27938:•  j.  zairimyaDUra-  m.  Name  eines fAiftischen  Tiers,    'Schildkröte"':    da^m
27940:yim  'rpm  nqma  ..yim  maiyäka  avi  duiva- ^avJtS zairimyaksm^&A.)  nqma  ao/ai/e"dcn Dasva  Z.  mit  Namen,  den  die  Übel- redenden Leute  Z,  nennen"  V.  13.  ö. Komp.;  zairimya-  +  *a/mra-  'des  Glieder  (oder Zehen)  in  einem  festen  Gehaus  stecken';  a  in der  KompFuge  statt  £  (bi.  i,  %  sgS.  ^),  %  36S. 3  b.  *aoura-  (statt  'angura-,  %  268. 47  c)  m. 'Glied'  oder  "Finget,  Zehe';  vgl.  ai.  anga- n.  'Glied',  aiigülof-  f.  'Füiger,  Zehe';  woss. ong  'Glied',  änguljä  'Finger*.  —  Vgl.  ioirim- yäia:  —  ai.  vgl.  harinu/a-  m.  'Schildkröle'.  — Pü, :  transskr.  [larimangur),  Npü. :  läi  fait.  — <)  Sa  nach  Npü.  nnd  Gü. ,  deren  Angaben von  der  Etymologie  nnterstätit  werde«.  GcR. OK.  160  denkt  vielmehr  an  den  Maulwurf. S.  noch  Sp.  Komm.  i.  297.
```


## [2026-09-14T02:34:10.815Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pewter",
 "prompt": "Full etymology of pewter and of spelter (search both): Old French peautre, Vulgar Latin *peltrum, origin unknown? Quote verbatim, including any connection to Latin spelta or Germanic."
}
```


### [2026-09-14T02:34:14.809Z] TOOL RESULT

```
# Etymology of Pewter

Based on the provided content, here's what the Online Etymology Dictionary states about pewter's origin:

The word entered English in the early 14th century from Old French *peautre* and Medieval Latin *peutrum*. These derived from Vulgar Latin *\*peltrum*, which is described as "a word of uncertain origin."

**Direct quote:** "from Old French _peautre_ (12c.) and Medieval Latin _peutrum_, from Vulgar Latin _\*peltrum_ 'pewter'...a word of uncertain origin."

The document traces pewter through Romance language variants (Spanish *peltre*, Italian *peltro*) but does not establish any confirmed connection to Latin *spelta* or Germanic sources. The etymology simply stops at Vulgar Latin with an acknowledgment that the ultimate origin remains unknown.
```


## [2026-09-14T02:34:24.863Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22700,22715p' BRT.txt; echo \"=== search sparo.dasta variants ===\"; grep -n -i \"spär\\|spâr\\|spar5\\|sparS\\|sparo\" BRT.txt | head -20"
}
```


### [2026-09-14T02:34:24.946Z] TOOL RESULT

```
—  Pü. ;  vay,  vay  1  vatlar.  —  ■)  Anders  SBE. j/.  224  No-,  Dst.  ZA.  3.  579.
•  j.  *vaya'vant-  Adj.  (fem.  *vai/T-)  'mit Vögeln  versehen,  bevölkert':  iä^a  asäum apa.jas3  sitibyasca  haca  gaomaiOhyaica *'vaitibyasca*^  Itaca  mayavaitibyas^a  (sd.) H.2. 16.
Ableit.  aus  )vay-,  in  Anschluss  an  die  them. Kasus  daraus  gebildet;  s.  No.  i.  —  Pü.;  4^11- Aünmand;  ob  vayömand  zu  lesen?  —  ■)  Hds. vayaitbyasi'a,  das  wäre  DPm.  (oder  n.),  was sich  nicht,  wie  DsT.  tot,  mit  mäyavailibyasca DPf.  verbinden  lässl.     Geringe  Stelle.
•  p.  vayas'pira-  m.  EN.  eines  Persers: v^de^famH  namc^  °rahyä  pu^^'e^  pärs^ Bh.4.18.
Eig.  vll.  'der  der  Verfolgung  ein  Ende  macht' ; *vayah-  n.  zum  V.  v^y.  —  <)  Falsch  JüSTl
dby  Google
i36o
NB.  34a,  FoY  KZ.  3S-  Ö3  ('»childfl«chtend' ; aber  'Schild'  wäre  ap.  *sparar,  i.  np.  npat; auch   anapaßäpat   bei  Mesvch  dürfte  anf  ap.
•  j.  vayah-  m.  'Luftraum':  fi-aarase  .  . J  tat  :^ar>nS /ratgaiata  avi  •^tf«(AS,)'* vuaptm  (sd.)  Yt  Jp.  83  (?)''.  *  A)  als Gottheit^':  altat  (näml.  mms)  yiAaj ahurtm  mazdqm  . .  aimls  sptntS .  .  ülao- nqm  fravaii/  .  .  *'yqn  (AS.)"'**  dan^S.- 2^" alahm  Ny./.  I.
ZoDi  V.  •i'ü-.  —  Vgl.  'vayav-.  —  PB. :  väy  (/
der^alälih);    %.  noch  No,  3.   —    »  S  ^'3  «.
^3.  7.  —  »)  Gani  unsichei
Diu  g.  %i.  l.    Pa.  iSl  erl.
und;  s.  daiu  tvayav-*\  —  j  her  den  schßnen  Wagen  lenkend"  YL/o. Fi  u»w.  JJJ4.
VgL  iF.  vauhätum.
[(ur  vayqtC):  \
=== search sparo.dasta variants ===
17881:strafen'^';  mit  Akk,  a)  II  der  Person:  mar- tiyi^  kyc^  .  ,  avam  *^uiaratam  abaram  I iSya*  .  .  avam  *'^/rasatam  (sd.)  sparsam  j Bh.^.  13;  7.  8;  —  avaiy  akifraltsdiy  (sd.) /arJjBh.4.14;  5.  b)  dcrSache,  in  Ver- bindung mit  IS.  frasa  (sd.):  yä  frasä aviSyä  yä  vä  ..  *p^nsam  (3DPM.,  als Pass,)'°*  taya  Y.jj.13.  Wertlos:  tatiBm p>nsänte  Vyi.40.
19238:KompE.  —  Pü. !  ape  afaspäriimA.  —  ')  Näml. eines  Kindes  an  einen  Priester  lum  Zweck pries teriicher  Hilfsleistungen.  —  »)  Hds.  'um.
20134:•  j.  mastay-  f.  'Kenntnis,  Wissen':  dasdi ahmähm  ..  'am  spära  vaä\imca  Yt  10. 33;  5-86.  Y.p.  22,  6'2.4;  —  -iT/n  iTj/J.- pagsaT)h»m    "allseitiges  Wissen"  Y.  5.  17;
23868:•  j.  vohuna-nliag- :  'na-zg-  Adj.  mit ^span-  m.  'Bluthund,  Hund,  der  auf  den Mann  geht':  kva  asti  spä  'naegS^'>  däityB.- g3tusi..yS naecim  isaiti  Aunaranam  tanuye isaitt  hrahnm'^  "Bei  wem  ist  der  Blut- hund richtig  am  Platz?  .  .  (Bei  dem)  der, keine  (besondere)  Fertigkeit,  (sondern)  nur Schutz  für  seine  Person  verlangt"  V. /?, 19;  5.30;  —  späram  yim  .  .  'zg9m  V, lg.  14,  22,  a6;  —  sänqm  .  .yim  . .  'tgqmca V.  i_J.  8;  —  *us  *fäcit  spann  patinti  pams.- haurvqmca  (sd.)  .  .  'sgam^a  V,  i^.  4a,
24042:näina"  vayaspärahyä  pu%''<r  pirsa*^  Bh.
26844:1)  'treten,  stossen';  ma  %wä  dasna mäzdayasnii  aspake  sparSit  sparmaini  (sd.) Vyt..?5-
26856:•  j.  sparman-  n.  etwa  'Tritt,  Stoss';  mü '^iwil  dalna  m/lzdayas'iis  aspaÄe''  sparSit 'maini  "damit  dich  nicht  die  tiasd.  Reli- gion stosse  mit  dem  Stoss  eines  Rosses" Vyt.ji(?).  '
26858:•  g.  sparsz-  V.,  nur  mit  ä  'bestrebt  sein'. Praes.  3  sp^nza-.
26945:•  j.  spära.däSta-  Adj.  (fem.  'tä-)  —  ?  — ", Beiwort  der  Asay;  ttm  hacät  asis  pourui.- x'ä%ra    Ua    sßra    gSusca    vSstraheca    Yt
```


## [2026-09-14T02:34:34.329Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '26945,26955p' BRT.txt"
}
```


### [2026-09-14T02:34:34.383Z] TOOL RESULT

```
•  j.  spära.däSta-  Adj.  (fem.  'tä-)  —  ?  — ", Beiwort  der  Asay;  ttm  hacät  asis  pourui.- x'ä%ra    Ua    sßra    gSusca    vSstraheca    Yt
^9-  54-
■)  Dasi  das  t.  Glied  des  Komp.s  mit  np. sipar  zusammenzustellen  sei  -  so  zuletzt  Fov KZ.  JS-  ^3  ~i  '^'  ganz  anwahricheinlich ,  s. aoch  zu  vaya^ra:  Man  verlangt  ein  Wort von  ahnlichei  Bedeutung  wie  fourui^^^ra-, aber  nicht  ein  'schildgewappnet'  (Gdn.  3yt. 30,  4t)  oder  'qui  porte  le  bouclier'  (DsT.  ZA. 2.  631).  Eher  möchte  an  ein  *.ifära-  'Erfolg', tu  ii/<i-  zu  denken  sein, j.  spilama  P.  26  u.5.;  lies  sßlama,
•  ].,  g.  sp^niSta-  Adj.  (fem,  'tä-)  'der heiligste';  I)  von  Gottheiten:  /ravast/  .  . spmth..  'ta  yatamaide  Yt  JJ.  75;  — paiti mqm  (näml.  ahunm)  .  .  pinsatfuha  yim daavänhpm  'timca  va^i^f^m^aV.  lif.j;  — raltrvS  razista  .  ,  'ta  .  .  va^üta  Yt72.  7; ;o.l36  (yio'te);  —  sraos?m  ..yö  axsHSla urvaitiica  drujs  spasyS  (sd.)  'tahe  Yt r/.  14;  —  insbes.  von  mainyav-  (sd.,  Sp. II 37  u.,  II 38  u.  und  Ntr.);  ayä  *mainivä varatä  (Sp.  1360  f.)  yS  dr»gva  aüistä v»r7zyS  astm  mainyuS  'tS  Y.jo.  5;  —  a/ ahurä    kvS    mainyäm   zara%uslrS  vfrantt
dby  Google
i6i9
sp3ni6ta-  U
spsnta- B
1620
(Sp.  13610.)  ..yastl  nSla  •(ffY.43.16;  — p^ä%rfm  daidita  %wa  *cütiw3  (Sp.  585  o.) ■Ö  maitvyü  Y.  43- " ;  JE?- 1 2.  5'-  7.  3<J- 1 ;
—  mainyus  vBH^p.  1417  u.)  a/iyä  °iS  ahl Y.jö.^.  a)  als  Bezeichnung  einer  der fünf  Arten  des  Feuers":  ätrvm  °t»m  yaza- maide  Y.  z?.  1 1.         II)  sonst:  akyä  *main-
```


## [2026-09-14T02:34:36.031Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/spelter",
 "prompt": "Give the etymology of English spelter (zinc): is it linked to Latin spelta or to pewter / Middle Dutch speauter? Quote verbatim. Also give the Wiktionary etymology of the Latin word spelta (spelt grain) if mentioned."
}
```


### [2026-09-14T02:34:39.021Z] TOOL RESULT

```
# Etymology of English "Spelter"

According to Wiktionary, the etymology of English spelter is:

> "Related to, and perhaps derived from, Middle Dutch _speauter_. Possibly related to _pewter_."

The entry does **not** mention any connection to Latin *spelta* (spelt grain). Additionally, the page provides no etymological information about the Latin word *spelta* itself.
```


## [2026-09-14T02:35:09.242Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD spel- ===\"; grep -n \"^spel-\\|^(s)pel-\\|^spelt\\|spelt\" AHD_watkins1985.txt | head -20; echo \"=== AHD spel-1 context ===\"; grep -n -A12 \"^spel-1\\|^spel-2\\|^spel-3\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-14T02:35:09.342Z] TOOL RESULT

```
=== AHD spel- ===
163:The Indo-Europeans practiced agriculture and the cultivation of cereals. We have sev- eral terms of Indo-European antiquity for grain: gre-no- (CORN), yewo-, and pdro-, which may have designated wheat or spelt. Others of more restricted distribution are wrughyo-, “rye,” and bhares-, “barley.” Two roots for grinding are attested, al-* and mele- (MEAL?, MILL). The latter is confined to the European branches of the family. Another European term is sé-', “to sow,” not found in Greek, Armenian, or Indo-Iranian. The verb “to plow” is are-, again a common European term, with the name of the plow, *ara-trom.
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
979:in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
981:ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
=== AHD spel-1 context ===
```


## [2026-09-14T02:35:10.687Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC spel ===\"; grep -n \"spelta\\|sphal\\|spel-\\b\" IEC.txt | head -20; echo \"=== SYN shield ===\"; grep -n -i \"spelt\\|sipar\" SYN.txt | head -10"
}
```


### [2026-09-14T02:35:10.766Z] TOOL RESULT

```
=== IEC spel ===
17002:sphált- “bang, burst. WP II, 677 Skt. sphatami, pp: sphatitáh, v. id. beside phat! “bang! phut!"; Gk. sphalásso, v. ‘cut, stab’; Br. fauta, tr. & intr. inf. ‘split; faut, pp. id.; MLG spalden, MHG spalten, sv. 7. ‘split’; Fris. spálte, id.; Icel. cf. speldi, n. "flap, valve'
=== SYN shield ===
8399:ChSl. brasino (in Gospels = Bp&pua) : SCr. bragno ‘meal’, Russ. borosno ‘rye- meal’, Lat. far ‘spelt’, Goth. barizeins ‘made of barley’, etc. Walde-P. 2.134. Berneker 74. Cf. the use of Grk. otros ‘grain’ for ‘food’ (above, 3).
9083:3. Ir. bazrgen, W., Br. bara : OE bere ‘barley’, Lat. far ‘spelt’, etc. Walde-P. 2.134. Walde-H. 1.455. Pedersen 1.101.
9187:3. Lat. farina (> Romance words), SCr. brasno (ChSI. brasino ‘food’, 5.12) : Lat. far ‘spelt, grain’, Goth. barizeins ‘made of barley’, OE bere ‘barley’, etc. Walde-P. 2.134. Ernout-M. 330. Walde-H. 1.455.
12929:in this order of preference (in Greece the bread par excellence, apros, was made of wheat, while the pata ‘barley-cake’ was the inferior diet of the common people), while in India rice and barley held the corresponding rank. The earliest food of the Romans was the far ‘spelt’, and its former importance is reflected in the use of pl. farra for ‘grain’ and esp. farina ‘meal’. Rye and oats were North Euro- pean products, the former unknown in classical antiquity, the latter only as wild oats in Greece, in Italy as weeds or used for fodder. Rice, of first impor- tance in India as in the whole Orient, was in Europe an importation little used until late times. Maize is a native American product, introduced into Eu- rope by the Spaniards. Schrader, Real- lex. under Weizen, Gerste, etc. Jardé, Les céréales dans l’antiquité grecque.
12931:Skt. yava- ‘grain’ in RV, later ‘barley’; Av. yava- ‘grain’, NPers. jav ‘barley’; Lith. javai (pl.) ‘grain’; Grk. feat (pl.) ‘spelt’.
12976:1 Grk, mupos, Lith. pirat, Lett. pir’t (in Baltic esp. ‘winter wheat’) : Chl, pyro ‘spelt?, Boh. pyr, Russ. pyre] “speat-grass’, OE fyrs ‘furze’, toot-connection? Walde-P. 2.83.
13014:4. Goth. barizeins adj. ‘xptOwvos’, ON barr (also ‘pine needles’), OF bere, berlic, ME vere, barli, NE barley, dial. bear : Lat. far, farris, ‘spelt’, prob. so-called fr, the spikes of the grain, and fr. the root in Skt. bhrsti- ‘point, tip’, ON burst, OE byrst, ete. ‘bristle’. Walde-P. 2.134. Walde-H. 1.455f. Feist 81.
14532:Chl. rasypati, SCr. sipati, Boh. sypati, Pol. sypaé, Russ. sypat’ ‘pour out, shake out, strew, scatter’ : Lith. supti ‘swing, rock’, Lat. swpdre ‘throw’ (Fes- tus), cpd. dissipare ‘scatter’. Walde-P. 2.524. Trautmann 293. Ernout-M. 1005. Walde-H. 1.356 f.
19351:It. sctupare (also ‘waste, squander’), perh. fr. *ex-siipdre ‘drink up’ second part fr. Gme. (MLG sipen, OF sipan, NE sup, etc.). - REW 3077. Or fr. a blend of this with Lat. disswpare (dis- sipare) ‘scatter, disperse, squander’?
21335:It. restare, rimanere, Sw. forbliva, stanna, vinta SCr. stati, ekat; aspeltare OE belifan, dwellan, Boh. ziistati, Fekatz
```


## [2026-09-14T02:35:21.447Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN shield section ===\"; grep -n \"20.33\\|‘shield’\\|SHIELD\" SYN.txt | head -15; echo \"=== IEC phala/spara ===\"; grep -n \"phála\\|phala-\\|spara-\\|'shield'\" IEC.txt | head -15"
}
```


### [2026-09-14T02:35:21.524Z] TOOL RESULT

```
=== SYN shield section ===
5338:6. Skt. tvac-, -tvacas- : Grk. cakos ‘shield’, root connection? Walde-P. 1.747.
6093:OE sculdor, NE shoulder, Du. schou- der (MLG schulder > Dan. skulder, Sw. skuldra), OHG scultir(r)a, MHG, NHG schulter, prob. through ‘shoulder blade’ from ‘flat piece’ : Goth. skildus ‘shield’, Grk. cxaXis ‘hoe’ (8.25), oxaddw ‘scrape,
7550:3. Ir, fert, prob. (either as ‘covering’ or ‘protected inclosure’) : fern ‘shield’, Goth. warjan, ON verja ‘protect’, Skt, vr- ‘cover’, etc., ef. Alb. vorr ‘grave’ (*wornd), IE *wer-. Walde-P. 1.289, Stokes 271.
10931:4. Ir. ferenn : fern ‘shield’ (20.34), and so prob. at first ‘sword-belt’.
15166:5. Lith. lenta, prob. orig. ‘board of linden-wood’ : ON, OF lind, OHG linta ‘linden-tree’ also ‘shield’. Walde-P. 2.437. Otherwise Falk-Torp 645.
15717:3. Ir. cliab, NIr. cliabh, perh. orig. ‘basket-shield’ : ON Alif ‘shield’, hlifa ‘protect’. Pedersen 1.116.
18766:Lk. 20.33,
19686:6. ChSl. sklezt (renders vouicua Mt. 22.19), cf. Pol. szelqg name of different old Polish coins, Russ. Seleg ‘counter’, etc., fr. the Gme., cf. Goth. skilliggs, ON skillingr, OE scilling, etc. ‘shilling’, name of various coins : ON skilja ‘sepa- rate, divide’, etc. (more directly : Goth. skildus ‘shield’?). Walde-P. 2.593. Feist 483. Stender-Petersen 380 f.
34330:| CHAPTER 20 i WARFARE 20.11 Freur (vb.) 20.28 Gun; CANNoNn 20.12 BatrxE (sb.) 20.29 GuNPOWDER 20.13 War 20.31 Anmor (Defensive) : 20.132 Enemy 20.32 BreasTPLaTr, Corsier hea ies 20.338 HetMer ne aes 20.34 Snreip 20, Renton 20.35 Fortress 20.18 GENERAL 2030 = LOWnE 20.19 Ap 20.41 Victory 20.21 Wearons, ARMS 20.42 Derzat (sb.) 20.22 Crus 20.43 Arrack (sb.) 20.222 BATTLE-Ax 20.44 DEFENSE 20.23 Sune 20.45 RETREAT (sb.) 20.24 Bow 20.46 SuRRENDER (vb.) 20.25 Arrow 20.47 Captivr, PRISONER : 20.26 SpPEar 20.48 Boory, Srors : 20.27 Sworp 20.49 AxpusH (sb.) 20.11 FIGHT (vb.) ee péxopal, qroenewo one meu Lith. kovott, kautis, muStis TONELO erjask, vega Lett. kauti Lat.  pugndare, proeliari Dan. tee bare ChSl. mtrdli 46, bratt It. combattere, pugnare Sw. kampa, fikta, sldss SCr. _boriti se (biti se) : Be. Fee en OE feohtan, wigan, win- eer oS Sia se) - , nan ol.  walezyd, bid sie : sa Pa ME Ee kempe Russ. eee Nee bit'sja, . chim, cai rie rat'sja | a ON al troidim ne Ae vechten Skt.  yudh- : ym ehtan Av. parat-, yud- Br. en em ganna MHG vehten, wigen
34388:3. Ir. cath, W. cad (cf. Gall. Catu-riges, etc.) : ON Hor, and Hod- in cpd. names, OE heapu- in heapubyrne ‘battle corslet’, heapulind ‘war-linden’ = ‘shield’, etc., OHG Hadu-brand, ete., MHG, NHG hader ‘quarrel, strife’, ChSI. kotora ‘battle’. Walde-P. 1.339.
35012:20.33 HELMET
35053:20.34 SHIELD
35055:Besides the commonest and most ge- neric words for ‘shield’, some of the most important of those used less commonly or for special types are mentioned.
35065:scirus ‘dark, obscure’, etc.; or tr. *skotto-m : Ir. sciath, etc. ‘shield’ (be- low, 3). Walde-P. 2.543, 548. Ernout- M. 918.
35067:Fr. bouclier, OF r. bocler (> ME boc- ler, NE buckler; also It., Sp., MHG, Boh., Pol. forms, but mostly special ‘small shield’; only in Fr. reg. for ‘shield’, re- placing écw), orig. adj. with escut (above) ‘shield having a boss’, deriv. of boucle
=== IEC phala/spara ===
1101:bhal- (2) ‘forehead; prominence’. WP II, 175 Skt. cf. (a)bhalam (1) ‘forehead’; Gk. cf. pháios ‘forepiece on helmet? a component also of phál-agx ‘wedge-shaped frontal formation’, phalaris ‘coot; Alb. ballë ‘forehead, front of a formation’; Lat. fala *battering-ram', beside in-fula ‘headgear, garland on animal fore- head; W bâl, pl. baloedd (*bhalos, -es-) ‘peak, prominence’; ON bali 'grass-bank' ; OPr. ballo ‘forehead’. Cf. also the Gk. cpd. phal- akrós ‘bald’. Cf. bhàal- (2). The form re- presented in Lat. balaena seems to represent a non-Greek form of phálaina (‘whale’, lit. ‘hostile forehead’, cf. nuino- ‘hostile’ in Gk. ainós: Olr. anfine, s. ‘enemy’: OE unwine, id.). For OHG belihha ‘coot’, see FK: Belche
12911:pipà “tip, tuft, rush". Cf. pipol- Hes. cf. pípo-, s. ‘tip; Alb. pipa, fpl. *aspara- gus’; ON fifa *cottongrass'; Latv. pipes, pl. *icicles; pipini, mpl. ‘cloves; pipins “little finger
16030:skütos, à (2) ‘covered; covering’. Cf. skeu-, skuu- and WP II, 543 & 549 Skt. (radical and pres. tense only) sku-, sku- nómi, v. ‘cover’; Arm. cf. xuc, xci, i-st. (“cell, room', from a generalized nom. sg. *skuts); Lat. scütum, n. 'shield', also: ‘patch on wound; defence’; Ukr. skyt, m. ‘hermitage’; Latv. skuta, f. and skutas, fpl. “protecting- board’; ON cf. skoða, v. ‘look after, watch’
```


## [2026-09-14T02:35:23.155Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG spar ===\"; grep -n \"^\\*spar\\|spar-\" CHEUNG.txt | head -20; echo \"=== ARY latin index spar ===\"; grep -n -i \"SPHEL\\|SPEL\\|SPAR\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T02:35:23.294Z] TOOL RESULT

```
=== CHEUNG spar ===
22942:*spar 351 
22960:*spar ‘to hand over, entrust’ 
22963:"psp ’I- /abespar-/ ‘to hand over, entrust [+ ’w 407], give up one's honour, life; to 
22985:-spard, Gz. ispär-/ispärt, Gil. (Rsht.) ispurdoen/ispur-, Ham. espartan/espar-, Isfah. 
22986:espartän/separ-, Khuns. ispar-/ispart, Soi bé-spar ‘to hand over, entrust to’, Siv. 
23013:*spard ‘to twitch, quiver’ 
23037:*sparH ‘to tread, kick’ 
23039:*AVESTAN: YAv. spar- ‘to tread, kick’ || (+ *fra-) ‘to tread forward’ || (+ *ui-) ‘to 
23045:*MIDDLE PERSIAN: BMP spl- /spar-/ ‘to trample, tread’, BMP splyh- /sparth-/ (pass.) 
23050:*KHOTANESE: (+ *aua-) LKh. *vaspar- (vaspud-) ‘to trample on’ || (+ *a-) OKh. 
23051:*aspar- (äspid-, äspud-) ‘to tread’ || (+ *upa-) LKh. *paspar- (paspud-) ‘to trample 
23056:*upa-hispar-), MSogd. pspr’mndyy ‘fixing’ (GMS: §1100) || (+ *ni-) BSogd. ’nspr- 
23086:*IE COGNATES: Hitt. /ispar-/ ‘to trample with the feet’, Lat. spernere ‘to push away, 
23095:*sparz ? ‘to aspire to, strive’ 
33726:spar-, 352 
34915:"psp 1- /abespar-/, 351 
35541:spl- /spar-/, 352 
37227:*paspar- (paspud-), 352 
37659:*vaspar- (vaspud-), 352 
43097:-spar-, 351 
=== ARY latin index spar ===
1042:oygTy3 03) 4) (39 Gasilgtl Glagh SPARTACUS 5 s\! Su 4 1G y
1058:| Ha Sgt Baldels 9 651TH} 9 IES g 4 boy jhye dlo yp gFI(SPARTA)
4574:SPARNAS (LITHUANIAN) gi PUR ABALUCHI) gx Sh
4575:SPARNS (LATVIAN) (33) er) PUR (AFGHANI) (3%) pat
4612:SPURGLIS, SPERGLA ___ SPARAN, SPAR
4614:SPARASION, SPAROS, SPORGILOS
4616:POKORNY SOS™~*~*~*~«éOS SPARWA GOTHIC) Ss,
4617:BARNHART: (SPARROW) 1040 {OLD SCANDINAVIAN) pS 2b j
4620:65, (SWALLOW) 135 SPARO, SPERK
4621:ONIONS: (SPARROW) 850 SPERLING (GERMAN) gst !
4622:SKEAT: (SPARROW) 585 SPEARWA :(OLD ENGLISH) oS g-&i\ '
4623:TAF sgbi obey SPARROW ENGLISH) gulSit |
4624:SPARWE, SPURV (DANISH) (lilo
4755:SPARNAS -(LITHUANIAN) 3h 3 FARA
4756:SPARNS (LATVIAN) (93) 5 FARAN (OLD SAXON) WS iS
9750:[SPARE tent gulp gn |
9853:‘APSPAREM, SPARNAL SPARAITI AAVESTAN) glo
9855:SPERNO, SPERNERE = (LATIN) 5,3 *APSPAR, *SPAR-
9857:: SPERNA, SPORNA APASPARTAN, ASPURTAN,
9858:SPURNAN (OLD SAXON) 35 giy-S SEPURDAN, SPAR, GSPURDAN
```


## [2026-09-14T02:35:27.843Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '35053,35080p' SYN.txt | cut -c1-600"
}
```


### [2026-09-14T02:35:27.924Z] TOOL RESULT

```
20.34 SHIELD
Grk. dozls, cdxos, Oupeds Goth. skildus NG domlda (dors) ON skjoldr Lat. _sciitum, clipeus Dan. —skjoldr Ir. scudo Sw. skéld Fr. bouclier OE scild Sp. escudo ME _ scheld Rum.  scut NE shield Tr. sciath, fern, boccoit Du. schild Nir. _— sciath OHG | scilt W. tarian MHG §schilt Br. skoed NHG | schild
Besides the commonest and most ge- neric words for ‘shield’, some of the most important of those used less commonly or for special types are mentioned.
A recurring connection is that with words for ‘board’, properly applied to the wooden shield. Some of the terms orig. denoted some part of the shield as the boss or rim. The function of ‘pro- tection’ is a rare source,
1. Grk. dozis, etym.? Walde-P. 1:50, 2.658. Boisacq 90.
Grk. céxos : Skt. tvac-, -tvacas- ‘skin, hide’. Walde-P. 1.747, Boisacq 849.
Grk. @vpeés, in Hom. ‘stone placed against the door’ (: 6tpa ‘door’), in late writers freq. ‘oblong shield’ and esp. for Lat. sciittum, vs. éonls = Lat. clipeus.
2. Lat. sciiium (> It. scudo, OFr. escul, Fr. écw now obs., Sp. escudo, Rum. scut), either fr. *skouto-m, fr. the root *skeu- ‘cover’ in Skt. skauti ‘eoy- ers’, Grk. cxiros ‘skin, hide’, Lat. ob-
Lith. Lett. ChSI. SCr. Boh. Pol. Russ.
skydas vairuogs Stitt
tit
Stit tarcza Sit
scirus ‘dark, obscure’, etc.; or tr. *skotto-m : Ir. sciath, etc. ‘shield’ (be- low, 3). Walde-P. 2.543, 548. Ernout- M. 918.
Lat. clipeus (clupeus, clipeum), the round bronze shield, etym. dub., perh. loanword. Walde-P. 1.432. Ernout-M. 198. Walde-H. 1.235 f.
Fr. bouclier, OF r. bocler (> ME boc- ler, NE buckler; also It., Sp., MHG, Boh., Pol. forms, but mostly special ‘small shield’; only in Fr. reg. for ‘shield’, re- placing écw), orig. adj. with escut (above) ‘shield having a boss’, deriv. of boucle
‘boss’, fr. Lat. buccula ‘cheek’. REW 1364. Gamillscheg 125. NED sv. buckler.
3. Ir. sciath, W. ysgwyd (obs.), Br. skoed : ChSl. stitti, ete. ‘shield’ (below, 6), OE sctd, OHG scit ‘board, plank’, fr. the root of Goth. skaidan ‘cut’, etc. Walde-P. 2.548. Pedersen 1.58.
Ir. fern, fr. IE *wer- in Goth. warjan,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE
OE werian ‘ward off, hinder, defend’, Skt. vr- ‘cover’, etc. Walde-P. 1.282.
Ir. boccoit (‘boss of a shield’ and ‘small shield’), fr. Lat. bucca ‘cheek’ (cf. Fr. bouclier, etc., above, 2). Pedersen 1.196.
W. tarian, fr. ME targe (below, 4). Parry-Williams 33.
4, Goth. skildus, ON skjoldr, OE scild, etc., general Gmc., prob. as orig. a ‘flat piece, board’ (cf. tenwes tabulae of the German shields, Tac. Ann. 2.14. and OE bord ‘board’, often ‘shield’) : Lith. skiltis ‘slice’, fr. the root in Lith. skelti ‘split?, ON skilja ‘separate’, Goth. skilja ‘butcher’, etc. Walde-P. 2.592. Falk-Torp 1006 f. Feist 432.
Other, less common or more special, Gme. words.
ON targa, OF targa, targe (> OFr. targe > ME, NE targe, whence dim. target) = OHG zarga ‘border’. Fr. targe
1403
```


## [2026-09-14T02:35:29.054Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== ARY سپر ===\"; grep -n \"سپر\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY زفت ===\"; grep -n \"زفت\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T02:35:29.138Z] TOOL RESULT

```
=== ARY سپر ===
311:صادق است. واژه‌ی «یخچالء (چاله‌ی یخ) را برای ابزار سرد ساز برقی بکار می‌پریم. واژه‌ی «سپر» را ۰۹ 48۶
326:(16780۸71) ساخته شده. در کنار جسد گنجانه‌ی سفالی (و در مورد بزرگان قوم) اسلحه و سپر قرار . ذٌ
10023:۰ | سپاردن» اسپاردن» سپردن
10090:چم این واژه در گوتبک و بونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی. :
11048:چم این واژه در زبان گرتبکه: سپر, :
=== ARY زفت ===
```


## [2026-09-14T02:35:37.626Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10075,10100p' incoming/ARY/ARY_pages.txt; echo \"=== page tag ===\"; awk 'NR<=10090 && /\\[pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_pages.txt; echo \"=== 11040-11055 ===\"; sed -n '11040,11055p' incoming/ARY/ARY_pages.txt; awk 'NR<=11048 && /\\[pdf page/ {p=$0} END{print p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T02:35:38.647Z] TOOL RESULT

```
7۸ اس ند بالشلشت۸ ۳۲1 : 5 ,لنشت[521
آرمنی (/۸48(/12): ۸۸ انگلیسی (524/سا8(/0): 5۳
برنانی (07820):. ۳5 دانمارکی (0۸//5): در ۱۸ رل
گوتیکد (00771/0): 50۸ سرئدی (520/534): 8۳1۸
ابسلندی کهن (10414۸ظآمف5 صا0): نروژی (/(0/07:75014): ۱8۸

: 5۳7۸0 ,ش5713 هلندی (0ع7ا0): 5۳17
ساکونی کهن (54:01 02): 87112۸0
[pdf page 341]
۲ ا_بِپژْز (به چم *طحال")
پسگشت‌ها ۰ کی 2 (811181,0) :22 ۸/۸02۷
. 6 (82111) +7 80/1 ۷
یادداشت: ون :
۱ چم این واژه در تخاری ۸ و 8: چالش کردن» سخت کوشیدن, 1
چم این واژه در گوتبک و بونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی. :
۲- چم اصلی این واژه آشکاش " و اُشّقه کردن" بوده است که در زبان‌های ژرمنی نوین تبدیل بُه "خونریزی" و
آریختن" و آنابرد کردن" شده است. ۱
,33300 سس
اوستایی (487۸۷): ای ترا ی ان بان ایرلندی کهن (لادلقا صاه): ان
پهلوی (1/اتلهه): ,857282 گالیک (لاقهه): ۳
سانسکریت (54۸/55/77). 7۸0
ارمنی (4748149۷): ۳۸۳۸۸۷ ۰ | پسگشت‌ها پیش دا
پرنانی 0368/0): 5 زر ری ۳
لائین (/47۸): ۰ 5۳180 ,1188718 ,158ر1 8 (8۳128) + مت امه
فرانسه‌ی کهن (ت۸/0ق۴۷ صا0): ۰ 858120 9 (76ه8) :قعتمالما02
=== page tag ===
[pdf page 341]
=== 11040-11055 ===
۲- 07/1088 ریشه‌ی واژه‌های ژرمی اب فهرست را "ناشناخته" می‌داند.
۳ چم این واژه در یونانی: کج بیل» بیل باغبانی. :
چم این واژه در زبان لاتین؛ چاقر,
۰ ۰
ار ۰
[pdf page 373]
۳ فا

چم این واژه در زبان گرتبکه: سپر, :

۴ در پیشتر زبان‌های هند و اروپایی این واجریشه به چم "استخوان کف" بکار می‌رفنه و شکل و کاربرد این
استخوان برای کندن و ضربه زدن منجر به پیدایش واژه‌ها و چم‌های دیگر شده املی ار

را ۶ ریم

:
[pdf page 373]
```


## [2026-09-14T02:35:46.740Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==342' incoming/ARY/ARY_pages.txt | head -25"
}
```


### [2026-09-14T02:35:47.778Z] TOOL RESULT

```
[pdf page 342]
۹
سپهر | ۳۴۳
ا
انگلیسی کهن (نْعلا8۸/0 ۰:02 بآ8ت8 8 97307۸
اسلاوی کهن (7۴بما؟ لام طا0):
زا لد این پسگشت‌ها ازش هت دای
لهستانی (نلقداهه): 5 0 ۶0/0520
, چکه (لع285ح): 5۸737 8 (8۸3) :02۵
۱ اسلوا کی (8101/7): ۵ 8 (03013) اد
لیتوانی (142 هلان[ 7ل): ک 2 6 (101) ۸2
۱ لدرنی (لتی) (/(/47۲): 50578 ,501081 لغت‌نامه دهخدا : ۷ و ۲۰۷۴
پروسی کهن ۶۸۹5۵۸7 ۵ا0).
پارسی پاستان (228۵1۵49 0ا0): 9۳118۸ پرتغالی (۳077010852): 3
پهلری (۳۸۶۲۲): ۰ 1188178 ,571118
سانسکریت (54(/8577): )2 پسگشت‌ها شک دا
بونانی 0788/0): 571۸۸ 9 ۶005908
لاتین (47100): 521۸2۸ ,5۳38 6 (5217882) نمی ده ی نا
فرانسه (ل۳87): 5۳ 5 (5711838) :002/5
اسپانبابی (52۸۷/8): ۸ 7 (8717838) دوه
ایتالیابی (۷ل۵ارلم7): 55۸ برهان قاطع + ۱.۹
رومانی (81014۸(0): 1 ان
بادداشت: 8 :
۱ بازگشت به: سپید.
‌ نت ۲ واژه‌های رومانس (برگرفته از لاتین) در این فهرست در آغاز چم "گوی" و "فلک" را داشتند و بعداً چم آنها
```


## [2026-09-14T02:35:48.352Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -3 MON_part1.txt; grep -c \"\" MON_part1.txt; grep -n \"pdf page\\|\\[page\" MON_part1.txt | head -3; echo \"=== asfalt in MON files ===\"; grep -rn \"آسفالت\" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head -5"
}
```


### [2026-09-14T02:35:48.461Z] TOOL RESULT

```
0 
2 

99339
=== asfalt in MON files ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:46568:که آسفالت نشده؛ راه خاکی. (تد. .عم. 0( پیاده 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:86806:مخلوط شوند تولید آسفالت کنند. درشتی
```


## [2026-09-14T02:36:04.881Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==341' incoming/ARY/ARY_pages.txt | head -40"
}
```


### [2026-09-14T02:36:05.945Z] TOOL RESULT

```
[pdf page 341]
۲ ا_بِپژْز (به چم *طحال")
پسگشت‌ها ۰ کی 2 (811181,0) :22 ۸/۸02۷
. 6 (82111) +7 80/1 ۷
یادداشت: ون :
۱ چم این واژه در تخاری ۸ و 8: چالش کردن» سخت کوشیدن, 1
چم این واژه در گوتبک و بونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی. :
۲- چم اصلی این واژه آشکاش " و اُشّقه کردن" بوده است که در زبان‌های ژرمنی نوین تبدیل بُه "خونریزی" و
آریختن" و آنابرد کردن" شده است. ۱
,33300 سس
اوستایی (487۸۷): ای ترا ی ان بان ایرلندی کهن (لادلقا صاه): ان
پهلوی (1/اتلهه): ,857282 گالیک (لاقهه): ۳
سانسکریت (54۸/55/77). 7۸0
ارمنی (4748149۷): ۳۸۳۸۸۷ ۰ | پسگشت‌ها پیش دا
پرنانی 0368/0): 5 زر ری ۳
لائین (/47۸): ۰ 5۳180 ,1188718 ,158ر1 8 (8۳128) + مت امه
فرانسه‌ی کهن (ت۸/0ق۴۷ صا0): ۰ 858120 9 (76ه8) :قعتمالما02
انگلیسی کهن (5۸/0/54 010)(از فراسه کهن) 4 (128) :۸۸۲2/28
لد رن 5 (8128) :0/102/5
انگلیسی (62/0/3/0): نداد 8 ون 9 (5۳158) و
اسلاوی کهن (عالابماد #64نابل) صا0): فرهنگ معین + ۱۳۴
۸ لفت نامه دهخدا: ۱۳۳۳۳(
| جواگلسی سوازی از ۱0۷۷
اوستایی (ل487۵): پهلوی (1هال۸ه): انا ان بان
۸۷۸7 ,5۳۸۷۸31 5753۸۰ گرنیک (0077/0): 181
```


## [2026-09-14T02:36:15.214Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%81%D8%AA",
 "prompt": "Give the etymologies for all entries on this page: Arabic زفت (zift) 'pitch, tar' and Persian زفت. For Arabic, does it say it is from Aramaic/Hebrew (zepet) or from Greek? Quote verbatim."
}
```


## [2026-09-14T02:36:16.810Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA",
 "prompt": "Give the Persian entry آسفالت: etymology (borrowed from French asphalte?) and meaning. Quote verbatim."
}
```


### [2026-09-14T02:36:20.198Z] TOOL RESULT

```
# Persian Entry: آسفالت

**Etymology:**
The Persian term was "Borrowed from Russian асфа́льт (asfálʹt, "asphalt"), from French asphalte ("asphalt"), from Ancient Greek ἄσφᾰλτος (ásphăltos, "asphalt, bitumen")."

So it came through Russian, not directly from French.

**Meaning:**
"asphalt, a sticky and highly viscous liquid or semisolid composed almost entirely of bitumen"
```


### [2026-09-14T02:36:22.292Z] TOOL RESULT

```
# Etymologies from the Wiktionary Page

## Arabic زفت (zift)

The page states the etymology is "Of uncertain ultimate origin" but lists related terms from Aramaic and Hebrew. It does **not** attribute the word to Greek. Instead, it notes connections to:

- Jewish Palestinian Aramaic זִפתָּא (ziptā)
- Hebrew זֶפֶת (zéfeṯ)
- Classical Syriac ܙܦܬܐ (zeptā)

The page also mentions Neo-Babylonian as possibly related.

**Direct quote:** "Of uncertain ultimate origin. Related to Jewish Palestinian Aramaic, Jewish Literary Aramaic, Jewish Babylonian Aramaic _זִפתָּא_ (zip̄tā) / _זִיפתָּא_ (zip̄tā), Classical Syriac _ܙܦܬܐ_ (zep̄tā), _ܙܒܬܐ_ (zeḇtā), Hebrew _זֶפֶת_ (zéfeṯ)"

## Persian زفت

The page does **not** provide a dedicated etymology section for the Persian entry. It only appears listed as a descendant language under the Arabic entry's "Descendants" section, with the note "→ Persian: زفت (zeft)".
```


## [2026-09-14T02:36:34.429Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for آسفالت verbatim, including any language-of-origin abbreviation such as (فر) or (فرانسه), and also the دهخدا section if it gives an origin."
}
```


## [2026-09-14T02:36:36.375Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN spelter/pewter ===\"; grep -n \"spelter\\|pewter\" KLN_1966.txt | head -10; echo \"=== SKT spelter/pewter/spelt ===\"; grep -n -i \"spelter\\|pewter\" SKT.txt | head -10"
}
```


### [2026-09-14T02:36:36.455Z] TOOL RESULT

```
=== KLN spelter/pewter ===
28415:pewter,  n.,  any  of  various  alloys  having  tin  as their  chief  constituent.  —  ME.  pewtyr,  pewtre, fr.  OF.  peltre,  peautre,  fr.  VL.  peltrum  (whence also  It.  peltro,  OProveng.,  Sp.  peltre ),  which  is of  uncertain  origin.  Cp.  spelter.
28416:Derivative:  pewter-er,  n.
36184:spelter,  n.,  zinc.  —  Prob.  a  blend  of  LG.  spialter or  Du.  spiauter,  ‘pewter’,  and  It.  peltro,  ‘pewter’. See  pewter.
36185:Derivative:  spelter,  tr.  v. speltoid,  n.,  a  kind  of  wheat.  —  A  hybrid  coined fr.  Late  L.  spelta,  ‘spelt’,  and  Gk.  -oct.8 tj?,  ‘like’, fr.  elSo?,  ‘form,  shape’.  See  spelt  and  -oid. speluncar,  adj.,  of  the  nature  of  a  Cave.  —  Form¬ ed  with  adj.  suff.  -ar  fr.JL.  spelunca,  ‘cave,  cavern, den’,  fr.  Gk.  aTrijXoyya,  ‘acc.  of  a7TrjXuy!;, ‘cave’,  fr.  on^XaLOv,  ‘cavern’.  See  spelaean.  For the  derivation  of  the  Latin  word  from  a  Greek  ac¬ cusative  cp.  Numidia  and  words  there  referred  to. speluncean,  adj.  —  See  prec.  word  and  -ean. spence,  n.,  larder,  pantry  (arch.)  —  Aphetic  for
=== SKT spelter/pewter/spelt ===
13875:Pewter.  (F.  -  E.  ?)  M.  E.  pmtir.  - O.  F.  prutre.  Ptautrt,  piautrt,  a  kind  of metal  (Ro<)aefort).    It  standi  tot  peitrs*.
13877:and  if  akin  to  Span  peltrt.  Ilal.  ft pewter.  Diet  reniarKC  that  the ptttro  is  believed  to  be  dcrivoi English,  which  he  rejecla,  but  onljr  ol grounii  that /rtw/rr could  not  become/i However,  ptitro  is  probably  (l'" peutre),  an  adaptation  of  E.  $piHfr\ Spelter.
18062:Spelter,  powtcr,  xinc  (E.7)  tn  Blount (i674\  Prob.  E;  cf.  lx)w  G.  jr/iW/rr, [KTWlcr  ;  Du.  sfiaufcr,  ^  TTiis  seems  to be  the  origin.il  of  Pewter,  q.v.
```


### [2026-09-14T02:36:36.635Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:36:43.948Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=asphalt",
 "prompt": "Give the American Heritage Dictionary entry for 'asphalt', especially the bracketed etymology (Middle English, Late Latin, Greek asphaltos, a- + sphallein?). Quote verbatim."
}
```


## [2026-09-14T02:36:46.122Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA",
 "prompt": "Quote the Mo'in (فرهنگ معین) entry for آسفالت verbatim, including the origin abbreviation (e.g. فر = French) and definitions."
}
```


### [2026-09-14T02:36:47.183Z] TOOL RESULT

```
# American Heritage Dictionary Entry for "Asphalt"

**Etymology:**
According to the dictionary entry, the bracketed etymology states:

"[Middle English _aspalt_, from Medieval Latin _asphaltus_, from Greek _asphaltos_.]"

**Note:** The entry does not include the hypothetical breakdown you mentioned (a- + sphallein). The etymology provided traces the word through Middle English, Medieval Latin, and Greek, but stops at the Greek form without further decomposition into component parts.
```


### [2026-09-14T02:36:49.659Z] TOOL RESULT

```
# Mo'in Dictionary Entry for آسفالت

According to the Mo'in (فرهنگ معین) dictionary shown on the page:

"[ فر. ] ( اِ.) مخلوطی از قیر و شن و ماسه که به رنگ قهوه ای یا سیاه است که در پوشش کف خیابان ها، جاده ها و پشت بام به کار می رود."

**Translation:** The entry indicates the word originates from French (فر. = French) and defines asphalt as a mixture of tar, sand, and gravel that is brown or black in color, used as a surface coating for streets, roads, and rooftops.
```


## [2026-09-14T02:37:11.740Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 469 -l 469 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg469 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg469.png"
}
```


### [2026-09-14T02:37:13.259Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 36109 Sep 13 22:37 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg469.png
```


## [2026-09-14T02:37:15.340Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg469.png"
}
```


### [2026-09-14T02:37:15.368Z] TOOL RESULT

```

```


## [2026-09-14T02:37:31.502Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LEW spelta ===\"; grep -n \"spelta\" LEW_1910.txt | head -10; echo \"=== LAT spelta ===\"; grep -n \"spelta\" LAT.txt | head -10"
}
```


### [2026-09-14T02:37:31.625Z] TOOL RESULT

```
=== LEW spelta ===
=== LAT spelta ===
59771:spelta, -ae f.: sorte de bl^, dpeautre, originaire de Pannonie
```


## [2026-09-14T02:37:33.212Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=sphal&iencoding=&lang=en",
 "prompt": "What do Monier-Williams and other dictionaries give for the Sanskrit root स्फल् (sphal) and स्फट् (sphaṭ)? Give the glosses verbatim."
}
```


### [2026-09-14T02:37:34.858Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:37:38.489Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '59771,59780p' LAT.txt"
}
```


### [2026-09-14T02:37:38.545Z] TOOL RESULT

```
spelta, -ae f.: sorte de bl^, dpeautre, originaire de Pannonie
d'aprbs S t Jdrfine. Rare; tardif, preniep ex. dans 1 ’ddit de Diocldtien.
Sana doute eapruntd au germanique, passd dans lea 1 . roaanes, M.L.
8x39, et de nouveau eaprunt^ par le V.h.a .spSlza, r.amgl.spSlt?
Un e devaht I suivi de conaonne va contre le traiteaent noraal
de e en latin.
spSlunca, -ae f.: caverne. Classique, atteatd depuia Cicdron;
ne seable plus attestd apros le i er s. de 1 'Bapire. Baprunt A l'ac-
cuaatif du gr.arerjAuy?, coaae spelaeum est eapruntd A oTCqXauov, deneurd
dans quelques dialectes rosans aous la forne *spelHca, M.L.O140.
```


## [2026-09-14T02:37:40.599Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AB%E0%A4%B2",
 "prompt": "Sanskrit फल (phala): give the etymology section — does it derive from a root meaning 'to burst/split' (√फल् phal)? Also does it list the sense 'blade of a plough / ploughshare'? Quote verbatim."
}
```


### [2026-09-14T02:37:49.559Z] TOOL RESULT

```
# Sanskrit फल (phala) Etymology

## Root Derivation

Yes, the etymology section discusses a root meaning related to thickening/coagulating. According to Mayrhofer's analysis cited in the article:

"groups it with the family of words derived from the root फल् (phal, 'to coagulate, become thick')"

However, the entry notes this is debated—it may derive from Proto-Indo-European *(s)bʰel- ("to swell") rather than from Dravidian sources.

## Ploughshare Sense

Yes, the entry lists multiple blade-related senses including ploughshare. The noun section states:

"[blade](/wiki/blade "blade") (of fan, etc.) [vane](/wiki/vane "vane"), [weathervane](/wiki/weathervane "weathervane") (of wind mill) [arrowhead](/wiki/arrowhead "arrowhead") [shield](/wiki/shield "shield") [ploughshare](/wiki/ploughshare "ploughshare")"

The related terms also mention [फाल](/wiki/%E0%A4%AB%E0%A4%BE%E0%A4%B2#Sanskrit "फाल") (phā́la, "ploughshare").
```


## [2026-09-14T02:38:02.507Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%AB%E0%A4%B2%E0%A5%8D",
 "prompt": "Is there a Sanskrit entry for the root स्फल् (sphal)? What glosses are given (to burst, to open, to tremble)? Quote verbatim. If the page does not exist, say so."
}
```


### [2026-09-14T02:38:04.013Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:38:04.366Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)pel-",
 "prompt": "Is there a Proto-Indo-European reconstruction page for *(s)pel- 'to split'? Give its gloss and descendants, especially Latin spelta, Germanic *speltō, and any Indo-Iranian forms. Quote verbatim; if the page does not exist say so."
}
```


### [2026-09-14T02:38:08.848Z] TOOL RESULT

```
Based on the page provided, there is **no Proto-Indo-European reconstruction for *(s)pel- 'to split'**. 

The page shown is for *(s)pel-* meaning "to say aloud, recite" or "to publicly speak." Its descendants include Albanian *fjalë* ("word"), Old Armenian *aṙaspel* ("tale, proverb, riddle"), Proto-Germanic *spellą*, and Ancient Greek *apeilḗ* ("boast").

The page does not mention Latin *spelta*, Germanic *speltō*, or Indo-Iranian forms related to a 'split' meaning. A separate entry for *(s)pel-* 'to split' does not appear to exist on Wiktionary based on this content.
```


## [2026-09-14T02:38:13.345Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/sphal",
 "prompt": "What does Monier-Williams / the Sanskrit dictionaries give for the root स्फल् (sphal)? Quote the glosses verbatim."
}
```


### [2026-09-14T02:38:16.800Z] TOOL RESULT

```
# Monier-Williams Sanskrit Dictionary Definition

According to the Monier-Williams Sanskrit-English Dictionary provided in the content, the root स्फल् (sphal) is defined as:

"to quiver, shake, vibrate, burst, break etc."

The entry also notes it as a variant of √sphul and includes the causative form _sphālayati_.
```


## [2026-09-14T02:38:28.006Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82' \\\n 'https://en.wiktionary.org/wiki/%CF%83%CF%86%CE%AC%CE%BB%CE%BB%CF%89' \\\n 'https://www.etymonline.com/word/asphalt' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1' \\\n 'https://www.etymonline.com/word/pewter' \\\n 'https://en.wiktionary.org/wiki/spelter' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 469 (Sphallein / Sphel): asphalt-sphallo-sipar-spelter chain' 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:38:31.280Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0d5b80f03d535ee6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d6e6715ece66748.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb936a6b8e13c6ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4215adb25c0ec941.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1ea8858e443f007.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/efeafd5fd150879b.txt
```


## [2026-09-14T02:38:37.205Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D9%81%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA' \\\n 'https://www.ahdictionary.com/word/search.html?q=asphalt' \\\n 'https://vajehyab.com/moein/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%AB%E0%A4%B2' \\\n 'https://www.wisdomlib.org/definition/sphal' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 469 (Sphallein / Sphel): zeft, asfalt, asphalt AHD, Skt phala/sphal' 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:38:40.758Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e04c1109e8499191.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/911b1eedefadb390.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55188b6e00daeaca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/46d8fb433f8bf13f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e43b671d3c029f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b027b4755c16b51d.txt
```


## [2026-09-14T02:38:43.123Z] AGENT

Now let me save the Borhan page transcriptions and images for audit.


## [2026-09-14T02:39:10.585Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr; mkdir -p BQT BOOK\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncp $S/bqt469-n486.jpg BQT/1024.png 2>/dev/null; cp $S/bqt469-n547.jpg BQT/1085.png\ncp $S/pg469.png BOOK/469.png\ncat > BQT/1024.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1024 = archive.org borhan-ghate-v2 leaf n486;\nread from the page image by the verification agent, page 469 task, 2026-09-13]\n\nSection heading: بیان دهم — در زای نقطه دار با فا مشتمل بر ده لغت\n\nHeadword (right column, continued into left column):\n«زقت / زفت» ... نوعی [صمغ] چسبنده که از درخت صنوبر حاصل شود ... و به عربی «زفت»\nهمین معنی دارد، و آن سه نوع است: یکی زفت رومی و آن براق و صاف و املس می‌باشد و از روم\nبه رومی شهرت دارد؛ و دیگری زفت تر و آن آبکی و روان می‌باشد و آن را در مرهم‌ها به کار برند\nو آن از قبیل قیر است و از انواع صنوبر گیرند؛ و نوع سیم زفت خشک است و آن را بیشتر از زیتون/\nینبوت و رز گیرند ...\n\nMo'in's etymological footnote 5 (bottom of the page, verbatim):\n«۵ = poix (فر) «لک ۲ ص۲۱۲». بعضی آن را از یونانی Asfaltos (قیر) مأخوذ دانسته‌اند «نفی».»\n\n(i.e. Mo'in equates the word with French poix, cites Lokotsch II p. 212, and adds that\n\"some have taken it to be derived from Greek Asfaltos (= qīr, tar)\", attributing that view\nto «نفی» = Nafisi.)\n\nAdjacent footnote 6 on the same page (for زفر, unrelated to this chart):\n«۶ ـ اوستا zafar (کلو)، پهلوی zafar «اسشق ۶۶۳». هوبشمان zafar , zafan فارسی را با\nسانسکریت jabh (گرفتن، با پوزه گرفتن) و jambha- (دندان، اسنان، گلو) متعلق می‌داند «هوبشمان ۶۶۳».»\nEOF\ncat > BQT/1085.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1085 (running head «-۱۰۸۵-») = archive.org\nborhan-ghate-v2 leaf n547; read from the page image by the verification agent,\npage 469 task, 2026-09-13]\n\nHeadword: «سپار = به ضم اول بر وزن دچار، آهنِ جفت را گویند و آن آهنی باشد سرتیز که زمین\nبه آن شیار کنند ـ و به کسر اول، اسباب و مایحتاج و آلات و ادوات خانه باشد از هر نوعی ـ\nو چرخی را [نیز] گویند که بدان شیرِ انگور گیرند.»\n\nMo'in's etymological footnote 2 (verbatim):\n«۲ ـ هندی باستان ـ phála (دستهٔ خیش)، از ریشهٔ ـ phal، sphal (باز کردن)، سریکلی spur\n(خیش) «اسشق ۶۹۶»: «سپار، کارآهنی که زمین شکافند» «لغت فرس ۱۲۷».»\n\nFootnote 3 on the same page: «۳ ـ از ریشهٔ spar به معنی لگدمال کردن: Henning, Sogdian\nloan-words..., BSOS, X, 1, p. 97.» (this note belongs to سپاردن/سپردن, not to سپار 'plough-tip')\nEOF\nls -la BQT/ | head"
}
```


### [2026-09-14T02:39:11.562Z] TOOL RESULT

```
total 66272
drwxrwxr-x  2 sfmqrb sfmqrb   16384 Sep 13 22:39 .
drwxrwxr-x 14 sfmqrb sfmqrb    4096 Sep 13 22:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb  620205 Sep 13 22:39 1024.png
-rw-rw-r--  1 sfmqrb sfmqrb    1735 Sep 13 22:39 1024.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
```


## [2026-09-14T02:39:14.267Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-14T02:39:14.343Z] TOOL RESULT

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


## [2026-09-14T02:39:16.981Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-14T02:39:17.090Z] TOOL RESULT

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


## [2026-09-14T02:40:30.220Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 spel split ===\"; grep -n \"spelta\\|spel-\\|spalten\" incoming/WLD/WLD_Bd2_pages.txt | head -15; echo \"=== LKT zift ===\"; grep -n -i \"zift\\|zefit\\|Pech\" LKT.txt | head -15"
}
```


### [2026-09-14T02:40:30.294Z] TOOL RESULT

```
=== WLD Bd2 spel split ===
3167:dolere : (Mare u. dgl. "^del- „spalten“.)
4008:  Yielleicht ist pel- „Haut" eig. „die abgespaltene" (wie dogctiSegw u. dgl.),
4499:   Man sucht Wzanknizpfung an "^spel- „8palten“ (Falk-Torp aaO. ; vgl.
5615:(s.    spel- „8palten“) an, ich         weiB nicht, ob mit Eecht.
6042:spalten und breitlegen (s. auch u. plei „kahb’), pripleiJcti „hinzufugen^' (dazu
6182:plas- ,,abspalten, abreil3en“, vielleicht als ^ph-s- Ableitung von der Set-
6183:    Basis {s)pelt- von {fi)p(}i)el- ,,spalten“. Persson Beitr. 804.
6190:spalten*’, flasa „lose hangende Scheibe von Rinde oder Holz'^, schwed.
6191:mdartl. flasa „abschalen“, isl. flaska ,,gespalten werden“: lit. plaskanos
6209:rindet oder geschunden” und zu {s)plei- „spleiBen“ (s. spel- „spalten“) ; dabei
6213:aisl.    flim      „Spott‘*       (aber in      lit.   pleikti „Fische aufspalten                   und breitlegen“
6389:Beitr. 806 f. auf eine damit gleiche Wz. * pleus- „abspalten, abschalen" bezogen,
6395:fieder,   Haar von YierfuBlern" usw. (s. u. spel- „spaken") annimmt, die
6539:(S04f., SSI halt er unsere Wzln. fiir                 Erw. von ( 5) 396 ? „spalten'^ was immer-
6725:Paukenschlagel Kopf, Schadel Samenkolben“ (s. aber auch u. spel- „spalten“;.
=== LKT zift ===
651:dem  Pers.,  etwa  pük  Horn  NpEt  S.  75, Nr.  339  '^Brennholz'],  ebenso  tk.  bakam; hieraus  rum.  bäcan  'Blauholz',  russ. bakan  Tlorentinerlack'.  Bakkam  ist dasselbe  wie  Fernambuk-  oder  Brasil- holz, Caesalpinia  echinata  Lam.,  seit  der Entdeckung  Amerikas  unser  gebräuch- lichstes Rotholz,  das  die  Portugiesen 1.540  in  den  südamerikanischen  Wäldern in  großen  Mengen  fanden  [wie  Haema- toxylon  campechianum  L.  oder  Cam- pecheholz unser  gebräuchlichstes  Blau- liolz  ist].  Im  angloind.  sappanwood  ist wahrscheinlich  tamul.  shappu  oder  ma- layäl.  shappannani  "rot'  als  Grundwort anzusetzen.  Der  dritte  bereits  genannte Name  Brasil  oder  Brazil,  schon  im Mittelalter  gebraucht,  ist  noch  nicht  er- klärt.   [Hobson-Jobson  794.
1776:'Harz'  [vgl.  assyr.  kupru  'Erdpech'  Del HWB  348a];  hieraus  gr.  KutTdpiöaoc;, lat.  cupressus  'Zypresse',  ahd.  ciqjfer- houm  und  schheßlich  dtsch.  Kiefer  Pi- nus  L.  [vgl.  auch  assyr.  giparu  'eine Baumart'  ZAkkFW  53,  wo  allerdings die  Zugehörigkeit  des  gr.  Wortes  an- gezweifelt wii'd].
2386:Vollständig-  kafr  aljahüd  'Judenpech, Asphalt';  hieraus  sp.  acafelar  'Tür  oder Fenster  zumauern,  eine  Wand  mit Gips  oder  Kalk  tünchen'  [Dicc  Gast  21a], pg.  acafelar  'mit  Stein  und  Kalk  zu- mauern' [Constancio  Dicc  9  c].  —  DE 51/52.
2660:'Teer'  [vom  Vb.  katara  'tropfenweise fließen',  vgl.  dazu  aram.  'atränä  'Teer' <  ass.  etränu  'dass.'  ZAkkFW  60] ;  hier- aus z.  T.  über  tk.  katran  'dass.':  rum. catran  'Teer,  Gift  und  Galle',  cäträni 'teeren',  it.  catrame  'Schiffsteer',  afrz. cotran,  nfrz.  guitran,  goudi-on,  prov. catran,  sp.  alqtiiträn,  pg.  alcaträo  'Schiffs- teer'; bulg.  serb.  katran,  serb.  katram 'Schiffspech',  russ.  katran  'Erdpech'. [DE  186.  Eguilaz  251.  ML  6902.  Bern SlEtWb  494.
3473:'Wachs',  ebenso  tk.  niiim  'dass.,  Kerze', hieraus  serb.  nium  'Kerze',  [über  tk. tnumgi/]  rum.  mungiü,  munger  'Kerzen- fabrikaiit',  m!<H.9?/7f 'Keizenfabrik',  kat. sp.  nioniia  'Pech  und  Asphalt',  apg. muminha  'Mischung  vou  Pech  und Quecksilber',  bes.  die  harzige  Masse,  die aus  den  der  Sonne  ausgesetzten  Mumien floß  und  als  heilkräftig  galt.  —  Ar.
3547:'Erdpech,  Naplitha'  (Horn  NpEt  S.  23'2, Nr.  103Ö],  ar.  naft  [der  Wurzel  nafata 'sieden,  wallen'  anfrepaßl;  nachZAkkFW (iO  jedoch  ülier  aram.  napfä  aus  ass. naptu  'Erdöl'],  Ik.  na/t,  neft;  hieraus gr.  vctqpöa  [ngr.  tö  vd9Ti],  lat.  naphtha und  sp.  nafta,  frz.  naphte,  rum.  7iafta, naft;  luss.  neft';  dtsch.  Naphtha  'Erd- pech, Petroleum'.  [Gorjajew  228.  Löbel EITAP  68.  Eguilaz  462.
3954:Auch  sabag,  die  besondere  Art  glänzend schwarzer  Pechkohle,  die  dtsch.  'Gagat', frz.  jais,  engl,  jet  heißt  [KM  II,  885: haraz  aswad  'schwarzer  Schmuck';  wohl aus  pers.  säbäh,  ZDMG  L,  613];  hieraus mit  ar.  Art.  sp.  azabache,  kat.  acebeja, pg.  azeviche  'Gagat,  Trauerschmuck', sp.  azabaches  'Gagatkette,  die  den  Kin-
4260:1882.  Hebr.  s^lö  inö'il: 'Derjenige,  der  nichts  taugt;  Tauge- nichts'; hieraus  dtsch.  Schlemiel,  Schle- mihl  'Pechvogel',  bes.  bekannt  durch CH AMISSOS  ,  Peter  Schlemihl',  den Schattenlosen.  [Ablt.  von  TORCZYNER in  ZDMG  L,  557 ;  andere  Ableitungen : a)  Eigenname  Selümfel  Num.  1.  6;  II, 12,  ein  jüd.  Fürst,  so  Ave-L  IV,  470; denselben  Namen  soll  ein  Rabbinerschüler des  XIV.  Jahrhunderts  in  Ens  in  Öster-
4340:'Unglück,  Pechvogel'  [moderner  Aus- druck, s.  H.  L.  Strack,  Jüdisches  Wörter- buch. Leipzig  1916.  S.  195;  aus  dtsch. schlimm  und  nhebr.  mazol  'Geschick, Glücksstern',  s.  hier  Nr.  1455];  hieraus jüd.-dtsch.  Schlimasel  'Unglück',  Schlam- massel, ganz  modern  Schlamastik  'Verle- genheit, Unannehmlichkeit' ;  mit  slav. Endung  jüd.-dtsch.  Schlimasalnik  'ein Mensch,  dem  alles  widerrät ;  Pechvogel' [Birnbaum  Hebr.  El  52 1.  [SCHU- CHARDT  in  ZromPh  XXXI,  8.  SPITZER in  Herrigs  Archiv  CXXXVIII,  159  und 234/236.
4876:ins  vulg.  Ar.  übergegangen  [vgl.  DE- FREMERY  in  JAs  (5)  XLX,  89  f.] ;  hier- aus sp.  pg.  azagaya,  pg.  zagaia,  it.  za- gaglia,  frz.  zagaye,  zagaie;  durch  die Portugiesen  [s.  Camöes  Lusiadas  Ganto  I, X6]  wurde  das  Wort  früh  nach  Südafrika gebracht,  und  von  hier  gelangte  es  durch die  Kämpfe  der  Engländer  mit  den  Ein- geborenen in  die  engl.  Zeitungssprache ussegay  'Wurfspieß  der  Neger',  Vb.  to assegay  'mit  dem  Wurfspieß  durch- bohren', dtsch.  Hassagai,  Assegai,  ndl. sagaai.  —  Genaue  Beschreibung  nebst Abbildungen  bringt  F.  A.  K.  von  Specht, Geschichte  der  Waffen.  Berlin- Leipzig 1877.  III,  61/62;  100/101  und  öfter. [Dozy  Oost  77.  Hobson-Jobson  38/39. DE  223.  Eguilaz  318.  ML  9591.  Fischer in  MSOS  II,  236.
```


## [2026-09-14T02:40:32.035Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM zift ===\"; grep -n \"زفت\" AFM.txt AFM_pages.txt 2>/dev/null | head -10; echo \"=== PLA ===\"; ls | grep -i PLA; grep -rn \"زفت\" PLA*.txt 2>/dev/null | head -5; echo \"=== FVQ zift ===\"; grep -n -i \"zift\\|zephet\\|zepheth\" FVQ.txt | head -10"
}
```


### [2026-09-14T02:40:32.139Z] TOOL RESULT

```
=== AFM zift ===
AFM_pages.txt:1788:9 وهر م ذلك 0 10 © زفت برطت ٠واما‏ يكون صلم
AFM.txt:2894:9 وهر م ذلك 0 10 © زفت برطت ٠واما‏ يكون صلم 
=== PLA ===
(eval):1: no matches found: PLA*.txt
=== FVQ zift ===
9954:a loan-word, and in Phlv. ej3 3 and Arm. Zift oil, <*/i/V/^
```


## [2026-09-14T02:40:36.915Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ 9945-9960 ===\"; sed -n '9945,9962p' FVQ.txt; echo \"=== AFM 2888-2900 ===\"; sed -n '2888,2900p' AFM.txt"
}
```


### [2026-09-14T02:40:36.991Z] TOOL RESULT

```
=== FVQ 9945-9960 ===
Guidi, Delia Sede, 600, had noted the word as a foreign borrowing, 
and Fraenkel, Fremdw, 147, points out that the olive was not indigenous 
among the Arabs. 1 We may suspect that the word belongs to the 
old pre-Sfcmitic stratum of the population of the Syrian area. In 
Heb. f"PT means both olive tree and olive, 2 but Lagarde, Mittheilungen, 
iii, 215, showed that primitively it meant oil. In Aram, we have X1TT 
and Syr. 1A*1, which (along with the Heb.) Gesenius tried unsuccess- 
fully to derive from HHT to be brif/ht, fresh, luxuriant. The word is 
also found in Coptic &OJT beside tfeeiT and a'o^iT, where it is clearly 
a loan-word, and in Phlv. ej3 3 and Arm. Zift oil, <*/i/V/^ 
olive tree, which are usually taken as borrowings from Aram., 4 but 
which the presence of the word in Ossetian zefi, and Georgian 'bgcno 
would at least suggest the possibility of being independent borrowings 
from the original population. 5 

The Arabic word may have come directly from this primitive 
source, but more likely it is from the Syr. "JA^I, which also is the source 
of the Eth. HjMh (Noldeke, Neite Beilraye, 42). 6 1 1 was ail early borrow- 
=== AFM 2888-2900 ===

اه 


ܐ ® صمغ الصنو بر 5 لغة فيه ٠‏ وهو داتبانج الفارسية ٠‏ قال في 
البرهان 0 اطع : « راتيانج على وزن ܝ ع8 الصنو بر وهو مثل سائر الصموغ 50 
9 وهر م ذلك 0 10 © زفت برطت ٠واما‏ يكون صلم 
فنسكى حبائل «رحته» ܝ يعمد بالطبخ فية شال له 0 20030 ) باليونانة وحام 
1 في شيراز 3 والظاهر 5 اصل الكلمة يونالي 
83 ܐܐܝ مطلقاً وهو مشتق من :0 سال : 

( ܙ( ] نج ) الأنسون وقيل هو الشمرة وهو الأصح لان الاطاء في كتب 
الفردات يذحكرون الأ نيسون في حرف الهمزة ثم يذكون الرازيانج في حرف اراء
```


## [2026-09-14T02:40:47.802Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"zift\\|Pech\" AFA.txt | head -20"
}
```


### [2026-09-14T02:40:47.861Z] TOOL RESULT

```
4427:Ji^.^ iJife. 1. SS5.S ^(JLii >Grünspecht" entlehntaus
5436:n. 384, 8; Tab. III. 895. UT »Pech'* ist übernommen aus
```


## [2026-09-14T02:40:49.687Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5430,5448p' AFA.txt"
}
```


### [2026-09-14T02:40:49.753Z] TOOL RESULT

```
auf aramäische Originale hin.
So zunächst ^1^ Näb. 3, 8; yergl. ^^%LäJt %U
Amrk. Append. 28 , 1 ; Qamäsah 147 ; ib. 448 ; Jä|^t
n. 387, 22; davon ^yS Zuhair 10, 8, das schon den
Arabern als fremd bekannt war. Mu^arrab p. 122. VgL
Ir^d Gast. 796. Daneben ^ und davon ienominativ ^aj Jäküt
n. 384, 8; Tab. III. 895. UT »Pech'* ist übernommen aus
tt*l£lO \rsaA wie schon Freytag mit hebr. *1S3 andeutet.
^1«^ 9am. 745 hat wegen ^iner Form , trotzdem es zur
Wurzel Jij »tropfen*' sich sehr bequem stellt, Nöldeke als
aramäisch in Anspruch genommen (mündl. Mittheiluug). Dafür
spricht auch die Form ^Zjaiij woneben allerdings auch
i\yia£ji Div. Leb. 94 paenult. vorkommt. Es giebt aber
kein aramäisches *iJi^^^ P^*^' und so bleibt nichts übrig
als pC2)^ für westaramäisch zu halten und daneben eine ost-
aramäische Form mit p anzusetzen. Zu dem Wechsel vgl.f^;
■ 181 "■ -• ■
m^Vuj? » 7\V^y mm MTiXinie und NSldeke Z D M 6.
XXVI. 232.
```


## [2026-09-14T02:40:55.365Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:46:37.209Z] AGENT

I'll write the verification file now.


## [2026-09-14T02:52:37.158Z] TOOL CALL #91: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write469.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndata = {\n \"pdf_page\": 469,\n \"book_page\": 439,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Sphallein\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"Ancient Greek σφάλλω (sphállō) 'to trip up, make fall, baffle', from PIE *(s)gʷʰh₂el- 'to stumble' (cf. Sanskrit skhalate, Armenian sxalem); NOT of Semitic origin\",\n   \"note\": \"The Greek word and the gloss are right: σφάλλω 'to cause to fall, trip up, make slip' is well attested from Homer on, and the citation form σφάλλειν is its infinitive. What is wrong is the origin note. Nourai's 'From an unknown Semitic root' is Klein's remark about the DERIVATIVE ἄσφαλτος, not about σφάλλω: Klein p.114 s.v. asphalt writes 'Gk. ἄσφαλτος, which is of uncertain, possibly Sem., origin' and refers to H. Lewy, Die semitischen Fremdwörter im Griechischen (1895) p.53. σφάλλω itself has a solid Indo-European etymology — Beekes (EDG 2010, via Wiktionary) derives it from PIE *(s)gʷʰh₂el- 'to stumble', with Sanskrit स्खलति (skhalati) 'stumbles' and Old Armenian սխալեմ (sxalem) 'to err' as cognates. (Pokorny 985-987 instead put σφάλλω under (s)p(h)el- 'split', which is the root of the second chart on this page — an older view now abandoned.) So the root box mixes a real Greek verb with a Semitic-origin claim that belongs to a different word and that no modern authority applies to σφάλλω.\",\n   \"note_fa\": \"سرواژهٔ این نمودار، فعل یونانی σφάλλω (مصدر sphallein) «لغزاندن، بر زمین زدن» است که واژه و معنای آن درست ثبت شده؛ اما یادداشت «از ریشه‌ای سامی ناشناخته» نادرست جای گرفته است. کلاین (ص ۱۱۴) این نکته را نه دربارهٔ sphallein بلکه دربارهٔ مشتق آن ἄσφαλτος می‌گوید («خاستگاهش نامعلوم و شاید سامی است»، با ارجاع به لِوی ۱۸۹۵ ص ۵۳). خودِ sphallein ریشه‌شناسی هندواروپایی روشنی دارد: بیکس آن را از *(s)gʷʰh₂el- «لغزیدن، سکندری خوردن» می‌داند، هم‌ریشه با skhalati سنسکریت و sxalem ارمنی. پوکورنی (ص ۹۸۵) آن را زیر ریشهٔ (s)p(h)el- «شکافتن» آورده بود که دیدگاهی کهنه است. پس: ادعای سامی‌بودن را پژوهش امروزی رد می‌کند، هرچند واژه و معنای یونانی درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%CF%83%CF%86%CE%AC%CE%BB%CE%BB%CF%89\",\n    \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82\",\n    \"https://www.ahdictionary.com/word/search.html?q=asphalt\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:114\", \"status\": \"partial\", \"note\": \"Klein 1966 p.114 (page marker '114' at line 3646 of KLN_1966.txt) s.v. asphalt: 'F. asphalte, fr. Late L. asphaltus, fr. Gk. ἄσφαλτος, which is of uncertain, possibly Sem., origin. See Heinrich Lewy, Die semitischen Fremdwörter im Griechischen, Berlin, 1895, p.53.' The page is exactly right, but Klein's 'possibly Semitic' is said of ἄσφαλτος; he says nothing about σφάλλειν, and he does not analyse asphaltos as a- + sphallein.\"},\n    {\"ref\": \"AHD:78\", \"status\": \"partial\", \"note\": \"The 1975 AHD New College Edition p.78 is not on disk (only Watkins's IE-root appendix is, and grep -i 'sphal|asphalt' in AHD_watkins1985.txt returns no root entry). The current online AHD s.v. asphalt prints only '[Middle English aspalt, from Medieval Latin asphaltus, from Greek asphaltos.]' — no Semitic source and no a- + sphallein decomposition.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 985-987, (s)p(h)el-1 (POK_full.txt line 79838 ff.)\", \"stance\": \"contradicts\", \"note\": \"Pokorny files σφάλλω under the IE root (s)p(h)el- 'spalten': 'zu σφαλάσσειν also σφαλός … und σφάλλω \\\"throw (originally with Prügeln), toss, fling\\\" … from which \\\"bring to collapse, injure, deceive\\\"'. An Indo-European etymology, not a Semitic one — though this particular assignment is itself now superseded.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, appendix of IE roots\", \"stance\": \"silent\", \"note\": \"No root *sphal- / *(s)gʷʰel- in the appendix and no ASPHALT among the English reflexes listed under spel-1 'to split, break off' (grep of AHD_watkins1985.txt).\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"partial\", \"note\": \"'Gk. ἄσφαλτος, which is of uncertain, possibly Sem., origin' — the only source behind Nourai's 'unknown Semitic root', and it concerns asphaltos, not sphallein.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, col. s.v. sphált- (IEC.txt line 17002)\", \"stance\": \"partial\", \"note\": \"'sphált- \\\"bang, burst\\\". WP II, 677. Skt. sphaṭāmi … Gk. sphalássō, v. \\\"cut, stab\\\"' — Mann too has a Greek sphal- family, but under 'burst/split', i.e. the second root on this page, not a Semitic source.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Greek\",\n     \"words\": \"a-sphallein; asphaltos\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The attested word is ἄσφαλτος (ásphaltos), f., 'bitumen, mineral pitch', first in Herodotus 1.179, where the bitumen of Is (Hit on the Euphrates) is used as mortar in the walls of Babylon; Dioscorides and Strabo use it of the Dead Sea pitch. The traditional analysis, which Nourai follows, takes it as ἀ- privative + a verbal adjective *σφαλτός of σφάλλω, 'that which does not let (things) fall apart', from its use as a binder — hence his gloss 'not slippery, a bonding agent'. Two caveats. (a) There is no Greek verb *ἀ-σφάλλειν: the form Nourai prints is an analytic citation, the real adjective being ἀσφαλής 'not liable to fall, steadfast, secure'. (b) Modern scholarship distrusts the analysis: Etymonline calls it 'weak' and notes the alternative that the word is Semitic or otherwise non-Greek, and Beekes (EDG) simply marks ἄσφαλτος as Pre-Greek. So the derivation drawn here is the traditional one, still commonly repeated, but not the current consensus.\",\n     \"derivation_fa\": \"واژهٔ اصلی ἄσφαλτος «قیر معدنی» است که نخستین بار در هرودوت (۱٫۱۷۹) دربارهٔ قیر «ایس» بر فرات و ملاط دیوارهای بابل به کار رفته است. تحلیل سنّتی — که نورایی از آن پیروی می‌کند — آن را ἀ- نفی + صفت فعلی *σφαλτός از σφάλλω می‌داند، یعنی «آنچه نمی‌گذارد [دیوار] فروریزد»، از کاربردش به عنوان چسباننده. دو نکته: نخست آنکه فعلی به صورت *a-sphallein در یونانی وجود ندارد و صورتِ نورایی ساختگی و تحلیلی است (صفت واقعی ἀσφαλής «استوار، ایمن» است)؛ دوم آنکه ریشه‌شناسی امروزی این تحلیل را سست می‌شمارد و بیکس واژه را «پیشایونانی» (وام از زیرلایهٔ بومی) می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CF%86%CE%B1%CE%BB%CF%84%CE%BF%CF%82\",\n      \"https://www.etymonline.com/word/asphalt\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD:78\", \"status\": \"partial\", \"note\": \"The 1975 print p.78 is not accessible; the current online AHD s.v. asphalt gives only '[Middle English aspalt, from Medieval Latin asphaltus, from Greek asphaltos.]', i.e. it has dropped the a- + sphallein analysis that Nourai credits to it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"contradicts\", \"note\": \"'fr. Gk. ἄσφαλτος, which is of uncertain, possibly Sem., origin' — Klein declines the a- + sphallein analysis altogether.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. ἄσφαλτος (citing Beekes, EDG 2010)\", \"stance\": \"partial\", \"note\": \"'Generally taken as deriving from ἀ- (a-, \\\"not\\\") + σφάλλω (sphállō, \\\"to fall, cast down\\\"), under the assumption that it denoted the material that protects walls from tumbling down. However, according to Beekes, the word is rather Pre-Greek.'\"},\n      {\"src\": \"SKT\", \"where\": \"Etymonline s.v. asphalt (for the English chain)\", \"stance\": \"partial\", \"note\": \"'from Greek asphaltos … a- \\\"not\\\" + *sphaltos \\\"able to be thrown down\\\" … the etymology is considered weak', with the alternative of a Semitic or other non-Greek source.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"zeft «زفت»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Persian زفت zeft 'pitch, tar' (Borhān-e Qāṭeʿ p.1024 describes three kinds — زفت رومی, زفت تر 'liquid pitch used in salves', زفت خشک — all resins/bitumen) is not a descendant of Greek ἄσφαλτος. It is the Arabic زِفْت zift 'pitch' taken into Persian, and Arabic zift belongs to an old Northwest-Semitic family: Jewish Palestinian/Babylonian Aramaic זִפתָּא (ziptā), Classical Syriac ܙܦܬܐ (zeptā), Hebrew זֶפֶת (zépet) 'pitch' (Exod. 2:3; Isa. 34:9); Wiktionary calls the ultimate origin uncertain but lists Persian only as a borrower ('→ Persian: زفت'). Phonetically ásphaltos could not give zeft: the whole -al- syllable and the initial a- would have to vanish and the -s- to disappear before f. Mo'in's own footnote on the cited page reports the Greek derivation merely as somebody else's opinion — «بعضی آن را از یونانی Asfaltos (قیر) مأخوذ دانسته‌اند» — and his own equation is with French poix, citing Lokotsch. If Lewy's suggestion (behind Klein's 'possibly Semitic') is right, the relation runs the other way: Greek ásphaltos would be the borrower and zeft a relative of its source, never its descendant.\",\n     \"derivation_fa\": \"«زفت» در فارسی «قیر، صمغ چسبندهٔ صنوبر» است (برهان قاطع ص ۱۰۲۴ سه گونهٔ آن را برمی‌شمارد: زفت رومی، زفتِ تر و زفت خشک). این واژه از یونانی ásphaltos نیامده، بلکه وام‌واژه‌ای است از عربی «زِفت»، و خودِ زِفت عربی به خانواده‌ای سامی شمالی‌غربی تعلق دارد: آرامی ziptā، سریانی zeptā، عبری zépet «قیر» (سفر خروج ۲:۳). از نظر آوایی نیز گذار ásphaltos به zeft ناممکن است (افتادن هجای ‑al‑ و همخوان s). حتی معین در همان صفحه این اشتقاق یونانی را تنها به «بعضی» نسبت می‌دهد و خود واژه را با poix فرانسه می‌سنجد. اگر هم گمان لِوی درست باشد که ásphaltos یونانی وام سامی است، جهت وام‌گیری وارونهٔ نمودار نورایی می‌شود. نتیجه: پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B2%D9%81%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1024\", \"status\": \"partial\", \"note\": \"Page located and read from the image (archive.org borhan-ghate-v2 leaf n486 = printed p.1024; transcription saved as data/verification/sources/refs/ocr/BQT/1024.vision.txt). Mo'in's footnote 5 reads verbatim: «۵ = poix (فر) «لک ۲ ص۲۱۲». بعضی آن را از یونانی Asfaltos (قیر) مأخوذ دانسته‌اند «نفی».» — i.e. Mo'in himself glosses the word by French poix and cites Lokotsch, and reports the Greek derivation only as the view of others (attributed to «نفی» = Nafisi). The reference therefore supports Nourai's arrow only as a minority opinion, not as Mo'in's own.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Mo'in, p.1024 (leaf n486), headword زفت\", \"stance\": \"partial\", \"note\": \"Entry text: «نوعی [صمغ] چسبنده که از درخت صنوبر حاصل شود … و آن سه نوع است: یکی زفت رومی … و دیگری زفتِ تر … و نوع سیم زفت خشک است»; footnote as quoted above.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"partial\", \"note\": \"Klein's 'uncertain, possibly Sem., origin' for ἄσφαλτος is the only support for any Greek/Semitic link, and it points to Greek as the borrower, not the lender.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, s.v. راتیانج (AFM.txt line 2894)\", \"stance\": \"silent\", \"note\": \"There is no headword زفت in Addi Shir; the word occurs only inside the entry راتیانج (pine resin) as a gloss, with no etymology of زفت itself.\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen (AFA.txt line 5436)\", \"stance\": \"silent\", \"note\": \"grep -i 'zift|Pech' finds only the discussion of Arabic كفر/قفر 'Pech' (< Aramaic, cf. Heb. kōfer); no usable entry for زفت in the OCR.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (FVQ.txt line 9954)\", \"stance\": \"silent\", \"note\": \"The 'Zift' hit is inside Jeffery's entry on زيت zayt 'olive oil' (Phlv. and Arm. forms for 'oil'), a different word; Jeffery has no entry for زفت.\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\", \"note\": \"grep -i 'zift|Pech' turns up nos. on كفر الیهود 'Judenpech, Asphalt', قطران 'Teer' and نفط 'Erdpech/Naphtha', but no zift entry; so Mo'in's citation «لک ۲ ص۲۱۲» could not be matched in the local text.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Latin\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: Late/Medieval Latin asphaltus (also asphaltum, neuter), a straight transliteration of Greek ἄσφαλτος with -os > -us, used by Pliny (Nat. Hist. 35.178, of the bitumen of Judaea) and by the Vulgate tradition; it is the form from which both the French and the English words come. The current online AHD prints exactly this link: 'from Medieval Latin asphaltus, from Greek asphaltos'.\",\n     \"derivation_fa\": \"این گره خالی است و تنها حلقهٔ لاتینی زنجیره را نشان می‌دهد: لاتینی متأخر/میانه asphaltus (و asphaltum)، که آوانگاری مستقیم ἄσφαλτος یونانی است با تبدیل پایانهٔ ‑os به ‑us؛ پلینیوس آن را دربارهٔ قیر یهودیه به کار برده است. همین صورت سرچشمهٔ واژهٔ فرانسوی و انگلیسی است. فرهنگ AHD امروزی نیز همین حلقه را می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.ahdictionary.com/word/search.html?q=asphalt\",\n      \"https://www.etymonline.com/word/asphalt\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Current online AHD s.v. asphalt: '[Middle English aspalt, from Medieval Latin asphaltus, from Greek asphaltos.]' — the Greek > Latin step is exactly Nourai's arrow (the 1975 print p.78 itself is not on disk).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"supports\", \"note\": \"'F. asphalte, fr. Late L. asphaltus, fr. Gk. ἄσφαλτος' — Late Latin as the intermediate, as drawn.\"},\n      {\"src\": \"SKT\", \"where\": \"Etymonline s.v. asphalt\", \"stance\": \"supports\", \"note\": \"'from Late Latin asphaltum, from Greek asphaltos'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node: Old French aspalte / aspalt (13th-14th c.), remodelled on the Latin spelling as asphalte (Modern French asphalte, m.), 'bitumen'; from the 1830s-40s it acquires the sense 'bituminous paving material' in Paris (the 'asphalte de Seyssel'), and that is the sense in which the word is re-exported to the rest of Europe and to Persian. Klein routes English asphalt through exactly this French form.\",\n     \"derivation_fa\": \"این گره نیز خالی است و حلقهٔ فرانسوی را نشان می‌دهد: فرانسوی کهن aspalte (سدهٔ سیزدهم-چهاردهم) که بعدها بر پایهٔ املای لاتینی به asphalte دگرگون شد. در دههٔ ۱۸۳۰-۱۸۴۰ در پاریس معنای «مادهٔ قیراندود برای سنگ‌فرش خیابان» یافت و با همین معنا به دیگر زبان‌ها و از جمله فارسی رفت. کلاین نیز واژهٔ انگلیسی را از همین صورت فرانسوی می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/asphalt\",\n      \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"supports\", \"note\": \"'asphalt also asphaltum, n. — F. asphalte, fr. Late L. asphaltus' — French asphalte from Latin, as drawn.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. آسفالت (Persian)\", \"stance\": \"supports\", \"note\": \"The Persian word is traced 'from French asphalte (\\\"asphalt\\\"), from Ancient Greek ἄσφᾰλτος', confirming that French is the link between Latin and Persian.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"âsfâlt «آسفالت» (also اسفالت، آسفالته)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"آسفالت āsfālt is a 20th-century European loan in Persian, in the modern road-surfacing sense: Mo'in's Farhang marks it '[فر.]' = French, defining it 'مخلوطی از قیر و شن و ماسه … که در پوشش کف خیابان‌ها، جاده‌ها و پشت بام به کار می‌رود'. French asphalte gives Persian آسفالت with the regular prothetic ā- for the French initial a-, and the variant spelling اسفالت; آسفالته (< French asphalté 'asphalted') is the past-participle-based adjective, and آسفالت کردن is the denominative verb. Nourai's arrow French > Persian is right; Wiktionary adds that the word may have reached Persian through Russian асфа́льт (asfálʹt), which is itself from French — plausible for the early 20th century but not contradicting the French source.\",\n     \"derivation_fa\": \"«آسفالت» وام‌واژه‌ای اروپایی و نو در فارسی است، به معنای مادهٔ روکش خیابان: معین در فرهنگ خود آن را با نشان «[فر.]» یعنی فرانسوی آورده و چنین تعریف کرده است: «مخلوطی از قیر و شن و ماسه … که در پوشش کف خیابان‌ها، جاده‌ها و پشت بام به کار می‌رود». از asphalte فرانسه، با افزوده شدن الف کشیده در آغاز (آ-) و نیز صورت نوشتاری «اسفالت»؛ «آسفالته» از صفت مفعولی فرانسوی asphalté ساخته شده است. ویکی‌واژه میانجی‌گری روسی (асфальт) را نیز محتمل می‌داند که خود از فرانسه است و با ادعای نورایی ناسازگار نیست. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA\",\n      \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D9%81%D8%A7%D9%84%D8%AA\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:264\", \"status\": \"supports\", \"note\": \"The lexicon volumes of Mo'in are not in the local OCR (grep 'آسفالت' in MON_part1.txt / the 2-vol Adena scan finds only two incidental mentions, no headword), so the entry was read on vajehyab's Mo'in text: «[ فر. ] ( اِ.) مخلوطی از قیر و شن و ماسه که به رنگ قهوه‌ای یا سیاه است که در پوشش کف خیابان‌ها، جاده‌ها و پشت بام به کار می‌رود.» The '[فر.]' tag is exactly Nourai's French source; the page number 264 could not be verified against a paginated copy.\"},\n      {\"ref\": \"VOP:12\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vāzhe-hā-ye Orupāyi dar Fārsi (1371/1992) is not available anywhere online or locally (refs_online.json records a failed 2026-09 re-search).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. آسفالت (vajehyab)\", \"stance\": \"supports\", \"note\": \"'[ فر. ]' — French, with the modern paving sense.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. آسفالت (Persian)\", \"stance\": \"partial\", \"note\": \"'Borrowed from Russian асфа́льт (asfálʹt, \\\"asphalt\\\"), from French asphalte (\\\"asphalt\\\"), from Ancient Greek ἄσφᾰλτος' — same ultimate route, with a Russian relay Nourai does not draw.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"asphalt\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English asphalt first appears in the early 14th c. as aspalt/aspalte, from Medieval Latin asphaltus (reinforced later by French asphalte); the learned -ph- spelling is restored in the 16th-17th c. on the Greek model. The original English sense is 'hard, resinous mineral pitch found originally in Biblical lands' (the Dead Sea bitumen, whence the lake's name lacus Asphaltites); the modern sense 'paving composition of tar and gravel' dates from 1847, and the verb 'to cover with asphalt' from 1872. This displaced the older learned forms asphaltum and asphaltos.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی asphalt نخست در آغاز سدهٔ چهاردهم میلادی به صورت aspalt از لاتینی میانه asphaltus وارد شد (و بعدها زیر تأثیر asphalte فرانسه تقویت گشت)؛ املای عالمانهٔ ‑ph‑ در سده‌های شانزدهم و هفدهم بر الگوی یونانی بازگردانده شد. معنای نخستین آن «قیر معدنی سرزمین‌های کتاب مقدس» (قیر دریای مرده) بود و معنای امروزی «مصالح سنگ‌فرش از قیر و شن» از ۱۸۴۷ و فعل آن از ۱۸۷۲ است. ادعای نورایی (لاتین ← انگلیسی) درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/asphalt\",\n      \"https://www.ahdictionary.com/word/search.html?q=asphalt\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Current online AHD s.v. asphalt: '[Middle English aspalt, from Medieval Latin asphaltus, from Greek asphaltos.]' — precisely the Latin > English arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 p.114 s.v. asphalt\", \"stance\": \"partial\", \"note\": \"'asphalt also asphaltum, n. — F. asphalte, fr. Late L. asphaltus' — Klein routes the English word through French rather than straight from Latin; Nourai draws the Latin arrow only.\"},\n      {\"src\": \"SKT\", \"where\": \"Etymonline s.v. asphalt\", \"stance\": \"supports\", \"note\": \"'early 14c., \\\"hard, resinous mineral pitch found originally in Biblical lands\\\" … from Late Latin asphaltum, from Greek asphaltos'; 'meaning \\\"paving composition\\\" dates from 1847'; verb 1872.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Sphel\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *(s)p(h)el- 'to split, cut off, tear off; board' (Pokorny 985-987, (s)p(h)el-1; Watkins/AHD spel-1 'to split, break off')\",\n   \"note\": \"Pokorny IEW 985-987 heads the entry '(s)p(h)el-1, Meaning: to split, cut off, tear off; board', with Old Indic sphaṭati 'reißt, springt auf', phalati, phalakam '(cloven wood) board, lath, shield', phala- 'plowshare', the Old Persian Hesychius gloss σπαραβάραι· οἱ γερροφόροι 'shield-bearers' with 'npers. ispar, sipar \\\"shield\\\"', Latin spolium, Gothic spilda, OHG spaltan, Germanic *speltō (> Latin spelta), English spelter, and OCS ras-platiti. Nourai's headword spelling 'Sphel', the language label 'Indo-European' and the gloss 'to split' all match, and POK:985 is the right page. Watkins/AHD lists the same root as spel-1 'To split, break off. … [Pok. 1. (s)p(h)el- 985.]' Buck 20.34 notes independently that words for 'shield' recurrently come from 'board' and from roots meaning 'split', which is the semantic bridge this chart uses.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(s)p(h)el- «شکافتن، جدا کردن؛ تخته» در فرهنگ پوکورنی (ص ۹۸۵–۹۸۷) با همین معنا ثبت شده است و در همان‌جا سنسکریت sphaṭati «می‌شکافد»، phalakam «تخته، سپر»، phala- «تیغهٔ خیش»، واژهٔ پارسی باستان در تفسیر هزیخیوس σπαραβάραι «سپرداران» همراه با «فارسی نو ispar، sipar»، لاتین spolium و ژرمنی *speltō آمده‌اند. سرواژه، برچسب زبانی و معنایی که نورایی داده و نیز شمارهٔ صفحهٔ ارجاع (پوکورنی ۹۸۵) همگی درست است؛ واتکینز نیز همین ریشه را با نام spel-1 «شکافتن» آورده است. باک (بند ۲۰٫۳۴) هم یادآور می‌شود که واژه‌های «سپر» در زبان‌های هندواروپایی بارها از «تخته» و از ریشه‌های به معنی «شکافتن» می‌آیند — همان پل معنایی که این نمودار بر آن استوار است. ادعای نورایی درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E0%A4%AB%E0%A4%B2\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:985\", \"status\": \"supports\", \"note\": \"POK_full.txt line 79838 ff.: 'Root / lemma: (s)p(h)el-1. Meaning: to split, cut off, tear off; board … Page(s): 985-987'. Exactly Nourai's root, label and gloss, on the cited page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. spel-1\", \"stance\": \"supports\", \"note\": \"'spel-1. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (probably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT1 … [Pok. 1. (s)p(h)el- 985.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 677 ff. (index hits in WLD_Bd2_pages.txt, e.g. lines 6182-6183)\", \"stance\": \"supports\", \"note\": \"WP II 677 ff. is the reference Pokorny himself gives; the volume's cross-references cite 'Basis (s)pelt- von (s)p(h)el- \\\"spalten\\\"' and repeatedly 'spel- \\\"spalten\\\"'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 17002 s.v. sphált-\", \"stance\": \"partial\", \"note\": \"'sphált- \\\"bang, burst\\\". WP II, 677. Skt. sphaṭāmi, pp. sphaṭitáḥ … MLG spalden, MHG spalten, sv. \\\"split\\\"' — the same family under a narrower headword.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 20.34 'SHIELD'\", \"stance\": \"supports\", \"note\": \"'A recurring connection is that with words for \\\"board\\\", properly applied to the wooden shield … Goth. skildus, ON skjöldr, OE scild, prob. as orig. a \\\"flat piece, board\\\" … fr. the root in Lith. skelti \\\"split\\\"' — the same semantic path, though Buck's list has no Iranian forms.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 342 (ARY_pages.txt [pdf page 341]), root entry for this family\", \"stance\": \"supports\", \"note\": \"Note 1 to the entry: «چم این واژه در گوتیک و یونانی: لوحه با صفحه‌ای چوبی؛ سپر چوبی» ('the sense of this word in Gothic and Greek: writing tablet with a wooden face; wooden shield'), and note 2: «چم اصلی این واژه … شکافتن … بوده است» — 'split' as the original sense.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"spâra\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The pre-form of the Iranian 'shield' word is well established, but it is Old Persian, not Avestan. Pokorny 985 — the page Nourai cites — writes 'Old pers. Glosse σπαραβάραι· οἱ γερροφόροι Hes. \\\"schildtragend\\\", npers. ispar, sipar \\\"shield\\\"': the evidence is the Hesychius gloss sparabárai for the Achaemenid wicker-shield bearers, i.e. OP *spara-bara- 'shield-bearer', hence OP *spara- 'shield' (Kent's and Bartholomae's reconstruction alike). Nourai's 'Avestan spāra' comes from Horn no. 700 (p.155), who adds 'aw. spāra- \\\"Schild\\\" in spārō.dašta-'; but Bartholomae, AiW col. 1619, prints 'j. spāra.dašta- Adj. — ? —, Beiwort der Ašay' with the meaning explicitly unknown, and his note calls Foy's equation of the first member with NP sipar 'ganz unwahrscheinlich', preferring a *sfāra- 'Erfolg'. Wiktionary likewise derives Middle Persian spar straight from Old Persian *sparah with no Avestan link. The root connection (*(s)p(h)el- 'split' > 'board' > 'shield', with the s-mobile stem *spar-) is Pokorny's and is reasonable, but the node's language label and form are not supportable.\",\n     \"derivation_fa\": \"صورت کهنِ واژهٔ «سپر» در ایرانی روشن است، اما پارسی باستان است نه اوستایی. پوکورنی در همان ص ۹۸۵ می‌نویسد: «واژهٔ پارسی باستان در تفسیر هزیخیوس σπαραβάραι· οἱ γερροφόροι \\\"سپربردار\\\"، فارسی نو ispar، sipar»؛ یعنی گواه، نام سپرداران هخامنشی *spara-bara- است و از آن *spara- «سپر» بازسازی می‌شود. آنچه نورایی «اوستایی spāra» می‌نامد از هرن (شمارهٔ ۷۰۰، ص ۱۵۵) گرفته شده که «اوستایی spāra- \\\"سپر\\\" در ترکیب spārō.dašta-» را افزوده است؛ ولی بارتولومه در فرهنگ ایرانی باستان (ستون ۱۶۱۹) معنای این ترکیب را با علامت «؟» ناشناخته می‌گذارد و یکی‌دانستن جزء نخست آن را با «سپر» فارسی «به‌کلی نامحتمل» (ganz unwahrscheinlich) می‌خواند و صورت *sfāra- «کامیابی» را پیشنهاد می‌کند. ویکی‌واژه نیز فارسی میانهٔ spar را یکراست از پارسی باستان *sparah می‌گیرد. پس برچسب «اوستایی» را پژوهش امروزی رد می‌کند و به جای آن «پارسی باستان *spara-» می‌گوید.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:985\", \"status\": \"partial\", \"note\": \"POK_full.txt (s)p(h)el-1, p.985: 'Old pers. Glosse ἀναπα-βάραι [= σπαραβάραι]· οἱ γερροφόροι Hes. \\\"schildtragend\\\", npers. ispar, sipar \\\"shield\\\" (Old Indic phalakam, spharam \\\"shield\\\" … probably from the Iranian)'. The page supports the root and the Persian word but labels the ancient form OLD PERSIAN; Pokorny gives no Avestan spāra-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1619 s.v. spāra.dašta- (BRT.txt line 26945)\", \"stance\": \"contradicts\", \"note\": \"'j. spāra.dašta- Adj. (fem. °tā-) — ? —, Beiwort der Ašay' with the note 'Dass das 1. Glied des Komp.s mit np. sipar zusammenzustellen sei — so zuletzt Foy KZ. 35.63 — ist ganz unwahrscheinlich … Eher möchte an ein *sfāra- \\\"Erfolg\\\" zu denken sein.' Bartholomae also remarks at vayaspāra- (col. 1360) that «'Schild' wäre ap. *spara-, s. np. sipar; auch σπαραβάραι bei Hesych dürfte auf ap. … zurückgehen».\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 700, p.155 (HRN.txt leaf beginning '— 155 —')\", \"stance\": \"supports\", \"note\": \"'700. sipar, ispar \\\"Schild\\\". ap. σπαραβάραι· οἱ γερροφόροι Hesych; aw. spāra- \\\"Schild\\\" in spārō.dašta-; phlv. spar (Men.); skr. phara-, phalaka- (Mbh.) \\\"Schild\\\", daneben LW. sphara-, spharaka-; arm. LW. aspar.' This is Nourai's source for the Avestan label.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. سپر (Persian)\", \"stance\": \"partial\", \"note\": \"'Inherited from Middle Persian spl (spar, \\\"shield\\\"), from Old Persian *sparah. Akin to Old Armenian ասպար (aspar), an Iranian borrowing.' No Avestan stage.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"separ «سپر»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian سپر sipar/separ 'shield' descends without a break from Middle Persian spar, written [spl]: MacKenzie, CPD p.76, 'spar [spl | M ʾspr, N sipar] shield'; Nyberg II 'spar [spl] shield 85⁵. — Paz. spar, NP sipar'. The Old Iranian form is *spara- (Old Persian, via Hesychius' σπαραβάραι 'the wicker-shield bearers' of the Achaemenid army; Armenian borrowed it as aspar). In New Persian the inherited initial cluster sp- is broken by an anaptyctic/prothetic vowel, giving both sipar/separ and ispar — Hübschmann, Persische Studien, lists 'ispar (sipar) \\\"Schild\\\", afgh. spar, phl. spar' under the very heading 'Vorschlag von i', and §155 'Idg. sp … = np. sp' cites the same word. Only the parent node's language label (Avestan) is at fault; the Persian word, its meaning and its Iranian pedigree are certain.\",\n     \"derivation_fa\": \"«سپر» فارسی نو بی‌گسست از فارسی میانهٔ spar (نوشتهٔ [spl]) آمده است: مکنزی در فرهنگ پهلوی کوچک (ص ۷۶) «spar [spl | فارسی نو sipar] سپر» و نیبرگ در واژه‌نامهٔ خود «spar [spl] سپر … پازند spar، فارسی نو sipar» آورده‌اند. صورت ایرانی باستان *spara- است که گواه آن نام سپرداران هخامنشی در تفسیر هزیخیوس (σπαραβάραι) است؛ ارمنی نیز آن را به شکل aspar وام گرفته است. در فارسی نو خوشهٔ آغازین sp- با واکهٔ میانجی شکسته شده و صورت‌های sipar/separ و ispar پدید آمده‌اند — هوبشمان همین واژه را زیر عنوان «افزودن i آغازین» می‌آورد. تنها ایرادِ این پیکان، برچسب «اوستایی» در گرهِ بالادست است؛ خود واژهٔ فارسی و پیشینهٔ ایرانی آن قطعی است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B3%D9%BE%D8%B1\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"HRN:155\", \"status\": \"supports\", \"note\": \"Horn's printed p.155 (the \\\\f-block of HRN.txt that opens '— 155 —' contains nos. 699-701): '700. sipar, ispar \\\"Schild\\\". ap. σπαραβάραι· οἱ γερροφόροι Hesych; aw. spāra- \\\"Schild\\\" in spārō.dašta-; phlv. spar (Men.) …'. The page number is exact and the entry is precisely Nourai's Persian word with the derivation he draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.76 (PHD.txt line 566)\", \"stance\": \"supports\", \"note\": \"'spar [spl | M ʾspr, N sipar] shield.'\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt line 3482)\", \"stance\": \"supports\", \"note\": \"'spar [spl] shield 85⁵. — Paz. spar, NP sipar.'\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 6055, 6075, 7812)\", \"stance\": \"supports\", \"note\": \"'c) Vorschlag von i in: … ispar (sipar) \\\"Schild\\\", afgh. spar, phl. spar'; and '§ Idg. sp und kṣ = iran. und ap. sp = np. sp: … asp \\\"Pferd\\\" = zd. ap. aspa-' — the regular treatment that yields sipar.\"},\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1360 (BRT.txt line 22707)\", \"stance\": \"partial\", \"note\": \"«'Schild' wäre ap. *spara-, s. np. sipar; auch σπαραβάραι bei Hesych dürfte auf ap. … zurückgehen» — supports the Persian word's Old Persian ancestry while rejecting the Avestan one.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"sphal\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"A Sanskrit root स्फल् sphal does exist in the grammarians' Dhātupāṭha tradition, but its glosses are 'to quiver, shake, vibrate, burst, break' (Monier-Williams, who treats it as a variant of √sphul); 'to open' is a loose rendering of 'burst open, split' and is in fact Horn's 'aufreissen' passed on through Mo'in's «باز کردن». Pokorny 985 does not cite sphal itself but the cognate present forms: 'Old Indic sphaṭati (Dhātup.) \\\"reißt, springt auf\\\", sphuṭati \\\"spreads, bursts open\\\" … phalati \\\"cracks, springt entzwei\\\", phalakam \\\"(cloven wood) board, lath, leaf, shield\\\", phala- \\\"plowshare\\\"'. So the root is real and the assignment to *(s)p(h)el- is Pokorny's, but two reservations apply: (a) the gloss should be 'burst, split open' rather than 'open'; (b) modern Indology no longer regards the phala-/phal- family as securely from this root — Mayrhofer (via Wiktionary s.v. फल) groups phala- with √phal 'to coagulate, become thick' or with PIE *(s)bʰel- 'to swell', and even a Dravidian source has been proposed.\",\n     \"derivation_fa\": \"ریشهٔ سنسکریت स्फल् (sphal) در سنّت دستورنویسان (دهاتوپاتها) وجود دارد، اما معنای آن نزد مونیه-ویلیامز «لرزیدن، تکان خوردن، ترکیدن، شکستن» است و آن را گونه‌ای از √sphul می‌داند؛ «باز کردن» برگردانی آزاد از «شکافتن، از هم دریدن» است که در اصل از «aufreissen» هرن آمده و از راه حاشیهٔ معین به نمودار نورایی رسیده است. پوکورنی (ص ۹۸۵) خودِ sphal را نمی‌آورد بلکه صورت‌های هم‌خانواده را: sphaṭati «می‌شکافد، می‌ترکد»، phalati، phalakam «تخته، سپر» و phala- «تیغهٔ خیش». دو نکته: نخست آنکه معنای دقیق «شکافتن» است نه «گشودن»؛ دوم آنکه هندشناسی امروزی (مایرهوفر، به نقل ویکی‌واژه) خانوادهٔ phala- را دیگر به‌یقین از این ریشه نمی‌داند و آن را با √phal «بستن، غلیظ شدن» یا با *(s)bʰel- «آماسیدن» می‌سنجد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://www.wisdomlib.org/definition/sphal\",\n      \"https://en.wiktionary.org/wiki/%E0%A4%AB%E0%A4%B2\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:985\", \"status\": \"partial\", \"note\": \"POK_full.txt, (s)p(h)el-1, p.985: 'Old Indic sphaṭati (Dhatup.) \\\"reißt, springt auf\\\", sphuṭati … phalati \\\"cracks, springt entzwei\\\", phalakam \\\"(cloven wood) board, lath, leaf, shield\\\", phala- \\\"plowshare\\\"'. The page carries the Indic material and the meaning 'burst open/split', but prints sphaṭati, not sphal, and does not gloss anything 'to open'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 17002 s.v. sphált-\", \"stance\": \"supports\", \"note\": \"'sphált- \\\"bang, burst\\\". WP II, 677. Skt. sphaṭāmi, pp. sphaṭitáḥ, v. id. beside phaṭ! \\\"bang! phut!\\\"; Gk. sphalássō, v. \\\"cut, stab\\\"' — the Indic root with the 'burst' sense.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 696, p.155\", \"stance\": \"supports\", \"note\": \"'696. supār \\\"Pflug\\\". ai. phála- \\\"Pflugschar\\\", zu √phal-, sphal- \\\"aufreissen\\\". sar. spur \\\"Pflug\\\".' — this is where the pairing 'sphal = aufreissen' in Nourai's chart ultimately comes from.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. फल (Sanskrit); Monier-Williams s.v. sphal (wisdomlib)\", \"stance\": \"partial\", \"note\": \"MW: sphal 'to quiver, shake, vibrate, burst, break etc.', a variant of √sphul. Wiktionary on phala: Mayrhofer 'groups it with the family of words derived from the root फल् (phal, \\\"to coagulate, become thick\\\")', possibly PIE *(s)bʰel- 'to swell', possibly Dravidian — so the root assignment is no longer certain.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"spâr «سپار»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Persian word is real and Nourai's gloss is Borhān's own: سپار (vocalised سُپار / supār, Mo'in marks it بضم اول) is defined 'آهنِ جفت را گویند و آن آهنی باشد سرتیز که زمین به آن شیار کنند' — 'the plough's iron, a sharp-pointed iron with which the ground is furrowed' (Borhān-e Qāṭeʿ p.1085); Asadi's Loghat-e Fors 127, quoted there, has «سپار، کارآهنی که زمین شکافند». What is misdrawn is the arrow: supār is not borrowed from a Sanskrit verb but is the inherited Iranian cognate of the Indic noun. Horn no. 696 (p.155) sets it out: 'supār \\\"Pflug\\\". ai. phála- \\\"Pflugschar\\\", zu √phal-, sphal- \\\"aufreissen\\\". sar. spur \\\"Pflug\\\"'; Hübschmann §155 repeats 'supar \\\"Pflug\\\" = skr. phala-, afgh. spāra \\\"Pflugschar\\\"'. Iranian keeps the s-mobile (sp-) where Indic loses it (sph- ~ ph-), so Persian sup-ār and Sanskrit phála- are sister forms of PIE *(s)p(h)el-o-, related to Sarikoli spur and Pashto spāra. Nourai's transliteration 'spâr' also omits the vowel of the first syllable. Verdict: the etymology is the received one (Horn, Hübschmann, Mo'in), but 'Sanskrit → Persian' should read 'cognate with Sanskrit'.\",\n     \"derivation_fa\": \"واژهٔ فارسی درست است و معنایی که نورایی داده همان تعریف برهان قاطع است: «سپار» (به ضمّ اول: سُپار) «آهنِ جفت را گویند و آن آهنی باشد سرتیز که زمین به آن شیار کنند» (برهان، ص ۱۰۸۵)، و لغت فرس اسدی (ص ۱۲۷) آن را «کارآهنی که زمین شکافند» آورده است. آنچه نادرست ترسیم شده جهت پیکان است: «سپار» وام‌واژه‌ای از فعل سنسکریت نیست بلکه هم‌ریشهٔ (cognate) اسم هندی است. هرن (شمارهٔ ۶۹۶) می‌نویسد: «supār \\\"خیش\\\"، سنسکریت phála- \\\"تیغهٔ خیش\\\"، از ریشهٔ phal-, sphal- \\\"شکافتن\\\"؛ سریکلی spur»، و هوبشمان نیز «supar = skr. phala-، پشتو spāra» را می‌آورد. در شاخهٔ ایرانی s آغازین (sp-) نگه داشته شده و در هندی افتاده است (sph-/ph-)، پس سُپار فارسی و phála- سنسکریت خواهرِ یکدیگرند نه مادر و فرزند. آوانگاری «spâr» نیز واکهٔ هجای نخست را نینداخته است. نتیجه: ریشه‌شناسی همان است که هرن و هوبشمان و معین می‌گویند، اما «از سنسکریت» باید «هم‌ریشه با سنسکریت» خوانده شود.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E0%A4%AB%E0%A4%B2\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1085\", \"status\": \"supports\", \"note\": \"Verified on the page image (archive.org borhan-ghate-v2 leaf n547, running head «-۱۰۸۵-»; transcription saved as data/verification/sources/refs/ocr/BQT/1085.vision.txt). Headword: «سپار = به ضم اول بر وزن دچار، آهنِ جفت را گویند و آن آهنی باشد سرتیز که زمین به آن شیار کنند». Mo'in's footnote 2 verbatim: «۲ ـ هندی باستان ـ phála (دستهٔ خیش)، از ریشهٔ ـ phal، sphal (باز کردن)، سریکلی spur (خیش) «اسشق ۶۹۶»: \\\"سپار، کارآهنی که زمین شکافند\\\" \\\"لغت فرس ۱۲۷\\\".» — this is exactly Nourai's chart, including the gloss 'to open' (باز کردن) for sphal.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 696, p.155\", \"stance\": \"supports\", \"note\": \"'696. supār \\\"Pflug\\\". ai. phála- \\\"Pflugschar\\\", zu √phal-, sphal- \\\"aufreissen\\\". sar. spur \\\"Pflug\\\".' — Mo'in's footnote is a translation of this.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §155 and §sp (HUB.txt lines 9253, 7812, 6100)\", \"stance\": \"supports\", \"note\": \"'supar \\\"Pflug\\\" = skr. phala-, afgh. spara \\\"Pflugschar\\\"'; and 'supurdan (pr. sipāram) \\\"übergeben\\\", Wrzl. spar; supār \\\"Pflug\\\", afgh. spāra fem. \\\"Pflugschar\\\"' — a cognate relation, not a borrowing.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny IEW 985, (s)p(h)el-1\", \"stance\": \"partial\", \"note\": \"Lists 'phala- \\\"plowshare\\\" (\\\"zugespitztes Aststück\\\"?)' among the Indic reflexes of the root, but gives no Persian plough word.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ p.1085, headword سپار and footnote 2\", \"stance\": \"supports\", \"note\": \"See ref_check; note also footnote 3 on the same page («از ریشهٔ spar به معنی لگدمال کردن», citing Henning, BSOS X.1, p.97) belongs to سپاردن/سپردن 'to entrust, tread', a different word that must not be confused with this one.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"spelta\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Latin spelta is a real word of the right family but it does not mean 'split ore'; it means spelt, the hulled wheat Triticum spelta. Ernout-Meillet: 'spelta, -ae f.: sorte de blé, épeautre, originaire de Pannonie d'après St Jérôme. Rare; tardif, premier ex. dans l'Édit de Dioclétien [301 CE]. Sans doute emprunté au germanique, passé dans les l. romanes … et de nouveau emprunté par le v.h.a. spelza'. Pokorny (986-987) says the same: 'Germanic *speltō (out of it Latin spelta) in Old High German spelza, Vulgar Latin spelta (from which:) \\\"spelt\\\"'; Watkins/AHD: 'Middle Dutch spelte, wheat (probably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt.' So (a) the Latin word is a late loan FROM Germanic, not a direct Latin reflex of the root, and (b) the gloss 'split ore' has no basis in any dictionary — it appears to have been invented to make a bridge to 'spelter' in the next box. The motivation for the name is the splitting of the grain's husk in threshing, i.e. the root sense is preserved in a cereal name, not a metallurgical one.\",\n     \"derivation_fa\": \"spelta واژه‌ای واقعی از همین خانواده است، اما معنای آن «سنگ‌معدنِ شکافته» نیست؛ نام گونه‌ای گندمِ پوست‌دار (اسپلت، Triticum spelta) است. ارنو-مِیه می‌نویسد: «spelta: گونه‌ای گندم، اسپلت، به گفتهٔ ژروم بومی پانونیا. کمیاب و متأخر؛ نخستین کاربرد در فرمان قیمت‌های دیوکلتیانوس [۳۰۱ م]. بی‌گمان وام‌گرفته از ژرمنی است و از آنجا به زبان‌های رومانس رفته.» پوکورنی (۹۸۶–۹۸۷) نیز می‌گوید ژرمنی *speltō سرچشمهٔ لاتینی spelta است، و واتکینز می‌افزاید که نام‌گذاری از «شکافته‌شدن پوستِ دانه هنگام خرمن‌کوبی» است. پس نخست آنکه واژهٔ لاتینی وام‌واژه‌ای دیرین از ژرمنی است نه بازماندهٔ مستقیم ریشه در لاتین، و دوم آنکه معنای «سنگ‌معدن شکافته» در هیچ فرهنگی نیست و گویا برای پل‌زدن به spelter در گرهِ بعدی ساخته شده است. پژوهش امروزی این معنا را رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/spelter\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:986\", \"status\": \"partial\", \"note\": \"POK_full.txt, (s)p(h)el-1 (pp.985-987): 'Germanic *speltō (out of it Latin spelta) in Old High German spelza, Vulgar Latin spelta (from which:) \\\"spelt\\\"; engl. spelter \\\"Zink\\\" (*spaldiz-)'. The cited page does carry spelta under the root, but as a Germanic loan into Latin and with the meaning 'spelt (grain)', not 'split ore'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, DELL s.v. spelta (LAT.txt line 59771)\", \"stance\": \"contradicts\", \"note\": \"'spelta, -ae f.: sorte de blé, épeautre … Sans doute emprunté au germanique' — a cereal name, and a borrowing into Latin.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. spel-1\", \"stance\": \"partial\", \"note\": \"'Middle Dutch spelte, wheat (probably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt' — right root, wrong gloss in the chart.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. speltoid (KLN_1966.txt line 36185)\", \"stance\": \"contradicts\", \"note\": \"'speltoid, n., a kind of wheat. — A hybrid coined fr. Late L. spelta, \\\"spelt\\\" …' — Klein knows spelta only as 'spelt'.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etym. Wb. (LEW_1910.txt)\", \"stance\": \"silent\", \"note\": \"grep 'spelta' returns nothing in the local OCR of the 1910 edition.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"spelter; pewter\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Neither word descends from Latin spelta. (a) spelter 'commercial zinc' (not 'zinc ore' — it is the smelted metal) is first recorded in Blount 1674; Klein: 'spelter, n., zinc. — Prob. a blend of LG. spialter or Du. spiauter, \\\"pewter\\\", and It. peltro, \\\"pewter\\\". See pewter'; Skeat: 'Spelter, pewter, zinc (E.?) in Blount (1674). Prob. E.; cf. Low G. spialter, spelter; Du. spiauter. This seems to be the original of Pewter'; Wiktionary: 'Related to, and perhaps derived from, Middle Dutch speauter. Possibly related to pewter.' Pokorny does list 'engl. spelter \\\"Zink\\\" (*spaldiz-)' under (s)p(h)el-, but as a Germanic formation in parallel with OE speld 'splinter', not as a descendant of the Latin grain-name. (b) pewter: Middle English pewtyr/pewtre, from Old French peautre/peltre, from Vulgar Latin *peltrum (whence Italian peltro, Spanish peltre) — 'a word of uncertain origin' (Klein; Etymonline). The gloss 'tin alloys' is right for pewter; the etymology drawn for both words is not.\",\n     \"derivation_fa\": \"هیچ‌یک از این دو واژه از spelta لاتین نیامده است. نخست، spelter در انگلیسی «رویِ تجاری» است (نه «سنگ‌معدن روی»؛ فلزِ گداخته است) و نخستین بار در ۱۶۷۴ در بلاونت دیده می‌شود؛ کلاین آن را «احتمالاً آمیزه‌ای از spialter آلمانی سفلا یا spiauter هلندی \\\"پیوتر\\\" با peltro ایتالیایی» می‌داند و اسکیت نیز آن را ژرمنی و اصلِ pewter می‌شمارد. پوکورنی هرچند «انگلیسی spelter \\\"روی\\\"» را زیر همین ریشه آورده، آن را ساختی ژرمنی (*spaldiz-) می‌داند، هم‌پایهٔ speld انگلیسی کهن «تراشهٔ چوب»، نه بازماندهٔ نام گندم لاتینی. دوم، pewter از انگلیسی میانهٔ pewtyr، از peautre/peltre فرانسوی کهن، از *peltrum لاتینی عامیانه است که «خاستگاهش نامعلوم» خوانده شده است. معنای «آلیاژهای قلع» برای pewter درست است، ولی ریشه‌شناسیِ ترسیم‌شده برای هر دو واژه را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/spelter\",\n      \"https://www.etymonline.com/word/pewter\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent box's POK:986 was checked instead (see node #5) and does not support Latin spelta > English spelter/pewter.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. pewter (line 28415) and spelter (line 36184)\", \"stance\": \"contradicts\", \"note\": \"'pewter … fr. OF. peltre, peautre, fr. VL. peltrum … which is of uncertain origin. Cp. spelter.' / 'spelter, n., zinc. — Prob. a blend of LG. spialter or Du. spiauter, \\\"pewter\\\", and It. peltro, \\\"pewter\\\".'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.vv. Pewter and Spelter (SKT.txt lines 13875, 18062)\", \"stance\": \"contradicts\", \"note\": \"'Spelter, pewter, zinc (E.?) in Blount (1674). Prob. E.; cf. Low G. spialter, spelter; Du. spiauter. This seems to be the original of Pewter.' / 'Pewter … O.F. peutre, peautre, piautre, a kind of metal … probably an adaptation of E. spelter.'\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny IEW 986-987, (s)p(h)el-1\", \"stance\": \"partial\", \"note\": \"'engl. spelter \\\"Zink\\\" (*spaldiz-)' is listed under the root, but in the Germanic section beside OE speld 'splint; bit of wood', not as a derivative of Latin spelta; pewter does not appear at all.\"},\n      {\"src\": \"WEB\", \"where\": \"Wiktionary s.v. spelter; Etymonline s.v. pewter\", \"stance\": \"contradicts\", \"note\": \"'Related to, and perhaps derived from, Middle Dutch speauter. Possibly related to pewter.' / 'from Old French peautre (12c.) and Medieval Latin peutrum, from Vulgar Latin *peltrum \\\"pewter\\\" … a word of uncertain origin.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-469.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write469.py"
}
```


### [2026-09-14T02:52:38.429Z] TOOL RESULT

```
written
```


## [2026-09-14T02:52:40.786Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-469.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 469"
}
```


### [2026-09-14T02:52:42.028Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 3, 'disputed': 4, 'confirmed': 5}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 5, 'supports': 5, 'not_checked': 3}
books consulted: {'contradicts': 7, 'partial': 12, 'silent': 5, 'supports': 15} | by book: {'KLN': 7, 'WEB': 6, 'SKT': 4, 'HRN': 3, 'BQT': 2, 'BRT': 2, 'HUB': 2, 'POK': 2, 'AFM': 1, 'AFA': 1, 'FVQ': 1, 'LKT': 1, 'MON': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'LAT': 1, 'AHD': 1, 'LEW': 1}
```


## [2026-09-14T02:52:51.617Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PY'\nimport json,io\np='data/verification/page-469.json'\nd=json.load(open(p,encoding='utf-8'))\ndef fix(lst):\n    for c in lst or []:\n        w=(c.get('where') or '')+' '+(c.get('note') or '')\n        if c.get('src')=='WEB' and 'Wiktionary' in w and 'Webster' not in w:\n            c['src']='Wiktionary'\n        if c.get('src')=='SKT' and 'Etymonline' in w and 'Skeat' not in w:\n            c['src']='Etymonline'\nn=0\nfor e in d['entries']:\n    fix(e.get('consulted'))\n    for nd in e['nodes']:\n        fix(nd.get('consulted'))\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nio.open(p,'a',encoding='utf-8').write('\\n')\nprint('patched')\nPY\npython3 -m json.tool data/verification/page-469.json >/dev/null && python3 tools/verify_check.py 469"
}
```


### [2026-09-14T02:52:52.867Z] TOOL RESULT

```
patched
nodes verified: 12/12
node verdicts: {'plausible': 3, 'disputed': 4, 'confirmed': 5}
root verdicts: {'disputed': 1, 'confirmed': 1}
ref checks: {'partial': 5, 'supports': 5, 'not_checked': 3}
books consulted: {'contradicts': 7, 'partial': 12, 'silent': 5, 'supports': 15} | by book: {'KLN': 7, 'Wiktionary': 6, 'Etymonline': 3, 'HRN': 3, 'BQT': 2, 'BRT': 2, 'HUB': 2, 'POK': 2, 'AFM': 1, 'AFA': 1, 'FVQ': 1, 'LKT': 1, 'MON': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1, 'LAT': 1, 'AHD': 1, 'LEW': 1, 'SKT': 1}
```


## [2026-09-14T02:53:10.100Z] AGENT

Page 469 (book p. 439) verified — `data/verification/page-469.json`, `verify_check.py 469` shows 0 PROBLEM lines (12/12 nodes).

Counts: nodes — 5 confirmed, 3 plausible, 4 disputed. Roots — 1 confirmed (Sphel), 1 disputed (Sphallein). Ref checks: 5 supports, 5 partial, 3 not_checked. No transcription_suspect items and **no extraction errors**: the printed page (rendered and read) matches the JSON exactly.

Disputed items:
- **ROOT Sphallein** — "from an unknown Semitic root" is misapplied: Klein p.114 says that of ἄσφαλτος, not σφάλλω. σφάλλω is IE, from *(s)gʷʰh₂el- "to stumble" (Skt. skhalati, Arm. sxalem).
- **#2 Persian زفت zeft ← Gk. asphaltos** — zeft is from Arabic زفت zift, a NW-Semitic word (Aram. ziptā, Syr. zeptā, Heb. zépet); phonetically impossible from asphaltos. Mo'in's own footnote (p.1024, read from the page image) reports the Greek derivation only as «بعضی … دانسته‌اند».
- **Entry 1 #1 "Avestan spāra"** — Pokorny 985 labels the form Old Persian (Hesychius σπαραβάραι); Bartholomae AiW 1619 marks Av. spāra.dašta- "— ? —" and calls the link to NP sipar "ganz unwahrscheinlich". The real parent is OP *spara-.
- **#5 Latin spelta "split ore"** — spelta means *spelt* (the grain), a late loan from Germanic (Ernout-Meillet, Pokorny 986-7); the gloss "split ore" is unsupported anywhere.
- **#6 spelter / pewter ← spelta** — spelter is from LG/Du. spialter/speauter (Klein, Skeat), pewter from OFr. peautre < VL *peltrum "of uncertain origin"; neither from spelta.

Notable ref-check results: HRN:155 and BQT:1085 and BQT:1024 all land exactly on the cited pages (Borhan vol. 2 offset confirmed as leaf n547 = printed 1085 from the running head); BQT page transcriptions saved to `sources/refs/ocr/BQT/1024.vision.txt` and `1085.vision.txt` with the page images, and the chart page PNG to `sources/refs/ocr/BOOK/469.png`. AHD:78 could not be read in the 1975 print — the current online AHD no longer gives the a- + sphallein analysis Nourai credits to it. VOP:12 remains unobtainable. 12 web pages archived via `fetch_source.py`.
