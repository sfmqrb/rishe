# Verification process log — verify-page-546


## [2026-10-17T00:00:15.410Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 546 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-546.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-546.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-546.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 546` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.484Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.278Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.334Z] TOOL RESULT

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


## [2026-10-17T00:00:18.780Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-546.txt"
}
```


### [2026-10-17T00:00:18.797Z] TOOL RESULT

```
1	=== PDF page 546 (book page 516) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wer 3 / Werg 2, Wreg 2, Wrg : to cover / to enclose, constrict  (refs POK:1116; IEC:1599)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1116; AEF:212; KNT:207; SPG:230 | var 6, vara 2, vâra 2 : cover, wall ; vardana, paru-zana : walled-in area, city
5	  #2 (parent #1) [Persian] refs=BQT:216, 254, 1473 | vâr 1 «ـوار۴» : wall ; bâru «بارو» : castle wall ; barzan «بَرزن» : suburb, street | extra: باره
6	  #3 (parent #1) [Avestan / Old Persian] refs=POK:1116; AEF:268 | děğa-vâra : clay wall ☞Dheigh ; fra-vârna, upairi-vâra : with walls around or cover over ☞Per 1,Upo ; pairi-vâra : walled around, barn ☞Per 1 ; paiti-vâra : castle (defense) wall ☞Per 3
7	    #4 (parent #3) [Persian] refs=BQT:391,1473; AEF:268 | dîvâr «دیوار» : "clay wall" ; farvâr «فَروار» : a summer house with doors or windows on all sides ; parvâr «پروار» : barn, barn raised animal, fat animal | extra: فرواره، برواره
8	  #5 (parent #1) [Avestan / Old Persian] refs=BQT:1476,1478 | fra-var, fra-vahr, fravaši : a protecting angel ☞Per 1 ; fra-var-tinam : descent of holy spirits
9	    #6 (parent #5) [Pahlavi] refs=BQT | farvahr : a guarding angel ; farvartin : the month of "Farvahar"
10	      #7 (parent #6) [Persian] refs=BQT:1476-1478 | Farvahar «فَروَهَر» : a protecting angel ; Farvardîn «فروردین» : the first month of year | extra: فردین
11	#8 (parent #0) [Avestan] refs=POK:1116 | varethra : defender, also name of a demon ; varethra-jan, varethra-ğam : demon killer ☞Gwhen 2
12	  #9 (parent #8) [Pahlavi] refs=BQT:324 | varhrâm : victorious
13	    #10 (parent #9) [Persian] refs=None | vahrâm «وهرام» : victorious ; bahrâm «بهرام» : "demon killer", a male name
14	#11 (parent #0) [Persian] refs=IEC:1599; MON:3505 | gîj «گیج» : dizzy, dumb
15	#12 (parent #0) [Latin] refs=AHD | op-erîre : to cover ☞Epi ; ap-erîre : to uncover, open ☞Apo
16	  #13 (parent #12) [English] refs=None | cover ; aperture
17	#14 (parent #0) [Germanic] refs=AHD | war-n
18	  #15 (parent #14) [English] refs=None | warn
19	--- entry 1 ---
20	ROOT Wer 4 -> redirect to Wed
21	
```


## [2026-10-17T00:00:19.205Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-546.json"
}
```


### [2026-10-17T00:00:19.233Z] TOOL RESULT

```
1	{
2	  "pdf_page": 546,
3	  "book_page": 516,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wer 3 / Werg 2, Wreg 2, Wrg",
8	        "lang": "Indo-European",
9	        "refs": "POK:1116; IEC:1599",
10	        "gloss": "to cover / to enclose, constrict"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan / Old Persian",
17	          "refs": "POK:1116; AEF:212; KNT:207; SPG:230",
18	          "words": [
19	            {"translit": "var 6, vara 2, vâra 2", "gloss": "cover, wall", "script": null},
20	            {"translit": "vardana, paru-zana", "gloss": "walled-in area, city", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:216, 254, 1473",
30	          "words": [
31	            {"translit": "vâr 1", "gloss": "wall", "script": "ـوار۴"},
32	            {"translit": "bâru", "gloss": "castle wall", "script": "بارو"},
33	            {"translit": "barzan", "gloss": "suburb, street", "script": "بَرزن"}
34	          ],
35	          "script_extra": "باره",
36	          "note": null,
37	          "quote": {"text": "سر بارهٔ دژ بُد اندر هوا - ندیدند جنگ هوا کس روا", "poet": "Ferdowsî"}
38	        },
39	        {
40	          "id": 3,
41	          "parent": 1,
42	          "lang": "Avestan / Old Persian",
43	          "refs": "POK:1116; AEF:268",
44	          "words": [
45	            {"translit": "děğa-vâra", "gloss": "clay wall", "script": null, "see": ["Dheigh"]},
46	            {"translit": "fra-vârna, upairi-vâra", "gloss": "with walls around or cover over", "script": null, "see": ["Per 1", "Upo"]},
47	            {"translit": "pairi-vâra", "gloss": "walled around, barn", "script": null, "see": ["Per 1"]},
48	            {"translit": "paiti-vâra", "gloss": "castle (defense) wall", "script": null, "see": ["Per 3"]}
49	          ],
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Persian",
57	          "refs": "BQT:391,1473; AEF:268",
58	          "words": [
59	            {"translit": "dîvâr", "gloss": "\"clay wall\"", "script": "دیوار"},
60	            {"translit": "farvâr", "gloss": "a summer house with doors or windows on all sides", "script": "فَروار"},
61	            {"translit": "parvâr", "gloss": "barn, barn raised animal, fat animal", "script": "پروار"}
62	          ],
63	          "script_extra": "فرواره، برواره",
64	          "note": null,
65	          "quote": {"text": "آن کن که درین وقت همی کردی هرسال - خز پوش و به کاشانه رو از صفّه و فروار", "poet": "Rŭdakî"}
66	        },
67	        {
68	          "id": 5,
69	          "parent": 1,
70	          "lang": "Avestan / Old Persian",
71	          "refs": "BQT:1476,1478",
72	          "words": [
73	            {"translit": "fra-var, fra-vahr, fravaši", "gloss": "a protecting angel", "script": null, "see": ["Per 1"]},
74	            {"translit": "fra-var-tinam", "gloss": "descent of holy spirits", "script": null}
75	          ],
76	          "note": null,
77	          "quote": null
78	        },
79	        {
80	          "id": 6,
81	          "parent": 5,
82	          "lang": "Pahlavi",
83	          "refs": "BQT",
84	          "words": [
85	            {"translit": "farvahr", "gloss": "a guarding angel", "script": null},
86	            {"translit": "farvartin", "gloss": "the month of \"Farvahar\"", "script": null}
87	          ],
88	          "note": null,
89	          "quote": null
90	        },
91	        {
92	          "id": 7,
93	          "parent": 6,
94	          "lang": "Persian",
95	          "refs": "BQT:1476-1478",
96	          "words": [
97	            {"translit": "Farvahar", "gloss": "a protecting angel", "script": "فَروَهَر"},
98	            {"translit": "Farvardîn", "gloss": "the first month of year", "script": "فروردین"}
99	          ],
100	          "script_extra": "فردین",
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 8,
106	          "parent": 0,
107	          "lang": "Avestan",
108	          "refs": "POK:1116",
109	          "words": [
110	            {"translit": "varethra", "gloss": "defender, also name of a demon", "script": null},
111	            {"translit": "varethra-jan, varethra-ğam", "gloss": "demon killer", "script": null, "see": ["Gwhen 2"]}
112	          ],
113	          "note": null,
114	          "quote": null
115	        },
116	        {
117	          "id": 9,
118	          "parent": 8,
119	          "lang": "Pahlavi",
120	          "refs": "BQT:324",
121	          "words": [
122	            {"translit": "varhrâm", "gloss": "victorious", "script": null}
123	          ],
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 10,
129	          "parent": 9,
130	          "lang": "Persian",
131	          "refs": null,
132	          "words": [
133	            {"translit": "vahrâm", "gloss": "victorious", "script": "وهرام"},
134	            {"translit": "bahrâm", "gloss": "\"demon killer\", a male name", "script": "بهرام"}
135	          ],
136	          "note": null,
137	          "quote": null
138	        },
139	        {
140	          "id": 11,
141	          "parent": 0,
142	          "lang": "Persian",
143	          "refs": "IEC:1599; MON:3505",
144	          "words": [
145	            {"translit": "gîj", "gloss": "dizzy, dumb", "script": "گیج"}
146	          ],
147	          "note": null,
148	          "quote": {"text": "گفتگو بسیار گشت و خلق گیج - در سر و پایان این چرخ بسیج", "poet": "Molavî"}
149	        },
150	        {
151	          "id": 12,
152	          "parent": 0,
153	          "lang": "Latin",
154	          "refs": "AHD",
155	          "words": [
156	            {"translit": "op-erîre", "gloss": "to cover", "script": null, "see": ["Epi"]},
157	            {"translit": "ap-erîre", "gloss": "to uncover, open", "script": null, "see": ["Apo"]}
158	          ],
159	          "note": null,
160	          "quote": null
161	        },
162	        {
163	          "id": 13,
164	          "parent": 12,
165	          "lang": "English",
166	          "refs": null,
167	          "words": [
168	            {"translit": "cover", "gloss": null, "script": null},
169	            {"translit": "aperture", "gloss": null, "script": null}
170	          ],
171	          "note": null,
172	          "quote": null
173	        },
174	        {
175	          "id": 14,
176	          "parent": 0,
177	          "lang": "Germanic",
178	          "refs": "AHD",
179	          "words": [
180	            {"translit": "war-n", "gloss": null, "script": null}
181	          ],
182	          "note": null,
183	          "quote": null
184	        },
185	        {
186	          "id": 15,
187	          "parent": 14,
188	          "lang": "English",
189	          "refs": null,
190	          "words": [
191	            {"translit": "warn", "gloss": null, "script": null}
192	          ],
193	          "note": null,
194	          "quote": null
195	        }
196	      ]
197	    },
198	    {
199	      "root": {
200	        "name": "Wer 4",
201	        "redirect": "Wed"
202	      },
203	      "nodes": []
204	    }
205	  ]
206	}
207	
```


## [2026-10-17T00:00:23.573Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; command ls data/verification/sources/refs/ | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AEF','KNT','SPG','BQT','MON','AHD','WLD','BRT','PHD','NYB','HRN','HUB','CHEUNG','ARY','KLN','SKT']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-17T00:00:24.190Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SPG {"title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)", "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)", "kind": "archive_djvu", "url": "https://archive.org/details/diealtpersis
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-10-17T00:00:27.862Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]); print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:4000])\"; sed -n 1,200p tools/verify_check.py | grep -n \"PROBLEM\\|def \\|required\\|min\" | head -60"
}
```


### [2026-10-17T00:00:28.534Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Wekw, Weqw",
 "verdict": "confirmed",
 "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')",
 "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)",
   "stance": "supports",
   "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“ ... lat. vox vocis „Stimme“, voco, -āre „rufen“'."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985 s.v. wekw-",
   "stance": "supports",
   "note": "AHD_watkins1985.txt: 'wekw-. To speak. 1. O-grade form *wokw- in: a. Latin vox (stem voc-), voice: VOCAL, VOICE, VOWEL ... 2. Suffixed o-grade form *wokw-a- in Latin vocare, to call: VOCABLE, VOCATION ... 3. Suffixed form *wekw-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekw- 1135.]'
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "vak, vačah, vaxš 1",
 "verdict": "confirmed",
 "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.",
 "derivation_fa": "در اوستایی فعل vac- / vaoc- «گفتن»، نام‌واژهٔ vacah- «سخن، گفتار» (برابر سنسکریت vacas- و یونانی épos) و نام‌واژهٔ vāč- «آواز، سخن» با حالت فاعلی vāxš (برابر سنسکریت vāk و لاتینی vōx) آمده است. kʷ هندواروپایی در هندوایرانی به k و پیش از واکهٔ پیشین به č بدل شده است. بارتولومه و پوکورنی و چونگ همین را می‌گویند و ادعای نورایی درست است. تنها این صورت‌ها اوستایی‌اند و در پارسی باستان گواهی ندارند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-",
  "https://en.wiktionary.org/wiki/آواز"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90122 'Avestan vac- speak ... Old Indic vacas- n. = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word'."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "col. 1333-1336 s.v. vāk-; col. 1340-1341 s.v. vacah-",
   "stance": "supports",
   "note": "BRT.txt l.22236 'vāk- (vāxš) m., f. 1) Stimme; 1) der Menschen (und Götter) Stimme ... 2) Rede, Wort ... Zum V. vak-'; l.22355 'vacah- n. 1) Sprechen, Rede, Wort ... im Gegensatz zu Denken und Handeln'."
  },
  {
   "src": "WLD",
   "where": "Bd. I 245",
   "stance": "supports",
   "note": "'ai. vacas- n. = av. vacah- „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“'."
  },
  {
   "src": "SYN",
   "where": "18.11 VOICE",
   "stance": "supports",
   "note": "'Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš)'."
  },
  {
   "src": "CHEUNG",
   "where": "p. 402 s.v. *u̯ač",
   "stance": "supports",
   "note": "'AVESTAN: vaoc- (vāč-) to say' with forms vaocat, uxδa- etc."
  }
 ]
}
16:def page_no(path):
20:def main(argv):
90:        print("PROBLEM:", p)
```


## [2026-10-17T00:00:31.945Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py; command ls tools/"
}
```


### [2026-10-17T00:00:32.267Z] TOOL RESULT

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
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_commit_deploy.sh
verify_export_process.py
verify_finish_page.sh
verify_publish.sh
```


## [2026-10-17T00:00:35.303Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s) 111[5-7]\\|Page(s) 1160\\|Page(s) 1154\" POK_full.txt | head; grep -n \"to cover, shelter\\|to shut, cover\\|bedecken\" POK_full.txt | head"
}
```


### [2026-10-17T00:00:35.625Z] TOOL RESULT

```
81518:"deckend, sheltering; bedeckt, hidden, concealed', aT£yv6(; "bedeckend, schutzend; 
81522:*tegu- "thick'), aT£KTiK6(; "bedeckend, schutzend';
```


## [2026-10-17T00:00:38.017Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 1500 POK_full.txt; echo; grep -n \"1160\\b\" POK_full.txt | head; grep -n \"vara-\\|varəθra\\|vərəθra\" POK_full.txt | head -20"
}
```


### [2026-10-17T00:00:38.542Z] TOOL RESULT

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
91968:Page(s): 1159-1160 
92096:Page(s): 1160-1162 
4820:Old Indie adhvanru. = Avestan advanm. ' way, road ', for what Old Indie adhvara-h 
7453:preposition m. Akk. " there, there in '; therefrom Old Indie avara- "inferior' and Avestan 
23069:deception, seduction ', *d'^vara-^ deceiving ' in dhvaras-i. (Nom. -ah) "a kind of female 
23487:Old Indie *dati- "bestowal, gift' in dat/'-vara- ^a\\ott\ng willingly, generous ', havya-dat/-' 
24870:hardly accessible ', pratar-ftvan-^ fruh ausgehend oderauskommend ', itvara- "going', vTta- 
29201:possessed, governed ', Isvara-' wealthy, ably; m. master, lord '; Avestan /se'is master, 
38068:hurchati^ fails, glides, sways, falls '; hvaras-n. " curvature ', hvara- m. "snake', vihrut-t 
38294:Material: Old Indie yVara//" has a temperature, is feverish \jvara-h lever, pain, distress ', 
38348:', gaha-h'dep\h, the interior '; with a. gahana-, gahvara-' deep, dense', n. "depth, abyss, 
50229:karvara-, kabara-, karbura-, karbu- ds.); 
53058:quater{*k"etrus)\ Old Indie catvara-m. " rectangular place', Lithuanian ketverT quadruple 
65234:pTvan-, f. yC>7i/5/7 "tumescent, plentiful, obese, fat', pTvara- ds., newer formation of Fem. From 
81332:"standsicher, standing firm' in Old Indie sfhavara-'t\r\'\ck, standing firm, bestandig' (latter 
84194:pipe' (flute?); svara- svara-xx\. " clangor, sound, tone'; 
90269:having, welcome, wanted ', vara- m. "wish, Gegenstanddes Wunsches', vara- "vorzijglich, - 
90271:distinguished ', varana- n. "das Wahlen, WiJnschen', vara- m. "Kostbares, treasure, tribute' 
90297:voliti); Old High German walai.. Old Icelandic i/a/n. 'choice '(: Old Indie vara- m.); 
90426:D. Old Indie vala-, vara- m. " tail (haar), Haarsieb', ablaut. Lithuanian 1/5/arSchweifhaar 
90478:'immersion um die root eines Baumes' (compare Mayrliofer 1 , 79 f.), probably also vara- 
92023:vadhra-rw. va{i)-dhrT ds., i/ara- m. 'Einschlieften', also 1/5/a- (Avestan vara- ds.),
```


## [2026-10-17T00:00:44.924Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s): 11[01][0-9]\" POK_full.txt | head -30"
}
```


## [2026-10-17T00:00:45.195Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92000,92096p POK_full.txt"
}
```


### [2026-10-17T00:00:46.165Z] TOOL RESULT

```
87883:Page(s): 1100-1101 
88070:Page(s): 1104-1105 
88195:Page(s): 1105-1106 
88291:Page(s): 1106-1107 
88352:Page(s): 1110-1111 
88396:Page(s): 1111-1112 
88442:Page(s): 1112-1113 
88456:Page(s): 1113-1114 
88590:Page(s): 1111 
88599:Page(s): 1111 
88647:Page(s): 1108-1109 
88771:Page(s): 1114-1115 
88867:Page(s): 1115-1116 
88891:Page(s): 1116-1117 
89043:Page(s): 1118-1120 
89087:Page(s): 1117-1118 
93567:Page(s): 1103-1104
```


### [2026-10-17T00:00:46.200Z] TOOL RESULT

```
VetterGI. 29, 240); 

Lithuanian uzveriu, -i/e/^^/'shut', afverf/'open' (from which previously without proverb 
ver/u, vert/'open', and 'shut'; Old Church Slavic (za)/vbrQ, K/ieZ/'shut', Iter, ot-voriti^ open'; 

derivatives: *uortom\n Nom. PI. Lithuanian vartai, Latvian i/a/Y/'gate, door'. Old Prussian 
warto ^Uaustuxe'; Old Church Slavic vrata, russ. vorota^gate, luxe'; also to 3. uer- could 
belong Old Church Slavic vereja and z5-i/c>/7>'Hebebaum', russ. i/e/'eya'Torflugel', zavor 
'gesperrter passage '; 

perhaps here Lithuanian i/a/y// "drive, push' (formal = Germanic warjan. Old Church 
Slavic ot-voriti, compare also Old Indie Kaus. varayati) as 'das gate open, um das Vieh 
from the hurdle hinauszutreiben'; in addition russ. provornyj^ fast, rapid, hurried, agile'. 

B. uer-, ueru-, jw^-'verschlieften, cover, shield, rescue'; uer-to-^ paddock ', uer-tro^ 
protection', ^y-Zir-'Einzaunung'. 

Old Indie vrn6ti{a\so varatiand Kaus. varayati) 'umschlieftt, wehrt'; Avestan Akt. - 
varanav-, Med. varan- 'cover, wrap'; derivatives from a light basis: Old Indie i//Ya- participle 
Perf. Pass., vrti-f. 'Einzaunung' (Avestan h^m-varatay-^ braveness'), varman-n. ' 
protection ', vartra-n. 'Schutzdamm, Deich' (osset. i/5/f 'shield' from Iran. *vr&ra-, s. Bailey 
IRAS 1953, 110 f.), vrtra-n. 'Abwehr, enmity(en), fiend(e)', (Avestan vara&ra-'W\de'cstand, 
Wehr, shield'), Sg. GN l/A/As-Cthe die Gewasser einschlieflt'?), varatra-^ strap', vardhra-, 
vadhra-rw. va{i)-dhrT ds., i/ara- m. 'Einschlieften', also 1/5/a- (Avestan vara- ds.), 
lengthened grade vara- (Avestan -vara-) 'Deckung, Wehr'; Avestan i/5/'a/7a- 'UmhiJIIung, 



Bedeckung' (thereafter Old Indie varna- "paint, color' probably from "Bedeckung'), vars&a- 
"Verteidigungswaffe, Wehr', var9&man-^y^e\\r, parapet' etc.; 

£/e/i7- besides in present vmot/\n Old Indie varu-tar-m. "guarder, Schirmer', varu-tha-n. 
' protection, shield, army, herd, swarm ', perhaps the GN Varuna- as "the binder' (as M/tra 
above S. 710); here also Old Indie ^msya//" releases, eriost, rettet' as uru-s-yati, compare 
Hittite ^a/resse's/a 'protected'; about Old Indie Varuna-s. Wackernagel-Debrunner II 2, S. 
485 (to i/e/-- 'water', above S. 80); 

gr. perhaps supux;, -wtoc; ' mildew, mould, dank decay ', if actually 'Bedecker' (would be 
*e-Fpu)-T-, compare Old Indie arnd-vrt^6\e Fluten einschlieftend'); 

Fepu- in hom. epuaOai 'abwehren, rescue, preserve, protect', Impf. £pu:-ao, -to, themat. 
has changed spusTO, Perf. Eipupai (*F£-Fpuijai), Ionian Eipuopai (*£F£puopiai) 'hold fest, 
preserve', spupia ' protection, defense ', £pupv6(; 'geschijtzt, befestigt', spuai-nroAK; 
'stadtschijtzend'; Eupuai-Aao(;, Eupu-Aao(; (s-Fpu-); 

other ablaut grade FpO- without Vokalvorschlag in Inf. hom. puaOai, hom. Ionian puoijai 
'schirme, errette; hold fest, hold back' (latter meaning, die also the /r-Erweit. spuKU), 
spuKavu), spuKavaoj 'hold ab, back'. Pass, 'zogere' innewohnt, from ' through einen lock 
fernhalten, abwehren'), Perf. £ipO|jai (*F£-FpOpai), pupa ' protection, defense ', puaiO(; 
'schiJtzend, rettend', puTOjp, pOrrip 'savior, redeemer, liberator', pOainoAK; 
"stadtschijtzend'; lengthened grade npiov 'burial mound'; 

alb. varr' grave' {*yorna), vathe' paddock'; 

Old Irish ferenn {* uereno) 'belt, girdle', /fe/Yae (Middle Irish fert} 'burial mound' (with 
stone verschlossen) = Old English weord{see below). Old Irish feronn, ferann {*uerono-) 
'land, farmland' (probably '*umhegt'); mcymr. ^i4/e/f/7y/' 'fortress' {*uertro-\ compare above 
Old Indie vartra-); here probably Old Irish Eriu, Gen. Erenn, (common Celtic -ns-, -nt- > - 
nrh), cymr. /M/e/io'o'o/7'lrland' as *epi-uend. Gen. -/c»/7cs'hill, island' (compare Old High 
German werid) after Pokorny KZ. 47, 233, ZcP. 15, 197 ff.; 

Gothic warjan ' 6eien6' , Old Icelandic i/e/ya 'defend, hinder, verteidigen'. Old English 
wer/an^6s., aufdammen'. Old High German n/e/ie/? 'verteidigen, shield ', Old Saxon werian 
"defend, shield, hinder', Germanic -K5/77('Verteidiger', out of it 'inhabitant') in Chatuvarii, 
Bojuvarii, Old Icelandic e.g. Rum-verjar' Romer'; Proto Norse waru'the umschlieftende 
Steinkreis um ein grave' (see above Irish fert) = Old Icelandic vgri., New Norwegian vor 
m. "Reihe from stone ', also "hill or bank from stone or gravel ', Old Icelandic veru. " dam. 



fish weir', Old Engiisli werxw. ds., Middle High German wern. 'Stauwehr', Old High 
German werfy^ehr, protection', Old English mylen-waru, -M/e/''Muhlenteich', waru^ 
protection'; lengthened grade Old High German wuoni. " dam ', Swiss wuhr^VMehr'; Old 
Icelandic i/p/77'Verteidigung, protection'. Old English M/ea/77'Widerstand, Verweigerung' (in 
Middle High German warne, M/e/77e"Vorsicht, FiJrsorge, warning' is ein to *uer- 'gewahren' 
gehoriges word eingeflossen). Old Icelandic Ka/77a"sichenthalten, vorenthalten' = Old 
English wearn/an' warn', refl. "sich enthalten'. Old High German M/a/77d/7 "sich hijten, warn', 
Old English M//e/77a/7'sich enthalten, vorenthalten, chop, cut, reject'; 

Old English warodn. "bank, border, shore, beach, seaside'. Old High German i/i/erid 
"island, Halbinsel' (Modern High German Werder), Middle High German M/e/'/"Landrucken 
between Sumpfen, bank, border, shore'. Middle Low German werde{i) "eingedeichtes land 



Old English weord, wordn. m. " courtyard, household ' {*uer-to-, *ur-to-). Old Saxon 
wurtht "gestampfter odergepflasterter Platz' (= Old Indie vrti-). Middle Low German wurt, 
wort, wurde, wordei. "erhohter place, Hofstatte; garden, FeldstiJck', Old Icelandic urdi. 
"heap from Felsblocken'; 

compare alb. vathe^ paddock, Hof um das Haus, hurdle, sheepfold ' {*uor-ta), tochar. B 
warto, warfffjo' garden, wood, forest', Irish fert'bur\a\ mound'; in the meaning also Old 
Church Slavic i/c»/'5"saepimentum'. 

References: WP. I 280 ff.. Frisk 568 f., 593 f., 643 f.; 
See also: in addition uergh-1. 
Page(s): 1160-1162
```


## [2026-10-17T00:00:50.642Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91880,91975p POK_full.txt | grep -n \"Root\\|Meaning\\|Page\" ; for l in 88771 88867 88891; do sed -n \"$((l-0)),$((l+6))p\" POK_full.txt; done; grep -n \"Root / lemma: uer\\|Root / lemma: ver\\|lemma: uer\" POK_full.txt|head -30"
}
```


### [2026-10-17T00:00:50.992Z] TOOL RESULT

```
48:Page(s): 1158-1159 
50:Root / lemma: uer-3. I. ur-ek e) ureip-, unp-{*huer-3) 
51:Meaning: to turn 
68:Page(s):1159 
70:Root / lemma: uer-S. I. ur-ei-. Q ureit- {* huer-3) 
71:Meaning: to turn 
89:Page(s): 1159-1160 
91:Root / lemma: uer-4 {*huer-4) 
93:Meaning: to find, take 
Page(s): 1114-1115 

Root / lemma: ued^-l 

Meaning: to push, hit 

Material: Old Indie vadhati, avadhTt^hW, bump, poke, destroy', Kaus. vadhayati, vadha-xx\. 
Page(s): 1115-1116 

Root / lemma: ueA'^-S 

Meaning: to bind, attach 

Material: Old Indie vl-vadha-m. "Schulterjoch zum Tragen from Lasten, Tragholz, 
Page(s): 1116-1117 

Root / lemma: ued- 
See also: s. ue(i!^-2 
Page(s):1115 

Root / lemma: ueg- 
22997:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
74446:Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
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
91827:Root / lemma: uer-3. I. ur-ei- a) urei-n-: {* huer-3) 
91846:Root / lemma: uer-S. I. ur-e/-. p) urizd- {* huer-3) 
91860:Root/ lemma: uer-3. I. ur-ei- y) ureig- {* huer-3) 
91877:Root/ lemma: uer-3. I. ur-ek 5) ureiR- {* huer-3) 
91929:Root / lemma: uer-3. I. ur-ek e) ureip-, unp-{*huer-3) 
91949:Root / lemma: uer-S. I. ur-ei-. Q ureit- {* huer-3)
```


## [2026-10-17T00:00:56.008Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91141,91240p POK_full.txt; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['POK'],ensure_ascii=False,indent=1)); print(json.dumps(d['IEC'],ensure_ascii=False,indent=1))\""
}
```


### [2026-10-17T00:00:56.413Z] TOOL RESULT

```
Root /lemma: uerg-1, ureg-{*huerg-1) 

Meaning: to close, enclose; pen 

Note: extension from uer-5. 

Material: Old Indie vraja-m. " hurdle, Umhegung', vrjana-m. "Umhegung, Einfriedigung, 

abgeschlossene settlement ', Gatha-Avestan varazana-, \&^ . varazana-, ap. vardana-n. 

"Gemeinwesen' (out of it borrowed Old Indie vardhana-' town, city', Wackernagel KZ. 67, 

168f.); Avestan varaz- ^absperren'; oss. aerudez{*wraza-= Old Indie vraja-) " herd, 

Hirsche'; 

hom. spyu), spyaGw (F-) and (with Vorschlags £-) sspyu), Attic sipyu) "schliefte ein, from, 
hold ab', Attic sipKir), Ionian spKir) " jail ', Attic £ipyp6(; " jail, lock ', Cypriot ka-te-vo-ro-ko- 
/7e"sie belagerten'; in addition Old Irish fraig^wa\\\ nir. fraigh^\Na\\ from wickerwork, roof, 
hurdle ', because of mcymr. ach-vre 'wattled fence' from *uregi- (Loth RC. 38, 301). 

References: WP. I 290, Frisk 465 f.; Benveniste BSL. 52, 34; 
See also: compare uergh- above S. 1 154. 
Page(s):1168 

Root / lemma: uerg-2, ureg- {*hueig-2) 
Meaning: to do, work 

Material: Avestan varaz-{varazyeiti= Gothic waurkeil=^, s. also gr. ps^oo) " work, do, make', 
participle varsta-, varaza-m. " work, Verrichten from, occupation ' (npers. varz, barz 
"Feldarbeit, Ackerbau'), varsti-i. "Handein, Tun', varstva- M]. 'was to tun is'; Armenian 
gorc^work' (with secondary o); gr. spyov, Fspyov ' work' (= German Work ' work '), 
epya^OMQi 'arbeite', thereafter £pyaTr|<; 'worker' (for *£py6Tr|<;), spSu) (occasionally £p5(jo) 
"do, sacrifice ' (*F£pz5u), "i/e/g/o lengthened grade after Fspyov as in Old Saxon wirkian). 



