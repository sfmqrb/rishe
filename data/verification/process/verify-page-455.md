# Verification process log — verify-page-455


## [2026-09-14T01:56:24.304Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 455 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-455.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-455.json. Write /home/sfmqrb/git/rishe/data/verification/page-455.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 455` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:25.124Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:56:26.007Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:26.023Z] TOOL RESULT

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


## [2026-09-14T01:56:26.568Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-455.txt"
}
```


### [2026-09-14T01:56:26.590Z] TOOL RESULT

```
1	=== PDF page 455 (book page 425) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skěu 1, Pneu : to sneeze; to breathe  (refs POK:838,953)
4	#1 (parent #0) [Persian] refs=POK:953; BQT:1102,1304 | šonŭšeh «شنوشه» : sneeze | extra: شنوسه، اشنوسه
5	#2 (parent #0) [Germanic] refs=AHD:1535 | fniu : to sneeze
6	  #3 (parent #2) [English] refs=None | sneeze
7	#4 (parent #0) [Greek] refs=AHD | pneuma : wind, breath
8	  #5 (parent #4) [English] refs=AHD | pneumatic, pneumonia
9	--- entry 1 ---
10	ROOT [Indo-European] Skeu 2, Sku, Keu 3, Kŭ 3; Skŭr, Ku-z-dho, Kut-no : to cover; cover, shell  (refs POK:952,953; IEC:1193AHD:1540)
11	#1 (parent #0) [Avestan / Old Persian] refs=POK:952; KNT:180; BQT:785 | xaôda, xaudâ : helmet ; tigra-xaudâ : pointed (sharp) helmet ☞Steig
12	  #2 (parent #1) [Persian] refs=POK:952; KNT:180; BQT:785 | xŭd «خود۲» : helmet | extra: کلاهخود
13	#3 (parent #0) [Persian] refs=BQT:1562; MON:2821; SOD:187 | kâz «کاز» : hut, cover | extra: کازه، کاژ، کاژه | NOTE: BQT claims these words are cognates of the Sogdian word "k`zk`kh".
14	#4 (parent #0) [Greek] refs=IEC:595 | kutos : hollow, belly, body
15	#5 (parent #0) [Avestan] refs=POK:953 | kusra : vault, hole, cavity
16	  #6 (parent #5) [Persian] refs=POK:953 | kos «کس۲» : external female genitalia
17	#7 (parent #0) [Germanic] refs=POK:953; AHD | husôn, hŭdjon : cover ; hudiz, hudjan : skin, hide ; skŭma : foam or scum covering water
18	  #8 (parent #7) [English] refs=AHD | hose, hut ; hide : skin ; skim, scum
19	#9 (parent #0) [Latin] refs=POK:953; IEC:595 | cutis : skin ; ob-scŭrus : covered, unclear
20	  #10 (parent #9) [English] refs=AHD | curium, cutis ; obscure
21	#11 (parent #0) [Persian] refs=IEC:594,1193; MON:1899,3114 | skŭreh «سکوره» : earthen bowl ; kŭč «کوچ» : household, family, tribe | extra: سکره، اسکوره، سکربه
22	--- entry 2 ---
23	ROOT Skeu 3 -> redirect to Keu 3
24	
```


## [2026-09-14T01:56:28.132Z] AGENT

I'll read the source JSON and the reference infrastructure.


## [2026-09-14T01:56:29.533Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-455.json",
 "description": "Read source JSON for page 455"
}
```


### [2026-09-14T01:56:29.581Z] TOOL RESULT

```
{
  "pdf_page": 455,
  "book_page": 425,
  "entries": [
    {
      "root": {
        "name": "Skěu 1, Pneu",
        "lang": "Indo-European",
        "refs": "POK:838,953",
        "gloss": "to sneeze; to breathe"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:953; BQT:1102,1304",
          "words": [
            {
              "translit": "šonŭšeh",
              "gloss": "sneeze",
              "script": "شنوشه"
            }
          ],
          "script_extra": "شنوسه، اشنوسه",
          "note": null,
          "quote": {
            "text": "مرا امروز توبه سود دارد - چنان چون دردمندان را شنوشه",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1535",
          "words": [
            {
              "translit": "fniu",
              "gloss": "to sneeze",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "sneeze",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "pneuma",
              "gloss": "wind, breath",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "pneumatic, pneumonia",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skeu 2, Sku, Keu 3, Kŭ 3; Skŭr, Ku-z-dho, Kut-no",
        "lang": "Indo-European",
        "refs": "POK:952,953; IEC:1193AHD:1540",
        "gloss": "to cover; cover, shell"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:952; KNT:180; BQT:785",
          "words": [
            {
              "translit": "xaôda, xaudâ",
              "gloss": "helmet",
              "script": null
            },
            {
              "translit": "tigra-xaudâ",
              "gloss": "pointed (sharp) helmet",
              "script": null,
              "see": ["Steig"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:952; KNT:180; BQT:785",
          "words": [
            {
              "translit": "xŭd",
              "gloss": "helmet",
              "script": "خود۲"
            }
          ],
          "script_extra": "کلاهخود",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1562; MON:2821; SOD:187",
          "words": [
            {
              "translit": "kâz",
              "gloss": "hut, cover",
              "script": "کاز"
            }
          ],
          "script_extra": "کازه، کاژ، کاژه",
          "note": "BQT claims these words are cognates of the Sogdian word \"k`zk`kh\".",
          "quote": {
            "text": "امید وصل تو نیست در وهم من که آخر - در کازهٔ گدایان سلطان چگونه گنجد",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:595",
          "words": [
            {
              "translit": "kutos",
              "gloss": "hollow, belly, body",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:953",
          "words": [
            {
              "translit": "kusra",
              "gloss": "vault, hole, cavity",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "POK:953",
          "words": [
            {
              "translit": "kos",
              "gloss": "external female genitalia",
              "script": "کس۲"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:953; AHD",
          "words": [
            {
              "translit": "husôn, hŭdjon",
              "gloss": "cover",
              "script": null
            },
            {
              "translit": "hudiz, hudjan",
              "gloss": "skin, hide",
              "script": null
            },
            {
              "translit": "skŭma",
              "gloss": "foam or scum covering water",
              "script": null
            }
          ],
          "script_extra": null,
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
              "translit": "hose, hut",
              "gloss": null,
              "script": null
            },
            {
              "translit": "hide",
              "gloss": "skin",
              "script": null
            },
            {
              "translit": "skim, scum",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:953; IEC:595",
          "words": [
            {
              "translit": "cutis",
              "gloss": "skin",
              "script": null
            },
            {
              "translit": "ob-scŭrus",
              "gloss": "covered, unclear",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "curium, cutis",
              "gloss": null,
              "script": null
            },
            {
              "translit": "obscure",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:594,1193; MON:1899,3114",
          "words": [
            {
              "translit": "skŭreh",
              "gloss": "earthen bowl",
              "script": "سکوره"
            },
            {
              "translit": "kŭč",
              "gloss": "household, family, tribe",
              "script": "کوچ"
            }
          ],
          "script_extra": "سکره، اسکوره، سکربه",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Skeu 3",
        "redirect": "Keu 3"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:56:30.404Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:30.484Z] TOOL RESULT

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


## [2026-09-14T01:56:35.187Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','IEC','KNT','BQT','MON','SOD','WLD','BRT','SYN','KLN','PHD','HRN','HUB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700]); print()\n\""
}
```


### [2026-09-14T01:56:36.146Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


## [2026-09-14T01:56:39.793Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(grep -c $'\\f' $f) leaves, $(wc -c <$f) bytes\"; done"
}
```


## [2026-09-14T01:56:40.533Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pneu\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:56:41.825Z] TOOL RESULT

```
POK_01.txt: 352 leaves, 981836 bytes
POK_02.txt: 420 leaves, 1137861 bytes
POK_03.txt: 415 leaves, 1170809 bytes
POK_full.txt: 0 leaves, 3971883 bytes
```


### [2026-09-14T01:56:41.945Z] TOOL RESULT

```
68564:Root / lemma: pneu- 
77391:through hybridization with pneu- (above S. 838 f.): *ksneu-s- ( *kneus-, *sneus-) in npers.
```


## [2026-09-14T01:56:44.628Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '68555,68600p' POK_full.txt"
}
```


### [2026-09-14T01:56:44.688Z] TOOL RESULT

```
f. "rafter, sloped beam that forms the framework of a roof ', Norwegian expressive flautaf. 

"crossbar, crossbeam an einem sled '. 

References: WP. II 90. 

Page(s): 838 

Root / lemma: pneu- 

Meaning: to breathe 

Material: Gr. nvsu) (nvsuaai) "blow, pant, gasp, breathe, smell', ttveOmq "das Wehen, 

breath, breeze, breath etc.', nvorj "das Wehen, snort'; in addition perhaps also noinvuu) 



'sich rijhren, astir sein', trans, "sich eager wherewith beschaftigen', Perf. TTsnvuaGai " 
spiritually astir, sensible, wise sein', nvuT6(; spcppajv, auxppojv Hes., apnvuaGai "again 
zum Bewufttsein come', if "sich riJhren, astir, esp. spiritually astir' from "beim Laufe 
keuchen' and "breathe = agile, lively sein' has evolved; 

Old Icelandic fnysa'pant, sniff, snort'. Old English fneosan^ sneeze' {fnora^6as 
Niesen'), Middle High German pfnusen^pant, sniff, snort, sneeze' {pf- schallverstarkend 
for /), pfnustm. "unterdrijcktes laughter', Norwegian fnysa' giggle '; besides Germanic 
*fnes-, *fnds-, *fnas-:0\6 English fnesan ^ an\r\e\are' , fnsestxr\. "breath, breath, breeze', 
/^^5e//a/7"schnarchen, pant, sniff, snort'. Middle High German pfnasen ^ pant, sniff, snort', 
pfnastm. "das snort'. Old High German /^as/ed/7 "anhelare'; Old Icelandic fn0sa'pant, 
sniff, snort'; Old Icelandic fnasa'pant, sniff, snort'; Old High German fnaskazzen, 
fneskezzen. Middle High German phneschen pant, sniff, snort, pant, gasp'; 

Germanic fneh-:0\6 High German fnehan. Middle High German pfnehen breathe, pant, 
sniff, snort, pant, gasp'. Old High German /^a/7/e/7/e "schnaubend' (Middle High German 
pfnuhtxw. "snort' braucht nicht die zero grade from Indo Germanic /7/7e:/-widerzuspiegeln). 

References: WP. II 85, Wissmann Nom. Postverb. 18 f., Schwyzer Gr. Gr. 1, 696. 
Page(s): 838-839 

Root / lemma: ppksti- 

Meaning: fist 

Material: Old High German fust. Old English fyst= Old Bulgarian p^stb {*pinstb) "fist'.
```


## [2026-09-14T01:56:45.175Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '77360,77420p' POK_full.txt"
}
```


### [2026-09-14T01:56:45.241Z] TOOL RESULT

```
westfal. schgC spawn, spat, spawn of oyster'. New Franconian schaiden{ai= wgrm. a) 
"laichen', perhaps westfal. schaden ' Ertrag give, of wheat'; 

Old English sceaddm. 'Maifisch', Modern High German Schac^e) ds., Norwegian dial. 
skadd ^smaW Schnapel', wherefore (loanword) cymr. ys^ao''a/7"Haring', Middle Irish scatan, 
nir. scadan ds.] 

Old Lithuanian skastu, skatau, s/ra5//"spring, jump ', su-skantu, -skaciau, -skasti 
"aufhijpfen'; 

an Indo Germanic additional form auf -{/perhaps in: Norwegian s/ra/'Wipfel eines 
Baumes', skata^'xu eine cusp, peak auslaufen'. Old Icelandic skatai. " magpie, 
Glattrochen'. 

References: WP. II 538 f., WH. II 491. 
Page(s): 950 

Root / lemma: skeu-3, kseu- 

Meaning: to sneeze 

Material: Old Indie /rsa^//" niest', ksuta-^6as Niesen'; common Old Indie -gh- > -ks-0\6 

Lithuanian skiaudziu, sk/audef/^ sneeze' (similarly ciaudziu, -deti), Latvian skauju, skavu, 

skaut, Iterat. skaudet' sneeze' (viel strong irregular Slavic kbchngt/, kychat/an6 Cbchati, 

compare Old Indie c/7/Ma "Niesen'); 

Maybe alb. {*skauda) hunda^ nose '. 

through hybridization with pneu- (above S. 838 f.): *ksneu-s- ( *kneus-, *sneus-) in npers. 
isnosa, asnosa^ H\esen'\ Old Icelandic hnjdsa. Middle English nesen. Old High German 
/7/c»sa/7 (participle ginoran); Old Icelandic hn^rim.. Old English /7/7c»/'5 "Niesen', Old Saxon 



hn/oxwrt'H'\eQ>\Nurz'; besides Middle English snesen, engl. sneeze; compare Low German 
snusen, Danish 5/7^5e"schnoben, scent' ; similarly also Lithuanian 5/7/aJ/r//"schnupfen'. 

References: WP. II 85, 551, Trautmann 266. 
Page(s): 953 

Root / lemma: skeu-5 

See also: besides sReu-{see below) 'throw, schieften, hetzen'; s. die extensions skeub-, 

skeUti^-, skeud-, skeug-, skeuk-. 

Page(s): 954 

Root / lemma: skeu-6(t-) 

Meaning: to cut, separate, scratch 

Note: extension from 5e/r-"cut, clip' 

Material: Old Indie skau-ti, skunati, skunot/ ^stori, stobert, stochert', with a- 'zerkleinert 

through Stochern; makes Einschnitte (in die ears from animals)', ava-skava-m. 'ein worm',
```


## [2026-09-14T01:56:53.505Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: skeu\\|^Root / lemma: keu\\|^Root / lemma: ku\\|^Root / lemma: kseu\" POK_full.txt"
}
```


### [2026-09-14T01:56:53.575Z] TOOL RESULT

```
46624:Root / lemma: keuad- kud- 
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46749:Root / lemma: keu-2, keua- 
48878:Root / lemma: kseud- {*gheud-) 
48907:Root / lemma: kuku 
48935:Root / lemma: ku-, kus- {*k"'uk"'h-) 
48970:Root / lemma: kuak- 
48989:Root / lemma: kuat(h)- 
49019:Root / lemma: kueiek- or kelak-, kolak- 
49051:Root / lemma: kuelp-2 
49079:Root / lemma: kuerp-, also kuerb- : to turn, wind, derived from a suffixed Root / lemma: 
49111:Root / lemma: kuet- : kuat- : kut- 
49140:Root / lemma: kuoi-, kuT- 
49157:Root / lemma: kures- kuers- kujrs- 
76617:Root / lemma: skeud-1 
77377:Root / lemma: skeu-3, kseu- 
77403:Root / lemma: skeu-5 
77411:Root / lemma: skeu-6(t-)
```


## [2026-09-14T01:56:57.655Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 95[123]\" POK_full.txt"
}
```


### [2026-09-14T01:56:57.710Z] TOOL RESULT

```
76857:Page(s): 951-953 
77401:Page(s): 953
```


## [2026-09-14T01:56:59.453Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '76770,76860p' POK_full.txt"
}
```


### [2026-09-14T01:56:59.513Z] TOOL RESULT

```
Old Icelandic hud. Old English hyd. Old High German hut{*hOdi-) 'Haut' (Swiss hut 
'husk, Fruchtschale'); 

Old High German hodo. Old Frisian /7c»//7a 'testicle'; Old English hodmam. ' darkness ', 
Old High German hufta 'cottage' ( *kuf/a or *ku6^ja: out of it Old Saxon hufta, huttia); 

Old Lithuanian /ri//j7s'bag, Geldkatze'; Baltic *keuta^sV\v\\ Old Prussian keuto, 
Lithuanian k/autas^bo\N\, husk', dial, kevetasm. ds.; k/ava/asm. 'Eierschale' {*keuo/o-), 
Latvian cau/ai. 'bowl', caumalat 'hard bowl' (Trautmann 132); 

nasalized * kunt/'o ^ preserve' perhaps in Old Church Slavic sbkgtat/" calm, appease, 
stillen', russ. kutatb ' veil, cover ' etc.. Old Prussian -/rJ/7//"pflegt', Inf. pokunst, pakunst 
'preserve, protect' and with intonation change Slavic *kgtai. in Old Church Slavic kgsta^ 
tjKrivri ', kir. kuca^ pigpen' (Trautmann 145). 

Maybe alb. {*po-skura) pasqyra^ mirror ' (common Slavic po- alb. pa- prefix). 



(s)keuA 



h_- 



Old Indie kuhara-v\. "cave', kuhaka-xw. "Schelm, Gaukler, cheater', kuhayate^be\xu<^\! , 
kuhu-t "Neumond' ("the hidden, concealed moon'); pamirdial. skTd' high MiJtze from 
fleece '; 

gr. K£u0u) "hide', keuGo^ n., keuGjjwv "verborgene depth', k£u0|j6c; "verborgener place, 
cavity, Saulache'; 

Middle Irish coda/^sk\n'; 

Old English /7j/o'a/7 "conceal'; here or to *5/rei//- Gothic skauda-(raip) /\Vk. Sg. " shoe 
(riemen)'. Old Icelandic skaudi. "vagina', PI. "Vorhaut; Elender, monster', skjodai. "bag, 
sack, bag'. Middle Low German schodeu. "vagina' (beim horse), f. " pod, pea'. Middle High 
German schote^ pod, Samengehause'; 

unclear is Latin cudo, -d/7/s "helmet from fell, fur' (loanword?); in the meaning near 
stands Avestan xad5a-rr\., ap. xauda- "hat, Kappe; helmet'. 

B. guttural extension (s)keu-R-: 

Old Indie /rosa-m. " container, Schatzkammer etc' (late also kosa-, das perhaps Indie 
development from k6sa-\s)\ doubtful kosaka-m. n. "egg, testicle, Gehause', kusapa-m. 
(uncovered) "Trinkgeschirr', kusaya-m. (uncovered) " cistern '; kuks/- m. "belly, womb, 
cavity'; common Old Indie -gh- > -/rs-npers. /r^5 "vulva'; Avestan kusra-^s\dc\ wolbend, 
hollow', vJkusra-, hankusra- "sich auseinander-, zusammenwolbend'; 

Lithuanian /rJsys (Plur. kusys), Latvian kusis, /rt/sa "vulvahaare' {*kuki-ox *kuksi-)\ 
Lithuanian /r/ai/se "skull, cranium', k/aus/s ^egg, testicle', Prussian-Latvian kaus/s 'egg'; 
Lithuanian /ra^55S "large dipper', Latvian kauss' platter, Kochloffel'. 

C. 5-extension (s)keu-s-: 

Perhaps Old Indie kostha-rc\. n. " container, lower abdomen, storeroom' , kustha-m. 
"Lendenhohle' (?), kusthika' content of the intestines ', npers. kust' groin ' (Armenian 
loanword /r^s/" belly, groin, body'); 

gr. kugtk;, -sux;, -iboq, " bladder, bag ', Kua9o(; "vulva'; 

doubtful Latin ci/s/ds "Wachter', compare WH. I 319; 



cymr. cwfhr'Aiter, Mastdarm' {*kuz(i^ro-); 

Old Icelandic haussm. 'cranium'; ablaut. Norwegian dial, husem. "Fischkopf, Old High 
German /7j5C»'Hausen', after dem with Schildplatten gepanzerten head; 

Modern High German dial. /7c»se/7"husk, pod ', Old English hosam. "Strumpf, husk', Old 
Icelandic Old High German /7c»S5"trouser'; 

presumably here Gothic Old Icelandic Old English Old Saxon Old High German hus 
'house', compare Low German /7Js/re'Kerngehause, sheath, TiJte' ; 

Gothic huzd, Old Icelandic hoddl (?), Old English Old Saxon hard, Old High German 
/70/f "treasure, tribute, Hort'{*kuz-6^o-= gr. KuoGoq); Swedish /7j/o'c/5 'cottage', dial, hodda, 
hudda 'Schu^^eu, Gefangnisraum', aschw. /7/0'c/a 'conceal'. 

References: WP. II 546 ff., WH. I 298 f., 301, 309, 319, 320, II 196, 503, Trautmann 132, 

145. 

Page(s): 951-953 

Root / lemma: (s)keu-4
```


## [2026-09-14T01:57:05.649Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '76700,76775p' POK_full.txt"
}
```


### [2026-09-14T01:57:05.743Z] TOOL RESULT

```
Armenian c/n/'roof, cover' {*skeuo-); with an!. A/?-/ Armenian xuc^Siube' {*khu-sRho-, at 
most zur 5-extension), fraglicher A-ai/aA'dark' {*khouo-, forms Armenian -ar), xu-p "cover', 
xul, A///r "cottage', xlay{*khulati-) " female Kopfverliuiiung, Scliieier; dress'; 

gr. OKuvia PI. " brows ', sniOKuviov "skin oberhalb the Augenbrauen' (compare Old Indie 
skunati); okuKoc, n. " kip, animal skin, bowl', gkuAov "abgezogene kip, animal skin ', gkuAov 
ds. " arms stripped off a slain enemy, spoils '; doubtful Kwaq, PI. Kwea " fleece '; 

Latin obscurus^*be6ecVX = "dark'; cu/us't\r\e Hintere'; 

Maybe Italian scuro : Reggiano : scur : Bergamasco sciJr : Venetian scuro : Zeneize scuo : 
Catalan obscur : Spanish oscuro : Galician escuro : Portuguese escuro : alb. {escui) err- 
te, erret: /erret^dark' < Latin obscurus'6ark'. 

Old Irish cu/m. "back, rump', cymr. c//"back'; Old Irish cul{*ku-la-) f. " angle, hideout ' = 
cymr. etc. cil, ysgiT hideout '; Irish cuaran, cymr. curan^ shoe '; perhaps Celtic-Latin 
cucullus " cowl ' (compare above Old Indie ku-kula-l); 

Old Icelandic skjai. "barn' {*skeua), probably also Old Icelandic hai. "skin' in hross-ha 
{*skoua), s/ra//" cottage, room' (Germanic * skawalan-); skyu. {*skeuio-) "cloud, 
Verdunklung', Old English scTo, Old Saxon sc/b "cloud'; Old English scu(w)arc\. "shadow, 
darkness, protection'. Old High German scuwo, scum, "shadow', scO-c(h)arv\. "mirror', 
actually "Schattengefaft', Old Icelandic skuggiru. "shadow, reflection, ghost', skugg-sjai. 
"mirror', Gothic skuggwam. "mirror'; Old High German skugin(a). Middle High German 
schiune. Modern High German Sc/7e^/7e ("hideout'), Norwegian dial, skyggnem. "cottage, 
hiding place, nook, bolt-hole'; Old Icelandic skaunt (or skaunnxu.) "shield'; Norwegian 
5/rJ/r7e "dark'. Old Icelandic skumivn. "dawn, twilight'. Middle Low German schummer 
"dawn, twilight' (: Latvian skumt); Old Icelandic hOmu. " twilight ', PN. /yK/77/>'"Verdunkler'; 
perhaps Old High German scum "scum, froth, foam' (if "deckendes'); 

maybe alb. {*scum) shkume'ioam' 

Old Icelandic sk/'o/n. " hideout, Zuflucht, protection, barn', sA/io/a "Butte, bowl, basin ', 
("Verwahrungsraum'), changing through ablaut Old Icelandic sky//, Middle Low German 
sc/iu/en. " hideout ', Old Frisian s/r^/e "cottage'; Old Icelandic 5/rj?/a"beschutzen', Middle 
High German sc/iu/en' bent sein, lurk, lugen'; 

Old High German scurm. "Wetterdach, protection' (: Latin obscurus). Middle High 
German sc/7j/'"hideout, shelter'. Old Icelandic skOri. "skin the Mandel', Old High German 
skura, sciura, ( *skurja) " barn'; with formants -/ro-and lengthened grade ^u\ probably 



Gothic skohs, Old Icelandic skor, PI. skuar, Old High German scuoh' shoe ' (actually 
"deckendes Oberlederof Schuhes', compare above Irish cOaran^ shoe ' and Middle Dutch 
sc/7oe 'sword scabbard, sheath '); 

Lithuanian /rei/a/as'Eierschale', Latvian cau/a'bo\N\, husk'; Latvian /r^a "vulva'; Latvian 
skaut^ hug, embrace, hold tight ', skumstu, skumf become sad ' (' obscurari '); but 
Lithuanian skura 'leather, bark, outer covering of a tree ', Latvian skura 'husk' from 
weiftruss. skyra. 

A. Dental extensions (respectively formations with dental formants): 

(s)keu-t-: 

Gr. GKUTOi; n. 'skin, leather', syKUTi, £yKUTi(; ' besides the skin', kuto(; n. 'sleeve, 
wrapping, skin' and 'vessel, Urne, cavity', kutI^ 'small Kasten, BiJchse', Kuaoq n nuyn; n 
yuvaiKsTov ai5oTov Hes.; (*kut-io(; or *ku9-i6(;), KUT(T)apo(; 'cavity, bulge, Bienenzelle, 
Eichelnapf, Kuaaapoc; ' anus ' (*KUTFapoc;); about Latin cuturnium ' vas, quo in sacrificiis 
vinum fundebatur ' s. WH. I 320; 

Latin c^//s'skin'; c£//7/7£/s 'pudendum muliebre' {*kut-nos)\ (under the influence of 
common Celtic -ns-, -nt- > -nn-). 

cymr. CM/o''Hodensack'; mcymr. esk/'t, esgit, ncymr. esgid, corn, eskit, esg/s' shoe ' 
{*ped-skuti-)\ (common Celtic Alb. abbreviation) 

Old Icelandic hud. Old English hyd. Old High German hut{*hOdi-) 'Haut' (Swiss hut 
'husk, Fruchtschale'); 

Old High German hodo. Old Frisian /7c»//7a 'testicle'; Old English hodmam. ' darkness ', 
Old High German hufta 'cottage' ( *kuf/a or *ku6^ja: out of it Old Saxon hufta, huttia);
```


## [2026-09-14T01:57:34.650Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD skeu ===\"; grep -n \"skeu\\|^pneu\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T01:57:34.731Z] TOOL RESULT

```
=== AHD skeu ===
941:skeup-
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
1646:HOP2 skeup-
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2252:SEXTUPLE pel-3 SHABBY skep- SHADE skot- SHADOW skot- SHAFT! skep- SHAH tké- SHAKO dek-2 SHAKTI kak-1 SHALE skel-1 SHALL skel-2 SHAMBLES skabh- SHANK skeng- SHAPE skep- SHARD  sker-1 SHARE! | sker-1 SHARE? sker-1 SHARP sker-1 SHATTER sked- SHAVE skep- SHAWM kolem- SHE so- SHEAF skeup- SHEAR sker-1 SHEARS sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
```


## [2026-09-14T01:57:36.185Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT xauda ===\"; grep -n \"xauda\\|xaudā\\|tigraxaud\\|tigra-xaud\" KNT.txt | head -20\necho \"=== BRT xaoda ===\"; grep -n \"xaoδa\\|xaoda\" BRT.txt | head -20"
}
```


### [2026-09-14T01:57:36.258Z] TOOL RESULT

```
=== KNT xauda ===
1260:$100. PAR. kh seems to appear in a few words, which have no far-reaching etymological con- nections: yaudd- ‘cap’, also in dgraxauda- ‘wearing the
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4185:XV iyam : Saka : tigraxaudé
4582:27 : tigraxauda : Skudra : Akaufaciya :
4726:: Зака : haumavargà : : бакё : tigraxauda : : Babirus :
=== BRT xaoda ===
```


## [2026-09-14T01:57:48.261Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^pneu-\\|pneu-\\. \\|fneusan\\|SNEEZE\\|pneumon\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:57:48.318Z] TOOL RESULT

```
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
864:1. Germanic *fleutan in Old English fléotan, to float, swim: FLEET!, FLEET2, 2. Zero-grade form *plud- in Germanic *flut-, *flot- in: a. Germanic derivative *floton, to float, in (i) Old English flotian, to float: FLoaT (ii) Old French floter, to float: FLOTSAM; b. Old Norse floti, raft, fleet: FLOTILLA; c. Old English floterian, flotorian, to float back and forth (-erian, iterative and frequentative suffix): FLUTTER; d. Germanic *flutjan, to float, in Old Norse flytja, to further, convey: FLIT. 3. Probably Ger- manic suffixed form *flaut-sta-, contracted into *flausta- in Icelandic flaustr, hurry, and flaustra, to bustle, akin to the probable Scandinavian source of FLUSTER. [Pok. pleu- 835, pl(e)u-mon- 837.] pleus-. To pluck; a feather, fleece. 1. Germanic *fleusaz, fleece, in Old English fléos, fleece: FLEECE. 2. Suffixed zero-grade form *plus-ma in Latin pliima, a feather: PLUMATE, PLUME, PLUMOSE, PLUMULE; DEPLUME. [Pok. pleus- 838.] plou-. Flea. 1. Extended form *plouk- in Germanic *flau- haz in Old English fléa(h), flea: FLEA. 2. Extended zero-grade form *plus- metathesized into *pusl- in: a. Latin pilex (< *puslex), flea: PUCE; PULICIDE; b. Greek psulla, flea: PSYLLA. [Pok. blou- 102.] [plumbum. Lead. Latin noun, probably borrowed from the same unidentified source as Greek molubdos, lead. 1. Latin plumbum: PLUMB, PLUMBAGO, PLUMBER, PLUMBISM, PLUMMET, PLUNGE; APLOMB, PLUMBIFEROUS. 2. Greek molubdos: MOLYBDENUM.] pneu-. To breathe. Imitative root. 1. Germanic *fneu- in Old English fnéosan, to sneeze: SNEEZE. 2. Greek pnein, to breathe (> pnoia, breathing): APNEA, DIPNOAN, DYSP- NEA, EUPNEA, HYPERPNEA, HYPOPNEA, POLYPNEA, TACHYPNEA. 3. Suffixed form *pneu-mn in Greek pneuma, breath, wind, spirit: PNEUMA, PNEUMATIC, PNEUMATO-, PNEUMO-. [Pok. pneu- 838.]
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
```


## [2026-09-14T01:57:59.002Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xauda\\|yaudd-\\|xaudā\" KNT.txt | head; echo \"---- search lexicon x section\"; grep -n \"tigra-\" KNT.txt | head -20"
}
```


### [2026-09-14T01:57:59.074Z] TOOL RESULT

```
1260:$100. PAR. kh seems to appear in a few words, which have no far-reaching etymological con- nections: yaudd- ‘cap’, also in dgraxauda- ‘wearing the
4582:27 : tigraxauda : Skudra : Akaufaciya :
4726:: Зака : haumavargà : : бакё : tigraxauda : : Babirus :
---- search lexicon x section
1320:tigra- ‘pointed’, also in tigrarauda-; Tigra-, a fortress in Armenia; Tigrd- ‘Tigris’, borrowed from Semitic,
1918:all lands’; hama-pitar- ‘having the same father’; ha-matar- ‘having the same mother’; tigra- zauda- "wearing pointed caps’; wéd-marsiyu-
5299:zaudü- sb. ‘hat, cap’ ($100, $143.IV): Av. таоба-, Oss. хойй, NPers. тоб, Arm. (borrowed) zoir ‘headband’ (cf. Duchesne-Guillemin, BSOS 9.865, for further connections). See also tigra- zauda-. [zaudāäļm asf. DB 5.22.
5441:igrazauda- adj. ‘wearing the pointed cap’ + i ($161.ITa), asisshown in the sculpture of Skunkha 4 the Scythian at Behistan (cf. also НФ. 7.64): ’hgra- ‘pointed’ + хашіа- ‘cap’ ($159). tigra- тамай npm. DNa 26, DSe 25°, XPh 27; for пега, ($56.11) DN xv, A?P 15.
```


## [2026-09-14T01:58:00.065Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xaoδa\\|xaoda\\|χaoδa\\|xaobn\\|Helm\" BRT.txt | head -30"
}
```


### [2026-09-14T01:58:00.143Z] TOOL RESULT

```
4933:•  j.  ayö.xao8a-  Adj.  (fem.  °'&ä-)  mit  me- tallenem (eisernem)  Helm':  fravasayB  . . °3rf  ayS^aya  ayl.virj^rä  Yt,  73.45.
7687:•>a/»a-  m.  Name  einer  Waffe,  wohl  einer Schui2walTe;  Windischmann  (u.  A.):  'Helm', DST.i  'eenouilldres'.
9674:Et.?  —  Pü.!  grcv  pän,  erL:  an  i  ha?  latak l'Helm')  apäc  e  iteh  basi.  S.  daiu  JtJ.  ClMs. Stud.  in  Hon,  ofDrisler  iiS.  —  <)  Oder  auch auf  'd:  -  »)  K  1,  L  4;  NA.  küir'.  —  3)  Them., ans  dem  NS.;  wertlos.
10529:•  j.  xao^a-  (,  p.  xauda-)  m.  'Hut,  Kappe Helm'.
10736:tritt  Ai.  nur  wenig  hervor.  Die  Metalle  stehen unter  seinem  Schutz.  Bei  den  letzten  Dingen kämpft  er  nach  Bd.  jo.  29  mit  dem  Dämon Sautva.  Auf  Münien  erscheint  Sala-niar  (PAO- PHOPO,  PAOPHOAP;  s.  Stein  Or&BabRec. iSS^.  I59ff.)  als  Kriegsgott  mit  Helm,  Schild und  Speer.  Vgl.  im  Übrigen  Tikle  Godsdiensl' 2.  136,  JusTi  PrJ.  SS.  75.  JN.  GlrPh.  2.  637, femer  die  bei  DsT.  ZA,  2.  313  übersetite  Stelle des  GrBd.
25749:•  j.  urvLJtaoÄa-  Adj.  'des  Helm  (oben) in  einer  Spitze  ausläuft'":  pt^rs  ..  'tB urvi.v3r>%rB  stvT.fnanadhril^  Mt.  g.  ^o.
25750:')  Vgl.   die  Abbildung   des  Helms    und   des Schild»  au«  Kirmättiäk  in  ZDMG.  36.  655. j,  uroilyeiH  P.  £6:  lies  urvity*.
26213:•  j.  sara-vara-  m.  'Helm':  yag/qtn  %aya- nam  ra%di!H  .  .  das^mä  'rS  V.  14.  9; *Vd.  12.
27876:•  j.  zaranyö.xao<)a-  Adj.  'mit  goldenem Helm  (bedeckt)':  voim  '\>m  .  .  zaranyS.-
```


## [2026-09-14T01:58:08.027Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,lines in [('KNT.txt',[5299,5441,1320]),('BRT.txt',[10529,4933])]:\n    data=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    for ln in lines:\n        leaf=sum(1 for i in range(ln) if '\\f' in data[i])\n        print(f,ln,'leaf(0-based ff count)=',leaf)\nEOF"
}
```


### [2026-09-14T01:58:09.216Z] TOOL RESULT

```
KNT.txt 5299 leaf(0-based ff count)= 199
KNT.txt 5441 leaf(0-based ff count)= 205
KNT.txt 1320 leaf(0-based ff count)= 49
BRT.txt 10529 leaf(0-based ff count)= 313
BRT.txt 4933 leaf(0-based ff count)= 121
```


## [2026-09-14T01:58:13.877Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==200' KNT.txt | head -20; echo \"=====205/206\"; awk 'BEGIN{RS=\"\\f\"} NR==206' KNT.txt | head -8"
}
```


### [2026-09-14T01:58:15.119Z] TOOL RESULT

```
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
uba- adj. ‘both’: GAv. uba-, Skt. dual ubhá(u), pIE *ubhó(u), cf. Gk. &p-dw, Lt. ат-00 ($143.11). ubà ndm. ($189) DSf 14; XPf 21.
ubarta- adj. ‘well-borne, lifted, esteemed’: u- well’ + barta- ‘borne’, pte. to bar- ‘bear’, pIE *su-bhrio- (830, $122, §242.1). ubartam asm. DB 1.21f;4.66.  ubartàm asf. DB 4.88. On meaning, cf. Altheim, ZII 3.33-5: hardly as taken by König, RulD 69.
[U]mamaita, see Atamaita-.
umartiya- adj. 'eontainig good men’: u- ‘good’ + martiya- ‘man’. umartiyd nsf. AmH 6; DPd 8f. wmartiyam asn. Р 11f; DSm 4°; DSp 3°; DZc 4.
Uyamad- sb. ‘Uyama’, a fortress in Armenia: Elam. t-i-ja-ma, Aram. huyaw (Cowley, AP 251 line 4, 257). Uyamà nsf. DB 244 (all charac- ters visible to Cameron),
urala- adj. ‘having good chariots’; Skt. sura- tha- as man’s name: u- ‘good’ + raba- ‘wagon’, Av. raba-, Skt. rdtha-, Lt. rota ‘wheel’ ($143.11). See also urafara-. ‘urabd-cd apn. as sb. ‘good chari- ots’ DSs 5.
urafara- adj. ‘having good charioteers’: deriv. of urada- ($148.1). [u|raüaram asn. DSp 3 (Bv. BSLP 33.2.0451 and Hz. AMI 4.126 restore |f\raBaram).
uradana- adj. ‘of good regulation’: u- ‘good’
+ deriv. of rad- ‘direct’ (§122, $147.I): see Hz. Ар1 206-7 (but he is wrong in drawing in also Lt. lé law). uradandm así. ОХЬ 23.
-
ре
LEXICON
tuva- refi. pron. ‘self? and poss. adj. ‘own’ (8118.1V): Av. z"a-, Skt. sva-, Gk. € and ds, Lt. sé and suos, pIE *sye and *suos (5148.11); in wada-, wvăipašiya-, wdmar kyu-.
watpasiya- adj. ‘belonging to self’ (wrongly ‘wayward’, Sen 246), nt. as sb. ‘own possession’: Ау. x’aépaibya- ‘own’; OP uvai-, nom. of wa-, as in Skt. svay-dm ‘self? (MB Gr. §293), + pAr. *natia-, formed on pIE *poti-, Av. рой ‘master, husband’, Skt. pati-, Gk. тоса ‘husband’, Lt. potis ‘able’, Lith. pats ‘self’: pIE *suoi-potio- (858, §143.- II, $152.11, $161.1Ib). watpasiyahya gsn. DNb 15.
 wüipasiya-, same as preceding, with vriddhi in initial syllable (§126; MB Gr. §298); but wai- may be an error for uvai-, or wai- for wäi- (§53). uvdipasiyam asn. DB 1.47.
‘UvaaStra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-tš-tar-ra, АКК. ú-ma-ku-iš- lar, Gk. Kva£ápys. From u- ‘good’ + varštra- ‘growth’ ($9.11, $79, $148.11), to vaxi-, Av. vazš-, Skt. vaks-, Gm. wachsen, N Eng. wax ($102): 'Hav- ing good growth’ ($164.11, IV). So ВЫ. AiW 1836; but Hz. АрІ 209 interprets ‘having good oversight’, to Av. aiwy-axrstrat (dat.) ‘oversight’ (otherwise Hüsing, OLZ 2.139-40). Стах аһу gsm. DB 2.15f, 81.  Uvaxstrahya (S86.IVb) DB 4.19, 22; DBe 7; ОВр 9f.
Uvaja- Uvajiya-, read Uvja- Uvjiya-: see Uja- Ujiya-.
wadd- sb. ‘abode’, vriddhi-form to Skt. svadha- ‘innate character’, from wa- ‘own’ + dhà- ‘make’ ($142; OP wa- + ?dà-) ; in PaiSiyduvdda-, q.v.
=====205/206
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
```


## [2026-09-14T01:58:27.985Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 197 198 199 200; do echo \"--- leaf $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -oE \"^[0-9]{2,3}$|[0-9]{3}[[:space:]]*$\" | head -3; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | tail -c 300; done"
}
```


### [2026-09-14T01:58:29.121Z] TOOL RESULT

```
--- leaf 197 ---
174
n; for imäm, §52.V]); DPd 15, 18; DPe 24; DNa 1f, 32, 53; DSe 1f; DSf 1; DSt 1; DZe 1, 8, 12; DE 2; XPa 1; XPb 2; ХРе 1; XPd 1f; ХРЇ 1f; XPh 1, 58; XE 3; XV 2, 24; A!Pa 2°; Ае 4f (as asn., $56. V), 5; А284 3 (as nsn., §56.V); А?Не 2; АзРа 2, 25f. ama npf. DB 1.13, 18, 23; 2.6�
--- leaf 198 ---
175
�. Uvjiyaibis ipm. DB 5.10,
ula (for шй, $36.I) conj. ‘and’ (52911-00): Av. ula, Skt. ш, Gk. Hom. -úre ‘like’, pIE *ute (hardly both -@ and - in Aryan, despite Mt. MSLP 19.57-8, MB Gr. 5151). Correlative with preceding -сӣ, DB 1.66f (cf. Gk. тё xai); ша... шб ‘both ... and’ 
--- leaf 199 ---
176
IAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken
--- leaf 200 ---
177
am. ren-
177
derings. So KT 9; Tm. Lex. 78; Wb. KIA 17 with note; Hz. BSOS 8.589-97 and Ар! 216-9; W. Hinz, Altpers. Wortschatz 141. Not to be taken with W. Schulze, РАЖ 1912.685-703, 1918.331- 2, as ‘by a natural death’, citing semantic par- allels in other languages; who is followed by M
```


## [2026-09-14T01:58:35.189Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /zaudü- sb/ {print \"record\",NR; print substr($0,1,120)}' KNT.txt\nawk 'BEGIN{RS=\"\\f\"} /igrazauda- adj/ {print \"record\",NR; print substr($0,1,150)}' KNT.txt"
}
```


### [2026-09-14T01:58:36.544Z] TOOL RESULT

```
record 204
ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, s
record 210
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. �
```


## [2026-09-14T01:58:39.835Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 204 210; do echo \"--- rec $n ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -oE \"(^|[^0-9])1[678][0-9]([^0-9]|$)\" | head -4; done"
}
```


### [2026-09-14T01:58:41.006Z] TOOL RESULT

```
--- rec 204 ---
§164.
 173,
$163.
 181.
--- rec 210 ---
$166)
$161.
.170;
$187)
```


## [2026-09-14T01:58:47.074Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==203' KNT.txt | head -6; echo \"....\"; awk 'BEGIN{RS=\"\\f\"} NR==203' KNT.txt | grep -oE \" 1[678][0-9][.,]\" | head -3"
}
```


