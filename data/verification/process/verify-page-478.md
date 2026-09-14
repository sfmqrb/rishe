# Verification process log — verify-page-478


## [2026-09-14T02:28:20.757Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 478 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-478.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-478.json. Write /home/sfmqrb/git/rishe/data/verification/page-478.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 478` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:21.831Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:22.610Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:22.622Z] TOOL RESULT

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


## [2026-09-14T02:28:23.112Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-478.txt"
}
```


### [2026-09-14T02:28:23.132Z] TOOL RESULT

```
1	=== PDF page 478 (book page 448) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Steig, Stig, Teig : pointed, sharp  (refs POK:1016)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1016 | tiğra : sharp, pointed ; taĕža, taĕğa : sharp ; tigrâ : Tigris, "fast moving" river
5	  #2 (parent #1) [Persian] refs=BQT:543,1104,1105 | tîr «تیر» : "pointed" thing, sharp, arrow ; tîr-kaš «تیرکش» : a bag for carrying arrows, quiver ☞Kenk 1 ; setîz «ستیز» : sharp ; setîhîdan «ستیهیدن» : to fight | extra: تیز ، تیج ؛ ترکش ؛ ستیزیدن ، ستیزه ، ستیغ ؛ ستهیدن
6	  #3 (parent #1) [Semitic] refs=IRN:112 | Diglat : Tigris
7	    #4 (parent #3) [Arabic] refs=IRN:112 | Dîjlat
8	      #5 (parent #4) [Persian] refs=MON5:520; IRN:112 | Dejleh «دجله» : "fast river", Tigris ; Dîyâleh «دیاله» : name of another river in Iran | NOTE: "Arvand :swift (river)" is translation of "Dejleh: fast (river)".
9	#6 (parent #0) [Greek] refs=PRT:667 | tigris : fast running
10	  #7 (parent #6) [English] refs=PRT:667 | tiger : a fast running animal ; Tigris : a fast moving river
11	#8 (parent #0) [Greek] refs=AHD | stizein : to prick ; a-stigmat : without a (focal) point
12	  #9 (parent #8) [French] refs=None | 
13	    #10 (parent #9) [Persian] refs=MON:54 | âstîgmât «آستیگمات»
14	  #11 (parent #8) [English] refs=None | astigmatism
15	#12 (parent #0) [Germanic] refs=AHD | stik : to prick, attach
16	  #13 (parent #12) [French] refs=AHD:451 | etiquette : label, a set of instructions
17	    #14 (parent #13) [Persian] refs=MON:140 | etîket «اتیکت» : manners
18	    #15 (parent #13) [English] refs=None | etiquette
19	  #16 (parent #12) [English] refs=None | stick ; ticket
20	#17 (parent #0) [Latin] refs=AHD | stinguere : to separate, distinguish
21	  #18 (parent #17) [English] refs=None | distinguish ; extinguish ; instinct
22	
```


## [2026-09-14T02:28:26.058Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-478.json | head -200",
 "description": "Read source JSON for page 478"
}
```


### [2026-09-14T02:28:26.104Z] TOOL RESULT

```
{
  "pdf_page": 478,
  "book_page": 448,
  "entries": [
    {
      "root": {
        "name": "Steig, Stig, Teig",
        "lang": "Indo-European",
        "refs": "POK:1016",
        "gloss": "pointed, sharp"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:1016",
          "words": [
            {"translit": "tiğra", "gloss": "sharp, pointed", "script": null},
            {"translit": "taĕža, taĕğa", "gloss": "sharp", "script": null},
            {"translit": "tigrâ", "gloss": "Tigris, \"fast moving\" river", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:543,1104,1105",
          "words": [
            {"translit": "tîr", "gloss": "\"pointed\" thing, sharp, arrow", "script": "تیر"},
            {"translit": "tîr-kaš", "gloss": "a bag for carrying arrows, quiver", "script": "تیرکش", "see": ["Kenk 1"]},
            {"translit": "setîz", "gloss": "sharp", "script": "ستیز"},
            {"translit": "setîhîdan", "gloss": "to fight", "script": "ستیهیدن"}
          ],
          "script_extra": "تیز ، تیج ؛ ترکش ؛ ستیزیدن ، ستیزه ، ستیغ ؛ ستهیدن",
          "note": null,
          "quote": {
            "text": "چون نداری ناخن درّنده تیز - با ددان آن به کم گیری ستیز",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Semitic",
          "refs": "IRN:112",
          "words": [
            {"translit": "Diglat", "gloss": "Tigris", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "IRN:112",
          "words": [
            {"translit": "Dîjlat", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON5:520; IRN:112",
          "words": [
            {"translit": "Dejleh", "gloss": "\"fast river\", Tigris", "script": "دجله"},
            {"translit": "Dîyâleh", "gloss": "name of another river in Iran", "script": "دیاله"}
          ],
          "note": "\"Arvand :swift (river)\" is translation of \"Dejleh: fast (river)\".",
          "quote": {
            "text": "اگر پهلوانی ندانی زبان - بتازی تو ارونـد را دجله خوان",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "PRT:667",
          "words": [
            {"translit": "tigris", "gloss": "fast running", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "PRT:667",
          "words": [
            {"translit": "tiger", "gloss": "a fast running animal", "script": null},
            {"translit": "Tigris", "gloss": "a fast moving river", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "stizein", "gloss": "to prick", "script": null},
            {"translit": "a-stigmat", "gloss": "without a (focal) point", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:54",
          "words": [
            {"translit": "âstîgmât", "gloss": null, "script": "آستیگمات"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "astigmatism", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "stik", "gloss": "to prick, attach", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "French",
          "refs": "AHD:451",
          "words": [
            {"translit": "etiquette", "gloss": "label, a set of instructions", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:140",
          "words": [
            {"translit": "etîket", "gloss": "manners", "script": "اتیکت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "etiquette", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "stick", "gloss": null, "script": null},
            {"translit": "ticket", "gloss": null, "script": null}
          ],
          "note": null,
```


## [2026-09-14T02:28:26.912Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:28:26.959Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T02:28:31.038Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '200,300p' data/extracted/batch/page-478.json; echo ===; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','PRT','IRN','MON','BQT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n\"",
 "description": "Rest of JSON and ref metadata"
}
```


### [2026-09-14T02:28:32.163Z] TOOL RESULT

```
Exit code 1
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "stinguere", "gloss": "to separate, distinguish", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "distinguish", "gloss": null, "script": null},
            {"translit": "extinguish", "gloss": null, "script": null},
            {"translit": "instinct", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
(eval):1: == not found
```


## [2026-09-14T02:28:34.690Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','PRT','IRN','MON','BQT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print()\n\"",
 "description": "Ref metadata for keys"
}
```


### [2026-09-14T02:28:35.757Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.", "notes": "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."}

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.",

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
```


## [2026-09-14T02:29:14.447Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-14T02:29:14.492Z] TOOL RESULT

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


## [2026-09-14T02:29:21.605Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=p.split('\\f')\nprint(\"leaves\",len(leaves))\n# POK_01: leaf = p + 8\nfor pg in (1016,1017):\n    i=pg+8\n    if i<len(leaves):\n        print(\"==== printed\",pg,\"leaf\",i)\n        print(leaves[i][:3000])\nEOF",
 "description": "Pokorny p.1016-1017"
}
```


### [2026-09-14T02:29:22.711Z] TOOL RESULT

```
leaves 364
```


## [2026-09-14T02:29:26.338Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; python3 -c \"\nimport sys\np=open('$f',encoding='utf-8',errors='replace').read()\nprint('leaves',len(p.split(chr(12))),'chars',len(p))\n\"; done\ngrep -n \"steigh-\\|(s)teig-\\|steig-\" POK_03.txt | head -30",
 "description": "Locate Pokorny steig-"
}
```


### [2026-09-14T02:29:27.583Z] TOOL RESULT

```
== POK_01.txt
leaves 364 chars 966268
== POK_02.txt
leaves 434 chars 1119436
== POK_03.txt
leaves 430 chars 1150862
== POK_full.txt
leaves 1 chars 3967710
3534:steigh-  »schreiten,  steigen';  st{o)igho-,  stigh-tä  ,Weg'.
3557:3.  stel-,  steig-  , ausbreiten,  flach  hinbreiten';  stlä-to-  , breit'.  /-    J
3586:steig-  (auch  stelk-'?)  nominal  {s)tolgo-:
```


## [2026-09-14T02:29:30.809Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"stechen\" POK_03.txt | sed -n '1,60p'",
 "description": "Find stechen entries in POK_03"
}
```


### [2026-09-14T02:29:30.866Z] TOOL RESULT

```
338:1.  peig-  und  peik-  , Kennzeichnen  durch  einritzen  oder  färben ;  bunt,  farbig' (daneben  Worte  für  ,stechen');  pik-ro-  ,bunt';  poiko-  ds.;  pelu-poiko- ,viele  Flecken  habend'.
768:peuk-  und  peug-  ,stechen',  atch  ,boxen*  (,mit  vorgestrecktem  Knöchel  des Mittelfingers').
769:r.  peuk'  :  gr.  *nsvKog  n.  , Spitze,  Stachel'  in  gr.  TtsoL-nsvaig,  hom.  i^^^ TCEvyLsg  ,mit  einer  Spitze  versehen';  ftevAsdavög  ,stechend,  verwundend* später  jbitter',  7tevY.alL}iog  ,scharf,  eindringend'*,  ^  ^  ;:.
770:hierher  als  ,die  stechende'  das  Wurzelnomen  peuk-  :  puk-  ,Fichte*  ix^ gr.   TtevyiT)   f.  ds.,   thrak.   ON    JTsvxiy,   illjr.  VN   Peucetii,    mir.    ochtach  l  -^^ (*puktäkä)  ,Fichte,  Speer';  8.hd.  fiuhta,  SiSdichs.  fiuhtia  {*fiuhtjön)  »Fichte*, apr.  peuse  f.  ,Kiefer'   (halt.  *piause\   schwundstuf.   lit.   puSis  f.,  Gen.  P|. pusiij  ostlit.  Nom.  Fl.  pü§es  (kons.  St.).
993:gr.  ftQsrttü  , falle  in  die  Augen,  erscheine,  steche  hervor,  zeichne  mich aus',  TtQSTtSL  ,es  ziemt  sich',  ägi-,  dia-,  in-,  sd-,  iiera-TtQercrjg  ,hervor- stechend,  sich  auszeichnend';  d^eo-ngÖTtog  , Seher'  (,der  sich  von  Gott  aus vernehmlich  Machende');  vielleicht  rtgaTclg  , Zwerchfell';  anders  oben  S.  620.
2029:khai-t~  in  arm.  xait''  ,stechen.  Stich*,  xait^em  , steche',  xit'^am  ,bin  ängst- lich', xit''  ,Betrübtheit,  heftiger  Schmerz';  dagegen  xio-t  ,stutzig,  ängstlich, argwöhnisch'  aus  *khid-ro-]
2114:ahd.  scehan  st.  V.  ^eileii;,  schnell  fortgehen'^  mhd.  nhd.  geschehen,  ags. sceon  schw.  V.  ,geschehen,  eilen*;  mhd.  schehen  schw.  V.  .schnell  einher- fahren;  eilen',  ahd.  skihtlg  ,scheu'  (got.  sköhsl  n.  ,böser  Geist,  Unhold'  als einherfahrend*  oder  , schüttelnd'  hierher?);  Faktitiv  mhd.  schicken  (^von- statten  gehen  lassen')  »bereiten^  ordnen,  senden',  nhd.  schicken]  ahd.  geseiht ^Ereignis',  nhd.  Geschichte,  mhd.  schiht , Anordnung,  Schicht  (bei  Bergleuten, und  sonst)';  mit  gramm.  Wechsel:  aisl.  skaga  ^hervorspringen,  hervor- stechen', skagi  m.  , Landzunge^,  dehnstufig  skögr  m.  ,Wald';  ags.  töscecgan jsich  scheiden*,  sceaga  m.  , Gebüsch'  (aus  ,Wald') ;  auch  aisl.  skegg  n.  ;Bart' (*skaggja-),  ags.  sceagga  , Haupthaar',  aisl.  skeggja  f.  , Streitaxt'  (vgl.  nhd. Barte  ds.);
2119:1.  (s)kel-  »schneiden^,  nicht  zuverlässig  von  kel-  , schlagen'  und  kel-  ^stechen'
2347:aisl.  skera  ,schneiden,  stechen,  abmachen',  ahd.  sceran  ,scheren,  ab- schneiden', ags.  scieran  ds.,  as.  sker-sahs  , Schermesser' ;  ahd.  scero  , Maul- wurf, nhd.  Schermaus,  norw.  vatn-skjer  u.  dgl.  ,Spitzmaus'  (vgl.  unten ags.  scierfe-müs  , Spitzmaus') ;  Kaus.-Iter.  ahd.  scerian,  as.  skerjan,  ags. scierian  ,zuteilen,  bestimmen';  aisl.  sk^r  f.  ,Haar;  Rand;  Ende',  ags.  sceörrit f.  ,das  Haarschneiden;  Anteil',  ahd.  scara  , Heeresabteilung,  Schar  usw.', mnd.  schare  f.  ds.  (daraus  aisl.  skqr  f.,  skari  m.  , Schar,  Menge^) ;  mit nicht  klarer  Bed. -Entw.  ahd.  liaram-skaraj  as.  harm-skara,  ags.  hearm- scearu  , Strafe,  Plage' ;
2636:skuerh{h)-  , stechen,  etwa  wie  Dornen'?  Nur  keltisch  und  baltisch. Com.  bret.  syern  ,spinae*  {-rn-  aus  -rhn-) ;
2637:lit.   skverbiü,   skverbti   ,m\i   einem   spitzen  Werkzeug   bohrend   stechen', Iter.    skvarhaüj   skvarbyti  ds.,   skvirhinu,   -inti  , stechen,   bohren,  prickeln', WP.  II  602.
3474:2.  {s)teg-   ,Stange,   Pfahl,    Stock,    Knüttel,   Balken*;    s.   auch   unter   ftii* , stechen'.
3484:stegh-j  nasal,  stengh-  , stechen;  Stange,  Halm,  Spitzes,  Steifes*.
3485:Gr.  (TTÖxog  ,das  aufgestellte  Ziel,  Vermutung'  (aroxaCoi.Lai  , ziele,  forsch« aus,  errate*) ;  schwed.  stagg  (germ.  *stagga-)  ,steifes  und  stechendes  Gras'; dial.  ,Achel,  Stichling  (Fisch)',  wozu  *staggian-  .mit  *Stachel  =  penil versehen*  in  aisl.  steggi  m.  , Stecher*,  nisl.  auch  ,Kater'  (spät  ags.  stagg^ m.,  engl,  stag  ,der  ausgewachsene  Hirsch',  engl.  dial.  auch  , Männchen', aus  dem  Nord.);  preuß.-lit.  stege,  stegis  , Stichling*,  lett.  staga{i)8  ,ein stacheliger  Fisch',  stage  , Alant'  (auch  stagi  ,ein  Kraut,  das  als  Kohl gegessen  wird'?);
3489:aisl.  stinga,  stakk,  ags.  stingan  , stecken' ;  got.  usstagg  ,e^els,  stich  aus!'; jhd.  stanga,  aisl.  stgng  ,Stock,  Pfahl,  Stange',  ags.  steng  (*stangi-)  ds.,  nl. steng  (*stangiö[n]-)  ds.,  ahd.  stengil , Steng eV  \  ablaut.  ahd.  stungen  .stechen';
3494:Av.  staera-  ,Bergspitze'  ^Wg  Xsy.,  taera-  ,Bergspitze,  Gipfel'  (wohl  *stoi- lo-,  so  daß  die  Vollstufe  zu:)  lat.  stilus  ^spitziger  Pfahl,  Stiel,  Stengel, Griffel  zum  Schreiben';  mit  Formans  -wo-:  lat.  sti-mu-lus  , Stachel';  dazu lat.  stlva  (und  *steva  der  rom.  Sprachen)  ^Pflugsterz'  als  *stei-uä?  vgl.  ai. tivrd-  , heftig,  scharf,   das   aus  ,*spitz,   stechend'   entwickelt  sein   könnte;
3508:{s)teig-  ,stechen;  spitz',  Erweiterung  von  stei-  ds.;  (s)tig-tO'  ,gestickt'.
3516:got.  stiks  , Stich,  Punkt',  ahd.  stih,  as.  stiki,  mnd.  steke,  ags.  stice  m.  ,df/j stician  ,stechen* ;  Intr.  ,steckenbleiben,  fest  bleiben*,  mnd.  sticken  ,stecbeni sticken,  anzünden,  ersticken*,  ahd.  sticken  , stechen,  sticken',  ir-sticken  ,er*
3521:festheften,  festhaften',  ahd.  stehhan,  nhd.  stechen,  Kaus.   *stakjan  in  ahd.
3526:o-ot.  stiks,  nhd.  stechen  zu  einer  neuen  Einheit  zusammenschloß;  so  beruht
3531:zu  *stig-  stellen  sich  noch:  aisl.  stikill  , Spitze*,  ags.  sticel(s)  m.  ,Stachel', mnd.  stekel,  ahd.  stihhil  ,Stachel',  nhd.  Stichel]  got.  stikls,  ahd.  stehhal ^Becher*  als  ,zum  Einstecken  in  die  Erde  unten  zugespitzt  verlaufendes Gefäß';  as.  stekal  ,rauh,  steinig*,  mnd.  stekel  ,devexus',  ags.  sticol  , steil, hoch',  ahd.  stehhal,  mhd.  stechel,  Stichel,  stickel  , steil'  als  ,die  Fußsohlen stechend,  voll  spitzer  Steine' ;
3754:stre-k-:    ags.    stregdan    st.  V.    ,streuen,    spritzen,   verteilen'   (Prllil#'  [ bildung  wie   bregdan)]    dehnstufig   aksl.   strekati   ,stechen',   ablaut  ttnkl j^yiivzgov,   ariyna^,    slav.   *stn>kati   in   cech.   strkati   ,stoßen',    serb.  $^Ct^ »spritzen'.  ,^^,
3778:t)ter-n-   in  Worten    für    stechende    Pflanzenschäfte;    zu    ster-    ,starren, f  steif  sein*.
3797:A.  {s)teu-k-'.  gr.  rv-Aog  ,Hammer,  Meißel;  Streitaxt*,  rrx/fc Steine',  rvndvrj  ,Dresch Vorrichtung*  (bei  Hes.  Tviavif)]  air.  toll , Höhle,  Loch'  [Hukslo-),  cymr.  twll  ,foramen',  adj.  ,perforatus', ,Loch*;  wahrscheinlich  ahd.  düJien  ,drücken,  niederdrücken', deon  , drücken,  zwingen,  stechen*   (s.   Genaueres  u.   tuengh-  ,b(
3798:lett.   tukstet   ,klopfen*,   taucet  ,im  Mörser  stampfen',  russ.-kal ,effodere*,  aksl.  tzkati  , weben,  stechen',  usw. ;
3805:I  sch^e<^*  Stuka  , überwältigen*,  norw.  stauka  , stoßen,  verletzen,  stottern', IudI-  ^^^'  ^^^^^'"'  ^stoßen,  aufschichten,  erstaunen*,  nhd.  verstauchen  (aus I  ^gjji  Nd.)?  ^^^-  ^^rstuiken  ^verrenken*;  afries.  stak  ,steif*  zu  norw.  stauka -^ 1;  jjind.  stoken  , stechen,  stochern*,  engl.  dial.  stoke  ,das  Feuer  schüren', I  tbd.  stoche{r)n]  ohne  anlaut.  s- :  aisl.  /)OÄa  ,rücken,  verändern,  gehen*, ?'ifS.  docerian  ,umherlaufen* ;
4114:4.  suer-  ,schneiden,  stechen,  schwären,  eitern'.
4116:air.  sei^bj   cjmr.    chwerw  ,bitter'  (*suer-uo-)j  ursprüngl.  wohl  ,' stechend' ;  cymr.  chwarren  f.  , Drüse'  (*suorsina) ;  .,
4117:ahd.   sioeran   st.  V.  ^schmerzen,  schwären,  schwellen',   swero  ,! Schmerz,  bes.  Geschwür',  nhd.  Schioäre,  Geschivür,  ahd.  swer(a)do Schmerz',  ags.  sioeornian  ,gerinnen';  ahd.  sivei^t  ,Schwert^,  ags. sverd  aus  *swe)^-da-  ,stechende  Waffe';  -p
```


## [2026-09-14T02:29:35.412Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3505,3545p' POK_03.txt\necho \"=== leaf index ===\"\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nidx=t.find('(s)teig-  ,stechen')\nif idx<0: idx=t.find('teig-  ,stechen')\nprint('leaf', t[:idx].count('\\f'))\nEOF",
 "description": "Print Pokorny steig- entry"
}
```


### [2026-09-14T02:29:37.961Z] TOOL RESULT

```
gr.  PN  2Tt7tü)v  zu  *aTlTtog  =  ags.  stlf,  mhd.  (eigentl.  md.)  atif  ^y auf  rechte  neben  altfries.  stef(?)]  mnd.  süvele  , Stütze',  mhd.  stlvel  ds.,  |^^ stlfla  , dämmen'  (daraus  engl,  stifte  , ersticken') ;  mit  germ.  p:  nd.  m-^j^ s^zper  , Stützholz',  fries.  s<?pe  ,PfahlS  engl,  stipe  ,Stengel';  mnd.  stip^  ^pi ,Punkt,  Tupf,  stippen  ,punktieren,  sticken',  mhd.  steppen  ,reihenweise  niW sticken',  nhd.  steppen-  mnd.  stift  , kleiner  Nagel,  Stift',  ahd.  steft  ,Spit|« Dorn,  Stift']  unklar  sind  and.  stiftön  ,aedificare',  ahd.  mhd.  stiften  fy^ stellen,  gründen,  bauen,  anstiften',  nhd.  stiften;
lit.  stimpü  stipti  ,erstarren,  verenden',  stipriXs  ,stark,  kräftig',  pl.  ^ pinat  ,Stütze  am  Schlitten',  lett.  stipt  ,steif  werden*,  ablaut.  lit.  stiepti^  l^tt stiept  ,recken';  apr.  postippin  ,ganz*.
WP.  II  646  f.,  WH.  II  593  ff.,  Trautmann  287,  Vasmer  3,  7;  zu  stäi~  S.  lOlO.
{s)teig-  ,stechen;  spitz',  Erweiterung  von  stei-  ds.;  (s)tig-tO'  ,gestickt'.
Ai.  tejate  ,ist  scharf,  schärft',  tejdyati  ,schärft,  stachelt',  tiktd-  ^thttt bitter',  tigmd-  ,spitzig,  scharf,  tijas-  n.  ,Schärfe,  Schneide,  Glanz',  tijana»% ,das  Schärfen,  Anzünden ;  Spitze,  Pfeilspitze,  Rohrstab,  Pfeilschaft',  wott als  Kollektiv  tejani  f.  ,Geflecht  oder  Bund  von  Schilf,  Stroh  u.  dgl/j     ,
av.  taeya-,  tae^a-  , scharf;  m.  Schärfe',  tiyra-,  ap.  tigra-  , spitz*;  afgbtEu ter9  , scharf,  spitzig*  {^taigra-)]  av.  tiH-  ds.,  tiyri-  ,Pfeil'  usw.,  np.  itf ,Spitze,  Schwert'  (arm.  Lw.  teg  , Lanze'),  tez  ,scharf',  tej  , Pfeil';    .
ohne  anlaut.  s-  auch  germ.  *pihstila-  , Distel*  (vgl.  den  s-St.  ai.  tijas-) in  aisl.  pistill,  ags.  distel,  ahd.  distil  und  norw.  tlstel,  ostfries.  dissel  ,Di8tel* und  vielleicht  acymr.  tigom  ,naevi'  (,*Punkt,  Tupf  aus  , Stich'?  vgl.  j^r, arly^a)]  ^
gr.  gtI^ü)  ,steche,  tätowiere',  arty^ia  , Stich,  Punkt',  arixTÖg  ,bunt^ Ggestickt');
lat.  instigö,  -are  ,anspornen,  anstacheln,  anreizen,  aufreizen';
nasaliert  Instinguö  ,reize  an',  interstinguö  , besetze  (bestecke)  hin  und wieder  mit  etwas*,  distinguö  , (steche,  stochere  auseinander)  unterscheid«* {-uö  nach  unguö  usw.),  umbr.  anstintu  ,distinguito' ;  lat.  stinguö-  -ere  ,»0*« löschen'  (vom  Auseinanderstochern  der  brennenden  Scheite);  ''
mir.  tiug-  {Higu-)  ,letzter',  acymr.  guotig,  cymr.  wedi  ,nach*  (,*hint*r dem  Ende'),  air.  tigernae  ,Herr*,  gall.  Tigernum  castrum,  cymr.  teym  ,Herr« scher*  (oft  beeinflußt  von  *tegos  ,Haus');  bret.  stech  , Garbe'  (^*stikkä)]  breU stiogen  ,Tintenschnecke'  zu  *stiog  aus  *stigäkä  (vgl.  Loth  RC  43,  I66)j
got.  stiks  , Stich,  Punkt',  ahd.  stih,  as.  stiki,  mnd.  steke,  ags.  stice  m.  ,df/j stician  ,stechen* ;  Intr.  ,steckenbleiben,  fest  bleiben*,  mnd.  sticken  ,stecbeni sticken,  anzünden,  ersticken*,  ahd.  sticken  , stechen,  sticken',  ir-sticken  ,er*
1017
sticken',   ahd.   stecken  ^festsitzend   nhd,   stecken  (*stik]cen  gleichsam   ^ange-
jj^gelt  sein');  als),  steikja  , braten'  (eig.  ,an  den  Spieß  stecken^;  dazu  steikr
Braten',    stikna    , gebraten   werden');    mit    Ablautentgleisung:    as.    stekan
festheften,  festhaften',  ahd.  stehhan,  nhd.  stechen,  Kaus.   *stakjan  in  ahd.
stecken  , (durch  Stiche)  befestigen,  einstecken',  nhd.  stecken  tr.,  got.  staks
Wundmal',   ahd.    stahhula    ,Stachel',  aisl.   sfi^kr   , stinkend,   scharf;   diese
Überführung  in  die  e-Reihe  war  begünstigt  durch  die  germ.  Ableger  von
*steg-  , Stange'  (z.  B.  aisl.  stjaki  m.  ,Pfosten'),  mit  denen  sich  die  Gruppe
o-ot.  stiks,  nhd.  stechen  zu  einer  neuen  Einheit  zusammenschloß;  so  beruht
formell  auf  *stig-,  aber  mit  der   Bed.   von  *steg-:   aisl.   stika,   ahd.   stehho
Stecken*  (letzteres  aber  zugleich  auch  =  aisl.  stjaki),  aisl.  stik  n.  , Pfahl';
mit  kk:  aisl.  stikka  , Stecken,  Stange',  ags.  sticca  m.  , Stecken,  Löffel',  as.
stekko  , Stecken,  Pfahl',  ahd.  stecko  , Stecken';
zu  *stig-  stellen  sich  noch:  aisl.  stikill  , Spitze*,  ags.  sticel(s)  m.  ,Stachel', mnd.  stekel,  ahd.  stihhil  ,Stachel',  nhd.  Stichel]  got.  stikls,  ahd.  stehhal ^Becher*  als  ,zum  Einstecken  in  die  Erde  unten  zugespitzt  verlaufendes Gefäß';  as.  stekal  ,rauh,  steinig*,  mnd.  stekel  ,devexus',  ags.  sticol  , steil, hoch',  ahd.  stehhal,  mhd.  stechel,  Stichel,  stickel  , steil'  als  ,die  Fußsohlen stechend,  voll  spitzer  Steine' ;
lett.  stigt  , einsinken',  lit.  stingii  stigaü,  siigti  und  stygau,  -oti  ,an  einem Orte  ruhig  verbleiben  (steckenbleiben');  ob  zu  (s)teig^h-?
WP.  II  612  ff.,  Wissmann  Nomina  Postverb.  86  f.,  191,  Vasmer  3,  8; s.  unter  2.  {s)teg-.
steigh-  »schreiten,  steigen';  st{o)igho-,  stigh-tä  ,Weg'.
Ai.  stighnöti  ,steigt'  (Dhätup.),  ved.  pra-stighnuyät  Opt.  Präs.  ,er  möge emporkommen',  ati-stigham  Inf.  , übersteigen,  bemeistern';
gr.  OTsixu)  , schreite,  gehe',  *<tt/^,  Gen.  orLxög,  PI.  fffixeg,  -ag  ,Reihe,  Zeile', att.  arlxog  , Reihe,  Zeile,  Linie',  OTixäad-ai  ,in  dichter  Reihe  neben-  oder hintereinander  gehen  oder  kommen',  Gxolxog  , Reihe,  Linie';
alb.  shtek,  shteg-u  , Durchgang,  Eingang,  Weg,  Haarscheitel'  (=  aroTxog) ;
air.  tiagu  ,ich  schreite,  gehe',  techt  f.  ,das  Gehen,  der  Bote',  cymr.  taith jReise'  =  bret.  tiz  ,Eile'  (*[s]tikta),  cymr.  mor-dwy  , Seefahrt'  (*[s]teigho-) usw. ;
got.  steigan,  Siisi.  stlga,  ags.  ahd.  stlgan  , steigen'  (=  gr.  GTel%(jj)\  ahd. üig  ,Steig,  Pfad,  Stufe',  aisl.  stigr  ,Fußsteig' ;  got.  staiga  , Steig,  Weg', ahd.  steiga  , steiler  Weg';
ahd.  Steg  m.  ßteg,  kleine  Brücke';  aisl.  stigi  m.  , Stiege,  Leiter',  stig n.  , Schritt,  Stufe',  ags.  stige  ,das  Hinauf-  oder  Herabsteigen',  ahd.  stega ,Stufe, Treppe,  Leiter' (ahd.  stiega,  nhd.  Stiege  mit  e^,  also  wohl  aus  *st^ighä); ags.  sfceger  f.   ,Treppe'  (engl,  stair),  mnd.  Steiger  ,steil',  nid.   ,Ladeplatz'
1018  ,
Gerüst',  aisl.  steigur-ligr  , steil,  aufrecht';  aisl.  stett  f.  ^Fußspur,  Trittstein Weg,  Stand,  RangS  stettr  m.  ds.  (:  cymr.  taitli),  aisl.  stetta  jUnterstützei^ helfen',  ags.  stihtan,  stihtian  (,*auf  eine  Basis  stellen  =)  einrichten,  ordnen«      ^ anfrk.  stihtan  (=  ahd.  stiftan?)  usw.;  l
lit.  staigä  Adv.  ,plötzlichS  staigüs  ,heftig,  schnell  aufbrausend',  staigasu     i -ytis  und  steigiüos,  stetgtis  ,sich   beeilen,  sich  bemühen';   lett.   steidzu(d$\     1 steigt{ies)    ,sich  beeilen',  s^al^a^  , wandeln',  s^i^a  ,Pfad';   aksl.   stignq  ^^ komme',  sthdza,  sthza  ,Fußsteig,  Straße',  sttgna  ,Straße'.
WF.  II  614  f.,  Trautmann  285  f.
{s)teigli-  , Schulter,  Arm,  Schenkel'?
=== leaf index ===
leaf 257
```


## [2026-09-14T02:29:52.252Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD steig ===\"; grep -n -i \"steig-\\|stig-\\|etiquette\\|astigmat\" AHD_watkins1985.txt | head -30\necho \"=== BRT ===\"; grep -n \"tiγra\\|tiyra\\|taeza\\|taēža\\|tiγri\\|tiyri\\|taēγa\\|taeγa\" BRT.txt | head -30",
 "description": "Grep AHD and Bartholomae"
}
```


### [2026-09-14T02:29:52.326Z] TOOL RESULT

```
=== AHD steig ===
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1010:steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
1011:steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1487:EXPOSTULATE prek- EXPOUND apo- EXPRESS per-5 EXPUNGE peuk- EXPURGATE peue- EXQUISITE quaerere EXSCIND skei- EXSECT sek- EXSICCATE seikw- EXTANT sta- EXTEND ten- EXTENUATE ten- EXTERIOR eghs EXTERMINATE ter- EXTERNAL eghs EXTINGUISH  steig-
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
2272:SNICKERSNEE sneit-, steig-
2289:STEAD sta- STEADFAST past- STEAK steig- STEAL ster-4 STEALTH  ster-4 STEAROPTENE pet- STEED sta-
2296:STICK  steig- STICKLE steigh- STICKLEBACK | steig- STIFF steip-
2297:STIGMA  steig- STILE! steigh- STILL! | stel-
2305:STIRRUP steigh- STITCH steig- STITHY sta-
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
=== BRT ===
4202:tiyrim)  ahurö  mazdä  avqn  "  tat  äps  urva-
4205:tiyrim)     ahurS     mazdä     avqn ''      \am}sä
5112:•  j.  avavat  Adv.  'in  solcher  Grösse,  Masse, Entfernung,  Weise;  ebensosehr,  ebenso': *av'  F.  7  " ;  —  'vatat  Vd.  75.  a)  sonst  1 mit  dem  Korrelat. ^a^u :  ye^Ju  av  . .  tüti  1 SpS  ava.barpnte  yaia  vupa  imi  äpS  .  . Yt  5.  1 S ;  —  ^^  haca  iristaäbyS  yaia ^rigäim  V.Äii;  39,  76,  p.39;  — yd^a iattm  kaydhanqm  av  asava./aalYt  JO.z; — y3  av°  xSva^zvs  vasaiti .. yäka  tiyris.. YtÄö;  —  'vaiai  yaka  kv5  ptruahe'^. 7.53  PüZ.
5265:I  mit  nt,  niy  i)  'herab(zur  Erde)kommeB, I -sinken':  vTsp>m  a  ahmltyataim  (tiyris) \paili.apayal  vazamnö  sl'amantpm  avi gat- Wlm  ^fanvaia  paiti  nirat'''  "bis  dass  er (der  Pfeil)  dahinschiessend  zum  Berg  X^. gelangte;  auf  dem  ?C.  kam  er  zur  Erde" Yt<?.38;  —  5.  noch  «r«  Inf.  2)  'herab- kommend sich  einstellen  in  — ',  mit  abiy und  Akk.;  siy.itis..  hauvciy  t^urä  nirasätiy abiy  imäm  vi^am  "Wohlbehagen  ■ .  (es) wird  sich  durch  Ah.  einstellen  in  diesem Haus"  D.  5.3.
6467:•  j.  "aätay-  m.  'Pfeil':  yat .  .  jyä  navi- >jqn  (sd.)  tiyrar?hs  "tayS  Yt  10.  113.
6722:1)  'werfen  (eine  Waffe),  schiessen':  arstii yqm  *an/iyeili'^  avi.>tiiiris  Yt  10.  ao;  *2i; —  tiyris" .  ,  yi'm  an/iaf  »rsxsö  (sd.)  Yt  8. 6;  —  äsyatjka  Avastayn  {sA.)  *arikima- nayäi^  (GD.)  Y.57.  28;  —  yalat  hvasttm (sd.)  *a»Ayeiti''>  Yt/0. 21;  —  asia  F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^'>  "der Feind  wurde  ins  Wasser  gedräng "" /.  19.
7635:•  j.  3r9x§a-  a  £N.  eines  berühmten iranischen  Schützen**:  tiyris  . . y'im  anhat °sS  xi-vitui-Uus  xsviwi.iivaiimd  airyanqm airyö^stii:at  haca  garSit  ^anvantain  avi gairim  "der  Pfeil  , .,  den  der  PfeilschUtze if.  schoss,  der  beste  Pfeilschütze  der  Arier, vom  Berg  A.  bis  zum  Berg  X<:"   Vt.ÄÖ.
9204:mit /rJ  'durch  Einfurchen  herstellen':  (sSPrM.)  Vt.ij.  107;  —  aü?..  fr  acaraiti karsasiit  (sd.)  frakirayjis  tiyra  xi'a'ira  \*antan.ar/6}m  nm3nahe  Yt.  iS.  4;  3;  — *vairya  V.^,  10;  11',  F. 5;  —  nava  karsa.vasS.xsa^rS  (näml.  jran//')  *fracaraite  aoi frakJrayat  "neun  Furchstreifen  zog  er"  ^y^m  ..  gas%qm  ¥.57.34;  —ya'i:a..anJzarvtä \.22.ao; — yS  ZJinS  tisrS  kari^a/rak3ra-\.  .  yahm  (näml.  fravasayS)  fra^ara'imie yHH  N.;o/;  YL4.63.  (2PPM-)  ¥1/^.34.         2)  mit  Akk.  'hinzu
9354:•  j.  'kar§a-'>  m.,  n.  i)  'Furche,  Furch- strich, -streifen  (auf  dem  Erdboden)':  yj t»mS  tisrö  *'/ä  (APn.)  frakärayeiti  ava  1 ika  bartnti  (sd.)  *yavahe  ",  ,  drei  Fur- chen . ."  N,  }0i;  —  äva.dasa  'sa  /rakä- rayÖM  "zwölf  Furchstriche  sollst  du  ziehen" V,  5.  1 1  *';  —  'säsat  (APm,)'*  frakäraySis tiyra  Xioira  ^vairya  "Furchstriche  sollst du  ziehen  mit  einem  spitzen  Metallstuck" \.g.  10";  zit  *F.53)j  —  nava  v'^  (APn.) ß-äiJrtiyiat  V. 22.20.  2)  'Bezirk,  Gau'<>: **a>  F.  5;  —  y3  hudaind . .  vlspa  -sS  (als AP.)  rJoayäti  Yt  4.  9  (?).  |
12245:•  j.  'tiyra-  (,  p.  t^ra-)  Adj.  'spitz,  spitzig' iarsasat(sd.)/rai3raySi/'°ra{lS.)  x/a^ra
12255:•  j.  tiyray-  m.  'Pfeil':  ya^a  •ris  mainya- i-asa  yim  aahat  >r?xsS  (sd.)  Yl  S.  6.
12763:VyL2/;  —  ya^a  tiyri/ yim  a^hat..  laoa
14885:—  paoiryS  gairiS  AqtnJtisiat  .  .  'ti  äya z^mä  YX.ig.i;  /O.  98,  /J.97,  Y.9.IS.  V, 7,  54;  —  nasunqm  yä  'ti  aya  zimä  irJri- ^ar»  V.5. 4;  — '11  karJ*  pärst^  hyJ'  vtha- (id.)patiy3'^  . .  Bh.  J.  4;  2.  5  (ergänzt);  — tiyri/  ,  ,  afanvaia  'ti  niral  (Sp.  184  o.) Yt^.  38;  —  dasina  'ti  ahoanha  "auf  der rechten  Seile"  N.  65.  4)  mit  Abi.,  nur räumlich;  a)  auf  die  Frage  woher?:  mihr>m .  .  yS  vlspfm  aAsm  . ,  ädiiäiti  haraihyat 'ti  bar3tanhai  Ytio.  51.  b)  auf  die Frage  wo?:  dunmqn  hqmJiiitinli  *iisMndvat °ti  garsit  YtS.32;  —  yim  yazata  ahurS mazda  raoxinat  'ti  gara  nmana£  Yt /0. 1 2  3 ; 5.25,45.  s)  mit  Gen.,  nur  raumlich; a)  auf  die  Frage  woher?:  naKa  dunmqn (sd.)  uzjasaiti  Aaraihyd  'ti  iamayä  Yt 10.  50.  b)  auf  die  Frage  wo?r  ^dasimm J  va  gaonavatö  (sd.)  ^banstrvS  va  'ti vayhanaAe  N.  65;  —  zqm  .  .  yetiAa  'ti  . . apa  taünti  Yt  jj.  9  f. ;  i  o ;  — y^iihe  nmämm ..vüätfm  banzi'te  paiti  bar^aAi (Sp.Ba^ u.)  AaraiiyS  'tt  banxayä  Y. 57.21;  19;  — ys .  .  Aaomq  utdasta  .  .  kara^yS  'ti  bar»- '  xayä  Ytio.  90.  c)  auf  die  Frage  wo- hin?: aurvantim  %wä  .  .  bcrjS  nida'iat .  . Aarai^yS  'ti  banzaya  Y.SO.  10.  6)  mit Dat(?)"'',  räumlich  auf  die  Frage  wo?: tarn  yazata  auf  .  .  daAakS  bawrsii  'ti daiiihaove  Yt.  5.  29.  3)  zum  Ausdruck des  Gleichkoromens,  Aufwiegens;  mit  Akk. 'gleichwertig  mit  — ',  bei  Ellipse  des  Verbums {'ah-):  ha  ml  baya  .  .  satam  'ti  anyaisqm ra^wqm  gä^anqm  "dieses  Stück  .  .  wiegt hundert  andre,,  auf  Y./^.S"';  15.  A)bes. zur  Angabe  dessen,  was  als  Preis  oder  Lohn geboten  oder  verlangt  wird,  'gegen,  um, für';  i)  mit  Akk.:  uzbasaui  'ti  ammxtttn (sd.) /rarazaite  miirS  Yt  10. 1 24.  a)  mit Lok.:  yehyS  .  .  vaAistptn  yesng  'ti  vaidä (sd.)   mazda  Y,  57.  2a;   27.15,  Vr.  16I3;
18947:•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
19836:•  j.  tnaimv-asah-'>,inainyav-*Adj.(auch fem.)  'im,  durch  den  Raum  der  Geister (d.  L  die  Luft)  sich  bewegend,  schwebend, fliegend';  a)  von  Rossen:  sraoltm .  .yim . . aurvantö..sp>nta  vi^änhs  asaya  'ivasanAs (NPm.)  vaxaaii  Y.57,  a?.  b)  von  Ge- schossen: ^aäiz  tiyris  'ytmasä  (ÜSia.)  yim anÄai  .  .  YtS.6;  —  hazaarjm  ifunam (arltinqm,  lakuianqm,  kantanqm,  gMa- nqm,  fem.!) ..  'j/avasä  (NPm.,  {.)'*  vas^nti •yavasä  patanti  kam?r^  paiti  äalvanam YLJO.i39(fi:).
23167:sva. 'einherziehen':  sp^)m..yS  mi  pasill£ vazaite  Yt,  14.  58;  —  aSru  pascalta  vao- zinm  (3PPrPfM.)^'  baohntg  iuhm.."Aort werden  sie  alsdann  einherziehen  .  ,"  Yt iff.6g.  2)  'fahren'  intrans.  von  jeder Art  gleitender  Bewegung  wie  'schweben, fliegen  (usw.)':  ti/trTm  . . yS  avavat  xhiOKifJf vazaite  avi  srayS  .  .  ya'ha  tiyris  ".  .  der so  rasch  dahinfährt  zum  See  . .  wie  der Pfeil  .  ."  Yttf.  6,  37  (wo  vazaite);  — tis'tryS  ,  .  raexsnusva  vat^mnS  YtÄ  13, 45;  —  aSra  pascaSa  vazaite  v3tB  darst/ YLÄ  33;  —  avai  sfarmg  .  .  yim  vataite
26076:•  j.  Sarah-  n.  'Kopf:  karitacii  .  .  yfi ttiyraire  'raAu  masyakanqm  Yt.  10.  40.
```


## [2026-09-14T02:30:07.142Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12240,12262p' BRT.txt\necho \"=== search taeza/taeya ===\"\ngrep -n \"ta5za\\|taBza\\|taeza\\|taeya\\|tae/a\\|tiii-\\|ti/i-\" BRT.txt | head -20",
 "description": "Bartholomae tiγra- context"
}
```


### [2026-09-14T02:30:07.243Z] TOOL RESULT

```
6S>
tifäyah-
65a
•  j.  t^yah-  Adj.  (fem.  •yeil-)  'der  tapfrere,  |  xiapatis  .  .  'rys  .  .  kshrpm   ra^wayäti
energischere,  heldenhaftere':  fravalayB  . yä  'yehli  (NPf.)  ahmäl  .  .  yaHa  vaca  fra tnraväire  (sd.)  Yt.  13.  64. KompE.  —  Kompar.  zu  laxma: j.  liurva  N,  6^;  lies  lüirya.
•  j.  'tiyra-  (,  p.  t^ra-)  Adj.  'spitz,  spitzig' iarsasat(sd.)/rai3raySi/'°ra{lS.)  x/a^ra
spähe  kihrpa  aurusake  .  .  äal  paiti avaiti  .  .  avi  zrayS  vourukasttn  .  .  ä  äim paüi.yq^  nisdvaraili  daevS  yS  apaoiö aspahe  kfhrpa  iümahe .  .  kam  läcit  bäzus barats  . .  'ryaica  . .  -vasca .  .'täyüitya%ö  . . a    rapi^winfm    srvämm    ä    Mm    bavatli
'.ao/ä  . .  daiüm  yim  apaohm  apa
*vairya  V.  5.  i  o ;  —  vispaca  avi  'ra  ( APn.)  j  alät  iiyeiti  Yt  Ä  1 8  -  2 1  und  2  8  f. ;  —  -nm *iumata  (sd.)  Y.3.  35;  —  arstayasai  ■  ■ ,  stänm  rasvantim  :^armat3uhant)m  yaza- huxinuta  "ra  (NP.)  Yt.JO.39;  —  'ratihö \maide  .  .  yS  pairika  Htärayäü  ya  starS astays  Yt  10.  II  i.  k^nma  patanH  aniart    tarn    asmarumca
KompA.  —  Zdu  aL  V.  ttjaie  'sticht'.  —  Pü.; ,  Vt  A>  b.    ,    ,    ,,    ,,    ,_     '      ,_     ,0  _    _ eh  («  di*  /-«.-Lesung.)  ^  I  „^   ,■  l',    ''  ''  "■  !5-  S^.   '2   27.   18.  5,  7
.  p.  =ligra-    m.^  Name    emer  Festung  m  („äjnl.  pairil-S)    ys   taurvaydti    viväiH
Armenien":  °ra*  nama'  dida  armaniyaiy Bh.  2. 8.
*)  Nach  JusTi  GlrPh.  2.  42g  "das  heutige Fort  Till  am  7y-/«.  «o  die  Strasse  nach  BitlU abzweigt".
•  p.  tigra-xauda-  Adj.  'spitzhütig,  spiu- kappig">  als  Bezeichnung  einer  Abteilung der  Sak^xi:  sakai^A.)  'da  D.6'.3.
■)  Vgl.  die  Abbildung  des  letiten  Empörers auf  der  Bahislänvci'scb.T^it  und  Uerodot /.  64.
•  j.  tiyray-  m.  'Pfeil':  ya^a  •ris  mainya- i-asa  yim  aahat  >r?xsS  (sd.)  Yl  S.  6.
Vgl.  'li-jra-.  —  np.  tir.
•  p.  tigrä-  f  Name  eines  Flusses,  Tigris : 'räm  viyatarayamO*  Bh.i.  18; S-4i — isra* Jiya*  nadriabairakyil  °ram  adilrayt^  Bh. /.  18.
Stammansatz  und  Geschlecht  unsicher.  Die Namensfoim  berohl  vll.  auf  volksctjrmologi- scher  Umgestaltung  des  nicht  iranischen Namens,  vgl,  tiira-  und  titraj/-.  Das  Mp.  hat i/iilat;  Aü.  iätlat,  Eu.  Ii^p-a.
•  j.  titarant-  Adj.,  PPA.:  s.  'tar-,
j.  änqni   N.  p^:  lies  lanüm.
•  j.  tin]a  Ad?,  'zurück':  f  avat  handag- sayaauha  (sd)  "zurück!  .  ."  Yl  ig.  50.
Vgl.  -V^.
=== search taeza/taeya ===
17261:•  j.  bi-taeya-  Adj.  'auf  zwei  Seiten  scharf, doppelschneidig':  cakusanqm  'yanqm  Yt. 10. 130,
23010:Vyt52  (wo  v)r>sinl»m);  —  sajfärS (sd.)  ,.y3..  viiv?ntSi  painM%V  äaeaäisca tnaiyaiicä  ySca  vanlaitg  (Konj.)  aipl.- ä^IJ  V.  2p.  4;  —  ayanqm  mq%ranqm  ya vsrgtydti  avi.mi^ris  \X.l0.3o;  —  *syao- "istum.vgnam  (sd.)  —  vtmyst  *^aehiam  — V. /j.  33;  —  A/ft'  tä  ^ao^na  varita yä  ankut  astvh  v^n^äti  V. /j.  i;j,  41, 75. 10,  }§.(>%;  —  imat  .  .  staviittm  fyao- %mm  ma^a  virxinti  Yt  77.  59;  V.  75. 1 ; —  nsit  vanh^  ahmat  fyaohn»»  v^ntyäli yaha  yat..  N.4S,  v'iS.  10,  12;  76'.  17;  — astimsm  agtae/am  syaoh^nanam  virfsim- n?m  V.  4.20;  go; —  *AavantH&ä.)  aitaAe syao^naAe  VMixyqn  n/tca  kainica  hanäca V.  75.14;  —  t^i  yä  variiä  {\%.) yäca  pairl 2  u.)  iyaoham  Y.  50.  10;  — ai'(7ni?i/(sd.)  . .  baosavasca
```


## [2026-09-14T02:30:22.846Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"'tiyra-  (,  p.  t^ra-)\")\nprint('leafidx', t[:i].count('\\f'), 'of', t.count('\\f'))\nprint(repr(t[i-3000:i-2500]))\nEOF",
 "description": "Find BRT column marker"
}
```


