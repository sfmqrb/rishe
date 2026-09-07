# Verification process log — verify-page-369


## [2026-09-07T20:14:47.695Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 369 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-369.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-369.json. Write /home/sfmqrb/git/rishe/data/verification/page-369.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 369` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:14:50.159Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:14:50.869Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:14:50.897Z] TOOL RESULT

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


## [2026-09-07T20:14:51.353Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-369.txt"
}
```


### [2026-09-07T20:14:51.384Z] TOOL RESULT

```
1	=== PDF page 369 (book page 339) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nogw : naked  (refs POK:769)
4	#1 (parent #0) [Avestan] refs=POK:769; KLN:1026; SYN:325 | mağnâ : naked | NOTE: See "Bŭnai: naked" for another possible root
5	  #2 (parent #1) [Pahlavi] refs=ISS:256 | brahnak : naked
6	    #3 (parent #2) [Persian] refs=ISS:256; MON:517 | berehneh «برهنه» : naked | NOTE: See "Bŭnai: naked" for another possible root.
7	#4 (parent #0) [Germanic] refs=AHD | nakw-eda
8	  #5 (parent #4) [English] refs=None | naked
9	#6 (parent #0) [Latin] refs=AHD | nudus : naked
10	  #7 (parent #6) [English] refs=None | nude
11	#8 (parent #0) [Indo-European] refs=IEC:364 | Gumnos, Gunos : beautiful, naked
12	  #9 (parent #8) [Persian] refs=IEC:364; MON:4760 | na-ğâm «نغام» : not beautiful, ugly ☞Ne 1
13	  #10 (parent #8) [Latin] refs=IEC:364 | vinnus : wanton
14	  #11 (parent #8) [Greek] refs=AHD | gumnos : naked ; gumnazein : to train naked
15	    #12 (parent #11) [French] refs=None | 
16	      #13 (parent #12) [Persian] refs=MON:1779 | žimnâstîk «ژیمناستیک» : gymnastics
17	    #14 (parent #11) [English] refs=None | gymnasium, gymnastics, gym
18	--- entry 1 ---
19	ROOT [Indo-European] Noktis, Nekw, Nekwt : night  (refs POK:762; AHD:1530; IEC:850; SYN:992)
20	#1 (parent #0) [Old Persian] refs=IEC:850 | naktin : night
21	#2 (parent #0) [Sanskrit] refs=IEC:850; KLN:1047 | naktih : night ; naktam : at night
22	#3 (parent #0) [Germanic] refs=POK:762 | naht : night
23	  #4 (parent #3) [English] refs=KLN:1047; AHD | night, nightingale
24	#5 (parent #0) [Latin] refs=POK:762 | nox, nocht : night ; noctua : night owl
25	  #6 (parent #5) [English] refs=AHD | nocti-, nocturnal, noctule
26	#7 (parent #0) [Greek] refs=POK:762 | nux, nukti : night
27	  #8 (parent #7) [English] refs=AHD | nyctalopia
28	--- entry 2 ---
29	ROOT Nokut -> redirect to Neku
30	
```


## [2026-09-07T20:16:06.097Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-369.json | head -200",
 "description": "Read source JSON for page 369"
}
```


## [2026-09-07T20:16:06.801Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:16:07.512Z] TOOL RESULT

```
{
    "pdf_page": 369,
    "book_page": 339,
    "entries": [
        {
            "root": {
                "name": "Nogw",
                "lang": "Indo-European",
                "refs": "POK:769",
                "gloss": "naked"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:769; KLN:1026; SYN:325",
                    "words": [
                        {
                            "translit": "ma\u011fn\u00e2",
                            "gloss": "naked",
                            "script": null
                        }
                    ],
                    "note": "See \"B\u016dnai: naked\" for another possible root",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "ISS:256",
                    "words": [
                        {
                            "translit": "brahnak",
                            "gloss": "naked",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "ISS:256; MON:517",
                    "words": [
                        {
                            "translit": "berehneh",
                            "gloss": "naked",
                            "script": "\u0628\u0631\u0647\u0646\u0647"
                        }
                    ],
                    "note": "See \"B\u016dnai: naked\" for another possible root.",
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nakw-eda",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "naked",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nudus",
                            "gloss": "naked",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "nude",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "IEC:364",
                    "words": [
                        {
                            "translit": "Gumnos, Gunos",
                            "gloss": "beautiful, naked",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Persian",
                    "refs": "IEC:364; MON:4760",
                    "words": [
                        {
                            "translit": "na-\u011f\u00e2m",
                            "gloss": "not beautiful, ugly",
                            "script": "\u0646\u063a\u0627\u0645",
                            "see": [
                                "Ne 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0648\u0646 \u0635\u0648\u0631\u062a \u0648 \u06a9\u0627\u0631 \u062f\u06cc\u0648 \u0631\u0627 \u062f\u06cc\u062f\u06cc - \u0628\u06af\u0630\u0627\u0631 \u0637\u0631\u06cc\u0642\u062a \u0646\u063a\u0627\u0645\u0634 \u0631\u0627",
                        "poet": "N\u00e2ser-Khosrow"
                    }
                },
                {
                    "id": 10,
                    "parent": 8,
                    "lang": "Latin",
                    "refs": "IEC:364",
                    "words": [
                        {
                            "translit": "vinnus",
                            "gloss": "wanton",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 8,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "gumnos",
                            "gloss": "naked",
                            "script": null
                        },
                        {
                            "translit": "gumnazein",
                            "gloss": "to train naked",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
```


### [2026-09-07T20:16:07.546Z] TOOL RESULT

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


## [2026-09-07T20:16:40.120Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-369.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-07T20:16:41.646Z] TOOL RESULT

```
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "MON:1779",
                    "words": [
                        {
                            "translit": "\u017eimn\u00e2st\u00eek",
                            "gloss": "gymnastics",
                            "script": "\u0698\u06cc\u0645\u0646\u0627\u0633\u062a\u06cc\u06a9"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 11,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "gymnasium, gymnastics, gym",
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
                "name": "Noktis, Nekw, Nekwt",
                "lang": "Indo-European",
                "refs": "POK:762; AHD:1530; IEC:850; SYN:992",
                "gloss": "night"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "IEC:850",
                    "words": [
                        {
                            "translit": "naktin",
                            "gloss": "night",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "IEC:850; KLN:1047",
                    "words": [
                        {
                            "translit": "naktih",
                            "gloss": "night",
                            "script": null
                        },
                        {
                            "translit": "naktam",
                            "gloss": "at night",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "POK:762",
                    "words": [
                        {
                            "translit": "naht",
                            "gloss": "night",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": "KLN:1047; AHD",
                    "words": [
                        {
                            "translit": "night, nightingale",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "POK:762",
                    "words": [
                        {
                            "translit": "nox, nocht",
                            "gloss": "night",
                            "script": null
                        },
                        {
                            "translit": "noctua",
                            "gloss": "night owl",
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
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nocti-, nocturnal, noctule",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "POK:762",
                    "words": [
                        {
                            "translit": "nux, nukti",
                            "gloss": "night",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "nyctalopia",
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
                "name": "Nokut",
                "redirect": "Neku"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-07T20:16:42.751Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','SYN','ISS','MON','AHD','IEC','BRT','PHD','NYB','HRN','HUB','WLD','LEW','LAT','SKT','SOD','ARY','BQT','CHEUNG']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Ref metadata"
}
```


### [2026-09-07T20:16:44.130Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file ha
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== CHEUNG null
```


## [2026-09-07T20:16:49.657Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; grep -n \"maγna\\|magna- 'nackt'\\|nog[ʷw]-\" POK_full.txt | head -30",
 "description": "Grep Pokorny for nogw root"
}
```


### [2026-09-07T20:16:49.708Z] TOOL RESULT

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
---
```


## [2026-09-07T20:16:51.038Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -c \"\" $f; awk 'BEGIN{RS=\"\\f\"} {n++} END{print \"pages:\",n}' $f; done",
 "description": "POK file sizes"
}
```


### [2026-09-07T20:16:52.400Z] TOOL RESULT

```
== POK_01.txt
5152
pages: 363
== POK_02.txt
6716
pages: 433
== POK_03.txt
5975
pages: 429
== POK_full.txt
93771
pages: 1
```


## [2026-09-07T20:18:08.732Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nogᵘ\\|nogu̯\\|nackt\" POK_02.txt | head -40; echo \"=== full\"; grep -n -i \"nackt\" POK_full.txt | head -20",
 "description": "Grep nackt in Pokorny"
}
```


### [2026-09-07T20:18:08.787Z] TOOL RESULT

```
13:I.  gal-  ,kahl,  nackt';    mit   u-Erweiterung:  Adjekt.  galuo-s,  Subst.  galuä.
16:akl.  goh  , nackt',  sloven.  gbi,  russ.  göiyi  ,kahl,  nackt',  cech.  holp  ds., holek  , bartloser  Bursche',  holka  ,Mädchen',  usw. ;  dazu  ksl.  golotb  f.  ,Eis', cech.  holoty  russ.  göioh  f.  , Glatteis';
4218:koi-lo-  ,kümmerlich,  nackt^;  nur  kelt.  und  halt.
4219:Air.  cöil,  cöel  ,dünn,  schmal',  cymr.  corn.  cid  ,macilentus,  macer'; lett.  kails  ,nackt,  kahl,  bloß',  kaili  laudis  ,Ehepaar  ohne  Kinder'  (könnte auch  zu  kai-  ,allein'  gehören). WP.  I  326,  455,  WH.  I  130.
5127:gr.  Xelixa^  , nackte  Schnecke'  (daraus  lat.  llmäx  ds.)  =  russ.  slimdk  m. , Schnecke';  vgl.  apr.  slayx  m.,  lit.  sliekas  m.,  lett.  slieka  f.  ,Regenwurm' und  lett.  sliekas  f.  Fl.  , Speichel';  vielleicht  auch  lit.  seiles,  lett.  seilas  f. PI.  , Speichel'  (aus  ^sleiläs?).
5307:alb.  lakur  .nackt',  lekure,  likure  .Fell,  Leder.  Baumrinde.  Schote' ;
5593:unklar  ist  der  Labial  (b,  bh  oder  p)  in  mir.  luchtar  ,Boot'  (aus  Rinde), 5lid.  lo(ii')fl  ,Ria(ie;  Bast',  aisl.  lopt  n.  , Zimmerdecke,  Dachstube'  und Luft'  (,Himmel  als  obere  Decke'),  got.  luftus  f.,  ahd.  as.  Ivft  m.  f.,  ags. Itjft  m.  f.  n-  >^^flf  Himmel',  mnd.  lucht  , Oberstock,  Bodenraum';  ebenso anklar  in  air.  lomm,  cymr.  llwm  ,bloß,  nackt'  {Hup-smo-  oder  Hub(h)-smo-), mir.  lommraim  , schäle' 5  unklar  ist  nair.  lumman  ,covering'. WP.  II  417  f.,  WH.  I  790  f.,  Trautmann  150  f.
=== full
63078:English nacod. Old High German nackut, nachut. Modern High German nackt. Old Irish 
68444:bald head, nackte Ebene', p/eT/<e^ baldness ', p//n/<u, p/'i/<t/' baldheaded become'
```


## [2026-09-07T20:18:12.715Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63040,63110p' POK_full.txt",
 "description": "Read POK_full nogw entry"
}
```


### [2026-09-07T20:18:12.765Z] TOOL RESULT

```
See also: probably as "the winding, turning ', to root (s)ne-. 

Page(s): 767 

Root / lemma: /?/-, nei- i*he- nei-) 
See also: see above S. 312 f. {en-). 
Page(s): 767 

Root / lemma: niz-do- {*he- niz-do-) 
Meaning: nest' 
See also: see below sed-. 
Page(s): 769 

Root / lemma: nog^o- or nag^o- {*he- nag^o-) 

Meaning: tree 

Material: Old Indie naga-m. "tree, mountain'; Old Icelandic ngkku/m., Old High German 

nahho. Old Saxon naco. Old English naca^ bark, type of sailboat, dugout canoe'. 

References: WP. II 340. 

Page(s): 770 

Root / lemma: nog"-, nog''od(h)o- nog^-no- {*he- neg^o^ 

Meaning: naked 

Note: often distorted taboo 

Material: Old Norse nokkva " make naked '; lengthened grade Lithuanian nuogas, Latvian 

dial, nuogs. Old Church Slavic nagi^ "naked'; 

with dental formants: Latin /7/7o'^s "naked' from * nog"ed(h)os or *nog"od(h)os= Gothic 
naqat^s{-d-). Old Norse n0kkuidr{a\so ngkti), next to which Old Swedish nakut^er. Old 
English nacod. Old High German nackut, nachut. Modern High German nackt. Old Irish 
nocht, cymr. etc. /7c»e//7" naked' {*nog"-to-s)\ (common alb. Celtic -kt > -th, -gt > -dh) 

with formants -no-:0\6 Indie nagna-^ naked', Avestan mayna-6s. (/77- through 
dissimilation, the initial grade of westosset. baynay); Armenian merk^nake6'; hieher also 



gr. YUMv6(;, by Hes. Aupv6(; (for *vu|jv6(;) and anoAuY|JaTO(; anoYUiJvwaK;. Kunpioi; Old 
Icelandic nakinn. Old Frisian /75/re/7 "naked' (/rinstead of nord. /r^ point to metathesis from 
*nak{u)-na- after the participle in -inn); Hittite neku-manza ^ naked' . 

Comments: 

Root/ lemma: nog''-, nog''od(h)o-, nog^-no-. naked > Root/ lemma: lek-2. lak-\ to tear, 

fell, fur, leather, bark, outer covering of a tree, pod 

Maybe alb. {*naku-n-os) lakun'q^ naked', lekure^ skin, naked skin', lakun'q^ bat, hanging 

skin ' : Greek Aupvoi; (for *vumv6i;) (common Baltic Hittite n- > l-= alb. Greek n- > /-) See 

Lithuanian //ekuot/ds., Latvian //ie Asa "winnowing shovel' Root/ lemma: nei'k-: "to winnow 

grain'. 

References: WP. II 339 f., WH. II 185, Trautmann 201, Specht Indo Germanic Dekl. 251. 

Page(s): 769 

Root / lemma: nok^-(t)- {*he- nek^-Ct)-) 
See also: s. nek"-(t)-. 
Page(s): 770
```


## [2026-09-07T20:18:19.805Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nek\\\"-(t)-\\|Nacht'\" POK_full.txt | head -20",
 "description": "Grep Pokorny night root"
}
```


### [2026-09-07T20:18:19.855Z] TOOL RESULT

```
63109:See also: s. nek"-(t)-.
```


## [2026-09-07T20:18:23.329Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 762\" POK_full.txt | head; echo ---; grep -n \"night'\" POK_full.txt | head -20",
 "description": "Find Pokorny page 762"
}
```


### [2026-09-07T20:18:23.388Z] TOOL RESULT

```
62331:Page(s): 762 
62398:Page(s): 762-763 
---
7345:the night, night's rest, station '. 
7348:Inf. aF£a(a)ai; quAk;, -xboo, ' place of residence, camp, stable, night's lodging ', auAi^oijai " 
8821:or night ' besides there is />stem Old Danish d0gnn. "day and night'. 
19342:npers. o'ds "the former yesterday night'; 
26351:Old Icelandic n/f/-he/mrbe\o\N likewise, /t/o/' darkness, night' (Germanic *neb/a-an6 
29364:"cloudy, stormy night', as hom. opcpvair) vu^; 
62341:Root/ lemma: nek^-ft-), nok^-t-si* hounk''-(t-))\ night' derived from zero grade of Root/ 
62343:lemma: ong^-Ao anoint, dark ointment' : Old Indie akta- [f] 'night' (RV 01 .062.08) {2}; aktu- 
62345:[m] 'flowing; ointment; (light or dark) color; (final part of the) night' (RV+) {3}. 
62347:Material: Old Indie nak{*nakt) Nom. 'night' {nagjihTte), naktai. Du., naktam My. solidified 
62353:gr. vu^, vukt6(; f. "night', in compound vukti-, vukto-, vuktojp Adv. " at night, by night ' 
62356:lasting the whole night ', auTOvuxi "in the same night'; 
62358:alb. nate, /7e/e PI. "night'; 
62360:Maybe alb. per-nate^ every night' : mcymr. peu-noeth^e^ch night'. 
62362:Latin nox, /70c//5 "night' (Gen. PI. noct/um /-stem, but distinct conservative stem in Adv. 
62364:vuKTOjp); of stem *noktu-. Latin noctu^by night', noctua^ a night-owl, an owl '; 
62368:henoz6s.\ cymr. corn, nos, bret. /7c»z "night', probably from *nokf-s u- cymr. neithiwyr, 
62369:neithwyr{cov\{a\v\s /7tyj//' "evening') "last night', corn. /7e/7^es Middle Breton neyzor, nbr. 
62373:Old Saxon naht. Old English neaht, /7//7/"night' (conservative stem). Old English nihterne^ 
62377:Sg.) "night', nakftjv-yne ^n\ghthosie\', nakftjvot/ ^\odge, stay ovevnight' , nakv/nas' accommodate
```


## [2026-09-07T20:18:26.305Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62330,62400p' POK_full.txt",
 "description": "Read Pokorny night entry"
}
```


### [2026-09-07T20:18:26.356Z] TOOL RESULT

```
Page(s): 762 

Root / lemma: nelc-fl-), nolc-t-s {* hounk'*-(t-}) 

Meaning: night 

Grammatical information: stem nok'i-i. (originally neutr.??), nok'ii-, nok'iu-i., nok'i(e)ru. 

Note: about ablaut forms see below 

Root/ lemma: nek^-ft-), nok^-t-si* hounk''-(t-))\ night' derived from zero grade of Root/ 

lemma: ong^-Ao anoint, dark ointment' : Old Indie akta- [f] 'night' (RV 01 .062.08) {2}; aktu- 

[m] 'flowing; ointment; (light or dark) color; (final part of the) night' (RV+) {3}. 

Material: Old Indie nak{*nakt) Nom. 'night' {nagjihTte), naktai. Du., naktam My. solidified 

Akk. ' at night ', Instr. PI. naktabhih 6s. (imitation from ahabhih), Akk. PI. naktJh^ nights '; 



gr. vu^, vukt6(; f. "night', in compound vukti-, vukto-, vuktojp Adv. " at night, by night ' 
(*Akk. shaped as u5u)p), vuKT£p6(;, vuKT£piv6(; " nocturnal ' (: Latin nocturnus); unclear are 
vuxa vuKTOjp Hes., horn. £ivavux£<; " nine nights through ', £vvuxo(; " nocturnal ', navvuxiO(; " 
lasting the whole night ', auTOvuxi "in the same night'; 

alb. nate, /7e/e PI. "night'; 

Maybe alb. per-nate^ every night' : mcymr. peu-noeth^e^ch night'. 

Latin nox, /70c//5 "night' (Gen. PI. noct/um /-stem, but distinct conservative stem in Adv. 
nox' at night, by night ' from Gen. *nokt-es, -os)\ nocturnus " nocturnal ' (: vuKT£piv6(;, 
vuKTOjp); of stem *noktu-. Latin noctu^by night', noctua^ a night-owl, an owl '; 