Fut. sp^oj, Aor. sp^a, Perf. sopya), ps^w "do' (from ps^ai neologism, hom. apsKToq 
"ungetan' reconverted with metathesis from *a[F]£pKTO(;); opyavov "tool', opyia "(secret) 
worship', opYia^u) "feiere Mysterien', opyscbv "Mitglied a religiosen BriJderschaft'; opva^u), 
Ionian opvau), opyiCu) "knead, ruhre through, tan, convert hide into leather' (as Modern 
High German Teig wirken\N\Vr\ meaning- contraction in the professional jargon), wherefore 
EopYH " verticil, whorl, group of parts (leaves, flowers, etc.) arranged in a circle ' (probably 
redupl. Fs-Fopya); 

Zero grade alb. {*ureg-) rregj"c\ear\\ Mediopassiv rregjem^ trouble about, strain, strive' 
(stem E. Mann Lg. 26, 382 f.); (common Slavic Baltic Albanian Greek ure-> rre-see pE^co 
"do'). 

abret. guerg^ effective] capable of filling some function; (person/medicine); legally valid ', 
gall, vergo-bretus^ uppermost authority of Aeduer', also i/e/rc-it'/'e/o (Pokorny, Vox 
Romanica 10, 266 f.); mcymr. gwre/fhleat, dead, act' {*ureg-tu-), 1. PI. Imper. acymr. 
guragun, newer gwnawn etc. (/? instead of /"through influence of *gn/'- ' make' , S. 373), 
corn, gruen, mbr. gr-{u)eomp {* ureg- "make'), Lewis-Pedersen S. 336 f.; 

Old Saxon wirkian (neologism after werR), warhta. Old High German (Franconian) 
wirkan, wirchen, war{a)hta^ work, be active, work '; Gothic waurkjan{= Avestan varazyeitl). 
Old Icelandic yrkja, orta. Old English wyrcan, worhte. Old High German (Upper German) 
wurchen, wor{a)hta^ work, do, make, effectuate ', Old High German gawurhti. "feat, dead, 
act, action', Gothic frawaurhts^ sinful ', f. " sin ' etc., Gothic waurstwr\. "work' {*waurh- 
stwa-\ similarly Avestan varstva-); Old High German were, werah. Old Saxon werk. Old 
Icelandic werkr\. (= spyov) "work, occupation, job'. Old English weorca\so " hardship, 
agony', wherefore also Old Icelandic verkr. Gen. verkjar{rw. /-stem) "pain, affliction' could 
belong here; 

Old High German liv/^e/? nanena^iicKena^eDen^en^mger^ = Old Saxon wirkian. 
Old English wircan, and das therefrom not trennbare Old High German werifi\r\ the 
meaning " coarse flax, tow, oakum ', awirihhi, awuritihi^ oakum ' show use our root auf die 
Weberei; s. against it Marstrander IF. 22, 332 f. (the l/Verg ar\d wirken^to weave' the root 
*uerg-'turr\, coil ' allot mochte); an Modern High German IVerg rerr\\r\6s cymr. cy-warc/i' 
hemp, flax' = bret. koarc'fi, abret. coarcholion <^\. " canabina '; Marstrander ZcP. 7, 362 
seeks therein ein Indo Germanic *uer-k- "turn', see above S. 11 55. 

References: WP. I 290 f.. Frisk 548 f. 
Page(s): 1168-1169 



Root / lemma: ueiy-3, uorg- {*hueiy-3) 

Meaning: to abound, to be full of strength 

Material: Old Indie urj-, urjai., urja- m. "juice, sap and power, nourishment, food' {*Uorg-l), 

urjayati' nourishes, strengthens', urjasvant-^ plentiful '; 

gr. opYH "seelischer, heftiger shoot, Affekt, rage, fury' (opyi^u) 'erzijrne jemanden' ), 
opYQU) "from dampness and juice, sap strotzen, violent lust, crave, in leidenschaftlicher 
Stimmung sein', opya^, -a5oc; (vn) "iJppigerfruchtbarer Erdboden, Marschland, Au'; 

e-grade Old Irish fere. Middle Irish fergi. "rage, fury' presumably also the (oKzavoo, 
Ou£pyiouiO(; by Ptol. (i.e. i/e/y/V/bs "the angry'? or still "the schwellende, surging '?); 
mcymr. y wer/t^ sea' (that is to say y werydd) rather from *UerJo- to *auer- above S. 80 and 
1165; compare Pedersen Celtic Gr. II, 669 f. 

References: WP. I 289, Mayrhofer 1,116. 
Page(s): 1 1 69 

Root /lemma: uer-10{*huer-10) 

{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
```


## [2026-10-17T00:01:02.699Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 352 353 354 355; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt | head -8; done"
}
```


### [2026-10-17T00:01:03.031Z] TOOL RESULT

```
=== leaf 352
 291,  H.  Seiler  Festschrift  Debrunner  409  ff dazu  das  folgende:
'&'
uen-  ^schlagen,  verwunden'  (:  uä-,  ähnlich  wie  g^em-ig^ä-  ,gehen,  kommta^j Arm.  vandem  ^zerstöre*;  got.  wunds  , verwundet',  ahd.  nhd.  as.  ag87li0Mk/ Subst.  ahd.  wunta,  ags.  wund,  aisl.  und  , Wunde'  (^un-tös,  -td),  agt.^1 ^Geschwulst'  (ursprüngl.  wohl  , Beule  infolge  eines  Schlages'),  eng1,\<. mnd.  wene,  dän.  dial.  vann,  vosTie  (urgerm.  *wanja)'  cymr.  ym-wan  ,kämpL. mcymr.  gweint  ^ich  durchbohrte',  3.  Sg.  gwant]  gwäuj  ,punctio',  com.  yt< ym-wanas  ,percussit',  gwane  ,perforare*.
WF.  I  212.  W
3.  uä-  , auseinander',  bes.  , auseinander  biegen,  drehen'.
Diese  Wurzel,  welche  möglicherweise  eine  Reihe  von  Erweiterangf» (s.  u.),  liegt  nach  aller  Wahrscheinlichkeit  vor  in  lat.   värus  ^useiüMI gebogen,  auswärts  gebogen;  dachsbeinig;  entgegengesetzt*,  väricui auseinander    spreizend',    väricö,    -äre    ,Füße    auseinander    spreizen, , gabelförmige  Stange,  Gabel,   Querholz';   ob   hierher  varius  ,manni| wechselnd,  verschieden,  bunt*,  variö,  -are  , mannigfach  machen,  bunt ob  vielleicht  in  ai.  ürü-  m.  , Schenkel,  Lende'?  "^
1109
Erweiterungen  der  Wurzel  scheinen,  meist  mit  der  Bedeutung  ,geboo-eii sein',  vorzuliegen   in   den  Wurzeln   uät-,  udg-,  uek-,  udk-^  uengQi)-,  u^k-. WP.  I  212,  WH.  II  734  f.,  Majrhofer  1,  116.
=== leaf 353
legung  einer  Bürgschaft Berufung  einlegen',  ags.  weddian  , Vertrag  machen,  versprechen,  verheiraten' [weres  weddian  ,sich  einem  Manne  verloben',  engl,  wed  .heiraten'),  mhd. wetten  , Pfand  geben,  Strafgeld  entrichten,  wetten',  nhd.  wetten^
lit.  vädas  , Pfand,  Bürge',  vaduoti  (lett.  vaduot)  , etwas  Verpfändetes  ein- lösen', uz-vaduoti  ,für  jemanden  eintreten'.
WP.  I  216  f.,  WH.  II  735  f.
Idh-y  U9dh-  ,gehen,  schreiten';  uadhom  ,Furt^
Arm.  gam  ,ich  komme' ;  lat.  vädö,  -ere  .gehe,  schreite',  vadum  , seichte Stelle  im  Wasser,  Furt'  (davon  alb.  va,  Gen.  vau  ds.),  vädö,  -äre  .auf einer  Furt  übergehen,  durchwaten';
aisl.  Aor.  Präs.  vada  st.  Vb.  .gehen,  vorwärtsdringen,  (durch) -waten', ags.  wadan,  afries.  loada,  mnd.  waden]  ahd.  watan,  mhd.  waten  ds.;  hierzu germ.  *wada-  ,Furt';  aisl.  vad  n.,  ags.  wced  n.  , Wasser.  See',  gew<sd .Furt',  mnd.  wat  ,seichte  Stelle',  ahd.  wat  ,Furt',  aisl.  vadill  ,Furt',  vgl. nhd.  QN  Salzwedel
WP.  I  217,  WH.  II  723  f.
1110  ,
=== leaf 354
 sdgr  m.  ,Lärm'  (*«t^ö^'-),  illt swögan  ,tönen,  sausen,  brüllen',  sweg,  swxg  m.  ,Lärm,  Klang',  as.  $wi^^(m , rauschen',  holl.  zwoegen  , stöhnen';  tiefstufig  wohl  aisl.  svagla  ,plätschtni*t arn-sügr  ,das  Rauschen  des  Adlerflugs';
lit.  svageti  ,tönen',  lett.  svadzet  ,rasseln';
für  isl.  sukka  ,lärmen',  daneben  svakke,  ist  jedoch  Vergleich  mit  BOfWt dial.  seykia  ,bellen'  und  lit.  saugti  , eigenartig  singen',  alit.  sugti  ,betikly winseln',  lett.  sudzet  ,klagen',  sükstities  , seufzen'  (daneben  ^-Formen  wit  Bti saukill  durch  Einfluß  von  kaukti  ,heulen',  §aükti  , schreien')  untar  M|^» *s(e)ug-  möglich;  got.  sioegnjan  ,frohlocken'  könnte  auf  Grund  von  yif»» swög-j  swag-  als  Schall  wort  ins  Leben  gerufen  worden  sein;  das  -Wf-  » aisl.  sukka  ist  intensivierend.
WP.  I  214  f.,  WH.  II  725  f.
uai  Interjektion  ,wehe!',  uai-lo-s  ,Wolf'.
Av.  vayöi,  avöi,  ävöya   ,Avehe'!  (yoya-  ,Wehruf'):  arm.  vay  ,Weh^
IUI
glück'  (v-  statt  g-  aus  idg.  u-  durch  nebenherlaufende  NeuscLöpfung); ähnlicb  gr.  öd  (wie  lat.  vah!)  uad  seit  alexandrinischer  Zeit  ovd,  ovä,  oiai^ ^crr.  ßai  (Neuschöpfungen);  alb.  vaj  ,Leid,  Klage';
=== leaf 355
hwäche,  Krankheit'.
WP.  I  213 f.,  WH.  II  789  f.,  Loth  RC.  39,  417.
\ikä  ,Kuh'  ?
Ai.  vasä  ,Kuh  (die  weder  trächtig  ist,  noch  ein  Kalb  nährt)',  väsitä »rindernde  Kuh;  brünstiges  Tierweibchen  überhaupt';  lat.  vacca  ,Kuh': lat.  -CG-  wäre  als  Konsonantendehnung  in  Tiernamen  verständlich.
WP.  I  214,  WH.  II  722.
'3i-  ,ual-d(h)-  ,stark  sein'.
Lat.  valeö,  -ere  ,bei  Kräften  sein,  stark  sein;  gelten,  vermögen',  osk.  J^aXs
1112
```


## [2026-10-17T00:01:13.394Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 357 358 359; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt | grep -o \"11[0-9][0-9]\\s*$\" ; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt | head -c 600; done; grep -n \"uer-5\\|Root / lemma: uer-5\" POK_full.txt | head"
}
```


### [2026-10-17T00:01:13.757Z] TOOL RESULT

```
=== leaf 357
1115
*-om),  got.  w;eis^   ahd.  xoir    »ij ver,  ags.  ?üI  usw.,  hitt.  ues  (*uei-es),  toch.  B  ives,  A  it?as  ,wi^^
WP.  I  220,  Trautmann  344,  Vasmer  1,  175  f.,  Liebert,  Idg.  PersoniL pron.  102  ff.  -  ""  ****
"2.  ue-,  uedb-  , flechten',  s.  oben  S.  75  f.
S.  ye-,  U9-  , blasen^  wehen*,  s.  oben  S.  82 ff.;  ebenda  ue-lo-,  ue-s-,  uet-  Am
4,  ue-,  uo-,  ues-  , herab',  s.  oben  S.  73.  l
5.  ue-,  uo-  ,jener*,  s.  oben  S.  75.  ---
uebh-
1.  , weben,  flechten,  knüpfen*.
Ai.  ubhndtij  umbhdti,  undhdhi  , schnürt  zusammen*,  mit   dpa-  und  pf4* === leaf 358
  vamboU^  lett.  vambale,  vambuole ^Mistkäfer').
WP.  I  257  f.,  WH.  II  733,  Trautmann  336,  Vasmer  1,  176;  hierzu:
jed-  s.  2.  uedh'.
1.  uedh-  jStoßen,  schlagen';  uedh-ri-s  ,verschnitten^
Ai.  vadhati,  dvadhit  ,schlagen,  stoßen,  vernichten^,  Kaus.  vadhayati, vadhd-  m.  ,tÖtend,  Mordwaffe  (bes.  von  Indras  Geschoß);  Schlag,  Ver- nichtung' =  av.  vada-  m.  ,Keil  zum  Spalten  des  Holzes',  ai.  vddhar-  n. ,Mordwaffe  (bes.  von  Indras  Geschoß)'  =  av,  vadar-  n.  ,Waffe  (zum Schlagen)',  vddhram  , Lederriemen',  ai.  vadhasnd-  m.  ds.,  av.  väd=== leaf 359
1117
lösen,  loskaufen**  g.  ob«^ S.  1109;  aksl.  vo^dq,  voditi  , führen',  aruss.  voditi  ^enu  ,eine  Frau  beütt« führen*.
Dazu  wohl  ued-mno-,  das  Wort  für  den  Kaufpreis  der  Braut:
Gr.  eövov  (für  *J^edvov  mit  Spir.  asper  nach  *fhadvg  jangenehm'),  bota, PI.  esdva  , Brautgabe*;  aber  auch  , Aussteuer  der  Eltern*,  id^öcoy  hom.  UMm , ausstatten,  verheiraten',  hom.  hdvibrrjg  ,der  (die  Tochter  ausstattende)  Val#f der  Braut',  &v-äedvoq  ,vom  Bräutigam  unbeschenkt*  {di[f']advog  und  JT/V edvov  mit  a  und  s  als  Vorschlagvokalen);
ags.  weot84282:Root / lemma: suer-5 
90484:wehrt', Avestan varanavaiti ^be6ecVX hijllend' (eontain partly Indo Germanie *uer-5), das 
91145:Note: extension from uer-5. 
91991:Root / lemma: uer-5 {* huer-5) 
92286:with metathesis gr. £u- (as in supioKw, uer-4; compare supuai- under uer-5) in £upu(;
```


## [2026-10-17T00:01:18.891Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91985,92000p POK_full.txt; grep -n \"^u[e]r-\\|uer-.*cover\\|bedecken\\|wer-.*cover\" IEC.txt | head -40"
}
```


### [2026-10-17T00:01:19.337Z] TOOL RESULT

```
*uref-\n Lithuanian su-resti, surecau' catch, grasp', Old Church Slavic obrest/l\n6', sh- 
rest/l\n6, encounter, meet', Aor. -retb (present -r^stg), Oit'-ri^s/^'Erfindung'. 

References: WP. I 280, Vasmer 2, 244, Frisk 589 f. 
Page(s): 1 1 60 

Root / lemma: uer-5 {* huer-5) 

Meaning: to close, cover; to guard, save 

Material: A. With Prafixen: 'shut' and 'open'; 'door'; uortom' gate'. 

Old Indie ap/-vrndt/\ersc\r\\\eQ>t, bedeckt', apa-vrnot/^ off net'; also Latin operio 
'bedecke', aper/'o ^ off ne' (from *op{/)- and *ap(o)-uerid)\ Oscan i/e/i/'portam', Umbrian 
verof-e^\n portam', Oscan vereiasQen. Sg. 'Jungmannerbund' (originally 'Torwache', 
VetterGI. 29, 240); 
3374:dhuer- (2) Skt. dhváràmi “fell, hurt, kil; Hitt. duwarna- ‘shatter’. (The Skt. form dvarami ‘obstruct, cover' is as problematic as dvar "door" in its consonantism. Li. dvérstu, dvérti “extend, expand" is of uncertain origin. Isophonic is MHG ge-twér “mixture; temperature")
7808:krop ‘torture’; R kropát, v. ‘botch, mangle? kraps- ‘grab, snatch; rapacious; grab, sei- zure’ Br. krafa ‘seize, snatch; scratch, engrave’; kraf ‘seizure’; kraf, m. ‘stylus’: kraf, krav ‘stitch’; W craff ‘quick, keen; secure’; m. pl. -au ‘clasp, cramp’; craffu, v. ‘secure, grip’; Cor. crafa, v. ‘grip’; crāf, adj. ‘tenacious’; s. pl. crafow "basting-stitch"; cf. crefny, adj. ‘grasping, gree- dy’; OE hrespan ‘strip, despoil’; hresp ‘spolia- tion’ krās- (?) ‘glory, praise’ ON hrósa, v. ‘praise’; hrósan, f. ‘praise; boast- ing’; hræsni, f. id.; mod. Icel. hrós, n. ‘praise’; OCS krasa ‘beauty’ (and com. Sl.); Latv. cf. krāšns 'splendid'. See Supt. K : krās- (krast-, see karst-). Variant in W cras ‘toasted, parched, arid’; Br. kraz, id. krateið ‘overpower’. See kratos Gk. kratéo ‘rule’; OCS krostọ, krotiti (tame' and com. Sl.) kratos, is, us “strong; strength, power, force’. WP I, 354 Skt. krátuh “power, will, ability’; Av xratus ‘wisdom’; Ober xraQu-, id.; Gk. kratüs *power- ful”; krátos, n. ‘power’; W crad, craid, m. (“vig- our, force’, fr. *kratos, *kratis); OHG hrad ‘swift; OE hrad “swift, active; ON hraór, id.; OCS cf. krotükü ('tame', lit. overpower- ed"). Isophonic: Li. kratüs (rough, uneven’ krátos, à, is 'enclosure, envelope” W crawd “coating, surface’; OE hréóa 'goat- skin cover, mantle’; cf. hroó-girela ‘crown’; Li. krótai, krótos, mfpl. "lattice, grille’; Latv. krats ‘cage, prison’. (W and OE ambig.) kratsos, ios (?) Lat. crassus ‘fat, gross’; ON hress “hale, hear- ty’; hressa, Lat v. ‘cheer’ (kraug-, variant of krauk-, q. v.). (WP I, 417, 477 & II, 573) Hes. kraugós ‘woodpecker’; Gk. kraugé ‘croak, caw’ krauk- ‘caw, croak; crow, raven’. (Variant: krauk-) EMAIb. krak, mod. krrak ‘a bird of crow type’; OE hrēa (Crumble in the bowels’? Cf. hream ‘uproar’, fr. *kraukmo-?); Pol. Ukr. kruk ‘raven’; Latv. kraukjs ‘rook’ beside krauklis
12213:(operið ‘cover, enclose’. Prob. for op-uer-, q. v. Lat. operio, ire, v. ‘close’; OCz. opeřu, iti, v. ‘cover’, cf. Lat. cooperið, id.)
14239:quré-, extended form of quer- (2) (cf. plé- in relation to pel-) Lat. cf. creo, pf. crévi, v. ‘grow’; Cz. cf. o-kfeju, inf: -kYát ‘revive, recover; W cf. pri, pl. -on, m. ‘origin’ (phonol. ambig.)
19481:tuor- (1) o-gde of type tuer-, cf. tuer- (2) and tur- (2) “hold, grip”, etc. Arm. cf. Eat, Let (&dog-collar', if fr. *tuorsis); Gk. sorós, f. ‘urm’; OCz. cf. za-tvofen, adj. *enclosed'; zá-tvora, f. ‘enclosure’; OCS za- tvorü, m. id.; za-tvorjo, -iti, v. 'enclose'; Srb. zü-tvor, m. ‘prison’; Li. tvarüs, adj. ‘firm’; sán-tvara, f. “prop; self-control; Latv. cf. tvarts, m. ‘cover, shelter’; pa-tvara, f. asylum; despotism'. Cf. WP I, 751
20025:uer- (1) (uero, io, uro, ið) open, close’. WP I, 280 Skt. várami, v. pp: vrtab, id.; Av. var-, v. ‘cover; Lat. cf. ambig. ap-erio, erte, v. ‘open’; cop- erio, -erire, v. ‘close, cover, hide’; Li. veriü, vérti, v. tr. (9) open or shut — a door or window’; Latv. veru, vērt, tr. ‘open’; (z-gde in) OCS (and com. SL) vro, vréti, v. ‘close’; cf. Cz. ote-vfit, inf. "open": za-vřít, inf. ‘close’. Nominal types: Osc. vereias, adj. f. ʻofa door’; R verejà, f. 'doorpost; Cz. vefeje, f. id.; cf. roz-vera, f. *wantonness'. (Isophones, of un- certain kinship to uer- (1): Skt. long-gde varah “time, turn’; Per. bar, id. beside di-vàr "wall": Romani -var *-times'; Lat. hapax verones, pl. ‘sheets of lead; ON -var, in pris-var ‘three times’; Skt. varah; m. ‘enclosure, space, room’: Av. varo ‘garden’ beside vairis, m. ‘lake’; Medic in Gk. ouéra, f. ‘gardem or sim. Cf. Osc. veru, neut. pl. ‘door’; MIr. farr, pl. fairre, n. -es-st. bedpost; OE wer, m. "wer: ON ver, n. 'fish-weir'; Gk. cf. próra ‘prow’, if for *pro-ueràa)
20026:uer- (2) “look, watch, observe, care for. Verbal type: uereio, cf. uor- (2). WP I, 284 Tokh. wär-, B war-, v. “sense, feel Lat. vereor, inf. vereri, v. ‘regard, revere’; Br. cf. gwéré, pl. -u, f. ‘watchtower, coastguard post; Srb. verem se, inf: verati se, v. ‘keep a look-out, be furtive’; Latv. cf. veros, inf: vērtis, v. ‘watch, look’; cf. vērā ņemt, v. ‘take heed’;
20027:uer- (3) (uero, ið) ‘speak’. Cf. ueru-, uoru-. WP I, 283 Hitt. weriyami, v. “call, invite’; Gk. eíro, v. “say, speak, tell; éromai, v. "ask
20028:uer- (4) (?) *up, upon' Per. bar, adv. & prp. id.; Arm. ger, cpds: gera-, id.; Lat. (?) cf. the hapax: verones plum- bei ‘sheets of lead”
```


## [2026-10-17T00:01:24.708Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"gij\\b\\|gīj\\|gëj\\|gēj\" IEC.txt | head; grep -n \"^uerg\\|^uereg\\|^ureg\\|^urg\\|^uerghe\\|^uerg-\" IEC.txt | head; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"uer- (1)\")) print NR-1}' IEC.txt"
}
```


### [2026-10-17T00:01:25.055Z] TOOL RESULT

```
9946:loghos, à, iom, ios, io ‘lair, bed, resting-place, situation". WP II, 424. See legho, logheió Oss. cf. lägät ‘cave’; Arm. cf. logor “bait, lure’; Tokh. A lake; B leke ‘bed, lair’; Gk. lókhos ‘ambush’; lokhós ‘childbed’; Lokhía, f. ‘god- dess of childbirth’; lokheía ‘childbirth’; MIr. loige, laige; Ir. luighe, f. ‘lying; reclining’; MHG lege, wf. “laying; layer, row, line’; OE lagu, neut. pl. ‘expanse’; f. ‘law’; ON lag, n. ‘stratum’; leg, n. *burial-place'; lega, f. “flying in bed’; R log ‘valley’; po-logij, adj. ‘sloping’; OCS po-logü ‘placing, deposit’; lože 'bed'; Big. log ‘bait’; pò-log “laying-nest, shelter, corrie’; Li. pã-lagas ‘childbed, windshield’; pa-laga, f. ‘windshield’; Latv. pa-lags “sheet. Finn. LW laki ‘law’; lako ‘prostration’. See next
13303:poigh- “mark; marked, motley, doomed'. Cf. poiK-, peigh, peiK- Umb. cf. peia-, peiu, adj. “a colour’; cf. Lat. pio, are, v. (2) ‘defile’; OHG feigi; Du. veeg; OE fag, adj. ‘motley, gay’ beside fæge “marked, doomed, fey’; OCS pégü, adj. ‘motley’; R pégij, id.; Srb. pjega, Cz. piha, f. ‘freckle’; Li. cf. piegma, f. id. ON feigr ‘fated’; Sw. feg ‘cow- ardly, (as OHG and Du.) display extn. of sense “marked?” > ‘doomed’.
20039:uergho, io (1) “annoy, plague, torture’. Cf. uorgh- Skt. cf. upa-valhami, v. & válhe, mp. ‘quizz’; Ir. feargaim, v. "be angry” (here?); MHG wér- gen, sv. 3. ‘strangle’ beside (o-gde) wergen, wv. ('téar', fr. *uorghejo); Li. vérgiu, ti, v. *en- slave’. Nominal types: Ir. fearg, f. (anger. Here?); Li. vérgas, m., vérge, f. ‘slave’; Latv. vérgs, m. id.
20040:uergho (2) (?) ‘come, go’ Gk. érkhomai, v. ‘come’; Lat. (?) vergo, ére, v. ‘incline’
20041:uergo, io (1) “tie, twist, squeeze, strain,
20068:uergh-, uergh- — uéros
138
335
569
583
742
750
802
806
807
834
835
836
837
838
```


## [2026-10-17T00:01:30.026Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20036,20045p IEC.txt | cut -c1-1500; awk 'BEGIN{RS=\"\\f\"} NR-1>=805 && NR-1<=808 {print \"=== leaf \" NR-1; print substr($0,1,300)}' IEC.txt"
}
```


### [2026-10-17T00:01:30.425Z] TOOL RESULT

```
(uereiKa ‘heather’, see uroiK-)
uereio “look, watch, observe, care for’. Cf. uer- (2) and WP I, 284 Tokh. wár-, B war-, v. ‘sense, feel’; Lat. vereor, vereri “regard, revere'; Srb. verem se, verati se, v. ‘keep watch: Latv. cf. veros, vérties, v. “look, watch’; Gk. (z-gde) cf. eüron “have found' Cf. uor- (2)
(uereios, à, see uer- (1))
uergho, io (1) “annoy, plague, torture’. Cf. uorgh- Skt. cf. upa-valhami, v. & válhe, mp. ‘quizz’; Ir. feargaim, v. "be angry” (here?); MHG wér- gen, sv. 3. ‘strangle’ beside (o-gde) wergen, wv. ('téar', fr. *uorghejo); Li. vérgiu, ti, v. *en- slave’. Nominal types: Ir. fearg, f. (anger. Here?); Li. vérgas, m., vérge, f. ‘slave’; Latv. vérgs, m. id.
uergho (2) (?) ‘come, go’ Gk. érkhomai, v. ‘come’; Lat. (?) vergo, ére, v. ‘incline’
uergo, io (1) “tie, twist, squeeze, strain,
Cf. uereio,
uerbó (uorb-, urb-) — uergh-
10
20
=== leaf 805
 Li. Go. bwahan, sv. 6. ‘wash’; OHG thwahan, dwahan; MHG dwahen, twahen; OE pwéan; ON bvá, id.; G dial. zwahen & zwagen, id.; Arm. cf. Sacem, v. “crash, bang, din’; Li. tvak- sið, éti, v. (throb, beat". Semantics of W gol-
tuuos — tuauonos (tuauün-)
20
25
30
35
40
45
1464
chi, inf. ‘wash; beat’; Cz.
=== leaf 806
ig., cf. tuengh- above)
tuer- (1) (run, rush'. Cf. tur- (1) and tuerst-. Lat. ambig. or variant. Cf. trs- (2) Skt. tváre, mp. id.; Lat.? cf. torrens, gs: -entis, adj. & s. “violent, headlong, gush’ beside festinus, adj. ‘hasty’; festino, ar, v. intr. (“hur- ry’, if fr. a type *tuer-stino, cpd. in de
=== leaf 807
hing; rush, haste’. (ambig.) Lat. cf. festinus, adj. ‘hasty’; festino, åre, intr. ‘hurry’; con-festim, adv. “immediately”. (Length of -e- in Lat. uncertain)
tuerst- (2) (tuorst-) ‘firm, fixed; hold, secu- rity’. Lat. ambig. Av. Owarsto, adj. ‘fixed’; Lat. cf. mani-festus, adj. ‘caught redhanded'; in
=== leaf 808
t; tylà ‘silence’, tyleti, v. “be silent. Ambig. in Alb. tinëz, adv. ‘secretly’, if fr. *tuisnidi-)
tuisk- (?) (variant of tuiks-, q.v.) Lat. cf. fiscus, i, m. *olive-press of wicker; strainer; moneybag' beside fiscína, f. “basket, bag’; Cor. (?) tysk, pl. -ow, mf. ‘bunch’; OCS tisků, m. *wine-press
```


## [2026-10-17T00:01:34.404Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"uergo, io (1)\" IEC.txt; awk 'BEGIN{RS=\"\\f\"} index($0,\"uergo, io (1)\") {print \"leaf \" NR-1; print $0}' IEC.txt | head -150 | grep -n \"Per\\.\\|^1[56][0-9][0-9]\\|uergo\\|uerg\" "
}
```


### [2026-10-17T00:01:34.754Z] TOOL RESULT

```
20041:uergo, io (1) “tie, twist, squeeze, strain,
4:uer- (4) (?) *up, upon' Per. bar, adv. & prp. id.; Arm. ger, cpds: gera-, id.; Lat. (?) cf. the hapax: verones plum- bei ‘sheets of lead”
7:1517
15:uergho, io (1) “annoy, plague, torture’. Cf. uorgh- Skt. cf. upa-valhami, v. & válhe, mp. ‘quizz’; Ir. feargaim, v. "be angry” (here?); MHG wér- gen, sv. 3. ‘strangle’ beside (o-gde) wergen, wv. ('téar', fr. *uorghejo); Li. vérgiu, ti, v. *en- slave’. Nominal types: Ir. fearg, f. (anger. Here?); Li. vérgas, m., vérge, f. ‘slave’; Latv. vérgs, m. id.
16:uergho (2) (?) ‘come, go’ Gk. érkhomai, v. ‘come’; Lat. (?) vergo, ére, v. ‘incline’
17:uergo, io (1) “tie, twist, squeeze, strain,
19:uerbó (uorb-, urb-) — uergh-
27:1518
28:force’. Cf. urĝ- (2). WP I, 290 Skt. várjami, v. pp: varjitah “turn, twist; with- hold, remove’; Tokh. A wárk-, B wark-, v. "be fit, be strong; Hom. Gk. érgo, Gk. eírgo, v. ‘shut; confine, restrain, avert’; Myc. queried wereke(i), 3s. “hems in’; Alb. cf. z-vjerdh, aor: z-vordha, v. (*wean', fr. *dis-9); OCS vrüzo, vrésti, v. ‘tie’; ON verkja, impers. ‘cause pain"; Li. verZü, veřžti, v. ‘squeeze, choke; urge’. Nominal types: Lat. vermen, n. ((2) ‘gripes’, fr. *uer&mn-); ON verkr, gs: verkjar, pl. ver- kir, m. “pain, smarting’. (For Latv. verzeles, pl. ‘trappings’, ON virgill ‘halter’, see uergh-). Cf. Ukr. ot-verezyti, inf. tr. ‘sober’
```


## [2026-10-17T00:01:38.878Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /\\n1599\\n|\\n1598\\n|\\n1600\\n/ {print \"=== leaf \" NR-1; print $0}' IEC.txt | grep -n \"^=== \\|^[a-zA-Zū]*[a-z]-* (\\?[0-9]*)\\? \\|Per\\.\" | head -60"
}
```


### [2026-10-17T00:01:39.214Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:01:41.590Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^159[0-9]\\|^160[0-9]\" IEC.txt | head; grep -n \"^15[2-9][0-9]$\" IEC.txt | tail -5"
}
```


### [2026-10-17T00:01:42.151Z] TOOL RESULT

```
20448:1550
20457:1551
20471:1552
20479:1553
20494:1554
```


## [2026-10-17T00:01:45.123Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20494,20700p IEC.txt | grep -n \"^[0-9]\\{4\\}\\|Per\\. \\|uerĝ\\|urĝ\\|ureĝ\" | head -60; wc -l IEC.txt"
}
```