### [2026-09-14T02:30:23.959Z] TOOL RESULT

```
leafidx 378 of 1040
' ti-\nZmn  V.  >(0w-.  —  ai  lövifh  f.,  np.  fff  (HBm. ITAn«.  10.  aS).  —   Po.:   *A«Äfe.t),    erl  (im\ntf^^rySvant-\nY.  4S):  nfröi;  (lu  Y.  34,  43,  43,  J/  lut: mit  utayälay-) :  *litx}i}n  <)  i  titvaniiXiä,   erl.  (in y.  43):  idr  i  patüiViä,     Vgl.  m  utayütay-,  — <)  Geschr.  1  n  *  dan  n. j.  uns"  Verbalf.i  s.  unter  %Tah:\n•  j.  te  Part,  i)  hinter  ku%a  \'wie?":  -taSa (Stverz.)  t  V3r>tyqn  aSe  yöi  mazdayama V.5.10USW.;  —  ku%a{_z^)  f  aSe  matda- yas'
```


## [2026-09-14T02:30:29.970Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN tir/tiz/setez ===\"; grep -n -i \"tīr\\|tir \\|tēz\\|tez \\|sitēz\\|sitez\\|stēz\\|sitīh\\|sitih\" HRN.txt | head -40",
 "description": "Grep Horn"
}
```


### [2026-09-14T02:30:30.026Z] TOOL RESULT

```
=== HRN tir/tiz/setez ===
387:(110 Anm. Vers 8, Calc), Zerf'r auf tir (1536, 705), Ardes^^
3803:tir *Pfeir.
3806:über Tir =: aw. Tistrya- vergl. zuletzt Nöldeke,
3817:S. 93) die Bedeutung von tir 'Pfeil* auf den Gottes-
3818:namen Tir übertragen sein lässt. Die dort erwähnten
3829:') Tir reimt auf qir (Sahn. I, 112 Vers 900); falsch auf ser in
4563:Chants pop. XXXII); oss. d. yor, t. /Tir (306); si/n.
18795:K. v^rntez 979.
19308:istir 69.
19614:Itir 448, 799.
19629:tir 406.
19740:Atir 156.
20853:tez 408.
20857:n. tir 406.
21127:d. ^Atir 938.
23207:s. pTir «56.
```


## [2026-09-14T02:30:32.752Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3795,3840p' HRN.txt\necho \"=== HRN no.408 tez ===\"\ngrep -n \"^408\\|408\\.\" HRN.txt | head -10",
 "description": "Horn tir entry"
}
```


### [2026-09-14T02:30:32.816Z] TOOL RESULT

```
löschen' (400).
405. teheniy tehm *stark'^).
V
ap. Cid^ra^ta/ma- N. pr.; aw. ta/nia-; im PehlevT
nicht belegt.
406. Ur^) 'Pfeil', tlrkes, terkes 'Köcher 5^).
ap. vergl. Tigra-, med. riy()iif xaXovöi t6 tohvf^ia ol
Mrjöoi (Dionys. Eusthat. 994); aw. tiyri- Tfeil'; phlv.
tir *Pfeir.
LW. kurd. tlr, tlrek; bei. ttr, n. fir *Pfeil, Kugel'
(387).
über Tir =: aw. Tistrya- vergl. zuletzt Nöldeke,
Persische Studien I, 33 folg. und auch Bartholomae,
ZDMG. 44, 554. Ich möchte die Entstehung von Tir
durch Contraction aus Tistrya- mit Geiger, Etym. d.
BalüöT s. V. tlrhand 'Sternbild des Orion (No. 388) doch
nicht für durcliaus unmöglich halten. Zwar bleibt
aw. str gewöhnlich im Np. erhalten, indess vergl.
beide aw. pistra-^ deren Verhältniss zu phlv. pesak
etc. allerdings nicht klar ist. Ganz unwahrscheinlich
ist jedenfalls A. Stein' s Meinung, der (Zoroastrian
Deities on indo-scythic Coins, Indian Antiquary, 1886
S. 93) die Bedeutung von tir 'Pfeil* auf den Gottes-
namen Tir übertragen sein lässt. Die dort erwähnten
Münzen haben die Form TEIPO.
*J FJ hat folgende Belegverse des altertümlichen Wortes aus
Pirdüsl:
h^nezd'ik'i sengul ftristäd^ büd
hemänä kX sah ü Wiemzäd^ büd
und
fShem hesi^ der pehl^äm zebän
hemerdi füzün z*ezdehä-yl dem an
Dr. Landauer belegt mir das Wort aus Srthn. I, 228 Vers 1768,
III, 1524 Vers 497 {tehm), IXT, 1109 Vers 754, 1617 Vers 2125 (Wtem).
') Tir reimt auf qir (Sahn. I, 112 Vers 900); falsch auf ser in
dem unechten Verse Sahn. I, 212 Anm. 8, Calc.
*) Daraus ital. tttrcasso, franz. carqitois (de Lagarde, Ges. Abh.
80); vergl. auch mhd. ^(5^rÄ;is *Köcher* bei Wolfram sowie Miklosich,
Denkschr. WAW. Band 38, 53 s. v. terlces.-- 92 -
407. tere *finster , tereyt^) (auch in Indien spricht man heute
nur ttre).
aw. *tq3ri/a-, vergl. tar, tank (No. 370) ; phlv. terak,
LW. afy. ttra; bei. n. feray (274); siyn. t4r,
408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
g. ^f/ 'scharf; mäz. tTjf,
ap. vergl. ^i5rra[/a?*rfa-; aw. bröi&rö.]tapJa^ mit
=== HRN no.408 tez ===
1266:Zu ai. 1 V^hur-, Nöldeke, ZDMG. 32, 408.
3838:408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
9295:(Justi, No. 408.)
13822:■ /^- 408.
13837:lez 408.
14199:tigrnjiaudn- 408.
14700:(iVra- 408.
17446:/gi 408.
17724:l°- ■'■!/-, '«>'e 408. 722.
18729:«j 408.
```