Old Irish i-nnochV hac nocte ', mcymr. peu-noeth' each night ', trannoeth^ during the 
following day ', acymr. henoid, cymr. he-no^ hac nocte ', corn, haneth. Middle Breton 
henoz6s.\ cymr. corn, nos, bret. /7c»z "night', probably from *nokf-s u- cymr. neithiwyr, 
neithwyr{cov\{a\v\s /7tyj//' "evening') "last night', corn. /7e/7^es Middle Breton neyzor, nbr. 
neizeur(is.\ 

Gothic naMs {Dat. PI. nahtam after dagam). Old Icelandic nott, natt. Old High German 
Old Saxon naht. Old English neaht, /7//7/"night' (conservative stem). Old English nihterne^ 
nocturnal '; 

Lithuanian /7a/r//s (conservative Gen. PI. naktu), Latvian nakts. Old Prussian nakt/'n {Akk. 
Sg.) "night', nakftjv-yne ^n\ghthosie\', nakftjvot/ ^\odge, stay ovevnight' , nakv/nas' accommodate 
for the night'. Old Bulgarian /7c»s/i. "night', russ. netopyr Nachtschmetterling, bat'; 

Hittite neku-' dawn'; Gen. ne-ku-uz {nekuz) "night'; Tocharian A n[a]ktim^ nocturnal ', B 
nekciye " the evening, during the early nighttime hours '; 

zero grade: Old Indie 5/r/a"night' (perhaps /7-stem), aktu-m. " darkness, night, light, ray' 
(actually "dawn, twilight'), compare in latter meaning Gothic uhtwd{: Latin noctu etc.), Old 
Icelandic ofta. Old High German Ohta{uohta), Middle High German uhte{uohte). Old 
Saxon uthai.. Old English uth(a)xr\. " early morning time ', Gothic uhteigs' early '; 

another ablaut grade *onk"t- seems Lithuanian anksti " early, matutinal ', is anksto " from 
early on ', ankstus M]. "early, matutinal'. Old Prussian angstainai, angsteina Mn . " early in 
the morning '. 



References: WP. II 337 ff., WH. II 181 ff., Trautmann 9, 193, Specht Indo Germanic Dekl. 

11. 

Page(s): 762-763 

Root / lemma: ne1, ne, nei{*houn)
```


## [2026-09-07T20:18:34.182Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==441' IEC.txt | head -80",
 "description": "Read IEC leaf 440"
}
```


### [2026-09-07T20:18:35.547Z] TOOL RESULT

```
h Go. móbps, m. “anger, courage; MHG muot, sm ‘strength, courage, joy, mood, intent; OE mod, n. (heart, mind’; adj. /harmonious); Du. moed, m. (courage
mogh- (radical element of the following en- tries) “large, powerful, heavy”, etc. (The Skt. forms are ambig. in view of Iranian equivalents of type *maz-). Cf. maháh “big, strong’; compar. mahiyas, superl. mahistha, but cf. Vedic maham, n. ‘great deed, exploit’: Av mayom, n. ‘greatness’, and Skt. mahán, n. ‘greatness: OE mægen, n. ‘strength; feat; force’; Skt. máhas, n. ‘greatness, glory’; ma- hát, pres. pt. ‘strong; great: Olr. mochta ‘mighty’; Go. mahts, etc The velar is explicit in Skt. maghám, n. ‘reward, bounty; OHG mag ‘I can, may’, and OCS mogọ, id. Cf. also OCS moštij ‘worse’. (Speculations on Go. mais, maiza ‘more’; OHG mēro, ON meiri, id. in SF: VWGS: mais)
moghdheio (moghidheio, -dhàio) ‘torture; toil, suffer’. (Sl. ambig. cf. maghido) Gk. mokhthéo ‘toil, suffer’; Lat. moereo, ere, supine: moestum ('grieve' if for *moghid- or *moghidh-, cf. meridies (*med-); merx
modhoros (modhuros) — moghnos (moghinos), om
20
25
30
35
40
45
784
(*medh- Ou: OCS cf. po-mozdajo, tr. ‘weaken’
moghənt- (moghnt-) ‘big, great strong’. (The velar consonant is represented in Av. mayom ‘greatness’, and is explicit in Skt. maghám *reward'") Skt. mahát ‘great; greatness’; Av. cf. mazafit, id. (w. secondary palatalism?); Tokh. mokats ‘strong’; Lat. prob. mons, gs montis, gp mon- tium, m. “mountain; mass, quantity” (but cf. Av. matis 'cliff, peak' for possible variant *mnt-. For Olr. mét, melt, f. ‘size, greatness’; Ir. méid, m & f ‘quantum’; OW meint, f., W maint, m. amount, size, quantity’; Br. ment, mend, f. id.; OBrit. pa-mint “how much cf. megont- ‘quantity’ above); OFris. magande “mighty, able’; ON megandi, id.; OCS mogoti, mogosti, m. ‘master; Cz. cf. mohutny ‘mighty’; v$e-mohoucí ‘almighty’; R mogücij ‘powerful’; Srb. moguć possible; wealthy; powerful. Cf. WP II, 238 & 257
moghotos, à, is “strong; strength’. (Variant of type moghtis, q. v.) Gaul. cf. mageto-, mogeti- (in names); Ir. cf. mocht ‘large’; mochta, pp 'enlarged'; Olr. mochta & mogda, id. (and *mighty'); R mogo- tà “strength, force’.
moghlos, ios, iə ‘grip, firmness; clamp, bolt, mainstay'. Cf. WP II, 692 Arm. magil, gs magli, ab. sg. -av “clutch, claw, fang; Gk. mokhlós, m. ‘bolt, bar’; mokhlía *dislodgment'; Ir. mogall, m. “mesh; globe, cluster’; Li. magliai, mpl. “mangle, wringer
moghnos (moghinos), om strong, big; strength, size, ability’. WP II, 227 Skt. cf. mahán, n. greatness’. See note on mogh- above); cf. magháh “wealth, power: Av. mayom, n. ‘greatness’; Gk. cf. mos-sün, & -sünos, m. ('tower, scaffold, erection’, if fr. *mogh-dün-, see dünos); OLat. cf. moene, n. "wall: Lt. moenia, npl. ‘city walls; Olr. maigne, adj. ‘mighty’ beside MIr. mog, mogh, adj. ‘big; Cor. men ‘strong, able; OHG ma- gan, n. ‘strength, virtue’; OE mægen ‘might, prowess’; ON megn, adj. ‘strong’; magn, n. as OHG & OE (cf. Eng. “might and main"); OCS cf. moZenije, n. “power? beside R (and com. Sl.) moZnyj “possible?
785
moghó, moghmi “am able, can’. WP II, 227. Cf. radical: mogh- above Skt. cf. magháh *wealth, power'; Av. mayom, n. ‘greatness, feat; MIr. mog, mogh, adj. ‘big’; Ir. mogh, id. and m. ‘size’; OE maga, w. adj. ‘powerful, able, rich? beside defective vb. mæg; Go. OHG mag ʻI can, may’; OCS (and com. Sl.) mogọ ‘I can’; cf. ne-mogy, adj. ‘im- possible’; R cf. pod-moga, f. ‘sustenance’
(moghs, possible analysis of type moks, q. v.)
moghtis ‘power’. See moghət- and radical mogh-. WP II, 227 Olr. cf. mochta, mogda, adj. ‘migh
```


## [2026-09-07T20:18:41.605Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"noktis\\|nokts\\|noktu\" IEC.txt | head -20; echo \"=== gumnos/gunos\"; grep -n \"gumnos\\|gunos\\|vinnus\" IEC.txt | head -20",
 "description": "Grep IEC for noktis and gumnos"
}
```


### [2026-09-07T20:18:41.673Z] TOOL RESULT

```
8202:ksitis, à ‘damage, destruction’. Cf. ksipt- Skt. ksitih, f. (3) ‘ruin, destruction’; EMAIb. & Alb. (ambig.) shitë, f. wound, blow, paraly- sis'. See ksipt-); W cid, pl. Aan. m. ‘havoc? beside cis, pl. -ion, m. ('slap, blow”, fr. *ksits, cf. nos fr. *nokts)
8822:Kiā-noktei, -nokt ‘tonight, last night. Cf. Kia, nokts Alb. sonte ‘tonight’; Venetic (queried) sahna- teh ‘today’; OHG, MHG hinaht “tonight, last night’; G heint, id.; OCS si nošči, Srb. sinoć, OCz s nóci, Ukr. s-nocy; Li. šonakt, id. Cf. WP I, 453
11607:nekt- (?) ‘evening (progressive aspect with vowel *-e- as against terminal aspect of type noktis, q.v. with vowel *-o-) Skt. (ambig.) náktam, n. ‘night’; Hitt. nekuc, gs. id. “evening, nightfall'; OCS cf. neto- in netopyrí, m. Chat, zool.)
11823:nokterinos ‘nightly’. See noktis & nokts. WP II, 317 Gk. cf. nukterinós ‘nocturnal’; Lat. cf. noctur- nus, id.; OE nihterne, id.
11824:noktím ‘by night, at night, yesterday night. Cf. nokts, noktis Skt. náktam id.; Tokh. A noktin “in the even- ing; MHG nehten “last night; OPr. naktin ‘by night; Li. nákti, id.
11825:noktis, nokts ‘night (ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti, v. ‘spend the night, with an echo in Hitt. nekuc “evening, night- fall’, e-gde indicating the approach to night, as also in Tokh. B nekciye “in the evening, For a possible u-affection in Gk. cf. püksis under poks- below, and híppos (?); -u- and -i- for *-o- & *-e-. The i-stem seems to denote ‘night when counted; the consonantal form a familiar entity, as in Lat. vox, dux, lex, sol ‘the voice’ etc. I-stem in Skt. (Vedic) náktih, f.; Ober naktin, acc. sg.; Tokh. noktin and niktin ‘toward evening’; Lat. nox, gp noctium, but OLat. nox ‘by night; Ir. a nocht, in nocht 'to- night; W nôs, Br. noz, pl. nosiu, f.; Cor. nos; OCS oos Cz. noc, npl. noci; Latv. nakts, gp: nakéu. Cons.stem in Vedic nak, m.; Gk. nux; Alb. natë, pl: net; cf. nádje “in the morn- ing; Go. nahts £.; OHG naht, npl. id., gp: nahto; OE niht (fr. *nekt- or *nequt-); ON. nátt, nótt; Cz. veliko-noce, pl. (great nights? = *Easter); Li. naktis, gp naktü. Cf. also Go.
11850:(noqu-, ultimate theme of type *noktis, *nokts, q. v. and cf. nqu-, nqut- Cf. Hitt. nekuc-; Gk. nukheüo “watch through the night; nukhth-émeron, n. "a day and a night', and the vocalism of nüx 'night'; Li. nakvinti, inf. “put up for the night; nakvyne *night's lodging")
11935:nqu-, nqut-, noqu-, nequ-. Presumed radical background for type *nokts, *noktis q. v. Skt. ambig. Cf. Skt. aktüb, m. ‘darkness’; aktàu ‘by night’; Vedic aktā ‘night; Go. ühtwo, OHG ühta, OE üht, ühte, OS ühta, MHG uhte, uohte, f. ‘daybreak, dawn, dusk’. For other indications of labialism cf. Gk. núkha “by night beside nukhth-émeron ‘twenty-four hour period: Hitt. nekuc 'nightfalP and Lat. noctu ‘by night ; Li. nakvinti, v. ‘put up, lodge’; nakvóti, v. inf. ‘spend the night
12750:per-nokt- ‘overnight. Cf. per-, nokts (noktis) Alb. cf. (archaic) pér-nátet, v. 3s. ‘grows dark’; pér-nata, -naté, adv. (ambig. *per- or *pro-: “by night); Lat. cf. per-nocto, äre, f. spend
13327:poksos, is, ios, üs ^wing, side, flank, wall, partition, pigeon-hole'. WP II, 3 Skt. paksáb, m. “wing, side, half, party’; Oss. faxs, pl. fäxstä ‘side’ beside fáxs ‘strip, board’; Gk. puxís, gs: -idos, f. (box. Vocalism as nüx, see noktis above); Myc. cf. pukso(1) (parts of a table, perh. *drawers, flaps"); Latv. paksis, pl "nterlocking beams, tenon-and-mortise joint, corner of box, side’. Cf. also OE fzes, n. ‘border’; Swiss Fácke, f. ‘wing’. Long-gde in R pax, Cz. pach, m. ‘groin’; Cz. also pachy “loose sleeves’; Ukr. paxa, f. ‘armpit’; Blg. pàxove, pl. (^waist': Skt. pāksah “of half, side or party’: Oss. faxs ‘side’)
16778:review, purview'. Cf. speK- (1) Skt. spastah, pp. & adj. ‘clear’; Av. spasta, obl: -tar, m. ‘watchman’; (LW from Iran. in) Arm. Spas, u, u, S. (service, cf. Per. sipás 'thanks- giving"), beside past, i-st. (? also an Iran. LW) “proof, reason, plea’; Tokh. cf. spaktàn, s. "ser. vice’; Gk. cf. (metath.) sképsis, f. 'considera- tion’; Lat. spectus, gs: -üs, s. ‘sight’: W ffes, m. ‘insight’, fr. *speKtis, cf. nos < *noktis or *nokts; ffesu, inf. ‘see through’; MDu. cf. spiede, spie, m. ‘spy’
=== gumnos/gunos
252:agunos, aguhnos, (agunos) “lamb”. WP I, 39 Gk. amnós, amnís; Lat. agnus; Ir. uan; W oen; OCor.oin; Cor.on; Br. oan; OE eane; (a) OCS agne; Cz. jehné; Latv. (Gmc.LW?) aun ‘ram’
253:agunos (2) (?) see ogunos
4495:gungos, à (1) “lump, swelling”. See next and cf. gungoros, gunos, gongos, gong-. WP I, 638. (The Alb. & Balt. evidence is ambig.) Skt. gungüh “full moon’; It. gonga ‘swelling of gland'; Alb. gungë “lump, boss, swelling"; gung, adj. “hard; impotent’: Rum. substrate cf. goangá 'dung-beetle'; Norw. kunk 'clod' beside konk (2) ‘tub’; variant in Norw. kong (*boil", fr. *geungho-); E conk “head, lump, fat nose’; cf. OE cynca (tuft, fr. *gungio(n)); Li. günga “lump, boss’; Latv. (alleged) gungis, id.
5271:gulio — gumnos (gunos)
5286:gumnos (gunos) ‘comely, beautiful". Cf. gu- mið (gunio) Per. cf. na-yam (“ugly”, fr. *n-?); Gk. gumnós ‘naked; lightly clad' beside gános ‘beauty’; gá- numai ‘be cheerful; Lat. vinnus ‘luxuriant, dainty, easygoing, wanton’; OE cymen, pp. be- side cyme “lovely, comely’; ON kominn, pp. as adj. “of such a state’; beside Icel. kyn (^won- der’: Gk. gán-). (For the Gk. phonol. cf. guné, gána, baná)
11797:nogudos, nogutos (noguito-) ‘naked’. Variant: nogumnos (nogunos, nongu-). WP II, 339 First form in Lat. nūdus; MIr. nocht, Ir. nocht; W noeth; Br. nôaz; Cor. nōth; Go. naqabs; OE nacod; MHG nacket & nackent, (G dial. nackend); ON noktr & nokirðr, id. beside mod. nekt, f. ‘nudity’. Second form in Skt. nagnáh; Hind. Sind. nanga, Romani nango; Av. mayno (sic), id.; Arm. cf. t-nank, gs: -1, ab.s: -av “poor” beside s-nank, i, av ‘bankrupt’; MHG nacken; ON nakinn; Sw. naken “naked. (The antecedents of Per. nang, Kurd. neng ‘shameful; shame’ and of Gk. gumnós ‘naked’, < *p-gum-? are obscure). Cpd. in Oss. bá$- näg “naked? and perh. in Gk. kín-nabos 'sculp- tor's model, if for *-nogu-?). A long-gde form arises in OCS and com. SI. nagü “naked; cf. R naglyj ^barefaced, impudent; Blg. naglo, adv. ‘impudently’; Li. nuogas *naked'; An e- gde form arises in Hitt. nekumanc ‘naked’, fr. *ne-gum- ‘uncomely’?
11994:ogunos, us ‘striving, effort, energy’. Cf. agnos (agunos). (Li. ambig.) Ir. obann, gsf: oibne ‘sudden, rapid, rash’; beside Olr. uinnem, m. ‘effort; (variant in) W afn. m. (boldness, fr. *eguno-?); Li. agnüs ‘lively’; agnà, f. ‘energy’
19838:ue£hen- (ueghn-) ‘carrier, conveyor, convey- ance; carriage, cartage'. Cf. uegh- Skt. vahanam, n. ‘conveyance’; váhnih, m. *charioteer; steed'; Av. vazanom, n. 'cartage, conveyance’; -vazano, adj. cpds. *-conveying"; Lat. cf. (?) vena, f. (tube, vein’; LLat. also *stream — of tar'; cf. ductus, üs in a similar sense); Gaul. cf. co-vinnus, m. (fchariot'. Cf. W cy-wain, v. *Àconvey?); OIr. fén, Ir. féan, pl. féin, m. ‘wagon’; W gwain, pl. gweiniau, f. (2) ‘support; (3) ‘carriage’; (o-gde in) OHG wagan, mpl: wagene, wegene, m. (cart, and com. Gmc.); Blg. vezni, mpl. “scales, balance”; Li. vezenà, f. ‘goods in transit beside vež- mene, pl. “baggage”
```


## [2026-09-07T20:18:57.862Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# map line no -> leaf\nleaf=0\nimport sys\ntargets={252:0,4495:0,5271:0,5286:0,11797:0,11824:0,11825:0,11935:0}\nfor i,l in enumerate(lines,1):\n    if i in targets: targets[i]=leaf\n    leaf+=l.count('\\f')\nprint(targets)\nleaves=data.split('\\f')\nfor t,lf in targets.items():\n    txt=leaves[lf]\n    nums=re.findall(r'^\\s*(\\d{2,4})\\s*$',txt,re.M)\n    print(t,lf,nums[:12])\n\"",
 "description": "Map IEC lines to leaves and page numbers"
}
```


### [2026-09-07T20:18:59.188Z] TOOL RESULT

```
{252: 17, 4495: 181, 5271: 212, 5286: 212, 11797: 473, 11824: 474, 11825: 474, 11935: 479}
252 17 ['15', '20', '25', '30', '40', '45']
4495 181 ['15', '20', '25', '30', '35', '40', '45', '306', '307']
5271 212 ['15', '20', '25', '30', '35', '40', '45', '364']
5286 212 ['15', '20', '25', '30', '35', '40', '45', '364']
11797 473 ['20', '25', '30', '35', '40', '45', '848']
11824 474 ['849', '10', '15', '20', '25', '30', '35', '40', '45', '850']
11825 474 ['849', '10', '15', '20', '25', '30', '35', '40', '45', '850']
11935 479 ['859', '860']
```


## [2026-09-07T20:19:05.994Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==350' SYN.txt | head -60",
 "description": "Buck p.325 naked"
}
```


## [2026-09-07T20:19:06.544Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1017' SYN.txt | head -60",
 "description": "Buck p.992 night"
}
```


### [2026-09-07T20:19:07.261Z] TOOL RESULT

```
‘heal’
arste fr. MLG arste
Digitized by Arya Samaj Foundation Chennai and eGangotri
am BODY; BODILY FUNCTIONS AND CONDITIONS 309 r
SCr. bajati ‘enchant, conjure’, etc., fr. the root in Grk. gnyi ‘say’, ete. Berne- ker 42.
ChSl. vract, Russ. vraé = SCr. vraé ‘sorcerer, fortuneteller’, etc., orig. ‘con- jurer’ : Russ. voréat' ‘growl, grumble, mutter’, vraka ‘nonsense, idle talk’, etc., fr. the root *wer- in Grk. etpw ‘say’, Skt. vrata- ‘command, vow’, etc. Walde-P. 1.283. Solmsen, Unters. 263.
ChSl. (late) lékart, SCr. lijekar, lijeé- nik, etc., fr. the Gme. (above, 3).
7. Skt. bhisaj- : bhisaj-,  bhisajya- ‘cure’ (4.86).
Skt. vaidya-, lit. ‘one versed in science (vidya- : vid-‘know’), learned’, then, like the current European adoption of Lat. doctor, (above, 4), ‘one skilled in medical science, doctor’.
Skt. cckitsaka-, fr. cikitsa- ‘heal, cure’ (4.86).
Av. vimad- : Lat. (4.86). Barth. 1450.
medeéri ‘cure’, etc.
4.88 MEDICINE, DRUG
Grk.  $éppaxoy Goth. (lubja-) Lith. vaistas, gydyklas NG yrarpixd, péppaxo ON lyf, lekningarlyf,lek- Lett. _zles Tat. medicamen(tum), _re- nisdimr ChSI. baltstvo, lékit
medium Dan. medicin, legemiddel SCr. _lijek, ljekarije It. medicina, droga Sw.  medicin, lékemedel, Boh. lék me médicament, drogue drog Pol. _lekarstwo, lek Tim nedicamento, droga OE _lybb, lacedom, ete. Russ. lekarstvo oe medicament, leac, doc- ME __ medicine, drogges Skt.  dGusadha-, bhesaja- ae ae 1.) Ay. —_ baéSaza- Nh. ie f NE medicine, drug Waa, toc Du. —_artsenij, geneesmid- Bn eddyginiaeth, cyffur del, drogerij
poo OHG  lachin, lachintuom,
etc. MHG arzenie, arzatie, la- chen NHG arznei, heilmittel, me-
The dizin, d
```


### [2026-09-07T20:19:08.535Z] TOOL RESULT

```
; | at ited types with suffix -to- or
H Falde?. 1.753. Brugmann, Grd. dio |
99.53 ip. Gtk. rplros, Toch. A trit. _ is Lat. tertius (> It. terzo, ae etc.); W- iryddydd, Br. trede; i “ii etc. general Gmce.; Lith. a Lett. tresars (OPruss. tirtis, but oe ); ChSl. éretiz, etc., general
so lirts an Skt irltya-, Av. Orilya-, OPers.
pritiya-.
9, Ir. tiers, Sp. tercio (fr. Lat. tertius)
were specialized to ‘a third’ (fraction), the former replaced by trotsiéme, with the same new formation as the other or- dinals (orig.? Meyer-Liibke, rz. Gram. 2.177); the latter by tercero, like Ofr. lercier, fr. Lat. terliarius (cf. Sp. primero, Fr. premier fr. Lat. primarius). Rum. al ireilea, fem. a treia, formed fr. the cardinal with preceding article and nom.-aee, sg. of the postpositive article. Tktin, Rum. Elementarbuch 97. ot Ir iris(s), tres, fr. *tristo- or Insli- in form like Lat. testis ‘witness’ - *erstis, *tristis, Walde-P. 1.753. i 2.185. Thurneysen, Gram. ... aie formed after Iv. an, ourth’, etc., with suffix ~m- Silat ae the ordinals for 7, 9, 10. Soe t. (rivet with suffix -eto- after et ‘fifth’, ete. Pedersen 2.135. 13.43. “A thirg?
Dressed by 9 ae (fraction) is often ex-
ene or phrase containin ae for ‘third’ and the word oe taken in c terms are so transparent, 18.49 ag peinection with 13.23 and Or the pote no further comment. ath ee 18 used alone, either in derstog ‘Ng with the word for part 8) op j as Lat. tertia beside tertia © neuter (or later inde-
QUANTITY AND NUMBER
igitized by Arya Samaj Foundation Chennai and eGangotri
943
clinable) form. Among such forms, Fr. tiers, Sp. tercio are now specialized to the fractional sense since their replacement as ordinals by troisiéme, tercero (13.42); and Skt. tfttya- neut. is distinguished by the accent from the ordinal trttya-.
There are also some derivs. formed with various suffixes from the ordinal or cardinal, as follows:
1. Lat. triéns, -ntis ‘a third’ in gen- eral, but esp. ‘a third of an as’, a particip- ial deriv. like quadrdns, sextdns, etc. Thurneysen, IF 39.201.
2. Rum. treime ‘trinity’ and ‘a third’, deriv. of the cardinal with suffix -ime fr. Lat. -tmen. Meyer-Liibke, Rom. Gram. 2.486.
3. Ir. trian, NIr. trian, W. traean, derivs. of the cardinal. Thurneysen, Gram. 250.
4, ON pridjungr, deriv. of the ordinal with suffix -ungr.
OE primen (rare), OFris. thrimin, de- riv. of the cardinal.
5. SCr. treéina, Boh. tfetina, formed fr. the ordinal with suffix -ina, like ChSI. desetina ‘tithe’:
6. Av. 6rigva-, like éafrusva- ‘a fourth’, haptahva- ‘a seventh’, formed fr. the cardinals (pantahva- ‘a fifth’ fr. an ordinal?) with suffix -sva-, IE *swo-, and pe
```


