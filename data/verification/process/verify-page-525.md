# Verification process log — verify-page-525


## [2026-10-16T05:13:01.673Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 525 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-525.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-525.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-525.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 525` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.715Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.194Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.215Z] TOOL RESULT

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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-16T05:13:05.696Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-525.txt"
}
```


### [2026-10-16T05:13:05.712Z] TOOL RESULT

```
1	=== PDF page 525 (book page 495) ===
2	--- entry 0 ---
3	ROOT Wâ -> redirect to Eu 1
4	--- entry 1 ---
5	ROOT Wag -> redirect to Wegh
6	--- entry 2 ---
7	ROOT [Indo-European] Wag 2, Gwag, Gwâk
8	Gwĕguos : cry, quack, squeak, squeal
9	a cracking bird  (refs POK:1110; IEC:351,354)
10	#1 (parent #0) [Persian] refs=IEC:351,352,354; BQT:1057; MON:1742 | žâž «ژاژ» : worthless speech ; zâğ «زاغ» : crow ; zakîdan «زکیدن» : bluster, rage, talk to oneself in rage | extra: ژاژخا ، زکان ، ژکیدن
11	#2 (parent #0) [Sanskrit] refs=POK:1110 | vagnu : tone, call, cry
12	#3 (parent #0) [Greek] refs=IEC:351 | bazô : talk ; bagma : talking
13	#4 (parent #0) [Latin] refs=IEC:351 | vâgîre : scream ; vâgio : scream
14	--- entry 3 ---
15	ROOT [Indo-European] Wai : alas  (refs POK:1110)
16	#1 (parent #0) [Avestan] refs=POK:1110 | vayôi, âvôya : alas
17	  #2 (parent #1) [Persian] refs=BQT:2255 | vây «وای» : alas, woe
18	#3 (parent #0) [Germanic] refs=KLN:1749 | wai
19	  #4 (parent #3) [English] refs=None | woe
20	--- entry 4 ---
21	ROOT [Semitic] W.a`.m : to match, agree, pair up  (refs KLN:1609)
22	#1 (parent #0) [Arabic] refs=KLN:1609 | taw`am : twin child, accompanying
23	  #2 (parent #1) [Persian] refs=MON:1159 | tow`am «توأم» : together with, twin ; tow`amân «توأمان» : twins
24	#3 (parent #0) [Syriac] refs=KLN:1609 | tômâ : twin
25	  #4 (parent #3) [Greek] refs=KLN:1609 | tomas
26	    #5 (parent #4) [English] refs=KLN:1609 | Thomas, Tom
27	
```


## [2026-10-16T05:13:06.411Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-525.json"
}
```


### [2026-10-16T05:13:06.705Z] TOOL RESULT

```
1	{
2	  "pdf_page": 525,
3	  "book_page": 495,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wâ",
8	        "redirect": "Eu 1"
9	      },
10	      "nodes": []
11	    },
12	    {
13	      "root": {
14	        "name": "Wag",
15	        "redirect": "Wegh"
16	      },
17	      "nodes": []
18	    },
19	    {
20	      "root": {
21	        "name": "Wag 2, Gwag, Gwâk\nGwĕguos",
22	        "lang": "Indo-European",
23	        "refs": "POK:1110; IEC:351,354",
24	        "gloss": "cry, quack, squeak, squeal\na cracking bird"
25	      },
26	      "nodes": [
27	        {
28	          "id": 1,
29	          "parent": 0,
30	          "lang": "Persian",
31	          "refs": "IEC:351,352,354; BQT:1057; MON:1742",
32	          "words": [
33	            {"translit": "žâž", "gloss": "worthless speech", "script": "ژاژ"},
34	            {"translit": "zâğ", "gloss": "crow", "script": "زاغ"},
35	            {"translit": "zakîdan", "gloss": "bluster, rage, talk to oneself in rage", "script": "زکیدن"}
36	          ],
37	          "script_extra": "ژاژخا ، زکان ، ژکیدن",
38	          "note": null,
39	          "quote": {
40	            "text": "کسیکه ژاژ درآید به درگهش نشود - که چرب گویان آنجا شوند کند زبان",
41	            "poet": "Farrokhî"
42	          }
43	        },
44	        {
45	          "id": 2,
46	          "parent": 0,
47	          "lang": "Sanskrit",
48	          "refs": "POK:1110",
49	          "words": [
50	            {"translit": "vagnu", "gloss": "tone, call, cry", "script": null}
51	          ],
52	          "script_extra": null,
53	          "note": null,
54	          "quote": null
55	        },
56	        {
57	          "id": 3,
58	          "parent": 0,
59	          "lang": "Greek",
60	          "refs": "IEC:351",
61	          "words": [
62	            {"translit": "bazô", "gloss": "talk", "script": null},
63	            {"translit": "bagma", "gloss": "talking", "script": null}
64	          ],
65	          "script_extra": null,
66	          "note": null,
67	          "quote": null
68	        },
69	        {
70	          "id": 4,
71	          "parent": 0,
72	          "lang": "Latin",
73	          "refs": "IEC:351",
74	          "words": [
75	            {"translit": "vâgîre", "gloss": "scream", "script": null},
76	            {"translit": "vâgio", "gloss": "scream", "script": null}
77	          ],
78	          "script_extra": null,
79	          "note": null,
80	          "quote": null
81	        }
82	      ]
83	    },
84	    {
85	      "root": {
86	        "name": "Wai",
87	        "lang": "Indo-European",
88	        "refs": "POK:1110",
89	        "gloss": "alas"
90	      },
91	      "nodes": [
92	        {
93	          "id": 1,
94	          "parent": 0,
95	          "lang": "Avestan",
96	          "refs": "POK:1110",
97	          "words": [
98	            {"translit": "vayôi, âvôya", "gloss": "alas", "script": null}
99	          ],
100	          "script_extra": null,
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 2,
106	          "parent": 1,
107	          "lang": "Persian",
108	          "refs": "BQT:2255",
109	          "words": [
110	            {"translit": "vây", "gloss": "alas, woe", "script": "وای"}
111	          ],
112	          "script_extra": null,
113	          "note": null,
114	          "quote": null
115	        },
116	        {
117	          "id": 3,
118	          "parent": 0,
119	          "lang": "Germanic",
120	          "refs": "KLN:1749",
121	          "words": [
122	            {"translit": "wai", "gloss": null, "script": null}
123	          ],
124	          "script_extra": null,
125	          "note": null,
126	          "quote": null
127	        },
128	        {
129	          "id": 4,
130	          "parent": 3,
131	          "lang": "English",
132	          "refs": null,
133	          "words": [
134	            {"translit": "woe", "gloss": null, "script": null}
135	          ],
136	          "script_extra": null,
137	          "note": null,
138	          "quote": null
139	        }
140	      ]
141	    },
142	    {
143	      "root": {
144	        "name": "W.a`.m",
145	        "lang": "Semitic",
146	        "refs": "KLN:1609",
147	        "gloss": "to match, agree, pair up"
148	      },
149	      "nodes": [
150	        {
151	          "id": 1,
152	          "parent": 0,
153	          "lang": "Arabic",
154	          "refs": "KLN:1609",
155	          "words": [
156	            {"translit": "taw`am", "gloss": "twin child, accompanying", "script": null}
157	          ],
158	          "script_extra": null,
159	          "note": null,
160	          "quote": null
161	        },
162	        {
163	          "id": 2,
164	          "parent": 1,
165	          "lang": "Persian",
166	          "refs": "MON:1159",
167	          "words": [
168	            {"translit": "tow`am", "gloss": "together with, twin", "script": "توأم"},
169	            {"translit": "tow`amân", "gloss": "twins", "script": "توأمان"}
170	          ],
171	          "script_extra": null,
172	          "note": null,
173	          "quote": null
174	        },
175	        {
176	          "id": 3,
177	          "parent": 0,
178	          "lang": "Syriac",
179	          "refs": "KLN:1609",
180	          "words": [
181	            {"translit": "tômâ", "gloss": "twin", "script": null}
182	          ],
183	          "script_extra": null,
184	          "note": null,
185	          "quote": null
186	        },
187	        {
188	          "id": 4,
189	          "parent": 3,
190	          "lang": "Greek",
191	          "refs": "KLN:1609",
192	          "words": [
193	            {"translit": "tomas", "gloss": null, "script": null}
194	          ],
195	          "script_extra": null,
196	          "note": null,
197	          "quote": null
198	        },
199	        {
200	          "id": 5,
201	          "parent": 4,
202	          "lang": "English",
203	          "refs": "KLN:1609",
204	          "words": [
205	            {"translit": "Thomas, Tom", "gloss": null, "script": null}
206	          ],
207	          "script_extra": null,
208	          "note": null,
209	          "quote": null
210	        }
211	      ]
212	    }
213	  ]
214	}
215	
```


## [2026-10-16T05:13:15.268Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls page-52*.json; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','IEC','BQT','MON','KLN','WLD','AHD','BRT','HRN','HUB','SKT','ARY','FVQ','AFM','PLA','SYN']:\n  v=d.get(k,{}); print(k, v.get('kind'), v.get('local_file'), v.get('page_offset'), (v.get('lookup_hint') or '')[:150])\n\"",
 "description": "Inspect source matrix and refs index"
}
```


### [2026-10-16T05:13:15.658Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   50k sfmqrb 14 Oct 22:14  page-52.json
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
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
POK archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-ch
IEC archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
BQT archive_djvu+local_scan_ocr ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page s
MON website+archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] 
KLN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nour
WLD archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the 
AHD archive_djvu+website+archive_restricted /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word 
BRT archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special translite
HRN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak..
HUB archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the translite
SKT archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
ARY local_scan_ocr ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD 
FVQ archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'] printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
AFM archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'] 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba
PLA archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned v
SYN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the conc
```


## [2026-10-16T05:13:22.978Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'u̯ā̆g-\\|^u̯āg\\|wāg-\\|u̯ag-' POK_full.txt | head; grep -n -i 'u̯ai\\b\\|^u̯ai' POK_full.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==1110+8+1' POK_03.txt | head -5",
 "description": "Grep Pokorny for wag and wai"
}
```


### [2026-10-16T05:13:23.504Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:13:26.352Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'vagnú\\|vagnu\\|vāgio\\|vagio\\|vāgīre\\|vagire' POK_full.txt POK_03.txt | head; grep -n -i 'wehe\\|vayōi\\|vay[oō]i' POK_full.txt POK_03.txt| head",
 "description": "Grep Pokorny for cognates"
}
```


### [2026-10-16T05:13:26.790Z] TOOL RESULT

```
POK_03.txt:5001:Ai.  vagnu-  m.  ,Ton,  Ruf',  ved.  vagvand-  , lärmend',  vagvanü-  m.  QetOii*« lat.  vägiö,  -Ire  , schreie,  wimmere',  vägor,  -öris  m.  ^Widerhall'  (das  d  d^»! stufig;  von  einem  z'-St. "^uägi-s  ausgegangen);  lit.  vögrauti  ,wimmern  schreltn*
POK_full.txt:88556:Material: Old Indie vagnu-m. "sound, tone, shout, call', ved. vagvana- larmend', vagvanu- 
POK_03.txt:364:Mit  s- :  lat.  splrö,  -äre  ,blasen,  wehen,  hauchen,  atmen'  (*speis-),  spiritus, -üs  ,Hauch,  Atem,  Seele,  Geist';  spiräculum  ^Luftloch';
POK_03.txt:533:A.  perQ-  :pre:  gv.  nl(,i-TtQrj-f.ii,  *7rQrj^(jü  (Ttgifjao),  mor^aa)  ,(fache  an  =) zünde  an,  verbrenne;  blase;  spritze  aus',  Ttgr^öibv,  -ovog  i.  , entzündliche Geschwulst',  7tQ7]i.iaiv(ü  ,blase  heftig',  TCQrnioväu)  ,tobe',  ^Qr^arrjQ  ,Blitzstrahl, Sturmwind,  reißender  Strom';  slav.  *preieti  in  polu.  przec  ,sich  erhitzen, schmoren',  russ.  prejety  preth  , schwitzen,  sieden',  aksl.  para  , Rauch,  Dampft, (apr. ^ore  ,Brodem'  aus  poln.  para);  hitt.  paräi-  ,anfachen,  blasen,  wehen';
POK_03.txt:711:I.  pes-  ,blasen,  wehen'  (s.  auch  2.  pes-  ,Staub,  Sand').
POK_03.txt:712:Aisl.  fQnn  f.  ,Schneewehe,  Schneehaufe'  (*faznö),  -fenni  n.  ds. ;  als  ,im  Win- de wehender  Faden':  ah d. /aso  m.,fasa  f.  ^Faser,  Franse,  Saum',  sgs.fces(ri) n.  ,Franse',  engl,  feaze  ,Fasern';  aisl.  fqsull  m.  ,B^iid',  mnd.  vese{n),  Spreu, Faser,  Franse',  ndl.  vezel  ,Faden',  ahd.  fesa  ,Spreu,  Spelze',  nhd.  Fehse, dän.  ßcBser^  älter  f{j)es  ,Fasern',  ahd.  fasön  ^untersuchen'  (*zerfasern) ;
POK_03.txt:714:aksl.  'p^chyrh  ,bulla,  Blase',  'pachati  ,ventilare,  agitare',  russ.  pacÄnui^,  ^' ,wehen',  pdchnuh  ,duften,  riechenS  zapacA^  , Geruch,  Duft' usw. ;  russ.  pds,no  - ,Garnsträhne',  lett.  pudsm(i)s  ,Abteilung  zwischen  zwei  Endpunkten',  .soviel'" man  mit  zwei  Fingern  aus  der  Kunkel  Flachs  zieht';  6ech.-poln.  pochvQ  , ,Schwanz'  (, wedelnd'),  aksl.  o-pash  ds. ;  nasaliert  poln.  p^chnqc  ,anblasen,  J anwehen',  pqcJi,  p^ch  ,Witterung  (des  Hundes')  usw. ;  vielleicht  bulg.  "f; pasmina  ,Rasse'  (vgl.  ai.  tdntu-  ,Faden,  Faser,  Geschlechtsfaden,  Reih, der  Nachkommen,  Nachkommenschaft').
POK_03.txt:717:Ai.  pämm-,  pämsukd-  , Staub,  Sand',  av.  pqsnu-s  ds.;  ksl.  peshH  ,Sand'; vermutlich  als  ,der  wehende,  gewehte'  benannt  und  zu  1.  pes-  ,blasen'. WP.  II  68,  Trautmann  216  f.
POK_03.txt:795:Got.  fitan  ,gebärenS  vielleicht  zu  ags.  fitt  ,Streit',  engl  fit  ,Anfall  eiaei, Krankheit^  nwf ries.  ^<s  ,bissig';  mir.  idu,  Gen.  idan,  Nom.  PL  idain  ,GqJ burtswehen,  Schmerz';  die  mir.  Flexion  geht  auf  air.  ä-Flexion  zurück, wie  z.  B.  mir.  persu  ,Person^  auf  air.  persan]  der  air.  Nom.  Sg.  muß somit  Hdan  {*piduna)  gelautet  haben. WP.  II  70;  vgl.  Feist  155  f.
POK_03.txt:910:(3r.  'Ttveca  (Ttvsvaai)  , wehen,  keuchen,  atmen,  riechen*,  7Tvev(.ia  ,das iVehen,  Hauch,  Atem  usw/,  rtvori  ,das  Wehen,  Schnauben';  dazu  vielleicht auch  ftoiTtvto)  ,sich  rühren,  rege  sein'^,  trans.  ,sich  eifrig  womit  beschäf- tio-en',  Perf.  TtSTZvvad-ai  , geistig  rege,  verständig  sein',  jtvvTÖg'  eixcpqwv, fjfjjcpgtüv  Hes.,  dciiTtvvad-ai  , wieder  zum  Bewußtsein  kommen,  wenn  ,sich rühren,  rege,  bes.  geistig  rege'  aus  ,beim  Laufe  keuchen'  und  , atmen  = lebhaft  sein'  entwickelt  ist;
POK_03.txt:1037:pu-t-i  ai.  piipputa-  ,Anschwellung  an  Gaumen  und  Zahnfleisch';  gr. nvvvog  ,Steiß'  Hes.  {*put-snos)]  lat.  praepütium  ,Vorhaut'  (von  einem "^pütos  ,penis'.  vgl.  wruss.  potka  ds.);  vielleicht  ir.  uth  .Euter'  {*putus)', halt.  *putiö  , blase'  in  lit.  puciilj  pusti  ,blasen,  wehen',  reflex.  ,schwellen', puntü,  püsti  ,schwellen,  sich  aufblasen',  püsle  f.  .Blase,  Harnblase',  putlüs ,sich  blähend,  aufgeblasen,  stolz',  putä  .Schaumblase',  pütmenos  t  PI. , Geschwulst',  pari-putelis  .aufgeblasener  Mensch',  päpautas  ,Schwiele', auch  pautas  ,Ei,  Hode',  piisu,  püst  ,blasen.  wehen,  hauchen,  atmen', püsma  .Atemzug',  püte  ,Blase,  Blatter',  wohl  auch  lit.  puträ  .Grütze', lett.  putra  , Grütze,  Brei';  auf  Media:  lett.  pudurs,  puduris  ,Büschel, Haufe',  pudra  ,Haufe';  wruss.  potka  {*pztbka)  , männliches  Glied'.
POK_03.txt:3363:ai.  pr-?ti-  f.  ,Rücken'  usw.  (S.  813  Mitte)  und  prati-sthi-  »Widerstand'*  ;;"' gr.  l^aOTiq  ,aus  dem  Gewehe  vorstehender  Faden*  (*£?-ay-o"rtg),  xax  ^«  "• rriüXLv  , gegenüber'  (*avTr]v-ati-);  lit.  dim-stis  ,Hofraum,  Hof,  Gut'.
```


## [2026-10-16T05:13:29.078Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4995,5012p POK_03.txt; sed -n 88550,88580p POK_full.txt",
 "description": "Read Pokorny entries around wag/wai"
}
```