### [2026-09-14T01:58:48.288Z] TOOL RESULT

```
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24.
akariya imf. pass. (585.1, §99, $220) DSf 37; XPh 42.
akarzya^tà За pl. imf. pass. (§35.1, $66.IT, $220, 8236.11) DB. 3.92. !
[c]àzr[;yatà]| or cazr{iyatd] perf. pass. ($219, $220) DB 4.90 (Kent, JAOS 62.267-8, for KT's „ада... after König, Klotho 446).
....
```


## [2026-09-14T01:58:53.089Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD ==\"; grep -n \"helmet\" PHD.txt PHD_mackenzie.txt | head -20\necho \"== NYB ==\"; grep -n \"helmet\\|Helm\" NYB_vol2_glossary.txt | head -20\necho \"== HRN xod ==\"; grep -n \"Helm\" HRN.txt | head -20"
}
```


### [2026-09-14T01:58:53.172Z] TOOL RESULT

```
== PHD ==
PHD.txt:130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
PHD.txt:593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
PHD.txt:2257:helmet targ.
PHD_mackenzie.txt:608:add sirwir [s'lw'l] helmet.
PHD_mackenzie.txt:4929:targ [tlg I N --] helmet.
== NYB ==
1744:gurtéh [gwltyh] a part of the warrior’s armour, *neck-protector’ 855. Skr ren- ders the series zen u zréh u ~ by sarva- sannüha- = tavoTaAta. — gurt- < *kur-t- from the root kur- discussed by Bailey, Nyberg Vol. 9-16: Av. (474) kuirit- (< kurit), nom. kwiris, Vd. 14°, following immediately after zräöö (v. zreh) in the enumeration of a Zoroastrian warrior’s armour, is rendered in Phl. by griv-pan ‘neck-protector’ with the gl. han i hac tarak apác 6 zre bast estet ‘that which is attached to the helmet at the back of the armour’. — Cf gri-kaft.
== HRN xod ==
4620:512. xöl Helm', yöd.
4621:ap. yauda- *Helm*; aw. ayö],yaoda'.
4622:arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd
6072:aw. sära-, särah- *Kopf*; phlv. vergl. sar[var 'Helm\
7504:863. Ualäh \VIütze'; Helm (aus Stahl, Sahn. I, 100 Vers
10976:176. sar^mr 'Helm'.
10977:aw. säravära- 'Helm*.
```


## [2026-09-14T01:59:01.059Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD xwd ==\"; grep -n \"xōd\\|xod \\[\" PHD.txt PHD_mackenzie.txt | head -10\necho \"== HUB 512 ==\"; grep -n \"^ *512\\. \\|512\\. x\" HUB.txt | head\necho \"== HRN leaf ==\"; python3 - <<'EOF'\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (4620,):\n    print(ln, sum(1 for i in range(ln) if '\\f' in d[i]))\nEOF"
}
```


### [2026-09-14T01:59:02.341Z] TOOL RESULT

```
== PHD xwd ==
PHD_mackenzie.txt:3678:naxod [nhwt ' ] N --] chick-pea.
== HUB 512 ==
2018:512. Np. xoi *Helm' ist die lautgesetzliche Form, aber
== HRN leaf ==
4620 127
```


## [2026-09-14T01:59:04.076Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2014,2030p' HUB.txt"
}
```


### [2026-09-14T01:59:04.129Z] TOOL RESULT

```
mit V an. Si vend, ftn *Blut* wird aus xun (vgl. fask
'trocken* = np. xusk) oder vun (vgl. fisagl *Hunger =
g. vasnegi) entstanden sein (Journ. asiat. 1893 p. 242,
261, 262, 265).
512. Np. xoi *Helm' ist die lautgesetzliche Form, aber
nicht belegt; das gebrauchliche xDd^) Helm* ist schwer-
lich aus dem Arab, xudat (pi. xuvaS) zuruckentlehnt.
Dazu arm. xoir *Kopf band, Diadem'. Horn vermeidet
es seltsamerweise, die arm. Lehnworter anzufuhren,
welche r fiir arsacidisch-persisches J haben (ZDMG.
36, 133). Sie sind die sichersten und interessantesten.
Hier sollte nach Fr. Muller (WZKM. 8, 188) np.
xoi 'Gewohnheit, Sitte, Charakter = gr. sd^og, skr.
svadhd- genannt werden, indessen wiirde letzterem nur
ein np. *x^ai entsprechen.
*) Es findet sich z. B. Fird. I, 23, v. 9; im Reim mit durOd
Fird. T, 170, v. 751 (Horn Nr. 555).— 59 —
```


## [2026-09-14T01:59:11.016Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt; echo ---; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; echo ---; grep -c \"\\[pdf page\" BQT_v2_pages.txt"
}
```


### [2026-09-14T01:59:11.088Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
---
---
0
```


## [2026-09-14T01:59:13.817Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT*; echo ---; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\nprint('leaves',d.count(chr(12)))\n\"\necho \"=== ref_page.py usage ===\"; head -40 /home/sfmqrb/git/rishe/tools/ref_page.py"
}
```


### [2026-09-14T01:59:15.050Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r-- 1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
---
leaves 683
=== ref_page.py usage ===
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
```


## [2026-09-14T01:59:18.458Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:785 --image 2>&1 | head -60"
}
```


### [2026-09-14T01:59:19.584Z] TOOL RESULT

```
no scan of BQT covers printed page 785 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:59:23.588Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(d))\n# search for a page with a standalone number to calibrate\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c)[0]!='C' or c in '\\n ')\nfor i in (0,1,2,300,301,340):\n    txt=clean(d[i])\n    nums=re.findall(r'(?<!\\d)\\d{3,4}(?!\\d)',txt)\n    print(i, nums[:6])\nPY"
}
```


### [2026-09-14T01:59:24.893Z] TOOL RESULT

```
684
0 []
1 ['۳۴۳۱']
2 []
300 ['۴۹۹', '۱۷۲٩', '۹۵۱', '۵۳٤', '۷۳4', '۱۷۲']
301 ['۱۷۲', '۹۷۱', '1۹16', '۵۷۲', '6491', '451']
340 ['۳٩٩', '۷۳۳']
```


## [2026-09-14T01:59:30.771Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xaod\\|xao\\|xauda\\|haoda\" BQT_v2_pages.txt BQT_v2.txt | head -20\necho \"=== kaz/kazk ===\"\ngrep -n \"k.zk\\|kāzak\\|kazak\" BQT_v3_pages.txt 2>/dev/null | head\nls incoming/BQT/"
}
```


### [2026-09-14T01:59:30.847Z] TOOL RESULT

```
=== kaz/kazk ===
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
```


## [2026-09-14T01:59:33.430Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\n\"\necho ---; head -c 400 incoming/BQT/BQT_v3_pagemap.json"
}
```


### [2026-09-14T01:59:34.572Z] TOOL RESULT

```
[
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
]
---
{
"pdf": "data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
"pdf_pages": 721,
"offset_mode": 1203,
"anchors": 34,
"map": {
"1210": 1,
"1211": 2,
"1212": 3,
"1213": 4,
"1214": 5,
"1215": 6,
"1216": 7,
"1217": 8,
"1218": 9,
"1219": 10,
"1220": 11,
"1221": 12,
"1222": 13,
"1223": 14,
"1224": 15,
"1225": 16,
"1226": 17,
"1227": 18,
"1228": 19,
"1229": 20,
"1230": 21,
"1231": 22,
"1232"
```


## [2026-09-14T01:59:41.695Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport re,unicodedata\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nhits=[i for i,p in enumerate(d) if 'کلاهخود' in clean(p) or 'کلاه خود' in clean(p)]\nprint('kolahxod leaves',hits[:20])\nhits2=[i for i,p in enumerate(d) if re.search(r'خود\\s*\\(',clean(p))]\nprint(len(hits2))\nPY"
}
```


### [2026-09-14T01:59:44.370Z] TOOL RESULT

```
kolahxod leaves [243, 257, 578]
1
```


## [2026-09-14T01:59:49.136Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nfor i in (243,):\n    t=clean(d[i])\n    print('=== leaf',i,'===')\n    print(t[:3000])\nPY"
}
```


### [2026-09-14T01:59:50.080Z] TOOL RESULT

```
=== leaf 243 ===
 خود خروه                                                                                ”“YA


 دایر - ۷ویمعنیذات و لقیضغیرهم آمدهانت ۷         و لام الف »   کلاا صیفتح کاف        خوب

ونان
   چ        چدنریان
                  چنالکه کوبند ف«لانی خو
میداند؟عنی ذات خود راله دمگریرا »ودر نع             خوب کلان۔ بر وزن موی کشان .
مضاف مضمری آید  -و ضد پیگانه هم هست                 تنگه باشد . بهاترضم
                                                                      بمعنی خوب کلا است ک
چنانکه کوبند «فلانی ازخوداست » معنی بیگاله
                                 يت . ۸
                                                    بای قارسی   خو بله ٣ ا انی ممدو لد و

خود بر ست د باانی معدوله و کر
                                                            بروزن طبله » بمعنی ابله ونادان باشد .
  ستا
    خجبوردو
          بای فارسی ؛ مردم متکبر و مت               حوج  -بروزن کوچ کله سر وفرقسر
                                       باشد .       مرغانرا گونند  وکوشت پار سرخی باشدکه
 خود یسور ٩ با-نالی مسوله کور                      برسرخروی است؟  -ونامگلیاست سرخرنگه
بای ابجد ( )۱و سین بی لقطه ( )۲بواو رسیده            که آنرا بستان افروز کوبند  -کووسفندجنگی
ویزای قطه دار ( )۳زده  ,آتشکده آنربابجان             رانز گفتهاند  1 ۴وترك کلاهخودهمهست  -وتبزی
است*٩ و بجای بای ابجد بای حطی ( )4نیز              طاق وایوان را نگیوزبند  -و حربر سرخیکه
                                      هست .                                  بکرلوگاه نیز نندند .

خودخروج -۱۱با جيم فارسی »                            خو چه  - °بانانینجهول بروزنکوچه.
بهعنی تاجخروس است وآن گوشت سرخی باشد              نمعتی دوم خوچ است که گلستان افروز -وتاج

                      که برسرخروس است .                                           ومغفر خروی باشد .
 خود خروه؟ د باهای هوز .بروزن                       با ثانی معروف بر وزن زود »         جود.

 ومعنی خود خروس است که تاج و مغفر خروس                بمعنی تاج ومخفرباشد  - ۷وبائانی معدولهبمعن
                  و کل بتانافروز ۳۱باشد .          او باشد چنانکه گویند د خود داند » سنی او

     ( )۳چك _:شطه دار .             ( )۷چك - :بی لقطه .               ( )۱چك  :و کسربا .
                                                                          ( )4چك :با.

  رك  :لفت فری  ۵۹۰ورك :خروج و خوچه.            ۴    مصحف «خو بله».     ۳.    رکه:خوب کلان       ۱

                                     غوچه (تاج خروس)« :اسفا۲ :۱ص ۰۷6         عه    ۵    غوچ .
   » تاج خروی   ورك  :خوچ  « :خوج

   (ر
     - ۱پارسی باستان  801121د                   بود و خوچه نکیوزبند « ».لفت فری ۵٩ ح٩۱ .
    خود سر تیز) « اثپیگل ص . ۱۲۲۰استی  (005کلاه ناح) «ك  .است۱٤۸ =                      09     8
    - ۲ضمیرافس" پهلوی )×4۷              پارسی خوی «لغت فرس ۱۲٥۰ ممرب آن خوذة «نفی؟ .
   ربک « ۹۳۱۰مینا ۲٥ :۹۳۱ «ناوادبا  ۷۹۱۰قس:پارسی باستان  )2۷(01 -او 6687۷5
                                                                           ۵نی
  (خود» خویش):اسفا  ۰۲ ۱ص  ۰۹۱۳۷۸۳ ۰۱6۲ ۰۹۱۱ ۸استی« 8680621کث .است› ۹۳۱
  باين معنی «خودی»استو مقپوم آن از جملهمذ کور          ۸          ورک :ص لد از دباچه
```


## [2026-09-14T02:00:03.725Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nfor i in (240,241,242,243,244,245):\n    t=clean(d[i]).strip().split('\\n')[0]\n    print(i,'|',t[:110])\nPY"
}
```


### [2026-09-14T02:00:04.852Z] TOOL RESULT

```
240 | “VAY                                                                                                      خوای
241 | خوان پابه                                                                                                     
242 | ۷                                                                                             خوانچة زر
243 | خود خروه                                                                                ”“YA
244 | e Cs                                                                             خجودرا رسن کردن
245 | خورخجیون                                                                                    YAY
```


## [2026-09-14T02:00:10.743Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport json,unicodedata,re\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\npdf=m.get('1562')\nprint('pdf page',pdf)\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8').read().split('\\f')\nfor p in d:\n    if '[pdf page %d]'%pdf in p[:200]:\n        t=''.join(c for c in p if unicodedata.category(c) not in ('Cf',))\n        print(t[:3500]); break\nPY"
}
```


### [2026-09-14T02:00:11.893Z] TOOL RESULT

```
pdf page 355
[pdf page 355]
Ve rs
la Jabs بسکون زای = IT
از چوب ولی و علف مانند خانهای Su TL
که مزارعان و پالیز بانان بر کنار زراعت و پالیز
اند که درکوه a سازند ۴ ؛ و بعضی جابیرا
" ویابان درز زمین بجهت کوسفند و خر وگاو
مغاره خوانند؛وبسضی guar وغیره بکنند وآنرا
کویندصومعهای باشد که برس رکوهساختهباشند»
و این معنی با کاف فارسی همآمده است» واسح
صاری US وصومعه در عربی خلوت . col این
AT aie راکوبند که سرآترا بلند وباريك
باشد که باغبانان درخت را بدان پیرایش دهند
- نی شاخهای زبادتی آنرا با آن (۱) ببرند
و درخت صنوبرسفار را ليز کونند ۴ ,وباینممنی
با زای فارسی هم آمده است - وسیلی وفنازدن
و شاخهابی باشد از FP وگردنیر! نیز کفتهاند
درخت که صیادان کهنه و لنه و چیزها بر آن
دام در(۲) زمینضب کنند GAG آویزند و بر
رمیده بجانب دام ودانه آبند OT تا جانوران از

باشد که در ایام ae ونوروز ازشاخ درخترامثال
OT آویزند و زنان و کودکان برآن نشینند ودر
هوا آیند وروند .

کاژ © پسکون زایفارسی ؛ بمعنی لوچ
باشد که بعربی احول خوانند» - ودرختسنوبر
صغار را نیز گوبند ۷ .

کازدون © بروزن حاضرون .نامشهری
وولایتی باشد آزفاری ؛ و باين معنی بازایفارسی

آمده انت ۷ .

poe 4 ع با زای فارسی » بی وزن
و tee کاشفر است و آن شپری باشد از
ماوراءالنهر .

SOS ه بنتح زای تفه دار . مطلق
Jp وخاله را گویند عموماً وخانهای کهمز ارعان
ازچوب وعلف بر کنار زراعتسازند خصوصاً *۱-
وتالار و عمارت چوییرا نیز گونند - و صومعه
وخلوتخانة ساریرا هم Salad درسرهای oS
سازند — وعلامتی باشد که صیادان درکنار Sela
شاخهای درخت سازند ٩۱ و چیزها از آنآویز ند

- ویمعتی ob پیچ هم آمده است وآن رسمانی

. چك . چش : بآن . )0( چك » چش : بر (t)

۰ (هم) iS = ۱

۴ - شهرباری که خلافش طلبد » زود افتد ازسمن زار بخارستان » و زکاخ Be .
« فرخی سیتانی ۲۶۵ * .
ee کج RO سکم (مم).

oot - ۲ Cpa) = ۱ بفاری بطول AL وعرض ٩* کیلومت رکه ازشمال
به مستی » از مشرق پبلوك کوه مره واز جنوب به جره ودشتی وخشت و ازمفرب بماهورمیلاتی
وخشت محدود است و جمعیت آن ۶ تن ۰ Sy آ نکازرون در ۱۶۰ کیلومتری شیراز و
۰ تن سکنه دارد « کیهان . جفرافیای سیاسی ص ۲۸-۷۲۷ . ۸ - ره : کاشفر .
4 = کاز ( هم. ) : در سقدی کلمه col که آنرا ]1۳076 خوانده ae ail
GE as) درصحرا ) . هنینگک گوید میتوانآنرا 2۵ خواند معادل کازه 16828 فارسی
Henning , Two Central Asian Words . p . 158 , 3 . note 3 .) (
0° امید وصل تو یستدروهم من STS مرکا کدابان سلطانچگونه باشد ؛
مولویبلخی « فرهنگه نظام >.

۱ رل : gal رودکی ج ۳ ص ۱۲۱۹ ۰

(eo abl olay (
```


## [2026-09-14T02:00:24.898Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"k'zk'kh\\|kzk\\|k’zk\\|kāz\\|k'z\" SOD_pages.txt | head -20\necho \"=== SOD hut/cabin ===\"; grep -n \"hut\\b\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T02:00:24.973Z] TOOL RESULT

```
17035:    4650 k'n'kh      B °* k'z'kh                                         kas (q's) ©Khwar. k*s ©ob. -y(y)
=== SOD hut/cabin ===
17057:                                                                         little house, hut
19917:             mysndy(y)y GMS 1396; mysnt y, STii 2.17                 shut, closcd(ey«)
26315:                                                                          0<?)shut up, (r<9)cease speaking
38535:     house of Buddha          8245              hut 4682                                 imitation      7784, 7790
39436:shut    5662                              sister's son 4327, 10700                  smartweed    3800
```


