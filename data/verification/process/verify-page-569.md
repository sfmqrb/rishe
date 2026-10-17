# Verification process log — verify-page-569


## [2026-10-17T00:30:14.486Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 569 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-569.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-569.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-569.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 569` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.555Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:20.280Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:20.297Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:30:20.780Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-569.txt"
}
```


### [2026-10-17T00:30:20.795Z] TOOL RESULT

```
1	=== PDF page 569 (book page 539) ===
2	--- entry 0 ---
3	ROOT [Arabic] Zarâfah : giraffe  (refs KLN:657; AHD:558)
4	#1 (parent #0) [Persian] refs=BQT:1009 | zarrâfeh «زرافه ( زراف )» : giraffe
5	#2 (parent #0) [Italian] refs=KLN:657; AHD:558 | giraffa | NOTE: Note the "z" to "j, g" sound change in Italian.
6	  #3 (parent #2) [French] refs=KLN:657 | girafe
7	    #4 (parent #3) [English] refs=KLN:657; AHD:558 | giraffe
8	--- entry 1 ---
9	ROOT [Avestan] Zauša : raising a noise, being violent or bad tempered  (refs AHM:220)
10	#1 (parent #0) [Persian] refs=AHM:220; BQT:1044; MON:1762 | ZÔŠ «زوش» : talk loudly, be violent, a bad tempered person
11	--- entry 2 ---
12	ROOT [Indo-Schythian] Zay, Zi, Âysan : to adorn; to decorate  (refs ISS:16)
13	#1 (parent #0) [Persian] refs=ISS:16 | zîb «زیب ( زیبا )» : beauty ; zîbîdan «زیبیدن ( زیبنده )» : to befit, deserve ; zîvar «زیور» : ornament
14	#2 (parent #0) [Pahlavi] refs=ISS:16 | děpâk : a beautiful cloth, brocade | NOTE: BQT:908 indicates that it may have come from Sanskrit "dîp:to shine".
15	  #3 (parent #2) [Persian] refs=BQT:908 | dîbâ «دیبا» : a colorful cloth | extra: دیبه ، دیباج | NOTE: See root "Dei" for another possible derivation.
16	#4 (parent #0) [Sogdian] refs=ISS:16 | zywr : ornament
17	
```


## [2026-10-17T00:30:21.598Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-569.json"
}
```


### [2026-10-17T00:30:21.624Z] TOOL RESULT

```
1	{
2	  "pdf_page": 569,
3	  "book_page": 539,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Zarâfah",
8	        "lang": "Arabic",
9	        "refs": "KLN:657; AHD:558",
10	        "gloss": "giraffe",
11	        "note": "This word is of an African root."
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Persian",
18	          "refs": "BQT:1009",
19	          "words": [
20	            {"translit": "zarrâfeh", "gloss": "giraffe", "script": "زرافه ( زراف )"}
21	          ],
22	          "script_extra": null,
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 0,
29	          "lang": "Italian",
30	          "refs": "KLN:657; AHD:558",
31	          "words": [
32	            {"translit": "giraffa", "gloss": null, "script": null}
33	          ],
34	          "script_extra": null,
35	          "note": "Note the \"z\" to \"j, g\" sound change in Italian.",
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "French",
42	          "refs": "KLN:657",
43	          "words": [
44	            {"translit": "girafe", "gloss": null, "script": null}
45	          ],
46	          "script_extra": null,
47	          "note": null,
48	          "quote": null
49	        },
50	        {
51	          "id": 4,
52	          "parent": 3,
53	          "lang": "English",
54	          "refs": "KLN:657; AHD:558",
55	          "words": [
56	            {"translit": "giraffe", "gloss": null, "script": null}
57	          ],
58	          "script_extra": null,
59	          "note": null,
60	          "quote": null
61	        }
62	      ]
63	    },
64	    {
65	      "root": {
66	        "name": "Zauša",
67	        "lang": "Avestan",
68	        "refs": "AHM:220",
69	        "gloss": "raising a noise, being violent or bad tempered"
70	      },
71	      "nodes": [
72	        {
73	          "id": 1,
74	          "parent": 0,
75	          "lang": "Persian",
76	          "refs": "AHM:220; BQT:1044; MON:1762",
77	          "words": [
78	            {"translit": "ZÔŠ", "gloss": "talk loudly, be violent, a bad tempered person", "script": "زوش"}
79	          ],
80	          "script_extra": null,
81	          "note": null,
82	          "quote": {
83	            "text": "بانگ کردمت ای بت سیمین - زوش خواندم تراکه هستی زوش",
84	            "poet": "Rŭdakî"
85	          }
86	        }
87	      ]
88	    },
89	    {
90	      "root": {
91	        "name": "Zay, Zi, Âysan",
92	        "lang": "Indo-Schythian",
93	        "refs": "ISS:16",
94	        "gloss": "to adorn; to decorate"
95	      },
96	      "nodes": [
97	        {
98	          "id": 1,
99	          "parent": 0,
100	          "lang": "Persian",
101	          "refs": "ISS:16",
102	          "words": [
103	            {"translit": "zîb", "gloss": "beauty", "script": "زیب ( زیبا )"},
104	            {"translit": "zîbîdan", "gloss": "to befit, deserve", "script": "زیبیدن ( زیبنده )"},
105	            {"translit": "zîvar", "gloss": "ornament", "script": "زیور"}
106	          ],
107	          "script_extra": null,
108	          "note": null,
109	          "quote": null
110	        },
111	        {
112	          "id": 2,
113	          "parent": 0,
114	          "lang": "Pahlavi",
115	          "refs": "ISS:16",
116	          "words": [
117	            {"translit": "děpâk", "gloss": "a beautiful cloth, brocade", "script": null}
118	          ],
119	          "script_extra": null,
120	          "note": "BQT:908 indicates that it may have come from Sanskrit \"dîp:to shine\".",
121	          "quote": null
122	        },
123	        {
124	          "id": 3,
125	          "parent": 2,
126	          "lang": "Persian",
127	          "refs": "BQT:908",
128	          "words": [
129	            {"translit": "dîbâ", "gloss": "a colorful cloth", "script": "دیبا"}
130	          ],
131	          "script_extra": "دیبه ، دیباج",
132	          "note": "See root \"Dei\" for another possible derivation.",
133	          "quote": {
134	            "text": "در گنج دینار و پرمایه تاج - همان گوهر و دیبه و تخت و تاج",
135	            "poet": "Ferdowsî"
136	          }
137	        },
138	        {
139	          "id": 4,
140	          "parent": 0,
141	          "lang": "Sogdian",
142	          "refs": "ISS:16",
143	          "words": [
144	            {"translit": "zywr", "gloss": "ornament", "script": null}
145	          ],
146	          "script_extra": null,
147	          "note": null,
148	          "quote": null
149	        }
150	      ]
151	    }
152	  ]
153	}
154	
```


## [2026-10-17T00:30:26.353Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','AHD','BQT','AHM','MON','ISS','ISS_alt_DKS','HRN','HUB','PHD','NYB','SOD','CHEUNG','SKT','WEB','FSD','PLA','AFM','LKT','DEV','ARY','POK']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:30:26.748Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt", "page_o
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
ISS_alt_DKS null
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
CHEUNG null
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt", "page_offset
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft
```


## [2026-10-17T00:30:30.575Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 80,200p sources/SOURCE_MATRIX.md; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','AHD','BQT','AHM','MON','ISS','HRN','HUB','PHD','SOD','ARY']:\n  print('==',k, json.dumps({x:d[k].get(x) for x in ['local_file','page_offset','lookup_hint','scans']},ensure_ascii=False)[:1500])\n\""
}
```


### [2026-10-17T00:30:31.027Z] TOOL RESULT

```
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
== KLN {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "scans": null}
== AHD {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", "scans": null}
== BQT {"local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"], "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512
== AHM {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt", "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.", "scans": null}
== MON {"local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "scans": null}
== ISS {"local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.", "scans": null}
== HRN {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "scans": null}
== HUB {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "scans": null}
== PHD {"local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", "scans": null}
== SOD {"local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "scans": null}
== ARY {"local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "scans": [{"file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]}
```


## [2026-10-17T00:30:34.211Z] AGENT

Now let me do the local greps: KLN giraffe, AHD, SKT, LKT, DEV.


## [2026-10-17T00:30:36.847Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -A8 '^giraffe' KLN_1966.txt | head -30; echo ==SKT; grep -n -i -A5 '^giraffe' SKT.txt | head; echo ==LKT; grep -n -i -B2 -A6 'giraff' LKT.txt | head -30; echo ==DEV; grep -n -i -A6 'girafe' DEV.txt | head -20; echo ==AHD; grep -n -i 'giraffe' AHD_watkins1985.txt | head; echo ==PHN; grep -n -i -A4 'girafe' PHN.txt|head; echo ==LAM; grep -n -i -A4 'girafe' LAM.txt|head; echo FSD; grep -n -i -A4 '^gi-raffe\\|^giraffe' FSD_vol*.txt | head"
}
```


### [2026-10-17T00:30:37.408Z] TOOL RESULT

```
Exit code 1
16167:giraffe,  n.  —  F.  girafe,  It.  giraffa,  fr.  Arab. zardfah,  which  is  prob.  of  African  origin.  The circumstance  that  Arab,  z  has  become  g  (pro¬ nounced  j)  proves  that  the  word  came  into  the European  languages  through  the  medium  of  the Italians.
16168-girandole.n.,  1)  a  kind  of  firework;  2)  a  water  jet; 3)  a  kind  of  earring.  —  F.,  fr.  It.  girandola , dimin.  of  giranda,  ‘a  revolving  jet’,  fr.  L.  gyran- dus,  gerundive  of  gyrare,  ‘to  turn  round  in  a circle,  revolve’.  See  gyrate  and  cp.  next  word. For  other  Latin  gerundives  or  their  derivatives used  in  English  cp.  agenda  and  words  there referred  to.
16169-girasol,  girasole,  n.,  1)  the  sunflower;  2)  the  fire opal.  —  It.  girasole  (whence  also  F,  girasol),  lit. ‘turning  toward  the  sun’,  fr.  girare,  ‘to  rotate, turn’  (fr.  L.  gyrare),  and  sole  (fr.  L.  solem,  acc. of  sol),  ‘sun’.  See  gyrate  and  Sol  and  cp.  Jeru¬ salem,  artichoke.  For  sense  development  cp. heliotrope,  and  It.  tornasole  (see  turnsole). gird,  tr.  v.,  to  encircle.  —  ME.  girden,  gerden, etc.,  fr.  OE.  gyrdan,  rel.  to  OS.  gurdian,  ON. gyrda,  OFris.  gerda,  OHG.  gurtan,  gurten, MHG.  gurten,  gurten,  G.  gurten,  Goth,  bi- gairdan,  uf-gairdan,  ‘to  gird’,  ON.  gjdrd,  MHG., G.  gurt,  Goth,  gairda,  ‘girdle’,  and  to  OE.  geard , ON.  gardr,  ‘hedge,  enclosure’.  See  yard,  ‘en¬ closure’,  and  cp.  words  there  referred  to.  Cp. also  girdle,  girt,  girth.
16170-gird,  intr.  v.,  to  gibe,  taunt.  —  The  original
16171-girder
16172-meaning  was  ‘to  strike’;  fr.  ME.  girden,gerden, etc., ‘to  strike,  cut  through’,  which  is  of  uncertain origin.  Cp.  gride.
16173-Derivative:  gird,  n.,  a  taunt,  gibe, girder,  n„  a  wooden  or  steel  beam.  —  Formed with  agential  suff.  -er  fr.  gird,  ‘to  encircle’. Derivative:  girder-age,  n.
16174-girder,  n.,  one  who  gibes  or  taunts.  —  Formed with  agential  suff.  -er  fr.  gird,  ‘to  gibe,  taunt . girdle,  n.,  belt.  —  ME.  girdil,  gerdelle,  gurdel,  fr. OE.  gyrdel,  rel.  to  ON.  gyrdill,  Swed.  gordel, OFris.  gerdel,  MLG.  gordel,  Du.  gordel,  OHG. gurtil,  gurtila,  MHG.,  G.  giirtel,  ‘belt’,  and  to OE.  gyrdan,  ‘to  gird’.  See  gird,  ‘to  encircle’,  and instrumental  suff.  -le.  Derivative:  girdle,  tr.  v. girdle,  n.  —  A  var.  of  griddle, girl,  n.  —  ME.  gurle,  gurl,  gerle,  gerl,  ‘boy,  girl’, rel.  to  LG.  gore,  gor,  ‘a  child’;  of  uncertain origin.  Derivatively,  the  -l  in  girl  is  identical with  dimin.  suff.  -el.
16175-Derivatives:  girl-hood,  n.,  girl-ish,  adj.,  girl-ish- ly,  adv.,  girl-ish-ness,  n. giron,  n.  —  See  gyron.
(eval):1: =SKT not found
```


## [2026-10-17T00:30:48.112Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /giraffe,  n.  —  F.  girafe/{print NR-1}' KLN_1966.txt; echo \"--SKT\"; grep -n -i -A5 'giraffe' SKT.txt | head; echo \"--LKT\"; grep -n -i -B2 -A6 'giraff\\|zarāf\\|zuräfa\\|zurāfa' LKT.txt | head -30; echo \"--DEV\"; grep -n -i -A6 'girafe' DEV.txt | head -20; echo \"--AHD\"; grep -n -i 'giraffe' AHD_watkins1985.txt | head; echo \"--PHN\"; grep -n -i -A4 'girafe' PHN.txt|head; echo \"--LAM\"; grep -n -i -A4 'girafe' LAM.txt|head; echo \"--FSD\"; grep -n -i -A4 'giraffe' FSD_vol*.txt | head -20"
}
```


### [2026-10-17T00:30:48.647Z] TOOL RESULT