### [2026-10-16T05:13:29.492Z] TOOL RESULT

```
1110  ,
1.   uäg-  , Hohldeckel,  Scheide;  schützend  überdecken,  überstülpen'
Lat.  Vagina  f.  _,Scheide,  bes.  des  Schwertes';  halt.  *uäziö   stül*    ^i' vöziu,   vözti  , etwas    Hohles   über   etwas   decken,   stülpen^    lett    »a*« , Deckel  auflegen,  stülpen*^;  ^^  ^""^
andererseits  könnte  lat.  vägina  (vgl.  nhd.  Scheide  zu  scheiden)      *L einer  Wurzel  uag-  , spalten,   brechen''  gehören,   die  Frisk  (S    13^  * Uyvvi.Li  , zerbreche',   mit  Redupi.   und   Ablaut   Iwyrj  (<  *J^i-J^(ay^\    o^t*!^ gegen  den  Wind',  falls  eigentl.   ,das  Sichbrechen  des  Windes*    <iytuU , Bruch,  steiler  Abhang'  und  im  tochar.  wäk-  ,sich  spalten',  Kaus   .m^W^ unterscheiden',  iväJcäm  n.  »Besonderheit,  Vorzug'  finden  will.  f^^^
WP.  I  214,  WH.  II  725,  Frisk  13,  Trautmann  343.  '  f
3.  uäg-  , schreien';  vielleicht  von  einer  Schallwurzel  uä-.
Ai.  vagnu-  m.  ,Ton,  Ruf',  ved.  vagvand-  , lärmend',  vagvanü-  m.  QetOii*« lat.  vägiö,  -Ire  , schreie,  wimmere',  vägor,  -öris  m.  ^Widerhall'  (das  d  d^»! stufig;  von  einem  z'-St. "^uägi-s  ausgegangen);  lit.  vögrauti  ,wimmern  schreltn*
WF.  I  214 f.,  WH.  II  725 f.;  dazu  gehört  das  folgende:
v^gh-,  suägh-  , schreien,  schallen'.
Gr.  '^xVy  ^or.  dxä  f.  , Schall,  Geräusch',  ^x^,  -ovg  f.  ,Schall,  Ton,  Wid«^ hall',  ^xos  (ark.  J^axog)  m.  ds.,  ijxeco  ,schalle,  töne',  ^x^Va,  ^x^'^S  »hell  ttfnttd' öva-Tjxrjg  ^widrig  tönend',  ablaut.  äiicpiaxvXa  , ringsum  schreiend',  laxf^  (Vi/ä* Xö),  iaY.xv  ^-  »Geschrei',  läxo)  (*/z/ax^)>  ^'orxf'w  ,schreie',  avlaxog  ,zu8aini&«ft« schreiend'  (*dJ^iJ^axog)]  **^/
vielleicht  mit  beweglichem  s-  hierher:
got.  ga-swögjarij  swögatjan  ,seufzen*,  aisl.  sdgr  m.  ,Lärm'  (*«t^ö^'-),  illt swögan  ,tönen,  sausen,  brüllen',  sweg,  swxg  m.  ,Lärm,  Klang',  as.  $wi^^(m , rauschen',  holl.  zwoegen  , stöhnen';  tiefstufig  wohl  aisl.  svagla  ,plätschtni*t arn-sügr  ,das  Rauschen  des  Adlerflugs';
lit.  svageti  ,tönen',  lett.  svadzet  ,rasseln';
für  isl.  sukka  ,lärmen',  daneben  svakke,  ist  jedoch  Vergleich  mit  BOfWt dial.  seykia  ,bellen'  und  lit.  saugti  , eigenartig  singen',  alit.  sugti  ,betikly winseln',  lett.  sudzet  ,klagen',  sükstities  , seufzen'  (daneben  ^-Formen  wit  Bti saukill  durch  Einfluß  von  kaukti  ,heulen',  §aükti  , schreien')  untar  M|^» *s(e)ug-  möglich;  got.  sioegnjan  ,frohlocken'  könnte  auf  Grund  von  yif»» swög-j  swag-  als  Schall  wort  ins  Leben  gerufen  worden  sein;  das  -Wf-  » aisl.  sukka  ist  intensivierend.
WP.  I  214  f.,  WH.  II  725  f.
uai  Interjektion  ,wehe!',  uai-lo-s  ,Wolf'.
Av.  vayöi,  avöi,  ävöya   ,Avehe'!  (yoya-  ,Wehruf'):  arm.  vay  ,Weh^
IUI
Root / lemma: uag-2 

Meaning: to cry 

Note: perhaps from an onomatopoeic word ua- 

Material: Old Indie vagnu-m. "sound, tone, shout, call', ved. vagvana- larmend', vagvanu- 

m. " din, noise '; Latin vagid, -/?e"cry, wimmere', vagor, -or/sm. "Widerhall' (das a 

lengthened grade, from a /-stem *^5^/-s derive ); Lithuanian vograut/" whimper, cry'. 

References: WP. I 214 f., WH. II 725 f.; 



See also: in addition belongs das following: uagh-, suagh- 
Page(s):1110 



Root / lemma: uai-, uT- 

Meaning: weak, miserable 

Material: Old Indie vayati, vayate^\N\rd faint, languid, exhausted', abhi-vata-^ sick ' {vata- 

"dry, arid'), vaya- ' tired '; 

cymr. gwae/ 'armWch, low' {*uai-lo-)\ acymr. guoilaut, cymr. gwaelodeic. " residuum ';
```