### [2026-10-17T00:01:45.446Z] TOOL RESULT

```
1:1554
20498 IEC.txt
```


## [2026-10-17T00:01:50.333Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ur[gĝģ]\\|^ure[gĝ]\\|^uro[gĝ]\" IEC.txt | cut -c1-600; grep -n \"giddy\\|dizzy\" IEC.txt | cut -c1-300 | head"
}
```


### [2026-10-17T00:01:50.782Z] TOOL RESULT

```
3188:dhrm- ‘excite, scare; be scared’. WP I, 845 Lat. cf. form-do, -idinis (“bogey”, if fr. *dhrm- ueido-?); MHG türmen "be giddy; rave, rage’; Srb. drmam, -ati ‘shake, shudder’; Slovak drmat ‘bang, clatter’; Cz. cf. drmolit ‘to jab- ber’. (Isophonic with Icel. dorma ‘to doze’)
3346:(dhüsolos, dhüsoros. See next and dhusəlos) Skt. dhüsarab 'dust-coloured, grey’. (Iso- phonic: Du. duizelen "be dizzy'. Isophonic radical in OCS dy$o, dyxajo “blow, breathe’; Li. dusauju and düstu 'gasp)
3354:dhüso, ið (2) *drowse, faint’. (Same as (1) ?) OFris. dusia "be dizzy’, LG düsen ‘daze, be- fuddle; be dazed'; ON dúsa ‘be calm? beside dús ‘lull’; Mod. dúsa *dummy comforter’; Sw. dusa ‘slumber; OHG cf. tūsig ‘mad’; OE dysig ‘foolish’; E dizzy; Li. düstu & dunsu, dusti (2) ‘go bad, decay; go o
9278:Arm. Srtnum, aor. Srteaj (1) “start, jump, swerve, be dizzy’; Slovene svéder 'gimlet' be- side (long-gde) Pol. świder, Cz. svider, id. (& *drill); Li. švidras ‘whirlwind, blizzard" strident creature’ Gk. sízo ‘hiss, squeak’; sígion “tree-cricket'; OE cf. hwic-ung, sf. ‘squeak’; E dial. cf. to w
12771:perperos ‘flighty, giddy’. Cf. peros (2) Gk. pærperos, adj. ‘fickle, rash, vain’; Lat. per- perus, id. cf. also perperam, adv. 'rashly, vain- ly’; Per. farfar, s. “hurry”
17925:time’; be-swich, m. (1) ‘departure’; OE swican, sv. 1. (1) *wander, MLG (z-gde) swicken, v. ‘hop; wind, bind’; Du. zwikken, v. “get sprained, be wricked'; zwik, m. 'sprain'; E to switch, v. ‘to change"; Icel. cf. svikull, adj. 'elusive'; Cz. (initial variant) švih, m. ‘élan, dash” beside svižn
```


## [2026-10-17T00:01:58.364Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-17T00:01:58.374Z] TOOL RESULT

```


```


## [2026-10-17T00:02:00.355Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گیج",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:01.053Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/دیوار",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:01.605Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بهرام",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:02.258Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/فروردین",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:03.823Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wer-",
 "prompt": "List the senses/homonyms of *wer- and, for the one meaning 'to cover/close', give its derivatives (esp. Indo-Iranian, Avestan vara-, varəθra, Latin aperio/operio, Germanic warn)."
}
```


### [2026-10-17T00:02:06.975Z] TOOL RESULT

```
# Persian Etymology Section

From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭯𐭫𐭥𐭫𐭲𐭩𐭭](/w/index.php?title=%F0%90%AD%AF%F0%90%AD%AB%F0%90%AD%A5%F0%90%AD%AB%F0%90%AD%B2%F0%90%AD%A9%F0%90%AD%AD&action=edit&redlink=1 "𐭯𐭫𐭥𐭫𐭲𐭩𐭭 (page does not exist)")_ (plwltyn /⁠Frawardīn⁠/).
```


### [2026-10-17T00:02:08.051Z] TOOL RESULT

```
# Persian Etymology Section

Cognate with Bakhtiari _گێز_ (gız, "mad"), Northern Luri _گێژ_ (gıj, "mad"), Dezfuli _گیز_ (geyz, "dizzy; confused"), Northern Kurdish _gêj_ ("dizzy"), and Sogdian _kyc_ (/⁠kēč⁠/). The entry also notes Iranian borrowings in Middle Armenian _գիժ_ (giž), Middle Georgian _გიჟი_ (giži, "crazy, mad; foolish"), Assyrian Neo-Aramaic _ܓܫ̰ܘܢܐ_ (gežūnē), and Udi _ҝиж_ (gʲiž).

The source states: "The Persian is probably borrowed from a Northwestern Iranian language, rather than inherited."
```


### [2026-10-17T00:02:09.547Z] TOOL RESULT

```
# Persian Etymology Section

The Persian etymology section states that دیوار is "[Inherited](/wiki/Appendix:Glossary#inherited "Appendix:Glossary") from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[dywʾl](/wiki/dyw%CA%BEl#Middle_Persian "dywʾl")_ (/⁠dēwār⁠/, "wall"), from [Old Persian](https://en.wikipedia.org/wiki/Old_Persian "w:Old Persian") _[𐎮𐎡𐎭𐎠](/w/index.php?title=%F0%90%8E%AE%F0%90%8E%A1%F0%90%8E%AD%F0%90%8E%A0&action=edit&redlink=1 "𐎮𐎡𐎭𐎠 (page does not exist)")_ (di-i-d-a /⁠didā-⁠/, "wall, fortress") + _[\*-wāra](/w/index.php?title=Reconstruction:Old_Persian/-w%C4%81ra&action=edit&redlink=1 "Reconstruction:Old_Persian/-wāra (page does not exist)")"

The section also includes comparisons to related terms in Avestan and Ancient Greek, demonstrating the word's Proto-Indo-European origins through multiple language families.
```


### [2026-10-17T00:02:09.575Z] TOOL RESULT

```
# Proto-Indo-European Root *wer-

Based on the Wiktionary entry, **\*wer-** has three distinct homonymic senses:

## The Three Senses

1. **"to burn"** – with alternative reconstruction \*werH-
2. **"to sense; to note"** – meaning to perceive or observe
3. **"squirrel or marten"** – an animal noun

## Derivatives for "to sense/note"

The entry documents extensive descendants across language families:

- **Indo-Iranian**: Sanskrit वृ॒णोति (vṛṇóti) via the néw-present formation
- **Germanic**: \*wardaz ("guard; keeper"), \*warōną ("to watch; to protect")
- **Hellenic**: Ancient Greek ὁράω (horắō, "to see") and related forms
- **Italic**: Latin-derived forms via Proto-Italic \*werēōr
- **Celtic**: Old Irish feraid ("to grant; to provide")
- **Albanian**: vërej ("to look; to observe")

The entry notes that "to sense" meanings evolved into "to guard/watch/protect" concepts across descendant languages, reflecting the semantic connection between observing and protecting.
```


### [2026-10-17T00:02:09.875Z] TOOL RESULT

```
# Persian Etymology Section

The etymology section states that بهرام comes "From Middle Iranian (see Parthian _𐭅𐭓𐭉𐭇𐭓𐭌_ (wryḥrm /⁠Wahrām⁠/, 'war god, god of victory')" and Middle Persian forms, ultimately deriving from Avestan _𐬬𐬆𐬭𐬆𐬚𐬭𐬀𐬖𐬥𐬀_ (vərəθraγna, "smiting of resistance, victorious").

The term traces back through Proto-Iranian and Proto-Indo-Iranian ancestry. It is "Related to Sanskrit _वृत्रहन्_ (vṛtrá-hán, 'smiter of _vṛtra_')". The entry notes an interesting linguistic development: in pre-Islamic Iran, the term became "mythologically conflated" with the Persian Gulf region, leading to an "incorrect" folk etymology connection with Bahrain.
```


## [2026-10-17T00:02:14.214Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/aperio",
 "prompt": "Give the Latin etymology section verbatim (incl. the PIE root)."
}
```


## [2026-10-17T00:02:14.982Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/warn",
 "prompt": "Give the etymology verbatim, incl. PIE root."
}
```


## [2026-10-17T00:02:15.582Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cover",
 "prompt": "Give the etymology verbatim, incl. PIE root."
}
```


## [2026-10-17T00:02:16.276Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/aperture",
 "prompt": "Give the etymology verbatim, incl. PIE root."
}
```


## [2026-10-17T00:02:16.868Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بارو",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:17.424Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/برزن",
 "prompt": "Give the Persian etymology section verbatim."
}
```


### [2026-10-17T00:02:18.109Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:02:18.114Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:02:18.118Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:02:19.858Z] TOOL RESULT

```
# Persian Etymology Section

The Persian Etymology section states:

"(This [etymology](/wiki/Wiktionary:Etymology "Wiktionary:Etymology") is missing or incomplete. Please add to it, or discuss it at the [Etymology scriptorium](/wiki/Wiktionary:Etymology_scriptorium#بارو "Wiktionary:Etymology scriptorium").)"

In other words, no etymological information is provided for the Persian word بارو on this page.
```


### [2026-10-17T00:02:21.469Z] TOOL RESULT

```
# Persian Etymology Section

The Persian etymology section states:

"Borrowed from Northwestern Iranian, from Proto-Iranian [Term?]."

This indicates the word derives from Northwestern Iranian languages and ultimately from Proto-Iranian, with the source note indicating incomplete etymological documentation.
```


### [2026-10-17T00:02:22.262Z] TOOL RESULT

```
# Latin Etymology of "aperio"

The word **aperio** derives from Proto-Italic *apweriō (or *apwerjō), which comes from Proto-Indo-European roots: "*h₂epó" ("off, from") plus "*h₂wer-" ("to cover, shut") with the suffix "*-ye-".

The entry notes cognates across multiple languages including Sanskrit अपिवृणोति (apivṛṇoti, "to close, cover"), Oscan veru ("door"), Ancient Greek ἀείρω (aeírō, "to lift, raise"), Lithuanian atvérti ("to open"), Proto-Slavic *ot(ъ)verti ("to open"), and Old Armenian գեր (ger, "above, hyper-"). It is also related to the Latin verb operiō ("to cover").
```


## [2026-10-17T00:02:25.222Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/warn",
 "prompt": "Give the English etymology verbatim incl. PIE root."
}
```


## [2026-10-17T00:02:25.936Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/cover",
 "prompt": "Give the English etymology (verb) verbatim incl. PIE root."
}
```


## [2026-10-17T00:02:26.581Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/فروهر",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:27.229Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/پروار",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-17T00:02:28.712Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/fravasi-",
 "prompt": "What does the article say about the etymology of fravaši (fravarti), its derivation from var- 'choose' vs var- 'cover/protect', and the month name Farvardīn (fravašinąm)? Quote key sentences."
}
```


### [2026-10-17T00:02:29.973Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:02:31.230Z] TOOL RESULT

```
# Response

I cannot provide the Persian etymology section verbatim because the webpage content shown only includes the **Urdu** section of the Wiktionary entry for "پروار". 

While the page indicates that this term exists in 7 languages (including Persian/فارسی), the actual Persian language entry is not displayed in the provided content. To access the Persian etymology, you would need to visit the Persian Wiktionary directly via the link shown on the page.
```


### [2026-10-17T00:02:31.522Z] TOOL RESULT

```
# Persian Etymology Section

**Etymology 1:**
"Inherited from Middle Persian [Book Pahlavi needed] (plwʾhl /⁠frawahr⁠/), from Old Persian *fravarti-. Compare Avestan" faruu­ahara.

**Etymology 2:**
"Inherited from Middle Persian [Book Pahlavi needed] (plwʾhl /⁠frawahr⁠/), via its later form frōhr (attested in Pazend as frōhar)."
```


### [2026-10-17T00:02:31.590Z] TOOL RESULT

```
# English Etymology of "Warn"

According to the Wiktionary entry, the word "warn" comes from Middle English _warnen_, derived from Old English _warnian_ ("to take heed; warn"), which traces back to Proto-Germanic _*warnōną_ ("to warn; take heed").

The ultimate root is Proto-Indo-European _*wer-_ meaning "to be aware; give heed."

The entry notes cognates across Germanic languages, including Dutch _waarnen_, German _warnen_, Swedish _varna_, and Icelandic _varna_.
```


### [2026-10-17T00:02:32.854Z] TOOL RESULT

```
# English Etymology of "Cover" (Verb)

From Middle English *coveren*, borrowed from Old French *covrir, cueuvrir* (modern French *couvrir*), from Late Latin *coperire*, from Latin *cooperiō* ("to cover completely"), from *co-* (intensive prefix) + *operiō* ("to close, cover").

The root *operiō* derives from Proto-Indo-European *h₁ep-*, with further connections to *h₁épi* ("near") and *h₂wer-* ("raise"), combined with the suffix *-yeti* (forming verbs).

[WebFetch note: this page's text is 235836 characters long and the answer above covers only characters 0 to 100000; the final 135836 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-17T00:02:53.955Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"gēj\\|gij\\|gīj\\|giž\\|gēž\" CHEUNG.txt HRN.txt HUB.txt | head -20; grep -n \"u̯aiǰ\\|u̯ai[jǰ]\" CHEUNG.txt | head"
}
```


### [2026-10-17T00:02:54.275Z] TOOL RESULT

```
HRN.txt:9441:phlv.-päz. hargij bezw. hargiz (PPGl.), püz. hargizi.
```


## [2026-10-17T00:02:57.278Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^\\*u̯\\|^\\*u\" CHEUNG.txt | head -80 | cut -c1-120; grep -n \"گیج\" MON_part*.txt BQT_v*_pages.txt incoming/BQT/BQT_v*_pages.txt incoming/ARY/ARY_pages.txt 2>/dev/null | head"
}
```


### [2026-10-17T00:02:57.725Z] TOOL RESULT

```
390:*uH respectively. Other implications are that a root cannot begin with a vowel or 
1742:*uzbàraiiat (У 18.10), 1р1. YAv. ham.baraiiama (V 19.44 Ё), OPT. 3pl. YAv. uzbäraiion (Yt 8.58, Yt 
4068:*ui-) BMP wyd’n /wiyan/ ‘tent’, MMP wy’nm’n ‘nomad, iss’. 0 On the 
4709:*u as stem vowel, may either derive or show influence from nominal *duma- (Skt. 
8179:*ui-) wzw- ‘to die (of plant); go out, be extinguished (of lamp)’, wz’w- (caus.) ‘to 
8633:*uz-) ‘zgyrw- ‘to take out’, 'zerysp- (pass./inch.) ‘to be removed, taken away, out’ || 
9287:*ul-xSar-) 
9707:*upa-) ‘to recite; to have an oral agreement’ || (+ *pati-) ‘to recall; long for’ || (+ 
10763:*upa-) ‘to go to, arrive at’ || (+ *upari-) ‘to behave, conduct one’self || (+ *niZ-) ‘to 
11612:*uz-) ‘to protect’ — Liste: 14 
11622:*ud-avaya-, the dental ought to have disappeared, becoming either -y- or -h-. 
14546:*ui- ?) Ard. viyu, Gz. viya, Tr. veya ‘separate’ 
14585:*us- ?) Yzgh. Soxs-/Soxt ‘to get accustomed to, get spoiled, learn? 
16948:*uz-) SSogd. zm’, CSogd. zm’y ‘to tempt’ || (+ *pati-) BSogd. ptm’k, ptm’’k, 
18162:*upa-) ‘to call upon’ || (+ *pati-) ‘to answer, reply’ || (+ *fra-) ‘to proclaim’ || (+ 
19503:*us-) LKh. uspurra- ‘full, completed’ || (+ *ham-) OKh. hambir- (etc.) ‘to be filled 
19850:*us-paua- from an IE root *peu- ‘to run’ (presumably the unenlarged root of 
20311:*upa-raisa-Ci- ?) 
22418:*ui-) LKh. bitcafi- ‘to break up’ = SGS: 28, 145, 53, 96 
22639:*upa-) ? Sh. bixsar-/bixcud ‘to ladle, scoop up (grain, fluid)’ || (+ *pati-) (?) Sariq. 
22729:*us- and removed accordingly ? || Chor. m/Skwnd- ‘to earmark’ has a peculiar, 
23056:*upa-hispar-), MSogd. pspr’mndyy ‘fixing’ (GMS: §1100) || (+ *ni-) BSogd. ’nspr- 
23194:*upa-) ‘to lean upon [intr.]’ || (+ *ni-) ‘to bring to, assign’ — Liste: 66 
23224:*ui-) ? Pash. waxedal ‘to slip (from the hand)’, Sh. (Baj.) wixi(y)-/wixid, Rosh. 
23545:*upa-) Arm. (LW) apastan ‘refuge, resort’ || (+ *us-) Par. ust-, Orm. (w)ust- ‘to rise’ 
24192:*upa-) ‘to reside’ — Liste: 69f. 
26104:*uab/f ‘to weave’ 
26158:*uaá ‘to say, speak’ 
26202:*us-fra-a-) CSogd. sfr’cy (m.) ‘speech, word’ (cf. Schwartz 1967: 126) || (+ *pari-) 
26262:*uadH ‘to slay’ 
26325:*uah? *to venerate, implore, pray' 
26367:*uaHr- ‘to rain’ 
26425:*uai ? ‘to cut off, sacrifice ?' 
26507:*uaid! ‘to know? 
26531:*uaid2 409 
26659:*uaiH 411 
26684:*uaiH ‘to hunt, chase; to run’ 
26778:*uaij 413 
26820:*uaij ‘to shake, swing’ 
26894:*uais 415 
26897:*uaip ‘to swing, shake’ 
26930:*uais ‘to enter’ 
26979:*uais ? ‘to be concerned, occupied; to work for ?' 
27003:*uaiZd ‘to raise’ 
27026:*uamH ‘to vomit’ 
27049:*uan ‘to triumph, win’ 
27096:*ua(n)é ‘to stagger, shake ?' 
27146:*uar 419 
27163:*uap? ‘to shave’ 
27179:*uar ‘to turn’ 
27239:*uar(H)! ‘to choose; convince; (med.) to believe’ 
27316:*uar(H)? *to mix, mingle' 
27351:*uarz. || Although referring to Humbach, l.c., Kellens — Pirart II: 299 rather translate 
27387:*uart 423 
27507:*uarz 425 
27627:*uat 427 
27634:*uas ‘to want, wish’ 
27669:*uat ‘to inspire, be informed, acquainted’ 
27712:*uaxš ‘to grow; increase’ 
27802:*uaz ‘to carry, drive (chariot, vel sim.) 
27805:*uz-) ‘to carry, transport up’ || (+ *pati-) ‘to drag back’ || (+ *para-) ‘to fly away 
27943:*uàs ‘to make a noise (roar, shout, vel sim.)' 
27981:*ui(H)z ? 433 
28003:*uaz? ‘to play, contend; [pass. ?] to lose (in games)’ 
28031:*ui(H)z ? ‘to venerate ?° 
28050:*uindar (*urndar ?) ‘to stand; (caus.) to establish’ 
28069:*uiaé ‘to contain’ 
28098:*uiaH ‘to cover, wrap’ 
28115:*urad 435 
28138:*ujeH;. ‘to braid, wind’ (Lat. viére ‘to bind, to plait’; Lith. vun ‘to twist’; OCS 
28152:*urad ‘to soften (> to boil)’ 
28180:*uraid ? ‘to blame, condemn’ 
28213:*uraiH ‘to crush, push down’ 
28224:*urais 437 
28236:*urais ‘to turn, spin’ 
28298:*uraj ‘to go forth’ 
28319:*urad ‘to become enthousiastic, joyous ?’ 
28334:*uraz ‘to be proud, haughty / to entertain, regale ?’ 
29338:*upa-) ? Yi. fxa-, M. fxaw-/fxevd ‘to shear sheep’ || (+ *ui- ?) (pass./intr.) Oss. I. 
29745:*uz-auga- Y Ау. aog- ‘to speak’, which is to be discarded. Note the additional 
incoming/ARY/ARY_pages.txt:5481:چم اين واژه در لاتین و زبان‌های رومانس: گیجگاه» شقیقه.
incoming/ARY/ARY_pages.txt:5725:چم این واژه در زبان لاتین و برخی زبان‌های اسلاوی: بی‌حساگیج و بی‌حال.
BQT_v1_pages.txt:24164:بتطیح - با لامبروزن زنگیجه:بمعنی
incoming/BQT/BQT_v3_pages.txt:25330:‏۴ -قی : ساننکریت ‎katara‏ ( ترسو » کمرو »گیج ؛ مضطرب)«وبلیامز ۴۱:۲۷
incoming/BQT/BQT_v3_pages.txt:27052:زده » بمعتی ‎Obl‏ وابله - وس کشته وگیج(۱) | است ‎٩‏ .
incoming/BQT/BQT_v3_pages.txt:27064:(۱) چش : -گیج .
incoming/BQT/BQT_v3_pages.txt:43712:‏گ رگیج ۴ 0 ‎SG‏ اولوسکون
incoming/BQT/BQT_v3_pages.txt:49334:‏عمه با حیزان حیز و حمه باگیجان گیج همه با دزدان دزد وهمه با شنگان شنگه»
incoming/BQT/BQT_v3_pages.txt:49338:: ‏حاصل مصتر ) [ رك‎ ots ) ۰+) ‏(قي : گیجید,‎ oS: ‏مر کب است از‎ an, ‏و دوارس‎
MON_part1.txt:3375:متحیر. گیج» شه هه نع نوان:
```


## [2026-10-17T00:03:01.968Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26820,26895p CHEUNG.txt; sed -n 49320,49345p incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-10-17T00:03:02.359Z] TOOL RESULT

```
*uaij ‘to shake, swing’ 

*AVESTAN: YAv. vij- ‘to shake, swing ?' || (+ *fra-) YAv. frauuaeya- “swinging 
forward’ (Yt 10.96, Yt 10.132) || (+ *ni-) ‘to swing down(wards)’ = Liste: 54 

Partic.: pres. YAv. vaéjant- (? Yt 19.92, ? F 431), perf. pass. YAv. -niuuixta- (Yt 6.5) 

*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to swing, fling, sprinkle’ || (+ *ui-) MMP 
whyz-, ВМР wyhyc- /wihéz-/ ‘to move, progress, set out’. 0 On the etymology of 
MMP whyz-, BMP wyhyc- see Nyberg 1974 II: 211b. The older etymology of 


Henning 1933: 178 has been rejected by Nyberg. > DMMPP: 342b 
Pres.: IND. 3sg. ВМР wycyt /wézéd/, 3р1. BMP wycynd /wézénd/; Inf: BMP wyhtn /wextan/ || (+ *ui-) 
Pres.: IND. 3sg. MMP whyzyd, 3р1. BMP wyhycynd /wihezend/ 


*PARTHIAN: (+ *ati-) 'dwyxs- ‘to shake (the head)’ > DMMPP: 25b 


414 *uaij 


(+ *ati-) Pres.: IND. 3pl. 'dwyxsynd {hapax} 

*SOGDIAN: BSogd. wyc, CSogd. wyc ‘to move, shake [intr.]’ || (+ *apa-) BSogd. 
pw’yc- ‘to shake, be agitated’ || (+ *a-) ? BSogd. ’’wys ‘to confuse, disorder’, 
CSogd. ’wyZ ‘to become agitated, angry’ || (+ *pati-) ptw’yc ‘to shake, be agitated’. 
© On CSogd. ’wyz "The etymological possibilities are numerous", Sims-Williams 
1984: 149. 

Pres.: IND. 3sg. BSogd. wyct, 3р1. BSogd. wycnt, CSogd. wycnt, SUBJ. 3sg. BSogd. wyc’t, Partic.: pres. 
BSogd. wyc’y || (+ *apa-) Pres.: SUBJ. 3sg. BSogd. pw’yc’t || (+ *ä-) Impf.: IND. 35р. CSogd. "wyZ 
Partic.: perf. pass. BSogd. "wystk ‘ksubdha’ 

*CHORESMIAN: ? wc- ‘to shake’ (rather from *ua(n)ë ?) = Samadi: 211 

*NWIR: NP bextan/bez- ‘to shake’, Bal. gé(h)t, gétk/géj- ‘to put, swing, turn towards; 
pour into; miscarry, abort’, Zaz. viziyayis/viz(iy)en- ‘to come out, appear’, Yar. 
vast, Isfah. vär-vezän/vär-vez-, Meim. a:-vaft-/a:re-vez-, Mah. wöstän, Natan. är- 
vast ‘to jump, leap’, ? Qohr. vut (pret. stem) “о hang, be suspended’ || (+ *a-) NP 
avextan/avez-, Meim. dar evidz-/dar a-vi:tai- ‘to hang, suspend [intr.]’, Khuns. 
aviz-/aviza ‘to hang on [tr.]’, (inch. ?) ? Kurd. (Kurm.) avasin/awas-, (Sor.) hał- 
awasin/awes- ‘to hang on’ (formally difficult) || 

*NEIR: Oss. I. wigyn/wygd, D. wegun/wigd ‘to shake; wave’, Sh. (Baj.) wuc-t ‘to 
move, stir, go (slowly), rock, swing, shake’, ? (Baj.) wuz-/wuzd ‘to move, stir’ || (+ 
*4-) Oss. I. awynzyn/awygd, D. awinzun/awigd ‘to hang’, ? Sh. avezun ‘to hang’ 
*MISC: ? Arm. (LW) vizem ‘I flow, miscarry’ 

*SANSKRIT: vej ‘to dart up or back, to move up (of a wave), flee, twitch, move 
quickly’ (RV, AV+) = EWAia II: 577 

Q The root is a blend of *yaité and *uaij! according to Nyberg 1974: 210; 
Sims-Williams 1989: 263. It should be noted though that we can distinguish two, 
sharply defined, meanings for an (apparently) single root, viz. ‘to move’ and ‘to 
shake, swing’. This is also found in Germanic: ‘to move’ and ‘to yield, give ground, 
weichen’ respectively. Although, obviously, it is possible that we may still deal with 
one and the same root, it is probably better to reconstruct two different 
(homonymous ?) roots. 

«PIE *ueig- ‘to (start to) swing, shake [vel am IT = LIV: 667 f. | Pok.: 1130 f. 

*IE COGNATES: Gr. eixo ‘I yield, give ground’ (with sec. -к-), OE wican ‘to yield, 
give ground’, ON víkja ‘to move, turn; respond, take action’, OHG wihhön ‘to jump, 
leap’, NHG weichen 

*REFERENCES: Christensen, Contributions I: 156, 255; Abrahamian 1936: 133; Lambton 1938: 40a f.; 


Abaev, Slovar’ I: 87 f., WIM I: 66; EVS: 87b, 96a; Abaev, Slovar’ IV: 108 Ё; Werba 1997: 376 Ё; Paul 
1998: 317b; Cabolov 2001: 98; Lecoq 2002: 656b; Shahbakhsh: s.v. géj- 


*uais 415 

‎. ‏زره‌بر » نز گوبند « رشیدی » . ظ . از :گی(ه.م.) + بر(برنده)‎ NYT, SY
gétéh ‏پهلوی‎ . gtthi , gétht gett ‏پازد‎ «evry.» 826408- ‏اوستا‎ - ۴
séthih ‏وحالا8#د منای :۲:۲۷ » و 86116 ( دیوی) « سربانی‎ cary ‏ط800 « تب رکه‎ ,
. ‏و قس :گهان . جهان‎ Lal ‏اسمق:‎ : dy ‏و‎ » ۹4٩ ‏موبشمان‎ «
. ‏مصلحتش رهبری کند ایام‎ sais ‏هرآنکه کرد کیتی یکین او برخاست‎ - ۴
.* ۱۱۹ ‏کلتان ص‎ > ۱
.) ‏بان ( پسونه نست و اتصاف‎ + ES: ‏رك :کل کیتی . © از‎ ۴
. ‏پژوهنده ). ۷ - از :کیتی ۲ نورد (نوردنده)‎ ( opt ‏از : کیتی‎ -
: ‏«کیج , ممجب و احمق بود . قربم گنت‎ -

‏گیچیفه ”)2 بروزن پیچیده . بمعنی
دماغ پربشان شده و سراسیم هکشته و سر ردان
وحبران گردیده باشد .

‏عمه با حیزان حیز و حمه باگیجان گیج همه با دزدان دزد وهمه با شنگان شنگه»

‎ON ‏فرس‎ cad?
‏بمعنی گردش سر«رشیدی»‎ » and yo ‏در«‎ - eae . ۷۳ ‏و رك : همان کتاب ص‎
: ‏حاصل مصتر ) [ رك‎ ots ) ۰+) ‏(قي : گیجید,‎ oS: ‏مر کب است از‎ an, ‏و دوارس‎
. 4 ‏پیمد ]. ۰ - اسم مفمول از« کیجیدن‎ ٩۵ ‏ص‎ ot AG ‏ممدر بقلم‎ pel

