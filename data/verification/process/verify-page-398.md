# Verification process log — verify-page-398


## [2026-09-14T00:49:52.091Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 398 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-398.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-398.json. Write /home/sfmqrb/git/rishe/data/verification/page-398.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 398` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:53.332Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:54.293Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:54.312Z] TOOL RESULT

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


## [2026-09-14T00:49:54.726Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-398.txt"
}
```


### [2026-09-14T00:49:54.750Z] TOOL RESULT

```
1	=== PDF page 398 (book page 368) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 4, Pera : to assign, to trade. Related to the Indo-European root "Per 1".  (refs POK:817)
4	#1 (parent #0) [Avestan] refs=POK:817 | pâra 1 : debt
5	  #2 (parent #1) [Pahlavi] refs=NYB:150 | pârak : debt, bribe, gift
6	    #3 (parent #2) [Persian] refs=MON; BQT:351; AEF:333 | pâreh «پاره (آتشپاره)» : money, gift, a piece of something
7	#4 (parent #0) [Latin] refs=AHD; KLN:1133 | portio, pars : part ; pertum : price, worth
8	  #5 (parent #4) [English] refs=None | part, parcel, portion, compare, price, prize, prison
9	#6 (parent #0) [Greek] refs=POK:817; AHD; KLN:1219 | pornĕ : "purchased", prostitute
10	  #7 (parent #6) [English] refs=None | pornography
11	--- entry 1 ---
12	ROOT Pera -> redirect to Per 4
13	--- entry 2 ---
14	ROOT [Indo-European] Perk 1 : to ask  (refs POK:821)
15	#1 (parent #0) [Avestan] refs=POK:821; SNS:141; AEF:205 | fras : to ask ; frasâ,frašna : question ; prs-sa, pere-sa : to ask ; peresaiti : he asks ; paiti-frasna : interrogation, punishment ☞Per 3
16	  #2 (parent #1) [Pahlavi] refs=BQT:206,385 | porsitan : to ask ; pâtî-frâs : punishment
17	    #3 (parent #2) [Persian] refs=BQT:385; AEF:205; ETM:62 | porsîdan «پرسیدن (پرسش)» : to ask ; pâdafrâh «پادافراه» : punishment | NOTE: See derivation through Old Persian
18	#4 (parent #0) [Old Persian] refs=POK:821; TZF:26; KNT:176 | pare-sa : to ask ; aparsam : I asked ; frašta, frasta : interrogated
19	  #5 (parent #4) [Pahlavi] refs=TZF:26 | purs : to ask
20	    #6 (parent #5) [Persian] refs=TZF:26 | porsîdan «پرسیدن (پرسش)» : to ask | NOTE: See the derivation through Avestan.
21	#7 (parent #0) [Latin] refs=POK; AHD | precârî : to pray, ask from God ; prex : prayer
22	  #8 (parent #7) [English] refs=AHD | pray, prayer
23	
```


## [2026-09-14T00:49:57.747Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-398.json",
 "description": "Read source JSON for page 398"
}
```


### [2026-09-14T00:49:57.806Z] TOOL RESULT

```
{
  "pdf_page": 398,
  "book_page": 368,
  "entries": [
    {
      "root": {
        "name": "Per 4, Pera",
        "lang": "Indo-European",
        "refs": "POK:817",
        "gloss": "to assign, to trade. Related to the Indo-European root \"Per 1\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:817",
          "words": [
            {"translit": "pâra 1", "gloss": "debt", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "NYB:150",
          "words": [
            {"translit": "pârak", "gloss": "debt, bribe, gift", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON; BQT:351; AEF:333",
          "words": [
            {"translit": "pâreh", "gloss": "money, gift, a piece of something", "script": "پاره (آتشپاره)"}
          ],
          "note": null,
          "quote": {"text": "به از نیکو سخن چیزی نیابی - که زی دانا بری برسم پاره", "poet": "Nâser-Khosrow"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:1133",
          "words": [
            {"translit": "portio, pars", "gloss": "part", "script": null},
            {"translit": "pertum", "gloss": "price, worth", "script": null}
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
            {"translit": "part, parcel, portion, compare, price, prize, prison", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:817; AHD; KLN:1219",
          "words": [
            {"translit": "pornĕ", "gloss": "\"purchased\", prostitute", "script": null}
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
            {"translit": "pornography", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Pera",
        "redirect": "Per 4"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Perk 1",
        "lang": "Indo-European",
        "refs": "POK:821",
        "gloss": "to ask"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:821; SNS:141; AEF:205",
          "words": [
            {"translit": "fras", "gloss": "to ask", "script": null},
            {"translit": "frasâ,frašna", "gloss": "question", "script": null},
            {"translit": "prs-sa, pere-sa", "gloss": "to ask", "script": null},
            {"translit": "peresaiti", "gloss": "he asks", "script": null},
            {"translit": "paiti-frasna", "gloss": "interrogation, punishment", "script": null, "see": ["Per 3"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:206,385",
          "words": [
            {"translit": "porsitan", "gloss": "to ask", "script": null},
            {"translit": "pâtî-frâs", "gloss": "punishment", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:385; AEF:205; ETM:62",
          "words": [
            {"translit": "porsîdan", "gloss": "to ask", "script": "پرسیدن (پرسش)"},
            {"translit": "pâdafrâh", "gloss": "punishment", "script": "پادافراه"}
          ],
          "note": "See derivation through Old Persian",
          "quote": {"text": "ترا زین پیش بسیار آزمودم - چه پاداش و چه پادافره نمودم", "poet": "Vîs-o-Râmîn"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:821; TZF:26; KNT:176",
          "words": [
            {"translit": "pare-sa", "gloss": "to ask", "script": null},
            {"translit": "aparsam", "gloss": "I asked", "script": null},
            {"translit": "frašta, frasta", "gloss": "interrogated", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "TZF:26",
          "words": [
            {"translit": "purs", "gloss": "to ask", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "TZF:26",
          "words": [
            {"translit": "porsîdan", "gloss": "to ask", "script": "پرسیدن (پرسش)"}
          ],
          "note": "See the derivation through Avestan.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK; AHD",
          "words": [
            {"translit": "precârî", "gloss": "to pray, ask from God", "script": null},
            {"translit": "prex", "gloss": "prayer", "script": null}
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
            {"translit": "pray, prayer", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:50:00.302Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','NYB','MON','BQT','AEF','AHD','KLN','SNS','TZF','KNT','ETM','HRN','HUB','PHD','BRT','WLD','IEC','SYN','SKT','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T00:50:01.409Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_ety
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
```


## [2026-09-14T00:50:06.603Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; ls ocr 2>/dev/null | head",
 "description": "List local reference files"
}
```


### [2026-09-14T00:50:06.660Z] TOOL RESULT

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


## [2026-09-14T00:50:07.448Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:50:07.503Z] TOOL RESULT

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


## [2026-09-14T00:50:10.438Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T00:50:10.474Z] TOOL RESULT

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


## [2026-09-14T00:50:16.608Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | sed -n '60,200p'; echo \"=== POK files ===\"; ls -la POK*",
 "description": "List remaining refs and POK files"
}
```


### [2026-09-14T00:50:16.662Z] TOOL RESULT

```
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
=== POK files ===
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
```


## [2026-09-14T00:50:17.446Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"verkaufen\" POK_full.txt | head -30",
 "description": "Grep Pokorny for verkaufen"
}
```


### [2026-09-14T00:50:17.503Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:50:19.813Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -40 POK_full.txt; echo \"=== grep 817 ===\"; grep -n \"817\" POK_full.txt | head -20",
 "description": "Inspect POK_full format"
}
```


### [2026-09-14T00:50:19.885Z] TOOL RESULT

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
=== grep 817 ===
23972:References: WP. I 817 ff., WH. I 104 ff., 354 f., 381 ff., 860, 861, Feist 484 ff., Trautmann 
67020:addendum toS. 817: 
67037:Page(s): 816-817 
67067:Page(s):817 
81916:References: WP. II 643 ff., WH. I 817 f., II 599, Trautmann 284, 290 f., Vasmer 3, 18.
```


## [2026-09-14T00:50:22.075Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66980,67130p' POK_full.txt",
 "description": "Read Pokorny around page 817"
}
```


### [2026-09-14T00:50:22.165Z] TOOL RESULT

```
Avestan: paratu-{vc\] 'crossing, bridge'; OAv. (fra)fra{\sq.sub].aox.3iCt] 'to cross' ( Y 



46.10); LAv. fra-para/7a/jhe [2sg.caus.sub\.ac\..] "to bring over' ( Yt 71.16); ni-paraiieinti 
[3pl.caus.act.] "to lead to' 

Latin porta, -are'bear, carry, guide, lead, drive, bringen, offer', Umbrian portatu 
"portato', yOO/:^i/5/"portaverit' ( *poritd, to an iterative *poreJd)\ 

Gothic faran, for^ wander, pull, drag', farjan^6uye, schiffen', stem V. Old High German 
Old English faran. Old Icelandic /^as "drive', schw. V. Old Saxon ferian. Old High German 
ferien, ferren. Old Icelandic /fe/ya "drive, schiffen'(/&/75/7 = *poreid)\ Old Icelandic fQr\. 
'journey, Fahrt', Old English faru\. "Fahrt, journey, pull'. Middle High German var\. 'Fahrt, 
way, kind of, way' (fem. to gr. n6po(;); Old Icelandic farmr. Old English fearmm. "shipload', 
Old High German farm " bark, type of sailboat' (= russ. porom); lengthened grade Kaus. 
Old Saxon forian. Old High German fuoren. Modern High German fuhren. Old Icelandic 
f0ra6s.. Old English (as Iter.) feran^qehu, pull, drag' (= Avestan parayati. Old Church 
S\av\c par/f/); Old High German fuoraTuhre, Fahrt etc.'. Old English fori. "Fahrt, cart '; 
Old Icelandic f0rr lahrbar, suitable ', Old High German gi-fuori^ fitting, comfortable, useful 
'; Verbalabstr. Old Icelandic ferd. Old English fierd. Old High German Middle High German 
fartTabr^ {*por-ti-); 

russ. -Church Slavic na-perjg{= Treipw), -yOeA/Z/'durchbohren'; perg, p-brati^i\y'\ Iter, pariti 
"fly, schweben' (= Old Indie parayati, Germanic Jorjan); pero^ feather '; russ. porom, 
Serbo-Croatian pram^ ferry ' (= Old Icelandic farmr); presumably here also Old Church 
S\ay\c porjg, yO/a//" carve, slit'; about Modern High German Farne\.c. s. addendum S. 850. 

per-tu-, por-tu-, Gen. pf-teus^ passage, ford': Avestan porotu-sxxx. f. (Proto Aryan *prtu- 
s) and pasu-src\. (Proto Aryan *prtu-s) " passage, ford, bridge' {hu-para^wa-' good to 
overstep ' = "Euphrat'); Latin portus, -Js"Hausture' (XII tab.); " harbor', angi-portus 
"narrow Passage, Nebengaftchen'; besides a-stem porta ^Siadiior, gate' = Oscan [pjurtam; 
lllyrian PN Nau-portus, gall, ritu- "ford' in Ritumagus, Augustoritum, acymr. n't, ncymr. rhyd, 
corn. A/rford'; Old High German furt. Old English ford^iord' (zero grade Old Icelandic fjgrdr 
"narrow gulf, bay' from *per-tu-s); besides f. /-stem in Modern High German PN Furth 
{*furti-). 

Maybe alb. porte'door' derived from Latin porta'gate', port 'harbor' derived from Latin 
yOC»/:^^s 'harbor'. 

addendum toS. 817: 



To Church Slavic pero " feather ' belong *por-no- " feather ' in Old Indie parna-v\. " 
feather, leaf, Avestan parana-v\. " feather, wing'. Old Saxon Old High German farn 
"Farnkrauf (*Federkraut), Old English fearnm. 6s., Lithuanian sparnas, Latvian sparnsm. 
"wing' (das s-from the root spher-); 

*prati-s\n gall, ratis. Middle Irish raithi. 'Farnkrauf, bret. /'ao'-e/?/? collective ds.; 

*po-port-io-\y\ Lithuanian papartis, papartys Tamkraui', Latvian paparde, paparske (is.; 
with lengthened grade Slavic *paparti-\. in russ. paporotb e\.c. ds. 

WP. II 21, Trautmann 206, Vasmer2, 313. 

References: WP. II 39 f., WH. II 344, Trautmann 206, 215 f. 
Page(s): 816-817 

Root / lemma: per-2: C. per-, pera- 
Meaning: to sell 

Material: a. Gr. nspvriMi (present and Impf.), nEpaw, -u) (formal = nspaw "dringe through '), 
£n£paa(o)a, and nirrpaaKU), nspaou) (Attic nspoj), Enspaoa, nsnpaKa 'verkaufe', (gr. 
stem *pera-), nopvp 'meretrix'; Old Irish ren{a)/d ^s/erkauit' {*pr-n9-: gr. nspva-), Konj. 3. 
Sg. -/7a-(*/7a-after Indik. *[p]ri-na-ior "/b/e/'a-eingetreten), Perf. 3. Sg. -rir {*ri-r-e); verbal 
noun reicc{Da\..) 'Verkaufen' (in final sound after /cc "healing, payment ' directed); 
compare with an old guttural-extension Lithuanian perku pFrkti' buy '. 

p. Avestan pairyante^sxe become compared', a/p/'-par-' {se'\r\e blame) begleichen, 
penance, atonement make', a-psrst/'-s' atonement ', pdrs^a-n. " equalization of (blame), 
atonement, punishment ', para- m. "blame' (in addition probably also par- "verurteilen'); 
Latin p5/'(lengthened grade), yC>a/7s"gleichkommend, alike, pair', therefrom paro, -are 
"gleichschatzen', comparare^ Q,oxr\^ax€ (Umbrian pa/'ses/'paresf has das sfrom mers 
est). 

y. Old Indie purta-u., purtf- f. "earnings' = Latin pars, -tis "parf ( *pereti-), port/o^part, 
allotment ' (Post Classical; Classical only pro port/one, assim. from * pro part/one); Old Irish 
rann, cymr. rhan, mcorn. ran, abret. PI. rannou^parV ( *per9-sna); (common Celtic -ns-, -nt- 
> -nn-). Old Irish ern(a)id^ grav\{s\ Konj. r-a-aera^ex moge esgewahren', preterit ro-fr^ev 
has gewahrf ( *per-e), Fut. *ebraid{ *pi-pra-s-e-tf); ro-rath^\s gewahrt worden' ( *pra-to-l\, 
Hittite Paz's- "break, rupture, grind, split up, cut up, divide'. 

References: WP. II 40 f., WH. II 250 f., 256 f., 257 ff. 



Page(s):817 



Root / lemma: per-2. D. per- 

Meaning: to bear (child) 

Note: (as fera 'gebare' in einstiger reiationsliip to per-2: C "allot') 

Material: a. Latin pario, -ere, peperT, partum, pariturus " to give birth to children ', reperio, - 

Tre, repperJ, repertum'\N\edefi\nden, find, learn', partus, -us' to give birth to children, birth; 

foetus', Parca {*par/ca) originally 'Geburtsgottin', Propert/us actuaWy "the FriJhgeborene' = 

Umbrian Propart/e 'ProperiW, pare, -are'bere'\\.e, acquire, buy', comparo' buy' ("sich 

etwas besorgen, obtain '); //77/?e/'5/'e 'anschaffen = order'; 

Lithuanian per/u, peret/ "brute', peraTHom. PI. "Bienenlarven'. 

(3. Old Indie prthuka-m. 'rother, cattle, calf, the young of an animal ', Armenian ort', -u 
"calf of Rindes or Hirsches' (with formants -thu-)\ gr. nopiq, nopra^, nopiK; "calf, young 
cow'; cymr. e/'//7j//"abortus'; Old High German far, farro. Modern High German Farre, Old 
English fearr. Old Icelandic farri {*farz-) "bull', with gramm. variation Middle High German 
verse. Modern High German Farse "young cow' (Germanic *farsT, Gen. *farsjds), to Old 
English heah-fore, engl. heifer, originally from jungen animals, compare engl. farrow^uoi 
pregnant'. West Frisian fear^qeW!; lengthened grade Old English for. Middle Low German 
KO/'"Schweinchen'; Old Church Slavic za-/0/^/b/rb "wind-Ei', Czech s-pratek Iruh 
geborenes calf, kir. Kj/-pc»/:^c»/r"Fruhgeburt'. 

References: WP. II 41 f., WH. II 255 f., Trautmann 215. 
Page(s):818 

Root / lemma: per-2. E. per- 
Meaning: to try, dare, risk; danger 
Note: (= /Oe/'-"hinuberfuhren, durchdringen') 

Material: Armenian yC>"c»/7"Versuch' (express, p"-); gr. nsTpa f. "Erfahrung, Versuch', Aeolic 
nsppa (*n£pja), nsipau), -a^u) "versuche', £|jTT£ipo(; " skillful, smart, adroit'; Latin experior, - 
/?/""versuche, prijfe', expeffmentum "Versuch, examination ', comperid, -/?e"erfahre genau', 
opperior, -Iff, -Itus {and -tus) s^/r? "warte, expect ', perJtus" skillful ', perTculum^M ersuch. 
Probe; danger; Prozeft; accusation '; das /"from perT-tus, -culum derives from den 
compounds with -perior. Old Irish a(/)/'e"Wachen, attention', nir. faire, because of gallo-brit. 
areanTP\. "Kundschafter' from * psreja, Germanic '7^/7/73- "das Auftergewohnliche' in Gothic 
fairina\. "blame'. Old High German firina" crime ' etc.; Germanic Yera- "danger' in Old 
Icelandic farn. "danger, misfortune'. Old English /^/"m.. Old High German far(a)" 



pestering, temptation; snare, danger', to GotJiic ferjaxr\. "Aufpasser', Old Higli German 

/^/'e/7"auflauern' etc.; perhaps in addition with Abtonunggr. TaAai-nwpoq " afflicted ' as 

"Gefahren erduldend'. 

References: WP. II 28 f., WH. II 288 f. 

Page(s):818 

Root / lemma: per-3, per-g- 

Meaning: to hit
```


## [2026-09-14T00:50:46.894Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT para\"; grep -n \"pāra-\\|para-, m\\|pāra\" BRT.txt | head -40",
 "description": "Grep Bartholomae for para"
}
```


### [2026-09-14T00:50:46.947Z] TOOL RESULT

```
### BRT para
```


## [2026-09-14T00:50:48.724Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD parag\"; grep -n -i \"pārag\\|pʾlk\\|parag\" PHD.txt PHD_mackenzie.txt | head -30; echo \"### NYB parak\"; grep -n -i \"pārak\\|parak\" NYB_vol2_glossary.txt | head -30",
 "description": "Grep MacKenzie and Nyberg for parag/parak"
}
```


### [2026-09-14T00:50:48.841Z] TOOL RESULT

```
### PHD parag
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:814:appetizer pēšpārag.
PHD.txt:1085:bribe pārag.
PHD.txt:2099:gift āyaft, dāšn, pārag, das?r.
PHD.txt:2966:offering mézd, pārag, us(t)dfrit, zēhr.
PHD.txt:3039:paragraph darak.
PHD.txt:3045:pārag, pēšag,
PHD.txt:3183:portion bahr, jād(ag), kardag, pārag.
PHD.txt:3465:robber apparag; highway ~ rāhdār,
PHD.txt:4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
PHD_mackenzie.txt:1147:apparag [)j.ilg] robber.
PHD_mackenzie.txt:1884:·darak [dlk l ] section, paragraph.
PHD_mackenzie.txt:4017:Iparag [p'lk l I N para] piece, part, portion.
PHD_mackenzie.txt:4018:2parag [p'lk l I M p'rg, N para] gift, offering, bribe.
PHD_mackenzie.txt:4031: pargandan, pargan- [plkn-, plgn-du'               (P pr'gnd, N paragandan)]
PHD_mackenzie.txt:4221:pM-parag [pyfp)lk I N ""'a] an appetizer.
PHD_mackenzie.txt:6078:boil (vt.) ayardenidan.                bribe parag.
PHD_mackenzie.txt:6692:gift ayaft, dasn, parag, dasar.               grass giya(h).
PHD_mackenzie.txt:7160:night raid sabixon.                    offering mezd, parag, us(t)Ofrit, zohr.
PHD_mackenzie.txt:7242:paragraph darak.                       perfect (a.) bowandag, hangirdig,
PHD_mackenzie.txt:7246:part bahr, bazisn, parag, pesag,       perfection spurrigih.
PHD_mackenzie.txt:7279:piece parag; (backgammon, etc.)            polish abroxtan.
PHD_mackenzie.txt:7293:pitchfork sanag.                           portion bahr, jad(ag), kardag, parag.
PHD_mackenzie.txt:7477:robber apparag; highway.- rahdar.          sanctification yoJdahrgarih.
PHD_mackenzie.txt:8762:pesparag            '~e.KYV               pilban                \'t"'~Q)
PHD_mackenzie.txt:8856:1-2parag                   \~CU              payag                      '~t)
PHD_mackenzie.txt:11414:abannand               ~~Q)I           aharag, apparag'                ~~
### NYB parak
2944:pārak [p*lk'] a bribe 7313, 7515. — Av. (889) para- ‘debt’; MPrs p’rg ‘gift’; NP pärah ‘gift, bribe’.
5274:pāra-: pārak Para-data-: Pēš-dāt parena-, perona-: parr paresu- (peresu-): pahlūk paršta-, paršti-: pušt pasca: pas
6061:preg: pārak
```


## [2026-09-14T00:50:56.591Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /pārak \\[p\\*lk/ {print NR}' NYB_vol2_glossary.txt; echo \"--- page markers?\"; grep -n \"\\[pdf page\" NYB_vol2_glossary.txt | head -3; grep -c $'\\f' NYB_vol2_glossary.txt",
 "description": "Locate Nyberg page for parak"
}
```


## [2026-09-14T00:50:57.778Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT 889 area\"; grep -n \"Schuld\" BRT.txt | sed -n '1,40p'",
 "description": "Grep Bartholomae Schuld"
}
```


### [2026-09-14T00:50:57.866Z] TOOL RESULT

```
166
--- page markers?
293
```


### [2026-09-14T00:50:57.920Z] TOOL RESULT

```
### BRT 889 area
2503:(Y.  j2.  15);   oft  wegselassen,  zB.  Vp.  12.  54  Schuld   und   Strafe    aus  der  Verhandlung
2528:i)  'Strafe'  (nur  Ableit.).  a)  Du.  'Schuld  16;  —  U  gaumillc^  . .  xia>^am  . .  agarbä- und  Strafe':  kö  asti  tkaEsü  *visätö  (sd.)  ?  yata  .  .  '/a*  xsdi''am  .  .  Bh.  /.  11  f ;  — yö  'ta  pairi  ar>>rra  frazänaiti  ".  .    vie.t\yäsaDAa..l>aoi'j7m 'tarn  baoi'jTm  K. 103;  —
3646:Pü.:  dnddtdd.  —  0  Die  beiden  Stellen können  ursprunglich  nicht  den  gleichen  Wort- laut gehabt  haben.  An  der  1.  Stelle  wird  etwa gestanden  haben:  Wer  eines  Verbrechens  be- zichtigt wird  und  leugnet ,  soll  das  Ordal- wasser  trinken.  An  der  2.:  Wer  das  Ordal- wasser  trinkt,  (rolzdem  er  sich  einer  Schuld bewusst  ist,  wird. .  bestraft.  H erste II ungs ver- suche —  von  vornherein  aussichtslos  —  bei Sp.  Komm.  i.  156,  Gdn.  Stud.  i.  103.
4260:•  j.  an-aipi.pär9mna-  Adj.  'der  (seine Schuld)  nicht  begleicht,  nicht  Busse  tut':
8032:•  j.,  g.  iäud'  i  'Schuldforderung',  die  an Jemand  gestellt  wird:  yä  "ds  (NP.)  dadsnU didranqm  (sd.)  hacä  aSäunJ  yasla  .  . ^dr^gvüJibyS  yaiä  ta  aahin  Y.J/.14;  — mazdä  at  möi  vahistn  sraväsUil  y/aeianäcä viioäl  a  tu  voha  manaahä  asäcä  "dim stäls  "o  M.,  tu  mir  die  besten  Lehren und  Handlungen  kund,  sie,  o  VM.,  und, o  Aia,  des  Preises  Schuldforderung"  Y. 34.\%-'^;~  kuira  ta  fryB  ..  tä  -i/j  (NP.) ij  ratayS  (sd.)  bavan  Y.  65.9,
8034:•  g.'J  iäüid'ya-  Praes.31  'der  (göttlichen) Schuldforderung  Genüge  tun,  seine  Schuld (an  die  Götter)  abtragen,  (ihnen)  danken'.
10044:Tmtpaiti  i)  'entgegengehen,  sich  wen- den gegen  — ';  a)  mit  Akk.:  vTsp»m  paiti usanhim  ..hazaaraja  (.y&ssA.dqma)  *ar?rö.~ mainyus{W.)  paiti.Jasaiti  V./ j.i.  b)mit Dat.;  miitvm  .  .  yet^he  hazar»nm  vaFja- nqm  paiti  katmrg'^äi  jasaiti  Yt  W.  69 ;  —  s. noch  Inf.  c)  absolut  'dagegen  angehen, als  Ausgleich  (einer  Schuld)  dienen':  aiia zaokra  palti.jamyat  Y.6S.1.  2)  'zurück- kommen, -kehren  zu  — '  (Dat):  iala  nS abmai  asanbalca  .  .  paiti.jasatö  (3DK.) isaca  ozuitiica  V.^.  54;  55,  57.  a)  ab-
13384:yim  dim  vatnäl  *>vutasyva  (sd.)  vindämm N.  16.  a)  'Ansatz,  Eintrag  in  der  Rech- nung, Buchung"*:  kva  /s(Sp.6i8m.)''Sr(» bavainti  kva  tä  "äru  *pairyeinle  . .  '^ra fairi.bavainti  .."'hra  paiti*/i3njaimte  maiyB astvaititi  arjAvS  havai  urutie  para.daioyäl "vro  finden  die  Buchungen  statt,  wo  werden die  Buchungen  (mit  einander)  verglichen, ,.  zumAbschlussgebracht,..  gegen  einander abgerechnet,  (die)  der  Mensch  immateriellen Leben  fiir  seine  Seele  veranlasst?"  V.  ig. 27;  —  yä  isudS  dadfttt^  ''hranami'  halä asäunS  yäscä  mazdä  *dngvS.d3byB yahä  ta an/wn  "die  Schuldforderungen,  die  auf Grund  der  Buchungen  an  den-4j<ianhänger, und,  0  M.,  die  an  die  Z'rwfgenossen  ge- stellt werden,  wie  die  sein  werden"  V. 31.  14.  Unklar;     ratul    "rauininam
14937:•  j.  paitita-  Adj.  (fem.  =«-),  PPfP.:  s. ^ay.  A)  n.  a)  'Begleich'  von  Schuld und  Strafe:  äa^  jim  il  anya  aya  i'yao%na nSil  fravarsta  'Dm  ahe  nars  yaval'a yavaSataica  "wenn  er  aber  andre  Übel- taten nicht  begangen  hat,  so  gilt  der (Schuld)begleich  dieses  Mannes  für  ,  ." V.J.  äi ;  7.  5a  PüZ.  (aSt)".  b)  Bezeich- nung eines  (nicht  erhaltenen)''  awestischen Stücks*':  'tfm  V.7.S2  PüZ.  (iSt)->.
16017:•  j.  'pira-  m.  'Schuld':  äa^a  masäayasnis ..spayeiti  anäpfrsh^m  syao'hn»m..d)mänB. p^rihtm  'rTtn  "die  m.  Religion  . .  nimmt auch  eine  Schuld  weg,  die  schwere  Sühne erheischt"  V,_j.  41;  F.  jo,  26;  - mudisbm  .  .  ^-ra ''  .  .  ^raSÜakcca  . .  *äst3- raiti  (sd.)  N.  g.
16074:•  g-  (1  ]■)  para^a-  n,  'Ausgleichung,  Sühne (einer  Schuld  durch  Leibesstrafe),  Strafe': para  hyat  ma  yä  mSng  "ää  (NP.)  jimaitt hat . .  "wird,  bevor  noch  die  Bestrafungen**, die  du  erdacht  hast,  eintreten, .,?"  Y.^Äa.
16852:nüt  paiti  i)  'zurückbringen,  wieder  er-  solut 'eine  Schuld  beseitigen  sva.  sie  wieder
21069:"wie  soll  ich  den..  Mann  purifiziren,  wieiPraes.  a  ydta-,    24  yataya-,    30  (Kaus.) die  Purifikation  der  Frau  besorgen?"  "^ .\yätaya-\  Perf.  i  yayai-iyaa-'^. rp.ia.  a) 'Reinigung  von  einer  Schuld  J       i)  'sich  in  Bewegung  setzen',  Perf,  'in
22084:'die  Schuld  einer  Tat  (Gen.)  gerichtlich feststellen,  (Jemanden)  einer  Tat  über- fuhren' :  paoirlm  aitaiSqtn  fyaoitnanqm V3r7zimn»m  nüit  bitim  (sd.)  av<^ia  aita^ altake  yyadhiiak^  yaüa  vag^mti  .  .  aya- nhafnäii  Aantäis  .  .  avaJ.vn'^yät  (sd.) ". .  wenn  sie  die  Schuld  an  dieser  Tat  (bei Jemand)  feststellen,.."  V.i^so;  51—54'.
24129:•  j.  viS-usa-  Adj.  'zur  Überführung  (eines Schuldigen),  zur  Schuldermittlung  dienend, verwendet' " :  'iaSbyasca  sao%räbyS  arüix-
24136:•  j.  vi^Savant-  Adj.  (fem,  'vaiti-)  'die  Er- mittlung der  Schuld  bewirkend',  vom  Ordal- wasser:  äpfm  saoknUavaitltn  taranyävaiilm ..  a/>3ihis  isd.)  ..  V.4.54-
25303:•  j.,  g.  ^rätay-  :  rSiti-  £  1)  'Gabe,  Ge- wälming':  'itf  ..kyat(%'^.  1315  m.)  mlidim *mavai^fm  (sd.)  /radadaha  daZnäbyd  Y. 40. 1 ;  —  tim  haiai  oHi  'ifi  . .  mafyäi yi.  18.  ^{7);  —  Aumrum  'ifi  bartila  FrW. g.  2  (?);  —  ku%ra  tä/ryS  Äawa«(näml,  aot.- büta)  .  .  iä  iütdä  .  .  tä  'tayB  *yam  ahurs mazdä  tara%usträi  /rävavaca  "werden  die Gebete  erfüllt  werden  . .  die  Schuldforde- rungen ■ .  ihre  Gewährungen,  die  . ."  V. 65. 9-  a)  insbes.  'Opfergabe,  -spende': avä  (näml,  vao^amä)  vS  vatmhls  •tsil dangsMasäu!  (sd.)  näla  . .  paitijJndä  Y. 38,$.  a)  'Freigebigkeif:  vainlt  ahmi nmäne  . .  °itii  araiffm  "überwinden  soll  in diesem  Haus  die  Freigebigkeit  die  Karg- heit" Y,  60.  5.         IS.  räitf  als  Inf.  sbes.
29116:•  j.  hada.£t^B-  Adj.  fmask.  °ä(i-)  'der mitzubiissen  hat,  mitbüsscnd':  an'/  saiaih '^anarn  narqm  nabänazdistanqm  para.- baraiti  "mit  dreimal  hundert  mitbUssenden Männern  aus  der  nächsten  Verwandtschaft hat  er  es  (die  Schuld)  wieder  gut  zu machen"  V.  4.  5.
```


## [2026-09-14T00:51:17.677Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"To traffic in, sell\\|to traffic in\\|traffic in, to sell\" AHD_watkins1985.txt | head",
 "description": "Find Watkins per-5"
}
```


### [2026-09-14T00:51:17.720Z] TOOL RESULT

```
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
```


## [2026-09-14T00:51:18.862Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"prek̑\\|To ask\\|to ask\\.\" AHD_watkins1985.txt | head -20",
 "description": "Find Watkins prek-"
}
```


### [2026-09-14T00:51:18.908Z] TOOL RESULT

```
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
```


## [2026-09-14T00:51:36.386Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s):821\\|Page(s): 821\\|Page(s):820-821\\|perk-4\\|perk̑-\\|pr̥k̑\" POK_full.txt | head -20",
 "description": "Find Pokorny 821"
}
```


### [2026-09-14T00:51:36.434Z] TOOL RESULT

```
66488:Page(s): 821 
66528:Page(s): 821-822
```


## [2026-09-14T00:51:38.634Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66440,66532p' POK_full.txt",
 "description": "Read Pokorny 821"
}
```


### [2026-09-14T00:51:38.682Z] TOOL RESULT

```
nspKvoc;, originally "ttoikiAo^', then, dunkelfleckig, dark, blauschwarz', nspKoivsi "wird 
dark'; npOKvov psAava Hes.; flpoKvri 'die swallow'; without -/?- Middle Irish e/r 'mottled, 
speckled, *tabby, oxblood, indigo ', also 'salmon, trout, cow, lizard', cymr. e/r/7 'mottled, 
speckled, *tabby' (= n£pKO(;); Old High German forhana. Middle High German forhe(n), 
forher trout ', Old Saxon furnia. Old English forn(e)6s. {*prk-na), ablaut. Swedish farna^ 
dace ' ( *perk-na)\ 

with -ua Old High German faro. Middle High German vare, flekt. varwer 'iarb\g', 
substantivized Old High German farawa ^ pa\nt, color' {*pork-u6-); Latin-Germanic fario 
'Lachsforelle' (Germanic *farhjdn-, older *farhwjdn-); 

other formations: gr. n£pKO(; m. 'Sperber' (Aristot.), nspKO-nrspoq 'weiftkofige Geierart', 
nspKQ^si 'wird dark, black'; np6^, -K6c,i. and npoKOc;, -aboo, 'Hirschkalb', npcb^, -Koq 
'Tautropfen'; nspKr) (Latin pe/ra loanword) ' perch ', Latin porous 'e\n fish with 
Stachelflossen', Ligurian FIN Poroo-bera{' trout iu\r\ren6'); Middle Irish c»/r(and ero, see 



above) "salmon'; Old Icelandic fjgrsungr'trach'mus draco' {*perks-nk6-); redupl. perhaps 
nanpa^ ein thrak. sea fish ('trout?'); 

perhaps here through Diss, eines *perk-ro-s\o *pelcro-, *po/cro-: Latin pulc(h)er. Old 
Latin yOC»/c/7e/''beautifur (= "varicolored'). 

References: WP. II 45 f., WH. II 384; 
See also: extension from per-1. 
Page(s): 820-821 

Root / lemma: perR-3, pfR- 

Meaning: to tear out, dig out; furrow 

Material: Old \nd'\c parsana-rc\. 'cleft, gap, abyss, sinking in '; 

Latin po/ra "furrow in farmland', "Wasserabzugsrinne in farmland' {porcu-/etum ' a field 
divided into beds' mars. Umbrian ^ porcu/eta'); cymr. rhych 'furrow' (with expressive -kk) 
perhaps = bret. rec'h^ distress ', against it with /rabret. rec, gl. 'suico', ro-ricse[n]ti 
"sulcavissenf; gall, /vica "furrow', French As/e 'stripe'; Old High German furuh. Old English 
furht "furrow'. Old Icelandic fori. " drainage ditch, canal' {*prk-)\ zero grade Norwegian 
ferexu. "a field divided into beds'; after F. R. Schroder, Festgabe K. Helm 25 ff. here Old 
Icelandic Fjgrgyni. as "goddess the Ackerfurche'; 

Lithuanian pra-persis^E\av\ke in ice', pra-parsas^ 6\\.c\\, trench, channel', persetT 
burning ache' (from Wunden); 

in addition */7c»/';^d5 "swine' ("WiJhler'). 

References: WP. II 46, 47, WH. II 340 f. 
Page(s): 821 

Root / lemma: perti-4, preR-, pfR- 
Meaning: to ask, ask for 

Material: 1. 5/^o-present *prk-skd, worfrom *prskd:0\6 Indie /C>/rc/75//"fragt', Avestan 
parasa/t/ Iragt, longs for' (participle parsta-), ap. aparsam^\ frug'; Armenian e-harc^he 
has gefragt' (: Old Indie a-prcchat), therefrom das present harcanem, Latin posed "ford ere, 
demand, beg '; Irish arco^\ beg ', cymr. archaf, corn, arghafds., Middle Breton archas'W 
commanda' (Old Irish //77/77-c/7c»/77-a/r"gegenseitiges Fragen, Begrijften' etc.) with ariromr 
before dem 5 the basic form *prskd {irom *prk-skd)\ Lithuanian persu, yO/?s//"forjemanden 
freien' (yO/As/ys "F re i we rber'), if with analogical present-ablaut e instead of r, in addition Old 



Indie /C!/rc/7a "question, Erkundigung' = Armenian hare 6s:, Old High German forsca 
"Forschung, question' is post-verbal to forscon^ inquire, research'; Latin postu/dlor6ere' 
(diminutive of participle */0C»5c/c»s to yOC»5cd);in Oscan-Umbrian is *porscd\.o *persc6 
reshaped: Umbrian persnimu\'(r\'^e'c. Med. 'precator', in addition with (forms -(e)lo-) 
Umbrian persklu, pes/r/i/ "supplicatione', further mars, pesco'sacrificum', and of participle 
*pes[c]to-ixor(\\ Oscan pestlum, peeslum ' an open place for observation, place marked off 
by the augur's staff ', from which Messapic hevokAev "Bethaus'. 

2. Old \v\6\c pra's- "(gerichtliche) Befragung', Avestan frasai. 'question'. Old \v\6\c prstha- 
(= Avestan parsta-) 'Gerichtsfrage', prasna-, Avestan frasna-m. 'Befragung, question' (= 
Old High German fragan' woodpecker ' KZ 62, 31, 2), Armenian harsn 'bnde, newlywed, 
daughter-in-law ' (compare Gothic frafhnan); Latin procus ' suitor ', prexi. 'request', 
precor, -a/7"bid, beg, ask', Umbrian pepurkurenfi. PI. Fut. 'poposcerint'; Gothic frafhnan^ 
inquire ', Old Icelandic fregna. Old English /^/g/7a/7(and„/b-present fricnan) ds.. Old Saxon 
preterit fragn. Old English friccea^ herald '; Germanic *frehti-\v\ Old Icelandic fretti. 
'question, Erforschung', Old English frehtt 'Wahrsagung'; Old High German fraga 
"question' {*frag-dn, -en, frahen^ inquire '), Old Icelandic frsegr. Old English ge-fraege. Old 
Saxon ^/-/^a^/' illustrious'; ablaut. Old High German /e/p'd/7'bid, beg, ask'; Old Icelandic 
prositi^b\(i, beg, ask'; 

Maybe alb. poros/t' order, demand' a Slavic loanword. 

Lithuanian Iterat. prasau, -y// "arrogate, bid, beg, ask'; Tocharian k prak-, B prek-' inquire ' 

References: WP. II 44, WH. II 346 f. 
Page(s): 821-822 

Root / lemma: pericu-s 
Meaning: oak
```