## [2026-10-16T05:13:35.434Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5012,5020p POK_03.txt | cut -c1-900; grep -n 'Interjection\\|\"woe' POK_full.txt | head",
 "description": "Read Pokorny wai continuation"
}
```


### [2026-10-16T05:13:35.822Z] TOOL RESULT

```
IUI
glück'  (v-  statt  g-  aus  idg.  u-  durch  nebenherlaufende  NeuscLöpfung); ähnlicb  gr.  öd  (wie  lat.  vah!)  uad  seit  alexandrinischer  Zeit  ovd,  ovä,  oiai^ ^crr.  ßai  (Neuschöpfungen);  alb.  vaj  ,Leid,  Klage';
lat.  vae;  mir.  /äe^  cymr.  gioae  ,weh!';  mit  einem  vielleicht  mit  lett.  valdi zusammenhängenden  cZ(7i).Suffix  vermutlich  mir.  fäed,  föid  ,Schrei,  Ton', gyinr.  gwaedd  ^clamor,  eiulatus';
hierher  als  , Heuler':  arm.  gaü,  gall.  *uai-lo-s  im  PN  Vailo,  Vailico,  ahrit. Gen.  Vailathi,  air.  Faildn,  m\v.fdel,fdel-chü  ,Wolf*  =  cymr.  gweil-gi , Ozean';
got.  wai,  aisl.  vei,  vä,  ahd.  as.  toe;  ags.  wä  ,wehe!',  got.  wai-nei  ,wenn doch!'  (eig.  ,wehe,  daß  nicht!')  in  Kompositis  des  schlechten,  fehlerhaften 2ustandes,  z.  B.  got.  wajamerjan  ,lästern',  loaidedja  , Übeltäter',  aisl.  veill locker,  schwach'  (^wai-haüa-),  vWla^  väla,  vela,  veila  ,jammern';  ags.  lo^lan, neinigen'  (,*krank  machen',  von  einem  *iva-häl  ==  aisl.  veill)-,  ahd.  tvewo^ icewa  ,Wehe,  Schmerz,  Leid',  as.  we,  Gen.  toewes,  ags.  wäwa,  wea,  aisl.  väj ug  ds.;,  finn.  (Lw.J  vaiva  ,Plage,  Elend';  ahd.  weinön  ,weinen',  ags.  zvänian, aisl.  veina  jjammern',  wovon  wohl  als  »bejammernswert'  got.  loainags  , elend, unglücklich',  ahd.  icenag  , elend,  unglücklich',  mhd,  auch  , schwach,  klein, gering',  nhd.  ivenig]
lett.  vai  ,wehe,  ach*,  vaijät  trans.  ,wehe  tun',  ivaXdet  , wehklagen,  jam- mern', väidi  PI.  jWehklage,  Jammer,  Not'  (s.  oben);  serb.  väj  ,wehe!'  ist Neuschöpfung.
WP.  I  212  f.,  WH.  II  724,  Trautmann  338.
lii-,  ui-  , schwach,  elend'.
Ai.  väyatij  väyate  ,wird  matt,  erschöpft',  abhi-väta-  ,krank'  (väta-  ,trocken, dürr'),  väyü-  ,müde';
```


## [2026-10-16T05:13:39.857Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vagio\\|vāgiō\\|vägiö\\|bazo\\|bagma\\|zag\\b\\|zāγ\\|zāgh\\|zhazh\\|zak-' IEC.txt | head -30",
 "description": "Grep Mann IEC for cognates"
}
```


### [2026-10-16T05:13:40.276Z] TOOL RESULT

```
5472:guheguh-, assimilated radical, form of dhe- guho, q. v. Cf. WP I, 849 Per. cf. zuyal, *zayal *'embers' beside gazam ‘sting’; Oss. dzagü “hot poultice’ beside qäzäl ‘charred matter’; Alb. cf. zegël, zegth ‘gadfly’; OCS Zego, Zeët ‘kindle, burn’; Zegü, žega “heat; Cz. cf. Zehadlo ‘sting’; Pol. zegadto ‘red-hot iron’; Cz. Zehlice ‘flatiron’; Slovene žežel ‘poker’. (An R-gde w. i-basis seems to be present in Gk. thibrós ‘roasted, hot, ten- der”, cf. OCz. Zhu, Zéci ‘kindle’ and OCS Z1Ze- nije ‘burning, inflammation’. Gk. type *guhï- gu-)
5570:$agholos ($aghilo-, $aghlo-) (1) ‘spike, point’. Variant: gaghoros. Cf. &agh-. WP I, 570 Oss. zágàl ‘nail’; OHG kegil ‘peg’: MHG. Du. kegel ‘cone; skittle, icicle’. Variants in Oss. dzagur ‘chisel’: Li. Ziogras ‘stake’, fr. a type *saghuro-, *&aghro-; Icel. kógur, n. fringe"; Li. Zágaras ‘twig’; pl. ‘brushwood’; Zagre ‘plow- share’ beside Zagáre, id.
5739:Skt. jihva; Av. hizu, hizva, hizvá-; OPer. izāva, hazvàn; Pehi. huzvan, hizvan: Per. zabàn; Oss. àvzag, dim. type
5918:ĉuhuos (£houos) “shout, call, appeal, impre- cation’. Cf. &uhuo, guhon- Skt. hū, adj. ‘calling’; juhū, jihva ‘tongue’; ` havah 'invocation' in Vedic; ‘sacrifice’ in Skt.; Av. zavō ‘call’; hizu, -áh-, n. and hizva, f. ‘tongue’; Ober, (alleged) izáva, id.; Oss. äv- zag, dim. type, id.; Per. cf. hazvan, zaban, id.; Arm. cf. n-zovK, gp. n-zovic (curse: Skt. ni- havah ‘invocation’; ni-hvaye invoke); Gk. Hes. cf. oló-phus or ol-óphus ‘mourning’; olo- phudnós, adj.; Mir cf. guth, pl. gothanna (“+ voice”. See next); Go. gaunópus ‘plaint’; OE géanobp, id.; MHG cf. guft ‘shout’; OCS züvü (cal, and com. Sl.); Cz. cf. ná-zev 'appella- tion’; Li. Zavai (charms, spells’; Zavüs *be- witching’
5921:$haghus (or ĉhoghus) ‘cub, chick’. Cf. &hiia- ghos Skt. jahuh; Av. jaZus; Arm. dzag, u-st., id.
8090:krksos, ios ‘oblique, awry’. WP II, 590. Var- iant krsos, see krs- (1) Gk. (ambig.) kársios ('oblique”. See krs-); Cz. & Slovak krch, krchy, adj. lefthanded, awk- ward’; Slovene cf. kíSiti ‘transgress; Blg. krás, m. “stile, crossing'; krăxvam, v “lay ath- wart; kráskam ‘go zigzag; krása, kărša (2) ‘wind, zigzag’; cf. krăšnjak ‘backbone’; Li. (?) kiršas ‘peevish, cross’; OPr. kirša “across; Li. cf. kìrkšnys, mpl. ‘lumbar region’; Latv. cirksnis, id. (but cf. krkin-) (the semantics are echoed in Alb. kryqza ‘lumbar region’ in relation to kryq, Lat. LW ‘cross’). An isophone arises in Skt. krsah ‘lean, poor?
9937:Inquos, ios, à, io “bent, turned; bend, turn, twist". Cf. lenquo, lonqueió Cz. leč, gs. -i, -e, f. ‘noose, snare’; Li. linkà ‘direction’; linke, f. ‘bend, twist’; liñkis, io, m. id. and ‘detour, bend in river’; linkstu, inf. linkti, intr. ‘bend’; Latv. līks, adj. ‘bent’; licis ‘bend in river, bay, inlet; cf. līku locu 'zig- zag
18086:suir- (1) (suirð, ið) “swing, sway, rush, whirl, brandish’. Onomat, See next Oss. cf. xerí, s. ‘swing, seesaw’; Lat. surið, ire, v. ‘be in heat — of males’; W chwyr, m. ‘dash, rush’; LG schwiren, v. ‘gallivant’; Du. zwieren, v. ‘tack, zigzag; veer’; G (expressive
```


## [2026-10-16T05:13:45.061Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 189 190 191 192; do echo \"=== leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -n -i 'gu.g\\|guāk\\|guak\\|guog\\|zāg\\|zag\\|ba[zg]\\|cry\\|croak\\|squeak' | head -20; done",
 "description": "Locate Mann p.351-354 entries"
}
```


### [2026-10-16T05:13:45.420Z] TOOL RESULT

```
=== leaf 189
8:ghiró, ið (expr: ghirr-) ‘scream, screech, caw? Per. (ambig.) giristan ‘cry’; girye, adj. ^weep- ing’; Arm. redup. gr-gram ‘caw, cackle, cluck’, fr. *ghir-ghir-); cf. W. Arm. kre (gre), s. ‘crane’; Alb. cf. n-gjirrem ‘be hoarse, croak’; lat. hir- rið, -ire ‘growl, yelp’; cf. hir-undo ‘swallow’; G girren ‘coo’; LG girren ‘entice; sing’. (A variant of type *&hir- occurs in Latv. Zirins 'sea swallow'. For Li. giriü, -ti, see gur-, gurtos)
=== leaf 190
=== leaf 191
28:ghnagho, io (1) “gnash, gnaw’; (2) ‘neigh, mutter, nag' Gk. cf. kanásso ‘gurgle’ beside kanakhé “clash; gnashing of teeth'; OHG. OE gnagan 'gnaw'; ON.Sw. gnaga, id
=== leaf 192
```


## [2026-10-16T05:13:52.684Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'b[aá]z[oō]\\|b[aá]gma\\|v[aā]g[ií]re\\|zàg\\|zāy\\|žāž\\|zhāzh\\|zakidan\\|zag ‘crow\\|‘crow' IEC.txt | head -20",
 "description": "Grep Mann for Greek and Persian words"
}
```


### [2026-10-16T05:13:53.133Z] TOOL RESULT

```
929:bobaio ‘prate’. Cf. baba (1) and next Gk. babázo; LLat. babare (both ambig.)
930:bobodió ‘prate; drivel Gk. babázo; Br. babaza ‘twaddle; slobber
1090:bhak-, bhakolos ‘compact; lump’. Cf. bhakos, bhaK-, bhaks- Gk. cf. óm-phax, -phakos “bunch of sour grapes’, phákelos ‘bunch’; Alb. bake *pot- belly’, bákull ‘tubby’; Lat. (fr. Celt.?) bacci- num: basin (see Dauzat: bassin); Ir. baicle, baclach ‘crowd’; Br. bagol ‘hale, hearty’; W cf. bagad “cluster, crowd", bagwy ‘clump’; Srb. cf. bokast ‘humped’?
1514:bhorda, iə (0-gde variant of bherdà, q.v.) ‘with young, pregnant. Illyr. bardia; Alb. barsé; Lat. forda; Umb. furfað (for *furfaf: Lat. fordās “in lamb’. Cf. Umb. mefiaí: mediae); MHG cf. barzen ‘swell, be full; Swiss barzen, id.; Barz ‘crowd’: Alb. m-bars ffecundate'
1527:bhorm- (bhormos, à, is, io) “burden; bearer, holder, container’. Cf. bhero Gk. phormós "basket, corn-measure'; Alb. barrë “load; Go. barms (i-st.); OHG OS barm ‘Jap’; OE bearm ‘lap; possession’; G (uml.) Berme (‘ramp of bulwark’. LW in Fr. berme, OFr. barme); ON cf. barmtog “haul-rope. (Isophonic forms, of uncertain kinship, are the following: Gk. phormís ‘faggot; Alb. barmë “inner bark’; Ger. Barm, Barmen ‘crowd, pack’; Barmen, Bärme ‘barm, yeast’; ON barmr ‘brim’; barmi ‘brother’; Ukr. brama sic ‘gate’). WP II, 164
1956:bhür-, is, à, om (1) ‘pile, mass, crowd’ Skt. bhürih *mass'; Av. büiri, n. id.; Gk. cf. la-phüron ‘plunder’; ge-phüra ‘mound, bridge’; Li. būrys, io ‘crowd, flock; W (*-u-) cf. bwr ‘embankment
2472:drongos, å ‘mass, company, tribe, settle- ment’. Cf. WP I, 860 Skt. drangah, -a ‘town’; Ir. drong ‘company, tribe, people’; Gallo-Lat. drungus ‘crowd’; Gaul. drungos ‘mass’; OBr. drogn (sic) ‘company’. (LWs in OCS drogarí ‘member of a troop’ fr. Med. Gk. drouggários fr. LLat. drungarius)
2761:dhelbho ‘dig, gouge’. Cf. dholbh-. WP I, 866 OHG MHG télben; OE delfan; Du. delven; (o-gde in) MHG dalpen (sic!) “dig, delve’; R pro-dolbit ‘gouge’ beside Cz. dlabu, ati, id.; cf. OPr. dalptan ‘chisel’; (z-gde in) OCS dlübo, dlübsti hollow out, gouge’ beside Cz. dloubu, at ‘dig’. Of uncertain connexion is Li. delba, dálba ‘crowbar’. Here also belong OCS (z- gde) dlübokü, Srb. dubok, Big. dlábok ‘deep’
3107:dhro£hos, à ‘turn; going; wheel". Cf. dhregho : Gk. trókhos ‘course’; trokhós *wheel'; MIr. droch *millwhee?'; OE drag ‘crowd, tumult’; OHG traga, MHG trage *bearer, carrier, ve- hicle, holder’. Isophonic, and here only if Go. (and com. Gmc.) vb. dragan, pf. *drog can be equated with Gk. trókhos: trokháo (Iliad)); E dray (ME id.) reflects the R drógi ‘dray, hearse’, droga ‘carriage shaft" only if the latter is a Gmc. LW. Preobr. untenable qua ‘shaker’
3185:dhr£h- (2), dhrghos ‘rough, coarse, insolent, boorish’. Cf. dhrágh- (2) Oss. dárzàg (rough, raw’, fr. *dhrghàkos, dim.); Gk. cf. bá-trakhos, m. (frog, lit. *croak- hoarse’, fr. *gua-^); Icel. durgur ‘boor’; Cz. drzý ‘insolent’; OCS drüzü “bold?
3328:dhüros, à “piercing; piercer; stab, hole’. Cf. dhurð (1) Skt. cf. dhur (2) “tip of pole, spike-head'; dhurah, à ‘pole, linch-pin'; Arm. dur, gs dro "tool, chisel, gimlet'; Lat. cf. (?) fuscina Char. poon’, if fr. *dhur-skin-); R dyrà ‘hole’; Li. dürà ‘crowbar; breech’; düris, io “stab, stitch’; Latv. cf. düréjs ‘piercer’; dūre ( fis". Seman- tics of Lat. pugnus: punctum)
3418:Av. dvar(eimi), v. ‘rush’; Gk. thoüros “rush- ing’; Ir. duar ‘crowd’; cf. also Skt. a-dhvaráh (a religious ceremony); Sw. däre "Tool dhuoros “entrance, court. WP I, 871. Cf. dhuer-, dhur- Lat. (ambig.) forus *hatchway'; forum *mar- ket; OCS dvorü (and com. Sl.) ‘court, yard’; Li. dváras (farm. Perh. SI. LW) dhuos- *drooping, ailing; spirit, exhalation, expiry’. Cf. dhues-, dhus- Skt. cf. (ambig.) dhvasrah *withered"; MIr. dássaim *madden'; EME cf. dwas-light *will- o"-the-wisp'; Sw. dåse (“sluggard”, cf. E dial. dozy, fr. Scand.); dásig ‘sleepy’; Li. dvásas, dvasià ‘spirit’; dvasus ‘ailing, pining (dhuriə, a zero-formula to dhuer-, dhuor-, dhur- ‘door’. etc.) WP I, 870 Gk. thairós singularized: ‘hinge of door
3644:epi (pi) "on, by, at, near. WP I, 122 Skt. Av. ápi; Oss. fe-, fi-, px; Arm. h- (j-) as in h-arnem (rise: Gk. ep-órnümi, -órnu- mai; h-awraj ‘stepfather’: Gk. epi-pátor, id.); beside ev, cj. "and: Lyc. epi (ambig. “after”); Myc. & Gk. en Lat. cf. -pe in quip-pe, nem-pe, sae-pe; Umb. (?) ie-pi ‘thither’; Olr. cf. fí-ad 'in front of; OW i-ad ‘crown of
4269:graik- ‘crow, caw?’ , Lat. (?) Graecus (‘Greek’, from their dark hair?); LG krei, kreih, wf. and kreien, kreigen ‘crow’; OE cra ‘croak, caw’. See next
4270:grāið ‘croak, caw’. Cf. grakso and WP I, 592. See grán- Alb. gróhem, mp. ‘hum, buzz; OHG cf. chronan ‘coo; twaddle; boast; Du. kreunen *moan'; E to croon (see below: *gràn-); OCS grajo, inf. grajati ‘caw’; graj ‘song’; Srb. grajim, grajati ‘croak’, graja, f. id.; Slovene graja ‘scolding’; Li. gróju, gróti (/caw; play’, intr. of an instrument). Cf. (variant) OHG kräien, MHG kræjen; OE crāwen, v. ‘crow’
4842:ghort- ‘assembly, mass, crowd’ Skt. ghatah ‘crowd, troop’; Lat. (ambig.) co- hors, gs -hortis ((2) “assembly; company, troop’. A cpd. as Skt. sam-hrtih ‘assemblage’)
5096:guaduå ‘chatter; a chattering bird’ Oss. cf. qäza (‘waterfowl’, fr. *guadio?); Alb. gadé (‘heron’, beside gaté and gac, id.); Ir. badhbh ‘crow’; G cf. quasseln ‘chatter’
5101:guag- (2), guāg- ‘quack, squeak, squeal’ Per. cf. žāž ‘twaddle’; Oss. cf. zågin, pp. zagd ‘say’; Arm. cf. kakan, a-st. ‘clamour, lament’; Gk. bázō ‘talk’, bágma ‘talking’; cf. babáx *prattler'; Alb. cf. gagac, adj. ‘stammering’; ON kvaka ‘chirp’; G quaken ‘moan, complain’; Du. kwaken ‘quack, croak’; Li. (ambig.) gagiu, eti (*quack', see gag-). Long vowel in Lat. vā- gire, v. ‘scream’; Slovene gágam, Blg. gagam ‘cackle’; Latv. gāgāju, id. and cf. Li. gógšiu, gókšiu, eti ‘sob’; gókčioju (2) ‘squeaľ
5114:guágos, à (variant: gueg-) “a croaking bird". See guag- (2). (A possible variant is of type *guüguo-) Alb. cf. gogés ‘woodpigeon’: R. Blg. gàga "e, derduck'; (alleged) Latvian gaga ‘duck’. Cf. variant *gueg- in Per. zay ‘crow’; Alb. zog ‘bird’
5141:gueguos, io “a croaking bird'. Variant of guag- (2) (guaguo-), q.v. Per. zày ‘crow, raven’; Alb. zog ‘bird’; cf. (*-e- in) Li. gege, f. ‘cuckoo’; OCz. ZeZ-hule, id. beside Li. Latv. dim. gegužē, dzeguze, id.
```


## [2026-10-16T05:14:09.106Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^woe,\\|^Woe,\\|^Thomas\\|^twin,' KLN_1966.txt | head; ",
 "description": "Locate Klein entries"
}
```


### [2026-10-16T05:14:09.428Z] TOOL RESULT

```
39088:Thomas,  masc.  PN.  —  Eccles.  L.,  fr.  Gk.  0co[i.5<;, lit.  ‘twin’,  fr.  Syr.  tomd,  ‘twin’,  which  is  rel.  to Aram.  t6dma,  Heb.  tldm,  Akkad,  tuamu,  ta'- umu,  Arab,  tau'am,  ‘twin’.  All  these  words  are prob.  derivatives  of  the  Semitic  base  w-a-m,  ‘to tally’.  Cp.  Arab,  wa'ama,  ‘it  tallied’.  In  keeping with  the  original  meaning  of  the  name,  Thomas is  three  times  referred  to  in  John’s  Gospel  as 6  Xsy6(zevoi;  At8o(j.o<;  (Thomas,  called  ‘theTwin’).
```


## [2026-10-16T05:14:12.321Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^woe\\b\\|^wo,\\|^woe ' KLN_1966.txt KLN_1971.txt | head; grep -n -i '^WOE\\|^THOMAS' SKT.txt | head; grep -n -i 'wai\\b.*woe\\|woe.*wai' KLN_1966.txt | head",
 "description": "Locate woe in Klein and Skeat"
}
```


### [2026-10-16T05:14:12.965Z] TOOL RESULT

```
KLN_1971.txt:267949:wo, inteij. — Archaic var. of woe. 
KLN_1971.txt:267987:woe, also wo, n. — ME. wa, wo, fr. OE. wd, ‘evil, 
KLN_1971.txt:267999:woe’, fr. wo, ‘woe’ (see prec. word), and begon ,
```


## [2026-10-16T05:14:15.716Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 267987,267998p KLN_1971.txt; grep -n -i 'WOE\\b' SKT.txt | head -3; grep -n 'vayōi\\|vayōi\\|vayöi\\|vayoi\\|āvōya\\|avoya\\|äväya' BRT.txt | head",
 "description": "Read Klein woe and grep Bartholomae"
}
```


### [2026-10-16T05:14:16.095Z] TOOL RESULT

```
woe, also wo, n. — ME. wa, wo, fr. OE. wd, ‘evil, 
suffering; woe’, rel. to OS., OFris., OHG., 
MHG. we, G. weh, MDu., Du. wee, ON. vei, 
va?, Goth, wai, from the I.-E. imitative base 
*wai-, ‘voe\ whence also OI. uve, Avestic vayor, 
Gk. 6dc, L. vae , Lith., Lett, wai, Mir. fde, W. 
gwae, ‘woe’. Arm. vay, ‘woe; misfortune’. Cp. 
wail and the first element in wellaway. 
Derivatives: woe-ful , adj., woe-ful-ly, adv., woe- 
ful- ness, n. 

woebegone, adj. — ME. wo begon, lit. ‘beset with 
2708:•  j.  aevö.däta-  Adj.  (fem.  °t,7-)  'einzig-,  "der  ich.,  (sie),  solang  als  ich  kann  und allcingeschaffen',  vom  Urrind*':  matikahe  vermag,  lehienwill.."V,2(V.4; — atvislaota gaoci^irahe  giuscct  'taya  giuüa  poum.sar)-  ]  aojai  (sd.)  . .  arthaca  yavai  (sd.)  . ,  taväca ouy.i  Yt7.o;  —  gaem  'iaAe  ..  pouru.-'Uitica  V-jO.  11;  4S- 9;  —  ..*smvayöil yezi sarp'-.ahe  tirunö  S.  2.  I2(?).  \iste  {yai)  n5it*i$ieO{%%^hl.)ttSit  asavamm
4441:•  j.  an-ä'st9r«tay-  f. 'Sichnicht  versündigen. Nichtgeraten  in  den  Zustand  der  Sündig- keit': *°t5  (LS.)  *pascaSa  avä  ya  any.r (gä'^ä)  srävay^it  "ohne  sich  zu  versün- digen ')  kann  er  alsdann  die  andern  ( Gä%<ls) au&agen"  N.  46;  — y^  *upsissil  nsit  7>inasli ^'t5  *pas^aSa''>  srävayöit  "wenn  er  {Bans-
4794:gehen':  m3  apaOna  *paourv3vayöil  {d.  i. paourva,  sd,  -^avaySif^^  Vr,  22.  a.  S.
7390:—  3)  Vjjl.  Fü.  zu  avöi,  vayöi.
10442:fravartis  agarbäyatä  "Fr.  wurde  gefangen  i genommen"  Bh.  2. 13.  E  3)  'etwas  weg- 1 nehmen  von— (Abi.)':  g}urvaya  Äipälai'e. sävar»  Y.  r).  28.  4)  'einen  Anteil  be- ! kommen  von  — '  (Gen.):  tnä  hl  mairyö'. giurvayöit  "nicht  soll  davon  was  be- kommen , ."  Yt.  8. 59;  —  yezi  se  mairys gfurvay.V  Yt.Äöo;  —  mizdahe  .  .  g>r)W- 1 ytiti  yS  girswyaUe  VyL  JO  (?).  5)  'i^-
11058:sävayöit  V.  Ä  75;  Aj.  13;  —  ß-aca  si/a vTca  tumanha  V.2. 10;  — fraca  äitiaiwica vazaite  Yt  jo.  118;  —  pairica  dadimahi äca  va^ayamahT  Y.4.1;  —  aiwica  vaiio- yänte  frai'a  yazantt  Yt.  10. 1 20;  —  yä  .  . zrasca  dat  apica  aotSl  Yt.  p.  26;  —  mrjz- ystäcä  it  aAmäi  fralä  vatryitä  Tt  aäbyd yH,.  Y.3^.f>\ — tarn  yazäi  :£'äil  ttämSnIs pairihl  jasSi  vantä  Y.  57.  22.  II)  bei der  Verbindung  von  mehr  als  zwei Gliedern«'  steht  cä  1)  beim  letzten;  ß)  im Aw. ;  i)  die  Glieder  sind  nominal;  a)  sie folgen  sich  unmittelbar:  usa  arSmpi^wa xsapscl  Y.  44-  5 ',  —  mananha  ux&ilis f^ao'kanais^a  Y.^3.2)  —  sa>rqm  kaeyqm karafnqmca  Y.g.  18;  —  voku  manat3hä xsa'im  asacä  Y, jj.  10;  —  ■vatihlul  ma- nanhs  maxdä   aiahyjcä  Y.30. 10;  53.  3;
13113:yahmat  haca  Jräkwirisal  näfs  airyanqm °Hyunqm  ^r^m  airyanqm  'hyunqm  Yt. '^■^7)  —  ifar^Rö  .  .  yat  asti  airyanqm 'Ayunqm  Ytip.  56;  V. /^.  39;  —  iava/ftn :^arpnd  'hrähr^m  airyanqm  "AyunamYl-ig. 69;/?.  10; —  avavat  kavaSm  3^ar>ns yaha yat  iöa  anairym  °Ahus  hakat  usäi  us.frs- vayöit  (sd.)  Yl.  ip.  6  8 ;  —  taurvayeiti  anairya *'/iAävS(3isA'P.)Yt.iS.2;  —  airaityanqm tat  °Ayunqm  Vf/y^rai  uzjasaiH  N.(iS;  — aiioitaradyJ  haca  'nhubyö  Yt  i'j.  14;  — mi>r)m  .  .  yim  yazmte  daiAkupatayS  .  . aniar»  -iiihu  (AD.)  papr^täne  Yt.  10.  8; r_5.  49;  —  hasaaräis  (näml.  asH  mihrS) aiitary  °Ryu  (AD.)  Yt.  /o.  117;  —  yd  .  . karafanö  urapayeintl  (sd.)  yacä  xrata *Ju£>sc/a'irä  "Ayunqm  Y.4^'.io;  —  säsia 'rthSui  äaähupailii  *äxsta  isimnS  'lihave amtm  is^mnS  tanuye  YtJÖ^.  19;  —  sSsta 'itißaus  hams^ia%rö  Yt  13.  r8,  69,  75.  50; — fraiimatcltl!  'Xyunqm  Yt  13.  95;  *lo.  18; —  nöit  me..  ährava  . .  'iiifiava  (LS,)  earät Y.p,  34;  —  Siihqm  'hyunqm  yä  anyä rajSit  Y.ig.  18;  —  bawrSil paiti  'tJihaove Yti.ag.  a)  GS.  mit  GS.  des  Landes- namens  zur  Bezeichnung  der  Gebürtigkeit bei  EN.:  parlatgava  dazgrS^ava  apa- jTjVavi  (sd.)  'iähfus'  Ytrj.i2j;  127;  — ^rüJ  atv5jar3(^  fyultahe  tanyehe  tanyayä •tViÄÄ/ Yl  jy.  125;  125';  —  s,  noch tnzavant-  daitiksus  EN.  a)  bes.  im Gegensatz  zu  Haus,  Gemeine  und  Gau***; a)  im  gAiw.:  *S  sl  dimSnsm  vTs)m  v3 söihnrrt  vä 'Ayäm  vä  adaj  du^iäcd(sd.) .. Y.jt.  18;  —  yP  Auäänus  d^manahyä  xla- %r?m  iiSi^rahyS  vä  'AySus  vä  .  .fi-ada'iiäi (sd.)  asppmaia  Y.Jl.  16;  —  ga  JrSnKis' (sd.)  /tfiiraAyä  vä  'AySus  vä  Y.4ß.^; —  ähnlich:  patri  jfaSSuf  airyamanascä dadaiii  (sd.)  tiSil  ma  xsnäus  yä  v^rvsSnä (sd.)  ..  naida  'hy3u!  ..  sästärB  (sd.)  Y.46. 1.  b)    im  jAw.:    */ratainitm   .  .  yä
18697:srz.)  wer.."  Y.44.4;  3"*'; — is  urva'iä (sd.)  tpUamai  saraiuHräi  nä  mazdä  Y. 5/.  11;  —  kS  möi  paiSiii  ks  tnS  na  "i^rStä vistd . .  azää  {iA.)  Y.30.  i;  —  ataf  ahmäi .  .  üiä  (Sp.  134  o.)  ankaitl  .  .  yi . .  vandayaita  (sd.)  Y.50.3;  —  a^ yS  rna nä  trtanxlaiti  attyida  (sA)  ttvS  . .  Y.5/. 10;  —  at  yasßm  rtö'it  nä  is^mnS  äyst. (Sp.  150  Q.)  .  .  hs5  .  .  \.46.6;  —  yi  1/ ahmai  ?r?:ux'jä  {%A^  nä  däitl  '^.44.  19; —  aat  yd  na  hli  fräyazaite ..ahmäi .,  Yt 'JSi;  'S,  152;  —  Mä  tfm  urvaijm  .  . fräyavayöis  .  .  aom  nar>m  daitlm  y5  nä . .  frayatät  (sd.)  Yt  /.  24 ;  —  y3  . .  kv5 nä  */rasrBiäyäi  (sA.)  ifTf^Tvö  \ . 4ß.  i y, — /ivö  ma  n  a  sravä  tnörmdat  (sd.)  yS  ,  . Y._^2. 10;  —  a/  hv5  var^Aius  vahyä  (sd.) nä  aibJ.jamyät  yS  ..  Y.^^j.  3;  —  hvS  tat na  ahmai  dasdi(^^.  715  u.)  Y.5/.  19;  — hicä  nä  ßüma  nHaaharatü  hs  aiwyä- xsayatü  Y.5Ä4;  —  yezica  ma  hau  nä ava  snaHita  (sd.)  .  .  aJnavät  P.  2/j  — nai'a  paicaaa  *hau  *«J'^  .  .  isaäa  .  . apasütHt  (sd.)  P.  23;  —  aisS  nä  yS yaoidä'hryS  V.  g.  39,  40,  42,  ip.  31,  Vd. *?,  10,  V.  5.  41,  4.  49  (wo  naröy-,  — h'at  hS  nä  atthuyäite  (sd.)  cvat  hö na  alayäti  hat  ahmäi  naire  miidam aahatyl  .  .  A.4.^i.;  6',  V.Ä81,  p.  39', 44,  Y.Ö2. 1,  Yl/o.  i37£3;  —  yesi^  hö nä  paitiMncSit  yS  nöi}  apivatäite  damaya sva, "wenn einer.,,  der.."  V.^. 47;  —  taEca narSg3rpo5Ji3r3lasca{iA.)..'^.j.7^;  24;  — yasia  mi  aS^m  narpm  .  .paili  utiärayat sva.  "und  wer  ihn  .  ."  V.iS.  10; — paiti- tjm  ahe  nari yavaiea  ..  V.^.ai;  —  ndtt zT  ahmt  paiti  nairi  .  .  rSna  (sd.)  .  .  V. 7.  5»;  —  anätartta  a^byS  nprtbyö  . . yöi  .  .  Yt  13.  30;  —  hauca  *anayä  narä (GD.)  vohu  man3  jäg)r)bustare  arfhat yS ..  V.  4. 48.  B)  Ohne  Attribut  steht 'ein  Mann'  im  Sinn  von  'einer,  Jemand'; insbesondere  hat  der  NS.  na  in  der  Stellung der  Enklitika  häufig  die  Bedeutung  unsres 'raa.ii'-.yB  nar»m  anduIa{zA.)  sna'iajainti V.4.  »6;  18,  ai ;  —  äfs  nanm  jainti  vä V.5.  8;  8f.3;  — yB  *naire"^  aoxte  Jrä im  «Ä  (sd.)  "wer  zu  einem  sagt :  . ."  F. 4A;  —  na  tat  (Sp.  630U.)  paraJri^yeiti V.  5.  i;  a,  5;  —  mit  der  Negation  'nie- mand': nüit  spsJ>3ntS  .  .  nasui  nar?m nsil  *ästarayäti  V.  5.  3,  a)  NS.  na  in
20410:•  j.  manizujitay-'*  i)  f.  -?-:  drvatqm datvayoinanqm  'dm  mafyanqm  V.  ig,  36, 29,  4i*>.  i)  Adj,— ?-:  il'afsata  ma^a- kär>hil  ..mfrizu.jva^hO  ..'jUayS^xVi.io.^Z.
21773:mq'^nm  ..  maraüa  V.^.  45; — y  tavqti  .ahunava^&^ca  .,  srOvayeiti  *anästfntff alte  mtadayasna  yi  ..  tütuxsva  {sA.;\pasiatta  ava  yä  anya  gähä  sravayoit  N. nämL  niäaiiiJia)  y*  nSit  tavqn  3?a.stairii\  46;  50.
```


## [2026-10-16T05:14:19.939Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'avöi\\|avōi\\|vayöi Interj\\|Interj' BRT.txt | head -20",
 "description": "Grep Bartholomae for interjection"
}
```


### [2026-10-16T05:14:20.273Z] TOOL RESULT

```
2278:Gramm.:  Grammatik er(mill eilung,  angäbe). gramm.:  grammatisch. Ga.:  GuiaratiBbersetzung. Hi:  Handschrift;  s.  NA.  ProL  IIL HaploL:  Haplologie. haploL:  haplologisch. Hds.:  Handschrift bervorheb.:  hervorhebend. Hsg.,  hsg.:  Heransgeber,  herausgegeben. I.  (in  IS.,  ID.,  IP.):  Intlmmenlal(i5). I.  (in  zSIA.  nsw-):  Imperativ(us). idg.;  indogermanisch. Imp.:  Imperativ(ns). (Dat)  incomm.:  (Dalirus)  iocomroodi. Ind.i  Indikativ(us). ind, :  indisch. indekl.:  indeklinabel Inf.:  Infinitiv(uB). Inkoh.:  Inkohativ{um> inkoh. :  inkoh  ativ(i  seh). inibes.:  insbesondre, lostr.:  Initnimental(is). Int.  (Intens.):  lnten«i»(nm). Interj. :  Interjektion. inteiTOg.  1  interrogBti¥(us). intrans.:  intransitiv, ir.,  iran.:  iranisch.
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2784:in-',  mit  Inf.:   gavöi  ..  fraliyamahl  ra-\  f'''';,  T.^"''  ,''^'"''''' ''"  ^'- "'■?);<?  .-^jj^if"'
3459:•  j.  a-]^ae§ah-,  g.  a-dvae§ah-  Adj.  'der keine  Feindseligkeit  ausübt,  kein  Leid  antuf : n^mS  voAn  ahavTm  °spm  (ASn.) "  Vr.  21. 3, Vt.//.2j  —  nBif  sanjä  (sd.)  "Ä  (NSm.)  •> gavöi  Y.2fj.3.
5193:•  g.  avöi  Inteij.  'wehe!',  als  SubsL:  asifyj affhlu^  177'°  ari/ial  apsmim  "denen  wird Wehe  werden  am  letzten  Ende  des  Lebens" V.45-3-
5619:'raAe  paiti  iamgnöfm'W.ig.^^i^y, —  'raAe\»].  'arSan- m.  EN.  eines  iranischen  Fürsten gtwaya  . .  yat  ahmya  äalva  kandvannti  ausder^ai'ix)'djTiastie,EnkelsdesÄijW(7/a'': "..wo  die  Ä  zusammenkommen"  V.J.  7.   -{■awa^»»    'srum  Yti^.71;  —  Aavöis  'Ins
6875:2g.  6,  33.6,  II,  51.  15,  53.  i):  y}  sivim 'rS  mazda  Jiä..  Y.j:^.ii;2Ä'.5;  —  spmtim at  %'wil  mazdä  m}nghl{sA.)  "rä  Y.  43.  5; 2g.  T,  5'.  16;  —  sp>ntS.t?mo  ..  mazdä  °rö Y.45.S;  —  mazda  sai^ärJi^A^  mairisiö.. kvS  vleirsisd.)  'r3'>  V.25.4;  —  hätä-maräm (sd.)  'rä  . .  mazdä  Y.  32.  6 ;  —  yaslqm tu  °rä  irixl»m  mazdä  vagdiitö  ahl  Y._y2. 7;  —  ai  S  (sd.)  vaocat  -rö  mazda  vtdva vq/äf  (sd.)  Y.  25.  6;  —  aiiiyS  mazda  'rS .  .  paiti.mraot  Y.^2.  2;  —  tvSm  mazdä °rä  frS  mä  sTsä  .  .  *vaocaiihi  Y.  28.  11; 4S-  ^  >  —  anhsttl  (sd.)  akya  paourvJm *yqm  mSi  vJdva  (sd.)  mazda  vaocat  'rö '^'■45-V>  —  tat  %w<i  pinsä  (sd.)  »nl mSi  vaocä  'rä  .  ,  azJm  täÜ  "iwä  fraxsnt (sd.)  avämX  masdä  .  .  vupanam  dätJnm \.44~T,  1-4,8-11,  14-18,'^/.  14,  J4- 15;  —  °rä  yaübys  mazdä  "hwöi  vasyäl damä  Y.44.11;  —  sdr  «7  mazdä  'rä vanhsus  /radaxitä  (sd.)  majianhB  Y.jj. 1 7 ;  34-  13;  —  yehya  . .  vakisUm  . .  valdä mazdä  'rff  Y.  51.2a;  31.3;  —  yJ  viHnaot dä%imcä  (sd.)  aää'^?mca  dangrä  mantu aM  mazdä  'rö  Y.  46. 17;  2S.  10;  —  ustä aAmäi  yahmäi  ultä  (sd.)  kakmäicii  *vasS xiayqs  mazda  däyät'rö\. 43.1  •,32.16;  — yS  afimJnT(sd.)  matda  srävT  °rö  Y.  45. 10"*;  —  tä^ä  x/a^rä  mazdä  dqmis  °rS Y.  45.  7 ;  —  voAb  xia%r»m  manaahä mazdä  dadät  'rS  Y.5J.  ai;  31.  zi,  34.  i, 47.  I ;  —  at  mazdä  taibyS  xi'a%r?m  voAli mananhä  *vSivTdaitl  aübyo  sastl{sA.)  °ril.. Y._jo.  8;  46'.  12;  —  at  hsi  mazda  ahüm (sd.)  dadät  'rB  V.^tf'ij;  —  y}  vahyo vat^Asuf  dazdi  ,  .  'rö  xsa'hrä  mazdä  at ahmäi  akäjl  asyS  Y.5/.  6;  —  Aat»Aus(sd.) ; .  .  mazdä  dadät  'rö  . .  yai'öi  vTspäi  ä  Y. 53- Ai  I.  5'-'7>  54- i;  —  aslscä  syao>a-^ nanqm  ..  mazdä  'rahyä  Y.2Ä4;  —  'rahyä urväzsmä  matda  Y._J2.  i; —  'rä  .,  hyal\ *avistä  *hudäbys  mTidfm{&A.)  mazdä  yehyä  ' tu  da'^nm  ^.34- 13;  14, 5 J.  15;  —  mazda  \ x/dira  *vanzT (sd.)  «ä  dyäj  'rö pasüs,,^ frada^äi  ä  Y.45.  9;  —  at  ahyäi  (n'äml.  1 gavöi)  asä  mazdä  urvara  vaxlai  'rö  Y. 4S.  6;  —  C7«  äzötöis  'rö  mq^r>m  lasai . . ' mazda  Y.2(J.  7;  —  ?«;s/  paüö  ya?ia' mazda  'rff  *saittl  ^.33.5;  46.16;  — y^ngstü  mazdä  kad»möi  minas  'rä  Y.  46. , 14; — gätamcä  'räi..t3raohm(^A^  mazdäi ^ Y. 2&5;  —  töi  rwr<7/(sd.)  rädmil  -rahyä- zaosl  mazdä  ^.33.2;   —    yai'ä  xsnaol)H\
7065:^poiiruyi fravöivlde(%^^  Y.44-^  i.        pairj
7237:/ay  (sd.) :  drsgvä  akät  *a  syqs  '*'  manatghö Y.  47-  5 ;  —  y!fi  vanhsus  3  mananAö lyeinti  Y. 3(^.3.  a)  verdoppelt:  vanAsus ä  zl  a  iiianav A3  sydntiYt.  11.12.  4)gAw. mit  Dat.,  nur  unmittelbar  hinter  dem  3i- Dat  der  <i-Stämme,  dessen  Bedeutung  da- durch nicht  verändert  wird :  /rlnpmna  (sd.) ahuräi  3  Y.  3p.  5;  —  yezT  AlH  d3t  .. aAurS .  .yavöi  vlspai  «'"  AvatpA/vTm  (sd.) Y.5J.1;  4;  —  at  m3  .  .  mazöi  magai  a paitTJiänata  Y.  25. 1 1 ;  —  xSmävatqm  vah- mäi  a  Y.^ff.io;  53.2;  —  at  töi  übe  .  . x'an^äi  3  Y.  34.11;  —  dazda  (sd.)  .  . syaohananqm  mazd3i  xfäitrimca  aAurai 3  Y.-jy.is;  —  auch  beim  Jt'-Inf,;  pasBs vJrlng.  ./rada'iai  (sd.)  a  45.9.  5)  gAw. mit  Instr.,  nur  unmittelbar  hinter  dem i3j7-Instr.  aus  Pron.  in  den  adv.-artigen Verbindungen  anais  3,  tat/  a,  yäis  a; sbes.  ni)  Praev.'*'    (mit    'Aar-,    ^kar-,
7386:•  j.  ävöya  Interj.  'wehe!':  ilv  aisra  ava äiöagm  "wehe!  da  sah  ich.."  Vyt.^lj;  —
7389:np.  vgl.  ävah  'wehe  l'  —  Vgl.  avöi  und  iar'öya. -^  Fa.:  anäk,  (zu  ■):  aaäk^i).  —  >)  Das  erste hfal  haben  die  H<ts.  Si-ayÖ.  —  >)  Im  Gegen- satz zu  ka%a  le  dari-pin  iiila  aiava/  H.  2.  l6.
7390:—  3)  Vjjl.  Fü.  zu  avöi,  vayöi.
7421:O  Der  Verf.  bat  wohl    eine   der  Stellen   mit  j  Y.  33.  1 2  j  4y.\;    —    'titaUg  (VS.)  yaoiäh ür«  (s.  >or.)  im  Kopf  gehabt.  I  ^^jj    ^„3,!^,-   *aipi.zaä:)m    vahUta   gavöi
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
9134:•  j.  kaväta-  m.  EN.  eines  iranisclien  j Fürsten,  Begründers  der  Afltvi;>'(sd.)dy- nastie:  kavalm  °l3m  Yti^.  71;  —  kavöis  \ 'taAe  ijsaoip  Vt/_y.  132.  1
10132:;  V.  ig.  41,  Yt  ig.  60';  —  n;imasj  « gaosp^nta^  tumas?  U *gaoAu}ia^^  ^>  V.  2A1, *V.34;  —  y!  . .  yazai  (sd.)  apa  . .  'iulcä västrät  acistsm  mantüm{sd.)  Y.^.  4;  — US  Sus  stuyl  täyäatcä  AazanAatcä  Y,  12. 2;  —  aipi.jatS {sd^  'am  Auhaf>A»m'>^  yai^a ra^aaiä  V.ij.^s; — yat .  .  Aainqm  ava- zSit  ..janyät*n»rSus  para  'am  asSitvar»- iqm  V.18.13;  F. 21;  —  xmmTm  'aus  yä canranhäxl  varaihlm  pantqm  azaite  Yt. 10.  38;  —  jvS  äp?m  jainli  Stram  fräva- yeiti  'am  *var)tqm  azaite  V.5.37;  —  al tsng  dngvä  ySng  alaAyä  vazdrfng  °ä  frU- ntffi/{sd.)  /JiiraAyä  .  .  Y.46.4;  —  nSii ..  karapanS  vSsträt  ar?ffi(sd.)  °avöi  äröis ä  *sfndä{sA.)..yi  Is' ilttgAs ..  Y.51.14;
10281:°tahe  kavöiS  asaonS  "des  G^  Sohns  des Ä".  .."  Yt  7^.123.
11753:—  tä  xsapanB  yä  *ß'äM  Y.öa.io;  — .  a)  adjektivisch;  a)  im  gAw.:  däidl  .  . ätiti  tä  ^ao^na  .  .  yä  anhus  . .  v»rft- '  tarn  aslm  vaahsus  äyaptä  (sd.)  manatgAs yäii  V.J5. 1;  4.41;  —  yat  ta  sravA  drm-  Y.  25.  7.  B)imjAw.:  *us  ^täai  späna jayqri  yä  pagurva  ,  .  'S,  4,  45;  —  ta  fryi  pat»titi  pasus.haurvqmca  . .  V.  /J.  4a;  43; , .  tä  isuds  .  .  ta  rätayo  *yam  (APn.)  —  pqscaUa  ava  ta  aiü  maya  ..  V.g.ii; oAurS  . .  frävavaca  Y.ö^.g; —  tä  daiA-\^2.  a)  mit  relativischem  Anschluss"; MävS  ..  nijayntnte .  .ydhra  /r<Mir!Hnti  ..^  k)  yai  %Pi}K.:  gavöi  aääisizA.)  iäis  ^ao- /mvafayuYtij.^Si  —  yasf  tarn  dahyüm  .'haiiäis  yäis  vahiitäis  Y.J5.4,  b)  im äcaraiti  yaia  {'wo')  huh3r?ts  *baraite  Yt-ijAiw.:  ttm  ratüm  yaxamaide  yim  zara- 10.112;  —  tä  (statt  NPf.)  daiMävS  ti  "ä-usinm  Y.70.IJ  i';  —  i?m  aküm  paik- ^hamtTT^e  yd^a  duzh?nni5  *baraite  mi~  yäite  yim  aiaoiiqm  V. 18.^6;  76,  5.62; ärff  Yt  10.  48;  41.  b)  substantivisch,  —  upa  tarn  ear?lqm  yqm  datvyqm  Yt  /'/. a)  im  gAw.:  «m  (ASm.)  ..  mimaysff  y!  77;  —  tqm  krhrffm  yqm  iristake  V.$.i; qnm3til(sd.)  mazda  srävl  ahursY.4$.io;  —  täia  vt'hü  yaxamaide  yä  antarpsta  Yt 9;  —  alca  töi  (NPm.)  vaim  hyäma  (Sp.  I3.\^y,~- tä  fravaiay5..aojiita  fuiiti  yä '75  0-)  y^^  ■  ■  ^^fDnaoit  . .  Y.30.  9;  —  paoiryanqm lialsanqm  Yt/J.17,  b)  sub- ai  tSi  at?h>n  saosyaiits  .  .  yH  .  .  htüänti  stantivisch;  A)imgAw.:(i//(i/  msi  daxstfm Y.dS.xi;  —  talcit  . .  ySi  /iisitms  \.  data:  ahyl  ar)ASu£  vTspä  atag^ä  (sd.)  Y. 32. 11;  —  t^ng  tfarayS (sd.)  yöi  vä  daibi-  34.6;  —  tatcä  .  .  'kwaAml  *ä  dqm{sA.) Alt/r  Y.  32.1;  44.11,  13;  —  maf  täis  nipäail:  man5  vofia  urunas^a  ..Y.4g.\o; vispais  yöi  .  .  marintl  Y.43. 14;  —  tal  —  yä  tat  upä.jamyjmä :  tavacä  haxfmä v»myädyäi  kyai  msi  mraota  (sd.)  i-aktstim  ,  asaAyl'ä  Y.  40.  a ; — y.J  tat  upä.jamyämä : 43. 1 1 ;  J/.  5 ;  —  vaida  tat  y''  "Ami  .  .  \  tavatä  sarSm  asafiyä/ä  Y.  4l-  6;  —  ta/a analiS  (sd)  Y.46',2;  —  ta  (APn.)  hwa'  vupä .  .htvaAml ..  xia%r?i  ä  voya'i  ra  (%A.) p^rysä  ..ya  aX  aiil(Sp.  14$  ZD.)  ..Y. 31.  i^l^Y.  34. 10;  —  tat  vJ  nJ  Aasaas Jr^Aj  (sd.)
14331:—  kaha  tsi  gavöi  ratul  "hast  du  einen Richter  für  das  Rind?"  Y.  2p.  a ;  —  ku%ra tsi  ar?drü  maztiä  Y.34.-J;  —  kat  tSi rasarJY.34.13;  49^3';  —  iä  tHivanAJui mazda  xiaHraAya  tfft'/ (sd.)  Y.48.8;  8;
17120:•  j.  bävöya  Interj.  'ach  wehe':  ai'Hya  mi.     Pö.;  häsäk  -.ahäk.
```


## [2026-10-16T05:14:26.418Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1057 2>&1 | head -80",
 "description": "Fetch Borhan page 1057"
}
```


