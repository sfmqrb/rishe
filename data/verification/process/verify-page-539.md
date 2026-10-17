# Verification process log — verify-page-539


## [2026-10-17T00:00:15.199Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 539 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-539.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-539.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-539.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 539` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.256Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:31.616Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:31.635Z] TOOL RESULT

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


## [2026-10-17T00:00:32.117Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-539.txt"
}
```


### [2026-10-17T00:00:32.132Z] TOOL RESULT

```
1	=== PDF page 539 (book page 509) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wel 1 : to wish, desire  (refs POK:1137)
4	#1 (parent #0) [Avestan] refs=POK:1137; DVS:198 | var 2, ver 1, varena : to wish ; upa-var : to believe ☞Upo ; adi-var : in truth ☞En ; xšatra-vairya : desired city, heavenly country ☞Ksei 1
5	  #2 (parent #1) [Pahlavi] refs=BQT:1316,1303 | varavistan : to believe ; paver : belief ; ěvar : indeed ; šatri-var : name of a month
6	    #3 (parent #2) [Persian] refs=BQT:1316,1803; HRN:203; MON:2098 | geravîdan «گرویدن» : to believe ; bâvar «باور» : belief ; ârî «آری» : yes, indeed ; Šahrîvar «شهریور» : name of a Persian month, also the forth day of each month | NOTE: See "Wer 1" for another possible root of "bâvar"
7	#4 (parent #0) [Sogdian] refs=SOD:412 | wrn : belief
8	#5 (parent #0) [Germanic] refs=AHD | 
9	  #6 (parent #5) [English] refs=AHD | well 1 : good ; wealth, will, William
10	#7 (parent #0) [Latin] refs=AHD | velle, vol : desire
11	  #8 (parent #7) [English] refs=None | volunteer
12	
```


## [2026-10-17T00:00:32.677Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-539.json"
}
```


### [2026-10-17T00:00:32.705Z] TOOL RESULT

```
1	{
2	  "pdf_page": 539,
3	  "book_page": 509,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wel 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1137",
10	        "gloss": "to wish, desire"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1137; DVS:198",
18	          "words": [
19	            {"translit": "var 2, ver 1, varena", "gloss": "to wish", "script": null},
20	            {"translit": "upa-var", "gloss": "to believe", "script": null, "see": ["Upo"]},
21	            {"translit": "adi-var", "gloss": "in truth", "script": null, "see": ["En"]},
22	            {"translit": "xšatra-vairya", "gloss": "desired city, heavenly country", "script": null, "see": ["Ksei 1"]}
23	          ],
24	          "note": null,
25	          "quote": null
26	        },
27	        {
28	          "id": 2,
29	          "parent": 1,
30	          "lang": "Pahlavi",
31	          "refs": "BQT:1316,1303",
32	          "words": [
33	            {"translit": "varavistan", "gloss": "to believe", "script": null},
34	            {"translit": "paver", "gloss": "belief", "script": null},
35	            {"translit": "ěvar", "gloss": "indeed", "script": null},
36	            {"translit": "šatri-var", "gloss": "name of a month", "script": null}
37	          ],
38	          "note": null,
39	          "quote": null
40	        },
41	        {
42	          "id": 3,
43	          "parent": 2,
44	          "lang": "Persian",
45	          "refs": "BQT:1316,1803; HRN:203; MON:2098",
46	          "words": [
47	            {"translit": "geravîdan", "gloss": "to believe", "script": "گرویدن"},
48	            {"translit": "bâvar", "gloss": "belief", "script": "باور"},
49	            {"translit": "ârî", "gloss": "yes, indeed", "script": "آری"},
50	            {"translit": "Šahrîvar", "gloss": "name of a Persian month, also the forth day of each month", "script": "شهریور"}
51	          ],
52	          "note": "See \"Wer 1\" for another possible root of \"bâvar\"",
53	          "quote": {"text": "به شهریور بهمن از بامداد - جهاندار داراب را بار داد", "poet": "Ferdowsî"}
54	        },
55	        {
56	          "id": 4,
57	          "parent": 0,
58	          "lang": "Sogdian",
59	          "refs": "SOD:412",
60	          "words": [
61	            {"translit": "wrn", "gloss": "belief", "script": null}
62	          ],
63	          "note": null,
64	          "quote": null
65	        },
66	        {
67	          "id": 5,
68	          "parent": 0,
69	          "lang": "Germanic",
70	          "refs": "AHD",
71	          "words": [],
72	          "note": null,
73	          "quote": null
74	        },
75	        {
76	          "id": 6,
77	          "parent": 5,
78	          "lang": "English",
79	          "refs": "AHD",
80	          "words": [
81	            {"translit": "well 1", "gloss": "good", "script": null},
82	            {"translit": "wealth, will, William", "gloss": null, "script": null}
83	          ],
84	          "note": null,
85	          "quote": null
86	        },
87	        {
88	          "id": 7,
89	          "parent": 0,
90	          "lang": "Latin",
91	          "refs": "AHD",
92	          "words": [
93	            {"translit": "velle, vol", "gloss": "desire", "script": null}
94	          ],
95	          "note": null,
96	          "quote": null
97	        },
98	        {
99	          "id": 8,
100	          "parent": 7,
101	          "lang": "English",
102	          "refs": null,
103	          "words": [
104	            {"translit": "volunteer", "gloss": null, "script": null}
105	          ],
106	          "note": null,
107	          "quote": null
108	        }
109	      ]
110	    }
111	  ]
112	}
113	
```


## [2026-10-17T00:00:40.746Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','DVS','BQT','HRN','MON','SOD','AHD','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HUB','CHEUNG','ARY','KLN','SKT']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:00:41.210Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
DVS {"title": "P. Davies, Roots: Family Histories of Familiar Words, McGraw-Hill 1981", "edition_found": "1981 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsfamilyhisto0000davi (lending)", "identifier": "rootsfamilyhisto0000davi", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 202
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-10-17T00:00:46.722Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -l -E 'bâvar|geravîdan|Šahrîvar|ârî' page-*.json | head; python3 - <<'E'\nimport json,glob\nfor f in sorted(glob.glob('page-*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            w=n.get('words','')\n            if any(k in w for k in ['bâvar','geravîdan','Šahrîvar','ârî','varavistan','wrn','volunteer','William']):\n                print(f,e['root'],n['id'],w[:80],n['verdict'])\nE"
}
```


### [2026-10-17T00:00:47.509Z] TOOL RESULT

```
page-128.json
page-121.json
page-154.json
page-156.json
page-190.json
page-189.json
page-211.json
page-216.json
page-242.json
page-245.json
page-121.json Deru 1 3 dârîyeh disputed
page-128.json Dher 1 12 Dârîuš «داریوش»; dârâbgard «دارابگرد» (extra: دارا ، داراب) plausible
page-154.json En; Ndher, Ndhos, Ndhi 8 îstâdan; ârî disputed
page-156.json Er 1, Or 11 ârîğ «آریغ ، أَریغ»; rîğ «ریغ» plausible
page-189.json Gher 4 5 hortârî confirmed
page-190.json Gherto 2 âğâr «آغار»; âğârîdan «آغاریدن»; âğeštan «آغشتن»; âğar «آغر» plausible
page-190.json Gherto 3 farğârîdan «فرغاریدن ، فرغردن»; farğâr «فرغار»; farğar «فرغر»; farğan «فرغن»; fa plausible
page-211.json Gwhder 2 šârîdan confirmed
page-216.json Gwher 12 fer «فِر ٢» ; forn «فُرن» ; fârîneh «فارینه ( فرنی ، فُرنیه )» disputed
page-242.json Kar 1, Qar 1, Quseros, Qhar; Karkar, Kongar 27 xârîdan «خاریدن» disputed
page-273.json Korkâ 13 sâxârîn «ساخارین» (extra: سوخاری) disputed
page-290.json Kwel, Qwel 14 kâštan «کاشتن»; kârîdan 1 «کاریدن ۱» (extras: کِشتن ، کِشت ، کشاورز ، کار ۳) confirmed
page-292.json Kwer, Qwer 2 kârîdan 2; gar 2; kahr-mân disputed
page-298.json Kwon, Ka 2, Sua 17 qanârî «قناری» confirmed
page-329.json Mel 2, Melo, Smelo 6 mâlârîyâ «مالاریا» confirmed
page-345.json Murvârît 1 morvârîd confirmed
page-398.json Perk 1 7 precârî; prex confirmed
page-44.json Akwa 9 âkvârîŭm «آکواریوم»; odokolon «ادوکلن ( ادکلن )» confirmed
page-451.json Skai 9 senârîo «سناریو» plausible
page-486.json Su 1, Esu, Wesu 6 Ordîbehešt «اردیبهشت»; Dârîuš «داریوش» plausible
page-519.json Upo 5 padîd; pasand; bâvar; bedrŭd; pegâh; penhân disputed
page-526.json Wě 1, Aŭe 1 20 mâlârîyâ confirmed
page-527.json Wed, Wer 4, Aŭe 2, Ud 2 2 vârân, vârîtan confirmed
page-73.json Awar 1 `awâr, `awârîyah confirmed
page-80.json Bhâ 2 5 fârî confirmed
```


## [2026-10-17T00:00:53.503Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'E'\nimport json\nfor f,eid,ids in [('page-519.json','Upo',[5]),('page-154.json','En',[8]),('page-486.json','Su 1',[6])]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        if e['root'].startswith(eid):\n            for n in e['nodes']:\n                if n['id'] in ids:\n                    print(f, json.dumps(n,ensure_ascii=False,indent=1)[:5000]); print('-----')\nE"
}
```


### [2026-10-17T00:00:53.973Z] TOOL RESULT

```
page-519.json {
 "id": 5,
 "lang": "Persian",
 "words": "padîd; pasand; bâvar; bedrŭd; pegâh; penhân",
 "verdict": "disputed",
 "derivation": "padīd 'visible' < MP pad dīd 'in sight' (Nyberg; Hübschmann: 'erst im Mittelpers. componirt aus pa und dīt'), not Av. *upa-dīti. pasand 'liking' < MP passand < *pati-sand- (Wiktionary, Nyberg, MacKenzie; Cheung's *sand 'seem'). bāvar 'belief' < MP wābar < upā + var- 'choose/believe' (Horn, Wiktionary) - plausible, though Nyberg prefers reduplicated *vā-vara-. bedrūd/padrūd 'farewell' < pa + drōd 'health' (MP drōd < *druvatāt-), Wiktionary 'be + dorud'. pegāh 'early morning' < pa + gāh 'time' ('betimes', Hübschmann/Nöldeke; Mo'in '= بگاه، بهنگام'). penhān 'hidden' < MP pad + nihān (Wiktionary; Horn himself 'phlv. pa nihān'). Five of six words therefore come from *pati-, not upa; worst verdict disputed.",
 "derivation_fa": "«پدید» از فارسی میانهٔ pad dīd «در دید» است؛ «پسند» از passand و ایرانی باستان *pati-sand-؛ «بدرود / پدرود» از pa + drōd «تندرستی»؛ «پگاه» از pa + gāh «به‌گاه، بهنگام»؛ و «پنهان» از pad + nihān. پس پیشوند همهٔ این‌ها pa- (از *pati-) است نه upa. تنها «باور» (فارسی میانه wābar) را می‌توان با هرن و ویکی‌واژه از upā + var- «برگزیدن، باور داشتن» دانست، هرچند نیبرگ صورت دوتایی *vā-vara- را ترجیح می‌دهد. هوبشمان همان زمان سخن هرن را درباره «پدید» و «پگاه» رد کرده بود.",
 "sources": [
  "https://en.wiktionary.org/wiki/پدید",
  "https://en.wiktionary.org/wiki/پسند",
  "https://en.wiktionary.org/wiki/باور",
  "https://en.wiktionary.org/wiki/بدرود",
  "https://en.wiktionary.org/wiki/پنهان",
  "https://en.wiktionary.org/wiki/پگاه"
 ],
 "ref_check": [
  {
   "ref": "BQT:373",
   "status": "partial",
   "note": "BQT_v1_pages.txt leaf 597 (≈p.373) s.v. پدید: Mo'in's footnote 'پهلوی ... کارنامه ... اوستا ... نیبرگ پهلوی آنرا ... نوشته ... آشکار' - gives the Pahlavi pad-dīd form; OCR rough."
  },
  {
   "ref": "BQT:406",
   "status": "not_found",
   "note": "leaf ≈632 not clearly matched; پگاه appears as 'بگه ... مخفف بگاه است که سحر و صبح باشد' at leaf 640 (≈p.414), i.e. be-gāh."
  },
  {
   "ref": "BQT:2230",
   "status": "not_found",
   "note": "ref_page.py BQT:2230 (vol.4 pdf 313) shows نیک / نیکو entries; نهان is at pdf 296-297 (≈p.2213-2214)."
  }
 ],
 "consulted": [
  {
   "src": "HUB",
   "where": "p. 42-43, notes to Horn nos. 289, 324 (HUB.txt l.1268-1276, 1440-1446)",
   "stance": "contradicts",
   "note": "'289. Streiche die Worte: \"also aw. *upadīti-\" ... Das Wort padīd sichtbar ist erst im Mittelpers. componirt aus pa und dīt = \"in Sicht\" wie padrūd aus pa und drūt'; '324. Np. pagāh ... kann weder = zd. *upakasa- noch = zd. *paitikāsa- gesetzt werden, sondern wird am besten mit Nöldeke als mp. Neubildung aus pa und gāh \"Zeit\"... gefasst'"
  },
  {
   "src": "NYB",
   "where": "vol. II s.v. dīt, passand, vāvarīkānēh (l.1293, 2990, 3938)",
   "stance": "contradicts",
   "note": "'NP padid'; 'NP pasand; < *pat-sand-'; for vāvar: '*vā-vara- \"choice\" ... from Av. var-, pres. vāvar-'."
  },
  {
   "src": "PHD",
   "where": "s.v. passand, paydāg, nihān, drōd (l.4087, 4135, 3762, 2066)",
   "stance": "partial",
   "note": "'passand [psnd | N pasand] pleasure, liking'; 'nihān [nyhʾn] concealment, secrecy'; 'drōd ... health, well-being' - components of pa-compounds; no upa."
  },
  {
   "src": "MON",
   "where": "2-vol. Mo'in (MON_part1.txt l.32365, 21615)",
   "stance": "supports",
   "note": "'پگاه ... [= بگاه، بهنگام] صبح' and 'بدرود [= پدرود] سلامت' - support pa/be + gāh, be + drūd."
  },
  {
   "src": "HRN",
   "where": "pp.41,65,71-73",
   "stance": "partial",
   "note": "Horn's upa-derivations (see ref_check); for penhān he himself gives 'phlv. pa nihān'."
  }
 ]
}
-----
page-154.json {
 "id": 8,
 "lang": "Persian",
 "words": "îstâdan; ârî",
 "verdict": "disputed",
 "derivation": "Both Persian words are real. ایستادن īstādan 'to stand' is Middle Persian ēstādan (ideogram YKʿYMWN-tnʹ), Horn's 'ēstaden, später istāden'; آری ārī 'yes, indeed' is Horn's no. 16, which he traces to Pahlavi ēvar. The arrow from this root, however, is what modern work rejects for īstādan: Cheung (EDIV 2007) files the Middle Persian verb under *staH with the prefix *abi- (→ ē-), and Wiktionary, following MacKenzie 1971 and Cheung, gives ایستادن < MP ēstādan < Proto-Iranian *staH < PIE *steh₂- with no *adi- and no connection to *h₁en. The prefix is the whole of Nourai's claim here, so the link to En/Ndhi falls with it. For آری the position is weaker still: Wiktionary's entry does derive it from MP ēwar < 'Old Persian adi-var', but it cites Nourai, An Etymological Dictionary, page 124 — this very page — so it is not independent confirmation; the only real authority is Horn's own conjecture of 1893, and Nyberg gives the New Persian reflex of ēvar as āvar, not ārī. آری is therefore 'plausible', ایستادن 'disputed', and the node takes the worse verdict.",
 "derivation_fa": "هر دو واژه واقعی‌اند، امّا پیوند آن‌ها با این ریشه محل اشکال است. «ایستادن» از فارسی میانهٔ ēstādan است، اما چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷) این فعل را زیر *staH با پیشوند *abi- می‌آورد نه *adi-؛ ویکی‌واژه نیز به پیروی مکنزی و چونگ همین را می‌گوید. پس پژوهش امروزی این پیکان را رد می‌کند. دربارهٔ «آری» ویکی‌واژه همان اشتقاق را می‌آورد ولی مأخذش خودِ همین صفحهٔ ۱۲۴ نورایی است (استدلال دوری)؛ مأخذ مستقل فقط حدس هرن (۱۸۹۳) است و نیبرگ بازتاب فارسی ēvar را «آور» می‌داند نه «آری».",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B3%D8%AA%D8%A7%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C"
 ],
 "ref_check": [
  {
   "ref": "HRN",
   "status": "supports",
   "note": "Horn p. 20 no. 84 'īstāden „stehen“, estāden, Praes. est-em ... ap. ∟stā- (ai. sthā-); pāz. estādan ... Ich leite np. estaden, später istāden, von ap. *adi + ∟stā- ab' and p. 5-6 no. 16 'ārī „fürwahr“. Kās. ore, āre, ārī' → 'phlv. ēvar ... auf ap. *adi + ∟var-'. The bare 'HRN' on the chart is Horn, and Horn does say this."
  }
 ],
 "consulted": [
  {
   "src": "CHEUNG",
   "where": "EDIV s.v. *staH",
   "stance": "contradicts",
   "note": "the Middle Persian reflex is listed as '(+ *abi-)', i.e. *abi-staH, not *adi-staH; the *adi- prefix does not appear in Cheung's article at all."
  },
  {
   "src": "PHD",
   "where": "MacKenzie 1971, ēstādan / ēwar",
   "stance": "partial",
   "note": "both Middle Persian words are there ('ēwar ... certain(ly), assured(ly)'; ēstādan in the verb phrases), but MacKenzie gives no New Persian ārī and no Old Persian prefix."
  },
  {
   "src": "NYB",
   "where": "Nyberg II 1470",
   "stance": "partial",
   "note": "'ēvar ... Paz. ēvar; NP āvar „true, certain“' — a different New Persian outcome from Nourai's آری."
  }
 ]
}
-----
page-486.json {
 "id": 6,
 "lang": "Persian",
 "words": "Ordîbehešt «اردیبهشت»; Dârîuš «داریوش»",
 "verdict": "plausible",
 "derivation": "اردیبهشت is a straightforward inherited descent; داریوش is a learned re-import. (a) Av. aş̣a- vahišta- / OP *arta-vahišta- > MP Ardwahišt, also Urdwahišt and Ašwahišt (MacKenzie lists all three), > NP اردیبهشت ordībehešt / ardībehešt, the second month and the third day of each month — the calendrical use being the reason the word survived at all. The -d- of ard- is the Old Persian/Median arta- with regular MP rt > rd, and the -i- is the MP connecting vowel; Nyberg gives 'MPrs ʾrdywh<yst>, Sogd., NP ardi- (urdi-)bihišt'. (b) داریوش: OP Dārayavauš was borrowed into Greek as Δαρεῖος (haplology for *Δαρειαῖος, Kent), Latin Darius, Hebrew Dāryāweš. The Persian line of descent, however, gave MP Dārāy > NP دارا/داراب (the Dārā of the Šāhnāme); modern داریوش Dāriuš is a 19th-20th-century revival shaped on the cuneiform/Greek form after the decipherment of Old Persian, not an unbroken Middle-Persian inheritance. Nourai's arrow is therefore right about the etymology but silent about the gap, which is why the node is 'plausible' rather than 'confirmed'.",
 "derivation_fa": "«اردیبهشت» از aş̣a- vahišta- اوستایی از راه فارسی میانهٔ Ardwahišt/Urdwahišt به فارسی نو رسیده است؛ تبدیل rt ایرانی باستان به rd در فارسی میانه قاعده‌مند است و بقای واژه مدیون کاربرد گاهشماری آن است. اما «داریوش» دنبالهٔ پیوستهٔ Dārayavauš نیست؛ صورت موروثی آن در فارسی میانه Dārāy و در فارسی نو «دارا/داراب» (شاهنامه) است و «داریوش» احیای عالمانهٔ سدهٔ سیزدهم/چهاردهم خورشیدی است که پس از خوانده شدن خط میخی از روی صورت پارسی باستان/یونانی ساخته شد. ریشه‌شناسی نورایی درست است ولی راه انتقال دقیقاً آن نیست که پیکان نشان می‌دهد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA",
  "https://www.etymonline.com/word/Darius"
 ],
 "ref_check": [
  {
   "ref": "BQT:101",
   "status": "supports",
   "note": "Borhan-e Qate' p. 101 (BQT_v1_pages.txt leaf 311, running head اردیبهشت) has the اردیبهشت article; the preceding page carries 'اردیبهشتگان — جشنی که ایرانیان باستان در روز اردیبهشت (سوم) از ماه ...' and the note 'رک: اردیبهشت ... شا وهیشته' (the Pahlavi/Avestan form)."
  },
  {
   "ref": "KLN:401",
   "status": "supports",
   "note": "Klein s.v. Darius, quoted at node #5: 'fr. OPers. Darayava(h)ush ... \"he who holds firm the good\"'."
  },
  {
   "ref": "MON:327",
   "status": "partial",
   "note": "6-volume Mo'in not on disk; the abridged edition supports the content of the بهشت/بهمن family but the exact page cannot be confirmed."
  },
  {
   "ref": "ZMA:19",
   "status": "not_checked",
   "note": "Jonaydi, Zendegi va Mohajerat-e Aryaian: no accessible copy (refs_online.json: purchase only)."
  },
  {
   "ref": "SYN:1176",
   "status": "supports",
   "note": "Buck p. 1176 names Dāraya-vauš as the Old Persian proper name preserving vasu-/vohu-."
  }
 ],
 "consulted": [
  {
   "src": "PHD",
   "where": "MacKenzie s.vv. Ardwahišt, Urdwahišt, Ašwahišt",
   "stance": "supports",
   "note": "'Ardwahišt ... (N urdībihist)'; 'Urdwahišt [ʾwrtwhšt'] = Ardwahist.'; 'Ašwahišt [ʾšwhšt'] = Ardwahist.'"
  },
  {
   "src": "NYB",
   "where": "Nyberg II s.v. Art-vahišt",
   "stance": "supports",
   "note": "'MPrs ʾrdywh<yst>, Sogd. 2771; NP ardi- (urdi-)bihišt.'"
  },
  {
   "src": "KNT",
   "where": "Kent s.v. Dārayava'u-",
   "stance": "partial",
   "note": "Confirms the Old Persian etymology and the Greek/Akkadian/Elamite renderings, but records no New Persian continuant — consistent with داریوش being a modern revival."
  },
  {
   "src": "HUB",
   "where": "Hübschmann (HUB.txt l.6712)",
   "stance": "supports",
   "note": "'zd. aša-vahista-; Farvardīn \"der erste Monat\" = phl. fra-...' — Hübschmann treats the month names as the Avestan/Pahlavi survivals."
  }
 ]
}
-----
```


## [2026-10-17T00:01:07.789Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^1137|wel-.*wollen|u̯el-.*wollen|\\bwel-3|welǝ-' POK_full.txt | head -20; grep -n -i -E 'wählen, wollen|wollen, wählen' POK_full.txt POK_0*.txt | head"
}
```


### [2026-10-17T00:01:08.292Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:01:11.526Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 1500 POK_full.txt; echo; grep -n -i 'wollen' POK_full.txt | head -20"
}
```


### [2026-10-17T00:01:11.859Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic 


EGmRun. 


East-Germanic Runic 


El. 




Elymian 


Elam. 




Elamite 


Elam.- 


Iran. 


Elamo-lranian 



EMoBret. 


Early Modern Breton 


EMolr. 


Early Modern Irish 


EMoW 


Early Modern Welsh 


ESI. 


East Slavic 


Faer. 


Faeroese 


FriRun. 


Frisian Runic 


Gal. 


Galindian 


Gallo-Gk. 


Gallo-Gk. (in Gk. authors) 


Gallo-Lat. 


Gallo-Latin (in Lat. authors) 


Gaul. 


Gaulish 


GaulG 


Gaulish in Greek letters 


GaulL 


Gaulish in Lat. letters 


Go. 


Gothic 


Gr. 


Greek 


Hebr. 


Hebrew 


Hell. 


Hellenistic 


Hi. 


Hindi 


HVan. 


Haut-Vannetais 


IE 


Indo-European 


Mr. 


Indo-lranian 


InsCI. 


Insular Celtic 


Iran. 


Iranian 
9994:glands near the genitals, part, in morbidly swollen state '; nisi, pua' blow, breathe '. 
10030:" hump, outgrowth ', Old Swedish bolin, bulin^ swollen '; Old Irish it'o/ac/? 'swelling, blister' 
10051:with Germanic -d- (-A«-): ndd. puddig^ swollen ', Old English p^o'^c "swelling, lump, 
10146:Swiss yO/Js/ig "swollen'. Modern High German Pfausback, with ndd. aniaut Pausback 
10399:Middle Irish borr^ sioui, proud, swollen', mcymr. bwrrds., corn, borlat'; 
11602:Old Icelandic participle bo/ginn "swollen', (under the influence of common Celtic -/7S-, - 
11814:ffroen-foir with swollen nostrils ' (: cpaAAoc;); 
11833:swollen = "thick, big, large', Swedish Dialectal bal, bor thick and large, strong, very daring 
11852:"swollen, inflated' = " arrogant, bold ', Gothic bal-t^aba Mv . " boldly ', balt^eii. " boldness ', 
15624:^/"a^sc/?© "swelling, blister'. Modern High German dial, brausche, brauschig^ swollen; of 
19040:remains far off SpTAoc; " bloodsucker, leech, penis', actually " the swollen ', to Spiaouaav 
26639:"swollen', Swedish dial, ink' blain, boil, furuncle of horses '. 
29588:probably as "the swelling, the swollen', compare russ. uditb or udetb "to bloat, bulge, 
30815:ganger, congerds.), yoYYpcbvn ' swollen neck gland ', perhaps yoyyajv [j(ji)p6(; Hes. ('fat, 
46769:xoyi. Gen. xuli^ a scrofulous tumor, swollen gland, struma, scrofula, tuberculosis of the 
46774:Maybe alb. kule^ hernia' = Armenian xoyi. Gen. xuir swollen gland ', alb. kulpra, kulper 
50857:ubermachtigst ', sJ/75- "swollen, turgid ' (Old Icelandic hunneic; about Old Indie suna-m 
50860:so-fha-m. " intumescence, swollen state ', so-pha-m. "swelling, lump, growth, ulcer'; sava- 
63345:*j§dro, J^drb: 0\d Church Slavic yl^o'/'o "quick, fast' (from "*strong' = "*swollen'), serb. Jedar 
64695:(from *pano-caps), pantex^^awuch, intestines (due to a participle */oa/7c-/c»-s 'swollen,
```


## [2026-10-17T00:01:20.760Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'to want, wish|to wish, want|want, choose|choose, want|wish, will' POK_full.txt | head; grep -n -E 'Page\\(s\\): 113[6-8]' POK_full.txt | head"
}
```


### [2026-10-17T00:01:21.135Z] TOOL RESULT

```
90272:etc., vrtha' futile ', Avestan ap. var- " choose, want, desire, will' (3. PI. preterit Med. varata. 
90262:Page(s): 1136-1137 
90321:Page(s): 1137-1138
```


## [2026-10-17T00:01:23.254Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90255,90330p POK_full.txt"
}
```


### [2026-10-17T00:01:23.579Z] TOOL RESULT

```
Postverb. 1, 11), Old English wlatian6s.; 

also Germanic *wull=>u-xx\. "glory, magnificence' ("*prestige'): Gothic wu/Pus'g\orY, 
magnificence'. Old Icelandic Ullr{*wult^uz) " god's name ', Old English n/i/Zcyo/'" gloria', 
compare Gothic wult^rs^ value, worth ', M/i//fc'/7za"herrlicher'; further wult^ags ^ zybo^oc^ . 

References: WP. I 293, WH. II 831. 
Page(s): 1136-1137 

Root / lemma: uel-2, ulei-, ule(i)- 
Meaning: to wish; to choose 

Material: A. Old Indie unthemat. 3. Sg. Med. Aor. avrta. Opt. vunta, participle urana-, 
vrnTte, vrnnati, vrnoti, vrnute^ choose, vorziehen, love', vrta- "gewahit, desirable, worth 
having, welcome, wanted ', vara- m. "wish, Gegenstanddes Wunsches', vara- "vorzijglich, - 
st, better, best', varlyarhs- 'better', var/stha- 'best', i/5/ya-"wahlbar, vortrefflich, 
distinguished ', varana- n. "das Wahlen, WiJnschen', vara- m. "Kostbares, treasure, tribute' 
etc., vrtha' futile ', Avestan ap. var- " choose, want, desire, will' (3. PI. preterit Med. varata. 
Opt. vairfmaidfj, v9r9n[a]-{\. Sg. Med. versnS), v9rdnav-{3. Du. Med. varanvaite, 
participle Perf. Pass, varata-, va/rya-'tbe beste, delicious, worth '; also Avestan var- 
"believe'; 

Armenian gef pleasure, beauty' (presumably from *uel-no-, compare cymr. gwell 
"better'); Venetic PN Volti-xnos, Voltiomnus, lllyrian Voltius, Voltisa etc. (M. Lejeune BSL. 
49, 41 ff.) from *ulti-; 

gr. Asiu), Anw "will', after Schwyzer Gr. Gr. 1, 676 from *ule(i)mi, PI. * uleime {1); Latin 
void {* veld), vult{*velt), velle 'want, desire, will' (Opt. velim), voluntas, -at/si. "good 
volition' (previous participle *uolunt-tat-s); nolo, nevis, nevolt'\ will not' {*ne-vold); mald'\ 
pull vor', back formation after mavolt{magls volt); Umbrian e/7-i/e//^"jubeto', i/e//i/"deligito', 
e/7i/e/M/"decretum, edictum'; 

mcymr. corn. bret. guell'better', ncymr. gwell {*uel-no-'Vorzug , choice ', or to uer-2, 
see there); gall. VN VellavT, Catu-vellaunr{corc\pare den Ligurian PN Genava'GenV: raet. 
VN Genauni); 

Gothic wlljan. Old High German wlllu, will, wellan etc. "want, desire, will'; Gothic wllja. 
Old High German ulllo, wlllio etc. 'volition', Kaus. Iter. Gothic waljan. Old Icelandic veija. 



Old High German wellen^ choose ' (= Old Indie i/aAayaZ/'wahlt for sich', Old Church Slavic 
voliti); Old High German walai.. Old Icelandic i/a/n. 'choice '(: Old Indie vara- m.); 