## [2026-09-14T00:51:50.984Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KNT parsa/aparsam\"; grep -n -i \"aparsam\\|pars-\\|frašta\\|frasta\\|frath\" KNT.txt | head -30",
 "description": "Grep Kent for OP pars-"
}
```


### [2026-09-14T00:51:51.032Z] TOOL RESULT

```
### KNT parsa/aparsam
595:frastam in u-frasiam u-frastam, pte. to root seen in Lt. precor, keeping strong-grade vowel.
921:*su- ‘good, well’, OP u-frastam, Skt. su-, Gk. b-yens ‘healthy’.
1027:П. OP f from pIE р before consonant: pIE *pro, OP fra- as prefix, Skt. prá, Gk. тро. pIE *prek- in OP pte. u-fraštam ‘well punished’,
1207:ійѕра-, see Lex. s.v. pIE *prek-to-, OP *u-frasta- ‘well punished’; for
1211:' u-frasta-, varying with "u-frasta-, see above.
1337:pIE *su-prek-to-, OP ufrašta- ‘well punished’, cf.
1534:*prek- in ufrastam ‘well punished’, *prk- in aparsam ‘I punished’.
1604:aor. niy-aparsam to pIE root *peik-; §102. pIE sir (after u) > pAr. sr > plr. #т > OP
1636:(3) plr. change of p tk to f 0 x before con- sonants ($74.D): рага but fra-, aparsam but -frastam, tuvam but ace. ийт, akariya but cazriyü, drauga adurujiya but duructam.
2075:айа DB 1.28, XPh 49, 52, when used with pari-ay- ‘respect’, is probably inst. rather than abl., because of the lack of prep. Ласа; note that the text of DSe 37-9, as now restored, gives no support for the abl. in the other passages, despite my remarks JAOS 54.46, Lg. 13.308, JAOS 58.117. On inst. sg. karšā, loc. sg. karšayā, nt. асе. casam, acc. pl. ufrasta-diy, see Lex. s.vv.
2445:pIE *prek-, pres. *prk-ske-, OP parsümiy ‘I pun- ish’, Skt. prechami ‘I ask’; imf. OP aparsam, Skt. dprecham; imv. OP parsd, Skt. prechd.
2528:I. The Sigmatic Aorist is seen in niy-aparsam ‘I inscribed’ (or -apiSam?)}, to root pai8-, pIE *peik-; in mid. adarSiy ‘I held’, to root dar-, pIE *dher-; perhaps in pass. -asahya in frasah[ya]. The aorist endings 3d sg. -s-t, pl. -s-nf, may also be respon- sible for the endings of @1$ -diSa" to root ay- (8208); akunaus akunavasa to kar-; adurujiyasa to durujiya-; abaraha to bar-.
2563:II. The secondary ending - was attached di- rectly to the thematic vowel -o-: pIE ebhero-m ‘I bore’, Skt. dbharam, Gk. éepor, OP abaram; Skt. dpyccham, OP aparsam. Other OP examples: niy- asddayam, franayam, arasam, etc. When attached to non-thematic stems, the -m became vocalic, and developed in pAr. to -am, a generalization of the antevocalic value, furthered by the identity
2634:but OP u-frašta- u-frasta- ‘well punished’ (where
3479:22 bartam : abaram : hya : апка : аһа : avam : ufrastam : aparsam : vašnā : Auramazda 23 ha : ima : dahyáva : tyanà : manā : dita : apariyàya : yaðāšām : hacima : абаһ
3832:38 patipayauvi : martàya : hya : draujana : ahatiy : avam : ufrastam : pars : ya
3857:63 yàha : bagitha : tyaiy : hatiy : yaf : палу : апка : Sham : пау : draujana : арат : na 04 iy : zürakara : &ham : поту : adam : поталу : tauma : upariy pev omis ~ 65 yam : naiy : škaurim : naiy : tunuvatam : züra : akunavam : martiya : һуа : hamata 66 xšatā : manā : vityà : avam : ubartam : abaram : hya : viyanüfaya : avam : ufrasta 67 т: aparsam | : фу : Юйгауауац$ : xSayafiya : tuvam : К : xšāyaðiya :
3885:%A blank space of one character between the di- vider and the following @ #, KT. 2 [akunavam] WB, KT; but KT state that the traces of the last letter are pos- sibly those of &, which leads to a restored akunauS (во also RL), of which Auramazda would have to be the implied subject (ef. Oppert’s restoration, IdA 150). It is more probable that the phrase is here as in DB 5.17, 29, 38, and that akunavam is correct. ? ah*y^ RL, KT; first correctly normalized ёлу by Tm. VS 1.30. So also 4.68, 72, 87. 9 ufraštam КТ. ? manfiydhy} Opp. МА, ete., KT; man(iyahay) Tm. after DPe 20; man[ryáhaiy] Kent, since there is no reason to assume here the defective writing of DPe. |
3889:Маг ат Foy KZ 35.45 (conj.), Jn., KT, for КІ в in- correct, abiStam. 9*5 Definitive жи е by Cameron, upariy | dlyalm [:] пабу : Sakaurim : naty : t[u]nuvatam, confirming uparty[üyam] of WB, HK, Wb. KIA; Sakaurim WB, Jn., fakauri[m] KT, Tm., Wb. KIA (read rather Skaurim, see Lex. s.v. skaudi-); [nay] Spiegel; ... uvata Rl., ]nuvatam Jn., t{ulnuvatam KT. ® zuku RL, züra Ri. later.  hya WB (from Rl.'s squeezes), Jn.; omitted by KT. #06... ВІ; 2076 WB, Jn; 090 KT. 6 piyaná[sa]ya WB, KT, HK, Tm., Wb. KIA; correctly viyana\balya Foy KZ 35.46. “avam : ufrasta- WB; wrongly ava : ufrasta- KT. ® [zu]rakara : ++ : KT, with possibly traces of two characters in the gap; but, Cameron finds [zuü]rakara : ahat- with only а gap for опе
3891:character, perhaps miswritten and erased, after the divider. * daustà WB, KT. 9 ...à KT; biylà WBn, НК, Tm. © atifraštādiy RL; aifrastádiy WB, Jn.; ufrastadvy KT.
4201:1 adam : Dārayavauš : XS : vazraka : XS XSyan 2 ат : XS DHnàm : Vistáspahy& : риса : Ha 3 xümanifya : 08у : Dàrayavaus : XS 4 : vaSnà : AMha : adam : ava : akunavam : tya : 5 akunavam : visahyà :frašam : Oadayataly Note то DSa: * frasam : 9adayátaiy, Hz. ApI 156-8, for the previously accepted frasia : 0adayámaiy; but Hinz, ZDMG 95.223-5, supporta a[dam : visa]hyà : frašta : @адауйтаїу. TRANSLATION OF DSa: 1. 1-3. Tam... (= DPa 1-5). $2. 3-5. Saith Darius the King: By the favor of Ahuramazda I have done that which I have done; to every one may it seem excellent.
4316:Notes то D§j: * [paruv}iyaba naiy ‘nicht in einem einzigen Anhieb�� Brd.; [пратш)|туаба naty ‘wie nie zuvor’ Hz. Api 103; [+++-+]:yaa@ тату ‘nicht planlos’ Hinz, ZDMG 95.240-1. € frasam ðadayāļtaiy}) Hz., аз in Da 5, q.v.; frasta Gadaya{maiy} Scheil, supported by Hinz, ZDMG 95.224.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5189:ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
5699:fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
5709:fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
5710:frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
```


## [2026-09-14T00:51:52.394Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT frasa\"; grep -n \"frasa-\\|frasna-\\|paiti\\.frasa\\|paitifrasa\\|frdsa\" BRT.txt | head -30",
 "description": "Grep Bartholomae frasa"
}
```


### [2026-09-14T00:51:52.450Z] TOOL RESULT

```
### BRT frasa
17767:•  j,  frayäi  Inf.  'vorwärts,  weiter  zu  gehen', mit  frasa-.  nStt  dim  bitlm  väHm  faiü.piri- sirnnB  h'a  (Sp.  929  u.)  frasa  fr'  vahishm a  aium  d  ".  .  stracks  soll  er  weiter  gehen zum  Paradies"  V. /Ä29.
17890:•  0->)  g-  frasa-  m.  i)  'Frage'  (nur Komp.).  2)  'Zurateziehen,  Erforschung, Studium'  (nur  Komp.).  3)  'Gericht, Strafe',  nur  IS.  'sa  mit  V,  Jras- "'  'etwas bestrafen.mitStrate ahnden':  yä  'sä  avTsyä yä  v3  maadä  *pir3saai  tayä  "welche  offen- kundigen oder  welche  geheimen  (Taten), o  M.,  mit  Strafe  geahndet  werden"  Y. j/.  i3'>.
17975:frasa-
18812:Pn.:«ufli™.»rf  •  J-  nasko.frasa-  Adj.  'der  Erforschung.
19696:•  j,  mat-paiti.frasa-  Adj,  (fem,  'sa-)  'mit den  Antworten  versehen,  sammt  den  Ant- worten': gä'hi  .  .  'sa  Y.57,  8.
```


## [2026-09-14T00:52:02.615Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5600 && NR<=5720' KNT.txt | grep -n \"^\\s*1[0-9][0-9]\\s*$\" ; echo \"--- form feeds before line 5699:\"; head -5720 KNT.txt | grep -c $'\\f'; echo \"--- context\"; sed -n '5690,5700p' KNT.txt | cut -c1-200",
 "description": "Locate Kent page for frath-"
}
```


### [2026-09-14T00:52:03.708Z] TOOL RESULT

```
86:197
97:198
--- form feeds before line 5699:
219
--- context
Putéya- adj. ‘man of Put, Libyan’ (§75.V, $/6.V, §144.HI); pl., ‘Libya’, a province of the Persian Empire (Cameron, JN ES 2.308-9) : Elam. pu-á-ti-ja-ap, Akk. pu-u-ta (Lg. 18.299, 15.165).
puça- sb. ‘son’: Av. puéra-, Ars. РЬ. рим, N Pers. pus, Skt. pulrá-, Ose. puclo-, рї *putlo- ($64, §75.1,§78,§148.1II). pucansm. AmH 3; AsH 4; CMb 2°; DB 1.8, 28, 39, 53, 74, 78, 79;
farnah- sb., see Vidafarnah-.
fra- prefix ‘before, forth’ (as prep., not found in OP): Av. fra, Skt. pra, Gk. тро, Lt. prü-fessus, Gt. fra-, pIE *pro ($33, $01, $75.II, $106, $132.3). Found with verbs а1$-, jan-, nay-, va
fratama- adj. ‘foremost’: fra- + superl. suf- fix -lama-, Av. fratama-, Skt. -tama- (4190.11). fratama npm. DB 1.57; 2.77; 3.48f, 51, 74, 90°, 91.
fratara- ad). ‘prior, further’: fra- + comp. suf- fix -tara-, Av. fratara-, Skt. adv. pratardm, Gk. mpotepos (§106, 5190.11). " fratara ism. DNb 38 (Sen 249 needlessly takes as error» for fratar
198
frataram asn. XPg 11; adv. ‘previously’ DB 3.26, A!Pa 21.
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. posc
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl
```


## [2026-09-14T00:52:14.164Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^17[4-8]$\" KNT.txt | head",
 "description": "Find Kent page 176 marker"
}
```


### [2026-09-14T00:52:15.189Z] TOOL RESULT

```
5125:174
5165:175
5173:176
5210:177
5220:178
```


## [2026-09-14T00:52:17.283Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5173,5210p' KNT.txt | cut -c1-300",
 "description": "Read Kent p.176"
}
```


### [2026-09-14T00:52:17.334Z] TOOL RESULT

```
176
Gk. 'Ürávgs; perhaps u- ‘good’ + tāna- to root tan- ‘stretch, extend’ (§164.II), Av. Skt. tan-, Gk. telve, Lt. tendit, cf. Skt. tdna-m ‘offspring’: ‘Hav- ing good posterity’. [апа] nsm. DB 4.83.
utava- adj. ‘strong, in health’: u- ‘good’ + deriv. of tav- ‘be strong’ (§122). utava nsm. DB 4.71f (emendation of HK, ApKT 1.63, 2.29, for KT’s detse, with first and third characters very faint; $541).
ubanuvaniya- sb. ‘good bowman’: u- ‘good’ + Sanwaniya- ‘bowman’. wudanwaniya nsm. DNb 42.
ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
ира (i.e. upd, cf. 5140.1) prep. and prefix ‘to- ward’: Av. ира, Skt. úpa, Gk. iad, Lt. s-ub ‘under’, pIE “иро.
(1) Prep. with acc., ‘under, with, m the time of (hardly ‘belonging to’, as taken by Hz. ApI 353): DB 2.18, 3.30; A’Sa 4; А?Ра 23; Sf.
(2) Prefix, ‘under’, in Upadarma-; ‘toward’, with verb ay-; ‘beside’, in upasia-.
Upadarma- sb. ‘Upadarma’, father of Agina: Elam. uk-ba-[lar|-ra-an-ma. From ира + darma- (root dar-), Skt. dhérma- ‘right conduct’ (§163.V): “Не who is under (= behaves himself according to) right conduct’ (so Bthi. AiW 390, with lit.; hardly Upadara"ma-, after the Elam.; hardly a
upariy adv., prep., prefix, ‘above’: Av. upairi, Skt. upd, Gk. тёр, Lt. s-uper, Gt. ufar, pIE *uperi (5191.1). (1) Adv. ‘above’, XPh 31. (2) Prep. with ace., ‘over, over and above, upon, according to’: DB 4.64; DNb 4, 32, 46, 49; DSf 27. (3) Prefix, ‘over’, with verb ay-.
upasté- sb. ‘help, aid’: upa- + verbal root slà- (6140.1, $142), ef. Gm. Bei-stand for meaning. upastém asf. AmH 10; DB 1.25, 55, 87, 94; 2.24f, 34, 40, 45, 54, 60, 68, 86, 97°; 3.6, 17, 37, 45, 62, 67, 87; 4.60f, 62; DPd 13; DNa 50; DSf 19°; DSk 5; XPh 32, 45.
Ufrütu- sb. ‘Euphrates’, river of Babylonia:
OLD PERSIAN
Elam. t-ip-ra-tu-i8, Akk. purattu, Gk. Еўфрат
(§75.V, §76.V, §166, $166.II). Etymology un. |
certain, probably a popular etymologizing in OP of a local non-Iranian name, cf. Bthl. AiW 1830; Fick, ВВ 24.310; Justi, ТЕА 17.116; Tm. Lex. 77, Ufrätwā ism. DB 1.92 (not gen., as taken by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + p
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
watpasiya- adj. ‘belonging to self’ (wrongly ‘wayward’, Sen 246), nt. as sb. ‘own possession’: Ау. x’aépaibya- ‘own’; OP uvai-, nom. of wa-, as in Skt. svay-dm ‘self? (MB Gr. §293), + pAr. *natia-, formed on pIE *poti-, Av. рой ‘master, husband’, Skt. pati-, Gk. тос
 wüipasiya-, same as preceding, with vriddhi in initial syllable (§126; MB Gr. §298); but wai- may be an error for uvai-, or wai- for wäi- (§53). uvdipasiyam asn. DB 1.47.
‘UvaaStra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-tš-tar-ra, АКК. ú-ma-ku-iš- lar, Gk. Kva£ápys. From u- ‘good’ + varštra- ‘growth’ ($9.11, $79, $148.11), to vaxi-, Av. vazš-, Skt. vaks-, Gm. wachsen, N Eng. wax ($102): 'Hav- ing good growth’ ($164.11, IV). So В
Uvaja- Uvajiya-, read Uvja- Uvjiya-: see Uja- Ujiya-.
wadd- sb. ‘abode’, vriddhi-form to Skt. svadha- ‘innate character’, from wa- ‘own’ + dhà- ‘make’ ($142; OP wa- + ?dà-) ; in PaiSiyduvdda-, q.v.
Uvadaicaya- sb. ‘Uvadaicaya’, a town in Persia (§159): Elam. ma-ie-gi-i& Uvadaicaya nsm. DB 3.51.
uvamar Siyu- adj. ‘(having self-death = ) dying by one’s own hand’, either by intent or by acci- dent: wa- ‘own’, with vriddhi, + *mptiu- ‘death’, Av. marabyu-, Skt. mptyii-, to mar- ‘die’ (S30, $80, 8113, §122, §126, $152.1II, §153.1, $161а); used of Cambyses, who, acc. to Her
177
```


## [2026-09-14T00:52:30.292Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v1 pdf page tags sample ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo \"=== search پاره ===\"; grep -n \"پاره\" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan vol1 for pareh"
}
```


### [2026-09-14T00:52:30.361Z] TOOL RESULT

```
=== v1 pdf page tags sample ===
=== search پاره ===
1956:وهفت کلمه ازین قبیل کلمات نداشته باشد . پاره‌ای باشاهدی ازنظم و سضی
2486:* فرهنگگ نطامی ۰ مشتمل برپاره‌ای از لفات و کنابات نظامیکنجوی؛ تألیف وحید
6534:۵ آقشیبرزیی - رك: آندبرزین  .‏ 5 آلش پاره - اخگرکرم شب‌تاب - مجازاً مخت جانی
9000:اکردیده بگردون بر کمارد زسهمش پاره پاره کردد آور
10098:(ه) بدست سلمانان اقاد وآنرا باره پاره کردند
16022:است؛ ون پوست پاره‌ای باشد مهو رکه رسمالی
16847:«بازبرة اول وبازبر؛ آخر» » مراد از آن پاره‌ای
18147:و پاره هم حست برقبا و خرقه و امثال آن .
18349:بیعنی پاره و حصه و بهره - و لخت و بعض
18382:بر 4 ۲ « بروزن چرخه . بمعنی پاره
20708:ثانی و فا و دال امجد » رشوت و پاره را دود »
20712:رشوت و پاره باشد .
21231:ازخرمن غله وکاه وضرمب وحم انی واظ پارهای
21299:امجد . پمعتی رشوت وپاره باشد ۴ .
23071:و پیش ازین باشد ۷ - و «خفف پاره هم هسنت -
23190:پاره بر وژن چاره . ممروف است
23199:ژاده هم هست چنانکه گوبند «مخدوم پاره» بعنی
23218:دلم‌را باره کرد آن‌پاره کار. نظامی کنجوی ً
24305:پاره‌ای از خمیر باشد که بجهت بك نه نان گرد
24811:و پاره ولخت باشد -- و پینه ووصله رائیز گویند
```


## [2026-09-14T00:52:34.167Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23180,23230p' BQT_v1_pages.txt; echo \"=== page marker style ===\"; grep -n \"page\\|صفحه\\|^\\s*[0-9]\\{3\\}\\s*$\" BQT_v1_pages.txt | sed -n '1,10p'",
 "description": "Read Borhan pare entry"
}
```


### [2026-09-14T00:52:35.317Z] TOOL RESULT

```
. که بشاعران و مطربان و امثال ابشان دهند
تا درجشن و میزبانی حاضر شوند- وزریرا گویند
که باجرت فاصدان دهند .
بار نجی ؟ - بر وزن آ کندن » میل
۳ ۲
بادو با وار مجهول بروزن جارو ,
پیر ذال و زن پیر را گوبند - و ببل مانتدی
باشد از چوب که بدان برف بروند؟ ,
پار وب بر وژن جاروب ۰ بیعنی‌پازو
است که زن پیر - دییل چوین باشد .
پاره بر وژن چاره . ممروف است
پر کار
که در مقابل درست باشد» وبسربی فطمهخوانند
و گرزآهنن را هم کفته‌اند - و رشوت دا یز
گوبند - وبمعتی تحفه و ثبرك حمآهده است -
و نوعی از حلوا باشد که بشکر باره مشهور است
- وپربدن و پرواز کردنراهم کفتهاند - وجزو را
نیز گوبند که جمم آن‌اجزا باشد6 - ونادوشیزمرا
هم گویند که دختر بی بکارت باشد - و بمعنی
ژاده هم هست چنانکه گوبند «مخدوم پاره» بعنی
مخدوم زاذه - و بزبان رومی زری است که در
همان ولات در ایح است. و بپندی صماب‌وزسق‌را
گویند .
یاراد ه با عیزه بالف کشده
و برا و دال بی نقطهٌ زده . آش آردی است که
باوماج شهرت دارد. و آنرا بقدر کندمی آززخمیر
سازند و یز ند .
بارهٌ زرد ۳ بفتح‌زای نقطمداروسکون
را و دال بی نقطه » پارچه زردی باشد که‌بهودان :
برای اهتباز بردوش‌جامه دوزند» وآغی! بعربی‌غیار
وغباره خوانند
یاره کار ه باکاف بروزن لالعزارا ,
۴ - رك : پا اورنجن .
۴ دریهلوی
رشضدی شا هدن ملر ً 1 ‌ ده است:
و شاپور آمد اندر چارژ کار
۵ - < ورا (علم
۲ - صاحب فرهنگ
دلم‌را باره کرد آن‌پاره کار. نظامی کنجوی ً
بقه ازصفحة ۳۵۰
ه پارسی باستان ‏ بافری حخامنتی
بافرس‌قدیم» مکی‌از زبانهای ابرانی است که درعپد عخامنشیان» زبان‌رسمی ایران‌بوده وآن بااومتا
و سانکربت شباهت تام‌دارد و کنیبه ه‌ای‌هضامنشبان‌وبرخی ظروف ومهرها بدین‌زبانوبخط میخی
حضاننشی نوشته شده‌است. رك : مقدمه کتاب حاضر .داریلب ْ ۱ 4 ۲و
بمعنی جزئی باشد که دربرابر کنی استوپاز تاربان
بمعنی جزئیات؟ .
یازج با زای فارسی بر وزن‌آز رخ
تممنی مالش وان باشد۷ .
پارش بکرزای‌هوزبروزن خواهشی»
کیاه و علف ژبادتی را از مان غله زار کندن
ودور افکندن باشد» همحئانکه براش شاخهای
=== page marker style ===
133:خ مسیمت مصت ‏ سسسسست خن بت پوت وت بت سسصفحه 7
897:با میکنيم : بقیه در صفحهٌ ۲۵یست وینج زبانهای ایرانی
922:بقبه از صفحهٌ ۲6
1884:۲ - مولف انجمن‌آرا وشته : مه در حاشیه صفحه مدپنجاه ونه دسانیر
1892:بقبه ازصفحهٌ پیش
1942:است در دومجلد ضخیم تقریبا در دو هزار صفحه نیم ورقی درسال ۱۱۵۵
1955:و در نظم ونر قدیم وجدید مانیست و کمتر صفحه‌ایست که از يك الی شش
2031:نسخه‌ای خطی من دارم شامل ۵۳۰ صحیفه بفطم پنج‌صفحه ای بخط
2820:بفه از صفحهُ هشناد وش ۱
2863:فرهنگها ودارای متجاوزاز ۷۰۰۰ لفت است [رك: ح ۲ همین صفحه | بعتی نه برامرلفت فرس
```


## [2026-09-14T00:52:52.068Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== پادافراه ===\"; grep -n \"پادافراه\\|پادافره\\|بادافراه\\|بادافره\" BQT_v1_pages.txt | head -20; echo \"=== پرسیدن ===\"; grep -n \"پرسیدن\\|پرسش\" BQT_v1_pages.txt | head -20",
 "description": "Grep Borhan for padafrah and porsidan"
}
```


### [2026-09-14T00:52:52.157Z] TOOL RESULT

```
=== پادافراه ===
16027:بادافره ۲ - بحنف الف سیم ()
=== پرسیدن ===
1126:وص ۰6 4- امتاد هنینکه در جواب پرسش نگارنده شفاهً شفاها
7509:هم هست . گویند از حکیمی پرسیدنکه‌چندین
16066:۳۵۷-2 . جزو دوم مشتق از ۳85] همربشه و بمعنی پرسیدن « پیب رگ ۱۷۹ جمماً بسنی
18503:صژال کزدن و پرسیدن باشد . #
18958:از سب آن پرسیدند . سلیمان کفت این شخص
18965:حنا رکیفیت حال از جعفی پرسیدند . جوام‌داد:
19529:پرسش ۰ بممنی مقابله باشد که در برابر مقارنه
```


## [2026-09-14T00:52:58.831Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16000,16075p' BQT_v1_pages.txt",
 "description": "Read Borhan badafreh entry"
}
```


### [2026-09-14T00:52:58.887Z] TOOL RESULT

```
از هرماه شمسی باشد و ندییر و مصالح آن روز
پدو تعلق دارد . نك است درین‌روز نوبر‌مدن‌ونو
پوشیدن و براسب نو سوار شدن ۴ - و کنابه‌از
حدف و سخن هم حست - و بمعنی ابود و هیچ
باشد - و کنابه از تندو تیز هم هست - و منح
و ثنا را نیز کوبند - و بمعثی آه وناله هم آحده
(۱) چك : دوم .
است - و نام کنج دویم (۱) است از جملةٌ هشت
خسرویرویز و کنج بادآوردهمین است ؟ -
و بمعتی‌لخوت رغرور وخودیینی هم هست سوأسب
را نیز گونندکه بعربی فری خوانند - و بمعنی
شراب هم بنظ آمده است - و مخفف یاده
باه] بله س بل حلاك کننده را گویتد
باذاد نگ * - بننعرای‌فرشت‌وسکون
نون وکاف فارسی » ترنج‌را کویند و آن‌میوه‌ایست
معرو ف که‌پوست آنرا مرباسازند وآنرابادابنگه
حم میگوه مد . ۶
باداش « بروژنآ دای » مکافات وجزای
نیکی را گربند» وبابای فارسی هم آمدماست ۷ -
باد] فر اه ۲ - بافا و رای قرشت بوزن
آرامگاه ؛ بمعشی عقوبت و جزای کناه و مکافات
بدی باشد و بادفر را نیز کوین که بازییلاانال
است؛ ون پوست پاره‌ای باشد مهو رکه رسمالی
درآن گذرانند ودر کشا کشآ ور ند تابکردش‌در] مد
و صدابی از آن ظاهر شود ۸ .
پادافر اه ۲ » بروزن ماءدر عاه ,بمعنی
بادآ فراء است که جزا ومعافات بدی‌باشدد ویاژمسةً
بادافره ۲ - بحنف الف سیم ()
اطفال باشد ۸ . ۷
ضه درصفحً ۲۰٩‏نکن مم ینظر آعده است ٩‏
ادا فنجیر - نومی از درخت انجیراست
که یش از هم درختان موه دهد و انجیر آن
کاواك و پرباد میباشد .
بادان‌فیروذ - نم خهرآردیل است
و چون فیروز آن شهر را بنا کرد باین نام‌موسوم
ساخت چه بادان بممنی آبادان است.؟ .
باد) نگیز » نام کلی است که هر گاه
مزارعان خواهن که غله را از کاه جدا کنندو باد
نباشد آ نگل را بدست مالند و بر ک آنرا بر
هوا یاشند باد بهم‌رسد .
بادآ وود » نام کنم دوبم (۱) است
هشت کنج‌خسرءپرویز سد ی 5 زر
و گوهر بیکی از جزایر حصنه میفرسناد انفافاً
باد کشتی را بحوالی اردوی خسرو پرویز آورد
بادام شکوفه فشان - کنابه از
بادامه - بفتح میم ۰ یله ابریشم را
8 شتر هم آمده
است - و چشم مانندی باشد که از طلا و نقره
سازند و بر کلاه طفلان دوزند - و خال گوشتی
را هم گفته‌اند ۰ و آن اژخ مانندی است که‌بیدتی "
از بشر؟ میدم برمیآبد - وهردانه و حلفلزنجیر
را نیز کوبند - و رقعه و پینه را نیز گوین که
درویشان برخرقه دوزند - و خرفةٌ مرفعه را هم
میگوند » بعنی خرقه ای که ازیاره های رنگین
فراهم دوخنه‌شده باشد - وجنسی از ابر شمباشدب
و هرجنس مطبوع را یز کفته‌اند .
بادان - بر وزن نادان . مخفف آبادان
است که‌شیض‌خراب باشد - وبمعنی پاداش‌وجزای
۱ - باین ممنی ظاهرا مصحف «پاداش ‏ پاداش» است . راك : باداش . ۴ - ور
ممجم‌البلدان «باذان‌فیروز» ونیزدرمتن‌برهان وسروری *فیروز گرد» ودرثاهنامه «پیروزرام*» وقولی
بادان‌پیروز با آبادان پیروز نام قدیم اردبیل است که فیروز ساسانی در فرن پن<م میلادی آثرا بنا
کرده است «دائرتا لمعارف اسلام : اردیل».
بقیه ازصفحهٌ ۷۰۵
این روزرا «باد» خوانشد . «روزشماری ۵4-۵۳ . ركك : روزشماری ص ۸۲
۴ - رك : بادآور . ٩‏ طبری ۷2۲208 « واژه نامه ۶۷۷۶ گیلکی و
رك : بادرنگ . ۱ رد : پاداش. ۷ - بهلوی 02111725 (یادانی) م رکب از
۳۵۷-2 . جزو دوم مشتق از ۳85] همربشه و بمعنی پرسیدن « پیب رگ ۱۷۹ جمماً بسنی
بیرسیدن ۰ بازخواست . ۸ رگ : بادفر .
٩‏ که از يك کناه ار برفنم زراه
فتادم بباد افرءٌ تک اد اسدی .
#ادای _ آی(آسیا) که با بادکردد. (مر کب از:
باد ۳- آی راك : این‌دو کلمه ] )
» #دام ‏ پپلوی ۷2۱۵۲0 < اوبوالاء؛ ». ۸۳۷۵02105
درختی است ازدستة بادامی ها از بر گل سرخبان. عفز هستهٌ
آن که درشت میشودکاهی تلغ و در بسضی از جنس ها شیرین
استِ « کل کلاب ۰۲۲۹ « فرهنگ روستابی۲۲۹» «ثابنی۱۹۵*.سب ۰ ۷ --
```


## [2026-09-14T00:53:21.937Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>23190 && NR<28000 && /پرس/ {print NR\": \"$0}' BQT_v1_pages.txt | head -30",
 "description": "Search pors in Borhan after pare"
}
```


### [2026-09-14T00:53:23.068Z] TOOL RESULT

```
23278: صنیغات‌ابراهيم زردشت"۱ در آبینآتش پرستی»
23931: هاقیفن * » بروزن ساییهن . بمضنی‌دو پایین پرستی - کنابه از اطات
24673: پرسا! - بضم اول وسکون ثانی و سین
24674: بی نقطه بالف کشیده » خبر کیرنده وپرسنده را
24676: پرستنده و پرستار باشد؟ - وشخصی رالیزگویند
24679: پرستار ۴ - بر وزن طلبکار » خلام
24683: «بودکی ۱۱۰ » رك : پرست و پرمتیدن . .
24687: ۱ پرسنندث خبال
24690: پرستادان خبال ه کتابه از شرا
24692: پرستش! « بکس دابع و سکون‌شین
24696: پرستاث ۷ - کر اول وتانی‌وسکون
24701: پرستندة خیال - کنابه از شامر
24702: و منشی باشد و پرسند خیال هم آمده است که
24718: الك و ضم فوقانی و واو ساکن . بمعنی پرستكث
24719: است که خطاف‌باثد , وپسنی کویندپرستو وطواط
24721: پر ستو ۴2 - بسکون‌کاف.بسعنی‌پرستو
24723: پرستوك را بگیرد وقتی که ماه در افرونی بود
24728: اکر دو پرستواه بگیرند یکی نر و یکی ماده
24739: زنی خدمتکار باشد؟ - وبفتح‌اول وثانی‌پرسنیدمرا
24741: پرسق منم اول و ثاك و سکون
24746: پرسم ع منم الث بر وزن کندم .
24775: پرسیاو شان ا بالف ونون بسنی
24926: کفته‌اند۵ - ونام پرساوه‌شاه‌نیز هست «وباینمعنی
25167: است - و بمعنی پرستش و پرستیدن هم آمده
25173: پروردن - و پرسنش و پرسنیدن باشد - و کتابه
25414: کرده باشی ازو بپرسی جواب کوبد و تعبیر
26218: بی‌نقطه وضم فوفانی وکاف ساکن؛ پرستو باشد.
```