### [2026-10-16T05:14:26.817Z] TOOL RESULT

```
no scan of BQT covers printed page 1057 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:14:29.607Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'ژاژ' BQT_v2_pages.txt | head -20; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"ژاژ\")) print NR-1}' BQT_v2_pages.txt | head",
 "description": "Grep Borhan vol 2 for zhazh"
}
```


### [2026-10-16T05:14:30.047Z] TOOL RESULT

```
9914:           ‫خاونده را نجوید افتد بژاژخامی‪.‬‬                    ‫آن خر بودکهآید در بوستان دیا‬
13302: ‫_ معنی دیگر ‪ * :‬بافه وخله وژاژ ولك همه بیهوده بود ولیز گوبند ‪ :‬خله کردم و بافه‬
30889:                                        ‫را داری لورهستند بسی‌ژاژ خوران ( خران ن‪.‬د‪) .‬‬                     ‫‪۴‬‬
30927:             ‫که چرب کوبان آ بجا شود کند زبان ‪.‬‬             ‫‏‪ ٩‬کیکه ژاژ درابد بدرکیش نشود‬
169
225
518
519
```


## [2026-10-16T05:14:32.669Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==520' BQT_v2_pages.txt | sed -n 1,200p | grep -v '^\\s*$' | head -120",
 "description": "Print Borhan vol 2 leaf 519"
}
```


### [2026-10-16T05:14:33.619Z] TOOL RESULT

```
                                                                                               ‫وی ‪— ۵‬‬
