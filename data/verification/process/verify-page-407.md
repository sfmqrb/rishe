# Verification process log — verify-page-407


## [2026-09-14T00:53:12.168Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 407 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-407.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-407.json. Write /home/sfmqrb/git/rishe/data/verification/page-407.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 407` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:13.469Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:14.291Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:14.304Z] TOOL RESULT

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


## [2026-09-14T00:53:14.731Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-407.txt"
}
```


### [2026-09-14T00:53:14.749Z] TOOL RESULT

```
1	=== PDF page 407 (book page 377) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Prî : to love, praise  (refs POK:844)
4	#1 (parent #0) [Avestan] refs=POK:844 | âfritan : to create ; â-frî-nami : I praise ☞Apo
5	  #2 (parent #1) [Persian] refs=BQT:51 | âfarîn «آفرین» : praise ; âfarîdan «آفریدن» : to create ; nefrîn «نفرین» : curse | extra: آفریدگار
6	    #3 (parent #2) [Arabic] refs=AHD:23; PLA:203 | ifrît : demon creature | NOTE: RCH:lxxvii derives it from Arabic "A.f.r"
7	      #4 (parent #3) [Persian] refs=MON | efrît «عفریت» : demon | extra: عفریته
8	#5 (parent #0) [Sogdian] refs=SOD:3 | `pryn : to praise ; `prytyy : created ; `fryn, `frywn : praise
9	#6 (parent #0) [Germanic] refs=AHD | fri : friend, free, good
10	  #7 (parent #6) [English] refs=None | free, fresh, friend, Friday
11	--- entry 1 ---
12	ROOT [Indo-European] Prs : speck, spot, sprinkle  (refs POK:823; IEC:1003)
13	#1 (parent #0) [Avestan] refs=IEC:1003; POK:823 | pareš : drip ; paršuya : of water
14	  #2 (parent #1) [Persian] refs=IEC:1003; MON:665 | pâšîdan «پاشیدن» : sprinkle, scatter | extra: پاچیدن ، پاش
15	#3 (parent #0) [Sanskrit] refs=IEC:1003 | parsamî : sprinkle
16	#4 (parent #0) [Greek] refs=IEC:1003 | pardakos : wet
17	#5 (parent #0) [Medit] refs=PRT:349; IEC:998,1003 | parnas, pard : a spotted animal
18	  #6 (parent #5) [Sanskrit] refs=PRT:349; KLN:1129 | pardâku : panther
19	    #7 (parent #6) [Persian] refs=HRN:72; SKT:372; BQT:416 | pard «پارد» : panther ; palang «پلنگ» : leopard ; yŭspalang «یوزپلنگ» : a kind of leopard ☞Yeu 3 | extra: پارس۲
20	  #8 (parent #5) [Greek] refs=KLN:1129; PRT:349 | pardos : panther
21	    #9 (parent #8) [Latin] refs=AHD:952 | pardus : panther
22	      #10 (parent #9) [English] refs=KLN:1129; PRT:349; SKT:372 | pard, leopard
23	--- entry 2 ---
24	ROOT Pu 1 -> redirect to Peu
25	
```


## [2026-09-14T00:53:17.476Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-407.json",
 "description": "Read source JSON page 407"
}
```


### [2026-09-14T00:53:17.518Z] TOOL RESULT