## [2026-09-14T00:53:26.927Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24660,24700p;24735,24800p' BQT_v1_pages.txt",
 "description": "Read Borhan pors entries"
}
```


### [2026-09-14T00:53:26.978Z] TOOL RESULT

```
۲ - کب‌الاخبار مشهور فت
آفرده است .
۳ کم نگریدآبی رآن‌رنگه رخ‌آیی
رخ او چون رخ آن زاهد محراأبی
کته از کردش ابن چنبر دولایی
بر دخسش بر » اثر سبلت. سقلابی
یه درصفحة ۳۸۳-_۳۸۳
و ثالكث بتحنالی رسیده و واو مفتوح بنون ودال
ابجد زده , بىني صریح باشد که در مقابل رمز
وایماست . ۱
رس ح_بفتح اول بروزن‌دری, پردمرا
کویند که بر روی چیز ها پوشند و از جاها
آویزند . *
پرسا! - بضم اول وسکون ثانی و سین
بی نقطه بالف کشیده » خبر کیرنده وپرسنده را
ی
پرستنده و پرستار باشد؟ - وشخصی رالیزگویند
که در وهم ویندار خود- ببنی در فکر وخیال
خود مانده باشد ۴ .
پرستار ۴ - بر وزن طلبکار » خلام
و کنیز و خدمتکار و خادم - و فرمان بردار
0 ( برمننده) از 5002 +1 02۲ ( ور
ایتادن ) ۶ اسشق ۲۹۸ *.
«بودکی ۱۱۰ » رك : پرست و پرمتیدن . .
هرمتش ۰
۲ ره ءِ فرحنو.
سیاه ویفارسی فرشتوك کونند. هعنتهی‌الارب» .
۱ پرسنندث خبال
ومطبم ومنقاد باشد - و طاعت وعیادت کننده را
یز گوینده .
پرستادان خبال ه کتابه از شرا
و صاحبان نظم وش باشد . :
پرستش! « بکس دابع و سکون‌شین
قرشت » طاعت و عبادث را کونند - و خدسنکاری
ویار داری را نیز گنته اند که خدحت مار
کردن باشد .
پرستاث ۷ - کر اول وتانی‌وسکون
ثالث و ضم رابع و کاف حاکن ؛ فام پرنده ایست
که پشت ودم او سیله و سینه اش سفید ومنفارش
سرخ عیباشدو درسقف خاهاآشیان میکند واو را
ری ند .
بر‌دوسر کین اوبازهرة پ‌ستوك __
کاو بامیزند و بر موی طلا کنند بی هنگم
سفید. نشود .
فر سته < بکسر اول وثانی‌بروزن فرشته»
زنی خدمتکار باشد؟ - وبفتح‌اول وثانی‌پرسنیدمرا
بحق همچوخدایشالی و بباطل هسیو بت .*
پرسق منم اول و ثاك و سکون
ثانی وقاف » جانوری است که آنرا راو گویند
وبه_بی ابن عرس خوانند . اکر درون شک اورا
دك سود کرده او را خشث سازند. دو مثفال آن
دفع باد سموم کند .
پرسم ع منم الث بر وزن کندم .
تیه .
شاعر و منشی باشد؟ .
لیر سه س بفتح اول و اك . مخفف‌پارسه
است که گدایی باشد - و بضم اول بهعنی بر سنن
و احوال بر گرفتن و بعیادت بیمار رفتن باشد.
پررسیان « بنتم ات بر وزن پهلوان,
کیاهی اس ت که بر درخت‌پیجد وآنرابعربی‌عشقه
کویند .
«نامهای پرند گان در کردی44*.
رك : هرستدان .
ای آنکه ثرا میشه فرحتیدن مخلوق
-خدمت کردن ؛ بند گ یکردن 4
تن‌خوش بك‌چند بیمار کرد
برسنیدن بادشه خوار کرد . فردوسی طوسی.
( برهان قاطع ۲ه)ویو -
پر سیاوش" « بفتح‌اول وسکون‌نانی
و کسر ثالث و تحتانی بالف کشیده و واو مضموم
بشن فرشت زده ۰ نام گیاهی است که خلاشةآن
باريك وسیاه فام وب رکه آن سبز رنگه می‌باشد
و پیشتر در گوشه و کنار حوضها میروبد و آنرا
بمربی شمرالجن ولحیةالحمار خوانند- وشکلی‌را
یز گویند از اشکال فلکی متمل بر ست
ونه ستاره هورت عردی برپای ایستاده وسرغولی
دردست آ و یخته‌و آ نرا رأس‌الفول خوانند و کوا کب
آن‌دربرح ثوراست باتفاق ارباب رصد ودر زبجات
و کتاب صور کوا کب باین‌منی برشاوش نوشته‌اند
با بای ابجد و بجای حرف شثالث شین فرشت
وبحذف بای حطی » ال اعلم۴ .
پرسیاو شان ا بالف ونون بسنی
است که کیاهی باشد دوابی» اکر
آنرا بسوزانند و با روقن زبت و س رکه بر سر
از ۲4 عالند موی بروباند .۶
رشن « باشین نفطه دار بر وزن
اول برسباوش
فهمیدن , بمعنی بربلد دلدن بلشد ۴ .
پرغاده با خین فطه دار مر وزن
سر ۰ بخ وین ویر جاتوران پراده راگوشد»
فرگزه - ج ی
دار و سکون انی . مخفف پر غلزه است که یخ
و بن پر جانوران پرنده باشد .
پر ول « بروزن معقول ء کندم وجو
نیم کوفته و خرد شده را کوبند - و آشی را
کهآ نرا افروشه خوانشد .
بر و نه -. بر وژن حمدونه » هرچیز
که زشت ث و ازسا باشث .
پر ك . بفتح اول و انی و سکون کاف
۳ رودخانه ای حم
۴ - و مطلق صدا و ندا را نیز کفته اند .
و باين معتی بجای حرف اول تای قرشت حم
خیم یرت
6 « ارعة ۳۰۰ ».
۳ رگ :بر بشید
آزیشت کوه خلخ بکشابد وبثلحیت جنوب
6 پر سیلن- بضم
```


## [2026-09-14T00:53:36.256Z] TOOL CALL #31: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:385 2>&1 | head -60",
 "description": "Fetch Borhan page 385"
}
```


### [2026-09-14T00:53:37.362Z] TOOL RESULT

```
no scan of BQT covers printed page 385 (see 'scans' in refs_online.json)
```


## [2026-09-14T00:54:01.499Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN pursidan\"; grep -n -i \"pursīdan\\|pursidan\\|pursīd\\|purs\" HRN.txt | head -20; echo \"### HRN para\"; grep -n -i \"pāra\\|pâra\\|para,\" HRN.txt | head -20",
 "description": "Grep Horn"
}
```


### [2026-09-14T00:54:01.556Z] TOOL RESULT

```
### HRN pursidan
2897:299. pursTden 'fragen', pursis^).
2901:'fragen; iphW. pursUan, purs(i)sn, ptirsttar; ai. i^prag-^
10946:/vareh), pursartak (d. i. pursardak) etc. Zu pur Viel*
13421:pursiden 299.
13422:pursis 299.
14250:patipursähy 299.
### HRN para
3319:aw. '^para,yär' (+ säl),
```


## [2026-09-14T00:54:01.752Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG pars\"; grep -n \"PARS\\|\\*pars\\|pursīdan\\|pursidan\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for pars"
}
```


### [2026-09-14T00:54:01.813Z] TOOL RESULT

```
### CHEUNG pars
6774:*NWIR: Widely attested: NP pursidan/purs-, Kurd. (Kurm.) pirsin/pirs-, (Sor.) pirsin/ 
19620:298 *pars 
41349:pursidan/purs-, 89 
57964:*pars 
58003:*pars, *Oras
```


## [2026-09-14T00:54:04.282Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2890,2910p' HRN.txt; echo \"=== CHEUNG ===\"; sed -n '6740,6800p' CHEUNG.txt",
 "description": "Read Horn 299 and Cheung *pars"
}
```


### [2026-09-14T00:54:04.386Z] TOOL RESULT

```
dessen Bedeutung sich mit der von V^tac- {-\- pard)
unschwer vermitteln lässt.
298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
perestis.- 67 -
phlv.paras^* Verehrer, parastar,parastakzh, i)arast(i)sn
'Verehrung.
pari + l^ sthä' *um jemand herum stehen *).
299. pursTden 'fragen', pursis^).
g. parsädmün ; mäz. parsien ; Käs. vapersöddn, vöper-
sö'imün, vepersad,
ap. aw. [//ras-, Praes. pat{\parsähy bezw. peresahi
'fragen; iphW. pursUan, purs(i)sn, ptirsttar; ai. i^prag-^
Praes. pfchdti; arm. harc 'Frage', harcanem 'fragen,
harsn 'Braut' (H. No. 161).
kurd. />:/r5m 'fragen' ; aty. pust- hezw. pu/t-edal; oss.
d. farsun^ t. färsin (279); bei. LW. n. pur§ay (211);
WS,/, sar. pörsam.
300. perrisiym^uS, perrisiyCLvesän ^) , 'Frauenhaar (Pflanze),
Adiantum capillus Veneris L.'.
^= perr-t Siyävus y d. i. parenö (yö) Sydvarsäuahe
(de Lagarde, Armen. Stud. No. 1688, Pers. Stud.
=== CHEUNG ===
p’dypr’h, BMP p’tpl’s /padifrah/ ‘punishment, retribution’ || (+ *ham-) BMP 
hmpwrs- /hampurs-/ ‘to consult, take counsel = DMMPP: 287a, 26b, 275b258b 
Widely attested: Pres.: IND. 1sg. BMP pwrsym /pursém/, 25р. BMP pwrsyh /purse/, 3sg. MMP pwrsyd, 
BMP pwrsyt /purséd/, 3р1. MMP pwrsynd, 3р1. BMP pwrsynd /pursénd/, etc. || (+ *pati-) Pres.: IND. 1sg. 
MMP "phypwrsym, 35р. IMP ptpwrsyt, SUBJ. 3sg. IMP ptpwis’t, IMP "ptpwrsyt, IMPV. 2sg. MMP 
phypwrs, 2pl. MMP phypwrsyd, MMP phybwrsyd; Partic.: perf. pass. MMP phypwrsyd || (+ *ham-) 
Pres.: IND. 3sg. BMP hmpwrsyt /hampursed/ 

*PARTHIAN: pwrs- ‘to ask’ || (+ *a-) ? *’fr’s ‘teachings, instruction’ {hapax} || (+ 
*pati-) pdbwrs- ‘to read, recite’ || (+ *ui-) wyfr’s- ‘to teach, show’ = Ghilain: 69, 79 
| DMMPP: 287a, 26b, 269a, 352a f. 

Pres.: IND. 2sg. pwrsyh, 3sg. pwrsyd, 3pl. pwrsynd, SUBJ. pwrs’h, 2pl. pwrs’’d, IMPV. 2pl. pwrsyd, 
OPT. pwrsyndyh; Partic.: perf. pass. П pwrs'd, ? *pwrsyd; Inf.: pwrs'dn|| (+ *pati-) Pres.: SUBJ. 2sg. 
*pdbwrs'h, IMPV. 2р1. pdbwrsyd; Partic.: perf. pass. П pdbwrs'd; Inf.: *pdbwrs’dn || (+ *ui-) Pres.: IND. 
lsg. wfr's'm, 35р. "wyfr’syd, 3р1. wyfr’synd, IMPV. 2pl. wfr'syd; Partic.: perf. pass. wyfr’st, Inf.: 
wyfr’stn 

*KHOTANESE: puls- ‘to ask’ || (+ *4-) (caus.) auräss (oras-, auras-) ‘to inform’ || (+ 
*pati-) Khot. pus- (pus-) ‘to read’ = SGS: 85, 20 

*SOGDIAN: SSogd. p’rs-, SSogd. ’ps-, BSogd. ’prs-, CSogd. ps-, MSogd. ps- ‘to ask’ 
|| (+ *a-) BSogd. ’’p’rs ‘to ask for, take leave’ || (+ *pati-) BSogd. ptBs-, CSogd. 
ptfs-, MSogd. ptfs- ‘to read’ || (+ *ui-) BSogd. wp’rs, CSogd. wprs, ’wprs, MSogd. 
wprs ‘question’ 

Widely attested: Pres.: IND. 2sg. BSogd. ’prs’y, BSogd. ’ps’y, 3sg. BSogd. ’prsty, INJ. 1sg. BSogd. 
*prs’w, SUBJ. 35р. CSogd. ps’t, OPT. 2/3sg. BSogd. ’prsy, BSogd. ’prs’y, 2р1. SSogd. prsyöy, 3р1. 
CSogd. руш, etc. || (+ *a-) Pret.: IND. 3sg. BSogd. ’’prs || (+ *pati-) Widely attested: Pres.: IND. 3sg. 
BSogd. ptfsty, 1р1. dur. CSogd. "ptfsymsq, 2pl. CSogd. ptfs0’sq, SUBJ. 3sg. BSogd. ptßs’t, 3р1. BSogd. 
ptBs’nt, BSogd. ptßs’n, OPT. 3sg. BSogd. ptps’y, etc. 

*CHORESMIAN: m/bS- ‘to ask’ || (+ *ham-) ’nbS- ‘to ask’ = Samadi: 162, 117 

*NWIR: Widely attested: NP pursidan/purs-, Kurd. (Kurm.) pirsin/pirs-, (Sor.) pirsin/ 
pirs- (< Kurm. ?), Zaz. persayis/persen-, Abyan. parsoya/pars-, Awrom. parsay/ 
pars-, Gz. pärs-/pärsä, Gur. (Kand.) pärs-/-pärs-, Ham. va-pärsayän/va-pärs-, Isfah. 
pärsän/pärs-, Meim. vam parsa/va: a-pers-, (LW) Khuns. purs-/pursä, Nn. рагѕауе/ 
pars-, Qohr. parsada/pars-, Semn. pärs-, Siv. purs-/pursi, Soi pars-, Tr. parsaya/pars- 
‘to ask’ 


90 *fraul 


*NEIR: Ishk. f(s)ras-/f(e)rüt-, Sh. (Baj.) peXc-/peXst-, Rosh. paws-/pawst, Sariq. 
pars-/parst, Yzgh. pis-/pist, Yi. p(o)rs-/pist-, M. purs-/pist-, Pash. pust(ed)ol, Wa. 
pors-/porst- ‘to ask? 

*MISC: (+ *pati-) Arm. (LW) patuhas ‘punishment’ 

*SANSKRIT: pras ‘to ask’ (RV+) > EWAia П: 183 

© This root has an impeccable etymology. 

«PIE *prek- ‘to ask’ => LIV: 490 f. | Pok.: 821 f. 

*IE COGNATES: Lat. posco ‘I demand, to ask’, Toch. A prak- B prek-, Goth. 
fraihnan, OCS prositi, Lith. prasyti ‘to ask’, etc. 

*REFERENCES: КРЕ I: 135b f., 205b, 244a; Ivanow 1926: 421; KPF II: 188; IIFL II: 239b, 534b;
```


## [2026-09-14T00:54:11.119Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6700,6742p' CHEUNG.txt",
 "description": "Read Cheung pars entry head"
}
```


### [2026-09-14T00:54:11.169Z] TOOL RESULT

```
*PIE LIV: - | Pok.: 
*REFERENCES: IIFL I: 409b; EVP: 90; Werba 1997: 220 


*fras/prs ‘to ask, inquire’ 

*AVESTAN: fras- (paras-) ‘to ask, inquire’, YAv. frasna- ‘question’ || (+ *4-) Чо be 
advised [med.]’ || (+ *pati-) ‘to ask, interrogate (someone)’ || (+ *ham-) ‘to consult; 
to be consulted, contemplate [med.]’. 0 On the analysis of YAv. °frasäne see 
Klingenschmitt 1982: 62; Humbach 1956: 68. = Liste: 35 

Pres. inch: IND. 15р. OAv. porosa (Y 31.14 ff., Y 43.10, Y 44.1 ff, etc.), med. 150. YAv. porose (Yt 
12.1), 2sg. YAv. parasahi (H 2.17, H 2.35, Vyt 63), med. 3sg. parasaité (Y 31.12, X3 Yt 14.47), med. 3sg. 
OAv. parasaété (Y 31.13), 3р1. YAv. fra porosonti (N 61 £), med. 3pl. YAv. һат.рәгәѕәпіе (V 19.3), 
impf. (med. ?) 1sg. ? YAv. "aporosom (or "aporose) (V 2.2), (med. ?) 2sg. ? YAv. “aparasd (or 
"aporosagha) (V 2.1), 3sg. Y Av. aparasat (V), INJ. 2sg. poroso, 3sg. porosat, med. 3sg. Y Av. paiti porosata 
(V 9.43, V 9.45), SUBJ. med. 1sg. porasai (Y 44.12), med. 2sg. YAv. pərəsañhe (Yt 10.2), 3sg. YAv. 
porasat (У 18.6), med. Zeg. Ү Ау. "porosäite (V 15.14), med. 3р1. YAv. porosánte (P 44), OPT. med. 3du. 
Y Av. aporosaiiatom (Y 12.5 f.), IMPV. 25р. OAv. porosä (Y 43.10), med. 2sg. Y Av. porosary'ha (V); Pres. 
{2} anja-: IND. 35р. Y Av. porosaniieiti (Yt 8.15, Yt 8.17, Yt 8.19); Aor. s-: INJ. med. 1sg. OAv. frasi (Y 
44.8, Y 45.6), med. 3sg. OAv. frastä (Y 49.2, Y 47.3), ? OAv. afrasta (Y 51.11), SUBJ. med. 15р. ? ҮАУ. 
afrasane (У 3.27), IMPV. med. 25р. OAv. (°)forasuua (Y 53.3); Partic.: pres. {1} OAv. porosant- (Y 
51.5), med. OAv. porosemna- (Y 30.6) 

*OLD PERSIAN: prs- ‘to ask; punish’ || (+ *pati-) ‘to read, recite’ = Kent: 198a 

Pres. inch.: IND. 159. prsamiy <p-r-s-a-mi-y> (DNb 19), impf. 15р. aprsam <a-p-r-s-m> (DB 1.22, DB 
4.67), SUBJ. 2sg. patiprsahy <p-t-i-p-r-s-a-h-y> (DB 4.42), 3sg. patiprsatiy <p-t-i-p-r-s-a-t-i-y> (DB 


*fras/prs 89 


4.48>), IMPV. 25р. prsa <p-r-s-a> (DB 4.38, DB 4.69); Partic.: perf. pass. (+ *hu- ‘good, well’) °frasta- 
«?-f-r-$-t-^» (DB 1.22, DB 4.66, DB 4.38, DB 4.69); Pass.: pres. OPT. 3sg. fra0iyais <f-r-0-i-y-i-8S> (DNb 
21), aor. IND. 35р. patiyafrasiya <p-t-i-y-f-r-0-i-y> (DB 4.91) 

*MIDDLE PERSIAN: MMP pwrs-, BMP pwrs- /purs-/ ‘to ask’ || (+ *a-) MMP ’fr’h, 
MMP ’’pr’h, BMP ’pl’s /afräh/ ‘teaching(s), instruction, doctrine’ || (+ *pati-) MMP 
phypwrs-, phybwrs-, IMP ptpwrs-, ptpwls- ‘to read (aloud), recite’, ? MMP 
p’dypr’h, BMP p’tpl’s /padifrah/ ‘punishment, retribution’ || (+ *ham-) BMP 
hmpwrs- /hampurs-/ ‘to consult, take counsel = DMMPP: 287a, 26b, 275b258b 
Widely attested: Pres.: IND. 1sg. BMP pwrsym /pursém/, 25р. BMP pwrsyh /purse/, 3sg. MMP pwrsyd,
```


## [2026-09-14T00:54:20.498Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD padifrah\"; grep -n -i \"padifrah\\|pādifrāh\\|ptpl's\\|p'tpl's\" PHD.txt PHD_mackenzie.txt | head; echo \"### PHD pursidan\"; grep -n -i \"pursidan\\|pursīdan\" PHD.txt PHD_mackenzie.txt | head",
 "description": "Grep MacKenzie"
}
```


### [2026-09-14T00:54:20.591Z] TOOL RESULT

```
### PHD padifrah
PHD.txt:536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:3287:punishment drēš, pādifrāh, puhl.
PHD.txt:3423:retribution pādāšn, pādifrāh..
PHD.txt:4743:padrazm sò rey о) pādifrāh © teras arzan!, gāwars! 5o)
PHD_mackenzie.txt:3912:padifrah [p'tpl's I M p)dypr'h, N ·piidafriih] punishment, retribution.
PHD_mackenzie.txt:3946:padofrah [p)twpl)s] = padifrah.
PHD_mackenzie.txt:7373:punishment dros, padifrah, puhl.               razor awestarag.
PHD_mackenzie.txt:7428:remain (abaz) mandan, (manistan),        retribution padasn, padifrah..
PHD_mackenzie.txt:8828:peroz                     c;~Q)                padifrah               ~Q.)~QJ
### PHD pursidan
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:864:ask pursidan, zastan, (zayistan).
PHD.txt:4708:padzyān purs- pursīdan pursišnīg pursišn padpānag pa(č)čībāy- pa(č)čībāgīh frazand
PHD_mackenzie.txt:4280:pursidan, purs- [pwrs-ytn l I M pwrs-ydll, N ......] ask. \~ ? t(~ -
PHD_mackenzie.txt:5983:ask pursidan, zastan, (zayistan).        away parron.
PHD_mackenzie.txt:8744:panjag, pozag                  ,~~\ Q.)       pursidan                \\~"Q)
```


## [2026-09-14T00:54:22.083Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB pursidan/padifras\"; grep -n -i \"pursītan\\|pursitan\\|purs\\b\\|pātifrās\\|patifras\\|pādifrāh\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Nyberg"
}
```


### [2026-09-14T00:54:22.127Z] TOOL RESULT

```
### NYB pursidan/padifras
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
1526:B: 11-12 (in Arab it would be ’amarnä man šayyada) ; e) without any introductory part.: api-m framātv patpursčt I ordered
1551:frašn [plšn'] question 2114; conversation 375. — Av. (1009 sq.) frašna-; Paz. frasn (SGV). Same st. as pursitan (q. v.). Frašoštr [plšwštl] n. pr. 108%, — Av. (1007) Frašaoštra-.
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
1763:hāciš [hes], Ps. aei$ [Pcšy] adv. of hac 1. used instead of hac to refer back to an encl. pron. in the beginning of the sentence: -§ mà sax%van ~ pursét do not ask him any questions 74%7. 765-§; han gu ke-š Gayomart ~ the clay of which G. was (made) 9516; hamäk cis ké-§ martömän rämisn ... ~ all things in which men take pleasure 10029-21; api-§ purr aciš and full of it 12815-16; — referring directly to a preceding rel. pron.: ctš-ē ke ziyan nem šāyist butan something from which no harm
1857:ham-pursitan [hmpwrsytn'] to consult, to deliberate, to plan: han murv (pl. cas. rect.) hampursit hend ku ... 404. — V. pursitan.
2127:kart ēstēt, cigön Dahäk u Frāsyāp u Väman [thus Cod. DH; TD w’tn', Paz. vätan, perhaps for Väöarjä the father of Vaman, Tab. I, 530 init.] u apārīk hac én āivēnak marg-aržānān, pātifrās [+ Paz. vama, probably a misspelt Vaman] 10 ātvēnak-ic vitārēnd ‘those who have in- stituted their own *laws for mankind, as D. and F. and V. and other death deserving men of that kind, will undergo ten sorts of punishment’. For the whole passage cf Phl Vd ad 75? (p. 279).
2738:nimütan [nmwtn'] nimay- [nm?d-], pres. 3d p. sg. nm'dt', inser. nm?dty, both = nimáyét, 3d. p. pl. nm’dynd = nimdyénd, to show, to denote, to signify, to indicate 512, 810 etc.; to teach 81!!; — a syn. of kartan : patifras ~ 10112; handácak ~, v. the preceding w.; bahrak ~ to allot a share 1152-35, — < ni + Av. OP (1165) mäy-, cf framütan; MPrth nm?dn nm’y-; MPrs nmwdn nm?y; Paz. NP namudan; Verbum 203.
3015:pātifrās
3018:5913.25] retribution, reward 38. 5913.25, 719-8 (opp. ävenisn). 808-1? (opp. patifras). 9510-18, 103?5, — < pāt- = pat- (as to the lengthening of -ā- cf Verbum 229 sg.) + dašin (g.v.): MPrs. p’d’syn; Paz. pä- daišn, pädäs(a)n (Mx), NP pädäsan; Talm. lw. prdšn? ‚prdysn’ ‘gift on parting, a farewell present’ Cf Bailey, BSOS VI, 1930-31, 600; Telegdi 250 sq.
3027:patifras
3078:patpursitan [ptpwrsytn'] to read: api-m framät? patpursēt and I ordered (Someone) to read it = I ordered it to be read P 2: 4. — OP pati-prs- (Kent s. v. fra0-); M Prth pdbwrs-; MPrs pahypwrs-, phybwrs- ; Verbum 196. 228. V. pursitan.
3181:pursitan [pwrsytn'] to ask, followed by ku introducing direct speech 3? and passim; with a dir. obj.: to consult 481%. 6371; to ask a p. : o 68—88 passim, elsewhere hac; — about: apar 4814-25, 4912, or pat 1615; — frašn, or saxtan ~ hac to ask a question, questions 2114-15, 742.6-7, 766; with a rel. pron. as its dir. obj. 76%, 1055.9; — 6 ham ~ to deliberate 577, cf hampursitan; hakanén ham pursénd thev will converse, communicate with each other 1061-18. — Av. (997 sqq.) fras-, pres. parasa-, OP frad-, pres. p(a)rsa- (Kent); MPrth pwrs’dn pwrs-; MPrs pwrsydn pwrs; Paz. NP pursidan.
3418:saxtan [shwn'; MRY?] word, speech, passim; ~ haciš pursēnd they ask him 742.6-7, 765-6, — Av. (1569) saxtar- ‘device, plot’; MPrthPrs sewn; Paz. saxun; NP SAXUN, suxun, SULAN.
3575:w. after a lengthy digression: Ohurmazd, ka Ahriman apāk (g. v.), -(a)š hämöden dam u dahišn ... frac kart 9145, -(a)š re- ferring back to Ohurmazd; in this case the independent form aš would have been more appropriate, as in api-š hamäk da- mik, i-š apar rah būt, aš [8] perdvanihit (g. v.) kart 3316-17, — If it belongs to a prep. this changes to an adv., in a special adverbial form if there is one, which is placed afterwards in the sentence: (-š — andar:) api-š ... must" (g.v.) u drog andar nest F:6-7; — (-$ — apar:) api-š Vīdrafš . apar nišinčt V. gets on it (the horse) 2515; cé-§ apar baxt estet dušman dzanét 2714, v.s. v. baxtan; — (-$ — hac pas:) api-$ hac nihän hac pas fräc dväret from behind him 2519-20; — (-$ — avis, adv. of 0): tài ka-š hàn Hamäk . . . pat zanéh avis dahom to him 261-2 (285 without avis); 26°; bē-š avis barét ...! 767-8; — (-š — haciš:) gobet kū-š ma saxvan  haciš pursēt 7487; — (-§ — patis:) api-š afrin patiš kunēt (BYDWN-x,) 2716-17; apt-š dēvān apasēs u riyahreh patiš kunēnd 7526-27; — this construction is regular in relative clauses, v. s. v. ? and ka. — The adverbs avis, haciš and patis may be used alone as substitutes for 6, hac, pat + š, v. these ws. — Attached to a prep., but belonging to the governed subst.: 6-§ zäyisn until his birth 4412; in apāk-aš pat asp mišast estat 88 -š belongs to the whole sentence, cf 8? 4-6 apāk pat asp, and its place after apäk is fortuitous. — OP -Saty; common Milr and NP; v. -šān. šagr [šgl] lion; the constellation Leo 51, — MPrth srg (MHC); MPrs Sgr (A-H I); NP šēr.
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
4269:embarrassment in dealing with these terms. The translator of Vd. 8%, who quite correctly felt that vačpyo is a pass., borrowed the Av. vb. (1322 sg.) vaēp- (otherwise not attested in Milr as far as I know) and formed from it the pass. pt. viftak, then, likewise correctly interpret- ing vaepayö (vačpayant-) as an act., form- ed from viftak the caus. vb. viftén-, but, by assimilating it formally to viftak: vifténitak, created a bizarre mixture of act. and pass. The same curious contra- diction is found in DD, purs. 719-7 which is, however, closer to the Av. original: viftak and vépénitak. Our passage 82° has chosen a mitigating vb. ‘to seduce’, *vr- dip-: MPrth pres. wdyfs- ‘to be cheated’, wdybyšn ‘error, aberration’, wdyb-gr ‘im- postor’, wdyftgyft ‘deceit’, Ghilain 81 sg.; Arm. lw. vrép < *vidép ‘oblique, pervert- ed; fault, error, depravation’; MPrs pres. wyyb- (viyéb- < "videp-), also contracted wyb-, pass. wyfs-, pt. wyft(g), abstr. wyyftgyh = viyiftageh (also wyf-), wdyb *deecit certainly borrowed from NW ; v. Verbum 173. 198; Ps. wydyptk’n "those who have gone astray’. BP wdypt >
4889:fra0-: pursitan Fravarti-: fravahr fravatah: fröt
4920:pati-prs-: patpursitan
5681:pwrs’dn: pursitan
```