## [2026-09-07T20:19:15.037Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"NAKED\\|4\\.94\\|nagna\" SYN.txt | head -20; echo \"=== night\"; grep -n \"14\\.4[0-9] *NIGHT\\|NIGHT$\\|NIGHT \" SYN.txt | head -20",
 "description": "Grep Buck for NAKED and NIGHT sections"
}
```


### [2026-09-07T20:19:16.301Z] TOOL RESULT

```
1858:7. Skt. andha-, andhas-, andhakara-, fr. adj. andha- ‘blind’ (4.94), perh. : Lat. umbra ‘shade’ (1.63).
3880:: Goth. halts, OE healt ‘lame’, etc. (4.94). Pedersen 1.114.
5260:4.94 Lamp
7823:W. archoll, prob. (with irregular mu- tation) epd. of ar- ‘fore-’ and coll ‘de- struction, loss’ : Goth. halts, OE healt, etc. ‘lame’ (4.94). Morris Jones 264.
8131:4.94 LAME Grk. _ xwAds Goth. halts Lith. raiSas, Slubas NG xourcés ON halir (lami) Lett. _tizls, klibs, slums Lat.  claudus Dan. halt, lam ChSl. chromit It. zoppo, ranco Sw. halt, lam SCr. — hrom, Sepav Fy. botteur OE healt (lama) Boh. chromy, kulhavy yy Sp. cojo ME shalt, lame Pol. chromy, kulawy Rum.  schiop NE lame (halt) Russ. chromoj Ir. bacach, losc Du. kreupel, lam, mank Skt. grona-, srama-, pai- NIr. — bacach OHG _halz (lam) gu-, ete. W. cloff MHG lam, halz, hinlende Av. By hhe Br. kamm NHG  lahm, hinkend
8290:4.99 NAKED, BARE
8292:Fy. nu OE nacod; ber Boh. nahy; holy Sp desnudo ME naked, bare Pol nagt; goli Rum. gol NE naked; bare Russ. nagoj; golyj Tr. nocht; lomm Du. naakt; bloot Skt. nagna- NIr. —nocht; lom OHG  nachut; bar Av. mayna- W. noeth; Ilwm MHG nacke(n)t; bar, bléz
8302:, i Russ. nagoj; Skt. nagna, jp Po rialjor m-, cf. Barth. 1112); ‘naked’, nekuzi ‘goes
19905:NIr. bacach, also and orig. ‘cripple’ = bacach ‘lame’ (4.94).
22580:yal (possessiD 3 Byz, NG gapdis, orig. dub. G. Meyer Neugr. Stud. 4.94, connects with NG dial. papéos ‘large (meal-)bag ; jggnword fr. Ital. fardo or its source Amb, farda ‘bundle of goods’. Hatzi- dakis, Mec. 2.29, suggests deriv. fr, digpadts with semantic extension through ‘copious in speech’ > ‘wide’ in gneral. But the actual use of the rare dgpadjs connotes skill, rather than
=== night
25300:14.42 NIGHT Grk. vot Goth. nahis Lith. naktis ; NG voxra ON noatt Lett. nakts ; Lat. nox Dan. nat ChSl.  noStt i It. notte Sw. natt SCr. noé jj Fr. nuit OE nitht Boh. noc Ft Sp. noche ME night Pol. noc Rum. noapte NE night Russ. not! i Ir. adatg (nocht) Du. nacht Skt. ratrz., ksap-, nakt- 8 NIr. _ oidhche OHG = naht Av. OPers, 2Sap- W. nos MHG naht Br. noz NHG nacht tl Most of the words for ‘night’ belong general Slavic; Ved. nakt- (nom. Sg. nak, to an inherited group, pointing clearly | acc. sg. naktam), nakti- (class. Skt. only ( to an IE word for ‘night’. In Irish, ex- | adv. naktam ‘by night’, cf. Wackernagel, cept for an adv. relic, and in Indo- | Altind. Gram. 3.233 ff.); Alb. naté;— \ Iranian, except in Vedic and a classical | with e-grade Hitt. nekuz ‘evening’, : Skt. adv. relic, the old word was dis- | nekuzi ‘goes to bed’ (Sturtevant, Hitt, lL placed by others, but’ elsewhere has per- | Gloss. 108). i sisted as the usual word to the pres- 2. Ir. adaig, aidche, NIr. oidhche, ent day. etym. dub. Walde-P. 1.34. Walde-H. : 1. IE *nokt(t)-. Walde-P. 2.337 ff. | 1.61. Stokes 326. ( Ernout-M. 682. Sturtevant (connect- 3. Skt. rdtri- : Grk. Anr&, Dor. Aard ; ing this group and that for ‘naked’, | ‘Leto, mother of Apollo and Artemis’, : 4,99) JAOS 52.10, Hitt. Gram. 122 f, orig. personification of the night, perh. Grk. vit, vuerés, NG vixra (v prob. | fr. the root in Grk. \6w ‘be hidden’, fr. a reduced grade); Lat. nox, noctis | ete. Walde-P. 2.377. Boisacq 555. n (> Romance words); Ir. nocht (in in- | Uhlenbeck 248. Y nocht ‘tonight’), W. nos, Br. noz; Goth. Skt. ksap-, Av. xap-, rfapan-, xSapar-, Mi nahis, ON ndtt, etc., general Gmc.; Lith. | OPers. xsap- (Barth. 548 f.) : Grk. pédas, naktis, Lett. nakts; ChSl. nostt, etc., | pédos ‘darkness’. Walde-P. 1.524 f. h q ‘ 14.48 DAWN Grk. dus, Sp8pos Goth. : Lith. auSra, brékSta x NG aby}, xapépyara, ON — dagan, dagsbrin Lett. rita blazma, rila Xapavyy Dan.  dagning, daggry krésla, ausma D Lat. aurora, prima liz Sw.  dagning, gryning ChSl. rano(adv.), -brézgi, di It. alba, aurora OE degréd, degrima, zore (pl.) Fr. ube, aurore dagung SCr. ora, svanuce 1 Sp. alba, aurora ME  dawing, dawning, Boh.  svitdnt, risvit Rum. zori, auroré dayrawe, etc. Pol. Swit, brzask, zorza Tr. dedal NE dawn, daybreak Russ. zarja, razsvel i) Nir. fainne an lae Du. —dageraad Skt.  ugas-, aruna-, pra- D W. = gwawr OHG = morgenrot, -rata, bhata- i Br. goulou-deiz, tarz tagarat Ay. uSah-, astir- ! an deiz MHG morgenrét, -rale,
```


## [2026-09-07T20:19:23.614Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n'); leaf=0; targets={8290:0,8302:0,25300:0}\nfor i,l in enumerate(lines,1):\n    if i in targets: targets[i]=leaf\n    leaf+=l.count('\\f')\nleaves=data.split('\\f')\nfor t,lf in targets.items():\n    print(t,lf,re.findall(r'\\b(\\d{3})\\b',leaves[lf])[:20])\n\"",
 "description": "Find Buck page numbers"
}
```


### [2026-09-07T20:19:25.041Z] TOOL RESULT

```
8290 367 ['438', '578', '339', '684']
8302 367 ['438', '578', '339', '684']
25300 1068 ['427', '133', '180', '234', '772', '268', '350', '849', '467', '183', '176', '113', '877', '113', '329', '308']
```


## [2026-09-07T20:19:32.382Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ma\\(γ\\|y\\)na\\|nagna\" KLN_1966.txt | head -20; echo \"=== KLN night\"; grep -n \"naktih\\|nákti\\|nokt-s\\|nokt-\" KLN_1966.txt | head -20",
 "description": "Grep Klein"
}
```


### [2026-09-07T20:19:32.456Z] TOOL RESULT

```
24919:naked,  adj.,  entirely  unclothed;  bare;  nude.  — ME.  naked,  fr.  OE.  nacod,  rel.  to  OFris.  nakad, MDu.  naket,  Du.  naakt,  OHG.  nackot,  nackut, MHG.  nacket,  G.  nackt,  ON.  nokkvidr,  OSwcd. nakujrer,  Goth,  naqafrs,  ‘naked’,  fr.  I.-E.  *nogwo- dho-;  cogn.  with  L.  nudus  [fr.  *now(e)dos,  for I.-E.  *nogwedhos],  OIr.  nocht,  W.  noeth,  Bret. noaz (for  *nogwtos),  ‘naked’.  Cp. — with  -ro-for- mative  element — ON.  nakinn,  Swed.,  Norw., OFris.  naken,  Dan.  nogen,  and  OI.  nagndh, Avestic  mayna-  (prob.  dissimilated  fr.  *naynd-), ‘naked’.  Cp.  also  OSlav.  nagu  (for  *nog"-),  Lith. ntiogas  (for  *nogo-),  and  Gk.  yup,v6?,  also Xu[zv 6?  (Hesychius),  which  prob.  owe  their forms  to  dissimilation  (see  Boisacq,  DELG.,  p. 158  s.v.  yufivo?,  Hofmann,  EWG.,  p.  49  s.v. yup.v6?,  and  Walde-Hofmann,  LEW.,  II,  p. 185  s.v.  nudus).  Hitt,  nekumanza  and  Arm.  merk (for  *megwro-;  cp.  Avestic  mayna-)  are  cogn. with  the  above  words  (see  Frisk,  GEW.,  I, p.333  s.v.  yufivo? ).  Cp.  gymno-,  nude, naker,  n.,  a  kettledrum.  —  ME.  nakere,  fr.  OF. nacre,  fr.  It.  nacchera,  ‘kettledrum’,  fr.  Arab. naqqarah,  ‘drum’.  See  1st  nacre.
=== KLN night
```


## [2026-09-07T20:19:39.024Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^night,\\|night,  n\\.\\|nightingale\" KLN_1966.txt | head -10; echo \"=== gymnasium\"; grep -n \"gymnasium\\|gymno-,\\|gumnazein\\|yu(iva\\|nude,  adj\" KLN_1966.txt | head -10; echo === ; grep -n \"nyctalopia\\|noctule\\|nocturnal,  adj\" KLN_1966.txt|head",
 "description": "Grep Klein night, gymnasium, nude"
}
```


### [2026-09-07T20:19:39.105Z] TOOL RESULT

```
Exit code 1
6536:Carduus,  n.,  a  genus  of  prickly  herbs  ( bot .)  — L.  carduus ,  ‘thistle’.  See  prec.  word, care,  n.  —  ME.  care,  fr.  OE.  caru,  cearu,  ‘anxiety, sorrow,  care’,  rel.  to  OS.  kara,  ‘sorrow’,  OHG. chara,  ‘lament’,  Goth,  kara,  ‘sorrow’,  OS.  (mod) karag,  ‘anxious,  sad,  sorrowful’,  OE.  cearig, MDu.  carich,  ‘sad,  sorrowful’,  Du.  karig, ‘scanty,  frugal’,  OHG.  karag,  ‘anxious’,  MHG. karc,  karg,  ‘shrewd,  clever’,  G.  karg,  ‘stingy, scanty’;  fr.  Teut.  *karo ,  ‘sorrow,  care’.  These words  are  cogn.  with  Gk.  yr,pu?,  Dor.  yapu ;, ‘voice,  sound’.  Arm.  cicarn,  ‘swallow’,  cicarnuk, ‘nightingale’,  Ossetic  zar,  ‘song’,  zarun,  ‘to  sing’, L.  garrire,  ‘to  chat,  talk,  chatter',  W.  garm, OIr.  gair,  gairm,  W.  gawr,  ‘noise,  cry’,  Toch. karye,  ‘care’.  All  these  words  derive  front  the I.-E.  imitative  base  *gdr-,  ‘to  shout,  cry’.  The sense  development  of  Toch.  karye,  ‘care’,  E.  care and  the  related  Teut.  words  may  be  illustrated by  the  following  stages:  cry — lamentation — grief.  Cp.  chary,  cur,  garrulous,  Gerygone.  Cp. also  German.
6907:Celaeno,  n.,  one  of  the  Harpies  (Greek  mythol.)  — L.,  fr.  Gk.  KeXcclvco,  lit.  ‘the  Black  one’,  fr. xeXcuvo;,  ‘black’,  fr.  I.-E.  base  *qel-,  *qol-, ‘black,  spotted’,  which  is  rel.  to  base  *qdl-,  of s.m.,  whence  L.  caligo,  ‘darkness’.  See  caliginous. celandine,  n.,  the  swallowwort.  —  ME.  celydoine, fr.  OF.  celidoine  (F.  chelidoine),  fr.  L.  chelido- nium,  fr.  Gk.  yeXlSrlvLov,  fr.  yeXlStuv,  gen. X.eXi86vo;,  ‘the  swallow’,  which  is  rel.  to  xi/}:r,, ‘the  thrush’,  and  cogn.  with  OE.  gellan,  ‘to  yell, shriek’,  galan,  ‘to  sing'.  See  yell  and  nightingale and  cp.  chelidonium.
15229:Derivative:  fortissimo,  n.,  a  very  loud  passage, fortitude,  n.,  courage  in  endurance.  —  F.,  fr.  L. fortitidinem,  acc.  of  fortitiidd,  ‘strength,  cour¬ age’,  fr.  fortis,  ‘strong’.  See  fort  and  -tude. fortnight,  n.  —  Shortened  ft.  fourteen  nights.  Cp. sennight,  which  is  contracted  fr.  seven  nights. Derivative :  fortnight-ly,  adv. fortress,  n.  —  ME.  fortresse,  fr.  OF.  (=  F.) forteresse,  ‘strong  place,  stronghold’,  fr.  VL. *fortaricia,  fr.  L.  fortis,  ‘strong’.  See  fort  and cp.  fortalice.
15684:gale,  n.,  an  aromatic  shrub.  —  ME.  gawel,  fr. OE,  gagel,  ‘sweet  gale’,  rel.  to  Du.,  MHG.,  G. gagel,  ‘sweet  gale’;  of  uncertain  origin, gale,  n.,  a  strong  wind.  —  Of  uncertain  origin. It  is  perh.  rel.  to  Dan.  gal,  ‘furious’,  and  to  Norw. galen,  of  s.m.  (this  latter  is  often  used  of  the weather),  and  also  to  OE.  galan,  ‘to  sing’,  giellan, ‘to  scream,  cry’.  See  yell  and  cp.  the  last  element in  nightingale.
15902:cry’.  Accordingly,  ON.  geldr,  etc.,  prob.  meant originally  ‘enchanted,  bewitched’.  See  yell  and cp.  gale,  ‘a  strong  wind’,  and  the  last  element in  nightingale.
20426:Derivatives:  jug,  tr.  \.,jug-ful,  adj. jug,  n.,  note  of  a  nightingale.  —  Of  imitative origin.
20799:knight,  n.  —  ME.,  ‘boy,  youth,  knight’,  fr.  OE. cniht,  ‘boy,  youth,  attendant,  servant,  retainer’, rel.  to  OFris.  kniucht,  MLG.,  MDu.,  Du.  knechl, OS.,  OHG.,  MHG.  kneht,  ‘boy,  youth,  lad, man,  hero’,  G.  Knecht,  ‘servant,  bondman, vassal’;  of  uncertain  origin;  perhaps  rel.  to Swed.  knagg,  ‘knot  in  wood’,  dialectally  used also  in  the  sense  of  ‘a  thickset  man’.  Cp.  E. knag  and  see  Kluge-Mitzka,  EWDS.,pp.  380-81 s.v.  Knecht.  Cp.  also  the  second  element  in lansquenet.
21083:lance-knight,  n.,  a  lansquenet  (hist.)  —  Folk-ety¬ mological  alteration  of  G.  Landsknecht,  ‘foot soldier’  (lit.  ‘land  servant’ ;  see  lansquenet),  due to  a  confusion  of  the  first  element  of  the  word with  lance.
23856:midnight,  n.  —  ME.,  fr.  OE.  midniht.  See  mid, adj.,  and  night.
25422:neah,  neh.  See  nigh,  adv. night,  n.  —  ME.  niht,  night,  fr.  OE.  neah  I,  niht, rel.  to  OS.,  OHG.,  MHG.  naht,  OFris.,  MDu., Du.,  G.  nacht,  ON.  natt,  nott,  Dan.  nat,  Swed. natt,  dial.  Norw.  natt,  nott,  Goth,  nidus,  fr.  Teut. base  *naht,  corresponding  to  I.-E.  *noqt-, whenceOI.  naktam  (adv.  acc.),  ‘at  night’,  ndktih (acc.  pi.),  ‘nights’,  Gk.  vuq  (gen.  vuxtoc),  L.  nox (gen.  noctis).  Alb.  nate,  OSlav.  noiti,  Lith.  nak- tis,  ‘night’,  OIr.  in-nocht,  ‘tonight’,  W.  he-noid, ‘tonight’,  peu-noeth,  ‘every  night’,  W.,  Co.  nos, Bret,  noz,  ‘night’,  Toch.  A  n(o)ktirp,  ‘toward evening’,  Hitt,  nekus  (gen.) , ‘evening’.  Cp.  nocti-, nocturnal,  nycti-,  the  first  element  in  nightingale, Nakshastra,  and  the  second  element  in  acron- ychal,  equinox.
=== gymnasium
10102:cyniatrics,  n.,  that  branch  of  veterinary  medicine which  deals  with  diseases  of  dogs.  —  Com¬ pounded  of  cyn-  and  -iatrics. cynic,  n.  —  L.  cynicus,  ‘a  cynic’,  fr.  Gk.  xuvtx6c, an  adjective  formed  fr.  Kuv6oocpyc9,  ‘Cyno- sarges’,  a  gymnasium  near  Athens.  It  was  in  this gymnasium  that  Antisthenes  taught,  whence his  disciples  were  called  xuvixoi,  lit.  ’of  Cyno- sarges’.  (For  sense  development  cp.  stoic  and academician,  which  are  also  formed  from  place- names.)  The  usual  derivation  of  Gk.  xuvix6^, ‘a  cynic’,  fr.  xumv,  gen.  xu v6p,  ‘dog’,  and  the  ex¬ planation  that  x>jvix<9  orig.  denoted  a  ‘dog¬ like’  philosopher,  is  erroneous.  The  only  con¬ nection  between  a  cynic  and  a  dog  is  given  by
16916:gymkhana,  n.,  display  of  athletic  sports  (orig. Anglo-Indian).  —  A  blend  of  Hind,  gend-khana, ‘ball  house’  (fr.  gertd,  ‘ball’,  and  khdna,  ‘house’), and  E.  gymnastics  (q.v.) gymn-,  form  of  gym  no-  before  a  vowel, gymnasial.  —  Formed  fr.  gymnasium  with  adj. suff.  -al.
16918:gymnasium
16920:of  yupvaatov,  ‘gymnasium’,  and  apyoc;,  ‘leader, chief,  ruler’.  See  next  word  and  -arch, gymnasium,  n.,  i)  a  building  equipped  for  gym¬ nastics;  2)  in  Germany  and  some  other  coun¬ tries,  a  secondary  school  for  students.  —  L.,  fr. Gk.  yupvaatov,  ‘gymnastic  school,  school’,  fr. yujxva^ELv,  ‘to  practice  gymnastic  exercises’,  lit. ‘to  train  naked’,  fr.  yopiv6s,  ‘naked’;  so  called because  the  athletes  trained  naked.  See  gymno-. gymnast,  n.,  one  who  teaches  gymnastics.  —  Gk. YU[ivaaT%,  ‘trainer  of  athletes’,  fr.  yupva^Eiv. See  prec.  word  and  -ast.
16924:gymno-,  before  a  vowel  gymn-,  combining  form meaning  ‘naked’.  —  Gk.  yoizvo-,  yupv-,  fr. yujjivo?,  ‘naked’,  cogn.  with  OI.  nagndh ,  L. nudus,  Goth,  naqaps,  OE.  nacod,  ‘naked’.  See naked  and  cp.  nude.
22374:lyceum,  n.,  a  lecture  hall.  —  L.  lyceum,  fr.  Gk. Xuxct ov,  a  gymnasium  in  Athens  in  which  Aris¬ totle  taught;  so  called  after  the  neighboring temple  of  Apollo,  one  of  whose  epithets  was Auxetop,  lit.  ‘wolf-slayer’,  from  Xuxo?,  ‘wolf’, which  is  cogn.  with  L.  lupus,  ‘wolf’.  See  lupine, adj.
24919:naked,  adj.,  entirely  unclothed;  bare;  nude.  — ME.  naked,  fr.  OE.  nacod,  rel.  to  OFris.  nakad, MDu.  naket,  Du.  naakt,  OHG.  nackot,  nackut, MHG.  nacket,  G.  nackt,  ON.  nokkvidr,  OSwcd. nakujrer,  Goth,  naqafrs,  ‘naked’,  fr.  I.-E.  *nogwo- dho-;  cogn.  with  L.  nudus  [fr.  *now(e)dos,  for I.-E.  *nogwedhos],  OIr.  nocht,  W.  noeth,  Bret. noaz (for  *nogwtos),  ‘naked’.  Cp. — with  -ro-for- mative  element — ON.  nakinn,  Swed.,  Norw., OFris.  naken,  Dan.  nogen,  and  OI.  nagndh, Avestic  mayna-  (prob.  dissimilated  fr.  *naynd-), ‘naked’.  Cp.  also  OSlav.  nagu  (for  *nog"-),  Lith. ntiogas  (for  *nogo-),  and  Gk.  yup,v6?,  also Xu[zv 6?  (Hesychius),  which  prob.  owe  their forms  to  dissimilation  (see  Boisacq,  DELG.,  p. 158  s.v.  yufivo?,  Hofmann,  EWG.,  p.  49  s.v. yup.v6?,  and  Walde-Hofmann,  LEW.,  II,  p. 185  s.v.  nudus).  Hitt,  nekumanza  and  Arm.  merk (for  *megwro-;  cp.  Avestic  mayna-)  are  cogn. with  the  above  words  (see  Frisk,  GEW.,  I, p.333  s.v.  yufivo? ).  Cp.  gymno-,  nude, naker,  n.,  a  kettledrum.  —  ME.  nakere,  fr.  OF. nacre,  fr.  It.  nacchera,  ‘kettledrum’,  fr.  Arab. naqqarah,  ‘drum’.  See  1st  nacre.
25736:nude,  adj.,  naked  bare,  unclothed.  —  L.  nudus, ‘naked,  bare’,  fr.  * now(e)dos  for  I.-E.  *nog"e- dhos\  cogn.  with  Goth,  naqaps,  OE.  nacod,  ‘na¬ ked’.  See  naked.
26956:Palaemon,  n.,  the  genus  consisting  of  the  typical prawns  ( zool .)  —  Fr.  prec.  word, palaeo-,  combining  form.  —  See  paleo-. palaestra,  palestra,  n.,  1)  wrestling  school;  2) gymnasium.  —  L .palaestra,  fr.  Gk.  mxXaioTpa,
26957:‘wrestling  school,  gymnasium’,  formed  with -Tpa,  a  suff.  denoting  place,  fr.  TraXcdeiv,  ‘to wrestle’,  fr.  TcdcXv),  ‘wrestling’,  which  is  of  uncer¬ tain  origin.  Cp.  1st  Palaemon.  For  the  suff.  -tra, cp.  orchestra.
(eval):1: == not found
```


## [2026-09-07T20:19:45.872Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n'); leaf=0; targets={24919:0,25422:0,16920:0,16924:0,25736:0}\nfor i,l in enumerate(lines,1):\n    if i in targets: targets[i]=leaf\n    leaf+=l.count('\\f')\nleaves=data.split('\\f')\nfor t,lf in sorted(targets.items()):\n    print(t,lf,re.findall(r'\\b(\\d{3,4})\\b',leaves[lf])[:8])\n\"",
 "description": "Klein page numbers"
}
```


### [2026-09-07T20:19:47.428Z] TOOL RESULT

```
16920 372 ['690', '6915', '0091', '691']
16924 372 ['690', '6915', '0091', '691']
24919 549 ['480', '1707', '845', '1795', '1871', '612', '158', '185']
25422 560 ['844', '1900', '1860', '1917', '1743', '1819', '1776', '1848']
25736 567 ['1080', '1060', '1061', '1869']
```


## [2026-09-07T20:19:57.431Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nogw\\|nakwed\\|nokw\\|nekwt\\|nyctalopia\\|noctule\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-07T20:19:57.483Z] TOOL RESULT

```
779:nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: Noc- TUID, NOCTULE. 4. Greek nux (stem nukt-), night: NYC- TALOPIA, NYCTITROPISM. 5. Possibly suffixed zero-grade form *nkt-i- in Greek aktis, ray of light: acTrno-. [Pok. neku(t)- 762.]
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
796:Oku-. Swift. Zero-grade form *aku- in compound *oku-petro-, “swift-flying,” in Latin accipiter, hawk (*pet-ro-, flying; see pet-): ACCIPITER. [Pok. 6ku-s 775.] okv-, To see. 1. Germanic *augén- (with taboo deforma- tion) in: a. Old English éage, eye: EYE; DAISY; b. Old Norse auge, eye: WALLEYED, WINDOW; Cc. Low German 00g, eye: OGLE. 2. Suffixed form *ok-olo- in: a. Latin oculus, eye: EYELET, OCELLUS, OCULAR, OCULIST, UL- LAGE; INOCULATE, MONOCLE, OCULOMETER, OCULOMO- TOR; b. Gallo-Latin compound *ab-oculus, blind, modeled on Gaulish ex-ops, blind, in French aveugle, blind: INVEIGLE. 3. Form *okv-s in Greek dps, eye (and stem *op-, to see): METOPIC, MYOPIA, NYCTALOPIA, PEL- OPS, PHLOGOPITE, PYROPE. 4. Suffixed form *ok-ti- in Greek opsis, sight, appearance: OPSIN, -OPSIS, -OPSY; AUTOPSY, (IODOPSIN), (RHODOPSIN), SYNOPSIS. 5. Suf-
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
1573:GUT gheu- GYMNASIUM nogY- GYMNAST nog¥- GYMNOSOPHIST nogW- GYMNOSPERM nog¥- GYNAECEUM gWen- GYNECOCRACY gWen- GYNECOLOGY gWen- GYNO- gWen- -GYNOUS gWen- -GYNY gWen- GYRE géu-
1900:NACELLE nau-2 NAG! ghen- NAIAD (s)nau- NAIL nogh- NAINSOOK nele- NAIVE gene- NAKED nogW- NAME no-men- NANA nana NANNY nana NANO- nana NAP] ken-2 NAP2 ken-2 NAPERY mappa NAPKIN mappa NAPPE mappa NARCO- (s)ner- NARCOSIS (s)ner- NARCOTIC (s)ner- NARES nas- NARK? nas- NARRATE gnoé- NARROW (s)ner- NARWAL (s)kWal-o- NARWHAL nau-! NASAL nas- NASCENT gene- NASO- nas-
1929:NOBLE gno- NOCENT nek-! Nock ken-5 NOCTI- nekw-t- NOCTILUCA leuk- NOCTUID nekw-t- NOCTULE nekw-t- NOCTURN nekw-t- NOCTURNAL nekw-t- Nocuous_nek-! NOD ken-2
1944:NUDI- nogW- NUDNIK nau-! NUISANCE nek-1 NULL ne
1946:NUNCIO neu-1 NUNCUPATIVE kap-, nd-men- NUPTIAL sneubh- NURSE (s)nau- NURTURE (S)nau- NnuT ken-5 NUTATION neu-2 NUTHATCH skep- NUTRIA wed-1 NUTRIENT (s)nau- NUTRIMENT (s)nau- NUTRITION (s)nau- NUTRITIOUS (s)nau- NUTRITIVE (s)nau- NUX VOMICA weme- NUZZLE nas- NYCTALOPIA nekw-t-, okw- NYCTITROPISM nekw-t- NYMPH sneubh- NYMPHOLEPT (s)lag¥- NYSTAGMOUS sneud(h)-
```


## [2026-09-07T20:20:08.654Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '777,780p' AHD_watkins1985.txt | cut -c1-3000",
 "description": "Read AHD nekw-t entry"
}
```


### [2026-09-07T20:20:08.698Z] TOOL RESULT

```
44
neud-
nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: Noc- TUID, NOCTULE. 4. Greek nux (stem nukt-), night: NYC- TALOPIA, NYCTITROPISM. 5. Possibly suffixed zero-grade form *nkt-i- in Greek aktis, ray of light: acTrno-. [Pok. neku(t)- 762.]
nem-. To assign, allot; also to take. 1. Germanic *nem- in: a. Old English niman, to take, seize: NIM, NUMB; (BENUMB); b. Old English n#mel, quick to seize, and numol, quick at learning, seizing: NIMBLE. 2. Greek nemein, to allot: NEMESIS. 3. O-grade form *nom- in: a. Greek nomos, portion, usage, custom, law, division, district: NOME, -NOMY; ANOMIE, ANTINOMIAN, AN- TINOMY, (ASTRONOMER), (ASTRONOMY), AUTONOMOUS, BINOMIAL, DEUTERONOMY, METRONOME, NOMOGRAM, NOMOGRAPH, NUMISMATICS; b. Greek nomé, pasturage, grazing, hence a spreading, a spreading ulcer: NOMA; c. Greek nomas, wandering in search of pasture: NOMAD; d. Greek nomimos, legal, probably borrowed in Latin nummus, coin: NUMMULAR, NUMMULATE. 4, Perhaps suffixed o-grade form *nom-eso- in Latin numerus, num- ber, division: NUMBER; ENUMERATE, SUPERNUMERARY. [Pok. 1. nem- 763.]
```


## [2026-09-07T20:20:12.822Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '775,777p' AHD_watkins1985.txt | tail -c 2000; echo \"=== nightingale\"; grep -n -i \"nightingale\" AHD_watkins1985.txt | head -5",
 "description": "AHD nekw-t start"
}
```


### [2026-09-07T20:20:12.878Z] TOOL RESULT

```
ect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
44
=== nightingale
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
```


## [2026-09-07T20:20:28.332Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ISS brahnak\"; grep -n -i \"brahnak\\|brahnag\\|braxnak\" ISS_alt_DKS.txt | head -20; echo \"== PHD\"; grep -n -i \"brahnag\\|brhnk\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n -i \"brahnak\\|brahnag\" NYB_vol2_glossary.txt | head",
 "description": "Grep for Pahlavi brahnag"
}
```


### [2026-09-07T20:20:28.412Z] TOOL RESULT

```
== ISS brahnak
5476:bünaa- ‘naked’, SuvP. 71v3 (plur.) byelide büna vasta ће naked get clothes’, BS nagnài ca vastrāņi labliante, Z 2:13 bünai jsāte ‘he goes about naked’, п 44-56 būnai та sti ‘he is here naked’; п 4575 būnā và āva ' they came here naked’; 1t 98:16: bünà hvamdą 'naked men'. From *bagna-, Oss, DI. báyndg, D. báyan-vad І. báydm-vad 'bare-footed', D. báyén-sar, І. báydm-sar ‘bare-headed’, D. ron-báyd ' without girdle (-d < -n or possibly participle to base bag-), Sogd. Bud. Byn'k, Chr. булу, Chorasm. ВупуЁ Av. mayna-, Zor.P. brahnak, N.Pers. barahnah; Wanetsi йл. IE Pok. 769 nog"-, O.Ind. magnd-, Got. nagaps, Lit. nýogas, O.Slav. пай,
== PHD
PHD.txt:278:brahnag [b/(?)hnk' | M brhng, N barahna] naked.
PHD.txt:2885:naked brahnag.
PHD_mackenzie.txt:1615:brahnag [bW)hnk' 1M brhng, N bara/ma] naked.
PHD_mackenzie.txt:7124:month miih, mahigiin.                          naked brahnag.
PHD_mackenzie.txt:11094:brahnag                  \~~)      burd
PHD_mackenzie.txt:11098:brahnag                  \~~.-l    bum                             -6\)
== NYB
```


## [2026-09-07T20:20:52.590Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN\"; grep -n -i \"barahna\\|brahnak\\|brahnag\" HRN.txt | head; echo \"== HUB\"; grep -n -i \"barahna\\|brahnak\\|brahnag\\|maγna\\|mayna\" HUB.txt | head; echo \"== BRT maγna\"; grep -n \"maγna\\|mayna\\|maynō\" BRT.txt | head",
 "description": "Grep Horn, Hübschmann, Bartholomae"
}
```


### [2026-09-07T20:20:52.660Z] TOOL RESULT

```
== HRN
== HUB
== BRT maγna
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
19550:Ableit.  aus  mayna-,  auffill,  Bildung;  vgl  HoRW GIrPh.  I  b.  146.  —  Pü.:  TÜSlai.  —  ')  Wo das  Wort  ganz  entstellt  isL
```


## [2026-09-07T20:20:55.565Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19540,19560p' BRT.txt; echo \"=== search magna\"; grep -n \"magna-\\|maγna-\\|nackt'\" BRT.txt | head -20",
 "description": "Bartholomae maγna entry"
}
```


### [2026-09-07T20:20:55.629Z] TOOL RESULT

```
**matay-  iiia
Pü.  (zu  Y.jt):  fia  pmtm  iHo-pi,  oA.:  fa  oft- lak  vihih;  (zu  Y.  5/):   f  m  dn  n  dan  n  (^pü.: mimtvätil,  ob  ma-^kSni  —  ')  NA.  'gSutä;  s. auch  V.  //.  7. j.  maj'na-  Adj.   (fem.  *«J-)   i)  "nackt,
°Ha{ND.)  anaiv/i.- 'BS  apajpayai  vasfrä t  *tanBni  N.55"';  — oss,  lauter*:  'nS  Bia'^rä
I.  täjnäg,  gr. -    I)  Einmal
entblösst':  dva  t vasfra  V.S.io;  — Yt.j9.s6;  —  •«?« 'na  F.  II.         a)*bl N.2«
Ableit.   —  Vgl.  i
yvfiMc  (von  denen  jedei  ant  emi
laut  weist].     —    Pü.:  briknak.
mayari'.  —  »)  Text:  afasläk  ngö
•  j.  ma}^3nta-  Adj.  'nackt,  entblösst*: vari>ian/(as(sd.yit  'tasat  P.  //,  ■*!*.  tOf)  '*.
Ableit.  aus  mayna-,  auffill,  Bildung;  vgl  HoRW GIrPh.  I  b.  146.  —  Pü.:  TÜSlai.  —  ')  Wo das  Wort  ganz  entstellt  isL
•  j.  maxäl-  f.  'Fliege':  druxs  yä  nasus  .. nivSiryete  mqnaym  ahe  >fl5a  'syä  par^mm (sd.)  M.8.6'9;  23  PüZ.;  —  basvan 'sinam »rrfaitinatn  ava.Janyät  V.  14.  f>;  —  °H F.  II.       '[V.7.2  lies:' maxä.i^Är^a.].
KompA.  —  mp.  (Pü.)  maxi,  kurd,  mil,  aif. mal;  vgl.  ai.  mditiiä-  f.  'Biene',  np.  magas.
•  j.  *niaxäi.V«hrp-"  f  'Fliegengestalt':  a^a druxs  ya  nasus  upa.dvqtaiti  .  .  'kihrpa srr^aitya  V.  7.  %.
Pü.:  pa  maxi  karf.  —  ■)  NA.  trennt.
•  j.  maxäi.b3r«ta-  Adj.  'von  Riegen  ver- tragen, fortgeschleppt':  '0  nasu/  Y.S-i; j.  14  PüZ.;  —  aite  nasävö  ya  .  .  'taca nasui  V.  5. 4,
Pü. :  max!  buri.
•  j.  maxätay-  m.  EN.  eines  Gläubigen: sps.pt&ü  °Uis  alaonB  "des  Sp.,  Sohns  des M.  . ."  Yt  13.  116;  —  payanharo  'ieis aiaons  Yt.  13. 116.
Eig.  Bed.?
•  p.  maäya-  Adj.,  bezeichnet  ein  Volk'*: ima  dahySvJ'  fyä  adam  agarbäyam  , .  'yS (NPm.)  D.ff.3;  —  iyam  (sd.)  'ya  D./o(?).
')    liERODOT  4.  I9I;   ^ffi{iu(;   vgl.  JUSTI  GlrPh.
=== search magna
```


## [2026-09-07T20:21:03.838Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n'); leaf=0; t={19550:0,4290:0}\nfor i,l in enumerate(lines,1):\n    if i in t: t[i]=leaf\n    leaf+=l.count('\\f')\nleaves=data.split('\\f')\nfor k,v in t.items():\n    print(k,v,re.findall(r'\\b(1[0-9]{3})\\b',leaves[v])[:10])\n\"",
 "description": "BRT column number"
}
```


### [2026-09-07T20:21:05.224Z] TOOL RESULT

```
19550 619 []
4290 100 []
```


## [2026-09-07T20:21:08.368Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(615,624):\n    nums=re.findall(r'\\b(\\d{3,4})\\b',leaves[i][:400])\n    print(i,nums[:8],repr(leaves[i][:100]))\n\"",
 "description": "BRT leaf numbers nearby"
}
```


### [2026-09-07T20:21:09.634Z] TOOL RESULT

```
615 ['137'] "n/ö]  ahutS  maxdi*nämqm  (/«^veranlasst fiie  ist  wertlos.\nPPA,  einer  Basis  ir.  *maii-  'hervo"
616 [] '13-  3i  im Gegens.  lu  laslhaiufy.  SSVa^/a  freilich /o/rw- fararn  Aimilah.\n•  ].  maeS-ana-  n.'
617 ['266', '103'] '.  Ä  11; F.^g.\n*)  Insbesondere  gilt  das  vom  Rindshara  (a. ^armofta-)!);  TgL  dazu  DsT.  ZA.'
618 [] "zdayasna  aiäAa  z?md  %rii (sd.)  'yjm  ava.kanay>n  dva  'fa  frasnä^aym malsmana  giul  *Bim  äp3"
619 [] 'h  V.  //.  7. j.  maj\'na-  Adj.   (fem.  *«J-)   i)  "nackt,\n°Ha{ND.)  anaiv/i.- \'BS  apajpayai  va'
620 [] 'wann  wirst  du  den Unflat  dieses  Rauschtranks  treffen,  mit dem.."  Y-^i".!©!).  [N.jo:  lies  '
621 [] 'tivem\'  Sinn\'>:  haca  hl vaxtät  \'tyai /rayaräi  "von  Sonnenaufgang\nmaiSy ana-  1 1 1 6\nbis  zur  '
622 [] "e  des  Beins  geht':  yS  paoiryS bansma  frastprmata  %tyaxitls{^^ca  .  . äxlnaiea  maihfSifaitii"
623 [] "4J.i4i   —  m'  vayiibyäca  ..  Vr.i^.i;\n—  tnanf.vistäif(sd.)  tif  vTspilifY.46.19;\n—  tofniiu^  ("
```


## [2026-09-07T20:21:17.714Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON برهنه\"; grep -n \"برهنه\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON نغام\"; grep -n \"نغام\" MON_part1.txt MON_part2.txt | head -10; echo \"== BQT برهنه\"; grep -n \"برهنه\" BQT_v1_pages.txt | head -5; echo \"== BQT نغام\"; grep -rn \"نغام\" BQT_v*_pages.txt incoming/BQT/BQT_v*_pages.txt 2>/dev/null | head -10",
 "description": "Grep Persian dictionaries"
}
```


### [2026-09-07T20:21:17.821Z] TOOL RESULT

```
== MON برهنه
MON_part1.txt:4856:کاذب است. پروتوپلاسم آنها برهنه و بدون 
MON_part1.txt:10979:ماهیی است بزرگ و سر برهنه که دهانی 
MON_part1.txt:27536:پاپتی: آا«م5م (ص‌مر.) (عم.) پا برهنه» یکث 
MON_part1.txt:27905:کف پایش طویل و برهنه و انگشتانش نیز 
MON_part1.txt:29422:بی‌خورش» ساده» تنها: نان پتی. برهنه 
== MON نغام
MON_part1.txt:47036:رنگک. نغام. 
MON_part1.txt:50923:چکامه: (0-)2۳02ن [ - جنغامه < چکٌّامه | 
MON_part1.txt:72321:دارد؛) جسمی» حسل» نغام. 
MON_part2.txt:77262:نغام: ۲ (ص.) زشت و اخوش. تبره 
MON_part2.txt:77490:فرهنگ‌ها نغام به غین و نفام به فا را به یک‎ 
MON_part2.txt:77498:مصحح اقبال (ص ۳۳۷) نغام به عین به‎ 
== BQT برهنه
32028:اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
32053:برهنه و عربان - وتهی وخالی ۰
== BQT نغام
incoming/BQT/BQT_v4_pages.txt:9240:نغام ‎٩‏ « بفتح اول بروزن‌سلام » بمعنی | ورای بی‌نقطه بواو کشیده و بجیم قارسی زده »
```


## [2026-09-07T20:21:20.976Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '77255,77275p' MON_part2.txt; echo \"-----\"; sed -n '77485,77505p' MON_part2.txt",
 "description": "Mo'in naghām entry"
}
```


### [2026-09-07T20:21:21.074Z] TOOL RESULT