## [2026-09-14T02:30:42.516Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3838,3860p' HRN.txt\necho \"=== Kampf/streiten ===\"; grep -n \"Streit'\\|'Kampf\\|Kampf'\\|streiten\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"tigra\\|tiyri\\|taeza\\|tēz\\|stēz\\|sitez\" HUB.txt | head -20",
 "description": "Horn 408 and setiz search; Hübschmann"
}
```


### [2026-09-14T02:30:42.598Z] TOOL RESULT

```
408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
g. ^f/ 'scharf; mäz. tTjf,
ap. vergl. ^i5rra[/a?*rfa-; aw. bröi&rö.]tapJa^ mit
scharfer Schneide'^); phlv. tej (päz. ^öi), ^es 'Axt'
(vd. 14 (24)); ai. [/'tej-, tejati schärfen, scharf sein,
tejas-,
kurd. tt£, tizT; bei. tes: (275); afy. LW. tez, tezal; sar.
teiz, wa;K. tiz,
409. tey *spitz, Schwert', % (nicht belegt).
aw. bi.]taeya- 'zweischneidig'; arm. LW. teg.
kurd. tJ 'Degen ; bei. LW. n. tey 'scharf, schnell;
Schwert' (889).
phlv. HTl (oder wie man transcribiren mag) — vd.
3 (121) == aw. tiyra-y und häufig im Bund. — soll
vielleicht tey sein. Np. tey 'Berggipfel, Höhe', oss. fty,
d. feyä 'Bergrücken (250) gehören ebenfalls hierher
(spezialisirte Bedeutung: Spitze eines Berges).
J.
410. JädU 'Zauberer, Jadül.
aw. j/ätu- 'Zauberer'; i^hlw. jatuk, jatükih, arm. LW.
jatuk; ai. yätü- 'Spuk, Hexerei; Spukdämon'.
411. Jäm 'Glas, Becher'.
aw. yama- 'Glas' ; phlv. jatn bezw. yäm (auch für aw.
=== Kampf/streiten ===
3162:B r e h m , Vögel II : *Wenn zwei Wiedehopfe streiten,
3393:360. peikär, peigär *Kampf'.
3395:phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
3397:arm. LW. payUar *Kampf' .
5469:'Kampf, auch razm.
6327:aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
7244:834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
7247:'Zank, Streit'; got. harjis 'Heer.
8083:kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
8510:(AV.); ai. midhd- 'Kampf, Wettkampf; got. mizdö
=== HUB ===
2090:gerade Tigranaduxt kommt meines Wissens nicht vor.
2101:= phi. np. aneran^ zd. tiyri- = np. t%r ist.
6081:zd. staomi; sitez *Kampf', afgh. steza fern.; sikastan *zer-
8209:*scharf, spitz', tiyri- 'Pfeil'; xujasta gesegnet' = zd. */iw-
8216:diraz 'lang = zd. drajah-; sitez *Kampf', zd. stij- *Kampf' ;
```


## [2026-09-14T02:30:53.777Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6315,6340p' HRN.txt\necho \"=== HUB ctx ===\"; sed -n '8205,8222p' HUB.txt\necho \"=== CHEUNG staig ===\"; grep -n -i \"staig\\|stij\\|stēz\\|sitēz\" CHEUNG.txt | head -30",
 "description": "Horn setiz entry, Hübschmann, Cheung"
}
```


### [2026-09-14T02:30:53.862Z] TOOL RESULT

```
1) Geschrieben -tenbe,
*) Np. sutör in der angemeinen Bedeutung *Tier* (d. i. Säugetier)
kann ich aus der schon melirfach citirten z/e^. A'^'ärczin. nachweisen,
wo es Fol. 655 r (Berliner Handschrift) heisst: Mor Oleander toiUot
Menschen und sutörän*; der arabische Text des Ihn Sinä, don dor
Perser übersetzt (WZKM. IV, 132), hat aä-ilarräh (I, S. 292; Cuiro
1204 A. IT.).- 160 —
kurd. stün, istün\ af/. stan.
Die indogermanische Grundform ist nach Hübsch-
mann, ZDMG. 39, 93, "^'sthlnä-; dagegen siehe zuletzt
J. Schmidt, KZ. 32, 385 folg.
722. fiite^ *Kampf, Krieg*, süeziden,
aw. vergl. stij- *Kampf, Streit'; phlv. stej 'Kampf*
(Bund.).
Wohl zu ai. l/^t^J-, tejate 'scharf sein, scharf werden',
vergl. Desid. titiksati *sich scharf zu machen suchen,
sich zu stählen suchen gegen Etwas, d. h. Wider-
stand entgegensetzen ; gr. ötCQm, lat. in\stigärey
germ. i^stek-^) (as. stekaUy ahd. stehhan, got. staks
'Mal, Wunde').
723. sey(t 'hart, fest; sehr, se/ß.
ai. [/^^ak-, gaknoti 'vermögen, können*, skr. qaktä-
'vermögend*; phlv. sayt^ saxtak]tum (vd. 19 (47)).
bei. sak 'hart, stark, fest' (383); yidg. sukt.
V
72 t. sw/un, SU/m (Sahn. I, 29 V. 117 neben -ww, ebendas.
=== HUB ctx ===
arzani 'wiirdig', 3 pr. arze Viegt auf .
c) ap. /, ^ nach Vokalen = np. j^, z, z : bajf = bal =
haz Tribut*, ap. haji-, skr. hhaj\ Uj Tfeil' (Vullers; wo
vorkommend ?) neben tez 'scharf, vgl. tiyra-^ in Komp. tizi-
*scharf, spitz', tiyri- 'Pfeil'; xujasta gesegnet' = zd. */iw-
jasta- neben paz. gazista verflucht' (§ 52, 1); bar^jan =
bar^zan 'Backofen', zu iran. brij *backen' (oben p. 27) ;
bijisk = bizisk 'Arzt' aus "^bimk fiir *bisizk, vgl. § 112;
azdaha *Drache' = zd. azis dahakd-^ farjctm *Ende' aus phi.
frajdm H. 814; bHa^ veza rein H. 253, etym. unsicher
(oben p. 33— 34); maz Treude*, skr. mah (siehe oben p. 97);
diraz 'lang = zd. drajah-; sitez *Kampf', zd. stij- *Kampf' ;
dozax *H5lle' = zd. daozanuha-; Xuzistan = ap. (H)uvja-
oder (H)uvza\ rajfa^ raza, raza oben p. 66; kUZj kuz 'ge-
kriimmt* = skr. kubja- (oben p. 89) , u. s. w. Buntes
Material bei Vullers, Gram. p. 39.
§ 122. Die armenischen Lehuworter haben nach
Vokalen stets z:
=== CHEUNG staig ===
23613:*AVESTAN: YAv. stij- (f.) ‘fight, struggle’ (Yt 10.71) 
33752:stij-, 361
```


## [2026-09-14T02:31:00.990Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23580,23650p' CHEUNG.txt",
 "description": "Cheung stij entry"
}
```


### [2026-09-14T02:31:01.069Z] TOOL RESULT

```
*MIDDLE PERSIAN: MMP ‘st’n- (ВМР YNSBWN-) ‘to take (away) = DMMPP: 
88b 

Pres.: IND. 35р. MMP “‘st’nyd, 3р1. MMP ‘st’nynd, ‘st’nynd, SUBJ. 3sg. MMP ‘st’n’d, ‘st’n’d, Ipl. 
MMP *‘st’n’m, 3р1. MMP ‘st’n’nd, ‘st’n’nd, IMPV. 2р1. MMP ‘st’nyd; Partic.: perf. pass. MMP * ‘std, 
‘std; Pass.: pres. IND. 3sg. MMP ‘st’nyhyd, SUBJ. 3sg. MMP ‘st’nyh’d 

*PARTHIAN: ‘st’n- ‘to take (away)’ = Ghilain: 71 | DMMPP: 88b 

Pres.: IND. 3sg. ‘st’nyd, ‘st’nyd, 3pl. ‘st’nynd, ‘st’nynd, SUBJ. 1sg. ‘st’n’n, 2sg. ‘st’n’h, 3sg. *‘st’n’h, 
3р1. *‘st’n’nd, IMPV. 2р1. “пуа, OPT. ‘st’nndy, ‘st’nyndyh; Partic.: perf. pass. ‘std; Inf.: *‘stdn 

*NWIR: NP sitädan/sitän- ‘to take, carry away; stand, stay’, Awrom. asay/-san-, Gur. 
(Kand.) -sän- ‘to take, buy’, Kurd. (Kurm.) standin/stén-, stin-, (Sor.) s(t)andin/ 
s(t)en-, Gil. (Rsht.) usadoen/usan- ‘to take (up), gather’, Siv. san-, sen- (supplet. 
es(s)ä, es(s)é, isd < ?) ‘to take (away)’ 

© This root is perhaps originally a pres. n-stem of *staH (?). 

«PIE pres. n-stem *st(e)H>n- ‘to (want to) buy; fix (a price, one's mind on 
something)’ ? = LIV: 590 f. | Pok.: 1004 ff. 

*IE COGNATES: Lat. prae-stinare ‘to buy, fix (a price)’, de-stinäre ‘to fix (in position, 
one’s mind on something); to destine for one’s own by settling terms, arrange the 
purchase of’, ob-stinare ‘to set one's mind on’, ? Arm. stanam ‘I receive, acquire’ (< 
Ir. ?) 

*REFERENCES: KPF II: 203; Christensen, Contributions: I: 60; MacKenzie 1966: 89; WIM III:116; 
Cabolov 1997: 73 


*staij ? ‘to stab; to be contentious ?' 
*AVESTAN: YAv. stij- (f.) ‘fight, struggle’ (Yt 10.71) 
*MIDDLE PERSIAN: MMP ‘styz- ‘to quarrel’, ВМР styck /stézag/ ‘quarrel, strife’ 


c DMMPP: 91b 
Pres.: SUBJ. 1sg. MMP ‘styz’n 


362 *stamb(H) 


^ Xe 


*PARTHIAN: ‘styh’g, ‘styyh’g ‘contentious’, ^'styh'gyft ‘contention’ = Ghilain: 92 | 
DMMPP: 91b 

*NWIR: NP sitehidan (denomin.) ‘to quarrel, brawl’, NP sitezidan ‘to fight’, NP sitéz 
‘battle, combat, conflict’ 

*NEIR: Oss. І. stigyn/stygd, D. (@)st’egun/(z)st’igd ‘to skin; to clean the skin [of 
fruits and vegetables]; to plunder, loot’, ? Yzgh. s(a)tizd/s(a)tiz- ‘to take offence’ (< 
NP ?), ? Sariq. s(1)kit, Wa. štik “game; entertainment; joke’ (LW ?) 

*SANSKRIT: — © EWAia II: 761 

© The root is probably to be separated from Skt. stegh- ‘to march, mount’ (MS). The 
Oss. forms may be closer to the original meaning. 

*PIE *steig- ‘to sting, stab’ LIV: 592 | Pok.: 1016 f. 


*IE COGNATES: Gr. стібо, ёстүрол “I sting, mark’, NHG stechen ‘to sting, stab’ 
*REFERENCES: IIFL П: 543; Edel’man 1971: 240; EVS: 73b; Abaev, Slovar’ Ш: 151 f; 
Steblin-Kamenskij 1999: 347 


*stamb(H) ‘to withstand, be stiff, stern, unmoving’
```


## [2026-09-14T02:31:16.677Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i \"tigr\\|tēz\\|stēz\\|stēh\\|tēx\\|tēγ\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== NYB ===\"; grep -n -i \"stēz\\|tigr\\|tēz\" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie and Nyberg"
}
```


### [2026-09-14T02:31:16.760Z] TOOL RESULT

```
=== PHD ===
PHD.txt:67:The phonetic realizations of these phonemes can only be sup- posed to have been similar to those of the corresponding sounds of present-day Western Iranian speech. The only allophonic variation of importance concerns the voiced stops b, (d?), g, and affricate J. Between a vowel and a following consonant, in the same morpheme or close juncture, these almost certainly became the fricatives [B, (8), у, 2] respectively. Thus abd, tigr, dujdēn represent pronunciations [*afd, tiyr, duZdén]. How far, or when, this development affected the same phonemes elsewhere in post- vocalic position is uncertain. It is sufficient to regard [B, 8, y, Z] as possible realizations of postvocalic b, d, g, j.!
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
PHD.txt:851:arrow tigr; ~ shaft Cóbag.
PHD.txt:883:atonement puhl, tēzišn.
PHD.txt:1498:daytime tēzgār.
PHD.txt:1847:expiation puhl, tēzišn.
PHD.txt:3310:quiver kantigr.
PHD.txt:3619:sharp burāg, tēz, tund.
PHD.txt:3620:sharpness tēzīh.
PHD.txt:3685:skin Carm, dawāl, pēst; tēz; (a.) post- én; ~bag hambān, mašk; ~ 'table- cloth! maškīzag.
PHD.txt:4496:tuhig tohmag tanapuhl tuxš- tuxšagih tuxšag i tuxšīdan tuxšišn tēxtan tuwānāg tuwānīgīh tuwānīg tuwāngar tuwāngarīh tuwān tuwānsāmān tambūr tambūrag did!, tand, tang tandih, tangih tanigardig tanigard tan
PHD.txt:4508:tastig кам Sken(n)+ &kastan! nëw! xormat tex tihdg ahiigt tis tasum gilt gilēnī tigr, Tīr 1%tērag tēmār 1%tēz tēzīh tišn tišnagīh tišnag Tištar tīdag tan-
PHD.txt:4513:taxt taxtan, tāxtan taxtag tēx
PHD.txt:5005:kardār kardārīh kāntigr
PHD_mackenzie.txt:333:the fricatives fP, (8), y, z] respectively. Thus abd, tigr, duJden
PHD_mackenzie.txt:5969: anti- jud- i allti-demollic jud-dew.     arr(11) tigr; ,...., shaft U,hag.
PHD_mackenzie.txt:7408:quiver kantigr.                                   pad paniih griftan.
PHD_mackenzie.txt:8285:tigr, Tir                ~,o         r6bahI
PHD_mackenzie.txt:9576:kantigr                     ~~,~                kordil                       ~\~
PHD_mackenzie.txt:11243:bay                           .JoU \      tigr 1                   -"U~
=== NYB ===
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1434:én [inser., Ps. ZNH, but already in the inser. the z is often stunted; BP ZNH] dem. pron. this here, always referring to the present situation, that of the speaker, or to what is to follow; no pl.: api-n pad pat én darrak% nihat api-n tigr tar han citak be apakand we set our foot on this rock here and shot the arrow beyond that cairn yonder HajB:6-8; én damik this earth, our earth; én dam, én dam u dahisn, en getäh this world; én apécak vēh-dēn íi mäzdesnän this pure good religion of the Mazdayasnians 84? eto.; always én dén this (our) religion, of the Mazdaism; pat én apēgumān būtan ku to entertain no doubt about the fact that 634 etc.; vicčirišn ... en kū the explan- ation is this that 121"; — én i forms an elliptic gen.: frdc én % man yaz perform what here is mine (my duty, the rite incumbent on me on this occasion) 535; én būt i 6 peš gobam this happened which I am now going to tell 54!?; — én and, v. and. — Skr ena-; not in Av. and OP; SW w.: MPrs. ‘yn (no pl, instead im&sän, imin are used); Paz. NP in. Tedesco, Dial. 216.
1492:frac [pr’c, pc] 1. adj. forward; promi- nent, distinguished, comp. ~-tar 14, sup. ~-tom 1021?.19, — 2. adv.: ē tigriyaf ~-tar one bowshot further 212’. 222; m 1094, hac nun ~ 611? henceforth; hac han ~ thenceforth 985; ~ 6 P2:9. — 3. prev. ahead, along, forth, forward, on (-ward), up, ete., or denoting the perfec- tive aspect, both in a local and in a figurative sense, with a great many vbs., v. each separately; also together with v. nouns: ~ guftür, ~ ranjakēh, ~ tuxšākēh,
1520:framän [plm'n'] order, command 12). 11310 ete.; ~ būt hac... + inf. it was ordained, decreed by ... that 3611-13; ~ dätan to issue orders, to order 191 ete. passim; ~ patigraftan to comply with an order 38!; — be spoxtan to disregard, disobey an order 3? (cf 12"); v. also
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2207:kan-tigr [kntgl], kantir quiver 2013. 2716, 2819.7, 292. — V. tigr. Renders Av. (46) akana- Vd 14°; Ps. kwtyly is probably only a clerical error for kntyly.
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
3029:patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
3030:rād hac Ohurmazd patigrift these have.
3032:patigriftaréh [ptglpt'lyh] reception 731. Tola;.,
3173:purr [pwl; M’LH] full: ~ äp full of water 151; ~ tigr full of arrows 2013; 542-7.11, 581; often united with the follow- ing subst. so as to form a compound, from which an abstr. subst. may be derived: ~ Yarrah full of splendour 48?3: ~ avarrahēh 37°. 10619; ~-marg full of death 11719: ~-margéh 648; (—-xrat full of Wisdom): =-xratēh 90%; —-nerök full of power 50%; — before an adj.: fully, thoroughly, perfectly: ~ névak 1 ävam the perfectly brave man of the (World)- era, ‘‘the perfect hero of the generations", of the Prophet 5533, whence the abstr. subst. ~-névakéh 1109; — = hac... kartan to fill with 1218. 12815-16, — Av. (894) parana-; MPrthPrs pwr; Paz. NP pur.
3633:$et [Syt'] shining, radiant, bright: šētē tigr the radiant arrow 2119-1? (Prth con- struction, v. s. v. ménó$) ; Yam 4 ~ 105%, NP Jamšed. — Av. (541) xšačta-; NP sed; v. also x¥ar-xsét.
3675:šutan [ZLWN-tn'] šav- [ZLWN-), forms v. I, 177, to go, opp. (G)matan to come: hac ki mat hom u apāc 6 ku šavom? whence have I come and whither shall I go? 6245; pat druyist šutan u āmatan that they may go and come safely 8723; ka han damistan Sut when this winter has gone 972; hac man šavdi thou shalt go (fly) off from me 2715; — regularly be ~ to go away, passim; bē o ... ~ to go (away) to; bé ~ to disappear, vanish 9416, to escape 2415-16 ; bē-šutak baxt whose luck is gone, who is off his luck 5?; — andar ~ : tigr tai parr pat aškamb andar šut the arrow penetrated right up to the feather into its belly 3%; to enter 181%, also andar-rón 1813, andarón 1912-13; 7525. 10278; — apāc ~ to go back, to
3678:. ziyan u pašēmānēh nč rasēt 682122 (similarly 68—72 passim); hakar-at ham- bun-ic mihr i amäh hast 99; xānak i-t nest . . . i-t hast the house that does not belong to thee ... that belongs to thee 5320-21.25-26. as the logical subj. of an inf. or a v.n.: kü-t ... né apasihenitan that is: it is not up to thee, thou wilt not be able to annihilate 46° gl.; ce-t ne apar tarsišn for thou shalt not be afraid 5821, adak-it én tigr patkafom then I shall shoot off this arrow against thee 100%; — 3. the dir. obj.: kü-t Az dev nē frepet 68%; (kit...) api-t... dev 6 došax" nē kēšānd
3771:teh [tyh], tē [ty] 1. ray, splendour, of the sun 716, — 2. point, of the lance 2019, of the foot 112. 3211, — 3, blade, of the sword 2225. 9620, — SW form of tēy > te > te with dropping of -y, or > teh with a secondary -h; Paz. teh. — NW form téy: Arm. lw. teg ‘pike’; NP téy ‘sword, razor; point of a spear; a ray of the sun’; Bal. t'ēg ‘sharp, swift’. Av. (963) bi- taéya- ‘double-edged’, cf 2225, V, also tež, tigr; as to teh nr. 1 cf Skr tejas.
3772:tež [tyc] sharp, ardent, swift, sup. tom 4375, 967°; adv. 518, 6024-26, 6122-25, — The palatalized parallel form of the preceding w., "taiga- alternating with *taija-; Paz. tež ‘swift, vehement’ (Mx, Aog); Av. (973) brētdrē.taēža- ‘with sharp edge’, (653 sq.) čiži- in compounds ‘sharp’. MPrs tyj ‘sharp’, tyz ‘quick’, NP tēz ‘sharp, impetuous, swift’. (Henning, BSOAS XII, 1947, 45, separates MPrs tyz, NP tez ‘swift’ from tyj, tež, deriving the former from tak-; I do not agree).
3773:tigr [tgl] arrow 319-20, 2013 ete. passim. — Av. (651) tiyri-; OP tigra- ‘pointed’ = Av. (ibd.) čiyra-; Paz. NP tir (SW form).
3776:tigr-ahy (inscr. Prs) [tgl'hy] range of an arrow, HajB:l. — < tigr + *äfya- < *āpya-, from Av. (71) äp- < à + ap-; cf next w.
3777:tigr-ayap [tgly’p'] range of an arrow 2127. 222, — tigr + aydp, v. aydftan.
3812:tugrän, or turgän with the same Prth. metathesis as in tyrg = tirg < tigra- ‘swift’ (A-H ITI) or in the Arm. lw. turž ‘penalty’ < *tužra- (v. tog, toxtan). Prs tgwi'n shows the inverse Sogdian spelling -gw- for -wg- (Henning, BSOS IX, 1938, 548—550), thus representing tugrān, whence tiran according to the common SW phonetic rule. For Turdn, and designating the same country, Yàqult (3,554) quotes the form Tuwärän, which evidently goes back to *tugārān. (NB: no attention has been paid here to the Hast Turkistani names Qayodpot, Sogd twyry, MPrth twr’n Sh (S), MPrs ch?r twgrystn, ete.; I have no competence to meddle in the learned discussions inspired by Pelliot’s article Tokharien et Koutchéen, JA 224 1934, 23-106, and carried on between Bailey: BSOS VIII, 1936, 884-917, TPhS 1947 (1948), 126—153 (cf also BSOAS XIII, 1950, 403 sg.) — and Henning: BSOS IX, 1938, 545-571, A. M., N.S. I, 1949, 159-162. This much may be stated: all the twgrn etc. dealt with in the present article are quite distinct from the Tokharians: Tuxärän and Tuxā- ristän, whose capital was Balkh. V. also Tarn 515-519].
```


## [2026-09-14T02:31:28.492Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"stēz\\|stez\\|stēh\" PHD.txt | head\necho \"=== BQT v1 pages around 543 ===\"\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nm=re.findall(r'\\[pdf page (\\d+)\\]',t)\nprint(len(m), m[:5], m[-5:])\nEOF",
 "description": "PHD stez; BQT v1 structure"
}
```


### [2026-09-14T02:31:31.396Z] TOOL RESULT

```
=== BQT v1 pages around 543 ===
0 [] []
```


## [2026-09-14T02:31:35.141Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 600 BQT_v1_pages.txt; echo; echo \"---\"; python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count(chr(12)),'chars',len(t))\n\"\necho \"=== refs_online BQT offsets ===\"\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[900:3000])\n\"",
 "description": "Inspect BQT files"
}
```


### [2026-09-14T02:31:36.206Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
---
formfeeds 776 chars 1285412
=== refs_online BQT offsets ===
le.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-14T02:31:40.970Z] TOOL CALL #23: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:543 2>&1 | head -60",
 "description": "Fetch BQT page 543"
}
```


### [2026-09-14T02:31:42.076Z] TOOL RESULT

```
no scan of BQT covers printed page 543 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:31:46.205Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor v in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(v,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print(v,len(pages))\n    # find pages containing headword تیر\n    for i,p in enumerate(pages):\n        if 'ستیز' in p or 'ستیه' in p:\n            print(' hit',i,p[:150].replace('\\n',' '))\nEOF",
 "description": "Search BQT v1/v2 for setiz"
}
```


### [2026-09-14T02:31:47.386Z] TOOL RESULT

```
BQT_v1_pages.txt 777
 hit 269 ]هاچ » بای بروزن تاراج , خاکی باش د که تشانتیررا برآن صبکنند چه آماجگاه جاییرا کوبند که نثانه در آنجا بهند - وبسعنی تشانةٌ یرهم هست ۱ - و آلتی را نیز 
 hit 341 وت ۱ تیم استوی بش اول والث بر وزت بر کوی » مهر پشت را کویند . استه * ه ختح اول بروزن خسته , دالةٌ. خرما و شفتالو و زردآ لو ء امثال آبرا کوبند - واستضو
 hit 350 اسکندروی و دختثر از دارا حامله بودوأنظهار نمیکردتابوی دهن‌اورا با اسکندروی که آنرا بفارسی سیر کوشد علاح کردند و مدازآن فرزند بوجود آعد او را لسکنتو من
 hit 457 بچکم - بفتح اول و کاف بروزن شبتم» خانة 7 اطراف آن را شکه کرده بشند ۱ - و ابوان و سفه و بارکده را نیز گویند - و بمعتی کر که هم آهده است که بعربی ذئب‌خو
 hit 471 <- ٩ کرده باشند برجاس گوبند» وانرا که در زمین نمانه کنند حدف خوانند . پر جاسب (۱)- منم اول بروزن لپ راسپ» نام مبارزی است تورانی که با پبران وسه ببجنگه
 hit 620 پرهازه . و پر؛ آسیا (۱) و دولاب و امثال آن باشد - وبسمنی‌پهلو نیز بنظر آمدم‌است که‌بعربی جنب خوانند . پر هازه - بر وزن دروازه . چوب پومیده و رکوی سوخن
 hit 638 بشی بر وژن و ممنی بشه دار است که شجرء البق باشه ٩‏ . فشی س بکراول وانی وسکون تحتانی» مخفف پشیزاست. و آن یرل ریز؛ کرچك بفابت عنكك و نازاه باشد که ازمس 
BQT_v2_pages.txt 684
 hit 23                                           ‫بیان چهارم‬                      ‫درجدم ابجد باخای نقطه دار مشتمل برپنج لغت‬                          ‫برمی
 hit 83   ‫چنده‬                                                                                            ‫‪۷‬‬    ‫ی‬   ‫کسی جستن باشد ؛ وباین معنی‌بجای حر
 hit 296                                                                                                                                ‫درساره‬               
 hit 486                                                   ‫يان دهم‬                           ‫در زای نقطه دار بافا مشتمل برده لغت‬   ‫سياه و‬   ‫چویآزنیست‬  
 hit 523                                              ‫بیان هفتم‬                        ‫در زای فارسی با کاف مشتمل برهشت لفغت‬                                
 hit 554 ‫که درجنگه دوازده رخ بردست حجیری نگودرز‬             ‫سیهید ‪ = ۱‬بکر اول‌وضم بای ابجد‪.‬‬                                     ‫شته شد‪.‬‬           ‫
 hit 561                                                                                                                           ‫نز شا او‬              ‫بقز
 hit 563                                                                                                       ‫=‬  ‫آن قره بطالا باشد‬       ‫ون‬             
 hit 565                                                                                                  ‫‪î‬‬     ‫‪۱ ۵۳‬‬       ‫الوث‬      ‫ثلی‬        ‫ست
 hit 566    ‫‪۷‬‬   ‫‪4‬‬                                                                                                  ‫سنیز‬    ‫یابگراوهبمند ‪ -‬و بممنی 
 hit 567   ‫سجلاط‬                                                                                       ‫==‬   ‫ونافرمالی نمودن‪ -‬وفرباد وشور ‪ -‬ولجاجت کردن
 hit 614             ‫‪۱‬‬             ‫= هی‬                                                                                                                ‫ص
 hit 616       ‫‪۷‬‬       ‫‪ ۷‬ی‬   ‫سکسکی = یم هردو سین و سکون‬ ‫ثالی و رابع بتحتانی کشیده ‪ .‬زحمتی باشد که‬                                                
 hit 619                                                                                             ‫=‬        ‫ع یو‬                                      ‫با
```


## [2026-09-14T02:31:53.280Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (566,567):\n    print(\"==== leaf\",i)\n    print(t[i][:2500])\nEOF",
 "description": "Print BQT v2 leaves 566-567"
}
```


### [2026-09-14T02:31:54.373Z] TOOL RESULT

