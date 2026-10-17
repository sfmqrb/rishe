# Verification process log — verify-page-547


## [2026-10-17T00:00:15.452Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 547 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-547.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-547.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-547.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 547` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.525Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.585Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.604Z] TOOL RESULT

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


## [2026-10-17T00:00:19.092Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-547.txt"
}
```


### [2026-10-17T00:00:19.125Z] TOOL RESULT

```
1	=== PDF page 547 (book page 517) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wer 5 : to burn  (refs POK:1166)
4	#1 (parent #0) [Russian] refs=POK:1166; AHD:1148 | varit : to boil, cook ; samo-variti, samo-war : self boiler used for boiling water ☞Sem 1
5	  #2 (parent #1) [Persian] refs=MON:1918 | samâvar «سماور» : "self boiler"
6	--- entry 1 ---
7	ROOT [Indo-European] Wer 6, Swer : to bind, hang on the scale, heavy  (refs POK:1150; IEC:1347; WLD1:264)
8	#1 (parent #0) [Avestan] refs=IEC:1347 | xwâiris : blame, weight
9	  #2 (parent #1) [Persian] refs=IEC:1348 | xwâr «خوار» : indigent, low in value | NOTE: See root "Ěter" for a different derivation
10	#3 (parent #0) [Latin] refs=AHD:1549 | sěrius : grave, serious
11	  #4 (parent #3) [English] refs=AHD | serious
12	#5 (parent #0) [Greek] refs=IEC:1347; AHD:1150 | aeirein : to raise ; arteria : artery | NOTE: AHD is not sure of this derivation
13	  #6 (parent #5) [English] refs=AHD | aorta, artery, meteor
14	  #7 (parent #5) [French] refs=None | aorte
15	    #8 (parent #7) [Persian] refs=VOP:1 | â`ort «آورت» : aorta
16	--- entry 2 ---
17	ROOT [Indo-European] Wer 6, Werd
18	Wordos, Worda, Wordia : raised point
19	wart, frog  (refs IEC:1577; POK:1151)
20	#1 (parent #0) [Persian] refs=IEC:1577; MON:467; FRS:201 | bâlŭ «بالو ، پالو» : wart
21	#2 (parent #0) [Germanic] refs=POK:1151 | war, wartôn : wart
22	  #3 (parent #2) [English] refs=AHD | wart, warble
23	#4 (parent #0) [Latin] refs=POK:1151; IEC:1577 | verrŭka : wart
24	  #5 (parent #4) [English] refs=AHD | verruca
25	--- entry 3 ---
26	ROOT Werb -> redirect to Wer 2
27	--- entry 4 ---
28	ROOT Werd -> redirect to Wer 6
29	--- entry 5 ---
30	ROOT Werdh -> redirect to Ered
31	
```


## [2026-10-17T00:00:19.643Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-547.json"
}
```


### [2026-10-17T00:00:19.699Z] TOOL RESULT

```
1	{
2	  "pdf_page": 547,
3	  "book_page": 517,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wer 5",
8	        "lang": "Indo-European",
9	        "refs": "POK:1166",
10	        "gloss": "to burn"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Russian",
17	          "refs": "POK:1166; AHD:1148",
18	          "words": [
19	            {"translit": "varit", "gloss": "to boil, cook", "script": null},
20	            {"translit": "samo-variti, samo-war", "gloss": "self boiler used for boiling water", "script": null, "see": ["Sem 1"]}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "MON:1918",
30	          "words": [
31	            {"translit": "samâvar", "gloss": "\"self boiler\"", "script": "سماور"}
32	          ],
33	          "note": null,
34	          "quote": null
35	        }
36	      ]
37	    },
38	    {
39	      "root": {
40	        "name": "Wer 6, Swer",
41	        "lang": "Indo-European",
42	        "refs": "POK:1150; IEC:1347; WLD1:264",
43	        "gloss": "to bind, hang on the scale, heavy"
44	      },
45	      "nodes": [
46	        {
47	          "id": 1,
48	          "parent": 0,
49	          "lang": "Avestan",
50	          "refs": "IEC:1347",
51	          "words": [
52	            {"translit": "xwâiris", "gloss": "blame, weight", "script": null}
53	          ],
54	          "note": null,
55	          "quote": null
56	        },
57	        {
58	          "id": 2,
59	          "parent": 1,
60	          "lang": "Persian",
61	          "refs": "IEC:1348",
62	          "words": [
63	            {"translit": "xwâr", "gloss": "indigent, low in value", "script": "خوار"}
64	          ],
65	          "note": "See root \"Ěter\" for a different derivation",
66	          "quote": null
67	        },
68	        {
69	          "id": 3,
70	          "parent": 0,
71	          "lang": "Latin",
72	          "refs": "AHD:1549",
73	          "words": [
74	            {"translit": "sěrius", "gloss": "grave, serious", "script": null}
75	          ],
76	          "note": null,
77	          "quote": null
78	        },
79	        {
80	          "id": 4,
81	          "parent": 3,
82	          "lang": "English",
83	          "refs": "AHD",
84	          "words": [
85	            {"translit": "serious", "gloss": null, "script": null}
86	          ],
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 5,
92	          "parent": 0,
93	          "lang": "Greek",
94	          "refs": "IEC:1347; AHD:1150",
95	          "words": [
96	            {"translit": "aeirein", "gloss": "to raise", "script": null},
97	            {"translit": "arteria", "gloss": "artery", "script": null}
98	          ],
99	          "note": "AHD is not sure of this derivation",
100	          "quote": null
101	        },
102	        {
103	          "id": 6,
104	          "parent": 5,
105	          "lang": "English",
106	          "refs": "AHD",
107	          "words": [
108	            {"translit": "aorta, artery, meteor", "gloss": null, "script": null}
109	          ],
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 7,
115	          "parent": 5,
116	          "lang": "French",
117	          "refs": null,
118	          "words": [
119	            {"translit": "aorte", "gloss": null, "script": null}
120	          ],
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 8,
126	          "parent": 7,
127	          "lang": "Persian",
128	          "refs": "VOP:1",
129	          "words": [
130	            {"translit": "â`ort", "gloss": "aorta", "script": "آورت"}
131	          ],
132	          "note": null,
133	          "quote": null
134	        }
135	      ]
136	    },
137	    {
138	      "root": {
139	        "name": "Wer 6, Werd\nWordos, Worda, Wordia",
140	        "lang": "Indo-European",
141	        "refs": "IEC:1577; POK:1151",
142	        "gloss": "raised point\nwart, frog"
143	      },
144	      "nodes": [
145	        {
146	          "id": 1,
147	          "parent": 0,
148	          "lang": "Persian",
149	          "refs": "IEC:1577; MON:467; FRS:201",
150	          "words": [
151	            {"translit": "bâlŭ", "gloss": "wart", "script": "بالو ، پالو"}
152	          ],
153	          "note": null,
154	          "quote": {
155	            "text": "ای عشق ز من دور که بر دل همه رنجی - همچو زیر چشم یکی محکم بالو",
156	            "poet": "Shâker Bokhârî"
157	          }
158	        },
159	        {
160	          "id": 2,
161	          "parent": 0,
162	          "lang": "Germanic",
163	          "refs": "POK:1151",
164	          "words": [
165	            {"translit": "war, wartôn", "gloss": "wart", "script": null}
166	          ],
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 3,
172	          "parent": 2,
173	          "lang": "English",
174	          "refs": "AHD",
175	          "words": [
176	            {"translit": "wart, warble", "gloss": null, "script": null}
177	          ],
178	          "note": null,
179	          "quote": null
180	        },
181	        {
182	          "id": 4,
183	          "parent": 0,
184	          "lang": "Latin",
185	          "refs": "POK:1151; IEC:1577",
186	          "words": [
187	            {"translit": "verrŭka", "gloss": "wart", "script": null}
188	          ],
189	          "note": null,
190	          "quote": null
191	        },
192	        {
193	          "id": 5,
194	          "parent": 4,
195	          "lang": "English",
196	          "refs": "AHD",
197	          "words": [
198	            {"translit": "verruca", "gloss": null, "script": null}
199	          ],
200	          "note": null,
201	          "quote": null
202	        }
203	      ]
204	    },
205	    {
206	      "root": {"name": "Werb", "redirect": "Wer 2"},
207	      "nodes": []
208	    },
209	    {
210	      "root": {"name": "Werd", "redirect": "Wer 6"},
211	      "nodes": []
212	    },
213	    {
214	      "root": {"name": "Werdh", "redirect": "Ered"},
215	      "nodes": []
216	    }
217	  ]
218	}
219	
```


## [2026-10-17T00:00:29.110Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -120; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','MON','IEC','WLD','VOP','FRS','BQT','HRN','HUB','ARY','KLN','SKT','BRT','SYN','CHEUNG','PHD','NYB','FSD','WEB']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:500])\n\""
}
```


### [2026-10-17T00:00:29.801Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google 
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed p
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a l
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; th
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
CHEUNG null
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/re
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g.
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, w
```


## [2026-10-17T00:00:40.992Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/ | tail -5; sed -n 1,200p tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','WLD','MON','FRS','AHD']:\n  v=d[k]; print(k, v.get('local_file'), '|', v.get('page_offset'), '|', str(v.get('lookup_hint'))[:400]); print()\n\""
}
```


### [2026-10-17T00:00:41.462Z] TOOL RESULT

```
page-97.json
page-98.json
page-99.json
process
sources
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
POK /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d

IEC /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.

WLD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab

FRS ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt'] | different edition — no mapping | Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.

AHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
```


## [2026-10-17T00:00:43.059Z] AGENT

Let me look up POK entries.