## [2026-09-14T00:54:36.016Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3010,3030p' NYB_vol2_glossary.txt; echo \"=== page marker near parak (line 2944) ===\"; awk 'NR>2860 && NR<2960' NYB_vol2_glossary.txt | grep -n \"^[0-9]\\{2,3\\}$\"; echo \"---\"; sed -n '2935,2950p' NYB_vol2_glossary.txt",
 "description": "Read Nyberg patifras and page"
}
```


### [2026-09-14T00:54:37.354Z] TOOL RESULT

```
pat
orthography the Iranians took over, it was necessary to mark it in some way as a word unit. For this purpose the ending -WN, very common in Aram. verb ideograms, was chosen. The form PWN thus created is consequently a spurious ideogr. and has no root in Aram, as I formerly assumed. The transliteration p'', adopted by de Menasce, is an attempt to visualize the spelling (but the real sign of abbreviation in BP is -g, originally probably -k: H-g, Š-g, P-g, FrP 4). - In compounds pat is regularly written pho- netically, only in special cases PWN, cf above A II, ll and some of the following ws. In compounds the genuine SW form pai- is sometimes reflected in the orthography. v. pairdstak, pairāyak, pairök.
patacanbyö [Av.] 6512, not found in the existent Av. texts; probably, through haplology, < *patt-tacanbyē, dat.-instr. pl. of *pati-tacant-, pt. pres. of pati + tac- (v. tacitan and iāxtan), thus ‘in an uninterrupted succession of generations’.
pätan [NTLWN-tn'] päy- [NTLWN., p'dt' = päyet 2512] 1. to guard, to protect, to watch: tan + x“éS be pāyēt: menišn hac dušmat . . . guard yourselves: your think- ing from evil thought (etc.) 65°; vas hamestar činod pdt estend a great many adversaries "keep watch there 724: pat seems to be an abstr. subst. < Olr *pāt?- ‘watch, guard’, cf Arm. lw. pat ‘fence, enclosure’, pat arnul, gal, pat-em, -im ‘to surround, to be surrounded by? — 2. to make a halt, to stay, to remain (zivan- dak apäc pätan 251), to last: 6%. 729, 107°. 205, 2671. 714, — Two vbs. have coalesced here: 1. Av. OP (885 sq.) päy- ‘to protect, to watch’, 2. a den. of pada- ‘place’ (v. pādak): "padayati > SW pāyēt, which has borrowed its inf. from the homonym päyet ‘to watch’. MPrthPrs only have p’dn p’y- ‘to protect’; Paz. id.; NP päyidan in both senses.
155
pātifrās
pat-apākēnīt [PWN-'p'kynyt'] pt. pret. pass. 3d p. sg.: pat apākēh ~ brought back with him 41?: instead of saying pat apakéh burt, the author has formed ad hoc a paronomastic den. vb. *pat- apākēnītan (v. apäk 2), and thus achieves a figura etymologica illustrative of the
man���s care and tenderness. — Cf pat- frazämenit. pātdāšin  [p'td'án' pādāšin [*p’d’än'
5913.25] retribution, reward 38. 5913.25, 719-8 (opp. ävenisn). 808-1? (opp. patifras). 9510-18, 103?5, — < pāt- = pat- (as to the lengthening of -ā- cf Verbum 229 sg.) + dašin (g.v.): MPrs. p’d’syn; Paz. pä- daišn, pädäs(a)n (Mx), NP pädäsan; Talm. lw. prdšn? ‚prdysn’ ‘gift on parting, a farewell present’ Cf Bailey, BSOS VI, 1930-31, 600; Telegdi 250 sq.
patéx"éh [ptyhwyh] welfare, prosperity, well-being 68%. 877. — Abstr. of patéx ‘thriving, prosperous, well-to-do’, render- ing Av. (805 sq.) Orqfada-; < *pati-ax"a-, from Av. (106 sgg.) ahu- ‘life, existence’, v.s. v. pat A II, 11; Paz. patixvi.
patéx"énitan [ptyhwynytn'] to nourish, to cause to prosper 8115.
pätez [p'tyz] autumn 887. — MPrs p'd(y)z (A-H I), Paz. pādēz, NP payiz. V. Bailey, TPhS 1945, 13.
pat-fracéh [PWN pPcyh] appearance 40% (read: api-sän ētēn-aš ~ 6 ham ārāst *,.. his appearance’). 4019, cf 39??, — pat fraceh 52? are two distinct ws., v. frācēk.
pat-fražāmēnīt [PWN ple’mynyt'] pt. = pret. pass. 3d p. sg., was finished 1169-12, — A den. of the expression pat frazdm, v. frazam and cf pat-apakénit.
pätifräs [[p'tpl's], Ps. pätufräs [p’tw- pPsy] punishment 93. 12°. 76H. 808-13, 10112-15, 10218-17.26, 10322, 1288, -NW w.: MPrth p’dyfr’s (MHC), Arm. Iw. patuhas, but SW pätifräh: MPrs p'dypr? h (S); Paz.
| pädafräh. The -u- in pätu-, also found in
www.parsianjoman.org | ool wok
patifras
the books, is due to the influence of the following labial.
patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
rād hac Ohurmazd patigrift these have.
=== page marker near parak (line 2944) ===
26:148
50:149
72:150
89:151
---
panj [pne'; figures] five.
panjih [figure] fifty; 3-50 = 58, v. 422%. — Cf Salemann, Gr 288.
Panj-bör [pncbwl] n. pr. 114. - ‘Having five grey (horses)’: bdr signifies ‘red’ and ‘bay’ in NP and Bal., but in other areas ‘grey, ash-coloured’ (hence Milr *bórak, Arm. lw. borak; Syr. lw. börgä, Arab. lw. bauräg- ‘borax’ which itself is borrowed).
panjom [pnewm; 5-wm] the fifth.
pánz-dahom 15-wm] the
fifteenth.
Päpak [p’pk'] the father of King Arta- xščr, receives the naked title King (MLK? = šāh): HajA:4. B:4. ŠPrs:8. Prth: 8; 1-3 passim. — NP bab, baba ‘father’.
[p'nedhwm ;
Papakan patron. of Päpak: Artaxšer 4 ~ 11. 6%, 1091, 1169-16; belonging to Papak: Staxr + ~ 10719,
pārak [p*lk'] a bribe 7313, 7515. — Av. (889) para- ‘debt’; MPrs p’rg ‘gift’; NP pärah ‘gift, bribe’.
par-bütan [pr-YHWWN-tn'] to shun, to avoid: yuvatak hac 63%. — I maintain the reading of the MSS; J.-A. deleted pr-. From Olr pard (Av. 852 pard) + butan, cf MPrs przyr ‘to abstain from’, prer- ‘to avoid’ <  "para-car-; prgn- (v. pargandak); Verbum 227.
pardaxtan [pldhtn'] pardac- [plde-] to run after, or to run to an end: 1. to strive for (6): avis névak pardac strive well for it! 7616 (Paz. friz = frēc [plyc], g. v., Skr v. sadrsam sädhu vardhaya; however, Cod. K has explicitly pidc with a marked d ; this reading pardac, accepted already by West, suits the context bet- ter). — 2. to be accomplished, finished, cf MPrs w "z ’wd dyw'n zd "wd prdxt mnd
www .parsianjoman.org | perl wb
pardaxtan
151
Pirs
```


## [2026-09-14T00:54:44.639Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### pornography\"; grep -n \"pornography\\|porne, prop\\|pornē\" KLN_1966.txt | head; echo \"### prison\"; grep -n \"^prison\\|prison, n\\.\" KLN_1966.txt | head; echo \"### price\"; grep -n \"^price\\|price, n\\.\" KLN_1966.txt | head",
 "description": "Grep Klein"
}
```


### [2026-09-14T00:54:44.729Z] TOOL RESULT

```
### pornography
26950:fr.  L.  paria ,  neut.  pi.  of  par,  ‘equal’  (taken  as  a fern.  sing,  noun),  whence  L.  parare,  ‘to  make equal’,  compdr,  ‘equal’,  comparare,  ‘to  com¬ pare’  ;  prob.  cogn.  with  Avestic  pairyante,  ‘they are  compared’,  Gk.  7r£pvT)p.i,  ‘I  sell’,  prop.  ‘I give  for  equal  value’,  L.  pretium,  ‘price’,  OI. 'prati,  ‘against’,  Gk.  rcpoc,  ‘toward,  to’,  OSlav. protivu,  protivQ,  ‘in  opposition  to,  against’,  Gk. mipvY),  ‘harlot’,  lit.  ‘bought,  purchased’,  Lith. perku,  ‘I  buy’,  OIr.  renim,  ‘I  sell’,  ernaim,  ‘I grant,  give’.  All  these  words  prob.  derive  fr. I.-E.  base  *per-,  ‘equal;  to  sell,  to  buy  (i.e.  to give,  resp.  take)  for  equal  value’.  Cp.  par.  Cp. also  appreciate,  compare,  depreciate,  disparage, disparity,  interpreter,  nonpareil,  Paris,  ‘a  genus of  plants’,  parisy liable,  parity,  parlay,  paroli, peer,  n.,  pornography,  praise,  precious,  price, prize,  pros-,  umpire,  herb  Paris.  Base  *per-,  ‘to sell’,  is  prob.  ult.  identical  with  base  *per-,  ‘to assign,  allot’,  whence  L.  pars,  gen.  partis,  ‘part’; see  part,  n.  Cp.  pare  and  words  there  referred  to. Derivatives:  pair,  tr.  and  intr.  v.,  pair-ed,  adj., pair-ed-ness,  n.
29666:pork,  n.  —  ME.,  fr.  OF.  pore,  ‘pig,  pig’s  flesh’,  fr. L.  porcus,  ‘pig’,  which  is  rel.  to  Umbr.  purka, porca  (=  L.  porccis,  ‘female  swines,  sows’,  acc.), and  cogn.  with  OSlav.  prasg,  ‘young  pig’,  Lith. parsas,  ‘pig’,  OPruss.  parstian,  prastian,  ‘young pig’,  MIr.  ore  (for  *pork),  ‘a  little  pig,  young  of an  animal’,  OHG .  farh,  farah,  ‘pig’,  OE.fearh, ‘a  young  pig’.  See  farrow  and  cp.  porcelain  and thefirst  element  in  porbeagle,  porcupine,  porpoise. Derivatives:  pork-er,  n.,  pork-y,  adj. pornographer,  n.  —  See  pornography  and  agential suff.  -er,
29667:pornographic,  adj.  —  See  pornography  and  -ic.
29668:Derivative:  pornographic-al-Iy,  adv. pomographist,  n.  —  See  next  word  and  -ist. pornography,  n.,  1)  description  of  prostitutes  or prostitution;  2)  obscene  literature.  —  Lit.  ‘a description  of  prostitutes’,  compounded  of  Gk. Ttopv/;,  ‘harlot’,  and  -ypaepta,  fr.  ypxtpcw,  ‘to write’.  Gk.  tropvr),  orig.  meant  ‘bought,  pur¬ chased’,  and  is  rel.  to  Tulpvv)p.t,  ‘I  sell’,  prop.  ‘I give  for  equal  value-,  irptaptat,  ‘I  buy’,  prop.  ‘I take  for  equal  value’,  and  cogn.  with  L.  par, ‘equal’,  pretium,  ‘price’.  See  pair  and  cp.  words there  referred  to.  For  the  second  element  see -graphy.
### prison
### price
```


## [2026-09-14T00:54:51.790Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>29600 && NR<29700 && /^[0-9]{3,4}$/ {print NR\": \"$0}' KLN_1966.txt; echo \"=== nearby numeric lines ===\"; awk 'NR>29600 && NR<29700' KLN_1966.txt | grep -nE \"12[0-9][0-9]\" | head",
 "description": "Find Klein page markers"
}
```


### [2026-09-14T00:54:52.866Z] TOOL RESULT

```
=== nearby numeric lines ===
32:1218
33:1219
86:1220
87:1221
```


## [2026-09-14T00:54:57.510Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^113[0-9]$\" KLN_1966.txt | head; echo \"===\"; grep -n \"part,  n\\.\\|part, n\\.\" KLN_1966.txt | head",
 "description": "Find Klein page 1133"
}
```


### [2026-09-14T00:54:58.639Z] TOOL RESULT

```
27405:1130
27424:1131
27457:1132
27458:1133
27519:1134
27520:1135
27574:1136
27575:1137
27628:1138
27629:1139
===
3041:apart,  adv.  —  F.  a  part,  fr.  L.  ad  partem,  ‘to  the one  side  or  part’,  fr.  ad,  ‘to’  (see  ad-)  and  par¬ tem,  acc.  of  pars,  ‘part’.  See  part,  n.,  and  cp. next  word  and  apartment, apartheid,  n.,  the  policy  of  racial  segregation  and discrimination  against  the  native  Negroes  and other  colored  peoples  in  South  Africa.  —  S. African  Dutch,  ‘apartness’,  formed  fr.  Du.  apart, ‘separate’  [fr.  F.  a  part  (see  apart)],  with  Du. suff.  -heid,  which  corresponds  to  E.  -hood  (q.v.) apartment,  n.  —  F.  appartement,  fr.  It.  apparta- mento,  prop,  ‘a  separated  place’,  fr.  appartare , ‘to  separate’,  fr.  a  (fr.  L.  ad),  ‘to’,  and  parte  (fr. L.  partem,  acc.  of  pars),  ‘part’.  See  apart  and -ment.
10894:depart,  intr.  and  tr.  v.  —  ME.  departen,  ‘to  de¬ part  ;  to  go  away’,  fr.  OF.  departir  (F.  departir ), ‘to  divide,  distribute’,  se  departir,  ‘to  separate oneself’,  fr.  de-  (see  de-)  and  partir,  ‘to  divide, separate’,  se  partir,  ‘to  separate  oneself,  leave’, fr.  L.  partire,  ‘to  divide’,  fr.  pars,  gen.  partis, ‘part’.  See  part,  n.  and  v.,  and  cp.  OProvenp. departir,  and  Sp.  despartir,  It.  sparfire,  ‘to  di¬ vide,  distribute’  (these  latter  derive  fr.  L.  dis- partire,  of  s.m.).
11735:dispart,  tr.  and  intr.  v.,  to  divide,  separate.  — OF.  despartir  (F.  departir ),  fr.  L.  dispartire,  a collateral  form  of  dispertire,  ‘to  divide,  distri¬ bute’,  fr.  dis-  and  partire,  ‘to  divide’,  fr.  pars, gen.  partis,  ‘part’.  See  part,  v.,  and  cp.  depart, dispart,  n.,  the  difference  between  the  semidia¬ meters  at  the  breech  of  a  gun  and  at  its  muzzle. —  Fr.  prec.  word.
14072:ex  parte,  from  one  side  only.  —  L.,  formed  fr.  ex, ‘out  of’,  and  abl.  of  pars,  ‘part’.  See  ist  ex-  and part,  n.
18837:Derivative :  impark-ation,  n. impart,  tr.  v.  —  OF.  empartir,  fr.  L.  impartire,  ‘to share  with  another,  impart,  communicate’, which  is  formed  fr.  in-,  ‘in’,  and  partire,  ‘to divide,  distribute’,  fr.  pars,  gen.  partis,  ‘part’. See  part,  n.
18838:Derivatives:  impart-ation,  n.,  impart-ment,  n. impartible,  adj.,  indivisible  (said  of  an  estate).  — Late  L.  impartibilis,  fr.  im-,  ‘not’,  and  partibilis, ‘divisible’.  See  part,  n.,  and  -ible.
26950:fr.  L.  paria ,  neut.  pi.  of  par,  ‘equal’  (taken  as  a fern.  sing,  noun),  whence  L.  parare,  ‘to  make equal’,  compdr,  ‘equal’,  comparare,  ‘to  com¬ pare’  ;  prob.  cogn.  with  Avestic  pairyante,  ‘they are  compared’,  Gk.  7r£pvT)p.i,  ‘I  sell’,  prop.  ‘I give  for  equal  value’,  L.  pretium,  ‘price’,  OI. 'prati,  ‘against’,  Gk.  rcpoc,  ‘toward,  to’,  OSlav. protivu,  protivQ,  ‘in  opposition  to,  against’,  Gk. mipvY),  ‘harlot’,  lit.  ‘bought,  purchased’,  Lith. perku,  ‘I  buy’,  OIr.  renim,  ‘I  sell’,  ernaim,  ‘I grant,  give’.  All  these  words  prob.  derive  fr. I.-E.  base  *per-,  ‘equal;  to  sell,  to  buy  (i.e.  to give,  resp.  take)  for  equal  value’.  Cp.  par.  Cp. also  appreciate,  compare,  depreciate,  disparage, disparity,  interpreter,  nonpareil,  Paris,  ‘a  genus of  plants’,  parisy liable,  parity,  parlay,  paroli, peer,  n.,  pornography,  praise,  precious,  price, prize,  pros-,  umpire,  herb  Paris.  Base  *per-,  ‘to sell’,  is  prob.  ult.  identical  with  base  *per-,  ‘to assign,  allot’,  whence  L.  pars,  gen.  partis,  ‘part’; see  part,  n.  Cp.  pare  and  words  there  referred  to. Derivatives:  pair,  tr.  and  intr.  v.,  pair-ed,  adj., pair-ed-ness,  n.
27510:parse,  tr.  v.,  to  state  the  parts  of  speech  in  a  sen¬ tence.  —  Fr.  L.  pars,  ‘part’,  in  the  stereotypic question  Quae  pars  orationisl  (‘What  part  of speech  ?’).  See  part,  n.
27517:parson,  n.  —  ME.  persone,  ‘person;  parson’,  fr. OF.  persone,  of  s.m. ;  see  person.  The  meaning ‘parson’  prob.  arose  from  the  abbreviation  of  L. persona  ecclesiae,  ‘person  of  the  church’. Derivatives :  parsonage  (q.v.),  parson-ic,  parson- ic-al,  adjs.,  parson-ic-al-ly,  ad parson-ed,  adj., parson-ers,  n.,  parson-ity,  n.,  parson-rv,  n. parsonage,  n.  —  ME.  personage,  fr.  MF.,  fr.  OF., fr.  OF.  persone.  See  prec.  word  and  personage, part,  n.  —  ME.,  fr.  OE.  and  OF.  part,  fr.  L. partem,  acc.  of  pars,  ‘part’,  which  is  rel.  to  L. portio,  ‘share,  portion’,  and  cogn.  with  Gk.  iti- ixpu-xai,  ‘it  has  been  granted’,  ijropov,  ‘I  gave, granted’,  OI.  purtdm,  ‘reward’,  Hitt,  parshiya-, ‘fraction,  part’.  All  these  words  derive  fr.  I.-E.
27523:part,  tr.  and  intr.  v.  —  ME.  par  ten,  fr.  OF.  (  = F.)  partir,  ‘to  divide,  separate,  leave’,  fr.  L. partire,  partin',  ‘to  divide’,  fr.  pars,  gen.  partis, See  part,  n.,  and  cp.  depart,  dispart,  repar¬ tee.
```


## [2026-09-14T00:55:11.942Z] TOOL CALL #42: Bash

```json
{
 "command": "ls site/pages/398.jpg 2>/dev/null; pdftoppm -f 398 -l 398 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg398\" 2>/dev/null || pdftoppm -f 398 -l 398 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg398; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 398"
}
```


### [2026-09-14T00:55:13.779Z] TOOL RESULT

```
site/pages/398.jpg
total 2068
drwx------ 2 sfmqrb sfmqrb   4096 Sep 13 20:55 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    592 Sep 13 20:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep 13 20:53 queue.txt
```


## [2026-09-14T00:55:17.931Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg398.png"
}
```


### [2026-09-14T00:55:18.347Z] TOOL RESULT

```

```


## [2026-09-14T00:55:18.333Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:55:34.490Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN prison\"; grep -n \"prisun\\|prehensionem\\|prisoun\" KLN_1966.txt SKT.txt | head -10; echo \"### KLN prize/price\"; grep -n \"price,  n\\.\\|prize,  n\\.\" KLN_1966.txt | head -5",
 "description": "Grep Klein/Skeat for prison"
}
```


### [2026-09-14T00:55:34.572Z] TOOL RESULT

```
### KLN prison
SKT.txt:14733:prison.  (F.  — L.)  O.  F.  prisun,  Y. prison  \  cf.  Ital.  prigione,  a  prison.  — I* ace.  prtnsiontm,  ace,  of  prmsio,  a  seizing, seiiure.- L. /rKfuux,  iot  prehctuus,  pp.  of prthenden,  to  sci^e.
KLN_1966.txt:8504:comprador,  n.,  a  native  agent  employed  by  a foreign  bank  or  office  in  China  or  Japan.  — Port.,  ‘buyer’,  fr.  Late  L.  comparator,  ‘pur¬ chaser,  buyer’,  fr.  L.  compardtus,  pp.  of  com- parare,  ‘to  prepare,  procure,  purchase’  (whence also  Rum.  cumpara,  ‘to  buy’),  fr.  com-  and pardre,  ‘to  prepare’.  See  compare, comprehend,  tr.  v.  —  L.  comprehendere,  ‘to  seize, grasp,  perceive’,  fr.  com-  and  prehendere,  ‘to seize’.  See  prehensile  and  cp.  comprise, comprehensible,  adj.  —  L.  comprehensibilis,  ‘that can  be  seized’,  fr.  comprehensus,  pp.  of  compre¬ hendere,  ‘to  seize’.  See  comprehend  and  -ible. Derivatives:  comprehensibil-ity,  n.,  comprehen- sible-ness,  n.,  comprehensibl-y,  adv. comprehension,  n.  —  F.  comprehension,  fr.  L. comprehensionem,  acc.  of  comprehensio,  ‘per¬ ception,  idea,  comprehension’,  fr.  comprehensus, pp.  of  comprehendere;  see  comprehend  and  -ion. Comprehensio  was  introduced  into  Latin  by Cicero,  as  a  loan  translation  of  Gk.  xaTaXr^i?, a  Stoic  term  meaning  ‘perception’, comprehensive,  adj.  —  Formed  with  suff.  -ive  fr. L.  comprehensus,  pp.  of  comprehendere.  See comprehend  and  -ive.
KLN_1966.txt:30296:Derivative:  prismatoid-al ,  adj. prismoid,  n.,  a  prismlike  body  with  similar,  but not  equal,  bases.  —  Compounded  of  Gk.  trpi- <jp.a,  ‘prism’,  and  -oEiSr)?,  ‘like’.  See  prec.  word. Derivative:  prismoid-al,  adj. prison,  n.  —  ME.  prison,  prisun,  fr.  OF.  prison, prisun  (F.  prison ),  ‘jail,  prison’,  fr.  VL.  *pre- sionem,  fr.  L.  prensidnem,  acc.  of  prensio,  con¬ tracted  form  of  prehensio,  ‘a  seizing,  arresting’, fr.  prehensus,  pp.  of  prehendere,  ‘to  lay  hold  of, seize,  catch’.  See  prehensile  and  cp.  misprision, prize,  ‘the  act  of  seizing’, prisoner,  n.  —  ME.,  fr.  OF.  prisonier  (F.  prison- nier),  prop,  ‘a  jailer’,  fr.  prison,  ‘jail,  prison’.  See prison  and  agential  suff.  -er. prissy,  adj.,  prim.  —  Prob.  a  blend  of  prim  and sissy.
### KLN prize/price
6457:caprice,  n.,  a  whim.  —  F.,  fr.  It.  capriccio,  ‘a shiver,  sudden  start,  a  whim’,  which  is  prob. compounded  of  capo  (fr.  L.  caput),  ‘head’  and riccio  (fr.  L.  ericius),  ‘hedgehog’.  See  capital, adj.,  and  urchin.
13007:empressement,  n.,  zeal,  eagerness.  —  F.,  fr.  s’em- presser,  ‘to  be  eager,  be  ardent’,  fr.  em-  and presser ,  ‘to  press’.  See  press,  v.,  and  -ment. emprise,  emprize,  n.,  enterprise,  adventure  (ar¬ chaic).  —  OF.  emprise,  prop.  fern.  pp.  of  em- prendre,  used  as  a  noun,  fr.  VL.  *imprendere.
22601:mainprize,  n.,  an  undertaking  to  be  responsible for  the  appearance  of  a  released  prisoner  in court  on  a  certain  day  (hist.)  —  ME.,  fr.  AF. meinprise,  mainprise,  lit.  ‘a  taking  into  the  hand’, fr.  main,  ‘hand’,  and  prise,  ‘a  taking,  seizing’, prop.  fern.  pp.  of  prendre,  ‘to  take’,  used  as  a noun.  F.  main  derives  fr.  L.  manus,  ‘hand’ ;  see manual.  For  the  etymology  of  F.  prise  see  prize, n.  Cp.  prec.  word.
30308:Derivatives:  privy,  n.,privi-ly, adv., privity  (q.v.) prize,  n.,  reward.  —  ME.  pris,  fr.  OF.  pris  (F. prix),  ‘price,  prize’,  fr.  L.  pretium,  ‘worth, value,  price’.  Prize  is  the  doublet  of  price  (q.v.) The  spelling  prize  is  due  to  the  influence  of prize,  ‘act  of  seizing’.  Cp.  praise, prize,  tr.  v.,  to  estimate.  —  ME.  prisen,  fr.  OF. preisier,  prisier  (F.  priser),  fr.  Late  L.  pretidre, ‘to  prize,  value’,  fr.  L.  pretium.  See  prec.  word and  cp.  misprize.
30309:prize,  n.,  something  taken  by  force.  —  ME.  prise, fr.  OF.  (=  F.)  prise,  ‘a  taking,  seizing,  holding’, prop.  fern.  pp.  used  as  a  noun,  fr.  prendre,  'to take,  seize’,  fr.  L.  prendere,  contracted  form  of prehendere.  See  prehensile  and  cp.  prey,  prison. Cp.  also  mainprize.
```


## [2026-09-14T00:55:36.965Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD Bd2 per verkaufen\"; grep -n \"per-.*verkaufen\\|verkaufen\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10; echo \"### IEC pars\"; grep -n \"perǝ-\\|pernēmi\\|pórnē\\|pornē\" IEC.txt | head -10",
 "description": "Grep Walde-Pokorny and Mann"
}
```


### [2026-09-14T00:55:37.094Z] TOOL RESULT

```
### WLD Bd2 per verkaufen
2550:lichen Bildungen (s. o.), wabrscheinlich auch mit per- „verkaufen (bin- 
2634:5. per- „verkaufen“ (eig. „zum Yerkauf hiniiberbringen, hiniiberhandeln“ 
2646:„verkaufen“ (gr. St. perd-')^ Ttogvr] „meretrix‘’ (gegen Saussure’s Mel Xicol 
2653:rekc (Dat.) Inf. zu „verkaufen“ (ob nach Thurneysen ZfcPh 2, 81 ff., Hdb. 
2708:„verkaufen“? So Curtius 281 f.. Pick P 476), davon auch Worte fiir 
3380:2. pel- ,,verkaufen, verdienen", pel-no-s „VerdieDst". 
3387:Gr. TioohTv „verkaufen", dor. noka^ att. (Gramm.) ncok'g „Yerkauf"; ahd. 
18416:Vf. LEWb.- 4&0f, m. Lit. und u. per- „verkaufen“; und von alb. mar 
32745:bringen, opfern“, anord. selia „uberliefern, iibertragen, verkaufen“, as. gi- 
32782:opfern", ahd. sellan „uberliefern", ags. sellan „ubergeben, verkaufen", anord. 
### IEC pars
```


## [2026-09-14T00:55:46.023Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2634,2680p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Read Walde-Pokorny per- verkaufen"
}
```


### [2026-09-14T00:55:46.106Z] TOOL RESULT

```
5. per- „verkaufen“ (eig. „zum Yerkauf hiniiberbringen, hiniiberhandeln“ 
und wohl mit per- „hiniiber“, per „hinubergelangen, durchdringen^ 
urspriinglich eins, z. B. Prellwitz s. v. Tieigco, Reichelt BB. 26, 233 f., 
Persson Beitr. 641, 688); aus dem Wert und Gegenwert im Handel 
zu erklaren und hier anzureihen ist auch eine Gruppe von Worten 
fur „gleich, vergleichen, begleichen‘‘; noch naher der ersten Gruppe 
steht eine mit der Bed. „zuteilen“ (s, dazu auch per- „gebaren“). 

1. Gr. Ttegvrjpi (Praes. und Impf.), :regdco, -c5 (form ell == Titgdoo „dringe 

durch“), l7tigao{p)ay und TitTigdoxco, Tiegdoco (att. Inigaoa, TtEJigdxa 

„verkaufen“ (gr. St. perd-')^ Ttogvr] „meretrix‘’ (gegen Saussure’s Mel Xicol 
511a 2 und Meillet’s Dial, i.-eur. 68 Gdf. pora-na s. Persson Beitr. 687 f.); 
air. renim „verkaufe“ {*prna- ; gr. Ttegvd-)^ Subj. St. ria-, z. B. m riat „ne 
vendant“, (*rf«- nach Ind. [p]yi-na- fur '^perci- eingetreten; fordert als 
Gdlage nicht ein idg. *pn- als Abl einer von J. Schmidt FestgruB an 
Roth 186 angesetzten Basis pero\i\-^ s. gegen diese auch Persson Beitr. 
746 a 3; Tigiapai „kaufe“ gehort zu ai. Icrimti)^ Pf. ni rir „non vendidit“, 
rekc (Dat.) Inf. zu „verkaufen“ (ob nach Thurneysen ZfcPh 2, 81 ff., Hdb. 
415 im Auslaut nach icc „Heilung, Bezahlung*’ gerichtet? Wahrschein- 
licher nach Zupitza ZfePh. 1, 466 f., KZ. 36, 237 aus ^prq-nd von einer 
alten Gutt.-Erw., vgl.:) lit. perlih „kaufe‘' (freilich nicht „verkaufe“); 
auch lat. merx^ mercdrl^ merces^ osk. aminmiud (s. a. meric- „fassen“) durch 
EinfluB von mercor fiir "^perlc- eingetreten? 

Curtius 273, Persson Wzerw. 21 a I, 93. — Aisl. (rtfir „bezahlt^^ (Kluge 
Stammb. 94, J. Schmidt FestgruB an Roth 186) ist wohl kein Zeuge eines 
*p{€)r7- : s. o., sondern eher als ,, durch Zahiung befriedigt^^ = aisl. 

frlp^' „hubsch‘*, ai. pritd- „befriedigt, erfreull 

2. Av. pairyente „sie werden verglichen^*', aipi-par- „(seine Schuld) be- 
gleichen, BuBe tun“, d-paroti-s 5 ,Suhne**, para^a- n. ,,Ausgleichung (einer 
Schuld), Suhne, Strafe^S para- m. „Schuld^^ (dazu wohl auch par- „ver- 
urteilen‘*), nach Bartholomae Y b. 849 zu lat. par^ parts ..gleichkommend, 



per- 


41 


gleich, Paar'', paro, are .,gleiclischatzen'S comparare „vergleichen“ (umbr. 
parsest „parerit“?? s. t. Planta I 494, II 325 f., Sommer KE. 108 f.).
```


## [2026-09-14T00:55:47.689Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD prek fragen\"; grep -n \"perk-.*fragen\\|„fragen\\|prek-\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -15",
 "description": "Grep Walde-Pokorny fragen"
}
```


### [2026-09-14T00:55:47.739Z] TOOL RESULT

```
### WLD prek fragen
1886:C. Kons. Erw. von per-- s. noch u. "^perk-^ prek- „gesprenkelt**, pers- 
2869:perek (perk-, prek-, pjk-) 
2872:perek (perk-, prek-, prk-) "^fragen, bitten“. 
2883:for sea „Forschung, Frage“ (wo von for scon „fragen, forschen^), i-St. arm. 
2899:„rogavermt, decreverint" ; got. fraihnan {frah, f rehum) „fragen“, anord. 
2903:fragip ahd. „Frage^^ {frUg-dn, -en, frahen „fragen‘0, anord. 
9437:m. „KenneF‘ (: gv, nevoriqQ-iog „fragend'^, Aesch.) : av. baodah- n. „Wahr-
```


## [2026-09-14T00:55:54.478Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2869,2910p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Read WLD perk fragen"
}
```


### [2026-09-14T00:55:54.525Z] TOOL RESULT

```
perek (perk-, prek-, pjk-) 


perek (perk-, prek-, prk-) "^fragen, bitten“. 

sko- Praes. ^p>Ji-sko^ woraus "^prsko: ai. prcchdti „fragt'‘ {praksyati^ 
dpmkslt, pritd-, prastum), av. pdrosaiti jsfragt, begehrt*^ (Ptc. parsta-)^ ap. 
aparsam ,,ich frug“, lat. posco ,,fordere, yerlange, bitte aus“; ir. arco „ich 
bitte“, cymr. archaf, corn, arghaf ds., mbret. arclias „il commanda^ (air. 
inun-chom-arc „gegenseitiges Fragen, Begru6en“, nsw., s. Pedersen KG. II 
457 f.) mit ar aus r vor dem s der Gdf. "^prskd (s. Pedersen KG. I 44, 
81), vielleicbt lit. perszhy plrszti ,,fur jemanden freien“ {pirszlys „Frei- 
werber'^), wenn mit analogischem Praes.-Ablaut e statt i (kann aber trotz 
praszyti auch ^perkU sein); dazu ai. prccM „Frage, Erkundigung^ = ahd. 
for sea „Forschung, Frage“ (wo von for scon „fragen, forschen^), i-St. arm. 
hare „Frage'S harc-anem „ich frage'‘ (Hiibschraann Arm.-St.1 38); IdLi.posttdo 
„fordere“ (ursprgl. milder als posco, und Deminutiv auf ido vom Ptc. ^posc- 
-tos zu posco, Sarauelsson Gl. 6, 238; anders Kiedermann lA, 29, 35); im 
Osk.-Umbr. ist ''^porsco nach nicht mehr nachweisbaren e-stufigen Formen 
zu *persco umgebildet; umbr. peperscust „precatus erit“, dazu (mit For- 
mans ’{e)lo) umbr. persclu, pcsclii „supplicatione'‘, ferner mars, pesco „8a- 
crum'S und vom Ptc. *pes[c\to- aus osk. pestlilm „templum'‘ (Formans wie 
z. B. in vinculum, „Ort = Mittel, Gelegenheit zum Beten“). 

Dagegen osk. comparascuster „consulta erit'*, kilmparakineis „consilii“ zu 
lat. parco. 

Ai. pracna-, av. frahia- m. „Befragung, Frage‘-, arm. harm „Braut, 
Keuvermahlte, Schwiegertochter'' (vgl. die germ. Praes. wie got. /’ra^Anan) ; 
lat. procus „Freier“, prex „Bitte“, precor, -art „bitten“, umbr. pepurkurent 
„rogavermt, decreverint" ; got. fraihnan {frah, f rehum) „fragen“, anord. 
fregna, z.%s.frignan (nni io-’Pra.es. f riegan) ds., as. pYaet f ragn ; ags.friccea 
„Heroid'' (: ai. pragnin- „Fragesteller“, Kluge Festgrufi an Bohtlingk 60); 
anord. frett f. „Frage, Erforschung*^ ags. freht f. „Wahrsagung“; got. 
fragip ahd. „Frage^^ {frUg-dn, -en, frahen „fragen‘0, anord. 

fr^gr, ags. gefrmge, as. gifragi „beruhmt‘‘; ahd. fergdn „bitten“. Lit. 
praszan^ -yti ,,fordern, bitten''; aksl. prositi „bitten", — Wesentlich nach 
Ebel KZ. 3, 444, Vanicek LWb.^ 164. 

Gr. '^EOTigoTiog „Trahrsager" (L. Meyer KZ. 22, 54ff., J. Schmidt KZ. 25, 
130, Schrader KZ. 30, 472; man nahm Formans uo oder Assimilation aus
```


## [2026-09-14T00:56:02.607Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS\"; grep -n \"purs\\|fras\\|frašn\\|frasn\" SNS_pages.txt | head -15; echo \"### SNS page 141\"; awk 'BEGIN{RS=\"\\f\"} NR==141' SNS_pages.txt | head -30",
 "description": "Grep SNS"
}
```


### [2026-09-14T00:56:03.711Z] TOOL RESULT

```
### SNS
2786:                                                                                                                           .**»Lm     .   >£-*S « *jjli* ',j-jtf*A     iharapursaglh: -*CJA*W4>4?
2787:                                                                                                                                          •   YA/1*»^    -TV**5 .(ij±>~sj hampursal:^
5189:                                                                                                                           paitifrasa- :L-
5556:                                          ,^j» <i&«> rfrasang:       3V->^0                                                                                   1       *A>>C>tV/?1 iS
5560:                                     U/T^ •(&&*) frasang :^                   |
5592:                                                                                      J   ko*^V* s      *="- ,   |--tf-okt5 *u»> «»=•-->:frasast: **>» -uJe>
6013:                                          ,*** : pursid: v*~>»«>
7344:                                                      1003)frasp,r3»a-              j'*
9518:                                                                                                                            *        ji   :m5nsr pursldfir:            \**k>-*>»o    J.of-6
15177:                                                             parahaoma- 125/23          frastuyS 132/22
15179:                                                             parana 125/14              frasparaya- 177/7
15214: nava-pixa- 143/16         paitifrasa- 116/13
15911:pursld 141/10              ratustaitlh 226/6                 ravisn 229/7           rOzag 230/12
15912:pursldar 141/14            r3y 224/11                        razmlgan 226/12        rOzaglha 230/14
15913:pursisn 141/15             rayenSd 224/23                    rScar 233/5            rSz saban 230/11-337/1
### SNS page 141
                         ,Uj --w
                            fc
                                   U*^0^
                                                                                                                                      Us is-«U *»|j •£!•                                                    W
                                                                                          .*;*£•& Jj»   •            >
                                                                                                                         .
                                                                                                                             i
                                                                                                                                 tj"ii.ii ' o'jj *^j* :margarzan:
                                                                                                                                            1
                                                                                                                                                                                                WtViobf
                                                                              jjlj      ^     *ljl«-        T oJ     U r Uol ^^U^.US                              .     j« j
                                                                                                                                                                      l5t      ^^ c ^k.l               jj



                                                                                               (       <iw :«&) •-^/.j.o'jj ^ '^- r                           1                1   l
                                                                                                                                                                                       -^* l   o1>^o T
                                                                                                                                                        .   TT-T l-IA-ir-W-A-T/A^
                                                                      .   a   :
                                                                                  -
                                                                                      » Jj.jiji^. aS^LS ^bljjUT^ :margarzanan:
                                                                                                                 ,
                                                                                                                                                                                        tri-O-o^-tf




                                                                                       •^WoVi'^^'tfA^jM^'ob                                     1
                                                                                                                                                        ^ :margarzan: W^»^
                                                                      /V««5.T-T/A^ WA-UY-Ufr-ni-A6-AT^Al-Yf-ff-?T-fo-n/T^
```


## [2026-09-14T00:56:04.315Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT paiti.fras\"; grep -n \"fräs-\\|frās-\\|paiti\\.frās\\|paitifräs\\|frãs\" BRT.txt | head -20",
 "description": "Grep Bartholomae for fras"
}
```


### [2026-09-14T00:56:04.393Z] TOOL RESULT

```
### BRT paiti.fras
```


## [2026-09-14T00:56:18.720Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"frasna\\|fras\\b\\|paiti\\.fras\\|paiti\\.par\" BRT.txt | head -20; echo \"=== around 17890 ===\"; sed -n '17880,17900p' BRT.txt",
 "description": "Grep Bartholomae frasna"
}
```


### [2026-09-14T00:56:18.804Z] TOOL RESULT

```
3025:ihn"  Yt  /^.gö;  ■ —  zaraiuströ  asar>lä  °ka  ,  upa.dvqsaiH  maxUJiihrpa   >nyaitya  fras-
3629:•  j.  apa-srayamna-  Adj..,  PPM.:  s.  sray-. m  j.  apa-za<)ah-  Adj.  (auch  fem.)  'den Steiss  ab-,  weghaltend  (nach  oben?)''*, von  der  Fliege:  ^maxsiJiihrpa  prrfaitya frasnaol  °Sawi4ff(GSf.))  * akaramm.driwya (sd.)  V.7.2.
4054:Ableit.  —  Eig.  'der  beim  (zum)  Gegenstand seinesWunsches(gelangtlist''.— Pü.!fljafiin(?). --  I)  Zum  o  s.  S  ^94  Nlr. «  j.  afraslh'vant-,  äfrasäh'vant-  Adj. (fem.  'vaili-)  'den  Wunsch,  die  Hoffnung erfüllend,  selig  machend':  a/f«  .  .  afra- satihaitim  V.  52.  i.  a)  mit  Dat  comm.: dsyh  ml  Stars  puhra  ahurahe  mazd$  yS
4056:ml    atfhat    afrasätphä  .  .  vaAishm  ahlim "verleihe   mir,  o  ^.,    Sohn   des   AAM., womit    er  mir  den  Wunsch  erfüllen  soll, das  Paradies  . ."  V.62.6. Eig.  "beatum  (beatos)  babens'  sva.'reddens'').
6073:—  yS  möi  'säi  haülm  (sd.)  hatä  var9saiti\hnii  'sähe  yat  vahistahe  (näml.  ratavö) Y.  46.  19;  —  spinia  mainyB  vahiiiäcä  \  mazds.frasästa  .  .  Y.  7. 10;  usw.  0)  GS. manatjhä  'säl  haiä  lyaohanäcä  valaahälä  ,  mit  gai'^ä-  (sd-,  auch  fdSt)'*:  'sähe  gatia ahmäi  dqit  .  .  mazda  "für  den  heiligen  |  Y.  ^.  3 ;  usw.  e)  AbL  mit  haca  dnw. Geist  und  für  das  nach  dem  göttlichen!  2  a  ß,  mit  vahista-,  yazatoHbyB  . .  y5i Recht  beste  Denken,  Handeln  und  Reden  I  h^nii  yasnyäca  vahmyäca  'sül  haca  yat wird  uns   -"  Y,  47.  i.         b)  im  jAw.:  1  vahiltät  Y,  1. 19;  77.  10,  V.  j.  2,  Yt  8. 15,
6134:vakiltfm  Yt/7.18;  V. /Äi6;  —  'hm  vahi- shm  staohwfm  (sd)  Vr.  2.6;  —  'saie  vahi- itahe  staokwahe  Vr./.4;  —  taraiuiirahe .  .  yim  slaotarTm  'sähe  yal  mazistahäa vahislakeca  sralstakeca  YtJj.  9z;  91;  — vanainitmcä  uparatäbm  yam  °sahe  vahi- HaAe  paiti.parstlmca  ■ma^rahe  ipmtahe Yt.  }o.  zz-  S.  noch  'a/a-  aK  mit  No. 30.  [Yt/J.91:  lies  awm^rav3\  —  H. 1.3:  lies  ahniJtuts^
7013:r  bei  aÄqw.  —   n)  NA.  ojyna'ä;    s.  Ho.  %'•  frasäUpayäH    Yt  Ä  32  f.  a)    vor   yät:
7025:frasüsat  ar?dvT  . .  J"  aoxta  ar)dvi  Yt5. 8;  V.  :ji.\2  2St;  —  äat  (s.  8)  ml paoiryäi risväi  xsafne  atars  .  .  nmSnS.paitim yHsaiti  .  .  iV  ml  bityiii  . ,  v<lstrlm  /suyan- t>m  yasaiti  .  .  ä'  tnl  ^rityäi  . .  sraosfm yäsaiti  V.JtV.iS— 22;  —  itir&  mt^rahe frayana  (sd.)  ,  .  ä°  hva  pasu  vfra  vasö.- xsa^rö  fracaraitt  (sd.)  Yt/0.  112;  — miiir^m  .  .ynihe..frada%at  ahurö  mazJit balvari  döthiariqm  .  .  ii°  nbyö  döiiräbyö ..spasyeiti ..  ä'  '..\Llo.Zz;  28,101  (vor j-a/), /J.68,  H.2.10,  i4iSt,P.jiS'2St(vor
7247:—  n  Hds.  äi7^i  s.  No,  6.  —  S)  Die  Hds,;  54.  A)  zusammen  mit/aJÄ,/flJirfli?a  und mit  Pü.  und  entsprechend  die  NA.  teilen  /j/;  ,j=  ^Aj^a  dva.dasa  karia  JrakUrayöis falschlichhinter/.™.-abPfi  :«/«-■  A>a-,W  _  s'  fiascaHa  ..  V.^.j,  5.52; spamiaramal  o  lata  .  .  ak  bciomand  .  .  valtum  ■'  '  ._,-  ,,■-,..,■  ^.X,  _  _ ^ä»ik(No.al).-9IFms«.jNA.w««.-|—  «^  /'"''  "1^-'  Aisiaitt  ..  tutryo  ..  a' 10)  NA.  ädqm;  s.  No.  6.  —  >')  Nur  gAw.  und  I  iaf  dunmqn  hqm.hi!t3nti  ..  ä°  tat  dunmqn nur  bei  n».)«.  —  ")  NA._  äwurfä ;  %.  '^o-  6\fras(iufayäti  YtÄ32f.  a)  vor  /j/; "^K  '^;  ~j  '"  ^■^.,'"i?^'  "■'!''■  ^'""  ?.'^^° '  1  j'öitim  J  ahmät  yat  hanS  . .  bavät  a°  yat
7255:aoxta  aAurö  mazdä  N.  2. 3ti.; —  äat(s.Z) frasüsat  andvl  . .  ä°  aoxta  arsdvl  Yt5. V.  22,i  iSt.;  —  aat  (s.  8)  mi paoiry3i T/äi  xSqfne  ätari  .  .  nmänS.paitim yäsaiti  .  .  ä'  mE  Htyäi  . .  v3strjm  ßuyan- t3m  yiJsaiti  .  .  ä-  ml  ^n'tyäi  .  .  sraoi3m yäsaiti  V.  7<S',  18— 22;  —  ci^ra  mürahe frayana  (sd.)  .  .  ä°  Ava  pasu  vira  vase.- xsa'hrö  fracaraüe  (sd.)  Yt.  10.  112;  — mi^nm  ..yaiAe../rada'ial  ahurö  mazdä ban-ar}  düikranqm  . .  ,r  äbyö  di'i^rabyS ..  spasyäti ..  ä'  ..  Yt./o.82;  28,  101  (vor yat),  JJ.68,  H.2.10, 14  iSt,  P.  j^'aSt.  (vor
7310:•  j.  äfrasäh'vant-  Adj.  (fem.  -vaiti-): s.  unter  a/ras\
8195:vor  dem  ersten  Glied;  'ta  buyä  afrasaiiitil 'ta  äSu^.sravä  AacimnS  Y.  /;.  i ;  —  E  gau- mülJ'  .  .  adlru^  k^bajiyam  °tä  psrsam 'tä  mudam  'ta  aniyil  daAyav^^h.i.ii'i*; loJ*',  iii*>,  2.13*,  14';  — fras'a  upa.- Siiiidayäti  tni^rS . .  'ta  nmänjui  °ta  vXs?m 'ta  . .  Yt.  /o.  i89.  b)  beim  letzten  Glied zusammen  mit  a)  td,  ß)  /i^  (s.  auch  II  2  a) 'und  auch';  a)  barat  i^amiS  , .  baSsas>m 'ta  anumca  Vt/^.2.  ß)  yat  upanhacat taelyantqm  vprpiräjanfin  'ta  anySsat'"' haxayS  Yt.  /().  89;  87;  —  Aazar^nm Vij^wA  bavaiti  'ta  äsmmcit  frazaintm Yl  /<V.  5.  II)  zur  Verbindung  von  Sätzen; i)  bei  gleichem  Subjekt:  \  hauv  käram fraisayi^  ..  'tJsiJm  i  martiyam  maiistam aiunaus  Bh.j.^;  l.iS,  2.4,  13',  14',  16, 3.7,  II,  4-2,  16,  I70-I'.  D-4.3,  X.7.3; —  babirum  asiyavam  vasna  a'urtrmaz- dähJ'  °/(7**  babirum  agarbäyam  'tä  avam .  .  agarbJyam  "ich  zog  nach  Babylon und  nahm  nach  dem  Willen  AhM&. Babylon  ein  und  nahm  jenen  .  .  ge- fangen" Bh.2.1-,11  — ya'^a  az?m  banäa- ytni  .  .  fraiirasyätam  'ta  .  ,  vdaayeni  'ta .  .  upanayeni  YL5.18;  9^,  31*,  5.34,  82, ;;.2,  Y./0.4,  F.p»  FrB.  a)  Das  Sub- jekt ist  wiederholt:  'ta  drvh  asp>m  *viste\ 't.i  drva  .  .  yavanhim  *viste  Aog.  ^2;  —  | da'iäni  li  .  .  'ta  tl  az?m  afrlnäni  V,  22. 5.  a)    bei   verschiedenen   Subjekten:
8565:td^w^m  frasnat!e{sd.)  ürisataüw^m  upa- srt'We  ayiyqm  (sd.)  paiti  'snäitimV.S.qZ.
9788:•  j.gao-dana,  °jiana-  n.  1)  'Milchgeföss': frä  tl  Aasaanm  xam  aam  . .  frasnaymi ''.an?m  avi  hatUaiinh  ya^  asti  puirake >rims"^e  tausend  Quellen,  die  zum  Milch- gefiss  zusammenfliessen,  das  die  Nahrung des  Kindes  ist"  V.  21. 7  ".  s)  überh. 'Gcfäss,  Napf,  Schüssel'  (nur  Komp.,  s. N.  64).
9840:ayasöis  yaont  fiairi  uxsän.>fn  bix^'^rgm (sd.)  .  .  V.  7p,  21;  —  »sj«  pas^aSa  upa- t3har?Z3m{^A^  V.p.  14;  —  catura  frasnana frasnaySit  °z3m  gava  daiäya  bis  äp>m tnazdmätaya  "vier  Waschungen  nehme  er ' vor  mit  Rindsurin,  der  vom  Rind  produ- zirt,  zwei  mit  Wasser,  das  von  Matdah geschaffen  ist"  V.  75.  22"'.
11147:—  '^wärS  ahurum  vairim  frasrävaysii V. /Ä43";  —  bawranqm  *°turS  (Am.)  3' aJzanatqtn  (sd.)  Yt5. 119;  —  '/«ra  (An.)*' frasnana  frasnaysit  V, /p, 22;  —  aivake pasvö  .  .  jfos  .  .  %ryqm  .  .  °turqm  N.  65;
11941:•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'  usw.  gebraucht  werden: ya  anrS  mainyui  frak?rfntat  avi  imqm 'nüm  yam  masyänqm  V.  20.3;  5;  s.  noch lu  aj  —  ks , .  a%r3  tafitus  äärayat  'naot haca  maiyehe  V.  20. 1 ;  —  yasca  .  .  dax- manam  avavantim  mazS  vXkänayat  yaha hl  'nui  anhal  V.  7. 5 1 ;  —  {yai)  *may'iain 'nUm**  aiwyästam  (sd.)  "irlris  .  .  N.  p5; *95^>  —  '*'"'  panna  (sd)  °nBm  aiwi.- si/ais  YX.  14. ^5 i  —  yaf  kl  'nus  hiskvi Aiynvi  (sd.)  pqsnu  bavai  V.5.31;  —  &«.- ayarpm..  'nüm  frasnayayania  Yt/0.  laz; 133;  —  US  'nüm  snayaita  us  *vasirä  V. J.  54;  —  "^ris  frasnaiti  •nunqm  . .  vastra- nam  V. /2.  a;  —  hakmt  aps  hvqm  'nüm pairi yaozdai^ita  V.  (),3i;  31",  ä  36,  37, 39,  Vd./5,  ig*,  20; —  Ja/  vlspam  kvam 'nüm  ayaozdata  k>r>naoiti  V,  ■¥.40;  — yal fU  zasta  nöie  frasnäta  aai  vJspam  hvqm 'nüm  ayaozdata  ik?n>»aoiti  Y.S.40; — yffi Aqm.nasüm  paitiäristfm  °nüm  yaozdai%yqn V.g.i;  —  iia  iristahe  'nüm  avaMsta  .. isaaa  (sd.)  ml  yaoldaitim  V,  Ä  100;   —
12012:•  j.,  g.  taya-  i)  Adj.  '(diebisch  sva.)  ver- stohlen, heimlich':  yS  frasäi^A.)  ävllyä  yä va..*p3r?saaiya(^Va.)\.3i.i^.  2)  m. a)  'Dieb':  'yaY.18.  b)  'Diebstahl'!?): °yS^'>  F.  25  b,
13680:•  j.  dunman-  n.  ''Nebel,  Nebelwolke, Wolke':  yayata  'ma  ,  .  frä.ap3m  nyäpftn upa.3p^m  (sd.)  V.21.2;  F.^g;  —  apim.. MdSrra  vat>m  'mqnia  ¥.5.15;  —  naioa 'man  utjasaiti  haratky3  paiti  banzayä "und  nicht  steigen  Nebel  empor  von . ."  Yt. 10. 50;  —  Hat  tat  'man  hqm.hishnti  . .  äat tat  '"tan  frasäupayeiti  (sd.)  magyS-kara Yt  S.  31 1
14580:•  '].  STi.ayar-  n.  'Zeit  von  drei  Tagen': As  ava%a  vazata  °nm  ^ri.x/apanm''' ", .  drei  Tage  und  Nächte  hindurch"  Yt 5.62;  S.22;  —  °r3m  ^rijxsapanm^'  tanüm frasnayayanta  "während  dreier  Tage  .  ." Yt/o.iaa;  V.p.sö.
=== around 17890 ===
um— '(Akk.):  :fan^xS pirgssmnaZiula V.J.  29'\  11)  mit  Neg.  'nicht  fragen nach  — ,  sich  nicht  kümmern  um  — '  (Gen.): ''ySi  nsil  driyaol  .  .  avat»ftasca  *äraära- heia    *p>r3sänte^'>  V.44.  12)    'richten,
strafen'^';  mit  Akk,  a)  II  der  Person:  mar- tiyi^  kyc^  .  ,  avam  *^uiaratam  abaram  I iSya*  .  .  avam  *'^/rasatam  (sd.)  sparsam  j Bh.^.  13;  7.  8;  —  avaiy  akifraltsdiy  (sd.) /arJjBh.4.14;  5.  b)  dcrSache,  in  Ver- bindung mit  IS.  frasa  (sd.):  yä  frasä aviSyä  yä  vä  ..  *p^nsam  (3DPM.,  als Pass,)'°*  taya  Y.jj.13.  Wertlos:  tatiBm p>nsänte  Vyi.40.
m\Xä  i)dnwS.  la:  ä  dim  pimat  zara- %uärs:  kö  .J  Y.p.ijNik./.  i)Med. dnwS.  7:  kP  vS  asa  a^raiVj  "wer  wird  sich von  A.  beraten  lassen?"  ¥.57,11.
mit  paiti,  piUiy  1)  'Jemanden  (Akk,) fragen''  poiti  mqm  ..  pmsanuha  ..  avaha *atghä  spanyä  yesi  mam  paiti.ptnsBrfhe  V, 18.  7.  a)  es  folgt  dir.  Frage:  paiti  dim
pfrtsal  zard^uiirS  . .:  kana  %wqm  yasna yazsnel  YL5.90J  94,  8.  57,  /o.iai,  i2.\, Vyt  2i\  —  paiü  dim  p?r>sata  zardäiu^trS . .:  AaJ  .  .i  V.p.  43.  a)  zugleich  mit Akk.  des  Inhalts:  nsit  dim  yava  .  ,  bitim väHm  paili.p)r»s?mnS  bva  (Sp.  929  u.) V.  iS.  19.  2)  'Jemanden  (Akk.)  aus- fragen, ausforschen'  (s.  Simpl.  5):  *naire aiaone..paitica*p»r}smanäi"^  xratüm  a^a- vansm  N.84;  —  paifi.parsta' .  3)  II  (spez. Geschriebenes  erforschen  sva.)  'lesen';  tu- vam  kä  hyt^  aparam  imäm  dipim  pafi- parsäAy  S\\.  4.  6;  —  mätya'^  kya' aparam imäm  dipim  paiiparsätiy  .  ,  Bh,  4-  8-
mit/rä  — ?  — :  jo/  vä  frä  uHtctätöi^ti) *p3r9S3nti  N.  61.
mit^an  i)  'Jemanden  zu  Rate  ziehen': S.  Absol.  hqm.parstim  und  Inf.  hSmfar- iidif.        2)  'sich  beraten  mit  — ,  beraten
(Akk.):    daiva  ml .  .  aei?m  ham.p>r?Sfnte
V./5.3.
ü.  pfcchiii,  aprof/a;  pflld^i  np.  pursad.  — Pü. :  pursüan,  kantpursUim  oder  umschrieben mit  fao-siht,  puriümh,  fartakVi,  pursiläri  s. noch  No.  7  f.  —  ■)  Nur  \a  p>rfsmana-  Y.30. 6,  *N.  S4.  Die  Bildung  ist  aufKUig.  —  >)  NA. par>s';  s.  Vir.  lu  Yt.  S.  15.  —  3>  jAw.  nnd gAw.;  ».  dsiu  Btiu-  W.g.  264.  —  0  S.  iSt Btkl.  AF,  2.  175.  —  5)  S  335-  —  *'  Vgl. Hbh.  ZC  333.  VIL  aber  vertritt  der  AbL vielmehr  den  Listr.  wie  bei  tnai,  s.  ebd.  240. —  7)  PS. :  j^ariin  faa-tiin  r& ,  erL :  tik  am dahäl  'bis  er  mir  gibt'.  —  ^  Hd*.  ptsinte ; Pü. !  kampitrsäid.  —  9)  VgL  zBed,  arm.  für- n!n  TroMSs'.  —  "»  Pt4  osw.;  IF.7.  216.  — ")  Hds, /flTjjiB*;  t.  No.  1.  —  ")  himi  ist nach  dem  Metnim  tu  sireichen.
•  0->)  g-  frasa-  m.  i)  'Frage'  (nur Komp.).  2)  'Zurateziehen,  Erforschung, Studium'  (nur  Komp.).  3)  'Gericht, Strafe',  nur  IS.  'sa  mit  V,  Jras- "'  'etwas bestrafen.mitStrate ahnden':  yä  'sä  avTsyä yä  v3  maadä  *pir3saai  tayä  "welche  offen- kundigen oder  welche  geheimen  (Taten), o  M.,  mit  Strafe  geahndet  werden"  Y. j/.  i3'>.
KompE.  ~  Zum  V./roi-.  —  Vgl./raiJ-.  — Pü.;  hamfursel,  Sä.:fj-cc/iaii.  —  >)  VgL  zAusdr. Bthl.  1F.  7.  326  mit  Bgm.  IF.  6,  loi;  s. femer  anumatay-,  usdaiza-,  pairi.fräsa-.  — >)  Vgl.  iSl.  IF.  7.  226.
•  j,  fra-saxta-  Adj.,  PPfP.:  s.  'sak-.
lassen  VI
' (JaSti.):  Ayai  ASm  vohs  masdä  4,&,  Vi.g.ö;
•  j-  '/ra-sasta-  Adj.  'rühmenswert"*. Ableit    —    ai.  piiüattä-  Adj.   'gerühmt'.    — ')  PPfP.  im  Sinn  de»  PFP.
•  j.  fra-8asta-n.'Riihmen,Ruhm':  akmäi saokäi  'täi  fraväkäi  Uta  */ramainyäi{sd.) Yt/tf,3;  —  'ia  F.  13.
Zum  V.  saai-i    am    ai.  'praiastha:    —   Pö.: fräl  ä/rinaiän.
•  j.  frasasta'ä-  f.  'Würdigkeit  gerühmt zu  werden':  aztm  dahqm  . .  aom  stänm yim  tillrJm  ,  .  avänfom  'sastata  (IS.)  Yt. «so.
•  j.,  g.  fra-sastay-  £  i)  'Anweisung,  Vor^ schiift' :  ai'aAe  paiti  pantqm . .  mahnm  ..'Um V.4.43.  2)  'Ruhm,  Lob';  DS.  undlS.  als Inf :  hävanse . .  yasnäicä  vahmäÜa  xsnao- %räi{Stvitz.)äi  Uayalla  Y. /.  23  usw.;  Yt
dby  Google
```


## [2026-09-14T00:56:33.528Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.fräsa\\|pairi\\.fräsa\\|pairi\\.frasa\\|Befragung\" BRT.txt | head -10",
 "description": "Grep Bartholomae frasna/Befragung"
}
```


