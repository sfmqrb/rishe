# Verification process log — verify-page-449


## [2026-09-14T01:56:07.719Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 449 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-449.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-449.json. Write /home/sfmqrb/git/rishe/data/verification/page-449.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 449` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:08.731Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:09.619Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:09.637Z] TOOL RESULT

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


## [2026-09-14T01:56:10.125Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-449.txt"
}
```


### [2026-09-14T01:56:10.155Z] TOOL RESULT

```
1	=== PDF page 449 (book page 419) ===
2	--- entry 0 ---
3	ROOT [Semitic] Š.f.f : it is transparent  (refs KLN:275)
4	#1 (parent #0) [Arabic] refs=KLN:275 | šaffa : to be transparent
5	  #2 (parent #1) [Persian] refs=MON | šaffâf «شفّاف» : clear, transparent | extra: شفّافیّت
6	  #3 (parent #1) [Arabic] refs=KLN:275 | šiff : light garment
7	    #4 (parent #3) [French] refs=None | chiffe : rag
8	      #5 (parent #4) [English] refs=KLN:275 | chiffon : silk fabric used for women's dresses | NOTE: AHD derives this word from a different root.
9	--- entry 1 ---
10	ROOT [Arabic] S.f.r, Asfar : (to be) yellow; yellow  (refs FVA:232)
11	#1 (parent #0) [Arabic] refs=FSD:2157 | za`farân : saffron, a plant with purple flowers and orange stigmas | NOTE: PLA:145 claims "za`farân" is from Persian "zar-parân:with gold petals".
12	CEL6:185 derives it from Indo-European "Kesuro: hair" (hairy plant).
13	CEL6:233 claims that Arabs imported it from Kashmir in the 9-10th century
14	  #2 (parent #1) [Persian] refs=MON:1739 | za`farân «زعفران» : saffron
15	  #3 (parent #1) [Middle Latin] refs=DEV:199; PRT:581; KLN:1372 | safranum : saffron
16	    #4 (parent #3) [Old French] refs=AHD:1142 | safron
17	      #5 (parent #4) [English] refs=AHD | saffron, safranine
18	#6 (parent #0) [Arabic] refs=FSD:2157 | safrâ : yellow, bile
19	  #7 (parent #6) [Persian] refs=FVA:232 | safrâ «صفرا ، صفراء» : bile
20	  #8 (parent #6) [Italian] refs=AHD:1142; KLN:1372 | saf-fior : yellow flower
21	    #9 (parent #8) [Old French] refs=None | saflor
22	      #10 (parent #9) [English] refs=AHD | safflower : a plant with orange flowers
23	--- entry 2 ---
24	ROOT [Pahlavi] Šfšyr, Šypšyr, Šamšěr : sword  (refs MPP:88; BQT:1294; NYB:186)
25	#1 (parent #0) [Persian] refs=BQT:1294 | šamšîr «شمشیر» : sword | NOTE: BQT rejects derivation of "šamšîr" from "šam-šîr:lion's paw" by SKT:468.
26	  #2 (parent #1) [English] refs=KLN:1397; SKT:468; HJB:804 | scimitar, cimetar
27	
```


## [2026-09-14T01:56:13.237Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-449.json",
 "description": "Read source JSON for page 449"
}
```


### [2026-09-14T01:56:13.386Z] TOOL RESULT