```
355
--SKT
2691:camelopard,  a  giraffe.  (L.—  Ilcb.  and Gk.)  Formerly  eamdop<u-daiis.  <»  L.  ca- nuhpaniaiis.  —  Gk.  «a^Aovii^>2aAis,  giraffe  ; partly  like  a  camel,  jiaxtly  like  a  pard.* Gk.  j(a/u]Ao-r.  a  camel  i^Wch. gdrndi) \  nud «af>3aA(t,  a  pard  i  see  FartL
2692-camlet,    a    «tuft.     ^Arah )      Formerly fdm^^/.supposedto  be  named  from  coittAin- iiiK  iitmel's  nair.    Really  iVoro  Arab,  kham^ /at,  khamalat,  camlet;  Kicb-  Diet  p.  c'ljs. Camellia.    (Personal   name.)     A   plant named  after  Geo.  Jos.  Kamcl,  a  Moravian Jesuit,   who    dt'&cjibed   the    plants    Ui   the ishuid  of  Liuon. Camelopard :  see  CameL Cameo.  (Ital.)     Ital.  cammeo,  a  cameo, piecious  stune  carved  ic  relief.     Origin  tin* known. Camera.  (L.)     L.  camera,,  a  chamber; hence  camera  odsatra.  a  dork  chamber,  box for  photography  ;  see  Chamber. Camlet ;  see  CameL Camomile ;  .%ec  Chamomile. Camp.  (L.)     We  find  F.  camp  (Cot.)  ; bnt  the  E.  word   was  prob.  taken  directly from  L.  eamfus.  a  field,  ground  held  by  an army.  +  Gk.  w^»o»,  a  garden.
2693-campaign,  orig.  a  large  field.  (F.» L.)  F.  (Picard)  camfaigne^  campapic,  an open  Acld.  —  L.  camfoHui,  open  field.  — L. lamptis^  a  field.  (Also  sptlt  champaii^M^ and  even  champion  in  old  authors.)
2694-oampestral,  Rowing  in  fields.  (L.) L.  camficitr-is^  growing  in  fields. —  L.  cam- pus,  a  field.
2695-champaflrno.  (F.— L.)  Awinenaroed from  Champagne  in  France,  which  means *a  plain  ; '  sec  below.
2696-champaign,  oi^en  country.  (F.— L.) In  Sh.  F.  champai^^nt,  of  which  tlie  Picard form  wa,^  cautpati^u ;  see  oampatgn.
--
7601:Giraffe,  ft  long-legged  animal.  (F.  • Span.«Aiab  — Egypt)  F-jpni^.  — Span. giraffa.  «  Arab.  *ard/,  tani/aL  Fiom ^ypt.  soraphi,  L  e.  long  neck  ^Mahn).
7602-Gird  ^i)>  to  enclose,  bind  ronnd.  ^E.) hi^K.  gurJtn.girddH,  A.  S,  ^m'aw,  to  gild. +Dd.  gordtn,  IceL  gyr^a^  to  gird  (cf. gtriSa,  to  fence  in).  Dan.  gt'orde,  G.  gurun. Cf.  Goth  6i'^atr,/an,  to  begird.  Allied  to aarth.  Garden,  and  Yard.  (VGHAR.) girdle.  (E.)  A.S  gyn/fJ,  that  which girds.  —  A.  S.  gyrdan.  to  gird.  -f-Du.  gordti, \<x\.gyf%iUt  Swed.  giirdel,  G.gurUl.
7603-girth.  (Scand.)  M.  E.  prth.  -  Icel. ^'^rS,  a  girdle,  girth;  gt'^'^%  g"lh  round  the waist :  l3an.^'<i}i-J.^(toth.  gainia,  a  girdle.
--LKT
4911-172
4912-Schweiger';  hieran-  ruui.  zampara 'Schwelgerei',  zamparagiü  'Zeciibruder, WüstUiig',  zamjHiraUc  'Schwelgerei'.
4913:•iiys.  Ar.  zjirb: 'Waäserrinne',  plr.  zurüh;  hieraus  mit ar.  Art.  pg.  algeroz,  aljaroz  'Dachrinne' |ar.  z  y>  0  wie  in  zuräfa  ^  girafa  und ar.  b  >  '-|.    [DE  125.   Eguilaz  180.
4914-^199.  Ar.  zarb: 'Hölzerner  Pferch  für  Vieh'  ;  hieraus  uiit ar.  Art.  pg.  ozerve,  azerbe  'aus  Zweigen hergesteilte  Wand  zum  Schutz  der  Üörr- diele'  [Constancio  Dicc  1.50a].  (DE  227. Eguilaz  322.
4915-2-20Ü.  Pors.  zärbäf: 'Golddurchwirktes  Gewebe,  Brokat'  [aus pers.  zär  'Gold',  Horn  NpEt  S.  145. Nr.  654,  und  bäftän  'weben'  ebenda S.  38,  Nr.  168],  ebenso  tk.  zerbaf  ;  hier- aus rum.  zarpa  'Brokat,  Brokatkleid, mit  Gold  durchwirkte  Pferdedecke'.  [Sain 61.    Löbel  EITAP  101.
4916-2201.  Ar.  zarbatäna:
4917-'Blasrohr  zum  Töten  von  Vögeln'  [mit adventivem  r,  auch  ohne  dieses:  zaba- iäna,  aus  dem  Pers.,  das  sicherlich  auf mal.  semjntan  'langes  Rohr  mit  enger Öffnung,  um  Pfeile  hindurehzublasen' aus  semjnt  'eng'  Pijn  140a  zurückgeht]; hieraus  sp.  zarbatäna,  zerbatana,  cebra- tana,  pg.  sarabatana,  saravatana,  frz. sarbacane  [mit  Anlelinung  an  canne 'Rohr']  'Blasrohr',  it.  cerbottana  '2  bis 3  m  lange  hohle  Stange'.  [Vgl.  ngr. rapaßoTdva].  [DE  251.  Uevic  DEt  203. Eguilaz  367.  ML  9600.  Lammens  Rem 214/215.    GrSVociSic  2-50.
4918-2202.  Ar.  zarf:
4919-'Untertasse',  aus  Porzellan  oder  Metall, in  die  man  die  Tasse  fingän  hineinstellt (wie  bei  unseren  Teegläsern),  tk.  ebenso zarf;  hieraus  serb.  zarf  'kleine  Schale' ; rum.  zarf  'Untertasse,  Untersatz,  Näpf- chen'.
--
4972-2233.  Pers.  zniniirud:
4973-'Smaragd'  [vielleicht  aus  gr.  oiudtpaYboQ, wahrscheinlich  beides  aus  dem  Ind.], ebenso  tk.  ziimriid  [Kelekian  Kämüs 646  b];  hieraus  hu\^.  zumrtui,  russ.  izum- rud  'Smaragd'.  [Gorjnjew  122.  Mikl SlEtWb  404  b.    Bern  SlEtWb  441.
4974:2234.  Ar.  zmära: 'Giraffe,  Cameloparilwlis  giraffa'  [sicher- lich selbst  ein  Fremdwort  und  wie  das
4975-Ar.  zurziil.
4976-174
4977:Tier  aus  Zentralafrika  stainuiend];  hier- aus it.  i/iraffa,  Irz.  girafe,  kat.  sp.  pg. (firafa,  runi.  girafä;  engl.  ndl.  giraffe, dtsch.  Giraffe  [älteste  Belege  s.  ZfdWf Xi,  3041'.];  russ.  i»ro/'.  [ÜE  218.  Egui- laz  413.    ML  9602.
4978-2235.  Ar.  /nrzäl: 'Drossel',   auch   zurzür   [KM  II,  839, Z.  G  V.  u.] ;  hieraus  sp.  pg.  zorzal  'dass.'. [DE  369.    Eguilaz  .531.    ML  9629.
4979-176
4980-Sach-  und  Namensverzeichnis.
4981-'Abbäs  I.  4 'Äbbäs  Pascha  507 Äbutilon  14 Adamsapfel  19 Ädenia  venenata  20 Adhatoda  1161 Ägypten  1222 Ailantus  glandulosa  1141 ^Zc«Z(J  1021 Alcdntara  1057 .4Zei)^;o  792 Algarve  674 Alhambra  882 Aljarafe  (de  Sevilla)  1840 ^/fco/jo/  1227 Almagra  1349 Amber  78 Amocklaufen  71 Anakonda  74 Antiaris  toxicaria  2136 Antilope  saiga  1774 .4rafta  90 ^rec«  1 7 Argali  96
4982-Arrecife  (Cördoba)  1704 ^4ssassmeM  839 ^<o«  132 '4«äö  133 Averroes  1084 ^OTcmna  579.  893. Bagdad  170 Bairam  183 Bakkam.  190 jBa/^is  203 Bartole  259 Baumwollpapier  1723 jBeÄen  176 Belsazar  1456  a Beriberi  291 £ete  sicula  1907
4983-318.  2149 Boehmeria  nivea  1697 Bolgar  351 Bougie  340 Brindisi  1657 Brundisium  1657 Brunfels  1570 Bungalo  214
4984:Bürän  358 ^Msa  376 Busbeck  544 Casuarina  1119 Casuarius  galeatus  1119 Cagatai  639 Ca/a  (Sizilien)  1036 Calamus  rotang  1724 Camelopardalis  giraffa
4985-2234 Camphora  1100 Cannabis  indica  839 Carrfoib  397 Ceratonia  siliqua  1182 Cercopitheciis  1 422 «.  Chamisso  1623.  1882. Chavica  belle  2149 Chedive  876 C/*mrt  841 Cochenille  1219 Collocalia  esculenta  1844 Constantin  VI.  1388 Corchorus  capsularis  693 Crataegus  azarolus  2206  ' Cypraea  moneta  1 133 Daimio  1992 Dante  1305
4986-Daudet  (Alphonse)  1542 Z)eZ«&as  507 Dipus  aegyptiaeus  936 Dollar  (zeichen)  1996 Domback  2012 Dschiu-Dschitsu  963 Dumdum  477 Dmws  Scotus  1927 Elixir  903 jBmM  1528 d'Entrecolles  1060 Equus  onager  1233 Esdragon  2034 Euphorbia  567 Euphorbus  567 Eusebius  1389 jPeZ«s  caracal  1081 Fe«  596 Floririda  1002 J'ooie  (Samuel)  1542
4987-Friedrieh  II.  1799
4988-i?'Ms^äjf  621
4989-Gadämas  633
4990-Gaeta  644
--
--DEV
1420:Girafe.  Esp.  girnfa  (ancienn.  azorafa),  portug.  giraja, ital.  giraffa.  On  trouve  en  vieux  français  orajle  (Joinville), girajlc;  Marco  Polo,  dans  l'édit.  Pauthier,  écrit  gcrojle. C'est  l'arabe  ioi^^  zourâfa,  zcrâja.  Meninski  donne  aussi UU-Aw,  bb)^  sourmlpâ ,  zourndpâ.
1421-Dans  le  man.  de  la  collection  de  M.  Schefer,  intitulé jsj^]  L^pjJ^  Merveilles  de  l'Inde,  ouvrage  dont  il  a  déjà été  question  et  qui  paraît  avoir  été  rédigé  au  x"  siècle  de
1422:notre  ère,  on  lit  sur  la  girafe  le  passage  suivant  :  <;^Jv-aw^
1423:conté  que  dans  l'île  de  Lamri  il  y  a  des  girafes  d'une grandeur  indescriptible.  Des  naufragés,  forcés  de  marcher des  parages  de  Fansour  vers  Lamri,  se  gardaient  de  che- miner la  nuit,  par  crainte  des  girafes;  car  elles  ne  se montraient  pas  le  jour.  Et,  quand  approchait  la  nuit,  les voyageurs  montaient  sur  un  grand  arbre,  par  peur  de ces  animaux.  Et,  la  nuit  venue,  ils  les  entendaient  rôder autour  d'eux;  et  le  jour,  ils  voyaient  les  empreintes  de leurs  pas  sur  le  sable.??  (P.  96.)
1424-9
1425-J30  DICTIOINNAIIU':  ÉTYMOLOGIQL  l!!
1426-Cela  ne  ressemble  guère  a  ce  que  raj)|)orU!  le  1\  Ange de  Saint-Joseph,  qui  explique  ainsi  le  mot  gi^'fijffh  ^^))^ dans  son  Gazophyl.  ling.  Pers.  :  çr Petit  daim;  l'on  en  trouve des  troupes  en  voyageant  par  la  Perse  :  elles  connaissent en  regardant  un  homme  s'il  est  amy  ou  ennemy,  et  en même  temps  ou  fuyent  ou  s'arrêtent.  »
1427-GiRBE.  Vieux  mot  désignant  le  péritoine.  Portug.  et  ital. zirbo.  De  l'arabe  c_.y  therb,  même  sens.  (Voy.  Freytag,  et aussi  Bocthor,  à  péritoine  et  à  épiploony    '
1428-GoLGOTHA.  En  grec,  yoXyoOâ,  que  les  Evangiles  ex- pliquent par  707105  KpoLviov,  place  du  crâne,  soit  à  cause de  l'aspect  de  l'endroit,  soit  parce  qu'on  y  trouvait  beau- coup de  crânes  de  suppliciés.  C'est  un  mot  chaldaïque NnS^Sj  gouJgalthyf ,  en  hébreu  nSsSs  goidgokth,  crâne.
1429-GoMOR.  Mesure  de  capacité  pour  les  matières  sèches, chez  les  Hébreux.  C'est  la  transcription,  dans  les  Septante, yojuop,  de  l'hébreu  "iDi?  'orner,  une  poignée.  Cette  mesure était  la  dixième  partie  d'une  autre,  nommée  nÇN  ephah.
--
2911:Azorafa,  esp.  voy.  Girafe.
2912-Azoth.
2913-Azougue ,  jMg-.  voy.  Assogue.
2914-Azub,  voy.  Alchimie,  33.
2915-Azucar,  esp.  voy.  Sucre.
2916-Azul,  hisp.  voy.  Azur.
2917-Azur.
--
3554:Gerofle,  voy.  Girafe.
--AHD
--PHN
5338:GIRAFE, s. f. (a.)
5339-Ailjy [zcrr^t], dérivé de cjjj [zeref\ marcher avec rapidité. Les
5340:Arabes ont sans doute appelé ainsi la girafe, à cause de sa lé-
5341-gèreté et de la vitesse de sa marche. Semblable au chameau
5342-sous plusieurs rapports, cet animal a la tête petite, surmontée
5343-de cornes velues, et les jambes de devant plus hautes que celles182 GOD
5344-de derrière; sa peau, tachetée de blanc sur un fondroussâtre,
--
10548:Girafe, s. f. (a.)
10549-Gobeau, s. m. (p. ) — Gobelet, s. m
--LAM
789:A : mahonne, girafe, calaf, Chewal.
790-E : ben ( de ô\ ), civette, cubèbe, chebec, chalef,
791-alkékenge, séné, carabe.
792-/ : zinzolin, gengéli, bougie, aubergine, abit, alfier.
793-Dans sirop l'alef est devenu 0. Ajoutez souche, d'abord
--
4384:Girafe* Esp : girafà, jlrâfa {ancienn. azorafa). It : giralTa;
4385-de i\jj , :{arâfa^ i^ourâfa. On trouve aussi 31 j3 1 sfour-
4386-rdfa^et SI j>., goard/a, forme moins classique, mais très
4387:voisine du nom de la girafe dans les langues romanes (i).
--FSD
FSD_vol3.txt:45103:lioriis back of ihe miln horns. (Ui a hve-horiicd giraffe
FSD_vol3.txt-45104-mlx'soilt a Sunt A triangular Hlorin*sml, so.mdimes
FSD_vol3.txt-45105-set (III tie mizzimmast in r>lii< I nl the spanker geuerully
FSD_vol3.txt-45106-Hilled «/«^roi-ou/x» " .'^«ellllI'^ midei Hitir \< F viUaini,
FSD_vol3.txt-45107-It mtzztnu ' I m * iliHU . ms mepiaN', o ) lillx'scii*
--
FSD_vol3.txt:92411:rica, differing from tlie giraffe by
FSD_vol3.txt-92412-S>h mWaTlcnSraSy'^^^^ lake Okanogan to the Co- O'laf, 1 6'laf. 26Maf. Saint (908-* /wl030). Klngand patron
FSD_vol3.txt-92413-lumbla river 8. A county in N K Washington. 8,318 sq saint of Norway, who Christianised the country. O-te'ns:.
FSD_vol3.txt-92414-ir i5unl[5-«oa? (^iiiVronully O'laf Tryg^ves-son. 1 trlg'vcs-w. 2 trjg'v^n (986-1(^1.
FSD_vol3.txt-92415-0"'ka-noi'u-lN*e. n. Hume ns NnxuDRK King of Norway, who deposed Haakon the Bad. In 900.
FSD_vol4.txt:1754:Sam"o-the'rI-uni,  l   sam'o-fhl'n-um  2   silm'’o-thC'ri-Om,  n Palcon  An  e'ctlnct  genus  of  ungulates,  fossils  of  hich,  found in  the  Greek  Miocene,  show  them  to  have  resembled  giraffes but  with  shorter  neck  [<  S\mo3+  Gr  thmeon  beast ) Sam'o-thrace,  1   sam'o-thrCs  2   sam'o-thrac,  n   Bib  (R  V   )
FSD_vol4.txt-1755-ervation  of  the  pattern  or  patterns  3.  A   device  for removing  a   portion  of  a   substance  for  test  An
FSD_vol4.txt-1756-exemplar,  pattern  (<  F   cxemplaire,  sec  exemplar) sain'plcr-} ,   l   sam'plsr-i,  2   sftm'plcr-y.  n   Tlic  art  of  making samplers,  ombrolderj ork
FSD_vol4.txt-1757-Same  as  SiMOTHRXKi,  — Victory  orSamothr.icc,  a   statue  sam'pllng,  1   sim'plip,  2   sfim'pllng,  n   Paper,  colored  or set  up  by  Demetrius  Pollorcctes  In  305  B   C   ,   now  In  the  uhlto  used  In  exhibiting  textile  samples Louvre  Paris  sain'pllng*tubc",  1   eam'plio*tlQb',  2   sfim'plIng-tOb',  n   A
FSD_vol4.txt-1758-Sain"o-thra'cl-a,  1   8am’o-nir5'<hi-o,  2   a5m  o-thrJl'shl-a  n   pipette  for  taking  small  quantities  of  liquor  from  a   cask Bib  .icisxvl,  11  See  SxMOTiiRAKi  Sa"mo-thra'kCt  (Gr  )   Samp-sji'’an,  1   samp-sl'an,  2   n   One  of  a   sect
--
FSD_vol4.txt:63616:gingival,  a   ,   JIn-jal'val,  E   7   37  TF*.  1,  3   6. 6.  7,  9,  11, 16. 16,  20,  21.  22,  23,-Jln'ji-v0l. S   TF  *   TFr ,   8,  12,  24.  25 giraffe,  Ji-raf',  E   E   7   37  5   *   TFr  ,   1,  3.  4.  5,
FSD_vol4.txt-63617-6,  7,  8,  11,  12.  13S  14,  15.  16,  17,  19,  20,  21. 22,  23.  24,  25  -31-raf',  5*.-Ji-rof'.  TF ,   9. — Ji-rar,  13*.  18
FSD_vol4.txt-63618-girandole,  Hr'en-dOl.  E   E   7   37  8*  TF  TFr . I   3,4,5.6,7.8,9,11,12  13.14,15,16  17,
```