‫و سیب آن چنان است که چون بشار بهوا رود‬                   ‫بأکله‌البعیریمنی علفی است که آنرا شتر خورد‬
‫وسرما درو اثرکند غلیظ شود وقطر‪ :‬بارانکردد‬                ‫‪-‬نوانه‬
                                                              ‫ورزن حرس خوالند ک‬
                                                                              ‫ویعربی غلیص ب‬
‫‌ در محل فرود آمدن فعل برودت زیاده درو‬                  ‫هرزه و یاوه و بی مزه و هذبان هم‬             ‫اسزخنان‬
‫تأثیر کند اورا بفشرد وبخ بندد ® ‪ -‬و شینم را‬                                                        ‫همست ‪. ۱‬‬
‫ایز گوبند و سبب آن چنان باشد که شدت‌سرما‬
                                                         ‫راو مك ‪ -‬بثالك بواورسیدہ و میم‬
  ‫یزن‬‫ززدموا‬
          ‫هوای صافی را غلیظ کند وبخار سا‬                 ‫مفتوح بکاف‌زده ‪ ۰‬لوببارا گویند‪,‬وآن تخمی‌است‬
‫اند کی بلند شود و بربر کهای ببانات شیند واز‬                             ‫که بعربی لیا خوانند بکسر لام ‪.‬‬
‫آن قطرها پدید کردد ‪٩‬‏ ‪ -‬و باران تساتراحم‬
                                                            ‫‪ll‬‬                            ‫‪۲‬‬    ‫‪‎ 4‬ا‬
                                                         ‫' = با زای قارسی بروزن تازه »‬              ‫‪2‬‬
‫کفته‌اند ‪ -‬وجاله را نیز گوبند؛ وآن‌چیزی‌باشد‬             ‫بمعنی زار است که علف‌بی‌مزه ‪ -‬کوذابه‌ازسخنان‬
‫که ازچوب وعلف سازند‪ .‬ومش‌کهلی پرباد برآن‬                                                      ‫باشف ‪۰‬‬    ‫هرزه‬
  ‫بوسی‬‫بندند وبرآن شته از آب گذرند ‪ ۷‬؛‬                    ‫ڪر ‪= ۴‬و بررنزن لااعغررا‪ .‬چچےینه‌دان‌مرغان‬
                                                                                                 ‫ژاغر‬
‫آن مشکهای برباد را و مشکی که شناوران بر‬                                 ‫را گوبند و بعربی حوصله خوالنف‪.‬‬
                   ‫پشت بندند ژاله گویشد‪.‬‬
‫او ب=كون واو » خالس وخلاصة هر‬
       ‫‪۰‬‬                                      ‫ھ‬
                                                         ‫کیاهی است دوابی شبیه‌بانگشتان چلیاسه وزفن‪.‬‬
                                     ‫‪۰‬‬   ‫چیز را گوند‬    ‫رال ‪ » ۴‬بروزن لاله‪ .‬تگرك رااگوند‬
             ‫که چرب کوبان آ بجا شود کند زبان ‪.‬‬             ‫‏‪ ٩‬کیکه ژاژ درابد بدرکیش نشود‬
  ‫‪۰‬‬        ‫(‪FA‬‏‬   ‫فری‬   ‫«لت‬   ‫فرخی‌سستالی‪.‬‬
  ‫‪ = ۴‬زاغر (ه‪.‬م‪ ).‬عنصری باخی درخطاب بساپزید بزاغگوبد ‪:‬‬                           ‫رك‪ :‬ژاز ‪.‬‬    ‫؟‏‬
                                          ‫خورند از آنچه بماند زمن ملوك زمین (جهان ‪ .‬ن‪.‬ل‪).‬‬
  ‫‪.‬‬        ‫«لفت امه‬           ‫نو از پلیدی ومردار پر کنی ژاغر ‪.‬‬
  ‫در سانسکریت‪( [802 ..‬سرد» خشك وبیح رکت) «اسشق‪ »4۸۱‬هوبشمان‌ژالهرا از‬                           ‫‪۴‬‬
                                         ‫‪ #‬مأخوذميداند‪ .‬افغانى ‪ « 210۳2‬هویشمان ‪4۸٩‬‏ ‪.‬‬                 ‫‪6‬‬
                  ‫چون غوره بخامی اسرون محکم ‪.‬‬               ‫چون ژاله بسردی اسرون موصوف‬             ‫‏*‬
   ‫‪.‬‬        ‫‪۲4‬‬
             ‫‪4‬رس‬
               ‫‪۹‬ت ف‬
                  ‫منك لرمذی‪ « .‬لف‬
               ‫کرده براو حواله » فواص دردربا‪.‬‬             ‫ژاله‬   ‫اکلهه‬
                                                                     ‫لیر‬
                                                                       ‫‪ ۱‬بافوت وار لاله ‪ .‬بر‬
       ‫کایی‌مروزی‪« .‬لت فرس ‪۲44۹.۰‬‬
  ‫‪-‬رای امن معنی دوشاهد از بك قصیدة فرخی کشرلده‌اند و استاد دهخدا درآن‬
                                                                    ‫‪ ۷‬ب‬
      ‫« کوحله» ‪« ۳‬حیاب» اقرب دالته‌اند نا مع؛ی قخيڭ ماد الدردمیدم» ‪ .‬رك‪:‬‬          ‫دو» کلمةٌ ژاله را نمی‬
                                                                                   ‫لت نامه؛ ورك‪ :‬حاله‪.‬‬
```


## [2026-10-16T05:14:49.809Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==519' BQT_v2_pages.txt | grep -n 'ژاژ\\|ژك\\|ژکیدن\\|۱۰۵' | head; awk 'BEGIN{RS=\"\\f\"} NR==519 || NR==520' BQT_v2_pages.txt | head -3",
 "description": "Check adjacent Borhan leaf"
}
```


### [2026-10-16T05:14:50.304Z] TOOL RESULT

```
36:                                        ‫را داری لورهستند بسی‌ژاژ خوران ( خران ن‪.‬د‪) .‬‬                     ‫‪۴‬‬
                                          ‫کفتار دو آزدهم‬
          ‫از کناب برهان فاطع در حرف زای فارسی با حروف‬
```


## [2026-10-16T05:14:55.638Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'زکیدن\\|ژکیدن\\|ژکید' MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt BQT_v2_pages.txt 2>/dev/null | head -20; grep -n 'zhakidan\\|zhaž\\|žakīdan\\|zhazh\\|ž[aā]ž' HRN.txt HUB.txt CHEUNG.txt | head",
 "description": "Grep Mo'in, Borhan, Horn for zakidan"
}
```


### [2026-10-16T05:14:55.975Z] TOOL RESULT

```
BQT_v2_pages.txt:24758:  ‫مصحف « زکیدن » ( «‪.‬م ‪ ).‬ورك‪ :‬رك »‬               ‫‪۴‬‬            ‫«یب رک ‪ ۹۱۲‬ورك‪ :‬باروچا ‪. ۸۹۲‬‬
BQT_v2_pages.txt:28974:                              ‫رك‪ :‬زکنج ‪.‬‬         ‫‪۴‬‬                ‫‪ - ۳‬رك‪ :‬ز کند‬                  ‫زکیدن ژکیدن )‪.‬‬
MON_part1.txt:71322:زکید ن: 221-14:0[- ژکیدن | (مصل.) خود 
MON_part1.txt:73170:رکیدن: 226-1450 [- زکیدن] (مصل.) 
MON_part1.txt:73172:ژکیده؛ ژکان). آهسته سخن گفتن در زیر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1365:کردن» ژکیدن. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40424:غضب يا غصه؛ ژکیدن. شکایت. شکوه. 
MON_part2.txt:1365:کردن» ژکیدن. 
MON_part2.txt:40424:غضب يا غصه؛ ژکیدن. شکایت. شکوه. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:71322:زکید ن: 221-14:0[- ژکیدن | (مصل.) خود 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:73170:رکیدن: 226-1450 [- زکیدن] (مصل.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:73172:ژکیده؛ ژکان). آهسته سخن گفتن در زیر
```


## [2026-10-16T05:14:59.169Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 71318,71330p MON_part1.txt; echo ---; sed -n 73160,73180p MON_part1.txt; echo; grep -n '^ژاژ\\|ژاژ:' MON_part1.txt | head; grep -n 'زاغ:' MON_part1.txt | head -3; grep -n 'توأم\\|توام:' MON_part1.txt | head -5; grep -n '^وای:\\|وای:' MON_part2.txt | head -3",
 "description": "Read Mo'in entries"
}
```


### [2026-10-16T05:14:59.520Z] TOOL RESULT

```
زکی: ۸ه2(ع.](ص.) پاک پاکیزه. پارسا؛ 
ی از کناء. 


زکید ن: 221-14:0[- ژکیدن | (مصل.) خود 
بخود از روی خشم سخن گفتن. 

رکبه: (۵-)- 2211۷ [ع. رکه | (ص.) مونث 
زکی. 

زگالاب: «:-2 (- زگالابه| (امر.) سرکبی 
سیاه که در دوات کنند؛ حبر؛ مداد. 

---
بممدیس ۵ 
زک: 226 [- زک] (.) سخنی که از روی 
حشم و غضب در زیر لب گویند. 
ژکاره: (-)«27مة [- زکاره] (ص.) لجوج» 
ستیز ه کار» ستبهنده. 
زکان: «22 [- زکان] (ص‌فا.) از خود 
رمنده. شخصی که از روی اعراضص در زیر 
لب خود به خود آهسته سخن گوید. 
ژکور: »22*0 [- زکور - ژگور] بخیل» 
خسیس؛ سفله. ببچیده دزد؛ قطاع الطر یق. 
رکیدن: 226-1450 [- زکیدن] (مصل.) 
(زکید» زکد» خواهد زکید» ‏ زژکنده؛ 
ژکیده؛ ژکان). آهسته سخن گفتن در زیر 
لب از روی خشم و غضب. متغیر شدن, از 
جا در رفتن» کوک شدن (در اصطلاح 
امروز). 
ژلا تین: 2 (۱.) ماده‌ای لزج و چسننده 
که برای ساختن چسب و نیز جهت چاپ‌های 
فوری دستی در روی نوردهای ماشین چاپ 



73001:ژاژ: 122 (۰) (گیا.) بوتة گیاهی است به 
73017:ژاژومیک: ص22 (.) (گیا.) لوییا. 
22827:خلط های ساده یا توأم با چرک و خون؛ ورم 
44606:توام: (-.«0ا)سه #ها [ع.] (ص. .) کودکی 
51488:شخص توأم با نفرت از چیزی. 
57677:خواب: (قد. 56050 (.) حالتی توأم با 
68111:حرکات توأم با موسیقی. (تسص.) حرکات 
81401:نه‌روای: 700-2۷2 اف. ع.) (امر.) ( کد.) نه 
84118:وای: ۶0 (صت.) کلمه‌ای است دال بر: الف 
84123:ای وای: ای افسوس! فسوسا! در یغا! دردا!
```


## [2026-10-16T05:15:02.738Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 73001,73010p MON_part1.txt; echo ---; sed -n 44606,44612p MON_part1.txt; echo ---; sed -n 84118,84123p MON_part2.txt 2>/dev/null; sed -n 84118,84123p MON_part1.txt; grep -n '^زاغ' MON_part1.txt | head -3",
 "description": "Read Mo'in zhazh, tow'am, vay"
}
```


### [2026-10-16T05:15:03.099Z] TOOL RESULT

```
ژاژ: 122 (۰) (گیا.) بوتة گیاهی است به 
غایت سفید و شبیه به درمنه در نهایت 
پیمزگی و هر چند شتر آن را بخاید نرم 
نشود و به سیب بیمزگی فرو برد. و 
دربارةٌ هویت این گیاه اختلاف است. مولف 
برهان آن را علفی دانسته که در دوغ کنند و 
هم آن را نوعی کنگر نوشته مرادف خارشتر 
دانسته است. ۳ د هحد ا در لغت نامه ۳ 
را همان « کا کو تی» می‌داند. ترة دوغ یعنی 
آنچه از رستنی که در دوغ و ماست کنند. 
---
توام: (-.«0ا)سه #ها [ع.] (ص. .) کودکی 
که با کودک دیگر در یکت هنکام زاییده 
شده باشد؛ همزاد؛ دوقلو. تد. توآمان 
ت وآمین؛ ج. توائم. جفت (زن و شوهر). دو 
چیز همراه. 

توآمان: (-.0)1007۷- ۵20 ۱۵ [ع.] (ص. .) 
---
وای: ۶0 (صت.) کلمه‌ای است دال بر: الف 
تألم و افسوس و اندوه» افسوس! در یغ! بت 
- درد و بیماری» دردا! وای بر فلان: افسوس 
بر حال وی. (ا.) انسوس. فریاد» ناله. وای 
فلان: وای بر آن کس؛ افسوس بر حال وی. 
ای وای: ای افسوس! فسوسا! در یغا! دردا! 
شبه: (0-)320-2 [د شوه - شسق) معر. - 
سیج» معر.] (ا.) (زم.) نوعی سنگ و آن 
گونه‌ای لینبیت است که در نتيجة تراکم 


ذرات کرین و تغییرات شیمیایی نسبة سخت 
70088:زاغ‌پا: 2-3 (امر.) ( کد.) سرزنش؛ طعنه. 
70089:زاغ‌چشم: (6) 22۵2 (ص‌مر.) آنکه 
70093:زاغجه: (0)مسته | زاغیچه - زاغیژه]
```


## [2026-10-16T05:15:07.968Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-16T05:15:07.976Z] TOOL RESULT

```