## [2026-10-17T00:00:44.615Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"lemma: (6\\. )?(s)?uer|lemma: 5\\. uer|lemma: 4\\. uer|lemma: ğ?uer\" POK_full.txt | head -30; grep -n -i \"Page(s): 1166\\|Page(s): 1150\\|Page(s): 1151\" POK_full.txt | head"
}
```


### [2026-10-17T00:00:44.972Z] TOOL RESULT

```
22997:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
74446:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
84141:Root / lemma: suergh- {*g"hergh- : ksuergh-) 
84162:Root / lemma: suer-1 (also ser-?) 
84188:Root / lemma: suer-2 
84233:Root / lemma: suer-3 
84255:Root / lemma: suer-4 
84282:Root / lemma: suer-5 
90799:Root / lemma: uerrS^-1 
90836:Root / lemma: uervS^-2 
91045:Root/ lemma: uep-2\ "to throw, throw out' derived from an extended Root/ lemma: uer-3. 
91141:Root /lemma: uerg-1, ureg-{*huerg-1) 
91166:Root / lemma: uerg-2, ureg- {*hueig-2) 
91239:Root /lemma: uer-10{*huer-10) 
91247:Root /lemma: uer-11, uer9-{*huer-11) 
91293:Root / lemma: uer-12{*huer-12) 
91314:Root / lemma: uer-13{*huer-13) 
91335:Root/ lemma: uer-1, also suer-{*huer-f) 
91411:Root / lemma: uer-2{*huer-2) 
91474:Root / lemma: uer-3{*huer-3) 
91484:Root/ lemma: uer-3. A. ufmi-s, ufmo-s{*huer-3) 
91513:Root / lemma: uer-3. B. uer-b-3in6 uer-k:i^-{*huer-3) 
91556:Root / lemma: uer-3. C. u(e)r-ed- {*huer-3) 
91578:Root / lemma: uer-3. D. uer-g- {*huer-3) 
91609:Root / lemma: uer-3. E. uer-gh-{*hues-3) 
91615:Root/ lemma: uer-3. E. uer-gh-{*hueiy''h^\ "to turn, press, strangle' derived from g- 
91637:Root/ lemma: uer-3. E. uer-gh- {* suerg^h^: 'to turn, press, strangle' < [common Latin 
91686:Root / lemma: uer-3. F. uer-k- {*hue-3) 
91713:Root / lemma: uer-3. G. uer-p-, ur-ep-{*huer-3) 
91760:Root / lemma: uer-3. H. uer-t- {* huer-3) 
91409:Page(s): 1150-1151 
91472:Page(s): 1151-1152
```


## [2026-10-17T00:00:53.835Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91335,91475p POK_full.txt; grep -n \"lemma: uer-[4-9]\\|lemma: uer-1[0-9]\\|Page(s): 116[5-7]\" POK_full.txt"
}
```


### [2026-10-17T00:00:54.173Z] TOOL RESULT

```
Root/ lemma: uer-1, also suer-{*huer-f) 

Meaning: to bind, to attach 

Material: A. Gr. asipu) from *aF£pjaj (with Vorschlags-a-), from Homer also aipw (anyhow 

from *a£pju) contracted, with ai instead of ai): a) 'reihe an, bandage, kopple', p) "lift high, 

raise, uplift'; 

to a) "kopple': 

^uvaipsTQi auvaiTTETai Hes., auvnopo(; Hom. (auvaopo(; Pind.) "narrowly vereint, 
coniunx', Attic auvwpiq "Zweigespann', TEipaopoc;, Attic T£Tpu)po(; "Viergespann', hom. 
napnopo(; "Beipferd besides dem Zweigespann'; 

to (3) "lift high, allow hangen': 

nspTO EKpepoTO Hes., hom. nspsGovTai "sie flattern'; hom. (jEinopoc;, Attic p£T£U)po(;, 
Aeolic n£5aopo(; "erhoben, high schwebend' (pisra " amid, in the middle of '); KaTr|opo(;, 
KOTCopiq; KaTOjpr|<; kqtu) psnajv Hes.; £rrnopo(;; aTTnopo(;; in addition with lengthened grade 
and Intensive reduplication aicbpa (*FaiFu)pa) "Schwebe, Schaukel', with aiajpsu). further 
in addition aoprrip "Schwertkoppel', aoprn "leather sack' (*aFopTa because of Latin 
loanword 5i/e/Ya"Packsack'), also probably aop n. "sword'; aopr- or rather aapr- 
contracted to apr- in aprripia " windpipe, Arterie', besides aoprn "Aorta'; aspr- contracted 



to apT- in aprav " attach with a hinge, hook ' (compare nspTnas nsprriMCii by Alexandrinern 
with apravn 'rope, loop, noose, snare ', apT£|ju)v 'Bramsegel'); 

alb. vjer^ hang on', 5Ka/7"together', vark, -^i/"row, Kranz, chain ', vargarfrow, Trupp'; 

Lithuanian veriu, i/e/Y/'einfadeIn'; Latvian veru, i/e/i^'einfadeln, prick, sew', in addition 
die iterative Lithuanian varstyti, Latvian i/a/'5//?"wiederholt einfadein', Latvian savare^ro6 
zum Binden', East Lithuanian virtine "bundle', Latvian virtene, virkne{*virtne)i. 
"Aneinandergereihtes, row', also Lithuanian pa-vare auA vorai. "long row' (from cart, 
animals etc.), Lithuanian virve, Latvian i//n/e"rope, band'. Old Church Slavic vrbvb6s. (= 
Old Prussian wirbeAs), Lithuanian api-varas " bootlace ', Ka/'a/7o'a "netting from withe ', 
voras' spider'; Old Church Slavic i/bi//'e//"hineinstecken', yO/'c»i//'e//"durchstecken', russ. 
veratb'st\ck, hineinlegen'. Old Church Slavic obora {*ob-vora) "rope', russ. verenfca^\ov\Q 
row, line'. Old Church Slavic verigyi. PI. "Ketten, Fessein', slov. verfga, veruga^ chain ', in 
addition also Gothic 1477^^5 "herd'. Old English wreed6s.\ russ. vorona, voronka ^Tnchter', 
\/ereta'sack, bag'. Old Church Slavic vret/sten. ds. etc.; 

Maybe alb. ver/ga' chain ring ', varg' chain '. 

B. With the meaning "row, swarm etc.': 

Old Indie vrndam'troop, multitude, crowd, bulk, mass'; Old Irish foirenni. " factio, group, 
troop, multitude, crowd', acymr. guer/'n lacWo' , ncymr. ^n/e/y/? "people, bulk, mass, troop, 
multitude, crowd', abret. ^^e/7/7 "factiones' {*vanna)\ Old English weorn, wearn^troop, 
multitude, crowd, bulk, mass, troop'; Tocharian B warna/'wltW; about russ. verenfca, 
Lithuanian vora, Latvian virkne, alb. vargansee above. 

C. With /b-formants: *ureto-\n Old Indie vrata- m. " multitude, crowd, troop, bulk, mass'. 
Old English wrsecf^\r\er6', Gothic wref^us {Hs. wnPus). 

D. with 5 mobile: suer-\u 

Lithuanian sver/u svert/'wagen', in addition svarasm. "Wage', svarus' heavy', and 
s\//ru, sv/'rt/"6as Ubergewicht have, iJberhangen'; svirtisi. "Brunnenschwengel', Latvian 
sveru, si/e/'/"wagen, wiegen', svars' weight', sverei. "Brunnenschwengel'; cymr. chwar-, 
bret. c'hoar-' befall '; 

Germanic swera-^ heavy ' in Gothic supers "geehrf. Old High German Middle High 
German swar{^\^ High German swarJ) " heavy, driJckend, schmerzend'; doubtful gr. sppa 
n. "Schiffsballasf (see 1152) and Latin 5e/7^s"ernst'. 



References: WP. I 263 ff., WH. II 521, Trautmann 296, 351 ff., Jokl Ungunder-kult. 
Untersuchungen 194, Vasmerl, 184 ff., 226 f., 229; 2, 243, Frisk 23 f., 49, 153 ff.; H. 
Lewis BBC S. 4, 136 f. about Celtic *suar-^ befall ' C*fall'). 
Page(s): 1150-1151 

Root / lemma: uer-2{*huer-2) 

Meaning: highland, high place, top, high 

Note: extended uer-d-, uer-s- 

Material: A. Latin i/ams'Gesichtsausschlag, Knospchen' (= Lithuanian viras, PI. viral 

compare East Lithuanian virys, PI. viriaTm. "Finne in pork '), Latin i/amA/s'Gerstenkorn in 

eye', varixm. f. "Krampfader'; 

perhaps Middle Irish ferbbi. "Hitzblatter, Finne' {*ueib^a), from which borrowed abret. 
P'i/e/^c'Brandmal', Middle Breton guerbrbubovi; 

nisi. varu. 'Augenschleim', Swedish varu. "pus'; compare Old High German warah. Old 
English wearh, worsm ds.; Old English wer-nseglm. "ulcer', nengl. warnelds.; Dutch weer 
"weal, callus', Norwegian dial, i/e/ie "swelling, lump, growth under the skin the KiJhe'; 

with A>suffix: Swedish dial, verna. Old High German iye/77a "Krampfader', Modern High 
German dial. H/e/77"Gerstenkorn in eye' {*wernd); 

with the meaning "lip' (*swollen elevation): Gothic wairilom Dat. PI., Old English weleras 
PI. (metathesis from *werelas). Old Frisian were, as from the s-extension Old Icelandic 
vgrri. Old Prussian warsus^\\'^\ 

uer-cf-: npers. ba/u' wart ' (Iran. *vard-)\ Old High German warza. Old English wearte. 
Old Icelandic vartat {*uorda) " wart '; ablaut. Old Church Slavic Kreo'b "damage', russ. 
i/e/'eo'" ulcer, abscess, boil '. 

£/er-5-; Latin verruca^ a steep place, height, a wart on the human body, an excrescence 
on precious stones ' (by Cato also "locus editus et asper'). Old English M/e'a/7-"weal, callus, 
wart', Flemish bya/re"weal, callus, knag'. Old High German n/e/ra "Krampfader', Modern 
High German I4fe/7'e"Gerstenkorn in eye'. 

B. Old Indie varsman-m. "height, headmost, topmost, highest, uppermost ', varsman-n. 
"height, headmost, topmost, highest, uppermost, cusp, peak' = gr. sppa n. "pad, reef, hill' 
(? after Frisk 561 ff. identical with sppa n. "Ballast' and from Indo Germanic *suer-mn 
"schweres weight '), Old Indie i/a/'s/yas- "higher', varsistha- "hochsf; Lithuanian virsus^das 



Obere, hochste cusp, peak', Latvian v/rsusvn. "das Obere', f. v/rsa; Slavic *vbrchb in Old 
Church Slavic vrtchb, russ. verch' headmost, topmost, highest, uppermost, acme, apex ' 
(Old Church Slavic vrbchu ' above' , of ^-stem); Old Irish /fe/r "better' {*uerso- " upper ') to 
Positive /fe/77'good' {*uer-no)\ cymr. etc. gweirbe\.\.ef either from *uel-no- " choice ' or 
after Thurneysen Gr. 236 /e/rand gwellirom * uer-/o- \N\t\r\ different development from -a/-; 
Middle Irish farri. " jamb ' = cymr. gwari. " nape ' {*ursa)\ manche connect Gothic 
wafrsiza. Old High German M///'s//'c»"bad' with Irish ferr, so that (as by Modern High German 
about S. 11 05) "in hoherem Grade' to "about dasrechte Maft hinausgehend'; doubtful gr. 
piov "Berghohe, foreland, promontory ' {*urisorR) and Old Icelandic risi. Old High German 
riso. Middle Low German rese^ giant ' {*wrisan-). Old Saxon wrisilAs., by/7s///<:7"riesenhaft' 
(die forms ohnen/through support in Germanic risan above S. 331); perhaps also thrak.- 
Phrygian ppia "fortress' {*uriia) and Tocharian AB /7"town, city' (whether not to uer- 
"umschlieften'); doubtful Phrygian opou "avco'; 

after Specht (KZ 66, 199 ff.) here also gr. oupav6(;, Lesbian u)pavo(; (more properly 
opp-), 6pavo(;, Boeotian Doric lak. u)pav6(; m. "sky, heaven' from *uorsanos, to *uorsos 
"high' (in Old Indie varsTyas- "higher', see above), further ablaut, gr. "Eppoq 6 Zsuc; (Hes). 

References: WP. I 266 f., WH. II 734, 762 f., Trautmann 360, 362, Vasmer 1, 190 f., 230. 
Page(s): 1151-1152 

Root / lemma: uer-3{*huer-3) 

91239:Root /lemma: uer-10{*huer-10) 
91247:Root /lemma: uer-11, uer9-{*huer-11) 
91291:Page(s): 1165-1166 
91293:Root / lemma: uer-12{*huer-12) 
91314:Root / lemma: uer-13{*huer-13) 
91970:Root / lemma: uer-4 {*huer-4) 
91991:Root / lemma: uer-5 {* huer-5) 
92098:Root / lemma: uer-6{^huer-6) 
92155:Root / lemma: uer-7{*huer-7) 
92218:Root / lemma: uer-8{*huer-8) 
92275:Root / lemma: uer-9. Ueru-s{*huer-9)
```


## [2026-10-17T00:00:57.668Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91239,91335p POK_full.txt"
}
```


### [2026-10-17T00:00:58.008Z] TOOL RESULT

```
Root /lemma: uer-10{*huer-10) 

Meaning: " river, flow ' 

See also: see above ayer-S. 80 f.; in addition Var-'m many FIN {Uer-). 

Page(s):1165 

Root /lemma: uer-11, uer9-{*huer-11) 

Meaning: friendship; trustworthy, true 

Material: A. root nouns uer- gr. Frip- in hom. (sni) npa cpspsiv "einen Gefallen tun', Pherek. 

npa igGi, Bacchyl. qpa with Gen. "xapiv'; £nir|pavo(; "wohlgefallig, pleasant'; Nom. PI. spi- 

npsc; " confidante ', Sg. ostem spiripoc; "traut, dear'; ppiripov fjEyaAwc; KSxapiajJEvov Hes.; 

PN Dspiriprif;, Aiu)pr|<;from Aio-Fripr|<;. 

B. derivative uera. Germanic Vera "pact, covenant, profession, declaration, covenant' 
in Old Icelandic GN l/a/'"goddess of oath of allegiance ', PI. i/a/'a/'"Treuegelubde', Old 
English wseri. "pact, covenant, loyalty, protection'. Old High German wara6s.. Middle Low 
German ware^'^aci, covenant, peace'; Old Church Slavic f. "faith, belief. 

C. compounds auf -uero-s, -ueri-s, formal as gr. £pir|po(;, ppir|po(;: Latin se'-i/ems"ohne 
Freundlichkeit', i.e. "stern', therefrom asseverare^ insure ', perseverare^ eu^ure"; 
GegenstiJck gall. PN Co-vTrus, cymr. cyty/A" right, loyal, faithful'; *uerf-s\n Gothic alla-werei 
"schlichte GiJte', Old Icelandic p/i/^/r "friendly, gastlich'. Old English ea/-M/e/'//ic"benigne', 
Old High German alauuari. Middle High German a/n/^/'e "simple, oafish, clownish ' Old 



High German zur-wan" dub'\ous ' = Gothic *tuzwers{tuzwerjan' doubt'), * unwers(un-werjan 
" unwilling sein'), Old High German /77///-M/5/7"gentle'. 

D. adjective t/ero-5 "true': Latin verus. Old Irish ffr, cymr. gwir. Old Saxon Old High 
German war. Modern High German wahr. 

E. verb derivations: gr. Eoprn (*F£FopTC() " celebration, festival', Aeolic spoTK; ds. 
(*F£poTi(;? rather assimilate an i^oioc,, hom. i^aioc, " mellifluous'); i^cxvoc, ds.; 

Old High German weren, giweren, giweron. Modern High German gewahren. Old Saxon 
waron^\e\s\.ev\\ 

Here probably also Germanic werduz{= Indo Germanic *uertu-) in Old Icelandic vert^r 
(Dat. Sg. K//'it'e besides frequent vert^e) 'repast, meal', Gothic wa/rdus ' ^ivoq' , Old Saxon 
werd. Old High German l/V/rt' householder, Eheherr, host ', Old Frisian hus-werda' 
landlord, householder'. 

References: WP. I 285 f., WH. II 528, 768, Wissmann Nom. postverb. 115 ff.. The altesten 
Postverb. of Germanic 45, Frisk 531 , 547 f., 565, Trautmann 351 , Vasmer 1 , 1 84. 
Page(s): 1165-1166 

Root / lemma: uer-12{*huer-12) 
Meaning: to burn 

Material: Armenian varem " set on fire, ignite ', varim 'burn'; perhaps alb. vorbe^ 
saucepan, cooking pot ' and (?) Germanic *uarma- 'warm' in Gothic warmjan' warm'. Old 
Icelandic varmr, afr. Old Saxon Old High German warm 'warm', changing through ablaut 
Old High German w/'rma' warmth ' {*wirmia) and wirmina. Middle High German wirme ar\d 
wirmen, compare (?) Old Icelandic orna' warm become, warm'; Old Church Slavic varh 
'heat', var/f/'cook' (different above S. 81); in addition also Balto-Slavic uarna-m. 'raven' in 
Lithuanian varnas. Old Prussian Vok. warm's, Akk. PI. warnins. Old Church Slavic vranh, 
russ. voron, probably a nominalized adjective * uarna- 'black, verbrannt' in Old Church 
Slavic vrant, russ. voron6j'b\acW etc.; with lengthened grade (Vriddhi) femin. Balto Slavic 
* uarna- 'crow' in Old Prussian M/5/77e (secondary e-stem), Lithuanian varna, russ. Church 
Slavic vrana, serb. vrana, russ. i/c»/'d/75 (glottal stop through Vriddhi); Hittite uar- 'burn', 
participle uarant- ' burning ' (Intrans.), uar-nu-'V\r\d\e, inflame, burn '. 
References: WP. I 269, Trautmann 343, 361, Vasmer 1, 169, 228 f., Szemerenyi Kratylos 
2, 121 f., the also Germanic *swarta-'b\acW (different above S. 1052) dazustellt. 
Page(s): 1 1 66 



Root / lemma: uer-13{*huer-13) 

Meaning: squirrel, etc.. 

Note: in certainly Zugehorigen with Redupl. uer-uer-, ue-uer-, uai-uer-, ui-uer-, ua-uer- 

Material: Npers. varvarah^ squirrel '; Latin vTverra\. Trettchen' {*vT-ver-sa)\ cymr. gwiwer, 

bret. gwiberirom Latin; unclear nir. iora ruadh, Scots Gaelic feorag, 

Balto-Slavic *ueyer-dx\^ *uauer- *uaiuer-\. 'Eichhornchen' in Lithuanian vaiveris 
{va/varas, vaivarys) "male of polecat or marten', vaivere, vovere^ squirrel '; Latvian vavere, 
vaveris6s.\ Old Prussian wewareAs.; Old Russian veverica, nslov. i/ei/e/yica'Eichhorn', 
kir. vyvirka, Czech veverka, Bulgarian ververica 6s.\ 

not reduplicated in 2. part from Old English ac-weorna. Old Swedish ekorne. Old High 
German eihhumo, eihhorneic. 'Eichhorn' (see below *5/^-"sich violent bewegen'). 

References: WP. I 287 f., WH. Ill 808, Trautmann 356, Vasmer 1, 176. 
Page(s): 1 1 66 

Root/ lemma: uer-1, also suer-{*huer-f)
```


## [2026-10-17T00:01:15.315Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"x[vw]a[ar]i\\|hvar\\|xwar\\|xvar\" IEC.txt | head -30; grep -n -i \"bal[uū]\\b\\|wordos\\|uordo\\|wordh\" IEC.txt | head"
}
```


### [2026-10-17T00:01:15.715Z] TOOL RESULT

```
331:type; (2) durative-freq. of verb type; (3) de- nominative extn. of verb type (1) Gk. outáo, geláo, eráo, damáo, skirtáo; Lat. crepo, seco, tono, veto, domo, sono, frico, all with inf. in -are, pf. in -u1; OS fol- gon; OHG tholon, holon and halon, volgon beside -en in all forms; OCS prijajo (beside prijo, inf. prijati: Skt. prinami: Go. frijon, see below: priià-, vrüzajo, vrükajo, tüpajo; Li. plasnóju, inf.-óti, riaumóju, pléscioju; Latv. bokaju, at. bojaju; (2) sedare, ducare, placare; Go. miton (mitan), hvarbon (hvairban); OCS tékajo, -ati (eko, testi); OCz. vídaju, -ati (vizu, viděti); Li. pa-jaújoju, -oti(jauti) Latv. plūkāju, -āt (plükt); (3) Gk. timáo (timé), ereunáo; Lat. fumare; OHG zilon (:Go. tilon) (zil), faston (fasta), fülön (fül); OCS dymajo, -ati (Lat. fümare)(dymü), düzdajo (düZzdi), kosajo (kosü); Li. ráudoju, -oti (ráuda), vo- Dom (vðlas). See below: *siiā- (sia), skiia-, neuà-, dhuma-, etc.
3371:dhuél- ‘languish, expire, gasp’. See dhuol-, dhul-, dhul- OHG twélan; MHG er-, vertwëln ‘expire’; (z-gde in Li. dvylu, dvilti ‘wane, pine’; OE dwolma ‘chaos’; Norw. cf. dolmen ‘faint’ be- side ON dylminn ‘indolent. (Long-grade iso- phone in Li. dvēlē 'spirit). Av. dvar- ‘rush, as demons’ is ambig. Cf. Skt. a-dhvaráh re, ligious ceremony’. Cf. also OHG twala, OS dwala “hesitate?
3418:Av. dvar(eimi), v. ‘rush’; Gk. thoüros “rush- ing’; Ir. duar ‘crowd’; cf. also Skt. a-dhvaráh (a religious ceremony); Sw. däre "Tool dhuoros “entrance, court. WP I, 871. Cf. dhuer-, dhur- Lat. (ambig.) forus *hatchway'; forum *mar- ket; OCS dvorü (and com. Sl.) ‘court, yard’; Li. dváras (farm. Perh. SI. LW) dhuos- *drooping, ailing; spirit, exhalation, expiry’. Cf. dhues-, dhus- Skt. cf. (ambig.) dhvasrah *withered"; MIr. dássaim *madden'; EME cf. dwas-light *will- o"-the-wisp'; Sw. dåse (“sluggard”, cf. E dial. dozy, fr. Scand.); dásig ‘sleepy’; Li. dvásas, dvasià ‘spirit’; dvasus ‘ailing, pining (dhuriə, a zero-formula to dhuer-, dhuor-, dhur- ‘door’. etc.) WP I, 870 Gk. thairós singularized: ‘hinge of door
5172:guer- (guor-) “food, drink, gulp, swallow, gullet, glutton’. WP I, 683 Skt. o-gde garáh, adj. ‘swallowing’, m. “drink, poison’; giràmi, z-gde v. ‘swallow’, fr. *gur-; Aw. gar-, xwar-, o-gde eat devour’; Arm. ker, o-st. “food, bait’; ker, cpds. —-eating', beside z-gde kur *food'; aor. suppletive to utem in keri, 3s. eker ‘ate’; Gk. dére, deré, deiré “neck, throat, bora ‘food’; cf. hellé-boros *helle- bore’, a poison-plant; Arc. derwà ('gully, glen’, with labiovelar -w echoed in suffix); borós (Cgluttonous': Lat. -vorus); Alb. cf. gab- zerr, gop-zerr *gullet; Lat. cf. ver-, -ver in ver- bena, -bascum, -àtrum (various herbs), and in cada-ver, cf. also ver-àgo ʻa disease in cattle’; -Vorus, cpds., voro, åre ‘devour’; cf. also ves- cor (“feed myself”, fr. *guersKo-); cf. also papā- ver ‘poppy’; Ir. cf. in-bhear, gs -bhir, m. ‘feed- ing, grazing’; MHG cf. quér-der ‘bait’; OE a- cweorran ‘guzzle’ (fr. *guers-); Pol. zer "Tod, der’; Cz. o-Zery, pl. *food-scraps'; R pro-Zora, Ukr. ob-Zora (e-gde: *glutton"); OCS Zro, Zréti
5177:guersos (guors-, gurs-) ‘sweet, soft, pleasant (lit. *enticeable with food?) Av. xwarezus ‘sweet, tasty; Go. qaírrus *tame'; MHG kürre, z-gde, id.; G cf. kirre, id.; (alleged) ON kvirr, id.
5395:gur- (1) ‘devouring; gulp; throat. WP I, 683 Skt. cf. gilami, gire, grnàmi ‘devour’; Av. gar-, xwar-, id. beside garð ‘throat’: Skt. galah, id. and -garáh *-vorous'; Tokh. B kor ‘throat’; Oss. gwr, id. and ‘abyss’; Arm. kur 'eatables' beside
5428:guró (1) 'gulp down, devour’. Cf. guer-, guor- Ved., Skt. gire, gilami, gírami, grnami, id.; Av. gar-, xwar-; Lat. voro, åre; OCS (i-basis) Zr, Zréti; Li. cf. girà “small beer" girtas, adj. ‘drunk; tipsy’; girtüs ‘heady — of wine’; Latv. dzira “drink”
9229:(Kuarmos, à “cover, protection, enclosure'. Variant of type quarm-, q.v.) Hes. sarmós (4) *enclosure, yard'. (For Gallo- Lat. parma ‘shield’: ON hvarmr ‘eyelid’, with a reference to OCS xramü ‘house’ & R xoró- my, fpl ‘mansion’, see quarmos)
13883:quarmos, à “lid, cover, protection, sanctua- ry’. Cf. Kuarm-. WP I, 506 Gallo-Lat. parma, f. “small shield”; cf. W parf- aes, pl. -eisiau, f., id. (fr. *parma + aegis); ON hvarmr, m. ‘eyelid’; OCS cf. (?) xramü, m. “house, sanctuary’; R xorómy, fpl. (*mansion' and com. Sl.); Cz. chrám “cathedral, temple" (SI. forms indicate *squarm-)
14189:quór- (quor-, qur-) adverbial extn. of the pronominal type quo-, q.v. WP I, 521 Skt. cf. kár-hi (^when', fr. *quor-ghi); ON hvar- gi ‘everywhere’; cf. also Skt. karanam, n. (*cause, reason! in sense of Lat. qua-re); Arm. ur, adv. (z-gde) ‘where’; Alb. kur ‘when’; Li. kuf, Latv. kur *where'; cf. also Alb. kurr (never', fr. *qur-ne > *qur-n: OE hwar-ne ‘not at all); Lat. quor, qur, quur & cür ‘why’; Ir cár “where? beside MIr. cair (Chow, fr. *quori, *quori); Cor. cf. par ‘as, so’; Go. hwar, interr. ‘whence’; ON hvar “where; anywhere’, MHG war ‘whither’: hwær ‘where, whither; somewhere, everywhere, wherever’; Du. waar ‘where’; OS hwar ‘where, whither'; OFris.
14203:quorpos, à “turn, link, join'. Cf. querp-, qurp-. (Skt. Av. & Li. Latv. ambig.) Skt. kalpah ‘manner’; Av. cf. kahrpuno Cl zard', LW in Arm. Karb, Let 'basilisk"); Go. hwarbon, denom. or freq. “walk? beside (e- gde) hwaírban, id., ga-hwaírbs (obedient, lit. *flexible)); OS hwarbon, as Go.; MHG warp, gs: Warbes, sm. ‘turn’; warbe, wf. ‘circle; as- sembly'; OE hwearf, m. “turn, crowd, move- ment, distance, change, error, embankment’; E wharf; EMSwedish hvarf, Sw. varv, n. ‘time, order, series, camp, layer; ON cf. hvarfla, v. ‘roam; waver’; Li. cf. pa-karpa, f. *nape: of neck’: Latv. karpis and karpe, mf. (/boathook'. Ambig.)
14374:qusõros ‘rough, gritty; gravel, scab, mange’. (Indo-Iran. ambig. cf. ksēr-) Skt. khárah “rough; Per. xāriš, xware "ich, mange’; xaram, v. ‘itch, scratch’; Oss. cf. (z- gde) xür, Dig. xurä ‘gravel, rubble’; Gk. pso- rós, adj. “rough, uneven; scabby’; psóra, f. ‘scab, itch’; Cz. charý ‘shabby, dingy’; Big. cf. xáro ‘rascal; ill-luck’; Li. šuoras, m. ‘scratch, line, groove, stripe; outburst, rage’; Ukr. cf. xaryty, inf. ‘clean’
15035:saul-, sáuel- ‘sun’. WP II, 446. (Indo-Iran. variant: sül-) Skt. cf. (z-gde) sürab, m. id.; Av. cf. hüro, gs. of hvaro, id.; Oss. cf. xur, Dig. xor, id.; Kurd. awer id. (and 'east); Scyth. (king's name) Saulius; Gk. helios, heélios, aélios (sic), id.; Lat. sol, cons. decl. m. id.; MIr. sól, id.; Gaul. sul- (in a name); W haul, pl. heu- liau, m., Br. héol, m. id.; Vannic dial. hiaol, m. id.; Cor. howl, m. id.; Go. sauil, n., OE Sol, n., Sw. sol, m. id.; ON sól, f. ‘sun, day”; Li. saulē, Latv. saule, f. id. (OCS slüníce n. ‘sun’ appears to be a cpd., cf. the Skt. variant sül- (*sul-) and (root of) Lat. nitere, nitidus?). Verbal types: Gk. héliázo, hélióo; Lat. solo, are, in-^; Icel. sóla, v. (a-stem); Sw. sola, v.; W heulo, inf.; Latv. saulot, inf.
17945:sueló (1) “burn, smoulder, blaze’. WP IL, 531 Skt. svárami, v. (2) ‘shine’; svar, n. ‘sunlight’; Av. Xxwar-, v. ‘shine’; hvaro, n. ((sun': Skt. svar, svaruh 'sunshine?)); Per. (ambig.) xuval, s. (lampblack', but cf. suord-); Gk. belle & héle, f. “heat of sun: also hélé, f. id. cf. eláne, f. lamp, torch'; dial. weléna, f. beside heléne, f. ‘goddess of light’; Lat. cf. sul-phur, z-gde (sulphur, w. semantics of OE cwic-fyr *'sulphur); OE swelan, intr. ‘burn, be burned? beside swaelan, tr. ‘burn’; G schwelen, v. 'smoulder'; ON svaela, wv. ‘choke’; f. ‘dense smoke’; Li. cf. svelmē, f. ‘smoke’; Latv. svelme, f. ‘glow’; (z-gde in) Li. svýlu, svilti, v. 'smoulder'; Latv. svilstu, svilt, v. ‘glow’; Fris. svilja, v. (dry, fr. *suelið); a possible cpd. in deíle, f. “twilight. The initial (su-) is explicit in Hes. (Lacon.) wélan, acc. ‘glow’
17949:suelo (3) ‘surge, swell. (Common Gmc. swëll- from *sueln-: FK. DEW: schwellen) Per. cf. ab-xvar, -xvard, s. ‘source, spring’; Gk. cf. hális, adv. Cen masse, surging’, fr. *suluit or sim.); Lat. cf. in-solesco, Gre, v. (1) ‘swell beside solidus, adj. (“firm?, prob. fr. *suelid-, not as WH to sollus); MHG swéllen, sv. 3 ‘swell; faint with hunger
17990:sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
17992:suer- (3) “harm, hurt, corrupt. See next Skt. svaràmi, v. (1) ‘blame’; Av. xwar-, v. “blame, injure’; xwairis, s. “abuse, blame"; Per. xware, s. ‘corruption, gangrene’; cf. xire, adj. ‘malignant’; MHG swérn, sv. “hurt; suppurate’
17993:suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumour’, fr. *suorel-); OHG swéro, wm., MHG swér(e), s. & wm. ‘ulcer’;
18161:suordos, is ‘black, dark; blackness, dark- ness’. Cf. WP II, 528 & 535 Per. xuval, s. (‘lampblack’. Phonol. of sal: Av. saroódo ‘year’); Oss. cf. xalon, pl: xälädtä, s. ‘raven’; xalas, adj. ‘grey’; Lat. surdus, adj. ‘deaf; dark; silent’; ab-surdus, adj. (grating, noisy; absurd, For sordes, -dis, see surd- queried); Go. swarts ‘black’; MHG swarz, id.; OE, ON sweart, svartr, id. (OE also = “dark, evil")
```


## [2026-10-17T00:01:24.156Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 17986,17991p IEC.txt | cut -c1-1500; grep -n -i \"uord\\|wart\\|verruca\" IEC.txt | head -20"
}
```


### [2026-10-17T00:01:24.486Z] TOOL RESULT

```
35
40
45
1348
sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
suer- (2) (suor-) “call, declare, state, speak, utter’. WP II 527 Skt. svaràmi, v. ‘sound; sing’; Gk. érō, éromai, v. ‘ask’; eíro, v. (2) “say, speak, tell’; cf. eirén, gs: -énos, m. “youth of speaking-age in Spar- tan parliament; MHG swéren, sv. 6. ‘swear’; OE swerian, sv. 6. id.; (o-gde in) Cz. ne- svor-ny, adj. ‘quarrelsome’; (long o-gde. in) OCS, Cz. svarü, svár, m. *quarrel' beside OCS svara, f., svarjo, -iti se, id.; ON sverja, v. ‘swear’ (p. t. sór & svór beside svaróa, pp: svarinn) (*-e-; *-0-; *-o-), (long o-gde in) MHG swuor, sm. (oath, curse: OCS svarü). Am- biguously *-e-/ *-o- in Skt. svárah, m. ‘sound, voice’. Ambiguous initial in Gk. éris, f. ‘strife’, and ambig. vocalism in Sw. sorl, n. ‘din’; sorla, v. (*syerol-?)
681:ardus, uos (1) ‘high’. WP I, 83. Cf. ordhus, uordhos, ardis Av arədus; Lat. arduus (1); MIr.Ir. ard, árd; Gaul. ardu- (in a placename Ardu-enna 'Ar- dennes’)
814:auk- (2) (?) full-grown, tall’ Lat. cf. -ūca in plant-names festūca, lactūca; verrūca ‘wart’ also qua ‘growth’; Br. cf. éog ‘tipe’; Go auhuma ‘highest’; Li. auklēti
1174:bhaus- “violent, dashing, boisterous; bang, beat, din’ Arm. cf. (variant) z-bawsank ‘amusement’, z-bawsnum (‘amuse os, fr. *bhauK-); Fris. boas "lively, eager; (of weather) bad: OHG bosi ‘paltry, bad'; bosa ‘badness’; Du. boos “angry, malignant, evil’; Nynorsk (archaic Nor- wegian) baus ‘stalwart’; Cz. cf. vý-buch, Ukr. vy-bux ‘explosion’. Verbal types include: Arm. (variant) z-bawsnum ‘amuse oneself; MHG besen ‘do evil; Cz. bušiti ‘hammer’; Big. bùša ‘punch’ beside bùxam ‘flog’. Cf. also ON beysta ‘thresh’; Big. buxtjà ‘dash, roar’
1198:bhegh- (variant of bhe&h-, see bhe&h-iKs) Skt. bahyah, adj. ‘outside’; Per. bàz "open: Tokh. A cf. pakür, B pākri *'openly'; ON (CO) bagr ‘chary, awkward"; bagi *opponent , bægi- (*athwart', in cpds.). See next
1201:sv. 7 “strive; shriek; boast; quarrel’; cf. OHG baga ‘battle’; MHG bàc, bàges ‘shriek, din, quarrel, boasting' & Ger. Bager 'restlessness, haste’; bágern ‘badger, nag’; ON bægja ‘oust, thwart, quarrel, force” |
1487:bholgo(n), os, om, à “tiebeam, crosspiece, baulk’. WP II, 181 OHG balco, balcho; OE balc, balca; ON bálkr; OCS blazna ‘thwart’; Pol. blozno ‘crossbar on sleď’; R bólozno ‘plank’; Li. balZienas, mf. 'tiebeam, axletree'; Finn. LW palkka, palkki “bean”
1812:bhrios (2) ‘son, young man. (Semantically related to (1)) Kurd. cf. bire “a stalwart’; Per. barnà, burnā ‘young man’; OE bora ‘son’ and byre, id.; Alb. bir, pl. bij, id.; Go. baür, cons. st. id., cpds. -born; ON burr, pl. rir, id.
2103:dederuos, dedrus ‘tetter, eczema, ringworm’. WP I, 800. Cf. der- Skt. dadrüh: Dacian (?) in LLat. *dzeruae (spelt zernae); GalloLat. cf. derb-itae (> Fr. dartres); Mir Ir. deir; Br. cf. derv-oed; OHG zetar-och; G Zitter-och ‘warts’, OE teter *tetters'; Icel. cf. tetur (^wretch', fig. usage); Li. cf. dederv-ine
3105:dhrobh- (2) ‘strike, smash, fragment. Cf. dhrebh- Go. cf. ga-draban “hew out’; ON drofn, pl. drafnir ‘breaker, wave’; cf. also ON -drefjar, cpds. 'spatterings'; Icel. drafa ‘talk thickly’; Norw. cf. drabelig ‘stalwart; OCS drobljo, drobiti ‘shatter; R drobi *lead-shot'; Cz. droby ‘rakings, scrapings’
4101:glist-, glisteros ‘adhesive’. WP I, 620 Mod. Gk. glisterós 'slippery, smooth'; cf. also Gk. glískhros 'gluey; MHG klister ‘glue’; OCS glista ‘tapeworm’; Srb. glista ‘worm’. Isophonic forms are S. Alb. glisht, Alb. gisht ‘finger’ and LGer. kliste ‘thwart on raft?
4296:greiĝ- ‘athwart’. Cf. groig- (2) ON kríkar ‘groin’; Latv. greizs ‘awry’
4556:ghaiios (ghaios) (?) *vigorous, lively, solid, firm. (The evidence is ambig.,, cf. WP I, 528 & 670). Cf. guoiio Gk. khaios ‘staunch, genuine’ (but a-gaios is *elegant); Br. gaé, adj. (gay. LW in Fr. gai); OCz. hojiti sé, v. *multiply', cf. Cz. hojný 'abundant'; Li. gajüs ‘sprightly’. (LG gau ‘dashing, gay’ is from a type *ghau-, cf. Norw. göy ‘fun’. Li. gaivüs ‘lively’ repre- sents *guoiu- apparently, but is entirely ambig. Gaulish gaeso- fstalwart may equate w. Br. gaé ‘gay’) |
4958:ghromb- “rough, harsh'. Cf. grombos (1) MLG cf. grempel “a sour drink’; ON grepp-, cpds. ‘grim, dour’; greppr ‘burly fellow, stal- wart; OCS grobü ‘raw, rough'. (Note: Pol. gruby, Cz. hrubý ‘coarse’, represent a type *ghroubh-; MHG grop, gs grobes, id. a type *ghrubh-); LW in Hung. goromba ‘coarse’; cf. Li. gramblüs, id.
7063:kersno- (1) «transversal; thwart; crosspiece, middle'. See next & kersos Hes. kérnai, kérna *spondyls, vertebral spurs’; Alb. qerr (coronet', vet.); Cz. cf. Cercha *cross- line’; Ir. cearn “angle, corner’; OCS cf. érěslo ‘groin’; R éresla, OCz. třiesla ‘loins’. (The con- sonantism of Skt. karásnah ‘forearm’, if re- lated, points to *koros-)
7068:and Gk. (z-gde) eg-kársios ‘oblique’; Lat. cf. cerr-itus ‘mad’; va-cerrosus ‘queer, mad’; va- cerra ‘village cross, post, tether’; Gaul. -cersos (in a name); Olr. MIr. cerr ‘maimed, awkward, left-handed, awry’; Ir. cearr ‘crooked, wrong’ beside corr, id. (fr. *krs-); ON hjarri (“hinge”, in view of Lat. cardo, if fr. *krsdo-); OE heorr, as ON; Sw. cf. hárs och tvärs “hither and thi- ther, criss-cross’; OCS éórésü, prp. “across? beside Slovene kfšiti, v. ‘transgress’; Cz. cf. Cercha, for *ércha *crossline^; Blg. cf. krexnu- vam, v. ‘place athwart’; Li. kersas ‘athwart, oblique'; Finn. LW karsas, id. (For ON hjarsi, hjassi ‘crown of the head? see kersno- 2). Umbrian va-sirslom is a landmark, “town cross? or sim. but of ambiguous phonol. cf. kirkolos and uadho
7687:thwart, cripple; be
7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
7828:kreio (kreiio, kroio) (1) “bring to life; luxuri- ate, multiply, abound’ Gk. cf. a-krá-antos ‘unfulfilled; fruitless’; Lat. Creo, creare ‘create’; re-creo ‘enliven’; cf. in- cré-mentum ‘increase’; Br. krui, v. (‘create’. Mng. infl. by Lat.); W creio 'freshen, enliven'; crai, adj. ‘fresh, lively; OCS cf. o-krijo & 0-krájo, -ati *convalesce, recover’; Cz. o-kfeju, O-kfát, id.; Latv. cf. krietns ‘stalwart; Lat. cré-ber, f: cré-bra (luxuriant, numerous, thick, frequent, fr. *kre- + *-bher-)
8017:kruĝ-? ‘cross, thwart; small of back’
8090:krksos, ios ‘oblique, awry’. WP II, 590. Var- iant krsos, see krs- (1) Gk. (ambig.) kársios ('oblique”. See krs-); Cz. & Slovak krch, krchy, adj. lefthanded, awk- ward’; Slovene cf. kíSiti ‘transgress; Blg. krás, m. “stile, crossing'; krăxvam, v “lay ath- wart; kráskam ‘go zigzag; krása, kărša (2) ‘wind, zigzag’; cf. krăšnjak ‘backbone’; Li. (?) kiršas ‘peevish, cross’; OPr. kirša “across; Li. cf. kìrkšnys, mpl. ‘lumbar region’; Latv. cirksnis, id. (but cf. krkin-) (the semantics are echoed in Alb. kryqza ‘lumbar region’ in relation to kryq, Lat. LW ‘cross’). An isophone arises in Skt. krsah ‘lean, poor?
```


## [2026-10-17T00:01:32.680Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Per. b[aā]l[uū]\\|bālū\\|balu,\\|Per. pal\" IEC.txt | head; grep -n \"^uord\\|^uer-.*wart\\|uerd-\\|uors-\\|uersos\" IEC.txt | head; grep -n -i \"x[ʷᵛv]a.r[ie]\\|hvāiri\\|xvāiri\\|xᵛairi\" BRT.txt | head"
}
```


### [2026-10-17T00:01:33.189Z] TOOL RESULT

```
13068:plëkis, à ‘offal, tripe, gut, intestine’. See next. Skt. plåsih, m. sg. & pl. (a part ofthe intestine); Li. plēšis, gs: -io, m. ‘rip, téar, tug’; plēšà, f. ‘strip’, in pl: pléšos 'strippings, fibre’ beside (variant) pl&kai, mpl. (2) ‘tripe’; Latv. plesis, m. 'tearaway, rip’. (For the semantics cf. senses of E pluck ‘guts’ & ‘snatch’. Isophonic: Per. palas ‘sackcloth’, OCS plësi, f. ‘baldness’ and plésni, f. ‘moth’; R. Cz. plésni, pléseni, plíseň, f. *mildew^)
13631:prd- (1), Indo-Iran. variant of type prs-, q. v. in Skt. pídakuh, m. (fviper; tiger or panther’, lit. spotted"); Per. palang, s. ‘tiger or leopard"; Oss. fálank, fárank (queried: ‘tiger or lion"); Gk. (fr. Iran.) párdos, m. ‘panther, leopard’
13686:prs- ‘speck, spot, mark, dapple, sprinkle, spray, dot, rash’. Cf. prsk-, (prks), prK-, prKs- Skt. cf. prsat, s. ‘droplet’; prsatah, adj. ‘motley, dappled’; prsvah, adj. *frosted'; Av. cf. paro&-, v. (e- or o-gde) ‘drip’; Per. cf. paSam, inf. pasi- dan, v. (e- or o-gde: Skt. parsami, v. 'sprinkle"); Tokh. A & B párs-, pras-, v. as Skt.; pársant, adj. ‘scintillating, brilliant; Hitt. parsa(mi), v. “flee? beside pap-pars(mi), v. 'sprinkle'; par- sanas, s. (-leopard', lit. *dappled"); Gk. cf. par- dakós, adj. (wet, if for *prs- + *-dnk-); Lat. cf. porr-1igo ('dandruff,, fr. *prs-); ON fors, m. ‘waterfall’; Sw. forsa, v. ‘gush’. Extns. in Skt. prdakuh, ‘panther; snake’; cf. Per. palang ‘leopard; tiger’; Oss. (queried) fálang, fárang ‘tiger’; Gk. párdos, m. ‘leopard, panther’; pár- dion, n. ‘giraffe’; párdalos, m. (‘plover or 'star- ling’); párdalis (an unnamed fish); cf. also Alb. pérpurth, v. (‘defile w. excrement’, fr. *-prsd- or fr. *-prKst-); Cz. cf. prznit, inf. (defile, fr. *prsd-)
5177:guersos (guors-, gurs-) ‘sweet, soft, pleasant (lit. *enticeable with food?) Av. xwarezus ‘sweet, tasty; Go. qaírrus *tame'; MHG kürre, z-gde, id.; G cf. kirre, id.; (alleged) ON kvirr, id.
7065:kerso, ið ‘cut’. Cf. kero, ið and quer-, quors-. W?P I, 429 Hitt. karsami ‘cut off, castrate’; MIr. cerrim, cirrim ‘cut, tear, hack, maim’; Alb. cf. (-é- in) korr, v. ‘reap, harvest’; korrë, f. id. The Slav forms are ambig. cf. R Cereslo ‘cutter, chisel’; Slovak crieslo *plowshare', perb. to quers-, quors- in view of Skt. kársåmi ‘drag, plow’ and krsami ‘plow’, karsah ‘plowing’. Li. kerslas ‘cutter, chisel' indicates the consonantal se- quence, as Ukr. éereslo ‘coulter’
```


## [2026-10-17T00:01:37.834Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"‘wart\\|'wart\\|“wart\" IEC.txt | cut -c1-700 | head; grep -n -i \"x.airi\\|x.arena\\|hvar\" BRT.txt | head -20"
}
```


### [2026-10-17T00:01:38.158Z] TOOL RESULT

```
814:auk- (2) (?) full-grown, tall’ Lat. cf. -ūca in plant-names festūca, lactūca; verrūca ‘wart’ also qua ‘growth’; Br. cf. éog ‘tipe’; Go auhuma ‘highest’; Li. auklēti
2103:dederuos, dedrus ‘tetter, eczema, ringworm’. WP I, 800. Cf. der- Skt. dadrüh: Dacian (?) in LLat. *dzeruae (spelt zernae); GalloLat. cf. derb-itae (> Fr. dartres); Mir Ir. deir; Br. cf. derv-oed; OHG zetar-och; G Zitter-och ‘warts’, OE teter *tetters'; Icel. cf. tetur (^wretch', fig. usage); Li. cf. dederv-ine
7702:korpos, å ‘cut, cutter; cutting, sharp; spike, point, crag’. Cf. kerp-, krp- Skt. (ambig.) cf. karparah (‘pot, sherd’. Cf. kerep-); Alb. karpë ‘rock, cliff; LW in Big. kàrpa, id.; Ligurian substr. in Rumansh crap, m. (‘boulder’, w. metath, as in cravun *carbonem', crapenda 'carpenta"); LW (?) in Alb. krep (‘crag’, as doublet of karpë?). Cf. WP II, 581. Here also prob. Ir. corr ‘peak, tip, corner, snout, bill, corn on foot"; W cor, pl. od m. (1) ‘point’; ON herfi ‘harrow’; Sw. harv, f. id. beside hárv, pl. -ar, f. ‘rake’; cf. EMSw. härvel ‘buckle’; Blg. krap, adi ‘short’; Li. karpas ‘cutting, clearing’; karpà ‘slice’; kárpa ‘wart; Latv. kārpa, id.
20089:uers- (3) 'growth, hard skin' Lat. cf. verr-üca, f. ‘wart; hillock’; OE wearr, m. *callouse'; OFris. cf. (?) wersene ‘wrinkle’
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
3220:der  Spitze  des  Satz(teü)es  stehend  (s.  No. 5,6);  i)  zeitlich 'dann,  darauf,  da';  ''fra- yaire  ayati  .  .  "oa  apare  ayqn  "am  Vor- mittag . .,  dann  (aber)  am  Nachmittag" Aog.5^;  V.  ii.4,  20.4,  N.5J,  F.7,Vt/9. 48;  —  -da  tala  giul  pir>sat  aspm  "da fragte  der  Schöpfer  des  Rinds  das  A."  Y. 2^.2;  — 'da  sl''  ,.  bavaiti  sk>ndö  spaya- %raAyil  (sd)  Y.jo.io;  —  ya%a  va/i  iäd.) ..*''öai^  aaAö  a/ava'V.yi.16.  a)  hinter yäoi:  yet'A  sT  hvar»  nöit  uzttxlyeiti  °oa  . . "wenn  (erst)  die  Sonne  nicht  mehr  auf- geht, dann  . ."  Yt.  6.3.  b)  "oo  .  .  °cit °'6a  'dann  wenn  .  .  dann':  "aa  syäscif pairipataili  'oa  fraistim  vöiynanqm  (sd.) V.  7.3.         a)  anreihend  'und,  und  auch':
4569:—  yat  °ri  vir^ka  ''as  *mat-^Ja  (sd.)  V. 18. 70  PüZ.;  —  °r?  zam  asmaii>mia  "zwi- schen Himmel  und  Erde"  Y. ffcS*.  15;  Yt S,%,  10. gs,  /J.13',  43,  44i  —  kax^örimia . .  "rt  mäahpmca  hvar>ca  Yt  ö.  5 ;  —  ..  *fra- Äifia'ft  (sd.)  *"r?J>  ütrimäi  barssmaca  it.6S;
4657:•  g.  anya'dä  ('da-ca)  Adv.  'anderswo'; hvar/tariqm  iyadacä(sd.)  -daca  vtrszyatntta- nqmca  väv^nzananqmÜä  Y.J5, 2.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4810:1.  a)  "herausgehen  aus  — '  (Gen.):  vai- \anhS  (sd.)  n5/V  uzSis  (aSPrA.)  V.J.  15 PüZ.(?).  a)  'aufgehen',  von  Gestirnen: yaira  avat  hvars  uzliti'J^F.4h.  3) 'hin- auskommen über  — ,  über  werden',  mit Äaca  und  Gen.r  ya'ia  as»m  uzayeni  haia kavsis  haosravauhahe  Vt  i^.  32.
4959:, .  Ailu  maza  m^rr/S  .  .  "ve  awrä  YL  z^.  *malnis  (sd.)  atiAat  pouruye  vTdv^  "vqm 41,  a)  mit  einem  ergänzenden  odsT  yä  im  af^Aaeapjma{^.)Y. 44.1g.  II)in erläuternden  Relativ:  'z'aj  karsvar}  _yff/' schwachdeiktischem  Sinn  'jener,  der'; *ar3zaAi  *savaAi  .  .  imat  iar^ar?  yat\  I)  auf  Vorhergenanntes,  Vorausgehendes :i^amra^sm  V.ip.^t);  39';  —  imS  /-irciv/ j  (Wort  oder  Satz)  zurückweisend;  i)  auf barizist^m  barszimanqm  °3raJ'>  yat  hvars  ein  Substantiv,  a)  adjektivisch,  auch  im avacT  "das  Licht  hier  (und)  jenes  Höchste !  Sinn  unsres  Artikels  (des  schwachtonigen unter  den  Hohen  dort,  was  Sonne  heisst"  'der'):  I  ka"bajiyJ' .  .  paruram  idä  xsäya- Y.  j6. 6.  2)    ohne    solchen    (ausge-  aya"  aAJ^  °vaAyü  k(fbüßyaAyS  brälä  bar-
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0.90;  6.4;  —  'tun  bavähi T-3r/irayn3m. .  ya^asli  antan  ahuna(&A.)  yaia  kiari  Az.  6";  —  am.nakc  hü  yat 'manaiAD.)Vi.24.i;*li.ioj.  a)  sonst |  Vn^  YLJO.  13;  —  hiarsxsaS^m  'ptm mit  isya-.  'mamm  isim  .  .  ßäsB  mq^fvm  Yt  6. 1,6, 12.^4, 1^.81,  \.  16.4;  —  hvar>- ..  b»r?am  Aa',aoxt?m  Vr.2.10;  G,/.6,  S.j^/attJj  °päi  Y.ÜÄ22;  —  hrerixiaiiahe 2.3;  —  tfm..  vJspanqm  sravanhqm  ufard.-\ ..  -pake  Yt.  Ö.o,  Y, 22. 24;  /.  11;  —  Iwan- kainm  fradaiqm  yim  'mamm  tsim  FrW. '  xsaiia  'pa  (VS.)  V,  j/.  5,  b)  von  apqm 4-1',  1 ;  —  'taan^m  isim  . .  maiisüm  o/aAe  napät-.  apqm  napa  -ps  Yt  ig.  51';  — sra-.arahqm  Y.54.2;  Vr.  24,1;  —  °manS  aPqm  napättm  'ptm  Y.  2. 5;  —  apqtn isyehe  hafu{iitä..'manö  isyeke ,.  haililca  ..  nap5  °pa  Y.65.13.  'pä'a  VyLjJ, Vr.24.2;  /.8,  S.7.3.                                    4'>"(?).
6861:garS  nmartptn  mai^anpm  'rahe  mazdä  V, '5-3*i  Vr.7.  I,  Vt.j.4(?);  —  vahiits aiphul  yö  mana  yat  °rahe  mazda  P.  4"; '^'^•33\  —  "vi  'rahe  mazdä  .  .  gätvS zaranyöjants  V,  ;p.  32;  —  hvarpca  xsai- lahe  .  .  dsi'irahe  'rohe  mazda  Y.  i.ii; 68.  22;  —  raocsbli  .  .  yäis  'rahe  mazdä Y.  5&Ö;  —  uyrpm  kai'aZ.n  p^ar^nS  ..yat
6871:Am?l'a  (^tvm.,va.ttx A. R-a.)  Sp^nta:  rumas» ts  'ra  mazda  ,  .  rumS  vS  amiiä  spsntä  . . allal  *jih<tt  'r)m  mazdqm  astat  am»si spjnts  Ny.  1. 1;  Y.  68.22;  usw.  b)  im Gegensatz  zu  A/jra(sd.)Mainyav:  xihae- ^ra  "rahe  mazdh  laröidtti  anrahe  main- ySus  Yt./.o;  —  sna>ai  attrahe  maittySuL. /rada%äi  'rahe  mazdiY.2-j.\(.  2  K)aAu- rahe  ma-id?!  (näml.  ayarg)  heisst  der  i. Monatstag:  'rahe  mazda  raivatS..  S,/,i, Y.j.  ii;vgL/6:i,S.2. 1.  3)inGHapt.; 'ra-  ist  einmal  Ci-3S-l)  von  mazdäh-  ge- trennt, sonst  steht  es  unmittelbar  davor oder  dahinter:  huxsa'irS.timüi  ..  xla'hnm .  .  *hvqnmahicii  kyat  mazdäi  'rat  Y.J5. S;  s.  A,_j.  6;  —  mazdil  'rä  . .  kätqm  hu- dsslfmä  \.4i.  2, 4;  —  'rä  mazda.. vaahuda YjA'.4;—  vohü  xsa'hr»m  tsi  mazdä  'rä apaSmä  Y.^/.  a;  —  sralstqm  at  tSi  k»hr- pSm  .  .  ävaSdayamahJ  masdä  'rä  . .  avat yät  hvar!  aväcl  V.j6.6;  — yäsctJ  tsi gmä  *'ra.mazdä^''>  Y.  j8.  i;  ^5.  3,  9;  — hyat  mizdjm  *mafai^im  (sd.)  Jradadfiä .  .  masdä  'rä  V.40.  i;  i,  4;  —  läa  äl yazamaide  'rtm  mazdqm  y}  gqmlä  ahmiä dat..  Y.3-J.  i;  —  BitJ  yä  v3  ..  '1^  mazdh *nämqm  dadät  ..  Y.  ^JÄ  4;  —  dätdl  a/.. mazdä  'rä  . .  västryJng .  .  akmaj-afonat>hs (sd.)  Y,  4a.  3;  —  ya^ä  tu  l  *'ra.mazdä^^ minghäcä  .  .yä  vohü  diä  tSi  dadunahi . . a^ä  iiSidyämahl  ^wä  mazdä  'rä  Y.yp.4; j6.  5,  I ;  —  'rakyä  :l  at  vi  mazda  yas- n»mcä  .  .  amSAmaidt  . .  Y.J5. 7;  —  ^wDi staotarascä  ..  ^''ra.mazdä"'^  aggitnadailä  .. Y. 41.%;  —  ätari  vSi (sd.)  mazdä  'rahyä ahi  Y.J6.3; — äiar^  mazdä  akurahyäY. 36.1,  3.  a)  in  Verbindung  mit  n)  Asa (sd,,  unter  A  1  a)  und  ß)  Asa  (sd.,  unter A  1  0,  VohuManah  ua.:  a)  *'ra.mazdä"'^ d/ä  srTrä  Y.  J^.  $;  — stets  garS  vahmSrtg 'rät  mazdäi  asäicä  vahiääi  dadtmahicä Y.  41.  I ;  _95.  s;  —  mazdä  'rä  .  .  iava/ä sar)iit  asaliyäcä  Y.  41. 5  f. ;  40.  i  f.  ß)  yaza- maide 'rillt  mazdqm  . .  ahm  ..  vahislmt  .. 7ighucä  inanö  . .  vohttcä  xiäi^rim  . .  Y.  ^-j. I— 5-  4)  im  gAw.  (ausser  GHapt,), Es  sind  hier  die  Strophen  herangezogen, die  ^ahura-  und  'mazdäh-  im  gleichen Kasus  enthalten;  s.  dagegen  I  z.  Die Stellung  der  Wörter  ist:  ah'..m',  m'..ah' (in  beiden  Fällen  ist  die  Trennung  oft erheblich);  m°  ah",  ah' m'  (im  letzten  Fall trifft  stets  die  Zäsur  dazwischen:  Y.  2^.  9,
7883:1)  'hin  zu  gehen  zu -',  mit  Dat. ■>  (statt  ,_(,aj«,j,-  Vr.;5.2;  V.jff.i^s'  (wo  "0,7),  2;. Akk.):  husiti  ..  äanyuMti  (sd.)  ite  vJse  (,^  Yti-agS;  —  aim  mSt  'äS  iw/y  (sd.) afrXnümi  yahmat  haca  . .  ".  .  in  (dessen) ' yj  „5  a?i-ö  . .  Y.  2(J.8;  —  iv//tt  -ö«  . .  hvar- Haus  zu  gehen,  von  dem  .  .'■  ^.6S.^lt)m  lyaoi:ni>m  S-s^i^i; —ya>a  yat '<.a 14.  a)'einzugehenauf-':iJOTff^^ä^W/|ana/rj'rf  daiühus  hakat  m^a  us./raraysil moi  data  danga/tya  *yaoi  ySm  vä  *nagas  (sd.)  YL  75.68;  V. 5.56,  y.55;  —  ime  nö däfMt  its  vairya  stdt/isd.)  "..ihn  sollt  ihr|.  .  aspa  para  *miira  *'c,a'>  iiaymU  (sd.) mir  gewähren,  auf  den  einzugehen  keiner  yt.io.  42;  60;  —ha  hl  asti  ä>a  ..aipi.- euch  zwingen  kann,  (den  Wunsch) .."  Y.  panmnäi  'oa  aSaone  V.Ä107;  —  ktj'M 43-^'h-  'ffff(sd.)''oa  alsum  agate  Y.ig.^i;  —  'oa
8126:u  '.ind'  oder  t.U  (n  d)  -bis.  usw.  bis'. '  aufmachend  :  /rdvaiayS Für  den  lelitren  Werl  vgl.  N.  44  mit  43  .  .  hvar?tS  .  .  Yt  7  J.  23. (wo  lä/i)  und  42.\  \      Komp.:  Ufra-^*arjt-.
9299:II  .)f*;,L!'-o7/"jriTverstiimmelteUä'ä  kavä  ..\.44-  2°;  —  .V^'^-  *grihm<l Formen.  Man  erwartete  »i^^jr/jK/j/,  »i-riHÄwA  [(sd.)    aM  varata   'pa   xsairimcä    Tianqm
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
9547:('Leichnam':  nDrfjtm  ..  upa  tarn  'ptm ' fratauharaitl  yqm  iristake  maiyeheV.^.x; ' — pqslö./ra'^a?»h»m  (sd.)  Al  kam?r?}.»m Ivinä^ay^n  ..  as.:^arft3maEiby3  ..*k3r»ß.- ifarqm  '/s  (als  Akk.)*'  paiti  nisirinuyJl \va\)qm  .  ,'^. 3.20;  —  yd  nar!  asaonö 1  iriri>usö  z»m  -pa  (statt  AS.)  nikainti  V. j.  40  PüZ.;  —  ma:dayasrta  aStsm  'pim hvarp-dansim  (sd.)  k?rjiiavqn  V.  5.  13; 14;  —  s.  noch  KompA.  a)  im  Gegen- satz zu  urvan-,  matiah-,  ifvTsl-:  ahurahe mazda  . .  yeähe  urfa  . .  "pas.'a  (NP.)  y3 ral^wayeiti  (sd.)  .  .  Yt  13.  81;  —  yö aSnatthaiti  nö  maiiS ,  .  nB  'p?m  Y.  9.  ag; —  frä  tS  'p»mca  imulmca  yao'zda'^äni V.3i,6;  —  ima  'pasca  tn-lsls:a  Vr.j/,3; Y.  55.  1.  3)    von   Tieren:  yal  barata
10219:{sd.)..'rd  thmSmY.$0.^\  —  Ayal  mlzihm zard^usirO  magavadj/U {sA-)  Üsisl  para  "rd d»mSnS  ahurS  masds  jasat  (sd.)  Y,  5/. 15.  b>  im  jAw.  (immer  in  der  Folge ^  nm°):  xsnäts  asaonqtn  urvanö  p3rayeiiiti . .  avi  'rS  nmäiDin  mal^amm  ahurake. mazdS  ..  amgsanam  spfntanqm  ..  anyalsam asaonam  V.ip.32; — 'rS  nmäitpm  ahurahe mazdä  yazamaide  Vr.  7.  i;  —  °rJ  nmämm asti  "nfrfyö  asävaoyd  Ytj.  4^4;  —  *°rB iimUne  ahurahe  hvSyaomm  Yt.^j,  3;  — zaoirä  .  .  ni  hJs  dasva  *'rS  nmäne  Yt, 10.^2;  —  urvätam  , ,  m»rtkw3fä3m  kuma- taglu  .  .  häxtagsu  ,  .  hvarstaiht  .  .  *°r5 nmansm  Ylij.  84;  —  ahurahe  mazdS.  g" fumän^i  yat  srlr?m  VyLJ'^^;  —  °r!f  sp3n- tahe  n>mäne  Vyt  28.  a)  sonst  mit raoxma-  Adj.:  raoxliam  "rS  ntnSrum  S. 2.30;  —  haca  raoxiha  *°rB  ttmäna  .  . .rr/ata  haca  duianha  Yt. /().  44;  —  mt- "ir^m  ..yim  yasata  ahurB  mazdä  raexsnät paiii  *'r5  nmänät  Yt  iQ.  IJ3;  *I33;  — raoxmahe  *°r5  nmänahe  S./.30,  Yt.72.37,
10247:AumataSa   hastaca  hvar^aca;    aiwi^trü-  bleiben  oder  sich  im  Hals  festsetzen"  V,
11070:sind  getrennt:  yS  gam  ia^d  apasca  itrva- rh^ä  Y,5/,  7";  — yi  .  .  amfrstatäUm  .  . as>mcä  .  ,  dätakä  (sd.)  .  .  xsairimla  Y. g4. 1 ;  —  a  mä  alhmö  hazascä  [rw»fl] '"' äkiSäyä  (sd.)  ä?nsiä  tivilcä  Y.  2(j.  i ;  —  mos- tJm ..  sparumca  vtniiraytumca  vanaitttlmca uparatät»nt  YtJ,  36;  —  apqm  napas)  tä äps  . .  vlbaxsaiti  vätasca  . .  awidätimla c^arfnB  asaonqmca  JrmiasayS  Yt.  8.  34; Y.  j/.  2a;  —  anyS  asSI  'kwatcd  ..  vahtstä- aüä  manarthd  Y.50. 1 ;  — yada  a?»m  twTm (sd.)  anAin  maedäscä  ahurhtths  asicä  -j* armaitl  Y.3/.  4.  a)  mit  Tmesis:  srao- s)m  .  .  asimca  . .  nairimca  saahfm  Y.57. 3  (s.  dagegen  Ytio.  53).  c)  das  erste Glied  ist  ein  enkL  Pron,  pcrs. ,  das  sich auf  einen  dahinter  stehenden  Vok.  be- zichtJ*;  nur  gAw.:  yi  "hwat  mazdJ  .  . a^alBu^cä  ..  virtz^naRyücä  ..  atryamanascä . .  gSuscä  Y._5'_J.4;  —  anats  va  nBit  ahurä . .  aipmeä  . .  saranafirnJ  . .  maitatcä  hyaf vahisiMtt  Y.  2Ä  9 ;  —  yS  vi  asa  ufyäni manascä  vohü..ma2dqmcä  Y.25.3.  d)ein Glied  oder  mehrere  oder  alle  sind  rela- tivisch  gegeben;  cä  steht  dann  beim  Rel.: narSi  firasaoiträi  maibyäcä  yalibyascä  Ti rrivAan'Aöi  "dem  .  .  J^r.  und  mir  und (all)  denen,  denen  du  .  ."  Y.  2.9.  8;  — AviF  .  .  yas!ä  .  .  dadät  yascä  . .  vfväpat yaüä  . .  vöiidat  '^.32. 10;  —  kavaim kavätsm  yimca  kava^n  aipi.vokum  yimca^.. Yt,  /()•  7 1 ;  —  ya  äps  yssla  urvari  yasca asaonqm  fravasayS  Yt/o.  100;  —  hujUayB .  .  yS  .  .  anharj  yascä  hfntJ  yascä  . .  ba- vainti  Y.33.  10;  — yä  tsi  .  .  adistil yacil vohB  uxbä  /ras'l (sd.)  ntanankäyäcä  ff/ö.. y.44-^',  —  yä  var^sä  yäcä  pairj  (sd.) J//  syadi^ani  y.lcil  .  .  aryat  (sd.)  V.  ^o. 10.  a)  mit  unregelmässiger  Stellung  des ain  tifyänl  manascä  voka  .  . %hur>m  yaeihyS  xsairpmtä"^ ■«(sd.)..Y.2Ä3(s.c).  e)das st  nicht  ausdrücklich  genannt, dem  Zusammenhang  zu  ergän- )6  u.);  nur  gAw.:  atcä  ..  scarUB iva'ä  viitlsps  ..forasaosiras'ä id^f^undA"Yoj.a.      2)die
11741:Korrelat;  a)  substantivisch;  a)  im  gAw.: yaitat  (Sp.öi^m.)  mtzdim  ..  ndil  däifl,  kä tim  (ASm.)  ahyn  *mainis{sd.}  at^fiat  Y.44. 19;  —  ySngstü  masds  .  .  minal  (sd.)  , ., fing  zbaya(s6..)'^.46.  14;  — yqsca  haxsai (sd.)  .  .,  frö  iail  vlspais.  .  \'.46. 10;  — ya^qm  ndi^  hvarltStS  vqs  duzvari'tä,  lOi daft'fng (sA.)  dqn  \.4g.^;  —  Ayat  vä  IBi näntanqm  vazUttm  . ,,  tä  (IS.)  &wä  pairi- jasämaidl  Y.^.y,  —  y3  vS  ..  mazdä *>tämqm  dadät,  täis  vif  yazamaidl,  iai/^.. Y.JA4;  —  ptTMä  . ,  yä  iiudö  dadpntl .., ya^ia  tä  (NSf)  anfun  Y,_J/.  14;  —  yäsca tsi  g3na  ..,  ta  yazamaidi'H.38. 1;  —  hyai Urvätern  . .,  tat  ns  .  .  vüo^  Y.  j/.  3;  — : yä  frasS  (sd.)  ävJsyä  yä  vä  .  .  *p)r3saHl tayä  .  .,  ta  (APn.)  . .  aÜT  vamahi  Y. J/.13;  7  i..St,46.^;—y(i/ravaxIyä,ym tä  .,  Aai^tyi  Y.44. 6;  33-J3i  —  mit Numerus  wechseP*:  Ayat  mt:d)m  zardhustrS magavabyS  (sd.)  cöist  parä  .  .,  tä  (APn.) j'J  .  .  saväis  *avT!l  (sd.)  Y.5J.  15;  — yehyä  .  -  vaAistfm  .  .  vaida  masdä  .  ,,  tq yaaäi  Y.5/,  22;  —  at  yS  aktm  drigväitl . . var.'faiil  vaftkäu  vä  cSiäiaitl  (sd.)  astlm, töi  (NPm.)  värai  (sd.)  rädmtl  .  .  Y. j^.  2.  b)  im  jAw.:  yim  (näml.  a/rumf) vaiänte  aAurStsAS  .  .,  t»m  vafata  .  .  Vt. '4-  39t  —  yaUa  .  .  aiti  mazyS  . ,,  tat  no däyata  Y,  65. 14;  —  y^  -  ■  nigänhinti *msAii,aiti  (sd.),  nsit  tarn  . .  Y. /o.  15;  — yqm  alava  aiayqm  va^a,  tarn  drvä 7VT6va  Vt.  22,  2 ;  —  yeAhl  kätqnt . .  vanAS .  .  ahurS  val%S  .  .  yänAanUä,  tqscä täscll  yazamaidlY.2-j.\^\ — yh  nS  fanti gä'iä    hari^ravaitisca  .  .,  tä  m  Amti
11915:j  machen  (Jmdn.  sva.  es  Jmdm.)':  täpayäii mqm  asa  vahista  mqnayfn  ahe  ya%a nyaoxivst)m  Hx.1-.2q.  a)  absolut  'Wärme bringen,  schaffen',  von  Sonne  und  Mond: yai  hvara  raoxlne  täpayatt  \t6.i\  i,  7.4.
```


## [2026-10-17T00:01:44.109Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{200\\}Tadel.\\{200\\}\" BRT.txt | head -8; grep -n -o \".\\{100\\}verwund.\\{200\\}\" BRT.txt | head -5"
}
```