```
{
  "pdf_page": 449,
  "book_page": 419,
  "entries": [
    {
      "root": {
        "name": "Š.f.f",
        "lang": "Semitic",
        "refs": "KLN:275",
        "gloss": "it is transparent"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:275",
          "words": [
            {"translit": "šaffa", "gloss": "to be transparent", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "šaffâf", "gloss": "clear, transparent", "script": "شفّاف"}
          ],
          "script_extra": "شفّافیّت",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:275",
          "words": [
            {"translit": "šiff", "gloss": "light garment", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "chiffe", "gloss": "rag", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:275",
          "words": [
            {"translit": "chiffon", "gloss": "silk fabric used for women's dresses", "script": null}
          ],
          "note": "AHD derives this word from a different root.",
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "S.f.r, Asfar",
        "lang": "Arabic",
        "refs": "FVA:232",
        "gloss": "(to be) yellow; yellow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FSD:2157",
          "words": [
            {"translit": "za`farân", "gloss": "saffron, a plant with purple flowers and orange stigmas", "script": null}
          ],
          "note": "PLA:145 claims \"za`farân\" is from Persian \"zar-parân:with gold petals\".\nCEL6:185 derives it from Indo-European \"Kesuro: hair\" (hairy plant).\nCEL6:233 claims that Arabs imported it from Kashmir in the 9-10th century",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:1739",
          "words": [
            {"translit": "za`farân", "gloss": "saffron", "script": "زعفران"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Middle Latin",
          "refs": "DEV:199; PRT:581; KLN:1372",
          "words": [
            {"translit": "safranum", "gloss": "saffron", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old French",
          "refs": "AHD:1142",
          "words": [
            {"translit": "safron", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "saffron, safranine", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FSD:2157",
          "words": [
            {"translit": "safrâ", "gloss": "yellow, bile", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "FVA:232",
          "words": [
            {"translit": "safrâ", "gloss": "bile", "script": "صفرا ، صفراء"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Italian",
          "refs": "AHD:1142; KLN:1372",
          "words": [
            {"translit": "saf-fior", "gloss": "yellow flower", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Old French",
          "refs": null,
          "words": [
            {"translit": "saflor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "safflower", "gloss": "a plant with orange flowers", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Šfšyr, Šypšyr, Šamšěr",
        "lang": "Pahlavi",
        "refs": "MPP:88; BQT:1294; NYB:186",
        "gloss": "sword"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1294",
          "words": [
            {"translit": "šamšîr", "gloss": "sword", "script": "شمشیر"}
          ],
          "note": "BQT rejects derivation of \"šamšîr\" from \"šam-šîr:lion's paw\" by SKT:468.",
          "quote": {
            "text": "چون شاه بگیرد بکف اندر شمشیر - از بیم بیفکند ز کفها شم شیر",
            "poet": "Asjadî Marvazî"
          }
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:1397; SKT:468; HJB:804",
          "words": [
            {"translit": "scimitar, cimetar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:56:15.627Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','FVA','FSD','PLA','CEL','DEV','PRT','AHD','MPP','BQT','NYB','SKT','HJB','POK','WLD','HRN','HUB','PHD','ARY','AFM','LKT','WEB','IEC','SYN']:\n    v=d.get(k)\n    print(k, '=>', json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T01:56:16.751Z] TOOL RESULT

```
KLN => {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON => {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVA => {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
FSD => {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
PLA => {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
CEL => {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Ha
DEV => {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PRT => {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
AHD => {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MPP => {"title": "W. B. Henning, \"A List of Middle-Persian and Parthian Words\", Bulletin of the School of Oriental Studies IX (1937–39), pp. 79–92", "edition_found": "1958", "kind": "archive_djvu", "url": "https://archive.org/details/henning-1958-mitteliranisch", "identifier": "henning-1958-mitteliranisch", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt", "page_offset": "l
BQT => {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
NYB => {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT => {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
HJB => {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
POK => {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD => {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN => {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB => {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD => {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
ARY => {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
AFM => {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT => {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
WEB => {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
IEC => {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN => {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-14T01:56:21.962Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FSD','DEV','MPP','NYB','SKT','HJB','PLA','AFM','ARY','PHD','LKT','BQT','MON','AHD','AFA','PHN','LAM','DOZ','TTS']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('====',k)\n    for f in ['kind','local_file','page_offset','lookup_hint','scans','notes','url']:\n        if v.get(f): print('  ',f,':',str(v[f])[:500])\n\""
}
```


## [2026-09-14T01:56:22.846Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo '---MATRIX---' && head -80 data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:56:23.273Z] TOOL RESULT

```
==== KLN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   notes : Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)
   url : https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein
==== FSD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
   page_offset : vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
   notes : Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt
   url : https://archive.org/details/in.ernet.dli.2015.147439
==== DEV
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt
   page_offset : leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : French headword in caps at line start.
   notes : Devic's text is also printed as the supplement of Littré (dictionnairedela00littuoft).
   url : https://archive.org/details/dictionnairety00devi
==== MPP
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt
   page_offset : leaf = printed - 14 (e.g. leaf 7 = p.21). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's Table IV entry for MPP is garbled in the OCR (reads like a Persian title, 'Honari darbareh Zaban Farsi ... 1961'); Table III credits MPP to Henning, so this is most likely 'Mitteliranisch'. Treat identification as tentative and verify that cited page numbers fall in 20-130.
   notes : CORRECTED 2026-09-05: Nourai's Table IV no. 66 identifies MPP as Henning's BSOS IX word-list (pp. 79–92), not "Mitteliranisch". The local file labelled MPP.txt is Mitteliranisch and does NOT contain the cited material; MPP:79 is simply the article's first page. The article itself is not on disk (JSTOR/Cambridge Core).
   url : https://archive.org/details/henning-1958-mitteliranisch
==== NYB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
   notes :  local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)
   url : https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg
==== SKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
   notes : Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.
   url : https://archive.org/details/aconciseetymolo01skeagoog
==== HJB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt
   page_offset : leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
   url : https://archive.org/details/hobsonjobsonagl02croogoog
==== PLA
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}]
   notes : Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).
   url : https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)
==== AFM
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   page_offset : 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   lookup_hint : Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
   notes : Arabic OCR fair; Syriac/Latin etyma partially garbled.
   url : https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)
==== ARY
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
   notes : Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)
==== PHD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
   url : https://archive.org/details/a-concise-pahlavi-dictionary
==== LKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   page_offset : leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
   url : https://archive.org/details/etymologische00lokoguat
==== BQT
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, 
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds a
   notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noo
   url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vo
==== MON
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incom
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
   notes : covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full
   url : https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)
==== AHD
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg
   notes : AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.
   url : https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only
==== AFA
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt
   page_offset : leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
   notes : Built from djvu.xml.
   url : https://archive.org/details/diearamischenfr00fraegoog
==== PHN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt
   page_offset : leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
   notes : Built from djvu.xml.
   url : https://archive.org/details/dictionnairetym01pihagoog
==== LAM
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt
   page_offset : leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : French headword in caps at line start with running heads like '2 ABRI'.
   notes : Built from djvu.xml.
   url : https://archive.org/details/remarquessurles00lammgoog
==== DOZ
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt
   page_offset : leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Dutch headword in caps at line start.
   notes : Built from djvu.xml.
   url : https://archive.org/details/oosterlingenver00dozygoog
==== TTS
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt']
   page_offset : TTS_pages.txt: 253 leaves; printed page N = leaf N+30.
   lookup_hint : Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.
   notes : Open full text (public domain). OCR rough (Fraktur + Turkic transliteration).
   url : https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)
```


### [2026-09-14T01:56:23.322Z] TOOL RESULT

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
---MATRIX---
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
```


## [2026-09-14T01:56:28.115Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^chiffon\\|chiffe\\|shaffa\\|šaffa' KLN_1966.txt | head -20"
}
```


### [2026-09-14T01:56:28.206Z] TOOL RESULT

```
7359:chiffonier
7396:chiffon,  n.,  a  sheer  silk  fabric  used  for  women’s dresses.  —  F.,  fr.  chiffe,  ‘rag’,  pi.  ‘clothes’,  fr. Arab,  shiff,  ‘light  garment’,  fr.  shaffa,  it  was  fine and  transparent’  (said  of  materials).
7398:chiffonier,  n.,  a  high  chest  of  drawers.  —  F.  chif- fonnier,  fr.  chiffon,  ‘rag’.  See  prec.  word  and  -ier.
```


## [2026-09-14T01:56:29.257Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'saffron\\|safflower\\|za.faran\\|zaferan' KLN_1966.txt | head -30"
}
```


### [2026-09-14T01:56:29.333Z] TOOL RESULT

```
2097:Alauda,  n.,  a  genus  of  birds,  the  skylark  (orni- thol.)  —  ModL.,  fr.  L.  alauda,  ‘lark’,  of  Gaulish origin,  and  prob.  literally  meaning  ‘tufted’, alazor,  n.,  the  safflower.  —  Sp.,  fr.  Arab,  al-usfur, in  vulgar  pronunciation  al-'osj'dr,  fr.  al-,  ‘the’, and  'usfhr,  resp.  osfdr,  ‘safflower’.
8011:Cnicus,  n.,  a  genus  of  plants  of  the  thistle  family (hot.)  —  L.  emeus,  meats,  ‘safflower’,  fr.  Gk. xvrpto;,  ‘safflower’,  whence  Gk.  xvr(x6<;,  Dor. xvixop,  ‘pale,  yellow,  tawny’;  cogn.  with  OE.
9712:crocein,  croceine,  n.,  any  of  several  yellow  and red  dyes  ( chem .)  —  Formed  with  chem.  suff.  -in, resp.  -ine  fr.  L.  croceus,  ‘saffron-colored’,  fr. crocus,  ‘saffron’.  See  Crocus.
9727:fron  colored’,  fr.  xp6xoc,  ‘saffron’.  See  next word.
9728:Crocus,  n.,  a  genus  of  plants  of  the  iris  family (hot.)  —  L.,  fr.  Gk.  xp4xoc,  ‘saffron’,  a  word of  Sem.  origin.  Cp.  Heb.  karkSm,  Arab,  kiir- kum,  ‘saffron’,  Aram.-Syr.  kurk-md,  Akkad. kurkdnu,  ‘saffron’.  OI.  kuhkumam,  ‘saffron’,  is prob.  a  Sem.  loan  word;  cp.  Manfred  Mayr- hofer,  A  Concise  Etymological  Sanskrit  Diction¬ ary,  Heidelberg,  1956,  I,  p.219  s.v.  kuhkumam. Derivative:  crocus-ed,  adj.
18021:Derivatives:  honest-ly,  adv„  honest-ness,  n. honesty,  n.  —  ME.  honeste,  fr.  OF.  honeste  (F. honnetete ),  fr.  L.  honestatem,  acc.  of  honestas , 'honor,  honesty’,  fr.  honestus.  See  prec.  word and  -y  (representing  OF.  -e,  -ee). honey,  n.  —  ME.  huni 3,  honi,  fr.  OE.  hunig,  rel. to  OS.  huneg,  honeg,  ON.  hunang ,  Dan.  honning, Swed. honung, OFris.  hunig,  MDu.  honich,  honinc, Du.  honig,  honing,  OHG.  honang,  honag,  MHG. honec,  hdnic,  G.  Honig,  ‘honey ,  and  prob. cogn.  with  OI.  kahcanam,  ‘gold’.  Dor.  Gk. xvax6<;,  Gk.  xvy;x 6?,  ‘pale  yellow’,  xvijx6;, ‘safflower’,  OPruss.  cucan  (=  cuncari),  ‘brown’, W.  canecon,  ‘gold’.  Cp.  Cnicus.
20895:kusum,  n.,  the  safflower  (India).  —  Hind.,  fr.  OI.
33477:saffian,  n.,  a  kind  of  leather  made  of  goatskins  or sheepskins.  —  Russ,  safyan,  fr.  Turk,  sakhtiyan, fr.  Pers.  sakhtiyan,  ‘goat’s  leather’, safflower,  n.  —  Either  fr.  Du.  saffloer,  or  directly from  OF.  saflor,  fr.  earlier  It.  sajfiore,  which  is prob.  a  hybrid  compounded  of  Arab.  $afra\ fern,  of  (if far,  ‘yellow’,  and  It .fiore,  ‘flower’.  See flower.
33478:saffron,  n.,  a  species  of  crocus.  —  ME.  saffron, fr.  OF.  (=  F.)  safran,  fr.  ML.  safranum,  fr. Arab,  za'faran,  whence  also  It.  zafferano,  Sp. azafran.
33479:Derivatives:  saffron,  tr.  v.,  to  color  with  saffron, saffron-y,  adj.
33480:safranine,  n.,  a  synthetic  orange-red  dyestuff (chem.)  — -  F.,  formed  with  chem.  suff.  -ine  fr. safran,  ‘saffron’.  See  prec.  word, safrole,  also  safrol,  n.,  a  poisonous  oil,  C10H10O2 ( chem .)  —  A  hybrid  coined  fr.  F.  safran  (see saffron)  and  -ol,  a  suff.  derived  fr.  L.  oleum,  ‘oil’, sag,  intr.  v.  —  Late  ME.  saggen,  prob.  of  Scand. origin.  Cp.  Dan.  sakke,  Swed.  sacka,  dial. Norw.  sakka,  ‘to  sink,  subside’,  Du.  zakken, of  s.m.  These  verbs  are  denasalized  derivatives of  the  Teut.  base  *sinkwan,  ‘to  sink’  (see  sink), and  have  a  frequentative  meaning.
35938:Sophora,  n.,  a  genus  of  plants  of  the  pea  family (hot.)  —  ModL.,  fr.  Arab.  }u/drah,  ‘yellow plants’,  which  is  rel.  to  tisfaru,  fern,  safra', ‘yellow’.  See  saffron.
40492:turma,  n.,  troop,  squadron  of  horse  (Roman antiq.)  —  L.,  of  uncertain  origin.  It  is  possibly rel.  to  turba,  crowd’  (see  turbid), turmeric,  n.,  an  aromatic  plant  of  the  ginger  fam¬ ily  (Curcuma  longa).  —  Fr.  earlier  tormarilh,  tar- maret,  fr.  F.  terre  merite,  ‘saffron’,  fr.  ML.  terra merita  ( =  deserved  earth’),  a  folk-etymological corruption  of  Arab,  kurkum,  ‘curcuma’.  See Curcuma.
```


## [2026-09-14T01:56:36.456Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport sys\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# build line -> leaf\nleaf=0\nm={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor n in [7396,33477,33478,33480,35938]:\n    print(n, 'leaf', m[n], '=> approx printed page', (m[n]-12)*2)\nEOF"
}
```


## [2026-09-14T01:56:37.484Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'scimitar\\|cimetar\\|shamshir\\|samshir' KLN_1966.txt SKT.txt HJB.txt | head -20"
}
```


### [2026-09-14T01:56:37.780Z] TOOL RESULT

```
7396 leaf 156 => approx printed page 288
33477 leaf 729 => approx printed page 1434
33478 leaf 729 => approx printed page 1434
33480 leaf 729 => approx printed page 1434
35938 leaf 782 => approx printed page 1540
```


### [2026-09-14T01:56:37.886Z] TOOL RESULT

```
HJB.txt:10951:1684.— "The  Souldiers  do  not  wear Hangers  or  Scimitars  like  the  Pernant,  but broad  Swords  like  the  Switzers.  .  .  .'*— Tavernier,  E.T.  ii.  65 ;  [ed.  Bali,  i.  157].
HJB.txt:19488:"  .  .  .  Bv  this  scimitar, That  slew  the  Sophy,  and  a  Persian  prince That  won  three  fields  of  Sultan  Soliman .  .  ."♦  Merchant  of  Venice,  ii.  1.
HJB.txt:20859:ri596.—  "...  this  scimitar
KLN_1966.txt:34071:Scilla,  n.,  a  genus  of  plants,  the  squill.  —  L.,  ‘the squill’,  fr.  Gk.  axlXXx.  See  squill, scimitar,  n.,  a  curved  Oriental  sword.  —  It.  sci- mitarra  (whence  also  F.  cimeterre),  fr.  Pers. shimshir,  ‘scimitar,  saber’.
```


## [2026-09-14T01:56:48.011Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==157' KLN_1966.txt | head -5 && echo '=====SAFF' && awk 'BEGIN{RS=\"\\f\"} NR==730' KLN_1966.txt | head -5"
}
```


### [2026-09-14T01:56:49.086Z] TOOL RESULT

```
ophistry.  — - F.  chicanerie,  fr.  chicaner.  See  chicane,  v.  and -ery.
chich,  n.,  the  chick-pea  ( obsol .)  —  F.  chiche.  See chick-pea.
chick,  n.  —  Shortened  form  of  chicken, chickadee,  n.,  the  black-capped  titmouse.  —  Imi¬ tative  of  its  note.
chickaree,  n.,  the  red  squirrel  of  North  America. —  Imitative  of  its  cry.
chicken,  n.  and  adj.  —  ME.  chiken,  fr.  OE.  cicen, cycen,  rel.  to  MDu.  kiekijen,  kuken,  Du.  kieken, kuiken,  ON.  kjuklingr,  Swed.  kyckling,  Dan. kylling,  G.  Kiichlein,  ‘chicken’.  All  these  words are  diminutives  formed  fr.  base  *kjuk-,  imitative of  the  sound  characteristic  of  a  chicken.  Cp. cock.
=====SAFF
onsecration.  —  ME.,  verbal  noun  of sacren,  ‘to  consecrate’.  See  sacred  and  -tag,  suff. forming  verbal  nouns.
sacrist,  n.,  a  keeper  of  the  sacred  vessels;  sacris¬ tan.  —  ME.,  fr.  Eccles.  L.  sacrista,  fr.  L.  sacer, fern,  sacra,  neut.  sacrum,  ‘holy,  sacred’.  See sacred  and  -ist.
sacristan,  n.  —  ME.,  fr.  Eccles.  L.  sacristanus,  fr. sacrista.  See  prec.  word  and  -an  and  cp.  sexton, which  is  a  doublet  of  sacristan. sacristy,  n.,  an  apartment  in  a  church  where  the sacred  vessels,  vestments,  etc.,  are  kept;  vestry. —  Eccles.  L.  sacristia,  fr.  Late  L.  sacrista.  See sacrist  and  -y  (representing  F.  -ie). sacro-,  before  a  vowel  sacr-,  combining  form meaning  ‘holy,  sacred’.  —  From  the  stem  of  L. sacer,  fern,  sacra,  neut.  sacrum,  ‘holy,  sacred’. See  sacred.
sacro-,  before  a  vowel  sacr-,  combining  form  de¬ noting  1)  the  sacrum;  2)  sacral  and.  —  See  sa¬ crum.
sacrosanct,  adj.,  very  sacred.  —  L.  sacrosanctus, ‘consecrated  with  religious  ceremonies,  doubly sacred’,  compounded  of  sacer,  ‘holy,  sacred’, and  sanctus,  of  s.m.  See  sacro-,  ‘holy’,  and sanctus,  saint.
```


## [2026-09-14T01:57:05.055Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 699 749 179 439; do echo \"--- leaf(0based) $n ---\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -2; done"
}
```


### [2026-09-14T01:57:06.302Z] TOOL RESULT

```
--- leaf(0based) 699 ---
ler  (F.  reconcilier),  fr.  L.  reconciliare,  ‘to  bring together  again,  reconcile',  fr.  re-  and  conciliare, ‘to  bring  together’.  See  conciliate.
Derivatives:  reconcil-able,  adj.,  reconcil-abil-ity, n.,  reconcil-able-ness,  n.,  reconcil-abl-y,  adv., reconcil-ee,  n.,  reconcile-ment,  n.,  reconcil-er,  n., reconcil-ing-ly,  adv.,  reconciliation  (q.v.),  recon- cili-at-ory,  adj.
--- leaf(0based) 749 ---
second'.  See  second,  adj. securable,  adj.  —  Formed  fr.  the  verb  secure  (see next  word)  with  suff.  -able, secure,  adj.,  safe.  —  L.  securus,  ‘free  from  care’, fr.  se-  and  cura,  ‘care’.  See  cure,  ‘care’,  and  cp. sure  and  sicker,  which  are  doublets  of  secure.
securiform
--- leaf(0based) 179 ---
om  comis,  ‘courteous,  kind,  affable’, fr.  OL.  cosmis,  which  prob.  stands  for  co-smi-s and  lit.  means  ‘he  who  smiles  with’,  and  is formed  fr.  co-  and  the  I.-E.  base  of  *smei-,  ‘to smile,  wonder’;  see  mirror,  smile.  OL.  cosmis became  L.  comis  in  the  sense  of  the  Latin  pho¬ netic  law,  according  to  which  s  disappeared  be¬ fore  d,  l,  m  or  n.  Cp.  L.  lubricus  (for  *sliibri- cos),  ‘slippery’,  mirus  (for  *smeirns),  ‘wonder¬ ful’,  nidus  (for  *nizdos),  ‘nest’,  ponere  (for *posnere,  fr.  *po-si-nere),  ‘to  place’,  primus  (for *prismos),  ‘first’;  see  lubricate,  miracle,  nest, position,  prime.
comma,  n.  —  L.,  ‘division  of  a  period;  comma’, fr.  Gk.  xojqj.*,  ‘a  piece  cut  off ;  a  short  clause’, fr.  xo7ttelv,  ‘to  cut  off’,  which  is  cogn.  with L.  capo,  ‘castrated  cock’.  See  capon,  and  cp. acopic,  Coptis,  pericope,  syncope.
--- leaf(0based) 439 ---
e,  adj.  —  Formed  with  suff.  -ive  fr.  L.
irrigatus,  pp.  of  irrigare.  See  irrigate, irriguous,  adj.,  moist,  irrigated.  —  L.  irriguus, ‘watered,  wet’,  from  the  stem  of  irrigare.  See irrigate.  For  E.  -ous,  as  equivalent  to  L.  -us, see  suff.  -ous.
```


## [2026-09-14T01:57:29.067Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'SCIMITAR\\|CIMETER\\|CIMETAR' SKT.txt | head && echo '---HJB---' && grep -n -i '^SCYMITAR\\|^SCIMITAR\\|SHAMSHIR\\|SUMSHEER' HJB.txt | head"
}
```


### [2026-09-14T01:57:29.142Z] TOOL RESULT

```
16640:Scimet&r,  Cimet&r.  (F.  pr  Ital.  - Ters.  ?)  F.  cim^Urt^,  *%  scj'mitar;'  Cot. Cf.  Ital.  fd'mifarm,  '»  simitar,'  Florio, Prob.  from  Pcrs.  sAimskfr,  sAamsklr,  "a cimeter.'  Rich.  Diet,  p.  009.  Lit.  lion's claw.  —  rers  jAam,  nail,  claw;  iM/r,  lion.
---HJB---
```


## [2026-09-14T01:57:30.772Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'samser\\|šamšēr\\|samsir\\|shafsher\\|sapsēr\\|šafšēr' PHD.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:57:30.836Z] TOOL RESULT

```
PHD.txt:579:šafšēr [!pfyl | M ут] = šamšēr.
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
PHD.txt:3923:sword sneh, šamšër, (šafšēr). swordsmith čēlāngar.
PHD.txt:4522:> šabestān šafšēr šiftālūg šiftēnag šaš!
NYB_vol2_glossary.txt:3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. below); if it is attached to a subst. it never depends on it as its poss., but refers to another w. in the sentence; it is never governed by a prep. (single exception 54%, v. s. v. apar); it has an independent form aš (g. v.). It expresses 1. the gen. his, her, its: api-š bar xrat and its fruit is Wisdom 6613; fravahr i Zartuxst api-$ tan gohr Z.’s fra- vashi and his corporeal substance 4226-27; 4-$ his, her, its: tāt matan 1-š 0... 4714; — 2. for, to him (ete.): apt-š... 6 patirak āyēnd go to meet him 741-2; api-š vát-ic hayyār bavet 25°; — 3. dir. obj.: api-š nod be barem 3915; ka-š vir royét x"arét he who believes in it eats 1002; (he said) ku-"'$ man be 6 vahist ne hilom” 3425 (dir. speech aš); — 4. the agent, passim: cigon- aš dit as soon as by him was seen 19!?; ka-š hàn saxtan āšnūt 2219; Pourušāsp hac Zartuzšt, pat višopišn i haciš, -(a)š škujt tarsenit P. was terribly frightened by him (the Karap) because of Z. that he should suffer destruction by him 488-9; still unexplained is the construction in api-š ... šamšēr HDWN-yt' (commonly for pres. girét) u tak BYDWN.x, (com- monly for kunēt, but cf hištan) 2220-21, — Proleptically, anticipating a subst.: cigon- aš dit kanicak as soon as she, the girl, saw 15°; adak-iš mčnit Pouruščisp kü then he, P., thought 40%; api-§ guft, apar apäc vast, Pourušāsp and he, P., returning said 5117-18; — anaphorical, taking up a
NYB_vol2_glossary.txt:4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
```


## [2026-09-14T01:57:41.587Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor fn,lines in [('SKT.txt',[16640]),('KLN_1966.txt',[34071,7396,33477])]:\n    txt=open(fn,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0; m={}\n    for i,l in enumerate(txt,1):\n        m[i]=leaf; leaf+=l.count('\\f')\n    for n in lines:\n        print(fn,n,'leaf',m[n])\nEOF\necho '--- SKT leaf->printed = leaf-20'"
}
```


## [2026-09-14T01:57:42.903Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'scymitar\\|shamsher\\|shumsheer\\|SWORD' HJB.txt | sed -n '1,25p'"
}
```


### [2026-09-14T01:57:42.924Z] TOOL RESULT

```
SKT.txt 16640 leaf 444
KLN_1966.txt 34071 leaf 742
KLN_1966.txt 7396 leaf 156
KLN_1966.txt 33477 leaf 729
--- SKT leaf->printed = leaf-20
```


### [2026-09-14T01:57:42.988Z] TOOL RESULT

```
1658:1882. — "We  received  a  message  from the  Acali  who  had  set  fire  to  the  village. ....  These  fanatics  of  the  Seik  creed acknowledge  no  superior,  and  the  ruler  of the  country  can  only  moderate  their  frenzy by  intrigues  and  bribery.  They  go  about everywhere  with  naked  swords,  and  lavish their  abuse  on  the  nobles  as  well  as  the peaceable  subjects.  .  .  .  They  have  on several  occasions  attempted  the  life  of  Run- jeet  Singh." — Bwrnea^  TraveUy  ii.  10-11.
1871:c.  1345.— "The  Master  of  the  Ship  is  like a  flrreat  amir;  when  he  goes  ashore  the archers  and  the  blackamoors  march  before him  with  javelins  and  swords,  with  drums and  horns  and  trumpets." — Ibn  BattUa,  iv. 93.
1904:*' Homicide  is  here  a  jest,  and  goes  with- out punishment.  Debtors  are  made  over  to their  creditors  as  slaves ;  and  some  of  these, preferring  death  to  slavery,  will  with  drawn swords  rush  on,  stabbing  all  whom  they  fall in  with  of  less  strength  than  themselves, until  they  meet  death  at  the  hands  of  some one  more  than  a  match  for  them.  This man,  the  creditors  then  sue  in  Court  for  the dead  man's  debt."— In  India  in  the  XVtk C.  45.
1933:„  "  If  the  Prince  is  slain  the  amonchi, who  are  numerous,  would  avenge  him desperately.  If  he  be  injured  they  put  on festive  raiment,  take  leave  of  their  parents, and  with  fire  and  sword  in  hand  invade  the hostile  territory,  burning  every  dwelling,  and slaying  man,  woman,  and  child,  sparing  none, until  they  themselves  faW^—Ibid.  237-8.
2217:1573. — "  In  this  city  {Fez)  there  ie  a  very great  building  which  tney  call  Pani^naj where  the  Chnstian  captives  used  to  labour at  blacksmith's  work  and  other  crafts  under the  superintendence  and  orders  of  renegade headmen  .  .  .  here  they  made  cannon  and powder,  and  wrought  swords,  cross-bows, and  arauebuases.  "—Jformo/,  Dete.  Oenaral d€  Affrvcoy  lib.  iii.  f .  92.
3537:1826.—'*  AU  the  BheelB  whom  we  saw  to- day were  small,  slender  men,  less  broad- shouldered  .  .  .  and  with  faces  less  Celtic than  the  Puharees  of  the  Bajmidial.  .  .  . Two  of  them  had  rude  swords  and  shields, the  remainder  had  all  bows  and  arrows." — ffeber,  ed.  1844,  ii.  76.
3952:1696.— "Being  informed  where  the  Chief man  of  the  Choultry  lived,  he  (Dr.  Brown) took  his  sword  and  pistol,  and  being  followed by  his  boy  with  another  pistol,  and  his  horse keeper.  .  .  ."—In  Wkeelery  i.  300.
4096:1825.—"  We  paased  a  number  of  Biin- JazTQM  who  were  carrying  salt.  .  .  .  They .  .  .  had  all  bows  .  .  .  arrows,  sword  and diidd.  .  .  .  ESven  the  children  had,  man^ of  them,  bows  and  arrows  suited  to  their strength,  and  I  saw  one  young  woman equipped    in    the   same   manner.  * — Heber,
4182:e.  1190. — "Very  grieved  was  Sarang  Deva. Constantly  he  performed  the  worship  of  the Arihant ;  the  Buddhist  religion  he  adopted  ; he  wore  no  sword."— !%«  Poem  qf  Uhand BardcU,  paraphr.  by  Beamfty  in  hid.  Ant, i.  271.
4459:And  Red  Coat  to  his  Back  ; A  Persian  Sword  to  dog  his  side,
4611:1772.  —  "  BackBenias.  Foot  soldiers whose  common  arms  are  only  sword  and tBLTget."— Glossary  in  Orose's  Voyage,  2nd ed.  [This  is  copied,  as  Mr.  Irvine  shows, from  the  Glossary  of  1757  prefixed  to  An Address  to  the  Proprietors  qf  E.  I.  Stock,  in. HolwelVs  Indian  Tracts,  8rd  ed.,  1779.]
4612:1788. — "  Buxenries- Foot  soldiers,  whos9 common  arms  are  swords  and  targets  or spears." — Indian  Vocabulary  (Stockdale's).
5870:GHEE8E,s.  Thisword  is  well  known to  be  used  in  modern  English  slang  for "anything  good,  first-rate  in  quality, eenuine,  pleasant^  or  advantageous" {Slang  Diet.).  And  the  most  probable source  of  the  term  is  P.  and  H.  cktz, *  thing.'  For  the  expression  used  to be  common  among  Anglo-Indians,  e.a., "  My  new  Arab  is  the  real  c^ia  ; "  These  cheroots  are  the  real  cfciz,"  i.e. the  real  thing.  The  word  may  have been  an  Anglo-Indian  importation, and  it  is  difficult  otherwise  to  account for  it.  [This  view  is  accepted  by  the N.E.D.;  for  other  explanations  see 1  ser.  N.  (h  Q.  viii.  89  ;  3  ser.  vii. 465,  605.]
6270:.  .  .  at  night  parading  about  with  his  spear, shield,  and  sword,  and  assuming  a  most terrific  aspect,  until  all  the  family  are asleep;  when  he  gobs  to  slbbf  too."— WaitarMon,  F.  M,  i.  295.
6329:*  a  tnin  plate  of  metal,'  which  is  no  doubt the  origmal  of  the  Old  EngliA  chape  for the  metal  plate  on  the  sheath  of  a sword  or  dagger.*  The  word  in  thia sense  is  not  in  the  Portuguese  Dic- tionaries;  but  we  find  *homem  eha- pado,'  explained  as  *a  man  of notable  worth  or  excellence,*  and Bluteau    considers    this   a    metaphor
6340:In  Captain  Forrest's  work,  quoted below,  a  golden  badge  or  decoration, conferred  on  him  by  the  King  of  Achin, is  called  a  chapp  (p.  55).  The  portrait of  Forrest,  engraved  by  Sharp,  shows this  badffe,  and  gives  the  inscription, translatea :  "Capt.  Thomas  Forrest, Orancayo  [see  QBANKAY]  of  the  Golden Sword.    This  chapp  was  conferred  as
6773:stout, who  such  an  arr'gance  of  the  sword  hath
7542:„  **  Of  this  realm  of  Bengala^  and  of other  four  realms  its  neighbours,  the  Gen- toos  and  Moors  of  those  parts  sav  that  God has  g^ven  to  each  its  peculiar  gift :  to  Ben- gala  infantry  numberless;  to  the  Kingdom of  Orixa  elephants ;  to  that  of  Bisnaga  men most  skilful  in  the  use  of  sword  and  shield ; to  the  Kingdom  of  Dely  multitudes  of  cities and  towns ;  and  to  Cou  a  vast  number  of horses.  And  so  naming  them  in  this  order they  give  them  these  other  names,  viz. : Etpaty^  Oaspaty,  Noropaty,  Buapaty,  and Coapaty. "—^anxM,  ibid,  [These  titles  ap- pear to  be  Atvapatiy  "Lord  of  Horses  ; Qajapati  ;  Narapatiy  "  Lord  of  Men  "  ; BhUpaHy  "Lord  of  Earth";  Oopaiiy  "Lord of  Cittle."]
7583:1618.— "CMsaokB  {Comccki)  ,  .  ,  joa should  know,  is  not  the  name  of  a  nation, but  of  a  collection  of  people  of  various countries  and  sects  (though  most  of  them Christians)  who  without  wives  or  childron, and  without  horses,  acluiowledge  obedienco to  no  prince ;  but  dwelling  far  from  cities  in fastnesses  amon^  the  woods  or  mountains, or  rivers  .  .  .  live  bv  the  booty  of  their swords  .  .  .  employ  themselves  in  perpetual inroads  and  cruisings  by  land  and  sea  to  the detriment  of  their  nea[re8t  enemies,  i,e.  of the  Turks  and  other  Mahometans.  ...  As  I have  heard  from  them,  thev  promise  them- selves one  day  the  capture  of  Constantinople, saying  that  Fate  has  reserved  for  them  the liberation  of  that  country,  and  that  they have  clear  prophecies  to  that  eifect." — P, delta  ValUy  i.  614  seq.
7804:0BEA8E,  CBI8,  &c.,  s.  A  kind of  dagger,  which  is  the  character- istic weapon  of  the  Malay  nations ; from  the  J  avanese  name  of  the  weapon, adopted  in  Malay,  Aru,  ibtm,  or  kres {^%F<wrey  Did,  Javanais-Fran^is,  1376, VrawfurtPB  Malay  Diet,  s.v.,  JansZy JavaanschrNederl.  Woordenboek,  202). The  word  has  been  generalised,  and is  often  applied  to  aiialogous  weapons of  other  nations,  as  'an  Arab  crease^* &c.  It  seems  probable  that  the  H. word  kirich^  applied  to  a  straight sword,  and  now  almost  specifically  to a  sword  of  European  make,  is  identical with  the  Malay  word  hks.  See  the form  of  the  latter  word  in  Barbosa, almost  exactly  kirich.  Perhaps  Turki iilich  is  the  original.  [Platts  gives Skt.  kritij  *a  sort  of  knife  or  dagger.'] If  Rei'naud  is  right  in  his  translation of  the  Arab  Relations  of  the  9th  and lOt.h  centuries,  in  correcting  a  reading, otherwise    unintelligible,   to   kfrn^  we
8458:1848.— "Jam:  You  have  received  the money  of  the  British  for  taking  charge  of the  dawk ;  you  have  betrayed  your  trust, and  stopped  the  dawkl.  ...  If  you  come in  and  make  your  salilm,  and  promise fidelity  to  the  Ibritish  Government,  I  will restore  to  you  your  lands  .  .  .  and  the  super- intendence of  the  dawkl.  If  you  refuse  I will  wait  till  the  hot  weather  has  gone  pyit, and  then  I  will  carry  fire  and  sword  into vour  territory  .  .  .  and  if  I  catch  you,  I  will iiang  you  as  a  rebel." — Sir  C.  Napier  to  the Jam  of  the  Jokees  (in  Life  of  Dr,  J.  Wileon., p.  440).
8509:And  a  Persian  sword,  and  a  twelve-foot spear,  and  a  pistol  at  my  waist." Sir  A.  C.  Lyali,  The  Old  Pindaree.
9003:by  Europeans  in  Burma,  for  the  hew- ing knife  or  bill,  of  various  forms, carried  by  the  races  of  those  regions, and  used  both  for  cutting  jungle  and as  a  sword.  Dha  is  the  true  Burmese name  for  their  weapon  of  this  kind, but  we  do  not  know  if  there  is  anv relation  but  an  accidental  one  with the  Hind.  word.  [See  drawing  in EgerUm,  Handbook  of  Indian  Arms, p.  84.]
9005:Ctless,  and  sharpened  on  one  side  only, blade  is  set  in  a  handle  of  wood;  a bamboo  root  is  considered  the  best.  The fighting  dao  is  differently  shaped ;  this  is  a long  pointless  sword,  set  in  a  wooden  or ebony  handle ;  it  is  very  heavy,  and  a  blow of  ahnost  incrodible  power  can  be  given  by one  of  these  weapons.  .  .  .  Tlie  weapon  is identioal  with  the  *  parang  latoi*  of  the Malays.  .  .  ,"^Lemn,  Wild  Jtaeet  of  S.E. Tndiaf  S5  teq,
9351:exist  no  longer.  But  I  do  remember  me  to have  seen  a  certain  Chapel,  not  to  be  seen now,  open  on  the  whole  fo^de  (which  was more  than  40  feet  in  length),  and  which along  the  rock  formed  a  plinUi  the  whole lenflth  of  the  edifice,  fashioned  like  our  altars both  as  to  breadth  and  height;  and  on this  plinth  were  many  remarkable  things  to be  seen.  Among  others  I  remember  to hare  noticed  the  story  of  Queen  Pasiphae and  the  bull;  also  the  Angel  with  naked sword  thrusting  forth  from  below  a  tree two  beautiful  flgpires  of  a  man  and  a  woman, who  were  naked,  as  the  Holy  Scripture paints  for  us  the  appearance  of  our  first parents  Adam  and  Etc." — CoutOf  Dec.  YII. Ht.  iii.  cap.  xi.
```


## [2026-09-14T01:57:50.184Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'cymitar\\|shimsheer\\|semsir\\|shamsheer' HJB.txt | head -20"
}
```


### [2026-09-14T01:57:50.243Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:51.206Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=846 && NR<=852 {print \"=== leaf \" NR-1; print substr($0,1,700)}' HJB.txt"
}
```


### [2026-09-14T01:57:52.304Z] TOOL RESULT

```
=== leaf 845
and  and  Sayer  Revenues"  are given,  but  Abkari  is  not  mentioned. Among  the  Receipta  and  Disburse- ments for  1800-1  appears  "Syer  Col- lections, including  Abkaree,  7,81,925."
These  forms  appear  to  have  remained in  force  down  to  1833.  In  the  ac- counts presented  in  1834,  from  1828-d» to  1831-2,  with  Estimate  for  1832-3» Land  Revenue  is  given  separately,  and next  to  it  Syer  and  Abkaree  Revenue. Except  that  the  spelling  was  altered back  U>. Sayer  and  Abkamfy  this  re- mained tiU  1856.  In  1857  the  ac- counts for  1854-5  showed  in  separate lines, —
Land  Revenue, Excise  Duties,  in  Calcutta, Sayer  Revenue, Abkarry  ditto.
In
=== leaf 846
s  were  levied  in  India,  which were  generally  included  under  the  denomi> nation  of  Sayer." — Mill,  H.  of  Br.  India,  v. 417.
1863.— "The  next  head  was  'Sayer,'  an obsolete  Arabic  word,  which  has  the  same meaning  as  'miscellaneoua,'  It  has  latterly been  composed  of  a  variety  of  items  con- nected with  the  Land  Revenue,  of  which the  Revenue  derived  from  Forests  has  been the  most  important.  The  progress  of  im- provement has  given  a  value  to  the  Forests which  they  never  had  before,  and  it  has been  determined  ...  to  constitute  the Revenue  derived  from  them  a  separate  head of  the  Public  Accounts.  The  other  Misc
=== leaf 847
,  part  of  tneir  duty  mtis to  see  that  the  streets  were  kept  clean  ; and  hence  the  modern  word  *  scaTen- ger,'  whose  office  corre^jponds  with  the rakyer  (raker)  of  former  times."  [The meaning  and  derivation  of  this  word have  been  discussed  in  Noies  dr.  Queries^ 2  ser.  ix.  325  ;  5  ser.  v.  49,  452.1
We  can  hardly  doubt  then  that  the office  of  the  Coromandel  scavenger of  the  18th  century,  united  as  we  find it  with  that  of  "  Rentall  General,''  or of  Land-customer,"  and  held  by  a senior  member  of  the  Compuiy's Covenanted  Service,  must  be  under- stood in  the  older  sense  of  Visitor  or Inspector  of  Goods  su
=== leaf 848
onth more  than  before  on  account  of  his  diligence and  assiduity  in  that  post." — Ft.  William. CoTitn.f  in  Longj  245.  It  does  not  appear from  this  what  the  duties  of  the  scavenger in  Mr.  Handle's  case  were.
1829.  —  "The  oversight  of  customable goods.  This  office,  termed  in  Latin  iii/)^^- visvsy  is  translated  in  another  charter  by the  words  search  and  surveyizig,  and  in  the 2nd  Charter  of  Charles  I.  it  is  termed  the BOavage,  which  appears  to  have  been  its most  ancient  and  common  name,  and  that which  is  retained  to  the  present  day.  .  .  . The  real  nature  of  this  auty  is  not  a  toll for  ghoimnffy  but 
=== leaf 849
  either  of  us  both  :  but  our Armenian  had  only  a  Scimeter."  —  (Sir^ Gtorge  Wheler,  Journey  into  Greece,  London, 1682,  p.  252.
1758.— "The  Captain  of  the  troop  .  .  . made  a  cut  at  his  head  with  a  spymetar which  Mr.  Lally  parried  with  his  stick, and  a  Coffree  (Galx«r)  servant  who  attend him  shot  the  I^njerine  dead  with  a  pistol. '* —OriM,  i.  328.
SEAOUNNY,  s.  This  is,  in  the phraseology  of  the  Anglo-Indian marine,  a  steersman  or  quartermaster. The  word  is  the  Pers.  ^uJbfcdni,  from Ar.  zuldcdriy  '  a  helm.'
c.  1580.  —  "Acs  Mocadfies,  Sooaea,  e Vogas.**— PWwor  e  Homo,  Ac.  f.  68?.  ("To- the  Mocndd
=== leaf 850
nt- maior.  I  supplied  the  Native  officers  and N.C.  officers  from  India  with  a  good  pea- jacket  each,  out  of  my  private  means,  and with  a  little  gold-lace  made  them  smart  and happy.
''When  I  visited  Darjeeling  again  in  1872,
I  found  the  remnant  of  my  good  Sapper
officers  living  as  pensioners,  and  waiting  to
give  me  an  affectionate  welcome.
•  •  •  •  •
"My  month's  acting  appointment  was turned  into  four  years.  I  walked  30  miles to  get  to  the  place,  lived  much  in  hovels  and temporary  huts  thrown  up  by  my  Hill-men, and  derived  more  benefit  from  the  climate than  from  my  previous  visit  to  England.  
=== leaf 851
Sevagi,  as  well  as  their  frequent annoyance  of  Uieir  country,  had  b<»eo  so much  facilitated  by  their  resort  to  Bombay, that  Sevsjgi  at  length  determined  to  compel the  Engluh  (Government  to  a  stricter  neu- trality, by  reprisals  on  their  own  port.'*— Orme,  FragmaiU,  78.
1690.— "As  he  whose  Title  ismorf  Ckritiinn, encouraged  him  who  is  its  principal  Adver- sarv  to  invade  the  Rights  of  Christendom, so  did  Senor  Padre  de  Pandora,  the  Principal Jesuite  and  in  an  adjacent  Island  to Bombay,  invite  the  Slddy  to  exterminate all  the  Protestants  there." — Ovington,  157.
1750-60.— "  These  (islands)  were  formerly in  t
```


## [2026-09-14T01:57:58.218Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==849' HJB.txt | tail -c 1800 && echo '#### LEAF849 head' && awk 'BEGIN{RS=\"\\f\"} NR==850' HJB.txt | head -c 900"
}
```


### [2026-09-14T01:57:59.410Z] TOOL RESULT

```
 <pip€L  TpcuatKfi v^HifffAara  o^^ird  koI  ffafij/z-iipat  al  B4  e^i (nrddai  fiapPapiKaL**  —  Quoted  in  Suidas Lexicon,  a.  v.
1595.—
"  .  .  .  Bv  this  scimitar, That  slew  the  Sophy,  and  a  Persian  prince That  won  three  fields  of  Sultan  Soliman .  .  ."♦  Merchant  of  Venice,  ii.  1.
*  In  a  Greek  tFanslation  of  Shakspere,  pub- lished some  years  ago  at  Constantlnonle,  thi$  Hm U  omitted  I
1610.—'*.  .  .  Anon  the  Patron  startio^ up,  as  if  of  a  sodaine  restored  to  life :  like a  mad  man  skips  into  the  boate,  and  draw- ing a  Turkise  C^nnitar,  beginneth  to  hj about  him  (thinking  that  his  ▼nwwll  had been  surprised  by  Pirats),  when  they  &I1 leapt  into  the  sea ;  and  diuing  vnder  water like  so  many  Diue-dappers,  ascended  with- out the  reach  of  his  furie.'* — Sand]fs,  He- lotion,  kc,  1615,  p.  28.
1614.  —  "Some  days  ago  I  visited  the house  of  a  goldsmith  to  see  a  ■#»awi4*«T> {ecimiiarra)  that  Nasuhbash^  the  first  vizir, whom  I  have  mentioned  above,  had  ordered as  a  present  to  the  Grand  Signor.  Soabbaid and  hilt  were  all  of  gold ;  and  all  covered with  diamonds,  so  that  little  or  nothicr of  the  gold  was  to  be  seen." — P.  della  Vailu i.43.   ^
c.  1630.— "They  seldome  go  withoat  their swords  (shaniBhaerB  they  cul  them)  form'd like  a  cresent,  of  pure  metall,  broad,  and sharper  than  any  rasor ;  nor  do  they  valae^ them,  unlesse  at  one  blow  they  can  cut  in two  an  Asinego.  .  .  ."— 5tr  T.  Hrrheri,  ed. 1638,  p.  228.
1675.—"  I  kept  my  hand  on  the  Cock  of my  Carabine ;  and  my  Comrade  followed  a foote  pace,  as  well  armed;  and  our  Jani- zary better  than
#### LEAF849 head
  either  of  us  both  :  but  our Armenian  had  only  a  Scimeter."  —  (Sir^ Gtorge  Wheler,  Journey  into  Greece,  London, 1682,  p.  252.
1758.— "The  Captain  of  the  troop  .  .  . made  a  cut  at  his  head  with  a  spymetar which  Mr.  Lally  parried  with  his  stick, and  a  Coffree  (Galx«r)  servant  who  attend him  shot  the  I^njerine  dead  with  a  pistol. '* —OriM,  i.  328.
SEAOUNNY,  s.  This  is,  in  the phraseology  of  the  Anglo-Indian marine,  a  steersman  or  quartermaster. The  word  is  the  Pers.  ^uJbfcdni,  from Ar.  zuldcdriy  '  a  helm.'
c.  1580.  —  "Acs  Mocadfies,  Sooaea,  e Vogas.**— PWwor  e  Homo,  Ac.  f.  68?.  ("To- the  MocnddnmB,  Beaniimlaa,  sad  oars- men.")
c.  1590.—"  SnkUagxr,  or  hehnsman.  U*^ steers  the  ship  according  to  the  orders  of  the MiCmiin:*~A\n,  i.  280.
1805.  —  "  I  proposed  concealing
```


## [2026-09-14T01:58:03.964Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==849' HJB.txt | grep -n -i -A6 'SCYM\\|SCIM\\|SEMSH\\|shamsh\\|Bcym\\|8CY' | head -40"
}
```


### [2026-09-14T01:58:05.004Z] TOOL RESULT

```
12:SOYMITAB,  s.  This  is  an  English word  for  an  Asiatic  sabre.  The common  Indian  word  is  talrodr  (see TULWAUB).  We  get  it  through  the French  cimiierrt^  Ital.  scvmeterra^  and according  to  Marcel  Devic  originally from  Pers.  stuxmskir  (chimchir  as  he writes  it).  This  would  be  still  very obscure  unless  we  consider  the  constant clerical  confusion  in  the  Middle  Ages between  c  and  f,  which  has  led  to several  metamorphoses  of  words ;  of which  a  notable  example  is  Fr.  car- quois  from  Pers.  Hrkcuh.  Scimecirra representing  shimshir  might  easOy  thus become  scimetirra.  But  we  cannot prove  this  to  have  been  the  real  origin. This  word  (sha/mshir)  was  known  to Greek  writers.     Thus :
13-A.D.  93.~"  .  .  ,  Kal  KaeUmf<ri  t^ »-pe<r/3iJraroi»  irai^a  Mo/)6/3afoi»  /ScurtX^o ir€pi$€i<ra  to  BidBfifUL  Kal  BoO<ra  rov  (njfiay- TTJpa  rod  frarpos  Baicr€\io¥,  Hfrre  aafi^fff}- p6.y  dpofiaj^ofUvrfP  trap*  adroTs.'* — Joatph. ArUiqq.  xx.  ii.  3.
14-c.  A.D.  114.  — "  Ai3pa  <pip€L  TpcuatKfi v^HifffAara  o^^ird  koI  ffafij/z-iipat  al  B4  e^i (nrddai  fiapPapiKaL**  —  Quoted  in  Suidas Lexicon,  a.  v.
15-1595.—
16:"  .  .  .  Bv  this  scimitar, That  slew  the  Sophy,  and  a  Persian  prince That  won  three  fields  of  Sultan  Soliman .  .  ."♦  Merchant  of  Venice,  ii.  1.
17-*  In  a  Greek  tFanslation  of  Shakspere,  pub- lished some  years  ago  at  Constantlnonle,  thi$  Hm U  omitted  I
18-1610.—'*.  .  .  Anon  the  Patron  startio^ up,  as  if  of  a  sodaine  restored  to  life :  like a  mad  man  skips  into  the  boate,  and  draw- ing a  Turkise  C^nnitar,  beginneth  to  hj about  him  (thinking  that  his  ▼nwwll  had been  surprised  by  Pirats),  when  they  &I1 leapt  into  the  sea ;  and  diuing  vnder  water like  so  many  Diue-dappers,  ascended  with- out the  reach  of  his  furie.'* — Sand]fs,  He- lotion,  kc,  1615,  p.  28.
19-1614.  —  "Some  days  ago  I  visited  the house  of  a  goldsmith  to  see  a  ■#»awi4*«T> {ecimiiarra)  that  Nasuhbash^  the  first  vizir, whom  I  have  mentioned  above,  had  ordered as  a  present  to  the  Grand  Signor.  Soabbaid and  hilt  were  all  of  gold ;  and  all  covered with  diamonds,  so  that  little  or  nothicr of  the  gold  was  to  be  seen." — P.  della  Vailu i.43.   ^
20-c.  1630.— "They  seldome  go  withoat  their swords  (shaniBhaerB  they  cul  them)  form'd like  a  cresent,  of  pure  metall,  broad,  and sharper  than  any  rasor ;  nor  do  they  valae^ them,  unlesse  at  one  blow  they  can  cut  in two  an  Asinego.  .  .  ."— 5tr  T.  Hrrheri,  ed. 1638,  p.  228.
21-1675.—"  I  kept  my  hand  on  the  Cock  of my  Carabine ;  and  my  Comrade  followed  a foote  pace,  as  well  armed;  and  our  Jani- zary better  than
```


## [2026-09-14T01:58:14.670Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== DEV safran'; grep -n -i 'SAFRAN' DEV.txt | head -10; echo '=== DEV leaf'; python3 - <<'EOF'\ntxt=open('DEV.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nimport re\nfor i,l in enumerate(txt,1):\n    if re.match(r'\\s*SAFRAN',l,re.I): print('line',i,'leaf',leaf,'printed~',leaf-29)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-14T01:58:15.755Z] TOOL RESULT

```
=== DEV safran
257:On  écrit  aussi  achards  :  c<  Les  acliards  colores  parle  safran,  v (Simonin,  Voyage  à  l'île  de  la  Réunion  '.)  Le  Dictionnaire  de Déterville  écrit  atchar,  qui  est  la  forme  ori^jinidle.  C'est  le persan  ^l=^t  aicluir,  en  malais  -^î  atchar.  Je  ne  saurais dire  quel  est  le  sens  primitif  de  ce  mot,  qui  nous  est  venu, non  de  la  Perse,  mais  des  Indes.
1032:Garthame  ou  safran  bâtard.  Latin  botan.  carthamus.  On tire  ce  mot  de  l'arabe  /oJ^-i  qortoum,  même  sens.  J'ignore quelles  sont  les  raisons,  excellentes  sans  doute,  qui  ont empêché  MM.  Dozy  et  Engelmann  de  compter  cartamo,  car- tama,  parmi  les  mots  espagnols  et  portugais  dérivés  de l'arabe.
1111:Chébile.  Espèce  de  myrobolan.  Dans  les  ouvrages  de  bo- tanique écrits  en  latin  \  on  trouve  kehulus,  quehula,  chcpida, cepuJa.  De  i'arabe-persan  Jol^  kâhouli,  c'est-à-dire,  je pense,  du  pays  de  Kaboul.  On  lit  en  effet  dans  Yakout^ que  le  Jol^  kâhoul  est  t^  une  province  et  ville  de  la  Perse ([ui  produit  le  coco,  le  safran  et  le  myrobolan.  v
1504:Henné.  Arbuste  d'Afrique  et  d'Asie,  dont  les  feuilles séchées  et  réduites  en  poudre  servent  aux  femmes  de  l'O- rient à  se  teindre  les  ongles  en  jaunie  safran,  (i'est  l'arabe
2045:Safran.  Esp.  azafrano,.  portug.  açafrào,  itaL  zafferano. On  trouve,  en  vieux  français,  sajleur,  sajlor.  De  l'arabe- persan  ^^')  zayercm  (avec  l'article  az-za  ferâri) ,  même sens.  Le  mot  est  dans  Razi  (man.  déjà  cité,  p.  /i5  recto).
2048:élymologistes  tirent  le  mot  safre  de  saphir^.  Gela  s'appli- querait difficilement  au  zafre  espagnol  qui  donne  une  co- loration non  pas  bleue,  mais  jaune;  et  M.  Dozy  propose de  rapprocher  zafre  de  l'arabe  ylo  sofi%  cuivre  jaune  [so- fra,  couleur  jaune),  qui  a  donné  l'espagnol  azofat%  laiton. Peut-être  saffre,  zafre  et  l'italien  zafjfcra  sont-ils  simple- ment le  mot  ij^-À^')  zaferCm,  safran,  privé  de  sa  finale^, comme  dans  le  pluriel jiUi;  za'âfir.  Les  alchimistes  appe- laient safran  de  mars  l'ocre  rouge  de  fer;  et  le  safran  des métaux  était  une  préparation  pharmaceutique  où  entraient du  soufre  et  de  l'oxyde  d'antimoine.
2367:Acafrâo,  pg.  voy.  Safran.
2883:Azafrano,  esp.  \oy.  Safran.
4212:Safleur,  voy.  Safran.
4213:Saflor,  voy.  Safran.
=== DEV leaf
line 2045 leaf 234 printed~ 205
line 4214 leaf 293 printed~ 264
```


## [2026-09-14T01:58:16.532Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== NYB 186 (leaf 194)'; awk 'BEGIN{RS=\"\\f\"} NR==195' NYB_vol2_glossary.txt | head -c 1500; echo; echo '=== grep samser NYB'; grep -n '^šamšēr\\|^samser\\|šafšēr' NYB_vol2_glossary.txt | head"
}
```


### [2026-09-14T01:58:17.615Z] TOOL RESULT

```
=== NYB 186 (leaf 194)
’, from spdh.
spāh-pat [sp'hpt'] army leader, general, passim; pl. cas. obl. ~-dn 28. 1113; — 72 ~ twelve leaders, of the twelve signs of the zodiac 7718, 794; 7 ~ the seven planets 7712, 7916, — Arm. lw. from Prth sparapet < *späda-pati-, v.s. v. späh; NP sipahbad.
spähpateh the rank of a general, general- ship 26°. 114°.
Spandarmat [spndrmt ], Spandmat (inscr.) [spndmt]] one of the Amahraspands (q. v.), the goddess of the earth 3919. 5719-22, 633. 9517-15, ]011, 1165-6. 1208; — the name of the twelfth month of the year P1:1. — Av. (336 sq.) Spontā Armaiti-; sponta- < spanta- < *suanta-; hence NW *spanta-, SW *santa- (cf s. v. !sak), both represented in Arm. lws.: 1. spandaramet - in Christian usage rendering Dionysos, 2. sandaramet < "santa aramati ‘abyss, Hell’; NP name of the 12th month Isfand(är, -ärmuö, -ärmed).
Spandi-dät [spndd’t'] n. pr. 2319-305 passim. 1132%. — Av. (1622) Spontē.dāta-; NP Isfandiyar.
Spandidätän patron. of the preceding w. 11522,
spannik  [spn'k]. ménoi 65°, spénak [spyn’k] ménoi 106° spénài [spyn’y] ménói 10215-17, 10312: the Effective, Good Spirit, the creative power of the world, as opposed to ganāk menör (g.v.). — The Phl rendering of Av. (1137 sqq.) sponta- mainyu-; spwk may be spannak < *spanta- enlarged with the suff. -āk and with -nt- > -nn-, or spanäk with the same suff. from the abstr. (1612) spanah-; spénük with the same suff.
www.parsianjoman.org | oe zl eju
spannäk 178
spurr
from 
=== grep samser NYB
```


## [2026-09-14T01:58:24.259Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'amšēr\\|amser\\|amsēr\\|afšēr' NYB_vol2_glossary.txt | head -20; echo '=== leaf 202/203'; awk 'BEGIN{RS=\"\\f\"} NR==203' NYB_vol2_glossary.txt | head -c 1200"
}
```


### [2026-09-14T01:58:25.364Z] TOOL RESULT

```
3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. below); if it is attached to a subst. it never depends on it as its poss., but refers to another w. in the sentence; it is never governed by a prep. (single exception 54%, v. s. v. apar); it has an independent form aš (g. v.). It expresses 1. the gen. his, her, its: api-š bar xrat and its fruit is Wisdom 6613; fravahr i Zartuxst api-$ tan gohr Z.’s fra- vashi and his corporeal substance 4226-27; 4-$ his, her, its: tāt matan 1-š 0... 4714; — 2. for, to him (ete.): apt-š... 6 patirak āyēnd go to meet him 741-2; api-š vát-ic hayyār bavet 25°; — 3. dir. obj.: api-š nod be barem 3915; ka-š vir royét x"arét he who believes in it eats 1002; (he said) ku-"'$ man be 6 vahist ne hilom” 3425 (dir. speech aš); — 4. the agent, passim: cigon- aš dit as soon as by him was seen 19!?; ka-š hàn saxtan āšnūt 2219; Pourušāsp hac Zartuzšt, pat višopišn i haciš, -(a)š škujt tarsenit P. was terribly frightened by him (the Karap) because of Z. that he should suffer destruction by him 488-9; still unexplained is the construction in api-š ... šamšēr HDWN-yt' (commonly for pres. girét) u tak BYDWN.x, (com- monly for kunēt, but cf hištan) 2220-21, — Proleptically, anticipating a subst.: cigon- aš dit kanicak as soon as she, the girl, saw 15°; adak-iš mčnit Pouruščisp kü then he, P., thought 40%; api-§ guft, apar apäc vast, Pourušāsp and he, P., returning said 5117-18; — anaphorical, taking up a
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
=== leaf 202/203
te sense is probably found in Av. (1080) ni-xšata adv. ‘below’, pointing to *xšata- ‘lowered’.
šašom [ššwm] the sixth 83%. — MPrs ššum; MPrth $whwm, šhwm.
Sat [8°t'] glad, happy 2'%. 312, 255. — Av. (1716) šyāta-, šāta-; OP Siyäta- ‘peaceful, happy’, štyāti- ‘peace, happiness’; Ps. :ty; MPrthPrs $’d; Paz. säd; NP sad.
šateh joy, happiness, mirth P 1:9 ($*tyhy). 121%; 41?? join ~ with the following 7, reading the cas. obl. sg. —-e. — MPrth P: dyft; MPrs $dyh, -yy; Ps. Ptyhy.
Sät-Farraxu-Xösröi [š't' plhw' hwslwd] the name of a town: ‘Happy is Glorious Kh.'11429-??; Herzfeld, ApI 137, emends: +gyh’n' plhw? <krt> hwslwd <*pš dst>krt' SM HNHTWN-t' = Gēhān-farrax"-kart- Xosrči (‘Kh. made the world glorious’, the foundation-name of Kh.’s fifth town) api-š Dast-kart näm nihät and he gave it the name D.
šayendakčh [S’dyndkyh] suitableness, worthiness 694, Skr. v. samädhäna. From
šayistan [š?dstn'], 894 Säyitan [š'dytn'] šāy-, 3d p. sg. šāyet [š*dt'], 139 šayet [š*dyt'], pl. šāyēnd [š*dynd], Ist p. pl. šāyem [S’dm]; subju. 3d p. sg. *šāyā [*š*d”] 34!2; pt. = pret. 3d p. sg. šāytst,
310 šāyī
```


## [2026-09-14T01:58:39.259Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 200 201 202; do echo \"=== 0-based leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | grep -n -i 'amš\\|amsh\\|sword\\|ams[eē]' ; done"
}
```


## [2026-09-14T01:58:39.923Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'sword' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:58:40.315Z] TOOL RESULT

```
Exit code 1
=== 0-based leaf 200
20:šamščr [SmSdl] sword 67. 2118 ete. - NP šamšer ; cf. also šifšer.
=== 0-based leaf 201
=== 0-based leaf 202
```


### [2026-09-14T01:58:40.368Z] TOOL RESULT

```
542:apa-stam [’pst’m] reliance 725. 8215, — Paz. awastgm; for *apa-stān < *upa- stäna-; Arm lw. apastan ‘refuge, resort’. apastéh [’p’styh] support 8222. — < Olr *upa-ā-stā-, ci Av. (396) upa-stā- ‘assis- tance, help’. Paz. substitutes dasti. apa-sütak [’pswtk'] probably: treated with magic art, of a sword 2516, 2813, —
546:Cf NP afsün, ausün ‘charm’, afsä ‘a wizard’, afsäyidan ‘to subdue, esp. by magic’, undoubtedly to be connected with NP sidan säy-, farsūdan farsäy (< *fra-) ‘to rub’, the magic treatment con- sisting of some special rubbing or strok- ing of the sword (< *upa-sü-, v. apa-). However, the corresponding OInd. vb. šā- means ‘to sharpen, to whet’ ($ita- ‘sharp’) a sense also attested in Ir: NP afsän, ausän ‘whetstone’; MPrs hswd = hassüd < *ham-süt "whetted' of a sword (Hen- ning, BSOAS XII, 1947, 45), directly to be compared with OInd (RV) sam-sä- ‘to whet’; thus apa-sütak could simply mean ‘sharpened, whetted’. The parallel epi- thet distak (g. v.) is not quite clear.
3601:šamščr [SmSdl] sword 67. 2118 ete. - NP šamšer ; cf. also šifšer.
3771:teh [tyh], tē [ty] 1. ray, splendour, of the sun 716, — 2. point, of the lance 2019, of the foot 112. 3211, — 3, blade, of the sword 2225. 9620, — SW form of tēy > te > te with dropping of -y, or > teh with a secondary -h; Paz. teh. — NW form téy: Arm. lw. teg ‘pike’; NP téy ‘sword, razor; point of a spear; a ray of the sun’; Bal. t'ēg ‘sharp, swift’. Av. (963) bi- taéya- ‘double-edged’, cf 2225, V, also tež, tigr; as to teh nr. 1 cf Skr tejas.
4106:iyöxtan [*NDYHWN-tn'] vēc- (vinj-, v. below) to detach, to separate, to sift, to remove: di véxt šusr his sperm was de- tached from him, with the gl. kū-š Suhr pat post ul Gmat that is: his sperm broke through his skin 5419-29; ātaxš haciš nē šāyet véxtan the fire (hidden in the plant) cannot break forth (from it) 95! (gl.); api-š hösak vest u hošet and its ears having been torn off (by the wind) it withers 12814-15 (uncertain, v. note below); v. also vecisn. — Av. (1312 sq.) vaék-, pres. vaéca-; Skr vic-, pres. vinakti ‘to sift, to winnow, to separate; to inquire, to con- sider’; Arm. lw. wié-em ‘to dispute, to debate’, več ‘discussion’, vičak, v. večak; Bal gécag ‘to sift? < vēc-, gécin, gēšin ‘sieve’ (Makrani, v. Geiger); NP béxtan bez- ‘to sift’. The pres. vinj- is only attest- ed by Cod. K in FrP 18: wync-, but read vij- = the other MSS; as this vb. is al- ways written ideographically in the texts the existence of vinj- in BP is not fully ascertained. However, Psht has winjal ‘to wash, to cleanse’; traces of vinj- in NP are perhaps bunjak ‘carded cotton’ (« *binjak < *vinjak); banjidan (for *binj-) ‘to cut to pieces’ (Steingass); possibly banj ‘one of two women who share a common husband’ < *vincä-, cf vēcak and nēm-vēcak. — [Note: — The Phl translation of 12814-15 is based on a Syriac text which is guite as obscure as the Hebr. original: 'grass on the roof which, as soon as the wind blows upon it, šālef and it withers’. The vb. ŠLP means ‘to extract, to pull, to draw a sword’, so the senses ‘to dry up, to languish’ and ‘to shoot up, to form blades and ears’ seem to be simply conjectured from our Ps. verse. Evidently the Prs. translator took Syr SLP in its ordinary sense ‘to extract, to pull’, and tried to make sense of its Phl. equivalent včatan to the best of his ability. He needed an obj. for it,
4521:gor zat he shot an arrow at the onager 319-20; parr 6 pist zat its wing struck (the bowl with) the meal 925-26; 57 (= 6) fravahr + Zartuxst aš zafar frac zat threw open its mouth towards Z. 4012-13; 5; (= 6) gurg zat zanak the wolf's jaw was struck 506, with the gl. kū-š dahān ēvak apäk dit frot oškan (g. v.); Vidrafš pat dil zat stabbed V. in the heart 292; 25?! (cf s. v. rad 2 b)]; 383; — ēvak 6 dit ~ to knock to- gether 12019-20; ka šamšēr frac zanēt when the sword makes a stroke forward 254 (opp. apāc vēžēt, v. *véxtan); to drive (a peg) down into the soil 202%; tanbür ~ to play on the lute 476, — Av. (490) !gan-, pres. jan-; MPrth jdn jn-; MPrs zdn zn-; Paz. NP zadan zan-. V. also janišn, zanišn, zatak, zatar; cf apa-žand, ozatan.
```


## [2026-09-14T01:58:49.061Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'šifšēr\\|šifser' NYB_vol2_glossary.txt | head -3; echo '=== BQT v3 shamshir'; grep -n 'شمشیر' incoming/BQT/BQT_v3_pages.txt | head -20"
}
```


### [2026-09-14T01:58:49.170Z] TOOL RESULT

```
=== BQT v3 shamshir
5594:‏جان عاشق ترسد از شمشیر
6512:۴ چون شاءبگیرد بکف الدر شمشیر از ‎get‏ بیفکند ز کفهاشم شبر .
6729:‏شمشیر
9048:‏شمشیری دارد و برپشت اوآفتاب میدرشد و آن شمار و شان رسمی دولت ابران است . راجم
13843:و تمگه - شکن و چین ‎ule‏ - نورد پوست - دم شمشیر - نام
14828:شمشیرآبدار هم هست - و هرچیز راست ودراز
14877:‏است که کودال و جای عمیق باشد - و شمشیر
15099:‏وهر شمشیر و کارد و براقی‎ les ‏انگشتان در زیر بغلکی و خاربدن پهلوو کف ]| از آن بر‎
19172:‎ot‏ ودال ابجد, جوهر ‎Et‏ وشمشیر را کویند؛ فر ‎po POG‏ وزن متصود ۰ بمعنی
20393:باشد که‌کارد وشمشیر بدان تيز کنند ۴ سوافانه
20505:‎col‏ وآن‌سنگی‌باشد که‌کارد وشمشیر را (۲)بدان
21894:‏و ‎oT‏ آهنی ‎ath‏ جوهردارکه‌کارد و شمشیر از
22897:‎em‏ اول در عربی جمع شهراست که شهرها باشد بلا دور ؛ ‎tle sett gine‏ وشمشیر دار هم
22912:‎SG -۴‏ >" قراچوری ‏ قراچولی << فراجوری «توروزنامه ص ‎٩۳۹‏ نوعی شمشیرهوهی
22919:شمشی .وشمشیر برداروشمشیرزن هرسه آ مدماست؛
23764:از تیغ و شمشیر ۴ و پیکان ‎wi‏ واسلحة صبقل قطر 9.958 — بنتحزای شله‌داروسکون
23895:وزن و معنی فراچوری است که شمشیر آبدار
24203:‏۱- قلمزن که بد کرد با زیر دست قلم بهتر او را بشمشیر » دست .
36440:بمعتی‌جوهر باشد چنانکه گویند شمشیریی کنخت
36441:عنی‌شمشیر بی‌جوهر( .
```


## [2026-09-14T01:58:50.359Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== PLA za faran'; grep -n -i \"za'far\\|zaʿfar\\|zafaran\\|Safran\" incoming/PLA/PLA_pages.txt | head -20"
}
```


### [2026-09-14T01:58:50.421Z] TOOL RESULT

```
=== PLA za faran
3629:       zum       Lachen        bringt;              falscher        Safran"
3646:ps -        bahram:           "Safran,              Henna"        pers,       9, wahrscheinlich                 aus    dem       pers.    _ı&
4623:       -       $ädi:          "Safran,            Wein"      pers.        8,,
8109:&r -            zardaß:             "flüssiger                  Safran"        aus     pers.       2),,, zardak          12 mp.             ges zardak
8279:Ol;              -       za°farän:                 "Safran!        pers.              8, wahrscheinlich                       aus    dem     pers.    a
8282:          afrz.               safran,             mhd.,    Safran,              dtsch. Safran                    11,
8285:his;                 -    zaCfärani:                    "goldgelb;              Safranfarbe                     Nisba    v.    Safran.
14049:—N_            muläab:        "Parfüm,                 Safran"           pers.             k mul     "Blume"             12,
```


## [2026-09-14T01:58:58.830Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfn='incoming/BQT/BQT_v3_pages.txt'\nlines=open(fn,encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if i in (6480,6512,6520,6729,6740):\n        print(i,'pdfpage',cur)\nEOF\necho '--- print around 6500-6560'\nsed -n '6495,6530p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-14T01:59:00.001Z] TOOL RESULT

```
6480 pdfpage 86
6512 pdfpage 86
6520 pdfpage 86
6729 pdfpage 89
6740 pdfpage 89
--- print around 6500-6560
‎oy‏ است - و در ‎gis‏ بتشدید ‎gE‏ مطلق ‎sy‏
‎ash‏ اعم ازبوی کل و ریحان و غیر آن-ویزبان
علمی ‎ate‏ بمعتی قراغت وآمایش باشد ۴ -وضم
اول پای‌افزاری را کوبند که ‎Ol pn;‏ ازچرم‌وبالای
آن از ‎ath olay‏ و ‎WT‏ بترکی ‎Sole‏

‏- وبا ثانی مشدد 2,5 ‎UTS‏ شاعری بوده‌است

‏شهار ‎ae‏ اول ‎sory‏ معروقف
است که شماره وحساب باشد - و بمهء‌نی دوستی
و محبت - و شبه راظیر ‎ey‏ ومانند هم هنت
- وزخی را نیز گورند که کاری باشد و ازآن
امید زیستن نباشد - و پکسر ‎Id‏ تامدرختی‌است

‏۱ - گیلکی ‎ba-sham‏ (بروم) ‎mt_sham sige‏ ( می‌شوم؛میگردم) ره: شدن.
۴ - رك : شمیدن , شمند . فی : ساسکریت 8818 ( مشوش شدن . آشفتن )
* وبلیامز ۱۱۵۲ ©
۴ چون شاءبگیرد بکف الدر شمشیر از ‎get‏ بیفکند ز کفهاشم شبر .
‎Some‏ مروزی «جهانگیری» ۰
۴ سالبذریت ‎sham‏ آرام بودن . استراحت کردن . 5112102 آراش . فرافت
(وبلیامز ۱۰۵۳ :۳ . * = شم پای افزار بود بمنی چارق . منجيك( لزمذی) کوبد :
چندت مدح گفتم و چندی عذاب د.د گر زآنکه لت سیمت‌جفتی شمم‌فرست ©
‎cal?‏ فری ۳۸۰ ۰
‎od, — ۹‏ شاماخ * شاماخچه . ۲ ‎Nel.‏ «شمردن) ربثة‌اوستایی -122۲(مشاهده
کردن) . پهلوی ‎oshmar 5. shumar‏ ۰ 206511208۲ (با شمرده)؛ ‎ia,‏ هندی باستان
8 (ذ کر کردن, بادآوردن). افنالی ع ‎Shumar‏ (شمردن نمره) , کردی 007 (عدو)
‎tel?‏ - هوبشدان ‎VAY‏ ورك : شمردن .
* ما - نم اول. اوستا - 090790816 . در ‎xshmaka -- igi‏ (شما) » بازند
‎sae. ۵‏ باستان - 90050۳06168.امتی ‎smax‏ ۰ 500۳087 , بلوچی ‎Shava.‏ ء
‎shavaigh‏ «اسق ۰ > ورگ : هوبتمان ‎was‏ گیاکی ۳۵نا؟.پهلوی ‎Shm4h‏ : اورال
تورفان ‎ashmah‏ از ‎in,‏ اوستابی ‎xshma.‏ «بارتولمه ‎٩۱۳۰۳‏ < تیبر ‎OT‏ ۲۱5 ضمیر دوم

[pdf page 87]
کوته و بسیار سخت که پشه‌وران از ‎feo oT‏
افزار و دست افزار ‎Ie‏ - و بمعنی رازباله هم
‎aT ibe‏ است که ‎bal‏ باشد #۰ ۲
```


## [2026-09-14T01:59:10.771Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6700,6790p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-14T01:59:10.832Z] TOOL RESULT

```
‏شمشدر ۴ با دال و رای بی شطه
پروزن ستمگر » بلفت زد وپازند (۱)سیر ‎why‏
‏ییاز راگوبند .

‏شمشر | = با رای بی‌قطه بروزن غمزداء
رستتیی باشد دوابی ‎UT,‏ می‌زنگوش خوانند

‏(۱) چك: ژند ویاژند .

‎m—\tAt—

‏وبعربی آذان‌الفار گوبند .

‎vw ‏بکر اول و فتح‎ - * os
‏و سکون ثالت‌وکاف » بلغت زلد ویازند(۱) کاجد‎
‏دانه‌ای باشد ممروف که(؟)ازآن‎ oT ‏راکوبند و‎
Sey

‏شمدور = بنم اول بروزن پرزور,بلت
‎SAT‏ رستنیی باشد که ب رکه ‎OT‏ بب ‎eee‏
‎wile‏ و در آشهای نرش داخل کنند و روغن‌آن
دره کوش را دافع است.

‏شمئیر ‘ » بفتح اول ‎Olay‏ تخیر ؛
معروفت و وجه ‎OT Las‏ شم شیر است کهدم

‎۱

‏شمشیر
‏شیر ولاخن شیر باشد چه شم بمعنی دم و ناخن
هردوآمده است ۷ - وروشنابی ‎FAT are‏

‏(۷) چش: و .

‎٩‏ - پپلوی ‎shamshar‏ > بندهش ‎۱۱٩‏ ر ۱۰۳ طبری 5205118۲ ۰ مازندرانی
کتونی ‎shishar‏ و ‎Shahr, shar‏ «واژءامه ۸۷ = ‎Boxus sempervirens‏ . شمشاد
( درتهران) = ششماد رسمی  ‎tay ۱۹4 ale Evonymus japonica‏ کل کلاب۲۰۹.

‏۴ - فدای آن ‎ad‏ وزلفش که گویی

‏۴ رك: ح ۱ .
6 م ‎jly‏ «بونکر ۸6 ۰۰
پهلوی ‎kunjed‏ . کنجد ‎ab Nagy?‏

‏«رو ‎atte‏ است از شم‌شاد شمشار .
زینبی. «لفت فری ۰۱۲۵

‎«(oT lus, ( shom(a)sh(ajdar. » - ۴‏ پهلوی
‎٩‏ ممحف هز . ع90(۳۱)۵۱ و ‎Shimagh‏ ,

‎۲۱۳ oF. Shamsher ‏بهاوی‎ - ۲

‎: Shfshyr ‏و‎ shypshyr ‏در اوراق ماتوی (پپلوی)‎
Henning, A list of Middle Persian..., BSOS., IX,1.p.82.

‏۷ - وچه اشتفاق ءاميامه .

‏(برهان اطع ‎(vw‏
[pdf page 90]
{Aa

رآن‌گیاهی باندکه بدان رخت شویند ‎٩‏ -
‎Ky‏ اولدارویی است ‎YTS‏ پیونالی فراسیون
کریند وبدیرازی کندنای کوهی خوانند. وبعضی
کوبند ‎ink‏ ممتی عربی است .

شنا و۴ = باواو . بروزن و معنی ناب
اعت که شذاوری وآب ورژی بائد(۱) - و شنا
کننده را نیز گویند(۱) .

شناه ۴

بمعتی شناواست که ‎CT‏ ورزی- وشنا کننده(۳)

بکر اول بر وزن نگاه .

. atk
‏شنت - بغتح اول و سکون ثانی و بای‎
‏وازین است که کنبذیرا‎ ath ‏ابجد, معنی کنبذ‎
‏که سلطان غازان درآذربا‎
. ۴ ‏غازان‎ LT ee ‏غازان خوانند‎
‏یکربای ابجد بروزنمجد.‎ = © eee
. ٩ ‏شنبه راگویند که روز اول هفته باشد‎

شنپلیت ۷ - بقتح اول و کون ‎GS‏

ان ساخته ‎oy‏ شنب

(۱) چش : - باشد . (۷) چش :
```


## [2026-09-14T01:59:37.271Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== FSD vol4 leaf 9-14 heads'; for n in 9 10 11 12 13 14; do echo \"-- leaf $n\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' FSD_vol4.txt | head -c 200; echo; done"
}
```


## [2026-09-14T01:59:38.332Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== AFM zafaran'; grep -n 'زعفران\\|الزعفران' AFM_pages.txt | head -10"
}
```


### [2026-09-14T01:59:38.351Z] TOOL RESULT

```
=== FSD vol4 leaf 9-14 heads
-- leaf 9
  loss  b}  becoming  loose  or  b}  tbeft  —   s.-chaln*
SAFETY^DEVICES.— n,
1   Bclt'E'Jard  of  pUnmc»machme  2   Interior  of  Amencan  Museum  of  Safety.  New  York  3   Grating  for  preve
-- leaf 10
lomis  tuberosa)  of  the  mint  family,  of  the  Mediter- ranean region,  often  cultivated  In  gardens  for  Its  showy yellow  flowers  —   sage'(aj)"ple,  n   Bot  An  edible  gall caused  on 
-- leaf 11
 schooner,  and  normally  nearly  parallel  to the  J   eel)  Sec  Ulus  under  ship
2.  A   sailing  vessel  or  craft  in  tlus  sense  having  the  same form  ID  singular  and  plural,  as,  30  
-- leaf 12
nty,  O   — St.  Ber- nard dog,  one  of  a   breed  of  large,  strong,  sagacious  dogs, formerly  bred  chiefly  at  the  hospice  of  St  Bernard, Switzerland,  but  since  1860  common  In  fan
-- leaf 13
rb Saint  Pan 'eras,  1   sent  pan'kras,  2   sfint  pfin'eras  A   borough In  X   London,  England
Saint  Par'Is.  A   v   Illage  In  Champaign  countj ,   O Saint  Paul,  l   sfint  pel  2   sfin
-- leaf 14
mbling  or  having  the  form ~   ”   vl  Herp  A
saiamandroldean  amphibians,  especially  those having  opistboccelous  vertebra?,  vomeropalatine  bonM
PostfSsqLmos^ g)— sal"a-man'<irid,  « �
```


### [2026-09-14T01:59:38.411Z] TOOL RESULT

```
=== AFM zafaran
1056:جسم 3 ` ومنة ساد الزعفران ٠»‏ وفي البارع :”لا يقال
1057:لغير احليوان العاقل حسد ¥ الزعفران والدم اذا يس ¢ ܟܝܝ اذا ܨ ساف
1058:قد ܚܨ جسدًا ܐܚܐ الدم بالمساد وهو الزعفران
```


## [2026-09-14T01:59:44.687Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'saffron\\|safflower\\|za.faran\\|zaffer' FSD_vol4.txt | head -10"
}
```


### [2026-09-14T01:59:44.752Z] TOOL RESULT

```
481:Saf-fa'rld,  1   saf-ftVrid,  2   saf-fa'rld,  n   One  of  a   Persian fly  nasty  of  Mohammedans  founded  In  the  Dth  century saf'n-an,  1   saf'i-on.  2   silfM-an,  n   A   leather  of  Russian origin  prepared  from  goat-skins,  and  dy'cd  yellow  or  red saf'flor-ltc,  laaf'tor-alt,28\riar-It,  n   Mineral  A   metallic tin-whitc  cobalt  dtarscnld  (CoAsj),  crystallizing  in  the  or- thorhombic system  [<  G   SOlBor,  BVFl-LOWER  ] saf'flow-cr,  1   safMou-ar,  2   sM'Iow'-er,  n   1.  A   thtstlc- hke  annual  (Carthamus  tinclonus)  about  2   feet  high, with  spinv'  heads  of  orange-red  flowers  cultivated  from China  and  India  to  Egypt  and  southern  Europe  for  the d\  c   obtained  from  its  flowers,  and  used  in  dyeing  China fiilks,  etc ,   and  ns  an  ingredient  tn  rouge  The  seeds yield  an  oil  used  for  lamps  and  for  cooking  See  Car- THAXtus  bastard,  dyers’,  or  false  saffront;  saf'- fron(this"het  2.  The  dried  flowers  of  this  plant made  up  info  flat  cakes,  the  size  of  a   ha/f-dollar,  for export  saf'floTV-cr*calfc"t.  3.  The  dyestuff  obtained from  the  dried  fiowers  ( <   OF  saflor^  <   O   It  saDlore,  < Ar  7isfilr,<  safri,  icMow  )   saf'llowt- saf'frc,  n   Same  as  zvffpr
482:saf'front,  tt  To  give  color  or  flavor  to,  savor,  make  yellow as  with  saffron  saf'frant.  (saffron
487:saf'fron,  1   safVan.  2   saf'ron  (mix),  a   Of  the  color  of  sa-gad',  1   sa-gad',  2   sa-gad',  n   Same  ns  wolav’E saf'fron,  n   1   The  dried  orange-colored  stigmas  of  Sag"a-da-hocMsag  8-dB-h0V,2silg'a-da-h6c',  n   A   county the  saffron-plant  An  ounce  of  the  product  reqmres  In  S   Maine,  259  sq  m   ,   county -seat,  Bath more  than  4,000  flowers  It  was  formerly  In  high  medicinal  sa-ga"m!-t6',  1   sa-ga'mi-tg',  2   sa-ga'ml-t/,  n   {Louisiana, repute  as  a   stimulant,  emmenagog,  cordial,  and  antlsp  is-  U   S   I   An  Indian  dish  of  hominy,  much  used  by  Creoles modlc.  but  is  now  used  mainly  for  coloring  confectionery,  sag’a-moro,  1   sag'e-mBr,  2   sit'a-mOr,  n   [Am  Ind  1   An liqueurs,  varnishes,  etc  ,   and  In  parts  of  the  Old  World  as  a   American  Indian  tribal  chief,  probably  of  secondary  rank, flavoring  and  coloring  Ingredient  In  cookery  tho  considered  by  some  writers  as  cquiv  alent  to  sachem
488:2   The  plant  (Crocus  saltvus)  that  produces  saffron,  an  sa'gan,  1   sQ'gsn,  2   sa'gan,  n   [Heb  J   1.  Bih  a   prefect
494:3.  A   deep  orange  color,  such  as  that  of  tho  stigmas  of  RR  antis  •'osmodlc  See  gum‘  I<  L   sagapenon,  <   Gr the  saffron  4.  [Eng)  One  of  vanous  yellow-winged  _   5fl?apanen,_a  gi^  1   saga-pcn$
500:tinclonus,  u>ed  as  an  auiifcbrln  — s.(thlstlc,  n   Same  as SAFFLOWER —   sarfron»wood",  n   A   South-AIrlcan  tree {ClTodendron  croceum)  or  Its  wood  —   saf'fron-y,  a   Of  a saffron  tint  orange-colored
520:saf'ra-nol,  1   saf'ro-nol  or  -nol  2   sifTa-nQl  or  -nGI,  n   Chem  ern A   crystalline  compound  (CnHisNiOj)  obtained  by  treating  high phcnosafranln  hydrochlorJd  with  an  aJeoholic  solution  of  gray potash  with  heat  [<  F   so/ran  (sec  saffron)  4--0L]  flow'i
524:saf'rol,  1   saf'rol  or  -rol  2   sif'rOl  or  -r61  n   Chem  A   crys-  ” talllne  stearoptene  (CwHwOj)  forming  a   large  portion  of  y sassafras-oil  and  contained  also  In  other  oils,  as  oil  of  cam- phor  [<  r   safr~  (In  safran,  see  saffron)  +   -ol] saf'ro-sln,  l8afTo-sln,2  8af'ro-8ln  n   Chem  A   fluorescein derivative  (Ca)H8Brj(NO0-O6)  used  as  a   salfron-dye saft,  1   saft  2   sift,  a   &   adv  [Scot  ]   Soft
10468:1.  Of  or  pertaining  to  the  island  of  Sicily  2   Of  or  per- taining to  the  United  Kingdom  of  the  Tw’o  Sicilies, founded  by  the  Normans  in  the  I2th  century  in  southern Italy,  and  overthrown  by  Garibaldi  in  1860  II  n   1. A   native  or  inhabitant  of  Sicily  2   A   subject  of  the United  Kingdom  of  the  Two  Sicilies  [   <   L   Siciha,  < Slcult,  the  Sicilians  1   —   Sicilian  Bull,  the  brazen  bull  pos- sessed by  Phalaris  See  Phalvris  —   S.  earth,  a   fossil  be- zoar  — S   saffron  1   The  long-flowering  crocus  {Crocus tongi/iorus)  of  southern  Europe,  an  autumnal  flowering species  2   An  Inferior  kind  of  saffron  yielded  by  this  crocus —   S.  \   espers,  the  massacre  of  the  French  in  Sicily  at  a   sig- nal of  the  vesper-bell  on  Easter  Monday  In  1282,  owing  to their  atrocities  under  Charles  of  Anjou
41248:[L  )   Horn  AntiQ  A   body  of  cavalry,  the  tenth  part  of  an ala  or  wmg  of  a   legion  Including  from  30  to  32  members tur'ma-lln,  n   Same  as  tourslalin  tur'ma-llnet. turmentlsct,  n   Torment  Chaucer  C   T   1   14,435 tur'mcr-Ic,  1   tur'mar-ik,  2   tfir'mer-ic,  n   1.  The tuber  or  aromatic  root  of  the  turmenc-plnnt  (see  def 2),  especially  when  powdered  used  as  a   yellow  dye- stufT,  as  a   condiment,  especially  m   the  East  m   currj'* powder,  in  medicine  as  an  aromatic  stimulant,  and  in chemistry  to  make  turmeric-paper  2   An  East-Indian plant  (Curcumo  lonoa)  with  perennial  rootstock  and annual  stems  3.  The  tiumenc-trce  (Zicrio  smifAii)  of Australia,  the  Tasmanian  stmkwood  4,  An  Australian ev ergreen  shrub  (//oiearfocfyfoirfes)  (<F  tcrremenle, perhaps  cor  of  Ar  AurAum,  saffron  I   — tur'mcr-lc*on"» n   Chem  SameasTURMEROL  —   f   (paper,  n   A   bibulous paper  yellow  from  saturation  with  the  extract  of  turmeric, used  as  a   test  for  alkalis,  by  which  It  Is  turned  brown  or  red. fur-cu'ma(pa"pcrj  —   t   (p)ant,n  SamensTURMERic  2 — t.troot,  n   1.  The  root  of  the  turmeric-plant  2   Orange- root  See  GOLDENSEAL  3   Bloodroot  —   t.*tree,  n   An Australian  tree  of  the  genus  Zieria,  whose  Inner  bark  yields a   dye
```


## [2026-09-14T01:59:57.293Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSD_vol4.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(txt,1):\n    if i in (481,487,488,494,500,520): print(i,'leaf',leaf,'printed~',leaf+2144)\n    leaf+=l.count('\\f')\nEOF\necho '--- saffron etym'; sed -n '489,500p' FSD_vol4.txt | grep -o '\\[.\\{0,160\\}' | head"
}
```


### [2026-09-14T01:59:58.591Z] TOOL RESULT

```
481 leaf 9 printed~ 2153
487 leaf 9 printed~ 2153
488 leaf 9 printed~ 2153
494 leaf 9 printed~ 2153
500 leaf 9 printed~ 2153
520 leaf 9 printed~ 2153
--- saffron etym
[Eng)  One  of  vanous  yellow-winged  _   5fl?apanen,_a  gi^  1   saga-pcn$
```


## [2026-09-14T02:00:04.399Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'safranum\\|za.faran\\|zaVaran\\|zafaran' FSD_vol4.txt | head -5; echo '=== sed 495-520'; sed -n '501,520p' FSD_vol4.txt"
}
```


### [2026-09-14T02:00:04.493Z] TOOL RESULT

```
=== sed 495-520
Sar'fron«>\al'dcn,  1   safTon-weTden,  2   siirron-wardBn,  n A   town  In  Essex,  England
Sa'fo-nov,  1   so  fo-nof  2   sTfo-ndf,  Vassily  Illch  (VelVzs,  O
as,  a   sage  counselor  2.  Characterized  by  or  proceeding from  such  wisdom,  judicious,  as,  sage  advice Tho  sage  counsels  of  the  Dul  e   of  Wellineton
BnonaKAU  British  Constitution  p   2C9  [o  n   *   co  1861  ] 3   Befitting  a   sage,  profound,  learned,  also,  grave, serious  (F ,   <   L   sapio,  be  wise  ]   sagedt  Syn  see BVGACious,  wisr  — sage'Iy,  adp  —   sagc'ncss,  n
S   ]   l852-yjjl9lt))  A   Russian  concert  conductor  and  planet.  Basest  «   A   person  of  calm,  far-seeing  wisdom,  especially,
Phllhnrmonlc  orrliLSlrA  Mnu  Vork  lOOfi-innO  ^   p       __  .   i   .   i
tion  of  dan-  O’TMJJT  o
gerous  pres-  ^       **
sures  2.  A   Safety-valves
similarly  1   Lever  safety-^aUe  a,  ^a^c.  6   lever,  c, acting xalv'e,  weight  2   Spring  safetj-\aUe  3   Lever
edmittinc  safety-valve  with  low-ivater  alarm  '
air  f   rnm  dome  e   jlcara-outlct.  d.  ^alvD,  «,  wh.stle  /, without  ,I,de..a.ve,„,flo.t
as  to  equalize  internal  and  external  pressures  in  atessei in  wluch  there  is  a   partial  vacuum  due  to  conden- sation
Of  the  three  general  types  of  safcty-valv'es,  tJie  first.  In which  the  valve  Is  held  against  the  pressure  of  the  steam,
simply  by  a   weight,  and  known  as  the  dead  *wmght  safMj*
valve,  Is  Seldom  used,  except  on  low -pressure  boilers  The second  type  or  lever  safety-valve  Is  extensively  used  on stationary  boilers  The  stem  of  the  valve  engages  with  a lever  of  the  third  order  a   short  distance  from  Its  plvotea extremity  To  the  other  end  of  the  lever  a   weight  is attached  which  may  bo  sot  so  as  to  cause  the  boiler  to  blow off  at  any  desired  pressure  In  the  third  or  spring  type,  m which  there  are  several  varieties,  a   spring  Is  sometimes  used
conducted  Philharmonic  orchestra  New  York  1906-1909  ^   '
saf'ra-nln,  \l  safTo-nln.  -nln  or  -nin,  2   sif'ra-nln,  -nin  or  ”   _ saf 'ra-nlnc,  J -nln  «   1   Chem  Any  of  a   class  of  basic
compounds  considered  as  symmetilcal  dlamlno  derivatives  _   c of  the  azonlum  bases  Their  salts  form  Important  dyes  ,   p The  simplest  safranln  is phcnosafranln  (CisHisN-Cl),  and the  most  important  Is  tolusafranin  (CisHufCHsizN^Cl), whose  ehlorid  is  used  in  cotton*  and  sllk-dyemg  2   Anyone of  various  mixtures  of  safranln-salts  (see  def  1)  used  In  dye-  cap-i-  ' Inc  The  most  common  is  a   brown  paste  composed  mostly  > of  tolusafranin  eWorld  3   Same  as  crocin  4   Same  as PHEXOSAFRANIN  [<  F   sQfran,  sec  SAFFRON]  saFfro- ninef,  saf'fron  jcFlowt.  sbru
saf'ra-nol,  1   saf'ro-nol  or  -nol  2   sifTa-nQl  or  -nGI,  n   Chem  ern A   crystalline  compound  (CnHisNiOj)  obtained  by  treating  high phcnosafranln  hydrochlorJd  with  an  aJeoholic  solution  of  gray potash  with  heat  [<  F   so/ran  (sec  saffron)  4--0L]  flow'i
```


## [2026-09-14T02:00:17.489Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:00:17.495Z] TOOL RESULT

```


```


## [2026-09-14T02:00:19.970Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/saffron",
 "prompt": "Full etymology of saffron, including Medieval Latin safranum, Old French safran, Arabic za'faran, and any note on further origin (Persian?)."
}
```


## [2026-09-14T02:00:21.102Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/safflower",
 "prompt": "Full etymology of safflower: French, Italian, Arabic usfur/safra forms, and any mention of 'yellow flower'."
}
```


### [2026-09-14T02:00:24.735Z] TOOL RESULT

```
# Etymology of Saffron

According to the Online Etymology Dictionary, saffron entered English around 1200 from Old French *safran*, which derived from Medieval Latin *safranum*. This Latin term connects to Italian *zafferano* and Spanish *azafran*.

The ultimate origin traces to Arabic *az-za'faran*, though the source notes that this Arabic root is "of unknown origin." The word traveled into other European languages through similar paths—German *Safran* came via French, while Russian *shafran'* came directly from Arabic.

The substance itself refers to "the dried stigmas of flowers of the autumn crocus," prized for its "sweet aroma and deep orange color." By the late 14th century, the term had expanded to describe the color itself, and by the early 15th century, it referenced the crocus plant.

The etymology doesn't indicate a Persian origin, though the spice itself has historical significance in Persian cuisine and trade networks—a connection not explicitly detailed in this source.
```


### [2026-09-14T02:00:25.053Z] TOOL RESULT

```
I appreciate your request, but I need to let you know that the webpage content provided doesn't actually contain etymological information about "safflower." 

The page you've shared is the **homepage** of Etymonline.com, which displays the site's navigation, branding, and footer information—but no dictionary entries or word definitions.

To find the etymology of "safflower" including details about French, Italian, and Arabic origins (usfur/safra), you would need to search the Etymonline database directly by visiting the site and looking up the word. The content you've provided doesn't include that specific entry.

If you can provide the actual dictionary entry content for "safflower" from Etymonline, I'd be happy to help summarize it within the constraints you've outlined.
```


## [2026-09-14T02:00:28.519Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/safflower",
 "prompt": "Etymology section of safflower: Dutch saffloer, Old French saflor, Italian saffiore, Arabic usfur, influence of flower."
}
```


## [2026-09-14T02:00:30.931Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86",
 "prompt": "Give the Arabic and Persian entries for زعفران: etymology (is it from Persian zar-parān? from Arabic ṣ-f-r 'yellow'? Aramaic?), meanings, and any cited scholars."
}
```


### [2026-09-14T02:00:33.748Z] TOOL RESULT

```
# Safflower: Etymology and Definition

**Definition:**
Safflower is a cultivated thistle-like plant (*Carthamus tinctorius*) from the Asteraceae family, "now grown mainly for its oil."

**Etymology:**
The word has a fascinating linguistic journey. It comes "from Middle French *safleur*; originally from Arabic *أَصْفَر* (ʔaṣfar, 'yellow')" but was influenced by the Middle French words *safran* (saffron) and *fleur* (flower).

**Historical Use:**
The plant's dye properties were historically significant. According to a 2002 source, safflower dye behaves uniquely: "with acids it goes a beautiful crimson pink which is the colour of the original 'red' tape once tied around legal documents in England."

The word appears across 21 languages, reflecting the plant's widespread cultivation and cultural importance across diverse regions worldwide.
```


### [2026-09-14T02:00:37.817Z] TOOL RESULT

```
# زعفران (Saffron) - Arabic and Persian Entries

## Arabic Entry

**Meaning:** Saffron

**Etymology:** The entry presents multiple theories:

1. **Aramaic origin:** Borrowed from Aramaic צפר with an unattested -ān ending
2. **Native Arabic formation:** Comparison with زعتر (zaʕtar, "wild thyme") and عصفر (ʕuṣfur) from the root ص ف ر (ṣ f r) meaning "yellow"
3. **Middle Iranian borrowing:** Maintained alongside Aramaic origin, inviting comparison with Persian جعفری (ja'fari, "parsley")

The entry notes that "A Middle Iranian borrowing is also maintained" alongside the Aramaic theory, referencing Asbaghi's work on Persian loanwords in Arabic.

## Persian Entry

**Meaning:** Saffron (with synonym کرکم - korkom)

**Etymology:** "Borrowed from Arabic زَعْفَرَان (zaʕfarān)"

The etymology tree shows the lineage: Aramaic צפר → Arabic زَعْفَرَان → Persian زعفران

**Notable:** The Persian entry does not independently discuss the *zar-parān* ("gold-wings") theory, though this Middle Iranian etymology appears in the Arabic section's references.
```


## [2026-09-14T02:00:45.345Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfn='incoming/PLA/PLA_pages.txt'\nlines=open(fn,encoding='utf-8',errors='replace').read().split('\\n')\n# find leaf index by form feeds\nleaf=1\nfor i,l in enumerate(lines,1):\n    if 8270<=i<=8300:\n        print(i,'|',l)\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-14T02:00:46.523Z] TOOL RESULT

```
8270 | 
8271 |  sl.
8272 | „’b,-                za czäfir:              Pl.              u
8273 |                                                         v.oyLs),       za Car
8274 |                                                                            faran                     q.    v.
8275 | 
8276 | 
8277 | Als, - zaCäfir:                                  Pl. v.ol=;            za°farän ag. v.
8278 | 
8279 | Ol;              -       za°farän:                 "Safran!        pers.              8, wahrscheinlich                       aus    dem     pers.    a
8280 |           zarparan                  "mit          goldenen         Blättern",                        mand.       zaparania          9 ,‚ syr.        us        10 .
8281 | 
8282 |           afrz.               safran,             mhd.,    Safran,              dtsch. Safran                    11,
8283 | 
8284 | 
8285 | his;                 -    zaCfärani:                    "goldgelb;              Safranfarbe                     Nisba    v.    Safran.
8286 | 
8287 | 
8288 | 
8289 | 1.       Wahrig               s.    v.
8290 | 2.       ebda.
8291 | 3.       Brockelmann                        s.     v.
8292 | 4.       ebda.
8293 | 5.       Kamäl            s.       v.
8294 | 6.       Löw         s.       v.
8295 | 7. Muhit s. v.
8296 | 8. Wahrmund                        s.       v.,        Golegoläb         n.          BQ.        s.    v.
8297 | 9.       Macuch               s.    v.
8298 | 10.          Löw         s.    v.
8299 | 11.          Wahrig            s.       v.
8300 | zufäna                                                                                  146                                                    zanburak
```


## [2026-09-14T02:01:00.782Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/scimitar",
 "prompt": "Full etymology of scimitar/cimeter: Italian scimitarra, French cimeterre, Persian shimshir/shamshir, and any statement of doubt about the Persian origin."
}
```


## [2026-09-14T02:01:03.374Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B4%DB%8C%D8%B1",
 "prompt": "Persian شمشیر entry: etymology (Middle Persian forms, Manichaean spellings, any Old Iranian reconstruction), descendants (Arabic, Turkish, European), and cited sources."
}
```


### [2026-09-14T02:01:05.322Z] TOOL RESULT

```
# Scimitar Etymology

The word "scimitar" traces back to the 1540s, entering English through French and Italian sources. According to etymonline, the term comes from "French _cimeterre_ (15c.) or Italian _scimitarra_."

The ultimate origin remains uncertain. While Turkish would be the expected source given the weapon's association with Turkish and Persian warriors, no corresponding Turkish word has been documented. The etymology suggests a possible Persian connection through _shimshir_ (pronounced "shamsher"), though experts consider this "unsatisfactory as to form."

The modern spelling reflects Italian influence. Historically, the word appeared in various forms due to "ignorance of its original form, and to the imitation now of the F. now of the It. spelling."
```


### [2026-09-14T02:01:12.000Z] TOOL RESULT

```
# شمشیر (Shamshir) - Etymology and Linguistic Overview

## Etymology

The Persian term شمشیر traces back to **Middle Persian** roots. According to the Wiktionary entry, it derives from Middle Persian forms including šmšyl (/šamšēr/) and špšyl, with a Manichaean spelling of 𐫢𐫜𐫢𐫏𐫡 (/šafšēr/, "sword").

The word is cognate with **Parthian** safsyr (/safsēr/, "sword"), indicating shared Iranian linguistic ancestry.

## Comparative Borrowings

The term appears across multiple ancient languages through Iranian borrowing:

- **Old Armenian**: սուսեր (suser, "sword")
- **Classical Syriac**: ܣܦܣܝܪܐ (sap̄sērāʾ, "sword")
- **Jewish Babylonian Aramaic**: ספסרא / ספסירא (sap̄sērāʾ)
- **Ancient Greek**: σαμψήρα (sampsḗra, "foreign sword")
- **Italian**: scimitarra ("scimitar")

## Modern Descendants

The word dispersed widely through Ottoman Turkish and into South Asian languages:

- **Ottoman Turkish**: şemşir, şimşir
- **Urdu/Hindi**: शमशेर / شَمْشیر (śamśer)
- **Uzbek/Uyghur**: shamshir / شەمشەر
- **Bengali**: শমশের (śomośer)
- **Kyrgyz/Kazakh**: шамшар / семсер

This linguistic journey reflects historical trade and cultural contact across Eurasia.
```


## [2026-09-14T02:01:16.217Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chiffon",
 "prompt": "Full etymology of chiffon: French chiffon, chiffe, and the ultimate origin of chiffe (Arabic? Germanic? English chip?)."
}
```


## [2026-09-14T02:01:17.940Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/chiffe",
 "prompt": "Give the TLFi/CNRTL etymology of French 'chiffe': proposed origins (English chip, Arabic šiff, etc.) and which the dictionary prefers."
}
```


### [2026-09-14T02:01:20.453Z] TOOL RESULT

```
# Etymology of Chiffon

The word "chiffon" entered English in 1765, originally meaning "feminine finery, something used by women purely for adornment." It derives from French *chiffon*, which is a diminutive form of *chiffe*, meaning "a rag, piece of cloth."

The ultimate origin of *chiffe* remains uncertain. Etymologists have proposed several possibilities:

- A variant of English "chip" or related Germanic words
- An Arabic source, as suggested by Klein
- Unknown origin

The fabric meaning—"sheer silk fabric, thin gauze"—is attested later, from 1890. By 1929, the term extended to pastry, likely referencing the characteristic lightness of chiffon cake.
```


### [2026-09-14T02:01:22.370Z] TOOL RESULT

```
I appreciate your question, but the web page content provided only shows "Portail lexical" (Lexical Portal), which doesn't contain the etymology information you're asking about for the French word 'chiffe'.

To answer your question about the TLFi/CNRTL etymology of 'chiffe'—including proposed origins from English "chip," Arabic "šiff," or other sources, and which origin the dictionary favors—I would need access to the actual dictionary entries from those resources, which aren't included in the content you've shared.

If you can provide the relevant dictionary pages or passages, I'd be happy to analyze the etymology information while following your guidelines.
```


## [2026-09-14T02:01:29.635Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%81%D8%A7%D9%81",
 "prompt": "Arabic شفاف (šaffāf) and Persian شفاف: etymology, root ش ف ف, meaning; also any info on the verb شَفَّ (šaffa) 'to be transparent' and the noun شِفّ (šiff)."
}
```


## [2026-09-14T02:01:31.799Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%B1%D8%A7%D8%A1",
 "prompt": "Arabic صفراء (ṣafrāʔ): etymology (feminine of أصفر aṣfar 'yellow', root ص ف ر), meanings including 'bile'; and note the Persian borrowing صفرا."
}
```


### [2026-09-14T02:01:36.181Z] TOOL RESULT

```
# Analysis of شفاف (šaffāf)

## Etymology & Root
The word شفاف originates from Arabic with root **ش ف ف** (š f f). Both Ottoman Turkish and Persian borrowed this term directly from Arabic.

## Meanings

**Arabic:** The adjective describes something that is "see-through, transparent" or, in textile contexts, "sheer, thin, fine, delicate."

**Persian:** The word carries similar meanings—"transparent, see-through"—but extends to figurative uses meaning "open, public" and describes lucid dreams (خواب شفاف).

**Ottoman Turkish:** Here it means "transparent, see-through, diaphanous, clear, translucent," referring to materials allowing light to pass through with minimal disturbance.

## Related Terms
The Wiktionary entry documents derived forms like شفافية (šaffāfiyya) in Arabic, along with compounds in Ottoman Turkish such as شفافلق (şeffaflık, "transparency").

## Note on Verb & Noun
The source provided does not include information about the verb شَفَّ (šaffa) or noun شِفّ (šiff), so I cannot address those aspects based on this content.
```


### [2026-09-14T02:01:36.647Z] TOOL RESULT

```
# صفراء (Ṣafrāʔ)

Based on the Wiktionary entry, this Arabic word has two primary functions:

**As an Adjective:**
The term represents the "feminine singular of أَصْفَر (ʔaṣfar)," meaning yellow.

**As a Noun:**
It denotes "bile," with a synonym provided as مِرَّة (mirra). The word is classified as a feminine noun with complex declension patterns across singular, dual, and plural forms.

**Linguistic Heritage:**
The word belongs to the Semitic root ص ف ر (ṣ f r) and has influenced several languages through borrowing, including Persian (صفرا), Turkish (safra), Spanish (zafra), and Swahili (safura).
```


## [2026-09-14T02:01:51.146Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== HRN shamshir'; grep -n -i 'šamšēr\\|šamšīr\\|schamschir\\|samsir\\|Schwert' HRN.txt | head -8; echo '=== HUB'; grep -n -i 'šamšēr\\|šamšīr\\|schamschir\\|samser' HUB.txt | head -8; echo '=== LKT safran'; grep -n -i 'safran\\|zafferano\\|za.faran' LKT.txt | head -8; echo '=== LKT shamshir'; grep -n -i 'scimitarra\\|schamschir\\|shamshir\\|semschir' LKT.txt | head -8"
}
```


### [2026-09-14T02:01:51.252Z] TOOL RESULT

```
=== HRN shamshir
3846:409. tey *spitz, Schwert', % (nicht belegt).
3849:Schwert' (889).
=== HUB
=== LKT safran
1946:Adj.  zu  ]ialük  'eine  Art  Wohlgeruch', Galia  muscata,  aus  Safran  und  anderen Zutaten  bestehend,  von  vorwiegend  roter Farbe,  daher  'hellrot'  [z.  B.  vom  Weine gesagt:  nah'td  Jialükl];  hieraus  sp.  aloyue als  Adj.  und  Subsl.  'hellrot,  hellroter Wein',  aZo^Mero 'Weinhändler',  aloqueria 'Weinlager  oder  -fabrik'.  [DE  184. Dicc  Gast  135  c.
2927:Hieraus  zunächst  ar.  kiirlmm  [das  viel- leicht erst  über  gr.  lat.  crocum  entstanden ist]  und  dann  it.  siz.  sp.  curcuma  'in- discher Safran',  ndl.  curcuma  'dass.'. [DE  257.  Dozy  Oost  32.  GrSVociSic  233.
4870:'Safran  Memocylon  tinctorium';  hieraus it.  zafferano,  frz.  Safran,  sp.  azafrän, pg.  agafräo,  rum.  safran,  sofran,  §ofran 'dass.',  afrz.  saffre  'mit  goldenem  Be- sätze versehen',  sard.  tofferanu  'Safran'; dtscli.  Safran,  engl  saffron,  ndl.  saff- raan-  russ.  safran,  poln.  szafran,  Cech. serb.  safran,  bulg.  serb.  öafran.  [DE  223. Eguilaz  317.  ML  9588.  Mikl  SlEtWb 336  a.
4872:'Hacke  des  Steuerruders';  hieraus  teils mit,  teils  ohne  ar.  Art.  pg.  agafräo,  sp. azafrän,  prov.  frz.  safran  'Schege, Steuerhacke'.    [ML  1479.
5489:sänija  1829 sannäg  1S33 sa'rä  1837 sarä&  1838 sarahha  1839 5«»-«/^«  1840 saraka  1951 saratän  1848 sarba  1838 sart^a  1439.  1838 san/-  121.  1852 S'irtft  1853 sar«  1886 sarifa  1854 sark(i)  1856 Sai-kije  1856  b sarmüta  1 602 sarr(a)  1859 sarräf  1860 iari  1861 sarwäl  1849 sös 5 1484.  1865 säsd  1776 säsija  1865 satara  1919 sa^;»  1868 «aii  1870 safrang  1 87 1 sa!;ri;a  1872 sätür  1873 sattvän  2141 sawA;  1783 sauka  1939 sa««Z  1874 saj<<  1875 stört?-  1890 si'dän  1365 sjrfr  1529 sifn��;  1895 ifi/^'  1893 si/r  1894 si^n  1896 S'/täö  1897 sijäsa  1776 sjfcS'  1899 s/fcöja  1900 s4-ä/  1901 sikö<ji  1902 s*fcfca  1903 sikkin  1904 s«Ä;te<  1794.  1905 s«7äÄ  1906 se7A;a  1907 stwSZ  902 simäsa  1816 s/ww  1819 simsär  1836 sin  807 sinä'a  495 sindlja  1911 stM»  1913 siV  1428
6677:i  sacre  1799 sa/T";-^  afz.  2178 Safran  2178.  2179
8616:Safran  2179
8742:safran  2178 I  sa/^ea  916 I  safterea  1768
=== LKT shamshir
4320:1910  Pers.  siiiisTr: 'Schwert' ;  hieraus  it.  scimitarra,  frz. cimeterre,  ciniiterre,  sp.  pg.  cimitarra 'tk.   Säbel' ;    engl,    scymitar,  cimetar 'Säbel,  Schwert'.  [Oriente  1, 195,  Anm,2.
```


## [2026-09-14T02:01:52.916Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== ARY shamshir'; grep -n 'شمشیر' incoming/ARY/ARY_pages.txt | head -5; echo '=== ARY zafaran'; grep -n 'زعفران' incoming/ARY/ARY_pages.txt | head -5; echo '=== AFM zafaran headword'; grep -n '( الزعفران\\|(الزعفران\\|زعفران )' AFM_pages.txt AFM.txt | head -5"
}
```


### [2026-09-14T02:01:53.007Z] TOOL RESULT

```
=== ARY shamshir
7083:۱ یکی از چم‌های این واژه در زبان‌های ژرمنی: شمشیر؛ درد.
10245:چم این واژه در زبان ایتالیایی؛ شمشیر,
12368:چم این واژه در زبان‌های ژرمنی: (با ضربه‌ی شمشیر و غیره) بریدن» ضربت زدن,
=== ARY zafaran
=== AFM zafaran headword
```


## [2026-09-14T02:01:59.673Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4866,4875p' LKT.txt; echo '=== 1910 ctx'; sed -n '4316,4324p' LKT.txt; echo '=== usfur'; grep -n \"usfur\\|'usfür\\|usfür\" LKT.txt | head -5"
}
```


### [2026-09-14T02:01:59.764Z] TOOL RESULT

```
Vulg.  'Unterjacke.  Korsett',  ebenso  tk. zebun  'Jäckchen,  Mieder' ;  hieraus  rum. zäbun  'wattierter  Bauernkittel';  bulg.  za- bunce,  serb.  zubuii,  klruss.  zobuncac, russ.  zipun  'Jacke'  [vielleicht  geht  das ar.  Grundwort  selbst  zuletzt  auf  ^r.gubba, s.  hier  Nr.  737,  zurück].  [Löbel  EITAP 99.    Mikl  SlEtWb  404a.
2177.  Pers.  zäbün:
'Schwach',  ebenso  tk.  zebun  'dass., energielos';  hieraus  serb.  zabun  'ver- blüfft', Vb.  zabuniti.  [Mikl  SlEtWb  399a.
2178.  Ar.  za'farän:
'Safran  Memocylon  tinctorium';  hieraus it.  zafferano,  frz.  Safran,  sp.  azafrän, pg.  agafräo,  rum.  safran,  sofran,  §ofran 'dass.',  afrz.  saffre  'mit  goldenem  Be- sätze versehen',  sard.  tofferanu  'Safran'; dtscli.  Safran,  engl  saffron,  ndl.  saff- raan-  russ.  safran,  poln.  szafran,  Cech. serb.  safran,  bulg.  serb.  öafran.  [DE  223. Eguilaz  317.  ML  9588.  Mikl  SlEtWb 336  a.
2179.  Ar.  za'frän:
'Hacke  des  Steuerruders';  hieraus  teils mit,  teils  ohne  ar.  Art.  pg.  agafräo,  sp. azafrän,  prov.  frz.  safran  'Schege, Steuerhacke'.    [ML  1479.
2180.  Ar.  zäg:
'Vitriol';  hieraus  mit  ar.  Art.  u.  Imäla [ä  y>  e]  sp.  aceche,  aciche,  acige,  pg. azeche,  frz.  azeg  [alchemistischer  Aus- druck] 'dass.'.  [DE  32.  Eguilaz  17. Devic  DEt  10.
2181.  Berb,  zagäja: 'Wurfspiefs,  Bajonett' ;  in  gleicher  Form
=== 1910 ctx
Eine  Pflanze  Beta  sicula  [aus  gr.  aiKeXöq, nach  Theophrast  so  benannt,  weil  sie aus  Sizilien  stamme];  hieraus  sp.  acelga 'Lauch',  pg.  acelga,  celga  'wei��e  Bete', siz.  (alt)  secla,  (Messina)  sicali,  s^gali. [DE  33.  Mahn  EtUnt  9.5/96.  Eguilaz  21/22. GrSVociSic  545/246.    ML  7797.
1908.  Tk.  silte:
'Matratze ;  langes,  breites,  mit  Baumwolle gefüttertes  Polster,  auf  dem  man  bequem sitzen  kann'  [Kelekian  Kämüs  732b]; hieraus  rum.  saltea  'dass.'.
1909.  Pers.  sim§äd: 'Buchsbaum,  Buxus  sempervirens',  tk. cimsir    'dass.';    hieraus    rum.  citnpr 'Buchsbaum':  serb.  simsir,  russ.  samSit, samsit  'dass.'.
1910  Pers.  siiiisTr: 'Schwert' ;  hieraus  it.  scimitarra,  frz. cimeterre,  ciniiterre,  sp.  pg.  cimitarra 'tk.   Säbel' ;    engl,    scymitar,  cimetar 'Säbel,  Schwert'.  [Oriente  1, 195,  Anm,2.
1911.  Ar.  siadTj.i: 'Wassermelone'  [ursprünglich  al-batfiha as-sindija  'die  Melone  aus  Sind  in Indien'];  hieraus  kat.  sindria,  acendria, sp.  sandia  'dass.';  sp.  sandio,  pg.  satv- deu  'töricht'.  [DE  339.  Eguilaz  490. ML  7934  a.
1912.  Pers.  singräb: 'Eichhörnchen,  Sciurus  cinereus',  ebenso tk. ;  hieraus  rum.  singeap  'Feh,  Marder- pelz', singepiii  'aschgrau'.
1913.  Tk.  sini:
'Große  Platte  an  Stelle  eines  Speisetisches' [aus  ar.  Adj.  sinl  'chinesisch,  Porzellan', zu  t^in  'Sina,  China'];  hieraus  rum. »inte  'Kuchenpfanne,  -form'.
=== usfur
```


## [2026-09-14T02:02:16.368Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=safflower",
 "prompt": "Give the American Heritage Dictionary etymology bracket for safflower verbatim."
}
```


## [2026-09-14T02:02:17.395Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=chiffon",
 "prompt": "Give the American Heritage Dictionary etymology bracket for chiffon verbatim (French chiffon, chiffe, and its origin)."
}
```


### [2026-09-14T02:02:19.382Z] TOOL RESULT

```
Based on the webpage content, here is the etymology bracket for safflower verbatim:

"[Middle English _saflour_, from Old French _safleur_, from Old Italian _saffiore_ (influenced by Old Italian _fiore_, flower), from Arabic _'uṣfur_.]"
```


### [2026-09-14T02:02:20.934Z] TOOL RESULT

```
# Chiffon Etymology

According to the American Heritage Dictionary, the etymology bracket states:

"[French, rag, scrap, ornamental piece of ribbon or lace, from _chiffe_, rag, alteration (influenced by Old French _chifre_, zero, thing of little value) of Old French _chipe_...]"

The entry traces the word's origin through French _chiffe_ (meaning "rag") back to Old French _chipe_, which derives from Middle English _chip_ (a wood shaving or splinter).
```


## [2026-09-14T02:02:32.006Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== MON shaffaf'; grep -n 'شفاف' MON_part1.txt MON_part2.txt | head -5; echo '=== MON zafaran'; grep -n 'زعفران' MON_part1.txt MON_part2.txt | head -5; echo '=== MON safra'; grep -n 'صفرا' MON_part1.txt MON_part2.txt | head -3; echo '=== MON shamshir'; grep -n 'شمشیر' MON_part1.txt MON_part2.txt | head -3; ls -la MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T02:02:32.172Z] TOOL RESULT

```
=== MON shaffaf
MON_part2.txt:118:شفافی و دندانه‌دار با فاصله زیاد و دارای 
MON_part2.txt:122:شفاف و سبز تیره است ولی سطح تحتانیش 
MON_part2.txt:3694:شتا ای کو هه غیر شفاف: کدر؛ مق. 
MON_part2.txt:3695:شفاف. غیرضرور(ی): آنچه که ضرور و 
MON_part2.txt:8340:که به حالت ورقه‌ای سیار نازک شفاف 
=== MON zafaran
MON_part1.txt:1467:تویسند و تذهیب کنند. شراب زعفرانی 
MON_part1.txt:2187:کر ده. آجیل آچار: اجیلی که ندان زعفران 
MON_part1.txt:11063:زعفران بمنی» بلیهه» ویسه» ویهه بکم» 
MON_part1.txt:15004:که در غذا ریزند» مانند: زعفران» زردچوبه 
MON_part1.txt:19945:به رنگک‌های خا کستری و زعفرانی و حنابی 
=== MON safra
MON_part2.txt:6680:معرق و زیاد کنندةٌ ترشحات صفرا تجویز 
MON_part2.txt:15813:ممکن است مربوط به انسداد کيسةٌ صفراوی 
MON_part2.txt:22339:در مسجاوری صفراوی و کبد گوسفند 
=== MON shamshir
MON_part2.txt:706:سازند. حربه‌ای شبیه شمشیر که پهن و 
MON_part2.txt:2060:مفاک» گودال, حفر ۵. شمشیر آندار. 7 
MON_part2.txt:2175:مثل جلد کتاب» شمشیر و جز آنها؛ نیام. 
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-14T02:02:38.233Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for زعفران, including any origin tag in brackets like [ع.] or [معرب]. Also quote Dehkhoda's etymological remark if present."
}
```


## [2026-09-14T02:02:39.587Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D9%81%D8%A7%D9%81/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for شفاف, including the origin tag in brackets (e.g. [ع.]) and the definition. Also any entry for شفافیت."
}
```


### [2026-09-14T02:02:43.711Z] TOOL RESULT

```
# شفاف (Transparent) - Mo'in Dictionary Entry

**From فرهنگ معین:**

**شفاف** [ع.] (ص.) "هرچیز لطیف و نازک که از پشت آن چیزهای دیگر دیده شود"

This entry defines the term as any delicate or thin substance through which other objects behind it become visible.

---

**Note on شفافیت (transparency):**

The dictionary does not provide a separate entry specifically for شفافیت. However, throughout the page, شفافیت appears as the noun form derived from the adjective شفاف, referring to the quality or state of being transparent or clear.
```


### [2026-09-14T02:02:45.151Z] TOOL RESULT

```
# زعفران - Dictionary Entry Summary

## Mo'in's Dictionary (فرهنگ معین)

According to Mo'in's definition:

> "(زَ فَ ) [ ع . ] (اِ. ) گیاهی است پایا از تیرة زنبقی ها با برگ های دراز و سبز"

This describes saffron as a perennial plant from the iris family with long, green leaves and fragrant yellow or reddish flowers.

## Dehkhoda's Etymological Note

Dehkhoda provides important etymological context:

> "عربی صحیح است. ( از المعرب جوالیقی ص 173 )"

He indicates the word has Arabic origins according to al-Jawaliqi's lexicographical work on Arabicized words. However, Dehkhoda also notes the plant name relates to its characteristics—the orange-red stigmas and styles used as the spice portion of the flower.

The entry documents that while the term entered Persian through Arabic, it references the plant's distinctive features: the delicate, aromatic orange-colored threads harvested from the *Crocus sativus* flower.
```


## [2026-09-14T02:03:04.384Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== DEV chiffe'; grep -n -i 'chiffe\\|chiffon' DEV.txt PHN.txt LAM.txt DOZ.txt | head -10; echo '=== SKT chiffon/saffron'; grep -n -i '^CHIFFON\\|^SAFFRON\\|^SAFFLOWER\\|Saffron,\\|Safflower' SKT.txt | head -10; echo '=== FSD chiffon'; grep -n \"chif'fon\\|chiffon,\" FSD_vol1.txt | head -5"
}
```


### [2026-09-14T02:03:04.500Z] TOOL RESULT

```
=== DEV chiffe
LAM.txt:7630:Chiffe et son dérivé Chiffon ; de Lii, chiffe étoffe légère
LAM.txt:7631:et transparente. Le mot français chiffe a encore mainte-
LAM.txt:7633:lité ». (Litt.) La terminaison on dans chiffon est pour le
LAM.txt:8903:Chiffe
LAM.txt:8907:Chiffon
DEV.txt:1131:Chiffon.  Ital.  chiffone,  arabe  chijfoun,  étoffe  mince  et transparente.  (Defrémery^.)  L'étymologie  est  bonne,  mais il  faut  dire  que  clàj^on  vient  de  chiffe,  vieux  mot  français qui  désigne  une  étoffe  légère  et  de  mauvaise  qualité^,  et
DEV.txt:3264:Chiffe,  voy.  Cliiffon,
DEV.txt:3265:Chiffon,
DEV.txt:3266:Chiffoiie,  ital.  \o\.  Chiffon.
DEV.txt:4896:\Ju:^  voy.  Chiffon.
=== SKT chiffon/saffron
3378:Chiffonier,   a  cupboard.    (F. place  to  put  rags  in.  —  t.  chii picker,  aUo  a  cupboard.  —  F. Urig.  unknown.
=== FSD chiffon
```


## [2026-09-14T02:03:05.659Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== AFA Safran'; grep -n -i 'Safran' AFA.txt | head -8; echo '=== FVQ zafaran'; grep -n -i 'zafaran\\|za.faran' FVQ.txt | head -5"
}
```


### [2026-09-14T02:03:05.740Z] TOOL RESULT

```
=== AFA Safran
=== FVQ zafaran
```


## [2026-09-14T02:03:11.122Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1128,1140p' DEV.txt; echo '--- page'; python3 - <<'EOF'\ntxt=open('DEV.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(txt,1):\n    if i in (1131,2045): print(i,'leaf',leaf)\n    leaf+=l.count('\\f')\nEOF\necho '=== LAM 7620-7640'; sed -n '7624,7640p' LAM.txt"
}
```


### [2026-09-14T02:03:12.236Z] TOOL RESULT

```
'   Dioscoridœ pharmacorum  liber  VIII.  Strasb.  iSaQ,  fol.  266  recto.
94  DICTIONNAIRE  ÉTYMOLOGIQUE
D'après  Beschereile,  il  se  dit  encore  d'une  certaine  ma- nière de  jouer  au  billard,  au  maiil,  a  la  paumée  Dans certains  appareils  de  chauffage  et  de  ventilation,  on  ap- pelle chicanes  des  pièces  de  diverses  formes  disposées  de manière  à  contrarier,  à  diriger  successivement  en  divers sens  un  courant  d'air  chaud  ou  froid;  à  quoi  on  peut comparer  l'expression  des  marins  chicaner  le  vent.  De  plus, on  trouve,  en  bas  grec,  TlvKdviov\  jeu  de  mail;  t^vKavi- ^siv,  jouer  au  mail.  Tout  cela  ne  laisse  aucun  doute  sur l'étymologie  :  c'est  le  persan  (jt^j^  tchaugân,  bâton  re- courbé, maillet  pour  jouer  au  mail.  Aussi  comprend-on difïicilement  que  Diez  et  Génin  aient  voulu,  après  Mé- nage, chercher  l'origine  de  chicane  dans  l'espagnol  chico, petit,  qui  n'explique  ni  la  forme,  ni  les  sens  de  ce  terme. De  {J^y=^  cljôkân,  forme  arabe  de  Jf^iy^^  dérive  le  por- tugais choca.  (Voy.  Dozy,  Gloss.  p.  2  54.)  Le  changement  de ^  u,  ou,  ou  en  i  est  si  fréquent  qu'il  est  à  peine  besoin  de s'y  arrêter.
Chiffon.  Ital.  chiffone,  arabe  chijfoun,  étoffe  mince  et transparente.  (Defrémery^.)  L'étymologie  est  bonne,  mais il  faut  dire  que  clàj^on  vient  de  chiffe,  vieux  mot  français qui  désigne  une  étoffe  légère  et  de  mauvaise  qualité^,  et
chijfe  est  l'arabe  v-Xii  chiff,  ^tvestis  tenuis  et  pellucida.  w La  terminaison  oun  dans  le  chijffoun  de  M.  Defrémery  est  la nunnation  arabe,  marque  du  nominatif  des  noms  indéter-
'  Voy.  Defrémery,  Mém.  d'hist.  orient,  p.  2  35.  Le  savant  professeur  cite un  passage  du  Voyage  de  Chapelle  et  de  Bachaumont,  ({ui  montre  qu'au XVII*  siècle  chicane  se  disait  du  jeu  du  mail  :  «Nous  y  arrivâmes  à  travers mille  boules  de  mail  :  car  on  joue  là,  le  long  dos  chemins,  à  la  chicane. '•
-  Mém,  d'hist.  orient.  9*  partie,  p;  33/j.
•*  Littré,  Dict.  franc.  Le  mot  chijfe  n'est  pas  encore  hors  d'usage.  Eu  voici un  exemple  pris  dans  la  préface  de  V/ilmagcstc  do  Ptolémée,  par  M.  Hal- uia  :  r Manuscrit  du  Vatican,  en  papier  de  chifTes"  (p.  lij).
DES  MOTS  D'OIUGINE  ORIENTALE.  95
minés.  Ia(juclle  n'a  jamais  joue  aucun  rôle  dans  la  trans- mission des  mots  arabes  aux  autres  langues.  Cf.  cependant zédavon,
(Ihiffre.  Esp.  et  portug.  cijra,  ital.  cifera.  De  l'arabe -jLo  sijr,  vide,  mot  employé  pour  désigner  le  zéro,  qui n'est  que  la  traduction  du  sanscrit  çounya,  par  lequel  ce caractère  est  désigné  dans  les  anciens  traités  d'arithmé- tique indiens.  En  effet,  chiffre,  cljfre,  cyfre,  cyffre,  em- ployé tantôt  au  masculin,  tantôt  au  féminin,  a  marqué primitivement  le  zéro  seuP;  encore  aujourd'hui,  le  por- tugais cifra  et  l'anglais  cipher  s'appliquent  spécialement  à ce  caractère.  Le  même  sens  est  resté  assez  longtemps  au terme  français;  car  on  lit,  dans  un  traité  d'arithmétique du  xvif  siècle  :  ç^La  dernière  figure,  qui  s'appelle  nulle ou  zéro,  ne  vaut  rien. . .  En  autre  langage,  elle  s'appelle chifre;  toutefois  ce  mot  abusivement  prins  en  françois signifie  toutes  les  figures  et  l'art  d'arithmétique  ^.  •)•>
Zéro  est  une  autre  forme  du  même  mot -àao  sifr,  que  les anciens  traités  de  calcul  écrits  en  latin  transcrivent  ze- phyrum,  en  italien  zejîro,  et  enfin  zéro^.  Si  l'on  songe  que l'invention  du  zéro  et  de  son  rôle  est  le  trait  caractéris- tique de  la  numération  écrite  moderne,  on  comprendra que  le  nom  de  ce  caractère  ait  fini  par  s'appliquer  à  toutes les  figures,  longtemps  nommées  figures  de  chiffre.
Chiper.  Tanner  les  peaux  d'une  certaine  façon  diffé- rente de  la  manière  ordinaire.  En  turc,  <-^a«  sep  est  le  tan ou  le  réservoir  où  se  fait  le  tannage,  ou  la  trempe  desti-
--- page
1131 leaf 126
2045 leaf 234
=== LAM 7620-7640
est bien plus conforme à Tétymologie. '
Cheiranthe. Giroflée. D'après Léman : de deux mots
grecs i^iQ et «'«'^otf , ou bien de ^^oç et de cheiri, nom
arabe des giroflées. Chéri, Alcheiri et Keiri, noms de di-
verses variétés de giroflées, viennent aussi de {Sj^ Khev-
rî, giroflée (V. Ibn-Beith. II. 82 et Mas'oûdî. VIII. 270).
Chiffe et son dérivé Chiffon ; de Lii, chiffe étoffe légère
et transparente. Le mot français chiffe a encore mainte-
nant la signification d' « étoffe légère et de mauvaise qua-
lité ». (Litt.) La terminaison on dans chiffon est pour le
diminutif et non la* nunnation, comme on Ta écrit. ( V.
Génin. Récréât, philolol. 86 ).
Chiffre. De Jl^ sifr, vide. Zéro est étymologiquement
le même mot.
Coran et Alcoran; de 0' j^ qorân^ lecture. Alcoran,
malgré l'autorité des classiques, tend à disparaître.
Colcothar. Transcript. de jUaïîï qolqoiâr^ corruption de. FIRM 26 j
```


## [2026-09-14T02:03:21.199Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2035,2050p' DEV.txt | cat -n"
}
```


### [2026-09-14T02:03:21.266Z] TOOL RESULT

```
     1	S
     2	Sabaotii.   Transcription,  dans  les  traductions  latines J de  l'hébreu    nlN3V  tsehaôth,  pluriel  de  N3^  tsahâ ,  armée  : Deussahaoth,  Dieu  des  armées.
     3	Sabbat.  C'est  l'hébreu  nai^  chahhath,  de  la  racine  chahath,
     4	T      -
     5	'  Dioscoridœ  pharni.  hh.  VlJf ,  Slrasb.  i529,  loi.  j  i  verso.
     6	DES  iMOTS  D'ORIGINE  ORIENTALE.  199
     7	se  reposer.  Mais  il  nous  est  venu  par  le  latin  sabhatum, qu'on  trouve  déjà  chez  les  classiques  (Ovide,  Justin,  etc.).
     8	Sacre.  Espèce  de  faucon.  Esp.  et  portug.  sacre.  De l'arabe  yu»  sfl^/',  même  sens,  c^  M.  Diez,  dit  Engelmann, donne  à  ce  mot  une  origine  latine  ;  il  le  considère  comme la  traduction  du  grec  iepaf ,  tandis  que  les  Arabes  auraient emprunté  leur  soijr  aux  langues  romanes;  mais  comme  il est  de  fait  que  saqr,  loin  d'être  un  mot  moderne  et  par- ticulier au  dialecte  vulgaire,  était  déjà  en  usage  parmi les  anciens  Arabes  du  désert  (cf.  Le  divan  des  Hodzdilites, p.  208),  cette  opinion  est  tout  à  fait  erronée,  w  i^Gloss. p.  338.)
     9	Sadder.  Livre  religieux  des  Parsis  ou  Guèbres.  Du persan  )^  J^-o  sad-der,  les  cent  portes,  de  sad,  cent,  et  der, porte,  chapitre  du  Zendavesta.
    10	Safar.  Deuxième  mois  de  l'année  musulmane;  saphar^ dans  les  ouvrages  du  siècle  dernier.  En  arabe  ^io  safar.
    11	Safran.  Esp.  azafrano,.  portug.  açafrào,  itaL  zafferano. On  trouve,  en  vieux  français,  sajleur,  sajlor.  De  l'arabe- persan  ^^')  zayercm  (avec  l'article  az-za  ferâri) ,  même sens.  Le  mot  est  dans  Razi  (man.  déjà  cité,  p.  /i5  recto).
    12	Safre  ou  Saffre.  C'est  aujourd'hui  un  oxyde  de  cobalt. En  espagnol,  zajre  est  un  oxyde  de  bismuth.  Ces  sub- stances, employées  Tune  et  l'autre  dans  la  poterie  ou  la cristallerie,  ont  pu  être  aisément  confondues.  L'oxyde  de cobalt,  qui  lui-même  est  d'un  gris  noirâtre,  sert  à  faire un  verre  bleu  très-foncé,  le  smalt,  lequel,  réduit  en poudre  très-fine,  forme  une  substance  colorante  employée dans  les  arts  sous  le  nom  à'azur.  C'est  pourquoi  plusieurs
    13	200  DICTIONNAIRE  ÉTYMOLOGIQUE
    14	élymologistes  tirent  le  mot  safre  de  saphir^.  Gela  s'appli- querait difficilement  au  zafre  espagnol  qui  donne  une  co- loration non  pas  bleue,  mais  jaune;  et  M.  Dozy  propose de  rapprocher  zafre  de  l'arabe  ylo  sofi%  cuivre  jaune  [so- fra,  couleur  jaune),  qui  a  donné  l'espagnol  azofat%  laiton. Peut-être  saffre,  zafre  et  l'italien  zafjfcra  sont-ils  simple- ment le  mot  ij^-À^')  zaferCm,  safran,  privé  de  sa  finale^, comme  dans  le  pluriel jiUi;  za'âfir.  Les  alchimistes  appe- laient safran  de  mars  l'ocre  rouge  de  fer;  et  le  safran  des métaux  était  une  préparation  pharmaceutique  où  entraient du  soufre  et  de  l'oxyde  d'antimoine.
    15	Sagou.  Fécule  extraite  de  la  moelle  du  palmier  sagus (sagouier  ou  sagoutier).  C'est  le  nom  malais  de  cet  arbre, ^L«  sagou,  qui  pousse  spontanément  dans  l'archipel  In- dien.
    16	Saïque.  Sorte  de  barque  ou  d(;  navire.  Du  turc  AJuUi ihfnqa.
```


## [2026-09-14T02:03:37.294Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n 'https://www.etymonline.com/word/saffron' \\\n 'https://en.wiktionary.org/wiki/safflower' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86' \\\n 'https://www.etymonline.com/word/scimitar' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B4%DB%8C%D8%B1' \\\n 'https://www.etymonline.com/word/chiffon' \\\n 'https://en.wiktionary.org/wiki/%D8%B4%D9%81%D8%A7%D9%81' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%B1%D8%A7%D8%A1' \\\n 'https://www.ahdictionary.com/word/search.html?q=safflower' \\\n 'https://www.ahdictionary.com/word/search.html?q=chiffon' \\\n 'https://abadis.ir/fatofa/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86/' \\\n 'https://abadis.ir/fatofa/%D8%B4%D9%81%D8%A7%D9%81/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 449 verification (saffron/safflower, shamshir/scimitar, chiffon/shaffaf)' 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:03:45.603Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e070336ad057d6a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ec15dab65a4cb06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c98ff1e38e6df815.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a069d295f59eaf6b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e585bf7185f8b672.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97217cfa1004dfe2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8611e1c344481d17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a68ea273f794be0f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3c550fca6576062.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/91d0729df946c36f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19b228de7724acc1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/882ba2bf45a6deb1.txt
```


## [2026-09-14T02:03:51.808Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=saffron",
 "prompt": "Give the American Heritage Dictionary etymology bracket for saffron verbatim (Middle English, Old French safran, Medieval Latin safranum, Arabic za'faran)."
}
```


## [2026-09-14T02:03:53.440Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%81",
 "prompt": "Arabic شف: is there a verb شَفَّ (šaffa) 'to be transparent/thin' and a noun شِفّ (šiff) 'thin garment'? Give the root and any Semitic cognates mentioned."
}
```


### [2026-09-14T02:03:54.766Z] TOOL RESULT

```
According to the dictionary entry, the etymology of saffron is:

"[Middle English _safroun_, from Old French _safran_, from Medieval Latin _safrānum_, from Arabic _za'farān_; akin to Akkadian _azupīru_, of unknown origin.]"

This traces the word's origins through multiple language stages, beginning with Middle English and progressing backward through Old French and Medieval Latin to Arabic, with an additional connection to Akkadian.
```


### [2026-09-14T02:03:57.527Z] TOOL RESULT

```
# Arabic شف Analysis

Based on the Wiktionary entry, **شَفَّ (šaffa)** is indeed documented as a verb meaning "to be seethrough" (Form I geminate verb). The root is **ش ف ف** (š f f).

However, the page does not list a noun **شِفّ (šiff)** meaning "thin garment," nor does it mention any Semitic cognates. The entry provides extensive conjugation tables for the verb across Arabic and South Levantine Arabic dialects, where in the latter dialect it means "to sip," but etymological information and related Semitic terms are absent from this source.
```


## [2026-09-14T02:04:07.871Z] TOOL CALL #62: Bash

```json
{
 "command": "pdftoppm -f 449 -l 449 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg449 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg449.png"
}
```


### [2026-09-14T02:04:09.708Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75433 Sep 13 22:04 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg449.png
```


## [2026-09-14T02:04:11.636Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg449.png"
}
```


### [2026-09-14T02:04:12.157Z] TOOL RESULT

```

```


## [2026-09-14T02:04:12.153Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:04:34.892Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://anglo-norman.net/entry/safran",
 "prompt": "Anglo-Norman Dictionary entry for safran: list the attested variant spellings (does 'safron' or 'safroun' occur?) and the gloss."
}
```


### [2026-09-14T02:04:40.184Z] TOOL RESULT

```
# Anglo-Norman Dictionary Entry: Safran