Lithuanian pa-velmi, 3. Sg. pa-velt, Infin. pa-ve/t/" want, desire, will, allow', ablaut. v/7t/st 
"hope' {*ultis), K///^c»5 "hoffe'; Old Church Slavic veljg, ve/et/^\Nant, desire, will, order', 
ablaut, voljai. "volition', therefrom voljg, vo/ft/'want, desire, will, wish', in weiteren ablaut 
do-vbljQ, do-vbleti^ suffice \*Uole-)\ 

about Gothic wafia. Old High German wela, wolaeic. "probably' compare Feist^ 543. 

B. o^extension ((y-present): gr. £A5o|jai, hom. ££A5o|jai "sehne myself, demand after 
etwas', ££A5(ji)p n. "wish, desire'; 

Irish fled, cymr. ^MVeo'o'"Gastmahl, festival' {*ulda); gall. PN Vlido-rTx. 

C. yo-extension: hom. eAttu) "allow hoffen', EArrofjai, ££Ano|jai "hoffe', Perf. poet. £oAna; 
EATTiq, -i5o(;f. "hope', EAni^w "hoffe', hom. £Anu)pn "hope', zero grade *aAniaTO(;, Sup. to 
aArraAEOc;, dissim. apnaAsoq " desirable, worth having, welcome, wanted, charming', 
£naAnvo(; " desirable, worth having, welcome, wanted ' (///7-stem); Latin volup{e) Adv. 
"vergnijglich, gerne', CVcZ/O/-, *ulpi-), i/oA/p/as "pleasure'; 

doubtful hom. EiAairivn "festival', Aeolic EAAarriva (*£-FAaTT-iva?). 

References: WP. I 294 f., WH. II 828 f., Trautmann 348 f., Specht KZ 62, 59 f., Vasmer 1 , 
1 80, 224, Frisk 78, 455, 485, 502 f. 
Page(s): 1137-1138 

Root / lemma: uel-3 
Meaning: to press, push 

Material: Hom. siAu) (*F£A-vci)); Inf.-Aor. eAqqi and with suggestion EcAaai, Aor. Pass. 
£aAr|v, aAri|j£vai, ep. Ionian siAsw {*FzK-ytuS), Attic siAAu) (*£F£Ajaj with Vorschlags-s), Doric 
el. Fr|A£U), redupl. lAAu) (*Fi-FAci)) "drange, push, press, presse'; lakon. pr|Ar||ja KcbAupa, 
cppaypa £v noraiJU) Hes., messen. riAr||ja, Ionian £iAr| "troop, multitude, crowd' (F£Av-), next 
to which probably with /= ©(as niAvapai) AtticlAr), DoriclAa "troop, multitude, crowd'
```


## [2026-10-17T00:01:28.579Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\s*wel-2|wel-2\\.|wel- *2' AHD_watkins1985.txt | head; grep -n -i 'William' AHD_watkins1985.txt | head; grep -n -i 'volunteer\\|voluntary' AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:01:28.966Z] TOOL RESULT

```
537:gva-. Also grem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumo6n-, he who comes, a guest, in compound *wil-ku- mon-, a desirable guest (*wil-, desirable; see wel-2), in Old English wilcuma, a welcome guest, and wilcume, the greeting of welcome: WELCOME; C. compound *bi-kuman, to arrive, come to be (*bi-, intensive prefix; see ambhi), in Old English becuman, to become: BECOME. 2. Suffixed form *g“(e)m-yo- in Latin venire, to come: VENIRE, VENUE; ADVENT, (ADVENTITIOUS), (ADVENTURE), (AVE- NUE), CIRCUMVENT, CONTRAVENE, CONVENE, (CONVEN- IENT), (CONVENT), (CONVENTICLE), (CONVENTION),
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1293:BENEVOLENT deu-2, wel-2
1551:GAGE! wadh-1 GAIN! wei-2 GAINLY gagina GAINSAY gagina GAIT ghé- GALACTIC melg- GALACTO- melg- GALAXY melg- GALL! ghel-2 GALLIARD gal-3 GALLINACEOUS = gal-2 GALLINULE gal-2 GALLOP klou-, wel-2 GALLOWGLASS yeu- GALLOWS ghalgh- GALORE lau-
1805:MALEDICT deik-, mel-5 MALEFACTOR dhé-1, mel-5 MALEVOLENT mel-5, wel-2 MALFEASANCE dhé-1 MALIC ACID mélon MALICE mel-5
2039:PALEO- kwel-2 PALETTE pag- PALFREY pert, reidh-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2200:ROW? era-1 ROWAN reudh-! ROWEL ret- ROWEN wel-2 ROYAL reg-! -RRHAGIA wrég- -RRHEA sreu- RUBATO reup- RUBEFACIENT dhé-1, reudh-1
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
48:Speaking to the Asiatick Society in Cal- cutta on February 2, 1786, the English orien- talist and jurist Sir William Jones uttered his famous pronouncement:
53:result of descent from a common original. Certain similarities may be accidental: the Greek verb “to breathe, blow,” has a root pneu-, and in the language of the Klamath Indians of Oregon the verb “to blow” is pniw-. Other similarities may reflect univer- sal or near-universal features of human lan- guage: in the languages of most countries where the bird is known, the cuckoo has a name derived from the noise it makes. A vast number of languages around the globe have “baby-talk” words like mama and papa. Fi- nally, languages commonly borrow words and other features from each other, in a whole gamut of ways ranging from casual or chance contact to learned coinages of the kind that English systematically makes from Latin and Greek. But where all of these pos- sibilities must be excluded, the comparatist assumes genetic filiation: descent from a common ancestor, which, in the case of Indo- European, as Sir William Jones surmised almost two centuries ago, no longer exists. In the early part of the 19th century, scholars set about exploring systematically the similarities observable among the princi- pal languages spoken now or formerly in the regions from Iceland and Ireland in the west to India in the east, and from Scandinavia in the north to Italy and Greece in the south. They were able to group these languages into a family which they called Indo-European (the term first occurs in English in 1813, though in a sense slightly different from today’s). The similarities among the different Indo-European languages require us to as- sume that they are the continuation of a single prehistoric language, called Indo- European or Proto-Indo-European. In the words of the greatest Indo-Europeanist, the
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
2457:VOILE weg-! VOIR DIRE wéro- VOLANT gWel-2 VOLATILE gWel-2 VOLE! welt- VOLE? gWel-2 VOLITANT gWel-2 VOLITION wel-2 VOLKSLIED léu-2 VOLLEY gWel-2 VOLT? wel-3 VOLUBLE wel-3 VOLUME wel-3 VOLUNTARY wel-2 VOLUPTUARY wel-2 VOLUPTUOUS wel-2 VOLUTE wel-3 VOLUTIN wel-3 VOLVA wel-3 VOLVOx wel-3 VOMER wogWh-ni- VOMIT weme- VORACIOUS gWere-4 VORLACE legh-, per! -VOROUS gWere-4 VORTEX wer-3 VOTARY wegh- VOTE wegWh-
```


## [2026-10-17T00:01:33.578Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\[pdf page|^=+ *page' incoming/WLD/WLD_Bd1_pages.txt | head -3; grep -n -E 'wählen, wollen|wollen, wählen|vereuo|vrnīte|vṛṇīte' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -i -E 'u̯el-.*wish|wel- .*wish|velle' IEC.txt | head"
}
```


### [2026-10-17T00:01:34.080Z] TOOL RESULT

```
4534:ghabheolos, io, io- (ghabhul-) “hold, holder”. Cf. ghabh- (1) Gaul. gabalo- (LW in Lat. gabalus *gibbet"); Fr. cf. javelle (‘handful of corn; pile, heap’, fr. *gabella); MIr. cf. frith-gabál ‘bridle’; Ir.
5673:8ernios ‘shrivelled; stone, pip’. Cf. 2znom Skt. jarņah ‘decayed, withered’; OBr. garn ‘pith, middle’; MHG kërn, kërne, s. & wm. ‘kernel, pith, grain’; ON kjarni, id.; EME kern ‘bumpkin’
7954:krinbos, à *wrinkled, shrivelled, withered'.
11329:mugoros (?) Lat. muger, m. ('sniveller'. Fest.); G Mucker, m. ‘hypocrite’. Cf. the various meanings of Lat. é-mungo, v. ‘wipe the nose; snuff a candle; cheat
13290:podios, iom, io of a foot, of a base, of a pace; foot, base, pace', etc. Cf. ped-, pod- (pods) and extns. WP II, 23. Adjectival variant: podiko- Skt. (vowel ambig.) pádyam ‘syllable’; pádya, f. “pace; path"; Oss. faz, Dig. fazà ('buttocks'. Vocalism as Lat. podex, but this is ambig. « *posd-?); Arm. oC, i-st. and o-st. (2) *haulm"; cf. atean, gs: ateni, i-st. ‘tribunal’; Gk. pódion, n. ‘small foot, foot-bandage'; (LW in) Lat. podium, n. ‘balcony, theatre-box'; Ir. oidhe, m. 'traveller'; OCor. odion, late Cor. ojyon, m. ‘0X’; Br. eZenn, s. id.; Icel. fet, n. ‘pace, step, foot’; OCS. poZzdi, m. “floor, pavement, foundation’; Li. padis, gs: padZio, m. ‘base’. For *podik- (podok-) cf. Skt. padikah “pede- strian’; Arm. h-atak, i, av, s. (bottom, base’, fr. *en-podok-); Gk. cf. a-pódikos “without standing, outcast’; Gaul. odicos, odecus, odo- cos *dwarf-elder'. (Lat. podex ‘arse’ is ambig. Despite the phonological equivalence of Oss. faz, fazà, id. the background may be *po-sd-, see po-, sed-). Cf. LG fette, f. 3oist
13393:poros, om 'passage, crossing, track, space, period'. Cf. per-, por-, etc. Gk. póros, m. “passage, track, ford’; MHG var, sn. “ferry, passage); OE fzer, n. “way, passage, ship’; faru, f. journey; chattels; lifetime’; ON far, n. ‘passage, track’; for, f. u-st. journey’; -fari, cpds. ‘traveller’; R porà, f. ‘time’; Blg. pora, f. “age”; Li. para, f. ‘day of 24 hours’; par-, px. ‘back’. WP II, 39
13752:pül- (3) (phül-) ‘pus, decay, foulness'. WP H, 82 Skt. pülyam, n. ‘shrivelled grain; Arm.
13780:pùr- (4) “free, frivolous; fling, scatter; jolt. Same as (3)? Sw. fyr, n. “joke, prank’; R cf. pyrjat,, v. ‘fling; butt, poke’; Srb. piriti, inf. blow’; Li. pürstu, pūrti, v. (3) ‘get dishevelled, blow about’; Latv. cf. purināju, v. ‘shake’, tr.
14856:rüksies, rükstos “harsh, rough’. Cf. rüghos and reug-, roug-. WP II, 353 Skt. rüksáh, adj. ‘rough, dry, arid"; Li. rükstüs, adj. ‘sour, harsh’. (The ultimate radical is un- certain, cf. OHG & OE rüh, gs: rüwes ‘coarse, raw’. A short vowel arises in OCS ot-rüxalü, adj. 'dishevelled")
15562:skemb- Ir sceamh, f. (3) eut: ME (from Norse) skimp, adj. ‘scanty’, but cf. skmb-; R cf. u- SCemit, inf. ‘trap, pinch’; Li. cf. skembras ‘shrivelled, hardened"; Latv. cf. šķembas, fpl. beside (o-gde) skambas 'road-flints'
```