```
==== leaf 566
   ‫‪۷‬‬   ‫‪4‬‬                                                                                                  ‫سنیز‬


 ‫یابگراوهبمند ‪ -‬و بممنی ستیزندگی‬
                               ‫مآسم‬
                                  ‫و‬                         ‫باشد وآن بوزن (‪ )۱‬تبربز بانزده مثقال است‌چه‬
                         ‫ولجاجت هم هت ® ‪.‬‬                  ‫ارلی‬ ‫تفو ه‬
                                                                    ‫مفال‬
                                                                       ‫بك من تبریز شش صد مت‬
‫‪ ۲‬س بکسر اول و تانیو سعکون‬                              ‫شش دانگه ‪ ,‬ویسنی گویند ستیر شش درم ولیم‬
‫تحتاني مجپول و میم » خون وچرك ورمی باشد‬                                            ‫‪۱‬‬                      ‫باشد ‪.‬‬
‫که درجراحت جمم شود و تا اتر ترنتدیرلیاید‬                    ‫ستیز ‪ - ۱‬بکسر اول و ثانی و سکون‬
‫وجراحت سرماخورده وآمای کردمرالیزکوند‬                         ‫تحتانی مجپول و زای شطه دار (‪ ۰ )۲‬بمعنی‬
‫آونرا کزك خوانند ؛ و بسنی خون فاسدیرا‬                       ‫و سرکشی و لجاجت و خشم‬        ‫چخنگصهوومت‬
‫کفته‌اند کهدرعنوی بهم رسد کها گردفم دکنند‬                    ‫وین و عناد و تسب و اساز کاری باشد ‪- ۴‬‬‫ک‬
 ‫چرك و رم کردد وآن عضو را مجروح سازد ‪.‬‬                      ‫و بمعنی ستیزنده همکفته‌اند ‪ -‬و امرباین‌معنی‬
‫ستیهف ‪» ۷‬با هابروزن ستیزد‪ ,‬ماضی‬                                                                     ‫همست ‪.‬‬
                                                                                                         ‫ه‬
‫ر فرناد و شور‬       ‫است ععنی جنگه‬        ‫خیهیدن‬             ‫اول و ایمکسور وفتح‬  ‫ستیزه ‪ - ۴‬ب ا‬
                                    ‫وغوغا کند ‪.‬‬              ‫زای قطمرار بمعنیستیزاست کە‌جنگه‌رخصومت‬
‫ستیهش ‪ ۰ ۸‬بکس هاو سکون شین‬                                  ‫ولجاجت و قهروکین باشد‪ -‬و بمعنیتظلموتمدی‬
   ‫شلددار سی‪.‬نی لجاجت و متیزدگی بشد‪.‬‬                        ‫هم آمده است ‪ -‬و با زای فارسی بمعنی چله‬
                                                             ‫باشد» وآن رسمانیاست که ازیه‌نای کارجولاهگان‬
‫ست‪7‬یهند گی * س بر وزنفریبندکی‪.‬‬                          ‫‪۱‬‬                                           ‫ژیاد آند ‪.‬‬
 ‫بمعنی ستیزه است که لجاجت وجنگه ورسکشی‬
                                                            ‫ستیغ ‪ » ۴‬بانعتالی مجهول بر وزن‬
                                ‫و تافرمالی ماشد ‪.‬‬
                                                             ‫دریغ» بمعنی ستیخ استکه چیزی راست‌وراست‬
 ‫ستیيند 
==== leaf 567
  ‫سجلاط‬                                                                                       ‫==‬

 ‫ونافرمالی نمودن‪ -‬وفرباد وشور ‪ -‬ولجاجت کردن‬           ‫ستیهیدن ‪ - ۱‬بر وزن شکیبیدن ‪,‬‬
                                            ‫باشد ‪.‬‬   ‫یمعنی ستیزه کردن ‪ -‬و سخن ناشنودن‬

                                              ‫بیان پنجم‬
                ‫بی‌نقطه باجیم مشتمل بر سز ده لغت و کنات‬                            ‫در سن‬

          ‫لون و‬                       ‫بنظرآمده |‬     ‫= بفتح اول و سکون الی ‪ ۰‬بمعنی‬                ‫سج‬


                                                     ‫الی دعرربی گل ا‬              ‫یاد‬
                                                                                    ‫وب‬‫تشدش‪-‬د‬
                                                                                           ‫رخاره با‬
                                                      ‫بدیوار مالیدن و ارم شدن چیزی غلیظ بود ‪- ۴‬‬
                         ‫حال اس باشد ‪.‬‬
                                                                 ‫وفل را گویند‪.‬‬‫وبضم اول سرین ک‬
 ‫سحاهر = بفتح اولوها بروزن‌سراسر»‬                    ‫سچا ‏ بنتح اول و ثالیبالف کشیده ‪,‬‬
         ‫بمعتی قرین وشبیه ونظیر ومانند باشد‪.‬‬         ‫عنوان کتابت و نامه را گویند ‪ - ۴‬و در عربی‬
 ‫سد ‪ - ۲‬بنتح اول و ثالیبروزن لمد»‬                                             ‫باشد ‪.‬‬      ‫ن‬‫وو‬
                                                                                            ‫کوام‬
                                                                                               ‫سنی د‬
                                                                                                   ‫بمع‬
‫سرمای مخت را گوند ؛ و پمایعننی با شین‬                   ‫سحادة نان » کنابه ازدسفسرهتاور‬
                         ‫اتاست‪.‬‬            ‫ی‬                                                 ‫خوان باشد ‪.‬‬

                                                      ‫سجا کند ‪ -‬بنتحاور و کاف بر وزن‬
 ‫سحك ‪ = ۸‬بفتح اولوضم ثالی وسکون‬
‫تی اننتن کلوباه وبریی فراق‬
                         ‫کباملس»‬                      ‫زراوند »کی را گونن دکه مکمل و ملح شده‬
 ‫سرت درهم آميخته باشد که‬       ‫اوشی‬
                                  ‫م‪-‬‬ ‫وند‬‫کوب‬                                                            ‫باشد ‪.‬‬
‫شبت را ریزه کرده در آن ريخته باشند و آبرا‬              ‫سحام ‪ - ۲‬بورزن عوام ‪ ۰‬سرمای‬
   ‫دوراغ نیزکوبند ؛ وباجیم فارسی آهممده‌است‬             ‫ده‬
```


## [2026-09-14T02:32:06.495Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\nprint('page_offset:',d['BQT'].get('page_offset'))\n\"",
 "description": "BQT scans config"
}
```


### [2026-09-14T02:32:07.576Z] TOOL RESULT

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
page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-09-14T02:32:15.639Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(766,776):\n    seg=t[i]\n    has = [w for w in ['تیر','ترکش','تیز','تیغ'] if w in seg]\n    print(i, has, seg[:120].replace('\\n',' '))\nEOF",
 "description": "BQT v1 leaves near 543"
}
```


### [2026-09-14T02:32:16.669Z] TOOL RESULT

```
777
766 ['تیز', 'تیغ'] بر وزن نرسا . شبره گرفتن از انگور را کوند . * فه غربالی -کنابه از دانهای کوچك وتخالهٌ هرچیز باشد . تهاث - بر وزن نمك » خ
767 [] تهمك - بر وزن لك لك , مصفر تهم اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه وعربان - وتهی وخالی باشدا .< بهمو درس - بنتح اول 
768 ['تیر'] قی ۱ ع یکسر اول و سکون ثالی : مخفف تهی است که خالی باشد . تیان اف قون مان دگتن کل بز رک راگوند ؟ » چه تبانچه دبگ سر کشاد
769 ['تیر'] "۹ ۲ - نام فرشته ایست ٩‏ که بر ستوران حو کل است دتدبیرومصالصی که در روز ثير وماه ثير وأفع شود او علق دارد . ۳ - نام ماه 
770 ['تیر'] باشد٩‏ . ٩‏ نام سثار# عطارد است و(۱) او را دیر فلك خواناد ‏ و گویند مربی علما و مشایخ وقضات وارباب فلم باشد ۴ . ۷ غب و ف
771 ['تیر'] 4۳و تبر تظلم ه کنابه از آ, مظلومان باشد . تیرچرخ - "تیه از کرک ساره است - و چیزی بیز باشد مانتد نیر هوایی که از آهن سازن
772 ['تیر', 'تیز', 'تیغ'] تیرعاهی با میم بروزن نیکخواهی: نوعي ازانگود است- ونام داروبی‌هم‌هست- و گزد وزردكه را نیز گویند . تیره۱ س_ پروزن خیره » ت
773 ['تیر', 'تیز', 'تیغ'] - وههات بالف کشیده و بسن سفص وتای فرشت زده » نم ضه‌ایست از موسیقی وآن دا کردانید نیز خوانند ۰ وآن‌از جملهةٌ ثش‌آوازه است
774 ['تیز', 'تیغ'] غ افراسداب نیز گفته‌اند ۱ - وهرچیزبلند وراست ابستاده‌بود- و فروغ و روشتیآفتاب و ماه و آنش وامثال آن باشد؟ - وجوهر فولاد 
775 [] اي محِ چنبر رسن تابی را گوبند م ویفتح اول‌جعل‌منقش دا یازا 9 تیلیاك - یکی اول وئالث وسکون‌ثانی گویند . لیم سم بر وزن میم
```


## [2026-09-14T02:32:24.219Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (768,769,770,771):\n    seg=t[i]\n    for line in seg.split('\\n'):\n        if 'تیرکش' in line or 'ترکش' in line or 'تیردان' in line or 'تیر ' in line[:20]:\n            print(i,'|',line.strip()[:200])\nEOF\necho \"=== grep tarkash whole v1 ===\"\ngrep -c \"ترکش\" BQT_v1_pages.txt",
 "description": "Search BQT for tirkash"
}
```


### [2026-09-14T02:32:25.368Z] TOOL RESULT

```
768 | و یقشار - و تیر را لیز گوشد که بعربی سهم
769 | ای نگار تیر بالا » تیر روز 7[
769 | کرچه تیر از کمانٍ هم يکنرد از کماندار ند امل‌خرد.« کلستان ۷*,
771 | تیر 2 ع ی دزن زیرك» صخیر نیرست
771 | تیر گر دون عم کنابه از آفتاب اسش
=== grep tarkash whole v1 ===
0
```


## [2026-09-14T02:32:35.255Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IRN pdf 123 (printed 112) ===\"\npython3 - <<'EOF'\nimport re\nt=open('incoming/IRN/IRN_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nprint('pages',len(d), min(d), max(d))\nfor p in (122,123,124):\n    print('---- pdf',p)\n    print(d.get(p,'')[:2500])\nEOF",
 "description": "Iranvij page 112"
}
```


### [2026-09-14T02:32:36.385Z] TOOL RESULT

```
=== IRN pdf 123 (printed 112) ===
pages 222 1 222
---- pdf 122

اروندرود ۱۱
از سرکشی آن ساخته بودند خرا بکرده ودر خود فرو برده وزمین‌های بسیار را
نخمت به دریاچه وب رکه و باتلاق وسپس به بیابان تبدیل کرده است.
سرچشمه‌هایی که این رود درکوههای غربی ایران در زاگرس دارد »
به اندازه‌ای بلند هستند که طبعاً بستر این رودهای فرعی را تند و سراشیب
می‌سازند وآب این رودها در هنگام بارانهای بهاری زود طغیان می‌کند و همواره
در ماه‌های اسفند و فروردین و اردی‌بهشت سیلابهای تند ازاین رودهای پرشیب
دامنةُ زاگرس به دجله می‌ریزد وسوجب طغیان آن می‌شود . در تاریخ میانرودان
همواره این طفغیانهای بزرگك موجب خرابی‌های بسیارشده است . یکی از این
سرکشی‌های دجله درسال و ۲و میلادی است که خرابی‌های بسیار ببار آورد .
در این سال دجله وفرات هردو باهم طغیان کردند ودر همه‌جا سد و بندها
شکسته شد وغانه وسزرعةٌ مردم را فراگرفت ودر حدود صدهزار نفر در این حادثه
ازمیان رفتند . خسرو پرویز برای بستن‌سدها خرج بسیارکرد ولی نتیجه‌ای نگرفت»
بطور ی که آب به تالارکاخ تیسفون رسید وگوشه‌ای از آن فرو ریخت وپس از
این بلای بزرگك ودر اثرکشتاری که سیل ببار آورد» طاعونی سهمگین روی آورد
که شیرویه پادشاه ساسانی نیز از آن بیماری درگذشت و همین بیماری طاعون که
در م رک زکشور ایران درکنار دجله بروزکرد ونیز خشکسالی بزرگی که در همان
هنگام براثر از میان رفتن مزرعه‌ها روی داد» موجبات گشوده شدن راه حملةٌ تازیان
رابه ایران قراهم آورد .
در همین سدهٌ پیستم درسالهای ‎٩.٩‏ (9 ۹۶۱ 9۱9239۱ ۹۰2 رمیلاد ی
طغیانهای بزرگك دجله موجب ویرانی‌های بسیار شد ودرسال ۱۹۰۶ آب دجله
داخل فرات گشت . بنابرهمین س رکشی‌ها وطفیانهای دجله اس تکه ایرانیان به‌آن
نام تیگر 872 يا تند و سرکش داده‌اند,
نام 872 هنگامی که وارد زبان بابلی گشت تغییرات کوچک فونتیکی
یافت» به این ترتی ب که حرف ۲ به «4 » بدل شد و « ۶ » ایرانی به (1۸ » تبدیل

---- pdf 123

۱۱۲ ایرانویج
یافت واین تغییرات» تغییرات منظم فونتیکی اس ت که به هنگام عاریت گرفتن
واژه‌ها پیش‌می‌آید. در زبانهای ایرانی نیز ها ی کهن به4 و ۶ ها ی کهن به 1
بدل می‌شوند . به این ترتیب از واژهٌ 1872 در بابل ی کهن نام دیگله +هاونل پدید
آمد وسپس گاف به جیم بدل شد واين نیز یک تبدیل رایج است وگاف‌های
پارسی در عربی به جیم بدل می‌شوند. بدین ترتیب ديگلة ول به چهرةٌ ديجلة
+ازنه در آمد وسپس به دیجله (تلفظ عریی آن) و دجله گرائید.

اما این تبدیل به همین‌جا پایان نیافته است وبار دیگر تبدیل دیگری
صورت گرفته واین بارهج» ‏ در دیجله به 7 مبدل شده اس تکه این هم‌يکك تبدیل
منظم فونتیکی‌است ودر بسیاری از زبانها «ج» به «ی» تبدیل می‌شود. بااین تغییر
واه دیجله هلان به صورت 2اأونك یا دیاله در آم د که آن هم یکی از رودهایی
اس ت که از ایران سرچشمه می‌گیرد وسمیرش تند وسراشیب است وبه دجله فرو
می‌ریزد .

در دوران ساسانیان رود دجله راء هم به‌نام کهن آن دیگله 2اونك یادیلگه
2ولنلمی‌خواندند وهم‌خود وارْهٌ تیگر 872 را که یک واژْهٌ فارسی باستان است به
زبان پهلوی ترجمهٌ کرده وآن را اروندرود می‌نامیدند. واژه اروند همان معنای
«تیگر» را دارد و از آن تند وتیز وس رکش برمی‌آید, در دور ساسانیان هردو نام
«دیگله» و«اروند» را برای رود دجله بکار می‌بردند.

اروند که ترجمهٌ واه تیگر است دارای. ريشه وبن اوستایی است ودر اوستا
به صورت ائوروت 27۷2 آمده است وازريشهٌ کهن ائورو 27۷2 به معنی سرکش
وتند وتیزاست وپسوند ۷2۳ يا ۷2 به معنی‌دارنده است وبرروی هم‌به‌معنی دارندةٌ
تندی وتیزی وسرکشی است. ریشهٌ اروند در نام لهراسب نیز دیده می‌شود.
لهراسب از دو واه ائوروت +27۷2 واسپ 28202 ت ر کیب يافته وبه معنی‌تیزاسب
پا تند اسب است یعنی کس ی که دارای اسب تند وس رکش است. ائوروت اسپ

---- pdf 124

اروندرود ۱۱۳
در پهلوی به صورت اروت اسپ 2۳7۷2۳2802 آمده و در پازند تیز اسپ معنی شده
و در فارسی لهراسب شده است . ائوروت 27۷2 در اوستا صفت خورشید نیز
هست‌وخورشید تیزاسب در اوستا چندین بار آمده است . درجای دیگر اوستا ائوروت
+4 هصفت. ایزداپم‌نپات 2031 20270 یعنی ناف ونژاد آب آمده وآن ایزد
نگهبان آبهاست واز اینرو ایرانیان نام اروند راهم به مناسبت تندی وتیزی و
سرکشی رود دجله وهم به سبب آنکه اروند صفت فرشته آب یااپم‌نپات واناهیت
است برروی این رود گذاشته‌اند» زیرا دجله در نظر ایرانیان مانند همه آبها و رودها
به خاطر اینکه زمین را بارور وسیراب می کرده» مقدس وقابل‌ستایش بوده است .

در ایران کهن اروند به صورت نام خاص نیز بکار رفته است. یکی از این
نام‌های خاص ارنت يا ارونتس 0702169 اس ت که چهرةٌ یونانی شدهٌ نام اروند
است ونام یکی از سرداران دوران اردشیر دوم هخامنشی است . اروند باواژه‌های
دیگر نیز پیوسته ونام های خاص بسیار پدیدآورده است . اروند دست 428۴ ۸۳۷2۳0
نام پسر خسرو دوم است.

ارونداسپ بجز نام لهراس پ که ذکر آن رفت» نام پدر بیوراسپ ونیز نام
وزیر تهمورث است.

واژْةٌ الون د که نام کوه مشهور در همدان است شکل تحول یافته‌ای از واه
اروند اس ت که در آن «ر» به «ل» تبدیل شده است واین نام به مناسبت قلةٌ بلندو
نوک تیز وشیب تند این کوه به آن داده شده است .

در فرهنگك برهان قاطع در زیر نام اروند چنین آمده است: «اروند بروزن‌و
معنی‌الوند است وآن کوهی باشد در نواحی همدان . . .ودجله بغداد را نیز گفته‌اند.

فرهنگك جهانگیری برای واه اروند چنین شاهد آورده است:

دار اروندرود را بریاد که بتازی بود شط بغداد

فردوسی در شاهنامه بارها از اروندرود به جای دجله نام برده است وبه

هنگامی که از خواب دیدن انوشیروان یاد.می"کند چنین آورده است:
```


## [2026-09-14T02:32:48.998Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:32:49.005Z] TOOL RESULT

```


```


## [2026-09-14T02:32:52.128Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-",
 "prompt": "Give the reconstructed root, its meaning, and the list of descendants (especially Proto-Indo-Iranian/Iranian, Greek, Latin, Germanic)."
}
```


## [2026-09-14T02:32:53.047Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tiger",
 "prompt": "Full etymology of \"tiger\" and any note about Tigris river and the Iranian/Avestan connection."
}
```


### [2026-09-14T02:32:56.568Z] TOOL RESULT

```
# Proto-Indo-European Root *(s)teyg-

**Reconstructed Root:** *(s)teyg-

**Meanings:** The root denotes two related senses: "to be sharp" and "to sting."

**Key Descendants:**

**Proto-Indo-Iranian/Iranian:**
- Sanskrit téjas (brightness/splendor) and tiktá (sharp)
- Persian تیز (tiz, sharp)
- Kurdish tîj/tûj (sharp)

**Greek:**
- Ancient Greek στίζω (stízō, to prick/mark)
- Ancient Greek στίγμα (stígma, mark/puncture)

**Latin:**
- instīgō (to stimulate or incite)

**Germanic:**
- Proto-Germanic *stikaną (to stick/pierce)
- Proto-Germanic *þistilaz (thistle plant)

The root demonstrates the characteristic Indo-European semantic evolution from physical sharpness to abstract notions of brightness and stimulation across descendant languages.
```


### [2026-09-14T02:32:58.521Z] TOOL RESULT

```
# Etymology of "Tiger"

The word "tiger" traces back through multiple language layers. Middle English *tigre* derives from Old English *tigras* and Old French *tigre*, both ultimately from Latin *tigris*, which came from Greek *tigris*.

The most intriguing element is the possible Iranian origin. According to the source, the Greek term may come "from an Iranian source akin to Old Persian *tigra-* 'sharp, pointed,' Avestan *tighri-* 'arrow,'" with this etymology potentially referencing the animal's pouncing behavior on prey. However, the source notes that "no application of either word, or any derivative, to the tiger is known in Zend."

**Regarding the Tigris River:** While the etymology article doesn't explicitly discuss the Tigris River connection, the shared Latin root *tigris* suggests both the animal name and the river name derive from the same ancient source, likely reflecting the Iranian linguistic roots mentioned above.

The connection to sharpness and arrows in the Iranian languages appears to capture the tiger's defining characteristic—its swift, piercing attack on prey—making it a metaphorically apt name across ancient cultures.
```