## [2026-10-17T00:30:58.302Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['BQT'].get('page_offset'),ensure_ascii=False)); print(json.dumps(d.get('ISS_alt_DKS') or {k:v for k,v in d.items() if 'DKS' in k},ensure_ascii=False)[:600])\"; grep -n 'زرافه' BQT_v2_pages.txt | head; grep -n 'زوش' BQT_v2_pages.txt | head"
}
```


### [2026-10-17T00:30:58.689Z] TOOL RESULT

```
"vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...')."
{}
27877:‫که آبرا زرافه و شتر کاو پلنگ خوانند چه‬                       ‫؛ و با‬        ‫عمود کار اسواخت‬              ‫ب‬
27904:                                                 ‫‪ - ¥‬رك ‪ :‬زرافه ‪.‬‬                    ‫‪:‬راغن ‪.‬‬
27909:                       ‫‪ #‬زرافه ‪ -‬بفتح‌اول وچهارم (صاحب قاموس آارا بچهار وزن بادکند)؛‬
27911:                       ‫"رادوی‬                                                   ‫از عربی زرافه |‬
412: ‫بر وزن بازوشکن » بلغت زند ودازند(‪ )۱‬بمعنی‬                                            ‫گویند ‪.‬‬
6347: ‫چرغ وبازوشاهین وامثال نراکوبند‪ -۱۷‬وبمعنی‬
7287:      ‫‪- ۱‬مخفف چنگال (ه‪.‬م‪« :).‬چنگل‪ ,‬ناخن‌بازوشاهین‌راگویند‪ .‬رود کی(سمرقندی) کفت‪:‬‬
9465:                  ‫لدارد بپر کس ورا استوار ‪.‬‬                         ‫همی داردش روزوشب‌در کنار‬
11230:‫رگاویند کهآ نرا پر اشزوشة طلا با زرنقد کرده‬
17739:‫هم گفته‌اند که‌دروایست باشد® ‪-‬ونامفرشته‌است*‪۷‬‬              ‫صدایی‌باشد که اتزواختن ناقوس وتارسازوشکستن‬
18951:  ‫بناهای عجیب اکزوشکها وابوانهاست که همه را ازنخته سنگهای خوش برش بآوررده‌اند وبیننده‬
19890:      ‫کزوشت قیمه کرده آکنده باشند ‪-‬‬
22742:                                              ‫ممحف « زوش » («‪.‬م‪ .).‬و رك ‪ :‬لفت نامه ‪.‬‬      ‫‪۴‬‬
25991: ‫رومی ود نگی «کنابه از روزوشب‬                     ‫روملوس ‪ ۴‬با لامر‪-‬ین بی‌نقطه(‪)۱‬‬
```


## [2026-10-17T00:31:04.958Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27895,27925p BQT_v2_pages.txt; awk 'BEGIN{RS=\"\\f\"} /بفتح‌اول وچهارم \\(صاحب قاموس/{print \"leaf\",NR-1}' BQT_v2_pages.txt; grep -n '\\[pdf page' BQT_v2_pages.txt | awk -F: '$1<27909' | tail -1"
}
```


### [2026-10-17T00:31:05.435Z] TOOL RESULT

```
                                               ‫قطه دار ‪.‬‬     ‫‪:‬‏‬   ‫(‪ )۲‬چك‬                   ‫(‪ )۱‬چك‪ :‬نودر ‪.‬‬
     ‫؟ = زرك = ‪ 51۲60۲6۳‬دثایتی ‪4۸۱٩‬‏ ‪.‬‬                                ‫‪.‬‬     ‫زارتشت‬   ‫رك ‪ :‬زردشت ‏‬         ‫‪۱‬‬

                                                                                           ‫‪ = ۴‬زراجه ‪:‬‬
                ‫که برپشت پیلان کشم پیل پای‪.‬‬                               ‫زراحه هنم پیل پولاد خای‬
     ‫نظامی کنجوی «کنجینه ‪A۷.‬‏‬

     ‫»ارغنگه ‪.‬‬
             ‫‪_ °‬رك ‪ :‬زراغش ز‬                         ‫‪ = ۴‬زراغن = زارغنگه = زراغنگه ‪.‬‬
                                                 ‫‪ - ¥‬رك ‪ :‬زرافه ‪.‬‬                    ‫‪:‬راغن ‪.‬‬
                                                                                           ‫‪ ۱‬رك ز‬
                                                                             ‫» زرفن‪.‬‬        ‫ین‬
                                                                                             ‫ف‪:‬‬‫زلرك‬
                                                                                                  ‫‪۸‬‬
                       ‫‪ #‬زرافه ‪ -‬بفتح‌اول وچهارم (صاحب قاموس آارا بچهار وزن بادکند)؛‬
                            ‫و ازین زبان وارد ف‬
                       ‫"رادوی‬                                                   ‫از عربی زرافه |‬
                                                              ‫رکه ‪ :‬دزی ج ‪ ۱‬ص ‪۷۸۵‬‬
                      ‫و انگلیسی ‪ 6112718‬و آلمابی ‪ 616271‬شده ؛ لوعی از پستانداران‬                                 ‫‪6‬‬
                                       ‫شخرار کننده افریقا ‪ ,‬باقدی بسیار بلند ‪ .‬رکه ‪:‬لك ‪ ۲‬ص ‪. ۸۰۲‬‬
    ‫—‬        ‫)‪0‬‬
                                                                                                                       ‫زراوه‬

 ‫ونفس ناطفه ‪ -‬و عقل فلك عطارد ‪ -‬ونورمجرد‪-‬‬                                 ‫تام خوای ابت که آن دونوع میباشد ‪ :‬یکی‬
        ‫وعفل فعال ‪ -‬ورب‌النوع انان وراست کوی‬
                                                                          ‫را زراوند طوبل میگوبند یمتی‌دراز وآترا شجرة‬
‫رالیز گوبن دکه‬               ‫ورردشت‬              ‫و لور ردان باشف ‪۷‬‬        ‫رستم و قتاءالحیه میخوانند » وآن نر باشد و از‬
                      ‫یشرو ویشوایا شس برستان است ‪.‬‬                         ‫انگشت بر گنده‌تر »گرم است در سیمو خشك‬
 ‫زر لك س با ای قرشت بر وزن‬                                                ‫است دردویم ؛ ودیگربرا زراوند مدحرج خوانند‬
‫کل کاو شه‬               ‫وخق‬      ‫باشف ‪۰‬‬          ‫خق‬     ‫آب‬   ‫که ‪۰‬‬   ‫زرد‬
                                                                           ‫است‬     ‫روف‬
leaf 471
```


## [2026-10-17T00:31:14.140Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in $(seq 495 508); do awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n 'زوش\\|زوس\\|zauša\\|zausa' | sed \"s/^/leaf $l: /\"; done"
}
```


### [2026-10-17T00:31:15.472Z] TOOL RESULT

```
leaf 501: 12: ‫وقلندران‌بندند ‪ ۴‬و بمعنی تند وتیزوسوزندهحم‬                   ‫ومعرب‌آن زندیق است ‪.‬‬               ‫ءد‬
leaf 506: 69:     ‫زوش‌خواندم ترا کههستی زوش»‪ « .‬لفت‌فری*‪٩۱۲‬‏ ‪.‬‬                          ‫بانگ کردمت ای بت سیمین‬
```


## [2026-10-17T00:31:17.766Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==507' BQT_v2_pages.txt | sed -n 55,100p"
}
```


### [2026-10-17T00:31:18.098Z] TOOL RESULT

```
     ‫از بر ‪-‬اخته‌های فرقهٌ آذر کیوان ‪ -‬و ایز اکمتابی است ازین فرقه «درشناختن‬                       ‫‪۴‬‬
     ‫آغاز و انجام وزمان ر جهان وجهایان وشناخت راه نيك از بد و غیرها » کفتار ابراهیم زردشت‬
      ‫پیغمبر ايران (!) ترجمه‌و توضیح آذر پژوه اسپپالی ‪ ۰‬واين کتاب در «آ ین هوشنك » بمال ‪۲۹۲۱‬‬
     ‫‪ - 6‬شهر کی ازحدودنشابور‪«.‬حدودالعالم ‪.*۷۲۵‬‬                       ‫بجاپ سنگی رسده است ‪.‬‬        ‫فمری‌درتهران‬
     ‫‪ - ۱‬درباب اول کلتان (ص‪ ) 84‬آمده‪ « :‬ملك زوزن را خواجه‌ای بود ‪ » ...‬و مراد‬
  ‫پادشاه لاحیت زوزن (فوام الدین از امرای محمد خوارزهشاه) گ«لتان ‪٦۲۲٠‬‏ است ‪ .‬ظاهر ا«ملك‬
            ‫‪ - ۷‬رك ‪ :‬جوجن ‪.‬‬                     ‫زوزن» بکرکاف را ملك زوزن بسکون کاف خوانده‌اند !‬
     ‫طبری ‪ ( 2202‬صدای کر که وشفال) ‪,‬‬                    ‫‪٩‬‏‬          ‫«زونی»(« م‪).‬‬     ‫حف‬
                                                                                      ‫ظ‪۰‬‬‫م_ص‬
                                                                                          ‫‪۸‬‬
     ‫مازندرالی کنوتی ‪ « 212‬واژه نامه ‪ ۰ ۰۱46‬کرماشاهی ‪( 8200‬زوزء سك) « وحدت» کلیایگانی‬
         ‫‪ - ۰‬رك ‪ :‬زاوش ‪.‬‬                 ‫‪.‬یلکی ‪ (8202‬زوزۂ سگ و شغال ) ‪.‬‬
                                                                      ‫نیز ‪« 2200‬قاسمی» ک‬
        ‫‪ _۹‬رك ‪ :‬اسشق؛ حوبشمان‪.۷1٦‬‏ «تند وسخت طبحم ‪ ۰‬رود کی (سمرفندی) کوید ‪:‬‬
     ‫زوش‌خواندم ترا کههستی زوش»‪ « .‬لفت‌فری*‪٩۱۲‬‏ ‪.‬‬                          ‫بانگ کردمت ای بت سیمین‬
     ‫د‪-‬اسم‌مصدر) ؛لقیورتو‪.‬مندی»تواهابی_اعمال زوروفشار ‪:‬‬
                                                      ‫* زورمندی ‪-‬یاز(‪:‬زبورسم‌وندن ‪۳‬‬
  ‫تا دعابی بر آسمان فرود ‪« . .‬کلستان ‪. > ۸6‬‬                               ‫زور مندی مکن بر اهل زمن‬
```