```


## [2026-10-16T05:15:10.229Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زاغ",
 "prompt": "Give the Persian etymology section of زاغ verbatim (Middle Persian form, Proto-Iranian, PIE, cognates)."
}
```


## [2026-10-16T05:15:10.876Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/βάζω",
 "prompt": "Give the Ancient Greek etymology section verbatim."
}
```


## [2026-10-16T05:15:11.679Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/vagio",
 "prompt": "Give the Latin etymology section of vāgiō verbatim."
}
```


## [2026-10-16T05:15:12.230Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/وای",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-16T05:15:13.027Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Thomas",
 "prompt": "Give the English etymology of the given name Thomas verbatim."
}
```


## [2026-10-16T05:15:13.715Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تَوْأَم",
 "prompt": "Give the Arabic etymology and root of tawʾam verbatim."
}
```


### [2026-10-16T05:15:14.831Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-16T05:15:16.817Z] TOOL RESULT

```
# Persian Etymology Section

**Etymology 1:**

The term originates from "Proto-Iranian *wáy, from Proto-Indo-Iranian *wáy, ultimately from Proto-Indo-European *wáy". It shares cognates with Latin "vae" and English "woe", with similar words in Semitic languages including Aramaic and Arabic equivalents.

**Etymology 2:**

This represents an alternative form of another Persian word meaning "hey!"
```


### [2026-10-16T05:15:16.952Z] TOOL RESULT

```
# Latin Etymology of vāgiō

From Proto-Indo-European *weh₂g-. The term shares a cognate relationship with Sanskrit vagnú (वग्नु).
```


### [2026-10-16T05:15:18.139Z] TOOL RESULT

```
# Persian Etymology of زاغ

Based on the Wiktionary entry, here's the etymology information:

**Etymology Source:** "From [Middle Iranian](https://en.wikipedia.org/wiki/Middle_Iranian_languages "w:Middle Iranian languages"), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language")"

**Cognates listed:**
- Sogdian: zʾγ /zāγ/ ("crow")
- Northern Kurdish: *zax* ("crow")
- Parthian: zxs- /zaxs-/ ("to sound")

The entry does not provide a Middle Persian form, Proto-Indo-European reconstruction, or additional PIE cognates—only the Middle Iranian and Proto-Iranian origins with the three related forms noted above from neighboring language families.
```


### [2026-10-16T05:15:18.839Z] TOOL RESULT

```
# Ancient Greek Etymology

The etymology section for Ancient Greek βάζω states: "Probably onomatopoeic; see also βάσκειν (báskein) and βάσκανος (báskanos), which are potentially related."

It also notes the possibility that this word group represents borrowings from Macedonian or Balkan Indo-European languages (Thracian, Illyrian) derived from Proto-Indo-European *bʰeh₂- ("to speak, say"), with a comparison to φάσκω (phắskō, "to declare; to affirm; to think").

The section concludes by noting this Ancient Greek term is unrelated to Modern Greek βάζω (vázo, "to put, place"), which instead derives from Ancient Greek βιβάζω (bibázō, "to raise").
```


### [2026-10-16T05:15:19.347Z] TOOL RESULT

```
# English Etymology of Thomas

According to the Wiktionary entry, Thomas is "Inherited from Middle English _Thomas_, from Latin _Thōmās_ m (as in the Vulgate), from Ancient Greek _Θωμᾶς_ m (Thōmâs), the Biblical Greek transcription of Aramaic _תאומא_ or _תאמא_ ("twin"), the nickname of one of the Twelve Apostles."

The name has been used as a given name since the Middle Ages, with early historical examples including Thomas the Presbyter (7th century) and Thomas the Slav (8th century).

[WebFetch note: this page's text is 115414 characters long and the answer above covers only characters 0 to 100000; the final 15414 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-16T05:15:21.444Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/توأم",
 "prompt": "Give the Arabic and Persian etymology and root verbatim."
}
```


## [2026-10-16T05:15:22.270Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/woe",
 "prompt": "Give the English etymology section verbatim (first etymology)."
}
```


## [2026-10-16T05:15:22.688Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ژاژ",
 "prompt": "Give the Persian etymology and meanings verbatim."
}
```


### [2026-10-16T05:15:25.757Z] TOOL RESULT

```
# Arabic Etymology and Root

**Etymology:** The word compares to Akkadian _tu'amu_, Aramaic _təyōmā_, Classical Syriac _təʾāmā_, and Hebrew _təʾôm_.

**Root:** و ء م (w ʔ m)

# Persian Etymology

**Etymology:** "Borrowed from Arabic _تَوْأَم_ (tawʔam)."

The Persian entry explicitly derives from the Arabic source, carrying the same root: و ء م (w ʔ m).
```


### [2026-10-16T05:15:26.456Z] TOOL RESULT

```
# Persian Etymology and Meanings of ژاژ

**Etymology:** The Wiktionary entry does not provide an explicit etymological origin for the Persian term ژاژ.

**Meanings:**

1. **Archaic sense:** "A tough, insipid variety of artichoke which cannot be chewed or swallowed by the camel"

2. **Figurative sense:** "idle talk, nonsense"

The entry includes a literary citation from Rumi's Masnavi (c. 1260s), where the term is used to mean drivel or foolish speech.
```


### [2026-10-16T05:15:27.198Z] TOOL RESULT

```
# English Etymology 1

From Middle English *wo*, *woo*, from Old English *wā*, *wǣ*, from Proto-West Germanic *\*wai* (interjection), from Proto-Germanic *\*wai* ("woe!", interjection), ultimately from Proto-Indo-European *\*wáy* ("oh!; ah!; woe!; alas!", interjection).

The word shares cognates across numerous languages, including Scots *wae*, German *Weh/Wehe*, Dutch *wee*, Yiddish *וויי* (vey), and Scandinavian forms like Swedish *ve*. Related terms also appear in Romance languages (Spanish *guay*, Italian *guai*, Portuguese *guai*), Celtic languages (Welsh *gwae*, Cornish *gew*), and other Indo-European languages including Latin *vae*, Russian *увы́* (uvý), and Ancient Greek *οὐαί* (ouaí).
```


## [2026-10-16T05:15:33.497Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/زاغ|page 525, root Wag 2/Gwag, zâğ crow: Sogdian zʾγ, Kurdish zax cognates' 'https://en.wiktionary.org/wiki/βάζω|page 525, root Wag 2, Greek bazô: probably onomatopoeic' 'https://en.wiktionary.org/wiki/vagio|page 525, root Wag 2, Latin vagio < PIE *weh2g-, cognate Skt vagnu' 'https://en.wiktionary.org/wiki/وای|page 525, root Wai, Persian vay < PIr *way < PIE *way' 'https://en.wiktionary.org/wiki/Thomas|page 525, root W.a.m, Thomas < Greek Thomas < Aramaic twin' 'https://en.wiktionary.org/wiki/توأم|page 525, root W.a.m, Arabic tawam root w-ʔ-m, Persian loan' 'https://en.wiktionary.org/wiki/woe|page 525, root Wai, English woe < OE wa < PGmc *wai < PIE *way' 'https://en.wiktionary.org/wiki/ژاژ|page 525, root Wag 2, Persian žâž: plant (insipid thistle) and figurative nonsense'; do python3 tools/fetch_source.py \"${u%%|*}\" --note \"${u#*|}\" 2>&1 | tail -1; done",
 "description": "Archive web sources"
}
```


### [2026-10-16T05:15:36.776Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5721c53027109d6f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e2ad6d3fdb0e917.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8981008fafbe017e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/feb7e8cfe626a24f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ece05050ff75720d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/48ec259be66e3bb6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/53dd6ca60bc4ed1f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/362afe12cee53e1c.txt
```


## [2026-10-16T05:15:43.078Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo AHD; grep -n -i '^wai\\b\\|^wai\\.\\|^wāg\\|^wag-' AHD_watkins1985.txt | head; grep -n -i 'woe' AHD_watkins1985.txt | head -3; echo HRN; grep -n -i 'zäg\\|zāg\\|zâg\\|zagh\\|wäi\\|wāi\\b\\|väi\\b' HRN.txt | head; echo HUB; grep -n -i 'zäγ\\|zāγ\\|zäg\\|zāg\\|väi\\b\\|wäi\\b' HUB.txt | head; echo PHD; grep -n -i 'zāg\\|^way\\b\\|wāy\\b\\|wayy' PHD_mackenzie.txt | head; echo NYB; grep -n -i 'zāγ\\|zāg\\b\\|vāy\\b\\|wāy\\b' NYB_vol2_glossary.txt | head",
 "description": "Grep AHD, Horn, Hubschmann, MacKenzie, Nyberg"
}
```


### [2026-10-16T05:15:43.431Z] TOOL RESULT

```
AHD
1117:wag-. Sheath, cover. Suffixed lengthened-grade form *wdg-ind in Latin vagina, sheath: VAGINA, VANILLA; EVAGINATE, INVAGINATE. [Pok. 1. wag- 1110.]
1118:wai. Alas (interjection). 1. Germanic *wai in Old English wd, wei, woe (interjection), alas: WOE; WELLAWAY. 2. Germanic *waiwalén in Old Norse vdla, véla, *veila, to lament, akin to the Scandinavian source of Middle English wailen, to wail: wat. [Pok. uai- 1110.]
1118:wai. Alas (interjection). 1. Germanic *wai in Old English wd, wei, woe (interjection), alas: WOE; WELLAWAY. 2. Germanic *waiwalén in Old Norse vdla, véla, *veila, to lament, akin to the Scandinavian source of Middle English wailen, to wail: wat. [Pok. uai- 1110.]
HRN
1731:kurd. ha, wäi; afy. vö; oss. t. wäd, vad (69); bei.
2787:oss. fäzzäg 'Herbst' (269) (?); sar. pij 'Herbst'.
2938:eS05. perväi^ 'Flug .
4506:finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
4650:denkt dagegen an ein ap. *kwäisiija' als Grundform;
7513:KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
12258:rfösWäi- 582, 1121.
17035:väiömandi/^ 213.
HUB
PHD
5280:way [w)d I M w)y, N ......] woe.
NYB
4058:vāyēndak [w'yndk'] flying creature, pl. cas. obl. —-än, enumerated after murvān 802. — Pres. pt. of Av. (1356) Wvay- ‘to fly’.
5428:lvay-: vāyēndak
```


## [2026-10-16T05:15:47.360Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7505,7516p HRN.txt; grep -n -i 'zag\\b\\|zāγ\\|zāy\\b' PHD_mackenzie.txt | head -5; grep -n 'زاغ' BQT_v2_pages.txt | head -5; grep -n '\\b\\(zag\\|zāg\\)\\b' SOD.txt | head -3; grep -n -i 'Wai\\b\\|Weh' incoming/WLD/WLD_Bd1_pages.txt | grep -i 'u̯ai\\|uai' | head",
 "description": "Read Horn and grep for zag"
}
```


### [2026-10-16T05:15:47.813Z] TOOL RESULT

```
711)', kidä, hdeli.
') Vergl. g. kaj).
^) Durch einen Vers des vorfirdusischen Dichters Abu Öekür
belegt.
^) Im Neupersischen wird das Wort aber nie mit q^ sondern stets
mit k geschrieben. Es müsste also ein Schnitzer im Gazophylacium
und in der jüd.-pers. Schreibung vorliegen.
*) Nachträglich sehe ich Hübsch mann's Bemerkungen in
KZ. 26, 607 folg., der auch aw. väi^ayun- nicht als *Rabe* gelten lassen
will und bei. f/nräy *crow\ köh-f/uräy Vaven' (Damea, S. 104) heran-
zieht ( Corrokturnoto ).— 193 —
Zu ahd. hulja, hulla 'Kopfbedeckung, also zu got.
583:delete niylzag ... (read wezag).
630:add war·wezag [wl-w}yck'] andi.xtall : cast lots.
632:add wezag [w)yck'] lot.
765: ---mlzag [-m(y)ck l ] tasteless.
793: abezag ['pyck l I M 'bycg, (N weza)] pure, holy.
607:‫بر وزن نامه » بارچة بافتة‬                   ‫جامه =‬                       ‫جامقول‪ -‬باغینقطەدارېروزنزاغنول‪.‬‬
1809:                                                                             ‫‪ ۴‬و دشمن زاغ است‬           ‫مشپور‬
1814:                                                                             ‫کرده بودند و با زاغ مشورت‬
2042:           ‫یاجگر بندپیش زاغ بنه‪.‬‬                      ‫ببتاشوش وغصه راضی شو‬
4119:‫چالیوس ت بابای فارسی‌وواومجهول‬                             ‫کووچثآ نرکاه ببزرکی‌زاغ است‌چال کوبند ‪۴‬‬
19331:von dt. ic und s. u.), Fick I 4 542 (unter Yermengung mit *uai- „weh“)
19478:    uai Interjektion „wehe!“
```


## [2026-10-16T05:15:52.139Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 19478,19486p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-400; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"uai Interjektion\")) print \"leaf\",NR}' incoming/WLD/WLD_Bd1_pages.txt; grep -n 'uäg-\\|uāg-\\|u̯āg' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -i 'zāγ\\|zāγ\\|zāg\\b\\|zäγ' SOD.txt | head -3; grep -n -i '^THOMAS\\|^WOE\\|^WO,' SKT.txt SKT_dli_revised.txt | head",
 "description": "Walde-Pokorny and Gharib, Skeat lookups"
}
```


### [2026-10-16T05:15:52.528Z] TOOL RESULT

```
    uai Interjektion „wehe!“
         Ai. live (NeiBer BB. 30, 303), av. vayoi, avoi, Uvbya „wehe!“                  voya „Weh-
                                                                                      (
    ruf“):      arm. vay                  „Wehe, Pngluck u (Scheftelowitz BB. 29, 43; v- statt g- aus
idg.w- dutch nebenherlaufende Neuschopfung); ahnlich gr. oa (wie lat. rahl)
    und     seit          alexandrinischer Zeit ova,                  ova, ovai,                 ngr.    [id'i   (Yeusclidpfungen;
    s.   auch Curtius 563)
         lat.   vac   ;
                              mir. fate, cymr. gwae „weh              !
leaf 221
SKT.txt:21597:Wo,  Woo.  (E.)  M.E,  «B»;  A.S,  wri, intcrj.  and  adv. ;  wea^  wo,  «b.  +  Da.  vct^ inteij.  and  sb. ;  led-  vci^  Dan.  vee^  Swed. ve,  G.  ttvA,  Goth,  wai,  interj. ;  also  Dan. V€tt  G.  wth,  sb.  Allied  to  ll  ««,  wo  I Orig.  an  exclamation  ;  hence  a  cry  of pain,  &c.  Der.  wob^gom,  i.e.  wo-sor- rotmded,  from  M,  E.  bcgon^  pp.  of  begtm  — A.  S.  hegiin^  to  sarround,  lit.  to  go  roand abont ;  from  A.  S.  ^-  ( —  £.  J^l,  and  gdn, to  go.  Also  wo  worth,  i.  e.  wo  be  to ;  see Worth.
SKT_dli_revised.txt:35945:Thomas, who is called Didymus, John 
SKT_dli_revised.txt:88550:Wo, Woe. (E.) M. E. ; A. S. zvn,
```


## [2026-10-16T05:15:58.392Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'vagn\\|vägiö\\|vagio\\|vāgiō' incoming/WLD/WLD_Bd1_pages.txt | head -3; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"vagnu\")||index($0,\"vägiö\")) print \"leaf\",NR}' incoming/WLD/WLD_Bd1_pages.txt; grep -n -i 'vagio\\|vāgiō\\|vāgīre' LAT.txt | head -3; grep -n -i 'gaga\\|‘crow\\|crow' SYN.txt | grep -i 'zāγ\\|zāg\\|zag' | head",
 "description": "More lookups in WLD, Ernout-Meillet, Buck"
}
```


### [2026-10-16T05:15:58.735Z] TOOL RESULT

```
19670:                                                                                                      (:   gloss,               vagna „jiovTtig /ueydb],
20091: air. fan *vagno- „schrag, abschussig", cymr. gwitun „Feld, Wiese", ncorn.
23367: ags. ivatgn,      vagn „Wagen“ (abl. mit ir. fen); aisl. vagi m. „Hahnen-
```


## [2026-10-16T05:16:02.427Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'schreien' incoming/WLD/WLD_Bd1_pages.txt | grep -i 'u.g\\|uag\\|uäg' | head; grep -n -i 'v[aā]gi[oō],\\|vagio\\b' LAT.txt LEW_1910.txt | head -4; grep -n -i 'z[aā][γgy]\\b' SYN.txt | head -5",
 "description": "Search WLD for wag schreien; LEW/LAT vagio; Buck crow"
}
```


### [2026-10-16T05:16:02.839Z] TOOL RESULT

```
19720: uag- „schreien“.
19759:uagh-     „schreien, schallen ':         1
19798:Mitwirkung von kaiikti „heulen“. Baiikti „schreien' ) unter idg. c tig- moglich
56303:     Mit i-Erweiterung daneben mhd. krischen „kreischen“, mnd. kriten „schreien,
59752:rein schallmalende Konsonantenscharfung); anord. gala (Prat, got) „schreien,
60466:      Zweifelhaft bleibt, ob *ghouros zu ghau- „rufen ,schreien“ zu stellen ist.
62560:ghleu- „frohlich              sein,    scherzen",         Erweiterung von <jhcl- ,,schreien“ oder
LEW_1910.txt:3120:Onvdg.ioyv, Onvagio- boc I 339
15011:Grk,  zplav ON sog Lett.  zag’is NG — zptért Dan. sav ChSl. pila Lat. serra Sw. sdg SCr. _ pila, testera It. oP OE _ sagu, snid Boh. pila eS Rrra ME _ sawe Pol. pila a feresirdtu NE saw Russ. pila Ir ” ‘tuiresc (serr) Du. zaag Skt. krakaca-, karapatra- Nir, sdbh (loireasc) vias saga Ay. : w. lif sage Br. _heskenn NHG _ sdge
15028:Lett. zag’is, fr. MLG sage: OHG saga, etc. (above, 4). Miihl.-Endz. 4.695.
25287:Boh. zase ‘backwards’ and ‘again’, fr. za ‘behind’ and refl. se, like Pol. zag ‘but’, earlier zasig. Gebauer 1.206. Linde 6.887.
29213:OHG zagi, MHG zage, zag(e)haft, NHG (zag), zaghaft (in older periods ‘cowardly’, now much milder ‘faint- hearted, timid, hesitant’; replaced in older sense by feig) with vb. OHG zagén ‘lose courage, be undecided’, NHG ver- zagen ‘despair’, perh.: Goth. tahjan ‘tear’, Norw. dial. teja, taa ‘shred’, cf. also Norw. dial. taag ‘slow, lasting’, and for semantic development NHG zégern ‘delay’ : OHG zogon ‘pull, tear’. In any case semantic development prob. through ‘hesitant, irresolute’. Walde-P. 1.785. Falk-Torp 261.
```


## [2026-10-16T05:16:07.323Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 19720,19730p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-300; grep -n 'CROW' SYN.txt | head -3",
 "description": "Read WLD uag- schreien"
}
```