**Attested Variant Spellings:**

The entry lists numerous variants including: safferan, safferen, safforun, saffran, saffrane, saffrayn, saffren, saffroun, safran, safren, **safron**, **safroun**, saphran, saphron, sauphron, and seffran.

Yes, both "safron" and "safroun" occur among the documented spellings.

**Gloss:**

The primary definition indicates this term refers to "saffron, Crocus sativus" in botanical contexts. Additionally, it denotes "pigment, paint, dye (etc.) derived from the dried and powdered flower or stamen of the Crocus sativus." Compound forms like "saffron de cortil" and "saffron de ort" designate garden saffron or safflower varieties.
```


## [2026-09-14T02:05:09.230Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==445' SKT.txt | head -3; echo '...'; awk 'BEGIN{RS=\"\\f\"} NR==445' SKT.txt | tail -3"
}
```


### [2026-09-14T02:05:10.393Z] TOOL RESULT

```
same  word; it  aUo  appears  as  scull,  Trotl.  v.  5.  3  3.
Schooner;  see  Shun.
Sciatic,  pertaining  to  the  hip-joint.  (F.
...
>al     {F.  -L.  -  Gk.)      O.   F. .■■L.  tpkscopatU,  adj..  from  tpiico-
buUo,  afllicteJ  with  scurvy.  (Low iw  C.)  From  Low  L.  scorbutus^ ;  Laliniscd  from  Low  G.  icharbock, lui,  iciirry;  O.  Du.  icheurbuyik. The  name  15  due  to  some  con- AS  the  lit.  sense  of  O.  Do.  scheur- I  •  rupture  of  the  bcUy.'  from  scheur- nr,  and  buy(k  (mod.  Du.  huik),  the
!h.  (F.-L.)  O.  F.  escorc
```


