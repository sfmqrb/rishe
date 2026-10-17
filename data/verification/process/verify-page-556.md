# Verification process log — verify-page-556


## [2026-10-17T00:00:15.863Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 556 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-556.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-556.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-556.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 556` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.933Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:20.093Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:20.281Z] TOOL RESULT

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


## [2026-10-17T00:00:20.571Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-556.txt"
}
```


### [2026-10-17T00:00:20.600Z] TOOL RESULT

```
1	=== PDF page 556 (book page 526) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wrdho, Wrod : thorn, flower  (refs KLN:1357; SYN:527)
4	#1 (parent #0) [Avestan / Old Iranian] refs=KLN:1357; BQT:1822 | wrda, varedha : rose ; suxra-vard : red rose, town near Tehran ☞Keuk 1
5	  #2 (parent #1) [Pahlavi] refs=None | vardâ, vard, vart
6	    #3 (parent #2) [Persian] refs=MON:5000; AHD:1550; SYN:527 | vard «وَرد» : rose ; sohrvard «سُهروَرد» : red rose, name of a town
7	    #4 (parent #2) [Persian] refs=BQT:2290; IRN:129 | val, vel, vol «وَل ، وِل ، وُل» : flower, rose ; valğŭneh «والغونه، ولغونه» : (red cheeks), facial powder | NOTE: This pronunciation change took place in early Aškânî era.
8	      #5 (parent #4) [Persian] refs=SKT:454; AHD:129,1550 | gol «گُل» : flower | extra: گلاب
9	        #6 (parent #5) [Arabic] refs=PLA:88 | julâb : rosewater
10	          #7 (parent #6) [English] refs=AHD | julep ☞Ab 1
11	#8 (parent #0) [Greek] refs=SYN:527; KLN:1357; | rhodon : rose
12	  #9 (parent #8) [Latin] refs=None | rosa
13	    #10 (parent #9) [French] refs=None | 
14	      #11 (parent #10) [Persian] refs=MON:1647 | roz «رُز» : a rose | extra: ۲
15	    #12 (parent #9) [English] refs=None | rose
16	#13 (parent #0) [Sogdian] refs=SOD:411 | wrd : rose
17	
```


## [2026-10-17T00:00:21.131Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-556.json"
}
```


### [2026-10-17T00:00:21.164Z] TOOL RESULT

```
1	{
2	  "pdf_page": 556,
3	  "book_page": 526,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wrdho, Wrod",
8	        "lang": "Indo-European",
9	        "refs": "KLN:1357; SYN:527",
10	        "gloss": "thorn, flower"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan / Old Iranian",
17	          "refs": "KLN:1357; BQT:1822",
18	          "words": [
19	            {"translit": "wrda, varedha", "gloss": "rose", "script": null},
20	            {"translit": "suxra-vard", "gloss": "red rose, town near Tehran", "script": null, "see": ["Keuk 1"]}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Pahlavi",
29	          "refs": null,
30	          "words": [
31	            {"translit": "vardâ, vard, vart", "gloss": null, "script": null}
32	          ],
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 2,
39	          "lang": "Persian",
40	          "refs": "MON:5000; AHD:1550; SYN:527",
41	          "words": [
42	            {"translit": "vard", "gloss": "rose", "script": "وَرد"},
43	            {"translit": "sohrvard", "gloss": "red rose, name of a town", "script": "سُهروَرد"}
44	          ],
45	          "note": null,
46	          "quote": {"text": "نیست درموکب جهان مردی - نیست بر گلبن وفا وَردی", "poet": "Khâqânî"}
47	        },
48	        {
49	          "id": 4,
50	          "parent": 2,
51	          "lang": "Persian",
52	          "refs": "BQT:2290; IRN:129",
53	          "words": [
54	            {"translit": "val, vel, vol", "gloss": "flower, rose", "script": "وَل ، وِل ، وُل"},
55	            {"translit": "valğŭneh", "gloss": "(red cheeks), facial powder", "script": "والغونه، ولغونه"}
56	          ],
57	          "note": "This pronunciation change took place in early Aškânî era.",
58	          "quote": {"text": "مسلسل زلف بر رو ریته دیری - وُل و سنبل بهم آمیته دیری", "poet": "Bâbâ Tâher"}
59	        },
60	        {
61	          "id": 5,
62	          "parent": 4,
63	          "lang": "Persian",
64	          "refs": "SKT:454; AHD:129,1550",
65	          "words": [
66	            {"translit": "gol", "gloss": "flower", "script": "گُل"}
67	          ],
68	          "script_extra": "گلاب",
69	          "note": null,
70	          "quote": {"text": "در کار گلاب و گل حکم ازلی این بود - کان شاهد بازاری وین پرده نشین باشد", "poet": "Hâfez"}
71	        },
72	        {
73	          "id": 6,
74	          "parent": 5,
75	          "lang": "Arabic",
76	          "refs": "PLA:88",
77	          "words": [
78	            {"translit": "julâb", "gloss": "rosewater", "script": null}
79	          ],
80	          "note": null,
81	          "quote": null
82	        },
83	        {
84	          "id": 7,
85	          "parent": 6,
86	          "lang": "English",
87	          "refs": "AHD",
88	          "words": [
89	            {"translit": "julep", "gloss": null, "script": null, "see": ["Ab 1"]}
90	          ],
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 8,
96	          "parent": 0,
97	          "lang": "Greek",
98	          "refs": "SYN:527; KLN:1357;",
99	          "words": [
100	            {"translit": "rhodon", "gloss": "rose", "script": null}
101	          ],
102	          "note": null,
103	          "quote": null
104	        },
105	        {
106	          "id": 9,
107	          "parent": 8,
108	          "lang": "Latin",
109	          "refs": null,
110	          "words": [
111	            {"translit": "rosa", "gloss": null, "script": null}
112	          ],
113	          "note": null,
114	          "quote": null
115	        },
116	        {
117	          "id": 10,
118	          "parent": 9,
119	          "lang": "French",
120	          "refs": null,
121	          "words": [],
122	          "note": null,
123	          "quote": null
124	        },
125	        {
126	          "id": 11,
127	          "parent": 10,
128	          "lang": "Persian",
129	          "refs": "MON:1647",
130	          "words": [
131	            {"translit": "roz", "gloss": "a rose", "script": "رُز"}
132	          ],
133	          "script_extra": "۲",
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 12,
139	          "parent": 9,
140	          "lang": "English",
141	          "refs": null,
142	          "words": [
143	            {"translit": "rose", "gloss": null, "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 13,
150	          "parent": 0,
151	          "lang": "Sogdian",
152	          "refs": "SOD:411",
153	          "words": [
154	            {"translit": "wrd", "gloss": "rose", "script": null}
155	          ],
156	          "note": null,
157	          "quote": null
158	        }
159	      ]
160	    }
161	  ]
162	}
163	
```


## [2026-10-17T00:00:26.796Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['KLN','SYN','BQT','MON','AHD','IRN','SKT','PLA','SOD','POK','WLD','IEC','HRN','HUB','PHD','NYB','BRT','ARY','FSD','WEB','LKT','AFM','FVQ','CHEUNG']:\n  v=d.get(k); print(k, v and {x:v.get(x) for x in ['local_file','page_offset','scans','lookup_hint']})\n\"; command ls sources/refs | head -100; sed -n 1,80p ../../tools/verify_check.py | head -0"
}
```


### [2026-10-17T00:00:27.236Z] TOOL RESULT

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bgrzrh5rq.txt

Preview (first 2KB):
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
...
</persisted-output>
```


## [2026-10-17T00:00:33.004Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bgrzrh5rq.txt | grep -v '^  `.*\\.pdf`$' | head -250"
}
```


### [2026-10-17T00:00:33.407Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}], 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'scans': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'scans': None, 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
IRN {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'], 'page_offset': '222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.', 'scans': [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', 'first_printed': 1, 'last_printed': 210, 'pdf_offset': 11, 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'}], 'lookup_hint': "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
PLA {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'scans': [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}], 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)'}
SOD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'scans': None, 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}"}
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'scans': None, 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'scans': [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}], 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
FSD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
LKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None, 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
AFM {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'scans': None, 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
FVQ {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'scans': None, 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).'}
CHEUNG None
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


## [2026-10-17T00:00:53.152Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('page-538.json'));e=d['entries'][0];print(json.dumps({k:d[k] for k in d if k!='entries'}));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\"; grep -n 'PROBLEM' ../../tools/verify_check.py | head -40"
}
```


### [2026-10-17T00:00:53.691Z] TOOL RESULT

```
{"pdf_page": 538, "book_page": 508, "verified_by": "claude-opus-5.5", "verified_on": "2026-10-16"}
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
90:        print("PROBLEM:", p)
```


## [2026-10-17T00:00:56.312Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,95p tools/verify_check.py"
}
```


### [2026-10-17T00:00:56.920Z] TOOL RESULT

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


## [2026-10-17T00:01:15.222Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: u̯rdh\\|lemma: wrdh\\|lemma: u̯r̥dh\\|lemma: wr̥dh\\|lemma: u̯rod' POK_full.txt; grep -n -i 'rhodon\\|ῥόδον\\|brodon' POK_full.txt | head; "
}
```