```
لطیف. (ص.) پر نعمت. 

نغ: : وم [- نق] (.) (عم.) بهانه جویی. (عم.) 

غرغر. 

نغام: ۲ (ص.) زشت و اخوش. تبره 

رنگ» سبه‌فام. 

نغر: ۸ (ص.) خسوب. خوش. نیکو. 

عجیب و بدیع. نرم و لطیف. چست و 
چابکد. 

نغ زدن: ««ه«سوه [- نق زدن] (سصل.) 

(عم.) بهانه جویی کر دن. (عم.) غرغر کردن. 

ضح. -اين لغت اصلاً در مورد بهانه گیری 
-----


۱۹٩۵۵ 
ولی در حاشیه عبدالررسولی نفام آمده.‎ 
ضصح. جهانگیری آرد: «در بعضی از‎ 
فرهنگ‌ها نغام به غین و نفام به فا را به یک‎ 
معنی نو شته‌اند. همانا که مصنفان را سهوی‎ 
واقع شده. چه نفام به فا به معنی سیاه رنگ و‎ 
تبره فام است و نفغام به غین به معنی زشت و‎ 
ناخوش» رشیدی هر دو را صحیح می‌داند به‎ 
معنی تیره و گوید «تیرگی را زشتی و‎ 
ناخوشي لازم است نه آنکه زشت و ناخوش‎ 
به معنی علی حده است.» اما در لغت فرس‎ 
مصحح اقبال (ص ۳۳۷) نغام به عین به‎ 
معنی «زشت‌نما و تیره گون و بی‌رونق)‎ 
آمده اگر ضبط غین در این نسخه صحیح‎ 
باشد رنفام» مصحف ان است.‎ 

نفایه: (۵-)-۱۸ ,غز3ا۱۵ [ع. نقابه | (۱.) هر جبز 
که به سبب فساد و پستی و بی‌قیمتی به دور 
انداخته شود. نبهر ه» ناسر 4۰ ج. تقابات.
```


## [2026-09-07T20:21:40.142Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# find nearby standalone numbers\nfor i in range(77200,77300):\n    s=lines[i-1].strip()\n    if re.fullmatch(r'[۰-۹٠-٩\\d ]{3,6}',s):\n        print(i,s)\n\"",
 "description": "MON page markers near naghām"
}
```


### [2026-09-07T20:21:41.458Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:21:45.498Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\nfor i in range(77150,77300):\n    s=lines[i-1].strip()\n    if re.search(r'[۰-۹]{4}',s) or re.search(r'\\b4[0-9]{3}\\b',s):\n        print(i,s[:80])\n\" | head -20",
 "description": "MON page markers search"
}
```


### [2026-09-07T20:21:46.804Z] TOOL RESULT

```
77184 نعمت پر ورده.: (۵-)0:۱۲۷۵۸۲۵۱۵-.(1 [ع. ف.|
77240 لعیت: ۱۸۸۲ [ع.] (مص‌ل.) بانگ کلاغ و
77243 نعیق فرهنگ فارسی معین ۱۹۵۳
```


## [2026-09-07T20:22:39.859Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9230,9255p' incoming/BQT/BQT_v4_pages.txt; echo \"=== pdf page tag\"; awk 'NR>=9100 && NR<=9250 && /pdf page/' incoming/BQT/BQT_v4_pages.txt | tail -3",
 "description": "BQT naghām entry"
}
```


### [2026-09-07T20:22:41.064Z] TOOL RESULT

```
نعل و اژ گون - کنابه ازکاری است نعنا ۴ - نوعی از پودنه باشد و اسلآن
که مردم پی بدان نبرند وخبردار نگروید ‎٩‏ .۱ | انعتاع است در عربی » و پارسیان عین آخر را
نعمت جذر اصم «کنایه از نست ۲ حذف کرده انا میگوبند.#
هشت بهشت است ۲ . نعیم پاك - با بای فارسی » کنایه از
نعمتکده ؟ - کنابه ازبپشت است. | اعمال شایسته است که طاعت وعبادت باشد.
بیان چهاردهم
در نون با عین نقظه‌دار مشتتمل بر بیست وسه لغت
نغالگ * - بکر اول وئانی‌بالف کشیده | زشت و ناخوش باشد - وتیره رنگه و سیه قام را
وبکاف زده, بمعتی ابله ونادان باشد - وحرامزاده | نی زکوبند ؛ و بکر اول هم‌آهده است .
را نی زکوبند و بعربی ولدالحرام خوانند. نفرفدج ۷ بضم اول و اسکون ثالی
نغام ‎٩‏ « بفتح اول بروزن‌سلام » بمعنی | ورای بی‌نقطه بواو کشیده و بجیم قارسی زده »
۱ - نمل بازگون و واز کون و باژگونه وواز کونه و وارون و وارونه و واژون و واژونه
(باشگونه) زدن - رسم است که دزد درموقعی که بخواهد کسی نفعمد از کدام (جا) رفته تمل‌وارونه
باسب خود میزند تا نشان پاهای اسب بمکس‌راهی که رفته. افتد. جنگیها هم درمقام خدعة جنگی
چنان کار می‌کنند « فرهنگه نظام *
تعلهای با زگونه است ای سلیم افرت فرعون را دان از کلیم .
مولوی بلخی رومی . ر4 : امثال وحکم دهخداص۰۱۸۱۹
۲ - زیرا « هشت > جذر اصم است وریشه ندارد . ۴ از : سمت (عی) ۳ کده
( پوند مکان ). ۴ - ر4 : هناع . 8 مسحف « ففناککه » (ه.م.)
۹« نام , زشت اما و تیره گون و بی‌رونق باشد . دقیقی ( طوسی ) کوید :
بخیزد یکی تندگرد از میان که روی اندرآن کرد کردد نفام.>
« لفت فری ص ۳۳۷
۷ - ر4 : جهانگیری . رشیدی کوید ‎ :‏ و ی بفا ( افروچ ) گفته‌اند » رك: افروچ؛
در اوستا الغره رئوچ 2 ۲8 ۸5۶8 ( افروچ ) ( از : ان ( فی )۳ اغره
( پایان , حد و حصر + روج ( روشن ( لغة بمعنی روشنی بی پابان است وآن
با رکاه جلال اهور مزدا ( عرش اعظم ) محسوب میشود- ونیز نام ایزدی است که
=== pdf page tag
[pdf page 230]
[pdf page 231]
[pdf page 232]
```


## [2026-09-07T20:22:58.904Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\ndata=open('ISS_alt_DKS.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n'); leaf=0\nfor i,l in enumerate(lines,1):\n    if i==5476: print('leaf',leaf); break\n    leaf+=l.count('\\f')\n\"; echo \"== MON gymnastics\"; grep -n \"ژیمناستیک\\|ژیمناس\" MON_part1.txt MON_part2.txt | head; echo \"== MON barahna alt\"; grep -n \"برهنگی\\|بر هنه\\|بَرهنه\" MON_part1.txt | head -5",
 "description": "DKS leaf and MON greps"
}
```


### [2026-09-07T20:23:00.228Z] TOOL RESULT

```
leaf 340
== MON gymnastics
MON_part1.txt:16704:ژیمناستیکك و شیرجه تعداد آن از ۱۰ 
MON_part1.txt:54087:آنت: زره. حلقهٌ ژیمناستیکك: (ور.) دو حلقه 
MON_part1.txt:73289:دختری که همواره در مجالس لهو و لعب و ژیمناستیک: »۶1۳800 (4) ورزش بدنی 
== MON barahna alt
26163:ما کبان‌ها که دارای گردنی بر هنه و گوشتی و 
27498:پابر هنه: )۲2۱92 0۸-.ج (ص مر .) 
47531:جرده: (م-)2[ (.) برهنگی. 
52077:بر هنه. 
94136:عاری: 217 [ع.] (افا. ص.) بر هنه» لخت؛ ج.
```


## [2026-09-07T20:23:14.970Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بر هنه:\\|برهنه:\\|بر هنه ‌\" MON_part1.txt | head -5; echo \"=== context 52077\"; sed -n '52070,52080p' MON_part1.txt; echo \"=== ARY barahna\"; grep -n \"برهنه\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "MON and ARY barahna"
}
```


### [2026-09-07T20:23:15.070Z] TOOL RESULT

```
27498:پابر هنه: )۲2۱92 0۸-.ج (ص مر .) 
=== context 52077
دریابنده را حاسه و جمع آنها را حواس 
نامند. (شفا ۲۹۷۵۲۹۵:۱) فرع. سج.) 
حاسد: 4 (ع.] (افا.) رشکک برنده؛ 
رشکین. بدخواه» بداندیش» بدسگال؛ ج. 
اد حسده. (غم.)» حاسد ین. 

حاسر: و۳( [ع.] (رص.) بی‌زره» بی خود. 
بر هنه. 

حاشا: 545« [ع.] (ق. کلم انکار) هرگ 
مبادا؛ نه چنین است. (ف.) (.) انکار. دبوار 
=== ARY barahna
```


## [2026-09-07T20:23:25.261Z] TOOL CALL #39: Bash

```json
{
 "command": "pdftoppm -f 369 -l 369 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369.png",
 "description": "Render PDF page 369"
}
```


### [2026-09-07T20:23:27.132Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74176 Sep  7 16:23 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369.png
```


## [2026-09-07T20:23:29.900Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369.png"
}
```


### [2026-09-07T20:23:30.381Z] TOOL RESULT

```

```


## [2026-09-07T20:23:30.378Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:23:49.541Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 369 -l 369 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg369hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg369hi.png'); print(im.size)\nw,h=im.size\n# empty box region approx x 0.45-0.78, y 0.485-0.52 of page\nim.crop((int(0.42*w),int(0.475*h),int(0.80*w),int(0.525*h))).resize((int(0.38*w*1.6),int(0.05*h*1.6))).save('pg369-emptybox.png')\nim.crop((int(0.18*w),int(0.58*h),int(0.75*w),int(0.65*h))).save('pg369-latin.png')\n\"",
 "description": "Crop empty box region"
}
```


### [2026-09-07T20:23:52.474Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-07T20:23:55.910Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369-emptybox.png"
}
```


### [2026-09-07T20:23:56.006Z] TOOL RESULT

```

```


## [2026-09-07T20:23:56.003Z] INPUT

[Image: original 2067x352, displayed at 2000x341. Multiply coordinates by 1.03 to map to original image.]


## [2026-09-07T20:24:00.927Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg369hi.png'); w,h=im.size\nim.crop((int(0.34*w),int(0.535*h),int(0.80*w),int(0.575*h))).save('pg369-eb2.png')\n\"",
 "description": "Crop empty box again"
}
```


### [2026-09-07T20:24:02.531Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:24:05.860Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369-eb2.png"
}
```


### [2026-09-07T20:24:05.873Z] TOOL RESULT

```

```


## [2026-09-07T20:24:13.215Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg369hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.66*h),int(0.42*w),int(0.71*h))).save('pg369-nocht.png')\n\"",
 "description": "Crop Latin nocht"
}
```


### [2026-09-07T20:24:15.170Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:24:18.167Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369-nocht.png"
}
```


### [2026-09-07T20:24:18.179Z] TOOL RESULT

```

```


## [2026-09-07T20:24:27.092Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:24:27.098Z] TOOL RESULT

```


```


## [2026-09-07T20:24:31.829Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%86%D9%87",
 "prompt": "Give the Persian entry برهنه verbatim: etymology (Middle Persian form, Proto-Iranian reconstruction, cognates such as Avestan maγna-, Khotanese, Sogdian, Ossetian), and the meaning. Quote exactly."
}
```


## [2026-09-07T20:24:33.982Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts",
 "prompt": "Quote the reconstruction, meaning, and the list of descendants (Indo-Iranian, Latin, Greek, Germanic, Balto-Slavic). Does it list any Old Persian form? Does it list Avestan or Old Persian at all for 'night'?"
}
```


### [2026-09-07T20:24:37.895Z] TOOL RESULT

```
# Persian Entry: برهنه

**Etymology:**
The word derives from Middle Persian *bl(ʾ)hnk'* (brahnag), tracing back to Proto-Iranian *\*bagná* ("naked") with a secondary -r-. The ultimate source is Proto-Indo-European *\*negʷ-* ("naked").

**Meaning:**
"Bare, naked, nude"

**Note on Cognates:**
The provided Wiktionary entry does not explicitly list cognates such as Avestan maγna-, Khotanese, Sogdian, or Ossetian forms. The etymology section references only the reconstructed Proto-Iranian and Proto-Indo-European ancestors, along with the Middle Persian intermediate form.
```


### [2026-09-07T20:24:38.521Z] TOOL RESULT

```
# Proto-Indo-European *nókʷts

**Reconstruction and Meaning:**
The reconstructed form is "*nókʷts" (feminine noun), meaning "night" or possibly "evening."

**Major Descendant Groups:**

- **Indo-Iranian:** Sanskrit nákt-, Avestan forms listed
- **Latin:** nox
- **Greek:** Ancient Greek núx
- **Germanic:** Proto-Germanic *nahts
- **Balto-Slavic:** Proto-Balto-Slavic *náktis

**Regarding Old Persian:**
The page does not list any Old Persian form. It includes Younger Avestan ("upa.naxturušu") under Proto-Iranian descendants, but Old Persian is not mentioned.

**Summary:** While Avestan is documented, Old Persian receives no coverage in this etymological entry for the word meaning "night."
```


## [2026-09-07T20:24:44.687Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/naked",
 "prompt": "Quote the etymology of 'naked' including the PIE root and Proto-Germanic form."
}
```


## [2026-09-07T20:24:46.433Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gymnasium",
 "prompt": "Quote the etymology of gymnasium, gymnastic, and gym: Greek gymnasion, gymnazein 'to exercise naked', gymnos 'naked', and the PIE root; also whether French gymnastique / German Gymnasium mediated the English words."
}
```


### [2026-09-07T20:24:48.711Z] TOOL RESULT

```
# Etymology of "Naked"

The word "naked" traces back to Old English *nacod*, meaning "nude, unclothed, bare." According to the Online Etymology Dictionary, it derives from Proto-Germanic *\*nakwadaz* and ultimately from the PIE root *\*nogw-* meaning "naked."

Here's a direct quote encompassing both linguistic ancestors:

"from Proto-Germanic *\*nakwadaz*...from PIE root *\*nogw-* 'naked'"

This ancient root is remarkably widespread across Indo-European languages, appearing in Sanskrit *nagna*, Greek *gymnos*, Latin *nudus*, and Russian *nagoi*, among others.
```


### [2026-09-07T20:24:59.106Z] TOOL RESULT

```
# Etymology of Gymnasium, Gymnastic, and Gym

**Gymnasium (1590s):** From Latin *gymnasium*, derived from Greek *gymnasion* "public place where athletic exercises are practiced," rooted in *gymnazein* "to exercise or train," literally "to train naked," from *gymnos* "naked." This traces back to the Proto-Indo-European root *\*nogw-* meaning "naked."

**Gymnastic (1570s):** "Pertaining to athletic exercise," from Latin *gymnasticus* and Greek *gymnastikos* "fond of or skilled in bodily exercise," also derived from *gymnazein*.

**Gym (1871):** U.S. student slang, functioning as an abbreviated form of *gymnasium*.

**Regarding mediation through French and German:**

The source material indicates that German adopted gymnasium terminology from the 15th century onward as "a name for 'high school.'" However, the document does not explicitly address whether French *gymnastique* or German *Gymnasium* served as intermediaries for English adoption. The English terms appear to derive directly from Latin and Greek sources rather than through Romance or Germanic languages.
```


## [2026-09-07T20:25:08.223Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B3%CF%85%CE%BC%CE%BD%CF%8C%CF%82",
 "prompt": "Quote the Ancient Greek γυμνός etymology section verbatim: what PIE form is given, is it from *nogʷ-no- / *nogʷ-mo- with metathesis or dissimilation, what do Beekes/Frisk say, and is the origin considered obscure?"
}
```


## [2026-09-07T20:25:08.398Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nightingale",
 "prompt": "Quote the etymology of nightingale: Old English form, the 'night' element and the 'galan' (to sing) element."
}
```


### [2026-09-07T20:25:13.695Z] TOOL RESULT

```
# Etymology of Nightingale

**Old English Form:**
"from Old English _næctigalæ_, in late Old English _nihtegale_"

**The "Night" Element:**
The first part comes from _\*nakht-_ meaning "night," which traces back through Proto-Germanic and ultimately to the PIE root _\*nekwt-_.

**The "Galan" (to sing) Element:**
"_\*galon_ 'to sing,' related to Old English _giellan_ 'to yell'"

Together, the word literally combines the concept of nighttime with the act of singing, perfectly capturing the bird's defining characteristic of its melodious vocalizations heard during evening hours.
```


### [2026-09-07T20:25:13.762Z] TOOL RESULT

```
# γυμνός Etymology Analysis

## PIE Form
The Proto-Indo-European form given is **\*nogʷnós** via metathesis from **\*nogʷós** ("naked").

## Metathesis Details
The etymology states: "From Proto-Indo-European _\*nogʷnós_ by metathesis (possible taboo deformation; if the metathesis didn't happen we would have _\*νυγνός_ (\*nugnós)), from _[\*nogʷós](/wiki/Reconstruction:Proto-Indo-European/neg%CA%B7- "Reconstruction:Proto-Indo-European/negʷ-")_ ("naked")."

The source specifically notes this as a "possible taboo deformation" rather than straightforward sound change.

## Scholarly Sources
The page cites **Beekes** (2010) in the "Further reading" section but does not present his specific analysis within the etymology section itself. The etymology does not explicitly state whether Beekes or Frisk consider the origin obscure—it treats the metathesis explanation as the working hypothesis without flagging exceptional obscurity.
```


## [2026-09-07T20:25:24.306Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW vinnulus\"; grep -n \"vinnulus\\|vinnus\" LEW_1910.txt LAT.txt | head -10",
 "description": "Grep Latin dictionaries for vinnulus"
}
```


### [2026-09-07T20:25:24.359Z] TOOL RESULT

```
== LEW vinnulus
```


## [2026-09-07T20:25:28.448Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vinnul\\|uinnul\\|vinnus\" LEW_1910.txt LAT.txt POK_full.txt | head -10; echo \"== nudus LEW\"; grep -n \"nudus\" LEW_1910.txt | head -5; echo \"== nudus LAT\"; grep -n \"n[uū]dus\" LAT.txt | head -5",
 "description": "Search vinnulus and nudus in Latin refs"
}
```


### [2026-09-07T20:25:28.532Z] TOOL RESULT

```
LAT.txt:68796:oratione uinnula, uenustula; le passage de Non.x 86 ,13, se rapportamt
LAT.txt:68797:i ce mot eet alter 4 ; cf. aussi Thes. Gloss. uinnulus, mollis, blandus;
LAT.txt:68802:pour expliquer uinnulus ), cf. le non propre Vinnius ?
LAT.txt:82448:" *303, «»aa uinnulus, li**e 4 , l <: e «t altdrfi.
== nudus LEW
== nudus LAT
42238:Les anciens rattachaient nubo, nupta a gr. vup,cpr), e.g. P.F.i73,a,nudus
42284:nudus, -a, -um: nu, d^nude. Avec 1 'ablatif, "denue de, d 4 pouill^
42286:"legerement vetu", cf. Vg., G. 1,399, nudus are, sere nudus. Sens derive:
42296:got.naqaps et *-to- dans iri. nochf, gall. noeth, *-edo- dans lat. nudus
61862:et lat. nudus. - la spdcialisation de sena tient A ce que siccus a
```


## [2026-09-07T20:25:32.646Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68790,68805p' LAT.txt; echo \"=== nudus\"; sed -n '42284,42300p' LAT.txt",
 "description": "Ernout-Meillet vinnulus and nudus"
}
```


### [2026-09-07T20:25:32.750Z] TOOL RESULT

```
manu. - Le uindex etant le defenseur d'un membre de la "grande fa-
mille", on pense a iri. fine qui est le non de la "grande famille";
v.h.a.wtni signifie "appartenant 4 . la famille, ami". Ces rapprochements
sont s^duisants.
ulnnulus, -a, -um: — dicitur molliter se gerens et minime ui-
riliter quid faciens, P.F.5iy,6; cf. un seul ex. dans Pl., As.a«3,
oratione uinnula, uenustula; le passage de Non.x 86 ,13, se rapportamt
i ce mot eet alter 4 ; cf. aussi Thes. Gloss. uinnulus, mollis, blandus;
-m, delectabile. II faut peut-Stre y rapporter la glose uinnicus,
vcd)(eXr|C (avec une variante uinicus) CGL II 309,5.
De uinnus doublet de cincinnus, cit£ par Isid., Gr.3, xy: uinnus,
cincinnus molliter flexus (si toutefois uinnus n'est pas invente
pour expliquer uinnulus ), cf. le non propre Vinnius ?
Adjectif expressif, sans ^tymologie sfire. Cf. uieo?
uinnus: v. le pr^c^dent.
ulnum, -i n.iulnus forme vulgaire, Petr.41, 13. Schol. Bern. in
=== nudus
nudus, -a, -um: nu, d^nude. Avec 1 'ablatif, "denue de, d 4 pouill^
de". Quelquefohs aussi, comme gr. yup,voS, et peut-etre a son imitation,
"legerement vetu", cf. Vg., G. 1,399, nudus are, sere nudus. Sens derive:
sans ornement,' simple; nuda ueritds. ~ Ancien (Enn.), usuel. *Panroman,
sauf roumain. M.L.S988.
Derives et composes: nudulus, -a, -um (tardif); nuditas; nudo,-as,
M.L.5985, nudatio; denudo (depuis Enn. jusqu ’1 la Vulg., cf. oltio-
yup,vcxo); enudo (rare, tardif); nudipes (= gr. yu^anouc), nudipedalia,
n.pl.; renudo (epoq. imper.).Tout se passe comme s'il y avait eu un adjectif radical, repr 4 sente
par le derive th 4 matique a vocalisme radical long v.sl .nagii, lit.
nUgas "nu", et par des derives pourvus de divers suffixes: *-no- dans
skr. nagndh et *-eno- dans v.isl. nakinn, *-e!oto- dans v.isl. nekkuidr,
got.naqaps et *-to- dans iri. nochf, gall. noeth, *-edo- dans lat. nudus
(pour la coexistence de -to- et *-do-, cf. lit. tvirtas et v.sl .tvrudH
"ferme"); forne a e radical dans hitt. nekumanza "nu". 11 y a des
formes aberrantes, comme av.mafreo et gr. yu(i.vo£ (et Xup.vo£ Hes.), dont
la theorie fait difficulte. L'armenien meme, avec m- initial comme
```


## [2026-09-07T20:25:47.161Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT naktin/xsap\"; grep -n -i \"naktin\\|nakti\\|xšap\\|xsap\" KNT.txt | head -10; echo \"== TLM\"; grep -n -i \"naktin\\|xšap\" TLM.txt | head -5; echo \"== HRN night\"; grep -n -i \"šab\\|sab 'Nacht'\\|Nacht\" HRN.txt | head -5",
 "description": "Kent Old Persian lexicon"
}
```


### [2026-09-07T20:25:47.237Z] TOOL RESULT

```
== KNT naktin/xsap
2224:"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
3477:20 : afahya : xSapava :raucapativà : ava : akunavayatà —— :8atiy : Dárayava
== TLM
== HRN night
112:es ihm darin nicht nachtun und habe ihn daher vielleicht
140:sehen weggeblieben; vergl. Nachträge, S. 256,Xtistü (No. 485), meyezfl (No. 1007), auch gerzman (N'o.
150:nachträglich keine Nummer mehr herausnehmen und musste
228:für die Nachträge verwerten konnte^).
288:*) In der Umschreibung der FD. bin ich, wie ich nachträglich
```


## [2026-09-07T20:26:01.618Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neg%CA%B7-",
 "prompt": "Quote the reconstruction, its meaning, and the descendants list: which forms (Proto-Indo-Iranian, Avestan, Proto-Iranian, Latin nudus, Proto-Germanic, Greek) are listed? Does it list Avestan maγna- and Proto-Iranian *bagna-?"
}
```


## [2026-09-07T20:26:03.500Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D8%B9%D8%A7%D9%85/",
 "prompt": "Is there an entry for نغام? What do Dehkhoda and Farhang-e Mo'in say about نغام - meaning and any etymology?"
}
```


### [2026-09-07T20:26:07.266Z] TOOL RESULT

```
# Proto-Indo-European Root *negʷ-

**Reconstruction and Meaning:**
The root is reconstructed as "*negʷ-" with the meaning "bare, naked."

**Listed Descendants:**

The page documents several major descendant forms:

- **Proto-Indo-Iranian:** "*nagnás" is listed with a reference to further descendants
- **Latin:** "niger" is mentioned under a possibly related form "*negʷ-ro-s"
- **Proto-Germanic:** "*nakwadaz" and "*nakʷnaz" are included
- **Ancient Greek:** "gumnós" appears under Proto-Hellenic "*gumnós"

**Notable Omissions:**

The entry does **not** list Avestan maγna- or Proto-Iranian *bagna- among its descendants. The page only references Proto-Indo-Iranian "*nagnás" without providing Avestan or Proto-Iranian cognates within the main derived terms section. These forms, if attested as descendants of this root, would need to be verified through other etymological sources.
```


### [2026-09-07T20:26:08.081Z] TOOL RESULT

```
Based on the content provided, there is no entry for **نغام** (nogham) in this dictionary page. The page only contains an entry for **نعام** (ne'am), which has different meanings including:

1. Ostrich (شترمرغ)
2. Desert/wasteland (دشت)
3. A marker placed on roads
4. An affirmative word similar to "yes"
5. A phrase meaning "for prosperity and comfort"

The dictionary sources cited (Dehkhoda, Nahayat al-Arab, Aghrab al-Mavarad, and Nazem al-Attebba) all relate to **نعام**, not **نغام**. If you're looking for information about نغام specifically, you would need to consult a different dictionary entry, as it does not appear on this page.
```


## [2026-09-07T20:26:15.953Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D8%BA%D8%A7%D9%85/",
 "prompt": "Quote the entry for نغام: the meaning(s) given by Dehkhoda and Farhang-e Mo'in, and any etymological note or origin tag (e.g. [پهلوی], [ع.]). Also quote the poetic citation if any."
}
```


## [2026-09-07T20:26:17.919Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%DB%8C%D9%85%D9%86%D8%A7%D8%B3%D8%AA%DB%8C%DA%A9/",
 "prompt": "Quote the entry for ژیمناستیک: the origin tag given by Farhang-e Mo'in or Dehkhoda (is it marked as French [فر.]?) and the meaning."
}
```


### [2026-09-07T20:26:22.328Z] TOOL RESULT

```
# نغام

## Dehkhoda Definition
"زشت نمای. زشت. ناخوش. بد" (ugly in appearance; ugly; unpleasant; bad). Also: "تیره گون. بی رونق. گردآلود. تیره گون" (dark-hued; dull; dusty; murky).

## Farhang-e Mo'in Definition
The dictionary provides two senses: "ذرات گرد و غبار پراکنده در هوا" (scattered dust particles in air) and "زشت و ناخوش" (ugly and unpleasant).

## Poetic Citation
From Daqiqi:
"بخیزد یکی گرد تند از میان / که روی اندر آن گرد گردد نغام"
(A swift dust rises from midst / the face in that dust becomes murky)

**Etymology:** The entry notes an Arabic origin form [ن َغ ْ غا] with the descriptor (ع ص) indicating both Arabic and substantival parts of speech.
```


### [2026-09-07T20:26:22.844Z] TOOL RESULT

```
# ژیمناستیک Entry Origin and Meaning

**Dehkhoda Dictionary:**
Origin marked as French [فرانسوی]: "ورزش بدنی با اسبابهای مختلف از قبیل پارالل و بارفیکس و دارحلقه و غیره" (Physical exercise with various apparatus such as parallel bars, horizontal bar, and rings, etc.)

**Farhang-e Mo'in:**
Origin marked as French [فر.]: Described as "ورزشی است به منظور پرورش و آماده سازی بدن برای نمایش حرکت های تعادلی" (A sport designed for physical development and body preparation to display balancing movements)

Both sources identify the word as originating from French, with definitions emphasizing physical training using specialized apparatus.
```


## [2026-09-07T20:26:42.526Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; python3 -c \"\nimport re\ndata=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\ni=data.find('nog')\n# find pdf page tags near printed 337-340\nimport sys\nm=[(mm.start(),mm.group(1)) for mm in re.finditer(r'\\[pdf page (\\d+)\\]',data)]\nprint(len(m))\n\" 2>/dev/null; grep -n \"nackt\" WLD_Bd2_pages.txt | head -20",
 "description": "Explore WLD Band 2"
}
```