## [2026-09-14T02:05:18.106Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nprint('leaves',t.count('\\f')+1)\""
}
```


### [2026-09-14T02:05:19.338Z] TOOL RESULT

```
leaves 657
```


## [2026-09-14T02:05:31.450Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo '=== FSD1 chiffon'; grep -n \"chif'fon\\|chiffon\" FSD_vol1.txt | head -3; echo '=== WEB chiffon'; grep -n -i 'chiffon' WEB*.txt 2>/dev/null | head -3; ls WEB* 2>/dev/null; echo '=== KLN 1971 chiffon'; grep -n -i 'chiffe' KLN_1971.txt | head -3"
}
```


### [2026-09-14T02:05:31.562Z] TOOL RESULT

```
=== FSD1 chiffon
74836:com 'mo-date,  1   kem'o-det;  2   cdm'o-dfit,  n.  Scots  Law.  A loan  made  free  of  charge  on  condition  of  return  undamaged. [<  LL.  commodalum,  <   L.  commodo,  adapt,  <   com  mo- dus; see  commodious.]  com"mo-da'(ura{.-  com"mo- da'ta-ry,  n.  The  receiver  of  a   commodate. com"mo-da't!ont>  n.  Accommodation;  adaptedness, com-mode't,  a.  1.  Convenient.  2.  Accommodating, corn-mode',  1   ke-mod'^2  c5-mod',  n.  1.  An  article  of furniture  to  contain  things  for  convenience.  (1)  A   set of  drawers;  a   chiffonier.  (2)  A   covered  wash-stand  with basin,  waste-pipe,  or  other  conveniences.  (3)  A   night-chair or  *stooI.  2.  A   head-dress  worn  by  women  about  1700.
=== WEB chiffon
32188:chiffon
32197:chiaf’ry, chiéf’rie, n. 1. rent paid to ais 2. the domain or system of governmenn lord or chief, especially of ancien ye Abe chiéf’ tain (-tin), n. [ME. chefelain eS T taine; LL. capitanus, a commander, A t, head. DE chief le a clan or mibe, 2, any leader of a group. ; née chiaf/tain-cy, n.; pl. chief’ tain-cles, Mf a shipi captaincy; the rank or pos chief! tain-ship; n. same as chieftaincy- fellow: chiela, n. a young man; 2 youth; i i a an end; Beeson: and v.t. to come one to to prosper or accompli L A i ng iff’ cha . the white 1 er ote. ae nk so called from its nO called petlychaps. a (or shi-fon’), 7. [Er] ides worn “4. [pl.] any ornamental eae Asa , laces, Ete- w women ue Par material used for dresses, blouses, etc. nek chif/fon, a. 1. made ot © * 9, light and fluffy from a lemon chiffon pie filling.
32221:chiffonier
WEB_vol1.txt
=== KLN 1971 chiffon
45175:dresses. — F., fr. chiffe, ‘rag’, pi. ‘clothes’, fr.
```