```
{
  "pdf_page": 407,
  "book_page": 377,
  "entries": [
    {
      "root": {
        "name": "Prî",
        "lang": "Indo-European",
        "refs": "POK:844",
        "gloss": "to love, praise"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:844",
          "words": [
            {"translit": "âfritan", "gloss": "to create", "script": null},
            {"translit": "â-frî-nami", "gloss": "I praise", "script": null, "see": ["Apo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:51",
          "words": [
            {"translit": "âfarîn", "gloss": "praise", "script": "آفرین"},
            {"translit": "âfarîdan", "gloss": "to create", "script": "آفریدن"},
            {"translit": "nefrîn", "gloss": "curse", "script": "نفرین"}
          ],
          "script_extra": "آفریدگار",
          "note": null,
          "quote": {
            "text": "اگر دشنام فرمایی و گر نفرین ، دعا گویم - جواب تلخ می‌زیبد لب لعل شکرخا را",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "AHD:23; PLA:203",
          "words": [
            {"translit": "ifrît", "gloss": "demon creature", "script": null}
          ],
          "script_extra": null,
          "note": "RCH:lxxvii derives it from Arabic \"A.f.r\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "efrît", "gloss": "demon", "script": "عفریت"}
          ],
          "script_extra": "عفریته",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:3",
          "words": [
            {"translit": "`pryn", "gloss": "to praise", "script": null},
            {"translit": "`prytyy", "gloss": "created", "script": null},
            {"translit": "`fryn, `frywn", "gloss": "praise", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "fri", "gloss": "friend, free, good", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "free, fresh, friend, Friday", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Prs",
        "lang": "Indo-European",
        "refs": "POK:823; IEC:1003",
        "gloss": "speck, spot, sprinkle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:1003; POK:823",
          "words": [
            {"translit": "pareš", "gloss": "drip", "script": null},
            {"translit": "paršuya", "gloss": "of water", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:1003; MON:665",
          "words": [
            {"translit": "pâšîdan", "gloss": "sprinkle, scatter", "script": "پاشیدن"}
          ],
          "script_extra": "پاچیدن ، پاش",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1003",
          "words": [
            {"translit": "parsamî", "gloss": "sprinkle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:1003",
          "words": [
            {"translit": "pardakos", "gloss": "wet", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Medit",
          "refs": "PRT:349; IEC:998,1003",
          "words": [
            {"translit": "parnas, pard", "gloss": "a spotted animal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Sanskrit",
          "refs": "PRT:349; KLN:1129",
          "words": [
            {"translit": "pardâku", "gloss": "panther", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "HRN:72; SKT:372; BQT:416",
          "words": [
            {"translit": "pard", "gloss": "panther", "script": "پارد"},
            {"translit": "palang", "gloss": "leopard", "script": "پلنگ"},
            {"translit": "yŭspalang", "gloss": "a kind of leopard", "script": "یوزپلنگ", "see": ["Yeu 3"]}
          ],
          "script_extra": "پارس۲",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "Greek",
          "refs": "KLN:1129; PRT:349",
          "words": [
            {"translit": "pardos", "gloss": "panther", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Latin",
          "refs": "AHD:952",
          "words": [
            {"translit": "pardus", "gloss": "panther", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:1129; PRT:349; SKT:372",
          "words": [
            {"translit": "pard, leopard", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pu 1",
        "redirect": "Peu"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T00:53:19.844Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','SOD','AHD','PLA','MON','BQT','PRT','KLN','HRN','SKT','WLD','BRT','PHD','NYB','SYN','FVQ','AFM','RCH','CHEUNG','HUB','ARY','WEB','FSD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T00:53:20.898Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.his
CHEUNG null
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-14T00:53:24.375Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -60; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head"
}
```


### [2026-09-14T00:53:24.455Z] TOOL RESULT

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


## [2026-09-14T00:53:24.867Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:53:24.911Z] TOOL RESULT

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


## [2026-09-14T00:53:31.209Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps({k:d[k] for k in ['POK','IEC','SOD','PRT','KLN','HRN','SKT','BQT','MON','AHD','PLA','RCH']},ensure_ascii=False,indent=1))\" | head -200"
}
```


### [2026-09-14T00:53:32.144Z] TOOL RESULT

```
{
 "POK": {
  "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
  "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/indogermanisches01pokouoft",
  "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
  "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
  "local_files": [
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
  ],
  "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
 },
 "IEC": {
  "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
  "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
  "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
  "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
  "notes": "",
  "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
 },
 "SOD": {
  "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/SogdianDictionary",
  "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
  "local_file": [
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
  ],
  "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
  "covers_etymology": true,
  "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
  "cites": "entry number / page in Gharib's Sogdian dictionary"
 },
 "PRT": {
  "title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958",
  "edition_found": "1958 (lending-only copies)",
  "kind": "archive_restricted",
  "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending",
  "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)",
  "local_file": null,
  "page_offset": null,
  "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.",
  "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."
 },
 "KLN": {
  "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
  "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
  "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
  "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
  "local_files": [
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
  ],
  "cites": "page number, continuous across the two volumes (1966–67)"
 },
 "HRN": {
  "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
  "edition_found": "1893 (Google scan, Univ. Michigan)",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/grundrissderneu00horngoog",
  "identifier": "grundrissderneu00horngoog",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
  "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
  "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
  "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
 },
 "SKT": {
  "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
  "edition_found": "1911 'new and corrected impression' (Google scan)",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/aconciseetymolo01skeagoog",
  "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
  "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
  "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.",
  "cites": "page number of Skeat, Concise Etymological Dictionary"
 },
 "BQT": {
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
 },
 "MON": {
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
  "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
  "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
 },
 "AHD": {
  "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
  "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
  "kind": "archive_djvu+website+archive_restricted",
  "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
  "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
  "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
  "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
  "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
  "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
 },
 "PLA": {
  "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
  "edition_found": null,
  "kind": "archive_djvu",
  "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)",
  "identifier": null,
  "local_file": [
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
   "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"
  ],
  "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).",
  "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
  "notes": "Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).",
  "scans": [
```


## [2026-09-14T00:53:36.768Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 84[34]\" POK_full.txt | head -20; echo \"=== lemma prai\"; grep -n -i \"lemma: pr[aā]i\\|lemma: prī\\|lemma: pri\" POK_full.txt | head"
}
```


### [2026-09-14T00:53:36.829Z] TOOL RESULT

```
68772:Page(s): 843 
68966:Page(s): 844 
68986:Page(s): 843-844 
=== lemma prai
68912:Root / lemma: prai- prai-, prT- (pri-)
```


## [2026-09-14T00:53:37.426Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 82[234]\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:53:37.480Z] TOOL RESULT

```
66567:Page(s): 822-823 
67188:Page(s): 823 
67218:Page(s): 823 
67246:Page(s): 823 
67264:Page(s): 824 
67302:Page(s): 824-825 
67801:Page(s): 823-824 
67814:Page(s): 824
```


## [2026-09-14T00:53:40.123Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '68900,68995p' POK_full.txt"
}
```


### [2026-09-14T00:53:40.205Z] TOOL RESULT

```
actually "young bird'), Lithuanian putyt/s'young animal, young bird' (Zartlichkeitsausdruck), 
Baltic *put-n-a-\n Latvian putns'b\r6'\ with other, demin. Formansverbindung Lithuanian 
yOaJ-/rs//s "bird'. 

maybe alb. pa/a "goose' Slavic loanword from russ. -Church Slavic yOb/a "bird' : Serbo- 
Croatian: pa'//ra"duck' [f]. 

References: WP. II 75 f., WH. II 259, 265 f., 382 f., 385 f., 394, Trautmann 233. 
Page(s): 842-843 



Root / lemma: prai- prai-, prT- (pri-) 
Meaning: to like, feel well-disposed, friendly 

Material: Old Indie pnnat/" pleases ', Med. "is cheerful about etwas', pnyateds., ' loves ', 
yO/'/?a- "cheerful, befriedigt; geliebt', prltf-i. 'pleasure, joy, satisfaction', pr/yayate 'behandeW. 
liebevoll, befreundet sich' (: Gothic fr/jon, Old Church Slavic prija-jg), priya- 'dear, 
desirable, worth having, welcome, wanted, liked, beloved, fancied ', m. ' lover, husband ', 
f. 'Geliebte, wife' (= Avestan frya-. Old Icelandic Friggeic, and Gothic freis, c. rhydd 
'free'), pr/yatva-m ^ das Liebsein or -have' (: Gothic frijat^wai. 'love'), priyata ds. (= Old 
English freodlos/e'); with *pr9/-: prayahn. 'pleasure, enjoyment', preman-m. n. 'love, 
favour', yO/ie/a/'- 'Wohltater, Liebhaber, Pfleger', Superl. prai'stha-{ved.), prestha- 'Webst, 
teuerst', whereupon Kompar. preyas- 'lieber' for older *prayas-\ Avestan fray- ' satisfy ', 
e.g. /^>v75/775/7/ participle frita-, fnna-, /^/z?a- 'blithe, glad; befriedigt; geliebt', friti-t 'prayer', 
frya-^ dear, worth '; perhaps the hispan. (Venetic-lllyrian ?) VN Praesta-marci {: Old 
English fnd-hengest)\ 
Note: 

alb. Geg prende, Tosc Premte]^ preman- d/es] 'Friday' was created on the same basis as 
Latin L Veneris dies day of the planet Venus (whence Fr. vendredi), based on Gk 
Aphrodites tiemera day of Aphrodite, Germanic Freitag'day of Freya = goddess of love' 
similar to gr. napaoKEun 'Friday' from gr. TTpauc; ' soft, mild ' 

gr. TTpauq 'gentle, mild' from *TTpc(ju- with jijngerer oinflection irpgoc;, beweist Indo 
Germanic ai, whereas, belongs Old Irish rfari. 'volition, wish' to erei-, S. 330; 

cymr. riiydd'free' = Gothic freis (akk. frijana). Old High German Old Saxon frf. Old 
English free, frflree, loose, free from'. Old Icelandic in frjaisirom * frifiais {d\e meaning 
'free' originally 'to den Lieben belonging'); Old Icelandic Frigg, Old High German Fri/'a 'wife 
Wotans', Old English freoi., Old Saxon frfn. 'woman from noble lineage ' ('die love'); 
Gothic fri/onlove', Old Icelandic frjads., Old English frfoganlove, set free, release ', mdn. 
vriien, Old Saxon frioiian' woo, court, marry, werben', participle Gothic fri/onds Inend' , Old 
Icelandic frsendi, PI. freendr^iueud, kinsman, relative'. Old English frfond. Old Saxon friund 
"friend, lover, kinsman, relative'. Old High German /^/i//?/ 'friend, lover'; Old Icelandic frfdr 
'beautiful'. Old English /^/b'-/7e'/7^e's/'stattliches horse'; from *frTda-\v\ the meaning 
"geschonf derives Gothic freidjan 'spare, look after'. Old High German i//7?e/7'hegen' 
(M^o/'eingefriedigter courtyard ', Modern High German Freitfiof av\d popular etymology 
Fried fiof)\ with /Old Icelandic fridiii^ lover, lover ', f. fridia, friiia. Old High German fridei, f. 
/^/ioV/a 'Geliebte(r)', next to which from participle Jrijoda-iroru: Old Saxon friutfiil. Old High 
German friudiids.; Old High German friduxr\. 'peace, protection, certainty, Einfriedigung', 



Old Saxon frithuxw. "peace', Old English frioduxw. "peace, protection, certainty'. Old 
Icelandic fridrvn. "love, peace', Gothic ^5-/^/^0/7 "spare, look after'. Old Icelandic frida 
"Frieden make, versohnen'. Old English fridian^ shield ', Old High German gifridon 
"beschijtzen'; 

Old Church Slavic prejg^ be favorable to, take care of ', prija-jQ, -//ds., prijatelb "friend, 
lover '; probably also Latvian prieks "pleasure, joy'. 

maybe alb. yO/"e/r "touch, make love' : Latvian p/ye/rs "pleasure, joy', alb. Geg me phte\o 
host, protect, expect, wait. 

References: WP. II 86 f., Trautmann 231 . 
Page(s): 844 

Root / lemma: pra- 

Meaning: to bend 

Note: ?; only Latin and Celtic 

Material: Latin pravus^ inverted; slant, skew; evil, bad'; in addition pratum meadow' (as " 

incurvation of Bodens', compare e.g. Lithuanian lanka^ sinking in, meadow': /e'/7/r//"bend') 

and (as "Aufbiegung, bulge, hill'); Middle Irish rath, raithxu. f. " earthwall, fortress', mcymr. 

bed-rawt, ncymr. bedd-rodxr\. "burial mound, grave', bret. bez-reti. "Begrabnisplatz, 

graveyard ', gall, ratin f\Vk. Sg. "castle(hugel)', PN Argento-rate. 

References: WP. II 86, WH. II 358 f. 

Page(s): 843-844 

Root / lemma: preg- 

Meaning: willing, covetous, active 

Material: Gothic (faihu-)friks\qe\(i-) greedy ', Old Icelandic frekr^ greedy, strong, hard, 

agile, lively'. Old English frecc^ greedy, audacious' {*frakja-). Old High German freh^
```


## [2026-09-14T00:53:40.210Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '67150,67310p' POK_full.txt"
}
```


### [2026-09-14T00:53:40.263Z] TOOL RESULT

```
Old Church Slavic perg, pbrat/'\r\\t, esp. with dem Blauel hit, wash', Serbo-Croatian 
perem, prat/^\NasW; ablaut. Old Church S\a\/'\c ptrjg, *pbret/" contendere' , sg-pbrja, sb- 
porb fight', Czech pru, pr/t/ se ' quarreV and Old Church Slavic *pbrg, *pert/"\n russ. pru, 
pratb, peretb 'press, urge, press, push', naporb ' shove ' etc.. Old Russian pbrtb 
'Badestube'; 

pe/g'-; Armenian harkanem {prg-) 'hit, zerhaue (wood), falle (tree), slay, fight '; Old Irish 
orcaid. Middle Irish o/zy^/ic/'erschlagt, slays, verwiJstet'; Middle Irish cymr. 0/77'Morden, 
Zersioren' { *fPprg-no- od. -na)\ abret. treorgam 'perforo', org/at 'caesar' (= caesor), gall, 
o/ye 'occide', PN Orgeto-rTx, different about Celtic org-s. Lewis-Pedersen 387 (to Hittite 
harganu-' destroy'; compare das Old Irish verbal noun orcunirom *orgena)\ perhaps here 
Old Indie Parjanya- rain- and Gewittergott; see be\o\N perk"u-s. 

References: WP. II 42 f., WH. II 288, Trautmann 215; 
See also: further to perg-1. 



Page(s): 818-819 



Root / lemma: persna, -snT-, -sno- 

Meaning: heel 

Material: Old Indie parsni-i., Avestan pasna-u. "calcaneus '; gr. nTspvri f.; Latin pernai. 

{*persna) "Hinterkeule, Schweineschinken, thigh, leg', /Oe/77/s 'quick, fast' (with the 

calcaneus); Gothic fafrsna. Old Saxon fersna. Old High German /fe/'sa/75 "calcaneus ' 

{* persna). Old English fiersini. ds. {*persni-)\ Hittite pars/na{\eg. parsna) "thigh, hip ', pars- 

(a)nai-^ crouch ' (auf den Oberschenkein). 

References: WP. II 50 f., WH. II 289 f., Pedersen Hittite 258. 

Page(s): 823 

Root / lemma: pers- 

Meaning: to drizzle, sprinkle; dust, ashes 

Note: 

Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 

pera-. pre- preu-: to drizzle, sprinkle, jet < Root/ lemma: *(s)p(h)ereg- (s)p(h)erag-, 

(s)p(h)reg- {nasaXxzedi spreng^ : to rush, hurry; to scatter, sprinkle. 

Material: Old \x\6\c prsat, prsata-mu. "drip'; prsant-, f. prsatf dappled, dotted, spotted, 

varicolored', yq/'S5//'"scheckige cow, gefleckte antelope '; Avestan parsuya- ^oi water', n., 

perhaps "Schneewasser'; Old Icelandic fors, fossm. "waterfall'; 

Lithuanian purs/as, y0^7's/a"Schaumspeicher, purksf/'as eine Katze prusten, 
schnarchen'; Latvian pars/aT\ocke' (of snow, ash, wool) ablaut. p^rs/a6s.; (compare 
Latvian sp^/'s/a/ "prusten'); Slavic *parsa- m. "dust, powder' > *porchb in Old Church Slavic 
prachb ds.; Slavic ptrstb in Old Church Slavic prtstb "xou(;', ( *Pers-), besides sloven, prh 
m. "dust, powder, ash' (= Old Icelandic fors), pfhaf/" strew, distribute, whisk ', Czech prseti 
ds. etc.; Tocharian A B pars- "sprinkle'; participle Akt. papars, Hittite pappars-^ s^r\tzer\, 
sprinkle '. 

References: WP. II 50; Trautmann 206 f.. 
See also: extension from per-/ "spray'. 
Page(s): 823 

Root / lemma: perth- {*pe-horghi-a) 

Meaning: pole; sprout 

Note: 



Root / lemma: perth-{*pe-horghi-a)\ pole; sprout, derived from a prefixed pe- of Root/ 

lemma: oii- {* horghi-a)\ vine, *grape < Root/ lemma: orghi-, j'ghi-{*horghi-a)\ testicle. The 

prefix pe-, po is common of Hittite, Slavic languages. 

Material: Armenian ort' {o-siexn) " grapevine, Rebe'; 

Maybe alb. hardi, hardh/a ^grapey\ne' (see above). 

gr. nT6p9o(; m. 'sprout' (compare nToAsfJoq : noAstJoq etc.); perhaps Latin pertica^ shaft, 

pole', whether not from per-ti-caio Oscan pert^\i\s to' from *per-ti, also originally " transom 

'; compare Czech pfiska^s., S. 810. 

References: WP. II 49, WH. II 292 f. 

Page(s): 823 

Root / lemma: pes-3, pesos 

Meaning: membrum virile 

Grammatical information: n. 

Material: Old Indie pasas- n. = gr. n£0(; n. 'penis', gr. nooGn f. ds., Latin penis ( *pesnis)\ 

Old High German fasel. Old English/fes/, Old High German /^se//" penis'. Middle High 

German vaselrinV breeding bull ', Modern High German Faselschwein^ breeding pig ', 

ablaut. Middle High German i/es// "fertile', i//5e/"penis'. 

References: WP. II 68, WH. II 281. 

Page(s): 824 

Root / lemma: pet-1, pet-, peta- 

Meaning: to open wide (the arms) 

Material: Avestan pa^ana-^W\6e, breit' (das z? after yoa/-az?^-ds.); 

gr. Aor. nsTaaaai, nsTaaai, thereafter n£Tavvu|ji 'breite from, offne', previous present 
niwriMi, nirvw (from *Pet-), nsraapa n. 'curtain', -nt^aaoc, m. 'breitkrempiger hat', n£TaAo(; 
"ausgebreitef, nsraAovn. 'Platte, leaf, naravn f. ' platter ' (from *n£Tavc(; out of it Latin 
patina (is.); 

Latin pated, -ere'sich erstrecken, be open '; in addition pando, -ere 'offne, breite from' 
(the variation /: o^ expounded sich through old athemat. inflection after Kuiper, Nasalpras. 
163), passusm. ' footstep, fathom'; pateral\at bowl' (from yC>a//>75 through influence of 
crater?); whether here petrius'th\n and fragile, flimsy '??; Oscan patpWJ 'patet', patensfns 
'panderent', Volscan Imper. an-patitu '*adpanditd\ 

Scots Gaelic aitheamii {*eitheamH) ' filament ' (as measure), = acymr. etem, ncymr. 
edau ds. ( *petima); 



Old Icelandic fadmr^ hugging, embrace, fathom, filament ', FIN Fgd, Gen. Fadar, Old 
English /fed/77 mf. ds. " filament, fathom', engl. fathom. Old High German fadam, fadum^ 
filament '; here also Old English foder, engl. father. Modern High German Fuder?, Old 
High German fuodar. Old Saxon father. Old English /&dc»/'"Wagenlast', Modern High 
German Fuder, from Germanic *fddra-^6as Umfassende'; Gothic fat^a. Middle High 
German vadei. 'fence' (as ' encirclement '); Old High German /feo'e/-^c»/o''Blattgold' (:gr. 
nsTQAov), doubtful Old English ^c»/o'-/fe//"Goldplatte', Middle High German golt-veF gold 
plating '; 

Lithuanian yoe/ys "shoulder'. Old Prussian pettei. ds.; pettisxn. "shovel, scapula'; 

Hittite pattar, Dat. paddanriab\e\.\. (?)'. 

References: WP. II 18, WH. II 244 f., 262, Trautmann 217. 
Page(s): 824-825 

Root / lemma: pet-2, peta- : pte- pto- (gr. pta^ 
Meaning: to fall; to fly 



Material: Old Indie patat/lWes, wirft sich, fallt' (= TTETOMai, Latin peto, acymr. hedarit), Aor. 
apaptat, peta-\x\ Put. patisyati, Supin. patitum, participle patita-); patayat/lWes' (= gr.
```


## [2026-09-14T00:54:32.556Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD watkins pri\"; grep -n \"^prī-\\|^pri-\\|^prāi\\|^prai\" AHD_watkins1985.txt | head; echo \"=== AHD pers\"; grep -n \"^pers-\\|^perk\\|^per-\\b\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T00:54:32.631Z] TOOL RESULT

```
=== AHD watkins pri
=== AHD pers
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
```


## [2026-09-14T00:54:33.983Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD pryn\"; grep -n \"pryn\\|frywn\\|prytyy\" SOD.txt | head -20; echo \"=== SOD_pages\"; grep -n \"pryn\" SOD_pages.txt | head -20"
}
```


### [2026-09-14T00:54:34.070Z] TOOL RESULT

```
=== SOD pryn
2868:Ill  3jj>  j3  JUL* . ju^>  oLiy  ^r/'  n>f A)  j    *frywn  £sjy-*<i 
5783:/afriwanV  *frywn        blessing 
7774:20  »pryn-   B,  S  C»J'jjn<d>J'j^ 
7775:afrin   ©<*d-frina  =»*fryn-,  *pryn- 
7780:21  »prync-   S  cpjj>, 
7796:afriwan   ('prywnh)  =»*prywn,  "frywn 
8033:afnn   ®<*a-frlna-   ®impf.  m>fryn  =*»pryn-, 
8035:"pryn- 
8050:70  »frywn  M  - 
8054:'frywn 
8913:219  Mpryn-    B  o^/j-U-O^- 
8927:afriwan   =»*Prywn,  8frywn 
11237:frywn   ©pi.  -f   =»bywny 
11820:afrin    =>*fryn-,  *pryn-,  'fryt- 
11857:674  'frywn   M,  C 
11858:afriwan   =»*Prywn,  *frywn,  *prywn 
11864:675  'frywncyq   M,  C  yjl  cj^ 
18375:osprenc(an)   =>spryncn  snng 
18422:1638  'sprymk  =»  'sprynVk 
18431:osprayme  ©pi.  -yt,  -t\  -kt   ^'sprynVk 
=== SOD_pages
3908: 20 »pryn- B, S                 C»J'jjn<d>J'j^
3909:    afrin ©<*d-frina =»*fryn-, *pryn-                           a8e, a8aku, a8o (»Syy, »8k, »8yh) ©abl. >8>(h)t
3913: 21 »prync- S                                       cpjj>,      EGSii 136, GMS 1560-80; »<yjfct MD; ><?*vv, Anc.
3986:                                                                        afnn ®<*a-frlna-         ®impf. m>fryn =*»pryn-,
3987:      aSektam, aSktam                                   fi4Ty,            "pryn-
4430:219 Mpryn-   B                      o^/j-U-O^-
5686:        afrin =>*fryn-, *pryn-, 'fryt-                                 BBB 528; GMS      169, 318
8493:                                                                         osprenc(an)    =>spryncn snng
8517:1638 'sprymk =» 'sprynVk                                                   >sptkw, MDii; >spt(i)w% TSP 2.751, 1223, 7.76,
8525:     osprayme ©pi. -yt, -t\ -kt ^'sprynVk                                  STii 8.8; BBB 649, 610; >sptyh% BBB b49; Hen.
10936:        f(a)rayn (Prynh)       =»pryn\ fryn(>), Pryn>              u^~"
11624:2734 brc =* z>tk prch                                        2747 pryn* S                              j 3J <o^U < jUj
11626:2735 brd'r-    C => Prt-                                          frayna (prynh, Prynh) =*fryn()), P'ryn               <
11631:                                                             2748 prynh B =* Pryn>
11780: 2801 prypryny(y) M                        >^*jjjl                 Prze (Prz}y) ©<*brzaka ©ace. flrzk^w, pi.
11785: 2802 prync M                                         ^
11795:2804 pryny M                  :                •ju><^              length
14764:      frayna (Prynh, prynh, frynh) ®f. n. =*PJryn,                    3903 frm'n M, C                           J>w<^
23824:                                                                               =»pryng2
23878:        Av. avian ^pryng1                                             7029 pr'yt B                                     *"S &j
```


## [2026-09-14T00:54:40.498Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if ' 20 »pryn-' in p or '»pryn-  B' in p:\n        print('leaf',i,'printed~',i-66)\n        print(p[:2500])\n        break\nEOF"
}
```


### [2026-09-14T00:54:41.658Z] TOOL RESULT

```
leaf 67 printed~ 1
"Pryn-

    GMS 1103; BBB 568                                        35 »8>k -> »5>y
                                                             36 "5'kw B, S         (jy >^- >>)u<^ ^^         <trT
 20 »pryn- B, S                 C»J'jjn<d>J'j^
    afrin ©<*d-frina =»*fryn-, *pryn-                           a8e, a8aku, a8o (»Syy, »8k, »8yh) ©abl. >8>(h)t
    (ro)praise                                                    pi. M(>V; pi. ob. *Sytyy =>*Syyt My
    TSP 25ii, 1 n p236; KG 552, 572                             somebody, anybody

 21 »prync- S                                       cpjj>,      EGSii 136, GMS 1560-80; »<yjfct MD; ><?*vv, Anc.
    aPrenc ? ©<*a-bar9g-\ Parth. abrang                           Lett.; S W, SGI 1986,407-10
    (fo)cultivate                                            37 "8'm M                              (jsz^ks^)^
    Gersh. apud. Sund. MSP p39
                                                                Adam ^S'm
                                                                adam
 22 "pryt'k S                                        »j^
    afrite (*Pryty) ©pp. ^fryty                                 Hen. JRAS 1944, 18

     praised                                                 38 "5'wkh   B                                J^^<i
     KG 327, 580; TSP 25ii, 3; W-Li 71                          a8uk (»Swk) ®<*aSu-
 23 >}pryty     B => »pryt>k                                    grain, crop
                                                                TSP 6.157 n p206; BSTBL, Dhu. 29; Emmerick.
 24 "prywn B                           jijl <uk^                  TPS 1966, If
    afriwan ('prywnh) =»*prywn, "frywn
    blessing, praise                                         39 »5>y B,S                <^>^    jAr-^'u-O
    TSP 17.39; KG pl77                                          somebody
                                                                a8e  (»8y, »8>k) ©abl. Wh -^'kw^Syt

  25 wprywncyk
     afriwancik      S    ^j^ij^fCjijlj^^iJtty_jl
                                                                GMS
                                                                  7.80 1580; S W, SGI 1986, 408-10; *&yk, TSP
     praising
     Hen. Tales. 486.13, -w                                  40 'WycCw) B,S                              j«r>>o*r
  26 "prywnh       S =* »prywn                                  a8ec(u) =**8c(w)
                                                                something, anything
  27 Mbwx
```


## [2026-09-14T00:54:54.632Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT frinami\"; grep -n \"frInAmi\\|frīnāmi\\|frinami\\|a-frInAmi\\|āfrīnāmi\" BRT.txt | head -20; echo \"=== BRT frI-\"; grep -n \"^frI\\|^frī\\|frI-\\b\" BRT.txt | head -20"
}
```


### [2026-09-14T00:54:54.697Z] TOOL RESULT

```
=== BRT frinami
12891:•  j.  darvj'ain.Jitay-  f.  'langes  Leben': Sfrinami  tava  nara  daäAupaiti  vohu.}xH us.jTti  'jUi  (soll  heissen)  "ich  segne  dich, o  . .,  mit  gutem  Leben,  mit  hohem  Leben, langem  Leben"  Az,  7;  Vyt/.
=== BRT frI-
```


## [2026-09-14T00:54:56.713Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD afrin\"; grep -n \"āfrīn\\|afrin\\|ʾpryn\\|nifrīn\\|nifrin\\|āfurīdan\\|afuridan\\|āfrīdan\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-14T00:54:56.768Z] TOOL RESULT

```
== PHD afrin
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
PHD.txt:1017:bless āfrīdan.
PHD.txt:1019:blessing āfrīn.
PHD.txt:1469:curse nifrin.
PHD.txt:3199:praise (n.) afrin, burzišn, niyāyišn, stāyišn, šnāyišn.
PHD.txt:3200:praise (v.) āfrīdan, burzidan, stūdan, (stāyīdan), šnāyīdan,
PHD.txt:3202:prayer namāz, niyāyišn; ahunawār, āfrīnagān, hūmāst.
PHD.txt:5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
PHD_mackenzie.txt:874:   afridan, afrin- I afur- ['jjlytn l , 'plyn-, )pwl- I M )p(w)ryd, 'pwr-, P
PHD_mackenzie.txt:876:   afrin ['pryn' I M )pryn, N afarin] praise, blessing. \\!.'.1A. nf"y·n
PHD_mackenzie.txt:3737:nifrin [nplyn l I N -] curse.
PHD_mackenzie.txt:6337: curse nifrin.                                wiyabanenidan.
PHD_mackenzie.txt:7317:praise (n.) afrin, hurzisn, niyayisn,          progress (y.) wihez-.
PHD_mackenzie.txt:7323:   afrinagan, homast.                          promote franaftan, abgar-.
PHD_mackenzie.txt:9958:nifrin
PHD_mackenzie.txt:11416:               '\)~ QY                 afrin-
PHD_mackenzie.txt:11442:afrinagan                  \,...~¥\~          aweran                \~Cl>*
PHD_mackenzie.txt:11452:afuridan                    \\~'t)I           abesug         \~~Cl)'
```


## [2026-09-14T00:55:06.191Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"frinami\\|fri-nami\\|frinaiti\\|äfriti\\|afriti\\|frita-\\|frya-\" BRT.txt | head -30"
}
```


### [2026-09-14T00:55:06.241Z] TOOL RESULT

```
8860:amanha  asti  masyd  gfurvaya  hl . .  zUvarp Y.p.28;  —  ai  .  .  mainyßm  zara%uströ v^jtttl  (sd.)  yaste  I  ascil  spSmstd  Y.  43.16; —  ySi  mffi  ahmii  s^rao/^m  dqn  I  cayasla (NP.) "'  upä.jimm  (sd.)  . .  ". .  die  mir  ihm Gehör  schenken,  all  die  .."  Y.415,5;  —  MiSl Spants  mainyti  ,  .  asäunl  cBÜ  (sd.)  yä  3i lelcä  vakistä  .  .  drvgvä  baxhitf  (sd.)  Y. 47.  S ;  verwend.  12.  i ;  — *spaydti  vispa  tä ^aobna  yä  I aca  (APn.)  virxyäti  V.J. 4)  in  negativen  Sätzen  'irgend einer",  mit  der  Negation  'keiner,  niemand, nichts';  im  Ap.  mit  folgendem  (iy\  nur substantivisch:  tnä  Icis  at  vi  dngvatS mq^rqscä  gs/tä  säsnas^ä  (sd.)  Y.31.1S; Mä  läfpaurvö  bäioyalfa  nS  Y.ff.21; 10.123,  /7.54; — mä  lafiars(sd^)  a:vs yat  tristem  V,j.i4;  —  nStt  zi  iü^  aAhä drujs  nyäsäite  (sd.)  FrW.  8.1;  ■ —  naioa jainti  na^a  fraSsyäti  (sd.)  "keiner vermag  . ,"  Hx.  14.^/6;  —  atvahe  . .  zänu.- asti  äfritiS  (sd.)  .  .  "israyqm  naiäa I tti  V.  iS.ii;  —  n3it  cahmi  sasva  (sd.) yS  .  .  FrD._j;  3;  —  mi^r^m  .  .  yü  nffii kahmili  ai7tii.draoxls  Yt.  io.  17;  —  II  mit kasäy  naiy  adari'naus  (sd.)  i  cilay (ASn.)  '^astanaiy  .  .  "wer  immer  es  war, er  wagte  nicht  irgendwas  zu  sagen  .  ." Bh. /.  13,  a)  mit  Gen,  part:  nöit  zt l  eis  asraosyanqm  tanunqm  asahe . ,  viaäiti P.  /j ;  —  mi^rjm  . .  yö  nöit  kahmät  mi'^rS.- drujqm  .  .  aojS  daiiäiti  Yt. /O.62;  62;  — yaiia  vli..yakmai  ttStt  cahmäi  naiitianqm karaiia  (sd.)  pairi.vasnei'^e  Yt. /_j,  3;  — nsit  iahmäi  ap>r»näyunqm  N. //;  —  D  mit Uy:  naiy  aha*  (sd.)  marttyJ'  naiy  pärsi^ .  .  naiy  amäxam  taumäyä  kalay  hyt^  .  . Bh. /.  13,  5)  gAw.  im  Nebensatz  mit yes%   'jeder',    substantivisch:    kadä    valdä
12891:•  j.  darvj'ain.Jitay-  f.  'langes  Leben': Sfrinami  tava  nara  daäAupaiti  vohu.}xH us.jTti  'jUi  (soll  heissen)  "ich  segne  dich, o  . .,  mit  gutem  Leben,  mit  hohem  Leben, langem  Leben"  Az,  7;  Vyt/.
16115:nach   vom    sich   wendend,   sich   weithin  •  j.,  g.  'parsna- Adj. 'gefiillt,  voll':  afriti
18195:•  j., g. fräy-V. 'befriedigen'.  Praes-i/rr'*, 1 1  a  fnna-  ■.frln-,  1 1  b  */ryan-*\  —  PPfP. 'frita-,  /ri^a-  (sbes.),  /rfna';  Inf.  /rine.
18358:•  j-,  g.  'frya-  Adj.  (fem.  °yä-)  'lieb,  wert, freund':  //.V  zT  drpgvä  yS  dngviiits vahistS hvö  asavil  yahmäi  asavä  °ryS  "denn  der ist  (selber)  ein  Z^n/^enosse,  der  dem  Drug- genossen  wohlwill,  der  ein  ,^/aanhänger, dem  der  ^i^iäanhänger  wert  ist"  Y.  46^-6;
18362:•  ].  "frya-  m.  EN.  zweier  Gläubiger:  °yehe a'saonö  i)  Yt  13. 110,  2)  Yt  13. 119.
20910:YtÄ  48.  f)  GPra.:  mtirS  vtspS  matda'\  hacaite  asis  .  .  uyrasca  dämdis  upamanO yasnanqm  yam  asaenqm  fr}},wä{sd.)cit  .  .\uyrasca  asaonqm  frava^ayS  yasla  pouru- Yt./o.i3ci,  IIB) bedeutungslos  erscheint  HflOT  hairaks\%A:)  Yt.  /o.  66.  b)  NSf.: uns  das  Relativ  vielfach  dann,  wenn  es,  j>'n^  dim  upanhacat  yä  uyra  naire  kam.' ohne  dass  ein  Verbum  folgt,  dem  Nomen,  1  z-'n/vift'/ Yt. /p.  39;  —  aiHi  ätm  atwyäiti mit  dem  es  kongruirt,  und  dessen  Attri-|_V'l  dahma  *va»uhi  afritis  P,J2;  —  kai buten  vorausgeht  a)  im  gAw.;  I)  \\a\hE  vä  i7j><«  (Sp.  237  m.)  *v?nzyap  ya  näi- Nominativ  oder  dem  ihm  gleichen  Akku- ,  rika  N.  6;  —  saoayeiti  yü  hava  daena  H. sativ.  Die  Fälle,  die  hierher  gezogen  wer-  2.9;  it']  —  ks  yä  kaine  'V.i4.-i^^'>'>;  — den  können,  sind  unter  IIB  verzeichnet:  [hierher  oder  zuIB  (Rel,  in  Kongruenz  mit Y-JO-S  0'^  dr3gva\  4ü.z  (ysi  uxsanS  Atm  Praed.):  *kä  larJ.maitisl  ya  kaca asnqm),32.i.%{yä  karapuäsm  k3Vltasi^,\dainay3t  milzdayasiiStl  apastüitii  U.  4t; 45- 1  (ya  n^qs  sadra),  46.Z  (yy  vä  iiiDi' —  ya  papiiiua  vasö  acisße  (sd.)  N, yä  galhä  datdl  *aSnaAhFj  usw.  Z)  in  ■  62.       c)N.-APm.r  *'taty5i  taxma  xitavayB
25026:—  "^wal^a  myasdaiM  '^waSca  ratufrita- yalia  Vt.4.2;  ti.Sl';  —  x^aA/zii  'tav5 'Vr.14.3;  —  aSaisqm  'tavö  azdai  N.  5j; 102.         \S..iQ.  17;    lies    ratus.m?rrta\    —
25301:•  i^  g.  'rätay- :  raiti-  i)  Adj.  'dienstwillig;  \ Diener,  Gehilfe' :  mßiryin .  .yaihe  aita  *tayB  l ..  spass  ätfhsire  Yt  10.  45.  i)  f.  'Dienst, Dienstwilligkeitj  Pflichterfüllung':  aAurit  na na  avarS  (sd.)  shmä  (3p.  270  o.)  °töis. yüsmävalqm  ".  .:  so  wollen  wir  bereit sein  euresgleichen  zu  dienen"  Y.  2g. ' 11".  a)  bes.  in  religiöser  Hinsicht:  avis\ nä  antan  hSntü  mmaifaitji  ctärä  '/ayS' "oflfenkundig  sollen  unter  uns  werden  die deutlichen  ehrerbietigen  Pflichterfüllungen" ^•33-  7")  *'*•  P- J^  ™''  der  Ausführung:  [ tä  ävifj'ä  °tayg^^  antar?  *afm^sca  sp?nts iaoiyantas^a  fräräUllca  *vldlsäs(sd.)ca arttan  *^3dainäif  asaonis  "die  sollen offenkundig  werden  die  Pflichterfdllungen zwischen  den  ASp.  und  den  Sao^y.  und , die  Freigebigkeit  und  Mildtätigkeit  zwischen  I den  rechtgläubigen  Retigionsgenossen"  P. ^■,  — yäti  catica  . .  dahmS  aiava  *kaurvh *'itl^''''  dähaj  a0i  dim  aiwyäiH  yä dahma  vatshi  äfritis  "so  oft  ein  recht- gläubiger Gemeinder  seine  religiösen  Pflich- ten völlig  erfüllt,  .  ."  P.ja.
28900:•  j.  *ha-j'Äai»h«m ''  Adv.  'in  Erfüllung  der Bitte' :  ä  hlpasiaüa  frinaiti  atarl. .  xhiüto atbistö  •nhm:  Upa  äa/3  haxMt  . .  "ihm wünscht  Äf.  dann,  wenn  er  zu&ieden  ge- stellt, nicht  gekränkt  ist,  in  Erfüllung  der Bitte;  'es  möge  dir  zu  teil  werden  . .'" Y.52.9f.;  V.i&26.
```


## [2026-09-14T00:55:07.258Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"afrin\\|āfrīn\" HRN.txt | head -20; echo \"== HUB\"; grep -n -i \"afrin\" HUB.txt | head -20"
}
```


### [2026-09-14T00:55:07.321Z] TOOL RESULT

```
776:39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
== HUB
```


## [2026-09-14T00:55:15.589Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 776\nimport itertools\ncum=0\npages=t.split('\\f')\nn=0\nfor i,p in enumerate(pages):\n    n+=p.count('\\n')+1\n    if n>=776:\n        print('leaf',i,'printed',i-21)\n        print(p[:1800])\n        break\nEOF"
}
```


### [2026-09-14T00:55:16.746Z] TOOL RESULT

```
leaf 30 printed 9
- 9 ~
34(2). äänä, äsnäh 'Öchwinuner, Schwimmerei', üsnäh^ dsnäiv,
aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
vergl. aber aw. asnätar-, skr. äsnäna- (*Bad').
Vergl. sina (No. 792).
35. äsyäne, äsyän 'Nest'.
a + aw. Ksö- bezw. gäi>. syä- ruhen' ^), oder wohl
bereits wohnen'^). (Nöldeke, mündliche Mitteilung).
Aber das y ist auffällig, vergl. np. süd,
36. üyärden, ayäriden Verschlingen*.
ai. ä + l/^gar- {jacjdrd) verschlingen' ; lat. coräre,
wa;^. nez-yar-am verschlingen*.
In der Bedeutung Verschlingen' vermag ich das Wort
nicht zu belegen. Bei AM., wo es sehr häufig vor-
kommt, bedeutet es immer vermischen, einweichen in'.
In der letzten Bedeutung könnte es zu skr. l/^ghar-,
ghdrati 'besprengen, beträufeln* gehören^).
37. äftäh *Sonne, ixDS'X (jüd.-pers.).
skr. "^ahha + tapa- (vergl. No. 3).
kurd. LW. a^taw (Houtum-Schindler), ätätv etc.
(Jaba-Justi).
38. äfdutn 'letzter', nur im Mujmil ettevärT;^ (ed. Mohl,
Journ. asiat. 1841, S. 178)^), vergl. hafdum zuletzt*^).
«) Hübschmann, ZDMG. 38, 431.
') Bartholomae, Arische Forsch ungren II, 102.
*) Dazu wohl auch äyisten, z. B. AM. 14 Zeile 16, 193 Zeile 11.
do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
*) Vergl. Spiegel, Grammatik der- Huzväresch-Sprache, 76.
^) Für bäfdum (d. i. be äfdum) haben die Wörterbücher folgende
Belegstellen: SF (S. 95 Vers 53), Metrum Remel:
kär-i dänä nek^ gerded bäf^dum
FR, Metrum Muteqärib:
ci bäyedf kerden kenün bäf^dum
meger -j^äne-röbl cü robeh bMum
Abu SukUr.
FR, FJ, Metrum Muteqärib:
b^r esb-i gümän ez reh-i räst^ x^m
q^räret bedöze-^ büved bäj^dum
Esedl.
```


## [2026-09-14T00:55:20.072Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==32' HRN.txt | head -40"
}
```


### [2026-09-14T00:55:21.236Z] TOOL RESULT

```
— 10 -
aw. *up((tama' letzter ; phlv. afdiim, päz. awdum
'letzter.
39. äfvtden ^schaffen, Praes. afrin-em, afrUegär (AM.);
afrtn 1) 'schaffend' 2) 'Lob', vergl. nefnn 'Fluch'.
aw. afrmami 'ich preise' etc., äfrlna- 'Segen'; phlv.
äfritan 'schaffen', afrm 'Lob', nafrm 'Fluch' (AV.);
ai. Ä + i^prT' 'befriedigen' etc.
Die Bedeutung 'schaffen' geht nicht über das Pehlevl
hinaus. Oder zwei ganz verschiedene Verba?
40. ägäh, kundig, Kunde'.
aw. ä + i^kas-, äkasat er erblickte'; phlv. äkäs, äkäslh^
äkäsimtan, arm. LW. akah 'kundig'; ai. Kiä^-, ka^ate
'sichtbar sein, erscheinen, überblicken'.
afy. bei. LW. ägäh.
41. ägenden 'anfüllen', ägenis^ ägm 'voll'.
skr. ghana- 'dick, voll von etwas', m. 'Klumpen',
ähandS' 'schwellend, strotzend'; vergl. lit. (/awd 'genug,
ksl. gonüi 'genügen'^).
42. äluden 'beschmutzen', Praes. äläy-em,
phlv. lütak (AV.).
lat. Inf um; air. loth 'Schmutz'; lit. lutyna-Sy lutgn^
(fem.) 'Pfuhl, Lehmpfütze'.
Durchaus unsicher, da np. äläy-em dann die se-
kundäre Form und ü ursprünglich sein müsste. Auch
scheint die Grundbedeutung von älüden 'beschmieren*
zu sein, vergl. AM. 35, Zeile 6; 40, 16.
43. äluh 'Adler'.
phlv. äluh (Kärn. 59, Note 2), vergl. arvä (Bund.)
in Zendbuchstaben.
Dazu gr. ögvig 'Vogel'; ksl. ortlü 'Adler; lit. erilis;
got. ara\ corn. bret. er, cymr. eryr 'Adler? Vergl.
Hörn, KZ. 32, 583 No. 14.
FK will des falschen Reimes halber in dem letzten Verse statt ^em
vielmehr gom losen, während FJ danach mit Unrecht die Aussprache
bäf^dem für richtig erklärt.
»j KZ. 32, 579 No. 4 war mir leider Rüokert ZDMO. 8, 286
entgangen.
```


## [2026-09-14T00:55:32.665Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in range(255,268):\n    p=pages[i]\n    head=' '.join(p.split()[:12])\n    print(i, repr(head[:120]))\nEOF"
}
```


### [2026-09-14T00:55:33.780Z] TOOL RESULT

```
777
255 'ی آشنا کر خابة سک آنی است ۷ . خالهرا نیز گویند'
256 'آشناو ۳ ف_ رای فرشت ۰ بمعنی شناور باش که شناکننده |'
257 '۰- 1 حه شا فه ۱ - بروزن\u200cتلزبانه.بمعنیآشیان است که خانهٌ مرغان'
258 'شخصی دییگر - وبمعنی تحريك\u200cنمودن وبرشورانیدن بجنگه هم هست که جربی اغراء'
259 '"-هِ- " ]غود ع بنم ات و سکون واو وزای هوز. ..'
260 'گذارند . ۶ ] قتاب\u200cز درد دوه بکس بای ابجد . کنابه'
261 'ملکی باشد . * [ سا فه - با سن\u200cبی فطه\u200cبروزن آستانه'
262 'آقای ۱ هت آقال ۱ - بر وزن پاماا , افکندنی |'
263 'کپ هن اف ودک از فارسی 9 کویند و آن کرداکرد اندرون'
264 'و بکرکاف فارسی محکم بتهراگویند ۱ . ] گففت - بنتح کاف'
265 'و شین فرشت » بممنی در آوجخته باشد چه اندر آکیشید پمنی'
266 '۲ ۰ وا آلان ِ پروزن\u200cبالان » ام ولایتی ونم محله ایست'
267 'کت ۱ آننک و امٌال اینها باشد 0.٩\u200f ۲ لر - بروزن'
```


## [2026-09-14T00:55:40.450Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'آفرین' in p or 'آفريدگار' in p or 'āfrīn' in p or 'afrin' in p.lower():\n        print('--- leaf',i,'printed~',i-210)\n        import re\n        for line in p.split('\\n'):\n            if 'آفرین' in line or 'afrin' in line.lower() or 'آفري' in line:\n                print('   ',line.strip()[:200])\n        if i>275: break\nEOF"
}
```


### [2026-09-14T00:55:41.658Z] TOOL RESULT

```
--- leaf 54 printed~ -156
    تخستین چوکاوس با آفرین ‏ . کی آرش دوم‌بد» سوم کی نشین .
--- leaf 188 printed~ -22
    کویند « در پای تو میرامیعنی در پای تو بمیرم و «جهان آفرین بر تو
--- leaf 195 printed~ -15
    چشم خوش نوکه آفرین باد برد
--- leaf 227 printed~ 17
    بمعنی آفرین و جاركايهٌ -
--- leaf 241 printed~ 31
    شتین چوکاوس با آفرین
--- leaf 260 printed~ 50
    آنها که مهمترین آفرینکان بشمار میروند » در عتن اوستای کلدنر 261006) باين ترتیب ضبط
    (برای شرح نها رلك : خرده‌اوستا تألیف آقای پورداود) آفرینگان مرکب است از آفرین بمعنی
    دعا و نيایش . و همچنین بممنی دعای نيك وستایش است در برابر نفرین ( رل : آفرین ) دهارله
    از اطاعت باپدر زردشت بر خود بنك آفرینگا نکنته است
--- leaf 261 printed~ 51
    ع رکب : جهان آفرین, سورت آفرین . جانآفرین » محر آفرین» دادا فرمن وغره» رد «لغت ناحه>.
    آفر دار - پهلوی له د مناس ۲:۷۹4 * خالق . آفریننده . صفتی از صفات
--- leaf 308 printed~ 98
    مشغول بود بقتل در آورد و به آفرین و همای
```


## [2026-09-14T00:55:45.002Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==262' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-14T00:55:46.178Z] TOOL RESULT

```
ملکی باشد . *
[ سا فه - با سن‌بی فطه‌بروزن آستانه ؛
اضانه وس گذشت راکوید .
۲ فگا نه با اف فارس‌بروزن آیخانه.
شود و بسنی گوبند نان خورشی است د رکیلان
و آن چتان است که زرد* تخم‌عرغ را درشیرخام
بر‌بزند و نيك بر هم زند و بی بالای آتش نهند
تا شیر مانند دلمه بسته شود , بعد از آن شیرینی
با خشکه و پلاو در عبان آن ریزند و با قاشق رو
خورند - ولوزنعرا فل آفروشه کوشد وبلفور ‏
گندم را هم گوبند ِ#
] فر پدون ۱ ۰ بسکون ثاك . نام
نی ات وف
ند . 3۶
] قثك - بروزن پابند . جنگ و جدال
وعداوت وخصومت را گویند .
آ نف الک - یک ثالت و سکون بون
و دال بی نقطه بالف کشبده و یکاف زده » قوی
وقرح را ؟
| گنل یدن « بروزن آدم دیدن .یمعتی
جنگ و جدال و عداوت و خمومت کردن
باشد . #
آقر ین ۲ » بروزن آنئین» بسنی‌تحین
و ستایش و دعای نيك‌باشد - ویمعتی آفر‌ناده
متداول‌است ۴ سونام روزاول خسفُسترفه سالهای
٩ ۰‏ -رك : فی‌بدون و آژی دهالك . ۴ - بممنی ژه » زهی , اجسنت : اوستا 2101۷2۳2
د بارتولمه ۳۳۱ . پهلوی 21718 « تب رکت4 » , « اونوالا ۳۱۵ » مرکب از 71 + بوند
2 مقابل‌نفرین ( 20 + 21118 ) بممنی لعنت ۶ دائرتالمعارف اسالام   .‏ ۳ - درکلمات
ع رکب : جهان آفرین, سورت آفرین . جانآفرین » محر آفرین» دادا فرمن وغره» رد «لغت ناحه>.
۴ - آفگانه کردن» بچه‌افکندن . «لت‌نامه» ‏ ۵ رك : آزفنداك و آژفنداك .
آفر دار - پهلوی له د مناس ۲:۷۹4 * خالق . آفریننده . صفتی از صفات
خدا. ركك : آفربدن . * آفریدن - بهلوی 2111020 « تب رکک 4» «منای ۲۹۶ : ۲ »
از مصدد اوستائی 1۲1 بمعنی دعا وناش ؛ درسانسکربت 2-5 < پارنولمه ۵ »؛ خلق, ابجاد ,
فتت گرفان : آفریده _ پپلوی 2 «مناس ۷۹6 : ۷» مخلوق ء خلق :
بان آو که خدا آفربدماست ازهیج دقیقه‌است که هیچآفریده نگشاده است . حافتدلفت‌نامه».
م آفریتگات ‏ رك : آفرنگان. ۵ آق ‏ در ترکی و مفولی بمعنی سقید
« داثرقالمعارف اسلام » . آق اردو ( اردوی سفید ) عنوان مسکن فبیلة اردا ( در دشت قبچاق )
بود و رنگه سفید در میان مفول بر رنگه آبی برتری و تقدم داشت . مسکن قبیلةٌ مزبور مقابل
ک و که اردو (اردوی آیی) که عئوان فسمت دست چپ فبایل مطیم بانو بود- قرار داشت.فطیقات
ملاطن املام س ۷۲۰۱»: 11 قوبنلو (دارای نز نان « گوسیندسپید» ) نام طایفه‌ای از تر کمنان است
که از ۷۸۰ تا و۹۰ در آیربایجان حکومت کردند « هرن . تاریخ ایران ۱۳۰ 5
۵ آقا _ < آغا. مفولی . در ترد مفول نامی بوده که برادر کهتر ۰ برادو مهتر
را بدان میخوانده « لفث جفتابی و تر کی عثمانی جح ۱ ص ۱۶ > « عاث اللفات » و ححنی
اسلی آن بز رکه بودء » و احالی خوارزم عم ( برادر پدر ) را آقا میگفته اند « دائرة المعارف
لاسلامیه ج ۱ : آق وآغ » « داثرة المعاوف بتانی ج | ص۱۱۱ * .(گی چه دراتدا اطلاق این
له فقط پرادر بزرکتر وعم ميشده ولیک ک‌هر امیر بر هه رئیس وشریفی را آقامیواندن.
بقبه در صفحةٌ 6۲
```


## [2026-09-14T00:55:57.413Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\np=pages[217]  # 1-based leaf 218\nprint(p[:2500])\nEOF"
}
```


### [2026-09-14T00:55:58.597Z] TOOL RESULT

```
302
Saraba                                                                       203                                                  Saı amdar


=         -       Saraba:        "Wagen"           ist        nach    Ml.         ein    arabisiertes         tk.    Wort,        Johnson
         bezeichnet               es       als     Wort           persischen            Ursprungs        1,


     -                                                  Pr
lu            -    Casäkir:           Pl.     v.       Lu askar          q.        vv

 Pr
me        - Caskar:              "Soldat,              Armee"            pers.           X) laskar        ? mp.           BER) laSkar        °,
         mand.        Caskar *, aram.                             Nas.
          Laskar:
          ind.       Matrose
                            "Matrose,
                                       od.
                                                   Soldat"
                                                  Kanonier           _
                                                                         pers.
                                                                         pers.. is
                                                                                        >    ar.
                                                                                             Laschkar
                                                                                                     >    engl. B>) frz.
                                                                                                              >
                                                                                                                                   lascar,/



     _                       _
SA - Caskari:                         "Soldat" s. Caskar,

=.                - Saskariyya:               "Heeresdienst".

2-12:! - Catärid:
            -
                                      "Merkur"               pers.                “Tr
                                                                                   Stir ep.                7     n
                                                                                                         *tira-däta.

urue - Safarit: Pl. v.                                       ws. Sifrit g. v.

uss -              Sifrit:        "Dämon"              pers.             ra [ äfarid            v.   äfaridan            "schaffen"    mp.
                  uweo» afri
```


## [2026-09-14T00:56:02.837Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[217][2200:4200])\nEOF"
}
```


### [2026-09-14T00:56:03.949Z] TOOL RESULT

```
                                         *tira-däta.

urue - Safarit: Pl. v.                                       ws. Sifrit g. v.

uss -              Sifrit:        "Dämon"              pers.             ra [ äfarid            v.   äfaridan            "schaffen"    mp.
                  uweo» afritan
                        afritan a.                            a-fräy          .


CyYas - Cifrin:                   "mächtig"                  s.    Cifrit u.            pers.      Aus f afaridan           q. ”


4         - Cakkäz:              "Stock"           v.        pers.    0, |, kawäze od.               gawäze         7,    mand.     gauaza


Ik            - “akäkiz:              Pl.     v.        „Us Cakkäz q. v.
      BG                                                      .
BIT               - Sakäkiz            pl.        v.     sk        Cakkaz         q.    v.


Its            - Salamdär: "Fahnenträger" er. d« “alam + pers.                                                           suff. _l» dar v.
              caul, daßtan "haben" mit der Bed. "Fahnenträger".



1.       Johnson        S.       846.
2. Wahrmund
         s. v., Muhit
                   s. v.
3.    Mackenzie              s.       v.
4.    Macuch          S.     v.
5.       Fremdwörterbuch                     s.    v.,        Wahrig        s.     v.
6.    Nyberg          Bd.        II     s.    v.
7.       Chista       Bd.        10    S.     1191.
```


## [2026-09-14T00:56:13.782Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== IEC pardakos\"; grep -n \"pardakos\\|pardak\\|pṛdāku\\|pardaku\\|pardāku\" IEC.txt | head -20; echo \"== IEC pers- / prs-\"; grep -n \"^persō\\|^pers-\\|^pr̥s\\|^prsō\\|^prso\\|^pars-\" IEC.txt | head -20"
}
```


### [2026-09-14T00:56:13.873Z] TOOL RESULT

```
== IEC pardakos
== IEC pers- / prs-
12775:pers- (1) ‘athwart, counter-, crosswise’. Cf. perquo OE feorsian, v. ‘pass, excel’; OCS cf. présovü, OR peresov ‘beam, rafter’ cf. also R prjàsio *crosspiece'; Cz. přes over, across’; cf. also OCS présme, n. ‘interruption, pause’; Hitt.
12786:pers- (2), persno-, see pters- Av. pāšnō, m. (heel; Skt. cf. parsnih, f. id.; Go. faírzna, OHG férsana, f. id.; Lat. perna, id.; Hitt. c£. (queried) parsinus (for *parsnus, pl. (knees in view of parsna-, v. ‘kneel, crouch’). For W ffern, f. 'ankle-bone': Gk. ptérna, see ptersna
```


## [2026-09-14T00:56:14.927Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN pard\"; grep -n \"^pard,\\|^pard \\|^leopard\\|^pardal\" KLN_1966.txt | head; echo \"== SKT\"; grep -n \"^PARD\\|^LEOPARD\" SKT.txt | head"
}
```


### [2026-09-14T00:56:14.999Z] TOOL RESULT

```
== KLN pard
27379:pard,  n.,  partner  (slang).  —  Abbreviated  fr. pardner,  a  slang  variant  of  partner, pardao,  n.,  a  former  Portuguese  gold  coin  of Western  India.  —  Port,  pardao,  ult.  fr.  OI. pratapah,  ‘splendor’,  which  is  formed  fr.  pref. pra-,  ‘before,  forward,  forth’,  and  tapati,  ‘makes warm,  heats’.  OI.  pra-  is  cogn.  with  Gk.  ttp<S, ‘before’ ;  see  pro-  and  cp.  Purana  and  the  first element  in  Prajapati,  Prakrit,  prakriti,  Pralaya.
== SKT
13251:PARD.
13268:PARDON,
```


## [2026-09-14T00:56:20.300Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (574,575,576,577):\n    p=pages[i]\n    import re\n    if 'pard' in p:\n        idx=p.find('pard')\n        print('--- leaf',i)\n        print(p[max(0,idx-300):idx+1500])\nEOF"
}
```


### [2026-09-14T00:56:21.646Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:56:24.012Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pardus\\|pardos\\|prdaku\\|pṛdākuḥ\\|pardalis\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T00:56:24.063Z] TOOL RESULT

```
6273:camelopard,  n..  the  giraffe.  —  Lit.  "camclpard  . fr.  L.  cametopardus,  fr.  Gk.  y.y.-irp.'n.y.zh’X/.iz, which  is  compounded  of  Gk.  xiur/.o:,  'camel', and  —xpSxXu;,  ‘pard’.  See  camel  and  pard  and cp.  leopard.
21494:gen.  Xeovxo?,  ‘lion’,  and  68<!>v,  gen.  oSovto?, ‘tooth’.  See  lion  and  odonto-  and  cp.  dandelion. Leonurus,  n.,  a  genus  of  plants,  the  motherwort (hot.)  —  ModL.,  lit.  ‘lion’s  tail’,  fr.  Gk.  Xitov, ‘lion’,  and  oupoi,  ‘tail’.  See  lion  and  uro-,  tail- . leopard,  n.  —  ME.  leopard ,  lepard ,  fr.  OF.  leo¬ pard  (F.  leopard),  fr.  L.  leopardus,  lit.  ‘lionpard’, fr.  led,  ‘lion’,  and  pardus,  ‘pard’.  See  lion  and pard.
27377:parclose,  n.,  a  screen  or  railing  (archit.)  —  ME. parclos(e),  fr.  OF.  parclose,  ‘enclosure,  end’, prop,  fem.  pp.  of  parclore,  ‘to  enclose,  shut  in’, fr.  par-  (for  L.  per)  and  clore,  ‘to  close’,  fr.  L. claudere.  See  per-  and  close,  adj. pard,  n.,  leopard  (archaic)  —  ME.  parde,  fr.  OF., fr.  L.  pardus,  fr.  Gk.  rripSo;,  rcipSaXn;,  ‘pan¬ ther’,  generally  connected  with  OI.  prdakuh, ‘panther,  tiger’.  It  is  more  probable,  however, that  Greek  KocpSog  has  been  borrowed  fr.  Heb. barSdh,  ‘spotted’  (said  of  an  animal),  and  lit. denotes  ‘the  spotted  animal’;  see  Heinrich Lewy,  Die  semitischen  Fremdworter  im  Grie- chischen,  Berlin,  1895,  p.  7.  For  the  change  of Heb.  *  top  in  Greek,  cp.  Gk.  Eup&>7rr),  ‘Europe’, fr.  Heb.  ‘erebh,  'evening,  west’.  Cp.  leopard camelopard,  guepard.
```


## [2026-09-14T00:56:32.105Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nfor f,ln in (('KLN_1966.txt',27377),('KLN_1966.txt',21494)):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f'); n=0\n    for i,p in enumerate(pages):\n        n+=p.count('\\n')+1\n        if n>=ln:\n            print(f,ln,'leaf',i,'printed ~',2*(i-12),2*(i-12)+1); break\nEOF"
}
```


## [2026-09-14T00:56:33.137Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==13252,NR==13252' /dev/null; sed -n '13240,13270p' SKT.txt"
}
```


### [2026-09-14T00:56:33.362Z] TOOL RESULT

```
KLN_1966.txt 27377 leaf 590 printed ~ 1156 1157
KLN_1966.txt 21494 leaf 462 printed ~ 900 901
```


### [2026-09-14T00:56:34.518Z] TOOL RESULT

```
■r&lysiB    (.L.-Gk)     L.  far^ns.'~
r<a/dX»<it.  a  loo<«ning  aside,  disabling
BTca.  paralysis  or  palsy.  —  Gk.  impa-
».  Co  lootcn  aside  *Gk.  vo^  beside;
K   to  lo«am,  allied  lo  I*o8o.     Der.
VM^  CpbCd  F.  paraljtstr,  verb  formed
F.    th.  par^yrit,   paralyib.      Also
^He*  from  CIc  ToyKxAvrt*^,  adlictetf
ll^"  (F.  - 1-  -Gk.)     M.  E.  piMtisy,
t  form   parl/ry.  »  F.  paralytii.  *  U
iL,  oipamiy$ii  (abort).
PARD.
329
Paramatta,  a  fabric  like  merino.  (New S  WoJci.)     So  named  from  /^aramatta,  a
town  near  Sydney,  New  South  Wales,
Paramount ;  see  Mount. Paramour ;  sec  Amatory.
Parapet ;  sec  Par«.
Farapbemalia,  ofnaments.  (L.— Gk.) Properly  the  property  which  a  bnde possesses  beyond  her  (lowrr.  Formed  by adding  L.  neut.  pi.  suffix  'o/ia  to  Low  L. ParapMema,  the  property  of  a  bride  over and  above  her  duwcr.  »  Gk.  wapa^tpva, that  which  a  bride  brings  beyond  her dower.  -■  Gk,  wa^,  beitidc;  <p*p*'^,  thai which  is  brought,  fiom  <f>ipttv,  to  bring, allied  to  E.  Bear  (l).
Paraphrase.  (F.  -  L.  -  Gk  )  O.  F. parapkrtue.^l^ paraphrasin,  ace  of  Mro- /^/-izrw. —Gk.  im/*«ifjia<T«,  a  paraphrase, free  translation.  —  Gk.  wapA,  beside ;  ^/xUrtf , a  phrase,  from  ^C'*S  ^^  speak ;  tec PhroBO.
Paraquito,  Parakeet,  a  little  parroL (Span.)  Siv»n.  periquito,  a  little  parrot, dimin.  oi  pence,  a  parrot.  Dtez  supposes perUo  to  be  a  nickname,  meaning  Miitla Peter,'  dimtn.  of  Ptdn,  Peter.  See Parrot,
Parasite.  (F.-L.-Gk.)  F.  parasiU. —  L  parasitui.  •-  Gk.  mtxpaakrtK,  eating be>i<Jc  another  at  his  table,  a  flatterer,  toad- catcT.  —  Gk.  »«pd,  bisidc;  ^lro%^  wheat, foqd.    Orig.  in  a  good  sense  ;  see  Gk.  Lea.
Parasol  ;  see  Poro,
Parboil ;  see  Bull  (a).
Parcel ;  ace  Port.
Parch,  to  scorch.  (F.-L.)  Very  diffi- cult  M.  K.  pan  hen,  to  parch.  Prob.  the same  as  M.  E.  perthen^  lo  pierce,  an  oc- casional form  ol penm,  to  pierce.  This  ii the  most  tikelv  soUiiion ;  in  fact,  a  careful examination  of  M.  K.ftrchfn  fairly  proves the  point.  It  was  nt  htst  osed  in  the  sense '  to  jiierce  with  cold,'  and  was  aiterwardt tmnsl'cried  to  ezprc^  the  effects  of  heat We  still  say  *purnng  cold.'  Sec  Miltoo, P.  L.  ii.  594.  —  F.  p<fx€r^  to  pierce,  See Plorco.
Parchment.  (F.-L.-Gfc.)  M  E./v^ chimin.  —  F.  parchemin.  —  L.  pergamina, p<r;^mtna^  parchment ;  fern,  of  L.  Perpi- men «j,  belonging  to  I'crgo m os  ( wh ere parchment  was  firit  invented).  ~  Gk. inpyn^i}y4l,  parchment,  from  nip-ya^ot^  Hip- TQ/Jor,  Pergamus,  in  Mysia  of  A<:ia  Minor.
Pard.  a  panther,  Icopanl.  (L  —  Gk.) L./anyMi,-Gk.«df8oi,   An  EA^^nwcn^  *,
I
PARDON,
PARENT.
I
```


## [2026-09-14T00:56:45.288Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('LEAF576:', ' '.join(pages[576].split())[:600])\ns=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(s))\nfor i in (390,391,392,393):\n    print('SKTleaf',i, ' '.join(s[i].split())[:300])\nEOF"
}
```


### [2026-09-14T00:56:46.496Z] TOOL RESULT

```
LEAF576: e ecology, oecumenic, oecumenical, adjs. — See ecumenic, ecumenical. oecus, n., a room or hall in a house. — L., fr. Gk. olxo c, ‘house’. See economy, oedema, n. — See edema. Oedipus, n., the son of Laius and Jocasta, king and queen of Thebes, who unknowingly slew his father and married his mother; he solved the riddle of the Sphinx ( Greek mythol.) — L., fr. Gk. OlSi7tou;, lit. ‘swell-foot’, fr. olSav, ‘to swell’, and iro’ic (gen. tco86? ), ‘foot’. See edema and -pod. oeil-de-boeuf, n., a round or oval window ( archit .) — F. ail-de-bceuf lit. ‘eye of an ox’, fr. aril (fr. L. oculus), ‘eye’, 
657
SKTleaf 390 poser, to put (above). oppose. ;F.— L. tfN</ Gk.> F. ,. to withstand.— L. op- (for ob) agtina;! poser, to place (above). poae (a), to puzzle byquestiaiiK (F- L. ant/ Gk.) M. £. appostn, to qoolioi not ically-F. apposer, but a comptios M. E. oppoien, to oppose, hence, to C0 question ; see opi>oBe abo
SKTleaf 391 L./ariV-itf, pp. oiponert, to set. settle. post <!)• a stake set in the ground. (L.)i M. E. post X A. S. post. — L. pcstis, a post ; i.e. something firmly fixed— L./o//itr, short for positus, pp. oi poture, to set. post (a), a military station, a public letter-carrier, stage on a toad. (F. — L.) Gri
SKTleaf 392 i, beil. postU. an explanator)* note or comtacD' tarj- on the Bible. <F-— L.'^ V pRSfi.^ Low L. postiila, a marginal note in a iiible. Derived by Ducange from h.pasf HU mtri%' i.e. after those words, because the glocia were added afteivards. post- meridian, pomerldi&n, longing to the aftemuoa. (L.) 
SKTleaf 393 r, pinner, an impounder. (E.) Formetl with stiffix -tr of the agmt from A. S. pyndan, lo pen up.» A. S. punJ, an enclosure. % Not allied \q pen (i). pinfold, a pound. (E.) Put for pinJ- /old; {a\<iO speXt pwtd-Jb/d).^ A. S. pynJan, to pen op ; (or pund, an enclosure ;) and /ofJ. pond. (E.) M. E. pvn
```


## [2026-09-14T00:56:59.883Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(586,594):\n    nums=re.findall(r'\\b1[01]\\d\\d\\b',pages[i])\n    print(i,nums[:10], ' '.join(pages[i].split())[:80])\nEOF"
}
```


### [2026-09-14T00:57:01.059Z] TOOL RESULT

```
586 ['1096'] s American birds of the family Icteridae. — F. oriol, fr. OF., fr. ML. oryolus, 
587 [] �orris root’, which is identical with Gk. Epecoe, gen. of Iptc, ‘iris’. See iris
588 [] vowel osche-, combining form meaning the ‘scrotum’. — Fr. Gk. Soysov, ‘scrotum’,
589 ['1103'] a vowel, osteal, adj., bony. — Formed with adj. suff. -al fr. Gk. ooteov, ‘bone’
590 ['1104', '1105'] h’. See oto- and cyst. otolith, n., chalky matter in the internal ear of animals
591 ['1106', '1107'] fr. OE. ofen, rel. to OFris., MDu., Du. oven, OHG. ovan, MHG. oven, G. Ofen, ON.
592 ['1108'] ddling, moderate, indifferent, tol¬ erable', orig. ‘being half-way up the height
593 [] n., a genus of plants of the staff-tree family (bot.) — ModL., compounded of pac
```


## [2026-09-14T00:57:07.070Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'pard,  n.,  leopard' in p or 'pard, n., leopard' in p:\n        print('leaf',i, re.findall(r'\\b1[01]\\d\\d\\b',p)[:8])\n        print(' '.join(p.split())[:200])\n    if 'leopard,  n.' in p:\n        print('LEO leaf',i, re.findall(r'\\b1[01]\\d\\d\\b',p)[:8])\nEOF"
}
```


### [2026-09-14T00:57:08.191Z] TOOL RESULT

```
LEO leaf 473 []
leaf 603 []
rm¬ ed from the stem of 7rapot-ria<iEiv, ‘to lay side by side’, whence also 7rapaTai;i<; > ‘arrangement’. See parataxis and adj. suff. -ic. Derivatives: paratactic-al, adj., paratactic-al-ly, adv. par
```


## [2026-09-14T00:57:11.654Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(598,610):\n    print(i, re.findall(r'\\b1[01]\\d\\d\\b',pages[i])[:6])\nEOF"
}
```


### [2026-09-14T00:57:12.879Z] TOOL RESULT

```
598 ['1120', '1121']
599 ['1096', '1122', '1123']
600 ['1124', '1125']
601 ['1126', '1127']
602 ['1126']
603 []
604 ['1130', '1131', '1132', '1133']
605 ['1134', '1135']
606 []
607 ['1136', '1137', '1138', '1139']
608 ['1140']
609 []
```


## [2026-09-14T00:57:24.334Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==94' HRN.txt | head -50"
}
```


### [2026-09-14T00:57:25.639Z] TOOL RESULT

```
72
kurd. plslk, pTsTk^ pTsT, pisile *Katze'; af/. />j^ö; bei.
[)üsi^ piinsJ, pisl (307) ; wa;^. pis, si;'n. pas.
Gewiss nicht zu ai. pncöha- ^Schwanz', wie Toma-
schek, Centralas. Stud. II, 762 will.
323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
(Castle aus der jüd.-pers. ßibelübs.).
plilv. pas(i)nci:fan (vd. 5 (6) 61.; Bund.), vergl.
(is(i)ncitan (siehe ^Verlorenes Spraehgut', No. 33),
das im Commentar immer für aw. yhaec- (auch für
visrascayen vd. 7 (77)) steht.
Zusammenhang mit l/"Aa^c-, hincaiti, ai. l/'sec-,
sincdti ist unklar, aber doch wohl vorhanden.
324. pegäh *Frühlicht, früher Morgen .
aw. upa ~r (Jäh (s. No. 889).
325. pul^) 'Brücke.
gel. purd.
aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
Bartholomae, Ar. Forsch. II, 35 folgg.); phlv.
puhrj puhl ^Brücke, Furt'.
kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
pul.
326. peleng 'Leopard'^).
skr. p^däku' *Tiger, Panther' (ai. pfdaku-^ pfdäkü-
nur *Natter, Schlange').
kurd. LW. pilink; afy. prang,
327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
phlv. panäh,, panähih^ vergl. Mitr]panähak (AV.).
Doch wohl zu l/^pä- schützen'?
Bartholomae stützt diese Erklärung brieflich
*) Das Wort ist nicht allzu gut beglaubigt. Die anderen Wörter-
bücher belegen es gar nicht, nur der FR hat folgenden Vers Leblbl's
(Metr. Muteqärib) mit der Aussprache bis^ :
be^enjer heme tens^ enjlde end
ber an /äk^ /üues bisetijlde end
2j Nie pul gesprochen oder geschrieben (Vullers), das nur
•Geld' bedeutet.
^) Felis pardus L. (Blanford, S. 34).
```


## [2026-09-14T00:57:36.402Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(630,660):\n    p=pages[i]\n    if 'پلنگ' in p or 'پارد' in p:\n        print('leaf',i,'printed~',i-228)\n        for line in p.split('\\n'):\n            if 'پلنگ' in line or 'پارد' in line:\n                print('   ',line.strip()[:180])\nEOF"
}
```


### [2026-09-14T00:57:37.551Z] TOOL RESULT

```
leaf 637 printed~ 409
    بشنگ بروزن پلنگه, نام‌پدرافراسیاب
leaf 642 printed~ 414
    پلنگان گوذن افکن- کنایه از
    پلنگر یکسر اول بروزن سئمگی » تام
leaf 649 printed~ 421
    نگ س بفتح‌اول بروزن پلنگه, دريجهةٌ
```


## [2026-09-14T00:57:39.863Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==644' BQT_v1_pages.txt | tail -40"
}
```


### [2026-09-14T00:57:40.975Z] TOOL RESULT

```
آدمی و کلش بناخن شیر میماند » و بیخ آن
۹ سیاه و ب رکه آن تارنجی میشود ؛ و در
جنگلهای هندوستان بیار است- وبیعنی بناعت
فلیل واندك هم‌هست - وموی اطراف سر را نیز
گویند. وچوبکی که ربسمان بر کمر آن بندند
و کفة ترازو را هم گفته‌اند - و بکسر اول و فتح
ثانی‌مضفف بروزن صله» ابرشم بود- وأنجه کرم
ابرشم برخود تنیده باشد ؟ - ودرخت بیدی که
۱ -ر4 : یلوان. ۴ - راد: پله.
0 هم فریزندی و برنی 06118 « 4
و چوبکی رانیز گویند بمقدار يك‌قبطه وهردوس
آن تیز میباشد وآن را برزمن گذارند و چوب
درازی بمقدار سه وجب برسر آن زنند نا از
زمین بلند شود و در وفت فرود آمدن ب رکمر
آن زد فا دور روده وآن بازیی است. مفهور که
آنرا پله‌چوب خوانند. وبفتح اول و انی مشدد
بروزن غله بمعنی‌درجه ومرتبه باشد- و هرمرثبه
و یابه از نردبان را کویشد ۴ , و پاین ممنی
با ئانی مخفف هم درست است- وبکسر اولوفتح
ثانی مشدد بر وزن چله. کفهٌ ترازو را گوند -
و بمعنی هرمرتبه و پابه‌از تردبان باشد» و باین
وزن و باین عمنی بجای حرف ارل نای فرشت
هم‌نیز نظر آمده است. الله اعلم.
پل هفت طاق « کنابداز حت فلك
باشد . ۶
فلیته > بنج اول و فوفانی بر وزن
خربطه , ينبه ولتهُ تاب‌داده را گوند ومعرب‌آن
فنیله است؛ خواء فتبلمُ چراغ باشد وخواء فتبله
داغ تک
پلید بفتح اول بر وزن بزید . سمعنی
مردار و نجس باشد - و مخفف پالید هم هست
که ماضی پالیدن است بعنی جستجو کرد وتفحص
لین ه بیوزن رسدل مضفف
بالیدن است که بمهنی جستجو کردن و تفحص
نمودن باشدا .
پلینف‌ی ‏ بروزن فرزندی, نام نوعی از
خربزه باشد که عربان بعایخ گویند .
۳ بهلوی 1 (رله : پلکان). گیلکی
۴ رك : فیل.
٩‏ - رك : پالیدن.
```


## [2026-09-14T00:57:46.961Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==643' BQT_v1_pages.txt | tail -45"
}
```


### [2026-09-14T00:57:48.134Z] TOOL RESULT

```
پلمسه بروزن وصوسه ؛ «معئی بلمی
۱ تر مضطرب شدن و دست و یاکم کردن -
وحتهم ساختن- و دروغ گفتن باق . ۲
‌ غ ک ۳ آن نوسند تا اطفال بخوانند -
ویممتی دروع غم گفتن و بهانه کردن- وتهمت‌نمودن
و متهم ساختن - ودست و پا کم کردن هم شظن
امه ای ۳ ۰
بلنگ بفتح اول بر ون خدنگه ۰
از رنگي
جانوری است معروف ۴ - و توعی
کیوتر باشد -
وجانوری‌هم هت
دشمن شیر
است ۴ -وجانوری
که‌آن,ا زرافه هم
میگوند ۵ وهر
چیز که در آن نقطها ی باشد -
و چاریابی را نیز گویند, و آن چهار چوب است
بهم وصل کرده که درمیان آن را بانوار و امثال
آن ببافتد وف بخوابند ؛ واین دد حندو مان
یدترهتعارف استب و بکر او و ثالی از یش
آستانه نا توادت ضخامت دیوار را کیش ععنی
میان در.
پلنگان گوذن افکن- کنایه از
دلاوران و بهادران باشد.
پلنگر یکسر اول بروزن سئمگی » تام
بادشاه زار زنکیان ود ودر بدا بدستسکندر
کنته شد. وبفتح اول هم گفته‌اند 1
بلنگمثك ٩‏ ع و فلنجمشكث بفتح اول
و کسر هیم. نام داروبی است. و وجه تسمیةٌ آن
به دانگی مشك آنمت که که آن دارو یگلهای
بت پلنک و برنگ آن میماند و بوی مك
میدهد.- وبیدمشك را هم گفثه‌اند.
بلواس « باوار بروزن المای » پنعنی
فربب وچایلوسی باشد ۷ .
هلو ان » نم ارذ بروزن نقصان, بلندی
۴ - ره : پلمی ویلمنه.
کننحد 001278 «یثوتن ۱ ٩‏ ص ۲۳*.
کاو پلنک کوبند. رد: اعت رکاو .
۲ وف :: باوی ۱
۵ پلکان یکسر
«ناوادباة ۱۱
- او دا شتر
۴ همان‌منی اواست. ه
(بر هان قاطع9۷)
```


## [2026-09-14T00:58:00.054Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    for w in ('پلنگ','پاشیدن','یوزپلنگ','آفریدن','آفرین'):\n        if w in p:\n            for line in p.split('\\n'):\n                if w in line:\n                    print(i, w, line.strip()[:200])\n            break\nEOF"
}
```


### [2026-09-14T00:58:01.253Z] TOOL RESULT

```
148 پلنگ ۲ / پارس» پلنگ
435 پاشیدن چم این واژه در زبان‌های کهن این فهرست: فررپاشیدن؛ صدمه‌ی شدید دیدن,
```


## [2026-09-14T00:58:03.935Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(\"=== page idx148 (printed\", 148+1,\")\")\nprint(pages[148][:2000])\nEOF"
}
```


### [2026-09-14T00:58:05.007Z] TOOL RESULT

```
=== page idx148 (printed 149 )
[pdf page 149]
۲ / پارس» پلنگ
پهلری (2۸(711): 8۸6 پسگشت‌ها اک ده
کردی (008013): ۳1 ۳۱
1 افغانی (پشتو) (/4701۸): 6 ۱ 539 (080۴۸80 ,755 (۸0ه)
سانسکریت (84(/3777): 80۸4 1 (1302۸80) :2/5
۱ یرنانی 07620): رانا :070078
: لاتین (7100مل): ۳5 3 (۳0۳۸30) باق6 (8۸330)
فرانسه (۳۳۸/3): دراد ۱.۱ :57
انگلیسی کهن (بلولا80/0 ۰:۵0 ۳8805 7 (7307۸330) ,429 (8۸30)
انگلیسی:(8(/0/84): 0 زرد دی :۸2۸43 4 تما
هیت (7/77778: 7۸18۸۸ ,8۸38۸۸ برهان قاطع : ۴۱۶۰
سغدی (50021۸(1): گرلداان نها
یادداشت:
۱ بیشتر واجریشه شناسان معتقدند که این واژه از زبان‌های هند و ایرانی به یونانی و سپس به لاتین و غیره رفته است.
۲- در اکثر زبان‌های اروپایی واژه‌های ۳۸183 جای خود را به (802۸/80] (۳۸0 + 1.102) داده است.
ِ
ْ
اوستایی (۸887۸۸): ۵۰ بشال8۸ اسپانیایی (3۳/۸//8): ۰ ۳۸718 ,8۸75
پهلوی (1/ماتله۳): 6 ۴28۸6 ایتالبایی (۷لمللم7): ۳۸371886 ,8۸37
بلوچی (16141ابلم8۸): ۸ رومانی (4(/۸0الاه): دبای ۱:۱
افغانی (پشتو) (۸70/7۸۸7). ۳۸۸۱۷ پرتغالی (۳۸3713:)0070010858 ,۳۸7
سانسکریت (84(/3777): رای اد انگلیسی (60/0/58/7):(از فراسه) ۴۸۲
8 80831 لبترانی (70۸//]4۸۷/.): ۳183۳31 ,ت۳6
برنانی (0ظ088). ایرلندی کهن (8]7ل#ا صا0): ۸
۸ ۲880 ولزی (۳215[7): 2۸
لانین (1477۸): ۳08710 ,۳۸/۲718 ,8۸385 برتونی (875701): 0
فرانسه (۳2/)[7): هتبت (07177178: ۳۸81۸ ۳۸۹817
8 ,۳۸۹318 ,8۸3
```


## [2026-09-14T00:58:14.142Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[435][:1800])\nEOF"
}
```


### [2026-09-14T00:58:15.261Z] TOOL RESULT

```
[pdf page 436]
1 ٍ
سوئدی (9[752[/57). 87106۸ پسگشت‌ها رد تا رد۲
هلندی (17ع007: لد ۳
لیعوانی (/4271۸0لاب0./72: اند نی 609 (57106) 8
1024 ۸
رون
4 (5713) ,60 (878077) ۱
برهان قاطع + 1۸۴
بادداشت:
۱ 8۸۹۸۷۲1۸7 معتقد است که ریشه‌ی اصلی واژه‌های ژُرمنی این فهرست ناشناخته است.
۲ بازگشت به: گند.
۱
او ستایی (7 0۲۹ 85۸30 ,5۸05۸ پر تغالی (۳۵0۸70535)+ نید 0۱۰۱۱
پارسی باستان (28781۸42 00): انگلیسی (۳)60/0/37از فرانسه) ۲۳۸۵8
دا زاس رها ایرلندی کهن (374لقا 2ل0):
پهلوی (۸۶۲7 ۰:۳ ۷۷181۴ ,۷۷18157۸۷ ,۸۸۲73870
تخاری 4 (۸ [/۸ل7047): ۰ ۵8۷۸۳ آلبانی (غم/۸8۸). 7
نخاری 8 (8 ۸۷ 70527۸7): زا ۱۲
سانسکریت (5۸/877): پسگشت‌ها ی اد دیدن :
507۸ ,85183۸75 ,5۸01۸71 را
تم برنانی 08280): ۰ ۲1123۸120 ,ق0399 5 (759همی) ی
لاتین (/710ل): 38 ,5 1
فرانسه (لع/(۳8۵): 8 م۲ 4 (581) ,105 5۸0 6)
اسپانیایی ((8۳۸(//3): 5 برهان قاطع : ۸۶
ایتالیایی (/477۸۸): ی
یادداشت: ۱ [
چم این واژه در زبان‌های کهن این فهرست: فررپاشیدن؛ صدمه‌ی شدید دیدن,
چم این واژه در زیان‌های رومانس نرین؛ فساد دندان, ا
:
```


## [2026-09-14T00:58:24.476Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== CHEUNG\"; grep -n \"pāšīdan\\|pasidan\\|pāš-\\|\\*paš\\|pāxš\" CHEUNG.txt | head -20; echo \"== HRN pas\"; grep -n \"pasiden\\|päsiden\\|pasiden\\|pä^siden\" HRN.txt | head"
}
```


### [2026-09-14T00:58:24.549Z] TOOL RESULT

```
== CHEUNG
19630:*NWIR: NP pasidan/pas-, (LW) Bal. pasit/pas-, Gz. pas-/pasa, Siv. pas- ‘to sprinkle, 
19716:*paš ‘to shave, shear’ 
23154:*NWIR: NP sipas ‘kindness, favour, thanksgiving’, NP sipasidan/sipas- (denomin.) 
41317:pasidan/pas-, 298 
41480:sipasidan/sipas-, 354 
57808:*braiH, *paš, *xšau 
== HRN pas
3167:334. püde *faul, verfault', päsiden (Inchoat.) *faulen .
```


## [2026-09-14T00:58:26.460Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '19600,19660p' CHEUNG.txt"
}
```


### [2026-09-14T00:58:26.561Z] TOOL RESULT

```
jump; to flee’, Bal. pan(n) ‘leaf? 

*NEIR: Pash. pana (Ё), Sh. pun, Bart. pont, Yi. pünä, M. pungy ‘feather’, Yi. pónék 
‘leaf’ 

*SANSKRIT: parnä- (n.) ‘wing’ = EWAia П: 97 

9 The denominatives above derive from the noun *parna-, which has impeccable IE 
credentials. 

«PIE *por-no- ‘wing, feather’ => LIV: – | Pok.: 850 (Nachtrag) 

*IE COGNATES: OCS pero, Lith. spafnas, Latv. spārns (m.) ‘wing’ (with sec. s-), 


OHG farn, OE fearn (m.), Engl. fern, etc. 
*REFERENCES: Horn 1893: 65 f.; IIFL II: 238a; DKS: 231a f.; EVS: 56b; Benzing 1983: 521; Lecoq 2002: 
122, 125, 127 (passim); NEVP: 63; Korn 2005: 133, 361 


298 *pars 


*parš ‘to sprinkle, strew’ 

*AVESTAN: Y Av. parsat.gauu- PN ‘having a speckled cow’ (Yt 13.96, Yt 13.127) 
*KHOTANESE: ? OKh. pruha-, prraha, praha- ‘hoar-frost, dew’. © The connection of 
these Khot. forms to this root, as made in DKS: 1.с., is both semantically and 
formally difficult. It may rather have a different (substrate ?) origin. 

*NWIR: NP pasidan/pas-, (LW) Bal. pasit/pas-, Gz. pas-/pasa, Siv. pas- ‘to sprinkle, 
strew’, Gz. раёп-/раёпа (caus.) ‘to scatter, spread’, ? Гог. perxa ‘sprinkling’ 

*NEIR: ? Sh. purx-/purxt, Rosh. parx- ‘to sprinkle, splash water’, Sariq. pirx-/pirxt ‘to 
vomit’ (why -x- ?), Pash. pana ‘sprinkling water, irrigating’, ри? ‘sprinkling’, M. 
porx (Ё) ‘hoarfrost, hail’ (Zarubin), ? Oss. I. pyrx, D. purx(&), purf ‘sprinkled, 
scattered’ (LW ?, with dissimilation f... x> р... х?) 

*MISC: Par. phis- ‘to strew, scatter, sow’, (?) Orm. prusnaw- ‘to sprinkle’ 

*SANSKRIT: pfsant- “dappled, with white spots’ (RV, AV+) = EWAia П: 164 

«PIE *pers- ‘to spray, sprinkle’ = LIV: 788 f. | Pok.: 823 

*IE COGNATES: Hitt. /pappars-/ ‘to spray’, Toch. pärs- ‘to sprinkle’, OCS ras-praso 
(ras-prasiti) ‘I scatter’, Lith. purskiu (purksti) ‘I spray, (be)sprinkle’ 

*REFERENCES: IIFL I: 279a, 404b, 375, 240a f.; EVP: 63; Morgenstierne 1942: 264; Abaev, Slovar’ II: 
245 f.; EVS: 60b; WIM II/1: 81; DKS: 256a; WIM III: 114; Werba 1997: 357; NEVP: 63; Shahbakhsh: 


s.v. pas- 


*part ‘to fight, struggle’ 

*AVESTAN: YAv. porat- ‘to fight, struggle’ = Liste: 34 

MED.; Pres. them.: IND. 3pl. YAv. paratonte (Yt 13.27, Yt 13.45), INJ. 3sg. YAv. paratata (Yt 5.50), 
SUBJ. 34и. YAv. 'porotaiüe (Yt 19.46); Partic.: pres. YAv. porotomna- (Yt 17.13), perf. Y Av. 
рарәгәіапа- (Yt 10.8)
```


## [2026-09-14T00:58:38.499Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in range(512,522):\n    p=pages[i]\n    print('---leaf',i, re.findall(r'\\b(?:99\\d|10[01]\\d)\\b',p)[:6])\n    print(' '.join(p.split())[:300])\nEOF"
}
```


### [2026-09-14T00:58:39.657Z] TOOL RESULT

```
858
---leaf 512 []
, ripen’; Lat. coquo, ére, v. as Skt.; Osc. Umb. *pop- (in the Lat. LW popina, f. ‘cook- shop’: Lat. coquina); Br. pibi, pp: pobet, v. 921 as Skt.; W pobi, id.; Cor. pobas, inf., 3s. fut. pep, v. id.; OCS peko, pesti (and com. SL), id.; Li. (metath.) kepü, képti, id.; Latv. cepu, cept, v. id. pequos
---leaf 513 []
éran, id.; Tokh. A pärne, B parna, adv. “outside; cf. OHG férrana ‘far perənt- (pernt-) ‘birdlife, bird(s) Per. parandah ‘bird’; Cz. peruť, f. ‘wing’; cf. Srb. perad, f. “fowl peri (per, per-) «through, over, round; very-'. WP II, 30 Skt. pári; Av. pairi; Ober pariy; Per. pār; Oss. fäl- ‘through-’; 
---leaf 514 []
wflake’; Li. peršùs ‘tingling’. Z-gde in Cz. pršet, inf. ‘rain’; prchnout (Cevaporate', intr.) perK- (1) “split, breach’. Skt. cf. pár$anah, m. ‘chasm’; OCz. prés, prp. through, over’; Li. cf. pra-persa, f. ‘chasm, gap, breach' perk- (2) “hurt, harm, punish, castigate’ Ober. parsamiy, v. ‘punish’; O
---leaf 515 []
ti, v. “flog” (pf: periau); Latv. peru, pert, id. (Z-gde in OCS prja, f. ‘quarrel’. Of indeterminate grade in Hitt. parh- mi, v. "drive pero, io (3) breed (Variant: por-) Lat. cf. puer-pera, adj. f. ‘in childbirth’; -pe- rium, n. ‘parturition’; cf. also jüni-perus, gs: 1, f. Cjuniper,, if fr. *jeuni
---leaf 516 []
erthu, inf. ‘strive’ perun-, peroun- (?). Cf. perquón- Hitt. perunas "rock mountain’; OCS cf. peru- nú, m. ‘thunderbolt’ perut, peruti (z-gde of per- and uet-, q.v.) “last year’. WP II, 31 Skt. parut, id.; Arm. heru, id.; Myc. & Gk. pérusi, id.; Alb. cf. par-vjét, adv. (“the year before last', fr. *
---leaf 517 []
Lat. pesna, f. ‘feather, wing’; Ir. (?) eathar, m. ('ship'. Cf. ‘pinnace’ for sense); (oblique form in) MIr. én, m. ‘bird’; OBr. cf. hataned, pl. (feathers', w. “false? h-) beside atan-oc, adj. ‘winged’; eterin, pl: atar, m. ‘bird’; Br. (oblique form) adan, pl. -éd, m. “a bird, owl or nightingale'?;
---leaf 518 []
: pari, prp. (at, over, toward’. (Variant of type *prei in OCS and com. Sl. pri-, Li. prie-). Cf. also Alb. pari, f. ‘nobility’: MIr. aire, s. ‘prow, temple of head, chief, noble’. Comp. in Lat. praeter ‘beside’; Olr. airther *eastern'; E farther & further. WP II, 33-4 poró “forth, before; therefore
---leaf 519 []
pouont- Cypr. cf. pai “altogether, -ever; kasa-pai (queried: *also'); Cz. pevný, adj. ‘firm’; Pol. pewny, pewien, id.; Latv. cf. pa-puve, f. ‘fallow land" (Arm. havat, o-st. “faith” appears to be an Iranian LW) pi ‘on, upon’. Aphetic form of epi, q. v. Skt. pi, pi- (in pi-drbh, -dhà, -nah, etc.); Os
---leaf 520 []
nger’; pykstü, pýkti, v. ‘be angry; LW in Ir. pioc, pioch, m. ‘droplet; jot; pore & in Alb. pikë ‘point, dot, source of Fr. pique, fr. a Lat. type *picca. A type pīkāið arises in Alb. pikoj, v. ‘drip’; OCz. pikati, inf. ‘urinate’ and in OCS pikanina, pikotyna, f. “urine? pikolos, à, is (pikl-) ‘tip,
---leaf 521 []
fig" beside pippalih, f. ‘capsicum, chilli’; pippalah ‘sacred figtree; nipple; pippalam, n. ‘berry, (The variants occur in the river-name Pimpala & Pippalàa); Sp. cf. pimpóllo ‘shoot; beau’; Port. pimpáo, id. beside pimpolho ‘bud’ (LW in E pimple); G Fimmel, Femmel, m. “male hop, male hemp’; Li. cf.
```


## [2026-09-14T00:58:48.349Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (513,514):\n    print('=== leaf',i,'(pp ~',2*(i-15),2*(i-15)+1,')')\n    print(pages[i][:4000])\nEOF"
}
```


### [2026-09-14T00:58:49.508Z] TOOL RESULT

```
=== leaf 513 (pp ~ 996 997 )
éran, id.; Tokh. A pärne, B parna, adv. “outside; cf. OHG férrana ‘far
perənt- (pernt-) ‘birdlife, bird(s) Per. parandah ‘bird’; Cz. peruť, f. ‘wing’; cf. Srb. perad, f. “fowl
peri (per, per-) «through, over, round; very-'. WP II, 30 Skt. pári; Av. pairi; Ober pariy; Per. pār; Oss. fäl- ‘through-’; Gk. peri, per; (Alb. ambig. për ‘for’, see pro, pro); Lat. per; Umb. -per, post-
923
pos. ‘for’; Venetic per ‘through’; Olr. cf. ire, adj. ‘ulterior; OW eir, cj. ‘since’; W. Cor. OBrit. er, prp. ‘for, because of; OCS prě-, px. Cover, and com. Sl); Li. per, prp. ‘through’. As an intensive px: cf. Skt. pári *very'; Oss. fír, id.; Arm. cf. ar- in ar-amur ‘very strong’; Gk. péri (enclitic), per, peri- ‘very’; Alb. (ambig.) për-, id.; Lat. per-, id.; MIr. er OBr. er, Wer, id. cf. Br. er-vad (“indeed, very well, properly’, fr. mad *good^); Go. faír- *very-; OS.OHG firi- in -wit, -wi3, s. *portent, wonder; OCS, Srb. pré-, pre- *very'; Li. per-, id.
peri-bhán-, cf. bha-mi, (bho-) Skt. cf. bhànam, n. “appearance”; pari-bhàse, mp. ‘appear’; Arm. cf. h-erevan acem, v. ‘show’; h-erevan gam, v. (appear, fr. *en- peri- or *pi-) Gk. peri-pháneia, f. *conspi- cuousness'
peri-do-(-dídó-), cf. do-mi, dídó- Skt. pari-dMádami; Gk. peri-dídomai; Lat. perdo, -dére; W (?) rhyddau, inf. v. (free, cf. rhydd, adj. 'free); OCS pré-dami, datt: OLi. per-duomi, mod. -duodu, inf: -duoti
perin- (peri-, pern-) Tokh. A pare, B peri ‘fault; Arm. her, i-st. “hate, envy; OS. OHG firina, Go. faírina ‘crime; blame’; OE firen, f. ‘crime; violence; suffering’; OFris. firne, f. ‘crime’; ON firn, npl. ‘outrage’; cf. mod. Icel. firnindi, npl. ‘the wilds; MHG virne, sf. *misdeed' (but virne, adj. “old, wise’ unrelated)
perinēmi ‘transact’ Gk. pérnēmi, id.; Olr. renaim, renim, v. id.; Skt. cf. páne, mp. “buy, bargain'
peri-sthà- Skt. pari-stha-, v. encompass; obstruct; Per. firistam, v. "send: Arm. (ambig.) ertam, v. (*go', but cf. strm-); Gk. periístémi ‘go round, surround'; Lat. cf. persto, -stare (continue, persist; OHG firstan, inf. ‘perceive, under- stand": OCS pré-stajgo, -stati, v. and -stajati (*cease', cf. Av. pairista, pp. ‘tried; powerless’); Li. per-stoju, -stoti, v. ‘cease’. Cf. variants of type *-sthon- in Arm. erit'anam, v. ‘sink, waste away” and Lat. prae-stino, åre, v. *pre-empt,, and type *-stos, -sthios, -sthis in Skt. paristih, f. ‘reverse, distress; Gk. perissós ‘huge’;
peri-bhán- — perkt-, prKt-, prokt-
15
20
25
30
35
40
45
924
OHG, OE first 'roof-ridge', etc.
per-itos, à, is, us “passed; passage”. Cf. per-, ei-mi Skt. paritas, adv. “round, about’; paritah, pp. ‘surrounded, clasped? beside páretab, adj. (deceased', fr. *per-eit-); Gk. cf. peritios “Macedonian month’; peritia ‘a feast’; Lat. cf. perítia, f. ‘expertise’ beside peritus, adj. ‘expert’; ON ferð, f. journey, conduct’; Swed. cf. fárde, adv. “in progress, under way”
perior- (?) Per. parre ‘side, border: Gk. peirar, gs. pef- ratos, n. end. limit?
perio, cf. peri-ei-, itos. Hitt. cf. pariya(mi), v. ‘send forth’; pariya(n), adv. “forth, ahead"; Gk. peíro; Lat. perio, ire; MHG cf. verje, verige, wm. (*ferryman': G Ferge, f. 'ferry); E also to ferry, v.; G also Fåhre, f. id.; Sw. fárja, f. id.
(perion-, peron- ‘pin, awl, bodkin’. See Supt: P)
perkos, å (perk-?) “spot, dot; mottled, spot- ted; mottled fish’, etc. Cf. perks-, prks- and prs- Gk. pérke, f. ‘perch — fish’; MIr. erc, Ir. earc, adj. 'speckled"; Ir. earc, f. ‘trout’; cf. also MIr. ercaim, Ir. earcaim, v. ‘decorate’; Sw. cf. fárna, f. ‘chub’ and OHG (z-gde) forhana, OS forna, f. ‘trout
perks- “scatter, sprinkle'. Cf. prks-, perkos Br. erch, m. ‘snow’; ercha, erchi, v. id.; Li. per- šiù, éti, v. ‘itch, tingle; Latv. cf. pérsla, f. ‘sno
=== leaf 514 (pp ~ 998 999 )
wflake’; Li. peršùs ‘tingling’. Z-gde in Cz. pršet, inf. ‘rain’; prchnout (Cevaporate', intr.)
perK- (1) “split, breach’. Skt. cf. pár$anah, m. ‘chasm’; OCz. prés, prp. through, over’; Li. cf. pra-persa, f. ‘chasm, gap, breach'
perk- (2) “hurt, harm, punish, castigate’ Ober. parsamiy, v. ‘punish’; OCz. cf. pfésny ‘exact’; R presnyj ‘unleavened’; Pol. przasny, id. (lit. ‘sour, harsh")
perksKo, see prÉs-, preK-, prok- Umb. cf. persklum, n. ‘prayer’; Li. persu, piřšti, v. (“mediate between a prospective bride and groom’; refl. ‘woo, pester’)
perkt-, prkt-, prokt- OCS présto, prétiti, v. ‘threaten’; OCz. prétiti,
925
inf. id.; (z-gde in) Go. faürhts, adj. "fearful; OE forht, adj. “afraid, terrible’; OHG forhta, f. “fear; Slovene cf. (variant) protiti, inf. (threaten, fr. *proKt-); OCz. also pféta, f. ‘threat’; při-přčta, f. ‘reverence, awe’; (metath. in Du. gods-vrucht, f. ‘reverence’)
perKus, uos (prku-) ‘side, bosom, soul, heart, life’. (Semantics obscure). WP II, 44. Skt. cf. par$vya, dual n. “heaven & earth’; pārśvam, n. “side? and pársuh, f. ‘rib’; Av. (z- gde) porosus, m. ‘rib, side’; Oss. fars, s. ‘side, rib, wall: cf. also fársmá' ‘sideways’; färsäi “on one side”, färsón, s. ‘side, flank, bosom’; Go. fairhwus, m. ‘world’; Crim. Gothic fers, m. (mar, lit. sou); OS firihos, mpl. ‘men’; OHG firah-, id.; OE feorh, m. “life, soul; MHG vërch, gs: vérhes, sn. id.; adj. ‘vital; cf. also OE feorm, f. (“food', if for *perKm-). Z-gde in Alb. preh, usu. prehén, T prehër, m. (bosom, fr. *prKu-); OCS prüsi, fpl. ‘breasts’; Cz. prsa, n. dual ‘chest, breast’; Li. pirSys, gpl: -iu, f. “breast of horse’. Cf. ON fjor, ds: fjorvi ‘life’ beside firar, pl. “people?
per-m-, cf. per-, emó Lat. per-imo, -imére, v. (remove, liquidate'; OCS préimo, pré-eti (take, grasp, under- stand'; Li. pér-imu, -imti, v. 'take over; pull through, stab, grab'
pernoi (pern-) “last year, of yore’; pernos “last year's, ancient'. WP IT, 31 Per. pàr, adv. “last year’; cf. pàrine, adj. "old: Oss. farà, fáron, adv. “last year’; Arm. cf. (dial.) herun, id. Contaminated w. type perut, q. v.); Umb. perne, adv. ‘before’; pernaiaf, acc. pl. f. ‘ancient’; Go. fairns, adj. “last year’s’; faírneis, adj. íancient; MHG vérn, vérne “last year’; OHG firni, adj. ancient? beside férn-erig “last years’; (contaminated w. type *perut- in) MHG vérnet, vérnt, vérnent, adv; ‘last year’; G cf. firn, adj. ‘long-standing’; Firn, m. "per, petual snow’; Swiss cf. vor-fern, adv. “the year before last; Li. pérnai “last year’; Latv. pērn, id. beside perns, adj. “last year’s’; pērnais, adj. id.
per-nokt- ‘overnight. Cf. per-, nokts (noktis) Alb. cf. (archaic) pér-nátet, v. 3s. ‘grows dark’; pér-nata, -naté, adv. (ambig. *per- or *pro-: “by night); Lat. cf. per-nocto, äre, f. spend
perkus, uos (prKu-) — péros, à, om (peior-?)
10
20
25
30
35
40
45
926
the night; MHG ver-nahten, v. id.; OCS pré- noStujo, -evati, v. id.; Li. per-nàkt, adv. “through the night’; cf. per-nakvoti, inf. ‘spend the night; Latv. cf. par-naktim, parnaktis ‘night after night’; pàrnakSot, inf. ‘spend the night
pern- (pernt-) ‘beyond, away, far’. Cf. pe- rəm-. (Some forms ambig.) OPer. cf. parana-, adj. ‘former’; Tokh. A pärne, B parna, prp. ‘outside’; Arm. cf. heri, adj. ‘distant’; heru, adv. ‘far’; Hitt. peran, parranta, adv. ‘forth, away’; Gk. pérà, péran, prp. “be- yond’; péras, gs: pératos, s.n. ‘limit; Lat. cf. peren-die ‘the day after tomorrow’; OHG fër- rana, MHG vërren “far”; OE feorr, adj. & adv. id.; ON fjarri, adv. “far”
perð (1), see perið “pass through”, etc.
peró, io (2) ‘beat, flog? OCS pero, inf: prati, v. id. (and ‘wash - clothes"); Li. periü, per
```


## [2026-09-14T00:58:57.701Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(548,560):\n    p=pages[i]\n    m=re.findall(r'\\n\\s*(9\\d\\d|10\\d\\d)\\s*\\n',p)\n    print('leaf',i,m[:4],'|', ' '.join(p.split())[:150])\nEOF"
}
```


### [2026-09-14T00:58:58.863Z] TOOL RESULT

```
leaf 548 ['987', '988'] | losami, v. (2) ‘sprinkle, anoint; (z-gde in) prusnómi, id.; (long z-gde in) Cz. prys- kati, inf. ‘spray, squirt’; (o-gde in) Li. prausiü, ti, v. ‘wash
leaf 549 ['989', '990'] | prí-, q.v.) Lat. cf. pri-die ‘the day before’; pri-dem *re- cently' beside OLat. pri (Lat. prae); Li. pri- (verbal prefix) beside OCS (and com. S1.) p
leaf 550 ['991', '992'] | , cf. pro-, ago Per. far-àz, adj. *exalted"; far-azam, v. ‘erect’; Oss. (Graz, s. ‘means, facility’; fárazun, inf. ‘be able’; Arm. ar-ac, i-st. s. “pr
leaf 551 ['993'] | í, proj, adv. “early'; próios, adj. id.; EMAIb. prej, prp. ‘towards’; MIr. ré, prp. id.; MHG vrüe, vruo, vrüeje, adv. *early'. Variant in Greek próén,
leaf 552 ['994', '995'] | v. "order": Gk. prómantis ‘prophetic; prom-, prom-, próm- (promi-) — pro-pet- (pro-pət-) 10 20 25 30 -H 994 propheť (cf. the vocalism of Skt. pramātr,
leaf 553 ['996', '997'] | m. and -am, n. ‘plain, plateau’; cf. (variant) prasthah (lying ahead; chief”, fr. *prosthios); Per. fere- propor- — proti (proti, protio) 10 15 20 25 
leaf 554 ['998', '999'] | d: OCz. prsk, m. “spray, spurt’; (prS&ti, inf. “rain? < *prusk-: *prks-, q. v.); Slo- vene pfsk, m. ‘rut, heat in animals; prskati, inf. ‘rustle; spur
leaf 555 ['1000', '1001'] | m of prqu-, q.v. and cf. perquó) prk- “board, beam, barrier, thwart'. (Oss. & Balto-Slav forms ambig.) Oss. fark (&board, slat, paddle, oar’, fr. *per
leaf 556 ['1002', '1003'] | on, f. (*question', fr. *porKs-); MHG vorsch, e sf. ‘enquiry’; OCS prici, m. ‘advocate’; Li. cf. pirslýs, m. ‘matchmaker’ prks- (2), see prks- and var
leaf 557 ['1004', '1005'] | see prks- and variants (prsom, iom ‘leck’. See Supt: P. WP II, 84) prsthis, ios, os (pristh-, prkst-) 'spike, peak, eminence, top, ridge’. Cf. pr-, -s
leaf 558 ['1006', '1007'] | ére, id. is obscure pstuio (pstiuio, psth-) ‘spit’. Cf. spuuo, ið. Onomat. WP II, 683 Skt. sthivami, pp: sthyütah, id.; Hind. cf. thuk, s. id.; Per. t
leaf 559 ['1008'] | - and sd-, sed-); Lat. cf. sal-püga beside sol" soli (5jump-tail' hence ‘poison ant); Big. pia, (^wench', fr. *pugio). (Isophone: Skt. puja, f. honour
```


## [2026-09-14T00:59:02.359Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[556][:4500])\nEOF"
}
```


### [2026-09-14T00:59:03.745Z] TOOL RESULT

```
on, f. (*question', fr. *porKs-); MHG vorsch, e sf. ‘enquiry’; OCS prici, m. ‘advocate’; Li. cf. pirslýs, m. ‘matchmaker’
prks- (2), see prks- and variants
prKsKo “ask, beg, beseech’. Cf. prKs- (1) and preK-, perK-. Variant prKsn- Skt. préchámi, v. id.; Av. porosa, lsg. id.; Per. pursam, -idan, id.; Oss. fársin, inf. id.; Tokh. B. park-, v. id.; Arm. cf. harcnem, harcanem, id.; Lat. posco, ére, pf: poposci, id.; Umb. cf. pe-purkurent (‘they shall ask’. Umb. pers- nimu, depon. imperative is prob. ‘put, not ‘pray!’); W erchi, inf. (“ask”, fr. *porKsK-); Cor. erghy, yrghy, v. ‘command’; MHG vorschen, v. “ask, seek’; Li. cf. pirsti, inf. of persü, v. ‘mediate; woo’
(prKst-, Slav. variant of type prkst-, q.v.)
(prKt-, see prks- and variants)
prÉ- — prqutos, à
20
25
30
35
40
45
1002
prm- (contracted formula of type promo-, cf. pr-, etc.). See next Doric prán, cj. & adv. (&before' of time) beside Hom. prin, id.; Alb. cf. pér-parém, adj. Cfront-, fr. *pro-prom-); OS formon, v. ‘further’; MHG vorn, vorne, voren, adv. "be- fore’; Icel. forn, adj. “ancient? beside frum-, in cpds. id.; Go. fruma, adj. ‘first’; Sw. forn-, px. fearly-; fören, m. ‘bows of a ship’; Li. pirm, pirmà, adv. & prp. “before; ago'; Latv. cf. pirms, adv. (sic) “before?
prmos "first. Cf. prm- above, and proiom-, priiom-, proim-. WP II, 37 Gk. prámos, m. "leader, first-ranker'; Lat. cf. pràn- in pran-dium, n. ((midday-meal, fr. *pram-ediom — Vetter); Go. fruma, OE forma, adj. beside OE frum, adj. “earliest, primal; Li. pirmas, adj. ‘first’; Latv. cf. pirmais, adj. first’; pirms, adv. cj. “before?
(prn- ‘transact’, see perinemi)
(pro, pro-, proti, see pro- and extns., proti, etc.)
prquð (1) “touch, hit, meet, join’. Cf. perquo & prequo Skt. cf. pricami, pi-prCami E prnákmi, pp: prktáb “make touch; join, mix’ cf. also prktih, f. ‘contact’; Alb. cf. prek, v. id. (fr. *prequo or *prqu-. See Mann: Alb. Hist. Gr. pp. 159 & 167) beside pérkás, id. (Mann: p. 181); Gk. cf. (e-gde) prépo, v. ‘resemble; beseem, suit, fit; Cor. cf. ryp, prep. «touching, alongside’; Srb. cf. prk, m. ‘obstinacy’; u-prk, prp. 'de- spite’; Li. perku, inf. pifkti, v. ‘buy’; pilkis, gs. io, m. “purchase; Latv. pérku, pirkt, v. as Li.
prquó (2) (prequ-) “force” W rhabu, inf. ‘check’; rhab, m. ‘force, con- straint’; Cz. cf. à-prk, m. (dash, rush". Other Slav. forms ambig. Cf. prk- and perquo)
prquo- (prquà, prquno-), cf. perquos and prk- (2). (Slav. ambig.). WP IL, 47 OHG cf. foraha, f. (*fir-tree and com. Gmc.); Norw. furu, id.; OCS *prükno, n. ((board', ambig. cf. prk- Ou: Li. cf. pirkià, f. "log-cabin'
prqutos, à ‘athwart, crosswise; thwart, bar- rier’. Cf. prquo (1) & (2) Alb. pritë, usu. pl. prita, fpl. ‘railing’; Blg. părt, m. ‘bar’. Isophonic w. Skt. prktáh, pp.
1003
“mixed, joined”. Cf. prquð (1) and (2)
prs- ‘speck, spot, mark, dapple, sprinkle, spray, dot, rash’. Cf. prsk-, (prks), prK-, prKs- Skt. cf. prsat, s. ‘droplet’; prsatah, adj. ‘motley, dappled’; prsvah, adj. *frosted'; Av. cf. paro&-, v. (e- or o-gde) ‘drip’; Per. cf. paSam, inf. pasi- dan, v. (e- or o-gde: Skt. parsami, v. 'sprinkle"); Tokh. A & B párs-, pras-, v. as Skt.; pársant, adj. ‘scintillating, brilliant; Hitt. parsa(mi), v. “flee? beside pap-pars(mi), v. 'sprinkle'; par- sanas, s. (-leopard', lit. *dappled"); Gk. cf. par- dakós, adj. (wet, if for *prs- + *-dnk-); Lat. cf. porr-1igo ('dandruff,, fr. *prs-); ON fors, m. ‘waterfall’; Sw. forsa, v. ‘gush’. Extns. in Skt. prdakuh, ‘panther; snake’; cf. Per. palang ‘leopard; tiger’; Oss. (queried) fálang, fárang ‘tiger’; Gk. párdos, m. ‘leopard, panther’; pár- dion, n. ‘giraffe’; párdalos, m. (‘plover or 'star- ling’); párdalis (an unnamed fish); cf. also Alb. pérpurth, v. (‘defile w. excrement’, fr. *-prsd- or fr. *-prKst-); Cz. cf. prznit, inf. (defile, fr. *prsd-)
prsk-,
```


## [2026-09-14T00:59:24.390Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[554]\ni=p.find('998')\nprint(p[:3000])\nEOF"
}
```


### [2026-09-14T00:59:25.486Z] TOOL RESULT

```
d: OCz. prsk, m. “spray, spurt’; (prS&ti, inf. “rain? < *prusk-: *prks-, q. v.); Slo- vene pfsk, m. ‘rut, heat in animals; prskati, inf. ‘rustle; spurt’; (long vowel in) Lat. prūs- cum (an unidentified shrub); Ir. rüisc, s. ‘lash, volley, hail of bullets; OCz. prýščiti, inf. ‘spurt, spray’; cf. Cz. o-prysk-aly, adj. “peeling, blistering’; R pryskat, v. ‘spurt, squirt’; cf. Slovene, Big. prist, m. “swelling, tumour, blister. Variant in OCS prysti, m. ‘sprout; swelling’; prystati se ‘swell, sprout'. (Iso-
prous- — pri (pori, proi, pri)
5
10
20
25
30
23
40
45
998
phone: OE frysca, wm. “kite? or *bittern")
prüst- (phrüst-) ‘snort’. Cf. prüs- (1) Sw. frusta, v. id.; Blg. práxtja, id.; Li. cf. prunks&Ciu, prunksti, id.
prüt- Gk. cf. dia-prüsios, adj. ‘penetrating’; R (*-ü-) pryt, f. ‘speed’; prytkij, adj. ‘nimble’; Cz. pryt, m. ‘bud; filling, stuffing’; prytiti, inf. “bud, sprout'. See next
(prut-, pruth-, see preut- (preuth-). Z-gde in ON froða, f. ‘froth’ and in Srb. prtljam, Datt, v. *twaddle")
pF, př- (por-), Zero-gde and r-gde of types peri, pro, pri, etc. The vocalism echoes that of type tr- (tor-, tro-), q. v. Arm. cf. (?) ar in ar eri ‘near’; Gk. pár, pará (Cat, etc.); Alb. (ambig.) për, w. loc. "at by’; Lat. por-, (assimilated: pol-) in some cpds.; Umb. pur-, Fal. por-; Venetic cf. porah (for pora 'for); Go. (and com. Gmc.) faür, prp. “for”; cpds. faür-; Ir. W. ar on upon’; Slovak pre, prp. ‘for’; Lith. cf. par-, verbal px.; Latv. par ‘over’; par-, px.
prd- (1), Indo-Iran. variant of type prs-, q. v. in Skt. pídakuh, m. (fviper; tiger or panther’, lit. spotted"); Per. palang, s. ‘tiger or leopard"; Oss. fálank, fárank (queried: ‘tiger or lion"); Gk. (fr. Iran.) párdos, m. ‘panther, leopard’
prd- (2) (prdilos, à; prdos, ios, a) ‘fart’. Cf. perd-, pord-. WP IT, 49 Gk. cf. pradíle, f. id.; Cz. prdel, m. ‘arse’; OHG furz, MHG vurz, vorz, sm. id.; Icel. furtur, m. (Tout, fig.); Cz. prd, m. ‘fart’; Slo- vene prda, f. ‘arse’; Li. pirdà, f. & pifdis, gs: pirdZio, m. “fart?
(pro, see pr- above)
(prg- ‘dry, roast, fry, wither’ (?) Per. cf. pažmān, adj. ^withered" (?); See Supt: P)
(pr&- (per&- or porg-) in Skt. parjanyah, m. ‘rain’; Cz. prznit, inf. *de- file’. Cf. prk- (prKnios, prksios))
pri (pori, proi, pri) “before, at, to’. Cf. peri, pr-. WP II, 33 (Arm. eri- in cpds. ‘young, early’, cf. af eri “near”, an e-gde form w. links only in r- or z-gde); Lyc. (?) ürpi, prp. ‘for’; Gk. paraí, adv.
999
“by, alongside’; Alb. pari, postp. (near, in phr. aty — ‘yonder’); OLat. pri, Lat. prae ‘before’; Mir ré, id. beside ri ‘towards’; Ir. ré; ria, ri- ‘before; towards’; Gaul. are, ari “on, upon’; W. Cor. ar, id. beside OW & W rhy, adv. ‘very, too much' and W rhwy, id. (fr. *prei); Br. ré, adv. as W rhy; OHG, OS furi, prp. “in front of; for’; as px. *past-; ON fyrr and fyrri, adv. “before, sooner’; OCS (and com. S1.) pri, prp. ‘at’; cf. isprí, adv. ‘above’; Srb. pre, prp. (“be- fore”, fr. *proi); adv. ‘too much’; Cz. pře- *over-, too much’; Li. prie, prp. Cat, fr
```


## [2026-09-14T00:59:42.605Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 407 -l 407 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg407 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg407.png"
}
```


### [2026-09-14T00:59:44.532Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79866 Sep 13 20:59 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg407.png
```


## [2026-09-14T00:59:44.668Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== MON pashidan\"; grep -o \"پاشیدن[^.]\\{0,120\\}\" MON_part1.txt | head -5; echo \"== MON efrit\"; grep -o \"عفریت[^.]\\{0,150\\}\" MON_part1.txt | head -5; echo \"== MON palang\"; grep -o \"پلنگ [^.]\\{0,120\\}\" MON_part1.txt | head -3"
}
```


### [2026-09-14T00:59:45.839Z] TOOL RESULT

```
== MON pashidan
پاشیدن» متلاشی شدن 
پاشیدن: 22-12۳01027 ( مص‌ل
پاشیدن» 
پاشیدن (اب یا 
پاشیدن
== MON efrit
== MON palang
پلنگ به صید)
پلنگ دارد
پلنگ گوزن‌افنکن:
```


## [2026-09-14T00:59:49.115Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -o \".\\{80\\}پاشیدن: 22-12۳01027.\\{0,300\\}\" MON_part1.txt | head -2; echo \"=== palang entry\"; grep -o \".\\{60\\}پلنگ (.\\{0,300\\}\" MON_part1.txt | head -3; echo \"=== efrit in part2\"; grep -o \"عفریت.\\{0,200\\}\" MON_part2.txt | head -5"
}
```


### [2026-09-14T00:59:50.310Z] TOOL RESULT

```
=== palang entry
=== efrit in part2
```


## [2026-09-14T00:59:53.568Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ('پاشیدن','پلنگ','عفریت','آفرین','آفریدن'):\n        idxs=[m.start() for m in re.finditer(w,t)][:3]\n        for i in idxs:\n            print(f,w,'>>',' '.join(t[i-60:i+200].split()))\n        print()\nEOF"
}
```


### [2026-09-14T00:59:54.796Z] TOOL RESULT

```
MON_part1.txt پاشیدن >> و زیر کردن. اش و لاش ند لن: 0-135-50020 24 (مسصل.) از هم پاشیدن» متلاشی شدن چنانکه مرداری وجیفه‌ای. سخت چرکین شدن و منبسط گشتن زخم اشیان: 2827 (- آشیانه] (ا.) لانهٌ حبوانات از مرغ. سنگگ» موش زنبور» مار و غیره؛ آشیانه. خانهء مآوی» مسکن. طبقه» مر تبه»
MON_part1.txt پاشیدن >> (ص.) روشن» درخشان. سپید روشن» سپید رنگ» سپید روی. از هم پاشیدن: 22-12۳01027 ( مص‌ل.) پراکنده شدن» متفرق شدن. گسیخته شدن امرء تباه گردیدن کار. ازیرا: قع-2ه [- ازایرا - زیرا] (حر. رد. مر.) زیرا» برای اين» از برای آن» از آن جهت» بدین سبب» بدین علت» بناب
MON_part1.txt پاشیدن >> . اشس‌پوختن: 30 [- اشسپیختن < اشپوختن - اشبیختن] (مسصم.) پاشیدن» پرا کندن» پراکنده کردن» افشاندن. گل نم ردن. ترشح کردن. اشپون: اجه (.) (چاپ.) سرب باریکی که میان هر دو سطر نهند تا فاصلهً مطلوب پیدا شو د. (چاد.) و احد طول سطر. اشتاد: 024 (.) (اخ.) نام

MON_part1.txt پلنگ >> ان الارض آقوش: مر (د) (جان.) درندگان» سباع از شیر » سر 6 پلنگث» بوز و غیره. اک: : 28 [ند» شر بر) بدی] (.) آسب؛ آفت. آکادمی: ااس 7۱ (.) انجمنی نز کت از بزرگان علم و ادب و فن» فرهنگستان (فره.) اکپ: ۲ ([+- آکب] (.) گرداگرد درون دهان؛ لب لشو س. اکتور: ۲
MON_part1.txt پلنگ >> جون آب نماید» سرات. 1 قلة (- آل] (ص.) سرخ سرخ نیمرنگك. الاپلنگی: آ-212-221208 (امر .) اعم ۰ با گل‌ها و خال‌های بزرگ مانند بوست پلنگك» الات: :715 (ع.] (.) ج. آلت. انزارها اسزارها)ا؛ ادوات» اسیات. آلات تغد به: مجمو ع عضوهایی که در کار تغد به بکار است. الا
MON_part1.txt پلنگ >> 12-221208 (امر .) اعم ۰ با گل‌ها و خال‌های بزرگ مانند بوست پلنگك» الات: :715 (ع.] (.) ج. آلت. انزارها اسزارها)ا؛ ادوات» اسیات. آلات تغد به: مجمو ع عضوهایی که در کار تغد به بکار است. الات تناسل: عضوهایی در حبوان از نر و ماده که سب تولید مثل و نتاج است. ا


MON_part1.txt آفرین >> آبادی؛ معموره؛ مق ویرانه» خرابه. (صت. ادات تحسین و دعا)» آفرین! احسنت! مرحبا! زه! بصورت بسوند در آخر نام‌های مکان درآید به معنی بنا سل و ری معمو ر ... آباد نودن: معمور بودن» داير ودن» بربا بودن؛ مق. ویران نودن» خراتب بو دن. مرروع بودنء کاشته بودن. بر
MON_part1.txt آفرین >> دن: 212۲-127 (مسصم.) (آفربد» آفربند. خواهد آفرید» بیافرین» آفرینند» آفریده) خلق کردن, از یستی هست کردن» از عدم بوجود آوردن» ایجاد» هستی دادن. افریده: (6-)2]2-102 (امف. آفریدن) مخلوق» خلق شده» از تسش هت گر دنك فرهنکگ فارسی معین ۵۳ آفرین: 0 (افا.) در
MON_part1.txt آفرین >> مخلوق» خلق شده» از تسش هت گر دنك فرهنکگ فارسی معین ۵۳ آفرین: 0 (افا.) در کلمات مرکب بجای آف نننده نکسا رود جهان آفرین؛ افرین: 21۳ (۱.) تحسین» ستایش» مدح. شکرء سپاس. تهنیت» تبریکك. خوشی؛ خیر» سعادت. جوبی» نیح صلاح. آمرزش‌خواهی برای مر د8. نظطر سعد ‏

MON_part1.txt آفریدن >> 2,6د] 2 (ص فا .) خالق» آنکه خلق کند» آفر بننده. خدا الله. آفریدن: 212۲-127 (مسصم.) (آفربد» آفربند. خواهد آفرید» بیافرین» آفرینند» آفریده) خلق کردن, از یستی هست کردن» از عدم بوجود آوردن» ایجاد» هستی دادن. افریده: (6-)2]2-102 (امف. آفریدن) مخلوق» خلق شده»
MON_part1.txt آفریدن >> م بوجود آوردن» ایجاد» هستی دادن. افریده: (6-)2]2-102 (امف. آفریدن) مخلوق» خلق شده» از تسش هت گر دنك فرهنکگ فارسی معین ۵۳ آفرین: 0 (افا.) در کلمات مرکب بجای آف نننده نکسا رود جهان آفرین؛ افرین: 21۳ (۱.) تحسین» ستایش» مدح. شکرء سپاس. تهنیت» تبریکك. خو
MON_part1.txt آفریدن >> در 10 عبادت کنند» نمازخانه. افرینش: *510:10-0 (امص.) عمل آفریدن؛ کار خلقت. خلقت. خلق, انشاء ابداع. جمیع موجودات» همه آفر بدگان. افرینگان: 2]2717-0 (امر.) یک عده از نمازهای زردشتان که که در طی سال» در جشن‌ها و مواقع مختلف نحجای آورده می‌شود. چهار عدد

MON_part2.txt پاشیدن >> نند گل سرخ و زرد و غیره) کل برافشاندن. -۸۲-.: (مص‌ل.) گل پاشیدن؛ گلریزان کردن. گلبرگ: ۲۵۱-8 | برگگل | (امر یک از برگک‌های یکث گل؛ ۳ همجون برگک گل. (کن.) معشوقه‌ای که بدنش مانند برگک گل لطیف و نازک باشد. (کد.) چهره» رخساره. گلبن: 00و زگل سرخ | (امر) بی
MON_part2.txt پاشیدن >> تیجه: 20-) )22 [ع] (ق.) بالنتیجه» در نثار: هه« [ع.] (مصل.) پاشیدن چیزی را افشاندن. پاشیدن نقد و جنس بر فرق و در قدم کسی. (امص.) پراکندگی؛ افشان. (.) آنچه که بر سر يا در پای کسی (عروس و غیره) بپاشند (از نقد و جنس). هر چه که به روی کسی باشند. تک هد به. فدا
MON_part2.txt پاشیدن >> النتیجه» در نثار: هه« [ع.] (مصل.) پاشیدن چیزی را افشاندن. پاشیدن نقد و جنس بر فرق و در قدم کسی. (امص.) پراکندگی؛ افشان. (.) آنچه که بر سر يا در پای کسی (عروس و غیره) بپاشند (از نقد و جنس). هر چه که به روی کسی باشند. تک هد به. فدا» قربان» برخی. نثار؛ 5

MON_part2.txt پلنگ >> ه کرده در محل گسزیدگی می‌مالند» فر نجمسکك» از بان زرعلی) پلنگمشک. فلنگمشکا رام تلسی» حبق قرنفلی؛ ابرنجمشککه اقبلیس» حبق صعتری؛ است.. . در اد حبق الصعتری» حبق الکرمانی» حبق نبطی» بر نجمشکك. فرند: ۳:4] [- افرند» معر. پرند] جوهر نیغ و شمشیر. نرنگ:
MON_part2.txt پلنگ >> فهمیدن» درک کر دن. نهد.: 2۱0 [ع. ۰] (.) (جاد.) بوز» بوز پلنگ؛ . فهو د» افهد. فهر : ۳ (ع. (!.) سنگی که بدان چهار مغز بشکنند؛ سنکگک صلایه. فهرست: 16۳7 (۱.) جدولی شامل ابوات و فصول کتاب در انتدا با انتهای آن. صورت نهلر به: (۵0۱۵۷-۲-۵)۵] [معر. بهلوی]
MON_part2.txt پلنگ >> با مردهٌ حیوانات است. اين حیوان نسبه عظیم الجثه و به قدر پلنگی کوچک است. اندام‌های خلفیش از اندام‌های قدامی کوتاه‌ترند. رنگش خاکستری با خال‌های سیاه (شبیه پلنگ) است. هر یک از اندام‌های جلو و عقبش به چهار ناخن قوی ختم می‌شوند. اگر این جانور بقایای جسد ح


MON_part2.txt آفرین >> راد دیگر و یا ایمان به شرکت ایشان با خدا در معبودیت یا در آفرینش خلق و اعطای زندگی و غیره با در صفات ذاتی خدا مانند قدرت؛ علم؛ ور با اعتقاد به اینکه خداوند در آن اف اد حلول کرده با با آنان متحد شده است یا اینکه آنان بدون وحی و الهام ربانی به امور غیبی آ
MON_part2.txt آفرین >> دگان نیک ایزدی از آسمان فروفرستاده . نسیرویی است که سراسر آفرینش نیک از پرتو آن پایدار است. پیش از آنکه اهورمزدا جهان خاکی را بیافرند فروهر هر یک از آفریدگان نیک این گیتی را در جهان مینوی زبرین بیافرید و هر یکث را به نو خود برای نگهداری آن آفریدة جهان خ
MON_part2.txt آفرین >> ت. علم آموخته. عالم. فری: (-27])16] (صت. ادات تحسین) زه! آفرین! اختتتا: فر یاد: (:2۳۷30)16] [دوست» تکیه اتگاء؛ پاری] (!.) یاری خواستن با آواز بلند» فغان. شکایت با آوای رسا. بانگ رساء آواز بلند. به فریاد کسی رسیدن: استغائهٌ کسی را اجابت کردن» درمانده‌ای

MON_part2.txt آفریدن >> و چای دانةً برنج و غیره (فرعا.جما) نشاء: 1۵۹2 [ع. ۳ میم ۱ آفریدن. (مصل.) زیستن. نمو کردن بزرگ شدن. (امص.) آفرینش. زیست. نمو. نشاب: ۱۸۹820 |ع.] تسار 6 تن کر کر نده و پرتاب کننده یر . نشاب: ۰8680" ۱ع.) (.) تیرها. واحد آن و 3 ختن. ۵1-0 [- نش‌استن < شا
```


## [2026-09-14T01:00:03.105Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer('پاشید',t):\n    s=' '.join(t[m.start()-100:m.start()+150].split())\n    if 'پاشیدن:' in s or 'پاشیدن(' in s or 'پاش:' in s:\n        print('>>',s)\nprint('---- پاش')\nfor m in list(re.finditer('پاش:',t))[:5]:\n    print('>>',' '.join(t[m.start()-150:m.start()+200].split()))\nEOF"
}
```


### [2026-09-14T01:00:04.174Z] TOOL RESULT

```
>> ازصهر: 7 ([ع.] (ص‌تفف.. زاهر) روشن تر. (ص.) روشن» درخشان. سپید روشن» سپید رنگ» سپید روی. از هم پاشیدن: 22-12۳01027 ( مص‌ل.) پراکنده شدن» متفرق شدن. گسیخته شدن امرء تباه گردیدن کار. ازیرا: قع-2ه [- ازایرا - زیرا] (حر. رد. مر.) زیرا» برای اين
>> پاسوز: 02-7 (عم.) عاشق شیفته. پاسوز کسی شدن: زیان بردن به علت دوستی و محبت با کسی. پاش: ۲55 [ری. پاشیدن] (امص.) پاشیدن» برافشاندن. امر از «باشیدن». در کلمات مرکب مانند گهر باش مخفف پاشنده است. بر شان» افشان. پاشا: 7585 [- پادشاه| (امر.) در تدا
>> .) عاشق شیفته. پاسوز کسی شدن: زیان بردن به علت دوستی و محبت با کسی. پاش: ۲55 [ری. پاشیدن] (امص.) پاشیدن» برافشاندن. امر از «باشیدن». در کلمات مرکب مانند گهر باش مخفف پاشنده است. بر شان» افشان. پاشا: 7585 [- پادشاه| (امر.) در تداول ترکان عشمان
>> پای بیمار را بدان شویند. دیوارة حوض. آب رو گردا گرد حوض. پاشیب: «05-1 (امر.) نردبان زینه پایه. پاشیدن: «:05814 [- پاچیدن] (سصم.) (باشید»ه پاشد» خواهد پاشید» بباش؛ باشنده» باشیده» پاشان» پاشش). برا کندن» بر یشیدن» افشاندن. ربختن» باچیدن (عم.)
>> ض. پاشیب: «05-1 (امر.) نردبان زینه پایه. پاشیدن: «:05814 [- پاچیدن] (سصم.) (باشید»ه پاشد» خواهد پاشید» بباش؛ باشنده» باشیده» پاشان» پاشش). برا کندن» بر یشیدن» افشاندن. ربختن» باچیدن (عم.) شنجیدن. اب پاشیدن: اب زدن جایی را. ازهسم پاشیدن: متلاش
>> بباش؛ باشنده» باشیده» پاشان» پاشش). برا کندن» بر یشیدن» افشاندن. ربختن» باچیدن (عم.) شنجیدن. اب پاشیدن: اب زدن جایی را. ازهسم پاشیدن: متلاشی کردن. پاشیر: ۲2-337 (امر.) زیر زمین خرد که شیر اب انبار بر دیوار آن نصب شده است؛ گودال پای شیر آب ان
>> پاشش). برا کندن» بر یشیدن» افشاندن. ربختن» باچیدن (عم.) شنجیدن. اب پاشیدن: اب زدن جایی را. ازهسم پاشیدن: متلاشی کردن. پاشیر: ۲2-337 (امر.) زیر زمین خرد که شیر اب انبار بر دیوار آن نصب شده است؛ گودال پای شیر آب انبار» کليةٌ بنای مجاور شیر » آن
---- پاش
>> بهای آب دهند (فره.)؛ اب بینی: 101 2-.2 (امر.) آب غلظ که از بینی جاری گردد؛ خل. آب‌پا: 3-.1 (انا.) میراب؛ آب باینده» آنکه در تقسیم ] اب پاش: *05-.2 (امر.) آلتی آهنی یا حلبی اب نظارت دارد. دسته‌دار که دارای لو له درازی است و سر ان پهن و سوراخ سوراخ است و بدان اب‌پاشان: 2.7 (امر.) (جشین آب باشان): جشنی در ايران باستان که تا
>> ر با؛ پبادة جلد و چابکك. پاسور: ۲8-907 (.) نوعی از بازی ورق. پاسوز: 02-7 (عم.) عاشق شیفته. پاسوز کسی شدن: زیان بردن به علت دوستی و محبت با کسی. پاش: ۲55 [ری. پاشیدن] (امص.) پاشیدن» برافشاندن. امر از «باشیدن». در کلمات مرکب مانند گهر باش مخفف پاشنده است. بر شان» افشان. پاشا: 7585 [- پادشاه| (امر.) در تداول ترکان عشمانی صاحب رتبة پاشایی و
>> ان بطوری عمود بر پنجه‌ها قرار گرفته و ظاهرا بجای استخوان ساق می‌نماید. پریا: ۳۲-5 [- بربایه] (امر.) (جاذ.) خرخاکی» خرخداء حمار البیت» پریایه. پرپاش: ۲۰54 (امر.) طبقی چوبین که با آن حوب را باش دهند» طبق چوبی که غلات و حبوب را در آن ریزند و پاک پریر: 06۲-۲ (اصت.) (تد. اطفال) صدای "۳ فرهنگک فارسی معین پر بره بربدن گنجشک و مانند 1 پر پ
>> و جز آن. سوخت اما: قجقت۳: [- سوخت آماینده] (ص‌فا.) (نو.) (فر.) کاربوراتور. ضح.- ایین کلمه رواج نیافته و بسجای آن همان کاربوراتورمستعمل است. سوخت پاش: 5-.: [- سوخت باشنده] (ص‌فا.) [۳ برای براکنده کردن نفت و بنزین در ماشین‌ها» ژیکلور. ضح.- این کلمه رواج نیافته و همان ژیکلور داول است. سسو ختگی: آ-ع(2)6:: (حامص.) عمل سوخته شدن. درد و مسصیتی ک
```


## [2026-09-14T01:00:10.973Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg407.png"
}
```


### [2026-09-14T01:00:11.505Z] TOOL RESULT

```

```


## [2026-09-14T01:00:11.503Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:00:24.545Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T01:00:24.552Z] TOOL RESULT

```


```


## [2026-09-14T01:00:28.659Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/preyH-",
 "prompt": "Give the reconstructed root, its meaning, and the list of descendants (especially Proto-Indo-Iranian, Avestan, Proto-Germanic *frijōndz/*frijaz, Old English frēo, Frīgedæġ). Quote the root gloss verbatim."
}
```


## [2026-09-14T01:00:30.485Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%B1%DB%8C%D8%AF%D9%86",
 "prompt": "Persian آفریدن: give the full etymology (Middle Persian form, Proto-Iranian, Avestan, PIE root) verbatim."
}
```


### [2026-09-14T01:00:33.551Z] TOOL RESULT

```
# Proto-Indo-European Root *preyH-

**Reconstructed Root:** *preyH-

**Meanings:** The root glosses as "to please" and "to love"

**Key Descendants:**

The primary attested descendants include:

- **Proto-Indo-Iranian:** *prináHti (nasal-infix present form)
  - Sanskrit: prī́yate ("to be pleased")
  
- **Ossetian** (via Proto-Iranian *friHmā́): Digor limæn, Iron lymǽn (both meaning "friend, lover")

- **Pashto** (via Proto-Iranian *friHnáh): wrin ("open, happy, sincere")

**Note:** The entry mentions an alternative reconstruction of *preyh₂-, and references note the form appears in Proto-Germanic and Old English derivatives, though the specific Germanic forms you mentioned are not detailed in this particular Wiktionary entry.
```


### [2026-09-14T01:00:35.285Z] TOOL RESULT

```
# Etymology of Persian آفریدن (āfarīdan)

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian:** The entry states the word comes "From Middle Persian [script needed] (āfritan)"

**Proto-Iranian:** It derives from "Proto-Iranian *ā- + *fraiH- ('to rejoice, atone, please')"

**Proto-Indo-European roots:** 
- The prefix *ā- comes from PIE "*h₂éd" meaning "to, at"
- The verbal component *fraiH- derives from PIE "*preyH-" meaning "to please; to love"

**Note on Avestan:** The document does not mention an Avestan form in the etymology section provided. The entry does list cognates including Sogdian, but Avestan is not explicitly referenced in the etymological reconstruction shown here.
```


## [2026-09-14T01:00:42.086Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B9%D9%81%D8%B1%D9%8A%D8%AA",
 "prompt": "Arabic عفريت (ʿifrīt): quote the etymology section verbatim — does it derive it from Persian آفرید/آفریدن, or from the Arabic root ع ف ر? Mention any cited scholars."
}
```


## [2026-09-14T01:00:44.240Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%84%D9%86%DA%AF",
 "prompt": "Persian پلنگ (palang): quote the etymology verbatim — Middle Persian form, Proto-Iranian reconstruction, relation to Sanskrit पृदाकु (pṛdāku) and Greek πάρδος. Also give any mention of یوزپلنگ."
}
```


### [2026-09-14T01:00:47.624Z] TOOL RESULT

```
# Etymology of Arabic عفريت (ʿifrīt)

Based on the Wiktionary entry, the etymology section presents **two competing theories** rather than settling on one:

**Theory 1 (Middle Iranian origin):** "From a Middle Iranian past participle _āfrīd_ ('created'), originally an elliptic expression for _\*dīw afrīt_ ('demon's creation')"

**Theory 2 (Arabic root origin):** Alternatively, it may derive "from the root ع ف ر (ʕ f r) related to 'ash', compare for the derivation type _عَكْرُوت_ (ʕakrūt, 'scoundrel')."

The entry does not cite specific scholars by name, nor does it decisively attribute the word to Persian آفرید/آفریدن. Instead, it acknowledges both possibilities: a loanword from Middle Iranian languages or a native Arabic formation from an existing root. This reflects scholarly uncertainty rather than consensus.
```


### [2026-09-14T01:00:50.271Z] TOOL RESULT

```
# Etymology of Persian پلنگ (palang)

Based on the Wiktionary entry, the etymology of Persian **پلنگ** (palang) involves cognates across several ancient languages:

**Comparative forms cited:**
- Bactrian: "πορλαγγο-ζινο" (porlango-zino)
- Pashto: "پړانګ" (pṙâng)
- Sanskrit: "पृदाकु" (pṛdāku, "panther")
- Ancient Greek: "πάρδαλις" (párdalis)

The entry notes these represent related forms across Indo-European languages, suggesting a shared etymological root referring to spotted felines.

**Note on یوزپلنگ:** The webpage does not contain any mention of this related term (which means "snow leopard" in Persian).

The entry indicates the word likely derives from a Proto-Indo-European source related to the concept of leopards and panthers, with the Sanskrit and Greek cognates being particularly significant for reconstruction purposes.
```


## [2026-09-14T01:00:54.872Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/leopard",
 "prompt": "Quote the full etymology of \"leopard\", including what it says about Greek pardos/pardalis and any Iranian/Sanskrit/Semitic origin."
}
```


## [2026-09-14T01:00:55.752Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fresh",
 "prompt": "Quote the full etymology of \"fresh\": the Proto-Germanic and PIE reconstruction given."
}
```


### [2026-09-14T01:00:59.885Z] TOOL RESULT

```
# Etymology of "Leopard"

The word "leopard" originates from Old French *lebard/leupart*, derived from Late Latin *leopardus*, literally meaning "lion-pard, lion-panther." According to the source, the ancients believed this animal was "a hybrid of these two species."

The Latin term comes from Greek *leopardos*, which combines *leon* ("lion") with *pardos* ("male panther"). Regarding the deeper origins, the source states that *pardos* is "generally said to be connected to Sanskrit *prdakuh* 'panther, tiger.'"

The entry for the related term "pard" provides additional detail: Greek *pardos* derives "from the same source (probably Iranian) as Sanskrit *prdaku-s* 'leopard, tiger, snake,' and Persian *palang* 'panther.'"

So the etymological chain traces through Old French and Latin back to Greek, with the ultimate root likely being Iranian or Sanskrit in origin, indicating this terminology traveled along ancient trade and cultural contact routes.
```


### [2026-09-14T01:01:00.758Z] TOOL RESULT

```
# Etymology of "Fresh"

Based on the provided content, here is the full etymology with Proto-Germanic and PIE reconstructions:

The word "fresh" derives from **Proto-Germanic *friskaz**, which is the source of related forms across Germanic languages (Old Frisian *fersk*, Middle Dutch *versch*, Old High German *frisc*, German *frisch*).

The content also notes the word is "probably cognate with Old Church Slavonic *presinu* 'fresh'" and Lithuanian *preskas* "sweet," suggesting deeper Indo-European connections, though a specific PIE reconstruction is not explicitly provided in this source.

The Modern English form underwent metathesis from Old English *fersc*. Additionally, the word was influenced by Old French *fres*/*fresche* (from Proto-Germanic *frisko-*), which shares the same Germanic root and produced Italian and Spanish *fresco*.

Unfortunately, this etymology source does not provide a complete PIE root reconstruction for "fresh," focusing instead on the Proto-Germanic stage and documented daughter languages.
```


## [2026-09-14T01:01:08.997Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/friend",
 "prompt": "Quote the etymology of \"friend\", including Proto-Germanic *frijōjands, the verb *frijōnan 'to love', PIE *pri- 'to love', and the related words free, Friday, Frigg."
}
```


## [2026-09-14T01:01:11.586Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%80%CE%AC%CF%81%CE%B4%CE%B1%CE%BB%CE%B9%CF%82",
 "prompt": "Ancient Greek πάρδαλις / πάρδος: quote the etymology section — is it called an oriental/Iranian loanword? What does it say about Sanskrit pṛdāku, Persian palang, Hittite paršana-, and Beekes's opinion?"
}
```


### [2026-09-14T01:01:13.811Z] TOOL RESULT

```
# Etymology of "Friend"

According to the Online Etymology Dictionary, "friend" originates from Old English *freond*, derived from Proto-Germanic *frijōjands* meaning "lover, friend." This stems from the PIE root *pri- meaning "to love."

The entry states: "from Proto-Germanic *frijōjands 'lover, friend'...from PIE *priy-ont-, 'loving,' present-participle form of root *pri- 'to love.'"

The word's linguistic family includes cognates across Germanic languages: Old Norse *frændi*, Dutch *vriend*, and German *Freund*. Interestingly, the entry notes that Old English paired *freond* alliteratively with *feond* ("fiend," meaning enemy)—opposite in meaning despite similar grammatical structure, both deriving from verbs expressing love and hate respectively.

**Note:** The provided content does not discuss connections to "free," "Friday," or "Frigg," so I cannot include those related words based on the source material available.
```


### [2026-09-14T01:01:16.831Z] TOOL RESULT

```
# Etymology of πάρδαλις

According to the Wiktionary entry, the word is described as "Borrowed from a foreign eastern language." The etymology section compares it to several Indo-Iranian terms:

- **Sanskrit**: pṛ́dāku
- **Persian**: palang
- **Pashto**: pṛāng
- **Bactrian**: porlango-zino
- **Sogdian**: pwrδnk

The entry also references a related term, πάνθηρ (panthēr), though Hittite paršana- is not mentioned in this particular article.

Regarding scholarly opinion, the entry cites Robert S. P. Beekes's *Etymological Dictionary of Greek* (2010) as the source for this etymological information, indicating that Beekes supports the Indo-Iranian origin theory for this Greek animal name.
```


## [2026-09-14T01:01:24.234Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"FRIDAY\" AHD_watkins1985.txt | head -5; echo ---; grep -n \"^prī\\|^pri\\b\\|^pri-\\|^prI\" AHD_watkins1985.txt | head; echo ---; grep -n \"To love\\.\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:01:24.354Z] TOOL RESULT

```
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
---
---
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
```


## [2026-09-14T01:01:32.722Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=afreet",
 "prompt": "Give the AHD entry for \"afreet\" verbatim, especially the bracketed etymology."
}
```


## [2026-09-14T01:01:33.612Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/afreet",
 "prompt": "Quote the etymology of \"afreet\" — what origin does it give for Arabic ifrit?"
}
```


### [2026-09-14T01:01:36.502Z] TOOL RESULT

```
I don't see any etymology entry for "afreet" in the web page content provided. The page shows the Etymonline website's header, navigation, and footer, but doesn't include the actual dictionary entry or etymology information for that word.

To find the etymology of "afreet" and its Arabic origin "ifrit," you would need to search the Etymonline database directly on their website.
```


### [2026-09-14T01:01:38.567Z] TOOL RESULT

```
# AHD Entry for "Afreet"

**Headword and Pronunciation:**
"af·reet (ăfrēt′, ə-frēt) also af·rit (ăfrēt′, ăfrĭt′, ə-frēt, ə-frĭt), also if·rit (ĭfrēt′, ĭfrĭt′, ə-frēt, ə-frĭt)"

**Definition:**
"A powerful evil spirit or gigantic and monstrous demon in Muslim tradition."

**Etymology (Bracketed):**
"[Arabic _'ifrīt_, from Middle Persian _āfrīd_, created (an afreet probably being so called because it is a "creature," a creation of God or divine powers), from _āfrīdan_, to bless, create, from Old Iranian _\*__āfrī-_, to bless (attested in Avestan _āfrī-_) : _\*__ā-_, to, towards, hither + _\*__frī-_, to rejoice, please; see **prī-** in the Appendix of Indo-European roots.]"
```


## [2026-09-14T01:01:43.613Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=pard",
 "prompt": "Give the AHD entry for \"pard\" verbatim, including the bracketed etymology (Latin pardus, Greek pardos, and any Iranian/Sanskrit note)."
}
```


### [2026-09-14T01:01:46.744Z] TOOL RESULT

```
# AHD Entry for "Pard"

**Pronunciation:** (pärd)

**Definition:** "A leopard or other large cat."

**Etymology:** "[Middle English _parde_, from Old French, from Latin _pardus_, from Greek _pardos_, probably of Iranian origin; akin to Sogdian _purdhank_.]"
```


## [2026-09-14T01:01:57.571Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/preyH-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%B1%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B9%D9%81%D8%B1%D9%8A%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%84%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%AC%CF%81%CE%B4%CE%B1%CE%BB%CE%B9%CF%82\" \\\n \"https://www.etymonline.com/word/leopard\" \\\n \"https://www.etymonline.com/word/fresh\" \\\n \"https://www.etymonline.com/word/friend\" \\\n \"https://www.ahdictionary.com/word/search.html?q=afreet\" \\\n \"https://www.ahdictionary.com/word/search.html?q=pard\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 407, roots Pri/Prs: afarin/ifrit/palang/pard verification\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:02:02.573Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4e43b999d1a4927a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/257fe13f56b17277.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6f9db27bac45962.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cdd8a571b645aec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4dd40d5b9d91b9c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c5a2715369718be.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/460be8e07e4d4dda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05d8a20af8f45ba7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b5f47c26500ef9ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec8d545cf9576be6.txt
```


## [2026-09-14T01:02:11.721Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT parsuya\"; grep -n \"parsuya\\|par§uya\\|parsuia\" BRT.txt | head -5; echo \"== FVQ ifrit\"; grep -n -i \"ifrit\\|'ifrīt\\|afrit\" FVQ.txt | head -10; echo \"== NYB afrin\"; grep -n \"āfrīn\\|'pryn\\|afrin\" NYB_vol2_glossary.txt | head -8; echo \"== SOD purdnk\"; grep -n \"pwrdnk\\|purdank\\|purOank\\|leopard\" SOD.txt | head -8"
}
```


### [2026-09-14T01:02:11.892Z] TOOL RESULT

```
== BRT parsuya
== FVQ ifrit
== NYB afrin
283:ā-dūš [Pdwšy Ps.] armful 12817. — Av. | äfritan, āfrīn-, to create, of gods: äfrit u
2698:(1016 sq.) frāy-, opp. dfrin (q. v.); MPrs nfryn (S); Paz. nifrin; NP nafrin.
3272:āfrīn (q. v.) ~ i rāstē u ~ i ahläyeh the
3575:w. after a lengthy digression: Ohurmazd, ka Ahriman apāk (g. v.), -(a)š hämöden dam u dahišn ... frac kart 9145, -(a)š re- ferring back to Ohurmazd; in this case the independent form aš would have been more appropriate, as in api-š hamäk da- mik, i-š apar rah būt, aš [8] perdvanihit (g. v.) kart 3316-17, — If it belongs to a prep. this changes to an adv., in a special adverbial form if there is one, which is placed afterwards in the sentence: (-š — andar:) api-š ... must" (g.v.) u drog andar nest F:6-7; — (-$ — apar:) api-š Vīdrafš . apar nišinčt V. gets on it (the horse) 2515; cé-§ apar baxt estet dušman dzanét 2714, v.s. v. baxtan; — (-$ — hac pas:) api-$ hac nihän hac pas fräc dväret from behind him 2519-20; — (-$ — avis, adv. of 0): tài ka-š hàn Hamäk . . . pat zanéh avis dahom to him 261-2 (285 without avis); 26°; bē-š avis barét ...! 767-8; — (-š — haciš:) gobet kū-š ma saxvan  haciš pursēt 7487; — (-§ — patis:) api-š afrin patiš kunēt (BYDWN-x,) 2716-17; apt-š dēvān apasēs u riyahreh patiš kunēnd 7526-27; — this construction is regular in relative clauses, v. s. v. ? and ka. — The adverbs avis, haciš and patis may be used alone as substitutes for 6, hac, pat + š, v. these ws. — Attached to a prep., but belonging to the governed subst.: 6-§ zäyisn until his birth 4412; in apāk-aš pat asp mišast estat 88 -š belongs to the whole sentence, cf 8? 4-6 apāk pat asp, and its place after apäk is fortuitous. — OP -Saty; common Milr and NP; v. -šān. šagr [šgl] lion; the constellation Leo 51, — MPrth srg (MHC); MPrs Sgr (A-H I); NP šēr.
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
3940:Ghilain 79, is an error]; Arm. lw. vawer, vawerakan < *vāvarya(kana)- ‘true, valid, authorized’ (thus in the sense of *vä- para-); — MPrs wbr, wbryg ‘faith’, w?bryg?n ‘true’, possibly also pl. cas. obl. 'the believers'; on the other hand MPrs w^wrydn ‘to believe’, in all probability borrowed from Prth; Verbum 195, Ghi- lain 79, S, Gloss. s. v. w’bryg’n. — BP always w’pl-, mostly in the sense of ‘true, truth’, seldom ‘belief’; Ps. w’plyk’n ‘true’; Paz. vawar ‘truth’, but vafringqni (SGV) through confusion with Gfrinakan;
5536:’frywn: āfrīn
6528:dätan dadigar: ditikar dačsta: dätistän daéstamandi: dätistänö- mandéh dahan: dahan dahišn(i): dahišn, dašin dahma: Dahman afrin dahum: dahom dam: dam damastan: damistàn dana: danak danastan, -estan: danis- tan
== SOD purdnk
63154:leopard 
91237:leopard     8204
```


## [2026-09-14T01:02:15.404Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '283,290p' NYB_vol2_glossary.txt; echo \"=== 2695-2700\"; sed -n '2695,2702p' NYB_vol2_glossary.txt; echo \"== SOD 8204\"; grep -n \"8204\" SOD.txt | head -5"
}
```


### [2026-09-14T01:02:15.482Z] TOOL RESULT

```
ā-dūš [Pdwšy Ps.] armful 12817. — Av. | äfritan, āfrīn-, to create, of gods: äfrit u
(674) daoš-, v. Barr, Gl. s.v.
adyän [’dyn] Prth, then, this being so HajA: 10. - MPrth ?dy'n (S, A-H III); to be distinguished from SW ’DYN, v. adak.
a-frac-saci8néh [’pr’c sešnyh] the quality of not passing away, continuance, con- tinued existence (of the family) 597°. — Av. (1554) pasca frasaxtahe mašyehe ‘after mankind has come to an end’, Vd. 1928, is rendered in Phl. by pas hac fräc-sacisneh i martömän, v. sacišneh.
ātrās [’pl’s; B*W] learning, teaching 6713. 8423; bun u [B'W =] äfräs original text and teaching (= doctrine based on the bun) 1119. — NW form; MPrs "fr?h, ’/r’h, *pr*h ‘teaching, doctrine’ (8, BBB); Paz. veh-äfräh ‘of good learning, well informed in the good Religion’, Skr. v. uttama-hita-ddyaka (Aog.). Cf Av. (999) d-fras-. — FrP 30 (31) BSW bg. bd. ’pl’s ’pl’h, that is: BSW: bag (bay) äfräs (äfräh), which means: “the ideogr. B*W signifies bag äfräs = [SW form] bay djfrah". BSW, wholly coinciding in writing with bwn = bun, is BAT, st. abs. of Syr. BATUTA ‘petition, rogation’, the prob- able sense of the Ir. equivalent being ‘petition to the King or a royal person’. The lemma is thus given in Cod. S,, but mutilated or corrupted in the other MSS; unrecognizable in Junker’s ed. (ch. 31).
äfrin [inser., Ps. ’plyny; ’pryn'] benedic- tion, praise, blessing 773. 12818; ~kartan to praise, to glorify, to utter benediction P1:10-11. F: 5. 12819, 116, 1511; to bless 9427; to perform an invocation P 2:5. — dahman ~: v. dahmān. — Av. (331) äfrivana-; MPrth ?frywn; MPrs ?fryn, pryn (S, A-H Il); NP 4f(z)rin. Cf the next ws.
üfritak [’plytk'] (heavenly) created 6218, from
dat 8818. MPrth ’fryd ‘created’; generally regarded as identical with Av. (1017) ā- fräy-, pres. ā-frīnā-, MPrth ?frydn ’fryn- (v. also Sogd. 1774); MPrs ’prydn, ?pwr- or ?fwr- (S, A—H II) ‘to praise, to bless, to worship’, cf s.v. appurišn. Another etymology by Bailey, BSOS VI, 1931, 587.
=== 2695-2700
Nishapur
nézak [nyck'] lance, javelin 201° and passim. — Av. (1037) naéza-; MPrth nyzg
(S); Paz. neža; NP mizah; Arab lw. naizak-. nifrin [nplyn'] curse 9717”. — ni + Av.
(1016 sq.) frāy-, opp. dfrin (q. v.); MPrs nfryn (S); Paz. nifrin; NP nafrin.
nifritak [nplytk'] cursed 661°”. — Pt. of ni-fräy-, v. above.
*nigné-sar [*ngnys'1] *annihilated, *pow- erless 902%. — Reading quite hypothetical; Paz. substitutes nazär ‘thin, emaciated’, Skr. v. krsa. The last element may be -sär as in NP nigü-sür ‘turned upside down’, but the first element, which allows a great many other readings, can by no means be identified with NP nigü <
mikun (let alone that the meaning does |
not suit the context). Could it guite simply be the Av. (492) pres. niyne ‘I shall knock down’ Yt. 45 (Owgmca dru- jomca niyne), taken over from the Av. lan- guage as a petrified term? A mere guess.
== SOD 8204
63151:8204  pwr8>nk   B  £& 
91237:leopard     8204
```


## [2026-09-14T01:02:25.538Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; python3 - <<'EOF'\nimport re,io\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'prāi-' in p or 'prai-' in p or 'prāi' in p:\n        print(i, ' '.join(p.split())[:150]); \nEOF"
}
```


### [2026-09-14T01:02:26.653Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 725
```


## [2026-09-14T01:02:30.354Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find page with '86' running head near 'fri' entries\nfor i,p in enumerate(pages):\n    if re.search(r'\\bfrij[oō]n', p) or 'frijonds' in p or 'Frigg' in p:\n        print('leaf',i, ' '.join(p.split())[:200]); print()\nEOF"
}
```


### [2026-09-14T01:02:31.623Z] TOOL RESULT

```
leaf 47 per- 43 Lit. p'^rhtnas „Donner; der Donnergott bei den alten Litauern“, per- Icunija jjGewitter^, lett. pt'rhims (u. dgl., s. Muhlenbach IF. 17, 428 f.) j.Donner, Donnergott^^ apr. perctinis „Doiiner“

leaf 90 86 pra prei-, prei-, pri (pri-) pra- „biegen“. Lat, 'pravus „krumin, verkehrt; ungestalt; schlimm, bose^. Dazu wohl pratum „Wiese“ (als „feuchte, bewachsene Einbiegung des Bodens‘‘, vgl. „Einsenkung, 

leaf 91 preu- 87 va-m j,das Liebsein oder -haben'' (: gotfrijapwa f. „Liebe‘'), priydta ds. (= 2ig'&,freod „Liebe“); mit *pr9i-prdyah n. ,,Yergnugen, Ergotzen, Genu6“, prBndn- m. n. „Liebe, Gunst'', prHdr- „'
```


## [2026-09-14T01:02:34.284Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(' '.join(pages[90].split())[:2000])\nEOF"
}
```


### [2026-09-14T01:02:35.529Z] TOOL RESULT

```
86 pra prei-, prei-, pri (pri-) pra- „biegen“. Lat, 'pravus „krumin, verkehrt; ungestalt; schlimm, bose^. Dazu wohl pratum „Wiese“ (als „feuchte, bewachsene Einbiegung des Bodens‘‘, vgl. „Einsenkung, Wiese“: lenHi j,biegen'‘) und als „Aufbiegung, z. B. lit. lanlca Wolbung, HiigekS mir. rath, raith f. „Erdwand, Erdbank^, mcymr. hed-rawt, ncymr. beddrod m. „Grabhugel, Grab“, cymr. gaeaf-rawd „a winter-abode", bret, bez-ret f. „Begrabnisplatz, Friedhof", gall, ratin acc. sg. „Burg(hugel)", Argento-ratiim (%), Fick II^ 226, Stockes BB. 23, 52, Vf. LEWb.^ s. v., Osthoff MU. VI, 92 a (mit unannehmbarer Gdbed., zu ^praiu-s), prain-8 „energielos, lassig". Ai. d-prayii-, gr. ngavg, s. u. prti- „gern haben, schonen". prat- „ver8tehn". Got. frapi n. .,Sinn, Yerstand", frapjan, frop „verstebn“, props „klug, verstandig", aisl. frodr „klug, kundig", as, ags. frod, ahd. fruot „verstandig, weise", mhd. vruotec, vriletec „schnell entschlossen, munter, tapfer", nhd. schweiz. fruetig „munter, froh, frisch, tapfer, schnell", in ahnlicher Bed.- Entw. auch ahd. frad „strenuus efficax", fradoMh „procax"; lit. prantii, prdsti „gewohnt werden", suprdsti „verstehn", protas „Yerstand", lett. pru'tiij prast „verstehn, begreifen, merken", pra'ts „Yerstand, Sinn, Wille, Gesinnung, Meinung, Gemiit", apr. pratin acc. „Rat“, issprestim „verstehn", ispresnan acc. „Yemunft", isspreitingi adv. „namlich" (e scheint aus a ent- wickelt nach den bei Trautmann Apr. 100 f., § 7, a, a und y entwickelten Regeln): mir. rorathaig „er bemerkte". Curtius KZ. 4, 237, Gdz.^ 673, Fick KZ. 20, 449, Wb. 487, Windisch KSB. 8,11, Fick m 226. Femzubleiben hat gr. (pga^co (Lit. bei Wiedemann BB. 27, 237 ff.) und lat. interpres, interpretari (s. Yf. LEWb.^ s. v. und besser Bergk Phil. 14, 185, Usener Kl. Schr. I, 253: Hypostase aus inter partes mit diss. Umstel- lung von -ter-per-i- zu -ter-pre-t). Fiir e-Yokalismus der Wz. ist das PreuB. keine ausreichende Stiitze, s. o. ; und antfrist „interpretatio", antfrist^ antfristo
```


## [2026-09-14T01:02:43.404Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (53,54,55):\n    s=' '.join(pages[i].split())\n    print('--- leaf',i, s[:1400]); print()\nEOF"
}
```


### [2026-09-14T01:02:44.550Z] TOOL RESULT

```
--- leaf 53 perth- — perd- 49 unsicher; anders iiber die germ, Worte Zupitza Gutt. 6 (: ai. spr^dti „be- riihrfc*', ptc. so faurlits eig. „timore affectus ((pofio)) e>c7cka- beachtenswert, aber ein Yerbum "^furhen j,affectum esse'* docb sehr in Frage stellend. Ificht uberzeugend weiter Giintert Reimw. 47 f.); Johansson IF. 8, 166a (: si. parkafa- „Angst", unbelegtes, unsicheres und etymologisch nicht verwendbares Wort); Bezzenberger BB. 12,77 (: lat. querquerm, doch unhaltbar, s. Yf. LEWb.^ s. v.) Collitz aaO. (: cymr. : erch „horrendus", erchyll „horribilis“, idg. perq-, nicht Lewy IF. 32, ; 159 (lit. pe/V9^e^i„schmerzen"; nicht uberzeugend); verfehlt SutterlinIF.25,65. perth- „Rute, Stange, SchoBling*'. Ai. ha-prth- „mannliches Glied" (iiber and ere Deutungen s. u. kapro -) arm. orf (o-St.) „Weinstock, Rebe“; vielleicht gr. nxoQ'dog „Scho61ing“ (vgl. TiToXejuog noleiJ^og u. dgl. : kann als '^m-oo§og zu eredh -) wohl auch ; ; lat. pertica „Stange" ” o. pere\kais\ „perticis“, u, perknf „Yirgas“ (kaum Ab- leitung Yon ^per^-ti zu per- „hiniiber uber“ 1 auch nicht nach Persson : Beitr. 474 f. zu slaY. p^rn „stutze usw., s. u. sper „Sparren"); nasaliert abg. prqi^ „Rute" {"^prontJio-), Kaum ist mit einer Bed.-Entw. „Spro6“ — „Junges‘‘ auch ai. prtJm-ka-h „Rind, Kalb, Tierjunges", arm, orf (u-St.) „Kalb des Rindes oder Hirsches^' (s. Hiibschmann Arm. Gr. I 483) anzu- schlieBen, da eher mit gr, 

--- leaf 54 50 Potd- — persaa konnteu (vgl. zur Bed. russ. peVesyj ^^gefleckt, bunt“ : abg. peles^ „grau‘*), spricht fur idg. rnach Charpentier KZ. 47, 175 fF. gr. negdil, -r/og „Reh- huhn“ (wie auch in ahd. repa-huon usw. eine Farbenbezeichnung steckt; freilich konnte nigdti aucb Schallwort sein, nach seinem schwirrenden Aufflug) und die Ahnlichkeit mit den gleichbed. Wzln. perJc-^ pers-. poFd- „na6, feucht, 8chleimig“. gr. jiagdaxog „na6, feucht“ (jon. nogdaxog^ woraus nagdaxog assimiliert), \ett purdtd'i „Nasenschleira“. Persson Beitr. 229 (s. auch 8S7a 1, 946, Boisacq s. v.). perp- „schwellen; aufblasen'^? Lit. parpstu, parpau^ parpti = „aufdinsen'', piupti „sich aufblahen‘‘ {wareo pufpia „der Prosch blaht sich auf“), papurp^s „angeschwollen, auf- getrieben, stolz aufgeblasen''; hellenist. nsQjieQog „eitler Windbeutel, Geek, dummer Schwatzer“, TceQTteQsvojuai „prahle, briiste mich‘^; Persson Beitr. 269. Ganz unsicher; denn die lit. Worte konnten wegen parpm, parpti „knarreD, quarren“ auf eine Schallvorstellung, etwa des Prustens mit auf- geblasenen Backen zuriickgehen, und die spaten gr. Worte gestatten kein Urteil liber ihre Bed.-Entw. (Entlehnung aus lat. perperam^ s. u. „2^er-hinaus- iiber“ B,ist freilich auch sehr unsicher, s. Havers IP. 28, 202 a 1, dessen Verbindung von nsgjieQog als „einer, der einen Titsch hat“ mit jiijgog „ge- lahmt'‘ = ,,vom Schlage getroffen“ aber nicht einl

--- leaf 55 (pel-) — pel- 51 Sana j.Ferse^, ags. fiersni^fersm) ds. Z. B. Fickl^ 81 f., 254, 476. Da6 der gr. Anlaut pt- das urspriingliche darstelle, ist hochst fraglich (vgl. z. B. 7i(x)6)dg unter „Burg“, wo Lit.); ebenso daher auch die Herleitung eines solchen "^pter-sna aus dem r-St. ^peier in nreQv^ usw. (s. u, pet- „worauf losstiirzen, fliegen“) unter einer an sich schon wenig einleuchtenden Gdbed. „Flug- Oder Fallgelenk“. Gegen andere Deutungen von lat. perna s. Vf. LEWb.2 s. V. 1. (pel-), pelo^ gen. peLes und *poli-s „Burg‘^, d. i. ursprgl. 5 ,uni- wallte Hohe als Pluchtburg‘‘. Ai. pur {. (pur-ki, pilr-am^ pur-dh) „Burg, Stadt“, piira- n., nachved. puri-li, purl ds. lit.; piVis f. „Burg, Schlo6‘S lett. pi'ls ds. (idg. "^p^li-s Oder vom Acc. sg. pi. auf -w, -i^=urbalt. -im, -ins aus von der kons. in die /-Dekl. iibergefiihrt, wie z. B. lit. szirdis) gr. ndkig, nrokig „Stadt; Staat“. ; Curtius^ 281. 7i{T)6Xig nicht nach Pick BB. 5, 167f., Wb. 82 zu q^el- ,,colere“; iiber den gr. Anlaut nxin nicht iiberzeugend Jacobsohn KZ. 42, 264 fF., bes. 272 f., Schrijnen KZ. 44, 19 (s. auch Hermann Sprw. Kommentar zu Homer 15f., sowie nxoXefxog, nokefiog u. pel- „unruhige Bewegung‘‘); fiir Jacobsohns Anlaut pu-^ der allerdings vielleicht die Herleitung von 7c6/ug aus "^pu^is = lit. piVis^ ai. puri-h ermoglichen wiirde, kann nMri „Stadttor, groBes Tor'' und ai. gopura-m „Stadttor" wegen des ganz u
```


## [2026-09-14T01:02:59.139Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (51,52,53):\n    s=' '.join(pages[i].split())\n    for m in re.finditer(r'pers-', s):\n        print(i, s[max(0,m.start()-400):m.start()+700]); print('...')\n        break\nEOF"
}
```


### [2026-09-14T01:03:00.364Z] TOOL RESULT

```
51  etwas heran)" mit Acc. der Richtung, vielleicht aus gedoppeltem ‘‘^proque proqiie „immer vor warts heran'* losge- lost (s. Vf. LEWb.^ s. V.; verfehlt Wood Min. 1914, S. [2] des S, A., Fay AJPh. 31, 418). 2. (perq-):prq- „gluhende Asche, Kohle‘\ Lit. pirksznys f. pi. ,, Asche mit gliihenden Funken", lett. pirksti^ pirkstes pi. besser nach J. Schmidt Yoc. II 28 mit eingeschobenem k zu ds. (nicht "^pers- ..spriihen, stieben"); air. riches „Kohle", bret. reges „Kohlenglut“ (f'prki-stcij Ygl. das lett. Formans), syncopiert cymr. rhys-ijn, PL rJiys-od „Ammern‘S mit anderem Formans acorn, rcgihten „pruna“. Fick IP 56, Ygl. zu den kelt. Worten noch Pedersen KG. I 484, II 20 f. Ob als „spruhend“ zu '^sp{h)er „streuen, spriihen"? vgl. lett. spirgsti „gluhende Kohlen unter der Asche" u. sp{li)er{e)g- „zucken spriihen". 3 perq^(o-) Baumname, ursprgl. Yermutlich „Eiche“. Ai. parkatl „ficus religiosa, ficus infectoria" (Hirt IP. 1, 481), nind. (mit offenbar alterer Bed., Hoops \Yaldb. 119) pargdi SSteineiche"; lat. quer- CHS, „Eiche" (zur Stammbildung s. Yf. LEWb.^ s. y.); ahd. fereh-eih -lis „Ei
...
```


## [2026-09-14T01:03:05.140Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    s=' '.join(p.split())\n    if 'parsuya' in s or 'pr^sat' in s or 'prsat' in s or 'pfsat' in s or 'Schneewasser' in s:\n        print('leaf',i,'-->',s[:1500]);print()\nEOF"
}
```


### [2026-09-14T01:03:06.353Z] TOOL RESULT

```
leaf 50 --> ; 46 perk- mann BPhW. 1903, 1305), ligur. (Olsen KZ. 39, 608) Porcohera „PIufiname^‘, mir. (und nir. earc, s. o.) „Lachs“ (Stokes KZ. 35, 595), lat (germ.) o)x fario, (Ausonius) vermutlich „Laclisforelle“ (germ, ^farhion-, das sich entweder zu aM. faro yerhalt, wie de^-tog zu got. taihswa, oder aus "^farhvjon- entstanden ist); aisl. fjqrsungr „trachinus draco“ {^perksnJco- zur Farbung des Fisches s. Falk-Torp u. fjessing), redupl. vielleicht nd- ein Fisch im Prasiassee („Forelle?“; Fick BB. 29, 235). Vermutlich hieber dtirch Diss. eines "^perh-ro-s oder prJc-7'o-s zu "^peJero-, (== „bunt“ nach dem Geschmacke polcro- lat. pul{c)}ier, alat. polcJier „schon‘‘ von Katurvolkern; Schweizer KZ. 1, 55, Yf. LEAVb.- s. v. Hasses Gl. 3, ; 276 f., Verb. m. placet als „gefMig“ weiB ich mit dem Yokalismus von dessen Wz. plUq- nicht in Einklang zu bringen). Gr. ngdy^y -y.6g „Tropfen (dehnstufig; nach Brugmann 477 mit ,,7*^) und die Bed.- Verb, bei ai. prsant- „gesprenkelt, bunt“, prsatt „scbeckige Kub, gefieckte Antilope'', p[satd~m „Tropfen'', cech. prseti „spruhen, stieben, regnen'' usw., weisen auf Entw. der Bed. ,,gesprenkelt" aus „sprit2 en, spriihen" (nhd. sebweiz. sprigel, spregel „Flecken", mnd. springel „Sommer- sprosse", a. dan. spranglet „gesprenkelt", z. B, Fick III^ 5 6, stiinden dann 1 als Bildungen von einer s-anl. Wzform unserer Gruppe nahe, s. spQi)er{e)g „zucken“) ; und ^per-s- (ai. prsant- usw.) sind verschiedene Erw. von "^per- „8pruhen"; ob aber nacb Pick BB. 29, 198f. 

leaf 54 --> 50 Potd- — persaa konnteu (vgl. zur Bed. russ. peVesyj ^^gefleckt, bunt“ : abg. peles^ „grau‘*), spricht fur idg. rnach Charpentier KZ. 47, 175 fF. gr. negdil, -r/og „Reh- huhn“ (wie auch in ahd. repa-huon usw. eine Farbenbezeichnung steckt; freilich konnte nigdti aucb Schallwort sein, nach seinem schwirrenden Aufflug) und die Ahnlichkeit mit den gleichbed. Wzln. perJc-^ pers-. poFd- „na6, feucht, 8chleimig“. gr. jiagdaxog „na6, feucht“ (jon. nogdaxog^ woraus nagdaxog assimiliert), \ett purdtd'i „Nasenschleira“. Persson Beitr. 229 (s. auch 8S7a 1, 946, Boisacq s. v.). perp- „schwellen; aufblasen'^? Lit. parpstu, parpau^ parpti = „aufdinsen'', piupti „sich aufblahen‘‘ {wareo pufpia „der Prosch blaht sich auf“), papurp^s „angeschwollen, auf- getrieben, stolz aufgeblasen''; hellenist. nsQjieQog „eitler Windbeutel, Geek, dummer Schwatzer“, TceQTteQsvojuai „prahle, briiste mich‘^; Persson Beitr. 269. Ganz unsicher; denn die lit. Worte konnten wegen parpm, parpti „knarreD, quarren“ auf eine Schallvorstellung, etwa des Prustens mit auf- geblasenen Backen zuriickgehen, und die spaten gr. Worte gestatten kein Urteil liber ihre Bed.-Entw. (Entlehnung aus lat. perperam^ s. u. „2^er-hinaus- iiber“ B,ist freilich auch sehr unsicher, s. Havers IP. 28, 202 a 1, dessen Verbindung von nsgjieQog als „einer, der einen Titsch hat“ mit jiijgog „ge- lahmt'‘ = ,,vom Schlage getroffen“ aber nicht einleuchtet, s. iiber jzygog u. „wehtun''). pers- ,;Spruhen, stieben, spritzen (bespritzt= gesprenkelt),
```


## [2026-09-14T01:03:18.811Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB peleng\"; grep -n \"peleng\\|palang\\|pilink\" HUB.txt | head -5; echo \"== HUB afrin/afriden\"; grep -n \"afrid\\|äfrid\\|afrin\" HUB.txt | head -5; echo \"== KLN free\"; grep -n \"^free,  adj\\|^free, adj\" KLN_1966.txt | head -3; echo \"== KLN Friday\"; grep -n \"^Friday\" KLN_1966.txt | head -3; echo \"== KLN fresh\"; grep -n \"^fresh,  adj\\|^fresh, adj\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T01:03:18.935Z] TOOL RESULT

```
== HUB peleng
5067:Mit Uebergang von w in a: palang 'Leopard oder
8534:Wrzl. vik*^ (oben p. 10); palang 'Leopard', vgl. skr.prdaku-;
9319:mrdtHka- *Weintraube'; palang 'Leopard*, afgh. pr(ing,[8kv,
== HUB afrin/afriden
== KLN free
== KLN Friday
15405:Friday,  n.  -  ME.  fridai,  fr.  OE.  frigedxg,  lit. ‘the  day  of  the  goddess  Frig’,  fr.  Frige,  gen.  of Frig,  which  corresponds  to  ON.  Frigg,  name of  the  wife  of  Odin  (see  Frigg),  and  dxg,  ‘day’, rel.  to  ON.  frijddagr,  Dan.,  Swed.  Fredag, OFris.  frigendei,  friadei,  fredei,  MLG.,  MDu. vridach,  Du.  vrijdag,  OHG .  friatag,  MHG.  vri- tac,  G.  Freitag;  prop,  a  loan  translation  of  L. Veneris  dies,  ‘the  day  of  Venus,  Friday’  (whence It.  venerdi ,  Rum.  vineri,  OF.  vendresdi,  F.  ven- dredi,  Proven?,  divenres,  Sp.  viernes),  itself  a loan  translation  of  Gk.  ’A^poSi-v,:;  qpipa,  ‘the day  of  Aphrodite’;  ON.  Frigg,  was  considered as  the  goddess  of  love.  For  the  second  element in  OE.  frigedteg  see  day.
== KLN fresh
15387:fresh,  adj.,  newly  made;  cool.  —  ME.  fresch,  fr. OF.  fres,  freis,  fem.  fresche  (whence  F.  frais, fem.  fraiche),  ‘fresh’,  fr.  Teut.  *  frisk-  (whence also  It.,  Sp.,  Port,  fresco,  OProven?.  fresc)\  cp. OiE.fersc  [whence  ON  .ferskr  (Dan  .fersk,  Swed. farsk)],  OFris.  fersk,  MLG.  versch,  Du.  vers (Dan.,  Swed.,  Norw.  frisk  are  MLG.  loan words),  OHG.  frisc,  MHG.  vrisch,  G.  frisch, ‘fresh’  [MLG.,  MDu.  vrisch  (Du.  fris),  are  bor¬ rowed  fr.  MHG.  vrisch].  These  Teut.  words  are prob.  cogn.  with  OSlav.  presinu  (for  *praiskino-), ‘fresh’  (whence  Lith.  preskas,  ‘sweet;  unleav¬ ened’).  Cp.  afresh,  refresh.  Cp.  also  fresco,  frisk. Derivatives:  fresh,  n .,  fresh-en,  tr.  and  intr.  v., fresh-en-er,  n.,  fresh-ly,  adv.,  fresh-ness,  n. fresh,  adj.,  obtrusive,  impudent  (slang).  —  G. frech,  ‘impudent’,  fr.  OHG.  freh,  ‘covetous, avaricious’,  rel.  to  OE  .free,  ‘gluttonous,  greedy, bold’  (see  freak,  ‘whim’);  influenced  in  form, but  different  in  origin,  from  fresh,  ‘new’, freshet,  n.,  a  stream  of  fresh  water;  a  flood.  — Formed  fr.  fresh,  ‘newly  made’,  with  suff.  -et. fret,  tr.  v.,  to  eat  away;  intr.  v.,  to  gnaw  (into, on  or  upon)-,  to  be  worn  away.  —  ME.  freten, fr.  OE  .fretan,  ‘to  eat  up,  devour’;  which  stands for  fr-etan,  fr.  pref.  fr-  (fr.  Teut.  *fra-)  and  OE. etan,  ‘to  eat’;  rel.  to  Du.  vreten,  OHG.  frejjan, MHG.  vre^jen,  G.  fressen,  Goth,  fra-itan,  of s.m.  See  for-  and  eat  and  cp.  frass.
```


## [2026-09-14T01:03:26.755Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nn=0\ntargets={8534:None,9319:None,5067:None}\nfor i,p in enumerate(pages):\n    n+=p.count('\\n')+1\n    for k in list(targets):\n        if targets[k] is None and n>=k:\n            targets[k]=i\nprint(targets, {k:v-10 for k,v in targets.items()})\nfor k,v in targets.items():\n    s=' '.join(pages[v].split())\n    idx=s.find('palang')\n    print('---printed',v-10, s[max(0,idx-300):idx+300])\nEOF"
}
```


### [2026-09-14T01:03:27.803Z] TOOL RESULT

```
{8534: 242, 9319: 263, 5067: 150} {8534: 232, 9319: 253, 5067: 140}
---printed 232 — 232 — bfinj^) 'Reis' (Mos. Geogr. ed. Soukry 43, 6 v. u., Galen, Yaismav.) = np. birinjf, gurinj^), afgh. vrize, skr. vrihi^ (Atharva Veda), gr. ogv'Qa ; — ganj *Schatz' (5. Jhd.) = np. ganj, phi. ganj Gl. and Ind. 274, skr. LW. ganja-, gr. yd^a, syr. Nill *Schatz', dazu X*1DT:i --= hebr. "\2u *S
---printed 253 — 253 — zd. varsni- und nach eingeschobenem Vokal in ddsan *Ge- schenk, Gabe* (= phi. dcihisn), rosan *heir = zd. raoxsna-, Ueber m aus g^, g^h + n siehe § 112, c; fiber s» aus 4'w siehe § 131. c) Idg. rfw, dAw — ap. np. n: sikanam zerbreche aus arisch *8kadnami, Wrzl. idg. slcend; vgl. zd. 6wna- J
---printed 140 — 140 — (arab. misk) 'Moschus* = musk; Hier folgt auf u entweder ein Zischlaut (s, s, z) oder ein i in der folgenden Silbe. § 25. Inl. u wird zu u durch Ersatzdehnung in : pur 'Sohn' aus *puhr neben pus (pusar) = ap. pttd'^a-; Sapur^) = phi. Sahpiihr. arm. Sapuh (alter Sapurh) = 'KSnigs-sohn . Vgl.
```


## [2026-09-14T01:03:32.476Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (242,263,150):\n    s=' '.join(pages[i].split())\n    j=0\n    while True:\n        idx=s.find('palang',j)\n        if idx<0: break\n        print('printed',i-10,'>>',s[max(0,idx-250):idx+250]); print()\n        j=idx+1\nEOF"
}
```


### [2026-09-14T01:03:33.664Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:03:36.569Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'palang' in p:\n        s=' '.join(p.split())\n        idx=s.find('palang')\n        print('leaf',i,'printed',i-10,'>>',s[max(0,idx-300):idx+300]); print()\nEOF"
}
```


### [2026-09-14T01:03:37.779Z] TOOL RESULT

```
leaf 155 printed 145 >> - 145 — gvsn *ManTichen* ~= zd. varsni-, skr. vrsni-; gnl 'Rose' aus *wrf- als Nebenform zu vard- (arab. arm. LW. vard, semn. vale, Horn Nr. 927, zd. varedO-). Mit Uebergang von w in a: palang 'Leopard oder Panther (aus *pulang) = afgh. prang *a tiger, a panther, skr. prdaku-^ gr. ndgdaXig^ nagdog; harnd *Jiingling' = hurnd, Vgl. § 23. In den Dialekten von Kasan, Semnan u. s. w. ist ur regelmassig zu ar, er geworden, wie im Ossetischen der r-Vokal zu dfr, dl (s. meine Etym. u. Laut

leaf 249 printed 239 >> Gurgm N. pr. = arm. Vrken; harg 'Blatt' --^ zd. vareka- ; kargas 'Geier = zd. kahrkasa- ; pargm re- ceptaculum aquarum' =^ arm. parken ; Lehnwort nargis aus *narkis — syr. Dpi3 = gr. vu^f/.iaoog u. s. w. ; — avingdn 'hangend' ^^ ap. ^d-vinkana- ptc. pr. med. der 7. CI. von Wrzl. vik*^ (oben p. 10); palang 'Leopard', vgl. skr.prdaku-; tang *enge', bal. tank zu skr. tatic, zd. taxma-, aber phi. taiig 61. and Ind. 121 ; rang 'Bergschaf -^ skr. rankii- ; angaram glaube, halte fur', arm. angarem, zd. hankaray^mi, aber phi. angart Phi. Mm. p. 05, Z. 3, angarend 3. pL pr. Gl. and Ind. 52. Nach r ersc

leaf 270 printed 260 >> s ^barz-nu-); mdlldan reiben\ phi. -marz, zd. marez; iola 'Hagel, Reif* aus *kirdak H. 684; naVRohr, skr. nada-, gr. vdg^og?; Mtlad aus MihlG>d{i^. 189) = Mihrdat; paz. kala 'verriickt', zd. hareii- (8iehe^§ 9, a); gul *Rose' aus *!?rd-, vgl. arab. arm. vard; mul 'Wain', skr. mrdtHka- *Weintraube'; palang 'Leopard*, afgh. pr(ing,[8kv, prdaku", gr. ndpduhg; dil *Herz* = zd. zered-^ skr. Ard-; hilad 'lasst' = ap. *hrdatiy = zd. herezaiti, skr. srjati (siehe § 34, a und b) ; gUa 'Klage* = phi. gilak, ap. "^grdor- = zd. gereza- (siehe § 110). Der Uebergang von rd in / fand in sassanidischer Zeit s
```


## [2026-09-14T01:03:49.263Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor f in ('BQT_v1_pages.txt',):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        if 'پارد' in p:\n            for line in p.split('\\n'):\n                if 'پارد' in line: print(f,'leaf',i,'printed~',i-220,line.strip()[:160])\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('پارد',t))[:6]:\n    print('MON >>',' '.join(t[m.start()-80:m.start()+160].split()))\nEOF"
}
```


### [2026-09-14T01:03:50.446Z] TOOL RESULT

```
BQT_v1_pages.txt leaf 22 printed~ -198 باغ‌و بوستانست. لفت‌پاردوس ار سنی‌بمعتی باغ وپالیز پارسی و فردوس عر یی ۸
BQT_v1_pages.txt leaf 24 printed~ -196 چپاردهم میلادی بجاما نده بعد از [ ین مدا رك و اسناد و مو لفات ختنی نو شته شده است 4
BQT_v1_pages.txt leaf 64 printed~ -156 بپارسی‌قدیم ترجمه کرد درتوحید وتجرید وحکمت‌وطاعت است.و آن‌چپارده
BQT_v1_pages.txt leaf 64 printed~ -156 صحیفه ایست که برچپارده بزر گواد نازل‌شده و آنرا در بندر بمیثی چاپ
BQT_v1_pages.txt leaf 121 printed~ -99 گفتن نکند . فاطع برهان در اکمل‌المطابع دهلی باهتمام فخرالدین و پاردیکگی
BQT_v1_pages.txt leaf 122 printed~ -98 مقد مه صد وچپارده
BQT_v1_pages.txt leaf 132 printed~ -88 عرض‌هفتاينچ. هر صفحه قر یب‌چپارده‌سطر؛ طول‌هر سطر شش اینچو نیم» در
BQT_v1_pages.txt leaf 508 printed~ 288 تا۱ه - بطلمیوی دوازده, از 6۱ ت٩2‏ - بطلمیوی سیزدهم از4ع ا 44 - بطلمیوی چپاردهم
MON >> و کتان و پشم» جامه» منسوج؛ قماش. کمی» اند کی. باردان فرهنگ فارسی معین ۳۱۳ پاردان: 0 (امر.) جوال. تنگ» ظرف ماه. روزهای پارسی: سی روز ماه شمسی شراب. شراب. اپرانیان: «هر مزد» بهمن» اردیبهشت» شهریور پاردم: 0 ([ - پاره‌دم ] (امر.) چرمی
MON >> ارسی: سی روز ماه شمسی شراب. شراب. اپرانیان: «هر مزد» بهمن» اردیبهشت» شهریور پاردم: 0 ([ - پاره‌دم ] (امر.) چرمی که بر زین يا پالان می‌دوزند و زير دم اسب یا پس ران چاربا می‌انداز ند؛ رانکی» قشقون. پارس: صق (اخ.) نامی قومی ایرانی ساکن
MON >> دو ستون ِِِ یکدیگر گردد. (عم.) (دامپروری) پیما ی اسر ۳ مدت معینی به او می‌سپارد. برحسب چنین پیمانی محصول و نتاج حیوانات مزبور بین طرفین تقسیم می‌شود. ترازنامه: (0-)202-.۱ (امر.) سیاهه‌ای که موّسسات در پایان سال نوبسند و دارایی و
MON >> برند (خصوصا). سپار: ۲ (.) آهنی سرتیز که زمین را بدان شیار کنند؛ آهن جفت. سپاردن: ۵02۲-8 [- سیردن] (مص‌ل.) (سبارد» سیازد» خواهد سیارد» سیار» سیرانده» سبارده» سپارض). سپارش: ۰057۰4: (- سپاردن] (اسص.) سپردن کسی رابه کسی برای اهتمام
MON >> سبارد» سیازد» خواهد سیارد» سیار» سیرانده» سبارده» سپارض). سپارش: ۰057۰4: (- سپاردن] (اسص.) سپردن کسی رابه کسی برای اهتمام و تیمار؛ سفارش؛ توصیه. سپاروک: *۳570:: [- سباروک)] (.) سپاأس: 5 (.) حمد» ستاش. شک نعمت. لطف» شفقت سپاه: ۵۲2
```


## [2026-09-14T01:04:05.480Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پارس' in p and ('پلنگ' in p or 'یوز' in p):\n        for line in p.split('\\n'):\n            if 'پارس' in line or 'پلنگ' in line or 'یوز' in line:\n                print('leaf',i,'~p',i-215,line.strip()[:150])\n        print()\nEOF"
}
```


### [2026-09-14T01:04:06.779Z] TOOL RESULT

```
leaf 39 ~p -176 الف کلمة پارسيك (-پارسی) درزبان پیلوی بزبانی اطلاق شده
leaf 39 ~p -176 بنا بمفاد این‌عبارت پارسيك بزبانی اطلاق میشده که گوجی هیندوك
leaf 39 ~p -176 « گوزهندی» است. بپمین مناسبت برخی از محققان معاصر «پارسيك» را
leaf 39 ~p -176 « بر تخت نشستن‌شیرویه واندرز کردن وفرستادن‌سران‌نزد بدرپندویوزش»

leaf 509 ~p 294 ۱ - نام بنداد 2880044 که امیوزه عرب آنرا اغل 191180080 تلفظ کند بی خكه
leaf 509 ~p 294 در پارسیٌ باستان بمعنی خدا و دادار وآفرید کار است . در اوستا اين کلمه چند بار مرادف خدا
```


## [2026-09-14T01:04:11.707Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B1%D8%AF/",
 "prompt": "Does any Persian dictionary (Dehkhoda, Moein, Amid) list پارد as a word meaning panther/leopard? Quote what the entry says. Also say if the page is empty/not found."
}
```


### [2026-09-14T01:04:17.395Z] TOOL RESULT

```
Based on the content provided, the Persian dictionaries listed do **not** define پارد as meaning panther or leopard.

According to the page, the Dehkhoda dictionary entry states: "پارد. ( اِخ ) بلوکی از توابع قزوین" (a village in Qazvin's dependencies) and "پارد. ( ص ) زن پیر" (an old woman, according to some sources).

The Farsi dictionary section simply lists: "بلوکی از توابع قزوین زن پیر" (a village and/or old woman).

A user suggestion mentions that "pard" appears in Ahmad Kasravi's lexicon relating to "چم ماده و ماتریال" (material/substance), but this is not from the major dictionaries requested, and the reference is incomplete.

The page is fully loaded with content; it is not empty or not found.
```


## [2026-09-14T01:05:25.279Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B9%D9%81%D8%B1%DB%8C%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Moein) entry for عفریت, including the bracketed origin tag (e.g. [ع.]) and the meaning; also quote briefly what Dehkhoda says about عفریت and عفریته."
}
```


### [2026-09-14T01:05:30.263Z] TOOL RESULT

```
# Moein Dictionary Entry

According to Farhang-e Moein, the entry for عفریت reads:

"(عِ) [ع.] (اِ.) موجودِ زشت و ترسناک، دیو، غول. ج. عفاریت."

This translates to a foul and fearsome creature, demon, or ghoul, with the plural form عفاریت.

# Dehkhoda Dictionary Notes

Dehkhoda provides two distinct entries. The first describes عفریت as "a wicked, vile person." The second entry offers more extensive commentary, noting that عفریت can mean a powerful lion, and referencing the phrase "عفریت نفریت" (tyrant and oppressor). Dehkhoda also mentions عفریته as a variant form, with grammatical discussion of how the final letter changes depending on pronunciation.
```


## [2026-09-14T01:05:36.410Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B9%D9%81%D8%B1%DB%8C%D8%AA/\" --note \"page 407 root Pri node 4: Moein/Dehkhoda entry for عفریت\" 2>&1 | tail -1; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B1%D8%AF/\" --note \"page 407 root Prs node 7: Dehkhoda/Moein have no پارد 'panther'\" 2>&1 | tail -1; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg407.png data/verification/sources/refs/ocr/BOOK/407.png && echo copied"
}
```


### [2026-09-14T01:05:40.405Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e625a4386a8f7c7c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/395c5f18204c3e47.txt
copied
```


## [2026-09-14T01:05:43.018Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-14T01:05:43.068Z] TOOL RESULT

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


## [2026-09-14T01:13:03.210Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-407.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Prî\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *preyH- (Pokorny *prāi- : *prəi- : *prī-) 'to please, to love, be well-disposed'\",\n  \"note\": \"Pokorny I 844 has exactly this root, 'prāi-, prəi-, prī- : to like, feel well-disposed, friendly', with the Avestan (fray-, frīta-, frīna-, friti- 'prayer', frya- 'dear') and Germanic (Goth. freis, frijōn, frijōnds, ON Frigg) material Nourai draws. Watkins/AHD gives 'prī-. To love' and Wiktionary reconstructs *preyH- 'to please; to love'. The language label (Indo-European) and the form are right; of the gloss, 'to love' is the PIE meaning, while 'praise' is specifically the Indo-Iranian development of the compound *ā-frī- 'to bless, praise' and not a PIE sense — a venial imprecision, so the root box counts as confirmed.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *preyH- (نزد پوکورنی *prāi-/*prī-) به معنی «دوست داشتن، خشنود کردن، مهر ورزیدن» است؛ پوکورنی در صفحهٔ ۸۴۴ همین ریشه را با شاهدهای اوستایی (frī-، frīta-، frya-) و ژرمنی (گوتی frijōn، frijōnds) آورده و واتکینز نیز آن را prī- «دوست داشتن» ضبط کرده است. برچسب زبانی و صورت ریشه درست است؛ تنها باید توجه داشت که معنی «ستایش، آفرین» ویژهٔ ترکیب هندوایرانی *ā-frī- است و معنی آغازین هندواروپایی نیست. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n  \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/preyH-\",\n    \"https://www.ahdictionary.com/word/search.html?q=afreet\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:844\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt 'Root / lemma: prai- prai-, prī- (pri-) / Meaning: to like, feel well-disposed, friendly ... Avestan fray- \\\"satisfy\\\", participle frita-, frīna-, friti- \\\"prayer\\\", frya- \\\"dear, worth\\\" ... References: WP. II 86 f. ... Page(s): 844' — the page number and the root are exactly Nourai's.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 86-87\", \"stance\": \"supports\",\n     \"note\": \"WLD_Bd2_pages.txt leaf 90 (running head '86 pra'): cross-reference 'Ai. ā-prayu-, gr. πρᾱΰς, s. u. prāi- \\\"gern haben, schonen\\\"'; leaf 91 (p. 87) carries the material 'priyatvam ... (: got. frijaþwa f. \\\"Liebe\\\")'. Pokorny's own reference WP. II 86 f. checks out.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. prī-\", \"stance\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt: 'prī-. To love. Contracted from *priə-. 1. Suffixed form *priy-o- in Germanic *frijaz ... Old English frēo, free: FREE ... 2. *priy-ont- ... Germanic *frijand- ... FRIEND ... 4. *priy-ā- ... Germanic *frijjō ... FRIGG; *frije-dagaz ... FRIDAY. [Pok. prāi- 844.]'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/preyH-\", \"stance\": \"supports\",\n     \"note\": \"'*preyH- : to please, to love'; descendants include PIIr. *prináHti, Skt. prī́yate, Proto-Iranian *friHmā́ (Oss. limæn 'friend'), Pashto wrin.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"âfritan; â-frî-nami\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Av. ā-frīnāmi 'I bless, I praise' is genuine and is exactly the nasal present of the Avestan verb frī- (Bartholomae's headword 'frāy- V. \\\"befriedigen\\\", Praes. frīnā-, PPfP. frīta-, frīθa-, frīna-, Inf. frīnē'), from PIE *preyH- with the preverb ā- 'to, towards': *ā-prī-né-h₂-mi > OIr. *ā-frī-nā-mi. The second form in the box, âfritan, is NOT Avestan: -tan is the Middle Persian infinitive ending, and Horn (Grundriss no. 39, p. 10) lists it under 'phlv. āfrītan \\\"schaffen\\\"' beside 'aw. āfrīnāmi \\\"ich preise\\\"'; MacKenzie p. 5 has MP āfrīdan/āfritan ['plytn'] 'praise, bless; create' and Nyberg II 'āfrītak \\\"(heavenly) created\\\" ... generally regarded as identical with Av. ā-frāy-, pres. ā-frīnā-'. Avestan itself has only the participle ā-frīta- and the noun āfrīti- 'blessing'. So the derivation is right but the node mislabels a Middle Persian infinitive as Avestan; and the sense 'to create' is, as Horn says expressly, one that 'does not go back beyond Pahlavi'.\",\n  \"derivation_fa\": \"صورت اوستایی درست āfrīnāmi «می‌ستایم، آفرین می‌گویم» است؛ ستاک آن همان فعل اوستایی frī- (بارتولمه: frāy- «خشنود کردن»، حال frīnā-، اسم مفعول frīta-/frīna-) است که با پیشوند ā- ساخته شده، و بازماندهٔ ریشهٔ هندواروپایی *preyH- است. اما صورت دیگرِ این خانه، āfrītan، اوستایی نیست: پایانهٔ -tan نشانهٔ مصدر فارسی میانه است و هرن (بند ۳۹، ص ۱۰) و مکنزی (ص ۵) و نیبرگ آن را صریحاً پهلوی می‌دانند. افزون بر این، معنی «آفریدن/خلق کردن» به گفتهٔ هرن از پهلوی فراتر نمی‌رود و در اوستایی تنها معنی «ستودن، دعای نیک کردن» هست. پس پیوند ریشه‌شناختی درست است ولی برچسب زبانیِ یکی از دو واژه خطاست.\",\n  \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D8%AF%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:844\", \"status\": \"supports\",\n     \"note\": \"Pokorny p. 844: 'Avestan fray- \\\"satisfy\\\", e.g. frīnāmi, participle frita-, frīna-, friti- \\\"prayer\\\", frya- \\\"dear\\\"' — the Avestan verb is there, though Pokorny cites frīnāmi (without preverb) and has no *āfritan.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.v. frāy- (BRT.txt line 18195)\", \"stance\": \"supports\",\n     \"note\": \"'j., g. frāy- V. \\\"befriedigen\\\". Praes. frīnā-, ... PPfP. frita-, friθa- (sbes.), frīna-; Inf. frīnē.'; and s.v. darəγō.jitay- (line 12891) the quotation 'āfrīnāmi tava nara ... \\\"ich segne dich, o ..., mit gutem Leben\\\"' (Az. 7) — Avestan ā-frīnāmi is real and means 'I bless'.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 39, p. 10\", \"stance\": \"partial\",\n     \"note\": \"'39. āfrīden \\\"schaffen\\\", Praes. āfrīn-em, āfrīdegār; āfrīn 1) \\\"schaffend\\\" 2) \\\"Lob\\\", vergl. nefrīn \\\"Fluch\\\". aw. āfrīnāmi \\\"ich preise\\\", āfrīna- \\\"Segen\\\"; phlv. āfrītan \\\"schaffen\\\", āfrīn \\\"Lob\\\", nafrīn \\\"Fluch\\\"; ai. ā + √prī- \\\"befriedigen\\\". Die Bedeutung \\\"schaffen\\\" geht nicht über das Pehlevī hinaus.' — Horn assigns āfrītan to Pahlavi, not Avestan.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. āfrīn / āfrītak\", \"stance\": \"partial\",\n     \"note\": \"'āfrīn [inscr., Ps. ʾplyny; ʾpryn\\\\'] benediction, praise, blessing ... Av. (331) āfrivana-; MPrth ʾfrywn; MPrs ʾfryn ...'; 'āfrītak [ʾplytk\\\\'] (heavenly) created ... generally regarded as identical with Av. (1017) ā-frāy-, pres. ā-frīnā-' — again the -t- forms are Middle Iranian.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"âfarîn «آفرین»; âfarîdan «آفریدن»; nefrîn «نفرین»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP آفرین āfarīn 'praise, blessing' < MP āfrīn ['pryn', Manichaean ʾpryn] 'praise, blessing' < OIr. *ā-frī-na- (Av. ā-frī-nā-mi); NP آفریدن āfarīdan 'to create' < MP āfrīdan/āfritan ['plytn'], present āfrīn-/āfur- 'praise, bless; create' (MacKenzie p. 5: 'āfrīdan, āfrīn-/āfur- ... N āfarīdan, āfarīn-'). The anaptyctic -a- of āfarīn/āfarīdan is the regular New Persian resolution of the MP cluster ā-fr- (cf. MP frazand > NP farzand). نفرین nifrīn/nafrīn 'curse' is the same stem with the negative-privative preverb ni- (MacKenzie: 'nifrīn [nplyn'] curse'; Nyberg: 'nifrīn ... ni + Av. frāy-, opp. āfrīn'), i.e. 'to un-bless'. آفریدگار āfarīdegār 'creator' = MP āfrīdagār. The semantic move 'bless, praise' > 'create' happened inside Middle Persian, in the religious language where the gods' blessing IS the act of creation.\",\n  \"derivation_fa\": \"«آفرین» از فارسی میانهٔ āfrīn «ستایش، دعای نیک» و آن از ایرانی باستان *ā-frī-na- (اوستایی ā-frīnā-mi)؛ «آفریدن» از مصدر پهلوی āfrītan/āfrīdan با ستاک حال āfrīn-/āfur- «ستودن، برکت دادن؛ آفریدن» (مکنزی ص ۵). واکهٔ میانجی «ـَ» در آفَرین و آفَریدن همان شکستِ خوشهٔ آغازینِ fr در فارسی نو است (مانند فرزند < frazand). «نفرین» همان ستاک با پیشوند منفی‌سازِ ni- است (نیبرگ: nifrīn در برابر āfrīn) یعنی «دعای بد». «آفریدگار» = پهلوی āfrīdagār. تحول معنایی «ستایش/برکت» به «آفرینش» در دورهٔ فارسی میانه و در زبان دینی رخ داده است؛ ادعای نورایی درست است و حاشیهٔ معین بر برهان قاطع (ص ۵۱) نیز همین را می‌گوید.\",\n  \"sources\": [W + \"%D8%A2%D9%81%D8%B1%DB%8C%D8%AF%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:51\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 261 (= printed p. 51; Aryanpur independently cites 'برهان قاطع : ۴۱۶' for پلنگ, confirming this offset scheme). Mo'in's footnotes on that page: under آفرین '... اوستا āfrī... بارتولمه ۳۳۱، پهلوی āfrīn «تبرکت» ... مرکب از ā + frī ... مقابل نفرین (ni + frīn) بمعنی لعنت'; and 'آفریدگار - پهلوی āfrīdagār ... خالق، آفریننده'; 'آفریدن - پهلوی āfrītan ... از مصدر اوستائی frī بمعنی دعا و نیایش؛ در سانسکریت prī (بارتولمه)'; 'آفریده - پهلوی āfrīdag، مخلوق' — exactly the arrow Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 5\", \"stance\": \"supports\",\n     \"note\": \"'āfrīdan, āfrīn-/āfur- [\\\\'plytn\\\\', \\\\'plyn-, \\\\'pwl- | M ʾp(w)ryd, ʾpwr-, P ʾfryn-, N āfarīdan, āfarīn-] praise, bless; create.  āfrīn [\\\\'pryn\\\\' | M ʾpryn, N āfarīn] praise, blessing.  āfurīdan, āfur- create.  nifrīn [nplyn\\\\' | N ~] curse.'\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol. Adena condensation) s.vv. آفریدن، آفرین، آفریدگار\", \"stance\": \"supports\",\n     \"note\": \"'آفریدن: āfarīdan (مصم.) خلق کردن، از نیستی هست کردن ...'; 'آفریده: āfarīda مخلوق'; 'آفریدگار: خالق، آنکه خلق کند'; 'آفرین: تحسین، ستایش، مدح' — the two senses stand side by side in Mo'in as in the chart.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 39, p. 10\", \"stance\": \"supports\",\n     \"note\": \"'āfrīden \\\"schaffen\\\", Praes. āfrīn-em, āfrīdegār; āfrīn 1) \\\"schaffend\\\" 2) \\\"Lob\\\", vergl. nefrīn \\\"Fluch\\\"' — Horn's New Persian headword covers all three words of this node.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Arabic\", \"words\": \"ifrît\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic عفريت ʿifrīt 'demon' (Qur'an 27:39 ʿifrītun mina l-jinni) is derived by AHD and by Asbaghi from the Middle Persian past participle āfrīd 'created' — originally elliptic *dēw āfrīd 'a demon('s) creation', with the Arabic نسبة-like -īt reshaping and the initial ʿayn supplied to give the loan an Arabic-looking triliteral shape (ʿ-f-r), which then attracted it to the native root ʿafar 'dust, ashes' (whence ʿifr 'wicked, cunning'). AHD s.v. afreet: 'Arabic ʿifrīt, from Middle Persian āfrīd, created ..., from āfrīdan, to bless, create, from Old Iranian *āfrī-, to bless (attested in Avestan āfrī-) ... see prī-'. The chart's own NOTE (RCH:lxxvii from Arabic 'A.f.r') records the rival native-Arabic derivation; Wiktionary gives both and decides for neither, so the node is 'plausible' rather than 'confirmed': the Iranian etymology is the one adopted by AHD and Asbaghi, but the ʿ-f-r derivation (type عَكْرُوت ʿakrūt) is still defended.\",\n  \"derivation_fa\": \"واژهٔ عربی «عفریت» (قرآن، نمل ۳۹) را فرهنگ AHD و آسبقی (اسبغی) وام‌واژه‌ای از فارسی میانه می‌دانند: از صفت مفعولی āfrīd «آفریده»، در اصل کوتاه‌شدهٔ *dēw āfrīd «آفریدهٔ دیو»؛ عینِ آغازی برای عربی‌نمودن واژه و جا دادن آن در ریشهٔ سه‌حرفی ع‌ف‌ر افزوده شده و همین سبب شده که واژه‌شناسان عرب آن را با «عَفَر» (خاک) پیوند دهند. دیدگاه رقیب، که یادداشت خود کتاب هم از ریچاردسون نقل می‌کند، آن را برساختهٔ همان ریشهٔ عربی ع‌ف‌ر می‌شمارد و ویکی‌واژه هر دو را می‌آورد. بنابراین ادعای نورایی با احتیاط پذیرفتنی است (معرّبِ ایرانی، نه عربیِ اصیل).\",\n  \"sources\": [\n    \"https://www.ahdictionary.com/word/search.html?q=afreet\",\n    W + \"%D8%B9%D9%81%D8%B1%D9%8A%D8%AA\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"AHD:23\", \"status\": \"supports\",\n     \"note\": \"AHD main dictionary s.v. afreet (p. 23 of the New College Edition; checked in the current online AHD, same etymology): '[Arabic ʿifrīt, from Middle Persian āfrīd, created (an afreet probably being so called because it is a \\\"creature\\\", a creation of God or divine powers), from āfrīdan, to bless, create, from Old Iranian *āfrī-, to bless (attested in Avestan āfrī-) : *ā- + *frī-, to rejoice, please; see prī- in the Appendix.]' — literally Nourai's arrow.\"},\n    {\"ref\": \"PLA:203\", \"status\": \"supports\",\n     \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, PLA_pages.txt leaf 218 = printed p. 203: 'ʿifrīt: \\\"Dämon\\\" pers. آفرید āfarīd v. āfarīdan \\\"schaffen\\\", mp. ʾplytn āfrītan, av. ā-frāy-'; the same page also has 'ʿifrīn: \\\"mächtig\\\" s. ʿifrīt u. pers. āfarīdan'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"searched KLN_1966.txt for afreet/afrit/ifrit\", \"stance\": \"silent\",\n     \"note\": \"grep for '^afreet' / 'ifrit' in KLN_1966.txt returns nothing usable (the word is not a Klein headword in the scanned text).\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'ifrit|afrit' FVQ.txt gives no hit; Jeffery does not treat ʿifrīt among the foreign words of the Qur'an, i.e. he did not accept it as a loan.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"عفريت (Arabic)\", \"stance\": \"partial\",\n     \"note\": \"'From a Middle Iranian past participle āfrīd (\\\"created\\\"), originally an elliptic expression for *dīw afrīt (\\\"demon's creation\\\")' — alternatively 'from the root ع ف ر related to \\\"ash\\\", compare عَكْرُوت (ʕakrūt)'. Both views given.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"efrît «عفریت»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian عفریت ʿefrīt 'demon, ogre' is the Arabic ʿifrīt taken back into Persian — a round trip: MP āfrīd > Arabic ʿifrīt > NP ʿefrīt, with the Arabic spelling (ʿayn, ت) and the Arabic broken plural عفاریت ʿafārīt; the feminine عفریته ʿefrīta 'shrew, she-demon' follows the Arabic feminine in -a. Mo'in tags it '[ع.]' i.e. Arabic: '(عِ) [ع.] (اِ.) موجودِ زشت و ترسناک، دیو، غول. ج. عفاریت.' The word is therefore a doublet of native آفریده āfarīda, borrowed back in an unrecognizable Arabic dress.\",\n  \"derivation_fa\": \"«عفریت» در فارسی نو وام‌واژه‌ای از عربی است؛ یعنی واژه‌ای که خاستگاه ایرانی داشته (پهلوی āfrīd)، در عربی به صورت «عفریت» معرّب شده و سپس با املای عربی (عین و تای کشیده) و جمع مکسر «عفاریت» به فارسی بازگشته است — نمونهٔ روشنِ وام‌گیریِ رفت‌وبرگشتی. صورت مؤنث «عفریته» نیز بر وزن عربی است. معین آن را با نشانهٔ [ع.] «موجود زشت و ترسناک، دیو، غول» آورده است. پس «عفریت» دوگانهٔ (doublet) واژهٔ بومی «آفریده» است و ادعای نورایی درست است.\",\n  \"sources\": [\"https://abadis.ir/fatofa/%D8%B9%D9%81%D8%B1%DB%8C%D8%AA/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"partial\",\n     \"note\": \"no page is given by Nourai and the 6-vol. Farhang-e Farsi is not online; Mo'in's entry read via abadis.ir: '(عِ) [ع.] (اِ.) موجودِ زشت و ترسناک، دیو، غول. ج. عفاریت' — it confirms the word and its Arabic origin tag, but Mo'in gives no further etymology, so the ultimate Iranian source is not asserted there.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"vajehyab/abadis, فرهنگ معین s.v. عفریت\", \"stance\": \"supports\",\n     \"note\": \"'[ع.] (اِ.) موجودِ زشت و ترسناک، دیو، غول. ج. عفاریت' — Arabic-loan tag.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (vols 3-5 cover ع)\", \"stance\": \"silent\",\n     \"note\": \"not cited by Nourai for this node and not checked page by page; Dehkhoda (via abadis) has عفریت 'مردم بدذات و پلید' and عفریته as the feminine, with no etymology.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p. 203\", \"stance\": \"supports\",\n     \"note\": \"Asbaghi treats ʿifrīt as a Persian loanword in Arabic, which presupposes exactly the Persian→Arabic→Persian route of this node.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"`pryn; `prytyy; `fryn, `frywn\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Gharib's Sogdian dictionary has all four forms in the same early block of entries: '20 ʾpryn- B, S āfrīn ©<*ā-frīna- (to) praise', '22 ʾprytʾk S āfrīte ©pp. = ʾfryty praised', '24 ʾprywn B āfriwan (ʾprywnh) blessing, praise', '674 ʾfrywn M, C āfriwan'. The Buddhist/Christian ʾp- and Manichaean ʾf- spellings are the same word, Sogdian /β/ written p or f; the abstract in -wn continues OIr. *-ϑwan- (cf. Parthian ʾfrywn, MP āfrīwan). All of them go back to OIr. *ā-frī-na- exactly as the Persian branch does, so the arrow root→Sogdian is right. The one slip is the gloss: Nourai renders ʾprytyy 'created', but Gharib glosses the past participle 'praised' — Sogdian did not develop the Persian 'create' sense.\",\n  \"derivation_fa\": \"در فرهنگ سغدیِ بدرالزمان قریب هر چهار صورت آمده است: «۲۰ ʾpryn- āfrīn < *ā-frīna- ستودن»، «۲۲ ʾprytʾk āfrīte ستوده»، «۲۴ ʾprywn āfriwan ستایش، برکت» و «۶۷۴ ʾfrywn». نوشتن p و f هر دو نشانهٔ واج /β/ سغدی است و پسوند -wn دنبالهٔ ایرانی باستان *-ϑwan- است (سنجیدنی با پارتی ʾfrywn و فارسی میانهٔ āfrīwan). بنابراین پیوند این خانه با ریشه درست است؛ تنها خطا در معناست: نورایی ʾprytyy را «آفریده» معنی کرده، حال آنکه قریب آن را «ستوده» آورده است و معنی «آفریدن» در سغدی پدید نیامده است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:3\", \"status\": \"supports\",\n     \"note\": \"SOD_pages.txt leaf 67 (printed p. ~1-3, entries 20-27): '20 ʾpryn- B, S  afrin ©<*ā-frīna- =»ʾfryn-, ʾpryn-  (to)praise  TSP 25ii...', '22 ʾprytʾk S  afrite (ʾpryty) ©pp. =ʾfryty  praised', '24 ʾprywn B  afriwan (ʾprywnh)  blessing, praise', and (line 11857) '674 ʾfrywn M, C  afriwan'. Nourai's page number points at the right block; only his gloss 'created' for ʾprytyy disagrees with Gharib's 'praised'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib entries 20, 21, 22, 24, 674\", \"stance\": \"partial\",\n     \"note\": \"forms confirmed; gloss of ʾpryty/ʾprytʾk is 'praised' (āfrīte), not 'created'.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. āfrītak\", \"stance\": \"supports\",\n     \"note\": \"Nyberg expressly cross-refers the Middle Iranian material to 'Sogd. 1774', i.e. the same Sogdian ʾfry- family, under Av. ā-frāy-, pres. ā-frīnā-.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p. 5\", \"stance\": \"supports\",\n     \"note\": \"the Manichaean Middle Persian form 'M ʾpryn' quoted by MacKenzie is the direct counterpart of Sogd. ʾpryn-.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Germanic\", \"words\": \"fri\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *frijaz 'beloved, belonging to the loved ones, hence not in bondage, free' < PIE *priy-o-, with the cognate verb *frijōnan 'to love' (Goth. frijōn) and the participle *frijōnd- 'friend'. Watkins: 'prī-. To love. 1. Suffixed form *priy-o- in Germanic *frijaz ... 2. Suffixed (participial) form *priy-ont- ... in Germanic *frijand-, lover, friend ... 3. *pri-tu- in Germanic *frithuz, peace ... 4. *priy-ā- in Germanic *frijjō, beloved, wife ... Frigg'. Pokorny p. 844 has the same list (Goth. freis, OHG/OS frī, OE frēo; Goth. frijōn, ON frjā, OE frēogan; Goth. frijōnds, OE frēond; OHG fridu 'peace'). Nourai's gloss 'friend, free, good' is a compressed but accurate label for that cluster (the 'good/peace' side being *frithuz).\",\n  \"derivation_fa\": \"ژرمنی آغازین *frijaz «دوست‌داشته، از آنِ خویشان و دوستان، و از این رو آزاد» بازماندهٔ *priy-o- هندواروپایی است؛ فعل هم‌ریشهٔ *frijōnan «دوست داشتن» (گوتی frijōn) و اسم فاعل *frijōnd- «دوست» نیز از همین ستاک‌اند و *friþuz «صلح، آشتی» صورت *pri-tu- است. واتکینز و پوکورنی (ص ۸۴۴) هر دو همین فهرست را می‌آورند. معنی‌ای که نورایی داده («دوست، آزاد، نیک») فشردهٔ درستِ همین خوشه است؛ ادعای او درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/preyH-\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. prī- (AHD_watkins1985.txt): '*priy-o- in Germanic *frijaz, beloved, belonging to the loved ones, not in bondage, free ... *priy-ont-, loving, in Germanic *frijand-, lover, friend ... [Pok. prāi- 844.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 844\", \"stance\": \"supports\",\n     \"note\": \"'cymr. rhydd \\\"free\\\" = Gothic freis (akk. frijana), Old High German Old Saxon frī, Old English frēo ...; Gothic frijōn \\\"love\\\" ... participle Gothic frijōnds \\\"friend\\\" ... Old High German fridu \\\"peace, protection\\\"'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 86-87\", \"stance\": \"supports\",\n     \"note\": \"leaf 91 (p. 87) of WLD_Bd2_pages.txt has the Germanic block ('got. frijaþwa f. \\\"Liebe\\\"', 'ags. frēod \\\"Liebe\\\"') under prāi-.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. Friday, free, friend\", \"stance\": \"supports\",\n     \"note\": \"'Friday ... fr. OE. frīgedæg, lit. \\\"the day of the goddess Frig\\\" ... a loan translation of L. Veneris dies' (KLN_1966.txt line 15405).\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"free, fresh, friend, Friday\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Three of the four are right and one is not. FREE < OE frēo < PGmc *frijaz < *priy-o-; FRIEND < OE frēond, the present participle of OE frēogan 'to love' < PGmc *frijōnd- < *priy-ont-; FRIDAY < OE frīgedæg 'day of Frigg' (PGmc *frijjō 'beloved, wife'), a calque of Latin Veneris diēs which is itself a calque of Greek Aphrodītēs hēmera — all three are given under prī- by Watkins and under prāi- by Pokorny. FRESH, however, does NOT belong here: OE fersc 'unsalted' (metathesized to fresh under influence of OF fres/fresche, itself from the same Germanic word) goes back to PGmc *friskaz, cognate with OCS prěsьnъ 'fresh' and Lith. prėskas 'sweet, unleavened' (Klein s.v. fresh; Etymonline s.v. fresh) — a different root (*preysk-), unconnected with *preyH-.\",\n  \"derivation_fa\": \"سه واژه از چهار واژهٔ این خانه درست‌اند: free از انگلیسی کهن frēo، friend از frēond (اسم فاعل فعل frēogan «دوست داشتن») و Friday از frīgedæg «روز فریگ»، که ترجمهٔ قرضی لاتینی Veneris dies است؛ هر سه را واتکینز و پوکورنی زیر همین ریشه آورده‌اند. اما fresh به این ریشه ربطی ندارد: انگلیسی کهن fersc «بی‌نمک» از ژرمنی *friskaz است و هم‌ریشه با اسلاوی کهن prěsьnъ و لیتوانیایی prėskas، یعنی ریشه‌ای دیگر (*preysk-). کلاین و اتیمآنلاین هر دو همین را می‌گویند. پس این بخش از ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n  \"sources\": [\"https://www.etymonline.com/word/fresh\", \"https://www.etymonline.com/word/friend\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"the node carries no reference of its own in the book; it inherits AHD from the Germanic parent, and Watkins s.v. prī- lists FREE, FRIEND and FRIDAY but not FRESH.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.vv. fresh, Friday\", \"stance\": \"contradicts\",\n     \"note\": \"'fresh, adj., newly made ... fr. Teut. *frisk- ... These Teut. words are prob. cogn. with OSlav. prěsьnъ (for *praiskino-), \\\"fresh\\\" (whence Lith. prėskas)' — a separate root; 'Friday ... fr. OE. frīgedæg ... the day of the goddess Frig' supports the other three.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. prī-\", \"stance\": \"partial\",\n     \"note\": \"FREE, FRIEND, FRIDAY (and FRIGG, AFFRAY, SIEGFRIED) are listed; FRESH is not.\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.vv. fresh, friend\", \"stance\": \"contradicts\",\n     \"note\": \"fresh: 'from Proto-Germanic *friskaz ... probably cognate with Old Church Slavonic presinu \\\"fresh\\\", Lithuanian preskas \\\"sweet\\\"'; friend: 'from Proto-Germanic *frijōjands \\\"lover, friend\\\" ... from PIE *priy-ont-, present-participle form of root *pri- \\\"to love\\\"'.\"}\n  ]\n }\n]\n\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Prs\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *pers- 'to sprinkle, spray; (be)speckled' (Pokorny 823; Mann's *prs-)\",\n  \"note\": \"Both cited references check out literally. Pokorny I 823: 'Root/lemma: pers- ... Meaning: to drizzle, sprinkle; dust, ashes', with Skt. pṛṣat 'drip', pṛṣant-/pṛṣatī 'dappled, spotted', Av. paršuya- 'of water', Toch. pärs-, Hitt. pappars- 'sprinkle'. Mann col. 1003 (= IEC:1003) has the headword in Nourai's very wording: 'prs- \\\"speck, spot, mark, dapple, sprinkle, spray, dot, rash\\\"'. Walde-Pokorny II 50 has 'pers- \\\"sprühen, stieben, spritzen (bespritzt = gesprenkelt)\\\"' and WP II 46 spells out the semantic bridge: 'gesprenkelt' develops out of 'spritzen, sprühen'. Cheung (Iranian Verb, p. 298) sets up Proto-Iranian *parš 'to sprinkle, strew' < PIE *pers-, LIV 788 f. The root box is therefore right in form, label and gloss; the questionable part of the chart is only the 'Medit' leopard branch (see node #5).\",\n  \"note_fa\": \"ریشهٔ هندواروپایی *pers- «پاشیدن، افشاندن؛ خال‌خال شدن» است. پوکورنی (ص ۸۲۳) آن را با شاهدهای سنسکریت pṛṣat «قطره»، pṛṣant- «خال‌دار»، اوستایی paršuya- «آبی»، هیتی pappars- «پاشیدن» آورده و مان (ستون ۱۰۰۳) دقیقاً با همان تعریفی که نورایی نقل کرده ثبتش کرده است: prs- «خال، لکه، نقطه، پاشیدن». والده-پوکورنی (ج ۲ ص ۵۰) نیز pers- «افشاندن، پاشیدن (پاشیده‌شده = خال‌خال)» دارد و در ص ۴۶ توضیح می‌دهد که معنی «خال‌دار» از «پاشیدن» پدید آمده است؛ چونگ هم ایرانیِ آغازین *parš «پاشیدن» را به همین ریشه می‌برد. پس ریشه و معنای آن درست است و تنها شاخهٔ «مدیترانه‌ای» (خانهٔ ۵) جای چون‌وچرا دارد.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"POK:823\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: pers- / Meaning: to drizzle, sprinkle; dust, ashes / Material: Old Indic pṛṣat, pṛṣata-m \\\"drip\\\"; pṛṣant-, f. pṛṣatī \\\"dappled, dotted, spotted\\\" ... Avestan paršuya- \\\"of water\\\" ... Tocharian A B pärs- \\\"sprinkle\\\" ... Hittite pappars- \\\"sprinkle\\\". References: WP. II 50 ... Page(s): 823'.\"},\n    {\"ref\": \"IEC:1003\", \"status\": \"supports\",\n     \"note\": \"Mann, IEC.txt leaf 556 (column numbers 1002/1003 printed in the leaf): 'prs- \\\"speck, spot, mark, dapple, sprinkle, spray, dot, rash\\\". Cf. prsk-, (prks), prK-, prKs-' — Nourai's gloss is copied from here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 46 and 50\", \"stance\": \"supports\",\n     \"note\": \"p. 50 headword 'pers- \\\"sprühen, stieben, spritzen (bespritzt = gesprenkelt)\\\"'; p. 46 'ai. pṛṣant- \\\"gesprenkelt, bunt\\\", pṛṣatī \\\"scheckige Kuh, gefleckte Antilope\\\", pṛṣatá-m \\\"Tropfen\\\", cech. pršeti \\\"sprühen, stieben, regnen\\\" ... weisen auf Entw. der Bed. \\\"gesprenkelt\\\" aus \\\"spritzen, sprühen\\\"'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb p. 298\", \"stance\": \"supports\",\n     \"note\": \"'*parš \\\"to sprinkle, strew\\\" ... «PIE *pers- \\\"to spray, sprinkle\\\" = LIV: 788 f. | Pok.: 823'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n     \"note\": \"grep of AHD_watkins1985.txt finds no 'pers-' root entry for 'sprinkle' (the root has no English derivative, so Watkins omits it) — consistent with Nourai citing only POK and IEC here.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pareš; paršuya\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Av. paršuya- 'of water, (perhaps) snow-water' is real and is exactly where Pokorny p. 823 puts it, a -uya- derivative of the root *parš- 'to sprinkle'; Cheung adds the well-attested Young Avestan personal name parṣat.gauu- 'having a speckled cow' (Yt 13.96, 13.127) as the Avestan witness of the root. The bare verb 'pareš : drip' is taken over from Mann col. 1003 ('Av. cf. parəš-, v. (e- or o-grade) \\\"drip\\\"'), but Mann's form is a normalized citation form, not an attested Avestan verb: Bartholomae has no verb parəš-, and a grep of BRT.txt for paršuya likewise fails (the Avestan lemma is there but the OCR of the Latin-script Avestan is defective). Hence 'plausible': the root is Avestan, the second word is attested, the first is a scholar's reconstruction quoted as if it were a text form.\",\n  \"derivation_fa\": \"صورت اوستایی paršuya- «آبی، (شاید) آبِ برف» واقعی است و پوکورنی (ص ۸۲۳) آن را زیر همین ریشه آورده؛ ساخت آن مشتقی با پسوند -uya- از ستاک *parš- «پاشیدن» است. چونگ نیز نام خاص اوستایی نو parṣat.gauu- «دارندهٔ گاو خال‌دار» (یشت ۱۳) را گواه این ریشه در اوستایی می‌داند. اما فعل «pareš = چکیدن» را نورایی از مان (ستون ۱۰۰۳) گرفته است و آن صورتی است که مان خود بازسازی کرده، نه فعلی که در متن اوستا آمده باشد؛ در فرهنگ بارتولمه چنین فعلی نیست. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"POK:823\", \"status\": \"supports\",\n     \"note\": \"'Avestan parsuya- \\\"of water\\\", n., perhaps \\\"Schneewasser\\\"' stands verbatim in the pers- entry on p. 823.\"},\n    {\"ref\": \"IEC:1003\", \"status\": \"supports\",\n     \"note\": \"Mann col. 1003: 'Av. cf. parəš-, v. (e- or o-gde) \\\"drip\\\"' — the source of Nourai's 'pareš : drip'; note Mann's own 'cf.' marks it as a comparison, not a citation.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, searched for parsuya/parəš-\", \"stance\": \"silent\",\n     \"note\": \"grep -n 'parsuya|par§uya|parsuia' BRT.txt returns nothing — the Google-scan OCR of Bartholomae's Avestan transliteration is too noisy to locate the lemma; no positive or negative evidence obtained from him.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p. 298 s.v. *parš\", \"stance\": \"supports\",\n     \"note\": \"'*parš \\\"to sprinkle, strew\\\". *AVESTAN: Y Av. parsat.gauu- PN \\\"having a speckled cow\\\" (Yt 13.96, Yt 13.127)' — the Avestan attestation of the root, though not of a verb parəš-.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 46\", \"stance\": \"supports\",\n     \"note\": \"the Indo-Iranian 'drop/speckled' material (pṛṣatá-m 'Tropfen', pṛṣant- 'gesprenkelt') is gathered there under *per-s-.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"pâšîdan «پاشیدن»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP پاشیدن pāšīdan / pres. pāš- 'to sprinkle, scatter' continues Proto-Iranian *parš- with the regular Iranian development -rš- > -š- and compensatory lengthening of the vowel (the same change that gives Av. pāšna- 'heel' < *paršna-, NP پاشنه pāšna). Cheung sets it out under *parš: 'NWIR: NP pāšīdan/pāš-, (LW) Bal. pašit/paš-, Gz. paš-/paša, Siv. paš- \\\"to sprinkle, strew\\\" ... «PIE *pers-'; Mann col. 1003 has 'Per. pāšam, inf. pāšīdan'. The variant پاچیدن pāčīdan quoted in the chart's extra field is Mo'in's own cross-reference ('پاشیدن [- پاچیدن]'), a dialectal č/š alternation, and پاش pāš is the bare present stem used as a noun and in compounds (گلاب‌پاش, آب‌پاش).\",\n  \"derivation_fa\": \"«پاشیدن» با ستاک حالِ «پاش» دنبالهٔ ایرانیِ آغازینِ *parš- است: خوشهٔ -rš- در ایرانی به -š- بدل شده و واکهٔ پیش از آن به جبرانِ آن کشیده شده است — همان دگرگونی‌ای که در «پاشنه» (اوستایی pāšna- از *paršna-) دیده می‌شود. چونگ در فرهنگ فعل‌های ایرانی (ص ۲۹۸) زیر *parš می‌آورد: «فارسی نو pāšīdan/pāš-، بلوچی pašit/paš-» و آن را به *pers- هندواروپایی می‌رساند؛ مان نیز «pāšam، مصدر pāšīdan» را ثبت کرده است. صورت «پاچیدن» که در کنار آن آمده، ارجاع خود معین است و دگرگونیِ گویشیِ چ/ش است. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"IEC:1003\", \"status\": \"supports\",\n     \"note\": \"Mann col. 1003: 'Per. cf. pāšam, inf. pāšīdan, v. (e- or o-gde: Skt. parṣāmi, v. \\\"sprinkle\\\")'.\"},\n    {\"ref\": \"MON:665\", \"status\": \"partial\",\n     \"note\": \"the six-volume Farhang-e Farsi is not online and its pagination cannot be checked; in the two-volume Adena condensation (MON_part1.txt) the entry reads 'پاشیدن: pāšīdan [- پاچیدن] (مصم.) ... پراکندن، پریشیدن، افشاندن، ریختن، پاچیدن (عم.)' and 'پاش: pāš [ری. پاشیدن] (امص.) پاشیدن، برافشاندن' — headword, variant پاچیدن and پاش all as in the chart, but with no etymological tag, so Mo'in supports the words, not the IE derivation.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"p. 298 s.v. *parš\", \"stance\": \"supports\",\n     \"note\": \"'*NWIR: NP pāšīdan/pāš-, (LW) Bal. pašit/paš- ... \\\"to sprinkle, strew\\\" ... «PIE *pers- \\\"to spray, sprinkle\\\" = LIV: 788 f. | Pok.: 823'.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol.) s.vv. پاشیدن، پاش\", \"stance\": \"supports\",\n     \"note\": \"quoted above; confirms the forms and the variant پاچیدن.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss, searched for pāšīden\", \"stance\": \"silent\",\n     \"note\": \"grep of HRN.txt finds only 'pūside/pāsiden \\\"faulen\\\"' (no. 334), a different word; Horn has no entry for pāšīdan.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched پاشیدن\", \"stance\": \"silent\",\n     \"note\": \"the only hit (pdf p. 436) is an entry glossed 'فروپاشیدن؛ صدمهٔ شدید دیدن' belonging to a different root, so Aryanpur gives no independent support for pāšīdan < *pers-.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"parsamî\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Sanskrit has the root pṛṣ- 'to sprinkle' chiefly in the nominal derivatives pṛṣat- 'drop', pṛṣatá- 'speckled', pṛṣant-/pṛṣatī 'dappled (cow, antelope)' (RV, AV); the finite 1sg. 'parṣāmi' printed in the chart is Mann's normalized citation form for the strong grade, taken over verbatim from IEC col. 1003 ('Skt. parṣāmi, v. \\\"sprinkle\\\"'). It is thus a real Sanskrit formation-type but not the form a Vedic dictionary would head, and the derivation from PIE *pers- (with the Indo-Aryan *-rs- > -rṣ- retroflexion by the ruki rule) is standard. 'Plausible' therefore only because of the citation form, not the etymology.\",\n  \"derivation_fa\": \"در سنسکریت این ریشه بیشتر در صورت‌های اسمی دیده می‌شود: pṛṣat «قطره»، pṛṣant-/pṛṣatī «خال‌دار (گاو، آهو)» در ریگ‌ودا و اثرووِدا. صورت parṣāmi «می‌پاشم» که در نمودار آمده، عیناً از مان (ستون ۱۰۰۳) گرفته شده و صورتی است که او برای پایهٔ قوی بازسازی کرده، نه سرواژه‌ای که در فرهنگ‌های ودایی بیاید. خودِ ریشه‌شناسی درست است: *pers- هندواروپایی با قاعدهٔ «روکی» در هندوآریایی به pṛṣ- بدل می‌شود. پس ادعا با احتیاط پذیرفتنی است و ایراد تنها بر صورتِ نقل‌شده است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"IEC:1003\", \"status\": \"supports\",\n     \"note\": \"Mann col. 1003, inside the prs- entry: 'Per. cf. pāšam, inf. pāšīdan, v. (e- or o-gde: Skt. parṣāmi, v. \\\"sprinkle\\\")' — the exact source of the node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 823\", \"stance\": \"partial\",\n     \"note\": \"Pokorny cites for Old Indic only 'pṛṣat, pṛṣata-m \\\"drip\\\"; pṛṣant-, f. pṛṣatī \\\"dappled, dotted, spotted\\\", pṛṣatī \\\"scheckige cow\\\"' — no finite verb.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 46\", \"stance\": \"partial\",\n     \"note\": \"same nominal material ('ai. pṛṣant- \\\"gesprenkelt, bunt\\\", pṛṣatá-m \\\"Tropfen\\\"'), no *parṣāmi.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"p. 298\", \"stance\": \"partial\",\n     \"note\": \"'*SANSKRIT: pṛṣant- \\\"dappled, with white spots\\\" (RV, AV+) = EWAia II: 164' — Mayrhofer's dictionary likewise knows the nominal stem.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Greek\", \"words\": \"pardakos\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Greek πάρδακος (Ionic πόρδακος) 'wet, soaked' is a real, if rare, adjective. Mann puts it under *prs- with an explicit caveat — 'Gk. cf. pardakós, adj. (\\\"wet\\\", if for *prs- + *-dnk-)' — i.e. only on condition that the -d- is a suffixal extension. Walde-Pokorny, by contrast, set up a separate root on p. 50 of Bd. II: 'pord- \\\"naß, feucht, schleimig\\\": gr. πάρδακος \\\"naß, feucht\\\" (ion. πόρδακος, woraus πάρδακος assimiliert), lett. purdāt \\\"Nasenschleim\\\" (Persson, Beiträge 229)'. So the two authorities Nourai himself relies on disagree about this word: Mann places it here, Walde-Pokorny do not. The node is accordingly plausible rather than confirmed.\",\n  \"derivation_fa\": \"صفت یونانی πάρδακος (در گویش ایونی πόρδακος) «خیس، نمناک» واژه‌ای کمیاب ولی واقعی است. مان آن را با تردید زیر همین ریشه آورده است: «اگر از *prs- + *-dnk- باشد». در برابر، والده-پوکورنی (ج ۲ ص ۵۰) برای آن ریشهٔ جداگانه‌ای می‌سازد: pord- «خیس، نمناک، لزج» با گواه لتونیایی purdāt «آب‌بینی». پس دو منبعی که خودِ نورایی بر آن‌ها تکیه دارد در این واژه هم‌داستان نیستند و این خانه تنها «با احتیاط پذیرفتنی» است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"IEC:1003\", \"status\": \"supports\",\n     \"note\": \"'Gk. cf. pardakós, adj. (\\\"wet\\\", if for *prs- + *-dnk-)' in the prs- entry, col. 1003.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 50\", \"stance\": \"contradicts\",\n     \"note\": \"'pord- \\\"naß, feucht, schleimig\\\". gr. πάρδακος \\\"naß, feucht\\\" (ion. πόρδακος, woraus πάρδακος assimiliert), lett. purdāt \\\"Nasenschleim\\\". Persson Beitr. 229' — a root of its own, not pers-.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 823\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's pers- entry does not mention πάρδακος at all.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Medit\", \"words\": \"parnas, pard\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The first form is corrupt. Mann, in the very column Nourai cites (IEC 1003), writes inside the prs- entry: 'Hitt. paršā(mi), v. \\\"flee\\\" beside pap-parš(mi), v. \\\"sprinkle\\\"; paršanas, s. (\\\"leopard\\\", lit. \\\"dappled\\\")' — Hittite paršana- 'leopard', literally 'the dappled one'. 'parnas' is that word with -ša- lost; no source knows a Mediterranean *parnas. The printed page (pdf 407, book 377) shows 'parnas, pard : a spotted animal', so the extraction is faithful and the slip is Nourai's own. Substantively, the 'Medit' (Mediterranean substrate) label follows Partridge (PRT:349) and Klein, who derives Gk. pardos from Heb. bārōd 'spotted'; but modern opinion (AHD s.v. pard 'probably of Iranian origin; akin to Sogdian purδank'; Etymonline; Beekes ap. Wiktionary 'borrowed from a foreign eastern language', comparing Skt. pṛdāku, Pers. palang, Sogd. pwrδnk) treats the whole family as an Iranian/oriental Wanderwort, with Hitt. paršana- either a cognate or an early Anatolian relay — not as a separate Mediterranean etymon feeding both Sanskrit and Greek.\",\n  \"derivation_fa\": \"صورت نخست این خانه نادرست است. مان در همان ستون ۱۰۰۳ که نورایی به آن ارجاع داده، می‌نویسد: «هیتی paršanas «پلنگ»، در اصل به معنی خال‌دار». صورت «parnas» همان واژه است که هجای -ša- از آن افتاده و در هیچ منبعی واژهٔ «مدیترانه‌ایِ» parnas وجود ندارد. تصویر صفحهٔ چاپی (برگ ۴۰۷ پی‌دی‌اف، ص ۳۷۷ کتاب) نشان می‌دهد که همین «parnas» در کتاب چاپ شده است؛ پس خطا از خوانش اسکن نیست، خطای خودِ کتاب است. از سوی محتوا نیز برچسب «مدیترانه‌ای» از پارتریج و کلاین می‌آید (کلاین یونانی pardos را از عبری bārōd «خال‌دار» می‌گیرد)، در حالی که دیدگاه امروزی (AHD، اتیمآنلاین، بیکس) همهٔ این خانواده را واژه‌ای سرگردان با خاستگاه ایرانی/شرقی می‌داند.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"parnas, pard\",\n  \"correct_form\": \"paršanas (Hittite paršana- 'leopard', lit. 'the dappled one'; Mann IEC col. 1003)\",\n  \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=pard\", W + \"%CF%80%CE%AC%CF%81%CE%B4%CE%B1%CE%BB%CE%B9%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:1003\", \"status\": \"partial\",\n     \"note\": \"IEC.txt leaf 556 (col. 1003): '... Hitt. parša(mi), v. \\\"flee\\\" beside pap-pars(mi), v. \\\"sprinkle\\\"; parsanas, s. (\\\"leopard\\\", lit. \\\"dappled\\\")' — Mann has paršanas and calls it Hittite, not 'Medit', and does not print 'parnas'.\"},\n    {\"ref\": \"IEC:998\", \"status\": \"partial\",\n     \"note\": \"IEC.txt leaf 554 (col. 998): 'prd- (1), Indo-Iran. variant of type prs-, q. v. in Skt. pṛdākuḥ, m. (\\\"viper; tiger or panther\\\", lit. \\\"spotted\\\"); Per. palang, s. \\\"tiger or leopard\\\"; Oss. fälank, färank; Gk. (fr. Iran.) párdos, m. \\\"panther, leopard\\\"' — Mann derives the whole branch from an Indo-Iranian variant of the root, with Greek explicitly 'fr. Iran.'; there is no Mediterranean intermediary.\"},\n    {\"ref\": \"PRT:349\", \"status\": \"not_checked\",\n     \"note\": \"Partridge, Origins (1958), is lending-only on archive.org and not available locally; his 'Medit' label is nevertheless the evident source of Nourai's node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p. 1129 s.v. pard\", \"stance\": \"partial\",\n     \"note\": \"'Gk. πάρδος, πάρδαλις \\\"panther\\\", generally connected with OI. pṛdākuḥ ... It is more probable, however, that Greek πάρδος has been borrowed fr. Heb. bārōd, \\\"spotted\\\" (said of an animal), and lit. denotes \\\"the spotted animal\\\"' — a Semitic, not a Mediterranean-substrate, source for the 'spotted animal' idea.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. pard (online AHD)\", \"stance\": \"contradicts\",\n     \"note\": \"'[Middle English parde, from Old French, from Latin pardus, from Greek pardos, probably of Iranian origin; akin to Sogdian purdhank.]' — Iranian, not Mediterranean.\"},\n    {\"src\": \"SOD\", \"where\": \"Gharib no. 8204\", \"stance\": \"supports\",\n     \"note\": \"'8204 pwrδʾnk' glossed 'leopard' — the Sogdian word AHD invokes; it shows the family is at home in Iranian.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Sanskrit\", \"words\": \"pardâku\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Sanskrit पृदाकु pṛdāku- is genuine, but two qualifications are needed. (a) Its oldest meaning is 'adder, snake': Horn notes expressly 'skr. pṛdāku- \\\"Tiger, Panther\\\" (ai. pṛdāku-, pṛdākū- nur \\\"Natter, Schlange\\\")', i.e. the Vedic word means only 'viper' and the 'panther' sense is later Sanskrit; Mann glosses 'viper; tiger or panther', lit. 'spotted'. (b) The direction of the arrow is doubtful: Mann treats prd- as an 'Indo-Iran. variant of type prs-' (col. 998), i.e. pṛdāku- is a formation on the inherited root, not a borrowing from a Mediterranean source, and the standard view (Beekes, AHD, Etymonline) makes the whole word-family an Iranian-based Wanderwort. The transcription pardâku for pṛdāku- is Nourai's habitual way of writing vocalic ṛ, not an error.\",\n  \"derivation_fa\": \"واژهٔ سنسکریت pṛdāku واقعی است، اما دو نکته هست: نخست آنکه معنی کهن آن «مار، افعی» است و معنی «پلنگ/ببر» متأخر است؛ هرن صریح می‌گوید که در سنسکریت ودایی تنها «مار» معنی می‌دهد. دوم آنکه سوی پیکان جای تردید دارد: مان (ستون ۹۹۸) prd- را «گونهٔ هندوایرانیِ همان ریشهٔ prs-» می‌داند، یعنی pṛdāku مشتقی از ریشهٔ موروثی است نه وام‌واژه‌ای از منبعی مدیترانه‌ای؛ دیدگاه رایج امروزی نیز (بیکس، AHD) کل این خانواده را واژه‌ای سرگردان با خاستگاه ایرانی می‌شمارد. آوانویسی pardâku به جای pṛdāku شیوهٔ همیشگی نورایی در نوشتن «ر» واکه‌ای است و خطا شمرده نمی‌شود.\",\n  \"sources\": [W + \"%CF%80%CE%AC%CF%81%CE%B4%CE%B1%CE%BB%CE%B9%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1129\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p. 1129 s.v. pard (IEC leaf-checked: KLN_1966.txt leaf 603, whose neighbours carry the running numbers 1126/1127 and 1130/1131, so this leaf = pp. 1128-1129): 'Gk. πάρδος, πάρδαλις \\\"panther\\\", generally connected with OI. pṛdākuḥ, \\\"panther, tiger\\\"'. The page number is exactly right.\"},\n    {\"ref\": \"PRT:349\", \"status\": \"not_checked\",\n     \"note\": \"Partridge, Origins 1958 — lending-only on archive.org, no local copy.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann col. 998 s.v. prd- (1)\", \"stance\": \"partial\",\n     \"note\": \"'prd- (1), Indo-Iran. variant of type prs-, q. v. in Skt. pṛdākuḥ, m. (\\\"viper; tiger or panther\\\", lit. \\\"spotted\\\")' — supports the root-affiliation, contradicts the Mediterranean parentage.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 326, p. 72\", \"stance\": \"partial\",\n     \"note\": \"'skr. pṛdāku- \\\"Tiger, Panther\\\" (ai. pṛdāku-, pṛdākū- nur \\\"Natter, Schlange\\\")' — the 'panther' meaning is post-Vedic.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"πάρδαλις (Beekes 2010)\", \"stance\": \"partial\",\n     \"note\": \"'Borrowed from a foreign eastern language', compared with Skt. pṛ́dāku, Pers. palang, Pashto pṛāng, Bactrian porlango-, Sogdian pwrδnk.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"pard «پارد»; palang «پلنگ»; yŭspalang «یوزپلنگ»\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"پلنگ palang 'leopard' is old and certain — MP palang, Kurd. pilink, Pashto pṛāng, Bactrian πορλαγγο-, Oss. färäng — but it is a COGNATE of Sanskrit pṛdāku-, not a loan from it, as the arrow claims. Hübschmann (Persische Studien pp. 145 and 260) derives it inside Iranian: 'Mit Uebergang von ṛ in a: palang \\\"Leopard oder Panther\\\" (aus *pulang) = afgh. pṛang, skr. pṛdāku-, gr. πάρδαλις, πάρδος' — i.e. NP palang goes back to an Old Iranian *pṛd-anga-/*pṛdanka- with the regular Iranian vocalization of syllabic ṛ (ṛ > ur/ul/al) and the same suffix seen in Sogdian pwrδʾnk 'leopard'. Horn no. 326 (p. 72) likewise merely compares the Sanskrit. یوزپلنگ yūz-palang 'cheetah' is a transparent Persian compound of یوز yūz 'cheetah' + palang, correctly cross-referenced by the chart to root Yeu 3. پارد pard «پارد», however, is not a Persian word for 'panther': Dehkhoda, Mo'in and Amid know پارد only as a place-name (a district of Qazvin) and, in one source, 'old woman'; Borhan-e Qate' has no such entry either. It looks like the Latin/English pard written back into Persian script. Hence the node as drawn is disputed.\",\n  \"derivation_fa\": \"«پلنگ» واژه‌ای کهن و مسلم است — فارسی میانه palang، کردی pilink، پشتو pṛāng، بلخی πορλαγγο-، آسی färäng — اما هم‌ریشهٔ pṛdāku سنسکریت است، نه وام‌گرفته از آن، چنان‌که پیکان نمودار می‌گوید. هوبشمان (مطالعات فارسی، ص ۱۴۵ و ۲۶۰) آن را درون ایرانی توضیح می‌دهد: palang از *pulang و آن از ایرانی باستان *pṛd-anga-، با تحول قاعده‌مندِ «ر»ِ واکه‌ای به ur/ul/al؛ همان پسوندی که در سغدی pwrδʾnk «پلنگ» دیده می‌شود. «یوزپلنگ» ترکیب روشن «یوز + پلنگ» است. اما «پارد» در فارسی واژه‌ای به معنی پلنگ نیست: دهخدا، معین و عمید تنها «پارد» را نام بلوکی از توابع قزوین (و در یک منبع «زن پیر») آورده‌اند و در برهان قاطع هم چنین مدخلی نیست؛ ظاهراً صورت لاتینی/انگلیسی pard است که به خط فارسی بازنویسی شده. از این رو این خانه چنان‌که رسم شده پذیرفتنی نیست.\",\n  \"sources\": [\n    W + \"%D9%BE%D9%84%D9%86%DA%AF\",\n    \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%B1%D8%AF/\",\n    \"https://www.etymonline.com/word/leopard\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"HRN:72\", \"status\": \"partial\",\n     \"note\": \"HRN.txt leaf 94 = printed p. 72, no. 326: 'peleng \\\"Leopard\\\". skr. pṛdāku- \\\"Tiger, Panther\\\" (ai. pṛdāku-, pṛdākū- nur \\\"Natter, Schlange\\\"). kurd. LW. pilink; afγ. pṛang.' Horn compares the Sanskrit word in his usual cognate-listing format; he nowhere says Persian borrowed it from Sanskrit.\"},\n    {\"ref\": \"BQT:416\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 642 (printed ≈ 414-416; Aryanpur's entry پارس/پلنگ cites 'برهان قاطع : ۴۱۶' for this very word, which fixes the page) has the headword 'پلنگ ... جانوری است معروف ... دشمن شیر است ... و هر چیز که در آن نقطه‌ها باشد' — note Borhan's own gloss 'anything with spots on it', which is the semantic core of the root. Mo'in's Latin-script footnote on that page is not legible in the OCR.\"},\n    {\"ref\": \"SKT:372\", \"status\": \"not_found\",\n     \"note\": \"in the 1911 Concise Skeat (SKT.txt) p. 372 (leaf 392) is the 'post-' range; the entry is at p. 329: 'Pard, a panther, leopard. (L.-Gk.) L. pardus. - Gk. πάρδος. An Eastern word ...'. Nourai's 372 must belong to another impression; the content supports the Greek-Latin-English chain but has nothing on Persian.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 145, 260\", \"stance\": \"contradicts\",\n     \"note\": \"p. 145: 'Mit Uebergang von ṛ in a: palang \\\"Leopard oder Panther\\\" (aus *pulang) = afgh. pṛang \\\"a tiger, a panther\\\", skr. pṛdāku-, gr. πάρδαλις, πάρδος'; p. 260 lists palang among the words showing Iranian ṛ > ul/al. Hübschmann derives palang inside Iranian, not from Sanskrit.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. 998\", \"stance\": \"contradicts\",\n     \"note\": \"'prd- (1), Indo-Iran. variant of type prs- ... Skt. pṛdākuḥ ...; Per. palang, s. \\\"tiger or leopard\\\"; Oss. fälank, färank; Gk. (fr. Iran.) párdos' — palang is a parallel Iranian reflex, on a level with the Sanskrit word.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"Persian پلنگ\", \"stance\": \"contradicts\",\n     \"note\": \"lists Bactrian πορλαγγο-ζινο, Pashto پړانګ, Sanskrit पृदाकु, Ancient Greek πάρδαλις as cognates, i.e. parallel developments, not a Sanskrit loan.\"},\n    {\"src\": \"MON\", \"where\": \"Dehkhoda/Mo'in/Amid s.v. پارد (abadis.ir)\", \"stance\": \"contradicts\",\n     \"note\": \"'پارد. (اِخ) بلوکی از توابع قزوین' and 'پارد. (ص) زن پیر' — no sense 'panther' in any of the three dictionaries.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, pdf p. 149 (headword پارس/پلنگ)\", \"stance\": \"partial\",\n     \"note\": \"gives Pahlavi palang, Kurdish, Pashto, Sanskrit pṛdāku, Greek pardos, Latin pardus, English pard, and notes 'بیشتر واژه‌ریشه‌شناسان معتقدند که این واژه از زبان‌های هند و ایرانی به یونانی و سپس به لاتین و غیره رفته است' — Indo-Iranian → Greek → Latin, and he cites برهان قاطع ۴۱۶.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Greek\", \"words\": \"pardos\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Greek πάρδος (and the commoner πάρδαλις) 'panther, leopard' is well attested from Aristotle onwards, and the Latin and English links hanging from it are beyond doubt. What is doubtful is the parent drawn here. Three views compete: (i) a Semitic source — Klein p. 1129, following H. Lewy 1895, derives πάρδος from Heb. bārōd 'spotted' (with b > p as in Εὐρώπη from ʿerebh), and Nourai's 'Medit' box is the Partridge/Klein variant of this; (ii) an Iranian source — AHD s.v. pard 'probably of Iranian origin; akin to Sogdian purδank', Etymonline s.v. pard 'from the same source (probably Iranian) as Sanskrit pṛdāku-s and Persian palang'; (iii) simply 'borrowed from a foreign eastern language' (Beekes 2010, quoted by Wiktionary), comparing Skt. pṛdāku, Pers. palang, Bactrian porlango-, Sogd. pwrδnk. Mann col. 998 is explicit: 'Gk. (fr. Iran.) párdos'. Today (ii)/(iii) are the standard view, so the word is right but its 'Medit' parentage is not the current account.\",\n  \"derivation_fa\": \"واژهٔ یونانی πάρδος (و صورت پرکاربردتر πάρδαλις) «پلنگ» از ارسطو به بعد گواه دارد و حلقه‌های لاتینی و انگلیسیِ پس از آن قطعی‌اند؛ آنچه جای گفت‌وگوست خاستگاه آن است. سه دیدگاه در برابر هم‌اند: کلاین (ص ۱۱۲۹) به پیروی از لِوی آن را از عبری bārōd «خال‌دار» می‌گیرد و «مدیترانه‌ای»ِ نورایی همین دیدگاه است؛ AHD و اتیمآنلاین آن را «احتمالاً ایرانی، هم‌ریشه با سغدی purδānk» می‌دانند؛ و بیکس آن را وام‌واژه‌ای از «زبانی شرقی» می‌شمارد. مان نیز صریح می‌نویسد: «یونانی párdos (از ایرانی)». امروز دو دیدگاه اخیر پذیرفته‌ترند؛ پس واژه درست است ولی پدرِ نمودار (خانهٔ مدیترانه‌ای) دیدگاه روز نیست.\",\n  \"sources\": [\n    W + \"%CF%80%CE%AC%CF%81%CE%B4%CE%B1%CE%BB%CE%B9%CF%82\",\n    \"https://www.ahdictionary.com/word/search.html?q=pard\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1129\", \"status\": \"partial\",\n     \"note\": \"Klein p. 1129 s.v. pard: 'fr. L. pardus, fr. Gk. πάρδος, πάρδαλις, \\\"panther\\\", generally connected with OI. pṛdākuḥ ... It is more probable, however, that Greek πάρδος has been borrowed fr. Heb. bārōd, \\\"spotted\\\" ... see Heinrich Lewy, Die semitischen Fremdwörter im Griechischen, Berlin, 1895, p. 7.' Klein's 'spotted animal' idea is Semitic, not Mediterranean.\"},\n    {\"ref\": \"PRT:349\", \"status\": \"not_checked\", \"note\": \"Partridge is lending-only; not consultable.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann col. 998\", \"stance\": \"contradicts\",\n     \"note\": \"'Gk. (fr. Iran.) párdos, m. \\\"panther, leopard\\\"' — Mann makes the Greek a loan from Iranian.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. pard\", \"stance\": \"contradicts\",\n     \"note\": \"'from Greek pardos, probably of Iranian origin; akin to Sogdian purdhank'.\"},\n    {\"src\": \"SOD\", \"where\": \"Gharib no. 8204 pwrδʾnk 'leopard'\", \"stance\": \"supports\",\n     \"note\": \"the Sogdian form on which the Iranian explanation rests is in Gharib's dictionary.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"Latin\", \"words\": \"pardus\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin pardus 'panther' (Pliny, Lucan) is a straightforward loan from Greek πάρδος, with the Greek o-stem taken into the Latin second declension (-os > -us); the feminine pardalis was likewise borrowed. From pardus come Late Latin leopardus (leō + pardus, 'lion-pard', so called because the animal was thought to be a hybrid) and, by way of Old French, English pard and leopard.\",\n  \"derivation_fa\": \"لاتینی pardus «پلنگ» وام‌واژه‌ای است از یونانی πάρδος که ستاک -os یونانی در صرف دوم لاتینی به -us بدل شده است. از همین صورت، لاتینی متأخر leopardus (leō «شیر» + pardus) ساخته شد، زیرا پنداشته می‌شد این جانور دورگهٔ شیر و پلنگ است؛ و از راه فرانسهٔ کهن به انگلیسی pard و leopard رسید. ادعای نورایی درست است.\",\n  \"sources\": [\"https://www.etymonline.com/word/leopard\", \"https://www.ahdictionary.com/word/search.html?q=pard\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:952\", \"status\": \"supports\",\n     \"note\": \"the page number belongs to the 1976 New College Edition, which is not open online, but the AHD entry itself (checked in the current online edition, same wording tradition) reads s.v. pard: '[Middle English parde, from Old French, from Latin pardus, from Greek pardos ...]' — the Greek > Latin link Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 1129 s.v. pard; p. 900f. s.v. leopard\", \"stance\": \"supports\",\n     \"note\": \"'pard ... ME. parde, fr. OF., fr. L. pardus, fr. Gk. πάρδος'; 'leopard, n. — ME. leopard, lepard, fr. OF. leopard (F. léopard), fr. L. leopardus, lit. \\\"lion-pard\\\", fr. leō, \\\"lion\\\", and pardus, \\\"pard\\\"'.\"},\n    {\"src\": \"SKT\", \"where\": \"p. 329 s.v. Pard\", \"stance\": \"supports\",\n     \"note\": \"'Pard, a panther, leopard. (L. - Gk.) L. pardus. - Gk. πάρδος. An Eastern word.'\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"English\", \"words\": \"pard, leopard\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"ME parde (14th c., Chaucer) < OF pard < L. pardus < Gk. pardos: modern English pard, now archaic/poetic. LEOPARD: ME leopard/lebard < OF leopard < Late Latin leopardus < Gk. leopardos (leōn 'lion' + pardos), the ancients taking the leopard for a lion-panther hybrid; the same compound gives camelopard 'giraffe' (kamēlos + pardalis). The chain is uncontroversial in Klein, Skeat, AHD and Etymonline alike.\",\n  \"derivation_fa\": \"انگلیسی میانهٔ parde (سدهٔ ۱۴، چاسر) از فرانسهٔ کهن pard و آن از لاتینی pardus و یونانی pardos؛ صورت امروزی pard اکنون کهن و شاعرانه است. «leopard» از انگلیسی میانهٔ leopard/lebard، از فرانسهٔ کهن، از لاتینی متأخر leopardus و یونانی leopardos (leōn «شیر» + pardos)، زیرا پیشینیان پلنگ خالدار را دورگهٔ شیر و پلنگ می‌پنداشتند؛ همین ترکیب در camelopard «زرافه» نیز دیده می‌شود. این زنجیره نزد کلاین، اسکیت، AHD و اتیمآنلاین یکسان است.\",\n  \"sources\": [\"https://www.etymonline.com/word/leopard\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1129\", \"status\": \"supports\",\n     \"note\": \"Klein p. 1129 s.v. pard: 'pard, n., leopard (archaic) — ME. parde, fr. OF., fr. L. pardus, fr. Gk. πάρδος, πάρδαλις, \\\"panther\\\" ... Cp. leopard, camelopard, guepard.'\"},\n    {\"ref\": \"SKT:372\", \"status\": \"not_found\",\n     \"note\": \"p. 372 of the 1911 Concise Skeat is the 'post-' range; the relevant entry is p. 329 ('Pard, a panther, leopard. (L.-Gk.) L. pardus. — Gk. πάρδος'), so Nourai's page number does not match this edition, though the content agrees.\"},\n    {\"ref\": \"PRT:349\", \"status\": \"not_checked\", \"note\": \"Partridge not available (lending-only).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"p. 329 s.v. Pard\", \"stance\": \"supports\",\n     \"note\": \"'Pard, a panther, leopard. (L. - Gk.) L. pardus. - Gk. πάρδος. An Eastern word.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"s.vv. leopard, pard\", \"stance\": \"supports\",\n     \"note\": \"'leopard ... from Old French lebard/leupart, from Late Latin leopardus, literally \\\"lion-pard\\\" ... from Greek leopardos, from leon \\\"lion\\\" + pardos \\\"male panther\\\"'; pard: 'from the same source (probably Iranian) as Sanskrit prdaku-s \\\"leopard, tiger, snake\\\" and Persian palang \\\"panther\\\"'.\"}\n  ]\n }\n]\n\nout = {\n  \"pdf_page\": 407,\n  \"book_page\": 377,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [e0, e1]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-407.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-407.py"
}
```


### [2026-09-14T01:13:04.627Z] TOOL RESULT

```
written
```


## [2026-09-14T01:13:08.535Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-407.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 407"
}
```


### [2026-09-14T01:13:09.862Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 8, 'confirmed': 6, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'partial': 6, 'not_checked': 5, 'not_found': 2}
books consulted: {'supports': 21, 'partial': 13, 'silent': 7, 'contradicts': 10} | by book: {'KLN': 5, 'HRN': 4, 'MON': 4, 'WLD': 4, 'Wiktionary': 3, 'SOD': 3, 'POK': 3, 'AHD': 3, 'CHEUNG': 3, 'IEC': 3, 'BRT': 2, 'NYB': 2, 'PHD': 2, 'Etymonline': 2, 'ARY': 2, 'SKT': 2, 'FVQ': 1, 'BQT': 1, 'PLA': 1, 'HUB': 1}
```


## [2026-09-14T01:13:27.200Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-407.json` written, valid JSON, `verify_check.py 407` shows **0 PROBLEM lines** (17/17 nodes).

**Page 407 (book p. 377), 2 entries + 1 redirect (Pu 1 → Peu, skipped)**
- Roots: 2 confirmed (Prî = POK 844 *prāi-/*prī-; Prs = POK 823 *pers-, Mann col. 1003 *prs- verbatim).
- Nodes: 6 confirmed, 8 plausible, 2 disputed, 1 transcription_suspect.

Flagged items:
- **transcription_suspect — Prs #5 "parnas, pard [Medit]"**: no source knows a Mediterranean *parnas; Mann (the cited IEC:1003) has Hittite **paršanas** 'leopard', lit. 'dappled'. The printed page shows "parnas", so `error_in: book` (extraction faithful); page PNG saved to `data/verification/sources/refs/ocr/BOOK/407.png`. Also the "Medit" parentage itself is outdated — AHD/Etymonline/Beekes make the whole family an Iranian Wanderwort (cf. Sogdian pwrδʾnk, Gharib 8204).
- **disputed — Prî #7 "free, fresh, friend, Friday"**: free/friend/Friday are correct (Watkins s.v. prī-), but *fresh* belongs to PGmc *friskaz (OCS prěsьnъ, Lith. prėskas) — Klein and Etymonline both, unrelated root.
- **disputed — Prs #7 Persian "pard پارد; palang; yūzpalang"**: پارد is not a Persian word for 'panther' (Dehkhoda/Mo'in/Amid have only the Qazvin place-name); and palang is a *cognate* of Skt pṛdāku (Hübschmann pp. 145/260: *pulang < *pṛd-ang-; Mann col. 998; Wiktionary), not a borrowing from Sanskrit as the arrow draws.

Other notable findings: Prî #1 labels the **Middle Persian** infinitive *āfritan* as Avestan (Horn no. 39 p. 10, MacKenzie p. 5, Nyberg all put it in Pahlavi) → plausible. Prî #3 ʿifrīt: AHD:23 and PLA:203 support Nourai exactly (MP āfrīd 'created'), but the native ʿ-f-r derivation is still live → plausible. Sogdian ʾprytyy is glossed 'praised' by Gharib, not 'created'. Reference-number misses: **SKT:372** (entry is p. 329 in the 1911 Concise ed.); KLN:1129 and BQT:51/416, HRN:72, PLA:203, IEC:998/1003, POK:823/844 all verified on the exact page. No extraction errors found (JSON matches the printed page throughout).