### [2026-10-17T00:01:15.811Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:01:20.373Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'rose' POK_full.txt | head -30; grep -n -i 'rhod\\|wrod\\|vrod' POK_0*.txt | head -20"
}
```


### [2026-10-17T00:01:21.053Z] TOOL RESULT

```
2689:Latvian /gstu, fgt' have internal pain, be sullen, morose ', /gnet' have disgust ', fgn/'s^ 
9270:from which *abnes, from obi. case arose from Latin amnis, was compensated during in 
12999:high' arose from the strengthening mode of Old High German bora-, e.g. in bora-tail^yery 
15625:style, turgid, bombastic, torose ', brauschen 'sweW up'. 
15661:it'/zz/se 'injure', probably also Old High German brosma. Middle High German brosem, 
15662:broseme, brdsme'b\t, flake, crumb'; Old English brosn/an' molder '. 
19251:meaning "care, worry, be considerate of ' arose from "pull, drag' perhaps about "bring up'; 
23076:(Plaut), Umbrian frosetom^ cheated, beguiled, defrauded, robbed ', Latin frustra {newer 
30149:thornbush, rosehip, dog rose '; 
31661:Gekrose, ndd. kruse {*krusi-) "wrinkle, crease, furrow, curl ', holl. kreus^ fold in staves '; 
32953:grumble, growl ', ndd. gnadderig' iJbellaunisch, morose '. 
34119:German gruosei. ' young plant shoot, plant juice ', Middle Low German grosei. ' plant 
34756:peruke; a rose-bud; a conical cap of leather, fur cap ' is uncovered to be borrowed from gr. 
37274:or system, promiscuously, indiscriminately, in unfettered language, i.e. in prose, 
41357:responsibility, prosecutes, avenges ', yati- m. "ascetic' ("*striver'), yatuna-^ keen ', yatna- 
42202:Epic -ionische Psilose), in Attic prose seldom used words; 
50799:f., engl. hip, Norwegian hjupa^ rosehip, dog rose '; 
53316:"where he', as from Lithuanian kuf [*k"ur]^\Nhere' +J/s^\r\e' arose Lithuanian Rel. kuris, 
63844:amu-sotti. " Rose ' (disease, malady), amr^ reddish brown ', Modern High German Ahm, 
69266:phuphusa-, -/77' lung ', pupphusa-^ lung, Samenkapsel the Wasserrose' (Lex.), phut-karoti 
70655:'Rostpfanne, pyre, stake'. Old High German rose. Middle High German rosch, rosch 
71038:a formal complaint, indictment, accusation, prosecution '; 
72475:when he rose from the sitting, seat, breech, fundament, Hp. Aph.5.22, etc.; of birds and 
72969:arose 6s. {*ad-pro-sk"'o-)\ Middle Irish /'osc'dithyrambische poem ' {*pro-sk"'o-)\ Old Irish 
72989:auch con-secha, cose as Latin animadvertere a\so ' reprove ') in: Old Irish rosem. 'eye, 
74040:sorobalina^ rosehip, dog rose, blackberry ', Lithuanian serbenta, serbentas^ black currant 
74774:Umbrian prusekatu' prosecato ', prosesetir' to cut off, cut away ', asegeta' non secta ', 
79404:addition after Rosenfeld, Forsch. under Fortschr. 29, 176 schwachtonig 5/in Proto Norse 
80717:f. "scum, froth, foam', pumexm. "Bimsstein' (from seiner schaumartig porosen 
86939:5e(Gen. Dat. Sg. f.) etc. (s-from //■), Proto Norse ^Tt, Old Saxon //7//"dorthin' (Rosenfeld 
POK_03.txt:1312:Ai.  rdtha-  m.  .Wagen',  ratU- , Wagenlenker',  rdthya-  .zum  Wagen  gehörig', rathar-ydti  .f<ährt  im  Wagen';  rathesthä-  .Krieger'  =  av.  radaeUä  ds.;  av.  ra-. ^a-  .Wagen',  raid^ya  .Fahrstraße';  lat.  rota  ,Rad',  birotus  ,zweirädrig'  (:iit,  ^^ dvirätis),  rotundus  ,scheibenrund';  ir.  roth  m.  ,Rad';  cymr.  rhod  f.  .Rad'j gall.  OIST  Roto-magus  (Rouen);  kelt.  *-reto-  .Lauf,  neutr.  Abstraktsuffix  in cymr.  brith-red  .Verwirrung'  =  mir.  brecht-rad  .Mannigfaltigkeit'.  Kollektiv-,.. Suffix  in  mir.  aig-red  ,Eis' ;  dehnstufig  *-röto-  in  mcymr.  rhawd  ,Lauf,  LauM.,.. bahn,  Schaar',  gaeaf-rawd  .Winterszeit'  =  mir.  gem-rad  ds.,  mcymr.  bed- rawd,  cymr.  bedd-rod,  bret.  bez-ret  , Gräber'  (cymr.  bedd  .Grab'),  dazu  miri rä(i)the  .Jahreszeit.  Vierteljahr'  {^rötio-)]
POK_03.txt:2621:Ahd.  scart-lsarn,  mlid.  schart  m.  n.,  scharte  f.  , eiserne  Pfanne';  aksl. skrada  ,Tiegel,  Pfanne,  Herd'  (auch  skvrada,  skovrada,  poln.  skowroda, russ.  skovorodd]  v  kann  von  slav.  skver-  ,schmelzen',  aksl.  raskvhrg  usw., übernommen  sein);  lett.  skärds,  skärde  , Blech,  Weißblech'  hat,  wenn  zu- gehörig, seine  Bed.  vielleicht  aus  , Scherbe  (scharf  und  dünn)'  entwickelt.
POK_03.txt:5554:gr.  rhod.  ic&gag  ,Wa.gen'  Res.,  xch^v-ad'QOv  ,Korhwa.gen^  {*undh-roA-xitnU jpre-uendu  ,advertitö*,  aha-uendu  ,avertitö';  '  *
POK_03.txt:5788:A.  uerd-:  av.  varddva-  ,weich,  locker*,  aksl.  vr^d^,  russ.  vered  , Wunde'; ytred-'.  ai.  avradanta  ,sie  wurden  weich*,  vrandin-  ,mürbe  werdend^* ured-:  apr.  redo  , Ackerfurche',  älter  dän.  vraade,  vrode  , wühlen,  auf- bohren*; uröd-:  lat.  rödöj  -ere  ,nage,  verzehre',  röstrum  (*röd-trom)  n. ,Nage Werkzeug,  Schnauze,  Schnabel',  ags.  wrötan  , wühlen,  graben',  aisl. röta  ds.,  ahd.  ruozit  ,suscitat,  movet',  ags.  wrötj  mhd.  ruozel,  rüezel,  nhd. Rüssel  (*im^ötila-)]  dazu  die  Schwundstufe  in  schwed.  dial.  rota,  ruta , wühlen*;  nach  Frisk  (Etyma  Armen.  30)  dazu  noch  arm.  gercum  , rasieren' aus  *uerd-s-  (ursprüngl.  Aoristbildung).
POK_01.txt:3711:gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßiog,  ther.  Qhagvfxaqhog),  d-gaavg  ,kühn, mutig;  verwegen,  frech'  (=  ai.  dlifsu-),  lesb.  Adv.  -S^goaecjg,  Mgavvog mutig,  getrost,  vertrauend'  (*-9-ag(To-avvog)]
POK_02.txt:4514:gr.  'ATL^cü  ,gründe',  iv-KTifj^svog  ,wohl  gehaut,  wohl  bestellt',  iv'/.TLTog  ^. rteQiy.TLOvsg,  Tteqiy.Tkai  ,Um wohner,  Nachbarn',  d(X(pLy,TLOvsg  ,Herumwohnende* (zur  Form  df.icptxrvovsg  Lit.  bei  Boisacq  525  Anm.  2),  xr/ö-tg  , Anbauung' Ansiedelung',  rhod.  xroivä  , Wohnsitz,  Gemeindebezirk',  auch  xTtAog  ,ruhig» (eigentl.  ,an  die  Siedelung  gebannt,  gezähmt') ;  gehört  wohl  zum  Folgenden:
POK_02.txt:4859:kret.  o-7tvL  , wohin',  syrak.  fivg  ("^TrvL-g),  rhod.  djtvg  , wohin'  (*^vl  neu gebildet  zu  ftoZ)]
POK_02.txt:5049:legh-  ursprüngl.  nur  punktuell  aoristisch  ,(sich)  legen',  später  durativ  ,liegen'; logho-s  m.  , Lager*,  legh-tro-,  loghio-  ds. Gr.  lexsTai'  ycoifxäTai  Hes.,  Xs^o^iai,  A^xro,  iXs^aTO  ,sich  legen  (zum Schlafe)',  eXs^a  , lullte  ein*»  XsXoxvTa'  Xs%d}  ysvofxsvr]  Hes.»  Xs^og  n.  ,Bett, Hochzeitsbett,  Totenbett*»  Xenxqov  »Lager*  (=  ahd.  lehtar),  »Gebärmutter, Nachgeburt*,  Xsx^  ,Wöchnerin*,  Xeaxv  rhod.  ,Ruhestätte  =  Grab',  att. »Erholungsort  für  Müßige,  dann  Plauderei  u.  dgl.'  {Heghskä,  vgl.  unten air.  lese,  ahd.  irleskan),  Xo^og  »Hinterhalt  (daraus:  bewaffnete  Schar); Niederkunft',  fi  Xo%6g  »Kindbetterin',  U-Xo^og  »Bettgenossin»  Gattin*  (:  slar. *sg-logz),  Xoxfirj  »Wildlager;  Dickicht';
```


## [2026-10-17T00:01:25.849Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30130,30160p POK_full.txt; grep -n 'lemma: .*rdh\\|lemma: u̯er(e)dh\\|lemma: u̯r' POK_full.txt | head -30"
}
```


### [2026-10-17T00:01:26.288Z] TOOL RESULT

```
Swedish kalk^ marrow in wood' ("marrow globules '), Middle English /re//res "eggs of 
fish', colk coike " apple core '. 

The consecutive only Germanic (and Celtic?) word groups (Indo Germanic gleg-, glog- 
?) make no Indo Germanic impression with their expressive intensification and 
nasalization, so 

g/ek-\n Old Norse kleggi {* klagjan-) " haycock, haystack ', nasalized Modern High 
German Dialectal (siebenbg.) heu-kling, klang^ haycock, haystack ', klang, klinge^ 
gravelly shallow place in the river, sandbank'; Old English clingan^ contract, shrink ', engl. 
cling^ cling, stick; adhere ', Old Norse klengiask^ auf jemand eindringen ' ("*cling '), Middle 
High German klingen' climb, ascend, go up, mount ' (with consonant-sharpening Modern 
High German dial, klinken^ cling '), Old High German klinga. Modern High German Klinge 
"narrow gorge, ravine, gulch, gully, canyon ', wherefore with gramm. variation (also Indo 
Germanic *gle-n-k-) engl. dough {= Old English *cldhirovc\ *klanh-) " steep gully, canyon, 
gorge ', Old High German Clah-uelde; Old High German klunga^ ball (of thread, yarn), 
tangle, knot ', Demin. klungilTn, Modern High German Klungel6s., Swedish klunga^ 
congested heap, mass ', klanga' climb, ascend ', Old Norse klungr{*klung-ra-, -ru-) " 
thornbush, rosehip, dog rose '; 



with Germanic -k- (partly Indo Germanic g, partly Germanic consonant-sharpening) Old 
Norse k/ak/ Irozen earth's crust ', k/akkr' lumps, wool lumps, blot, cloudlet, small cloud ', 
Middle High German k/ak' spot, blot '; Old English c/yccan' pack, grapple, grasp ' (engl. 
clutch), to Old Frisian k/ets/e^sp\t, pike', Swedish klyka {*klykja) " agrafe, hook, clasp, fork 



in addition (?) that in proto Celtic /r/rweisende Middle Irish glace, nir. ^/ac'hand', 
10301:Root/ lemma: b^ai&^a {*b'^a'c^^eb2 > bhardheh2)
```


## [2026-10-17T00:01:30.092Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Rose\\b\\|Rose,\\|Rose'\"'\"'\\|ῥόδ\\|ßgodov\\|QÖdov\\|godov' POK_0*.txt | head -20; grep -n -i 'rose\\b' WLD_band3.txt | head; grep -n -c . WLD_band3.txt"
}
```


### [2026-10-17T00:01:30.503Z] TOOL RESULT

```
POK_03.txt:107:germ.    *ampra-   (aus    *ambra  <  ''am-ro-)   in    ndl.    amper   ,scharf,    bitter, unreifS  aisl.  apr   (*ampraR)   ,scharf',    Subst.   ags.   ampre,    ahd.    ampfaro  t^l ,(Sauer)ampfer*;  unsicher  ags.  öm  m.  ,RostS  öme  f.  ,RotlaufS  aisl.  ama  f., öTnw-sö^i  f.  ,Rose'  (Krankheit),   ämr  ,rotbraunS  nhd.  Ahm,  Ohm  ,Rotlauf«j
POK_02.txt:1161:aksl.  god^  ,Zeit^  rechte  Zeit',  godina  ,äQa%  godhm  ,gefällig'_,  russ.  godnyj ,tauglich',  aksl.  u-goditi  ,gefallen',  russ.-ksl.  goditi  ds.,  ksl.  ugoda  ^Wohl- gefallen', russ.  vygoda  ,Vorteil',  aksl.  negodovati  ,unwillig  sein',  iter.  aksl.
1979:mm $84. Aeon mld. ohd. #89 torr ahd. ee Sra ea a 5 Aringea Are a. tM ot Ariat mn A, Bea? Aun ok Aumpein nhd. 375, Aace Aripsda as. 410 0". Aweit Aria abu. Ligh Paap a 375. Ariepahi abd. fi m age, 367. Arisaan as. S72" Hundert phd. 7 Arifon, Arifion on, 344*,585". Awagor ahd. 40] Ajritio, rife ald. S71* HGamar ahd. 307. pribig ; how ,,Aund™” ahd. 466, rit 4 Aont ,,100" ahd, 780, y junta aps. 400 ie “ah be huoha ahd. 345, Awof ahd, 3465, : Mckenna aga. on Anohdli hid. 335. Arog age. (453). Auolen ahd. 446, Ajrogen ali. 483, Awon all. S51. r ope. ao, huor, Auora ahd, 325, Aros ahd. 428, 667*. Avowfo abil, SM. h)roso, (Aprose aie 479. huol ahd. 342, as, 485, husla abd. 242.
2721:XV. Slaviech: Joltkate — brine, briniti 205 -rawerrl Saat Loe tidinuty russ. 211%, 200%. borty ruan. LUT*, blekotity ruse, 120%. bore T.-kal. 164°, bateft 12 1s". bigkots russ. 211°  » Art Hires rose. dial. Psa m . (178*). ilen, blem akr. 180* 34". bleplafi éech.. LOG bérzyj ruse. 175% one See 172". blest deoh. 212%, bose LSOF. léju, Méjati russ. 120* 6 russ. 120" ben hyulg. 180°. botlis russ. 100" Http img er ieniba lulg.. 180* boule Geoh. L12* batdis, bazites rose, 1ST* Zaks. rose.-kal, 212%. boute, Loufiti doch. 101%, ‘babad poln. dial. 107* bled, 0 blgati 216°. hoza russ. L20*. bate poln. 10S". brada 125%. Dietyd poln. 113* wig, Mis, Hlikeam bulg. brady 135%. bokad poin. 113°, ga rues. (165*). tobam, babdfi sloven. 106*. biikam, ‘blihati ekr. 211%, Brak dech. 172°. beblati tech. LOG*. ihném, bl iliimeds ake. 211%. brane 161%. cbrjans arnss. LOT* int rosa. 287%, bradnne 134". . dech, 110%, iy E Hiseati: a 2129. trate (194*). badro 1OD*, per) blisks 2 z*. braire, a 193". bébatt bir. 12 ! } brasda 133*. hero, byrafi 157". j bfaidtec slovin. | bérce, berco ruse. 164". bfilats ekr. LO2* iérdo russ. 103*. i eerb, 100* béirdo kir. 169%, brédt elov, L62*, , beré’s rues. 172" brbrafi aloven. 106*. ruza, 203°. bdo akr. 163%, herdmja russ. dial. 157%. brechnjd ruse. 171* béresta ruse. 170*. lvédity rus. 201". hertca russ. 170*. bredw, dresti russ.-kal, 201* beriaja russ, 157". bredz, redina russ. 201%, rues, 166", 172% brcbctm, i akr, 171* russ. (166") breilty kir, 187*. bez 137%. breplati doch. LOG" bez poln. L29*. breetly rusa.-kel. 16%, Bide 185". brefil, brechdty russ. 171%. bigna, bégnats 1 ae bets ruse. Leo end ruse. 1B0*, bala (123°), 176%. bien L2G", 160". biidu, béditi 1S5*. bigs. 138". fils ruse. 1T6*. bint kondis. 144° itr kir. 164". bites rina.
2768:doma 785. | dérob wrurs. 308 ' * dor ga i Pune. ™ : . BOR drahina poln. 700" derevo russ. 506. d werb.-kel. Sf. ait rues. SOL. ébe rose. 700. dérkij ruse. TH. drdmifi sloven. T26. dermé risa. 799. drans russ. TH. dérns ruse. THO. drdzahi aloven. 803 dértyj kir. 700. drisa eloven. 3 dese, 185 drazaift russ. (875). = 783. rhea deco eerb. 875 erelt if # dean daga poln. dink, 704 drbdeats sorb. S08. drdijtia serb. 705. din, d&jati §27 didra aloven. 715. dda, délama B29 drdvdis sloven. 705. dreben bulg. 875 das 704, 811. ania russ. S75 - drechia (700) di $27.0 dresela (720, 855) dépica B30. drezga (BOR). dint) Toss, S27. dr ; B21. diners THT. drico S00. a russ. Aoi. drjdchiy) russ. (665) dg wy rues. Tl. drjant Tusa. ruze.-kal, 71. dridpaju, +> rum. 501 , dit sloven. S38. ca nog akr. Bt ij russ. 776. dripa bulg. 800 ow dristdiy russ. 56] dira serh, THD. dtizha tech. #03. diru bulge. (774) dfLam, dréem, dt hati sloven. Wiija. rose’ (890) diljam, diljati serb. 729 cbyed Free. 7 Don r cm, : j Ciel aor * : . dye Tus. 70). drijim, dAjift serb. TOD. ram a doch. T74. drmati serb, TOG. dirhjs 775 dfmim seth. 521 dice 774. drmiais tech. 7 i tech. 887 drmolidi éeoh. T aud Mi Be po hats drmedifi Geach. dijha tech. S12. drobiju, drobiti 575. dian 811. | drota, drobd russ. din). 850
2824:308. konp 345, bord russ. (344, 373) Furs. | * borpar fa, ‘. ft 5al* cL kir, SO1*. dpath russ. SHO. pica sro 350 kowuto kal. roc. 346. kora 574*. boreiji _ 618. kéréu, -if) rose. 569", korch wrues. 560", brik: skr. 455. kra Goch, 420, Loriéet rues. O76". rdkorati tech. 413. ireek elovak. 421. ‘forens 412, tranwtp russ. 422. eh skr, 420. herlit, russ. GT6*- irdpacioa slov. 457. rruda kir, 422, korgd, borddeyj ross. 660°. Lrepoti Fl. slov. 457 bridging kel, 569". kories kal, 570". krasa 418, (480). Eruchs 479 idrlud kr. 569". iraac cel. (486). hruka 417 kored rosa. ST7*. krasta { kruke rosa. 414 hérnaj Toss. dial. S77* Erasuna 419 Anil 1 #50, 573". onde ross, 590%. inilafp krupa 450, « kordda kir. 485. krats. 570°" pi kB a 482. Toropdeyj kir, 457. iratzks kal. 570° wiiti alow, 470 her russ. 457, brava 407. krufif, rusa. 422. horton rua. 255. krogs GTO", brute r.-kel, 422. hordthy} russ, B70" Leptin. -tt 600° : tel. S18. ij Tusa, - kroptja, - * kortdty ia kir. 668* krefets rnes.-kel. 414. kraknuti 414. ries. 425, 568°. brockts rose. 414. iruma_,,Steverradar 577*. hort yak russ. 422. krék alov. 453. irom, salt horsno russ. 573* krilo eerh. 414. irenuli, afi aruaa, 524. kera 355. rele rues. 414 kranz 677". bors ..Mnsern* rues, 576%, brite ross. 414. rag korn. Wurzel* ruse. dial.412, krems rasa. din]. 593°. i 481,
2835:ds Toss. S80". mah elov. 252*. narojb lat. smolokita 4. 207", méels ruse. 240° ness 320". molokd rosa. 207%, (200"), mucha 301*. nairils 731. moloats rusa. dink, 200", moutati ekr. 31. nde ad. S1b*. mdéiol kir. 256". mukljiw wkr. 2534. nordi; rosa, 2b. miofs rus, 2G", mul, miilas! nilov. 386. neatijga tn hulp. 230. molits ruse, 256°. mul poln. 250*. notes S10. molizive muss. 20". mulec, muljdk nalov. 386. wevers 263, molotit, tsa. 200", mitted nalov. 386. fart S10". modets russ. 300*. milli nelov., B86. ndzemt ruse. 669, moles sloven. 289°. militts rons. 250)", nazwa Tusa. 540 mol, Sah", murdatyy ruse. 202*. nqditi 316". sc moleif, toss. 313*, merdea russ. 252°. gids S10". seks er murard ruse, te sor age morpate 4 rue. murayéy russ, 200*, . : mars Tass. 252%, neboma. Lab’ sisegats ottibe werden” musldka russ. 251%. nedaga. ‘TIM. russ. 280". mist ross. 25)". negodorms 532. mora rk 77". miei serb. 200". negebl, S07. in. 250°, maga 251". meje kal, 320*, S daae. mocks 251". mej kal. 320". mors, morke russ. 313° mamoli, mtmali 243°". melazjd rues. 427°. moroch, mee. 250", te S68", neni b alg". morobné kir, 262°, matieq 311°. as ot russ.-kal. méroks russ: 274". middil 251". 1". | moromrals aruss. 277*, migia 247", nerefd, nerdfa ruse, TOO*. morons dech, 270". megngt, metair 246". neroda 74. moron: fuss. 250". miia, monifi 200". nese, neste 120. moricn Tuas, 282°. ming, met 269" nelay SRO", more ZTE". mbit je ti 256. momtd wo osorb. 2257. mist 248". nevods 17, (59) mooilils rose, 225". mitels 240%, nerazaphns. 177. mosiondia ruaa, 235° miada 301*. mele, nego 357° mowty 236" myddin ruse. 1. nedra pas $16" ka 229° myjett éech. 310* med modina 225° wid oo ni ", modi, 227° mits S10*. ni kir. S87". motadi 5 malo - jinye rune. 317* moss ,.H 00". mysly 2h". nich 335". morgh ,tecn. Wetter” rose. mgs russ. 204° nizaitj? adoch. 6 mezgnute rose. 251" ites 312°. deo tii. Tues, Li nt monolh eas 260". miaté y Seoh. 6, % b, mit, rasa. 240°, nidta mort ,,potes” aler.-kel.227*. mayily moss, 251". mitt, 695°. moziit, russ. 251* may ,wtan " rum. niet 355", mrad 274* 247". njichots toss. 325" mks 274° na. priip. noga na ots hart dn's! slay, nogefh 181. mraza abg. 282", (314"). nord oH". wrth, trariti 274". d ate poln. 187*. norera rum. dad”. mrtia okel. 273%. idknuis russ, 203°. norgda kir, 334". mig. we bale. 274", nadeatals 579". nore 315*. iti deol nading, -defi 306. nodty 338". a mriiy kir, 274* aodtGre ras. 602. nora 324° werb. 3 nogiokrucineioo kel. GOO". nord’ 318° ts 274". naga 69, noin 3 ; 07". nogs don", narra 355*.. muraaiis ve (601") wale Tusa. 306". nuecid poln, 316". “ti oe aalyheti kal. 400°. euda poln. 316* a witdediraotai™ dares uth 10° ny oe are usae ? j ’ LJ ai | rt 4 14 rarkzmyhi yeaa take anton wan sorb. ee ura io bale cas mriids, mriits eid", noperyy, -periti , = fl é mitra uloy, 277*. napors russ, 42*, wuida
2837:ma, mynd 340° ovens 167, mery, nréh 334" ornes. 24. pat perro nyra, nyrét; 324" risa. 11 yt ri shen satay tine 115. @ ist pate BD. oba 56, pades Sook. 449, obaceyd poln. 171 ear pte Moet othe 119. pacha russ. 27°. obs, ob, o Le opona O61, packs rsa. 4*. obpda B27. opud tech. 83°. pady, paati 29°, obtta ares. 201. opuita pola, 81", padoraga aruse, BOS. obliditi 396°. opisia Tura. 83°. pagubs 563. ‘obls 303. fdbyna kir. 146 pahalj ckr. 67° ebwuina russ, 210°. dtje 75, 3097 paky 50 oomichwifeda roa, 249° orkks Tis pilom bulg. (7*) obora 203, orig, orati 78, palica, palokn 675° ‘oborih kir. 172°. ort 143. palica Tusa, 102" pita reali 280, 367°. oritise werb, 182, palit’ 59*. wrdzgnuli ruse.-kal, ordiy roma. Laz. pilin tram, 102" obruaii russ.skel. 107". ornla 136. pdlubs rose, 415" obrgtens Foms.-kal, LOT". om, oils, ovina poly. $0, pefych 12", SSreetheny pola. 170" bee os iat ane ab catt TU") With. Lt ' An Fie +e Obujag, uti 100. onjeka wer, 473° apache cee ty ‘oterestt russ, STD", ona russ. GO. para 27°, orpda mbg. #70", oukoma poln. (G14). prey, posi 72°. oder, odrina wkr. 121. onbinds russ, 5380*. pdserin ruse, 456". coding 828. olrels 582° pasemian tails. = edévali 827. okrad, a0" paimnio ruse. 67° odina tose. 101, oma 175. qaatyre 72°. odolits S11. onmh 17S. past ruse, 27* odringy tune. THO, chert ira aod" parity 225 | odra, cariee, ahi 131. ruse. 450%, ane pamners rea ae opamify lesl, 005. oka , Anklage*poln.470*. pez slow. (783), 3°. one 323, osha ,carox wruss. 22, posluka 782. 637 75%, posucha 782. osha ,,Blatetter* rasa. pag, ah ie. Bii®. pate toch. 4°. oategs (G21"). prance Oo". Larch aja kir. @32°, podilise O*. oatrors 703", pock, peck poln. 67* ostruiti, oxtrwjati 640%. podili 662", orira 25, Payrica 6", oats 443°. pagy 6*. onftng 32. Pot poln. &* ons 33. PrPs (190), 108° on 27, gato 661". = aa 29. pote 26°. fibajpy, fi GOL. ee cn BO, at, ota 43, 4 ross, 60° okied tusa, 43, pelena 5S*, olegndin 726. peless 54*. ofucha poln. 715 pelion Tuss, 59". ataliks 207 pélpba russ. 58". ofedia rasa. 2B. pepels G0*, aide olvorsti 281. weny, poruti 39%, 42%, omnes Tus. 24 ceuits ruse. 40". oompia LAT. pere fusa, 31°. ove 187, perepela. russ. (64%). erica 167. peresliga ruse. 713°.
2923:serpy, srifs OM zirjy, sertté G02, regis O42. treniiy rose. O42. trend rosa. 44. surcati 642. ziggy (42.
4012
```


## [2026-10-17T00:01:36.133Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): 116[5-9]' POK_full.txt; grep -n -i 'varəδ\\|vard-\\|wurd\\|vrd' POK_full.txt | head"
}
```


### [2026-10-17T00:01:36.439Z] TOOL RESULT

```
91215:Page(s): 1168-1169 
91291:Page(s): 1165-1166 
92325:Page(s): 1169-1170 
4860:Vrddhi; "mouth' as "breath, the breathing '); p/a/?///" breathes'; 
26436:drive on '; Pass. Aor. riv£x6r|v ' wurde getragen ', Perf. KOT-nvoKa Hes., £v-r|voxa (£v- is 
26790:inmost '; Old Indie antra-, also with Vrddhi antra- v\. " intestines, entrails '; 
36213:and with Vrddhierung Old Indie hayana- 'annua\, yearly', hayana-m. n. 'year' (rhyme 
50374:Cf. SOQ di-rfkob (di-rfkab) 'boyaU [LS 400]; see also QALAN-V d-Trekob 'estomac de ctievrd et al. [SSL 4 
65805:{*plels= Old Irish I/a) and of Kompar. to nAsToTOc; wurde; from a Indo Germanic *pleu-es- 
65806:"UberfluR), big, giant bulk, mass' wurde secondary the gr. Kompar. n. nAsov, wherefore the 
65807:achaische Nom. PI. nAssc; neologism wurde; also wurde Old Latin pious, Latin plus to 
69410:rabbate ' erf a(i>t, halt sich fest' = labhate, /ambbate ' erf aQ>t, ergreift', placed wurde; compare 
73432:nrh), (from Indo Germanic *som(i!"e, welches to sondo- reshaped wurde); Gothic sa sama
```


## [2026-10-17T00:01:43.110Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'ROSE' SYN.txt | head; grep -n -i '^wrod\\|wrdho\\|wr̥dh\\|wrdh' AHD_watkins1985.txt IEC.txt | head; grep -n '^rose,\\|^julep,' KLN_1966.txt"
}
```


### [2026-10-17T00:01:43.679Z] TOOL RESULT

```
13293:8.58 ROSE Ab5ov Goth. .... Lith. rozeé tptavTagvAdo ON rds, rosa Lett. ruoze rosa Dan. rose Ch&l. Bee rosa Sw. TOS SCr. ruza rose OE rose Boh. _rtiZe . ‘rosa ME rose Pol. roza . trandafir NE Tose Russ. roza, rozan ros Du. 700s Skt. (japa-, odra) TOs OHG rosa Av. varaéa-(?) thosyn MHG rose rozenn NHG rose
25936:fT a) Ss a ROSES cree Se
AHD_watkins1985.txt:1171:wrod-
AHD_watkins1985.txt:1175:wrod-. To root, gnaw. Germanic *wrét- in Old English wr6tan, to dig up: ROOT?. [Pok. 7. ver- 1163.]
33124:rose,  n.  —  ME.,  fr.  OE.,  fr.  L.  rosa,  fr.  Gk.  poSov, ‘rose’, for *Fpo8ov,  fr.OIran. *  wrda-  (whence also Aram,  warda.  Arm.  card).  OIran.  *wrda-  be¬ came  gul  in  ModPers.  in  the  sense  of  the  pho¬ netic  law,  according  to  which  initial  w  becomes  g and  -rd  is  changed  to  /.  Turkish  giil,  ‘rose’,  is  a Persian  loan  word.  OIran.  *wrda-,  ‘rose’,  repre¬ sents  I.-E.  * wrdho-,  ‘thorn,  bramble’,  whence also  OE.  word,  ‘bramble’,  Norw.  dr,  ol  (for *ord),  ‘currant,  bush’.  Cp.  rhodo-.  Cp.  also  the first  element  in  julep  and  the  second  element  in bedeguar.
```


## [2026-10-17T00:01:48.957Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13293,13310p SYN.txt | cut -c1-2500; grep -n '^julep\\|^gul\\b\\|^JULEP\\|^ROSE' KLN_1966.txt SKT.txt | head"
}
```