## [2026-09-14T02:00:27.023Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17030,17070p' SOD_pages.txt"
}
```


### [2026-09-14T02:00:27.082Z] TOOL RESULT

```
           kan =»kJm\ -q>                                                worker
           future particle
                                                                          MDii, A-9R3, p96.3; Gersh. Advice. 85
           GMS 646-50
                                                                    4666 k*s B, M, S          (^^(T^iT          :J-^S)Sy~
    4650 k'n'kh      B °* k'z'kh                                         kas (q's) ©Khwar. k*s ©ob. -y(y)
                                                                         pork, pig
    4651 q'ny* M                        (UT;J^)^l^bU
         kanya                                                           TSP 3.138, 9.44, 13.17; SCE 88, 122, 141, 360;
         stupidity                                                         Anc. Lett. 3.24, BBB f8, 766; GMS 822, 1683;
         BBB 716                                                           Hen. LW 99; Frye 2
    4652 k'p B                                        <*io3 t AX7
         kap?                                                       4667 q's C =» k's
                                                                    4668 k's M                                         j£&
         piece                                                           kas ©Parth. k}$
         TSP 3.180; Hen. Texts. 728; k>p\ TSP 3.196                      Kashghar
    4653 k'r S -» »ztk>r                                                 Sogdica. 8.10
    4654 -kVk            («jf» i^J» J.>U.)«»ju^» ^a, ju^            4669 k's'k B, M, S                             ^jjtf
         kare (-k'ry, -q'ry, -k}rk, -qry) ©<*kdraka                      kase (k'sk)
           ©f. -q>ra suff. =*-kr>k                                       (//ww)Kashghar
         making, doing                                                   Sogdica. 8.10c, n p!0; GMS 1048; MDii; TSP



,
 187                                                                                                              kpnyyn

                                                                         little house, hut
         8.185; Texts. 737; f. kl q}Pnc, GMS 1048; MDiii
                                                                         VJ 952; Hen. Mittelir. 126
4670 k'skp95=* k's'k                                                4683 qbn    C =» kpn-
4671 k't S                               jV^<v£f «JV                4684 k0n- B, M                                Sx\ ^
     kat/9 (q>t) =»k>6n                                                  ka(3n (qbn) ©<*kabna; Yaghn. kavm
     dumb, deaf-mute, mute                                                  <*kambna ©ace. -w; abl. -> =>kPny, knpy
     BSTi 139; Benv. JA 1943-5, 101 n5; BSTii                            little, few
        886.23; C2, 51R23; Frag. Len,, S W, BSOAS                        Hen. Texts. 732; BBB d7 cl6; C2; Benv. Notesiv
        1981, 236                                                           515
                                                                    4685 kpn'kpnw      B                              ff
4672 q>t C =» k>t
4673 k't'k B                                                             kaPne-kaPnu =>kpnw
                                                                         little by little
```


## [2026-09-14T02:00:32.943Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"k'z\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T02:00:33.017Z] TOOL RESULT

```
17035:    4650 k'n'kh      B °* k'z'kh                                         kas (q's) ©Khwar. k*s ©ob. -y(y)
```


## [2026-09-14T02:00:39.910Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Mittelir. 126\\|VJ 952\" SOD_pages.txt | head; echo ---; sed -n '17070,17130p' SOD_pages.txt"
}
```


### [2026-09-14T02:00:39.988Z] TOOL RESULT

```
17059:                                                                         VJ 952; Hen. Mittelir. 126
---
                                                                         little by little
     kate ©Khwar. kyU Pahl. kadag                            <s*
     game, play             v                                            BSTBL; GMS 1199

     VJ 283, 288, +kr- "to play", k}tyw kr-                         4686 kpnJkk B, S                              Sx\<^
4674 k'tsy'nty S                                                         kaPnak, kaPne (qbnq) ©*kaflnakka- =»kpny
     kat-sxandc (q>tsxndy) ©pi. -t                                       little, a little
     mockery, ridicule                                                   VJ 1463, 1475; GMS 982; STi 34.2; Sund. AoFviii
     BBB p84, 716; GMS 344; Frag. Len. 70.8                                 1981 p215; STii 2.15; MD A-9 R14; C2, 87V6,
                                                                            60R3; S W, CLI 1989, 180
4675 k'tsyVS B                                  a>
     kat-sxar5 ? ©KkVk-sxrS ?                                       4687 kpnyw'r'k B                       ^^jul^y^/
     mockery, ridicule                                                   kaPn-xwar6
     SCE 143                                                             drinking little
                                                                         BSTBL, Intox. 19
4676 q'tsxndy M =» k'tsy'nty
4677 kV B                  <u>>^          i jj)>S At i<J}Je*j iAj   4688 qbnq C -» kPn'kk
       ko (qw2) ^kw1                                                4689 kpnptz'n'y S                        fiJ «±te^
       to, at, in                                                        kaPn-patzane
                                                                         little known
     GMS 1629-32. Jfe'w. . . s*r, k>w.
                                                                         KG 482
4678 kV B, M                                      <S"^> «Uf
                                                                    4690 kpnty* S                                J^^
       ku ^'kw2, kw2                                                     kaPnt/dya
       where
                                                                         a little, shortage
       VJ 1067; SCE 542-3; BSTBL, Vim. 64, 178; GMS
                                                  p'r                    MDii p 176.1
         1531; kywtyy Frag. Len. 93.10
4679 k'wt'm B                                                       4691 kpnw                                    ifSiSxl
                                                          u/
     k/gotam                                                             kapnu (qbnw) ©ace. adv.
     Gotama                                                              a little
     TSP 5                                                               VJ 958; TSP 3.195, 13.30-, BSTBL, Dhu. 208, 151;
                                                                           C2, 31V 11, 12, 48R 27; MSP; GMS 1195
4680 q'xws'ty C                      (e>jjj£ (jUj)^ if \j£**\
     kax-wisate ©ace. -tw                                           4692 qbnw    C =» kpnw
     vomiting
                                                                    4693 kpny B, M                           Sx\ ^
       BSTii 829.21: C2, 102R21; Benv. JA 1955, 300                      kaPne (qbnq, qpnyy) ©comp. adj. =*kmby(y),
4681 q>yn C                                                jj;
     kayin                                                                  knpy,a little
                                                                         little,   kPn}kk
     Cain                                                                VJ 899; TSP; SCE 308, 312; BSTBL, Intox. 31;
       C2, 51V 17,29                                                      BBB dlO; kfiny kpny, TSP 3.178, 231 n pl77;
                                                                          GMS 1211
4682 k>z>kh B                             K&tJ^f^
     kazak, kaze (k'n'kh)                                           4694 kpnyyn ? B                        ^ ccMUJl ^jTjuI
  qPnyy

       kapn-yaxn ?
       meagre, remnant                                             kaSac (qd>c) ©<ka<5a-cih Parth. kd'c
       TSP 13.14; S W, HJ 1976,59                                  ever, never
                                                                   EGSii 159f; GMS 1559-, VJ 1115; TSP; BSTBL;
 4695 qpnyy    M =» kpny
                                                                     MDii; Hen.; Tales.; STi 21.15; Sund. AoFi 1974,
 4696 kprSh B           (Jf t/Jr t<siJJh jS fi)J^j>j
                                                                     6V13; q6>c, Cosm. 307.32, 64; iW'cw, Frag. Len.
      kaparS ?                                                       38, 28; MSP b79, 114, 111; Dhu. 71
      \ecks(Benv: caper)
```


## [2026-09-14T02:00:47.022Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la MON_part*; python3 -c \"\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    d=open(f,encoding='utf-8',errors='replace').read()\n    print(f, len(d), 'leaves', d.count(chr(12)))\n\""
}
```


### [2026-09-14T02:00:48.359Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part1.txt 2611770 leaves 0
MON_part2.txt 2568024 leaves 0
```


## [2026-09-14T02:00:51.221Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"کازه\" MON_part1.txt MON_part2.txt; echo ---; grep -o \"کازه[^\\n]\\{0,200\\}\" MON_part1.txt | head -5; echo \"--- skureh ---\"; grep -o \"سکوره[^\\n]\\{0,200\\}\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-14T02:00:52.389Z] TOOL RESULT

```
MON_part2.txt:3
MON_part1.txt:2
---
کازها: تقریاً در یکك سطح 
کازهای داخلی منابع 
--- skureh ---
MON_part1.txt:سکوره] (ا.) کاسة سفالین؛ کاس گلین. جام 
MON_part1.txt:سکوره ِ اسکره ِ
```


## [2026-09-14T02:00:54.169Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \".\\{200\\}سکوره.\\{300\\}\" MON_part1.txt | head -5"
}
```


### [2026-09-14T02:00:54.234Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:00:56.888Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport re\nd=open('MON_part1.txt',encoding='utf-8').read()\nfor m in re.finditer('سکوره',d):\n    print('---')\n    print(d[max(0,m.start()-400):m.start()+400].replace('\\n',' | '))\nPY"
}
```


### [2026-09-14T02:00:58.155Z] TOOL RESULT

```
---
سا کن کردن.  | خانه‌نشین کردن.  |  | اسکدار: 22۲ [لهجه‌ای از اسکدار و  | معر.] (ص‌مر. امر.) بیکك سوار» پیکك بیاده.  | خریطه و کیسة پیک‌ها که نام‌ها را در آن  | گذارند. بایگاه و منزل پیک‌ها.  | اسکربوت: ۲۱ (.) (بز.) مرضی که  | بر اثر فقدان ویتامین ث در بدن پیدا شود. و  | علائم آن شل شدن لثه‌ها و ریختن دندان‌ها  | و خونریزی زیاد بر اثر جراحت مسختصر  | است؟ اسقر بو ط» فسادالدم.  |  | اسکر ۵ (۵0۳۲2)6-. ,(6-)0350۲2 [< سک ۵ -<  | سکوره] (ا.) کاسة سفالین؛ کاس گلین. جام  |  |  | آب‌خوری. پیمانه‌ای بوده است برای  | اندازه گیری دارو.  |  | اسکفه: 2 (معر. ارمی اسقو فتا] (.)  | آستانه» آستان‌در.  |  | اسکلت: 6۱ استخو ان‌بندی.  |  | اسکله: عاعتای رداف‌اه آمکعر. و متر] (ا.)  | بندرء لنگ رگاه» بارانداز کشتی‌ها.  | اسکناس: عقجعمه (.) نوعی کاغذ بهادار  | که بهای وی بر روی آن نوشته شده و برای  | خرید و فروش بکار می‌رود؛ پول کاغذی.  | نشر اسکناس: چاپ کردن و انتشار دا
---
س‌عر. سکرچه]  | ظرفی است کوچک که در آن نانخورش‌ها  | نهند و بر سر سفره گذارند. واحد وزن.  | سکرجه صغیر : واحد وزن معادل سه اوقبه.  | (رسالهٌ مقداریه. فرهنگ ایران زمین.  | ۴2۰ ص ۴۲۲). سکرجة کبیر: واحد  | وزن معادل نه اوقیه و آن را صدفه گویند.  | (رسالةٌ مقداربه. یضا) سکرجه مطلقه:  | واحد وزن معادل شش استار و چهار یک  | استار.  |  | سک رکه: (0۲0:۵)۵: [حبشی - سقرقع»  | معر.] (ا.) شرابی که از ارزن سازند.  | سکره: (6-)0۲2: [- اسکوره ِ اسکره ِ  | اسکرچه - سکرچه - سکرجه معر.] (.)  |  |  | کاسة گلی. (پز. قد.) پیاله‌ای است که  | مقداری معین جا بگیرد؛ سکرجه.  |  | سک زدن: ٩0‏ راندن چاریا به وسبلة  | سک. (مج.) تحریک کردن» اغوا نمودن.  | سکس: 6 (.) جنس» مجموع افرادی که  | از یک جنس هستند ( کم.) جنس زن. صمح.-  | احتراز از استعمال این کلمة بیگانه اولی  | است؛.  |  | سکسک: 0۲۵0۶: (ا.) زمین ناهموار و  | درشت.  |  | شنکشیک: (ص.) اسبی که چون تند  | حرکت کند خود را بجن
```


## [2026-09-14T02:01:09.832Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i in (311,312,313):\n    print('=== leaf',i,'===')\n    print(d[i][:2500])\nPY"
}
```


### [2026-09-14T02:01:11.313Z] TOOL RESULT

```
leaves 858
=== leaf 311 ===
ó (1) “hut, tent, pen; prison’; Br. krau, kroe ‘stable, stal’; W craw ‘hovel, sty’; Cor. crow ‘shed’; OCS (and com. Sl.) krovü, m. "roof
kregoros, ios ‘cormorant, heron’. See next W creyr, pl. -od ‘heron’; Cz. kfehaf *cormor- ant'. Cf. kregó
kregotos (kregutis, kregitos) ‘shrill cry”. Cf. kregó W crewt ‘faint cry’; Icel. hrik (écreak?. Ambig. cf. krig-); Cz. kfeh-ot ‘shrill cry’; Li. cf. kregždē “swallow, martin”
kreeg ‘croak, caw’. WP I, 415. Cf. kregoros, kregotos W crëu “cry, caw'; Cz. krehat “call, as part- ridge’; Slovene cf. kreg, m. ‘quarrel’; Li. kregü, EU ‘grunt; chatter, as bird?
kreiio, see kreio (1)
kraupio — kreko, ið
20
25
30
35
40
45
546
kreiuos ‘bent’. Slav. and Li. only. Cf. kriuos, kroiu- OCS (and com. Sl.) krivü, id.; Li. kreivas, id.
kreio (kreiio, kroio) (1) “bring to life; luxuri- ate, multiply, abound’ Gk. cf. a-krá-antos ‘unfulfilled; fruitless’; Lat. Creo, creare ‘create’; re-creo ‘enliven’; cf. in- cré-mentum ‘increase’; Br. krui, v. (‘create’. Mng. infl. by Lat.); W creio 'freshen, enliven'; crai, adj. ‘fresh, lively; OCS cf. o-krijo & 0-krájo, -ati *convalesce, recover’; Cz. o-kfeju, O-kfát, id.; Latv. cf. krietns ‘stalwart; Lat. cré-ber, f: cré-bra (luxuriant, numerous, thick, frequent, fr. *kre- + *-bher-)
kreio (2) ‘pine, fret ON hrjá, id.; Blg. krája, id.
krek- "a raucous bird; bird-cry'. Cf. WP I, 413 & krik-, kreko, etc. Skt. cf. krakarah 'kind of heron'; Gk. kréx, gs krekós ‘landrail’; Lat. crex, gs crecis *daker- hen’; W crec ‘chirp’ beside cregyr, m. ‘heron’; Cz. krek ‘croak’; Pol. cf. krzekac ‘squawk’; Big. krec 'tree-cricket'; Latv. (*-&-) krekjs ‘nuthatch’
krekolos, à, is (kreklos) 'crosspiece, stay, stake, bar, stick’. Cf. WP I, 422, 483 and see krikol-. ((2) ‘garment’, see Supt. K) Ir. (ambig.) creachail ‘crooked wood, block, stump’; OE brëol ‘reel’; ON hræll *weaver's sley’; Li. kréklas ‘rafter, truss, crossbar’. Rad- ical in Blg. kreć 'centre-pole of threshing- floor’. For OHG rigil, MHG rigel (G Riegel ‘bolt, bar’), of ambig. vocalism, see krikəlos
krekəros ‘heron’. Cf. krekō, etc. Skt. krakarah, id.; W cregyr, id.
krekitos, a ‘stridency; strident creature’. Cf. krikət- W cf. creciad ‘chirping’; criciad (‘cricket in- sect, fr. Se or *-1-); Fr. criquet Conicket, fr. Gallo-Lat. unrecorded); OCS krěćetů ‘tree- cricket’; cf. kreksto, krektati ‘croak’; R krèčet ‘gyrfalcon’; Big. cf. kreketùša ‘frog’
krekō, ið ‘creak, screech, grind, grate’. Cf. WP I, 463, 483 & 486 and next Skt. cf. krákşamānah, adj. ‘roaring, raging
=== leaf 312 ===
’; kres-ba ‘design, draw- ing” (beside variant o-krs ‘district’. See kirKos). (Isophonic are Slovak kres ‘dawn’; Latv. krēsls *dusk")
kreKus (kerKus) (?) *weaver's sley, comb’ Gk. cf. kerkís, id.; Alb. krehén, krahén, krahán ‘comb’ beside kreh, kref, v. ‘comb’; W (*-e-) cf. crib ( ‘comb’, if fr. *kreKu- as ebol, m. ‘colt fr. *eKulo-)
krembo (kromb-) ‘twist, bend, turn, folg’. Cf. WP I, 276, IL, 373 & 589 & krinbos below Gk. cf. krémbolon *bobbin' (isophonic: krém- balon ‘rattle, castanet); OHG hrimfan, rim- phan, MHG rimphen ‘crease, crumple’; OE hrimpan, id.; Du. cf. rimpel ^wrinkle'; Li. cf. kremblyjs (a fungus)
krémen-, krémno- ‘rocky, hard; rock, flint". Cf. WP I, 419, 483 & II, 583 Gk. kremnós ‘cliff; Br. cf. (variant) krémen, f. ('grime', fr. *kremben- to account for -m-, not *-v-); MHG ram, ran, m. “crust of oxide, patina, soot’; G Rahm (2) ‘soot; OCS kremy, gs kremene, f. beside kremeni, f. ‘flint’; Pol. krzem ‘silicium’, krzemian ‘silicic acid’; Blg. krem ‘flint’; Cz. křemen, id. Cf. Latv. krams ‘flint
krémil- (krémbil-) ‘flint, pebble’. Cf. kré- men-
krekos — krep-
20
25
30
35
40
45
548
W crimell, f. (sharp ridge’, fr. *kremb-); Cz. Kiemel, m. f. *pebble'
krems- (krem-, krms-) ‘crunch, gnaw; crun- chy fat, cracklings, gristle’. Lat. cf. cremium ‘fried meat; Umb. krematruf, acc. pl. m. *crisped or fried fat’; MIr. cremmim, Ir. crei- mim ‘gnaw, chew’; Ir. creim, f. id.; Li. krem- sið, éti ‘crunch’ beside (o-gde) kramsiü, eti, id.; Latv. cf. kremtu, krimst ‘gnaw; clutch at: cf. o-gde ON hremsa “clutch? and Li. (z-gde) krimstala ‘gristle’
kremusó(n), kromuso(n) “onion, garlic’. Cf. keromuso(n), kermsos. WP I, 426 In this sense cf. Hes. krémuon, Gk. krómuon; Ir. creamh; OE hramsa or hramse; E ramsons; R Ceremica; Li. kermuse “wild garlic”
krengh- ‘ring, circle, belt, girth’. WP II, 570 Umb. cf. krenkatrum, cringatro (rope? or sim.); OHG, OE hring (fring, circle’. OE also hringe, f. id.); ON hringr, id.; OCz. kráž, id. O-gde in Cz. kruh; Pol. krag, id.
krenk- (1) OE hringan “clash; ring’; Sw. ringa, id.; Pol. krzgkac ‘hawk, cough’; R krjákat ‘quack’; Li. krenksSiu, krenksti ‘hawk, cough’; Latv. cf. krencelis ‘dry cough’; Icel. hringla ‘jingle’
krenk- (2) MHG ring, ringe ‘lightweight; paltry; easy- going; bad’; Sw. ringa, adj. ‘paltry’; Slovak cf. (?) kriak “low bush’; Latv. krencelis (2) ‘tuft, bunch?
krēnos (kren-) ‘withered, old, dry, sickly'. Cf. krn- MIr. crin, Ir. crion, Br. krin, OW & W crin, Cor. cryn, 1d.; MHG ron adj. ‘lean, frail’; G rahn (fa
=== leaf 313 ===
it, křísit, id. See next
krésro- (?) “hale, hearty, luxuriant’. Cf. kresKo Lat. creber, f. crebra ‘luxuriant, frequent; ON hress *hale, hearty'
kretolos, kretilos ‘rattle, clatter, din". See kretó & cf. krotolos Ir. creatal, id.; Li. kretilas, id. (Fr. crécelle ‘rattle’ appears to derive from a form *cre- cilla, but a Lat. form crepitacillum, id. occurs)
kretoros ‘inner place, sanctum, bosom’? Ir. creathar ‘sanctuary’; OE hreóer ‘bosom’
krētər (kréter-, kret-) ‘sieve’. Cf. krīt- Gk. kreséra; Mir (ambig.) críathar, f. id.; Ir. criathar, id.; (*-e- in) Li. kretelas, kretilas (2), id. and in Latv. kretulis, id.
kreto, ið ‘shake, tremble, rattle? Cf. WP I, 424 & 484. See kretolos, krot- Ir. creathaim, crothaim, id.; MHG réden ‘iddle’; OE hrióian ‘shake, shiver’; Srb. kre- Cem (se), kretati (se), tr. intr. ‘move’; kret, sm. *movement ; Li. krečiù, kresti ‘shake’; krataü, -ýti ‘tremble’.
kreudos, is (kroud-) ‘rough, harsh, hard". (Vowel ambig., cf. krüd-, krusd-). WP I, 479 Lat. (ambig.) crūdus ‘raw, fresh; queasy; cruel; MIr. crúaid, Ir. cruaidh, Mir. cpds. crúad- ‘harsh, severe’; cruaidh, f. ‘steel’; ON cf. hrjóstr, n. ‘wasteland’; hrjóstugr ‘rough, barren’ (fr. *kreusd-, cf. krusd- below)
krequ- — kreut-
20
25
30
35
40
45
550
kreudhos, om (?) ‘whip, reed'; (2) ‘shake’? OE hrëod, n. ‘reed’; OHG hriot, OS hriod, id.; Lusat. krjud, m. ‘whip’. (FK: EWDS 17 otherwise). (Isophonic: Skt. krodhah “anger? beside krudhyami *be angry': Av. xraodei(mi) “fear, tremble’)
(kreuk-, see krukis. E-gde only in R krjuk ‘hook, crook, hinge’ and in W crugo ‘torment. OS hreuwan ‘accuse, offend? is prob. fr. *kreuuo)
kreukio (kreuksio) ‘cough, pant OE *hreohan implied in hreoung, f. ‘panting’; Li. cf. kriaukSiu, eti, v. hawk, cough up’; Br. cf. kraost ‘phlegm’
kreuKos, ios (1) “height, cliff, mountain’. Cf. WP I, 573 & II, 477 Mir crüach, f. “pile, hill; Ir. cruach, id. and ‘mountain’; W crug ‘pile, hillock'; Cor. crüg, id.; Br. cf. krügel, f. id.; Li. kriauSis, ies f. & kriauSius, m. “cliff, height. (A variant arises in OE hreac, ON hrauk-, cpds. ‘rick, pile, fr. *kroug-)
kreuKos (2) ‘noise’
Skt. kró$ah 'shout'; Br. krük, krüg ^warble- fly’; OE hréoh ‘storm; stormy”
kreup- (kroup-, krüp-) “rough, gritty; rough- ness, grit, grains, See below for variants. WP I, 481 OHG hriuva (*hriuba (plague); OE hreof ‘rough, scabby, leprous'; ON hrjüfr, id.; Latv. kraupis, kraupa “mange, scab'. (Long-zero-gde in Alb. kripë 'salt). (An alleged Li. kriaüpa *scurf? is untraceable)
kreuqulis, os (?)
```


## [2026-09-14T02:01:16.770Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (335,336):\n    print('=== leaf',i,'===')\n    print(d[i][:3000])\nPY"
}
```


### [2026-09-14T02:01:17.897Z] TOOL RESULT

```
=== leaf 335 ===
��; kpic ‘make a fool of": Ukr. kpyty ‘jeer at
küpió (2) ‘surge, swell, stir, seethe’. WP I, 379 Skt. kupye, mp. ‘seethe, stir; desire’ beside (e- gde) Copàmi, tr. ‘stir; Av. kup-, id.; Lat. cupio, īre & Gre ‘desire’; Br. kia (ambig; suffer); EME huff, v. ‘swagger’; Norw. hovne, pp: hoven ‘swell’ beside (variant) hovere ‘exult’; OCS kypljo, kypëti ‘well up, rise, swell, abound’; Cz. kypět, inf. ʻeffervesce’; Latv. kūpu, inf. kupt & kūpēt, kūpst ‘ferment, smoulder, work — as yeast’; Li. cf. kūpsoti, inf. ‘puff oneself up’. Cf. (short grade) Pol. kiep, inst. sg. kpem "Tool
küpos (1) & (2), see küpa
küprió “shake up, stir, loosen; burst forth, effervesce, swell, be turgid’. Cf. WP I, 380 and kupið (2) Gk. kuprízo ‘blossom’; cf. küpris “Venus: love’; Umb. (?) kubra-, adj. (queried: ‘good’. E. Vetter: HbID: p. 167); Du. huiveren “shiv- er; Fris. huverje, id.; Norw. hovere ‘exult; Cz. kypřit, inf. ‘loosen’; kyprý, adj. “loose, friable’; Slovak kypret “become loose, friable’; cf. OCS kyprü, adj. “loose, flaccid’
kur- (1) ‘round, curved’. Cf. kuruos, kor-. WP II, 568 Arm. (ambig.) kor (fcurved, bent; curve’. Cf. kor-); Gk. kur-tós, id. (Aeolic alleged ‘kurpós’ is a misspelling for kurtós); Ir. (ambig.) cor, m. (bend, turn’. See kor-); W côr, m. & f. (‘circle’. See kor-)
kur- (2) 'skin-covered boat, fishing-basket, creel’ Arm. kur, gs kri, i-st. ‘skiff; wooden bowl’; Gk. cf. kúrtë ‘creel’; LLat. (Gallo-Lat.) curu- cus, m. dim. ‘coracle’, cf. cur-cuma ‘straw bas- ket’; W cwrwg, pl. cyrygau ‘frame, carcase; coracle, boat’; Ir. cf. curach, m. & f. ‘coracle’
kur- (3) (kuros, om, iom, iə) ‘heat, fire, fuel, burning’. Cf. WP I, 418 Per. küre ‘fireplace, forge’; Go. haúri, n. ‘coal’; pl. haúrja ‘coalfire’; ON bert, gs hyrjar, m.
591
fire’; Li. küras ‘fuel’; kuriü, inf. kürti ‘light a fire’; Late kuru, kurt, id., beside kure 'heat- ing’; Skt. cf. külayami ‘singe’
kür- (4) ‘blind; deaf. Cf. quor- Per. kür (“blind”). But for Gk. porós: Pol. kary, see quór-. Per. -ü- is of ambig. origin); Li. cf. kuřčias, kurtas, kurtüs ‘deaf; Latv. cf. kufns, kuflis, kufls, kursls, id.; Finn. LW kuuro, id.; Est. LW kurt, gs kurdi, id.
kur- (5) (kurs-) ‘run, race, dash". WP I, 428. Cf. Kurs-. (Lat. & Gmc. are ambig.) Lat. curro, ére ‘run’; MHG hurren ‘dash, run’; OE hyrsian (queried) ‘run together’; ON (al leged) hurra “rush, rumble’; OE cf. hors, n., OFris. hors, Fris. hoars ‘horse’; Li. (*kur- in) kuriü, kort (3) ‘run, dash? beside kurnù, -éti, id.
kur- (6) (residual element of type quer- (1), q.v.) ‘do, make’ Skt. cf. kuru- (dual & plur. stem of kr- ‘do, make’); kuru! *do'!; kurvat (act. part. ‘doing’, fr. *kurunt- or *qurunt-); Li. kuriù, kürti (3) ‘build, create’; cf. küryba “creativity”
kür- (7) (residual element of type quor-, q. v.) “where, when, why'. WP I, 521-3 Alb. kur ‘when’; Lat. cür ‘why’; Ligurian (in Rumansch) cur ‘when’; Li. & Latv. kut, kur (^where'. Latv. also *whither")
küreió ‘get, acquire’. (Residual long-gde of type keuro (1), q.v.) Skt. kürayami ‘stea’; Gk. 
=== leaf 336 ===
 korgà (“bent old woman’. Also ‘reef, sandbank’. Cf. krgos); Du. hurk, f. ‘haunch’; hurken, v. ‘squat’; cf.
kür- — kurn-
20
25
30
35
40
45
392
Srb. kvrga 'knot kürio (kureið) “light, burn’. See kur- (3) kurk- (1) ‘rumbling of bowels, belch, croak’. Variant of krk-, q.v. Sl. ambig. Cf. WP I, 414 and kurkulið, kurkurið Gk. cf. korko-rugé, cpd. ‘rumbling of bowels; roar’; LLat. corcus, ‘rumble in bowels’ beside Jt. córcoro, id.; cf. Lat. curculio ‘windpipe’; OCS krükno, noti ‘croak, pipe’; Cz. krkat, krknout, inf. ‘belch’; Blg. krúkam ‘shout; gulp;
` quaff’; Srb. krča, 3s. ‘rumbles in bowels’ be-
side kvrčim, ati ‘grumble, purr’ (Slavonic forms ambig.); Li. kurkiù, ti ‘croak, gobble, as turkey’; kurke, f. ‘turkey’; Latv. kurkstu, kurkt, v. as Li. For OE horgian, horian, hyran ‘hawk, cough’ see krk-).
kurk- (2) “squat, cower'. Cf. kurguos (2) W cwrc, cwrcwd, m. ‘squatting’; Cz. kréit, inf., id.; R kórCit, inf. ‘cramp, squeeze’; kórca, f. ‘cramp’
kurk- (3) 'stir, rouse; move', intr. Gk. cf. kurkanë ‘disturbance, stir’; kurkanáo ‘mix, stir, confuse’; Blg. krákam ((2) “stir”, intr.); Lusat. krkac, inf. ‘fling’
kurk- (4), see kurquos and cf. kurguos (1) and kork-
kurkurió ‘rumble, esp. of bowels’. (Variant: kurkulio. Cf. kurk- (1), gurgulio, gurgurið. Ono- mat.) Arm. (ambig.) krkram ('gobble, croak’. See gurgur-); Ir. córcoro ‘rumble of bowels’; Blg. krákorja (beside krukam), id.; Li. kurkuliuoti, inf. (variant: *croak")
kurmos, à, is (1) ‘accretion, mass, substance, body, food' Alb. kurm “body; slice; cutlet’; cf. kurma-gjak “black pudding’ (possibly a SI. LW in some senses); Gaul. (isophone or cognate) koürmi ‘beer’; Ir. corm “ale? beside cuirm, m. “ale; food'; W cwrf, pl. cyrfau, m. “body, trunk of body’ beside cwrw ‘ale’; OCS krümü, krüma, krümlja 'food'; Srb. cf. krme, n. ‘pig’; Latv. cf. kurmulis “lump, mass’
kurmos (2) (?) (a creature ‘creeper, crawler’ ?) Skt. cf. kürmah, kurmih, m. f. ‘tortoise’; Li. kurmis, io, m. (‘mole’, zool.); Latv. kurmis, id.
kurn- (1) (Kurn- ?) “head, knob?. Cf. Krn-
593
Hes. kürna, kurnika “heads, skulls’; Maced. kürna, id. (and *dolt); W cwrn ‘spire, knob, pile’; Arm. (?) krni ‘gorse’
kurn- (2), cf. kor-, kur- Ir corn ‘roll, coil, bale’; cornaim, v. ‘roll, coil; Arm. cf. (denom.) koranam “bend; warp; stoop'
kurquos (kurk-) “filth, mucus'. Prototype uncertain. Cf. kurguos (1) & kork- Arm. (ambig.) kork, Let ‘filth’; OE horh, gs horwes, id. (& mucus"); Latv. cf. kurkstu, kurkt (2) ‘rot, grow mouldy’
kurs-, see Supt:K
kurst- ? *moor, wasteland'. Cf. WP I, 408 & 421. (Phonol. ambig., cf. korst- (2), and qurstis W cors, pl. -ydd, f. treedbed, bog’; Cor. cors, coll. ‘reeds’; Br. kors, id.; OHG hurst, horst ‘thicket’; OE hyrst ‘wooded hill, hurst
kurtis ‘enclosure, shed’. (Lat. and Go. am- big. cf. kortos, is (4) and krt- (2) Skt. kutib “bend, curve; hut, shed'; Lat. (am- big.) cors, gs cortis, usu. cortes, pl. ‘coop, yard”; Gk. kürtis ‘wicker basket, cage, net beside kürtos, kürte, id. (Go. haürds, etc. pre- ferably to krt-
```


## [2026-09-14T02:01:24.106Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (337,338):\n    print('=== leaf',i,'===')\n    print(d[i][:4000])\nPY"
}
```


### [2026-09-14T02:01:25.258Z] TOOL RESULT

```
=== leaf 337 ===
type *kusdhero-, *kusdhro- in Skt. küharah, m. ‘hole, cave’; W cwthr ‘vulva, anus’
(kusimno-, see kusKimno- (kuKsimno-))
kusio 'tug, drag, strain, tease, incite' Skt. kusami, kugnami, pp. kusitah “pinch; téar; Av. kuš- *téar; kil; Per. kusam, -1idan ‘strive’; Gk. kunéo, fut. küssó & kuüso (2) 'im-
kurn- — kut-
10
20
25
30
35
40
45
594
plore’; EME to hoze (dogs) 'incite, scare off; (long-gde in Sw. af-hysa ‘demolish’, but prob. denom. fr. hüs *house"); OCS kùšọ se, küsiti se ‘draw lots? beside küsinéti ‘dally, drag on’ (but cf. next entry); Li. kusaü, -yti ‘rouse, incite’. (Isophones: Hitt. kusne(mi) ‘hire’; Latv. kust, v. melt Cf. Gk. cpd. pros-kunéo *prostrate oneself"
kusKimnos (kuKsimnos) (?) ‘dragging, dawd- ling, sluggish’ Icel. hyskinn, id.; OCS küsínü, id.; R kosnyj, id.; Li. ? cf. kušù, éti, intr. “stir, move"; küsinti, inf. “stir; touch’; Latv. cf. kusls ‘ailing’
kustis “skin; skin bottle, bladder Gk. küstis, f. ‘bladder’; Ir. cust ‘skin, hide’
kusthis, os, a ‘tuft; tufted plant Skt. kusthah, -am (a plant); cf. (long-gde) R kisti, f. ‘tuft, bunch, cluster, wrist, artist's brush’; Li. cf. (variant) kùškis, gs -io ‘tuft, wisp, flock of wool (with the possible conso- nantism of Lat. cusculium 'scarlet oak' and cuscuta *dodder")
kut- (1), (kutik-) ‘tickle’. Cf. gudil- (gudul-) Arm. (ambig.) ktik-ktik ollam, id. (cf. gudil-); Blg. kátkam ‘fondle’; Li. kutenü, -énti (2) ‘tickle’; Latv. impers. man kut, inf: kutet ‘itch, tickle'
kut- (2) ‘strong; strength'.' See kutor-
kut- (3) 'diminutive'. Variant: kütoko- Av. cf. kutako "little; Per. cf. kütàh ‘short’; kucak “little; küdak ‘boy’. (Li. kūdikis, m. “child” seems to be a Slav. LW. fr. *xud-)
kut- (4) (küta, is) ‘stump’ W cwt, f. and cot, pl. -iau, f. ‘tump, tail’; OCS kyta “arm, shoulder’; Cz. kýta “leg, haunch’; Big. kita ‘penis? '
kut- (5) (kütos, à) ‘tassel, tuft’ Blg. kit ‘tuft of wool, fibre’; OCS cf. kytüka ‘bunch’; Cz. kytka, id.; Li. kutà, and fpl: ku- tos ‘tassel, fringe? beside kütas, m. id.
kut- (6) (kūtis, à, io) ‘shelter, house’. See next Per. (?) kuc ‘household’; Hitt. kuca (queried) "wall, side’; Ligurian (in Rumansh) kuts ‘house’; a kuts “at home’; Ir. cuithe, m. ‘den, pit; OE hyó ‘harbour’; Li. kūtis, gs -ičs, & kūtē ‘stable, stall; Latv. kūts, gp kücu, f. id.
kut- (7) (kütis, os, iom) “container, skin”. Cf.
 
595
kut- (6) Arm. cf. (?) ktit, gs kčči, Let 'earthen pot (from *kütitis?); Gk. kütos, n. ‘hollow, belly, jar, body'; kutis, f. “box, basket'; cf. Gk. ég- kuti (“on the skin”, fr. zen Lat. cutis, f. gp *cutium 'skin"); OHG hüt, gp hütio, f. id.; adj. *with a skin'; OE hyd, f. id.; ON húð, pl. ir, f. id. beside hýði, n. ‘husk, shell’; W cwd, pl. cydau, m. ‘pouch’
kut- (8) ‘grain, kernel, nut? (?) Arm. (ambig.) kut, gs kto, o-st ‘grain, kernel; OHG hodo ‘testicle’; Lat. cf. cutio, -onis, m. *woodlouse'
kutokos, see kut- (3)
kutor-, kutno- 'strength; strong'. Cf. WP II, 601 Hitt. kutar, ds kutani (-tt-) ‘strength’; Arm. cf. ktrič ‘brave’; Li. kutrüs ‘vigorous, active’; kùtinu, -inti, v. ‘strengthen’ beside kuntu, pf. kutau, inf. kusti “recover”
kūturið ‘dawdle’ SWG haudern, id.; Li. kūturióti, id.; Latv. cf. kūtrs, adj. ‘sluggish’. Uncertainly Arm. kkrim, v. (1) wait", if for *kutur-). O-gde in Latv. kau- tra (2) ‘hesitancy’
küuo, io, eio “move, stir, sway’ (tr. & intr.). Cf. WP I, 376 and kieuuo MHG cf. hüwe, wm. ‘onset, rush"; W cf. ciw, adj. (smart, clever. Ambig.); OCS kyvajo, ati (w. instr. "move Pol. kiwać ‘wag, wave’; Cz. kyvu, kyvat ‘move, nod'; short-gde (*-u-) in OCS kvajo, kvati *wag'; Latv. küveju
=== leaf 338 ===
, et ‘frolic, fool about’; küve, f. ‘frolic’. (Variant of type *kuio in OCS kyjo, kyti ‘move, wag; swell, inflate’. Cz. kvas ‘leaven’ seems to re- present a type *kuu-oK-, see oKus). (Isophonic: Li. küviüos, küvétis "be shamed'. Cf. WP II, 548)
kuak- (kuuak-) ‘croak, quack’. Onomat. Hes. kakkázð, v. (“cackle’. With expressive doubling); cf. Gk. kakkábē (2) ‘partridge’; Cz. kvokat, kvoknout, inf. ‘cluck’; Li. kvakiu, ēti ‘croak, quack’
kuapos, à (kuuap-) ‘exhalation, vapour’. Cf. kuëp-. WP I, 379 Gk. kápos, id.; kapúo, v. ‘exhale’; Alb. (?) vapë ‘sultriness’; Umb. cf. vapu-tu ‘with in- cense’; Lat. cf. vapor, vapidus; Li. kvüpas
kut- — kuoit- (kuoitio, kuoitaio)
20
25
30
35
40
45
596
‘pungent smell, vapour; kvapüs ‘pungent’. (For the initial, cf. Go. af-hvapjan, v. ‘choke’. The evidence for IE *ku- > Lat. v- is limited to this word and a doubtful equation in-vitare: Li. kvieciü, kviésti ‘invite’. See WP I, 475)
kuat- (kuuat-, kuats-) ‘seethe, ferment’. WP I, 468 Skt. kváthàmi, tr. & intr. ‘boil’; Go. hvapjan ‘foam, seethe’; hvapo, f. ‘foam’. (Isophone: Li. kvatoti, inf. *guffaw")
(kuep- (kuuep-, kuép-) (redolent; vapour. See kuap-, kuip- Li. kvepiü, kvépti (smell', intr.); cf. kvépalai, mpl. ‘aromas’; Latv. kvepstu, kvept ‘smoke, get blackened'; kvēpi, mpl. 'soot
kuikio (kuikaio) ‘squeal, squeak, shriek’ MHG (ambig.) wihen (‘neigh’. Initial *ku- or *u-? Extn. in G wiehern, id.); OHG cf. OH wiho, wijo, wigo & wiwo “kite (bird); G Weih, e id.; Li. kvykiù, ti ‘squeak, squeal’; Blg. kvikam, id.; Latv. cf. kvicinåju, -at ‘make squeal' beside kviecu, kviekt ‘squeal’. (Ono- mat. A type *kueij- is represented by R Càj-ka ‘seagull’; Cz. Cejka ‘lapwing’, and perhaps by Ir. Mir cíim, com *wail')
kuinoros ‘whizz, whistle; whizzing, whist- ling’. Cf. WP I, 469 & Kuoin- (The initial occurs in a parallel Skt. form kvanami ‘shriek, creak, ring’). Gk. kinurós ‘whining’; OE cf. hwinan ‘whine, whizz’ be- side ON hvinr, m. ‘whizz, whirr, whistle’. (Extns. in E to whinny & G winseln. MIr. cói- nim ‘wail is ambig. Cf. Kuoin-, Kuin-)
kuip- (kuuip-) “smell, stench; stinking” Oss. (9) cf, Dig. c'ifá ‘mire’; (Br. chwés, chwéz, f. smell fr. a type *kuipsa with expres- sive initial?); E whiff Of not a LW); Cz. Cpu, inf. čpět ‘stink’; Li. kvimpu, inf. kvipti, id.
kuis (kuuis; Kuis, Kuuis) "a small insect, weevil, louse’ Av. spis, m. ‘louse’; Gk. kīs, gs kiós ‘weevil’
kuoikō (kuuoiK-) 'gawp, stare, gape’ Gk. cf. koikúllō, id.; Li. kvaištu, kvaišti, id.
kuoilis, os (?) Lat. vilis (“base?. Ambig.); Li. kvailas and kvai- lùs “silly”
kuoit- (kuoitio, kuoitaio) (?) *invite'. WP I, 475. Cf. uoit- (Lat. ambig.)
` 597
Lat. cf. in-vitare, id.; Li. kvieciü, kviésti, id.
(Isophones: OCS cvétü, Cz. květ ‘flower’; Li.
kvietys *wheat'; Latv. kvieši, mpl. id.) kuókuó (kuuokuuo) ‘shriek, squawk'
Gk. kóküo, id., cf. kotílos ‘chattering’; Cz.
kvákám, at Cchatter" Ambig. in view of ono-
mat. type kuak- as in Li. kvakiü, et *quack) khakha- “laugh, guffaw'. Onomatopoeic
type of atypical phonology
Skt. kákhami, khakkha-, id.; Arm. cf. xaxank,
s. ‘laughter’; Gk. kakházó, wd Lat. cf. ca-
Kabolis, os “a furry animal, sable’ (Scythian word?) Oss. cf. salábir, salávír, Dig. salaur ‘marten’; R sóboll ‘sable’. LWs in alleged Lat. sabellum; OFr. sable, whence E sable; Li. sábalas. (Iso- phonic with Skt. Sabálah ‘motley’. Cf. AP: ESRJa: sóbolí, p. 348)
Kad- ‘fall’. WP I, 339-340 Skt. Sad in $a$ada 3s pf., and $atsyati 3s fut., pp: śannah (fall, fly out, Semantics of *pad- and of *pet-, *pípét-, q. v.); Gk. cf. kekádonto 3pl pf. mp. ‘retreat, escape’; Lat. cado, Gre, pf: cecídi (f
```


## [2026-09-14T02:01:36.263Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(d):\n    if re.search(r'sk[uū]r[-o]', p) and 1190>0:\n        pass\nfor i in (635,636,637):\n    print('=== leaf',i,'===')\n    print(d[i][:3500])\nPY"
}
```


### [2026-09-14T02:01:37.863Z] TOOL RESULT

```
=== leaf 635 ===
. (3) ‘shame’; Dig. kämä, id. (and *pudenda?); Arm. (ambig.) xam, adj. ‘boorish’; MHG scham, adj. ‘shameful’; sf. and -e, wm. & f. ‘shame’; OE scamu, f. ‘shame; privy parts’; ON skamm-, cpds. 'shame-'; OFris. cf. skamel, OHG skamal, adj. "poor"
skam- (2) ‘baring of teeth, grin’ Ir. scamh, f. (2) ‘grimace, grin’; scamhaim, v. ‘grin’; R cf. o-skómina, f. “setting of teeth on edge. (Isophone: skomljo, skomati, v. ‘groan? OCS; Ukr. o-skoma, f. *biunting")
(skamno- ‘lightweight’. Celtic only (?). WP II, 601 Mir. scaman, id.; Ir. cf. scamhán, s. “lung, lights; OBr. scamn- ‘lightweight’; Br. skanv,
skalið — skandh-
10
20
25
30
39
40
45
1148
id. beside skan ‘swift’; W ysgafn ‘lightweight’; Cor. scaf “light; quick’)
skamp- (skampið, skampos, skampto-) ‘shorten, constrict; defective, short; lack, want’ Verbal types” Ir. scamaim, scamhaim, v. ‘drain, strip, exhaust, reduce, bare, milk dry'; ON skemma, v. ‘truncate’; Sw. fór-skümma, v. ‘ruin’ beside skämma, v. “fall ill, sicken, pine, turn bad’; mod. Icel. skemma ‘damage’; OCS skọpljọ, skọpiti, v. ‘constrain, contract’; Cz. skoupiti se, v. refl. "be miserly’. Adjectival types: ON skammr, adj. ‘short; MHG scham, adj. ‘disgraced, ashamed’; EME sham ‘coun- terfeit; pretence’; cf. also OE scom-lic, adj. “short? (for *scom- = *sceam?); OCS (and com. Slav) skopü ‘miserly’; Blg. skáp ‘dear’; (LW in) Rum. scump ‘dear’; Latv. skops ‘miserly’. . Further (type *skamptos) Ir. scamtha ‘milked dry’ beside scamhtha ‘stripped, bare); MHG schamede, schemde, schande, f. 'disgrace, shame”; OE scand, f. id. beside E scant (fr. neuter form of skammr); (MHG fr. *skam- pita). Cf. skam- (1)
skand- (skandos, à) “fall, breakdown, ruin’. (skond-? Cf. skend-, skond, skid- and WP II, 564. Alternative vocalism of types skál-: skel- and skár-: sker-, q.v. EM confused on Lat. scando; WH inconclusive) Skt. skandah, m. destruction; disease- demon’; Av. skondo, m. ‘ruin’; Arm. (ambig. *skand- or *sknd-) xanti, adj. (Cindigent'. But for xant ‘lewd’, see sknt-: Gk. skat-: G Schund, etc.); Gk. cf. skándalon, n. (fsnare; offence, disgrace’. For sense cf. G Falle ‘snare’: fallen ‘fall’. Gk. type *skndol-?); Olr. cf. scannar, scaindir, m. ‘defeat’; Ir. scannar, m. (Caffray; slander but for Olr. aor. sescaind “he jumped”, see skend-); Olr. cf. scaindrim, v. “scatter” beside Ir. scannruighim, v. (scare; scatter. E scant, adj. is of ambig. origin, cf. skam-); OCS skodü, adj. ‘puny, poor, defec- tive’; skoda, f.; Li. skandinti, tr. ‘drown, sink” Variant in Skt. skannáh, pp. “fallen”
skandh- (?) Skt. skandháh, m. “shoulder; tree-trunk; re- gion’; LG Schanne, f. ‘wold’. (Isophones: Hes. skánthes ‘bed’; Gk. skánthos "a bird”;
1149
Ir. scann “film?)
skanguos, ið (skiiguo-?) 'awry; misplace’ Gk. skambós, adj. “askew, inbent'; Icel. skekk- ja, v. ‘displace, skew’
skapet- (skapt-) ‘cut, cutting; cut-out, thing cut, shape’. Cf. skapt- Gk. skápetos, m. “ditch, trench’; OE sceafoóa, wm. ‘chip, shaving’; OCS cf. skopíci, m. "eu. nuch’. See next
skapo, ið (skap-) ‘chip, dig, scrape, Cut, Cf. skabhos (2). WP II, 560 Oss. cf. Küpi, kapi, s. “hoe, hook’, fr. *skhàp-); Gk. cf. skapáne, f. “hoe, spade’; Alb. hap, v. (- nji gropë ‘dig — a hole"); Lat. cf. scapula, f. 'shoulder-blade'; (ambiguous forms are Go. skaban, sv. 6 and Gmc. generally, see skabh-); OCS (ambig.) skopljo, skopiti, v. (&castrate', but cf. skop-); Li. skapiü, inf: skópti, v. Cgouge, scrape, cut, strip, pluck’: *á/a) cf. skaptos
skapos, ó(n) ‘stick, post, log’. WP II, 561 Hes. skápos, m. “br
=== leaf 636 ===
aped; cut, carving, gouged article, shaped article’. Cf. skapó and skabh-. (Gk. ambig. as also Gmc. See skabhos (2)). WP II, 561 Gk. (ambig.) skaptós ‘dug; diggable' (for the radical cf. skapáne, skápetos but the vb. skápto is fr. type skabh-, q. v.); OHG scaft, m. (shaft, spear, arrow'. Ambig. as Gk. cf. skabh-); MHG schaft, sm. (also: ‘bathtub’); OE sceaft, m. ‘shaft, pole’; E (also ‘tunnel in a mine"); ON skapt, n., skepti, n. as OHG (also: ‘shaft, handle, missile; Li. skáptas, m. ‘scoop, gouge, carving-knife'"
skarbos “rough, jagged'. WP II, 582. Pol. skrobac, inf. ‘shave, scrape? ambiguous; Ir scarbh, adj. “tough, hard, firm; MHG scarph, adj. ‘sharp’, and com. Gmc. Occurs as a noun scarphe, f. ‘sharpness’; OE scearp, adj. ‘sharp, severe’; ON skarpr, adj. ‘sharp, scorched, pinched, withered, barren, bitter, keen’; Latv. skarbs, adj. ‘sharp’. (R skorbnut, inf. ‘roughen, stiffen’ represents a type *skrb-.
skanguos, ið (skiüguo-?) — skars-
10
15
20
25
30
35
40
45
1150
Isophonic w. type *skarb- is R skorobit, inf. “bend, warp")
skard- ‘jump’. Cf. skerio (1) Alb. cf. hardhje, f. ‘lizard’; hardhoj, denom. ‘cast, aim"; MHG cf. scharzen, v. jump, frolic’; scharz, sm. id.; ON skarta, v. ‘swagger’; skart, n. ‘swank, finery’. (NB: a form schérzen oc- curs in MHG, with -&- accdg. to Lexer, but this is uncertain). (Isophone: Br. skarz ‘tiny; neat; pernickety")
skaris, io “small insect. Cf. skor- “jump”, etc. Gk. skarís, gs: -ídos, f. 'bellyworm, mosquito larva? (form of askarís, id.); Alb. harje, f. ‘mosquito’; Pol. dim. skorek, m. ‘earwig’
skarn- (D ‘foul; filth’. Cf. skór-, skorn-. Cf. also WP II, 587 Arm. xarn, i-st. “mixed; polluted, impure’; OE scearn, n. ‘filth, dung’; ON skarn, n.id. (The radical seems to be present also in R skor-ómnyj, (2) *'obscene")
skarn- (2) (?) ‘rough; roughness, harshness’? Arm. xat, s. ‘briar’; OLat. scarreo, Gre, v. "be rough’. (Isophone: Albanian harr, v. *weed")
(skáró, ið ‘rush, hurry, bound, jump’. See skor-. WP II, 566)
(skáro-, skário ‘cut, cutting’, etc. indicating long-gde of type sker- (2), q. v. MHG schuor, sm. & f. ‘clipping’; Du. scheur, f. ‘crack’; ON skoera 'fray?)
skarp- (skrap-) ‘rough, rugged, sharp; crack, split, splinter. (Evidence ambiguous. Cf. skars-) Br. skarr, pl. -u, m. (crack, chink’. But cf. skars-); Du. scherf, f. ‘sherd, potsherd’; scher- ven, v. ‘be shattered’; MHG scharben, v. ‘hack, pare’; Swiss scherb, scherp, adj. ‘hard, dry, brittle’; cf. Blg. Srb. xrapa, hrapa ‘roughness’; Slovene hrapa, f. ‘rough patch in leather’; Srb. hrápav, adj. ‘uneven, rough, knotty’; Blg. xrapav, Slovene hrapav, adj. trough; hoarse’; Cz. chrapěti, v. ‘be hoarse; snore beside chrápat, inf. ‘snore’; Pol. cf. chropowaty, adj. ‘tough, uneven’. Cf. also G Scharbe, f. (2) ‘sod, clod’?
skars- ‘scrape, roughen; rough, harsh’. Cf. skors-, skers- & skarp- Arm. xaf, s. ‘briar’; xarem, v. ‘wrench’; Alb.
1151
harr, herr, v. *weed'; Old Lat. scarreo, ere, v. ‘be rough'; G scharren, v. ‘scratch, root, scrab- ble, shuffle, hawk, cough'; Scharre, f. ‘rasp; raspings'; ON skarr, n. ‘skirmish’ beside skars, skass, n. ‘ogress’. (NB. A form *skors- in im- plied in Arm. xorem, v. (dig). Cf. also Norw. skarre, v. (‘burr the ‘r as in Bergen dialect) (skat- (1) jump, dash, spout'. See sKat-) skat- (2) “hit, strike, touch'. Cf. skot-. (Alb. ambig.) Alb. has, v. aor: hasa “hit, touch, meet: MIr. & Ir. scathaim, scaithim, v. “cut, lop, destroy” skaudhos (ksaudhos?) ‘miserable, poor, lean, abject'. Variants in OPer. & Arm. Ober. cf
=== leaf 637 ===
tched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudüs, adj. ‘painful, offen- sive; man skauda “it aches’; skaudZiü, inf: skaüsti, v. ‘offend’; Latv. cf. skaudrs, adj. ‘keen, painful. (Variant of uncertain phono- logy in Srb. hud ‘bad’; Cz. chudý ‘poor’, dial: Jean’, and R xudój ‘bad; ill; lean’; xudà ‘blame, abuse’, fr. *ksaudh-, *qusoudh- or sim. Cf. Oss. cawd "bad fr. a variant *sKaudh-?) skaug- Sw. skóka, f. ‘whore’; Li. skaugüs, adj. *miser- ly’; skáugis, ‘miser’; Latv. skaugis, m. ‘envious person’ but cf. skaudigs ('envious'. See above) (skaul-, see ksaul-. Thus only in W ysgawl, adj. ‘vehement, dashing’) skaupos, å ‘tuft, bunch, sheaf Lat. (dial.) scopae, fpl. ‘broom’; scopo, are, v. (sweep. WH & EM untenable); (W cf. ysgaw, Br. skað, Cor. scaw.'elder? but the semantic link is obscure); MHG schoup, gs: schoubes, sm., Du. schoof, f., OE sceaf, m., ON skauf, n. ‘sheaf, bundle’; LG Schauw, wf. “flock, swarm’; cf. ON sküfr, m. ('tuft, topknot,, fr. *sküp- or *skübh-); Big. cf. (dial.) skupü, m. “collection, heap', sküpom ('to- gether, unless from a dialect of Srb. type, *su- and *komp-. Thus Mladenov. Isophonic: OCS pro-skupü *depraver, profaner’; -sku- pístvo 'depravity')
skat- — skedhros
10
20
25
30
35
40
45
1152
skauros (skhauros) ‘limping, club-footed'. WP II, 538 Skt. khorah, adj. (‘limping’, fr. *skh-); Gk. skaüros, adj. 'acromegalous'; Lat. scaurus, adj. *club-footed'. (For Sw. skör *overripe, squa- shy', see ksaur-)
(skauth-, possible variant of type skaudh-, q.v. for OPer. skauðis: Arm. xawt)
(skau-, skauu-, ksau- "watch, care’. (Variant sKou-? q.v.). See Supt:S)
skáuios “bent, twisted, left-hand’, etc. See skaiuos. The present variant arises in Alb. i huej, i huaj, adj. ‘strange, foreign’; t&-huej, v. ('alienate', fr. *at-skaujo); EMDu. schou- wen, v. ('avoid'. NB. Du. schuwen, id. is fr. a type *skeukio: skük- in view of OHG skiu- hen, G scheuen, etc. LWs in OFr. eschiver, It. schivare, E eschew, etc.); schouw, adj. *depraved, wayward'
sked- (skhed-) ‘fling, broadcast, scatter’. WP II, 558 Gk. skedánnümi, fut: skedóo, v. id.; Alb. hedh, (N. dial. hjedh), aor. hodha, v. (Cfling', fr. *sked-: sked- aor.); cf. hedhe, f. ‘flake’; OCS *SteZdo, Stediti, v. 'expend, spare’ in Cz. Stéd- iti, id.; cf. OCS Stedrü “generous”; Cz. štědrý, Pol. szczodry, id.
skeds- “crust, shell, rock'. Cf. skhid-, sKhid- Arm. xec, Lët “shell, scale; felloe, rim’; cf. (variant) Kecem, Kecum, v. ('split, separate’, fr. *skhed-); OHG scésso, wm. ‘rock’; (iso- phonic w. Icel. skessa ‘giantess’). (NB. Per. xišt ‘brick, tile’? appears to be cognate w. Skt. ístakå & Av. istya, id. but the phonol. is ob- scure)
skedh- (skhedh-?) ‘cut, hurt’. (Phonol. am- big.). Cf. skedhros, skhidros Gk. cf. a-skethés, adj. *un-harmed'; Latv. Ske- dens “split stick’; Li. cf. skederé, f. ‘chip’; (long-gde in) Olr. scíss, Ir. scíos, f. (fatigue, if from a type *sked(h)sa)
skedhros “fine, close, narrow, thin'. WP II, 482. Cf. skhidros (skh-) Gk. skethrós, adj. (careful, exact; OHG ské&- tere, adj. ‘thin, fine; MHG scháétter, sm. “fine linen’; (LW in) Finn. ketterä ‘clever’. (The Slavonic forms represented by OCS štedrů ‘merciful, generous’ are of uncertain conso-
1153
nantism, cf. sked-)
skeg- (skheg-?) “jump, shake, fling’. (Conso- nantism ambig. cf. skKhág-, skheg- with vari- ants). Skt. cf. Chàgab, m. 'goat';? Alb. tér-hoz, v. *snatch; anger”; tér-hózem, mp. (“prance, rear, shy; rage”, fr. *tro-skegio or *-skagio?); MHG schachen, v. "road: schäch, adj. ‘predatory’; OFris. skēka,
```


## [2026-09-14T02:01:43.983Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport re\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if re.search(r'\\bsk[uūü]r', p):\n        # print page numbers found\n        print(i, re.findall(r'\\b11[0-9][0-9]\\b', p)[:4], [x for x in re.findall(r'\\bsk[uūü]r[a-zA-Z-]*', p)][:8])\nPY"
}
```


### [2026-09-14T02:01:45.397Z] TOOL RESULT

```
650 ['1176', '1177'] ['skurn']
657 ['1189', '1190'] ['skurb-', 'skurbstu', 'skurbti', 'skurbe', 'skurbs', 'skurka', 'skur-', 'skurstu']
658 ['1191', '1192'] ['skur-', 'skuro']
659 ['1193'] ['skur-', 'skur', 'skūru', 'skurti', 'skurinat', 'skur-', 'skur', 'skür-']
660 ['1194', '1195'] ['skurda', 'skurdsko']
663 [] ['skür-']
664 [] ['skür-', 'skürs-']
```


## [2026-09-14T02:01:47.592Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[659][:3500])\nPY"
}
```


### [2026-09-14T02:01:48.771Z] TOOL RESULT

```
�; ON skýla, v. ‘shelter, protect; skýli, n. (shelter, protection’; Sw. skyla, v. ‘cover’. (Isophones: Fris. skûlje (2) ‘glide’; Norw. skule, v. 'scow?'. E-gde in ON. skjól, Dan. skjul as ON. skyli. Isophone: Sw. skulor, fpi. ‘swill, dishwater’)
skundh- (1) 'vile, evil, offensive; wrong, bad'. WP II, 554 & 564. See next Per. sukunj, sukun£ ‘foul breath’; Arm. xung, s. ‘bogey’; OE scyndan, v. (3) ‘offend’; cf. scyndel, m. ‘vagabond’; Du. cf. on-ge-schon- den, pp. ‘undamaged’; OCS skodü, adj. ‘puny, poor’; skodëjo, čti, v. ‘diminish’; R po-skud- nyj, adj. ‘nasty? beside skudnyj, adj. ‘poor, scant’; Li. skundas, skundà, mf. ‘complaint, charge, retort’. SI. LW in Rum. scund, adj. tiny”
skundh- (2) “egg on, stimulate, probe, vex’. Cf. skundh- (1) & skndh- Ir. sconn-, cpds.; sconn-ach, adj. ‘hasty, rash’; OHG skuntan, wv. ‘egg on’; OE scyndan, tr. & intr. ‘hasten; incite; censure’; LG schünnen, v. ‘incite’; Li. skundZiu, skųsti, v. ‘complain’; man skunda, impers. ‘aches’; Latv. skundu, et, v. ‘grumble, murmur’. (Baltic forms equally to type (1))
skün- (?) Gk. cf. epi-skúnion, n. (“brow, beetling brow’ or sim.); Du. schuin, adj. ‘wry’
(sku-neu-, -nu- in Skt. skunómi, v. (2) ‘cover’, cf. skuio, etc.)
skupros (skubhros?) ‘mass, pile’ Oss. Kubár, s. ‘clump, cluster’ beside Kubir, s. ‘bud; hillock’; MHG. schober m. ‘pile’; Jong ode in ON skúfr, m. ‘tassel; Latv. cf. skupsna, f. “bush, tuft; copse’
skur- (skurð, ið ) (1) ‘lacerate, chafe, fray, scratch, scrape’. Cf. skər- (skăr-) Ir. scoraim, v. id.; ON skora, v. ‘chafe, score’; (LW in E to score); Li. skūru, skurti, v. ‘fray,
1193
get tattered'; Latv. cf. skurinat, inf. (2) ‘tousle’. Cf. also Ir. scor, m. ‘gash; mark’; W ysgor, f. ‘ampart’; MHG schor, m.
skur- (skurð, io) (2) ‘thrust, poke Arm. rem. v. tr. id.; MHG schurn, schorn, v. ‘poke; jolt beside OHG scurigen, MHG schürgen, v. id. (and “incite'); OE scorian, v. (2) jut’; Du. schoren, v. “prop up, shore up’; schoor, m. "prop, stay, strut'; ON skora, v. (2) ‘urge, challenge’ beside skor-óa, f. ‘stay, prop’; Cz. cf. skeřit zuby, v. ‘bare the teeth’; skeřit se ‘grin’
skür- (3) ‘rock, stone’. Cf. skur- (1) and (2). Ir. ambig. cf. skoros (1) & (2) Arm. cf. xrem, v. (2) ‘strand; run aground’; cf. xrut, s. ‘shoal, bar’; Gk. sküron, n. ‘stone chip’; Ir. (ambig.) scor, m. (‘reef, scar’. Cf. skor-); MHG schor, sm. ‘scar, crag, cliff; Du. schor, f. ‘sandbank, shore’; ME. shor(e), id.; OCS skra, f. ‘sod’
(skür- (4). See Supt: S)
skür- ‘cover, shell”. Cf. skuu. WP II, 548 Per. suküre, s. ‘earthen dish’; Lat. cf. ob-scü- rus, adj. ‘dark’; OHG skūra, f. ‘barn’; MHG schūr, sm. ‘shelter, protection’; Du. schuur, f., LG schür, n. id.; ON skúr, s. ‘penthouse; shell”; Li. dial, skūrà, f. “fur, pelt’. Cf. also Arm. xr-tin, adj. cpd. ‘dark, obscure’. Mod. G Scheuer, mfn. represents a type *sküuor-, see skuu- ‘cover’, but dial. Schauer occurs. (The epithetic Dio-skūroi ‘Castor and Pollux’ seems to contain the isophone *skūr- in Eng. shower: G Regen-schauer or indeed G Schauer ‘shudder’. Omitted. fr. FK: EWDS. Isophone: ON skýra, v. ‘explain’: skyrr, adj. ‘clear, bright, clever’)
skurb-, possible variant of type skrb-, q.v. Cf. also Li. skrubùs, adj. ‘thrifty; stingy’. WP II, 582
skurd- ‘lack, suffer’. Cf. WP II, 579 & 590 Du. schorten, v. ‘be ailing; lack’; ON skorta, Norw. skorte, v. id.; cf. also OHG scurz, MHG schurz, OE scort, adj. ‘short’; OFris. skorte, f. ‘detriment’; ON skortr, m. ‘scarcity’; cf. skort + gen. ‘short of . . ^; Li. skurdas, m. ‘want, poverty’
```


## [2026-09-14T02:02:05.722Z] TOOL CALL #52: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:02:05.730Z] TOOL RESULT

```


```


## [2026-09-14T02:02:08.370Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sneeze",
 "prompt": "Full etymology of \"sneeze\": Old English fneosan, the fnese > snese misreading story, PIE root, related forms."
}
```


## [2026-09-14T02:02:09.335Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pneumonia",
 "prompt": "Etymology of pneumonia and pneumatic: which Greek words (pneumon vs pneuma) and which PIE roots."
}
```


### [2026-09-14T02:02:14.142Z] TOOL RESULT

```
# Etymology: Pneumonia vs. Pneumatic

**Pneumonia** derives from Greek *pneumōn* meaning "lung," specifically referring to "inflammation of the lungs" (c. 1600).

**Pneumatic** would derive from Greek *pneuma* (related to *pneín* "to breathe"), which is the broader concept of air or breath.

## Shared PIE Root

Both trace back to the Proto-Indo-European root **\*pleu-** meaning "to flow." According to the source, *pneumōn* was "altered (probably by influence of *pnein* 'to breathe') from *pleumōn*," with the word literally meaning "floater"—referencing how lungs float when placed in water, unlike heavier organs.

The connection to *pleu-* explains related English words like "float," "flow," and "fleet," all sharing this ancient Indo-European concept of movement through space or medium.
```


### [2026-09-14T02:02:14.409Z] TOOL RESULT

```
# Etymology of Sneeze

The word "sneeze" has fascinating linguistic roots. The verb form originated in the late 15c. from the Old English term *fneosan*, meaning "to snort" or "sneeze."

## Sound Evolution

A key transformation occurred when the uncommon digraph *fn-* was misread as *sn-*. The OED notes that the shift wasn't direct; instead, "sneeze" represents a "strengthened form" of the earlier *nese*, which had emerged as *fnese* declined by the early 15c.

## Imitative Origins

The word belongs to a family of onomatopoetic terms. It traces back to Proto-Germanic *\*fneu-s-* and ultimately to PIE *\*pneu-*, both meaning "to breathe" and reflecting the sound itself. Similar imitative words exist across languages, including Latin *sternuere*, German *niesen*, and Russian *čichat'*.

## Related Meanings

An interesting figurative use developed: "to sneeze at" (from 1806) means "show contempt for, regard as of little value." Additionally, an old phrase "to teach how the cat sneezes" referred to domination or bullying.

The noun form arrived later, appearing around 1640s to describe the physical act and accompanying sound.
```


## [2026-09-14T02:02:20.230Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%AF",
 "prompt": "Persian خود: is there an entry for خود meaning \"helmet\" (xud/xōd)? Give its etymology (Middle Persian, Old Persian xauda-, Avestan xaoδa-, Proto-Iranian) and also the separate entry for خود \"self\". Quote the etymology sections."
}
```


## [2026-09-14T02:02:22.096Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B3",
 "prompt": "Persian کس: list all etymologies given, especially کس meaning \"vulva/cunt\" — its etymology (Proto-Iranian, Avestan kusra-, PIE root), and کس \"person\". Quote the etymology sections verbatim."
}
```


### [2026-09-14T02:02:26.165Z] TOOL RESULT

```
# خود (xud/xōd) - Helmet Entry

Yes, the Wiktionary page contains a separate entry for خود meaning "helmet" under **Etymology 2**.

## Helmet Etymology

The etymology section states:

> "From Middle Persian xwd (xōd, 'helm'), borrowed from Parthian xwwd (*xōδ, 'helmet'), from Old Iranian, ultimately from Proto-Indo-European *kadʰ- ('to guard, cover, care for, protect')."

The entry further notes cognates including:

> "Old Persian 𐎧𐎢𐎭𐎠 (xaudā-, 'hat'), Avestan 𐬑𐬀𐬊𐬜𐬀 (xaoδa, 'helmet')"

## Self/Reflexive Pronoun Entry

A distinct entry appears under **Etymology 1** for خود meaning "self":

> "From Middle Persian BNPŠE, 𐭡𐭭𐭯𐭱𐭤 (xwad), from Old Persian *hvatah"

This reflexive pronoun sense is unrelated linguistically to the helmet meaning, representing two separate etymological paths that converged on the same Persian word form.
```


### [2026-09-14T02:02:28.823Z] TOOL RESULT

```
# Persian Etymologies for کس

## Etymology 1: "Person"

The entry states: "Inherited from Middle Persian _AYŠ_ (kas, 'person, somebody')., from kas-čid. Compare چیز (čiz) from čis-čid."

This semantic sense derives from Middle Persian, tracing back through historical Persian language development.

## Etymology 2: "Vulva/Cunt"

The documented etymology reads: "Inherited from Proto-Indo-European _*kuḱis_ ('(female) pubic hair; vulva'). Cognate with Northern Kurdish _quz_ ('vagina, vulva, cunt, pussy'), Hawrami (kʷsî, 'vulva'), Lithuanian _kūšỹs_ ('pubic hair, vulva') and Latvian _kūsis_ ('pubic hair, vulva')."

The entry notes this "Possibly a euphemism from the older meaning 'belly', preserved in Sanskrit _कुक्षि_ (kukṣí, 'belly'), in Sogdian _qwšy_ ('side (e.g. of the body)') and in Persian _کشتی_ (kuštī, 'girdle')."

The word spread to descendant languages including Arabic, Hebrew, Khalaj, and Urdu through Persian transmission.
```


## [2026-09-14T02:02:50.358Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kadh ===\"; grep -o \"kadh-\\. To shelter[^\\[]*\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -2\necho \"=== BRT kusra ===\"; grep -n \"kusra\" BRT.txt | head\necho \"=== POK kusra context already seen ===\""
}
```


### [2026-09-14T02:02:50.455Z] TOOL RESULT

```
=== AHD kadh ===
=== BRT kusra ===
9678:475                        kusra-                          —  gae9ä-  i                     476
9679:•  j,  kusra-  Adj,   'sich   wölbend,   hohl':  loS;  —  i'  tacil  aitahe  aiwyästB  *ralufris 'räoa  iusrS.patäba  (sd.)  Y.  10. 11.  "wenn  man  mit  diesem  —  beliebig  guten  —
23908:•  j.  vad^vö.dä-  Adj.  Ileerden  schenkend': mi^rym  ..  yS  'd,'r  '^1.10.6$.  •    J-    vi-kusra-    Adj.    'sich    auseinander
29343:•  j.  han-kusra-  Adj.  'sich  zusammen wölbend,  eng  zusammenschliessend':  ätn.- vasamm  (sd.)  . .  vlhtsrvm  e&arät  naimäl •r?tn  uparat  narntät  Y.i4j.
=== POK kusra context already seen ===
```


## [2026-09-14T02:02:58.240Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"kadh-[^.]\\{0,40\\}\" AHD_watkins1985.txt | head -5; echo ---; grep -o \"kadh-\\..\\{0,900\\}\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-14T02:02:59.365Z] TOOL RESULT

```
kadh-
kadh- 516
kadh- HATCHET skep- HATE kad- HATRED ar-, kad
kadh-
kadh-
---
kadh-. To shelter, cover. 1. Suffixed zero-grade form *kod-u- in Germanic *haduz in expressive form *hattuz in Old English Azxt(t), hat: HAT. 2. Basic form *kddh- in: a. Germanic *hdéda in Old English hdd, hood: HoopD!;
```


## [2026-09-14T02:03:01.498Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"kadh-\\. To shelter.\\{0,1200\\}\" AHD_watkins1985.txt | head -1"
}
```