### [2026-09-07T20:26:43.826Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
0
6198:   Norw. mdartl. flein „kahl, nackt“, Subst. „kahler Fleck^', schwed. mdartl.
6199:flen „nackt'*, norw. mdartl. fleina ,,entbl66t, kahlkopfig werden" und ,,die
6203:nackte Ebene^',               plinkii,     pTikti      ^kahlkopfig werden”,                 lett.   pVks   entbloBt,
12365:bhoso-s „nackt“ (das                      nacb Pedersen Ark. f. n, f. 20, 3S5
12372:  Ahd. bar ..nackt, blo6^', nbd. 6ar, ags.      aisl. bcrr ,,nackt, bloB‘*; lit.
13641:bldfj mhd. blo^ ^bloB, nackt“, nhd. hIo(i (ahd. blo^ mit merkwurdiger Bed.
13957:Wog „bla8, nackt^* fiihren in der Bed. weit ab, vgl. Kluge ®, Weigand-Hirt
22447:nogw-        ^.nackt”.
22448:   Anord.        „nackt machen"; dehnstufig \\t. ndgas^ aksL       „nackL*,
22449:(ob auch ai. naga-h ,,Schlange, Elefant als ,,nacktes. uiibehaartes Tier"? '
22462:   mit Dentalforrnantien                   :    lat.               „nackt“ aus            ncg^irdhos           '^nog'^iodhos
22464:ags. nacod,          ahd. nackut,                naclmt, nhd. nackt\                   air.   nocht,   cymr. usw. nocth
22465:,,nackt"      {'‘iiog^^-to-s )
22467:   mit Formans- }io- anord. nakinn.^ afries. naken ,.nackt‘' (k statt nord.
22469:-inn )   :ai. 7iagnd- ..nackt". av. niayna- ds. (m- unerklart, aber wohl auch
22494:zu air, lomni, cymr. llinn ,,blo6. nackt* ? und beide zu kuh-, -p- „abschalen''?
22526:(sei „UDgehoriit“ aus „glatt, abgeschabt“) und idg. nog]^- „nackt‘' nicht uber-
25798:gr. Xetjbia^ „nackte Schnecke“, lat. Ifmax, -acis „Wegschnecke“ (wohl aus
27786:ihurneysen IP. 14, 127ff.) air. lomni^ cymr. Ihvm „blo6, nackt" (lupsmo-
27789:vog Hes.           (s.    u, nog^-   „nackt"); mit      air.        lumman „covering" vgl. (als Lw.?)
```


## [2026-09-07T20:26:48.127Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '22447,22480p' WLD_Bd2_pages.txt; echo \"=== find printed page marker\"; awk 'NR>=22400 && NR<=22460' WLD_Bd2_pages.txt | grep -n \"33[0-9]\\|34[0-9]\" | head",
 "description": "Walde-Pokorny nogw entry"
}
```


### [2026-09-07T20:26:49.511Z] TOOL RESULT

```
nogw-        ^.nackt”.
   Anord.        „nackt machen"; dehnstufig \\t. ndgas^ aksL       „nackL*,
(ob auch ai. naga-h ,,Schlange, Elefant als ,,nacktes. uiibehaartes Tier"? '




s. Zubaty BB. IS, 251; Schroder Ablautst. 12 f       s. aber auch Liden                       ;


Stud. 32 f. usw. u. sncg- ..kriechen*’                             )




   mit Dentalforrnantien                   :    lat.               „nackt“ aus            ncg^irdhos           '^nog'^iodhos
= got. }iagaps {-d-K anorJ. npkkiddr (auch noktr), woneben aschwed. nakuper,
ags. nacod,          ahd. nackut,                naclmt, nhd. nackt\                   air.   nocht,   cymr. usw. nocth
,,nackt"      {'‘iiog^^-to-s )

   mit Formans- }io- anord. nakinn.^ afries. naken ,.nackt‘' (k statt nord.
weist   aiif L'mgestaltung aus iilterem                u. zw. nach den Ptc. auf
-inn )   :ai. 7iagnd- ..nackt". av. niayna- ds. (m- unerklart, aber wohl auch

die Yorstufe von weslosset. hay nay als Dissimilationsform h—n fiir m~-n\
s. Bartholomae Airan. Wb. 1112; fiir ^nag-ma- als Grundlage von mayna-

ist keine positive Sttitze beizubringen, auch nicht aus den gr. Formen)

hieher wohl auch gr. yviivog, bei lies, kvavog und aTioAvyuaiog d:rtoyi\(f-                                     '



vcDoig. Kv7ioioi\ s. liber die Tersuche, die lautlichc Entwicklung zu ver-
=== find printed page marker
16:Bmy BB. 7, 338£.), vgl. in letzterer Bed. gr. dxxlg „Strahl“ (Pick BB.
28:                                                                  nog^^*                                                  339
```


## [2026-09-07T20:26:59.156Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"Nacht”\\|Nacht\\\"\\|nok\\^\\|nekt\" WLD_Bd2_pages.txt | sed -n '1,25p'",
 "description": "WLD night entry"
}
```


### [2026-09-07T20:26:59.205Z] TOOL RESULT

```
22651:Hierzu ai. ram f. „Nacht“, doch hat ai. ratri „Nacht" fernzubleiben, da
```


## [2026-09-07T20:27:03.943Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"noctua\\|nvktóg\\|naktam\\|naktis\" WLD_Bd2_pages.txt | head -10; echo ---; awk 'NR>=22200 && NR<=22300' WLD_Bd2_pages.txt | grep -n \"33[6-9]\" | head",
 "description": "WLD night material"
}
```


### [2026-09-07T20:27:05.200Z] TOOL RESULT

```
22379:Kacht“,     noctua „Nachteule“, nodumus, noctuabundus (vgl. u. ai. ahtiU,
---
23:336                                                 nit    no-
36:   Vgl. Fick BB. 1, 336, Wb. I* 95, 500, Schulze KZ. 27, 603 f., Qu. ep.
61:     335f., 339, 344, 994 f. (hier spez. iiber die Partikelformen).
76:Grdr. II ^ 2, 339), ai. anena^ andya,, g. 1. du. ai. anaydh, av. g. du. anoyd
```


## [2026-09-07T20:27:09.418Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '22360,22400p' WLD_Bd2_pages.txt",
 "description": "WLD nekwt entry text"
}
```


### [2026-09-07T20:27:09.472Z] TOOL RESULT

```
Boisacq 674 Anm- 1 ein, daB dann statt dxzTg, s. u., *ajti'ig zu erwarten
ware;   unbefriedigend auch Petersson                              LUA
                                                  1915, 12 f), vvxtcoq Adr.
„nachts“ (*Acc. der Bildung vdcog, vvxTsgog, vvxrsQivog „nachtlich“       lat.                     :



nodumus); vv^a’ vvxtcoq Hes. hom. sivdvv%eg ,,neun Naehte hindurch“,
evvvxoQ „nachtlich“, 7iavvv%iog ,,die ganze Nacht dauernd“, aixovvxi „in der-
selben Nacht“ (dafi dies z-lose w/- nach dvv^i ovv/og zu vv^ hinzugebildet
sei, Termuten Bartholomae BB. 15, 21, J. Schmidt PI. "iSlff., Brugmann II*
1, 140; aber  waram dann nur auBerhalb des lebendigen Paradigmas? Es
muB wohl eine adverbial erstarrte Kasnsform der Ausgangspunkt gewesen
sein; ob ein Lok. [oder neutraler Acc.??] *vvx\t\ „nacht8“, dann zu vvxa,
*vvxi aufgefullt mit assimilatorischer Aspirierung des -x in der haufigen Yer-
bindung mit qf.uQal)-, alb. naie „Nacht“ (G. Meyer BB. 8, 187, Alb. Wb. 298).
  Lat. nox, noctis „Nacht“ (g. pi. noctmm ?-St,, aber deutlich kons, St. im
Adv. nox „nachts“ aus gen. *noqt-es, -os.   Solmsen Stud. 192), nocturnus
„nachtlich“    (: wxxsQivog, vvxtcoq); vom Stamme *noqtu- lat. noctu „bei
Kacht“,     noctua „Nachteule“, nodumus, noctuabundus (vgl. u. ai. ahtiU,
                   und got. uthw-o,
alctau- „bei I^acht"'                                       lit.   nak{t)w6ti,   s.   bes. Osthoff aaO.,
Uhlenbeck PBrB. 30, 318).
   Air. innocht „hac nocte“, cymr. peu-noeth ,,jede Nacht“,                            mcymr. trannoeih
„am folgenden Tage“, cymr. he-no „hac nocte“                               (nicht idg.    -Mose Form,
sondern der nom. *noqt-s oder sin suffixloser Loc. *mqt, wenn dieser oben
mit Recht fiir *vvx- angenommen wurde), corn, haneth, mbret. henoz ds.;
cymr. corn, nos, bret. nos „]Sracht“, wohl aus *noqt-stu--, cymr. neithnvyr,
neithwyr (Zs. oder Zsruckung mit Tiivyr „Abend“) „la8t night“, com. nehues,
mbret. neyzor, nbr. neiseur ds. (s. Pick II* 195, Pedersen KG. I 123, 516 f.,
11 79, 192 f); daB ir. tiug-nair „rruhmette“ als „Ende der Nacht“ (air!
tiug „Ende“) nach Stokes KZ. 35, 595 eine Spur des r-St. enthalte (*noqtri-),
ist aus lautlichen Grunden ausgeschlossen.

   Got. nahts (D. pi. nahtam nach dagam), aisl. nott, naft, ahd. as. naht,
ags. neaht, niht „Kacht‘’ (kons. St.), ags. nihlerne „nachtlich“ (iiber
                                                                        das von
Pick in* 290, Falk-Torp und negtern als dehnstufige Form angereihte
      nuothurn „nuchtern“ s. u. nagih- „nuchtem“); lit. naktts (kons.        pi.                   g.
naJctu),   lett.   nahts,        apr.   naktin
                                      sg) „Nacht“, nak{f)v-yne „Kachther-
```


## [2026-09-07T20:27:19.901Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT naked\"; grep -n \"^Naked\\|Naked, \" SKT.txt | head -3; grep -n \"Nude\\|Nocturnal\\|Nightingale\\|Gymnastic\" SKT.txt | head -6",
 "description": "Skeat entries"
}
```


### [2026-09-07T20:27:19.976Z] TOOL RESULT

```
== SKT naked
```


## [2026-09-07T20:27:24.666Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"naked, bare\\|nightingale\\|gymnastic\\|nocturnal\" SKT.txt | head -8",
 "description": "Skeat grep case-insensitive"
}
```


### [2026-09-07T20:27:24.718Z] TOOL RESULT

```
10149:Lemur,  a  noctonial  animaL  (L.)  I* lemur,  n  ghost :  so  nicknamed  by  oaSorai-- isls  from  Its  nocturnal  habits.
23851:Bulbul.  a  nightingale.      (Pen.) buIM,   a   bird   with    a    mcludlous a-sembting  the  night ingxtc.     Of  inulitiv ongin.
```


## [2026-09-07T20:27:32.811Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== noctule\"; grep -rn -i \"noctule\" FSD_vol*.txt WEB_vol1.txt | head -4; echo \"== nyctalopia\"; grep -rn -i \"nyctalopia\" FSD_vol*.txt WEB_vol1.txt | head -4; echo \"== gym\"; grep -rn -i \"gymnasium, n\" FSD_vol*.txt WEB_vol1.txt | head -3",
 "description": "FSD/Webster for noctule, nyctalopia"
}
```


### [2026-09-07T20:27:32.925Z] TOOL RESULT

```
== noctule
== nyctalopia
FSD_vol3.txt:75353:niysiertoUB a-spect - n.-slght, a Nyctalopia ii. •sing-
FSD_vol3.txt:77238:TUBNR ] — nocturnal sight, day-blindness, nyctalopia —
FSD_vol4.txt:49157:lalnthodnrkorbllndtolded-fleldofv.  1   See  under  field 2.  SamcMFiELD,  0   (2)  See  also  point  of  view  — Indirect or  peripheral  v   ,   vision  In  which  the  Image  Is  formed  outside of  the  fovea  centralis  of  the  retina,  by  the  ra>  s   of  light  fall- ing on  tho  peripheral  parts  of  the  retina  — Iridescent  v   *   a state  of  vision  In  which  objects  appear  either  colored  or  with their  outlines  presenting  prismatic  colors  — multiple  v.,  a morbid  state  of  \   Islon  In  which  sev  eral  images  of  a   single  ob- ject are  seen  at  the  same  time,  manifold  vision,  polyopia  or polyopsla  —   nlglitfV.*  n   Same  as  nyctalopia  —   point  of V   ,   same  as  cfnter  of  v   ision  —   reflected  or  refracted  v.* vision  as  affected  by  reflected  or  refracted  rajs  of  light  — Bklmv,,  R   Tho  perception  of  light  by  a   reflex  functional action  of  the  skin  without  organs  of  vision,  as  with  certain earthworms  —   Vrslon-al*  a   Of,  pertaining  to,  or  consist- ing of  vision  or  a   vision  visionary -vTslon-al-ly,  adv  — vrslon-Ist*  n   A   dreamer  or  believer  In  dreams,  especially In  preternatural  visions,  also,  a   visionary  —   vi'slon-lcss*  a Destitute  of  sight  or  of  visions
== gym
```


## [2026-09-07T20:27:39.483Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/nyctalopia",
 "prompt": "Quote the etymology of nyctalopia: Greek nyx/nyktos 'night', alaos 'blind', ops 'eye', via Latin nyctalopia; and the meaning (night blindness or day blindness)."
}
```


## [2026-09-07T20:27:40.794Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nocturnal",
 "prompt": "Quote the etymology of nocturnal and any mention of noctule and nocti-: Latin nocturnus, nox/noctis, and the PIE root."
}
```


### [2026-09-07T20:27:43.008Z] TOOL RESULT

```
# Etymology of Nyctalopia

**Etymology:** "Borrowed from Ancient Greek νυκταλωπία (nuktalōpía), from νύξ (núx, 'night'), ἀλαός (alaós, 'blind'), and ὄψ (óps, 'eye')."

**Meaning:** The term denotes "the inability to see clearly in dim light; night blindness" in medical contexts. It is a countable and uncountable noun with plural forms nyctalopias or nyctalopiae.
```


### [2026-09-07T20:27:46.345Z] TOOL RESULT

```
# Etymology of Nocturnal

**Main Etymology:**
"Of or pertaining to the night, used or done at night," the word derives from Old French *nocturnal* or directly from Late Latin *nocturnalis*, which stems from Latin *nocturnus* meaning "belonging to the night."

**Latin Roots:**
The Latin *nocturnus* comes from *nox* (genitive *noctis*), meaning "night." This Latin term is cognate with Old English *neaht*, demonstrating ancient linguistic connections across language families.

**Proto-Indo-European Origin:**
The word ultimately traces to PIE *\*nekwt-*, which meant "night" and appears across multiple ancient languages including Greek *nyx*, Latin *nox*, Sanskrit *naktam*, and Lithuanian *naktis*.

**Note on Related Terms:**
The document does not mention "noctule" specifically. However, it discusses related words like *nocturn* (a liturgical term from c. 1200) and *nocturne* (a musical composition style from 1851), both sharing the same Latin *nocturnus* root.
```


## [2026-09-07T20:27:53.788Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nude",
 "prompt": "Quote the etymology of nude: Latin nudus, the date of entry into English, and the PIE root."
}
```


## [2026-09-07T20:27:54.892Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/night",
 "prompt": "Quote the etymology of night: Old English niht/neaht, Proto-Germanic *nakht-, PIE *nekwt-, and the cognates listed."
}
```


### [2026-09-07T20:27:57.583Z] TOOL RESULT

```
# Etymology of Nude

**Latin Origin:** The word derives from "Latin _nudus_ 'naked, bare, unclothed, stripped.'"

**Date of Entry:** The adjective form entered English in the **1530s** as a legal term meaning "unsupported, not formally attested," while the noun form referring to artistic representations appeared in **1708**.

**PIE Root:** The ultimate source is the Proto-Indo-European root **_\*nogw-_** meaning "naked," which also gave rise to related words like the English "naked."
```


### [2026-09-07T20:27:59.524Z] TOOL RESULT

```
# Etymology of Night

According to the Online Etymology Dictionary, the word "night" derives from "late Old English _niht_ (West Saxon _neaht_, Anglian _næht_), from Proto-Germanic _\*nahts_" and ultimately traces back to "PIE _\*nekwt-_."

The entry provides several cognates across Indo-European languages, including Greek _nyx_, Latin _nox_, Sanskrit _naktam_, and Lithuanian _naktis_. Scholars believe the root probably comes from a verb meaning "to be dark, be night."

An interesting historical note: "The fact that the Aryans have a common name for night, but not for day...is due to the fact that they reckoned by nights." This reflects how ancient peoples organized their calendars, with days beginning at sunset rather than sunrise.
```


## [2026-09-07T20:28:10.492Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg369.png data/verification/sources/refs/ocr/BOOK/369.png && for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%86%D9%87' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/neg%CA%B7-' \\\n 'https://en.wiktionary.org/wiki/%CE%B3%CF%85%CE%BC%CE%BD%CF%8C%CF%82' \\\n 'https://en.wiktionary.org/wiki/nyctalopia' \\\n 'https://www.etymonline.com/word/naked' \\\n 'https://www.etymonline.com/word/nude' \\\n 'https://www.etymonline.com/word/night' \\\n 'https://www.etymonline.com/word/nightingale' \\\n 'https://www.etymonline.com/word/nocturnal' \\\n 'https://www.etymonline.com/word/gymnasium' \\\n 'https://abadis.ir/fatofa/%D9%86%D8%BA%D8%A7%D9%85/' \\\n 'https://abadis.ir/fatofa/%DA%98%DB%8C%D9%85%D9%86%D8%A7%D8%B3%D8%AA%DB%8C%DA%A9/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 369, roots Nogw / Noktis' 2>&1 | tail -1\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T20:28:18.524Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6b3e45b2f524a43e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac6a9ffb9cc769e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e641189bd1555258.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74ad033d4a42b3bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa69db3599d19bd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9600179c946194f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ecdc5f1569850ea1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf32d2a76f7ddd23.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65ddbd6c2a573d98.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/838d26b4fb8caf2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb462bf4da546cfc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b51b57d1fc20c183.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b6755474eb638432.txt
```


## [2026-09-07T20:28:22.789Z] TOOL CALL #75: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T20:28:22.842Z] TOOL RESULT

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


## [2026-09-07T20:30:45.021Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nfor fn,ln,off in [('PHD.txt',278,21),('LAT.txt',42284,18),('LAT.txt',68794,18),('KLN_1966.txt',24919,0)]:\n    data=open(fn,encoding='utf-8',errors='replace').read()\n    lines=data.split('\\n'); leaf=0\n    for i,l in enumerate(lines,1):\n        if i==ln: break\n        leaf+=l.count('\\f')\n    print(fn,ln,'leaf',leaf,'printed~',leaf-off if off else '?')\n\"; echo \"== LAT nox\"; grep -n \"^nox,\\|nox, noctis\" LAT.txt | head -3",
 "description": "Compute printed pages"
}
```


### [2026-09-07T20:30:46.646Z] TOOL RESULT

```
PHD.txt 278 leaf 42 printed~ 21
LAT.txt 42284 leaf 815 printed~ 797
LAT.txt 68794 leaf 1321 printed~ 1303
KLN_1966.txt 24919 leaf 549 printed~ ?
== LAT nox
42122:nox, noctis f.: nuit; diesse de la nuit. La diclinaison de nox
```


## [2026-09-07T20:30:57.717Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A8%D8%B1%D9%87%D9%86%D9%87",
 "prompt": "Quote the Farhang-e Mo'in entry for برهنه verbatim, including any origin tag in brackets such as [په.] (Pahlavi), and the definitions."
}
```


### [2026-09-07T20:31:01.529Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for برهنه

According to the Farhang-e Mo'in dictionary, the entry reads:

"(ب ِ رَ نِ) [په.] (ص.) 1 - لخت ، عریان . 2 - آشکار، پدیدار، فاش ."

This indicates the word has a Pahlavi origin [په.] and provides two main definitions: first, meaning naked or bare; second, meaning obvious, apparent, or exposed.
```


## [2026-09-07T20:31:06.516Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://vajehyab.com/moein/%D8%A8%D8%B1%D9%87%D9%86%D9%87' --note 'pdf page 369, root Nogw, Mo-in entry برهنه [په.]' 2>&1 | tail -1",
 "description": "Archive vajehyab source"
}
```


### [2026-09-07T20:31:07.976Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/70654efd52d27fab.txt
```