### [2026-10-17T00:01:49.363Z] TOOL RESULT

```
8.58 ROSE Ab5ov Goth. .... Lith. rozeé tptavTagvAdo ON rds, rosa Lett. ruoze rosa Dan. rose Ch&l. Bee rosa Sw. TOS SCr. ruza rose OE rose Boh. _rtiZe . ‘rosa ME rose Pol. roza . trandafir NE Tose Russ. roza, rozan ros Du. 700s Skt. (japa-, odra) TOs OHG rosa Av. varaéa-(?) thosyn MHG rose rozenn NHG rose
‘Rose’ is chosen as a conspicuous ex- ample of specific flower names. The i does not rest upon inherit- €itom an IE form, but upon bor- heen name spreading with the cultivation of the flower. Pee rosa, the source of most of the sis Uropean forms, is itself a loan- : eat fr, Some dialect form of tise : ee or with the latter fr. a com- pra Mediterranean source. Grk. ‘eh: Fedo belongs further with (Av * Tose’? Barth, 1369 ‘ ), Arm. vard,
a ers, ul ? gu! rose’, whether orig. an Irani-
an word, or all from some common un- known source. Schrader, Reallex. 2.267 ff. Ernout-M. 870 f.
2. NG spravraduddo, displacing pédov as the common word (hence Rum. tran- dafir, Alb. tréndafil), was orig. the rose ‘of thirty petals’. Cf. the parallel éxa- rovragudnva. (Theophr.) and rosa centifolia (Pliny), and the reference to Adda, & éxaorov éxov eEnxovra dbdAda (Hat. 8.138).
3. Skt. japa- and odra-, said to denote the ‘Chinese rose’, are both of unknown origin.
8.60. ‘Tree’ = 1.49.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
528 8.61 8.62 8.63 8.64 8.65 OAK BEECH BIRCH PINE FIR (Pinus) (Abies) Seiopini eyes tba onpbda(?) mebxn, alrus drm Re ee étua onubia mebxn, melo arm, Fie Lat. quercus (robur) fagus belu(l)la pinus abies It. quercia (rovere) faggio betula pino abele Fr. chéne (rouvre) _hétre bouleau pin sapin Sp. roble haya abedul pino abeto Rum.  stlejar fag mesteacdn pin brad Ir, daur Saghvile bethe gius, ochtach ime Nir. dair Saigh beith peine, gris gits W. derwen ffawydden bedwen pin(wydden) Dynidwyaa en, : sybwydden Br. dervenn favenn bezvenn pin saprenn Goth. .... maths sees Be onexd ee ON eik bok bjork Sura gron Dan. eg b6g birk fyr gran Sw. ek bok bjork tall, fura gran OE dc béce beorc pinbéam, furh S@ppe, gyr ME i oke beche birch pine Syrre NE oak beech birch pine fir, spruce Du. eik beuk berk pijn(boum) den OHG eth buohha bircha, birihha pinboum,forha, fiohta tanna MHG eich(e) buoche birke, birche —_-vorhe tanne, viehte NHG eiche buche birke Kiefer, fohre tanne, fichte Lith. qZuolas skroblus, skirpstas berzas pusis eglé Lett. udzuols viksna berzs priede egle GaslD eae: Sate asc (borit) jela SCr. _hrast, dub bukva breza bor jela Boh. dub buk briza sosna, smrk jedle Pol. dab buk brzoza sosna jodta Russ. dub buk bereza sosna el’ Skt. ate bhirja- piluddaru, devaddru-, etc. Ay.
8.61-8.65. As illustrative of specific tree names are chosen those for ‘oak’, ‘beech’, ‘birch’, ‘pine’, and ‘fir’, For these and some others (as ‘elm’, ‘yew’, ‘willow’) there are cognate groups com- mon to several of the European branches of IE, but only in a few cases extending to Indo-Iranian. The root connections are mostly obscure. The interest of such tree names lies mainly in their bearing on the moot question of the IE flora and the IE home, and further in the shift of application, connected with dif- ferences in the flora of different regions, So of ‘beech’ to ‘oak’ in Grk. onyds (8.62), of ‘oak’ to ‘fir’ in Gmc, words for ‘fir’ (8.65), of ‘yew’ to ‘willow’ (OE iw,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
etc. ‘yew’, but Slavic zva ‘willow’), be- tween ‘pine’ and ‘fir’ (8.64, 8.65), ‘beech’ and ‘oak’ or ‘elm’ (8.62), etc.
Noteworthy is the primacy of the oak, as shown in mythology and in the recur- ring use of ‘oak’, as the tree par excel- lence, for ‘tree’, also in some derivatives for ‘mountain’ and ‘forest’. :
Schrader, Reallex. 2.629 ff. and in separate items, Hiche, etc. Hoops, Wald- biume und Kulturpflanzen.
8.61. ‘Oak’. 1. IE *derwo-, dru-, ete, in words for ‘oak’ and for ‘tree, wood (1.42), the former, specific, use bells probably the earlier, Walde-P. 1.804 #. Osthoff, Parerga 169 ff.
d Ir. dair, W. a Br. dervenn, all ‘oak’ (an
```


## [2026-10-17T00:01:59.378Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'Rose\\b' BRT.txt | head; grep -n '^1369\\|^ *1369 *$\\|^1370' BRT.txt | head"
}
```


### [2026-10-17T00:02:00.029Z] TOOL RESULT

```
22893:•  j.  varaSa-  m.  i)  'Mehren,  Grossmachen' (nur  Komp.).  2)  Name  einer  Pflanze, vll.  "Rose':  yS  bar^smqtt  *frast)rmte  hae- mqsca   'iss:a  "hanvasca   antar).d3ta    "wer
22896:—  KDs.  väli  -Blurae',  arm.  LW.  vard  'Rose';
22897:Tgl.  np.  ^/ 'Rose'i    s.   daza    Bthl.   WklPh.
21354:1369
22883:1369
22886:1370
```


## [2026-10-17T00:02:02.681Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22888,22902p BRT.txt"
}
```


### [2026-10-17T00:02:02.973Z] TOOL RESULT

```
A.  4>6;  —  vari^ja  F.jh"';  —  ySi  aus.- xraiwä  a£)m>m  varid^n  rämsmca  sfais hiatbis  "die  durch  ihre  Zungen  die  Raserei mehren   und   die   Grausamkeit"  Y.  4g.  4;
—  yaiibyS  xsahnmcl  *ayiBjivamn>m  (sd.) vandaiti  armaitifY.  2&  3;  —  auch  Med.: yf  nä  aMi  aojaftka  vandayattä  yqm  . . gaiüqm  . .  baxsain  (sd.)  "dem,  der  durch die  Kraft  der  A.  gross  machen  wird  das . ." V.  ^0. 3.  a)  Med.  und  Pass.  'wachsen,  ge- deihen': var^ayaiauha  mana  vaca  vTspss^a paiti  varsa/r^  Y.  io.  j;  —  sfaipaike  nS daiühu!  fralataila  vartbataiia  (3SKPM.) Yt  13. 68;  —  yö  daitihave  hu.vaxsJi  fra- t^mnahe  7!ar>\>mnahe  ..  V..^.  zGl.;  — aila  äruxiya  nasus  as.aojastara  vanlayde yaäia  para  ahmät  as  V.  g.  48.  a)  PPfP. 'gross,  gewaltig";  kihrpasca  .  .  srTrä  .  . v)r»zää  am>ianqm  spmtanqm  Yt.y.81;
—  unsinnlich:  kada  .  .  frannil  V)rsz- ääis  s^nghlil  saosyantam  xratavB  (sd.) Y.4tf.3.
mit  vi:  s.  PPfA.
li.  virdhati,  'le,  vardhäyati,  vj-ddhä^;  np. hälidan.  —  Pö.:  vilUan  [tt\.-.  frapihtar  oder - lu  Y.  4g  -ftek  ä)  kort  esiälait),  väßnVan  (erl. : frapiktat  oller  -  ru  Y. /o  -  frärönlar  tartan; (fflr  virnda-):  varaJn.  —  S.  noch  No.  if.  — ')  Unsicher.  Pü.:  välB  Fite,  tri.;  frapih.  — >>  Von  Mills  G.  4Ö  parS  gelesen  t  Einieice Hds.  haben //-j/a,  s.  vorher.
•  j.  varaSa-  m.  i)  'Mehren,  Grossmachen' (nur  Komp.).  2)  Name  einer  Pflanze, vll.  "Rose':  yS  bar^smqtt  *frast)rmte  hae- mqsca   'iss:a  "hanvasca   antar).d3ta    "wer
B.  spreitet  und  Haoma-  und  Rosen-  und .  .  Stengel  dazwischen  tut"  N.97.
KompE.  —    Zum  V.  vat>d-.   —  Vgl.  varAä-.
—  KDs.  väli  -Blurae',  arm.  LW.  vard  'Rose';
Tgl.  np.  ^/ 'Rose'i    s.   daza    Bthl.   WklPh.
fäpS-   598-  —  Pü.:  fehlt, j.  vanda  V,  ?0.  8:  s.  anter  virid-, j.  varüaianqm  Yt.  p.  31:  lies  vSriiian'.
•  j.  varada^*  n.  'Wachstum,  Zunahme, Mehrung' :  para  .  .  axslai  .  .  fradaismca "^imea  vaxsa^smca  V.p.  53;  51,  Y.g.  17, 7/.  17,  Vr.20. 1,  *FrW.p.  2",  Vyt.jp;   —
frada%a..  '^a  (IS.)  Y.55.3;  —  fradathe
•%nica  Y.  68.  2. Zum  V.  vat)d:   —   PO.:  väUin  dahOnlh,   (zu Vr.):    undeutlich;   Sü.:  puffidäü^.    —    »  Wo Hds.  v>r>d'.
•  j.  varvdatgaed'i-  Adj.  'der  die  Lebe- wesen, den  lebendigen  fiesitz,  Haus  und Hof,  Hab  und  Gut  mehrt,  gedeihen  macht', von  Aritai:  arstattm  .  .  frädal^al'^qm '%qm  sen>S^at^qm  Vr.  7.  2;  Y.'s.  7,  Yt 70. 139,  13.  18;  —  ar^tatS  frädat^ihayä •äfl/i  savffgal%ay&  Yt//.  i6;  Y./.  7.
```


## [2026-10-17T00:02:08.585Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^gul\\|^wurd\\|^ward\\b\\|^gulāb\\|^gulgōn' PHD.txt PHD_mackenzie.txt | head; grep -n '^gul\\|^vart\\|^vard\\|^gul-' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:08.927Z] TOOL RESULT

```
PHD_mackenzie.txt:2602:gul [gwll N ......,] flower, rose.
PHD_mackenzie.txt:5191:ward-, v. lwaitan.
1732:gul [gwl] flower 219. — Av. (1369) varoóa- ; Arm. lw. vard ‘rose’ as Aram. (Syr. etc.) lw. wrd’, Arab ward; MPrth wr ‘flower’ (A-H III), NP gul ‘rose,; flower’. Gulaxšan [gwlhš’n'] patron. of *Gulaxš < Valaxš (g. v.) 1174,
3981:vart [wlt'] captive = the next w.?: Mihrak 4 —-ruvän M. whose soul is (to be) captured (?) 132%, cf 6512-18. — MPrth wrd ‘captive’ (MHC).
3982:vartak captive 19%. — Av. (1368) ?varota-; Ps. wldky; MPrthPrs wrdg; NP bardah.
3983:vartčn [wltyn'] wheel: and cand vartén-é [7--?y] as large as a wheel 3118; war-cha- riot 2012-23, — From vart-, v. vaštan. Hen- ning, List 82, reads 3113 vartēnāt and identifies it with MPrs grd(y)n’g, which seems, however, to be the pt. of gardén- and only to refer to the Zodiac.
3984:varten-där [wltynd?l] charioteer 2012,
3985:vartčnišn [wltynän'] transformation
3987:varténitan to change, to alter, to trans- form 7625. 7779.26.27 782.4, 791.3, — Caus. of vart-, v. vastan; Paz. vardinidan.
3988:vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
3991:vartišnēh det. v. n.: hac tan bod bē ~ the departure of the consciousness from the. body (= death) 642°.
6856:vardinidan: varténitan
```


## [2026-10-17T00:02:14.509Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *9[0-9][0-9]\\. gul\\|gul .Rose\\|gul ,Rose\\|gul „Rose' HRN.txt | head; grep -n \"gul\\b.*Rose\\|Rose.*gul\\b\" HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:02:14.875Z] TOOL RESULT

```
HUB.txt:5512:gul Rose' aus yfd-?, vgl. arm. vard,
HUB.txt:5611:np. bar *Brust*; vard *Rose' = np. gul; varz 'Stock' = np.
HUB.txt:5683:p. 255; 18) gul Blume, Rose Bdh. Gl. 225, aber phi. vard
```