## [2026-10-17T00:01:37.590Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'v[oō]l[oō]|welo|vellem|Lat\\. volo' IEC.txt | grep -i -E 'wish|will|want' | head -8; grep -n -E 'w[aä]hlen|wollen' incoming/WLD/WLD_Bd1_pages.txt | head -10"
}
```


### [2026-10-17T00:01:37.925Z] TOOL RESULT

```
19931:uel- (1) *wish, will, command'. Cf. ual- (2), and uol- (4). WP I, 294 Skt. varami, pp: vrtah, v. ‘choose’ beside (o- gde) varáyami, v. ‘choose; woo’; várah, adj. ‘elite’; m. ‘choice’; váryah ‘eligible’; Av. var-, v. (3) ‘wish’; varo, adj. ‘desired’; vairyo *desir- able’; varom & varo, gs: varáh-, n. ‘gift; Tokh. cf. A wäl, B wel, s. ( ‘king’, to ual- (2), q.v.); Gk. defect. vb. eilon, aor. ‘I chose’; Lat. (*-e- or *-o-) volo, inf: velle, defect. vb. ‘wish; OLat. cf. velim, v. ‘may wish’; Osc. cf. vellia-, f. ‘will: It. voglia, id. beside Rumansh veglia, id.; cf. also lat. volup, volupe, defect, adj. (pleasant, fr. *uel-/uol- + *op- in opes ‘wealth, power, help’; and volup-tàas, cf. Umb. gs. opeter “of the best’: Skt. aptas, n. “act of sacrifice’. See op- (2) and (3) and opoetom. Not as WH); Ir. feillim, v. ‘suit, please’; Go. wiljan, wv. ‘wish’; wilja, f. id.; MHG wëllen, wv. anomal. vb. ‘wish’; Du. willen; OE willan, id. beside willen, adj. ‘desirous’; ON vilja, v. ‘wish, will’; vili, m. id.; OCz. vele, adv. "great. ly’; Cz. vele-, cpds. id.; beside OCS (o-gde) vole! “well! indeed"; voljo, voliti, v. ‘wish’; Cz. volit, inf. ‘choose’; (e-gde in) OCS po- velja, f. ‘edict’; Cz. povel, gs: -u, m. ‘com- mand’; (o-gde also in MHG welen, weln, Go. waljan, tr. ‘choose’); OLI. velmi, 3s: velti, velt, v. ‘wish, augur’; Li. pa-vélti, v. 'grant'; cf. velyjimas, m. ‘greeting’; véliju, yti, v. ‘wish sb. sth’; velyk, adv. ‘rather’; Latv. vēlu, et, v. ‘want’ beside Slavonic calque: pa-velet, inf. ‘<command’; pa-velë, f. id.; Li. cf. also veliaŭ, velý, adv. ‘preferably’
1861:-ea d. a. sg. „wohlwollend, mild“ ( *ev-dfi)s mit Zsdehnung; urgr. a nach
7372:   Gegen Anreihung von slav. me Hi „wollen, gonnen“ Bruckner IvZ. 45,                                        i
8993:daher :) eingeboren, rechtmaBig geboren“ (l&aiysvgg wollen Fick und Bechtel
10007:kaum zu *uek- jj-wollen                  1
12093:„Geschwulst“ (urgerm. *inkwa-z), 0kkvemi „geschwollen“, schwed. mdartl.
13640:yrsian „fibelwollen“,                               ai.      irasydti „zfirnt,            will       tibel,        benimmt     sich gewalt-
13642: tatig ',              irasyd „das t)belwollen“,                            av. aras-ka „Neid“,                     mp. np. arask „Neid,
13899:lich‘   schw. dial. ulka. ylka, olka „sich erbrechen wollen“ usw.
13905:olga „sich erbrechen wollen“; norw. dial, elgja „sich erbrechen wollen usw-                                            11
15236:        = „*geschwollen‘ ), russ. njadretb „stark werden. sich kraftigen;
```


## [2026-10-17T00:01:41.438Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'v[rṛ]n[iī]te|vrnite|wiljan|velle' incoming/WLD/WLD_Bd1_pages.txt | head; grep -c $'\\f' incoming/WLD/WLD_Bd1_pages.txt; grep -n -o '\\[pdf page [0-9]*\\]' incoming/WLD/WLD_Bd1_pages.txt | sed -n '300,302p'"
}
```


### [2026-10-17T00:01:41.918Z] TOOL RESULT

```
20072:      Ai. vi'uitcya „Querbalken‘                                  mir. feicc „ridgepole, rooftree. Obersclnvelle".
24385:  Ygl. Persson \Vtf. 5 15, wo auch abg. uniti „velle u asl. unij nnej „melior“                                           ,                ,
27950:     lat.           volo (*velo), vult {*velf), velle „wolleir‘                                             Opt.   irllm und got. iviljan,
28249:ziehung zu lat. vellere (Wz. ud~ „rei6en“) aus *uel-s-o liegt bier besonders
42823:serb. kosim, -iti „lacerare, vellere ', das wohl Iterativ zu resat i; kosnati,
887
```


## [2026-10-17T00:01:44.233Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27920,27960p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200; awk 'NR<=27950' incoming/WLD/WLD_Bd1_pages.txt | grep -c $'\\f'"
}
```


### [2026-10-17T00:01:44.631Z] TOOL RESULT

```
2.    u el- (auch *uelei-) „wollen, wahlen -.                                       1




     Ai. unthemat. 3. sg.                         med.        avr.          avrta, opt. vurltu, ptc.                         urand-   ;
                                                                                                                                          vniitc,
vrnati,              vrnoti,      vrnute
                         wahlen, vorzieben, wiinschen, lieben“, vrtd- „ge-
                                                 ,.


wahlt, erwiinscht", vara- m. ,,Wahl, Wunsch, Gegenstand des Wunsches 11                                                                            ,

vara- „vorzuglich, -st, besser, best"', vanyums- ,,besser", varistha- „best“,
vary a-              „wahlbar,            vortrefflieh,                   ausgezeiehnet",                     vurana    n.    ,,das   Wahlen,
Wiinschen               £

                            ,
                                vara- m.
                                       Schatz“ usw.    av. ap. var- „wahlen,
                                                      ,,Ivostbares,                                            ;