### [2026-10-17T00:01:44.585Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:01:48.685Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c . BRT.txt; grep -n -o \".\\{150\\}[Tt]adel.\\{150\\}\" BRT.txt | head -8; grep -n -o \".\\{150\\}Wunde.\\{150\\}\" BRT.txt | head -8"
}
```


### [2026-10-17T00:01:49.085Z] TOOL RESULT

```
30725
```


## [2026-10-17T00:02:01.800Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o \".\\{150\\}Tadel.\\{150\\}\" BRT.txt | head -8; grep -a -n -o \".\\{150\\}Wunde.\\{150\\}\" BRT.txt | head -8"
}
```


### [2026-10-17T00:02:02.130Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:02:04.769Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -a -c \"Wunde\" BRT.txt; grep -a -c \"Tadel\" BRT.txt; grep -a -n \"Wunde\" BRT.txt | cut -c1-300 | head"
}
```


### [2026-10-17T00:02:05.285Z] TOOL RESULT

```
4
0
5895:•  j.  asnae-rae§a-  Adj.  'in  der  Nähe Wunden  beibringend,  verwundend':  -ss (nämL  ist  der  Hund)  yatia  vaisS  V.  y. 46;  —  'iö  ydha  jahika  V.  rj.48.
16415:13.  132;    —  yimca   kavam    'mm  (AS.)->   ,  ^  ^^5^^»-  m.  i)  'Quetschung.  Quetsch- Ei|!'Bed.?     Ob  A(ygl.  aipty^sinah-  (zum  V.   r"*^^'    Jü"   j^'^Pfe«'   Instrument   beige- '■'■r/B''«flj-,  S2.i)?  — »Sid'/aE.   brachte  Wunde':  _>■?  jfiwe  'nm  jatntt  ytm
16695:Vgl.  got.Äoiy o 'Wunde',  ahd.  *a«fl' Verderben'». —  S.  auch  'band-.  —  Pü.;  vimärhtilan,  erl. : ähökcmian.  —  ■>  S  3g6.  3.  —  ')  Vgl.  dagegen IQ  ^aAümM-.  —  j)  Doch  a.  Zupitza  Gu(t,  30.
27496:'Komp.  mit  ND.  (*.  srü-  NÖ.  3)  im  1.  Glied; "iläy  f.,  zum  V.  ttä-,  s.  daiu  ZDMG.  4^.  665 und  mp.  ittnii.  Eig.;  'dem  ein  Horn(spltzen)- paar  als  Ständer  dient',  vom  Pfeil,  an  dem unterhalb  der  Spitze  ein  paar  Hornspitzen  als Widerhaken  eingesetzt  sind,  du
```


## [2026-10-17T00:02:11.242Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -a -n -i \"xwār\\b\\|xwar \\|xwār \" PHD.txt PHD_mackenzie.txt | head; grep -a -n -i \"xwār\\|hwār\\|xvār\" NYB_vol2_glossary.txt | head; grep -a -n \"خوار\" HRN.txt HUB.txt | head; grep -a -n -i \"xvär\\|xvâr\\|chwär\\|xwär\" HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:02:11.694Z] TOOL RESULT

```
PHD.txt:32:Sincethe ambiguities ofthe script make a mechanical translitera- tion of one letter by one roman symbol of no practical value, a certain amount of interpretation is essential, This interpretation can be based, either directly or by the use of analogy, on the less ambiguous evidence of the above-mentioned earlier documents of the language. With this help it is possible to go far in distin- guishing between the original values °’, й, dy, etc., of -», n, w, Р of у, and so on. But it is neither necessary nor desirable to go beyond this by attempting to give closer “phonetic” values to the letters, such as r for written /, or x for written h. For example, Sy hwl represents xwar ‘sun’, but to transliterate it *xwr entails both confusion with the true letter r \ and the introduc- tion of even greater ambiguity into the interpretation of .». It is better to accept that the scribes wrote r and / almost indis-
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:662:xwāb 95 xwārīdan
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:693:abject xwār.
PHD.txt:1697:drink (v.) xwaridan; cause to — xwārēn-. f
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
4332:xvārēh [hw’lyh] bliss, felicity, delight. 4722, 141-16, 10020.21, — From lavār; MPrs zw’ryy (A-H N).
4342:x"är-män [hw?lm?n'] whose house is dirty, contemptible 4522. — From ?axvār + màn (q. v.).
4922:Patišhuvari-: Patišxvār- gar
5222:katäma-: katam katära- (katarascit): katarcihé Kavärasman-: Karazm kaväta-: kavät kavi-: kai kavi-: kayak kavi-(usan-): Käyös kay-: citan kohrp-: karp keresaspa-: Krišāsp kū (kuda): kū kutaka-: kötak xrafstra-: xrafstr xratu-: xrat xrvidru-: xurdruš ni-xšata-: šastan xša0ra-: šahr xSa0ra-vairya-: šahrēvar pati-xSay: pätixsäi xšinaka-: šmah xŠnā-: šnāxtan xšnav: Šnāyišn (ava/avi-) xšnav-: ošntitak xšusta-: šustan x$viwra-: "šif(a)rg xUaöna-ayah-: xYan-asén xUačpal0ya-: xVēš xVafna-: xYamn x"üirizam-: xVārizm xUanat.caxra: x"andan
HRN.txt:4576:kurd. ymnn^ y^ärin essen ; af;'. yöral; oss. d. xvärun,
```


## [2026-10-17T00:02:15.905Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4325,4345p NYB_vol2_glossary.txt | cut -c1-400; grep -a -n \"xvär\\|x^är\\|yvär\\|yär \" HRN.txt | head; grep -a -n \"x[vw]ār\\|xvär\\|xwār\" HUB.txt | head"
}
```


### [2026-10-17T00:02:16.256Z] TOOL RESULT

```
?x"ür [hw?l] contemptible, sup. —-tar 4218 (gl.). — Bal. whär ‘dirty, foul, spoilt’ (Langworth Dames) leads us back to an original *hü-vära-‘swinish’: Av. (1817) hu-, MIr NP vik ‘pig, swine’; as to the formation ef šāh-vār. NP z"ür; v. also avār-mān.
x"arg [hwlg] consuming, of the fire: —-ē ātaxš 92°, with the same ending -é as in menöye, v. meno. — < *xvarka-, cf vastarg, vistarg, vitarg, vazurg, etc. Cf MPrth xwryndg or waryndg.
xuar-äsän [hwl’s’n'] the East 1137. 1201, — ‘Sunrise’: from xar ‘sun’ (v. x“arxSét) + äsän pt. of Prth ds- ‘to come’: ‘the coming sun’, Ghilain 49.
xuar-barän [hwlbPn'] the West 114?4. 1201, — ‘Sunset’ < z"ar-parün, MPrs xwrpr'n (S), from xtar + parün pt. of
Av. (851) *par- ‘to pass’, cf appurtan and
puhl; also MPrs zwrwpr’n ‘evening (A-H I) < war + ava-par- ‘to go down’. An- other w. is zwrnw’r = z"ar-nivàr ‘the West’ (BBB), on which v. van Windekens, Musčon 62, 1949, 126-127. It is very un- certain whether any of these ws. should be identical with NP xävar.
Xuar-cašm [hwlešm] n. pr. 1062-12, — ‘Hav- ing a sunny eye’, cf Av. (1849) hvara. darasa-.
xvārēh [hw’lyh] bliss, felicity, delight. 4722, 141-16, 10020.21, — From lavār; MPrs zw’ryy (A-H N).
xuärönitan [hw’lynytn'] to give to drink: frac ~ 6017-29, — V, xtartan.
www.parsianjoman.org | ool wok
x"ariha
x"ärihä [hw’lyh’] easily 1182. 119%. — From !x"àr.
x'arifn [hwlšn'] the act of eating; nour- ishment, food, drink 27°, 912.22 ete. pas- sim; pl. cas. obl. ~-dn 7418; hence
x'arifnéh det. v. n. the act of eating: patmänik ~ 7027; gost ~ 104%.
x"äritan [hw’lytn'] to give to drink: fräc audrit 432. — Another caus. of z"artan, cf xudirčnitan.
Xuärizm [hw?lem] the country of Khwar- izm 9512. 1143. — Av. (1878) X“dirizam-.
x"arm [hwlm] sleep 3215. — < a¥amr through metathesis, MPrth xwmr (S, MHC), < z"amn (g.v.) through dissi- milation of -n- > -r after -m-.
x"är-män [hw?lm?n'] whose house is dirty, contemptible 4522. — From ?axvār + màn (q. v.).
x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor u ~ + visp-ākāh spēnāk meno datar Ohurmazd 1063-24, — 2. a cosmic essence 9215.19, — 3. Zartuxst’s divine essence 36-38. 43-45 passim; the elements con- stituting his individuality are his
dour, ''glory", of the King, of the dynasty, -
of the priests: ~ i xatdyéh 7%. (81); ~ i kayän u äturän šah 12%; kayān ~ u han 4 herpat — 554; yazdan ~ i Erän šahr 52-61; in a more general sense 427. 11918; in names of towns 1165-22, — 5. fate 1311. — Av. (1870 sq.) x%aronah-, in Old Median farnah- in proper names: Vinda-farnah-, also in OP: Tioox-pepvng < *tica- (SW form of cidra-) + farnah, ’Apraptpvng etc.; MPrthPrs frh, MPrs also prh, pl. 
4308:/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
4576:kurd. ymnn^ y^ärin essen ; af;'. yöral; oss. d. xvärun,
6088:man sonst seryär erwarten müsste.
6978:798. sehryär 'Herrscher*.
9660:Wl21. yär 'Freund', yärl-, yärwer (Sahn. I, 126 Vers 1117).
9664:phlv. äyär (die Lesung scheint durch haniäyär, z. B.
9684:Suffixes -yär - vergl. beytyür 'glücklich* , hösyär
9685:Verständig', däwyär * Jäger , sehrydr 'Herrscher u.
9686:a. m., sowie den Eigennamen hfendyär etc., auch
9711:Suffix -yär ist generell jünger als -r/är, doch erscheint dieses letztere
```


## [2026-10-17T00:02:20.284Z] TOOL CALL #19: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:02:20.293Z] TOOL RESULT

```

```


## [2026-10-17T00:02:22.595Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/самовар",
 "prompt": "Quote the Russian etymology section of самовар verbatim, and any Persian/Tatar/Turkic notes."
}
```


## [2026-10-17T00:02:23.304Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/variti",
 "prompt": "Quote the etymology section verbatim (PIE root etc.) and list Russian descendants."
}
```