## [2026-10-17T00:02:17.820Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5505,5515p HUB.txt; sed -n 5605,5614p HUB.txt; sed -n 5678,5688p HUB.txt; awk 'BEGIN{RS=\"\\f\"} /gul .Rose|gul Rose/{print NR-1}' HUB.txt | head; grep -n -i 'gul\\b' HRN.txt | head -20"
}
```


### [2026-10-17T00:02:18.364Z] TOOL RESULT

```
zd. veredka-^ veretka-; gurs 'Hunger*, gursina^ gusna, gusna
'hungrig', paz. gursnal 'Hunger Min. Gl. 94, phi. gursak
'hungrig', Gl. and Ind. 275, in den Dialekten mit v anlautend,
vgl. Horn Nr. 907, dazu afgh. vaMi'hungrig, also gurs =
zd. *veresa' (oben p. 92) ; gurg 'Wolf* = phi. giirg Gl. and
Ind. 275, zd. vehrka-; gusn 'Mannchen* = zd. varsni-y skr.
vrsni^; Gusasp aus Gusnasp = arm. Vsnasp^ skr. vrsanagva-;
gul Rose' aus yfd-?, vgl. arm. vard,
Ausnahmen:
§ 46. Ap. va- wird zu ga (statt ha):
gardtdaUy gastan (pr. gardam) 'sich drehen, wenden',
vagr *Tiger = np. babr'i (aus bagr?), skr. vycLghra-; va6ar
*Handel, Markt' = np. bazar -^ vank, vang Xaut* = np. bang;
vasx *Wucher' =^ plil. vaxs Ganj. 61. p. 19; vat *schlecht*
= li^.^bad; varaz *Eber (Eznik 66 u. s. w.) = np. guraz;
varapanak-U *Waffenrock' 1 Kg. 17, 38, varapan *Panzer
Thom. Artsr. 37, 2 v. u., eigentlich: *Bru8t-schiitzer zu
np. bar *Brust*; vard *Rose' = np. gul; varz 'Stock' = np.
gurz\ varsamak ^Schweisstuch' = np. bfisclma , vdsama
Velum*; variing *Gurke, Citrone', np. badrang, balang, va-
rang, phi. latrang?; vars *Haar' = phi. vars; vaver, vave-
*vrsa', siehe § 45 ; 14) gurg 'Wolf Gl. and Ind. 275, Bdh.
Gl. 223 = zd. vehrka-; 15) gurtak *Niere' = zd. veretka-
ZPGl. 10, 12; 16) gum 'Mannchen Gl. and Ind. 280, Bdh.
Gl. 224 = skr. vrsni-, vgl. arm. Vsn-asp § 45; 17) yudax-
tak 'fliissig' Bdh. Gl. 222, daneben aber v(i)taxt, ebenda
p. 255; 18) gul Blume, Rose Bdh. Gl. 225, aber phi. vard
in phi. aram. varta, vgl. Horn Nr. 927, arm. vard; 19)
gumartan anordnen, einsetzen, beauftragen' Bdh. Gl. 225,
paz. gumardnn Min. Gl. 93, np. gumastan, arm. gumar-el
'iibergeben, einsetzen (Eliso 56, 7 v. u.; Sebeos 80, 4).
Hier ist zunaehst klar, dass von den Formen, welche
166
893:vielmehr regulär durch ""XDi wiedergegeben. Im
1241:Sahn. I, 88, Vers 494, Sa di, Gul. (Sprenger), 38 Zeile 9.
1666:und (irregulär) pati zusammengefallen, ein Vorgang,
2638:*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL— 60 —
3822:h^nezd'ik'i sengul ftristäd^ büd
4200:Daneben np. cl 'etwas' (Gul. Sprenger 29 Zeile 17).
5865:Muss dialektisch sein, da die reguläre Form np.
6634:762. sex (i'^i^iit auf be/^), Sa di, Gul. 46 Zeile 5 v. u., Spr.)
8531:erscheint im nb. regulär s, vergl. Geiger, Dialekt-
9259:Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
11201:diesen Derivaten sondern regulär stets den Accent auf
```


## [2026-10-17T00:02:23.455Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *92[67]\\.' HRN.txt; n=$(grep -n '^ *927\\.' HRN.txt | head -1 | cut -d: -f1); [ -n \"$n\" ] && sed -n \"${n},$((n+8))p\" HRN.txt; awk 'BEGIN{RS=\"\\f\"} /HUB/{}' /dev/null; awk 'BEGIN{RS=\"\\f\"} /gul Blume, Rose Bdh/{print \"HUB leaf\",NR-1}' HUB.txt"
}
```


### [2026-10-17T00:02:23.781Z] TOOL RESULT

```
8027:926. guften sprechen, Praes. göy-etn, guftar 'Rede', gep,
8033:927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
Daraus sind bokanntlich entlehnt it. ghdehhe ^ fr. julep^ sp.
julepe *Küliltrank*.ma
- 207 -
phlv. varta d. i. varda ^) (PPGL), g^d (Bund.), vard in
arm. arab. LW. vard, (sogar ar. muvarrad rosenfarbig',
AM. 168 Zeile (>), vergl. arm. Vardges, phlv. N.
pr. Vardakl (Gemme, Hörn, Mitteilungen, Heft IV,
HUB leaf 171
```


## [2026-10-17T00:02:28.133Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8041,8050p HRN.txt; grep -n -i 'julab\\|jul[aā]b\\|gulab\\|gul[aā]b' HRN.txt AFM_pages.txt LKT.txt SKT.txt FVQ_pages.txt | head -20; grep -n '^JULEP' SKT.txt"
}
```


### [2026-10-17T00:02:28.459Z] TOOL RESULT

```
pr. Vardakl (Gemme, Hörn, Mitteilungen, Heft IV,
34); gr. Qoäoy, lesb. /J^'Jor.
927»»*« gil 'Schmutz. Lehm'.
arm. kir Xehm' (Fr. Müller, WZKM. 5, 268)2).
928. guia, gelü (AM. 109 Zeile 1 v. u.) 'Kehle .
aw. garah' 'Kehle'; phlv. garük vd. 15 (11); skr.
gala-; lat. gula; arm. vergl. -kul '-verschlingend' (H.
No. 145), ker 'Nahrung, Frass' etc. (H. No. 143).
kurd. gerü 'Kehle'; af}'. yäre; oss. gm' (166; un-
sicher); sangl. yar,
```


## [2026-10-17T00:02:34.659Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^julep\\|JULEP' SKT.txt KLN_1966.txt | head -5; grep -n 'جلاب' AFM_pages.txt AFM.txt | head -5; grep -n -i 'gul[aā]b\\|dschul\\|ğul[aā]b\\|julab' LKT.txt incoming/PLA/PLA_pages.txt | head"
}
```


### [2026-10-17T00:02:35.038Z] TOOL RESULT

```
KLN_1966.txt:1142:Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
KLN_1966.txt:20443:F.,  fr.  Late  L.  zizyphum,  ‘jujube’,  which  together with  Late  L.  zizyphus,  'jujube  tree’,  derives  fr. Gk.  Shipov,  ‘jujube  tree;  jujube’,  which  is  of unknown  origin.  Cp.  Zizyphus. julep,  n.,  a  sweet  drink.  —  F.,  fr.  OProven^.  julep or  fr.  Sp.  julepe,  fr.  VAr.  juleb,  corresponding to  classical  Arab,  juldb,  fr.  Pers.  gulab,  ‘rose water,  julep’,  which  is  compounded  of  gul,  ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest.
KLN_1966.txt:33124:rose,  n.  —  ME.,  fr.  OE.,  fr.  L.  rosa,  fr.  Gk.  poSov, ‘rose’, for *Fpo8ov,  fr.OIran. *  wrda-  (whence also Aram,  warda.  Arm.  card).  OIran.  *wrda-  be¬ came  gul  in  ModPers.  in  the  sense  of  the  pho¬ netic  law,  according  to  which  initial  w  becomes  g and  -rd  is  changed  to  /.  Turkish  giil,  ‘rose’,  is  a Persian  loan  word.  OIran.  *wrda-,  ‘rose’,  repre¬ sents  I.-E.  * wrdho-,  ‘thorn,  bramble’,  whence also  OE.  word,  ‘bramble’,  Norw.  dr,  ol  (for *ord),  ‘currant,  bush’.  Cp.  rhodo-.  Cp.  also  the first  element  in  julep  and  the  second  element  in bedeguar.
```


## [2026-10-17T00:02:38.372Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; awk 'BEGIN{RS=\"\\f\"} NR==104{print}' data/verification/sources/refs/incoming/PLA/PLA_pages.txt | head -60; command ls data/verification/sources/refs/ocr/PLA 2>/dev/null | head"
}
```


### [2026-10-17T00:02:38.629Z] TOOL RESULT

```
Yulbat                                                                      89                                                     Zulfakar

ul     -        &ulbat:          "großes           Schiff"          aus    dem      pers.Z)s golbat               1     vielleicht         aus
       dem           pers. J; gul               "Riese"        + „bat             "Ente",


are             -    $ulbahang:             "Semon           fruiticis           spinosi"         aus    dem    pers.      BERN $olbahang.


ur - Zulbahank = $ulbahan? s. Zulvahang                                                      °.

Suse - $ulbahik - Zulbahank s.                                            Zulbahank °.

Slip - Äultäg:                       "eine       Pflanze"           pers.        4,


PANNE
    NT Zun           $ulduran:             "Sesam",           wahrscheinlich               aus     dem    pers.       nd         golgolan       5,
       s.           gul    u.    ward.


BI     lo       -    £ul$abin:
                                 -         "Rosenkonserve'"                 aus     dem    pers,
                                                                                                          r,
                                                                                                         u de golangabin
                                                                                                                                 6        aus
 “     dem           pers.      ygol        s.     Zul + angabin                  —T mp.     wypp       anguben       7,


Jr = &ild:"Haut"                          pers.        aus    dem    mp.               jalta      8     syr.    Y>a°.


put - Yalsäm:                        "Fieberwahn"              =     Zarsam        10, s.      barsäm,         balsam       u.     sarsäm.


Orr         -       Eulsän:          "Rosengarten!                 aus    dem     pers.      „tugolfan          Ss.   gol    11,


Die             -    $ulistän:             "Rosengarten!"                aus     dem   pers,       oO.     golestan          s,.    gol   12,


A           - Zullakar:                   "Rosenzucker"              pers.         13, aus     dem      pers. $’gol s. gul + pers.
       Be Sakar                      "Zucker" —T mp. )y., Bakar -


1.    BQ.           s.    v.
2.    Löw           s.    v.,    FM.       s.     v.
3.    ebda.
4.    FM.           S.    v.
5.    Löws.               v.
6.    FM.           s.    v.
7.    Mackenzie                 s.    v.
8.    Pahl.-
         paz. s. v.
9.    Brockelmann                    s.    v.
10.    LD.           s.    v.
11. Steingaß                    s. v., Muhlt s. v., al-Mufarrab                                   s. v., LD.          s. v.
12,    LD.           s.    v.
13. Muhit s. v.

0018.png
0018.txt
0022.png
0022.txt
0027.png
0027.txt
0194.png
0194.txt
```


## [2026-10-17T00:02:41.554Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; awk 'BEGIN{RS=\"\\f\"} NR==103{print}' data/verification/sources/refs/incoming/PLA/PLA_pages.txt | grep -v '^\\s*$' | head -60"
}
```


### [2026-10-17T00:02:41.885Z] TOOL RESULT

```
kafsin                                                                 88                                                     Zulbän
rer - Kafsin = dabsin                             s.    Zabsin.
Jer- gagal:               "Schakal"              aus    dem pers.           Jix+ dokäl    >        tk.   cakal         , schakal.
               tk.        tschakal              <T pers.       schagal,        skr.     srgala      2,
Je-    Zul:        "Decke,           Pferdedecke;              Schleier"        3 pers.,        syr.     Bu    ®.
32-    Zul:        "zudecken!               s,    £ul.
JP- Zul:           "Blume"           aus dem pers. Ygol i <—Imp.)r gul —Taw.                                     varzsa       Dar.
       Lw.     ward        6 s.       ward.
RENT -       $uläb:        "Rosenwasser"                 pers.        75.     gul,     lat,    julapium,         it.    julepe,        sp.
       Julep.         8,
                                                                                                                                  9
       dtsch.         Julep:              "kalter       Alkohol        mit    Pfefferminze'               pers.         > ar.
Vo - Ziläl: PL. voyeful s. Zul.1.
ee       -    $uläh        q:       "Schießkugel"              aus     dem    pers.      &,#    gulüle        1         mp.    97%
       girdag         12,
Wr       -    falbä        :    "eine           Art    Anzug"     pers.       13, wahrscheinlich              aus      dem    pers.
             Le Zulpa.
ol       -    $ulbän:           "Schoten"              pers.     14 „us       dem     pers. or y golpän           s.    gol u.        pän
                      .                                                                        4
       inoLGs              huskbän.
1. Muhit s. v.
2.    Wahrig         s.    v.
3.    Wahrmund            s.    v.
4.    Brockelmann               s.    v.
5.    Wahrmund            s.    v.,       al-MuCarrab            s.    v.
6.    Nyberg         Bd.       II    s.     v.
7.    Wahrmund            s.    v.,       Littmann        s.     v.
8.    Löw     s.     v.
9.    Fremdwörterbuch                      s.    v.
10.    FM.     Ss.    v.
11.    Wahrmund            s.       v.,     al-MuCarrab           s.    v.
12.    Mackenzie               s.    v.
13.    albasa         s.       v.
14.    LD.     s.     v.
```


## [2026-10-17T00:02:46.728Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:1822 BQT:2290 IRN:129; do echo \"=== $r\"; python3 tools/ref_page.py $r --image 2>&1 | head -80; done",
 "timeout": 300000
}
```


### [2026-10-17T00:03:06.096Z] TOOL RESULT

```
=== BQT:1822
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1822.png
REF: BQT:1822  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 619  OCR-lang: fas

بیان چهاردهم
در کاف فارسی با لام مشتّمل بر یکصد و سه لغت و کنایت
عل ۱ < بنم اول وسکون نانی»معروق خوانند.. تبی را که در ایام وبا و طاعون بپم‌رشد
است و جریی ورد خوانند - و بمعنی‌اخگرآنش | لافع است . کوبند وقتی در ارمن وبا و طاعون
همست - و رنگه سرخهرا نیز گویند - وطریق | عظیمی بهم رسید چنانکه معدودی چند مانده
کنایه افاده معنی‌دولت هم میکندچنانکه کوبند | بودند چون ازایشان تفحص کردند در آن‌یام ازین
« از کل تو اینها را می‌شنویم > بعنی بدولت کل می‌خوردند ۰
تو- وبکسراول,/خا4 باب آمیٌخته را کوبند ۲ .#۸ گل‌اقر یی ۴ «بکسر اول و فتح
علاج ۳ م اول وئانی بالف کشیده الک و سکون قاف و رای قرشت بختانی‌رسیده
و بجیم زده » نام حلوائی است پاکیزه و عربان | و طای حطی مضدوم بسین بی‌نقطةٌ زده . نوعی از
قطایف میگوبند ؛ و بسنی کوبند لالیست بیار | کل باشد و آنرا از جزایر بونان آورند. کوبند
داز و تنك ماشدکاغذ حربر و آنرا از بشاسته | اکر زن آبستن بر خود بندد بِچچهٌ او را آسیبی
وتخم مرغ پزند ودرشربت قند ولبات ریز کنند | رسد تا برسد .
و با فاشق و چمجه بخورند . گلا گو نه * - بنم اول وکاف فارسی
گل‌ار به - نم اول و کسرئانی‌وهمزه بواو رسیده و فتح آلون , بمعنی غازه و کلگونه
مضموم برای قرشت زده وفتح بای ابجد , دوائی | است و آن چیزی باشدا سرخ که زنان بر روی
است که آنرا ازشامآورند و عنبر بید نیزخوانند. | مالند . ۱
کزند کی جانوران را نافع است و بعربی جعده گل ] گین کردن - کنایه از لبریز
کویند . کردن بعنی پرساختن پیاله و صراحی باشد از
گل‌ارهنی * بکسر اول و ثانی,گلی | شراب لعلی ۰ .
۰ باشد سرخ رنگه بسیاهی مایل وچمریی طین‌ارمتی کلاله < بروزن نخاله » بمعنی پیراهن
۹ - در اوراق مانوی (بپارتی) ۷*۶ (کل‌سرخ ) . اوستا - ۷۵۳۵41128 ۰ ارمنی ۷2۳4
(88 . ۶ و1 ,125 , 8508 ...86۲5188 ۸۸:۵6 ۵۲ 1عا ۸ ,8 )۰ پهلوی
آناچ . ۰۷2۲۸2۵ ۷:42 » معرب «ورد» ( بفتح اول ) » فس: ارمنی ۷2۲888 «اسشق ۹۲۷
کردی 801 (کل سرخ ) . [اع ( خار ) « ژاباس ۳۹۶ زازا ۷11۵ > ژابا س 2۳۵ > کینکی
آ۵ع . ۴ - پپلوی أذْع «منای ۲۷4 : ۷ رك : اسشق- هوبشمان ‎٩۲۷‏ 18 .
۴ - مخغف «کولاج»(ه.م.) کولاج(ه.م.)ورك : کولالج:
خوشنوسان قطابف با قلمهای شک ص 4
باق السه ارنیدی | ویو نوی
۱ ی بم اول, درختی است (60821218 8)) بن راو 1
از دستهٌ سیبی‌ها (8ع002:206) «کل کلاب ص ۲۲۷ > دارای و
میوءٌ مخروطی شکل ولذید . ب رکه وشکوفة کلایی-»