### [2026-09-14T00:56:33.586Z] TOOL RESULT

```
9008:24  genannten  Bergs,  anj^ebl.  idiidräsfi,  den man  für  idenlkch  hielt,  s.  vunStackelber<i WZKM.  12.  239. •  j.,  g.  ka'iH  Adv.  1)  "wie?,  in  welcher Weise':  "^il  '>,wä  mazda  xlnaoiiii  {%A^  V. 4O.  1;  —  °^ff  zaoia  gidh  /rasrävayätti N'.W;  Vyt.j/C?);  —  -^d  ffjv7w»»  ^/-a.- iri^j-S  Oa  ..  ii/aJasJ  "wie  ists  geschehen, dass  du  . .  gestorben,  wie  dass  du  .  ." K.  2.  16;  16;  —  °ä(7'>  ajfiirS  daxsära fiiasaysi  dlsil  "durch  welches  Zeichen "' willst  du  die  Tage  kund  machen  für  dte Befragung?"  Y,4j.  7".  a)  als  Indefini- tum,  a)  mit  vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  'nicht irgendwie':  *'mä',a  ^'i^aäna  paitt.Jime  (.sä.) Vr.22.3.  2)  'wie  so?,  was  ist,  heissi das?,  was  hat  man  darunter  zu  verstehen? (die  Antwort  wird  mit  ya'^a  eingeleitet) °>a  alvö.gäimi  ra>a  '^ripai^m  "'wie  so eine  Schrittlänge?'    'Drei  Fuss'."   V.  5. 8;
15838:•  j.  "parStay-  f.  '(gegenseitige)  Befragung, Disputation':  yS  .  .  gaot)ma?ie  (sd.)  parSyä HSit  avaiti  \t13.16.  LS.  'ta  als  Int sbes.
17891:KompE.  ~  Zum  V./roi-.  —  Vgl./raiJ-.  — Pü.;  hamfursel,  Sä.:fj-cc/iaii.  —  >)  VgL  zAusdr. Bthl.  1F.  7.  326  mit  Bgm.  IF.  6,  loi;  s. femer  anumatay-,  usdaiza-,  pairi.fräsa-.  — >)  Vgl.  iSl.  IF.  7.  226.
17908:•  g.  fsrasä-,  fr°  f.  i)  'Frage':  ahya  'ssm (AS.):  iahmäi  vXviduye{%A.)  va^i  ai  a.. mtam(sA.)  "auf  seine  Frage:  "Wofür  .  .? 'Bei ..'"  V.43-  9''-  2)  'Fragen,  Befragung Über-'  (auf  mit  LoL):  ia^5  (sd.)  ayärS ..'sayäi  lifsä  aibJ  %iWäka ga/knAa  lanusica
17909:■  "..  für  die  Befragung  über  das  Deine  und dich  selbst?"  Y.  43.  7  ">,  3)  'Sichbcraten- lassen  von  — '  (Gen.):  y5i  asru/ßt/ (sd.) pgnnäafß  nl^il  aiahya  advvyeintl  (sd) *hatSna  nSi£  'saya  (IS.p'  vaahSus  cSxnarS mananhs  "die . .  nicht . .  noch  darum  Sorge tragen,  sich  von  VM.  beraten  zu  lassen" Y.  44. 13"-
22272:pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw.  der  GiJhäs"'>: tiiranam  haurva.paoiryanqm  (sd.)  häiliSla afsmanäca  vacasca  va^astaslim{sA.)ca  Vr. y.  3;  —  *ey3mcit  .  .  väcitn  gä^anqm asrvUm  (sd.)  N.  103;  — yS  gä^anqm  Byam vScim  afayäiti  alvqnt  v3  vacastaltXm  N. 4s\  42;  — ys  asnitgaoia  v3  ajravaoco  va nBii  Sim  Smm  väcim  *aiwyHs  (Sp.  378  0.)  \ .  .  yezi  äat  Syumpt  *väam  *aiwyas  1 anaiwilfi  (sd.)  astryeite  N.  i4-  Undeut- liche oder  wertlose  Stellen:  sar^yO  vaxs FrW.fj.i;  —'kaityavaca  FrW.5.2; — yS kaca  damayät . .*apastv6it  '^rilvayzibis^'^ ^haktni. .  N. 41 "';  —  xsvas  vayeibis^i N. 6j,  /OJ'J';  —  aAunavaitim  gshqm  .  .yasa- maide..  mal  vay£iby3^Va'*>  *pdübyasca V1.14.1;  YLz,  II,  13  (vacqm).  S.  noch vacim  bes.
29132:♦)  Der  M^ra  (sd.)  lerfillt  in  iwei  Teile,  den eigentlichen  M.,  den  AHM.  spontan  ofTenbart hat,  and  den  H.,  der  auE  besondere  Befragung mitgeteilt  oder  von  Sehern  erschaut  worden  ist, daher  letzlerer  die  Bezeichnungen  taini.parila- 'vom  Kundigen  (d.  i.  Zarii%Hllra)  erfragt'  und upaiti.^lubyd  gtripta-  'von  den  Sehern  wahr- genommen' führL  Vgl.  ha^a.däla-  und  West SBE.  J/.  4  (lu  mp.  hätakmänsrlk),    Gdn.  GIrPh.
```


## [2026-09-14T00:56:42.378Z] TOOL CALL #53: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py",
 "description": "Check fetch_source usage"
}
```


### [2026-09-14T00:56:42.426Z] TOOL RESULT

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


## [2026-09-14T00:56:49.290Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%B3%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D8%A7%D9%87\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CF%8C%CF%81%CE%BD%CE%B7\" \\\n ; do echo \"--- $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 398, roots Per 4 / Perk 1\" 2>&1 | tail -2; done",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-14T00:56:53.795Z] TOOL RESULT

```
--- https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/bc34a3374f105034.txt
--- https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%B3%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/98a75438c8d3c8f2.txt
--- https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D8%A7%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/bc8db5d3b84bea53.txt
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-
/home/sfmqrb/git/rishe/data/verification/sources/web/69aee26efd6f2318.txt
--- https://en.wiktionary.org/wiki/%CF%80%CF%8C%CF%81%CE%BD%CE%B7
/home/sfmqrb/git/rishe/data/verification/sources/web/b92c4a78c3dc5cfc.txt
```


## [2026-09-14T00:56:56.436Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== پاره ===\"; grep -n -A20 \"^Persian\" bc34a3374f105034.txt | head -60",
 "description": "Read Wiktionary pareh"
}
```


### [2026-09-14T00:56:56.498Z] TOOL RESULT

```
=== پاره ===
```


## [2026-09-14T00:56:59.757Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c bc34a3374f105034.txt 98a75438c8d3c8f2.txt bc8db5d3b84bea53.txt b92c4a78c3dc5cfc.txt; echo \"=== pare etym ===\"; grep -n -i \"Etymology\" -A12 bc34a3374f105034.txt | head -60",
 "description": "Inspect archived pages"
}
```


### [2026-09-14T00:56:59.818Z] TOOL RESULT

```
10012 bc34a3374f105034.txt
12471 98a75438c8d3c8f2.txt
  174 bc8db5d3b84bea53.txt
11555 b92c4a78c3dc5cfc.txt
34212 total
=== pare etym ===
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Adjective 
92-
93- 2.3.1 
94- Derived terms 
95-
96- 2.4 
97- Noun 
--
179: Etymology
180- [ edit ] 
181-
182- From Persian پاره ( pâre ) , from Middle Persian .
183-
184- Noun
185- [ edit ] 
186-
187- پاره • ( pare ) 
188-
189- piece , part , morsel 
190- Synonyms: پارچه ( parça ) , لوقمه ( lokma ) , دیلیم ( dilim ) , قسم ( kısm, kısım ) 
191-
--
262: Etymology
263- [ edit ] 
264-
265- From Middle Persian [script needed] ( pʾlk' /⁠pārag⁠/ , “ piece, part, portion ” ) , also meaning "gift, offering, bribe".
266-
267- In the sense of "gift": from Proto-Iranian *pāraka ( “ gift, offering ” ) , from *pāra- ( “ giving ” ) + *-ka ( “ suffix ” ) , from Proto-Indo-European *perh₃- ( “ to give, provide ” ) . Cognate with Sanskrit पॄ ( pṝ , “ to grant, bestow ” ) , Ancient Greek ἔπορον ( époron , “ give, grant ” ) , Old Irish ernaid ( “ to bestow, grant ” ) . [ 1 ] [ 2 ] [ 3 ] 
268-
269- In the sense of "piece": from Proto-Iranian *pāraka ( “ piece, part ” ) , from Proto-Iranian *par- ( “ to separate, divide into parts ” ) , from Proto-Indo-European *per- ( “ to sell, exchange ” ) , and cognate with Latin pars ( “ part, portion ” ) . [ 1 ] 
270-
271- Pronunciation
272- [ edit ] 
273-
274- ( Classical Persian ) IPA ( key ) : /paː.ˈra/
```


## [2026-09-14T00:57:18.911Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Etymology\" -A10 98a75438c8d3c8f2.txt | sed -n '1,60p'; echo \"=== padafrah ===\"; cat bc8db5d3b84bea53.txt",
 "description": "Read Wiktionary porsidan"
}
```


### [2026-09-14T00:57:18.972Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
--
161: Etymology
162- [ edit ] 
163-
164- From Middle Persian 𐭯𐭥𐭥𐭮𐭩𐭲𐭭 ( pʿʿsytn /⁠pursīdan⁠/ ) , from Old Persian 𐎱𐎼𐎿𐎠𐎷𐎹 ( p-r-s-a-mi-y /⁠pạrsāmiy⁠/ , “ to ask, punish ” , 1sg.pres.act. ) , from Proto-Iranian *pr̥sáti , [ 1 ] from Proto-Indo-Iranian *pr̥šćáti , from Proto-Indo-European *pr̥sḱéti .
165-
166- Cognate to Northern Kurdish pirsîn , Sanskrit पृच्छति ( pṛcchati ) , Russian проси́ть ( prosítʹ ) , Old English friġnan .
167-
168- Pronunciation
169- [ edit ] 
170-
171- ( Classical Persian ) IPA ( key ) : /pur.siː.ˈdan/ 
=== padafrah ===
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D8%A7%D9%87
FETCHED: 2026-09-14T00:56:53Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T00:57:24.320Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D9%87\" \\\n \"https://www.etymonline.com/word/prison\" \\\n \"https://www.etymonline.com/word/pray\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pre%E1%B8%B1-\" \\\n ; do echo \"--- $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 398, roots Per 4 / Perk 1\" 2>&1 | tail -2; done",
 "description": "Archive more sources"
}
```


### [2026-09-14T00:57:27.095Z] TOOL RESULT

```
--- https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/194d15d58a3e26e4.txt
--- https://www.etymonline.com/word/prison
/home/sfmqrb/git/rishe/data/verification/sources/web/00f735f18fe6e65f.txt
--- https://www.etymonline.com/word/pray
/home/sfmqrb/git/rishe/data/verification/sources/web/d2540f53fd805b39.txt
--- https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pre%E1%B8%B1-
/home/sfmqrb/git/rishe/data/verification/sources/web/805a4353ab195c09.txt
```


## [2026-09-14T00:57:30.479Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== padafreh ===\"; sed -n '150,200p' 194d15d58a3e26e4.txt; echo \"=== prison ===\"; grep -n -i \"prison\" 00f735f18fe6e65f.txt | head -8; echo \"=== pray ===\"; grep -n -i \"precari\\|prex\" d2540f53fd805b39.txt | head -5; echo \"=== prek ===\"; grep -n -i \"to ask\\|Descendants\\|Avestan\\|Old Persian\" 805a4353ab195c09.txt | head -20",
 "description": "Read archived pages"
}
```


### [2026-09-14T00:57:30.569Z] TOOL RESULT

```
=== padafreh ===
=== prison ===
1:URL: https://www.etymonline.com/word/prison
4:TITLE: Prison - Etymology, Origin & Meaning
6:Prison - Etymology, Origin & Meaning 
21: Origin and history of prison 
23: prison (n.) 
25: late Old English, prisoun , "place of confinement or involuntary restraint, dungeon, jail," from Old French prisoun "captivity, imprisonment; prison; prisoner, captive" (11c., Modern French prison ), altered (by influence of pris "taken;" see prize (n.2)) from earlier preson , from Vulgar Latin *presionem , from Latin prensionem (nominative prensio ), shortening of prehensionem (nominative *prehensio ) "a taking," noun of action from past-participle stem of prehendere "to take" (from prae- "before," see pre- , + -hender e, from PIE root *ghend- "to seize, take").
30: prison (v.) 
32: "to imprison, shut up in a prison, restrain from liberty," literally or figuratively, early 14c., from prison (n.) or Old French prisoner (v.). Related: Prisoned ; prisoning .
=== pray ===
25: early 13c., preien , "ask earnestly, beg (someone)," also (c. 1300) in a religious sense, "pray to a god or saint," from Old French preier "to pray" (c. 900, Modern French prier ), from Vulgar Latin *precare (also source of Italian pregare ), from Latin precari "ask earnestly, beg, entreat," from *prex (plural preces , genitive precis ) "prayer, request, entreaty," from PIE root *prek- "to ask, request, entreat."
61: c. 1300, preiere, "earnest request, entreaty, petition," also "the practice of praying or of communing with God," from Old French prier "prayer, petition, request" (12c., Modern French prière), from Medieval Latin precaria "petition, prayer," noun use of Latin adjective precaria,
73: imprecationem (nominative imprecatio) "an invoking of evil," noun of action from past participle stem of imprecari "invoke, pray..., call down upon," from assimilated form of in- "into, in, within" (from PIE root *en "in") + precari "to pray, ask, beg,...
77: averting by prayer," noun of action from past-participle stem of deprecari "plead in excuse; avert by prayer," literally "to pray...(something) away," from de "away" (see de-) + precari "to pray" (from PIE root *prek- "to ask, entreat")....
=== prek ===
139: to ask 
156: Proto-Balto-Slavic: *práśīˀtei ( “ to ask ” ) ( see there for further descendants )
168: Avestan: 𐬟𐬭𐬀𐬯𐬁 ( frasā ) , 𐬟𐬆𐬭𐬀𐬯𐬁 ( fərasā ) 
171: Latin: prex ( see there for further descendants )
172: ⇒ Latin: precor ( see there for further descendants )
176: Latin: procus ( see there for further descendants )
185: Proto-Germanic: *frehnaną ( see there for further descendants )
189: Northern Kurdish: pirs ( “ question ” ) , pirsîn ( “ to ask ” ) 
191: Old Persian: √fraθ/pars > parsa-
196: > ? Latin: percontor ( see there for further descendants )
```


## [2026-09-14T00:57:37.397Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"etymology\" -A8 b92c4a78c3dc5cfc.txt | sed -n '1,40p'",
 "description": "Read Wiktionary porne"
}
```


### [2026-09-14T00:57:37.451Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
101-
102- 2.3.1 
--
196: Etymology
197- [ edit ] 
198-
199- From Proto-Hellenic *pórnē , from the Proto-Indo-European root *perh₂- ( “ to sell ” ) , which also gave the verb πέρνημῐ ( pérnēmĭ , “ to sell ” ) .
200-
201- Pronunciation
202- [ edit ] 
203-
204- IPA ( key ) : /pór.nɛː/ → /ˈpor.ni/ → /ˈpor.ni/ 
--
376: Etymology
377- [ edit ] 
378-
379- From Ancient Greek πόρνη ( pórnē ) .
380-
381- Pronunciation
382- [ edit ] 
383-
384- IPA ( key ) : /ˈpoɾ.ni/
```


## [2026-09-14T00:57:38.994Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON pareh\"; grep -n \"پاره\" MON_part1.txt MON_part2.txt | head -10; echo \"### ARY\"; grep -n \"پاره\\|پرسیدن\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Mo'in and Aryanpur"
}
```


### [2026-09-14T00:57:39.082Z] TOOL RESULT

```
### MON pareh
MON_part1.txt:2016:آتشپاره: 9 ۳ پارة ! آتش 
MON_part1.txt:6691:خراج» مال دیوان» پاره» باج. بول آب؛ 
MON_part1.txt:11805:(مص‌م.) رشوه طلبیدن» پاره خواستن. 
MON_part1.txt:19883:باشند. خرقه درویشان که از پاره‌های 
MON_part1.txt:22214:برخ: ۰۵۷ [بخش کردن» بخشیدن] (ا.) پاره؛ 
MON_part1.txt:22239:برحه. (6-)۳2۳۵ [- برخ) (.) پاره‌ای از 
MON_part1.txt:23611:گسلانیدن] (مص‌م.) پاره کردن. شکستن. 
MON_part1.txt:24024:بضعه. ,62 ۶۵ (ع.] () گوشت شت پاره؛ 
MON_part1.txt:24403:بقعه: (007۸)۵ [ع. بقع ] (ا.) پاره‌ای زمین 
MON_part1.txt:25436:دارالحرب گيرند. پاره‌ای از آهن با روی که 
### ARY
377:شاید در آینده گواهان قطعی در پاره‌ی خاستگاه هند و اروپائیان پیدا شود. تا آنزمان» همه‌ی
3910:مس بوس» بوسه» پرسیدن / ۱۳۵
9244:چم این واژه در زبان یونانی؛ ریز ریز با پاره پاره کردن,
11280:چم این زاژه در ایسلندی کهن: نیمکت» پاره‌سنگه:
```


## [2026-09-14T00:57:47.959Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON headword pareh\"; grep -n \"^پاره\\|پاره\\. \\|پاره؛ (\" MON_part1.txt MON_part2.txt | head -10; echo \"### MON porsidan\"; grep -n \"پرسیدن\" MON_part1.txt MON_part2.txt | head -10; echo \"### ARY latin index PERK\"; grep -n -i \"PERK\\|PREK\\|PER-\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Mo'in and Aryanpur index"
}
```


### [2026-09-14T00:57:48.056Z] TOOL RESULT

```
### MON headword pareh
MON_part1.txt:27815:پار: :۲2 [- پاره] (ص.) پاره. قطعه: ماهپار. 
MON_part1.txt:28056:پاره: 0۵ (قطعه» یول] (.) قطعه» تکه 
MON_part1.txt:28058:ماه‌باره» کاه‌باره» آتشپاره. پنبه» و صله» رقعه 
MON_part1.txt:28087:پاره: «۲27 [- پر(پریدن)] (ا.) پرواز» پرش» 
MON_part1.txt:32359:پاره شدن] (مصل.) پاره شدن» گسستن. 
MON_part1.txt:38898:پاره‌اش کنند. (ص‌مر.) چیزی که با تخته و 
MON_part1.txt:42629:پاره پاره ساختن. بریدن پارچه. کوتاه گفتن. 
MON_part1.txt:47353:پاره و ریزه از هر چیز. 
MON_part1.txt:49568:شکاف سیاره 3 پاره پاره. 
MON_part1.txt:53848:پاره‌ای از امور را از شخص دیگر بخواهند و 
### MON porsidan
MON_part1.txt:8527:گرفتن» پرسیدن و جمع آوری رأی‌های 
MON_part1.txt:8541:گرفتن برای کاری. پرسیدن رأی برای 
MON_part1.txt:11565:جستن» آگهی خواستن» خبر پرسیدن) ج. 
MON_part1.txt:12083:پرسیدن» خبر گرفتن. آموزش خواستن؛ ج. 
MON_part1.txt:12164:پرسیدن» در باب مسائل فقهی و شرعی از 
MON_part1.txt:12196:کردن خواستن» طلب تفسیر کردن. پرسیدن. 
MON_part1.txt:12215:جستن» فهمیدن خواستن. پرسیدن؛ سوال 
MON_part1.txt:15326:پرسیدن. بی‌انديشه سخن گفتن. به قريحة 
MON_part1.txt:30602:پرسش: 07-۵8 (امص. پر سیدن) پرسیدن» 
MON_part1.txt:30711:کردن؛ احوال پرسیدن» جویای حال شدن» 
### ARY latin index PERK
4274:PERK, PIRKTI :(LITHUANIAN) gi} PURTI-, PURTIS
4620:65, (SWALLOW) 135 SPARO, SPERK
4636:VRAGEN (DUTCH) sacks PREK (TOKHARIAN B) Bs ja
4653:SKEAT: © (PREK) 757 FRAGEN, FRAGE (GERMAN) gulT
4655:MALLORY & ADAMS: PERK SPORGE (DANISH) jails
5257:PER- HOLD PRUSSIAN) 25.3.4 PAIRI- AVESTAN) oes}
5260:ER. s(WELSH) (53) PERI-, PER- i(GREEK) gly
5269:PER., PER- A(LITHUANIAN) ip
11283:PER, PRE- PARIY, PARI, PER-
11287:PER- (BOHEMIAN) goa PERI (GREEK) gli
11288:PER., PRA+:(OLD PRUSSIAN) oS 3.4 PER-, PERI-, PRO- (LATIN) 3
15893:PERKS, ROBERT S. P. COMPARATIVE INDO-EUROPEAN LINGUISTICS. AMSTERDAM: .
```