## [2026-09-07T20:40:30.752Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-369.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0_nodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mağnâ\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Young Avestan maγna- (fem. maγnā-) 'naked, stripped' is real and correctly placed: Bartholomae, Altiranisches Wörterbuch col. 1111-1112 s.v. 'j. maγna- Adj. (fem. °ā-) 1) \\\"nackt, entblösst\\\"', citing Vd. 8.10 (nara .. maγna ..) and Vd. 5.10 (dva .. vastra). The form continues *nagna- < PIE *nogʷ-no- (exactly Skt. nagná-), the initial n- having gone to m- by dissimilation against the following nasal (n—n > m—n); Pokorny 769 writes 'Avestan maγna- ds. (m- through dissimilation, the initial grade of westosset. bæγnaγ)', Walde-Pokorny II 339 calls the m- 'unerklärt' but refers it to Bartholomae 1112 and rejects a base *nag-ma-, and Klein s.v. naked has 'Avestic maγna- (prob. dissimilated fr. *naγnā-)'. Avestan γ is the regular voiced spirant reflex of the labiovelar *gʷ before -n-. Nourai's spelling 'mağnâ' reproduces Bartholomae's feminine maγnā-; the normal citation form is maγna-. The chart's own NOTE ('See \\\"Bŭnai: naked\\\" for another possible root') is well taken: the b-forms of the same taboo family (Khot. būnaa-, Sogd. βγn'k, Oss. bæγnæg) are where the Persian word actually comes from.\",\n  \"derivation_fa\": \"واژهٔ اوستایی maγna- «برهنه، عریان» (مادهٔ مادینه maγnā-) در اوستای نو گواهی شده است؛ بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۱۱۱–۱۱۱۲ آن را با شاهدهایی از وندیداد ۸/۱۰ و ۵/۱۰ آورده است. این صورت از ایرانی باستان *nagna- و آن از هندواروپایی آغازین *nogʷ-no- است (همانند سنسکریت nagná-)؛ «ن» آغازین در برابر «ن» دوم دچار ناهمگونی (dissimilation) شده و به «م» بدل گشته است — پوکورنی (ص ۷۶۹) و والده-پوکورنی (ج ۲ ص ۳۳۹) و کلاین هر سه همین را می‌گویند. γ اوستایی نیز دگرگونی آوایی منظم *gʷ پیش از -n- است. ادعای نورایی درست است؛ تنها نکته این‌که صورت فرهنگ‌نامه‌ای maγna- است و «mağnâ» صورت مادینهٔ آن را نشان می‌دهد.\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/neg%CA%B7-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:769\", \"status\": \"supports\", \"note\": \"Pokorny IEW 769 s.v. nogʷ-, nogʷod(h)o-, nogʷ-no- 'naked', Note: 'often distorted taboo': 'with formants -no-: Old Indic nagna- \\\"naked\\\", Avestan maγna- ds. (m- through dissimilation, the initial grade of westosset. bæγnaγ)' (POK_full.txt line ~63070, 'Page(s): 769').\"},\n    {\"ref\": \"KLN:1026\", \"status\": \"supports\", \"note\": \"Klein, Compr. Etym. Dict. s.v. 'naked' (KLN_1966.txt line 24919, leaf 549 ≈ pp. 1025-1026): 'Cp. ... OI. nagnáh, Avestic maγna- (prob. dissimilated fr. *naγnā-), \\\"naked\\\"'.\"},\n    {\"ref\": \"SYN:325\", \"status\": \"supports\", \"note\": \"Buck, Dict. of Selected Synonyms §4.99 NAKED, BARE (SYN.txt line 8290, leaf 367 ≈ p.325): the Avestan column reads 'Av. maγna-' beside 'Skt. nagna-'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"col. 1111-1112 s.v. maγna-\", \"stance\": \"supports\", \"note\": \"'j. maγna- Adj. (fem. °ā-) i) \\\"nackt, entblösst\\\" ... — Pü.: brahnak' (BRT.txt leaf 619; the neighbouring leaf carries the running column number 'maiθyana- 1116').\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 339 s.v. nogʷ-\", \"stance\": \"supports\", \"note\": \"'ai. nagná- \\\"nackt\\\", av. maγna- ds. (m- unerklärt, aber wohl auch die Vorstufe von westosset. bæγnæg als Dissimilationsform b—n für m—n; s. Bartholomae Airan. Wb. 1112; für *nag-ma- als Grundlage von maγna- ist keine positive Stütze beizubringen)' (WLD_Bd2_pages.txt line 22469; page marker 'nogʷ- 339' on the same leaf).\"},\n    {\"src\": \"LAT\", \"where\": \"s.v. nudus (leaf 815 ≈ p. 797)\", \"stance\": \"partial\", \"note\": \"Ernout-Meillet: 'Il y a des formes aberrantes, comme av. maγna- et gr. γυμνός (et λυμνός Hes.), dont la théorie fait difficulté' — same root, but they stress that the Avestan m- is not regularly derivable.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. nogʷ-\", \"stance\": \"silent\", \"note\": \"Watkins lists only the Germanic, Latin and Greek reflexes of nogʷ-; no Iranian form (AHD_watkins1985.txt line 787).\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"brahnak\", \"verdict\": \"plausible\",\n  \"derivation\": \"Middle Persian brahnag 'naked' is real (Book Pahlavi <brhnk'>, Manichaean <brhng>; MacKenzie, CPD: 'brahnag [b/(?)hnk' | M brhng, N barahna] naked'), and it is exactly the word the Pahlavi Zand uses to render Avestan maγna-, which is why Bartholomae's entry for maγna- ends 'Pü.: brahnak' — so Nourai's arrow is right as a translation equation and right about root membership: Bailey (Dict. of Khotan Saka, s.v. būnaa-) lists 'Av. maγna-, Zor.P. brahnak, N.Pers. barahnah' together under 'IE Pok. 769 nogʷ-'. It is not, however, a phonological descendant of maγna-: Avestan maγna- would have given MP *maγn-/*mahn-, never brahn-. Wiktionary derives brahnag from Proto-Iranian *bagná- 'naked' (whence Khot. būnaa-, Sogd. βγn'k, Oss. bæγnæg) 'with a secondary -r-', the b- being a further taboo dissimilation (WP II 339: 'Dissimilationsform b—n für m—n'). Avestan maγna- and MP brahnag are therefore sister formations on *nogʷ-no-, not parent and child; Nourai's own cross-reference to his root 'Bŭnai: naked' points at precisely the *bagna- family that modern scholarship prefers. Hence plausible rather than confirmed.\",\n  \"derivation_fa\": \"فارسی میانهٔ brahnag «برهنه» واقعی است (خط پهلوی <brhnk'>، مانوی <brhng>؛ مکنزی، «فرهنگ کوچک زبان پهلوی»). این واژه در زند، برگردان اوستایی maγna- است و از همین رو بارتولومه در پایان مدخل maγna- می‌نویسد «پهلوی: brahnak»؛ بیلی نیز maγna- اوستایی و brahnak پهلوی و «برهنه»ی فارسی را زیر ریشهٔ *nogʷ- (پوکورنی ۷۶۹) کنار هم می‌آورد. اما brahnag را نمی‌توان بازماندهٔ آوایی maγna- دانست: maγna- در فارسی میانه *maγn-/*mahn- می‌شد، نه brahn-. ریشه‌شناسی امروزی (ویکی‌واژه) آن را از ایرانی باستان *bagna- «برهنه» می‌گیرد — همان که ختنی būnaa-، سغدی βγn'k و آسی bæγnæg از آن است — با «ر» افزودهٔ ثانوی؛ و b- آغازین خود ناهمگونی تابویی دیگری است (والده-پوکورنی: b—n در برابر m—n). پس maγna- و brahnag هم‌ریشه و خواهرند، نه پدر و پسر: ادعای نورایی با احتیاط پذیرفتنی است، و ارجاع خودِ او به ریشهٔ «Bŭnai» درست به همان خانوادهٔ *bagna- اشاره دارد که پژوهش امروزی می‌پسندد.\",\n  \"sources\": [W+\"%D8%A8%D8%B1%D9%87%D9%86%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:256\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies VI (Prolexis to the Book of Zambasta) is not available online (refs_online.json: 'not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute'). The substitute by the same author was checked instead and is recorded under 'consulted' (ISS_alt_DKS s.v. būnaa-).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"s.v. brahnag (PHD.txt leaf 42, ≈ p. 19-21)\", \"stance\": \"supports\", \"note\": \"MacKenzie: \\\"brahnag [b/(?)hnk' | M brhng, N barahna] naked\\\"; the English-Pahlavi index has 'naked brahnag'.\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. būnaa- 'naked' (ISS_alt_DKS.txt line 5476, leaf 340 ≈ p. 322)\", \"stance\": \"supports\", \"note\": \"Bailey: 'From *bagna-, Oss. D. bæγnæg ..., Sogd. Bud. βγn'k, Chr. ..., Chorasm. ..., Av. maγna-, Zor.P. brahnak, N.Pers. barahnah; Wanetsi ... IE Pok. 769 nogʷ-, O.Ind. nagna-, Got. naqaþs, Lit. nuogas, O.Slav. nagŭ.'\"},\n    {\"src\": \"BRT\", \"where\": \"col. 1112 s.v. maγna-\", \"stance\": \"supports\", \"note\": \"the entry closes 'Pü.: brahnak' — i.e. the Pahlavi version glosses Av. maγna- by brahnak, which is the equation Nourai draws.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"grep -i 'brahnak|brahnag' returns nothing; the word is not in Nyberg's Manual glossary.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. برهنه, Etymology\", \"stance\": \"partial\", \"note\": \"'From Middle Persian bl(ʾ)hnk' (brahnag), from Proto-Iranian *bagná ('naked') with a secondary -r-, from Proto-Indo-European *negʷ- ('naked')' — same root, different immediate Iranian ancestor than the chart's Avestan maγna-.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"berehneh «برهنه»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian برهنه barahna / berehne 'naked' descends regularly from MP brahnag: the MP suffix -ag loses its -g in New Persian and appears as -a/-e (brahnag > barahna, like MP bandag > banda, zindag > zinda), and the initial cluster br- is broken by an anaptyctic vowel (br- > ba-r-/be-r-), a common New Persian treatment of inherited initial clusters. The meaning is unchanged, with the usual metaphorical extension 'bare > open, manifest' (Mo'in gives '1- لخت، عریان 2- آشکار، پدیدار، فاش'). Mo'in tags the word [په.] 'Pahlavi', which is exactly the arrow drawn here; Bailey lists 'N.Pers. barahnah' in the same set as Zor.P. brahnak. Wiktionary's chain is 'Persian برهنه < Middle Persian brahnag < Proto-Iranian *bagná- < PIE *negʷ-'.\",\n  \"derivation_fa\": \"«برهنه» در فارسی نو بازماندهٔ منظم brahnag فارسی میانه است: پسوند -ag پهلوی در فارسی نو «گ» پایانی را از دست می‌دهد و به -ه/-e بدل می‌شود (brahnag > برهنه، همچون bandag > بنده و zindag > زنده)، و خوشهٔ آغازی br- با واکهٔ میانجی شکسته می‌شود (be-r-/ba-r-). معنا دست‌نخورده مانده و تحول معنایی «لخت > آشکار، فاش» نیز طبیعی است؛ معین در فرهنگ خود آن را با برچسب [په.] (پهلوی) و با دو معنی «لخت، عریان» و «آشکار، پدیدار، فاش» می‌آورد — یعنی درست همان پیکانی که نورایی کشیده است. بیلی نیز barahnah فارسی را در همان دستهٔ brahnak پهلوی می‌گذارد. ادعای نورایی درست است.\",\n  \"sources\": [W+\"%D8%A8%D8%B1%D9%87%D9%86%D9%87\", \"https://vajehyab.com/moein/%D8%A8%D8%B1%D9%87%D9%86%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"ISS:256\", \"status\": \"not_checked\", \"note\": \"ISS VI not online; Bailey's DKS s.v. būnaa- (the substitute) does list 'N.Pers. barahnah' beside 'Zor.P. brahnak' — see 'consulted'.\"},\n    {\"ref\": \"MON:517\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. برهنه: '(ب ِ رَ نِ) [په.] (ص.) ۱- لخت، عریان. ۲- آشکار، پدیدار، فاش' — the [په.] tag is precisely the Pahlavi origin of this arrow. Read via vajehyab.com/moein/برهنه; the copy of MON on disk is the 2-volume Adena reprint, whose pagination cannot be mapped onto the 6-volume print Nourai cites, so p.517 itself could not be checked.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.v. برهنه (vajehyab)\", \"stance\": \"supports\", \"note\": \"'[په.] (ص.) ۱- لخت، عریان...' — Pahlavi origin, meaning 'naked'.\"},\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"s.v. būnaa-\", \"stance\": \"supports\", \"note\": \"'Av. maγna-, Zor.P. brahnak, N.Pers. barahnah ... IE Pok. 769 nogʷ-'.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'barahna|brahnak'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no entry for the word (grep returns nothing).\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'barahna|brahnak|maγna'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien does not treat it (grep returns nothing).\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. برهنه\", \"stance\": \"supports\", \"note\": \"'From Middle Persian brahnag ... Proto-Iranian *bagná ... PIE *negʷ- \\\"naked\\\"'; gloss 'bare, naked, nude'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Germanic\", \"words\": \"nakw-eda\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Nourai's 'nakw-eda' is Watkins' Proto-Germanic *nakweda-: 'nogʷ-. Naked. 1. Suffixed forms *nogʷ-eto-, *nogʷ-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED.' Phonetically: PIE *o > Gmc *a; the labiovelar *gʷ gives Gmc *kw by Grimm's law (voiced *gʷ > voiceless *kʷ); the dental suffix *-eto-/-oto- appears as *-eda-/-ada- by Verner-conditioned voicing of *þ after an unstressed syllable. Whence Goth. naqaþs, ON nǫkkviðr, OHG nackut, OE nacod. Klein reconstructs the same shape as I.-E. *nogʷo-dho-; Etymonline has Proto-Germanic *nakwadaz.\",\n  \"derivation_fa\": \"صورت «nakw-eda» همان *nakweda- ژرمنی آغازین در فرهنگ واتکینز (پیوست ریشه‌های هندواروپایی) است: «*nogʷ-eto-, *nogʷ-oto- در ژرمنی *nakweda-, *nakwada- و انگلیسی کهن nacod». دگرگونی‌های آوایی منظم‌اند: *o هندواروپایی در ژرمنی به a بدل می‌شود؛ همخوان لبی‌کامی *gʷ بر پایهٔ قانون گریم به *kw بی‌واک می‌گراید؛ و پسوند دندانی *-eto-/-oto- بر پایهٔ قانون ورنر به *-eda-/-ada- واک‌دار می‌شود. بازماندگان: گوتی naqaþs، نورس کهن nǫkkviðr، آلمانی علیای کهن nackut، انگلیسی کهن nacod. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/naked\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. nogʷ-: 'Suffixed forms *nogʷ-eto-, *nogʷ-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED' (AHD_watkins1985.txt line 787).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. naked (leaf 549 ≈ pp. 1025-1026)\", \"stance\": \"supports\", \"note\": \"'OE. nacod ... Goth. naqaþs, \\\"naked\\\", fr. I.-E. *nogwo-dho-'.\"},\n    {\"src\": \"POK\", \"where\": \"p. 769\", \"stance\": \"supports\", \"note\": \"'with dental formants: ... Gothic naqaþs (-d-), Old Norse nøkkuiðr ..., Old English nacod, Old High German nackut, nachut, Modern High German nackt'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 339\", \"stance\": \"supports\", \"note\": \"'mit Dentalformantien: ... = got. nagaþs (-d-), anord. nøkkiðr (auch nøktr), woneben aschwed. nakuþer, ags. nacod, ahd. nackut, nachut, nhd. nackt'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. naked\", \"stance\": \"supports\", \"note\": \"'from Proto-Germanic *nakwadaz ... from PIE root *nogw- \\\"naked\\\"'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"naked\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OE nacod 'nude, unclothed, bare' > ME naked > NE naked; the word is a straight inheritance, and its final -ed is not the English participial ending but the inherited PIE dental suffix *-eto-/-oto- reanalysed as one (Klein: 'ME. naked, fr. OE. nacod'). The chart's arrow Germanic > English carries no reference in the book, but the chain is uncontroversial and covered by both Klein and Watkins.\",\n  \"derivation_fa\": \"«naked» انگلیسی میراث بی‌واسطهٔ انگلیسی کهن nacod «لخت، بی‌جامه» است که در انگلیسی میانه naked شده و بی‌تغییر به انگلیسی نو رسیده است. نکتهٔ باریک آن‌که -ed پایانی، پسوند اسم‌مفعولی انگلیسی نیست بلکه همان پسوند دندانی هندواروپایی *-eto-/-oto- است که بعدها به قیاس اسم‌مفعول تحلیل شده است. این حلقه بی‌مناقشه است و کلاین و واتکینز هر دو آن را می‌آورند؛ ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/naked\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the book gives no reference for this box; the parent Germanic box cites AHD, which covers 'Old English nacod, naked: NAKED'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. naked (leaf 549 ≈ pp. 1025-1026)\", \"stance\": \"supports\", \"note\": \"'naked, adj., entirely unclothed; bare; nude. — ME. naked, fr. OE. nacod'.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. nogʷ-; index 'NAKED nogʷ-'\", \"stance\": \"supports\", \"note\": \"'... in Old English nacod, naked: NAKED'; the index at AHD_watkins1985.txt line 1900 has 'NAKED nogʷ-'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. naked\", \"stance\": \"supports\", \"note\": \"'Old English nacod \\\"nude, unclothed, bare\\\"'.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Latin\", \"words\": \"nudus\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin nūdus 'naked, bare' goes back to *nogʷ-edo- (Watkins: 'Suffixed form *nogʷ-edo- in Latin nūdus, naked: NUDE, NUDI-; DENUDE'); Klein spells the intermediate stage out: 'L. nudus [fr. *now(e)dos, for I.-E. *nogʷedhos]' — i.e. *gʷ > Lat. w before a vowel, then the sequence *-owe- contracts with loss of -w- to give ū. Ernout-Meillet s.v. nudus assign it the same suffix ('*-edo- dans lat. nudus') beside *-no- in Skt. nagnáḥ and *-to- in OIr. nocht. Gloss 'naked' correct; the word is old (Ennius) and pan-Romance except Romanian.\",\n  \"derivation_fa\": \"لاتینی nūdus «برهنه، عریان» از *nogʷ-edo- است (واتکینز: «*nogʷ-edo- در لاتینی nūdus»). کلاین مرحلهٔ میانی را روشن می‌کند: «nudus از *now(e)dos و آن از هندواروپایی *nogʷedhos» — یعنی *gʷ پیش از واکه در لاتینی به w بدل شده و سپس زنجیرهٔ *-owe- با افتادن w کشیده و به ū تبدیل شده است. ارنو-مِیه نیز در مدخل nudus همین پسوند را می‌دهند («*-edo- در لاتینی nudus») در برابر *-no- در سنسکریت nagnáḥ و *-to- در ایرلندی کهن nocht. معنی «برهنه» درست است و واژه از انیوس به بعد گواهی شده و در سراسر زبان‌های رومی (جز رومانیایی) برجاست. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/nude\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. nogʷ-: '2. Suffixed form *nogʷ-edo- in Latin nūdus, naked: NUDE, NUDI-; DENUDE' (AHD_watkins1985.txt line 787).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"s.v. nudus (LAT.txt line 42284, leaf 815 ≈ p. 797)\", \"stance\": \"supports\", \"note\": \"Ernout-Meillet: 'nudus, -a, -um: nu, dénudé ... *-no- dans skr. nagnáh et *-eno- dans v.isl. nakinn, *-etoto- dans v.isl. nekkuidr, got. naqaþs et *-to- dans irl. nocht, gall. noeth, *-edo- dans lat. nudus'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. nude (leaf 567 ≈ pp. 1060-1061)\", \"stance\": \"supports\", \"note\": \"'nude, adj., naked bare, unclothed. — L. nudus, \\\"naked, bare\\\", fr. *now(e)dos for I.-E. *nogʷedhos'.\"},\n    {\"src\": \"POK\", \"where\": \"p. 769\", \"stance\": \"supports\", \"note\": \"'with dental formants: Latin nūdus \\\"naked\\\" from *nogʷed(h)os or *nogʷod(h)os'.\"},\n    {\"src\": \"LEW\", \"where\": \"LEW_1910.txt, grep 'nudus'\", \"stance\": \"silent\", \"note\": \"the 1910 Walde on disk yields no readable hit for nudus (OCR gap); Ernout-Meillet used instead.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"nude\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English nude is a learned Latin borrowing, not an inherited form: Latin nūdus was taken directly into English in the 1530s as a legal term ('unsupported, not formally attested', as in nude pact), the ordinary sense 'unclothed' following, and the art-historical noun ('a nude') dating from 1708. Klein: 'nude, adj. ... — L. nudus'. So the chart's Latin > English arrow is right, and 'nude' is a doublet of inherited 'naked' at node #5.\",\n  \"derivation_fa\": \"«nude» انگلیسی وام‌واژه‌ای دانشورانه از لاتین است، نه صورتی موروثی: nūdus لاتینی در دههٔ ۱۵۳۰ نخست به‌عنوان اصطلاح حقوقی («بی‌پشتوانه»، در ترکیب nude pact) به انگلیسی راه یافت، سپس معنی «بی‌جامه» و در ۱۷۰۸ کاربرد اسمی آن در هنر پدید آمد. کلاین: «nude از لاتینی nudus». پس پیکان لاتین > انگلیسی درست است و nude با naked موروثی (گرهٔ ۵) دوگانه (doublet) می‌سازد.\",\n  \"sources\": [\"https://www.etymonline.com/word/nude\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no reference in the box; the parent Latin box cites AHD, whose nogʷ- entry lists 'NUDE, NUDI-; DENUDE' among the English words from Latin nūdus.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. nude (leaf 567 ≈ pp. 1060-1061)\", \"stance\": \"supports\", \"note\": \"'nude, adj., naked bare, unclothed. — L. nudus ... See naked.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. nude\", \"stance\": \"supports\", \"note\": \"'from Latin nudus \\\"naked, bare, unclothed, stripped\\\"'; adjective 1530s (legal sense), noun 1708.\"},\n    {\"src\": \"AHD\", \"where\": \"index 'NUDI- nogʷ-'\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1944 lists NUDI- under nogʷ-.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Indo-European\", \"words\": \"Gumnos, Gunos\", \"verdict\": \"disputed\",\n  \"derivation\": \"The box reproduces Mann, IEC 364 word for word: 'gumnos (gunos) \\\"comely, beautiful\\\". Cf. gumiə (gunio). Per. cf. na-γam (\\\"ugly\\\", fr. *n-?); Gk. gumnós \\\"naked; lightly clad\\\" beside gános \\\"beauty\\\"; gánumai \\\"be cheerful\\\"; Lat. vinnus \\\"luxuriant, dainty, easygoing, wanton\\\"; OE cymen ...'. So the reference checks out — but the reconstruction itself is Mann's alone and is rejected everywhere else. Pokorny 769 puts Greek γυμνός inside *nogʷ- ('hieher wohl auch gr. γυμνός, bei Hes. λυμνός', WP II 339); Watkins derives it as 'Suffixed form *nogʷ-mo- differentiated or developed into Greek gumnos'; Wiktionary (with Beekes) has γυμνός 'from Proto-Indo-European *nogʷnós by metathesis (possible taboo deformation) ... from *nogʷós \\\"naked\\\"'. Mann himself, in his own entry nogudos/nogumnos (IEC 848), writes that 'the antecedents of ... Gk. gumnós \\\"naked\\\", < *n-gum-? are obscure' — i.e. he does not link that Greek word to his gumnos 'comely'. There is thus no independently reconstructible IE *gumnos/*gunos 'beautiful': the Greek 'beauty' words γάνος, γάνυμαι belong to a separate root, and γυμνός is the taboo-deformed reflex of *nogʷ-no-/*nogʷ-mo-. Nourai's placement of the node under his Nogw root is right in the end; the intermediate 'IE Gumnos, Gunos: beautiful' is not.\",\n  \"derivation_fa\": \"این جعبه عیناً مدخل مان (فرهنگ مقایسه‌ای هندواروپایی، ص ۳۶۴) است: «gumnos (gunos) «خوش‌رو، زیبا» ... فارسی na-γam «زشت»؛ یونانی gumnós «برهنه» در کنار gános «زیبایی»؛ لاتینی vinnus ...». پس ارجاع نورایی درست است، اما بازسازیِ خودِ مان در جای دیگری پذیرفته نشده است. پوکورنی (ص ۷۶۹) و والده-پوکورنی (ج ۲ ص ۳۳۹) γυμνός یونانی را زیر همان *nogʷ- می‌آورند؛ واتکینز آن را از *nogʷ-mo- می‌گیرد؛ و ویکی‌واژه به پیروی از بیکس می‌گوید γυμνός از *nogʷnós با قلب (metathesis) و احتمالاً دگرگونی تابویی پدید آمده است. خودِ مان هم در مدخل دیگرش (ص ۸۴۸) پیشینهٔ γυμνός را «تاریک» می‌خواند و آن را به gumnos «زیبا» نمی‌بندد. بنابراین واژه‌ای هندواروپایی به معنی «زیبا» با این صورت بازسازی‌شدنی نیست: پژوهش امروزی این گره میانی را رد می‌کند، هرچند جای دادن مجموعه زیر ریشهٔ Nogw درست است.\",\n  \"sources\": [W+\"%CE%B3%CF%85%CE%BC%CE%BD%CF%8C%CF%82\", W+\"Reconstruction:Proto-Indo-European/neg%CA%B7-\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:364\", \"status\": \"supports\", \"note\": \"Mann, IEC leaf 212 (the leaf carries the printed page number 364, and the running head reads 'gulio — gumnos (gunos)'): 'gumnos (gunos) \\\"comely, beautiful\\\" ... Per. cf. na-γam (\\\"ugly\\\", fr. *n-?); Gk. gumnós \\\"naked; lightly clad\\\" beside gános \\\"beauty\\\" ...; Lat. vinnus \\\"luxuriant, dainty, easygoing, wanton\\\"'. The reference is exactly what the box says.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 769 s.v. nogʷ-\", \"stance\": \"contradicts\", \"note\": \"'hieher also gr. γυμνός, by Hes. λυμνός (for *νυμνός)' — Greek gumnos is a reflex of nogʷ- itself, not of a separate root meaning 'beautiful'.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. nogʷ-\", \"stance\": \"contradicts\", \"note\": \"'3. Suffixed form *nogʷ-mo- differentiated or developed into Greek gumnos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPERM.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 339\", \"stance\": \"contradicts\", \"note\": \"'hieher wohl auch gr. γυμνός, bei Hes. λυμνός und ἀπολύγματος ἀπογύμνωσις' — again under nogʷ-.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. nogudos, nogutos (leaf 473, p. 848)\", \"stance\": \"partial\", \"note\": \"Mann's own other entry: 'The antecedents of Per. nang, Kurd. neng \\\"shameful\\\" and of Gk. gumnós \\\"naked\\\", < *n-gum-? are obscure' — he does not himself connect γυμνός with gumnos 'comely'.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. γυμνός, Etymology\", \"stance\": \"contradicts\", \"note\": \"'From Proto-Indo-European *nogʷnós by metathesis (possible taboo deformation; if the metathesis didn't happen we would have *νυγνός), from *nogʷós (\\\"naked\\\").'\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"Persian\", \"words\": \"na-ğâm «نغام»\", \"verdict\": \"disputed\",\n  \"derivation\": \"The word is real. Borhan-e Qateʿ (bayān 14, 'در نون با عین نقطه‌دار') has 'نغام، بفتح اول بر وزن سلام، بمعنی زشت و ناخوش باشد — و تیره‌رنگ و سیه‌فام را نیز گویند'; Moʿin's Farhang gives 'نغام (ص.) زشت و ناخوش. تیره‌رنگ، سیه‌فام' and also 'ذرات گرد و غبار پراکنده در هوا'; Dehkhoda 'زشت‌نمای. زشت. ناخوش. بد ... تیره‌گون. بی‌رونق. گردآلود'. What is disputed is the analysis. Nourai's 'na-ğâm = not beautiful' (with his cross-reference to root 'Ne 1', the negative) is taken straight from Mann IEC 364, where it appears as 'Per. cf. na-γam (\\\"ugly\\\", fr. *n-?)' — flagged with a query by Mann himself. It requires a Persian *غام 'beautiful' which is nowhere attested in Borhan, Moʿin, Dehkhoda or Loghat-e Fors, and Persian غ is not a regular reflex of IE *gu-. The Persian lexicographical tradition instead ties the word to its doublet نفام and to فام 'hue, colour' (whence سیه‌فام, تیره‌فام): Moʿin's footnote to Borhan reports Jahangiri's judgement that 'نفام به فا به معنی سیاه‌رنگ و تیره‌فام است و نغام به غین به معنی زشت و ناخوش' and Rashidi's that both are correct and mean 'dark' ('تیرگی را زشتی و ناخوشی لازم است'). The oldest citation, Daqiqi in Loghat-e Fors (ed. Eqbal p. 337), is unambiguously about dust-darkening: 'بخیزد یکی گرد تند از میان / که روی اندر آن گرد گردد نغام'. Nourai's Nāser-Khosrow line is later. No modern etymological treatment derives the word from a negated IE *gum-no- 'beautiful'; the segmentation is a folk etymology carried over from Mann.\",\n  \"derivation_fa\": \"خودِ واژه واقعی است: برهان قاطع (بیان چهاردهم، «در نون با عین نقطه‌دار») می‌آورد «نغام، بفتح اول بر وزن سلام، بمعنی زشت و ناخوش باشد — و تیره‌رنگ و سیه‌فام را نیز گویند»؛ فرهنگ معین «زشت و ناخوش. تیره‌رنگ، سیه‌فام» و نیز «ذرات گرد و غبار پراکنده در هوا»؛ دهخدا «زشت‌نمای، زشت، ناخوش، بد؛ تیره‌گون، بی‌رونق، گردآلود». آنچه مورد اختلاف است تجزیهٔ واژه است. تحلیل نورایی (نه + غام «زیبا») مستقیماً از مان (ص ۳۶۴) گرفته شده که خود آن را با علامت پرسش آورده است؛ این تحلیل به واژهٔ فارسی *«غام» به معنی «زیبا» نیاز دارد که در برهان و معین و دهخدا و لغت فرس هیچ گواهی ندارد، و «غ» فارسی نیز بازماندهٔ منظم *gu- هندواروپایی نیست. سنّت فرهنگ‌نویسی فارسی آن را به دوگانهٔ «نفام» و به «فام» (رنگ، گونه؛ سیه‌فام، تیره‌فام) می‌بندد: معین در حاشیهٔ برهان قاطع، داوری جهانگیری را نقل می‌کند که «نفام به فا به معنی سیاه‌رنگ و تیره‌فام است و نغام به غین به معنی زشت و ناخوش»، و رشیدی هر دو را درست و به معنی «تیره» می‌داند. کهن‌ترین شاهد، بیت دقیقی در لغت فرس (چاپ اقبال، ص ۳۳۷)، آشکارا از تیره‌شدن با گرد و غبار سخن می‌گوید. پس پژوهش امروزی تجزیهٔ «نه + غام» را رد می‌کند و آن را ریشه‌شناسی عامیانه می‌شمارد.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%86%D8%BA%D8%A7%D9%85/\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:364\", \"status\": \"supports\", \"note\": \"Mann, IEC p. 364 s.v. gumnos: 'Per. cf. na-γam (\\\"ugly\\\", fr. *n-?)' — the box is faithful to its source, query mark included.\"},\n    {\"ref\": \"MON:4760\", \"status\": \"partial\", \"note\": \"Moʿin does have the entry — 'نغام: (ص.) زشت و اخوش [=ناخوش]. تیره رنگ، سیه‌فام' (MON_part2.txt line 77262), with a long note at line 77490 on the نغام/نفام variation — but he gives NO etymology, so the reference supports the word and gloss and not the derivation. The MON copy on disk is the 2-vol Adena reprint (own pagination), so p. 4760 of the 6-vol print could not be located.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol. 4, bayān 14 (incoming/BQT/BQT_v4_pages.txt line 9240, [pdf page 231-232])\", \"stance\": \"partial\", \"note\": \"'نغام ۹ « بفتح اول بروزن سلام » بمعنی زشت و ناخوش باشد - و تیره رنگ و سیه فام را نیز گویند'; Moʿin's footnote 9: 'نغام، زشت‌نما و تیره‌گون و بی‌رونق باشد. دقیقی (طوسی) گوید: بخیزد یکی تند گرد از میان / که روی اندر آن گرد گردد نغام. «لغت فرس ص ۳۳۷»' — word and gloss confirmed, no etymology offered.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 77262, 77490 ff.\", \"stance\": \"partial\", \"note\": \"the entry plus the note quoting Jahangiri ('نفام به فا به معنی سیاه رنگ و تیره فام است و نغام به غین به معنی زشت و ناخوش') and Rashidi — an association with فام 'hue', not with a word for 'beautiful'.\"},\n    {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'نغام'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary of Persian has no entry (grep returns nothing).\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn does not treat نغام.\"},\n    {\"src\": \"Dehkhoda/abadis\", \"where\": \"abadis.ir/fatofa/نغام\", \"stance\": \"partial\", \"note\": \"'زشت نمای. زشت. ناخوش. بد ... تیره گون. بی رونق. گردآلود'; Daqiqi's verse cited — 'dust-darkened' is the primary sense; no IE etymology.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"Latin\", \"words\": \"vinnus\", \"verdict\": \"disputed\",\n  \"derivation\": \"Mann IEC 364 really does print 'Lat. vinnus \\\"luxuriant, dainty, easygoing, wanton\\\"', so the box is faithful to its reference — but the Latin data are wrong twice. First, the form: Latin vinnus is a single gloss in Isidore (Gramm.) explaining cincinnus — 'uinnus, cincinnus molliter flexus', i.e. 'a softly curled lock of hair' — and Ernout-Meillet add 'si toutefois uinnus n'est pas inventé pour expliquer uinnulus', suspecting it was coined to gloss the adjective. Second, the meaning: it is vinnulus, -a, -um that means 'soft, charming, effeminate' (Plautus, Asinaria 223 'oratione uinnula, uenustula'; Paulus-Festus 517,6 'dicitur molliter se gerens et minime uiriliter quid faciens'; Thes. Gloss. 'uinnulus, mollis, blandus'), not vinnus 'wanton'. Third, the etymology: Ernout-Meillet class the word as an 'adjectif expressif, sans étymologie sûre' — no IE reconstruction at all, and nothing connecting it with Greek γυμνός or with a root for 'naked/beautiful'. The 1910 Walde and Pokorny do not list it. So this arrow has no support outside Mann.\",\n  \"derivation_fa\": \"مان در فرهنگ خود (ص ۳۶۴) به‌راستی «لاتینی vinnus «سرزنده، نازنین، هرزه»» را آورده است، پس جعبه به منبعش وفادار است؛ اما دادهٔ لاتینی از سه سو نادرست است. یکم صورت: vinnus در لاتینی تنها یک بار در «گرامر» ایزیدور به‌عنوان توضیح cincinnus آمده است — «uinnus, cincinnus molliter flexus» یعنی «طرّهٔ نرم پیچیده» — و ارنو-مِیه می‌افزایند که شاید همین صورت را برای توضیح صفت uinnulus ساخته باشند. دوم معنا: آنچه «نرم، دلربا، زن‌صفت» معنی می‌دهد صفت uinnulus است (پلاؤتوس، Asinaria ۲۲۳: oratione uinnula, uenustula؛ پاؤلوس-فستوس ۵۱۷٫۶)، نه vinnus «هرزه». سوم ریشه: ارنو-مِیه آن را «صفتی حسّی و بی ریشه‌شناسی مطمئن» می‌خوانند؛ نه بازسازی هندواروپایی دارد و نه پیوندی با γυμνός یونانی. پوکورنی و والدهٔ ۱۹۱۰ نیز آن را نمی‌آورند. پس این پیکان بیرون از کتاب مان هیچ پشتوانه‌ای ندارد و پژوهش امروزی آن را رد می‌کند.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"IEC:364\", \"status\": \"supports\", \"note\": \"Mann, IEC p. 364 s.v. gumnos: 'Lat. vinnus \\\"luxuriant, dainty, easygoing, wanton\\\"' — the box faithfully copies the reference; the reference is what is at fault.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"s.v. uinnulus / uinnus (LAT.txt lines 68794-68803, leaf 1321 ≈ p. 1303)\", \"stance\": \"contradicts\", \"note\": \"Ernout-Meillet: 'uinnulus, -a, -um: — dicitur molliter se gerens et minime uiriliter quid faciens, P.F.517,6; cf. un seul ex. dans Pl., As.223, oratione uinnula, uenustula ... De uinnus doublet de cincinnus, cité par Isid., Gr.3: uinnus, cincinnus molliter flexus (si toutefois uinnus n'est pas inventé pour expliquer uinnulus) ... Adjectif expressif, sans étymologie sûre.'\"},\n    {\"src\": \"LEW\", \"where\": \"LEW_1910.txt, grep 'vinnul|vinnus|uinnul'\", \"stance\": \"silent\", \"note\": \"no hit in the 1910 Walde on disk.\"},\n    {\"src\": \"POK\", \"where\": \"POK_full.txt, grep 'vinnul|vinnus'\", \"stance\": \"silent\", \"note\": \"Pokorny does not list the word under nogʷ- (p. 769) or anywhere the grep reaches.\"}\n  ]\n },\n {\n  \"id\": 11, \"lang\": \"Greek\", \"words\": \"gumnos; gumnazein\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Both Greek words are correct as given. γυμνός 'naked, lightly clad' is the Greek reflex of the *nogʷ- family: Watkins has 'Suffixed form *nogʷ-mo- differentiated or developed into Greek gumnos', while Wiktionary/Beekes derive it 'from Proto-Indo-European *nogʷnós by metathesis (possible taboo deformation; if the metathesis didn't happen we would have *νυγνός)'; the u-vocalism is the labial colouring left by the labiovelar (as in νύξ beside Latin nox), and Hesychius' variant λυμνός shows how unstable the initial was. From it the denominative verb γυμνάζειν 'to practice gymnastic exercises', literally 'to train naked' — Nourai's gloss is verbatim Klein's — and the noun γυμνάσιον 'training ground'; Greek athletes did compete naked, so the semantics are literal, not figurative. Only the parent arrow (from node #8) is objectionable; hung directly off the Nogw root box, this node is right.\",\n  \"derivation_fa\": \"هر دو واژهٔ یونانی درست است. γυμνός «برهنه، سبک‌جامه» بازماندهٔ یونانی خانوادهٔ *nogʷ- است: واتکینز آن را از *nogʷ-mo- می‌گیرد و ویکی‌واژه به پیروی از بیکس از *nogʷnós با قلب (metathesis) و احتمالاً دگرگونی تابویی — چه اگر قلب رخ نداده بود *νυγνός می‌داشتیم. واکهٔ u بازماندهٔ رنگ‌پذیری از همخوان لبی‌کامی است (چنان‌که در νύξ در برابر nox لاتینی)، و صورت λυμνός در هزیخیوس نشان می‌دهد که همخوان آغازین چه اندازه ناپایدار بوده است. از همین واژه فعل مشتق γυμνάζειν «ورزش کردن»، تحت‌اللفظ «برهنه تمرین کردن» (همان تعریف کلاین که نورایی آورده) و اسم γυμνάσιον «ورزشگاه» ساخته شده است؛ ورزشکاران یونانی به‌راستی برهنه مسابقه می‌دادند، پس معنا تحت‌اللفظی است نه مجازی. تنها ایراد، جعبهٔ میانی (گرهٔ ۸) است؛ این گره اگر یکسر زیر ریشهٔ Nogw آویخته شود درست است.\",\n  \"sources\": [W+\"%CE%B3%CF%85%CE%BC%CE%BD%CF%8C%CF%82\", \"https://www.etymonline.com/word/gymnasium\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. nogʷ-: '3. Suffixed form *nogʷ-mo- differentiated or developed into Greek gumnos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPERM'; index 'GYMNASIUM nogʷ-' (AHD_watkins1985.txt lines 787, 1573).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 769\", \"stance\": \"supports\", \"note\": \"'hieher also gr. γυμνός, by Hes. λυμνός (for *νυμνός) und ἀπολύγματος ἀπογύμνωσις'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. gymnasium, gymno- (leaf 372, pp. 690-691)\", \"stance\": \"supports\", \"note\": \"'gymnasium ... fr. Gk. γυμνάσιον, \\\"gymnastic school, school\\\", fr. γυμνάζειν, \\\"to practice gymnastic exercises\\\", lit. \\\"to train naked\\\", fr. γυμνός, \\\"naked\\\"; so called because the athletes trained naked'; 'gymno- ... fr. γυμνός, \\\"naked\\\", cogn. with OI. nagnáh, L. nudus, Goth. naqaþs, OE. nacod'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 339\", \"stance\": \"supports\", \"note\": \"puts γυμνός under nogʷ- and refers to the attempts to explain its phonology.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. γυμνός\", \"stance\": \"supports\", \"note\": \"'From Proto-Indo-European *nogʷnós by metathesis (possible taboo deformation) ... from *nogʷós (\\\"naked\\\")'.\"}\n  ]\n },\n {\n  \"id\": 12, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"A pass-through box, printed empty in the book (verified on the page image, pdf p. 369). The forms intended are French gymnastique (adjective 1571, noun feminine 'la gymnastique' by the end of the 18th c.) and gymnase, learned borrowings of Latin gymnasticus / gymnasium, themselves from Greek γυμναστικός / γυμνάσιον. In French the Greek/Latin initial gy- is pronounced [ʒi], which is what makes the box necessary: it is the link through which the word reached Persian as ژیمناستیک (node #13), whereas English took its own gymnasium straight from Latin (node #14).\",\n  \"derivation_fa\": \"این جعبه در کتاب خالی چاپ شده است (بر تصویر صفحهٔ ۳۶۹ نسخهٔ پی‌دی‌اف بازبینی شد) و نقش گذرگاه دارد. صورت‌های مورد نظر فرانسوی gymnastique (صفت ۱۵۷۱، اسم مؤنث در پایان سدهٔ هجدهم) و gymnase است، که وام‌واژه‌های دانشورانه از لاتینی gymnasticus / gymnasium و در نهایت از یونانی γυμναστικός / γυμνάσιον هستند. در فرانسوی gy- آغازین [ʒi] تلفظ می‌شود و همین نکته وجود این جعبه را لازم می‌کند: واژه از همین راه به فارسی «ژیمناستیک» رسیده است (گرهٔ ۱۳)، در حالی که انگلیسی gymnasium را یکسر از لاتین گرفته است (گرهٔ ۱۴).\",\n  \"sources\": [\"https://www.etymonline.com/word/gymnasium\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference and no word; it is a blank connector in the printed book.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. gymnasium (leaf 372, pp. 690-691)\", \"stance\": \"supports\", \"note\": \"gives the Latin/Greek chain that French shares: 'L., fr. Gk. γυμνάσιον ... fr. γυμνάζειν'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. gymnasium\", \"stance\": \"partial\", \"note\": \"traces gymnasium/gymnastic through Latin and Greek and notes the German use for 'high school'; it does not itself make French the intermediary for English, which is why the French box only feeds the Persian one here.\"}\n  ]\n },\n {\n  \"id\": 13, \"lang\": \"Persian\", \"words\": \"žimnâstîk «ژیمناستیک»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"A twentieth-century French loanword, and the arrow French > Persian is exactly right. Persian ژیمناستیک žimnāstīk renders French gymnastique [ʒimnastik]: Persian ژ /ʒ/ is the regular substitute for French initial g- before i/y (pronounced [ʒ]), the French nasal-free -ast- is kept, and -ique is naturalised as -یک. Both dictionaries tag the word as French: Moʿin '[فر.]' and Dehkhoda '[فرانسوی] ورزش بدنی با اسبابهای مختلف از قبیل پارالل و بارفیکس و دارحلقه'. It is therefore not an inherited Iranian word at all but a borrowing that re-imports the Greek root into Persian — the mirror image of the inherited برهنه at node #3, which reaches Persian from the same PIE root by descent.\",\n  \"derivation_fa\": \"«ژیمناستیک» وام‌واژه‌ای فرانسوی از سدهٔ بیستم است و پیکان فرانسوی > فارسی دقیقاً درست است. این صورت، gymnastique فرانسوی [ʒimnastik] را بازمی‌نمایاند: «ژ» فارسی جانشین منظم g- آغازین فرانسوی پیش از i/y است (که در فرانسوی [ʒ] تلفظ می‌شود) و پسوند -ique به -یک فارسی بدل شده است. معین با برچسب [فر.] و دهخدا با «فرانسوی» هر دو آن را وام‌واژهٔ فرانسوی می‌دانند. پس این واژه میراث ایرانی نیست بلکه وام‌گیری تازه‌ای است که ریشهٔ یونانی را دوباره به فارسی آورده — آیینهٔ وارونهٔ «برهنه» در گرهٔ ۳ که از همان ریشهٔ هندواروپایی، اما از راه توارث، به فارسی رسیده است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%DA%98%DB%8C%D9%85%D9%86%D8%A7%D8%B3%D8%AA%DB%8C%DA%A9/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:1779\", \"status\": \"supports\", \"note\": \"Moʿin's entry for ژیمناستیک is tagged '[فر.]' (French) and glossed 'ورزشی است به منظور پرورش و آماده سازی بدن ...' (read via abadis.ir, section فرهنگ معین); the local MON copy is the 2-vol reprint, so the 6-vol page 1779 itself could not be located, but MON_part1.txt line 73289 has 'ژیمناستیک: ... ورزش بدنی'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/ژیمناستیک, section فرهنگ معین; MON_part1.txt line 73289\", \"stance\": \"supports\", \"note\": \"origin tag [فر.] = French.\"},\n    {\"src\": \"Dehkhoda/abadis\", \"where\": \"abadis.ir/fatofa/ژیمناستیک, section لغت‌نامه دهخدا\", \"stance\": \"supports\", \"note\": \"'[فرانسوی] ورزش بدنی با اسبابهای مختلف از قبیل پارالل و بارفیکس و دارحلقه و غیره'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. gymnasium (pp. 690-691)\", \"stance\": \"supports\", \"note\": \"supplies the Greek > Latin end of the chain that French passed on.\"}\n  ]\n },\n {\n  \"id\": 14, \"lang\": \"English\", \"words\": \"gymnasium, gymnastics, gym\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three are Greek by way of Latin, and the chart is right to hang them on the Greek box rather than on the French one: gymnasium (1590s) is Latin gymnasium < Gk. γυμνάσιον 'public place where athletic exercises are practised'; gymnastic (1570s) is Latin gymnasticus < Gk. γυμναστικός 'fond of or skilled in bodily exercise', from γυμνάζειν, whence the plural noun gymnastics; gym (1871) is US student slang, a clipping of gymnasium. Watkins indexes GYMNASIUM, GYMNAST, GYMNOSOPHIST and GYMNOSPERM all under nogʷ-.\",\n  \"derivation_fa\": \"هر سه واژه از یونانی و از راه لاتین به انگلیسی رسیده‌اند و نمودار به‌درستی آن‌ها را زیر جعبهٔ یونانی آویخته است، نه زیر جعبهٔ فرانسوی: gymnasium (دههٔ ۱۵۹۰) از لاتینی gymnasium و آن از یونانی γυμνάσιον «میدان ورزش عمومی»؛ gymnastic (دههٔ ۱۵۷۰) از لاتینی gymnasticus و آن از یونانی γυμναστικός «ورزش‌دوست، ورزیده» از γυμνάζειν، که جمعِ اسمی آن gymnastics شده است؛ و gym (۱۸۷۱) کوتاه‌شدهٔ gymnasium در زبان دانشجویی آمریکا. واتکینز هر چهار واژهٔ GYMNASIUM و GYMNAST و GYMNOSOPHIST و GYMNOSPERM را زیر ریشهٔ nogʷ- فهرست می‌کند. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/gymnasium\"],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no reference in the box; the parent Greek box cites AHD, whose nogʷ- entry ends 'GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPERM'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. gymnasium, gymnast, gymkhana (leaf 372, pp. 690-691)\", \"stance\": \"supports\", \"note\": \"'gymnasium, n., 1) a building equipped for gymnastics ... — L., fr. Gk. γυμνάσιον'; 'gymnast, n. ... — Gk. γυμναστής, \\\"trainer of athletes\\\", fr. γυμνάζειν'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. gymnasium\", \"stance\": \"supports\", \"note\": \"'Gymnasium (1590s): from Latin gymnasium, from Greek gymnasion ... Gymnastic (1570s) ... Gym (1871): U.S. student slang, abbreviated form of gymnasium.'\"},\n    {\"src\": \"AHD\", \"where\": \"index, line 1573\", \"stance\": \"supports\", \"note\": \"'GYMNASIUM nogʷ- GYMNAST nogʷ- GYMNOSOPHIST nogʷ- GYMNOSPERM nogʷ-'.\"}\n  ]\n }\n]\n\ne1_nodes = [\n {\n  \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"naktin\", \"verdict\": \"disputed\",\n  \"derivation\": \"There is no Old Persian *naktin — indeed no Old Persian reflex of *nokʷt- at all. The Achaemenid inscriptions use xšap- 'night' (DB I 20 xšapavā raučapativā 'either by night or by day'); Kent, Old Persian §88 lists 'xšap- \\\"night\\\"' among the p-stems, and Buck 14.42 gives 'Av., OPers. xšap-' for 'night', remarking that in Indo-Iranian, apart from Vedic relics, 'the old word was displaced by others'. The form in the box comes from Nourai's own source, but there it is OLD PRUSSIAN: Mann, IEC 850 s.v. noktis, nokts writes 'I-stem in Skt. (Vedic) náktih, f.; OPr. naktin, acc. sg.' — the item immediately after the Sanskrit form that fills the next box of this very chart — and his separate entry noktím reads 'OPr. naktin \\\"by night\\\"'. Mann's abbreviation for Persian is 'Per.' (cf. 'Per. cf. na-γam' at IEC 364), so 'OPr.' cannot be Persian. Walde-Pokorny II 338 has the same form as 'apr. naktin (Akk. Sg.) \\\"Nacht\\\"' (apr. = altpreußisch) and Pokorny 762 as 'Old Prussian naktin (Akk. Sg.)'. Wiktionary's *nókʷts lists no Old Persian descendant at all. The box is therefore a misreading of 'OPr.' as 'Old Persian', promoting an Old Prussian accusative singular to an Old Persian lemma. The JSON matches the printed page, so this is the author's error, not the extraction's.\",\n  \"derivation_fa\": \"«naktin» پارسی باستان وجود ندارد؛ در پارسی باستان هیچ بازماندهٔ *nokʷt- گواهی نشده است. سنگ‌نوشته‌های هخامنشی برای «شب» xšap- به کار می‌برند (بیستون ستون ۱ بند ۲۰: xšapavā raučapativā «چه به شب چه به روز»)؛ کنت در دستور پارسی باستان (بند ۸۸) xšap- «شب» را در شمار ستاک‌های p-دار می‌آورد و باک (بند ۱۴٫۴۲) نیز «اوستایی و پارسی باستان xšap-» می‌دهد و می‌افزاید که در هندوایرانی، جز بازمانده‌های وِدایی، واژهٔ کهن جای خود را به واژه‌های دیگر داده است. صورت این جعبه از منبع خودِ نورایی می‌آید، اما در آن منبع «پروسی کهن» است نه «پارسی باستان»: مان در ص ۸۵۰ می‌نویسد «ستاک i-دار در سنسکریت (وِدایی) náktih؛ OPr. naktin، رایی مفرد» — همان مدخلی که صورت سنسکریت جعبهٔ بعدی همین نمودار نیز از آن گرفته شده — و در مدخل noktím می‌آورد «OPr. naktin «به شب»». نشانهٔ اختصاری مان برای فارسی «Per.» است (سنجید با «Per. cf. na-γam» در ص ۳۶۴)، پس OPr. نمی‌تواند فارسی باشد. والده-پوکورنی (ج ۲ ص ۳۳۸) همین صورت را «apr. naktin (رایی مفرد)» یعنی پروسی کهن می‌آورد و پوکورنی (ص ۷۶۲) نیز «Old Prussian naktin». ویکی‌واژه در مدخل *nókʷts هیچ بازماندهٔ پارسی باستان فهرست نمی‌کند. پس این جعبه خطای خوانش «OPr.» به «Old Persian» است: پژوهش امروزی آن را رد می‌کند. متن جیسون با صفحهٔ چاپی یکی است، پس خطا از مؤلف است نه از استخراج.\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:850\", \"status\": \"contradicts\", \"note\": \"Mann, IEC leaf 474 (printed pp. 849-850) s.v. noktis, nokts: 'I-stem in Skt. (Vedic) náktih, f.; OPr. naktin, acc. sg.; Tokh. noktin and niktin \\\"toward evening\\\"; Lat. nox ...' (OCR renders 'OPr.' as 'Ober'), and s.v. noktím: 'Skt. náktam id.; Tokh. A noktin \\\"in the evening\\\"; MHG nehten \\\"last night\\\"; OPr. naktin \\\"by night\\\"; Li. nákti, id.' — the form is Old Prussian, not Old Persian.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §88 (KNT.txt line 2224) and §K (line 2672)\", \"stance\": \"contradicts\", \"note\": \"'§88 ... these include stems ending in ... p (xšap- \\\"night\\\", ap- \\\"water\\\")'; 'DB 1.20 xšapavā raučapativā ava akunavayatā \\\"either by night or by day, that was done\\\"' — the Old Persian word for night is xšap-.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.42 NIGHT (SYN.txt line 25300, leaf 1068 ≈ pp. 992-993)\", \"stance\": \"contradicts\", \"note\": \"'Av. OPers. xšap-' in the Iranian column, with 'Skt. ksap-, Av. xšap-, xšapan-, xšapar-, OPers. xšap- (Barth. 548 f.)'; and 'in Indo-Iranian, except in Vedic and a classical Skt. adv. relic, the old word was displaced by others'.\"},\n    {\"src\": \"POK\", \"where\": \"pp. 762-763\", \"stance\": \"contradicts\", \"note\": \"the Baltic paragraph reads 'Lithuanian naktis ..., Latvian nakts, Old Prussian naktin (Akk. Sg.) \\\"night\\\"' — no Iranian form of the root is cited at all.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 338\", \"stance\": \"contradicts\", \"note\": \"'lit. naktìs (kons. g. pl. naktu), lett. nakts, apr. naktin (Akk. sg.) \\\"Nacht\\\"' — apr. = altpreußisch (Old Prussian).\"},\n    {\"src\": \"TLM\", \"where\": \"TLM.txt, grep 'naktin|xšap'\", \"stance\": \"silent\", \"note\": \"Tolman's Ancient Persian Lexicon yields no hit for 'naktin' (nor a readable one for xšap-, an OCR gap); no Old Persian naktin anywhere.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/nókʷts\", \"stance\": \"contradicts\", \"note\": \"the descendant list has Sanskrit nákt-, Avestan (Younger Av. upa.naxturušu), Latin nox, Greek núx, Proto-Germanic *nahts, Proto-Balto-Slavic *náktis — and no Old Persian at all.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"naktih; naktam\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Both forms are genuine Vedic. The consonant stem appears as nom. sg. nák (< *nakt-s), the i-stem as náktiḥ (Mann: 'I-stem in Skt. (Vedic) náktih, f.'; Klein cites 'náktih (acc. pl.), \\\"nights\\\"'), and náktam is the frozen accusative used adverbially, 'at night' — in classical Sanskrit only this adverb survives, the ordinary noun being rātrī- (Buck 14.42: 'Ved. nakt- (nom. sg. nak, acc. sg. naktam), nakti- (class. Skt. only adv. naktam \\\"by night\\\")'). Phonetically the labiovelar loses its labial appendix before the dental: PIE *nokʷt- > Indo-Iranian *nakt- (with *o > a by Brugmann-independent Indo-Iranian a-merger), so Skt. kt corresponds to Latin ct and Greek κτ. Nourai's glosses ('night'; 'at night') are correct.\",\n  \"derivation_fa\": \"هر دو صورت وِدایی راستین‌اند. ستاک همخوانی در نهاد مفرد nák (< *nakt-s) و ستاک i-دار در náktiḥ دیده می‌شود (مان: «ستاک i-دار در سنسکریت وِدایی náktih مؤنث»؛ کلاین: «náktih، رایی جمع، شب‌ها»)، و náktam رایی منجمدی است که نقش قید یافته و «به شب» معنی می‌دهد؛ در سنسکریت کلاسیک تنها همین قید بازمانده و نام معمول شب rātrī- است (باک ۱۴٫۴۲). از نظر آوایی، همخوان لبی‌کامی پیش از دندانی، پیوستِ لبی خود را از دست می‌دهد: هندواروپایی *nokʷt- در هندوایرانی *nakt- شده است (با ادغام *o و *a در a)، و از این‌رو kt سنسکریت با ct لاتینی و κτ یونانی برابر است. معناهایی که نورایی داده درست است.\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts\", \"https://www.etymonline.com/word/night\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:850\", \"status\": \"supports\", \"note\": \"Mann, IEC pp. 849-850 s.v. noktis, nokts: 'I-stem in Skt. (Vedic) náktih, f. ... Cons. stem in Vedic nák, m.' — exactly the box's naktih.\"},\n    {\"ref\": \"KLN:1047\", \"status\": \"supports\", \"note\": \"Klein s.v. night (KLN_1966.txt line 25422, leaf 560 ≈ p. 1047): 'corresponding to I.-E. *noqt-, whence OI. naktam (adv. acc.), \\\"at night\\\", náktih (acc. pl.), \\\"nights\\\"' — both of the box's words with the box's glosses.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"pp. 762-763\", \"stance\": \"supports\", \"note\": \"'Old Indic nak (*nakt) Nom. \\\"night\\\" (nag jihīte), naktā Du., naktam adv. solidified Akk. \\\"at night\\\", Instr. Pl. naktabhih ds., Akk. Pl. naktīh \\\"nights\\\"'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.42 (pp. 992-993)\", \"stance\": \"supports\", \"note\": \"'Ved. nakt- (nom. sg. nak, acc. sg. naktam), nakti- (class. Skt. only adv. naktam \\\"by night\\\", cf. Wackernagel, Altind. Gram. 3.233 ff.)'.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. nekʷ-t-\", \"stance\": \"silent\", \"note\": \"Watkins gives only the Germanic, Latin and Greek branches; no Sanskrit form (AHD_watkins1985.txt line 776-779).\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/nókʷts\", \"stance\": \"supports\", \"note\": \"Sanskrit nákt- listed among the Indo-Iranian descendants.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Germanic\", \"words\": \"naht\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *nahts (a consonant stem, feminine) from *nokʷt-s: *o > Gmc a, and the labiovelar *kʷ becomes *h before *t by Grimm's law with loss of labialisation, giving *naht-. Pokorny 762 lists 'Gothic nahts (Dat. Pl. nahtam after dagam), Old Icelandic nótt, natt, Old High German, Old Saxon naht, Old English neaht, niht \\\"night\\\" (conservative stem)'; Nourai's 'naht' is precisely the OHG/OS shape (Watkins writes the branch form *naht-, Etymonline *nahts). The retention of the consonant stem in Gothic and Old English is one of the classic archaisms of this word.\",\n  \"derivation_fa\": \"ژرمنی آغازین *nahts (ستاک همخوانی، مادینه) از *nokʷt-s: *o به a بدل شده و همخوان لبی‌کامی *kʷ بر پایهٔ قانون گریم پیش از *t به *h رفته و لبی‌شدگی خود را از دست داده است، و صورت *naht- به دست آمده. پوکورنی (ص ۷۶۲) می‌آورد: «گوتی nahts (دری جمع nahtam به قیاس dagam)، نورس کهن nótt, natt، آلمانی علیای کهن و ساکسون کهن naht، انگلیسی کهن neaht, niht «شب» (ستاک همخوانی)». صورت «naht» که نورایی داده همان صورت آلمانی علیای کهن/ساکسون کهن است. برجاماندن ستاک همخوانی در گوتی و انگلیسی کهن از کهن‌ترین ویژگی‌های این واژه است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/night\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"Pokorny IEW 762-763 s.v. nekʷ-(t-), nokʷ-t-s 'night': 'Gothic nahts {Dat. Pl. nahtam after dagam}, Old Icelandic nott, natt, Old High German Old Saxon naht, Old English neaht, niht \\\"night\\\" (conservative stem)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"s.v. nekʷ-t-\", \"stance\": \"supports\", \"note\": \"'nekʷ-t-. Night. O-grade form *nokʷ-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 338\", \"stance\": \"supports\", \"note\": \"'Got. nahts (D. pl. nahtam nach dagam), aisl. nótt, naft, ahd. as. naht, ags. neaht, niht \\\"Nacht\\\" (kons. St.)'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. night (leaf 560 ≈ p. 1047)\", \"stance\": \"supports\", \"note\": \"'rel. to OS., OHG., MHG. naht ... fr. Teut. base *naht, corresponding to I.-E. *noqt-'.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. night\", \"stance\": \"supports\", \"note\": \"'from Proto-Germanic *nahts'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"English\", \"words\": \"night, nightingale\", \"verdict\": \"confirmed\",\n  \"derivation\": \"night: OE niht (West Saxon neaht, Anglian næht) > ME niht/night > NE night; the OE h [x] survives only in the spelling gh. nightingale: OE nihtegale (earliest næctigalæ) 'night-singer', a compound of niht 'night' and galan 'to sing' (related to OE giellan 'to yell', cf. Klein s.v. gale 'the last element in nightingale'); the intrusive -n- of ME nightingale is a later insertion. Only the first element belongs to this root, which is why Watkins indexes 'NIGHTINGALE ghel-1' while 'NIGHT nekʷ-t-'; Klein, s.v. night, nevertheless explicitly lists 'the first element in nightingale', so Nourai's KLN:1047 does cover both words exactly as drawn. Verdict confirmed, with the caveat that the bird's name is only half from *nekʷ-t-.\",\n  \"derivation_fa\": \"night: انگلیسی کهن niht (وِسِکسی neaht، آنگلی næht) > انگلیسی میانه niht/night > انگلیسی نو night؛ همخوان h [x] انگلیسی کهن تنها در نگارش gh بازمانده است. nightingale: انگلیسی کهن nihtegale (کهن‌ترین صورت næctigalæ) «شب‌خوان»، ترکیبی از niht «شب» و galan «سراییدن» (هم‌ریشه با giellan «بانگ زدن»)؛ «ن» میانجی در صورت انگلیسی میانه افزوده شده است. تنها جزء نخست این واژه به ریشهٔ حاضر می‌رسد و از همین رو واتکینز NIGHTINGALE را زیر ریشهٔ ghel-1 «بانگ زدن» و NIGHT را زیر nekʷ-t- فهرست می‌کند؛ با این حال کلاین در مدخل night صریحاً «جزء نخست nightingale» را می‌آورد، پس ارجاع KLN:1047 نورایی هر دو واژه را همان‌گونه که کشیده است پشتیبانی می‌کند. ادعای نورایی درست است، با این یادآوری که نام این پرنده تنها نیمی از ریشهٔ «شب» دارد.\",\n  \"sources\": [\"https://www.etymonline.com/word/night\", \"https://www.etymonline.com/word/nightingale\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1047\", \"status\": \"supports\", \"note\": \"Klein s.v. night (leaf 560 ≈ p. 1047): 'night, n. — ME. niht, night, fr. OE. neaht, niht ... Cp. nocti-, nocturnal, nycti-, the first element in nightingale, Nakshatra, and the second element in acronychal, equinox.'\"},\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins s.v. nekʷ-t- gives 'Old English niht, neaht, night: NIGHT', but his index (line 1914) puts 'NIGHTINGALE ghel-1', i.e. under 'to call' (OE galan), not under nekʷ-t-; only the first element of the compound belongs here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. gale 'a strong wind' and s.v. celandine (lines 15684, 6907)\", \"stance\": \"supports\", \"note\": \"'OE. galan, \\\"to sing\\\", giellan, \\\"to scream, cry\\\". See yell and cp. gale ... and the last element in nightingale.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. nightingale\", \"stance\": \"supports\", \"note\": \"'from Old English næctigalæ, in late Old English nihtegale ... *nakht- \\\"night\\\" ... *galon \\\"to sing\\\", related to Old English giellan \\\"to yell\\\"'.\"},\n    {\"src\": \"AHD\", \"where\": \"index lines 1914, 1929\", \"stance\": \"partial\", \"note\": \"'NIGHT nekʷ-t- NIGHTINGALE ghel-1'.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"nox, nocht; noctua\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"nox (gen. noctis) 'night' and noctua 'night-owl' are both correct and both stand in Pokorny 762 ('Latin nox, noctis \\\"night\\\" (Gen. Pl. noctium i-stem, but distinct conservative stem in Adv. nox \\\"at night\\\" from Gen. *nokt-es, -os); ... of stem *noktu-: Latin noctu \\\"by night\\\", noctua \\\"a night-owl, an owl\\\"'). Latin ct is the regular reflex of *kʷt (loss of labialisation before the dental). But the second form as printed, 'nocht', is not a Latin word: Latin has no <ch> in this paradigm, and the stem is noct-. The printed page (pdf p. 369 = book p. 339) really does read 'nox, nocht : night' — I rendered and read it — so the JSON is faithful and the misprint is Nourai's own. The likeliest source of the slip is Pokorny's own paragraph, where the Celtic forms 'Old Irish i-nnocht, ... cymr. etc. noeth' and the Insular nocht sit a few lines from the Latin ones; or a simple typo for the stem noct-. Verdict transcription_suspect with the error located in the book; the intended content of the box (nox, noct-, noctua) is confirmed.\",\n  \"derivation_fa\": \"nox (اضافی noctis) «شب» و noctua «جغد شب» هر دو درست‌اند و هر دو در پوکورنی ص ۷۶۲ آمده‌اند («لاتینی nox, noctis \\\"شب\\\" ... از ستاک *noktu-: لاتینی noctu \\\"به شب\\\"، noctua \\\"جغد\\\"»). ct لاتینی بازماندهٔ منظم *kʷt است (از دست رفتن لبی‌شدگی پیش از همخوان دندانی). اما صورت دوم، چنان‌که چاپ شده — «nocht» — واژهٔ لاتینی نیست: در این ساخت لاتینی ch ندارد و ستاک noct- است. صفحهٔ چاپی (صفحهٔ ۳۶۹ پی‌دی‌اف = ۳۳۹ کتاب) را تصویر گرفتم و خواندم: به‌راستی «nox, nocht : night» چاپ شده است، پس داده‌های استخراج‌شده امانت‌دارانه است و خطای چاپی از خودِ نورایی است. محتمل‌ترین سرچشمهٔ لغزش، همان بند پوکورنی است که در آن صورت‌های سِلتی («ایرلندی کهن i-nnocht»، «ولزی noeth») چند سطر پایین‌تر از صورت‌های لاتینی نشسته‌اند؛ یا صرفاً غلط حروف‌چینی به جای ستاک noct-. حکم: خطای چاپی کتاب؛ محتوای مورد نظر جعبه (nox، noct-، noctua) تأیید می‌شود.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"nox, nocht : night\",\n  \"correct_form\": \"nox, gen. noctis (stem noct-)\",\n  \"sources\": [\"https://www.etymonline.com/word/nocturnal\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:762\", \"status\": \"partial\", \"note\": \"Pokorny 762 has 'Latin nox, noctis \\\"night\\\" ... noctua \\\"a night-owl, an owl\\\"' — so nox and noctua are supported, but no Latin 'nocht' appears anywhere on the page; the ⟨ch⟩ forms on that page are Celtic ('Old Irish i-nnocht', 'cymr. etc. noeth'). The book's second form is a misprint.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"s.v. nox (LAT.txt line 42122, leaf ~815 ≈ p. 795-797)\", \"stance\": \"partial\", \"note\": \"Ernout-Meillet: 'nox, noctis f.: nuit; déesse de la nuit' — the paradigm is nox / noctis, with no variant nocht.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 338\", \"stance\": \"partial\", \"note\": \"'Lat. nox, noctis \\\"Nacht\\\" (g. pl. noctium i-St., aber deutlich kons. St. im Adv. nox \\\"nachts\\\" aus gen. *noqt-es, -os), nocturnus \\\"nächtlich\\\"; vom Stamme *noqtu- lat. noctu \\\"bei Nacht\\\", noctua \\\"Nachteule\\\"' — nox and noctua yes, nocht no.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. nekʷ-t-\", \"stance\": \"partial\", \"note\": \"'2. Latin nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: NOCTUID, NOCTULE.' — the stem is spelled noct-.\"},\n    {\"src\": \"BOOK\", \"where\": \"printed page, pdf 369 / book 339, Latin box of the Noktis chart (page image saved as data/verification/sources/refs/ocr/BOOK/369.png)\", \"stance\": \"supports\", \"note\": \"the page image plainly reads 'nox, nocht : night' / 'noctua : night owl', confirming that the extraction reproduced the book and that the odd form is the book's.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"English\", \"words\": \"nocti-, nocturnal, noctule\", \"verdict\": \"confirmed\",\n  \"derivation\": \"All three are Latin-derived learned words and all three are listed by Watkins under nekʷ-t-: 'Latin nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: NOCTUID, NOCTULE.' In detail: nocti- is simply the Latin combining form of the stem noct-; nocturnal comes from Late Latin nocturnalis, built on Latin nocturnus 'belonging to the night' (nox + the -urnus suffix of diurnus), partly through Old French nocturnal; noctule, the bat Nyctalus noctula, reaches English through French noctule from Italian nottola / Latin noctua 'night-owl', so it is the noctua branch rather than the nox branch — which is exactly how the chart draws it, both words sitting in the same Latin parent box.\",\n  \"derivation_fa\": \"هر سه واژه دانشورانه و لاتینی‌تبارند و هر سه در فرهنگ واتکینز زیر ریشهٔ nekʷ-t- فهرست شده‌اند: «لاتینی nox (ستاک noct-) \\\"شب\\\": NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO؛ EQUINOX. ۳. لاتینی noctua \\\"جغد شب\\\": NOCTUID, NOCTULE». به تفصیل: -nocti همان صورت ترکیبی لاتینی ستاک noct- است؛ nocturnal از لاتینی متأخر nocturnalis و آن از nocturnus «شبانه» (nox با پسوند -urnus مانند diurnus) و تا اندازه‌ای از راه فرانسوی کهن nocturnal آمده است؛ و noctule، نام خفاش Nyctalus noctula، از راه فرانسوی noctule و ایتالیایی nottola به لاتینی noctua «جغد شب» می‌رسد — یعنی به شاخهٔ noctua نه nox، و نمودار هم درست همین دو واژه را در یک جعبهٔ لاتینی کنار هم نشانده است. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/nocturnal\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. nekʷ-t- (AHD_watkins1985.txt line 779): 'Latin nox (stem noct-), night: NOCTI-, NOCTURN, NOCTURNAL, NOTTURNO; EQUINOX. 3. Latin noctua, night owl: NOCTUID, NOCTULE.' Index (line 1929): 'NOCTI- nekʷ-t- ... NOCTUID nekʷ-t- NOCTULE nekʷ-t- NOCTURN nekʷ-t- NOCTURNAL nekʷ-t-'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. night (leaf 560 ≈ p. 1047)\", \"stance\": \"supports\", \"note\": \"'Cp. nocti-, nocturnal, nycti-, the first element in nightingale ... and the second element in acronychal, equinox.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.v. nocturnal\", \"stance\": \"supports\", \"note\": \"'from Old French nocturnal or directly from Late Latin nocturnalis, from Latin nocturnus \\\"belonging to the night\\\", from nox (genitive noctis) ... ultimately PIE *nekwt-'.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol3.txt (grep 'noctule')\", \"stance\": \"silent\", \"note\": \"no readable hit for noctule in the Funk & Wagnalls OCR.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Greek\", \"words\": \"nux, nukti\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Greek νύξ, gen. νυκτός, dat. νυκτί 'night'; the compositional/oblique stem νυκτι-/νυκτο- is Nourai's 'nukti'. Pokorny 762: 'gr. νύξ, νυκτός f. \\\"night\\\", in compound νυκτι-, νυκτο-, νύκτωρ adv. \\\"at night, by night\\\"'. Phonetically κτ is the regular Greek outcome of *kʷt; the vocalism υ instead of the expected ο is the crux — Buck calls it 'prob. fr. a reduced grade' and Mann suspects an original *noqutis with u-affection ('ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti'), while the modern account takes the u as the labial residue of the lost labiovelar; the same υ appears in γυμνός at entry 0 node #11 and, in the accepted Hittite comparison, in neku- 'to become night'.\",\n  \"derivation_fa\": \"یونانی νύξ، اضافی νυκτός، دری νυκτί «شب»؛ ستاک ترکیبی/غیرفاعلی νυκτι-/νυκτο- همان «nukti» نورایی است. پوکورنی ص ۷۶۲: «یونانی νύξ, νυκτός مؤنث \\\"شب\\\"، در ترکیب νυκτι-, νυκτο-, νύκτωρ قید \\\"به شب\\\"». از نظر آوایی κτ بازماندهٔ منظم *kʷt در یونانی است؛ گره اصلی، واکهٔ υ به‌جای ο ی انتظار است — باک آن را «احتمالاً از پایهٔ کاهیده» می‌داند و مان صورت آغازین *noqutis را حدس می‌زند («با توجه به واکهٔ nux یونانی و nakvóti لیتوانیایی»)، در حالی که تحلیل امروزی υ را بازماندهٔ لبیِ همخوان لبی‌کامیِ از میان رفته می‌شمارد؛ همین υ را در γυμνός (گرهٔ ۱۱ مدخل نخست) و در سنجش پذیرفتهٔ هیتی neku- «شب شدن» نیز می‌بینیم. ادعای نورایی درست است.\",\n  \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"Pokorny 762-763: 'gr. νύξ, νυκτός f. \\\"night\\\", in compound νυκτι-, νυκτο-, νύκτωρ Adv. \\\"at night, by night\\\" ... νυκτερός, νυκτερινός \\\"nocturnal\\\" (: Latin nocturnus)'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"s.v. nekʷ-t-\", \"stance\": \"supports\", \"note\": \"'4. Greek nux (stem nukt-), night: NYCTALOPIA, NYCTITROPISM.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 337-338\", \"stance\": \"supports\", \"note\": \"'νύκτωρ Adv. \\\"nachts\\\" (*Acc. der Bildung νύχος, νύκτερος, νυκτερινός \\\"nächtlich\\\": lat. nocturnus)'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 14.42 (pp. 992-993)\", \"stance\": \"supports\", \"note\": \"'Grk. νύξ, νυκτός, NG νύχτα (υ prob. fr. a reduced grade)'.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. noktis, nokts (p. 850)\", \"stance\": \"supports\", \"note\": \"'ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti ... Cons. stem in Vedic nák, m.; Gk. nux'.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"nyctalopia\", \"verdict\": \"confirmed\",\n  \"derivation\": \"nyctalopia is a medical Latinisation of Greek νυκταλωπία, itself from νυκτάλωψ, a compound of νύξ/νυκτ- 'night' + ἀλαός 'blind' + ὄψ 'eye' — literally 'night-blind-eye'. Watkins accordingly indexes it twice, 'NYCTALOPIA nekʷ-t-, okʷ-', i.e. under this root for the first element and under okʷ- 'to see' for the last, which is exactly the analysis Wiktionary gives ('from νύξ (\\\"night\\\"), ἀλαός (\\\"blind\\\"), and ὄψ (\\\"eye\\\")'). Ancient and early modern usage wavered between 'night blindness' and 'day blindness' (Funk & Wagnalls still glosses 'nocturnal sight, day-blindness, nyctalopia'); current medical usage is 'inability to see in dim light, night blindness'. The chart's Greek > English arrow is right, the word being a learned coinage rather than an inherited form.\",\n  \"derivation_fa\": \"«nyctalopia» لاتینی‌شدهٔ پزشکی از یونانی νυκταλωπία است، و آن از νυκτάλωψ، ترکیبی از νύξ/νυκτ- «شب» + ἀλαός «کور» + ὄψ «چشم»، یعنی تحت‌اللفظ «چشمِ شب‌کور». واتکینز آن را دو بار فهرست می‌کند — «NYCTALOPIA nekʷ-t-, okʷ-» — یکی برای جزء نخست و دیگری برای جزء پایانی زیر ریشهٔ okʷ- «دیدن»؛ ویکی‌واژه هم همین تجزیه را می‌دهد. کاربرد کهن و آغاز دوران جدید میان «شب‌کوری» و «روزکوری» در نوسان بوده (فانک و واگنالز هنوز «روزکوری» می‌نویسد)، اما کاربرد پزشکی امروز «ناتوانی دیدن در نور کم، شب‌کوری» است. پیکان یونانی > انگلیسی درست است، چه این واژه ساختی دانشورانه است نه صورتی موروثی.\",\n  \"sources\": [W+\"nyctalopia\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. nekʷ-t-: '4. Greek nux (stem nukt-), night: NYCTALOPIA, NYCTITROPISM'; the index (line 1946) reads 'NYCTALOPIA nekʷ-t-, okʷ-', and the okʷ- entry (line 796) lists 'Greek ōps, eye ... METOPIC, MYOPIA, NYCTALOPIA'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. nyctalopia\", \"stance\": \"supports\", \"note\": \"'Borrowed from Ancient Greek νυκταλωπία (nuktalōpía), from νύξ (núx, \\\"night\\\"), ἀλαός (alaós, \\\"blind\\\"), and ὄψ (óps, \\\"eye\\\")'; 'the inability to see clearly in dim light; night blindness'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. night (leaf 560 ≈ p. 1047)\", \"stance\": \"supports\", \"note\": \"the entry's cross-references include 'nycti-', the same Greek stem.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol3.txt lines 75353, 77238\", \"stance\": \"partial\", \"note\": \"'nocturnal sight, day-blindness, nyctalopia' — same word, the older (opposite) medical sense.\"}\n  ]\n }\n]\n\ndoc = {\n \"pdf_page\": 369,\n \"book_page\": 339,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Nogw\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *nogʷ- (Wiktionary lemma *negʷ-) 'naked', with the derivatives *nogʷ-eto-/*nogʷ-oto- (Gmc), *nogʷ-edo- (Lat.), *nogʷ-no- (Indo-Iranian) and *nogʷ-mo-/metathesised *nogʷnós (Gk.)\",\n   \"note\": \"Root, language label and gloss are all correct. Pokorny 769 has exactly 'nogʷ-, nogʷod(h)o-, nogʷ-no- \\\"naked\\\"', with the standing note 'often distorted taboo' — the taboo deformation is what produces the irregular initials (Av. m-, Arm. m-, Oss. b-, Gk. g-, Hes. l-) that recur all over this chart. Walde-Pokorny II 339 f., Watkins s.v. nogʷ-, Klein s.v. naked and Buck 4.99 (p. 325) all give the same root. Two things in the chart do not survive scrutiny: the intermediate box 'Indo-European Gumnos, Gunos: beautiful, naked' (node #8) is Mann's private reconstruction, rejected by Pokorny, Watkins, Walde-Pokorny and Beekes, who all derive Greek γυμνός from *nogʷ- itself; and the two items hanging off it, Persian نغام (node #9) and Latin vinnus (node #10), are respectively a folk etymology and a mis-glossed hapax. The Iranian line (nodes #1-#3) is right in substance, but Avestan maγna- is a sister of MP brahnag, not its ancestor — as Nourai's own cross-reference 'See \\\"Bŭnai: naked\\\"' half concedes.\",\n   \"note_fa\": \"ریشه، برچسب زبانی و معنا هر سه درست است. پوکورنی در ص ۷۶۹ عیناً «nogʷ-, nogʷod(h)o-, nogʷ-no- «برهنه»» را می‌آورد با این یادداشت که این ریشه «غالباً دچار دگرگونی تابویی شده است» — و همین دگرگونی تابویی است که همخوان‌های آغازین نامنظم (م اوستایی و ارمنی، ب آسی، گ یونانی، ل در هزیخیوس) را در سراسر این نمودار پدید آورده است. والده-پوکورنی (ج ۲ ص ۳۳۹ به بعد)، واتکینز، کلاین و باک (بند ۴٫۹۹، ص ۳۲۵) همین ریشه را می‌دهند. اما دو نکته در نمودار پذیرفتنی نیست: جعبهٔ میانی «هندواروپایی Gumnos, Gunos: زیبا، برهنه» (گرهٔ ۸) بازسازی شخصی مان است که پوکورنی و واتکینز و والده-پوکورنی و بیکس همه رد کرده‌اند و γυμνός یونانی را یکسر از *nogʷ- می‌گیرند؛ و دو واژهٔ آویخته به آن، «نغام» فارسی (گرهٔ ۹) و vinnus لاتینی (گرهٔ ۱۰)، یکی ریشه‌شناسی عامیانه است و دیگری واژه‌ای یک‌بارگواه با معنای نادرست. شاخهٔ ایرانی (گره‌های ۱ تا ۳) در اصل درست است، اما maγna- اوستایی خواهرِ brahnag پهلوی است نه نیای آن — چنان‌که ارجاع خودِ نورایی به ریشهٔ «Bŭnai» تا نیمه به آن اعتراف می‌کند.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/neg%CA%B7-\", \"https://www.etymonline.com/word/naked\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:769\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: nogʷ-, nogʷod(h)o- nogʷ-no-. Meaning: naked. Note: often distorted taboo ... References: WP. II 339 f., WH. II 185, Trautmann 201, Specht Indo Germanic Dekl. 251. Page(s): 769.' Page number, root shape and gloss all match the chart.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II p. 339\", \"stance\": \"supports\", \"note\": \"'nogʷ- \\\"nackt\\\"' with the same material (anord. nøkkva, lit. nuogas, aksl. nagŭ, lat. nudus, got. nagaþs, ai. nagná-, av. maγna-, gr. γυμνός).\"},\n     {\"src\": \"AHD\", \"where\": \"s.v. nogʷ-\", \"stance\": \"supports\", \"note\": \"'nogʷ-. Naked.' with the Germanic, Latin and Greek derivatives and '[Pok. nogʷ- 769.]'.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck §4.99 NAKED, BARE (leaf 367 ≈ p. 325)\", \"stance\": \"supports\", \"note\": \"the comparative table lists 'Skt. nagna-', 'Av. maγna-', 'Lat. nudus', 'OE nacod; ber', 'Russ. nagoj; golyj'.\"},\n     {\"src\": \"IEC\", \"where\": \"s.v. nogudos, nogutos (leaf 473, p. 848)\", \"stance\": \"partial\", \"note\": \"Mann's own root entry: 'nogudos, nogutos (noguito-) \\\"naked\\\". Variant: nogumnos (nogunos, nongu-). WP II, 339' — same family, but he keeps γυμνός out of it as 'obscure'.\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. naked (leaf 549 ≈ pp. 1025-1026)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. *nogwo-dho-; cogn. with L. nudus [fr. *now(e)dos, for I.-E. *nogwedhos]'.\"}\n   ],\n   \"nodes\": e0_nodes\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Noktis, Nekw, Nekwt\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *nókʷt-s / *nekʷ-t- 'night' (o-grade *nokʷ-t-, i-stem *nokʷ-ti-)\",\n   \"note\": \"The root box is right in every respect. Pokorny 762-763 lemmatises it 'nekʷ-(t-), nokʷ-t-s \\\"night\\\"' with the stem inventory 'nokʷt-, nokʷti-, nokʷtu-, nokʷt(e)r-'; Watkins has 'nekʷ-t-. Night. O-grade form *nokʷ-t-' [Pok. nekʷ(t)- 762]; Mann IEC 850 'noktis, nokts \\\"night\\\"'; Buck 14.42 (pp. 992-993) 'IE *nokt(t)-'. Nourai's three shapes Noktis / Nekw / Nekwt map onto the i-stem, the bare root and the t-stem respectively, so all three are in the sources. AHD:1530 cannot be verified as a page (the copy on disk is Watkins' 1985 standalone reprint, which has no p. 1530; the 1975 New College appendix ran pp. 1505-1550, so a page in the 1520s-1530s for the n- roots is plausible), but the entry it points to says what the box says. Two problems on the page: node #1 'Old Persian naktin' is a misreading of Mann's 'OPr.' (Old Prussian) — Old Persian's word for night is xšap-; and the printed Latin box reads 'nox, nocht', a misprint in the book. The page also carries a completely BLANK double-ruled box fed by the Old Persian node — empty in the print, and correspondingly absent from the extraction; nothing is lost, but it should be noted as a defect of the book's layout.\",\n   \"note_fa\": \"جعبهٔ ریشه از هر نظر درست است. پوکورنی (ص ۷۶۲–۷۶۳) آن را «nekʷ-(t-), nokʷ-t-s «شب»» می‌آورد با فهرست ستاک‌های nokʷt-, nokʷti-, nokʷtu-, nokʷt(e)r-؛ واتکینز «nekʷ-t-. شب. پایهٔ o-دار *nokʷ-t-»؛ مان (ص ۸۵۰) «noktis, nokts «شب»»؛ و باک (بند ۱۴٫۴۲، ص ۹۹۲–۹۹۳) «هندواروپایی *nokt(t)-». سه صورتی که نورایی داده (Noktis / Nekw / Nekwt) به‌ترتیب ستاک i-دار و ریشهٔ ساده و ستاک t-دار است و هر سه در منابع هست. ارجاع AHD:1530 را نمی‌توان از روی شمارهٔ صفحه سنجید (نسخهٔ موجود، چاپ مستقل ۱۹۸۵ واتکینز است و صفحهٔ ۱۵۳۰ ندارد؛ پیوست چاپ ۱۹۷۵ صفحات ۱۵۰۵–۱۵۵۰ بوده و صفحه‌ای در حدود ۱۵۳۰ برای ریشه‌های n- پذیرفتنی است)، اما مدخل مورد نظر همان را می‌گوید که جعبه می‌گوید. دو ایراد در این صفحه هست: گرهٔ ۱ («پارسی باستان naktin») خطای خوانش «OPr.» (پروسی کهن) در کتاب مان است — واژهٔ پارسی باستان برای شب xšap- است؛ و جعبهٔ لاتینی «nox, nocht» چاپ شده که غلط چاپی کتاب است. همچنین در صفحهٔ چاپی، جعبه‌ای دوخط و کاملاً خالی از گرهٔ پارسی باستان آویخته است که در کتاب تهی است و در استخراج هم نیامده؛ چیزی از دست نرفته، اما شایستهٔ یادآوری است.\",\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/n%C3%B3k%CA%B7ts\", \"https://www.etymonline.com/word/night\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: nekʷ-(t-), nokʷ-t-s. Meaning: night. Grammatical information: stem nokʷt-, nokʷti-, nokʷtu-, nokʷt(e)ru ... References: WP. II 337 ff., WH. II 181 ff., Trautmann 9, 193 ... Page(s): 762-763.'\"},\n     {\"ref\": \"AHD:1530\", \"status\": \"partial\", \"note\": \"the page number cannot be checked in the 1985 standalone Watkins on disk (it has no p. 1530), but the entry meant is 'nekʷ-t-. Night. O-grade form *nokʷ-t-. 1. Germanic *naht- ... 2. Latin nox (stem noct-) ... 4. Greek nux (stem nukt-) ... [Pok. nekʷ(t)- 762.]' — precisely the content of the root box and of nodes #3-#8.\"},\n     {\"ref\": \"IEC:850\", \"status\": \"supports\", \"note\": \"Mann, leaf 474 (printed pp. 849-850): 'noktis, nokts \\\"night\\\" (ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti ...)' — the lemma 'Noktis' of the box.\"},\n     {\"ref\": \"SYN:992\", \"status\": \"supports\", \"note\": \"Buck §14.42 NIGHT (SYN.txt line 25300, leaf 1068 ≈ pp. 992-993): '1. IE *nokt(t)-. Walde-P. 2.337 ff. ... Most of the words for \\\"night\\\" belong to an inherited group, pointing clearly to an IE word for \\\"night\\\".'\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II pp. 337-338\", \"stance\": \"supports\", \"note\": \"the parent article of Pokorny's entry, with the Greek, Latin, Celtic, Germanic and Baltic material (including 'apr. naktin (Akk. sg.)').\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. night (leaf 560 ≈ p. 1047)\", \"stance\": \"supports\", \"note\": \"'fr. Teut. base *naht, corresponding to I.-E. *noqt-, whence OI. naktam ..., Gk. νύξ (gen. νυκτός), L. nox (gen. noctis), Alb. natë, OSlav. nošti, Lith. naktis'.\"},\n     {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §88 and DB I 20\", \"stance\": \"contradicts\", \"note\": \"relevant to node #1 only: Old Persian 'night' is xšap-, and the root *nokʷt- has no Old Persian reflex.\"},\n     {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/nókʷts\", \"stance\": \"supports\", \"note\": \"*nókʷts, feminine, 'night'; descendants in Indo-Iranian (Skt. nákt-, Younger Avestan), Latin nox, Greek núx, Proto-Germanic *nahts, Proto-Balto-Slavic *náktis — and no Old Persian.\"}\n   ],\n   \"nodes\": e1_nodes\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-369.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-369.py",
 "description": "Build page-369.json"
}
```


### [2026-09-07T20:40:32.359Z] TOOL RESULT

```
ok
```


## [2026-09-07T20:40:39.212Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-369.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 369",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T20:40:40.665Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 16, 'plausible': 1, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 18, 'not_checked': 6, 'partial': 3, 'contradicts': 1}
books consulted: {'supports': 50, 'partial': 12, 'silent': 12, 'contradicts': 10} | by book: {'KLN': 12, 'AHD': 10, 'WLD': 8, 'Etymonline': 8, 'Wiktionary': 7, 'POK': 7, 'LAT': 4, 'MON': 3, 'SYN': 3, 'BRT': 2, 'ISS_alt_DKS': 2, 'HRN': 2, 'LEW': 2, 'IEC': 2, 'Dehkhoda/abadis': 2, 'FSD': 2, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'BQT': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1, 'BOOK': 1}
```