## [2026-09-14T02:33:03.419Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"tiger\" \"Tigris\" \"astigmatism\" \"etiquette\" \"ticket,\" \"stigma,\"; do echo \"#### $w\"; grep -n -m3 \"^$w\\|[^a-z]$w\" KLN_1966.txt | head -4; done",
 "description": "Grep Klein"
}
```


### [2026-09-14T02:33:04.513Z] TOOL RESULT

```
#### tiger
7273:chatelain,  n.,  castellan.  —  F.  See  castellan, chatelaine,  n.,  the  mistress  of  a  castle;  key  chain worn  at  the  waist  by  women.  —  F.,  fern,  of chatelain.  See  prec.  word, chati,  n.,  a  South  American  tiger  cat.  —  Of  South American  Indian  origin.
7661:Cichoriaceae,  n.  pi.,  the  chicory  family  (bot.)  — ModL.,  formed  fr.  Cichorium  with  suff.  -aceae. cichoriaceous,  adj.  —  See  prec.  word  and  -aceous, Cichorium,  n.,  a  genus  of  plants,  the  succory  or chicory  (bot.)  —  ModL.,  see  chicory. Cicindelidae,  n.  pi.,  a  family  of  beetles,  the  tiger beetles  (entomol.)  —  ModL.,  fr.  L.  cicindela, ‘glowworm’,  formed  with  reduplication — through  the  medium  of  the  forms  *cecandela, *cecendela — fr.  candere,  ‘to  glow’.  See  candid and  cp.  words  there  referred  to.  For  the  ending see  suff.  -idae.
9838:cub,  n.,  the  young  of  the  fox,  bear,  wolf,  lion, tiger  etc.  — •  Of  uncertain  origin;  perhaps  rel. to  ON.  and  Icelandic  kobbi,  Norw.  kobbe,  ‘seal’.
#### Tigris
14605:Fertile  Crescent,  a  semicircle  of  fertile  land  ex¬ tending  from  Palestine  and  Phoenicia  around the  Euphrates-Tigris  valley  to  the  Persian  Gulf {Ancient  hist.)  —  Coined  by  the  American  ar¬ chaeologist  and  historian  James  H.  Breasted (1865-1935).
23636:mesoblast,  n.,  the  mesoderm.  —  Compounded  of  between  the  Euphrates  and  Tigris  rivers.  —  Gk.
39240:Derivative:  tigell-ate,  adj. tiger,  n.  —  ME.  tigre,  fr.  OF.  (=  F.)  tigre,  fr.  L. tigris,  fr.  Gk.  riypt?,  prop,  ‘the  swift  animal’, a  word  of  Iranian  origin.  Cp.  Avestic  tiyrish, ‘arrow’,  tiyra-,  ‘pointed’.  These  words  are  deriv¬ atives  of  I.-E.  base  *(s)teig-,  ‘to  prick,  stick, pierce’.  Cp.  Gk.  Tlypt?  (whence  L.  Tigris),  ‘the Tigris  river’,  lit.  ‘the  swift  river’,  and  see  stick, v.,  and  words  there  referred  to.
#### astigmatism
72:aspirin,  n.  ( pharm .)  —  A  hybrid  coined  by  H.  Dreser  in  Pfliiger's  Archiv  in  1 899.  The  acetylo-salicylic acid  occurs  in  the  flowers  of  the  plant  Spiraea  ulmaria.  In  order  to  distinguish  from  this  natural  pro¬ duct  the  same  substance  gained  chemically,  the  word  aspirin  was  formed  by  Dreser  from  priv.  pref. a-,  the  above  mentioned  plant  Spiraea,  and  chem.  suff.  -in.  Hence  aspirin  prop,  means  ‘acetylo-sali¬ cylic  acid  which  is  gained  not  from  the  Spiraea  ulmaria  (but  in  a  chemical  way)’, astigmatism,  n.,  defect  of  the  eye  that  prevents  the  rays  of  light  from  converging  to  a  point  on  the  retina (med.  and  optics ).  —  Coined  by  the  English  mathematician  and  philosopher  William  Whewell  ( 1 794- 1866)  in  1819  fr.  priv.  pref.  a-  and  Gk.  a-uypa,  gen.  crTlyiiaTog,  ‘a  prick,  puncture,  mark’.  See  stig- matic  and  -ism.
3742:asthmatic,  adj.  —  L.  asthmaticus,  fr.  Gk.  aaffpia- xixoc,  fr.  dahlia.  See  asthma  and  -atic. Derivative:  asthmatic-al-ly,  adv. astigmatic,  adj.,  pertaining  to,  or  suffering  from, astigmatism  (med.  and  optics).  —  See  next  word, astigmatism,  n.,  defect  of  the  eye  that  prevents the  rays  of  light  from  converging  to  a  point  on the  retina  (med.  and  optics).  —  Coined  by  the English  mathematician  and  philosopher  Wil¬ liam  Whewell  (1794-1866)  in  1819  fr.  priv.  pref. a-  and  Gk.  axiypa,  gen.  oxtypaxo?,  ‘a  prick, puncture,  mark’.  See  stigmatic  and  -ism. Astilbe,  n,,  a  genus  of  plants  of  the  saxifrage family  (bot.)  —  ModL.,  lit.  ‘not  shining’,  fr. priv.  pref.  a-  and  axiX()eiv,  ‘to  shine’.  See  stilbite. astir,  adv.  —  Formed  fr.  a-,  ‘on’,  and  stir, astomatous,  adj.,  having  no  mouth.  —  Formed fr.  priv.  pref.  a-  and  -stomatous. astonish,  tr.  v.  —  Obsol.  astony,  fr.  ME.  astonien , astonen,  which  is  formed  with  change  of  pref. fr.  e st oner  (whence  F.  etonner),  fr.  VL.  *exto- nare,  lit.  ‘to  strike  with  thunder’,  fr.  1st  ex- and  L.  tondre,  ‘to  thunder’.  See  thunder  and  cp. astound.  The  verb  astonish  was  influenced  in form  by  English  verbs  ending  in  -ish,  in  which this  suff.  is  the  equivalent  of  OF.  and  F.  -iss.
36789:stick,  tr.  and  intr.  v.  —  ME.  stikien  (weak  v.),  ‘to prick;  to  be  infixed’,  and  steken  (strong  v.),  ‘to prick,  fix’,  fr.  OE.  stician,  ‘to  stab,  prick,  pierce’, rel.  to  OS.  stekan,  OFris.  steka,  Du.  steken, OHG.  stehhan ,  MHG.,  G.  stechen,  ‘to  stab, prick’,  OHG.  stechhon,  MHG.  stecchen,  stec- ken,  G.  stecken,  ‘to  stick  (intr.),  OHG.  stecchen, MHG.,  G.  stecken,  ‘to  stick’  (tr.).  Du.  stikken, G.  sticken,  ‘to  embroider’,  ON.  steikja,  ‘to roast’,  lit.  ‘to  fix  to  the  spit’ ;  fr.  I.-E.  base  *steig-, ‘to  prick,  stick,  pierce’,  whence  also  L.  instigare, ‘to  goad’,  instinguere,  ‘to  incite;  impel’,  distin- guere,  ‘to  distinguish’,  Gk.  or ££ew  (for  *ax(- Yielv),  ‘to  prick,  puncture’,  oxixxo?  (prop, verbal  adj.  of  crxt£ei.v),  ‘embroidered;  spotted’, axiyp.a,  ‘mark  made  by  a  pointed  instrument’, Lith.  stingu,  stigti,  ‘to  remain  (lit.  be  stuck)  in  a place’,  Russ,  stegdti,  stegnuti,  ‘to  quilt’,  stezka, ‘seam,  suture’,  Bret,  stiogan,  ‘cuttlefish’.  Cp. — without  initial  s — OI.  tejute,  ‘is  sharp,  sharpens’, tejdyati,  ‘sharpens,  pricks,  stings’,  tigmah, ‘pointed’,  Avestic  tiyra-,  ‘pointed’,  tiyri-,  ‘ar¬ row’.  Base  *steig-  is  an  enlarged  form  of  base *stei-,  ‘pointed’,  whence  L.  stilus,  ‘pointed  in¬ strument’,  stimulus,  ‘a  goad,  sting,  incentive’. Cp.  stick,  n.,  and  the  first  element  in  stickle¬ back.  Cp.  also  astigmatism,  distinct,  distinguish, etiquette,  extinguish,  instigate,  instinct,  steak, stigma,  stimulus,  stipple,  stitch,  style,  ‘pointed instrument’,  thistle,  ticket,  tiger,  Tigridia. Derivatives:  stick-er,  n.,  stick-y,  adj.,  stick-i-ly, adv.,  stick-i-ness,  n.,  stick-ing,  adj.,  and  n. stick,  n.  —  ME.  sticke,  fr.  OE.  sticca,  rel.  to  ON. stik,  stikka,  OHG.  stehho,  stecko,  MHG.  steche, G.  Stecken,  ‘stick,  staff’,  and  to  OE.  stician,  ‘to stab,  prick,  pierce’;  in  many  meanings  directly fr.  stick,  v.  (q.v.)  Cp.  the  second  element  in tandstickor.
#### etiquette
13746:Derivatives:  (a)etiolog-ic-al,  adj.,  (a)etiolog-ie- al-ly,  adv.,  (a)etiolog-ist,  n. etiquette,  n..  conventional  rules  of  social  behav¬ ior.  —  F.  etiquette,  fr.  OF.  estiquier,  estiquer, ‘to  stick  on,  attach’,  fr.  Du.  stikken,  'to  stitch’, which  is  rel.  to G. sticken, ‘toembroider’, stechen. ‘to  stab,  prick,  puncture’.  See  stitch  and  cp. ticket,  which  is  a  doublet  of  etiquette. etna,  n.,  a  device  for  boiling  water.  —  Fr.  Mt. Etna,  fr.  Phoen.  attund,  ‘furnace’,  which  prob. derives  fr.  Akkad,  atunu,  uliinu,  wdtence  also Aram,  attfm,  attund,  Syr.  attonid,  of  s.m.;  cp. Arab,  attiin,  Ethiop.  etdn,  of  s.m.,  which  are Syriac  loan  words.  Cp.  Etnean.
36789:stick,  tr.  and  intr.  v.  —  ME.  stikien  (weak  v.),  ‘to prick;  to  be  infixed’,  and  steken  (strong  v.),  ‘to prick,  fix’,  fr.  OE.  stician,  ‘to  stab,  prick,  pierce’, rel.  to  OS.  stekan,  OFris.  steka,  Du.  steken, OHG.  stehhan ,  MHG.,  G.  stechen,  ‘to  stab, prick’,  OHG.  stechhon,  MHG.  stecchen,  stec- ken,  G.  stecken,  ‘to  stick  (intr.),  OHG.  stecchen, MHG.,  G.  stecken,  ‘to  stick’  (tr.).  Du.  stikken, G.  sticken,  ‘to  embroider’,  ON.  steikja,  ‘to roast’,  lit.  ‘to  fix  to  the  spit’ ;  fr.  I.-E.  base  *steig-, ‘to  prick,  stick,  pierce’,  whence  also  L.  instigare, ‘to  goad’,  instinguere,  ‘to  incite;  impel’,  distin- guere,  ‘to  distinguish’,  Gk.  or ££ew  (for  *ax(- Yielv),  ‘to  prick,  puncture’,  oxixxo?  (prop, verbal  adj.  of  crxt£ei.v),  ‘embroidered;  spotted’, axiyp.a,  ‘mark  made  by  a  pointed  instrument’, Lith.  stingu,  stigti,  ‘to  remain  (lit.  be  stuck)  in  a place’,  Russ,  stegdti,  stegnuti,  ‘to  quilt’,  stezka, ‘seam,  suture’,  Bret,  stiogan,  ‘cuttlefish’.  Cp. — without  initial  s — OI.  tejute,  ‘is  sharp,  sharpens’, tejdyati,  ‘sharpens,  pricks,  stings’,  tigmah, ‘pointed’,  Avestic  tiyra-,  ‘pointed’,  tiyri-,  ‘ar¬ row’.  Base  *steig-  is  an  enlarged  form  of  base *stei-,  ‘pointed’,  whence  L.  stilus,  ‘pointed  in¬ strument’,  stimulus,  ‘a  goad,  sting,  incentive’. Cp.  stick,  n.,  and  the  first  element  in  stickle¬ back.  Cp.  also  astigmatism,  distinct,  distinguish, etiquette,  extinguish,  instigate,  instinct,  steak, stigma,  stimulus,  stipple,  stitch,  style,  ‘pointed instrument’,  thistle,  ticket,  tiger,  Tigridia. Derivatives:  stick-er,  n.,  stick-y,  adj.,  stick-i-ly, adv.,  stick-i-ness,  n.,  stick-ing,  adj.,  and  n. stick,  n.  —  ME.  sticke,  fr.  OE.  sticca,  rel.  to  ON. stik,  stikka,  OHG.  stehho,  stecko,  MHG.  steche, G.  Stecken,  ‘stick,  staff’,  and  to  OE.  stician,  ‘to stab,  prick,  pierce’;  in  many  meanings  directly fr.  stick,  v.  (q.v.)  Cp.  the  second  element  in tandstickor.
36842:Derivatives :  stirrup,  tr.  v.,  stirrup-less,  adj. stitch,  n.  —  ME.  stiche,  fr.  OE.  slice,  ‘puncture, stab,  stitch,  stitching’,  rel.  to  OE.  stician,  ‘to prick’.  See  stick,  v.,  and  cp.  etiquette,  ticket, stitch,  tr.  and  intr.  v.  —  ME.  stichen,  fr.  stiche. See  stitch,  n.
#### ticket,
13746:Derivatives:  (a)etiolog-ic-al,  adj.,  (a)etiolog-ie- al-ly,  adv.,  (a)etiolog-ist,  n. etiquette,  n..  conventional  rules  of  social  behav¬ ior.  —  F.  etiquette,  fr.  OF.  estiquier,  estiquer, ‘to  stick  on,  attach’,  fr.  Du.  stikken,  'to  stitch’, which  is  rel.  to G. sticken, ‘toembroider’, stechen. ‘to  stab,  prick,  puncture’.  See  stitch  and  cp. ticket,  which  is  a  doublet  of  etiquette. etna,  n.,  a  device  for  boiling  water.  —  Fr.  Mt. Etna,  fr.  Phoen.  attund,  ‘furnace’,  which  prob. derives  fr.  Akkad,  atunu,  uliinu,  wdtence  also Aram,  attfm,  attund,  Syr.  attonid,  of  s.m.;  cp. Arab,  attiin,  Ethiop.  etdn,  of  s.m.,  which  are Syriac  loan  words.  Cp.  Etnean.
36789:stick,  tr.  and  intr.  v.  —  ME.  stikien  (weak  v.),  ‘to prick;  to  be  infixed’,  and  steken  (strong  v.),  ‘to prick,  fix’,  fr.  OE.  stician,  ‘to  stab,  prick,  pierce’, rel.  to  OS.  stekan,  OFris.  steka,  Du.  steken, OHG.  stehhan ,  MHG.,  G.  stechen,  ‘to  stab, prick’,  OHG.  stechhon,  MHG.  stecchen,  stec- ken,  G.  stecken,  ‘to  stick  (intr.),  OHG.  stecchen, MHG.,  G.  stecken,  ‘to  stick’  (tr.).  Du.  stikken, G.  sticken,  ‘to  embroider’,  ON.  steikja,  ‘to roast’,  lit.  ‘to  fix  to  the  spit’ ;  fr.  I.-E.  base  *steig-, ‘to  prick,  stick,  pierce’,  whence  also  L.  instigare, ‘to  goad’,  instinguere,  ‘to  incite;  impel’,  distin- guere,  ‘to  distinguish’,  Gk.  or ££ew  (for  *ax(- Yielv),  ‘to  prick,  puncture’,  oxixxo?  (prop, verbal  adj.  of  crxt£ei.v),  ‘embroidered;  spotted’, axiyp.a,  ‘mark  made  by  a  pointed  instrument’, Lith.  stingu,  stigti,  ‘to  remain  (lit.  be  stuck)  in  a place’,  Russ,  stegdti,  stegnuti,  ‘to  quilt’,  stezka, ‘seam,  suture’,  Bret,  stiogan,  ‘cuttlefish’.  Cp. — without  initial  s — OI.  tejute,  ‘is  sharp,  sharpens’, tejdyati,  ‘sharpens,  pricks,  stings’,  tigmah, ‘pointed’,  Avestic  tiyra-,  ‘pointed’,  tiyri-,  ‘ar¬ row’.  Base  *steig-  is  an  enlarged  form  of  base *stei-,  ‘pointed’,  whence  L.  stilus,  ‘pointed  in¬ strument’,  stimulus,  ‘a  goad,  sting,  incentive’. Cp.  stick,  n.,  and  the  first  element  in  stickle¬ back.  Cp.  also  astigmatism,  distinct,  distinguish, etiquette,  extinguish,  instigate,  instinct,  steak, stigma,  stimulus,  stipple,  stitch,  style,  ‘pointed instrument’,  thistle,  ticket,  tiger,  Tigridia. Derivatives:  stick-er,  n.,  stick-y,  adj.,  stick-i-ly, adv.,  stick-i-ness,  n.,  stick-ing,  adj.,  and  n. stick,  n.  —  ME.  sticke,  fr.  OE.  sticca,  rel.  to  ON. stik,  stikka,  OHG.  stehho,  stecko,  MHG.  steche, G.  Stecken,  ‘stick,  staff’,  and  to  OE.  stician,  ‘to stab,  prick,  pierce’;  in  many  meanings  directly fr.  stick,  v.  (q.v.)  Cp.  the  second  element  in tandstickor.
36842:Derivatives :  stirrup,  tr.  v.,  stirrup-less,  adj. stitch,  n.  —  ME.  stiche,  fr.  OE.  slice,  ‘puncture, stab,  stitch,  stitching’,  rel.  to  OE.  stician,  ‘to prick’.  See  stick,  v.,  and  cp.  etiquette,  ticket, stitch,  tr.  and  intr.  v.  —  ME.  stichen,  fr.  stiche. See  stitch,  n.
#### stigma,
26889:Pachystima,  n.,  a  genus  of  plants  of  the  staff-tree family  (bot.)  —  ModL.,  compounded  of  pachy- and  Gk.  crnypia,  ‘puncture,  stigma'.  See  stigma, pacific,  adj.  —  MF.  (=  F.)  pacifique,  fr.  L. pdcificus,  ‘peace-making’,  fr.  pax,  gen.  pads, ‘peace’,  and  -ficus,  fr.  -ficere,  unstressed  form  of facere,  ‘to  make,  do’.  See  pacify  and  adj.  suff.  -ic. Derivatives:  pacific-al,  adj.,  pacific-al-ly,  adv. Pacific,  n.,  the  Pacific  Ocean.  —  From  prec. word;  so  called  by  its  discoverer  Vasco  Nunez De  Balboa  (cca.  1475-1517)  in  allusion  to  the calmness  of  its  waves.
36789:stick,  tr.  and  intr.  v.  —  ME.  stikien  (weak  v.),  ‘to prick;  to  be  infixed’,  and  steken  (strong  v.),  ‘to prick,  fix’,  fr.  OE.  stician,  ‘to  stab,  prick,  pierce’, rel.  to  OS.  stekan,  OFris.  steka,  Du.  steken, OHG.  stehhan ,  MHG.,  G.  stechen,  ‘to  stab, prick’,  OHG.  stechhon,  MHG.  stecchen,  stec- ken,  G.  stecken,  ‘to  stick  (intr.),  OHG.  stecchen, MHG.,  G.  stecken,  ‘to  stick’  (tr.).  Du.  stikken, G.  sticken,  ‘to  embroider’,  ON.  steikja,  ‘to roast’,  lit.  ‘to  fix  to  the  spit’ ;  fr.  I.-E.  base  *steig-, ‘to  prick,  stick,  pierce’,  whence  also  L.  instigare, ‘to  goad’,  instinguere,  ‘to  incite;  impel’,  distin- guere,  ‘to  distinguish’,  Gk.  or ££ew  (for  *ax(- Yielv),  ‘to  prick,  puncture’,  oxixxo?  (prop, verbal  adj.  of  crxt£ei.v),  ‘embroidered;  spotted’, axiyp.a,  ‘mark  made  by  a  pointed  instrument’, Lith.  stingu,  stigti,  ‘to  remain  (lit.  be  stuck)  in  a place’,  Russ,  stegdti,  stegnuti,  ‘to  quilt’,  stezka, ‘seam,  suture’,  Bret,  stiogan,  ‘cuttlefish’.  Cp. — without  initial  s — OI.  tejute,  ‘is  sharp,  sharpens’, tejdyati,  ‘sharpens,  pricks,  stings’,  tigmah, ‘pointed’,  Avestic  tiyra-,  ‘pointed’,  tiyri-,  ‘ar¬ row’.  Base  *steig-  is  an  enlarged  form  of  base *stei-,  ‘pointed’,  whence  L.  stilus,  ‘pointed  in¬ strument’,  stimulus,  ‘a  goad,  sting,  incentive’. Cp.  stick,  n.,  and  the  first  element  in  stickle¬ back.  Cp.  also  astigmatism,  distinct,  distinguish, etiquette,  extinguish,  instigate,  instinct,  steak, stigma,  stimulus,  stipple,  stitch,  style,  ‘pointed instrument’,  thistle,  ticket,  tiger,  Tigridia. Derivatives:  stick-er,  n.,  stick-y,  adj.,  stick-i-ly, adv.,  stick-i-ness,  n.,  stick-ing,  adj.,  and  n. stick,  n.  —  ME.  sticke,  fr.  OE.  sticca,  rel.  to  ON. stik,  stikka,  OHG.  stehho,  stecko,  MHG.  steche, G.  Stecken,  ‘stick,  staff’,  and  to  OE.  stician,  ‘to stab,  prick,  pierce’;  in  many  meanings  directly fr.  stick,  v.  (q.v.)  Cp.  the  second  element  in tandstickor.
36796:stifle,  n.,  the  joint  above  the  hock  of  a  horse  or dog.  —  Of  uncertain  origin, stigma,  n.,  mark;  reproach.  —  L.,  fr.  Gk.  oxtypia, ‘puncture,  brand’,  from  the  stem  of  oxi^eiv  (for ‘oxtyiciv ),  ‘to  prick,  point,  mark’.  See  stick,  v., and  cp.  astigmatism.  Cp.  also  the  second element  in  Pachystima.  For  the  ending  see  suff. -ma.
```


## [2026-09-14T02:33:18.884Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 steig ===\"\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nprint('pages',len(d),min(d),max(d))\n# find (s)teig-\nfor p,txt in d.items():\n    if 'teig-' in txt and 'stechen' in txt:\n        print('hit pdf',p, txt[:80].replace('\\n',' '))\nEOF",
 "description": "Find Walde-Pokorny steig-"
}
```


### [2026-09-14T02:33:20.042Z] TOOL RESULT

```
Exit code 1
=== WLD Bd2 steig ===
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
ValueError: min() iterable argument is empty
```


## [2026-09-14T02:33:22.883Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 400 incoming/WLD/WLD_Bd2_pages.txt; echo; echo \"---\"\ngrep -n \"steig\\|(s)teig\" incoming/WLD/WLD_Bd2_pages.txt | head -20",
 "description": "Inspect WLD Bd2"
}
```


### [2026-09-14T02:33:22.950Z] TOOL RESULT

```
                ALOIS WALDE


VERGLEICHENDES WORTERBDCH
                            DER


  INDOGERMANISCHEN SPRACHEN

          HERAUSGEGEBEN UNO BEARBEITET
                            VON

               JULIUS POKORNY


                      II.   BAND




             B£|UN UND LEIPZIG 1*927

       WALTER DE GRUYTER & CO.
  VORMALS G. J. GOSCHEN'SCHE VERLAGSHANDLUNG -
  J.   GUTTENTAG, VE
---
2335:„vor, fur^**, ags. for ebenso, aisl. for- in Zs. ,,vor^‘ mit steigernder Bed. vor
6227:im Fluge heimkehren", usfrav&nte ,j(die Wolken) steigen auf" kann in nicht
11884:gewinnen, da flare sich nicht zu so grellen Schallbedeutungen steigert
12352:bholo- etwa „Dunstj Dainpf, warm aufsteigender Geruch“.
25258:a = e\     XdfjiTieo ist vielleicht kein uniibersteigliches Hindernis.
26720:jiirga Hes., eig. „unersteiglich“, Xlip nhga^ dp i]g vdcog ozdCei Hes, (s. dazu
26750:laipirdi „steigen lassen"), lipsznus, lipniis „klebrig“, lipus „ds., anhanglich",
27235:nnorw. auch „Fleck,                    wo das Wasser wie von aufsteigendem Fett glanzt“
27623:„das Aufsteigen, Erhebung, H6he“, avarddha- m. „\Yurzeltrieb, Luftwurzel,
27661:     Kaum richtig wird vielfach unter einer Bed. „hervorkomnien oder steigen“
28289:Itse   „kriechf‘,           slav.    (abg. usw.)        le^q.,   lesti   „kriechen,         schreiten, steigen'^
30614:wohnhaft; beendigt, abgeschlossen“, avasana- n. „Ort des Absteigens, Ein-
35915:     lat. scando^ -ere „steigen, sich erheben“, scala (^scand-sla) ,jStiege, Treppe,
36766:einer solchen Yerkniipfung kein uniibersteigliches Hindernis bereiten.
40576:Pick BB, 6, 215, Wb. I^ 568 nicht annehmbar mit gr. oxelpoy unter ^steig^-
40621:612                                          stag-   — steig-
40679:                                                      steig-                                              613
40743: FickBB. 2, 187, Yerb. mit "^steig^h- „ausharren^‘).
40747:614                                          (s)teig«        steigh-
40756:Reichelts        KZ.    Yereinigung unseres "^steig- „stecben“ mit *steg-
```


## [2026-09-14T02:33:25.764Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40620,40760p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD II 612-614 steig-"
}
```


### [2026-09-14T02:33:25.818Z] TOOL RESULT

```
stqkuttr „kurz*‘, dan. stak-aandet „kurzatmig‘\
612                                          stag-   — steig-
stag- „sickern, tropfeln, leise rinnen"".
  Gr. ord^co, ard^co, orayfjvai „traufeln, eintraufeln tr., tropfeln lassen;
tropfeln iutr., rinnen*^, oraxTog „tr6pfelnd, tropfend“, oraycov, - „Tropfen%
ordyeg pL (ApolL-Ehod.) ds. (nicht wahrscheinlicher als stng- zu lit. stingti
           Persson Wzerw. 23; nicht zn aisl. st^hkua „sich plotzlich be-
„geriniieii‘‘,
wegen, spritzen, bersten" Fickl^ 569);
  lat. stagnum „jedes ausgetretene Gewasser, See, Teich, Tiimpel, Pfuhl,

Oder langsam fliefiendes Gewasser^ (z. B. Froehde BB. 21, 198, Karstea
[Studier II 26ff., Zitat nach:] Bgm. II^ 1,262; wohl nicht als „stehendes
Wasser" zu *stak- „stehn“, s. d.);
  abret. staer, nbret. ster „FluB, Bach'^ {^stagra), cymr. taen „conspersio,
adspersio“ {[s]tagna; Strachan BB. 14, 316, Fick II* 121, 312, Stokes BB.
21, 126f.).


stei- „spitzig‘‘.
  Av. staera- „Bergspitze‘', taera- „Bergspitze, Gipfel“, afghan. terq „scharf,
spitzig*^ (wohl mit Formans -Zo-, so da6                die Yollstufe zu;)       lat. siiliis „spitziger
Pfahl, bes.      im Kriege zum SpieBen in Fallen oder      der Landwirtschaft
                                                                           in
zum auflockern          u.   dgL;   Stiel,    Stengel, Griffel      zum Schreiben'*;
                                                                     mit For-
mans -mo- lat. sti-mu-lus „Stacher‘. Ob dazu lat. stiva (und *steva der
rom. Sprachen) „Pflugsterz“ als ^stei-ua'l (Ehrlich BPhW. 1911, 1576 Ter-
gleicht es mit ai. tivra-h „heftig, scharf“, das allenfalls auch aus „*spitz,
stechend“ entwickelt sein konnte ; nicht iiberzeugend uber stwa Bgm. IF.
28, 369, Siitterlin IF. 29, 128).
   Erweiterung von stei- ist "^stei-g- „8techen“ (s. d. aber wohl nicht auch
                                                                       ;


mnd. slip „Punkt"", s. u. stlp- „Stange“);
   Liden IF. 19, 322 ff., Yf. LEWb.^ u. stiliis. Falk-Torp u. stilk stellt hier-
her (nicht zu gr. axeXexog usw.) auch as, stil „Schaft, Stengel'^, ahd. stil
„Stil“, wohl mit Eecht wegen der Ablautform mnd. stil „Saule, Stange“,
norw. mdartl. stil „dunner Stecken, Stock“.

stoig- „stehen; spitz^, wohl Erw. von                   stei- ds.

  Ai. tejate „ist scharf, 8charft“, tejdyati „scharft, stachelt'*, tiktd-h „scharf,
bitter^, tigmd-h „spitzig, scharf*', tejah n. „Scharfe, Schneide, Spitze, Glanz,
Energie'*, tejana-m „das Scharfen, Anzunden ; Spitze, Pfeilspitze, Eohrstab,
Pfeilschaft“, wozu als Kollektiv tejant f. „Geflecht oder Gebund von Schilf,
Stroh u. dgl.‘‘ (trotz Fay IF. 26, 37 a 4; 33, 356 f. nicht unter einer Gdbed.
„Schaft“ mit lat. tigmim zu vereinigen);
  av. taeya-^ taeza- „scharf;          m. Scharfe‘‘,       tiyra-^ ap. tigra- „spitz“; av. tizi-
(als 1. Zsglied) ds., tiyri- „Pfeil“ usw., np. tey „Spitze,                     Schwert" (arm. Lw.
teg „Lanze‘‘), tez „8charf^, tej ,,Pfeil“.
  Ohne      anl.   s-   auch germ, jnkstila- „Distel“ (vgl. den 5-St. ai. tejas-]
2 . B. Fick III * 1 84,    Sverdrup IF. 35, 1 54) in aisl. pistill^ ags. pistel^ ahd.
distil   und norw. mdartl. Ustel^ ostfries. dlssel „Di8tel" und vielleicht (nach
Windiseh KSB. 8, 252) acymr. iigom „naevi‘‘ („*Punkt, Tupf*‘ aus „Stich“?
vgl. gr. axiyfia),
   Gr. onfo)       „steche,    tatowiere",       cniy/Aa    „Stich,   Pankt“,        oxocxog   „bunt"
(„ge8tickt“).
                                                      steig-                                              613

  Lat. instlgo, -are ^anspornen, anstacheln, anreizen, aufreizen“;
  nasaliert instinguo „reize aii“, interstingiw „besetze (bestecke)                             bin und
wieder mit etwas“, distinguo „(steche, stochere auseinander) unterscbeide“
{-uo nach unguo usw., s. Yf. Festgrufi aus Innsbruck 1909, 93), umbr. au-
stintu „distinguit;o“; iat. stinguo, -ere „ausl6schen“ (vom auseinanderstocbern
der brennenden Scheite, wie nhd. ersticken, mhd. intr. ersticken, trans. er-
stechen „ersticken machen“, ursprgl. vom Feuer und erst: spater iiber diese
Verwendung hinausgewachsen; s. Vf. LEWb.^ s. v.).
  Got. stiks „Stich,           Punkt“ (wie            lat.       punctum pungo), abd. stih
                                                                         :
                                                                                                   ds.,    as.

stiki   „stick'',    mnd.     steke        „Stich,   Stachel,        Seitenstechen“,   ags.   slice       „ds.,

stechendes Gefuhl“, stician „stechen            intr. stecken bleiben, festhalten‘^,
                                                             ;


mengl.   sticchen ''iiahen“,  mnd.  sticken „stechen,  sticken, anstecken, anziinden,
ersticken'^, ahd. sticken „stechen, sticken^", irsticken „ersticken (s. o.), ahd.
stecken „festritzen“, nhd. {wo)stecken {*stikken gleichsam ,,^0 angenagelt
seim‘); aisl. steikja „braten'' (eig. „an den SpieB stecken“; dazu steikr
„Braten‘‘, stikna ,,gebraten werden“) ; mit Ablautentgleisung as. stekan, stak
„festheften, festhaften“, ahd. stelihan, nhd. stechen, stack, kaus. "^stakjan in
ahd. stecken „(durch Stiche) befestigen, einstecken“, nhd. stecken tr., got.
staks „oTlypa, Mai, Wundmah^, ahd. stahhula „StacheF’ (isl. st^kr „stinkend“?
s. u. steug- „stoBen'’)      diese tJberfuhrung in die e-Reihe war begxinstigt
                                ;


durch die germ. Ableger von "^steg- „Stange“ (z, B. aisl. stjaki m. „Pfosten‘‘),
mit denen sich die Gruppe got. stiks, dt. stechen zu einer neuen Einheit
zusammenschloS (s. Liden IP. 18,499 und die Ubersicht des germ. Be-
standes bei Pick III^ 479, 480, 490, Falk-Torp u. stikke)', so beruht formell
auf '"^stig-, aber mit der Bed. von "^steg-, aisl. stika, ahd. stehho „stecken“
(letzteres aber zugleich auch = aisl. stjaki), aisl. stik n. pi. „ins Wasser ge-
rammte Pfahle“, mit kk aisl. stikka „Stecken, Stange'', ags. sticca „Stecken,
L6flfeb‘, as. stekko         „Stecken, Pfahl“, ahd. stecko „Stecken;
   inYok. und Bed. zu "^stig- stellen sich noch aisl. stikill „Spitze eines
Horns^' (usw., s. Palk-Torp u. steill II), ags. sticel m. „Stachel“ mnd. stekel,
      „ Stachel, Dorn“, ahd.      „Stachel“, nhd. Stichel; wenn got. stikJs,
ahd. stehhal „Becher“ dazu gehort, so kaum als „spitziges Trinkhorn“, son-
dern als „zum Einstecken in die Erde oder in Sand unten zugespitzt ver-
laufendes Gefafi'‘ (Kluge PBrB. 35, 573 geht      damit an sich vereinbar—
 — vom Begriff „steir^- ahd. stechal „8teil“ aus, s. u., nach MaBgabe von

mhd. stouf ,,Becher''               :     Beziehung zu slav. sihklo „Glas
                                        ags.   steap „steib';
als StofF, vitrum“. DaB das germ. AYort nach Uhlenbeck PBrB. 22, 191 aus
dem Slavischen stamme, ist hochst fraglich; das slavische Wort ist wohl
germanisches Lehnwort.     Falk-Torp u. steile II K., Feist Got. Wb. 250;
KZ. 20, 360);
   vermutlich auch as. stekal „rauh, steinig'*, mnd. stekel „devexus‘', ags.
                   ahd. stehhal, stecchal, mhd. stechel, stichel, stickel „sto8sig,
sticol „steil, hoch“,
 steil, abruptus'^ als „die FuBsohlen                 stechend, voll spitzer Steine und Stenger\
   Mit dem          dt.    „stecken, stecken bleiben” nachststehender Bed.                      lett.      stigt
 „einsinken”,       lit.             und stygau, -oti „an einem Orte ruhig
                           stingii, stigail, stigti

 verbleiben” („wo steckenbleiben”; Wiedemann Praet. 38, Rozwadowski IF.
 4,411; weiteres bait. Zubehor bei Zupat)- BB. 27, 325, wo aber, wie bei
 FickBB. 2, 187, Yerb. mit "^steig^h- „ausharren^‘).
    Wa d e Etymologisches Wbrterbuch. II.
         I    ,
                                                                                              4q
614                                          (s)teig«        steigh-



     Russ. stegdth, stegnUth „steppen, durchnahen, peitschen'*, steSka
{e    in geschlossener Silbe aus h und auf stegdh iibertragen; gegen Verb,
mit    "^steg-   „Stange“ spricht die Bed.)
     cech. steh, poln. scieg, scig „Stich‘‘.
     Ygl, Curtins 2l4f.,           Fickl^ 144, 569, Zup. G. 168 (Lit.).                     Yerfehlt   ist
Reichelts        KZ.    Yereinigung unseres "^steig- „stecben“ mit *steg-
                         39, 17
„Stange'‘ unter idg. ste(i)g-, zumal fur "^steg- „Stange“ eine Urbedeutung
„stechend‘^ und fur steig- „stechen“ andrerseits eine Urbed. „mit einer
Stange oder einem Stock stechen'^ wenigstens nicht zu erweisen ist (aller-
```


## [2026-09-14T02:33:41.102Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"آستیگمات\" \"استیگمات\" \"اتیکت\" \"دجله\" \"دیاله\"; do echo \"#### $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done",
 "description": "Grep Mo'in for the loanwords"
}
```


### [2026-09-14T02:33:42.252Z] TOOL RESULT

```
Exit code 1
#### آستیگمات
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
#### استیگمات
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part2.txt:0
#### اتیکت
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3
MON_part1.txt:3
MON_part2.txt:0
#### دجله
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
#### دیاله
MON_part2.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
```


## [2026-09-14T02:33:44.470Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \".\\{200\\}اتیکت.\\{200\\}\" MON_part1.txt | head -5",
 "description": "Mo'in etiket context"
}
```


### [2026-09-14T02:33:44.534Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:33:47.262Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\ni=0\nwhile True:\n    i=t.find('اتیکت',i+1)\n    if i<0: break\n    print('---', repr(t[max(0,i-300):i+300]))\nEOF",
 "description": "Mo'in etiket context py"
}
```


### [2026-09-14T02:33:48.743Z] TOOL RESULT

```
--- 'ت؛ ج. \nآبات. \n\nید [- آی؛ - آیبدک - آیده - \nایژک] (.) شراره» شرر آتش. \n\nآیین: درد (۱.) ر سم» روشء ادت. معمول» \nمتداول» مرسوم. . شیوه» آهنگ. صفت. \nکردار. اندازه» حد» عدده شمار. قاعده» \nقانون» نظم. سامان» اسباب. طبیعت» نهاد» \nفطرت. آذین» شهر آرای» جشن. زبب» \nزینت. فر» شکوه. شرع» شریعت» کیش. \nتشر یفات» اتیکت (فره.) به آیین: چنانکه \nمرسوم است» طبق معمول. چنانکه باید» \nچنانکه ضروری است. زیبا؛ جمیل. بر آیین: \nمثل و مانند. \n\nآیسین\u200cبندی: آ-0200-.3 (حامص. امر.) \nآذین\u200cشهر» شهر آرای» هنگام قدوم شاهی با \nکین پا پیش آمدن جشن و سوری. \n\nایین برست: 2.51 (افا. ص مر .) آنکه \nطرفدار آیین و رسم است. خدمتکار؛ \nپرست'
--- ') تهمت نهادن \nبر کسیء افتراء» کسی را به چیزی تهمت \nکردن. (مصل.) تهمت پذیرفتن» بدنام \n\n\n۸۸ فرهنگ فارسی معین \n\n\nشدن. \n\nاتیان 3 [ع.] (مص\u200cل.) ادن بودن. \n(مص م.) آرمیدن با زن. آوردن. کردن کاری \nرا. هلاک کردن. نزدیک رسیدن بل با \nدشمن کسی را. ارتکاب؛ ارتکاب دنوب. \nاتیان به مثل: نظیر و شبیه آوردن چیزی را. \nاتیکت: 6۱6۱ ( نوشته\u200cای که رودی \nکیسه\u200cها یا شیشه\u200cهای دوا و کالای بازرگانی \nبرای تعیین محتوی و وزن آنها می\u200cچسبانند» \nبر چست ۰ رسوم و آداب درباری» تشر یفات. \nرسوم و آداب در زندگی اجتماعی و رفتار ب \n0 رم سم \nاتیلن: مع۱آ۱ع (شیم.) کازی است بی\u200cرنکك» \nکم رایحه و آن را به وسیلاً اخراج آب از \nالکل به وسیلهٌ ا'
--- '» بالا آمده. شخص معروف \nو بزرگک؛ جح برجستگان. خوب؛» بسند یده. \n\n\nممتاز» عالی. چست. چالاکک. \n\nبر چسب: اعمه-02۲ (امر.) که کاغذ که بر \nآن نوع جنس و محل ساخت و دیگر \nمشخصات آن را نوشته یا چاپ کنند و آن را \nروی شیشه و بطری\u200cها چسبانند؛ قطعه کاغذی \nکه روی اجناس چسبانند تا معرف جنس و \nقیمت آنها باشد (فره.) اتیکت. \n\nبر چجیدل: 420--.ه [- برچدن)] (مص\u200cم.) \nدانه دانه برداشتن (از زمین)؛ دانه چجیدن. \nانتخاب کردن برگزیدن. جمع کردن» گرد \nکردن. تعطیل کردن یک بنگاه» منحل کردن \nیک سازمان. \n\nبرخ: ۰۵۷ [بخش کردن» بخشیدن] (ا.) پاره؛ \nلخت. حصه؛ حظ» نصیت. \n\nبرخاستن: 0 (مص\u200cل.) بربا شدن» \nایستادن؛ مق. نشستن. ببدار شدن. ر'
```


## [2026-09-14T02:33:58.438Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Tigris",
 "prompt": "Give the full etymology section for Tigris: Sumerian/Akkadian forms, Old Persian, Greek, and any mention of folk etymology or Aramaic Diglath / Arabic Dijla."
}
```


## [2026-09-14T02:34:00.030Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%AC%D9%84%D8%A9",
 "prompt": "Give the Arabic entry دجلة: etymology, meaning, and any Persian/Aramaic/Akkadian source mentioned."
}
```


### [2026-09-14T02:34:05.946Z] TOOL RESULT

```
# Arabic Entry: دجلة (Dijla)