wollen“ (3. pi. praet. med. varata , opt. vairnnaidJ ), vjr,m[a\- (1. sg. med.
varone), var, mar- (3. du. med. varorivn itv usw. s. Bartholomae Airan. Wb.
1 360 f.   ppp. varata-, vairya- ,,der beste, kostlich, wert”; auch av. var-
 .glauben‘-   (s. unter *uer- ..Freundliches erweisen"), arm. gd „Gefallen,
Schonheit" (vermutlieh aus *ud-no-, vgl. cymr. givell „besser");
     lat.           volo (*velo), vult {*velf), velle „wolleir‘                                             Opt.   irllm und got. iviljan,
u'ilcima, ahd.                   iville    vielleicht nicht ursprgl. Opt.,                                      sondern Ind.- oder             Inj.-
St.von der Basis *uelvi-, vgl. aksl. veljq vdiii veleti, Brugmann II 2 3, 90',          ,
                                                                                                        :




umbr. di-vdtu ..jubeto", veltu ..deligito oder dgl.“, ehvdlda ,.decretum,
edictuin“
  mcymr. corn. bret. guell „besser“, ncymr. gwell (wohl *uel-no- ..Yorzug,
299
```


## [2026-10-17T00:01:49.810Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'giraw|girav|wurr|wābar|wavar|gurav' CHEUNG.txt | head -20"
}
```


### [2026-10-17T00:01:50.284Z] TOOL RESULT

```
27284:*NWIR: NP giravidan ‘to believe, confide in; to obey’, NP bavaridan (denomin. ?) ‘to 
41027:giravidan, 421
```


## [2026-10-17T00:01:55.797Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27240,27330p CHEUNG.txt"
}
```


### [2026-10-17T00:01:56.346Z] TOOL RESULT

```
*AVESTAN: var- ‘to choose; to convince’ || (+ *fra-) ‘to choose’ — Liste: 50 

MED.; Pres. n-: IND. 1sg. OAv. varané (Y 46.3), YAv. vorone (Y 12.2, Vr 5.3), 3sg. OAv. varanté (Y 
43.16, Y 51.18), INJ. 35р. YAv. verenta (Yt 10.92), 3р1. OAv. voronata (Y 30.6), OPT. 35р. them. ҮАУ. 
fraoronaeta (V 19.2); Aor. athem.: INJ. 3sg. OAv. varata (Y 30.5, Y 32.12), OAv. frauuarata (Y 31.10), 
1р1. OAv. varomaidi (Y 32.2, Y 35.3), SUBJ. 1sg. YAv. frauuarane (Y 12.1, Y 12.8, VdPZ 9.32), 35р. 
Y Av. "frauaraite (ЕТА 5); Inf.: pres. YAv. vorondiiai (Vr 4.2) 

*OLD PERSIAN: v(a)r- ‘to choose, convince’ = Kent: 206b 

MED.; Pres. them. nu- IND. 3sg. v(a)rnavataiy <v-r-n-v-t-i-y> (DNb 23), impf. 35р. av(a)rnavatä 
<a-v-r-[n]-[v]-[t]-[a]> (DSf 17), SUBJ. 3sg. v(a)mavataiy <v-r-n-v-a-t-i-y> (DB 4.49), IMPV. 35р. 
v(a)rnavatam <v-r-n-v-t-a-m> (DB 4.42, DB 4.53) 

*MIDDLE PERSIAN: MMP wrw- (BMP HYMNWN-) ‘to believe’ = DMMPP: 345 
Pres.: SUBJ. 3sg. MMP wrw'd, OPT. 2pl. MMP wrwwyd; Partic.: perf. pass. MMP wrwyd, II MMP 
wrwyst-; Inf.: MMP wrwystn 

*PARTHIAN: wrw- ‘to believe’ — Ghilain: 79, 85 | DMMPP: 345a 

Pres.: IND. 3pl. wrwynd; Partic.: perf. pass. "wrw’d 

*SOGDIAN: CSogd. wrn-, MSogd. wrn- ‘to have faith, believe’ || (+ *ui-) SSogd. yw’r 
‘separation’, SSogd. yw’r, BSogd. yw’r, CSogd. yw’r, MSogd. yw’r ‘but, never- 
theless, except’ 

Well attested: Pres.: IND. 15р. CSogd. wrn’m, dur. CSogd. wrn'msqn, CSogd. wrn'msq, 2sg. dur. CSogd. 
wrnysqn, 1р1. CSogd. wrnymsqn, etc. 

*CHORESMIAN: m/wrw- ‘to believe’ || (+ *apa-) bw’r- ‘to separate oneself, diverge’, 
bw’ry- (caus.) ‘to separate’ || (+ *upa-) ? bw’ry- ‘to select’ || (+ *ui-) yw’ry- ‘to 
know, experience, understand’. ó Rather than putting Chor. bw’ry- ‘to select’ and 
bw’ry- ‘to separate’ together under a single entry (as done by Samadi), we may 


*yar(H)2 421 


distinguish two differently prefixed formations, viz. with the pref. *upa- and *apa- 
respectively. > Samadi: 217, 29, 258, 208 f. 

*BACTRIAN: (о)оосро, 000000, oxoapo (etc.) ‘valid’ = S-W, Bact.: 209b 

*NWIR: NP giravidan ‘to believe, confide in; to obey’, NP bavaridan (denomin. ?) ‘to 
believe; credit’, NP bavar ‘belief; credit’ (< old intensive), Kurd. (Kurm.) bariya (Е) 
‘wish’, bavar, bawar (m.), (Sor.) bawar, birwa ‘belief; hope’ (Pers. LW ?) || (+ *uz-) 
? Bal. zurag, zirag, zorag ‘to take (out ?)’ || (+ *ui-) ? Bal. giwart/giwar- ‘to make 
equal’ (but in dial. also “о choose, select’, ‘to part, separate’) 

*NEIR: Oss. I. wyrnyn ‘to believe’, Yi. war-/wat-, M. wet-/wetta ‘to separate’ || (+ 
*apa-) Yzgh. bawurn ‘canal’ || (+ *uz-) Oss. І. evzaryn/avzarst, evzerd, D. 
evzerun/evzurst ‘to get separated; to sprout (of plants); to occur, appear’, (orig. 
caus.) Oss. I. avzarum/evzarst, D. avzarum/avzurst ‘to pick out, choose; to 
separate; to make out (of), understand; to experience’, Wa. zvor, z(o)wor, Sh. ziwor 
(f.) ‘offset, offshoot; the head part of an irrigation channel branching off from a 
main canal or river’, Sariq. ziwur ‘mouth of a river’ || (+ *ui-) Oss. I. waryn/weerst, 
D. iwarun/iurst ‘to divide, distribute; to be divided, divide up possessions’, Wa. 
yo(r)wor-/yo(r)word- ‘to divide, disperse (cattle)’ 

*MISC: Arm. (LW) vawer ‘true’ 

*SANSKRIT: var” ‘to choose, pick’ (RV+) > EWAia II: 511 

«PIE *uelH;- ‘to want, wish’ = LIV: 677 f. | Pok.: 1137 f. 

*IE COGNATES: Lat. volo ‘I want’, OCS velits ‘wants, orders’, Lith. vélti ‘to wish, to 
prefer’, Goth. wiljan ‘to want’, Engl. will, etc. 

*REFERENCES: JIFL II: 262b, 555b; Henning, Cosmog.: 310; Abaev, Slovar’ I: 209 ff.; EVS: 21b, 109b; 


Abaev, Slovar’ IV: 123 f., 51 f.; Werba 1997: 378 f.; Steblin-Kamenskij 1999: 434, 439; Cabolov 2001: 
124, 158 f.; Shahbakhsh: s.v. giwar- 


*uar(H)? *to mix, mingle' 

*CHORESMIAN: (+ *ham-) m/w’r- ‘to be mixed, confused’, (caus.) m/w’ry- ‘to mix, 
confuse’ — Samadi: 208 f. 

*NEIR: (+ *ni-) Wa. ni(y)or-/ni(y)ord-, nayor-/nayerd ‘to mix, mingle’. > 
Steblin-Kamenskij 1999: 245 derives the Wa. verb from *ni-uar (*yar ‘to turn’), but 
we may now assign it to *uar(H). 

© According to Samadi (ibid.) Chor. m/w’r-, m/w’ry- are counter-formations of 
bw’r- ‘to be separated’, bw’ry- to separate’ (< *upa-°). It remains unclear though 
how this procedure would have taken place, especially if we consider the simplex 
verb, which means ‘to choose; to convince; (med.) to believe’. Perhaps, m/w’r-, 
m/w’ry- has a different origin, being related to the well-attested Germanic forms for 
‘to confuse’. No further Ir. cognates can be cited though, with the exception of the
```


## [2026-10-17T00:02:03.344Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 'wurr' 'w[aā]bar' 'w[aā]war' '[eē]war ' 'ahr[eē]war' 'ahrivar|ahrēvar'; do echo \"== $p\"; grep -n -E \"$p\" PHD.txt | head -5; grep -n -E \"$p\" NYB_vol2_glossary.txt | head -5; done"
}
```


### [2026-10-17T00:02:04.237Z] TOOL RESULT

```
== wurr
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
970:belief āstawānīh, wābar, wurroyiin, xwastügih.
1229:choose wéxtan, wizidan, wurróyistan.
2272:heresy ahlomoyih, dušwurrēyišnīh, judristagih, zandikih; v. hetero- doxy.
== w[aā]bar
603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
970:belief āstawānīh, wābar, wurroyiin, xwastügih.
979:beneficence hudā(ha)gīh, kirbakkarih, xwābarīh.
980:beneficent hudā(ha)g, hugar, kirbak- kar, xwābar.
== w[aā]war
== [eē]war 
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
4523:ālag! šahrewar šahr frést-t šahryār šahryārīh fréstidan! šahrestān frēstādanī álag!
== ahr[eē]war
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
4388:I Frawardin II Ardwahišt III Hordad IV Tir V Amurdad VI Sahrewar
4392:3 Ardwahist 4 Sahrewar
4523:ālag! šahrewar šahr frést-t šahryār šahryārīh fréstidan! šahrestān frēstādanī álag!
== ahrivar|ahrēvar
3591:Šahrēvar [štr'ywr, Stlywl] one of the Amahraspands 391°, 10116 10222. ~ In the calendar the name of the 6th month and of the 4th day of the month. — Borrowed from Av. (545) xšadra- vairya-.
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
```


## [2026-10-17T00:02:08.146Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'v[aā]var|varravist|v[uo]rr[oō]y|virr[oō]y|ēvar ' NYB_vol2_glossary.txt | head -12"
}
```


### [2026-10-17T00:02:08.453Z] TOOL RESULT

```
1467:évak [HDwk'; on coins *ywky] num. one, passim; hàn + ~ Arjäsp A. alone 2416, 2927; ~ ~ one by one 92$; har ~ every- one 1045-%, 10617. 11318; ~~ bēvar ten thou- sand 244; 3 ~ one third 6329-22, 9316, 1025; 4 ~-é [-’y] one fourth 998; 5 ~-é [^y] 10015-17, 10227. 1031-2; — in correspon- dence with dit, ditikar, ane, v. these ws. — Av. ačva-. OP awa- + -ka-, v. s. v. žē; MPrs yk; Paz. yak, iak, NP yak — as against MPrth ‘yw ‘one’, *ywg ‘alone’.
2019:hömikän [hwmyk’n'] containing haoma, “haomic”: äp + ~ 5623.15, — As to the suff., cf östikän, vāvarīkān; šāhīkān ‘royal’ FrP 2. — V. also *huhömikän.
3041:patiš [pts] adv. 1. before (= pēš), with hac: ~ hac zāyišn i ... before the birth of ... 365. — 2. used instead of pat if it refers back to an encl. pron. in the be- ginning of the sentence: cē-m anākēh vas ~ kunēnd (BYDWN-x;) for they will do much harm to me 954; i ka-t anākēh ~ kuném for we shall do. harm to thee 76°; api-š dēvān apasós ~ kunénd and the devs sneer at him 7576-2"; api-ščin ~ nē virroyam and I do not believe in them 64%; cigan ka-šān Sir i garm ~ andar dösend as if warm milk were milked upon them 10121-22; 4228; 8024-26; 9825-26, . 3, as a substitute for the prep. pat + the encl. pron. of the 3d p. sg. -$: on, to, at (etc.) him, her, it 4?6. 3212, 4726, 559.16, 6311.16, 6420.24 6614, 801, 8615.
3591:Šahrēvar [štr'ywr, Stlywl] one of the Amahraspands 391°, 10116 10222. ~ In the calendar the name of the 6th month and of the 4th day of the month. — Borrowed from Av. (545) xšadra- vairya-.
3940:Ghilain 79, is an error]; Arm. lw. vawer, vawerakan < *vāvarya(kana)- ‘true, valid, authorized’ (thus in the sense of *vä- para-); — MPrs wbr, wbryg ‘faith’, w?bryg?n ‘true’, possibly also pl. cas. obl. 'the believers'; on the other hand MPrs w^wrydn ‘to believe’, in all probability borrowed from Prth; Verbum 195, Ghi- lain 79, S, Gloss. s. v. w’bryg’n. — BP always w’pl-, mostly in the sense of ‘true, truth’, seldom ‘belief’; Ps. w’plyk’n ‘true’; Paz. vawar ‘truth’, but vafringqni (SGV) through confusion with Gfrinakan;
4191:virröyistan [HYMNW<N)-stn'] to be- lieve (pat in) 64?. 8017, 8212. 10023. — Av. (1360) ?var-, pres. varanav-, OP vrnav- which has furnished the base of the Milr vb. As to the second syllable I follow the Paz. forms of ŠGV and Mx: 1. grotstan (for "guro-), garoistan, grūtšn besides varčišni (SGV); 2. pres. gla)ročd, garčičd, garēhēd, gla)rčišni (Mx); they are best in keeping with the phonetic spelling of virroyišn (g. v.). FrP 18 gives the Paz. readings viravistan, varvistan, varvidan, varvid; NP giravidan is due to the coales- cence of this vb. and the den. of girav, BP grav 'pledge' and has the senses of both. — MPrth pt. wrwd (MHC); MPrs wrwystn (may be virröyistan or virra- vistan), pres. subju. 3d p. sg. wrwd. — As to virrav-: virróy- cf ménoi < *mainya- oya-. (A reading vurr- is excluded; vu- always > gu-, in NP also > bu-).
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
5713:wrw’d: virroyistan
6180:wrwyšn: virroyišn
6326:agröisnihä: avirroyišn
7026:aužand: apa-cand āvar: ēvar āvār: ēvār āvār(ah): ēvarz āvāz: ēvāc (a)vizah: apécak āxur: axtar az: hac azadi: azateh äzärdan, äzär-: läzär- äzarm: azarm azmudan (äzmäy-): ozmutan aždaha: Azi-dahak ažgahan: ašgihanēh
```


## [2026-10-17T00:02:13.364Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3934,3940p NYB_vol2_glossary.txt | cut -c1-900; pdftoppm -f 539 -l 539 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg539"
}
```


### [2026-10-17T00:02:14.424Z] TOOL RESULT

```
vànitan [w’nytn'], pres. Ist p. sg: vänom 615, to vanquish, to defeat 1065. 109?2, —
| Av. (1350) !van-; MPrs pres. w’n-; pt.
w’nyst (BBB).
vanj- [wnc-] *to hold exactly, pres. pass. 3d p. sg.: dek i catrusvätak vanjihet [wneyhyt', restore the reading of M] a pot in which is contained (which holds) a quarter (?) 428-9. — NP gunjidan ‘to be contained or held; to hold exactly, to be filled’.
vaparikanéh [w’plyk’nyh] truth, trust- worthiness 361. — Two ws. of kindred meanings have intersected here: 1. *vā- vara- ‘choice’, ‘adoption of the true faith’, hence ‘conviction, belief, faith’, from Av. (1360 sqq.) ?var-, pres. vävar-, vdur-; 2. *päpara- ‘fulfilment, realization of the conviction or the faith chosen’, hence ‘the realized faith: truth, validity’, from Av. (850) ?par- ‘to fill, to fulfil, to perform (e. g. an act of piety)’, pres. pāfr-, the zero-stage of *päpar-. Original *pa- para- became *väpara- through dissimi- lation, certainly prompted by the in- fluence of *vàvara- whose meaning falls within the same semantic range. In Prth
vüvara-, in Prs *väpara- prevailed: MPrth wwr, wwryft ‘faith’, ’w’wryg ‘unbeliever’? [w’wryg’n ‘the believers’,
Ghilain 79, is an error]; Arm. lw. vawer, vawerakan < *vāvarya(kana)- ‘true, valid, authorized’ (thus in the sense of *vä- para-); — MPrs wbr, wbryg ‘faith’, w?bryg?n ‘true’, possibly also pl. cas. obl. 'the believers'; on the other hand MPrs w^wrydn ‘to believe’, in all probability borrowed from Prth; Verbum 195, Ghi- lain 79, S, Gloss. s. v. w’bryg’n. — BP always w’pl-, mostly in the sense of ‘true, truth’, seldom ‘belief’; Ps. w’plyk’n ‘true’; Paz. vawar ‘truth’, but vafringqni (SGV) through confusion with Gfrinakan;
```


## [2026-10-17T00:02:18.323Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg539.png"
}
```


### [2026-10-17T00:02:18.771Z] TOOL RESULT

```

```


## [2026-10-17T00:02:18.767Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:02:29.629Z] TOOL CALL #22: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg539.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/539.png; cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'wrn|believ|faith' SOD.txt | head -15; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['SOD'],ensure_ascii=False)[:900])\""
}
```


### [2026-10-17T00:02:30.124Z] TOOL RESULT

```
4114:Hellenized,  had  adopted  the  Buddhist  faith.  Although 
4132:believed  that  the  western  extension  of  the  earlier 
4197:reason  to  believe  that  the  big  Sogdian  cities,  having 
4284:centuries  AX).  There  are  reasons  to  believe  that  new 
4391:Tajikestan,  is  believed  to  be  the  direct  descendant  of 
4588:are  believed  to  be  translations  of  Chinese  originals. 
4600:was  established  to  be  a  faithful  translation  of  the 
4808:Manichean  faith,  the  Sogdian  colonies  were 
4816:century.  The  faith  also  gained  followers  in  Mongolia 
4818:Manicheism  as  his  national  faith.62  With  the 
4944:spread  of  the  Nestorian-Christian  faith  through 
5256:821)  who  had  adopted  the  Manichean  faith  as  the 
5825:XI)  [p]  There  are  reasons  to  believe  that  a  short, 
9436:299  »tr  xwrndy(y)   M 
9589:hope,  trust,  faith  z 
{"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
```


## [2026-10-17T00:02:32.104Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\s*[0-9]{4,5}\\s+wrn|wrn[\\x27’ ]' SOD_pages.txt | head -15; grep -n '\\[pdf page 478\\]' SOD_pages.txt"
}
```


### [2026-10-17T00:02:32.614Z] TOOL RESULT

```
10664:        120.4                                                   2386 (spwrn M                          •x~it1J\£iJ9
10675: 2387 'spwrn'k M                                                  JJf
21341:6131 nwh' C                                                       6144 nwrn'y B =* zwrn}k
21441:                                                                6174 nwwrn'ky^h)        M                                    LU
26781:7999 ptwysd'r-    C                        c^J'^jjs < j-ul>-             xwrn ptxwrk
27359:                                                                                     8207 pwrn B, M, C                                     j^o!
32642:      ux(a)rn/wuxrn ©Av. vohuni\ <*xwrn ©ace.                     10026 wysmy     B
33122:10167 wrn-1 C, S               jju j^f « ^I^UipU jsibjjl £H 10177   wrs    B, S, C                               yj \y
33130:10168 wrn-2                        *ia*l o^J o^                       y^vart-
33143:10169 wrnwpch    B                          jX^^)
33149:10170 wrn'yk'm B                                                  wirat, wrat ©*m-rata-         =»wrm, wrcy*
33166:10172 wrnqyn C                                '^jj* 'j^y*
37117:      zuyt/ ydar (zwyt(t)r) -»zywttr                                 11489 zwrn'k B                                 dhj>«Jl*j
37126:      zuyyak ©f. n. «»zwy                                            11490 zwrn'kcyk B                          Jjj><^3
37133:      zOk ©<*druva =*zwk(>>, 6rwk, jwk                               11491 zwrn'y =4 zwrnik
```


## [2026-10-17T00:02:34.362Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33115,33170p SOD_pages.txt | cut -c1-160; awk 'NR<=33122' SOD_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1"
}
```


### [2026-10-17T00:02:34.818Z] TOOL RESULT

```
                                                            10176 wrr} C                                (j^f Jl^)j^
10166 wrmztjmnw   M                                               urara ? ©Syr.
      u/ormazd-zamnu                                                orarium
      Thursday
                                                                    C2, 57R5, 27, 29; Benv. BSL 1958, 70; Schwartz.
        BBB 724
                                                                      STSC 86; BSTii 903.5, 90427, 29
10167 wrn-1 C, S               jju j^f « ^I^UipU jsibjjl £H 10177   wrs    B, S, C                               yj \y
      warn ©trans, pret. wrnd^r-                                    wars     ©Av. vardsa   ©pi. -t(h)
      OcObelieve, (/cOhave faith                                    hair
      GMS 579; TSP 2.657; STi; BSTi, 142; C2 gloss.
                                                                    VJ 837, 1262, 545; TSP 2.525, 192a, C2, 87V4,
        p230; Frag. Len. 39.5; KG 565; Sund. AoFi                     91R6; Sund. AoFi 1974, lOii R10; AI 1988,
        1974, 6V17
                                                                       185; wrstK VJ 545; Gersh. AHM      p265
10168 wrn-2                        *ia*l o^J o^                       y^vart-
      warn, warn ©Av. vardna ©nom. ob. -y(y);
                                                            10178 wrs»k        B                                 ^J \y
         ace. -w; abl. -1
       faith, belief                                                warse,warsak ©in compd. ^ys'yn wrs>k
                                                                    hair
       GMS 62, 513, 1168n 1; TSP 6.70, 8.168; W-Lii
         547.1; BSTBL 634; Dhu. 88; C2 gloss. p230;               VJ 40d; SCE 88
         KG 603, 610; STii 2.1, 20, 8.7; Sund. AoFviii      10179 wrt S                                          *j*<>y
         1981, 20 Rl, 25V5; BSTii 844.60, 886.18,                   wart ©pi. #wr-
         915.5, 916.5                                               interest
                                                                                    -ty
                                                                    MDii, Nov. 4V8; -h>, Nov. 4V7 p23.8 n p43;
10169 wrnwpch    B                          jX^^)
      warn-apc ?                                                      Gersh. Advice. 93; wryyt, BuguL Insc. B2.13;
                                                                      CII 1990 B23, wrty ?
      (name of cOdrug
             -/
      TSP 8.125, 19.6, 9                                    10180 *wrt M                                            flj7
10170 wrn'yk'm B                                                  wirat, wrat ©*m-rata-         =»wrm, wrcy*
                                        y^^^a
      warnykam ? (wrnykto) ©=Skt. amatya ©pi.                     calm
                                                                    Hen. apud. Gersh. Sogd. Cpds. 145n
       min                                                  10181 wrtn       B, M, S                         oJJ<*j>J
          ist
              e
       BST r Vim 158; SCE 485; TSP 6.16 n p20                       wartan     ©<*wartana ©ob. -y(yh pi. -tld\ ob.
          BL,   .                      7      7

10171 warna
      wrnh B©Av. vardna-, Past.warai ©f. n. '         ^             char     c
      wool                                                             iot, arriag
                                                                    BBB pl3        e
                                                                            7; GMS 33, 1218, 1221; VJ 342, 343,
       TSP 19.20 n p232; Bailey. AO 1966, 43                          751, 769 38e, 39e, 986, 117a, TSP 6.46, 137;
                                                                      SCE 110, 111; BSTBL, Dhu. 15; Vim. 64, 84;
10172 wrnqyn C                                '^jj* 'j^y*
      warn-ken (wrnky(y)n)       ©pi. -tld\ ob. pi. -ty               KG 606; pi. -/, MSP bl21; -d, GMS 1225,
        ^nwwn^ky^h)                                                   1206
       faithful, believing                                  10182 wrtnpV B, S                                    OL><W
       C2, 48R22, 57R16, 88V22; pi. wrnkyynd, BBB                 wartan-par
```


## [2026-10-17T00:02:37.763Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=33122' SOD_pages.txt | grep -o -i 'pdf page [0-9]*\\|leaf [0-9]*' | tail -2; awk 'NR<=33122' SOD_pages.txt | grep -c $'\\f'; grep -n -E '^\\s*(var|2var|var- )' BRT.txt | head; grep -n -E '1360|glauben' BRT.txt | head -10"
}
```


### [2026-10-17T00:02:38.629Z] TOOL RESULT

```
leaf 
477
22800:var»k-  xöAftä
22884:var«8a-
22885:var«8«-
23729:var^zyashva-
2800:der  . .  ?  . .  Das  ist  der  glaubensfeindliche
4376:•  j.  an-aSavan-  Adj.  'nicht  rechtgläubig, ungläubig,  glaubensfeindlich' :  vTsße  asraosö yS  'Sai'anö  (NP.)  vlspe  'iavanS  yS  tanu,- p>r?%B  \.  16.18;  —  zao/a  'sava  adahmd atanu.mO^rd  Yi.  yo.  138.  a)  sonst  von as^maaya-  (sd,  auch  fdSt.):  "sava,  -saonS (GS-),  'saonqm.        [N.  lOg:  lies  asavanim^
6951:•  g.  abmä.rafsnab- Adj.'uns  (den  Priestern) treu  ergeben,  unsres  Dienstes  beflissen"': d3idr  al  tarqs  asSunS  aiacinanhö  aidyüf västrySng  dar>gäi  izyäi  bizvaitl  haxmaim aktnaibyä  'ttatshs  "mach,  dass  die  Ritter glauben  und  nach  dem  Aia  verlangen, dass  die  Bauern  tUchtig  werden  zu  dauern- der eifervoller  fester  Genossenschaft,  für uns  (aber)",  dass  sie  (beide)  uns  treu  er- geben seien"  Y.40.3.
13765:•  j.  'duS.dätay- ''  f  'schlechte  Einsicht, Mangel  an  Einsicht':  'iayä»  (GS.  als  AblS.) fraista  dmantS  "wegen  Mangels  an  Ein- sicht sind  die  meisten  glaubensfeiadlich" Aog.  sOm.
13896:•  g.  duz-varana-  Adi.   'der  den  Miss-         .   .,   _.-  '.,         *        . glauben  hat,  misselaubiB':  'nats  vagsS  r,lsti  ,  ,  ..■,.,
14110:j  glaubensfeindlich';   i)  bes.  im  Gegensatz I  zu  asavan-  (sd,,  Sp.  346  m.,  auch  filr  den »5*
14131:(Sp.  251  u.):  asaonS  ahmi  'vatö  nöit  ahmt Y. /O.  16;  —  fradahäi  vTspayä  alaonS stöis  hamistSe  vupayh  'vatö  j/Si'/ Y.52.4; Ä  8.  10)  von  ajidem  Schöpfungen  der dafiAschta  Welt  'glaubensfeindlich,  ruch- los'; pairi  'valal  mahrkäl  pairi  °vatai a^mät  pairi  drvafhyö^''  ''kaltabys\.$-].ti, YtJO.  93  (wo  'vataiibyü')''''.
19731:tSm  Vi  ala  mjAmaiäl  *htiJtaxaim  (sd.)  Y. 4lS-  ij;  —  sptutjm  ai  %wa  maxdä  nOngkl oAwa  hyat  . .  "als  den  Heiligen  erkannte ich  dich  da,  o  AfAi^  als  . ."  Y.4j.  5; —  atfmcti  akyä  masda  ^wam  mfAAr foMtrDim  vaBi»m{sA.)  Y.2g.  10;  —  matdä yasmmla  vakm^mcä  vafditim  amshmaidl (Angm.)  Y.J5.  7;  —  Xmatyi^  ..  avaiya pama  *^adayä^  (ad.)  ^a*  mana  kartam mailitn  vamavätaiy  tlurvxtam{sA^  *mam- yataiy  Bh.^8; — pass.:  lUAi  aysm  angrS (sd.)  *maüiyae(Kony)  Y.  44. 1 2,  a)  zum praed.  Aide  tritt  der  In&nitiv  'sein':  al ^wä  m^hJ^paaurvlm  .,*yaxüm{sA.)  stSt manaifÄa  Y.JJ.S.  6) Med. 'sich halten fQ[  — ,  sich  voilcommen  wie  — ,  sibi  videri' mit  piaed.  Nom.  eines  Fait  sva.  'glauben, vermeinen  zu  — ':  nmati^m  hs  mariyaZla paraJahlf  "der  mag  ein  Haas  zu  ver- schenken glauben"  V.  /<?.  a8;  — yS  *main~ yäU'^  davayänti  (Sp.  680  o.)  ^rava- n^mta..  Y.i0.i$;  — yS,.na^a  mai^ett jaynvä  "der  . .  und  nicht  geschlagen  zu hai>en   vermeint"   Yljo.  71.  7)    mit
22409:*  j.  va<)a')^n-  m.  EN.  eines  glaubensfeind- lichen  Fürsten:  adavata  ..  aarS  mainyui: ,  ,  tard^uilra  .  .  apastavartuha  .  .  dabtqm mätdayasnJm  vindäi  ystum  ya^a  vindai °nS  (NS.)  ■'  daiähupaitis  ". .  Zar. !  schwör der  maid.  Religion  ab,  um  die  Gunst  zn erlangen,  wie  sie  der  Landesherr  V.  er- langte" V.J5.6;  —  •7a(NS.)  Y.8'\
22743:1)  'etwas  (Akk.)  wählen,  sich  auswählen, sich  entscheiden  für  — ,  sich  überzeugen von  — ,  glauben,  ■n^i^eii%ai' ;  Med.^':  hyat Ti  a.d^aoma  (sd.)  .  .  upa.Jasat  hyat  vir^ natil  (3P.)  acistim  manS  ",  .  so  dass  sie sich  das  schlechteste  Denken  ausenrähl- ten"  Y,^.  6;  —  aya  *niainivS  varata (aPPrM.)  yi  drsgva  aältä  vtryxyS  aitm mainyus  spSnistB  .  .  yascä  .  .  "unter  diesen beiden    Geistern    wählten    sich    der    zur
```


## [2026-10-17T00:02:41.420Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22730,22745p BRT.txt | cut -c1-400; grep -n -E 'xsa[θ9].*vairya|vairya-.*Sp|^.*vairya-  ' BRT.txt | head -5; grep -n -E 'upa\\.?var|adi.?var|aiwi.var' BRT.txt | head"
}
```


### [2026-10-17T00:02:43.000Z] TOOL RESULT

```
•  g.  vayü.bar^t- Adj.'wehe!,  Wehgeschrei anhebend':  'bmdubyS  dui^'ara-hsm  nasal  \  •  '}■>  &.  P-  'var-  V.  'irählen  (usw.)'.  Praes.
Zum  Perf.  de»  V.  via;  -
•  j,  "vavCata'*  F.  i/. PQ.i  nndeullich. —  ■)  Unter  den  Wörtern  mit anlant.  m.    Zweimal  mit  Anlauls-c  geschr.
•  'var-  V,  'hüllend  bedecken';    nur  mit Praev.     Praes.  10  varmav-  :  vamv-,     it
mit  aiwi  'überdecken,  verbergen':  mqna- yptt  bä  . .  ya%a  masyayh  vana  kasyarihqm vanqm  aiwi.vfr^ttvaiti'^  ".  .  wie  ein grösserer  Baum  kleinere  Bäume  verbirgt" V.5-24-
mit  avi  und  kam  'in  etwas  (Lok.)  hinein bergen':  fl  mqnt  ava'ha  vinrunte  (sd., Sp.  1363  m.)  yä^a  anyascU  ariänö  avi x/udrä    x/ährisva    Aam.v^tynavainti'''    V.
mit  h4im  'zudecken,  bedecken':  aitaaa altaÄe  äste  (Sp.  340  m.)  stairisca  bar?nua hqm.v?r»nante  V.5. 59.
ai.  v^nSli,  vfnase. —  Pü.  (1UV.5J:  HÜu/iati't, (zu  V.'  /j):  äfiuiltan').  —  ')  Them.  —  ")  VgL
jr^jäfSM  dngvSui>byd  djfit.antaiibyl>  "den wehe!  rufenden  wird  Üble  Speise  (vorge- setzt)", das  Paradies  (aber)  geht  ihnen verloren,  denZ^n^enossen,  die  das  Recht missachten"  Y.5?.  6.
'vayü  Interj.  'wehe !'.  —  Vgl.  vayöi.  —  Pü. : S  an')daAiiri  tarind  ruvätt  i  »■«.  —  ')  Die Zusammenstellung  Weheruf  und  Qble  Speise als  das,  was  des  Z'rti^anhängers  wartet,  auch Y.  31.  20  und  H.  2.  34,  36.    —    =)    Vgl.    zu
•  j.ya'^a  para  "vayto  nmänamca  vlsimca zatäSuica  datahJuÜa  iii.S:  —  ?  — .
Pü.:    vai  elSii    kac  öi  afi  failäkih  hend  haf
7  väur-'^,  10  v>rmav-,  vamav-''' :  v»rfnv-,  11  v>r>n-  [,25  v?rfnaitä\.  — PPfP.  'vanta-,  PFP.  vairya-;  Inf.  urväm, virmdyäi.
1)  'etwas  (Akk.)  wählen,  sich  auswählen, sich  entscheiden  für  — ,  sich  überzeugen von  — ,  glauben,  ■n^i^eii%ai' ;  Med.^':  hyat Ti  a.d^aoma  (sd.)  .  .  upa.Jasat  hyat  vir^ natil  (3P.)  acistim  manS  ",  .  so  dass  sie sich  das  schlechteste  Denken  ausenrähl- ten"  Y,^.  6;  —  aya  *niainivS  varata (aPPrM.)  yi  drsgva  aältä  vtryxyS  aitm mainyus  spSnistB  .  .  yascä
dby  Google
13^1  'var-i  a
6790:103.         A)  sonst  mit  vairya-  Adj.  (dem  vatum  . .  ah'  ^a.näs}m  vakista.näs^m  (sd.)
10731:Monatstag:  'Gräfte  vairyehe  aySxlustahe . . S.  1. 4;  vgl.  2. 4,  Y.  i6. 3.  aa)  als  Be- zeichnung des  unter  Xs.%  Obhut  stehenden Metalls,  mit  vairya-  Adj.:  kariasät  fra- käraysil  liyra  '^ra  *vairya  V.g.io;  — °ir3i  vairyli  pairiAarim  pairi^araysil V.ij.ß;  —  ayao/ia&um  vä  srum  vä mfyma(sd.)  '^ra  vairyaV,  16,6;  —  *Aqm.- ivqmca  .  .  (sd.)  *upairispata  aka  bastqm ''kr?m  vainm  Yt/0.135.
22982:•  j-i  g-  vairya-  Adj.  (fem.  'yä-)  'zu  wählen, den  man  sich  wählen  soll'^  i)  sva.  'der; beste':  ya%ä  aha  ys  a^a  ratus  a/atcu\ haiä . .  dazda  (sd.)  Y.  27. 1 3,  2)  sva.  'kost- 1 lieh,  wert' :  yssca  tsi  gmä  * afiura.mazda . .  \ aiät  kacä  'ya  (NPf.)  Y.JÄ  i;  —  dars- gahya  *yat>s. .  'yä(GS{.)  rf«/(sd.)  Y.4j. 13;    —  yä  dalnS  -rlm  Aanüt  rnlzdim  .  .
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
4614:•  j.  antama-  Adj.  i)  'der  innerste':  'ma aiwi.varma  "das  innerste  Kleidungsstück" (d.  i.  das  Hemd)  V.  7.10;  —  'ma  aiwyi- fthänS  Vd.  /2  '*.  —  2)  'der  vertrauteste, intimste':  *°m3mcit'''^  sanhs-n  "auch  das vertrauteste  Wort"  F.  j  eJ'.
8445:anttma  aiwi.var7na(s&.)\.7.\o.  ,'if)'höch-  *'  ?'  "™-  fi"^-" *'  S  ^StS-  3  f^  — s'  Pt4 -»       ,       ,    .     .  ,.- j  J.      .      '/,.     ,,         t-aafyii.  —    6>  J  2öi'.  10.  _    7)  Zitat  aus  \.
12595:—  '^avai  Ai  'ma  nStt  upar»Aamäl  Vd,  l(); ig;  — *pairi  °ma  a/sayqn  vJ  'ma  caEsayqn (sd.)  V.  <?.  2;  —  'mazha  .  .  yöi  paiti  äya Zimä  bavainti  (sd.)  uzdatza  usdista  V.  7. 54;  —  nasOm  .  .  •in^m  .  .  Aixnm  V.  5. 16;  —  aeiaiTva  'ma^a  hqmJ>avainti axtisca  garmusea  .  .  V.  7.  57;  58,  55;  — *AixsaSsa  .  .  kimcit  .  .  altalsva  'tnaliva iT^un/Ä  V,  7.  50;  51;  —  nasunqmca  .. 'manqmca    aiwi.varslatiqm  (sd.)   V.5.  14;
13236:—  asdibü ..  rao^a.aiwi.varma  (sd.)  ..  t?/ne faiti  mdai^iiaV.6.  sijÄ 76;  —  iva's.h) . .  tanüm  . .  nida'hamal . .  dar^is'tagA'aläi] fiaiti  gntuh'a  V.6.^i,{.  g)  paiti  mit Gen.:  aurvant^m  "iawä  ,  .  bayB  nida^al
13482:•  j.  däuru.-upa.darana-  d.  'aus  Holz (-Stangen  od.  dgl.)  aufgerichtete  Hütte">: yat  'tu  vä  *tumats.aiwi.varane  vä  spS  nS vä  iri>yai  V.  cV.  1.
16128:•  j.  paradiLvarah-  Adj.  'mit  breiter '  °ni '*  vtoärayöis  avi  fa^am  kaiarascit Brust,  breitbriistig':  pay»/,.''z'iir^(NSm)""vier  Federn  sollst  du  verteilen  auf  den YLJ5.54.  ]Weg'*  nach  beiden  Seiten  hin"  Yt/4-44;
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
18950:•  j.  *namato.-aiwi.varana-'*  n.  'Unter- schlupf,   Hütte    aus  Reisiggeflecht"*:  yat
21940:V  ai  vä  mananha  tastBibya  v°  Y._JJ.  2; 3.  a)  va  . .  va  .  .  im  Sinn  (fast)  von 'et  .  ■  ef  (s.  Sp.  1106  u.)";  a%rä  *vaam baraitl  mi^ahva^ä  V  ^»ns.vaiä  (sd.)  V vldvä  V  rvidvä  v°  Y.  31. 12.  c)  im jAw.;  1)  bei  zwei  Gliedern:  ya^  äauru.- upa.daratu  V  *n)mate.aiwi.varane  V  spä
```


## [2026-10-17T00:02:46.873Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 1316 1303 1803; do echo \"=== $p\"; timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "timeout": 600000
}
```