### [2026-09-14T02:03:02.587Z] TOOL RESULT

```
kadh-. To shelter, cover. 1. Suffixed zero-grade form *kod-u- in Germanic *haduz in expressive form *hattuz in Old English Azxt(t), hat: HAT. 2. Basic form *kddh- in: a. Germanic *hdéda in Old English hdd, hood: HoopD!;
```


## [2026-09-14T02:03:07.373Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Root / lemma: kadh-\" POK_full.txt; awk '/Root \\/ lemma: kadh-/,/Page\\(s\\): 51[0-9]/' POK_full.txt | head -40"
}
```


### [2026-09-14T02:03:08.516Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:03:10.732Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 516\" POK_full.txt; grep -n \"kadh\" POK_full.txt | head"
}
```


### [2026-09-14T02:03:10.803Z] TOOL RESULT

```
49304:Page(s): 516-517
```


## [2026-09-14T02:03:12.672Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '49280,49306p' POK_full.txt"
}
```


### [2026-09-14T02:03:12.739Z] TOOL RESULT

```
Root / lemma: Rad-2 

Meaning: to shine, to flaunt 

Material: Old Indie Perf. sasaduh, participle sasadana-^ s\c\\ auszeiehnen, jut, project, 

protrude, stick out '; 

gr. Perf. K£Kaa|jai, Plusqpf. £K£Kaapr|v, participle KEKaapsvoc; (Hom. Aisch.) " honor, 
grant ', K£Ka5|j£V0(; (Pind.) " prangend ', Kaarajp actually " the shining ' (?), Kaari-avsipa " 
excellent among men ', etc.; in addition Kaarajp m. "beaver' with transference of GN 
because of the healing effect of the castor: Kaaropiov (> Old Indie kastuni. " musk '); 
present Kaivupai seems neologism after Saivuijai; 

perhaps Middle Irish ca(i)d^\\o\y\ wherefore gall, caddos^ consecrated, established as 
inviolable, sacred, inviolable ' C. Gl. L. V 493, 30; 

abrit. Be/atu-cadrus ep\t\r\et of " god of war '?? reshuffling a *katros 's/aWanV (compare 
Aa/- "fight') to kadros\Nou\6 be certainly excluded totally. 



References: WP. I 340. 
Page(s): 516-517 

Root / lemma: Rak-
```


## [2026-09-14T02:03:17.221Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '49240,49282p' POK_full.txt"
}
```


### [2026-09-14T02:03:17.281Z] TOOL RESULT

```
Latin canicae ' bran '; 

Old Icelandic hunang. Old Swedish hunaghu.. Old English hunig. Old Saxon honig. Old 
High German honag, honang^houey' (named after the color; basic form probably 
Germanic *hunaga-, from which Finnish hunaja; partially before ^appearing /? based on 
nasalization of the vowel through the preceding /7and supporting influence of Germanic 
suffixes -ung-, -ing-)\ 

Old Prussian c^ca/7 'brown' (I. cucan, i.e. cuncarr, u\s Baltic development from reduced 
vowel in disyllabic base); 



about Old Indie kanaka-v\. "gold' s. Kuiper, Proto-Munda 30 f.; 

gall, caneco-sed/on bare\y as ' golden seat' here, also not to Middle Irish canach' 
marsh grass ' (: cymr. pan 6s.)] 

References: WP. I 400, Vendryes RC 47, 200 f., H. Lewis Et. Celt. 1, 320 f. 
Page(s): 564-565 

Root / lemma: Racf-I 

Meaning: to fall 

Material: Old Indie sacf-, Perf. sasada. Put. satsyati^ drop off, fall down, fall out' (: Latin 

cadd); 

Armenian cacnum ( *RadJo-) 'fall, get low '; 

Latin cadd, -ere "fall' (Oscan antkadunrR s. WH. I 128); cadaver v\. " corpse ' as "the 
fallen ' {*kada-ues)\ caducus^ fragile '; 

Old Irish casart "hail; lightning' {* kad-t-ara), PI. cymr. cesair^ihe finished ', corn, keser, 
bret. kazerc'h^haiW 

References: WP. I 339 f., WH. I 127 f. 
Page(s):516 

Root / lemma: Rad-2
```


## [2026-09-14T02:03:25.800Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86",
 "prompt": "Persian کوچ: give all etymologies (migration/nomadic move; also any sense \"household/family/tribe\"). Is it from Turkic köç or from Iranian? Quote the etymology sections."
}
```


## [2026-09-14T02:03:27.109Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/cutis",
 "prompt": "Latin cutis: etymology, PIE root, cognates (Greek kutos, Germanic *hūdiz). Quote the etymology section."
}
```


### [2026-09-14T02:03:32.224Z] TOOL RESULT

```
# Persian کوچ Etymology

The word has **two distinct etymologies**:

## Etymology 1: Migration/Nomadic Movement

**Source:** "Borrowed from Turkic, from Proto-Turkic *köč- ('nomadizing'). Compare Chagatai كوچ (köç), Azerbaijani köç, Turkish göç."

This sense means "migration (originally of nomadic tribes, now generally)" and appears in historical Persian texts, including Rumi's work from circa 1260.

## Etymology 2: Service/Power

**Source:** "Borrowed from Khorezmian Turkic كوچ (küç, 'force, power, work'), from Proto-Common Turkic *kǖč ('force')."

This obsolete sense refers to "service, power offered," typically occurring in the phrase کوچ دادن (what a vassal performs).

## Secondary Archaic Sense

Etymology 1 also historically encompassed "chattel" (household belongings), with extensions meaning "family" or "wife"—reflecting nomadic domestic structures.

**Conclusion:** Both etymologies trace to **Turkic sources**, not Iranian origins, though the word was well-established in Persian by the medieval period.
```


### [2026-09-14T02:03:32.285Z] TOOL RESULT

```
# Etymology of Latin *cutis*

According to the Wiktionary entry, Latin *cutis* originates from Proto-Italic *\*kutis*, which derives from Proto-Indo-European *\*kuH-t-*, described as the "zero-grade form of *\*(s)kewH-* ('to cover') without s-mobile."

The entry identifies several cognates across Indo-European languages:

- **Greek**: σκύλος (skúlos, "hide")
- **Germanic**: Old English *hȳd* (modern English "hide")
- **Baltic**: Lithuanian *kutỹs* ("purse")
- **Sanskrit**: स्कुनाति (skunā́ti, "to cover")

The word is also related to Latin *culus* and shares etymological connections with Germanic *Haut* (skin) and *Hoden* (scrotum), as well as Old English *scēo* (sky), reflecting the ancient root meaning "to cover."
```


## [2026-09-14T02:03:40.402Z] TOOL CALL #66: Bash

```json
{
 "command": "pdftoppm -f 455 -l 455 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$PWD/data/verification/sources/refs/ocr/BOOK/455\" && ls -la data/verification/sources/refs/ocr/BOOK/455.png"
}
```


### [2026-09-14T02:03:42.231Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82567 Sep 13 22:03 data/verification/sources/refs/ocr/BOOK/455.png
```


## [2026-09-14T02:03:44.314Z] TOOL CALL #67: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/455.png"
}
```


### [2026-09-14T02:03:44.902Z] TOOL RESULT

```

```


## [2026-09-14T02:03:44.895Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:04:03.634Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\ni=1102-542\nfor j in (i-1,i,i+1):\n    t=clean(d[j])\n    print('=== leaf',j,'header:',t.strip().split('\\n')[0][:110])\nt=clean(d[i]); print(t[:2600])\nPY"
}
```


### [2026-09-14T02:04:04.791Z] TOOL RESULT

```
=== leaf 559 header: ۷4۰ات
=== leaf 560 header: هه اس                                                                                                ستاله
=== leaf 561 header: نز شا او
هه اس                                                                                                ستاله


گفتن   لمیدحکوبی  دعا وثنا وشکر لسمت و                ستائه  = ۱بر وزن فاله "بمعنی آستاله
                   وستودن وآفرین باشد .                                دن باشد.   کینکفش
                                                                                       است که جا
ستایشگاه  -شربطه و مخلص شمر را                        دماوند ؛     ستاو ند = بفتح اول بورزن
کوبند بمنی بیتی که فصبده باقطعه بامثنوی               رواق و بالا خانه باشد که بیش آن مانند ابوان
                              بدان تمام شود ٩ *.        نزد
                                                           ما ی
                                                              هروکر ک
                                                                    کوده بود و-صفهٌ بلندی بز

ستیر  ۲ه بکر اول » بروزن و معنی                      ص-فوهای رکانهتمهاند که سقف آنرا بيك
سطبر است که کنده و لك ويك و غلبظ باشد ؛               سبتروانفراشته باشند  ۴؛ و باضوملیز آمده
                                                                                                     است .
                وسطبر با طای حطی معرب آنست .
 ستبر نای - ۸بانون بکاشلیفدهبتحتانی                   ستأوه  -بفتح اول جروزن کجاوه.بمعنی
                                                      مکر و فریب و حیله و خدعه باشد # ۴ویکسر
زده ,کند کی و سطبری و غلیظی و لك و یکی                                                   اول همگفتهاند ۰
ربکزی چیزی را کویند وآ ارابعربی خضمه و
                               خوانند .                بکر اول بروزن سياه  ۰مخففستأه ب
                                                      ستاره باشد کهبعریی کو کب کوبند  - ۴وبمعنی
 ستخر * -بکر اولوفتح ثانیوسکون
 تفای اقطفوار بوروای ب فة محف اس                      تقره وسم قلبوناسره هم مده است-ونام پردهای
                                                                                   ازموسیتقی .       حم هت
 است که تالاب و یگنر باشد _ و نام قلعهایست
مشهور در فاری که جمشید ساخته است وچونحر               ستایش * = بکر اول بروزنفزایش,
                                                                  وك :آستانه  4آستان ۰           ۱

        بایوان چه بری رلج ویکاخ وبتاوند ؟!              _ ۴جهان جای بقا نیست باسانی بگذار
   طانمرءری« .لغت فرس ۹٩؟.
                                      انگیزد از برای توهردم ستاوهای  .بنقل رشیدی .              2
  « - ۴مولف چهانگیری لفظ مکذور را مخفف ستاره هم خبطکرده واین شعر ابوالفرج
                                                                             آوزده :    رولی را هم شاهد

           ۰    بگفتار اوسیپر وستاه
```


## [2026-09-14T02:04:10.983Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata,re\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nfor f in ('BQT_v2_pages.txt',):\n    d=open(f,encoding='utf-8').read().split('\\f')\n    for i,p in enumerate(d):\n        t=clean(p)\n        if 'شنوشه' in t or 'شنوسه' in t or 'اشنوسه' in t:\n            print(f,'leaf',i,'header:',t.strip().split('\\n')[0][:90])\nPY"
}
```


### [2026-09-14T02:04:12.886Z] TOOL RESULT

```
BQT_v2_pages.txt leaf 564 header: ==
```


## [2026-09-14T02:04:15.732Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nt=clean(d[564])\nprint(t[:3000])\nPY"
}
```


### [2026-09-14T02:04:16.953Z] TOOL RESULT

```
 ==                                                                                              سوه

وزن کبوتر » هوابی باشد با صدا که بیاختیار از     یمعثی وصف نمودن وستایش کردن باشد؛ وبضم
        راه دمام بجپد وآارا معربی عطه خواند.

ستوسه  = ۴بفتح اول و سین بی لقطه                   رزن
                                                     بو        اول         ستو ده  ۱ه یکر
 بورزن دبوسه ؛ بمعنی ستوسر است که عطسه            باشد سنتی          شنه   کرده    قروده » سمعنئی مدح
                                     باشد ۷#.
                                                 او را     یکریی      و    کنند   مدح   کسی که اورا

 ستو نه د بکر اول و فتح نون بروزن                                                            .   ْف
انداز   و   و ری   کردن شاهدن   چمگونه  ,حمله
                                                  خم ول بروزن حور » هر                  ستور ؟
 لمودن باز و باشه و امثال آن باشدبجانب باولی»
                                                  جاور چارپابیرا ۳عموماً واسب و استروخر
و باولی جانوری راگوبند که بعضی ازپروبال او
 پدیرش باز شواهین نو رسالیده
                           کنده باشند و
و نازه مشکار درا ورده سردهند îl بآٌسالی بگیرد     ستوردن = بکر اول بمعنی ستردن
  -بمعنی کریز و کریختنهم آمده استوبمربی
                                        و         است که تراشبدن وحك لمودن وباك کردنباشد؛
         اس                رب                                                     اول هما مده است     وم


ْم اول بروزن گروه «ممعنی      ستوه °


                                                      اسزتو«دن».             ول
                                                                               ف اعسم
                                                                                    م-٩
   ساسکرت        - ۳پهلوی( 605 ۲اسب) اوستا« 83۲0815--بارتولمه ۱6 ۰۹۵لجر گ۸۰۲
    ( 01711201)5-بار اسب .بار ورزاو) » استی ( 316۳005حیوان خانگی)» کردیزازا ع.۲۵158شغنی
    , ۲سریکلی 8 ۲0148و( ۲041حیوان بارکش » ورزار یالغ) » بفتوبی  ۲0/۱5گ(وسفند »
    ججانور ,چلریا » دواب)«هوشمان*۷ ۲؟.       فی :افغالی ۲
                                                        حیوان خانگی عموما) «اسشقق ٩۲ ۰ ۷٩
    کث :مقدمهص نودودو = .اشنیجه = شهمیرزادی asînhso        )...ر      - ۴محف سلوسه» E
   [رك :اعنوشه].درلهج توش[ باکداشانچنانکه آ قایرضاتابش نوشته ند:هاشنشه» بمعنیعطهمتعملاست
    نگلو-اکسن    وااسهمراابصنکولتمهاست.قس:ا لگلیسی .828808انگلیسی میانه5 06560و 1165604۰
    gfnêsanر « 02906۵0۲لغت بینالمللی جدید وبسترسال ٤۲۹۱٩  .امادربارتمصراعرود کی(چنان
    چون دردمندان را شنوشه» دراینجا همبمعنی عطسه امت چه درطب قدیم در امراض دماغی عطسه
      - ۴پهلوی 28005                 ژدن رابرای تداوی امراش دماغی و زکام مفید مدانتند .
   بیزور) . ( ۷ 2 0 5 ی و ل ه پ - ®      ممحنی قله درخت است ی تاوادیا  9۹۰ور کف 3 :
   پازید  . 210005ایرای باستان  6 ۹۱ -۲۵۷۵-از۷ها ( نوانستن » فادر بودن ) » ستوه فارسی
   مر کب امت از  2 82۳12۷20-۹۱ :قی :کوناه ( ه.م ( ).آنکه زورش کم است) . رکه :
            ور کے  :استوه ٠ ضدآن  :دتوه (خستگی ایذیر) مخفف آن «سته» («.م.).               تبرکه ۸
```


## [2026-09-14T02:04:31.240Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata,re\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(558,570):\n    t=clean(d[i]).strip().split('\\n')[0]\n    print(i,'|',t[:120])\nPY"
}
```


### [2026-09-14T02:04:32.425Z] TOOL RESULT

```
558 | ۱۰۵۹                                                                                                                    
559 | ۷4۰ات
560 | هه اس                                                                                                ستاله
561 | نز شا او
562 | ۵ات       4
563 | =
564 | ==                                                                                              سوه
565 | î     ۱ ۵۳
566 | ۷   4                                                                                                  سنیز
567 | سجلاط                                                                                       ==
568 | —       ۵                                                                           نجن
569 | ¬ ۱      وه
```


## [2026-09-14T02:04:39.431Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in list(range(0,8))+list(range(676,684)):\n    t=clean(d[i]).strip().split('\\n')[0]\n    print(i,'|',t[:120])\nPY"
}
```


### [2026-09-14T02:04:40.618Z] TOOL RESULT

```
0 | 
1 | 7
2 | م و
3 | ar
4 | و              فك اا  .بخشاول (منطق)                            ۰ای
5 | . ۱فيه ما فيه  .مولوی بلخی رومی  ۰مسحح بدیم الزمانفروزانفر .از
6 | مأخن بزبانهای اروپایی-۲
7 | 46- Minorsky              (V.),      Géographes et voyageurs musul-
676 | ه
677 | سینه کردن                                                                                                صما =
678 | ۷۲۸                                                                                                  سنه گشادن
679 | ه
680 | وفاجر و کنه کار وید کاره ونامه صاه باشد ۰       را ګوبند که سودا   کی    سیه هقز »
681 | 
682 | Mohammad Hosayn ebn ~e Khalaf
683 |
```


## [2026-09-14T02:04:51.837Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata,re\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in range(500,620):\n    t=clean(d[i]).strip().split('\\n')[0]\n    m=re.findall(r'[۰-۹]{3,4}',t)\n    if m: print(i,m, t[:60].replace('\\n',' '))\nPY"
}
```


### [2026-09-14T02:04:53.176Z] TOOL RESULT

```
553 ['۰۹۱'] سپوز کار                                                    
555 ['۱۱۳'] سییفهداز                                                    
558 ['۱۰۵۹'] ۱۰۵۹                                                        
575 ['۳۱۱'] ۳۱۱ات
577 ['۱۱۱'] ۱۱۱     6--
579 ['۱۱۷'] ۱۱۷
580 ['۱۱۱'] ۱۱۱                                                         
585 ['۷۷۴'] ٩۷۷۴
587 ['۷۱۲'] ۷۱۲6-
588 ['۷۱۷'] ۷۱۷ ۷۹
594 ['۳۱۱'] ۰؟(-۳۱۱                               o    «.               
598 ['۱۳۹'] -۱ ۱۳۹
600 ['۱۱۳'] ۱۱۳
601 ['۱۳۹'] ۱۳۹
613 ['۷۱۷'] ۷۱۷ 6-
```


## [2026-09-14T02:05:11.522Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport json,unicodedata\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\npdf=m.get('1304'); print('pdf',pdf)\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nfor p in d:\n    if '[pdf page %d]'%pdf in p[:60]:\n        print(clean(p)[:2600]); break\nPY"
}
```


### [2026-09-14T02:05:12.749Z] TOOL RESULT

```
pdf 95
[pdf page 95]
هنوشه