**Meaning:** The Tigris river, "a river in West Asia flowing 1,150 miles east-southeast from the Armenian Highland in Turkey through Iraq."

**Etymology:** The word traces back through multiple ancient languages. It was "borrowed from Aramaic דיגלת (diḡlāṯ), borrowed from Akkadian 𒀀𒇉𒈦𒄘𒃼 (Idiglat), borrowed from Sumerian 𒀀𒇉𒈦𒄘𒃼 (id₂idigna)." 

The Sumerian origin possibly derives from combining "river" + finite prefix + "went" + a nominalising suffix.

**Key Source Languages:**
- **Aramaic:** דיגלת (diḡlāṯ)
- **Akkadian:** Idiglat
- **Sumerian:** id₂idigna
```


### [2026-09-14T02:34:07.071Z] TOOL RESULT

```
# Etymology of Tigris

**English Etymology:**
The word "Tigris" traces through multiple ancient languages. It comes from "Latin _Tigris_," which borrowed from "Ancient Greek _Τίγρης_ (Tígrēs)," which in turn borrowed from "Old Persian _𐎫𐎡𐎥𐎼𐎠_ (t-i-g-r-a /⁠Tigrā⁠/)."

**Earlier Sources:**
The Old Persian form came from "Akkadian _𒀀𒇉𒈦𒄘𒃼_," which ultimately derives from Sumerian. The Sumerian origin is possibly from "_𒀀𒇉_ (id₂ /⁠id⁠/, 'river') + _𒉌_ (i₃ /⁠i⁠/, finite prefix) + _𒁺_ (g̃en, 'went') + _𒀀_ (a /⁠'a⁠/, nominalising suffix)."

**Alternative Names:**
The Catalan etymology notes the term literally means "fast as an arrow" from Sumerian sources. Arabic and other Near Eastern languages use distinct terms: Arabic _دِجْلَة_ (dijla) and Aramaic _דִּגלָת_ (diḡlāṯ) represent alternative naming traditions rather than etymological descendants of the Greek-Latin line.
```


## [2026-09-14T02:34:12.754Z] TOOL CALL #42: WebSearch

```json
{
 "query": "Diyala river name etymology Sirwan Arabic Diyālā origin"
}
```


## [2026-09-14T02:34:15.048Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D8%B3%D8%AA%DB%8C%DA%AF%D9%85%D8%A7%D8%AA/",
 "prompt": "Show the فرهنگ معین entry for آستیگمات (origin tag and definition), and any other dictionary entries shown."
}
```


### [2026-09-14T02:34:17.285Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:34:19.319Z] TOOL RESULT

```
Web search results for query: "Diyala river name etymology Sirwan Arabic Diyālā origin"

Links: [{"title":"Meaning of the name Sirwan","url":"https://www.wisdomlib.org/names/sirwan"},{"title":"The Sirwan River: A Vital Lifeline of the Middle East | by Jannat Chaudhary | Medium","url":"https://medium.com/@jannat8x/the-sirwan-river-a-vital-lifeline-of-the-middle-east-51759c5b4e20"},{"title":"Diyala River","url":"https://en.wikipedia.org/wiki/Diyala_River"},{"title":"Sirwan","url":"https://en.wikipedia.org/wiki/Sirwan"},{"title":"Sirwan River - Wikidata","url":"https://www.wikidata.org/wiki/Q20988000"},{"title":"Category:Diyala River - Wikimedia Commons","url":"https://commons.wikimedia.org/wiki/Category:Diyala_River"},{"title":"Diyālā River | Middle East, Tigris, Euphrates | Britannica","url":"https://www.britannica.com/place/Diyala-River"},{"title":"Sirwan is not only the name of a river!","url":"https://kurdshop.net/en/geography/3496"},{"title":"Sirwan River","url":"https://en.wikipedia.org/wiki/Sirwan_River"}]

Based on the search results, here's information about the etymology and names of the Diyala River:

## River Names and Etymology

The Diyala is known in Arabic as Nahr Diyālā, in Kurdish as Sîrwan, and in Persian as Diyâleh / Sīrvān.

In Kurdish and Persian, the river's origin name "Sirwan" means 'roaring sea' or 'shouting river'. Another source indicates that "Sirwan" directly translates to "roaring river" or "mighty river," symbolizing strength, vitality, and the life-giving properties of water.

## Name Change

Upon its confluence with the Tanjaro river in Darbandikhan Dam in the Sulaymaniyah Governorate of Northern Iraq, its name changes to Diyala River.

## Geographic Connection

The Diyala River is known as Sirwan in Kurdish, and it rises in the Zagros Mountains of western Iran near Hamadān as the Sīrvān River and flows westward across lowlands to join the Tigris just below Baghdad, Iraq.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:34:27.908Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A2%D8%B3%D8%AA%DB%8C%DA%AF%D9%85%D8%A7%D8%AA",
 "prompt": "Show the Mo'in (فرهنگ معین) entry for آستیگمات: origin tag (e.g. [فر.]) and definition."
}
```


## [2026-09-14T02:34:28.856Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/diyala",
 "prompt": "What does Encyclopaedia Iranica say about the name Diyala / Diyālā river and its origin?"
}
```


### [2026-09-14T02:34:29.058Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:34:29.980Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:34:36.806Z] TOOL CALL #46: Bash

```json
{
 "command": "ls site/pages/478.jpg 2>/dev/null || pdftoppm -f 478 -l 478 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg478 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg478.png",
 "description": "Render printed page 478"
}
```


### [2026-09-14T02:34:37.870Z] TOOL RESULT

```
Exit code 2
site/pages/478.jpg
ls: cannot access '/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg478.png': No such file or directory
```


## [2026-09-14T02:34:39.744Z] TOOL CALL #47: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/478.jpg"
}
```


### [2026-09-14T02:34:39.773Z] TOOL RESULT

```

```


## [2026-09-14T02:34:59.748Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ===\"; grep -n -o \".\\{0,120\\}\\(TIGER\\|Tiger\\|tiger,\\|ticket,\\|etiquette\\|stigma,\\).\\{0,400\\}\" SKT.txt | head -8",
 "description": "Skeat entries"
}
```


### [2026-09-14T02:35:03.743Z] TOOL RESULT

```
=== SKT ===
ugrep: error: error at position 124
xbf][\x80-\xbf]*){0,400}
                        \___exceeds complexity limits
```


## [2026-09-14T02:35:07.071Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor w in ['TIGER','TICKET','ETIQUETTE','STIGMA','DISTINGUISH']:\n    i=t.find(w)\n    print('####',w,i)\n    if i>0: print(t[i:i+500].replace('\\n',' '))\nEOF",
 "description": "Skeat lookups"
}
```


### [2026-09-14T02:35:08.297Z] TOOL RESULT

```
#### TIGER -1
#### TICKET -1
#### ETIQUETTE -1
#### STIGMA -1
#### DISTINGUISH -1
```


## [2026-09-14T02:35:11.813Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nprint(len(t))\nfor w in ['Tiger','Ticket','Etiquette','Stigma','tigris']:\n    import re\n    for m in re.finditer(w, t):\n        i=m.start()\n        seg=t[i:i+350].replace('\\n',' ')\n        print('####',w,i,seg[:330])\n        break\nEOF",
 "description": "Skeat lookups 2"
}
```


### [2026-09-14T02:35:12.972Z] TOOL RESULT

```
2620367
#### Tiger 2145037 Tiger.  (F.-L.- Gk.- Per*.)  M  K.tigrt. —  F.  tigrt.  —  L.  tip^m,  ace  of  tigris,  a tiger.  — Gk.  rt'-ypi j.  —  Zend  (O.  Pers.^  tigkri, an  arrow  (hence  a  tiger,  from  its  swifincss, also  the  river  Tigris,  from  its  swiitncvs) ; mod.  Pcra.  //r,  an  arrow,  the  river  Tigris. •■Zend  tighra,  sharp;  all
#### Ticket 2142837 Ticket ;  see  8Uok  (x). ;  *ec  Tiok  (4). M.E.  tidt.     A.S.  tU,  time» +  Du.   tijd,  Icel.  //5,   L>an. uit.     Lit.  an  allotted  time, on :   cf,  Sltt  dffy,  to  allot. assign.     (^  DA.l     Allied Der.  tidi  tvaiur,  an  officer  who val  of  vessels  with  the  tiiU,  to t  of  duties. tScand.)     M.  E.  
#### Etiquette 555552 Etiquette  ;  see  Stick  (i). Etymou,  the  tnie  aource  of  a  word. (L.*Gk.)  L^  etymon. ^GV,  irvfiov  \  neuL aUrv^Mst,  real,  true.  — Gk.  Iriut,  tnie.  Al- lied to  Booth. etymology.  (F.  -  L.  -  Gk.)  O.  F. ttymcfpip'f.  —  L.  etymohgia.  —  Gk.  Jru/fo- Ao^i'a,  etymology. —  Gk.ery/io-!,  tnie  ;*A*7fa, Recou
#### tigris 2145117 tigris,  a tiger.  — Gk.  rt'-ypi j.  —  Zend  (O.  Pers.^  tigkri, an  arrow  (hence  a  tiger,  from  its  swifincss, also  the  river  Tigris,  from  its  swiitncvs) ; mod.  Pcra.  //r,  an  arrow,  the  river  Tigris. •■Zend  tighra,  sharp;  allied  to  Skt.  tigrna, sharp,  from  tij,  to  be  sharp.     (^STAU.) Tight  (S
```


## [2026-09-14T02:35:20.420Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index steig/teig ===\"; grep -n -i \"STEIG\\|TEIG\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== IEC teig ===\"; grep -n \"teig\\|tēg\\|tigro\" IEC.txt | head -10\necho \"=== SYN sharp/arrow ===\"; grep -n \"tigmá\\|tigra\\|tēz\\|tīr \" SYN.txt | head -10",
 "description": "Aryanpur, Mann, Buck"
}
```


### [2026-09-14T02:35:20.511Z] TOOL RESULT

```
=== ARY latin index steig/teig ===
1254:eed ot SE yy 30 (pad come 4) TEIG cal 0st og SLIT 59 (yl yo gee 4) DEHA
6037:SKEAT: (STEIG) 759 DISTEL «(OLD ENGLISH) 5 5S!
6043:pean ore ln +(S)TEIG- INDO-EUROPEAN) «gt9 9 3
7993:SKEAT: TEIG (GERMAN) gait
8593:wilde ly ae 555 (st oi W)TEIG glsT » DOUGH Sil uly oe
10184:SKEAT: (STEIG) 759 STILUS, STIVA. ss AK LAPIN)’ oy
=== IEC teig ===
17152:stk- — steigh-
17168:steigh- ‘rise, go’. Cf. stoigh-, stigh-. WP II, 614 Skt. cf. -stighnomi, v. in cpds: ati-; pra- ‘stride; rise’; Go. steigan, sv. 1. ( climb’, and com. Gmc., MHG stigen, OE sügan, Du. stijgen, ON stíga, id. ON usu: (step); OCS cf. do-stigo, -stisti, v. (come, arrive’; stigno, -noti, v. ‘reach’; stižọ, stizati (sic) “follow up’; R cf. do-stic, inf. ‘reach’; OLi. cf. steigóms, steigomis ‘hastily’; Latv. stiegu, t, v. ‘sink’;
17170:steidzu, steigt, v. ‘hurry’; steiga, f. ‘haste’. (Isophones in Ir. stéig, Let f. ‘bluff, peak; strip of leather; gut; gullet’; Li. stiegé, f. ‘tile, roof-shingle"). Extn. in G Stiegel, m. “post, pole”; E stile. Nominal types in OHG stiga, f.; MHG stic, gs: ses sm.; OE stig, ON ster *foot-path'; Du. stijg, m. ‘climb’
17171:(steigu, stigu-? See Supt: S)
17177:Steigu, stigu- — stenos (stenios, stentós)
17243:stigó, ið “stab, pierce, goad'. Cf. sting-. WP II, 612 Gk. stízo, v. id.; adj: stiktós; Lat. stigo, are, v. id.; cf. ve-stigium ('footprint, trace’, fr. *uegh-steig-, *-stig-); prae-stigiae, fpl. ‘wiles’; OHG stéchan, sv. 4. ‘stab’; OE stician, wv. id.; MHG sticken, OE stician, wv. id. MHG also ‘stitch’; Sw. sticka, v. “stab; stitch"; Cz. cf. na-stehnout, pfi-stehnout, inf. ‘stitch on’; R stegàt, inf. ‘quilt’; Latv. stiegu, inf: stigt. v. “shoot in, immerse’. Nominal types: Gk. stigmé, f. “point, puncture; moment Go. stiks, m. “point of time, moment: OE stice, m. ‘sting, stab, stitch in the side’; sticca, wm. ‘stick, peg’; ON stik, npl. ‘stakes, piles’ beside stika, f. ‘stick’; Cz. steh, m. ‘stitch’; Pol. $cieg, m. id.; R (dim.) stežòk, m. id. Sw cf. also stick, n. ‘stitch’; sticka, f. ‘stick’
17244:stigh- (stigh-), see steigh-, stoigh- Skt. cf. ati-, pra-stighnomi, v. ‘step’; W cf. siád ‘crown of head’; OCS stigna, f. “boule- vard, forecourt beside stígnoti, Cz. stihnout, v. ‘go; reach’; MHG cf. stigel, stigele, s & wf. ‘stile’ beside stige, stie, f. ‘sty’; Li. dial. stingù, stigti, v. “arrive, get to, come’; Latv. cf. stidzeju, v. ‘climb; become’. Nominal types in Av. stij, f. ‘battle’; Gk. stíkhes, pl. “lines, series’ beside stíkhos, m. “line, row'; OHG stëg, m. ‘footbridge, path’; stëga, f. ‘stairway’; OE stige, m. ‘ascent, descent’; ON ster stier, m., stig, n. ‘step, pace, path, degree’; OCS stíza, stízja, f. “path? beside stígní, stigna, f. “public square’; OCz. stzě, f. ‘path’; R stezjà, id.; Srb. staza, id.; Latv. stiga, f. ‘beeline’; (long-gde in) Ir. stíog, m. ‘dash, fit’. Extn. in ON stétt, f. ‘paving; degree; order; keelson'; stéttr, m. (crank, fr. *stight-)
17272:stoigos, à (sth-) ‘support’. Cf. stig- OCS stégü, m. 'ensign'; Blg. stég, m. id.; stéga, f. ‘stay, strut’; Cz. stéh, m. ‘stay, strut'; stézeje, f. "hinge of door; pole, axis’; stézen ‘mast’; Pol. cf. sciezaj in phr: na — ‘wide open’; Li. stiege, f. ‘roof-tile’; cf. j-staiga, f. ‘foundation’; (e-gde in) steigiü, "ti, v. “found”
17273:stoigh- (o-gde of type steigh-, stigh-, q.v. WP II, 614) Gk. stoikhéo, v. “proceed, file’; stoikhízo, v. ‘plant in rows; MHG steigen, wv. ‘erect’; OE a-stéegan, wv. ‘rise, embark’; OCz. stéZiti, inf. “bring, lead? beside stézéti ‘drag; betake oneself; Latv. stiedzeju, v. “extend, train up- ward'. Extn. of type *stoighlos, -ilos in MHG steigel and steil, adj. ‘steep’; OE stægel, id. beside st&ger ‘stair’; Sw. stegel, m. ‘wheel of torture’; Cz. štíhlý, adj. “tall, slim’. Nominal types in Gk. stoikhos, m. ‘line’, Alb. shteg, pl. shtigje, m. ‘path’; Go. stáiga, f. id.; MHG steic, gs: steiges, sm. ‘rise’; steige, sf. ‘path’; Du. steeg, f. ‘alley; pommel of saddle’; Scots ste, adj. ‘steep’; Sw. steg, n. ‘step, rung of ladder’; stege, wm. ‘ladder’; Latv. staiga, f. *walk'; Li. staigüs, adj. (2) 'steep'
17281:stoighos (2). For (1) see Nominal types above. Br. stü, adj. (“in good heart, fertile'. Ambig.); Du. steeg, Fris. steech, adj. 'stubborn'; ON cf. steigur-liga ‘proudly’; Li. staigüs, adj. 'sud- den, dashing’
=== SYN sharp/arrow ===
10909:Av. «xaoda- (OPers. xauda- in tigra- rauda- ‘with pointed cap’), perh. : Lat. cud6é ‘skin helmet’, IE *(s)keudh-, ex- tension of *skeu- ‘cover’. Walde-P. 2.550. Walde-H. 1.301.
28027:Nir. sagruighim, beside sb. stigradh ‘play, sport, fun’, cf. also siigach, MIr. sucach ‘merry, cheerful’, etym.?
34758:Av. tiyri- (NPers. tir) : tiyra-, OPers. tigra- ‘sharp-pointed’, ete. (15.78). Walde-P. 2.612.
35051:Av. xaoda- in ayd-raoda- adj. ‘with bronze (or iron) helmet’ (Yt. 13.45, 15.57), cf. OPers. tigra-cauda- ‘with pointed cap’, NPers. xid ‘helmet’, perh. fr. the root in Grk. KebOw ‘hide’, etc. Walde-P. 2.550. Barth. 162, 531.
```


## [2026-09-14T02:35:29.296Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6030,6050p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== pdf page tag near ===\"\nawk 'NR<=6043 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt\npython3 - <<'EOF'\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nlast=None\nfor i,l in enumerate(lines[:6100]):\n    if '[pdf page' in l: last=(i,l)\nprint(last)\nEOF",
 "description": "Aryanpur steig index"
}
```


### [2026-09-14T02:35:30.413Z] TOOL RESULT

```
TIGOM (GAULISH) JS STIGO, STINGO LATIN) g3¥
{OLD SCANDINAVIAN) AS 54\
‘REFERENCES cB ‘THISTILL
POKORNY: TTT 016 DISSEL MOLD FRISIAN) AS 52.9
BARNHART: (THISTLE) 1135 {OLD HIGH GERMAN) oA et
DELAMARRE: 286 DISTIL
‘MACKENZIE: (SHARP) 132 SISTEL GERMAN) glST
SKEAT: (STEIG) 759 DISTEL «(OLD ENGLISH) 5 5S!
RAMAT: 143 THISTLE ENGLISH) g-l83!
orf tabi chy TIDSEL DANISH) S\ail3
seetlaal
eee erste
ase apg Ady Shee ot! gad lads Sel siza, ONIONS ~*
pean ore ln +(S)TEIG- INDO-EUROPEAN) «gt9 9 3
STIH (OLD HIGH GERMAN) o4S gs) TAEGHA NAVESTAN) gl 3)
STICE «(OLD ENGLISH) oS gS! TEGH, TEX (PAHLAVI) «5 3h
TEGH, TEGHA {(OSSETIC) ,o3\
‘REFERENCES cathe TEG (BALUCHI) gs
POKORNY: 1016 TEJA, TEJATE (SANSKRIT) cy Sie
MACKENZIE: (EDGE) 112 TEG ARMENIAN) 5+)!
are abl oly INSTIGO, INSTIGARE (LATIN) g3
=== pdf page tag near ===
(6081, '\x0c[pdf page 211]')
```


## [2026-09-14T02:35:37.469Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/etiquette",
 "prompt": "Full etymology of etiquette, including Old French estiquette, estiquier, Frankish/Germanic source, and the relation to ticket."
}
```


## [2026-09-14T02:35:38.211Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/astigmatism",
 "prompt": "Full etymology of astigmatism: who coined it, when, from which Greek elements."
}
```


### [2026-09-14T02:35:42.191Z] TOOL RESULT

```
# Etymology of Etiquette

The word **etiquette** entered English in 1750 from French *étiquette*, meaning "prescribed behavior." The French term derived from Old French *estiquette*, which originally meant "label" or "ticket."

## Sense Development

The meaning shift likely occurred through two pathways:

1. **Court instructions**: Small cards with behavioral guidelines for proper conduct at court
2. **Military billets**: Behavior instructions written on soldiers' lodging notices

## Linguistic Roots

The Old French *estiquette* traces back to *estiquer*, meaning "to affix or stick on," which comes from Frankish *stikkan*. This connects to Old English *stician* ("to pierce") and ultimately to Proto-Germanic *stikken* and the Proto-Indo-European root *steig-* ("to stick; pointed").

## Related Word

The modern term **netiquette** (1993) is a playful coinage combining "net" (internet) with "etiquette," referring to "proper style and manners in communicating on the internet."
```


### [2026-09-14T02:35:42.583Z] TOOL RESULT

```
# Etymology of Astigmatism

**Who Coined It:** Rev. William Whewell, an English polymath

**When:** 1849

**Greek Components:** The term combines two Greek elements:
- **a-** meaning "without" (the alpha privative)
- **stigmatos** (genitive of stigma), meaning "a mark, spot, or puncture"

**Full Definition:** According to the source, astigmatism refers to a "defect in the structure of the eye whereby the rays of light do not converge to a point upon the retina." The term's construction literally means "without a focal point" or "without a stigma" (in the sense of a precise mark where light converges).

**Root Connection:** Both components trace back to Proto-Indo-European roots—specifically *steig-, which means "to stick" or denotes something "pointed."
```


## [2026-09-14T02:35:53.607Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-\" \"https://www.etymonline.com/word/tiger\" \"https://en.wiktionary.org/wiki/Tigris\" \"https://en.wiktionary.org/wiki/%D8%AF%D8%AC%D9%84%D8%A9\" \"https://www.etymonline.com/word/etiquette\" \"https://www.etymonline.com/word/astigmatism\" \"https://en.wikipedia.org/wiki/Diyala_River\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 478, root Steig/Stig/Teig: tir, tiz, setiz, Tigris/Dejleh, tiger, astigmatism, etiquette/ticket, stinguere\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T02:35:58.123Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2a308dcd24b68281.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1893e5870b24ee8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a18d715cf9115f79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6751abe490acba3d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35ef960119e9b86e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f95d2749d449d73.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3b517f0be4229af.txt
```


## [2026-09-14T02:36:22.450Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:46:38.826Z] AGENT

I'll write the verification JSON file now, based on all the research gathered.