=== BQT:2290
(no exact page map; using offset -1917 -> pdf page 373; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2290.png
REF: BQT:2290  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 373  OCR-lang: fas

وکیل در ۹۰۳
و کیل‌در۷ - وکیل دربار و تایب ۱ مناب راگوبند .9
در واو با لام مشتمل برچهارده لغفت وکنایت
ول ؟ - بفتح اول وسکون ثالی, بممنی هم آمده است.
خصوصاً وبعربی فقاح‌الکرم(۱) خوانند. راکوبند .
تا رسمان که رشته شود ازدو4 بیرون نرودوآارا ولایت‌ستان ۴ ه کنابه از اولیاء ات
بعربی فلکه خوانند ۴ - ودر عرپی‌بممنی‌زاییدن | است .
باشد ۴ ۲ ولایت قالوابلی ۸ «کنایه‌ازایمان
ولانه « بفتح اول پروزن زماله,بممنی است بمنی که ارواح موْمنان با خدای‌تمالی بدان
جراحت وریش باشد ؛ و بکر اول پروزن‌فانه ] میئاق وعهد کردند و پیمان بستند .
(۱) چك , چش : فقاع‌الکرم . در جهانگیری مانند متن است.
درگاه پادشاه مقیم می‌داشته‌اند که کارهای مربوط پایشان را انجام دهد و مراقب مصالح کارباشد :
« ازمعدی شنودم ۰ وکیل دره که خوارزمشاه سخت لومید کشت و بدست وپای بمرد.» « تاریخ
بیهقی مصحح دکترفیاضش ص۳٩‏ متن وح۲ > «وکیل‌در ( یمنی و کیل‌دری که ازطرف سبکنگین
در بغارا بود ) ابشت ( به سبکتگین ) که رسول می‌آید بدین خدمت ...۰« تاریخ بیهقی ابضا
ص ۲۶۸ متن وح ۰.۹۵ ۲ - ۷۵1 ( جم واو ) درلوجه‌ها بمعنی گل‌آهده :
ملل زلف بر رو ریته (ریخته) دیری (داری) ول وسنبل بهم آمیته ( آميخته )دبری
پریشان چون کری (کنی) آن مار زلفان بهرتاری دل آویته ( آويخته ) دیری .
بابا طاهرعریان همدانی «فرهنگه نظام».
و بدعنی شکوفه نیز » فرع همین معنی‌است . در برهان بفتح اول و درجم‌انگیری بکسراولآهده-
1 ( بکسر واو ) بمعنی ترك ورهاست و * ول کردن » بمعنی رهاکردن است .
ارچ رك:سروری. ۴ ولادة (رلادت). و «خفل‌والانه ( م.( ۹ اکنون
۷ات ءا-ت. ۷ - از: ولابت (عر)ستان (ستاننده) لغة معنی شپر کیر, کشو رکنا :
واپْدهم علی‌اشهم‌الست بربکم ؟ فالوا : بلی شهدنا آن تقواوایوم‌القيمةانا کناعن هذا غافلین. »
۰ وگال - ر2 : لغات متفرقة پایان کتاپ .
(برهان قاطع ۲۸۸)

=== IRN:129
(no exact page map; using offset 11 -> pdf page 140; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/IRN/0129.png
REF: IRN:129  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 140  OCR-lang: fas

سرگذشت واژُه گل ۱۳۹
اینرو آنرا آرامی پنداشته وجزء لغات هزوارشی آورده اند.
تحول‌دیگر این واه بنابرقاعدهٌ زیانشناسی ایرانی (1--۷4) است و دراوایل
دوران اشکانی صورت گرفته است. این شکل کهن را در گویش سمنانی می‌بینيم
که واه ۷۵۳۵2 به وال ۷212 تحول یافته است و نیفتادن وایل آخ رکلمه‌نشانی
از قدمت آنست . در دوره‌های بعد با افتادن وایل 2 از آخ رکلمه» این واژه بصورت
ول ۷۵1 در آمده است , در برهان قاطع آمده : ول» بفتح اول و سکون ثانی بمعنی
شکوفه باشد عموماً و شكوفةٌ انگور راگویند خصوصاً .
با باطاهر وازةٌ ول را بمعنی گز. استعمال کرده است,ء
مسلسل زلف بررو ریته دیری ول و سنبل بهم آمیته دیری
پریشان‌چون کری‌آن‌تار زلفان بهرتاری دلی آویته دیری
که معنی آن چنین است:
مسلسل زلف بر رو ریخته‌داری گل وسنبل بهم آمیخته‌داری
پریشان چو ن کنی آن تار زلفان بهرتاری دلی آویخته داری
در ترانه‌های روستایی این واژه گاهی بمعنی گل وگاهی بمعنی گل یکه‌بدان
عشق می‌ورزند یعنی يار و معشوقه آمده است.
شب تاریک وره باریک وول مست کمون ازدست من افتاد وبشکست
کمون دارون کمون از نو بسازید ولم یاغی شده مشکل دهد دست
واژْهٌ [۷2 يا ۷۵1 با 8022 بمعنی گونه تر کیب يافته و در فرهنگك‌ها ولغونه
و والفونه بمعنی‌غاژه یاسرخی (سرخاب) زنان آمده است
در دوره‌های بعد این واژه از [۷2 و۷۴1 تحول یافته بطکورت گل اج و در
لهجه‌ها [84 در آمده است . در زبانشناسی تطبیقی ایرانی همواره یک ۷ قدیمی با
رن دادن به وایل بعدی خود بصورت 8 در می‌آید مانند ۷154390 که 0ف3ا3اع
شده و عا7طاه که ع3تاع (گرگك) شده است و غیره.
بدین ترتیب واژْةٌ گل لا فارسی از واژةٌ کهن اوستایی ۷۵۳۵8۵ درآمده
است.
```


## [2026-10-17T00:03:12.478Z] TOOL CALL #26: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/IRN/0129.png"
}
```


### [2026-10-17T00:03:13.047Z] TOOL RESULT

```

```


## [2026-10-17T00:03:13.044Z] INPUT

[Image: original 2080x2955, displayed at 1408x2000. Multiply coordinates by 1.48 to map to original image.]


## [2026-10-17T00:03:17.611Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '\\brose\\b' SOD_pages.txt | head; grep -n 'GOL\\b\\|VARD\\|ROZ\\b' incoming/ARY/ARY_latin_index_pages.txt | head; grep -n '^گل \\|^ورد\\b\\|^گل[ ،:]' incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-17T00:03:18.026Z] TOOL RESULT

```
3273:                           rose        Av. varzSa-                   a separate phoneme is the fact that the Uigurs, who
33043:          C2 gloss. p230; STi 21.18; GMS 939, 1088; BSTii                 145; "rose-colour" wrSYwn Twite,
33088:          rose
39321:rose   10149                             saint 751,9437,9438, 11368,            saw 10420
519:Ab shoal etbtth til 92 S pte 9 SUR L Wj eat 37 22 end GOL,
781:eeK eat cael > ange Ob5 AS obo po "op SL gS" otly GOL! Tages
1141:52590 38) 537 Gilg) GOL; a sath 9 ging Shar ob ple Jy Curl 03 Srl wore y
2844:i Sy ahs Se te 9 (SL 2 eu alaul 9 He GOL) ST 0 OT OSU L slabs» “vale!
3076:OLD NORSE) Sp,  VARD (PAHLAVI) 5
3097:VARDE LATVIAN) (3) iy
5247:(PAITI) 150, (LEUGH) 687 PEROZ, PEROZGAR
5249:AMINDAROY: (TRIUMPH) 302 PEROZ ARMENIAN) | s,\
5757:pal Wend esd GOL a gi a Bed 2s atl
5935:ga Gly ody glad abs 9 aMlel GOL 29 5s cal
```


## [2026-10-17T00:03:20.191Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33030,33095p SOD_pages.txt | cut -c1-160; grep -n '^10149\\|10149' SOD_pages.txt | head -3; sed -n 3070,3080p incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-10-17T00:03:20.674Z] TOOL RESULT

```
      crow(j)                                                 10140 wrewnkry1 B                         ^^JUjM
      GMS 1186 n 1                                                  warcun-karya
                                                                    miracle, magic
10131 wr'kh B, S                                •.*«>-
                                                                    TSP 13.1; S W, HJ 1976 p54
      wara(k) ©f.n^ ob. -y/z =»wr-
    411                                                                    rosy

                                                                                                                     wrmyy'h
    10141 wrcwny} C                                                      war8-yon ©<*warda-gauna
          warcu/onya (wrc wnyO ©pi. wrcwnyt
            =^wrc}wny(h)                                                 GMS 1113; BSTBL, Dhy. 145, 146; Benv. Titres
          miracle, wonder                                                 et Noms Propres. 122; wrdYwn fiymy, Dhy.
          C2 gloss. p230; STi 21.18; GMS 939, 1088; BSTii                 145; "rose-colour" wrSYwn Twite,
            857.7, 861.57, 880.14                                         warSron-ronc, Dhy. 146; CII 1990 B15, 16
    10142 wrc wny* =4 wrcwny*                                     10154 wrg M                                (£^P
    10143 wrcxwndqy* M               uT* j*** (jJ^\cJ&,
          warc-xundakya                                                  warag
                                                                         Aries      =^wr*n
            ©*var?cahvant>*varcxwant>warcxund                            Hen. AM      1952, 203, 9
          miraculous
                                                                  10155 wryVY'nt ? B                                •l/(t^>)
          GMS 939; BBB; Hen. BSOAS 8.586, 12.307, 18,                    (wryVrY^t)
            (Cosm.)
                                                                         (name of a)plant
    10144 wrcy> B, M                     >l«*>J\flJ7                     TSP 3.286; S W, BSOAS 38, 1975, 133
          wo/iracya, wracya ? (wrcyh) ©*wi-rata-,
                                                                  10156 wryNvry'nt =» wrY}YJ*Y>nt?
          ^Sram- +usi-t wrt+sy} ?                                 10157 wryd'r- C                                           #*,mJ
          appeased
          BBB p67, 539; BSTBL, Dhy. 27, 94, 240; TSP                    wiraydar ®<*wrVt-6yr- ©trans, pret.
            3.217; Frag. Len. 44.10, 97b2; Gersh. Sogd.                    =»wrycd}r-
            Cpds. 145n 1; C2 p!48                                        (/o)pour
                                                                         STii 4.33; GMS 218; Sund. AoFviii 1981, 21V1
    10145 wrcy'str S                         JLjfJ'frJtW
          wiracyastar, wracyastar                                 10158 wrh       B, S~> wr-
l         most soothing                                           10159 wrq'ry C                             •Jti\iiXjoJ*
          GMS 1289                                                      warakare ©pi. -t
                                                                        profitable, advantageous
    10146 wrcy'w'k B
                                               J*y3tJ*\J                BSTii 908.19: C2, 40R19, 48R5; STii 6.42; Gersh.
          w(i)racyawe, wracya we
          appeasement                                                     Sogd. Cpds. 138
          TSP 15.6; STii, 9.5 p599; GMS 1082                      10160 wrkr B, M                                           J j>

    10147 wrcy'wn'k S                                                    warkar (wrqr) ©Parth. wargar-, <*warka~r/n
                                               J>^J
          wiracyune,                                   <cr*'->'
                                                                         leaf
                                                                           ©pi. -t
          appeasement, security
          GMS 1087; Karab. Insc. 21.4 apud. Hen. BBB                    Sogdica. 4; GMS 943; VJ 955, 1370 n p96; Frag.
                                                                          Len 38.8, 18, 41.6, 84a6; Sund. AI 28, 185
            p67, 539
    10148 wrcyh   B =» wrcy>                                      10161 wrqr      C => wrkr
    10149 wr6'-tyyM                                  /</          10162 wrm       M, B                                  j^ljT
          war5 (wrd) ©Av. varzSa; <*warda         ©pl.ob.               w(i)ram ©loc. -yyyh          =*wyrm, *wrm, ^vrta,
                                                                          wyr'mCy), wrmyy*h
          rose
                                                  C^
          GMS 207, 282, 526; BBB 574; C2, 68R27                         quietness
                                                                        GMS 213n 2; Hen. Cosm. 307.43; Frag. Len.
    10150 wrS2 S                                          t^T             97c 1
          or5 =»}wr5
          there                                                   10163 wrm'ych B                ^ <£» j^-. < JU-U £_y»
          Anc. Lett. 5.7                                                warmecya ? ©Av. varpmi; Pahl. warm
33085:    10149 wr6'-tyyM                                  /</          10162 wrm       M, B                                  j^ljT
39321:rose   10149                             saint 751,9437,9438, 11368,            saw 10420
45428:  '     SW, xwast, 1991,      panamCI, 1991,                     X                                              10149     +
Seetlaak
epSEhS gt s5 D5 29 039 cal om
at Ste 055 F552 05s al ow
wad path SAS iy Fle W522 Ss cal om
4
7
OLD NORSE) Sp,  VARD (PAHLAVI) 5
WARTA — (OLD SAXON) ofS gi 3-S VARSMAN (SANSKRIT) <2 Suite
WARTE (OLD FRISIAN) WSs 1.3 GORT ARMENIAN) 2)

(OLD HIGH GERMAN) 24S glT VERRUCA LATIN) ys
```


## [2026-10-17T00:03:24.835Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=3076 && /\\[pdf page/{p=$0} NR==3076{print p}' ARY_latin_index_pages.txt; grep -n 'WRDHO\\|WROD\\|RHODON\\|VAREDHA\\|VAR∂DA' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:03:25.221Z] TOOL RESULT

```
[pdf page 108]
```


## [2026-10-17T00:03:28.668Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i 'wrdh\\|wrod\\|rhodon\\|varəδa\\|vareda\\|varada\\|wurd\\|rosa\\b' ARY_pages.txt | head; command ls; "
}
```


### [2026-10-17T00:03:29.110Z] TOOL RESULT

```
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
```


## [2026-10-17T00:03:31.307Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=3076 && NR>=3040' ARY_latin_index_pages.txt | head -40; grep -c 'pdf page' ARY_pages.txt; grep -n 'ROSE\\|Rose\\|rose' ARY_pages.txt | head"
}
```


### [2026-10-17T00:03:31.921Z] TOOL RESULT

```
10935405 Sb S 23s onl owe
sel aly gaat jl pt Sy gdb
ip thy CAFU oF
BALESHT AFGHAND) () gil BAREZISH s(AVESTAN) gis 9\
(SANSKRIT) ey Sule OLD PERSIAN) ihuel, go 3h,
BARHISH, BARISHN BALESHT, BALIN
BULGA (ULEX(GREEK) gly BALISH PAHLAVI) «5 Shy
BALGS GOTHIC) Si BAZ AOSSETIC) ga)
we
[pdf page 108]
i!
V9 1 CET CSS oe 4) gh
POLSHTAR, PODUSHKA HOLD SCANDINAVIAN) S.5-ces\
BLAZINA 1( SERBIAN) 9 pe BELGR, BOLSTR
BALNAS (LITHUANIAN) gi 3 BELER HOLD NORSE) S335
PABALSTS LATVIAN) (3) 6) BELGAN (OLD SAXON) oy pS
BALSINIS :(OLD PRUSSIAN) 4S 59.4 -BULGEN — (OLD FRISIAN) pS 64.3
(OLD IRISH) AS 544 p\ BALG :(OLD HIGH GERMAN) yf git
BOLG, BOLGAIM BALG (GERMAN) galt
BOLY, BOLA (WELSH) 5) BIELG, — (OLD ENGLISH) op gS)
BELIG, BALG, BALIG
REFERENCES bok, BELLY ENGLISH) SS
POKORNY =~S~*~*~*~*«wS DG BUG DANISH) Sil
BARNHART — (BELLOWS, BELLY) 88 BUK, BALG (SWEDISH) 4 yo
DELAMARRE: (COUSIN) 117 BUK (NORWEGIAN) 535
MACKENZIE: (PILLOW) 127 BALG DUTCH) ucla
BUCK: 252-254 POLSHTAR, POLISH) glo)
ONIONS: - (BELLY) 87-88 PODUSHKA :
SKEAT: (BELLY) 55 BOLOZEN (RUSSIAN) +3)
rr : sebi iby (CZECH) Sey
Seetlaak
epSEhS gt s5 D5 29 039 cal om
at Ste 055 F552 05s al ow
wad path SAS iy Fle W522 Ss cal om
4
7
OLD NORSE) Sp,  VARD (PAHLAVI) 5
545
```


## [2026-10-17T00:03:35.568Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n 'VARDA\\|VARDHA\\|VAROS\\|VAR∂S\\|ROSA\\|RHOD\\|GUL\\b\\|WARD\\b' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:03:35.978Z] TOOL RESULT

```
520:aceolndys Sighyysl sea GUL) CALE yo edie dp cary g 2p) ULI SU 5a JT jl
1127:he Bal Wks 4 BAS cell 4 AS Als! GUL; Obslole y SLIKEI algo 5
1815:we Slip (ailegy GUL; 9 SY 2 5s cel om
2164:RHOD - (GAULISH) SE RUEDA (SPANISH) lily
3621:a gph 602 S Gla Fogg) GUL; 22 05s cal om
3710:gen GUL; 42 OT Glan Jy e| CONOMATOPOETIC) “pls yal gol S aw Sy
4216:Yo SH yar BE 5 AT GALA GUL; 32 15d Gol
4782:65, (AFTERWARD) 101, (LBST) 121 PASCAT, PASCA, PACCA =: + ar
5301:each pe wal gg} GUL; 2 OS cal
5367:. ebay ob teBV y aii GUL; 22 05 cal
```


## [2026-10-17T00:03:38.881Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-17T00:03:41.077Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-17T00:03:46.880Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%84' \\\n 'https://en.wiktionary.org/wiki/%E1%BF%A5%CF%8C%CE%B4%CE%BF%CE%BD' \\\n 'https://en.wiktionary.org/wiki/rosa' \\\n 'https://www.etymonline.com/word/rose' \\\n 'https://www.etymonline.com/word/julep' \\\n 'https://en.wiktionary.org/wiki/%D9%88%D8%B1%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%A7%D8%A8' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/w%C3%BAr%CC%A5das' \\\n 'https://vajehyab.com/?q=%D8%B1%D8%B2&d=moein' \\\n 'https://vajehyab.com/?q=%D9%88%D8%B1%D8%AF&d=moein' \\\n 'https://en.wikipedia.org/wiki/Sohrevard' ; do python3 tools/fetch_source.py \"$u\" --note \"page 556, root Wrdho (rose): gol/vard/rhodon/rosa/julep/roz/Sohrevard\" 2>&1 | tail -1; done",
 "timeout": 300000
}
```


### [2026-10-17T00:03:52.118Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8d83ef3016d6c78a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/472ecfb4a2f00d31.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/219f00b82b74d2ce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b92f4e0e8cff33c8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/be31610a43bbe132.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d73100561a698a25.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/85207fff344ada3e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/688cf642d1446994.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8bc1a85f3a256b1c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a5edfba72b118227.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f7612a5b9a88ec2a.txt
```


## [2026-10-17T00:03:54.336Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 8d83ef3016d6c78a 472ecfb4a2f00d31 688cf642d1446994 d73100561a698a25 85207fff344ada3e; do echo \"=== $f $(wc -c <$f.txt)\"; grep -n -i -A6 'Etymology' $f.txt | head -40 | cut -c1-500; done"
}
```


### [2026-10-17T00:03:55.038Z] TOOL RESULT

```
=== 8d83ef3016d6c78a 21958
65: Etymology 
66-
67- 1.3 
68- Suffix 
69-
70- 2 
71- Khalaj 
--
95: Etymology 1 
96-
97- 4.1.1 
98- Noun 
99-
100- 4.2 
101: Etymology 2 
102-
103- 4.2.1 
104- Noun 
105-
106- 5 
107- Persian 
--
112: Etymology 1 
113-
114- 5.1.1 
115- Pronunciation 
116-
117- 5.1.2 
118- Noun 
--
127: Etymology 2 
128-
129- 5.2.1 
130- Pronunciation 
131-
132- 5.2.2 
133- Noun 
--
145: Etymology 3 
146-
=== 472ecfb4a2f00d31 9572
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
168: Etymology
169- [ edit ] 
170-
171- From Proto-Hellenic *wródon , borrowed from some Eastern language, most likely Proto-Iranian *wardah ( “ flower, rose ” ) (compare Mycenaean Greek 𐀺𐀈𐀸 ( wo-do-we ) , Old Persian *vr̥dah , Aramaic 𐡅𐡀𐡓𐡃𐡀 ( warda ) , Classical Syriac ܘܪܕܐ ( wardā ) , Old Armenian վարդ ( vard ) , Demotic Egyptian wrṱ , Arabic وردة ( warda ) , Persian گل ( gol ) – all from the same source). [ 1 ] An alternative source could possibly be as a Pre-Greek loan, such as Thracian (the rose was native to Thrace). [ 2 ] 
172-
173- Latin rosa ( “ rose ” ) is likely a loanword from Ancient Greek.
174-
=== 688cf642d1446994 172
=== d73100561a698a25 33479
62: Etymology 1 
63-
64- 1.1.1 
65- Verb 
66-
67- 1.1.1.1 
68- Conjugation 
--
86: Etymology 2 
87-
88- 1.2.1 
89- Noun 
90-
91- 1.2.1.1 
92- Declension 
--
104: Etymology 3 
105-
106- 1.3.1 
107- Verb 
108-
109- 1.3.1.1 
110- Conjugation 
--
113: Etymology 4 
114-
115- 1.4.1 
116- Noun 
117-
118- 2 
119- North Levantine Arabic 
--
124: Etymology 
125-
126- 2.2 
127- Pronunciation 
128-
129- 2.3 
130- Noun 
--
=== 85207fff344ada3e 8338
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
82: Etymology 
83-
84- 2.2 
85- Noun 
86-
87- 3 
88- Urdu 
--
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
98- 3.3 
99- Noun 
--
193: Etymology
194- [ edit ] 
195-
196: Etymology tree
197-
198- Proto-Indo-European *Hwerdʰ- der. ? 
199- Proto-Indo-Iranian *(H)wardʰ- 
200- Proto-Iranian *wardah 
201- Old Persian *vr̥dah 
202- Late Middle Persian gwl ( gul ) 
--
319: Etymology
320- [ edit ] 
321-
322- Borrowed from Classical Persian گُلَاب ( gulāb ) .
323-
```


## [2026-10-17T00:03:57.363Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 196,240p 85207fff344ada3e.txt | grep -v '^\\s*$' | cut -c1-400; grep -n -i 'Etymology tree' -A30 8d83ef3016d6c78a.txt | grep -v '^\\S*-\\s*$' | head -50 | cut -c1-400"
}
```


### [2026-10-17T00:03:58.102Z] TOOL RESULT

```
 Etymology tree
 Proto-Indo-European *Hwerdʰ- der. ? 
 Proto-Indo-Iranian *(H)wardʰ- 
 Proto-Iranian *wardah 
 Old Persian *vr̥dah 
 Late Middle Persian gwl ( gul ) 
 Persian گل ( gol ) 
 Proto-Indo-European *h₂ep- der. 
 Proto-Indo-Iranian *Hā́ps 
 Proto-Iranian *Hā́fš 
 Old Persian 𐎠𐎱𐎡𐎹𐎠 ( a-p-i-y-a ) 
 Middle Persian ʾp̄ 
 Persian آب ( âb ) 
 Persian گلاب 
 From گل ( gol , “ rose ” ) + آب ( âb , “ water ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ɡu.ˈlaːb/ 
 ( Dari, formal ) IPA ( key ) : [ɡʊ.lɑ́ːb] 
 ( Dari, formal ) IPA ( key ) : [ɡʊ.lɑ́ːb] 
 ( Kabuli ) IPA ( key ) : [ɡʊ.lɑ́ːb] 
 ( Hazaragi ) IPA ( key ) : [ɡu.lɔ́ːb̥] 
 ( Iran, formal ) IPA ( key ) : [ɡ̥o.lɒ́ːb̥] 
 ( Tajik, formal ) IPA ( key ) : [ɡu.lɔ́b] 
 Rhymes: -aːb 
 Readings
 Classical reading ? 
 gulāb
 Dari reading ? 
506: Etymology tree
508- Proto-Indo-European *Hwerdʰ- der. ? 
509- Proto-Indo-Iranian *(H)wardʰ- 
510- Proto-Iranian *wardah 
511- Old Persian *vr̥dah 
512- Late Middle Persian gwl ( gul ) 
513- Persian گل 
515- Inherited from Late Middle Persian gwl ( gul , “ rose, flower ” ) .
517- Pronunciation
518- [ edit ] 
520- ( Classical Persian ) IPA ( key ) : /ˈɡul/ 
522- ( Dari, formal ) IPA ( key ) : [ɡʊl] 
524- ( Dari, formal ) IPA ( key ) : [ɡʊl] 
525- ( Kabuli ) IPA ( key ) : [ɡʊl] 
527- ( Hazaragi ) IPA ( key ) : [ɡul̥] 
529- ( Iran, formal ) IPA ( key ) : [ɡ̥ol̥] 
531- ( Tajik, formal ) IPA ( key ) : [ɡul] 
533- Rhymes: -ul 
535- Readings
775: Etymology tree
777- Proto-Indo-European *ǵʰeh₂- der. 
778- Proto-Germanic *gailō 
779- Proto-West Germanic *gailu 
780- Old English *gāl 
781- Middle English gol 
782- English goal bor. 
783- Persian گل 
785- Borrowed from English goal .
787- Pronunciation
788- [ edit ] 
790- ( Iran, formal ) IPA ( key ) : [ɡ̥ol̥] 
792- Readings
794- Iranian reading ? 
796- gol
798- Noun
799- [ edit ] 
801- Dari
803- گول 
805- Iranian Persian
1033: Etymology tree
1035- Proto-Indo-European *gʷel- 
1036- Sanskrit गल ( gala ) der. 
1037- Urdu گل 
1039- Derived from Sanskrit गल ( gala ) .
1041- Noun
1042- [ edit ] 
1044- گل • ( gal )  m ( Hindi spelling गल ) 
1046- throat 
1048- neck 
1050- hook
```


## [2026-10-17T00:03:59.491Z] AGENT

Now Arabic ward, Mo'in roz/vard, etymonline rose/julep, Sohrevard.


## [2026-10-17T00:04:02.884Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i 'borrowed\\|aramaic\\|iranian\\|persian' d73100561a698a25.txt | head -10 | cut -c1-400; for f in 8bc1a85f3a256b1c a5edfba72b118227; do echo == $f; grep -n 'فر\\.\\|گل\\|ع\\.\\|\\[' $f.txt | head -12 | cut -c1-300; done; grep -n -i 'rosa\\|rhodon\\|Iranian\\|Oscan\\|Etruscan' b92f4e0e8cff33c8.txt | head -8 | cut -c1-500; grep -n -i 'julab\\|gulab\\|rose' be31610a43bbe132.txt | head -5 | cut -c1-500; grep -n -i 'rose\\|red\\|zanjan\\|Suhraward\\|province' f7612a5b9a88ec2a.txt | head -10 | cut -c1-300"
}
```


### [2026-10-17T00:04:03.393Z] TOOL RESULT

```
Exit code 1
133: Persian 
135: Toggle Persian subsection 
256: From Proto-Semitic *warad- . Cognate with Hebrew יָרַד ( yārád , “ to go down ” ) , Aramaic ירד ( yreḏ , “ stream ” ) , Ge'ez ወረደ ( wärädä , “ fall down, go down, drain off, pour down ” ) , and Akkadian 𒉿𒊏𒁺𒌝 ( warādum , “ to go down to lower ground, to come ashore, to go downhill or downstream ” ) and Ugaritic 𐎊𐎗𐎄 ( yrd ) .
1447: As Aramaic וַרְדָּא ( wardā ) , ܘܪܕܐ ( wardā ) , Hebrew וֶרֶד ( wéreḏ ) , and Old Armenian վարդ ( vard ) and Ancient Greek ϝρόδον ( wródon ) , borrowed from a reflex of Proto-Iranian *wardah . Doublet of جُلّ ( jull ) .
1746: → Persian: ورد ( vard ) 
2336: Persian
2342: Borrowed from Arabic وَرْد ( ward ) , itself of Iranian origin and from the same etymon as native گل ( gol ) .
2347: ( Classical Persian ) IPA ( key ) : /ˈward/ 
2372: Iranian reading ? 
2396: Persian ورد 
(eval):1: = not found
```


## [2026-10-17T00:04:07.563Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 8bc1a85f3a256b1c a5edfba72b118227 b92f4e0e8cff33c8 be31610a43bbe132 f7612a5b9a88ec2a 219f00b82b74d2ce; do echo \"== $f $(wc -c < $f.txt)\"; done; grep -n 'رز\\|فر' 8bc1a85f3a256b1c.txt | head -8 | cut -c1-300; grep -n 'ورد' a5edfba72b118227.txt | head -5 | cut -c1-300; grep -n -i 'Greek\\|Iranian' b92f4e0e8cff33c8.txt | head -5| cut -c1-600; grep -n -i 'gulab\\|julab' be31610a43bbe132.txt | head -3| cut -c1-500; grep -n -i 'rose\\|Zanjan\\|Suhraward' f7612a5b9a88ec2a.txt | head -6 | cut -c1-300"
}
```


### [2026-10-17T00:04:07.945Z] TOOL RESULT

```
== 8bc1a85f3a256b1c 2698
== a5edfba72b118227 3542
== b92f4e0e8cff33c8 131
== be31610a43bbe132 132
== f7612a5b9a88ec2a 21823
== 219f00b82b74d2ce 80553
4:TITLE: معنی رز | واژه یاب
6:معنی رز | واژه یاب 
8: 26 فرهنگ 
15: رز
30: رز
31: فرهنگ انتشارات معین
33: رز
34: فرهنگ انتشارات معین
4:TITLE: معنی ورد | واژه یاب
6:معنی ورد | واژه یاب 
15: ورد
32: ورد
35: ورد
170: City in Zanjan province, Iran
174: {{Cite map |author=((OpenStreetMap contributors)) |url=https://www.openstreetmap.org/?mlat=36.074444&mlon=48.438333&zoom=15#map=15/36.07444/48.43833|website=[[OpenStreetMap]] |title=Sohrevard City, Khodabandeh Central District, Khodabandeh County, Zanjan Province, Iran|date=11 September 2024|ac
187: Province Zanjan 
197: Sohrevard ( Persian : سهرورد ) {{GEOnet3|-3766562}}</ref>"}},"i":0}}]}'> [ a ] is a city in the Central District of Khodabandeh County , Zanjan province, Iran , serving as the administrative center for Sohrevard Rural District . [ 6 ] The previous capital of the rural district was the village o
207: Medieval Muslim geographers described Sohrevard as a town in the province of Jibal , located south of Soltaniyeh on the road from Hamadan to Zanjan . [ 9 ] According to al-Istakhri , this route was the shortest route to get from Jibal to Adharbayjan and was the one usually used in peacetime; in
222: Sohrevard was the birthplace of the 12th-century Iranian philosopher, Shahab al-Din Suhrawardi , [ 12 ] the Persian Sufi Abu al-Najib Suhrawardi and his nephew Shahab al-Din Abu Hafs Umar Suhrawardi (a direct descendant of Islamic Khalifa Abū Bakr as-Ṣiddīq). [ citation needed ]
```


## [2026-10-17T00:04:11.222Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 28,45p 8bc1a85f3a256b1c.txt; sed -n 30,45p a5edfba72b118227.txt; cat b92f4e0e8cff33c8.txt; grep -n -i 'Etymology' -A4 219f00b82b74d2ce.txt | grep -i 'greek\\|rhod\\|Etruscan\\|Oscan' | head -5 | cut -c1-400"
}
```


### [2026-10-17T00:04:11.632Z] TOOL RESULT

```
 ۳ واژه 
 رز
 فرهنگ انتشارات معین
 (رَ) (اِ.) 1 - درخت انگور. 2 - انگور.
 رز
 فرهنگ انتشارات معین
 ( ~.) (اِ.) زهر هلاهل .
 رز
 فرهنگ انتشارات معین
 (رُ) [ فر. ] (اِ.) گل سرخ .

 جست‌وجوی مترادف

 ۸ واژه 
 تاک
 فرهنگ انتشارات معین
 [ په . ] (اِ.) درخت انگور.

 ۲ واژه 
 ورد
 فرهنگ انتشارات معین
 (و ) [ ع . ] (اِ.) 1 - ذکر، دعا. 2 - جزیی از قرآن که انسان هر روز و هر شب بخواند. ج . اوراد.
 ورد
 فرهنگ انتشارات معین
 (وَ) [ ع . ] (اِ.) گل ، گل سرخ .

 جست‌وجوی مترادف

 ۱۵ واژه 
 ذکر
 فرهنگ انتشارات معین
 (ذَ کَ) [ ع . ] (اِ.) 1 - نر، نرینه . ج . ذکور. 2 - آلت تناسلی مرد.
 تب
URL: https://www.etymonline.com/word/rose
FETCHED: 2026-10-17T00:03:49Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden1439- From Spanish rosa , from Latin rosa , probably from Ancient Greek ῥόδον ( rhódon ) .
2740- Probably derived from a variant of Ancient Greek ῥόδον ( rhódon ) , but some of the details remain mysterious. Possibly via another Italic language like Oscan , or alternatively via the Aeolic version of ῥοδέᾱ ( rhodéā , “ rose-bush ” ) , which would have been *ῥοζά ( *rhozá ) . [ 1 ] Compare rubus .
```


## [2026-10-17T00:04:14.925Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ROSE\\|^JULEP\\|^Rose\\b\\|^Julep' SKT.txt SKT_dli_revised.txt | head; grep -n -i 'julep' SKT.txt | head -3; grep -n -i 'rose, sb\\|ROSE, sb' SKT.txt | head"
}
```


### [2026-10-17T00:04:15.346Z] TOOL RESULT

```
SKT.txt:16209:Rose,  (L.-Gk.-Anib.)  A.  S.  Mr^.- L.  tosa ;  borrowed  from  Gk.  ^^ov,  a  rose (whence  a  form  ^/a*  —  rosa)\  ./EoUc ^/mSJ$o»'.— Arab.  UHirJ,  a  ro*e.  Der.  rhodo- dendron (Gk.  iivZpov,  a  Irec).  •*
SKT_dli_revised.txt:40840:Julep, a drink. (P\ — Span. — Pers.) P". 
SKT_dli_revised.txt:66375:Rose. (L. — Gk. — Armenian .) A.S rose.
```


## [2026-10-17T00:04:17.815Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 40840,40846p SKT_dli_revised.txt; sed -n 66375,66382p SKT_dli_revised.txt; grep -n -i 'julep' SKT.txt FSD_vol2.txt | head -4 | cut -c1-300; awk 'BEGIN{RS=\"\\f\"} /Julep, a drink|julep/{print \"SKT leaf\",NR-1}' SKT.txt | head -2"
}
```


### [2026-10-17T00:04:18.416Z] TOOL RESULT

```
Julep, a drink. (P\ — Span. — Pers.) P". 
julep. — Span, julcpe. — Vet's,, jtildb, julep, a 
sweet drink ; also gitldb, rose-water, also 
julep. — Pers. gul, a rose ; db, water. For 
Pers. gul, see Bose. Pers. db is cognate 
with Skt. ap-, water. 