## [2026-09-07T20:41:03.043Z] AGENT

Done. `data/verification/page-369.json` written, valid JSON, `verify_check.py 369` reports **0 PROBLEM lines** (22/22 nodes).

**Page 369 (book p. 339) — verdicts**
- Roots: 2 confirmed (Nogw = PIE \*nogʷ- "naked", POK 769; Noktis/Nekw/Nekwt = PIE \*nókʷts "night", POK 762–763)
- Nodes: 16 confirmed, 1 plausible, 4 disputed, 1 transcription_suspect
- Ref checks: 18 supports, 3 partial, 1 contradicts, 6 not_checked; 84 `consulted` entries across 24 books/sites

**Disputed / flagged**
- **Nokt., #1 Old Persian `naktin` — disputed.** There is no Old Persian reflex of \*nokʷt-; OP "night" is *xšap-* (Kent §88, DB I 20; Buck 14.42 "Av., OPers. xšap-"). Nourai's form comes from Mann IEC 850, where it is **Old Prussian**: "Skt. (Vedic) náktih, f.; **OPr.** naktin, acc. sg." (Mann's abbreviation for Persian is "Per."). Confirmed by WP II 338 "apr. naktin (Akk. sg.)" and POK 762 "Old Prussian naktin". A misread abbreviation, not a scan error.
- **Nogw, #8 IE "Gumnos, Gunos: beautiful, naked" — disputed.** Faithful to Mann IEC 364, but Mann's construct alone: POK 769, WP II 339, Watkins (\*nogʷ-mo-) and Wiktionary/Beekes (\*nogʷnós by metathesis/taboo) all derive Gk. γυμνός from \*nogʷ- itself; Mann's own IEC 848 calls γυμνός "obscure".
- **Nogw, #9 Persian نغام "not beautiful" — disputed.** Word is real (Borhan v4 bayān 14; Mo'in; Dehkhoda), but the na- + \*ğām analysis is Mann's queried guess; no Persian \*غام "beautiful" is attested, and the oldest citation (Daqiqi, Loghat-e Fors p. 337) means "dust-darkened". The tradition ties it to the doublet نفام and to فام "hue".
- **Nogw, #10 Latin `vinnus` "wanton" — disputed.** Ernout-Meillet: *vinnus* is an Isidore hapax = *cincinnus* "curled lock" (possibly invented to explain *vinnulus*); "wanton/charming" belongs to *vinnulus*, an "adjectif expressif, sans étymologie sûre" — no link to γυμνός.
- **Nokt., #5 Latin "nox, nocht" — transcription_suspect, `error_in: "book"`.** Page image (rendered at 400 dpi, saved to `data/verification/sources/refs/ocr/BOOK/369.png`) plainly prints "nox, nocht : night". Extraction is faithful; correct form is *nox*, gen. *noctis* (stem *noct-*). Likely contamination from the Celtic *nocht* a few lines away in POK 762.
- **Nogw, #2 Pahlavi brahnak — plausible.** Right root and right Zand equation (BRT col. 1112 "Pü.: brahnak"; Bailey DKS s.v. *būnaa-*), but MP *brahnag* continues PIr. \*bagna- with secondary -r- (Wiktionary), not Av. *maγna-*; they are sisters, not parent/child.

**For the owner (extraction, minor)**: the printed page has a **blank double-ruled box** hanging off the Old Persian `naktin` node — empty in the book itself, and omitted from the JSON. No content lost, but it is a layout defect worth recording.