## [2026-10-17T00:31:26.272Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1044 --image 2>&1 | tail -40"
}
```


### [2026-10-17T00:31:26.645Z] TOOL RESULT

```
no scan of BQT covers printed page 1044 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:31:30.250Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==507' BQT_v2_pages.txt | grep -n 'زوش\\|هوبشمان\\|حوبشمان\\|اشتق\\|اسشق'; awk 'BEGIN{RS=\"\\f\"} NR==507' BQT_v2_pages.txt | head -5; grep -n -i 'zauš\\|zaus\\|zōš\\|zosh' ../refs/HUB.txt | head; grep -n -i 'zauša\\|zaoša\\|zausa\\|zaoš' AHM.txt BRT.txt | head"
}
```


### [2026-10-17T00:31:30.727Z] TOOL RESULT

```
68:        ‫‪ _۹‬رك ‪ :‬اسشق؛ حوبشمان‪.۷1٦‬‏ «تند وسخت طبحم ‪ ۰‬رود کی (سمرفندی) کوید ‪:‬‬
69:     ‫زوش‌خواندم ترا کههستی زوش»‪ « .‬لفت‌فری*‪٩۱۲‬‏ ‪.‬‬                          ‫بانگ کردمت ای بت سیمین‬
 ‫‪٩۰ 6‬‬                                                                                              ‫زور زرین‬
 ‫وغرورباشد واین‌لفت‌را درفرهنگه جهانگیری‌زور‬                                                ‫کشتی کوچك را‬
‫دوم اصحیح کرده‌ا ندکهتقدیم‌دال باشدبواو‪ .‬له اعلم‪.‬‬
                                                                                            ‫و کلاحی‬    ‫گومند‬

AHM.txt:1977:opposite meaning, and seek a connection with Oss. (Digor) zust ‘hart, finster, grob’ (Miller-Freiman’s Dictionary, 1, 627), provided, of course, the lattar is not from *e-zusta- (cf. Morg.’s explanation of NPers. 2af ‘vehement, vialent, wicked’ as from *a-szausa-, EVP, 106); cf. Middle krish guss < *ghustu-s, ‘force, violence, anger’, Pokorny, Indagermanisches Wirterbuch, 448? On the other hand, for the epithet avd. zusam (Sth. ‘wearing a jewel’ (?)), which immediately follows afrakatacim, a connectian with P&. zwaz 'naise, clamaur’ may he sug- gested, which Morz., lac. ciz., derives from *zausa-; ‘raising a noise’, with bar-, is reminiscent af the cammon Av, expression vacim bar-, see Bth., W3., 935 sa.
```


## [2026-10-17T00:31:42.754Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /raising a noise/{print \"leaf\",NR-1}' AHM.txt; sed -n 1970,1980p AHM.txt | cut -c1-900; echo; grep -n '^ *71[56]\\. \\|^ *71[56] ' HRN.txt | head; grep -n '71[56]\\.' HUB.txt | head"
}
```


### [2026-10-17T00:31:43.101Z] TOOL RESULT

```
leaf 237
qt. frastacd hamars9a8a, Wi. ‘der hervorstirzt vom Gegner gefalgt’; Gdn. (followed by Bth, and Lo.) ‘den feind im laufe iiberholend’; Da, ‘poursuivant.. .l’ennemi’; Spi. ‘welcher vorwarts stiirzt nachdem er an den Feind sich gehangt hat’; Htl. ‘der, dem Gegner entgegenlaufend, sich an ihn macht’. Far the meaning assumed by Gdn. there is a parallel in Arezd.’amana’s epithet afrakatacim (Yt 19.42), far which Bth.’s translation ‘not running forward (from the caver he had taken)’ is unconvincing; one expects a positive, not a negative quality.} Gdn.’s
t¢ The epithets which precede afrakatacim in Yi 19.42 include frazustam [... Justem (the latter probably a compound of °zustam with a preverb other than
v
fra, cf. Bth., Wo. 429), which have been assigned by Bth. ts the base zus- ‘to like’; Wo. accordingly translates ‘den geliebten’, One would rather expect the
219
71.1-71.2] COMMENTARY
interpretation, Drei Yasht, 26, n. 4, is therefore to be preferred: he took afrakatak- for a bahuvrihi containing *fraka-tak- ‘Zuvorkammer’, hence meaning ‘who has no Zuverkommer, cannot be caught up with’. 7°. stija, Wi. ‘verwundend’ (comparing Gr. arilw, ortyua); W. Geiger, OK, 447, n. 1, ‘spitze Waffe’ (comparing Ved. tigmd, etc.), a view which was revived by Duch., BSOS, 1x, 865; Justi, Spi, Gdn, Da., Bth., Lo., Hth, ‘im, mit, Kampf’, comparing NPers, sit2z. Justi’s interpretation deserves preference over Geiger’s, inasmuch as a ‘pointed weapon’ is unwanted: the bestial treatment meted out to the victim clearly shows that the attacker is the boar, nat Varaérayna, let alone Mithra, as might appear from some translations; the baar’s fangs and
opposite meaning, and seek a connection with Oss. (Digor) zust ‘hart, finster, grob’ (Miller-Freiman’s Dictionary, 1, 627), provided, of course, the lattar is not from *e-zusta- (cf. Morg.’s explanation of NPers. 2af ‘vehement, vialent, wicked’ as from *a-szausa-, EVP, 106); cf. Middle krish guss < *ghustu-s, ‘force, violence, anger’, Pokorny, Indagermanisches Wirterbuch, 448? On the other hand, for the epithet avd. zusam (Sth. ‘wearing a jewel’ (?)), which immediately follows afrakatacim, a connectian with P&. zwaz 'naise, clamaur’ may he sug- gested, which Morz., lac. ciz., derives from *zausa-; ‘raising a noise’, with bar-, is reminiscent af the cammon Av, expression vacim bar-, see Bth., W3., 935 sa.
There is a different *zus-, from which Morgenstierne derived Sanglechi 2d! (ete.} ‘sleeve’, see IZFL, 11, 424, This can Se recognized in Av. 2usa in the Frahang t oim (‘jewel’ according to Bth.), and in Av. frazuf-, epithet of aSfa- ‘gaat’ in Yet 5.126 (quoted note 124%), which is generally thought to mean ‘precious’, As Skt. pra-hasta means ‘long-handed’, cf, Wn., 11, 1, 234, 89 fra- sus- could mean ‘long-sleeved’; cf. A. Waag, Nirangistan, 134, who souzht in aka- a coat with long sleeves. The Pahl. transl. of frazug-, which also accurs in N, looks like fre sew’stk, that of susa in F like xwstwk. Bearing in mind Yidya avldsta ‘sleeve’ < *uda-dasta- (Morz., TFL, 1, 194), and the Pahl. word which Nyberg reads *gpasast and translates ‘Handschutz' (idfsduch des Pehlevi, 1, >. x1), one might read *’wstn% instead of Pahl. xwsiwk, and, with a slight emendation, *wystk instead of xw’sth. *wyst-
220
COMMENTARY [71.2-75.1

6266:715. sntuvff, sittirg 'stark, gross*.
6271:716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
2598:716. Fiir die Volksetymologie {astarvan^ jiid. pers. astar-
```


## [2026-10-17T00:31:53.681Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'zös\\|zôs\\|zōš\\|zoš\\|zös\\b\\|zoh\\b' HRN.txt HUB.txt | head; grep -n -i 'zwaž\\|zwaz\\|zauša' *.txt 2>/dev/null | head; grep -n 'زوش' incoming/ARY/ARY_pages.txt MON_part1.txt MON_part2.txt | head"
}
```


### [2026-10-17T00:31:54.041Z] TOOL RESULT

```
HUB.txt:7309:pah = parh *Waohe*, zoh *Opfer', Sapuh, sah in sahap u. s. w.— 206 -
HUB.txt:7329:zohr Gl. and Ind. 150, arm. zoh 'Opfer, syr. N'imT *Opfer-
HUB.txt:7916:im Armenischen: zoh *Opfer, zur 'ungerecht', zaur 'Heer',
HRN.txt:5962:LW. zoh *Opfer ; ai. hoträ- *üpferhandlung, Opfergabe';
HRN.txt:5965:676. zös 'zornig, grob*.
HRN.txt:5966:aw. zöismi' *unrein (nach Justi); arm. LW. (?) zös
AHM.txt:1977:opposite meaning, and seek a connection with Oss. (Digor) zust ‘hart, finster, grob’ (Miller-Freiman’s Dictionary, 1, 627), provided, of course, the lattar is not from *e-zusta- (cf. Morg.’s explanation of NPers. 2af ‘vehement, vialent, wicked’ as from *a-szausa-, EVP, 106); cf. Middle krish guss < *ghustu-s, ‘force, violence, anger’, Pokorny, Indagermanisches Wirterbuch, 448? On the other hand, for the epithet avd. zusam (Sth. ‘wearing a jewel’ (?)), which immediately follows afrakatacim, a connectian with P&. zwaz 'naise, clamaur’ may he sug- gested, which Morz., lac. ciz., derives from *zausa-; ‘raising a noise’, with bar-, is reminiscent af the cammon Av, expression vacim bar-, see Bth., W3., 935 sa.
SOD_pages.txt:37207:                                                                            zwaz, zuz ©<*uz-waza         =»zywz
SOD.txt:86268:zwaz,  zuz  ©<*uz-waza   =»zywz 
RCH.txt:98683:zcazwaz^  Volatile,  light,  inconstant  (man).  Nimble, active.  One  who  makes  a   peculiar  motion  of  the  hips*  when walking.  Short  in  body.  Name  of  a   bird.
RCH.txt:98686:A   wazwazal  (from  JjJj  a),  Moving  the  hips  in  a   pecu-
MON_part2.txt:42390:تو صسف و تشر یج کرده است؛ مازوشیسم؛ 
MON_part1.txt:23195:بسزوشم: ۲07-1 [- بزوش - بزشم] 
MON_part1.txt:72303:زوش: (قد. 205054 (ص.) تندخو»ه سخت 
MON_part1.txt:72307:زوش: (72۷۷75)20۷75 [ع.] (ص.) , و
```


## [2026-10-17T00:31:56.888Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5960,5972p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /676. zös/{print \"leaf\",NR-1}' HRN.txt; sed -n 72300,72310p MON_part1.txt; grep -n 'zös\\|676' HUB.txt | head"
}
```


### [2026-10-17T00:31:57.230Z] TOOL RESULT

```
i bezw. e im Pehlevl zu belogen, was für die Richtigkeit der obigen
Etymologie spricht.- 150 —
LW. zoh *Opfer ; ai. hoträ- *üpferhandlung, Opfergabe';
arm. vergl. jaimem Veihen, darbringen, opfern', jauni
TsXia(fo()og (H. No. 181).
676. zös 'zornig, grob*.
aw. zöismi' *unrein (nach Justi); arm. LW. (?) zös
*hässlich'.
Die Zusammenstellung ist sehr problematisch, wahr-
scheinlich sogar falsch; aw. zöisnu- ist unsicher
(v. Bradke, KZ. 28, 297 und danach Bartholomae
BB. XV, 11 Anm. 1 nehmen es zweifelnd als
glühend', während Geldner; KZ. 30, 524 es mit
leaf 171
کردن سک و شغال. ناله کردن (مطلقاً) 
موندن: 

زوش: (قد. 205054 (ص.) تندخو»ه سخت 
طبع» بدطبع» خشمگین. صاحب قوت» 
نیر و مند. 

زوش: (72۷۷75)20۷75 [ع.] (ص.) , و 
فرومایه» عبد الگیم. 

زوفا: 225[ع. زوفاء ع. زوفی ‏ زوفه] () 
2471:*) Zur Bedeatang vgl. Horn Nr. 676.
2473:676. Die Zusammenstellung ist sicher falsch, da zd. zQisnu-
```


## [2026-10-17T00:32:01.457Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2468,2480p HUB.txt; sed -n 5972,5980p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /676. Die Zusammenstellung ist sicher/{print \"leaf\",NR-1}' HUB.txt"
}
```


## [2026-10-17T00:32:02.990Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=ISS_alt_DKS.txt; command ls -la $f; grep -n -i 'zīb\\|zeb\\b\\|zēb\\|zēwar\\|zywr\\|zēvar\\|zīvar\\|ysīv\\|āysan\\|aysan' $f | head -30"
}
```


### [2026-10-17T00:32:03.431Z] TOOL RESULT

```
setzt ein zd. ap. "^ziUa- (nicht *juta-) voraus.
675. Lies skr. hotrd- ntr. 'Opferhandlung, Opfergabe.' Arm.
jaunem geh5rt wohl nicht hierher.
*) Zur Bedeatang vgl. Horn Nr. 676.
') YgL die mand&isohe Uebersetzung b9t zainS (NQldeke),— 71 —
676. Die Zusammenstellung ist sicher falsch, da zd. zQisnu-
(= ap.*^a2snw-) im Neup. nur "^zH (oder *zeSan) lauten,
umgekehrt np. »d8 nur auf ein zd. *zaosnU' zuriick-
gehen kdnnte.
677. Dazu pSz. jflk (-for ztk*") Uread' Shk. 252; afgh. LW.
zihglr *die Kerbe am Bogenende zur Befestigung der
Sehne' = np. zihglr,
678. Gegen Noldeke's Deutung ist einzuwenden, dass ap.
glühend', während Geldner; KZ. 30, 524 es mit
zitternd' übersetzt — dazu s. aber Bartholomae,
Indog. Forssch. I, 191 Anm.).
677. zih 'Bogensehne*.
Käs. zeh, ze,
aw. jyd' 'Bogensehne; Sehne* (yt. 10, 70, Geldner,
KZ. 30, 514); ai. i^a-.
kurd. zih 'Bogensehne*; af/. za-l^ bei. j%y (177).
Urform von zih ist "^jtjaka-,
leaf 81
```


### [2026-10-17T00:32:03.504Z] TOOL RESULT