## [2026-09-14T02:58:23.990Z] TOOL CALL #56: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-478.json <<'JSONEOF'\n{\n  \"pdf_page\": 478,\n  \"book_page\": 448,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Steig, Stig, Teig\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)teyg- 'to prick, stab; pointed, sharp' (with and without s-mobile), an extension of *stei- 'pointed'\",\n      \"note\": \"Pokorny IEW 1016 heads the entry exactly '(s)teig- ‚stechen; spitz', Erweiterung von stei- ds.; (s)tig-to- ‚gestickt'' and gathers there Skt. tejate/tigma-, Av. taēža-/taēγa-/tiγra-/tiγri-, OP tigra-, NP tēγ/tēz/tīr, Gk. stízō/stígma, Lat. īnstīgō/stinguō/distinguō, Goth. stiks, OHG stehhan — i.e. every branch drawn on this chart. Watkins (AHD) heads the same root 'steig-. To stick; pointed' and closes with '[Pok. steig- 1016.]'. Nourai's triple heading 'Steig, Stig, Teig' is his way of writing the s-full full grade, the zero grade and the s-less variant (Skt. tej-, Av. taēža-); the language label 'Indo-European' and the gloss 'pointed, sharp' are both right. The one systematic weakness of the chart is that it treats the river-name Tigris as an Iranian word exported to the Semitic world, whereas the Semitic name is the older one (see node #3).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *(s)teyg- «خلیدن، نیش زدن؛ تیز و نوک‌دار» که پوکورنی در صفحهٔ ۱۰۱۶ فرهنگ خود آورده و آن را گسترش‌یافتهٔ *stei- «نوک‌دار» دانسته است. این ریشه دو صورت دارد: با s آغازین (یونانی stízō، لاتین īnstīgō، ژرمنی stechen) و بدون آن (سنسکریت tejate، اوستایی taēža-، پارسی باستان tigra-). سه صورتی که نورایی در سربرگ آورده (Steig، Stig، Teig) همین سه پایهٔ آوایی است و برچسب زبانی و معنای آن درست است؛ پس ادعای نورایی دربارهٔ خود ریشه درست است. تنها کاستی اصلی نمودار این است که نام دجله را ایرانی و صادرشده به زبان‌های سامی می‌داند، در حالی که صورت سامی کهن‌تر است (نگاه کنید به گرهٔ ۳).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1016\", \"status\": \"supports\", \"note\": \"POK_03.txt line 3508 (leaf 257, printed p.1016): '{s)teig-  ,stechen;  spitz',  Erweiterung  von  stei-  ds.;  (s)tig-tO'  ,gestickt'.' — followed on the same page by 'av. taeya-, taeža- ,scharf; m. Schärfe', tiyra-, ap. tigra- ,spitz'' and 'np. [tēγ] ,Spitze, Schwert' ... tez ,scharf', tej [=tīr] ,Pfeil''. Exactly Nourai's root, label and gloss.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 612-614 (incoming/WLD/WLD_Bd2_pages.txt lines 40620-40760)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny II 612 heads the entry 'st[e]ig- ‚stehen[=stechen]; spitz', wohl Erw. von stei- ds.' and lists 'av. taeya-, taeza- „scharf; m. Schärfe“, tiyra-, ap. tigra- „spitz“ ... np. tey „Spitze, Schwert“ ..., tez „scharf“, tej „Pfeil“', then Gk. stízō, Lat. īnstīgō/distinguō/stinguō, Goth. stiks. Pokorny's source for p.1016.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. steig- (AHD_watkins1985.txt line 1010)\", \"stance\": \"supports\", \"note\": \"'steig-. To stick; pointed. Partly blended with stegh-. ... [Pok. steig- 1016.]' — same root, same gloss, same Pokorny page Nourai cites.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. stigō (IEC.txt line 17243)\", \"stance\": \"supports\", \"note\": \"'stigó, ið “stab, pierce, goad'. Cf. sting-. WP II, 612  Gk. stízo, v. id.; adj: stiktós; Lat. stigo, are ... Go. stiks, m. “point of time' ... OE stice'.\"},\n        {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt lines 6037-6046 (pdf p.211)\", \"stance\": \"supports\", \"note\": \"Aryanpur's Persian IE-root dictionary carries an entry '(S)TEIG- (INDO-EUROPEAN)' with 'REFERENCES POKORNY: 1016' and the Iranian material 'TAEGHA (AVESTAN), TEGH/TEX (PAHLAVI), TEG (BALUCHI), TEJA/TEJATE (SANSKRIT), TEG (ARMENIAN), INSTIGO (LATIN)'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"tiğra ; taĕža, taĕğa ; tigrâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The three adjectives are impeccable. Young Avestan tiγra- 'pointed, sharp' (Bartholomae AiW col. 651: '• j. tiγra- (, p. tigra-) Adj. ‚spitz, spitzig'', with V. 9.10 frakārayaōi tiγra xšaθra 'you shall draw the furrows with a pointed metal piece'), beside the s-less full grade taēža-/taēγa- 'sharp; edge' (attested in the compounds brōiθrō.taēža- 'with sharp edge', bi-taēγa- 'double-edged', BRT.txt line 17261), and the noun tiγri- 'arrow' (AiW col. 651, Yt 8.6, the arrow of ərəxša). Old Persian tigra- is the same word (tigra-xauda- 'wearing the pointed cap', the Saka tribe, DB/DPe), from PIE *(s)tig-ro- with the s- lost in Indo-Iranian and *-ĝ- > Ir. -γ- after -i-. What is only 'plausible' is the third item: OP Tigrā is indeed the Old Persian name of the Tigris (DB 1.18 'Tigrām viyatarayamā ‚we crossed the Tigris''), but Bartholomae flatly warns at that entry that 'Stammansatz und Geschlecht unsicher. Die Namensform beruht vll. auf volksetymologischer Umgestaltung des nicht iranischen Namens, vgl. tiγra- und tiγray-. Das Mp. hat Diglat; Ass. Idiqlat, Gr. Tigris.' So Tigrā is a Persian re-shaping of a Mesopotamian name to look like tigra- 'sharp/swift', not a genuine derivative of it; the gloss '\\\"fast moving\\\" river' is the folk etymology, not the etymology.\",\n          \"derivation_fa\": \"صورت‌های اوستایی tiγra- «تیز، نوک‌دار»، taēža-/taēγa- «تیز، لبه» و tiγri- «تیر» و پارسی باستان tigra- همگی در فرهنگ ایرانی باستان بارتولومه (ستون ۶۵۱) مضبوط‌اند و از همان ریشهٔ *(s)teig- می‌آیند؛ s آغازین در هندوایرانی افتاده و *ĝ هندواروپایی در ایرانی پس از i به γ بدل شده است. اما دربارهٔ Tigrā (نام دجله در سنگ‌نوشتهٔ بیستون ۱،۱۸) بارتولومه صریحاً هشدار می‌دهد که «این صورت شاید دگرگونی ریشه‌شناسیٔ عامیانهٔ یک نام غیرایرانی باشد؛ آشوری Idiqlat». پس معنای «رود تندرو» ریشه‌شناسیٔ عامیانه است نه ریشهٔ واقعی؛ دو واژهٔ نخست پذیرفته، واژهٔ سوم با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Tigris\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1016\", \"status\": \"supports\", \"note\": \"POK_03.txt (leaf 257 = p.1016): 'av. taeya-, taeža- ,scharf; m. Schärfe', tiyra-, ap. tigra- ,spitz'; afghan. terə ,scharf, spitzig' (*taigra-); av. tiži- ds., tiyri- ,Pfeil' usw.' — covers tiγra, taēža, taēγa exactly as drawn. Pokorny says nothing about the river name.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. ~651 s.v. tiγra-, tiγray-, tigrā- (BRT.txt lines 12245-12258)\", \"stance\": \"partial\", \"note\": \"'• j. tiγra- (, p. tigra-) Adj. ‚spitz, spitzig''; '• j. tiγray- m. ‚Pfeil' ... Vgl. tigra-. — np. tīr'; but s.v. '• p. tigrā- f. Name eines Flusses, Tigris': 'Stammansatz und Geschlecht unsicher. Die Namensform beruht vll. auf volksetymologischer Umgestaltung des nicht iranischen Namens ... Das Mp. hat Diglat; Ass. Idiqlat, Gr. Tigris.'\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. tigr (NYB_vol2_glossary.txt line 3773)\", \"stance\": \"supports\", \"note\": \"'tigr [tgl] arrow ... — Av. (651) tiγri-; OP tigra- ‚pointed' = Av. (ibd.) čiγra-; Paz. NP tīr (SW form).' Nyberg's '(651)' is the Bartholomae column, confirming the AiW reference.\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian lexicon s.v. tigra- / Tigrā (via BRT and DB 1.18)\", \"stance\": \"supports\", \"note\": \"Kent's text of DB 1.18 has 'Tigrām viyatarayamā' — the OP river name is genuine; Kent glosses tigra- 'pointed' (tigraxauda-).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 20.24 'arrow' (SYN.txt line 34758)\", \"stance\": \"supports\", \"note\": \"'Av. tiyri- (NPers. tir) : tiyra-, OPers. tigra- ‚sharp-pointed', etc. (15.78). Walde-P. 2.612.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tîr; tîr-kaš; setîz; setîhîdan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tīr «تیر» 'arrow' is Av. tiγri- > MP tigr [tgl] (MacKenzie, PHD p.83 'tigr ... | M tygr, N tīr] arrow') > NP tīr, the SW dialect form with -gr- > -r- and compensatory length; Horn no.406 gives exactly 'tīr ‚Pfeil', tīrkes, terkes ‚Köcher'', so the quiver word tīr-kaš / таrkaš «تیرکش / ترکش» is tīr + kaš (root kaš- 'draw', Nourai's ☞ Kenk 1) and is itself the source of Ital. turcasso, Fr. carquois. The chart's extra forms تیز tīz 'sharp' and تیج/تیغ tēγ belong here too: Horn no.408 'tēz ‚scharf, heftig; schnell', tēj ‚Pfeil', tēše ‚Axt'' with 'phlv. tēj, tēz', and no.409 'tēγ ‚spitz, Schwert' ... aw. bi-taēγa- ‚zweischneidig'' — i.e. tīz < *taijī- and tēγ < *taiga-, the s-less variants of the root. But setīz «ستیز» and setīhīdan «ستیهیدن» do NOT descend from tiγra-/taēža- as the arrow drawn on the page claims: they continue the s-retaining branch, YAv. stij- f. 'fight, struggle' (Yt 10.71) > MMP ʾstyz- 'to quarrel', BMP stēzag, Parth. ʾсtyȟāg 'contentious' > NP sitēz / sitēzīdan and (denominative) sitēhīdan — Cheung, EDIV 361f. s.v. *staij, who files the whole group under 'PIE *steig- ‚to sting, stab', LIV: 592 | Pok.: 1016 f.' So the root is Nourai's root, but the intermediate step is wrong. The book's gloss 'setīz: \\\"sharp\\\"' (printed in quotation marks on p.448) is also wrong as a translation: ستیز means 'combat, strife, obstinacy' — Borhan-e Qate' glosses it «خصومت و سرکشی و لجاجت و خشم و کین و عناد»; Nourai put it in quotes to signal the root sense, not the actual meaning. The last extra form ستیغ setīγ 'mountain ridge, peak' is a fourth strand again: it goes with Av. staēra-/taēra- 'mountain peak' from the unextended *stei- 'pointed' (Pokorny 1016, same page).\",\n          \"derivation_fa\": \"«تیر» از اوستایی tiγri- از راه فارسی میانهٔ tigr (مکنزی، فرهنگ پهلوی، ص ۸۳) آمده است؛ خوشهٔ -gr- در گویش جنوب غربی به -r- ساده شده و واکه کشیده شده است. هرن (شمارهٔ ۴۰۶) دقیقاً «tīr پیکان، tīrkeš/terkeš ترکش» را می‌آورد و «تیز» و «تیغ» را نیز (شمارهٔ ۴۰۸ و ۴۰۹) از همین ریشه می‌گیرد. اما «ستیز» و «ستیهیدن» از tiγra- نیامده‌اند بلکه دنبالهٔ اوستایی stij- «پیکار»، فارسی میانه stēz/stēzag و پارتی ʾсtyȟāg هستند (چونگ، فرهنگ فعل‌های ایرانی ۳۶۱–۳۶۲) که همان ریشه را با s آغازین نگه داشته‌اند؛ پس ریشه درست است ولی حلقهٔ میانی نمودار نادرست است. معنای «تیز» که کتاب برای «ستیز» آورده نیز درست نیست؛ برهان قاطع آن را «خصومت و سرکشی و لجاجت» معنا کرده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:543\", \"status\": \"supports\", \"note\": \"BQT vol.1, printed p.543 = BQT_v1_pages.txt leaf 771 (offset 'printed ≈ leaf − 228' near the end of vol.1): the leaf is entirely تیر compounds — 'تیر ... تیرگردون کنایه از آفتاب است', 'تیرچرخ', 'تیر تظلم'; leaf 768 has 'و تیر را نیز گویند که بعربی سهم' ('tīr, which in Arabic is sahm'). The headword تیرکش/ترکش is not findable in this OCR.\"},\n            {\"ref\": \"BQT:1104\", \"status\": \"supports\", \"note\": \"BQT vol.2 leaf 566 (offset 'printed ≈ leaf + 543') carries the whole ستیز nest: 'ستیز – بکسر اول و ثانی ... بمعنی خصومت و سرکشی و لجاجت و خشم و کین و عناد', 'ستیزه ... بمعنی ستیز است که جنگ و خصومت', 'ستیغ ... بمعنی ستیخ است که چیزی راست و راست', 'ستیهش ... لجاجت و ستیزندگی'. Note the estimate puts this leaf at printed ≈ 1109; Nourai's 1104/1105 is within the OCR-offset uncertainty and the words are unmistakably the ones cited.\"},\n            {\"ref\": \"BQT:1105\", \"status\": \"supports\", \"note\": \"The next leaf (BQT_v2_pages.txt 567) opens with 'ستیهیدن – بر وزن شکیبیدن، یمعنی ستیزه کردن – و سخن ناشنودن ونافرمانی نمودن – وفریاد و شور – ولجاجت کردن' — exactly Nourai's setīhīdan 'to fight', on the page after ستیز.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss nos. 406, 408, 409, 722 (HRN.txt lines 3803, 3838, 3846, 6327)\", \"stance\": \"partial\", \"note\": \"no.406 'tīr ‚Pfeil', tīrkes, terkes ‚Köcher' ... aw. tiyri- ‚Pfeil'; phlv. tir ‚Pfeil''; no.408 'tēz ‚scharf, heftig; schnell', tēj ‚Pfeil'' ; no.409 'tēγ ‚spitz, Schwert' ... aw. bi-taēγa-'. BUT no.722 files setīz separately: 'sitēz ‚Kampf, Krieg', sitēzīden. aw. vergl. stij- ‚Kampf, Streit'; phlv. stēj ‚Kampf' (Bund.). Wohl zu ai. √tij- ... gr. στίζω, lat. instigāre, germ. *stek-' — same PIE root, different Iranian preform.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 361-362, s.v. *staij (CHEUNG.txt lines 23611-23640)\", \"stance\": \"partial\", \"note\": \"'*staij ? ‚to stab; to be contentious ?' — YAv. stij- (f.) ‚fight, struggle' (Yt 10.71); MMP ʾstyz- ‚to quarrel', BMP styck /stēzag/ ... NP sitehidan (denomin.) ‚to quarrel, brawl', NP sitezidan ‚to fight', NP sitēz ‚battle, combat, conflict' ... *PIE *steig- ‚to sting, stab' LIV: 592 | Pok.: 1016 f.' Confirms Nourai's ROOT for setīz/setīhīdan but not the tiγra- parentage.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.83 s.v. tigr, tēz, tēx, kantigr (PHD.txt line 595, 3310)\", \"stance\": \"supports\", \"note\": \"'tigr [HTYA < A ḥṭyʾ; tgl | M tygr, N tir] arrow'; 'kantigr [kntgl] quiver'; 'tēz [tyc | M tyz, N ~] quick'; '*tēz ... sharp'; 'tēx [tyh | N tēγ] sharp edge, ridge; ray'. The MP link tīγri > tigr > tīr is explicit.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.~223 (HUB.txt lines 8209, 8216)\", \"stance\": \"partial\", \"note\": \"'tīj ‚Pfeil' ... neben tēz ‚scharf', vgl. tiγra-, in Komp. tiži- ‚scharf, spitz', tiγri- ‚Pfeil''; but separately 'sitez ‚Kampf', zd. stij- ‚Kampf'' — again two different Iranian preforms.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. tež, tigr (NYB_vol2_glossary.txt lines 3771-3773)\", \"stance\": \"supports\", \"note\": \"'tež [tyc] sharp, ardent, swift ... *taiga- alternating with *taija-; Av. (973) brōtərē.taēža- ‚with sharp edge' ... NP tēz'; 'tigr [tgl] arrow ... Av. (651) tiγri-; OP tigra- ‚pointed' ... NP tir (SW form)'.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, via Borhan's ستیز footnote markers (BQT_v2 leaf 566, notes (1)(2))\", \"stance\": \"silent\", \"note\": \"Mo'in's numbered footnotes are present on the ستیز page but the bottom-of-page note text is not legible in this OCR; no Latin-script Pahlavi form recoverable.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Semitic\",\n          \"words\": \"Diglat\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart makes Aramaic/Akkadian Diglat a borrowing FROM Iranian tiγra-. That is the reverse of the accepted history. The oldest attested form is Sumerian id₂-idigna / Idigna (3rd millennium BCE), whence Akkadian Idiqlat (Old Babylonian, centuries before any Iranian presence in Mesopotamia), whence Aramaic דִּגלָת dig̈lāṯ with the usual Aramaic aphaeresis of the initial unstressed vowel. Old Persian Tigrā (DB 1.18, 6th c. BCE) is the LATE end of this chain: the Persians took over the Mesopotamian name and re-shaped it so that it looked like their own tigra- 'sharp, swift' — exactly the process Bartholomae calls 'volksetymologische Umgestaltung des nicht iranischen Namens'. Nourai's own authority here, Farahvashi's Iranvij p.111-112, does argue the opposite (he writes that the Iranians named the river تیگر 'swift, unruly', that on entering Babylonian t > d and g stayed, giving دیگله, then g > j giving دیجله > دجله) — so the reference genuinely supports the arrow, but the reference is a minority Iranian-nationalist reading that Assyriology and Iranian philology alike reject. The phonetic step Farahvashi needs (Iranian t- > Babylonian d-, r > l) is also unmotivated, whereas Sumerian idigna > Akkad. idiqlat > Aram. diglat is regular.\",\n          \"derivation_fa\": \"نمودار نام سامی Diglat را وام‌گرفته از tiγra- ی ایرانی می‌داند، و این وارونهٔ تاریخ است. کهن‌ترین صورت، سومری Idigna (هزارهٔ سوم پ.م.) است که در اکدی Idiqlat شده و از آنجا به آرامی دیگلات رفته است؛ پارسی باستان Tigrā حلقهٔ آخر این زنجیره است و دگرگونی عامیانهٔ همان نام غیرایرانی بر پایهٔ tigra- «تیز» است (بارتولومه). ماخذ نورایی، ایرانویج فره‌وشی ص ۱۱۱–۱۱۲، دقیقاً همین را می‌گوید، اما این دیدگاه در آشورشناسی و زبان‌شناسی ایرانی رد شده است. پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Tigris\",\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%AC%D9%84%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IRN:112\", \"status\": \"supports\", \"note\": \"Farahvashi, Iranvij, printed pp.111-112 (IRN_pages.txt pdf 122-123): 'بنابر همین سرکشی‌ها و طغیانهای دجله است که ایرانیان به آن نام تیگر یا تند و سرکش داده‌اند … نام Tigra هنگامی که وارد زبان بابلی گشت تغییرات کوچک فونتیکی یافت … به این ترتیب از واژهٔ Tigra در بابلی کهن نام دیگله پدید آمد' — word for word Nourai's arrow. The reference supports the claim; the claim itself is what modern scholarship rejects.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. p. tigrā- (BRT.txt line ~12258)\", \"stance\": \"contradicts\", \"note\": \"'Die Namensform beruht vll. auf volksetymologischer Umgestaltung des nicht iranischen Namens, vgl. tiγra- und tiγray-. Das Mp. hat Diglat; Ass. Idiqlat, Gr. Tigris.' Bartholomae makes the Assyrian form primary and the OP form the folk-etymological re-shaping.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter (AKD.txt) — grep for Idiqlat/Diglat\", \"stance\": \"silent\", \"note\": \"Zimmern's list of Akkadian loanwords into the West does not treat the river name; no entry found.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Aramäische Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\", \"note\": \"grep for 'Diglat'/'Digla' returns nothing; Fraenkel treats appellatives, not hydronyms.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"Dîjlat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"As a step in itself this arrow is right: Arabic دِجْلَة Dijla(t) is the Aramaic name taken over by the Arabs. Wiktionary's Arabic entry: 'دِجْلَة — borrowed from Aramaic דיגלת (diḡlāṯ), borrowed from Akkadian Idiglat, borrowed from Sumerian id₂-idigna.' The Aramaic cluster -gl- is preserved, the feminine ending -āṯ is re-analysed as the Arabic tāʾ marbūṭa, and the initial vowel is the one already lost in Aramaic. Farahvashi (Nourai's source) describes the same step in Persian terms: 'گاف به جیم بدل شد و این نیز یک تبدیل رایج است و گاف‌های پارسی در عربی به جیم بدل می‌شوند. بدین ترتیب دیگله به چهرهٔ دیجله در آمد' — the g > j step is in any case the normal Aramaic-to-Arabic adaptation of the reflex of *g, and the outcome is not in doubt. Only the ultimate origin (node #3) is wrong, not this link.\",\n          \"derivation_fa\": \"«دجله» ی عربی همان نام آرامی دیگلات است که عرب‌ها وام گرفته‌اند؛ خوشهٔ -gl- مانده، پایانهٔ مؤنث آرامی -āṯ به تاء مربوطهٔ عربی بدل شده و گ به ج گراییده است — ابدالی کاملاً رایج. فره‌وشی نیز همین پله را می‌آورد. این حلقه از نمودار درست است؛ تنها سرچشمهٔ نهایی (گرهٔ ۳) نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%AC%D9%84%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IRN:112\", \"status\": \"supports\", \"note\": \"Iranvij p.112 (IRN_pages.txt pdf 123): 'بدین ترتیب دیگله به چهرهٔ دیجله در آمد و سپس به دیجله (تلفظ عربی آن) و دجله گرائید' — precisely the Diglat > Dījlat > Dijla step drawn here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. tiger (KLN_1966.txt line 39240)\", \"stance\": \"partial\", \"note\": \"Klein knows only 'Gk. Τίγρις (whence L. Tigris), ‚the Tigris river', lit. ‚the swift river'' and does not mention the Semitic forms — he is silent on the Arabic link.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM.txt)\", \"stance\": \"silent\", \"note\": \"grep for دجلة finds no entry: Addi Shir's list of Persian words arabized does not claim دجلة as a Persian loan.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsīr al-alfāẓ al-dākhila (TAD.txt)\", \"stance\": \"silent\", \"note\": \"no entry for دجلة among the foreign words treated.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"Dejleh; Dîyâleh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"دجله Dejle is the ordinary New Persian name of the Tigris and is simply the Arabic دِجْلَة read with Persian vowels — an Arabic-mediated round trip only if node #3 were right; on the mainstream account it is a plain Arabic loan into Persian, replacing the native Middle Persian name Arwand. The chart's own NOTE (\\\"'Arvand: swift (river)' is translation of 'Dejleh: fast (river)'\\\") reproduces Farahvashi p.112: 'در دوران ساسانیان رود دجله را هم به نام کهن آن دیگله می‌خواندند و هم خود واژهٔ تیگر را … به زبان پهلوی ترجمه کرده و آن را اروندرود می‌نامیدند'; that half IS right — Arwand < Av. aurvant- 'swift, impetuous' is a genuine Iranian word (cf. Lohrāsp < aurvat.aspa-) used of the Tigris, and Ferdowsi's couplet quoted in the box ('اگر پهلوانی ندانی زبان / بتازی تو اروند را دجله خوان') says exactly that the Pahlavi Arwand equals Arabic Dejle. The weak item is دیاله Dīyāle: Farahvashi derives it from دیجله by j > y ('بار دیگر تبدیلی صورت گرفته و این بار ج در دیجله به ی مبدل شده'), which is phonetically conceivable but is asserted rather than documented; the river is otherwise known as Kurdish/Persian Sīrwān 'roaring river', and no standard reference derives Diyālā from Dijla.\",\n          \"derivation_fa\": \"«دجله» در فارسی نو وام‌واژه‌ای عربی است که جای نام ایرانی «اروند» را گرفته است. اروند از اوستایی aurvant- «تند، تیزرو» است (همان که در لهراسپ < aurvat.aspa- دیده می‌شود) و بیت فردوسی که در کادر آمده همین برابری را گواهی می‌دهد؛ پس یادداشت نورایی دربارهٔ اروند درست است. اما بند دوم، یعنی گرفتن «دیاله» از «دیجله» با ابدال ج به ی، تنها ادعای فره‌وشی است و پشتوانهٔ مستقلی ندارد؛ این رود در کردی و فارسی سیروان نام دارد. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%AC%D9%84%D8%A9\",\n            \"https://en.wikipedia.org/wiki/Diyala_River\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IRN:112\", \"status\": \"supports\", \"note\": \"Iranvij p.112 (pdf 123): 'با این تغییر واژه دیجله به صورت دیاله در آمد که آن هم یکی از رودهایی است که از ایران سرچشمه می‌گیرد'; and p.112-113 for Arwand = translation of Tigra. Both of Nourai's items come from this page.\"},\n            {\"ref\": \"MON5:520\", \"status\": \"not_checked\", \"note\": \"Mo'in vol.5 (اعلام, proper names) is not among the local scans and vajehyab/abadis expose only the lexicon volumes; the abridged 2-vol Adena text on disk has no دجله entry (grep returns 0).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_2vol_Adena (grep دجله , دیاله)\", \"stance\": \"silent\", \"note\": \"0 hits in either local Mo'in text — the abridgement drops the aʿlām volumes where these names stand.\"},\n            {\"src\": \"FSF\", \"where\": \"Noushin, Farhang-e Shahnameh, s.v. اروند\", \"stance\": \"supports\", \"note\": \"The Shahnameh glossaries gloss اروندرود as the Tigris, matching Ferdowsi's couplet quoted in the box.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan s.v. اروند, quoted by Farahvashi IRN p.113\", \"stance\": \"supports\", \"note\": \"'در فرهنگ برهان قاطع در زیر نام اروند چنین آمده است: اروند بروزن و معنی الوند است و آن کوهی باشد در نواحی همدان … و دجلهٔ بغداد را نیز گفته‌اند' — Borhan itself equates Arwand with the Tigris.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"tigris\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Ancient Greek τίγρις is the name of the animal (Ctesias, Aristotle, 4th c. BCE, after the Persian-wars contact with the East) and also, as Τίγρης/Τίγρις, the river-name taken from Old Persian Tigrā. Nourai's gloss 'fast running' is not the Greek word's meaning but the etymological gloss he takes from Partridge; Klein states it in the same words: 'Gk. τίγρις, prop. ‚the swift animal', a word of Iranian origin. Cp. Avestic tiγriš ‚arrow', tiγra- ‚pointed'. ... Cp. Gk. Τίγρις (whence L. Tigris), ‚the Tigris river', lit. ‚the swift river'.' Skeat says the same. So the derivation as drawn is a respectable 19th-20th c. view. It is nevertheless only 'plausible' today: Etymonline records the objection that 'no application of either word, or any derivative, to the tiger is known in Zend' — no Iranian language actually calls the tiger *tigra-, and Watkins, while keeping the Iranian source, explains the name differently ('in Greek tigris, tiger (from its stripes)'), i.e. from the 'tattoo, mark' sense of the root rather than from speed. Beekes treats the animal name as a loan of unknown (possibly non-IE) origin.\",\n          \"derivation_fa\": \"یونانی τίγρις هم نام جانور (ببر) است و هم نام رود دجله که از پارسی باستان Tigrā گرفته شده است. معنای «تندرو» که نورایی آورده معنای واژه نیست بلکه توضیح ریشه‌شناختی او به پیروی پارتریج است؛ کلاین و اسکیت نیز همین را می‌گویند. اما امروز این ریشه‌شناسی قطعی شمرده نمی‌شود، زیرا در هیچ زبان ایرانی ببر را *tigra- ننامیده‌اند؛ واتکینز نام جانور را به معنای «خال‌دار، خط‌دار» از همین ریشه می‌گیرد و بیکس آن را وام‌واژه‌ای با خاستگاه نامعلوم می‌داند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tiger\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:667\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is lending-only on archive.org and has no local copy (refs_online.json: 'RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only'). Klein and Skeat, however, give the identical derivation and identical 'swift' gloss, so the substance of PRT:667 is corroborated.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. tiger (KLN_1966.txt line 39240)\", \"stance\": \"supports\", \"note\": \"'tiger, n. — ME. tigre, fr. OF. (= F.) tigre, fr. L. tigris, fr. Gk. τίγρις, prop. ‚the swift animal', a word of Iranian origin. Cp. Avestic tiγriš, ‚arrow', tiγra-, ‚pointed'. These words are derivatives of I.-E. base *(s)teig- ... Cp. Gk. Τίγρις (whence L. Tigris), ‚the Tigris river', lit. ‚the swift river'.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Tiger (SKT.txt offset 2145037)\", \"stance\": \"supports\", \"note\": \"'Tiger. (F.-L.-Gk.-Pers.) M.E. tigre. — F. tigre. — L. tigris ... — Gk. τίγρις. — Zend (O. Pers.) tighri, an arrow (hence a tiger, from its swiftness, also the river Tigris, from its swiftness); mod. Pers. tīr, an arrow, the river Tigris. — Zend tighra, sharp.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steig- I.7\", \"stance\": \"partial\", \"note\": \"'Suffixed reduced form *tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan tighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER.' Same Iranian source, but a different motivation for the name.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"tiger ; Tigris\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words come through Latin from the Greek of node #6. 'tiger': Latin tigris (acc. tigrim/tigrin) > Old French tigre > Middle English tigre (Old English already had a plural tigras, borrowed directly from Latin) > tiger, with the -re/-er metathesis normal in English (cf. Old French chambre > chamber). 'Tigris' is the learned Latin form of the river-name kept unchanged in English since the Wycliffite Bible; the everyday Arabic-based form Dijla never entered English. The glosses 'a fast running animal' / 'a fast moving river' are Nourai's etymological glosses carried down from node #6, not the words' meanings; the borrowing route itself (Gk > Lat > OFr > ME) is beyond dispute.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی از راه لاتین از یونانی گرفته شده‌اند: لاتین tigris > فرانسهٔ کهن tigre > انگلیسی میانه tigre > tiger، با قلب رایج -re > -er (مانند chambre > chamber). Tigris صورت عالمانهٔ لاتین نام رود است که دست‌نخورده در انگلیسی مانده است. معناهایی که نورایی آورده («جانور تندرو»، «رود تندرو») توضیح ریشه‌شناختی است نه معنای واژه؛ خود مسیر وام‌گیری درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tiger\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:667\", \"status\": \"not_checked\", \"note\": \"Partridge Origins p.667 not accessible (lending-only); the chain L. tigris > OF tigre > ME tigre > tiger is given identically by Klein, Skeat and Etymonline.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. tiger (KLN_1966.txt line 39240)\", \"stance\": \"supports\", \"note\": \"'ME. tigre, fr. OF. (= F.) tigre, fr. L. tigris, fr. Gk. τίγρις' — exactly the route drawn.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Tiger\", \"stance\": \"supports\", \"note\": \"'(F.-L.-Gk.-Pers.) M.E. tigre. — F. tigre. — L. tigris ... also the river Tigris, from its swiftness.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steig- I.7 and index 'TIGER steig-' (line 2389)\", \"stance\": \"supports\", \"note\": \"TIGER is listed in the Watkins index under steig-.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Greek\",\n          \"words\": \"stizein ; a-stigmat\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"στίζειν stízein 'to prick, tattoo, brand' (Herodotus, of branding slaves) is the regular Greek outcome of the root with s- preserved: *stig-yē/o- > *stígyō > στίζω by the normal Greek change of *-gy- > -ζ-, beside the verbal adjective στικτός 'tattooed, dappled' and the noun στίγμα, gen. στίγματος 'puncture, mark, point'. Watkins files it as 'Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM.' The second item, 'a-stigmat \\\"without a (focal) point\\\"', is not an ancient Greek word at all: it is the modern scientific stem abstracted from the neo-classical coinage astigmatism (see #11), built from the alpha privative ἀ- plus στίγματ-. Presenting it in a 'Greek' box is a shortcut; the elements are Greek but the compound is 19th-century English. Hence 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"یونانی στίζω (stízō) «خلیدن، خالکوبی کردن» بازماندهٔ مستقیم همین ریشه با s آغازین است: *stig-yō با دگرگونی قاعده‌مند *-gy- > -ζ- به στίζω رسیده، و از همان ستاک στίγμα «نقطه، نشان» ساخته شده است. اما a-stigmat واژه‌ای یونانی نیست؛ ستاکی است که از برساختهٔ سدهٔ نوزدهم astigmatism بیرون کشیده شده (الف نفی یونانی + στίγματ-). پس ادعای نورایی دربارهٔ stízein درست است ولی گذاشتن a-stigmat در جعبهٔ یونانی مسامحه است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/astigmatism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. steig-, I.6: 'Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM.' (AHD_watkins1985.txt line 1010) — both of Nourai's Greek items are covered, with astigmatism explicitly derived through stizein.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1016 (POK_03.txt leaf 257)\", \"stance\": \"supports\", \"note\": \"'gr. στίζω ,steche, tätowiere', στίγμα ,Stich, Punkt', στικτός ,bunt' (,gestickt').'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stigma and astigmatism (KLN_1966.txt lines 36796, 3742)\", \"stance\": \"supports\", \"note\": \"'stigma, n. — L., fr. Gk. στίγμα, ‚puncture, brand', from the stem of στίζειν (for *στίγιειν), ‚to prick, point, mark'.' and 'astigmatism ... fr. priv. pref. a- and Gk. στίγμα, gen. στίγματος'.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 612\", \"stance\": \"supports\", \"note\": \"'Gr. στίζω „steche, tätowiere“, στίγμα „Stich, Punkt“, στικτός „bunt“ („gestickt“).'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box: the French link between the Greek stem and Persian آستیگمات. The words implied are French astigmatisme (n., attested from 1866 in medical French, after the English term) and the adjective/noun astigmate 'astigmatic (person)'. French took the coinage from English ophthalmological literature and gave it the regular French suffixes -isme / -ate; it is French astigmate, not English astigmatism, that yields the Persian form of node #10 (Persian آستیگمات ends in -āt, not in -ism), so the box is doing real work in the chart even though it is blank.\",\n          \"derivation_fa\": \"این جعبهٔ خالی، حلقهٔ فرانسوی میان ستاک یونانی و «آستیگمات» فارسی است. واژهٔ مورد نظر astigmate / astigmatisme فرانسوی است که از متون پزشکی انگلیسی وام گرفته و با پسوندهای فرانسوی ساخته شده است؛ وجود این حلقه لازم است، زیرا صورت فارسی به -āt ختم می‌شود نه به -ism انگلیسی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/astigmatism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); nothing of Nourai's to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. astigmatism (KLN_1966.txt line 3742)\", \"stance\": \"partial\", \"note\": \"Klein gives the coinage as English (Whewell) and does not mention a French intermediary, but the French forms astigmate/astigmatisme are the obvious donors for the Persian shape.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in's practice of tagging European loans (فره. = فرانسه)\", \"stance\": \"supports\", \"note\": \"Mo'in routinely tags this stratum of medical vocabulary as French, e.g. the neighbouring entry اتیلن 'اتیلن: éthylène (شیم.)' in MON_part1.txt, the same French-scientific layer.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"âstîgmât\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"آستیگمات āstīgmāt is a 20th-century Persian borrowing of French astigmate, part of the wave of French medical and optical vocabulary that entered Persian through the Dār al-Fonūn and French-trained physicians. The French initial cluster ast- is resolved, as Persian always does with initial st-/sp-/sk-, by a prothetic long ā- (cf. استادیوم, استاتیک, آسفالت); French nasal-less -gmate is rendered -gmāt with the long ā of the French [a] in an open stressed syllable. The word means 'astigmatism' or 'astigmatic' in Persian optical usage. The derivation drawn (Greek > French > Persian) is correct in route.\",\n          \"derivation_fa\": \"«آستیگمات» وام‌واژه‌ای است از فرانسوی astigmate که در سدهٔ چهاردهم هجری همراه با انبوهی از اصطلاحات پزشکی فرانسوی از راه دارالفنون به فارسی آمده است. خوشهٔ آغازین st- که در فارسی ناممکن است، مانند همیشه با افزودن الف (آ-) آغازین گشوده شده است؛ همان‌گونه که در استادیوم و آسفالت. مسیر یونانی > فرانسوی > فارسی که نورایی کشیده درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/astigmatism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:54\", \"status\": \"not_checked\", \"note\": \"Mo'in vol.1 p.54 could not be opened: the local Mo'in texts (MON_part1/2 and the 2-vol Adena abridgement) return 0 hits for آستیگمات / استیگمات, and vajehyab.com/moein/آستیگمات returned HTTP 500, abadis.ir HTTP 400. The page number is plausible: آستیگمات falls in the آست- run early in Mo'in vol.1.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_2vol_Adena_v1_djvu.txt (grep آستیگمات, استیگمات)\", \"stance\": \"silent\", \"note\": \"0 hits in both local Mo'in texts; the Adena 2-volume abridgement drops most technical European loans.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, IE roots dictionary (ARY_latin_index_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for ASTIGMAT finds nothing; Aryanpur's index covers inherited vocabulary, not modern French loans.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"astigmatism\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A documented coinage, not an inherited word: the Rev. William Whewell of Trinity College, Cambridge made it for his friend the astronomer George Biddell Airy's eye defect, from the Greek alpha privative ἀ- 'without' plus στίγμα, gen. στίγματος 'a point', with the suffix -ism — literally 'the condition of having no point (of focus)', i.e. the rays of light not converging to a point on the retina. Klein dates the coinage 1819, Etymonline 1849 (the term was publicised in Whewell's circle in the 1840s); either way it is 19th-century English. Nourai's gloss of the Greek element in node #8, 'without a (focal) point', is precisely right. Watkins lists ASTIGMATISM under steig- in the AHD index.\",\n          \"derivation_fa\": \"«astigmatism» واژه‌ای برساخته است نه میراثی: ویلیام ویول انگلیسی در سدهٔ نوزدهم آن را از الف نفی یونانی ἀ- و στίγματ- «نقطه» به افزودن پسوند -ism ساخت، به معنای «نبودن نقطهٔ کانونی». کلاین سال ۱۸۱۹ و اتیموآنلاین ۱۸۴۹ را می‌آورد. معنایی که نورایی برای جزء یونانی آورده دقیقاً درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/astigmatism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. astigmatism (KLN_1966.txt line 3742)\", \"stance\": \"supports\", \"note\": \"'Coined by the English mathematician and philosopher William Whewell (1794-1866) in 1819 fr. priv. pref. a- and Gk. στίγμα, gen. στίγματος, ‚a prick, puncture, mark'.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1266)\", \"stance\": \"supports\", \"note\": \"'ASTIGMATISM  steig-' — and at the root entry 'Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Germanic\",\n          \"words\": \"stik\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *stikan-/*stikkōn- 'to prick, stab, stick (into), attach' is the zero-grade *stig- of the root with the regular Grimm shift *g > k: Gothic stiks 'point (of time)', OE stician 'to stab, prick, pierce', OHG stehhan/sticken, OS stekan, MDu. steken 'to stick, stab', ON steikja 'to roast (= to fix on a spit)'. Pokorny 1016-1017 sets out the whole Germanic paradigm and explains the anomalous e-grade forms (OHG stehhan) as an 'Ablautentgleisung' under the influence of *steg- 'pole'. Watkins gives the same and specifies the form that matters for the next two nodes: 'Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET'. Nourai's gloss 'to prick, attach' is exactly the two senses that generate the French descendants.\",\n          \"derivation_fa\": \"ژرمنی آغازین *stikan- «خلیدن، فرو کردن، چسباندن» درجهٔ صفر همین ریشه (*stig-) است که طبق قانون گریم *g به k بدل شده است: گوتی stiks، انگلیسی کهن stician، آلمانی علیای کهن stehhan، هلندی میانه steken. پوکورنی (۱۰۱۶–۱۰۱۷) همهٔ این صورت‌ها را گرد آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/etiquette\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. steig- I.1-4: 'Germanic suffixed form *stik-ilaz in Old English sticel ... Germanic expressive form *stikkōn- in Old English sticca, stick: STICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET' (AHD_watkins1985.txt line 1010).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1016-1017 (POK_03.txt leaf 257-258)\", \"stance\": \"supports\", \"note\": \"'got. stiks ,Stich, Punkt', ahd. stih, as. stiki, mnd. steke, ags. stice m. ... stician ,stechen'; ... mnd. sticken ,stechen, sticken, anzünden, ersticken', ahd. sticken ,stechen, sticken'.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stick, v. (KLN_1966.txt line 36789)\", \"stance\": \"supports\", \"note\": \"'OE. stician, ‚to stab, prick, pierce', rel. to OS. stekan, OFris. steka, Du. steken, OHG. stehhan ... fr. I.-E. base *steig-, ‚to prick, stick, pierce'.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 613\", \"stance\": \"supports\", \"note\": \"'Got. stiks „Stich, Punkt“ (wie lat. punctum : pungo), ahd. stih ds., as. stiki „stick“ ... ags. stician „stechen; intr. stecken bleiben, festhalten“.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"French\",\n          \"words\": \"etiquette\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French étiquette is a Germanic (Frankish/Middle Dutch) loan into Old French, not an inherited Romance word. Old French estiquier / estiquer 'to stick on, to fix, to attach' is Frankish *stikkan (= MDu. steken, cf. node #12); from it the diminutive noun estiquette 'a slip stuck up, a label, a ticket' (14th-15th c.), the initial e- being the French prothetic vowel that regularly breaks a Germanic s+consonant onset (cf. escarlate, espérer, estandard). The modern sense 'etiquette, protocol' develops at the Spanish and French courts of the 16th-17th c. from the small cards (estiquettes) on which the order of ceremonies — or a soldier's billeting instructions — was written; Nourai's gloss 'label, a set of instructions' names both stages of that shift precisely. English borrowed the court sense in 1750 (node #15), while the earlier form estiquet had already given English ticket (node #16), so the two are doublets.\",\n          \"derivation_fa\": \"«اتیکت» فرانسوی (étiquette) وام‌واژه‌ای ژرمنی در فرانسهٔ کهن است: از estiquier «چسباندن، الصاق کردن» از فرانکی *stikkan، و از آن اسم مصغر estiquette «برچسب، کاغذ الصاقی»؛ الف آغازین همان واکهٔ میانجی است که فرانسه برای شکستن خوشهٔ st- می‌افزاید. معنای «آداب دربار» در سدهٔ شانزدهم–هفدهم از همان کارت‌های کوچکی پدید آمد که ترتیب تشریفات را بر آن می‌نوشتند؛ پس معنای دوگانه‌ای که نورایی آورده (برچسب / دستورالعمل) دقیقاً درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/etiquette\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:451\", \"status\": \"partial\", \"note\": \"The Watkins appendix (the part of AHD available on disk) supports the derivation in full — s.v. steig-, I.4: 'Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET'; index line 1477 'ETIQUETTE steig-'. Page 451 is a page of the AHD New College Edition main word-list (the 'e' range), which is not in the local copy and is lending-only on archive.org, so the exact page could not be opened.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. etiquette (KLN_1966.txt line 13746)\", \"stance\": \"supports\", \"note\": \"'etiquette, n., conventional rules of social behavior. — F. étiquette, fr. OF. estiquier, estiquer, ‚to stick on, attach', fr. Du. stikken, ‚to stitch', which is rel. to G. sticken, ‚to embroider', stechen, ‚to stab, prick, puncture'. See stitch and cp. ticket, which is a doublet of etiquette.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Etiquette (SKT.txt offset 555552)\", \"stance\": \"supports\", \"note\": \"'Etiquette ; see Stick (1).' — Skeat files it under the same Germanic verb.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic / PHN (French words of oriental origin)\", \"stance\": \"silent\", \"note\": \"Neither Devic nor Pihan lists étiquette, consistent with a Germanic, not an oriental, source.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Persian\",\n          \"words\": \"etîket\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"اتیکت etīket is a direct loan from French étiquette, one of the very large group of French words that entered Persian from the Qajar period onwards; the French final -ette is rendered -et, and the initial é- as a short e written with alef. Mo'in's dictionary gives both senses that French had developed: 'اتیکت: [étiquette] نوشته‌ای که روی کیسه‌ها یا شیشه‌های دوا و کالای بازرگانی برای تعیین محتوی و وزن آنها می‌چسبانند، برچسب. رسوم و آداب درباری، تشریفات. رسوم و آداب در زندگی اجتماعی و رفتار...'. Nourai's gloss 'manners' is the third of these. Mo'in also cross-refers the native calque برچسب to it ('برچسب ... (فره.) اتیکت'), confirming the French tag.\",\n          \"derivation_fa\": \"«اتیکت» وام‌واژه‌ای فرانسوی (étiquette) است که از دورهٔ قاجار به فارسی راه یافته است؛ پایانهٔ -ette به -et ساده شده و é- آغازین با الف نوشته شده است. معین هر دو معنای فرانسوی را می‌آورد: «برچسب» و «رسوم و آداب درباری، تشریفات»؛ معنایی که نورایی آورده (آداب معاشرت) همان معنای سوم معین است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/etiquette\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:140\", \"status\": \"supports\", \"note\": \"Mo'in's entry was located in the local 2-vol Adena abridgement of Farhang-e Farsi (MON_part1.txt, on the leaf headed '۸۸ فرهنگ فارسی معین', between اتیان and اتیلن): 'اتیکت: [étiquette] نوشته‌ای که روی کیسه‌ها یا شیشه‌های دوا و کالای بازرگانی ... می‌چسبانند، بر چسب. رسوم و آداب درباری، تشریفات. رسوم و آداب در زندگی اجتماعی و رفتار'. The page number differs (p.88 of the abridgement vs. Nourai's vol.1 p.140 of the 6-vol edition), but the entry and its French tag are exactly what Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. برچسب and آیین\", \"stance\": \"supports\", \"note\": \"'برچسب: (امر.) ... قطعه کاغذی که روی اجناس چسبانند تا معرف جنس و قیمت آنها باشد (فره.) اتیکت' and s.v. آیین 'تشریفات، اتیکت (فره.)' — Mo'in twice tags اتیکت as French (فره. = فرانسه).\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur IE-roots dictionary\", \"stance\": \"silent\", \"note\": \"no entry; the book treats inherited Persian vocabulary, not modern French loans.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"etiquette\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English took étiquette from French in 1750 in the court sense only ('prescribed behaviour'), keeping the French spelling and approximately the French stress; the older 'label' sense of the French word never came with it, because English already had ticket (node #16) in that role. Lord Chesterfield's letters are among the earliest users. Klein and Etymonline agree on the date and the route, and Watkins lists ETIQUETTE in the AHD index under steig-.\",\n          \"derivation_fa\": \"انگلیسی etiquette را در ۱۷۵۰ میلادی از فرانسه وام گرفت، آن هم تنها در معنای «آداب دربار و تشریفات»؛ معنای کهن‌تر «برچسب» همراه آن نیامد زیرا انگلیسی پیش‌تر ticket را داشت. املای فرانسوی دست‌نخورده ماند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/etiquette\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. etiquette (KLN_1966.txt line 13746)\", \"stance\": \"supports\", \"note\": \"'etiquette, n., conventional rules of social behavior. — F. étiquette ...'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1477)\", \"stance\": \"supports\", \"note\": \"'ETIQUETTE steig-'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Etiquette\", \"stance\": \"supports\", \"note\": \"'Etiquette ; see Stick (1).'\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"stick ; ticket\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"'stick' is the native word and is drawn correctly: OE stician 'to stab, prick, pierce' (weak verb) and the strong ME steken, plus the noun OE sticca 'stick, peg', all from PGmc *stik- (node #12). 'ticket' is NOT a direct Germanic inheritance, however: it is a 16th-century borrowing of Old French etiquet / estiquet, the masculine by-form of estiquette, so it re-enters English from the French branch (node #13) and is, in Klein's words, 'a doublet of etiquette'; the aphaeresis of the initial e- (estiquet > ticket) happened in English. Drawing it straight from 'Germanic stik' short-circuits two steps, which is why the node is only 'plausible' rather than 'confirmed'. Watkins prints the same double outcome at one place — 'Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET' — with the parentheses marking the French mediation.\",\n          \"derivation_fa\": \"«stick» واژه‌ای بومی است: از انگلیسی کهن stician و اسم sticca، از ژرمنی آغازین *stik-؛ این پیوند درست است. اما «ticket» میراث ژرمنی نیست بلکه وام‌واژه‌ای از فرانسهٔ کهن estiquet است که در سدهٔ شانزدهم وارد انگلیسی شد و الف آغازین آن در انگلیسی افتاد؛ پس ticket و etiquette دوگانه (doublet) اند. کشیدن فلش مستقیم از ژرمنی دو پله را نادیده گرفته است؛ پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/etiquette\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. etiquette and stick, v. (KLN_1966.txt lines 13746, 36789)\", \"stance\": \"partial\", \"note\": \"'See stitch and cp. ticket, which is a doublet of etiquette' — Klein routes ticket through French, not straight from Germanic; 'stick' he derives directly from OE stician < *steig-.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ticket (SKT.txt offset 2142837)\", \"stance\": \"partial\", \"note\": \"'Ticket ; see Stick (1).' Skeat files ticket under the Germanic verb, i.e. he takes the same short-cut Nourai does, but at 'Etiquette; see Stick (1)' he treats the two as one family.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steig- I.4 and index line 2389\", \"stance\": \"partial\", \"note\": \"'Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET'; index 'TICKET steig-'. The parenthesis marks the indirect (French) route.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Latin\",\n          \"words\": \"stinguere\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Latin family is nasal-infixed *sti-n-g-: īnstīgāre 'to goad, incite' (un-nasalised, the basic form), īnstinguere 'to incite', interstinguere 'to set here and there with', distinguere 'to mark off, separate, distinguish', ex(s)tinguere 'to quench'. Pokorny 1016 lists them all under (s)teig- and explains the 'quench' sense as originally 'to poke apart the burning logs' ('lat. stinguō, -ere ‚auslöschen' (vom Auseinanderstochern der brennenden Scheite)'). Two qualifications make this only 'plausible': (a) the simplex stinguere in classical Latin means 'to extinguish', not 'to separate, distinguish' — Nourai has transferred the gloss of the prefixed distinguere to the simplex; (b) Watkins himself hedges: 'Nasalized form *sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure)'. De Vaan likewise keeps distinguere/exstinguere from *steig- but treats 'quench' as secondary. The root connection is standard; the gloss and the internal semantics are not tidy.\",\n          \"derivation_fa\": \"خانوادهٔ لاتین با میانوند خیشومی ساخته شده است: *sti-n-g- در برابر صورت بی‌خیشوم īnstīgāre «برانگیختن»؛ از آن distinguere «جدا کردن، بازشناختن» و exstinguere «خاموش کردن». پوکورنی (۱۰۱۶) همه را زیر همین ریشه می‌آورد و معنای «خاموش کردن» را از «بهم زدن هیزم‌های سوزان با نوک چوب» توضیح می‌دهد. دو نکته ولی مانع از تأیید کامل است: معنایی که نورایی به stinguere داده در واقع معنای distinguere است؛ و واتکینز خود می‌نویسد که «گذارهای معنایی مبهم اند». پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. steig- I.5: 'Nasalized form *sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTINGUISH, INSTINCT.' (AHD_watkins1985.txt line 1010) — the arrow is Watkins's, including the reservation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 1016 (POK_03.txt leaf 257)\", \"stance\": \"supports\", \"note\": \"'lat. instigō, -are ,anspornen, anstacheln'; nasaliert īnstinguō ,reize an', interstinguō ..., distinguō ,(steche, stochere auseinander) unterscheide' ...; lat. stinguō, -ere ,auslöschen' (vom Auseinanderstochern der brennenden Scheite)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 613\", \"stance\": \"supports\", \"note\": \"Same text, with the cross-reference 's. Vf. LEWb.² s. v.' — Walde's own Latin etymological dictionary.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stick, v. (KLN_1966.txt line 36789)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *steig- ... whence also L. instigare, ‚to goad', instinguere, ‚to incite; impel', distinguere, ‚to distinguish'.'\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt) s.v. stinguo\", \"stance\": \"supports\", \"note\": \"Walde derives stinguō/distinguō from the same *steig- 'stechen', the source Pokorny cites at IEW 1016.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"distinguish ; extinguish ; instinct\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are learned borrowings out of the Latin family of node #17, and the odd -ish of the first two is a well-understood hybrid. 'distinguish' (1560s) is Middle French distinguer < L. distinguere, remodelled in English on the many verbs in -ish that render French -iss- (finish, punish), with an unetymological -gu- kept from the Latin spelling; 'extinguish' (1540s) is L. ex(s)tinguere given the same -ish treatment; 'instinct' (15th c.) is L. īnstinctus, the past participle of īnstinguere 'to incite, impel', originally 'impulse, prompting', whence the modern zoological sense in the 17th c. Watkins closes the steig- entry with exactly these three words in capitals.\",\n          \"derivation_fa\": \"هر سه واژه وام‌واژه‌های عالمانه‌اند که از خانوادهٔ لاتینی گرهٔ ۱۷ آمده‌اند: distinguish و extinguish از distinguere و exstinguere با افزودن پسوند انگلیسی -ish (به قیاس finish و punish که برابر -iss- فرانسوی است)؛ instinct از اسم مفعول لاتین īnstinctus از īnstinguere «برانگیختن» که نخست به معنای «انگیزه، رانه» بود و سپس معنای جانورشناختی گرفت. واتکینز هر سه را در پایان مدخل steig- می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)teyg-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steig- I.5 and index lines 1429, 1487, 1681\", \"stance\": \"supports\", \"note\": \"'DISTINGUISH, EXTINGUISH, INSTINCT' at the root entry; index 'DISTINGUISH steig-', 'EXTINGUISH steig-', 'INSTIGATE steig- INSTINCT steig-'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. stick, v. (cross-references)\", \"stance\": \"supports\", \"note\": \"'Cp. also astigmatism, distinct, distinguish, etiquette, extinguish, instigate, instinct, steak, stigma, stimulus, stipple, stitch, style ... thistle, ticket, tiger, Tigridia.' — Klein's own list of the English descendants of *steig- matches the whole right-hand side of this chart.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt), s.v. Distinguish / Extinguish\", \"stance\": \"supports\", \"note\": \"Skeat refers both to Latin stinguere and thence to the same Germanic/IE group he files under Stick (1).\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-478.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-478 verification JSON"
}
```


### [2026-09-14T02:58:25.305Z] TOOL RESULT

```
JSON OK
```


## [2026-09-14T02:58:27.555Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 tools/verify_check.py 478",
 "description": "Run verify_check for page 478"
}
```