## [2026-09-14T02:06:04.150Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in 'https://anglo-norman.net/entry/safran' 'https://www.ahdictionary.com/word/search.html?q=saffron' 'https://en.wiktionary.org/wiki/%D8%B4%D9%81'; do python3 tools/fetch_source.py \"$u\" --note 'page 449 verification (OF safron variant; AHD saffron; Arabic root sh-f-f)' 2>&1 | tail -1; done; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg449.png data/verification/sources/refs/ocr/BOOK/449.png && echo copied"
}
```


### [2026-09-14T02:06:06.975Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9934a4d15c8c377f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c72c70fb80b382ea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a9e4870a4c691e5.txt
copied
```


## [2026-09-14T02:06:09.673Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:06:09.720Z] TOOL RESULT

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


## [2026-09-14T02:13:14.603Z] TOOL CALL #70: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-449.json <<'JSONEOF'\n{\n  \"pdf_page\": 449,\n  \"book_page\": 419,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Š.f.f\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Arabic root ش ف ف (š-f-f) 'to be thin and let light through, be transparent'\",\n      \"note\": \"The root itself is real and correctly glossed: Arabic شَفَّ (šaffa) 'to be see-through', root ش ف ف, with شَفّ/شِفّ 'a thin diaphanous garment', شَفّاف 'transparent', شَفافيّة 'transparency'. The reservation is the language label: Nourai writes [Semitic], but his own authority Klein (KLN:275 s.v. chiffon) cites only 'Arab. shaffa'; no Hebrew/Aramaic/Akkadian cognate of a root *š-p-p 'be transparent' turned up in Klein, Fraenkel (AFA) or Wiktionary, so the root is securely Arabic but not demonstrably common Semitic. Everything inside the Arabic box is confirmed; the doubtful link is the French one (see node #4), and Nourai's own NOTE that AHD takes chiffon to a different origin is correct.\",\n      \"note_fa\": \"ریشهٔ عربی «ش‌ف‌ف» به معنی «نازک و نورگذر بودن» است: شَفَّ «نازک و روشن بود»، شِفّ «جامهٔ نازک»، شَفّاف «روشن، نورگذر». تا اینجا ادعای نورایی درست است، اما برچسب «سامی» بیش از آن چیزی است که منبع خودِ او (کلاین ۲۷۵) می‌گوید؛ کلاین تنها صورت عربی را می‌آورد و در فرانکل و ویکی‌واژه هم‌ریشهٔ عبری یا آرامی برای این ریشه یافت نشد. بنابراین ریشه را باید «عربی» دانست نه «سامی مشترک»؛ حلقهٔ سست این نمودار پیوند فرانسویِ chiffe است (بند ۴).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B4%D9%81\",\n        \"https://en.wiktionary.org/wiki/%D8%B4%D9%81%D8%A7%D9%81\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:275\", \"status\": \"partial\", \"note\": \"Klein 1966 s.v. 'chiffon' (local KLN_1966.txt line 7396, leaf 156, printed page ~288 in this scan — Nourai's 275 is close but the scan carries no page numerals): 'F., fr. chiffe, \\\"rag\\\", pl. \\\"clothes\\\", fr. Arab. shiff, \\\"light garment\\\", fr. shaffa, \\\"it was fine and transparent\\\" (said of materials)'. Klein has the root and gloss exactly, but labels it Arabic, not Semitic.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7396 (s.v. chiffon)\", \"stance\": \"partial\", \"note\": \"'fr. Arab. shiff, \\\"light garment\\\", fr. shaffa, \\\"it was fine and transparent\\\"' — root yes, 'Semitic' label no.\"},\n        {\"src\": \"AFA\", \"where\": \"AFA.txt, grep 'transparent|Safran|schiff'\", \"stance\": \"silent\", \"note\": \"Fraenkel's Aramäische Fremdwörter has no entry for a root š-p-p 'be transparent' (grep found nothing usable), so no Aramaic cognate is documented there.\"},\n        {\"src\": \"DEV\", \"where\": \"p. 94-95 s.v. Chiffon\", \"stance\": \"supports\", \"note\": \"'chiffe est l'arabe شف chiff, \\\"vestis tenuis et pellucida\\\"' — Devic knows the Arabic word with exactly this sense.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"šaffa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic شَفَّ (šaffa), a geminate Form-I verb of the root ش ف ف, 'to be thin/diaphanous, to let what is behind show through' (said of cloth). Wiktionary lists it as Form I geminate with the gloss 'to be seethrough'; Klein glosses it 'it was fine and transparent (said of materials)'. The verb is simply the root realised as fa'ala, so the arrow root → verb is a morphological identity, not a derivation across languages.\",\n          \"derivation_fa\": \"فعل عربی شَفَّ (باب فَعَلَ مضاعف) از ریشهٔ «ش‌ف‌ف» به معنی «نازک و نورگذر بودن» است؛ دربارهٔ پارچه به کار می‌رود، یعنی «آنچه پشتش پیداست». پیکان از ریشه به این فعل در واقع صورت‌بندی صرفی همان ریشه است، نه دگرگونی آوایی. ویکی‌واژه و کلاین (ص ۲۷۵) هر دو همین معنی را می‌دهند؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D9%81\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:275\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 7396: '...fr. shaffa, \\\"it was fine and transparent\\\" (said of materials)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7396 (also KLN_1971.txt line 45175, same wording)\", \"stance\": \"supports\", \"note\": \"'fr. Arab. shiff, \\\"light garment\\\", fr. shaffa'.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt line 1131-1133, printed p. 94-95\", \"stance\": \"supports\", \"note\": \"'chiffe est l'arabe شف chiff, \\\"vestis tenuis et pellucida\\\"' — Devic cites the same Arabic material.\"},\n            {\"src\": \"LAM\", \"where\": \"LAM.txt line 7630 s.v. Chiffe\", \"stance\": \"supports\", \"note\": \"'Chiffe et son dérivé Chiffon; de [شف], chiffe étoffe légère et transparente.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"šaffâf\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian شفّاف (šaffāf) is the Arabic intensive adjective فَعّال of the same root (šaffāf 'very transparent'), taken over unchanged as an Arabic loanword in New Persian; the abstract شفّافیّت (šaffāfiyyat, printed by Nourai as the second Persian form) is likewise the Arabic nisba-abstract شَفافيّة borrowed with the Persian pronunciation of -iyyat. Mo'in tags the entry '[ع.]' (= Arabic) and glosses it 'هرچیز لطیف و نازک که از پشت آن چیزهای دیگر دیده شود'. In modern Persian usage šaffāf has additionally acquired the political sense 'open, accountable' (شفافیت 'transparency'), a 20th-century calque on European usage.\",\n          \"derivation_fa\": \"«شفّاف» صفت مشبههٔ عربی بر وزن فَعّال از ریشهٔ «ش‌ف‌ف» است که بی‌هیچ دگرگونی آوایی وارد فارسی شده؛ «شفّافیّت» نیز مصدر صناعی عربی شَفافيّة است. معین در فرهنگ خود آن را با نشان «[ع.]» یعنی عربی آورده و چنین معنی کرده است: «هرچیز لطیف و نازک که از پشت آن چیزهای دیگر دیده شود». معنای امروزی «شفافیت» در سیاست و اداره، گرته‌برداری سدهٔ بیستم از transparency اروپایی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%81%D8%A7%D9%81\",\n            \"https://abadis.ir/fatofa/%D8%B4%D9%81%D8%A7%D9%81/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in via abadis.ir: 'شفاف [ع.] (ص.) هرچیز لطیف و نازک که از پشت آن چیزهای دیگر دیده شود' — the bracket [ع.] is Mo'in's Arabic-origin tag. Nourai gives no page, so the page itself cannot be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. شفاف\", \"stance\": \"supports\", \"note\": \"'[ع.] (ص.) هرچیز لطیف و نازک که از پشت آن چیزهای دیگر دیده شود'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/شفاف\", \"stance\": \"supports\", \"note\": \"'Persian: borrowed from Arabic شَفَّاف (šaffāf), root ش ف ف'; Ottoman Turkish شفاف likewise from Arabic.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep شفاف\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-root dictionary has no entry (as expected for an Arabic loan).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"šiff\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic شِفّ (šiff), also شَفّ (šaff), is the verbal noun / result-noun of šaffa: 'a thin, fine, diaphanous garment or veil' (Lane: 'a thin, fine garment through which what is behind shows'). Klein cites it in exactly this form and sense ('Arab. shiff, \\\"light garment\\\"'), and Devic renders it with the Latin gloss 'vestis tenuis et pellucida'. The step šaffa → šiff is internal Arabic derivation (fiʿl form of the geminate root), not a borrowing.\",\n          \"derivation_fa\": \"شِفّ (یا شَفّ) اسمِ برگرفته از همان فعل شَفَّ است به معنی «جامهٔ نازک و نورگذر»؛ لین آن را «جامهٔ نازکی که آنچه پشت آن است پیدا باشد» معنی کرده و دِویک آن را با عبارت لاتین «vestis tenuis et pellucida» آورده است. گذر از شَفَّ به شِفّ اشتقاق درون‌عربی است، نه وام‌گیری. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/chiffon\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:275\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 7396: 'fr. Arab. shiff, \\\"light garment\\\", fr. shaffa'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"DEV.txt line 1131-1133, printed p. 94-95 s.v. Chiffon\", \"stance\": \"supports\", \"note\": \"'chiffe est l'arabe شف chiff, \\\"vestis tenuis et pellucida\\\"'.\"},\n            {\"src\": \"LAM\", \"where\": \"LAM.txt line 7630\", \"stance\": \"supports\", \"note\": \"'de [شف], chiffe étoffe légère et transparente'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 7396\", \"stance\": \"supports\", \"note\": \"same wording as the ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"chiffe\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French chiffe (attested 16th c.) 'a poor, flimsy cloth; a rag'. The Arabic derivation drawn here is a real scholarly position, not Nourai's invention: Defrémery proposed it, Devic (1876, p. 94-95) endorsed it ('L'étymologie est bonne... chiffe est l'arabe shiff'), Lammens repeats it, and Klein (Nourai's source) adopts it. But it is a minority view today. AHD derives chiffon 'from chiffe, rag, alteration (influenced by Old French chifre \\\"zero, thing of little value\\\") of Old French chipe', itself from Middle English chip; Etymonline lists the Arabic proposal only as one of several ('perhaps a variant of English chip... an Arabic source [Klein]... origin unknown'), and Skeat's Concise (s.v. Chiffonier) simply says 'orig. unknown'. Phonetically Arabic šiff → OF chiffe is unobjectionable (Arabic š- regularly gives French ch-, as in chiffre < ṣifr), so the case rests on documentation of the borrowing route, which nobody has produced.\",\n          \"derivation_fa\": \"واژهٔ فرانسوی chiffe «پارچهٔ نازک و بی‌کیفیت، کهنه» از سدهٔ شانزدهم گواهی شده است. ریشه‌یابی عربی آن (از شِفّ) از دفرِمری آغاز شد، دِویک (۱۸۷۶، ص ۹۴–۹۵) آن را پذیرفت («این ریشه‌شناسی درست است… chiffe همان شِفّ عربی است»)، لامنس تکرارش کرد و کلاین — منبع خودِ نورایی — آن را برگزید. اما دیدگاه غالب امروز این نیست: فرهنگ AHD آن را دگرگون‌شدهٔ chipe فرانسوی کهن (از chip انگلیسی میانه) با اثرپذیری از chifre «صفر، چیز بی‌ارزش» می‌داند و اتیمانلاین فرضیهٔ عربی را تنها یکی از چند احتمال می‌شمارد. از نظر آوایی «ش» عربی در فرانسوی به ch بدل می‌شود (چنانکه صِفر ← chiffre)، پس اشکال آوایی در کار نیست؛ اشکال در نبودِ سند راهِ وام‌گیری است. پس: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chiffon\",\n            \"https://www.ahdictionary.com/word/search.html?q=chiffon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the arrow is implicitly covered by KLN:275 on the neighbouring boxes, which does assert Arab. shiff > F. chiffe.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"DEV.txt line 1131-1134, printed p. 94-95 s.v. Chiffon\", \"stance\": \"supports\", \"note\": \"'Chiffon. Ital. chiffone, arabe chiffoun... L'étymologie est bonne, mais il faut dire que chiffon vient de chiffe, vieux mot français... et chiffe est l'arabe shiff, \\\"vestis tenuis et pellucida\\\".'\"},\n            {\"src\": \"LAM\", \"where\": \"LAM.txt line 7630-7634\", \"stance\": \"supports\", \"note\": \"'Chiffe et son dérivé Chiffon; de [شف]... La terminaison on dans chiffon est pour le diminutif et non la nunnation.'\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. chiffon\", \"stance\": \"contradicts\", \"note\": \"'[French, rag... from chiffe, rag, alteration (influenced by Old French chifre, zero, thing of little value) of Old French chipe]' < Middle English chip.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 3378 s.v. Chiffonier\", \"stance\": \"contradicts\", \"note\": \"'(F. ...) rag-picker, also a cupboard. — F. ... orig. unknown.' Skeat records no Arabic source.\"},\n            {\"src\": \"PHN\", \"where\": \"PHN.txt, grep 'chiffe|chiffon'\", \"stance\": \"silent\", \"note\": \"Pihan's dictionary of French orientalisms has no CHIFFE/CHIFFON headword.\"},\n            {\"src\": \"DOZ\", \"where\": \"DOZ.txt, grep 'chiffe|chiffon'\", \"stance\": \"silent\", \"note\": \"Dozy's Oosterlingen has no corresponding entry.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"chiffon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English chiffon is a straightforward 18th-century borrowing of French chiffon, the -on diminutive of chiffe ('rag' → 'scrap of finery'), first in English in 1765 in the sense 'feminine finery, ornamental trimmings' (usually plural 'chiffons'); the modern sense 'sheer silk gauze' is only from 1890, and the dessert sense from 1929. Lammens notes correctly that the -on is the French diminutive suffix and not, as had been claimed, the Arabic nunation of a form *šiffun. Nourai's own NOTE — 'AHD derives this word from a different root' — is accurate: AHD takes chiffe back to Old French chipe < Middle English chip, not to Arabic (see node #4). The French → English step itself is uncontested.\",\n          \"derivation_fa\": \"«chiffon» انگلیسی وام‌واژهٔ سدهٔ هجدهم از فرانسوی chiffon است که خود مصغّر chiffe («کهنه، پارچهٔ نازک») با پسوند -on است؛ نخستین کاربرد انگلیسی آن در ۱۷۶۵ به معنی «زیورهای زنانه» است و معنای امروزی «پارچهٔ ابریشمی نازک» تنها از ۱۸۹۰ دیده می‌شود. لامنس به‌درستی یادآور شده که -on پسوند تصغیر فرانسوی است نه تنوینِ عربیِ *šiffun. یادداشت خودِ نورایی که «AHD این واژه را از ریشه‌ای دیگر می‌گیرد» درست است. خودِ حلقهٔ فرانسوی ← انگلیسی بی‌چون‌وچرا پذیرفته است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chiffon\",\n            \"https://www.ahdictionary.com/word/search.html?q=chiffon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:275\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 7396: 'chiffon, n., a sheer silk fabric used for women's dresses. — F., fr. chiffe, \\\"rag\\\", pl. \\\"clothes\\\"...' — the French→English step exactly as drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. chiffon\", \"stance\": \"partial\", \"note\": \"confirms French chiffon > English, but takes chiffe to Old French chipe < ME chip — i.e. Nourai's NOTE about AHD is correct.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 32197 s.v. chiffon\", \"stance\": \"partial\", \"note\": \"Webster's 2nd gives only '[Fr.]' — French source, no ulterior etymology.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 3378\", \"stance\": \"partial\", \"note\": \"Skeat has only Chiffonier, 'orig. unknown'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"S.f.r, Asfar\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root ص ف ر (ṣ-f-r) 'to be yellow'; أَصْفَر (ʔaṣfar) 'yellow', fem. صَفْرَاء (ṣafrāʔ)\",\n      \"note\": \"The root box is right: ṣ-f-r is the ordinary Arabic colour root, with the elative-pattern colour adjective aṣfar / fem. ṣafrāʔ 'yellow' (Wiktionary s.v. صفراء: 'feminine singular of أَصْفَر (ʔaṣfar)', root ص ف ر), and the derivatives ṣufrah 'yellowness', ʿuṣfur 'safflower', iṣfirār 'turning yellow'. The right-hand branch of the chart (ṣafrāʔ 'yellow/bile' → Persian صفرا, Italian saffiore → safflower) is sound. The left branch is not: making زَعْفَران (zaʿfarān) a derivative of ṣ-f-r is not accepted by modern scholarship (see node #1), which is also why Nourai's own three marginal NOTEs contradict each other. Of those NOTEs: PLA:145 (Asbaghi) really does derive zaʿfarān from Persian zar-parān and that view is still current enough to be cited on Wiktionary; the two CEL6 claims are worthless — an Indo-European *kes- 'hair' source is phonetically impossible for a word with ز and ع, and the claim that the Arabs got saffron from Kashmir only in the 9th-10th century is refuted by the word's appearance in pre-Islamic Arabic poetry and by Akkadian azupīru.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است: «ص‌ف‌ر» ریشهٔ رنگِ زرد در عربی است با صفت أَصْفَر (مؤنث صَفْراء) «زرد»، و مشتقاتی چون صُفرة، عُصفُر و اصفِرار. شاخهٔ راست نمودار (صفراء «زرد/صفرا» ← فارسی صفرا؛ ایتالیایی saffiore ← safflower) پذیرفتنی است، اما شاخهٔ چپ نه: گرفتن «زعفران» از ریشهٔ «ص‌ف‌ر» را ریشه‌شناسی امروزی نمی‌پذیرد (بند ۱). از سه یادداشت خودِ نورایی: ادعای اسبغی (PLA:145) دربارهٔ «زرپران» واقعاً در آن کتاب هست و هنوز نقل می‌شود؛ اما دو ادعای CEL۶ بی‌پایه است — ریشهٔ هندواروپایی *kes- «مو» با واژه‌ای که «ز» و «ع» دارد از نظر آوایی ناسازگار است، و اینکه عرب‌ها زعفران را تازه در سدهٔ نهم–دهم از کشمیر آورده باشند با کاربرد واژه در شعر جاهلی و با azupīru اکدی نقض می‌شود.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%B1%D8%A7%D8%A1\",\n        \"https://www.ahdictionary.com/word/search.html?q=saffron\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVA:232\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: refs_online.json records no digital copy anywhere (archive.org, ketabnak, noorlib all searched), and there is no local file, so p. 232 cannot be read.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/صفراء\", \"stance\": \"supports\", \"note\": \"'feminine singular of أَصْفَر (ʔaṣfar)' = yellow; noun 'bile'; root ص ف ر; borrowings listed: Persian صفرا, Turkish safra, Spanish zafra, Swahili safura.\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 35938 s.v. Sophora\", \"stance\": \"supports\", \"note\": \"'fr. Arab. ṣufārah, \\\"yellow plants\\\", which is rel. to uṣfur, fem. ṣafrāʾ, \\\"yellow\\\"' — Klein's own statement of the root.\"},\n        {\"src\": \"LKT\", \"where\": \"LKT.txt entry 2178 (printed p. ~250)\", \"stance\": \"partial\", \"note\": \"Lokotsch gives 'Ar. zaʿfarān: Safran' as the source of the European words but says nothing about its connection with ṣ-f-r.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"za`farân\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic زَعْفَران (zaʿfarān) 'saffron, Crocus sativus' is old and well attested (pre-Islamic poetry; Rāzī's medical manuscripts, cited by Devic), but deriving it from the root ṣ-f-r 'yellow' as this arrow does is rejected by modern scholarship: the initial ز (z) and medial ع (ʿ) cannot be reconciled with ص-ف-ر, and no Arabic grammarian derives it that way. AHD states flatly '[...] from Arabic zaʿfarān; akin to Akkadian azupīru, of unknown origin'; Etymonline likewise 'from Arabic az-zaʿfaran, of unknown origin'. Wiktionary offers three competing accounts — a borrowing from Aramaic ṣpr with an added -ān, an internal Arabic formation on the pattern of زعتر zaʿtar and عصفر ʿuṣfur (this is the only one that touches ṣ-f-r, and only obliquely), and a Middle Iranian borrowing. Nourai's own NOTE reports Asbaghi (PLA:145), which I read on the page: 'zaʿfarān: \\\"Safran\\\" pers., wahrscheinlich aus dem pers. زرپران zarparān \\\"mit goldenen Blättern\\\", mand. zaparania, syr. ...' — i.e. Asbaghi makes it a Persian loan, the opposite direction from the arrow drawn. Against that, Dehkhoda quotes al-Jawāliqī's al-Muʿarrab p.173, 'عربی صحیح است' ('it is genuine Arabic'). The honest verdict is 'origin uncertain, certainly not a transparent ṣ-f-r derivative'.\",\n          \"derivation_fa\": \"«زعفران» عربی واژه‌ای کهن و پرکاربرد است (در شعر جاهلی و در نسخه‌های پزشکی رازی)، اما گرفتن آن از ریشهٔ «ص‌ف‌ر» — چنانکه این پیکان می‌گوید — پذیرفتنی نیست: «ز» آغازین و «ع» میانی با ص‌ف‌ر سازگار نمی‌شود. فرهنگ AHD می‌نویسد «از عربی زعفران، هم‌ریشه با azupīru اکدی، با خاستگاه ناشناخته» و اتیمانلاین نیز «خاستگاه نامعلوم». ویکی‌واژه سه فرضیه می‌آورد: وام از آرامی ṣpr با پسوند ān؛ ساختی درون‌عربی بر قیاس «زعتر» و «عُصفُر»؛ و وام‌گیری از ایرانی میانه. یادداشت خودِ نورایی به اسبغی (PLA:145) ارجاع می‌دهد و متن آن صفحه را خواندم: «زعفران: “Safran”، فارسی، احتمالاً از فارسی زرپران “دارای برگ‌های زرین”، مندایی zaparania، سریانی …» — یعنی اسبغی جهت وام‌گیری را وارونهٔ نمودار می‌داند. در برابر، دهخدا از «المعرّب» جوالیقی (ص ۱۷۳) نقل می‌کند: «عربی صحیح است». نتیجه: پژوهش امروزی این پیکان را رد می‌کند و خاستگاه واژه را نامعلوم می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86\",\n            \"https://www.etymonline.com/word/saffron\",\n            \"https://www.ahdictionary.com/word/search.html?q=saffron\",\n            \"https://abadis.ir/fatofa/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FSD:2157\", \"status\": \"partial\", \"note\": \"Funk & Wagnalls New Standard, vol. IV leaf 9 (≈ printed pp. 2153-2157) carries saffron / safflower / safranin; the OCR of the saffron etymology bracket is broken, but the neighbouring safflower bracket reads '( < OF saflor, < O It saflore, < Ar ʿuṣfur, < ṣafrā, yellow )' and safranin '[< F safran, see SAFFRON]'. So F&W does tie the ṣ-f-r material together on this page, but for saffron itself no ṣ-f-r derivation could be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 145 (PLA_pages.txt lines 8279-8283; the running head 'zufāna 146 zanburak' sits at the top of the next page)\", \"stance\": \"contradicts\", \"note\": \"'zaʿfarān: \\\"Safran\\\" pers., wahrscheinlich aus dem pers. زرپران zarparān \\\"mit goldenen Blättern\\\", mand. zaparania, syr. ... → afrz. safran, mhd. Safran, dtsch. Safran' — Persian source, not an Arabic ṣ-f-r derivative. Confirms Nourai's NOTE verbatim.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. saffron\", \"stance\": \"contradicts\", \"note\": \"'from Arabic zaʿfarān; akin to Akkadian azupīru, of unknown origin.'\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entry 2178\", \"stance\": \"partial\", \"note\": \"'Ar. zaʿfarān: \\\"Safran Memocylon tinctorium\\\"; hieraus it. zafferano, frz. Safran, sp. azafrán...' — Arabic as the source of the European words, silent on its own origin.\"},\n            {\"src\": \"MON\", \"where\": \"Dehkhoda quoted on abadis.ir s.v. زعفران\", \"stance\": \"contradicts\", \"note\": \"'عربی صحیح است. (از المعرب جوالیقی ص ۱۷۳)' — Jawāliqī treats it as genuine Arabic, i.e. not analysable and not a loan.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep زعفران\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words arabicised has no زعفران headword (the three hits are inside other entries), so he did not count it a Persian loan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"za`farân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian زعفران (zaʿfarān) is the Arabic word taken over unchanged, ʿayn and all — the surest sign of an Arabic-mediated loan in Persian. Mo'in's entry tags it '[ع.]' (Arabic) and defines it as the perennial of the iris family with long green leaves; Wiktionary's Persian entry likewise reads 'borrowed from Arabic زَعْفَرَان (zaʿfarān)', with کرکم as its synonym. If Asbaghi is right that the Arabic word itself began as Persian zar-parān (node #1), then the Persian word is a round trip: Middle Iranian → Arabic → New Persian, of which the present form preserves only the Arabic shape.\",\n          \"derivation_fa\": \"«زعفران» فارسی نو همان واژهٔ عربی است که دست‌نخورده — با «ع» و همه — وام گرفته شده، و همین «ع» مطمئن‌ترین نشانهٔ وام‌گیری از راه عربی است. معین آن را با نشان «[ع.]» می‌آورد و «گیاهی است پایا از تیرهٔ زنبقی‌ها با برگ‌های دراز و سبز» معنی می‌کند؛ ویکی‌واژه نیز می‌نویسد «وام‌گرفته از عربی زَعْفَرَان» و «کرکم» را هم‌معنی آن می‌شمارد. اگر نظر اسبغی (بند ۱) درست باشد که خودِ واژهٔ عربی از «زرپران» فارسی آمده، آنگاه این واژه یک «دوگردش» است: ایرانی میانه ← عربی ← فارسی نو، و صورت امروزی تنها قالب عربی را نگاه داشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86\",\n            \"https://abadis.ir/fatofa/%D8%B2%D8%B9%D9%81%D8%B1%D8%A7%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1739\", \"status\": \"supports\", \"note\": \"The 6-vol Mo'in is not online and its pages cannot be mapped, but the entry text via abadis.ir reads '(زَ فَ) [ع.] (اِ.) گیاهی است پایا از تیرة زنبقی‌ها با برگ‌های دراز و سبز' — Arabic-origin tag exactly as the arrow requires.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. زعفران\", \"stance\": \"supports\", \"note\": \"'[ع.]' = Arabic loan.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/زعفران (Persian section)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic زَعْفَرَان (zaʕfarān)'; etymology tree Aramaic → Arabic → Persian.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 145\", \"stance\": \"partial\", \"note\": \"would make the Persian form a re-borrowing of an originally Persian zar-parān, i.e. the same Arabic→Persian step but with a prior Persian→Arabic one.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"safranum\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Medieval Latin safrānum, the apothecaries' and herbalists' Latin for saffron, is the Arabic zaʿfarān Latinised: the Arabic article az- is dropped in the Italian/French line (it is kept in Ibero-Romance: Spanish azafrán, Portuguese açafrão), the initial z- appears as s- in the French-Latin chain but as z- in Italian zafferano, the ʿayn is lost with compensatory lengthening, and the ending is fitted to the Latin second declension. It is the immediate source of Old French safran (12th c.) and the base of the whole Northern European set. Klein and AHD both give exactly this step.\",\n          \"derivation_fa\": \"safrānum لاتین میانه، همان واژهٔ عربی «زعفران» است که به قالب لاتین درآمده: حرف تعریف «ال» در شاخهٔ ایتالیایی–فرانسوی افتاده (ولی در اسپانیایی azafrán و پرتغالی açafrão مانده است)، «ع» از میان رفته، «ز» آغازین در این شاخه به s بدل شده (در ایتالیایی zafferano همان z مانده) و پایانهٔ -um صرفِ لاتین بدان افزوده شده است. این صورت، سرچشمهٔ بی‌واسطهٔ safran فرانسوی کهن (سدهٔ دوازدهم) و پایهٔ همهٔ صورت‌های شمال اروپاست. کلاین و AHD هر دو همین مرحله را می‌آورند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/saffron\",\n            \"https://www.ahdictionary.com/word/search.html?q=saffron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"DEV:199\", \"status\": \"partial\", \"note\": \"Devic p. 199 exactly (the running heads 'DES MOTS D'ORIGINE ORIENTALE. 199' and '200 DICTIONNAIRE ÉTYMOLOGIQUE' bracket the entry in DEV.txt lines 2040-2048): 'Safran. Esp. azafrano, portug. açafrão, ital. zafferano. On trouve, en vieux français, safleur, saflor. De l'arabe-persan زعفران zaʿferān (avec l'article az-zaʿferān), même sens. Le mot est dans Razi.' Devic has the Arabic source and the Romance forms but does not name a Middle Latin safranum.\"},\n            {\"ref\": \"KLN:1372\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 33478 (leaf 729): 'saffron, n. — ME. saffron, fr. OF. (= F.) safran, fr. ML. safranum, fr. Arab. zaʿfaran, whence also It. zafferano, Sp. azafran.' Exactly the chain. (The scan has no page numerals; by leaf arithmetic this sits near p. 1430, so Nourai's 1372 may follow a different printing.)\"},\n            {\"ref\": \"PRT:581\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins: all archive.org copies are lending-only (originsshortetym00part etc.); no open text.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 33478\", \"stance\": \"supports\", \"note\": \"'fr. ML. safranum, fr. Arab. zaʿfaran'.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. saffron\", \"stance\": \"supports\", \"note\": \"'from Old French safran, from Medieval Latin safrānum, from Arabic zaʿfarān'.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entry 2178\", \"stance\": \"partial\", \"note\": \"lists it. zafferano, frz. safran, sp. azafrán directly from Ar. zaʿfarān, with no Latin waystation named.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old French\",\n          \"words\": \"safron\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French / Anglo-Norman safran, with the widely attested variant safron (and safroun, saffroun, saffran, saphron...), is the regular continuation of Medieval Latin safrānum — the Latin ending is dropped, giving safran, and the unstressed -a- rounds to -o- in the insular tradition. The Anglo-Norman Dictionary lists 'safron' and 'safroun' explicitly among the spellings of safran 'saffron, Crocus sativus', so Nourai's form (which the printed page really does show as 'safron') is an attested variant, not an error — and it is precisely the variant that explains English saffron rather than *saffran. AHD gives the same step but cites the base form: 'Middle English safroun, from Old French safran'.\",\n          \"derivation_fa\": \"صورت فرانسوی کهن/آنگلونورمن safran با گونهٔ پرکاربرد safron (و نیز safroun، saffroun، saphron…) دنبالهٔ قاعده‌مند safrānum لاتین میانه است: پایانهٔ لاتین می‌افتد و مصوت بی‌تکیهٔ a در سنت جزیره‌ای (انگلستان) به o گرد می‌شود. فرهنگ آنگلونورمن هر دو گونهٔ safron و safroun را ذیل safran ثبت کرده است، پس صورتی که نورایی آورده (و در چاپ کتاب هم همان «safron» است) گونه‌ای گواهی‌شده است نه خطا — و درست همین گونه است که saffron انگلیسی را توضیح می‌دهد. AHD همین مرحله را با صورت پایه می‌آورد: «انگلیسی میانه safroun، از فرانسوی کهن safran». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://anglo-norman.net/entry/safran\",\n            \"https://www.ahdictionary.com/word/search.html?q=saffron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1142\", \"status\": \"supports\", \"note\": \"The 1976 New College page is not open online, but the same entry in the current AHD reads '[Middle English safroun, from Old French safran, from Medieval Latin safrānum, from Arabic zaʿfarān; akin to Akkadian azupīru, of unknown origin.]' — the Old French step is AHD's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AND\", \"where\": \"anglo-norman.net/entry/safran\", \"stance\": \"supports\", \"note\": \"variants listed include 'safron' and 'safroun'; gloss 'saffron, Crocus sativus'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 33478\", \"stance\": \"supports\", \"note\": \"'ME. saffron, fr. OF. (= F.) safran'.\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt printed p. 199\", \"stance\": \"partial\", \"note\": \"gives the Romance forms and the Old French safleur/saflor but not safran/safron as a headword form.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"saffron, safranine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English saffron is attested c.1200 (Middle English safroun) from the Anglo-Norman form; 'saffron' as a colour term follows in the late 14th c. and as the name of the crocus in the early 15th. Safranine (also safranin) is a quite separate, 19th-century chemical coinage: French safranine, from safran + the chemical suffix -ine, the name of a synthetic orange-red azonium dye — Klein says so explicitly, and Funk & Wagnalls likewise '[< F safran, see SAFFRON]'. So both words in the box descend from the Old French form, but by very different routes (medieval loan vs. modern learned formation), which the chart's single arrow does not distinguish.\",\n          \"derivation_fa\": \"«saffron» انگلیسی از حدود ۱۲۰۰ م. (انگلیسی میانه safroun) از صورت آنگلونورمن وام گرفته شده؛ کاربرد آن به‌عنوان نام رنگ از اواخر سدهٔ چهاردهم و نام گیاه زعفران از آغاز سدهٔ پانزدهم است. اما «safranine» واژه‌ای یکسره جداست: ساختهٔ سدهٔ نوزدهم در فرانسوی از safran + پسوند شیمیایی -ine، نام رنگ‌دانهٔ مصنوعی نارنجی‌ـ‌سرخ؛ کلاین و فانک‌ووگنالز هر دو همین را می‌گویند. پس هر دو واژه به صورت فرانسوی کهن بازمی‌گردند، ولی از دو راه بسیار متفاوت (وام‌واژهٔ قرون وسطایی در برابر ساختِ علمی نو) که نمودار با یک پیکان آن دو را یکی گرفته است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/saffron\",\n            \"https://www.ahdictionary.com/word/search.html?q=saffron\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. saffron: '[Middle English safroun, from Old French safran...]'. AHD has no separate etymology for safranine in the free online edition, but the formation is standard.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 33478-33480\", \"stance\": \"supports\", \"note\": \"'saffron, n. — ME. saffron, fr. OF. (= F.) safran'; 'safranine, n. — F., formed with chem. suff. -ine fr. safran, \\\"saffron\\\"'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt line 520 (≈ printed p. 2155)\", \"stance\": \"supports\", \"note\": \"'saf'ra-nin ... [< F safran (see SAFFRON) ...]'.\"},\n            {\"src\": \"etymonline\", \"where\": \"etymonline.com/word/saffron\", \"stance\": \"supports\", \"note\": \"'c.1200, from Old French safran, from Medieval Latin safranum'; colour sense late 14c.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"safrâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic صَفْرَاء (ṣafrāʔ) is the feminine of the colour adjective أَصْفَر (ʔaṣfar) 'yellow' on the aflaʿ/faʿlāʔ colour pattern, and is used substantivally for 'bile, yellow gall' — the yellow humour of Galenic medicine, one of the four اخلاط. The step root ṣ-f-r → aṣfar/ṣafrāʔ is plain Arabic morphology, and the semantic move 'the yellow (one)' → 'yellow bile' is the ordinary substantivisation of a colour adjective. Wiktionary gives both senses under one entry, with مِرَّة as the synonym for the bile sense.\",\n          \"derivation_fa\": \"«صَفْراء» مؤنثِ صفت رنگِ «أَصْفَر» (زرد) بر وزن أفعل/فَعلاء است و در کاربرد اسمی به معنی «صفرا، زردآب» به کار می‌رود؛ یکی از چهار خلط در طب جالینوسی. گذر از ریشهٔ ص‌ف‌ر به أصفر/صفراء صرفِ ساده عربی است و تحول معنایی «آنِ زرد» ← «زردآب» همان اسم‌شدنِ معمولِ صفتِ رنگ است. ویکی‌واژه هر دو معنی را ذیل یک مدخل می‌آورد و «مِرّة» را هم‌معنی آن می‌شمارد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%B1%D8%A7%D8%A1\"],\n          \"ref_check\": [\n            {\"ref\": \"FSD:2157\", \"status\": \"partial\", \"note\": \"Funk & Wagnalls vol. IV leaf 9 (≈ pp. 2153-2157) s.v. safflower: '( < OF saflor, < O It saflore, < Ar ʿuṣfur, < ṣafrā, yellow )' — F&W states the Arabic ṣafrā 'yellow' on the page Nourai cites, though it puts ʿuṣfur between it and the Romance forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/صفراء\", \"stance\": \"supports\", \"note\": \"'feminine singular of أَصْفَر (ʔaṣfar)'; noun 'bile', synonym مِرَّة; root ص ف ر.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt lines 33477, 35938\", \"stance\": \"supports\", \"note\": \"'Arab. ṣafrāʾ, fem. of aṣfar, \\\"yellow\\\"' (s.v. safflower); 'rel. to uṣfur, fem. ṣafrāʾ, \\\"yellow\\\"' (s.v. Sophora).\"},\n            {\"src\": \"DEV\", \"where\": \"DEV.txt printed p. 200 s.v. Safre\", \"stance\": \"supports\", \"note\": \"'M. Dozy propose de rapprocher zafre de l'arabe صفر ṣofr, cuivre jaune (ṣofra, couleur jaune)'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"safrâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian صفرا (safrā), also written صفراء in learned/medical orthography, is the Arabic ṣafrāʔ borrowed wholesale as the technical term for yellow bile in Perso-Islamic humoural medicine (Avicenna's Qānūn and after), alongside سودا (black bile), بلغم and دم. The final hamza is regularly dropped in Persian pronunciation (safrā, not safrāʔ), and the word has produced the Persian adjectives صفراوی and the idiom «صفرا بریدن». Both script forms that Nourai prints — صفرا and صفراء — are current in Persian. Wiktionary lists Persian صفرا expressly among the borrowings of Arabic صفراء.\",\n          \"derivation_fa\": \"«صفرا» (و در املای پزشکی و ادبی «صفراء») همان صَفْراء عربی است که یکسره به فارسی وام داده شده و در طب دورهٔ اسلامی نام یکی از چهار خلط است، در کنار سودا و بلغم و دم (قانون ابن‌سینا و پس از آن). همزهٔ پایانی در تلفظ فارسی می‌افتد و واژه صفتِ «صفراوی» و اصطلاح «صفرا بریدن» را ساخته است. هر دو صورتی که نورایی چاپ کرده — صفرا و صفراء — در فارسی رایج است. ویکی‌واژه فارسیِ «صفرا» را صریحاً در فهرست وام‌های صَفْراء عربی آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%B1%D8%A7%D8%A1\"],\n          \"ref_check\": [\n            {\"ref\": \"FVA:232\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi has no digital copy (refs_online.json: searched archive.org, ketabnak, noorlib, web) and no local file; p. 232 is unreadable here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/صفراء\", \"stance\": \"supports\", \"note\": \"borrowings listed: 'Persian صفرا, Turkish safra, Spanish zafra, Swahili safura'.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 6680, 15813, 22339 (grep صفرا)\", \"stance\": \"supports\", \"note\": \"Mo'in's 2-vol abridgement uses صفرا / صفراوی throughout in the medical sense ('مفرق و زیادکنندهٔ ترشحات صفرا', 'کیسهٔ صفراوی'), confirming the Persian word and sense; the 6-vol page cannot be mapped.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep صفرا\", \"stance\": \"silent\", \"note\": \"no entry — Aryanpur covers only Indo-European material.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Italian\",\n          \"words\": \"saf-fior\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Old Italian word is saffiore (also zaffiore, saflore) 'safflower, Carthamus tinctorius'. Klein — the reference Nourai cites — analyses it exactly as the chart does: 'It. saffiore, which is prob. a hybrid compounded of Arab. ṣafrāʾ, fem. of aṣfar, \\\"yellow\\\", and It. fiore, \\\"flower\\\"'. Modern scholarship keeps the fiore but changes the first element: AHD reads '[from Old Italian saffiore (influenced by Old Italian fiore, flower), from Arabic ʿuṣfur]', Wiktionary 'from Arabic أَصْفَر (ʔaṣfar) \\\"yellow\\\"... influenced by Middle French safran and fleur', and Funk & Wagnalls '< O It saflore, < Ar ʿuṣfur, < ṣafrā, yellow'. ʿuṣfur is the actual Arabic plant-name (the safflower), itself built on the same root ṣ-f-r, so Nourai is in the right root but one step off the attested etymon; his hyphenated 'saf-fior' is an analytical spelling, not an Italian citation form.\",\n          \"derivation_fa\": \"صورت ایتالیایی کهن saffiore (و نیز zaffiore، saflore) به معنی «گلرنگ، Carthamus tinctorius» است. کلاین — همان منبعی که نورایی به آن ارجاع می‌دهد — آن را دقیقاً مانند نمودار تحلیل می‌کند: «ترکیبی دورگه از صَفراء عربی و fiore ایتالیایی». اما پژوهش امروزی جزء نخست را عوض کرده است: AHD می‌نویسد «از ایتالیایی کهن saffiore (با اثرپذیری از fiore «گل») از عربی عُصفُر»، و ویکی‌واژه و فانک‌ووگنالز نیز عُصفُر را می‌آورند. «عُصفُر» خودْ نام عربیِ همین گیاه است و از همان ریشهٔ ص‌ف‌ر ساخته شده؛ پس نورایی ریشه را درست گرفته اما یک گام از صورت گواهی‌شده فاصله دارد. نگارشِ «saf-fior» هم تحلیلِ خودِ اوست نه صورت ضبط‌شدهٔ ایتالیایی. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/safflower\",\n            \"https://www.ahdictionary.com/word/search.html?q=safflower\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1372\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 33477: 'safflower, n. — Either fr. Du. saffloer, or directly from OF. saflor, fr. earlier It. saffiore, which is prob. a hybrid compounded of Arab. ṣafrāʾ, fem. of aṣfar, \\\"yellow\\\", and It. fiore, \\\"flower\\\".' Note Klein's own 'prob.'.\"},\n            {\"ref\": \"AHD:1142\", \"status\": \"contradicts\", \"note\": \"The current AHD entry reads '[Middle English saflour, from Old French safleur, from Old Italian saffiore (influenced by Old Italian fiore, flower), from Arabic ʿuṣfur.]' — Arabic ʿuṣfur, not ṣafrāʾ, is the etymon; fiore is only an influence.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 33477\", \"stance\": \"supports\", \"note\": \"as quoted above.\"},\n            {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. safflower\", \"stance\": \"contradicts\", \"note\": \"'from Old Italian saffiore (influenced by Old Italian fiore, flower), from Arabic ʿuṣfur'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt line 481 (≈ printed p. 2153)\", \"stance\": \"contradicts\", \"note\": \"'( < OF saflor, < O It saflore, < Ar ʿuṣfur, < ṣafrā, yellow )' — same root, but ʿuṣfur as the immediate source and no 'flower' element.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/safflower\", \"stance\": \"partial\", \"note\": \"'from Middle French safleur; originally from Arabic أَصْفَر (ʔaṣfar, \\\"yellow\\\"), influenced by Middle French safran and fleur'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 2097 s.v. alazor\", \"stance\": \"partial\", \"note\": \"'Sp., fr. Arab. al-uṣfur ... \\\"safflower\\\"' — Klein elsewhere records ʿuṣfur as the Arabic plant-name.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old French\",\n          \"words\": \"saflor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old/Middle French saflor, beside safleur and safflour, is the borrowed Italian saffiore refashioned on French fleur 'flower' — the -fiore ending being reinterpreted, and the whole form additionally attracted to safran. Devic records the forms at first hand: 'On trouve, en vieux français, safleur, saflor' (s.v. Safran, p. 199); Klein cites 'OF. saflor', AHD 'Old French safleur', and F&W 'OF saflor'. The node carries no reference in the book, but the form is independently attested by all four.\",\n          \"derivation_fa\": \"صورت فرانسوی کهن/میانهٔ saflor (و نیز safleur و safflour) همان saffiore ایتالیایی است که پایانهٔ آن به قیاس fleur «گل» بازساخته شده و صورت کلی آن نیز زیر تأثیر safran قرار گرفته است. دِویک این صورت‌ها را دست‌اول ثبت کرده است: «در فرانسوی کهن safleur و saflor دیده می‌شود» (ذیل Safran، ص ۱۹۹)؛ کلاین «OF. saflor»، AHD «safleur» و فانک‌ووگنالز «OF saflor» می‌آورند. نورایی برای این جعبه ارجاعی نداده، اما صورت را هر چهار منبع گواهی می‌کنند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/safflower\",\n            \"https://www.ahdictionary.com/word/search.html?q=safflower\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is printed on this box; the neighbouring boxes' KLN:1372 / AHD:1142 cover the step and both give the Old French form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"DEV\", \"where\": \"DEV.txt printed p. 199 s.v. Safran\", \"stance\": \"supports\", \"note\": \"'On trouve, en vieux français, safleur, saflor.'\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 33477\", \"stance\": \"supports\", \"note\": \"'or directly from OF. saflor, fr. earlier It. saffiore'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt line 481\", \"stance\": \"supports\", \"note\": \"'( < OF saflor, < O It saflore ... )'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"safflower\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English safflower (Middle English saflour) is the Old French saflor/safleur with its opaque second syllable remade by folk etymology into the familiar English 'flower' — a textbook case, since the plant really is grown for its orange flowers, whose dye gave the 'red tape' of English legal bundles. Klein allows either a direct French route or transmission through Dutch saffloer; AHD takes it straight from Old French safleur through Middle English saflour. The gloss on the chart, 'a plant with orange flowers', matches Carthamus tinctorius exactly.\",\n          \"derivation_fa\": \"«safflower» انگلیسی (انگلیسی میانه saflour) همان saflor/safleur فرانسوی کهن است که هجای دوم مبهم آن به ریشه‌شناسی عامیانه به واژهٔ آشنای flower «گل» بدل شده — نمونه‌ای کلاسیک، چون خودِ گیاه را برای گل‌های نارنجی‌اش می‌کارند و رنگ همان گل‌ها بود که نوار سرخِ پرونده‌های حقوقی انگلستان را رنگ می‌کرد. کلاین هم راه مستقیم فرانسوی و هم گذر از هلندی saffloer را ممکن می‌داند؛ AHD آن را یکراست از safleur فرانسوی کهن از راه انگلیسی میانهٔ saflour می‌گیرد. معنایی که نمودار می‌دهد («گیاهی با گل‌های نارنجی») دقیقاً بر Carthamus tinctorius منطبق است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/safflower\",\n            \"https://www.ahdictionary.com/word/search.html?q=safflower\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"'[Middle English saflour, from Old French safleur, from Old Italian saffiore (influenced by Old Italian fiore, flower), from Arabic ʿuṣfur.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 33477\", \"stance\": \"supports\", \"note\": \"'Either fr. Du. saffloer, or directly from OF. saflor'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt line 481 (≈ printed p. 2153)\", \"stance\": \"supports\", \"note\": \"full entry for safflower, Carthamus tinctorius, 'with spiny heads of orange-red flowers ... for the dye obtained from its flowers', etymology '( < OF saflor ... )'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/safflower\", \"stance\": \"supports\", \"note\": \"'from Middle French safleur ... influenced by Middle French safran and fleur'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Šfšyr, Šypšyr, Šamšěr\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Middle Persian šamšēr (Pahlavi ⟨šmšyl⟩), variant šafšēr (⟨špšyl⟩, Manichaean ⟨šfšyr / šypšyr⟩) 'sword'; Parthian safsēr\",\n      \"note\": \"All three forms in the root box are real and correctly labelled. MacKenzie's Concise Pahlavi Dictionary gives both 'šamšēr [smsyl | N ~] sword' and 'šafšēr [špšyl] = šamšēr'; Nyberg's glossary has 'šamšēr [šmšyl] sword 6.7, 21.18 etc. — NP šamšēr; cf. also šifšēr'; Wiktionary reconstructs Middle Persian šmšyl/špšyl with a Manichaean spelling šafšēr and a Parthian cognate safsēr. Nourai's two odd-looking spellings ⟨Šfšyr⟩ and ⟨Šypšyr⟩ are not misreadings: they are the consonantal transliterations of the Manichaean-Pahlavi spellings, and they come, letter for letter, from Mo'in's footnote 2 on Borhan-e Qate' p. 1294, which reads 'پهلوی Shamsher ... و در اوراق مانوی (پهلوی) Shfshyr و shypshyr — Henning, A list of Middle Persian..., BSOS., IX, 1, p. 82'. Only the ulterior origin of the Middle Persian word is open: it is not securely Indo-Iranian, it appears in Greek as σαμψήρα already in Josephus (1st c. AD) and in Aramaic/Syriac as sapsērā, and may be a Wanderwort of the ancient Near East.\",\n      \"note_fa\": \"هر سه صورتِ جعبهٔ ریشه واقعی و درست برچسب‌خورده‌اند. مکنزی در «فرهنگ کوچک پهلوی» هم šamšēr ⟨smsyl⟩ «شمشیر» را دارد و هم šafšēr ⟨špšyl⟩ = šamšēr؛ نیبرگ در واژه‌نامهٔ خود می‌نویسد «šamšēr ⟨šmšyl⟩ sword … NP šamšēr؛ نیز نک. šifšēr»؛ ویکی‌واژه صورت‌های فارسی میانهٔ šmšyl/špšyl و املای مانوی šafšēr و هم‌ریشهٔ پارتی safsēr را می‌آورد. دو املای عجیب‌نمای ⟨Šfšyr⟩ و ⟨Šypšyr⟩ نزد نورایی خطای خوانش نیست: نویسه‌گردانی املای پهلویِ مانوی است و حرف‌به‌حرف از حاشیهٔ ۲ معین بر برهان قاطع ص ۱۲۹۴ گرفته شده که می‌نویسد: «پهلوی Shamsher … و در اوراق مانوی (پهلوی) Shfshyr و shypshyr — Henning, A list of Middle Persian…, BSOS., IX, 1, p. 82». تنها نکتهٔ باز، خاستگاه دورترِ این واژهٔ فارسی میانه است: پیوند هندوایرانی آن مسلم نیست، در یونانی از همان سدهٔ یکم میلادی نزد یوسفوس به صورت σαμψήρα دیده می‌شود و در آرامی/سریانی sapsērā؛ چه‌بسا واژه‌ای سرگردان در خاور نزدیک باستان باشد.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B4%DB%8C%D8%B1\"],\n      \"ref_check\": [\n        {\"ref\": \"MPP:88\", \"status\": \"not_checked\", \"note\": \"Henning, 'A List of Middle-Persian and Parthian Words', BSOS IX (1937-39) 79-92, is not on disk (the local MPP.txt is Henning's 'Mitteliranisch', a different work). Indirect confirmation: Mo'in's footnote on BQT p. 1294 cites this very article for Shfshyr/shypshyr but gives p. 82, not 88.\"},\n        {\"ref\": \"BQT:1294\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol. 3, printed p. 1294 = BQT_v3_pages.txt [pdf page 89]: headword شمشیر, with Mo'in's footnote 2 'پهلوی Shamsher ... و در اوراق ماتوی (پهلوی) Shfshyr و shypshyr / Henning, A list of Middle Persian..., BSOS., IX,1.p.82.' — the exact source of Nourai's root box.\"},\n        {\"ref\": \"NYB:186\", \"status\": \"supports\", \"note\": \"Nyberg, Manual of Pahlavi II (Glossary), NYB_vol2_glossary.txt leaf 200 (running head '178' four leaves earlier, so printed p. ~184-186): 'šamšēr [šmšyl] sword 6.7, 21.18 etc. — NP šamšēr; cf. also šifšēr.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"PHD\", \"where\": \"PHD.txt line 579 and line 583\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'šafšēr [špšyl] = šamšēr'; 'šamšēr [smsyl | N ~] sword'; and the English index line 3923 'sword snēh, šamšēr, (šafšēr)'.\"},\n        {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 200\", \"stance\": \"supports\", \"note\": \"'šamšēr [šmšyl] sword ... cf. also šifšēr'; the word also occurs in context at 22.20 and 25.4 ('ka šamšēr frāc zanēd').\"},\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/شمشیر\", \"stance\": \"supports\", \"note\": \"Middle Persian šmšyl /šamšēr/ and špšyl, Manichaean spelling /šafšēr/ 'sword'; Parthian safsēr; borrowings Old Armenian սուսեր, Syriac ܣܦܣܝܪܐ, JBA ספסרא, Ancient Greek σαμψήρα.\"},\n        {\"src\": \"BQT\", \"where\": \"BQT_v3_pages.txt pdf page 89 = printed 1294\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote giving the Pahlavi and Manichaean forms with the Henning reference.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"šamšîr\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian شمشیر (šamšīr) continues Middle Persian šamšēr ⟨šmšyl⟩ directly: the Pahlavi ⟨l⟩ of the historical spelling is simply how MP wrote /r/, and MP ē regularly becomes NP ī (majhūl ē > maʿrūf ī in the classical-to-modern shift), giving šamšēr > šamšīr; the variant stem šafšēr/šifšēr of the Manichaean texts did not survive. Borhan-e Qate' (p. 1294) offers the popular analysis šam-šīr, 'because šam means both the tail and the claw of the lion' — the same etymology Skeat gives ('Lit. lion's claw. — Pers. sham, nail, claw; shīr, lion') — and quotes the punning verse of Asjadī Marvazī that Nourai reproduces: 'چون شاه بگیرد بکف اندر شمشیر / از بیم بیفکند ز کف‌ها شم شیر'. Mo'in's editorial footnote marks this explicitly as 'وجه اشتقاق عامیانه', a folk etymology, and gives the real Pahlavi forms instead — so Nourai's NOTE ('BQT rejects... by SKT:468') is correct in substance, though strictly it is Mo'in the editor, not Borhan's own text, that rejects it. Note also that the verse is a pun on a wholly separate word شم 'claw/tail', not evidence of the compound.\",\n          \"derivation_fa\": \"«شمشیر» فارسی نو بی‌واسطه دنبالهٔ فارسی میانهٔ šamšēr ⟨šmšyl⟩ است: حرف ⟨l⟩ در املای تاریخی پهلوی همان /r/ را می‌نمایاند و «ی مجهول» فارسی میانه (ē) در فارسی نو به «ی معروف» (ī) بدل شده است؛ گونهٔ šafšēr/šifšēr متن‌های مانوی به فارسی نو نرسیده است. برهان قاطع (ص ۱۲۹۴) تحلیل عامیانهٔ «شم‌شیر» را می‌آورد — «چه شم بمعنی دم و ناخن هردو آمده است» — و همان را اسکیت هم تکرار کرده است («تحت‌اللفظ: چنگال شیر»)، همراه با همان بیت جناس‌آمیز عسجدی مروزی که نورایی نقل کرده است: «چون شاه بگیرد بکف اندر شمشیر / از بیم بیفکند ز کف‌ها شم شیر». اما معین در حاشیه صریحاً آن را «وجه اشتقاق عامیانه» می‌خواند و به‌جایش صورت‌های راستین پهلوی را می‌آورد؛ پس یادداشت نورایی در اصلِ مطلب درست است، هرچند در دقت باید گفت ردکننده معینِ مصحح است نه متن برهان. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B4%DB%8C%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1294\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt [pdf page 89] = printed 1294: 'شمشیر ... و وجه تسمیهٔ آن شم شیر است که دم شیر و ناخن شیر باشد چه شم بمعنی دم و ناخن هردو آمده است'; footnote marked 'وجه اشتقاق عامیانه'; footnote 2 'پهلوی Shamsher ... Shfshyr و shypshyr'. The Asjadi verse stands in the footnotes of printed p. 1291 ([pdf page 86]) s.v. شم: 'چون شاه بگیرد بکف اندر شمشیر از بیم بیفکند ز کفها شم شیر — عسجدی مروزی، جهانگیری'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 583\", \"stance\": \"supports\", \"note\": \"'šamšēr [smsyl | N ~] sword' — the '| N ~' notation means the New Persian form is identical, i.e. direct continuation.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 200 (printed ~186)\", \"stance\": \"supports\", \"note\": \"'šamšēr [šmšyl] sword ... — NP šamšēr'.\"},\n            {\"src\": \"BQT\", \"where\": \"printed p. 1294, Mo'in's footnotes\", \"stance\": \"partial\", \"note\": \"Borhan's own text asserts the šam-šīr 'lion's claw/tail' analysis; Mo'in's footnote overrules it as a folk etymology and supplies the Pahlavi forms.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'šamšēr|schamschir'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no article on šamšīr (the only Schwert entries are no. 409 tēγ etc.).\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'šamšēr|schamschir|samser'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien does not treat the word.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/شمشیر\", \"stance\": \"supports\", \"note\": \"Persian شمشیر from Middle Persian šmšyl/šamšēr; descendants Ottoman Turkish şemşir/şimşir, Urdu شمشیر, Italian scimitarra.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"English\",\n          \"words\": \"scimitar, cimetar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English scimitar (1540s), earlier and variously cimeter, cimetar, scymitar, comes from Italian scimitarra or French cimeterre (15th c.), and the Italian word has been derived from Persian šamšīr since at least Devic. Klein states it flatly ('It. scimitarra (whence also F. cimeterre), fr. Pers. shimshir'); Lokotsch (no. 1910) does the same; Wiktionary lists Italian scimitarra among the borrowings of the Persian word. But the derivation is not secure: the OED's verdict, followed by Etymonline, is that Persian šamšīr is 'unsatisfactory as to form' and that no corresponding Turkish word — which the object's history would lead one to expect — is documented. Hobson-Jobson (p. 804) reaches the same position with an ingenious defence and an honest retreat: 'according to Marcel Devic originally from Pers. shamshīr... if we consider the constant clerical confusion in the Middle Ages between c and t, Scimecirra representing shimshir might easily thus become scimetirra. But we cannot prove this to have been the real origin.' Skeat too hedges: 'Prob. from Pers. shimshīr, shamshīr... Rich. Dict. p. 909.' So: the Persian etymology is the standard candidate, but the medial -t-/-tarra of the Italian form remains unexplained.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی scimitar (از دههٔ ۱۵۴۰، با گونه‌های cimeter و cimetar و scymitar) از scimitarra ایتالیایی یا cimeterre فرانسوی (سدهٔ پانزدهم) آمده است، و واژهٔ ایتالیایی را دست‌کم از زمان دِویک از «شمشیر» فارسی گرفته‌اند. کلاین بی‌تردید می‌نویسد «ایتالیایی scimitarra از فارسی shimshir» و لوکوچ (شمارهٔ ۱۹۱۰) نیز همان را می‌گوید و ویکی‌واژه scimitarra را در فهرست وام‌های واژهٔ فارسی آورده است. اما این ریشه‌یابی قطعی نیست: داوری فرهنگ آکسفورد — که اتیمانلاین هم تکرارش می‌کند — این است که «شمشیر» از نظر صورت رضایت‌بخش نیست و هیچ واژهٔ ترکیِ متناظری که تاریخِ خودِ سلاح انتظارش را برمی‌انگیزد گواهی نشده است. «هابسن‌ـ‌جابسن» (ص ۸۰۴) با دفاعی هوشمندانه و عقب‌نشینی‌ای صادقانه به همین‌جا می‌رسد: «به گفتهٔ مارسل دِویک در اصل از فارسی shamshīr… اگر درهم‌آمیزی همیشگی c و t در دست‌نویس‌های سده‌های میانه را در نظر بگیریم، *Scimecirra به‌آسانی scimetirra می‌شود؛ اما نمی‌توانیم ثابت کنیم که خاستگاه واقعی همین بوده است». اسکیت نیز با «احتمالاً» سخن می‌گوید. پس: با احتیاط پذیرفتنی است؛ -t- میانیِ صورت ایتالیایی همچنان بی‌توضیح مانده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/scimitar\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D9%85%D8%B4%DB%8C%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1397\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 34071 (leaf 742): 'scimitar, n., a curved Oriental sword. — It. scimitarra (whence also F. cimeterre), fr. Pers. shimshir, \\\"scimitar, saber\\\".' (No page numerals in the scan; by leaf arithmetic this falls near p. 1460, so Nourai's 1397 probably follows a different printing.)\"},\n            {\"ref\": \"SKT:468\", \"status\": \"supports\", \"note\": \"SKT.txt line 16640 (leaf 444): 'Scimetar, Cimetar. (F. or Ital. — Pers.?) F. cimeterre, \\\"a scymitar\\\"; Cot. Cf. Ital. scimitarra ... Prob. from Pers. shimshīr, shamshīr, \\\"a cimeter.\\\" Rich. Dict. p. 909. Lit. lion's claw. — Pers. sham, nail, claw; shīr, lion.' This is exactly the 'lion's claw' derivation that Nourai's NOTE says BQT rejects. (Skeat's page numerals are not in the scan; by leaf arithmetic ≈ p. 424 in the 1911 Concise, so 468 is probably another printing.)\"},\n            {\"ref\": \"HJB:804\", \"status\": \"partial\", \"note\": \"Hobson-Jobson s.v. SCYMITAR, HJB.txt leaf 848 (printed ≈ 804): 'We get it through the French cimeterre, Ital. scimeterra, and according to Marcel Devic originally from Pers. shamshīr (chimchir as he writes it). This would be still very obscure unless we consider the constant clerical confusion in the Middle Ages between c and t... But we cannot prove this to have been the real origin.' Supports the route but declines to affirm it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 34071\", \"stance\": \"supports\", \"note\": \"'It. scimitarra ... fr. Pers. shimshir'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 16640\", \"stance\": \"partial\", \"note\": \"'Prob. from Pers. shimshīr... Lit. lion's claw' — right source language, wrong (folk) internal analysis.\"},\n            {\"src\": \"HJB\", \"where\": \"HJB.txt leaf 848, printed p. ~804\", \"stance\": \"partial\", \"note\": \"quotes σαμψηρά in Josephus (Antiqq. xx.ii.3, AD 93) and in Suidas, and Herbert 1630 'swords (shamshaers they call them) form'd like a cresent'; but 'we cannot prove this to have been the real origin'.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entry 1910\", \"stance\": \"supports\", \"note\": \"'Pers. šimšīr: \\\"Schwert\\\"; hieraus it. scimitarra, frz. cimeterre, cimiterre, sp. pg. cimitarra, engl. scymitar, cimetar.'\"},\n            {\"src\": \"etymonline\", \"where\": \"etymonline.com/word/scimitar\", \"stance\": \"partial\", \"note\": \"'1540s, from French cimeterre or Italian scimitarra. Origin unknown. Turkish would be the expected source, but no such word has been found there. Perhaps from Persian shimshir, but this is unsatisfactory as to form.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-449.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 449"
}
```


### [2026-09-14T02:13:16.916Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 3, 'disputed': 1}
root verdicts: {'plausible': 1, 'confirmed': 2}
ref checks: {'supports': 13, 'not_checked': 4, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 36, 'silent': 7, 'contradicts': 7, 'partial': 13} | by book: {'KLN': 11, 'Wiktionary': 7, 'DEV': 6, 'AHD': 5, 'MON': 4, 'FSD': 4, 'LAM': 3, 'SKT': 3, 'LKT': 3, 'ARY': 2, 'PLA': 2, 'etymonline': 2, 'PHN': 1, 'DOZ': 1, 'WEB': 1, 'AFM': 1, 'AND': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'HRN': 1, 'HUB': 1, 'HJB': 1}
```