‏۱ ره : ‎gut,‏ . « ظاهراً همان جالور است که مشابه بود به غلیواج » و آن ‎es‏
‎ce‏ ات « و ‎askin Sa nT se‏ به ها .ون از عم توق
لمانین است.» « سراج اللغات بنقل‌فرهنگه نظام »
[pdf page 666]
NAMA
```


## [2026-10-17T00:03:14.084Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *2. var-\\|^ *1. var-\\|^ *3. var-\\|^ *var- \\|^ *2. vāra-\\|^ *vāra-\\|^ *1. vara-\\|^ *2. vara-\\|^ *vara-\\|^ *varəθra-\\|^ *vərəθra-\\|^ *varəθrağn\\|^ *vərəϑraγn\\|fravaši-\\|frava8i\\|^ *vərəzāna-\\|^ *varədana\" BRT.txt | head -40"
}
```


### [2026-10-17T00:03:14.561Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:03:18.597Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"θraγn\\|ϑraγn\\|9rayn\\|draγna\\|Ѳraγn\" BRT.txt | head -10; grep -n \"fravaš\\|fravas\\|fravaS\" BRT.txt | head -10; grep -n \"vardana\\|varədana\" BRT.txt KNT_full.txt | head"
}
```


### [2026-10-17T00:03:19.018Z] TOOL RESULT

```
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2492:aohqm  saoi:ranqm  vinditayä  mävöya  nipä- rayeinti  .  .  Yt  77.54;  —  vTspanqm/a  att-  • kam   aiaonqm  alaoninqm^a  .  .  ya^qn zaoyasca  fravasayö  Yt./J.i48;    148; .  .  aAmat  haca  nmänilt  .  .  ya^ra  .  .  1 staoiti  Y.io.-j;  —  nbyö  daiiiAubyö  . . ya^-a  ( l'wo')    aim    bavaiti  yaslö    YtÄ47;    /j. 34,  P. /7*;   —    ..  ahmi   nmäne  ..  yaia aAmya  (sv^.  yaAmya)  amtsä  sp^nta  . .  pai-
2873:girfsaite  akur.li ..  uiti  aojanö  Yt/0.53; — yö  aoxta  a/iiiräi  ..uity aojanö''  Yt.  Ä 10;  J0.73,_V.2.io,j.2o;  —  fravasayö  .  .^ uityaojana^'  \\,tj.(>(>;  —  uifyaojana (NPm.)'>  mi>rHi  Yt.ro.41;  —  ätar! . . uiti  vacibii  aojanö  Yt.  19. 49;  5.76;  — ; aus. .uiti  vaülns  aojana  Yt/7.17;  22;i —  bulyqsta  . ,  uiti  aej^mna  uiti  daomna FrW.  10.  42.  2)  'verkünden,  nennen, bezeichnen  ab  — ,  wovon  sprechen  als  — ', mit  dopp.  Akk.:  ratavö  .  .  y5i  (als  AP.) aoxta  ahurö ..zaraiustrrd  yasnylca  i<ahm- yica  "..  die  AA.  dem  Z.  als  verehrungs- und  preiswürdig  nannte"  Vr.  2. 3;  —  staei.l- nm  vatthanhm  aoxta  ahurö  . .  ya'^a  . . V.  ro.9;  —  yi  aastfm  *Ta^aiiA0  (sd.) aog?äJ  (3SPr.)  £am  asibyä  Avaniä  Y._j2. 10.  a)  statt  des  praed.  Akk.  steht  "der Nora.  3*;   yim    m^iyüka    ifil  (sd.)    n<ima
3554:an  Gerechtigkeit,  von  AHM.:  ahurvm  Durch H.pIoL  «us  -M-"«"'''"'"''-.  Superl.  aus mazdqm  ..yS  aÜahe  'mS  Y.57.4;  I.\;  — |  'apayanta- Aiy,  V¥¥.  iam\. yam-;  yant{a-  ist fravaslm  avqm  yqtn  shurahe  mazdä  ,  ,  |  Komp.-Form  zn  ü.  yämi^aväi,  IF.  /,  70. asäi°mqmca'V.26.2.  2) 'der  tüchtigste,  •  j.  apayav-  'der  es  (einem  Geräusch wirksamste"*;  'maya  fiaiti  vacastaitü  "^loxtmA  der  Stimme)  gleichtun  kann' :  _j'£si  .. der  wirksamsten  Strophe"  Y.5Ä 8;  —  °m>m\nSii..aiivi.surum>aiti  apayät{sA.)ym  apsU ra^wqm  H.'i.y, —  °mahe  rakws  Vr.i?.  j  (NS.)'*  aa/  näil  apöis(NS.)'^  iiat*maoTaya 6;  —  ihm  ..at'^rapaitim  upayali  *°m?m^^  *vala  /ramanmnö  ratufris  ", .  wenn  er  es dahmsm  N.  is,  1  gleichtun  kann  (,  ist  er  r^\    wenn  er  es
3849:•  j.  aiivi-S-üra-  Adj.  (fem.  °ra-)  'rings, sehr  siegreich',  von  Gottheiten:  uyrs  'rS ..  w/iSz-J  Yt,  JO.6;  78;  — fravasibyö  ya uyrhca  °rasia  Y.4.6;  Yt  iJ-4o;  — frava- iayö  uyrä  °ra  Y.  6$.  1  a ;  YL  /J.  7  5 ;  — fravaHnam  ttjranqm  °ranam  Y.  i.  18.
4456:•  j.  an-ä'zar^ta-  Adj.  (fem.  °ta-)  'nicht enilmt':  ytzi  sl  bavaitUi  °ta  xsnütä  ainilä al/nsia  .  .  fravasayi  Yt/^.63;  30,  34.
4713:•  j.  anvarJitavas't?ma-<>  Adj.  (fem,  °m3-) etwa  'der  am  will  fahrigsten,  geeignetsten wirkt*:  fravasayö  'tfmä  frascimbananqm ". .  die  geeignetsten  unter  den  StÜUbalken" yt.y.26.
4744:Pü.:  an  /  Jäiaiiän,  erl.:  ii(f)  dj/aiij«  ne  äii  —  fravasayö  . .  ya  . ,  frostisinlc . .  'mint
4770:•  j,  a-mar^xtay-  i)  f.  'Nichtverderben, Freiheit  von  Verderben,  Sicherheit  vor  Ge- fährdung': ya'ha  asitn  "Um  avaiaräni  avi masdä  dumabys  Yt  (?.9;  —  uzbSsau^  paiti 'tun  fravasaile  mihro  "die Arme  umSicher- heit (der  Gläubigen)  emporhebend"'  fährt M.  heran"  Yt.  10.  124,  2)  Adj.  'dem kein  Verderben  droht':  yai . .  Jasät  Jvayö °til "..,  kommen  wird  der  lebendige,  un- gefährdete (näml.  Sao^yani)"  Yt.  75.11.
4800:'von  —  weg',  der  Akk.  zu  ergänzen;  yS  vä adqs..drUa  ayant^m  urvatllii(siL)  vä.. mi'^rsibys  vd  Y.46.$.  3)  mit  Lok.  des Ziels :  fravaSayS  xinüth  ayantu  ahtnya nmäne  YL/j.  136.  Vgl.  auch  Simpl.
KNT_full.txt:2869:vardanam = opj-, GAV. vorozóna, LAV. varozüna-, 
KNT_full.txt:5415:in adánd, vardana-; from plE gh in gaud-, Bar- 
KNT_full.txt:8535:‘city’, generic word not given in OP; vardanam 
KNT_full.txt:12117:place where or within which: DB 1.92 vardanam 
KNT_full.txt:14348:‘fortress, stronghold’, vardanam ‘town’, dvahanam 
KNT_full.txt:17121:Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 
KNT_full.txt:17134:22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 
KNT_full.txt:17212:66 vardanam : Мадалу : avada : hauv : Fravartis : һуа : Madaty : xSdyafiya : a 
KNT_full.txt:17575:5 nā : nama : vardanam : Рагдауају : ауада : hamaranam : akunaus : hada: 
KNT_full.txt:17605:22 fiya : I martiya : Vahyazdáta, : пата : Tarava : пата, : vardanam
```


## [2026-10-17T00:03:23.507Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2862,2872p KNT_full.txt; grep -n \"^vardana\\|vardana- n\\|^vartanam\\|Fravarti-\\|^Fravarti\" KNT_full.txt | head; grep -n \"didā-\\|didà-\\|dida- \" KNT_full.txt | head -5"
}
```


### [2026-10-17T00:03:23.864Z] TOOL RESULT

```
Varkana =  Vpküna, Elam. Mi-ir-qa-nu-ia-ip 
‘Hyrcanians’, РЫ. MPers.  Gurgün, Gk. 
"f pxavla. 


vardanam = opj-, GAV. vorozóna, LAV. varozüna-, 
Skt. opjdna-; see Lex. s.v. 

ardata- ‘silver’, Av. srezata-; Yezdi ali ‘silver’, 
2869:vardanam = opj-, GAV. vorozóna, LAV. varozüna-, 
8417:maspüda-, Fravarti-, and the Sagartian Ciça- 
27585:haj-; in nouns framdtar-, framānä-, Fravarti-; in 
28783:matic. See also duvarüi-, Fravarti-. — varnava- 
28838:vardana- sb. ‘town’: Av. vorozona-, LAV. 
28843:vardanam nsn. DB 1.92; 2.9°, 22, 66, 95f; 3.5, 22, 
7761:isuvà-, zaudà-, Hka-, didà-, yakd-, Ѕака-, ha"dugà-, $ 
26703:didà- sb. ‘wall, stronghold, fortress’: N Pers.
```


## [2026-10-17T00:03:30.870Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28770,28845p KNT_full.txt; sed -n 26700,26710p KNT_full.txt; grep -n \"Fravarti- \" KNT_full.txt | tail -3"
}
```


### [2026-10-17T00:03:31.197Z] TOOL RESULT

```
(epithet of Aši; the meaning is inappropriate, and 
the etymology is therefore rejected by ВМ. AiW 
1358-9). Vaàlya|splára]hyà gsm. DB 4.83. 


var- vb. ‘cover, protect; (mid.) choose, con- - 


vince’: Av. var-, pres. varanav- (‘var-, "var, war- of 
Bthl. AiW 1360-3, and perhaps *var-, are reducible 
to one root as to form and meaning), Skt. urn oti, 
Gt. warjan ‘ward off’, Lt. operit ‘covers’ (from 
*ор-џет-); OP pres. varnava- (830, $2101), the- 
matic. See also duvarüi-, Fravarti-. — varnava- 
taty mid. (§235.1) DNb 23.  ava|navatà] imf. mid. 
(8235.1) DSf 17 (Hz. AMI 3.43; Kent, JAOS 
58.11). varnavataty subj. mid. ($222.11) DB 4.49. 
varnavatém imv. mid. ($237.1V) DB 4.42, 53. 


vāra- sb., see Uvárazmi-. 
varka- sb. ‘wolf’, see Varkdna-. 


Varküna- sb. ‘Hyrcania’, a district southeast 
of the Caspian Sea (§166.1): Elam. mi-ir-qa-nu- 
ja-ip ‘the Hyrcanians’, РЫ. and NPers. Gurgan, 
Gk. ‘Tpxavia (830, $99, $107); ‘Wolf-Land’, deriv. 
of pIE *ylg*o-, Av. vohrka-, Skt. vfka-, Lith. vilkas, 
Gt. wulfs ($143.IIT): see also Varkazana-. Var- 
kāna nsm.-.DB 2.92f. 


* 


LEXICON 


Varkazana- adj. ‘Varkazana’, eighth month, 
Oct.-Nov.: Elam. margašanaš, Akk. arahsamna. 
From varka- ‘wolf’ ($148.11) + zana- ‘man’ (§9.- 
ГҮ, §88, $120): ‘Month of the Wolf-Men’ (8161.- 
IIb). [Varkazanahya] gsm. DB 3.88, restored 
after the Elam. (see Wb. KIA 56-7; the first and 
the third a’s may have been long). 


varga- sb., see haumavarga-. 


vart- vb. ‘turn’, trans. in active, гей. or in- 
trans. in middle: Av. varat-, Skt. vrl-, pres. várlati 
vdrtate, LA. vertit, Gm. werden ‘become’, pIE *uert-. 
[valriaiyary ist sg. mid. caus. (831, $48, $215, 
. $233.II; JAOS 62.275, 63.67-8) DB 444 (Camer- 
on’s reading; not upa- + à + varl-, \updvalriary 
with dittography in -"tysiy*, as proposed by Tm. 
Vat. Stud. 1.30-1, Lex. 122; for other restorations, 
see Gray JAOS 23.60-2, Bthl. WZKM 22.69, Wb. 
ZDMG 61.728, HK Phil. Nov. 3.103, ApKT 1.61, 
2.28). 


vard- vb. ‘work’: Av. varaz-, Gk. рёрүө ‘work’, 
Gm. Werk, pIE *yerg-; in Artavardiya-. 


vardana- sb. ‘town’: Av. vorozona-, LAV. 
varazdna- ‘community’, Skt. wpjdna- ‘enclosed 
space’, pIE *urgeno- (830, 5147.1), to root *uerĝ-, 
Skt. yrj-, Gk. &pyo “Т enclose’ (discussion of etymol- 
ogy, with variant view, see Hall, Те. 12.297-9). 
vardanam nsn. DB 1.92; 2.9°, 22, 66, 95f; 3.5, 22, 
34, 51f; DSe 45f. 

(JAOS 51.229). 


didà- sb. ‘wall, stronghold, fortress’: N Pers. 
diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos, 


191 


NEng. dike, ditch (676.011, 588, §148.IV, 5166).
```


## [2026-10-17T00:03:49.333Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=28700 && NR<=28900 && /^ *20[0-9] *$/ {print NR\": \"$0}' KNT_full.txt; grep -n \"Fravarti- sb\\|^Fravarti-\" KNT_full.txt"
}
```


### [2026-10-17T00:03:49.748Z] TOOL RESULT

```
28872: 207
```


## [2026-10-17T00:03:54.936Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^wer-\\|^werg-\\|^wreg-\\|^wer- [0-9]\\|^wer[0-9]\" AHD_watkins1985.txt | head -20"
}
```


### [2026-10-17T00:03:55.516Z] TOOL RESULT

```
1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
```


## [2026-10-17T00:03:57.897Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1148,1152p AHD_watkins1985.txt; grep -n \"^warn\\|WARN\" AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:03:58.621Z] TOOL RESULT

```
wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
77
wers-2
*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
’ BULWARK. 2. Greek ergon, work, action: ERG, -URGY;
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
```


## [2026-10-17T00:04:02.533Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"verschlie\" WLD_Bd1_pages.txt | head -20; grep -n \"vara&ra\\|varəθra\\|varo^ra\\|var9\\|vara9ra\" WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:04:02.959Z] TOOL RESULT

```
6941:dgy.sco,          arceo,       lit.   rak'inti „verschlieSen“.
7331:   lat. arceo, -ere „verschlieBen, einhegen; durch AbschluB fernhalten, ab-
25018:..verschlieBen, schiitzen 11 ).
26518:                         ..verschlieBen.
26519:        retten, abwehren”: aus ..verschlieBen'- aucb Worte fiir „Tur‘ und                                                                          £
26533:auf.    entbiillt j".            lat.   operio ..verschlieBe                    (decke zu/                       -
26925:    *ner- ..verschlieBen"                                 .
26945:    ohne Sclieidung von ~uer- ..verschlieBen, wahren"). Ill 392 f., Falk-Torp
27057:mehr zu *aer- ,,verschlieBen, wehren").
27225:zu ncr- ..verschlieBcn, bedecken, abwohren”) mit (1-Taw. (ursprgl. r/-Praes
29036:als ,,eingeschlossen“            zu tier- ,,verschlie6en‘- gehoren.
46509:    steckten Haken, Riegel, ein Pflockchen verschlieBen". Unsicher sind
46519:xhiixog ds., xbjim (jon.), xbja> (altatt.), y.Xe’m (att.) „verschlieBe mit einem
46585:                                                    PI.    doeu       „clavi“,     doi „verschlieBen, verriegeln“,
71088:Tenne*); abg. tvoriti, sv'voriti ,,sehaffen. machen *, zatvorili „verschlieBen,                              1
```


## [2026-10-17T00:04:06.823Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 26505,26620p WLD_Bd1_pages.txt | tr -s ' ' | head -120"
}
```


### [2026-10-17T00:04:07.220Z] TOOL RESULT

```
verwandtes *nrC-d -, *iim-d- (oder -db-) zuruckgebn (Lit. bei Brugmann
aaO. doch s. aucb unter *ner-, * tn-rcd ..drehen '). 1




 Kaum eine Erw. dieses *//->- ist ^ucrgdt- „ab-, wegreilaen ££
 ,
 s. d.


7. tier- bedeeken-, woraus ..durch YerscblieBen schiitzen,
 ..verschlieBen.
 retten, abwehren”: aus ..verschlieBen'- aucb Worte fiir „Tur‘ und £
 —
 ursprgl. nur in Gegensatzbildungcn mit Praefixen der Bed. ,.auf, von“
 — ..aufschlieBen, iiffnen'' s. bes. Bgm. IF. 174, Johansson IF. 25. 2 13 f.) 1 .




 aus ..absperrende oder umscblieliende Steinmauer. Damm alsSchutzwehr,
 FluchtburgY aucb z. T. Worte fiir nicbt diesem Zwecke dienende Stein-
 walle und Erhohungen. = Neben tier- bes. im Ar. undGr. eine Erw. verfi-.
 Bedeutungsgruppe ..schlieBen" (sekundiir ..iiffnen'), ,.Tur‘:
 Ai. api-crnbti ..verschlicBt (bedeckt. verb ii 11 1) '. apuvrndti ..iiffnet <
 deckt
auf. entbiillt j". lat. operio ..verschlieBe (decke zu/ -
 — aperio ..offne (ent-
 uer- 281

 nach Niedermann IF. 26, 50 aus
hiille)“ (aus *op-, ap-verio; letzteres nicht
*at-verio, s. Brugmann II 2 2, 806), umbr. verof-e „in
 osk. vp.ru „portanr ,
 £



portam" (hierher wohl auch osk. verehia- ..Gemeinwesen", s. u. *ita *uergh-
 £
„drehen"), lit. iizveriu , -verti „schlieBen ‘, atverti „6ffnen“', lett. atvert ds.,
apr. etwcre „du offnest", endlich neutrales lit. veriii, verti „offnen oder
schlieBen", vartai PL „Tor ££
 ,
 apr. ivarto n. pi. „Haustiir", aksl. vvrq, vrZti
 £
,,schliefien‘ ,
 £
 zavrcti ds., otvoriti „offnen“, vrata n. pi. „Tor, Tiir , russ.
zavorv „mit Stangen gesperrter Durchgang" (aksl. zavon „vectis", wie
 ££
ver'eja „vectis wahrend kkr. vereja „Torflugel", verej „Riegel
 ££
 ,
 iiber die ;

 ££
Schwierigkeit scharfer Abgrenzung gegeniiber der Sippe von tier- „Schnur
s. lit. vcmjti „treiben‘ (formell
 d.) ; =
 germ, ttarjnn, aksl. ot-voriti, vgl. auch
 £




ai.Kaus. vardyati) wo’nl als „das Tor offnen, um das Vieh aus der Hiirde
hinauszutreiben mit einem Keil eine Offnung treiben" hierher z. B. Uhlen-
 ;
 :




heck Ai. Wb. 283, Pedersen IvZ. 38, 195). Nach Liden Aufsatze fiir Kuhn
139 — 142 tocli. B ruwim „icli offne (*«W?-). ££




 „Verschliefien, bedecken, schiitzen, retten":
 Ai. vniuti vrulte, vdrati „verhiillt, bedeckt, umschlieBt. umringt, liemmt,
 ,

wehrt" (darin ist auch idg. *oel- ..drehen usw." aufgegangen, s. d.), vrtd-,
vdrtum, Kaus. vardyati ,,verhullt, bedeckt, halt ab, wehrt", varmnn- n.
„Schutzwehr", vdrtra- n. ,,Schutzdamm, Deich" (: cymr. gwerthyr), vtxr ya-
rn. „Uberwurf. Decke, Farbeusw.", vara tut- m. .(Wall, Damm“, arno-vrt ,.die

Fluten einschlieBend", vrti- f. ,,Zaun, Einzaunung" = as. wurth usw.) varu- i

 ;



tdr- m. ..Schiitzer, Schirmer", vdrutha- n. „Schutz, Schirm. Schild, Wagen-
einfassung, Heer, Herde, Schwarm“ (daB auch Vanina- eigentlich ,.IIimmel"
„*bedeckender. hiillender" sei s. unten gr. ovgarog —
 und Solmsen Unt.
297 f. m. Lit.. Reichelt IF. 32, 27 ist bestritten. s. *>ier- —
 drehen"); vielleicht .,


mit formantischem g hierher vdrga- m. ,.Abwehrer, Beseitiger" winders
unter *uer-, *uenj- „drehen"): dehnstufig vara- m. ,.Deckung. Wehr (ebenso
 £
 ‘




av. -vara- in Zs„ npers. bant, -ear ,.Wall ‘), vdralca- ..Zuriickhalter, Ab-
 £
```


## [2026-10-17T00:04:09.738Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 26620,26720p WLD_Bd1_pages.txt | tr -s ' ' | grep -v \"^ *£* *$\" | head -70"
}
```


### [2026-10-17T00:04:10.152Z] TOOL RESULT

```
wehrer" (vgl. gr. ijgarog ,,Besehutzer. Herrscher" — das nicht zu *ner-
„freundliches Wesen" — mit *o cymr. yicawr ..Held" av. -vorrmavaiti ;
fm. Praef. -voranantp ..bedecken, lnillen" z. T. idg. 9 gel-, s. o.; vermutlich
hierher raraia- ..gefangen" als ..unter YerschluB", kaum zu gr. dUay.ouai.
s. *ucl- ..reiBen"), var m. ..SehloB, Burg", varjiut ..Umliullung, Bedeckung",
vnr.rda- m. ..Yerteidigungswaffe, Welir", var.nhnan- n. ..Brustwehr, Wehr",
voradra- n. ,.Wehr, Schild".
 Gr. vielleicht svoai ..eiserner Beschlag der Wagenachse, worin die Riider
sicli wenn eigentlich ..Hiille" (Prellwitz 2 Boisacq s v.) und evgcbg,
 drehen", ,
 -tTjxog ..Schimmel. Moder". wenn eigentlich ./Bedecker" (ware *e-foco- t-.
 2
 vgl. ai. arno-vrt: s. Brugmann II 2. 298;; ovgarog. aol. dgurog ,,IIimmel"
 (nach Kretschmer KZ. 31. 444. Solmsen Unt. 297 f. aus *fooarog, dpogarog.
oder aus *foopa»'d?, *dfoof-av6g. so daB zur Wzf. *ueru-. wie alle folgen-
den Worte) hom. tovaOai ..abwehren, retten. bewahren". Impf. tov-oo. -to,
 ;
themat. geworden fovtio (s. Solmsen Unt. 40). Pf. eToupai pgr/iau),
jon. etovouai (*efrovopai) ..halte fest, bewahre eovaa ..Schutz. Schutz- -
 ,
wehr". sgvnt’og ,.geschiitzt, befestigt", tgvai.-nohg ..Schiitzerin der Stadt":
evQvoi-laog. r.rgv-hmg u. dgl. (i-fov-: beweist fiir anl. y der gr. Sippe. dem
auch der hom. Tatbestand nicht widerspriclit. und gegen ihre Yerb. mit
2S2 uer-
*ser- ..servarc", s. Solmsen Tint. 243 ff. ;
 Zweit'cl bei Bechtel Lexil. 139 f.)
 T
fov- ohne A okalvorsehlag in inf. hom. gva&at, hom. jon. gvo/uat „schirme,
 (letztere Bed., die auch der k- Erw. igvy.co ,
 1
errette; halte fest, lialte zuriick'
tovy.avco.iovxavaco ..halte ah, zuriick", Pass. ..zogere" innewohnt. aus ,.durch
einen YerscliluB fernhalten, abwehren". niclit als ..wegziehen" nach Boisacq
zu igvco ..ziehe", das zu ..verrere"), gvua ,, Schutz, Scliutzwehr‘%
gvoio ..schiitzend, rettend '. ovtcoo. gvrijg ..Retter, Bcfreier", g voinohg
..Schirmerin der Stadt"; dehnstufig Bed s. u.). fyo (or ..Grabhiigel" (zur
 Alb. vn? ..Grab" (G. Meyer Alb. St' Y 104, Jokl SBAkAYien lG',, I 94;
'’nornu . cade ..Gehege" (s. u ;
 Jokl aaO.).
 Air. fir van ..Giirtel". fern ..Scliild", fn-t, ferine ,. Grabhiigel" (mit
Steinen versehlossen oder mit einer Stcinmauer umschlossen, geschiitzt. vgl.
l'uss. clorouitb ..begrabeiv aksl. chraniti ..schiitzen, schirmen"'.; = ags.
 :
word. (s. u. r, fironn, ft runn ..Land. Acker” (wohl „*umhegt", allenfalls
•.durch die aus der Scholle ausgeraumten Steine schutzmauerartig umsaumt";
oder ursprgl. ..erhohtes odor deichgeschiitztes Land zwischen Siimpfen oder
am \Yasser", wie ags. icarop usw. ? s. u. meymr. nwerthijr f. ..Festung- (f.a r- ;
trd: vgl. o. ai. rarfru- tjirwrr ..Held", s. o. (Pick II 4 271 mit lcaum ver-
 ,
einbarem weitern: iiber ir. foiann ..factio" s. *v.e - ..Schnur"). >
 Got. wnrjttn ..weliren", anord. rerjn ..weliren, hindern, verteidigen *, ags.
inrian ..ds.. aufdiimmcn". ahd. we mi ..verteidigen, schiitzen”. as. uwittn
..wehren, schiitzen, hindern germ, -carii (..Yerteidiger \ daraus Ein- .
woliner ) in Chuiuurti, B’-jnmrii. anord. z. B. Ilum-verjur ..Romer”: urnord.
want ..der umschlieBende Steinkrois uni ein Grab" A. o. ir. f<rt) = anord.
rqr f., nnonv. tor m. ..Reihe von Steinen an beiden Seiten eines Landungs-
platzes. worin die Bote aufs Land gezogen werden" (aber gr. ocgol ..Lauf-
griiben, in denen die Schiffe ins Meer gezogen werden", von Liden Auf-
siitze liir Kuhn 39 —
 142. wo Lit. iiber andere Deutungen, damit verglichen,
 1
wohl zu *t era- ..graben ’i, auch ..Iliigel oder Bank von Steinen oder Kies,
Glctschermoriine". anord. ixr n. g. pi. ctrjtt) ..Datum. Fisckwekr\ ags.
```


## [2026-10-17T00:04:16.276Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"dîvâr\\|divär\\|dlvär\\|dīvār\" \"bärü\\|bārū\\|bäru\" \"barzan\" \"bahräm\\|bahrām\\|Bahräm\" \"farvard\\|fravard\" \"parvär\\|parvār\" \"farvär\\|farvār\" \"frava[šs]i\\|fravaäi\\|fravahr\"; do echo \"== $w\"; grep -n \"$w\" HRN.txt | head -5 | cut -c1-250; done"
}
```


### [2026-10-17T00:04:16.891Z] TOOL RESULT

```
== dîvâr\|divär\|dlvär\|dīvār
5350:599. dlvär 'Mauer, Wand'.
== bärü\|bārū\|bäru
== barzan
== bahräm\|bahrām\|Bahräm
== farvard\|fravard
== parvär\|parvār
2937:parvär,
== farvär\|farvār
== frava[šs]i\|fravaäi\|fravahr
```


## [2026-10-17T00:04:20.164Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5350,5365p HRN.txt; sed -n 2925,2945p HRN.txt; grep -n \"bärü\\|baru\\b\\|bärö\\|bära 'Mauer\\|bära\\b\" HRN.txt | head; grep -n \"barzan\\|bar^an\\|barzau\" HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:04:20.702Z] TOOL RESULT

```
599. dlvär 'Mauer, Wand'.
ap. ^deghavära- (vergl. gr. th/o^-, osk. felhuss).
Nöldeke (mündliche Mitteilung), unter der Voraus-
setzung, dass die np. Grundform '^devür lautete, was
die Zusammenstellung mit dev (8ähn. I, 24 Vers 86)
wahrscheinlich macht.
kurd. LW. dwär; wa;^. LW. dival^ sar. delvül 'Mauer,
Wand, Umwallung.
*) Der Majhül vokal ist nicht mehr in der Aussprache erhalten.
') College Jensen hat din sogar im Verdachte, babylonisch zu
sein. Er äussert sich in folgender WeiBe über diese Ansicht:
y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
dattira ibid. = framätaram, beides in der Inschr. von Naqs-i-Rustani.
iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
welches in der babyl. Version der Achämonideninschriften vorkommt.
iHiiii = 'Gesetz, Recht* könnte sehr wohl persisches daina übersetzen,
vergl. pards 'über hinaus, mehr als', purand- 'vor-
malig, purd einst'.
*) Dazu arm. amparist , ambarisf *unfpomm , gottlos* nach F r.
Müller, WZKM. 5, 186 (?).
*) Arm. LW. p^ursis,
«) AM., Seite 46. Vergl. auch x^n-i S. (AM. 128 Zeile 6).
5*— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
6532:ap. as(s)a]bära- 'Reiter' (doch wohl = *aspabara- ^) ;
HUB.txt:851:von barzan noch vollkommen dunkel.
HUB.txt:4378:baranjan (§ 62 und 72j *Armband* = arm. aparanjan *Armband' (5. Jhd.)
HUB.txt:6133:baranjan), arm. aparanjan (s. § 3); azbar oben' — zabar
```


## [2026-10-17T00:04:26.196Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 840,852p HUB.txt; for w in \"divär\\|dlvär\\|divar\" \"bärü\\|bära\\b\\|bäru\" \"bahräm\\|Bahräm\\|vahräm\\|Vahräm\" \"farvard\\|Farvard\\|fravard\" \"parvär\\|parwär\" \"frava[šs]\\|fravahr\\|frohar\"; do echo \"== $w\"; grep -n \"$w\" HUB.txt | head -5 | cut -c1-250; done"
}
```


### [2026-10-17T00:04:26.758Z] TOOL RESULT

```
196. Zu barda *Gefangener' = phi. vartak hat schon Geiger
an der von Horn citierten Stelle richtig zd. vareta-
gefangen' gestellt. Dazu afgh. LW. barda *a female
slave.'
199. Np. barman 'Quartier' ist nicht — ap. vardana- *Stadt',
das doch zu np. *balan geworden ware. Zd. verezena-
heisst nach Geldner (Pischel - Geldner, Ved.
Studien II, p. 19) Bauernstand, Bauernschaft*, dagegen
soli skr. vrjana- *Fangnetz, Falle, Anschlag, List, Hinter-
halt, Versteck' etc. (Pischel-Geldner, Ved. Stud. I,
143 flg.) bedeuten. Jedenfalls bleibt die Etymologic
von barzan noch vollkommen dunkel.
200. Dazu syr. LW. NDD^ID, Hoffmann, Auszuge p. 94,
== divär\|dlvär\|divar
4195:= pSz. x'divar = *the west'. Naoh N old eke ist die &lteste Bedeu-
6858:sassanid. ana^iaSovao ^ "^spah-dadivar^ phi. datiwary aram.
== bärü\|bära\|bäru
== bahräm\|Bahräm\|vahräm\|Vahräm
== farvard\|Farvard\|fravard
5980:(neben fravardiyan), gr. Oovpiiyap = vtxvla (Menander,
6712:zd. asa-vahista-; Farvardm 'der erste Monat' = phi. fra-
6910:sisch *farvard lauten, vgl. np. Farvardin der erste Monat
8684:Farvarddjan 'die letzten funf Tage des Monats Aban und
8687:dagan, farvardiydn u. s. w. (die fiinf Schalttage als Fest
== parvär\|parwär
== frava[šs]\|fravahr\|frohar
6713:vartm 61. and Ind. 87, zd. fravasinqm (gen. pi.), vgl.
6908:phi. fravahr (Gl. and Ind. 100), zd. fravasi-, ap. *fravarti';
6911:= i^\A, fravartln = zd, fravasinqm (s. oben § 84, b); phi.
```


## [2026-10-17T00:04:35.282Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6708,6716p HUB.txt; sed -n 6904,6914p HUB.txt; grep -n \"frawahr\\|frawardīn\\|wahrām\\|wālān\\|dēwār\\|parwār\\|bārūg\\|bārag\" PHD.txt | head -20"
}
```


### [2026-10-17T00:04:35.567Z] TOOL RESULT

```
*Feuer*, taSarv 'Fasan* fRebhuhn* nach Sal. Shuk.), kdyaS *Papier*
gumbaS 'KuppeV, Sal. Shuk. p. 12.-- 190 -
b) Ap. t nach r = phi. t^ paz. d, np. d: Ardtbahist
'der zweite Monat' = phi. Art(a)v(a)hist 61. and Ind. 87,
zd. asa-vahista-; Farvardm 'der erste Monat' = phi. fra-
vartm 61. and Ind. 87, zd. fravasinqm (gen. pi.), vgl.
0ovQdlyav {= vsavia) bei Menander; Ardastr^ Sirin, Art asir
(alter Artases), gr. ^JtQTantlgtjg u. s. w. BB. 4, 35, alter immer
Arta- ; ArdavSin, arm. -4r^at;aw, gr. ^Agva^avoq u. s.w. Dazu bei
specifisch parsisch und wiirde echt mittelpersisch *amurt' oder
*amurd-8pand lauten, vgl. phi. murtak Gl. and Ind. 217 'todt* =
np. murda = zd. mesa- und mereta- 'todt*, ap. *mrta- sowie
Murddd (der fiinfte Monat) = zd. ameretat- ; np. farvar =
phi. fravahr (Gl. and Ind. 100), zd. fravasi-, ap. *fravarti';
aber das Wort ist specifisch parsisch und wiirde echt per-
sisch *farvard lauten, vgl. np. Farvardin der erste Monat
= i^\A, fravartln = zd, fravasinqm (s. oben § 84, b); phi.
Mahrih (NOldeke, Pers. Stud. I, 38, Anm. 2) = zd. Masya-
(West, PT. I, p. 57) neben phi. Masya, das nur Umschrei-
bung ist ; aber der Name ist parsisch und das entsprechende
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
335:frawahr [рі | M prwhr-] man's immortal soul, guardian angel during his lifetime.
337:fraward [plwit' | M frwrd-] = frawahr.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
789:angel fréstag; guardian ~ frawahr, fraward.
1239:circumvallation, citadel parwār; v. fortification.
1810:evening ēbārag; previous — dēš.
2856:mount bārag, stor.
3744:soul frawahr, fraward, griw, gyan, ruwan, uštān.
3872:suburb parwār,
3902:surroundings parwār.
4207:vessel jām(ag), kabārag, takók.
4250:wall dēwār.
4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo parwāz о» ro franāftan мү оу \ o Farrobag Yo (read pin-) Farróbag | 23 » a) piring E N a palang 3 М оз рагпарап w as» QJ palangmusk VU re N) Q) parwand E R Фу parwand- - 9 i a parron Ў оу frogih- -45?o frogihistan Us 4» оу frog Po parrwar N М P
4988:kaf- "kabāh kabārag kabīg kabiz
5530:dēnār, dēwār, suxr
```


## [2026-10-17T00:04:44.875Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \"wahrām[^.]*\\.\\|frawardīn[^.]*\\.\\|frawardig[^.]*\\.\\|bārū[^.]*\\.\" PHD.txt | head; grep -n \"wahrām\\|varhrām\\|vahrām\\|frawardīn\\|fravardīn\\|dēvār\\|parvār\\|frāvahr\\|fravahr\" NYB_vol2_glossary.txt | head -20 | cut -c1-300"
}
```


### [2026-10-17T00:04:45.256Z] TOOL RESULT

```
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt
1557:fravahr [plw’hl] the heavenly and im- mortal counterpart of the earthly beings, their tutelary genius 31? etc. passim; also fravaš (g. v.). — Av. (992 sqq.) fra- vaši- < "fravarti-, cf OP n. pr. Fravarti- = Gr Öpaöprns; MPrs pr’whr ‘ether’
1563:fravartikin [plwltyk’n'] the five inter- calary days at the end of the year, cele- brated in commemoration of the dead and their fravahrs: 8995, — NP farvardgan, farvardiyan.
1564:fravartin [plwltyn'; inser. prwrtyn] 1. the name of the first month of the year SPrthPrs: 1; 952°. — 2. the name of the 19th day of the month 30%. — < *fravarti- nam, Av. (994) fravašinam, gen. pl. of fravarti-, v. fravahr.
1565:fravaš [plwš] = fravahr 4011, — Borrowed from Av. fravasi-.
2045:hu-fravart [hwplwlt'] having a good fra- vart (= fravahr, q.v.), Saint, venerable 1085, 11125,
2113:jan [y'n'; HY?] the animal spirit of man, as opposed to his ruvdn and fravahr; common to human beings and animals 9717-18; perishable: death signifies kanišn i ~ u višopišn + tan the destruction of the animal spirit and the disintegration of the body 6410-11; after death ~ merges with the Wind,
3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. b
3711:tan [tn'] body, passim, stalk of a plant 9524; ~ u jan body and vital spirit 1523. 6422 (the constituents of human physical nature); ~ u jan u hir u xvāstak 4%; kanišn 4 jan u višopišn i ~ the destruc- tion of the vital spirit and the decom- position of the body (= the physical death) 64191; ~o
4343:x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor u ~ + visp-ākāh spēnāk meno datar Ohurmazd 1063-24, — 2. a cosmic essence 9215.19, 
4382:xučš [NPŠH; hwyš] 1. refl. pron. self, valid for all persons, a) referring to the agent = the logical subj.: -š ~ hécak hac cäh ul hixt he himself hauled up 1519; b) as an obj.: ~ hac ranj äsän kartan to relieve oneself of trouble 1313-14; c) after a prep.: vinäskäreh andar ~ bē guft 3474; (šmā
4415:yašt [ySt'] worship, invocation, religious ceremony 6519, 7019 ( u niyäyisn u īzišn u azbäyısn) ; 1005-14-17 ete, passim; v. also yast-fravahr. — Borrowed from Av. (1280) yašti-.
4422:yašt-iravahr [-plw’hl] he whose frava& is worshipped, of deceased holy men; of Zartuxšt 1115-9. — yašt < Av. pt. yašta-; v. fravahr.
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit fro
4889:fra0-: pursitan Fravarti-: fravahr fravatah: fröt
5145:frabdö.dräjah: fravd fraca, fraš: frāc fradašafšū: Frādatafš Fradat-xUaronah-: Fradat-xUarrah fračšta: frayist Franrasyan: Frangrasi- yak fra-pad-: frabd, fravd ä-fras-: äfräs a-fray-: äfritan Frašaoštra-: Frašostr Fraš.ham.varota: fraša- vart frašna-: frašn frašč.koroti-: fraš-kart fratoma: fr
5465:yama-: yam (&-)yaog-: &yuxtan (api-)yaog-: api-yuxtan yaoz-: āyēz-: yod- yašta-: yašt-fravahr yaštar-: yastar yašti-: yašt
6078:pr'whr: fravahr
6089:prwhryn: fravahr
6570:fravaš: fravahr
```


## [2026-10-17T00:04:57.224Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^vahrām\\|^Vahrām\\|^varhrān\\|^vāhrām\\|^dēvār\\|^parvār\\|^Varhrān\" NYB_vol2_glossary.txt | cut -c1-400; grep -n \"^parvār\\|^dēvār\\|^vahr\" NYB_vol2_glossary.txt | cut -c1-300; grep -n \"wahrām \\[\" PHD.txt | cut -c1-200; grep -o \"wahrām \\[[^]]*\\][^.]*\" PHD.txt | head"
}
```


### [2026-10-17T00:04:57.873Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:01.429Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"vahr.m\\|varhr\\|dēvār\\|devar \\[\\|parvār\" NYB_vol2_glossary.txt | cut -c1-300 | head; grep -n -i -o \"wahr[aā]m.\\{0,120\\}\" PHD.txt PHD_mackenzie.txt | head -5"
}
```


### [2026-10-17T00:05:01.835Z] TOOL RESULT

```
761:ātaxš [^th$] fire, in the ordinary sense 20? and passim; — in the Zoroastrian creed and cult: personified as the son of Ohur- mazd 311-235, passim; 589.29, 593; wor- shipped 353. 6629-22, 95%, cf 116’; one of the basic elements of the creation 92?. 9425.27, 9874.25, 12013; man 4 —-ān fire- templ
3071:*pat-kust [PWN kwst'] 5" is possibly the irregular spelling of the pt. of a vb. *patkustan "to come into contact with, to join side by side with (hac): api-š hac Vahram u Anähit ~ and it (the planet Jupiter) has joined side by side with Mars and Venus; but the construction is strange, and this 
3314:réxtan [lyhtn'] réc- 1. to flow, v. récisn; Mah hac Kaivān u Vahräm rēcēt 6 Ohur- mazd the Moon is proceeding from Saturn and Mars to Jupiter 7" (astrologi- cal). — 2. to pour 108°. — Av. (1479) račk-; MPrth pt. ryxt, MPrs pres. ryz-, both ‘to flow’; Paz. pres. réz-; NP réatan rez- ‘to flow, to
3328:vahist. 4. Sahrévar. 5. Spandarmat. 6. Har- vadat. 7. Amurdat. 8. Dade pat Atur. 9. Ātur. 10. Āpān. 11. X*ar. 12. Mah. 13. Tir. 14. Goš. 15. Dadv ‘pat Mihr. 16. Mihr. 17. Sroš. 18. Rašn. 19. Fra- vartin. 20. Varhran. 21. Ram. 22. Vat. 23. Dadv pat Den. 24. Den. 25. Art. 26. Astät. 27. Asman. 28
3840:MPrth texts only) and w with two dots above: w = u, with encl. pron. ’w- : >w-m 46-0, ^w-8 ete. u-m, u-t, u-$. No doubt Milr had double sandhi forms: *ut before a vowel and u in other positions. A trace of "ut in the official Sassanian language is found in the Arm. rendering of the set phrase E
3912:Vahram [w’hl’m] later form of Varhrän, Varhräm (q. v.): 1. the god V. 72°; ātaxš i ~ 203-4, v. Varhrän ; the planet Mars 511, 77. — 2. n. pr. the Sassanid king V. V, son of Yazdékirt I (420—438), 114*. 115?. 11712-18 with the surname Gēr 116?!; a town Vahräm-Gör founded by him in Media 115°. — 
3913:Vahrämävand [w’hl’m’wnd] the name of a fortress in Media 115%. — Haplology of Vahram-amävand ‘Strong (is) V.’, cf 729-10,
3914:Vahram-Gör v. s. v. Vahram.
3948:2yar enclosure, defences, fortress: ~ 4 Yam-kart (g. v.) 9719; ~ 4 Täcikän 115°. 1178; ~ % Vahramdvand (q. v.) 1158. — Av. (1363) "var-; Paz. var; Bailey, BSOS VI, 1930-31, 591 sq.: ~ synonym to dast.
3963:varcävand possessing supernatural pow- er: of ätur farröbäg 974; of ātaxš Varhran 1139-21; of ātaxš i Karköi 1164; — subst. a man endowed with supernatural power, of Zartuxšt 36%; mart i vazurg x"arrah 4 Yam u an-ic ~ 44°; pl. cas. obl. ~-an 455, — MPrs wrc'wynd (S).
PHD.txt:605:Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak
PHD.txt:2739:Wahram.
PHD.txt:4406:Wahrām
PHD.txt:5290:Wahrām
PHD_mackenzie.txt:5150:Wahram [wllll'n l , w'hl'm I M whr)m, N bahram] god of war, victory; astr.
```


## [2026-10-17T00:05:07.279Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'));b=d['BQT'];print({k:b[k] for k in b if k not in('title',)})\" | cut -c1-3000; command ls refs/ocr/BQT 2>/dev/null | head -50"
}
```


### [2026-10-17T00:05:07.700Z] TOOL RESULT

```
{'kind': 'archive_djvu+local_scan_ocr', 'url': "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/
0001.png
0001.txt
0049.png
0049.txt
0143.jpg
0143.vision.txt
0262.jpg
0262.vision.txt
0332.jpg
0332.vision.txt
0334.jpg
0334.vision.txt
0338.jpg
0338.vision.txt
0339.jpg
0339.vision.txt
0342.jpg
0342.vision.txt
0456.jpg
0456.vision.txt
0479.jpg
0479.vision.txt
0480.jpg
0480.vision.txt
0511.jpg
0511.vision.txt
0544.jpg
0544.vision.txt
1024.png
1024.vision.txt
103.vision.txt
1074.vision.txt
1083.jpg
1083.vision.txt
1085.png
1085.vision.txt
1092.jpg
1092.vision.txt
1096.png
1096.vision.txt
1187.png
1187.vision.txt
1194.png
1194.vision.txt
1202.jpg
1202.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
```


## [2026-10-17T00:05:09.354Z] AGENT

Let me run ref_page for the cited BQT pages.


## [2026-10-17T00:05:10.764Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 216 254 324 391 1473 1476 1478; do echo \"######## BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p 2>&1 | head -80; done 2>&1 | cut -c1-300",
 "timeout": 600000
}
```


### [2026-10-17T00:05:25.789Z] TOOL RESULT

```
######## BQT:216
no scan of BQT covers printed page 216 (see 'scans' in refs_online.json)
######## BQT:254
no scan of BQT covers printed page 254 (see 'scans' in refs_online.json)
######## BQT:324
no scan of BQT covers printed page 324 (see 'scans' in refs_online.json)
######## BQT:391
no scan of BQT covers printed page 391 (see 'scans' in refs_online.json)
######## BQT:1473
REF: BQT:1473  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 266  OCR-lang: fas

-۱8۳- فروخته
از پوستین روباه باشد وآن کرم‌ترین پوستی‌روباه | اطراف‌آن درها و پنجره‌ها دارد -
است بعد ازآن سمور ودیگر قاقم ‎٩‏ - فرواله ۱ - بر وزن پرکاله . بمعنی
فروار ۲ بروزن پروارخانةٌ تآبستانی فروال است که خانةٌ تابستانی و بالاخانهٌ اطراف
راگویند عموماً و بالاخانه‌ای که اطراف آن‌ورها | کشاده باشد . ۱
و پنجره‌ها داشته باشد خصوصاً - و بمعنی خانهٌ فروت - بفتح اول وئانی وسکون ثالث
زمتانی هم بنظرآمده است . وفوقانی» بمعنی بسیار باشد و بعربی کثیرخوانند؛ ‏
۰ نا ۰ اه
فرواده ۴ - بر وزن کهواره بمعنی وجتم اول هم گفتهاند :
فروار است که خانةٌ تابستانی و بالاخانهٌ چپار ور ۱ فرولن * « بکر اول وافتح تای
وبادگیر باشد - وبمعنی کنجینه هم‌آمده‌است. فرشت وسکون نونء تواضع کننده ومتواضع را
فرواز - بروزن انداز , چوب کوتاهی و و تنده ۸ زار دید
باشد بمقداردو بدست بعنی دوشبر وآنرادرپوشش ۱ فرو ه_- م‌اول بروزن‌خروشنده.
و بوربا بر بالای آن کسترانیده کل وخاریزند فروختاد؟ - بکسر اول وثانی بواو
و اندایند - و خانةٌ تابتانی و بالاخانه را هم | رسیده وسکون خای نقطه‌دار (۱) و فوقانی بالف
فرواره است کهخانةٌ تابتانی‌وبالاخانه‌ای باشد که فروخته *۱-,کراولبیم کزده شدسرا
۱- باین معنی «فرو» ( بفتح اول وسکون دوم وعربی است» جمع‌آن فراء (بکسر اول)
وفراء ۱ بح اول وتشدید دوم ( پوستین دوزاست اما« فرو یا درفارسی ۳ فرود ۰ پهلوی ۵1
ابرانی باستانی 05۳8۷812 [ رلك: فرود ] « نیب رکه ۷۹ برسرافعال مرکب درآید مانند : فرو
ربختن » فروخواندن » فرو کوفتن [ رك : دیباچهٌ مولفح‌لد ] و نیز براسماء درآید : فروتن -
۴ - اوستا- ۹۵۳2۷2۳888 1۳2۷8۵۲۵ » پهلوی 1۳2۷2۲ معنی « فروارنه »
اوستایی‌مشخص نیست . فروار فارسی با 2102171۷2۳2112 (بروار) (۸.م.) منطبق‌است . بعلاوه
هممکن اآست «فروار شکل همعرب «یروار» باشد ویهلوی و۱۱ فقط در کتیبه‌ها آمده «اسشق
۳ ورك : هوبشمان ۸۲۳. ورك : فروال » فرواله. ۴ - رد4 : فروار » فرواله »فروال.
۴ سد یمه آخر مصحف 7« قروار» (هم.). ه‌ قرواره («.م.) که فرواره.
‎٩‏ * فرواله ‏ فرواره * ۷ - از: فرو تن - ۸ - ازدساتیر «فرهنگه
دساتیر ۲۵۸ ۰ ‎٩‏ - از : فروخ ( فروختن ) + تار ( پسوند کار ورزی ) « دارمتش .
تعات ۳۱ ورك : سم مصدرص ۱*۵ ۰ ۹۰ آسم مفعول ازه فروختن » (و.م.) ۰
فر وختن - بنم اول ودوم وفتح پنجم ( درزبا ن کنونی ) ؛ اوستا ۷2۳90۰ ل 01۳۲2
( توسعهٌ - ۷26 چنانکه 8278 از - 386 ) ( صداکردن » بمعرض فروش گذاشتن) ؛ پهلوی
48 آاسشق - هوبشمان ۸۲۶« منای ۲۷۶ > ؛کردی 5۷70118 » کردی ع5۳۱۸112
( فروش ) « ژابا ص ۲۹۱ > » کردی ۶۷۳۵510 (فروشنده) « ژابا ۲۹۲ > + گلکی۳0۳0(:128؛
واکذارکردن‌چیزی يکي باگرفتن بهای‌آن - پزمخف افروختن (هم.).

######## BQT:1476
REF: BQT:1476  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 269  OCR-lang: fas

فروردبان ۱ -۱۷۹-
و عطربات بسیار بکارپرندوتنعمات کنندومیوه‌های | هم‌هست و او از خازبان بهشت است و تدییرامور
لطیف خورند و باتش خانها روند و کاهنبار | و مصالحی که درین ماه و در روز فروردین
همسيتميدیم (۱)۰۱ را بعمل آورند پعنی دعاها که نوزدهم این ماه است واقع شود بدو متعلق
و بخوراتیکه درروز اول خمةٌ مسترقه‌بایدخواند | است - و نام روز نوزدهم باشد از هرماه شممی
وباید کرد درین پنجرو ز کنند و خوانندومعرب | و درین روز فارسیان جشن سازند وعید‌کنند بنا
آن فروردجانت . برقاعدة کلیه که پیش ایشان جاری است که هر

فروردیان ۲ - با بای حطی () , | روزی از ماهی که نام همان ماه داشته باشد عید
بروزن و معنی فروردگان است ۴ که پنج روز | بامد کرد . نيك است درین روز باعتفاد اسان
آخر سال فارسیان باشد و آنرا خمهٌ مسترقه | جامةٌ نوپوشیدن و دیدن کوسفندان وکله و رمةٌ
میگونند ۰ کاوان واسبان .

فروددین ؟ « نم ماه اول سالشمسی فروز - بم اول و ثانی و سکون واو
باشد» وآن بودنآفتابست در برج حمل . وآن | وزای هوز . بمعنی تابش و روشنی وفروغ آفتاب
برج اول است ازپروج دوازده گانهٌ فلك وباددبور وغیرهباشد وبمعنی صفت هم‌آمده‌است 9.۹
که بادمغرب است‌درین آبام‌میوزد - ونام‌فرشته‌ای فرودان فر « بم اول وفتح‌فای‌دوم

. (۱) چك : همسپيتميدم . (۲) چك : با با -

‎٩‏ < اوستایی13210250210102648(2 ( ششمین گاهنبار) که‌درسیسد وشست وینجمین
روزسال برپا میشده « پورداود . خرده اوستا ص ۲۱۹ . ۴ - جشن فروردیان . جشن
فروودها ( فروهران ) است که هنگام فرودآمدن فروهران‌پزمین محوب میشود وآن ده روزامت
از اشتاد روز تا انیران روز از اسفندماه و پنج روز گاتها « پورداود» خرده اوستا ص۲۱۹-۲۱۸*.

‏۴ - رك : فروردکان . ۴ - پهلوی 1۳2۷27117 مأخوذ از پارسمی باستان
0۲۳3۷8۵۲70 جمم موك حالت اضافی كلمهٌ 8۳۳8۵۷87۳11 ( فروهن » فرور ) « نیب رک ص
4 ( رك : فروهر ) در اوستا نیز این‌کلمه بهیأت اضامه در جمع موّنت بیار آمده وهمیشه
همراه آشاون 889122۷80 ( 38128010) ز کر شده جمعاً بمعنی : فزورد های پاکان » فروهرهای
پارسایان » بدیتوجه دركلمةٌ مر کب «* فروردین اشاون » مطاف‌الیه آن که بمعلی پاکان بودم حذف
شده ‏ نظین « بهشت > ( «.م. ) بنابرین ین > در آخر فروردین پساوند بت نیت« فاب ۱ص
۶۵۵-۳ . بیرونی در فپرست روز های ایرانی در آثارالباقیه » روز نوزدهم را * فروردین » و
درسغدی « فرون > و درخوارزمی « روجن > بادکرده. درادبیات پارسی« فرودین » بتخفیف ( بفتح
اول وسکون دوم وفتح سوم ) آهده . مسعود سعد گوید :

‏فروردین است وروز فروردین شادی وطرب را کند تلفین
ای دو لب‌تو» چو می مراده کان باشد رسم روزفروردین.

‏ورك : روز شماری ص ‎4٩‏ - 4۸ ۰ « دیوان منمود سعم ۰.۹۹4

‏8 - ر4 : افروز » افروختن . ۹ * فروزه ( از دساقیر ) (ه.م.).

‏فروزان - جنم اول و دوم » صفت فاعلی از فروختن ( * افروختن) ‏ افروزان ؛
افروزنده » درخشنده :

‏يكآفتاب درخشان شده ز روی سپهر يكآفتاب فروزان شده ز روی زمئن.
معزی نیشابوری ۴9۳۹

######## BQT:1478
REF: BQT:1478  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 271  OCR-lang: fas

فرومالیدن ۱4۷۸
از آقامت کردن و در جایی‌ماندن هم هت . ۱ طوی و بفارمد مشهور است.
فرومالیدن * بکر اول ولام.:کنایه فرو نجث * صم اول وناتی‌بواو رسیده
از برچیدن وپیچیدن وافشردن باشد . و بنون زده و فنح جیم و اسکون کاف ۰ کرانی
فروما ان « بکر اول و میم بالف | وسنگینیی باش د که درخواب پرمردم افندهویم‌یی
کشید, بمعنی منتظر (۱) باشد که مشق ازادشلر | کابوی و عبدالجنه کوبند ‎٩‏ - واطراف وپیرامون
بای حطی است , بمعنی بداصل و بیداش باشد | نگردد .
- وشخضی‌را نز گوبند که(؟)کارهای دنی و سغل و ۱ ۱
نذه اس ن! رز شک ۷
کند ۴ - و بی‌هنر وفقیررا هم کفته‌اند . رد ی رر فده بممتی گر ون
1 ست که چوب پس درخانه باشد.
فرومد؟ - بنتح اول و میم و مسکون : 6
(۱) خم ۱: منظره. (۲) چش: + در . (۳) چش: -کوچه .
۰ حافظ شبرازی ۰.۱۶۹
۴ - و معزول شدن : « دوست دبوانی را فراغت دیدار دوستان وقتی بودکه از عمل‌فرو
۴ - با فرومایه روزکار هیر کز نی بوربا شکر نخوری . «کلستان ۲۳*.
برفنحك » درفنجحك ,فدر سك . ۷ -قی : فرهانج؛ فرنج» فرونچك . ۸ - رك : فرونده.
‎٩‏ - پپلوی ۳۵۷۵۳ ۰ ابرانی باستان - 01۳2۷2۳11 » اوستا - 5131 ۲82۷2«بارتولمه
لش لیب رکه 4 ۶ تاوادیا ۱۹۹ > « هناسی ۲۷۳ :۰.۶۲ فروزتی ( فروشی) با فرور(فرورد)
از دوجزء تر کیب پافته : فره 6۳2 با فرا 1۲2 (پیش) + ور ۷2۳ ( پوشاندن . نگپداری کردن؛
پناه بخشیدن ). طبق مندرجات اوستا فروشی ( فرورتی ) نیروبی است که اهورمزدا برای‌نگهداری
آفریدکان بيك ایزدی ازآسمان فرو فرستاده و نیروبی‌است که سراسر آفربنش نيك از پرنوان
پایدارامت. پیش ازانکه اهورمزدا جهان خاکی ۳
را بیافربند . فروهر هر يك از آفریدکان‌نيك ار
۰ ۰ ۰ ۰ ۱ هت یت ۸ یج
هريك را بنوبة خود برای نگپداری آنافریدة ۳ ی
۱
جهان خاکی فرو میفرستد و پس از هرک آن ری
آفریده, فروهی او دیگرباره بنویآسمان گراید فروهی مزدا
بدیدن وی میآید وآن هنگام جشن فروردین امت یعنی روزهایی که برای فرودآمدن فروهرهای
بیاکان ویاکان اختصاس دارد. ۶ پورداود فاب ٩اص4ه‏ >؛ «پوردآود. بشتها ج ۱ م۵۹۸۲ - 1۹*۲
«حورقلیا بقلم‌نگارنده . مجلة داشکدهة ادبیات ۳:۱».
```


## [2026-10-17T00:05:39.533Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *بارو\\b\\|بارو -\\|بارو ۱\\|بارو *-\" BQT_v1_pages.txt | head; grep -n \"برزن\" BQT_v1_pages.txt | head; grep -n \"بهرام *[-۱۲]\" BQT_v1_pages.txt | head -5; grep -n \"پروار\" BQT_v1_pages.txt | head -5"
}
```


### [2026-10-17T00:05:40.032Z] TOOL RESULT

```
16608:بارو عه بر وژن جارو » حصار و قلمه را
16610:بارو د بادال » بر وزن و ععنی‌باروت
16614:بارود نه - بتح نات و زای هوز
16616:باروده » با زای حوز بر وزن پالوده.
7036:که پرشماعة کافورشدکه‌وبرزن . عمسق
15969:چو قهر آورد سوی خاورکریغ هم از باختر برزند بازتیغ . عنصری باخی.
18532:و باآتدر تموزی‌مه ببارد جراد منتشر بربام وبرزن . «منوچپری دامفانی۵۸ »
18558:است - و بمعنی برزن هم آمده است- و صجرا
19305:۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
19406:زد کااد - باکاف بروزن‌شرمسار»برزنگر
19651:کوند کد برزنگران در میان خودکرده باشند .
20501:پالاش ۱ « بتح اول برزن لواش » نام
26439:آن فنجکشت است . اکر شهوت برزنان غلبه
32138:الارب نویری آعده «گاء شماری مي ۰۳۳۸ گوبند هر گاه نیشتر از آسمان سربرزند وبدرخشد»
6573:4 آتش بهرام - باآنرهرام , آشکد‌های بزرکه را پارسیان آش‌بهرام نامند ودربرابر
2947:مثال۳- دمتواری بفتح ۴ بروزن پرواری» بنپان‌شده باشد که مقا بل
25066:پر وادهه بروژن انگاره » بمعنی‌پروار
25195:۳۹+ ۳ ۳ رژد: پروار:
```


## [2026-10-17T00:05:48.647Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16600,16640p BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1<16608' | tail -1"
}
```


### [2026-10-17T00:05:49.139Z] TOOL RESULT

```
بار مان - بر وزن آرمان » نلم‌یکی از
بپلوانان ئوران است .
تجمل و حشمت و بزرگی باشد - و حنت نهادن
بر کسی - و پروانه وفرمان ورضا و رخصت‌دادن
باشد بدخول خانةٌ سلاطین - و بمعنی نازش
و مباهات - و لقب‌نيك وتفاخر + غرورهم‌هست
و بمعتی مدح و نعت هم بنظر آمده است.
بار نهادن - کنابه از زادن باشد .
بارو عه بر وژن جارو » حصار و قلمه را
گونتد . #۶
بارو د بادال » بر وزن و ععنی‌باروت
باشد که داروی تفنگه است: و بلخت سر بانی‌شوره
را گوبندکه جزو اعظم باروت باشد و آنرا نمك
چینی هم گونند ۴
بارود نه - بتح نات و زای هوز
و ون و سکون رابع » نلم فواٍبیست از موسیقی .
باروده » با زای حوز بر وزن پالوده.
خوراك و فوت‌هرروزه باشد- و ضروری‌وها:<تاح
هر روزه رانیز گویند از جامه و زبرجامه وامث
آن - و جامةٌ کهنه را نیز گفته‌اند .
بادوق » بر وزن فاروق ۰ بلخت رومی
باژه - بر وزن‌خاره ؛ دیوار و حمارقلمه
و شپر را کوبند ٩‏ - و کرت و مرنیت و خوبت
را نیز کفته‌اند - و بمعنی دوست هم آمده است
همچو: علام باره ,یمنی پسر دوست ۷ - و بمعئی
حق و شان هم حست چنانکه گونند : «درسارة
فلان؟ بعنی درحق فلان و در شان فلان‌سوبمعنی
۱ - ميي‌خو رکه مخشی زر و بلرکی
؟ ‏ زیان تنا گردر گاه مصطفی بهتر
۴ مثل ملك و ملك بوز کار
6 60۵56 دلك س۲۰۱*.
تست شهرت‌طلب و خسرو شاعزباره
۵ باروت ‏ رك : بارود .
/ بر هان فاطع ترا۲۱۷
طرز و روش ٩‏ -و قاعده وفانون باشد وعشرویی
را یز کنته‌اند مست کننده که آنرا از آرد برنج
وارزن و امثال آن سازند وحریی‌ابین خوانند ۲-
وهر چیز زشت را یز گویند- و بعنی زلف هم
هبت- و گله و رمة کاو و گوسفند واسب وامثال
آن باشد. و اسپ را یز گوبند که بعربی فری
خواند ؟ .
```


## [2026-10-17T00:05:55.556Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *برزن\\|برزن [-»]\" BQT_v1_pages.txt | head; grep -n \"varəzəna\\|varazana\\|vardana\\|verezena\" BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:05:55.831Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:06:00.399Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"رزن\" BQT_v1_pages.txt | sed -n 1,60p | cut -c1-150 | grep -v \"وزن\" | head -30"
}
```


### [2026-10-17T00:06:00.955Z] TOOL RESULT

```
1348:ابنك‌در آ ربابجان بقابای آذری کهن ببنوان هرزندی , حسنوء فره چولی, خلخالی و ناتی تکلم
1452:و تحامل‌ورزند. ازیکی از اصحاب معدانی شنیدم که میگفت: یکیازملوك
1897:ساسانی نوشته وه کرزن داتش» نیز نام بافته - دیگر «سالةٌ « زر دست افشار » که دادیوبه‌ابن‌هوش
3919:آهمند کی زا گویند که دروغ‌گوید تافریپ دهد [ مثل مادرزن
4378:رزنبرگ. پطر زبورگ ۱۹۰6 میلادی.
5112:اسلامی بسیاری ازشهرها را بیکی از فرزندان ونوادگان نوح نسبت داده‌اند ونام شهر را نام پانی
6448:خوانند؟ گویندا گرزن‌خامله
6449:بخورد فرزندش خوشخوی )۱(
6550:نیز کوبند . * سنغنان عاشقانهٌ پر سوز از اوسرزند + ومردم تیز
6770:باشد که ازآرد برفج با آرد جو یا آرزن و امتال
7036:که پرشماعة کافورشدکه‌وبرزن . عمسق
8711:کگفت ده .که همه فوم باوی خواهند رفت » وفرزندان بجمله آماده‌اند »که زشت بود باوی‌ایشان
9588:نشود ا.« ابر » که در عربی بمعنی نره و فرزند فررینه است و 26779)2(8 هزوارش پمعنی آلت
9686:اسمعیل از او متولد کردید . بعد ها ابراهيم پسوی جنوب « جرار » سفر کرد و در اینجا فرزنه
9954:داثرة الممارف اسلام » م رکب از انا و بکه (ییگه) بعنی پدر بزر که , عملم . حودب فرزند‎ «
10149:شرابی‌باشد که از آرد ارزن وجو و امتال آن‌سازند.
10191:و آرد ارزن سازند .
10627:نیز نام دشتی درفاری که آنرا ارزن وارجن وارجنه هم کفته‌اند . این‌البلخی در فارسنامه (ص۱۵)
10628:گوبد : مرغزار دشت ارزن » این مرغزارکه برکنار بحیره ارزن است وببشه است ومعدن شیر »
10639:« کل کلاب * ۱ ارزن
10689:را کوید که از آرد ارزن یخته باشند .
10796:ار غاب - بر رزن چرخاب » بمعنی
11753:و تضیرزند را جضم اول نیز گفته‌اند 4 - وبکس
12335:مدازآن فرزند بوجود
12401:و بنون زده » نام پدرزن وامق است وعاقبت او
13663:که آنرا کاوری و ارزن کوبند .
13846:کنند زود بزایند و اکر باشیرزنان سح قکنند
13875:ی رزن
14028:و مرزنگوش را نیز گوبند و آن نومی آزرباحین
14062:افحوخ - بررزن مطبوخ . چن‌وشکن
```


## [2026-10-17T00:06:07.928Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"۲۵۴\\|۲۵۳\\|۲۵۵\" BQT_v1_pages.txt | head; grep -n \"۳۲۴\\|۳۹۱\" BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:06:08.413Z] TOOL RESULT

```
656:و 1۱6۵۵۳9۲۵۵ 0عی5 (مقر سغدیان) :در بوتانی 5080101 با
787:2 2۵ ۵۱0۵۳۲۵۵۵۵۸ رانا ۷ .۲
792:0۳80-00۵۲۵۵۵ 5061616 12 06 100۳۲۱۱۵۸1 از حاعوع(ه
800:ما 1۳21:۲۵۵۸ ر ۳۳۸۲۷۱۷۲۸۲ . ۸ .۸
847:. 6 . ۷0۵۵۸۵۲ ,۲۱08 ,0 هر . ۳۵26۵ ۵۳62۵1۲۵۲۵۵۵
854:(۲۲6۳۱۵- ۲۵۳
892:۴ - 2۳0۳۵۱0 , ۲۵۳۵۲5۹6۵8 , ۲۵۸00۵0 ۱928 ,۳. 6 ۰
895:۰ . ۵ , ۸۲2۳۵۴ ۱۵۵ ۳۵۲۵۵۲ 06۲ عاطء‌نطع9ع0 , و۵1۵6(
923:۲۵۴2۵۲ نا ۵۵۵2۲ ۱۵۲۵۵۵۱۵۵6 , عصوطه۱۷:۵0 صد۷ [ ۸
925:-0۵۵۲ 6] ,6۷۱ ۷۲.5۷۱۷۵۱۳: ۱94۱ ط۲2۱ نام .عمع۱ :۲۵۵2 ۶ع)۲۳۱2۸۱66] ععل
3954:۲- نقل‌از فپرست کنابضانهستانه . ج ۲ص‌۳۹۱-۳۹۵.
17382:د بایستن - در پهلوی 202228420 «منای ۲۹ : ۲» *«اونوالا۳۲۴» و 0هال(22د.
27051:و در شهرمور ۱۳۲۴از
27762:۲ «اسثق ۰۳۹۱ .
28155:اتواریح ص ۳۹۱ >
29017:۳۳۵۵۱66 ۳6۳۵۱۵۸ عطا ۵۲ ۳۱5/۵۲۷ ,۵۱۳۹۱620 . ۲ . ۸ (ه
```


## [2026-10-17T00:06:14.326Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"بهرام\" BQT_v1_pages.txt | cut -c1-160 | sed -n 1,40p"
}
```


### [2026-10-17T00:06:14.645Z] TOOL RESULT

```
439:شابور - بهرام دوم‌جای‌مانده : يكسنگنپشتة کو تاهدر نقش‌رجب؛ يكسنگنیشتة
441:رستم و درسر مشهد . درهمن سرمشید آثاری از بهرام دوم( ۲۹۲-۲۷۵ )
1115:ولیز در « کشتن هرمز وسیماه برزین ؛بهرام آنر مهانرا» آرد ٩‏ :
3391:و جماعتی بر آنند که وضع این زءان در زمان جمشید شد؛ وبعضی دیگر گویند در زمان بهرام»
6281:ببهرام داد ان زمان دخترش
6533:۵ آتشان - پهلوی طألاأکقاك بمعنی آتشکده - آنشکد؛ بهرام « تاوادبا ۱۵۹ >.
6573:4 آتش بهرام - باآنرهرام , آشکد‌های بزرکه را پارسیان آش‌بهرام نامند ودربرابر
6575:آت‌بهرام و درحدود سد ٩‏ گیاری است . «مزدسنا ۲۳۳* .۰ آتش بهرام لباهش - یکی ازدماز
6928:نوش ۳ - آنر بهرام ؛ - آنرآین ه ‏ آنرخرین
8553:]له _ مخفف آگاه» رك : ۲گاه. آیاری - رك : آتش بهرام .
15608:بهرام چوین هم‌هست . ۱
16696:باشدبموجب‌قرارداد زراشت‌بهرام ۵, وهراسنیری
18186:حهودی که بهرام مال او را بلثبك مقا داد ۴ -
21580:و زرشت بهرام کوبد :
21910:ومصالحی که در روز بهرام وافع میشود باو تعلق
21919:هرمزین نوشیروان که اورا بهرام‌چوبین میکفتند
21933:آمده که بهرام بار و همراء مهر ( فرشتة رزم ) و پاسبان عهد
21934:و پیبان است - پشت چهلردهم اوشا بنام«بهرام بشت * است.
21935:آش ورهرام ( بهرام ) که بجای 6824۳607916 عسوبانت "
21936:راب مخصوص باایزد پیروزی» بهرام دارد - نگهبانی روز بیستم
21937:هرهاه شمسی بدین فرشته سیرده شده و دد ادببات‌ها بهرام گاه
21939:اسم کیاء ( منسوب ببهرام ) و گاه نلم یکی از ناهن بثلم
21941:- بهرام نام پنج پادشاه ساسانی است: بیرام. اول ( ۷۷۳
21958:بهرامن است که بافوت سرخ ۵ -و بافتهابرشمی
21963:۴ . رك : بهرام . ۴
22939:ب ی آب شود خنجر بهرام ات . خن
24368:سامان وئجمل در زمان بهرام کور"و بهرام سامان
25210:(پسوند ) لفة بمعنی مربی؛ توییت کننده : کوبند بهرام گور روزی پیش سمان منذر ابستاده بود
26761:رای قنوج است و او در حبالةٌ بهرام گور بود .
28297:دبهرامی. بنقل لغت‌فری *۱۹*.
```


## [2026-10-17T00:06:52.734Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21895,21945p BQT_v1_pages.txt"
}
```


### [2026-10-17T00:06:53.181Z] TOOL RESULT

```
خسه ممترقه ودر فارسی ينجهٌ دزدیده و بهیزك ( نه: بهترك) ودر پهلوی وهيجك وپنجه وپنج وه
رکاه واند رگاه و روزهای کانها نامیدماند باسم پنج فصل نپا . دردینکرد قطبم سنجانا , ج ٩‏
ص ۵۷۱۲ ۵۹۸ وهی ۳1 رك: خرده‌اوستا ۲۱۱-۲۱۰ واتفهیپم ۲ دیشکرت(ج۳.
نر س ۳۹-۳۰) صراحة ازدونوع سال شممی ابرانیان یمنی سالعرفی وسال بهیز کی (مکیوی) یاد
شده. سالعرفی راسال «وهیژ کيك روج بعنی دارای کبيءة روزهاوسال ابت‌راسال «وهیر کياكزمان»
بمنی دارای کبيسة ساعات‌میخواندند. این کور اضافی درفریب *۱۲سال. یکماه تمام میشد ودرسال
بهی ز کی جبران و تکماه برسال اضافه میکردند. اه شماری .
۵ بهارستان - بفتح‌اول (مر کب‌از: بهار +-ستان). جایی که‌شکوفه و کلپ ای کوتا کون
درآن انبوه باشد نام کتاب منئور عبد الرحمن جامی بسبك گلستان سمدی < دائرفالمعارف اسلام*.
ونیز بپارستان چین- رك: ص۳۲۲ ح۸. ۵ بهافه - بفتح اول. پپلوی ۷۵2 «ناوادبا ۱۹۹.بهزا
است ۱- ودر عربی بمعنی عجب ازتعجب_ وحلااه
ازهللا کت باشد .
لور آح بر وزن صحرا » بعنی ار جهت
چیزی وازبرای چیزی باشد.
بر ۴۴۷ » بروزن‌فرجامء نام فرشته‌است
ومصالحی که در روز بهرام وافع میشود باو تعلق
و اقلیم سیم از ءنسویات اوست - و للم پادشاهی"
هم بوده است در عراق‌که او را رام گور
میگفتند » ببب آنکه پیوسته شکار کور خر
کردی دار سر بزدجرد ائم بود - گویند مد
چهار سال در ملأث او کسی نمرد وپادشاهی او در
دور زهره بود چه در زمان او ساز و نوا رواجی
تمام داشت - ویمعنی گل کاجیره هم‌بنظر آهده
است که بحریی عفر خوانند - و نام سرلشکر
هرمزین نوشیروان که اورا بهرام‌چوبین میکفتند
دارد. ونام روز ستم ازهرماه شمسی باشد و نم
- -انسکریت 0180754 «اسفا ۱ : ۲ ص۲۳» همرشةٌ 03۲2 (سهم . حصه)» ورپارسی باستان
۵ اوستا 02۷۵00۳2 «اسفا ۱ :۲ س ۸۱> : بهلوی ۲ط08 . 0891 «امفا ۱ : ۲
س ٩۵‏ ازرشة طوعو «ثی رگد 6۹ * منای ۲5۹۹ » ۶ بارتولمد۹۲۳ . ۳ در اوستا
۷۵/۵۵/2۵ ۰ پهلری ۷۵۲۳۵۵ , ۷2۳۵۲۵۲ ۰ ۷۵۵۲۵۵ آمده < تب رکه ۲۳۳ >
بمحنی پیروز هند . اصلا مر کب است ار دو جزو : ۷۵۲۵013۳2 اوستابی و ۷۴۱0۶۵ ساسکریت
بمنی اادهایی که بادان دا محبوی میدادد و آرباییان آنرا بز رکترین دشمن خود محصوب
حیداشتند , جزو دوم 81087 اوستابی و 288 ساسکربت از حصمر 88[ ابرانی باستان و 2
اوستا , بهء‌عنی زدن و کشئن . ورثرغنه اوستا و ۷۲۸/۲22810 ساسکرت لفة بمعنی ورنرا کش ۰
فانل دشمن. این نام بزرکترین و محترم نرین لقبی است که بخدابانی که بورنره حمله میکردند
متوضا 8 (رب‌النوع رعد) داده میشد. «مزدبسنا ص ۳۵*- همین عفپوم دردین قدیم آرمنی
بنام ۷2188315 ( خدای اژوها کش ) آمده است . نیز در ارمنی ۷۵1810 و مردم گرجستان
0 کومند. ریییکی از ایزوان‌بساریز که مزدبسناست ودرهمام همیاية سروش است_درمهربشت
آمده که بهرام بار و همراء مهر ( فرشتة رزم ) و پاسبان عهد
و پیبان است - پشت چهلردهم اوشا بنام«بهرام بشت * است.
آش ورهرام ( بهرام ) که بجای 6824۳607916 عسوبانت "
راب مخصوص باایزد پیروزی» بهرام دارد - نگهبانی روز بیستم
هرهاه شمسی بدین فرشته سیرده شده و دد ادببات‌ها بهرام گاه
اسم ایزد پیروزی . گاه روز بیسم ماه , کاه ستار هریخ » گاه
اسم کیاء ( منسوب ببهرام ) و گاه نلم یکی از ناهن بثلم
ای رو ی کور آهده . « روژ شماری 4۸ -
- بهرام نام پنج پادشاه ساسانی است: بیرام. اول ( ۷۷۳
ید گرد اول.. ۴ -ره؛ ۶ تربتنن. ساسان. ص۳ یمد ۰0۰۵۸4۷۱ ۲ بعد.ی ۳۹ ده
بهر ام تل - هی مر فج توح
کتک
هر اهج -_بنتح میم و سکون جيم .
```


## [2026-10-17T00:07:03.227Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25040,25070p BQT_v1_pages.txt; sed -n 25185,25200p BQT_v1_pages.txt"
}
```


### [2026-10-17T00:07:03.558Z] TOOL RESULT

```
بالف کشیده . بمعنی طافت و آرام و صبرباشد -
و بمعتی نوجه و التفات‌ورعبت ومیل هم‌هست*۷-
گرا
رك : تون .۰
۶ »> ممرب‌آن» برنکان «اين درید».
٩‏ - رك » پروین .
یز 5 یکوی عاشقان‌آی ار صرسودای ما داری
۴ - راثد: برنج و برنگه .
۲ پهلوی 08۲0130 تاوادبا
سیف اسفرنك «لنت ناعه».
1 ۷۲۸۷ ‌
منگری ع ی « 4 . ۲ یس ۱۸ ۲ , زباکی 021002 « کربرس ۱ * ؛ خوانساری
0 , دزفولی 216042 سالنامةٌ فرهنکه کلپایگان 45؛ مرغ » طائر» مقابل چرنده ؛
و در شم رکله بتشدید آید:
خمانف قد سیاز واندك سای ر‌ بر نله وهردم چاریای. فردوسی طوسی. «لفت. نلمه».و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین
و بمعنی داشتن (۱) و فرات - و پرداخت -
و پرورش - و پرواز هم آ مده‌است.
رواد ۲ « بر وزن خروار » جالوری
بائد کهآ نرا در جای خوبی بندلد و خوراك لابق
دهند نا فربه شود - وخانهة تابسئانی‌وخاناباد گیر
دار را نیز گویند بهء‌نی اطراف آن ثمام پنجره
داشته باشد - و خانه‌ای را نیز گوبند که‌بربالای
خالاً ددگر ساخته باشند و اطرافآن بازباشد -
و بمعن ی گنجینه هم آمده است - و تختهابی را
کویند که سقف خانه را بدان بپوشند - و بول
و پیشاب بیمار را نیز گوبن که پیش طبیب‌برند.
پر وادهه بروژن انگاره » بمعنی‌پروار
است که خانةٌ تابتانی - و بالاخانه  -‏ وکنجیته.
و تختهای خانه پوشیدن باشد - و بمعنی عودسوز
سو فارورة بیمار- وپرورش افته شدم و فربه نیز
آمده است و بعربی حسمن گویند؟ ۰
نگهای دبگر دوزند . و جامهة دو رنگه درهم
یرام کر را شب انسر روز نیز
خوانند - ویمعنی مر 3 هم مدده است وآن نوعی
از سبز؛ باشددر نهایت لطافت وطراوت؟ -وحلفه
زدن لشکی رااکویند از سوار وبیلده ۰ .
فر ود ۰ بر وزن صف شکن » مخثف
پرویزن باشد که‌آردییز است - و هرچیز صوراخ
سوراخ را گویند عموماً ۵.
پروسنان (۱0۱ - بنتع اول وئاك
کونند از هر پیغمی رکه بوده باشد .
۳۹+ ۳ ۳ رژد: پروار:
۴ - پروز سبزه دمید بر نمط آبگیر
۵ - چرخ پنداری خواهد بختن
بقیه ازصفحه ۳۹۲
۵ - پروانه نام عمومی حثرانی
از آنکه رمح غلامان نست بابز نش.
```


## [2026-10-17T00:07:09.948Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{60\\}pairi.v[äa]ra.\\{120\\}\" BRT.txt | head -5; grep -n -o \".\\{40\\}paiti.v[äa]r.\\{120\\}\" BRT.txt | head -5; grep -n -o \".\\{40\\}upairi.v[äa]r.\\{100\\}\" BRT.txt | head -3; grep -n -o \".\\{30\\}fravär.\\{100\\}\" BRT.txt | head -5"
}
```


### [2026-10-17T00:07:10.699Z] TOOL RESULT

```
23300:.92'*;p5;  —  *yffi .vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum  V.  4. 49; *Y.8^^;  —  anyqmla  sutsm  vatfhsnahe N.52(?);  —  vanhS
```


## [2026-10-17T00:07:16.187Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{80\\}\\(Schloss\\|Burg\\)\\b.\\{80\\}\" BRT.txt | grep -i \"var\" | head -8; grep -n -o \".\\{100\\}Abwehr.\\{100\\}\" BRT.txt | grep -i \"v.r.\\?ϑra\\|varo\\|vsr\" | head -5"
}
```


### [2026-10-17T00:07:16.547Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:07:19.556Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c . BRT.txt; grep -n -o \".\\{60\\}Schutzwehr.\\{80\\}\\|.\\{60\\}Umwallung.\\{80\\}\" BRT.txt | head -8"
}
```


### [2026-10-17T00:07:19.879Z] TOOL RESULT

```
30725
15619:vurntt  pairi . .  dru/aj  Yt  y.  7 1.  a)  'Um- wehrung,  Umwallung':  hahra  nmänä  ava- staya  .  .  /rashmb)mca  (sd.)  fravanmca °r?mla  V.  2.
```


## [2026-10-17T00:07:30.760Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15610,15625p BRT.txt | cut -c1-1500"
}
```


### [2026-10-17T00:07:31.104Z] TOOL RESULT

```
•  j.  pairi^sm  Adv.  'um  und  um,  ganz und  gar':  pairika  yä  duiyairya  vispahe atfA3uI  astvats  parsii  p"  ar?hvqm  ava.- Msflyai  (sd.)  "die  F.  des  Misswachses würde  die  Lebenskraft  der  ganzen  körper- lichen Welt  gani  und  gar  entzwei  spalten" ■ytÄ54;    —    ava    ml  Stil  .  .  paröit  p'
BARTMOLOHAa>  Altiiin.  Wb.
zAusdr. /ro/o-  No.  i
•  j.  paoirim  .\dv.:  s.  Sp.  873  u,
•  g.,  j.  pairi-matay-  f.  'Geringschätzung' (Andrer)'*,  sva,  'Selbstüberhebung,  Hoffart': akSl  manatths  sta  Hhnm  .  .  drUjasiä 'tdislä  Y.J2.  3.  A)  als  Dämon:  tarS.- mata  apa.dvarata  'mala  apaJvarata  Vt J-8;  11,15*.
Pü.i  apar  mtnihtlar,  »gl.  zu  F.  J/.  —  ")  VgL iBed.  KV,  /.  59.  3:  nahi  vat  caramäm  autd väsiffha^  parimamsalf  "auch  über  den  letzten ja  von  «uch  denkt  V.  nicht  gering".
•  j.  pairi.yaozdad'ant-  Adj.,  PPA.:  s. yaozdä-.
Vgl.  lU  para.da%ani:
•  j.  pairi  varazäi  Inf.:  s.  unter  varptäi.
•  ').  pairi.vära-  m.  i)  'Schutzwehr,  Wehr'; ta  hl  snaihis  ■vanhas^a  parHasea  *raiia vurntt  pairi . .  dru/aj  Yt  y.  7 1.  a)  'Um- wehrung,  Umwallung':  hahra  nmänä  ava- staya  .  .  /rashmb)mca  (sd.)  fravanmca °r?mla  V.  2.  a6.
ti.  parivära-  m.  'Decke;  Umgebung';  aram. LW.  pareärä  'Vorstadt';  FrMÖllbR  WZKM. S.  97.  —  Pü, ;  pirämin  farvär.
•  j.  pairi.urvaeäta-  Adj.  'der  am  meisten, besten  zu  Grunde  richtet',  mit  Akk.:  tat drvatö  drvatySs^a  asi  [jwV]  karma  gava *ävari^ra  zafarf  .  ,  'Um  "das  ists,  was am  besten  des  Gottlosen  Augen , .  zu  Grunde richtet"  Yt  n.  2.
Superl.  lamV.ivar-;  aus  ar.  *gfaif'ßlha-;  der Superl.  setzt  ein  mit  pairi.vätaya-  gleichbe- deutendes Praes.  24  'pairi.urvaya-  voraus,  s. IF.  7-  73-  -  PS-!  ^artinil.
•  j.  pairi.spätay-  f.  'Herumwerfen,  Hin- werfen, Hin{ein)fanenlassen' :  nöil  attqm nöil  varsqm  . .  'ipäiti  apqm  ästryattte  "sie
dby  Google
867
```


## [2026-10-17T00:07:39.584Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{20\\}paiti.v[aä]ra.\\{200\\}\" BRT.txt | head -4; grep -n -o \".\\{20\\}upairi.v[aä]r.\\{200\\}\\|.\\{20\\}upairi.vär.\\{200\\}\" BRT.txt | head; grep -n -o \"[•]  j.  fravä[^•]\\{0,300\\}\" BRT.txt | head -4"
}
```


### [2026-10-17T00:07:40.045Z] TOOL RESULT

```
23300:.vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum  V.  4. 49; *Y.8^^;  —  anyqmla  sutsm  vatfhsnahe N.52(?);  —  vanhSnS  F.S;  —  asman?m .  ,  yint  maedä  vasle  vaahansm  stfhr- paesanhim  "den
```


## [2026-10-17T00:07:47.245Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"paruzana\" KNT_full.txt | head -3; n=$(grep -n \"^paruzana-\" KNT_full.txt | head -1 | cut -d: -f1); sed -n \"${n},$((n+5))p\" KNT_full.txt"
}
```


### [2026-10-17T00:07:47.555Z] TOOL RESULT

```
6600:pIE 0: paruzana-, vispazana-, Varkazana-, vaz- 
27340:See also paruzana-. рати) nsm. ($114, $127, 
27372:paruzana- adj. ‘having many men, or many 
paruzana- adj. ‘having many men, or many 
kinds of men’ (‘having men of all tongues’, Wb. 
ZfA 44.165, after the Akk.): paru- ‘many’ + 
zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- 
zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. 
poruvzandndm (523.1) XPb 15f; XPd 11. раги
```


## [2026-10-17T00:07:54.975Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/546.* 2>/dev/null; python3 -c \"\nfrom PIL import Image; im=Image.open('site/pages/546.jpg'); print(im.size)\""
}
```


### [2026-10-17T00:07:55.564Z] TOOL RESULT

```
Exit code 1
site/pages/546.jpg
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('site/pages/546.jpg'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-17T00:07:58.049Z] TOOL CALL #77: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/546.jpg"
}
```


### [2026-10-17T00:07:58.086Z] TOOL RESULT

```

```


## [2026-10-17T00:08:04.461Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wer-",
 "prompt": "Give the meaning(s) and all listed derivatives, especially Indo-Iranian (Sanskrit vṛṇoti, vṛtra, varūtha; Avestan var-, vərəθra-, vara-), Latin aperio/operio, Germanic."
}
```


## [2026-10-17T00:08:05.299Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wr̥θrajánah",
 "prompt": "Give etymology and descendants verbatim (Avestan, Parthian, Middle Persian, Persian)."
}
```


### [2026-10-17T00:08:06.084Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:08:09.864Z] TOOL RESULT

```
# Proto-Indo-European Root *h₂wer-

## Meanings
According to Wiktionary, this root has two primary definitions:
1. "to lift, to raise"
2. "to cover, to enclose, to bind"

## Listed Derivatives

**Indo-Iranian:**
- Sanskrit: वृणोति (vṛṇóti, "to cover, ward off") from *h₂wr̥-né-ti

**Latin:**
- aperīō ("to open")
- operīō ("to cover")

**Greek:**
- Ancient Greek ἀείρω (aeírō, "to lift, raise")

**Albanian:**
- vjerr ("to hang, suspend")

**Other:**
- Old Armenian գեր (ger, "above, hyper-")

The page notes that "37" derived terms exist in total, though only select examples are detailed in the reconstructed entry. Germanic descendants are referenced in the original request but not explicitly detailed in this Wiktionary article excerpt.
```


## [2026-10-17T00:08:11.044Z] AGENT

Now archive the web sources.


## [2026-10-17T00:08:16.490Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/گیج|p546 Wer3 node11 gij: cognates (Sogd. kyc), NW Iranian loan, no IE root\" \"https://en.wiktionary.org/wiki/دیوار|p546 Wer3 node4 divar < MP dēwār < OP didā + *-wāra\" \"https://en.wiktionary.org/wiki/بهرام|p546 Wer3 node8-10 Bahram < Av. vərəθraγna\" \"https://en.wiktionary.org/wiki/فروردین|p546 Wer3 node7 Farvardin < MP frawardīn\" \"https://en.wiktionary.org/wiki/فروهر|p546 Wer3 node6-7 farvahar < MP frawahr < OP *fravarti-\" \"https://en.wiktionary.org/wiki/برزن|p546 Wer3 node2 barzan borrowed from NW Iranian\" \"https://en.wiktionary.org/wiki/aperio|p546 Wer3 node12 aperio < *h2wer- cover, shut\" \"https://en.wiktionary.org/wiki/cover|p546 Wer3 node13 cover < OF covrir < Lat. cooperire\" \"https://en.wiktionary.org/wiki/warn|p546 Wer3 node14-15 warn < PIE *wer- be aware\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wer-|p546 Wer3 root: *h2wer- to cover, enclose\" \"https://en.wiktionary.org/wiki/بارو|p546 Wer3 node2 baru: no etymology on Wiktionary\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done",
 "timeout": 300000
}
```


### [2026-10-17T00:08:19.862Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b261d9e5ce587318.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c29457feb48b6fb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2683df65d9a0d4c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bbdc6f97b578c142.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4a09145c7be8f12e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4aa3410255649a02.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e10bd8e1992dff75.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d0871b56c60a50e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/843a73f2e16051b6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a859f6d3ed652c08.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d70dc5a7b2d80958.txt
```


## [2026-10-17T00:08:23.101Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^WARN\\|^Warn\\|^COVER\\|^Cover\\|^APERTURE\\|^Aperture\" SKT.txt | head; grep -n -i \"^warn,\\|^cover,\\|^aperture,\" KLN_1971.txt | head"
}
```


### [2026-10-17T00:08:23.361Z] TOOL RESULT

```
21203:Warn .  see  Wary.
17023:aperture, n., an opening. — L. apert ur a, ‘an ope- 
37798:cover, hide, conceal’, which is rei. to xaXuj 3 yj, 
58561:cover, tr. v. — OF. covrir, cuvrir (F. couvrir), fr. 
108825:cover, hide, conceal’, OIr.ctf/Ve, ‘cellar, magazine’, 
113558:cover, hide, conceal’. See custody and cp. next 
116250:cover, hide’. See hide, v. and cp. hoard, hose, 
154569:warn, advise, instruct’. L. mbnstrare, ‘to show, 
162815:warn, to communicate secretly’, ME. nyrnen , ‘to 
265096:warn, tr. v. . — ME. warnien, warnen, fr. OE. 
265928:cover, covert, louver, operculum, overt, varna.
```


## [2026-10-17T00:08:25.926Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 265096,265102p KLN_1971.txt; sed -n 58561,58566p KLN_1971.txt; sed -n 17023,17027p KLN_1971.txt; sed -n 265920,265930p KLN_1971.txt; grep -n \"^Wary\" SKT.txt; n=$(grep -n \"^Wary\" SKT.txt|head -1|cut -d: -f1); sed -n \"$n,$((n+8))p\" SKT.txt"
}
```


### [2026-10-17T00:08:26.409Z] TOOL RESULT

```
Exit code 1
warn, tr. v. . — ME. warnien, warnen, fr. OE. 
warnian, warenian, ‘to warn, admonish’, rel. to 
MDu. waernen, ‘to provide, warn’, ON. varna , 
‘to admonish’, OHG. war non, ‘to take heed*, 
MHG., G. warnen, ‘to warn’, and to OE. wxr, 
‘aware, cautious’. See ware, ‘alert’, and cp. words 
there referred to. Cp. also garnish. 
cover, tr. v. — OF. covrir, cuvrir (F. couvrir), fr. 
L. cooperire , ‘to cover wholly, cover’, fr. co- 
and operire, ‘to cover’, for * op -we r ire, which is 
formed fr. ob, ‘toward’, and I.-E. base *wer~, 
‘to enclose, cover’. See ob- and weir and cp. 
aperient, operculum. Cp. also the first element 
aperture, n., an opening. — L. apert ur a, ‘an ope- 
ning’, fr. apertus , pp. of aperire. See aperient and 
-ore. 

Derivatives: apertur-al, apertur-ed , adjs. 
'inner dike’, vdrii-tham , ‘protection’, varu-tar 
‘protector’, Avestic vere&ra-, ‘weir’. Alb. va&e 
(for *wor-ta-), ‘enclosure, fence, fold’, OIr. fe- 
ronn, ‘field’, prop, ‘enclosed land’, Gk. £pua&oci 
(for *f£poCT&aL), ‘to guard, rescue’. Cp. garret, 
garrison, the first element in wehrmacht and the 
second element in landwehr. Cp. also aperient, 
aperitif, aperitive, apert, aperture, apricate, 
cover, covert, louver, operculum, overt, varna. 
Derivative: weir, tr. v. 

sed: -e expression #1, char 1: unknown command: ','
```


## [2026-10-17T00:08:29.204Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n \"دیوار\\|بهرام\\|فروهر\\|پروار\\|بارو\" ARY_pages.txt | head -15 | cut -c1-200"
}
```


### [2026-10-17T00:08:29.496Z] TOOL RESULT

```
218:همین علت است که نقش‌های دیواری یافت شده در تورفان و تارم آنها را با موی سرخ و چشمان آبی
700:ایرانی را نشان می‌دهد. گورهای آذربایجان (مثل کورگان‌های اوکرائین) دارای دیواره‌ی چوبی بوده
1284:31۸ (به معنی دیوار)» در آلمانی کهن شده است 7810 (به معنی خمیر)؛ در یونانی شده است
3551:887 بسپار شبیه به نظر می‌رسد. در دوران پیش از اسلام عرب‌های عربستان دارای برج و بارو نبودند و می‌دانیم که
4514:۲- واژه‌ی اوستایی از دو اجريشه درست شده است: ۳۸13 (به چم "دور" و "پیرامون") و 3۸122۸ (به چم "آدیوار»)
4515:(بازگشت به: دیوار)
8169:۱ بازگشت به: دیوار. :
8170:۲ چم این واژه در زبان‌های ایرانی باستان و یرنانی؛ دیوار,
8739:دیوار /] ۲۹۷
11282:چم این واژه در انگلیسی کهن و انگلیسی نوین: تاقچه» شکاف دیوار..
```


## [2026-10-17T00:08:31.347Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 8715,8745p ARY_pages.txt | cut -c1-250"
}
```


### [2026-10-17T00:08:31.706Z] TOOL RESULT

```
اوستی (0558716): ۰.8۸ 58 ,16

کردی (0201571:): اند اسلاوی کهن (70/ما5 #ل#6نالل صان):

سانسکریت (8445877): 085 2

یونانی (02880): 28 لیتوانی (/(1۸م۸لال771.): نایدا

لاتین (7100ما)د تشه لتونی (لتی) (/7014مل): ند

فرانسه (۳5۸۲[7): 0218 پروسی کهن (7(ف۲۴-551 0ا0).

اسپانیایی (۸/]8ط5): 0085 : 58 و1257۷7۸8

ایتالیایی (۵(۷ال7۸): 210 ایرلندی کهن (570ل12 صا0): 0۸

رومانی ((۵ا ۸1۸2 ): [ا78 گالی (0703[7): -080

پرتغالی (۳071001858): نراد . ولزی (58977): 12

ایسلندی‌کهن (0100/40/هشی5 صا0): برترنی (88870/0): 001
3 أ
[pdf page 296]
دیوار /] ۲۹۷
پسگشت‌ها مرت ی 3 (05770) +57
زا 8 ننک مه
2 (018) :ما05 0 ((0810) 0
0 ((0510) :8 ۲۵(/2 ۸۸ برهان قاطع : ۹1۷
3115 لاه
یادداشت: له پم
```


## [2026-10-17T00:11:38.104Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-546.py <<'EOF'\nimport json\nW = {\n \"gij\": \"https://en.wiktionary.org/wiki/گیج\",\n \"divar\": \"https://en.wiktionary.org/wiki/دیوار\",\n \"bahram\": \"https://en.wiktionary.org/wiki/بهرام\",\n \"farv\": \"https://en.wiktionary.org/wiki/فروردین\",\n \"farvahar\": \"https://en.wiktionary.org/wiki/فروهر\",\n \"barzan\": \"https://en.wiktionary.org/wiki/برزن\",\n \"baru\": \"https://en.wiktionary.org/wiki/بارو\",\n \"aperio\": \"https://en.wiktionary.org/wiki/aperio\",\n \"cover\": \"https://en.wiktionary.org/wiki/cover\",\n \"warn\": \"https://en.wiktionary.org/wiki/warn\",\n \"root\": \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wer-\",\n}\nPOK1116 = {\"ref\": \"POK:1116\", \"status\": \"not_found\", \"note\": \"POK_03.txt leaves 357-359 (printed pp. 1115-1117) hold ue-, uebh- 'weben', uedh- 'stoßen' and ued- 'Pfand': no uer- 'cover' on p. 1116. The root Nourai means is on pp. 1160-1162: POK_full.txt l.91991ff. 'uer-5 ... Meaning: to close, cover; to guard, save ... Avestan Akt. varanav-, Med. varan- cover, wrap ... (Avestan varaθra- Widerstand, Wehr, shield) ... vara- (Avestan -vara-) Deckung, Wehr ... Page(s): 1160-1162'. So 1116 is probably a slip for 1160.\"}\nWLD_I280 = {\"src\": \"WLD\", \"where\": \"Bd. I 280-282, s.v. 7. uer- (WLD_Bd1_pages.txt l.26516-26640)\", \"stance\": \"supports\", \"note\": \"'7. uer- bedecken, woraus durch Verschließen schützen, verschließen, retten, abwehren' ... 'lat. operio verschließe (decke zu), aperio öffne' ... 'dehnstufig vāra- m. Deckung, Wehr (ebenso av. -vāra- in Zs., npers. bāra, -vār Wall)' ... 'av. var m. Schloß, Burg ... varəθra- n. Wehr, Schild'.\"}\nAHD5 = {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wer-5 (AHD_watkins1985.txt l.1148-1151)\", \"stance\": \"supports\", \"note\": \"'wer-5. To cover ... *ap-wer-yo- in Latin aperire, to open, uncover: APERTURE ... *op-wer-yo- in Latin operire, to cover: COVER ... O-grade *wor-. Germanic *war-nēn in Old English war(e)nian, to take heed: WARN ... [Pok. 5. uer- 1160.]'\"}\nKNT_var = {\"src\": \"KNT\", \"where\": \"p. 206-207 Lexicon s.v. var-, vardana- (KNT_full.txt l.28774-28844)\", \"stance\": \"supports\", \"note\": \"'var- vb. cover, protect; (mid.) choose, convince: Av. var-, pres. varənav- ... Skt. vṛṇoti, Gt. warjan ward off, Lt. operit covers (from *op-uer-) ... See also duvarθi-, Fravarti-' and 'vardana- sb. town: Av. vərəzəna-, LAv. varəzāna- community, Skt. vṛjána- enclosed space, pIE *uṛĝeno-, to root *uerĝ-, Skt. vṛj-, Gk. eirgō I enclose'.\"}\n\nentry = {\n \"entry\": 0,\n \"root\": \"Wer 3 / Werg 2, Wreg 2, Wrg\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *wer- (Wiktionary *h₂wer-) 'to cover, enclose, ward off' (Pokorny 1160-1162 uer-5; Watkins wer-5); extension *werǵ- 'to enclose, shut in' (Pokorny 1168 uerg-1)\",\n \"note\": \"Both roots are real and the glosses are right: Pokorny uer-5 'to close, cover; to guard, save' (Skt. vṛṇoti, Av. var-, varəθra-, vāra-, Lat. operio/aperio, Gmc. *warjan) and its extension uerg-1 'to close, enclose' (Skt. vrajá-, vṛjána-, Av. vərəzəna-, OP vardana-, Gk. eirgō). Nourai's page POK:1116 is wrong: that page carries uedh- 'strike'; the entry is on pp. 1160-1162 (uerg-1 on p. 1168). Most branches are sound: Lat. operire/aperire > cover, aperture; Av. vāra-/pairi.vāra- > MP dēwār, parwār > NP divâr, parvâr; Av. vərəθra-γna- > MP Wahrām > NP Bahrâm; MP frawahr, frawardīn. The weak points: OP paruzana- 'having many men' belongs to zana- 'man' and has nothing to do with this root (node 1); several Avestan compounds in node 3 are reconstructions, not attested words; warn is put under *wer- 'perceive' by Klein and Wiktionary (only Watkins/Pokorny put it here); gîj has no known IE etymology. The extraction matches the printed page (site/pages/546.jpg).\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *wer- (در ویکی‌واژه *h₂wer-) «پوشاندن، در میان گرفتن، بازداشتن» در پوکورنی (ص ۱۱۶۰-۱۱۶۲، uer-5)، والده-پوکورنی (ج ۱، ص ۲۸۰) و واتکینز (wer-5) آمده است. گونهٔ گسترش‌یافتهٔ آن *werǵ- «در میان گرفتن، بستن» (پوکورنی ص ۱۱۶۸) است و اوستایی vərəzəna- و پارسی باستان vardana- «شهر» از آن است. پس ریشه و معنایی که نورایی داده درست است، ولی شمارهٔ صفحهٔ پوکورنی (۱۱۱۶) نادرست است. بیشتر شاخه‌های نمودار (دیوار، پروار، بهرام، فروردین، cover و aperture) پذیرفتنی است. ولی paru-zana پارسی باستان از zana- «مرد» است و به این ریشه ربطی ندارد. برای «گیج» هم ریشهٔ هندواروپایی شناخته‌ای در دست نیست.\",\n \"sources\": [W[\"root\"], W[\"aperio\"]],\n \"ref_check\": [\n   POK1116,\n   {\"ref\": \"IEC:1599\", \"status\": \"not_checked\", \"note\": \"Local IEC.txt ends at p. 1554 (Mann's supplement pages are not in the OCR). Mann's main entry uer- (1) 'open, close' (IEC.txt l.20025: 'Av. var-, v. cover; Lat. ap-erio open; op-erio close, cover ... Per. bar ... beside di-vār wall') supports the root; p. 1599 itself could not be read.\"}\n ],\n \"consulted\": [\n   WLD_I280, AHD5,\n   {\"src\": \"IEC\", \"where\": \"uer- (1), IEC.txt l.20025; uergo (1) p. 1517-1518\", \"stance\": \"supports\", \"note\": \"'uer- (1) open, close. WP I, 280 Skt. vṛṇómi; Av. var-, v. cover; Lat. ap-erio open; op-erio close, cover ... Per. bar ... beside di-vār wall ... Av. varo garden'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. cover (l.58561) and weir (l.265920)\", \"stance\": \"supports\", \"note\": \"'cover ... L. cooperire ... operire to cover, for *op-werire, formed fr. ob and I.-E. base *wer- to enclose, cover'; s.v. weir: 'Avestic varəθra- weir'.\"}\n ],\n \"nodes\": []\n}\nN = entry[\"nodes\"]\nN.append({\"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"var 6, vara 2, vâra 2; vardana, paru-zana\", \"verdict\": \"disputed\",\n \"derivation\": \"Avestan has the verb var- 'to cover, ward off' (present varənav-, = Skt. vṛṇoti < PIE *wer-/*h₂wer- with a nasal present), the noun vara- 'enclosure' (Yima's var) and the lengthened-grade -vāra- 'cover, wall' in compounds (pairi.vāra-); Old Persian has var- 'cover, protect' in Kent's lexicon. OP vardana- 'town' is the Persian form of Av. vərəzəna- 'community' (Skt. vṛjána- 'enclosed space'), from the extension *werǵ- 'to enclose', with OP d for Iranian *z (< PIE *ǵ); that fits the chart. paru-zana is wrong here: OP paruzana- means 'having many (kinds of) men' (paru- 'many' + zana- 'man, people', PIE *ǵenh₁-) and is not a word for a walled-in place, nor from *wer-.\",\n \"derivation_fa\": \"اوستایی var- «پوشاندن، بازداشتن» (برابر سنسکریت vṛṇoti)، vara- «بارو، جای در میان گرفته» (ور جمشید) و -vāra- «پوشش، دیوار» در واژه‌های مرکب از این ریشه‌اند. پارسی باستان vardana- «شهر» هم برابر اوستایی vərəzəna- است و از *werǵ- «در میان گرفتن» آمده. d پارسی باستان در اینجا برابر z ایرانی است. ولی paru-zana در پارسی باستان یعنی «دارای مردمان بسیار» و از paru- «بسیار» و zana- «مرد، مردم» ساخته شده. به «شهرِ بارودار» و به این ریشه ربطی ندارد. پس این بخش از ادعای نورایی را کنت رد می‌کند.\",\n \"sources\": [W[\"root\"]],\n \"ref_check\": [POK1116,\n   {\"ref\": \"KNT:207\", \"status\": \"supports\", \"note\": \"KNT_full.txt l.28774ff. (pp. 206-207): 'var- vb. cover, protect ... Av. var-, pres. varənav-' and 'vardana- sb. town: Av. vərəzəna- ... Skt. vṛjána- enclosed space, pIE *uṛĝeno-, to root *uerĝ- ... Gk. eirgō I enclose'. Kent's paruzana- (l.27372) is 'having many men, or many kinds of men: paru- many + zana- man', which contradicts Nourai's gloss.\"},\n   {\"ref\": \"AEF:212\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian Horn translation is not on disk.\"},\n   {\"ref\": \"SPG:230\", \"status\": \"not_checked\", \"note\": \"Spiegel's title is uncertain (refs_online.json) and no searchable copy is on disk.\"}],\n \"consulted\": [KNT_var,\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.v. paruzana- (KNT_full.txt l.27372)\", \"stance\": \"contradicts\", \"note\": \"'paruzana- adj. having many men, or many kinds of men (having men of all tongues ...): paru- many + zana- man'.\"},\n   WLD_I280,\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. 2var (NYB_vol2_glossary.txt l.3948)\", \"stance\": \"supports\", \"note\": \"'var enclosure, defences, fortress: ~ i Yam-kart ... — Av. (1363) var-'.\"},\n   {\"src\": \"BRT\", \"where\": \"BRT.txt\", \"stance\": \"silent\", \"note\": \"The OCR of Bartholomae's var-/vara- columns is unreadable; Kent and Nyberg cite Bthl. AiW 1360-1363 for var-.\"}]})\nN.append({\"id\": 2, \"lang\": \"Persian\", \"words\": \"vâr 1; bâru; barzan\", \"verdict\": \"plausible\",\n \"derivation\": \"-vâr 'wall' survives only inside compounds (divâr, parvâr), from Iranian *wāra- (Av. -vāra-), as Walde-Pokorny already noted ('npers. bāra, -vār Wall'). bâre 'castle wall' (also written in the chart) and bâru 'rampart, fortress' (Borhan p. 216: 'بارو: حصار و قلعه') are usually taken from the same *wāra- with Persian b- for Iranian w- (cf. Wahrām > Bahrām); bâru has no published etymology on Wiktionary, so the link is likely but not proven. barzan 'quarter, street' is the NW Iranian counterpart of OP vardana- (Av. vərəzəna-, *werǵ-), with z (not OP d) and b- < w-; Wiktionary calls it a Northwestern Iranian loan, while Hübschmann called its etymology 'vollkommen dunkel'.\",\n \"derivation_fa\": \"«ـوار» به معنی «دیوار» تنها در واژه‌های مرکبی چون «دیوار» و «پروار» مانده است و از ایرانی باستان *wāra- (اوستایی -vāra-) است. «باره» و «بارو» به معنی «حصار و قلعه» را هم معمولاً از همین *wāra- می‌دانند. w آغازی ایرانی در فارسی به b بدل شده، چنان‌که «وهرام» به «بهرام» رسیده. ولی برای «بارو» ریشه‌شناسی چاپ‌شده‌ای نیافتم. «برزن» صورت ایرانی شمال‌غربی همان vardana- پارسی باستان (اوستایی vərəzəna-) است. هوبشمان ریشهٔ آن را تاریک دانسته است. پس ادعای نورایی پذیرفتنی است، اما همهٔ جزئیاتش استوار نیست.\",\n \"sources\": [W[\"barzan\"], W[\"baru\"]],\n \"ref_check\": [{\"ref\": \"BQT:216\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt l.16608 'بارو - بر وزن جارو، حصار و قلعه را گویند' and l.16622 'باره - بر وزن خاره؛ دیوار و حصار قلعه و شهر را گویند' (printed p. 216). The OCR does not show an etymological footnote.\"},\n   {\"ref\": \"BQT:254\", \"status\": \"not_found\", \"note\": \"Searched BQT_v1_pages.txt for the headword برزن; the OCR shows only inflected forms (برزند) and cross-references ('رک: برزن و پریزن', l.19305). The p. 254 entry could not be located.\"},\n   {\"ref\": \"BQT:1473\", \"status\": \"partial\", \"note\": \"ref_page.py BQT:1473 (vol. 3 pdf p. 266): the page holds فروار/فرواره and Mo'in's note that the Avestan source is uncertain; it does not discuss -vār 'wall' itself.\"}],\n \"consulted\": [WLD_I280,\n   {\"src\": \"HUB\", \"where\": \"§ 199 (HUB.txt l.840-851)\", \"stance\": \"partial\", \"note\": \"Hübschmann rejects deriving the NP word from OP vardana- (which 'zu np. *balan geworden wäre') and ends 'Jedenfalls bleibt die Etymologie von barzan noch vollkommen dunkel'.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt grep bārū / barzan\", \"stance\": \"silent\", \"note\": \"Horn has no entry for bārū or barzan.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. 2var (l.3948)\", \"stance\": \"supports\", \"note\": \"'var enclosure, defences, fortress ... Av. var-' (Pahlavi base of the -vār family).\"}]})\nN.append({\"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"děğa-vâra; fra-vârna, upairi-vâra; pairi-vâra; paiti-vâra\", \"verdict\": \"plausible\",\n \"derivation\": \"pairi.vāra- is real Avestan: Bartholomae col. 866-867 'pairi.vāra- m. 1) Schutzwehr, Wehr; 2) Umwehrung, Umwallung (V. 2.26)', glossed in Pahlavi as pērāmōn farvār, = Skt. parivāra-. The other forms are Nourai's reconstructions, not attested words. *daiǰa-/*didā-vāra 'clay wall' is Horn's starred OP *deghavāra- behind divâr (OP didā- 'wall, fortress' + -vāra-). For 'fra-vârna' Mo'in (BQT 1473) says the Avestan form is uncertain ('اوستایی مشخص نیست'). upairi-vāra and paiti-vāra are not found in the dictionaries checked. The prefixes are real (pairi- 'around', upairi- 'over', paiti- 'against'), so the compounds are well formed but hypothetical.\",\n \"derivation_fa\": \"اوستایی pairi.vāra- به معنی «باروی پیرامون، پناهگاه» واژه‌ای واقعی است. بارتولمه آن را آورده و برگردان پهلوی آن «پیرامون فروار» است. صورت‌های دیگر این خانه بازسازی خود نورایی یا دیگران است. «*دیگ‌وار» همان *deghavāra- پارسی باستان است که هرن بازسازی کرده، یعنی didā- «دژ، دیوار» با -vāra-. معین دربارهٔ صورت اوستایی «فروار» می‌گوید «مشخص نیست». upairi-vāra و paiti-vāra را در فرهنگ‌ها نیافتم. پیشوندها درست‌اند و این ترکیب‌ها ساخت درستی دارند، ولی گواهی متنی ندارند. پس سخن نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W[\"divar\"]],\n \"ref_check\": [POK1116,\n   {\"ref\": \"AEF:268\", \"status\": \"not_checked\", \"note\": \"AEF is not on disk; its source, Horn no. 304 (pervār < Av. *pairivārana-, cf. pairi.vāra- 'Wall, Stall'), supports pairi-vâra.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 866-867 s.v. pairi.vāra- (BRT.txt l.15619)\", \"stance\": \"supports\", \"note\": \"'pairi.vāra- m. 1) Schutzwehr, Wehr ... 2) Umwehrung, Umwallung: ... V. 2.26 ... Pü.: pērāmōn farvār'; Skt. 'parivāra- m. Decke; Umgebung; aram. LW. parvārā Vorstadt'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 599 dīvār (HRN.txt l.5350)\", \"stance\": \"supports\", \"note\": \"'599. dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. teichos, osk. feihúss)'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 304 pervār (HRN.txt l.2937ff.)\", \"stance\": \"supports\", \"note\": \"'304. pervār Stall. aw. *pairivārana-, vergl. pairi.vāra- Wall, Stall (vd. 2, 26 vielleicht, Bartholomae); phlv. parvār'.\"},\n   WLD_I280]})\nN.append({\"id\": 4, \"lang\": \"Persian\", \"words\": \"dîvâr; farvâr; parvâr\", \"verdict\": \"plausible\",\n \"derivation\": \"divâr 'wall' < MP dēwār [dywʾl] < OP *didā-vāra- ('fortress-wall', OP didā- 'wall, fortress' from *dʰeyǵʰ- 'knead clay' + -vāra-). MP ē became NP ī, and the first part shrank by haplology. Horn, MacKenzie and Wiktionary agree, so divâr is confirmed. parvâr < MP parwār 'citadel; circumvallation; suburb' (MacKenzie) < *pari-vāra- (Av. pairi.vāra- 'Umwallung'). The sense moved from 'enclosure, pen' to 'stall' and to 'animal fattened in the stall', and separately to 'summer house open on all sides' (Borhan 391). farvâr 'summer house / upper room open on all sides' (Borhan 1473, Rudaki) is the same kind of building, but Mo'in calls its Avestan source uncertain and suggests it may be only a variant of parvâr. So the fra- + vāra analysis is plausible, not proven.\",\n \"derivation_fa\": \"«دیوار» از فارسی میانهٔ dēwār و آن از پارسی باستان *didā-vāra- «دیوارِ دژ» است، از didā- «دژ، دیوار» و -vāra-. ē فارسی میانه در فارسی نو به ī بدل شده است. هرن و مکنزی و ویکی‌واژه همین را می‌گویند. «پروار» از فارسی میانهٔ parwār «دژ، بارو، حومه» و ایرانی باستان *pari-vāra- است. معنی آن از «جای محصور، آغل» به «جانوری که در آغل فربه کنند» و نیز «خانهٔ تابستانی» رسیده است. «فروار» را معین با «پروار» یکی می‌گیرد و می‌گوید صورت اوستایی آن روشن نیست. پس «دیوار» قطعی است و «پروار» و «فروار» با احتیاط پذیرفتنی‌اند.\",\n \"sources\": [W[\"divar\"]],\n \"ref_check\": [\n   {\"ref\": \"BQT:391\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt l.25058ff. (p. 391): 'پروار - بر وزن خروار، جانوری باشد که آنرا در جای خوبی بندند و خوراک لایق دهند تا فربه شود - و خانهٔ تابستانی و خانهٔ بادگیردار را نیز گویند بمعنی اطراف آن تمام پنجره داشته باشد' — exactly Nourai's glosses.\"},\n   {\"ref\": \"BQT:1473\", \"status\": \"partial\", \"note\": \"ref_page.py BQT:1473 (vol. 3 pdf p. 266): 'فروار ... خانهٔ تابستانی ... و بالاخانه‌ای که اطراف آن درها و پنجره‌ها داشته باشد'; Mo'in's note: 'اوستایی مشخص نیست. فروار فارسی با ... (بروار) منطبق است. بعلاوه ممکن است فروار شکل معرب پروار باشد' — the word and gloss are confirmed, the Avestan source is doubted.\"},\n   {\"ref\": \"AEF:268\", \"status\": \"not_checked\", \"note\": \"Not on disk; Horn no. 304 (its source) supports parvâr < *pairivārana-.\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 599 and no. 304\", \"stance\": \"supports\", \"note\": \"'599. dīvār Mauer, Wand. ap. *deghavāra-'; '304. pervār Stall. aw. *pairivārana-, vergl. pairi.vāra- Wall, Stall ... phlv. parvār'.\"},\n   {\"src\": \"PHD\", \"where\": \"pp. 26, 64 s.vv. dēwār, parwār (PHD.txt l.312, l.542)\", \"stance\": \"supports\", \"note\": \"'dēwār [dywʾl | M dywʾr, N ~] wall'; 'parwār [plywʾl | N ~] citadel; circumvallation; suburb, surroundings'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 866-867\", \"stance\": \"supports\", \"note\": \"'pairi.vāra- ... Umwehrung, Umwallung ... Pü.: pērāmōn farvār' (Pahlavi uses farvār for the Avestan word).\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p. 296 s.v. دیوار (ARY_pages.txt l.8739)\", \"stance\": \"silent\", \"note\": \"The entry heading 'دیوار' is present but the OCR of the etymology is unreadable.\"}]})\nN.append({\"id\": 5, \"lang\": \"Avestan / Old Persian\", \"words\": \"fra-var, fra-vahr, fravaši; fra-var-tinam\", \"verdict\": \"plausible\",\n \"derivation\": \"Avestan fravaši- (fravašay-) is the guardian spirit. It comes from Iranian *fra-warti- (OP personal name Fravarti-, Gk. Phraórtēs) with Avestan -š- for *-rt-. The base is fra- 'forth' + var-, but which var- is debated: Mo'in (after Pourdavoud), Kent and Lommel take var- 'cover, protect' ('protecting spirit'), while others prefer var- 'choose, confess' or Bailey's *fra-wṛti- 'valour'. So Nourai's derivation is one accepted view among several. 'fra-vahr' is Middle Persian (frawahr), not Avestan. 'fra-var-tinam' stands for OP *fravartīnām = Av. fravašinąm, genitive plural ('(the month) of the fravašis'), the source of the month name Farvardin; 'descent of holy spirits' describes the Farvardigān feast rather than translating the form.\",\n \"derivation_fa\": \"«فروشی» اوستایی (fravaši-) از ایرانی باستان *fra-warti- است و نام پارسی باستان Fravarti- (فرورتیش) همان است. rt ایرانی در اوستایی به š بدل شده است. این واژه از پیشوند fra- و ریشهٔ var- ساخته شده، ولی دربارهٔ اینکه کدام var- است اختلاف هست. معین و پورداود و کنت آن را var- «پوشاندن، نگهداری کردن» می‌دانند و دیگران var- «برگزیدن، ایمان آوردن» را. پس سخن نورایی یکی از دیدگاه‌های پذیرفته است. fra-vahr صورت فارسی میانه است و اوستایی نیست. fravartīnām حالت اضافی جمع است، یعنی «(ماهِ) فروهرها».\",\n \"sources\": [W[\"farvahar\"], W[\"farv\"]],\n \"ref_check\": [\n   {\"ref\": \"BQT:1478\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1478 (vol. 3 pdf p. 271), Mo'in's footnote on فروهر: 'پهلوی fravahr، ایرانی باستان *fravarti-، اوستا fravaši- ... فروشی (فرورتی) یا فرور از دو جزء ترکیب یافته: فره fra یا فرا (پیش) + ور var (پوشاندن، نگهداری کردن؛ پناه بخشیدن)'.\"},\n   {\"ref\": \"BQT:1476\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1476 (pdf p. 269) s.v. فروردین: 'پهلوی fravartīn مأخوذ از پارسی باستان *fravartīnām جمع مؤنث حالت اضافی کلمهٔ fravarti- (فروهر، فرور) ... در اوستا نیز این کلمه بهیأت اضافه در جمع مؤنث ... همراه اشاون'.\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.v. var- (KNT_full.txt l.28774-28783)\", \"stance\": \"supports\", \"note\": \"'var- vb. cover, protect; (mid.) choose, convince ... (var-, var-, war- of Bthl. AiW 1360-3 ... are reducible to one root) ... See also duvarθi-, Fravarti-'.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. fravahr, fravartin (NYB_vol2_glossary.txt l.1557, 1564)\", \"stance\": \"supports\", \"note\": \"'fravahr ... tutelary genius ... Av. (992 sqq.) fravaši- < *fravarti-, cf OP n. pr. Fravarti-'; 'fravartin ... the first month ... < *fravartinām, Av. fravašinąm, gen. pl. of fravarti-'.\"},\n   {\"src\": \"HUB\", \"where\": \"§ 84 b, p. 190 (HUB.txt l.6708-6713, 6908-6911)\", \"stance\": \"supports\", \"note\": \"'Farvardīn der erste Monat = phl. fravartīn ..., zd. fravašinąm (gen. pl.)'; 'np. farvar = phl. fravahr, zd. fravaši-, ap. *fravarti-'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 992ff. fravaši-\", \"stance\": \"silent\", \"note\": \"Bartholomae's entry is cited by Nyberg (992 sqq.) but the local OCR is unreadable.\"}]})\nN.append({\"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"farvahr; farvartin\", \"verdict\": \"confirmed\",\n \"derivation\": \"MP frawahr [plwʾhl] 'guardian spirit, immortal soul' < *fravarti- (the -rt- > -hr- change typical of SW Middle Persian, cf. *mithra > mihr). Beside it the learned form fraward is used. MP frawardīn [plwltyn'] 'first month; 19th day' < OP *fravartīnām, the genitive plural ('of the fravašis'), with the older -rt- kept in this calendar name. MacKenzie and Nyberg give both words. Nourai's 'farvahr/farvartin' are older transliterations of the same Pahlavi spellings.\",\n \"derivation_fa\": \"پهلوی frawahr «فروهر، روان جاوید، فرشتهٔ نگهبان» از *fravarti- است. rt ایرانی باستان در فارسی میانهٔ جنوب‌غربی به hr بدل شده، چنان‌که «میثره» به «مهر» رسیده است. frawardīn «ماه نخست، روز نوزدهم» از *fravartīnām پارسی باستان است، یعنی حالت اضافی جمع «از آنِ فروهرها». مکنزی و نیبرگ هر دو را آورده‌اند و ادعای نورایی درست است.\",\n \"sources\": [W[\"farvahar\"], W[\"farv\"]],\n \"ref_check\": [{\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"No page given; BQT 1476 and 1478 (ref_page.py) cite 'پهلوی fravartīn' and 'پهلوی fravahr'.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 33 s.vv. frawahr, fraward (PHD.txt l.335-337)\", \"stance\": \"supports\", \"note\": \"'frawahr [plwʾhl | M prwhr-] man's immortal soul, guardian angel during his lifetime'; 'fraward [plwlt' | M frwrd-] = frawahr'.\"},\n   {\"src\": \"NYB\", \"where\": \"s.vv. fravahr, fravartīkān, fravartīn (l.1557-1564)\", \"stance\": \"supports\", \"note\": \"'fravartin [plwltyn'; inscr. prwrtyn] 1. the name of the first month ... 2. the name of the 19th day ... < *fravartinām, Av. fravašinąm, gen. pl. of fravarti-'.\"}]})\nN.append({\"id\": 7, \"lang\": \"Persian\", \"words\": \"Farvahar; Farvardîn\", \"verdict\": \"confirmed\",\n \"derivation\": \"NP farvahar / foruhar (Zoroastrian and learned usage) continues MP frawahr, with an anaptyctic vowel breaking the initial cluster fr- > far-. NP Farvardin (shortened poetic Fardin, in Mas'ud-e Sa'd) continues MP frawardīn < OP *fravartīnām, the genitive plural of *fravarti-. Since Achaemenid/Sasanian times it names the first month, with the Farvardigān festival of the descending fravašis just before it. Hübschmann notes that genuine SW Persian would give *farvard, and that farvar/farvahar is a 'Parsi' (Zoroastrian) form.\",\n \"derivation_fa\": \"«فروهر» در فارسی نو (بیشتر در کاربرد زرتشتی و ادبی) از فارسی میانهٔ frawahr است. در آغاز واژه برای شکستن خوشهٔ همخوانی fr- یک واکه افزوده شده است. «فروردین» (کوتاه‌شدهٔ شعری آن «فردین» در دیوان مسعود سعد) از فارسی میانهٔ frawardīn و پارسی باستان *fravartīnām، حالت اضافی جمع «فروهرها»، است و نام ماه نخست سال شده. هوبشمان و معین و ویکی‌واژه همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\": [W[\"farv\"], W[\"farvahar\"]],\n \"ref_check\": [{\"ref\": \"BQT:1476-1478\", \"status\": \"supports\", \"note\": \"BQT 1476 (pdf p. 269): 'فروردین - نام ماه اول سال شمسی ... پهلوی fravartīn مأخوذ از پارسی باستان *fravartīnām ... در ادبیات پارسی «فردین» بتخفیف آمده. مسعود سعد گوید ...'; BQT 1478 (pdf p. 271) s.v. فروهر: 'پهلوی fravahr ... اوستا fravaši-'.\"}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"pp. 190, 202 (HUB.txt l.6712, l.6908-6911)\", \"stance\": \"supports\", \"note\": \"'Farvardīn der erste Monat = phl. fravartīn, zd. fravašinąm (gen. pl.)'; 'np. farvar = phl. fravahr ... zd. fravaši-, ap. *fravarti-; aber das Wort ist specifisch parsisch und würde echt persisch *farvard lauten'.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. frawahr\", \"stance\": \"supports\", \"note\": \"'frawahr ... guardian angel' (the MP source).\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt grep farvard/fravahr\", \"stance\": \"silent\", \"note\": \"Horn has no entry for farvardīn or farvahar.\"}]})\nN.append({\"id\": 8, \"lang\": \"Avestan\", \"words\": \"varethra; varethra-jan, varethra-ğam\", \"verdict\": \"plausible\",\n \"derivation\": \"Av. varəθra- n. means 'defence, resistance; offensive power' (Pokorny: 'Widerstand, Wehr, Schild'; Klein compares it with weir). It is = Skt. vṛtra- 'obstacle', personified in the Rigveda as the demon Vṛtra, and both come from *wer- 'cover, ward off' + the instrument suffix *-tro-. varəθraγna- (Nourai's 'varethra-ğam', ğ = γ) and the adjective varəθrajan- 'victorious' are compounds with jan-/γna- 'smite' (*gʷʰen-), 'smiting of resistance' = Skt. vṛtrahán- 'Vṛtra-slayer'. The root link is right. The glosses are partly off: Avestan varəθra- is not 'defender' and not the name of a demon (the demon is Indic only), so 'demon killer' is the Vedic reading, which Mo'in also gives.\",\n \"derivation_fa\": \"اوستایی varəθra- به معنی «پایداری، ایستادگی، نیروی تهاجم» است و پوکورنی آن را «Widerstand, Wehr» معنی می‌کند. این واژه برابر سنسکریت vṛtra- «بازدارنده» است که در ریگ‌ودا به اژدهای «ورتره» بدل شده. هر دو از ریشهٔ *wer- «بازداشتن» با پسوند ابزارساز -θra- آمده‌اند. varəθraγna- و varəθrajan- «پیروز» با جزء دوم jan- «زدن، کشتن» ساخته شده‌اند، یعنی «درهم‌شکنندهٔ ایستادگی»، برابر سنسکریت vṛtrahán- «ورتره‌کش». پیوند با این ریشه درست است، ولی معنی «دیو» تنها در هندی است و در اوستا نیست. پس گزارش نورایی (که از حاشیهٔ معین گرفته شده) با احتیاط پذیرفتنی است.\",\n \"sources\": [W[\"bahram\"]],\n \"ref_check\": [{\"ref\": \"POK:1116\", \"status\": \"not_found\", \"note\": \"Not on p. 1116; on p. 1160-1162 POK_full.txt l.92020: 'vṛtra- n. Abwehr, enmity, fiend(e) (Avestan varəθra- Widerstand, Wehr, shield)' — supports the root assignment.\"}],\n \"consulted\": [WLD_I280,\n   {\"src\": \"KLN\", \"where\": \"s.v. weir (KLN_1971.txt l.265920ff.)\", \"stance\": \"supports\", \"note\": \"'Avestic varəθra- weir' listed among the derivatives of I.-E. *wer- 'to enclose, cover'.\"},\n   {\"src\": \"BQT\", \"where\": \"s.v. بهرام, BQT_v1_pages.txt l.21918-21941\", \"stance\": \"supports\", \"note\": \"Mo'in: 'اوستا verethraghna ... بمعنی پیروزمند. اصلاً مرکب است از دو جزو: varəθra اوستایی و vṛtra سانسکریت بمعنی اژدهایی که باران را محبوس میداشت ... جزو دوم ghna اوستایی ... بمعنی زدن و کشتن'.\"},\n   {\"src\": \"BRT\", \"where\": \"BRT.txt\", \"stance\": \"silent\", \"note\": \"varəθra-/varəθraγna- columns unreadable in the local OCR.\"}]})\nN.append({\"id\": 9, \"lang\": \"Pahlavi\", \"words\": \"varhrâm\", \"verdict\": \"confirmed\",\n \"derivation\": \"Av. varəθraγna- > Parthian Warhragn/Warhrān > MP Warahrān [wlhlʾn'], later Wahrām [wʾhlʾm]. θr became hr (the SW and Parthian development), the cluster -γn- was simplified to -n, and n then dissimilated to m. The word is the god of victory, the planet Mars and the 20th day of the month. Nourai's 'varhrâm' is a mixed transliteration of the old and the late forms. The gloss 'victorious' renders the god's epithet.\",\n \"derivation_fa\": \"اوستایی varəθraγna- در پارتی warhrān و در فارسی میانه نخست warahrān و سپس wahrām شده است. θr به hr بدل شده و خوشهٔ -γn- ساده شده و n به m گراییده است. این نام ایزد پیروزی، سیارهٔ بهرام (مریخ) و روز بیستم ماه است. نیبرگ و مکنزی همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\": [W[\"bahram\"]],\n \"ref_check\": [{\"ref\": \"BQT:324\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt l.21918ff. s.v. بهرام (vol. 1 p. 324): Mo'in gives 'اوستا verethraghna ... پهلوی varhrān, vahrām ... بمعنی پیروزمند'.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 88 s.v. Wahrām (PHD.txt l.605)\", \"stance\": \"supports\", \"note\": \"'Wahrām [wlhlʾn', wʾhlʾm | M whrʾm, N bahrām] god of war, victory; astr. Mars; cal. 20th day'.\"},\n   {\"src\": \"NYB\", \"where\": \"s.v. Vahrām (NYB_vol2_glossary.txt l.3912)\", \"stance\": \"supports\", \"note\": \"'Vahrām [wʾhlʾm] later form of Varhrān, Varhrām (q. v.): 1. the god V. ... the planet Mars ... 2. n. pr. the Sassanid king'.\"}]})\nN.append({\"id\": 10, \"lang\": \"Persian\", \"words\": \"vahrâm; bahrâm\", \"verdict\": \"confirmed\",\n \"derivation\": \"NP Vahrâm (archaic, also Zoroastrian) and Bahrâm continue MP Wahrām. In New Persian, initial w- regularly became b- (cf. wād > bād, wārān > bārān). The name of the god of victory became a royal name (five Sasanian kings, Bahrām Gōr) and a common male name, and also names Mars. 'Demon killer' is the literal Vedic sense of vṛtrahan, not a Persian meaning.\",\n \"derivation_fa\": \"«وهرام» (صورت کهن‌تر و زرتشتی) و «بهرام» از فارسی میانهٔ wahrām است. w آغازی در فارسی نو به b بدل شده، چنان‌که wād به «باد» رسیده است. نام ایزد پیروزی نام پادشاهان ساسانی (مانند بهرام گور) و نام مردانه و نام ستارهٔ مریخ شده است. معنی «دیوکش» برگردان لفظی vṛtrahan ودایی است، نه معنی فارسی. ادعای نورایی درست است.\",\n \"sources\": [W[\"bahram\"]],\n \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No reference printed on this box; BQT 324 (checked under node 9) covers it.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. Wahrām\", \"stance\": \"supports\", \"note\": \"'Wahrām ... | M whrʾm, N bahrām'.\"},\n   {\"src\": \"BQT\", \"where\": \"s.v. بهرام (BQT_v1_pages.txt l.21918-21941)\", \"stance\": \"supports\", \"note\": \"'بهرام - بروزن فرجام، نام فرشته‌است ... و نام پادشاهی ... بهرام گور ... بهرام نام پنج پادشاه ساسانی است'.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt grep bahrām\", \"stance\": \"silent\", \"note\": \"No entry for bahrām in Horn.\"}]})\nN.append({\"id\": 11, \"lang\": \"Persian\", \"words\": \"gîj\", \"verdict\": \"unverified\",\n \"derivation\": \"gij 'dizzy, confused' (Rumi; Borhan s.v. گیجیده 'سراسیمه و حیران') is a real word. Its etymology is unknown. Wiktionary lists cognates (Kurd. gêj, Luri gıj, Sogd. kyc /kēč/) and calls the Persian a likely Northwestern Iranian loan, but gives no IE root. A link to *wer-/*werǵ- 'enclose, constrict' would need *w- > g- (possible in NW Iranian, as in gurg 'wolf'). The Sogdian k- and the sense 'dizzy' do not fit that, and no dictionary checked (Horn, Hübschmann, Cheung, Mann) makes the connection. Nourai's IEC:1599 could not be read.\",\n \"derivation_fa\": \"«گیج» به معنی «سرگشته، منگ» واژه‌ای واقعی است و در شعر مولوی و در برهان قاطع آمده. ولی ریشهٔ آن روشن نیست. ویکی‌واژه هم‌ریشه‌های کردی gêj، لری gıj و سغدی kēč را می‌آورد و آن را احتمالاً وام‌واژه‌ای از ایرانی شمال‌غربی می‌داند، اما ریشهٔ هندواروپایی برایش نمی‌دهد. پیوند آن با *wer-/*werǵ- «در میان گرفتن، فشردن» نه از نظر آوایی (k- سغدی) و نه از نظر معنا پشتوانه‌ای ندارد. در هرن و هوبشمان و چونگ هم چنین پیوندی نیامده. ادعای نورایی را نمی‌توان تأیید کرد.\",\n \"sources\": [W[\"gij\"]],\n \"ref_check\": [\n   {\"ref\": \"IEC:1599\", \"status\": \"not_checked\", \"note\": \"Local IEC.txt stops at p. 1554; grep for gij/gēj/giž in IEC.txt finds nothing.\"},\n   {\"ref\": \"MON:3505\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang p. 3505 not on disk in paginated form; MON_part1.txt l.3375 has only 'متحیر. گیج' inside another entry.\"}],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt grep gij/gēj; s.v. *u̯aiǰ 'to shake, swing' p. 413-414\", \"stance\": \"silent\", \"note\": \"No entry for NP gij; *u̯aiǰ gives NP bextan/bēz- 'shake', Bal. gē(h)t/gēj- 'swing', but gij is not listed.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt grep gīj\", \"stance\": \"silent\", \"note\": \"Only 'phlv.-pāz. hargij' (hargiz) found; no gīj.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt grep gīj\", \"stance\": \"silent\", \"note\": \"No entry.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 s.v. گیجیده (BQT_v3_pages.txt l.49330-49338)\", \"stance\": \"silent\", \"note\": \"'گیجیده ... دماغ پریشان شده و سراسیمه گشته و سرگردان و حیران گردیده باشد'; Mo'in's note only refers to گیج / گیجیدن, no etymology legible.\"}]})\nN.append({\"id\": 12, \"lang\": \"Latin\", \"words\": \"op-erîre; ap-erîre\", \"verdict\": \"confirmed\",\n \"derivation\": \"Latin operiō 'to cover' < *op-weriō (ob-/op- 'over, toward' + *wer- 'cover') and aperiō 'to open, uncover' < *ap-weriō (*h₂epo 'off, away' + *wer-). In both, the -w- was lost after the consonant and the vowel weakened in the medial syllable; the participles are opertus and apertus. Skt. api-vṛṇoti 'covers' and apa-vṛṇoti 'opens' are the exact parallels (Pokorny, Walde-Pokorny, Watkins, Wiktionary). Nourai's cross-references 'Epi' and 'Apo' match the prefixes.\",\n \"derivation_fa\": \"لاتینی operiō «پوشاندن» از *op-weriō است، یعنی پیشوند op- «بر، رو» و ریشهٔ *wer- «پوشاندن». aperiō «گشودن» از *ap-weriō است با پیشوند ap- «دور، باز». w پس از همخوان افتاده است. برابرهای دقیق آن در سنسکریت api-vṛṇoti «می‌پوشاند» و apa-vṛṇoti «می‌گشاید» است. پوکورنی و واتکینز و ویکی‌واژه همین را می‌گویند و ادعای نورایی درست است.\",\n \"sources\": [W[\"aperio\"], W[\"root\"]],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.1148-1151 wer-5: '*ap-wer-yo- ... in Latin aperire, to open, uncover ... *op-wer-yo- (*op-, over; see epi) in Latin operire, to cover'.\"}],\n \"consulted\": [WLD_I280,\n   {\"src\": \"IEC\", \"where\": \"uer- (1), l.20025; operio l.12213\", \"stance\": \"supports\", \"note\": \"'Lat. cf. ambig. ap-erio, -ire, v. open; op-erio, -erire, v. close, cover'; '(operio cover, enclose. Prob. for op-uer-, q. v.)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. cover (l.58561)\", \"stance\": \"supports\", \"note\": \"'operire, to cover, for *op-werire, which is formed fr. ob, toward, and I.-E. base *wer-, to enclose, cover'.\"}]})\nN.append({\"id\": 13, \"lang\": \"English\", \"words\": \"cover; aperture\", \"verdict\": \"confirmed\",\n \"derivation\": \"cover: ME coveren < Old French covrir (Fr. couvrir) < Late Latin coperire < Latin cooperīre 'to cover wholly' (co- + operīre), borrowed after the Norman Conquest (c. 1300). aperture: borrowed (15th c.) from Latin apertūra 'an opening', from apertus, past participle of aperīre. Both reach English through Latin from the node above.\",\n \"derivation_fa\": \"انگلیسی cover از انگلیسی میانه coveren و فرانسوی کهن covrir آمده است، و آن از لاتینی متأخر coperire و لاتینی cooperīre «سراسر پوشاندن»، یعنی co- با operīre. aperture از لاتینی apertūra «روزنه، گشادگی» است که از apertus، صفت مفعولی aperīre، ساخته شده. هر دو وام‌واژهٔ لاتینی‌اند و ادعای نورایی درست است.\",\n \"sources\": [W[\"cover\"]],\n \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No reference printed on this box; AHD wer-5 (checked at node 12) lists COVER and APERTURE.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. cover (l.58561), aperture (l.17023)\", \"stance\": \"supports\", \"note\": \"'cover, tr. v. — OF. covrir ... fr. L. cooperire, to cover wholly'; 'aperture, n., an opening. — L. apertura, an opening, fr. apertus, pp. of aperire'.\"},\n   AHD5]})\nN.append({\"id\": 14, \"lang\": \"Germanic\", \"words\": \"war-n\", \"verdict\": \"plausible\",\n \"derivation\": \"Proto-Germanic *warnōną / *warnijaną 'to take heed, warn; withhold' (OE warnian, wearnian, ON varna, OHG warnōn). Watkins (AHD wer-5) and Pokorny (uer-5, p. 1161) put it under *wer- 'cover, ward off', reading it as 'ward off, keep from'. Pokorny himself notes contamination with *wer- 'gewahren, perceive'. Klein and Wiktionary instead derive it from *wer- 'to be aware, heed' (with wary, ward, OE wær). The sense 'warn' supports the second view, so this is one of two current analyses.\",\n \"derivation_fa\": \"ژرمنی آغازین *warnōną «هشیار بودن، هشدار دادن، بازداشتن» (انگلیسی کهن warnian، نوردی کهن varna) است. واتکینز و پوکورنی آن را زیر *wer- «پوشاندن، بازداشتن» آورده‌اند. ولی کلاین و ویکی‌واژه آن را از *wer- دیگری به معنی «آگاه بودن، پاییدن» می‌دانند، هم‌ریشه با wary و ward. خود پوکورنی هم از آمیختگی این دو ریشه سخن می‌گوید. پس سخن نورایی یکی از دو دیدگاه رایج است و با احتیاط پذیرفتنی است.\",\n \"sources\": [W[\"warn\"]],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.1151 (wer-5): 'O-grade form *wor-. 1. Germanic *war-nēn in Old English war(e)nian, to take heed: WARN'.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 1160-1162 uer-5 (POK_full.txt l.92060ff.)\", \"stance\": \"partial\", \"note\": \"'Old Icelandic varna sich enthalten = Old English wearnian warn ... Old English wearn Widerstand' under uer-5, with the remark '(in Middle High German warne ... is ein zu *uer- gewahren gehöriges Wort eingeflossen)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. warn (KLN_1971.txt l.265096)\", \"stance\": \"contradicts\", \"note\": \"'warn ... fr. OE. warnian ... and to OE. wær, aware, cautious. See ware, alert' (i.e. *wer- 'perceive', Watkins wer-4).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Warn (SKT.txt l.21203)\", \"stance\": \"contradicts\", \"note\": \"'Warn. see Wary' — Skeat files it with wary (the 'heed' root).\"}]})\nN.append({\"id\": 15, \"lang\": \"English\", \"words\": \"warn\", \"verdict\": \"plausible\",\n \"derivation\": \"warn: ME warnen < OE warnian / wearnian 'to take heed, admonish' < Proto-Germanic *warnōną, inherited by English with no borrowing. The word itself is certain. Its assignment to *wer- 'cover' depends on node 14: Watkins says yes, while Klein, Skeat and Wiktionary tie it to *wer- 'to be aware'.\",\n \"derivation_fa\": \"انگلیسی warn از انگلیسی میانه warnen و انگلیسی کهن warnian «هشیار بودن، هشدار دادن» و ژرمنی *warnōną آمده و بی‌واسطه به انگلیسی ارث رسیده است. خود واژه روشن است. ولی وابستگی آن به *wer- «پوشاندن» تنها دیدگاه واتکینز است. کلاین و اسکیت و ویکی‌واژه آن را از *wer- «آگاه بودن» می‌دانند. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [W[\"warn\"]],\n \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"No reference printed on this box; AHD wer-5 (node 14) lists WARN.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. warn\", \"stance\": \"contradicts\", \"note\": \"'warn ... rel. to ... OE. wær, aware, cautious. See ware, alert'.\"},\n   AHD5]})\nout = {\"pdf_page\": 546, \"book_page\": 516, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-16\", \"entries\": [entry]}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-546.json\", \"w\"), ensure_ascii=False, indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-546.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-546.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 546"
}
```


### [2026-10-17T00:11:39.268Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'disputed': 1, 'plausible': 7, 'confirmed': 6, 'unverified': 1}
root verdicts: {'confirmed': 1}
ref checks: {'not_found': 4, 'supports': 10, 'not_checked': 9, 'partial': 2}
books consulted: {'supports': 32, 'contradicts': 4, 'silent': 11, 'partial': 2} | by book: {'HRN': 7, 'WLD': 5, 'NYB': 5, 'BRT': 5, 'PHD': 5, 'KLN': 5, 'HUB': 4, 'KNT': 3, 'BQT': 3, 'AHD': 2, 'ARY': 1, 'CHEUNG': 1, 'IEC': 1, 'POK': 1, 'SKT': 1}
```


## [2026-10-17T00:11:48.055Z] TOOL CALL #86: SubagentHandback

```json
{
 "message": "Page 546 (book p. 516, root Wer 3 / Werg 2) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-546.json, and `verify_check.py 546` reports 15/15 nodes and 0 PROBLEM lines. Wer 4 is a redirect, so I skipped it.\n\n- **Root:** confirmed. It is PIE *wer- \"cover, enclose\" (Pokorny uer-5, pp. 1160-1162) plus its extension *werǵ- (Pokorny uerg-1, p. 1168). Nourai's citation POK:1116 is wrong: that page has uedh- \"strike\", so 1116 is probably a slip for 1160. His IEC:1599 can't be checked, because the local Mann text stops at p. 1554.\n- **Node verdicts:** 6 confirmed (#6, 7, 9, 10, 12, 13), 7 plausible (#2, 3, 4, 5, 8, 14, 15), 1 disputed (#1), 1 unverified (#11).\n- **Disputed, #1 paru-zana:** Old Persian paruzana- means \"having many (kinds of) men\" (paru- \"many\" + zana- \"man\"; Kent's lexicon). It is not \"walled-in area, city\" and has nothing to do with *wer-. The other words in that box (var, vara, vāra, vardana) are fine.\n- **Unverified, #11 gîj \"dizzy\":** no source gives an IE root. Wiktionary calls it a likely Northwestern Iranian loan, and its Sogdian cognate kēč starts with k-, which doesn't fit *w-. Horn, Hübschmann and Cheung say nothing about it.\n- **Other plausible points worth knowing:**\n  - Several Avestan compounds in #3 (upairi-vāra, paiti-vāra, fra-vārna, *daēza-vāra) are reconstructions; only pairi.vāra- is attested (Bartholomae col. 866).\n  - Scholars disagree on which var- fravaši comes from (\"cover\" or \"choose\").\n  - Avestan varəθra- means \"resistance\". The demon reading (\"demon killer\") is Vedic only.\n  - Klein, Skeat and Wiktionary put warn under *wer- \"be aware\"; only Watkins and Pokorny file it here.\n- **Transcription:** nothing flagged. The JSON matches the printed page (site/pages/546.jpg), so there are no extraction errors to fix.\n\nThe web sources are archived with fetch_source.py (11 Wiktionary pages). Etymonline and Iranica returned 403, so I don't cite them."
}
```


### [2026-10-17T00:11:48.368Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
