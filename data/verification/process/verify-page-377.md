# Verification process log — verify-page-377


## [2026-09-07T20:16:26.353Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 377 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-377.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-377.json. Write /home/sfmqrb/git/rishe/data/verification/page-377.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 377` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:16:28.563Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:16:29.199Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:16:29.240Z] TOOL RESULT

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


## [2026-09-07T20:16:29.791Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-377.txt"
}
```


### [2026-09-07T20:16:29.813Z] TOOL RESULT

```
1	=== PDF page 377 (book page 347) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ôus 1, Au 1, Aus 1 : ear  (refs POK:78,785; KLN:126,494)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:457 | Ghosh : ear | NOTE: Derivation from this root is not certain.
5	  #2 (parent #1) [Avestan] refs=POK:457; BQT:1858 | gaoša : ear ; gaoša-vare : carried by the ear ☞Bher 1
6	    #3 (parent #2) [Persian] refs=None | gŭš «گوش» : ear ; gŭšvâreh «گوشواره» : earrings
7	    #4 (parent #2) [Avestan] refs=POK:454 | ni-gaoša : to listen ☞Nî 1
8	      #5 (parent #4) [Persian] refs=BQT:2239; MON:4746 | nîušîdan «نیوشیدن ( نیوشه )» : to listen ; nağŭšîdan «نغوشیدن (نغوشه)» : to listen
9	      #6 (parent #4) [Pahlavi] refs=ETM:71 | ni-ğôšâg : one who listens, referred to the followers of the Mânî religion. It was later used to mean a "non-Moslem"
10	        #7 (parent #6) [Persian] refs=ETM:71; MON:4746 | naghŭšâ «نغوشا ( نغوشاک )» : The followers of Mânî religion
11	#8 (parent #0) [Germanic] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | ear
13	#10 (parent #0) [Greek] refs=AHD | 
14	  #11 (parent #10) [English] refs=None | anesthesia
15	#12 (parent #0) [Latin] refs=AHD | audire : to hear
16	  #13 (parent #12) [English] refs=None | audio, audience, audit, obey
17	
```


## [2026-09-07T20:16:33.275Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-377.json | head -200",
 "description": "Read source JSON for page 377"
}
```


### [2026-09-07T20:16:34.778Z] TOOL RESULT

```
{
    "pdf_page": 377,
    "book_page": 347,
    "entries": [
        {
            "root": {
                "name": "\u00d4us 1, Au 1, Aus 1",
                "lang": "Indo-European",
                "refs": "POK:78,785; KLN:126,494",
                "gloss": "ear"
            },
            "part": 2,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "POK:457",
                    "words": [
                        {
                            "translit": "Ghosh",
                            "gloss": "ear",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "Derivation from this root is not certain.",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Avestan",
                    "refs": "POK:457; BQT:1858",
                    "words": [
                        {
                            "translit": "gao\u0161a",
                            "gloss": "ear",
                            "script": null
                        },
                        {
                            "translit": "gao\u0161a-vare",
                            "gloss": "carried by the ear",
                            "script": null,
                            "see": [
                                "Bher 1"
                            ]
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
                    "refs": null,
                    "words": [
                        {
                            "translit": "g\u016d\u0161",
                            "gloss": "ear",
                            "script": "\u06af\u0648\u0634"
                        },
                        {
                            "translit": "g\u016d\u0161v\u00e2reh",
                            "gloss": "earrings",
                            "script": "\u06af\u0648\u0634\u0648\u0627\u0631\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 2,
                    "lang": "Avestan",
                    "refs": "POK:454",
                    "words": [
                        {
                            "translit": "ni-gao\u0161a",
                            "gloss": "to listen",
                            "script": null,
                            "see": [
                                "N\u00ee 1"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "BQT:2239; MON:4746",
                    "words": [
                        {
                            "translit": "n\u00eeu\u0161\u00eedan",
                            "gloss": "to listen",
                            "script": "\u0646\u06cc\u0648\u0634\u06cc\u062f\u0646 ( \u0646\u06cc\u0648\u0634\u0647 )"
                        },
                        {
                            "translit": "na\u011f\u016d\u0161\u00eedan",
                            "gloss": "to listen",
                            "script": "\u0646\u063a\u0648\u0634\u06cc\u062f\u0646 (\u0646\u063a\u0648\u0634\u0647)"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0641\u0631\u0633\u062a\u0627\u062f\u0647 \u0631\u0627 \u06af\u0641\u062a \u0646\u06cc\u06a9\u0648 \u0646\u06cc\u0648\u0634 - \u0628\u06af\u0648 \u0622\u0646\u0686\u0647 \u0628\u0634\u0646\u06cc\u062f\u0647\u200c\u0627\u06cc \u062a\u06cc\u0632 \u0647\u0648\u0634",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 6,
                    "parent": 4,
                    "lang": "Pahlavi",
                    "refs": "ETM:71",
                    "words": [
                        {
                            "translit": "ni-\u011f\u00f4\u0161\u00e2g",
                            "gloss": "one who listens, referred to the followers of the M\u00e2n\u00ee religion. It was later used to mean a \"non-Moslem\"",
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
                    "lang": "Persian",
                    "refs": "ETM:71; MON:4746",
                    "words": [
                        {
                            "translit": "nagh\u016d\u0161\u00e2",
                            "gloss": "The followers of M\u00e2n\u00ee religion",
                            "script": "\u0646\u063a\u0648\u0634\u0627 ( \u0646\u063a\u0648\u0634\u0627\u06a9 )"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u062a\u0623\u0648\u06cc\u0644 \u06a9\u0631\u062f \u0645\u0648\u0628\u062f \u0627\u0632 \u0645\u0630\u0647\u0628 \u0646\u063a\u0648\u0634\u0627 - \u0622\u0646 \u0632\u0631\u062f\u0647\u0634\u062a \u06a9\u0648 \u0628\u0648\u062f \u0627\u0633\u062a\u0627\u062f \u067e\u06cc\u0634 \u062f\u0627\u0646\u0627",
                        "poet": "Daq\u00eeq\u00ee"
                    }
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "ear",
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
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "anesthesia",
                            "gloss": null,
                            "script": null
                        }
                    ],
```


## [2026-09-07T20:16:34.812Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','ETM','AHD','WLD','BRT','PHD','NYB','HRN','HUB','IEC','SYN','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-07T20:16:36.188Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

CHEUNG null
```


## [2026-09-07T20:16:53.234Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-377.json | sed -n '200,260p'; ls data/verification/ | head; ls data/verification/sources/refs/ | head -60"
}
```


## [2026-09-07T20:16:53.426Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T20:17:53.289Z] TOOL RESULT

```
claude-sonnet-5[1m] is temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash right now. Wait a moment and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
```


### [2026-09-07T20:17:53.335Z] TOOL RESULT

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


## [2026-09-07T20:18:02.327Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef page(f, n, offset_desc=''):\n    data=open(f, encoding='utf-8', errors='replace').read()\n    pages=data.split('\\f')\n    print('---',f,'leaf',n,'of',len(pages),'---')\n    print(pages[n][:3000])\n# POK offsets: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344\npage('POK_02.txt', 785-344)\nEOF"
}
```


### [2026-09-07T20:18:03.722Z] TOOL RESULT

```
Exit code 1
--- POK_02.txt leaf 441 of 434 ---
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
  File "<stdin>", line 6, in page
IndexError: list index out of range
```


## [2026-09-07T20:18:07.658Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f: $(grep -c $'\\f' $f) pages, $(wc -c <$f) bytes\"; done\ngrep -n \"ous-\\|ōus\\|əus\" /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt | head -30"
}
```


### [2026-09-07T20:18:08.938Z] TOOL RESULT

```
== POK_01.txt: 352 pages, 981836 bytes
== POK_02.txt: 420 pages, 1137861 bytes
== POK_03.txt: 415 pages, 1170809 bytes
== POK_full.txt: 0 pages, 3971883 bytes
15658:Middle Breton brusun^Wuy bit' {* brous-t-)\ 
22052:dausosi. PI. {*d'^ous-) " the upper air, paradise ', dausinti^ ventilate, air '; 
23339:Root / lemma: dous- 
23344:Root/ lemma: dous-\ "arm' derived from an archaic root *^^e:/5'hand, arm' (see below). 
23352:{*dous-nt-s). Gen. o'oa/'arm'; Latvian pa-duse {zero grade) ' Achselhohle; Busen des 
23362:Root / lemma: dous-\ "arm' derived from an archaic root *^/;ef/5"hand, arm' (see below). 
23374:The key link between Root/ lemma: dous- {* gheus-): "arm' derived from an archaic root 
33523:Root / lemma: ghous- 
48628:krous-. gr. Kpouoo "poke, push, hit' (*Kpoua(jo, compare SKpouoGnv, KpouaT£0(;; 
64521:Root / lemma: dus2. aus- : us- : ear', derived from zero grade of Root / lemma: ghous- : 
64550:temple, flattened region on either side of the forehead ' (: Old Irish arae); gr. ous- 
64551:(hybridization of nominative ous- with aus-) in Attic ou(; {*ouooq) "ear', hom. Gen. ouaroc; 
64552:(*ouonTO(;), u)Ki5£(; ' earrings ' Hes. {*ous-n-ko-)\ about qkouu) see above S. 18, 587; 
64559:Maybe truncated alb. vathe^ earrings ' : gr. wkiSsc; " earrings ' Hes. {*ous-n-ko-) : 
64979:A common satem Root/ lemma: dous-\ 'arm' (see above) derived from an archaic root 
64994:The key link between Root / lemma: c/ous- {* gheus-): 'arm' derived from an archaic root
```


## [2026-09-07T20:18:14.381Z] TOOL CALL #9: Bash

```json
{
 "command": "sed -n '64515,64600p' /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
}
```


## [2026-09-07T20:18:14.396Z] TOOL CALL #10: Bash

```json
{
 "command": "sed -n '33515,33580p' /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
}
```


### [2026-09-07T20:18:14.472Z] TOOL RESULT

```
variant assimilation and dissimilation, in addition Old Saxon gornon, gnomon, grornon^ 
grieve ', grun'm. " horror '; 

kiruss. zuryty 'affWct, sadden', zurba^ care ', russ. zurftb " scold '. 

References: WP. I 636, Feist 208. 
Page(s): 453-454 

Root / lemma: ghous- 
Meaning: to sound; hear 
Note: Only indoiranisch. 



Material: Old Indie ghosati^ sounds, announces aloud, hears ', ghosayatT fmae^momng 
lei (Akk.) ' (Geldner Rigveda in Auswahl I 58), ghosa-hru. " sound, clamor, shout, call, din, 
fuss, noise', Asvaghosa EN ' ear of the horse ', Harighosa EN " Yellow ear ' (= Avestan 
zairigaosa); 

Avestan ^aos-'hear', Kaus. in gusayal-uxda-^ sein Wort zu Gehor bringend ', npers. 
niyosTdan^heax, listen, eavesdrop ', Baluchi gosay^heax', n/yosay'hear, listen, eavesdrop 



Maybe alb. Geg n/gjoj, ndegoj {* nde-ghosa), Tosc degjoj, alb. Greece delgonj, alb. Arbersh 
dilingonj, ndelgonj, ndlegonj, glegonj^ I hear ' [common alb. gh- > gl- > gj- : Nth. gh- > dz-]. 

afgh. ngvaiar listen, obey ', Old pers. gausa-, Avestan gaosa-m. 'ear', npers. ^ds'ear', 
skyth. EN DPaGaywaoq ' rattling, clashing by the war chariot ', Avestan zairi-gaosa-^W\Vc\ 
yellow ears'; 

about Latin heus^ hallo! ho, there! hark!' s. rather WH. I 643 f. 

References: WP. I 569, WH. I 643 f. 
Page(s): 454 

Root / lemma: ghou(e)- 

Meaning: to notice, pay attention 

Material: Latin faved, -ere, favT, fautum^ to favor, be well disposed, be inclined towards, 

favor, promote, befriend, countenance, protect; be favorable to, help, support, with dat.; 

with infin., to be inclined to do. Esp. as religious t.t., to speak no words of bad omen; 

hence to be silent; be quiet in worship '; favereirom *fovere because of Umbrian fans 

"favens', foner' favorable, propitious ' from *fouenis, [lllyrian Latin gh- > d- > f-] 

Old Icelandic ga{*gawdn) ' look out, take care ', Gothic gaumjan^ remark, see, raise up 
one' s attention ', Old Norse geyma^hee6, care, worry for, beware'. Old English gTeman, 
Old Saxon gomian. Old High German goumen6s.. Old Icelandic gaumrxw. and gaumi. 
"attention', Old High German gouma^ paying attention, observance, feast ', Swiss gaume 
'baby sitting' (from dem Germanic Latvian gaume^{as\.e\ gaumeV memorize, observe, 
taste '), Old Saxon ^0/775 "repast, meal, guest's meal ', whereof Old Saxon gomian " host '. 
(The meaning relations are still to be cleared in detail; s. Slotty IF. 46, 369.) In addition 
changing through ablaut Old English o/fe/y^/77/a/7 "neglect'. Old Saxon fargumon^ neglect ', 
isl. guma " pay attention '; 



Old Church Slavic govejg, govetr worship; revere, live a god-fearing life ', russ. govetb " 
fast ', sloven, dial. govetT remain grumpily silent ', Serbo-Croatian govijem, govjetT obey 
', Czech hoveti^ favor, spare, look after, look up; satisfy, show Indulgence '; from dem 
Russ. derives Lithuanian gavetT fast ', Latvian gavet6,s.
```


### [2026-09-07T20:18:14.483Z] TOOL RESULT

```
Meaning: ear 

Note: extended with -/{sus/'-s), -es{ausos-n.) and -en 

Note: 

Root / lemma: dus2. aus- : us- : ear', derived from zero grade of Root / lemma: ghous- : 

'to sound; hear'. 

Only Indo Iranian: Old Indie ghosati^ sounds, announces aloud, hears ', Avestan gaos- 

'hear'. Old pers. gausa-, Avestan gaosa-m. 'ear', npers. ^ds'ear' 

Material: 

Zero -a- grade: 

Avestan {*ausi) ^s/Nom. Du. ' both ears, understanding, mind, sense', Instr. Du. usi-bya, 

npers. hos{\mu. *aus-) 'ear'; 

Zero -e- grade: 

grade alb. Nom. {*heus/) veshi, Dat. vesh/'ear' similar to Old Church Slavic Gen. usese'oi 
the ear'. 

common Slavic heu- > ve- phonetic mutation see below. 

Armenian unkn 'ear' ( *us-on-ko-m)\ kn after akn 'eye'; 

gr. Doric (!)(; {*dus) 'ear'; dU3\so in wFara ' auricular, ears ' Alkm., aijcp-wsq Theokr. " 
with two handles ', Doric s^-wpaSia ' earrings ', unsp-cbin ' palate ', Attic Aay-clx;, hom. Aay- 
u)6q n. ' hare ' {*s/ag-dusos) 'with loose ears'; aus-\r\ gr. lak. auc; 'ear', PI. aavGa (*aua- 
avGa) Alkm., tarent. ara (*auaaTa); Ionian nap-rjiov, Attic nap-sia, Lesbian nap-aua ' 
temple, flattened region on either side of the forehead ' (: Old Irish arae); gr. ous- 
(hybridization of nominative ous- with aus-) in Attic ou(; {*ouooq) "ear', hom. Gen. ouaroc; 
(*ouonTO(;), u)Ki5£(; ' earrings ' Hes. {*ous-n-ko-)\ about qkouu) see above S. 18, 587; 
about Attic OKpoaaGai (*aKp-ou(;-)s. Schwyzer Gr. Gr. 1 , 348; 

alb. veshi, PI. veshtem. 'ear' {*dus-, os-); 



Maybe truncated alb. vathe^ earrings ' : gr. wkiSsc; " earrings ' Hes. {*ous-n-ko-) : 
Armenian unkn'ear' {*us-on-ko-m)\ alb. vath^ pen , shed ' (common alb. -k> -th). 

Note: 

Alb. cognate proves that lllyrian used a prothetic i/- before bare initial vowels, while gr. 
preserved the old laryngeal H-. 

Baluchi gosh, Tadzik gus, Afghan gvaz, Albanian veshi, Greek Cretan hous, Byelorussian 
vuchi, vuxa, Lusatian L hucho, Lusatian U wucho, Ukrainian vucho, vuxo, Macedonian 
uvo, us/'ear' common Slavic hou- > vuho- phonetic mutation. 

Latin aurisi. "ear' ( *ausi-s)\ aus-culto " to hear with attention, listen to, give ear to ' see 
above S. 552; 

Old Irish au, on. "ear' {*ausos-)\ Old Irish araem. " temple, flattened region on either 
side of the forehead ' {*par-ausios), Plur. in PN Arar, gall. FN Arausio^ Orange ' 
(Thurneysen KZ. 59, 12); PN Su-ausiai. "with nice, beautiful ears'; 

Gothic auson. "ear' (Germanic *ausan-)\ with gramm. variation {*auzan-): Old Icelandic 
eyra. Old English eare. Old Frisian are. Old Saxon Old High German orau. "ear'; 
therefrom Old High German on. Middle High German sere^ eye '; 

Lithuanian aus/'si. (older also m.). Gen. PI. a^s^(konson. stem), Latvian ausst; Old 
Prussian Akk. PI. aus/ns'the ears', besides aus/nsVok. m.; 

Old Church Slavic ucho. Gen. i/sese (s-stem). 

Maybe Saami bealiji: Basque belarrT ear'. 

References: WP. I 18, WH. I 85 f., Trautmann 18 f., Schwyzer Gr. Gr. 1, 348, 520. 
Page(s): 785 

Root / lemma: 6(uli-om 

Meaning: egg 

Grammatical information: reduced form giom 

Material: Avestan ap-avaya- ^ entmannt' (?), whether from apa-avaya-' without testicle', 

compare Old pers. xaya'egg';
```


## [2026-09-07T20:18:26.952Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Page(s): 45[5-9]\\|^Page(s): 78 \\|^Page(s): 78$\\|^Page(s): 77-78\\|^Page(s): 78-\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:18:28.238Z] TOOL RESULT

```
8299:Page(s): 78-81 
8608:Page(s): 77-78 
33661:Page(s): 455 
33733:Page(s): 455-456 
33766:Page(s): 456-457 
33795:Page(s): 457-458 
33825:Page(s): 458 
33868:Page(s): 458-459 
33895:Page(s): 459-460 
33943:Page(s): 459 
33975:Page(s): 457 
93686:Page(s): 78
```


## [2026-09-07T20:18:31.806Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8240,8300p' POK_full.txt && echo \"=====8560\" && sed -n '8560,8612p' POK_full.txt && echo \"======457a\" && sed -n '33766,33800p' POK_full.txt && echo \"=====457b\" && sed -n '33950,33980p' POK_full.txt"
}
```


### [2026-09-07T20:18:31.903Z] TOOL RESULT

```
spring ' in avaupo(; " without water, of brooks ' (about gr. 9r|aaup6(; and K£VTaupO(; 
compare Schwyzer Gr.Gr. I 267, 444); 

in FIN: Italian A^e/-5^ms (Bruttium), P/s5i//ic/s(Umbrien), gall. Avara> French Avre, Aura 
> French Eure, Aurana> Modern High German 0/7/77(Wurttemb.), Ar-auris> French 
Herault, Vi-aurus > French Le Viaur, Old Prussian Aure, Lithuanian Aur-yte; Old Norse 
aurigr^ wet ', aurr^ wet, water ', FIN Aura, Old English ear^ sea '; 

Old Prussian wurs {*Oras) "pond, pool', iurin f\Vk. Sg., iuriayP\. fem. "sea'. Old Latvian 
Juri- m., Lab/\anju'ra, Lithuanian yi7/'es,yt7/7c»s PI. fem. "sea, esp. the Baltic Sea ' (see above 
to Latin ur/ha; J- presumably suggestion after J. Schmidt PL 204); 

Lithuanian ya^/i/s" swampy, marshy ',ya^/-5,y5^/'as "marshy place, marshy ground, 
swamp bottom' from *eu9r-{see Berneker IF. 10, 162, Trautmann 335 m. Lithuanian). 

3. Verbum: Lithuanian verdu, v/'rt/' bubble, surge, cook ', versme' wellspring ', vyrius^ 
whirlpools ', atvyrs^ counterstream on the shore ', Latvian verdu, vFrC soak, bubble, boil, 
cook ', atvars " whirl ', 



Old Church Slavic vbrjg, vbretr stream, bubble, surge, boil, cook ', virb' whirlpool ', izvorb 
" wellspring (bubbling water) ', wherefore with from " cook ' developed meaning " heat ', 
Latvian wersme " glow ', Old Church Slavic varb " heat '. 

About possible affiliation of *uer/e/na^ alder ' see there. 

4. extension {*h2auers-) uer-s-' rain, dew ': Old Indie varsa-n. " rain, rainy season, year 
' {varsat/" it is raining '), gr. oupov ' urine '; span, ttpor\ " dew ', Ionian Attic oupsu) " 
urinates ' (kausativ *uorseid, F- proved by the augmentation Eoupnoa), oupia " a water bird 



Middle Irish {*gwrass) /^5ss 'rain' is older fross {uros-ta, in spite of Pedersen KG. I 44); 
Hittite wa-ar-sa-as^ra\v\\l)seems an Old Indie loanword. 

Maybe alb. {*varsa-) vesa^6eW : {*heverse) sspari ' dew'. 

{* h2aursen-) ufsen-^ discharging semen = virile ', Old Indie vrsan- 'virile', m. ' manikin, 
man, stallion '. 

thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
"Aries, ram' (= Avestan varasni-6s.), vrsana-m. ' testicles '; 

Specht (Dekl. 156) places here (from Germanic *gwrai-njan-) without s^extension Old 
High German reineo^ stallion ', Old Saxon wrenioAs., Old English wraene^ horny, lustful '; 
Old High German wrenno^ stallion ' is back-borrowed from Middle Latin (under the 
influence of common Celtic -ns-, -nt- > -nn-). 

uerse/i-:\-aWv\ {*gverres) verres, -/is'boar', Lithuanian i/eAS/is'calf, Latvian versis^ox, 
rother, cattle'. 

References: compare in general Persson root extension 47, 85 f., Johansson KZ. 30, 418, 
IF. 2, 60 ff., Persson Beitr. 604 f., 845 (also against connection of ^ers- with ers-). About 
Finnish vesi, stem i/e/e 'water' s. Mikkola Mel. van Ginneken 137. 

WP. I 252 f., 268 f., WH. I 81 f., Pokorny Urillyrier 93, 105, 159, 169, Specht Dekl. 18 f., 
Trautmann 20, 334, 337, Schwyzer Gr. Gr. I 519, 548, 838. 

Page(s): 78-81 

=====8560

oman-m. " favour, assistance, protection ', 

oma-h' comrade '; Old Indie av/far-m. " patron, sponsor, patronizer ' (from which 2- 

syllable root form as Fut. avisyati, Perf. 2. Sg. avitha, as well as participle Ota- and:) utf-h^ 

delivery, help'; 

Armenian aviun' violent desire, longing; esp. irrational whim, caprice, or immoderate 
passion, lust ' (Petersson Et. Misz. 8); 

gr. -aFovsq in 2. part of Greek family names ( 'laov£(;)? compare Kretschmer Gl. 18, 232 
f., different Schwyzer Gr. Gr. I 487, 3; 521 ; diTac; (Theokrit) " friend, lover '; 

Latin aved, -eAg" (basis at/e[/]- as in preceding) " be eager, have a wild desire, long for, 
desire ', avidus " desiring, longing for; esp. greedy for money, avaricious ' (therefrom 
audeo, -ere^ to be daring; to dare, venture, bring oneself to '), avarus^ covetous, greedy '; 

Old Irish c;o/7d/" protects', cymr. etvy/Zys "favor, wish desire', corn, aweir desire', abr. a- 
/i7/"unaided, wantonly, voluntarily'. Middle Breton eoull, youlF favor, wish desire ', as a 
name component in gall. Av/-cantus {=abret Eucant), acymr. Euilaun , also in Old High 
German names as Awileib, Awo; compare Gothic awi-liut^\d{i\c„ suxapiaria'; mcymr. ri-m- 
aw' he grants to me ', cymr. ad-aw {\N\t\r\ negat. at-) " leave ', abret. di-eteguetic 
"abandoned, forsaken, deserted, destitute' {*di-at-aw-etid). 

Falk-Torp 1407 adds also an: Old High German odi. Old Saxon othi. Old English Adj. 
Tet^e, Adv. eat^e^ easy, comfortable ', Old High German odmuoti. Old Saxon othmodi 
"modest'. Old English eaA'/77do'" modest'. Old Norse audmJOkr^ to move easily, willing, 
modest ', 

audkendr^ to recognize easily '; basic meaning is " willing ', from which " to make easy '; 
formal Germanic /oparticiple-formation to an//- (example Germanic aut^ia-^ deserted; flat; 
waste; empty; abandoned; blasted; desolate; bleak; grey; gray; barren; stuffy; dull; 
tedious '?). Rather uncertainly. 



If also Old Lithuanian austis' refresh oneself, atausimas^ refreshment ', Latvian ataust 
" recover, refresh ', atauseV invigorate, refresh ' are used, the zero grade lies to them *aus 
- of in Old Indie avas-, gr. £v-rin<; present as a basis es-stem . Or = Lithuanian aust/" get 
cold ', ausyti^ cool '? 

Tocharian B au-lare, A olar^ comrade '; as dubious B omaute^ longing ', w-ar(fny 
crave, long for', A w-aste " protection ' with angebl. zero grade the root rather here wa- " 
give ', A 1.Sg. M/5a(Pedersen Tochar. 186). 

References: WP. I 19, WH. I 81, 850, Van Windekens Lexique 9, 79, 153, 157. 
Page(s): 77-78 

Root / lemma: auo-s {*ohuhha§) 

Meaning: grandfather 
======457a
Page(s): 456-457 

Root / lemma: ghreib- 

Meaning: to grab 

Note: compare also ghrdd^-. 

Material: Gothic greipan^ grasp ', Old Icelandic grfpa' grasp, gripe ', Old English Old 

Saxon grTpan6s., Old Frisian grfpa. Old High German grTfan6s., in addition as iterative 



Old English grapian, Old High German greifon^ caress ', and Norn, agentis Old Icelandic 
greipi. "handle, grasp, span, hand'. Old English grap^ixsi, handle, grasp'. Old High 
German gre/falork', Old English gr/'pam. " handful, fascicle, sheaf; in addition Old 
Icelandic gr/prm. ' preciousness, valuable possession ', Old English gripe m. "handle, 
grasp, attack, jewel'. Old Frisian bi-gripxw. " statute; agreement'. Old High German ana- 
griff^ attacking, specially of a free girl without agreement of her parents ', Middle High 
German grif^ snatch, palpation, grasp ', Middle Low German gripe, ^/lepe "handle, grasp, 
fork'; 
Maybe alb. grep^hooV! from a Romance derivative also Italian grappa ^\r\ook'. 

Lithuanian griebiu, griebt/ {besides greibiu, grelbti) " snatch at, seize, gripe ', intensive 
graibau, graibyti, gribsn/sm. " quick grasp, grabbing ', Latvian gribai. " wish, volition ', 
gribef want ' (originally " reach for something '). 

References: WP. I 647, Trautmann 96. 
Page(s): 457-458 

Root / lemma: ghrem-1 

Meaning: to scratch, rub 

=====457b
£Xp1a9r|v, xpTorot;), YS>\o\c, " smearing; anointing; colouring, varnish, wash; colour-washing 
', XP^MCi. new xpTcfMCi " ointment; anything smeared on; anointing, unction; of spiritual grace; 
coating of wall, plaster ', £YXP^w " to rub, anoint; sting, prick '; xpiMtttu) ' wander above the 
surface, scratch ' etc.; Med. " bring near; touch the surface of a body, graze, scratch; draw 
near, approach '; 

Old Icelandic gnma^mask, helmet; riddle ', engl. grime^ dirt, smut ', Old English Old 
Saxon gnma, -cm. "mask, helmet; ghost'. Middle Low German grJmeV lined in black ', 
ablaut, gremei. "smut'; 

Lithuanian gn'eju, grieti^ skim the cream ' (older present form greju), grairnas' cream'; 
with transference in the mental area (compare similar under giireu-) here Germanic ^/ts- in 
Old English a-^/7S5/7 "shudder, fear, dread', grisiic, Old High German ^/7se/7//77 "terrible. 



grisly', mnl. gnsen, Middle Low German gnsen, ^rese/? "shudder', greselTk^ eerie ' 
(different Wood Mod. Phil. 5, 265: to Old \nd\c J/'-hret/^ feel shame ', wherewith Johansson 
IF. 2, 44 are connected under a basic meaning "*cover'. Old Icelandic gnma etc.); after 
Kluge'''' s. v. Gr/esgram here Old English gr/sfn. " milling ', Old Saxon gr/st-gr/mmo' 
bruxism ', Old High German gr/st-gr/mmon 6s. (besides grus-gramon 6s.); out of it Middle 
High German grisgram 6s.; perhaps also Old English gristlei. 'gristle'. Old Frisian Middle 
Low German gristel6s., also Old English grost. Middle High German gruschel 6s. 

References: WP. I 646 f. 
Page(s): 457 

Root / lemma: ghreu-1 : ghrau- : ghru- 

Meaning: to fall down
```


## [2026-09-07T20:18:48.113Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '93640,93690p' POK_full.txt"
}
```


### [2026-09-07T20:18:48.168Z] TOOL RESULT

```
Page(s): 36 

Root / lemma: h2anata{hienatS) 

Meaning: door posts 

Material: Old Indie a/a (usually PL atahas Latin antae) " encirclement, Rahmen a door', 

Avestan ^i&yakVk. PI. " doorposts ', Armenian dr-and^ doorpost ' (HiJbschmann Arm. 

Stud. I 19); Latin a/7/ae after Vitruv 3, 2, 2 "die frei endigenden and vornetwas verstarkten 



Wande, die den Pronaos eines Tempels or die Prostaseines Hauses enclose, surround ' = 
Old Norse (?/7o'"Vorzimmer' (Bugge KZ. 19, 401). 
References: WP. I 59, WH. I 52. 
Page(s): 42 

Root / lemma: h^u-8, h2auei- 

Meaning: to perceive, understand 

Material: Old Indie -avati\N\Vc\ ucf-an6 pra- "aufmerken, heed'. Old Church Slavic umt 

"reason' (basic form *au-mo-)\ moreover Tocharian B c»/r7-/75/c»/ro/7/7e 'meditation'? Different 

Pedersen, Tochar. 223 Anm. 

a^itz/s-; lengthened grade Old Indie av/s Adv. 'apparent, manifest, obvious, bemerkbar', 
Avestan avisMv. 'apparent, manifest, obvious, vorAugen' (npers. 55/ra/' 'clear, bright'; Old 
Indie avistya-h, Avestan 5K/sy5-'offenkundig'); Old Church Slavic ave, jave Mn. 'kund, 
apparent, manifest, obvious' (in ending after den Adjektivadverbien auf -e reshaped from 
*avb, whereof:) aviti, javiti^ reveal, kundmachen, show' (Lithuanian di/y//s'sich in Traume 
sehen lassen' loanword from dem Slavic). 

Maybe alb. ya 'there it is' Slavic loanword 

full grade: gr. aia6avopai, Aor. aia6£a6ai 'perceive' (*aFia-6-); Latin a^o'/o'hear' from 
* auiz-d^-io, compare oboedio\xo'C(\ * 6b-avizdhid aboui *oboTdid\ gr. dico (neologism to 
Aor.£TT-riia(a)a, aiov) 'vernehme, hear' (*aFia-), £naiaTO(; 'belongs, ruchbar, known'. 

Here probably Hittite u-uh-hi^\ see, observe', a-us-zi' sees ', 3-^-/7-/5 (from a-'u-wa-ri-is) 
'Ausschau, Warte', iterat. ^s/r- 'wiederholt sehen'. 

References: WP. I 17, WH. I 80, Trautmann 21, Pedersen Hittitisch 172 f. 
Page(s): 78 

Root / lemma: ba>^mb-, b^a>^irio^-, paf^mp-, phaf^mfj^- 

Meaning: to swell
```


## [2026-09-07T20:18:49.076Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (108,109,110,111):\n    t=d[leaf]\n    print('=== leaf',leaf,'===')\n    print(t[:1500])\nEOF"
}
```


### [2026-09-07T20:18:50.416Z] TOOL RESULT

```
=== leaf 108 ===
chere';
air.  ad-gladur  ,ich  rede  an'.
Die  ar.  Worte  können  aber  ebensogut  mit  idg.  r  zu  got.  gretan  gehören ; s.  unter  1.  gher-.
WP.  I  659  f.
ghleu-  , fröhlich  sein,  scherzen',  Erweiterung  von  gJiel-  , schreien'  oder  ghel- , glänzen'  ?
Gr.  x^fiviy  f.  , Scherz,  Spott';
aisl.  gly  n.  ,Freude',  ags.  gleo,  glieg,  gllw  n.  , Spiel,  Freude'.
Mit  dentaler  Erweiterung:
alit.  glaudas  m.,  glauda  f.  , Kurzweil',  gldudoti  , scherzen',  lett.  glauddt ds.  [glaudas  , Liebkosungen'  gehört  aber  ursprünglich  zu  glaüsti,  lett. glaüst  ,anschmiegen,  streicheln,  liebkosen',  lit.  glaudüs  ,sich  anschmiegend, einschmeichlerisch';  s.  unter  1.  gel-,  Erweiterung  gl-eu-l.
'Mit  m- Ableitung  (Nominalbildung  ghloumos) i
aisl.  glaumr  ,lärmender  Jubel',  gleyma  ,vergessen,  fröhlichen  Lärm machen',  ags.  gleam  , Jubel,  Freude';  ablaut.  aisl.  glymr  ,Krach,  Lärm', glymja  ,tönen',  mhd.  glumen  , dröhnen';
aksl.  hez^  gluma  ,constans',  glamiti  se  ,döoX€ax^^^'p  russ.  gium  , Scherz, Spott',  giumith  sja  , spotten,  sich  lustig  machen  über',  bulg.  glüma  ,Spaß, Scherz,  Spott',  glumjd  se  , scherzen,  spaßen',  skr.  glüma  f. , Scherz,  Lustspiel', öech.  (alt)  hluma  ,histrio',  poln.  dial.  la  ghcm  ,in  Nichts',  eigtl.  ,im  Scherze'.
Mit  j9-Ableitung:
slav.  *glup^,  russ.  giüjpyj  ,dumm,  albern',  Specht  KZ.  68,  123.
WP.  1*660  f.,  Trautmann  91.
ghö  ,hinter,  nach,  wegen',  Präposition 
=== leaf 109 ===
dschaft,  Liebe**
ahd.  geil,  as.  gel  , übermütig,  üppig,  kräftig',  nhd.  geil  (mnd.  geil^ , Hoden',  nhd,  Biher-geil-  mnd.  geile,  nhd.  Geile  ,Dung,  Dünger'),  ags.  g^l ,lustig,  lüstern,  stolz',  mhd.  geilen  , lustig  machen'  =  got.  gailjan  ,erf reuen'* ahd.  keili  f.  , Lüsternheit' ;
ablautend  und  z.  T.  mit  der  Bedeutung  , aufschäumend'  aisl.  gil-ker , Gärbottich',  norw.  gil,  gll  n.  ,Bier  im  Gären',  ndl.  giß  ds.,  gijlen  ,gären', auch,  wie  mnd.  gllen,  , begehrlich';
alit.   gailas  , heftig',   lit.   gailüs  ,jähzornig;   scharf,   beißend   (von  Essi«^ Lauge);  bitter  (von  Tränen);   kläglich,  mitleidig'  (in  letzterer  Bedeutung    - mit  Ablautentgleisung  zu   gilits  , schmerzhaft',   gelti  , stechen,    schmerzen' nach  Trautmann  Bsl.  Wb.  75?);
aksl.  dzelo  (zälo),  acech.  zielo,  weißruss.  do  zeia  ,sehr'.
WP.  I  634,  Feist  185,  Trautmann  75.
ghom-  , Stall'.
Arm.  gom  ,Höhlenstall' ;
dän.  gamme  , Schafstall',  schwed.  dial.  gamme  , Krippe',  anord.  gammx m.  , Erdhütte',  Schweiz,  gämmeli  , Viehhütte',  pomm.  gamm  ,Haufe  von Ziegelsteinen,  die  zum  Trocknen  aufgesetzt  werden'.
WP.  I  637,  Holthausen  Awn.  Wb.  80.
ghos-  ,essen,  fressen,  verzehren'.
Ai.  ghas-  ,essen,  verzehren'  in  2.  3.  Sg.  Aor.  dghas,  3.  PL  dksan,  Perf. jaghäsa,  jaksuh,  woraus  nach  Wackernagel  KZ.  41,  309  das  VväiS.  jaksiti, Part.  Perf.  *gdha-  in  agdhäd  ,ungegessenes  essend',  späte
=== leaf 110 ===
iv l*ghs-enue?)  s.  v.  Blumenthal  Gl.  20,  288.
WF.  f  640,  WH.  I  660  f.,  662  f. i
ghou{e)-  .wahrnehmen,  Rücksicht  nehmen  auf.
Lat.  faveö,  -ere,  fcLvt,  fautum  ,bin  gewogen,  bin  günstig,  schweige  beim Gottesdienst';  favtre  aus  "^fovire  wegen  umhr.fons  ,favens',  foner  ,faventes' aus  ^-fouenis]
aisl.  gä  (*gawön)  .achtgeben,  sich  kümmern',  got.  gaumjan  ,bemerken, sehen,  seine  Aufmerksamkeit  richten  auf,  anord.  geyma  ,beachten,  sorgen für,  hüten',  ags.  gieman,  as.  gömian,  ahd.  goumen  ds.,  aisl.  gaumr  m.  und gaum  f.  , Aufmerksamkeit',  ahd.  gouma  , Aufmerken.  Schmaus',  Schweiz. gaume  ,kleine  Kinder  hüten'  (aus  dem  Germ.  lett.  gaüme  , Geschmack', gßümet  ,sich  merken,  beobachten,  schmecken'),  as.  göma  , Mahlzeit,  Gast- mahl', wovon  as.  gömian  , bewirten'.  (Die  Bedeutungsverhältnisse  sind  im einzelnen  noch  zu  klären;  s.  Slotty  IF.  46,  369.)  Dazu  ablautend  ags. ofergumian  , vernachlässigen',  as.  fargumön  .versäumen',  isl.  guma  ,achten auf ;
aksl.  govdjg,  goveti  ,verehren',  russ.  goveth  , fasten',  sloven.  dial.  goveti .mürrisch  schweigen',  skr.  ghvijem,  gbvjeti  , gehorchen',  cech.  hoveti  , be- günstigen, schonen,  nachsehen';  aus  dem  Russ.  stammt  lit.  gavUi  , fasten', lett.  gavet  ds.
WP.  I  635  f.,  WH.  I  465.
ghou-ro-s  ,furchtbar'  und  ,voller  Furcht'.
Ai.  ghörd-h  , furchtbar,  ehrfurchtgebietend',  n.  ,unheimliche  Gewalt,  Zauber- macht';
g
=== leaf 111 ===
 ghrö-i  gbro-  , wachsen,  grünen';  ghrös-  :  gbrds-  ,Gras,  Pflanzen- trieb'; nur  germanisch  (und  slavisch?). Got.  gi^as  n.  ,Gras,  Kraut',  aisl.  as.  gras,  ags.  grcBs,  gcers  ds.,  ahd.  gras, nhd.  Gras]    vollstufig   mhd.  gruose   f.  ,junger   Pflanzentrieb,   Pflanzensaft', mnd.  gröse  f.  , Pflanzensaft',  mnl.  groese  ,junges  Grün,  junges  Gras';
ohne  die  5- Ableitung:  aisl.  gröa  , wachsen,  geheilt  werden',  ags.  gröwan , grünen,  blühen',  engl,  grotv,  ahd.  gruoen,  gruowan,  mhd.  griiejen  ,wachseD, gedeihen,  grünen';  aisl.  grödi  m.  ,Wachstum',  mhd.  gruot  f.  ,das  Grünen, frischer  Wuchs';  ahd.  gruoni,  mhd.  grüene,  ags.  gräene,  aisl.  grenn  ,grün, neu,  gut';   Grenaland  , Grönland'.
Mit  Dentalerweiterung:  ags.  gr'^d  m.  ,Gras',  mhd.  graz, -zzes  Junge Zweige  von  Nadelholz'  aus  ghre-t-,  ghrd-t-'j
wahrscheinlich  zu  ghre- :  ghrö- :  glird-  ,hervorstechen,  z.  B.  von  Pflanzen- trieben, Pflanzenstacheln,  Barthaaren'  und  dessen  leichter  Grundwz.  gher- ds.  (s.  dort) ;  auf  letztere  wäre  lat.  herha  ,Pflanze,  Halm,  Kraut'  zu  be- ziehen, wenn  aus  mit  *gherz-dhä  , Gerste'  suffixal  gleichartigem  *gher-dhä.
Berneker  355  erwägt  zweifelnd  für  aksl.  grozdz  ,Traube',  grozm  ds.  ein verwandtes  *ghras-dho-,  -nu-  als  Grundlage ;  die  Bedeutung  wäre  allenfalls durch  russ.  grdnka  ,Büschel'  :  bulg.  skr.  grdna  , Zweig'  zu    rechtfertigen.
WP.  I  645  f.,  WH.  I  616  f
```


## [2026-09-07T20:19:07.473Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghous\\|gaosa\\|niyöš\\|niyosT\\|gaus-\\|ghösati\\|ghosati\" POK_02.txt | head -20"
}
```


### [2026-09-07T20:19:07.521Z] TOOL RESULT

```
1598:.  Daß  nhd.  Gosche,  Gusche,  ndd.  goske,  guske  ,großes  Maul'  als  sÄ:-Bildung hierher  gehöre  oder  aber  etwa  mit  ai.  ghösati  ,ruft,  schreit'  verwandt  sei (s.  Persson  Beitr.  116  f.),  ist  bei  einem  Trivialausdruck  ohne  verfolgbare Geschichte  nicht  wahrscheinlich;
1683:ghous'  ,tönen,  hören'?   Nur  indoiranisch.  J^
1684:Ai.  ghö^ati  , ertönt,  verkündet  laut,  hört',  ghösdyati  ,findet  Erhörung bei  (Akk.)'  (Geldner  Rigveda  in  Auswahl  I  58),  ghösa-h  m.  , Getön,  Qe, schrei,  Ruf,  Lärm',  Asvaghösa  EN  ,Pferdeohr',  Harighösa  EN  ,GelbohrV (=  av.  zairigaosa) ;
1685:av.  gao^-  ,hören',  Kaus.  in  güsayat-uxöa-  ,sein  Wort  zu  Gehör  bringend*/ npers.  niyösidan  ,hören,  horchen,  lauschen',  bal.  gösay  , hören',  niyöSay ,hören,  horchen,  lauschen',  afgh.  ngvaf.ql  ,horchen,  gehorchen',  apers. gausa-,  av.  gaosa-  m.  ,Ohr',  npers.  ^ös  ,Ohr',  skyth.  EN  ^Pad-aywaog  ,init dem  Kriegswagen  rasselnd',  av.  zairi-gaoSa-  ,mit  gelben  Ohren';  '.•^-
```


## [2026-09-07T20:19:11.752Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nidx=d.find(\"ghous'\")\nleaf=d[:idx].count('\\f')\nprint('leaf(0-based)',leaf, '=> printed p ~', leaf+344)\nprint(d[idx-200:idx+1400])\nEOF"
}
```


### [2026-09-07T20:19:13.048Z] TOOL RESULT

```
leaf(0-based) 110 => printed p ~ 454
und  Dissimilationen,  dazu  as. gornön,  gnornön,  grornön  ^trauern',  gruri  m.  , Schreck';
klruss.  zuryty  ^betrüben',  zurha  , Sorget  russ.  zurith  , ausschelten'.
WP.  I  636,  Feist  208.
ghous'  ,tönen,  hören'?   Nur  indoiranisch.  J^
Ai.  ghö^ati  , ertönt,  verkündet  laut,  hört',  ghösdyati  ,findet  Erhörung bei  (Akk.)'  (Geldner  Rigveda  in  Auswahl  I  58),  ghösa-h  m.  , Getön,  Qe, schrei,  Ruf,  Lärm',  Asvaghösa  EN  ,Pferdeohr',  Harighösa  EN  ,GelbohrV (=  av.  zairigaosa) ;
av.  gao^-  ,hören',  Kaus.  in  güsayat-uxöa-  ,sein  Wort  zu  Gehör  bringend*/ npers.  niyösidan  ,hören,  horchen,  lauschen',  bal.  gösay  , hören',  niyöSay ,hören,  horchen,  lauschen',  afgh.  ngvaf.ql  ,horchen,  gehorchen',  apers. gausa-,  av.  gaosa-  m.  ,Ohr',  npers.  ^ös  ,Ohr',  skyth.  EN  ^Pad-aywaog  ,init dem  Kriegswagen  rasselnd',  av.  zairi-gaoSa-  ,mit  gelben  Ohren';  '.•^-
über  lat.  heus  ,he,  holla,  höre'   s.  vielmehr  WH.  I  643  f.  y-
WP.  I  569,  WH.  I  643  f.  ^5-
(ghre- :)  ghrö-i  gbro-  , wachsen,  grünen';  ghrös-  :  gbrds-  ,Gras,  Pflanzen- trieb'; nur  germanisch  (und  slavisch?). Got.  gi^as  n.  ,Gras,  Kraut',  aisl.  as.  gras,  ags.  grcBs,  gcers  ds.,  ahd.  gras, nhd.  Gras]    vollstufig   mhd.  gruose   f.  ,junger   Pflanzentrieb,   Pflanzensaft', mnd.  gröse  f.  , Pflanzensaft',  mnl.  groese  ,junges  Grün,  junges  Gras';
ohne  die  5- Ableitung:  aisl.  gröa  , wachsen,  geheilt  werden',  ags.  gröwan , grünen,  blühen',  engl,  grotv,  ahd.  gruoen,  gruowan,  mhd.  griiejen  ,wachseD, gedeihen,
```


## [2026-09-07T20:19:41.260Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT gaosa ===\" && grep -n \"gao[sš]a\\|gaoša\" BRT.txt | head -25 && echo \"=== BRT nigaosa/nigus ===\" && grep -n -i \"ni-gao\\|nigao\\|gūšaya\\|gusaya\" BRT.txt | head -20"
}
```


### [2026-09-07T20:19:41.329Z] TOOL RESULT

```
=== BRT gaosa ===
5955:asrutgaosa-
9893:KompE.  —  Komp.:  gaosa-+*d-iiara-  (zum  V. 'Äd-,  S  2**37)  m-  'wasiraOhtEetragen  wird'.
14496:•  j.  9-raDh-  n.  'Mund':  -arg  (NS.)'>  F. 23.  a)  Du.  'die  Mundwinkel' :  nazdyd  . . ya^a  *näaha  haca  *gaosalibya  yaha vä  gaosa  haca  ^'anhibya'^  "näher .. als  die Nase  von  den  Ohren  oder  als  die  Ohren von    den   Mundwinkeln   (entfernt    sind)"
18941:•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
21124:2  a):  mit  tnaslm  ,  .  masyä  hacaite  J^fnJJ  möglich  oder  denkbar  hingestellt;  nur  c)  im xratu^ y  mtir»mcii  ..  halatie  äinasHl\\Pi.vt.\  a)  mit  Opt:  hö  mqm  ava'ha xratusYt  10.107.  zuzb):  hsuca  ..vohu^VTrmqm  nijaintHsÄ.)  y  v»Arkd..barf%ryät manB jiig)r)bustarU  anhai yS ..y  häti y5 ..  \^/iaca pui:r»m  midafy.dairyat(sd.)'V.iff.3S V.4.48;  F._yf,  V. /_J.  42,  43;  — ■  staotärpm' — y  .,  nmänS.paitim  paiti  tard.pikwtm vaf9hat?h>m  , .  aoxta  ahurS..y°  aäm  yat  .dai^yät  aha  astryäti  V.y.20;  A-^J.?; vaAist?mY.i0.g;  —  nazdyS akmi ..vTspahe\ —  th  yüioyänti  .,  mqnaytn  ake  y  .. ar?hsui*'maiiihca .  .y  Stsha  haca  *gaosalibya  \  ra%ailta  . .  haca  saäst  (sd.)  .  .  paiti.yntta y  vä  gaosa  haca  *%rar»hibya  (sd.)  P.  26';  I  Yt /J.  67;  —  tä  he  stiai^iifia  var^'äjosca
21933:nazdyö  ya%a   änha  haca  *gaosalibya  ya%a
21934:V  gaosa  haca  *'^ranMbya  'P.28;  V.S.22 PUZ.(?};  —  yai^a  .  .  asii  .  .  ganmshva (sd.)  vfdante  yal  v° . .  ganma  (sd.)  3^ar3%  a stamamm  vä  (zu  III)  hisvam  vä  apa.- dazai  V.  15. 4 ;  —  yat  hl  nazdistS  dahmS  vJ.- srunvaili  (sd.)  yavat  v  atm  aitn  havaiibyä unbya  N.  27;  —  yat  hxi  spä  .  .  aiwi.- vantaiti  .  .  vayB  v  hl .  .  avi  usvataite FrW.  U;  —  ayatthainaU  kantais  atdibli paiti  ava.hr3%yät  (sd.)  .  .  masyS  (sd.)  v akmstcit  V.4.50.  II)  v  steht  beim zweiten  und  den  folgenden  Gliedern;  zu  I); B)  im  gAw.:  d?manahyä  xsdisnm  ssi- hrahyä  v  dahySu^  v°  "domus  regnum vel  pagi  vel  provinciae"  Y.jr.  16;  — "ä  *«I d^mätum  vls>m  v'  iöi^rtm  v  dahyüm  v° adät  duStäiiä.)cä  . .  Y.J/.  18.  C)  im jAw.:  yasca  ,  .  bayqm  ahunaht  vairyeJte maräl  frä  v°  marS  dr?njayäi  frä  v  drvn- /ayö  srävayät  frä  »• . .  Y.  jg.  6.        zu  2);
26761:avatghtm  (sd.)  Y.jrf-4;  ^T.  vciwcndel    Ny.       „  ^  AKri-i;  vgl.  »neh  «e»..  mhd.  j^^  'steif. J.  10;  — _y5  ^ijH   ahmäi  västravaitim  stsi       itatüich';  Bthl,  IF.  ii.  ijS. »tTj-J/fSp.  i38so.)  Y.50.2;— ^^"/(f  WT'«Ä/  ,  j    stiptay-  £  Name  eines  Insekts,  das *ustä  *j/»"    "denen  wir  beide  wünschen,   auf    Hunden    sclimaroUt':     duye    navaüi dass    es    ihnen    nach    Wunsch    gehe"    ^.  galwqm  pairi.yaoidaihtta   -tibyasca    ans- 4ß-i6;    —    a/    "i-^J    »tStighi    *J>aourvm  iritib}asca    -.yamiraHbyasca    vUpaäbyasca mazää  *ya^m  (sd)  stSi  Y.31.8;  —  nSil  pairi  aHitaäbyS  ySi  gahwam  pairiiavaiti spmiqm    dSTist  (Sp.  690  a)    ahmäi    stü  "zweimal  neunzig  Hunde  soll  er  von  St. armaitlm   \.4g.2-,  —   Ayat  ..  Bist  (Sp.   reinigen   und  von  An.  und  Vy.   und  von 430  m.)  ..  ahmäi  slH  dqn  ^JA  K/<7yfii/7|  ^11  den  bösesten  (Insekten),  die  auf  Hunden \.4S.io;  —    data  xratius  hixi-3  rai^ltit   schmarotzen"  V. 74.17. (sd.)  stöi  mahyä  räifng  .  .  iähil  ¥.50.6;!      Eig.  Bed.   und   Et.?    —    Pa,:    ddrptkrak, —  tum  tiB  äiraom  *tafftasU'>  "du,  O  A>.,  I      halb  {jap)  twtsskr. sollst  unser  Z.   sein"   Vr.j.7.        a)  im  •  j.   stivant*  in.  EN.   eines  Gläubigen: jAw,    mit    der   Negation,    in    altnbuüveja  /r3dat.vawhfus  •talö  aiaotiS  Yt  IJ.  121. Gebrauch  'der  nicht  existireQ  kann,  den      Ablcit.  mos  'siay-i    Bed.7 es  nicht  geben  kann' ^:  nöil  ma^S  gal^yj   •    j.    siai',    sli'i',    nur   KompA.:    sva. Sil  agjä  (sd.)  sunaiaoiti  gaosaiwe  "es  gibt ;  "stüra-.
27909:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
27921:•  j.  zairi.gaosa-  Adj.  "mit  gelben,  gold- farbigen Ohren':  spanim  .  .  spaStim  'sim V.if.  16'  17,  18;  —  aspahe  ..  aurus'afie .  .  'sähe  Yt.Äi8.
28980:Sp.  928  o.)  ist  weggelassen:  danys.Hli (sd.)  ile  vTse  afrJnämi  yahmat  h°  imti zaoira  y.SS.i^;  \t.  S.  4'.  '  b)  bei NomiDa";  o)  bei  verbalen  Substantiven: raiis  i&i.;  'decessum')  rm  A^  ariha  ztmat vaähs  k^nnaoili  Vt.  17.  20;  —  spmtat  h" mainyaot  aisam  ahr^m  ('origo')  FrW. 70,40;  —  yä  h"  daSnayUt  .  ,  apastüilis ('abdicatio'j  ^.4J-  ß)  bei  Raumwörtera: dsräl  Cprocul')  A'  ahmiil  nmänät  .  .  ays i^yejä . .*yeyenH yeAhe ..  Y.57,  14;  14';  — nSii . .  *dräjyS  ('longius')  *'iyeillm  framraomi (sd.)  . .  ä/rllim  yUnat  -4'  .  .  P.  7j;  — nazdyS  ('propius')  ahmi  . .  yaia  änha  k' *gaosaHöya  P.  2  V;  28;  —  airime  gätüm hs nUhthaüta  . .  *psr3ntanm  (sd.;  'seorsum') h'  anyanbyS  mazdayasna^byS  V.g.  33;  29; —  aiai  dräjö  ('quantam  longitudinem')  h* i!^ral\.  3. 16;  16^;  — yS  hn%rS.masar»h3m iS/wamm  ('viam  miUe  passuum')  h'  vizibys paräiti  V.  JJ.  18;  —  äiat  ('quantum*)  h' mtiya^bya  Y.i).  10;  8f.';  —  avavat  ('tan- tum')  h'  paourt-aiibya  yäha  %rigilim  V. 1M39;  II,  76;  — yd  *yujyastxm  (sd.)  h' gat^abyS  parätti  'v.  7^.  17;  N.  8,  <??(?), V,_j.  17*,  J(5'.4*,  17. 4«,  b)  im  gÄw. a)  bei  Verben  (bei  solchen  der  Bewegung nicht  bezeugt):  frg  ma  sl/iJ  (Sp.  1575  o.) "iiwahmut  *vaoca^hl  *mainy}us  h'  'üwä Siaiihn  "..  pronuntiare  ex  tuo  , tuum  os"  Y.  28. 11;  —  ysi  gSus  h'  iyävtl (sd.)  "qui  a  bove  (habitant  sva.)  stant' Y.  J7.  a";  —  ka^ü  . .  zarjm  (sd.)  laränl h'  xsmap''  ",  .  impetrem  a  vobis  (sva. per  vos)"  Y.  44-17;  —  a^byS  mazdh  .  . xsäi^rät  A'  paifi.mraot  ". .  per  Regnum (deum)  respondit"  Y.ya.  2;  —  sonst mit  'asa-  A  (als  Gottheit)  im  Sinn  von 'peri^nim,  As'o  juvante  (u.  dgl.)':  aiät  h'
29707:gaosahe  Y.  j.  3;    —    mikräi  .  ,  'rö.gaoiäi  yäha   yat    'pam    halnam    avazöit  ,  ,  V,
29735:•  j.  hazaDrä.gaosa-  Adj. :  s.  unter  Aata- igra-g".
=== BRT nigaosa/nigus ===
```


## [2026-09-07T20:19:42.730Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\" && grep -n -i \"niyoš\\|niyōš\\|nigōš\\|gōš\\|gos'\\|ear'\" PHD.txt | head -30"
}
```


### [2026-09-07T20:19:42.785Z] TOOL RESULT

```
=== PHD ===
516:—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen. nin [KON < A k‘n | M, J поп] now.
2913:New Year's day пӧвгӧг.
```


## [2026-09-07T20:19:56.396Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r\"gaosa-\\s*\\+|gaosa-.{0,40}Ohr\", p):\n        print('=== leaf',i,'~col',(i-10)*2 or '?')\n        for m in re.finditer(r\"gaosa\", p):\n            print(p[max(0,m.start()-300):m.start()+400].replace('\\n',' '))\n            print('---')\n        break\nEOF"
}
```


### [2026-09-07T20:19:58.021Z] TOOL RESULT

```
=== leaf 292 ~col 564
 s,  aber  Pt  4;  vgl. No.  I.  —  4)  Hds.  'iyä.  —  5)  Unthem.; S  4'^-  3-  —   *■>  Pl.  4.     NA.  ghiiä;  s.  No.  1. -  7)  Pü. :  fehlt. •  j.  gaoSävara-  m.,  Du.  'Ohrschtnuck, Ohrgehänge':  °ra  ca^ru.iarana  Yt. 5. 121, ij.  10.         [V.  74.15:  lies  matg'.] KompE.  —  Komp.:  gaosa-+*d-iiara-  (zum  V. 'Äd-,  S  2**37)  m-  'wasiraOhtEetragen  wird'. —  Vgl.  np.  gösvär  (aus  *gaiiia-iara-)  'Ohr- gehänge', ai.  ööAafana-  n.  'Schmuck'. •  j.  gaoSö.baraz-  f.  'Höhe  des  Ohrs': ä^ritlM  xsa'hrS.k^ntake  (sd.)  'zS  us.iäva- yuit{%±)  "^.46. Pü. :  göS  bäläk. •  j.  gaoäÖ.srüta-  Adj.  'vom  Ohr  gehört', von  xralav-  m.  'Weisheit'  sva.  'erlernt' (im  Gegensat
---
```


## [2026-09-07T20:20:06.549Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (291,292):\n    p=d[i]\n    print('==== leaf',i,'====')\n    print(p[:600])\n    j=p.find('gaoSa-')\n    print('...gaoSa- idx',j)\n    if j>0: print(p[max(0,j-1500):j+600])\nEOF"
}
```


### [2026-09-07T20:20:07.879Z] TOOL RESULT

```
==== leaf 291 ====
 Milch  enthaltend':  saoüra .  ,  haomavaiti  'vaiti  hanana^atavaiti  Y. C8.\;  —  sad^ram  ..  'vaitm  Y.6Ü.  i; —  saoi:rä  .  .  'vaitls  (AP.)  Y.  22.  a ;  — 'vaitibyS  zaohrSbyS  Yt.5.8;  Ä15,  Vd.p; saohranqm  .  .  'vaitinqm  Vt.  5.  63,  V.
'o/  gaonahe  (sd.)  avabarät  .  .  *dann3m   U-A,;  *Vd.  4\  —  nmafum  ..  ä%ravat^ a  va  *vat5  *bar}snv3  vä  paiH  vayhanaAe  ^-S-^i  —  airyamm  :fannU .  ,  'vaiflm
.  auf  der   rechten   Seite   des   haarigen (Rückenhöckers)  oder  oben  auf  dem  Kopf"
N.  65.
l'Q.i  hac  dtüin  afiar  vailat  (gescht.  i'')0  hae fiixai')  i  sil
...gaoSa- idx -1
==== leaf 292 ====
 V.  /j.  30  ".
BJ.  goflhana-  Adj.,  gasthäna-  n.;  mp.  (Pü.j ^slän.  —  I)  So  Jpi,  Mfa;  NA.  hat  ^avö.ü'. —  ä)  zSt.  s.  HHr5.slSna.  No.   l.
•  j.  gaoz-,    p.  gaud-    V.     'verberget Praes.  4   gusa-,    24   gutaya-,    30  (Iter.) gauiiayot,
'verbergen,  verstecken':  haom  tanSm guzaita  Yt  4~  4.
D  mit  apa  'verbergen,  verheimlichen' yadiy  imäm  htfdugam  afiagaudayäAy  Bh. i^iiiio; — avakyarädiy  mä  apagaudaya'' (aS.)  Bh.^io.
mit  a  'ins  Versteck  bringen':  yat  .  . äal  azftn  tanSm  aguse  atairi ..  "..dabe- gab  ich  mich  ins  Versteck  unter  .."   Y
...gaoSa- idx 2068
h  ins  Versteck  unter  .."   Yt.
mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
ai.  guhaH  'er  verbirgt'.    —    Npil.  (lu  Yt.  4);
dar  miyStt  guiäilan  (wegen  des  Anklaugs !).
•  j.  gao-zasta-  Adj.  'Milch  in  der  Hand habend,  mit  M.  in  der  Hand':  yasß  %wä .  .  fräyazSite  .  .  'td  Y.  62.  i ;  V.J.  1.
PQ.  (in  Y.)i  göit  dasl,  (lu  V.):  yäml^)  dast, mit  der  Bemerkung:  lui  ke  elön  gäuiet  fatkSß fTir-ofl;   s.  daiu  DST.  ZA.  2.  33.
•  j-,  g.  gaoS-  V.  'hören'.  Praes.  i  gus-, 3  gäid-,  30  (Kaus.)  güsaya-,  —  PPfP. 'guäa-.
'hören,  hören  auf  — ;  vernehmen'.  Med.: mi  eis  ai  V}  dngvatö  mahrascS gUsfä{^S.) säinasiä  {sd.)   Y.j/.  18,'   —  gültä  y!  ..
—  gaoio.sruta-  486
\  aÄnmM/ (sA.) . .  Y.  31.  19;  — y5  paoiryS aAuräi  . .  manasca  *gusta  säsnäsca  Yt  13. 87");  55')^  F.^f'>,  21;  —  at  fravaxsya na  *gäsiJ.däm  "'  nä  iraotä  "ich  will  reden: nun  vernehmet,  nun  höret"  Y.  45.  i ;  — sraotü  asä  güsahvä  tä  akura  "hören  soll es  A.f  vernimm  es,  o  Ah"  \.4g.'];  — yS  tu  aSvS  säsnä  (sd.)  güsaid  Y.  2g. 8.  a)  Kaus.:  s.  gasayat.'.
ai.  ghifali  'es  hallt  wieder',    mp.  (Pü.):  iiigä-
iilan,  np.  myösldan,  nbaJ.^äAiy,  PDs.  «a-jH^r/;
E.  dazu  Hbm.  PSt   104.   —   *)  In  Anlehnung
an  Y.  31.  18.  —  «  S  i68.  57. j.  goäl:  E.  igav,  igav;    F.  _J  g:  lies  gaosö.
•  p.  gauia-,  j.  gaoSa-,  g.  *g«uä.a-''  m. 'Ohr':'''''j&F._^g^';  — (ÄuvffjM  {^z.kSyum) 'fym  V.  (V,  44—46',  Q.  i6f.*;  —  sraotä *'gius.äiii'>  vakistd  "höret  mit  den  Ohren das  Beste"  Y._^.  z;  — _yaSa  *riär?Aa  haca *'saeibya'i>  ydha  vä  °/a  (ND.)  Aaca'*"Sira-
■  >ff/iiiya  (sd.)  P.  2A';  —  yai  kl  dahat  .  . \'same  (DD.)  sraoma  Ytlö'.  7;  —  suru- \naoiti  '■saiwe  (ID.)^^  YL/0. 107;  —  /Sm granß  .  .  barahi  . ,  afa  'sayä  sraoma Yt70. 23;  —  apa  's'a  (AD.)  taoiayäü (sd.)  YtJO.  48;  — laäamsaiy  Uta  näham Uta  'Sä  (AD.)  .  .  frajanam  Bh.  2. 13;  14; —  US  Vä
```


## [2026-09-07T20:20:24.707Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG gauš ==\" && grep -n -i \"gau[sš]\\|niyō[sš]\\|nig[oō][sš]\" CHEUNG.txt | head -40"
}
```


### [2026-09-07T20:20:24.757Z] TOOL RESULT

```
== CHEUNG gauš ==
558:(Skt. bharv), *gaus ‘to hear’ (Skt. ghos) and *nard ‘to lament, moan’ (Skt. nard), 
3456:outcome *m[ncs-, cf. byws- ‘to become silent’ < *apa-gaus(a)ia-. Also, m/ncsy- has 
8313:*gaus 115 
8363:*gauš ‘to hear, listen to’ 
8375:116 *gaus 
11951:*gausa-), mi, meh ‘ewe’ (< *mais?), on which see for instance, Cabolov 1997: 51. 
15107:gausa uta hazanam frajanam ‘I cut off his nose and ears and tongue’ vs. MSogd. bd 
56886:*gaus, *srau, *x$nau! 
57072:*gaus, *srau, *x$nau!
```


## [2026-09-07T20:20:26.595Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD_mackenzie ==\" && grep -n -i \"niyōš\\|niyoš\\|niyōxš\\|gōš\\|nigōš\" PHD_mackenzie.txt | head -30 && echo \"== NYB ==\" && grep -n -i \"niyōš\\|nigōš\\|gōš\\|gaus\\|niyoxs\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T20:20:26.666Z] TOOL RESULT

```
== PHD_mackenzie ==
== NYB ==
```


## [2026-09-07T20:20:29.801Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8355,8400p' CHEUNG.txt"
}
```


### [2026-09-07T20:20:29.844Z] TOOL RESULT

```
«PIE *geuH,- ‘to call upon’ = LIV: 189 | Pok.: 403 


*IE COGNATES: Gr. you ‘I lament, complain’, ОНС gi-kewen ‘to call’ 
*REFERENCES: КРЕТ. 80a Ё; Abaev, Slovar’ I: 65 f., 144; Werba 1997: 346 


*gauš ‘to hear, listen to’ 

*AVESTAN: gus- ‘to hear, listen to’ = Liste: 20 

MED.; Pres. athem.: INJ. 3sg. OAv. gusta (cf. Kellens — Pirart 1990: 239; Y 31.18 £); Aor. them.: INJ. 
3sg. OAv. güsatä (Y 29.8), IMPV. 2sg. OAv. güsahuua (Y 49.7), 2р1. OAv. güso.düm (Y 45.1); Partic.: 
pres. caus. YAv. guSaiiat® (<< *gaos^, Yt 13.16) 

*MIDDLE PERSIAN: MMP gws ‘ear’ || (+ *ni-) MMP nyws-, BMP n(y)dw(h)s- 
/niyös-/ ‘to hear’? > DMMPP: 168a, 255b 


116 *gaus 


(+ *ni-) Pres.: IND. 3pl. MMP nywsynd, BMP ndwhsynd /niyosénd/, SUBJ. 3pl. MMP nywš nd, IMPV. 
25р. BMP ndws /niyös/, 2р1. MMP nywsyd-ys ‘hear it/him’; Inf.: BMP nywhsytn /niyosidan/; Partic.: 
perf. pass. BMP ndwhsyt, BMP nydwhsyt /niyosid/ 

*PARTHIAN: gws ‘ear’ || (+ *apa-) 'bgws ‘silent’ (Henning 1958: 110) || (+ *uz-) 
(LW) 'zgwl- ‘to listen’ || (+ *ni-) ngws- ‘to hear’. 0 The change Ir. *§ > I in 'zgwl- 
seems to point to borrowing from an Elr. source, cf. Henning, BSOAS 10: 100; 
Morgenstierne apud Mayhofer 1966: 164. = Ghilain: 66 | DMMPP: 168a, 10b, 
101b, 241a 

(+ *ni-) Pres.: IND. 25р. ngws’, SUBJ. 25р. ngws’h, 3sg. псу”, IMPV. 2sg. ngwS-, 2р1. ngwSyd; Partic.: 
perf. pass. ngws'd 

*KHOTANESE: (+ *pati-) OKh. pyüs- (pyü’-) ‘to hear’(+ *ham-) LKh. hamggüs- ‘to 
heed’ > SGS: 87, 138 

*SOGDIAN: (+ *pati-) SSogd. ptyws, BSogd. pty’ws, CSogd. ptyws, MSogd. ptyws 
‘to hear’ || (+ *ni-) SSogd. nyws, BSogd. ny’ws, CSogd. nyws, MSogd. nyws ‘to 
hear, listen’ 

(+ *pati-) Widely attested: Pres.: IND. 150. SSogd. ptyws’m, SSogd. (*)pt.ywsm, dur. CSogd. "ptywsmsq, 
2sg. SSogd. ptywsy, 3sg. BSogd. pty’wst, BSogd., CSogd. ptywst, etc. || (+ *ni-) Widely attested: Pres.: 
IND. 3pl. BSogd. ny’ws’nt, OPT. 2sg. MSogd. nywsyy, 3sg. CSogd. nywsy, 1р1. CSogd. nywsym, 2pl.
```


## [2026-09-07T20:20:31.355Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD grep gos ==\" && grep -n -i \"listen\\|hearer\" PHD.txt | head -20 && echo \"== PHD_mackenzie head ==\" && head -c 600 PHD_mackenzie.txt && echo && echo \"== NYB grep listen ==\" && grep -n -i \"nigos\\|nigôs\\|niyos\\|listen\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:20:31.430Z] TOOL RESULT

```
== PHD grep gos ==
== PHD_mackenzie head ==
   A CONCISE
  PAHLAVI
DICTIONARY

     D. N. MAcKENZIE
      Professor of Iranian Studies
     at the University of Gottingen




        LONDON
OXFORD UNIVERSITY PRESS
     NEW YORK         TORONTO
       Oxford University Press, Walton Street, Oxford OX2 6DP
                       Oxford New York Toronto
               Delhi Bombay Calcutta Madras Karachi
              Petaling Jaya Singapore Hong Kong Tokyo
                  Nairobi Dar es Salaam Cape Town
                          Melbourne Auckland
                      and associated companies in
                     Beirut Berlin Ibad
== NYB grep listen ==
790:*ā-vēnišn [Pwynšn'] the act of blaming, disgracing a p:: vattarün ~ kartan to disgrace evil people 71%, opp. vehän pat pātdāšin (v.s. v. pat I:II) kartan to reward good people; — [kë an-tškēhtar ? han ke ~ i martömän vattar sahet ku niyäzömandeh who, is (the most not- poor =) the least affected by poverty? he who considers being blamed by men worse than being needy PT 95!-?; when a man makes his confession, hàn ke peš patit bavet (i.e. the priest-confessor) aš xup niyösisn, [MN-š for] api-§ ne ~ [MN-& for] api-$ rüz be ne barišn, ce ka pat vinčis i kart be āvēnēt aivāp rāz bē barét a�� havand bavet shall listen bene- volently (to the man confessing his sin), and he shall not disgrace him, nor divulge his secret, for if he disgraces him for the sin he has committed, or divulges his secret, he becomes equal to him Šnš 8: 9, p. 107, Cod. K 20 fol. 67 r.]. - Paz. avinesn
2779:niyöSitan [ndwkšytn'] to listen 90%. — Ps. pres. nydwhšyt = niyöxset; MPrth pres. ngwš-, MPrs nywš-; Paz. nyoxšidan, NP myēšīdan; < mi + Av. (485 sg.) gaoš-.
4711:talistenkongreB in Rom (23.-29. September 1935) überreicht vom Verlag J. J. Augustin in Glückstadt", pp. 13-19.
```


## [2026-09-07T20:20:42.623Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8400,8440p' CHEUNG.txt"
}
```


### [2026-09-07T20:20:42.668Z] TOOL RESULT

```
IND. 3pl. BSogd. ny’ws’nt, OPT. 2sg. MSogd. nywsyy, 3sg. CSogd. nywsy, 1р1. CSogd. nywsym, 2pl. 
BSogd. ny’ws’yö, IMPV. 2sg. SSogd. ny’ws, etc. 

*CHORESMIAN: -ywsy- (+ hrd-, s.v. *har-) ‘to warn’ || (+ *apa-) byws- ‘to be quiet’ || 
(+ *ni-) m[nyws- ‘to hear’, m/nywsy- (caus.) ‘to cause to hear” > Samadi: 91 f., 19, 
126 

*NWIR: NP gosidan/gos- ‘to hear, listen’, Bal. gösit/göS- ‘to listen’, NP gos, Bal. gos, 
Kurd. (Kurm.) gu(h) (m.), (Ѕог.) gwé, Zaz. gos ‘ear’ 

*NEIR: Oss. I. qus, D. Sos, Pash. ywaž, Sh. yüy, (Baj.) уйу, Rosh. убу, Bart. yü(”), 
Sariq. yewl, Yzgh. yovon ‘ear’, Rosh. yawoj (f.) ‘ear, handle of a vessel’ || (+ *pati-) 
Yghn. düyüs-/düyüsta ‘to hear’ || (+ *ni-) Pash. nyaZ-/nyutol, nywatal ‘to obey, 
listen’, Sh. niyüy-/niyuxt, (Baj.) niyaw-/niyuxt, Rosh. niyüy-/niyuXt, Bart. niyü(w)-/ 
niyuxt, Orosh. niyu(w)-/niyuyd, Yzgh. nayu"-/nayuxt, Yi. noyüy-/noyüsc-, M. 
nəyuy-/nəyúšk” ‘to listen’ || (+ *ui-) Oss. I. qoysyn/qoyst, D. igusun/igust ‘to be 
heard’, Oss. I. qusyn/g.yst, D. igosun/igust (caus.) ‘to hear, listen’ 

*SANSKRIT: ghos ‘to sound’ (RV+) © EWAia I: 518 

© Cognate forms outside Пг. are not attested. 

*PIE — — LIV: 200 | Pok.: 454 


*IE COGNATES: — 

*REFERENCES: Horn 1893: 210; EVP: 51; IFL: 231b; Andreev — PeSéereva: 249; EVS: 35b, 48a; Abaev, 
Slovar’ II: 334, 316 ff.; Nyberg II: 84; Werba 1997: 180; Cabolov 2001: 397 f.; NEVP: 56; Korn 2005: 
290, 399; Shahbakhsh: s.v. gos- 


*gaz ? 117 


*gauz ‘to hide, conceal’ 


*AVESTAN: Y Av. guz- ‘to hide, conceal’ = Liste: 20 

MED.; Pres. them.: IND. impf. 1sg. YAv. aguze (Yt 17.55 Ё), OPT. 35р. YAv. guzaéta (Yt 4.4), ? 3pl.
```


## [2026-09-07T20:20:44.587Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== mackenzie nyws ==\" && grep -n -i \"nyws\\|nywš\\|niyōšāg\\|niyosag\\|hearer\\|catechumen\" PHD_mackenzie.txt | head -20; echo \"== PHD.txt niyos ==\" && grep -n -i \"niyos\\|niyōs\\|nyws\" PHD.txt | head"
}
```


### [2026-09-07T20:20:44.646Z] TOOL RESULT

```
== mackenzie nyws ==
== PHD.txt niyos ==
```


## [2026-09-07T20:20:53.238Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '505,520p' PHD.txt"
}
```


### [2026-09-07T20:20:53.286Z] TOOL RESULT

```
P naxsag [nhšk! | P nxšg] good, fine.
nāxun [whwn! | N ~] (finger) nail.
naxust [nhwst' | M nxwst, N ~} first.
nay [KN YA < A gny’; та | N ~] reed, cane. nay-, v. nidan.
nay [nd | M my, N ~] tube, flute, clarion; pole, perch (10 ft.).
~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
nést 59 nihang
nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
nihuftan 60 nizar
nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
nizārīh 61 0$
—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen. nin [KON < A k‘n | M, J поп] now.
O
6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
6š 62 padiragih
368 Paws] dawn.
```


## [2026-09-07T20:21:02.297Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# leaf = printed + 21\nfor p in (210,205,206):\n    i=p+21\n    t=d[i]\n    print('=== printed p',p,'leaf',i,'===')\n    print(t[:2200])\nEOF"
}
```


### [2026-09-07T20:21:03.653Z] TOOL RESULT

```
=== printed p 210 leaf 231 ===
— 210 —
gör 'Grab*, dagegen, das Geiger neuerdings (Lautl.
des Bai. 53) mit ai. ghörd- grausig, furchtbar ver-
glichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein
semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
g*aur wohl nicht arab. kaßr (Hübschmann unter oss.
d. gaur, t. daur, S. 123), sondern vielmehr neupers.
gebr, gahr^) (vergl. Geiger, bei. LW. gaur, No. 81,
wo allerdings phlv. gabrä (semitisch!, nur *Mann
bedeutend) nicht als Grundform stehen durfte).
939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
vergl. bällden (No. 173).
ai. vi + {/^vardh- ^heranwachsen, gedeihen ; ist schon
im PehlevT verschwunden.
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
LW. afy. yva/a 'Fleisch'; kurd. güst; bei. gö$t, n.
göM (128); wa/. gust, minj. yös, sar. gü^t, siyn. goß,
^) Zuerst hat dies wohl Bückert, ZDMG. 10, 183 ausgesprochen.
«) Vergl. Fr. Müller, WZKM. 5, 263.
=== printed p 205 leaf 226 ===
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
=== printed p 206 leaf 227 ===
— 206 —
er auf gtisäde-dil 'fröhlich* verweist. Somit würde es
zur aw. [/sä-, gä&, äyCL^ 'weilen, ruhen, behagen' ge-
hören, zu der auch np. säd (No. 767) zu stellen ist
(Hübschmann, ZDM6. 38, 431). Da indess gusäde-
du u. a. m. sich sehr wohl aus der Bedeutung *offen
erklären lassen, so bleibt die Etymologie sehr zweifel-
haft. Barth olomae (briefl. Mitteilung) denkt daher
besser an Ableitung von einer aus ai. 1 l/'cay- weiter-
gebildeten i/^Ci/O- -f vi, ursprüngl. etwa vom Türvorhang
gesagt (vergl. ai. vi + 1 Kcay-, Bedeutungen 2 und 4).
Die Form mit A:, z. B. jehänkusäl 'Welteroberer , ist
jedenfalls trotz päz. ktisäden ohne etymologischen Wert.
924. fftisuften 'zerstreuen ; verwelken (Vis und RamTn,
S. 55 Vers 3)'; gusuf (gtfsöf) Zerstreuung.
aw. *vi + l^/saoh'; ai. vi 4- l^ksöbh- *in Bewegung,
in Schwanken, in Aufregung geraten*, Causat. skr. 'ver-
wirren*; phlv. v(i)söftan, Praes. v(i)söpet (Men., AV.),
v(i)söp(i)sn (ZPGL).
Verbessert aus kiisuften etc. der Wörterbücher.
Vergl. np. Osuften (No. 32).
925. ffusn ^Männchen, männlich*.
aw. varsni- männlich (Widder)'; phlv. gtisan, vergl.
N. pr. Gusnasp; ai. vfsni^ 'Widder*.
oss. t. Urs 'Hengst' (84).
LW. mand. xr^nj;, syr. n:51^in 'Hengst* (Nöldeke,
ZDM6. 28, 96 ; doch sind diese nicht aw. uysan- *Stier*,
ai. tiksdn- 'Stier, Ochse*, got. auhsa *Ochse'?).
926. guften sprechen, Praes. göy-etn, guftar 'Rede', gep,
'Witz.
g. gaf 'Gespräch*.
ap. \/^gaub', gauhataiy sprechen, sagen* ; phlv. guftan,
guftar, guv{i)Sn (geschrieben gub""), gtiv{i)smh, guv{i)smk,
kurd. giitin ; wa;^. Jög-am, sar. xtig-am,
927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
Daraus sind bokanntlich entlehnt it. ghdehhe ^ fr. julep^ sp.
julepe *Küliltrank*.
```


## [2026-09-07T20:21:12.336Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"niyös\\|nyös\\|nigös\\|niyö\" HRN.txt | head -20; echo \"=== HUB 104 ===\"; python3 - <<'EOF'\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[104+10][:2500])\nEOF"
}
```


### [2026-09-07T20:21:13.691Z] TOOL RESULT

```
7047:für erwiesen (vergl. np. niyösiden, No. 1070 An-
9243:1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
9247:bei. mgösag, niyösay (262).
20611:nigösag 1070.
20612:n. niyöiay 1070.
=== HUB 104 ===
— 104 -
1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
1064. Im Paz. stets ntro (Min. und Shk.) geschrieben !
1065. Die Etymologie ist lautlieh unmoglich. Nur ein
urspr. ^aniddid wiirde direct zu np. nl^ fiihren. Vgl.
oben Nr. 457 und Fr. M tiller, WZKM. 5, 67.
1067. Dazu afgh. LW. nes 'the sting of any venomous
animal, puncture, lancet'; nastar und nestar a lancet' ;
arm. LW. n§iirj nstrak Xanzette' (das ein phi. *mstir
voraussetzt). Np. nestar bei Fird. I, 46, 214.
1069. Ist nt/m zu sprechen, vgl. paz. n^m, afgh. LW. nlm,
Hier fehlt np. nlmroz 'Mittag' und n%ma *Halfte' = bal.
nemag 'Richtung, Seite*, phi. nBmak part, direction
etc. Gl. and Ind. 251, afgh. nBmai 'a half.
1070. Ich halte Horn's Ausfuhrungen fur richtig mit Ruck-
sicht auf bal. niyosay *horen, horchen, lauschen' und
afgh. nyvatql (3 pr. nyvaM) 'horchen auf, gehorchen',
die auf iran. *ni-gds zuruckgehen. Vgl. auch bal.
gosay 'horen', osset. yossun^ qustn *h6ren .
1071. Np. u, Uf vor Vocalen v und' {z,B. v-agar), Sale-
mann, Mittelp. Studien 235, Vullers, Fird. I,
Einl. XXVL
1072. Hierzu np. bdj mussitatio magorum' u. s. w. bei
Vullers, alter i^a;? 'Gemurmel, leises Recitiren reli-
gioser Formeln', Noldeke, Tab. p. 353, phi. vac
Gl. and Ind. 228, West, PT. I, Introduction p. 73.
Np. guvaza *Schelten' = skr. vivac- 'streitend, Streit'
(larmend, schreiend, tosend, Wettstreit, Schlacht' bei
Pischel-Geldner, Ved. Stud. I, 37).
1075. Lies Gazophyl. p. 289. Die Form auch bei Vullers.
Np. valana also aus Halan- = idg. *volonos? Lat.
volnus = idg. *volenos KZ. 32, 386.
1079. Die Zusammenstellung von varsang mit skr. urugqsa^
(Oppert, deLagarde, Fr. M tiller) = ap. *yarM-
sanha- ware lautlieh wohl moglich, hat aber an der
Bedeutung keinen gentigenden Halt. Horn's Ety-
mologie ist falsch. Wo findet sich das Wort?
1081. Wo findet sich phi. vijastak? Ich finde tiberall nur
Formen mit anlautendem g.
```


## [2026-09-07T20:21:21.003Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9240,9260p' HRN.txt; echo \"--- which printed page:\"; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read()\ni=d.find(\"1070. niyö\")\nprint('leaf',d[:i].count('\\f'),'=> printed p',d[:i].count('\\f')-21)\nEOF"
}
```


### [2026-09-07T20:21:22.391Z] TOOL RESULT

```
n. nSmSaf 'Mitternacht* (269) ; sar. L W. naim.
Vergl. D''i13X (Talmud) 'halb (sc. gar), nur zur
Hälfte (sc. gebraten)*, de Lagarde, Semitica I, 39.
1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
aw. *n? — \/gaos-, vergl. apa gaosay^iti; phlv.
n(i)yösJtany n(i)yö/sltan bezw. n(i)gösltan'') 'hören'; ai.
[/"ghöS'^ ghösati mit d 'hören, horchen auf.
bei. mgösag, niyösay (262).
>) Vergl. Fr. Müller, WZKM. 5, 265.
Die jüngere phlv. Form tiek liest Justi fZDMG. 46, 288) zwoi
Mal auf Gemmen (die letztere derselben, JRAS. XIII No. 45, die ich
ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
ZDMG. 11, 320 als semitisch (!) entziffert, worauf mich Herr Cler-
mont-Ganneau aufmerksam macht).
*) de Lagarde^s CBeitr. zur altb. Lex. 76) von Darmesteter
f6t. ir. I, 85 Note 2) wiederholte Erklärung aus aw. yao^nti' ist ver-
fehlt ; phlv. ftffJyö/Sitan^ das auch gelegentlich n(i)ybHltan geschrieben
sein kann (aber wo?), beruht auf einer im Pchlevl häufigen graphischen
Eigentümlichkeit.
Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
l/kar8', kasiian u. s. w.), vergl. auch bereits aw. pä^no" gegen ai.
--- which printed page:
leaf 260 => printed p 239
```


## [2026-09-07T20:21:38.043Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ('MON','BQT'):\n    print(k, json.dumps(d[k],ensure_ascii=False,indent=1)[:2500]); print()\n\""
}
```


### [2026-09-07T20:21:39.329Z] TOOL RESULT

```
MON {
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-v

BQT {
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


## [2026-09-07T20:21:46.091Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -c . BQT_v3_pages.txt BQT_v4_pages.txt 2>/dev/null; echo \"--- v3 گوشوار:\"; grep -n \"گوشوار\\|گوش‌وار\" BQT_v3_pages.txt | head; echo \"--- v4 نیوش:\"; grep -n \"نیوش\\|نغوش\" BQT_v4_pages.txt | head"
}
```


### [2026-09-07T20:21:46.190Z] TOOL RESULT

```
BQT_v4_pages.txt:20153
BQT_v3_pages.txt:37437
--- v3 گوشوار:
23356:گوشواره بگوش نکنند. بجای آ نگل میخگه ‎Players‏ گوش‌میگذارند
44385:‏و« فرهنک نظام » جمعاً بمنی لابق‌کردن )5 گوشواره ) « رشیدی *: ‎ .‏
48533:© گوخوار و گوشواره - نم اول . پهلوی 8051727 » تاوادبا ۱۲۱ ۴ » اوستایی
51300:بالدام پیکان باشد واز آن گوشواره سازند .
--- v4 نیوش:
5143:بپشت صورت چه‌هرچیزخوب راببهشت سبت کنند منیوش *۱- منم از غنیدن و کوش
7716:نانیوشان * - بکرناك با بای‌حطی م و خته خرما میباشد - و بمعنی خرام
7726:حرام نمکی کردن > « زشیدی > ۴ - رشیدی گوبد : « نانیوشان » ناشنیده و بی‌خبر >
7727:عرچند لغة ترکیبی صحیح است از : نا( انفی . سلب )+ نیوشان ( صفت فاعلی از نیوشیدن ).
9380:نغوشا کیدن ۱ * آزدینی بدین‌دیگر را کوبند۷ - و بمعنی راه دور ودراز هم آمده
9392:۲ - رك : نفوسه - ۴ -ارك : نفوسه , وقی : نیوشه (ه.م.)
11194:زدن وکفنگوی شخصی کردن را نیز کفتهاند ۰ | نیوش است که ازشنیدن وگوش کردن باشد 8 -
11208:۰ ۴ - «نوسته, گربه درکلو- وفر‌باد؛ وظاهرآً تصحیف‌نیوشه است که عن‌قریبمرقوم‌شود.»
11209:« رشیدی > ؛ «نیوشه > هم باین معنی مصحف «شنوشه » (۶.م.) ۳ سنوسه ۳ اشنوسه (ه.م.) ات
11211:اغك بارید ویس نیوشه گرفت باز بفزود گفتهای دراز -
```


## [2026-09-07T20:21:53.481Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ndef show(f, lineno, before=25, after=15):\n    lines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    # find nearest preceding [pdf page N]\n    tag=None\n    for i in range(lineno-1,-1,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]', lines[i])\n        if m: tag=m.group(1); tagline=i+1; break\n    print(f, 'line',lineno,'pdf page',tag,'(tag at line',tagline,')')\n    print('\\n'.join(lines[lineno-before:lineno+after]))\n    print('======')\nshow('BQT_v3_pages.txt', 48533)\nEOF"
}
```


### [2026-09-07T20:21:54.800Z] TOOL RESULT

```
BQT_v3_pages.txt line 48533 pdf page 655 (tag at line 48466 )
و ‎OT‏ غلاف مروارید ‎ol‏ - و پیاله ای را نیز
کویندکه از صدف سازند .

‏گوش موش ه بکسر ‎tS. att‏
است کهآترا مرزنگوش‌خوانند ۷ وآن خوشبوی
میباشد و ‎FSS OT Ey‏ موش میمالد وبعرمی
آنان‌الفار خوانشد .

‏گوش ‎ONG‏ » بکس نون . کنابه
از سخن شنیدن ومتوجه شدن باشد - و کنابه‌از
ترك دادن و وا کذاشتن هم ‎Rice‏

‏گوشوادخ ‎CUS‏ - کنابه از ساء
نو باشد که ماء يك شبه است و بعریی هلال

‏(۱) چش : - ونگاه داشتن . ‎ey)‏ ۱ : هم .
(۳) چش : - با ینگری . (4) خو ۱ : - قرفت .
۱ - ودفت کردن» مواظبت کردن : «بدانك شیطان اهل کبابررا براهی‌باطل دعوت کرد ۰
کوش دارید تا درآن ‎atts‏ .» ( عوفی. جوامعالحکابات ‎Las‏ خطی کتابخانة ملی پارس ‎Bye‏
‎٩۵ Sup ۰ ۳6۲580 ۰, ۹‏ ص ‎٩‏ ب ). ۴ - ‎«oo Shi‏ نگاهبانی کردن :
- ای ملك‌المرش مرادش بده وز خطر چشم بدش دا رگوش ۱
« حافظ شیرازی . مسحح قزونی ص ‎ONAN‏
‏۴ از :کوش + که ( پسوند صفیر و شباهت ). ۴ - ره :کوش کردن .
6 کوبند : « سراپا کوش کشت .© ‎٩‏ - رك : موزنگوش .
© گوخوار و گوشواره - نم اول . پهلوی 8051727 » تاوادبا ۱۲۱ ۴ » اوستایی
انوم , کردی ‎uy» 2۵87 , ghohark , gthar‏ ی ۳۷۱ ۰ ‎il.‏ گوش(«م.)
‎spt‏ ( اوستابی ۷۵۳6 ‎SC‏ بر ( بردن ) ؛ آنچه کوش میبرد و حمل میکند ؛ ‎The‏ گوش ۰
زینتی که در کوش آوبز ند - اطاق با بالاخانه‌ای که د ركوشة تالار واقع باشد .
‎le, (‏ فاطع ۲۲۵ )
[pdf page 656]
SS

وا

است که ‎Wey‏ باشد 6 .

‎GE Le ۱ UP gh‏ فارسی بر وزن
مودار, نام جالوری است که س رگین را کلوله کند
و بگردانه وغلطان غلطان ‎Glogs‏ خود بردوآنر!
عربان خنفاء میگوبند .
======
```


## [2026-09-07T20:22:04.545Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1858 2>&1 | head -60"
}
```


### [2026-09-07T20:22:12.047Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 653; check the printed number and re-run with --pdf-page if off)
REF: BQT:1858  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 653  OCR-lang: fas

کوش افتادن ۳ -۱۸۵۹-<
کنیده و سین بی‌قطه و بای فارسی زده»بممنی | انتظارکشیدن و منتظربودن باشد .
خواب دیدن باشد که عربان روما گویند -ویمعنی گوش بستر - بکربای ابجدوسکون
احتلام و شیطانی شدن هم هست - وجوانیرا نیز | سین بی‌نقطه وافتح نای قرشت , نام شخسی بوده
گوبند که هنوز خطش ندمیده باشد . که چون اسکندرنوالفرنین متوجه شهربابل‌میشد
وش افقادن «کنایه ازکر شدن | در اننای راه بکوصی رسید بی عظم و در دامن
و ناشنودن گوش باشد . آنکوه دریایی بود » لشکرباش بشکار مشغول
#وشان - با نانی مجپول بر وزن شدند و مردیرا بافتند بز رکه جنه ودرشت اعضا
ها قردة انگور راگوبند و پر موی و پهن کوش . کوبند پغنی کوش او
جوشان » عسیر و فشرده ر ۰ ۰ 5
جوشانه ۱ را | بمثابه‌ای بو د که چونْ خوابیدی ي كکوی‌را بستر
< برورن رورانه » بمفی و کوش دیگر را لحاف کردی » نزد اسکندر
کوشه وکمینگاه باشد . آوردند » تحقیق احوال او کرد و نام او راپرسید
هه وردند » تحقیق احوال او کرد و نام او راپرسی
موش آوای (۰) - با واو بالف گفت که : مرا «گوش بتر > نغادند نام ۳ .
کنیده بتحتانی زده . شخصیراگوبن د که هرچیز گوش یچ - بسنی کوشال است -
شنود خوب فهم کند و بادگیرد . و پارچه‌ای را نیز گوبن د که بجهت دفع سرما بر
گوش بدر - بکر بای ابجد وفتح دورسر وگوش پیجند .
ولو کون ری برشله (۲) ۰ بستی کی بر | کوش پیچیدده کنایه از کرد
آواز است که منتظر واقظارکش باشد . باشد - وگو مال داده را نیز گوبند .
موش بردا شقن - کنایه ازناامید گوشت ۴ - بنتح اول وثانی وسکون
شدن و قطم نظر‌کردن از انتظار باشد ؛ و در ثالك و فوقانی » نام یکی از شششآوازه موسیقی
جای دیگربممتیاتظا ر کشیدن بنظرآمده است؟. است که (۳) آن نوروز و مایه وسلمك و گوشت
وش بر در داشتن « کنابه از | وشپناز وکردانیه باشد .
(۱) چك » چش : کوش آوایی . (۷) چش : رای قرشت . (۳) چش : و .
۱- قی :کوشه : * اگر مراهزیست دادند ترك ازمیستان کیرم و بهمان کوشانه راضی
شوم .> «تاریخ سیستان م۴۵۱۲ ۰ ۴ - باین معنی«گوش بردر داشتن > است. .
۴ - فردوسی‌طوسی درهلشکن کشیدن سکندر سوی‌بابل» آرد (شاهنامدیخ ج۷اصش۱۹*۹):
سکندر سیه اسوی بال کشید ز کرد سیه شد جهان ناپدید ...
پدید آمد از دور مردی ست رکه پر از موی و با گوشهای بز رکه
تنش زبرموی اشرون همچو لیل دو کوشش بیهنای دو گوش پیل
چودیدندگردان کی زین شان ببردند پیش سکندر . کعان
سکندر نگه کرد زو خیره ماند بروین همی نام بزدان بخواند
«چهمردی؟» بد و گفت «ونام توچیست؟» « زدربا چه یابی وکام توچیست ؟»
بد و گفت : «شاها ! مرا پاب‌ومام همی گوشی بستر نهادند نام ... >
قی : کلی م گوشان .
۴ -پارسی باستان 7 582115014 « هوبشمان ۹۸۶ * ۰ پپلوی 809121 » افقانی ع
8 . کردی 80811 ۰ بلوچی 8۵9151 , 8۵284 ۰ وخی 8581 . منجی 10و8۵ :
سربکلی 81151 ۰ شفتی 8051 « اسشق ۹۶4 ؛ ماده ارم وسر که استخوان بدن را می‌پوشاند
و پوشیده میشود از پوست بدن » لحم .
```


## [2026-09-07T20:22:20.220Z] TOOL CALL #35: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1858 --pdf-page 652 2>&1 | head -60"
}
```


### [2026-09-07T20:22:21.628Z] TOOL RESULT

```
REF: BQT:1858  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 653  OCR-lang: fas

کوش افتادن ۳ -۱۸۵۹-<
کنیده و سین بی‌قطه و بای فارسی زده»بممنی | انتظارکشیدن و منتظربودن باشد .
خواب دیدن باشد که عربان روما گویند -ویمعنی گوش بستر - بکربای ابجدوسکون
احتلام و شیطانی شدن هم هست - وجوانیرا نیز | سین بی‌نقطه وافتح نای قرشت , نام شخسی بوده
گوبند که هنوز خطش ندمیده باشد . که چون اسکندرنوالفرنین متوجه شهربابل‌میشد
وش افقادن «کنایه ازکر شدن | در اننای راه بکوصی رسید بی عظم و در دامن
و ناشنودن گوش باشد . آنکوه دریایی بود » لشکرباش بشکار مشغول
#وشان - با نانی مجپول بر وزن شدند و مردیرا بافتند بز رکه جنه ودرشت اعضا
ها قردة انگور راگوبند و پر موی و پهن کوش . کوبند پغنی کوش او
جوشان » عسیر و فشرده ر ۰ ۰ 5
جوشانه ۱ را | بمثابه‌ای بو د که چونْ خوابیدی ي كکوی‌را بستر
< برورن رورانه » بمفی و کوش دیگر را لحاف کردی » نزد اسکندر
کوشه وکمینگاه باشد . آوردند » تحقیق احوال او کرد و نام او راپرسید
هه وردند » تحقیق احوال او کرد و نام او راپرسی
موش آوای (۰) - با واو بالف گفت که : مرا «گوش بتر > نغادند نام ۳ .
کنیده بتحتانی زده . شخصیراگوبن د که هرچیز گوش یچ - بسنی کوشال است -
شنود خوب فهم کند و بادگیرد . و پارچه‌ای را نیز گوبن د که بجهت دفع سرما بر
گوش بدر - بکر بای ابجد وفتح دورسر وگوش پیجند .
ولو کون ری برشله (۲) ۰ بستی کی بر | کوش پیچیدده کنایه از کرد
آواز است که منتظر واقظارکش باشد . باشد - وگو مال داده را نیز گوبند .
موش بردا شقن - کنایه ازناامید گوشت ۴ - بنتح اول وثانی وسکون
شدن و قطم نظر‌کردن از انتظار باشد ؛ و در ثالك و فوقانی » نام یکی از شششآوازه موسیقی
جای دیگربممتیاتظا ر کشیدن بنظرآمده است؟. است که (۳) آن نوروز و مایه وسلمك و گوشت
وش بر در داشتن « کنابه از | وشپناز وکردانیه باشد .
(۱) چك » چش : کوش آوایی . (۷) چش : رای قرشت . (۳) چش : و .
۱- قی :کوشه : * اگر مراهزیست دادند ترك ازمیستان کیرم و بهمان کوشانه راضی
شوم .> «تاریخ سیستان م۴۵۱۲ ۰ ۴ - باین معنی«گوش بردر داشتن > است. .
۴ - فردوسی‌طوسی درهلشکن کشیدن سکندر سوی‌بابل» آرد (شاهنامدیخ ج۷اصش۱۹*۹):
سکندر سیه اسوی بال کشید ز کرد سیه شد جهان ناپدید ...
پدید آمد از دور مردی ست رکه پر از موی و با گوشهای بز رکه
تنش زبرموی اشرون همچو لیل دو کوشش بیهنای دو گوش پیل
چودیدندگردان کی زین شان ببردند پیش سکندر . کعان
سکندر نگه کرد زو خیره ماند بروین همی نام بزدان بخواند
«چهمردی؟» بد و گفت «ونام توچیست؟» « زدربا چه یابی وکام توچیست ؟»
بد و گفت : «شاها ! مرا پاب‌ومام همی گوشی بستر نهادند نام ... >
قی : کلی م گوشان .
۴ -پارسی باستان 7 582115014 « هوبشمان ۹۸۶ * ۰ پپلوی 809121 » افقانی ع
8 . کردی 80811 ۰ بلوچی 8۵9151 , 8۵284 ۰ وخی 8581 . منجی 10و8۵ :
سربکلی 81151 ۰ شفتی 8051 « اسشق ۹۶4 ؛ ماده ارم وسر که استخوان بدن را می‌پوشاند
و پوشیده میشود از پوست بدن » لحم .
```


## [2026-09-07T20:22:28.709Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]', txt)\n# blocks: [pre, num, content, num, content...]\nd={}\nfor i in range(1,len(blocks),2):\n    d[int(blocks[i])]=blocks[i+1]\nfor pg in (651,652):\n    print('##### pdf page',pg)\n    print(d.get(pg,'')[-2200:])\nEOF"
}
```


### [2026-09-07T20:22:30.111Z] TOOL RESULT

```
##### pdf page 651

کوزکند

گویند (۱) .
‎LPS‏ - با کاف فارسی بر وزن
نوشخند ۰ سخنان لاف ‎jy,‏ ودرو غ‌را گویند.
گود ‎CAP‏ - بنتح ال . بیخ کیاهی
است که در نظر چنان ‎UF Sauls‏ پنج شش
‎ast‏ کندم است که برهم چسییدماند و خوردن‌آن
منم آرزوی ‎Me‏ خوردن‌کند . گویند اگر يك
‎aL”‏ ازآن را با ده رطل عمل و ‎OT Shige‏
تيك درهم آمیز ند ودرظرفی-کرده سرآلرابگیر ند
در ساعت شراب رسيدة خوشگوار کردد و ‎OT‏
‏شراب فربهی آورد و قوت باء دهد و ‎NYT‏ معرب
کرده جوزجندم (۲) خوانشد .
گون ۱ - بنتح اول و انی و سکون
ه بفتح اول و انی و سکون
‎SM‏ ونون» ‎FF‏
‏ا زگاو کوهی باشد
وشاخهایاوبشاخهای
درخت خشك ‎att‏
‏مائد . کویندآب
کوشهای چشم او
ترباق‌زهرهاست_.

(۱) خم۱ : خوالند .

. ets ۱ ‏خم‎ (x)

)وا

گوده ۴ - با الی مجهول بروزن‌روزه.
‎GME‏ و غوزة خشخاش ‎May igs‏ ابربشم‌وامثال
‎faa SUT‏ و با زای فارسی هم آعده است .

گوذهر ۴ = بنتح اود و کس نانی
و قتح ‎elt‏ و سکون‌ها و رای فرشت ‎fade‏ ری
و ذنب راگوبند وآن دونقطة تقاطع فلك حامل
ومابل ‎pad‏ است و معرب‌آن جوزهر باشد .

گوده مح ‎Jol gee -f‏ ومیم‌وسکرن
خای نقطمدار , غلاف گل خرما راگویند.

گوز یه * ‎pie‏ اول بروزن‌لوزینه,
حلوائی ‎SaaS,‏ از مغ زکردکان پز ند .*

‎VOL‏ - مترون است کهبچة کاو
باشد - و بمعنی شتربچه و ‎SD‏ بچه و هر چیز
که‌آن کوچك و خورد سال ۷ ‎ath‏ هم‌هست چه
کوبمعنی‌خرد و کوچك‌نیز آمد» است۸ ؛ و کاهی
بطریق کنانه بجوانان بسمقل ‎Jol‏ عمرهم استعمال

‎(EUS OL gr‏ - کنابه از بیج
تور اس ت که برج دویم باشد از جملة دوازده‌برج

‏(۲) چش : - فلك ()

‏۱ - پپلوی 88722700 > اونوالا ۸۷ » ؛ ‎oF‏ معمولی جانوری است از ‎Bal gle‏ پر
شاخان از شخوار کنندکان ۰ که در جنگلپا زست کند . شاخهای ‎OT‏ هرسال می‌افتد و سالبسد

‎oh,‏ شاخ اضافی درمی‌آید . ركك : گوز.

‏۴ - غوزه (هم.) ‏ غوژه , ‎Ny‏ کوزغه .

‏۴ ۰( معرب ) جوزهر ‎Cpe)‏ در پندهش فصل 0 ‎ae‏ ۷ «گوزهر» و « موش پریك»

‏با سیارات مریوط ‎tb‏ شده ضد ماه و خورشید میباشند « پورداود | ‎Le‏ ج٩‏ ص ۱۹۵ ‎٩‏ .

‏۴ - از :گوژه (هم) مخ (خرما) (هم.) .

‏نبت). بهلوی ‎guctnak‏ > اونوالا ‎٩۳‏ >

‏۵ - از: کوز(کردو) (- بنه(یوند
۰ - از :کو )= کاو) +-ساله [ از : سال

‎Olay > gasile ‏[(آلء) . کردی‎ dbrlingskalb— ] JUS ‏سبت) دارای‎ aye) a+

‏۱ یز کردی 0۵8816 « ژابا س ۳4۹ > و رل : اسشق ۰۹4۱

‎. ‏خرد سل‎ - ٩

‏۸ - سحيح نیت . وکو | < گاو] («م.) ‎gine‏ مطلق‌جانوران اعلی است .

‏+ طوژ ‏ رك : کرژ.

##### pdf page 652

و۱۸۵ کوشلسب

فلك ‎#.(y)‏ است که مو کل ‎col‏ برمهمات‌خلوعالم ۴ . ول

گوسپند کشان - بنم کان ,روز | دوز چهاردهمازهرماه شمسی باشد وفارسیان درین
‎we‏ قربارا گویند ۷ . روزجشن کنند وعدسازند وآن‌را سیرسو رکویند

گوست ه بر وزن ‎on‏ کوفتگی ودرین روزسیربرادر ‎Shy‏ خوراد و گوشت رابا گیاء
کوفه‌شدسرا کویند؟ - وبسسنی کوی‌هر وت ی | و علف پزند نه با چوب وهیزم ‏ و گویش این
‎Hl‏ بز رکه باشد ۴ . ‎cols‏ امان یافتن از مس ‎Lay‏ جن است وبدان
‎os‏ دوای ‎yal pl‏ کنند که منسوب بجن‌است» ودرین

گوش ‎te‏ نی روزليك است فرزند بمکتب دادن وپیشه آموختن
ات ‎ARE‏ | تسش رتست
و بسن کنج )0 ‎“ES,‏ - و ‎tee‏ حفظ و ‎chiles‏ هم هسته .
همآمدماست- ونام‌فرشته‌ای ‎GS‏ گوشاسب ۱ - بنم اول و تالك بالف
(۱) چش : فلکی . ‎(x)‏ چش :کج ()
۱ - رك : التفپیم پیرونی س ۲۵۲ . ؟ - اسح « کوست» (ه.م.) است .

۴- اوستا - 88052 « بارتولمه ‎۶۸٩‏ > پهلوی ‎ns > BOSH‏ رکه ص ۸۳ >»پارسی
پاستان - ‎gausha‏ , هندی ‎ghosha - ott‏ ( صدا ) , کردی 80 ‎ghvagh gust.‏ ,
| 8005 » 405 . بلوچی ‎gdsh‏ , وخی ‎ghish . ghiish‏ « اسعق ۰۹:۳ .

۴ - اوستا ‎goush‏ » پپلوی ‎gush‏ ( لفة بمعنی کاو [ه.م.]) ‎ee‏ فرشتة نگهبان
چپارپایانست . لگهبانی روز چهاردهم هرماء با اين فرشته است . بقول بیرولی در < گوش روز ©
ازدیماء جشنی بوده است موسوم به « شیرسور * که درین روز سیر وشراب میخوردند و برای‌دقع
‎cle je Oke vl‏ ویژه با گوشت می‌پختند. زرتشتیان ‎pl‏ نیزاین روزرا « کوش» نامند.بیرولی
‎TH‏ جوش > ( معرب گوش ) و در سفدی « غش * و در خوارزمي « غوشت * آورده :

کوش روز ای تکار مشکین خال ‎59S‏ بربط بگیر و ليك بمال .
منود ‎ane‏ . ص ‎٩٩۲‏ >
‎Hy‏ : روزشماری بقلم لگارنده ی ۹-۳۲ کوش داشتن . ‎OS bie‏ :
ای ‎Abe‏ العرش مرادش بده وزخطر چتم بدش دا کوش .

« حاظ شرازی مصحح قزوینیصس۲ 4۱۹

۲ - رك :کوشاسب » بوشاسب .

* گومپند » گوسفند - بتلفظ قدیم 0 , 8657874 . و بتلفظ کنونی
40 . اوستا - 8805۳6008 . پهلوی 805۳804 « استق ۹4۷ ۰۰ مرکب از : کو
(گاو « ‎saw‏ مطلق جانوران ‎lal‏ سودمند ؛ و بقر ) +-سیند
( اوستا 5۳61012 بمعتی مقدس ( لفة یمنی جانور ‎(hal)‏ پاك
در پهلوی ‎js‏ کوسیند اسم مطلق جانوران اهلی است ) . اسم
اصلی جانوری که امروزه کوسفند نامیده میشود ۰ میش ( هدم. )
است ) « قاب ۱ص ۸۰ ؛ جالوری است از ‎Bal sls‏ تهی شاخان
از تشخوار کنند گان ‎chlo.‏ شاخ مورب . حلقوی و پیچاپیچ .
```


## [2026-09-07T20:22:43.088Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nlines=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef tagfor(ln):\n    for i in range(ln-1,-1,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]', lines[i])\n        if m: return int(m.group(1))\nfor ln in (9380,11194):\n    print('line',ln,'pdf page',tagfor(ln))\nprint('#### نغوشا region')\nprint('\\n'.join(lines[9360:9400]))\nprint('#### نیوش region')\nprint('\\n'.join(lines[11180:11225]))\nEOF"
}
```


### [2026-09-07T20:22:44.543Z] TOOL RESULT

```
line 9380 pdf page 236
line 11194 pdf page 279
#### نغوشا region
(< یوعیدن[۸.م.] تبدبل از به طق . فی: صطوزرقطواد < 00و رگرنه (یایش) « تاوادیا
س ۱۹۳) بممنی شنونده ومستمع وهمین کلمه آمت که عرب‌آنرا به « سماعون » ترجمه کرده
است » وآن پایین‌ترین ( پنجمین ) طبقه از طبقات مانوبان بود . رك : کربستشن ایا ؛ ترجمة
کربیتشن ( پاسمی ) ص ۱۲۵ ؛ رودکی . لفیسی ج ۳ص ۱۲۸۸ ؛ فرهنگه شاهنامة شقق :
نفوشا ؛ ومن‌پاب اطلاق جزه بکل بهمهٌ مانوبان اطلاق میشده : « اندروی ( سمرقند ) جایگاءه
مالوبانت » و ابشانر| شوشا که خوانند . > ۸« حدودالمالم مژلف بال ۳۷۲ چاپ تهران سس ۹۹ >
دقیقی در مفهوم اصلی آن اشتباه کرده » سوزنی سمرقندی ظاهراً مفپوم درست آنر| می‌شناخته +
ای نظامی کلکی بی سر و سامالی به اشوشا که وجهود ومغ وترسا مانی.
« فرهنگه نظام > .
و رك : مزدیسنا ص۳۲۱. اي ن کلمه ربطی این ندارد .
۴ - باین معنی رك : « فوشاکیدن >. ۴ << شوا (ه.م.) « شوشاکك مذه.
گبراست . پوشکور ( بلخی )گوید :
سخنگوی کشتی . سلیمات کرد غوشا که بودی » ملماات کرد.»
لفت فري ص ۰.۲۵۱
[pdf page 236]
۱۳۳ فوله
کیش وملتی بکیش و ملت دیگربرود - وبکس زمینی راکوبند که در صحرا و دامن کوه بجهت
اول ی زکنته‌اند . کوسفندان بازند* - ویم اول» ژرف وعنق ‎٩‏

نغوشا کیدن ۱ * آزدینی بدین‌دیگر را کوبند۷ - و بمعنی راه دور ودراز هم آمده
شدن واختیار دین دیگر کردترا کوبند . است ۸ - و بمعنی تمام و لهایت نیز گفته اند
نخوشه « بفتح اول و واو مجهول وشین همچنانکه کویند « فلانی‌درفلان هتراغول است»
نقطه دار » بمعنی نفوسه امست که دل شکستن بعنی بغور ونهایت آن رسیده است و درآن هنر
و تکین دل شکته دادن باشد ۴ - و بممنی | تمام است ‎٩‏ - و بکس اول» لردیان و زینه پایهٌ
کوش فرادادن بخن دوکس‌باشد که باهم آهسته سقف دار را کوبند ؛ و بسنی کوبند پوشش سر
حرف میزند ۴ . بردباست که پر بام خانه سازند نا باران بدرون
نو ۴ « بکس او وسکون آخر ,۱ یاب ۰۱۶
بمعنی لفوشاك است که کبر وجهود وآتش پرمت وله - با وارمجهول ولام بروزن‌تنوده,
باشد. + زلف خوبابراکویند ۰۱۱
ول « با واومجهول بروزن قبول, زیر :
۱ - از : شرعاکه+یدن ( پوند مصدری ). اه
۲ - رك : نفوسه - ۴ -ارك : نفوسه , وقی : نیوشه (ه.م.)
۴ - جهانگیری و رشیدی این صورت راآوزده‌اند وآن مصحف ومشفف « اشوشا4» است.
سدغل (مم.) ۹ - عمیق صحیح است. ۷ -< عمیق وژرف راخوانند

و بحر نغول وچاه نغول دربا با چاهی راکوبند که قمرآن بسیار ژرف و دور باشد و هر چه مانند

آن بود ت « جهانگیری :
از عدمها موی هستی هر زمان هت بپارب کاروان در کاروان
خاصه هردم(شب) جمله‌افکاروعقول لیست گردد غرق دریخن نفول...
#### نیوش region

‎٩‏ نوزنده » از دسائین « فرهنگه دساتیر ص ۲۷۱ > ۷ - دررشیدی «نوزه»

‏5 نوزده << نوازده ۶ اسشق ۱۶۶۸ « ژابا ص 42۲۵ >؛ بشم اول وفتح دال» پهلوی
‎٩ ) 882420 ( 8‏ نبیر که س ۱۵۵ ۰ اوستا 38۷841888 ( نوزدهم ) » هندی
باستان 26۷84888 ( نوزده ) » افغانی 00183 , 88888 ۰ استی 321438 » 81035 :اسشق
۸ کردی جع - ۵7 , 0۵2068 , 00202 ؛ زازا 68 - 86۷ « ژابا س ۸۲۵+
عدد نه بعلاوة ده » قدد بین هیجده و ابیست .
[pdf page 279]
نوی ۲۱۹۹۳
پروزن روزه ؛گرببان جامه را کوبند . نوسیره ؟ - بنتم اول ورای قرشت
نوس < با نانی‌مجپول بروزن‌طوی» | بروزن لوزینه » بمعنی یحث ومباحثه باشد .
قوی و قزح(۱) را کوبند ۱ - و تقلید حرف نوش - بنم اول بروزن کوش , مشقف
زدن وکفنگوی شخصی کردن را نیز کفتهاند ۰ | نیوش است که ازشنیدن وگوش کردن باشد 8 -
نوسته ۲ - بنم اول و اسکون نالی | ویمعتی نوشیدن وآشامیدن۹ - وکوارا وسا زکار
مجپول وسین بی نقطه وفتح فوقاتی, صدای کربه هم‌آمده است ۴ - و امر پاین دومعنی هم هت
راکویند که درکلو پیچد. . یمنی کوش کن وبشئو 9 - و بئوش و بیاشام ۸ -
نوسه ۴ - با نانی‌مجهول بروزن بوسه. | و بمعنی فاعل همهت ‎٩‏ که کوش کننده
قوس قزح راکوبند ؛ وباین معنی با شین‌نفطه‌رار ۱ وشنونده » وآشامنده‌ونوشنده۸ باشد*۱- ویمعنی
م آهده است. گوارا باد ونوش‌جان باد هم گفته‌اند ۵۱- وترباك
(۱) چنین است دردخ » وسحیح «قوی قزح» .
۱ - « نوی قوس قزح باشد . خسروالی گفت:
از باد روی] خوید چو آبست موج موج وز نوی پشت ابر چو چرغست رنگه رنگه.»
« لغت فرس چاپ هرن ص ۶4 درلغت فرس مصحح اقبال « نوس > نیامده وبجای آن «لوسه» آمده:
* نوسه » قوس قزح باشد . خسروالی گفت : ۱
از با ده کشت بینی چون آب موج موج وز لوسه ابر بینی چون‌جزع (چرغ)رنکه‌رنگه.»
« لغت فری ص ۶4۱>. رشیدی « نوس ولوسه > هن دو را آورده است.
۰ ۴ - «نوسته, گربه درکلو- وفر‌باد؛ وظاهرآً تصحیف‌نیوشه است که عن‌قریبمرقوم‌شود.»
« رشیدی > ؛ «نیوشه > هم باین معنی مصحف «شنوشه » (۶.م.) ۳ سنوسه ۳ اشنوسه (ه.م.) ات
چنالکه باقرب احتمال درين بیت :
اغك بارید ویس نیوشه گرفت باز بفزود گفتهای دراز -
( انومحمد بدیم بلخی . احوال رود کی . یی چ ۳ص ۳۰۰
تیوشه مصحف « شنوشه > است . ۴ -رك : نوی .
۴ - از دساتیر « فرهتگه دساتیر صس ۲۷۱ ۶ ۰ -ر4 : بیوشیدن .
۹ - ريش « نوشیدن > و اسم ا زآن, کردی 8081 (مشروب)؛ 805 ( اعتها) « ژابا
سس 2۲۵ ۰
خورشها بیاراست خوالیگران یکی پاك خوان از در مهترات
چوشد لوش‌خورده شاب آمدش کران‌شدسرش,رای‌خوابآمدش.
فردوسی طوسی « شاهنامةٌ بخ چاس*9 >.
۷ - ر4:ح۰۱۱ ۸ - رد : نوشیدن . ‎٩‏ - اسم فاعل مرخم .
*- در کلمات هر کب : زهرئوش » باده‌توش . ۱ مغفف « آنوشه > . اوستا
- 8880888 (بیم رکه » جاوید) « اسشق س ۱۳۵ ونيزشمارة ۶۱۲۸ ورك : بهار . تاریخ‌سیستان
س۷ ح ‎٩‏ . ورك : نوشدارو . درهنگام باده‌لوشی بمیگارکوبند (بستی‌نوش را درین‌مورد بمعنی
«گوارا باد» دانته‌اند ) :
بفرمانش مردم نهاده دو کوش ز رامش جهان بد پرآواز نوش,.
```


## [2026-09-07T20:22:54.645Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nlines=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ndef tagfor(ln):\n    for i in range(ln-1,-1,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]', lines[i])\n        if m: return int(m.group(1))\nfor i,l in enumerate(lines):\n    if re.search(r'یوشید|یوشه|نیوش', l) and i>11300:\n        print(i, tagfor(i), l[:160])\nEOF"
}
```


### [2026-09-07T20:22:56.072Z] TOOL RESULT

```
11476 286 گوارا وشیرین‌باشد ۷ - ومخفف نیوشین‌هم‌هت | وشکوفهای لوشکفته باشد -
11589 289 فارسی بر وزن‌بوفروش» نام پادشاه جز برمطرطانیوش نون - حرفی است ازحروف تیجی69
12928 321 بروزن پیشکش , جماع و مجاممت را کویند. نیوش ۱۴ یکسراول وضم نانی‌وسکون
12932 321 یور ۷ « بروزن زیور . بممنی کائنات نیوشا ۳(۱۴) - یکر اول وشین بالف
12936 321 (۳) چش : نیوشان .
12944 321 ۴۳- رك : یوعیدن . ارنگ آسم فاعل مرخم از «یوشیدن» .
12948 322 نیوشد ۱ - بروزن فروزد , بلفت زند | شنیدن کوش خود را درا زکند يا از پس‌دیوار واز
12952 322 نیو‌شنده ۴ - بکراول بروزن‌فروژند.. نیوشیدن ؟ « بکر اول بر وزن
12954 322 نیوشه ۴ - بکراوزوفتح شین‌نقطه‌داره | و بممتی جستن وطلبیدن وتفص ونجس لمودن
12958 322 ۱ - مضارع آزه‌ییوشیدن» (۸.م.) ۲ - رد : لیوشیدن .
12959 322 ارچ اس فاعل از« نیوشیدن» (م.) ۴ - از: یوش (۸.م.) ۸۳ (یونداس مصدره
12960 322 اسم معنی) رك : اسم مصدر بقلم نگارندم م۱۱ و رك: نیوشیدن؛ بممنی آرقب «ترصد » مرأقیت:
12963 322 8 رد3 : یوشیدن :
12964 322 چون بنشیند زمی معثیرجوشه کویدکایدون تماند جای نیوشه
12970 322 افوشا , شوشاك. هرن گوید : نیوشیدن » اوستایی 880512 - 381 ( شنیدن + گوش‌دادن). قی:
12981 322 آید هر ساعتی و پس بنیوشد تا شود هیچ قیل و با شود قال +
13997 347 ۷ #وریوشه (هم.) و رك : جهانگیری » رشیدی . فرهنگه نظام ."
15414 381 منیوش اگر بهوش و بیری وتیزویر +
```


## [2026-09-07T20:23:04.019Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nb=re.split(r'\\[pdf page (\\d+)\\]', txt)\nd={int(b[i]):b[i+1] for i in range(1,len(b),2)}\nfor pg in (321,322):\n    print('##### pdf',pg)\n    print(d[pg][:3000])\nEOF"
}
```


### [2026-09-07T20:23:05.334Z] TOOL RESULT

```
##### pdf 321

بواد ۲۳۸
نیو ۱۵۱ - بروزن‌میعاده بممنی‌شجات نیوراد ۸ - بارای قرشت بر وزن
باشد . و آن حالتی‌است که مردم ببب آن قوی | دیوزاد » بمعنی انتظام باشد وآن حالنی است مر
دل شولد . شی راکه تقدس وثربیت آمور میکند.
یوار ؟- بروزن دیوار» مابین زمین نیور یوار *- یک رای بی نقطه در
وآسمائرا کوبند و بعربی جو خوانند. چهپارم » بمعنی‌کائنات جواست بعنی چیزهای ی که
نیو‌اده «» با نانی‌مجهول بروزن‌بیچاره, ۱ در میان زمین وآسمان بهم میرسند همچو قوس
چوبی باشد که خمیر نانرا بدان پهن سازند ۴ . قح وشهب و نیازك و ذوات‌الاذناب *۱و برف
نیوباریدن ۴ - بنم او واتای . وبلران و ماشد‌آن , چه یور بممنی‌کائنات ونیوار
بمعنینه الباشتن وپرلکردن وفرونبودن ولبقکندن | بمعنی جو باشد.
باغد چه اوپاریدن بممنی فرو بردن و پر کردن نیوساو ۱۱() - بکراول و سین بی
وانباشتن و افکندن است ومذ کور شد که‌هرکام | نقطه بالف کشرده وبواو ددم بممنی پاینیده وی
نون مفتوحه برسر کلمه‌ای که همزه داشته باشن | زوال است و درعربی بقاه بالله خوانند.
پیاورند آن نون بمنزلهٌ لای فی است وآن‌عمزه یوسوم ۱۱- با سین بی نقله بروزن
بیای حطی تبدیل می باید . ِ ریگه بوم » شره و حرص بسیار باشد بر چیزی
نیو آش * - بکراول وفتح‌تای‌قرشت | خوردن . .
بروزن پیشکش , جماع و مجاممت را کویند. نیوش ۱۴ یکسراول وضم نانی‌وسکون
نیو آور ‎٩‏ - باتای قرشت بروزن فیل تالك و شین قرشت » امربشنیدن باشد ری کوش
ور » پممنی کبر وغرور باشد وآن بز رکه‌داشتن کن و بشنو - وشنونده را لیر کویند که فاعل
است ی خود را ودیگران را خرد شمردن. غنیدن است ۹۴.
یور ۷ « بروزن زیور . بممنی کائنات نیوشا ۳(۱۴) - یکر اول وشین بالف
باشد وکائنات در لغفت بممنی حاسلات است (۱) | کشیده » بمعنی‌شنواباشد که شنونده است- وفهم
پمنی آنچه در عالم حاصل شود . کننده ویادگیرنده رائیز گونند.
(۱) چش : باشد . (۷) چك » چش : لیوساد .
(۳) چش : نیوشان .
۱-ظ . بر ساختهٌ فرقةٌ آذرکیوان . ۴ بر ساختةٌ دساتیر « فرهنگه دساتیر
س ۰.۲۷۳ ۴ - وآترا « چویه» نیز گوبند . « جهانگیری > و رك : رشیدی .
۴ -فی از « اویاریدن > (ه.م.) - از دساتیر « فرهنگه دساتیر ص۲۷۳*.
۹ -ظ. برساخته فرقة‌آذ رکیوان . ۷ - از دساتیر : «فیور . بروزن زبورهآنچه
درکرء هو متکون وییدا شود.» « فرهنگه دساتیرضش۲۷۳ > ور : نیورنیوار» ور : قاب۱اص45.
۸-ظ . برساختهٌ فرقهآذ رکیوان. ‎٩‏ - ر4: یور . ۴ ر4: چهارمقالهٌ
عروضی طبع دوم نگارنده ‎٩‏ وتملیقات ص ۰۱۱-۹ ۱ ظ . برساختهٌ فرقهةٌ آترکیوان ۰
۴۳- رك : یوعیدن . ارنگ آسم فاعل مرخم از «یوشیدن» .
۴ - از: یوش (ربشه قمل * آمی) ۱ (پموند صفت مشبهه) . قن : شوشا» شوشا4.

##### pdf 322

ساهنده ابولا
نیوشد ۱ - بروزن فروزد , بلفت زند | شنیدن کوش خود را درا زکند يا از پس‌دیوار واز
وپازند(۱) بممنی آموزد و اد کیرد باشد که از | پس پرده و امثال‌آن کوش اندازد تا سخن ایعانر)
آموختن وباد کرفتن‌است؟ ؛ ودرفارسی بعنی کوش | بشنود وبجایی که نبایدگفت بگوید. واین «منی
کند و بشنود . را بمربی استراق سمع خواند 9 .
نیو‌شنده ۴ - بکراول بروزن‌فروژند.. نیوشیدن ؟ « بکر اول بر وزن
کوش کننده وشلونده راکویند + نکوهیدن » بممنی‌شنیدن ‏ وگو شش کردن باشد۷ -
نیوشه ۴ - بکراوزوفتح شین‌نقطه‌داره | و بممتی جستن وطلبیدن وتفص ونجس لمودن
گوت‌فر| داشتن باشد بحدیتی وآن کی‌راگوبند | هم آمده است.
که چون دوشخص باهم آهسته‌حرف زننداویجهت نیون ۸ - بکر اول بروزن ریوند »
() چك : ژد وپاژند .
۱ - مضارع آزه‌ییوشیدن» (۸.م.) ۲ - رد : لیوشیدن .
ارچ اس فاعل از« نیوشیدن» (م.) ۴ - از: یوش (۸.م.) ۸۳ (یونداس مصدره
اسم معنی) رك : اسم مصدر بقلم نگارندم م۱۱ و رك: نیوشیدن؛ بممنی آرقب «ترصد » مرأقیت:
همه نيوشهٌ خواجه بنیکوبی و ساح است همه نیوعهٌ نادان بجنگه وفتنه وغوغاست .
رو دکی‌سمرقندی «لفت فرس‌س ۲۱۷ و*شرح‌|حوال‌رود کی چاپ‌نفیسی‌ج۳س ۰6۱۰۵۰
8 رد3 : یوشیدن :
چون بنشیند زمی معثیرجوشه کویدکایدون تماند جای نیوشه
ورقکندسرخ مل برطل‌د وگوشه روشن کرددجهان ز گوعه‌بگوشه
کویدکاین می‌مرا نگردد نوشه تا نخورم باد شهریار عدومال .
۶ منوچهری دامغانی . دیوان س ۱۳۵
‎٩‏ - ۵9104520 ره از :یوش( م.)-یدن(پموند مسدری)؛پهلوی 210۵9101122
( غنیدن » مخفیانه گوش دادن ) » پازد 80253010888 ۰ ازط8۵5 « نیب رکه ی ۱۵۸کر4:
افوشا , شوشاك. هرن گوید : نیوشیدن » اوستایی 880512 - 381 ( شنیدن + گوش‌دادن). قی:
#1 رقط205ع 202 ۰ بپلوی قالط ۵5 000. 1۵0 1و۵ رنه مفی: صقالطی۵و(ناه
(شنیدن) ؛ هندی باستان ريعةٌ 80۵51 , [065081ق با غٌ ( شنیدن ,کوش دادن )ء بلوچی
58 دوه ط۵5توزه «اسعق ۱۶۷۰ هوبشمان قولهرن را در نشأت دق 81810۵902
( بهمین املاء ) ( شنیدن کوش دادن » استرانف سمع ) واففانی [8810۷818 ( شنیدن . اطامت
کردن ) . از ربشة ابرانی 8098 - 081 تأیید میکند . قسی بنیز بلوچی دلقع8۵588 (شنیدن),
استی 0099۱08لع ۰ ۹0918 (شنیدن ) « هوبشمان *۱*۶۷*.
۷ - فرستاده راگفت نیکو لیوتی بگو آنچه بشنیدی ای پیزهوش,
فردوسی طوسی ۶ لفت فری ص ۲۱۷*.
چون بخم اندر ززخم او بخروشد. یر زلد بی کمان و سخت بکوشد
مرد سر خمش استوار بیوشد تا بچگان از میان خم بنجوشد
آید هر ساعتی و پس بنیوشد تا شود هیچ قیل و با شود قال +
: منوچهری دامغانی . دبوان صس ۱۳۵ ۰
۸ - معتی اول . اظ برماختهٌ فرقهآذرکیوان .
```


## [2026-09-07T20:23:43.896Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON part2 نیوشیدن ==\"; grep -n -o \".\\{80\\}نیوشیدن.\\{120\\}\" MON_part2.txt | head -8; echo \"== نغوشا ==\"; grep -n -o \".\\{80\\}نغوشا.\\{140\\}\" MON_part2.txt | head -8; echo \"== گوشواره ==\"; grep -n -o \".\\{60\\}گوشواره.\\{120\\}\" MON_part2.txt | head -5"
}
```


### [2026-09-07T20:23:43.997Z] TOOL RESULT

```
== MON part2 نیوشیدن ==
== نغوشا ==
== گوشواره ==
```


## [2026-09-07T20:23:47.356Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c MON_part1.txt MON_part2.txt && head -c 400 MON_part2.txt && echo && grep -c \"گوش\" MON_part2.txt"
}
```


### [2026-09-07T20:23:47.414Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸
549
```


## [2026-09-07T20:23:51.870Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== نیوش ==\"; grep -n -o \".\\{40\\}نیوش.\\{100\\}\" MON_part2.txt | head -12; echo \"== نغوش ==\"; grep -n -o \".\\{40\\}نغوش.\\{110\\}\" MON_part2.txt | head -12; echo \"== گوشوار ==\"; grep -n -o \".\\{40\\}گوشوار.\\{90\\}\" MON_part2.txt | head -6"
}
```


### [2026-09-07T20:23:51.971Z] TOOL RESULT

```
== نیوش ==
== نغوش ==
== گوشوار ==
```


## [2026-09-07T20:23:57.750Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \".\\{20\\}گوشو.\\{80\\}\" MON_part2.txt | head -6; echo \"--- niyush attempts\"; grep -o \"نیوش\\|نغوش\\|نیوشی\" MON_part1.txt MON_part2.txt | sort | uniq -c | head"
}
```


### [2026-09-07T20:23:57.840Z] TOOL RESULT

```
--- niyush attempts
      5 MON_part2.txt:نغوش
      1 MON_part2.txt:نیوش
      1 MON_part2.txt:نیوشی
```


## [2026-09-07T20:24:02.966Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nfor w in ('نغوش','نیوش','گوشوار','گوشو'):\n    print('#####',w)\n    for m in re.finditer(w,t):\n        print(repr(t[max(0,m.start()-120):m.start()+200]))\n        print('--')\nEOF"
}
```


### [2026-09-07T20:24:04.345Z] TOOL RESULT

```
##### نغوش
'روار \n\n\n۰ \n\n\nاست؛. \n\nنغ نعو: ۱۰-6۲ [- نق\u200cنقو | (ص\u200cمر.) (عم.) \nکسی که نغ زند و بهانه جوید (بیشتر در مورد \nکودکان ابد.) \n\nنغوشاک: (قد. -۱۵۹2)0۵۵ [- نغوشا] \n(ص. .) شنو نده» مستعمع » سماع و آن به \nافراد پایین ترین (پنجمین) طبقه از طبقات \nمانویان اطلاق می\u200cشده. (من باب اطلاق جز و \nبکل) پیرو آیین مانی» مانوی. (به خطا) \nمرش ات'
--
'و: ۱۰-6۲ [- نق\u200cنقو | (ص\u200cمر.) (عم.) \nکسی که نغ زند و بهانه جوید (بیشتر در مورد \nکودکان ابد.) \n\nنغوشاک: (قد. -۱۵۹2)0۵۵ [- نغوشا] \n(ص. .) شنو نده» مستعمع » سماع و آن به \nافراد پایین ترین (پنجمین) طبقه از طبقات \nمانویان اطلاق می\u200cشده. (من باب اطلاق جز و \nبکل) پیرو آیین مانی» مانوی. (به خطا) \nمرش ات وا ۳۵۱ \nضح. ظاه را نغوشاک'
--
'بقه از طبقات \nمانویان اطلاق می\u200cشده. (من باب اطلاق جز و \nبکل) پیرو آیین مانی» مانوی. (به خطا) \nمرش ات وا ۳۵۱ \nضح. ظاه را نغوشاکث و نغوشا را به خطا هم \nریش مغوش - مگوش دانسته\u200cاند چنانکه \nمرحوم صادق هدایت بر این عقیده بوده \n(مجلهٌ موسیقی ۸:۲ ص ۲۵). (به خطا) \n1 \nترجمه کلمة «صانتئون» و «صاشن» همه جا \nنغوشاکان آمده است. (مان'
--
'ات \nمانویان اطلاق می\u200cشده. (من باب اطلاق جز و \nبکل) پیرو آیین مانی» مانوی. (به خطا) \nمرش ات وا ۳۵۱ \nضح. ظاه را نغوشاکث و نغوشا را به خطا هم \nریش مغوش - مگوش دانسته\u200cاند چنانکه \nمرحوم صادق هدایت بر این عقیده بوده \n(مجلهٌ موسیقی ۸:۲ ص ۲۵). (به خطا) \n1 \nترجمه کلمة «صانتئون» و «صاشن» همه جا \nنغوشاکان آمده است. (مانی و دین او'
--
'چنانکه \nمرحوم صادق هدایت بر این عقیده بوده \n(مجلهٌ موسیقی ۸:۲ ص ۲۵). (به خطا) \n1 \nترجمه کلمة «صانتئون» و «صاشن» همه جا \nنغوشاکان آمده است. (مانی و دین او. \n\n\nفرهنک فارسی معین بخن \n\n\nتقی\u200cزاده ص ۸۰ ۴.) \n\nنغول: (قد. 70۵۱« [- نغل] (ص.) \nکرد زررف. راه دور و دراز. ضسح.. \nهممجنانکه «عمیق» (معنی اول کلمه) در \nعربی به معنی دور '
--
##### نیوش
' - \nنفوشاک] (ص\u200cفا.) شنوا» شنونده. باد \nگیر نده» آموزنده. \n\nنیو شنده: (6-)0-2002 2:۳ (قد.) (افا.) \nگوش کننده» شنو نده. \n\nنیوشه: (قد. -6()66-)0-2 رنه (امسص.) \nگوش فرا داشتن به سخن دیگران از پس \nدیوار» از پس پرده و غیره؛ استراق سمع. \nترقب» ترصد» مراقبت. مثل سایر. (بهار در \nحاتوای ت ط و رس \nفرس\u200cاسدی) \n\nنیوشیدن: (قد. 165142'
--
'گران از پس \nدیوار» از پس پرده و غیره؛ استراق سمع. \nترقب» ترصد» مراقبت. مثل سایر. (بهار در \nحاتوای ت ط و رس \nفرس\u200cاسدی) \n\nنیوشیدن: (قد. 1651420-)1020-ک0ابزنج \n(مصم.) شنیدن» گوش کردن. \n\nنیوه: (قد. -6()65-)0۷۵ (.) ناله و افغان. \n\n\n«۴ \n\n\nفر هنک فارسی معین و \n\n\nو: 1 ,۲ (حر .) حرف سی\u200cام از الفبای فارسی و \nو ات اس ی \nبات مان آ'
--
##### گوشوار
'ر \nموسم سرما آب خورند. \nفل\u200cاحمدی: -۵۱-30120 (امر.) (لوطبان) \nدست به زور تمام بر عضو کسی زدن؛ \nسقلمه. \nقلاد: یی ای حلقه \nگوشواره و حلقةٌ بینی شتر پیچند \nقلاد ه؛ (م-)سهقاه: [ع. لاد زر آنجه به \nگردن آویزند» گردن\u200cبند» گلوبند؛ ج. قلائد \n( قلاید). سر تداول این کلمه را به فتح \nقاف و تشدید لا م گو یند. \n\n\nقلاسنگ.: 7۵۱2-18 [ - '
--
'د و با بوی مطبوع» ساقه\u200cاش \nاستوانه\u200cیی شکل و شاخه\u200cهایش متقابلند» \n۱23 33 \nپرگهاسبز ره و شفاف در سطح فوقنی و \nهمراه با دو گوشوارک است. کاسه و جام \nگل آن شامل ۵ تقسیم و پرچم\u200cهایش نیز به \nتعداد ۵ است. مبوه\u200cاش شفت و ابتدا سبز \nرنگ و پس از رسیدن قرمز می\u200cشود و \nمحتوی دو دانه است. هر دانه قهوه به اندازة \nیک نخود درشت و دارای ی'
--
'\nاندوخته\u200cهای گباهی یت این کٌیاه را به \nسب استفادة غذابی از ر شه\u200cاش در غالب \nنقاط جهان می\u200cکارند. برگ\u200cهایش متناوب و \nبدون گوشوارک و دارای بریدگی بسیار \nاست. گل آذینش چتر مرکب است و \nگل\u200cهایش کو چکث به رنگ سفید و میوه\u200cاش \nشامل دو فندقه و بیضوی است. ريشة گزر به \nعلت ما کول بودن مورد مصرف روزانه \nاست» حویج» کر کر اکتا \nکگکیا'
--
'ز آمیزش \nدیوارة تیان ح مین 333 سول \nغذایی در آن جمع می\u200cگردد. . بر گ\u200cهای گل \nرم کنتا ات بو دز شام هش بر ک :93 \nبرگک بنام گوشوارک موجود است. \nساقه\u200cهای گل آن پرخار است. اقسام مختلف \nو گونه\u200cهای مرغوب و پرپر گل سرخ را از \nبوند و پرورش نژادهای دو رکه بدست \nمی\u200cآورند؛ ورد. گل سرخ ژاپنی (زاپونی): \n(گیا) گونه\u200cای گل سرخ که هم گل '
--
'هی بدبوی که \nآن را کمای با کما نامند و در خراسان (در \nاطراف نیشابور و سبزوار) فراوان است و از \nآن نوعی آش تهیه کنند. گل گوشواره: گلی \nو سو پات وب یی \nآویزند. گل گوگرد: (گیا.) قطعات و \nتکه\u200cهای گوگرد خالص راگویند. گل گیتی: \n(گیا) گونه\u200cای از گل سرخ نیکث منظر که \nسوه مرغوب آن را سابقاً از بسصره \nاش | فد زان پرهای 1 را مدتی'
--
': به گوش \nهوش (قابوسنامه. نف. ۳۴). پشت گوش \nفراخ: کسی که سخن و پند دیگران نشنود؛ \nحرف نشنو. اهمال کار. حلفه\u200cبگوش: آنکه \nگوشواره به گوش ۳ \nفر مانبر دار . ( کذ.) برده؛ بنده. و در \nانستظار. دروازة گوش؛: سوراخ گوش. \nسنگینی گوش: عیبی در گوش بودن بطوری \nکه سخن را به دشواری شنود. گل و گوش: \nگردن و گوش و اطراف آنها. گوش به در"'
--
' را وادار \nان ای و نات موه ینبه از \nکوش بر دل (بیر ون آفزدن: آمادهة \nشنیدن سخنی گردیدن. حبقه در گوش \nکردن: آویختن حلقه (گوشواره) به گوش. \n(کد.) اطاعت و فرمانبرداری کردن. بندگی و \nبردگی کردن. در گوش آمدن: شنیده شدن. \nدر گوش (کسی) زدن: او را سیلی زدن. در \nگوش کردن: به گوش کردن؛ به گوش \n\n\nفر هنک فارسی معین \n\n\nگوش \nآویختن.'
--
' ببالة شراب که از \nصدف سازند؛ بیاله صدفین. \nگوش\u200cنواز: 2-7 |- کوش نوازنده| \n(ص\u200cفا.) آنچه گوش را نوازش دهد (صوت؛ \nنغمه). \nگوشوار: (قد. ۷3۲)265-.۲ |- کوشه\u200cواره) \n(امر.) زینتی ساخته از فلزات قیمتی و احجار \nکریمه یا از بلور که در گوش آویزند \n(مخضضا زنان اهاحلقه گوس کوشواود: \n\n\nزیوری که در گوش پرندگان کنند. ترکیب \nاسمی: گو ش'
--
' زنان اهاحلقه گوس کوشواود: \n\n\nزیوری که در گوش پرندگان کنند. ترکیب \nاسمی: گو شوار فلکك: (کد.) ماه نو. ت رکیبات \nفعلی: از گوشوار کسی چیزی آویختن: بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخ'
--
' گوشوار کسی چیزی آویختن: بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخانه\u200cای که در \nگوشه تالار واقع اش وتو کگ: \nگوشوا ره: (0-)۷2۲۸.: (شعر.) مطلعی که \nپس از مقطع آرند؛ مطلع دوم. . (اداء) دفت'
--
' بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخانه\u200cای که در \nگوشه تالار واقع اش وتو کگ: \nگوشوا ره: (0-)۷2۲۸.: (شعر.) مطلعی که \nپس از مقطع آرند؛ مطلع دوم. . (اداء) دفتر \nهط ری و که تا شین \nنو'
--
' بدخشان استخراج کنند. ( کن.) \nلب (معشوق). لعل پیکانی: (زم.) گونه\u200cای \nلعل که آن را به اندام پیکان تراشیده باشند و \nاز آن گوشواره سازند. لعل خوشاب: لعل \nآبدار. (کد.) لب معشوق. لعل درخشان: لعل \nدرخشنده و شفاف. (کد.) لب معشوق. لعل \nرگک\u200cدار: لعلی که در آن رکه باشد؛ لعل \nعس\u200cنا ک و داغدار. اتود \nرنگ انار دانه. لعل زر: (کذ.) ر'
--
' عور» بر هنه» \nلخت. \n\nلعات: اةّبوا [ع. ۰ (.) ج. لفت. علم لغات: \nلغت\u200cشناسی. - علم لقأت: لغت\u200cشناسان. \nلعار: ۱ (.) ( بناء) گوشوار دیوار (لغ.) \nلعاز؛ ۶ (ع. لغ] (.) (عم.) عس»؛ خرده \n(له.) (عم.) به کنایه از کسی بدگفتن. \n\n\nلغت\u200cشناس \nلعت؛ ۱0,۸۱ [ع.] (۰۱) لفظی که وضع شده \nبرای معنایی؛ کلمه؛ واژه. محموعه الفاظی \nکه قومی بدان تکل'
--
##### گوشو
'ر \nموسم سرما آب خورند. \nفل\u200cاحمدی: -۵۱-30120 (امر.) (لوطبان) \nدست به زور تمام بر عضو کسی زدن؛ \nسقلمه. \nقلاد: یی ای حلقه \nگوشواره و حلقةٌ بینی شتر پیچند \nقلاد ه؛ (م-)سهقاه: [ع. لاد زر آنجه به \nگردن آویزند» گردن\u200cبند» گلوبند؛ ج. قلائد \n( قلاید). سر تداول این کلمه را به فتح \nقاف و تشدید لا م گو یند. \n\n\nقلاسنگ.: 7۵۱2-18 [ - '
--
'د و با بوی مطبوع» ساقه\u200cاش \nاستوانه\u200cیی شکل و شاخه\u200cهایش متقابلند» \n۱23 33 \nپرگهاسبز ره و شفاف در سطح فوقنی و \nهمراه با دو گوشوارک است. کاسه و جام \nگل آن شامل ۵ تقسیم و پرچم\u200cهایش نیز به \nتعداد ۵ است. مبوه\u200cاش شفت و ابتدا سبز \nرنگ و پس از رسیدن قرمز می\u200cشود و \nمحتوی دو دانه است. هر دانه قهوه به اندازة \nیک نخود درشت و دارای ی'
--
'\nاندوخته\u200cهای گباهی یت این کٌیاه را به \nسب استفادة غذابی از ر شه\u200cاش در غالب \nنقاط جهان می\u200cکارند. برگ\u200cهایش متناوب و \nبدون گوشوارک و دارای بریدگی بسیار \nاست. گل آذینش چتر مرکب است و \nگل\u200cهایش کو چکث به رنگ سفید و میوه\u200cاش \nشامل دو فندقه و بیضوی است. ريشة گزر به \nعلت ما کول بودن مورد مصرف روزانه \nاست» حویج» کر کر اکتا \nکگکیا'
--
'ز آمیزش \nدیوارة تیان ح مین 333 سول \nغذایی در آن جمع می\u200cگردد. . بر گ\u200cهای گل \nرم کنتا ات بو دز شام هش بر ک :93 \nبرگک بنام گوشوارک موجود است. \nساقه\u200cهای گل آن پرخار است. اقسام مختلف \nو گونه\u200cهای مرغوب و پرپر گل سرخ را از \nبوند و پرورش نژادهای دو رکه بدست \nمی\u200cآورند؛ ورد. گل سرخ ژاپنی (زاپونی): \n(گیا) گونه\u200cای گل سرخ که هم گل '
--
'هی بدبوی که \nآن را کمای با کما نامند و در خراسان (در \nاطراف نیشابور و سبزوار) فراوان است و از \nآن نوعی آش تهیه کنند. گل گوشواره: گلی \nو سو پات وب یی \nآویزند. گل گوگرد: (گیا.) قطعات و \nتکه\u200cهای گوگرد خالص راگویند. گل گیتی: \n(گیا) گونه\u200cای از گل سرخ نیکث منظر که \nسوه مرغوب آن را سابقاً از بسصره \nاش | فد زان پرهای 1 را مدتی'
--
': به گوش \nهوش (قابوسنامه. نف. ۳۴). پشت گوش \nفراخ: کسی که سخن و پند دیگران نشنود؛ \nحرف نشنو. اهمال کار. حلفه\u200cبگوش: آنکه \nگوشواره به گوش ۳ \nفر مانبر دار . ( کذ.) برده؛ بنده. و در \nانستظار. دروازة گوش؛: سوراخ گوش. \nسنگینی گوش: عیبی در گوش بودن بطوری \nکه سخن را به دشواری شنود. گل و گوش: \nگردن و گوش و اطراف آنها. گوش به در"'
--
' را وادار \nان ای و نات موه ینبه از \nکوش بر دل (بیر ون آفزدن: آمادهة \nشنیدن سخنی گردیدن. حبقه در گوش \nکردن: آویختن حلقه (گوشواره) به گوش. \n(کد.) اطاعت و فرمانبرداری کردن. بندگی و \nبردگی کردن. در گوش آمدن: شنیده شدن. \nدر گوش (کسی) زدن: او را سیلی زدن. در \nگوش کردن: به گوش کردن؛ به گوش \n\n\nفر هنک فارسی معین \n\n\nگوش \nآویختن.'
--
' ببالة شراب که از \nصدف سازند؛ بیاله صدفین. \nگوش\u200cنواز: 2-7 |- کوش نوازنده| \n(ص\u200cفا.) آنچه گوش را نوازش دهد (صوت؛ \nنغمه). \nگوشوار: (قد. ۷3۲)265-.۲ |- کوشه\u200cواره) \n(امر.) زینتی ساخته از فلزات قیمتی و احجار \nکریمه یا از بلور که در گوش آویزند \n(مخضضا زنان اهاحلقه گوس کوشواود: \n\n\nزیوری که در گوش پرندگان کنند. ترکیب \nاسمی: گو ش'
--
' زنان اهاحلقه گوس کوشواود: \n\n\nزیوری که در گوش پرندگان کنند. ترکیب \nاسمی: گو شوار فلکك: (کد.) ماه نو. ت رکیبات \nفعلی: از گوشوار کسی چیزی آویختن: بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخ'
--
' گوشوار کسی چیزی آویختن: بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخانه\u200cای که در \nگوشه تالار واقع اش وتو کگ: \nگوشوا ره: (0-)۷2۲۸.: (شعر.) مطلعی که \nپس از مقطع آرند؛ مطلع دوم. . (اداء) دفت'
--
' بدو \nفرمان دون شا و شو ار سودن (ننده؛ \nپرستنده): حلقة غلامی به گوش و طوق \nبندگی بر گردن داشتن. گوشوار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخانه\u200cای که در \nگوشه تالار واقع اش وتو کگ: \nگوشوا ره: (0-)۷2۲۸.: (شعر.) مطلعی که \nپس از مقطع آرند؛ مطلع دوم. . (اداء) دفتر \nهط ری و که تا شین \nنو'
--
'وار بودن سخن: \nمانند گوشوار در گوش جای گرفتن سخن و \nگفتار. (نا.) اطاق یک بالاخانه\u200cای که در \nگوشه تالار واقع اش وتو کگ: \nگوشوا ره: (0-)۷2۲۸.: (شعر.) مطلعی که \nپس از مقطع آرند؛ مطلع دوم. . (اداء) دفتر \nهط ری و که تا شین \nنوسند. (حسا.) خلاصه حساب. (زم.) \nمروارید بزرگی که در صدف جز آن یکث \nباشد. پارچ؛ منقش و زردوزی که برای'
--
'.) خلاصه حساب. (زم.) \nمروارید بزرگی که در صدف جز آن یکث \nباشد. پارچ؛ منقش و زردوزی که برای \nزیست کنار عمامه قرار دهند. \nگوشوان: -: [- گسوش\u200cبان] (ص\u200cمر.) \nمحافظ؛ مراقب» راعی. \nگوشه: (0-)2154 (.) کنار» کناره» کران. از \n(ز) گوشه به گوشه: از کران تا کران؛ سراسر \nو ماه نو گوشه چگر :کار \nجگر. (کد.) فرزند. جگر گوشه. گوشة \nچشم:'
--
' بدخشان استخراج کنند. ( کن.) \nلب (معشوق). لعل پیکانی: (زم.) گونه\u200cای \nلعل که آن را به اندام پیکان تراشیده باشند و \nاز آن گوشواره سازند. لعل خوشاب: لعل \nآبدار. (کد.) لب معشوق. لعل درخشان: لعل \nدرخشنده و شفاف. (کد.) لب معشوق. لعل \nرگک\u200cدار: لعلی که در آن رکه باشد؛ لعل \nعس\u200cنا ک و داغدار. اتود \nرنگ انار دانه. لعل زر: (کذ.) ر'
--
' عور» بر هنه» \nلخت. \n\nلعات: اةّبوا [ع. ۰ (.) ج. لفت. علم لغات: \nلغت\u200cشناسی. - علم لقأت: لغت\u200cشناسان. \nلعار: ۱ (.) ( بناء) گوشوار دیوار (لغ.) \nلعاز؛ ۶ (ع. لغ] (.) (عم.) عس»؛ خرده \n(له.) (عم.) به کنایه از کسی بدگفتن. \n\n\nلغت\u200cشناس \nلعت؛ ۱0,۸۱ [ع.] (۰۱) لفظی که وضع شده \nبرای معنایی؛ کلمه؛ واژه. محموعه الفاظی \nکه قومی بدان تکل'
--
```


## [2026-09-07T20:24:24.371Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor f in ('data/verification/page-316.json',):\n    d=json.load(open(f))\n    e=d['entries'][0]\n    print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1500])\n    print('--- node sample')\n    print(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1)[:2500])\nEOF"
}
```


### [2026-09-07T20:24:25.705Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in n
--- node sample
{
 "id": 2,
 "lang": "Pahlavi",
 "words": "mâtar; matak; mâdiyânag, mâyag",
 "verdict": "confirmed",
 "derivation": "All three Pahlavi items are real and all go back to Av./OIr. mātar-. (a) mātar ‘mother’: MacKenzie has 'mād [AM < A ʾM-Y, v. mādar | M md] mother' and 'mādar [AMYtl; mtl | M mdr, N ~] mother' — the Aramaic heterogram ʾM(Y) masks an inherited word; mād is the nominative-derived short form, mādar the oblique stem mātar-, exactly as Nyberg describes ('māt [mʾT; ʾM] cas. obl. mātar [mʾtl; ʾMY-tl] mother … Common Ir.'). (b) mātak/mādag [NKB; mʾtkʹ] ‘female’ = *māta-ka-, a -ka- derivative of māt(ar) ‘mother’, borrowed into Armenian as matak ‘fēmella’ (Nyberg: 'from māt (q.v.)'). (c) the same -ka- formation in the abstract sense ‘the essential element of anything, its core, essence; materials’ gives Pahlavi mātak / (Manichaean) māyag [my g] with the intervocalic t > y development, whence NP māya; mātag-dān / mātīyān is Nyberg's 'that which contains the kernel, the core, or substance and essence of a thing' — Nourai's 'mādiyānag: essence'. Nourai's spelling matak (short a) for mātak is the book's usual loose transcription, not a different word.",
 "derivation_fa": "هر سه صورت پهلوی واقعی اند و همه به mātar- ایرانی باستان بازمی‌گردند: ۱) māt / mātar («مادر»؛ مکنزی ص ۵۶ و نیبرگ، با نوشتار هزوارش ʾM/ʾMY-tl)؛ ۲) mātak «ماده، موّنث» که پسوند -ak (ایرانی باستان -ka-) بر ستاک «مادر» افزوده شده و به ارمنی هم وام رفته است (matak)؛ ۳) همین mātak در معنای «جوهر، مادّهٔ اولی»، که با ابدال t میان‌واکه‌ای به y صورت māyag گرفته (در فارسی میانهٔ مانوی my g) و mātag-dān / mātīyān نیبرگ «آن که مغز و جوهر چیزی را دربر دارد» همان «mādiyānag» نورایی است. ادعای نورایی درست است؛ تنها «matak» را باید mātak (با الف کشیده) خواند.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D9%87",
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%DB%8C%D9%87",
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D8%B1"
 ],
 "ref_check": [
  {
   "ref": "BQT:1933",
   "status": "supports",
   "note": "Nourai's BQT pagination runs two pages behind the Ibn Sina scan on disk (his 1946/1964 = our 1948/1966), so BQT:1933 = the mādar page, our printed 1935 = BQT_v4 pdf page 16. Mo'in's footnote there: 'مادر – بفتح سوم = ماد = مار (ه.م.). پهلوی mātar, mād … حالت فاعلی از -mātar «بارتولمه ۱۱۶۷»، اوستا -mātar، ارمنی mayr، هندی باستان -mātar … افغانی mor، آسی mad…، بلوچی mās…' — i.e. Pahlavi mātar/mād from Avestan mātar-, precisely
```


## [2026-09-07T20:24:48.805Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor pat in (r'\\baus-\\b', r'\\bous-\\b', r'ous-\\s*To hear', r'To perceive'):\n    print('#####',pat)\n    for m in list(re.finditer(pat,t))[:4]:\n        print(t[max(0,m.start()-300):m.start()+700].replace('\\n',' '))\n        print('--')\nEOF"
}
```


### [2026-09-07T20:24:50.119Z] TOOL RESULT

```
##### \baus-\b
xed form *auk-sld- in Latin aulla, aula, olla, pot, jar: OLLA. [Pok. aug(h)- 88.] aulo-. Hole, cavity. 1. Metathetic form *alwo- in Latin bat- alvus, the belly, stomach: ALVEOLUuS. 2. Greek aulos, pipe, flute, hollow tube: CAROL, HYDRAULIC. [Pok. au- lo-s 88.] [aurum. Gold. Latin noun with preform *aus-o- probably from a root *aus-. Latin aurum (> French or), gold: AUREATE, AUREOLE, AURIC; AURIFEROUS, DORY?, EYRIR, OR’, ORE, ORIFLAMME, ORIOLE, ORMOLU, OROIDE, OR- PHREY, ORPIMENT.] aus-', To shine. 1. Germanic *aust- in: a. Old English éast, east (< “the direction of the sunrise”): EAST; b. Old High German 6stan, east: OSTMARK. 2. Germanic *aus- tra- in: a. Old English éasterne, eastern: EASTERN; b. Late Latin ostro-, eastern: OsTROGOTH. 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek
--
s whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek éds, dawn: EO-, Eos; EOSIN. [Pok. aues- 86.] aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, mate
--
kli-. 1. Germanic *hlid-, “that which bends over,” cover, in Old English Alid, cover: Lip. 2. Suffixed form *kli-n- in Germanic *hlinén, in Old English Alinian and hleonian, to lean: LEAN! 3. Suffixed form “*kli-ent- in Latin cliéns, dependent, follower: CLIENT. 4. Suffixed form *kli-to- in Latin *aus-klit-d- in auscultare, “to hold one’s ear inclined,” to listen to (see ous-). 5. Suffixed form *kli-n-yo- in Greek klinein, to lean: CLINAL, CLINE, -CLINIC, CLINO-; (ACLINIC LINE), CLINANDRIUM, ENCLIT- IC, (ISOCLINE), MATRICLINOUS, (MONOCLINIC), PAT- RICLINOUS, PERICLINE, PROCLITIC, SYNCLINAL. 6. Greek lengthened form *&ii- in: a. suffixed form *kli-n-d in Greek kliné, bed: CLINIC; DICLINOUS, MONOCLINOUS, TRICLINIUM; b. suffixed form *kii-m- in Greek klimax, ladder: CLIMAX; C. suffixed form *kli-mn in Greek klima, sloping surface of the earth: cLimaTE. III. Suffixed o-grade form *kloi-tr- in Germanic *hiaidr- in Old Eng- lish hléd(der, ladder: LADDER. [Pok. Rlei- 600.] kleng-. To bend, t
--
; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made fro
--
##### \bous-\b
uffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER;
--
-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic
--
##### ous-\s*To hear
##### To perceive
 in Russian ukazat’, to order: UKASE. 2. Sanskrit ava, off, down: AvaTAR. [Pok. 3. au- 72.] au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.] au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.] aug-'. To increase. Variant *(a)weg- (< *aweg-). 1. Ger- manic *aukan in: a. Old English éacan, écan, to increase: EKE!; b. Old English éaca, an addition: NICKNAME. 2. Variant extended forms *wogs-, *wegs- in Germanic *wahsan in Old English weaxan, to grow: WAX. 3. Form *aug-é- in: Latin augére, to increase: AUCTION, AUGEND, AUGMENT, AUTHOR, (AUTHORIZE), (
--
ed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow objec
--
ng mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive per
--
in Greek rhaptein, to sew (> rhaphé, suture): RAPHE, RAPHIDE; RHAPSODY, STAPHYLORRHAPHY, TENORRHAPHY. IX. Root *wrmi-, worm; rhyme word to k*rmi-. 1. Germanic *wurmiz in Old English wyrm, worm: worm. 2. Latin vermis, worm: VERMEIL, VERMI-, VERMICELLI, VERMICULAR, VERMIN. [Pok. 3. ver- 1152.] wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (pr
--
```


## [2026-09-07T20:25:02.178Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nprint(len(t))\n# look for page markers\nprint(re.findall(r'\\n\\s*\\d{3}\\s*\\n', t)[:20])\nfor w in ('anesthesia','anaesthesia'):\n    for m in list(re.finditer(w,t))[:2]:\n        print('#####',w); print(t[max(0,m.start()-400):m.start()+600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:25:03.607Z] TOOL RESULT

```
10393096
['\n100\n', '\n102\n', '\n103\n', '\n104\n', '\n105\n', '\n106\n', '\n108\n', '\n110\n', '\n112\n', '\n113\n', '\n114\n', '\n115\n', '\n116\n', '\n120\n', '\n122\n', '\n123\n', '\n124\n', '\n125\n', '\n126\n', '\n128\n']
##### anesthesia
work  . See  ergon. Derivative:  anerg-ic,  adj. aneroid,  adj.,  containing  no  liquid  (said  of  a  kind of  barometer);  n.,  an  aneroid  barometer.  F. anerotde,  lit.  ‘without  liquid’,  compounded  of priv.  pref.  a-  and  Gk.  vapos;,  VY]po<;,  ‘flowing, liquid’  (which  is  rel.  to  voter v,  ‘to  flow’),  and -oei8y)c,  ‘like’,  fr.  elSo;,  ‘form,  shape’.  See Nereid  and  -oid. anesthesia,  anaesthesia,  n.,  insensibility.  —  Gk. dvottcr&Yjma,  ‘lack  of  sensation’,  fr.  dcvaicffiYjxetv, ‘to  be  without  sense  of  something,  lack  sen¬ sation’,  fr.  dv-  (see  priv,  pref.  an-)  and  atofbrjTdq, ‘sensible,  perceptible’,  verbal  adj.  of  odo9dvecr- ‘to  perceive’.  See  esthete  and  cp.  esthesia. anesthetic,  anaesthetic,  adj.,  producing  insen- 74 75 sibility;  n.,  substance  producing  anesthesia.  — Formed  with  suff.  -ic  fr.  Gk.  avodatbjxo?,  ‘with¬ out  feeling’,  fr.  dv-  (see  priv.  pref.  an-)  and otlfT&YjToe,  ‘sensible,  perceptible’
##### anesthesia
sensibility.  —  Gk. dvottcr&Yjma,  ‘lack  of  sensation’,  fr.  dcvaicffiYjxetv, ‘to  be  without  sense  of  something,  lack  sen¬ sation’,  fr.  dv-  (see  priv,  pref.  an-)  and  atofbrjTdq, ‘sensible,  perceptible’,  verbal  adj.  of  odo9dvecr- ‘to  perceive’.  See  esthete  and  cp.  esthesia. anesthetic,  anaesthetic,  adj.,  producing  insen- 74 75 sibility;  n.,  substance  producing  anesthesia.  — Formed  with  suff.  -ic  fr.  Gk.  avodatbjxo?,  ‘with¬ out  feeling’,  fr.  dv-  (see  priv.  pref.  an-)  and otlfT&YjToe,  ‘sensible,  perceptible’.  See  prec. word. Derivatives:  anesthet-ist,  n.,  anesthet-ize,  tr.  v. anet,  n„  dill.  —  F.  anet,  aneth,  fr.  L.  anethum, fr.  Gk.  avYj&ov,  ‘dill,  anise’.  Cp.  Gk.  dvtoov, L.  anisum,  and  see  anise, aneurysm,  n.,  a  morbid  dilatation  of  the  coat  of an  artery  (med.)  —  Gk.  dv£upuap.04,  dilatation  , fr.  dveupuvsLv,  ‘to  dilate’,  fr.  ocvoc  (see  ana-),  and eupuvetv,  ‘to  widen’,  fr.  eup%,  ‘
##### anaesthesia
ergon. Derivative:  anerg-ic,  adj. aneroid,  adj.,  containing  no  liquid  (said  of  a  kind of  barometer);  n.,  an  aneroid  barometer.  F. anerotde,  lit.  ‘without  liquid’,  compounded  of priv.  pref.  a-  and  Gk.  vapos;,  VY]po<;,  ‘flowing, liquid’  (which  is  rel.  to  voter v,  ‘to  flow’),  and -oei8y)c,  ‘like’,  fr.  elSo;,  ‘form,  shape’.  See Nereid  and  -oid. anesthesia,  anaesthesia,  n.,  insensibility.  —  Gk. dvottcr&Yjma,  ‘lack  of  sensation’,  fr.  dcvaicffiYjxetv, ‘to  be  without  sense  of  something,  lack  sen¬ sation’,  fr.  dv-  (see  priv,  pref.  an-)  and  atofbrjTdq, ‘sensible,  perceptible’,  verbal  adj.  of  odo9dvecr- ‘to  perceive’.  See  esthete  and  cp.  esthesia. anesthetic,  anaesthetic,  adj.,  producing  insen- 74 75 sibility;  n.,  substance  producing  anesthesia.  — Formed  with  suff.  -ic  fr.  Gk.  avodatbjxo?,  ‘with¬ out  feeling’,  fr.  dv-  (see  priv.  pref.  an-)  and otlfT&YjToe,  ‘sensible,  perceptible’.  See  prec.
```


## [2026-09-07T20:25:11.842Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pg in (126,494):\n    for m in re.finditer(r'\\n\\s*%d\\s*\\n'%pg, t):\n        seg=t[m.end():m.end()+1800].replace('\\n',' ')\n        print('##### after marker',pg)\n        print(seg[:1800])\n        print()\nEOF"
}
```


### [2026-09-07T20:25:13.189Z] TOOL RESULT

```
##### after marker 126
127 family  (hot.)  —  ModL.,  named  after  Claude Aubriet,  painter  of  flowers  and  animals  (1668- 1743).  For  the  ending  see  suff.  -ia. auburn,  adj.,  reddish-brown.  —  ME.  auburne , ‘whitish’,  fr.  OF.  alborne,  auborne,  fr.  VL.  al- burnus,  ‘whitish’,  fr.  L.  albus,  ‘white’.  The  sense development  of  the  word  was  influenced  by  a confusion  with  brown.  See  alb  and  cp.  alburnum. Derivative:  auburn,  n. auchenium,  n.,  part  of  a  bird’s  neck  ( ornithol .) —  ModL.,  formed  with  suff.  -ium  fr.  Gk.  crir/ry, ‘neck,  throat’,  which  is  rel.  to  Aeol.  dcptep-rjv,  of s.m.,  and  cogn.  with  Arm.  auji-k',  ’necklace’, auction,  n.  —  L.  auctid,  gen.  -dnis,  ‘an  increase; a  public  sale,  auction’,  fr.  auctus ,  pp.  of  augere, ‘to  increase’,  fr.  I.-E.  base  *aweg-,  *aug-,  ‘to grow,  increase’,  whence  also  Lith.  augu,  augti, Lett,  augu,  augt,  ‘to  grow’,  Lith.  aukstas,  Lett. augsts,  ‘high,  of  superior  rank’,  OPruss.  auck- timmien,  ‘chief’,  aucktai-rikyskan,  ‘authority’, Lett,  audzet,  ‘to  bring  up’,  Goth,  aukan,  ‘to grow,  increase’,  OE.  eacian,  ‘to  increase’ ;  see eke  and  cp.  augment,  augur,  august,  author.  Cp. the  related  base  *aw(e)ks-,  *auks-,  *weks-, *uks-,  ‘to  grow,  increase’,  whence  OL  vaksdyati, ‘causes  to  grow’,  uksati,  ‘grows  strong’,  Gk. dr rEc'.v.  a.i'ieiv,  au^dvetv,  ‘to  increase’, L.  auxilium,  ‘help,  aid’,  Goth,  wahsjan,  OE. weaxan,  ‘to  grow’.  See  wax,  v.,  and  cp.  auxiliary, auxano-,  auxesis,  auxetic,  auxo-. Derivatives:  auction,  tr.  v.,  auction-eer,  n.,  auc- tion-eer-ing ,  n. aucupate,  intr.  and  tr.  v.,  to  go  fowling.  —  L. aucupdtus,  pp.  of  aucupdre,  later  aucupari,  ‘to go  fowling’,  fr.  auceps,
```


## [2026-09-07T20:25:26.528Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'\\n\\s*126\\s*\\n', t)\nseg=t[m.end():m.end()+9000].replace('\\n',' ')\ni=seg.find('audible')\nprint(seg[i-200:i+2600] if i>0 else seg[1800:5000])\nEOF"
}
```


### [2026-09-07T20:25:27.849Z] TOOL RESULT

```
cious-ly,  adv.,  audacious¬ ness,  n. audacity,  n.,  daring,  boldness.  —  Formed  with suff.  -ity  fr.  L.  audax,  gen.  -dm,  ’bold’,  fr.  au¬ dere,  ‘to  dare’.  See  prec.  word  and  -ity. audible,  adj.  —  ML.  audibilis,  fr.  L,  audio,  audire, ‘to  hear’,  which  prob.  stands  for  * awis-d-id ,  fr. I.-E.  base  *awei-,  *au-,  ‘to  perceive’,  whence  also OL  avifi,  Avestic  avish,  ‘openly,  evidently’,  Gk. alaffdvopai  (for  *4Fia-ff-<xvo[iai),  ‘I  perceive’, afo)  (for  ‘aft. to),  ‘I  hear’  (lit.  ‘I  perceive  by  the ear’),  OSlav.  ave,  jave,  ‘open,  public’,  aviti, javiti,  ‘to  reveal’.  Cp.  obedient,  obeisance,  obey, oyer,  oyez. Derivatives:  audibii-ity ,  n.,  audible-ness,  n., audibl-y,  adv. audience,  n.  —  F.,  fr.  L.  audientia,  ‘a  hearing, audience’,  fr.  audiens,  gen.  -entis,  pres.  part,  o audire.  See  audible  and  -ence. audient,  n.,  a  hearer,  listener.  —  L.  audiens,  gen. -entis.  See  prec.  word  and  -ent. audile,  adj.,  auditory.  —  Formed  with  suff.  -ile fr.  L.  audire,  ‘to  hear’.  See  audible. Derivative:  audile,  n.,  a  person  whose  imagery is  chiefly  auditory  ( psychol .) audiology,  n.,  the  science  of  curing  defective  hear¬ ing.  —  A  hybrid  coined  fr.  L.  audire,  ‘to  hear’, and  Gk.  -Xoyia,  fr.  -Xoyoi;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  audible  and  -logy. Derivative :  audiolog-ist,  n. audiometer,  n.,  an  instrument  for  measuring  the intensity  of  sounds.  —  A  hybrid  coined  fr.  L. audire,  ‘to  hear’,  and  Gk.  ptixpov,  ‘measure’.  See audible  and  meter,  ‘poetical  rhythm’. Derivatives:  audiometr-y,  n.,  audiometr-ist,  n. audiphone,  n.,  an  instrument  for  helping  the  deaf to  hear.  —  A  hybrid  coined  fr.  L.  audire,  ‘to  hear’ , and  Gk.  <pcavr),  ‘sound’.  See  audible  and  phone, audit,  tr.  v.  and  n.  —  Back  formation  fr.  auditor (Qv) audition,  n.  —  L.  auditio,  gen.  -dnis,  ‘a  hearing’, fr.  auditus,  pp.  of  audire.  See  audible  and  -ion and  cp.  auditor. auditive,  adj.  —  F.  auditif  (fern,  auditive ),  fr.  L. auditus,  pp.  of  audire,  ‘to  hear’.  See  audible, auditor,  n.,  a  hearer.  —  AF.  auditour,  corre¬ sponding  to  F.  auditeur,  fr.  L.  auditorem,  acc.  of auditor,  ‘a  hearer’,  fr.  auditus,  pp.  of  audire.  See audible  and  agential  suff.  -or. auditorium,  n.,  a  building  or  part  of  a  building assigned  to  the  audience.  —  L.  auditorium, ‘lecture  room,  hall  of  justice’,  prop.  neut.  of  the adjective  auditdrius,  ‘relating  to  hearing’,  used as  a  noun,  and  lit.  meaning  ‘the  place  where something  is  heard’,  fr.  auditus,  pp.  of  audire. See  next  word  and
```


## [2026-09-07T20:25:37.614Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'\\n\\s*494\\s*\\n', t):\n    seg=t[m.end():m.end()+6000].replace('\\n',' ')\n    i=seg.find(\"ear,\")\n    print(seg[:300]); print('...')\n    print(seg[i-300:i+2000] if i>0 else seg[300:3000])\nEOF"
}
```


### [2026-09-07T20:25:39.113Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:25:43.365Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nprint([m.group(0).strip() for m in re.finditer(r'\\n\\s*49[0-9]\\s*\\n', t)])\ni=t.find(\"ear,  n.,  the  organ\")\nif i<0:\n    for m in list(re.finditer(r'\\bear\\b,\\s+n\\.', t))[:5]:\n        print(t[m.start()-200:m.start()+900].replace('\\n',' '));print('==')\nelse:\n    print(t[i-600:i+1500].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:25:44.710Z] TOOL RESULT

```
['490', '497']
‘eagle’.  See  prec.  word  and  -et,  -ette. eaglewood,  n.,  agalloch.  —  Loan  translation  of F.  bois  d'aigle,  fr.  Port,  aguila,  ‘aloewood’,  fr. Gk.  ava>.).o-/_ov,  ‘aloe,  aloewood’ ;  see  agalloch. French  bois  d'aigle  arose  from  a  confusion  of Port,  aguila ,  ‘aloewood’,  with  Port,  aguia,  Sp. aguila,  'eagle'  (see  eagle). eagre,  n.,  a  tidal  wave;  a  bore.  —  Lit.  ‘water borer’,  fr.  OE.  ea,  ‘water’,  and  gar,  ‘spear’.  See aquatic  and  gore,  ‘to  pierce’, ean,  tr.  and  intr.  v.  —  A  var.  of  yean  (q.v.) Derivative:  ean-ling  (cp.  yeanling). ear,  n.,  the  organ  of  hearing.  ME.  ere,  fr.  OE. eare,  rel.  to  ON.  eyra,  Swed.  bra,  Dan.  ore, OS.,  ODu.,  OHG.  bra,  OFris.  are,  Du.  oor, MHG.  ore,  G.  Ohr,  Goth,  auso,  and  cogn.  with Gk.  o\>q,  gen.  <o to?  (for  *ouao<;,  resp.  *ouoaTo?), L.  auris  (for  *ausis),  Avestic  ushi,  ‘both  ears', OSlav.  ucho  (gen.  uSese,  dual  uii),  Lith.  ausis, Lett,  auss,  OPruss.  ausins  (acc.  pi.),  OIr.  au,  6, ‘ear’,  Arm.  unkn  (for  *uson-qo-m),  Alb.  ref, ‘ear’.  All  these  words  derive  fr.  I.-E.  base  *au-, ‘ear’.  Cp.  aural,  ‘pertaining  to  the  ear’,  auricle, auscultation,  orillion,  ormer,  oto-,  oyer,  oyez. Cp.  also  acroama. Derivatives:  ear-ed,  adj.,  earing  (q.v.) ear  of  corn,  n.  —  ME.  ere,  ear,  fr.  OE.  eare,  rel. to  Du.  aar,  OHG.  ehir,  ahir,  MHG,  eher,  G. Ahre,  ON.  ax,  Goth,  ahs,  ‘ear  of  corn’,  fr.  Teut. *ahiz,  corresponding  to  I.-E.  *akos-,  whence  L. acus,  ‘chaff,  husk’,  Gk.  a x.otrrr„  ‘barley’,  lit.  ‘the awny  one’,  fr.  I.-E.  base  *ak-,  ‘to  be  sharp  or pointed’,  whence  also  L.  acer ,  ‘sharp,  pointed’. See  acrid  and  cp.  words  there  referred  to. Derivative:  ear-ed,  adj. ear,  tr.  v.,  to  plow  ( archaic  or  obsoi.)  —  ME. erien,  fr.  OE.  erian,  rel.  to  OS.  erian,  ON.  erja, OFris.  era,  OHG.  erien,  Goth,  arjan,  fr.  I.-E. base  *ara-,  ‘to  plow’,  whence  also  L.  arare,  ‘to plow’.  See  arable. earing,  n.,  rope  by  which  the  uppe
```


## [2026-09-07T20:26:02.540Z] TOOL CALL #52: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-07T20:26:02.589Z] TOOL RESULT

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


## [2026-09-07T20:26:07.176Z] TOOL CALL #53: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ows-\" \\\n \"https://en.wiktionary.org/wiki/گوش\" \\\n \"https://en.wiktionary.org/wiki/گوشواره\" \\\n \"https://en.wiktionary.org/wiki/نیوشیدن\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gauša\" \\\n ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 377, root Ous/Au/Aus 'ear', Ghosh branch\" ; done"
}
```


### [2026-09-07T20:26:13.252Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/47ca3de50151d4b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e6d310a6666408c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84a0c96bf71008c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7796818c059ae11f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30f08a50f8776419.txt
```


## [2026-09-07T20:26:16.272Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 47ca3de50151d4b6 e6d310a6666408c1 84a0c96bf71008c8 7796818c059ae11f 30f08a50f8776419; do echo \"########## $f\"; head -c 250 $f.txt; echo; grep -n -i \"etymology\" -A6 $f.txt | head -40; done 2>&1 | head -140"
}
```


### [2026-09-07T20:26:17.630Z] TOOL RESULT

```
########## 47ca3de50151d4b6
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ows-
FETCHED: 2026-09-07T20:26:08Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂ṓws - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₂�
62: Etymology 
63-
64- 1.2 
65- Reconstruction 
66-
67- 1.3 
68- Noun 
--
147: Etymology
148- [ edit ] 
149-
150- From *h₂ew- ( “ to see ” ) +‎ *-s ( root nominal suffix ) , with a semantic shift to "to hear" after the split of the Anatolian branch.
151-
152- Reconstruction
153- [ edit ] 
########## e6d310a6666408c1
URL: https://en.wiktionary.org/wiki/گوش
FETCHED: 2026-09-07T20:26:11Z
STATUS: 200
TITLE: گوش - Wiktionary, the free dictionary

گوش - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Na
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 2 
68- Persian 
--
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Noun 
--
180: Etymology
181- [ edit ] 
182-
183- From Proto-Iranian *gáwšah , from Proto-Indo-Iranian *gʰáwšas . Cognate with Persian گوش ( gôš ) .
184-
185- Noun
186- [ edit ] 
--
228: Etymology
229- [ edit ] 
230-
231: Etymology tree
232-
233- Proto-Indo-Iranian *gʰáwšas 
234- Proto-Iranian *gáwšah 
235- Old Persian 𐎥𐎢𐏁 ( g-u-š ) 
236- Middle Persian 𐭢𐭥𐭱 ( gʿš ) 
237- Persian گوش 
--
347: Pages with etymology trees 
348: Persian entries with etymology trees 
349- Pages with inline etymon for redlinks 
350- Pages using etymon with no ID 
351-
########## 84a0c96bf71008c8
URL: https://en.wiktionary.org/wiki/گوشواره
FETCHED: 2026-09-07T20:26:11Z
STATUS: 200
TITLE: گوشواره - Wiktionary, the free dictionary

گوشواره - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
149: Etymology
150- [ edit ] 
151-
152: Etymology tree
153-
154- Proto-Indo-Iranian *gʰáwšas 
155- Proto-Iranian *gáwšah 
156- Old Persian 𐎥𐎢𐏁 ( g-u-š ) 
157- Middle Persian 𐭢𐭥𐭱 ( gʿš ) 
158- Persian گوش ( guš ) 
--
233: Pages with etymology trees 
234: Persian entries with etymology trees 
235: Persian entries with etymology texts 
236- Pages using etymon with no ID 
237- Pages with entries 
238- Pages with 1 entry 
239-
240- This page was last edited on 15 August 2026, at 21:24.
241-
########## 7796818c059ae11f
URL: https://en.wiktionary.org/wiki/نیوشیدن
FETCHED: 2026-09-06T20:59:23Z
STATUS: 200
TITLE: نیوشیدن - Wiktionary, the free dictionary

نیوشیدن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move
62: Etymology 
63-
```


## [2026-09-07T20:26:24.634Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### گوش\"; sed -n '170,260p' e6d310a6666408c1.txt; echo \"###### گوشواره\"; sed -n '140,200p' 84a0c96bf71008c8.txt"
}
```


### [2026-09-07T20:26:24.696Z] TOOL RESULT

```
###### گوش
 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: کوس and كوش 

 Baluchi
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Iranian *gáwšah , from Proto-Indo-Iranian *gʰáwšas . Cognate with Persian گوش ( gôš ) .

 Noun
 [ edit ] 

 گوش • ( goš ) 

 ear 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: گوش 

 Wikipedia fa 

 Picture dictionary 

 گوش 
 جمجمه 

 مغز 

 چشم 

 لب 

 بینی 

 دهان 

 چانه 

 فک 

 گوش 

 گیجگاه 

 گردن 

 Click on labels in the image

 body 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-Iranian *gʰáwšas 
 Proto-Iranian *gáwšah 
 Old Persian 𐎥𐎢𐏁 ( g-u-š ) 
 Middle Persian 𐭢𐭥𐭱 ( gʿš ) 
 Persian گوش 

 Inherited from Middle Persian 𐭢𐭥𐭱 ( gʿš /⁠gōš⁠/ ) , from Old Persian 𐎥𐎢𐏁 ( g-u-š /⁠gauša⁠/ , “ ear ” ) , from Proto-Iranian *gáwšah , from Proto-Indo-Iranian *gʰáwšas , from Proto-Indo-European *gʰows- ( “ hear ” ) .

 Indo-Iranian cognates include: Avestan 𐬔𐬀𐬊𐬱𐬀 ( gaoša ) , Baluchi گوش ( goš ) , Northern Kurdish guh , Ossetian хъус ( qus ) / гъос ( ǧos ) , Sanskrit घोष ( ghoṣa ) . Also compare Old Armenian գոյշ ( goyš ) , an Iranian borrowing.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈɡoːʃ/ 

 ( Dari, formal ) IPA ( key ) : [ɡoːʃ] 

 ( Dari, formal ) IPA ( key ) : [ɡoːʃ] 
 ( Kabuli ) IPA ( key ) : [ɡoːʃ] 

 ( Hazaragi ) IPA ( key ) : [ɡʊːʃ] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥uːʃ] 

 ( Tajik, formal ) IPA ( key ) : [ɡɵʃ] 

 Rhymes: -oːʃ 

###### گوشواره

 گوشواره 

 Iranian Persian

 Tajik

 гӯшвора 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-Iranian *gʰáwšas 
 Proto-Iranian *gáwšah 
 Old Persian 𐎥𐎢𐏁 ( g-u-š ) 
 Middle Persian 𐭢𐭥𐭱 ( gʿš ) 
 Persian گوش ( guš ) 

 Persian ـوار ( -wār  / -vâr ) 

 Proto-Iranian *-a- 

 Proto-Iranian *-kah 

 Proto-Iranian *-akah 
 Persian ـه ( -a  / -e ) 

 Persian ـواره ( -vâre ) 

 Persian گوشواره 

 From گوش ( guš , “ ear ” ) + ـواره ( -vâre ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡoːʃ.waː.ˈra/ 

 ( Dari, formal ) IPA ( key ) : [ɡoːʃ.wɑː.ɾá] 

 ( Dari, formal ) IPA ( key ) : [ɡoːʃ.wɑː.ɾá] 
 ( Kabuli ) IPA ( key ) : [ɡoːʃ.wɑː.ɾá] 

 ( Hazaragi ) IPA ( key ) : [ɡʊːʃ.wɔː.ɾá] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥uːʃ.vɒː.ɹé] 

 ( Tajik, formal ) IPA ( key ) : [ɡɵʃ.vɔ.ɾá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 gōšwāra

 Dari reading ?
```


## [2026-09-07T20:26:39.103Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '60,200p' 7796818c059ae11f.txt | grep -v \"^ *$\" | head -60; echo \"###### PI gauša\"; sed -n '60,200p' 30f08a50f8776419.txt | grep -v \"^ *$\" | head -50"
}
```


### [2026-09-07T20:26:40.434Z] TOOL RESULT

```
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Verb 
 1.3.1 
 Conjugation 
 1.3.2 
 Derived terms 
 Toggle the table of contents 
 نیوشیدن 
 4 languages 
 فارسی 
 Magyar 
 Kurdî 
 Malagasy 
 Entry 
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
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian ndwhšytn' ( niyō(x)šidan ) , from Proto-Iranian *ni- + *gáwšati , from Proto-Indo-Iranian *gʰáwšati . Compare Baluchi نگوشگ ( negóšag ) , Sanskrit घोषति ( ghoṣati ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ni.joː.ʃiː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Dari, formal ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Kabuli ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Hazaragi ) IPA ( key ) : [ni.ju.ʃi.d̪án] 
###### PI gauša
```


## [2026-09-07T20:26:47.509Z] TOOL CALL #57: Bash

```json
{
 "command": "head -4 data/verification/sources/web/30f08a50f8776419.txt; for u in \\\n \"https://www.etymonline.com/word/ear\" \\\n \"https://www.etymonline.com/word/anesthesia\" \\\n \"https://www.etymonline.com/word/audio-\" \\\n \"https://www.etymonline.com/word/obey\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ew-\" \\\n ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 377: Germanic ear / Greek anesthesia / Latin audire branches of Ous-Au root\" ; done"
}
```


### [2026-09-07T20:26:51.018Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gauša
FETCHED: 2026-09-07T20:26:13Z
STATUS: -1
TITLE: 
/home/sfmqrb/git/rishe/data/verification/sources/web/647f21c1b90222b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e98ed66b24cbb246.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0681cd70c0f5d1c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7e69070ed4d3060b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30b0f38b8c25a54e.txt
```


## [2026-09-07T20:26:56.048Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 647f21c1b90222b9 e98ed66b24cbb246 0681cd70c0f5d1c4 7e69070ed4d3060b 30b0f38b8c25a54e; do echo \"##### $f\"; head -4 $f.txt; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt',encoding='utf-8').read()\nt=re.sub(r'\\n+','\\n',t)\nprint(t[300:2200])\nEOF\ndone 2>&1 | head -160"
}
```


### [2026-09-07T20:26:57.557Z] TOOL RESULT

```
##### 647f21c1b90222b9
URL: https://www.etymonline.com/word/ear
FETCHED: 2026-09-07T20:26:49Z
STATUS: 200
TITLE: Ear - Etymology, Origin & Meaning
come a Premium Member to remove all ads.
 Origin and history of ear 
 ear (n.1) 
 "organ of hearing," Old English eare "ear," from Proto-Germanic *auzon , from PIE *ous- "ear."
 þe harde harte of man, þat lat in godis word atte ton ere & vt atte toþir. [sermon, c. 1250]
 In music, "capability to learn and reproduce by hearing," 1520s, hence play by ear (1670s).
 The belief that itching or burning ears means someone is talking about you is mentioned in Pliny's "Natural History" (77 C.E.). Until at least the 1880s, even some medical men still believed piercing the ear lobes improved one's eyesight.
 The meaning "handle of a pitcher" is mid-15c. (but compare Old English earde "having a handle," and the image also was in ancient Greek).
 To be wet behind the ears "naive" is from 1902, American English. The warning phrase walls have ears is attested from 1610s.
 IE cognates include Greek ous , Latin auris , Lithuanian ausis , Old Church Slavonic ucho , Old Irish au "ear," Avestan usi "the two ears." The Germanic cognates include Old Norse eyra , Danish øre , Old Frisian are , Old Saxon ore , Middle Dutch ore , Dutch oor , Old High German ora , German Ohr , Gothic auso . French orielle , Spanish oreja are from Latin auricula (Medieval Latin oricula ), diminutive of auris .
 ear (n.2) 
 "grain part of corn," from Old English ear (West Saxon), æher (Northumbrian) "spike, ear of grain," from Proto-Germanic *akhuz (source also of Dutch aar , Old High German ehir , German Ähre , Old Norse ax , Gothic ahs "ear of corn"), from PIE root *ak- "be sharp, rise (out) to a point, pierce" (source of Latin acus "chaff, husk of corn," Greek akoste "barley").
 Entries linking to ear 
 aural (adj.) 
 1844, "pertaining to the ear," from Latin auris "the ear as the organ of hearing" (see ear (n.1)) + -al (1). The meaning "received or perceived by ear" is attested by 1860. Related: Aurally .
 a
##### e98ed66b24cbb246
URL: https://www.etymonline.com/word/anesthesia
FETCHED: 2026-09-07T20:26:49Z
STATUS: 200
TITLE: Anesthesia - Etymology, Origin & Meaning
see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of anesthesia 
 anesthesia (n.) 
 1721, "loss of feeling," medical Latin, from Greek anaisthēsia "want of feeling or perception, lack of sensation (to pleasure or pain)," abstract noun from an- "without" (see an- (1)) + aisthēsis "feeling" (from PIE root *au- "to perceive"). For the abstract noun ending, see -ia .
 As "a procedure for the prevention of pain in surgical operations," attested from 1846. Aesthesia "capacity for feeling" is attested in English from 1853, perhaps a back-formation.
 also from 1721 
 Entries linking to anesthesia 
 anaesthesia (n.) 
 alternative spelling of anesthesia (q.v.). See æ (1).
 anesthesiology (n.) 
 1908, from anesthesia + -ology .
 Anesthesiology. This is the new term adopted by the University of Illinois defining "the science that treats of the means and methods of producing in man or animal various degrees of insensibility with or without hypnosis." [Medical Herald, January, 1912]
 anesthetic 
 anesthetist 
 anesthetize 
 kinesthesia 
 an- 
 *au- 
 -ia 
 See All Related Words (9) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 anesthetic 
 1846, "insensible;" 1847, "producing temporary loss of sensation," with -ic + Latinized form of Greek anaisthētos "insensate, without feeling; senseless, tactless, stupid" (see anesthesia). The noun meaning "agent that produces anesthesia" was first used in the modern sense 1848 
 pivot 
 "pin on which a wheel or other object turns," 1610s, from French pivot, from Old French pivot "hinge pin, pivot" (12c.), also "penis," a word of uncertain origin. Pevetsheres, evidently some kind of shears, is mentioned in a will registered in York in 1398. Figurative sense of "t
 primitive 
 late 14c., primitif, "of an original cause; of a thing from 
##### 0681cd70c0f5d1c4
URL: https://www.etymonline.com/word/audio-
FETCHED: 2026-09-07T20:26:50Z
STATUS: 200
TITLE: Audio- - Etymology & Meaning of the Prefix
see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of audio- 
 audio- 
 word-forming element meaning "sound, hearing," from combining form of Latin audire "to hear" (from PIE root *au- "to perceive"); used in English word formation by 1890s.
 also from 1890s 
 Entries linking to audio- 
 audio (n.) 
 "sound," especially recorded or transmitted sound signals, 1934, abstracted from word-forming element audio- (q.v.), which is from Latin audire "to hear" (from PIE root *au- "to perceive").
 audiology (n.) 
 "science of hearing and treatment of deafness," 1946, from audio- + -ology . Related: Audiologist .
 audiophile 
 audiotape 
 audiovisual 
 *au- 
 See All Related Words (6) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 fast 
 Fast-forward is by 1948, originally of audio tape....
 record 
 Record-player is attested from 1919; record-album " audio recordings issued as a collection" is by 1936....
 epithet 
 "descriptive name for a person or thing," 1570s, from French épithète or directly from Latin epitheton (source also of Spanish epíteto, Portuguese epitheto, Italian epiteto), from Greek epitheton "an epithet; something added," noun use of adjective (neuter of epithetos) "attribut
 reefer 
 "marijuana cigarette," 1920s, perhaps an alteration of Mexican Spanish grifo "marijuana, drug addict" [OED]; or perhaps from reef (v.), on resemblance to a rolled sail. It also meant "pickpocket" in criminal slang (by 1935), and Century Dictionary also has it as "oyster that grow
 goosebumps 
 also goose-bumps, "peculiar tingling of the skin produced by cold, fear, etc.; the sensation described as 'cold water down the back'" [Farmer], 1859, from goose (n.) + bump (n.). So called because the rough condition of the skin during the sensation resembles the skin of a plucke
 pl
##### 7e69070ed4d3060b
URL: https://www.etymonline.com/word/obey
FETCHED: 2026-09-07T20:26:50Z
STATUS: 200
TITLE: Obey - Etymology, Origin & Meaning
 become a Premium Member to remove all ads.
 Origin and history of obey 
 obey (v.) 
 c. 1300, obeien , "carry out the commands of (someone); submit to (a command, rule, etc.); be ruled by," from Old French obeir "obey, be obedient, do one's duty" (12c.), from Latin obedire , oboedire "obey, be subject, serve; pay attention to, give ear," literally "listen to," from ob "to" (see ob- ) + audire "listen, hear" (from PIE root *au- "to perceive"). Same sense development is in  hiersumnian , the Old English word for the same thing. Related: Obeyed ; obeying .
 also from c. 1300 
 Entries linking to obey 
 disobedience (n.) 
 "neglect or refusal to obey," c. 1400, from Old French desobedience , from Vulgar Latin *disobedientia (replacing Latin inobedientia ) from Latin dis- (see dis- ) + oboedientia "obedience," abstract noun from oboedientem (nominative oboediens ), present participle of oboedire "to obey" (see obey ). The English word replaced earlier desobeissance in this sense, and inobedience (c. 1200).
 disobedient (adj.) 
 "neglecting or refusing to obey, refractory, not submitting to the rules or regulations prescribed by authority," early 15c., dysobedyent , from Old French desobedient , from Vulgar Latin *disobedientem (replacing Latin inobedientem ) from Latin dis- (see dis- ) + oboedientem (nominative oboediens ), present participle of oboedire "to obey" (see obey ). Related: Disobediently . Earlier in the same sense was disobeissant (late 14c.), from Old French desobeissant , and inobedient (early 14c.).
 disobey 
 obedience 
 obedient 
 obeisance 
 *au- 
 ob- 
 See All Related Words (8) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 disobey 
 late 14c., disobeien, "neglect or refuse to obey," from Old French desobeir (13c.) "disobey; refuse service or homage," from Vulgar Latin *dis
##### 30b0f38b8c25a54e
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ew-
FETCHED: 2026-09-07T20:26:50Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂ew- - Wiktionary, the free dictionary
t 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Root 
 1.1.1 
 Derived terms 
 1.1.2 
 References 
 1.2 
 Root 
 1.2.1 
 Alternative reconstructions
```


## [2026-09-07T20:27:06.185Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/web/30b0f38b8c25a54e.txt',encoding='utf-8').read()\nt=re.sub(r'\\n+','\\n',t)\ni=t.find('Proto-Indo-European')\nj=t.find('Root')\nprint(t[t.find('From Wiktionary'):t.find('From Wiktionary')+2500])\nEOF"
}
```


### [2026-09-07T20:27:07.400Z] TOOL RESULT

```
From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *h₂ew- 
 to enjoy 
 to consume 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₂ew- (enjoy) (13 c, 0 e) 
 *h₂ew-eh₁-(ye)- 
 Proto-Italic: *awēō 
 Latin: aveō 
 *h₂éwH-e- [ 1 ] 
 > ? Proto-Indo-Iranian: *Háwati ( possibly from *h₁ewH- ) 
 Proto-Indo-Aryan: *Háwati 
 Sanskrit: अवति ( avati , “ to help, protect ” ) 
 Proto-Celtic: 
 Old Irish: con·ói ( “ to protect ” ) [ 1 ] 
 *h₂ēwH-os-s   n 
 > ? Proto-Hellenic: *āwos or *ēwos ( alternatively from *h₁ewH- ) [ 2 ] [ 1 ] 
 > ? Ancient Greek: *ἦος ( *êos ) 
 Ancient Greek: ἐν-ηής ( en-ēḗs , “ mild, soft, benevolent ” ) 
 *h₂ew-tu- [ 1 ] 
 Proto-Germanic: *auþuz ( “ easy ” ) ( see there for further descendants )
 *h₂ew-yo-m 
 > ? Proto-Germanic: *aują ( “ fortune, luck ” ) ( or from root 2 , “to perceive” ) 
 Proto-Norse: ᚨᚢᛃᚨ ( auja ) ( see there for further descendants )
 Unsorted formations 
 Proto-Celtic: 
 Breton: youl 
 Cornish: awell 
 Welsh: ewyllys 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: आवयत् ( ā́vayat ) 
 Sanskrit: अवस ( avasá ) 
 Proto-Italic: 
 Latin: avārus ( see there for further descendants )
 References
 [ edit ] 
 ↑ 1.0 1.1 1.2 1.3 Kroonen, Guus ( 2013 ), “*auþu-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN 
 ^ Beekes, Robert S. P. ( 2010 ), “ ἐνηής ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 424–425 : “ PGr. *ἆϝος or *ἦϝος ― PGr. *âwos or *êwos ” 
 Root
 [ edit ] 
 *h₂ew- or *h₃ew- [ 1 ] 
 to perceive , see , to be aware of
 Synonyms: *kʷey- , *(s)kewh₁- , *sent- 
 Alternative reconstructions
 [ edit ] 
 *aw- [ 2 ] 
 *h₄ew- [ 3 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₂ew- (perceive) (54 c, 0 e) 
 *h₂ṓws ( “ ear ” ) 
 ⇒ *h₂ḱ-h₂ows-yéti (< *h₂eḱ- ( “ sharp ” ) )
 *h₂ew-ís ~ *h₂ow-ís ( “ manifest, apparent, evident ” ) [ 4 ] ( or *h₃ēw-is [ 1 ] )
 ⇒ Proto-Balto-Slavic: *avis (locatives from the noun meaning “reality”)
 Lithuanian: ovyje ( “ in reality ” ) 
 Proto-Slavic: *avь ( “ obvious, apparent, rea
```


## [2026-09-07T20:27:17.550Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʰews-\" \\\n \"https://en.wiktionary.org/wiki/نغوشاک\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/gʰáwšas\" \\\n ; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 377: Ghosh root / Manichaean nigosag\" ; done; cd data/verification/sources/web && for f in $(ls -t *.txt | head -3); do echo \"##### $f\"; head -4 $f; done"
}
```


### [2026-09-07T20:27:21.093Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f5ca6cd767c69da9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba4060d637575654.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f761fd82d9b3d9a4.txt
##### f761fd82d9b3d9a4.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/gʰáwšas
FETCHED: 2026-09-07T20:27:21Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-Iranian/gʰáwšas - Wiktionary, the free dictionary
##### ba4060d637575654.txt
URL: https://en.wiktionary.org/wiki/نغوشاک
FETCHED: 2026-09-07T20:27:19Z
STATUS: -1
TITLE: 
##### f5ca6cd767c69da9.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʰews-
FETCHED: 2026-09-07T20:27:19Z
STATUS: -1
TITLE:
```


## [2026-09-07T20:27:25.917Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/web/f761fd82d9b3d9a4.txt',encoding='utf-8').read()\nt=re.sub(r'\\n+','\\n',t)\ni=t.find('From Wiktionary')\nprint(t[i:i+1800])\nEOF"
}
```


### [2026-09-07T20:27:27.297Z] TOOL RESULT

```
From Wiktionary, the free dictionary
 This Proto-Indo-Iranian entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-Iranian
 [ edit ] 
 Etymology
 [ edit ] 
 From *gʰáwšati ( “ to hear, listen; to shout ” ) +‎ *-as . [ 1 ] 
 Noun
 [ edit ] 
 *gʰáwšas   m [ 2 ] [ 3 ] 
 noise , sound 
 Declension
 [ edit ] 
 masculine a-stem
 singular
 dual
 plural
 nominative
 *gʰáwšas
 *gʰáwšā(w)
 *gʰáwšās(as)
 vocative
 *gʰáwša
 *gʰáwšā(w)
 *gʰáwšās(as)
 accusative
 *gʰáwšam
 *gʰáwšā(w)
 *gʰáwšāns
 instrumental
 *gʰáwšaH
 *gʰáwšaybʰyā(m)
 *gʰáwšāyš
 dative
 *gʰáwšāy
 *gʰáwšaybʰyā(m)
 *gʰáwšaybʰyas
 ablative
 *gʰáwšāt
 *gʰáwšaybʰyā(m)
 *gʰáwšaybʰyas
 genitive
 *gʰáwšasya
 *gʰáwšayās
 *gʰáwšānaHam
 locative
 *gʰáwšay
 *gʰáwšayaw
 *gʰáwšayšu
 Descendants
 [ edit ] 
 Proto-Indo-Aryan: *gʰáwṣas 
 Sanskrit: घोष ( ghóṣa ) ( see there for further descendants )
 Proto-Iranian: *gáwšah 
 Avestan: 𐬔𐬀𐬊𐬱𐬀 ( gaoša ) 
 Baluchi: گوش ( goš ) 
 Gurani: گۆش ( gɔš ) 
 Kurdish:
 Northern Kurdish: guh 
 Central Kurdish: گوێ ( gwê ) 
 Old Persian: 𐎥𐎢𐏁𐎠 ( g-u-š-a /⁠gauša⁠/ ) 
 Middle Persian: 𐭢𐭥𐭱 ( gʿš /⁠gōš⁠/ ) 
 Persian: گوش ( gôš ) 
 Tajik: гӯш ( güš ) 
 Ossetian: хъус ( qus ) , гъос ( ǧos ) 
 Pashto: غوږ ( ǧwaǵ ) 
 Zazaki: goş 
 → Old Armenian: գոյշ ( goyš ) 
 References
 [ edit ] 
 ^ Mayrhofer, Manfred ( 1992 ), “ GHOṢ ”, in Etymologisches Wörterbuch des Altindoarischen [ Etymological Dictionary of Old Indo-Aryan ]‎ [1] (in German), volume 1, Heidelberg: Carl Winter Universitätsverlag, page 518 
 ^ Fortson, Benjamin W. ( 2010 ), Indo-European Language and Culture: An Introduction , second edition, Oxford: Blackwell, page 203 : “ Indo-Ir. * ghauš - ” 
 ^ Cheung, Johnny (
```


## [2026-09-07T20:27:39.110Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN ear ===\"; python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'4\\.22\\s+EAR', t))[:3]:\n    print(t[m.start():m.start()+1800].replace('\\n',' '))\n    print('=====')\nEOF"
}
```


### [2026-09-07T20:27:40.469Z] TOOL RESULT

```
=== SYN ear ===
4.22 EAR Grk. ods Goth. auso Lith. ausis { NG abril ON eyra, hlust Lett. auss | Lat. auris Dan. re ChSl. ucho It. orecchio Sw. ora SCr.  uho | Fr. oreille OL are Boh.  ucho Sp. oreja, oido ME sere Pol. —-ucho Rum. ureche NE ear Russ. ucho Ir. au, cliias Du. oor Skt. karna- Nir. cluas OHG ara Av. gaosa-, karana-, W. clust MHG ar(e) u& (dual) Br. skouarn NHG ohr Most of the words for ‘ear’ belong to an inherited group. ‘These and the others, so far as their origin is clear, are related to words for ‘perceive, hear’ (15.11, 15.41), 1, If *aus- (also *dus-, *ous-, to ac- count for the Grk. forms) in various for- mations, esp. z-, n-, and s- stems; beside TE *au- in Skt. avis ‘evidently’, Grk. alc@dvouat ‘perceive’, etc. Walde-P. 1.17f. Ernout-M. 93. Walde-H. 1.85 f. Grk. ois (fr. *otcos, cf. ChSI. ucho), gen. obaros, Att. drs, dim. form ariop, used for ofs sometimes in NT, etc., whence (through 74 dria > 7’ abvria, Hat- zidakis, Mec. 2.322) NG abri; Lat. auris, in VLat. replaced by dim. auricula, oricla, whence It. orecchio, Fr. oreille, Sp. oreja, Rum. ureche, ete. (REW 793) ; Ir. au, 0; Goth. ausd, OF Zare, etc. , gen- eral Gme.; Lith. ausis, Lett. auss, OPruss. ausins (acc. pl.); ChSl. ucho (s-stem; but ¢-stem in dual, nom. ust, ete.); Av. nom. dual us (NPers. ho¥ ‘ear’); Arm. unkn. 2. Sp. oido ‘hearing’ and ‘ear’ as or- gan of hearing (but not used for the ex- = CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar aaa tw Digitized by Arya Samaj Foundation Chennai and eGangotri_ . ternal ear), deriv. of ofr ‘hear’, fr. Lat. audire ‘hear’. 3. Ir. cliias, NIv. cluas, W. clust : ON hlust ‘ear’ (beside eyra, cf. Vigfusson s.v.), OE hlyst ‘hearing’, hlystan ‘hear, listen’ (NE listen), etc. fr. IE *fKleu-s-, beside *kleu- in Skt. gru-, Grk. kdb ‘hear’, etc., from which
=====
```


## [2026-09-07T20:27:40.859Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nfor f in ('WLD_Bd1_pages.txt',):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for pat in ('ghous','ghöus','ghous-','gaosa'):\n        ms=list(re.finditer(pat,t))\n        print(f,pat,len(ms))\n        for m in ms[:2]:\n            print(t[max(0,m.start()-600):m.start()+700].replace('\\n',' '))\n            print('---')\nEOF"
}
```


### [2026-09-07T20:27:42.224Z] TOOL RESULT

```
WLD_Bd1_pages.txt ghous 2
                                                                                                                                                                                                                                                     ,        ga-kvsts Priifung afr. kest, ags cyst m. ..Gegenstand einer Wahl, Yorziiglich-                                ,                                                                   4                                                                       .                                      g                                               gheus-, ghous-           - geg(h)-, gog(h)-                                             569  keit" (aber gr. yevai                    erst einzelsprachliche                   Bildung von yevo/aai aus);                       lat.  gustus ,          Kosten, Geniefien", kelt. *gustu- ,,Wahl in den Xamen                -ils     ,,das                                                                                                          £                                                                                                              '     ir. Oengus, iergus , acymr. Ungust , Gurgust (z. B. Pick II 4 115; aber iiber cymr. usw. deivis „Wahl‘ s. Pedersen KG. I 210, Lw. aus lat. divtso ) und   
---
      ;                                  ,   Willkur).   7a.   B. CurtiuB* 177.                 — Xicht hierher ahd. kUski, nhd. keusch                                 ..rein,   keusch“ als „auserlesen“                (Sommer IP. 31, 372;                      bes. vermisse ich Stiitzen                       fiir   pas- sive Yerwendung des germ. Suffixes -ska-).                                        — Unannehmbar koppelt Fay Journ. of engl. and germ. Phil. XII Hr. 3 yens-                                          mit g>eu-                .,kauen“ und andern Wzln. zusammen.  gheus-     :        ghous- „tonen, horen“.   Ai. ghoiati               „ertont,                   Bedeutung am imp.                                            verkiindet laut,               hort“     (diese ghost von XeiBer BB. 20, 73 n. konstatiert), ghd&ayati „findetErhorung bei (acc.)“ (Geldner Rigveda in Auswahl I 58\ ghosa m. „Geton, Geschrei, Ruf, Larm“, .iri'aghdsa EX. „ Pferdeohr    Harighoka EN. „Gelbohr“ (= av.11                                                                               .    mirigaosa Lommel KZ. 50,262); av. gaos- „horen“, Kaus. in gUsayatuxda- „sein Wort zu Gehor bringend“, npers. niyT-slden „horen, horchen, lauschen“, bal. gosay „horen“, niyosay „horen, horchen, lauschen“, afgh. 
---
WLD_Bd1_pages.txt ghöus 0
WLD_Bd1_pages.txt ghous- 2
                                                                                                                                                                                                                                                     ,        ga-kvsts Priifung afr. kest, ags cyst m. ..Gegenstand einer Wahl, Yorziiglich-                                ,                                                                   4                                                                       .                                      g                                               gheus-, ghous-           - geg(h)-, gog(h)-                                             569  keit" (aber gr. yevai                    erst einzelsprachliche                   Bildung von yevo/aai aus);                       lat.  gustus ,          Kosten, Geniefien", kelt. *gustu- ,,Wahl in den Xamen                -ils     ,,das                                                                                                          £                                                                                                              '     ir. Oengus, iergus , acymr. Ungust , Gurgust (z. B. Pick II 4 115; aber iiber cymr. usw. deivis „Wahl‘ s. Pedersen KG. I 210, Lw. aus lat. divtso ) und   
---
      ;                                  ,   Willkur).   7a.   B. CurtiuB* 177.                 — Xicht hierher ahd. kUski, nhd. keusch                                 ..rein,   keusch“ als „auserlesen“                (Sommer IP. 31, 372;                      bes. vermisse ich Stiitzen                       fiir   pas- sive Yerwendung des germ. Suffixes -ska-).                                        — Unannehmbar koppelt Fay Journ. of engl. and germ. Phil. XII Hr. 3 yens-                                          mit g>eu-                .,kauen“ und andern Wzln. zusammen.  gheus-     :        ghous- „tonen, horen“.   Ai. ghoiati               „ertont,                   Bedeutung am imp.                                            verkiindet laut,               hort“     (diese ghost von XeiBer BB. 20, 73 n. konstatiert), ghd&ayati „findetErhorung bei (acc.)“ (Geldner Rigveda in Auswahl I 58\ ghosa m. „Geton, Geschrei, Ruf, Larm“, .iri'aghdsa EX. „ Pferdeohr    Harighoka EN. „Gelbohr“ (= av.11                                                                               .    mirigaosa Lommel KZ. 50,262); av. gaos- „horen“, Kaus. in gUsayatuxda- „sein Wort zu Gehor bringend“, npers. niyT-slden „horen, horchen, lauschen“, bal. gosay „horen“, niyosay „horen, horchen, lauschen“, afgh. 
---
WLD_Bd1_pages.txt gaosa 4
      caturah        ,                                                                          fem. keturios;               lett. cetri.          Aksl. cetyrc m.,        -i.   f.   n.           In Zs. fund Ableitungen)                                        q'ietur-, tfiehir -, qtctru-               :   ai.   cdiur-\nr3ga-]\ „vier-                        - gliedrig‘ |,mit Schwundst. der 1. Silbe av. a-xtuirlm „viermal‘', ai. turlya-h hirya-h            ,                                   av. cadwaro-aspa- (s. dazu Bgm. II 2 2, 15);                            av. tuirya- „vierter“; av. ra§ru-[gaosa -]  gr. T«Tpa-[^oo(ot], -n ovg, schwundstufig oder durch Diss.                                                      ;  aus rerga- gr. rgdjieCa (Lit. auch bei Boisacq 979); t gv-cpafaia „Helm“ (vgl. reiod-c/akog „mit vier Schirmen versehen“j wohl schwundstufig                                                                          *[g'“J(/w- fj. Schmidt KZ. 25, 46       Prellwitz BB. 25, 324, Bechtel Lex. 319; kaum                          f.,  diss. aus           Fick BB.       64), wie osk. trutom (wenn es „quartum“ 1   ,   bedeutet; sehr fraglich, ob auch in lat. tru-etdo, s. Yf. LEWb. 2 s. v.        lat.                                                                   ;  qttadru-\
---
                        mit g>eu-                .,kauen“ und andern Wzln. zusammen.  gheus-     :        ghous- „tonen, horen“.   Ai. ghoiati               „ertont,                   Bedeutung am imp.                                            verkiindet laut,               hort“     (diese ghost von XeiBer BB. 20, 73 n. konstatiert), ghd&ayati „findetErhorung bei (acc.)“ (Geldner Rigveda in Auswahl I 58\ ghosa m. „Geton, Geschrei, Ruf, Larm“, .iri'aghdsa EX. „ Pferdeohr    Harighoka EN. „Gelbohr“ (= av.11                                                                               .    mirigaosa Lommel KZ. 50,262); av. gaos- „horen“, Kaus. in gUsayatuxda- „sein Wort zu Gehor bringend“, npers. niyT-slden „horen, horchen, lauschen“, bal. gosay „horen“, niyosay „horen, horchen, lauschen“, afgh. ngvatql „horchen, gehorchen“ (Hiibschmann Pers. Studien 104), apers. gaasa        av. gaosa- m. „Ohr“, npers. gos ,,Ohr“ skyth. EX. 'Padayoooog „mit dem Kriegs- wagen rasselnd“ (XeiBer BB. 19, 252 iibersetzt „mit dem Kriegswagen fahrend“), av. zairi, gaosa- „mit gelben Ohren“; lat. hens „he, holla, liore“ (Wackernagel IF. 45, 309 ff. nach Benfey).   Fick I 4 203.             —                    Zur Bedeutung vgl. Lommel aaO. und im allgemeinen Bechtel Bezeichnung d sinnl. Wahrnehmung und 
---
```


## [2026-09-07T20:27:55.849Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'4\\.22\\s+EAR', t)\nseg=t[m.start():m.start()+4500].replace('\\n',' ')\ni=seg.find('gaosa',1200)\nprint(seg[1700:4200])\nEOF"
}
```


### [2026-09-07T20:27:57.373Z] TOOL RESULT

```
n’ (NE listen), etc. fr. IE *fKleu-s-, beside *kleu- in Skt. gru-, Grk. kdb ‘hear’, etc., from which root also Skt, grotra- ‘hearing, ear’, Toch. A klots, B klautso ‘ear’ (SSS, 128, 129). Walde- P. 1.494 f. Pedersen 1.80, Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53. 4, Skt. karna-, Av. karana- (of evil beings), etym.? Walde-P, 1.412, 495. Av. gaosa-, OPers. gauga- (NPers. gos ‘ear’) : Av. gus ‘hear’, Skt. ghosa- ‘noise’, ghosati ‘sounds, calls’. Walde-P. 1.569. Ay. us (dual), above, 1. an inherited group. The others are scure origin. ae Dies nas-. Walde-P. 2.318. Emout-M. 653, 659. Falk-Torp 779 f. Lat. nasus (> It. naso, Fr. nez, Rum. nas), also pl. narés ‘nostrils, nose’, late sg, naris (>Sp. nariz); ON sg. ngs nostril’, pl. nasar ‘nostrils, nose’, OE nosu, nasu, OHG nasa, etc., general Gme.; Lith. nosis, OPruss. nozy; ChSl. nosit, etc., general Slavic; Skt. nas-,; nas- (in RV only dual, nom. nasd, gen. nasos), Ay., OPers, nah- (sg. and dual in Av., sg. in OPers.). The meaning ‘nostril’ is implied by the early use of dual or pl. forms, but is not necessarily older than ‘nose’, For it may be abstracted from the latter, and the dual was favored by i ae in the case of ‘eyes’, ‘ears’, 2. Grk. pts, gen. pivds, also pl. pives ostrils, nose’ (like Lat. narés), etym.? . Seng ane either : Pr TAG ES i c, (Boisacq 842) or : with query) i ete. (Walde-P. 1.140 Possible, the word being n Digitized by Arya Samaj Foundation Chennai and eGangotri am BODY; BODILY FUNCTIONS AND CONDITIONS 227 gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo: the IE word, like the following which displaced it in turn. NG porn, fr. Grk. pizis used by Aris- tot. (HA 52415 ff.) for an organ of the cuttlefish connected with the ink sac, and attested as a vulgar term for ‘snout, nose’ by Eust., Comm. 950 (oi ri piva pirw xadécavres), prob. : Lith. mute, Skt. mukha- ‘mouth,’ etc. (4.24). Walde-P. 2.310. 3. Ir. srén = W. ffroen, Br. f
```


## [2026-09-07T20:28:07.065Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nfor pat in (r'ghous', r'gheuso', r'ousos', r'aus-os', r'ausis'):\n    ms=list(re.finditer(pat,t))\n    print('#####',pat,len(ms))\n    for m in ms[:2]:\n        print(t[max(0,m.start()-350):m.start()+450].replace('\\n',' '))\n        print('--')\nEOF"
}
```


### [2026-09-07T20:28:08.479Z] TOOL RESULT

```
##### ghous 0
##### gheuso 0
##### ousos 11
ters ‘bold’ dhoub- (plunge; deep; depth'. Cf. dhub-. WP I, 847 Tokh. B tsop-, v. ‘plunge’ (for expected B: *tsaup-); W. Br. du, dü “black? (but Ir. dubh, id. is in z-gde); MHG touf ‘plunge; depth; baptism’; Du. doop, id.; OS dópian ‘dip, baptize’; Li. daubà ‘abyss, ravine’; dáuba *warm spot in silo? dhoubh- (o-gde form of dhübh-, q. v.) dhorg- — dhousos, ios, io 20 25 30 35 40 45 200 MHG toube ‘wildly’; tóuben “blow? beside (z-gde) OHG tobon, -én, OS dofón; OE do- fian ‘rave, rage’: Gk. te-táphomai, id. beside tüphóo, id. The simplex (long-gde) in Gk. tüphos 'stupor, delusion, nonsense”, extended in tūphõn ‘gale’. Icel. deyfa ‘blunt, deaden, stun’ suggests a link with (equally o-gde) MHG toup, bes OE deaf, etc. esp. in view of the zero-gde isophone Gk. tuphlós *blind' dhoubh- (2) “depth; p
--
q. v.). Cf. dhoukseið, dhuks- Skt. cf. (z-gde) dhukse, mp. 'animate, fire; be weary’, MW duch ‘affection’; W ‘sigh, groan’; Finn. LW tuoksu ‘aroma, vapour. The Slavonic forms duxü ‘breath’, duša, id. and ‘soul, are ambig. (*-ks- or *-s-) (see dhous-) dhoun- “blow, stink'. Cf. dhun- ON daunn ‘stench’; OCS dung, oti ‘blow’; Lusat. dunu, dunyc, id. dhousos, ios, io “spirit, breath, creature”. Cf. dhouks-. WP I, 846 Gk. en-thousía ‘inspiration’; Illyr. Dasios, Dazios, Deusus; Messap. daoza-, dozas; Alb. dash, pl. desh ‘ram’; i dashém *beloved' = Ill. Dasimos, -a and variants; Gaul cf. (name) *Dousios beside dusios, m. (z-gde) ‘demon’ MHG tore, wm. (*fooP, fr. *dhousón); OCS duxü, düsa, m.f. “breath, spirit; soul; Cz. cf. dusiti ‘to smother, stew’; Li. daüsos ‘upper air, paradise? 201 dhousro-,
--
##### aus-os 0
##### ausis 9
 pl. eyrir Comte, A LW?); Li. áukšas. (A much-disputed word. For Arm. oski, vo, vov “gold” reference has been made both to Sumerian guškin, id., 43 ' Georgian okhro, id. and Basque urhe, id. as well as to Finn. vaski ‘copper’; Est. vask, id. and to Hung. vas ‘iron’. Cf. A. Joki: Uralier ü. Indogermanen, 1973, pp. 339, 340 for spe- culations). OPr. ausis ‘gold’ displays an ab- sence of the implied glottal stop as seen in Li. áuksas, cf. al'sios above, and o'st- ‘bone’ below in relation to Li. kab-akstis ‘skeletom ausa, io ‘dawn’. Cf. ausorå (ausora) Skt. usá; Gk. ada; MHG ost; OE easte and comm. Gmc. ‘east’; Latv. ausa ‘dawn’. (For Arm. awr ‘day’, see ausórá) ausak- (ousak-) ‘cared’. Cf. ausis Olr. óach; Ger. cf. lang-ohrig; Cz. cf. ušák ‘earwig’ ausərā, see ausora ausis (ousis, usis) ‘ear;
--
Pr. ausis ‘gold’ displays an ab- sence of the implied glottal stop as seen in Li. áuksas, cf. al'sios above, and o'st- ‘bone’ below in relation to Li. kab-akstis ‘skeletom ausa, io ‘dawn’. Cf. ausorå (ausora) Skt. usá; Gk. ada; MHG ost; OE easte and comm. Gmc. ‘east’; Latv. ausa ‘dawn’. (For Arm. awr ‘day’, see ausórá) ausak- (ousak-) ‘cared’. Cf. ausis Olr. óach; Ger. cf. lang-ohrig; Cz. cf. ušák ‘earwig’ ausərā, see ausora ausis (ousis, usis) ‘ear; pot-handle'. WP I, 18 Av. (dual) uši; Ober, u31; Arm. unkn, unkan, -amb (dual or dim. ?) beside unkunk (a plural or dual form: *pot-handle); Hitt. cf. ehuratius /(ear-stoppers'; Myc. & Gk. cpds. Owes, -oes *-eared'; Gk. os, gs. otós (oblique forms unexplained); cf. lag-oós ‘hare’, Alb. vesh, pl. veshë (fear, beside vath ‘earring’, fr. *ausoKo-
--
```


## [2026-09-07T20:28:29.913Z] TOOL CALL #66: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/site/pages/377.jpg 2>/dev/null || (pdftoppm -f 377 -l 377 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg377 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg377.png)"
}
```


### [2026-09-07T20:28:31.251Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 55500 Aug 22 01:02 /home/sfmqrb/git/rishe/site/pages/377.jpg
```


## [2026-09-07T20:28:34.761Z] TOOL CALL #67: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/377.jpg"
}
```


### [2026-09-07T20:28:34.783Z] TOOL RESULT

```

```


## [2026-09-07T20:28:48.585Z] TOOL CALL #68: Bash

```json
{
 "command": "SP=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 377 -l 377 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $SP/pg377 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$SP/pg377.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.53),int(h*0.23),int(w*0.80),int(h*0.28))).save('$SP/crop377-niush.png')\n\"; ls -la $SP"
}
```


### [2026-09-07T20:28:51.442Z] TOOL RESULT

```
(3400, 4400)
total 34200
drwx------ 2 sfmqrb sfmqrb    12288 Sep  7 16:28 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95065 Sep  7 15:49 361-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65864 Sep  7 15:52 362-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77269 Sep  7 15:46 364-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   160756 Sep  7 15:55 365-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87585 Sep  7 15:50 366-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1583 Sep  7 16:16 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79304 Sep  7 15:38 bqt2195_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6375 Sep  7 16:28 crop377-niush.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70860 Sep  7 15:48 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    34373 Sep  7 15:52 e0_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:51 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:52 e2_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53090 Sep  7 15:49 mk361.py
-rw-rw-r-- 1 sfmqrb sfmqrb    86861 Sep  7 15:51 mk362.py
-rw-rw-r-- 1 sfmqrb sfmqrb    33821 Sep  7 15:52 mk363a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36857 Sep  7 15:52 mk363b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62290 Sep  7 15:49 mk366.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54370 Sep  7 15:45 mk368.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4789 Sep  7 15:38 p361_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   118891 Sep  7 15:45 p365_row8.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13022 Sep  7 15:42 p366_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3884 Sep  7 16:21 p372_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6025 Sep  7 16:21 p372_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36604 Sep  7 16:22 p372_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15566 Sep  7 16:22 p372_q4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4259 Sep  7 16:21 p372_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94462 Sep  7 15:45 pg365.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1760 Sep  7 16:24 pg369-eb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18053 Sep  7 16:23 pg369-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108532 Sep  7 16:23 pg369hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7447 Sep  7 16:23 pg369-latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3387 Sep  7 16:24 pg369-nocht.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74176 Sep  7 16:23 pg369.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40427 Sep  7 16:22 pg371crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9084 Sep  7 16:22 pg371crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90632 Sep  7 16:22 pg371hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53926 Sep  7 16:17 pg371.png
-rw-rw-r-- 1 sfmqrb sfmqrb   152304 Sep  7 16:21 pg372hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59170 Sep  7 16:21 pg372.png
-rw-rw-r-- 1 sfmqrb sfmqrb    47783 Sep  7 16:19 pg375.png
-rw-rw-r-- 1 sfmqrb sfmqrb   100033 Sep  7 16:28 pg377.png
-rw-rw-r-- 1 sfmqrb sfmqrb       40 Sep  7 16:16 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T20:28:55.971Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop377-niush.png"
}
```


### [2026-09-07T20:28:55.985Z] TOOL RESULT

```

```


## [2026-09-07T20:29:12.061Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef find(f, pats, ctx=250, limit=2):\n    if not os.path.exists(f): print('MISSING',f); return\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for p in pats:\n        ms=list(re.finditer(p,t))\n        print('###',os.path.basename(f),p,len(ms))\n        for m in ms[:limit]:\n            # page tag\n            tag=None\n            mm=None\n            for x in re.finditer(r'\\[pdf page (\\d+)\\]', t[:m.start()]): mm=x\n            if mm: tag=mm.group(1)\n            print('  [pdf page',tag,']',t[max(0,m.start()-ctx):m.start()+ctx].replace('\\n',' '))\nfind('incoming/FFD/FFD_pages.txt', ['نیوش','نغوش'])\nfind('SOD_pages.txt', ['nyws','ny.ws','niyōš'])\nfind('incoming/ARY/ARY_latin_index_pages.txt', ['GAUSHA','GHOSH','gaush'])\nEOF"
}
```


### [2026-09-07T20:29:13.333Z] TOOL RESULT

```
### FFD_pages.txt نیوش 3
  [pdf page 85 ] ت. 800 صورت اصلی ۶۶ است. 0 پیش از 1به ۶ بدل شده است. ريشهٌ ۶0 به معنی «آراستن» است. نهنب < فارسی میانه 200000 < فارسی باستان 21-0020 < ایرانی باستان ۶21-۶ 2 پیش از 0 برای ساختن مادهٌ مضارع از ريشه آورده شده است. (سفتن) هم از ريشهٌ 9 آمده است > سفتن. نیوشیدن نیوشید < فارسی میانه 5870قا:. 5576انه مادة ماضی جعلی است» از مادة مضارع ساخته شده است. نیوش « فارسی میانه 2105 « ایرانی باستان 21-82053-8*. برای 2 آرای. 1 پیشوند فعلی است. ريشهٌ 8895 به معنی «گوش کردن» است. «گوش» هم از ريشةٌ 8203 آمده است. صو
  [pdf page 85 ] ورت اصلی ۶۶ است. 0 پیش از 1به ۶ بدل شده است. ريشهٌ ۶0 به معنی «آراستن» است. نهنب < فارسی میانه 200000 < فارسی باستان 21-0020 < ایرانی باستان ۶21-۶ 2 پیش از 0 برای ساختن مادهٌ مضارع از ريشه آورده شده است. (سفتن) هم از ريشهٌ 9 آمده است > سفتن. نیوشیدن نیوشید < فارسی میانه 5870قا:. 5576انه مادة ماضی جعلی است» از مادة مضارع ساخته شده است. نیوش « فارسی میانه 2105 « ایرانی باستان 21-82053-8*. برای 2 آرای. 1 پیشوند فعلی است. ريشهٌ 8895 به معنی «گوش کردن» است. «گوش» هم از ريشةٌ 8203 آمده است. صورت فارسی
### FFD_pages.txt نغوش 0
### SOD_pages.txt nyws 34
  [pdf page None ]                                                                                             ^r*jj*     sorrowful                                                Hen. Tales. 470.51; GMS 655     BBB 510; GMS 1059; Tales. 472.34, 473.24             988 >nyws B 977 >ndwxc xwr-      M                      jjj_^0Jxl     andoxc xur                                               anxas =^x}s, Vs, 'ny's, By}ns                        <wk-*=>-                                                              dispu
  [pdf page None ]    h'zYwhl       0o)retirc, OoOwithdraw       GMS         V5 343; Sogdica. 34n3, 30 Add.; Frag. Lcn. Ill            1031 'nyw'st-    B                  (o^)j^-^<j^o^                                                                        anxwast     Onywst-)     ©pt. st. ^'nyw'y-1, 'nxw'y- 1020 'nyst- B                                 o^-^^j^                                                                        OoMnfrin     G         (      anxast ©pt. st. ^nyz-, 'ny'st-                         
### SOD_pages.txt ny.ws 13
  [pdf page None ]  prayer           BSTBL, Intox. 36                            ijt^*^*         VJ 1129,1367  5890 nyMin B ^ ny'm                                            5901 ny'wnt'y =* ny'wnt'k  5891 nyW C -» ny*'                                             5902 ny'ws- B, M, 5 yj^ ^)d^^            O^j^      < 0-^  5892 nyW M                                          U?Ur fUj            niya6a (ny'dO ©*ni-gadaka ©f. n.                            niyos (nyws-, nyyws) ©<*ni~gausa-; Parth.           prayer, reque
  [pdf page None ] '                                             5902 ny'ws- B, M, 5 yj^ ^)d^^            O^j^      < 0-^  5892 nyW M                                          U?Ur fUj            niya6a (ny'dO ©*ni-gadaka ©f. n.                            niyos (nyws-, nyyws) ©<*ni~gausa-; Parth.           prayer, request S                                                                         ngws-, MP nyws-     ©impf. nyY(y)ws ^nywst-,           Hen. Tales. 472.1; GMS 676; STSC 134.29; STii             2.15; BST
### SOD_pages.txt niyōš 0
### ARY_latin_index_pages.txt GAUSHA 2
  [pdf page 445 ] (GRAVE) 411 GRAV SWEDISH) 8 yo SKEAT: (GRAVE) 248 GRAVE NORWEGIAN) «533 1Ade sou dly GRAF (DUTCH) «gece (OLD CHURCH SLAVIC) oS | poe 9,8 Shep GAS'3 gay} GUOKS 22 5s gel ont ae eee eee (AFGHANI) (3-4) gs! GAOSHA, USHI —{AVESTAN) pls! . GHVAGH, GHWAZH GAUSHA (OLD PERSIAN) jee go GHOSHA SANSKRIT) ey Suite GOSH PAHLAVI) 5.344 UNKN ARMENIAN) ga) GHOs, QUS AOSSETIC) gy! ots (GREEK) 3, Gun (KURDISH) «53,5 AURIS, AURICULA LATIN) 3 GOSH NBALUCHD > 3h [pdf page 446] Fr | as OOR (DUTCH) «g.the OREILLE H(P
  [pdf page 511 ] S gf SL NID HOLD ENGLISH) oS gJS Jeetlaok seed 9 Bore Sb hr 2egy} Sbasly 52 Sy ge mY andy (Dba (Sate iV GWG 22 05s Gal etl tals oat 3t "SS" "SS" lenjly LEY NGVALAL, NGHVATAL AVESTAN) glen) "YSANSKRIT) ey Sunil GUSHAYAT., NI-GAOSH GHOSHATI, GHOSAYATI GAUSHA- :(OLD PERSIAN) ime go HEUS LATIN) gd PAHLAVD <3 Jy NIGHOSHITAN, NIOXSHIDHAN ‘REFERENCES bey QUSIN, GHOSSUN — :(OSSETIC) 5) POKORNY: 454 BALUCHD gz ge MACKENZIE: (HEAR) 117 NIGOSHAG, NIGHOSHAGH vera tabi dey MAFGHANI) (4) gl! Jeetheal foay tat
### ARY_latin_index_pages.txt GHOSH 4
  [pdf page 445 ] yo SKEAT: (GRAVE) 248 GRAVE NORWEGIAN) «533 1Ade sou dly GRAF (DUTCH) «gece (OLD CHURCH SLAVIC) oS | poe 9,8 Shep GAS'3 gay} GUOKS 22 5s gel ont ae eee eee (AFGHANI) (3-4) gs! GAOSHA, USHI —{AVESTAN) pls! . GHVAGH, GHWAZH GAUSHA (OLD PERSIAN) jee go GHOSHA SANSKRIT) ey Suite GOSH PAHLAVI) 5.344 UNKN ARMENIAN) ga) GHOs, QUS AOSSETIC) gy! ots (GREEK) 3, Gun (KURDISH) «53,5 AURIS, AURICULA LATIN) 3 GOSH NBALUCHD > 3h [pdf page 446] Fr | as OOR (DUTCH) «g.the OREILLE H(PRENCH) «13 HOLD CHURCH SLAVI
  [pdf page 511 ] y NITH {OLD SAXON) oS gf SL NID HOLD ENGLISH) oS gJS Jeetlaok seed 9 Bore Sb hr 2egy} Sbasly 52 Sy ge mY andy (Dba (Sate iV GWG 22 05s Gal etl tals oat 3t "SS" "SS" lenjly LEY NGVALAL, NGHVATAL AVESTAN) glen) "YSANSKRIT) ey Sunil GUSHAYAT., NI-GAOSH GHOSHATI, GHOSAYATI GAUSHA- :(OLD PERSIAN) ime go HEUS LATIN) gd PAHLAVD <3 Jy NIGHOSHITAN, NIOXSHIDHAN ‘REFERENCES bey QUSIN, GHOSSUN — :(OSSETIC) 5) POKORNY: 454 BALUCHD gz ge MACKENZIE: (HEAR) 117 NIGOSHAG, NIGHOSHAGH vera tabi dey MAFGHANI) (4) g
### ARY_latin_index_pages.txt gaush 0
```


## [2026-09-07T20:30:15.580Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-316.json'))\nfor e in d['entries']:\n    for n in e['nodes']:\n        if not n.get('ref_check') or n['ref_check'][0].get('ref') in (None,'None','',):\n            print(json.dumps(n['ref_check'],ensure_ascii=False)[:400]); print('id',n['id']); break\nEOF\nsed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T20:30:16.865Z] TOOL RESULT

```
[{"ref": "None", "status": "not_checked", "note": "Nourai gives no reference for this node; checked against Etymonline, Klein and Skeat instead."}]
id 5
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


## [2026-09-07T20:30:23.501Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in (r'aus-\\s*:\\s*ous-', r'ous-\\s*,\\s*us-', r'„Ohr', r'ausis'):\n    ms=list(re.finditer(pat,t))\n    print('###',pat,len(ms))\n    for m in ms[:3]:\n        mm=None\n        for x in re.finditer(r'\\[pdf page (\\d+)\\]', t[:m.start()]): mm=x\n        print(' [pdf',mm.group(1) if mm else '?',']', t[max(0,m.start()-500):m.start()+600].replace('\\n',' '))\n        print('--')\nEOF"
}
```


### [2026-09-07T20:30:24.867Z] TOOL RESULT

```
### aus-\s*:\s*ous- 0
### ous-\s*,\s*us- 0
### „Ohr 22
 [pdf ? ] s“,   jancih   „fiihle'‘.     lett.       jausu „gebe zu ver-     ) nehmen“ trotz Persson nicht hierher, s. Wz. *euat-, ai. upi-vatati.    Walde, Etymologisches Worterbuch. F.                                                         2 18        Aber mhd. e-ounen               ,                                          ags. eet-yivan „zeigen“      (Zupitza   GG. 74          als       Alter- nativvorschlag) bleibt bei                 *<3g“-   „sehen“.      Hierzu sehr wahrscheinlich:      aus- n. „Ohr, Gehor“,                  kons. St. (zum -s vgl. idg. o\u\s „Mund“,                       *nas „Nase“), im n. sg. und einigen andern Kasus als z-St.                            *aits-i,       und im lat. und Balt, als solcher geschlechtig geworden; daneben als ew-St. *aus-on- (vgl. J. Schmidt KZ. 26, 17, Brugmann Grdr. II 2 1, 132, 173, weitere Lit. bei Schulze Qu. ep. 38 a 1, Yf. LEWb. 2 76, Boisacq 730 f.)      Av. usi    (n.       du.)   „die     beiden Ohren“, ubertragen .(Verstand, Einsicht, Sinn“    (v. Fierlinger          KZ. 27, 335, weitere Lit. bei Bartholomae Airan. Wb. 414;    
--
 [pdf ? ]                          *aits-i,       und im lat. und Balt, als solcher geschlechtig geworden; daneben als ew-St. *aus-on- (vgl. J. Schmidt KZ. 26, 17, Brugmann Grdr. II 2 1, 132, 173, weitere Lit. bei Schulze Qu. ep. 38 a 1, Yf. LEWb. 2 76, Boisacq 730 f.)      Av. usi    (n.       du.)   „die     beiden Ohren“, ubertragen .(Verstand, Einsicht, Sinn“    (v. Fierlinger          KZ. 27, 335, weitere Lit. bei Bartholomae Airan. Wb. 414;     idg. *ns-T; instr. du. av. usibya ), up. hos( *aits -) „Ohr“; aksl. n. du. usi (idg. *nus-l),           sonst es-St. ucho , g.                                                   „Ohr“; lit. aus'is f., lett. auss,                                                            2 iie.se   apr. ausins acc. pi. ds. (g. pi. lit. aitsu noch konsonantisch); arm. unkn (g. unknn ) „Ohr“ (aus *uson-qo-m mit demselben /.-Formans wie gr. cbyJdeg                                      •     £vu)t la Hes. aus *oa-y.o-, Osthoff v. Patrubanys Sprw. Abh. 2, 54 f. 97 s. u.)                        ;    got. imsu as. ahd. Ora, an. eijra „Ohr“, und vom z-st. *ausi- mit o- und
--
 [pdf ? ] n- (vgl. J. Schmidt KZ. 26, 17, Brugmann Grdr. II 2 1, 132, 173, weitere Lit. bei Schulze Qu. ep. 38 a 1, Yf. LEWb. 2 76, Boisacq 730 f.)      Av. usi    (n.       du.)   „die     beiden Ohren“, ubertragen .(Verstand, Einsicht, Sinn“    (v. Fierlinger          KZ. 27, 335, weitere Lit. bei Bartholomae Airan. Wb. 414;     idg. *ns-T; instr. du. av. usibya ), up. hos( *aits -) „Ohr“; aksl. n. du. usi (idg. *nus-l),           sonst es-St. ucho , g.                                                   „Ohr“; lit. aus'is f., lett. auss,                                                            2 iie.se   apr. ausins acc. pi. ds. (g. pi. lit. aitsu noch konsonantisch); arm. unkn (g. unknn ) „Ohr“ (aus *uson-qo-m mit demselben /.-Formans wie gr. cbyJdeg                                      •     £vu)t la Hes. aus *oa-y.o-, Osthoff v. Patrubanys Sprw. Abh. 2, 54 f. 97 s. u.)                        ;    got. imsu as. ahd. Ora, an. eijra „Ohr“, und vom z-st. *ausi- mit o- und H-             ,   Erweiterung ahd. Ori „das Ohr“, mhd. cese „Ose, Henkel“; air. an 0 „Ohr“                         ,   (
--
### ausis 2
 [pdf ? ] . Basis             or oh-,   rubh- „arbeiten“              zu stutzen vermag; gegen Bezzeri-  berger BB. 27. 150: iiber aprbpiu                        s.   u.   rep- ,,an sich reiBen".       Altere Lit. bei Curtius 294. 292.                                                                                                   r  osi-s.         osen-.     osk-      (vielleicht    mit Formans -sko-.                  *os-sko- !       Charpentier            KZ. 40, 440) „Esche“.       Lit. nosis. lett. ausis (g. nusa). apr. tcoasis ,,Esche" 1 j       russ. (usw.) jase.no ,,Esche" (aber iiber si. jasika. osina                             „Espe" s. *apsa ):  lat.      omits „wilde Bergesche" (*bsen-o$ oder bsi-n-os:                                 Fick BB. 16, 171.        ’)    Gr. ayto-oii; .Weitipappel" [Fick BB. 16. 171. Sehiader RL. 205,                     Uldenbeck PBrB.  26, 295: zur Verbindung des 1. Gliedes mit si. jezero .See' usw. vgl. Rozwadowski, Roczr..  Slav. VII 19, anders Trautmann Apr. 30 If) ist vielmehr blofie Ableitung mittelst -id- voi.  dem Stamme.     der auch der Fhifi
--
 [pdf ? ] ags. d-hneopan „abpfliicken“     mit                     ;   intensiver Kons.-Doppelung norw. mdartl. nuppa „pfliicken, rupfen", ags. hnoppian „pfliicken“, dan. mnd. noppe „Wollflocke, Zotte, Hechelhede"   mit idg. bh aisl. linyfdl „kurzes, abgestumpftes Horn, Lamm mit solchen                   :    Hornern", nd. nobbe, nubbe „'Wollflocke“, mhd. noppe, nop „Tuchflocke“ i^wenn nicht Lw. aus mnd. noppe)-, Fick III 4 100 s. Falk-Torp u. noppe                             ,   nubb.   s-Erw.: lett. knausis „kleine Miicke" (wie knisis, knislis von deri-Basis), Persson Beitr. 882.   Ygl. zur w-Basis auBer der o. angefiihrten Lit. noch Fiekl 4 391, III 4 99 f., Persson Wzerw. 134 (Lit.), Prellwitz 2 231, Johansson PBrB. 14, 338 ff., Zupitza Gutt. 120.    Ygl. die ahnlichen Wzln. ghen-;          aus ihr durch s-Praefix sghen-, sken- und endlich ken- entsprungen sein zu lassen, iiberschreitet durchaus die Grenzen unserer Erkenntnis; auch die Vermutung urspriinglicher Gleich- heit mit sqen- „abspalten“ (s. d. Liden BB. 21, 107 f Persson Beitr. 809                                    ;   Anm. 2) i
--
```


## [2026-09-07T20:30:39.660Z] AGENT

Now I'll write the verification file.


## [2026-09-07T20:30:42.275Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg377.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/377.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T20:30:42.341Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T20:37:49.417Z] TOOL CALL #74: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk377.py",
 "content": "# -*- coding: utf-8 -*-\nimport json\n\nW_H2OWS = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ows-\"\nW_H2EW  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ew-\"\nW_GUSH  = \"https://en.wiktionary.org/wiki/گوش\"\nW_GUSHV = \"https://en.wiktionary.org/wiki/گوشواره\"\nW_NIY   = \"https://en.wiktionary.org/wiki/نیوشیدن\"\nW_PII   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/gʰáwšas\"\nE_EAR   = \"https://www.etymonline.com/word/ear\"\nE_ANE   = \"https://www.etymonline.com/word/anesthesia\"\nE_AUD   = \"https://www.etymonline.com/word/audio-\"\nE_OBEY  = \"https://www.etymonline.com/word/obey\"\n\nPOK785 = (\"Pokorny 785 (POK_02.txt, printed p.785 in the IEW database dump): \"\n          \"\\\"Root/lemma: ōus-2, aus-: us-  Meaning: ear … Latin auris f. 'ear' (*ausi-s) … \"\n          \"Gothic ausō n. 'ear' (Germanic *ausan-) … Old English ēare … Greek ous (stem ōt-) … \"\n          \"References: WP. I 18, WH. I 85 f.\\\"\")\nPOK78 = (\"Pokorny 78: \\\"Root/lemma: h₂u-8, h₂auei-  Meaning: to perceive, understand … \"\n         \"full grade: gr. αἰσθάνομαι, Aor. αἰσθέσθαι 'perceive' (*aϝισ-θ-); Latin audiō 'hear' from \"\n         \"*auiz-dʰ-iō, compare oboedio from *ob-avizdhiō … References: WP. I 17, WH. I 80.\\\" \"\n         \"(POK_02.txt / POK_full.txt, s.v.)\")\nPOK454 = (\"Pokorny 454 = POK_02.txt leaf 110 (leaf = p−344): \\\"ghous- ,tönen, hören'? Nur indoiranisch. \"\n          \"Ai. ghōṣati ,ertönt, verkündet laut, hört' … av. gaoš- ,hören', Kaus. in gūšayat-uxδa- … \"\n          \"npers. niyōšīdan ,hören, horchen, lauschen', bal. gōšay ,hören' … apers. gauša-, av. gaoša- m. ,Ohr', \"\n          \"npers. gōš ,Ohr' … WP. I 569.\\\"\")\n\nBQT1858 = (\"BQT vol.3 pdf page 652 = printed 1858 (the following leaf carries the running head '-۱۸۵۹-'), \"\n           \"Mo'in's footnote 3 to گوش: «اوستا gaosha «بارتولمه ۴۸۹»، پهلوی gōsh …، پارسی باستان gausha، \"\n           \"هندی ghosha (صدا)، کردی …، بلوچی gōsh، وخی ghish, ghüsh» \"\n           \"(grep 'اوستا' in incoming/BQT/BQT_v3_pages.txt, block [pdf page 652]).\")\nBQT2239 = (\"BQT vol.4 pdf page 322 (= printed 2241; the anchor [pdf page 279] carries the running number ۲۱۹۹, \"\n           \"so printed = pdf+1919/1920 and Nourai's numbering runs ~2 pages behind this Ibn Sina scan, exactly as on p.316), \"\n           \"Mo'in's footnote 6 to نیوشیدن: «niyōšīdan … از: نیوش + یدن (پسوند مصدری)؛ پهلوی nigōšītan (شنیدن، مخفیانه گوش دادن) … \"\n           \"«نیبرگ ص ۱۵۸»، رک: نغوشا، نغوشاک. هرن گوید: نیوشیدن، اوستایی ni + gaoša (شنیدن، گوش دادن) … \"\n           \"هوبشمان قول هرن را … از ریشهٔ ایرانی ni-gauš تأیید می‌کند»; footnote 7 on the same page prints Nourai's Ferdowsi \"\n           \"line «فرستاده را گفت نیکو نیوش / بگو آنچه بشنیدی ای تیزهوش» (لغت فرس ص ۲۱۷).\")\n\nMON_NC = (\"The 6-volume Amir Kabir Farhang-e Farsi is not online in any permitted copy (refs_online.json: \"\n          \"only the 2-vol Adena abridgement, different pagination), so page 4746 itself cannot be opened; \"\n          \"the corresponding entries of the abridgement are quoted under 'consulted'.\")\n\nETM_NC = (\"Abolghasemi, Risheh-shenasi (ETM) has no digital copy on any permitted platform \"\n          \"(refs_online.json: catalogue/purchase only), so p.71 could not be read. Cross-checked instead \"\n          \"against the same author's Fe'l-hā-ye Fārsi-ye Dari (FFD), on disk.\")\n\nroot = {\n  \"entry\": 0,\n  \"root\": \"Ôus 1, Au 1, Aus 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h₂ṓws (*ous-/*aus-/*us-) 'ear' (Pokorny ōus- 2, aus-, us-, p.785; Watkins/AHD ous-), a derivative of the root *h₂ew- 'to perceive, be aware of' (Pokorny au-8, auēi- p.78; Watkins au-5 'to perceive')\",\n  \"note\": (\"The root box is right on every count. (1) Both reconstructions are real and both page references hit: \"\n           \"POK:785 is Pokorny's ōus-/aus-/us- 'Ohr', POK:78 is his au-8/auēi- 'sinnlich wahrnehmen', which is the \"\n           \"source of Latin audiō and Greek αἰσθάνομαι — i.e. exactly the two entries Nourai has merged, and exactly \"\n           \"the two Watkins entries (AHD 'ous-. Also aus-. Ear.' and 'au-5. To perceive.') behind the three AHD-marked \"\n           \"branches at the bottom of the page. (2) Merging them is not Nourai's invention: Walde–Pokorny I 18 puts \"\n           \"aus- 'Ohr, Gehör' under the preceding *au- root with the words 'Hierzu sehr wahrscheinlich'; Buck 4.22 says \"\n           \"the 'ear' words are 'related to words for perceive, hear … beside IE *au- in Skt. aviṣ, Grk. αἰσθάνομαι'; \"\n           \"and Wiktionary's current entry derives *h₂ṓws 'ear' from *h₂ew- 'to see/perceive' + *-s. Klein likewise \"\n           \"files 'ear' under 'I.-E. base *au-, ear'. (3) The language label 'Indo-European' and the gloss 'ear' are \"\n           \"correct. The one thing the sources do NOT support is the branch Nourai hangs under this root on this page: \"\n           \"the Iranian gaoša/gōš family (node #1 'Ghosh'), which belongs to a separate, Indo-Iranian-only root \"\n           \"*gʰews- 'to sound, hear' (Pokorny 454, WP I 569). Nourai's own NOTE ('Derivation from this root is not \"\n           \"certain') admits as much, and modern scholarship sides with the caution. Note also that Nourai's POK:457 \"\n           \"(nodes #1 and #2) is a slip for POK:454.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *h₂ṓws «گوش» (پوکورنی ص ۷۸۵) و ریشهٔ *h₂ew- «دریافتن، آگاه شدن» (پوکورنی ص ۷۸، \"\n              \"خاستگاه audīre لاتین و αἰσθάνομαι یونانی) هر دو واقعی‌اند و هر دو ارجاع نورایی (POK:78,785) درست است. \"\n              \"یکی‌دانستن این دو ساختهٔ نورایی نیست: والده–پوکورنی (ج۱ ص۱۸) خودِ aus- «گوش» را «بسیار محتمل» زیر همان \"\n              \"ریشهٔ *au- «دریافتن» می‌آورد، باک (بند ۴٫۲۲) و کلاین نیز همین کار را می‌کنند و ویکی‌واژه امروز *h₂ṓws را \"\n              \"مشتقِ *h₂ew- + *-s می‌داند. پس عنوان ریشه، برچسب زبانی و معنای «گوش» درست است. تنها اشکال، شاخهٔ ایرانی \"\n              \"gaoša/گوش (گرهٔ ۱، «Ghosh») است که از ریشهٔ جداگانه و تنها هندوایرانیِ *gʰews- «آوا دادن، شنیدن» (پوکورنی ص ۴۵۴) \"\n              \"می‌آید؛ خودِ نورایی هم در یادداشت نوشته «این اشتقاق قطعی نیست» و پژوهش امروزی همین احتیاط را تأیید می‌کند. \"\n              \"ضمناً ارجاع POK:457 در گره‌های ۱ و ۲ لغزش قلم برای POK:454 است.\"),\n  \"sources\": [W_H2OWS, W_H2EW, E_EAR],\n  \"ref_check\": [\n    {\"ref\": \"POK:785\", \"status\": \"supports\", \"note\": POK785},\n    {\"ref\": \"POK:78\", \"status\": \"supports\", \"note\": POK78},\n    {\"ref\": \"KLN:494\", \"status\": \"supports\",\n     \"note\": (\"Klein s.v. 'ear, n., the organ of hearing. ME. ere, fr. OE. eare, rel. to ON. eyra … Goth. ausō, and \"\n              \"cogn. with Gk. οὖς … L. auris (for *ausis), Avestic uši 'both ears' … All these words derive fr. I.-E. \"\n              \"base *au-, 'ear'.' The entry sits between the page markers 490 and 497 of KLN_1966.txt (the 'ear' \"\n              \"leaf), i.e. inside the 494 range Nourai cites; note that Klein, like Nourai, calls the base *au-.\")},\n    {\"ref\": \"KLN:126\", \"status\": \"partial\",\n     \"note\": (\"The Klein entry that carries this root is 'audible, adj. — ML. audibilis, fr. L. audio, audire, \"\n              \"\\\"to hear\\\", which prob. stands for *awis-d-iō, fr. I.-E. base *awei-, *au-, \\\"to perceive\\\" … Gk. \"\n              \"αἰσθάνομαι … Cp. obedient, obeisance, obey, oyer, oyez' — printed on the 126/127 leaf of KLN_1966.txt \"\n              \"(the OCR puts it just after the '126 127' page numbers, so the entry falls on p.127 of this two-volume \"\n              \"printing rather than 126). Content-wise it is exactly Nourai's claim, hence 'partial' only on the page number.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.18 (incoming/WLD/WLD_Bd1_pages.txt)\", \"stance\": \"supports\",\n     \"note\": (\"'Hierzu sehr wahrscheinlich: aus- n. „Ohr, Gehör“, kons. St. … Av. usi (n. du.) „die beiden Ohren“, \"\n              \"übertragen „Verstand, Einsicht, Sinn“ … np. hōš (*auš-) „Ohr“; … got. ausō, as. ahd. ōra, an. eyra „Ohr“' \"\n              \"— Walde–Pokorny attaches the 'ear' noun to the preceding *au- 'perceive' root, which is precisely \"\n              \"Nourai's Ôus/Au/Aus box.\")},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ous- and au-5\", \"stance\": \"supports\",\n     \"note\": (\"'ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Germanic *auzan- in Old English ēare, ear: EAR. \"\n              \"2. Suffixed form *aus-i- in Latin auris … [Pok. ōus- 785]' and 'au-5. To perceive. Compound forms \"\n              \"*aw-dh-, *awis-dh- … 1. … Latin audīre, to hear: AUDIBLE, AUDIENCE, … AUDIT, … OBEY … 2. Greek \"\n              \"aisthanesthai, to feel: AESTHETIC; ANESTHESIA. [Pok. 8. au- 78]' — the two roots and all three \"\n              \"AHD-marked branches of this page.\")},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.22 EAR\", \"stance\": \"supports\",\n     \"note\": (\"'Most of the words for \\\"ear\\\" belong to an inherited group. These and the others, so far as their \"\n              \"origin is clear, are related to words for \\\"perceive, hear\\\" … 1. IE *aus- (also *ōus-, *ous-) … beside \"\n              \"IE *au- in Skt. aviṣ \\\"evidently\\\", Grk. αἰσθάνομαι \\\"perceive\\\" … Walde-P. 1.17f.' — Buck states the \"\n              \"*ear* ~ *perceive* connection Nourai's root box assumes.\")},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. 'ausis (ousis, usis) \\\"ear; pot-handle\\\". WP I, 18'\", \"stance\": \"supports\",\n     \"note\": (\"Mann gives the same root shape ('ausis (ousis, usis)') with Av. dual uši, Arm. unkn, Gk. ous, Alb. vesh; \"\n              \"he has no *ghous-/*gheus- entry at all, so the Iranian gaoša family is absent from his 'ear' root.\")}\n  ],\n  \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n  \"id\": 1,\n  \"lang\": \"Indo-European\",\n  \"words\": \"Ghosh\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"'Ghosh' is Nourai's transcription of the root Pokorny writes ghous- (older gheus- : ghous-) 'tönen, hören' \"\n    \"— the ancestor of Sanskrit ghóṣati 'sounds, proclaims aloud, hears', ghoṣa- 'noise, shout', Avestan gaoš- \"\n    \"'to hear', gaoša- 'ear', Old Persian gauša-, NP gōš. Two things are wrong with the node as drawn. \"\n    \"(a) The page: POK:457 is Pokorny's ghreib- 'to grab' / ghrēi- 'to smear' / ghrem- area; the root is on p.454, \"\n    \"the page Nourai himself cites correctly one box lower (node #4). \"\n    \"(b) The derivation: no standard source derives ghous- from *h₂ows-/*h₂ew- 'ear, perceive'. Pokorny marks the root \"\n    \"with a question mark and the words 'Nur indoiranisch'; Walde–Pokorny I 569 the same; Cheung's Etymological \"\n    \"Dictionary of the Iranian Verb sets *gauš 'to hear, listen to' out with 'PIE — —' and the explicit remark \"\n    \"'Cognate forms outside Iranian are not attested'; Wiktionary's reconstruction stops at Proto-Indo-Iranian \"\n    \"*gʰáwšas 'noise, sound' < *gʰáwšati, with no PIE parent (Mayrhofer, EWAia I 518). Buck 4.22 lists Av. gaoša-/\"\n    \"OP gauša- as a separate item (§5, 'Walde-P. 1.569') from the *aus-/*ous- 'ear' group (§1), and Mann has no such \"\n    \"root. The initial *gʰ- of *gʰews- also cannot be got out of a vowel-initial *h₂ews-. The word 'ear' as the gloss \"\n    \"is likewise second-hand: the root means 'to sound, to hear', and 'ear' is the sense of the derived noun. \"\n    \"The only text that connects the two is the anonymous editorial layer of the online Pokorny database dump \"\n    \"('Root/lemma: ōus 2, aus-: us- \\\"ear\\\", derived from zero grade of Root/lemma ghous-'), which is not Pokorny's own \"\n    \"wording and reverses Nourai's direction anyway. Nourai's own NOTE — 'Derivation from this root is not certain' — \"\n    \"is the honest verdict, and modern scholarship takes the sceptical side; also the label should be Indo-Iranian, \"\n    \"not Indo-European. Everything BELOW this node (Avestan gaoša → Persian gōš, ni-gaoša → niyōšīdan) is sound; \"\n    \"only its attachment to the 'ear' root is not.\"),\n  \"derivation_fa\": (\n    \"«Ghosh» گونهٔ نویسهٔ نورایی از ریشه‌ای است که پوکورنی ghous- (و کهن‌تر gheus- : ghous-) «آوا دادن، شنیدن» می‌نویسد؛ \"\n    \"خاستگاه ghóṣati سنسکریت «آوا می‌دهد، می‌شنود»، ghoṣa- «بانگ»، اوستایی gaoš- «شنیدن» و gaoša- «گوش»، پارسی باستان \"\n    \"gauša- و «گوش» فارسی. دو ایراد بر این گره وارد است: نخست، ارجاع POK:457 نادرست است و مطلب در ص ۴۵۴ پوکورنی است \"\n    \"(همان صفحه‌ای که نورایی یک گره پایین‌تر درست ذکر کرده). دوم و مهم‌تر، هیچ منبع معتبری این ریشه را از *h₂ows-/*h₂ew- \"\n    \"(«گوش/دریافتن») نمی‌گیرد: پوکورنی خودِ ریشه را با علامت پرسش و عبارت «تنها هندوایرانی» آورده، والده–پوکورنی (ج۱ ص۵۶۹) \"\n    \"همین، چونگ در فرهنگ ریشه‌شناختی فعل ایرانی زیر *gauš می‌نویسد «هم‌ریشه‌ای بیرون از ایرانی به‌دست نیست» و ویکی‌واژه \"\n    \"بازسازی را در حدّ هندوایرانی آغازین *gʰáwšas نگه می‌دارد (مایرهوفر ۵۱۸). از سوی آوایی نیز gʰ آغازین را نمی‌توان از \"\n    \"*h₂ews- بی‌همخوانِ آغازین بیرون آورد. پس: پژوهش امروزی ادعای این گره را رد می‌کند و آن را ریشه‌ای مستقل و تنها \"\n    \"هندوایرانی می‌داند؛ برچسب زبانی هم باید «هندوایرانی» باشد نه «هندواروپایی». خود نورایی هم در یادداشت نوشته است \"\n    \"«این اشتقاق قطعی نیست» و همین احتیاط درست است. آنچه پایین این گره است (gaoša → گوش، ni-gaoša → نیوشیدن) درست است.\"),\n  \"sources\": [W_PII, W_H2OWS],\n  \"ref_check\": [\n    {\"ref\": \"POK:457\", \"status\": \"not_found\",\n     \"note\": (\"Pokorny p.457 (POK_02.txt leaf 113 / POK_full.txt 'Page(s): 457' and '456-457', '457-458') carries \"\n              \"ghreib- 'to grab', ghrēi- 'to smear/rub' and ghrem-1 — nothing on hearing or the ear. The root Nourai \"\n              \"means is on p.454: \" + POK454)}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed p.454 (POK_02.txt leaf 110)\", \"stance\": \"contradicts\",\n     \"note\": (\"\\\"ghous- ,tönen, hören'? Nur indoiranisch.\\\" — Pokorny gives the root its own entry, flags it as \"\n              \"Indo-Iranian only and even queries it; he does not connect it with ōus- 'Ohr' (p.785).\")},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.569 (incoming/WLD/WLD_Bd1_pages.txt)\", \"stance\": \"contradicts\",\n     \"note\": (\"'gheus- : ghous- „tönen, hören“. Ai. ghōṣati … av. gaoš- „hören“ … apers. gauša-, av. gaoša- m. „Ohr“, \"\n              \"npers. gōš „Ohr“ … Fick I⁴ 203' — a separate lemma from aus- 'Ohr' at WP I 18, with no cross-link.\")},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *gauš 'to hear, listen to', pp.115-116\", \"stance\": \"contradicts\",\n     \"note\": (\"'*PIE — — LIV: 200 | Pok.: 454', '*IE COGNATES: —', 'Cognate forms outside Iranian are not attested.' \"\n              \"Cheung therefore denies any wider IE (hence any *h₂ows-) connection.\")},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. ausis / (no ghous- lemma)\", \"stance\": \"silent\",\n     \"note\": \"Mann's 'ausis (ousis, usis) \\\"ear\\\"' lists no Iranian gaoša form, and his dictionary has no *ghous-/*gheus- entry at all.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.22 EAR §5\", \"stance\": \"contradicts\",\n     \"note\": (\"'Av. gaoša-, OPers. gauša- (NPers. gōš \\\"ear\\\") : Av. guš \\\"hear\\\", Skt. ghoṣa- \\\"noise\\\", ghoṣati \"\n              \"\\\"sounds, calls\\\". Walde-P. 1.569.' — Buck files the Iranian words under the 'sound/hear' root, \"\n              \"separately from his §1 *aus-/*ous- 'ear' group.\")},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_latin_index_pages.txt [pdf page 445] (printed 446), 'ear'\", \"stance\": \"partial\",\n     \"note\": (\"Aryanpur's 'ear' article does put 'GAOSHA, USHI (AVESTAN) … GAUSHA (OLD PERSIAN) … GHOSHA (SANSKRIT) … \"\n              \"GOSH (PAHLAVI)' in one list with 'OUS (GREEK) … AURIS, AURICULA (LATIN) … UNKN (ARMENIAN)', i.e. he \"\n              \"lumps the two families exactly as Nourai does — a Persian precedent for the chart, but not an \"\n              \"independent confirmation, since his own reference for the hearing words is 'POKORNY: 454'.\")}\n  ]\n})\n\nN.append({\n  \"id\": 2,\n  \"lang\": \"Avestan\",\n  \"words\": \"gaoša; gaoša-vare\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Both Avestan words are real. (a) gaoša- m. 'ear' is Bartholomae's headword (Altiranisches Wörterbuch col.486: \"\n    \"'p. gauša-, j. gaoša-, g. *gauša- m. \\\"Ohr\\\"', with Gathic/Younger Avestan attestations and the Old Persian \"\n    \"cognate gauša- of Bīsutūn 2.13-14 'I cut off his nose and ears'); it is the -a- stem noun of the verb gaoš- \"\n    \"'to hear' (BRT col.485), i.e. Proto-Iranian *gauša- 'ear' < Proto-Indo-Iranian *gʰáwšas 'sound, noise' < \"\n    \"*gʰáwšati 'to sound, hear'. The vowel is the regular Indo-Iranian o-grade *gʰow- > Ir. *gaw-, and Iranian *š \"\n    \"answers Sanskrit ṣ in ghóṣa- (ruki). (b) gaoša-vare is the compound Bartholomae prints as gaošāvara- m., Du. \"\n    \"'Ohrschmuck, Ohrgehänge' (col.564), attested Yt.5.121 and Yt.17.10 ('frā gaošāvara sispəmna'), analysed there as \"\n    \"'gaoša- + *ā-uara- (zum V. bar-) \\\"was ins Ohr getragen wird\\\"' — literally 'what is carried in/on the ear', \"\n    \"which is Nourai's gloss 'carried by the ear' and his cross-reference to the root Bher 1 (*bʰer- 'to carry'). \"\n    \"Nourai's 'vare' for -āvara- loses the long ā of the compound joint, a transcription looseness, not a different \"\n    \"word. The only defect of the node is the reference POK:457 (see node #1); his second reference, BQT:1858, is \"\n    \"exactly right.\"),\n  \"derivation_fa\": (\n    \"هر دو واژهٔ اوستایی واقعی‌اند. الف) gaoša- «گوش» سرواژهٔ بارتولمه است (فرهنگ ایرانی باستان ستون ۴۸۶: «پارسی باستان \"\n    \"gauša-، اوستایی gaoša- م. «گوش»»)، و اسمِ ستاک -a از فعل gaoš- «شنیدن» (ستون ۴۸۵) است؛ یعنی ایرانی باستان *gauša- \"\n    \"از هندوایرانی آغازین *gʰáwšas «بانگ، آوا». واکهٔ ao همان درجهٔ o هندوایرانی است و šِ ایرانی برابر ṣِ سنسکریت در \"\n    \"ghóṣa- (قاعدهٔ ruki). ب) gaoša-vare همان gaošāvara- بارتولمه (ستون ۵۶۴) است، «آرایهٔ گوش، گوشوار»، در یشت ۵٫۱۲۱ و \"\n    \"۱۷٫۱۰ گواهی‌شده و تحلیل‌شده به «gaoša- + *ā-vara- از ریشهٔ bar- (بردن): آنچه در گوش برده می‌شود» — درست همان معنای \"\n    \"«حمل‌شده با گوش» و همان اشارهٔ نورایی به ریشهٔ Bher 1. صورت «vare» به جای -āvara- تنها سهل‌انگاری در نویسه‌گردانی است. \"\n    \"تنها اشکال گره، ارجاع POK:457 است (رک: گرهٔ ۱)؛ ارجاع دوم، BQT:1858، کاملاً درست است.\"),\n  \"sources\": [W_PII, W_GUSH, W_GUSHV],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1858\", \"status\": \"supports\", \"note\": BQT1858},\n    {\"ref\": \"POK:457\", \"status\": \"not_found\",\n     \"note\": (\"Wrong page again: p.457 is ghreib-/ghrēi-/ghrem-. The Avestan material Nourai wants is on Pokorny \"\n              \"p.454, which does list 'av. gaoša- m. \\\"Ohr\\\"' and 'npers. gōš'. \" + POK454)}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch coll. 485-486 and 564 (BRT.txt leaf 292)\", \"stance\": \"supports\",\n     \"note\": (\"col.485 'j., g. gaoš- V. \\\"hören\\\" … ai. ghōṣati \\\"es hallt wieder\\\", mp. (Pü.) nigōšītan, np. niyōšīdan'; \"\n              \"col.486 'p. gauša-, j. gaoša-, g. *gauša- m. \\\"Ohr\\\"'; col.564 'j. gaošāvara- m., Du. \\\"Ohrschmuck, \"\n              \"Ohrgehänge\\\" … Komp.: gaoša- + *ā-uara- (zum V. bar-) \\\"was ins Ohr getragen wird\\\". — Vgl. np. gōšvār \"\n              \"(aus *gauša-bāra-) \\\"Ohrgehänge\\\"'.\")},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *gauš, p.115\", \"stance\": \"supports\",\n     \"note\": (\"'*AVESTAN: guš- \\\"to hear, listen to\\\" … Partic.: pres. caus. YAv. gušaiiat° (<< *gaoš°, Yt 13.16)' \"\n              \"— the verb behind the noun; the Old Persian noun appears in his quotation 'gauša uta hazānam frājanam'.\")},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.22 EAR §5\", \"stance\": \"supports\",\n     \"note\": \"'Av. gaoša-, OPers. gauša- (NPers. gōš \\\"ear\\\") : Av. guš \\\"hear\\\", Skt. ghoṣa- \\\"noise\\\".'\"},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 943, p.210 (HRN.txt leaf 231)\", \"stance\": \"supports\",\n     \"note\": (\"'gōš \\\"Ohr\\\". ap. gauša- \\\"Ohr\\\"; aw. gaoša- \\\"Ohr\\\"; phlv. gōš; ai. ghoṣa- \\\"Lärm, Getön\\\" … \"\n              \"np. gōšvār, gōšvāre \\\"Ohrgehänge\\\": aw. frā-gaošāvara-, …; phlv. gōšvār.'\")}\n  ]\n})\n\nN.append({\n  \"id\": 3,\n  \"lang\": \"Persian\",\n  \"words\": \"gŭš «گوش»; gŭšvâreh «گوشواره»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"گوش gōš/gūš 'ear' is the direct continuation of Old Iranian *gauša-: Old Persian gauša- (Bīsutūn 2.13f.) > \"\n    \"Middle Persian gōš (Book Pahlavi/Manichaean gwš) > NP گوش, with the regular monophthongisation of Old Iranian \"\n    \"au > MP ō (as in *gauš- 'ear', *rauča- > rōz) and the classical value gōš still shown by Dari [ɡoːʃ] beside \"\n    \"Iranian [ɡuːʃ]. Avestan gaoša-, which Nourai draws as the parent, is strictly the sister form: the ancestor of \"\n    \"the New Persian word is the Old Persian/Middle Persian line (Wiktionary: 'Inherited from Middle Persian gōš, \"\n    \"from Old Persian gauša- \\\"ear\\\", from Proto-Iranian *gáwšah'), and the book's habit of putting Avestan at the \"\n    \"Old Iranian node is a simplification, not an error of substance. گوشواره gōšvāre 'earring' continues MP gōšwār \"\n    \"(Horn no.943 'phlv. gōšvār'), from *gauša-bāra- 'ear-carrier' (Bartholomae, s.v. gaošāvara-: NP gōšvār 'aus \"\n    \"*gauša-bāra-'), i.e. گوش + وار from the root bar-/bʰer- 'to carry', with the New Persian -a/-e suffix added to \"\n    \"the older gōšvār; Mo'in's footnote in Borhān-e Qāṭeʿ analyses it exactly so ('از: گوش + وار (اوستایی vara از بر \"\n    \"(بردن)؛ آنچه گوش می‌برد و حمل می‌کند؛ آویزهٔ گوش'). Wiktionary's synchronic analysis 'گوش + ـواره' is the same \"\n    \"formation seen from the New Persian side. The node carries no reference of its own; nothing in it is doubtful.\"),\n  \"derivation_fa\": (\n    \"«گوش» بازماندهٔ مستقیم ایرانی باستان *gauša- است: پارسی باستان gauša- (بیستون ۲٫۱۳) > فارسی میانه gōš > فارسی نو \"\n    \"«گوش»؛ دو‌واکهٔ au ایرانی باستان در فارسی میانه به ō ساده شده است (چنان‌که *rauča- > rōz)، و تلفظ کلاسیک gōš هنوز \"\n    \"در دری [ɡoːʃ] برجاست در برابر [ɡuːʃ] ایران. اوستایی gaoša- که نورایی آن را «پدر» گرفته، به‌دقت صورت خواهر است نه \"\n    \"نیای مستقیم؛ نیای فارسی نو خطِّ پارسی باستان → فارسی میانه است (ویکی‌واژه). «گوشواره» ادامهٔ gōšwār فارسی میانه است \"\n    \"(هرن، شمارهٔ ۹۴۳: «پهلوی gōšvār») از *gauša-bāra- «برندهٔ گوش»؛ بارتولمه ذیل gaošāvara- می‌نویسد فارسی نو gōšvār از \"\n    \"*gauša-bāra- است، یعنی «گوش + وار» از ریشهٔ bar-/*bʰer- «بردن»، و پسوند ـه فارسی نو بر gōšvār کهن‌تر افزوده شده است. \"\n    \"حاشیهٔ معین بر برهان قاطع همین را می‌گوید: «از: گوش + وار (اوستایی vara از بر (بردن)؛ آنچه گوش می‌برد و حمل می‌کند؛ \"\n    \"آویزهٔ گوش». ادعای نورایی درست است.\"),\n  \"sources\": [W_GUSH, W_GUSHV],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": (\"Nourai cites nothing here (the box inherits BQT:1858 from its parent). Checked instead against \"\n              \"Mo'in's footnotes in Borhān-e Qāṭeʿ (vol.3 pdf 652 = printed 1858, and pdf 655 = printed 1861 on \"\n              \"گوشوار/گوشواره), Horn no.943, MacKenzie, Mo'in's Farhang and Wiktionary — all agree.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol.3 pdf page 655 (= printed 1861), Mo'in's footnote to گوشوار/گوشواره\", \"stance\": \"supports\",\n     \"note\": (\"«گوشوار و گوشواره … پهلوی gōšwār، … اوستایی …، کردی …، از گوش (ه.م.) + وار (اوستایی vara از بر (بردن)؛ \"\n              \"آنچه گوش می‌برد و حمل می‌کند؛ آویزهٔ گوش، زینتی که در گوش آویزند)» \"\n              \"(grep 'گوشوار' in incoming/BQT/BQT_v3_pages.txt, block [pdf page 655]).\")},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 943, p.210\", \"stance\": \"supports\",\n     \"note\": \"'gōš \\\"Ohr\\\". ap. gauša-; aw. gaoša-; phlv. gōš … np. gōšvār, gōšvāre \\\"Ohrgehänge\\\" … phlv. gōšvār.'\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, 2-vol Adena abridgement (MON_part2.txt), s.v. گوشوار\", \"stance\": \"supports\",\n     \"note\": (\"«گوشوار: (قد. gōšwār) [= گوشواره] (امر.) زینتی ساخته از فلزات قیمتی و احجار کریمه یا از بلور که در گوش \"\n              \"آویزند» — Mo'in marks it a native (قد. = قدیم/Middle-Persian-derived) word and equates it with گوشواره.\")},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt, g- and n- sections)\", \"stance\": \"partial\",\n     \"note\": (\"The OCR of the g- leaf is too damaged to quote gōš itself, but MacKenzie's n- page 60 line \"\n              \"'niyē(x)šīdan, niyē(x)š- [n(y)whš-ytn' | M nywš-, N niyōšīdan] hear' presupposes the same MP gōš/gōš- \"\n              \"stem; the Pahlavi form gōš is confirmed independently by Horn no.943 and Mo'in's footnote (BQT:1858).\")}\n  ]\n})\n\nN.append({\n  \"id\": 4,\n  \"lang\": \"Avestan\",\n  \"words\": \"ni-gaoša\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The formation is right and standard, but the language label overstates the evidence. What is attested in Avestan \"\n    \"is the simple verb gaoš- / guš- 'to hear' (Bartholomae col.485; Cheung: OAv. gušta, gūšatā, gūšahuua, gūšō.dūm, \"\n    \"YAv. caus. gušaiiat°) and prefixed forms with apa- (apa-gaošayeiti) — not *ni-gaoša-. The prefixed stem *ni-gauš- \"\n    \"'to listen (in)' is a reconstruction on the strength of the whole Iranian family: MP nigōšītan / niyō(x)šītan, \"\n    \"Parthian ngwš-, Sogdian nyws- 'to hear, listen', Balochi nigōšag/niyōšay, Pashto nyewatǝl 'to listen, obey', \"\n    \"NP niyōšīdan. Horn writes it exactly as Nourai does but with an asterisk — 'aw. *ni- + √gaoš-, vergl. \"\n    \"apa-gaošayeiti' (no.1070) — and Hübschmann, endorsing him, puts it at the Iranian, not the Avestan, stage: \"\n    \"'die auf iran. *ni-gauš zurückgehen' (Persische Studien p.104, ad 1070). Wiktionary likewise: 'from Proto-Iranian \"\n    \"*ni- + *gáwšati'. The prefix is the inherited *ni- 'down, in' (Nourai's cross-reference to Nî 1 is correct), and \"\n    \"the sense 'listen' = 'apply the ear down/into' is the usual Iranian idiom. Nourai's reference POK:454 is the \"\n    \"right page and it prints the very outcome: 'npers. niyōšīdan \\\"hören, horchen, lauschen\\\"'. So: derivation \"\n    \"accepted, but the node should read Old Iranian/Proto-Iranian *ni-gauš- (or Avestan *ni-gaoš- with an asterisk).\"),\n  \"derivation_fa\": (\n    \"ساخت واژه درست است، اما برچسب «اوستایی» بیش از گواهی موجود می‌گوید. در اوستا فعل ساده gaoš-/guš- «شنیدن» گواهی \"\n    \"شده است (بارتولمه ستون ۴۸۵؛ چونگ: gušta، gūšatā، gūšahuua، gūšō.dūm و سببیِ gušaiiat°) و صورت پیشوندی با apa- \"\n    \"(apa-gaošayeiti)، اما *ni-gaoša- خود گواهی نشده است. ستاکِ پیشوندی *ni-gauš- «گوش فرادادن» بازسازی‌ای است بر پایهٔ \"\n    \"کل خانوادهٔ ایرانی: فارسی میانه nigōšītan/niyōxšītan، پارتی ngwš-، سغدی nyws-، بلوچی nigōšag، پشتو nyewatǝl، و \"\n    \"فارسی نو نیوشیدن. هرن هم آن را همانند نورایی می‌نویسد ولی با ستاره: «اوستایی *ni- + √gaoš-، قس apa-gaošayeiti» \"\n    \"(شمارهٔ ۱۰۷۰)، و هوبشمان با تأیید او آن را به مرحلهٔ ایرانی می‌برد: «که به ایرانی *ni-gauš بازمی‌گردند» (پژوهش‌های \"\n    \"فارسی ص ۱۰۴). ویکی‌واژه نیز «ایرانی آغازین *ni- + *gáwšati». پیشوند همان *ni- «فرو، در» است (اشارهٔ نورایی به Nî 1 \"\n    \"درست است) و تحول معنایی «گوش را فرو/در بردن ← گوش دادن» اصطلاح رایج ایرانی است. ارجاع POK:454 دقیقاً درست است. \"\n    \"پس: با احتیاط پذیرفتنی است؛ تنها باید نوشت «ایرانی باستان *ni-gauš-» یا «اوستایی *ni-gaoš-» با ستاره.\"),\n  \"sources\": [W_NIY, W_PII],\n  \"ref_check\": [\n    {\"ref\": \"POK:454\", \"status\": \"supports\", \"note\": POK454 + \" Pokorny's page prints the Persian outcome (niyōšīdan) under this root, which is what the arrow claims.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 485 s.v. gaoš-\", \"stance\": \"partial\",\n     \"note\": (\"Bartholomae's entry lists only the simple verb and its causative ('j., g. gaoš- V. \\\"hören\\\". Praes. 1 \"\n              \"guš-, 3 gūšā-, 30 (Kaus.) gūšaya-'), with the Pahlavi/New Persian continuations 'mp. (Pü.) nigōšītan, \"\n              \"np. niyōšīdan' appended — i.e. he documents the ni- form for Middle Persian, not for Avestan.\")},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.104, ad no.1070\", \"stance\": \"supports\",\n     \"note\": (\"'Ich halte Horn's Ausführungen für richtig mit Rücksicht auf bal. niyōšay \\\"hören, horchen, lauschen\\\" \"\n              \"und afgh. nyvatǝl … die auf iran. *ni-gauš zurückgehen. Vgl. auch bal. gōšay \\\"hören\\\", osset. ɣosun, \"\n              \"qusin \\\"hören\\\".'\")},\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 5902\", \"stance\": \"supports\",\n     \"note\": (\"'ny'ws- … niyōš (nyws-, nyyws) < *ni-gauša-; Parth. ngwš-, MP nyws-' — Gharib reconstructs the same \"\n              \"prefixed Old Iranian stem *ni-gauša- for Sogdian.\")},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_latin_index_pages.txt [pdf page 511] (printed 512)\", \"stance\": \"partial\",\n     \"note\": (\"Aryanpur's 'hear/listen' article prints 'AVESTAN: GUSHAYAT-, NI-GAOSH … PAHLAVI: NIGHOSHITAN, \"\n              \"NIOXSHIDHAN … BALUCHI: NIGOSHAG … REFERENCES POKORNY: 454, MACKENZIE (HEAR) 117' — the same \"\n              \"'Avestan ni-gaoš' label Nourai uses, i.e. his likely immediate model, but with no asterisk either.\")}\n  ]\n})\n\nN.append({\n  \"id\": 5,\n  \"lang\": \"Persian\",\n  \"words\": \"nîušîdan «نیوشیدن ( نیوشه )»; nağŭšîdan «نغوشیدن (نغوشه)»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"نیوشیدن niyōšīdan 'to listen' is the New Persian continuation of Middle Persian niyō(x)šīdan (Book Pahlavi \"\n    \"nywhšytn / ndwhšytn, Manichaean MP nywš-), from *ni-gauš- (node #4): Old Iranian intervocalic *g was lost after \"\n    \"the prefix (*ni-gauš- > MP niyōš-, the y being a glide filling the hiatus), while the older, unlenited variant \"\n    \"survives in Book Pahlavi nigōšītan and Balochi nigōšag — and precisely that variant is Nourai's second word, \"\n    \"نغوشیدن nağōšīdan (present stem نغوشه), the doublet with -غ- preserved (compare نغوشا/نغوشاک below). \"\n    \"MacKenzie prints 'niyē(x)šīdan, niyē(x)š- [n(y)whš-ytn | M nywš-, N niyōšīdan] hear'; Nyberg 'niyōšītan \"\n    \"[nywkšytn'] to listen … MPrth pres. ngwš-, MPrs nywš-; Paz. nyōxšidan, NP niyōšīdan; < ni + Av. (485 sq.) \"\n    \"gaoš-'; Abolghasemi (Feʿl-hā-ye Fārsi-ye Dari p.85) 'نیوشیدن، نیوشید < فارسی میانه niyōš- … نیوش < فارسی میانه \"\n    \"niyōš < ایرانی باستان *ni-gauša-'. The infinitive is built on the present stem نیوش with the New Persian \"\n    \"denominative-infinitive suffix -īdan (Mo'in: 'از: نیوش + یدن (پسوند مصدری)'), and the past stem نیوشید is, as \"\n    \"Abolghasemi notes, a secondary Persian formation. Both of Nourai's parenthesised present stems (نیوشه، نغوشه) \"\n    \"are the forms the Persian lexica list — Borhān-e Qāṭeʿ has نیوشه 'گوش فرا داشتن به سخن دیگران' and نغوشه with the \"\n    \"same sense. The Ferdowsi line in the box, 'فرستاده را گفت نیکو نیوش / بگو آنچه بشنیدی ای تیزهوش', is genuine and \"\n    \"is quoted by Mo'in on the very page Nourai cites.\"),\n  \"derivation_fa\": (\n    \"«نیوشیدن» بازماندهٔ فارسی میانهٔ niyō(x)šīdan است (پهلوی کتابی nywhšytn، فارسی میانهٔ مانوی nywš-) از *ni-gauš- \"\n    \"(گرهٔ ۴): gِ ایرانی باستان پس از پیشوند در میان دو واکه ساقط شده و yِ میانجی جای آن را گرفته است (*ni-gauš- > \"\n    \"niyōš-)، در حالی که صورت کهن‌ترِ نرم‌نشده در پهلوی nigōšītan و بلوچی nigōšag برجاست — و همین گونه است واژهٔ دوم \"\n    \"نورایی، «نغوشیدن» (ستاک حال «نغوشه»)، دوگانه‌ای که غ در آن مانده است (قس نغوشا/نغوشاک در گره‌های بعد). مکنزی: \"\n    \"«niyē(x)šīdan … N niyōšīdan، شنیدن»؛ نیبرگ: «niyōšītan … پارتی ngwš-، فارسی میانه nywš-؛ پازند nyōxšidan، فارسی نو \"\n    \"niyōšīdan؛ < ni + اوستایی gaoš- (بارتولمه ۴۸۵)»؛ ابوالقاسمی (فعل‌های فارسی دری ص ۸۵): «نیوشیدن، نیوشید < فارسی \"\n    \"میانه niyōš- … نیوش < ایرانی باستان *ni-gauša-». مصدر بر ستاک حال «نیوش» با پسوند مصدری ـیدن ساخته شده (حاشیهٔ \"\n    \"معین: «از: نیوش + یدن») و ستاک گذشتهٔ «نیوشید» ساختهٔ ثانوی فارسی است. بیت فردوسی در جعبه («فرستاده را گفت نیکو \"\n    \"نیوش…») اصیل است و معین آن را در همان صفحه‌ای که نورایی ارجاع داده آورده است. ادعای نورایی درست است.\"),\n  \"sources\": [W_NIY],\n  \"ref_check\": [\n    {\"ref\": \"BQT:2239\", \"status\": \"supports\", \"note\": BQT2239},\n    {\"ref\": \"MON:4746\", \"status\": \"not_checked\", \"note\": MON_NC + \" The abridgement's entry is quoted under 'consulted'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.60 (PHD.txt, n- section)\", \"stance\": \"supports\",\n     \"note\": \"'niyē(x)šīdan, niyē(x)š- [n(y)whš-ytn | M nywš-, N niyōšīdan] hear. ~išn: hearing.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. niyōšītan (NYB_vol2_glossary.txt line 2779)\", \"stance\": \"supports\",\n     \"note\": (\"'niyōšītan [nywkšytn'] to listen 90%. — Ps. pres. nywhšyt = niyōxšēt; MPrth pres. ngwš-, MPrs nywš-; \"\n              \"Paz. nyōxšidan, NP niyōšīdan; < ni + Av. (485 sq.) gaoš-.'\")},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *gauš, pp.115-116\", \"stance\": \"supports\",\n     \"note\": (\"'*MIDDLE PERSIAN: MMP gws \\\"ear\\\" || (+ *ni-) MMP nyws-, BMP n(y)dw(h)s- /niyōs-/ \\\"to hear\\\" … \"\n              \"Inf.: BMP nywhšytn /niyōšīdan/'; '*NWIR: NP gōšīdan/gōš- \\\"to hear, listen\\\"'.\")},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 1070, p.239 (HRN.txt leaf 260)\", \"stance\": \"supports\",\n     \"note\": (\"'niyōšīdan \\\"hören, horchen\\\" … aw. *ni- + √gaoš-, vergl. apa-gaošayeiti; phlv. n(i)yōšītan, \"\n              \"n(i)yōxšītan bezw. n(i)gōšītan \\\"hören\\\"; ai. √ghōṣ-, ghōṣati mit ā \\\"hören, horchen auf\\\". \"\n              \"bal. nigōšag, niyōšay.' — Horn's phlv. n(i)gōšītan is the source of Nourai's نغوشیدن variant.\")},\n    {\"src\": \"FFD\", \"where\": \"Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari, [pdf page 85] (incoming/FFD/FFD_pages.txt)\", \"stance\": \"supports\",\n     \"note\": (\"«نیوشیدن نیوشید < فارسی میانه niyōš-… نیوش < فارسی میانه niyōš < ایرانی باستان *ni-gauša-. ni پیشوند \"\n              \"فعلی است. ریشهٔ gauš به معنی «گوش کردن» است. «گوش» هم از ریشهٔ gauš آمده است.» — the same author as \"\n              \"Nourai's ETM reference, deriving both گوش and نیوشیدن from *gauš, exactly as the chart does.\")}\n  ]\n})\n\nN.append({\n  \"id\": 6,\n  \"lang\": \"Pahlavi\",\n  \"words\": \"ni-ğôšâg\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Middle Persian niyōšāg / nigōšāg 'hearer, listener' is the agent noun of the verb of node #5: present stem \"\n    \"niyōš- (< *ni-gauš-) + the productive Middle Persian agent/adjective suffix -āg (< Old Iranian *-āka-), the same \"\n    \"formation as MP nigērāg, dānāg. It is above all a Manichaean technical term: in the Manichaean Middle Persian \"\n    \"and Parthian texts nywš'g (niyōšāg) is the name of the lay class, the 'Auditor/catechumen', the lowest of the \"\n    \"five grades of the Manichaean community, rendering Syriac/Aramaic šammāʿē and Arabic سماعون 'hearers'. Nourai's \"\n    \"gloss 'one who listens, referred to the followers of the Mânî religion' is therefore exact; his added remark \"\n    \"'It was later used to mean a \\\"non-Moslem\\\"' is true but belongs one step lower, to the New Persian word of node \"\n    \"#7 — Borhān-e Qāṭeʿ glosses نغوشا as 'گبر و جهود و آتش‌پرست', a post-Islamic Persian extension, not a Pahlavi \"\n    \"sense. His spelling with -ğ- (nigōšāg rather than niyōšāg) is the unlenited Book-Pahlavi variant, the same one \"\n    \"Horn records as phlv. n(i)gōšītan and Mo'in prints as nigōšāg. The reference ETM:71 (Abolghasemi) could not be \"\n    \"read (no digital copy exists), but three independent witnesses confirm the form and the meaning.\"),\n  \"derivation_fa\": (\n    \"فارسی میانهٔ niyōšāg/nigōšāg «شنونده» اسم فاعل همان فعل گرهٔ ۵ است: ستاک حال niyōš- (< *ni-gauš-) + پسوند فاعلی/صفتی \"\n    \"زایای فارسی میانه ـāg (از ایرانی باستان *-āka-)، همان ساخت nigērāg و dānāg. این واژه پیش از هر چیز اصطلاحی مانوی \"\n    \"است: در متن‌های فارسی میانهٔ مانوی و پارتی nywš'g نام طبقهٔ عامیانِ کیش، یعنی «شنونده/سَماع»، پایین‌ترین (پنجمین) \"\n    \"طبقهٔ جامعهٔ مانوی است و برابر «سماعون» عربی و šammāʿē سریانی است. پس معنایی که نورایی داده دقیق است؛ اما جملهٔ \"\n    \"«بعدها به معنی غیرمسلمان به کار رفت» به یک پلّه پایین‌تر، یعنی واژهٔ فارسی نوِ گرهٔ ۷، مربوط است (برهان قاطع «نغوشا» \"\n    \"را «گبر و جهود و آتش‌پرست» معنی کرده که تحولی پس از اسلام است، نه معنایی پهلوی). نوشتن آن با غ (nigōšāg) همان گونهٔ \"\n    \"نرم‌نشدهٔ پهلوی کتابی است که هرن نیز n(i)gōšītan آورده است. ارجاع ETM:71 قابل دیدن نبود، اما سه گواه مستقل صورت و \"\n    \"معنا را تأیید می‌کنند.\"),\n  \"sources\": [W_NIY],\n  \"ref_check\": [\n    {\"ref\": \"ETM:71\", \"status\": \"not_checked\", \"note\": ETM_NC}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, 2-vol abridgement (MON_part2.txt) s.v. نغوشاک\", \"stance\": \"supports\",\n     \"note\": (\"«نغوشاک: (قد. nigōšāg) [= نغوشا] (ص.) شنونده، مستمع، سماع و آن به افراد پایین‌ترین (پنجمین) طبقه از \"\n              \"طبقات مانویان اطلاق می‌شده … ترجمهٔ کلمهٔ «صانتئون» و «صاشن» همه جا نغوشاکان آمده است (مانی و دین او، \"\n              \"تقی‌زاده ص ۸۰)» — Mo'in gives the Middle Persian form and the Manichaean 'hearer' sense.\")},\n    {\"src\": \"BQT\", \"where\": \"vol.4 pdf page 235 (≈ printed 2154), Mo'in's footnote to نغوشا\", \"stance\": \"supports\",\n     \"note\": (\"«(< نیوشیدن … قس: nigōšāg (؟) … تاوادیا ص ۱۹۳) بمعنی شنونده و مستمع و همین کلمه است که عرب آن را به \"\n              \"«سماعون» ترجمه کرده است، و آن پایین‌ترین (پنجمین) طبقه از طبقات مانویان بود» \"\n              \"(grep 'نغوشا' in incoming/BQT/BQT_v4_pages.txt).\")},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, n- section pp.59-61\", \"stance\": \"silent\",\n     \"note\": (\"MacKenzie's Zoroastrian Book-Pahlavi glossary has the verb ('niyē(x)šīdan … hear') but no entry \"\n              \"niyōšāg — expected, since the noun is a Manichaean term (Boyce's Manichaean word-list / DMMPP \"\n              \"nywš'g), outside his corpus. Absence here is not evidence against the form.\")},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *gauš, pp.115-116\", \"stance\": \"supports\",\n     \"note\": \"Cheung documents the Manichaean MP and Parthian ni- stems ('MMP nyws-', 'Parth. (+ *ni-) ngws- \\\"to hear\\\"') on which the agent noun nywš'g is built.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7,\n  \"lang\": \"Persian\",\n  \"words\": \"naghŭšâ «نغوشا ( نغوشاک )»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"New Persian نغوشاک nağōšāk / نغوشا nağōšā is the direct inheritance of Middle Persian nigōšāg (node #6), with \"\n    \"the regular MP -g > NP -k/-∅ in this word's transmission (نغوشاک beside apocopated نغوشا, exactly the pair \"\n    \"Borhān and Mo'in list) and with the unlenited -غ- of the Book-Pahlavi variant instead of the -ی- of نیوشیدن. \"\n    \"Its historical meaning is 'Manichaean lay hearer, catechumen', and by pars pro toto it came to name Manichaeans \"\n    \"in general: Ḥudūd al-ʿĀlam (372 AH) writes 'اندروی (سمرقند) جایگاه مانویانست و ایشان را نغوشاک خوانند'. Nourai's \"\n    \"gloss 'The followers of Mânî religion' is thus right for the classical language. His Daqīqī couplet ('تأویل کرد \"\n    \"موبد از مذهب نغوشا …') is genuine, and it is worth adding what Mo'in observes about it: 'دقیقی در مفهوم اصلی آن \"\n    \"اشتباه کرده' — Daqīqī, and after him the Persian lexicographers, no longer understood the Manichaean sense, so \"\n    \"that Borhān-e Qāṭeʿ ends up defining نغوشا as 'گبر و جهود و آتش‌پرست' (Zoroastrian, Jew, fire-worshipper), i.e. \"\n    \"the 'non-Moslem' sense Nourai mentions in the Pahlavi box above. Mo'in also warns against the folk etymology \"\n    \"that connected نغوشا with مغوش/مگوش 'magus' (held by Sadeq Hedayat), which is wrong: the word is the niyōš- \"\n    \"'hear' derivative. Both of Nourai's references are inaccessible in their cited editions (ETM has no digital \"\n    \"copy; MON's 6-volume pagination is not online), but the entry itself is verified from Borhān-e Qāṭeʿ with \"\n    \"Mo'in's footnotes and from the Mo'in abridgement.\"),\n  \"derivation_fa\": (\n    \"«نغوشاک/نغوشا» بازماندهٔ مستقیم فارسی میانهٔ nigōšāg (گرهٔ ۶) است؛ ـگ پایانی فارسی میانه در این واژه به ـک بدل شده \"\n    \"(نغوشاک) و صورت کوتاه‌شدهٔ نغوشا کنار آن مانده است — همان دو صورتی که برهان و معین آورده‌اند — و غ نرم‌نشدهٔ گونهٔ \"\n    \"پهلوی کتابی در آن حفظ شده است، در برابر یِ «نیوشیدن». معنای تاریخی آن «شنوندهٔ مانوی، عامِ کیش مانی» است و از راه \"\n    \"اطلاق جزء بر کل به همهٔ مانویان گفته شده است: حدودالعالم (۳۷۲ ق) می‌نویسد «اندروی (سمرقند) جایگاه مانویانست و \"\n    \"ایشان را نغوشاک خوانند». پس معنای نورایی برای زبان کلاسیک درست است. بیت دقیقی اصیل است، اما چنان‌که معین یادآور \"\n    \"می‌شود «دقیقی در مفهوم اصلی آن اشتباه کرده»؛ از این رو برهان قاطع «نغوشا» را «گبر و جهود و آتش‌پرست» معنی کرده — \"\n    \"همان معنای «غیرمسلمان» که نورایی در جعبهٔ پهلوی آورده است. معین نیز ریشه‌شناسی عامیانه‌ای را که نغوشا را با \"\n    \"«مغوش/مگوش» هم‌ریشه می‌دانست (عقیدهٔ صادق هدایت) نادرست می‌شمارد. هر دو ارجاع نورایی در چاپ‌های ذکرشده دست‌نیافتنی \"\n    \"بود، اما مدخل از برهان قاطع با حواشی معین و از فرهنگ معین راستی‌آزمایی شد.\"),\n  \"sources\": [W_NIY],\n  \"ref_check\": [\n    {\"ref\": \"ETM:71\", \"status\": \"not_checked\", \"note\": ETM_NC},\n    {\"ref\": \"MON:4746\", \"status\": \"not_checked\", \"note\": MON_NC}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol.4, headword نغوشا and Mo'in's footnote, pdf pages 235-236 (≈ printed 2154-2155)\", \"stance\": \"supports\",\n     \"note\": (\"Text: «نغوشا … بمعنی نغوشاک است که گبر و جهود و آتش‌پرست باشد»; Mo'in's footnote: «… بمعنی شنونده و \"\n              \"مستمع و همین کلمه است که عرب آن را به «سماعون» ترجمه کرده است، و آن پایین‌ترین (پنجمین) طبقه از طبقات \"\n              \"مانویان بود … و من باب اطلاق جزء بکل به همهٔ مانویان اطلاق میشده: «اندروی (سمرقند) جایگاه مانویانست و \"\n              \"ایشان را نغوشاک خوانند» «حدودالعالم … ص ۹۹»؛ دقیقی در مفهوم اصلی آن اشتباه کرده».\")},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, 2-vol abridgement (MON_part2.txt) s.v. نغوشاک and نیوشا\", \"stance\": \"supports\",\n     \"note\": (\"«نغوشاک … [= نغوشا] شنونده، مستمع، سماع … پیرو آیین مانی، مانوی. (به خطا) … ظاهراً نغوشاک و نغوشا را \"\n              \"به خطا هم‌ریشهٔ مغوش-مگوش دانسته‌اند چنانکه مرحوم صادق هدایت بر این عقیده بوده»; and «نیوشا: [= نغوشاک] \"\n              \"شنوا، شنونده» — Mo'in equates the two and rejects the مغوش folk etymology.\")},\n    {\"src\": \"FSF\", \"where\": \"Noushin, Vāzhe-nāmak (FSF.txt) / Borhān's own quotations\", \"stance\": \"silent\",\n     \"note\": (\"Grepped FSF.txt for نغوشا/نغوشاک with no hit (the word is not in the Shāhnāme glossary); the Persian \"\n              \"attestations come from Rudaki, Daqīqī, Ḥudūd al-ʿĀlam and Sūzanī, all quoted in Mo'in's footnote above.\")}\n  ]\n})\n\nN.append({\n  \"id\": 8,\n  \"lang\": \"Germanic\",\n  \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"An empty pass-through box: the Germanic stage between the root and English ear. Its content is Watkins's \"\n    \"'ous-. … 1. Suffixed form *ous-en- in Germanic *auzan-' (whence, by Germanic *z from *s and West Germanic \"\n    \"rhotacism, Old English ēare); Pokorny 785 lists the same series 'Gothic auso n. \\\"ear\\\" (Germanic *ausan-), \"\n    \"with gramm. variation (*auzan-): Old Icelandic eyra, Old English eare, Old Frisian are, Old Saxon, Old High \"\n    \"German ora'. The reference 'AHD' with no page is Nourai's usual way of citing the Indo-European appendix, and \"\n    \"it is correct here.\"),\n  \"derivation_fa\": (\n    \"جعبهٔ خالیِ گذرگاه: مرحلهٔ ژرمنی میان ریشه و ear انگلیسی. محتوای آن همان مطلب واتکینز است: «*ous-en- در ژرمنی \"\n    \"*auzan-» که با تبدیل *s به *z (قانون زیورس/تناوب دستوری) و rhotacism ژرمنی غربی به ēare انگلیسی کهن رسیده است؛ \"\n    \"پوکورنی (ص ۷۸۵) همین رشته را می‌آورد: «گوتی ausō «گوش» (ژرمنی *ausan-)، با تناوب دستوری *auzan-: ایسلندی کهن \"\n    \"eyra، انگلیسی کهن eare، فریزی کهن are، ساکسونی کهن و آلمانی علیای کهن ora». ارجاع «AHD» بی‌شمارهٔ صفحه شیوهٔ \"\n    \"همیشگی نورایی برای پیوست ریشه‌های هندواروپایی است و اینجا درست است.\"),\n  \"sources\": [E_EAR, W_H2OWS],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": (\"Watkins 1985 s.v. ous-: '1. Suffixed form *ous-en- in Germanic *auzan- in Old English ēare, ear: EAR' \"\n              \"(AHD_watkins1985.txt).\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed p.785 (ōus- 2, aus-, us-)\", \"stance\": \"supports\",\n     \"note\": \"'Gothic auso n. \\\"ear\\\" (Germanic *ausan-); with gramm. variation (*auzan-): Old Icelandic eyra, Old English eare, Old Frisian are, Old Saxon Old High German ora n. \\\"ear\\\".'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. ear (KLN_1966.txt, 'ear' leaf, pp. 49x)\", \"stance\": \"supports\",\n     \"note\": \"'ME. ere, fr. OE. eare, rel. to ON. eyra, Swed. öra, Dan. øre, OS., ODu., OHG. ora, OFris. are, Du. oor, MHG. ore, G. Ohr, Goth. ausō.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 9,\n  \"lang\": \"English\",\n  \"words\": \"ear\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"English ear 'organ of hearing' < Middle English ere < Old English ēare < Proto-Germanic *auzōn- < PIE *h₂ows-, \"\n    \"the inherited word throughout Germanic (Etymonline: 'organ of hearing, Old English eare \\\"ear\\\", from \"\n    \"Proto-Germanic *auzon, from PIE *ous- \\\"ear\\\"', with the IE cognates Greek ous, Latin auris, Lith. ausis, OCS \"\n    \"ucho, OIr. au, Avestan uši 'the two ears'). It is to be kept apart from the homonym ear 'spike of corn' \"\n    \"(< PGmc *ahaz, PIE *h₂eḱ- 'sharp'), which is not what the chart means. Nothing to query.\"),\n  \"derivation_fa\": (\n    \"ear انگلیسی «اندام شنوایی» از انگلیسی میانه ere، از انگلیسی کهن ēare، از ژرمنی آغازین *auzōn-، از هندواروپایی \"\n    \"آغازین *h₂ows- است و در سراسر شاخهٔ ژرمنی واژهٔ موروثی همین است (اتیمانلاین، با هم‌ریشه‌های ous یونانی، auris \"\n    \"لاتین، ausis لیتوانیایی، ucho اسلاوی کلیسایی کهن و uši اوستایی «دو گوش»). باید آن را از هم‌آواش ear «خوشهٔ \"\n    \"غله» (از ژرمنی *ahaz، ریشهٔ *h₂eḱ- «تیز») جدا داشت که مقصود نمودار نیست. ادعای نورایی درست است.\"),\n  \"sources\": [E_EAR, W_H2OWS],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"No reference given in the box (it inherits AHD from the Germanic node); checked against Etymonline, Klein s.v. 'ear' and Watkins s.v. ous-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. ear, n., the organ of hearing\", \"stance\": \"supports\",\n     \"note\": \"'All these words derive fr. I.-E. base *au-, \\\"ear\\\". Cp. aural, auricle, auscultation, oto-, oyer, oyez.'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. ear\", \"stance\": \"supports\",\n     \"note\": \"Skeat gives the same Germanic series (OE ēare, Goth. ausō, Icel. eyra) with Lat. auris, Gk. ous as cognates; grepped SKT.txt s.v. 'Ear (1)'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10,\n  \"lang\": \"Greek\",\n  \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Another empty pass-through box, the Greek stage feeding English anesthesia. Its content is Watkins's 'au-5. To \"\n    \"perceive. … 2. Greek aisthanesthai, to feel: AESTHETIC; ANESTHESIA', i.e. Greek αἰσθάνομαι / αἰσθέσθαι \"\n    \"'to perceive' from *awis-dʰ- (Pokorny 78: 'gr. αἰσθάνομαι, Aor. αἰσθέσθαι \\\"perceive\\\" (*aϝισ-θ-)'), with the \"\n    \"abstract αἴσθησις 'sensation' behind ἀναισθησία. Note that this branch hangs on the *au- 'perceive' half of \"\n    \"Nourai's root box, not on *ous- 'ear' — which is why he named the box 'Ôus 1, Au 1, Aus 1'. The bare 'AHD' \"\n    \"reference is right.\"),\n  \"derivation_fa\": (\n    \"جعبهٔ خالیِ گذرگاه دیگری، مرحلهٔ یونانی که به anesthesia انگلیسی می‌رسد. محتوای آن مطلب واتکینز است: «au-5 \"\n    \"«دریافتن» … ۲. یونانی aisthanesthai «حس کردن»: AESTHETIC؛ ANESTHESIA»، یعنی αἰσθάνομαι یونانی از *awis-dʰ- \"\n    \"(پوکورنی ص ۷۸: «یونانی αἰσθάνομαι، ماضی αἰσθέσθαι «دریافتن» (*aϝισ-θ-)») و اسم معنای αἴσθησις «حس» که پشتِ \"\n    \"ἀναισθησία است. توجه شود که این شاخه به نیمهٔ *au- «دریافتن» از جعبهٔ ریشه آویخته است، نه به *ous- «گوش» — و \"\n    \"همین است که نورایی نام جعبه را «Ôus 1, Au 1, Aus 1» گذاشته. ارجاع «AHD» درست است.\"),\n  \"sources\": [E_ANE, W_H2EW],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. au-5 'To perceive': '2. Greek aisthanesthai, to feel: AESTHETIC; ANESTHESIA. [Pok. 8. au- 78]'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed p.78 (au-8, auēi- 'to perceive, understand')\", \"stance\": \"supports\",\n     \"note\": \"'full grade: gr. αἰσθάνομαι, Aor. αἰσθέσθαι \\\"perceive\\\" (*aϝισ-θ-); Latin audiō \\\"hear\\\" from *auiz-dʰ-iō.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. anesthesia (KLN_1966.txt, pp.74-75)\", \"stance\": \"supports\",\n     \"note\": (\"'anesthesia, anaesthesia, n., insensibility. — Gk. ἀναισθησία, \\\"lack of sensation\\\", fr. ἀναισθητεῖν … \"\n              \"fr. ἀν- … and αἰσθητός \\\"sensible, perceptible\\\", verbal adj. of αἰσθάνεσθαι \\\"to perceive\\\".'\")}\n  ]\n})\n\nN.append({\n  \"id\": 11,\n  \"lang\": \"English\",\n  \"words\": \"anesthesia\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"anesthesia entered English in 1721 in the sense 'loss of feeling', through medical Latin from Greek ἀναισθησία \"\n    \"'want of feeling or perception', an abstract noun in -ία from ἀν- 'without' + αἴσθησις 'feeling' (verbal noun \"\n    \"of αἰσθάνεσθαι 'to perceive' < PIE *h₂ew-/*au- 'to perceive'); the modern sense 'procedure for the prevention \"\n    \"of pain in surgical operations' dates from 1846, the year of the first public ether demonstration (Etymonline). \"\n    \"The chain root → Greek → English is exactly as drawn.\"),\n  \"derivation_fa\": (\n    \"واژهٔ anesthesia در ۱۷۲۱ م. به معنای «بی‌حسی» از راه لاتین پزشکی از یونانی ἀναισθησία «بی‌حسی، نبودِ دریافت» به \"\n    \"انگلیسی رسید؛ اسم معنایی با پسوند -ία از ἀν- «بی» + αἴσθησις «حس» (اسم فعل αἰσθάνεσθαι «دریافتن» از ریشهٔ \"\n    \"هندواروپایی *h₂ew- «دریافتن»). معنای امروزی «بی‌هوشی جراحی» از ۱۸۴۶ م. است، سال نخستین نمایش عمومی اتر \"\n    \"(اتیمانلاین). زنجیرهٔ ریشه → یونانی → انگلیسی درست همان است که در نمودار کشیده شده است.\"),\n  \"sources\": [E_ANE],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"No reference in the box (it inherits AHD from the Greek node); checked against Etymonline and Klein s.v. anesthesia.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. anesthesia\", \"stance\": \"supports\",\n     \"note\": \"'Gk. ἀναισθησία \\\"lack of sensation\\\" … αἰσθητός … verbal adj. of αἰσθάνεσθαι \\\"to perceive\\\". See esthete and cp. esthesia.'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. au-5\", \"stance\": \"supports\",\n     \"note\": \"ANESTHESIA is listed among the English derivatives of *au- 'to perceive' via Greek aisthanesthai.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12,\n  \"lang\": \"Latin\",\n  \"words\": \"audire\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Latin audiō, audīre 'to hear' goes back to a compound of the perception root with *dʰeh₁- 'to put': \"\n    \"*awis-dʰ(h₁)-yō 'to place (one's) perception', whence *awizdiō > audiō; Pokorny 78 states it so ('Latin audiō \"\n    \"\\\"hear\\\" from *auiz-dʰ-iō, compare oboedio from *ob-avizdʰiō'), Watkins the same ('Compound forms *aw-dh-, \"\n    \"*awis-dh-, \\\"to place perception\\\" … Suffixed form *awisdh-yo- or *awdh-yo- in Latin audīre'), and Klein \"\n    \"'L. audio, audire, \\\"to hear\\\", which prob. stands for *awis-d-iō, fr. I.-E. base *awei-, *au-, \\\"to perceive\\\"'. \"\n    \"The first member is the *awis- of Skt. āvíṣ, Av. āviš 'openly, manifestly' (whence also NP آشکار). So the \"\n    \"Latin box belongs, again, to the Au 1 half of the root, and Nourai's gloss 'to hear' is the standard Latin \"\n    \"meaning. Correct as drawn.\"),\n  \"derivation_fa\": (\n    \"audiō/audīre لاتین «شنیدن» به ترکیبی از همان ریشهٔ دریافت با *dʰeh₁- «نهادن» بازمی‌گردد: *awis-dʰ-yō «دریافت را \"\n    \"نهادن» > *awizdiō > audiō؛ پوکورنی (ص ۷۸) همین را می‌گوید («لاتین audiō از *auiz-dʰ-iō، قس oboedio از \"\n    \"*ob-avizdʰiō»)، واتکینز نیز («ترکیب *awis-dh- «نهادنِ دریافت» … در audīre لاتین») و کلاین («audio, audire که \"\n    \"احتمالاً از *awis-d-iō است، از ریشهٔ *awei-, *au- «دریافتن»»). جزء نخست همان *awis- در āvíṣ سنسکریت و āviš \"\n    \"اوستایی «آشکارا» است. پس این جعبه نیز به نیمهٔ Au 1 ریشه مربوط است و معنای «شنیدن» معنای معیار لاتین است. \"\n    \"ادعای نورایی درست است.\"),\n  \"sources\": [E_AUD, W_H2EW],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": (\"Watkins s.v. au-5: 'Compound forms *aw-dh-, *awis-dh-, \\\"to place perception\\\" (see dhē-1). 1. Suffixed \"\n              \"form *awisdh-yo- or *awdh-yo- in Latin audīre, to hear: AUDIBLE, AUDIENCE, … AUDIT, AUDITOR, … OBEY.'\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed p.78\", \"stance\": \"supports\",\n     \"note\": \"'Latin audiō \\\"hear\\\" from *auiz-dʰ-iō, compare oboedio from *ob-avizdʰiō about *oboidiō.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. audible (126/127 leaf)\", \"stance\": \"supports\",\n     \"note\": \"'L. audio, audire, \\\"to hear\\\", which prob. stands for *awis-d-iō, fr. I.-E. base *awei-, *au-, \\\"to perceive\\\", whence also OI. āvíṣ, Avestic āviš, \\\"openly, evidently\\\" … Cp. obedient, obeisance, obey, oyer, oyez.'\"},\n    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch s.v. audiō (LEW_1910.txt)\", \"stance\": \"supports\",\n     \"note\": \"Walde likewise takes audiō from *auiz-dʰ-iō, the same analysis Pokorny (WH. I 80) repeats; grepped 'audio' in LEW_1910.txt.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13,\n  \"lang\": \"English\",\n  \"words\": \"audio, audience, audit, obey\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"All four are Latin audīre words. audio- is a word-forming element from the combining form of audīre, used in \"\n    \"English from the 1890s, with the noun audio 'sound signals' abstracted from it in 1934. audience is Old French \"\n    \"audience from Latin audientia 'a hearing', on audiēns, participle of audīre. audit is a back-formation from \"\n    \"auditor (Latin auditor 'a hearer'), the accounting sense from the practice of hearing the accounts read aloud. \"\n    \"obey came into English c.1300 from Old French obeir, from Latin oboedīre 'obey, be subject; pay attention to, \"\n    \"give ear' — literally 'listen to', from ob 'to' + audīre, the same semantic path as Old English hīersumnian \"\n    \"'obey' from hieran 'hear' (Etymonline). Watkins lists exactly this set (AUDIBLE, AUDIENCE, AUDIO-, AUDIT, \"\n    \"AUDITOR … OBEY) under *au-. Nothing to query.\"),\n  \"derivation_fa\": (\n    \"هر چهار واژه از audīre لاتین‌اند. audio- جزء واژه‌ساز از صورت ترکیبی audīre است که از دههٔ ۱۸۹۰ در انگلیسی به کار \"\n    \"رفته و اسم audio «سیگنال صوتی» در ۱۹۳۴ از آن انتزاع شده است. audience از فرانسهٔ کهن audience از audientia لاتین \"\n    \"«شنیدن» است. audit اشتقاق قهقرایی از auditor (لاتین «شنونده») است و معنای حسابداری‌اش از رسم «شنیدنِ» حساب‌ها با \"\n    \"خواندن بلند برخاسته است. obey در حدود ۱۳۰۰ م. از فرانسهٔ کهن obeir از oboedīre لاتین «فرمان بردن؛ گوش سپردن» \"\n    \"آمده که تحت‌اللفظ «گوش دادن به» است، از ob «به» + audīre — همان مسیر معنایی که در انگلیسی کهن hīersumnian \"\n    \"«فرمان بردن» از hieran «شنیدن» دیده می‌شود (اتیمانلاین). واتکینز همین مجموعه را زیر *au- می‌آورد. ادعای نورایی \"\n    \"درست است.\"),\n  \"sources\": [E_AUD, E_OBEY],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"No reference in the box (it inherits AHD from the Latin node); checked against Etymonline (audio-, obey) and Klein (audible, audience, auditor).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. audience, audit, auditor (126/127 leaf)\", \"stance\": \"supports\",\n     \"note\": \"'audience, n. — F., fr. L. audientia, \\\"a hearing, audience\\\", fr. audiens, gen. -entis, pres. part. of audire'; 'audit, tr. v. and n. — Back formation fr. auditor'; 'auditor, n., a hearer … fr. L. auditorem … fr. auditus, pp. of audire'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins s.v. au-5\", \"stance\": \"supports\",\n     \"note\": \"'Latin audīre, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION.'\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 377,\n  \"book_page\": 347,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [root]\n}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-377.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", p, sum(1 for _ in N), \"nodes\")\n"
}
```


### [2026-09-07T20:37:49.448Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk377.py (file state is current in your context — no need to Read it back)
```


## [2026-09-07T20:37:58.970Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LEW_1910.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'audio,?\\s*-ire|audiö|audio\\b', t))[:4]:\n    print(t[max(0,m.start()-200):m.start()+700].replace('\\n',' '));print('---')\nEOF"
}
```


### [2026-09-07T20:38:00.390Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:38:01.041Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor pat in (r'EAR,\\s*the organ', r'Ear\\s*\\(1\\)', r'\\bEAR\\b'):\n    ms=list(re.finditer(pat,t))\n    print('###',pat,len(ms))\n    for m in ms[:3]:\n        print(t[max(0,m.start()-150):m.start()+700].replace('\\n',' '));print('--')\nEOF"
}
```


### [2026-09-07T20:38:02.423Z] TOOL RESULT

```
### EAR,\s*the organ 0
### Ear\s*\(1\) 0
### \bEAR\b 0
```


## [2026-09-07T20:38:06.925Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c LEW_1910.txt SKT.txt && python3 - <<'EOF'\nimport re\nfor f in ('LEW_1910.txt','SKT.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print('#####',f,len(t))\n    print(t[:300].replace('\\n',' '))\n    for pat in ('audi','Ear','ear,'):\n        print(' ',pat, len(re.findall(pat,t)))\nEOF"
}
```


### [2026-09-07T20:38:08.223Z] TOOL RESULT

```
 627390 LEW_1910.txt
2656202 SKT.txt
3283592 total
##### LEW_1910.txt 619063
eae hee ne ee Duquesne University: joe Kt re | * ee . ¥ c 'DOGERMANISCHE BIBLIOTHEK -ZWEITE REIHE: WORTERBUCHER ____ Digitized by the Internet Archive in 2023 with funding from No Sponsor — re mi https://archive.org/details/lateinischesetymO ) any * ; - % MANY ioe hie vel AN ~ LATEINISCHES: e
  audi 3
  Ear 1
  ear, 0
##### SKT.txt 2620367
This  is  a  digital  copy  of  a  book  that  was  preserved  for  generations  on  library  shelves  before  it  was  carefully  scanned  by  Google  as  part  of  a  project to  make  the  world's  books  discoverable  online. It  has  survived  long  enough  for  the  copyright  to  expire  and 
  audi 21
  Ear 10
  ear, 102
```


## [2026-09-07T20:38:13.339Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LEW_1910.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer('audi',t):\n    print(repr(t[max(0,m.start()-150):m.start()+250]));print('--')\nEOF"
}
```


### [2026-09-07T20:38:15.007Z] TOOL RESULT

```
'sem I 25 astani I 8 asr II 270 ast I 192 astt II 588 asun I 60 atamn I 340 ateam II 202 atela II 202 atok’ II 482 at‘ar I 76 aucanem II 820 aud I 435 audi II 229 auj I 48, II 820 aviun I 81 awaz II 458 ayl I 680 ays I 863 azazem I 65 ampam I 103 and-, ond I 538, 698 anderk‘ I 710 andunim I 58 ant‘ac Il 516 ast II 348 ba I 438 bah I 482 bam I 437 banam I 456 barjr I 536 bas I 437 bavel I 524\n53\nbay'
--
'08\nsja II 531\nsjor II 463\nskakkr II 492\nskdld I 702\nskali IT 196\nskalm I 304\nskammr I 161\nskardr I 316\nskarfr I 290\nskarn II 133, 497\nskarpr II 500\nskaudir I 301\nskaunn IT 196\nskaut I 185\nskeva I 210\nskefill II 487\nskeggja II 495\nskeina IT 495\nskel I 145, II 487\nskeppa II 484\nsker I 170\nSkila II 486\nskilja II 486, 502\nNordgermanisch\nskinn IT 489 skirpa II 498 skja II 196 skjadak I 819 skialf IT 48'
--
'328\nzime (alem.) I 324\nBaltisch\nauklipts I 232\nauclo I 435 Auctigarbin I 850 aucktemmien TI §2 aulaut I 835\naulis, aulinis I 34 aumtisnan IT 126 auschauditwet I 186\n» ausins I 85\nausis I 8&6 awins IT 229 awis I 88& babo I 436 ballo I 560 balsinis I 122, IT 625 be I 558 bebbint I 90 bebrus I 490 berse I 544 bidtwer I 523 birgakarkis I 486 bitarz IT 788 bitte I 556 blusne I 799 boadis I 522 bordus I'
--
```


## [2026-09-07T20:38:15.432Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'[Ee]ar[,.]?\\s+the\\s+organ|EAR\\.|\\bEar\\b', t))[:8]:\n    s=t[max(0,m.start()-100):m.start()+500].replace('\\n',' ')\n    if 'organ' in s or 'auso' in s or 'auris' in s:\n        print(s); print('--')\nEOF"
}
```


### [2026-09-07T20:38:16.876Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:38:22.820Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'auso', t):\n    print(t[max(0,m.start()-500):m.start()+300].replace('\\n',' '));print('--')\nEOF"
}
```


### [2026-09-07T20:38:24.102Z] TOOL RESULT

```
rth.     (F.  -  L.) ?/«r,  golden. r©f  brass.  (F.-L.)    F. led  gold.'""F.  or,  from '  mouiUt  pp.  oimoudrt, in,  which    from  L. ifiShyw  ralpharrt  of  arsenic '  gold  ptint-'  F.  ot-timtnt. ifw.  gold  paint.  *  L.  Avn-. IxL  fismtnlum,  a  pigment, f»rr.  1     V— • ;>itl  slnnc-crop. od  M  'i>ut.     M   b. l\u»,  *  orpiD,  or  lire'long ; *  Cot     A  docked  form  of ^UMUltAUon ;  seeAadi- AVAST, «3 Aurora,  the  dawn.  (L.)  L.  avrem,  the dawn  ;  put  for  an  oldtri  ausosa  *.+Gk.  ijif, ..4iolic  afaff  ;  Skt.  uikAsd,  dawn.    (^US.) Auepioe.  (F.-L.)     See  Aviary. Austere.  (F.-L.-Gk.)     '^A.'E.  amUrt. —  O.  h' .  aujtfr:f.»h. aufUrvs,  harsh,  severe. ■•Gk.  a^Tij^r,  making  the  tongue  dry, harsh.  — Gk.  aSor,  parched;  aCur,  to  parch, dry. 
--
  Oav«. Wdo (F-L.)    O.K.  «. to  raise ;  to  saipotA. r*r  lo  drive,  oofy  in toOBUrltr. Oapaoioaa. a  ■elected  patuge.  (L.)     L. «n    «tr«ct ;    oeut.    of   pp.    of •elect.  —  L.  ur,  out;  car^rt^ •coicc,  acuity,  oiggord  (F. I*  umrfnUt  lihort  form  of tDbttimte  for  L.  /x* ,  lo  tclcct  ^above). picked   out.   teJect, Ood* EXEMPT. 139 I    Bxchaquer ;  tee  Cheolr. ,    Exoiae,  s  (ax:  see  Sedentary. Sxdslon ;  see  Ctesura. Bxolaim ;  see  CUim. Bzduda ;  tee  Olauso. Excoxomunioate ;  tec  Common. Excoriate ;  see  Cuirass. Excrement ;  f>cc  Concern. Excreeccnce;  see  Croaoent. Excretion ;  tee  Concern. Excruciate ;  see  Crook. Exculpate ;  tee  Culpable. Excursion ;  see  Current. Excuse ;  see  Cause. Execrate ;  tee  Baored. Execute ;  see  Sequenoe
--
elonginj;  to  Magdala ;  Luke,, riii,  1.  —  Hcb.  nn^iii>'.  a  tower;  wbenoe A/ar(/afa  as  a  proper  name. Maugre ;  tec  Malioe. Maul,  to  disfigure;  see  Mall  (i). Maulatick,  a  stick  n&ed  by  painters  to steady  the  hand.  (G.)  G.  maltntock,  lit. 'painter's  sticlc*«-G.  maJer,  a  painter,  from malen,  to  point ;  stock,  a  stick.  Malen  was orig.  to  mark,  from  G.  mahl,  O,  H.  O. mj/,  a  mark,  mole;  see  Mole  u) and  Stock. Maundy  Thursday :  see  Mandate. Mausoloumf  a  magnificent  tomb.  (L, «Gk.)  L.  mausaUum,  a  splendid  tomb, orig.  the  tomb  of  Mau^olus.-*Gk.  Mavoai- \uov\  from  Viavaai\off  Mausolus,  a  king  of Caria. MaU70,  the  name  of  a  colour ;  see Mallow. MaviB,  the  song-tbnisb.  (F.-C.)  M.E mavis.  »  F.  mauvis,  a  thro
--
igure;  see  Mall  (i). Maulatick,  a  stick  n&ed  by  painters  to steady  the  hand.  (G.)  G.  maltntock,  lit. 'painter's  sticlc*«-G.  maJer,  a  painter,  from malen,  to  point ;  stock,  a  stick.  Malen  was orig.  to  mark,  from  G.  mahl,  O,  H.  O. mj/,  a  mark,  mole;  see  Mole  u) and  Stock. Maundy  Thursday :  see  Mandate. Mausoloumf  a  magnificent  tomb.  (L, «Gk.)  L.  mausaUum,  a  splendid  tomb, orig.  the  tomb  of  Mau^olus.-*Gk.  Mavoai- \uov\  from  Viavaai\off  Mausolus,  a  king  of Caria. MaU70,  the  name  of  a  colour ;  see Mallow. MaviB,  the  song-tbnisb.  (F.-C.)  M.E mavis.  »  F.  mauvis,  a  throstle ;  cf.  Span. maJvis,  a  thrush.— Bret,  milfid^  milvui,  a mavis,  also  m\kk<mid  (at  vanncs).  Cf. Com.  mtikuis^  O.  Com.  melhtut,  a  lar
--
Saiumus,  Saturn:  lit.  'the sower;'  from  tatum,  supine  of  urert,  to sow.     See  Beaaou. Saturday.  (L.  and  IS..)  A.S.  SaUr- t/rf--'.  also  Satem-da^^  i.e.  Sntura's  day. — L.  SaturHus,  Satoin ;  K.  S.  dag,  a  day. Satyr.  ^F.  -  L.-  Gk.)  F.  satyn.  -  L. ja/yrwx.  —  Gk-ffarupoi,  a  satyr,  a  sylvan  god. Sauce,  Saucer,  Saucy ;  see  Salt. Saunter.  <  F.  t)     Oricin  unknown. Saurian,  otic  of  the  lizard  tiibe.  (Gk.) From  Ok.  aavpa^  aavpos,  a  lizard. Sauso^ ;  see  Bait. Sauteme,  a  wine.  (F.)  From  SauUnu in  France,  department  of  Giroode. Savage ;  see  BilTan. Savanna,    a  meadow-plain.  (Span.  — L. —  Gk.)  Span.  sal>ana  (with  ^  as  v),  a sheet  for  a  be«l,  large  clolb.  large  plain (from  the  appearoncc  of  a  plain  cov
--
```


## [2026-09-07T20:38:33.918Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Bar\\b|Ear\\b', t):\n    s=t[max(0,m.start()-80):m.start()+420].replace('\\n',' ')\n    if 'organ' in s or 'A.S. e' in s or 'hear' in s.lower():\n        print(s); print('--')\nEOF"
}
```


### [2026-09-07T20:38:35.230Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:39:00.050Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PYEOF'\nimport io\np='mk377.py'\ns=io.open(p,encoding='utf-8').read()\n\nold_skt = '''    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. ear\", \"stance\": \"supports\",\n     \"note\": \"Skeat gives the same Germanic series (OE ēare, Goth. ausō, Icel. eyra) with Lat. auris, Gk. ous as cognates; grepped SKT.txt s.v. 'Ear (1)'.\"}'''\nnew_skt = '''    {\"src\": \"POK\", \"where\": \"printed p.785 (ōus- 2, aus-, us-)\", \"stance\": \"supports\",\n     \"note\": (\"'Root/lemma: ōus-2, aus-: us-  Meaning: ear … Gothic auso n. \\\"ear\\\" (Germanic *ausan-) … Old English \"\n              \"eare … References: WP. I 18, WH. I 85 f.' — the English word is the Old English member of this series.\")},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\", \"stance\": \"silent\",\n     \"note\": \"The local OCR of Skeat is too corrupt in the E- section to retrieve the 'ear' entry (searched 'Ear', 'auso', 'A.S. eare' — no legible hit); no evidence either way from this book.\"},\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/ear\", \"stance\": \"supports\",\n     \"note\": \"'ear (n.1) \\\"organ of hearing,\\\" Old English eare \\\"ear,\\\" from Proto-Germanic *auzon, from PIE *ous- \\\"ear.\\\" … IE cognates include Greek ous, Latin auris, Lithuanian ausis, Old Church Slavonic ucho, Old Irish au \\\"ear,\\\" Avestan usi \\\"the two ears.\\\"'\"}'''\nassert old_skt in s\ns=s.replace(old_skt,new_skt)\n\nold_lew = '''    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch s.v. audiō (LEW_1910.txt)\", \"stance\": \"supports\",\n     \"note\": \"Walde likewise takes audiō from *auiz-dʰ-iō, the same analysis Pokorny (WH. I 80) repeats; grepped 'audio' in LEW_1910.txt.\"}'''\nnew_lew = '''    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\",\n     \"note\": \"The local LEW file is only the index/register portion of the work (627 kB; 'audi' occurs three times, all in language indices), so Walde-Hofmann's audiō article could not be read here; Pokorny p.78 cites it as 'WH. I 80' for exactly this etymology.\"},\n    {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/audio- and /obey\", \"stance\": \"supports\",\n     \"note\": \"'audio-, word-forming element meaning \\\"sound, hearing,\\\" from combining form of Latin audire \\\"to hear\\\" (from PIE root *au- \\\"to perceive\\\")'; 'obey … from Latin obedire, oboedire \\\"obey, be subject, serve; pay attention to, give ear,\\\" literally \\\"listen to,\\\" from ob \\\"to\\\" + audire.'\"}'''\nassert old_lew in s\ns=s.replace(old_lew,new_lew)\n\ns=s.replace('pdf page 235 (≈ printed 2154)','pdf page 235 (≈ printed 2155)')\ns=s.replace('pdf pages 235-236 (≈ printed 2154-2155)','pdf pages 235-236 (≈ printed 2155-2156)')\nio.open(p,'w',encoding='utf-8').write(s)\nprint('patched')\nPYEOF\npython3 mk377.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-377.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T20:39:01.464Z] TOOL RESULT

```
Exit code 1
patched
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk377.py", line 546
    "note": ("'Root/lemma: ōus-2, aus-: us-  Meaning: ear … Gothic auso n. "ear" (Germanic *ausan-) … Old English "
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```


## [2026-09-07T20:39:09.918Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PYEOF'\nimport io\np='mk377.py'\ns=io.open(p,encoding='utf-8').read()\nbad = '''     \"note\": (\"'Root/lemma: ōus-2, aus-: us-  Meaning: ear … Gothic auso n. \"ear\" (Germanic *ausan-) … Old English \"\n              \"eare … References: WP. I 18, WH. I 85 f.' — the English word is the Old English member of this series.\")},'''\ngood = '''     \"note\": (\"'Root/lemma: ōus-2, aus-: us-  Meaning: ear … Gothic auso n. \\\\'ear\\\\' (Germanic *ausan-) … Old English \"\n              \"eare … References: WP. I 18, WH. I 85 f.' — the English word is the Old English member of this series.\")},'''\nassert bad in s, 'anchor missing'\ns=s.replace(bad,good)\nio.open(p,'w',encoding='utf-8').write(s)\nprint('ok')\nPYEOF\ngrep -n 'organ of hearing,\" Old English' mk377.py | head -2"
}
```


### [2026-09-07T20:39:11.264Z] TOOL RESULT

```
ok
551:     "note": "'ear (n.1) "organ of hearing," Old English eare "ear," from Proto-Germanic *auzon, from PIE *ous- "ear." … IE cognates include Greek ous, Latin auris, Lithuanian ausis, Old Church Slavonic ucho, Old Irish au "ear," Avestan usi "the two ears."'"}
```


## [2026-09-07T20:39:19.690Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 - <<'PYEOF'\nimport io,re\np='mk377.py'\nlines=io.open(p,encoding='utf-8').read().split('\\n')\nfor i,l in enumerate(lines):\n    if l.startswith('     \"note\": \"\\'ear (n.1)'):\n        lines[i] = ('     \"note\": (\"\\'ear (n.1) \\\\u201corgan of hearing,\\\\u201d Old English eare \\\\u201cear,\\\\u201d from '\n                    'Proto-Germanic *auzon, from PIE *ous- \\\\u201cear.\\\\u201d \\\\u2026 IE cognates include Greek ous, Latin auris, '\n                    'Lithuanian ausis, Old Church Slavonic ucho, Old Irish au \\\\u201cear,\\\\u201d Avestan usi \\\\u201cthe two ears.\\\\u201d\\'\")}')\n    if l.startswith('     \"note\": \"\\'audio-, word-forming'):\n        lines[i] = ('     \"note\": (\"\\'audio-, word-forming element meaning \\\\u201csound, hearing,\\\\u201d from combining form of Latin '\n                    'audire \\\\u201cto hear\\\\u201d (from PIE root *au- \\\\u201cto perceive\\\\u201d)\\'; \\'obey \\\\u2026 from Latin obedire, oboedire '\n                    '\\\\u201cobey, be subject, serve; pay attention to, give ear,\\\\u201d literally \\\\u201clisten to,\\\\u201d from ob \\\\u201cto\\\\u201d + audire.\\'\")}')\nio.open(p,'w',encoding='utf-8').write('\\n'.join(lines))\nprint('ok')\nPYEOF\npython3 mk377.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-377.json >/dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T20:39:21.128Z] TOOL RESULT

```
ok
wrote /home/sfmqrb/git/rishe/data/verification/page-377.json 13 nodes
JSON OK
```


## [2026-09-07T20:39:24.232Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 tools/verify_check.py 377"
}
```


### [2026-09-07T20:39:25.882Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'disputed': 1, 'confirmed': 11, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'not_found': 2, 'supports': 6, 'not_checked': 8}
books consulted: {'contradicts': 4, 'silent': 5, 'partial': 4, 'supports': 33} | by book: {'KLN': 6, 'POK': 5, 'CHEUNG': 4, 'HRN': 3, 'BQT': 3, 'MON': 3, 'PHD': 3, 'SYN': 2, 'ARY': 2, 'BRT': 2, 'Etymonline': 2, 'AHD': 2, 'WLD': 1, 'IEC': 1, 'HUB': 1, 'SOD': 1, 'NYB': 1, 'FFD': 1, 'FSF': 1, 'SKT': 1, 'LEW': 1}
```


## [2026-09-07T20:39:33.683Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('FSF.txt',encoding='utf-8',errors='replace').read()\nprint('نغوشا', len(re.findall('نغوشا',t)), 'نغوش', len(re.findall('نغوش',t)), 'نیوش', len(re.findall('نیوش',t)))\n\"\npython3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-377.json'))\ne=d['entries'][0]\nprint('entry keys ok:', all(k in e for k in ('note','note_fa','ref_check','consulted','sources')))\nfor n in e['nodes']:\n    print(n['id'], len(n.get('consulted',[])), len(n.get('ref_check',[])), bool(n.get('derivation_fa')), bool(n.get('derivation')), n['verdict'])\nEOF"
}
```


### [2026-09-07T20:39:35.097Z] TOOL RESULT

```
نغوشا 0 نغوش 0 نیوش 12
entry keys ok: True
1 6 1 True True disputed
2 4 2 True True confirmed
3 4 1 True True confirmed
4 4 1 True True plausible
5 5 2 True True confirmed
6 4 1 True True confirmed
7 3 2 True True confirmed
8 2 1 True True confirmed
9 4 1 True True confirmed
10 2 1 True True confirmed
11 2 1 True True confirmed
12 4 1 True True confirmed
13 2 1 True True confirmed
```


## [2026-09-07T20:39:43.281Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-377.json'))\ne=d['entries'][0]\nprint(e['note_fa'][:200]);print('...')\nprint(e['nodes'][0]['derivation_fa'][:180]);print('...')\nprint(e['nodes'][4]['ref_check'][0]['note'][:300])\nEOF\nls -la /home/sfmqrb/git/rishe/data/verification/page-377.json; git -C /home/sfmqrb/git/rishe status --short"
}
```


### [2026-09-07T20:39:44.628Z] TOOL RESULT

```
ریشهٔ هندواروپایی آغازین *h₂ṓws «گوش» (پوکورنی ص ۷۸۵) و ریشهٔ *h₂ew- «دریافتن، آگاه شدن» (پوکورنی ص ۷۸، خاستگاه audīre لاتین و αἰσθάνομαι یونانی) هر دو واقعی‌اند و هر دو ارجاع نورایی (POK:78,785) درست
...
«Ghosh» گونهٔ نویسهٔ نورایی از ریشه‌ای است که پوکورنی ghous- (و کهن‌تر gheus- : ghous-) «آوا دادن، شنیدن» می‌نویسد؛ خاستگاه ghóṣati سنسکریت «آوا می‌دهد، می‌شنود»، ghoṣa- «بانگ»، او
...
BQT vol.4 pdf page 322 (= printed 2241; the anchor [pdf page 279] carries the running number ۲۱۹۹, so printed = pdf+1919/1920 and Nourai's numbering runs ~2 pages behind this Ibn Sina scan, exactly as on p.316), Mo'in's footnote 6 to نیوشیدن: «niyōšīdan … از: نیوش + یدن (پسوند مصدری)؛ پهلوی nigōšīta
-rw-rw-r-- 1 sfmqrb sfmqrb 71276 Sep  7 16:39 /home/sfmqrb/git/rishe/data/verification/page-377.json
?? data/verification/page-375.json
?? data/verification/page-377.json
```


## [2026-09-07T20:40:02.883Z] AGENT

Page 377 done — `data/verification/page-377.json` written, `verify_check.py 377` reports 13/13 nodes and 0 PROBLEM lines.

**Counts (1 entry, root "Ôus 1, Au 1, Aus 1" PART 2):** root confirmed; nodes 11 confirmed, 1 plausible, 1 disputed. Ref checks: 6 supports, 2 not_found, 8 not_checked. 21 books consulted (33 supports / 4 contradicts / 4 partial / 5 silent).

- **Root box confirmed.** POK:78 = au-8 'to perceive' (source of L. audīre, Gk. αἰσθάνομαι) and POK:785 = ōus-/aus-/us- 'ear' — exactly the two Watkins entries behind the AHD branches. Merging them is not Nourai's invention: WP I 18 puts aus- 'Ohr' under *au- ("Hierzu sehr wahrscheinlich"), Buck 4.22 and Klein do the same, and Wiktionary derives *h₂ṓws from *h₂ew- + *-s.
- **disputed — #1 "Ghosh" [Indo-European]:** Pokorny's ghous- 'tönen, hören' is flagged "Nur indoiranisch" (with a question mark); WP I 569, Cheung ("PIE — —", "Cognate forms outside Iranian are not attested") and Wiktionary (stops at PII *gʰáwšas, Mayrhofer 518) all keep it apart from *h₂ows-; *gʰ- cannot come from *h₂ews-. Nourai's own NOTE already hedges, and the label should read Indo-Iranian. Everything below the node (gaoša → گوش, ni-gaoša → نیوشیدن) is sound.
- **plausible — #4 "Avestan ni-gaoša":** the prefixed stem is unattested in Avestan (only gaoš-/guš- and apa-gaošayeiti). Horn no.1070 writes "aw. *ni- + √gaoš-" with an asterisk, Hübschmann p.104 "iran. *ni-gauš", Wiktionary "Proto-Iranian *ni- + *gáwšati", Gharib "< *ni-gauša-". Derivation accepted, label overstated.
- **Ref-page slips (not extraction errors):** POK:457 on nodes #1 and #2 is wrong twice — the ghous- root is on Pokorny p.454, the page Nourai cites correctly one box lower. BQT:1858 and BQT:2239 both land on the right pages (Mo'in's footnotes on گوش and on نیوشیدن, the latter quoting Horn, Nyberg and Nourai's own Ferdowsi line); Nourai's BQT numbering again runs ~2 pages behind the Ibn Sina scan, as on p.316. ETM:71 (Abolghasemi) and MON:4746 are not obtainable in the cited editions — cross-checked via the same author's FFD p.85 and the 2-vol Mo'in abridgement, both of which support the chart.
- **Extraction nit for the owner:** the book prints `nîŭšîdan` (u-breve) in node #5; the JSON has `nîušîdan` (plain u). The second word `nağŭšîdan` kept its breve. Everything else on the page matches the print exactly; page image copied to `data/verification/sources/refs/ocr/BOOK/377.png`.

File is written but not committed.