## [2026-10-17T00:02:24.102Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/خوار",
 "prompt": "Quote the Persian etymology section(s) verbatim (Middle Persian, Proto-Iranian, PIE)."
}
```


## [2026-10-17T00:02:24.698Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بالو",
 "prompt": "Quote the Persian etymology section verbatim, if any."
}
```


### [2026-10-17T00:02:26.784Z] TOOL RESULT

```
# Persian Etymology Section

Akin to Proto-Georgian-Zan *bal- ("wild cherry"). The nature of the relationship and the ultimate origin are unknown.
```


### [2026-10-17T00:02:27.935Z] TOOL RESULT

```
# Persian Etymology Section

**Etymology 1:**

"From Middle Persian [script needed] (hw'l /⁠xᵛār⁠/), from Proto-Iranian *ātra- / *āθra- ('spirit, breath'), of unknown further origin."

The entry notes that the Proto-Iranian roots derive from an origin of unknown provenance. No Proto-Indo-European (PIE) etymon is provided in this Wiktionary article.
```


### [2026-10-17T00:02:28.483Z] TOOL RESULT

```
# Etymology Section and Russian Descendants

## Etymology 1 Quote:
"From Proto-Balto-Slavic *wārīˀtei / *wōrīˀtei, from Proto-Indo-European *wōr- ('to burn')"

## Etymology 2 Quote:
"Perhaps from Proto-Indo-European *wer- ('to cover, to envelop'), cognate with Sanskrit vārayati"

## Russian Descendants:

From **Etymology 1** (boil, cook):
- вари́ть (varítʹ) - modern Russian

From **Etymology 2** (go ahead, overtake):
- варять (varjatʹ) - from Old East Slavic
- предвари́ть (predvarítʹ) - to anticipate/forestall
```


### [2026-10-17T00:02:31.338Z] TOOL RESULT

```
# Russian Etymology of самовар

From the Wiktionary page, the Russian Etymology 1 section states:

"From _[само-](/wiki/%D1%81%D0%B0%D0%BC%D0%BE-#Russian "само-")_ (samo-, "self-") + a deverbal form of _[вари́ть](/wiki/%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D1%8C#Russian "варить")_ (varítʹ, "to boil")."

This indicates the word combines a prefix meaning "self" with a verb root related to boiling or cooking.

**Persian/Tatar/Turkic Notes:**

The Descendants section shows the word spread widely to these language families:
- **Persian**: سماور (samâvar)
- **Tatar**: (not explicitly listed as Tatar, but Bashkir is shown as самауыр)
- **Turkic languages**: Azerbaijani, Bashkir, Kazakh, Kyrgyz, Turkmen, Ottoman Turkish, Uyghur, and Uzbek all have cognate forms listed in the descendants

No specific etymological notes regarding Persian or Turkic origins appear in the article—the word clearly originates from Russian and was borrowed into these languages.
```


## [2026-10-17T00:02:34.638Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp; for w in خوار بالو سماور; do echo \"== $w\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" $w)&action=raw\" | sed -n '/==Persian==/,/^----/p' | head -60; done"
}
```


### [2026-10-17T00:02:35.539Z] TOOL RESULT

```
== خوار
==Persian==

===Pronunciation===
{{fa-IPA|xwār}}

===Etymology 1===
{{etymon|fa|id=easy|:inh|pal:hw'l<id:easy>}}
From {{inh|fa|pal||tr=hw'l|ts=xᵛār}}, from {{der|fa|ira-pro|*ātra-}} / {{m|ira-pro|*āθra-|t=spirit, breath}}, of {{unknown|fa|nocap=1}} further origin.<ref>{{R:ira:ESIJa|vol=1|page=324}}</ref>

====Adjective====
{{fa-adj|tr=xvâr}}

# {{lb|fa|archaic}} [[easy]]
# [[mean]], [[abject]]

=====Descendants=====
* {{desc|kk|қор|bor=1}}
* {{desctree|ota|خور|tr=hor|bor=1}}
* {{desc|tk|har|hor|bor=1}}

===Etymology 2===
See below.

====Verb====
{{head|fa|verb form|tr=xvâr}}

# {{verb form of|fa|خواردن||pres|stem|form|t=to eat, to consume}}

===References===
{{reflist}}

==Ushojo==

===Etymology===
From {{bor|ush|fa|خوار|tr=xvâr}}.

===Adjective===
{{head|ush|adjective|g=|tr=xvār}}

# [[weak]]
# [[vulnerable]]== بالو
==Persian==

===Etymology===
Akin to {{cog|ccs-gzn-pro|*bal-|t=wild cherry}}. The nature of the relationship and the ultimate origin are {{unk|fa|title=unknown}}.

===Noun===
{{fa-noun|tr=bâlu}}

# [[cherry]]
#: {{syn|fa|گیلاس<tr:gilâs>}}

====Derived terms====
* {{l|fa|آلوبالو|tr=âlubâlu}}

====Descendants====
* {{desctree|axm|բալ|bor=1}}

====References====
* {{R:fa:Steingass|بالو}}

{{attention|fa|please, check}}

{{C|fa|Stone fruits|Fruits}}

==Ushojo==

===Noun===
{{head|ush|noun|g=|tr=bālū}}

# [[hair]]
# [[hair]] ([[singular]])== سماور
==Persian==
{{wp|fa:}}

===Etymology===
From {{uder|fa|ru|самова́р}}, literally “self-boiler”; from {{m|ru|сам|само́}} “self” + {{m|ru|вари́ть}} “to boil” or “to cook”. {{cog|lrc|سںمۋںر|tr=səmüər}}.

===Noun===
{{fa-noun|tr=samâvar}}

# [[samovar]]
```


## [2026-10-17T00:02:44.686Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -a -n \"'leicht\\|\\\"leicht\\|‘leicht\\|verächtlich\" HRN.txt | head; grep -a -n \"verächtlich\\|'leicht'\" HUB.txt | head"
}
```


### [2026-10-17T00:02:44.960Z] TOOL RESULT

```
4495:496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
4498:in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
4501:Die Bedeutung 'niedrig, verächtlich' ist erst neu-
6259:phi. sr(u)p; sabuk 'leicht' = paz. sabuk Min. 61. 180 — 181,
7737:'leicht' = zd. x^a&ra-; x^astan Vunschen', x^ai *Wohl-
```


## [2026-10-17T00:02:55.060Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4490,4512p HRN.txt; sed -n 7730,7742p HUB.txt; python3 -c \"\nt=open('HRN.txt',errors='ignore').read().split('\\f')\nfor i,p in enumerate(t):\n  if '496. x' in p: print('leaf',i)\n\""
}
```


### [2026-10-17T00:02:55.445Z] TOOL RESULT

```
Kä§. ;^öw?[es; hevoft 'schlafen*.
aw. /'a/wa- *Schlaf; phlv. /*'äÄ; ai. svdpiw-; arm.
^un (H. No. 295).
kurd. /evii, /evin; af/. LW. yöb; bei. ^?a/>, n. väir
(410).
496. x'^^^ 'leicht, gerade; niedrig, verächtlich', x^^ärT,
aw. /'ad-ra- (Geldner, KZ. 25, 478, Studien I, 17
folgg. ; Darm est eter. Et. ir. II, 189)'); phlv. /"är, nur
in der Bedeutung 'leicht', /"änha *leichtlich' (Sa le-
rn an n, Mel. asiat. IX, 234).
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
Ahmatan also fiir *Hahmatan, Vgl. § 143, a.
Im Inlaut zwischen Vokalen scheint A = ap. A nicht
geschwunden zu sein, selten h = ap. &, siehe § 60.
§ 108. Ap. uv (fiir huv ?= zd. a;", ^uh = idg. sv)
wird im Np. zu x^\ inl. nach a zu x:
a) im Anlaut: x^arazm =^ ap. uvarazmis; x^ahar
'Schwester = zd. x^a/ihar- ; x^ob 'Schlaf , zd. x^afna- ; x^ar
'leicht' = zd. x^a&ra-; x^astan Vunschen', x^ai *Wohl-
geschmack' (oben p. 57), skr. svad; x^andan *rufen, lesen',
skr. svan *tonen' ; x^ai 'Schweiss' = zd. x^a^a-, skr. svBda- ;
x^'ar, spater xur 'Sonne', gewohnlich x^arsBd, xurSed = zd.
"^x^are, gen. x^eng (neben hor 'Sonne' = zd. hvare, hvare-
rsa^tem, gen. hu und hUro =- skr. siiar, gen. suras); x^ar-
leaf 131
```


## [2026-10-17T00:03:03.599Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('HUB.txt',errors='ignore').read().split('\\f')\nfor i,p in enumerate(t):\n  if 'zd. x^a&ra-' in p: print('HUB leaf',i)\n\"; grep -n \"بالو\" BQT_v1_pages.txt | head; grep -n \"^خوار\\|خوار ـ\\|خوار -\" BQT_v2_pages.txt | head; grep -n \"خوار\\b\" incoming/ARY/ARY_pages.txt | head -5; grep -n \"بالو\\|سماور\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-17T00:03:04.263Z] TOOL RESULT

```
HUB leaf 227
HUB leaf 228
1327:۳ جر مق 6۲۳۱۱6:) و بالو ۳۵112 است.
3512:( ذیل: نرمدست)» واشه (ذیل: بالوانه)» والوچانیدن (ذیل: خمانیدن وذیل:
8321:رین بالولة بلند که درآن‌آب کنند .ملکی باشد . *
8637:» آئبالو 6مع۳1ه وناصطظ درخئی است از وتا بادامی ها از تیرژ کل
8642:درهمدان که بالوند شپرت دارد ؟ . «
8725:حرآنگ هکه توشنه کیتی بخون بالودی این خنجرآبگون فردوسی «لفت‌طمه».
8829:بونانی نگاسته را گونند که از آن بالوده و
10344:همدان مشهور بالوند .
12911:کنناکناع ۸ (عالی ۰ عظیم , مقدی » . لقب اکتاوبالوی و هم امپراتوران بعدی « مرچنت * .
15892:یا بو نه ‌ با تای‌فرشت مر وزن بالوده ۰
1157:تومشرگی (71718771701788)) سغدی (80001۸30) با کتربایی (8۸2771۸0 خوارزمی
4931:معنی واژه‌ی .5۳۸۸-۳3681 در زبان آلمانی: خوکك شیرخوار,
3126:بالو (به چم ازگیل" َْخ) / ۱:۹
```


## [2026-10-17T00:03:07.538Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3118,3140p incoming/ARY/ARY_pages.txt; grep -n \"^بالو\\|بالو [:ـ-]\\|بالو:\" BQT_v1_pages.txt | head; grep -n \"زگیل\\|زخ \".. BQT_v1_pages.txt | head -3"
}
```


### [2026-10-17T00:03:08.044Z] TOOL RESULT

```
اوستایی (/4589740): ادن ۹ اففانی (پشتر) (47080۷7): 8278577۲
پارسی‌باستان (42۷ا۳8۶۵ طا0): سانسکریت (84۸/877):
7 ,827۴5111 7 ,8۸7373181
پهلری (/۲اتنه): 57 بونانی (07555)(شاید) 816۸
اوستی (05357/6): 8/۸2 گرتبکه (007[716): 05
ا
[pdf page 108]
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
17156:بالوایه - بنتح بای حطی . پرستول
17165:بالودن « بر وزن آسودن » بمعنی
17175:بالوس است که کافورمفدوش باشد» چد درفارسی
23533:بالوابه ویاله :۰ . ۱ . رك : پالونه.
23558:بالوده ِ- بروزن| اوده.سروف‌امت
23569:بالوش- بروزن آغوش؛ کافورمفشوش‌را
23571:بالو نه هه بر وزن وآژونه. بمضی‌پالوانه
7739:همواره پرآزخ است آن چش فزاکن
15966:اهر یمن و دیوان و مکان درزخ دانسته شده « خرده اوستا ۸۷ ح ۲ » . در پپلوی نبز کق2021
16374:بسوزد چو دوزخ شود بادغر . خسروانی .
```


## [2026-10-17T00:03:12.051Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 17140,17180p BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1<17160' | tail -1"
}
```


## [2026-10-17T00:03:13.854Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^بالو\\b\\|^بالو \\|^بالو$\\|بالو -\\|بالو ـ\\|بالو -\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt | head; grep -n \"^پالو\\|پالو -\\|پالو ـ\" BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:03:14.349Z] TOOL RESULT

```
بالنگ - بروزن آهنگه. نوعی‌ازترنج
باشد که سار شیرین و نازك شود و ازآن مر با
سازند - و جنی از خیار هم هت که آنرا
بادرنگ خوانند .
پالنگو « ,کر الك‌وسکون رابم‌وکاف
فادسی بواورسده ؛ دوابی است که] ترامادر تجبوبه
خوانند و درعربی یله اترجیه گویند .
پا لو - بروزن‌خالو . برادریراگوبند که
از يك مادر و ی پدر باشد - و بمعنی آزخ هم
هست و آن دانهایسشت باش. که دراعنای! دمی
بر هی آید ودرد نمیکندء آنرا بعربی تولول
خوانند - و ممعنی آواز حزمن هم آهدم است ‏
با لو اسه بروژن‌شاه کاسه ۰ بمعنی‌ثار
باشد که در مقابل بود ی
دالوافه - بر وزن آسمانه . مرغکی
باشد کوچكوسیاه کدشیر ازبانآ نراهواشه» کوشد.
بالوایه - بنتح بای حطی . پرستول
باشد و آن برنده است در سقف خانها آشیان
کند ۷ . و به‌ضی گویند پر نده‌ایست کوچك وراه
و کوتاه پاچه که شب و روز در پرواز میباشد
مگر درهنگام بجه کردن که بسوراخی رودوا کر
برژعن اد زتو اند بر خاست و آ را بعر ی ابایل
گوشد. .
باوث « نم الت ر سکون واو و دال,
عمنی افزود و بالید و نمو کرد وبز رکه شد ۷
بالودن « بر وزن آسودن » بمعنی
افزودن و بالیدن و نمو کردن و بز رکه شدن
باشد ۸ .
۴ - بالیغ در «فولی بمعنی شهر است
ه‌ ۳۳۹ .ك ضِ بادارنگک و بادرنگ.
آب و آاش بهم نيامیزد
۲ تراد : بالودن.با لو س ت برءزن‌سالوی ء,کافورمخشوش,ا
و
۳۹
پا لوش - با شن‌قرشت . بروزن‌وممنی
بالوس است که کافورمفدوش باشد» چد درفارسی
سین بشن و برعکس تبدیل می‌باید .
باله - بروزن لاله . قسمی از جوالباشد
که چیز ها را در آن کنند 4
پالیك - بر ون ناهید . ماضی بالیدن
است یمنی افزون کردید و نمو کرد وبزر که شد
```


### [2026-10-17T00:03:14.591Z] TOOL RESULT

```
BQT_v1_pages.txt:17156:بالوایه - بنتح بای حطی . پرستول
BQT_v1_pages.txt:17165:بالودن « بر وزن آسودن » بمعنی
BQT_v1_pages.txt:17175:بالوس است که کافورمفدوش باشد» چد درفارسی
BQT_v1_pages.txt:23533:بالوابه ویاله :۰ . ۱ . رك : پالونه.
BQT_v1_pages.txt:23558:بالوده ِ- بروزن| اوده.سروف‌امت
BQT_v1_pages.txt:23569:بالوش- بروزن آغوش؛ کافورمفشوش‌را
BQT_v1_pages.txt:23571:بالو نه هه بر وزن وآژونه. بمضی‌پالوانه
BQT_v1.txt:33312:بالوایه - بنتح بای حطی . پرستول 
BQT_v1.txt:33323:بالودن « بر وزن آسودن » بمعنی 
BQT_v1.txt:33341:بالوایه مروزن خا کیانه ات که شاد مولف‌آن بااوانه دا صحبه مبدانتد است: 
8676:6 آلوپالو - آلی‌بالی . رجوع به « فاراسیا » شود . ۱
23550:پالوث ‏ بروزن آسود , ماضی پالودن
23553:پالودن ۳ بر وزن آسودن » بمعنی
23607:پالودجان خویش بيالونة بلا
```


## [2026-10-17T00:03:31.463Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=17147 && /pdf page/ {l=$0; n=NR} END{print n, l}' BQT_v1_pages.txt; grep -n \"بالو\\|ازخ\\|آژخ\" FRS_pages.txt | head; "
}
```


### [2026-10-17T00:03:32.384Z] TOOL RESULT

```
47: ‫شدهرا باطبع وانتشار آنسرافراز فرمود ازخداوند خواهانم کهاینوجود‬
83:‫اینت که ازخوانشد گات حترمی که بعدها با اینطبع سرو کار‬
204:‫ميزسته ازخود‬       ‫یآجان‬
489: ‫ترحاربمرشخآصن‌ساخت»ظاهواً یکی از مالکن آننرا ازخودبر حاثة‬
661:‫همت بلند و دست ودل باز ایشانست‌قد‪.‬م نمایم وازخدا بقایسالامتو دوام‬
788:           ‫‪- ۱‬ن ‪ :‬آسا » دهان در باشد چنانکه دهان باز کند ازخواب یاکاهلی‬
1625:              ‫توهوا زی حدبغاب ون‬              ‫ءردهان ازخرد سین کو راد‬
1801:‫کنده ببرازخانه بیرون شد بترب |‬                     ‫چرب‬        ‫اندر امد هرد با زن چرب‬
1895:‫بم رک بالومژل و مرک شاکرجلاب‬
2286:            ‫ازخسیسان بعقل بی‌جفتی‬                     ‫از لگان بطم متازی‬
```


## [2026-10-17T00:03:35.634Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c \"pdf page\" BQT_v1_pages.txt; python3 -c \"\nt=open('BQT_v1_pages.txt').read().split('\\f')\nfor i,p in enumerate(t):\n  if 'برادریراگوبند' in p: print('leaf(1-based)',i+1); print(p[:200])\n\"; grep -n \"شاکر\\|بالو\" FRS_pages.txt | head"
}
```


### [2026-10-17T00:03:36.123Z] TOOL RESULT

```
0
leaf(1-based) 447
بالش زمرسرنهادن
بالیز یر سر نهادن - کنابه از
خوشحال کردانیدن باشدکسی را.طریق خوشامد
و تیثال .
بااش قر ه مقدار هشت درم‌ودودانگ
شره باشد ‏ .
بالغ - بضم ثالث و سکون غن‌نقطه‌دار ,
شاخ کاو میان خالی با چوب
1895:‫بم رک بالومژل و مرک شاکرجلاب‬
3251:                                                            ‫‪:‬‬    ‫شاکر بخاری کت‬
3255:     ‫چنانکه شاکر بخاری گفت ه(مان ببت فوق ) و معفی دیکراز ندخه افتاده است ‏‬
4091:                   ‫و "دخ نیزگونندش» | شاکر بخاری گفت ‪:‬‬
6271:                                   ‫کاهل بسیار خوار بود ؛ شاکربخاری گوید‪:‬‬
8114: ‫‪ ۱‬کذا] بود وشاکردانه کو ند و نودران نیزکوند و کروهینباز کوند کف این‌اغت‌را‬
9224: ‫‪ - ۲‬ن ‪ :‬ابوشاکر (؟) ‪ - ۳‬س ‪ :‬زر باشده همه نقلکر ان کرده ابله ‪ .‬چ‬      ‫ندارد‬
9691:       ‫ارزیستن خیزد رم نرم [شاکربخاری کو ید ‪:‬‬
9727:                    ‫[درتر کستان ]‪ 1‬شاکربخاری کوبد ‪:‬‬              ‫نامشهر ست‬
11080:‫کافور تو بالوس "بد ومشك تو نالگ ‏ بالوس توکافورتومفشوش بود ‪] ۲‬‬
```


## [2026-10-17T00:03:40.451Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4080,4100p FRS_pages.txt; sed -n 3245,3258p FRS_pages.txt"
}
```


### [2026-10-17T00:03:40.939Z] TOOL RESULT

```
                                                                      ‫عنصر ی کوید ‪:‬‬
    ‫مور و ملخ کشیدند از کوه تاکوه نخ ‪۳‬‬                           ‫بو شید لشعر چو‬

                                     ‫‪۰۳‬‬        ‫‪«۶‬‬
                                          ‫دو خ‬
                                          ‫سا‬

‫ها نیزبافند‬
          ‫شو‬‫رها‬
              ‫فیر‬
                ‫گیاهی بود نرم در ماسجفدکهناند و ازو چون حص‬
                   ‫و "دخ نیزگونندش» | شاکر بخاری گفت ‪:‬‬
                                            ‫روی مرا هجر کرد؛ زرد تر از زر‬
‫کردن من دق کرد * نرمتر از دوخ ]‬

‫وسخ و کرس بود که برئن نشیند و کروهی مردم عا مهچرك نیز کوبند‬
                                                                   ‫[ خسروی کگفت ‪:‬‬
    ‫چه باشد دم از طمعهست باك‬                     ‫اکر شوخ برجامةمنبود‪۷‬‬
                                     ‫‪ ۶‬و ‪9‬‬          ‫‪۶‬‬
                               ‫‪۸‬‬                ‫*‬
                                   ‫ف ششُر‬       ‫‪۳‬‬

                                      ‫خربزة نارسیده بود‪ » ۸‬بوالمل گفت ‪:‬‬



  ‫‪ :‬کلج سنده و سوده کررمابه [کذا ؛] باشد ‪ ۰‬چ ‪ :‬کلج شک نن و چین باشده‬      ‫‪۳‬‬
                                                            ‫‪:‬‬    ‫شاکر بخاری کت‬

   ‫هز اران کلج بر کل‬           ‫ناده صد‬       ‫زنحر‬   ‫مشکینش چو‬      ‫ثری زان زلف‬
   ‫کلج دیگر سید کرم‌اه بانان ‪,‬اشد ‪ ۰‬ن ‪ :‬کلج دو نوع است یکی چنن و شکن بود‬
     ‫چنانکه شاکر بخاری گفت ه(مان ببت فوق ) و معفی دیکراز ندخه افتاده است ‏‬
   ‫سنی‬    ‫نید‬ ‫اهم‬‫شو‬‫‪ - ۲‬در چ ‪ :‬سد ‪ - ۳ ۰.‬شاند از مصدر شاندن بمعنی شانه کرددن‬
      ‫»‏ چ ون ‪ :‬زلفینکان ‪.‬‬         ‫؛ ‪-‬س وچ ‪ :‬صباغان ‪.‬‬              ‫‪۳‬‬
     ‫ناند‬          ‫وزل ‪- ۸ ۰.‬س اضانه دارد ‪:‬‬
```


## [2026-10-17T00:03:44.039Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"محکم\\|زیر چشم\\|ز من دور\" FRS_pages.txt | head"
}
```


### [2026-10-17T00:03:44.346Z] TOOL RESULT

```
11762:‫محکم‌ستبرساقی زین کرده‌ساعدی" ]‬               ‫گیگی پلید بینی گنگی پلید پای‬
```


## [2026-10-17T00:03:47.811Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -40"
}
```