### [2026-10-16T05:16:07.831Z] TOOL RESULT

```
 uag- „schreien“.
   Ai. ragnti- m. „Ton. Ruf, Zuruf", ved. ragvam- „liirmend“, vagvanu- m.
 „Get6se“ (Ublenbeck Ai. Wb. 267 zw.     lat. vugio. -ire „wimmern, quieken          ;
                                                                                                                                                                 11



 (FBilenbeck aaO. kann a als von einem 7-St. *iiagi-s ausgegangene Debn-
                                         ;
stufe  haben, s. Niedermann IA. 19, 35 f.); fraglich gr. tieqi - ayvvzai uy )
,,hallt ringsum wider      Fick I 4 124: eher „wird ring&um gebrochenA zu
23681:13.19 MULTITUDE, CROWD
```


## [2026-10-16T05:16:14.775Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"woe, also wo\")||index($0,\"Thomas,  masc\")) print \"leaf\",NR-1}' KLN_1966.txt; cd /home/sfmqrb/git/rishe-private; timeout 200 python3 tools/ref_page.py BQT:2255 2>&1 | grep -n 'وای\\|png\\|PNG' | head",
 "description": "Locate Klein leaves and fetch Borhan 2255"
}
```


### [2026-10-16T05:16:23.593Z] TOOL RESULT

```
leaf 852
6:وق وامق و عذرا مشهور است ‎٩‏ - وایکی | ترکیب گفته دمیشود .
16:ولایت شروان 9 - و شبه و مانند ونظیر را لیز وای - بر وزن لای » چاهی را گوبند
30:امیرفرمو د که «مامردم قرآن خوایم .۰ بغیر ازقر آن وحدیث پیغمبر چیزی لمیخواهیم. ما را ازین
31:نوع کناب درکاریست » واین کتاب تألف هفاست و پیش ها «*ردودست.» فره‌ود تاآن کناب را در
52:وای ۰ منتهی‌الارب » «صاب» ۹
```


## [2026-10-16T05:16:27.192Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 200 python3 tools/ref_page.py BQT:2255 2>&1 | sed -n 1,25p; timeout 200 python3 tools/ref_page.py BQT:2255 2>&1 | sed -n 45,60p",
 "description": "Show Borhan 2255 text"
}
```


### [2026-10-16T05:16:27.721Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 338; check the printed number and re-run with --pdf-page if off)
REF: BQT:2255  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 338  OCR-lang: fas

<< ارای

وق وامق و عذرا مشهور است ‎٩‏ - وایکی | ترکیب گفته دمیشود .

از اصطلاحات بازی نرد هم هت » و آن داوی وانج ه بسکون نون وجیم » غله‌است

باشد که بر بازد هکشند؟ . ۱ که آنرا بعربی عدس میگوبند۷ ۰
وامی؟ بروزن جامی » قرض دار - وانکونتی۸ * باکاف‌وئون دیگروتای

ودرمانده وعاجز را ۴ کوبند . قرشت بروزن آرزوشکن» بلغت زلد وپازند (۱)
وان - بر وزن کان » نام شهرست از | بمعنی کرفتن باشد .

ولایت شروان 9 - و شبه و مانند ونظیر را لیز وای - بر وزن لای » چاهی را گوبند

میگویند - وبمعنی‌نگهبان ونگاهدارنده وحاری | که زینه پایها برآن ساخته باشند تا باسانی بته

و محافظت کننده هم هت ‎٩‏ همچو کله وان رفته آب بردارند ‎٩‏ - وبمعتی گمراه نیز آمده

ودشت وان وفیل‌وان و امثال آن » لیکن بدون | است - و لفظی باشد که در محل آزاری ودردی

(۱) چك : ژند و یاژند .

استه وغامی شدم ز درد جدایی هامی و وامی شدم زختن مترب" .>

« لفت. فری ص ۳۰-۵۲۹
8 - شهری در ترکیه » واقع در فلات ارمنستان » در ماحل شرقی درباچهٌ وان . رك :
دالرةالممارف اسلام : 3 ‎٩‏ ع بان (م.) وزك : ص لو- له از ديباچهٌ مولف .۰
۷ - رك : جهانگیری . ۸ - مسحف دز . ۷88۵8128 ۰ ۰۷84۵81188
0 پپلوی 8716128 ( کرفتن ) « یونکر ص ۷۹ *. ‎«٩-4‏ ویل (عر )۰
وای ۰ منتهی‌الارب » «صاب» ۹
```


## [2026-10-16T05:16:42.718Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,200p tools/verify_check.py | grep -n 'PROBLEM\\|def \\|required\\|sources' | head -60",
 "description": "Inspect checker requirements"
}
```


### [2026-10-16T05:16:43.063Z] TOOL RESULT

```
16:def page_no(path):
20:def main(argv):
90:        print("PROBLEM:", p)
```


## [2026-10-16T05:16:45.258Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 20,95p tools/verify_check.py",
 "description": "Read checker logic"
}
```


### [2026-10-16T05:16:45.898Z] TOOL RESULT

```
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