## [2026-09-14T00:57:53.977Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4615,4660p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== 4270 ===\"; sed -n '4265,4285p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Read Aryanpur index region"
}
```


### [2026-09-14T00:57:54.036Z] TOOL RESULT

```
‘REFERENCES beth PARRA (LATIN) ogi
POKORNY SOS™~*~*~*~«éOS SPARWA GOTHIC) Ss,
BARNHART: (SPARROW) 1040 {OLD SCANDINAVIAN) pS 2b j
DELAMARRE: (MOINEAU) 140 SPORR |
MACKENZIE: (OLD HIGH GERMAN) cn gST
65, (SWALLOW) 135 SPARO, SPERK
ONIONS: (SPARROW) 850 SPERLING (GERMAN) gst !
SKEAT: (SPARROW) 585 SPEARWA :(OLD ENGLISH) oS g-&i\ '
TAF sgbi obey SPARROW ENGLISH) gulSit |
SPARWE, SPURV (DANISH) (lilo
feetlool
seg 83s ge! GIES 9 BY gw
FARSUN, FARSIN — -(OSSETIC) gu) HAVESTAN) leah
PIRSIN ABURDISH) 52,8 PERESA, FRASA, PERESAITI
PURSAGH ABALUCHD) gy gs (OLD PERSIAN) jt, ges)
PUSHT AAFGHAND (4) gli APARSAM
PRAK -(TOKHARIAN A) A <5 53 PURSITAN PAHLAVI) «5 shy
bh 7
[pdf page 162]
i,t
irl je
VRAGEN (DUTCH) sacks PREK (TOKHARIAN B) Bs ja
(OLD CHURCH SLAVIC) op 531 PRACCHATI, (SANSKRIT) cy Site
PROSITI PRACHH, PRAS-, PRCCHATI
PROSIC POLISH) gling) ARMENIAN) «\
PROSIT, POZVAT —(CZECH) Sx HARSN, E-HARCH, HARCHANEM
PROSIT (SLOVAK) gal POSCO, POSCERE. A(LATIN) 3
(LITHUANIAN) gi 3 PREGUNTAR, (SPANISH) lily!
PERSHU, PIRSHTI PREGUNTA
ARCO (OLD PERSIAN) la 543 p! PERGUNTAR (PORTUGUESE) Ji 4
ARCHAF (GAULISH) J FRAIHNAN (GOTHIC) Saf
OLD SCANDINAVIAN) 45 cles!
‘REFERENCES both, FRETT, FREGNA
POKORNY, = SS*~*«RRD PROSITI {OLD NORSE) oS yes,
BARNHART: (PRAY) 827 FRAGON — (OLD SAXON) 5 Ste
DELAMARRE: (DEMANDER) 275 FREGIA (OLD FRISIAN) S523
MACKENZIE: (ASK) 103 OLD HIGH GERMAN) pS glT
BUCK!” 1264-1266 FORSCON, FRAHEN, FRAGA
SKEAT: © (PREK) 757 FRAGEN, FRAGE (GERMAN) gulT
AMINDAROV: (ASK) 187 FRIGNAN (OLD ENGLISH) oS iS!
MALLORY & ADAMS: PERK SPORGE (DANISH) jails
rAd seb oly FRAGA SWEDISH) 528 y-
SPORRE NORWEGIAN) 533
“
PARWAZ HAFGHAND (54) lil AVESTAN) gly)
SANSKRIT) = Sle PAIRI-VAZAITI, PARA-VAZ
=== 4270 ===
PWRONK (SOGADIAN)
reetloal
eel yb IVY ree Hin 4 lal a Ha clad STs gol Side Obed ply hE
scl 031 (LION + PARD) LEOPARD) 4 |, 25 slr PARD slots ols)! Glas Sh 2-1
PARTE, PARTIR — (SPANISH) gli! PARA, PAR- (AVESTAN) gm 3!
PARTE, PARTIRE — :((TALIAN) ol! PARAK, PARAG PAHLAVI) 5 3h,
PARTE (RUMANIAN) ley) PART 4BALUCHI) gh
PARTE, PARTIR:(PORTUGUESE) Jl PARAY AFGHAN) (2-4) lai)
PART (1 D(ENGLISH) Si} PORTA, SANSKRIT) ty Sue
PERK, PIRKTI :(LITHUANIAN) gi} PURTI-, PURTIS
RANN HOLD IRISH) aS 5414! s(GREEK) gy
PHAN WELSH) «5 5 PERASO, EPERASA
RANNOU H(BRETON) 5.2 PARS, PARTIS, PORTIO <(LATIN) SY
PARSH., PARSIYA — (HITTITE) ca» (FRENCH) «il
PART, PARTIE, PARTIR
[pdf page 150]
—
YOY f_glassty 2 4) nl
BUCK: (PART)933-934 ‘REFERENCES beth
ONIONS: “powory; SSsS~S~S~«SY
(PART) 653-654, (PORTION) 698 BARNHART:
```


## [2026-09-14T00:58:15.032Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28050,28095p' MON_part1.txt; echo \"=== MON پرسش/پرسیدن headword ===\"; sed -n '30598,30612p' MON_part1.txt",
 "description": "Read Mo'in entries"
}
```


### [2026-09-14T00:58:15.101Z] TOOL RESULT

```
سری پهن دارد و خمیر را روی آن به نحو 
مسخصوص پهن مسی‌کنند و در تسنور 
می‌گذارند. استخوان شانه» استخوان کتف» 
استخوان هوبه. پول کسی با پارو بالا رفتن: 
(تد.) بسیار ثرو تمند بودن‌وی. 

پاره: 0۵ (قطعه» یول] (.) قطعه» تکه 
پارچه» جزو» بخش» برخ» لخت» ترکیبات: 
ماه‌باره» کاه‌باره» آتشپاره. پنبه» و صله» رقعه 
در بی. دربده» شکافته» چاکك. گسیخته. 
نادوشیزه» بکارت شده. جزو؛ مق. کل» 
یک جزو از سی جزو قرآن. سهم؛ بهر 
بخش. بول» مسک وکد. زری که در ولایت 
روم رایح است» خردترین پول مسین یا 
نیکلی یا سیمین عثمانیان» چهل یک قروش 
(در ترکیه پاره چهل یک پیاستر و هر صد 
پیاستر معادل یک لیر ترک است.) رشوه؛ 
رشوت که قاضی را دهند. مدفوع انسان و 


حیوان که برای حاصلخیزی زمین بکار برند؛ 
کود. نوعی از حلوا که آن را شکر پاره نیز 
وت زاده: محدوم باره. مزد» جعل. باج» 
خراج. هدبه» تحفه» تبرک. گرز آهنین. 
یکت باره: اند کی» کمی» باره‌ای. پارح آجر: 
شکنته آجر آجر باره. باره آرد: اوماج» 
آش اوماج. پارة اسب: (اخ.) صورتی از 
صور فلکی. قطءهً الفرس. باره تن 
عزیزترین کس نزد آدمی» خویش؛ وصلة 
سن» باره دل» جگکر گوشه. بارة دل: 
عزیزترین کس نزد آدمی چون فرزند» پارة 
جگر پارة تن. جگر گوشه. پارةٌ ر: قراضه. 
پار؟ زرد: پارچة زردی که یهودان برای 
استباز از مسلمانان بر کتف می‌دوختند؛ 
عسلی» غبار» غیاره» زرد باره. بارة سنگ: 
قطعه‌ای از سنکك. پارة کار: کارا گاه؛ عارف 
بر امور. 
پاره: «۲27 [- پر(پریدن)] (ا.) پرواز» پرش» 
پریدن» پرواز کردن. 
باره‌دوز: -2-.۳ [- پاره‌دوزنده] (افاء) 
آنکه ک‌فش‌ها را وصله کند: بینه‌دوز» 
لخت‌دوزء لاحخه‌دوز» وصله گر. تن پرست. 
پاریاب: 2575 [- پاراب - فاراب] (امر.) 
زراعتی را گویند که به آب رودخانه و امثال 
آن مزروع شود؛ فاریاب» فاریاو» آبی. (اخ.) 
نام شهر ی است. 
=== MON پرسش/پرسیدن headword ===
فرمان. خدمت کردن» خدمت. خم شدن به 
رسم تعظیم» نماز بردن. دوست گرفتن» 
دوست داشتن. ورزیدن. 

پرسش: 07-۵8 (امص. پر سیدن) پرسیدن» 
سوّال» استفسار» تِِ استخار» اقتراح» 
استطلاع. ۰ پژوهش» تحقیق. احوال‌برسی» 
پبرسش از سلامت شار پژوهش حال. 
دلجویی» تفقد. بازخواست» مژاخذه. به 
پرسش آمدن: به عیادت آمدن» عیادت 
کردن. به پرسش رفتن: به عیادت رفتن» به 
احوالپرسی مریض رفتن. پرسان پرسان رفتن. 
ه پرسش گرفتن: پژوهش کردن» تحقیق 
کردن» استفسار کردن» پرسش اندر گرفتن» 
پرسش گرفتن.
```


## [2026-09-14T00:58:16.351Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN ask\"; grep -n \"ASK\\b\" SYN.txt | head -5; echo \"### SYN part\"; grep -n \"^18.12 PART\\|PART$\" SYN.txt | head -5",
 "description": "Grep Buck"
}
```


### [2026-09-14T00:58:17.506Z] TOOL RESULT

```
### SYN ask
31824:18.31 ASK! (Question, Inquire)
31964:18.35 ASK?, REQUEST Grk. — alréw (Epwréw) Goth. bidjan Lith.  pragyti, reikalauti NG §q7G, wapaxadd ON bidja Lett. prasit Lat.  poscere, pelere, rogare Dan. _bede, forlange, fordre ChSl.  prositi, moliti It. domandare, (ri)chie- Sw. bedja, begdra, fordra SCr.  -moliti, iskati, traziti dere OE biddan, dscian, giwian Boh. _ prositt, Zddali Fr. demander ME bidde, aske, demaund Pol. prosic, zadaé Sp. pedir, rogar NE ask, request Russ. prosit’, trebovat' Rum. cere Du. verzoeken, verlangen Skt. yac-, (pra-)arthaya- Tr. condaigim, cuingim OHG _ bitten, eiscon Av., OPers. jad- Nir. tarraim MHG bitten, eischen, vor- W. gofyn Br. goulenn NHG bitten, verlangen, for-
### SYN part
17567:10.49 GO AWAY, DEPART
```


## [2026-09-14T00:58:26.777Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31824,31850p' SYN.txt | cut -c1-1200; echo \"=== SYN PART ===\"; grep -n \"13.23 PART\\|PART (sb\" SYN.txt | head",
 "description": "Read Buck ASK"
}
```


### [2026-09-14T00:58:26.846Z] TOOL RESULT

```
18.31 ASK! (Question, Inquire)
Grk. épwrdw Goth. fraihnan Lith. klausti NG pure ON spyrja, fregna, frétta Lett.  jautat, vaicat, klaust Lat. rogare, quaerere Dan.  spé¢rge ChSl.  vitprositi It. domandare Sw. frdga SCr. _ pitati Fr. demander OE Sregnan, dscian, Boh. pti se Sp. preguntar spyrian Pol. pytaé Rum. inireba ME aske, frayne Russ. — sprosit’ Tr. tarmi-foig, imm- NE ask Skt.  pracch- comairc Du. vragen Av. Sras- Nir. fiafruighim OHG  fragén, eiscon W. gofyn MHG vragen, eischen Br. goulenn NHG fragen
There is considerable interchange, in the same word or among cognates, be- tween the two notions covered by NE ask, namely 1) ask ‘question, inquire’ and 2) ask ‘request’ (ask a person to do something, and with the thing requested as object, ask aid, but for the latter now most commonly ask for, like NHG bitte wm). In such groups the develop- ment may be in either direction or from & common ‘seek’ (an answer or a thing). In the following, for the sake of brevity, the two senses are distinguished as ‘ask’! and ‘ask’. But except in words or groups in which both senses are involved ‘ask’! is understood here, and expressions for ‘ask’ are combined in 18.35.
1. IE *prek- and *pr(k)-sk-, etc. in words for ‘ask’ in one or both senses. Walde-P. 2.44. Ernout-M. 794. f.
Lat. poscere ‘ask’?; Ir. arcu ‘beg, be- seech’, cpds. com-aircim ‘inquire’, imm- comaire (3sg.) ‘ask’!, W. arch ‘request’, MBr. archas ‘il commanda’; Goth. fraih- nan, ON fregna (sb. frétt ‘question, in-
vestigation’, whence vb. fréta), OE fregnan, frignan, ME frayne, MLG ovra- gen (> Sw. frdga), Du. vragen, OHG fragén, MHG vragen, NHG fragen all ‘ask’!; Lith. pragyti ‘ask’?, Lett. prasit id. and rarely also ‘ask’! (ef. Miihl.-Endz. s.v.); ChSl. prositi, ete. ‘ask’, for ‘ask’! ChSl. vt-prositt, Russ. sprosit’; Skt. pracch-, prac-, Av. fras- ‘ask’, Arm. harcanem id., Toch. A pdrk-, prak-, B prek- act. ‘ask’?, mid. ‘ask’! (SSS 449).
2. Grk. Hom. elpwraw, Att. gpwraw, NG pw7@, orig. deriv. of an *épfws : Grk. (epic) épéw, épéouar ‘ask, inquire about, search, explore’, ON reyna ‘try’, rawn ‘trial, attempt’. Walde-P. 2.356. Boi- sacq 278.
3. Lat. rogadre (‘ask’ in both senses); prob. orig. ‘direct (oneself) to, address : regere ‘direct, guide, rule’, Ir. gum ‘stretch out (the hand)’, etc. Walde-P. 2.363. Ernout-M. 868 f.
Lat. quaerere ‘seek’ (11.31) also com- mon for ‘ask’, Hence sb. quaestt ‘questioning, investigation’ (rarely for
Wo aN Oe ee
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar —
|
vOCAL UTTERANCE, SPEECH; READING AND WRITING
ne concrete ‘question’), whence Fr., i ip, NE question, etc. Cf. also epd. M arere “nquire into’, NE inquire, ete. a domandare, Fr. demander (‘ask’ in oth senses “Sp: demandar mostly ‘ask”?), fr. Lat. demandare ‘give in charge, in- trust, commit’, cpd. of mandare ‘intrust, command, charge with’, orig. ‘put in the hand’ : manus ‘hand’, etc. Ernout-M. 586. Walde-H. 2.25. REW 2547.
Sp. preguntar, Port. perguntar, fr. Lat. percontart ‘investigate, inquire’, fig. use of ‘sound’ (the depth), deriv. of contus ‘pole, pike’ (fr. Grk. xovrés id.). Ermout-M. 217. REW 6400.
Rum. tntreba, fr. Lat. interrogare, cpd. of rogare (above). REW 4496.
4, Olr. tarmi-foig (8sg.), MIr. zar- mafaigim, iarfaigim, hence NI. fia- fruighim, cpd. (*iarm-fo-saig-) of saigim ‘go after, seek’ : Goth. sdkian ‘seek’, etc. (11.31). Pedersen 2.608, 610.
W. gofyn ‘ask’ in both senses, perh. fr. *upo-men- : mynnu ‘wish’, fr. the root *men- in Skt. man- ‘think’, etc. Peder- sen 2.451. Walde-P. 2.265.
Br. goulenn ‘ask’ in both senses, etym. dub., perh. as orig. ‘seek, search’ = Ir. fo-ghiunn ‘learn’, fr. the root of ChSl. gledati ‘see’, etc. (Walde-P. 1.625). Loth, RC 45.185. Otherwise Henry 138.
5. Goth. fraihnan, OE fregnan, etc., above, 1. I ON spyrja, Dan. spérge (Sw. spéorja 8 common), OE spyrian, ME spyre
Digitized by Arya Samaj Foundation Chennai and eGangotri
1265
(NE dial. speer), lit. (and so often in ON and OE) ‘track, trace’ = OHG spurian ‘trace, search, notice’ (NHG spiren ‘trace, feel’), fr. ON, OE, OHG spor ‘track’. Falk-Torp 1141. NED s.v. Walde-P. 2.669.
OE dscian, dcsian, ME aske, axe, NE ask, OHG eiscén, MHG eischen ‘ask’ in both senses (NHG heischen ‘request, demand’, with A- fr. heissen) : Lith. ieskott, ChSl. iskati ‘seek’, Skt. z3- ‘seek, wish’, etc. Walde-P. 1.12. Weigand-H. 1.840. NED s.v. ask, vb.
6. Lith. klausti, Lett. klaust, prob. as ‘will hear’ (orig. fut. formation) : klau- sytt, Lett. klaustt ‘listen’, etc. (15.41). Walde-P. 1.495. Miihl.-Endz. 2.216 f.
Lett. jautat, cf. Lith. jautotis (refl.) ‘Inquire, inform oneself’ : Lett. jaust ‘perceive, notice, feel’, Lith. jausti ‘feel, notice’, etc. (15.11). Cf. for semantic development Grk. zuv@dvopac ‘find out, inquire’ : Skt. budh- ‘be awake, notice’, and NE feel someone out. Mihl- Endz. 2.104.
Lett. vaicat, fr. the interrog. particle vat, fr. Liv. vot. Miihl.-Endz. 4.433 f.
=== SYN PART ===
23766:13.28 PART (sb.)
```