### [2026-10-17T00:03:48.307Z] TOOL RESULT

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
```


## [2026-10-17T00:03:55.290Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 547, $2\"; }\nf \"https://en.wiktionary.org/wiki/самовар\" \"Wer 5: samovar = samo- + varit'\" \nf \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/variti\" \"Wer 5: *variti < PIE *wor- burn\"\nf \"https://en.wiktionary.org/wiki/سماور\" \"Wer 5: Persian samâvar from Russian\"\nf \"https://en.wiktionary.org/wiki/خوار\" \"Wer 6 Swer: xwâr origin\"\nf \"https://en.wiktionary.org/wiki/بالو\" \"Wer 6 Werd: bâlu (cherry sense only)\"\nfor w in serious aorta artery meteor wart warble verruca samovar; do f \"https://www.etymonline.com/word/$w\" \"etymology of $w\"; done\nfor w in سماور خوار بالو آئورت; do f \"https://vajehyab.com/moein/$w\" \"Mo'in s.v. $w\"; done\nf \"https://en.wiktionary.org/wiki/serius\" \"Latin serius etymology\"\nf \"https://en.wiktionary.org/wiki/ἀείρω\" \"Greek aeirō etymology\"\nf \"https://en.wiktionary.org/wiki/verruca\" \"Latin verruca etymology\"\nf \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wartō\" \"PGmc *wartō\"\nf \"https://en.wiktionary.org/wiki/آئورت\" \"Persian aort\"\nf \"https://ahdictionary.com/word/search.html?q=aorta\" \"AHD aorta root wer-1\"\nf \"https://ahdictionary.com/word/search.html?q=serious\" \"AHD serious root swer-\"\nf \"https://ahdictionary.com/word/search.html?q=wart\" \"AHD wart root wer-2\"\n"
}
```


### [2026-10-17T00:04:04.995Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/edd2cc6cf4f9bfa8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/db334453b5c88406.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3eefbf48400630a4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/26b8d7430a228111.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b8cc20d08fd7bb7a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/208b794a529121d1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fae69cd8ad9a8708.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d67bce29ae358a3a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/46005e3bef0f96ed.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/78edce2537b33e24.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ada40fc6db8ddacd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2aed2b4ac79bf04a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f44bdb2d71f209a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c1b451854915daf5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/53fc810c926513c6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8c169ecd35b17f4b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eaa41ee10c7c691c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/013b88b8eef5b888.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1dbed5582ad9f654.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5d6ecd9fcaf59f70.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/96fbd0a30c65e675.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7a84d222cea71022.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8e63c98a3317be9a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/75d0fd58841f2b7d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4b61209f10ee409a.txt
```


## [2026-10-17T00:04:21.557Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -40 index.jsonl | grep \"page 547\" | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'], d['bytes'], d['url'], d['file'])\""
}
```


### [2026-10-17T00:04:21.999Z] TOOL RESULT

```
-1 39 https://www.etymonline.com/word/artery data/verification/sources/web/d67bce29ae358a3a.txt
-1 39 https://www.etymonline.com/word/meteor data/verification/sources/web/46005e3bef0f96ed.txt
-1 39 https://www.etymonline.com/word/wart data/verification/sources/web/78edce2537b33e24.txt
-1 39 https://www.etymonline.com/word/warble data/verification/sources/web/ada40fc6db8ddacd.txt
-1 39 https://www.etymonline.com/word/verruca data/verification/sources/web/2aed2b4ac79bf04a.txt
-1 39 https://www.etymonline.com/word/samovar data/verification/sources/web/0f44bdb2d71f209a.txt
-1 39 https://vajehyab.com/moein/سماور data/verification/sources/web/c1b451854915daf5.txt
200 693 https://vajehyab.com/moein/خوار data/verification/sources/web/53fc810c926513c6.txt
200 465 https://vajehyab.com/moein/بالو data/verification/sources/web/8c169ecd35b17f4b.txt
200 524 https://vajehyab.com/moein/آئورت data/verification/sources/web/eaa41ee10c7c691c.txt
200 10923 https://en.wiktionary.org/wiki/serius data/verification/sources/web/013b88b8eef5b888.txt
200 20754 https://en.wiktionary.org/wiki/ἀείρω data/verification/sources/web/1dbed5582ad9f654.txt
200 6799 https://en.wiktionary.org/wiki/verruca data/verification/sources/web/5d6ecd9fcaf59f70.txt
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wartō data/verification/sources/web/96fbd0a30c65e675.txt
200 2428 https://en.wiktionary.org/wiki/آئورت data/verification/sources/web/7a84d222cea71022.txt
200 4446 https://ahdictionary.com/word/search.html?q=aorta data/verification/sources/web/8e63c98a3317be9a.txt
200 5787 https://ahdictionary.com/word/search.html?q=serious data/verification/sources/web/75d0fd58841f2b7d.txt
200 4555 https://ahdictionary.com/word/search.html?q=wart data/verification/sources/web/4b61209f10ee409a.txt
```


## [2026-10-17T00:04:26.494Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -60 index.jsonl | grep \"page 547\" | head -8 | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'], d['bytes'], d['url'])\"; for f in 53fc810c926513c6 8c169ecd35b17f4b eaa41ee10c7c691c; do cat $f.txt; echo ----; done; grep -i -A3 \"etymolog\" 013b88b8eef5b888.txt | head -20; grep -i -A4 \"Etymology\" 1dbed5582ad9f654.txt | head -20; grep -i -A3 \"Etymology\" 5d6ecd9fcaf59f70.txt | head; grep -i \"wer-\\|swer\\|\\[\" 8e63c98a3317be9a.txt 75d0fd58841f2b7d.txt 4b61209f10ee409a.txt | head -20"
}
```


### [2026-10-17T00:04:27.103Z] TOOL RESULT

```
200 11205 https://en.wiktionary.org/wiki/самовар
200 10926 https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/variti
200 2814 https://en.wiktionary.org/wiki/سماور
200 8061 https://en.wiktionary.org/wiki/خوار
200 2715 https://en.wiktionary.org/wiki/بالو
-1 39 https://www.etymonline.com/word/serious
-1 39 https://www.etymonline.com/word/aorta
-1 39 https://www.etymonline.com/word/artery
URL: https://vajehyab.com/moein/خوار
FETCHED: 2026-10-17T00:03:59Z
STATUS: 200
TITLE: معنی خوار | فرهنگ انتشارات معین | واژه یاب

معنی خوار | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 خوار

 فرهنگ انتشارات معین
 (خا) [ په . ] (ص .) 1 - آسان ، سهل . 2 - پست ، زبون .
 خوار در فرهنگ‌های دیگر
 معنی خوار در لغت‌نامه دهخدا 
 معنی خوار در فرهنگ فارسی عمید / قربان‌زاده 
 معنی خوار در دیکشنری عربی به فارسی 
 معنی خوار در دیکشنری فارسی به عربی 
 معنی خوار در دیکشنری فارسی به انگلیسی 
 معنی خوار در فرهنگ مترادف و متضاد 
 معنی خوار در فرهنگ فارسی طیفی 
 واژه‌های مشابه
 خوارکار 
 خواربار 
 خوارج 
 خوارق 
 مرده خوار 
 جامگی خوار 
 پاره خوار 
 جیره خوار 
 حرام خوار 
 رستی خوار 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید----
URL: https://vajehyab.com/moein/بالو
FETCHED: 2026-10-17T00:03:59Z
STATUS: 200
TITLE: معنی بالو | فرهنگ انتشارات معین | واژه یاب

معنی بالو | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بالو

 فرهنگ انتشارات معین
 ( اِ.) زگیل ، آزخ .
 بالو در فرهنگ‌های دیگر
 معنی بالو در لغت‌نامه دهخدا 
 معنی بالو در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بالو در گویش مازنی 
 واژه‌های مشابه
 بالوایه 
 بالوعه 
 بالون 
 آلبالو 
 بابوفیسم 
 بابونه 
 پر و بال زدن 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید----
URL: https://vajehyab.com/moein/آئورت
FETCHED: 2026-10-17T00:04:00Z
STATUS: 200
TITLE: معنی آئورت | فرهنگ انتشارات معین | واژه یاب

معنی آئورت | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 آئورت

 فرهنگ انتشارات معین
 (ئُ) [ فر. ] (اِ.) سرخرگ بزرگی که به بطن چپ قلب متصل است و خون تصفیه شده را به تمام بدن می رساند، بزرگ سرخرگ . (فره )
 آئورت در فرهنگ‌های دیگر
 معنی آئورت در فرهنگ فارسی عمید / قربان‌زاده 
 معنی آئورت در واژه‌های مصوب فرهنگستان 
 واژه‌های مشابه
 اوورتور 
 آورتا 
 اپورتونیست 
 اپورتونیسم 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید----
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 

 2.2 
 Pronunciation 
--
 Etymology 

 3.3 
 Pronunciation 
--
 Etymology
 [ edit ] 

 Borrowed from Dutch serieus , from Medieval Latin sēriōsus , an extension of Latin sērius ( “ grave, earnest, serious ” ) , from Proto-Indo-European *swer- ( “ heavy ” ) .
--
 Etymology 

 1.3 
 Pronunciation 

--
 Etymology
 [ edit ] 

 From Proto-Hellenic *awéřřō , from Proto-Indo-European *h₂wér-ye-ti , from Proto-Indo-European *h₂wer- ( “ to raise?; to bind, enclose? ” ) ; the relation between the "raise" and "enclose" meanings, if any, is unclear, though Chantraine (DELG) appears to consider the latter a semantic specialization of the former. [ 1 ] [ 2 ] Potential cognates include Old Armenian գեր ( ger , “ above, hyper- ” ) , Latin aperiō ( “ to open ” ) , Proto-Balto-Slavic *wérˀtei ( “ to thrust, prod ” ) , Sanskrit वृणोति ( vṛṇoti , “ to cover, ward off ” ) , Albanian vjerr ( “ to hang, suspend ” ) .

 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 

 2.2 
 Noun 
--
75d0fd58841f2b7d.txt: [Middle English, from Old French serieux , from Late Latin s ē ri ō sus , from Latin s ē rius .]
4b61209f10ee409a.txt: [Middle English, from Old English wearte .]
8e63c98a3317be9a.txt: [New Latin, fromGreek ā ort e , from ā eirein , to lift; see wer- 1 in the Appendix of Indo-European roots .]
```


## [2026-10-17T00:04:30.838Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -A3 \"Etymology\" 013b88b8eef5b888.txt | sed -n 1,60p | grep -v \"^--$\" | grep -i \"from\\|perhaps\\|cognate\" ; grep -i \"from\" 5d6ecd9fcaf59f70.txt | head -5; grep -i \"Proto\\|from\" 7a84d222cea71022.txt | head"
}
```


### [2026-10-17T00:04:31.250Z] TOOL RESULT

```
211- Borrowed from Dutch serieus , from Medieval Latin sēriōsus , an extension of Latin sērius ( “ grave, earnest, serious ” ) , from Proto-Indo-European *swer- ( “ heavy ” ) .
461- Borrowed from English serious , from Middle English seryows , from Old French serieux , from Medieval Latin sēriōsus , an extension of Latin sērius ( “ grave, earnest, serious ” ) , from Proto-Indo-European *swer- ( “ heavy ” ) .
 From Wiktionary, the free dictionary
 Borrowed from Latin verrūca . Doublet of wart .
 Inherited from Latin verruca .
 From Proto-Italic *we/ors-u- + -ūca , from Proto-Indo-European *wers- ( “ to rise ” ) . Cognate with varus , varix , Old Church Slavonic врьхъ ( vrĭxŭ , “ top, peak ” ) , Ancient Greek ἕρμα ( hérma , “ reef, rock, hill ” ) , Lithuanian viršùs ( “ top ” ) , Old Irish ferr ( “ best ” ) , Old High German riso ( “ giant ” ) . [ 1 ] 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=verruca&oldid=92119794 "
 From Wiktionary, the free dictionary
 Borrowed from French aorte , from Ancient Greek ἀορτή ( aortḗ ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=آئورت&oldid=91549110 "
 Categories : Persian terms borrowed from French 
 Persian terms derived from French 
 Persian terms derived from Ancient Greek
```


## [2026-10-17T00:04:45.455Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 547, $2\" >/dev/null; h=$(python3 -c \"import hashlib,sys;print(hashlib.sha1(sys.argv[1].encode()).hexdigest()[:16])\" \"$1\"); echo \"== $1\"; grep -i \"from\\|perhaps\\|uncertain\\|cognate\" data/verification/sources/web/$h.txt | grep -v \"Retrieved\\|free dictionary\" | head -${3:-4}; }\nf \"https://en.wiktionary.org/wiki/wart\" \"English wart\" 3\nf \"https://en.wiktionary.org/wiki/warble\" \"English warble (swelling)\" 8\nf \"https://en.wiktionary.org/wiki/artery\" \"English artery\" 3\nf \"https://en.wiktionary.org/wiki/meteor\" \"English meteor\" 3\nf \"https://en.wiktionary.org/wiki/aorta\" \"English aorta\" 3\nf \"https://en.wiktionary.org/wiki/aorte\" \"French aorte\" 3\nf \"https://en.wiktionary.org/wiki/ἀρτηρία\" \"Greek arteria\" 3\nf \"https://en.wiktionary.org/wiki/ἀορτή\" \"Greek aortē\" 3\nf \"https://en.wiktionary.org/wiki/varit\" \"x\" 1\nf \"https://en.wiktionary.org/wiki/варить\" \"Russian varit\" 3\nf \"https://ahdictionary.com/word/search.html?q=meteor\" \"AHD meteor\" 3\nf \"https://ahdictionary.com/word/search.html?q=artery\" \"AHD artery\" 3\nf \"https://ahdictionary.com/word/search.html?q=verruca\" \"AHD verruca\" 3\nf \"https://ahdictionary.com/word/search.html?q=samovar\" \"AHD samovar\" 3\nf \"https://ahdictionary.com/word/search.html?q=warble\" \"AHD warble\" 6\n"
}
```


### [2026-10-17T00:04:51.829Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/wart
 From Middle English warte , werte , from Old English wearte , from Proto-West Germanic *wartā , from Proto-Germanic *wartǭ . Cognate with Dutch wrat , German Warze , Hunsrik Waarz , Swedish vårta and Danish vorte .
 Inherited from Proto-Slavic *vьrtъ .
 Borrowed from German wert .
== https://en.wiktionary.org/wiki/warble
 Perhaps onomatopoeic . (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
 2015 April 16, Richard P. Grant , “Sex and the successful fundraiser”, in The Guardian ‎ [1] , archived from the original on 13 October 2026 : The blackbirds and robins and and [ sic ] tits and finches shout at each other, chups and warbles and chirrups that, loosely translated, mean “Fancy a shag?”, “Get OFF my land” or “I’ve got a great big tonker.” 
 From Middle English werble (at least for the noun), from Frankish *werbel ( mole cricket ), cognate to Walloon waerbea .
 English terms inherited from Middle English 
 English terms derived from Middle English 
 English terms derived from Frankish 
== https://en.wiktionary.org/wiki/artery
 Late Middle English arterie , borrowing from Old French artaire and Latin artēria ( “ a windpipe; an artery ” ) , from Ancient Greek ᾰ̓ρτηρῐ́ᾱ ( ărtērĭ́ā , “ windpipe; artery ” ) .
 ( anatomy ) Any of the muscular - and elastic -walled blood vessels forming part of the circulation system by which blood is conveyed away from the heart regardless of its oxygenation status ; see pulmonary artery .
 2013 July–August, Stephen P. Lownie , David M. Pelz , “ Stents to Prevent Stroke ”, in American Scientist ‎ [1] , volume 101 , number 4, →DOI , archived from the original on 23 March 2021 , page 292 : As we age, the major arteries of our bodies frequently become thickened with plaque, a fatty material with an oatmeal-like consistency that builds up along the inner lining of blood vessels. The reason plaque forms isn’t entirely known, but it seems to be related to high levels of cholesterol inducing an inflammatory response, which can also attract and trap more cellular debris over time. 
== https://en.wiktionary.org/wiki/meteor
 From Middle French météore , from Old French , from Latin meteorum , from Ancient Greek μετέωρον ( metéōron ) , from μετέωρος ( metéōros , “ raised from the ground, hanging, lofty ” ) , from μετά ( metá , “ in the midst of, among, between ” ) (English meta ) + ἀείρω ( aeírō , “ to lift, to heave, to raise up ” ) .
 ( now meteorology ) An atmospheric or meteorological phenomenon . These were sometimes classified as aerial or airy meteors ( winds ), aqueous or watery meteors ( hydrometeors : clouds , rain , snow , hail , dew , frost ), luminous meteors ( rainbows and aurora ), and igneous or fiery meteors ( lightning and shooting stars). [from 16th c.] 
 A fast-moving streak of light in the night sky caused by the entry of extraterrestrial matter into the earth's atmosphere ; a shooting star or falling star . [from 16th c.] 
== https://en.wiktionary.org/wiki/aorta
 Borrowed from Ancient Greek ἀορτή ( aortḗ , “ the arteries springing from the heart ” ) , from ἀορτέω ( aortéō ) , lengthened form of ἀείρω ( aeírō , “ to lift, raise ” ) .
 ( anatomy ) The great artery which carries the blood from the heart to all parts of the body except the lungs; the main trunk of the arterial system.
 2007 January 26, Stefan Kanfer , “In Lower Manhattan, the Echo of the Yiddish Stage Endures”, in The New York Times ‎ [1] , archived from the original on 31 March 2019 : Tracing their battles, I had many occasions to walk along Second Avenue, the aorta of the Lower East Side, exploring places that were once as vibrant and tumultuous as Midtown Manhattan. 
== https://en.wiktionary.org/wiki/aorte
 Borrowed from Ancient Greek ἀορτή ( aortḗ ) .
 Categories : French terms borrowed from Ancient Greek 
 French terms derived from Ancient Greek 
== https://en.wiktionary.org/wiki/ἀρτηρία
 Supposed contraction of *ᾰ̓ορτηρῐ́ᾱ ( *ăortērĭ́ā ) (cf. ᾰ̓ορτήρ ( ăortḗr ) ), from ᾰ̓είρω ( ăeírō , “ to bind, hang up ” ) . [ 1 ] 
 artery ( as distinct from a vein )
 ^ Farnebo, Lars-Ove ( 2023-06-02 ), chapter 4, in On the Greek Physician Praxagoras from Kos and the Development of Medicαl Thinking in Antiquity (Thesis), Lund University, pages 8-9, 20, 48-49 
== https://en.wiktionary.org/wiki/ἀορτή
 From Proto-Indo-European *h₂wortéh₂ , from *h₂wer- (whence ἀείρω ( aeírō , “ to raise, lift, hang ” ) ).
 ( in the singular ) aorta , the artery which proceeds from the left ventricle
 a knapsack that hangs from the shoulders
== https://en.wiktionary.org/wiki/varit
== https://en.wiktionary.org/wiki/варить
 Inherited from Proto-Slavic *variti , from Proto-Indo-European *wer- ( “ to burn ” ) .
 The participle ва́ренный ( várennyj ) is considered to be the "official" past passive participle of вари́ть . But its related adjective варёный ( varjónyj ) is also derived from another "older" past passive participle of вари́ть .
 Categories : Russian terms derived from Proto-Indo-European 
== https://ahdictionary.com/word/search.html?q=meteor
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 [Middle English metheour , atmospheric phenomenon, from Old French meteore , from Medieval Latin mete ō rum , from Greek mete ō ron , astronomical phenomenon, from neuter of mete ō ros , high in the air : meta- , meta- + - ā oros , lifted; akin to ā eirein , to lift up; see wer- 1 in the Appendix of Indo-European roots .]
== https://ahdictionary.com/word/search.html?q=artery
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 n. pl. ar·ter·ies 1. Anatomy Any of the muscular elastic tubes that form a branching system and that carry blood away from the heart to the cells, tissues, and organs of the body.
== https://ahdictionary.com/word/search.html?q=verruca
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .
== https://ahdictionary.com/word/search.html?q=samovar
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .
== https://ahdictionary.com/word/search.html?q=warble
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 [Middle English werbelen , from Old North French werbler , dialectal variant of Old French guerbler , to sing in a certain way (perhaps by modulating), of Germanic origin; akin to Middle Dutch wervelen and Old Norse hvirfla , to whirl.]
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .
```


## [2026-10-17T00:04:58.273Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^wer-\\|^swer-\\|^\\*\\?wers-\" AHD_watkins1985.txt | head -20; grep -n -i \"WARBLE\\|SAMOVAR\\|VERRUCA\" AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:04:58.826Z] TOOL RESULT