شنوشه ۱ © بفتح اول وئالیبوا رکشیده
و شین شطهدار حفتوح « lyn باشد که از راه
دماغ بجلدی ونئدی op plat اختیار برآبدرآترا
پعربی عطسه کوبند ۰ و بکسر اول حم کفتهاند
وبا سین بقطه (۱) gt درست است چهدرفارسی
سین وشن بپم تبدیل مییابند .
شنو لقن ۲ ه با تای ets بروزن
سیوشکن ۰ بلفت زندوپازند (۳) بمعنی  لوشتن
باشد و شئولمی st لوسم و شنولید عنی
بنوسید .*
Mea = بنتح اول وئالیبی نشدید مجمیع
آواز ها را گوبند ءموماً همچو صریر قلم ۴ -
و آوازنفیر و بای وسورنای - وآواز سبعوبهايم
و وحوش و طیور و مانند آن ۴ - و het اسب
را نیز کفتهادد خسوصآوآنرا بعربی صهیلخوانند
- و بمعنی چارشاخ دهقادان هم آمده است»,وآن
آلتی باشد dents ule دست و دستهایبیز دارد
که OL غلهة کوفتهشده را oly دهند نا ازکاهجدا
۰ (۱) چك :- بی نقطه .
de (t) :

عشحه +

۱ سح سوسه (pn) < اشتوسه (هم) .
مولف خلط کرده است !

. ۵۰۷ باروچا : Ay. col
Jie کلك اوبخندد tas, زگربه - ۴

. چك: با تا (x)

ماس

شود - و پمعتی فرین وللشت هم حست 6٩ - وبا
تشدید تالی Ret اسب را گوبند.

شنی = بنتح اول بروزن دلی * گیاهی
باشد که از پوست OT رسمان سازند - وبمعنی
سینی هم کفته al وآن خوالی باشد که از طلا
وقره و مس و امثال OT سازند.

شنیدن 1 ه بفتح اول بروژن رسیدن »
معروف است و بعربی سماع گویند - و بمعنی
بوبیدن و بوی کردن لیز گفته الد ۷ - و بععنی
هجوم لمودن - و جمعیت کردن هم آمدهاست.

شنیز = بنتح اول بر وزن gel » چوب
آپنوی را کویند - و کمان pb اندازیرا ببز
کفته اند - و بضم اول مشفف شولیز است که
سیاه دانه باشد ۸ .

شنیژه = بنتح اول و زای فارسیبروزن
ame (4) » رسمانی باشد که از پهنای کار
جولاهگان زباد آید و LT نبافند و بانگشت
پیچیده در کناری گذارند .

(۳) چك : ژند ویاژلد .
۴ - هزوارش نوشتن ,2111000180

ز خندة مه منجوق او بگرید جان .
مختاری غزاوی. افره ery نظام».

۴ - طبری sherna » مازندرالی کنوتی 52606 دواژه نامه ۲4۷4

دزآ گهی که Aten درون سیبده دمان

ie رگ ۵

ز بیم شنة او شیر بقکند چنگال .
Chante رمذی. «لفت فری 4۷۲.

شنودن < اشنودن (pe) » پهاوی 25۳1018۳ , یازند

oxshnavamiy اشنودن) « ازپارسیباستان : sly) xshnddan . (;,:+) shnavesho
(yan) beshndstan «هوبشمان-اسشق ۷۹۵ طبری Sanagh بلوچی xshnd ازرمشة
«راژءبامه6۱۲۰, کیلکی0(1:00۵۷25)2۳), beshnossen,bashniissan,y مازندرانی کنو
. 4٩۲۰ سخن سال دوم شمارء ۸ ص Alene « shonidan تا جیکی

مرغ آزپس OW خوردن او ریزه نچیدی.

> کلتان ۱۰۹ ۰.

Gas طمامش sy بجز on - ۲

۸ - رگ : شولبر .
* شنودی - بنم اول و درم gids چهارم » Cem) Gage اشنودن po)
```


## [2026-09-14T02:05:24.285Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B2%D9%87/",
 "prompt": "Give the \"فرهنگ معین\" (Mo'in) and \"لغت‌نامه دهخدا\" entries for کازه, including any etymology/origin tag and definitions. Quote in Persian."
}
```


## [2026-09-14T02:05:28.682Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== ARY latin index ==\"; grep -n -i \"skeu\\|kutos\\|xauda\\|kusra\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"== ARY persian ==\"; python3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('incoming/ARY/ARY_pages.txt',encoding='utf-8').read().split('\\f')\nprint('leaves',len(d))\nfor i,p in enumerate(d):\n    t=clean(p)\n    for w in ('کازه','سکوره','شنوسه','کلاهخود'):\n        if w in t: print(w,'leaf',i, t.strip().split('\\n')[0][:80])\nPY"
}
```


### [2026-09-14T02:05:30.503Z] TOOL RESULT

```
# کازه - معانی از منابع فارسی

## لغت‌نامه دهخدا
**تلفظ:** (زَ / زِ)

تعریف‌های اصلی شامل: "نشستگاهی که پالیزبانان از چوب و گیاه سازند" و "خانه خرگاهی که از چوب و نی و علف سازند." معانی مترادف عبارت‌اند از: سایه‌گاه، سایبان، کومه، کوخ، و صومعه.

## فرهنگ معین
**تلفظ:** (زِ) (اِ.)

سه تعریف اساسی ارائه می‌شود:
1. "آلاچیق، کلبه"
2. "صومعه"
3. "خانه و منزل"

هر دو منبع بر کاربرد این واژه برای ساختمان‌های موقتی و پناهگاه‌هایی در طبیعت تأکید دارند.
```


### [2026-09-14T02:05:31.884Z] TOOL RESULT

```
== ARY latin index ==
10158:ala SKEU- | KSEUs gly! y stn Gat, aly jt) Cai cal lan jly BUCK ~¥
== ARY persian ==
leaves 545
شنوسه leaf 89 [pdf page 90]
شنوسه leaf 348 [pdf page 349]
```


## [2026-09-14T02:05:37.318Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('incoming/ARY/ARY_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (89,348):\n    t=clean(d[i])\n    idx=t.find('شنوسه')\n    print('=== leaf',i,'===')\n    print(t[max(0,idx-1200):idx+900])\nPY"
}
```


### [2026-09-14T02:05:38.568Z] TOOL RESULT

```
=== leaf 89 ===
[pdf page 90]
تج

اشنوسه» شنوسه اشنوسیدن / ٩۹۱

لکیس سرواژی ار سر 968
پهلوی (۸(71471): با نان روسی (/785142): 1
سانسکریت (۴۳817871,:)54۸88/7 ,14817۳۸ چکه (250): ۹
لازنا صربی (58881۸۸): 1
ایسلند یکین (۷010۸۸ی5 صام): برهمی (/لف80/78(1): وا نی ها
۸ ا 11086 اسلوا کی (51].0740): ۷۲۸7
نورس کهن (ظ۸۵7۶ 00): نی نان لینرانی (۸اللا تلم ,87121۸1071
آلمانی کهن (0880/۸ لوالا 2ام): اترا رن
[ نا 110۸ لنونی (لتی) (7۲7/7ها): (7آه58
آلمانی (/(08): نود ند الا 7 ,تا [نآه 511

انگلیسی کهن (#لولساه 8 صا0):

8 ش130۸ پسگشتها 5 ۱
انگلیسی (8(/0188): (زدنن زا
دانمارکی (0۸/[3): نان 6 (85۱8825) 0
سوئدی (8752157): 85۸ 1 (3ظ6۳8) :02
نروژی (7077801۸۷): دنه دا 8 :۸۸215
هلندی ([01776): ۳ 23 8۸
اسلاری کهن (76ما؟ تال صا0): 4 (88875) :0/105

۰ 105۸ 6 (585578) 5
لهستانی (۳0./53). ۴1۸۴ برهان قاطع : ۱۴۱

و بر
۰ 1
بادداشت. 9
۱- 8۸881۸87 و 813۸7 این واژه را شتق از واجریشهی هند و اروپایی -8۸/811* (به معلی "دمزدن")
میداند.
۲- محتملاً ۷81610۷۷۰ و ۶88۷
=== leaf 348 ===
[pdf page 349]
۵۰ ) ستوسه شنوسه اشنوسه؛ سنرسه (به چم "عطسه")
فارسی (۳8۸۹۸/۷): استوسه, شنوسه, اشنوسه, سنوسه (به چم عطسه:)
| چمانگلیسی سرواژی فارسن 0 ور ۱88828
پهلری (7اتله۸): ان بایان سوئدی (5178:201377): ۷۷8۸
سانسکریت (5۸/5717): ردنا نروژی (/081850142/: انیا
ارمتی (47482/1۸7): اد انشا هلندی (010767): 122
پونانی (0865): ۳۲۸۹۲۲۸۸۲ ایرلندی کهن (تلول#ا 0):
لاین (770) :57870۷0838 ,8787437110 ,87835070
فرانسه ([)27ق۳): لد زانی اد ید
اسپانپایی (5۶۸(/18): ۰ 88703802۸ پسگشتها 5
ایتالیایی (7(مال )+ 5۸1۸ 33839 مایمن
رومانی (۸//21(7-): 578201۸ 6 (8۳578) +80
ابسلندی کهن (/(010۸/14/م5 صاه): 5 (8788۳8) +7۵( تط0
8۸ ,32708۸" 3 (8(8578) نقل الق ها
آلمانی کهن (/(628۵/۸ لبط صان): 24 ناه
1108۸7 0 (58575) :005
آلمانی (058/۸0): لد اد ال 6 (83۳828) 7
انگلیسی کهن (50/ا50/0 010): برهان قاطع : ۱۱۰۲۴۱
01 ,5۸/55۸ لغتنامه دهخدا: ۳ و ۱۴۵۳۲
انگلیسی (8/7/ا8(70): اد رد اد ون فرهنگ معین + ۱۹۶۴
دانمارکی (0۸/1324): نی ۱
یادداشت:
۱ واژههای ژرمنی وابس
```


## [2026-09-14T02:05:48.768Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10150,10170p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-14T02:05:48.819Z] TOOL RESULT

```
ei) sabi chy HOLD ENGLISH) pS gul&i\
ior y irre haces aabctd FNESAN, FNEOSAN
TAN Teak lo Kad SNEEZE ENGLISH) gaJ&\
1 NYSE (DANISH) jails
heethoal
ENYSAt 45 5sthe! (ENEHAN: 5 gli rales ly gol jl 53 “bape” @ aly gay} Gas -d
ce ST sed opt gs" pe 4) PNEDMA 4 ("02303" (2p 4) PNEIN gly Slay ocaen
ale aly
ala SKEU- | KSEUs gly! y stn Gat, aly jt) Cai cal lan jly BUCK ~¥
STUN, STUNAG PAHLAVI) 5 hq STONA, STUNA —-(AVESTAN) glee!
—_
[pdf page 350]
TOV | faten opie
STEOR — (OLD ENGLISH) oS gnd&\ STON, ISTUN KURDISH) 52,
STEER ENGLISH) gud} STAN MAFGHAND (34) gait
STUUR DUTCH) «sacha STHONS, SANSKRIT) a) Suibe
SIUN, SIUNAG = (ARMENIAN) 1
‘REFERENCES cntKag STYLOS, STAUROS (GREEK) gli
POKORNY. —=~=~=« 081009. -STAU,, (IN-STAU-RARE).(LATIN) 53
BARNHART: STIU-RJAN GOTHIC) S56
(STYLUS) 1081, (STEER) 1065 MOLD SCANDINAVIAN) 46 Ll
```


## [2026-09-14T02:05:54.623Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== SYN sneeze ==\"; grep -n -i \"sneeze\" SYN.txt | head -20\necho \"== HRN ==\"; grep -n \"niesen\\|Niesen\\|nusa\\|snosa\" HRN.txt | head\necho \"== HUB ==\"; grep -n \"Niesen\\|niesen\" HUB.txt | head"
}
```


### [2026-09-14T02:05:54.709Z] TOOL RESULT

```
== SYN sneeze ==
5212:SNEEZE (vb.)
6714:2. Grk. mvéw (dvarvéw ‘take breath’, in NG the usual form for ‘breathe’; cf. Fr. respirer, etc., below) with the sbs. mvedua, von : ON fnysa ‘sneeze, snort’, OE fnéosan ‘sneeze’, etc., IE *pneu- in words for ‘puff, pant, breathe, etc.’. Walde-P. 2.85 (with other similar groups with initial *pn-, all of imitative orig.).
6769:BOD pans OF THE 4.54 SNEEZE (vb.) Goin ee Lith. tiaudéti
6770:arapvysat ON hnjosa-, fnijsa Lett.  sk’aut, 3k’audét Grk. greprifoHet Dan. nyse Chsl. . see NG sternuere Sw, nysa SCr.  kthati Lot starnulare OE gefnésan Boh.  kgchati It qernuer ME nese, fnese, snese Pol. _—kichaé a estornudar NE sneeze Russ. _¢ichat’ Pe sirdnula Du. niezen (fniezen) Skt.  ksu-~ Tr sreod (sb-) OHG  nitosan, niesan Av. 3 Nir. sraoth (sb.) MHG niesen Mey pane NHG _niesen Br __sirea
6771:he words for ‘sneeze’ are of imita- | NHG niesen; *keu-s- (*hkus-) in SCr.- Alt - Noun and verb are regularly ChSl. kuchnovenije (sb.), SCr. kihati, Ea ‘Only the verbal forms are | Boh. kychati, Pol. kichaé; but also with ba t for Irish, where the verbal i-vowel, Russ. cichat’, etc. Berneker
6783:ME snese, NE sneeze, perh. due in part to a misreading of fnese, but sup- ported by new imitative association (or, as Walde-P. 2.551, an inherited form representing *sneus- beside *kneus-, etc., above, 2). NED s.v. sneeze, vb.
29352:usual in this sense); not as = thanks! and similar polite expressions, which, though of the same group, with some exceptions (e.g. Lith. adia, fr. the sound of asneeze = ‘good luck, God bless yow’; Russ. spasibo : spasat’ ‘save, spare’), are not always identical with the forms listed (e.g. Fr. merci).
== HRN ==
1209:90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
1223:niesen, an. hnjosa, mittelengl. fnesen niesen', ver-
== HUB ==
428:90. Die germanischen W5rter fiir 'Niesen' fiihrt Kluge auf
6043:spenta-; asndsa {isnosa) 'das Niesen H. 90 und oben p. 15;
6054:H. 78; istOx 'Zweig* H. 82; isfand *Raute*, isnGsa *Niesen
6083:'Niesen' H. 90; sind 'Schwimmen' H. 792; sikdftan spalten,
8312:p. 79 ; mar *Gatte H. 796, oben p. 82 ; isnOsa 'Niesen H.
```


## [2026-09-14T02:05:58.025Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- HRN 90 ---\"; sed -n '1205,1232p' HRN.txt\necho \"--- HUB 90 ---\"; sed -n '424,440p' HUB.txt"
}
```


### [2026-09-14T02:05:58.081Z] TOOL RESULT

```
--- HRN 90 ---
Jer. 2, 22).
arm. LW. ausnan 'Seifenkraut*,
aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
Zu aiwis vergl. indessen unter bes-, bis- (No. 221).
90. eSnOse, isnöse 'das Niesen', senöse, sinöse, sinöse-).
germ. Vhnus bezw. /wws, vergl. ahd. niosan^ mhd.
') Die Awestaform ist von de Lagarde falsch angesetzt, der
die Lautverhältnisse verkennt.
V V
*) FR und FJ haben die folgenden Belege (nur FJ constatirt
einen Majhülvokal): (Metr. Hezej)
deniäyl pisk'l ö esnösc'l ter
cü äred gös^ gerdünrä küned her
Abu'l Xeir.
(Metr. Hezej):
merä imröz^ tobe süd^ däred
ciinänci derd-i dendänrä senöse
Rüdegl.- 22
niesen, an. hnjosa, mittelengl. fnesen niesen', ver-
schieden von mittelengl. snesan, engl, to snee:se
(Kluge, Etymolog. Wörterbuch).
kurd. heenlsum *ich niese' (Justi, No. 66, wo auch
die Etymologie).
Die neupersische Grundform müsste *senöse sein.
91. ef-, ew-, Praefix, ß-, fu-,
ap. abiij 'herzu'; aw. aihi, aiwi *herzu, oben' etc.;
phlv. a/-, päz. awa-; ai. abhi 'herzu, oben' etc.
92. uftäden ^fallen', Praes. uft-em, fitaden, uftädegt
--- HUB 90 ---
(vgl. zd. uS'Snd Vaschen* und wegen sn fiir sn : ap.
vasna = zd. vasna u. ahnl.) zuriickgehen k5nnte. Ap.
^abisnana^ ware zu np. *afsnan = arm. *ausnan^ osnan^)
geworden.
90. Die germanischen W5rter fiir 'Niesen' fiihrt Kluge auf
die Wurzein vorgermanisch qnus^) und ksmis zuriick."*)
Bildet man aus letzterem ein vorgerm. Substantiv
*ksnoMso- und ubertrS-gt dies ins Iranische, so erhalt
man iran. "^x^nauSa- = phi. *snOsak = np. iSnoSa.
Leider ist die Wurzel ksnus sehr hypothetisch.
92. Np. iiftddan ^fallen* aus oftatan (Gl. and Iiid. 45) von
Wrzl. pat scheint zunachst eine Bildung wie gr. nrwaig^)
von Wrzl. pet {Trl-nT-to), erweist sich aber durch phi. opastan
*) Vgl. aitsakf dSak fur osak — np. wla, arab. pers. tiSSoq 'gummi
ammoniacum'.
*) Vgl. np. afsarn = arm. auSarak, dSdrak,
') qmts — germ, hmts und fnus, vgl. N o r e e n , Abriss der
```


## [2026-09-14T02:06:16.319Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"^scum\" \"^skim\" \"^hose\" \"^hut,\" \"^hide\" \"^obscure\" \"^corium\" \"^curium\" \"^cutis\"; do echo \"--- $w ---\"; grep -n -m2 \"$w\" KLN_1971.txt | cut -c1-400; done"
}
```


### [2026-09-14T02:06:17.554Z] TOOL RESULT

```
--- ^scum ---
57703:scum’, OHG. hroz, roz, ‘nasal mucus’, MHG., 
216033:scum, n. — MDu. schum(e) (Du. schuim), rel. to 
--- ^skim ---
223373:skim, tr. and intr. v. — ME. skimmen, prob. fr. 
223382:skimmer, n., 1) a person or thing that skims ; 2) a 
--- ^hose ---
116012:hose, n., article of clothing for the legs; stock- 
--- ^hut, ---
117125:hut, n. — F. hutte , fr. MHG. hiitte or fr. OHG. 
--- ^hide ---
17404:hide away’, ff. Ami (see apo-) and xpuirmv, ‘to 
17405:hide’. See crypt 
--- ^obscure ---
45055:obscure. 
105221:obscure, unintelligible book; book of spells, 
--- ^corium ---
56907:corium, n., vascular layer of the skin, the derma. 
56933:corium. 
--- ^curium ---
61925:curium, n., name of a radioactive element ( chem .) 
--- ^cutis ---
62339:cutis, n., the skin beneath the epidermis, the 
216128:cutis, cuticle.
```


## [2026-09-14T02:06:20.426Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '56907,56920p;61925,61932p;62339,62350p' KLN_1971.txt\necho \"==== hose/hut/scum/skim ====\"\nsed -n '116012,116022p;117125,117136p;216033,216045p;223373,223382p' KLN_1971.txt"
}
```


### [2026-09-14T02:06:20.551Z] TOOL RESULT

```
corium, n., vascular layer of the skin, the derma. 
— L., ‘hide, skin, leather’, lit. ‘the hide stripped 
off’, rel. to cortex , ‘bark’, scortum , ‘skin, hide*, 
fr. I.-E. base *(s)qer-, ‘to cut, separate*, whence 
also OI. kftih, ‘hide’, carman -, Avestic dayman-, 
‘hide, skin’, Russ, skord, ‘hide’, kora, ‘bark, 
rind’, Gk. xopjxoc;, ‘trunk of a tree’, OHG. scerm, 
scirm , ‘shield, defence, cover’ (orig. ‘the hide 
covering the shield’), OHG. herdo , ‘fleece’, OE. 
heorda, ON. horundr, ‘skin’, Mir. scairt, ‘mid- 
riff, heart’, W. corwg, cwrwg , ‘trunk of the body, 
carcass, boat’, OE. sceran , sciran, ‘to cut, shear’. 
See shear and cp. words there referred to. 
Corixa, n., a genus of insects (entomol.) — ModL., 
curium, n., name of a radioactive element ( chem .) 

— ModL; named in 1946 by its discoverer, 
the American chemist Glenn Theodore Seaborg 
(born in 191 2) in honor of the two Curies (Pierre 
and his wife Marie), for their pioneering work 
on radioactivity. Cp. curie and prec. word. For 
the ending of curium see chem. suff. -ium. 
cutis, n., the skin beneath the epidermis, the 
derma ( anat .) — L. cutis, ‘skin’, lit. ‘that which 
covers’, fr. I.-E. base *{s)qeut ‘to cover’, 
whence also OE. hyd , ‘skin’. See hide, ‘skin’, and 
cp. cutaneous, cuticle. Cp. also cyst, -cyte, ecu, 
escutcheon, esquire, scudo, scum, Scutellaria, 
scutellum, scuttle, ‘receptacle’, scutum, syncy- 
tium, zuchetto. Base *(s)qeut - is rel. to base 
*(s)qeudh-, ‘to cover’; see custody. 

Cutiterebra, Cuterebra, n., a genus of botflies (en- 
tomol.) — ModL., compounded of L. cutis , 
==== hose/hut/scum/skim ====
hose, n., article of clothing for the legs; stock- 
ing. — OE. hosa, rel. to OS., ON., OHG. hosa, 
MHG. hose, ‘covering for the leg’, Dan. hose, 
‘stocking, hose’, G. Hose, ‘trousers’, Du. hoos, 
‘waterspout’. These words lit. mean ‘cover, 
covering’, and derive fr. I.-E. *qeus-, -5- enlarge- 
ment of base *qeu~, ‘to cover, hide’. See hide, 
v., and cp. house. OF. hose (whence F. houseau ) 
and It. uosa, ‘gaiter’, are Teut. loan words. 
Derivatives, hose, tr. v., hosier (q.v.) 

hut, n. — F. hutte , fr. MHG. hiitte or fr. OHG. 
hutta [OS. hutta, Dan. hytte , Swed. hytta, Fris., 
MLG., MDu. hutte (Du. hut) and Sp. huta are 
borrowed fr. HG.], which is rel. to OE. hydan, 
‘to hide’. See hide, ‘to conceal’, and cp. words 
there referred to. Cp. also cuddy, ‘cabin’. 
Derivative : hut , tr. and intr. v. 
hutch, n., 1) a chest or box for storage; 2) a coop 
or case for small animals; 3) a hut, hovel; 4) a 
mining trough; 5) a truck; 6) a measure. — 
ME. huche, fr. OF. (= F.) huche, ‘bin, kneading 
trough’, fr. ML. hutica, which is of uncertain 
scum, n. — MDu. schum(e) (Du. schuim), rel. to 



ON. skum , Dan., Swed., Norw. skum, OHG. 
scum , MHG. schum, schoum , G. Schaum , ‘foam, 
froth’; perh. fr. I.-E. base *sqeu-, ‘to cover’. 
See sky and cp. next word. Cp. also skim and 
the second element in meerschaum. Cp. also 
scutum, scuttle. 

Derivatives : scum, tr. and intr. v., scumm-er , n., 
scumm-ing, verbal n., scumm-y , adj. 
skim, tr. and intr. v. — ME. skimmen, prob. fr. 
OF. escumer (F. ecumer), fr. escume (F. ecume), 
fr. OHG. scum (MHG. schum, schoum , G. 
Schaum)\ rel. to MDu. schum(e), whence E. 
scum (q.v.) For the change of u to / cp. brisk (fr. 
F. brusque) and ribbon (fr. F. ruban). 
Derivatives: skim, n., skimm-ing, n., skimm-ing- 
ly, adv. 

skimmer, n., 1) a person or thing that skims ; 2) a
```


## [2026-09-14T02:06:28.249Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -A10 \"^obscure, adj\" KLN_1971.txt | head -20; echo \"=== SKT ===\"; grep -n -A6 \"^obscure\" SKT.txt | head -12; echo \"=== LEW obscurus ===\"; grep -n \"obscurus\" LEW_1910.txt | head -5"
}
```


### [2026-09-14T02:06:28.346Z] TOOL RESULT

```
164755:obscure, adj., dark, gloomy; not dear, indistinct, 
164756-vague; difficult to understand. — ME., fr. OF. 
164757-(= F.) obscur , fr. L. obscurus, ‘dark, dusky; in- 
164758-distinct, uncertain, unintelligible’, orig. ‘cover- 
164759-ed’, formed fr. ob- and I.-E. base *(s)qeu -, 
164760-*(s)qewa-, ‘to cover’, whence also L. scutum, 
164761-‘shield’, ON. sky, OE. sceo, OS. skio, ‘cloud’. See 
164762-sky and cp. words there referred to. Cp. also 
164763-the second element in chiaroscuro. 
164764-
164765-Derivatives: obscure, n., obscure, v. (q.v.), ob- 
=== SKT ===
=== LEW obscurus ===
```


## [2026-09-14T02:06:40.026Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%88%DA%86/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for کوچ verbatim, including any origin tag in brackets (e.g. [ تر . ] for Turkish), and the دهخدا entry's note on origin. Also any sense \"خانواده، ایل\"."
}
```


## [2026-09-14T02:06:41.851Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== TTS koch ==\"; grep -n -i \"köç\\|kotsch\\|kütsch\\|wandern\" incoming/TTS/TTS_pages.txt | head -10\necho \"== LKT ==\"; grep -n -i \"köç\\|kotsch\" LKT.txt | head -5"
}
```


### [2026-09-14T02:06:41.929Z] TOOL RESULT

```
== TTS koch ==
== LKT ==
10:KARL  LOKOTSCH
59:Dr,  Karl  Lokotsch.
187:Lokotsch,  Etymolog.  Wörterbuch.
225:Lokotsch,  Etymolog,  Wörterbuch.
1097:(Vom  Stamme  jap,  cap  s.  hier  Nr.  395] 'Kurzer  Mantel  mit  langer,  ausgeschnit- Lokotsch,  Etymolog.  Wörterbuch.
```


### [2026-09-14T02:06:45.890Z] TOOL RESULT

```
# کوچ Dictionary Entries

## Farhangu Mo'in (فرهنگ معین)

**[تر - مغ.]** (اِ.) حرکت عده ای از جایی به جایی.
(ص.) لوچ و احول.
(اِ.) جغد، بوم.

*[The origin tag indicates Turkic-Mongolian origin]*

## Dehkhoda Dictionary

The Dehkhoda entry contains an explicit note stating: "این لفظ ترکی است" (This word is Turkish), attributed to a margin note in the Burhan dictionary edition.

## Family/Household Sense

The page documents that کوچ also means "خانه کوچ" referring to "زن و فرزندان و اهل و عیال" (wife, children, and family members), with some sources suggesting metonymic use for "زن" (wife).
```


## [2026-09-14T02:06:57.130Z] TOOL CALL #86: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B2%D9%87",
 "prompt": "Persian کازه: is there an entry? Give etymology and meaning. If no entry, say so."
}
```


## [2026-09-14T02:06:59.169Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-",
 "prompt": "Proto-Indo-European *(s)kewH- \"to cover\": give the reconstruction, meaning, and the list of derived terms/descendants (Latin cutis, obscurus, cunnus; Greek kutos, skutos; Germanic *hūdiz, *huzdą, *huson-; Avestan; Persian). Quote what is listed."
}
```


### [2026-09-14T02:07:00.503Z] TOOL RESULT

```
# کازه (kāza/kâze)

**Entry exists:** Yes, this is a Persian noun entry in Wiktionary.

**Etymology:** The word was "Borrowed from Sogdian (kʾzʾk, 'little house')" and is cognate with Khotanese khāśā̮na-, meaning "abode, place."

**Meaning:** An archaic term for a "hut; cottage" or small dwelling.
```


### [2026-09-14T02:07:04.777Z] TOOL RESULT

```
# Proto-Indo-European *(s)kewH-

**Reconstruction:** *(s)kewH-

**Meanings:** The root carries two primary senses: "to cover, conceal, hide" and "hide, skin."

**Key Derived Terms:**

The entry lists approximately 50 derived terms across Indo-European languages. Notable descendants include:

- **Latin:** *cutis* ("skin, hide, leather")
- **Greek:** σκῦτος *skûtos* ("skin, hide") and κύτος *kútos* ("hollow vessel")
- **Germanic:** *hūdiz* ("hide, skin")
- **Sanskrit:** स्कुनाति *skunā́ti* ("to cover")

**Additional Descendants Mentioned:**

The page documents formations yielding Old English *sċunian* ("to shun, avoid"), Latin *scūtum* ("shield"), and various Norse terms like Old Norse *há* ("hide") and *skáli* ("hut, shed, barn").

The page notes an alternative reconstruction of *(s)keHu-* and indicates Balto-Slavic, Celtic, and Tocharian cognates exist, though some connections remain marked as uncertain with question marks throughout the scholarly documentation.
```


## [2026-09-14T02:07:12.091Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"khāśā\\|khasana\\|khāśa\\|kaza-\\|kāza\" ISS_alt_DKS.txt | head -10\necho \"=== HENNING two central asian ===\"; grep -n -i \"Two Central Asian\\|k'z'k\\|kazak\" HENNING_selected_papers.txt | head -10"
}
```


### [2026-09-14T02:07:12.178Z] TOOL RESULT

```
713:а ‘ог’, І 189, 11172 riysütcana khāśāña à тарї Атуї uca jsa tto be drunk with rice-water or with honey water'; JS 512 fdgd (for famgd) а và solda, а mīrāhīja Катай à ча
1698:ma asajamana, Pali asajjamdna-, with -jo- archaistic from -ў- < -Jy-. For khasána- either Rhata- with suffix -ana- or -akāna-, or compound khāsg-däna- (as khaysána- ‘belly’ *&hüysa-dana-) to base kas- or khas- as in N.Pers. as ' hut', kāzah ‘house’, Armen. lw Каст ‘arrangement’ (see s.v. pyays-, käysū).
8518:háysiná ‘fountain (?)', ти 38:42 jastüzie khasa va isphiraciiid haysatña ' celestial (royal) beverages splashing in the foun- tain’, HI 47:62-3 Јаѕіййе khasana asphirdci(sa) һйузїйй. Possibly *fraoazana- ‘place of gushing forth’, to Sogd. Bud. "w'z "p (*avaza- ap) ‘pond water’; "алай ‘lake’, Man. "олуу 'lake, pond’, Armen. lw auazan 'water receptacle, pond’, Syriae *wzn-' 'font', N.Pers. dvüxah
=== HENNING two central asian ===
85:Two Central Asian Words (TPS, 1945, pp. 150-162)
11448:W. B, HENNING—TWO CENTRAL ASIAN WoRDS I
11581:W. B. HENNING—TWO CENTRAL ASIAN WoRDS 158 as Buddhist term, suduryan is the equivalent of Skt. stiipa, ie. a mound or tower or pyramid or dome in which relios of the Buddha are preserved. It is found already in Uyyur ‘Turkish where in the hendiadys with either sin “tomb, grave "? (sce F. W. K. Miller, Uigurioa, i, 68; ii, 58; Bang-Gabain- Rachmati, Tiirkische Turfantezte, vi, p. 128, line 290 var.), or sitavan = SI a, &- (Vigurica, iii, 19, 21%) it in lace” in general. By itself it is met with in a Manichwan story (LeCoq, Tiirkische Manichaica, i, 6%, spelt
11694:W. B. HENNING—TWO CENTRAL ASIAN WoRDS 160
```


## [2026-09-14T02:07:18.510Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11570,11590p' HENNING_selected_papers.txt | cut -c1-1200"
}
```


### [2026-09-14T02:07:18.578Z] TOOL RESULT

```
ated an intentional ‘there is no other truco of
 
   
 
    
 
    
   
        
                                                                                         
W. B. HENNING—TWO CENTRAL ASIAN WoRDS 158 as Buddhist term, suduryan is the equivalent of Skt. stiipa, ie. a mound or tower or pyramid or dome in which relios of the Buddha are preserved. It is found already in Uyyur ‘Turkish where in the hendiadys with either sin “tomb, grave "? (sce F. W. K. Miller, Uigurioa, i, 68; ii, 58; Bang-Gabain- Rachmati, Tiirkische Turfantezte, vi, p. 128, line 290 var.), or sitavan = SI a, &- (Vigurica, iii, 19, 21%) it in lace” in general. By itself it is met with in a Manichwan story (LeCoq, Tiirkische Manichaica, i, 6%, spelt
 
 
  
 
     
 
* burial-p
nepery’n in Man. script, —either supuryan or suburyan) which ells of a prines who being intoxicated spent « night in a tomb: he mistook it for his own house. It is clear from the story that a suburyan was a se above the ground, not, ¢.g., a subterranean vault. ‘The word
alchral monument raised
```


## [2026-09-14T02:07:22.964Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"XAUDA\\|XAODA\\|HELMET\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T02:07:23.018Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:07:37.690Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/sneeze' --note 'page 455 root Skeu 1/Pneu, node 3: English sneeze < ME fnese, fn- misread as sn-' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://www.etymonline.com/word/pneumonia' --note 'page 455 root Skeu 1/Pneu, node 5: pneumonia from Gk pneumon (root *pleu-), not pneuma' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%AF' --note 'page 455 Skeu 2, node 2: Persian khud helmet, MP xod < Parthian, PIE *kadh- not *(s)keu-' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%B3' --note 'page 455 Skeu 2, node 6: Persian kos < PIE *kuHis vulva, cognate Lith kusys' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86' --note 'page 455 Skeu 2, node 11: Persian kuch borrowed from Turkic *koch-, not Iranian' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/cutis' --note 'page 455 Skeu 2, node 9: Latin cutis < PIE *(s)kewH- to cover' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B2%D9%87' --note 'page 455 Skeu 2, node 3: Persian kaze borrowed from Sogdian k-z-k little house' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D9%88%DA%86/' --note 'page 455 Skeu 2, node 11: Moin tags kuch [tor.-mogh.] Turkic-Mongolian; Dehkhoda this word is Turkish' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B2%D9%87/' --note 'page 455 Skeu 2, node 3: Moin kaze = alachiq, kolbe, soumee; no etymology tag' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-' --note 'page 455 Skeu 2 root box: PIE *(s)kewH- to cover, descendants Lat cutis, Gk kutos/skutos, Gmc *hudiz' >/dev/null 2>&1; ls data/verification/sources/web | tail -15"
}
```


### [2026-09-14T02:07:45.693Z] TOOL RESULT

```
ff55c7ac46891403.txt
ff5dfd0afcdc6a63.txt
ff652b3a9e61958b.txt
ff6e2af5503b9a8c.txt
ff6fd07203196bd5.txt
ff7e9b1baa06d2b4.txt
ff935500b70ed5ac.txt
ff953f567dd42ef2.txt
ffa4ae351c7c0905.txt
ffd3321bd18bd33d.txt
ffd9a1cb348544e3.txt
fff60cb0f7522ebe.txt
fff785f6acf3f6b9.txt
fffecb896b08a176.txt
index.jsonl
```


## [2026-09-14T02:07:48.694Z] TOOL CALL #92: Bash

```json
{
 "command": "tail -12 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'), '->', d.get('file') or d.get('path'), d.get('status',''))\n\""
}
```


### [2026-09-14T02:07:49.845Z] TOOL RESULT

```
https://abadis.ir/fatofa/%D8%B3%D9%85%D8%A7%D9%88%D8%B1/ -> data/verification/sources/web/4a6b49c3f8426395.txt 200
https://vajehyab.com/?q=%D8%B3%D9%85%D8%A7%D9%88%D8%B1&d=moein -> data/verification/sources/web/6b12397f08a11eba.txt 200
https://www.etymonline.com/word/sneeze -> data/verification/sources/web/ab164fa2981039e4.txt 200
https://www.etymonline.com/word/pneumonia -> data/verification/sources/web/21ce6ce116e42414.txt 200
https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%AF -> data/verification/sources/web/dace010ac1c69ac8.txt 200
https://en.wiktionary.org/wiki/%DA%A9%D8%B3 -> data/verification/sources/web/964bcfb2722aab78.txt 200
https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86 -> data/verification/sources/web/c27d4eb9df4b5f78.txt 200
https://en.wiktionary.org/wiki/cutis -> data/verification/sources/web/4e13703c0dc8b87b.txt 200
https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B2%D9%87 -> data/verification/sources/web/0f097745b114ed1f.txt 200
https://abadis.ir/fatofa/%DA%A9%D9%88%DA%86/ -> data/verification/sources/web/9646f59ab39949ed.txt 200
https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B2%D9%87/ -> data/verification/sources/web/2527095eb56362d9.txt 200
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH- -> data/verification/sources/web/b80c5d141c276db6.txt 200
```