```
<persisted-output>
Output too large (30.5KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bg9a65ybr.txt

Preview (first 2KB):
-rw-r--r-- 1 sfmqrb sfmqrb 3409804 Oct 14 22:19 ISS_alt_DKS.txt
573:avaysána ‘ignorant’, JS 36v3 fere dire myüna атаузййа jaysaña 'good, bad, middling, ignorant, knowing'; K 68:185 avaysüfie udmadi sana, == K 71, gv1-2 avaysāmdye üttamatta уйпа (BS иптӣаа-). Adjective suffix -ya- to *paysüna- ‘knowing’; as also avaysünda- ‘ignorant’, to gaysanda- ‘knowing’.
616:avyüsta- ‘not heard’, K r, 13572 ne auyüstu pyüsde ' hears nottheunheard' ; Z 2:117 nistd avyüstáadáte avaysandà kari tis not unheard, unseen, unknown at all’, See apyiisfa-.
839:Rysün- 'to deck, adorn, equip’, SuvO. 36v3 йузйпййа- 'to be adorned’, BS samalamkartavya-; Z 356, 3 plur. üysdnüre; 3 sing. Z 16:60 üysindà, Z 16:64 aysándá; participle SuvO. 4r; äysätu, BS samalamkrta-, SuvO. 68v2 dysáte; later SuvP. 73r2 ttyau aysya, BS samalamkrtā bhontu, SuvP. бугт aysya amga, BS lalita-indriya-amga-, SuvP. 69v3 laksanyau aysya amga, BS surucira-laksana- anga-; K бо, 37r2 vasue üysye budha-hsettra- ‘pure adorned Buddha-fields' (BS buddha-Rgetra-), SuvP. 72v4 aysyamde, BS asádayantu, Base zai-: zi- ‘to equip’, N.Pers. z&var ‘ornament’, Sogd. zywr; with increment -b- N.Pers. aébidan ' befit', ёрат ' beauty’, Lit. Saib-, 3ieb-, Zibit, Sibéti ' to shine’, Zaibas, 3iebas 'lightning'. Kroraina jheva, seva аз second component, proper name ph'uma- jheva, ph'uma-seva (Т. Burrow, BSOS 7, 1935, 789).
...
</persisted-output>
```


## [2026-10-17T00:32:11.177Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /to deck, adorn, equip/{print \"leaf\",NR-1}' ISS_alt_DKS.txt; grep -n -i -A3 '^dēbāg\\|^debag\\|dēbāg' PHD.txt PHD_mackenzie.txt | head -20; grep -n -i -A2 '^zēb\\|^zēwar\\|zēwar\\|^zeb ' PHD.txt | head -20; grep -n -i 'dēpāk\\|dēpak\\|dypʾk\\|dēbāk\\|zēvar\\|zēwar\\|zēp\\b\\|zēpāk' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:32:11.544Z] TOOL RESULT

```
leaf 39
PHD.txt:1099:brocade dēbāg.
PHD.txt-1100-broken, be ~ ških-; v. break.
PHD.txt-1101-bronze brinj; brinjēn.
PHD.txt-1102-broom gyāg-rēb.
PHD_mackenzie.txt:1959:debag [dyp)k I N deM] brocade.
PHD_mackenzie.txt-1960-              l
PHD_mackenzie.txt-1961-
PHD_mackenzie.txt-1962-debahr [dyp)hll P dybhr] anger.
```


## [2026-10-17T00:32:15.803Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^zeb\\|^zew\\|^zib\\|zewar\\|ornament' PHD_mackenzie.txt | head -20; grep -n -i 'ornament\\|brocade' PHD.txt | head; grep -n -i 'dēpāk\\|dypʾk\\|dyp.k\\|zywl\\|zēwar\\|zēvar\\|zyp\\b' NYB_vol2_glossary.txt | head; grep -n -i 'zywr\\|zyw r' SOD_pages.txt | head"
}
```


### [2026-10-17T00:32:16.259Z] TOOL RESULT

```
3547:mes-sar [myIs)ll N ........] having a sheep's head (ornament).
4163: payrayag [pyl)dk' I M pyr)yg, N periiya] ornament, adornment.
5822:zib [zyh I N zih] bow-string.
7203:ornament payrayag.                        let...., widar(i)dan.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
488:mēš-sār [туї | N ~] having a sheep’s head (ornament).
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
1099:brocade dēbāg.
3003:ornament payrayag.
4269:embarrassment in dealing with these terms. The translator of Vd. 8%, who quite correctly felt that vačpyo is a pass., borrowed the Av. vb. (1322 sg.) vaēp- (otherwise not attested in Milr as far as I know) and formed from it the pass. pt. viftak, then, likewise correctly interpret- ing vaepayö (vačpayant-) as an act., form- ed from viftak the caus. vb. viftén-, but, by assimilating it formally to viftak: vifténitak, created a bizarre mixture of act. and pass. The same curious contra- diction is found in DD, purs. 719-7 which is, however, closer to the Av. original: viftak and vépénitak. Our passage 82° has chosen a mitigating vb. ‘to seduce’, *vr- dip-: MPrth pres. wdyfs- ‘to be cheated’, wdybyšn ‘error, aberration’, wdyb-gr ‘im- postor’, wdyftgyft ‘deceit’, Ghilain 81 sg.; Arm. lw. vrép < *vidép ‘oblique, pervert- ed; fault, error, depravation’; MPrs pres. wyyb- (viyéb- < "videp-), also contracted wyb-, pass. wyfs-, pt. wyft(g), abstr. wyyftgyh = viyiftageh (also wyf-), wdyb *deecit certainly borrowed from NW ; v. Verbum 173. 198; Ps. wydyptk’n "those who have gone astray’. BP wdypt >
4278:viyift or vihift, abstr. vihifiakéh ‘sodomy’ BdA p. 2078, pres. *vidēp- > viyép- > vihep- with the alternation of intervocalic -y-: -h-. This vb. has a so well defined Ablaut-series and ends so clearly in -p that it cannot be combined with Av. (670 sq.) !dab- ‘to deceive’ (against Ver- bum, l. e.). — Anklesaria's second MS has wdyptk w wyhypynytk = viyiftak u vihe- penitak = Paz. vehéfta u vehevnida, thus with two coordinated predicates (against Cod. K) as the Av. text has it, but not with the Av. vbs.
27178:     GMS 200n 1; perf. st. ptzyWr-, BSTii 840.3; JA
36308:         GMS 1060, 1647; pi. zywrkyndy Hen. BSOAS
37158:       102R21, fut. 51R10, pret. 87V 12; impf. zywrt,                          pi. -tl}\ ob. pi. -fy> =»?Ywsk-, jwxsk/q          ?y
37474:                                                                           ziwart (zywrt-) ©impf. =»zw}rt-, zWrt-
37486:                                                                    11612 zywr B, M, S                      x^jjlix^*^ ijyj
37493:                                                                             BBB pl40; MDii, Nov. 3R10 V5 p21; zywrh,
37495:                                                                             VJ 465; zywrt(h), VJ 982; BSTBL, Dhy. 175,
37498:    11602 zyt-3 S(M)                                  Jpj<j=H*      11612 zywrt- =» zyw'rt-
```


## [2026-10-17T00:32:22.207Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 37480,37496p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} /11612 zywr B, M, S/{print \"leaf\",NR-1}' SOD_pages.txt; grep -n -i 'zēwar\\|zewar\\|zēb\\b\\|zeb\\b' PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt | head"
}
```


### [2026-10-17T00:32:22.886Z] TOOL RESULT

```
            Sund. AI 28, 1988, 186
                                                                    11610 zyw'yrt-      B, M, S                          o^Jy.
    11600 zyt-1 M                        j»/jj><*>-1=-.                   zlwert ©impf. =»zw»yrt-
          zlt ©OP dita-\ Av. zinaiti ©pt. St.; pres. zyn-
            =4*zyt-                                                       (/o)make return
            (ro)take away                                                 KG 566; Frag. Len. 93.17
                                                                    11612 zywr B, M, S                      x^jjlix^*^ ijyj
            GMS 750; zytS'r, Hen. JRAS 1944, 137.4; BBB;
                                                                          zewar ©pi. -t(h)
              MDii B-17R 14 pi 17, lsg. perf. >ztyw Srym
                                                                           ornament, necklace
    11601 zyt-2 S                                         jj£              VJ pl24; TSP 5.47, 81, 125; Hen. Cosm. 307.17;
          zit ©pt. St. *^zyt-, jyt-
                                                                             BBB pl40; MDii, Nov. 3R10 V5 p21; zywrh,
            Go)kill
                                                                             VJ 465; zywrt(h), VJ 982; BSTBL, Dhy. 175,
            Anc. Lett. 2.4a, GMS 108n 1
leaf 540
HRN.txt:3592:ter *feucht* Yorliegt ; vielleicht auch nicht in der Phrase ter kerden zebän
HRN.txt:3825:fShem hesi^ der pehl^äm zebän
```


## [2026-10-17T00:32:29.401Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'zeb[aäâ]\\|zebid\\|zevar\\|zewar\\|zēvar\\|zivar\\|zSbä\\|dlbä\\|dibä\\|dībā\\|dēbā\\|debä' HRN.txt HUB.txt | head -20; grep -n -i 'zē[bv]\\|dēbā\\|debag\\|dibaj\\|dībāj' CHEUNG.txt | head"
}
```


### [2026-10-17T00:32:29.698Z] TOOL RESULT

```
HRN.txt:3592:ter *feucht* Yorliegt ; vielleicht auch nicht in der Phrase ter kerden zebän
HRN.txt:3825:fShem hesi^ der pehl^äm zebän
HRN.txt:5299:591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
HRN.txt:13204:' pädebän 267.
```


## [2026-10-17T00:32:32.759Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5299,5312p HRN.txt; grep -n '^591\\.' HUB.txt; grep -n -A5 '^591\\. ' HUB.txt | head; grep -n -i 'zaiba\\|zaib\\b\\|*zai-\\|zēba\\|zēwar\\|zēv' CHEUNG.txt | head"
}
```


### [2026-10-17T00:32:33.132Z] TOOL RESULT

```
591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
phlv. depäk {S«äy. näsäy. 4, i), arm. LW. dipak, syr.
LW. :i2n.
Die Etymologie ist nicht sicher, da im Sanskrit nur
Formen mit T, nie solche mit e vorkommen.
592. dlden 'sehen, dld 'Anblick; sehend', didär,
ap. i^dai-, didiy sehen'; aw. l/'rföi-, a]di^aifi:
phlv. dUan; ai. V^dhäi-, didhye.
kurd. dUin *sehen' ; af/. Udal ; bei. dU, diMr (LW.),
dtdö:^ ^Augapfel'; wa/. didig-am.
593. "des, -dis, -des gleichend, ähnlich*.
aw. dareS' 'Blick* (yt. 19, 94); ai. dfc- *das Sehen;
sehend*, -dfga- '-Aussehen; -sehend*.
ugrep: error: error at position 20
(?mi)zaiba\|zaib\b\|*zai-\|zēba\|zēwar\|zēv
                    \___empty (sub)expression
```


## [2026-10-17T00:32:38.148Z] TOOL CALL #24: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:32:38.157Z] TOOL RESULT

```

```


## [2026-10-17T00:32:40.663Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/giraffe",
 "prompt": "Give the full English etymology of giraffe verbatim."
}
```


## [2026-10-17T00:32:41.403Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D9%87",
 "prompt": "Give the Persian (and Arabic) etymology sections verbatim."
}
```


## [2026-10-17T00:32:42.408Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D9%88%D8%B1",
 "prompt": "Give the Persian etymology verbatim, including Middle Persian, Proto-Iranian and cognates."
}
```


## [2026-10-17T00:32:43.157Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7",
 "prompt": "Give the Persian etymology verbatim."
}
```


## [2026-10-17T00:32:43.852Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%D8%A7",
 "prompt": "Give the Persian etymology verbatim."
}
```


### [2026-10-17T00:32:47.020Z] TOOL RESULT

```
Based on the Wiktionary page provided, I cannot give you the Persian etymology verbatim as requested, because the page does not include Middle Persian, Proto-Iranian, or cognate information.

The page only states that the Urdu term زیور is "Borrowed from Classical Persian _زیور_ (zēwar), related to _زیبیدن_ (zēbīdan)." This mentions a related Persian verb but does not trace the word's deeper historical origins through Middle Persian or Proto-Iranian stages.

To find the complete etymological chain you're seeking, you would need to consult more comprehensive etymological resources beyond this Wiktionary entry.
```


### [2026-10-17T00:32:47.285Z] TOOL RESULT

```
# Persian Etymology of دیبا

According to the Wiktionary entry, the etymology is:

"From Middle Persian dypʾk' (dēbāg, 'brocade'), probably a derivative of Proto-Iranian *diHp- ('to shine, light up'), due to the sheen imparted by gold and silver in traditional brocades."

The entry also notes it is "a doublet of دواج (dawāj / davâj, 'bed-quilt')" and lists related borrowings in Old Armenian, Classical Syriac, and Arabic with similar forms and meanings.
```


### [2026-10-17T00:32:47.528Z] TOOL RESULT

```
# Persian Etymology Section

**Etymology:**
Borrowed from Arabic زُرَافَة (zurāfa), which came from Classical Syriac ܙܪܝܦܐ (zārīp̄ā). The Syriac term derived from ܙܪܢܦܐ (zarnāp̄ā), itself borrowed from Classical Persian زُرْنَاپَا (zurnāpā)—a compound of زُرْنَا (zurnā) plus پَا (pā, meaning "leg").

**Arabic Etymology (referenced):**
The Arabic term زُرَافَة (zurāfa) serves as the source from which Persian borrowed, tracing back through Classical Syriac to Classical Persian origins.
```


### [2026-10-17T00:32:48.141Z] TOOL RESULT

```
# Persian Etymology of زیبا

According to the Wiktionary entry, the etymology is presented as follows:

From "زیب (zib) +‎ ـا (-â). The adjective form of the verb زیفتن (ziftan, 'to deserve, to shine, to have beauty and form.')."

In essence, the word زیبا is formed by combining the root زیب with the suffix ـا, deriving from a verb that conveys meanings related to deserving, shining, and possessing beauty.
```


### [2026-10-17T00:32:48.158Z] TOOL RESULT

```
# English Etymology of Giraffe

According to the Wiktionary entry, the etymology is as follows:

"From Middle French *giraffe*, from Italian *giraffa*, from Arabic زُرَافَة (zurāfa), from Classical Syriac ܙܪܝܦܐ (zārīp̄ā), from Classical Persian زُرْنَاپَا (zurnāpā, literally 'flute-leg')."