```
1052:swer-'. To speak, talk. O-grade form *swor- in: a. Ger- manic *swarjan in Old English swerian, to swear, pro- claim: SWEAR; b. Germanic “*and-swar6, “a swearing against,” “rebuttal” (*andi-, against; see ant-), in Old English andswaru, answer: ANSWER. [Pok. 1. swer- 1049.] swer-2. To buzz, whisper. Imitative root. I. O-grade form *swor-. 1. Suffixed form *swor-mo- in Germanic *swar- maz in Old English swearm, swarm: SWARM. 2. Germanic *swar- in Dutch zwirrelen, to whirl, akin to the Low German source of Middle English swyrl, eddy: SWIRL. II. Zero-grade form *sur-. 1. Suffixed form *sur-do- perhaps in: a. Latin surdus, deaf, mute: SORDINO, SOUR- DINE, SURD; b. Latin absurdus, discordant, away from the right sound, harsh (ab-, away; see apo-): ABSURD. 2. Reduplicated expressive form *su-surr- in Latin susur- rus, whisper: SUSURRATION. [Pok. 2. swer- 1049.] swer-3, Post, rod. Suffixed zero-grade form *sur-o- in Latin surus, branch: SURCULOSE. [Pok. 3. suer- 1050.] swer-4. To cut, pierce. Germanic *swerdam in Old Eng- lish sweord, sword, sword: sworD. [Pok. 4. suer- 1050.] swer-5. Also ser-. To lift, hang on the scale; heavy. Variant *ser- in suffixed lengthened-grade form *sér-yo- in Latin sérius, serious, grave: SERIOUS.
1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
1150:wers-2
1155:wers-'. To confuse, mix up. Compare ers-'. I. Suffixed basic form. 1. Germanic *werz-a-, whence *werra- in: a. Old North French werre, war: WAR; b. Spanish gue- rra, war: GUERRILLA. 2. Germanic comparative *wers- izon- in Old English wyrsa, worse: WORSE. 3. Germanic superlative *wers-istaz in Old English wyrsta, worst: worst. II. Suffixed zero-grade form *wrs-ti- in Germanic *wursti- in Old High German wurst (> German Wurst), sausage (< “mixture”): WURST; (LIVERWURST). [Pok. uers- 1169.]
1156:wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
2211:SAMOVAR sem-1, wer-7 SAMPLE em- SAMSARA sem-1, ser-2 SANCTIFY sak- SANCTUM sak- SAND bhes-1 SAND-BLIND sémi- SANDHI dhé-1, sem-1 SANE sano- SANHEDRIN  sed-1 SANITARY sano- SANS sen-2 SANSKRIT k¥er-1, sem-1 SAP! sab-
2449:VENUE gWa- VENUS wen-1 VERACIOUS wéro- VERB wer-6 VERBENA wer-3 VERBOTEN bheudh- VERDANT virére VERDICT deik-, wéro- VERDITER ters- VERGE? wer-3 VERIDICAL deik-, wéro- VERIFY wéro- VERISIMILAR wéro- VERISM Wéro- VERITY wéro- VERMEIL wer-3 VERMI- wer-3 VERMICELLI wer-3 VERMICULAR wer-3 VERMIN wer-3 VERNAL west VERRUCA wer-1 VERSATILE wer-3 VERSE! wer-3 VERSION wer-3 VERST wer-3 VERSUS wer-3 VERTEBRA wer-3 VERTEX wer-3 VERTIGO wer-3 VERVAIN wer-3 VERVE wer-6 VERY weéro- VESICA udero- VESPER weS-pero-
```


## [2026-10-17T00:05:14.539Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/547.jpg 2>/dev/null; pdftoppm -f 547 -l 547 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg547"
}
```


### [2026-10-17T00:05:15.314Z] TOOL RESULT

```
site/pages/547.jpg
```


## [2026-10-17T00:05:22.128Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg547.png"
}
```


### [2026-10-17T00:05:22.161Z] TOOL RESULT

```

```


## [2026-10-17T00:05:29.595Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nt=open('WLD_Bd1_pages.txt',errors='ignore').read().split('\\f')\nimport re\nfor p in (264,266,267,269):\n    s=t[p+9-1]\n    print('=== printed',p, len(s)); \n    for kw in ['sver','serius','aorta','ἀορτ','bālū','balu','Warze','verr','varīti','variti','varъ','wart']:\n        for m in re.finditer(kw,s): print(kw,':',s[max(0,m.start()-150):m.start()+150].replace('\\n',' ')); break\nE"
}
```


### [2026-10-17T00:05:30.157Z] TOOL RESULT

```
=== printed 264 6787
sver :                              11 einem Strick hinaufhangen als Mittelbegriff annehmbar, vgl z. B. av-egoei' dvagx/jaet. y.geudon Hes. und zur Bedeutungsverzweigung der gr. Sippe bes. Pott EF. 2 II 3, 102—113, Schulze Qu. ep. 420, zu den Deutungsver- suchen Liden Arm. St. 107, Boisaeq s. v., DeWitt Cl
wart : igen kontrahiert, ob-  vohl Brugmann IvZ. 27, 196 von *faguo ausgeht, da aeigco mit echtem  Diphthong et Kontraktion zu *«oco, mit unechtem zu aga> erwarten lasse:  aber da auch neben detgco „kopple“ solches gwatgexai ovvdnxezat Hes.                                                                   
=== printed 266 5069
=== printed 267 4648
Warze : pr. uarsits ,,Lippe" (siehe Trautmann Apr. 458, Lewy IF. 32, 165, Wood MLK. 1914, S. 4 des SA.).    uer-d       ahd. warga ags. wearte, anord. carta „Warze“ (Bugge BB.                                                          ,   3, 112 f.)  npers. (Horn bei Kluge 6 u. Worse) balti „ WarzeA          
verr :                                                     ,   3, 112 f.)  npers. (Horn bei Kluge 6 u. Worse) balti „ WarzeA             ,      uer-s-: lat. verruca „Waize“ (bei Cato auch „locus editus et aspei- nacli Gellius III 7), ags. wearr „Sehwiele, Warze“, flam, war re „Scliwiele, Knorren“, ahd. wer
=== printed 269 4526
```


## [2026-10-17T00:05:34.658Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nt=open('WLD_Bd1_pages.txt',errors='ignore').read().split('\\f')\nimport re\nfor p in range(262,271):\n    s=t[p+9-1]\n    for kw in ['svér','sver','svar','serius','ser','aorta','aoqt','arteria','agrrjQ','Zoroaster','var','kochen','brennen','heiß']:\n        for m in re.finditer(kw,s): print(p,kw,':',s[max(0,m.start()-120):m.start()+150].replace('\\n',' ')); break\nE"
}
```


### [2026-10-17T00:05:34.998Z] TOOL RESULT

```
262 brennen : ur auf den gemeinsamen Anlaut sit- aufgebaute Yereinigung letz- terer Gruppe mit alid. sivedan „langsam nnd dampfend verbrennen“ (Mikl. vielleieht  ursprgl. suit-, s. u. siieid- „glanzen“) und(??) mit ahd. siodan „sieden“   (Falk-Torp u. si/dr stimmt auch in der Bed. ni
263 var :        sun-are smear       ,                    sawares „die die Eggenholzer zusammenhaltenden Quer-                 saivari , stangen“, werens „Faden“, werens „ein Stick mit der Nadel mit Durch- fiihren des Fadens; Hieb, Schlag“: lit. obi-mis „Schlinge“, virvS „Strick“
264 sver : 1 einem Strick hinaufhangen als Mittelbegriff annehmbar, vgl z. B. av-egoei' dvagx/jaet. y.geudon Hes. und zur Bedeutungsverzweigung der gr. Sippe bes. Pott EF. 2 II 3, 102—113, Schulze Qu. ep. 420, zu den Deutungsver- suchen Liden Arm. St. 107, Boisaeq s. v., DeWitt Cl
264 ser : chstufigen *dj-sgico abgehoben  habe; zur Zeit der Kontraktion noch fortwirkende Mouillierung des g lieB  im Kontraktionsergebnis das i vorherrschen, also ui, nicht at entstehn;  auch der Akut des erst bei Aristoteles sicherstehenden dooig zeugt nicht  gegen Kontraktion
265 sver :                                  ',      vargart „Reihe, Trupp“, sowie (mit An- laut su-)                        lit.   sveriit , sverti „wagen“, svarits                       „schwer“, svdras „Wage, Pfund“, preufi.-lit.siwas „Uhrgewicht“. lit.siuVaa, sv\rti „dasUbergew
265 svar :        ',      vargart „Reihe, Trupp“, sowie (mit An- laut su-)                        lit.   sveriit , sverti „wagen“, svarits                       „schwer“, svdras „Wage, Pfund“, preufi.-lit.siwas „Uhrgewicht“. lit.siuVaa, sv\rti „dasUbergewichtbekommen“,            
265 ser :                           702)mit iihnlicher Bedeu-                                                             lat.    serins „ernsthaft, ernstlich                                                                                                                    11    
265 var : sg-x-, wie die von Alexandrinern und Spateren bervorgeholten fjegxgoe, yegxyfiai lehren.                          Alb. avarl „zusammen“ (nach Jokl Wiener Sb. 168, 4 erstarrtes Subst. „Yerkoppelung,                                          Aneinanderreihung", mit Praep. 
266 ser :  gl. duas factiones (Kelt. Gdf. *v arlna, Yendryes He. 33, 473, Pedersen KG. II 660; trotz Pokorny KZ. 45, 360 nicht besser zu uer- „umsehliefien“), ags. tceorn „Trupp. Menge“, russ. verenica „lange Reihe sieh hintereinander bewegender Gegenstande, Zug, Strich 11 (s. o.
266 var :                                   ;                                                11 kiipa „sich zusammenrotten , alb. vargari       Reihe, Trupp“ (s. o.), mit to-                                                                        ,,   Formans ai. vrata-h „Schar, H
267 ser :  (auch von lat. verruca wild ein u-St. vorausgesetzt), aksl. vizclrb .,Gipfel"               vom u- St.), air. ferr „besser“ („*oberer“, Strachan                     (vnchu „oben''                                                  £                                       
267 var :                                                                               267  wie von der s-Erw. anord. vqrr (Gen. varrar) = apr. uarsits ,,Lippe" (siehe Trautmann Apr. 458, Lewy IF. 32, 165, Wood MLK. 1914, S. 4 des SA.).    uer-d       ahd. warga ags. wearte, ano
268 ser : 2, 59, Pedersen KZ. 38, 194). — Uber gr. deigco „hebe“ (Curtius 3 348) s. u. *uer- ..Schnur"; verbale Anwendung fehlt unserer Sippe iiber- haupt; uer(e)dh- „wachsen, steigen“ scheint trotzdem verwandt.   3.       uer-        (vereinzelt eu[e\r-)                  ,,feuch
268 var : gs. uner „Spritzwasser", anord. ver n. ..Fangplatz im Meere, Flut", vqr f. „Kielwassei”‘ (germ, a eher = idg. o als a), vari „Fliissigkeit, Wasser (siehe                                                              11    Falk PBrB. 13, 363, Ark. f. nord. fil. 5, 14):   
269 ser :  eovgyaa), ovgov ..Harn“ (postverbal: von Ehrlich IvZ. 39, 568 freilich auf *fogoiov zuriick- gefiihrt), ovgia ,.ein Wasservogel"   aber mir. frass „Regen“ ist alter fross                                                        ;     (* uros-ta  trotz Pedersen ICG. I 44)
269 var :                                                  v'uti    ange- schlossen sein sollen, erscheint mir bes. wegen lett. atvars als eine iiber- flussige Annalime), und alb. vorbe ..irdener Kochtopf" (Jokl SBAk. Wien 168 I 97).   Bedeutungskern nieht „Feuehtigkeit‘, sondern
269 kochen :                   :   :      Wobl fiir sich stehn (s. auch u. erd- „zerflieBen“), lit. verdu, v'trti „sprudeln, wallen, kochen“, versmS Quelle"', vyrius „Strudel", atvijrs „Gegenstrom am                                         ,,   LT fer\ lett. verdu, vift „quellen, sp
269 brennen : ch wird aueh der weitern Anreihung von arm.                                   ;    rarem .,entziinde“, car ,,entzundet, brennend" (z. B. wieder Scheftelowitz IF. 33, 150; aber idg. it- wird sonst zu arm. g-) und von dt. warm (Lit bei Palk-Torp u. varm; vielmehr zu gVdie
270 ser : . vrnoti ,.deckt hiillend, scliiitzt" usw. ist erwiigenswert unter                                              :    dieser Yoraussetzung konnte auch gr. (jApiro; „Haut, Leder' (ra/.a-vgiyos                                        -     ..Schild tragend”) entweder mit de
270 var :      ;   lautges. 18 mit vertex unter einer Schallwurzel *uer- zu vereinigen).       Strittig     auch   ags.       wantvara ..KaufmannsgutA dt. Ware, die                                                ,    anord. wegen           des hierher gehorigen anorw.aisl. vara „
```


## [2026-10-17T00:05:39.597Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in samovar serious \"wart,\" verruca warble aorta; do echo \"== $w\"; grep -a -n -i -o \"^$w.\\{0,350\\}\" KLN_1971.txt | head -2; grep -a -n -i -o \"^$w.\\{0,300\\}\" SKT.txt | head -2; done 2>/dev/null | cut -c1-450"
}
```


### [2026-10-17T00:05:40.146Z] TOOL RESULT

```
== samovar
211954:samovar, n., a Russian tea um. — Fr. Tatar Sana- 
== serious
218696:serious, adj. — F. sirieux (fem. strieuse), fr. Late 
== wart,
265168:wart, n. — ME., fr. OE. wearte , rel. to OS. warta, 
== verruca
28605:verruca. See verruca and cp. words there re- 
260914:verruca, n., a swart. — L. verruca , ‘excrescence, 
== warble
264924:warble, tr. and intr. v., to sing with trills. — ME. 
264937:warble, n., a small hard tumor on horses or cattle. 
21392:warble,  to  sing  as  a  bird.  (F.  — O.  H. G-)  M.  E.  ttterbcln,  wtt-btUn.  ••  O.  F. icvrW^r  (Burguy),  — M.  H.  G.  ivtrbiUn^  old spelling  of  G.  wirhtlHf  to  whirl,  run  round, warble  (above).
== aorta
16867:aorta, n. — ModL., fr. Gk. AopTifj, ‘the great 
82072:aorta. — Compounded of end-, aorta and -ic. 
791:Aorta.    (Gk.)      Gk.  Afl/m^,    the artery  'rising'  from  the  hcarU  — Gk.1 «r0cu,  to  rise  up;  atipuv,  to  raise.
```


## [2026-10-17T00:05:41.927Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 211954 218696 265168 260914 264937 16867; do sed -n \"${n},$((n+6))p\" KLN_1971.txt | tr '\\n' ' ' | cut -c1-600; echo; echo; done"
}
```


### [2026-10-17T00:05:42.360Z] TOOL RESULT

```
samovar, n., a Russian tea um. — Fr. Tatar Sana-  bar, ‘tea urn’, altered by folk etymology into  Russ, sdmovar, ‘self-boiler’, fr. sdmo, ‘self’, and  varit\ ‘to boil’.   Samoyed, Samoyede, n. and adj., name of a Si-  berian people. — Russ. Sdmoyed , lit. ‘self-  


serious, adj. — F. sirieux (fem. strieuse), fr. Late  L. seridsus, fr. L. ser i us, ‘grave, earnest, serious’,  which is cogn. with Lith. sveriu, sverti , ‘to weigh,  lift’, svariis, ‘heavy’, svdras, ‘pound, balance’,  OE. swaere, swaer, swar, ‘heavy’, OS. swar, ON.  svarr, MDu. swdre, Du. zwaar, OHG. swar(i),  sward, MHG. swxre, swdre, G. schwer , ‘heavy’,  


wart, n. — ME., fr. OE. wearte , rel. to OS. warta,  ON. varta , Swed. v&rta, Dan. vorten, OFris.  warte , Du. wrat, OHG. warza, MHG., G. warze,  ‘wart’, and to OE. wearr, ‘callosity’, and cogn.  with OI. vdr?man-, ‘height, point’, vdrfifthah,  ‘the highest’, L. verruca (for * versuca) ‘ex-  crescence, swelling, wart’, OSlav. vrQchu , ‘sum-  


verruca, n., a swart. — L. verruca , ‘excrescence,  swelling, wart’, which stands for *versiicd and  is cogn. with OE. wearr, ‘callosity, wart’, wearte,  ‘wart’. See wart and cp. verruga, verrugas,  verrucose, adj., warty. — L. verrucosus, fr. ver-  ruca. See prec. word and adj. suff. -ose.  Derivative: verrucose-ness, n.  


warble, n., a small hard tumor on horses or cattle.  — Of uncertain origin.   warble fly, a fly of the family Oestridae. — So called  because its larvae cause warbles. See prec. word,  ward, tr. v., to fend off, protect. — ME. wardien ,  fr. OE. weardian , ‘to keep, guard’, rel. to OS.  


aorta, n. — ModL., fr. Gk. AopTifj, ‘the great  artery’, fr. Aetpetv, ‘to lift, raise up, bear’,  which is rel. to the second element in p.exr]opo<;,  Att. jxex^wpw;, ‘raised from the ground, high*,  of uncertain etymology. Cp. artery and the  second element in endaortic and in meteor. Cp.  also air, ‘atmosphere’.
```