### [2026-10-17T00:03:03.451Z] TOOL RESULT

```
=== 1316
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1316.png
REF: BQT:1316  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 107  OCR-lang: fas

شهر بار -۱۳۱۹-<
شهریار ۱ - با بای بالف کفیدموبرای | نام ماه هشتم ۴ باشد از سال شمسی » وآن‌بودن
قرشت زده , پادشاهی راگوبند که‌ازهمهٌپادشاهان | آفتاب است در برج سنبله - و نام فرشته ایست
صر خود بزرکتر باشد - وکلاتی وبزرکسدهر | موکل برآش و موکل برجمیع فلزات وتدیین
راهم میگویند . امور و مصالح ماء شهربو رکه روزچهارم است از
شهریده ؟۴ « بروزن فهمیده * بمعنی هرماه شمسی بدو تعلق دارد ۰ درین روز مغان
آکند غاد < ها ۱ جشن کنند وعید سازند بنابر فاعده کلیه که ازد
پرا گنه و پردنان شا 2 ان ۰۳۳۰۶ ۳۶ | ابغان ممتبر است که‌چون ناپروز با نام مامموافد
و پهن گردیده باشد. بغان ممتبر است که‌چون نام‌روز با نام ماه‌موافق
هو و۲ ی : آید هید بای کرد و بسیب آنکه درین روزتولد
۴هریر ۴ رت کش ۰ ۲۳ | واراب واقع شده بود جشن سازند وعی دکنند.
شهربور است که ماء هشتم ۴ شمسی باشد - ویام
۱ است از ومام فر 6 شهر پورگان ۷ - باکاف ا بالف
روز چهارم است از هرماه شمسی رسی
شهر بور ۹ < با واو بروزن برزیگر, کشیده وبنون زده , نام روز چهارم است آزماه
۹ - پهلوی 5۳2۳0704۲ « اوتوالا ۱۹۹ * و 5۳2411۳8901:47 ( نگاهبان شهر ) » از
7 (عپر)۳ 44۳ (از: داغتن) «یبر که۲۱۸» اوستا - 335112111۳6.42۳2 :پهاوی
( کتیبه‌ها) 5824۳048120 «اسشق ۰.۹۷۹۸ ۴ - عملیده (هم.).
۴ - مخفف «شهر پور» (ه.م.) . ۴ - سحیح «ششم» است .
8 - چو در روز شهربرآمد بشهر زشادی همه شهر را داد بهر .
لبیبی . «انجمن آرا» ورك :ح ‎٩‏ ۰
- دراوستا ۷217۷8 35128211078 ۰ پپلوی 5112171۷27: مر کب از:- 251211072
که در اوستا ویارسی باستان وسانسکریت بمعنی کشور وپادشاهی است (رك: شهر) وجزو دوم صفت
است از - ۷2۲ 0 بمعنی برکزیدن . برتری دادن وکرویدن , وثیریه بعنی بر گزیده, وكلمهٌ
مر کب پعنی کشور منتخب با پادشاهی برکزیده . این ترکیب بار ها در اوستا بمعنی بهپشت با
کشور آسمانی آهورمزدا آمده - ونیز نام امشامپندی است که نگهبانی ششمین ماه سال وچهارمین
روز ماه بدو-پرده شده . وی درجمان برین نمابنده پادشاهی ایزدی و فر و اقتدار خداوندی است
ودرجهان مادی پاسبان فلزات میباشد . در کناب الازه‌نة والامکنه تیف امام ابوعلی مرزوقی
اسفهانی ( متوفی 2۷۸ ۸ . ) بجای شهر‌بور «شهربر» ( هام ) آهده « التفپیم مدحح همایی ص
4 و فردوسی طوسی لیز«شهربر» آورده :
زشهریر بادی تو پیرو زگر ۷ بنام بزرکی و فر واهنی (ور4: : ح ه).
آبوربحان بیرولی درفهرست روزهای ایراای نام این ررز را ۶۸ 4هریور » و درسفدی « ختشور »
(حتدور .ن . ل . ) ودرخوارزمی «اخشربوری» یاد کردء . درکالشی (گیلان) 27 5۳3۲1۳۲
نام ماه دهم سال است «روزنامة گیلاشهر سال اول شمارء ۲۲: زندکی وعروسی ساکنن‌جنگل».
درطبری 5122۳۷18.ماز سرانی کنونی ۲8 5۳87۷106 , 228 513۳۷1۲6 ۰ ۳2 5112۳۷2۳6
« واژه نامه 2۷۵ وض ۲۵۸ . هسعود سمدلاغوری کوید:
ای‌تنت‌رازنیکوبی‌ز یور شهرءروزست‌روزشهربور. ‏ «دبوان‌مسعود۹ ۹6ءوراء: روزشماری۷۱-۱۹.
۷ - از : شهربور (ه.م.) ۳ کان ( پوند بت - جشن ) جشنی که درشهر یور روز
(چهارمین روز) از شهربورماه (شدمین ماء) درابران باستان برپا میداشتند. «یورداود. بشتها چاص
۴۳ خرده اوستا ۰۲*۹

=== 1303
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1303.png
REF: BQT:1303  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 94  OCR-lang: fas

۳۳ شنلوك
وگندم و جو ۱ -و بمعنی ربشه باشد آزایریهم شنگویز * - با رار رتحتانی مجهول
و غیوه که بر سر دستار ورویااء و امثال آن‌دوزند | برورن رنگه ریز » بمعنی شنگه‌بیز است و آن
- وجامهٌ ملوت‌زنان ۳ - و جای نایاك سواسطبل | شرابی باشد که ازدرخت خرما بپم رسد ؛ ویجای
را نیز گوبند که آخور باشد. زای نقطه‌دار رای بی نقطه هم بنظر آمده است

شنگلیل ۳ بر وزن و معنی زاجبیل بروزن اردشیر ۱*۶ .
است . شنگه « بفتح اول و ثالث و سکون‌الی,
شنگور ؟ - بر وزن انگور . بادریه | آلت تناسمل راکوبند ۱۱ - و جایی وموضعی را
خمه را کوند. و آن نغته‌ای باشد هدور | نیز گفته اند که در آنجا سرکین و خاشاك
و میان -وراخ که بر سر چوب خیمه محکم وخا کروبه و پلیدی‌ها انبارکنند ۱۴ - و لته‌ای
سازند - و چوب و چرمی را نیز کویند که بر | که زنان در ایام حیض بر فرج نهند۱۳.
کاوی دوك کنند. شنگیار ۱۳ «دبکسر اول وتحتانی بالف
شنگوك * - بر رزن مفلوك , بمعنی کشیده بر وزن کشت زار » لوعی از خیار باشد
آخر شنگور است که بادريهٌ دوك باشد و بعربی وآن دراز وکج میشود .
فلکه خوانند ؛ و باین معنی بجای کاف اول لام شنگینه « ب,فتح‌اودبروزن چرمبنه:چوی
هم آمده است . باشد که خر وگاو را بدان رانند ۱۴ .
شنگول ۱ - بر وزن مقبول * ,معنی شنلت ۱۹ - بنتم اول ولام بروزن‌اند4.
شوخ و ظریف و زیبا باشد :۷ - و دزد وراهزن | بممنی خوشه باشد اعم از خوشم انگور باخرمایا
- و خرطوم فیل را دز کقه‌اند . کندم با جو .
شنگو له ۸ - با وار مجهول بر وزن شنلو لَهُ ۱۱ - بروزن(۱)مفلوك,بادرسة
زنگوله , بمعنی شنگول است که شوخ وظریف ‏ دوك راگویند » و آن چرم با چوبی باشد هدور
و رعنا - و دزد وعیار - وخرطوم فیل باشد. که‌در کلوی دو 4 محکم‌ساز ندوبعر بی‌فلکه‌خوانند.
(9گ چك : بوزن .
۱ - رد : هنك . ۲ -رك دشنگه . ۴ -اظ , مصحف «شنگییل» :

« شنگویر وشنگبیر وشنگویل وشنگییل بوزن ومنی زنجبیل که معرب آدت» «رشیدی» رك :

شنگه بیز () ۴ <- هنگرد (هم.) . 8 مصحف «شنگر4 (هم.) .
له شنگل وشنگوله. رك : شنگه.
۷ - ناکهان بسد دلم «لدار کی شوخکی شنگولکی #یارکی .
مولوی . «فرهنگه اهلام»
۸ *هنگول (هم.) . ۹ < هنگه بیز . ۴ شنگویر باراء +
دنگبیل‌بمعنی زاجبیل است . ر4 : <۳.
۱-تاکی لب است وشنگه زبان‌است ورومه ریش...-وزنی سمرقندی . «فرهنك‌نظام».
۴ - قی: دنگله . ۴۳ - رك : شنکه .
۴- اکر بان دکر کاوی خوری ناکه بر برتیش و بر پهاوی شنگینه .
فرالاوی. « لفت فری ۲۹ ۰*4
رد : شنگله. ۹ مصعف «شنگر4» (وم.) .

=== 1803
(no exact page map; using offset -1205 -> pdf page 598; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1803.png
[transcription from the page image; OCR text in data/verification/sources/refs/ocr/BQT/1803.txt]
[Borhan-e Qate', ed. Mo'in, printed page 1803 = PDF page 600 of BQT_v3_picofile.pdf
 (NOT pdf 598: the running heads read 1801 = pdf 598, 1802 = pdf 599, 1803 = pdf 600,
 1804 = pdf 601, i.e. printed = pdf + 1203 in this region; the earlier cached 1803.txt
 was the OCR of pdf 598 = printed 1801. Running head of this page: «گره».)
 Transcribed from the page image by a vision model, 2026-09-05.]

Headwords on the page (col. 1 -> col. 2):
  گروه ۴ - بضم اول و ثانی بر وزن شکوه ، جماعت مردم را گویند و بعربی قوم خوانند .
  گروهه ۵ - ... بروزن و معنی کلوله است مطلقاً ...
  گروی ۸ - ... نام یکی از خویشان افراسیاب ...
  گرویدن ۹ - ... بمعنی ایمان آوردن و سر باطاعت نهادن و پذیرفتن ...
  گره ۱۰ - بکسر اول و ثانی و ظهور ها ، معروفست اعم ازینکه در ریسمان یا در درخت و امثال
        آن ... و بعربی عقده گویند ... و بمعنی مشکل هم بنظر آمده است ...

Mo'in's etymological footnotes (bottom of the page), verbatim:

  ۴ - پهلوی grôh ( دسته ، گروه ) ، ارمنی ع groh ( ملت ، جمعیت )، بلوچی grôf ،
      ایرانی باستان - *gravathva « نیبرگ ص ۸۴ »، کردی kuruh (اجتماع اشخاص)
      « ژابا ص ۳۳۱ » .

  ۵ - قس : کلوله ، غلوله . مخفف آن «گروهه» .

  ۸ - Guröy ( = Guröi Zirih ) رك : فهرست ولف .

  ۹ - virravistan ( از virrav_ ) (باور کردن ، گمان کردن)، پازند varöistan
      از اوستا - var ، « بارتولمه ۱۳۶۰ » ، « نیبرگ ص ۲۴۴ » و رك : اشتق - هوبشمان ۹۱۲ .

  ۱۰ - پهلوی grah « تاوادیا ص ۱۶۱ : ۲ »، کردی ghiri (گره ، عقد ازدواج) « ژابا
      ص ۳۶۱ » ، از پارسی باستان - *gratha ، سانسکریت grath ( بستن ) « هوبشمان ص۹۳ » .

[Both footnotes are the pages Nourai cites as BQT:1803 for his Old Persian box
 (gratha, gravatha), for Persian گره and, through MON, for گروه.]

[2026-09-06 addition, read from 1803.png by a vision model for pdf page 209 (root Gwer 2):
 the FIRST headwords of the right-hand column of printed p. 1803, above گروه, were
 omitted from the earlier transcription. Verbatim:]

  گرگری ۱ ـ ... فارسی بروزن خروشان، آلت تناسل را گویند ۱ ـ
      و بکسر اول و فتح ثانی، گرو کردنی را یعنی مرهون ـ و بمعنی بنده و عبد هم بنظر آمده است ۲ .

  گروگر ۳ ـ بفتح اول و کاف فارسی بروزن کبوتر، یکی از نامهای خدای تعالی است
      و معنی آن مرادبخش باشد .

Mo'in's footnote ۳ (bottom of the page), verbatim:

  ۳ ـ = گرکر ، ظ . از : gar (garo) (پرستیدن) [قس: گرزمان] در صد و یک نام خدا
      از دعاهای زرتشتیان، نام ۷۳ «گرکر» و نام ۷۴ «گروگر» آمده . رك : خرده اوستا .
      شهرمردان . بمبئی ۱۳۰۸ ص ۳ .
          فرزند تو امروز بود جاهل و عاصی      فردات چه فریاد رسد پیش گروگر .
      « ناصرخسرو بلخی . دیوان ص ۱۷۳ » .

[This is the page Nourai cites in BQT:1793-1806 for garogar «گروگر» "God"; the same
 Naser-Khosrow couplet is the one quoted in the chart. Mo'in glosses گروگر as
 "one of the names of God Most High", meaning مرادبخش ("granter of wishes"),
 apparently from Av./MP gar-, garō- "to worship, praise", cf. گرزمان; nos. 73/74 of
 the 101 names of God in the Zoroastrian prayers (Khordeh Avesta, Shahmardan,
 Bombay 1308, p. 3).]
```


## [2026-10-17T00:03:09.182Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'bāvar|bavar|giraw|girav|ārī|šahrēvar|sahrevar|šahrīvar' HRN.txt | head -15; grep -n -E 'bāvar|bävar|girav|giraw|šahrēvar|ēvar' HUB.txt | head"
}
```


### [2026-10-17T00:03:09.558Z] TOOL RESULT

```
2109:mäz. bavarden^ gel. barden.
18378:m. bavarden 196.
3274:Hier fehlt np. girav, girau (afgh. LW. grau 'a pledge'),
5741:yam (fiir giravam) zu erwartcn.— 163 -
6065:') Ueber giravidan *glauben* siehe § 53,- 172 -
6406:nBk)j ap. naiwa-, geschrieben naiba- *sch5n ; girav, girau
6427:wenden, daher: arm. grav *Pfand* = Sif,*grawa-y np.girav;
8806:garenU' (?) ; giran *schwer H. 898 ; giriftan ergreifen , girav
```


## [2026-10-17T00:03:11.644Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'w.bar|glauben|fürwahr|furwahr' HRN.txt | head -20; grep -n -E 'virr|wurr|glauben' HUB.txt | head"
}
```


### [2026-10-17T00:03:11.983Z] TOOL RESULT