The entry notes that this word "Displaced *camelopard*" as the English term for this animal.
```


## [2026-10-17T00:32:55.464Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8",
 "prompt": "Give the Persian etymology verbatim (Middle Persian form, Proto-Iranian, cognates)."
}
```


## [2026-10-17T00:32:56.079Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/giraffe",
 "prompt": "Give the etymology text verbatim."
}
```


## [2026-10-17T00:32:56.994Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B2%D9%88%D8%B4",
 "prompt": "Give the Mo'in dictionary entry for زوش verbatim, including origin tags."
}
```


### [2026-10-17T00:32:57.417Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:32:59.162Z] TOOL RESULT

```
# Mo'in Dictionary Entry for زوش

According to the Mo'in dictionary shown on this page, the entry for زوش contains:

"(ص .)1 - تندخو، خشمگین . 2 - نیرومند"

This provides two definitions: (1) quick-tempered, angry, and (2) strong/powerful. The notation "(ص .)" appears to indicate the source or origin reference in the dictionary format.
```


### [2026-10-17T00:33:01.026Z] TOOL RESULT

```
# Etymology Information for زیب

The Wiktionary page provided does not contain the Persian etymology you requested. The page lists زیب as "present stem of _[زیبیدن](/wiki/%D8%B2%DB%8B%D8%A8%DB%8C%D8%AF%D9%86#Persian)_ (zēbīdan / zibidan, 'to adorn, embellish, beautify')" but does not include Middle Persian forms, Proto-Iranian reconstructions, or cognate information.

To find the detailed etymological information you're seeking, you would need to consult the entry for the root verb زیبیدن (zēbīdan) or specialized etymological references on Persian language origins.
```


## [2026-10-17T00:33:03.481Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian etymology verbatim (Middle Persian form, Proto-Iranian, PIE, cognates)."
}
```


## [2026-10-17T00:33:04.482Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D8%A9",
 "prompt": "Give the Arabic etymology verbatim, including vocalization variants (zurāfa, zarāfa) and any alternative theories."
}
```


## [2026-10-17T00:33:05.191Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/giraffa",
 "prompt": "Give the Italian etymology verbatim, and the French girafe etymology if present."
}
```


### [2026-10-17T00:33:09.064Z] TOOL RESULT

```
# Etymology Information

## Italian Etymology

"Borrowed from Arabic زُرَافَة (zurāfa), borrowed from Classical Syriac ܙܪܝܦܐ (zārīp̄ā), from ܙܪܢܦܐ (zarnāp̄ā), borrowed from Classical Persian زُرْنَاپَا (zurnāpā), from زُرْنَا (zurnā) + پَا (pā)."

## French Etymology

The page indicates that French *girafe* derives from Italian *giraffa* through Middle French *giraffe*, which came from Italian. However, no separate French etymology section is provided on this page—the French entry is only mentioned in the Italian section's descendants list.
```


### [2026-10-17T00:33:10.079Z] TOOL RESULT

```
# Persian Etymology of زیبیدن (zībīdan)

Based on the Wiktionary entry, here's the etymological information:

**Proto-Iranian Origin:**
The word derives from Proto-Iranian "*zay-" meaning "to equip, to adorn," with "no apparent cognates outside of Iranian."

**Related Forms:**
- Connected to زیور (zivar, "ornament")
- Baluchi ázit ("to embellish, adorn") shows a comparable form

**Note on Middle Persian:**
The entry does not explicitly provide a Middle Persian form. It mentions an alternative form زیفتن (ziftan) but traces the etymology directly to the Proto-Iranian root without listing intermediate Middle Persian stages.

**Related Etymology Discussion:**
The entry notes scholarly debate about whether this root connects to other Proto-Iranian "*zay-" forms or to Proto-Balto-Slavic roots with similar meanings like "to shine" or "to wear."
```


### [2026-10-17T00:33:11.927Z] TOOL RESULT

```
# Arabic Etymology of زرافة (Giraffe)

## Primary Etymology

The word زرافة has two documented etymologies:

**Etymology 1 (Animal):** The word is "borrowed from Classical Syriac ܙܪܝܦܐ (zārīp̄ā), variant of ܙܪܢܦܐ (zarnāp̄ā); ultimately from Classical Persian زُرنَاپَا (zurnāpā), a compound of زُرنَا (zurnā, 'flute, zurna') and پَا (pā, 'leg')."

The noun has two vocalization variants:
- **زَرَافَة** (zarāfa)
- **زُرَافَة** (zurāfa)

Both forms are feminine, with plural forms including zarāfā, zurāfā, zarāʔif, and zarāf.

**Etymology 2 (Group):** This sense derives from "the concept of a giraffe being an amalgam of several animals jointly," similar to Persian and Ancient Greek compounds describing the animal's composite appearance. This form pluralizes as zarāfāt.

The word's journey traces through Syriac intermediaries back to Persian origins, where the compound literally means "flute-leg."
```


## [2026-10-17T00:33:24.009Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n 'زیور\\|زیبا\\|دیبا\\|زوش\\|زرافه' ARY_pages.txt | head; grep -n -i 'ZIVAR\\|ZIBA\\|DIBA\\|ZIB\\b' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:33:24.409Z] TOOL RESULT

```
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
45:دیباچه / ۵.
46:دیباچه
101:دیباچه / ۷
156:دیباچه / ‎٩‏ ۱
214:دیباچه / ۱۱
276:دیباچه / ۱۳
337:۱ دیباچه / ۱۵
390:دیباچه / ۱۷
445:دیباچه / ۱۹
10254:hie lp MA CKENZIB: (HEAD) 117 STIRN (GERMAN) gllT
```


## [2026-10-17T00:33:31.089Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'دیبا' 'زیور' 'زیبیدن'; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print NR-1}' BQT_v2_pages.txt | tr '\\n' ' '; echo; done"
}
```


### [2026-10-17T00:33:31.832Z] TOOL RESULT

```
== دیبا
8 16 17 153 240 241 266 271 284 367 368 369 396 455 512 559 582 595 602 
== زیور
31 72 235 366 438 480 527 545 
== زیبیدن
```


## [2026-10-17T00:33:35.912Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 367 368; do awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n 'دیبا\\|دپاک\\|دیپ\\|depak\\|dīp\\|dip\\|هرن\\|هوبشمان' ; echo ----; done; for l in 527 545; do awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n 'زیور\\|زیب\\|zēw\\|zew\\|zēb' | head -8; echo ---; done"
}
```


### [2026-10-17T00:33:36.587Z] TOOL RESULT

```
18:‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
----
7:‫دییاجی ‪ = ۱‬بروزن تیماجی» دیبایاف‬                            ‫اقطه بالف‬    ‫دال ‪۳‬‬    ‫و‬       ‫کشیده و قاف بواو زسده‬
9:‫راگوند بعتی هرچه آزدیبا بافته شده باشد ‪#.‬‬                   ‫را گونند‬    ‫خشخاش‬     ‫‪ ۰‬بلغت عودانی شرت‬             ‫کشده‬
12:‫دیبادین ‪ = ۳‬بفتح اول ودال دیگر بر‬
23:‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬
29:   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
33:   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
36:                                                                                      ‫دیباح است ج‬
38:                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
41:      ‫‪ #‬ویاچه = بکس اول وینجم (درلهجة مر کزی) » از ‪ :‬دیبا( ه‪.‬م‪ +) .‬چە ( توب‬
48:   ‫«دی بآنر» و روز پاتردهم را «دی بمهر» و روز بیت وسوم را «دی بدین» با « دیبا دين » گوشد‬
49:   ‫وکاهی نیز دئوش ( دی) را درفارسی «دین» کفته‌اند و دین‌بآنر ودیبا دين ازشروست ولی‌ترجمة‬
----
44:                                  ‫وبنابرینلفت مزیور زابزان «آسی» (محتملا استی) است ‪.‬‬
---
74:           ‫عروی صبح را زیور بهم بت ‪.‬‬                  ‫ازمشرق سبکدست‬       ‫بر آمد دزدی‬   ‫‪- ۵‬‬
---
```


## [2026-10-17T00:33:40.823Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==369' BQT_v2_pages.txt | sed -n 26,38p"
}
```


### [2026-10-17T00:33:41.221Z] TOOL RESULT

```
  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
       ‫‪4:۲۰ ۶۸‬‬   ‫‪ .‬ورك‪ :‬دزی حاص‬             ‫‪۱۸۱‬‬    ‫(فر) «لك‪۲‬ص‬    ‫‪60062‬‬       ‫‪Ff‬‏ —‬              ‫‪.‬‬    ‫داسشق ‪۰۹۵۰‬‬
   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
  ‫‪ - ۴‬درترکی ‪ :‬شایستگی‪ ,‬خوشبختی؛ ته " پ »ا پابه «جفتابی‬                               ‫م«اللهند ص ‪ ۰۸‬ی ‪٩‬‏ > ‪.‬‬
      ‫* ‪ -‬بهلوی ‪ « 081‬تاوادیا ‪ ۰ ۰۹۱‬از هندی باستان ‪802۷010 . 01 -‬‬                                          ‫‪.‬‬         ‫‪۳‬‬
   ‫‪ .‬رجه اشتقاق آن قطعی ليست‬                        ‫( زبانه کشیدن » پرتو افکندن » درخشیدن) ‪٠‬‏ ارمنی ع‬
   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
  ‫‪ 06.‬است «اسفا ‪ ۲: ۱‬ص ‪ > ۵۷۱ ۰ ۱۷۱‬وآلرا از ربشة‬                            ‫‪06‬‬
                                                                             ‫‪.‬زو اول آن‬
                                                                                      ‫دیباح است ج‬
      ‫‪ ۷001۱ ,‬اکدی گرفته‌اند < فاب ‪۱‬ص ‪> ۲۱۱‬رك‪:‬‬                     ‫تالا سومری (لوحه ‪ .‬خط ) و ا‪00‬‬
                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
```


## [2026-10-17T00:33:49.741Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; python3 $T 'https://en.wiktionary.org/wiki/giraffe' --note 'page 569, root Zarafah: English giraffe etymology chain' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D9%87' --note 'page 569, root Zarafah: Persian zarrafe from Arabic' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D8%A9' --note 'page 569, root Zarafah: Arabic zurafa/zarafa, Syriac/Persian zurnapa theory' ; python3 $T 'https://en.wiktionary.org/wiki/giraffa' --note 'page 569, root Zarafah: Italian giraffa, French girafe' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%DB%8C%D8%AF%D9%86' --note 'page 569, root Zay: zebidan < PIr *zay- adorn' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%D8%A7' --note 'page 569, root Zay: zeba' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D9%88%D8%B1' --note 'page 569, root Zay: zevar related to zebidan' ; python3 $T 'https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7' --note 'page 569, root Zay: diba < MP debag < PIr *diHp- shine' ; python3 $T 'https://vajehyab.com/moein/%D8%B2%D9%88%D8%B4' --note 'page 569, root Zausa: Moin zush tondkhu' 2>&1 | tail -3"
}
```


### [2026-10-17T00:33:53.383Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02186e1c74a5e925.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4b4436f9e220818a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/372ca199893f3163.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5a4898b25defc0e8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4693b54ef4f23311.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cc6b105c7ab83716.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6c1c0fab293bc7f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/68f02d9af94fe136.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0816f5839ea828b1.txt
```