Rose. (L. — Gk. — Armenian .) A.S rose. 

— L. rosa\ bouowed from Gk. a 

rose .whence a foim * ^o 5 ta > > ; 

iEolic ^pohov (foi ^^fpohov). — Armen. 
wardy a rose ; whence also Pers. gfil 
FSD_vol2.txt:65494:JuL,  abbr.  Julep;  Julian;  Julius: July.
FSD_vol2.txt:65496:Jn'lep,  1   ju'lep;  2   ju'lSp  (xin), n.  1.  A   drink  com  posed  usu- ally of  brandy  or  whisky,  sugar, cracked  ice,  and  some  flavor- ing, commonly  fresh  crushed g   r   e   e   ri  mint.  2.  A   subacid, mucilaginous,  sweetened  drink, often  used  as  a   vehic
```


## [2026-10-17T00:04:21.502Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /Rose,  \\(L.-Gk/{print \"leaf\",NR-1}' SKT.txt; grep -n 'Julep\\|JULEP' FSD_vol2.txt | head -2; sed -n 65496,65500p FSD_vol2.txt | grep -o '\\[[^]]*\\]' | head -3"
}
```


### [2026-10-17T00:04:21.900Z] TOOL RESULT

```
leaf 432
65494:JuL,  abbr.  Julep;  Julian;  Julius: July.
[<  L.  Juffurn,  tlon:  as,  fuU-;j«fced  apple.— juIccTul,  juIccTess,  a. yoke,  4- MAXILLART.]
[JuicT-er;  juic'i-est.]
```


## [2026-10-17T00:04:26.352Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'ROSE\\b\\|JULEP\\|rhodo' AHD_watkins1985.txt | head; sed -n 1165,1180p AHD_watkins1985.txt; grep -n -i 'wrdh\\|wr̥dh\\|rose' IEC.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:04:26.991Z] TOOL RESULT

```
<persisted-output>
Output too large (30.1KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bxdkmeu7g.txt

Preview (first 2KB):
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” wh
...
</persisted-output>
```


## [2026-10-17T00:04:29.506Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i '.\\{200\\}\\bROSE\\b.\\{200\\}' AHD_watkins1985.txt | head -5; grep -o -i '.\\{150\\}JULEP.\\{100\\}' AHD_watkins1985.txt | head; grep -o -i '.\\{100\\}wr̥dh.\\{100\\}\\|.\\{100\\}rose.\\{60\\}' IEC.txt | head -5"
}
```


### [2026-10-17T00:04:31.774Z] TOOL RESULT

```
n ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek ép
JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUP
Lat. cf. frustum beside frustáre, v. ‘shatter’; Olr. brus “fragment; gravel, grit; refuse; MHG cf. brosem ‘crumb’; OE brosnian ‘crumble, decay’; OCS brüsng, noti (1
being'); Br. bot, bod; Cor. bod, bos ‘dwelling’; W bod “being, existence; dwelling'; G Butte (“bud; rosehip', fr. *bhutón); ME budde ‘buď’; Li. bütas, butà ‘homeste
; deorfan, v. id.; ON djarf "bold'; dirfast, v. ‘to dare’; (o-gde in) Ir. doirbh ‘grievous, hard, morose’; Li. dárbas ‘work’; (z-gde in) Arm. darbin ‘smith’; Av. da
shka “lees of melted butter’; OCS droZdija, drož- dije ‘dregs’; Cz. droždí ‘yeast, barm, dregs’ . dhroseið ‘shout, rave’. Cf. dhres- Gk. throéó; Latv. draseju ‘yode
, as Gk.); Ir. cf. cocán ‘calyx, bud, poppy, topknot; Br. kok 'holly-berry; OE haga, MHG hage ‘haw; rosehip’; Norw. hegg, Sw. hägg (Cbird-cherry', fr. *kokió-); Big
```


## [2026-10-17T00:04:33.951Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o '.\\{10\\}wrod-.\\{300\\}' AHD_watkins1985.txt | head -5"
}
```


### [2026-10-17T00:04:34.374Z] TOOL RESULT

```
xed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive,
```


## [2026-10-17T00:04:36.499Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o '.\\{60\\}RHODO.\\{400\\}' AHD_watkins1985.txt | head -4; grep -o 'wrod-[^.]*\\. Rose.\\{400\\}\\|wrod-2.\\{400\\}' AHD_watkins1985.txt | head"
}
```


### [2026-10-17T00:04:37.512Z] TOOL RESULT

```
skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok
```


## [2026-10-17T00:04:39.698Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{80\\}[Rr]ose\\b.\\{300\\}' AHD_watkins1985.txt | grep -i 'wrod\\|wrd\\|rhodon\\|Iranian' | head"
}
```