```
327:sprochen. Vielleicht möchte mancher glauben, Fa;Kr
622:16. äri 'fürwahr.
659:Köche zum Sah gehen — fürwahr! und dann ein Mittel ersinnen etc. ?
1457:123. euffärden ^glauben, wähnen*, engüsten, Praes. enrjär-
1462:angärttan glauben, zählen' (Men., AV.); ai. 2 i^kar-
1464:oss. d. analuHj aüyalim ^meinen, glauben', t. änqül-
1658:belegbar seien) gleich aw. ha, bäd, ai. hat 'fürwahr.
1954:Zu [/^var- 'glauben' mit upä (d. i. upa+ä)^),
3137:831. pindUSten 'glauben, dafür halten', Praes. pindärem.
4889:ender (No. 119) mag ich nicht gern glauben, ebenso
7903:912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
7905:ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
7907:oss. t. urnjn (262) 'glauben*.
10202:ap. azda- 'Kunde'; aw. azdä-; ai. addhd 'fürwahr,
10749:135. menitan meinen, glauben \ sehr häutig.
11240:ap. aw. [/^var- 'glauben .
11243:Im Neupersischen ist l^var- 'glauben' in häver
23306:wird ihm kaum jemand glauben, und das konsonantische
801:va-vr-a-) von var glauben' BB. 13, 80 und np. avari
4571:'himmlisch'; phi. mSiiltan meinen, glauben', paz. minfdan
6065:') Ueber giravidan *glauben* siehe § 53,- 172 -
6943:angastan = angdrdan *glauben, halten fiir', pr. angdram,
```


## [2026-10-17T00:03:14.177Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1948,1960p HRN.txt; sed -n 7900,7910p HRN.txt; sed -n 11236,11248p HRN.txt; sed -n 622,640p HRN.txt; sed -n 795,805p HUB.txt"
}
```


### [2026-10-17T00:03:14.510Z] TOOL RESULT

```
1 vergl. säh]bänü 'Conyza' (AM. 162).
g. bänü, banewün 'Königin',
phlv. banük, Bänüki, N. pr. (Hörn, Mitteilungen,
Heft IV, S. 35, ZDMG. 44, 664 No. 92).
bei. bänuk, n. bänux (32).
178**'* bäver 'Glaube'.
Zu [/^var- 'glauben' mit upä (d. i. upa+ä)^),
179. baylsten müssen, nötig sein' (Imperson.), Praes.
^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
Kä§. apä (mit folgendem Futurum), vergl. ßmpeyd
etc. (S. 115).
\i
') Nie selbständig. Ghrest. Schahn. 10 ist hä an suwärän zu
kurd. bei. (100) garm, bei. garmag (LW. ? 101); afy.
yarma\ oss. d. yarm^ t. yarm (90); siyn. gfarw, sar.
iÄrm, gürm,
912. girevtden glauben* jT^in; (Qiss. Dan., Merx' Archiv,
I, 416, 4).
ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
(Mün., AV.), päz. garöldan, garöisn, garavisn (AV.).
oss. t. urnjn (262) 'glauben*.
913. gire 'Hals , girebän 'Halsberge' (arab. LW. jirbän,
Jurrubän).
aw. grTva- 'Nacken (des Berges)'; phlv. (aram.) \l^))i
np. her vereinigt bekanntlich auch sehr viele ver-
schiedene Bedeutungen in sich.
218. varöniand zweifelnd', varömandth 'Zweifel' (AW.-
Komm., Men.).
ap. aw. [/^var- 'glauben .
Zu dem Bedeutungsunterschied vergl. np. guman
Zweifel' und zugleich 'Meinung.
Im Neupersischen ist l^var- 'glauben' in häver
Aoristen auffassen; die griechischen r^-Formen können aber nicht von
fwAtj, ai. vdmifi, das ich besonders vermisse, u. a. getrennt werden.
Bartholomae betont BB. XVII, 110 ff., ebenso wie Brug-
mann, Grundriss I, § 110, das Ablautsverhältniss, das zwischen
ai. / und dem ^, a (i) der übrigen Sprachen besteht, und dieses bietet
16. äri 'fürwahr.
Käs. ore, dre^ drl.
^) Die Endung -ist ist bekanntlich im Afghanischen in der Form
'ist und -ast nicht selten.
*) Bartholomae BB. 17, 111 Anmerkung.6 -
phlv. evar (vd. 5 (146) Gl., Men.), päz. äwar^),
evarih (vd. 5 (146) Gl.). (Darmesteter, Et. ir. I, 251).
phlv. evar führe ich auf ap. *adi -+- [/'var- zurück;
adi (ai. adlii) kommt auch noch in estäden (und
vielleicht in evän, evar (^INZ^N Jer. 5, 6) vor (vergl.
KZ. 32, 581).
17. ärey 'Hass, Feindschaft*, rey,
ap. araika- Teind'; aw. ara^ka-.
Statt ärey ist vielleicht erey zu verbessern (dann
wäre rey die lautgesetzliche Form); die altpersische
Form könnte andernfalls natürlich auch äraika- gelesen
werden.
18. äz 'Begierde' (z. B. Vis und RämTn, Seite 47 Vers 14),
ahmend, azver {äzür),
gehort nicht zu upa + [/^var, sondern ist = paz. vawar
credibly, belief*, Shk. 272, phi. vawar (geschrieben
vapar)^) credible*, West, PT. II, 184, vawari-alto *is
believed*, ebenda 26, arm. vaver, vaver-akan glaub-
wiirdig, giiltig (WZKM 6, 79), an-vaver, an-vaver-akan
'unglaubwurdig, ungiltig, nichtig*. Vgl. zd. vaura- (aus
va-vr-a-) von var glauben' BB. 13, 80 und np. avari
glaubwiirdig oben unter Nr. 16.
179. Np. bdyad 'es steht an* konnte zu ayad *kommt' ge-
horen, also auf phi. "^upayat = ap. *upa -\- aitiy (skr.
upa + eti) zuriickgehen. Aus upO^ konnte nur ba
```


## [2026-10-17T00:03:20.417Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=7850 && NR<=7960' HRN.txt | grep -n -E '^\\s*-? ?[0-9]{3} ?-?\\s*$|— [0-9]{3}|[0-9]{3} —' | head; grep -c $'\\f' HRN.txt; awk 'NR<=7903' HRN.txt | grep -c $'\\f'"
}
```


### [2026-10-17T00:03:20.926Z] TOOL RESULT

```
1:') VuUers s. v. g erden (gerdengäfi).— 202 -
39:Käs. var, varg, mrg\ mäz. vurg.— 203 —
76:da weder ein Gesunder noch ein Kranker es ent-— 204 —
396
217
```


## [2026-10-17T00:03:24.074Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; command ls | grep -i -E 'MON|ARY'; grep -n -E '^(باور|گرویدن|شهریور|آری)\\b' MON_part*.txt 2>/dev/null | head; grep -n -E 'باور|گرویدن|شهریور' incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-17T00:03:24.492Z] TOOL RESULT

```
MON_part1.txt
MON_part2.txt
NYB_vol2_glossary.txt
MON_part2.txt:11868:آریان ۱۳۲۵ ص ۰۱۸۳ قس. صمیمی. 
MON_part2.txt:31874:گرویدن: 0-- 86۲۸۷ (مص‌ل.) (گروید» 
MON_part2.txt:56859:باور کرده شده. کسی که حرف او را حجت 
MON_part2.txt:67643:باور)» دستگیر. 
MON_part2.txt:80343:آریاییان در اعصار باستانی دو فصل گرما و 
MON_part1.txt:2771:آری: 29 (ق. اثبات) کلمه‌ای است برای 
MON_part1.txt:2779:آریغ: 19 [دشمن] (.) کراهت» نفرت» 
MON_part1.txt:5405:آری؛ بلی. 
MON_part1.txt:18595:آریایی» غبر ایرانی] (امر.) غیر ایران» خارج 
MON_part1.txt:21088:باور: ۲ (.) قول سخن» بذبرش قول 
85:باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
532:را بوجود آورد. طسبق این باور مردود کلیه‌ی زبانهای دنیا متعلق به یکی از این سه .
3159:۰ باور
```


## [2026-10-17T00:03:27.017Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2771,2776p MON_part1.txt; sed -n 21086,21094p MON_part1.txt; sed -n 31872,31880p MON_part2.txt; grep -n -E '^شهریور' MON_part2.txt | head -3; sed -n 3150,3175p incoming/ARY/ARY_pages.txt; grep -n -E 'شهریور|گرو' incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-17T00:03:27.588Z] TOOL RESULT

```
آری: 29 (ق. اثبات) کلمه‌ای است برای 
تصدیق امری» بلی» بله؛ مق. نه» نی. 

اریا: 8 قسمت اصلی و ملودیک ابر 
خواننده در این قسمت قدرت و مهارت خود 
را نشان می‌دهد. آهنگی دلکش برای ساز با 


باور: ۲ (.) قول سخن» بذبرش قول 
۳ یقین » اعتقاد. 

باه: (ع.] (.) (پز.) غریزه جنسی و 
شهوانی. قوةٌ جماع» تمایل جنسی. قوة باه: 
(یز.) نیروی شهوانی 

کفت ان 

گرویدن: 0-- 86۲۸۷ (مص‌ل.) (گروید» 
گرود» خواهد گروید؛ بگرو» کر وندهه 
گرویده» گروش). باور کردن: معتقد شدن. 
ایمان آوردن؛ اعتقاد بافتن. اطاعت کردن 
منقار شدن. محبت یافتن. پذیرفتن» قبول 
کردن. 

:
پهلوی (41اتل۸): 20 ‎ -‏ نورس کهن (۱۷0788 010):
سانسکریت (8۷5077): ۷۸5۸۷ ساکسونی کهن (/(54300 00): ۰ ۲۷/۸۲۸
ارمثی ((۸45(4/): لا زان فریزی کهن (40ا5ل۶۸ صا۵): ۰ ۷۷۸35
لاتین (۸710): شاد د دیا آلمانی کهن (۷ل087014 07 آتز صا0):
ایسلند یکین ((7۵ مهم صا۵): ۷۸۸
۷۸7۸ آلمانی (08701۸00): دس ای
زر ی با
[pdf page 109]
۰ باور
انگلیسی ,گهن (5/0/3/7ظ ۰:۵۵ ,۲۷/5۸7 اپرلندی کهن (#اکل۸ا صه). ی ادن |
انگلیسی (ن82للا0/(ق): ۷ برتونی (88870/1): اد 8( بد 11 ری
دانمارکی (0۸0۷1870): ۷۱07 و
سرئدی (/3(780/5): ۷۸ پسگشت‌ها اس ۳
نروژی (/(0/08۷014: ۷78 51 موووهرن ۷
هلندی (070[7): ۷۸5 0 0۸۵ 7
اسلاوی کهن (0//شا5 ۲27064 صا0): 2 (۷۸33) :541
۷۲ (1101130) :۸2(5 ۸ لت
روسی (/81/5542): راد دیا برهان قاطع + ۲۳۴
لینرانی (7214(/142/.): ۸35 ,۷1513178 فرهنگ معین : ۴۷
آغرنی (لتی) (71۸(1ما): در ۱/۱
بادداشست:
۱- 0810818 و 8168۸7 ریشه‌های غیرژرمنی اين واژه نمی‌دهند.
۲- فرهنگ معین و برهان قاطع : و لفت‌نامه‌دهخدا ریشه‌های این واژه را نمی‌دهند. ۱
۳ معنی این واژه در برتونی: دُمل
۴ معلی این واژه در لیتوانی و لتونی: وزغ
231:این دوگروه حا کی از وجود خاستگاه هند و اروپائیان در حدود مرز میان این دو گروه است.
957:یکی از سه اندیشه‌ی بالا بودند. ۱-نوما پامپیلیوس (۳01/211179 111۸ که بنیانگذا رگروه‌های !
1059:شامان بی لیاقت نقش اساسی داشتند. مجلس سنای روم باستان (57381۸7 173۳) و شورای گروسیا
10531:چم اين واژه ذر زبان ابرلندی کهن و ولزی: گروه» گروه سربازان.
10532:چم این واژه در ازبان‌های ژرمنی: گله» دسته‌ی گوسپند یاگاو» گروه.
12834:گرو ۳۳۳
```