## [2026-09-14T02:13:37.447Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-449.json` written, valid JSON, `verify_check.py 449` shows 17/17 nodes and **0 PROBLEM lines**.

**Page 449 (book p. 419) — 3 entries, 17 nodes**
- Node verdicts: confirmed 13, plausible 3, disputed 1. Root verdicts: confirmed 2, plausible 1.
- Ref checks: supports 13, partial 4, contradicts 1, not_checked 4 (FVA — no copy exists anywhere; PRT — lending-only; MPP — the BSOS article isn't on disk; plus two boxes printed with no ref).

**disputed**
- *S.f.r → Arabic za'farân* (saffron): AHD "from Arabic zaʿfarān; akin to Akkadian azupīru, **of unknown origin**"; Etymonline same; Wiktionary offers Aramaic ṣpr / internal Arabic / Middle Iranian. ز + ع cannot be squared with ص-ف-ر. Nourai's own NOTE citing Asbaghi PLA:145 (read on the page) actually derives it from Persian *zar-parān* — the opposite direction from his arrow. The two CEL6 claims in the NOTE are worthless (IE \*kes- "hair" is phonetically impossible; "imported from Kashmir in the 9–10th c." is refuted by pre-Islamic attestation and Akkadian azupīru).

**plausible (worth flagging)**
- Root *Š.f.f* labelled [Semitic] — Klein, his own source, calls it Arabic only; no Semitic cognate found.
- *French chiffe ← Arabic šiff*: real scholarly position (Defrémery/Devic p.94–95/Lammens/Klein) but AHD and Etymonline prefer OF *chipe* < ME *chip*.
- *Italian "saf-fior" ← ṣafrā' + fiore*: Klein supports, but AHD/F&W/Wiktionary make it Old Italian *saffiore* ← Arabic **ʿuṣfur** (same root, one step off); "saf-fior" is Nourai's analytic spelling, not an Italian citation form.
- *English scimitar*: OED/Etymonline call Persian šamšīr "unsatisfactory as to form"; Hobson-Jobson p.804 (verified) ends "we cannot prove this to have been the real origin".

**No extraction errors.** I rendered PDF p. 449 and checked it against the JSON: everything matches, including Old French "safron" (an attested Anglo-Norman variant — AND lists *safron*/*safroun*), so no transcription flag. Best find: Nourai's odd root box ⟨Šfšyr, Šypšyr⟩ is taken verbatim from Mo'in's footnote 2 on Borhan-e Qate' **p. 1294** (located in BQT_v3 pdf p. 89), which cites Henning BSOS IX p. **82** (not Nourai's MPP:88) and labels the "šam-šīr = lion's claw" story **وجه اشتقاق عامیانه** — confirming Nourai's NOTE, with the nuance that it is Mo'in the editor, not Borhan's text, doing the rejecting. Page image archived to `data/verification/sources/refs/ocr/BOOK/449.png`; 15 web pages archived via `fetch_source.py`.