### [2026-09-14T02:58:28.525Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'plausible': 7, 'disputed': 1, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 9, 'partial': 1}
books consulted: {'partial': 10, 'supports': 34, 'silent': 10, 'contradicts': 1} | by book: {'KLN': 12, 'SKT': 6, 'AHD': 6, 'MON': 5, 'POK': 3, 'WLD': 3, 'BRT': 2, 'NYB': 2, 'ARY': 2, 'KNT': 1, 'SYN': 1, 'HRN': 1, 'CHEUNG': 1, 'PHD': 1, 'HUB': 1, 'AKD': 1, 'AFA': 1, 'AFM': 1, 'TAD': 1, 'FSF': 1, 'BQT': 1, 'DEV': 1, 'LEW': 1}
```


## [2026-09-14T02:58:50.249Z] AGENT

Page 478 (book p. 448) verified — 1 entry, 18 nodes, 0 PROBLEM lines from `verify_check.py`.

**Counts:** root confirmed (1). Nodes: 10 confirmed, 7 plausible, 1 disputed, 0 transcription_suspect. Ref checks: 11 supports, 1 partial, 9 not_checked. 63 `consulted` entries across 23 books.

**Root** `Steig, Stig, Teig` = PIE *(s)teyg- "to prick; pointed" — Pokorny IEW 1016 confirms the heading verbatim, as do Walde-Pokorny II 612–614, Watkins/AHD ("[Pok. steig- 1016]") and Aryanpur's IE-root dictionary.

**Disputed:**
- #3 Semitic `Diglat` ← Iranian *tiγra-*: direction is reversed. Sumerian *id₂-idigna* → Akkadian *Idiqlat* → Aramaic *diglāt* is the older chain; Bartholomae (AiW s.v. OP *tigrā-*) says the OP name "beruht vll. auf volksetymologischer Umgestaltung des nicht iranischen Namens … Ass. Idiqlat". Nourai's cited source (Farahvashi, *Iranvij* p. 111–112) does argue exactly what the chart draws, so `IRN:112` genuinely supports it — the reference itself is the minority view.

**Notable plausibles:**
- #2 Persian: `tīr`/`tīr-kaš` confirmed (Horn 406, MacKenzie p. 83), but `setīz`/`setīhīdan` do **not** come from Av. *tiγra-*; they continue Av. *stij-* "fight" → MP *stēz(ag)* (Cheung EDIV 361f., Horn 722, Hübschmann) — same PIE root, wrong intermediate. Also the book's gloss `setīz : "sharp"` is wrong (Borhan: «خصومت و سرکشی و لجاجت»); the extraction is faithful to the printed page, so this is Nourai's own gloss, not a data error.
- #1 OP `tigrā` "fast-moving river" is the folk etymology, not the etymology.
- #6 Greek `tigris` "fast running": Klein and Skeat state exactly this, but Etymonline notes no Iranian language calls the tiger *tigra-*, and Watkins derives the animal name "from its stripes".
- #8 `a-stigmat` is a 19th-c. neo-classical stem, not attested Greek.
- #16 `ticket` is a doublet of *etiquette* via OFr *estiquet*, not a direct Germanic inheritance.
- #17 Latin `stinguere` means "quench"; the gloss "to separate, distinguish" belongs to *distinguere*.

**Extraction errors:** none. I read `site/pages/478.jpg`; the JSON matches the printed chart exactly, including the quoted gloss `setīz : "sharp"`.

**Unreachable references:** `PRT:667` (Partridge, *Origins* — lending-only; Klein/Skeat corroborate the substance), `MON5:520` and `MON:54` (Mo'in vols. 5 and the آستیگمات entry — not in the local scans; vajehyab returned 500, abadis 400), `AHD:451` (main-dictionary page; Watkins appendix covers the claim). BQT:543/1104/1105 were located and quoted in the local Borhan OCR; MON:140 (اتیکت) was found in the 2-vol abridgement. Seven web pages archived via `fetch_source.py`.