## [2026-09-14T00:58:32.808Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23766,23790p' SYN.txt | grep -o \"Lat. pars[^.]*\\.\\|pars, partis[^.]*\\.\\|Walde-P. 2.4[0-9]\" | head; echo \"---\"; sed -n '23770,23785p' SYN.txt | cut -c1-900",
 "description": "Read Buck PART"
}
```


### [2026-09-14T00:58:32.889Z] TOOL RESULT

```
Lat. pars, -tis (> It.
Walde-P. 2.41
Lat. pars (above, 2).
Lat. pars.
---
934
Words for ‘a part’ as opposite of ‘the whole’ are such as are also used in gen- eral for ‘portion, share’, often also ‘lo- cality, region’, and are derived from various roots for ‘share, divide’, etc.
1. Grk. pépos (also ‘share, portion’ be- side yepis ‘portion’): Hom. pelpopar ‘receive as one’s portion’, pepitw ‘di- vide’, yépos ‘lot, fate’, etc., Lat. merére ‘receive as portion or price’, ‘earn, merit’, fr. a root *(s)mer-, perh. the same as *(s)mer-in Lat. memor ‘mindful
of’, Skt. smr- ‘remember’. Walde-P. 2.690. Ernout-M. 609f. Walde-H. 1.75 f.
NG yépos in pop. speech mostly ‘lo- cality, region’ and in sense of ‘part’ often replaced by xoupare ‘piece’, fr. a dim. form of class. Grk. xoupa ‘piece cut off’ (also ‘stamp’, etc.), fr. xérrw ‘strike, cut’.
2. Lat. pars, -tis (> It., Sp., Rum. parte; Fr. part now mostly ‘portion, share’), prob. fr. the root of Ir. ro-ir ‘(he) granted’, Grk. éropov ‘gave, brought’, merpwrat ‘it is fated’, and also Lat. parere ‘bear, give birth to’ (fr. ‘obtain, get’). Walde-P. 2.41. Ernout-M. 735.
Fr. partie (now usual for ‘part’ of a whole, for older part), fr. partir in arch. sense ‘divide’ (now ‘part, leave’), fr. VLat. partire (for Lat. partiri) ‘divide’, fr. pars (above). REW 6259.
3. Ir., Br. rann, W. rhan, generally taken as (*pfsnd-?) : Lat. pars (above, 2). Pedersen 1.52. Stokes 227. Oras orig. ‘border’ : OE rand ‘border’, etc.? Loth, RC 41.400f. (but see also 43.411 f.).
Ir. cuit, NIv. cwid (in the older Jan- guage chiefly ‘portion, share’) : W. peth ‘thing’, Br. pez ‘piece’, further connec- tion doubtful. Pedersen 1.160 (: ChSI. cestt ‘part’, etc.; rejected by Walde-P. 1.393). Henry 222.
Ir. pairt (NIr. pairt now ‘regard, sympathy’, etc.), fr. Lat. pars. Ven- dryes, De hib. voc. 164.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
SELECTED INDO-EUROPEAN SYNONYMS
4. Goth. dails, OF dzl, OS dal (MLG > Sw. del, and Dan. del as old masc,) ME deel (NE deal), etc., general WGme,, ON deild (> Dan. del as old fem,), be. side vb. forms, Goth. dailjan, ON deila OE delan, etc. ‘divide’, etym. dub. (cf. ChSl. déhi, etc., below, 6). Falk-Torp 139. Feist 114.
ON Alutr, hluti, ‘share, lot? and also ‘part’ : OF hlot, Goth. hAlauts ‘lot’, ete., root connection dub. Walde-P. 1.493. Falk-Torp 651. Feist 262.
ME, NE part, fr. Fr. part (above, 2),
5. Lith. dalis, Lett. dal’a, OPruss. del- liks, with vbs. Lith. dalyti, Lett. dalit ‘divide’ : Russ. dolja ‘lot, share’, Skt. dala- ‘fragment, piece’, fr. the root in Skt. dal- ‘burst’, Lat. doldre ‘hew’, etc. Walde-P. 1.811. Miuihl.-Endz. 1.435. Berneker 209.
```


## [2026-09-14T00:58:40.056Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پرسیدن\\|پرس\" incoming/FFD/FFD_pages.txt | head -10",
 "description": "Grep FFD for porsidan"
}
```


### [2026-09-14T00:58:40.127Z] TOOL RESULT

```
1174:پرستیدن
1175:پرست + فارسی میانه 027181 < ایرانی باستان 7-512هم*.
1182:باستان. برای 1۸ > آراست. «پرستید» در فارسی جعلی است و از مادهٌ مضارع و «ید»
1184:پرسیدن
1185:پرسید < فارسی میانه 00781#. 005810 مادهٌ ماضی جعلی است. از مادهٌ مضارع
1187:پرس < فارسی میانه 0078 < ایرانی: باستان 0788* ج ۴۹7-2 برای 2 -> آرای. 5
1188:برای ساختن مادهٌ آغازی از ريشه به کار می‌رفته است.078 ريشه است, به معنی «پرسیدن».
2510:8 ؛ (ريشه < پرسیدن) ۴۲ َ 8
```


## [2026-09-14T00:58:45.971Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<1190 && /\\[pdf page/ {p=$0; n=NR} END{print n\": \"p}' incoming/FFD/FFD_pages.txt; sed -n '1180,1192p' incoming/FFD/FFD_pages.txt",
 "description": "Find FFD page"
}
```


### [2026-09-14T00:58:46.932Z] TOOL RESULT

```
1178: [pdf page 47]
ایستادن.
مادة ماضی 027191 در فارسی میانه 02719136 آمده است» از ۳27-513-1* ایرانی
باستان. برای 1۸ > آراست. «پرستید» در فارسی جعلی است و از مادهٌ مضارع و «ید»
: ساخته شده است.
پرسیدن
پرسید < فارسی میانه 00781#. 005810 مادهٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
پرس < فارسی میانه 0078 < ایرانی: باستان 0788* ج ۴۹7-2 برای 2 -> آرای. 5
برای ساختن مادهٌ آغازی از ريشه به کار می‌رفته است.078 ريشه است, به معنی «پرسیدن».
پروردن
پرورد ج فارسی میانه 40 << ایرانی باستان 02۳-۵-[۳۵7*. برای 13 -> آراست.
1 پیشوند فعلی است. ريشهٌ 7 به معنی «حمل کردن» است. «آوردن» و «بردن» هم از
ريشهٌ ۳27 آمده‌اند.
```


## [2026-09-14T00:59:23.674Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -20 69aee26efd6f2318.txt; echo \"...\"; grep -n -i \"sell\\|perh₃\\|Etymology\" 69aee26efd6f2318.txt | head -20",
 "description": "Check archived PIE per page"
}
```


### [2026-09-14T00:59:23.734Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-
FETCHED: 2026-09-14T00:56:31Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/per- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/per- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
...
302: See also *perh₃- ( “ to beget ” ) , often confused with this root, and perhaps conflated with or related to it.
```


## [2026-09-14T00:59:33.714Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg398.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/398.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/398.png; head -6 /home/sfmqrb/git/rishe/data/verification/sources/web/194d15d58a3e26e4.txt",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T00:59:33.787Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77067 Sep 13 20:59 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/398.png
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%A7%D9%81%D8%B1%D9%87
FETCHED: 2026-09-14T00:57:26Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T01:06:31.600Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-398.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PARE   = \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B1%D9%87\"\nW_PORS   = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%B3%DB%8C%D8%AF%D9%86\"\nW_PER    = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-\"\nW_PORNE  = \"https://en.wiktionary.org/wiki/%CF%80%CF%8C%CF%81%CE%BD%CE%B7\"\nW_PREK   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pre%E1%B8%B1-\"\nE_PRISON = \"https://www.etymonline.com/word/prison\"\nE_PRAY   = \"https://www.etymonline.com/word/pray\"\n\ndoc = {\n \"pdf_page\": 398,\n \"book_page\": 368,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Per 4, Pera\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *per- / *perə- 'to allot, grant; to hand over, sell' (Pokorny 2. per-, Section C, p. 817)\",\n   \"note\": \"Nourai's box is a faithful rendering of Pokorny's 'Root/lemma: per-2: C. per-, perə-, Meaning: to sell' (IEW 817), whose material contains exactly the three branches drawn here: Avestan pāra- 'Schuld', Greek πέρνημι / πόρνη, and Latin pār/parō/pars/portiō plus Old Indic pūrta-. The gloss 'to assign, to trade' is a fair double translation of Pokorny's 'verkaufen' + 'zuteilen', and the remark 'related to Per 1' is Pokorny's own ('s. dazu auch per- hinüber', WP II 40: 'wohl mit per- hinüber ... ursprünglich eins'). Modern handbooks split Pokorny's single 817 entry in two: Watkins/AHD gives perə-2 'to grant, allot' [Pok. 2. per, Section C 817] for pars/portiō/pār and per-6 'to traffic in, sell' [In Pok. 2. C. per 817] for pretium and πόρνη, and Wiktionary/LIV assign the 'grant' material to *perh3- and the 'sell' material to *per-. That is a refinement of, not a contradiction to, Nourai's chart.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *per-/*perə- «بخش کردن، دادن؛ سپردن، فروختن» است؛ پوکورنی آن را زیر «per-2، بخش C» در صفحهٔ ۸۱۷ آورده و درست همین سه شاخه‌ای را برمی‌شمارد که نورایی در نمودار کشیده است: اوستایی pāra- «بدهی، دَین»، یونانی pórnē، و لاتینی pars/portio. برچسب زبانی («هندواروپایی») و معنای «واگذاشتن، داد و ستد» درست است. ریشه‌شناسی امروزی (واتکینز در پیوست AHD و ویکی‌واژه بر پایهٔ LIV) این مدخل واحدِ پوکورنی را به دو ریشه بخش می‌کند: *perh₃- «بخشیدن، دادن» و *per- «فروختن»؛ این تفکیک تکمیل ادعای نورایی است نه ردّ آن. در مجموع ادعای نورایی درست است.\",\n   \"sources\": [W_PER, W_PARE],\n   \"ref_check\": [\n    {\"ref\": \"POK:817\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (database dump of IEW): 'Root / lemma: per-2: C. per-, pera- | Meaning: to sell ... Page(s):817'. The Material section contains 'Gr. πέρνημι ... πόρνη meretrix', 'Av. pairyante, aipi-par-, parəθa- n., para- m. \\\"blame\\\" (= Schuld)', and 'Old Indic purta-, purti- \\\"earnings\\\" = Latin pars, -tis \\\"part\\\", portio'. Exactly the three branches of Nourai's box.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 40-41 (WLD_Bd2_1927_dli_106624_djvu.txt l.2634ff)\", \"stance\": \"supports\",\n     \"note\": \"'5. per- \\\"verkaufen\\\" (eig. \\\"zum Verkauf hinüberbringen\\\" ... und wohl mit per- \\\"hinüber\\\" ... ursprünglich eins) ... noch näher der ersten Gruppe steht eine mit der Bed. \\\"zuteilen\\\"'; under 2: 'av. para- m. \\\"Schuld\\\" ... nach Bartholomae Vb. 849 zu lat. par, paris'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. perə-2 and per-6\", \"stance\": \"supports\",\n     \"note\": \"'perə-2. To grant, allot ... Latin pars (stem part-) ... Latin portio ... Latin par, equal ... [Pok. 2. per, Section C. 817.]' and 'per-6. To traffic in, sell (< \\\"to hand over\\\", \\\"distribute\\\") ... Greek pernanai, to sell, whence o-grade ... porne, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.]'\"},\n    {\"src\": \"KLN\", \"where\": \"p. 1149 s.v. 'pair'\", \"stance\": \"supports\",\n     \"note\": \"'All these words prob. derive fr. I.-E. base *per-, \\\"equal; to sell, to buy ... for equal value\\\" ... Base *per-, \\\"to sell\\\", is prob. ult. identical with base *per-, \\\"to assign, allot\\\", whence L. pars, gen. partis, \\\"part\\\"' — Klein states Nourai's very equation.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 13.28 PART (sb.), pp. 933-934\", \"stance\": \"supports\",\n     \"note\": \"'Lat. pars, -tis ... prob. fr. the root of Ir. ro-ir \\\"(he) granted\\\", Grk. eporon \\\"gave, brought\\\", peprotai \\\"it is fated\\\" ... Walde-P. 2.41.'\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt, entry before [pdf page 150]\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's entry for پاره lists under one root: 'PARA, PAR- (AVESTAN); PARAK, PARAG (PAHLAVI); PARS, PARTIS, PORTIO (LATIN); PERASO, EPERASA (GREEK); PURTI-, PURTIS (SANSKRIT); PERK, PIRKTI (LITHUANIAN)', with 'REFERENCES: POKORNY 817' and 'BUCK: (PART) 933-934' — an independent modern Persian handbook reproducing Nourai's grouping.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pâra 1\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan pāra- m. 'debt, guilt' (Bartholomae AiW col. 889) is a root noun of the verb par- 'to settle (a debt), atone', beside parəθa- n. 'settlement of a debt, atonement, punishment' and ā-pərəti- 'atonement'. Pokorny puts precisely this word in his per-2 C 'to sell/allot' entry (IEW 817, section β: 'Avestan ... para- m. \\\"Schuld\\\"'), the semantic bridge being 'what is handed over as equal value' > 'what one owes'. The chart's language label and gloss ('Avestan', 'debt') are exactly Bartholomae's; the '1' is Nourai's homonym number, distinguishing it from Av. pāra- 'shore, limit' (from *per- 'to cross').\",\n     \"derivation_fa\": \"اوستایی pāra- (نامِ نرینه) به معنی «بدهی، دَین، گناهِ بازپرداختنی» است؛ بارتولومه در «واژه‌نامهٔ ایرانی باستان» ستون ۸۸۹ آن را با معنی Schuld آورده و آن را با فعل par- «تاوان دادن، جبران کردن» و parəθa- «تاوان، کیفر» هم‌ریشه می‌داند. پوکورنی (ص ۸۱۷) همین واژه را زیر ریشهٔ per- «فروختن/واگذاشتن» جای داده است؛ پل معنایی آن «آنچه در برابرِ ارزشِ برابر سپرده می‌شود» ← «آنچه بر گردن است» است. شمارهٔ «۱» از خودِ نورایی است تا با pāra- دیگر (به معنی «کرانه») اشتباه نشود. ادعای نورایی درست است.\",\n     \"sources\": [W_PER],\n     \"ref_check\": [\n      {\"ref\": \"POK:817\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt p.817 section β: 'Avestan pairyante \\\"are become compared\\\", aipi-par- \\\"(seine Schuld) begleichen\\\", a-pərəti-s \\\"atonement\\\", parəθa- n. \\\"equalization of (blame), atonement, punishment\\\", para- m. \\\"blame\\\" [= Schuld] (in addition probably also par- \\\"verurteilen\\\")'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"BRT.txt l.16017 (AiW col. 889)\", \"stance\": \"supports\",\n       \"note\": \"'• j. pāra- m. \\\"Schuld\\\": aŋha mazdayasnis .. spayeiti anāpərəθəm syaoθnəm .. dəmānō pərəθəm \\\"die m. Religion nimmt auch eine Schuld weg, die schwere Sühne erheischt\\\" V. 3.41'. Col. 889 is the column Nyberg cites for this word.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 41\", \"stance\": \"supports\",\n       \"note\": \"'av. ... para- m. \\\"Schuld\\\" (dazu wohl auch par- \\\"verurteilen\\\"), nach Bartholomae Vb. 849 zu lat. par, paris \\\"gleichkommend, gleich, Paar\\\"'.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt before [pdf page 150]\", \"stance\": \"supports\",\n       \"note\": \"Aryanpur lists 'PARA, PAR- (AVESTAN)' as the Avestan member of the same root-family as Persian پاره.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"pârak\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian pārak, written <p'lk'>, is Old Iranian *pāra-ka-, i.e. Av. pāra- 'debt, what is owed' + the productive MP suffix -ak (< *-aka-); intervocalic OIr. -k- is preserved in the suffix while the sense drifts from 'what is owed' to 'what is handed over' > 'gift, present' > 'bribe'. Nyberg's glossary attests it twice in the Kārnāmag (73.13, 75.15) with the value 'a bribe' and derives it, as Nourai does, from Av. pāra- 'debt'. MacKenzie separates two homophones: 1pārag [p'lk'] 'piece, part, portion' and 2pārag [p'lk' | M p'rg] 'gift, offering, bribe'; it is the second that continues Av. pāra-, and Nourai's gloss chain 'debt, bribe, gift' belongs to it.\",\n     \"derivation_fa\": \"فارسی میانه pārak (با املای پهلویِ p'lk') از ایرانی باستانِ *pāra-ka- است: همان pāra- اوستایی «بدهی» به‌علاوهٔ پسوند اسم‌سازِ -ak (< *-aka-). تحول معنایی روشن است: «آنچه بر گردن است» ← «آنچه سپرده می‌شود» ← «پیشکش، هدیه» ← «رشوه». نیبرگ در واژه‌نامهٔ خود (ص ۱۵۰) همین را می‌نویسد: pārak «رشوه»، از اوستایی pāra- «بدهی». مکنزی دو هم‌آوا را جدا می‌کند: pārag ۱ «تکه، پاره» و pārag ۲ «هدیه، پیشکش، رشوه»؛ آنچه دنبالهٔ pāra-ی اوستایی است دومی است. ادعای نورایی درست است.\",\n     \"sources\": [W_PARE],\n     \"ref_check\": [\n      {\"ref\": \"NYB:150\", \"status\": \"supports\",\n       \"note\": \"Nyberg, Manual of Pahlavi II (Glossary) p. 150 (page marker 150 immediately precedes the entry in NYB_vol2_glossary.txt): 'pārak [p*lk'] a bribe 73^13, 75^15. — Av. (889) para- \\\"debt\\\"; MPrs p'rg \\\"gift\\\"; NP pārah \\\"gift, bribe\\\".' This is Nourai's arrow verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 65 s.v. pārag\", \"stance\": \"partial\",\n       \"note\": \"'1parag [p'lk' | N para] piece, part, portion. 2parag [p'lk' | M p'rg, N para] gift, offering, bribe.' MacKenzie keeps two homonyms; only the second belongs here.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW col. 889 s.v. pāra-\", \"stance\": \"supports\",\n       \"note\": \"Av. pāra- m. 'Schuld' is the base from which Nyberg derives pārak; Bartholomae's column number is the one Nyberg quotes.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt before [pdf page 150]\", \"stance\": \"supports\",\n       \"note\": \"'PARAK, PARAG (PAHLAVI)' listed as the Middle Persian stage of the same family.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"pâreh\", \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian پاره pāra continues MP pārag regularly (final -ag > -a/-e; Classical pāra, modern pāre). Borhān-e Qāte' p. 351 defines it 'معروف است که در مقابل درست باشد و بعربی قطعه خوانند ... و رشوت را نیز گویند و بمعنی تحفه و تبرک هم آمده است ... و جزو را نیز گویند', and Mo'in glosses it 'قطعه، تکه ... پول، مسکوک ... رشوه، رشوت که قاضی را دهند ... هدیه، تحفه، تبرک' — i.e. all three of Nourai's senses ('money, gift, a piece of something'). The reservation is that modern etymology treats this as two merged words: the 'gift/bribe/money' sense goes back to MP 2pārag < Av. pāra- 'debt' (Nourai's chain, correct), while the 'piece, fragment' sense — the one in the compound آتش‌پاره ātaš-pāra 'firebrand, a piece of fire' that the chart prints in the Persian-script field — goes back to MP 1pārag 'piece' from Proto-Iranian *par- 'to cut, divide' (so Wiktionary, following MacKenzie's two entries). Nourai's node therefore hangs a word on the chart that is only half descended from the branch drawn; the Nāser-Khosrow line quoted ('که زی دانا بری بر سم پاره') uses the 'gift/fee' sense, which is the right one.\",\n     \"derivation_fa\": \"«پاره» فارسی نو دنبالهٔ pārag فارسی میانه است؛ -ag پایانی در فارسی نو به -ه بدل شده است. برهان قاطع (ص ۳۵۱) آن را چنین معنی می‌کند: «معروف است که در مقابل درست باشد و بعربی قطعه خوانند ... و رشوت را نیز گویند و بمعنی تحفه و تبرک هم آمده است»، و معین نیز «قطعه، تکه ... پول، مسکوک ... رشوه ... هدیه، تحفه، تبرک» آورده است؛ پس هر سه معنیِ نورایی در فرهنگ‌های فارسی هست. اما با احتیاط پذیرفتنی است: ریشه‌شناسی امروزی دو واژهٔ هم‌آوا را از هم جدا می‌کند؛ معنیِ «پیشکش، رشوه، پول» از pārag ۲ و در نهایت از pāra-ی اوستایی «بدهی» می‌آید (همان زنجیرهٔ نورایی) ولی معنیِ «تکه، قطعه» — که در ترکیبِ «آتش‌پاره» در همین خانه آمده — از pārag ۱ و ستاکِ ایرانیِ *par- «بریدن، جدا کردن» است. بنابراین دو واژهٔ جدا در یک خانه درآمیخته‌اند.\",\n     \"sources\": [W_PARE],\n     \"ref_check\": [\n      {\"ref\": \"BQT:351\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate', printed p. 351 (the page carries the footnote header 'بقیه از صفحهٔ ۳۵۰'): headword 'پاره بر وزن چاره. معروف است که در مقابل درست باشد و بعربی قطعه خوانند ... و رشوت را نیز گویند - و بمعنی تحفه و تبرک هم آمده است ... و جزو را نیز گویند'. Found by grepping 'پاره' in BQT_v1_pages.txt (l.23190).\"},\n      {\"ref\": \"MON\", \"status\": \"supports\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. پاره (MON_part1.txt l.28056): 'پاره: [قطعه، پول] (ا.) قطعه، تکه، پارچه، جزو، بخش، برخ، لخت. ترکیبات: ماه‌پاره، کاه‌پاره، آتش‌پاره ... پول، مسکوک ... رشوه، رشوت که قاضی را دهند ... هدیه، تحفه، تبرک'.\"},\n      {\"ref\": \"AEF:333\", \"status\": \"not_checked\",\n       \"note\": \"Khaleqi Motlaq's Persian version of Horn is catalogue-only in refs_online.json (no local copy, no scan); p. 333 could not be opened.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 65\", \"stance\": \"partial\",\n       \"note\": \"Gives 'N para' for both 1pārag 'piece' and 2pārag 'gift, bribe' — the New Persian word is the merger of two Middle Persian homophones.\"},\n      {\"src\": \"HRN\", \"where\": \"HRN.txt, no entry\", \"stance\": \"silent\",\n       \"note\": \"Grep for 'pāra/para' in Horn's Grundriss returns only 'aw. para, yār (+ sāl)' (l.3319); Horn has no numbered entry for پاره.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt before [pdf page 150]\", \"stance\": \"supports\",\n       \"note\": \"Aryanpur's Persian headword for this family is پاره, with Av. PARA, Pahl. PARAK/PARAG, Lat. PARS/PORTIO, Gk. PERASO, Skt. PURTI- and 'POKORNY 817'.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt l.28056\", \"stance\": \"supports\",\n       \"note\": \"See ref_check; Mo'in's definition covers 'money', 'gift' and 'piece' exactly as the chart glosses them.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"portio, pars; pertum\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Latin pars (gen. partis) 'a share, part' and portiō, -ōnis 'a part, proportion' are the standard reflexes of this root: Watkins reconstructs suffixed *par-ti- > pars and *par-tiō(n)- > portiō (first attested in the phrase prō portiōne, probably assimilated from *prō partiōne), and Klein p. 1133 s.v. 'part, n.' says 'L. partem, acc. of pars \\\"part\\\", which is rel. to L. portio \\\"share, portion\\\", and cogn. with Gk. peprotai \\\"it has been granted\\\", eporon \\\"I gave, granted\\\", OI. purtam \\\"reward\\\", Hitt. parshiya-'. Those two words are confirmed. The third form, 'pertum : price, worth', is not a Latin word at all — Latin has no *pertum. Two things have been run together on Nourai's page: (a) Klein's own entry on the cited page 1133 quotes Old Indic pūrtám 'reward, earnings' (Aryanpur's parallel entry likewise lists 'PURTI-, PURTIS (SANSKRIT)'), and (b) the gloss 'price, worth' is Klein's gloss of Latin pretium ('fr. L. pretium, \\\"worth, value, price\\\"', s.v. prize), which is what the English box below (price, prize) actually requires. So the printed form is a misprint standing for Latin pretium, contaminated with the Sanskrit pūrtám that Klein prints on the same page. The printed page (pdf 398, book 368) shows 'pertum : price, worth' exactly as the JSON has it, so the extraction is faithful and the error is the book's.\",\n     \"derivation_fa\": \"لاتینی pars (مضاف‌الیه partis) «بخش، سهم» و portio «بهره، نسبت» بازتاب‌های معمول این ریشه‌اند؛ واتکینز آن‌ها را از *par-ti- و *par-tiō(n)- می‌گیرد و کلاین (ص ۱۱۳۳) زیر part می‌نویسد که pars با portio خویشاوند و با یونانی époron و سنسکریت pūrtám «پاداش» هم‌ریشه است. اما صورت سومِ این خانه، «pertum: price, worth»، در لاتینی وجود ندارد: این خطای چاپی کتاب است. دو چیز در هم آمیخته: از یک سو سنسکریت pūrtám «پاداش، دستاورد» که درست در همان صفحهٔ ۱۱۳۳ کلاین آمده (و آریان‌پور هم PURTI-, PURTIS را در همین مدخل آورده)، و از سوی دیگر لاتینی pretium «بها، ارزش» که معنیِ نوشته‌شده («price, worth») دقیقاً معنیِ کلاین برای همان است و مشتقات انگلیسیِ خانهٔ بعد (price, prize) هم آن را می‌طلبند. تصویر صفحهٔ چاپی (ص ۳۶۸ کتاب) نشان می‌دهد که «pertum» در خودِ کتاب چاپ شده است؛ پس خطای چاپِ کتاب است نه خطای خوانشِ اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"pertum : price, worth\",\n     \"correct_form\": \"pretium 'price, worth' (Latin); the Sanskrit form Klein prints on the cited page is pūrtám 'reward'\",\n     \"sources\": [W_PER],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1133\", \"status\": \"partial\",\n       \"note\": \"Klein 1966 p. 1133 (between the leaf markers 1132/1133 and 1134/1135 in KLN_1966.txt) s.v. 'part, n.': 'ME., fr. OE. and OF. part, fr. L. partem, acc. of pars, \\\"part\\\", which is rel. to L. portio, \\\"share, portion\\\", and cogn. with Gk. peprotai \\\"it has been granted\\\", eporon \\\"I gave, granted\\\", OI. purtam \\\"reward\\\", Hitt. parshiya- \\\"fraction, part\\\".' Supports portio/pars; the page has no Latin 'pertum' — it has Old Indic pūrtám.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. perə-2: 'a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, PARSE, PART ...; b. possibly suffixed form *par-tio in Latin portio, a part (first attested in the phrase pro portione ...): PORTION, PROPORTION'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 817 (POK_full.txt)\", \"stance\": \"supports\",\n       \"note\": \"'γ. Old Indic purta-n., purti- f. \\\"earnings\\\" = Latin pars, -tis \\\"part\\\" (*pereti-), portio \\\"part, allotment\\\" (Post Classical; Classical only pro portione, assim. from *pro partione)'. Pokorny too pairs Latin pars/portio with Old Indic pūrtá-, never with a Latin 'pertum'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 13.28, p. 934\", \"stance\": \"supports\",\n       \"note\": \"'Lat. pars, -tis (> It., Sp., Rum. parte ...) prob. fr. the root of Ir. ro-ir \\\"(he) granted\\\", Grk. eporon \\\"gave, brought\\\" ... Walde-P. 2.41.'\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.30308 s.v. 'prize, n., reward'\", \"stance\": \"partial\",\n       \"note\": \"'ME. pris, fr. OF. pris (F. prix), \\\"price, prize\\\", fr. L. pretium, \\\"worth, value, price\\\". Prize is the doublet of price.' — 'worth, value, price' is the gloss the chart attaches to its ghost-form 'pertum'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"part, parcel, portion, compare, price, prize, prison\", \"verdict\": \"disputed\",\n     \"derivation\": \"Six of the seven are right. part < ME part < OE/OF part < Lat. partem; parcel < OF parcelle < VLat. *particella, dim. of particula < pars; portion < OF porcion < Lat. portiōnem; compare < OF comparer < Lat. comparāre 'to pair, match' (from pār 'equal', the same root); price < ME pris < OF pris < Lat. pretium, and prize 'reward' is its doublet (Klein: 'Prize is the doublet of price'). PRISON, however, does not belong to this root: Klein s.v. prison, 'ME. prison, prisun, fr. OF. prison, prisun, fr. VL. *presionem, fr. L. prensionem, acc. of prensio, contracted form of prehensio, \\\"a seizing, arresting\\\", fr. prehensus, pp. of prehendere', and Etymonline the same, tracing prehendere to PIE *ghend- 'to seize, take'. The word reached the chart because Old French pris 'taken' (from prendre) reshaped preson into prison, and because the homonymous prize 'something taken by force' is from prendre too — a formal interference, not a common origin.\",\n     \"derivation_fa\": \"از هفت واژهٔ این خانه شش تا درست است: part از فرانسهٔ باستان part و لاتینی partem؛ parcel از *particella در لاتینی عامیانه (مصغّرِ particula از pars)؛ portion از portionem؛ compare از comparare (از pār «برابر»، هم‌ریشه)؛ price از pretium از راه فرانسهٔ باستان pris، و prize «جایزه» دوگانهٔ (doublet) همان price است. اما prison به این ریشه ربطی ندارد: کلاین و اتیمانلاین هر دو آن را از لاتینی prehensionem/prensionem «گرفتن، دستگیری» از فعل prehendere و ریشهٔ هندواروپایی *ghend- «گرفتن» می‌گیرند. علت لغزش روشن است: صورتِ کهن‌ترِ فرانسوی preson زیر تأثیر pris «گرفته‌شده» به prison بدل شد و prize دیگری هم (به معنی «غنیمت») از همان prendre است؛ این تداخلِ صوری است نه هم‌ریشگی. پس دربارهٔ prison پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n     \"sources\": [E_PRISON, W_PER],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node carries no refs= of its own on the printed page; the English words are meant to be covered by the Latin box's AHD; KLN:1133.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.30296 s.v. 'prison' and l.30308 s.v. 'prize'\", \"stance\": \"contradicts\",\n       \"note\": \"'prison, n. — ME. prison, prisun, fr. OF. prison, prisun, \\\"jail, prison\\\", fr. VL. *presionem, fr. L. prensionem, acc. of prensio, contracted form of prehensio, \\\"a seizing, arresting\\\", fr. prehensus, pp. of prehendere, \\\"to lay hold of, seize, catch\\\". See prehensile.' Only price/prize 'reward' belong to pretium.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. prison\", \"stance\": \"contradicts\",\n       \"note\": \"'prison. (F. — L.) O.F. prisun ... L. acc. prensionem, acc. of prensio, a seizing ... for prehensus, pp. of prehendere, to seize.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. perə-2 and per-6\", \"stance\": \"partial\",\n       \"note\": \"Lists PARCEL, PARSE, PART, PORTION, PROPORTION, COMPARE under perə-2 and PRAISE, PRECIOUS, PRICE, APPRAISE under per-6; PRISON is absent from both (it stands under ghend-).\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"pornĕ\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Ancient Greek πόρνη pórnē 'prostitute' is literally 'one who is sold, bought', an o-grade *por-nā- built to πέρνημι pérnēmi 'I sell' (< *per-nā-mi), the nasal-present of this root; Klein glosses it 'Gk. πόρνη, orig. meant \\\"bought, purchased\\\", and is rel. to πέρνημι, \\\"I sell\\\", prop. \\\"I give for equal value\\\"'. Pokorny prints it in the same paragraph as πέρνημι ('πόρνη \\\"meretrix\\\"', IEW 817). The word is classical Attic (Archilochus onwards) and denoted a slave prostitute, i.e. one literally purchased — exactly Nourai's gloss '\\\"purchased\\\", prostitute'.\",\n     \"derivation_fa\": \"یونانی باستان πόρνη (pórnē) «روسپی» در اصل به معنی «خریده‌شده، فروخته‌شده» است: صورتی با واکهٔ o از ستاکِ *por-nā- در برابرِ πέρνημι pérnēmi «می‌فروشم» (< *per-nā-mi، صورتِ حال با میانوندِ -n-). کلاین می‌نویسد که πόρνη «در اصل به معنی خریده‌شده بود و با πέρνημι \\\"می‌فروشم\\\" مربوط است»، و پوکورنی نیز در همان بندِ ص ۸۱۷ آن را در کنارِ πέρνημι آورده است. در یونانِ کلاسیک این واژه به روسپیِ برده — یعنی کسی که به‌راستی خریده شده بود — گفته می‌شد؛ پس هم صورت و هم معنیِ نوشتهٔ نورایی درست است.\",\n     \"sources\": [W_PORNE, W_PER],\n     \"ref_check\": [\n      {\"ref\": \"POK:817\", \"status\": \"supports\",\n       \"note\": \"IEW 817, per-2 C, section α: 'Gr. πέρνημι (present and Impf.), περάω ... και πιπράσκω ... \\\"verkaufe\\\", (gr. stem *pera-), πόρνη \\\"meretrix\\\"'.\"},\n      {\"ref\": \"KLN:1219\", \"status\": \"supports\",\n       \"note\": \"Klein 1966 p. 1219 (leaf markers 1218/1219 at l.29631f., 1220/1221 at l.29685f., entry at l.29668) s.v. pornography: 'compounded of Gk. πόρνη, \\\"harlot\\\", and -γραφία ... Gk. πόρνη, orig. meant \\\"bought, purchased\\\", and is rel. to πέρνημι, \\\"I sell\\\", prop. \\\"I give for equal value\\\", πρίαμαι, \\\"I buy\\\" ... and cogn. with L. par, \\\"equal\\\", pretium, \\\"price\\\".'\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins per-6: 'II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por(s)-na in Greek porne, prostitute: PORNOGRAPHY.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 40\", \"stance\": \"supports\",\n       \"note\": \"'Gr. πέρνημι (Praes. und Impf.), περάω ... πιπράσκω, περάσω ... \\\"verkaufen\\\" (gr. St. perā-), πόρνη \\\"meretrix\\\"'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.26950 s.v. 'pair'\", \"stance\": \"supports\",\n       \"note\": \"'prob. cogn. with Avestic pairyante, \\\"they are compared\\\", Gk. πέρνημι, \\\"I sell\\\" ... Gk. πόρνη, \\\"harlot\\\", lit. \\\"bought, purchased\\\"' — Klein links the Greek and the Avestan members in one paragraph, as the chart does.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"pornography\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English pornography is a 19th-century learned compound (first in English 1842/1857, after French pornographie 1769, Restif de la Bretonne), Greek πόρνη 'prostitute' + -γραφία 'writing', coined to name 'a description of prostitutes' — originally an antiquarian term for the erotic wall-paintings unearthed at Pompeii. Klein p. 1219: 'pornography, n., 1) description of prostitutes or prostitution; 2) obscene literature. — Lit. \\\"a description of prostitutes\\\", compounded of Gk. πόρνη, \\\"harlot\\\", and -γραφία, fr. γράφειν, \\\"to write\\\".' The word is a book-coinage, not an inherited descent, and the chart's arrow Greek > English is the usual shorthand for that.\",\n     \"derivation_fa\": \"«pornography» انگلیسی واژه‌ای ساختگی و دانشورانه از سدهٔ نوزدهم است (نخست در فرانسه pornographie، سپس در انگلیسی حدود ۱۸۴۲–۱۸۵۷) که از πόρνη یونانی «روسپی» و -γραφία «نگارش» ساخته شده و در آغاز اصطلاحی باستان‌شناختی برای توصیفِ نقاشی‌های دیوارِ پومپئی بود. کلاین (ص ۱۲۱۹) آن را «به‌لفظ: توصیفِ روسپیان» می‌نامد. پس این وام‌گیری/برساخته است نه میراثِ زبانی، و پیکانِ «یونانی ← انگلیسی» در نمودار همین را به اختصار می‌رساند. ادعای نورایی درست است.\",\n     \"sources\": [W_PORNE],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"The node prints no refs= of its own; it is covered by the Greek box's POK:817; AHD; KLN:1219.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l.29668, p. 1219\", \"stance\": \"supports\",\n       \"note\": \"'pornography ... Lit. \\\"a description of prostitutes\\\", compounded of Gk. πόρνη, \\\"harlot\\\", and -γραφία, fr. γράφειν, \\\"to write\\\".'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. per-6\", \"stance\": \"supports\",\n       \"note\": \"PORNOGRAPHY is the sole English derivative Watkins lists for Greek porne under this root.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Perk 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *preḱ- / *perḱ- 'to ask, entreat' (Pokorny 4. perk̑-, prek̑-, pr̥k̑-skō, pp. 821-822)\",\n   \"note\": \"Pokorny's entry begins on p. 821 and runs onto 822, so Nourai's POK:821 is right. The label 'Perk 1' is Nourai's own numbering, not Pokorny's (Pokorny's perk̑-1 is 'gesprenkelt' p. 820, perk̑-3 'ausreissen' p. 821, and the 'ask' root is his perk̑-4); Watkins lists it simply as prek- 'To ask, entreat [Pok. 4. perk- 821]'. The gloss 'to ask' is exactly right. One structural caveat that runs through the whole chart: the Avestan branch (#1-#3) and the Old Persian branch (#4-#6) are drawn as two parallel descents ending in the same New Persian پرسیدن, and Nourai's own NOTEs cross-refer between them. Genetically only the Old Persian line is ancestral — New Persian is South-West Iranian and continues OP pr̥sa-/MP purs-; the Avestan forms are cognates, not ancestors. Nourai's double presentation is a presentational device, and his notes acknowledge it, but a reader should not take the Avestan > Pahlavi arrow literally.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *preḱ-/*perḱ- «پرسیدن، خواستن» است؛ مدخلِ پوکورنی از صفحهٔ ۸۲۱ آغاز می‌شود و تا ۸۲۲ ادامه دارد، پس ارجاعِ POK:821 درست است. شمارهٔ «Perk 1» از خودِ نورایی است نه از پوکورنی (پوکورنی این ریشه را perk̑-4 نامیده است) و واتکینز آن را ساده prek- «to ask, entreat» می‌آورد. معنای «پرسیدن» درست است. یک نکتهٔ ساختاری در سراسر این نمودار هست: شاخهٔ اوستایی (خانه‌های ۱ تا ۳) و شاخهٔ پارسی باستان (۴ تا ۶) هر دو به «پرسیدن» فارسی می‌رسند، ولی از نظر تبارِ زبانی تنها راهِ پارسی باستان راهِ واقعی است، زیرا فارسی نو دنبالهٔ گویشِ جنوب‌غربی است؛ صورت‌های اوستایی هم‌ریشه‌اند نه نیا. خودِ نورایی در یادداشت‌ها به این دوگانگی اشاره کرده است.\",\n   \"sources\": [W_PREK, W_PORS],\n   \"ref_check\": [\n    {\"ref\": \"POK:821\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: perk̑-4, prek̑-, pr̥k̑- | Meaning: to ask, ask for | Material: 1. sk̑o-present *pr̥k-sk̑ō ... Old Indic pr̥cchati \\\"fragt\\\", Avestan pərəsaiti \\\"fragt, longs for\\\" (participle pr̥šta-), ap. aparsam \\\"I frug\\\" ... 2. ... Avestan frasa f. \\\"question\\\" ... Avestan frašna- m. \\\"Befragung, question\\\" ... Latin prex f. \\\"request\\\", precor, -ārī \\\"bid, beg, ask\\\". Page(s): 821-822'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 44-45 (WLD_Bd2 l.2869ff)\", \"stance\": \"supports\",\n     \"note\": \"'perek̑ (perk̑-, prek̑-, pr̥k̑-) \\\"fragen, bitten\\\". sk̑o-Praes. *pr̥k-sk̑ō, woraus *pr̥skō: ai. pr̥cchati \\\"fragt\\\", av. pərəsaiti \\\"fragt, begehrt\\\" (Ptc. pərəsta-), ap. aparsam \\\"ich frug\\\", lat. posco ... Ai. praśna-, av. frašna- m. \\\"Befragung, Frage\\\" ... lat. prex \\\"Bitte\\\", precor, -ārī \\\"bitten\\\".'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. prek-\", \"stance\": \"supports\",\n     \"note\": \"'prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural preces), with denominative precari, to entreat, pray: PRAY, PRAYER, PRECARIOUS ... [Pok. 4. perk- 821.]'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 18.31 ASK (Question, Inquire), pp. 1264-1266\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *prek- and *pr(k)-sk-, etc. in words for \\\"ask\\\" in one or both senses. Walde-P. 2.44 ... Skt. pracch-, praś-, Av. fras- \\\"ask\\\", Arm. harcanem id., Toch. A pärk-, prak-, B prek-.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Etymological Dict. of the Iranian Verb, pp. 89-90 s.v. *fras/pr̥s\", \"stance\": \"supports\",\n     \"note\": \"'*fras/pr̥s \\\"to ask, inquire\\\" ... © This root has an impeccable etymology. *PIE *prek- \\\"to ask\\\" => LIV: 490 f. | Pok.: 821 f.'\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt, entry before [pdf page 162]\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's entry for پرسیدن lists 'PERESA, FRASA, PERESAITI (AVESTAN); APARSAM (OLD PERSIAN); PURSITAN (PAHLAVI); PRACCHATI (SANSKRIT); POSCO, POSCERE (LATIN)' with 'REFERENCES: POKORNY 821; SKEAT (PREK) 757; MALLORY & ADAMS: PERK' — the same set of forms Nourai charts.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"fras; frasâ,frašna; prs-sa, pere-sa; peresaiti; paiti-frasna\", \"verdict\": \"plausible\",\n     \"derivation\": \"The Avestan material is correct in the main. The root is fras- (Bartholomae AiW 997ff.), whose inchoative present is pərəsa- (Nourai's 'pere-sa', with its zero-grade spelling 'pr̥s-sa'), 3sg. pərəsaiti 'he asks' (Gathic pərəsā 'I ask', Y 31.14 etc.); the nouns are frasā-/fərasā- f. 'question, consultation' (AiW s.v.) and frašna- m. 'Befragung, question' (AiW 1009, quoted by Nyberg). PIE *pr̥k-sḱé-ti gave Proto-Iranian *pr̥sa-, with *-rs- > Av. -ərəs- and the inherited *sḱ cluster simplified to -s-; the f- of fras- is the regular Iranian outcome of *pr- before a consonant (cf. OP fra- vs. Skt. pra-). The one form that is not an attested Avestan word is 'paiti-frasna'. Avestan does have paiti.pərəsa- 'to interrogate someone' and the participle paiti.parəšta-, and Bartholomae records frasa- m. in the sense 'Gericht, Strafe' (court, punishment) and the compound pairi.frāsa-; but the actual Old Iranian preform of the Middle Persian word for 'punishment' is *pati-frāsa- (with the long-grade root noun frās-), not *pati-frašna-. Nourai has substituted the commoner noun frašna- for frāsa-; the sense he gives ('interrogation, punishment') is right, the form is a normalisation.\",\n     \"derivation_fa\": \"مادهٔ اوستایی fras- «پرسیدن» است (بارتولومه، ستون ۹۹۷ به بعد)؛ ستاکِ حالِ آن pərəsa- است (همان «pere-sa»ی نورایی) و سوم‌شخصِ مفردِ آن pərəsaiti «می‌پرسد». نام‌ها عبارت‌اند از frasā-/fərasā- «پرسش، رایزنی» و frašna- «پرسش» (بارتولومه ۱۰۰۹). از نظر آوایی *pr̥k-sḱé-ti هندواروپایی به *pr̥sa- ایرانی باستان رسیده، *rs به -ərəs- اوستایی بدل شده و *pr آغازین پیش از همخوان در ایرانی به fr- تبدیل شده است (سنجید با پارسی باستان fra- در برابر سنسکریت pra-). تنها صورتِ نادرست «paiti-frasna» است: اوستایی paiti.pərəsa- «بازپرسیدن» و paiti.parəšta- دارد و بارتولومه frasa- را نیز به معنی «داوری، کیفر» آورده، ولی نیایِ راستینِ واژهٔ فارسی میانهٔ «کیفر» صورتِ *pati-frāsa- (با ستاکِ کشیدهٔ frās-) است نه *pati-frašna-. پس معنا درست است و صورت یکدست‌شده؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_PREK],\n     \"ref_check\": [\n      {\"ref\": \"POK:821\", \"status\": \"supports\",\n       \"note\": \"IEW 821f.: 'Avestan pərəsaiti \\\"fragt\\\" (participle pərəsta-)' and 'Avestan frasa f. \\\"question\\\" ... Avestan frašna- m. \\\"Befragung, question\\\"'. Pokorny has no paiti- compound.\"},\n      {\"ref\": \"SNS:141\", \"status\": \"supports\",\n       \"note\": \"Tavoosi, Glossary of Shayast ne Shayast: the back index (SNS_pages.txt l.15911f.) reads 'pursīd 141/10, pursīdār 141/14, pursišn 141/15' — the words of this family stand on p. 141, as cited; the same glossary lists 'paitifrasa- 116/13' for the Avestan comparandum.\"},\n      {\"ref\": \"AEF:205\", \"status\": \"not_checked\",\n       \"note\": \"Khaleqi Motlaq's Persian edition of Horn is catalogue-only in refs_online.json; no copy on disk or online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW 997ff. s.v. fras- and frasa- (BRT.txt l.17880-17891)\", \"stance\": \"partial\",\n       \"note\": \"Bartholomae s.v. fras-: 'mit paiti ... 1) Jemanden (Akk.) fragen ... 2) Jemanden ausfragen, ausforschen ... paiti.parəšta- ... Pü.: pursītan, hampursītan ... pursišn, pursītār ... np. pursad'; s.v. frasa- m.: '1) Frage 2) Zurateziehen, Erforschung 3) Gericht, Strafe'. Supports fras-, pərəsaiti and the 'punishment' sense, but the compound is paiti.pərəsa-/pairi.frāsa-, not paiti-frašna-.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"pp. 89-90 s.v. *fras/pr̥s, AVESTAN section\", \"stance\": \"partial\",\n       \"note\": \"'*AVESTAN: fras- (parəsa-) \\\"to ask, inquire\\\", YAv. frašna- \\\"question\\\" || (+ *pati-) \\\"to ask, interrogate (someone)\\\"' — the paiti- form is a verbal compound; Cheung derives MP padifrah from *pati- + the root, i.e. *pati-frāsa-, not from frašna-.\"},\n      {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar\", \"stance\": \"silent\",\n       \"note\": \"Consulted for the inchoative present pərəsa-; no separate treatment of the paiti- compound.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"porsitan; pâtî-frâs\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian pursīdan <pwrsytn'>, present stem purs- <pwrs->, continues Old Iranian *pr̥sa- with the regular MP change *r̥ > ur before s; the infinitive is built on the secondary past stem pursīd-. Nyberg's glossary gives 'pursītan [pwrsytn'] to ask ... — Av. (997 sqq.) fras-, pres. pərəsa-, OP fraθ-, pres. p(a)rsa- (Kent); MPrth pwrsʾdn pwrs-; MPrs pwrsydn pwrs; Paz. NP pursīdan', i.e. Nourai's whole chain. The second word, pātifrās <p'tpl's>, is *pati-frāsa- 'the calling to account' > 'punishment, retribution'; Nyberg reads it pātifrās and notes it is a North-West (Parthian) form — 'MPrth pʾdyfrʾs, Arm. lw. patuhas, but SW pātifrāh: MPrs p'dypr'h' — while MacKenzie reads the Book-Pahlavi spelling as padifrah. Both readings are current; Nourai's 'pâtî-frâs' is Nyberg's, and Mo'in's footnote in Borhān (p. 206) prints the same.\",\n     \"derivation_fa\": \"فارسی میانه pursīdan (املای پهلوی pwrsytn') با ستاکِ حالِ purs- دنبالهٔ *pr̥sa-ی ایرانی باستان است؛ *r̥ در فارسی میانه پیش از s به ur بدل شده و مصدر بر ستاکِ ماضیِ جعلیِ pursīd- ساخته شده است. نیبرگ در واژه‌نامهٔ خود می‌نویسد: «pursītan: پرسیدن — اوستایی fras-، ستاک حال pərəsa-، پارسی باستان fraθ-، ستاک حال p(a)rsa-؛ پارتی میانه pwrsʾdn؛ فارسی میانه pwrsydn؛ پازند و فارسی نو pursīdan» — یعنی دقیقاً همان زنجیرهٔ نورایی. واژهٔ دوم pātifrās (املای p'tpl's) از *pati-frāsa- «بازخواست» و از آنجا «کیفر» است؛ نیبرگ آن را صورتِ شمال‌غربی (پارتی) می‌داند و صورتِ جنوب‌غربی را pātifrāh می‌خواند، حال آنکه مکنزی همان املا را padifrah می‌خواند. هر دو خوانش رایج است. ادعای نورایی درست است.\",\n     \"sources\": [W_PORS],\n     \"ref_check\": [\n      {\"ref\": \"BQT:206\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qate' p. 206 (the page opens 'بقیه از صفحهٔ ۲۰۵' and closes 'بقیه در صفحهٔ ۲۰۹') carries the headwords بادافراه / پادافراه / بادافره, and Mo'in's footnote 7 reads 'پهلوی pātifrās ... جزو دوم مشتق از [fras] هم‌ریشه و بمعنی پرسیدن ... جمعاً بمعنی بازپرسیدن، بازخواست' — Nourai's Pahlavi form and gloss exactly.\"},\n      {\"ref\": \"BQT:385\", \"status\": \"partial\",\n       \"note\": \"The پ section around printed pp. 383-385 of BQT_v1_pages.txt (the marker 'بقیه در صفحهٔ ۳۸۳' stands at l.24665) carries پرسا، پرستار، پرستش، پرسه، پرسیدن, i.e. the word family, but Borhan gives no Pahlavi etymology for پرسیدن there; the etymological footnote Nourai needs is the one on p. 206.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"Glossary p. 181 s.v. pursītan and p. 179 s.v. pātifrās\", \"stance\": \"supports\",\n       \"note\": \"'pursitan [pwrsytn'] to ask ... — Av. (997 sqq.) fras-, pres. pərəsa-, OP fraθ-, pres. p(a)rsa- (Kent); MPrth pwrsʾdn pwrs-; MPrs pwrsydn pwrs; Paz. NP pursīdan.' And 'pātifrās [p'tpl's], Ps. pātufrās [p'twpl's] punishment ... NW w.: MPrth p'dyfr's (MHC), Arm. lw. patuhas, but SW pātifrāh: MPrs p'dypr'h (S); Paz. pādafrāh.'\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 65 and p. 69\", \"stance\": \"supports\",\n       \"note\": \"'padifrah [p'tpl's | M p'dypr'h, N *pādafrāh] punishment, retribution' and 'pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 89 s.v. *fras/pr̥s, MIDDLE PERSIAN section\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: MMP pwrs-, BMP pwrs- /purs-/ \\\"to ask\\\" ... || (+ *pati-) ... ? MMP p'dypr'h, BMP p'tpl's /padifrah/ \\\"punishment, retribution\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"porsîdan; pâdafrâh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian پرسیدن porsīdan / present ستاک پرس pors- is MP pursīdan/purs- unchanged but for the raising of MP u to Classical NP u and modern o; the verbal noun پرسش porseš continues MP pursišn (Nyberg's 'pursišn'). Abolghasemi, whom Nourai cites for this very chart (TZF/ETM), sets it out in his Fe'l-hā-ye Fārsi-ye Dari: 'پرسید < فارسی میانه pursīd ... پرس < فارسی میانه purs < ایرانی باستان *pr̥sa-'. پادافراه pādafrāh 'punishment, retribution' is MP pādifrāh (MacKenzie explicitly gives 'N *pādafrāh'), i.e. *pati-frāsa- with the SW development of final *-s to -h; the a of the first syllable is the usual NP treatment of MP pādi-/pati- (cf. پاداش pādāš < MP pādāšn). The Vīs-o-Rāmīn couplet quoted on the page ('چه پاداش و چه پادافره نمودم') pairs it with پاداش, its exact antonym and morphological twin.\",\n     \"derivation_fa\": \"«پرسیدن» فارسی نو با ستاکِ حالِ «پرس» همان pursīdan/purs- فارسی میانه است و «پرسش» دنبالهٔ pursišn است. ابوالقاسمی — که نورایی خود به دو کتابِ او ارجاع داده — در «فعل‌های فارسی دری» می‌نویسد: «پرسید < فارسی میانه pursīd ... پرس < فارسی میانه purs < ایرانی باستان *pr̥sa-». «پادافراه» نیز دنبالهٔ pādifrāh فارسی میانه است (مکنزی صریحاً «N *pādafrāh» می‌آورد)، یعنی *pati-frāsa- که در گویشِ جنوب‌غربی sِ پایانی آن به h بدل شده است؛ صورتِ «پادا-» همان تحولِ معمولِ pādi-/pati- است (سنجید با «پاداش» از pādāšn). بیتِ ویس و رامین که در همین صفحه آمده، «پاداش» و «پادافره» را در برابر هم می‌نشاند. ادعای نورایی درست است.\",\n     \"sources\": [W_PORS],\n     \"ref_check\": [\n      {\"ref\": \"BQT:385\", \"status\": \"partial\",\n       \"note\": \"Printed pp. 383-385 of Borhan carry پرسا، پرستار، پرستش، پرسه («بمعنی پرسش و احوال برگرفتن»)، پرسیدن, but with no etymology; the word family is there, the derivation is not.\"},\n      {\"ref\": \"AEF:205\", \"status\": \"not_checked\",\n       \"note\": \"Asas-e Eshteqaq-e Farsi is catalogue-only in refs_online.json.\"},\n      {\"ref\": \"ETM:62\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Rishe-shenasi (Etimoloji): refs_online.json records 'Searched archive.org, ketabnak, noorlib, web: not found', no local file. His parallel treatment in Fe'l-hā-ye Fārsi-ye Dari (FFD, on disk) was used instead — see consulted.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FFD\", \"where\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari, [pdf page 47-48] s.v. پرسیدن\", \"stance\": \"supports\",\n       \"note\": \"'پرسیدن — پرسید < فارسی میانه pursīd؛ ... پرس < فارسی میانه purs < ایرانی باستان *pr̥sa- ... prs ریشه است، به معنی «پرسیدن»'. Nourai's own authority (Abolghasemi) in another of his books.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 65 s.v. padifrah\", \"stance\": \"supports\",\n       \"note\": \"'padifrah [p'tpl's | M p'dypr'h, N *pādafrāh] punishment, retribution' — MacKenzie himself supplies the New Persian pādafrāh.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پرسش (MON_part1.txt l.30602)\", \"stance\": \"supports\",\n       \"note\": \"'پرسش: (امص. پرسیدن) پرسیدن، سؤال، استفسار ... بازخواست، مؤاخذه' — the verbal noun printed in the chart's Persian-script field.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 299, p. 67\", \"stance\": \"supports\",\n       \"note\": \"'299. pursīden \\\"fragen\\\", pursiš ... ap. aw. fras-, Praes. pati-parsāhy bezw. pərəsahi \\\"fragen\\\"; Pahlavi pursītan, purs(i)šn, pursītār; ai. praś-, Praes. pr̥cchāti; arm. harc \\\"Frage\\\", harcanem \\\"fragen\\\"; kurd. pursin; oss. farsun/färsin.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"pare-sa; aparsam; frašta, frasta\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian has the root fraθ- 'ask, examine, investigate, punish' with the inchoative present stem pr̥sa- <p-r-s-a->: 1sg. pr̥sāmiy (DNb 19), imperfect a-pr̥sam 'I asked/punished' (DB 1.22, 4.67), imperative pr̥sā (DB 4.38, 69), and the compound pati-pr̥sa- 'read, recite'. Nourai's 'pare-sa' is the usual Latin-letter rendering of <p-r-s-a> with the inherent vowel written out. The participle appears only in the compound u-fraštam / u-frastam 'well punished' (DB 1.22, 4.38, 4.66f.) = *hu- 'well' + *frašta-/frasta- 'questioned, investigated' < PIE *prek-to-; Nourai's 'frašta, frasta : interrogated' is Kent's double spelling. Sound-wise, PIE *pr- > OP fr- before a consonant while *pr̥- gives par-/pr̥- before a vowel, which is why the same root shows fraθ-/fraštam beside pr̥sāmiy/aparsam — Kent makes exactly that point (§74.D: 'para but fra-, aparsam but -fraštam').\",\n     \"derivation_fa\": \"در پارسی باستان ریشهٔ fraθ- «پرسیدن، بازجستن، کیفر دادن» با ستاکِ حالِ pr̥sa- (نویسهٔ میخی p-r-s-a) به کار رفته است: pr̥sāmiy «می‌پرسم» (DNb ۱۹)، aparsam «پرسیدم/کیفر دادم» (بیستون ۱٫۲۲ و ۴٫۶۷)، امرِ pr̥sā (بیستون ۴٫۳۸ و ۶۹) و ترکیبِ pati-pr̥sa- «خواندن». «pare-sa»ی نورایی همان صورتِ آوانگاریِ p-r-s-a است. اسمِ مفعول تنها در ترکیبِ ufraštam/ufrastam «به‌سزا کیفرداده» دیده می‌شود، یعنی hu- «نیک» + frašta- «بازپرسیده‌شده» از *prek-to- هندواروپایی. از نظر آوایی *pr آغازین پیش از همخوان به fr- بدل شده ولی پیش از واکه par-/pr̥- مانده است؛ کنت خود همین را می‌گوید: «para ولی fra-، aparsam ولی -fraštam». ادعای نورایی درست است.\",\n     \"sources\": [W_PREK],\n     \"ref_check\": [\n      {\"ref\": \"KNT:176\", \"status\": \"supports\",\n       \"note\": \"Kent, Old Persian, p. 176 (between the page markers 176 at KNT.txt l.5173 and 177 at l.5210): 'ufrašta- ufrasta- adj. \\\"well punished\\\": u- \\\"well\\\" + ptc. frašta- or frasta- (§93) \\\"questioned, investigated\\\" to root fraθ-: pIE *su-prekto- ... ufraštam asm. DB 1.22, 4.66f; ufraštam DB 4.38.' Exactly Nourai's 'frašta, frasta : interrogated'. The forms pr̥sa-/aparsam are on Kent p. 198 s.v. fraθ-.\"},\n      {\"ref\": \"POK:821\", \"status\": \"supports\",\n       \"note\": \"IEW 821: 'ap. aparsam \\\"I frug\\\"'.\"},\n      {\"ref\": \"TZF:26\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi's Tarikh-e Mokhtasar-e Zaban-e Farsi is 'kind: website' in refs_online.json (ketabnak, login-walled); no copy obtainable.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent p. 198 s.v. fraθ-\", \"stance\": \"supports\",\n       \"note\": \"'fraθ- vb. \\\"ask, examine, investigate, punish\\\": Av. fras-, Skt. praś-, Lt. precor, pIE *prek-, with inchoative present, *pr̥k-ske-, OP parsa-, Av. pərəsaiti, NPers. pursad, Skt. pr̥cchāti, Lt. poscit ... pr̥sāmiy 1st sg. ... aparsam 1st sg. imf. DB 1.22; 4.67, pr̥sā 2d sg. imv. DB 4.38, 69.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 89, OLD PERSIAN section\", \"stance\": \"supports\",\n       \"note\": \"'*OLD PERSIAN: pr̥s- \\\"to ask; punish\\\" || (+ *pati-) \\\"to read, recite\\\" = Kent: 198a. Pres. inch.: IND. 1sg. pr̥sāmiy (DNb 19), impf. 1sg. apr̥sam (DB 1.22, DB 4.67) ... Partic.: perf. pass. (+ *hu-) °frasta- (DB 1.22, DB 4.66, DB 4.38, DB 4.69).'\"},\n      {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon\", \"stance\": \"silent\",\n       \"note\": \"Checked for an independent Old Persian lexicon entry; nothing beyond what Kent gives.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"purs\", \"verdict\": \"confirmed\",\n     \"derivation\": \"This box gives the Middle Persian present stem purs- <pwrs-> alone, i.e. the direct continuant of OP pr̥sa- (Old Iranian *pr̥sa-), with *r̥ > ur. It is the same Pahlavi word as node #2's pursītan, presented here as the bare stem so that the South-Western line OP pr̥sa- > MP purs- > NP pors-/porsīdan can be drawn without the pādifrāh material. MacKenzie: 'pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask'; Cheung lists the Manichaean and Book-Pahlavi paradigm (pwrsym, pwrsyd, pwrsynd).\",\n     \"derivation_fa\": \"این خانه تنها ستاکِ حالِ فارسی میانه purs- (املای pwrs-) را می‌آورد، یعنی دنبالهٔ مستقیمِ pr̥sa-ی پارسی باستان که در آن *r̥ به ur بدل شده است. همان واژهٔ خانهٔ شمارهٔ ۲ است، اما اینجا تنها ستاک آمده تا راهِ جنوب‌غربیِ pr̥sa- ← purs- ← «پرس/پرسیدن» بی‌درآمیختن با «پادافراه» نشان داده شود. مکنزی: «pursidan, purs- [pwrs-ytn'] پرسیدن» و چونگ صرفِ کاملِ آن را در فارسی میانهٔ مانوی و کتابی می‌آورد. ادعای نورایی درست است.\",\n     \"sources\": [W_PORS],\n     \"ref_check\": [\n      {\"ref\": \"TZF:26\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi: login-walled PDF only (refs_online.json 'kind': 'website'); could not be opened.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 69\", \"stance\": \"supports\",\n       \"note\": \"'pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. ~išn: question. ~išnīg: responsible.'\"},\n      {\"src\": \"NYB\", \"where\": \"Glossary p. 181 s.v. pursītan\", \"stance\": \"supports\",\n       \"note\": \"Nyberg explicitly chains 'OP fraθ-, pres. p(a)rsa- (Kent); ... MPrs pwrsydn pwrs' — the Old Persian > Middle Persian step Nourai draws here.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 89, MIDDLE PERSIAN paradigm\", \"stance\": \"supports\",\n       \"note\": \"'BMP pwrsym /pursēm/, BMP pwrsyh /pursē/, MMP pwrsyd, BMP pwrsyt /pursēd/, MMP pwrsynd, BMP pwrsynd /pursēnd/' — the stem purs- throughout.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"porsîdan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The same New Persian verb as node #3, reached here by the genetically correct route: OP pr̥sa- > MP purs- > NP pors-, infinitive porsīdan on the secondary stem porsīd-. Wiktionary states it in these terms — 'From Middle Persian pursīdan, from Old Persian p-r-s-a-mi-y (pr̥sāmiy, \\\"to ask, punish\\\"), from Proto-Iranian *pr̥sáti, from Proto-Indo-Iranian *pr̥šćáti, from Proto-Indo-European *pr̥sḱéti' — and Nourai's own NOTE on the box ('See the derivation through Avestan') acknowledges that the two boxes are one word. Of his two parallel lines this is the real ancestry; the Avestan line of nodes #1-#3 supplies cognates.\",\n     \"derivation_fa\": \"همان فعلِ «پرسیدن» خانهٔ شمارهٔ ۳ است، اما اینجا از راهِ درستِ تباری: پارسی باستان pr̥sa- ← فارسی میانه purs- ← فارسی نو «پرس/پرسیدن» (مصدر بر ستاکِ ماضیِ جعلیِ porsīd-). ویکی‌واژه نیز همین را می‌گوید: «از فارسی میانهٔ pursīdan، از پارسی باستانِ pr̥sāmiy، از ایرانی آغازینِ *pr̥sáti، از هندوایرانیِ آغازین *pr̥šćáti، از هندواروپایی *pr̥sḱéti». خودِ نورایی در یادداشتِ این خانه نوشته «ریشه‌یابی از راه اوستایی را ببینید» و پذیرفته که دو خانه یک واژه‌اند. از میان دو راهی که او کشیده، همین راه تبارِ راستین است و صورت‌های اوستایی هم‌ریشه‌اند نه نیا. ادعای نورایی درست است.\",\n     \"sources\": [W_PORS],\n     \"ref_check\": [\n      {\"ref\": \"TZF:26\", \"status\": \"not_checked\",\n       \"note\": \"Same login-walled source as node #5; not obtainable. Abolghasemi's equivalent statement was checked in FFD instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FFD\", \"where\": \"Fe'l-hā-ye Fārsi-ye Dari, [pdf page 47-48]\", \"stance\": \"supports\",\n       \"note\": \"'پرس < فارسی میانه purs < ایرانی باستان *pr̥sa-' — Abolghasemi's own wording for this exact chain.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn no. 299, p. 67\", \"stance\": \"supports\",\n       \"note\": \"'299. pursīden \\\"fragen\\\" ... ap. aw. fras-, Praes. pati-parsāhy ...; Pahlavi pursītan' — Horn puts the Old Persian pati-pr̥sāhy first.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"pp. 89-90, *NWIR section\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: Widely attested: NP pursidan/purs-, Kurd. (Kurm.) pirsin/pirs- ... \\\"to ask\\\"', under the root *fras/pr̥s with 'PIE *prek-'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Latin\", \"words\": \"precârî; prex\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin prex f. 'request, prayer' (attested in the classical language only in the oblique plural precēs, precum) is the bare root noun *prek-s, and precārī 'to entreat, pray, ask earnestly' is its denominative; beside them stand procus 'suitor' (o-grade) and poscō 'I demand' (< *pr̥k-skō, the same inchoative that gives Avestan pərəsaiti and Old Persian pr̥sa-). Pokorny prints 'Latin procus \\\"suitor\\\", prex f. \\\"request\\\", precor, -ārī \\\"bid, beg, ask\\\"' in section 2 of this entry, and Watkins makes it the first branch of prek-. The chart's spelling 'precârî' is Nourai's macron-free rendering of precārī.\",\n     \"derivation_fa\": \"لاتینی prex (مادینه) «درخواست، دعا» — که در لاتینِ کلاسیک تنها در حالت‌های غیرفاعلیِ جمع (precēs، precum) به کار رفته — همان اسمِ ریشه‌ایِ *prek-s است و precārī «دعا کردن، به‌الحاح خواستن» فعلی برساخته از آن است. در کنارِ آن‌ها procus «خواستگار» (با واکهٔ o) و poscō «می‌طلبم» (< *pr̥k-skō، همان ستاکِ حالی که pərəsaiti اوستایی و pr̥sa- پارسی باستان از آن است) قرار دارد. پوکورنی در بخشِ دومِ همین مدخل می‌نویسد «لاتینی procus، prex، precor, -ārī» و واتکینز نیز نخستین شاخهٔ prek- را همین می‌گیرد. ادعای نورایی درست است.\",\n     \"sources\": [W_PREK, E_PRAY],\n     \"ref_check\": [\n      {\"ref\": \"POK\", \"status\": \"supports\",\n       \"note\": \"IEW 821f., section 2: 'Latin procus \\\"suitor\\\", prex f. \\\"request\\\", precor, -ārī \\\"bid, beg, ask\\\", Umbrian pepurkurent \\\"poposcerint\\\"'.\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. prek-: '1. Basic form *prek- in Latin *prex, prayer (attested only in the plural preces), with denominative precari, to entreat, pray: PRAY, PRAYER, PRECARIOUS; DEPRECATE, IMPRECATE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 45\", \"stance\": \"supports\",\n       \"note\": \"'lat. procus \\\"Freier\\\", prex \\\"Bitte\\\", precor, -ārī \\\"bitten\\\", umbr. pepurkurent \\\"rogaverint, decreverint\\\"'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 18.31, p. 1264\", \"stance\": \"partial\",\n       \"note\": \"Buck files Latin poscere (the *pr̥k-skō present) under IE *prek- and treats precari under 'ask (request)' 18.35; same root, different synonym slot.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. prex / precor\", \"stance\": \"supports\",\n       \"note\": \"Pokorny's own citation for this branch is 'WH. II 346 f.' (Walde-Hofmann s.v. precor); Ernout-Meillet 794f. is the reference Buck gives for the same equation.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"pray, prayer\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English pray is first recorded c. 1225 (preien) 'ask earnestly, beg', from Old French preier (c. 900; Modern French prier), from Vulgar Latin *precāre, a re-formation of deponent Latin precārī; the religious sense 'address a god' is already in the earliest English citations and comes with the Anglo-Norman religious vocabulary. prayer (c. 1300, preiere) is from Old French prier/preiere, from Medieval Latin precāria, the feminine of the adjective precārius 'obtained by entreaty' used as a noun. Etymonline gives both under 'PIE root *prek- \\\"to ask, request, entreat\\\"', as does Watkins.\",\n     \"derivation_fa\": \"فعلِ انگلیسیِ pray نخستین بار در حدودِ ۱۲۲۵ میلادی به صورتِ preien «به‌الحاح خواستن» ثبت شده است؛ از فرانسهٔ باستانِ preier (سدهٔ دهم، فرانسهٔ امروز prier) و آن از *precāre در لاتینِ عامیانه، بازساختهٔ فعلِ مجهول‌صورتِ precārī. معنیِ دینیِ «نیایش کردن» از همان نخستین شواهدِ انگلیسی هست و همراهِ واژگانِ دینیِ آنگلونورمن وارد شده است. prayer (حدود ۱۳۰۰، preiere) از فرانسهٔ باستانِ prier/preiere و آن از precāria در لاتینِ میانه است، مؤنثِ صفتِ precārius «به‌خواهش به‌دست‌آمده» که اسم شده است. اتیمانلاین و واتکینز هر دو آن‌ها را زیرِ ریشهٔ *prek- می‌آورند. ادعای نورایی درست است.\",\n     \"sources\": [E_PRAY],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins 1985 s.v. prek-: Latin precari yields 'PRAY, PRAYER, PRECARIOUS; DEPRECATE, IMPRECATE'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. pray / prayer\", \"stance\": \"supports\",\n       \"note\": \"Klein derives pray from OF. preier, fr. VL. *precare, fr. L. precari, and prayer from OF. preiere, fr. VL. *precaria, fr. L. precarius — the same chain.\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary s.v. pray\", \"stance\": \"supports\",\n       \"note\": \"Consulted as a second English dictionary; gives OF. preier < LL. precare < L. precari, agreeing with Klein and Etymonline.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-398.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-398.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-398.json > /dev/null && echo JSON-OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 398",
 "description": "Write and validate page-398.json"
}
```


### [2026-09-14T01:06:32.955Z] TOOL RESULT

```
ok
JSON-OK
nodes verified: 15/15
node verdicts: {'confirmed': 11, 'plausible': 2, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'not_checked': 9, 'partial': 3}
books consulted: {'supports': 32, 'partial': 7, 'silent': 3, 'contradicts': 2} | by book: {'PHD': 5, 'KLN': 5, 'CHEUNG': 5, 'BRT': 3, 'WLD': 3, 'ARY': 3, 'HRN': 3, 'MON': 2, 'SYN': 2, 'AHD': 2, 'NYB': 2, 'FFD': 2, 'POK': 1, 'SKT': 1, 'AVG': 1, 'KNT': 1, 'TLM': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-14T01:06:42.846Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN pray\"; grep -n \"pray,  intr\\|pray,  tr\\|prayer,  n\\.\" KLN_1966.txt | head -3; echo \"### LAT precor\"; grep -n \"precor\\|prex\" LAT.txt | head -5; echo \"### FSD pray\"; grep -n \"OF\\. preier\\|preier\" FSD_vol3.txt FSD_vol4.txt FSD_vol2.txt 2>/dev/null | head -3; echo \"### AVG peresa\"; grep -n \"peresaiti\\|pərəsaiti\\|paresaiti\" AVG.txt | head -3; echo \"### TLM parsa\"; grep -n \"aparsam\\|ufrastam\\|frasta\" TLM.txt | head -5",
 "description": "Verify remaining consulted claims"
}
```


### [2026-09-14T01:06:42.983Z] TOOL RESULT

```
### KLN pray
29930:pray,  tr.  and  intr.  v.  —  ME.  preien,  fr.  OF.  preier (F.  prier),  fr.  VL.  precare  =  L.  precari,  ‘to  ask, beg,  pray,  request",  fr.  prex  (most  freq.  in  the  pi. preces ),  ‘prayer,  request,  entreaty’,  which  is  rel. to  procits,  ‘wooer’,  fr.  I.-E.  base  *perek-,  *perk-, *prk-,  ‘to  ask  (questions),  to  request’,  whence also  Ol.  prasna-,  Avestic  frashna-,  ‘question’, OSlav.  prositi,  Lith.  prasyti,  ‘to  ask,  beg’,  OHG. frdhen,  fragen,  MHG.,  G.  fragen,  OS.  fragon, OE.  fricgan,  and,  with  present  tense  infix  n-, Goth,  frailwan,  Obi.  fregna,  O E .  frignan,  frinan, ‘to  ask  (questions)’.  For  further  derivatives  of base  *perek-,  *perk-,  *prk-,  see  postulate.  Cp. deprecate,  imprecate,  precarious,  precatory,  prie- dieu,  prithee,  procacity.
29932:prayer,  n.  —  ME.  preiere,  fr.  OF.  preiere  (F. priere),  fr.  VL.  *precaria,  prop,  subst.  use  of  L. precaria,  fern,  of  the  adj.  precarius,  ‘obtained  by- prayer’,  fr.  precari,  ‘to  pray’.  See  prec.  word  and subst.  suff.  -er.
36414:Derivative:  spray e-y,  adj. spray,  n.,  jet  of  water.  —  LG.  sprei,  ‘spray,  driz¬ zle’,  rel.  to  MDu.  spraeien,  ‘to  sprinkle,  pour, spray’,  MHG.  sprsejen,  sprsewen,  ‘to  spray,  fly'. G.  spruhen,  ‘to  sparkle,  drizzle’,  OHG.,  MHG. spriu,  G.  Spreu,  ‘chaff’  (lit.  ‘that  which  flies about’),  fr.  I.-E.  base  *sp(h)er-,  ‘to  sow,  scatter’, whence  also  Gk.  oTteipetv,  ‘to  sow,  scatter’.  See sperm  and  cp.  words  there  referred  to. Derivatives:  spray,  intr.  and  tr.  v.,  spray-er,  n., spraye-y,  adj.
### LAT precor
5386:Arx serait un mot racine comme lux,uox, prex, etc. Mais il n'y a peut-
6020:39,87, Diui diuaeque -.. . uos precor quaesoque uti .quae in meo imperio
26737:Mars pater, te precor uti tu fruges frumenta uineta uirgultaque gran¬
28458:tation (cf. deprecor), exhortor (~td): exhorter (frtquent, classique;
29959:uos precor, ueneror... Toutefois indigetes doit etre en rapport avec
### FSD pray
FSD_vol3.txt:103981:preiernaiural swelling of the scrotum - os'ehfSiU*plaa'’t} ,
### AVG peresa
### TLM parsa
138:67.  0atiy  darayavaus  xsaya0iya  tuvarn  [ka]  xsaya0iya  68.  h}ra aparam  ahy  martiya  [kya]  draujana  ahatiy  hyava  [zujrakara  +   + ahat-69.  iy  avaiy  rua  dausta  +   +   +   a   ufrastadiy  parsa
192:8.  0atiy  [Dara]yava-21)us  xsayatfiya  a"tar  ima  dahyava  martiya hya  agar[ta]2 3  aha  avam  u-22)bartam  abaram  hva  araika  aha avain  ufrastam  aparsam  vasn[a]  Auramazda-23)ha  ima  dahyava tyanaa  mana  data8  apariyaya"4 5  yaflasam  hacama  a&th-24)ya [ajvaftl  akunavaya”ta®
447:5.  0iltiy  Darayavaus  xsilya0i-37)ya  tuvam  ka  x[saya0iya  htya aparam3  aky4  haca  drauga  darsam  38)patipayauva  mart[iya  hya drau]jana  ahatiy  avam  ufrastam5  parsa  ya-39)diy  ava0a  man[iyil- hav']6  dahyausmaiy  duruva  ahati-40)y
452:5   ufrastam,  KT.  See  voc.
497:[naiy  a]da[m  na]  imaiy  tauraa  upariy  arstam1  upariy-65)[axsa- yai}r]2  naiy  sakauri[m3  naiy]  +   +   tunnuvatamai  zura  akunavam martiya  kya  hamata-66)xsata  mana  v^ifya  a]vam  ubartam a[ba]ram  hya  viyana[sa]ya5  avam  ufrasta-67)m  aparsam
```


## [2026-09-14T01:07:05.796Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np=\"data/verification/page-398.json\"\nd=json.load(open(p))\nE={e[\"entry\"]:e for e in d[\"entries\"]}\ndef node(en,i):\n    return [n for n in E[en][\"nodes\"] if n[\"id\"]==i][0]\n\n# entry2 node1 AVG\nfor c in node(2,1)[\"consulted\"]:\n    if c[\"src\"]==\"AVG\":\n        c[\"stance\"]=\"silent\"\n        c[\"note\"]=\"Grepped AVG.txt (Jackson, Avesta Grammar) for 'peresaiti / paresaiti / pərəsaiti': no hit; Jackson's grammar does not cite this present among its paradigms in the OCR text available.\"\n# entry2 node4 TLM\nfor c in node(2,4)[\"consulted\"]:\n    if c[\"src\"]==\"TLM\":\n        c[\"stance\"]=\"supports\"\n        c[\"where\"]=\"Tolman, Ancient Persian Lexicon, Behistun text (TLM.txt ll.192, 497)\"\n        c[\"note\"]=\"Tolman's text of DB gives the forms Nourai cites in situ: 'avam ubartam abaram hya araika aha avam ufrastam aparsam' (DB 1.21f.) and 'avam ufrastam aparsam' (DB 4.66f.), plus 'avam ufrastam parsa' (DB 4.38) — aparsam 'I punished/asked' and ufrasta- 'well punished'.\"\n# entry2 node7 LAT\nfor c in node(2,7)[\"consulted\"]:\n    if c[\"src\"]==\"LAT\":\n        c[\"stance\"]=\"silent\"\n        c[\"where\"]=\"LAT.txt (Ernout-Meillet), searched for 'precor'/'prex'\"\n        c[\"note\"]=\"The OCR of Ernout-Meillet on disk yields only passing occurrences of prex/precor inside quoted Latin passages (ll. 5386, 6020, 26737); the dictionary entry itself could not be located in this scan, so the book is recorded as silent rather than cited. Pokorny's reference for this branch is Walde-Hofmann II 346f.\"\n# entry2 node8 KLN and FSD\nfor c in node(2,8)[\"consulted\"]:\n    if c[\"src\"]==\"KLN\":\n        c[\"where\"]=\"KLN_1966.txt ll.29930, 29932 s.vv. 'pray' and 'prayer'\"\n        c[\"note\"]=\"'pray, tr. and intr. v. — ME. preien, fr. OF. preier (F. prier), fr. VL. precare = L. precari, \\\"to ask, beg, pray, request\\\", fr. prex (most freq. in the pl. preces), \\\"prayer, request, entreaty\\\", which is rel. to procus, \\\"wooer\\\", fr. I.-E. base *perek-, *perk-, *prk-, \\\"to ask (questions), to request\\\", whence also OI. prasna-, Avestic frashna-, \\\"question\\\"'; 'prayer, n. — ME. preiere, fr. OF. preiere (F. priere), fr. VL. *precaria ... fem. of the adj. precarius, \\\"obtained by prayer\\\", fr. precari.'\"\n    if c[\"src\"]==\"FSD\":\n        c[\"stance\"]=\"silent\"\n        c[\"note\"]=\"Grepped the four FSD volumes for 'preier' / the OF etymon: no usable entry surfaced in the OCR (only a garbled unrelated line in vol. 3), so Funk & Wagnalls is recorded as silent.\"\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 -m json.tool data/verification/page-398.json >/dev/null && echo JSON-OK && python3 tools/verify_check.py 398",
 "description": "Patch consulted notes for accuracy"
}
```


### [2026-09-14T01:07:07.301Z] TOOL RESULT

```
patched
JSON-OK
nodes verified: 15/15
node verdicts: {'confirmed': 11, 'plausible': 2, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'not_checked': 9, 'partial': 3}
books consulted: {'supports': 31, 'partial': 7, 'silent': 4, 'contradicts': 2} | by book: {'PHD': 5, 'KLN': 5, 'CHEUNG': 5, 'BRT': 3, 'WLD': 3, 'ARY': 3, 'HRN': 3, 'MON': 2, 'SYN': 2, 'AHD': 2, 'NYB': 2, 'FFD': 2, 'POK': 1, 'SKT': 1, 'AVG': 1, 'KNT': 1, 'TLM': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-14T01:07:14.515Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB markers near 3015 and 3181 ===\"; awk 'NR>2960 && NR<3260 && /^[0-9]{2,3}$/ {print NR\": \"$0}' NYB_vol2_glossary.txt; echo \"=== KLN markers near 26950 ===\"; awk 'NR>26890 && NR<27010 && /^1[0-9]{3}$/ {print NR\": \"$0}' KLN_1966.txt",
 "description": "Verify Nyberg and Klein page numbers"
}
```


### [2026-09-14T01:07:15.523Z] TOOL RESULT

```
=== NYB markers near 3015 and 3181 ===
=== KLN markers near 26950 ===
26949: 1113
26983: 1114
26984: 1115
```


## [2026-09-14T01:07:20.536Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>2950 && NR<3260 && /^ *[0-9]{2,3} *$/ {print NR\": [\"$0\"]\"}' NYB_vol2_glossary.txt; echo \"--- alt: lines containing only digits possibly with spaces\"; grep -n \"^1[5-9][0-9]$\" NYB_vol2_glossary.txt | awk -F: '$1>2900 && $1<3300' | head",
 "description": "Find Nyberg page markers"
}
```