### [2026-10-17T00:04:40.263Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:04:42.010Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '.\\{0,200\\}wrod-.\\{0,200\\}' AHD_watkins1985.txt | cut -c1-420"
}
```


### [2026-10-17T00:04:45.034Z] TOOL RESULT

```
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,200}
                       \___exceeds complexity limits
```


## [2026-10-17T00:04:46.969Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport re;t=open('AHD_watkins1985.txt').read()\nfor m in re.finditer(r'wrod-',t): print(repr(t[max(0,m.start()-150):m.start()+250]));print()\n\""
}
```


### [2026-10-17T00:04:47.438Z] TOOL RESULT

```
'o-. Man. Derivative of weie-?. 1. Germanic shortened from *wiraz becoming *weraz in: a. Old English wer, man: WEREWOLF, WERGELD; b. Germanic compound\nwrod-\n*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VI'

' round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS'

', to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:\nwrdd-\nROSE}, 3. Zero-grade form *wrd- in Iran'

'in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:\nwrdd-\nROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]\nwrod-. To root, gnaw. Germanic *wrét- in Old '

'od-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:\nwrdd-\nROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]\nwrod-. To root, gnaw. Germanic *wrét- in Old English wr6tan, to dig up: ROOT?. [Pok. 7. ver- 1163.]\nwrédh-. To gr'

'ffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:\nwrdd-\nROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]\nwrod-. To root, gnaw. Germanic *wrét- in Old English wr6tan, to dig up: ROOT?. [Pok. 7. ver- 1163.]\nwrédh-. To grow straight, upright. Suffixed zero-grade form *wrodh-wo- in Greek orthos, straight, correct, right: ORTHO-, ORTHOTICS; ANORTHITE. [In Po'

'ILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh-'

'er-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-\nRIB_ rebh-2\nRIBALD wer-3\nRICH reg-1 RICOTTA pekw-\nRID reudh-2\nRIDDLE!\nRIDDLE! ='

'RUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-\nRIB_ rebh-2\nRIBALD wer-3\nRICH reg-1 RICOTTA pekw-\nRID reudh-2\nRIDDLE!\nRIDDLE! = krei- RIDDLE'

'LL ret- ROLLMOPS mul- ROOD rét-\nROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reud'
```


## [2026-10-17T00:05:08.235Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /fr.OIran. \\*  wrda-/{print \"KLN leaf\",NR-1} /julep,  n.,  a  sweet  drink/{print \"julep leaf\",NR-1}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} /^8.58 ROSE|\\n8.58 ROSE/{print \"SYN leaf\",NR-1}' SYN.txt; awk 'BEGIN{RS=\"\\f\"} /927. fful/{print \"HRN leaf\",NR-1}' HRN.txt; awk 'BEGIN{RS=\"\\f\"} /gul \\[gwll N/{print \"PHD leaf\",NR-1}' PHD_mackenzie.txt;  awk 'BEGIN{RS=\"\\f\"} /^gul \\[gwl\\] flower 219/{print \"NYB leaf\",NR-1}' NYB_vol2_glossary.txt; awk 'BEGIN{RS=\"\\f\"} /varaSa-  m.  i/{print \"BRT leaf\",NR-1}' BRT.txt"
}
```


### [2026-10-17T00:05:08.922Z] TOOL RESULT

```
julep leaf 450
KLN leaf 722
SYN leaf 579
HRN leaf 227
PHD leaf 59
BRT leaf 753
```


## [2026-10-17T00:07:20.700Z] TOOL CALL #51: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-556.json",
 "content": "{\n  \"pdf_page\": 556,\n  \"book_page\": 526,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Wrdho, Wrod\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Wanderwort 'rose': Proto-Iranian *wr̥da- / *wardah (Wiktionary: PIE *Hwerdʰ- with a question mark); AHD bracketed root wrod- 'rose, not common Indo-European, of unknown origin'\",\n      \"note\": \"The rose words of Iranian (Av. varəδa-, Parth./Sogd. ward, MP/NP gul), Armenian vard, Aramaic wardā, Arabic ward, Greek rhódon (Aeolic bródon < *wródon) and Latin rosa really are one family, so the chart's grouping is right. They are not a regular common-IE inheritance, though. Klein derives OIran. *wr̥da- from IE *wrdho- 'thorn, bramble' (OE word 'bramble'), and Nourai follows him in the gloss 'thorn, flower'. Watkins/AHD puts wrod- 'rose' in brackets as 'not common Indo-European, of unknown origin'. Buck says the name 'does not rest upon inheritance from an IE form, but upon borrowing'. Wiktionary has the Greek word borrowed from Proto-Iranian *wardah, possibly from a pre-Greek or Thracian source instead. Pokorny 1959 has no entry for the rose word. The root box is acceptable as a label for the word family, but not as a securely reconstructed PIE root.\",\n      \"note_fa\": \"واژه‌های «گل/ورد/rhodon/rosa» به‌راستی از یک خانواده‌اند: اوستایی varəδa-، پارتی و سغدی ward، فارسی میانه و نو gul، ارمنی vard، آرامی wardā، عربی ward، یونانی rhódon (ائولی bródon) و لاتینی rosa. ولی ریشهٔ هندواروپایی آغازین *wrdho- «خار» که نورایی به پیروی از کلاین آورده، استوار نیست. واتکینز (فرهنگ امریکن هریتیج) این ریشه را میان قلاب و با عنوان «نه هندواروپایی مشترک، از خاستگاه ناشناخته» آورده است. باک نیز می‌گوید نام گل سرخ میراث هندواروپایی نیست و با کشت این گل وام گرفته و پراکنده شده است. پوکورنی هم مدخلی برای آن ندارد. پس گروه‌بندی نورایی درست است، ولی ریشهٔ هندواروپایی را تنها با احتیاط می‌توان پذیرفت. محتمل‌تر آن است که این واژه وام‌واژه‌ای ایرانی یا «واژهٔ سرگردان» باشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BF%A5%CF%8C%CE%B4%CE%BF%CE%BD\",\n        \"https://en.wiktionary.org/wiki/%DA%AF%D9%84\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:1357\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.33124 (leaf 722) s.v. rose: 'L. rosa, fr. Gk. rhodon, for *wrodon, fr. OIran. *wrda- (whence also Aram. warda, Arm. vard). OIran. *wrda- became gul in ModPers. ... initial w becomes g and -rd is changed to l ... OIran. *wrda-, rose, represents I.-E. *wrdho-, thorn, bramble, whence also OE. word, bramble'. This is exactly Nourai's root and gloss.\"},\n        {\"ref\": \"SYN:527\", \"status\": \"partial\", \"note\": \"SYN.txt l.13293, §8.58 ROSE: lists 'Av. varəδa-(?)'. Discussion: 'does not rest upon inheritance from an IE form, but upon borrowing ... spreading with the cultivation of the flower. Lat. rosa ... is itself a loanword fr. some dialect form of Grk. rhodon ... belongs further with Av. *varəδa- rose? (Barth. 1369), Arm. vard, NPers. gul, whether orig. an Iranian word, or all from some common unknown source.' Buck has the same word family but rejects an IE root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. [wrod-] (bracketed entry)\", \"stance\": \"partial\", \"note\": \"'[wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon ... 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa ... 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]'\"},\n        {\"src\": \"POK\", \"where\": \"POK_full.txt / POK_01-03\", \"stance\": \"silent\", \"note\": \"Searched for 'rose', 'Rose', 'rhod', 'wrod', 'rdh' lemmata and found no rose root. The only wrod-/wrad- entry is u̯(e)rād- 'root, branch' (p.1167), which is unrelated.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. III Wortregister\", \"stance\": \"silent\", \"note\": \"No index entry for Gk. rhodon or Lat. rosa that leads to an IE root (searched 'rose' and 'rhod').\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt\", \"stance\": \"silent\", \"note\": \"Searched 'wrdh', 'rose'. The only hits are other roots ('rosehip' under kok-), with no rose root.\"},\n        {\"src\": \"BRT\", \"where\": \"col. 1369 (BRT.txt l.22893, leaf 753)\", \"stance\": \"partial\", \"note\": \"'varəδa- m. 1) Mehren ... 2) Name einer Pflanze, vll. Rose ... Zum V. varəd- ... arm. LW. vard Rose; vgl. np. gul Rose'. Bartholomae attaches the word to the root vared- 'grow', not to IE 'thorn'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Iranian\",\n          \"words\": \"wrda, varedha; suxra-vard\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old Iranian *wr̥da- 'rose' is the reconstructed source of the whole Iranian set. Avestan varəδa- (Nourai's 'varedha') occurs once, in the Nirangistan (N. 97), as a plant name that Bartholomae translates only as 'perhaps rose', with intervocalic d spirantised to δ. The Iranian form is secure through Parthian/Sogdian ward, MP gul and the early loans into Armenian (vard) and Aramaic (wardā). 'suxra-vard' is not an attested Old Iranian form. It is Nourai's reconstruction of the place-name Sohravard/Sohrevard (*suxra- 'red' + ward 'rose'), and that etymology of the town name is folk-level and unproven. The town is also in Zanjan province (Khodabandeh county, on the old Hamadan–Zanjan road), not 'near Tehran'.\",\n          \"derivation_fa\": \"صورت ایرانی باستان *wr̥da- «گل سرخ» بازسازی‌شده و استوار است. گواهش پارتی و سغدی ward، فارسی میانه gul و وام‌واژه‌های ارمنی vard و آرامی wardā است. صورت اوستایی varəδa- تنها یک بار در نیرنگستان آمده و بارتولومه آن را نام گیاهی دانسته که «شاید گل سرخ» باشد. «suxra-vard» در هیچ متن ایرانی باستان نیامده و بازسازی نورایی برای نام «سهرورد» است. این ریشه‌شناسی نام شهر هم ثابت نشده است. سهرورد هم در استان زنجان (شهرستان خدابنده) است، نه نزدیک تهران. پس بخش اصلی ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84\",\n            \"https://en.wikipedia.org/wiki/Sohrevard\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1357\", \"status\": \"supports\", \"note\": \"s.v. rose: 'fr. OIran. *wrda- (whence also Aram. warda, Arm. vard)'.\"},\n            {\"ref\": \"BQT:1822\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:1822 (vol.3 pdf 619), Mo'in's footnote to گل: 'در اوراق مانوی (بپارتی) ward (گل سرخ). اوستا varəδa ... ارمنی vard ... پهلوی gul ... معرب «ورد»'. The footnote does not mention suxra-vard.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1369\", \"stance\": \"partial\", \"note\": \"'varəδa- ... 2) Name einer Pflanze, vll. Rose' (only 'perhaps'), with 'arm. LW. vard Rose; vgl. np. gul'.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II s.v. gul (NYB_vol2_glossary.txt l.1732)\", \"stance\": \"supports\", \"note\": \"'gul [gwl] flower — Av. (1369) varəδa-; Arm. lw. vard rose as Aram. (Syr. etc.) lw. wrd', Arab ward; MPrth wr[d] flower ..., NP gul rose, flower'.\"},\n            {\"src\": \"SYN\", \"where\": \"§8.58\", \"stance\": \"partial\", \"note\": \"'Av. varəδa-(?)' with a question mark.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"vardâ, vard, vart\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The real Middle Persian (Pahlavi) word is gul [gwl] 'flower, rose' (MacKenzie), from *wr̥da- by the two Persian sound changes initial w- > g(u)- and -rd- > -l-. 'vardâ/varta' is the Aramaic heterogram WRT'/WRD' (Aramaic wardā) written in Pahlavi texts and read gul (Horn: 'phlv. varta d.i. varda (PPGl.), gul (Bund.)'; Hübschmann: 'gul Blume, Rose Bdh., aber phl. vard in phl. aram. varta'). The native form ward with unchanged w and rd is Parthian (Manichaean wrd), not Persian. So the forms are attested in Pahlavi script, but as an Aramaic ideogram or a Parthian word, not as the spoken Middle Persian word. Nourai's 'vart' only reflects the heterogram spelling. It should not be confused with Pahlavi vart 'captive' (NYB), which is unrelated.\",\n          \"derivation_fa\": \"واژهٔ اصلی فارسی میانه (پهلوی) gul [gwl] «گل، گل سرخ» است. از *wr̥da- با دو دگرگونی آوایی ویژهٔ فارسی پدید آمده است: w- آغازی به g(u)- بدل شده و -rd- به -l-. «vardâ/varta» هزوارش آرامی WRD' (آرامی wardā) است که در متن‌های پهلوی نوشته و «gul» خوانده می‌شد (هرن و هوبشمان). صورت ward، با w و rd دست‌نخورده، پارتی (مانوی wrd) است نه پارسی. پس این صورت‌ها در خط پهلوی آمده‌اند ولی هزوارش یا پارتی‌اند. ادعای نورایی با این توضیح پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 38 s.v. gul (PHD_mackenzie.txt l.2602)\", \"stance\": \"partial\", \"note\": \"'gul [gwl] ... flower, rose'. MacKenzie has gul only and lists no native ward.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II s.v. gul; s.v. vart\", \"stance\": \"partial\", \"note\": \"'gul [gwl] flower ... Arm. lw. vard ... MPrth wr[d] flower'; 'vart [wlt'] captive' is a separate, unrelated word.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 927, p. 206-207\", \"stance\": \"supports\", \"note\": \"'927. gul Rose ... phlv. varta d. i. varda (PPGl.), gul (Bund.), vard in arm. arab. LW. vard'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 156 (§46, no. 18; HUB.txt l.5683)\", \"stance\": \"supports\", \"note\": \"'18) gul Blume, Rose Bdh. Gl. 225, aber phl. vard in phl. aram. varta, vgl. Horn Nr. 927, arm. vard'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"vard; sohrvard\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP vard وَرد 'rose' is real (Khāqāni's verse rhymes vard with mard). It does not continue Pahlavi directly, though: it is a loan from Arabic ward 'rose' (Mo'in tags it [ع.]). The Arabic word itself came, via Aramaic wardā, from an Iranian (Parthian-type) *ward, so this is a Persian → Aramaic/Arabic → Persian round trip, and the native reflex is gol. Sohravard/Sohrevard is the real town in Zanjan province, birthplace of Shehāb al-Din Sohravardi. Analysing it as sohr 'red' + vard 'rose' is possible as a Middle Iranian (Parthian-area) toponym, but no source confirms it, and the 'near Tehran' gloss is wrong.\",\n          \"derivation_fa\": \"«وَرد» در فارسی واژه‌ای رایج است (خاقانی آن را با «مرد» قافیه کرده). ولی مستقیم از پهلوی نیامده و معرّب است: از عربی ward «گل سرخ» (معین: [ع.]). عربی ward خود از راه آرامی wardā از ایرانی *ward (صورت پارتی) گرفته شده است. پس «ورد» واژه‌ای است که از ایرانی به آرامی و عربی رفته و دوباره به فارسی بازگشته است، و صورت بازماندهٔ اصیل همان «گل» است. «سهرورد» شهری در استان زنجان و زادگاه شیخ اشراق است. تحلیل آن به «سهر = سرخ» و «ورد = گل» شدنی است ولی منبعی آن را تأیید نمی‌کند، و «نزدیک تهران» نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%88%D8%B1%D8%AF\",\n            \"https://vajehyab.com/?q=%D9%88%D8%B1%D8%AF&d=moein\",\n            \"https://en.wikipedia.org/wiki/Sohrevard\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:5000\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (proper names, Sohravard) cannot be mapped to the page online. Mo'in s.v. ورد on vajehyab: '(وَ) [ ع . ] (اِ.) گل ، گل سرخ', which labels vard as an Arabic loan.\"},\n            {\"ref\": \"AHD:1550\", \"status\": \"partial\", \"note\": \"Watkins 1985 [wrod-]: '*wrd- in Iranian *wrd in Persian gul, rose: JULEP'. AHD has gul but not vard.\"},\n            {\"ref\": \"SYN:527\", \"status\": \"partial\", \"note\": \"§8.58 has 'NPers. gul' and does not list vard.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab s.v. ورد\", \"stance\": \"contradicts\", \"note\": \"'ورد (وَ) [ ع . ] (اِ.) گل ، گل سرخ'. Mo'in treats vard as Arabic, not as a direct Pahlavi heir.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 1822 footnote to گل\", \"stance\": \"partial\", \"note\": \"'... معرب «ورد» (بفتح اول)': Mo'in derives Arabic ward from the Iranian word, so NP vard came back through Arabic.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 927\", \"stance\": \"partial\", \"note\": \"'vard in arm. arab. LW. vard (sogar ar. muwarrad rosenfarbig)': vard is an Arabic/Armenian loan form.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt / ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Searched VARD, GUL, RHOD. The only hit is 'VARD (PAHLAVI)' in an unrelated index cluster (pdf p.108). There is no rose entry.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"val, vel, vol; valğŭneh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"val/vel/vol 'flower, blossom (esp. vine blossom)' is a real dialectal/lexicographical word: Borhan has ول 'شکوفه', and Bābā Ṭāher uses vol for gol ('ول و سنبل بهم آمیته دیری'). Semnani has vāla, which Horn also cites. valğune/vālğune 'rouge' is val + gūna 'colour', a doublet of golgune 'rose-coloured, rouge'. These are forms in which -rd- has already become -l- but initial w- has not yet become g-. That makes them a real intermediate stage, matching Farahvashi's sequence *varda > vāla > val/vel > gul. Nourai's note that the change happened 'in the early Arsacid era' comes from Farahvashi (IRN 129) and is not dated in standard handbooks. Modern scholarship treats -rd- > -l- and w- > g- as South-West Iranian (Persian) changes; Parthian itself kept ward. So the drawn chain, with Pahlavi 'vard' as the parent, is a simplification.\",\n          \"derivation_fa\": \"«وَل، وِل، وُل» به معنی «شکوفه، گل» در برهان قاطع (ول: شکوفه، به‌ویژه شکوفهٔ انگور) و در دوبیتی باباطاهر آمده است: «ول و سنبل بهم آمیته دیری». در گویش سمنانی صورت vāla هست. «ولغونه/والغونه» «غازه، سرخاب» هم از val و gūna «گونه، رنگ» ساخته شده و دوگانهٔ «گلگونه» است. در این صورت‌ها rd به l بدل شده ولی w آغازی هنوز g نشده است، پس مرحلهٔ میانی تحول *varda به gul‌اند (فره‌وشی، ایرانویج ۱۲۹). تاریخ‌گذاری این تحول به «اوایل دوران اشکانی» تنها سخن فره‌وشی است. پارتی خود ward را نگه داشته بود، پس این دگرگونی جنوب‌غربی (پارسی) است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2290\", \"status\": \"supports\", \"note\": \"ref_page.py BQT:2290 (vol.4 pdf 373): 'ول ... بفتح اول وسکون ثانی ...'. Mo'in's footnote: 'vol (ضم واو) در لهجه‌ها بمعنی گل آمده: مسلسل زلف بر رو ریته دیری / ول و سنبل بهم آمیته دیری ... بابا طاهر عریان همدانی «فرهنگ نظام». و بمعنی شکوفه نیز ...'.\"},\n            {\"ref\": \"IRN:129\", \"status\": \"supports\", \"note\": \"ref_page.py IRN:129 (pdf 140; image read, header '۱۲۹ سرگذشت واژهٔ گل'): 'تحول دیگر این واژه بنابر قاعدهٔ زبانشناسی ایرانی (rd=l) است و در اوایل دوران اشکانی صورت گرفته ... در گویش سمنانی varda به وال vāla ... بصورت ول vel ... واژهٔ val یا vol با gōna ... ولغونه و والغونه بمعنی غازه ... از val و vel تحول یافته بصورت گل gul'. This is the direct source of Nourai's node and note.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 927, p. 206\", \"stance\": \"supports\", \"note\": \"'Semn. vāle (vergl. np. vel Blüte des Weinstocks)'.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 1822\", \"stance\": \"supports\", \"note\": \"Same page: 'گلاگونه ... بمعنی غازه و گلگونه است و آن چیزی باشد سرخ که زنان بر روی مالند', which confirms the gūna 'rouge' compound type.\"},\n            {\"src\": \"PHD\", \"where\": \"s.v. gul\", \"stance\": \"partial\", \"note\": \"Has only gul and no l-form with w-, consistent with the change being complete in written MP.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"gol\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP gol (Classical gul) 'flower, rose' < MP gul [gwl] < Old Iranian *wr̥da-. Initial *w- before a rounded/syllabic r became g(u)- (cf. gorg < *wr̥ka-, Goštāsp < Vištāspa), and -rd- became -l- (cf. sāl < *sarda-, dil < *zr̥d-). The extra form golāb 'rose-water' is gol + āb 'water'. Hāfez's line pairs golāb and gol.\",\n          \"derivation_fa\": \"«گُل» در فارسی نو (دری gul) از فارسی میانهٔ gul [gwl] و آن از ایرانی باستان *wr̥da- است. w آغازی پیش از r هجایی به g(u) بدل شده، چنان‌که «گرگ» از *wr̥ka- و «گشتاسپ» از Vištāspa. -rd- هم به -l- بدل شده، چنان‌که «سال» از *sarda- و «دل» از *zr̥d-. «گلاب» از «گل» و «آب» ساخته شده است. ادعای نورایی درست است (هرن، هوبشمان، مکنزی، نیبرگ، کلاین، ویکی‌واژه).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84\",\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%A7%D8%A8\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:454\", \"status\": \"supports\", \"note\": \"Skeat (SKT.txt leaf 432; this local printing has the entry at p.~412, while Nourai's 454 is another printing) s.v. Rose: 'L. rosa; borrowed from Gk. rhodon ... Aeolic brodon'. SKT_dli_revised.txt l.66375: 'Armen. ward, a rose; whence also Pers. gul'.\"},\n            {\"ref\": \"AHD:129,1550\", \"status\": \"supports\", \"note\": \"Watkins 1985: 'ap-2. Water ... Iranian ap- in Persian ab, water: JULEP' and '[wrod-] ... *wrd- in Iranian *wrd in Persian gul, rose: JULEP'. These cover both elements of golāb.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 927\", \"stance\": \"supports\", \"note\": \"'927. gul Rose, arab. LW. julāb Rosenwasser'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 156 §45\", \"stance\": \"supports\", \"note\": \"'gul Rose aus *vṛd-?, vgl. arm. vard' among w > g examples (gurg, Gušasp).\"},\n            {\"src\": \"PHD\", \"where\": \"p. 38\", \"stance\": \"supports\", \"note\": \"'gul [gwl] flower, rose'.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II s.v. gul\", \"stance\": \"supports\", \"note\": \"'NP gul rose, flower'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. rose\", \"stance\": \"supports\", \"note\": \"'OIran. *wrda- became gul in ModPers. ... initial w becomes g and -rd is changed to l'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"julâb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic julāb جُلّاب 'rose-water; sweet syrup' is an Arabisation (muʿarrab) of Persian gulāb (MP *gul-āb) 'rose-water'. Arabic has no g, so Persian g- became j-. The word then passed into medieval medical Latin (julapium) and the Romance languages.\",\n          \"derivation_fa\": \"«جُلّاب» عربی معرّب «گلاب» فارسی است. عربی واج g ندارد و گ آغازی به ج بدل شده است. از عربی به لاتینی پزشکی سده‌های میانه (julapium) و سپس به زبان‌های رومی رسید. ادعای نورایی درست است (اصبغی، هرن، کلاین).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%AF%D9%84%D8%A7%D8%A8\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PLA:88\", \"status\": \"supports\", \"note\": \"PLA_pages.txt leaf 103 (= p.88): 'ğulāb: Rosenwasser, pers. gul, lat. julapium, it. julepe, sp. julep ... dtsch. Julep ... pers. > ar.'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 927\", \"stance\": \"supports\", \"note\": \"'arab. LW. julāb Rosenwasser ... Daraus sind bekanntlich entlehnt it. giulebbe, fr. julep, sp. julepe'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. julep (leaf 450)\", \"stance\": \"supports\", \"note\": \"'VAr. juleb, corresponding to classical Arab. julāb, fr. Pers. gulāb, rose water, julep, compounded of gul, rose, and āb, water'.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'جلاب' returned nothing (OCR).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"julep\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English julep (late 14th c., 'sweet syrup used as a vehicle for medicine') comes from Old French/Old Provençal julep, from Spanish julepe or medieval Latin julapium, from Arabic julāb, from Persian gulāb 'rose-water'. The American 'mint julep' sense is later (18th c.).\",\n          \"derivation_fa\": \"انگلیسی julep (سدهٔ چهاردهم، «شربت شیرینی که دارو را در آن می‌خوردند») از فرانسوی کهن و پرووانسی julep گرفته شده است. آن از اسپانیایی julepe یا لاتینی سده‌های میانه julapium، از عربی «جُلّاب» و در پایان از فارسی «گلاب» است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index: 'JULEP ap-2, wrod-', i.e. Persian gul + āb.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. julep\", \"stance\": \"supports\", \"note\": \"'F., fr. OProvenç. julep or fr. Sp. julepe, fr. VAr. juleb ... fr. Pers. gulāb'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT_dli_revised.txt l.40840\", \"stance\": \"supports\", \"note\": \"'Julep, a drink. (F. — Span. — Pers.) ... Span. julepe. — Pers. julāb, julep, a sweet drink; also gulāb, rose-water. — Pers. gul, a rose; āb, water'.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 2 s.v. julep (l.65496)\", \"stance\": \"partial\", \"note\": \"Entry present ('A drink composed usually of brandy or whisky, sugar ... mint'), but the etymology bracket is illegible in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"rhodon\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek rhódon 'rose' goes back to *wródon, with initial w- lost and rh- from *wr-. Aeolic has bródon (β- for *w-), and Mycenaean has wo-do-we 'rose-scented'. Most modern sources (Wiktionary, Buck, AHD) treat it as an early loan from an Eastern, most likely Iranian, *wr̥da-/*wardah, or from a pre-Greek (Thracian?) source. They do not treat it as a native inheritance from a PIE root, so the arrow from 'Wrdho' is better read as 'same Wanderwort' than as inheritance.\",\n          \"derivation_fa\": \"یونانی rhódon «گل سرخ» از *wródon است. w آغازی افتاده و rh از *wr آمده؛ در گویش ائولی bródon و در موکنایی wo-do-we «گلاب‌بو» دیده می‌شود. پژوهش امروزی (ویکی‌واژه، باک، واتکینز) آن را وام‌واژه‌ای کهن از ایرانی *wardah یا از زبانی پیش‌یونانی (شاید تراکیایی) می‌داند، نه میراث مستقیم هندواروپایی. پیوند آن با این خانواده درست است، ولی پیکان از «ریشهٔ هندواروپایی» را باید به معنای «همان واژهٔ سرگردان» گرفت.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BF%A5%CF%8C%CE%B4%CE%BF%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:527\", \"status\": \"partial\", \"note\": \"§8.58: 'Grk. rhodon belongs further with Av. *varəδa- ... whether orig. an Iranian word, or all from some common unknown source'. Buck has the same family but borrowing rather than inheritance.\"},\n            {\"ref\": \"KLN:1357\", \"status\": \"supports\", \"note\": \"'Gk. rhodon, rose, for *wrodon, fr. OIran. *wrda-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"[wrod-]\", \"stance\": \"partial\", \"note\": \"'Suffixed form *wrod-o- in Greek rhodon, rose', under a root marked 'not common Indo-European, of unknown origin'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 927\", \"stance\": \"supports\", \"note\": \"Ends the gul entry with 'gr. rhodon, lesb. brodon'.\"},\n            {\"src\": \"SKT\", \"where\": \"s.v. Rose\", \"stance\": \"supports\", \"note\": \"'Gk. rhodon ... Aeolic brodon'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"rosa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin rosa 'rose' is generally taken as a loan from Greek rhódon (or an Aeolic/dialectal *rhodja, *rhozá), but the -s- and the final -a are irregular. An Oscan or Etruscan intermediary is therefore assumed (Wiktionary: 'details remain mysterious'; AHD: 'perhaps via Etruscan'). The Greek → Latin edge is accepted, with the exact route uncertain.\",\n          \"derivation_fa\": \"لاتینی rosa را بیشتر پژوهشگران وام از یونانی rhódon (یا صورت گویشی *rhodja/*rhozá) می‌دانند. ولی s میانی و a پایانی با وام‌گیری مستقیم جور درنمی‌آید، و از این رو میانجی‌گری زبان اسکی یا اتروسکی را فرض می‌کنند. پیوند یونانی به لاتینی پذیرفته است و تنها راه دقیق آن روشن نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/rosa\",\n            \"https://en.wiktionary.org/wiki/%E1%BF%A5%CF%8C%CE%B4%CE%BF%CE%BD\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"§8.58\", \"stance\": \"supports\", \"note\": \"'Lat. rosa, the source of most of the European forms, is itself a loanword fr. some dialect form of Grk. rhodon ...'.\"},\n            {\"src\": \"AHD\", \"where\": \"[wrod-]\", \"stance\": \"supports\", \"note\": \"'Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. rose\", \"stance\": \"supports\", \"note\": \"'L. rosa, fr. Gk. rhodon'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through node for French rose (12th c.), inherited from Latin rosa. It is the intermediate source of Persian roz.\",\n          \"derivation_fa\": \"گرهٔ میانجی خالی، برای فرانسوی rose (سدهٔ دوازدهم) که بازماندهٔ لاتینی rosa است و فارسی «رُز» از آن گرفته شده. درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/rosa\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Empty node with no reference.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. rose\", \"stance\": \"supports\", \"note\": \"The entry traces English rose to L. rosa, the same Latin base as French rose.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab s.v. رز\", \"stance\": \"supports\", \"note\": \"'(رُ) [ فر. ] (اِ.) گل سرخ': Mo'in marks roz as French.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"roz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian roz رُز 'rose (esp. cultivated/garden rose)' is a modern (19th–20th c.) borrowing from French rose. It is distinct from native raz رَز 'vine' (Mo'in lists them as separate headwords). So Persian has the same Wanderwort three times: gol (inherited), vard (via Arabic) and roz (via French).\",\n          \"derivation_fa\": \"«رُز» در فارسی امروز وام‌واژه‌ای نو از فرانسوی rose است و با «رَز» به معنی «تاک» که فارسی اصیل است ربطی ندارد (معین این دو را جدا آورده). پس فارسی این واژهٔ سرگردان را سه بار دارد: «گل» (بازماندهٔ اصیل)، «ورد» (از راه عربی) و «رز» (از راه فرانسوی). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://vajehyab.com/?q=%D8%B1%D8%B2&d=moein\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1647\", \"status\": \"supports\", \"note\": \"Page not mappable online, but Mo'in's entry on vajehyab: 'رز (رُ) [ فر. ] (اِ.) گل سرخ', i.e. from French, as the chart says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab s.v. رز\", \"stance\": \"supports\", \"note\": \"Three headwords: 'رز (رَ) درخت انگور'; '... زهر هلاهل'; 'رز (رُ) [فر.] گل سرخ'.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"No entry for roz (Aryanpur covers inherited IE words only).\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"rose\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English rose comes from Old English rōse, an early loan from Latin rosa, reinforced in Middle English by Old French rose.\",\n          \"derivation_fa\": \"انگلیسی rose از انگلیسی کهن rōse است که وامی کهن از لاتینی rosa بود، و در انگلیسی میانه فرانسوی کهن rose آن را تقویت کرد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. rose\", \"stance\": \"supports\", \"note\": \"'rose, n. — ME., fr. OE., fr. L. rosa'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.16209 s.v. Rose\", \"stance\": \"supports\", \"note\": \"'Rose (L.-Gk.-Arab.) A. S. rose. — L. rosa; borrowed from Gk. rhodon'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Sogdian\",\n          \"words\": \"wrd\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian warδ 'rose' (written wrδ, Buddhist and Manichaean texts) comes from Old Iranian *wr̥da-/*warda-, with intervocalic/post-r d > δ as usual in Sogdian. Like Parthian ward, it keeps w- and rd unchanged, which shows that the gul development is specifically Persian. A derivative is wrδywn 'rose-coloured' (cf. NP golgun). The chart's 'wrd' is a simplified transcription of wrδ.\",\n          \"derivation_fa\": \"سغدی warδ (به خط wrδ) «گل سرخ» از ایرانی باستان *warda- است و d پس از r، چنان‌که در سغدی قاعده است، به δ بدل شده. سغدی مانند پارتی w و rd را نگه داشته است، و این نشان می‌دهد که تحول به «گل» ویژهٔ فارسی است. واژهٔ wrδywn «گلگون» هم از آن ساخته شده. «wrd» در جدول آوانویسی ساده‌شدهٔ wrδ است و ادعای نورایی درست است (قریب).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:411\", \"status\": \"supports\", \"note\": \"SOD_pages.txt l.33085 (page header '411'): '10149 wrδ ... warδ (wrd) < Av. varəδa; <*warda ... rose'. Entry 10141 has 'wrδywn ... rose-colour'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"no. 10149, p. 411\", \"stance\": \"supports\", \"note\": \"'warδ (wrd) © Av. varəδa; <*warda ... rose. GMS 207, 282, 526; BBB 574'.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II s.v. gul\", \"stance\": \"supports\", \"note\": \"Lists 'MPrth wr[d] flower' as the North-East-type cognate that keeps w- and -rd-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-17T00:07:20.747Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-556.json (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:07:24.811Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=data/verification/page-556.json; sed -i 's/\"p. 156 (§46, no. 18; HUB.txt l.5683)\"/\"p. 161 (leaf 171; HUB.txt l.5683)\"/; s/\"p. 156 §45\"/\"§45 (HUB.txt l.5512)\"/; s/MPrth wr\\[d\\] flower/MPrth wr (OCR; = wrd) flower/g' $f; python3 -m json.tool $f >/dev/null && python3 tools/verify_check.py 556"
}
```