## [2026-09-14T02:07:52.680Z] TOOL CALL #93: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:07:52.729Z] TOOL RESULT

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


## [2026-09-14T02:07:56.782Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2000])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-14T02:07:57.970Z] TOOL RESULT

```
{"pdf_page": 385, "book_page": 355, "verified_by": "claude-opus-5", "verified_on": "2026-09-07"}
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
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seite
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance": "partial",
   "note": "lists ai. pajasyá- 'Bauchgegend, Weichen' beside the pakṣa- family; gloss 'flank'."
  }
 ]
}
```


## [2026-09-14T02:09:09.007Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport re\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor i,p in enumerate(d):\n    if re.search(r'fn[eё]usan|fneosan|hnjosa', p):\n        print('leaf',i, re.findall(r'\\[pdf page (\\d+)\\]',p)[:1], p[:100].replace('\\n',' '))\nPY"
}
```


### [2026-09-14T02:09:10.155Z] TOOL RESULT

```
leaves 725
leaf 89 []                                                                                      :              
leaf 555 []                                                                                      ;
```


## [2026-09-14T02:09:13.408Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (89,555):\n    t=d[i]\n    import re\n    for m in re.finditer(r'fn[eё]usan|fneosan|hnjosa',t):\n        print('--- leaf',i,'---')\n        print(t[max(0,m.start()-900):m.start()+500])\n        break\nPY"
}
```


### [2026-09-14T02:09:14.615Z] TOOL RESULT

```
--- leaf 89 ---
-eia „die breitblattrige'' oder allenfalls „weit die      Aste breitende''.

pneu- und andere mit pn- anlautende Sippen fiir ,,keuchen, atmen", schall-
    malend, und geschichtlich noch nicht naher beurteilt.
  Gr. Tiveco {Ttvevoai) „wehen, keuchen, atmen, riechen", Ttvevjua „das Wehen,
Hauch, Atem usw.'', Tivorj „das Wehen, Schnauben"; dazu vielleicht auch
noi-Tivvoj       „sich riihren,   rege sein, trans. sich eifrig womit beschaftigen",
Pf. zxETivvo^ai ,,geistig rege, verstandig sein", TiEnvvpEvoq „geistig rege, ver-
standig", 7ivvt 6<^' £iu(fo(ov, owcpgcov Hes,, dfiTzvvo&ai „wieder zum BewuUt-
sein     kommen (s. auch u. pen „erforschen"), wenn „sich riihren, rege, bes.
geistig rege" aus    „beim Laufe keuchen" und „atmen = lebhaft sein" (vgl.
lat.  animus 1) entwickelt ist (vollstandige Trennung von             empfiehlt
 Schulze Qu. ep. 322 ff.).
    Aisl.fnpsa „8chnauben“, ags, fneosan „niesen {fnora „das Niesen"; s. auch
 u. sqeii „niesen"), mhd. plinfisen „schnauben, niesen" (pJi- schallverstarkend
fur f), phnust m. ..unterdriicktes Lachen" (vgl. auch nhd. pfnuttern ds.),
norw.-mdartl.          „kichem". Daneben germ, fncs-, fnos-, fnas-: ags.
fnwst m. Atem, Hauch", fn^cttan „schnarchen, schnauben", mhd. pJmcisen
„schnauben", phnast m. „das Schnauben", ahd. fnasteon „anheiare"; aisi.
fnosa „schnauben"; aisl. fnasa „schnauben"; ahd. fnasJcazzen, fneshezzen^
mhd. plmes
--- leaf 555 ---
israum“, alter i.^nJi 2 idde^hydde,^\vX^e\^ Gefangnis-
raum“. aschw. A^{7Ja„verbergen”' (s. Falk-Torp u. hytte^ m. Lit., Persson aaO.).


3. sqeu-,       qseu- schallmalend „niesen'^
     Ai.            ,,niest“,    kmii-lt „das Xiesen^*;              alit.   skiattdzm^ skiaudeti
(ahnlich cidtidziu,          '-deti)^    lett.       (viel starker abweichend
                                                      sk'aiidet „niesen“
slav. koclinatij kychatiund thcliati, an welch letzteres wueder einigermaBen
ai. chikkd „Kiesen'* anklingt, s. Uhlenbeck Ai. Wb. 94, Berneker 165 f.. 658f.\

z.   B.    FickIM42.
     Als nasalinfigierende Bildung kann betrachtet werden                                    (vgl.   Zupitza G. 9,
BB. 25, 95, Uhlenbeck Ai. Wb. 72f.. Falk-Torp                                   u.       nyse, fnyse)     "^qsnen-s-
 {qneus-^ mens-) in npers. imosa, asndki „niesen“; aisl. hnjosa, mengl. nesen^
ahd. niosan (daneben ags. fneosan, nl. fniezen durch Kreuzung mit "^pneu-)                                              ;


mengl. snesen^ ®^gJ*           in der Bed. ahnliche germ. Worte wie nd.
sniisen^ dan. smise ,,schnoben, wittern" u. dgl. s. bei Falk-Torp aaO. ahn-                                   ;


lich auch lit. Hiankti ,,schnupfen''' (Zupitza).
                                                                                                       36 *
```


## [2026-09-14T02:09:23.290Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (550,551,552):\n    t=d[i]\n    print('=== leaf',i,'(printed ~',i-4,') ===')\n    print(t[:1800])\nPY"
}
```


### [2026-09-14T02:09:24.455Z] TOOL RESULT

```
=== leaf 550 (printed ~ 546 ) ===
                         ^




546                                 speibh-, -p-, sqi-m-b-      — (s)qeu-

sqeibh-, -p-, nas. sqi-m-b- „8chief, hinken(d)‘‘.
   AisL sheifr „8chief“, ags, scdf^ scah ds. (in scaf-fdt „schieffuJBig“), mnd.
scJief ds.(nhd. mdartl. scheif)^ woneben (wohl als "^sqeipos^ Brgm.         207)
Dihd. (md. nd.) schief^ und (als germ. *skihha-') hess.-frank. schepp „schief“,
sowie (als germ. ^sMppa-) mhd. schipfes Adv. „quer“.
     Lett.    sJcibs    „schief“,    s/cieb-u,    -t   „scliief       neigen,     kippen^';     gr.   oxlyjai*
dxkaoau A^aioi Hes.
  Nas. gr oxip^og „lalim“, oxtp^d^eiv ,hinken“ (u. dgL, s. Ehrlich aaO.
                                                           5


und Boisacq s. t .; gegen Solmsens Beitr. I 215 Verb. m. ondCco „hmke‘‘
als    ^sqeng-uos spricht bes. oxty^ai).
   Zup. G. 43, Ehrlich aaO., Persson Beitr. 156; Falk-Torp u. skjev (auch
sclve^ wo mit Unrecht die zu sqei-p- „spalten“ gehorige Gnippe von ahd.
sciba „Scheibe“ angereiht wird), Fick III^ 464, auch 43 (die Sippe von dt.
Jcippen s. u. geibh-; mir. scibud „rucken“ stimmt in der Bed. nicht).
   Idg. sqei-p-j -ih- ist wohl erw. aus sqei-^ vgl. sqai-uo~s (sqdi-uo-s) „schief,
link‘‘; neben mhd. schie-f steht gibed, schie-c; liber solches nicht mit einigem

YerlaB in altere Zeit verfolgbares sJcei- „schief‘‘ im Germ. s. Fick III^
463 {sM-^ skik-)^ vgl. auch 467 {sku- IV).


1. (S)qeil-       „herrichten, ausfuhren“.
     Gr. oxevog n. (meist           pi.)    „Gerat, Riistung^,           oxeviq    ^Rustung, Kleidung,
Tracht^^, Gxevdl^ca „bereite, richte an; putze aus; bewaffne; stifte an“;
     aisl.   heyja (Praet. Jiada)^ ags. began „ausfuhren^;
     abg. prekutiti          „zieren,      schmucken^,         ksl.    kutiti    „machinari“,         u-kutiti
j^xaja
=== leaf 551 (printed ~ 547 ) ===
                                               (s)qeu-                                        547

vergleicht mit chavi-- zugleich av. surT „inenschliche Haiit“                       — mit palata-
lem Anlaut, daher fernzuhalten — und das weiSruss. Lw.                       lit.   shura „Haut“).
   Hochst fragwiirdig (Petersson IP. 34, 233) ai. hotambaka-^ m. eine Art
Zeug‘^              huUara- m. „wollenes Tuch, wollene Decke“ (^kutra-f)^
ut-kuta- m. „Sonnenschirm'‘ {^kida-^ kiitra- ?). Eedupl. ai. ku-kula „Hulsen,
Rustung‘‘ (Persson Beitr. 183; die Bed. „Hulsenfeuer“ durch AnschluB an
kUdayati ^versengt^^, woriiber s. u. qeu- „anzuiiden'‘; iiber das von Persson
verglichene apr. kekulis „Badelaken“ s. vielmehr Trautmann Apr. 355; auch
lat. cucullus^ cuctilio „Kapuze, Dute“, das nach Holder Akelt. Sprachsch.

I 1183, Yf. LEWb.^ und Thurneysen Thes. s. v. kelt. Ursprungs sein
durfte, bietet keine verlassliche Entsprechung).
      Arm. ciw „Dach, Decke“ {*skeuo-^ Scheftelowitz BB. 28, 294, Meillet MsL
18, 377);       mit anl. qh-     (s. o.)   arm. xuc   „Stube‘'' (v.   Patrubany IF. 13, 163;
Gdf. *qhU-skho-^ allenfalls zur 5-Erw.), fraglicher xavar „dunker‘ {^qhouo-^
Formans arm. -ar), xev „t6richt“ (eigentlicb „geistig verfinstert'*? Patru-
bany IF. 14, 57 f.), xu-p^ „Deckel“, xul, xVk „Hutte'', xlay (^qltUlatU) „weib-
liche Kopfverhullung, Schleier; Kleid'* Petersson KZ. 47, 282, der nicht
iiberzeugend auch ai. khola- „Art Helm, Regenhut^, russ, usw. siiba jjPelz^*
als    verwandte ^A-Formen auffaBt).
   Gr. oxvvta PL „Brauen“, imoxvviov „Haut oberhalb der Augenbrauen^'
(vgl. ai. skundti); axvlog n. ,,Tierhaut, (^^uB)schale“, o>cv?.ov abgezogene
Tierhaut‘‘ (nicht zu o>sv1a€o „zerrei6e,    schinde“, wie deqjua digco wegen        :



des V von:)            „abgezogene T
=== leaf 552 (printed ~ 548 ) ===
548                                    (s)qeu-



jjSchatten,   Dunkel, Schirm“, ahd* scuwo^ scU m. „Sebatten“,         sclo-c(Ji)ar n,
„Spiegel“, eigentlich „Schattengefa6'^ anord. sJcuggi m. „Schatten, Schatten-
bild, Gespenst*' shugg-sja f. „Spieger‘, got. skuggwa m. „Spieger‘ (diese
Sippe nicht besser zu schauen^ wie z. B. Feist 239); ahd. slcugin{a)^ mhd.
schiune^ nhd. Scheune („Obdach“), norw. mdarfel. shyggne m. „Hutte, Scheune,
Schlupfwiiikel“ (nicht annehmbar erwagt Persson Beitr. 186 fur die ahd.
snord. Form -g- — idg, k) anord. skaunn „Schild“; anord. skUme „dunker',
skumi m. „Zwielicht, Dammerung^', mnd. schummer „Dammerung“ (: lett.
skamt; vgl. Falk-Torp u. skummel^ sktimre)-, anord. hum f. „Zwielicht'',
hyma „dammern, dunkel werden“; vielleicht anora. skum^ ahd. scum „Schaum“
(wenn „deckendes‘‘);
  anord. skjdl n. „Versteck, Zufluchtsort, Schutz, Scheune'*, skjola „Bdtte,
Kubel“ (j.Yerwahrungsraum"), ablautend mnd. schul n. „Yersteck", afries.
skul „Yersteck", nnd. auCh „Schutz, Schuppen", woven anord. skyla „be-
schirmen, beschiitzen^, mhd. schuhn „verborgen sein, lauern, lugen";
  ahd. SCUT m. „Wetterdach, Schutz “ (; lat. ohscurus^ lit. skUra)^ mhd.
schUr „Obdach, Schirm", anord. skur „was die Schale der Mandel umgibt",
aha. skur a, sciura (^skurja) „Scheuer, Scheune" (nicht besser Siitterlin IF.
29, 128: "^skub-ra, zu dt. Schuppen, Schupfen); mit Formans -ko- (oder
von der Wzf. auf -A) und Dehnstufe o[u] wahrscheinlich got, skdJis^ anord.
skor, PI. skum\ aha. scuoh „Schuh" (Zupitza Gutt. 153, Trautmann Grm.
Ltges. 26, eigentlich „deckendes Oberleder des Schuhes", vgl. o. ir. cua-
ran „Schuh" und von der /-Erw. cymr. esgid „Schuh"; mndl. schoe „Schwert-
scheide, Futteral").
  Lit.   kevalas „Eierschale", lett.   cdula „Schale, Hiilse"   (s.   Endzelin B
```


## [2026-09-14T02:09:32.599Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(550,560):\n    t=d[i]\n    for pat in (r'xao[dδ]a',r'kusra',r'npers\\. kus|npers\\. kUs|kus „',r'cunnus',r'cutis',r'kusi|kUsis'):\n        for m in re.finditer(pat,t):\n            print('leaf',i,'(p',i-4,')',repr(t[max(0,m.start()-260):m.start()+260]))\n            break\nPY"
}
```


### [2026-09-14T02:09:33.731Z] TOOL RESULT

```
leaf 550 (p 546 ) '    90, 92, 96, 465f., 468 f., Zupitza Gutt. 127 f., 153, Johansson IP. 19,\n       128ff.  Die Gleichsetzung mit Wz. qeu- „wolben, hohr‘ unter „be-\n       decken=um etwas henimhiiHen; umwdlben; wolben; Wolbung nach\n       auBen“ (Johansson aaO., Yf. LEWb.^ u. cunnus^ Boisacq u. xvnr},\n       xvTog) verdient starkste Skepsis.                —\n                                             Ablaut z. T. von einer Set-Basis\n       sqeua^- {isqfi-; Hirt Abl. 106).                —\n                                         '
leaf 551 (p 547 ) 'zur w-Erw. von seq- „schneiden“, lat, secii-ris\nusw.), allenfalls, dock sehr unsicher, xcbag^ PL xcoea „Plie6‘^ (s. Boisacq s. v.).\n   Lat. ohsciirus „*bedeckt‘‘          =\n                                 „dunke^^ Yermutlich hieher (vgl. zur Bed.\nlett. kuja „cunnus\'‘, cymr. civthr ,,anus“, gr. xvooagog „anus‘^ usw., s. u.)\n\nlat. cuius „After‘‘ (wohl aus "^qu-los; an sich moglicb vom lat. Standpunkt\n\naus ware auch "^qMh-slo-^ Brugmann I^ 705, 769, oder qut-slo-; qfik-slo-;\ns. Yf. LEWB.2 s. V.; av. sUra- m. ,.Loch“ '
leaf 552 (p 548 ) 'ersson IF. 34, 235) ai. kugumbha- m.\n„Krug, Wassertopf der Einsiedler", ktiqapa- m. „Trinkgeschirr", kucaya-\nm. „Zisterne"; kaksi-- m. ^B^iich, Mutterleib, Degenscheide, Hohlung"; npers.\nAws „weibliche Scham" {s aus         nicht aus ks\\ s. Persson aaO.); av. kusra-\n„sich wolbend, hohl“, vikusra-^ hankusra- „sich auseinander-, zusammen-\nwolbend" (Geldner Metr. 159, Bartholomae IP. 1, 491 f., Airan. Wb. 475,\n 1436, 1770; die Bed. erinnert sehr an qeU’-q-^ qeu-g- „krummen, wolben",\ndoch ist neben letztem ein *qeu-k- '
leaf 553 (p 549 ) '62 (Zitat nach Boisacq 1117).\n     An. hud,, ags. hyd, ahd. hut i^hudi-) „Haut"" (schweiz. hut „Hulse, Frucht-\nschale"",  Binz ZfdtPh. 35, 101);\n     ahd. hodo, afries. hotha „Hode"" (Berneker IF. 10, 155,      Brugmannll^ 1,\n264;        zum -en-St. vgl. lat. cunnus aus "^cut-n-os^ Hode und cymr. cwd kaum\n—     z,    B. nach van Helten aaO.                      — zu      ai.     cotha m. „An8chwellung"") ;             ags.\nhopma m. ^Finsternis"", ahd. Jnitta „Hutte"" (y^quild oder "^qudhi^a; daraus\nas. huita, hutti'
leaf 553 (p 549 ) '\nJ. Schmidt Voc. II 351 Anm.      iiber das yon ihm zunachst verglichene lat.\n                                                :\n\n\n\ncuhirniiun „Yas, quo in sacrificiis yinum fundebatur"" s. Vf. LEWb.^ s. y.);\nliber xvodog^ xvortg s. die Wzf. qeii-s-,\n     Lat. cutis „Haut""; cimnus  pudendum muliebre"" i^qut-nos,^ s. Johansson\n                                                   ,,\n\n\nIF. 2, 19. 129;          nach Luft KZ. 36, 146 samt xvodog,^ das ^yvd-\'&og\n                                 nicht\nsei, zu ai. kJmddti ,,'
```


## [2026-09-14T02:09:55.703Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nd=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nln=6770\nprint('leaf', sum(1 for i in range(ln) if '\\f' in d[i]))\nPY\nsed -n '6780,6786p' SYN.txt"
}
```


### [2026-09-14T02:09:57.516Z] TOOL RESULT

```
leaf 300
Walde-P.
165, 658.
3. ON fnijsa, OE gefnésan (*fnéosan attested in fnéosung ‘sternutatio’), ME fnese, Du. fniezen : Grk. rvéw ‘breathe, blow’, etc., all of imitative orig. Walde- P. 2.85. Falk-Torp 247.
ME snese, NE sneeze, perh. due in part to a misreading of fnese, but sup- ported by new imitative association (or, as Walde-P. 2.551, an inherited form representing *sneus- beside *kneus-, etc., above, 2). NED s.v. sneeze, vb.
4. W. tisian, orig. dub. Formerly (Rhys) considered a loanword fr. Lat. tusstre ‘cough’ (4.53), but rejected by Loth, Mots lat. 211. Perh. an independ- ent imitative formation?
4.55 SWEAT (sb.)
Gtk. 4554, NG Hass Goth. Lith. prakattas Lat. siidor ON  sveiti Lett.  sviedri It, sudore Dan.  sved ChSl.  potit i, ie Sw. _—svelt SCr. — znoj (pot) ae sudor Ris swat Boh. pot eee eae om Sven feet ee Ms, allus Du. —_zweet Skt.  sveda- BR. chtoys Saw sueiz Av. —_-z"atéa-
```


## [2026-09-14T02:10:09.672Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== NYB xwd ==\"; grep -n \"xōd\\|xwd\\|Helm\" NYB_vol2_glossary.txt | head -5\necho \"== PHD hut/barn ==\"; grep -n \"^kadag\\|kadag \\[\" PHD_mackenzie.txt | head -3\necho \"== FRS kaz ==\"; python3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nfor f in ('FRS_pages.txt','FSF_pages.txt'):\n    try: d=open(f,encoding='utf-8').read().split('\\f')\n    except: continue\n    for i,p in enumerate(d):\n        t=clean(p)\n        for w in ('کازه','شنوسه','شنوشه','سکوره'):\n            if w in t: print(f,w,'leaf',i)\nPY"
}
```


### [2026-09-14T02:10:11.445Z] TOOL RESULT

```
== NYB xwd ==
4369:xuat [BNPSH; hwt' 122] himself, herself, itself: (asp 2) ēvak — u Evak kanicak apar našast the one (horse) he mounted him- self, and the other the girl mounted 6!2; ~ karap the karap himself 4812; ; ~ his (her, one’s) own, or proper 100. 12115; -m ~ myself 122; -šān ~ themselves 104, — Av. (1861) z"ató adv. ‘of one’s self, voluntarily’; MPrth wad; MPrs xwd; Paz. z"ad, xud; NP xtad (xod). — Cf x"es.
6211:xwd: xUat
6212:xwd'y, xwd^wy,xwdy?(h): x'atài
== PHD hut/barn ==
3124:kadag [k)tk l ] game, joke.
3125:kadag [ktk l 1M kdg, N kada] house.
9458:kadag                     \5t-S    kabotar
== FRS kaz ==
FRS_pages.txt کازه leaf 447
FRS_pages.txt کازه leaf 451
FRS_pages.txt کازه leaf 473
FRS_pages.txt شنوشه leaf 509
FRS_pages.txt کازه leaf 532
FRS_pages.txt شنوشه leaf 565
```


## [2026-09-14T02:10:14.868Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'PY'\nimport unicodedata\ndef clean(s): return ''.join(c for c in s if unicodedata.category(c) not in ('Cf',))\nd=open('FRS_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,w in ((447,'کازه'),(509,'شنوشه')):\n    t=clean(d[i]); idx=t.find(w)\n    print('=== leaf',i,'===')\n    print(t[max(0,idx-500):idx+500])\nPY"
}
```


### [2026-09-14T02:10:15.977Z] TOOL RESULT

```
=== leaf 447 ===
 ثوت


                                                         هم کسائی گوبد ۷