### [2026-09-14T01:07:21.777Z] TOOL RESULT

```
--- alt: lines containing only digits possibly with spaces
2932:150
2949:151
2969:152
3005:154
3014:155
3034:156
3052:157
3066:158
3094:159
3107:160
```


## [2026-09-14T01:07:29.458Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^1[6-9][0-9]$\" NYB_vol2_glossary.txt | awk -F: '$1>3100 && $1<3300'",
 "description": "Nyberg markers 160-190"
}
```


### [2026-09-14T01:07:30.613Z] TOOL RESULT

```
3107:160
3153:162
3185:163
3210:165
3255:167
3282:168
```


## [2026-09-14T01:07:38.934Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" PHD_pages.txt | head -3; echo \"---\"; grep -n \"padifrah\\|2parag\\|pursidan, purs\" PHD_pages.txt | head; echo \"--- page tag before those\"; awk '/\\[pdf page/{p=$0;n=NR} /padifrah \\[/{print \"padifrah at \"NR\" after \"p; exit}' PHD_pages.txt; awk '/\\[pdf page/{p=$0} /pursidan, purs-/{print \"pursidan after \"p; exit}' PHD_pages.txt; awk '/\\[pdf page/{p=$0} /2parag/{print \"parag after \"p; exit}' PHD_pages.txt",
 "description": "Find MacKenzie page numbers"
}
```


### [2026-09-14T01:07:40.201Z] TOOL RESULT

```
---
3912:padifrah [p'tpl's I M p)dypr'h, N ·piidafriih] punishment, retribution.
3946:padofrah [p)twpl)s] = padifrah.
4018:2parag [p'lk l I M p'rg, N para] gift, offering, bribe.
4280:pursidan, purs- [pwrs-ytn l I M pwrs-ydll, N ......] ask. \~ ? t(~ -
7373:punishment dros, padifrah, puhl.               razor awestarag.
7428:remain (abaz) mandan, (manistan),        retribution padasn, padifrah..
8828:peroz                     c;~Q)                padifrah               ~Q.)~QJ
8856:1-2parag                   \~CU              payag                      '~t)
--- page tag before those
padifrah at 3912 after 
pursidan after 
parag after
```


## [2026-09-14T01:07:50.847Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\np=\"data/verification/page-398.json\"\nd=json.load(open(p))\ns=json.dumps(d, ensure_ascii=False)\ns=s.replace(\"Klein 1966 p. 1149 s.v. 'pair'\",\"Klein 1966 p. 1113 s.v. 'pair'\")\ns=s.replace(\"p. 1149 s.v. 'pair'\",\"p. 1113 s.v. 'pair'\")\ns=s.replace(\"Glossary p. 181 s.v. pursītan and p. 179 s.v. pātifrās\",\"Glossary p. 162 s.v. pursītan and p. 155 s.v. pātifrās\")\ns=s.replace(\"Glossary p. 181 s.v. pursītan\",\"Glossary p. 162 s.v. pursītan\")\ns=s.replace(\"MacKenzie 1971 p. 65 s.v. pārag\",\"MacKenzie 1971 s.v. pārag (PHD_mackenzie.txt ll.4017-4018)\")\ns=s.replace(\"MacKenzie p. 65\",\"MacKenzie s.v. pārag (PHD_mackenzie.txt l.4018)\")\ns=s.replace(\"MacKenzie 1971 p. 65 and p. 69\",\"MacKenzie 1971 s.vv. padifrah and pursidan (PHD_mackenzie.txt ll.3912, 4280)\")\ns=s.replace(\"MacKenzie 1971 p. 69\",\"MacKenzie 1971 s.v. pursidan (PHD_mackenzie.txt l.4280)\")\ns=s.replace(\"MacKenzie p. 65 s.v. padifrah\",\"MacKenzie s.v. padifrah (PHD_mackenzie.txt l.3912)\")\nd=json.loads(s)\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\ngrep -c \"p. 1149\\|p. 181 s.v\\|MacKenzie 1971 p\\.\\|MacKenzie p\\. 65\" data/verification/page-398.json; python3 -m json.tool data/verification/page-398.json >/dev/null && echo JSON-OK && python3 tools/verify_check.py 398",
 "description": "Fix page citations"
}
```


### [2026-09-14T01:07:52.102Z] TOOL RESULT

```
ok
0
JSON-OK
nodes verified: 15/15
node verdicts: {'confirmed': 11, 'plausible': 2, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'not_checked': 9, 'partial': 3}
books consulted: {'supports': 31, 'partial': 7, 'silent': 4, 'contradicts': 2} | by book: {'PHD': 5, 'KLN': 5, 'CHEUNG': 5, 'BRT': 3, 'WLD': 3, 'ARY': 3, 'HRN': 3, 'MON': 2, 'SYN': 2, 'AHD': 2, 'NYB': 2, 'FFD': 2, 'POK': 1, 'SKT': 1, 'AVG': 1, 'KNT': 1, 'TLM': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-14T01:08:11.038Z] AGENT

Page 398 (book p. 368) verified. `verify_check.py 398` → **0 PROBLEM lines**, 15/15 nodes.

**Counts**
- Roots: 2 confirmed (`Per 4, Pera` = POK 817 *per‑2 C "to sell/allot"; `Perk 1` = POK 821f. *perḱ‑/prek̑‑ "to ask"). One redirect entry (`Pera`) skipped.
- Nodes: 11 confirmed, 2 plausible, 1 disputed, 1 transcription_suspect.
- Ref checks: 16 supports, 3 partial, 9 not_checked (AEF, ETM, TZF have no obtainable copy).
- Books consulted: POK, WLD, AHD/Watkins, KLN, SKT, SYN(Buck), BRT, KNT, TLM, PHD, NYB, CHEUNG, HRN, BQT, MON, ARY, FFD, SNS.

**Flagged items**
- `transcription_suspect` — **Per 4 / #4 Latin "pertum : price, worth"**: no such Latin word. `error_in: "book"` — the printed page (pdf 398) really prints it, so the extraction is faithful. It conflates Klein p. 1133's Old Indic *pūrtám* "reward" (Aryanpur's parallel entry likewise lists Skt. PURTI-, PURTIS) with Latin *pretium* "worth, value, price" (Klein's own gloss), which is what the English box below (price, prize) requires. Page image saved to `data/verification/sources/refs/ocr/BOOK/398.png`.
- `disputed` — **Per 4 / #5 English "prison"**: Klein, Skeat and Etymonline all derive it from L. *prehensiōnem/prensiōnem* "a seizing" (PIE *\*ghend-*), not from *per-*; it entered the chart via the formal interference of OF *pris* "taken". The other six (part, parcel, portion, compare, price, prize) are correct.
- `plausible` — **Per 4 / #3 Persian پاره**: BQT 351 and Mo'in support all three glosses, but modern work (MacKenzie's 1pārag "piece" vs 2pārag "gift, bribe"; Wiktionary) splits two homonyms; only the "gift/bribe/money" sense descends from Av. *pāra-* "debt", while آتش‌پاره belongs to the "piece" word.
- `plausible` — **Perk 1 / #1 Avestan "paiti-frasna"**: not an attested Avestan compound; the preform of MP *pātifrās/pādifrāh* is *\*pati-frāsa-* (cf. Av. *frasa-* "Gericht, Strafe", *pairi.frāsa-*), not *\*pati-frašna-*. Sense right, form normalised.

**No extraction errors** — every form, gloss, script field, note and quotation in `page-398.json` matches the printed page.

Notable confirmations: Nyberg p. 150 states Nourai's Av. *pāra-* → MP *pārak* → NP *pāre* chain verbatim; Borhān p. 206 carries Mo'in's footnote giving exactly Pahl. *pātifrās*; Kent p. 176 is indeed the *ufrašta-/frašta-, frasta-* page. BQT:385 is only `partial` (the پرسیدن family is there, the etymology is not — that sits on p. 206).