## [2026-10-17T00:33:56.928Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('page-558.json'));print(d['verified_by'],d['verified_on'],list(d['entries'][0].keys()))\"; grep -n 'PROBLEM\\|def \\|required' ../../tools/verify_check.py | head -40"
}
```


### [2026-10-17T00:33:57.352Z] TOOL RESULT

```
claude-opus-5.5 2026-10-16 ['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes']
16:def page_no(path):
20:def main(argv):
90:        print("PROBLEM:", p)
```


## [2026-10-17T00:33:59.695Z] AGENT

Now write the JSON.


## [2026-10-17T00:35:49.280Z] TOOL CALL #42: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-569.json",
 "content": "{\n  \"pdf_page\": 569,\n  \"book_page\": 539,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Zarâfah\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Arabic زَرَافَة zarāfa / زُرَافَة zurāfa 'giraffe' (ultimate origin disputed)\",\n      \"note\": \"The Arabic word, both vocalizations and the gloss are right, and it is undisputed that the European words come from it. The ultimate source is the open question. Nourai's box note ('of an African root') follows Klein and Lokotsch, who suggest a Central-African origin. Current Wiktionary instead derives Arabic zurāfa from Classical Syriac zārīp̄ā / zarnāp̄ā, borrowed from Classical Persian zurnāpā 'flute-leg' (zurnā + pā). On that view the Persian zarrāfe would be a Persian > Syriac > Arabic > Persian round-trip. Devic and Pihan only record the Arabic form, and Pihan's folk derivation from zarafa 'to walk quickly' is not accepted. The root is therefore 'plausible': right as a word, uncertain as an origin.\",\n      \"note_fa\": \"«زرافه» در عربی به دو صورت زَرافة و زُرافة به معنای همین جانور آمده است و همهٔ صورت‌های اروپایی از آن گرفته شده‌اند؛ تا اینجا سخن نورایی درست است. اما ریشهٔ دورتر واژه روشن نیست: کلاین و لوکوچ آن را از زبانی آفریقایی می‌دانند (همان یادداشت نورایی)، و ویکی‌واژه آن را از سریانی zārīp̄ā / zarnāp̄ā و آن را وام از فارسی «زُرناپا» (زرنا + پا، «نی‌پا») می‌گیرد. اگر این نظر درست باشد، «زرافه» در فارسی واژه‌ای است که از فارسی به سریانی و عربی رفته و دوباره به فارسی برگشته است. پس ریشه با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D8%A9\",\n        \"https://en.wiktionary.org/wiki/giraffe\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:657\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 355 (grep '^giraffe,'): 'giraffe, n. — F. girafe, It. giraffa, fr. Arab. zarāfah, which is prob. of African origin. The circumstance that Arab. z has become g (pronounced j) proves that the word came into the European languages through the medium of the Italians.' This supports the Arabic root and the Italian route. The leaf number suggests a printed page in the 680s rather than 657, so the page number may refer to another printing.\"},\n        {\"ref\": \"AHD:558\", \"status\": \"not_checked\", \"note\": \"AHD:558 is a main-dictionary page of the 1975 AHD (not the IE-roots appendix), and that edition is not available locally or online. The Watkins 1985 appendix has no 'giraffe' entry (grep -i giraffe AHD_watkins1985.txt: no hit).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LKT\", \"where\": \"no. 2234, pp. 173-174\", \"stance\": \"supports\", \"note\": \"'2234. Ar. zurāfa: \\\"Giraffe, Camelopardalis giraffa\\\" [sicherlich selbst ein Fremdwort und wie das Tier aus Zentralafrika stammend]; hieraus it. giraffa, frz. girafe, kat. sp. pg. girafa ... engl. ndl. giraffe' (grep 'Giraffe' LKT.txt)\"},\n        {\"src\": \"DEV\", \"where\": \"s.v. Girafe (DEV.txt l.1420)\", \"stance\": \"supports\", \"note\": \"'Girafe. Esp. girafa (ancienn. azorafa), portug. girafa, ital. giraffa ... C'est l'arabe zourâfa, zerâfa. Meninski donne aussi ... sournapâ, zournapâ' (Devic also reports the Persian zurnāpā form)\"},\n        {\"src\": \"PHN\", \"where\": \"s.v. GIRAFE (PHN.txt l.5338)\", \"stance\": \"partial\", \"note\": \"'[zerrâfet], dérivé de [zeref] marcher avec rapidité' (Arabic origin, internal Arabic folk derivation)\"},\n        {\"src\": \"LAM\", \"where\": \"s.v. Girafe (LAM.txt l.4384)\", \"stance\": \"supports\", \"note\": \"'Girafe. Esp: girafa, jirafa (ancienn. azorafa). It: giraffa; de zarâfa, zourâfa'\"},\n        {\"src\": \"SKT\", \"where\": \"s.v. Giraffe (SKT.txt l.7601)\", \"stance\": \"partial\", \"note\": \"'Giraffe ... (F.–Span.–Arab.–Egypt.) ... Arab. zarāf, zarāfa. From Egypt. soraphi, i.e. long neck (Mahn)' (Arabic agreed; Egyptian origin is an obsolete guess)\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"zarrâfeh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian zarrāfe / zarāfe 'giraffe' is the Arabic zarāfa / zurāfa, borrowed with the Arabic tā' marbūṭa rendered as Persian -e (ـه). Mo'in's footnote in Borhan says the same ('از عربی زرافه'). The doubled -rr- in Nourai's transliteration matches the common Persian pronunciation zarrāfe. If the Syriac/Persian zurnāpā theory is right, this is a re-borrowing of an originally Persian coinage.\",\n          \"derivation_fa\": \"«زرافه» در فارسی وام‌واژه‌ای از عربی زَرافة / زُرافة است و تای گرد عربی در فارسی به «ـه» بدل شده است. معین در حاشیهٔ برهان قاطع نیز می‌نویسد «از عربی زرافه». بنا بر نظر ویکی‌واژه، خود واژهٔ عربی از فارسی «زرناپا» از راه سریانی گرفته شده است. وام‌گیری فارسی از عربی قطعی است و ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%81%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1009\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 471 (≈ p.1014; grep 'زرافه'): headword '* زرافه - بفتح اول و چهارم ...' with Mo'in's footnote 'از عربی زرافه ... رک: دزی ج ۱ ص ۷۸۵ ... و ازین زبان وارد ف[رانسه] و انگلیسی giraffe و آلمانی Giraffe شده؛ نوعی از پستانداران ... افریقا'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab (not fetched for this word)\", \"stance\": \"silent\", \"note\": \"Not looked up separately. Mo'in's own Borhan footnote, quoted in ref_check, already gives his view.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'زرافه': no hit (not an IE word)\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2234\", \"stance\": \"supports\", \"note\": \"Ar. zurāfa as the source of the European words; Persian not mentioned\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Italian\",\n          \"words\": \"giraffa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Italian giraffa (attested from the 13th-14th c.) is borrowed from Arabic zarāfa / zurāfa, probably through trade with Egypt and North Africa. Arabic z was rendered by Italian g(i) [dʒ], and Klein takes this as proof that Italian carried the word into the other European languages; Old Spanish azorafa kept the z. Nourai's note on the 'z' to 'j, g' change is correct.\",\n          \"derivation_fa\": \"واژهٔ ایتالیایی giraffa وام از عربی زَرافة است. «ز» عربی در ایتالیایی به صدای «ج» (نوشتهٔ gi) درآمده است، و کلاین همین دگرگونی آوایی را نشانهٔ آن می‌داند که واژه از راه ایتالیایی به دیگر زبان‌های اروپایی رسیده است (اسپانیایی کهن azorafa هنوز «ز» را نگه داشته بود). ادعای نورایی و یادداشت او دربارهٔ ابدال z به j/g درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/giraffa\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 355: 'It. giraffa, fr. Arab. zarāfah ... Arab. z has become g (pronounced j) proves that the word came into the European languages through the medium of the Italians.'\"},\n            {\"ref\": \"AHD:558\", \"status\": \"not_checked\", \"note\": \"1975 AHD main-dictionary page not accessible\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 2234\", \"stance\": \"supports\", \"note\": \"'hieraus it. giraffa, frz. girafe'\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Girafe\", \"stance\": \"supports\", \"note\": \"'ital. giraffa ... C'est l'arabe zourâfa, zerâfa'\"},\n            {\"src\": \"LAM\", \"where\": \"s.v. Girafe\", \"stance\": \"supports\", \"note\": \"'It: giraffa; de zarâfa, zourâfa'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"French\",\n          \"words\": \"girafe\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French girafe (Middle French giraffe, 14th c.) comes from Italian giraffa. Old French had the earlier forms orafle (Joinville) and gerofle (Marco Polo, ed. Pauthier), taken more directly from Arabic (Devic), but they were replaced by the Italian-based form.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی girafe (فرانسوی میانهٔ giraffe) از ایتالیایی giraffa گرفته شده است. در فرانسوی کهن صورت‌های orafle و gerofle هم بوده که از عربی آمده بودند، اما صورت ایتالیایی جای آن‌ها را گرفت. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/giraffa\", \"https://en.wiktionary.org/wiki/giraffe\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 355: 'giraffe, n. — F. girafe, It. giraffa, fr. Arab. zarāfah'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"s.v. Girafe\", \"stance\": \"supports\", \"note\": \"'On trouve en vieux français orafle (Joinville), giraffe; Marco Polo ... écrit gerofle'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2234\", \"stance\": \"supports\", \"note\": \"'frz. girafe'\"},\n            {\"src\": \"PHN\", \"where\": \"s.v. GIRAFE\", \"stance\": \"partial\", \"note\": \"gives the French word directly from Arabic [zerrâfet], with no Italian step\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"giraffe\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English giraffe (late 16th c.; the common name only from the 18th c., replacing camelopard) comes from French girafe / Middle French giraffe, which comes from Italian giraffa and ultimately from Arabic zarāfa.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی giraffe از فرانسوی girafe / giraffe و آن از ایتالیایی giraffa و در نهایت از عربی زَرافة است. این واژه در انگلیسی جای نام کهن‌تر camelopard را گرفت. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/giraffe\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 355: 'giraffe, n. — F. girafe, It. giraffa, fr. Arab. zarāfah'\"},\n            {\"ref\": \"AHD:558\", \"status\": \"not_checked\", \"note\": \"1975 AHD main-dictionary page not accessible\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. Giraffe (l.7601)\", \"stance\": \"partial\", \"note\": \"'Giraffe ... (F.–Span.–Arab.–Egypt.) F. girafe – Span. girafa – Arab. zarāf, zarāfa' (routes via Spanish instead of Italian)\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 4 pronunciation list (FSD_vol4.txt l.63616)\", \"stance\": \"silent\", \"note\": \"'giraffe, ji-raf'' pronunciation only; no etymology found in the OCR\"},\n            {\"src\": \"LKT\", \"where\": \"no. 2234\", \"stance\": \"supports\", \"note\": \"'engl. ndl. giraffe'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Zauša\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Iranian *zauša- 'raising a noise' (Morgenstierne's reconstruction from Pashto zwaž; not attested in Avestan)\",\n      \"note\": \"Nourai's only reference, Gershevitch (AHM p.220, commentary to Yt 10.71), does not give *zauša- as an Avestan word. It is Morgenstierne's reconstruction (EVP) behind Pashto zwaž 'noise, clamour', and Gershevitch only suggests linking it to the Avestan epithet zušəm. So the label 'Avestan' is imprecise: the form is starred Proto-Iranian. Linking NP zōš 'violent, bad-tempered' with it is a possibility discussed on the same page, not an established etymology. Horn 676 offered Av. zōišnu-, and Hübschmann 676 rejected that ('sicher falsch'). Hübschmann noted that np. zōš can only go back to an Avestan-type *zaoš-, which fits *zauša- phonologically.\",\n      \"note_fa\": \"ستاک *zauša- «بانگ برآوردن» واژه‌ای ثبت‌شده در اوستا نیست. این صورت بازسازی مورگنستیرنه برای پشتو zwaž «بانگ، غوغا» است، و گرشویچ (سرود مهر، ص ۲۲۰) فقط پیشنهاد می‌کند که آن را با صفت اوستایی zušəm پیوند دهیم. پس برچسب «اوستایی» دقیق نیست و باید «ایرانی باستانِ بازسازی‌شده» گفت. پیوند «زوش» فارسی با این ستاک از نظر آوایی ممکن است (هوبشمان هم گفته زوش فقط می‌تواند از *zaoš- آمده باشد)، اما قطعی نیست. پس با احتیاط پذیرفتنی است.\",\n      \"sources\": [\"https://vajehyab.com/moein/%D8%B2%D9%88%D8%B4\"],\n      \"ref_check\": [\n        {\"ref\": \"AHM:220\", \"status\": \"partial\", \"note\": \"AHM.txt leaf 237 (= printed p.220+; grep 'raising a noise'): 'for the epithet av. zušəm ... a connection with Pš. zwaž \\\"noise, clamour\\\" may be suggested, which Morg., loc. cit., derives from *zauša-, \\\"raising a noise\\\"'. On the same page (OCR garbled) Morgenstierne's explanation of an NPers. word 'vehement, violent, wicked' as from '*a-zauša-' (EVP 106) is cited. The gloss is Nourai's source, but the form is reconstructed, not Avestan.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"HUB\", \"where\": \"no. 676, p.71 (leaf 81)\", \"stance\": \"partial\", \"note\": \"'676. Die Zusammenstellung ist sicher falsch, da zd. zōišnu- ... im Neup. nur *zēš ... lauten, umgekehrt np. zōš nur auf ein zd. *zaošnu- zurückgehen könnte' (rejects the Avestan comparison; implies a *zaoš- base)\"},\n        {\"src\": \"HRN\", \"where\": \"no. 676, p.150 (leaf 171)\", \"stance\": \"partial\", \"note\": \"'676. zōš \\\"zornig, grob\\\". aw. zōišnu- \\\"unrein\\\" (nach Justi); arm. LW. (?) zōš \\\"hässlich\\\". Die Zusammenstellung ist sehr problematisch, wahrscheinlich sogar falsch'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"ZÔŠ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Early New Persian zōš (Mo'in: archaic 'quick-tempered, harsh-natured, angry; strong'), attested in Rudaki's verse quoted by Nourai and by Asadi's Loghat-e Fors. Old Iranian -auš- regularly becomes NP -ōš (cf. gauša- > gōš 'ear'), so zōš can descend from *zauša-. The semantic chain 'raising a noise' > 'shouting, violent, bad-tempered' is reasonable, but no Middle Persian intermediate is attested. The derivation rests on Morgenstierne's Pashto comparison and is not certain. Horn's older comparison with Av. zōišnu- was rightly rejected by Hübschmann.\",\n          \"derivation_fa\": \"«زوش» در فارسی دری کهن به معنای «تندخو، سخت‌طبع، خشمگین، نیرومند» است (معین) و در بیت رودکی که نورایی آورده و در لغت فرس اسدی هم آمده است. ‎-auš- ایرانی باستان در فارسی نو به ‎-ōš- می‌رسد (مانند gauša- > گوش)، پس «زوش» از نظر آوایی می‌تواند از *zauša- آمده باشد. تحول معنایی «بانگ برآوردن ← پرخاشگر، بدخو» هم پذیرفتنی است. اما صورت فارسی میانه‌ای از این واژه شناخته نیست، و این ریشه‌شناسی تنها بر مقایسهٔ مورگنستیرنه با پشتو zwaž تکیه دارد. هوبشمان پیوندی را که هرن با اوستایی zōišnu- داده بود رد کرده است. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://vajehyab.com/moein/%D8%B2%D9%88%D8%B4\"],\n          \"ref_check\": [\n            {\"ref\": \"AHM:220\", \"status\": \"partial\", \"note\": \"Gershevitch p.220: Pš. zwaž 'noise, clamour' < *zauša- 'raising a noise' (Morgenstierne). The NPers. word is mentioned only via Morgenstierne's '*a-zauša-' (OCR garbled).\"},\n            {\"ref\": \"BQT:1044\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 506 (≈ p.1049; grep 'زوش'): entry glossed «تند و سخت طبع» with Rudaki's verse 'بانگ کردمت ای بت سیمین / زوش خواندم ترا که هستی زوش' and Mo'in's footnote 'رک: اشتق ...؛ هوبشمان ۶۷۶' (OCR gives ۷۱۶). The meaning is confirmed; no Avestan etymon is given.\"},\n            {\"ref\": \"MON:1762\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in s.v. زوش: '(ص.) ۱- تندخو، خشمگین. ۲- نیرومند'. MON_part1.txt l.72303 (2-vol abridgement): 'زوش: (قد. zōš) (ص.) تندخو، سخت طبع، بدطبع، خشمگین، صاحب قوت، نیرومند'. Meaning only, no etymology.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 676 (leaf 171)\", \"stance\": \"partial\", \"note\": \"'zōš \\\"zornig, grob\\\"' — the meaning agrees; Horn himself doubts the Av. zōišnu- comparison\"},\n            {\"src\": \"HUB\", \"where\": \"no. 676 (leaf 81)\", \"stance\": \"partial\", \"note\": \"'np. zōš [kann] nur auf ein zd. *zaošnu- zurückgehen' — consistent with an *zauš- base, rejects zōišnu-\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'زوش': no hit\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Zay, Zi, Âysan\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Proto-Iranian *zay- / *zi- 'to equip, adorn' (Khotanese āysan- 'to adorn')\",\n      \"note\": \"'Indo-Schythian' is the title of Bailey's book (Indo-Scythian Studies). The language is Khotanese Saka, whose verb āysan- 'to deck, adorn' Bailey refers to an Iranian base zai-: zi-. Bailey's Dictionary of Khotan Saka confirms the equation with NP zēvar, Sogd. zywr and, 'with increment -b-', NP zēbīdan / zēbā. Wiktionary likewise has Proto-Iranian *zay- 'to equip, adorn'. The root is sound, but it is Iranian, not a separate 'Indo-Scythian' language, hence 'plausible' for the label. The dībā / dēbāg branch does not belong here: modern sources derive it from *dīp- / *diHp- 'shine' (see node 2). Nourai himself hedges with 'See root Dei'.\",\n      \"note_fa\": \"«Indo-Schythian» نام کتاب بیلی (پژوهش‌های هندوسکایی) است. زبانِ مورد نظر ختنی (سکایی) است که فعل āysan- «آراستن» را دارد، و بیلی آن را از ستاک ایرانی zai-: zi- «آراستن، تجهیز کردن» می‌داند. فرهنگ سکایی ختنی بیلی و ویکی‌واژه هر دو «زیور»، سغدی zywr و (با افزودهٔ ‎-b-) «زیبیدن» و «زیبا» را از این ریشه می‌دانند. پس خود ریشه درست است، ولی ریشه‌ای ایرانی است و نه «زبان هندوسکایی». شاخهٔ «دیبا» به این ریشه تعلق ندارد.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%DB%8C%D8%AF%D9%86\"],\n      \"ref_check\": [\n        {\"ref\": \"ISS:16\", \"status\": \"not_checked\", \"note\": \"Indo-Scythian Studies (Khotanese Texts VI) is not online. The substitute, Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt leaf 39, s.v. āysān-), says: 'āysān- \\\"to deck, adorn, equip\\\" ... Base zai-: zi- \\\"to equip\\\", N.Pers. zēvar \\\"ornament\\\", Sogd. zywr; with increment -b- N.Pers. zēbīdan \\\"befit\\\", zēbā \\\"beauty\\\", Lit. žaib-, žieb-, žibėti \\\"to shine\\\"' — the same material as Nourai's chart (minus dēbāg).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"ISS_alt_DKS\", \"where\": \"leaf 39 s.v. āysān-\", \"stance\": \"supports\", \"note\": \"'Base zai-: zi- \\\"to equip\\\", N.Pers. zēvar \\\"ornament\\\", Sogd. zywr'\"},\n        {\"src\": \"POK\", \"where\": \"POK_full.txt\", \"stance\": \"silent\", \"note\": \"no Iranian *zay- 'adorn' entry located (Wiktionary: 'no apparent cognates outside of Iranian')\"},\n        {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'زیور', 'زیبا': no headword hit\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"zîb; zîbîdan; zîvar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP zēb (present stem of zēbīdan / zēftan 'to befit, adorn') and the adjective zēbā (zēb + -ā) go back to Iranian *zai-b- / *zai-p-, the root *zay- 'equip, adorn' extended by -b- (Bailey). NP zēvar 'ornament' (MP / Manichaean zēwar) continues *zai-bara- or *zai-war-, with the same root; its exact cognate is Sogdian zywr zēwar 'ornament, necklace'. NP ē merged with ī, hence modern zib, zivar. Wiktionary cites Baluchi āzit 'to adorn' as a further cognate.\",\n          \"derivation_fa\": \"«زیب» ستاک حال «زیبیدن / زیفتن» و «زیبا» (زیب + ـا) از ایرانی باستان *zai-b- است، یعنی ریشهٔ *zay- «آراستن، تجهیز کردن» با افزودهٔ ‎-b- (بیلی). «زیور» (فارسی میانهٔ zēwar) هم از همین ریشه است و هم‌ریشهٔ دقیق آن سغدی zywr (zēwar) «زیور، گردن‌بند» است. «ای مجهول» (ē) فارسی میانه در فارسی نو به «ای» (ī) بدل شده است. ادعای نورایی درست است (بیلی، ویکی‌واژه).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:16\", \"status\": \"not_checked\", \"note\": \"ISS itself not online. The DKS substitute (leaf 39) supports it: 'N.Pers. zēvar \\\"ornament\\\", Sogd. zywr; with increment -b- N.Pers. zēbīdan \\\"befit\\\", zēbā \\\"beauty\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"leaf 39 s.v. āysān-\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check\"},\n            {\"src\": \"SOD\", \"where\": \"no. 11612 (SOD_pages.txt leaf 540)\", \"stance\": \"supports\", \"note\": \"'11612 zywr B, M, S zēwar ... ornament, necklace' (Sogdian cognate of zēvar)\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt\", \"stance\": \"silent\", \"note\": \"grep 'zēb/zebā/zēvar': no entry found in the OCR\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt\", \"stance\": \"silent\", \"note\": \"no zēb/zēwar headword. MacKenzie lists 'ornament payrāyag' (l.7203) instead\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"děpâk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Pahlavi dypʾk is real: MacKenzie reads it dēbāg 'brocade' (older reading dēpāk; Arm. LW dipak, Syr. LW, Arab. dībāj). It has nothing to do with *zay- 'adorn': Pahlavi d- cannot come from Iranian *z-. Horn, Mo'in and Wiktionary all derive it from *dīp- / *diHp- 'to shine' (Skt. dīp-), from the sheen of gold- and silver-shot brocade. Horn and Mo'in mark even this as uncertain. The chart's own note (BQT:908, Skt. dīp- 'to shine') and the cross-reference to root 'Dei' state the better derivation. Placing the word under Zay is the error.\",\n          \"derivation_fa\": \"واژهٔ پهلوی dypʾk درست است. مکنزی آن را dēbāg «دیبا» می‌خواند (خوانش کهن‌تر dēpāk؛ ارمنی dipak، سریانی و عربی «دیباج» وام از آن‌اند). اما این واژه به ریشهٔ *zay- «آراستن» ربطی ندارد، چون «ز» ایرانی هرگز در پهلوی «د» نمی‌شود. هرن، معین و ویکی‌واژه آن را از ریشهٔ *dīp- / *diHp- «درخشیدن» (سنسکریت dīp-) می‌دانند، به سبب درخشش رشته‌های زر و سیم در دیبا، هرچند هرن و معین این را هم قطعی نمی‌دانند. پژوهش امروزی جای دادن این واژه زیر ریشهٔ Zay را رد می‌کند. یادداشت خود نورایی (سنسکریت dīp و ارجاع به ریشهٔ Dei) به نظر درست نزدیک‌تر است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\"],\n          \"ref_check\": [\n            {\"ref\": \"ISS:16\", \"status\": \"not_checked\", \"note\": \"ISS not online. The DKS substitute (leaf 39, s.v. āysān-) lists zēvar, zēbīdan, zēbā under base zai- but does NOT include dēbāg.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt l.1959 / PHD.txt l.312\", \"stance\": \"partial\", \"note\": \"'dēbāg [dyp'k | N dēbā] brocade' — the word and meaning are confirmed; no etymology given\"},\n            {\"src\": \"HRN\", \"where\": \"no. 591, p.135\", \"stance\": \"contradicts\", \"note\": \"'591. dēbā, dēbāh \\\"Brokat\\\", arab. dībāj ... ai. √dīp-, dīpyate \\\"flammen, strahlen, glänzen\\\"; phlv. dēpāk ..., arm. LW. dipak, syr. LW. Die Etymologie ist nicht sicher' (√dīp-, not *zay-)\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"grep 'dypʾk/dēpāk/dēbāg': no hit in OCR\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"dîbâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP dībā / dēbā (also dēba, dībah) 'brocade, coloured silk cloth' continues MP dēbāg: final -āg becomes NP -ā, and ē becomes ī in modern Persian. Arabic dībāj (معرب) was borrowed from the Middle Persian form with -g > -j, and dībāje 'preface' (literally 'brocaded front') belongs with it. Wiktionary also calls davāj 'bed-quilt' a doublet. The Pahlavi > Persian step is correct; only the attachment of the whole branch to root Zay is wrong (see node 2).\",\n          \"derivation_fa\": \"«دیبا» (و «دیبه»، «دیباه») از فارسی میانهٔ dēbāg است. پسوند ‎-āg در فارسی نو به ‎-ā بدل شده و ē به ī. صورت معرّب آن «دیباج» است که از صورت فارسی میانه با بدل شدن g به ج گرفته شده، و «دیباچه» هم از همین واژه است. ویکی‌واژه «دواج» را دوگانهٔ آن می‌داند. گذر از پهلوی به فارسی درست است (معین، هرن)، ولی چنان‌که گفته شد این شاخه زیر ریشهٔ Zay جای ندارد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:908\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 368 (≈ p.911; grep 'دیبا'): Mo'in's footnote 'پهلوی dēpāk (تاوادیا ...) از هندی باستان dīp- (زبانه کشیدن، پرتو افکندن، درخشیدن)، ارمنی dipak ... وجه اشتقاق آن قطعی نیست (اشتق ۵۹۱) در فارسی = دیباه، دیبه؛ و دیباچه ... نیز از همین ریشه است، معرب آن دیباج است'. This supports Pahlavi > Persian and the dīp- etymology (Nourai's note), not Zay.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 591\", \"stance\": \"supports\", \"note\": \"'dēbā, dēbāh \\\"Brokat\\\", arab. dībāj ... phlv. dēpāk' (Persian < Pahlavi confirmed)\"},\n            {\"src\": \"PHD\", \"where\": \"l.1959\", \"stance\": \"supports\", \"note\": \"'dēbāg [dyp'k | N dēbā] brocade'\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'دیبا' gives only 'دیباچه' (Aryanpur's preface), no headword\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"zywr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian zywr, read zēwar 'ornament, necklace', is attested in Buddhist, Manichaean and Christian Sogdian (Gharib no. 11612, with derivatives zywrt-, zywrh). It is the exact cognate of NP zēvar / MP zēwar and continues Iranian *zai-war- / *zai-bara- from *zay- 'adorn' (Bailey).\",\n          \"derivation_fa\": \"سغدی zywr (خوانده zēwar) «زیور، گردن‌بند» در متن‌های بودایی، مانوی و مسیحی سغدی آمده است (قریب، شمارهٔ ۱۱۶۱۲). این واژه هم‌ریشهٔ دقیق «زیور» فارسی و zēwar فارسی میانه است و از ریشهٔ ایرانی *zay- «آراستن» می‌آید (بیلی). ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%A8%DB%8C%D8%AF%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"ISS:16\", \"status\": \"not_checked\", \"note\": \"ISS not online. The DKS substitute (leaf 39) supports it: 'N.Pers. zēvar \\\"ornament\\\", Sogd. zywr'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"no. 11612 (SOD_pages.txt leaf 540)\", \"stance\": \"supports\", \"note\": \"'11612 zywr B, M, S ... zēwar ... ornament, necklace ... VJ p124; TSP 5.47 ...'\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"leaf 39 s.v. āysān-\", \"stance\": \"supports\", \"note\": \"'Sogd. zywr' listed under base zai-\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:35:49.320Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-569.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:36:01.316Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -i \"s/هوبشمان ۶۷۶' (OCR gives ۷۱۶)/هوبشمان ۷۱۶' as OCRed, probably ۶۷۶ = Hübschmann no. 676 on zōš/; s/'زوش: (قد. zōš) (ص.)/'زوش: (قد. [Latin garbled in OCR]) (ص.)/\" data/verification/page-569.json; python3 -m json.tool data/verification/page-569.json >/dev/null && python3 tools/verify_check.py 569"
}
```