که به زمعت بیغاره کوثر وتسنیم ]           نی درست و هم فوت بادروزه را




                                                  نعلین باشد [منجيك گوید :

                                    کانع"

خر بشته بود و سأه بان و گروهیگویند صووعه است ؛ نسخه  :کومه که


برکنار بستانها بزنند از بهر سایه و از چوب و از نیکنندکرومی آنرا
                                             صوععه کویند [فردوسی گوید :
1     بر این دشت سك مرد را کازه نت۴            سیه راز بسیاری اندازه تست


                                                           کی گوید :    رود


                                      بتکك (؟) از آن گزیدم اين کازه
     گًعش نك و دخل بی اندازه ؟ 1


                                    شکافه "
                                        زخهٌ مطربان باشد ک[سائی کوید :
        پیری آغوش بازکرده فراخ  .توهمی کوش باشكافهةٌ غوش۱
      : 0 - ۲کازه گروهی گو بندصومعه است    - ۱کذا درچیح اس » دررشیدی  :فام
 و گروی سایه کاه»س ؛ کا
=== leaf 509 ===
                ۲     

                                     کشه

خطکهابدر کشندکشهکویند و کدای را کشه خوانندینی کهمالمردم را
                                            بخود کشد » عسجدی گفت :

                              کشه بر بندی گرفتی در گدابی سرسری

       از تبار خود که دیدی کشه ای بر بنددا
                              شنوهه؟
                                           عطسه باشد» رود کی کوید :

        بنگریزدکس اگزرم آفروشه؛            رفیقا چند کوبی کونشاطت
       چنانچون درد مندان را شنوشه          مرا امروز توبه سود دارد

                                آزکی*
و مدری و نج انگشت افزاری باشد کهگبرزان دانه وکاه را بدان بباد
                           بدهرند تاازهم جدا شود »کسائی گفت :
                            لاون   به
                                فمان                 دوَة َو
                                                        شتش ااز گنواز
 با تبرزین و دبوسی" و رکاب کمری
  -        - ۴در چ و حاشيان      - ۲فقط در چ        - ۱نقط در چ و حاشب ن
 *  -ن(در      اینببت را
```


## [2026-09-14T02:10:35.057Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:19:49.068Z] TOOL CALL #102: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-455.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndoc = {\n \"pdf_page\": 455,\n \"book_page\": 425,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ ENTRY 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Skěu 1, Pneu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *pneu- 'to breathe, snort' (Pokorny 838-839; Watkins/AHD pneu-) blended with PIE *(s)keu-3 / *kseu- 'to sneeze' (Pokorny 953), the blend being *ksneu-s- (*kneus-, *sneus-)\",\n \"note\": \"Both halves of the box are genuine Pokorny headwords and the gloss is right. Pokorny IEW 953 s.v. 'skeu-3, kseu- : to sneeze' says in so many words: 'durch Kreuzung mit pneu- (oben S. 838 f.): *ksneu-s- (*kneus-, *sneus-) in npers. isnosa, asnosa \\\"Niesen\\\"; aisl. hnjosa, mengl. nesen, ahd. niosan; besides mengl. snesen, engl. sneeze' — i.e. Nourai's decision to put the sneeze-root and *pneu- in ONE box is Pokorny's own, not an invention. Walde-Pokorny II 551 says the same and adds that OE fneosan and Du. fniezen arose 'durch Kreuzung mit *pneu-'. The only thing that is Nourai's own is the NUMBER: Pokorny's number for the sneeze root is skeu-3, not 'Skeu 1' (Pokorny's (s)keu-1 is 'to perceive, heed', his (s)keu-2 'to cover' is the root of entry 1 on this very page). Both cited pages are correct: POK:838 = pneu-, POK:953 = skeu-3, kseu-.\",\n \"note_fa\": \"این جعبهٔ ریشه در واقع دو ریشهٔ هندواروپایی آغازین را یکجا آورده است: *pneu- «دمیدن، نفس کشیدن» (پوکورنی ص ۸۳۸–۸۳۹) و *(s)keu-/*kseu- «عطسه کردن» (پوکورنی ص ۹۵۳). این یکجا آوردن ابتکار نورایی نیست؛ خود پوکورنی در ص ۹۵۳ می‌نویسد که از «درآمیختن» این دو ریشه صورت *ksneu-s- پدید آمده و از همان است فارسی išnōsa/ašnōsa «عطسه»، و نیز hnjósa نورس کهن و niosan آلمانی علیا. والده–پوکورنی (جلد ۲ ص ۵۵۱) نیز همین را می‌گوید و می‌افزاید که fnēosan انگلیسی کهن و fniezen هلندی از «درآمیختگی» با *pneu- برآمده‌اند. تنها نکتهٔ نادرست، شمارهٔ ریشه است: شمارهٔ پوکورنی برای ریشهٔ «عطسه» skeu-3 است نه Skeu 1. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n \"sources\": [\n   \"https://www.etymonline.com/word/sneeze\",\n   \"https://www.etymonline.com/word/pneumonia\"\n ],\n \"ref_check\": [\n  {\"ref\": \"POK:838\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt line 68564: 'Root / lemma: pneu- | Meaning: to breathe ... References: WP. II 85 ... Page(s): 838-839'. The entry lists Gr. pneo/pneuma/pnoe and Old Icelandic fnysa, OE fneosan 'sneeze'. Exactly the page Nourai cites.\"},\n  {\"ref\": \"POK:953\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt line 77377: 'Root / lemma: skeu-3, kseu- | Meaning: to sneeze ... through hybridization with pneu- (above S. 838 f.): *ksneu-s- (*kneus-, *sneus-) in npers. isnosa, asnosa \\\"Niesen\\\" ... besides Middle English snesen, engl. sneeze. References: WP. II 85, 551, Trautmann 266. Page(s): 953'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 838-839 (pneu-) and 953 (skeu-3, kseu-)\", \"stance\": \"supports\",\n   \"note\": \"see ref_check; Pokorny himself makes the *pneu- x *kseu- crossing that the chart draws as one root box.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 85 (leaf 89 of WLD_Bd2_pages.txt) and WP II 551 (leaf 555)\", \"stance\": \"supports\",\n   \"note\": \"WP II 85: 'pneu- und andere mit pn- anlautende Sippen fuer \\\"keuchen, atmen\\\", schallmalend'. WP II 551: '3. sqeu-, qseu- schallmalend \\\"niesen\\\" ... *qsneu-s- (qneus-, sneus-) in npers. isnosa, asnosa \\\"niesen\\\"; aisl. hnjosa, mengl. nesen, ahd. niosan (daneben ags. fneosan, nl. fniezen durch Kreuzung mit *pneu-); mengl. snesen, engl. sneeze'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pneu-\", \"stance\": \"supports\",\n   \"note\": \"'pneu-. To breathe. Imitative root. 1. Germanic *fneu- in Old English fneosan, to sneeze: SNEEZE. ... 3. Suffixed form *pneu-mn in Greek pneuma, breath, wind, spirit: PNEUMA, PNEUMATIC... [Pok. pneu- 838.]' Watkins does NOT set up a separate sneeze root, so the *kseu- half comes from Pokorny only.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 4.54 SNEEZE, p.276 (SYN.txt leaf 300)\", \"stance\": \"supports\",\n   \"note\": \"'ON fnysa, OE gefnesan, ME fnese, Du. fniezen : Grk. pneo \\\"breathe, blow\\\", etc., all of imitative orig. Walde-P. 2.85.' Buck also registers the *keu-s-/*kseu- group (ChSl. kychati, Skt. ksu-).\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, entry 'استوسه، شنوسه، اشنوسه، سنوسه (به چم عطسه)', ARY_pages.txt leaf 348 = pdf p.349\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's footnotes tie the Persian word both to PNEIN/PNEUMA and (footnote 3, citing BUCK) to 'SKEU- | KSEU-' — the same double root box as Nourai's, reached independently.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"šonŭšeh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP شنوشه / شنوسه / اشنوسه 'a sneeze' is the direct Iranian continuant of the blended root. Hübschmann (Pers. Studien no. 90, p.59) reconstructs the chain explicitly: pre-Germanic *ksnus- gives a noun *ksnous-so-, which transferred to Iranian yields Iran. *xšnauša- > Pahlavi *šnōšak > NP išnōša; the initial cluster xšn-/šn- was resolved in New Persian by a prothetic vowel (ا-), whence اشنوسه beside شنوسه, and the final -ak of the Middle Persian noun regularly weakens to -a/-eh. Horn (Grundriss no. 90) lists 'ešnōse, išnōse \\\"das Niesen\\\", šenōse, sinōse' and remarks 'Die neupersische Grundform müsste *šenōse sein'; the š/s doublet is the ordinary Persian س~ش interchange, which Borhan-e Qate' itself notes ('در فارسی سین و شین بهم تبدیل می‌یابند'). Pokorny p.953 prints the word as 'npers. išnōsa, ašnōsa'. The Rudaki hemistich quoted in the chart ('مرا امروز توبه سود دارد — چنان چون دردمندان را شنوشه') is the 11th-c. attestation given by Asadi Tusi, Loghat-e Fors s.v. شنوشه.\",\n \"derivation_fa\": \"«شنوشه» (و گونه‌های آن شنوسه، اشنوسه) به معنی «عطسه»، بازماندهٔ راستین همان ریشهٔ درآمیخته است. هوبشمان در «مطالعات فارسی» (شمارهٔ ۹۰، ص ۵۹) زنجیره را چنین بازسازی می‌کند: ایرانی باستان *xšnauša- > فارسی میانه (پهلوی) *šnōšak > فارسی نو išnōša؛ خوشهٔ آغازینِ xšn-/šn- در فارسی نو با واکهٔ افزودهٔ آغازین (الف) ساده شده و پسوند -ak پهلوی نیز به -ه بدل گشته است. هرن (شمارهٔ ۹۰) صورت‌های ešnōse, išnōse, šenōse را می‌آورد و می‌گوید صورت اصیل فارسی نو باید *šenōse باشد. جابه‌جایی «س» و «ش» همان ابدال شناختهٔ فارسی است که خود برهان قاطع هم بدان تصریح کرده است («در فارسی سین و شین بهم تبدیل می‌یابند»). پوکورنی نیز در ص ۹۵۳ همین واژه را با صورت išnōsa/ašnōsa آورده است. بیت رودکی که در نمودار آمده، همان شاهدی است که اسدی طوسی در «لغت فرس» ذیل «شنوشه» نقل کرده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:953\", \"status\": \"supports\",\n   \"note\": \"'through hybridization with pneu- ...: *ksneu-s- (*kneus-, *sneus-) in npers. isnosa, asnosa \\\"Niesen\\\"' (POK_full.txt line 77391). Pokorny names the Persian word itself.\"},\n  {\"ref\": \"BQT:1102\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol. 2, headword شنوسه (BQT_v2_pages.txt form-feed leaf 564): 'شنوسه ... بمعنی شنوسه است که عطسه باشد'. Mo'in's footnote 4 there: 'مخفف اشنوسه ... شهمیرزادی ašinhso ... قس: انگلیسی sneeze، انگلیسی میانه snesen و fnesen، انگلیسی کهن fnēsan ... وبستر ۱۹۴۲. اما دربارهٔ مصراع رودکی «چنان چون دردمندان را شنوشه» در اینجا هم بمعنی عطسه است.' — i.e. exactly Nourai's Persian-to-English link, made by Mo'in himself.\"},\n  {\"ref\": \"BQT:1304\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol. 3 printed p.1304 = pdf p.95 of BQT_v3_picofile.pdf (via BQT_v3_pagemap.json), headword شنوشه: 'بفتح اول ... آن باشد که از راه دماغ ... برآید، آن را بعربی عطسه گویند ... و با سین بی‌نقطه هم درست است چه در فارسی سین و شین بهم تبدیل می‌یابند'. Mo'in's footnote 1: 'مصحف شنوسه < اشنوسه. مؤلف خلط کرده است!' — so BQT gives both spellings, on both pages Nourai cites.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HUB\", \"where\": \"Persische Studien no. 90, p.59 (HUB.txt line 428)\", \"stance\": \"supports\",\n   \"note\": \"'Die germanischen Woerter fuer \\\"Niesen\\\" fuehrt Kluge auf die Wurzeln vorgermanisch ǵnus und ksnus zurueck. Bildet man aus letzterem ein vorgerm. Substantiv *ksnousso- und uebertraegt dies ins Iranische, so erhaelt man iran. *xsnausa- = phl. *snosak = np. isnosa. Leider ist die Wurzel ksnus sehr hypothetisch.' Gives the Middle Persian intermediate.\"},\n  {\"src\": \"HRN\", \"where\": \"Grundriss no. 90 (HRN.txt line 1209, leaf 127)\", \"stance\": \"supports\",\n   \"note\": \"'90. esnose, isnose \\\"das Niesen\\\", senose, sinose ... germ. Vhnus bezw. fnus, vergl. ahd. niosan, mhd. niesen, an. hnjosa, mittelengl. fnesen \\\"niesen\\\", verschieden von mittelengl. snesan, engl. to sneeze (Kluge)'. Horn also prints the Rudaki verse, but in the reading 'cunanci derd-i dendan-ra senose'.\"},\n  {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors s.v. شنوشه (FRS_pages.txt leaf 509)\", \"stance\": \"supports\",\n   \"note\": \"'شنوشه: عطسه باشد، رودکی گوید: مرا امروز توبه سود دارد / چنان چون دردمندان را شنوشه' — the 11th-c. lexicon, with the very reading (دردمندان) that the chart prints.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt leaf 348 (pdf p.349)\", \"stance\": \"supports\",\n   \"note\": \"Persian entry 'استوسه، شنوسه، اشنوسه، سنوسه (به چم عطسه)', citing برهان قاطع ۱۱۰۲/۱۳۰۴, لغت‌نامه دهخدا and فرهنگ معین, with English SNEEZE, OE FNESAN/FNEOSAN, Danish nyse, Dutch niezen as cognates.\"}\n ],\n \"derivation_fa_ok\": True\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"fniu\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The node is right in substance, doubtful in form. Watkins/AHD s.v. pneu- has 'Germanic *fneu- in Old English fneosan, to sneeze', and Pokorny 838 lists the whole Germanic family: ON fnysa 'pant, snort', OE fneosan 'sneeze' (noun fnora 'sneezing'), MHG pfnusen, plus the ablauting series Gmc *fnes-, *fnos-, *fnas- (OE fnaest 'breath', OHG fnastōn 'anhelare') and Gmc *fneh- (OHG fnehan). The change *pn- > *fn- is simply Grimm's Law (PIE *p > Gmc *f), the only Germanic reflex of an initial cluster *pn-. What is odd is the vocalism Nourai prints: no handbook reconstructs '*fniu'; the standard citation forms are Gmc *fneu-/*fneus- (Proto-Germanic verb *fneusaną). 'fniu' is best read as Nourai's own shorthand for AHD's *fneu-, not as a form any source knows.\",\n \"derivation_fa\": \"محتوای این گره درست است ولی صورت آن ساختگی می‌نماید. فرهنگ AHD (واتکینز) ذیل *pneu- می‌آورد: «ژرمنی *fneu- در انگلیسی کهن fnēosan «عطسه کردن»»، و پوکورنی در ص ۸۳۸ همهٔ خانوادهٔ ژرمنی را برمی‌شمارد: fnýsa نورس کهن، fnēosan انگلیسی کهن (اسم fnora «عطسه»)، pfnusen آلمانی میانه، و نیز گونه‌های *fnes-, *fnōs-, *fnas- و *fneh-. تبدیل *pn- آغازین به *fn- همان «قانون گریم» است (پِ هندواروپایی > فِ ژرمنی). اما آوانویسی «fniu» در هیچ مأخذی نیامده؛ صورت متعارف *fneu-/*fneus- (ژرمنی آغازین *fneusaną) است. پس: پیوند درست است اما صورت بازسازی‌شده را باید با احتیاط پذیرفت.\",\n \"sources\": [\"https://www.etymonline.com/word/sneeze\"],\n \"ref_check\": [\n  {\"ref\": \"AHD:1535\", \"status\": \"supports\",\n   \"note\": \"The content is verbatim Watkins: 'pneu-. To breathe. Imitative root. 1. Germanic *fneu- in Old English fneosan, to sneeze: SNEEZE.' (AHD_watkins1985.txt line 864). The page number 1535 belongs to the 1975/76 New College appendix (pp. 1505-1550), which I could not open; the 1985 standalone edition on disk has no page numbers, so only the wording, not the page, is verified.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 838 (pneu-)\", \"stance\": \"supports\",\n   \"note\": \"'Old Icelandic fnysa \\\"pant, sniff, snort\\\", Old English fneosan \\\"sneeze\\\" (fnora \\\"das Niesen\\\"), Middle High German pfnusen ... besides Germanic *fnes-, *fnos-, *fnas-' — the Germanic branch is there, but with -eu-/-e-/-o-/-a- vocalism, never *fniu.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 85 (leaf 89)\", \"stance\": \"supports\",\n   \"note\": \"'Aisl. fnysa \\\"Schnauben\\\", ags. fneosan \\\"niesen\\\" (fnora \\\"das Niesen\\\"; s. auch u. sqeu \\\"niesen\\\"), mhd. pfnusen ... Daneben germ. fnes-, fnos-, fnas-'.\"},\n  {\"src\": \"SKT\", \"where\": \"grep 'fneosan'/'fnese' in SKT.txt\", \"stance\": \"silent\",\n   \"note\": \"Skeat's concise edition has no separate Germanic root entry; nothing found for the reconstructed form.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"sneeze\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English sneeze does continue the Germanic *fneu- word, but not by ordinary sound change: OE fneosan gave ME fnesen, which was reduced to nese by the early 15th c. (the cluster fn- died out in English); late 15th c. scribes, meeting the by-then unfamiliar digraph fn-, misread it as sn- (the two look alike in the secretary hand), and the resulting snese/sneeze was reinforced by the imitative sn- of snore, snort, sniff. The OED/Etymonline account of the misreading is already in Buck (1949, 4.54: 'ME snese, NE sneeze, perh. due in part to a misreading of fnese, but supported by new imitative association') and in Pokorny 953 ('besides Middle English snesen, engl. sneeze'). Walde-Pokorny II 551 offers the alternative that snesen inherits a real variant *sneus- beside *kneus-; either way the word belongs in this box.\",\n \"derivation_fa\": \"واژهٔ انگلیسی sneeze به‌راستی دنبالهٔ همان واژهٔ ژرمنی است، اما نه از راه دگرگونی آوایی منظم: fnēosan انگلیسی کهن به fnesen انگلیسی میانه بدل شد و چون خوشهٔ fn- در انگلیسی از میان رفت، تا اوایل سدهٔ پانزدهم به nese ساده شد؛ سپس کاتبان سدهٔ پانزدهم دونویسهٔ ناآشنای fn- را در دست‌نویس‌ها sn- خواندند و صورت snese/sneeze پدید آمد که با واژه‌های آوایی‌نمای snore و snort و sniff نیز تقویت شد. همین توضیح را باک (۱۹۴۹، بند ۴٫۵۴) و پوکورنی (ص ۹۵۳) آورده‌اند؛ والده–پوکورنی (ج ۲ ص ۵۵۱) احتمال دیگری هم می‌دهد که snesen بازماندهٔ گونهٔ اصیل *sneus- باشد. در هر دو صورت، جای این واژه در همین جعبه درست است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/sneeze\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The chart gives no reference for this node; the parent node's AHD citation covers it ('Germanic *fneu- in Old English fneosan, to sneeze: SNEEZE').\"}\n ],\n \"consulted\": [\n  {\"src\": \"SYN\", \"where\": \"Buck 4.54 SNEEZE, p.276 (SYN.txt leaf 300)\", \"stance\": \"supports\",\n   \"note\": \"'ME snese, NE sneeze, perh. due in part to a misreading of fnese, but supported by new imitative association (or, as Walde-P. 2.551, an inherited form representing *sneus- beside *kneus-). NED s.v. sneeze, vb.'\"},\n  {\"src\": \"KLN\", \"where\": \"grep 'sneeze' in KLN_1971.txt\", \"stance\": \"supports\",\n   \"note\": \"Klein likewise derives sneeze from ME snesen, alteration of fnesen, OE fneosan, of imitative origin, cognate with Gk. pnein.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 953\", \"stance\": \"supports\",\n   \"note\": \"'besides Middle English snesen, engl. sneeze; compare Low German snusen, Danish snuse \\\"schnoben, scent\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"pneuma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. πνεῦμα, -ατος 'wind, breath, spirit' is the regular *-mn̥ noun to the verb πνέω 'blow, breathe' (< *pneu-ō), with the productive Greek suffix -μα/-ματ- forming result-nouns; πνοή 'blast' is the same root with the *-ā suffix. Watkins reconstructs 'suffixed form *pneu-mn in Greek pneuma'. Greek is the only branch that kept the initial cluster πν- intact (Germanic turned *p- into f-, whence fn-), so πνεῦμα and OE fnēosan are the two ends of the same root. The semantic spread 'breath' > 'spirit' is post-classical (Stoic πνεῦμα, then the Septuagint and NT 'Holy Spirit').\",\n \"derivation_fa\": \"واژهٔ یونانی πνεῦμα «باد، دم، روح» اسمِ برساخته از فعل πνέω «دمیدن، نفس کشیدن» است با پسوند زایای یونانی ‎-μα/-ματ-‎ (بازسازی واتکینز: *pneu-mn̥). گونهٔ دیگرِ همین ریشه πνοή «وزش» است. یونانی تنها شاخه‌ای است که خوشهٔ آغازین πν- را دست‌نخورده نگاه داشته؛ در ژرمنی همان *p- بر پایهٔ قانون گریم به f بدل شده و fn- داده است. پس πνεῦμα یونانی و fnēosan انگلیسی کهن دو سرِ یک ریشه‌اند. تحول معنایی «دم» به «روح» متأخر و برآمده از فلسفهٔ رواقی و سپس ترجمهٔ سبعینه و عهد جدید است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/pneumonia\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. pneu-: '2. Greek pnein, to breathe (> pnoia, breathing): APNEA... 3. Suffixed form *pneu-mn in Greek pneuma, breath, wind, spirit: PNEUMA, PNEUMATIC, PNEUMATO-, PNEUMO-. [Pok. pneu- 838.]'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 838\", \"stance\": \"supports\",\n   \"note\": \"'Gr. pneo (pneusai) \\\"blow, pant, gasp, breathe, smell\\\", pneuma \\\"das Wehen, breath, breeze, breath etc.\\\", pnoe \\\"das Wehen, snort\\\"'.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 85 (leaf 89)\", \"stance\": \"supports\",\n   \"note\": \"'Gr. pneo (pneusai) \\\"wehen, keuchen, atmen, riechen\\\", pneuma \\\"das Wehen, Hauch, Atem usw.\\\", pnoe \\\"das Wehen, Schnauben\\\"'.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.v. pneuma / pneumatic\", \"stance\": \"supports\",\n   \"note\": \"Klein derives pneuma from Gk. pneuma 'wind, breath', from pnein 'to breathe, blow', of imitative origin.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"pneumatic, pneumonia\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Half right. PNEUMATIC is exactly what the arrow says: Gk. πνευματικός > Lat. pneumaticus > 16th-c. English pneumatic, a straight derivative of πνεῦμα. PNEUMONIA is not: it is Gk. πνευμονία 'inflammation of the lungs' (c.1600 in English through Latin), to πνεύμων 'lung' — and πνεύμων is itself an ALTERATION of older πλεύμων (Homeric, and the form behind Lat. pulmō), from PIE *pleu- 'to flow, float' ('the floater', because lungs float in water). Watkins puts PNEUMONIA under pleu-, not under pneu-, and Etymonline says πνεύμων was 'altered (probably by influence of pnein \\\"to breathe\\\") from pleumon'. So pneumonia reached its πν- only by secondary contamination with this root; the chart's arrow records the contamination but hides the *pleu- origin.\",\n \"derivation_fa\": \"این گره نیمه‌درست است. واژهٔ pneumatic دقیقاً همان است که نمودار می‌گوید: از πνευματικός یونانی از راه لاتینی pneumaticus به انگلیسی سدهٔ شانزدهم رسیده و مشتق مستقیم πνεῦμα است. اما pneumonia چنین نیست: این واژه از πνευμονία یونانی «آماس شش» است، مشتق از πνεύμων «شش»؛ و خودِ πνεύμων دگرگون‌شدهٔ صورت کهن‌ترِ πλεύμων است (همان که pulmō لاتینی از آن است) که به ریشهٔ هندواروپایی *pleu- «روان بودن، شناور بودن» بازمی‌گردد («شناور»، چون شش در آب می‌شناور می‌ماند). واتکینز نیز pneumonia را ذیل *pleu- آورده است نه ذیل *pneu-. پس π‌ن آغازینِ pneumonia تنها از راه همگونی ثانوی با این ریشه پدید آمده و پیکان نمودار این نکته را پنهان می‌کند: با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/pneumonia\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"partial\",\n   \"note\": \"Watkins 1985 s.v. pneu- lists only 'PNEUMA, PNEUMATIC, PNEUMATO-, PNEUMO-' — PNEUMONIA is absent. It appears instead s.v. pleu- 'to flow': '4. Suffixed form *pl(e)u-mon-, \\\"floater,\\\" lung(s), in: a. Latin pulmo (< *plumones), lung(s): PULMONARY; b. Greek pleumon, pneumon, lung: PNEUMONIA, PNEUMONIC.' So Nourai's own reference contradicts the pneumonia half of this node.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pleu- and s.v. pneu-\", \"stance\": \"contradicts\",\n   \"note\": \"see ref_check — PNEUMONIA is filed under pleu-.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.v. pneumonia / pneumon-\", \"stance\": \"partial\",\n   \"note\": \"Klein gives Gk. pneumon 'lung', for pleumon, refashioned after pnein 'to breathe' — i.e. the *pleu- origin with secondary contamination.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 837 (pl(e)u-mon-) vs 838 (pneu-)\", \"stance\": \"contradicts\",\n   \"note\": \"Pokorny keeps 'pl(e)u-mon- \\\"Lunge\\\"' (p.837, s.v. pleu-) apart from pneu- (p.838); the lung word is not in the pneu- entry.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ ENTRY 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Skeu 2, Sku, Keu 3, Kŭ 3; Skŭr, Ku-z-dho, Kut-no\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(s)keu- / *(s)kewH- 'to cover, conceal' (Pokorny 951-953 '(s)keu-2 bedecken, umhüllen'; Watkins/AHD (s)keu-), with the extensions *(s)keu-t- (Lat. cutis, *kut-no- > cunnus), *(s)keu-k-, *(s)keu-s- (*kus-dho- > Gmc *huzdam), and the lengthened *skūr- 'cover, shell'\",\n \"note\": \"Every label in this crowded box is a real headword somewhere. 'Skeu 2' = Pokorny's (s)keu-2 'bedecken, umhüllen', pp. 951-953 (= Walde-Pokorny II 546-552 '(s)qeu-'), which is where Nourai's POK:952,953 point and where AHD sends the reader ('[Pok. 2. (s)keu- 951.]'). 'Kut-no' is Walde-Pokorny's and Watkins's *kut-no- (Lat. cunnus < *kut-nos, WP II 549); 'Ku-z-dho' is their *kus-dho-/*kuz-dho- (Gmc *huzdam 'hoard', Gk. kusthos); 'Skŭr' is S. E. Mann's own headword 'skūr- \\\"cover, shell\\\"' at IEC 1193, which is exactly the page cited and which is also where the Persian سکوره of node #11 comes from. 'Keu 3, Kŭ 3, Sku' correspond to the *keu-/*kū- 'to vault, be hollow' family that Pokorny folded into (s)keu-2 (Av. kusra-, npers. kūs, Skt. kukṣi-). One caveat worth recording: Walde-Pokorny II 546 expressly warn that equating (s)qeu- 'cover' with the root qeu- 'wölben, hohl' 'verdient stärkste Skepsis' — so the merger that Nourai's box performs is Pokorny-1959's, not the unanimous view. The printed page runs two citations together as 'IEC:1193AHD:1540' (missing semicolon); the extraction reproduces the page faithfully.\",\n \"note_fa\": \"همهٔ برچسب‌های این جعبهٔ پرازدحام، سرواژه‌های واقعی‌اند. «Skeu 2» همان (s)keu-2 پوکورنی است به معنی «پوشاندن، در بر گرفتن» (صص ۹۵۱–۹۵۳؛ برابر با (s)qeu- در والده–پوکورنی ج ۲ صص ۵۴۶–۵۵۲) و ارجاع‌های POK:952,953 دقیقاً به همان‌جاست. «Kut-no» همان *kut-no- است که cunnus لاتینی از آن است (والده–پوکورنی ج ۲ ص ۵۴۹)؛ «Ku-z-dho» همان *kus-dho- است که *huzdam ژرمنی («گنج») و κύσθος یونانی از آن‌اند؛ و «Skŭr» سرواژهٔ مستقل مان (Mann) در فرهنگ تطبیقی هندواروپایی ص ۱۱۹۳ است با معنی «پوشش، پوسته» که «سکورهٔ» فارسیِ گرهٔ ۱۱ نیز از همان‌جا آمده است. «Keu 3، Kŭ 3، Sku» نیز به خانوادهٔ *keu-/*kū- «گود شدن، تهی» بازمی‌گردد که پوکورنی آن را در همان مدخل (s)keu-2 گنجانده است (kusra- اوستایی، kūs فارسی، kukṣi- سنسکریت). یک هشدار را باید ثبت کرد: والده–پوکورنی در ج ۲ ص ۵۴۶ به‌صراحت می‌گوید یکی‌دانستن (s)qeu- «پوشاندن» با ریشهٔ qeu- «گود کردن» «سزاوار بیشترین تردید» است؛ پس این ادغام، دیدگاه پوکورنیِ ۱۹۵۹ است نه اجماع. در چاپ کتاب دو ارجاع بی‌نقطه‌ویرگول به هم چسبیده‌اند («IEC:1193AHD:1540») که خطای حروف‌چینی خود کتاب است و استخراج داده درست انجام شده. در مجموع ریشه و معنای آن درست است.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-\",\n   \"https://en.wiktionary.org/wiki/cutis\"\n ],\n \"ref_check\": [\n  {\"ref\": \"POK:952\", \"status\": \"supports\",\n   \"note\": \"Pokorny's entry '(s)keu-... bedecken, umhuellen' runs 951-953 (POK_full.txt line ~76700-76857, 'Page(s): 951-953'); p.952 carries the dental and guttural extensions, including 'unclear is Latin cudo \\\"helmet from fell\\\"; in the meaning near stands Avestan xaoda-, ap. xauda- \\\"hat, Kappe; helmet\\\"' and 'npers. kus \\\"vulva\\\"; Avestan kusra- \\\"sich woelbend, hohl\\\"'.\"},\n  {\"ref\": \"POK:953\", \"status\": \"supports\",\n   \"note\": \"Same entry, final page: the s-extension (s)keu-s- with 'Modern High German dial. hosen \\\"husk, pod\\\", Old English hosa \\\"Strumpf, husk\\\" ... Gothic Old Icelandic Old English Old Saxon Old High German hus \\\"house\\\" ... Gothic huzd, ... Old High German hort \\\"treasure\\\" (*kuz-dho- = gr. kusthos)'. 'References: WP. II 546 ff.'\"},\n  {\"ref\": \"IEC:1193\", \"status\": \"supports\",\n   \"note\": \"Mann, IEC (IEC.txt leaf 659, printed p.1193): 'skūr- \\\"cover, shell\\\". Cf. skuu. WP II, 548. Per. sukūre, s. \\\"earthen dish\\\"; Lat. cf. ob-scūrus, adj. \\\"dark\\\"; OHG skūra, f. \\\"barn\\\"; MHG schūr, sm. \\\"shelter, protection\\\"; Du. schuur, f., LG schür, n. id.; ON skúr, s. \\\"penthouse; shell\\\"; Li. dial. skūrà, f. \\\"fur, pelt\\\".' Exactly the 'Skŭr' label and the Persian word of node #11.\"},\n  {\"ref\": \"AHD:1540\", \"status\": \"supports\",\n   \"note\": \"Content verified in Watkins 1985 s.v. (s)keu-: 'To cover, conceal. Zero-grade form *(s)ku-... 2b. suffixed form *sku-ro- in Latin obscurus...; 3b. suffixed form *ku-ti- in Latin cutis, skin...; 3d. suffixed form *ku-to- in Greek kutos, a hollow, vessel; 4a. Germanic *huson- in Old English hosa...; 4b. suffixed form *kus-dho- (or *kudh-to-) in Germanic *huzdam...; 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva. [Pok. 2. (s)keu- 951.]' The page 1540 belongs to the 1975/76 New College appendix, which I could not open; only the wording is verified.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 951-953\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 546-552 (WLD_Bd2_pages.txt leaves 550-556)\", \"stance\": \"partial\",\n   \"note\": \"The parent article: '(s)qeu- \\\"bedecken\\\"', with Lat. obscurus (p.547), npers. kūs and av. kusra- (p.548), an. hūd/ags. hȳd/ahd. hūt and ahd. hutta (p.549), lat. cutis and cunnus < *qut-nos (p.549). But p.546 warns: 'Die Gleichsetzung mit Wz. qeu- \\\"woelben, hohl\\\" ... verdient staerkste Skepsis' — precisely the merger Nourai's box performs.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)keu-\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann pp. 594-595 (kut- 6, kut- 7) and 1193 (skūr-)\", \"stance\": \"supports\",\n   \"note\": \"'kut- (7) (kūtis, os, iom) \\\"container, skin\\\" ... Gk. kútos, n. \\\"hollow, belly, jar, body\\\" ... Lat. cutis, f. ... OHG hūt ... OE hȳd ... ON húð'; and skūr- at 1193.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.v. cutis, obscure, hose, hut, scum\", \"stance\": \"supports\",\n   \"note\": \"Klein consistently refers all of these to 'I.-E. base *(s)qeu-, *(s)qewa-, \\\"to cover\\\"' and its extensions *(s)qeut-, *(s)qeudh-.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"xaôda, xaudâ; tigra-xaudâ\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms and their meanings are beyond doubt. Bartholomae, Altiran. Wb. col. 476: 'j. xaoδa- (, p. xauda-) m. \\\"Hut, Kappe, Helm\\\"'; Kent, Old Persian Lexicon (p.181) 'xaudā- sb. \\\"hat, cap\\\": Av. xaoδa-, Oss. xodä, NPers. xōd, Arm. (borrowed) xoir \\\"headband\\\"', and 'tigraxaudā- adj. \\\"wearing the pointed cap\\\" ... tigra- \\\"pointed\\\" + xauda- \\\"cap\\\"', the epithet of the Sakā tigraxaudā of DB 5.22, DNa 26, DSe 25, XPh 27 — the 'pointed-hat Scythians' shown with the conical cap on the Bisotun relief (Skunkha). Avestan xaoδa- has the regular Younger-Avestan -au- > -ao- before a consonant, Old Persian keeps -au-. What is doubtful is the ROOT. Pokorny 952 mentions xaoδa-/xauda- only as a semantic neighbour of the obscure Latin cudo ('unclear is Latin cudo \\\"helmet from fell\\\" (loanword?); in the meaning near stands Avestan xaoδa-') — he does not derive it from *(s)keu-. Modern scholarship puts it under a different root, PIE *kadʰ- 'to shelter, cover' (Watkins: 'kadh-. To shelter, cover ... Old English hatt, hat: HAT ... hōd, hood: HOOD'), which is what Wiktionary gives for the whole Iranian family.\",\n \"derivation_fa\": \"صورت‌ها و معانی این گره بی‌چون‌وچرا درست‌اند. بارتولومه در «فرهنگ ایرانی باستان» (ستون ۴۷۶) می‌آورد: «اوستایی نو xaoδa- (پارسی باستان xauda-) نرینه: کلاه، کلاهخود»؛ و کنت در واژه‌نامهٔ پارسی باستان (ص ۱۸۱): «xaudā- اسم «کلاه»: اوستایی xaoδa-، آسی xodä، فارسی نو xōd، ارمنیِ وام‌گرفته xoir»، و نیز «tigraxaudā- صفت «دارندهٔ کلاه نوک‌تیز»» که لقب «سکاهای تیزخود» در کتیبه‌های بیستون (۵٫۲۲) و نقش رستم (DNa ۲۶) است و پیکرهٔ سکونخا بر نگارهٔ بیستون همان کلاه مخروطی را نشان می‌دهد. دوگانگی xaoδa-/xauda- نیز قاعده‌مند است: در اوستایی نو ‎au‎ پیش از همخوان به ‎ao‎ بدل می‌شود و پارسی باستان ‎au‎ را نگاه می‌دارد. آنچه جای تردید دارد ریشه است: پوکورنی در ص ۹۵۲ تنها می‌گوید که xaoδa- «از نظر معنایی نزدیک» به cudo لاتینی است و آن را از *(s)keu- نمی‌گیرد؛ پژوهش امروزی (واتکینز، ویکی‌واژه) این خانواده را به ریشهٔ دیگری، *kadʰ- «پوشاندن، پناه دادن» (همان که hat و hood انگلیسی از آن است) بازمی‌گرداند. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%AF\"],\n \"ref_check\": [\n  {\"ref\": \"POK:952\", \"status\": \"partial\",\n   \"note\": \"Pokorny does have the words on that page, but only as a semantic parallel, not as a derivative: 'unclear is Latin cudo, -onis \\\"helmet from fell, fur\\\" (loanword?); in the meaning near stands Avestan xaoδa- m., ap. xauda- \\\"hat, Kappe; helmet\\\"' (POK_full.txt, entry '(s)keu-', line ~76794).\"},\n  {\"ref\": \"KNT:180\", \"status\": \"supports\",\n   \"note\": \"Kent's Lexicon, x- section: 'xaudā- sb. \\\"hat, cap\\\" ($100, $143.IV): Av. xaoδa-, Oss. xodä, NPers. xōd, Arm. (borrowed) xoir \\\"headband\\\"' and 'tigraxaudā- adj. \\\"wearing the pointed cap\\\" ... \\\"tigra- \\\"pointed\\\" + xauda- \\\"cap\\\"'. In the scan (KNT.txt) these sit on form-feed records 204 and 210; the page number printed on record 204 is 181, so the x- section spans pp.180-181 — Nourai's 180 is right to within one page. Kent offers no PIE root.\"},\n  {\"ref\": \"BQT:785\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' printed p.785 (BQT_v2_pages.txt form-feed leaf 243; leaf 240 carries the page number ۷۸۲), headword خود. Mo'in's etymological footnote 1 there reads 'پارسی باستان xauda ... (خود سر تیز) اشپیگل ص ۱۲۲۰ ... معرب آن خوذة' — i.e. exactly Old Persian xauda- and tigra-xauda-, with the Arabized form خوذة.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. 476 (BRT.txt line 10529)\", \"stance\": \"supports\",\n   \"note\": \"'j. xaoδa- (, p. xauda-) m. \\\"Hut, Kappe Helm\\\".' Bartholomae also has the compounds ayō.xaoδa- 'with a metal helmet' (col. 161), zaranyō.xaoδa- 'with a golden helmet' and urvi.xaoδa- 'whose helmet runs up into a point'.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent §100 and Lexicon s.v. xaudā-, tigraxaudā-\", \"stance\": \"supports\",\n   \"note\": \"'§100. PAR. kh seems to appear in a few words ...: xauda- \\\"cap\\\", also in tigraxauda- \\\"wearing the (pointed cap)\\\"'.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 952\", \"stance\": \"partial\", \"note\": \"see ref_check — semantic neighbour only.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kadh-\", \"stance\": \"contradicts\",\n   \"note\": \"'kadh-. To shelter, cover. 1. Suffixed zero-grade form *kod-u- in Germanic *haduz ... Old English hatt, hat: HAT. 2. Basic form *kadh- in: a. Germanic *hoda in Old English hod, hood: HOOD ...' [Pok. kadh- 516] — the root to which the Iranian helmet word is normally assigned, and it is NOT this box.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"xŭd\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP خود xūd/xōd 'helmet' (modern کلاه‌خود 'helmet', lit. 'helmet-cap') continues Old Iranian *xauda- through Middle Persian xōd — but by an irregular road, and that irregularity is itself an old crux. Hübschmann (Pers. Studien no. 512, p.59) points it out: 'Np. xōi \\\"Helm\\\" ist die lautgesetzliche Form, aber nicht belegt; das gebräuchliche xōd \\\"Helm\\\" ist schwerlich aus dem Arab. xūδat zurückentlehnt' — i.e. intervocalic Old Iranian *-d-/-δ- should have given -y- (so *xōi), and the preserved -d suggests a Parthian (Arsacid) rather than Persid transmission; Hübschmann adduces Armenian loan xoir 'diadem', whose -r for Arsacid δ makes the same point. Modern Wiktionary states it outright: 'From Middle Persian xōd \\\"helm\\\", borrowed from Parthian *xōδ \\\"helmet\\\"'. The word is well attested from Ferdowsi on (Hübschmann cites Šāhnāme I 23 v.9 and the rhyme with durōd I 170). Nourai's derivation is thus right as to the Iranian chain; it is the PIE root box that is questionable, as at node #1 (modern handbooks: *kadʰ-, not *(s)keu-).\",\n \"derivation_fa\": \"«خود» (کلاه‌خود) در فارسی نو دنبالهٔ ایرانی باستان *xauda- است از راه فارسی میانهٔ xōd؛ اما این تحول بی‌قاعده است و همین بی‌قاعدگی از دیرباز مسئله بوده است. هوبشمان (مطالعات فارسی، شمارهٔ ۵۱۲، ص ۵۹) می‌نویسد: «صورت قاعده‌مند فارسی نو xōi است اما گواهی نشده؛ و xōd رایج نیز به‌دشواری می‌تواند وام‌گیری دوباره از xūδat عربی باشد». به بیان دیگر، ‎-d/-δ-‎ میان دو واکه در فارسی میانهٔ جنوبی باید به ‎-y-‎ بدل می‌شد (یعنی *خوی)، و ماندنِ «د» نشان می‌دهد که واژه از راه پارتی (اشکانی) به فارسی رسیده است؛ وام‌واژهٔ ارمنی xoir «تاج‌بند» نیز با «ر» در برابر δ اشکانی همین را گواهی می‌کند. ویکی‌واژه نیز صریح می‌گوید: «از فارسی میانهٔ xōd، وام‌گرفته از پارتی *xōδ». واژه از شاهنامه به‌بعد فراوان گواهی شده است. پس زنجیرهٔ ایرانیِ نورایی درست است و تنها جای‌دهیِ آن زیر ریشهٔ *(s)keu- جای تردید دارد (ریشهٔ متعارف امروزی *kadʰ- است).\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%AF\"],\n \"ref_check\": [\n  {\"ref\": \"POK:952\", \"status\": \"partial\",\n   \"note\": \"Pokorny names the Avestan/Old Persian words on that page but no New Persian reflex, and only as a semantic neighbour of Lat. cudo; the NP form is not in Pokorny.\"},\n  {\"ref\": \"KNT:180\", \"status\": \"supports\",\n   \"note\": \"Kent s.v. xaudā- expressly gives the modern continuant: '... Oss. xodä, NPers. xōd, Arm. (borrowed) xoir \\\"headband\\\"' (KNT.txt record 204).\"},\n  {\"ref\": \"BQT:785\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' p.785 s.v. خود: 'بمعنی تاج و مغفر باشد' with Mo'in's footnote 'پارسی باستان xauda ... معرب آن خوذة' — headword, sense 'helmet' and Old Persian etymology all on the cited page.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Grundriss no. 512 (HRN.txt line 4620, leaf 127)\", \"stance\": \"supports\",\n   \"note\": \"'512. xōδ \\\"Helm\\\", xōd. ap. xauda- \\\"Helm\\\"; aw. xaoδa-. arab. LW. xūδat \\\"Helm\\\"; Sifγ. xōl; oss. d. xodä, i. xūd.'\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien no. 512, p.59 (HUB.txt line 2018)\", \"stance\": \"partial\",\n   \"note\": \"'Np. xōi \\\"Helm\\\" ist die lautgesetzliche Form, aber nicht belegt; das gebraeuchliche xōd \\\"Helm\\\" ist schwerlich aus dem Arab. xūδat zurueckentlehnt. Dazu arm. xoir \\\"Kopfband, Diadem\\\".' Hubschmann accepts the descent but flags the irregular -d.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt / PHD_mackenzie.txt)\", \"stance\": \"silent\",\n   \"note\": \"MacKenzie has no xōd; his Pahlavi word for 'helmet' is targ [tlg | N ~] and, in the addenda, sārwār [s'lw'l]. The MP xōd of the chain is therefore a reconstruction from NP + Parthian, not a MacKenzie entry.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n   \"note\": \"The glossary has xwat/xuat 'self' (line 4369) but no xwd 'helmet'; nothing bearing on this node.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"kâz\",\n \"verdict\": \"plausible\",\n \"derivation\": \"کاز / کازه / کاژ / کاژه 'a hut of wood and reeds built beside a field or orchard; an arbour, a hermit's cell' is a real and old word — Asadi Tusi's Loghat-e Fors (11th c.) already defines کازه as 'کومه که بر کنار بستانها بزنند از بهر سایه و از چوب و از نی کنند، گروهی آنرا صومعه گویند' and cites Ferdowsi. Its history is a loan, not an inheritance: Gharib's Sogdian dictionary no. 4682, p.187, has k'z'kh (kāzak, kāze) 'little house, hut' (VJ 952; Henning, Mittelir. 126), with no. 4650 k'n'kh cross-referring to it on the same page; Henning ('Two Central Asian Words', TPS 1945, p.158 n.3) read the Sogdian word as kāz and equated it with Persian kāza — which is precisely the claim the chart's NOTE attributes to BQT, and which Mo'in prints verbatim in his footnote to Borhan p.1562. Wiktionary accordingly says Persian کازه was 'Borrowed from Sogdian kʾzʾk \\\"little house\\\"', cognate with Khotanese khāśā̮na- 'abode'. So the Sogdian link is confirmed; what is NOT supported by any source consulted is the further step of hanging the word on PIE *(s)keu- 'to cover'. Bailey (DKS s.v. khasána-) refers NPers. kāz 'hut', kāzah 'house' to a base kas-/khas-, a different etymon. Hence: word real, Sogdian tie confirmed, root assignment Nourai's own.\",\n \"derivation_fa\": \"«کاز / کازه / کاژ / کاژه» به معنی «کلبه‌ای از چوب و نی که کشاورزان و پالیزبانان کنار کشت می‌سازند؛ آلاچیق؛ صومعه» واژه‌ای کهن و راستین است: اسدی طوسی در «لغت فرس» (سدهٔ پنجم) ذیل کازه می‌نویسد «کومه که بر کنار بستانها بزنند از بهر سایه و از چوب و از نی کنند، گروهی آنرا صومعه گویند» و شاهدی از فردوسی می‌آورد. اما تاریخ آن تاریخ وام‌گیری است نه میراث: در «فرهنگ سغدی» قریب (شمارهٔ ۴۶۸۲، ص ۱۸۷) واژهٔ سغدی k'z'kh (kāzak, kāze) به معنی «خانهٔ کوچک، کلبه» ثبت شده و هنینگ در «دو واژهٔ آسیای میانه» (ص ۱۵۸، پانوشت ۳) آن را kāz خوانده و برابر «کازهٔ» فارسی دانسته است — همان نکته‌ای که یادداشت نمودار به برهان قاطع نسبت می‌دهد و معین در حاشیهٔ ص ۱۵۶۲ عیناً آورده است. ویکی‌واژه نیز «کازه» را وام‌واژه‌ای از سغدی kʾzʾk می‌داند، هم‌ریشه با khāśā̮na- ختنی «جایگاه». پس پیوند سغدی تأیید می‌شود، ولی هیچ مأخذی این واژه را به ریشهٔ هندواروپایی *(s)keu- «پوشاندن» نمی‌بندد؛ بیلی نیز kāz/kāzah فارسی را به ستاک kas-/khas- بازمی‌گرداند. بنابراین: واژه و پیوند سغدی درست، و جای‌دهی زیر این ریشه از آنِ خود نورایی است — با احتیاط پذیرفتنی.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B2%D9%87\",\n   \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B2%D9%87/\"\n ],\n \"ref_check\": [\n  {\"ref\": \"BQT:1562\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' printed p.1562 = pdf p.355 of BQT_v3_picofile.pdf (via BQT_v3_pagemap.json): headwords کاز، کاژ، کازرون، کازه, with Mo'in's footnote 4: 'کاز (هم.): در سغدی کلمه‌ای است که آن را k'zk'kh خوانده‌اند ... (خانه‌ای در صحرا). هنینگ گوید می‌توان آن را kāz خواند معادل کازهٔ kāza فارسی. Henning, Two Central Asian Words, p.158, note 3.' The Molavi verse of the chart is footnote 5 on the same page ('امید وصل تو نیست در وهم من که آخر / در کازهٔ گدایان سلطان چگونه گنجد ... مولوی بلخی، فرهنگ نظام'). The chart's NOTE is an accurate report of this footnote.\"},\n  {\"ref\": \"SOD:187\", \"status\": \"supports\",\n   \"note\": \"Gharib, Sogdian Dictionary, printed p.187 (SOD_pages.txt lines 17035-17060): entry '4650 k'n'kh B ⇒ k'z'kh' and entry '4682 k>z>kh B — kazak, kaze (k'n'kh) — little house, hut — VJ 952; Hen. Mittelir. 126'. Nourai's page number is exact.\"},\n  {\"ref\": \"MON:2821\", \"status\": \"partial\",\n   \"note\": \"Mo'in's Farhang-e Farsi does have کازه — 'آلاچیق، کلبه؛ صومعه؛ خانه و منزل' (abadis.ir, فرهنگ معین section) — but with NO origin bracket and no etymology, so it supports the word and its sense, not the derivation. The 6-vol pagination (2821) cannot be checked: only the 2-vol Adena reprint is on disk and vajehyab/abadis give no page numbers.\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib no. 4682, p.187\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors s.v. کازه (FRS_pages.txt leaf 447)\", \"stance\": \"supports\",\n   \"note\": \"'کازه: ... کومه که بر کنار بستانها بزنند از بهر سایه و از چوب و از نی کنند و گروهی آنرا صومعه کویند [فردوسی گوید:] بر این دشت سک مرد را کازه نیست' — earliest Persian lexicographic attestation.\"},\n  {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dict. of Khotan Saka s.v. khasána- (ISS_alt_DKS.txt line 1698)\", \"stance\": \"contradicts\",\n   \"note\": \"'For khasána- either khata- with suffix -ana- ... to base kas- or khas- as in N.Pers. kāz \\\"hut\\\", kāzah \\\"house\\\", Armen. lw kʿazm \\\"arrangement\\\"' — Bailey assigns the Persian word to a base kas-/khas-, not to *(s)keu-.\"},\n  {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. کازه\", \"stance\": \"partial\",\n   \"note\": \"'(زِ) (اِ.) ۱- آلاچیق، کلبه ۲- صومعه ۳- خانه و منزل' — sense confirmed, no etymology.\"},\n  {\"src\": \"HRN\", \"where\": \"grep 'kaz'/'kaza' in HRN.txt\", \"stance\": \"silent\",\n   \"note\": \"Horn's Grundriss has no entry for kāz/kāza; the word is absent from his numbered list.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"kutos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. κύτος n. 'hollow, vessel, urn; the trunk of the body' is the *-to- formation on the zero grade *kut- of the root, and it is the Greek twin of Lat. cutis: Watkins gives 'suffixed form *ku-to- in Greek kutos, a hollow, vessel: -CYTE, CYTO-', and Pokorny 952 lists it under the dental extension '(s)keu-t-' beside σκῦτος 'skin, leather', κυτίς 'box, basket' and κύσθος. Mann prints it at exactly the page Nourai cites. The semantics run 'what covers' > 'skin, husk' > 'the thing skinned, container, hollow, body cavity', which is why the same root gives both 'hide' and 'vessel'; the modern biological -cyte/cyto- (Schwann's Zelle rendered κύτος) is a 19th-c. revival of the 'container' sense.\",\n \"derivation_fa\": \"واژهٔ یونانی κύτος «گودی، ظرف، خمره؛ تنه» ساختِ ‎-to-‎ بر پایهٔ درجهٔ صفرِ *kut- همین ریشه است و همزادِ یونانیِ cutis لاتینی به‌شمار می‌رود. واتکینز می‌نویسد: «صورت پسوندی *ku-to- در κύτος یونانی «گودی، ظرف»» و پوکورنی نیز آن را در ص ۹۵۲ زیر گسترشِ دندانیِ (s)keu-t- در کنار σκῦτος «چرم، پوست»، κυτίς «صندوقچه» و κύσθος آورده است. مان (Mann) نیز دقیقاً در همان صفحه‌ای که نورایی ارجاع داده آن را ثبت کرده است. تحول معنایی چنین است: «آنچه می‌پوشاند» > «پوست، پوسته» > «آنچه پوست از آن گرفته‌اند؛ ظرف، گودی، حفرهٔ تن»؛ و همین است که یک ریشه هم «پوست» می‌دهد و هم «ظرف». پسوند زیست‌شناختیِ ‎-cyte/cyto-‎ نیز احیای همان معنای «ظرف» در سدهٔ نوزدهم است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-\"],\n \"ref_check\": [\n  {\"ref\": \"IEC:595\", \"status\": \"supports\",\n   \"note\": \"Mann, IEC printed p.595 (IEC.txt leaf 337): 'kut- (7) (kūtis, os, iom) \\\"container, skin\\\". Cf. kut- (6). Arm. cf. ktit ... Gk. kútos, n. \\\"hollow, belly, jar, body\\\"; kutis, f. \\\"box, basket\\\"; ... Lat. cutis, f. ... OHG hūt ... OE hȳd, f. id.; ON húð ... W cwd \\\"pouch\\\"'. The gloss 'hollow, belly, body' is copied straight from Mann.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 952 ((s)keu-t-)\", \"stance\": \"supports\",\n   \"note\": \"'Gr. skutos n. \\\"skin, leather\\\", ... kutos n. \\\"sleeve, wrapping, skin\\\" and \\\"vessel, Urne, cavity\\\", kutis \\\"small Kasten, Buechse\\\"'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)keu-\", \"stance\": \"supports\",\n   \"note\": \"'3d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -CYTE, CYTO-.'\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 549 (leaf 553)\", \"stance\": \"supports\",\n   \"note\": \"The same Greek group (κύσθος, κύτος) is listed in the (s)qeu- article beside lat. cutis and cunnus.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.v. cutis\", \"stance\": \"supports\",\n   \"note\": \"'L. cutis \\\"skin\\\" ... fr. I.-E. base *(s)qeut \\\"to cover\\\" ... Cp. also cyst, -cyte, ecu, escutcheon, esquire, scudo, scum, Scutellaria, scutellum, scuttle, scutum, syncytium.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"kusra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan kusra- is genuine and is exactly where Nourai puts it. Bartholomae, Altiran. Wb. col. 476: 'j. kusra- Adj. \\\"sich wölbend, hohl\\\"', attested at Yasna 10.11, with the compounds vi-kusra- and han-kusra- 'arching apart / arching together' (cols. 1436, 1770). Pokorny, in the guttural extension '(s)keu-k-' of the (s)keu- article (p.952), puts it in this family: 'Avestan kusra- \\\"sich wölbend, hohl\\\", vi-kusra-, han-kusra-', alongside Skt. kukṣi- 'belly, womb, cavity' and npers. kūs. The form is *kus-ra-, a -ra- adjective on the zero grade. One small correction: kusra- is an ADJECTIVE 'arching, hollow', not the noun 'vault, hole, cavity' that the chart glosses it with — the noun sense is Nourai's paraphrase.\",\n \"derivation_fa\": \"واژهٔ اوستایی kusra- اصیل است و جای آن در همین خانواده درست است. بارتولومه در ستون ۴۷۶ می‌نویسد: «اوستایی نو kusra- صفت: گنبدی‌شونده، تهی/گود»، گواهی‌شده در یسنا ۱۰٫۱۱، همراه با ترکیب‌های vi-kusra- و han-kusra- «از هم گشاینده / بر هم آورنده» (ستون‌های ۱۴۳۶ و ۱۷۷۰). پوکورنی نیز در بخش گسترشِ کامیِ (s)keu-k- از همان مدخل (ص ۹۵۲) آن را در کنار kukṣi- سنسکریت «شکم، زهدان، گودی» و kūs فارسی آورده است. ساخت واژه *kus-ra- است، یعنی صفتی با پسوند ‎-ra-‎ بر درجهٔ صفر ریشه. یک نکتهٔ کوچک: kusra- صفت است («گنبدی، گود») نه اسم؛ معنای «طاق، سوراخ، حفره» که در نمودار آمده تعبیر خود نورایی است. در مجموع ادعا درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:953\", \"status\": \"partial\",\n   \"note\": \"Pokorny does list it — 'Avestan kusra- \\\"sich wolbend, hohl\\\", vi-kusra-, han-kusra- \\\"sich auseinander-, zusammen-wolbend\\\"' — but in the guttural-extension section '(s)keu-k-', which on the printed 1959 page falls on p.952; the article as a whole is 'Page(s): 951-953'. Content supports the node; the page number is one off.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. 475-476 (BRT.txt line 9679)\", \"stance\": \"partial\",\n   \"note\": \"'j. kusra- Adj. \\\"sich woelbend, hohl\\\": ... Y. 10.11' — the entry confirms form and attestation, but glosses it as an adjective, not the noun 'vault, hole, cavity' of the chart.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 548 (leaf 552)\", \"stance\": \"supports\",\n   \"note\": \"'av. kusra- \\\"sich woelbend, hohl\\\", vikusra-, hankusra- \\\"sich auseinander-, zusammenwoelbend\\\" (Geldner Metr. 159, Bartholomae IF. 1, 491 f., Airan. Wb. 475, 1436, 1770)'.\"},\n  {\"src\": \"AVG\", \"where\": \"grep 'kusra' in AVG.txt (Jackson, Avesta Grammar)\", \"stance\": \"silent\",\n   \"note\": \"Jackson's grammar does not cite the word; nothing for or against.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"kos\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Persian word is real and it does belong to this family — but not as a descendant of Avestan kusra-, which is how the chart draws it. Pokorny 952 and Walde-Pokorny II 548 list 'npers. kūs \\\"weibliche Scham\\\"' and 'av. kusra-' side by side as co-ordinate members of the guttural extension *(s)keu-k-, together with Skt. kukṣí- 'belly, womb, cavity', Lith. kūšỹs / Latv. kūsis 'pubic hair' (< *kuk̑i- or *kuksi-) — never one from the other; kusra- is a -ra- adjective and cannot be the source of a noun kos. Wiktionary goes further and takes کس straight back to PIE *kuḱis '(female) pubic hair; vulva' (cognates: Northern Kurdish quz, Hawrami kʷsî, Lith. kūšỹs, Latv. kūsis), 'possibly a euphemism from the older meaning \\\"belly\\\"' preserved in Skt. kukṣí-, Sogd. qwšy 'side of the body' and Pers. کشتی 'girdle'. Note also the vowel: Pokorny and WP write npers. kūs, while the living word is kos — Nourai's kos is the correct modern form. So: right family, wrong immediate parent.\",\n \"derivation_fa\": \"این واژهٔ فارسی راستین است و به همین خانواده تعلق دارد، اما نه چنان‌که نمودار می‌کشد، یعنی نه بازماندهٔ kusra- اوستایی. پوکورنی (ص ۹۵۲) و والده–پوکورنی (ج ۲ ص ۵۴۸) «kūs فارسی نو «شرمگاه زن»» و «kusra- اوستایی» را در کنار هم و هم‌رتبه، ذیل گسترشِ کامیِ *(s)keu-k- می‌آورند، همراه با kukṣí- سنسکریت «شکم، زهدان، گودی» و kūšỹs لیتوانیایی و kūsis لتونیایی «موی زهار» — نه یکی را از دیگری. افزون بر آن، kusra- صفت است و نمی‌تواند سرچشمهٔ اسمی چون «کس» باشد. ویکی‌واژه یک گام فراتر می‌رود و «کس» را مستقیماً به هندواروپایی آغازینِ *kuḱis «موی زهار؛ فرج» بازمی‌گرداند (هم‌ریشه‌ها: quz کردی شمالی، kʷsî هورامی، kūšỹs لیتوانیایی) و می‌افزاید که شاید حسن‌تعبیری از معنای کهن‌ترِ «شکم» باشد که در kukṣí- سنسکریت، qwšy سغدی «پهلو» و «کشتی» فارسی برجای مانده است. نکتهٔ آوایی: پوکورنی صورت را kūs می‌نویسد حال آنکه صورت زندهٔ فارسی kos است و نورایی همان را درست آورده. پس: خانواده درست، ولی «پدرِ» بی‌واسطه نادرست است — با احتیاط پذیرفتنی.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%B3\"],\n \"ref_check\": [\n  {\"ref\": \"POK:953\", \"status\": \"partial\",\n   \"note\": \"Pokorny does have the word — '(s)keu-k-: ... kukṣi- m. \\\"belly, womb, cavity\\\"; common Old Indic -gh- > -ks- npers. kūs \\\"vulva\\\"; Avestan kusra- \\\"sich wolbend, hollow\\\"' — but on p.952 of the 951-953 article, and as a sister of kusra-, not a daughter. Nothing in Pokorny licenses the arrow kusra- → kos.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"WP II 548 (leaf 552)\", \"stance\": \"partial\",\n   \"note\": \"'kakṣi- m. \\\"Bauch, Mutterleib, Degenscheide, Hoehlung\\\"; npers. kūs \\\"weibliche Scham\\\" (š aus ... nicht aus kš; s. Persson); av. kusra- \\\"sich woelbend, hohl\\\"' — the two Iranian words are listed in parallel.\"},\n  {\"src\": \"HRN\", \"where\": \"grep 'kus'/'Scham' in HRN.txt\", \"stance\": \"silent\",\n   \"note\": \"Horn's Grundriss has no entry for the word (it is not in his numbered list).\"},\n  {\"src\": \"BQT\", \"where\": \"grep for the headword in BQT_v3_pages.txt\", \"stance\": \"silent\",\n   \"note\": \"Borhan-e Qate' as edited by Mo'in does not carry the vulgar word as a headword with an etymological footnote; nothing to check there.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Germanic\", \"words\": \"husôn, hŭdjon; hudiz, hudjan; skŭma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five reconstructions are Watkins's, word for word, under (s)keu-: '4a. Germanic *huson- in Old English hosa, hose, covering for the leg'; '6b. Germanic suffixed zero-grade form *hud-jon- in French hutte, hut'; '3a. suffixed form *ku-ti- in Germanic *hudiz in Old English hyd, skin, hide'; '6a. Germanic suffixed lengthened zero-grade form *hud-jan in Old English hydan, to hide, cover up'; '2a. suffixed form *sku-mo- in Germanic *skumaz, foam, scum (< \\\"that which covers the water\\\"), in Old High German scum... Middle Dutch schum'. The phonology throughout is Grimm's Law on the zero grade *ku-/*sku- (PIE *k > Gmc *h, *sk stays), with Verner-free voiceless outcomes; *hūdiz < *kuH-ti- shows the regular lengthening before the lost laryngeal. Watkins files hide (v.) and hut under the extended root *keudh-, which Nourai has silently merged into the same node — a simplification, not an error, since Pokorny keeps them in one article too.\",\n \"derivation_fa\": \"هر پنج بازساختِ این گره واژه‌به‌واژه از واتکینز است ذیل (s)keu-: «ژرمنی *huson- در hosa انگلیسی کهن «پوشش ساق»»؛ «*hud-jōn- ژرمنی در hutte فرانسه، انگلیسی hut»؛ «*hūdiz ژرمنی در hȳd انگلیسی کهن «پوست»»؛ «*hūdjan ژرمنی در hȳdan انگلیسی کهن «پنهان کردن»»؛ و «*skūmaz ژرمنی «کف» (یعنی «آنچه روی آب را می‌پوشاند») در scūm آلمانی علیای کهن و schūm هلندی میانه». دگرگونی آوایی در همهٔ این‌ها همان «قانون گریم» بر درجهٔ صفرِ *ku-/*sku- است (کِ هندواروپایی > هـِ ژرمنی، و *sk بی‌تغییر)، و کشیدگیِ واکه در *hūdiz < *kuH-ti- برآمده از افتادنِ حنجره‌ای است. واتکینز فعل hide و واژهٔ hut را ذیل ریشهٔ گسترده‌ترِ *keudh- می‌آورد که نورایی آن را بی‌اشاره در همین گره ادغام کرده است؛ این ساده‌سازی است نه خطا، چون پوکورنی نیز همه را در یک مدخل نگاه می‌دارد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-\"],\n \"ref_check\": [\n  {\"ref\": \"POK:953\", \"status\": \"supports\",\n   \"note\": \"IEW (s)keu- final page: 'Modern High German dial. hosen \\\"husk, pod\\\", Old English hosa \\\"Strumpf, husk\\\", Old Icelandic Old High German hosa \\\"trouser\\\"; ... Gothic Old Icelandic Old English Old Saxon Old High German hus \\\"house\\\"; Gothic huzd ... Old High German hort \\\"treasure\\\" (*kuz-dho-)'; and on 952 'An. hud, ags. hyd, ahd. hut (*hudi-) \\\"Haut\\\" ... Old High German hutta \\\"cottage\\\" (*kutja or *kudhja)' and 'perhaps Old High German scum \\\"scum, froth, foam\\\" (if \\\"deckendes\\\")'.\"},\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. (s)keu- supplies all five forms verbatim (see derivation); '[Pok. 2. (s)keu- 951.]'\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)keu-\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.v. hose, hut, scum\", \"stance\": \"supports\",\n   \"note\": \"'hose, n. — OE. hosa, rel. to OS., ON., OHG. hosa ... These words lit. mean \\\"cover, covering\\\", and derive fr. I.-E. *qeus-, -s- enlargement of base *qeu-, \\\"to cover, hide\\\"'; 'hut, n. — F. hutte, fr. MHG. hütte or fr. OHG. hutta ... rel. to OE. hydan, \\\"to hide\\\"'; 'scum, n. — MDu. schum(e) ... perh. fr. I.-E. base *sqeu-, \\\"to cover\\\"'.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 548-549 (leaves 552-553)\", \"stance\": \"supports\",\n   \"note\": \"'An. hud, ags. hyd, ahd. hut (*hudi-) \\\"Haut\\\" ... ahd. hutta \\\"Huette\\\" (*qudja oder *qudhja; daraus as. hutta, hutti)'; and 'vielleicht anord. skum, ahd. scum \\\"Schaum\\\" (wenn \\\"deckendes\\\")'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"hose, hut; hide; skim, scum\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five English words are correctly attached, though three of them come in by loan rather than by direct inheritance. HOSE < OE hosa 'leg covering' is inherited. HIDE 'skin' < OE hȳd is inherited (the homophonous verb hide < OE hȳdan belongs to the extended root *keudh-). HUT is NOT inherited: it is a 1650s borrowing of French hutte, itself taken from MHG hütte / OHG hutta — Klein and Watkins agree ('Germanic *hud-jon- in French hutte, hut'). SCUM is a Middle-English borrowing from MDu. schum(e) (cognate OHG scūm, G Schaum). SKIM is secondary to it: ME skimmen from OF escumer 'to remove the scum', from escume < OHG scūm, with the regular French-to-English u > i (Klein compares brisk < F brusque, ribbon < F ruban). So the arrow from the Germanic node is right for all five, with the route running through Old French for hut and skim.\",\n \"derivation_fa\": \"هر پنج واژهٔ انگلیسی درست به این گره بسته شده‌اند، هرچند سه تای آن‌ها نه از راه میراث بلکه از راه وام‌گیری آمده‌اند. hose از hosa انگلیسی کهن «پوشش ساق» میراثی است؛ hide «پوست» از hȳd انگلیسی کهن نیز میراثی است (فعل هم‌آوای hide «پنهان کردن» از hȳdan به ریشهٔ گسترده‌ترِ *keudh- بازمی‌گردد). اما hut میراثی نیست: وام‌واژه‌ای است از hutte فرانسوی در حدود ۱۶۵۰ میلادی، و فرانسوی خود آن را از hütte آلمانی میانه / hutta آلمانی علیای کهن گرفته است — کلاین و واتکینز هر دو بر همین‌اند. scum وام‌واژه‌ای انگلیسی میانه از schum(e) هلندی میانه است (هم‌ریشه با scūm آلمانی کهن و Schaum آلمانی امروز)، و skim فرعِ همان است: از skimmen انگلیسی میانه از escumer فرانسوی کهن «کف گرفتن»، با ابدال قاعده‌مندِ u فرانسوی به i در انگلیسی (کلاین مقایسه می‌کند: brisk از brusque و ribbon از ruban). پس پیکانِ نمودار برای هر پنج واژه درست است، با این تفصیل که راه hut و skim از فرانسوی کهن می‌گذرد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kewH-\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 s.v. (s)keu- lists HOSE, HIDE(1), HIDE(3), HUT, SCUM (the last via 'Middle Dutch schum, scum: SCUM' and 'Old High German scum ... MEERSCHAUM'). SKIM is not in Watkins's list — it is covered by Klein (from OF escumer, to the same Germanic word).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.vv. hose, hut, hide, scum, skim\", \"stance\": \"supports\",\n   \"note\": \"'hut, n. — F. hutte, fr. MHG. hütte or fr. OHG. hutta ... which is rel. to OE. hydan, \\\"to hide\\\"'; 'skim ... prob. fr. OF. escumer (F. écumer), fr. escume (F. écume), fr. OHG. scum ... rel. to MDu. schum(e), whence E. scum. For the change of u to i cp. brisk (fr. F. brusque) and ribbon (fr. F. ruban)'.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat s.vv. hose, hut, scum\", \"stance\": \"supports\",\n   \"note\": \"Skeat likewise takes hut from French hutte < OHG hutta and scum from MDu. schuim, and groups them with 'to cover'.\"},\n  {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. hut / scum\", \"stance\": \"supports\",\n   \"note\": \"Same route: hut < Fr. hutte < OHG hutta; scum < MDu. schume, akin to OHG scum.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Latin\", \"words\": \"cutis; ob-scŭrus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Latin words are securely in the root. CUTIS 'skin' is *kuH-ti- (Watkins '*ku-ti- in Latin cutis'), the exact formal match of Gmc *hūdiz (OE hȳd 'hide') and the near-match of Gk. σκῦτος; Klein: 'L. cutis, \\\"skin\\\", lit. \\\"that which covers\\\", fr. I.-E. base *(s)qeut \\\"to cover\\\"'. OBSCŪRUS is ob- 'over, against' + *skū-ro- 'covering' (Watkins '*sku-ro- in Latin obscurus, \\\"covered,\\\" dark'), so literally 'covered over' > 'dark, indistinct'; Walde-Pokorny II 547 prints it as 'Lat. obscūrus \\\"*bedeckt\\\" = \\\"dunkel\\\"'. The same *skū-ro- shows up as OHG scūr 'shelter, penthouse' and in Mann's headword skūr- (IEC 1193), the very entry from which the Persian سکوره of node #11 is taken. Nourai's hyphenation 'ob-scŭrus' correctly marks the prefix.\",\n \"derivation_fa\": \"هر دو واژهٔ لاتینی به‌درستی در این ریشه جای دارند. cutis «پوست» از *kuH-ti- است (واتکینز: «*ku-ti- در cutis لاتینی»)، یعنی دقیقاً همتای صوریِ *hūdiz ژرمنی (hȳd انگلیسی کهن «پوست») و نزدیک به σκῦτος یونانی؛ کلاین می‌نویسد: «cutis لاتینی «پوست»، در اصل «آنچه می‌پوشاند»، از پایهٔ هندواروپاییِ *(s)qeut «پوشاندن»». واژهٔ obscūrus نیز ترکیب پیشوند ob- «بر، روی» است با *skū-ro- «پوشاننده» (واتکینز: «*sku-ro- در obscurus لاتینی «پوشیده»، تاریک»)، پس در اصل «سرپوشیده» > «تاریک، نامفهوم»؛ والده–پوکورنی (ج ۲ ص ۵۴۷) نیز می‌نویسد «obscūrus لاتینی: *پوشیده = تاریک». همان *skū-ro- در scūr آلمانی علیای کهن «سرپناه» دیده می‌شود و سرواژهٔ skūr- در فرهنگ مان (ص ۱۱۹۳) نیز همان است — همان مدخلی که «سکورهٔ» فارسیِ گرهٔ ۱۱ از آن گرفته شده است. خط تیرهٔ نورایی در «ob-scŭrus» پیشوند را درست نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/cutis\"],\n \"ref_check\": [\n  {\"ref\": \"POK:953\", \"status\": \"supports\",\n   \"note\": \"The (s)keu- article has 'Latin obscurus \\\"*bedeckt\\\" = \\\"dark\\\"; culus \\\"the Hintere\\\"' in its opening material and 'Latin cutis \\\"skin\\\"; cunnus \\\"pudendum muliebre\\\" (*kut-nos)' in the dental-extension section — both inside pp.951-953.\"},\n  {\"ref\": \"IEC:595\", \"status\": \"supports\",\n   \"note\": \"Mann p.595 s.v. kut- (7): '... cf. Gk. eg-kuti (\\\"on the skin\\\", fr. ... Lat. cutis, f. gp *cutium \\\"skin\\\"); OHG hūt, gp hūtio, f. id.'; and p.1193 s.v. skūr-: 'Lat. cf. ob-scūrus, adj. \\\"dark\\\"'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.vv. cutis, obscure\", \"stance\": \"supports\",\n   \"note\": \"'cutis ... L. cutis, \\\"skin\\\", lit. \\\"that which covers\\\", fr. I.-E. base *(s)qeut \\\"to cover\\\", whence also OE. hyd, \\\"skin\\\"'; 'obscure ... fr. L. obscurus, \\\"dark, dusky; indistinct\\\", orig. \\\"covered\\\", formed fr. ob- and I.-E. base *(s)qeu-, *(s)qewa-, \\\"to cover\\\"'.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 547 and 549 (leaves 551 and 553)\", \"stance\": \"supports\",\n   \"note\": \"'Lat. obscūrus \\\"*bedeckt\\\" = \\\"dunkel\\\"' (547); 'Lat. cutis \\\"Haut\\\"; cunnus \\\"pudendum muliebre\\\" (*qut-nos)' (549).\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)keu-\", \"stance\": \"supports\",\n   \"note\": \"'2b. suffixed form *sku-ro- in Latin obscurus, \\\"covered,\\\" dark (ob-, away from): OBSCURE; CHIAROSCURO'; '3b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"curium, cutis; obscure\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"curium, cutis, obscure\",\n \"correct_form\": \"corium (or, following AHD, cutaneous / cuticle)\",\n \"derivation\": \"CUTIS (the anatomical term for the dermis) and OBSCURE (ME, from OF obscur, from L. obscurus) are both straightforward Latin borrowings and belong here. CURIUM does not, and cannot: Klein s.v. curium — 'name of a radioactive element (chem.) — ModL; named in 1946 by its discoverer, the American chemist Glenn Theodore Seaborg ... in honor of the two Curies (Pierre and his wife Marie)'. A 1946 element-name has no Indo-European etymology at all. The printed page (rendered at 300 dpi and read: data/verification/sources/refs/ocr/BOOK/455.png) really does show 'curium, cutis, obscure', so the extraction is faithful and the mistake is Nourai's own. He almost certainly meant CORIUM, the dermatological term for the dermis, which is the natural companion of cutis — but even corium is not from this root: Klein s.v. corium derives it from L. corium 'hide, skin, leather', from I.-E. base *(s)qer- 'to cut, separate' (whence also cortex, scortum, English shear). The words AHD actually lists under (s)keu- for Latin cutis are CUTANEOUS, CUTICLE, CUTIS and CUTIN.\",\n \"derivation_fa\": \"دو واژهٔ cutis (اصطلاح کالبدشناسی برای «درم») و obscure (از فرانسوی کهن obscur، از obscūrus لاتینی) وام‌واژه‌های مستقیم لاتینی‌اند و جایشان در اینجا درست است. اما curium نه: کلاین ذیل curium می‌نویسد «نام عنصری پرتوزا؛ لاتینی نو، که در سال ۱۹۴۶ کاشف آن، شیمی‌دان آمریکایی گلن سیبورگ، به افتخار پیر و ماری کوری چنین نامید». نام عنصری که در ۱۹۴۶ ساخته شده اصلاً ریشه‌شناسی هندواروپایی ندارد. تصویر صفحهٔ چاپی (که با دقت ۳۰۰ نقطه بر اینچ ساخته و خوانده شد: data/verification/sources/refs/ocr/BOOK/455.png) به‌روشنی «curium, cutis, obscure» را نشان می‌دهد؛ پس خطای خوانشِ اسکن نیست، خطای چاپی خودِ کتاب است. نورایی به‌احتمال بسیار corium را در نظر داشته که اصطلاح پوست‌شناسیِ «درم» است و همنشین طبیعی cutis — ولی corium هم از این ریشه نیست: کلاین آن را از corium لاتینی «پوست، چرم» می‌گیرد، از پایهٔ هندواروپاییِ *(s)qer- «بریدن، جدا کردن» (همان که cortex و scortum و shear انگلیسی از آن است). واژه‌هایی که فرهنگ AHD ذیل (s)keu- برای cutis لاتینی می‌آورد اینهاست: cutaneous، cuticle، cutis، cutin.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/cutis\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"partial\",\n   \"note\": \"Watkins 1985 s.v. (s)keu- gives for Latin cutis only 'CUTANEOUS, CUTICLE, CUTIS; CUTIN' and for obscurus 'OBSCURE; CHIAROSCURO'. Neither CURIUM nor CORIUM appears anywhere in the (s)keu- entry; CORIUM is filed by Watkins under sker- 'to cut'. So Nourai's own reference supports two of his three English words and contradicts the third.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1971 s.vv. curium, corium, cutis, obscure\", \"stance\": \"contradicts\",\n   \"note\": \"'curium ... named in 1946 by its discoverer ... in honor of the two Curies'; 'corium, n., vascular layer of the skin, the derma. — L. \\\"hide, skin, leather\\\", lit. \\\"the hide stripped off\\\", rel. to cortex, scortum, fr. I.-E. base *(s)qer-, \\\"to cut, separate\\\"'. Both exclude the word from this root box.\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. corium / cutis\", \"stance\": \"partial\",\n   \"note\": \"Gives corium 'the dermis' < L. corium 'leather', cutis 'the skin' < L. cutis — confirming that the pairing Nourai wanted is corium + cutis, and that corium's Latin source is 'leather', not 'cover'.\"},\n  {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. curium\", \"stance\": \"contradicts\",\n   \"note\": \"'curium: a radioactive chemical element ... named after Pierre and Marie Curie' — a 20th-century coinage, with no IE pedigree.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"skŭreh; kŭč\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The two words have opposite fates. (1) سکوره skūreh 'earthen bowl' (variants سکره، اسکوره، اسکره) is exactly what Nourai's reference says: S. E. Mann, IEC p.1193, s.v. 'skūr- \\\"cover, shell\\\". WP II 548. Per. sukūre, s. \\\"earthen dish\\\"; Lat. cf. ob-scūrus; OHG skūra, f. \\\"barn\\\"; MHG schūr \\\"shelter\\\"; ON skúr \\\"penthouse; shell\\\"' — so the Persian bowl-word sits in Mann's list beside Latin obscūrus and OHG scūra, and Mo'in confirms the Persian forms ('اسکر [< سکر < سکوره] (ا.) کاسهٔ سفالین؛ کاس گلین'; 'سکره [= اسکوره، اسکره، اسکرچه = سکرچه = سکرجه معرب] کاسهٔ گلی'), incidentally showing that Arabic سكرجة is the Arabized offspring of the Persian word, not its source. This half is confirmed. (2) کوچ kūč 'household, family, tribe' is not. Mann does have 'kut- (6) (kūtis, ā, io) \\\"shelter, house\\\" ... Per. (?) kuc \\\"household\\\"' at IEC p.594 — but with his own question mark. Against it stands the whole Persian lexicographic tradition, including Nourai's second reference: Mo'in tags کوچ '[تر. - مغ.]' (Turkish–Mongolian) and Dehkhoda quotes the Borhan marginalia 'این لفظ ترکی است'. Wiktionary derives it from Proto-Turkic *köč- 'to migrate' (Chagatai كوچ, Azerbaijani köç, Turkish göç), with 'chattel, household, family, wife' as a secondary extension of the nomads' moving camp; a second Persian کوچ 'service, power' is from Turkic küç 'force'. Since the node's worst word governs, the node is disputed.\",\n \"derivation_fa\": \"سرنوشت این دو واژه وارونهٔ یکدیگر است. (۱) «سکوره» (گونه‌ها: سکره، اسکوره، اسکره) به معنی «کاسهٔ سفالین» دقیقاً همان است که مأخذ نورایی می‌گوید: مان در فرهنگ تطبیقی هندواروپایی (ص ۱۱۹۳) ذیل سرواژهٔ «skūr- «پوشش، پوسته»» می‌آورد: «فارسی sukūre «کاسهٔ سفالین»؛ لاتینی ob-scūrus؛ آلمانی علیای کهن skūra «انبار»؛ نورس کهن skúr». معین نیز صورت‌های فارسی را تأیید می‌کند («اسکر [< سکر < سکوره] کاسهٔ سفالین»؛ «سکره [= اسکوره، اسکره، اسکرچه = سکرچه = سکرجه معرّب] کاسهٔ گلی») و ضمناً نشان می‌دهد که «سکرجهٔ» عربی معرّبِ واژهٔ فارسی است نه سرچشمهٔ آن. این نیمه تأیید می‌شود. (۲) اما «کوچ» به معنی «خانواده، ایل» چنین نیست. مان در ص ۵۹۴ ذیل «kut- (6) «سرپناه، خانه»» می‌آورد «فارسی (؟) kuc «خانوار»» — با علامت پرسش خودش. در برابر آن، سراسر سنت واژه‌نگاری فارسی ایستاده است، از جمله مأخذ دوم خودِ نورایی: معین «کوچ» را با نشانِ «[تر. – مغ.]» (ترکی–مغولی) می‌آورد و دهخدا حاشیهٔ برهان را نقل می‌کند که «این لفظ ترکی است». ویکی‌واژه نیز آن را وام‌واژه‌ای از ترکی آغازین *köč- «کوچیدن» می‌داند (چغتایی كوچ، آذربایجانی köç، ترکی göç) و معنای «خانوار، زن و فرزند» را گسترشِ ثانویِ «اردوی کوچنده» می‌شمارد. چون بدترین حکمِ واژه‌ها بر گره حاکم است، این گره «ردشده» ارزیابی می‌شود: پژوهش امروزی «کوچ» را ترکی می‌داند نه ایرانی.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%86\",\n   \"https://abadis.ir/fatofa/%DA%A9%D9%88%DA%86/\"\n ],\n \"ref_check\": [\n  {\"ref\": \"IEC:1193\", \"status\": \"supports\",\n   \"note\": \"Mann, IEC p.1193 (IEC.txt leaf 659): 'skūr- \\\"cover, shell\\\". Cf. skuu. WP II, 548. Per. sukūre, s. \\\"earthen dish\\\"; Lat. cf. ob-scūrus, adj. \\\"dark\\\"; OHG skūra, f. \\\"barn\\\"; MHG schūr, sm. \\\"shelter, protection\\\"; Du. schuur, f., LG schür, n. id.; ON skúr, s. \\\"penthouse; shell\\\"; Li. dial. skūrà, f. \\\"fur, pelt\\\".' Exactly the سکوره of this node.\"},\n  {\"ref\": \"IEC:594\", \"status\": \"partial\",\n   \"note\": \"Mann, IEC p.594 (IEC.txt leaf 337): 'kut- (6) (kūtis, ā, io) \\\"shelter, house\\\". See next. Per. (?) kuc \\\"household\\\"; Hitt. kuca (queried) \\\"wall, side\\\"; Ligurian (in Rumansh) kuts \\\"house\\\"; Ir. cuithe, m. \\\"den, pit\\\"; OE hȳð \\\"harbour\\\"; Li. kūtis ... \\\"stable, stall\\\"; Latv. kūts.' The Persian word IS there, but Mann marks it with '(?)' and it is the only Iranian item in the lemma.\"},\n  {\"ref\": \"MON:3114\", \"status\": \"contradicts\",\n   \"note\": \"Mo'in's Farhang-e Farsi s.v. کوچ opens with the origin bracket '[تر - مغ.]' (Turkish–Mongolian) before '(اِ.) حرکت عده‌ای از جایی به جایی' (abadis.ir, فرهنگ معین section). Dehkhoda on the same page-set quotes 'این لفظ ترکی است'. Nourai's own Persian authority assigns the word to Turkic, not to this root.\"},\n  {\"ref\": \"MON:1899\", \"status\": \"supports\",\n   \"note\": \"Mo'in has the سکوره family: 'اسکر (oskora) [< سکر < سکوره] (ا.) کاسهٔ سفالین؛ کاس گلین. جام آب‌خوری' and 'سکره [= اسکوره، اسکره، اسکرچه = سکرچه = سکرجه معرب] (اِ.) کاسهٔ گلی' (MON_part1.txt). The 6-vol page number cannot be checked (only the 2-vol Adena reprint is on disk), but the entries are Mo'in's.\"}\n ],\n \"consulted\": [\n  {\"src\": \"IEC\", \"where\": \"Mann pp. 594 and 1193\", \"stance\": \"partial\", \"note\": \"see ref_check — supports سکوره unreservedly, کوچ only with a question mark.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in s.vv. اسکر/سکره and کوچ\", \"stance\": \"contradicts\",\n   \"note\": \"For کوچ, '[تر - مغ.]'. For سکوره, no origin bracket but the derivational chain سکوره > سکره > (معرب) سکرجه.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europaeischen Woerter orientalischen Ursprungs\", \"stance\": \"silent\",\n   \"note\": \"grep for köç/kotsch in LKT.txt returns nothing — the word did not travel into European languages, so Lokotsch has no entry.\"},\n  {\"src\": \"TTS\", \"where\": \"Vambery, Etym. Wb. der turko-tatarischen Sprachen (TTS_pages.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep for köç/kotsch/wandern in the OCR returns no usable hit (the OCR of this scan is poor); no confirmation of the Turkic side from Vambery, which is instead supplied by Mo'in, Dehkhoda and Wiktionary.\"},\n  {\"src\": \"WLD\", \"where\": \"WP II 548 (leaf 552)\", \"stance\": \"supports\",\n   \"note\": \"The page Mann cites for skūr-; the (s)qeu- article there carries 'ahd. scūr m. \\\"Wetterdach, Schutz\\\" (: lat. obscurus, lit. skūra), mhd. schūr \\\"Obdach, Schirm\\\", anord. skūr \\\"was die Schale der Mandel umgibt\\\", ahd. skura, sciura (*skurja) \\\"Scheuer, Scheune\\\"' — the Germanic half of Mann's skūr- lemma.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\n\n# strip helper key\nfor e in doc[\"entries\"]:\n    for n in e[\"nodes\"]:\n        n.pop(\"derivation_fa_ok\", None)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-455.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-455.py"
}
```


### [2026-09-14T02:19:50.411Z] TOOL RESULT

```
written
```


## [2026-09-14T02:19:54.558Z] TOOL CALL #103: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-455.json >/dev/null && echo \"valid JSON\" && python3 tools/verify_check.py 455"
}
```


### [2026-09-14T02:19:55.847Z] TOOL RESULT

```
valid JSON
nodes verified: 16/16
node verdicts: {'confirmed': 8, 'plausible': 6, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 19, 'not_checked': 1, 'partial': 8, 'contradicts': 1}
books consulted: {'supports': 32, 'silent': 9, 'contradicts': 7, 'partial': 8} | by book: {'WLD': 8, 'KLN': 8, 'POK': 6, 'AHD': 5, 'HRN': 4, 'HUB': 2, 'FRS': 2, 'SKT': 2, 'BRT': 2, 'MON': 2, 'WEB': 2, 'ARY': 1, 'SYN': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'AVG': 1, 'BQT': 1, 'FSD': 1, 'IEC': 1, 'LKT': 1, 'TTS': 1}
```


## [2026-09-14T02:20:13.239Z] AGENT

Verification of PDF page 455 (book page 425) is complete; `verify_check.py 455` reports 16/16 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed (entry 2 is the `Skeu 3 → Keu 3` redirect, skipped). Nodes: 8 confirmed, 6 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 19 supports, 8 partial, 1 contradicts, 1 not_checked.

**Disputed**
- *Skeu 2*, node #11 کوچ kūč "household, family, tribe": Mann (IEC 594) himself queries "Per. (?) kuc"; Nourai's other cited reference, Mo'in, tags کوچ **[تر. - مغ.]** (Turkish–Mongolian) and Dehkhoda quotes "این لفظ ترکی است"; Wiktionary derives it from Proto-Turkic *köč- "to migrate". The سکوره half of the same node is solidly confirmed by IEC 1193 (`skūr-` "cover, shell", "Per. sukūre 'earthen dish'"), so the node carries the worse verdict.

**Transcription_suspect**
- *Skeu 2*, node #10 English "**curium**, cutis; obscure": `error_in: "book"`. The 300 dpi render (saved to `data/verification/sources/refs/ocr/BOOK/455.png`) shows "curium" on the page, so the extraction is faithful. Curium is a 1946 element named after the Curies (Klein); Nourai meant *corium*, which Klein/AHD anyway assign to *(s)ker- "to cut", not to this root.

**No extraction errors found** — the JSON matches the printed page throughout, including the book's own run-together citation "IEC:1193AHD:1540" in the entry-1 root box (missing semicolon is the book's typography).

**Notable findings for the owner**: Pokorny 953 himself makes the *pneu- × *kseu- crossing that entry 0's double root box draws, and names "npers. išnōsa, ašnōsa"; Hübschmann no. 90 supplies the missing MP link (*xšnauša- > phl. *šnōšak > NP išnōša). The helmet nodes (#1, #2) are `plausible` only because Pokorny mentions Av. xaoδa- on p.952 merely as a semantic neighbour of Lat. cudo, while AHD/Wiktionary assign it to *kadʰ- (hat, hood). کاز/کازه (#3) is confirmed as a Sogdian loan (Gharib no. 4682 p.187; Henning via Mo'in's BQT 1562 footnote) but no source links it to *(s)keu-. Pneumonia (#5) belongs to *pleu-, per Nourai's own AHD.