## [2026-10-16T05:18:23.553Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-525.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOKwag={\"ref\":\"POK:1110\",\"status\":\"partial\",\"note\":\"POK_03.txt l.5000: '3. u̯āg- ,schreien'; vielleicht von einer Schallwurzel u̯ā-. Ai. vagnu- m. ,Ton, Ruf' ... lat. vāgiō, -īre ,schreie, wimmere' ... lit. vógrauti' — covers Skt and Latin only; no Greek bazō, no Persian, and the root is u̯āg- (not gʷag-).\"}\nIEC={\"ref\":\"IEC:351,354\",\"status\":\"supports\",\"note\":\"IEC.txt l.5101: 'guag- (2), guāg- ‘quack, squeak, squeal’ Per. cf. žāž ‘twaddle’ ... Gk. bázō ‘talk’, bágma ‘talking’ ... Long vowel in Lat. vāgire, v. ‘scream’'; l.5141: 'gueguos, io “a croaking bird'. Variant of guag- (2) ... Per. zày ‘crow, raven’' — this is Nourai's source for root, glosses and Persian/Greek/Latin; note Mann's own 'cf.' (tentative) for žāž.\"}\nWLDwag={\"src\":\"WLD\",\"where\":\"Bd. I p. 214 (WLD_Bd1_pages.txt l.19720)\",\"stance\":\"partial\",\"note\":\"'uag- „schreien“. Ai. vagnu- m. „Ton, Ruf, Zuruf“ ... lat. vāgio, -īre „wimmern, quieken“' — Skt and Latin only; Greek only a doubtful 'fraglich gr. περιάγνυται'; no Iranian.\"}\nAHDwag={\"src\":\"AHD\",\"where\":\"Watkins 1985 l.1117\",\"stance\":\"silent\",\"note\":\"only 'wag-. Sheath, cover ... Latin vagina [Pok. 1. wag- 1110]'; the 'cry' root 3. u̯āg- is not listed.\"}\nWAIpok={\"ref\":\"POK:1110\",\"status\":\"supports\",\"note\":\"POK_03.txt l.5011-5014: 'u̯ai Interjektion ,wehe!' ... Av. vayōi, avōi, āvōya ,wehe!' ... got. wai, aisl. vei, ahd. as. wē; ags. wā ,wehe!'' (pp.1110-1111).\"}\nWAIwld={\"src\":\"WLD\",\"where\":\"Bd. I p. 212 (leaf 221, WLD_Bd1_pages.txt l.19478)\",\"stance\":\"supports\",\"note\":\"'uai Interjektion „wehe!“ Ai. uve, av. vayoi, avoi, āvōya „wehe!“ ... arm. vay ... lat. vae ; mir. fáe, cymr. gwae'.\"}\nWAIahd={\"src\":\"AHD\",\"where\":\"Watkins 1985 l.1118\",\"stance\":\"supports\",\"note\":\"'wai. Alas (interjection). 1. Germanic *wai in Old English wā, wei, woe ... WOE [Pok. uai- 1110]'.\"}\nKLNthom={\"ref\":\"KLN:1609\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l.39088 s.v. Thomas: 'Eccles. L., fr. Gk. Θωμᾶς, lit. ‘twin’, fr. Syr. tōmā, ‘twin’, which is rel. to Aram. tᵉʾōmā, Heb. tᵉʾōm, Akkad. tuamu, Arab. tauʾam, ‘twin’. All these words are prob. derivatives of the Semitic base w-ʾ-m, ‘to tally’. Cp. Arab. waʾama'.\"}\nentries=[]\n# entry 2\ne2={\"entry\":2,\"root\":\"Wag 2, Gwag, Gwâk / Gwĕguos\",\"verdict\":\"plausible\",\n\"modern_form\":\"PIE *weh₂g- (Pokorny 3. u̯āg-) 'to cry, wail' (Skt vagnú-, Lat. vāgiō); Mann's separate *gʷag-/*gʷeguos 'quack; croaking bird' is an onomatopoeic set of doubtful status\",\n\"note\":\"The box merges two different reconstructions: Pokorny's 3. u̯āg- 'schreien' (p.1110; Skt vagnu-, Lat. vāgiō, Lith. vógrauti), and Mann's gʷag- (2) 'quack, squeak, squeal' + gʷeguos 'a croaking bird' (IEC), from which Nourai takes the Persian, Greek and gloss. Skt v- cannot continue PIE *gʷ- (which gives Skt g/j), so the Sanskrit node only fits Pokorny's *u̯āg-; Greek β- only fits *gʷ-. Both are onomatopoeic, so a loose 'cry-sound' family is acceptable, but as one root it is a conflation.\",\n\"note_fa\":\"در این کادر دو ریشهٔ جدا با هم آمیخته شده‌اند: ریشهٔ هندواروپایی آغازین *weh₂g- (پوکورنی ۱۱۱۰: u̯āg- «فریاد زدن») که سنسکریت vagnú- و لاتین vāgiō از آن‌اند، و ریشهٔ نام‌آوای *gʷag- / *gʷeguos «قارقار، پرندهٔ قارقارکن» در فرهنگ مان که واژه‌های فارسی و یونانی از آنجا آمده‌اند. «و» سنسکریت نمی‌تواند از *gʷ برآمده باشد، پس این دو یکی نیستند. ادعای نورایی تنها با احتیاط و به‌عنوان یک خانوادهٔ نام‌آوایی پذیرفتنی است.\",\n\"sources\":[W+\"vagio\"],\n\"ref_check\":[POKwag,IEC],\n\"consulted\":[WLDwag,AHDwag],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Persian\",\"words\":\"žâž; zâğ; zakîdan\",\"verdict\":\"disputed\",\n\"derivation\":\"žâž: Mo'in and Borhan define ژاژ first as a plant — a tough, insipid thistle/artichoke-like herb that camels chew without being able to swallow — and only figuratively as 'idle talk' via the idiom ژاژ خاییدن 'to chew žâž' (ژاژخا 'chatterer'); the 'nonsense' sense is thus a metaphor from the plant name, not an onomatopoeic reflex of *gʷag-, and Mann himself only writes 'cf.'. zâğ 'crow': Iranian *zāγ- (Sogdian zʾγ /zāγ/, Kurdish zax) is a genuine Iranian bird name; Mann derives it from *gʷeguos (PIE *gʷe- > PIr *ja- > z), which is phonetically possible but the word is more likely an independent imitative formation — plausible at best. zakîdan/žakîdan 'mutter in anger' (Mo'in: 'آهسته سخن گفتن در زیر لب از روی خشم') has no published etymology I could find — unverified. Worst verdict (žâž) governs: disputed.\",\n\"derivation_fa\":\"«ژاژ» در برهان قاطع و فرهنگ معین نخست نام گیاهی بی‌مزه و سخت (گونه‌ای کنگر یا خارشتر) است که شتر آن را می‌خاید و فرو نمی‌برد؛ معنای «سخن بیهوده» از ترکیب «ژاژ خاییدن» (ژاژخا) به‌گونهٔ استعاری برآمده است، پس پیوند آن با ریشهٔ نام‌آوای *gʷag- پذیرفتنی نیست و پژوهش امروزی آن را تأیید نمی‌کند. «زاغ» واژه‌ای ایرانی است (سغدی zāγ، کردی zax) و پیوندش با *gʷeguos از دید آوایی (*gʷe- > ایرانی *ja- > ز) شدنی است ولی احتمالاً نام‌آوای مستقل است. برای «ژکیدن/زکیدن» «زیر لب از خشم سخن گفتن» ریشه‌شناسی معتبری نیافتم.\",\n\"sources\":[W+\"ژاژ\",W+\"زاغ\"],\n\"ref_check\":[IEC,\n {\"ref\":\"BQT:1057\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaf 519 (≈ printed p.1057-1062): ژاژ 'بمعنی ژاژ است که علف بی‌مزه ... کنایه از سخنان هرزه باشد' with the same Farrokhi verse Nourai quotes ('کسیکه ژاژ درآید به درگهش نشود'); no IE etymology given, and the primary sense is a plant.\"},\n {\"ref\":\"MON:1742\",\"status\":\"partial\",\"note\":\"MON_part1.txt l.71322 'زکیدن [= ژکیدن] (مصل.) خود بخود از روی خشم سخن گفتن' and l.73170 'ژکیدن ... آهسته سخن گفتن در زیر لب از روی خشم و غضب' — meaning confirmed, no etymology.\"}],\n\"consulted\":[\n {\"src\":\"MON\",\"where\":\"MON_part1.txt l.73001 s.v. ژاژ\",\"stance\":\"contradicts\",\"note\":\"'ژاژ: (گیا.) بوتهٔ گیاهی است به غایت سفید و شبیه به درمنه در نهایت بی‌مزگی و هر چند شتر آن را بخاید نرم نشود' — the basic meaning is a plant, against an onomatopoeic origin.\"},\n {\"src\":\"HRN\",\"where\":\"p.193 fn. (HRN.txt l.7513)\",\"stance\":\"silent\",\"note\":\"only a footnote on Av. vāiγayun- 'raven' and Bal. gurāγ 'crow'; no entry for zāγ or žāž.\"},\n {\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt grep 'zāg'\",\"stance\":\"silent\",\"note\":\"no zāg 'crow' entry found.\"}]},\n{\"id\":2,\"lang\":\"Sanskrit\",\"words\":\"vagnu\",\"verdict\":\"confirmed\",\n\"derivation\":\"Vedic vagnú- m. 'sound, call, cry' (also vagvanú- 'din') is the standard Indic reflex of PIE *weh₂g-/*u̯āg- 'to cry' with short a (zero/normal grade), cognate with Latin vāgiō; it does not reflect *gʷag-, since PIE *gʷ- gives Sanskrit g-/j-, not v-.\",\n\"derivation_fa\":\"سنسکریت ودایی vagnú- «بانگ، آواز، فریاد» بازماندهٔ منظم ریشهٔ هندواروپایی آغازین *weh₂g- «فریاد زدن» و هم‌ریشه با لاتین vāgiō است. این واژه از *gʷag- نیست، چون *gʷ در سنسکریت g یا j می‌شود نه v. ادعای نورایی (با ارجاع به پوکورنی) درست است.\",\n\"sources\":[W+\"vagio\"],\n\"ref_check\":[POKwag],\n\"consulted\":[WLDwag,AHDwag]},\n{\"id\":3,\"lang\":\"Greek\",\"words\":\"bazô; bagma\",\"verdict\":\"plausible\",\n\"derivation\":\"Greek βάζω 'to speak, say' (< *βάγ-yω) with βάγμα 'speech' is attested from Homer on; Mann sets it under *gʷag- (PIE *gʷ- > Greek β- regularly), but Wiktionary/Frisk/Beekes regard it as 'probably onomatopoeic' (cf. βάσκω, βάσκανος) or a Balkan borrowing; Pokorny and Walde-Pokorny do not list it under u̯āg-. Accepted only by Mann, so plausible.\",\n\"derivation_fa\":\"یونانی βάζω «سخن گفتن» و βάγμα «گفتار» از هومر به بعد گواهی دارد. مان آن را از *gʷag- می‌داند (*gʷ در یونانی به β بدل می‌شود)، اما ویکی‌واژه و فرهنگ‌های یونانی آن را بیشتر نام‌آوایی یا وام‌واژهٔ بالکانی می‌دانند و پوکورنی آن را در این ریشه نیاورده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"βάζω\"],\n\"ref_check\":[IEC],\n\"consulted\":[WLDwag,{\"src\":\"POK\",\"where\":\"p.1110 (POK_03.txt l.5000)\",\"stance\":\"silent\",\"note\":\"3. u̯āg- lists only Ai. vagnu-, lat. vāgiō, lit. vógrauti — no Greek βάζω.\"}]},\n{\"id\":4,\"lang\":\"Latin\",\"words\":\"vâgîre; vâgio\",\"verdict\":\"confirmed\",\n\"derivation\":\"Latin vāgiō, vāgīre 'to cry, wail (of infants), squall' (with vāgor 'cry', vāgītus 'wailing') continues PIE *weh₂g- with lengthened/laryngeal ā; Pokorny, Walde-Pokorny and Wiktionary all pair it with Sanskrit vagnú-. Mann also lists it ('Long vowel in Lat. vāgire'), so all sources agree on the word; only the root label 'Gwag' is Mann's.\",\n\"derivation_fa\":\"لاتین vāgiō / vāgīre «گریستن و جیغ زدن (نوزاد)» بازماندهٔ ریشهٔ هندواروپایی آغازین *weh₂g- با ā کشیده است و پوکورنی، والده‌ـپوکورنی و ویکی‌واژه آن را هم‌ریشهٔ سنسکریت vagnú- می‌دانند. ادعای نورایی درست است.\",\n\"sources\":[W+\"vagio\"],\n\"ref_check\":[IEC,POKwag],\n\"consulted\":[WLDwag,AHDwag]}]}\nentries.append(e2)\ne3={\"entry\":3,\"root\":\"Wai\",\"verdict\":\"confirmed\",\"modern_form\":\"PIE *wáy 'woe!, alas!' (interjection)\",\n\"note\":\"Pokorny 1110 u̯ai Interjektion 'wehe!'; AHD wai 'alas'. Root, label and gloss correct.\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *wáy بانگ «وای! افسوس!» است (پوکورنی ۱۱۱۰، واتکینز). ادعای نورایی درست است.\",\n\"sources\":[W+\"woe\",W+\"وای\"],\"ref_check\":[WAIpok],\"consulted\":[WAIwld,WAIahd],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Avestan\",\"words\":\"vayôi, âvôya\",\"verdict\":\"confirmed\",\n\"derivation\":\"Young Avestan vayōi (also avōi) and āvōya are interjections 'woe!' (Bartholomae s.vv. avōi, āvōya: 'Interj. wehe!'), direct Iranian continuations of PIE *wáy (āvōya with prefixed ā-), cognate with Armenian vay.\",\n\"derivation_fa\":\"اوستایی نو vayōi (و avōi) و āvōya بانگ «وای!» هستند (بارتولومه: Interj. «wehe!») و بازماندهٔ مستقیم *wáy هندواروپایی‌اند؛ āvōya با پیشوند ā- ساخته شده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"وای\"],\"ref_check\":[WAIpok],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"BRT.txt l.5193 and l.7386\",\"stance\":\"supports\",\"note\":\"'avōi Interj. ‘wehe!’' and 'āvōya Interj. ‘wehe!’ ... np. vgl. āvah ‘wehe!’ — Vgl. avōi und vayōi'.\"},WAIwld]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"vây\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP vāy 'alas, woe' < MP way (MacKenzie 'way ... woe') < Proto-Iranian *wáy, the same interjection as Av. vayōi; Wiktionary gives Proto-Iranian *wáy < PIE *wáy. Not literally from the Avestan form, but from its Iranian sister, as the arrow intends.\",\n\"derivation_fa\":\"«وای» فارسی نو از فارسی میانهٔ way «وای، افسوس» و آن از ایرانی باستان *wáy است، همان بانگی که در اوستایی vayōi آمده؛ کشیدگی واکه در فارسی نو پدید آمده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"وای\"],\n\"ref_check\":[{\"ref\":\"BQT:2255\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:2255 (vol 4 pdf 338): 'وای ... و لفظی باشد که در محل آزاری و دردی [گویند]' — the interjection of pain; Mo'in's footnote not legible in OCR.\"}],\n\"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt l.5280\",\"stance\":\"supports\",\"note\":\"'way [wʾd | M wʾy] woe.'\"},\n {\"src\":\"MON\",\"where\":\"MON_part1.txt l.84118\",\"stance\":\"supports\",\"note\":\"'وای: (صت.) کلمه‌ای است دال بر: الف تألم و افسوس و اندوه'.\"},\n {\"src\":\"HRN\",\"where\":\"HRN.txt l.1731\",\"stance\":\"partial\",\"note\":\"Horn cites only 'kurd. hā, wāi' in passing; no separate vāy entry.\"}]},\n{\"id\":3,\"lang\":\"Germanic\",\"words\":\"wai\",\"verdict\":\"confirmed\",\n\"derivation\":\"Proto-Germanic *wai 'woe!' is attested as Gothic wai (also wai-nei 'would that'), ON vei, OHG wē, OE wā; a direct continuation of PIE *wáy.\",\n\"derivation_fa\":\"ژرمنی آغازین *wai «وای!» در گوتی wai، نوردی کهن vei، آلمانی علیای کهن wē و انگلیسی کهن wā آمده و بازماندهٔ مستقیم *wáy هندواروپایی است. ادعای نورایی درست است.\",\n\"sources\":[W+\"woe\"],\n\"ref_check\":[{\"ref\":\"KLN:1749\",\"status\":\"supports\",\"note\":\"KLN_1971.txt l.267987 s.v. woe: 'ME. wa, wo, fr. OE. wā ... Goth. wai, from the I.-E. imitative base *wai-, ‘woe’, whence also ... Avestic vayōi, ... L. vae'.\"},WAIpok],\n\"consulted\":[WAIahd,{\"src\":\"SKT\",\"where\":\"SKT.txt l.21597 s.v. Wo, Woe\",\"stance\":\"supports\",\"note\":\"'A.S. wā, interj. ... Goth. wai, interj.'\"}]},\n{\"id\":4,\"lang\":\"English\",\"words\":\"woe\",\"verdict\":\"confirmed\",\n\"derivation\":\"English woe < ME wo, wa < OE wā (interjection, later noun 'misery') < PGmc *wai; OE ā > ME ǭ > Mod. /oʊ/ by the regular southern rounding.\",\n\"derivation_fa\":\"انگلیسی woe از انگلیسی میانهٔ wo / wa و آن از انگلیسی کهن wā (نخست بانگ، سپس اسم «رنج») و ژرمنی *wai است؛ ā کهن در انگلیسی میانهٔ جنوبی به ō گرد شده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"woe\"],\n\"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference cited by Nourai for this node\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.267987\",\"stance\":\"supports\",\"note\":\"'woe ... ME. wa, wo, fr. OE. wā, ‘evil, suffering; woe’'.\"},{\"src\":\"SKT\",\"where\":\"SKT.txt l.21597\",\"stance\":\"supports\",\"note\":\"'Wo, Woo. (E.) M.E. wo; A.S. wā'.\"}]}]}\nentries.append(e3)\ne4={\"entry\":4,\"root\":\"W.a`.m\",\"verdict\":\"plausible\",\"modern_form\":\"Arabic root و ء م (w-ʔ-m) 'to agree, match'; comparative Semitic *tVʔ(V)m- 'twin'\",\n\"note\":\"Klein derives all the 'twin' words from Semitic w-ʾ-m 'to tally' (Arab. waʾama), and Arabic lexicography files tawʾam under w-ʔ-m. Comparative Semitists, however, reconstruct a noun *taʔm- 'twin' (Akk. tūʾamu, Heb. tᵉʾōm, Aram. tᵉʾōmā), with Arabic tawʾam probably reanalysed under w-ʔ-m; so the root is acceptable for Arabic but not proven as the source of the Aramaic/Syriac word.\",\n\"note_fa\":\"کلاین همهٔ واژه‌های «همزاد» را از ریشهٔ سامی و-أ-م «جور آمدن» (عربی وَأَمَ) می‌داند و لغت‌نویسان عرب نیز «توأم» را ذیل این ریشه آورده‌اند؛ اما سامی‌شناسان امروز بیشتر یک اسم کهن *taʔm- «همزاد» (اکدی tūʾamu، عبری tᵉʾōm، آرامی tᵉʾōmā) بازسازی می‌کنند که در عربی به ریشهٔ و-أ-م بازتحلیل شده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"توأم\"],\"ref_check\":[KLNthom],\n\"consulted\":[{\"src\":\"FVQ\",\"where\":\"FVQ_pages.txt grep 'tawʾam/Thomas'\",\"stance\":\"silent\",\"note\":\"Jeffery has no entry for tawʾam (not a Qurʾānic word).\"},{\"src\":\"MON\",\"where\":\"MON_part1.txt l.44606\",\"stance\":\"supports\",\"note\":\"'توأم [ع.] کودکی که با کودک دیگر در یک هنگام زاییده شده باشد؛ همزاد ...' — Arabic origin.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Arabic\",\"words\":\"taw`am\",\"verdict\":\"confirmed\",\n\"derivation\":\"Arabic تَوْأَم tawʔam 'twin; one of a pair' (pl. tawāʔim, dual tawʔamān), filed under root w-ʔ-m (waʔama 'to agree, match'); cognate with Akkadian tūʾamu, Hebrew tᵉʾōm, Syriac tᵉʾāmā.\",\n\"derivation_fa\":\"عربی «تَوْأَم» «همزاد، یکی از یک جفت» (جمع «تَوائِم»، مثنی «تَوْأَمان») ذیل ریشهٔ و-أ-م «جور آمدن» آمده و هم‌ریشه با اکدی tūʾamu و عبری tᵉʾōm است. ادعای نورایی درست است.\",\n\"sources\":[W+\"توأم\"],\"ref_check\":[KLNthom],\n\"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part1.txt l.44606\",\"stance\":\"supports\",\"note\":\"'توأم [ع.] ... همزاد؛ دوقلو. تث. توأمان'.\"},{\"src\":\"FVQ\",\"where\":\"grep tawʾam\",\"stance\":\"silent\",\"note\":\"no entry.\"}]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"tow`am; tow`amân\",\"verdict\":\"confirmed\",\n\"derivation\":\"Persian توأم towʔam 'twin; together with' and the Arabic dual توأمان towʔamān 'twins' are direct loans from Arabic tawʔam, tawʔamān; Persian aw > ow is the normal Tehrani pronunciation, and the sense 'accompanied by' (توأم با) is an internal Persian extension.\",\n\"derivation_fa\":\"«توأم» و «توأمان» در فارسی وام‌واژه‌های مستقیم عربی‌اند (تَوْأَم و مثنای آن تَوْأَمان)؛ معنای «همراه با» (توأم با) در خود فارسی گسترش یافته است. ادعای نورایی درست است.\",\n\"sources\":[W+\"توأم\"],\n\"ref_check\":[{\"ref\":\"MON:1159\",\"status\":\"supports\",\"note\":\"MON_part1.txt l.44606: 'توأم [ع.] (ص.) کودکی که با کودک دیگر در یک هنگام زاییده شده باشد ... دو چیز همراه'; next 'توأمان [ع.]'.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l.39088\",\"stance\":\"supports\",\"note\":\"'Arab. tauʾam, ‘twin’'.\"},{\"src\":\"BQT\",\"where\":\"BQT_v1/v2 grep 'توأم'\",\"stance\":\"silent\",\"note\":\"Arabic word not entered in Borhan.\"}]},\n{\"id\":3,\"lang\":\"Syriac\",\"words\":\"tômâ\",\"verdict\":\"confirmed\",\n\"derivation\":\"Syriac ܬܐܘܡܐ tᵉʾōmā / tōmā 'twin' (Aramaic tᵉʾōmā), the Semitic 'twin' noun with loss of the glottal stop; it was the epithet of the apostle Judas 'Thomas', glossed in John 11:16 as Δίδυμος 'twin'.\",\n\"derivation_fa\":\"سریانی tᵉʾōmā / tōmā «همزاد» (آرامی tᵉʾōmā) همان اسم سامی «همزاد» است با افتادن همزه؛ این لقب حواری توماس بود که در انجیل یوحنا به یونانی «دیدوموس» (همزاد) ترجمه شده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"Thomas\",W+\"توأم\"],\"ref_check\":[KLNthom],\n\"consulted\":[{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt l.35945\",\"stance\":\"supports\",\"note\":\"'Thomas, who is called Didymus, John' — Greek gloss 'twin'.\"},{\"src\":\"FVQ\",\"where\":\"grep\",\"stance\":\"silent\",\"note\":\"no entry.\"}]},\n{\"id\":4,\"lang\":\"Greek\",\"words\":\"tomas\",\"verdict\":\"confirmed\",\n\"derivation\":\"New Testament Greek Θωμᾶς (Thōmâs) transcribes Aramaic tᵉʾōmā with the Greek masculine -ς ending; the chart's 'tomas' is a simplified romanization of Thōmâs, not a different form.\",\n\"derivation_fa\":\"یونانی عهد جدید Θωμᾶς (Thōmâs) آوانویسی آرامی tᵉʾōmā با پایانهٔ مذکر -s یونانی است؛ «tomas» در نمودار تنها آوانویسی ساده‌شدهٔ آن است. ادعای نورایی درست است.\",\n\"sources\":[W+\"Thomas\"],\"ref_check\":[KLNthom],\n\"consulted\":[{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt l.35945\",\"stance\":\"supports\",\"note\":\"Thomas = Didymus.\"},{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l.39088\",\"stance\":\"supports\",\"note\":\"'fr. Gk. Θωμᾶς, lit. ‘twin’'.\"}]},\n{\"id\":5,\"lang\":\"English\",\"words\":\"Thomas, Tom\",\"verdict\":\"confirmed\",\n\"derivation\":\"English Thomas < ME Thomas < Ecclesiastical Latin Thōmās (Vulgate) < Greek Θωμᾶς; the chart omits the Latin/French stage. Tom is the English hypocoristic short form (from ME times).\",\n\"derivation_fa\":\"انگلیسی Thomas از انگلیسی میانه و لاتین کلیسایی Thōmās (ولگاتا) و آن از یونانی Θωμᾶς است؛ نمودار مرحلهٔ لاتین را نیاورده است. Tom شکل کوتاه‌شدهٔ خودمانی آن است. ادعای نورایی درست است.\",\n\"sources\":[W+\"Thomas\"],\"ref_check\":[KLNthom],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l.39088\",\"stance\":\"supports\",\"note\":\"'Thomas, masc. PN. — Eccles. L., fr. Gk. Θωμᾶς'.\"},{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt l.35945\",\"stance\":\"partial\",\"note\":\"mentions Thomas only in the Didymus citation.\"}]}]}\nentries.append(e4)\nout={\"pdf_page\":525,\"book_page\":495,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":entries}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-525.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-525.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-525.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 525",
 "description": "Write verification JSON and run checker"
}
```


### [2026-10-16T05:18:24.109Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'disputed': 1, 'confirmed': 11, 'plausible': 1}
root verdicts: {'plausible': 2, 'confirmed': 1}
ref checks: {'supports': 12, 'partial': 4, 'not_checked': 1}
books consulted: {'contradicts': 1, 'silent': 8, 'partial': 5, 'supports': 14} | by book: {'SKT': 5, 'WLD': 4, 'KLN': 4, 'MON': 3, 'AHD': 3, 'HRN': 2, 'PHD': 2, 'FVQ': 2, 'POK': 1, 'BRT': 1, 'BQT': 1}
```


## [2026-10-16T05:18:36.996Z] TOOL CALL #45: SubagentHandback

```json
{
 "message": "I verified page 525 (book page 495) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-525.json. The JSON is valid and `verify_check.py 525` shows 0 PROBLEM lines, with all 13 of 13 nodes done. Entries 0 (Wâ) and 1 (Wag) are redirects, so I skipped them.\n\n**Verdicts**\n- Nodes: 11 confirmed, 1 plausible, 1 disputed.\n- Roots: Wai is confirmed. Wag 2/Gwag and W.a`.m are plausible.\n\n**Disputed**\n- Wag 2/Gwag, #1 Persian žâž; zâğ; zakîdan:\n  - **žâž:** Mo'in and Borhan say ژاژ is first the name of a tasteless herb that camels chew. \"Idle talk\" is a figure of speech from ژاژ خاییدن (\"to chew žâž\"), so it is not a sound-imitating word from *gʷag-. Mann, the source Nourai follows, only marks it \"cf.\".\n  - **zâğ:** the link to *gʷeguos is only plausible.\n  - **zakîdan:** I found no etymology for it in any source.\n\n**Plausible (worth knowing)**\n- **Wag 2/Gwag root:** the box merges two roots. One is Pokorny's u̯āg- \"cry\", which covers Sanskrit vagnu and Latin vāgiō. The other is Mann's gʷag-/gʷeguos, where the Persian and Greek words come from. Sanskrit v- cannot come from *gʷ-.\n- **Greek bazô:** Wiktionary calls it probably sound-imitating. Pokorny does not list it under this root.\n- **W.a`.m root:** Klein and the Arabic dictionaries put tawʾam under w-ʾ-m. Semitic scholars instead reconstruct an old noun *taʔm- \"twin\" that Arabic later re-filed under w-ʾ-m.\n\n**Transcription:** none flagged, and the extraction matches the chart. The Greek \"tomas\" is a simplified spelling of Θωμᾶς, not an error.\n\n**Gap:** Borhan p.1057 has no page scan on disk. I matched it from the OCR text, where leaf 519 has the ژاژ entry with the same Farrokhi verse Nourai quotes."
}
```


### [2026-10-16T05:18:37.265Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