## [2026-10-17T00:03:30.104Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3125,3150p incoming/ARY/ARY_pages.txt; sed -n 3175,3200p incoming/ARY/ARY_pages.txt"
}
```


### [2026-10-17T00:03:30.555Z] TOOL RESULT

```
لح
بالو (به چم ازگیل" َْخ) / ۱:۹
ایسلندی‌کهن (۷( 50/070۸ صان): ۳۵88716۸ ,۳018137
881.6 صربی (55781۸(1 ): 3۸
نورس کهن (۸۵۳۹2 صا0): 7( لیتوانی (۸۸1۵2نا717(را): ند ۱۱۸
ساکسونی کهن (/(54200 ۰:۵0 881.6۸0 لنونی (لتی) (7014(۷ا): 75
فریزی کهن (/(۲۸/54 0۵): ۰ 801,688 پروسی کهن (/(۲8۷/۶914 00): 8۸1817118
آلمانی کهن (02704۸07 07ات صا۵): 8۸7.6 ایرلندی کهن (51ل78 010):
آلمانی (/058(44): 37۸6 71 و8016
انگلیسی کهن (801/38 0ا0): ۰ ,8186 ولزی (تکا8): 80۸ ,80
عالا8 ,8۸0 ,88116
انگلیسی (924ا8(0): 88 پسگشت‌ها 5
دانمارکی (0۸(۷/34): 1/0 6 ۶0050
سوئدی (9[780150): 86 ,تا 8 (شتآ88 ,5۵۷5 ‎ )0‏ رام
نروژی (/(۸707(501۵: 21 7 (08910)) :ما۸5
هلندی (7ع0177): 8۸0 7 (113۵۷) :2 2 له ما
لهستانی (۳0/182): 201117 2554 8
۱ ۳3011۸ 8 (طشتاطه :01008
روسی (551(۷): رد ادها 5 (53 0 5841
چکه (2800): برهان قاطع + ۲۳۵
یادداشت:
معنی اين واژه در زبان ژرمنی: کیسهشکم.
معنی این واژه در زبان گوتبکه: مشک شراب,
معلی این واژه در زبان ساکسونی کهن: خشمگین شدن.
1
:
۴ معلی این واژه در لیتوانی و لتونی: وزغ
اوستایی (4۲287221): رومانی (/0۸1۸214). 4۸ ۷0
۸ ۷۸۴۸۲۵ ۷۸۰ گرتبک (007//0): ۷۷1۸0 ,۷۷77۸
پارسی‌باستان (/۶88 صا0): ۷۸ ایسلندی کهن ((010/۸77۸ییه صا0):
پهلری (1اماللم۳). ت۷۸ بشق ۷13 بق۷۹
م۷۸۷۸ ,۱۷28۸3 ساکسونی کهن ((54200 صا0):
افغانی (پشتو) (/4۳0/(7): 3دتا ۷۸ ,۲۵
سانسکریت (54(/58007): ,۷۴ با۷8۸07 فریزی کهن (۷لفا5ت۶۸ ص۵):
71 م۷۳3۸ ,۷۸3۸۸7 ,۲۷۸۸۹۸ ۷۴۸ بش۷
آرمنی (۵//4744): 0 آلمانی کهن (/0570/۸ اهاز صام).
َ یونانی (0820): 0 ولا ۸۲ ,۷۵۲5 ,ت۷۲
لاتین (/710م1): ۷2۵ انگلیسی کهن (577لا5۸/0 010):
فرانسه (بق/۳۸): ۷۹ آلشق ۷ با بشت]۷
ایتالیایی ((ملله5): ۷۱0 انگلیسی (]5/ا8(/0): ۷
[pdf page 110]
باهو (به چم"چوبدستی بزرگ» "دیرک") / ۱۱۱
دانمارکی (157(م0): ند ۵ 8 رها ۱۸۱۸۸۱
سوئدی (8882154): ۷1۸ پسگشت‌ها هراد ]۲
نروژی (۵07۷50140: ۷۳3 ,۷5 ۶0020
هلندی (4لع07): 1 با[۷ 37 (73 ۲ همه
اسلاری کهن (72/ما5 7(#تاتز» 2ا0): :6 /( 021
0 ,۷۵111 2 (3101813) :]ت0۲
لهستانی ([۳01/3): ۲0۵۲۸ 4 (851387) +۸۸25
چک ((ع۲25): ۸ ,۷۵۲ ما۸
اسلواکی (51.0(4): ۵7 ب3۸ظ۷0۵۲ 1 (ت۲۲۳3
لیترانی (۸/1۸04لا727/): :00/7075
```


## [2026-10-17T00:03:36.320Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\" \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%88%D8%B1\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%DB%8C%D8%AF%D9%86\" \"https://en.wiktionary.org/wiki/%D8%B4%D9%87%D8%B1%DB%8C%D9%88%D8%B1\" \"https://www.etymonline.com/word/volunteer\" \"https://www.etymonline.com/word/well\" \"https://www.etymonline.com/word/William\" \"https://www.etymonline.com/word/wealth\"; do timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 539, root Wel 1: etymology check\" 2>&1 | tail -2; done",
 "timeout": 900000
}
```


### [2026-10-17T00:03:40.594Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0170f0d4323f601.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dfe6746f3e315327.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/adb80b6f144d54d0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/96cc64aaeee74141.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/208f78b0d2630076.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6f9c8a679c9b2b0d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f896d3799593f851.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/661edb64ca7492d0.txt
```


## [2026-10-17T00:03:43.437Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in dfe6746f3e315327 adb80b6f144d54d0 96cc64aaeee74141; do echo \"=== $f\"; grep -n -i -A4 'Etymology' $f.txt | head -30; done; for f in c0170f0d4323f601 208f78b0d2630076 6f9c8a679c9b2b0d f896d3799593f851 661edb64ca7492d0; do echo \"== $f\"; wc -c $f.txt; done; grep -n -i -E 'Iranian|wurr|var-' c0170f0d4323f601.txt | head -10"
}
```


### [2026-10-17T00:03:43.811Z] TOOL RESULT

```
=== dfe6746f3e315327
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
--
102: Etymology 
103-
104- 3.2 
105- Noun 
106-
--
183: Etymology
184- [ edit ] 
185-
186- Inherited from Middle Persian 𐭥𐭠𐭯𐭫 ( w'pl /⁠wābar⁠/ ) , [ 1 ] from Avestan 𐬎𐬞𐬁𐬬𐬀𐬭 ( upāvar , “ in belief ” ) , from Proto-Indo-European *upó and either Proto-Indo-European *werh₁- ( “ to speak ” ) or Proto-Indo-European *welh₁- ( “ to wish, desire ” ) . [ 2 ] Compare Old Armenian վաւեր ( vawer ) , an Iranian borrowing.
187-
--
344: Etymology
345- [ edit ] 
346-
347- Borrowed from Classical Persian بَاوَر ( bāwar ) .
348-
--
=== adb80b6f144d54d0
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
135: Etymology
136- [ edit ] 
137-
138- From Middle Persian [Book Pahlavi needed] ( HYMNN-stn' /⁠wurrōyistan⁠/ ) , 𐫇𐫡𐫇𐫏𐫘𐫤 ( wrwyst /⁠wurrōyist[an]⁠⁠/ , “ to believe; to choose ” ) ; regularized based on the present stem 𐫇𐫡𐫇 ( wrw /⁠wurrōy-⁠/ ) .
139-
=== 96cc64aaeee74141
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
147: Etymology
148- [ edit ] 
149-
150- Inherited from Middle Persian 𐭱𐭲𐭥𐭩𐭥𐭥 ( Šahrēwar , “ mere rule ” ) ; name of the third Amahraspand (divine deity) in Zoroastrianism . Compare شهر ( šahr , “ city ” ) .
151-
== c0170f0d4323f601
6003 c0170f0d4323f601.txt
== 208f78b0d2630076
136 208f78b0d2630076.txt
== 6f9c8a679c9b2b0d
131 6f9c8a679c9b2b0d.txt
== f896d3799593f851
134 f896d3799593f851.txt
== 661edb64ca7492d0
133 661edb64ca7492d0.txt
151: Proto-Indo-Iranian: 
155: Proto-Iranian: 
179: Proto-Indo-Iranian: *wr̥nHtáy 
183: Proto-Iranian: *wr̥nHtáy 
193: Proto-Indo-Iranian: *wáras
```


## [2026-10-17T00:03:47.573Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/web/208f78b0d2630076.txt; for u in \"https://en.wiktionary.org/wiki/volunteer\" \"https://en.wiktionary.org/wiki/wealth\" \"https://en.wiktionary.org/wiki/William\" \"https://en.wiktionary.org/wiki/well\" \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C\" \"https://en.wiktionary.org/wiki/volo\"; do timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 539, root Wel 1: etymology check\" 2>&1 | tail -1; done",
 "timeout": 900000
}
```


### [2026-10-17T00:03:50.483Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/volunteer
FETCHED: 2026-10-17T00:03:38Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden/home/sfmqrb/git/rishe-private/data/verification/sources/web/25490600651a7a5f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/655a2369ff645a51.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f322604cca0c5937.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/40ccbebf92997351.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/82f101b0194447c9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/036f36ff3ddf0fc0.txt
```


## [2026-10-17T00:03:53.260Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 25490600651a7a5f 655a2369ff645a51 f322604cca0c5937 40ccbebf92997351 82f101b0194447c9 036f36ff3ddf0fc0; do echo \"=== $f $(sed -n 1p $f.txt)\"; grep -n -A3 '^ *Etymology *$\\|^Etymology' $f.txt | grep -v '^\\-\\-' | grep -E 'From|from|Inherit|Borrow' | head -4 | cut -c1-500; done"
}
```


### [2026-10-17T00:03:53.928Z] TOOL RESULT

```
=== 25490600651a7a5f URL: https://en.wiktionary.org/wiki/volunteer
201- Borrowed from Middle French voluntaire , from Latin voluntārius ( “ willing, voluntary ” ) ; or from voluntary +‎ -eer .
=== 655a2369ff645a51 URL: https://en.wiktionary.org/wiki/wealth
213- Inherited from Middle English welth , welthe ( “ happiness, prosperity ” ) , from Old English *welþ , *welþu , from Proto-West Germanic *waliþu ( “ wealth ” ) . Alternatively, possibly an alteration (due to similar words in -th : compare helth ( “ health ” ) , derth ( “ dearth ” ) ) of wele ( “ wealth, well-being, weal ” ) , from Old English wela ( “ wealth, prosperity ” ) , from Proto-Germanic *walô ( “ well-being, prosperity ” ) , from Proto-Indo-European *wel- ( “ good, best ” ) ; equiva
=== f322604cca0c5937 URL: https://en.wiktionary.org/wiki/William
347- From Middle English William , from Anglo-Norman Willame , from Old High German Willahelm , from Proto-Germanic *Wiljahelmaz (> Latin Gulielmus ), from Proto-Germanic *wiljô ( “ will ” ) + *helmaz ( “ helmet ” ) , ultimately from the Proto-Indo-European roots *welh₁- ( “ to choose, wish, want ” ) and *ḱel- ( “ to cover, conceal, save ” ) , respectively. Cognate with Dutch Willem , German Wilhelm , etc.; cognate borrowings outside of Germanic include Guillaume and Guillermo .
675- From English William , from Anglo-Norman Willame , from Old High German Willahelm , from willo ( “ will ” ) + helm ( “ helmet ” ) .
703- Borrowed from English William .
718- Borrowed from English William , though ultimately of Anglo-Norman origin. Doublet of Guillaume .
=== 40ccbebf92997351 URL: https://en.wiktionary.org/wiki/well
2538- From the accusative of Middle High German wīle , from Old High German wīla , from Proto-West Germanic *hwīlu . Cognate with German weil .
2724- From Middle High German welich , from Old High German welih . Compare German welch .
=== 82f101b0194447c9 URL: https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C
325- Possibly inherited from Middle Persian [script needed] ( ʾywl /⁠ēwar⁠/ , “ certainly, assuredly ” ) , from Old Persian [script needed] ( adi-var , “ in truth, indeed ” ) . [ 1 ] 
396- Inherited from Prakrit 𑀆𑀭𑀸 ( ārā ) + Middle Indo-Aryan -𑀇𑀓𑀸- ( -ikā- ) , from Sanskrit आरा॑ ( ā́rā ) .
=== 036f36ff3ddf0fc0 URL: https://en.wiktionary.org/wiki/volo
302- From Latin volō ( “ to wish ” ) or voli +‎ -o ( nominalizing suffix ) .
```


## [2026-10-17T00:03:56.958Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E 'wel-|welh|PIE|Proto-Indo-European' 40ccbebf92997351.txt | head -8 | cut -c1-400; grep -n -E 'welh|wel-' 655a2369ff645a51.txt | head -3 | cut -c1-600; grep -n 'welh₁' 036f36ff3ddf0fc0.txt | head -3 | cut -c1-300; grep -n -i 'Etymology' -A3 c0170f0d4323f601.txt | head; grep -n -E 'Latin|Germanic|English' c0170f0d4323f601.txt | head"
}
```


### [2026-10-17T00:03:57.714Z] TOOL RESULT

```
441: Proto-Indo-European *welh₁- der. 
449: From Middle English wel , wal , wol , wele , from Old English wel ( “ well, abundantly, very, very easily, very much, fully, quite, nearly ” ) , from Proto-Germanic *wela , *wala ( “ well ” , literally “ as wished, as desired ” ) , from Proto-Indo-European *welh₁- ( “ wish, desire ” ) .
1702: From Middle English welle , from Old English wielle ( “ well ” ) , from Proto-West Germanic *wallijā , from Proto-Germanic *wallijǭ ( “ well, swirl, wave ” ) , from Proto-Indo-European *welH- ( “ to turn; wind; roll ” ) .
2860: English terms derived from the Proto-Indo-European root *welh₁- 
2864: English terms derived from Proto-Indo-European 
2881: English terms derived from the Proto-Indo-European root *welH- 
213: Inherited from Middle English welth , welthe ( “ happiness, prosperity ” ) , from Old English *welþ , *welþu , from Proto-West Germanic *waliþu ( “ wealth ” ) . Alternatively, possibly an alteration (due to similar words in -th : compare helth ( “ health ” ) , derth ( “ dearth ” ) ) of wele ( “ wealth, well-being, weal ” ) , from Old English wela ( “ wealth, prosperity ” ) , from Proto-Germanic *walô ( “ well-being, prosperity ” ) , from Proto-Indo-European *wel- ( “ good, best ” ) ; equivalent to weal +‎ -th ( abstract nominal suffix ) . Cognate with West Frisian wielde ( “ wealth ” ) , 
406: From Proto-Italic *welō , from Proto-Indo-European *welh₁- ( “ to choose, to want ” ) . [ 1 ] Cognate with Sanskrit वृणीते ( vṛṇīté , “ to choose, prefer ” ) , Old English willan ( “ to will, wish, desire ” ) . More at will .
1460: Esperanto terms derived from the Proto-Indo-European root *welh₁- 
1484: Latin terms derived from the Proto-Indo-European root *welh₁- 
83: English 
162: Proto-Germanic: *wiljaną ( from optative ) ( see there for further descendants )
190: Proto-Germanic: *waljaną ( see there for further descendants )
197: Proto-Germanic: *walō ( < *wolh₁-eh₂ ) 
212: Proto-Germanic: *wela ( see there for further descendants )
217: ^ De Vaan, Michiel ( 2008 ), “ volō, velle ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 687 
219: ↑ 2.0 2.1 Kroonen, Guus ( 2013 ), “*weljan- 1”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 578
```


## [2026-10-17T00:04:02.306Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -m3 '^volunteer\\|volunteer,' SKT.txt | cut -c1-300; grep -n -i -m3 'volunteer' KLN_1966.txt | cut -c1-300; grep -n -m3 -E '^Will(iam)?,|^wealth|^Wealth' SKT.txt KLN_1966.txt | cut -c1-300; grep -n -m4 -i -E 'will[,.] *(v|n)\\.|will \\(1\\)|^will' SKT.txt | cut -c1-300"
}
```


### [2026-10-17T00:04:02.725Z] TOOL RESULT

```
3368:arditi,  n.  pi.,  Italian  volunteers  serving  in  storm troops  in  World  War  I.  —  It.,  pi.  of  ardito, ‘brave,  audacious’,  fr.  F.  hard/,  prop.  pp.  of  OF. *hardir,  ‘to  render  courageous’,  lit.  ‘to  make hard’,  fr.  Frankish  *hardjan,  fr.  *hart,  ‘hard’, which  is  rel.
22989:Marsala,  n.,  a  kind  of  wine  produced  in  Sicily.  — So  called  from  Marsala,  a  seaport  in  Sicily,  fr. Arab,  Mirsa-llahi,  lit.  'the  Port  of  God’. Marseillaise,  n.,  name  of  the  French  national Republican  song,  composed  by  Rouget  de  Lisle in  1792.  —  F.,  fern,  
SKT.txt:21257:Wealth;  see  WiU(i).
19451:will.
21479:will  <a),  Kb.,  desit«.  (E.)  M  E.  m'llt, AS.  willa,  sb.  — A.  S.  villan.  to  will ;  see ■Will  (I)  above.  +Dn.  mi/,  led.  vili.  Dan. villie.  Swell,  vilj'a,  G.  wHU,  Rus.s.  volia.
21480:Willow.  lE)  ME.  wiloiv,  wihae  I A.  S.  welig.  -#-  Du.  wilg.  Low  G.  wilge, Wlmberry  ;  see  'Wine. Wimble  (i).  a  gimlet.  (Scand.^  M.E. u'/w^iV. — Dan.  vim/mi,  a  boring-tool:  of which  the  orig.  form  was  probably  vim/tl* or  ttnm/<l*,  as  it  seems  to  be  parallel
```


## [2026-10-17T00:04:04.897Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21470,21479p SKT.txt | cut -c1-600; grep -n -i -m3 'Volunt' SKT.txt | cut -c1-300; grep -n -m3 -E '^volunt' KLN_1966.txt | cut -c1-400; grep -n -m2 -E '^wealth|^William' KLN_1966.txt | cut -c1-400"
}
```


### [2026-10-17T00:04:05.273Z] TOOL RESULT

```
to  wi7/.  sb.  and  vb.  4-  Du.  tmI,  Icel.
lUii.  vf/,  Swcd.  va/,  Goth.  XMu/a,  G.
»W,  well.
ViM     -E)     ME.   wA/*;    K.S.  ttnld, rd.  4- Du.     »';7i/;    icel.   taV/r, .astray,  bewildered,   coofiised ; ^W(Mi.  viU,  G.  UfiVt/.  Goth  vtiUheu. Goth,  wi/iketj  is  formed  with  a tiom  tv</-,  base  of  wiJ/att,  to  will,
WIMPLE.
S63
Irish,  and  means  'actuated  by  will;*  so aUo  Icel.  vi//r,  wondering  at  will,  whence Lowl.  Sc.  w(V/.  astray.  Cf.  \S  gwyUt,  wild, allied  to  W.  gwyllys,  the  will.
wildemeas,  a  waste  place.  (E.)  M.  E. u'Udirmsu,  Layaffion,^o335;  it  stands  for wiiJtmnesst*.  We  also  find  M.  E. v/iidime,  a  desert,  formed,  with  adj.  sufhs •H  from  A. S.  wilder,  a  wild  animal;  so that  wildem  «  belonging  to  wild  animals, hence,  a  waste  place.  Tne  A.  S.  wil(Ur  is short  for  wild  dtdr,  a  wild  animal ;  sec Door.     Dor.  be-ioil-der.
wilful.  (E.)  ME.  wilful;  formed with  suffix  ■jfui  from  M.  E.  wil-U,  will;  see will  (a)  below.
will  <a),  Kb.,  desit«.  (E.)  M  E.  m'llt, AS.  willa,  sb.  — A.  S.  villan.  to  will ;  see ■Will  (I)  above.  +Dn.  mi/,  led.  vili.  Dan. villie.  Swell,  vilj'a,  G.  wHU,  Rus.s.  volia.
21049:Voluntary.  {V.  -  L.)  F.  voluHtairt^ vploHtairt.  ■•  L.  ato/un/artHS,  willing,  m L,  uoiuntas,  free  will.  — L.  mo/uhs  *,  by- form  of  uoJens,  willing,  from  «///<,  to  wt<h, tia/o,  I  wish.-fGk.  0ov\ofuu,  I  wilt;  Ski vri,  to  choose,  select.  Allied  to  WIU. (VWAR.)
19846:voluntary.
5009:William.
```


## [2026-10-17T00:04:16.934Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | grep -n -E 'PROBLEM|required|consulted|sources' | head -40"
}
```


### [2026-10-17T00:04:17.374Z] TOOL RESULT

```
79:                for c in vn.get("consulted") or []:
86:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
90:        print("PROBLEM:", p)
```


## [2026-10-17T00:04:18.594Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,95p tools/verify_check.py"
}
```


### [2026-10-17T00:04:18.907Z] TOOL RESULT

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
```


## [2026-10-17T00:04:19.920Z] AGENT

Now writing the verification file.


## [2026-10-17T00:06:03.355Z] TOOL CALL #44: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-539.json",
 "content": "{\n  \"pdf_page\": 539,\n  \"book_page\": 509,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Wel 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *welh₁- 'to choose, wish, want' (Pokorny 2. u̯el- 1137 'to wish; to choose'; LIV 677; AHD wel-2)\",\n      \"note\": \"Root, language label and gloss are correct: Pokorny p. 1137 '2. u̯el-, u̯lei- ... to wish; to choose', with Av./OP var- 'choose, want, desire, will' and 'also Avestan var- \\\"believe\\\"', Latin velle, Gothic wiljan. Watkins/AHD wel-2 'To wish, will' covers well, wealth, will and Latin velle (VOLUNTARY). Cheung (EDIV *u̯arH²) files Av. var-, MP wurrōy-, Sogd. wrn-, NP giravīdan and bāvar under PIE *u̯elH₁-. Note that Walde-Pokorny (I 294) put Av. var- 'glauben' under *u̯er- 'Freundliches erweisen' instead, which is the alternative Nourai flags in his note ('See Wer 1'); modern work (Cheung, LIV) assigns the Iranian 'choose/believe' verb to *welh₁-.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *welh₁- «برگزیدن، خواستن، آرزو کردن» (پوکورنی ص ۱۱۳۷؛ واتکینز/AHD wel-2) واقعی است و برچسب و معنای آن درست آمده است. پوکورنی خود فعل اوستایی و پارسی باستان var- «برگزیدن، خواستن» و نیز var- «باور داشتن» را زیر همین ریشه می‌آورد، و چونگ (۲۰۰۷) گرویدن و باور فارسی و wrn سغدی را نیز از همین ریشه می‌داند. والده‌ـ‌پوکورنی var- «باور داشتن» را به ریشهٔ دیگر *u̯er- برده بودند، و این همان احتمالی است که نورایی در یادداشت «Wer 1» به آن اشاره کرده است؛ پژوهش امروزی ریشهٔ *welh₁- را ترجیح می‌دهد. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1137\", \"status\": \"supports\", \"note\": \"POK_full.txt l.90262-90321, 'Page(s): 1137-1138': 'Root / lemma: uel-2 ... Meaning: to wish; to choose ... Avestan ap. var- \\\"choose, want, desire, will\\\" ... also Avestan var- \\\"believe\\\" ... Latin volo, vult, velle ... Gothic wiljan'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 294 (WLD_Bd1_pages.txt l.27920-27960)\", \"stance\": \"partial\", \"note\": \"'2. u̯el- (auch *u̯elei-) „wollen, wählen“ ... av. ap. var- „wählen, wollen“ ... auch av. var- „glauben“ (s. unter *u̯er- „Freundliches erweisen“) ... lat. volo, velle' — same root, but Av. var- 'believe' referred to *u̯er-.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wel-2 (AHD_watkins1985.txt l.1140)\", \"stance\": \"supports\", \"note\": \"'wel-2. To wish, will. 1. Germanic *wel- in Old English wel, well ... 2. ... wela ... WEAL, WEALTH. 3. ... willa ... WILL ... 7. Basic form *wel- in Latin velle (present stem vol-) ... VOLUNTARY ... [Pok. 2. u̯el- 1137.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, uel- (1) (IEC.txt l.19931)\", \"stance\": \"supports\", \"note\": \"'uel- (1) \\\"wish, will, command\\\" ... Av. var-, v. (3) \\\"wish\\\"; varo, adj. \\\"desired\\\"; vairyo \\\"desirable\\\" ... Lat. volo, inf. velle ... Go. wiljan'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 420-421 s.v. *u̯arH² (CHEUNG.txt l.27240-27300)\", \"stance\": \"supports\", \"note\": \"'PIE *u̯elH₁- \\\"to want, wish\\\" = LIV 677 f. | Pok. 1137 f. ... IE cognates: Lat. volo \\\"I want\\\" ... Goth. wiljan ... Engl. will'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"var 2, ver 1, varena; upa-var; adi-var; xšatra-vairya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan ²var- 'to choose; (mid.) to convince oneself, believe' (Bartholomae col. 1360 f.: 'etwas wählen ... sich überzeugen von —, glauben'; pres. vərəna-/vərənav-, OAv. varənē, OP v(a)rnavataiy) is the regular Indo-Iranian reflex of *welh₁- (cf. Skt. vṛṇīté 'chooses'); varəna- 'choice, belief' is attested (the base of Sogd. wrn). xšaθra- vairya- 'the desirable dominion', the Aməša Spənta Xšaθra Vairya, is genuine: vairya- is the gerundive 'to be chosen, desirable' of the same verb; Nourai's 'desired city, heavenly country' is a loose rendering (xšaθra- means 'dominion, kingdom', not 'city'; Mo'in explains it as 'کشور منتخب ... بهشت یا کشور آسمانی'). The two prefixed forms are not attested Avestan words: upa-var (upā-var) is Horn's reconstruction for bāvar, and adi-var Horn's Old Persian *adi-var for Pahlavi ēvar, so they are plausible reconstructions at best. 'var 2, ver 1' are Nourai's homonym numbers ('ver' is not a separate Avestan word).\",\n          \"derivation_fa\": \"فعل اوستایی var- (در فرهنگ بارتولومه ²var-) به معنای «برگزیدن» و در ساخت میانه «خود را قانع کردن، باور داشتن» بازتاب منظم *welh₁- هندواروپایی است (سنج. سنسکریت vṛṇīte «برمی‌گزیند») و varəna- «گزینش، باور» نیز در اوستا هست. xšaθra- vairya- «شهریاری آرمانی، کشور برگزیده» نام امشاسپند شهریور است و vairya- صفت فعلی همین فعل به معنای «برگزیدنی» است؛ معنای «شهر» برای xšaθra دقیق نیست (یعنی «شهریاری، کشور»). اما upa-var و adi-var واژهٔ گواهی‌شدهٔ اوستایی نیستند و بازسازی‌های هرن برای «باور» و «ایور» پهلوی‌اند؛ از این رو ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1137\", \"status\": \"supports\", \"note\": \"POK_full.txt l.90272: 'Avestan ap. var- \\\"choose, want, desire, will\\\" (3. Pl. preterit Med. varata ...) ... vairya- \\\"the best, delicious, worth\\\"; also Avestan var- \\\"believe\\\"'.\"},\n            {\"ref\": \"DVS:198\", \"status\": \"not_checked\", \"note\": \"Davies, Roots (1981): lending-only copy on archive.org (refs_online.json), not accessible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1360 f. s.v. ²var- (BRT.txt l.22730-22745); s.v. vairya- (l.22982); xšaθra- (l.10731)\", \"stance\": \"supports\", \"note\": \"'²var- V. \\\"wählen (usw.)\\\" ... 1) \\\"etwas (Akk.) wählen, sich auswählen, sich entscheiden für —, sich überzeugen von —, glauben\\\"'; 'vairya- Adj. \\\"zu wählen, den man sich wählen soll\\\"'; xšaθra- with 'vairya- Adj.' as name of the metal under Xšaθra's care. No upa.var or adi.var found (grep 'upa.?var|adi.?var' gives only aiwi.var- 'cover').\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 420 *u̯arH² (CHEUNG.txt l.27240-27250)\", \"stance\": \"supports\", \"note\": \"'AVESTAN: var- \\\"to choose; to convince\\\" || (+ *fra-) \\\"to choose\\\" ... OLD PERSIAN: v(a)r- \\\"to choose, convince\\\" = Kent 206b'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 178 (HRN.txt l.1953-1954) and no. 16 (l.622-636)\", \"stance\": \"partial\", \"note\": \"'bāver \\\"Glaube\\\". Zu √var- \\\"glauben\\\" mit upā (d. i. upa+ā)'; 'phlv. ēvar führe ich auf ap. *adi + √var- zurück' — the source of Nourai's upa-var and adi-var, presented as Horn's own derivations, not attested words.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"varavistan; paver; ěvar; šatri-var\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"varavistan is a genuine Pazand reading of the Pahlavi verb written HYMNN-stn' (MMP wrwystn), now read wurrōyistan/virrōyistan 'to believe; choose' (MacKenzie; Nyberg: 'FrP 18 gives the Paz. readings viravistan, varvistan'), from OIr. *u̯r̥nH-/var- 'choose'. 'paver' is not a Pahlavi word: the Book-Pahlavi word for 'belief, truth' is written w'pl and read wābar/wāwar (MacKenzie 'wābar [w'pl | M wbr, (N bāwar)] truth; belief'; Nyberg 'BP always w'pl-'; Hübschmann 'phl. vāwar (geschrieben vapar)'), Parthian wāwar; the book prints 'paver', apparently a garbled rendering of the older reading vāpar/vāvar — a misprint in the book, faithfully extracted. ēvar 'certain(ly), indeed' is MP ēwar (MacKenzie, Nyberg). šatri-var is a letter-by-letter rendering of the Pahlavi spelling štr'ywr of Šahrēwar, the third Amahraspand and name of the 6th month and 4th day (MacKenzie, Nyberg 'Borrowed from Av. xšaθra-vairya-'); the correct reading is Šahrewar.\",\n          \"derivation_fa\": \"«varavistan» خوانش پازند فعل پهلوی wurrōyistan / virrōyistan «باور کردن، گرویدن» است (مکنزی؛ نیبرگ خوانش‌های پازند viravistan و varvistan را می‌آورد). «paver» واژهٔ پهلوی نیست: واژهٔ پهلوی «باور» به خط w'pl نوشته و wābar / wāwar خوانده می‌شود (مکنزی، نیبرگ، هوبشمان: «نوشته‌شده vapar»)؛ پس «paver» خطای چاپی خود کتاب است و استخراج درست انجام شده. ēvar «همانا، به‌راستی» درست است. «šatri-var» حرف‌نویسی خط پهلوی štr'ywr است که «شهریور» (Šahrēwar) خوانده می‌شود و از xšaθra- vairya- اوستایی آمده است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"paver\",\n          \"correct_form\": \"wābar / wāwar (Book Pahlavi w'pl, Pazand vāwar, Parthian wāwar)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%88%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%87%D8%B1%DB%8C%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1316\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1316 (BQT_v3_picofile.pdf p.107) s.v. شهریور, Mo'in's footnote: 'پهلوی šahrēvar ... (نگاهبان شهر) ... اوستا xšaθra vairya ... جزو دوم صفت است از var بمعنی برگزیدن، برتری دادن وگرویدن، وئیریه بمعنی برگزیده' — supports šatri-var/Šahrewar and the var- link.\"},\n            {\"ref\": \"BQT:1303\", \"status\": \"not_found\", \"note\": \"ref_page.py BQT:1303 (pdf p.94) shows the شنگ... headwords (شنگلیل، شنگول، شنگه); no باور/ایور/گرویدن entry on that page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"s.vv. wurrōyistan, wābar, Šahrewar (PHD.txt l.657, 603, 583)\", \"stance\": \"supports\", \"note\": \"'wurrōyistan, wurrōy- [HYMNN-stn' ... M wrwyst, (wrw-) ... N ... girawidan] believe; choose'; 'wābar [w'pl | M wbr, (N bāwar)] truth; belief'; 'Šahrewar [štrywr | N ~] Best Rule, the third Amahraspand ... cal. 6th month; 4th day'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual II s.vv. virrōyistan (l.4191), vāparīkānēh (l.3934-3940), Šahrēvar (l.3591)\", \"stance\": \"partial\", \"note\": \"'FrP 18 gives the Paz. readings viravistan, varvistan ... NP giravidan is due to the coalescence of this vb. and the den. of girav'; for vābar: 'BP always w'pl- ... Paz. vāwar \\\"truth\\\"', derived from a crossing of *vā-vara- (var- 'choose') with *pā-para- (par- 'fill'); 'Šahrēvar ... Borrowed from Av. xšaθra-vairya-'.\"},\n            {\"src\": \"HUB\", \"where\": \"note to Horn no. 178 (HUB.txt l.795-803)\", \"stance\": \"partial\", \"note\": \"'[bāvar] gehört nicht zu upa + √var, sondern ist = paz. vāwar \\\"credibly, belief\\\" ... phl. vāwar (geschrieben vapar) \\\"credible\\\" ... arm. vawer ... Vgl. zd. vāura- (aus va-vr-a-) von var \\\"glauben\\\"' — explains the source of the 'p' in Nourai's 'paver'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"geravîdan «گرویدن»; bâvar «باور»; ârî «آری»; Šahrîvar «شهریور»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"(a) گرویدن giravīdan 'to believe, adhere to' < MP wurrōy-/wurrōyistan with regular initial wu- > gu-/gi- (Nyberg: 'vu- always > gu-'), regularized on the present stem; Cheung, Horn no. 912, Mo'in and Wiktionary all agree — confirmed (Nyberg adds that the NP verb merged with the denominative of girav 'pledge'). (b) باور bāvar < MP wābar/wāwar, Parth. wāwar (Arm. loan vawer); Horn's upā + var-, Nyberg's/Hübschmann's reduplicated *vā-var(a)-, and Cheung's 'old intensive' all put it on Av. var- 'believe', which Cheung derives from *welh₁-; Wiktionary leaves open *werh₁- or *welh₁-. Nourai's note pointing to 'Wer 1' records exactly this alternative; current scholarship (Cheung, LIV) prefers *welh₁-, so the chart's main placement stands — confirmed in substance. (c) آری ārī 'yes, indeed' < MP ēwar < OP *adi-var is only Horn's 1893 conjecture; Nyberg gives the NP reflex of ēvar as āvar, and Wiktionary's 'possibly' cites Nourai himself — plausible only. (d) شهریور Šahrīvar < MP Šahrēwar < Av. xšaθra- vairya- 'desirable dominion', MP ē > NP ī, the 6th month and 4th day of each month — confirmed (Mo'in, MacKenzie). The book's gloss 'forth day' is a spelling slip for 'fourth'.\",\n          \"derivation_fa\": \"«گرویدن» از فارسی میانهٔ wurrōy- / wurrōyistan «باور کردن» است؛ wu- آغازی در فارسی نو به گُ/گِ بدل شده (نیبرگ)، و چونگ، هرن (شمارهٔ ۹۱۲) و معین هم همین را می‌گویند. «باور» از فارسی میانهٔ wābar / wāwar (پارتی wāwar، وام‌واژهٔ ارمنی vawer) و از ساخت دوگانی یا پیشوندی فعل var- «باور داشتن» است؛ چونگ آن را از *welh₁- می‌داند، پس یادداشت نورایی دربارهٔ احتمال «Wer 1» نیز با احتیاط کنار گذاشته می‌شود. «شهریور» از Šahrēwar پهلوی و xšaθra- vairya- اوستایی است (ē میانه در فارسی نو ī شده). اما «آری» از ēwar پهلوی تنها حدس هرن است و نیبرگ بازماندهٔ ēwar را «آور» می‌داند؛ از این رو کل این گره با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D9%88%DB%8C%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%88%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%DB%8C\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%87%D8%B1%DB%8C%D9%88%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1803\", \"status\": \"supports\", \"note\": \"ocr/BQT/1803 vision transcription, s.v. گرویدن 'بمعنی ایمان آوردن و سر باطاعت نهادن'; footnote ۹: 'virravistan (از virrav-) (باور کردن، گمان کردن)، پازند varōistan از اوستا var- «بارتولمه ۱۳۶۰»، «نیبرگ ص ۲۴۴»'.\"},\n            {\"ref\": \"BQT:1316\", \"status\": \"supports\", \"note\": \"BQT_v3 pdf p.107 s.v. شهریور: 'نام ماه ششم ... و نام فرشته ایست موکل بر ... جمیع فلزات ... روز چهارم است از هرماه'; footnote derives it from Av. xšaθra vairya, var- 'برگزیدن ... وگرویدن'.\"},\n            {\"ref\": \"HRN:203\", \"status\": \"supports\", \"note\": \"Horn p. 203 (HRN.txt l.7903-7907, between page marks 203 and 204) no. 912: 'girevīden \\\"glauben\\\" ... ap. aw. √var- glauben; phlv. varav(i)stan ... päz. garōīdan'. Horn also has bāver no. 178 'Zu √var- \\\"glauben\\\" mit upā' and ārī no. 16 '< phlv. ēvar ... ap. *adi + √var-'.\"},\n            {\"ref\": \"MON:2098\", \"status\": \"partial\", \"note\": \"6-volume Mo'in page not on disk; the abridged Mo'in (MON_part2.txt l.31874) s.v. گرویدن: 'باور کردن، معتقد شدن، ایمان آوردن' and (MON_part1.txt l.21088) باور 'قول ... یقین، اعتقاد' — meanings confirmed, page unverifiable.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 421 *u̯arH² (CHEUNG.txt l.27284-27287)\", \"stance\": \"supports\", \"note\": \"'NP giravidan \\\"to believe, confide in; to obey\\\", NP bavaridan (denomin.?) \\\"to believe; credit\\\", NP bavar \\\"belief; credit\\\" (< old intensive)'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual II l.4191 and l.1470 (cited in page-154 check)\", \"stance\": \"partial\", \"note\": \"'NP giravidan is due to the coalescence of this vb. and the den. of girav'; 'ēvar ... NP āvar \\\"true, certain\\\"' — a different NP outcome from آری.\"},\n            {\"src\": \"HUB\", \"where\": \"note to Horn 178 (HUB.txt l.795-803)\", \"stance\": \"partial\", \"note\": \"bāvar 'gehört nicht zu upa + √var, sondern ist = paz. vāwar' from 'va-vr-a- von var glauben' — same root, different formation.\"},\n            {\"src\": \"PHD\", \"where\": \"s.vv. wābar, Šahrewar\", \"stance\": \"supports\", \"note\": \"'wābar ... (N bāwar)'; 'Šahrewar [štrywr | N ~] ... cal. 6th month; 4th day'.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 109-110], entry باور (l.3159-3185)\", \"stance\": \"supports\", \"note\": \"Aryanpur's باور entry lists Avestan, Old Persian, Pahlavi, Sanskrit, Latin, Gothic and Old English cognates (OCR garbled: 'اوستایی ... پارسی‌باستان ... پهلوی ... لاتین ... گوتیک'), i.e. the *wel- 'wish' family; also cites 'برهان قاطع ۲۳۴، فرهنگ معین'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sogdian\",\n          \"words\": \"wrn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian wrn /warn/ 'faith, belief' (Buddhist, Christian and Manichaean texts) continues OIr. *varna- = Av. varəna- 'choice, belief', the noun of var- 'choose, believe'; there is also the verb wrn- 'to believe, have faith' and the adjective wrnkyn 'faithful'. Gharib's dictionary (no. 10168) and Cheung both give it, so the arrow straight from the PIE root (via Old Iranian) is correct.\",\n          \"derivation_fa\": \"واژهٔ سغدی wrn (warn) «ایمان، باور» دنبالهٔ ایرانی باستان *varna- و هم‌ریشه با varəna- اوستایی «گزینش، باور» است؛ فعل wrn- «ایمان داشتن» و صفت wrnkyn «مؤمن» نیز در سغدی هست. فرهنگ قریب (شمارهٔ ۱۰۱۶۸) و چونگ هر دو آن را می‌آورند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:412\", \"status\": \"supports\", \"note\": \"SOD_pages.txt l.33122-33135, leaf 477 (printed ≈ leaf − 66 = p. 411/412): '10167 wrn-1 ... warn ... believe, have faith'; '10168 wrn-2 ... warn ← Av. varəna ... faith, belief'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 420 *u̯arH² (CHEUNG.txt l.27265)\", \"stance\": \"supports\", \"note\": \"'SOGDIAN: CSogd. wrn-, MSogd. wrn- \\\"to have faith, believe\\\"'.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1360 f. ²var-\", \"stance\": \"supports\", \"note\": \"the Avestan base var-/vərəna- 'wählen ... glauben' (see node #1).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through box for Proto-Germanic: *welh₁- gave *wiljaną/*wiljô 'will', *wela 'well' (lit. 'as wished') and *walô 'well-being' (AHD wel-2; Kroonen *weljan-), which feed node #6.\",\n          \"derivation_fa\": \"این خانه گذرگاه ژرمنی آغازین است: از *welh₁- صورت‌های *wiljaną / *wiljô «خواستن، اراده»، *wela «خوب، چنان‌که خواسته شده» و *walô «بهروزی» پدید آمده‌اند که واژه‌های انگلیسی گرهٔ بعد از آن‌هاست. درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins wel-2: 'Germanic *wel- ... Germanic *welon- ... Germanic *wiljōn- ... Germanic *wil(l)jan'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1137\", \"stance\": \"supports\", \"note\": \"'Gothic wiljan, Old High German willu, wellan ... Gothic wilja, Old High German willo'.\"},\n            {\"src\": \"IEC\", \"where\": \"uel- (1)\", \"stance\": \"supports\", \"note\": \"'Go. wiljan, wv. \\\"wish\\\"; wilja ... OE willan ... ON vilja'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"well 1; wealth, will, William\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"well (adv./adj. 'good') < OE wel < PGmc *wela 'as wished' < *welh₁- (AHD wel-2, Wiktionary). wealth < ME welthe, from wele (OE wela 'prosperity', PGmc *walô < *wolh₁-eh₂) + abstract -th, formed on the analogy of health (Wiktionary also mentions a separate *wel- 'good', but AHD and the PIE page put *walô under *welh₁-). will (noun and verb) < OE willa / willan < PGmc *wiljô / *wiljaną. William < Anglo-Norman Willame < OHG Willahelm = willo 'will, desire' + helm 'helmet, protection', brought to England by the Normans in 1066.\",\n          \"derivation_fa\": \"well (به معنای «خوب») از انگلیسی کهن wel و ژرمنی *wela «چنان‌که خواسته شده» است؛ wealth «ثروت» از wele / wela «بهروزی» با پسوند -th ساخته شده؛ will «اراده، خواستن» از willa / willan انگلیسی کهن است؛ و نام William از آلمانی علیای کهن Willahelm (willo «اراده» + helm «کلاه‌خود») است که نورمان‌ها پس از ۱۰۶۶ به انگلستان آوردند. همه از *welh₁- اند و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/well\",\n            \"https://en.wiktionary.org/wiki/wealth\",\n            \"https://en.wiktionary.org/wiki/William\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins wel-2: 'Old English wel, well (< \\\"according to one's wish\\\"): WELL ... wela, weola, well-being, riches: WEAL, WEALTH ... willa, desire, will power: WILL'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. will (SKT.txt l.21470-21479)\", \"stance\": \"supports\", \"note\": \"'will (2), sb., desire. (E.) ME. wille, AS. willa, sb. — AS. willan, to will ... Du. wil, Icel. vili ... G. wille, Russ. volia'; 'Wealth; see Well (1)' (l.21257).\"},\n            {\"src\": \"POK\", \"where\": \"p. 1137\", \"stance\": \"supports\", \"note\": \"Germanic wiljan/willo forms listed; 'about Gothic waila, OHG wela, wola \\\"well\\\" compare Feist 543' — Pokorny hesitant about 'well', AHD and Kroonen accept it.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"velle, vol\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin volō, velle 'to wish, want' (present stem vol-, infinitive velle < *wel-se with assimilation) < Proto-Italic *welō < PIE *welh₁-; derivatives voluntās 'will' and voluntārius 'willing'. Pokorny, AHD, Mann and de Vaan (via Wiktionary) all agree.\",\n          \"derivation_fa\": \"فعل لاتین volō / velle «خواستن» (ستاک حال vol-، مصدر velle از *wel-se با همگونی) از ایتالیک آغازین *welō و *welh₁- هندواروپایی است؛ voluntās «اراده» و voluntārius «داوطلبانه» از آن ساخته شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/volo\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welh%E2%82%81-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins wel-2 §7: 'Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1137\", \"stance\": \"supports\", \"note\": \"'Latin volo (*velo), vult (*velt), velle \\\"want, desire, will\\\" (Opt. velim), voluntas'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 294\", \"stance\": \"supports\", \"note\": \"'lat. volo (*velo), vult (*velt), velle „wollen“'.\"},\n            {\"src\": \"IEC\", \"where\": \"uel- (1)\", \"stance\": \"supports\", \"note\": \"'Lat. (*-e- or *-o-) volo, inf. velle, defect. vb. \\\"wish\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"volunteer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"volunteer (1600s, first military 'one who offers himself for service') < Middle French voluntaire/volontaire < Latin voluntārius 'willing, voluntary' < voluntās 'will' < volō, velle; the ending was assimilated to English -eer. Wiktionary and Skeat (s.v. voluntary) give this chain.\",\n          \"derivation_fa\": \"volunteer «داوطلب» (سدهٔ هفدهم، نخست در معنای نظامی) از فرانسوی میانه volontaire و لاتین voluntārius «به خواست خود» از voluntās «اراده» و فعل volō / velle است؛ پایانهٔ آن در انگلیسی به -eer همانند شده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/volunteer\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of Nourai's own (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"s.v. Voluntary (SKT.txt l.21049)\", \"stance\": \"supports\", \"note\": \"'Voluntary. (F. – L.) F. voluntaire, volontaire. – L. uoluntarius, willing, – L. uoluntas, free will ... from uelle, to wish, uolo, I wish ... Allied to Will'.\"},\n            {\"src\": \"AHD\", \"where\": \"wel-2 §7\", \"stance\": \"supports\", \"note\": \"VOLUNTARY listed under Latin velle.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:06:03.412Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-539.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:06:04.707Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-539.json >/dev/null && python3 tools/verify_check.py 539"
}
```


### [2026-10-17T00:06:05.271Z] TOOL RESULT

```
nodes verified: 8/8
node verdicts: {'plausible': 2, 'transcription_suspect': 1, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_checked': 2, 'not_found': 1, 'partial': 1}
books consulted: {'supports': 17, 'partial': 5} | by book: {'CHEUNG': 3, 'POK': 3, 'BRT': 2, 'PHD': 2, 'NYB': 2, 'HUB': 2, 'IEC': 2, 'SKT': 2, 'HRN': 1, 'ARY': 1, 'WLD': 1, 'AHD': 1}
```


## [2026-10-17T00:06:14.859Z] TOOL CALL #46: SubagentHandback

```json
{
 "message": "I wrote the page 539 (book p. 509) file, root \"Wel 1\", to /home/sfmqrb/git/rishe-private/data/verification/page-539.json. The JSON is valid, and `verify_check.py 539` checked all 8 of 8 nodes and printed no PROBLEM lines.\n\n- **Root:** confirmed. It is PIE *welh₁- \"to choose, wish\" (Pokorny p. 1137). Watkins (AHD wel-2), Mann and Cheung (*u̯arH²) agree. Walde-Pokorny (Bd. I p. 294) puts Avestan var- \"believe\" under *u̯er- instead. That is the \"Wer 1\" alternative in Nourai's note, and modern work (Cheung, LIV) prefers *welh₁-.\n- **Node verdicts:** 5 confirmed (#4–#8), 2 plausible (#1, #3), 1 transcription_suspect (#2), 0 disputed.\n- **Plausible #1, Avestan:** \"upa-var\" and \"adi-var\" are not attested Avestan words. They are Horn's 1893 reconstructions for bāvar and ēvar. The gloss \"desired city\" for xšatra-vairya is loose: xšaθra means \"dominion\", not \"city\".\n- **Plausible #3, Persian:** geravîdan, bâvar and Šahrîvar are confirmed by Cheung, Horn no. 912 (p. 203), Mo'in and MacKenzie. ârî < Pahlavi ēvar is only Horn's guess, and Nyberg gives āvar as the New Persian form. This matches the verdict on page 154.\n- **Transcription_suspect #2, Pahlavi \"paver\" (error_in: book):** this is not a Pahlavi word. The word for \"belief\" is written w'pl and read wābar/wāwar (MacKenzie, Nyberg). Hübschmann notes \"phl. vāwar (geschrieben vapar)\", which explains the misprint. The printed page shows \"paver\", so the extraction is faithful. The page image is saved at data/verification/sources/refs/ocr/BOOK/539.png.\n- **Extraction errors for the owner to fix:** none. The JSON matches the printed page.\n- **Cited refs:** POK:1137, HRN:203, BQT:1316, BQT:1803 and SOD:412 (Gharib entry 10168, wrn \"faith, belief\" < Av. varəna) support the chart. BQT:1303 is a page of شنگ- headwords with nothing relevant (not_found). MON:2098 is only partial because the 6-volume page isn't on disk. DVS:198 is not accessible.\n- **Etymonline:** it returned 403 for every fetch, so those archive entries hold failure stubs and none of them is cited. I used Wiktionary and Skeat instead for the English nodes."
}
```


### [2026-10-17T00:06:15.127Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