### [2026-10-17T00:36:01.828Z] TOOL RESULT

```
nodes verified: 9/9
node verdicts: {'confirmed': 7, 'plausible': 1, 'disputed': 1}
root verdicts: {'plausible': 3}
ref checks: {'supports': 7, 'not_checked': 5, 'partial': 1}
books consulted: {'silent': 8, 'supports': 13, 'partial': 5, 'contradicts': 1} | by book: {'LKT': 4, 'HRN': 4, 'ARY': 3, 'PHD': 3, 'DEV': 2, 'ISS_alt_DKS': 2, 'SOD': 2, 'MON': 1, 'LAM': 1, 'PHN': 1, 'SKT': 1, 'FSD': 1, 'HUB': 1, 'NYB': 1}
```


## [2026-10-17T00:36:05.275Z] TOOL CALL #44: Bash

```json
{
 "command": "grep -c 'probably ۶۷۶\\|Latin garbled' /home/sfmqrb/git/rishe-private/data/verification/page-569.json"
}
```


### [2026-10-17T00:36:05.574Z] TOOL RESULT

```
2
```


## [2026-10-17T00:36:14.873Z] TOOL CALL #45: SubagentHandback

```json
{
 "message": "I verified page 569 (book page 539) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-569.json`. It is valid JSON, and `verify_check.py 569` reports 0 PROBLEM lines.\n\n- **Nodes:** 9 of 9 checked. 7 confirmed, 1 plausible, 1 disputed, 0 transcription_suspect.\n- **Roots:** 3 of 3 plausible.\n  - Zarâfah: the Arabic word is right. Its deeper origin is open: Klein and Lokotsch say African, while Wiktionary says it came via Syriac from Persian zurnāpā \"flute-leg\".\n  - Zauša: not an attested Avestan word. It is Morgenstierne's reconstructed *zauša- (from Pashto zwaž \"noise\"), as cited by Gershevitch on p.220. That makes Persian zōš only plausible.\n  - Zay/Zi/Âysan: the root is real, but it is Proto-Iranian *zay- \"adorn\" (Bailey); \"Indo-Schythian\" is the title of Bailey's book, not a language.\n- **Disputed:** Zay / Pahlavi děpâk (dēbāg \"brocade\"). It cannot come from *zay-, because Iranian z- never becomes Pahlavi d-. Horn no. 591, Mo'in's note in Borhan and Wiktionary all derive it from *dīp- \"to shine\". The chart's own note (Sanskrit dīp-, \"see root Dei\") already points to the better derivation. The step dēbāg → dībā itself is confirmed.\n- **Extraction errors:** none found.\n- **Not checkable:** Nourai's ISS:16 and AHD:558 are not available. For ISS I used Bailey's Dictionary of Khotan Saka instead; its entry āysān- confirms zēvar, zēbīdan, zēbā and Sogdian zywr under the base zai-.\n- **Page-number drift:** Klein's giraffe entry sits near printed page 686, not 657. The Borhan entries are about 5 pages off (zarrāfe ≈ 1014, zōš ≈ 1049, dībā ≈ 911)."
}
```


### [2026-10-17T00:36:15.139Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