## [2026-10-17T00:05:48.697Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i \"Per\\. b.l.\\b\\|Per\\. b.l.,\\|Per. balu\\|wartö\\|wart\\b\" IEC.txt | cut -c1-300 | head; sed -n 20080,20092p IEC.txt | cut -c1-400; grep -n \"^15[67][0-9]$\" IEC.txt | head"
}
```


### [2026-10-17T00:05:49.262Z] TOOL RESULT

```
814:auk- (2) (?) full-grown, tall’ Lat. cf. -ūca in plant-names festūca, lactūca; verrūca ‘wart’ also qua ‘growth’; Br. cf. éog ‘tipe’; Go auhuma ‘highest’; Li. auklēti
1174:bhaus- “violent, dashing, boisterous; bang, beat, din’ Arm. cf. (variant) z-bawsank ‘amusement’, z-bawsnum (‘amuse os, fr. *bhauK-); Fris. boas "lively, eager; (of weather) bad: OHG bosi ‘paltry, bad'; bosa ‘badness’; Du. boos “angry, malignant, evil’; Nynorsk (archaic Nor- wegian) baus ‘stalwa
1198:bhegh- (variant of bhe&h-, see bhe&h-iKs) Skt. bahyah, adj. ‘outside’; Per. bàz "open: Tokh. A cf. pakür, B pākri *'openly'; ON (CO) bagr ‘chary, awkward"; bagi *opponent , bægi- (*athwart', in cpds.). See next
1201:sv. 7 “strive; shriek; boast; quarrel’; cf. OHG baga ‘battle’; MHG bàc, bàges ‘shriek, din, quarrel, boasting' & Ger. Bager 'restlessness, haste’; bágern ‘badger, nag’; ON bægja ‘oust, thwart, quarrel, force” |
1487:bholgo(n), os, om, à “tiebeam, crosspiece, baulk’. WP II, 181 OHG balco, balcho; OE balc, balca; ON bálkr; OCS blazna ‘thwart’; Pol. blozno ‘crossbar on sleď’; R bólozno ‘plank’; Li. balZienas, mf. 'tiebeam, axletree'; Finn. LW palkka, palkki “bean”
1812:bhrios (2) ‘son, young man. (Semantically related to (1)) Kurd. cf. bire “a stalwart’; Per. barnà, burnā ‘young man’; OE bora ‘son’ and byre, id.; Alb. bir, pl. bij, id.; Go. baür, cons. st. id., cpds. -born; ON burr, pl. rir, id.
1838:bhrtós, á “borne, carried'. Cf. bherð Sk. bhrtáh; Av. boroto; Per. bilà ‘alms’; ON burór (*bearing?, etc.)
1840:(bhru-, see bheru-. Z-gde radical in Per. balwà ‘tumult; OE brymm, m. ‘surf, sea”, prob. also in MHG brunne ‘spring’; ON brunnr, id.)
3105:dhrobh- (2) ‘strike, smash, fragment. Cf. dhrebh- Go. cf. ga-draban “hew out’; ON drofn, pl. drafnir ‘breaker, wave’; cf. also ON -drefjar, cpds. 'spatterings'; Icel. drafa ‘talk thickly’; Norw. cf. drabelig ‘stalwart; OCS drobljo, drobiti ‘shatter; R drobi *lead-shot'; Cz. droby ‘rakings, scra
4101:glist-, glisteros ‘adhesive’. WP I, 620 Mod. Gk. glisterós 'slippery, smooth'; cf. also Gk. glískhros 'gluey; MHG klister ‘glue’; OCS glista ‘tapeworm’; Srb. glista ‘worm’. Isophonic forms are S. Alb. glisht, Alb. gisht ‘finger’ and LGer. kliste ‘thwart on raft?
ueró, ueros, see uer- (1)
(uerógh-, see Supt: U)
uéros, à (1) ‘goodwill, grace, charm, favour, fortune' Skt. varah, m. “treasure”; -varah, cpds.; Av. vàro, m. ‘will, goodwill, gift, grace’; Hom. Gk. ēra, acc. sg. id.; Lat. cf. (?) se-vérus ‘harsh, exacting’; Go. cf. un-wéerei, f. ‘reluctance’; OHG cf. ala-wari, mite-wari, adj. ‘amicable, favourable’; ON vert, adj. ‘snug, peaceful. (Isophonic: Latv. veris ‘deciduous forest; vera, adv. “into notic
uéros, ios (2) “true, right, proper. WP I, 268 Lat. verus, id.; MIr. fir, Ir. fior, id.; Br. W gwir, Cor. gwyr, id.; OBr. guir, id.; OHG war, wāri, id. beside wara, f. (truth, loyalty’: Sl. véra); MHG were, adj. ‘true, loyal’; OCS (and com. Sl.) věra, f. (faith: OHG wara)
uéros (3) ‘watchful; watch" OE waer, adj. *watchful'; Latv. cf. vera, adv. ‘into notice’; cf. MHG o-gde ge-war, adj. *aware'; f. “awareness”
1521
(uerpó, see Supt: U and cf. urpo (2), urpol-; uerpos, à, see uorp- (2))
uers- (1) ‘droplet, sprinkling, shower, dew, rain’. WP I, 269. Cf. uersó (1) Skt. varsáh, -Á, Am. mfn. “rain, shower’; Av. cf. varo&-, v. ‘sprinkle’; Per. baris “rain”; Hitt. warsas (queried), id.; Gk. hérse, hérsé, f. (1) ‘dew’; Olr. cf. feraim, v. ‘pour, rain? beside Mir, fear-thuinn, Ir. fearthain, vbl. n. f. ‘raining’ (vocalism obscure in Olr. fross, f. “shower, downpour’, fr. *urost-?); Li. c
uers- (2) ‘young of animal’. Cf. uerks- and uersën-. WP I, 269. (Skt. urs-) Skt. cf. (z-gde) vrsah, m. ‘young male, esp. bullock’; Gk. hérse, hérse, f. (2) “young ani- mal, lamb”; cf. also (?) Hes. errás, usu. érraos, m. (cram, wild boar’. A synthetic cpd.?); Lat. verres, gs: verris, m. ‘boar’; Li. cf. versis, gs: -io, m. ‘calf’; Latv. versis & véersens, m. “ox; Finn. LW varsa (ffoal, fr. Iranian 
uers- (3) 'growth, hard skin' Lat. cf. verr-üca, f. ‘wart; hillock’; OE wearr, m. *callouse'; OFris. cf. (?) wersene ‘wrinkle’
uersen- ‘male animal". Cf. uers- (2), uerks-. WP I, 269 Av. varo$no, adj. ‘male’; Ionic Gk. érsen, gs: -enos, adj. id.; Latv. vérséns, m. “ox; steer’
uersi- (?). Cf. WP I, 267 Skt. cf. vargi-sthah ‘highest’; Per. bi$, adj. “much, more’; Olr. ferr, Ir. fearr, adj. “better”. (ISophonic: Go. waírsiza, OHG wirsiro, ON verri ‘worse’; G wirs, wirsch “bad, raging’; Du. cf. wars 'averse") (!)
uersð (-ið, -aio) (1) ‘shed, sprinkle, pour, gush, rain’. Cf. uers- (1). WP I, 269 Skt. várgati, 3s. ‘shower, bedew’; pp: vrstah; cf. vrstíh, f. ran: Av. varo&-, v. ‘sprinkle; in- seminate'; Gk. eráo, v. (pour, spew forth’; cf. hérse, f. ‘dew’; herseeis, adj. ((bedewed'. Cf. also árdo, v. ‘sprinkle, water’, if from *ursdo); It. Fr. versare, verser, v. (pour. Not in Lat. in this sense); Ir. (?) fer
```


## [2026-10-17T00:05:51.513Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^uord\\|^uorð\\|^uórd\\|^uord\" IEC.txt | cut -c1-500 | head"
}
```


### [2026-10-17T00:05:51.936Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:53.956Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^u.rd\" IEC.txt | cut -c1-500 | head; grep -n -a \"frog\" IEC.txt | grep -i \"wart\\|Per\" | cut -c1-500 | head -5"
}
```


### [2026-10-17T00:05:54.339Z] TOOL RESULT

```
4000:gi20, ið (1) “touch, hit, kick Oss. gezun, pp. gist ‘touch’; Arm. cf. kic, kick, s. Check. fr. *gigsK-); ME kicken (kick. G kicken perh. fr. Eng.); Du. cf. kikker, kik- vors ‘frog’ next, or guiĝ- (?) Arm. kcem, kčem, kcanem ‘prick, sting, burn, bite’; kic, gs kco, s. id.; (OCS go Zigati, beside Zego, žešti “burn, kindle’, fr. *gueg-?). Per. gazam (*burn'. Vocalism ambig.)
5051:ghükos (ghuk-) ‘hoot, whoop’ Skt. ghükah ‘owl; Per. yük ‘frog; R gik ‘whoop’; gikať, v. id.; Cz. (*-u-) hek ‘groan’ beside hykat ‘bray’; cf. R variant zyk (‘dim fr.
6902:kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘da
19824:uégo- (1), element of the following (?) Av. cf. vazaya, f. ‘lizard’; Per. vazaq, s. ‘frog’; Li. véZys, m. ‘crab, crayfish’; veZlys, m. “tor- toise’; Latv. vēzis, s. ‘crab’. (Oss. isophone (?) wázal, adj. = ‘cool, cold")
```


## [2026-10-17T00:05:57.659Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/سماور/\" --note \"page 547, Mo'in s.v. samavar\" ; f=$(tail -1 data/verification/sources/web/index.jsonl | python3 -c \"import json,sys;d=json.loads(sys.stdin.read());print(d['status'],d['file'])\"); echo $f; grep -n \"معین\\|روس\" $(echo $f|cut -d' ' -f2) | head -8"
}
```


### [2026-10-17T00:05:59.355Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0d34a9d589d2e5f3.txt
200 data/verification/sources/web/0d34a9d589d2e5f3.txt
20: سماور. [ س َ وَ ] ( روسی ، اِ ) یک قسم ابزاری فلزی جهت جوش آوردن آب که آتش خانه را در میانش قرار داده اند.
21:( ناظم الاطباء ). خودجوش. آلتی فلزی که در درون آن خانه ای تعبیه شده و برای جوش آوردن آن جهت چای و غیره بکار رود. در بالای آن قوری چای را جای دهند تا دم کشد. ( فرهنگ فارسی معین ). 
40: سماور واژه ای روسی �самовар� به معنای خودجوش یا وسیله ای که خودش آب را می جوشاند می باشد . 
41:سماور در اواخر دوره صفوی و سپس به طور گسترده تر در دوران قاجار از روسیه وارد ایران شد. 
42:نخستین سماورها از روسیه به ایران وارد شدند و در ابتدا در میان درباریان و اعیان مورد استفاده قرار گرفتند 
50: سماور ریشه در زبان ترکی دارد از سمت ترکان تاتار روسیه استفاده میشده چون منبع تولید این سماور نیز شهرهای ترک نشین روسیه است و همچنین مهد سماور باکو و آذربایجان است.
53: سمه به روسی خود است و ور/وریت= جوش
55: سَماوَر ( به روسی: Самовар )
```


## [2026-10-17T00:06:02.768Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^خوار\\|^ خوار\\|خوار ۔\\|خوار -\\|خوار ـ\" BQT_v2_pages.txt BQT_v2.txt | head; grep -n \"^خوار\\|خوار (\" incoming/ARY/ARY_pages.txt | head -3"
}
```


### [2026-10-17T00:06:03.263Z] TOOL RESULT

```
BQT_v2.txt:173:خوارزمی . ( فرهنگ عربی بفارسی) با اضافات باهتمام وزماو۵02 ¥ . 6 . [ .لبسيك 
BQT_v2.txt:4176:خوار را نیز گفته‌اند ۰ 
BQT_v2.txt:13866:خوارزمی است ۰ » از بیت ذیل عجدی مروزی برمیابد که درلهجةٌ مرولیز مممول بوده : 
BQT_v2.txt:21238:خوارباشد ۴ ۱ 
BQT_v2.txt:23162:خوار کادی - بانانی مسوله بروزن 
BQT_v2.txt:23182:خواری خوار » بائانی معدوله بر 
BQT_v2.txt:23185:خواری گردن ‏ کنابه از دشنام 
BQT_v2.txt:23188:خوار - بفتح اول بر وزن بماز » 
BQT_v2.txt:23827:خوارخوارآب همی پالاید ‏ آن خورآ به باشد , عنصری (بلخی) گفت : 
BQT_v2.txt:48895:ز نهار خوار - باخای شله دار
```


## [2026-10-17T00:06:05.479Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23140,23200p BQT_v2.txt | grep -n \"خوار\\|خوا\\|xv\\|x\\\"\\|په\\|اوستا\\|پهلوی\" | head -30"
}
```


### [2026-10-17T00:06:05.831Z] TOOL RESULT

```
8:خوردنی باشد "۳ وبعربی | واز کاو را خوانند ۰ 
18:کارزار ۰ ستمکار وخواری کننده را کوبند ® . 
23:خوار کادی - بانانی مسوله بروزن 
28:خوا ده = بانانی ممدوله بروزن چاره» 
34:خوازه 
43:خواری خوار » بائانی معدوله بر 
44:وزن ماهی خوار » دشنام شنونده را کوبند . 
46:خواری گردن ‏ کنابه از دشنام 
49:خوار - بفتح اول بر وزن بماز » 
54:بمعنی | فرین - وخواهش باشد٩۱-‏ ومطلق چوب
```


## [2026-10-17T00:06:34.217Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"aeír\\|aeir\\|aort\" IEC.txt | cut -c1-400 | head -5; grep -n -a -i \"swer\\|warze\\|wart\" SYN.txt | head -3; grep -n -a \"SERIOUS\\|ARTERY\\|AORTA\" AHD_watkins1985.txt | head -3"
}
```


### [2026-10-17T00:06:34.489Z] TOOL RESULT

```
19677:refd. to aeiro) (?); OCS cf. véverica, f. (“squir- rel, weasel, stoat’ etc.) beside Li. vovere, f., voveris, f. ('squirrel', but cf. uiuera); OLi. vaivaras, m. ((squirrel', vocalism obscure); Latv. vaivari, mpl. ‘marsh rosemary’ beside vaveraji, id.; Li. vaivara, f. 'speedwell"; Latv. vāvere, f. (squirrel, vocal. as Li.). (Radical form *uaiu-, or *uoig-, in Li. vaivó-rykste ‘rainbow’, cf. ry
72:The history of ideas is embodied in the history of the words used to ex- press them. Whether the ‘idea’, ‘notion’, ‘concept’, or ‘mental image’ (I shall commonly use the innocuous ‘notion’) is, as many believe, only an abstraction (the concrete object or the uttered and heard sound of the word being the only realities), or whether it corresponds to some reality in the brain (as an eminent neurologist has assured me he thinks quite tenable), need not concern us. For its close dependence upon its verbal ex- pression is beyond dispute. It is a pattern of reaction answering to a given stimulus, which (apart from the actual perception of an individual concrete object, which also suggests the general notion) is normally the word or group of words. It is this pattern of reaction which constitutes the mean- ing of a word. A word means what it refers to, in a given context or situa- tion. The meaning of a word as a whole may ne a composite of various allied applications.
109:Words not only change in meaning, they may be lost outright, displaced by others. Why? There is no one answer. Of the various alleged causes, each has some validity as a factor but is likely to be exaggerated by one whose attention is riveted on it in a hunt for examples. The existence of homonyms may favor the loss of one of them, as the verb let ‘hinder’ (cf. the noun in the old phrase let or hindrance and let in tennis) vs. let ‘permit’. Phonetic changes which have left little body to the word no doubt favored the partial displacement of Lat. dare, diés, apis, avis by donare, diurnum, apicula, avicellus in the evolution of the Romance words. But the great number of homonyms in English, and monosyllabic at that, shows that neither of these factors is a compelling cause.
129:The principal Indo-European languages are covered. Some of the minor Indo-European languages, as Albanian, Armenian, and all modern forms of Indie and Iranian, are excluded from the survey, except for incidental men- tion, since to include them systematically would increase the labor out of all proportion to the results added. Danish, with which Norwegian agrees in large measure, and Swedish are taken as representative of the modern Scandinavian languages, though thus one may miss certain interesting divergences in word preference between Danish and Norwegian and the more frequent persistence of the Old Norse words in Modern Icelandic. Of the Romance languages, Portuguese is omitted as generally going with Span- ish in vocabulary, though here, too, occasional differences are missed or only incidentally noted. There is no room to follow out the chronological and geographical distribution of Romance words on the elaborate scale which is customary and fitting in monographs in that field. Of the impor- tant Slavic languages, the (modern) Bulgarian is omitted, the words general- ly going with those quoted under either Church Slavic or Serbo-Croatian. Under Church Slavie are given preference the genuine Old Church Slavic (Old Bulgarian) words, especially from the Gospels, where such are quotable, but not to the exclusion of others which are (in part accidentally) quotable only from later times. The latter are sometimes marked “late”, but prob- ably without consistency. As is well known, Miklosich’s Lexicon is full of late forms that are merely Serbian, etc. in Church Slavic dress, and con- versely fails sometimes to give early quotations for words occurring in the best records. In this regard, Jagié’s Entstehungsgeschichte der kirchen- slavischen Sprache, with its indexes, is of inestimable value, though even this at times fails to answer the questions that arise. Since the quotable Old Irish vocabulary is too limited to serve, Old and Middle Irish forms are generally given without distinction and both marked as Ir. (as in Peder- sen’s Vergleichende Grammatik der keltischen Sprachen and elsewhere), while the modern forms are marked NIr. But under Welsh and Breton are given the modern forms, with special designation of the Old or Middle. Cornish words, which generally go with the Breton or Welsh or both, are not included in the list but often in the discussion, especially those quotable from the old Latin-Cornish vocabulary.
1052:swer-'. To speak, talk. O-grade form *swor- in: a. Ger- manic *swarjan in Old English swerian, to swear, pro- claim: SWEAR; b. Germanic “*and-swar6, “a swearing against,” “rebuttal” (*andi-, against; see ant-), in Old English andswaru, answer: ANSWER. [Pok. 1. swer- 1049.] swer-2. To buzz, whisper. Imitative root. I. O-grade form *swor-. 1. Suffixed form *swor-mo- in Germanic *swar- maz in Old English swearm, swarm: SWARM. 2. Germanic *swar- in Dutch zwirrelen, to whirl, akin to the Low German source of Middle English swyrl, eddy: SWIRL. II. Zero-grade form *sur-. 1. Suffixed form *sur-do- perhaps in: a. Latin surdus, deaf, mute: SORDINO, SOUR- DINE, SURD; b. Latin absurdus, discordant, away from the right sound, harsh (ab-, away; see apo-): ABSURD. 2. Reduplicated expressive form *su-surr- in Latin susur- rus, whisper: SUSURRATION. [Pok. 2. swer- 1049.] swer-3, Post, rod. Suffixed zero-grade form *sur-o- in Latin surus, branch: SURCULOSE. [Pok. 3. suer- 1050.] swer-4. To cut, pierce. Germanic *swerdam in Old Eng- lish sweord, sword, sword: sworD. [Pok. 4. suer- 1050.] swer-5. Also ser-. To lift, hang on the scale; heavy. Variant *ser- in suffixed lengthened-grade form *sér-yo- in Latin sérius, serious, grave: SERIOUS.
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1252:AORTA wer-2 APERIENT wer-5 APERITIF wer-5 APERTURE wer-5 APEX ap-! APHELION sawel- APHONIA bha-2 APLANATIC pele-2 APLOMB plumbum APNEA pneu-
```


## [2026-10-17T00:09:02.248Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-547.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nAHDq=\"https://ahdictionary.com/word/search.html?q=\"\nPOKf=\"POK_full.txt (IED dump)\"\ndef rc(ref,st,note): return {\"ref\":ref,\"status\":st,\"note\":note}\ndef cs(src,where,st,note): return {\"src\":src,\"where\":where,\"stance\":st,\"note\":note}\n\ne0={\"entry\":0,\"root\":\"Wer 5\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *wer- 'to burn' (Pokorny 12. uer- 1166; AHD wer-7 'to burn'; Wiktionary *wōr- 'to burn' for Proto-Slavic *variti)\",\n\"note\":\"Pokorny 1166 (12. uer- 'to burn': Arm. varem 'set on fire', OCS varъ 'heat', variti 'cook', Hitt. war- 'burn') and Watkins/AHD wer-7 ('Suffixed lengthened o-grade (causative) form *wōr-yo- in Russian varit', to boil: SAMOVAR') match root, label and gloss. Nourai's numbering 'Wer 5' is his own; Pokorny numbers it 12, AHD 7.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *wer- «سوختن» (پوکورنی ۱۱۶۶، شمارهٔ ۱۲؛ در فرهنگ امریکن هریتیج wer-7) است که در اسلاوی با بالاندگی o به صورت سببی *wōr-eye- «جوشاندن، پختن» درآمده و فعل روسی варить (varit') از آن است. ریشه، زبان و معنای نمودار نورایی درست است؛ تنها شمارهٔ «۵» شمارگذاری خود نورایی است.\",\n\"sources\":[W+\"Reconstruction:Proto-Slavic/variti\",W+\"варить\",AHDq+\"samovar\"],\n\"ref_check\":[rc(\"POK:1166\",\"supports\",\"POK_full.txt l.91293: 'Root / lemma: uer-12 ... Meaning: to burn ... Old Church Slavic varъ 'heat', variti 'cook' ... Hittite uar- 'burn' ... Page(s): 1166'.\")],\n\"consulted\":[\n cs(\"AHD\",\"Watkins 1985, s.v. wer-7 (AHD_watkins1985.txt l.1151)\",\"supports\",\"'wer-7. To burn. Suffixed lengthened o-grade (causative) form *wōr-yo- in Russian varit', to boil: SAMOVAR. [Pok. 12. wer- 1166.]'\"),\n cs(\"WLD\",\"Bd. I p. 269 (WLD_Bd1_pages.txt leaf 278)\",\"partial\",\"WP I 269 (the page Pokorny cites) discusses arm. varem 'entzünde', var 'brennend' and dt. warm under a uer- root; Slavic variti is not legible in the OCR excerpt.\"),\n cs(\"IEC\",\"grep 'variti|varit' IEC.txt\",\"silent\",\"no entry for the Slavic 'boil' verb found in Mann's OCR.\")],\n\"nodes\":[\n {\"id\":1,\"lang\":\"Russian\",\"words\":\"varit; samo-variti, samo-war\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Russian варить (varít', 'to boil, cook') < Proto-Slavic *variti < Balto-Slavic *wārīˀtei, a causative/iterative with lengthened o-grade *wōr-eye- from PIE *wer- 'burn' (OCS variti, varъ 'heat'). самова́р (samovár, 'samovar', 18th c.) = само- 'self' + deverbal -вар 'boiler' from варить, i.e. 'self-boiler' (Wiktionary, AHD). Nourai's 'samo-variti' is an analytic gloss, not an attested verb. Klein alone treats samovar as a folk-etymological reshaping of a Tatar 'samabar' 'tea urn'; Wiktionary and AHD (and the descendant lists, where the Turkic forms are loans from Russian) take it as a native Russian compound, which is the prevailing view.\",\n  \"derivation_fa\":\"فعل روسی варить (varit') «جوشاندن، پختن» از اسلاوی آغازین *variti و آن از ریشهٔ هندواروپایی *wer- «سوختن» با بالاندگی o (ساخت سببی *wōr-eye-) است. «سماور» در روسی (самовар) ترکیبی است از само- «خود» و -вар «جوشاننده» از همین فعل، یعنی «خودجوش». ارنست کلاین آن را دگرگون‌شدهٔ واژه‌ای تاتاری به شیوهٔ ریشه‌شناسی عامیانه می‌داند، اما ویکی‌واژه و امریکن هریتیج آن را ترکیب خود روسی می‌شمارند و صورت‌های ترکی را وام از روسی؛ ادعای نورایی درست است (صورت samo-variti تنها تحلیل اوست، نه فعلی موجود).\",\n  \"sources\":[W+\"самовар\",W+\"варить\",W+\"Reconstruction:Proto-Slavic/variti\",AHDq+\"samovar\"],\n  \"ref_check\":[rc(\"POK:1166\",\"supports\",\"uer-12 'to burn': 'Old Church Slavic varъ 'heat', variti 'cook'' (POK_full.txt l.91293-91310).\"),\n               rc(\"AHD:1148\",\"supports\",\"AHD 1985 wer-7 'To burn ... Russian varit', to boil: SAMOVAR' (AHD_watkins1985.txt l.1151); the 1976 page itself not accessible but the same root entry.\")],\n  \"consulted\":[cs(\"KLN\",\"1971 ed., s.v. samovar (KLN_1971.txt l.211954)\",\"partial\",\"'samovar ... Fr. Tatar Sanabar [samabar], 'tea urn', altered by folk etymology into Russ. sámovar, 'self-boiler', fr. sámo, 'self', and varit', 'to boil'' — accepts the self+boil analysis only as folk etymology.\"),\n               cs(\"AHD\",\"Watkins 1985 index (l.2211)\",\"supports\",\"'SAMOVAR sem-1, wer-7' (samo- under sem-1, -var under wer-7).\"),\n               cs(\"SKT\",\"grep '^samovar' SKT.txt\",\"silent\",\"no entry.\")]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"samâvar\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Persian سماور samâvar is a 19th-century (Qajar-era) loan from Russian самовар 'self-boiler' (samo- 'self' + var- 'boil'), arriving with the Russian-made urn itself; Mo'in marks it (روسی) 'Russian' and glosses خودجوش. Russian unstressed -o- in sam(o)- is rendered -â- as in Persian practice of the time.\",\n  \"derivation_fa\":\"«سماور» وام‌واژه‌ای روسی است (самовар، «خودجوش») که در دورهٔ قاجار همراه خود این ابزار از روسیه به ایران آمد؛ معین و دهخدا آن را «روسی» و به معنای «خودجوش» آورده‌اند. جزء دوم آن از فعل روسی варить «جوشاندن» و سرانجام از ریشهٔ هندواروپایی *wer- «سوختن» است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"سماور\",\"https://abadis.ir/fatofa/سماور/\"],\n  \"ref_check\":[rc(\"MON:1918\",\"supports\",\"Mo'in's entry as quoted on abadis.ir (Dehkhoda block): 'سماور ... ( روسی ، اِ ) ... خودجوش ... ( فرهنگ فارسی معین )'. The printed page 1918 cannot be mapped online.\")],\n  \"consulted\":[cs(\"ARY\",\"grep 'سماور' ARY_pages.txt\",\"silent\",\"no entry (Aryanpur covers only inherited IE words).\"),\n               cs(\"BQT\",\"grep 'سماور' BQT_v2_pages.txt\",\"silent\",\"not in Borhan-e Qate' (word post-dates the dictionary).\"),\n               cs(\"KLN\",\"s.v. samovar\",\"partial\",\"Klein gives Russian sámovar 'self-boiler' (as folk etymology of Tatar samabar); Persian not mentioned.\")]}\n]}\n\ne1={\"entry\":1,\"root\":\"Wer 6, Swer\",\"verdict\":\"plausible\",\n\"modern_form\":\"PIE *(h₂)wer- 'to bind, hang up, raise' (Pokorny 1. uer- 1150, with s-mobile *swer- 'to weigh, heavy'); AHD splits it into wer-2 'to raise, lift, hold suspended' and swer-5 'to lift, hang on the scale; heavy'\",\n\"note\":\"Pokorny 1150-1151 (1. uer-, also suer- 'to bind, attach'; Greek aeirō, aortē, artēria under it; D. 's mobile suer-': Lith. sverti 'weigh', svarùs 'heavy', Gothic swers; 'doubtful ... Latin serius') is exactly Nourai's composite root, and WP I 263-265 has the same grouping. Watkins/AHD separates the Greek 'raise' root (wer-2) from the 'heavy' root (swer-5), and Wiktionary calls the 'raise' vs 'bind' connection unclear. The root is therefore Pokorny's construct, accepted only in part today. The Iranian members come from Mann alone and do not hold (see nodes 1-2).\",\n\"note_fa\":\"ریشهٔ ترکیبی نورایی همان ریشهٔ ۱. uer- (با s متحرک: suer-) در پوکورنی (ص ۱۱۵۰) است: «بستن، آویختن، برداشتن» و نیز «وزن کردن، سنگین». پوکورنی و والده-پوکورنی یونانی aeirō و aortē و لیتوانیایی sverti «وزن کردن» و (با تردید) لاتین sērius را زیر یک ریشه گرد آورده‌اند، اما واتکینز (امریکن هریتیج) آن را به دو ریشهٔ جدا بخش کرده است: wer-2 «برداشتن، آویختن» و swer-5 «سنگین». پس ریشه با احتیاط پذیرفتنی است؛ شاخهٔ ایرانی آن تنها از مان است و پذیرفته نیست.\",\n\"sources\":[W+\"ἀείρω\",W+\"serius\",AHDq+\"serious\",AHDq+\"aorta\"],\n\"ref_check\":[rc(\"POK:1150\",\"supports\",\"POK_full.txt l.91335: 'uer-1, also suer- ... to bind, to attach ... Gr. aeirō ... aortē 'Aorta' ... D. with s mobile: suer- ... Lithuanian sveriu sverti 'wägen' ... svarus 'heavy' ... doubtful ... Latin serius 'ernst'. Page(s): 1150-1151'.\"),\n             rc(\"IEC:1347\",\"supports\",\"IEC.txt l.17990 (cols. 1347-1348): suer- '... Li. sveriù, sverti ... Latv. sveru, svert 'weigh' ... Go. swērs 'honoured', lit. 'weighty' ... OE swǣr 'heavy'' with Gk. hérma 'pendant'.\"),\n             rc(\"WLD1:264\",\"supports\",\"WLD Bd. I pp. 263-265 (WLD_Bd1_pages.txt): uer- 'Schnur, aufreihen, anbinden' with gr. aeirō on 264 and on 265 '(mit Anlaut su-) lit. sveriù, sverti „wägen“, svarùs „schwer“ ... lat. serius „ernsthaft“'.\")],\n\"consulted\":[cs(\"AHD\",\"Watkins 1985 wer-2 and swer-5 (l.1144, 1052)\",\"partial\",\"'wer-2. To raise, lift, hold suspended ... Greek aeirein ... artēria' and separately 'swer-5. Also ser-. To lift, hang on the scale; heavy ... Latin sērius' — same material split into two roots.\"),\n             cs(\"IEC\",\"l.17992\",\"partial\",\"Mann lists Av. xwairis 'abuse, blame' also under a different root suer- (3) 'harm, hurt' — internal inconsistency for the Iranian branch.\")],\n\"nodes\":[\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"xwâiris\",\"verdict\":\"unverified\",\n  \"derivation\":\"Mann (IEC 1347-1348) cites 'Av. xwairis, f. blame' as a long-grade derivative of *swer- 'weigh', but the same form also appears under his suer- (3) 'harm, hurt, corrupt' (Av. xwar- 'blame, injure'). The gloss 'weight' in the chart is not in Mann. Pokorny, Walde-Pokorny and AHD give no Iranian reflex of *swer- 'heavy'. The Bartholomae OCR is too poor in the xᵛ- section to check whether an Avestan noun xᵛāiri-/xᵛairi- exists. No independent confirmation of either the form or the link to 'heavy'.\",\n  \"derivation_fa\":\"صورت اوستایی xwāiris «نکوهش» را تنها مان (ص ۱۳۴۷-۱۳۴۸) آورده و آن را از بالاندگی بلند ریشهٔ *swer- «سنگین» دانسته است، ولی همو همین صورت را زیر ریشهٔ دیگری به معنای «آزردن، نکوهیدن» نیز آورده است. معنای «وزن» در منابع دیده نشد و پوکورنی و امریکن هریتیج هیچ بازماندهٔ ایرانی برای این ریشه نمی‌آورند. متن اسکن‌شدهٔ بارتولومه در بخش xᵛ- خواناییِ کافی برای بررسی ندارد. بنابراین این گره نه تأیید شد و نه رد.\",\n  \"sources\":[],\n  \"ref_check\":[rc(\"IEC:1347\",\"supports\",\"IEC.txt l.17990: '(Long-gde in) Av. xwairis, f. 'blame'' under suer- 'weigh'; but l.17992 lists 'xwairis, s. 'abuse, blame'' under suer- (3) 'harm'.\")],\n  \"consulted\":[cs(\"BRT\",\"grep 'x.airi|Tadel' BRT.txt\",\"silent\",\"OCR of the xᵛ- columns unusable (no hit for xᵛairi-/'Tadel').\"),\n               cs(\"POK\",\"1. uer- 1150-1151\",\"silent\",\"no Iranian material under uer-/suer- 'bind, weigh'.\"),\n               cs(\"AHD\",\"swer-5\",\"silent\",\"only Latin sērius cited.\")]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"xwâr\",\"verdict\":\"disputed\",\n  \"derivation\":\"Persian خوار xᵛār 'mean, abject, despised' < MP xwār [hwʾl] 'light, easy; mean, abject' (MacKenzie). Horn no. 496 and Hübschmann (§108) equate it with Av. xᵛāθra- 'well-being, ease, comfort' (Geldner, Darmesteter): Old Iranian *hu-āθra- > MP xwār (θr > r), originally 'easy'; Horn notes that the sense 'low, despicable' first appears in New Persian (easy > cheap > base). Wiktionary (after ESIJa I 324) gives the same *āθra- connection. Nyberg suggests instead *hu-vāra- 'swinish' for a homonym x'ār 'contemptible'. No source except Mann derives it from *swer- 'heavy'; the 'heavy' > 'indigent' semantics are not supported. The chart's own note ('See root Ěter') points to the āθra- derivation, which is the one modern scholarship follows.\",\n  \"derivation_fa\":\"«خوار» از فارسی میانهٔ xwār «آسان، سبک؛ پست، زبون» (مکنزی) است. هرن (شمارهٔ ۴۹۶) و هوبشمان آن را با اوستایی xᵛāθra- «آسایش، خوشی» یکی می‌دانند (از ایرانی باستان *hu-āθra-، با تحول θr به r در فارسی میانه). معنای نخستین «آسان» بوده و به گفتهٔ هرن معنای «پست و زبون» تنها در فارسی نو پدید آمده است. ویکی‌واژه نیز همین پیوند را با *āθra- می‌آورد، و نیبرگ برای خوارِ «پست» احتمال *hu-vāra- را مطرح کرده است. پیوند آن با ریشهٔ *swer- «سنگین» تنها از مان است و پذیرفته نیست؛ یادداشت خود نورایی که به ریشهٔ «Ěter» ارجاع می‌دهد به ریشه‌شناسی درست‌تر نزدیک است.\",\n  \"sources\":[W+\"خوار\",\"https://vajehyab.com/moein/خوار\"],\n  \"ref_check\":[rc(\"IEC:1348\",\"supports\",\"IEC.txt l.17990 (col. 1348): 'Per. xwar, adj. 'indigent'' under suer- 'weigh' — Mann does say what the arrow says, but stands alone (see consulted).\")],\n  \"consulted\":[cs(\"HRN\",\"no. 496, p. 110 (HRN.txt leaf 131)\",\"contradicts\",\"'496. xᵛār 'leicht, gerade; niedrig, verächtlich' ... aw. xᵛāθra- ... phlv. xᵛār, nur in der Bedeutung 'leicht' ... Die Bedeutung 'niedrig, verächtlich' ist erst neupersisch.'\"),\n               cs(\"HUB\",\"§108, p. ~217 (HUB.txt leaf 227)\",\"contradicts\",\"'xᵛār 'leicht' = zd. xᵛāθra-' (ap. uv/huv > np. xᵛ).\"),\n               cs(\"PHD\",\"p. 95 s.v. xwār (PHD.txt l.663)\",\"partial\",\"'²xwār [hwʾl | M xwr, N ~] light, easy; mean, abject.' — confirms the MP form and both senses, no etymology.\"),\n               cs(\"NYB\",\"Glossary s.v. x'ār (NYB_vol2_glossary.txt l.4325)\",\"contradicts\",\"'²x'ār [hwʾl] contemptible ... Bal. whār 'dirty, foul, spoilt' leads us back to an original *hu-vāra- 'swinish' ... NP xᵛār'; ¹x'ār 'easy' separately (x'ārēh 'bliss').\"),\n               cs(\"MON\",\"vajehyab moein s.v. خوار\",\"partial\",\"'(خا) [ په . ] (ص .) 1 - آسان ، سهل . 2 - پست ، زبون' — Pahlavi origin, senses 'easy' and 'base'; no IE root.\"),\n               cs(\"BQT\",\"grep 'خوار' BQT_v2.txt (l.23188 region)\",\"silent\",\"Mo'in's footnote for the adjective not recoverable from the OCR.\"),\n               cs(\"ARY\",\"grep 'خوار' ARY_pages.txt\",\"silent\",\"no headword خوار in Aryanpur.\")]},\n {\"id\":3,\"lang\":\"Latin\",\"words\":\"sěrius\",\"verdict\":\"plausible\",\n  \"derivation\":\"Latin sērius 'grave, earnest' is derived by Watkins/AHD (swer-5) from a variant *sēr-yo- (lengthened grade of *ser-, beside *swer-), and Wiktionary also traces it to *swer- 'heavy', with cognates Lith. sverti 'to weigh', Goth. swērs 'honoured', OE swǣr 'heavy'. Pokorny lists it only as 'doubtful', and the loss of -w- (expected *swēr- > Lat. *sēr- after s-?) is unexplained, so the derivation is accepted by some, not all. The book prints 'sěrius' with Nourai's breve-style vowel mark (Latin has long ē); the extraction is faithful.\",\n  \"derivation_fa\":\"لاتین sērius «جدی، سنگین» را واتکینز از صورت *sēr-yo- (گونه‌ای از *swer- «سنگین») می‌داند و ویکی‌واژه هم آن را به *swer- می‌رساند؛ هم‌ریشه‌های آن لیتوانیایی sverti «وزن کردن» و انگلیسی کهن swǣr «سنگین» است. پوکورنی این پیوند را «مشکوک» خوانده، زیرا افتادن w پس از s توضیح روشنی ندارد. پس با احتیاط پذیرفتنی است. نشانهٔ روی e در کتاب شیوهٔ نگارش نورایی است و خطای خوانش نیست.\",\n  \"sources\":[W+\"serius\",AHDq+\"serious\"],\n  \"ref_check\":[rc(\"AHD:1549\",\"supports\",\"AHD 1985 swer-5 (AHD_watkins1985.txt l.1052): 'Variant *ser- in suffixed lengthened-grade form *sēr-yo- in Latin sērius, serious, grave: SERIOUS.'\")],\n  \"consulted\":[cs(\"POK\",\"1150-1151 (POK_full.txt l.91400)\",\"partial\",\"'doubtful gr. ἕρμα ... and Latin serius 'ernst'' under suer-.\"),\n               cs(\"WLD\",\"Bd. I p. 265\",\"supports\",\"'lat. serius „ernsthaft, ernstlich“' grouped with lit. sverti, svarùs.\"),\n               cs(\"KLN\",\"1971 s.v. serious (l.218696)\",\"supports\",\"'L. sērius ... which is cogn. with Lith. sveriu, sverti, 'to weigh, lift', svarùs, 'heavy' ... OE swǣre ... 'heavy''.\"),\n               cs(\"IEC\",\"l.17990\",\"silent\",\"Latin sērius not listed under suer-.\")]},\n {\"id\":4,\"lang\":\"English\",\"words\":\"serious\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English serious (15th c.) < Middle English seryows < Old French serieux < Late/Medieval Latin sēriōsus, an -ōsus extension of Latin sērius 'grave, earnest'. The chain is uncontroversial; its ultimate root connection is as plausible as node 3.\",\n  \"derivation_fa\":\"انگلیسی serious از انگلیسی میانه seryows، از فرانسوی کهن serieux و از لاتین متأخر sēriōsus است که با پسوند -ōsus از لاتین sērius «جدی» ساخته شده است. این زنجیره قطعی است و پیوند نهایی آن با ریشه به اندازهٔ گرهٔ لاتین پذیرفتنی است.\",\n  \"sources\":[AHDq+\"serious\",W+\"serius\"],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"AHD online s.v. serious: '[Middle English, from Old French serieux, from Late Latin sēriōsus, from Latin sērius.]'; 1985 appendix lists SERIOUS under swer-5.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. serious\",\"supports\",\"'F. sérieux ... fr. Late L. sēriōsus, fr. L. sērius'.\"),\n               cs(\"SKT\",\"grep '^serious' SKT.txt\",\"silent\",\"no line-initial entry found in OCR.\")]},\n {\"id\":5,\"lang\":\"Greek\",\"words\":\"aeirein; arteria\",\"verdict\":\"plausible\",\n  \"derivation\":\"Greek ἀείρω (aeírō, Attic αἴρω) 'lift, raise; hang up, bind together' < Proto-Hellenic *awérjō < PIE *h₂wér-ye-ti (Wiktionary; AHD wer-2 'to raise, lift, hold suspended'; Pokorny 1. uer- 'bind'). ἀρτηρία (artēría 'windpipe; artery') is a supposed contraction of *aortēría (cf. ἀορτήρ 'strap'), so from the same verb, and ἀορτή (aortḗ) is a derivative *h₂wortéh₂. Wiktionary says the relation between 'raise' and 'bind/enclose' is unclear, and the link of aeirō with the *swer- 'heavy' material is only Pokorny's. So the words are real and belong to aeirō, but the root grouping is contested. Nourai's note that 'AHD is not sure' matches the hedged treatment in the dictionaries.\",\n  \"derivation_fa\":\"یونانی ἀείρω (aeirō) «برداشتن، بالا بردن؛ آویختن، به هم بستن» از یونانی آغازین *awérjō و هندواروپایی *h₂wer- است. ἀρτηρία (artēria) «نای؛ سرخرگ» را کوتاه‌شدهٔ *aortēria می‌دانند و ἀορτή (aortē) نیز از همین فعل است. پیوند معنای «برداشتن» با «بستن» در ویکی‌واژه نامعلوم خوانده شده و پیوند با *swer- «سنگین» تنها از پوکورنی است. پس واژه‌ها درست‌اند و از aeirō می‌آیند، ولی پیوستن ریشه‌ها با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"ἀείρω\",W+\"ἀρτηρία\",W+\"ἀορτή\",AHDq+\"aorta\"],\n  \"ref_check\":[rc(\"AHD:1150\",\"supports\",\"AHD 1985 wer-2: 'Basic form *awer- in Greek aeirein, to raise, and Greek artēria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. [Pok. 1. wer- 1151.]' (Nourai's '1150' is presumably a Pokorny page number.)\"),\n               rc(\"IEC:1347\",\"not_found\",\"Mann's suer- entry (cols. 1347-1348) cites Gk. hérma/hórmos, not aeirō or artēria; grep 'aeir|aort' in IEC.txt finds only an unrelated mention.\")],\n  \"consulted\":[cs(\"POK\",\"1. uer- 1150 (l.91335ff.)\",\"supports\",\"'Gr. aeirō ... aortē 'leather sack' ... arteria 'windpipe, Arterie', besides aortē 'Aorta''.\"),\n               cs(\"WLD\",\"Bd. I p. 264\",\"supports\",\"WP I 264 discusses the contraction of aeirō to airō and its 'aufhängen' sense under uer- 'Schnur'.\"),\n               cs(\"KLN\",\"s.v. aorta (l.16867)\",\"supports\",\"'Gk. aortē, 'the great artery', fr. aeirein, 'to lift, raise up, bear''.\")]},\n {\"id\":6,\"lang\":\"English\",\"words\":\"aorta, artery, meteor\",\"verdict\":\"confirmed\",\n  \"derivation\":\"aorta (16th c.) < New Latin aorta < Greek aortḗ (Aristotle's term for the great artery 'hung' from the heart); artery (late ME arterie) < Old French artaire / Latin artēria < Greek artēría 'windpipe, artery'; meteor < Middle French météore < Medieval Latin meteōrum < Greek metéōron 'thing high in the air', from metéōros 'raised from the ground' = meta- + -āoros 'lifted', akin to aeírō. All three go back to aeírō as drawn.\",\n  \"derivation_fa\":\"aorta از لاتین نو aorta و یونانی aortē؛ artery از فرانسوی کهن artaire و لاتین artēria و یونانی artēria «نای، سرخرگ»؛ و meteor از فرانسوی میانه météore و یونانی metéōron «چیزی که در هوا بالاست»، از metéōros «از زمین برخاسته» (meta- + -āoros از aeirō). هر سه واژه چنان‌که نمودار نشان می‌دهد از aeirō اند؛ ادعای نورایی درست است.\",\n  \"sources\":[W+\"aorta\",W+\"artery\",W+\"meteor\",AHDq+\"meteor\",AHDq+\"aorta\"],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"AHD online: aorta '[New Latin, from Greek āortē, from āeirein, to lift; see wer-1]'; meteor '... meteōros, high in the air : meta- + -āoros, lifted; akin to āeirein, to lift up; see wer-1'.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. aorta\",\"supports\",\"'Cp. artery and the second element in endaortic and in meteor.'\"),\n               cs(\"SKT\",\"s.v. Aorta (SKT.txt l.791)\",\"supports\",\"'Aorta. (Gk.) Gk. aortē, the artery 'rising' from the heart. — Gk. aeirein, to raise.'\")]},\n {\"id\":7,\"lang\":\"French\",\"words\":\"aorte\",\"verdict\":\"confirmed\",\n  \"derivation\":\"French aorte (16th c., Ambroise Paré era) is a learned borrowing of Greek ἀορτή (via New Latin aorta), with the French -e of feminine nouns.\",\n  \"derivation_fa\":\"فرانسوی aorte وام‌واژه‌ای علمی از یونانی aortē (از راه لاتین نو aorta) در سدهٔ شانزدهم است؛ ادعای نورایی درست است.\",\n  \"sources\":[W+\"aorte\"],\n  \"ref_check\":[rc(\"none\",\"not_checked\",\"the node carries no reference in the book.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. aorta\",\"supports\",\"ModL. aorta from Gk. aortē; French form implied by the Romance chain.\"),\n               cs(\"AHD\",\"online s.v. aorta\",\"supports\",\"'[New Latin, from Greek āortē ...]'.\")]},\n {\"id\":8,\"lang\":\"Persian\",\"words\":\"â`ort\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Persian آئورت âort is a modern medical loan from French aorte (Mo'in marks it [فر.] 'French'), entering with French-language medical teaching in the late 19th-20th c.; the Academy equivalent is بزرگ‌سرخرگ.\",\n  \"derivation_fa\":\"«آئورت» واژه‌ای پزشکی است که در دورهٔ نو از فرانسوی aorte به فارسی آمده است؛ معین آن را [فر.] نشان داده و برابرش را «بزرگ‌سرخرگ» آورده است. ادعای نورایی درست است.\",\n  \"sources\":[\"https://vajehyab.com/moein/آئورت\",W+\"آئورت\"],\n  \"ref_check\":[rc(\"VOP:1\",\"not_checked\",\"Moshiri's Farhang-e Vazheha-ye Orupayi not available online (refs_online.json).\")],\n  \"consulted\":[cs(\"MON\",\"vajehyab moein s.v. آئورت\",\"supports\",\"'(ئُ) [ فر. ] (اِ.) سرخرگ بزرگی که به بطن چپ قلب متصل است ... بزرگ سرخرگ'.\"),\n               cs(\"ARY\",\"grep 'آئورت' ARY_pages.txt\",\"silent\",\"no entry (loanwords not covered).\")]}\n]}\n\ne2={\"entry\":2,\"root\":\"Wer 6, Werd\\nWordos, Worda, Wordia\",\"verdict\":\"plausible\",\n\"modern_form\":\"PIE *wer- 'raised spot' (Pokorny 2. uer- 1151 'highland, high place'; extensions *wer-d- 'wart' and *wer-s- 'height'); AHD wer-1 'high raised spot'\",\n\"note\":\"Pokorny 1151-1152 and Watkins/AHD wer-1 match the root, the extension *wer-d- (Germanic *wartōn) and *wr̥s-u-ko- (Latin verrūca), and Pokorny explicitly lists 'npers. bālū 'wart' (Iran. *vard-)'. The extra gloss 'frog' and the forms Wordos/Worda/Wordia (presumably from Mann) are not in Pokorny or AHD and could not be found in Mann's OCR (IEC 1577 not located), hence plausible rather than confirmed.\",\n\"note_fa\":\"ریشهٔ هندواروپایی *wer- «برآمدگی، جای بلند» (پوکورنی ۱۱۵۱، ریشهٔ ۲. uer-) با گسترش *wer-d- «زگیل» و *wer-s- «بلندی» در پوکورنی و امریکن هریتیج (wer-1) آمده است و پوکورنی خود «بالو»ی فارسی را به معنای «زگیل» از ایرانی *vard- می‌داند. بخش اصلی ریشه درست است، ولی معنای «قورباغه» و صورت‌های Wordos/Worda در هیچ‌یک از منابع دیده نشد؛ پس کل ریشه با احتیاط پذیرفتنی است.\",\n\"sources\":[AHDq+\"wart\",W+\"verruca\",W+\"wart\"],\n\"ref_check\":[rc(\"POK:1151\",\"supports\",\"POK_full.txt l.91411ff.: 'uer-2 ... highland, high place ... uer-d-: npers. bālū 'wart' (Iran. *vard-), Old High German warza, Old English wearte, Old Icelandic varta (*uordā) 'wart' ... uer-s-: Latin verruca'.\"),\n             rc(\"IEC:1577\",\"not_found\",\"no *uordos/'wart'/'frog' entry located in IEC.txt; Mann's uers- (3) 'growth, hard skin' (Lat. verruca) is near p. 1521.\")],\n\"consulted\":[cs(\"AHD\",\"Watkins 1985 wer-1 (l.1144)\",\"supports\",\"'wer-1. High raised spot. 1. Suffixed form *wer-d- in Germanic *wartōn- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish varbulde ... WARBLE2 ... 5. ... *wr̥su-ko- in Latin verrūca'.\"),\n             cs(\"WLD\",\"Bd. I p. 267\",\"supports\",\"'uer-d: ahd. warza, ags. wearte, anord. varta „Warze“ ... npers. (Horn bei Kluge) bālū „Warze“; uer-s-: lat. verruca'.\")],\n\"nodes\":[\n {\"id\":1,\"lang\":\"Persian\",\"words\":\"bâlŭ\",\"verdict\":\"plausible\",\n  \"derivation\":\"Persian بالو / پالو bālū 'wart' (Borhan: 'آژخ ... بعربی ثؤلول', Mo'in: 'زگیل، آزخ'; attested in the Samanid poet Shaker Bokhari) is derived by Horn (via Kluge), Walde-Pokorny and Pokorny from Iranian *varda-/*vr̥d- 'wart' = Germanic *wartōn. The sound changes are regular: initial *v- > b- (as in bād, barf), and *-rd- > -l- in Persian (as in sāl < *sard-, dil < *zr̥d-), plus a suffix -ū. Aryanpur accepts the same comparison. No modern Iranian etymological dictionary was found that discusses it (Wiktionary's بالو treats only the homonym 'cherry'), so the derivation stays plausible rather than confirmed.\",\n  \"derivation_fa\":\"«بالو / پالو» به معنای «زگیل، آژخ» (برهان قاطع: «آژخ ... به عربی ثؤلول»؛ معین: «زگیل، آزخ»؛ با گواه شعری از شاکر بخاری) را هرن، والده-پوکورنی و پوکورنی از ایرانی *varda- «زگیل»، هم‌ریشه با ژرمنی *wartōn و انگلیسی wart، می‌دانند. دگرگونی‌های آوایی منظم است: v آغازی به b (مانند باد، برف) و rd به l (مانند سال، دل)، و افزوده شدن پسوند -ū. آریان‌پور نیز همین هم‌سنجی را آورده است، اما در منابع ریشه‌شناختی نوین ایرانی بحثی درباره‌اش یافت نشد؛ پس با احتیاط پذیرفتنی است.\",\n  \"sources\":[\"https://vajehyab.com/moein/بالو\",W+\"بالو\"],\n  \"ref_check\":[rc(\"IEC:1577\",\"not_found\",\"no Persian bālū found in IEC.txt (grep 'Per. b.l.').\"),\n               rc(\"MON:467\",\"supports\",\"Mo'in (vajehyab moein s.v. بالو): '( اِ.) زگیل ، آزخ' — confirms the word and meaning; page 467 not mappable online.\"),\n               rc(\"FRS:201\",\"not_found\",\"FRS_pages.txt is a different edition (Eqbal/Horn); grep for بالو / the Shaker Bokhari line 'زیر چشم ... بالو' found nothing.\")],\n  \"consulted\":[cs(\"BQT\",\"vol. 1, BQT_v1_pages.txt leaf 447, l.17147\",\"supports\",\"'بالو - بروزن خالو. برادری را گویند که از یک مادر و دو پدر باشد - و بمعنی آژخ هم هست و آن دانه‌ایست ... که در اعضای آدمی بر می‌آید و درد نمی‌کند، آنرا بعربی ثؤلول خوانند' (meaning only, no etymology in the OCR).\"),\n               cs(\"ARY\",\"pdf page 108 (ARY_pages.txt l.3126)\",\"supports\",\"'بالو (به چم «زگیل»)' with cognates Old Icelandic varta, Old English wearte, German Warze, Latin verruca etc.\"),\n               cs(\"POK\",\"1151\",\"supports\",\"'npers. bālū 'wart' (Iran. *vard-)'.\"),\n               cs(\"WLD\",\"Bd. I p. 267\",\"supports\",\"'npers. (Horn bei Kluge) bālū „Warze“'.\"),\n               cs(\"HRN\",\"grep 'bālū|balu' HRN.txt\",\"silent\",\"no entry in the Grundriss itself (Horn's opinion is cited via Kluge).\")]},\n {\"id\":2,\"lang\":\"Germanic\",\"words\":\"war, wartôn\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Proto-Germanic *wartǭ / *wartōn- 'wart' (OE wearte, OHG warza, ON varta, Dutch wrat) < PIE *wr̥d-/*wordā-, a d-extension of *wer- 'raised spot' (Pokorny, AHD, Wiktionary). 'war' matches the unextended Germanic *war- of North Germanic var 'pus' (Swedish var, Icelandic var 'Augenschleim'), which Pokorny puts under the same root.\",\n  \"derivation_fa\":\"ژرمنی آغازین *wartōn «زگیل» (انگلیسی کهن wearte، آلمانی کهن warza، نورس کهن varta) از هندواروپایی *wr̥d-/*wordā-، گسترش d-دار ریشهٔ *wer- «برآمدگی» است. صورت war با *war- ژرمنی در سوئدی var «چرک» برابر است که پوکورنی آن را هم زیر همین ریشه آورده است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"wart\",AHDq+\"wart\"],\n  \"ref_check\":[rc(\"POK:1151\",\"supports\",\"'Old High German warza, Old English wearte, Old Icelandic varta (*uordā) 'wart'' and 'nisl. var 'Augenschleim', Swedish var 'pus''.\")],\n  \"consulted\":[cs(\"AHD\",\"wer-1\",\"supports\",\"'*wer-d- in Germanic *wartōn- in Old English wearte'.\"),\n               cs(\"KLN\",\"s.v. wart (l.265168)\",\"supports\",\"'OE wearte, rel. to OS warta, ON varta ... OHG warza ... cogn. with ... L. verrūca'.\"),\n               cs(\"WLD\",\"Bd. I p. 267\",\"supports\",\"'uer-d: ahd. warza, ags. wearte, anord. varta'.\")]},\n {\"id\":3,\"lang\":\"English\",\"words\":\"wart, warble\",\"verdict\":\"plausible\",\n  \"derivation\":\"wart < ME warte < OE wearte < Proto-West Germanic *wartā < PGmc *wartǭ (Wiktionary, AHD), so confirmed. warble (a small hard tumour on the back of cattle or horses, 1520s) is of uncertain origin (Klein). AHD connects it only 'possibly' with obsolete Swedish varbulde 'pus swelling' (var 'pus' + bulde 'swelling'), Germanic *war-; it is not a derivative of *wartōn. The bird verb warble is unrelated (Old North French werbler, Frankish). Overall plausible because of warble.\",\n  \"derivation_fa\":\"wart از انگلیسی میانه warte و انگلیسی کهن wearte و ژرمنی *wartōn است و قطعی است. اما warble به معنای «غدهٔ سخت زیر پوست چارپا» ریشهٔ روشنی ندارد (کلاین)؛ امریکن هریتیج تنها «شاید» آن را با سوئدی کهنه varbulde «ورم چرکی» (var «چرک» + bulde «ورم») پیوند می‌دهد، و فعل warble «چه‌چه زدن» واژه‌ای دیگر و نامرتبط است. پس این گره با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"wart\",W+\"warble\",AHDq+\"wart\",AHDq+\"warble\"],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"AHD 1985 wer-1: 'WART' and '2. Possibly Germanic *war- in obsolete Swedish varbulde, 'pus swelling' ... akin to the source of WARBLE2' — hedged for warble.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. warble n. (l.264937)\",\"contradicts\",\"'warble, n., a small hard tumor on horses or cattle. — Of uncertain origin.'\"),\n               cs(\"KLN\",\"s.v. wart\",\"supports\",\"'ME., fr. OE. wearte'.\"),\n               cs(\"SKT\",\"s.v. warble (l.21392)\",\"silent\",\"only the verb 'to sing as a bird' (O. F. werbler), not the swelling.\")]},\n {\"id\":4,\"lang\":\"Latin\",\"words\":\"verrŭka\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin verrūca 'wart; steep place, hillock' < *wersūkā < Proto-Italic *we/ors-u- + -ūca < PIE *wers-/*wr̥s- 'raised spot, height' (s-extension of the same *wer-, cf. Skt. várṣman- 'height', OCS vrьxъ 'top'); -rs- > -rr- regularly in Latin. Pokorny and AHD (*wr̥su-ko-) agree, though the extension is -s- rather than the -d- of the Germanic wart. The book prints 'verrŭka' in Nourai's transliteration (k for c, breve for long ū); extraction faithful.\",\n  \"derivation_fa\":\"لاتین verrūca «زگیل؛ تپه» از *wersūkā و ایتالیک آغازین *wors-u- با پسوند -ūca، از هندواروپایی *wers- «برآمدگی، بلندی» (گسترش s-دار همان ریشهٔ *wer-) است و rs در لاتین به rr همگون شده است. پوکورنی و امریکن هریتیج همین را می‌گویند؛ تنها گسترش آن s است نه d. ادعای نورایی درست است و نگارش verrŭka شیوهٔ آوانویسی خود نورایی است.\",\n  \"sources\":[W+\"verruca\"],\n  \"ref_check\":[rc(\"POK:1151\",\"supports\",\"'uer-s-: Latin verruca 'a steep place, height, a wart on the human body'' (POK_full.txt, uer-2).\"),\n               rc(\"IEC:1577\",\"partial\",\"Mann has 'uers- (3) 'growth, hard skin' Lat. cf. verr-ūca, f. 'wart; hillock'' (IEC.txt l.20089, near p. 1521), not on p. 1577.\")],\n  \"consulted\":[cs(\"AHD\",\"wer-1\",\"supports\",\"'Suffixed and extended zero-grade form *wr̥su-ko- in Latin verrūca, a wart: VERRUCA.'\"),\n               cs(\"KLN\",\"s.v. verruca (l.260914)\",\"supports\",\"'L. verrūca ... which stands for *versūcā and is cogn. with OE wearr, 'callosity, wart', wearte'.\"),\n               cs(\"WLD\",\"Bd. I p. 267\",\"supports\",\"'uer-s-: lat. verruca „Warze“ (bei Cato auch „locus editus et asper“)'.\")]},\n {\"id\":5,\"lang\":\"English\",\"words\":\"verruca\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English verruca (medical, 16th c.) is a learned borrowing of Latin verrūca 'wart', a doublet of native wart.\",\n  \"derivation_fa\":\"انگلیسی verruca اصطلاحی پزشکی است که در سدهٔ شانزدهم مستقیماً از لاتین verrūca «زگیل» گرفته شده و جفت‌واژهٔ (دوگانهٔ) واژهٔ بومی wart است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"verruca\"],\n  \"ref_check\":[rc(\"AHD\",\"supports\",\"AHD 1985 wer-1 ends '... Latin verrūca, a wart: VERRUCA'; index 'VERRUCA wer-1'.\")],\n  \"consulted\":[cs(\"KLN\",\"s.v. verruca\",\"supports\",\"'verruca, n., a wart. — L. verrūca'.\"),\n               cs(\"SKT\",\"grep '^verruca' SKT.txt\",\"silent\",\"no entry.\")]}\n]}\n\nout={\"pdf_page\":547,\"book_page\":517,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[e0,e1,e2]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-547.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-547.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-547.json >/dev/null && python3 tools/verify_check.py 547"
}
```


### [2026-10-17T00:09:02.989Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'unverified': 1, 'disputed': 1, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 14, 'not_found': 3, 'not_checked': 2, 'partial': 1}
books consulted: {'partial': 5, 'supports': 24, 'silent': 14, 'contradicts': 4} | by book: {'KLN': 12, 'AHD': 5, 'SKT': 5, 'WLD': 5, 'ARY': 4, 'POK': 4, 'BQT': 3, 'HRN': 2, 'MON': 2, 'BRT': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'IEC': 1}
```


## [2026-10-17T00:09:15.014Z] TOOL CALL #56: SubagentHandback

```json
{
 "message": "I verified PDF page 547 (book page 517) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-547.json. `verify_check.py 547` reports 15/15 nodes and 0 PROBLEM lines. The three redirect entries (Werb, Werd, Werdh) were skipped as instructed.\n\n**Verdicts**\n- **Nodes (15):** 9 confirmed, 4 plausible, 1 disputed, 1 unverified, 0 transcription_suspect.\n- **Roots (3):** 1 confirmed, 2 plausible.\n  - Wer 5 \"burn\" is confirmed.\n  - Wer 6/Swer is plausible: Pokorny puts \"bind/raise\" and \"weigh/heavy\" under one root; Watkins (AHD) splits them into two.\n  - Wer 6/Werd is plausible: the \"frog\" gloss and the forms Wordos/Worda/Wordia appear in no source I checked, including Mann.\n\n**Disputed (1)**\n- Wer 6/Swer #2, Persian xwâr «خوار»: only Mann (IEC 1348) derives it from *swer- \"heavy\". Horn no. 496, Hübschmann §108 and Wiktionary instead derive it from Avestan xᵛāθra- \"ease\", through Middle Persian xwār \"easy\". Horn says the sense \"low, despicable\" appears only in New Persian. Nyberg suggests a third origin, *hu-vāra-. Nourai's own note pointing to root \"Ěter\" is closer to the modern view.\n\n**Unverified (1)**\n- Wer 6/Swer #1, Avestan xwâiris: only Mann gives this form, and he lists it under two different roots. The \"weight\" gloss is not in Mann. The Bartholomae OCR is unreadable for xᵛ- words, so I couldn't check whether the form exists.\n\n**Plausible nodes (4)**\n- Latin sērius: Pokorny marks the link to *swer- as \"doubtful\".\n- Greek aeirein/arteria: the root grouping is contested, though the words themselves are real.\n- Persian bâlu \"wart\": supported by Pokorny, Walde-Pokorny and Aryanpur, and the sound changes fit (*v- > b-, *-rd- > -l-), but no modern Iranian dictionary discusses it.\n- English warble (the swelling on cattle): Klein calls it of uncertain origin, and AHD links it only \"possibly\".\n\nSamovar is confirmed, but Klein's minority view is noted in the file: he takes it as a Tatar word reshaped by folk etymology.\n\n**Extraction errors:** none. The printed page matches the JSON. The vowel marks in sěrius, verrŭka and bâlŭ are Nourai's own way of writing vowels, not misreadings.\n\n**Nourai's references not found:** I couldn't locate IEC:1577 (wart/frog) in Mann's OCR. FRS:201 is in a different edition from the one on disk, and the entry wasn't found there either. VOP:1 has no copy online."
}
```


### [2026-10-17T00:09:15.319Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