### [2026-10-17T00:07:25.382Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'plausible': 6, 'confirmed': 7}
root verdicts: {'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 5, 'partial': 3}
books consulted: {'partial': 9, 'supports': 26, 'contradicts': 1, 'silent': 3} | by book: {'HRN': 6, 'KLN': 6, 'NYB': 4, 'PHD': 3, 'MON': 3, 'SKT': 3, 'SYN': 2, 'HUB': 2, 'BQT': 2, 'ARY': 2, 'AHD': 2, 'BRT': 1, 'AFM': 1, 'FSD': 1, 'SOD': 1}
```


## [2026-10-17T00:07:35.370Z] TOOL CALL #53: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-556.json`. `verify_check.py 556` passes with 0 PROBLEM lines and all 13/13 nodes verified.\n\n**Page 556** has one entry, the root \"Wrdho, Wrod\" ('rose').\n- **Root: plausible.** The word family is right: Iranian *wr̥da-, Avestan varəδa-, Middle Persian gul, Greek rhodon, Latin rosa. But it is a borrowed word that travelled between languages, not an inherited Indo-European root. Klein gives Nourai's Indo-European *wrdho- 'thorn'. Watkins' AHD appendix brackets wrod- as \"not common Indo-European, of unknown origin\", Buck says the name was borrowed rather than inherited, and Pokorny has no entry for it.\n- **Nodes:** 7 confirmed, 6 plausible, 0 disputed, 0 transcription_suspect.\n  - Confirmed: gol, julâb, julep, the empty French node, roz, rose, Sogdian wrd.\n  - Plausible:\n    - **#1 wrda, varedha; suxra-vard:** Bartholomae glosses Avestan varəδa- only as \"perhaps rose\". \"suxra-vard\" is Nourai's own reconstruction, not an attested form. The gloss \"town near Tehran\" is a factual error in the book: Sohrevard is in Zanjan province.\n    - **#2 vardâ, vard, vart (Pahlavi):** the spoken Middle Persian word was gul. \"varda/varta\" is an Aramaic ideogram written in Pahlavi texts (Horn, Hübschmann), and plain ward is Parthian.\n    - **#3 vard:** Persian vard came back from Arabic ward (Mo'in marks it [ع.]), not directly from Pahlavi. The \"sohr + vard\" analysis of the town name is unproven.\n    - **#4 val, vel, vol; valğŭneh:** the forms are real (Borhan, Bābā Tāher, Semnani vāla). The \"early Arsacid\" dating comes only from Farahvashi (Iranvij p. 129).\n    - **#8 rhodon and #9 rosa:** these are loans within the family, not inherited from the root. Greek probably borrowed rhodon from Iranian; Latin rosa came from Greek, perhaps through Oscan or Etruscan.\n\n**Extraction errors:** none found. The JSON matches the chart text, and no node needed a check of the printed page.\n\n**Gaps:**\n- The etymonline fetches failed with 403, so they are not cited; Klein and Skeat cover rose and julep instead.\n- Mo'in's page numbers (MON:5000, MON:1647) can't be mapped online, so I checked those entries through vajehyab.\n- Aryanpur has no rose entry.\n\n**Other files touched:** reference pages BQT:1822, BQT:2290 and IRN:129 were rendered and cached under `data/verification/sources/refs/ocr/`. The web pages I used were archived through `fetch_source.py`."
}
```


### [2026-10-17T00:07:35.860Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
