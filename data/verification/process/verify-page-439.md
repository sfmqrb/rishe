# Verification process log — verify-page-439


## [2026-09-14T01:55:40.259Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 439 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-439.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-439.json. Write /home/sfmqrb/git/rishe/data/verification/page-439.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 439` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:41.445Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:55:42.424Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:42.445Z] TOOL RESULT

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


## [2026-09-14T01:55:42.921Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-439.txt"
}
```


### [2026-09-14T01:55:42.947Z] TOOL RESULT

```
1	=== PDF page 439 (book page 409) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sek : to cut, scrape, separate, tear, etc.  (refs AHD; POK:920,926,930,931,941; IEC:640,1155)  PART 2
4	#1 (parent #0) [Avestan] refs=POK:926 | xerpta : cut, shaped ; hu-xerpta, hu-kehrpta : shaped like a boar, pig ☞Su 2
5	  #2 (parent #1) [Persian] refs=BQT:794 | xŭk «خوک» : "boar-shaped animal", pig
6	#3 (parent #0) [Persian] refs=IEC:640; MON:1982 | sîlî «سیلی» : slap, blow
7	#4 (parent #0) [Germanic] refs=AHD | skith : a cut branch or piece of wood used for walking on snow, snow ski
8	  #5 (parent #4) [French] refs=None | ski
9	    #6 (parent #5) [Persian] refs=MON:272 | eskî «اسکی» : ski
10	  #7 (parent #4) [English] refs=AHD | ski
11	#8 (parent #0) [Latin] refs=AHD | crî-bellâre : to sieve, separate
12	  #9 (parent #8) [Arabic] refs=AHD:543 | ğarbala : a sieve
13	    #10 (parent #9) [Persian] refs=MON:2397 | ğarbâl «غربال ( غربیل )» : a sieve
14	#11 (parent #0) [Germanic] refs=AHD |  | NOTE: words meaning to cut, shape, peel or skin, etc.
15	  #12 (parent #11) [English] refs=AHD | shelf, half, shape, shave, skin, skirt, saw, scrap, sharp, shirt, shears, score, short
16	#13 (parent #0) [Latin] refs=AHD | scîre : to know, distinguish
17	  #14 (parent #13) [English] refs=AHD | science, conscience, nice
18	#15 (parent #0) [Latin] refs=AHD | carô : flesh ; carni-levare : reduce flesh, a festivity before fasting, carnival ☞Legwh
19	  #16 (parent #15) [French] refs=AHD | carnaval
20	    #17 (parent #16) [Persian] refs=VOP:269 | kârnâvâl «کارناوال» : carnival
21	  #18 (parent #15) [English] refs=AHD | carnival, carnivorous
22	#19 (parent #0) [Indo-European] refs=IEC:1155 | Skěl : division, part, thought
23	  #20 (parent #19) [Old Iranian] refs=FFD:61 | kar 3, kâr 3 : to think ; us-kâr-a : to think
24	    #21 (parent #20) [Pahlavi] refs=FFD:61 | uskâr, uskârd : thought
25	      #22 (parent #21) [Persian] refs=FFD:61; MON:1903 | segâl «سیگال ( سیکال )» : thought, (a bad) idea | extra: سگالیدن ، سگالش
26	--- entry 1 ---
27	ROOT Seks -> redirect to Sweks
28	
```


## [2026-09-14T01:55:43.897Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-14T01:55:45.251Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-439.json",
 "description": "Read page 439 source JSON"
}
```


### [2026-09-14T01:55:45.308Z] TOOL RESULT

```
{
  "pdf_page": 439,
  "book_page": 409,
  "entries": [
    {
      "root": {
        "name": "Sek",
        "lang": "Indo-European",
        "refs": "AHD; POK:920,926,930,931,941; IEC:640,1155",
        "gloss": "to cut, scrape, separate, tear, etc.",
        "note": "Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:926",
          "words": [
            {"translit": "xerpta", "gloss": "cut, shaped", "script": null},
            {"translit": "hu-xerpta, hu-kehrpta", "gloss": "shaped like a boar, pig", "script": null, "see": ["Su 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:794",
          "words": [
            {"translit": "xŭk", "gloss": "\"boar-shaped animal\", pig", "script": "خوک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:640; MON:1982",
          "words": [
            {"translit": "sîlî", "gloss": "slap, blow", "script": "سیلی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "skith", "gloss": "a cut branch or piece of wood used for walking on snow, snow ski", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "ski", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:272",
          "words": [
            {"translit": "eskî", "gloss": "ski", "script": "اسکی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ski", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "crî-bellâre", "gloss": "to sieve, separate", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Arabic",
          "refs": "AHD:543",
          "words": [
            {"translit": "ğarbala", "gloss": "a sieve", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:2397",
          "words": [
            {"translit": "ğarbâl", "gloss": "a sieve", "script": "غربال ( غربیل )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": "words meaning to cut, shape, peel or skin, etc.",
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "shelf, half, shape, shave, skin, skirt, saw, scrap, sharp, shirt, shears, score, short", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "scîre", "gloss": "to know, distinguish", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "science, conscience, nice", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "carô", "gloss": "flesh", "script": null},
            {"translit": "carni-levare", "gloss": "reduce flesh, a festivity before fasting, carnival", "script": null, "see": ["Legwh"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "carnaval", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "VOP:269",
          "words": [
            {"translit": "kârnâvâl", "gloss": "carnival", "script": "کارناوال"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "carnival, carnivorous", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:1155",
          "words": [
            {"translit": "Skěl", "gloss": "division, part, thought", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Old Iranian",
          "refs": "FFD:61",
          "words": [
            {"translit": "kar 3, kâr 3", "gloss": "to think", "script": null},
            {"translit": "us-kâr-a", "gloss": "to think", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Pahlavi",
          "refs": "FFD:61",
          "words": [
            {"translit": "uskâr, uskârd", "gloss": "thought", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "Persian",
          "refs": "FFD:61; MON:1903",
          "words": [
            {"translit": "segâl", "gloss": "thought, (a bad) idea", "script": "سیگال ( سیکال )"}
          ],
          "script_extra": "سگالیدن ، سگالش",
          "note": null,
          "quote": {"text": "باخود غزلی همی سگالید - که نوحه نمود و گاه نالید", "poet": "Nezâmî Ganjavî"}
        }
      ]
    },
    {
      "root": {"name": "Seks", "redirect": "Sweks"},
      "nodes": []
    }
  ]
}
```


## [2026-09-14T01:55:47.584Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','POK','IEC','BQT','MON','FFD','VOP','WLD','HRN','HUB','PHD','NYB','KLN','SYN','BRT','CHEUNG','ARY','AFM','PLA','SKT','FSD','WEB','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T01:55:48.667Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-14T01:56:22.512Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:56:22.578Z] TOOL RESULT

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


## [2026-09-14T01:56:23.015Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -100"
}
```


### [2026-09-14T01:56:23.221Z] TOOL RESULT

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


## [2026-09-14T01:56:26.760Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^sek-\\|^skei-\\|^sker-\\|^skel-\\|^krei-\\|^kerp-\\|^kar-\" AHD_watkins1985.txt | head -40; echo ---; grep -n \"sek-\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:56:26.828Z] TOOL RESULT

```
584:kar-2, To praise loudly, extol. Hypothetical base form. 1. Perhaps Germanic *hrém- in Dutch roemen, to praise: RUMMER. 2. Lengthened-grade form *kdru- in Greek (Doric) karux, (Attic) kérux, herald: capucEvs. [Pok. 2. kar- 530.]
911:sek-
933:skei-
935:skel-'
937:sker-'
939:sker-2
---
```


## [2026-09-14T01:56:27.881Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cribell\\|ghurbal\\|gharbal\\|garbal\" AHD_watkins1985.txt KLN_1966.txt KLN_1971.txt LKT.txt | head -30"
}
```


### [2026-09-14T01:56:27.964Z] TOOL RESULT

```
LKT.txt:7427:earuba  832 carumba  832 Castrum  1117 cavilla  980 census  1050 centenarius  1178 cephalica  (vena)  1172 cer  Villa  1095 ciccum  434 cimiabaris  1827 cintra  1057 commercium  751 cophinus  1225 cribellum  673 cromm  1247 cummum  1046 cuppa  1225 cnpresstis  727 ci/c^as  1794.  1905 cywa  445 t«/^oZa  442
KLN_1971.txt:59871:cribellum, ‘a small sieve’, dimin. of cribrum. See 
KLN_1966.txt:9668:cribble,  n.,  a  coarse  sieve.  —  F.  crible,  fr.  Late  L. cribellum,  ‘a  small  sieve’,  dimin.  of  cribrum.  See next  word.
KLN_1966.txt:15792:Derivative:  garbage,  intr.  v. garble,  tr.  v.,  to  select  improperly;  to  misquote. —  OF.  garbeiler,  grabeller,  ‘to  garble  spices, to  sift’,  fr.  Sp.  garbillar,  ‘to  garble,  sift’,  fr. Arab,  gharbala,  ‘he  sifted’,  fr.  ghirbdl,  sieve  , ult.  fr.  Late  L.  cribellum,  dimin.  of  L.  cribrum, ‘sieve’,  which  is  rel.  to  cernere,  ‘to  distinguish, separate,  sift’.  See  cribriform.
```


## [2026-09-14T01:56:30.928Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '905,945p' AHD_watkins1985.txt"
}
```


### [2026-09-14T01:56:30.990Z] TOOL RESULT

```
<persisted-output>
Output too large (37.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b3yytld5b.txt

Preview (first 2KB):
sawel-. Also s(u)wel-, su(a)el-, su(@)en-, sun-. The sun. Contracted from *saswel-. 1. Variant forms *swen-, *sun- in: a. Germanic *sunndn- in Old English sunne, sun: SUN; b. Germanic compound *sunn6én-dagaz, “day of the sun” (translation of Latin diés sdlis), in Old English sunnandeg, Sunday: SUNDAY; c. Germanic de- rivative *sunthaz, “sun-side,” south, in Old English sith, south, and sitherne, southern: SOUTH, SOUTHERN. 2. Variant form *s(2)wol- in: a. Latin sd/, the sun: soL’, SOL, SOLAR, SOLARIUM; GIRASOL, INSOLATE, PARASOL, SOLANINE, TURNSOLE; b. Latin compound sdlstitium, “a standing of the sun,” solstice (-stitium, a standing; see sta-): SOLSTICE. 3. Suffixed form *sdwel-yo- in Greek hélios, sun: HELIACAL, HELIO-, HELIOS, HELIUM; ANTHE- LION, APHELION, ISOHEL, PARHELION, PERIHELION. [Pok. sdwel- 881.]
s6-1, To sow. Contracted from *sea-. 1. Germanic *séan in Old English séwan, to sow: sow!. 2. Suffixed form *sé-ti-, sowing, in Germanic “sédiz, seed, in: a. Old English s&d, seed: sEED; b. Middle Dutch saet and Middle Low German sdt, seed: couza. 3. Reduplicated zero-grade form “si-s()- in Latin serere, to sow: SEASON; INSERT. 4. Suffixed form *sé-men-, seed, in Latin sémen, seed: SEME, SEMEN, SEMINARY, SEMINATION; DISSEMI- NATE. [In Pok. 2. sé(i)- 889.]
s@-2, Long, late. Contracted from *sea-. Variant *seoi-, zero-grade form *sia-, contracted to *si-. 1. Suffixed form sé-ro- in: a. Latin sérus, late: SEROTINOUS, SOIREE; b. Middle Breton Air, long: MENHIR. 2. Possibly Ger- manic *si- in: a. Germanic *sid6, “long surface or part,” in Old English side, side: stDE; b. Germanic ‘sith, “later,” after, in Old English siththon, siththan, after that, since: SINCE, SITH. [In Pok. 2. sé(i)- 891.]
s@-3, To sift. Contracted from *sea-. Suffixed form *sé-dho- in Greek éthein, to sift: ETHMOID. [Pok. 1. sé(i)- 889.]
...
</persisted-output>
```


## [2026-09-14T01:56:34.028Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 911 933 935 937 939; do echo \"=== line $n ===\"; sed -n \"${n}p\" AHD_watkins1985.txt | head -c 3000; echo; done"
}
```


### [2026-09-14T01:56:35.169Z] TOOL RESULT

```
=== line 911 ===
sek-

=== line 933 ===
skei-

=== line 935 ===
skel-'

=== line 937 ===
sker-'

=== line 939 ===
sker-2
```


## [2026-09-14T01:56:37.202Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 911 933 935 937 939 941; do echo \"=== $n ===\"; sed -n \"$((n)),$((n+1))p\" AHD_watkins1985.txt | head -c 2500; echo; done"
}
```


### [2026-09-14T01:56:38.325Z] TOOL RESULT

```
=== 911 ===
sek-
grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thin
=== 933 ===
skei-
*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian
=== 935 ===
skel-'
form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCU
=== 937 ===
sker-'
skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic sou
=== 939 ===
sker-2
*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kor
=== 941 ===
skeup-
leaves): CRAMBO. 4. Perhaps Celtic *krumb-i- in Welsh crwn, crooked, arched: CROMLECH. [Pok. (s)kerb(h)- 948.] skét(e)-. To injure. Suffixed zero-grade form *skoat-on- in Germanic *skathén- in: a. Old Norse skadha, to harm: SCATHE; b. Old High German scado (> German Scha- den), harm, injury, damage: SCHADENFREUDE. [Pok. skéth- 950.]
```


## [2026-09-14T01:56:47.730Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"sek-[.,][^[]\\{0,1200\\}\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -5; echo \"=== skel2/saw ===\"; grep -o \"SAW[^ ]\\{0,3\\}\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:56:49.167Z] TOOL RESULT

```
sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.]
sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.]
=== skel2/saw ===
SAW.
SAW!
```


## [2026-09-14T01:56:51.271Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"sek-\\?[!1]\\?\\. To cut[^[]\\{0,2000\\}\\[[^]]*\\]\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-14T01:56:52.492Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:56:54.637Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SICKLE\\|Pok. 2. sek- 895\\|sek- 895\" AHD_watkins1985.txt | head; echo ===; grep -o \".\\{200\\}SICKLE.\\{600\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-14T01:56:54.701Z] TOOL RESULT

```
Exit code 1
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
(eval):1: == not found
```


## [2026-09-14T01:57:00.426Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l POK_full.txt POK_01.txt POK_02.txt POK_03.txt && head -40 POK_full.txt"
}
```


### [2026-09-14T01:57:00.477Z] TOOL RESULT

```
  93771 POK_full.txt
   5151 POK_01.txt
   6715 POK_02.txt
   5974 POK_03.txt
 111611 total
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
```


## [2026-09-14T01:57:02.408Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page in Pokorny\\|Seite in Pokorny\" POK_full.txt | head -3; echo ===; grep -n \"926\" POK_full.txt | grep -i \"pok\" | head -5"
}
```


### [2026-09-14T01:57:02.478Z] TOOL RESULT

```
Exit code 1
11553:Page in Pokorny: 125 
14713:Page in Pokorny: 160 
(eval):1: == not found
```


## [2026-09-14T01:57:04.421Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page in Pokorny: 92[0-9] \\|Page in Pokorny: 93[0-9] \\|Page in Pokorny: 94[0-1] \" POK_full.txt | head -40"
}
```


### [2026-09-14T01:57:04.493Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:06.162Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page in Pokorny\" POK_full.txt | tail -5; echo ===; grep -c \"Page in Pokorny\" POK_full.txt"
}
```


### [2026-09-14T01:57:06.266Z] TOOL RESULT

```
11553:Page in Pokorny: 125 
14713:Page in Pokorny: 160 
(eval):1: == not found
```


## [2026-09-14T01:57:08.620Z] TOOL CALL #19: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['POK'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T01:57:09.726Z] TOOL RESULT

```
{
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
}
```


## [2026-09-14T01:57:11.604Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 92[0-9]\\|Page(s): 93[0-2]\\|Page(s): 94[01]\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:57:11.724Z] TOOL RESULT

```
75121:Page(s): 922-923 
75320:Page(s): 923-927 
75347:Page(s): 927 
75378:Page(s): 927 
75440:Page(s): 928 
75455:Page(s): 930 
75493:Page(s): 929-930 
75527:Page(s): 930 
75542:Page(s): 930 
76964:Page(s): 922 
77326:Page(s): 930-933 
77545:Page(s): 929 
77777:Page(s): 929 
77801:Page(s): 929 
77873:Page(s): 928
```


## [2026-09-14T01:57:14.258Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 75121 75320 75347 75440 75455 75493 77326; do echo \"=== $L ===\"; sed -n \"$((L-12)),$((L))p\" POK_full.txt | tr '\\n' ' ' | head -c 700; echo; done"
}
```


### [2026-09-14T01:57:15.364Z] TOOL RESULT

```
=== 75121 ===
', Old English sceacan^ shake (engl. shake); hurry, go away, pass over, flee'; Old Saxon  skakan siexw V. 'go away, pass over, escape, flee' (Low German schacken^ shake, move  '), Old High German unt-scachdndes^i\\}cWyaQ\'\ Old High German scahhom. ' foreland,  promontory ', Middle High German schachexu. ' StiJckeinzelstehenden Waldes ', Modern  High German Bavarian Swiss Schachen ds., Old Icelandic s/reA/// 'Landzunge'.   doubtful is affiliation from Old Frisian skakm. 'booty, robbery ', Old High German scach  m. ' burglary, theft, robbery ', Old English sceacere. Old High German scahhah^ robber'.  Modern High German Schacher^ haggler, bargainer, wrangler, peddler, merchant '  (actually, ' 
=== 75320 ===
"auseinanderflieften'; Lithuanian s/r/a/io'^5 "zerstreuf, Latvian sk/a/d/s ^ e\r\ Herumtreiber,  good for nothing, useless person'; without aniaut. s-: klaMt^s\c\\ herumtreiben', kli'stu,  klfdu, k/fst'err', Lithuanian klystu, klydau, klysti^s\ch verirren' (without d. Lithuanian klajdju,  -otr wander', Latvian klaijat, -udt6s. eineoriginally versch. family?); Old Prussian sc/a/f,  schlait, schk/a/t' but; without', schklaitsMv. "sonderlich, particularly, specially, especially,  particular: in particular, peculiarly, separately, extra, notably; otherwise ', Adj.  "unsophisticated, simple, just';   Old English 5//7&/7"spleiR)en', engl. slive. Old English /c-s/^/&/7 "split'. Middle Low  German s
=== 75347 ===
 Old Lithuanian ske/u ar\d Lithuanian skeliu, -e//"schuldig sein', skylu, {*sk/7u), s/r////"in  Schulden geraten', s/ro/a "blame'; Old Prussian 5/re//5/7/s "culpable', ablaut. skallTsnant  Akk. " obligation ', poskuITt {paskollet} "ermahnen';   without 5-.' Lithuanian /ra/Ze "blame', /ra/Zas "culpable'.   References: WP. II 596, Trautmann 264 f.;     See also: compare (s)kel-47  Page(s): 927  
=== 75440 ===
haunch' (with /r-insertion: kulksis, kulksn/s ^ank\e, Sprunggelenk'), Old Prussian culczr\r\\p,  haunch'; with -/r-suffix: Lithuanian kulnasm., kuln/st "hack, mattock, hoe, calcaneus '  {*kulk-n-), proto Slavic. *kulkai. "hip, haunch' in spatChurch Slavic A/b/ra"poples', bg.  /rb7/ra"hip, haunch, thigh' (/5-/rb/cb"verrenke'); Serbo-Croatian kuk6s. etc.;   Latin ca/v "calcaneus ' {calco, -SAe "tread, stomp', calcltrare^y\o\ev\\. ausschlagen', calcar  " spur', calceus^ shoe ', tarent. kqAtIov ds. from Oscan *calc-tlo-)\ after Trautmann 145  Indo Germanic root nouns *Aro/fr- besides koIR-.     References: WP. II 597 ff., WH. 1144 f., 248, II 492, Trautmann 114, 135 f., 145.  Page(s): 928  
=== 75455 ===
 Meaning: to plunge   Note: only gr. and Baltic   Material: Gr. okivGoc; "untertauchend'; Lithuanian sk^stu, 5/r#5//"untersinken, drown ',   causative skandinu, -dinti^ drown '; Old Prussian auskiendlai^er qo under'.   Maybe alb. {^skendh-) /7eo'/7 'plunge, throw' [common alb. sk- > h-].   References: WP. II 565, Trautmann 265.  Page(s): 930  
=== 75493 ===
skin', ys^e/7/7'Schinnen', Middle Breton quenn^sV\v\\ bret. kennm. "Schinnen', -/re/7 "skin'  in /?^-^e/7"Rindshaut' etc.; bret. (Vannes) sk/gnanlrog' {*skenniano-); Old Icelandic hinna  f. "thin skin. Membrane' {*skend-n-); (under the influence of common Celtic -ns-, -nt- > -nn-   )■     compare with a-vocalism: Middle Irish sca/ndr/m 'zerspa\\.e\ scandrad, scaindred  "dispersion", scainder^Qeiec\\\!.   References: WP. II 563 f.; Loth RC. 41, 405 f.  Page(s): 929-930  
=== 77326 ===
'zeptertragend', OKanoc; kAqSoc; Hes., aKr|TTavr| 'staff, Szepter', hom. OKPinaviov ds. =  Doric OKanaviov Hes.; OKrinTU) 'stijtze, swing, brandish with power ', intr. and med. 'sich  stijtzen; sich with Kraft auf etwas throw', aKr|nT6(; 'sudden niederfahrender whirlwind,  Wetterstrahl, misfortune'; Latin scapus^ shaft, Stiel, stalk, stem', scopai. 'thin twig,  branch, rod', PI. 'Reisigbesen', scopio, -on/sm. 'the Stiel, an dem die Beeren the grape  hangen; stem of Spargels', scopusds.;   Old High German skaft^ shaft, spear, javelin'. Old Saxon skaft'spear, javelin', Dutch  schacht' quill, Lanzenschaft', Old English sceaffm., Old Icelandic skaptn. ' shaft, shaft,  pole, spear, javelin'.   Re
```


## [2026-09-14T01:57:21.094Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.findall(r'Root / lemma:([^\\n]*)[\\s\\S]*?Page\\(s\\):\\s*([0-9\\-]+)',t)\n# need per-block; do splitting\nparts=t.split('Root / lemma:')\nfor p in parts[1:]:\n    lem=p.split('\\n')[0].strip()\n    m=re.search(r'Page\\(s\\):\\s*([0-9]+)',p)\n    mm=re.search(r'Meaning:([^\\n]*)',p)\n    if m:\n        pg=int(m.group(1))\n        if 915<=pg<=945:\n            print(pg, '|', lem, '|', (mm.group(1).strip() if mm else ''))\nEOF"
}
```


### [2026-09-14T01:57:22.379Z] TOOL RESULT

```
915 | seug- | sad, grievous; ill
915 | seua- su- | to let, leave (?)
915 | seuio- | left
915 | se- : reflexive pronoun | to sew
915 | se(i)-3, -sai- : 5/- and sei- : si- : to | 
916 | sArab^- skarrt^- | to support
918 | (s)kand- (s)kend- | shine
916 | (s)kai- (d-), (t-) | shining, bright
922 | (s)kek-, skeg-{* nasaWzeA *(skenk-, *skek-no-) | to spring, move quickly
923 | (s)kel-1 | to cut
927 | (s)kel-2 | to be guilty, to owe
927 | (s)kel-3 | to dry out
930 | skend^- | to plunge
929 | (s)ken-(d-) | to rift; to flay
930 | (s)keng- | lame; slant
930 | (s)kep-1 | to cover
933 | (s)ker-1 | to shrink, wrinkle; dry, thin
933 | (s)ker-2, skera- : skre- | to spring, to turn
935 | (s)ker-3 | to turn, bend
938 | (s)ker-4, (s)kera-, (s)kre- | to cut
922 | skei-b""-, -p- nasalized sk/'-m-b'^- | slant; to limp
919 | skei-\ (to cut, separate) is detrimental for alb. language because | to work with a sharp instrument
917 | (s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t- | to hit, kick
918 | (s)k(h)ed-, (s)k(h)e-n-d- | to crush, scatter
929 | skhel- | to stumble
917 | sRai-, sRai-. sRT-\ to glimmer (of wet things); shadow, derived from | 
919 | sRed- | to cover
929 | (s)Rel- | to spring
929 | (s)Rem- | disabled
928 | (s)k''el-5, (s)kel- | " sound, shout '
```


## [2026-09-14T01:57:36.505Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\ni=t.find('(s)kel-1')\nprint(t[i-200:i+9000])\nEOF"
}
```


### [2026-09-14T01:57:37.744Z] TOOL RESULT

```
 High German Schacher^ haggler, bargainer, wrangler, peddler, merchant ' 
(actually, ' wander, or run with the booty '?). 

References: WP. II 556 f., Trautmann 262. 
Page(s): 922-923 

Root / lemma: (s)kel-1 

Meaning: to cut 

Note: not reliable from kel- 'hit' and kel- 'prick' (above S. 545 f.) to separate. 



Material: Old Indie /ra/a 'small part' (: serb. pro-kola^leW eines gespaltenen Ganzen', das 
at first to Old Church Slavic koljg " prick ' and "split', above S. 546); 

Armenian de//r'e/77 "split, zerschlage'; probably also k'eir rudder, helm ' (meaning as in 
Old English helma, see below); auf ani. sk- (with otherwise nirgends wiederkehrendem 
palatal) wiese ceA//77 "split'; 

gr. GKaAAu) "scharre, hacke, ditch, grub', aKaAi(; "hack, mattock, hoe, Karst'; axaAi(; " 
wooden fork als StiJtze aufgerichteter Jagdnetze' (under influence of axa^w " split, schlitze 
auf, Gxaapa " incision '); GKaAfj6(; "peg, plug, oarlock' (compare thrak. OKaApr), Old High 
German scalm. Old English helma. Upper Serbian colm, Lithuanian kelmas); okuKKlo "flay, 
tear, rend, plage' {*skolid), KO-aKuA-paria "Lederschnitzel, Abfall from leather', okwAoc; 
"Spitzpfahr (compare Lithuanian /r^o/as "picket, pole'; with a Old Church Slavic /ro/b "peg, 
plug' above S. 546); perhaps is also kwAuu) " hamper, hindre' from a *k(I)Aoc; "peg, plug' 
derived ("anpflocken'), the ending -uw after dem begriffl. contrast Auw?; OKoAuGpov " 
footstool ', QKoAuTTTEiv " mutilate, beschneiden' Hes., anooKoAunTU) "kastriere'; auf eine 
meaning "from the skin sich abspaltende scale, husk ' goes back KsAscpoq " leper, outcast, 
one who is rejected by society' (compare Middle English scalle " crust, scab, eschar ', 
nengl. 5C5//(nord. loanword), Swedish s/r5/"skin rash am mouth'); 

thrak. amK\^'^\ "sword, knife' {*skolma)\ 

alb. /75/e" scale, husk, fishbone, splinter, beard the Ahren ' {*skolia= Gothic skaija); 
/7c»/e"thin, fine, tender'; f. "Zartheif {*skel-)\ /7e/"Pfrieme, pricker, awl', /7e/e"Bratspieft, spit, 
pike, lance ' (= aKU)Ao(;); perhaps shtel "offne, make gleaming, sharp, stecke fire an, 
entzijnde' (Lithuanian s/r//// likewise "fire anschlagen'); 

Latin 5///i7i/a"Hulsenfruchtschote' (whereof s/Z/ic/a "foenum graecum, Bockshorn'), diss, 
from *sciliqua, older *sce//qua: 0\6 Church Slavic 5/rc»/6/ra "ostreum'; Latin s/7ex, -/c/s' 
pebble ' diss, from *sc/7ec-o\6er scelic-, compare Middle Irish sce{/)//ec' rock' (ending after 
Old Irish carra/c' rocks'); 

without anI. 5- perhaps here: Latin cu/ter, -//7 "knife' {*kel-tro-s, *kol-tro-s or* M-tros); celtis 
f. "chisel' existiert not, s. Niedermann, Mus. Helv. 2, 123 f.; 

cymr. chwalu^scaVier', corn, scullye, sculye, bret. sku/a ds.; 

Middle Irish sco/7t, sca/7t'co\, gap', scoiltim "I split', brit. with metathesis of sk- to ks- {fiw- 
): cymr. /7c»///"col, gap', corn, /fe/ja (umlaut) "split', bret. faoutads.; Middle Irish scei77ec 
"rock' (see above); perhaps Middle Irish sce77an^ seed, sperm '; 



Old Irish co/a/nn l\esh' , cymr. celain' corpse ' {*kolanJ); cymr. caill, PI. ceilliau 
"testicle(n)', bret. ke//6s.; gall. ca///o-marcus ' coltsfoot, herb (Tussilago Farfara), whose 
leaves and root are employed in medicine to treat coughs ' from older *ca///o marcf 
testiculus equi '; compare gall, ebulcalium {ixoxx\ * epalo-callion) besides epo-calium {*epo- 
callion) 'ungula caballina'; 

Gothic 5/r/^a "Fleischer'; Old Icelandic s/r/^a 'separate, distinguish, discern, (ent)divide', 
skilu. (/after skiija) 'difference, verdict, information, message ', 5/r//a '(ent)divide'; Dutch 
\/ersch/7/encf^6\iierent' {*skiljand)\ Middle Low German sc/7e/e/7 'separate, distinguish, 
discern' (sc/7e/e 'difference, lack, limit, boundary') = Old English sc/e//an^6W\6e, entfernen' 
( *skeldn)\ 

Gothic s/r/Zc/^s "shield'. Old Icelandic skjgldrm. (out of it Middle Irish scell). Old English 
scield. Old Saxon scild. Old High German sc/7t6s. {-tu-stem besides Lithuanian sk/'/t/s 
"abgeschnittene disc '); in addition Gothic skillings. Old High German etc. scilling ^smaW 
coin. Schilling' from skildu -lings, 

Gothic s/ra^a 'Ziegel', Old Icelandic skeli. 'bowl'. Old English scielli. 'husk, 
Muschelschale', Middle Low German schellet 'bowl, fish scale '; Old High German scala 
"husk, shell ', Middle High German schale a\so 'flagstone ', Old English scealu^husk, 
bowl'; Old High German fuaz-ska/'\NOo6en peg, plug as lock for den foot'. Modern High 
German Sche//e 'rc\an\ca, compes, numella'. Hand-, Fu(ischell&, 

Maybe alb. (*skala) hala^ fish scale' common alb. sk-> h-. 

Old Icelandic skjallu. 'Hautchen', Old English sceallanvn. PI. 'testicles'. Old Frisian skall 
ds. (: cymr. caill); Old Icelandic skallim. ' bald head ', as 'abgeschnittene cranium'; also 
Norwegian Swedish skaiie; ablaut. Swedish skulle 'skull, cranium', older Swedish skolla 
"thin Platte', Old High German scollom., scollai. "plaice'; 

with lengthened grade *skel- (compare alb. Iioie): Old Icelandic skalai. "drinking bowl, 
Wagschale', Old High German Old Saxon scaia^bowY; 

Old Saxon skola. Old English 5cc»/i/ "dividing off, partitioning off, troop, multitude, crowd'; 

without aniaut. s-: Gothic liaiiusxu. "rock' {*koi-nu-). Old Icelandic iiaiirm. " stone, rock', 
tieiiai. ds., Finnish loanword kaiiioAs., {*haiij[dn]). Old Icelandic /7e////'"Berghohle', Swiss 
A/e// "flagstone ' etc.; see above S. 544; 



Old Icelandic holdv\. "flesh', Old English holdv\. "corpse', Old English ho/d/an lacerate' , 
hy/dan'6\e skin abziehen'. Old Icelandic hy/da '\acerate' (based on auf a participle *k/-td- 
m)\ 

Old High German scultirra. Old English sci/Zc/o/'" shoulder' (*5/r/-df^/'^ "scapula as shovel, 
as Grabwerkzeug'); 

with formants -/770-and den meaning " cutting tool; geschnittenes wood; ausgehohlter 
dugout canoe, barge': Old Icelandic skglmi. " tine a fork, pod ', PI. "scissors'. Low German 
ostfries Dutch SC/75//77 "thin board'. Old Icelandic ska/ma-tre ' c\oven tree'. Old High German 
sca/m "navis'; also probably Old High German scalmo " pestilence, epidemic disease, 
plague, corpse'; Middle High German schalm(e)6s.\ in addition 5/re//77c> "TodeswiJrdiger' 
{*skalmian-). Middle High German Middle Low German schelm(e)^ villain '; compare alb. 
/7e//77 "mourning, grief, poison '; without aniaut. s-.OId English helma, engl. /7e//77 "handle, 
grasp of Steuerruders, tax'. Middle High German halm(e), he/m ' AxtstieV , Old High 
German helmo, /7a//77c»"Ruderpinne', Dutch helmstock6s.. Middle Low German holm 
"crossbar, crossbeam, Jochtrager', Old Icelandic hjglmi. "tax', /7/5//77-K(?//'"Ruderpinne'; 

"s/roZ-d^a "(abgeschnittene) shaft, pole' is probably die base from Old High German 
sca//5"Stoftstange, Bootshaken', sea/tan '\N\t\r\ a shaft, pole push ', Modern High German 
schalten a\so "einschalten (= dazwischen hineinstoften)' and ijbertr. "walten', dial, also 
"split'. Old Saxon ska/dan'e\n vessel vorwarts push ', Middle High German schalte. Old 
Icelandic skalda' ferry'. Middle High German schalter, sche/fer'bar, bolt'. Modern High 
German 5c/7a//e/'"Schiebfenster, shaft, pole, Bootshaken'; 

with formants -^^o-; Middle Low German sc/7a//r"Sparrenstutze' East Frisian schalk 
"Holzklotzchen as Unterlage', Bavarian sc/7a//re/7"zerspalten'; Swedish 5/r^//r "abgesagter 
stump'; 

Lithuanian skeliu, s/re/// "split' (the pronunciation after skfltR), skilu, sk/7t/"s\c\r\ split'; "fire 
hit' (intonation of the heavy basis, as kelnes); s/ra/a "chip of wood, Lichtspan', Iterat. 
skeldetr burst, break, crack'; Latvian sA-e?/ "split', skelet6s., skele^ sliced piece', etc.; 
about Lithuanian kelmassee above S. 546; 

Old Church Slavic ska/a'rock, stone ' (the meaning "bowl' through borrowing from Old 
High German sca/a6s.), sloven, s/ra/a "assula tenuis; Lichtspan', russ. s/r5///7a"abgeloste 
birch bark'; s/rc»/6/r5 "Muschelschale' (see above Latin siliqua), russ. sce/b'co\, gap', 
sloven, sca^^ "splinter', poln. s/ra//ic5/i?"sichspalten, break, crack'; 



Hittite /ska//a/- 'zerre'\sser\, aufschlitzen'. 

root extension skel(e)-p-: 

perhaps in Old Indie kalpate^W\r6 geordnet, wird zuteil', kalpayati^or6v\e\. an', kjpta 
"fertig, geriJstet' = Avestan ^^-Zra/P/O/a-'schongeformt', das though also to /ra/7/77- 'shape' 
(above S. 620) belong could; 

gr. OKaAoip " mole ' (as "Graber'); OKoAoiy m. "Spitzpfahl'; 

Latin scalpo, -e/"© "scratch, scrape, ritzen, scratch, with spitzem tool cut, chisel, cut ' 
{scalprum, scalper^ scharies tool zum Schneiden, Meiftein'), sculpo, -e/ie (originally in 
compounds from scalpo) ds.; 

Old High German scelifa. Middle High German Modern High German dial, schelfe 
"hautige bowl'. Middle Low German sc^e/i/eA'abgeblattertes piece', schulvern^ exfoliate '; 
Old Icelandic skJglF bench ', Old English sc/e//feTlur, Stockwerk, Bretterverschlag', scielf 
m. ' crag ', Middle Low German sc/?©//' B re ttge rust, shelf; 

without s: Gothic halts. Old Icelandic halfr. Old English healf. Old Saxon half. Old High 
German Modern High German ^a/t* (actually 'divided'); Old English /7/e//fe 'handle, grasp, 
shaft' (engl. helve). Old High German Middle High German /75/fc>'hold, grasp'. Modern High 
German dial, halb, helb^SWe^; Old High German halftra ^bn6\e
```


## [2026-09-14T01:57:47.221Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"schöngeformt\\|schongeformt\\|hukǝrǝpta\\|hu-kar\\|kǝrǝp\" POK_03.txt | head -20"
}
```


### [2026-09-14T01:57:47.281Z] TOOL RESULT

```
2155:vielleicht  in  ai.  kdlpaU  ,wird   geordnet,  wird  zuteil',    kalpdyati  ,ordnet an*,  klptd  ,fertig,  gerüstet'  =  av.   hu-kdrd'pta-  ,schöngeformt^,  das  jedoch  ~ auch  zu  kdhrp-  , Gestalt'  (oben  S.  620)  gehören  könnte;
```


## [2026-09-14T01:57:51.171Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace')\nlines=t.readlines()\nimport re\nn=0\nfor i,l in enumerate(lines[:2160],1):\n    n+=l.count('\\f')\nprint('formfeeds before line 2155:',n)\nEOF\ngrep -n \"^\\s*926\\s*$\\|^926$\" POK_03.txt | head"
}
```


### [2026-09-14T01:57:52.355Z] TOOL RESULT

```
formfeeds before line 2155: 164
2151:926
```


## [2026-09-14T01:57:57.252Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kǝhrp\\|kəhrp\\|kehrp\\|kahrp\" BRT.txt | head -20; echo \"=== huk ===\"; grep -n \"hū̆ka\\|hūka\\|huka-\\|hu-kərəpta\\|hukərəpta\\|kərəpta\" BRT.txt | head -20"
}
```


### [2026-09-14T01:57:57.337Z] TOOL RESULT

```
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
7817:•  g.  a^nman-  n.  'Stetigkeit;  Unaufhörlich- keit': al  kahrplm  utayäitJs  äadät  armaiti^ 'mä  (AP.)'*  "und  Arm.  verlieh  den  Leibern Dauer  und  Stetigkeit"  Y.jo.;.  a)  LS. °m7nT  als  Adv.  'stets,  ewiglich;  unaufhör- lich"'; yi  'mSnl  mazdn  srävi  ahurd  "der ewiglich  MAk.  heisst"  Y.  45. 10;  —  yaii' gqm  karaps  usixscä  (sd.)  alhmUi  däii yücä    kavä   *'mJnI^^    urüdSyatä  (sd.)    Y.
9158:—  ks  UKtmSm  (sd.)  cBrM"^  . ,  pu'^nm pure  Y.  44. 7 ;  —  kjrmaomi  "iwam  hacat.- pu^rqm  V.2^.6;  — yat  k^rmaot..  *amar- /an/a  fasu  vira  V.p.  4;  Yt5.  30,  /j.  16 [k^rmavani);  —  matdqmcä  (s,  i  c)  büiricä kjrpsvä  .  .  xrapaitl  (sd.)  Ayat  ahmat  aibi Y.  4n.  I ;  —  yi  umm  pinmm  k?rpnaoiti  . . bantjm.'a  drum  k^rmaoUi  V.  22.5;  uj.^%, Y.  10,13;  —  \hatm  parsam  hami'i''iyam akunaus  Bh.  4.2;  2%  3;  —  ya'ia  asym amasyq  (sd.)  kmnaväni  .  .  karh'qn  Yt. 5.30;  —  ts  k>rmava  mdwaire  ajyamnem V.2.z8;  36  {kirnittol);  — yat  amm  patti.- irist»m  /rä.nastirii  kjnnaaiti  V.  r/,  42;  — armadsth  atiyh  äps  k^nnaoi  Yt.5,78;— >J( Im  firasJmisA.)  *k3rjnaon'^^  ahsm  Y.30.9; Yt.iil.ii  (k^rMavqn),  89  {k»rma7,;li) ;  — yezi  iidit . .  mazdayasna  . .  kahrpsm  kvars.- dar^slm  (sd.)  k:>rmavqn  V.5,14;  13  (wo k^r»nai)t,  statt  Plur,);  —  raeko  (sd.)  mS haca  aühij  s»mat  vatihö  k^rjnaoiii  Yt. iy.2o;  10.2S;  —  ya  *a/r3.ur7'isval  (sd.) hrmavainti  irmi  Yt  13.  z6;  —  I  av<^taiy (^urJ'mazdä  ^mazänam  (sd.)  kunautiro Bh.  4.'6;   —  ava'^  adam  patipadam{%iL)
9326:•  j.  kahrpuna-  m.  Name  eines  a'aft'ischen  j  schleppten  sie  die  Weiber  den  Menschen Tiers'*:  baivan  alinam  spakanqm  •■nanqmX-^^^'  Yt. /g.  80".
9535:kahrp-  Noten
9545:•  j.,  g.  kahrp-,  ksr?/-^'^  f.,  n.'>  'das  sieht- ' bare  Äussere  jedes  Wesens  und  Dings, , äussere  Erscheinung,  sichtbare  Gestalt': sraliiqm  at  tSt  'p/m  (AS.)  -^pam  (GP.)  j ävaedayamakl  tnazdä  ahurä  iinä  raota  . . avat  y.ll  hvarS  aväcT  Y._J(*'.  6;  — para avtiiriAe  hü  "^warstö  (sd.)  'pya  (LS.)  Y. ' /p.  8;  —  asmamm  ,  ,  y3  hislaite  ayanhs 'pa  (IS.)  x^amahe  (sd.)  ".  .  mit  der  Er- scheinung von.,  (sva. ..  anzusehen  wie..)'' YL  13.  2.  A)  insbes.  von  lebenden Wesen;  auch  vom  gestalteten  Stoff  selbst 'Leib,  Körper';  i )  von  Menschen  und Göttern:  aj  'psm  (GP.)  utayuitil  dadat ärmaitis  qnmä  (sd.)  Y.jo.  7;  — ■  yd>!a varsnahe  'palie^^  dsus  (sd.)  N.  7o(7;  — paiti  ainii  .  .  'p^m  .  .  gaia/ie  .  .  °ppm  .  . säJiar/  .  .  "Pim  .  .  abmatr/aAe  .  .  'P^m ..jahikayüi  ..  -p.m  Y.//.  30-32;  32;  — avqm  'P^m  yazamaide .  -yqtn . .  k^r^säspahe Yt /?.  61;  Az._J;  —  üjasat . .  viriisra-fitä ..vätahe  'pa  (IS.)  Vt/4-2;  —  mi%nm..
11964:•  j.  tanu.kahrp-  Adj.  'die  Gestalt  der eigenen  Person  habend' (?) '*,  von  Söhnen: puHrS  zayanle  °pa  kiArpa  Vyt  V;  3.
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
21224:Au.irixt^m(sd.)..trinaxtiYt.io.6B.  a)init' vorhergehendem  vTspum  S  aAm3J  'donec, bis':  näa  difyäi  aäa  ^rityäi  vJsp^m  ä ahmst  y'  hl  han/asaitt  yaia  iahrutiim *yär?  N.42;  43,  Vd..#.  3)  mit  dem Konj.  (oder  Inj.)  in  fiiCuiischem  Sinn:  yai (s.  V)  .  .frasna  (sd.)  paiti.mravSm  y  mgm ftrpsai  axtys  Yt  j.  8z;  —  y  irista  paiti us»hiltqn  ..  äa%aite  fras>m  vasna  anhui Yt  Jp.  1 1 ;  —  y  astvatjTTls  fraxHäite  .  . avaaa  drujpm  nilbarat  Yt  jg.  92  f.;  —  y yavs  dqyät  aal  daeva  :^um  (sd.)  y^  ■  ■ äayap  äaO  ..  V.,;.  32;  —  asti  zT  ana avavai  uxäata  (sd.)  ya'äsa  y  dim  vJsp5 ar»huf  äsaxiat  (sd.)  . .  pairi  irtkyqstätat (sd.)  haraite  Y.ig.  10.  /)  im  Sinn  des lat  Fut  II:  aSaha  hr  tanüm  . .  »idaihyqn vTsppm  3  ahmat  .  .  yat  (s.  c.)  frä  vayS patqn  ,  .  äat  y°  ('wenn')  ht^  frä  vayS patqn  fra  urvara  ux^qn  nysttiä  apa.- tacin  .  .  ariala  .  .  kahrptm  kvanJansJm kmnaot  V.  5.  i  a  £ ;  —  *fra  *ma  . .  *gara- yffi/ (sdj)  y  raful  fritsil  *a/asäi  N.  ip;  — y  dim  iatäj..paia  *avaMääiV.S.too(t); io3(?); — yai  nSiriAa  voAunls  atwi.vamäl y  (nachdem')  Al  'kray3  xlafiia  sacatüe V.  16. 8;  — y  ('nachdem')  kl  tanul  hilkvi Mymii  pqsnu  bavat  pascaSa  .  .  jasBtt  V. p.  31.  a)  mit  vorhei^ehendem  pasca 'postquam':  aem  ai^he  asti  utvanam  yal (s.  V)  nä  pasla  y  usthtÜäi^^  .  .  änV aÄOT  ■  upajtuyät  V.  18.  43;  s.  V.  18.  49 (unter    4).  b)    mit    vorhergehendem
26811:•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
=== huk ===
```


## [2026-09-14T01:58:04.641Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hu.k.r.pta\\|hukarapta\\|hukjrapta\\|hukirapta\\|schöngeformt\\|schöngestaltet\\|hu.kahrp\" BRT.txt | head -10; echo \"=== BRT hukairya/hu- list ===\"; grep -n \"^•\\s*[gj]\\.\\?,\\?\\s*\\(j\\.\\|g\\.\\)\\?\\s*hu.k\" BRT.txt | head -20"
}
```


### [2026-09-14T01:58:04.820Z] TOOL RESULT

```
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
19218:•  j.  nivizan-  Adj.  'anziehend,  reizend,  1 '^'''*  Yt/5. 45,  Geringe  Stelle. gefällig'  ■>:  Äa  hi  maiUm  nyazata  ya^aca  .  ,  j.  nisma-  m.  '(Hineingehen  in  den  Erd- hukfr)ptaßtänayai!aca  anh)rfz3nal^'Q:)  \^o^^^  sva.)  Tiefe':  paoirjm  upa  vmy>m "äe  schnürt  sich  ihre  Taille,  damit  '-^tz  ■  ni>:w>rnöil  .  .  dva  »rssu  -mähe''»  "das Brüste  schöngestaltet  und  damit  sie  gefällig ,  erste  Loch  sollst  du  .  .  zwei  Finger  in seien"  Yt 5.127.  der  Tiefe  ausstechen"  V.o.  6.
30152:•  j.  hu-kanpta-  Adj.  'schöngeformt':  hs (näml.  andvt)  hl  maiiim  nyanata  ya%aid 'ta  (NDm.)  fsiSna yähaca  aifhm  ntvaxäna
=== BRT hukairya/hu- list ===
30150:•  j.  hu-kshrp- Adj. 'wohlgestaltet':  vatihus haomS  .  .  'kfnfi  Y.p.  16;  F.  ja.
30152:•  j.  hu-kanpta-  Adj.  'schöngeformt':  hs (näml.  andvt)  hl  maiiim  nyanata  ya%aid 'ta  (NDm.)  fsiSna yähaca  aifhm  ntvaxäna
30545:•  j.  hugka-,  p.  Niäka-  i)  Adj.  'trocken, ausgetrocknet':  'i^m  alsmim  Y.  7/.  8;  — aHavat  'kanam  alsmanqm  aSavat  nafia- nqm  V.  7. 31;  —  vtlastiJrap  yat  (Sp. 1252  u.)  'kanqm  (als  Obj.)  ..  aitiha  s^mS nidaüyqn  "sie  sollen  in  der  Länge  einer V.  vom  trockenen  (Holz) , .  auf  der  Erde hier  niederlegen"  V,  7. 29;  3c,  33,  34;  — 'kanqm  yavanqm  V.  7.  35;  —  'hm  p>htn raicayat  Ytj.  78;  77;  —  aSavat  apat haca  nilbarayjn  °ke  z)me  nidathya»  "so- viel sollen  sie  aus  dem  Wasser  heraus-
30550:•  j.  huSkö.zam-  1)  f.  'trockene  Erde'; I  istyehe  v3  sarstvahe  va  'amanam ''  vä \pqsnam    "Staub    von  . ,  trockenen    Etd-
```


## [2026-09-14T01:58:22.726Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 خوک ===\"; grep -n \"خوک\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T01:58:22.786Z] TOOL RESULT

```
=== BQT v2 خوک ===
38713:                          ‫همچو دبولاخوکه‬               ‫شیرین باشد » و برچشم کشند سیلان آب را بر‬
```


## [2026-09-14T01:58:24.035Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD xuk ===\"; grep -n \"xūk\\|xūg\\|hūk\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"xūk\\|xūg\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T01:58:24.129Z] TOOL RESULT

```
=== PHD xuk ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:2249:hedgehog xārpušt, xūkar(ag), züzag.
=== NYB ===
```


## [2026-09-14T01:58:29.660Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));\nimport sys\nfor k in ['BQT','MON','FFD','IEC','VOP']:\n    print(k, json.dumps(d[k],ensure_ascii=False,indent=1)[:1800]); print('---')\""
}
```


### [2026-09-14T01:58:30.653Z] TOOL RESULT

```
BQT {
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, a
---
MON {
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
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in
---
FFD {
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
---
IEC {
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
}
---
VOP {
 "title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992",
 "kind": "none",
 "url": null,
 "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."
}
---
```


## [2026-09-14T01:58:35.678Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (334,335,336):\n    print('##### leaf',leaf)\n    print(t[leaf][:2500])\nEOF"
}
```


### [2026-09-14T01:58:36.932Z] TOOL RESULT

```
##### leaf 334
ambiguity in the Celtic forms) Skt. kumpah, adj. ‘with arm crooked'; MIr. comm ‘trunk, waist; W cf. cwman (2) ‘tump’; E dial. (ambig.) hum ('arse', cf. kum-); Du. (?) hom ‘milt’; Pol. kepa ‘hillock; tuft; clump of trees; Li. kumpas (hunchbacked'; kümpa ‘Jump, bump, gnur!’ beside Li. & Latv. kum- pis, m. ‘ham’; Latv. cf. also kumpju, t, v. “get humped, grow hunchbacked'; Li. kumpstu, kumpti ‘get bent’; Finn. LW kumpu ‘hillock’
(kundəlos, see kondulos)
kundos ‘stolid, stout, ponderous, stocky’ Arm. kunt & kund, gs knti & kndi, abl. -av “bald; squat, stocky’; Per. kund ‘blunt; stupid’; Hes. kundós ‘stolid, unwavering’; Fris. hont ‘stout fellow, sturdy fellow’. Cf. the variant Skt. kunthah (blunt, fr. a type *kundsios or sim.)
kungios, io (kungos, à) (1) ‘bulge, hump, mass'. Cf. kunkos, kunkolos & next Skt. kufijah ‘thicket’; Alb. cf. kungé ‘hump, swelling, dome'. Ambig. cf. kunk-); E hunk, hunch (according to dial.); Li. kungis, io, m. *potbelly'; Latv. kungis “belly? beside kungu- lis (and kunkulis *Iump^), w. denasalized tra- ditional parallels in kogars, kogurs ‘tuft
kungios (kung-) (2) (?) ‘corner’. Cf. kungios (1) Per. kunj (kung), id.; MDu. (alleged) honc ‘corner’; Du. Fris. honk, s. ‘home’. (Iso- phonic: E hunch “inspiration, idea; hunch- back’; Du. honk (2) “aim, target")
kunkolos, is, à “ball, Jump, knob, peak’. Cf. kungios (1), kunkos, konkolos Alb. (ambig.) küngull, m. ‘marrow, pumpkin; Li. kufikulas ‘bubble’; kunkulýs, m. “bubble; post, pillar’; Latv. kunkulis ‘small lump”
kunkos, à, io “lump, hump, bulge’. Cf. kung-, elc. Alb. (ambig.) kungë, f. id.; (R (ambig.) küca ‘heap, mass, crowd" preferably to kaukos (1), q.v); Li. cf. kunksoti, inf. ‘bulge; huddle together; Latv. cf. kunce, f. (*tadpole', fr.
589
*kunkio (?)). (The phonology of Oss. kunc, kuncä ‘bellows’ is uncertain)
kūnos ‘lump, swelling, body’. Cf. WP I, 367 Per. kün ‘arse’; Br. kin “bud, germ of wheat’; ON honn, gs hüns, m. (1) ‘knob’; Li. kūnas “body”; Latv. cf. künis (2) “abdomen
kuntsios (?), kundsios (?) ‘docked, short’. See kund- Skt. kunthah ‘blunt’; R kücyj ‘docked’; Cz. cf. kucel ‘clod, lump?
kūpā, os, is (1) ‘hollow, container, cup- shape, bonnet’. WP I, 372 Skt. kūpah ‘ditch, hollow’; Hiero-Hitt. kupas (queried: ‘tomb’); (?) Lyc. cf. gopa, gopu ‘tomb’; Myc. cf. kupera (queried: kupélla 'goblets'); Hes. küpe “hut; boat; Lat. cüpa ‘barrel’; MIr. cúa ‘cup, bowl’; ON hüfr “hull, hulk’; húfa ‘cap, bonnet; vault’; Sw. huv, m. ‘penthouse’; huva, f. ‘hood’; Du. huif ‘coif, hood, awn
##### leaf 335
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
kur- (6) (residual element of type quer- (
##### leaf 336
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
kurst- ? *moo
```


## [2026-09-14T01:58:48.008Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor leaf in range(355,366):\n    nums=re.findall(r'^\\s*(\\d{3})\\s*$',t[leaf],re.M)\n    print(leaf, nums, t[leaf][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:58:49.357Z] TOOL RESULT

```
355 ['628', '629'] lope’; Li. (long-gde) Sluonüs, adj. ‘sloping’. Cf. WP I, 442, I, 499 & II, 598 K
356 ['630', '631'] ris. hlestia, Sw. lystra, v. ‘to listen’ Klütos “heard, famous; fame, report, ru
357 ['632', '633']  cf. also Cantabria (the Basque country); Br. (mutated) gant, gand, gan, as W Km
358 ['634', '635'] �hostility, fury’. Isophonic in Li. šiepiù, ti “grin, sneer’: Saipas ‘mockery’ (
359 ['636', '637'] ��hesitate, fear; Lat. cünctor, ari, OL. conctor ‘delay, dally’ beside per-cünct
360 ['638'] sophonic is Slo- vak sotiť ‘thrust; throw’); Sw. häda, fór-háda, v. ‘Scorn’ Kót-
361 ['639', '640']  growth’; Gk. cf. krág- gë “a crustacean’; kraggón ‘crab’; W cf. cran- horny 639
362 ['641', '642'] Sab *night'; Av. x3apa, f. ‘night’; X3Sap-, v. (cover; Li. Sampu, inf. Sapti *di
363 ['643', '644'] : 'thistle"); Alb. thikë, f. ‘knife’; (Ir. coc ambig. ‘crest, comb, head-dress, 
364 ['645', '646'] ia & kuná-muia; Li. $Sun-muse Kūnos “lacking, diminutive’ Skt. cf. sunyah ‘empty
365 ['647', '648'] ron ‘broom; sweepings'; saróo, den. vb. ‘clean’; Li. Svarüs ‘clean’. (It is unce
```


## [2026-09-14T01:58:51.263Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[361])\nEOF"
}
```


### [2026-09-14T01:58:52.548Z] TOOL RESULT

```
 growth’; Gk. cf. krág- gë “a crustacean’; kraggón ‘crab’; W cf. cran-
horny
639
gen, pl. au, f. ‘wen’. (W cranc ‘crab’ is a LW)
Krnió ‘bring to a head, finish’. Cf. WP I, 405 Gk. kraino, id.; Alb. kryej, id. See next
Krniom (Krniio-) Krnios “head, skull, horn, tip; of a head”, etc. Cf. Krnom, Ker-, Kros, etc. WP I, 405 Gk. kraníon ‘skul’; Myc. cf. a-karano (ouer, ied: *headless); Alb. krye, n. ‘head’; OFris. herne, f. (corner; OE hyrne, f. id.; OSw. hórne, Sw. hórn, n. id.; Norw. hjórne, id.; ON hyrna, f. “tip of axe'; Slovak srní, adj. “of fal- low deer'. See next
Krnom (Krnu) (1) ‘horn, tip, corner’. Cf. Krniom, etc. WP I, 406 Per. sürna (trumpet. LW in OCS surna, su- rina, sarna *clarinet); Hiero-Hitt. surni ‘horn’; Gk. krános, gs -eos, n. ‘helmet’; kránon ‘head’; káàrnos, m. (tram'. Hes.) kárnon (‘Gallic horn’, prob. Gallic wd.); cf. Hes. karanó ‘goat’; Alb. krye, n. “head”; Lat. cornu “horn, corner, tip’; not in W or Ir.; Go. haürn, n.; OE horn, m.; OHG horn; ON horn, n. d: OCS srünü, srüna ‘fallow deer" Pol. sarna ‘doe’; R sérna ‘chamois’
Krnom (Ernos, us) (2) ‘cornel-cherry’ Gk. kránon (2), id.; Lat. cornus, gs -1 & -üs, f. id.; cornum 'cornel-berry'
Kros, -es- ‘head, tip, top’. Cf. Ker- (2), (Kor-), Krn-, etc. Skt. Siras, n. & Sirah, m. id.; Av. cf. saro, obl. -áh-, n. id.; Gk. kår, in phr. epi- ‘headlong’; kára, n. “head, headland’; Per. sar ‘head’; Arm. sar, gs -u ‘top, peak": Gk. -krús in i-krüs 'forth- right’; antikrü (Cfacing', etc.); beside kro- (in kro-taphos, kr-osphos, kr-ónos, krobulos, etc.)
Krs- (Krson, Krsron, Krsen-) ‘hornet, wasp’. WP I, 407 Lat. crābrō, gs -onis, m. id.; OW creyryn ‘wasp’; Du. cf. horzel, f. ‘hornet’; OCS srü- šení, Cz. sršeň & sršán; Pol. szerszeń; R šer- Seni, m. id. beside OCS srüsa, f. ‘wasp’; Li. širšuð, gs. -eñs, m., širšinas, m. & širše, f. id.; Latv. sirsenis, sirsonis, id. (The composition of MHG hornuz, hornis, OE hyrenetu, hyrnet ‘hornet’ is uncertain)
Krsr-, Krsno- see Kerosr-
Krt- (1) ‘cover, covering, skin’
Krnio — Ksaulð, ið (ksaul-)
10
20
25
30
35
40
45
640
OE hyró, f. ‘skin’; Li. Sirtas, m. ‘den’
Krt- (2) “cut, blow’. Cf. Kerto Skt. śūrtáh, -śīrtáh ‘shattered’; Arm. sartnum ‘be separated’; Per. cf. sile, sili, sīli “slap, blow’ beside süli Cplough lit. ‘cutter’ ?)
Krt- (3) ‘mixed’. Cf. Ker- (3)
Cf. Vedic $rtáh, śrītáh and $ratab, id.; Gk. cf. á-kratos, -krētos ‘unmixed, neat
Kruos, is ‘horn’. Cf. Ker-, Krn-, Kor-, Krnio-, etc.
Av srvà, f. “nail, horn’; MIr. cf. (alleged) crú ‘hoof (beside Irish: crúb, f. id.); OPr. sirwis ‘roebuck’. Cf. Gk. ánti-krus ‘head-on’
Ks-, zero-gde of eks, q.v. 'from-, out-; un-,
ex-; very- Oss. s- (intensive verbal extn.); Arm. c- (be- fore vowels); s- (before consonants); cf. c-ac ‘Jow’; c-ajg ‘night’; s-nank ‘bankrupt’, etc.; Gk. cf. s- (in s-kholé, á-s-thma, s-thénos, s-phod- rós, s-bénnumi, s-kháo, s-kházo, etc.); Alb. c-, sh- Cour, and adversative px.); Olr. ass, as, as- (as in as-caoin *un-kind") (r-gde type: *oKs-); W ys- (in ys-garm 'outcry', ys-barth, adj. 'separate"); Go. us-, us *out-, out of; ON Ot-, ór, as Go.; G er-, ur-; OCS sú, prp. w. gen. ‘off; š-, px. (as in StuZdi “foreign”, Stusto, Stutiti “feel, fr. *Ks-ieut-); Li. i$, i$- as Go. The sense of ‘to, toward? occurs in Arm. ç- (q-art till now’; c-ank “to the end, always”); and in Cz. s (in s to ‘up to it, able’; se-č ‘to what, for what’. Uncertainly as a fused px. in Skt. khajami ‘stir, cf. a20, and in OE sceacan ‘brandish, shake")
Ksaks- (variant form of Káksa, q.v. and cf. Kakis “branch; peg, spike" etc.)
Arm. caxem, v. ‘harrow’; cf. Go. hoha (plough', fr. *Kak-); Per. šāx “branch, horn’
Ksanio (ksánio) ‘flatter’
Gk. saíno ‘fawn, flatter’; OCz. (velar initial) chanéti, id.
Ksap- (?) “absence, disappearance, darkness” Skt. cf. kSap, f. & kSapa 'night'; kSapàmi, v. ‘fast’; Per.
```


## [2026-09-14T01:59:01.110Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor leaf in range(612,624):\n    nums=re.findall(r'^\\s*(\\d{3,4})\\s*$',t[leaf],re.M)\n    print(leaf, nums, t[leaf][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:59:02.257Z] TOOL RESULT

```
612 ['1106', '1107'] 1) and (2), q.v., and cf. ros- (2) Skt. cf. rsuh, adj. ‘dash
613 ['1108', '1109']  sakjo, f. “battle” beside ON sókn, f. (1) “attack, prosecut
614 ['1110', '1111'] �; Du. zaluw, adj. 'sal- low’; OE salo, saluwig- ‘dark’; R s
615 ['1112', '1113'] . also Skt. saminah, adj. “an- nual; W hafin, m. 'summer-sea
616 ['1114'] om, iio) “grain, flake, bran, scurf". WP II, 454 Skt. sasyám
617 ['1115', '1116'] .v.); OCS cf. jazdo, jazditi ‘ride’, fr. *ja-, -sd-, cf. iai
618 ['1117', '1118'] , 3s: sésti. Other- wise Skt. sádami, v. (sit; Ober Av. sad-
619 ['1119', '1120'] ing entries. Cf. also sengh- se&hedhla ^piough-tail, rudder,
620 ['1121', '1122'] g! “des- cend’; cf. e£K, iğiç, iğiwk, s. “descent. See SEM: 
621 ['1123', '1124'] “bind; spellbind'. Cf. soitos ON síóa, v. 1. *work charms'; 
622 ['1125', '1126'] . “drip, drizzle’ selĝ- (1) ‘get’. Cf. seluð in Supt:S Skt. 
623 ['1127', '1128'] al, simple’. Cf. sem- (1) Arm. amol, amolk, s. ‘pair; Gk. cf
```


## [2026-09-14T01:59:05.706Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor leaf in range(634,642):\n    nums=re.findall(r'^\\s*(\\d{3,4})\\s*$',t[leaf],re.M)\n    print('###',leaf, nums, t[leaf][:60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T01:59:06.828Z] TOOL RESULT

```
### 634 ['1146', '1147']  (-əlos) Hes. skáphalos ‘ladle, baler’; Ir. scabhal, mf. ‘ca
### 635 ['1148', '1149'] . (3) ‘shame’; Dig. kämä, id. (and *pudenda?); Arm. (ambig.)
### 636 ['1150', '1151'] aped; cut, carving, gouged article, shaped article’. Cf. ska
### 637 ['1152', '1153'] tched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudüs, adj. ‘p
### 638 ['1154', '1155'] v But R ščegol = 'goldfish"); (ON skikka, v. “arrange, ordai
### 639 ['1156', '1157']  skélti, v. ‘split; Latv. Skelu, Skelt, id. (NB. There is so
### 640 ['1158'] Ir. sceinnim, scinnim, v. ‘leap, start, bud, shoot'; Li. ske
### 641 ['1159', '1160'] . ‘rough, hoarse’ (skerd- (1) & (2), see skherd- skérd- ‘fli
```


## [2026-09-14T01:59:09.010Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[638])\nprint('========639========')\nprint(t[639][:3000])\nEOF"
}
```


### [2026-09-14T01:59:10.147Z] TOOL RESULT

```
v But R ščegol = 'goldfish"); (ON skikka, v. “arrange, ordain' and skikkja, v. ‘cloak’ are, like G schick-, of ambig. vocalism)
skeibh- “slice, cut, division’. (Gmc. ambig. cf. skeip-) MHG schibe, wf. (2) ‘slice’; E dial. shive, shiv, id.; ON skífa, f. id. & vb. id. Du. schijf, f. id.; Li. skiébas, m. 'firebreak in a wood, clearway', skiebiü, skiébti, v. ‘slice’
skeid-, see skid-)
skeidh- (skeidhrà, skheidh-) ‘slice, cut; blade, cutter, incision". WP II, 543. Cf. ski- dhros, skidros, skh-, etc. Arm. cf. xe, s. lees of grapes’; W (?) ysgwydd, pl. -au, f. ‘shoulder’; Br. skoaz, f. id.; Cor. scoth, pl. scodhow, f. id.; OHG skit, OFris. skid, n, OE. scid, n. ‘slip of wood E shide *roof-shingle; MHG schiten, sv. 1. ‘chop, split’; scht, sn. as OE; cf. G Scheiter-haufen; ON skíð, n. ‘lintel, chip, ski, roof-shingle'; cf. (probably fr. *skidh-) ON skíði, n. ‘sheath’; Sw. skida, f. (2) “pod, shell in view of Li. skydas ‘shield, carapace’; Cz. cf. Stidla, f. ‘stilt’; Li. skiedà beside skiedrà, f. ‘chip’; Latv. cf. Skiedi, mpl. “teeth of weaver's sley’; Li. skíedziu, skíesti, v. ‘divide’; Latv. šķiežu, Skiest, v. ‘scatter, squander’
skeiið (skeið, skheiio, skheio) “divide, split, distinguish, choose’. Cf. WP II 542 Hitt. cf. skyami, 3s. skici, v. (anoint, lit. “dis-
skeg- (skheg-?) — skeko, ið
10
15
20
25
30
35
40
45
1154
tinguish'?); Lat. scio, scire, v. ‘ordain, ap- point; know, be skilled in’; Br. cf. skeZa, v. ‘cut’; cf. skiant, f. ‘mind’; W cf. ysgi, pl. sciod, m. “slice?
skeim- “separation, division’. Cf. skeiio, etc. W cf. ysgwyf, m. ‘shower; scum’; Blg. &Cim, m. *wool-combings'; Li. skiemuó, eps, m. (woof-threads;  shuttle-race; pl. -menys *healds?); Latv. cf. Skiemele, f. *shuttle-race'
(skeip-, cf. skip-, sKip- and skoip-. All the evidence is ambig.) Cf. MHG schibe, wf. (2) ‘slice’; E dial. shive, id. (fr. *skeibh-, *skeip- or fr. *skibh-, skip- with variant initial in) Blg. cipa, f. (skin'. LW in Mod. Gk. & Alb.); cf. Cz. Cíply, adj. 'slender, slim”; Ciplenka, f. ‘fawn, young deer" For Li. skiépas, m. ‘graft’, see skoip-. (Isophones in OCS, and com. Sla- vonic, Stipljo, Stipati, v. ‘pluck, pinch’, R šči- pàt', inf. id. and in Li. (*ei/oi) skiepiü, ti, v. *slit open")
skeir- (skheir-, skhir-) ‘product of soured milk’. Cf. skir-, ksirom Oss. Ciri, Digor. Kere, s. fcheese-cake'; Arm. xer, O-st. (‘dish of beestings'. Cf. for phonol. lezu ‘tongue’: Li. liežuvis), Alb. hirrë, f. Cwhey', perh. fr. *skirs-, but vocalism may be *-ei- cf. dimén: Gk. kheima)
skeitos, à, om 'division, separation, separa- tor; sheath, shield'. Cf. skheit-. WP II, 543, and cf. skoitos Lat. scitum, n. & *scitus, ab. sg. scitu, m. ‘decree’; cf. in-scitia, f. ‘ignorance’; Mir, scíath, m. “shield, protection’; W ysgwyd, pl. -au, f. id.; Br. skued, pl. -u, m. (pl. also skueZu), id.; ON skíði, n. ‘sheath, sley’; Sw. cf. skid- gård, s. ‘fence’; OCS (and com. Sl.) Stitü, m. ‘shield’. Prob. o-grade in Li. skiétas, m. ‘sley’; Latv. Skiets, id. in view of OPr. skaitan, s.n. ‘shield’. See skoitos
(skeio, see skeiio)
skeko, ið (1) ‘chatter, yelp’ MHG schëhen, wv. (1) ‘squeak’; Cz. štěkati, inf. “bark?
skeko, ið (2) “jump, dash’. Cf. skok- Arm. cf. xeé, Let ‘shrimp, prawn’; Gk. cf. (?) skekós, m. ((lizard'", fr. *skēk-?); MHG schéhen, wv. (1) "hurry, hunt’; ON cf. skær, m. (fhorse', if fr. *skekro-); (o-gde in) OCS
1155
(and com. Sl.) skokü, m. “jump”
skel- (1) (skelið, skh-) “divide, distinguish, discern; split, division”, etc. Cf. skel-, skil-, skol- (skhel-, etc.), and skál-. WP II, 592 Alb. cf. cel, v. Copen’, fr. *skhelijo); LLat. *sce- lio, Ere, v. (“choose in It. sceglere, pp: scelto); OFris. skilla, v. ‘quarrel’; LG schelen, v. fdis- tinguish'; Du. schelen, v. ‘differ’; Li. skeliü,
========639========
 skélti, v. ‘split; Latv. Skelu, Skelt, id. (NB. There is some confusion in Gmc. between types *skel- and *skil-, q.v.). O-gde in Hitt. skalla(imi), v. (queried: ‘split, têar’). Nominal types: Arm. xelk, g: xelac, ab. xelawk, pl. ‘brain’; OE scelle & scielle, f. ‘cutting, separa- tion’; LG schel, f. ‘difference, separation, boundary’; R scel', f. ‘chink, slit’; Latv. cf. Skelte, id.; Sw. skål, n. “faculty of reason?
skel- (2) ‘dry, wither, decay, crumble’. Cf. WP II, 597 Gk. skéllo, aor: éskela, v. ‘wither, dry’; cf. skeletós *withered'; Li. skeliù, skelsti, v. ‘de- cay, crumble’; cf. Gk. -skelés (‘dry’ in cpds.)
skel- (3) “bent, twisted, wrong'. Variant skhel-, q. v. Arm. xey, i, av, adj. ‘crippled, lame); xeyem, v. ‘cripple’; Lat. scelus, gs: -eris, n. ‘crime’; OFris. skilla, v. ‘quarrel’; Fris. skeel (2) “de- fect, evil, setback, lack, blemish; dispute'; Li. skelià, éti, v. “be indebted'. (Isophone: Gk. skélos, gs: -eos, n. ‘leg, shin’. Lit. 'bend"?). Extension in OHG skélah, adj. (^squinting"; see FK:EWDS: schielen and cf. MHG schélch, gs: schélhes ‘crooked, awry, asquint’). Cf. WP II, 598
skel- (long-grade of type skel- (1), q.v.) “division, part; cut, separation; discernment’ Per. sikal 'thought'; sikalidan, inf. “think”; Arm. xil 'inquiry'; Alb. i hollë, adj. ‘thin, fine’; huall, pl. hoje, m. ‘honeycomb’ beside hoj, hoje, mf. id.; hoj&, f. ‘crag’; cf. té-huell, té-holl, v. (roll out thinly’ fr. *at-skelo); Br. Skil-, cpds. “partly-?; Fris. skiel, s. “peg, esp. one used in netmaking'; ON skáli, m. ‘hut, shed, room’; skál-hüs ‘privy’; Latv. šķēle, f. “slice”; Skeleju, v. id.; Li. cf. skelimas “cleavage”
skelb- (?). Cf. skolb-. Ir. ambig. skelbh-? Ir. scealb, f. ‘splinter’; Du. schelp, MDu. schel- pe, f. 'scallop-shell; (isophonic in OHG sciluf,
skel- — skendó, ið
15
20
25
30
33
40
45
1156
MHG schilf (reed, rush"). (E scallop is fr. MFr. escalope, and this fr. Gmc., cf. skolb- below)
skelbio (skolbió) “pull a face, grin” ON skelpa, f. ‘grimace’; Cz. (dial. 3-) Skleb, m. ‘grin’; Sklebit se, v. id. beside OCS (o-gde) sklabiti se, inf. ‘smile’; (isophonic: Li. skelbti, inf. *declare")
skelbh-, see skolbh-, and cf. skol-. Ir. ambig. Thus only in It. scealb, f. ‘splinter, fragment, slice, shred’; G cf. schelbern, v. “form a crust, esp. of ice’. Ir. also (o-gde in) scolb, mf. (splinter, peg, thorn, spar’: Latv. skalbi, mpl. ‘crossbars on plough-fork. Apparent isophones in OE scielf ‘pinnacle’; ON skjolf, f. 'height")
skeldh- ‘separation; separator’. Cf. skel- (1) Go. skildus, m. ‘shield’; MHG schilt, gs: des, m. id.; OE scild, scield, m. id.; ON skjoldr, ds: skildi, m. id.; cpds: skjald-; OCS (?) *xlédü, m. ‘weeds’; Li. skéldena, f. ‘split leather’; Latv. šķelda, f. “split, chip’. (ISophonic: Arm. xeyd, i-st. 'stranglehold, noose'; xydem, xey- dem, v. ‘strangle’; xyduk, adj. ‘sultry; MHG schélten ‘scold; repulse’; Icel. skjalla *flatter")
skelos, see skhelos and cf. skel- (3) (^wrong, crime', etc.)
skeluos, skelquos, see kseluos. This form is expli
```


## [2026-09-14T01:59:22.666Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG kar ===\"; grep -n \"uskār\\|us-kār\\|uskard\\|sigāl\\|sigal\\|segāl\\|sikāl\" CHEUNG.txt | head -20; echo \"=== CHEUNG kar3 ===\"; grep -n \"^\\*kar\\|^kar \" CHEUNG.txt | head -20"
}
```


### [2026-09-14T01:59:22.736Z] TOOL RESULT

```
=== CHEUNG kar ===
15822:sk’lynynd /skarénénd/; Partic.: perf. pass. caus. BMP ’wsk’lt /uskard/ || (+ *pati-) Caus.: pres. IND. 3pl. 
41464:sigalidan/sigal-, 238 
=== CHEUNG kar3 ===
15502:*kar8/*xrah. 
15768:*kar ‘to do, make’ 
15819:*kar 237 
15919:*karé ? ‘to strike’ 
15927:*karH2 239 
15939:*kard ? ‘to stick, keep down ?’ 
15960:*karH! ‘to celebrate, praise’ 
15984:*karH ‘to spread out, scatter (esp. seed), sow; to make furrows, plough’ 
15989:*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
16048:*kars/*xrah 241 
16074:*karp ? ‘to lament, moan, mumble’ 
16092:*kars/*xrah ‘to draw, plough’ 
16172:*kartl 243 
16180:*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
16196:*kart! ‘to cut’ 
16271:*kart? ‘to twist, turn’ 
16305:*karz ? ‘to cheat, deceive’ 
55117:*kard (s.v.), *tund 
55142:*kar (s.v.), *pas (s.v.), *sam 
55321:*kar (s.v.), *sac’, *tary (s.v.),
```


## [2026-09-14T01:59:24.207Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD uskar ===\"; grep -n \"uskār\\|uskard\\|wskʾl\\|us-kār\" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n \"uskār\\|uskard\" NYB_vol2_glossary.txt NYB.txt | head -10"
}
```


### [2026-09-14T01:59:24.284Z] TOOL RESULT

```
=== PHD uskar ===
PHD.txt:601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
PHD.txt:1351:consider abar nigerīdan, pad ēd dāštan, handēšīdan, hangārdan, ēšmurdan, uskārdan.
PHD.txt:1353:ēšmārišn, uskārišn(īh).
PHD.txt:3980:think handēšīdan, menidan, uskār- dan; v. consider.
PHD_mackenzie.txt:5070:uskardan, uskar- ['wsk'l-tn I J ......, (N sigal-)] think, consider, discuss.
PHD_mackenzie.txt:6260:  osmurdan, uskardan.                        corner gosag.
PHD_mackenzie.txt:11913:xwastiig                  \.sne» to'"      uskardan                 ,,~,U)ya
=== NYB ===
NYB_vol2_glossary.txt:3856:uskār [^wsk?l] consideration, deliberation : 6 ~ kartan to take into consideration, with inf. 10913; speculation 109%,
NYB_vol2_glossary.txt:3857:uskārišn [~-8n'] theoretical speculation 10924-27. as opposed to apécakéh 1101 [consideration: pat ~ ki... considering that, taking into account that Vd. 7?$, comm. (p. 255). 75? comm. (279)].
NYB_vol2_glossary.txt:3858:uskürtan to consider, to deliberate, to discuss: apāk spähpatän uskärt u cärak i... ntkérit he deliberated with the generals and examined the means for ... KnS VL20; Burzak u Burz-ätur 6 peš xuäst, apük uskart he summoned B. and B.and deliberated with them KnS VIII,2; har i-š... pat kirpak uskāri estet. . . han ti.š pat vinds uskdrt éstét everyone who has (reflected upon =) got an idea of virtue . . . of sin Vd. 3% comm. (p. 99); api-š pat kirpak an-iskārīt ['nsk?lyt'] éstét and (if) he has not got any idea of virtue ibd. 3% comm. (p. 94) - Belongs undoubtedly to Av. (448) ?kar-, v. ?kartak, *kartan, hangärtan, nikeritan, patküritan. — "ws- can only be the old prev. us-, which would, it is true, appear here as as-. There are, however, some ws. which have preserved us-, either because they were learned ws. or because the prev. had lost its original character. Paz. auaškardan, xuaškdirišn, where x"a$- can scarcely be phonetically explained from ^w8-. Possibly an aspirated pronunciation
NYB_vol2_glossary.txt:7390:sikāl, sigāl: uskārtan
```


## [2026-09-14T01:59:29.809Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15780,15840p' CHEUNG.txt"
}
```


### [2026-09-14T01:59:29.865Z] TOOL RESULT

```
2.25, V 2.28, У 2.30), impf. IND. 3sg. (?) YAv. frakoronaot (V 22.2); Aor. athem.: INJ. 3sg. OAv. cörot 
(Y 44.7, ? Y 45.9), SUBJ. 1sg. OAv. carani (Y 44.17), 3sg. OAv. caraiti (Y 51.1), OAv. carat (Y 46.4), 
OPT. 3sg. ? OAv. coirit (Y 45.9, Kellens — Pirart 1991: 193), IMPV. med. 250. OAv. korosuua (Y 40.1); 
Perf.: IND. 3pl. YAv. *caxrara (V 4.46); Partic.: pres. YAv. koronuuant- (Fr.), perf. pass. YAv. ?korota- 
(Y 26.9, Yt 10.128, V13.23, V 19.30), etc.; Pass.: pres. IND. 3sg. Y Av. kiriieiti (Yt 10.111), 3pl. ҮАУ. 
kiriieinti (V 3.9). © The form YAv. koronüsi can also interpreted as (emend.) med. 2sg. "koronüse, 
Hoffmann - Forssman 1996: 215. 

*OLD PERSIAN: kar- ‘to do, make, build’ — Kent: 179a 

Pres. nu- IND. 3sg. kunautiy <ku-u-n-u-ti-y> (DNb 24), <ku-u-n-u-[t]-[iJ-[y]> (DSs 3), 
<[ku]-[u]-[n]-u-t-i-y> (055 4), impf. lsg. akunavam <a-ku-u-n-v-m> (A’Sd 3), akunäm 
<[a]-[ku]-[n]-a-m> (XSc 3, ? A?Ha 5), ? akuvanasäsa <a-ku-v-n-8-a-8> (A’Sde 3), 3sg. akunaus 
<a-ku-u-n-u-8> (D'Sb 3), akunas <a-[ku]-u-n-8> (A’Sa 3 f), 3pl. akunava", med. 3pl. akunava"tà 
<a-ku-u-n-v-t-a> (DB 3.12, DSf 48), <a-[ku]-[u]-[n]-[v]-t-a> (DB 5.6), SUBJ. lsg. kunavanaiy 
<ku-u-n-v-a-n-i-y> (081 4), 2sg. kunavahy <ku-u-n-v-a-h-y> (DB 4.75, DB 4.79), med. 3sg. kunavätaiy 
<ku-u-n-..-v-a-t-i-y> (DNb 56), IMPV. 3sg. kunautuv <ku-u-n-u-tu-u-v> (DB 4.76); Aor. athem.: IND. 
med. 3sg. akuta <a-ku-u-t-a> (DB 1.47, CMb 4), I pl. akumä <a-ku-u-m-a-> (DB 1.90), IMPV. med. 2sg. 
kuSuva <ku-u-8-u-v-a> (DNb 50); Perf.: OPT. 35р. caxriyä <с-х-г-і-у-а> (DB 1.50); Partic.: perf. pass. 
karta-; Inf.: cartanaiy <c-r-t-n-i-y> (DB 1.94, DB 2.33, DB 2.44, etc.), <c-r-t-n-i-y> (2.38), <c-r-t-n-i-y> 
(DB 3.43, DB 3.65); Pass.: impf. IND. 3sg. akunavayatä <a-ku-u-n-v-y-t-a> (DB 1.20, DB 1.24, akariya 
<a-k-r-i-y> (DSf 37, XPh 42), 3р1. акагіуа"іа <a-k-r-i-y-t-a> (DB 3.92), OPT. 3sg. kariyais <k-r-i-y-i-8> 
(DNb 9, DNb 11) 

*MIDDLE PERSIAN: MMP kwn-, qwn-, BMP kwn- (‘BYDWN-) /kun-/ ‘to make, do’ || 
(+ *us-) BMP ’wsk’l- /uskar-/ (caus.) ‘to think, consider, discuss’ || (+ *pati-) BMP 
ptk’1/pahikar-/ (caus.) ‘to request, claim, consult, MMP phykr, BMP ptkl /pahikar/ 
‘picture, image’, MMP phyk’r, BMP рік? /pahikar/ ‘battle, struggle’ || (+ *ni-) 
MMP ng’r- (caus.) ‘to paint, draw’, MMP ner ‘picture’ || (+ *ui-) MMP w(y)c’r- 
(caus.) ‘to separate, divide, spread, interpret, decide....; perform, accomplish’ || (+ 
*ham-) MMP hng’r- (orig. caus.) ‘to (ac)count, reckon’, BMP hng’l- /hangär-/ ‘to 
perform, offer (thanks); calculate, determine; consider > DMMPP: 213b f., 275a, 
240b, 351b, 181a 

Widely attested: Pres.: IND. 1sg. MMP qwnym, "kwnym, 3sg. MMP kwnyd, etc.; Partic.: pres. MMP 
kwn'n, perf. pass. MMP qyrdg, MMP kyrd, дуга, Pass.: pres. IND. 3sg. MMP kyryhyd, 3р1. MMP 
qyryhynd, SUBJ. 3sg. MMP qyryh'd || (+ *us-) Caus.: pres. IND. 3pl. BMP ’wsk’lynd /uskarénd/, 


*kar 237 


sk’lynynd /skarénénd/; Partic.: perf. pass. caus. BMP ’wsk’lt /uskard/ || (+ *pati-) Caus.: pres. IND. 3pl. 
BMP ptk’lynd /pahikarend/ || (+ *ni-) Pres.: IND. 3sg. MMP ng’ryd, 3р1. MMP ng rynd; Partic.: perf. 
pass. MMP ng’rd || (+ *ui-) Pres.: IND. 3sg. MMP we’ryd, IMPV. 2sg. MMP we’r, Partic.: perf. pass. 
MMP wyc’rd || (+ *ham-) Caus.: pres. IND. 35р. BMP hng’lyt /hangaréd/, 3р1. MMP hng’rynd, BMP 
hng’lynd /hangarénd/; Pass.: pres. IND. 3pl. MMP hng’ryhynd (M7983 I Vii,11); Partic.: perf. pass. BMP 
hng’It /hangard/ 

*PARTHIAN: kr- ‘to do, make’ || (+ *pati-) pdk’r- ‘to contend, strive’, pdkr ‘picture’ || 
+ *fra-) ? ‘frg’r- ‘to be dejected’ || (+ *ni-) ng’r- ‘to paint, draw’, ng’rgr ‘painter’ || 
(+ *ui-) wyc’r- ‘fulfil, perform’ = Ghilain: 57, 73 f. | DMMPP: 207 f., 269b, 85b, 
351b 

Pres.: IND. Isg. kr’m, 25р. qryh, 35р. kryd, qryd, 1р1. “kr’m, 2р1. Куа, 3р1. krynd, qrynd, SUBJ. 1sg. 
kr’n, 25р. kr’h, 3sg. kr’h, OPT. 25р. qryndyh, IMPV. 2sg. kr, 2pl. kryd; Partic.: perf. pass. kyrd; Inf.: 
kyrdn, qyrdn || (+ *pati-) Pres.: IND. 3pl. pdk’rynd || (+ *fra-) Pres.: IND. 1pl. ‘frg’r’m || (+ *ni-) Pres.: 
IND. 3sg. ng ryd || (+ *ui-) Pres.: IND. 25р. wyc ryy, 3sg. we’ryd, wyc’ryd 

*KHOTANESE: yan- “о do, make’ || (+ ui-) LKh. güjsar- ‘to harm, injure? = SGS: 
110 £, 29
```


## [2026-09-14T01:59:42.781Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15927,15960p' CHEUNG.txt"
}
```


### [2026-09-14T01:59:42.852Z] TOOL RESULT

```
*karH2 239 


*KHOTANESE: kalj- ‘to strike’ || (+ *us-) OKh. uskaljaka- ‘opener’ || (+ *nis-) 
naskalj- ‘to drive away’. 0 The suggestion of Bailey (DKS: 55b) to connect the 
Khot. verbs to Av. kahrkäsa- ‘eagle’, etc. can be discarded. = SGS: 17, 21 

© An Ir. origin for these relatively isolated forms is doubtful. 

*PIE— > LIV: — | Pok.: 


*kard ? ‘to stick, keep down ?’ 

*CHORESMIAN: ? Krö- ‘to sink (in the dust), subside’ (i.e. ‘to get stuck (in the dust)’ 
?) || (+ *upa-) ? bkrry- (i.e. /bkrzy-/ ?) “о attack, grab, seize violently’ (MacKenzie, 
V: 67) > Samadi: 103 f., 20 f. 

*BACTRIAN: ? Kap(a)A- ‘to detain, arrest’ || (+ *pati-) mdoKapA- ‘to withhold, 
retain, detain’ = S-W, Bact.: 198a, 218a 

*NWIR: ? NP kal ‘ditch, valley’ (different etym. ?, from *karH? ?) 

*NEIR: ? Wa. korovir ‘layer of duckweed or mud on the water’ 

9 This root seems to be exclusively Ir. An IE provenance cannot be established. 

*PIE— > LIV: – | Pok.: 


*REFERENCES: Steblin-Kamenskij 1999: 218 


*karH! ‘to celebrate, praise’
```


## [2026-09-14T01:59:46.210Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15855,15918p' CHEUNG.txt | grep -n \"sigal\\|NP \\|PIE\\|Pok\" "
}
```


### [2026-09-14T01:59:46.273Z] TOOL RESULT

```
10:*NWIR: Widely attested: NP kardan/kun-, Bal. kan-/ku(r)t-, Kurd. (Kurm.) kirin/ki-, 
28:be done’ || (+ *us-) NP sigälidan/sigäl- ‘to think, meditate (mischief)’ || (+ *pati-) NP 
29:paykar ‘picture, statue’ || (+ *ni-) NP nigastan/nigar- ‘to paint’ || (+ *ham-) NP 
33:Natan. -hängäst ‘to talk, speak’, NP angärah ‘revenue-book, cash-account’ 
40:enk’aryn/enk’ard (pref. sec. ?), D. ank’arun/enk’ard ‘to feel, comprehend’ (< NP 
51:*PIE *k”er- ‘to do, make, construct’? = LIV: 391 | Pok.: 641
```


## [2026-09-14T01:59:56.970Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nfor f in ('FFD_pages.txt','FFD_pages_faseng.txt'):\n    try:\n        t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    except Exception as e:\n        print(f,e); continue\n    print('#####',f,len(t))\n    print(t[65][:2500])\nEOF"
}
```


### [2026-09-14T01:59:58.117Z] TOOL RESULT

```
##### FFD_pages.txt 115
[pdf page 66]
ماده‌های ماضی و مضارع فارسی دری _ ۶

سرای < فارسی میانه 8737 + ایرانی باستان ۹73۷-۵98*. 272 نشانه‌ای بوده که برای
ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ۶739 صورت بالاندةٌ ريشهٌ 872۷ است.

امروزه مشتقات «سرای» را به ضم «س»» به قیاس با «سرود»» تلفظ می‌کنند. این
قیاسی نادرست است. «س)» را باید به فتح خواند.

دا :

سفت < فارسی میانه 8011 < ایرانی باستان ۶۷1-1۵*. برای 12 -> آراست. 0اه صورت
اصلی 9۷۶ است» 0 پیش از به ۶ بدل شده است. ۶0 صورت ضعیف 820 است و آن به
معنی «آراستن» است.

ستب ه فارسی میانه 5010 + ایرانی باستان ۴*۹8 پیش از آخرین صامت ريشه:
برای ساختن مادهٌ مضارع.از ريشه» افزوده شده است. «نهفتن» هم از ريشةٌ 9۷0 آمده
است > نهفتن.

سکالیدن

«سگالید» ماد ماضی جعلی است. از مادةٌ مضارع ساخته شده است.

سگال + فارسی میانه 913۶ < ایرانی باستان ۶-137-۵*. برای 2 > آرای. 8 پیشوند
فعلی است. 137 صورت بالاندةٌ ریشه است. صورت افزودهٌ آن 187 است» به معنی
«اندیشیدن». ۱

مادهٌ ماضی ۶27۲ در فارسی میانه 81370 است» از ایرانی باستان ۶۵-۷3۶-12. برای
> 12 آراست.

سوختن ِ

سوخت + فارسی میانه 9071 + ایرانی باستان ۶۵-۱۵*. برای 2 > آراست. 521
صورت اصلی ۶27 است» ۴ پیش از ابه # بدل شده است. ريشةٌ 920 به معنی
(سوختن) است.

سوز <فارسی میانه 952 « ایرانی باستان 8۵06-۵*. برای 2-> آرای. تبه جای ۲ آمده
است.

FFD_pages_faseng.txt [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-14T02:00:13.710Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN xuk ===\"; grep -n \"chūk\\|ḫūk\\|hûk\\|xûk\\|Schwein\" HRN.txt | head -15"
}
```


### [2026-09-14T02:00:13.769Z] TOOL RESULT

```
=== HRN xuk ===
4609:510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
4612:skr. siikard- 'Eber, Schwein*.
```


## [2026-09-14T02:00:15.409Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"Schwein\\|ḫūk\\|hūk\" HUB.txt | head -15; echo \"=== HRN sigal ===\"; grep -n \"sikāl\\|sigāl\\|sikālīdan\\|sigālīdan\\|sikal\" HRN.txt HUB.txt | head"
}
```


### [2026-09-14T02:00:15.489Z] TOOL RESULT

```
=== HUB ===
7638:xUk Schwein' = phi. xUk 61. and Ind. 53 = zd. hu-; xujlr
8589:(nom.); dig gestern' (neben di), bal. zlk; xug 'Schwein
=== HRN sigal ===
```


## [2026-09-14T02:00:17.732Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4605,4616p' HRN.txt; echo \"=== HUB ctx ===\"; sed -n '7630,7645p' HUB.txt"
}
```


### [2026-09-14T02:00:17.823Z] TOOL RESULT

```
bei Fr. Müller, WZKM. 5, 352.
509. yiiisnüdj x^snü zufrieden, fröhlich*.
aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
/iisnüt, /usnütik (AV.).
510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.),
yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51);
skr. siikard- 'Eber, Schwein*.
kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310);
bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug,
511. //rn 'Blut', yümn.
aw. vohuni' *Blut'; phlv. yün, yUnömaud,
=== HUB ctx ===
'trocken' = ap. {h)uska', zd. huska- ; Xusrav = arm. Xosrov
— zd. husravah-; Xuzistan = arm. Xuzastan, ap. (A)w2?ia-;
^) Dass die Grieohen das vor a, i anlautende ap. h immer durch
den Spiritus lenis wiedergeben: ""AoaxtoaCa = HarauvatiS; ^Axaijuivrji =
HaxUmanii; ^Ay^aTava = Hagmat&na'] *Jv8(a — Hindui etc., ist nioht
Ton Belang.— 215 —
xusnud zufrieden' = zd. ^huxs^iiUa- (vgl. huxsnUiii-) oder
xusnUd = x^asnUd = zd. ^x^axsnuta- (siehe oben p. 58);
xUk Schwein' = phi. xUk 61. and Ind. 53 = zd. hu-; xujlr
(neben hujlr, hmlr) 'schSn' = zd. httdid^'a-; xUb *sch5n' =
skr. suvapus' (oben p. 57); xujasta gesegnet, gliicklich' =
zd. ^hujasta-; xurram^) *fr5hlich*, s. oben p. 55.
Ueber xun *Blut' siehe oben p. 58; iiber a?fm oben
p. 59 ; iiber vorgeschlagenes x Kap. 31 ; iiber xu- = a?^a-
§ 108.
Dagegen blieb u in den erwahnten huilVj hujtr sch5n'
```


## [2026-09-14T02:00:32.315Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ebergestalt\\|hū-kǝhrpa\\|hu.kahrpa\\|Eber'\" BRT.txt | head -10; echo \"=== BRT hu- Eber ===\"; grep -n \"'Eber\\|Eber,\\|Schwein'\" BRT.txt | head -12"
}
```


### [2026-09-14T02:00:32.466Z] TOOL RESULT

```
22823:Eber',
24292:allenthalben  gebietend',  vi-rät-;  aL  viraj-  m. 'Herrscher',  auchEN. ,  np.  fariaEN.»);  oder aber:  'Qber  Männer  gebietend',  haplol.  aus »viTa-räz-l).  —  ')  Them.  —  •)  Der  jedenfalls nicht  notwendig  'Eber'  bedeuten  muss.  — 3)  Statt  ar4äi  viTäfi^KVÜ)  ist  vielmehr  artak [Sp.  353  No.l2)i/i>-ä.3u  lesen.
=== BRT hu- Eber ===
24292:allenthalben  gebietend',  vi-rät-;  aL  viraj-  m. 'Herrscher',  auchEN. ,  np.  fariaEN.»);  oder aber:  'Qber  Männer  gebietend',  haplol.  aus »viTa-räz-l).  —  ')  Them.  —  •)  Der  jedenfalls nicht  notwendig  'Eber'  bedeuten  muss.  — 3)  Statt  ar4äi  viTäfi^KVÜ)  ist  vielmehr  artak [Sp.  353  No.l2)i/i>-ä.3u  lesen.
30174:VJ(AP.),  •ralibyU,  'ranqm  -.  Unklar: nSii  ^mairyeke  nSi^  Jahtkayh  tait  sünü  tOii 'rahe''>  V.io. Ableit  —  d.  lui/aträ-  Adj.  —  VgL  den  ^, EN. 'OJ«Vlt  1*- —  Pü. :  »"fl/üi ;  s,  noch  No.  3.— 0  iSt  s.  Bthl.  KZ.  aS.  11;  weitere  Litt,  bei JusTi  PrJ.  S8.  247,  woEu  noch  Gdn.  BB.  13. 9tS.  —  1)  Scheint  ein  andres  Wort  verdrängt lu  haben;  Pü.:  AüA  'Schwein'.  Dst.  ZA.  j. SS  vriU  freilich  "le  roi  des  porcs".  —  3)  S. übrigens  zu  uxsya{jr>la-.
```


## [2026-09-14T02:00:37.663Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30145,30160p' BRT.txt; echo \"=== 22820 ===\"; sed -n '22818,22828p' BRT.txt"
}
```


### [2026-09-14T02:00:37.794Z] TOOL RESULT

```
Eig.  'des  Amt,  Tätigkeit  gut  ist'.  —  >)  Mit  ü
Vt.  IQ.  88.  —  »)  S.  •).  —  J)  Vgl.  die  Noten
lu  zgad:
•  j.  hu-lrarsta-,  g.  ^hü.kamta-"  Adj. (fem.  °ta-)  "wohl  gefertigt,  schön  gefonnt (usw.)'i  a)  von  Sachen:  %anvar3itittqm  . . •ianqm  Yt.  iO.  laS;  119-13JS;  — '/«'(IS.) .  .  aia  (sd.)  Yt  jo.  12$;  —  iaÄe  vaca vanäi  kahe  vaca  apa.yasäi  kana  zaya "'tarfhs'^  mana  äama  V./^.S;  ^i^pusqm ..'iqm  YL5.  izS;  —  gäiava  . . 'ta  I^ol.) Yt  ly.  9;  —  nmätam  .  .  htihatfm  .  .  't?m Yt  5. 101 ;  —  mit  Instr.  des  Urhebers:  tJm advätum  .  ,  yä  *'til  (IS.)  asäcU  urvaxiat (Sp.  1536  o.)  Y.^.^.13.  b)  von  Per- sonen: srJrS  . .  'ta  ahi  spitama  hvatlvB Yx.i-j.ii.
ai.  süi^la-  Adj.  —  Pü, :  huiarl,  xüp  karl,  (la Y.  34)-  po  hakarlärlh.  —  ')  NA.  kü.karHä; s.  aber  R  4  und  wegen  der  Bedeutung  du vorherg. /taiö  ..  ^aShig.  —  »)  Man  verlangte den  IS.
•  j.  hu-kshrp- Adj. 'wohlgestaltet':  vatihus haomS  .  .  'kfnfi  Y.p.  16;  F.  ja.
Ableit.  — Pü.;  hukarp,  erl.:  fisSn  (xüplA) pata- lailAä  i  handäm  'gemeint  ist  (Schönheil)  in Beziehung  auf  die  ZusammenstelluDg  der Glieder';  vgl.  hulasta.,  Imraoia:
•  j.  hu-kanpta-  Adj.  'schöngeformt':  hs (näml.  andvt)  hl  maiiim  nyanata  ya%aid 'ta  (NDm.)  fsiSna yähaca  aifhm  ntvaxäna
Yt5.n7-
"kinpta-  Adj.,  PPtP.  mm  ai.  V.  kilpate;  ai. ilpiä-  Adj.  —  Vgl  np.  kulba  'Bude',  arm.  LW. kr-pak  'Werkstatt',
•  j.  huksrap'tsma-  Adj.  (fem.  'mix-')  'der
wohlgestaltetste':  ahurahe  mazdä  .  .  'ma- heca    Y.  I.  i;    —    fravallnt    avqm    yqm ahurahe  masda  .  .  •mqmca  Y.  26.  a. Pü. :  htitarplum,  erl. :  hii  hatidäm  eBok  5  diß-
db,Google
iSit)  hugaona-
kar pasacakluni  -  Sä.:  Üläsya  an^ni  anyonyam
j.  huii  H.  g£:  Um  hiiu.
=== 22820 ===
-  Vgl.  :
■i  V.  a
.  6:    lit:
'iar-,  Sp.  936  U
'varäza-  m.  'Männchen  des  Schweins, Verbindung  mit  dem  Namen  für
Eber',
Schwein"':  As(sd.)  k»hrpa  'zähe , .  arÜnS*''
hakirH.janS  'räzahe  Yt  1.^.15. 1  Vgl.~»iwfläa.  EN.  —  ai.  wflj-ä-ia- m.,  np.fNpO.) guräi.  —  ')  R.  zu  tarian-  No.  3  und  oaai [  KÖieptm  E  783.  —  ')  Zur  Verbindung  von 1  varäta-  mit  arlan-  s.  vfiabkir  varähäih  RV. I       TO.  67.  7.
•  j.  »varäza-   m.  EN.   eines  Gläubigen: iivatö  'zahe  asacnS  Yt.  y.  96.
I  Vgl.  ^varäia-.     —    ai.   varähA-    m.    EN.,    np.
!  baräa  EN.
```


## [2026-09-14T02:00:47.802Z] TOOL CALL #48: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:00:47.813Z] TOOL RESULT

```


```


## [2026-09-14T02:00:50.810Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%DA%A9",
 "prompt": "Give the Persian entry خوک: etymology (Middle Persian, Proto-Iranian, PIE reconstructions), meaning, and any cognates cited."
}
```


## [2026-09-14T02:00:53.344Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%A7%D9%84%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian entry سگالیدن: etymology (Middle Persian uskārdan, prefix us-, root), meaning, related terms like سگالش, and any alternative spellings سکالیدن."
}
```


### [2026-09-14T02:00:56.499Z] TOOL RESULT

```
# Persian Entry: خوک (xuk)

## Etymology
The word traces back through several ancient language layers:

- **Middle Persian**: hwk' (/⁠hūg⁠/) 
- **Proto-Iranian**: *huHkáh
- **Proto-Indo-Iranian**: *suH-
- **Proto-Indo-European**: *suh₂kéh₂, derived from *suH-

## Meaning
"Pig" — The entry provides an example: "I don't eat pork" (man gušt-e xuk nemi-xoram).

## Cognates
The word is "possibly cognate with English hog," according to the dictionary entry.

## Notable Information
The entry lists alternative forms (خوگ/xug) and derived terms like خوکچه (xukče, "piglet"). The word has descended into numerous languages including Central Kurdish, Gujarati, Hindi, Urdu, Northern Kurdish, Pashto, Turkmen, and others, demonstrating its wide linguistic influence across Persian-speaking and neighboring regions.
```


### [2026-09-14T02:00:57.873Z] TOOL RESULT

```
# Persian Entry: سگالیدن (segâlidan)

## Etymology
The word derives from Middle Persian *uskārdan* ("to think, consider"), ultimately tracing back to Proto-Indo-Iranian *\*kar-* ("to do, make, construct") and Proto-Indo-European *\*kʷer-*.

## Meaning
This is a **literary verb** meaning "to think, consider, discuss."

## Related Terms
Synonymous expressions include:
- اندیشیدن (andišidan)
- فکر کردن (fekr kardan)

## Alternative Spellings
The page indicates related forms like سگالش, though alternative spellings such as سکالیدن may exist in variant Persian orthographies.

## Pronunciation Notes
The word has multiple dialectal pronunciations across Classical Persian, Dari, Iranian, and Tajik variants, with the standard literary reading being *segâlidan*.
```


## [2026-09-14T02:01:02.063Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%84%DB%8C",
 "prompt": "Give the Persian entry سیلی (sili): etymology if any, meaning (slap), and any Middle Persian or Indo-European reconstruction mentioned."
}
```


## [2026-09-14T02:01:02.695Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ski",
 "prompt": "Give the full etymology of \"ski\" — Norwegian, Old Norse skið, PIE root, date of borrowing into English and French."
}
```


### [2026-09-14T02:01:05.991Z] TOOL RESULT

```
# سیلی (sili) - Persian Entry

**Meaning:** The entry defines this noun with two primary meanings: a "slap (in the face)" and a "musical stringed instrument."

**Etymology:** The Wiktionary page does not provide an explicit etymology section for this Persian term.

**Historical Reconstructions:** No Middle Persian or Indo-European reconstructions are mentioned in the provided content. However, the page does document linguistic descendants across multiple languages, showing the word's spread into Azerbaijani (sillə), Georgian (sila), Ottoman Turkish (sille), Armenian (silla/sille), and modern Turkish (sille), suggesting historical significance in regional language contact.
```


### [2026-09-14T02:01:07.993Z] TOOL RESULT

```
# Etymology of "Ski"

**Origin and Borrowing Date:**
The term entered English in 1883 from Norwegian *ski*, with an isolated earlier instance from 1755.

**Etymology Chain:**
Norwegian *ski* derives from Old Norse *skið*, meaning "long snowshoe," literally "stick of wood, firewood." This connects to Old English *scid* ("stick of wood") and German *Scheit* ("log"), all stemming from Proto-Germanic *\*skid-* ("to divide, split"), ultimately tracing to the PIE root *\*skei-* meaning "to cut, split."

**French Borrowing:**
The web page provided does not include information about the word's adoption into French, so this cannot be addressed based on the source material.

**Historical Reference:**
An 1885 college publication describes the sport: "They are long ash planks, carefully planed and turned up at the end," documenting early English usage of this Norwegian-derived term.
```


## [2026-09-14T02:01:11.673Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84",
 "prompt": "Give the Arabic entry غربال (ḡirbāl) and the Persian entry if present: etymology (Latin cribellum? Aramaic? Greek?), meaning sieve, and the verb غربل."
}
```


## [2026-09-14T02:01:12.942Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carnival",
 "prompt": "Full etymology of carnival: Italian carnevale, Medieval Latin carnelevamen/carnelevare, caro/carnis, French carnaval, date."
}
```


### [2026-09-14T02:01:17.431Z] TOOL RESULT

```
# غربال (Sieve) - Etymology and Definitions

## Arabic Entry (ḡirbāl)

**Etymology:** The word derives from Aramaic *ʿarbālā*, possibly originating from the Hurrian period. As the source states: "Possible a culture-word left from the Hurrian period in Nuzi from which sieves have been excavated."

**Meaning:** A sieve, riddle, strainer, or sifter used for filtering or separating materials.

**Derived Verb:** غَرْبَلَ (ḡarbala) - "to sift"

## Persian Entry (ġarbâl)

**Etymology:** Borrowed from Arabic غِرْبَال, which itself traces back through Aramaic to Hurrian origins.

**Meaning:** Identical to Arabic - a sieve, riddle, strainer, or sifter.

**Alternative Forms:** غربیل (ġarbil), غلبیر (ġalbir), گربال (garbâl)

## Note on Origin

The documentation indicates the word is **not** from Latin *cribellum* or Greek, but rather from ancient Aramaic with possible Hurrian substrate origins, supported by archaeological evidence from the ancient site of Nuzi.
```


### [2026-09-14T02:01:17.500Z] TOOL RESULT

```
# Carnival Etymology

The word "carnival" originated in the 1540s from French *carnaval*, which came from Italian *carnevale*, meaning "Shrove Tuesday." 

The Italian term derived from older forms like Milanese *carnelevale* and Old Pisan *carnelevare*, literally meaning "to remove meat." This reflected the religious practice of abstaining from meat during Lent.

The word breaks down into two Latin components: *caro* meaning "flesh" and *levare* meaning "to lighten, raise, or remove." A folk etymology suggests it comes from Medieval Latin *carne vale*, interpreted as "'flesh, farewell!'"

By the 1590s, the term expanded figuratively to describe "feasting or revelry in general." Its modern meaning—"a circus or amusement fair"—emerged by 1926 in American English, eventually giving rise to the related slang term "carny" for carnival workers in 1931.
```


## [2026-09-14T02:01:27.522Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA (Fraenkel) ===\"; grep -n \"girbāl\\|girbal\\|ġirbāl\\|Sieb\\|arbālā\\|arbala\" AFA.txt | head -20"
}
```


### [2026-09-14T02:01:27.581Z] TOOL RESULT

```
=== AFA (Fraenkel) ===
3563:Ein anderes Wort für »Sieb" Jü«x hat Lagarde
5588:ter >) sagt Tom Siebengestirn , das am Morgen erglänzt ,
9904:allerdings die Wurzel sehr beliebt. Sieber aber ist die
```


## [2026-09-14T02:01:29.003Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT 673 ===\"; grep -n \"cribellum\" LKT.txt | head; echo \"=== SKT garble ===\"; grep -n \"garble\" SKT.txt | head -3; echo \"=== AFM غربال ===\"; grep -n \"غربال\" AFM_pages.txt TAD_pages.txt | head"
}
```


### [2026-09-14T02:01:29.110Z] TOOL RESULT

```
=== LKT 673 ===
7427:earuba  832 carumba  832 Castrum  1117 cavilla  980 census  1050 centenarius  1178 cephalica  (vena)  1172 cer  Villa  1095 ciccum  434 cimiabaris  1827 cintra  1057 commercium  751 cophinus  1225 cribellum  673 cromm  1247 cummum  1046 cuppa  1225 cnpresstis  727 ci/c^as  1794.  1905 cywa  445 t«/^oZa  442
=== SKT garble ===
7405:Garble,  to  select  for  a  purpose;  hence, to  corrupt  an  account.  (F.  *  Span.  —  Arab.) Orifi.  to  pick  out,  sort,  sift  out.  —  O.  F. mrheUr*  (not  found),  the  same  as  gm- PttUr,  to  garble  spices,  or  sort  them  oat, orig.  to  sift.  The  same  as  Span  gurhiUar^ \\i^  gurhtUtkrtt  10  garble  or  sift  wares.— Spun.  gMrHliOt  a  coane  sieve.— Pen.  ^lUr*
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
=== AFM غربال ===
```


## [2026-09-14T02:01:31.967Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# offset leaf = printed + 26\nfor leaf in (698,699):\n    print('##',leaf)\n    print(t[leaf][:1500])\nEOF"
}
```


### [2026-09-14T02:01:33.812Z] TOOL RESULT

```
Exit code 1
## 698
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-14T02:01:36.685Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"673\" LKT.txt | grep -i \"girbal\\|garbal\\|cribel\" | head; echo ===; grep -n \"girbal\\|ġirbāl\\|gurbal\\|garbal\" LKT.txt | head"
}
```


### [2026-09-14T02:01:36.752Z] TOOL RESULT

```
Exit code 1
7427:earuba  832 carumba  832 Castrum  1117 cavilla  980 census  1050 centenarius  1178 cephalica  (vena)  1172 cer  Villa  1095 ciccum  434 cimiabaris  1827 cintra  1057 commercium  751 cophinus  1225 cribellum  673 cromm  1247 cummum  1046 cuppa  1225 cnpresstis  727 ci/c^as  1794.  1905 cywa  445 t«/^oZa  442
(eval):1: == not found
```


## [2026-09-14T02:01:40.436Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^673\\.\\|673\\.\\s*[a-zġ]\" LKT.txt | head -5; echo ===; grep -n \"garbillar\\|garbell\\|crivello\" LKT.txt | head"
}
```


### [2026-09-14T02:01:40.540Z] TOOL RESULT

```
Exit code 1
1666:673.  Ar.  garbäl:
(eval):1: == not found
```


## [2026-09-14T02:01:42.156Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1660,1690p' LKT.txt"
}
```


### [2026-09-14T02:01:42.264Z] TOOL RESULT

```
'Geschwulst',  insbesondere  eine  knochen- harte Anschwellung  am  hinteren  Rande
des  Sprunggelenks  der  Hinterbeine  des Pferdes  [Hasenhacke  oder  Hasenspat, vgl.  Theodor  Heinze,  Pferd  und  Reiter. 6.  Aufl.  Leipzig  18S9.  S.  75];  hieraus it.  ginrda,  zarda,  zerda,  frz.  jarde, jardon  'dsLSS.\  [DevicDEL143.  ML3943.
671.  Ar.  garänia:
'Steuer' ;  hieraus  sp.  pg.  garrama  'Steuer, Abgabe,  Raub,  Erpressung'.  [DE  275. Eguilaz  410.    ML  3680.
672.  Ar.  garas:
'Glocke,  Klingel';  hieraus  mit  ar.  Art. sp.  aljaraz.  (dial.)  nljarges,  aljorses. [DE  145.    Eguilaz  203.    ML  3943  a.
673.  Ar.  garbäl:
Klassisch-ar.  girbäl  'Sieh'  [dem  lat.  cri- öeZZtw  merkwürdig  ähnlich] ;  hieraus  siz. garhula  'Sieb,  Kasten  der  Trommel',  it. garhellare  'durchsieben'  (z.  B.  die  klein- sten Stücke  einer  Droge),  gavhellatura 'die  kleineren  Stücke  einer  Ware,  die durch  das  Sieb  hindurchfallen',  ebenso frz.  grabeler,  graheaii,  sp.  garhillo  'Sieb'. —  Aus  mit  Imäla  gesprochenem  garbel ergab  sich  sp.  arel  'großes  Sieb'. [GrSVociSic  238.  DE  188.  198.  274. Devic  DEt  132.    ZtVlWf  XI,  9/10.
674.  Ar.  garbi:
'Westlich';  hieraus  il.garbino,  frz. garbin 'Südwestwind'  auf  dem  Mittelmeere, prov.  garbin,  sp.  garbino  'Süd-  oder Westwind',  sp.  pg.  algarve  'fruchtbar', pg.  garabia  'Westen'.  Aus  dem  It. wurde  serb.  garbin  'Südwind'.  Jeden- falls mit  Kontamination  von  al-  arabija 'die  arabische  Sprache'  entstand  pg.  al- garabia,  pg.  algravia,  frz.  charabia  'un- verständliches Zeug,  Kauderwelsch',  frz. insbesondere  'Dialekt  der  Auvergne'.  — Aus  demselben  Stamme  ar.  garaba 'untergehen  (Sonne)'  ist  mit  präfigiertem ma-  zur  Angabe  des  Ortes  magrib  ge- bildet; der  Magreb  ist  Nordwestafrika von  Tunis  bis  Marokko;  ms  al-magribl 'der  Bewohner  des  M.'  wurde  irz. maugrebin  'dass.'.  —  Auch  der  Name der  pg.  Provinz  Algarve  ist  ar.  garb 'Westen',  daher  sp.  algarabio,  algarabia, pg.  algaravio  'Bewohner  von  Algarve'. [DE  119.  241.  Eguilaz  178.  Devic  DEt 125.    ML  3683.    Bern  SlEtWb  295.
675.  Pers.  gärdän:
'Hals,  Nacken'  [Horn  NpEt  S.  201 ,  Nr.  903], ebenso  tk.  gerden  'dass.,  Halsband'; hieraus  rum.  gherden,  ghiordan  'Hals- band, Perlenschnur',  bulg.  gerdan,  serb. dierdan  'Halsband',  kliuss.  garda 'Schmuck,  Zierat'.
676.  Ar.  garf:
'Fülle  des  Grases;  trockenes  Kraut'; hieraus  siz.  gerfa  'hoch  geschossene Pflanze'.    [GrSVociSic  238.
Pers.  gäigängä.]
54
677.  Pcrs.  g::irgäii^ä:
'Mulier  eoilu  iiisaliabilis'";  hieraus  an- geblich l'rz.  ffoiirgandine  'feile  Dirne'. [Etymologie  von  PIHAN.]  [Devic  DEt 132.
678.  Ar.  ^arl:
'Jugendlich;  schön,  artig';  hieraus  sp. pg.  garrido  'zierlich,  schön,  artig,  rei- zend'.   [ML  3087.
(579.  Hiud.  gravi: 'Karre,  Wagen' ;  hieraus  angloind.  garry, gharry  'dass.'.    [Hobson  Jobson  3(55.
ü80.  Ar.  garlb: 'Fremd,  seltsam' ;  hieraus  mit  ar.  Art. sp.   algarivo    'ein   Fremder,  schlecht' [nach  DE  l!21  „pas  dans  les  dictionnai- res",  Vgl.  jedoch  Dicc  Gast  121  a].
681.  Ar.  garid:
'Pdlmzvveig  ohne  Blätter,  Speer',  ebenso tk.  gerid,  girit;  hieraus  rum.  gerid 'Wurfspieß',  serb.  dzilit  'Wurfstab',  poln. dziryt  'kurzer  Spieß'.  —  [Über  das Geridspiel  bei  Arabern  und  Türken  vgl. Max  Freiherr  v.  Oppenheim,  Vom  Mittel- meer zum  persischen  Golf.  Berlin  1900. II,  38/39  und  H.  D.  Mordtmann,  Ana- tolien.  Skizzen  und  Reisebriefe  aus Kleinasien.  Eingeleitet  von  Franz  Ba- binger.   Hannover  192.5.    S.  484.]
682.  Ar.  garim:
'Schuldner',  plr.  guramä^,  tk.  gurema als  sglr.  gebraucht;  hieraus  imn.cwama 'Zeche'.
683.  Ar.  garima:
'Verbrechen;  Strafe  dafür',  ebenso  tk. geriin ;  hieraus  rum.  geremea  'Strafe'.
684.  Tk.  gärmsnd:
Vulg.  gemesit  [aus  pers.  gärni  'Avarm' Horn  NpEt  S.  203,  Nr.  911,  und  süd 'Nutzen,  Vorteil'  ebenda  S.  166,  Nr.  751] 'eine  Art  Stoff' ;  hieraus  rum.  ghermesit 'Art  Atlas'.
685.  Ar.  garnait:
```


## [2026-09-14T02:01:51.652Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7405,7412p' SKT.txt; echo \"=== PLA ===\"; grep -n \"ġirbāl\\|girbal\\|غربال\" incoming/PLA/PLA_pages.txt | head; echo \"=== TAD ===\"; grep -n \"غربال\\|غربيل\" TAD_pages.txt AFM_pages.txt | head"
}
```


### [2026-09-14T02:01:51.785Z] TOOL RESULT

```
Garble,  to  select  for  a  purpose;  hence, to  corrupt  an  account.  (F.  *  Span.  —  Arab.) Orifi.  to  pick  out,  sort,  sift  out.  —  O.  F. mrheUr*  (not  found),  the  same  as  gm- PttUr,  to  garble  spices,  or  sort  them  oat, orig.  to  sift.  The  same  as  Span  gurhiUar^ \\i^  gurhtUtkrtt  10  garble  or  sift  wares.— Spun.  gMrHliOt  a  coane  sieve.— Pen.  ^lUr*
GARRET.
W,  Arab.  gAirid/,  a  sicre ;  Arah.  ^Amrh
ttftittg,  seari^hing.
garba^.  remse.  (F.  —  Span.  —  Ai Prob.  for  gar^-^gt ;    »ec  above     CI graUoMt  rcKtse  of  drugs  (.Uttre). OarboU,  a  commotion.  (P'-^L.)    C
ftrbeuiSf  *  a  garboil,  hurliburly ; '  CoL pan.  garhtfh,  a  crowd;  ItaL  ^o^^ a  garboiU  disorder.  From  h.garr-i^ prattle,  chatter;  and  huUirt,  to  boil,  bn| boil  with  rage.  Thns  the  sense  ia  '  aa boiling.'  i.  e.  a  hubbub.  Florio  kai  ] gamimllare,  to  rave.  See  Jar  CO- Garden.  (F.-O.  HG)    M.  E./b«
—  O.  F.  gardin  (F.  jartfi'm).  -OK gartin,  gen.  and  diaL  oi  gaUo,  a  yaid.  1 oate  with  K.  Yard,  q.  r.  (Thegeii.  ap{l al^o  in  O.  H.  G.  gartin-art,  a  gaidend
Gargle.  Gargoyle ;  sec  Gorge.
=== PLA ===
=== TAD ===
```


## [2026-09-14T02:01:59.607Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ===\"; grep -n \"SEK\\|SKEL\\|SKEI\\|SKER\\|KWREP\\|SU-\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T02:01:59.746Z] TOOL RESULT

```
=== ARY latin index ===
2783:MACKENZIE: 61 ASU-, ASUS., (SANSKRIT) oy Site
2785:| (ANSU-) 2021 ANSES (GREER) gly
2819:STANDAN, :(OLD SAXON) oA gat SEKININ ABURDISH) (4\2).59,5
5204:PIRSHYS (LITHUANIAN) gly PARQSU-, PaRQSU- :(AVESTAN) gly!
6398:BARNHART: (SHEAR) 994 SKERA
6399:MACKENZIE: SKERA OLD FRISIAN) S523
7225:SU. SU-DRUS (LITHUANIAN) gly) PAHLAVI) 54,
7226:S0., SU- (OLD IRISH) AS 43 p! HU., XUB, HOP, XvaP, HUDAG eal
7228:HY- (WELSH) 539 SU-, SUVAPUS (SANSKRIT) ©. Sail
7231:SU- «(OLD SCANDINAVIAN) 45 54Leu!
7254:svoju SUI-, SU-, SUS, SE- (LATIN) ysV
7980:DEEG ¥ __{DUTCH) sae TSEKE (TOKHARIAN A) A 5,0
8578:SEYDIS TSEK- (TOKHARIAN A) A 5 jis
9833:SKINA (SWEDISH) (gat y+ SKEINAN GOTHIC) Si
10222:SAKYTI, SEKU, SAKAU SEGJA :
10324:(DROP) 111, (TEAR) 136 SRSKEL ARMENIAN) go \
10340:REFERENCES ntKang SKERN — (OLD FRISIAN) eS 53.5
10563:SAVIRA, SU-AYATI SURA., SISPIMNA  :(AVESTAN) gles)
10880:FE :(OLD SCANDINAVIAN) 46 54th! *FSHU-PAITI, PASU-
10889:DELAMARRE: (BERGER) 52 PASVAH, PASU, FSU-,
```


## [2026-09-14T02:02:01.182Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY خوک ===\"; grep -n \"خوک\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY سگال ===\"; grep -n \"سگال\\|سکال\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY سیلی ===\"; grep -n \"سیلی\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T02:02:01.276Z] TOOL RESULT

```
=== ARY خوک ===
294:«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می‌دهد که این مردم به کشاورزی هم اشتغال"
938:همریشه‌ی مربوط به «اسب» و «گاوه و «گوسفندء و دسگ» و «خوکک؛). همریشگی واژه‌های متعدد
4600:معلی این واژه در ارمنی: ران خوکك.
4931:معنی واژه‌ی .5۳۸۸-۳3681 در زبان آلمانی: خوکك شیرخوار,
7478:خوک ۲۵۵
=== ARY سگال ===
=== ARY سیلی ===
```


## [2026-09-14T02:02:04.096Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('خوک ۲۵۵')\nprint(t[i-3000:i+1500])\nEOF"
}
```


### [2026-09-14T02:02:05.246Z] TOOL RESULT

```
 هو :
۲ این واجريشه بیشتر بعنوان پیشوند بکار رفته است.
اوستایی (4872): فریزی کهن (۶78740 5817۸:)010 ,85817
۷۸707 ,13۸۸ آلمانی کهن (/(022214 1/04 صاه):
۱ پارسی باستان (/۶5781۸ صا0): 3 ,558 ,551230
۸1 ,2۷۸3 آلمانی (08#۵1۵4): 57 ,8812357
پهلری (۲7اتنهه): انگلیسی کهن (بلقل8(۷۵ صان): ۰
۸7 ,۷۷۸3 ,32۳۸3 . 2 ,551۵ ,ت55
کردی (08213[7): 310 انگلیسی (لل5لا6(/0): َ 557
افغانی (پشت) (4701/071):-131170 +107100 دانمارکی (0۸(/18[4): 2و
سانسکریت (54(/97007): س84 سوئدی (8۲50[54): ا۷تقزه
ارمنی (۸/8//1۵0۷): نروژی (۵فا۸/0۴0): 50
۸ 13-2 ,1118 هلندی (4ل0776): 2
برنانی (072280): + بش8 بظ اسلاوی کهن (۲70ا؟ 6 #تاتت صام):
لانین (4770): -886 رقتاتا5 ودنا5 داتا5 57017
گوتیک (0071/0: 816 ,5778 ,5118۸ لیترانی (۷لفاانهنات رم 58۷88 ,5۸88
ایسلندی کهن (42 90721۸4 صان): پروسی کهن ((851-۲# 0۱0): 8۸59
۲8۸3 آلبانی (۷لماانمقتم: ۷۳78
ساکسونی کهن (/(542:0 صا0):
0 و,قنل8 ۰ *
اا
[pdf page 252]
خورء خورشید» هور / ۲۵۳
پسگشت‌ها نخش یت دید ید
۶08۵0 48 هتم هه وهای

ی ان 5 اف ‌لگقلفم 778
9 (8110105) ,ا98 (8515) تلکلاه/8 ۰ 7278 08 لقهاا۵ 01077
2 (8517) مره ما 0 (8)(8) :ما
7 (851) ,884 (8110105)
یادداشت.
8 , 81۳5۸7 ریشه‌ی واژه‌های ژرمنی این فهرست را ناشناخته می‌دانند.
لد ۱
اوستایی (4۳57424): 01 ,81۸۸
5 ,311780 ,13۷۸3 ,2۷8016 ساکسونی کهن ((5420 ۰:0 81۸ ۹
پهلری (,۳۸//۸7): ۷۲۸۹ 7۷۸8015731 فریزی کهن (لفاکل۲ صا0):
ارستی (0555716): 3 5 510205
کر دی (90/ه3 باالاتل 75 آلمانی کهن ((087914 بله‌لبط صرم):
سانسکریت (5452777): لزان
۸ا518 ب80۷۸3 با5۷۸5 ,کهاناد آلمانی ((027/4): ان رین
ارمنی (4/4824۸1): 2 انگلیسی کهن (نتلکلاه8ظ صا0):
یونانی (070654): 8 دای 8 ادا 07 ,817008
لاتین (7120مل): : 50 انگلیسی (5لاه/82): درا
کی فرانسه (ل0/ق۳): 8015۲ دانمارکي (0۸/15). 507 ۱
اسپانیایی" ( 6 ۰ رن سرئدی (5780/57): 80
ایتالیایی ((۸لل 3.074" 5015 نروژی (/(07087801۸: ان
رومانی (۱/۸۸۷۸۸): ان هلندی (7لع۲77): 720
پر تغالی (ظ۳07001788): ان اسلاوی کهن (ع۷1ه51 17367( ا0):
گرتبک (00777/0): ل ی نرا 08۸
87 ماآنا5۸ ,81-2210 لهستانی (۳0/577): 10
ایسلندی کهن (01001427/هش5 صا۵): روسی (7ل7851۵): 0
[pdf page 253]
َ
۱ ۴ / خوردن
صربی (/85781۸): یزان پسگشت‌ها اش رد اد
برهمی (80178(/1407): دسا 81 200820
اسلوا کی 81.014/0): دون ۸ 1 : افتن ان
ا لیتوانی (/71717۸01۵/.): 8ا81 1 (3فآ80) 910 ۳800 با
۱ تونی (لتی) (/۸701۸2): انامه 9 (ااقا50 کم همم |
اپرلندی کهن (0دل#ا صام: نانآ بتا5 5 (818) . . :8 2 کل از
گالی (کلتلام): با1۸0 ۰ |54 علاط
ولزی (5 )+ ات1۸ 5 ((81) :005
برتونی (//82870): 11801 ماناها7 اد
آلبانی (8۸27۵ل)م. 81 9 (810۸) ,615 (۲ن81)
هتیت (4777175): 3 رانا 3 ایا
: 5 61 0
برهان قاطم + ۱۳۹۸۷
کص
اوستایی (۸587۵1): ساکسونی کهن (542000 صا0):
3۷۸۸11 ب20۸ ۸0 ,۲۸88
پهلوی (1ماتلمط): آلمانی کهن (057/۸0 01ابز صزه):
07 7۷۷۸2۸ ,207۸137۸ نان رن
اوستی (05967/0): 20۷۸8178 ,ل(3ه2 آلمانی (05/0440): ندید ان
کردی (08015/1): انگلیسی کهن (4ل8اا8/0 ص.ا0):
۱ 2۷219 ,2611810 81۸0 رالش ت57
بلوچی (041(ادلم8): 20۸ انگلیسی (20/00/5/7): 58۸110۷ ب3ل ۰90"
افغانی (پشتر) (//(۸۲0/۸: 7۸81[ دانمارگی (0۸0۷15/7): اد + 8 ان رن
آرمنی (۸۵4821۸): ,208716 سر دی (5770151): ت57
ایسلندی کهن (۷م هی صرم): نروژی ((۵08۳801۸): 5781618 م5013
3 ,57816۸ ب80133 هلندی (/0076): ندشن ریما
[pdf page 254]
۹ 5
خوک ۲۵۵
پسگشت‌ها انعر ند 1 (5/۸73.0۷0) :00/5
5 ۶002200 37
امه 2 (8]7) ما62 (8۸301)
2 (8[13) ,1099 3۵7۵ت۸ق) : مارا
۸1528 6 (5۸1) ,2 (0378)
1 (081(6) رقلا (5هق) برهان قاطع : ۷۸۸
1 , 328 تاه
بادداشت:
چم این واژه در زبان آلمانی: بزم برپاکردن.
چم این واژه در زبان انگلیسی: با حرص و شتاب خوردن؛ بلمیدن.
اوستایی ([/4887): :1 وتو
پهلری (1الل۲۸). 26 آلمانی ((088944): 7 و8۸
اوستی (0595716): 1 ل70 انگلیسی کهن (5لا84/0 صا0):
کردی (801377(): 2 5617 ,اا5۳ ,ناک
بلوچی (اللتانلمه): ب16 3 انگلیسی (8/0لق2۷0): 1306 ,5712158 ,8017
اففانی (پشتو) (/4۳0//۸/۷): ۰ 216 بکانا311 دانمارکی (0۸]84): 7 ,80
تخاری 8 (8 2427 /51۷22:)7087 ,810۷70 سوئدی (9780/8[7): 5۷1380 ,50 ,81766۸
سانسکریت (7ل84(/58): نروژی (۸۷0۳80140۷). ۰ 5718۲ ,81706۸
7 ممْتهانآو هلندی (07767): 37 ,2876
مین 4 یرنانی (0728/0): ۰ 15058108 ,138 ,1818 ۰ اسلاوی کهن 54۳1۵ 4ل#نابقه صان): ۱
لاتین (/4712ل): ار ۸ ,5۷9
شرآنا6ن51 ,51111178 ر8آنا9 ,818 لهستانی (۳0./5/4): این
گرتیک (0077810): لاد ین روسی (/۷2954): 5713101 ب87177[۸
ایسلندی کهن (۸1۵2/ 52/0 ضام): چکه (2801)): الا ان
۷ بلالآ8 صربی (لفا5578): اناد
ساکسونی کهن (//5۸200 57131:)01-0 ,81۸ برهمی (80[78(/127): لاد
آلمانی کهن ((6284۸ 4ل0الز صا): اسلواکی (81.07:4/4): 51۸
سم
[pdf page 255]
۶ ) خون ‏
لینرانی (4(0لفلا بل 7/): آنا1۸ پسگشت‌ها اشکیت را
لتونی (لتی) (700مل): 8 بو
4۸ ,51۷828 ,81705278 ادا سا

پروسی کهن (۶9۵(۷ت۲۴ ۰:۵ 88۷8۰ 2 (5۷13۵) ,1۵38 600 ی
ایرلندی کهن (تلقل#ا صا0): :3 (م 05
4 806 7 (7818 ,۳۵8۸)
سلتی (کلتی) (81-716-): رده زان 7 (۳16) ۱ :2/5
گالی ([5/.انا0۸): -81 104 نقلاظط
ولزی (877ل8): 8 ,
```


## [2026-09-14T02:02:13.820Z] TOOL CALL #65: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:794 2>&1 | head -60"
}
```


### [2026-09-14T02:02:14.843Z] TOOL RESULT

```
no scan of BQT covers printed page 794 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:02:18.514Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# find page numbering: look for 3-digit numbers\nfor i in (0,1,2,50,100):\n    print('###',i, t[i][:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:02:19.851Z] TOOL RESULT

```
leaves 684
### 0 
### 1                                          ‫‪7‬‬                            ‫رن‪۳‬‬     ‫نات‬       ‫ا م‬               ‫لض‌بال ‪ ۰ ۲۶‬رک‬ ‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬                               
### 2                    ‫م‬ ‫و‬ ‫نآکو سخنیم بیاموزد مرا‬                        ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬ ‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬  ‫دا
### 50    ‫سوت‬                                                                                ‫جنگه‬ ‫و بیاض بزر که را حمگفته‌اند ‪ -‬و نومی‬   ‫است ‪-‬‬   ‫و کنکاش کردن جممی باشد باهم» گوبند‬       ‫است ‪-
### 100       ‫‪4 -‬‬                                                                                  ‫‪ -‬چهمة قر کون‬ ‫از‬      ‫کتابه‬     ‫جشمة نوريخش ه‬                                   ‫آقتلب الت ‪٩‬‏
```


## [2026-09-14T02:02:29.976Z] TOOL CALL #67: Bash

```json
{
 "command": "curl -s https://archive.org/metadata/borhan-ghate-v2 | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d.get('files',[]):\n    if f['name'].endswith(('.pdf','_djvu.txt','.djvu','_jp2.zip','_djvu.xml','_chocr.html.gz')):\n        print(f['name'], f.get('size'))\n\""
}
```


### [2026-09-14T02:02:34.597Z] TOOL RESULT

```
ia800609.us.archive.org /25/items/borhan-ghate-v2
برهان قاطع، جلد دوم.pdf 10740708
برهان قاطع، جلد دوم_chocr.html.gz 21787068
برهان قاطع، جلد دوم_djvu.txt 2359504
برهان قاطع، جلد دوم_djvu.xml 24921944
برهان قاطع، جلد دوم_jp2.zip 340727786
برهان قاطع، جلد دوم_text.pdf 31711743
```


## [2026-09-14T02:02:37.347Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp && curl -sG 'https://ia800609.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=borhan-ghate-v2' --data-urlencode 'doc=برهان قاطع، جلد دوم' --data-urlencode 'path=/25/items/borhan-ghate-v2' --data-urlencode 'q=خوک' | head -c 2000"
}
```


### [2026-09-14T02:02:39.928Z] TOOL RESULT

```
{"ia": "borhan-ghate-v2", "q": "\u062e\u0648\u06a9", "indexed": true, "matches": [{"text": "<IA_FTS_MATCH>\u062e\u0648\u0643</IA_FTS_MATCH> = \u0628\u0631 \u0648\u0632\u0646 \u062f\u0648\u0643 \u061b \u062c\u0627\u0646\u0648\u0631\u06cc \u0627\u0633\u062a \u062a\u0628\u0648\u0646 \u0631\u0627\u062a\u0627 \u0631 \u06a9\u0631\u062a \u06a9\u0647 \u0627\u0646\u0632 \u06a9\u0644\u0648\u06cc \u0645\u0631\u062f \u0645 \u0628\u0631\u0645\u06cc\u0627 \u06cc\u0641 \u0648\u0628\u0639\u0631\u0628\u06cc", "par": [{"l": 1981, "t": 1397, "r": 2127, "b": 1470, "page": 254, "boxes": [{"l": 1981, "t": 1397, "r": 2127, "b": 1470, "page": 254}], "page_width": 2569, "page_height": 3970}]}, {"text": "\u0648 \u0627\u0642\u0627\u0645 \u063a\u0644\u0647 \u0631\u0627 \u0636\u0627\u064a\u0639 \u0645\u064a\u0643\u0646\u062f \u0661\u200f - \u0648 \u0646\u0627\u0645 \u062f\u0631\u062e\u062a\u06cc \u0627\u0633\u062a \u06a9\u0647 \u0628\u06cc\u062e \u0622\u0646\u0631\u0627 \u0627\u0633\u0644 \u0627\u0644\u0648\u0633 \u0648 \u0627\u0635\u0627\u0628\u0639 \u0627\u0644\u0633\u0648\u06cc \u0645\u06cc\u06af\u0648\u0628\u0646\u062f \u06f4 - \u0648\u0628\u0644\u0641\u062a \u0647\u0646\u062f\u06cc \u0646\u0627\u0645 <IA_FTS_MATCH>\u062e\u0648\u0643</IA_FTS_MATCH> \u0622\u0628\u06cc\u200c\u0627\u0633\u062a\u00bb \u0648 \u0622\u0646 \u062d\u06cc\u0648\u0627\u0644\u06cc \u0628\u0627\u0634\u062f \u0622\u0628\u06cc \u0645\u0627\u0646\u0646\u062f \u0645\u0634\u06a9\u06cc \u067e\u0631 \u0627\u0632 \u0628\u0627\u062f \u0648\u062e\u0631\u0637\u0648\u0645\u06cc \u0646\u06cc\u0632 \u062f\u0627\u0631\u062f .", "par": [{"l": 1523, "t": 659, "r": 1673, "b": 720, "page": 652, "boxes": [{"l": 1523, "t": 659, "r": 1673, "b": 720, "page": 652}], "page_width": 2569, "page_height": 3970}]}, {"text": "\u0633 \u0648\u06af - \u0628\u0627 \u0627\u0646\u06cc \u0645\u062c\u0647\u0648\u0644 \u0648 \u06a9\u0627\u0641 \u0641\u0627\u0631\u0633\u06cc \u0628\u0631\u0648\u0632\u0646 <IA_FTS_MATCH>\u062e\u0648\u0643</IA_FTS_MATCH> \u00bb
```


## [2026-09-14T02:02:52.847Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; curl -sL -o bqt439-l254.jpg \"https://ia800609.us.archive.org/BookReader/BookReaderImages.php?zip=/25/items/borhan-ghate-v2/%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%AF%D9%88%D9%85_jp2.zip&file=%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%AF%D9%88%D9%85_jp2/%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%AF%D9%88%D9%85_0254.jp2&id=borhan-ghate-v2&scale=2&rotate=0\"; file bqt439-l254.jpg; ls -la bqt439-l254.jpg"
}
```


### [2026-09-14T02:02:55.009Z] TOOL RESULT

```
bqt439-l254.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1285x1985, components 1
-rw-rw-r-- 1 sfmqrb sfmqrb 267233 Sep 13 22:02 bqt439-l254.jpg
```


## [2026-09-14T02:02:56.909Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt439-l254.jpg"
}
```


### [2026-09-14T02:02:56.935Z] TOOL RESULT

```

```


## [2026-09-14T02:03:26.819Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/794.vision.txt <<'EOF'\n[BQT printed page 794 = borhan-ghate-v2 scan leaf 254; read from the page image by Claude (page 439 verification, root Sek part 2)]\n\nHeadword (right column, printed p. ۷۹۴):\nخوك - بر وزن دوك ، جانوری است معروف ۵ - وگرهائیرا نیز گویند که از زیر کلوی مردم برمیآید وبعربی خنزیر میگویند وجمع آن خنازیر است .\n(with a woodcut of a pig captioned خوك)\n\nMo'in's footnote 5 at the foot of the page:\n«۵ ـ اوستا hū kehrpa (بشکل خوک نر) ، پهلوی xūk ، سانسکریت sūkará (خوک، خوک نر)، کردی xū ، افغانی xūg ، استی xu, xui ، بلوچی hīk و bīx ، وخی xūg ، سریکلی xáug «اشتق ۵۱۰» ورک: اسفلا ۲: ص ۳۱، ۳۶، ۶۳، ۶۶، ۲۶۰، ۲۹۶، و ۳۵۱ ورک: ك. ۱۴۰ ؛ گیلکی وفریزندی xîk ، ... سمنانی xî ، سنگسری xū و xūk ، سرخه‌یی xū ، لاسگردی xok ، شهمیرزادی xūk ... طبری xî ، مازندرانی کنونی xū «واژه‌نامه ۳۳۳» = porcus (لاتینی) ؛ جانوری نوقفاری‌ستان‌دار ضخیم‌الجلد ، سم‌دار ، دارای چهار ناخن در هریک از دستها و پاها ...»\n\ni.e. Mo'in's etymological note derives NP خوک from Av. hū kehrpa- 'in the shape of a boar', MP xūk, with Skt. sūkará- as cognate — the source Nourai (BQT:794) is following.\nEOF\necho saved"
}
```


### [2026-09-14T02:03:27.772Z] TOOL RESULT

```
saved
```


## [2026-09-14T02:03:29.406Z] TOOL CALL #72: Bash

```json
{
 "command": "ls site/pages/439.jpg 2>/dev/null; pdftoppm -f 439 -l 439 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg439 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg439.png"
}
```


### [2026-09-14T02:03:31.226Z] TOOL RESULT

```
site/pages/439.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 82782 Sep 13 22:03 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg439.png
```


## [2026-09-14T02:03:33.248Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg439.png"
}
```


### [2026-09-14T02:03:33.876Z] TOOL RESULT

```

```


## [2026-09-14T02:03:33.849Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:03:53.129Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"sker-!.\\{0,4200\\}\" AHD_watkins1985.txt | head -c 5200"
}
```


### [2026-09-14T02:03:54.549Z] TOOL RESULT

```
sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
sker-! SCATHE skét(o)- SCATO- sker-4 SCAVENGER keu-! SCENT sent- SCHADENFREUDE preu-, skét(e)- SCHEME segh- SCHERZO sker-2 SCHILLER skel-3 SCHIPPERKE skipam
sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
sker-! SHEATH skei- SHEAVE? skei- SHED! skei- SHEEN keu-1 SHEET! skeud- SHEET2 skeud- SHELDRAKE skel-1 SHELF skel-1 SHELL skel-1 SHIELD skel-1 SHIMMER skesi- SHIN! skei- SHINE skeei- SHINGLE! sked- SHINGLES kenk-! SHIP skipam SHIP skep- SHIRT sker-1 SHIT skei- Suiva_ kel-1 SHIVER? skei- SHOAL? skel-1 SHOOT skeud- SHORT sker-1 SHOT! skeud- SHOVE skeubh- SHOVEL skeubh- sHow keu-! SHOWER! kéwero-
```


## [2026-09-14T02:04:08.654Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"SKIN [a-zA-Z()0-9é-]*\\|SAW[!12]* [a-zA-Z()0-9é-]*\\|SHARP [a-zA-Z()0-9é-]*\\|HALF [a-zA-Z()0-9é-]*\\|SCIENCE [a-zA-Z()0-9é-]*\\|NICE [a-zA-Z()0-9é-]*\\|CONSCIENCE [a-zA-Z()0-9é-]*\\|SKI [a-zA-Z()0-9é-]*\\|CARNIVAL [a-zA-Z()0-9é-]*\\|CARNIVOROUS [a-zA-Z()0-9é-,]*\\|GARBLE [a-zA-Z()0-9é-]*\" AHD_watkins1985.txt | sort -u | head -30"
}
```


### [2026-09-14T02:04:08.725Z] TOOL RESULT

```
ugrep: error: error at position 265
a-zA-Z()0-9é-]*\|CARNIVOROUS [a-zA-Z()0-9é-,]*\|GARBLE [a-zA-Z()0-9é-]*
          invalid character class range___/
```


## [2026-09-14T02:04:12.587Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -oE \"(SKIN|SAW[!12]?|SHARP|HALF|SCIENCE|NICE|CONSCIENCE|SKI|CARNIVAL|CARNIVOROUS|GARBLE|SHAPE|SHAVE|SCRAP!?) [a-zA-Zé0-9()-]+\" AHD_watkins1985.txt | sort -u | head -40"
}
```


### [2026-09-14T02:04:12.685Z] TOOL RESULT

```
CARNIVAL legh-
CONSCIENCE skei-
GARBLE kreij-
HALF skel-1
NICE ne
SAW! sek-
SCIENCE ne
SCIENCE skei-
SHAPE skep-
SHARP sker-1
SHAVE (ii)
SHAVE skep-
SKIN sek-
SKI skei-
```


## [2026-09-14T02:04:22.062Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -oE \"krei[əe@]-\\.[^[]{0,1500}\\[[^]]*\\]\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-14T02:04:23.287Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:04:26.291Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -oE \".{80}CRIBRIFORM.{500}\" AHD_watkins1985.txt | head -2; echo ===; grep -oE \".{50}cribrum.{400}\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-14T02:04:26.368Z] TOOL RESULT

```
Exit code 1
riddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRI
(eval):1: == not found
```


## [2026-09-14T02:04:31.899Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -oE \"CRISIS.{0,400}\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-14T02:04:32.978Z] TOOL RESULT

```
CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog-
CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
```


## [2026-09-14T02:04:40.539Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"سیلی\" \"غربال\" \"اسکی\" \"سگال\" \"سیگال\"; do echo \"=== $w ===\"; grep -o \".\\{0,120\\}$w.\\{0,160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -3; done"
}
```


### [2026-09-14T02:04:58.314Z] TOOL RESULT

```
=== سیلی ===
=== غربال ===
=== اسکی ===
=== سگال ===
=== سیگال ===
```


## [2026-09-14T02:05:00.675Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 MON_part1.txt; echo; wc -c MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T02:05:00.792Z] TOOL RESULT

```
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی 
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
```


## [2026-09-14T02:05:06.091Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for غربال — its origin tag (e.g. [ع.]) and definition, plus the Dehkhoda note on its origin if present."
}
```


## [2026-09-14T02:05:07.547Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%DB%8C/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for سیلی — its origin tag and definition (slap), and any Dehkhoda etymological note."
}
```


### [2026-09-14T02:05:11.054Z] TOOL RESULT

```
# فرهنگ معین Entry for غربال

**Origin Tag:** (غَ یا غِ) (اِ.)

**Definition:** "وسیله ای مشبک یا سوراخ سوراخ برای جدا کردن اجزای ریز و درشت یک جسم، الک"

(A mesh or perforated device for separating fine and coarse particles of a substance; a sieve)

---

## Dehkhoda Note on Origin

According to the Dehkhoda dictionary entry presented here, غربال is derived from the root گربال and shares etymological connections with Latin *criblum* and *cribrum*, which entered French as *crible*. The term was then adopted into Persian as both گربال and غربال, with غِربال being the Arabicized version of the same word.
```


### [2026-09-14T02:05:13.208Z] TOOL RESULT

```
# فرهنگ معین Entry for سیلی

## Definition
According to Farhang-e Mo'in, سیلی is defined as: **"ضربه ای که به وسیلة کف دست به چهرة کسی زنند، تپانچه"** (a blow delivered with the palm of the hand to someone's face; a slap).

## Additional Meaning
The dictionary also notes an idiomatic usage: maintaining one's appearance while experiencing hardship, expressed as "با سیلی صورت خود را سرخ نگه داشتن" (keeping face red with slaps)—a euphemism for preserving dignity despite financial difficulties.

## Origin Information
The Dehkhoda etymological sources provided in this entry indicate that سیلی originates from straightening and joining the fingers of the hand to deliver a blow, particularly historically used as a form of punishment. However, the entry clarifies that calling a gun a "سیلی" (as in تپانچه) is incorrect—the term properly refers to hand-delivered strikes.
```


## [2026-09-14T02:05:28.292Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"AFM:\"; grep -c \"\" AFM_pages.txt; grep -n \"غربا\\|كربال\\|گربال\" AFM_pages.txt AFM.txt ARB_mo3rb.txt TAD_pages.txt FVQ.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T02:05:28.375Z] TOOL RESULT

```
AFM:
6684
ARB_mo3rb.txt:8748:إلا اين در يد وقلده ابلواليق ٠‏ ش (0) تصرف المؤلف فى هذه المادة تصرفا غربا » فأخطأً
```


## [2026-09-14T02:05:29.577Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/garble",
 "prompt": "Full etymology of \"garble\": Anglo-Latin garbellare, Arabic gharbala, ghirbal, Late Latin cribellum, Latin cribrum. Quote the chain."
}
```


### [2026-09-14T02:05:34.911Z] TOOL RESULT

```
# Etymology Chain of "Garble"

Based on the Online Etymology Dictionary, here's the linguistic ancestry:

**Arabic → Medieval Latin/Catalan/Italian → Anglo-French → English**

The word traces back through this progression:

1. **Arabic**: "gharbal" (to sift), related to "kirbal" (sieve)
2. **Late Latin**: "cribellum" (diminutive of "cribrum," meaning sieve)
3. **Medieval paths**: The term spread via "Medieval Latin, Catalan, and Italian garbellare"
4. **Anglo-French**: "garbeler" (to sift)
5. **English**: Early 15c. "garble" (initially meaning "to inspect and remove dirt and dross from spices")

As the source notes: "the word was widespread among Mediterranean traders" during the spice trade era, when "pepper and ginger and some other spices" required processing to remove chaff and debris before reaching European markets.

The semantic evolution progressed from the literal commercial practice of sifting spices to the figurative modern sense of distorting language or information.
```


## [2026-09-14T02:05:41.593Z] TOOL CALL #86: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-",
 "prompt": "Give the reconstruction page for PIE *sek-: meaning, derived terms, extensions (*skey-, *(s)ker-, *skel-), and references (Pokorny page)."
}
```


## [2026-09-14T02:05:43.058Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/science",
 "prompt": "Etymology of science: Latin scientia, scire \"to know\", its PIE root and the note about *skei- \"to cut, split\"; also mention of \"nice\" from nescius."
}
```


### [2026-09-14T02:05:47.310Z] TOOL RESULT

```
# Proto-Indo-European *sek-

## Meanings

The reconstruction documents two distinct roots:

1. **"to cut, cut off, sever"** – the primary sense with synonym *ḱes-
2. **"to dry out"** – a secondary meaning

## Alternative Reconstructions

Sources propose several variants: *sekH-, *sekh₁-, and *sekh₂-, reflecting uncertainty about laryngeal elements.

## Key Derived Terms

Notable formations include:
- *sek-eh₂yé-ti (Latin *secō*)
- *sék-no-m (Latin *segnom*)
- *sek-ūr- (Latin *secūris*, "axe")
- *séks-u-s (Latin *sexus*)
- *soks-ó-m (Germanic *sahsą*, Latin *saxum*)

## Extensions

The page references *skey- as an "ey-present" formation but does not detail *(s)ker- or *skel- as extensions of *sek-.

## Primary Source

Pokorny's *Indogermanisches etymologisches Wörterbuch* (1959), pages 895–896, provides the foundational reconstruction and comparative evidence across Indo-European language families.
```


### [2026-09-14T02:05:48.494Z] TOOL RESULT

```
# Etymology of Science

The word "science" originates from mid-14th century English, derived from Old French *science* and Latin *scientia*, meaning "knowledge" or "a knowing." The Latin root *scire* means "to know," with etymologists suggesting the original notion involved "to separate one thing from another, to distinguish."

## Key etymological connections:

**PIE Root:** The Latin *scire* traces back to the Proto-Indo-European root *skei-, meaning "to cut, split." This root also produced Greek *skhizein* (to split) and Old English *sceadan* (to divide).

**Semantic evolution:** Early meanings included "state or fact of knowing" and "book-learning." By the late 14th century, it denoted "systematized knowledge regarding a particular group of objects." The modern scientific sense—"body of regular or methodical observations"—became established by 1725.

**Related word:** Interestingly, "nice" shares linguistic kinship through Latin *nescius* ("not-knowing"), combining the negation *ne-* with the same *scire* root.

The predominant modern usage focusing on "natural and physical science" emerged by the mid-19th century, restricting the term to systematic study of material phenomena and natural laws.
```


## [2026-09-14T02:05:59.878Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%DB%8C/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for اسکی — the bracketed origin tag (e.g. [فر.] French or [انگ.] English) and definition."
}
```


## [2026-09-14T02:06:01.632Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for کارناوال — the bracketed origin tag (e.g. [فر.]) and definition."
}
```


### [2026-09-14T02:06:03.406Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for اسکی

**Origin tag:** [فر.] (French)

**Definition:** "یکی از ورزش های زمستانی که با کفش و چوب مخصوص روی برف ایستاده سر می خورند"

This entry identifies skiing as a winter sport performed while standing, using specialized footwear and poles on snow.
```


### [2026-09-14T02:06:05.555Z] TOOL RESULT

```
# فرهنگ معین Entry for کارناوال

**Origin tag:** [فر.] (French)

**Definition:** "کاروان شادی ، کاروانی که در ایام معینی از سال با لباس های مضحک برای تفریح و سرگرمی به راه می افتند"

In essence, Mo'in's dictionary defines carnival as a joyful procession occurring during specific times of year, where participants wear ridiculous costumes for entertainment and amusement purposes.
```


## [2026-09-14T02:06:23.216Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN sili ===\"; grep -nE \"sīlī|sili |silī|Ohrfeige\" HRN.txt HUB.txt | head -8; echo \"=== LAT caro ===\"; grep -nE \"^caro|carō|caro,? -\" LAT.txt | head -5; echo \"=== LAT scio ===\"; grep -nE \"^scio|scio,? \" LAT.txt | head -5; echo \"=== LAT cribrum ===\"; grep -nE \"cribrum\" LAT.txt LEW_1910.txt | head -5"
}
```


### [2026-09-14T02:06:23.331Z] TOOL RESULT

```
=== HRN sili ===
=== LAT caro ===
9990:caro (carro), -is, -ere: carder; carere a carendo, quod eam [sc.
10012:caro, c&rnls f.: morceau de chair, de viande; cf. le pl. carnes
10051:carota, -ae f.: panais, carotte. Emprunt tardif et populaire (Api¬
11664:cicaro, -onis m.: mot d'affection familier, pour designer un enfant,
=== LAT scio ===
3603:nescio, haud scio, fors an, forsitan, cf.Thes. II 7.,6ssqq., ou dans le
17782:rattache l'adj. dubius forme comme ludius de ludo, scius de scio, etc.,
18438:valeur la personne, et pour 1 'opposer A d'autrea: scio ego "je sais
18439:bien, aoi"; ego scio "aoi, je sais". Ausai eat-il souvent renforcd
20748:-tor, -torius, Vg., B.3,103, nescio quis teneros oculus mihi fascinat
=== LAT cribrum ===
LAT.txt:11289:"trfer, passer au crible" (cf. cribrum de meme racine, excrementum "cri-
LAT.txt:11291:per cribrum cernas-, Plin. 18,n, 19, conserve encore en roman, cf.M.L.
LAT.txt:11385:cribrum: crible, cf. M.L.3334, les formes romanes remontent souvent
LAT.txt:11414:trois groupes occidentaux: lat.cribrum (la forme / est conservee dans
LAT.txt:14606:cribrum
```


## [2026-09-14T02:06:25.584Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10012,10030p' LAT.txt; echo \"=== cribrum ===\"; sed -n '11385,11400p' LAT.txt"
}
```


### [2026-09-14T02:06:25.673Z] TOOL RESULT

```
caro, c&rnls f.: morceau de chair, de viande; cf. le pl. carnes
(= oapxee); e.g. Enn.A.333, Cyclopis uenter... carnibus humanis disten¬
tus, et 1'expression ancienne carnem petere, accipere "demander, rece-
voir sa part de viande dans les sacrifices" Varr.L.L.6,35, T.L.33,1,9;
le diminutif caruncula "petit morceau de chair"; ‘le compose carnifex,
carnufex defini par Donat, Hec.441, -es dicti quod carnes ex homi¬
ne faciant. Puis "chair", et "pulpe" (d'un fruit), comme le gr. CT<xp^.
- Ancien, usuel. Panroman, M.L.1706.
La langue ancienne et classique ne connait gufere en fait de derives
et de compos^s que 1 1 adjj. carnarius, usit6 surtout comme substantif,
carn&rium "garde-manger", M.L.1703, v.h.a. charnari, et carnifex "bour-
reau". On trouve dans Varr., Men.484 cite par Non.86,19, carnalis avec
un sens obscur; Pline emploie carniuorus pour traduire crapxopopoc
(camiuordx , Fulg.). A basse 4 poque dans la langue medicale et surtout
dans la langue de 1'tfgli se apparaissent de nombreux derivas: carnalis,
avec le sens de "charnel" (= crapiavos) M.L.i70ia; d'ou carnaliter,
camalitds; carnStib (Cael. Aur.) et con-, in-carnUtiS, -tus, d^u incarno-,
carnatus et excarndtus (d'ou excarno M.L.3960, cf. aussi fr. ddchamd) ;
carneus (opp. i spiritualis) et incarneus; carnifer (= oapnocpopoe),
=== cribrum ===
cribrum: crible, cf. M.L.3334, les formes romanes remontent souvent
4 des formes alt 4 r 4 es ou sont intervenues des dissimilations tardives,
ciribrum, *cTbrum, criblum, cribum, attest 4 es dans les Gloses, cf.
Thes. s.u. Iri. ribar ? Douteux.
Deriv 4 s: cribro,-Ss (formes tardives criblo (Mare.Emp., Chiron), cribo
(Diosc .), scribo (Itala), M.L.3333; cribrarius M.L.3333; cribellum M.L.
3331; cribellare M.L.3331; in-, per-cribro.
On trouve 4 galement dans les gloses une forme crefrat: siftid (ags),
CGL V 351,11 dont l*e et - 1 ’/ d 4 noncent le caractbre dialectal.
crimen,-inis n. (cf. gr. xpT(jxx) : a du signifier d'abord "ce qui sert
4 trier, 4 d 4 cider", puis "d 4 cision"; mais en passant dans la 1 . dn
droit, crimen s'est sp 4 cialise dans le sens de "d 4 cision judiciaire"
in crimen uoedre, adducere, et "objet sur quoi doit porter la d 4 cision,
grief, accusation, inculpation", souvent du reste avec nuance p 4 jora-
tive "fausse accusation, calomnie". Puis 1 'accusation se confondant
avec le crime (scelus) lui _ meme, crimen a fini par signifier le crime.
```


## [2026-09-14T02:06:32.020Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10035,10050p' LAT.txt; echo \"=== scio entry ===\"; grep -n \"^scio,\\|^scio \" LAT.txt | head; grep -n \"scio,-Is\\|scio, -is\" LAT.txt | head"
}
```


### [2026-09-14T02:06:32.120Z] TOOL RESULT

```
ficius-, carnificina (Pl .),-ficus; fico,-ds,-ficdtor,-trXx et excar-
nificS.
Plus encore qu'en latin, le sens de "part" de ce mot, dont la flexion
indique le caractbre ancien, est visible en osco-ombrien: osq. carneis
"partis", ombr. fcaru "pars", abi. karnus "partibus", k cot6 de ombr. kartu
"distribuito" (osq. karanter "uescuntur" est douteux; v. sous creo);
pour la forme, cf. v.isl . htprundr "peau". Le sens s'explique par la
faqon dont on partageait la viande des betes dans des sacrificesou
dans les repas en commun faits par les guerriers: il faut penser au
"morceau du h6ros" dans l'6pop6e irlandaise. Une expression pareillei8i
carpS
se trouve dans sogdien y’t (v. BSL 33, p.107). - Le mot italique est
1 1 elargissement en -n- d'un thbme racine; la racine est celle de xeupoo
"je coupe", xaprjvai,; et par suite de lat. corium, curtus, cortex, v. ces
mots. Elie a nn doublet a s- initial: iri. scaraim M je separe", T.h.a.
sceran "couper", lit. skiriu "je separe"; v.lat. scortum,
=== scio entry ===
```


## [2026-09-14T02:06:37.852Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ski,  n\\.\\|^ski\\b\" KLN_1966.txt | head -5; grep -o \"ski,  n\\..\\{0,400\\}\" KLN_1966.txt | head -2; echo \"=== carnival ===\"; grep -o \"carnival,  n\\..\\{0,500\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-14T02:06:39.336Z] TOOL RESULT

```
35425:Derivative:  skewer,  tr.  v. ski,  n.  —  Norw.,  fr.  ON.  skid,  ‘wooden  billet, snowshoe’,  which  is  rel.  to  OE.  scid,  ‘stick  of wood'  (whence  obsol.  E.  shide),  OHG.  skit, MHG.  schit,  G.  Scheit,  ‘log’,  and  to  OE.  scea- dan,  scadan,  ‘to  divide,  separate’.  See  shed,  v., and  cp.  skid.
ski,  n.  —  Norw.,  fr.  ON.  skid,  ‘wooden  billet, snowshoe’,  which  is  rel.  to  OE.  scid,  ‘stick  of wood'  (whence  obsol.  E.  shide),  OHG.  skit, MHG.  schit,  G.  Scheit,  ‘log’,  and  to  OE.  scea- dan,  scadan,  ‘to  divide,  separate’.  See  shed,  v., and  cp.  skid.
=== carnival ===
carnival,  n.  —  F.  carnaval,  fr.  It.  carnevale,  fr. ML.  came,  vale,  ‘O  flesh,  farewell1.’.  See  carnal and  vale,  interj.
```


## [2026-09-14T02:06:52.946Z] TOOL CALL #94: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg439.png data/verification/sources/refs/ocr/BOOK/439.png && ls -la data/verification/sources/refs/ocr/BOOK/439.png"
}
```


### [2026-09-14T02:06:53.015Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82782 Sep 13 22:06 data/verification/sources/refs/ocr/BOOK/439.png
```


## [2026-09-14T02:07:07.489Z] TOOL CALL #95: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%DA%A9|page 439 node 2, Persian xuk: MP xug, Proto-Iranian *huHkah, PIE *suH- (not from kahrp-)' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%A7%D9%84%DB%8C%D8%AF%D9%86|page 439 node 22, Persian segalidan < MP uskardan, PIE *kwer-' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%84%DB%8C|page 439 node 3, Persian sili slap - no etymology given on Wiktionary' \\\n 'https://www.etymonline.com/word/ski|page 439 nodes 4-7, ski < Norwegian < ON skid < PIE *skei-' \\\n 'https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84|page 439 nodes 9-10, Arabic girbal < Aramaic arbala (not Latin cribellum); Persian garbal < Arabic' \\\n 'https://www.etymonline.com/word/carnival|page 439 nodes 15-18, carnival < F carnaval < It carnevale < carnelevare' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-|page 439 root Sek, PIE *sek- to cut, Pokorny 895-896' \\\n 'https://www.etymonline.com/word/science|page 439 nodes 13-14, Latin scire < PIE *skei- to cut split; nice < nescius' \\\n 'https://www.etymonline.com/word/garble|page 439 node 9, Arabic gharbala, ghirbal, Late Latin cribellum' \\\n 'https://abadis.ir/fatofa/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84/|page 439 node 10, Moin/Dehkhoda entry for gharbal - Dehkhoda links to Latin cribrum/criblum' \\\n 'https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%DB%8C/|page 439 node 3, Moin entry sili = slap with palm of hand' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%DB%8C/|page 439 node 6, Moin tags eski as [فر.] French' \\\n 'https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/|page 439 node 17, Moin tags karnaval as [فر.] French' \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:07:18.646Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/87e98b3ce49cadc2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e53e048ebc45c9ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4a0f0b16b82cf2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c32e8bff0d2e23f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4a01d3d91ec879fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb1b4b76585eeaec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a55319786f2f0be1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e318226959638090.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b75e0ff80d54ffda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7106c7494f4aa6cc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d72fd59b27ec978a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9163b90270f4d220.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/58d8e782c0b6eb90.txt
```


## [2026-09-14T02:07:23.715Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 skel ===\"; grep -n \"skel-\" incoming/WLD/WLD_Bd2_pages.txt | head -5; echo \"=== WLD Bd2 hukarapta ===\"; grep -n \"schöngeformt\\|kǝrǝpta\\|karapta\" incoming/WLD/WLD_Bd2_pages.txt | head -5"
}
```


### [2026-09-14T02:07:23.790Z] TOOL RESULT

```
=== WLD Bd2 skel ===
20684:(s.   Parallelen bei Palk-Torp u. nms): gr. juvg ..ifuskel^, /livcov ,.muskel-
27929:(s. Yf. LEWb.2     ^   Reichelt KZ.  46, 349)  lacca (Yegetius)    „durch  Muskel-
=== WLD Bd2 hukarapta ===
```


## [2026-09-14T02:07:27.083Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"skel-\\|(s)kel\" WLD_band3.txt | head -5; echo \"=== Bd2 596 ===\"; grep -n \"kalpate\\|klptá\\|hu-k\" incoming/WLD/WLD_Bd2_pages.txt | head -8"
}
```


### [2026-09-14T02:07:27.154Z] TOOL RESULT

```
=== Bd2 596 ===
39513:und Nageln            :   beschnitten^ == av. hu-kdrdpta- „sch6ngeforint^‘ (Persson KZ.
```


## [2026-09-14T02:07:30.475Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '39500,39525p' incoming/WLD/WLD_Bd2_pages.txt; echo \"--- page tag ---\"; awk 'NR<=39513 && /\\[pdf page/ {p=$0} END{}' incoming/WLD/WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<39513' | tail -1"
}
```


### [2026-09-14T02:07:31.716Z] TOOL RESULT

```
                                                       (s)qel-                                            595

skr. prdJcoJa „Teil eines gespaltenen Ganzen^', russ.                          raskoh „Spaltung^‘ usw.
s. u. qel- „sclilagen“.

     Ygl. im allgem. Zup, Gutt. 151 f. m. alterer Lit., Persson Wzerw. 52,
KZ. 33, 284fF., Beitr. 174fif., 383 a 1, 646 f., 655, 657, 675, 786, 960f,



     Wzerw. s qel(e)-p- (Curtius 166, Persson Wzerw. 52, KZ. 33, 289f.):
     Arisch. wahrscheinlich             in     ai.   kdlpate „wird geordnet,               wird zuteiP*, kal-
pdyati                    an, verteilt, teiltzu“,     „geordnet, hergestellt; von Haaren
und Nageln            :   beschnitten^ == av. hu-kdrdpta- „sch6ngeforint^‘ (Persson KZ.
33, 289 f., Uhlenbeck AL Wb. 48f., s. auch u. '^qrep' „Leib‘‘)
     gr. oxd).oip         „Maulwurf'‘        (als „Graber“; kaum als schiefaugig“ zu sqel-
„biegen‘‘, oxaX-rjvog und 6\p\                 gegen Verb. m. lat. talpa s. Vf. LEWb.^ s. v.),
oxokoyj „Spitzpfabl“
     lat.   scalpo, -ere „kratzen, ritzen, scharren,                   mit spitzem Werkzeug scbnei-
den, mei6eln‘‘, scalpnimj scalper „scharfes Werkzeug zum schneiden, meiBeln'',
sculpOj -ere (ursprgl. in Zs. aus scalpo) ,,durch Graben, Stechen, Schneiden
etwas bilden; schnitzeln, meifieln"';
  ahd. scelifa, mhd., nhd. mdarti. sclielfe „hautige                               Schale'',   mnd. schelver
„abgeblattertes             Stiick'',   schulvern       „abblattern“;        aisl.    skidlf „Bank“,      ags.
scelfe,        „Bank, Bettgesteli, Stockwerk (tabulatum)'^ scylf m. „Fels-
             scyJfe
--- page tag ---
```


## [2026-09-14T02:07:56.643Z] AGENT

Now I'll write the verification JSON.


## [2026-09-14T02:16:13.662Z] TOOL CALL #99: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-439.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"xerpta; hu-xerpta, hu-kehrpta\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Avestan words are real but the book's first transliteration is impossible. Bartholomae, AiW col. 1830, has j. hu-kǝhrp- Adj. 'wohlgestaltet' (of Haoma, Y.9.16) and j. hu-kǝrǝpta- Adj. 'schöngeformt' (of a woman's breasts, Yt.5.127), the latter a participle matching Skt. kḷptá- to kalpate 'is arranged, is fashioned'; the second element is kahrp-/kǝrǝf- f./n. 'the visible exterior of any being or thing, outward appearance, shape', also 'body' (BRT col. 454). Avestan has no initial /x/ here: the cluster is k-ǝ-h-r-p / k-ǝ-r-ǝ-p, so the book's 'xerpta' (with x) is a misprint or an idiosyncratic notation for kǝrǝpta-; the companion form 'hu-kehrpta' on the same line prints the k correctly, which shows the x is the error. On the derivation itself Nourai follows Pokorny exactly: IEW 926, under the root extension skel(e)-p- of (s)kel-1 'schneiden' (923-927), lists 'ai. kḷptá- ... = av. hu-kǝrǝpta- \\\"schöngeformt\\\", das jedoch auch zu kǝhrp- \\\"Gestalt\\\" (oben S. 620) gehören könnte' — i.e. Pokorny himself allows the attachment to the cutting/shaping root *(s)kel-p- but flags the alternative *kʷrep- 'body, form' (Latin corpus). Walde-Pokorny II 595 says the same. So the edge root→node is plausible, the form is not.\",\n \"derivation_fa\": \"واژه‌های اوستایی درست‌اند ولی نویسه‌گردانی نخست کتاب ناممکن است: بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۸۳۰ صورت‌های hu-kǝhrp- «خوش‌اندام» و hu-kǝrǝpta- «زیبافرم» را آورده است؛ جزء دوم همان kahrp-/kǝrǝf- «پیکر، شکل بیرونی، تن» است. در اوستایی در این ریشه هیچ /خ/ آغازین نیست، پس «xerpta» خطای چاپی (یا نویسه‌گردانی شخصی) نورایی برای kǝrǝpta- است؛ همان سطر صورت درست «hu-kehrpta» را نیز چاپ کرده و همین نشان می‌دهد که x نادرست است. اما دربارهٔ خودِ پیوند، نورایی دقیقاً از پوکورنی پیروی کرده است: پوکورنی در ص ۹۲۶ ذیل گسترشِ ریشهٔ skel(e)-p- (از (s)kel- «بریدن») همین hu-kǝrǝpta- را می‌آورد و می‌افزاید که می‌تواند به kǝhrp- «پیکر» (ص ۶۲۰) هم وابسته باشد. پس «خطای چاپی کتاب» در صورت واژه، و پیوندِ ریشه‌شناختی «با احتیاط پذیرفتنی».\",\n \"error_in\": \"book\",\n \"book_prints\": \"xerpta : cut, shaped / hu-xerpta, hu-kehrpta : shaped like a boar, pig\",\n \"correct_form\": \"kǝrǝpta- (Av. hu-kǝrǝpta- 'beautifully formed', hu-kǝhrp- 'well-shaped')\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:926\", \"status\": \"supports\", \"note\": \"POK_03.txt line 2155, printed page header '926' at line 2151: 'vielleicht in ai. kálpate ... = av. hu-kǝrǝpta- ‚schöngeformt‘, das jedoch auch zu kǝhrp- ‚Gestalt‘ (oben S. 620) gehören könnte' — under 'Wurzelerweiterung skel(e)-p-' of (s)kel-1 'to cut'. Exactly Nourai's arrow, with Pokorny's own caveat.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW s.vv. hu-kǝhrp-, hu-kǝrǝpta-, kahrp- (BRT.txt lines 30150, 30152, 9545)\", \"stance\": \"supports\", \"note\": \"'j. hu-kǝhrp- Adj. ‚wohlgestaltet‘: vaŋhuš haomō ... Y.9.16' ; 'j. hu-kǝrǝpta- Adj. ‚schöngeformt‘ ... Yt.5.127' ; 'j., g. kahrp-, kǝrǝf- f., n. ‚das sichtbare Äussere jedes Wesens und Dings, äussere Erscheinung, sichtbare Gestalt‘ ... insbes. ‚Leib, Körper‘'. No form with initial x-.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 595 s.v. (s)qel(e)-p- (WLD_Bd2_pages.txt line 39513)\", \"stance\": \"supports\", \"note\": \"'ai. kḷptá- ... == av. hu-kǝrǝpta- ‚schöngeformt‘ (Persson KZ. 33, 289f. ... s. auch u. *qrep- ‚Leib‘)' — same attachment and same caveat as Pokorny.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, s.v. skel-1 'To cut' (AHD_watkins1985.txt)\", \"stance\": \"partial\", \"note\": \"Watkins gives the extended root *skelp- (SHELF, HALF, SCALPEL, SCULPTURE) but cites no Indo-Iranian material, so the Avestan word is simply absent from AHD.\"}\n ]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"xŭk «خوک»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"NP xūk 'pig' goes back to MP xūg (Book Pahlavi hwk', MacKenzie 1971 p. 94 'xūg [HZWLYA < A hzyr'; hwk'] pig'), from Proto-Iranian *huHka- 'pig', a -ka- derivative of *huH- 'pig' = PIE *suH- (Skt. sū-, sūkará- 'boar', Latin sūs, Gk. hûs, OE sū 'sow'); Av. hū- 'pig' is the same word, with the regular Persian development of initial *hu- before a back vowel to xu-/xū- (Hübschmann, Pers. Studien p. 215: 'xūk \\\"Schwein\\\" = phl. xūk = zd. hu-'). Nourai instead makes it a clipping of the compound hu-kǝhrpa- 'boar-shaped', a derivation he takes over from Horn (Grundriss no. 510) and from Mo'in's footnote in Borhan-e Qate' p. 794, which prints 'اوستا hū kehrpa (بشکل خوک نر)، پهلوی xūk، سانسکریت sūkará'. That 19th-century analysis is not tenable: nothing of -kǝhrpa- survives in xūk, and the 'pig' sense in the compound comes from hū- 'boar', not from kǝhrp- 'shape'. Nourai's own cross-reference ☞Su 2 concedes the pig root. The word therefore belongs under *suH-, not under Sek.\",\n \"derivation_fa\": \"«خوک» از فارسی میانهٔ xūg (پهلوی کتابی hwk'، مکنزی ص ۹۴) و آن از ایرانی باستان *huH-ka- «خوک»، مشتقِ پسوندیِ *huH- = هندواروپایی آغازین *suH- (سنسکریت sūkará- «گراز»، لاتین sūs، یونانی hûs، انگلیسی کهن sū). هوبشمان (پژوهش‌های فارسی، ص ۲۱۵) صراحتاً می‌نویسد «xūk = پهلوی xūk = اوستایی hu-»؛ *hu آغازین در فارسی پیش از واکهٔ پسین به xu/xū بدل شده است. نورایی به پیروی از هرن (شمارهٔ ۵۱۰) و حاشیهٔ معین بر برهان قاطع (ص ۷۹۴) آن را کوتاه‌شدهٔ ترکیب اوستایی hū-kǝhrpa «به شکل گراز» می‌داند؛ ولی این تحلیلِ سدهٔ نوزدهمی پذیرفتنی نیست، زیرا هیچ نشانی از جزء -kǝhrpa در xūk نمانده و معنی «خوک» در آن ترکیب از hū- «گراز» می‌آید نه از kǝhrp- «پیکر». آریان‌پور و ویکی‌واژه نیز آن را ذیل ریشهٔ *sū- می‌آورند. پس پژوهش امروزی ادعای نورایی را رد می‌کند و واژه را به ریشهٔ Su (گراز) می‌برد — چنان‌که ارجاع خودِ نورایی (☞Su 2) هم نشان می‌دهد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:794\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' printed p. 794 (archive.org borhan-ghate-v2, scan leaf 254 — page header ۷۹۴ visible; image read and saved to data/verification/sources/refs/ocr/BQT/794.vision.txt). Headword 'خوك - بر وزن دوك ، جانوری است معروف'; Mo'in's footnote 5: 'اوستا hū kehrpa (بشکل خوک نر)، پهلوی xūk، سانسکریت sūkará (خوک، خوک نر)، کردی xū، افغانی xūg ...'. Mo'in does print the hū-kehrpa derivation Nourai reproduces.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary p. 94 (PHD.txt line 661)\", \"stance\": \"supports\", \"note\": \"'xūg [HZWLYA < A hzyr; hwk' | N ~] pig' — the Middle Persian link in the chain, with no trace of a kǝhrp- element.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 215 (HUB.txt line 7638)\", \"stance\": \"contradicts\", \"note\": \"'xūk ‚Schwein‘ = phl. xūk ... = zd. hu-' — Hübschmann derives it straight from Av. hū- 'pig', not from the compound with kǝhrp-.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie no. 510 (HRN.txt line 4609)\", \"stance\": \"partial\", \"note\": \"'xūk ‚Schwein‘ ... aw. hū kehrpa ‚in Ebergestalt‘; phlv. xūk (Bund.) ... skr. sūkará- ‚Eber, Schwein‘' — Horn is the source of Mo'in's and Nourai's formulation, but he reads hū- as 'boar', i.e. the pig sense is in hū-, not in kǝhrpa-.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye Hend-o-Orupayi, entry خوک printed p. 255 (ARY_pages.txt, pdf page 254)\", \"stance\": \"contradicts\", \"note\": \"The خوک entry lists Avestan, Pahlavi, Ossetic, Kurdish, Baluchi, Pashto, Tocharian B, Sanskrit, Greek, Latin sūs/suīnus, Gothic and Old Norse cognates, i.e. it files the word under PIE *sū- 'pig', not under a 'cut/shape' root.\"}\n ]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"sîlî «سیلی»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP sīlī 'slap, blow with the flat of the hand' (Mo'in: 'ضربه‌ای که به وسیلهٔ کف دست به چهرهٔ کسی زنند'; borrowed onwards into Ottoman/Turkish sille, Azerbaijani sillə, Georgian sila, Armenian silla). The one etymology Nourai can be checked against is Mann's, and it is exactly what he cites: IEC 640 s.v. Kr̥t- (2) 'cut, blow' (an extension of the *(s)ker- 'cut' family that Nourai groups under Sek) gives 'Per. cf. sile, sili, sīlī ‚slap, blow‘ beside sūli (‚plough‘ lit. ‚cutter‘ ?)'. Note Mann himself writes 'cf.' and queries the second form, and no Iranianist source (Horn, Hübschmann, Cheung, Hasandust as excerpted on Wiktionary) gives an etymology for the word at all; Wiktionary's Persian entry has no etymology section, and Dehkhoda only paraphrases the sense. So the derivation rests on Mann alone: compatible with a *(s)ker-t- 'cut, strike' base, but unconfirmed elsewhere.\",\n \"derivation_fa\": \"«سیلی» در فارسی «ضربه‌ای که با کف دست بر چهره زنند» است (معین) و از فارسی به ترکی عثمانی sille، آذربایجانی sillə، گرجی sila و ارمنی silla رفته است. تنها منبعی که ریشه‌ای برای آن می‌دهد همان مأخذ نورایی است: مان در «فرهنگ تطبیقی هندواروپایی» ص ۶۴۰ ذیل Kr̥t- (2) «بریدن، زدن» می‌نویسد «Per. cf. sile, sili, sīlī ‚slap, blow‘»، یعنی آن را به خانوادهٔ *(s)ker- «بریدن» می‌بندد؛ ولی خودِ مان با «cf.» احتیاط کرده است. هرن، هوبشمان، چونگ و ویکی‌واژه هیچ ریشه‌شناسی‌ای برای این واژه نیاورده‌اند و دهخدا تنها معنی را شرح می‌دهد. بنابراین ادعای نورایی «با احتیاط پذیرفتنی» است و بر یک منبع تکیه دارد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%84%DB%8C\", \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%84%DB%8C/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:640\", \"status\": \"supports\", \"note\": \"Mann, IEC printed p. 640 (IEC.txt \\\\f-leaf 361, page number '640' printed in the leaf): 'Krt- (2) “cut, blow”. Cf. Kerto — Skt. śūrtáh, -śīrtáh “shattered”; Arm. sartnum “be separated”; Per. cf. sile, sili, sīlī “slap, blow” beside sūli (“plough” lit. “cutter” ?)'. Exactly Nourai's arrow.\"},\n   {\"ref\": \"MON:1982\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 2 p. 1982 is not paginated online; the entry text was read at abadis.ir (فرهنگ معین: 'ضربه‌ای که به وسیلهٔ کف دست به چهرهٔ کسی زنند، تپانچه'), which confirms the gloss but carries no origin tag.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie — grep 'sili/sīlī/Ohrfeige' in HRN.txt\", \"stance\": \"silent\", \"note\": \"no entry; Horn has no article for the word.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien — same grep in HUB.txt\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt — grep 'سیلی'\", \"stance\": \"silent\", \"note\": \"no headword سیلی in the Indo-European-roots dictionary.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir\", \"stance\": \"partial\", \"note\": \"gives the meaning ('a blow struck with the palm on the face') but no etymology; Dehkhoda's note likewise only explains the gesture.\"}\n ]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Germanic\", \"words\": \"skith\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Watkins/AHD s.v. skei- 'to cut, split' (an extended root of sek-): 'Extended root *skeit- in ... b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI'. Old Norse skíð n. 'billet of wood, snowshoe' is cognate with Old English scīd 'stick of wood' (whence obsolete E shide) and OHG skīt, German Scheit 'log' (Klein s.v. ski). Nourai's 'Germanic skith' is thus AHD's *skidam / ON skíð, correctly glossed 'a cut branch or piece of wood used for walking on snow'; the semantic path is 'split piece of wood' > 'long board strapped to the foot'.\",\n \"derivation_fa\": \"واتکینز (AHD) ذیل ریشهٔ skei- «بریدن، شکافتن» (از گسترش‌های sek-) می‌نویسد: «صورت گستردهٔ *skeit-… ژرمنی *skidam در اسکاندیناوی کهن skíð ‚چوب، تختهٔ برف‌نوردی‘: SKI». skíð هم‌ریشه است با انگلیسی کهن scīd «تکه چوب» و آلمانی Scheit «کندهٔ چوب» (کلاین). پس «skith» نورایی همان *skidam/skíð است و تحول معنایی «چوبِ شکافته» ← «تختهٔ بلندِ بسته به پا» درست ثبت شده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/ski\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. skei-: '5. Extended root *skeit- in ... b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI. [Pok. skei- 919.]' — and the index line 'SKI skei-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ski (KLN_1966.txt line 35425)\", \"stance\": \"supports\", \"note\": \"'ski, n. — Norw., fr. ON. skid, ‚wooden billet, snowshoe‘, which is rel. to OE. scid, ‚stick of wood‘ ..., OHG. skit, MHG. schit, G. Scheit, ‚log‘, and to OE. sceadan, scadan, ‚to divide, separate‘.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 919 s.v. skei- 'to work with a sharp instrument, cut, separate'\", \"stance\": \"supports\", \"note\": \"the root Watkins cites; POK_full.txt block 'Root / lemma: skei-\\\\1 ... Page(s): 919'.\"}\n ]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"French\", \"words\": \"ski\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French ski (m.) is attested from 1841/1865 and, like English ski, was taken not from a Germanic proto-form but from Norwegian ski, the modern reflex of Old Norse skíð, when Norwegian skiing became an international sport in the second half of the 19th century. Nourai's arrow Germanic > French is therefore right in substance but skips the actual donor: Norwegian. The node carries no reference of its own in the book.\",\n \"derivation_fa\": \"«ski» فرانسوی (نیمهٔ دوم سدهٔ نوزدهم) — مانند ski انگلیسی — نه از صورتی ژرمنیِ بازسازی‌شده، بلکه مستقیماً از نروژیِ ski وام گرفته شده است؛ ski نروژی خود دنبالهٔ skíð اسکاندیناویِ کهن است و همراه با رواجِ ورزشِ نروژیِ اسکی به زبان‌های اروپایی رفت. پس پیکان «ژرمنی ← فرانسوی» در اصل درست است اما حلقهٔ واقعیِ وام‌گیری (نروژی) را نادیده گرفته؛ ادعا «با احتیاط پذیرفتنی» است. این گره در کتاب هیچ ارجاعی ندارد.\",\n \"sources\": [\"https://www.etymonline.com/word/ski\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no refs= in the book (confirmed on the printed page image, data/verification/sources/refs/ocr/BOOK/439.png).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ski (KLN_1966.txt line 35425)\", \"stance\": \"partial\", \"note\": \"'ski, n. — Norw., fr. ON. skid' — Klein makes Norwegian, not Germanic in general, the donor; the same applies to French.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. skei-, index 'SKI skei-'\", \"stance\": \"supports\", \"note\": \"AHD traces SKI to Germanic *skidam / Old Norse skidh, which is what Nourai's chart shows.\"}\n ]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"eskî «اسکی»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian اسکی eskī is a 20th-century European loan naming the winter sport; Mo'in tags it [فر.] 'French' and defines it 'یکی از ورزش‌های زمستانی که با کفش و چوب مخصوص روی برف ایستاده سر می‌خورند'. The prothetic e- is the regular Persian repair of an initial sk- cluster (cf. اسپانیا, استادیوم, اسکناس), and the final -ī renders French -i. So French ski > NP eskī is exactly right.\",\n \"derivation_fa\": \"«اسکی» وام‌واژه‌ای اروپایی و امروزی است؛ معین آن را با نشانهٔ [فر.] (فرانسوی) می‌آورد و چنین تعریف می‌کند: «یکی از ورزش‌های زمستانی که با کفش و چوب مخصوص روی برف ایستاده سر می‌خورند». «ا» آغازین همان مصوتِ کمکی است که فارسی برای شکستنِ خوشهٔ آغازینِ sk- می‌افزاید (مانند اسپانیا، استادیوم، اسکناس) و «ی» پایانی برابرِ -i فرانسوی است. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%DB%8C/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:272\", \"status\": \"supports\", \"note\": \"Mo'in vol. 1 p. 272 is not page-mapped online, but the entry text at abadis.ir (فرهنگ معین) reads '[فر.] یکی از ورزش‌های زمستانی که با کفش و چوب مخصوص روی برف ایستاده سر می‌خورند' — Mo'in's origin tag is French, exactly the arrow Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. اسکی via abadis.ir\", \"stance\": \"supports\", \"note\": \"origin tag [فر.] = French.\"},\n   {\"src\": \"VOP\", \"where\": \"Moshiri, Farhang-e vazheha-ye Orupayi dar Farsi\", \"stance\": \"silent\", \"note\": \"not obtainable (refs_online.json VOP kind='none': no scan, no ebook found).\"}\n ]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"ski\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English ski is first recorded 1883 (with an isolated 1755 instance), borrowed from Norwegian ski = Old Norse skíð 'billet of wood, snowshoe', from Proto-Germanic *skīdą, from PIE *skei- 'to cut, split' — the same root that gives OE scēadan 'to divide' and Greek skhízein. AHD's index line 'SKI skei-' is Nourai's authority and it agrees.\",\n \"derivation_fa\": \"«ski» انگلیسی از ۱۸۸۳ م. ثبت شده و از نروژیِ ski وام گرفته شده که همان skíð اسکاندیناویِ کهن «چوب، تختهٔ برف» است، از ژرمنیِ آغازین *skīdą و هندواروپاییِ *skei- «بریدن، شکافتن» — همان ریشه‌ای که انگلیسی کهن scēadan «جدا کردن» و یونانی skhízein از آن است. فهرست AHD نیز «SKI skei-» را می‌آورد، یعنی همان ارجاع نورایی. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/ski\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index: 'SKI skei-'; entry skei- '... Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. ski\", \"stance\": \"supports\", \"note\": \"'ski, n. — Norw., fr. ON. skid ...'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt finds no 'ski' headword (the word entered English after Skeat's core vocabulary).\"}\n ]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"crî-bellâre\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Late Latin crībellāre 'to sift' is a denominative of crībellum, the diminutive of crībrum 'sieve' (Ernout-Meillet s.v. cribrum: 'Dérivés: cribro,-ās ...; cribellum M.L.3331; cribellare M.L.3331'). Crībrum itself is from PIE *krei- 'to sieve, discriminate, distinguish' (suffixed *krei-dhro-), which Watkins files as 'Pok. 4. sker-, Section II. 945' — i.e. as part of the (s)ker- 'to cut' complex that Nourai gathers under Sek, so the placement is legitimate; Latin cernere 'to sift, separate' and Greek krī́nein belong to the same root.\",\n \"derivation_fa\": \"crībellāre لاتینیِ متأخر «الک کردن» فعلِ ساخته‌شده از crībellum، مصغرِ crībrum «غربال» است (ارنو-میه ذیل cribrum: «مشتق‌ها: cribro,-ās …؛ cribellum؛ cribellare»). خودِ crībrum از هندواروپایی *krei- «بیختن، جدا کردن، بازشناختن» است (صورت پسوندیِ *krei-dhro-) و واتکینز آن را به «پوکورنی ۴. sker-، بخش دوم، ص ۹۴۵» می‌برد، یعنی به همان خوشهٔ (s)ker- «بریدن» که نورایی ذیل Sek گرد آورده است؛ لاتینِ cernere «بیختن، جدا کردن» و یونانیِ krī́nein نیز از همین ریشه‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/garble\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. kreiə- 'to sieve, discriminate, distinguish': '1. ... b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GARBLE. ... [Pok. 4. sker-, Section II. 945.]' — and the index line 'GARBLE kreiə-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cribrum (LAT.txt line 11385 ff.)\", \"stance\": \"supports\", \"note\": \"'cribrum: crible ... Dérivés: cribro,-ās (formes tardives criblo ..., cribo ...); cribrarius; cribellum M.L.3331; cribellare M.L.3331; in-, per-cribro.' — confirms crībellāre as a real (Late) Latin verb.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. cribble (KLN_1966.txt line 9668)\", \"stance\": \"supports\", \"note\": \"'cribble, n., a coarse sieve. — F. crible, fr. Late L. cribellum, ‚a small sieve‘, dimin. of cribrum.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 945, (s)ker-4 Section II (skerī-)\", \"stance\": \"supports\", \"note\": \"the page Watkins cites for krei-; falls inside the (s)ker-4 'to cut' entry, pp. 938-947, one of the ranges Nourai cites for the root (POK:941).\"}\n ]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Arabic\", \"words\": \"ğarbala\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic غَرْبَلَ ḡarbala 'he sifted' is a denominative of غِرْبَال ḡirbāl 'sieve'. The Latin connection Nourai draws is the classical Western view and is what AHD p. 543 (s.v. garble) prints: Arabic gharbala < ghirbāl < Late Latin cribellum < Latin cribrum. Klein says the same ('fr. Arab. gharbala, ‚he sifted‘, fr. ghirbāl, sieve, ult. fr. Late L. cribellum'), and Etymonline repeats it. But it is not unopposed: Lokotsch no. 673 only notes that classical Arabic ġirbāl is 'dem lat. cribellum merkwürdig ähnlich' without deriving it, Skeat routes the word through Persian, and Wiktionary's Arabic entry (with Semitic-studies citations) derives ḡirbāl from Aramaic ʿarbālā, 'possibly a culture-word left from the Hurrian period in Nuzi, from which sieves have been excavated'. Phonetically Latin c- > Arabic ġ- is irregular, which is why the Aramaic route is now usually preferred. So: a well-attested scholarly derivation, but one modern Semitists dispute.\",\n \"derivation_fa\": \"فعل عربیِ «غَرْبَلَ» (بیختن) از اسمِ «غِربال» ساخته شده است. پیوندی که نورایی با لاتین می‌زند همان دیدگاه کلاسیکِ غربی است و مأخذِ خودِ او (AHD ذیل garble، ص ۵۴۳) نیز همان را می‌آورد: عربی ġarbala < ġirbāl < لاتینِ متأخر cribellum < لاتین cribrum؛ کلاین و اتیمانلاین هم همین زنجیره را دارند. اما این نظر بی‌رقیب نیست: لوکوچ (شمارهٔ ۶۷۳) تنها می‌نویسد که «غِربالِ عربیِ کلاسیک به‌طرزِ شگفتی به cribellum لاتین شبیه است» و آن را از لاتین نمی‌گیرد، اسکیت واژه را از راه فارسی می‌برد، و ویکی‌واژه (به استنادِ سامی‌شناسان) «غِربال» را وام از آرامیِ ʿarbālā و احتمالاً واژه‌ای فرهنگی از دورهٔ هوری در نوزی می‌داند. از نظر آوایی هم بدل شدنِ c لاتین به «غ» عربی بی‌قاعده است. پس ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84\", \"https://www.etymonline.com/word/garble\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:543\", \"status\": \"supports\", \"note\": \"AHD New College Edition p. 543 is the 'garble' page; the AHD etymology (reproduced by Etymonline and Klein) is 'Arabic gharbala, to sift, from ghirbāl, sieve, from Late Latin cribellum, diminutive of Latin cribrum, sieve'. Watkins's index confirms the root filing: 'GARBLE kreiə-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. garble (KLN_1966.txt line 15792)\", \"stance\": \"supports\", \"note\": \"'garble, tr. v. ... fr. Sp. garbillar ..., fr. Arab. gharbala, ‚he sifted‘, fr. ghirbāl, sieve, ult. fr. Late L. cribellum, dimin. of L. cribrum, ‚sieve‘, which is rel. to cernere.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs, no. 673 (LKT.txt line 1666)\", \"stance\": \"partial\", \"note\": \"'673. Ar. ġarbāl: Klassisch-ar. ġirbāl ‚Sieb‘ [dem lat. cribellum merkwürdig ähnlich]; hieraus siz. garbula ..., it. garbellare ‚durchsieben‘ ..., frz. grabeler, sp. garbillo ‚Sieb‘.' — Lokotsch records only the resemblance, and makes Arabic the source of the European words.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Garble (SKT.txt line 7405)\", \"stance\": \"partial\", \"note\": \"'Garble ... (F. — Span. — Arab.) ... — Span. garbillo, a coarse sieve. — Pers. ghirbāl ... Arab. ghirbāl, a sieve; Arab. gharbala, sifting, searching.' — no Latin source at all; Skeat even inserts Persian.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an — grep 'غربال' in FVQ.txt/FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"no entry (the word is not Qur'anic).\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba — grep 'غربا' in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"not listed among the Persian words Arabicized, i.e. Addi Shir does not claim a Persian origin.\"}\n ]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"ğarbâl «غربال ( غربیل )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian غربال ḡarbāl / ḡerbāl (variant غربیل ḡarbīl, dialect گربال garbāl, غلبیر ḡalbir) 'sieve' is a borrowing from Arabic غِرْبَال ḡirbāl, with the Arabic pattern fiʿʿāl retained and the usual Persian dialectal variants (r/l metathesis in ḡalbir, -āl/-īl alternation). Mo'in gives it as a plain noun '(غَ یا غِ) (اِ.) وسیله‌ای مشبک … برای جدا کردن اجزای ریز و درشت یک جسم، الک'. Dehkhoda adds a different account — that the Persian form is گربال and that غِربال is its Arabicized (معرّب) shape — which would make the word a Persian→Arabic→Persian round trip; Wiktionary, by contrast, simply has 'Persian ġarbâl, borrowed from Arabic غِرْبَال'. Either way the immediate Persian source is the Arabic word, as the chart shows.\",\n \"derivation_fa\": \"«غربال» (گونه‌ها: غربیل، گربال، غلبیر) وام‌واژه‌ای است از عربیِ «غِربال» بر وزن فِعّال؛ گونه‌های فارسی با قلب r/l در «غلبیر» و تناوبِ ـال/ـیل پدید آمده‌اند. معین آن را چنین می‌آورد: «(غَ یا غِ) (اِ.) وسیله‌ای مشبک یا سوراخ‌سوراخ برای جدا کردن اجزای ریز و درشت یک جسم، الک». دهخدا روایت دیگری دارد و «گربال» را صورتِ فارسی و «غِربال» را معرّبِ آن می‌شمارد، یعنی رفت‌وبرگشتِ فارسی ← عربی ← فارسی؛ ویکی‌واژه اما ساده می‌گوید «فارسی غربال، وام از عربی غِربال». به هر روی سرچشمهٔ بی‌واسطهٔ واژهٔ فارسی همان واژهٔ عربی است و نمودار درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84\", \"https://abadis.ir/fatofa/%D8%BA%D8%B1%D8%A8%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:2397\", \"status\": \"supports\", \"note\": \"Mo'in vol. 2/3 p. 2397 is not page-mapped online; the entry read at abadis.ir (فرهنگ معین) gives '(غَ یا غِ) (اِ.) وسیله‌ای مشبک یا سوراخ سوراخ برای جدا کردن اجزای ریز و درشت یک جسم، الک' — the gloss and both vowel readings Nourai prints, with the variant غربیل.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. غربال via abadis.ir\", \"stance\": \"supports\", \"note\": \"gloss 'sieve'; no non-Arabic origin claimed.\"},\n   {\"src\": \"BQT\", \"where\": \"Dehkhoda note reproduced with the Mo'in entry at abadis.ir\", \"stance\": \"partial\", \"note\": \"Dehkhoda derives غربال from Persian گربال and calls غِربال the Arabicized form, while also pointing at Latin criblum/cribrum and French crible — i.e. a Persian→Arabic→Persian round trip rather than a one-way Arabic loan.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen — grep 'غربال/girbal' in PLA_pages.txt\", \"stance\": \"silent\", \"note\": \"not listed, i.e. Asbaghi does not count ġirbāl among the Persian loanwords in Arabic.\"}\n ]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A pass-through box with no word, standing for the mass of Germanic verbs and nouns built on the *sek-/*sker-/*skel-/*skep-/*skei- 'cut' complex, glossed by Nourai's own NOTE 'words meaning to cut, shape, peel or skin, etc.'. This is an accurate summary of Watkins's four 'extended roots' of sek- (sked-, skei-, sker-1, sker-4) plus skel-1 and skep-, all of which have their heaviest Germanic representation.\",\n \"derivation_fa\": \"این خانه واژه‌ای ندارد و تنها گذرگاهی است برای انبوهِ فعل‌ها و نام‌های ژرمنیِ ساخته‌شده بر خوشهٔ *sek-/*sker-/*skel-/*skep-/*skei- «بریدن»؛ یادداشتِ خودِ نورایی نیز همین را می‌گوید: «واژه‌هایی به معنی بریدن، شکل دادن، پوست کندن». این خلاصه با آنچه واتکینز «ریشه‌های گستردهٔ sek-» می‌نامد (sked-، skei-، sker-1، sker-4) به‌علاوهٔ skel-1 و skep- می‌خواند و بیشترین بازتابِ آن‌ها هم در ژرمنی است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. sek-: '... See also extended roots sked-, skei-, sker-1, sker-4. [Pok. 2. sék- 895, sken-(d)- 929.]' — the Germanic material is listed under each of those.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 923-927 (s)kel-1 'to cut', 930-933 (s)kep-2, 938-947 (s)ker-4 'to cut'\", \"stance\": \"supports\", \"note\": \"each entry's Material section is dominated by Germanic forms (Gothic skilja, ON skel, OHG scala, OE scield, scieran, sceafan ...).\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 595 ff. s.v. (s)qel-\", \"stance\": \"supports\", \"note\": \"'ahd. scelifa, mhd., nhd. mdartl. schelfe ‚häutige Schale‘, mnd. schelver ‚abgeblättertes Stück‘ ...; aisl. skjalf ‚Bank‘, ags. scelfe ...' — the same Germanic cluster.\"}\n ]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"shelf, half, shape, shave, skin, skirt, saw, scrap, sharp, shirt, shears, score, short\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every word in the list is in Watkins's index under one of the roots Nourai has gathered under Sek, and the assignments are: SHELF skel-1 (Gmc. *skelf- 'split piece of wood'), HALF skel-1 (OE healf, literally 'divided'), SHAPE skep- (OE gesceap '< cutting'), SHAVE skep- (OE sceafan 'to scrape, pare'), SKIN sek- (ON skinn '< the flayed hide'), SKIRT sker-1 (ON skyrta), SAW1 sek- (OE sagu, the cutting tool), SCRAP1 sker-1 (ON skrap '\\\"pieces\\\", remains'), SHARP sker-1 (OE scearp 'cutting'), SHIRT sker-1 (OE scyrte '< cut piece'), SHEARS sker-1 (OE scēar), SCORE sker-1 (ON skor 'notch, tally, twenty'), SHORT sker-1 (OE scort, '\\\"cut\\\", short'). The one qualification is that these are five different Indo-European roots in AHD (sek-, skel-1, skep-, sker-1), not a single one; Nourai's umbrella Sek is his own editorial grouping, explicitly licensed by AHD's cross-reference 'See also extended roots'.\",\n \"derivation_fa\": \"هر سیزده واژهٔ این فهرست در نمایهٔ واتکینز ذیل یکی از ریشه‌هایی است که نورایی زیر عنوانِ Sek گرد آورده است: SHELF و HALF ذیل skel-1 (انگلیسی کهن healf در اصل «تقسیم‌شده»)، SHAPE و SHAVE ذیل skep-، SKIN و SAW ذیل خودِ sek-، و SKIRT، SCRAP، SHARP، SHIRT، SHEARS، SCORE و SHORT ذیل sker-1 (انگلیسی کهن scyrte «تکهٔ بریده»، scort «بریده، کوتاه»، اسکاندیناویِ کهن skor «شکاف، خط شمار، بیست»). تنها نکته این است که این‌ها در AHD چهار-پنج ریشهٔ جداگانه‌اند نه یکی؛ گردآوریِ آن‌ها زیر Sek کارِ ویراستارانهٔ نورایی است که خودِ AHD با عبارتِ «ریشه‌های گسترده را نیز ببینید» به آن اجازه داده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 index lines, grepped verbatim: 'SHELF skel-1', 'HALF skel-1', 'SHAPE skep-', 'SHAVE skep-', 'SKIN sek-', 'SAW! sek-', 'SHARP sker-1', 'SHIRT sker-1', 'SKIRT sker-1', 'SHEARS'/'SCORE'/'SHORT' under sker-1 in the entry text, 'SCRAP! sker-1'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, s.vv. shelf, half, shape, shave, shirt, short\", \"stance\": \"supports\", \"note\": \"Klein's Germanic etymologies agree (e.g. cribble/shelf group from the 'split' root); no competing origin proposed for any item on the list.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 923-927 ((s)kel-1), 930-933 ((s)kep-2), 938-947 ((s)ker-4)\", \"stance\": \"supports\", \"note\": \"(s)kel-1 explicitly lists 'Gothic halts, Old Icelandic halfr, Old English healf ... (actually ‚divided‘)' and 'Middle Low German schelf, shelf'.\"}\n ]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Latin\", \"words\": \"scîre\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin scīre 'to know' is traditionally explained as 'to separate one thing from another, distinguish', from PIE *skei- 'to cut, split' — the same root as Greek skhízein 'to split' and OE scēadan 'to divide'. Watkins files it under skei- (index 'CONSCIENCE skei-', 'SCIENCE skei-'), and Mann, IEC 1154, gives the same: 's. skeiiō ... ‚divide, split, distinguish, choose‘ ... Lat. scio, scire, v. ‚ordain, appoint; know, be skilled in‘'. Nourai's gloss 'to know, distinguish' reproduces exactly that double sense.\",\n \"derivation_fa\": \"فعلِ لاتینِ scīre «دانستن» را به‌طور سنّتی از هندواروپاییِ *skei- «بریدن، شکافتن» می‌گیرند، با تحوّلِ معناییِ «جدا کردنِ چیزی از چیزی ← بازشناختن ← دانستن»؛ هم‌ریشه‌اش یونانیِ skhízein «شکافتن» و انگلیسی کهن scēadan «جدا کردن» است. واتکینز آن را ذیل skei- می‌آورد («SCIENCE skei-»، «CONSCIENCE skei-») و مان نیز در ص ۱۱۵۴ ذیل skeiiō «جدا کردن، شکافتن، بازشناختن، برگزیدن» می‌نویسد «Lat. scio, scire … know, be skilled in». معنایی که نورایی داده («to know, distinguish») دقیقاً همین دوگانگی است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/science\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. skei- 'to cut, split' [Pok. skei- 919], with the index lines 'SCIENCE skei-' and 'CONSCIENCE skei-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC p. 1154 s.v. skeiiō (IEC.txt leaf 638)\", \"stance\": \"supports\", \"note\": \"'skeiiō (skeiō, skheiio, skheiō) “divide, split, distinguish, choose” ... Lat. scio, scire, v. “ordain, appoint; know, be skilled in”; Br. cf. skeZa, v. “cut”; cf. skiant, f. “mind”'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 919 s.v. skei-\", \"stance\": \"supports\", \"note\": \"the entry Watkins cites for scīre; 'skei- (to cut, separate) ... to work with a sharp instrument'.\"}\n ]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"science, conscience, nice\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Science: Middle English (mid-14th c.) from Old French science, from Latin scientia 'knowledge', abstract noun to sciēns, present participle of scīre. Conscience: 13th c. Old French conscience, from Latin conscientia (con- 'with' + scientia), a calque on Greek syneídēsis. Nice: from Old French nice 'silly, foolish', from Latin nescius 'not-knowing, ignorant' (ne- 'not' + the stem of scīre); the English sense drifted 'foolish' > 'fussy, fastidious' (14th-16th c.) > 'agreeable' (18th c.). All three are under skei- in Watkins.\",\n \"derivation_fa\": \"science از فرانسهٔ کهن science و آن از لاتینِ scientia «دانش»، اسمِ معنی از scīre؛ conscience از لاتینِ conscientia (con- «با» + scientia) که خود گرته‌ای است از یونانیِ syneídēsis؛ و nice از فرانسهٔ کهنِ nice «نادان، ساده» و آن از لاتینِ nescius «نادان» (ne- «نه» + ستاکِ scīre)، با تحول معناییِ جالبِ «نادان ← سخت‌گیر و مو‌شکاف ← دلپذیر» در انگلیسیِ سده‌های چهاردهم تا هجدهم. هر سه در فرهنگ واتکینز ذیل skei- آمده‌اند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/science\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index: 'SCIENCE skei-', 'CONSCIENCE skei-', 'NICE ne' (nice is filed under the negative prefix *ne- because of nescius, but its second element is scīre < skei-).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. science, conscience, nice\", \"stance\": \"supports\", \"note\": \"Klein derives nice from OF. nice 'simple, silly', fr. L. nescius, and science from L. scientia, to scire.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.vv. Science, Nice\", \"stance\": \"supports\", \"note\": \"same chain: Nice < O.F. nice < L. nescius, from ne + scire.\"}\n ]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Latin\", \"words\": \"carô; carni-levare\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin carō, carnis f. originally 'a piece, portion (of sacrificial meat)', then 'flesh' — the older sense is still visible in Oscan carneis 'partis', Umbrian karu 'pars', kartu 'distribuito' (Ernout-Meillet s.v. caro). It is an -n- enlargement of a root noun from *(s)ker- 'to cut', the root of Greek keírō 'I cut', Latin corium, curtus, cortex, with an s-initial doublet in OIr. scaraim 'I separate', OHG sceran 'to cut'. Medieval Latin carnelevāre / carnelevāmen 'the removing of meat', attested in Milanese carnelevale and Old Pisan carnelevare, named the last feast before the Lenten fast; Nourai's ☞Legwh points correctly to levāre 'to lift, take away' under a different root (PIE *legʷh- 'light in weight').\",\n \"derivation_fa\": \"carō, carnis در لاتین نخست «پاره، بهره (از گوشتِ قربانی)» بوده و سپس «گوشت»؛ معنیِ کهن‌تر هنوز در اسکی carneis «partis» و اومبریایی karu «pars» و kartu «تقسیم شد» پیداست (ارنو-میه). این واژه گسترشِ -n-یِ یک اسمِ ریشه‌ای از *(s)ker- «بریدن» است؛ هم‌ریشهٔ یونانیِ keírō «می‌برم» و لاتینِ corium، curtus، cortex، با گونهٔ s-دار در ایرلندیِ کهن scaraim «جدا می‌کنم» و آلمانیِ عالیِ کهن sceran «بریدن». ترکیبِ لاتینیِ میانه carnelevāre/carnelevāmen «برداشتنِ گوشت» (میلانی carnelevale، پیزاییِ کهن carnelevare) نامِ آخرین جشنِ پیش از روزهٔ بزرگ بود؛ ارجاعِ «☞Legwh» نورایی هم درست است، زیرا levāre «برداشتن» به ریشهٔ دیگری (*legʷh- «سبک») می‌رسد. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/carnival\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. sker-1 'To cut': '9. Variant form *kar- in Latin carō (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCARNATE. [Pok. sker- 938.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. caro (LAT.txt lines 10012-10050)\", \"stance\": \"supports\", \"note\": \"'le sens de “part” de ce mot ... est visible en osco-ombrien: osq. carneis “partis”, ombr. karu “pars” ... Le mot italique est l’élargissement en -n- d’un thème racine; la racine est celle de κείρω “je coupe” ... et par suite de lat. corium, curtus, cortex ... Elle a un doublet à s- initial: irl. scaraim “je sépare”, v.h.a. sceran “couper”, lit. skiriu.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 938-947 s.v. (s)ker-4 'to cut'\", \"stance\": \"supports\", \"note\": \"the root Watkins cites; Latin caro belongs to the *(s)ker- 'cut/portion' family there.\"}\n ]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"French\", \"words\": \"carnaval\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French carnaval (16th c.) is a borrowing from Italian carnevale, not a direct continuation of a Latin form: 'carnival, 1540s, from French carnaval, from Italian carnevale ‚Shrove Tuesday‘, from older Italian forms such as Milanese carnelevale, Old Pisan carnelevare “to remove meat”' (Etymonline); Klein has the same route but with the folk-etymological Medieval Latin carne, vale 'O flesh, farewell!', which modern scholarship rejects in favour of carnelevāre. So the arrow Latin > French is right in direction but omits the Italian stage where the word was actually formed — the reason the chart shows carnaval and not a French *charnelever.\",\n \"derivation_fa\": \"«carnaval» فرانسوی (سدهٔ شانزدهم) نه دنبالهٔ مستقیمِ صورتی لاتین، بلکه وام‌واژه‌ای است از ایتالیاییِ carnevale؛ اتیمانلاین: «۱۵۴۰ م.، از فرانسویِ carnaval، از ایتالیاییِ carnevale ‚سه‌شنبهٔ توبه‘، از صورت‌های کهن‌ترِ میلانی carnelevale و پیزاییِ کهن carnelevare ‚برداشتنِ گوشت‘». کلاین همین مسیر را می‌دهد اما با ریشه‌شناسیِ عامیانهٔ لاتینیِ میانه carne vale «ای گوشت، بدرود!» که پژوهشِ امروزی آن را به سودِ carnelevāre کنار گذاشته است. پس جهتِ پیکان «لاتین ← فرانسوی» درست است ولی حلقهٔ ایتالیایی — جایی که واژه واقعاً ساخته شد — افتاده است؛ ادعا «با احتیاط پذیرفتنی» است.\",\n \"sources\": [\"https://www.etymonline.com/word/carnival\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins's index files CARNIVAL under legh- (for -levare) and lists it among the sker-1 derivatives of carō, but the AHD dictionary entry itself routes the word 'French carnaval, from Italian carnevale' — the Italian stage that the chart leaves out.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. carnival (KLN_1966.txt)\", \"stance\": \"partial\", \"note\": \"'carnival, n. — F. carnaval, fr. It. carnevale, fr. ML. carne, vale, ‚O flesh, farewell!‘' — Italian intermediary confirmed; Klein's ML. carne vale is the folk etymology now replaced by carnelevare.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"no entry — the word is not an Orientalism, as expected.\"}\n ]})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Persian\", \"words\": \"kârnâvâl «کارناوال»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کارناوال kārnāvāl is a 20th-century loan directly from French carnaval, as its vowels show: French [karnaval] with three short a's is rendered with Persian long ā throughout (kārnāvāl), the standard treatment of French a in Persian loanwords, and the stress-final shape rules out English carnival as the donor. Mo'in tags it [فر.] 'French' and defines it 'کاروان شادی، کاروانی که در ایام معینی از سال با لباس‌های مضحک برای تفریح و سرگرمی به راه می‌افتند'.\",\n \"derivation_fa\": \"«کارناوال» وامی امروزی و مستقیماً از فرانسویِ carnaval است؛ آوایش هم گواه است: سه «a»ی کوتاهِ فرانسوی در فارسی به «ا»ی کشیده بدل شده (kārnāvāl)، همان رفتاری که فارسی با aی فرانسوی دارد، و همین صورت، انگلیسیِ carnival را از گزینه بودن بیرون می‌گذارد. معین آن را با نشانهٔ [فر.] می‌آورد: «کاروان شادی، کاروانی که در ایام معینی از سال با لباس‌های مضحک برای تفریح و سرگرمی به راه می‌افتند». ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%B1%D9%86%D8%A7%D9%88%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"VOP:269\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vazheha-ye Orupayi dar Farsi (1371) is not available in any form — refs_online.json records kind='none' after a renewed 2026-09 search of archive.org, ketabnak and noorlib. Checked instead against Mo'in via abadis.ir, which tags کارناوال [فر.] = French.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کارناوال via abadis.ir\", \"stance\": \"supports\", \"note\": \"origin tag [فر.] = French; gloss 'کاروان شادی ...'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no entry — the book covers inherited Indo-European vocabulary, not modern European loans.\"}\n ]})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\", \"words\": \"carnival, carnivorous\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English carnival (1540s) is from French carnaval < Italian carnevale, ultimately Latin carō/carn- + levāre; the modern sense 'travelling amusement fair' is American, 1926. Carnivorous (1640s) is from Latin carnivorus 'flesh-eating', carn- + vorāre 'to devour' (PIE *gʷerə- 'to swallow'), coined as a rendering of Greek sarkophágos. Both keep the Latin stem carn- from the *(s)ker- 'cut, portion' root, so Nourai's arrow from the Latin box is correct.\",\n \"derivation_fa\": \"carnival انگلیسی (۱۵۴۰ م.) از فرانسویِ carnaval و آن از ایتالیاییِ carnevale است، در نهایت از carō/carn- لاتین + levāre؛ معنیِ امروزیِ «شهربازیِ سیّار» آمریکایی و از ۱۹۲۶ م. است. carnivorous (۱۶۴۰ م.) از لاتینِ carnivorus «گوشت‌خوار» است، carn- + vorāre «بلعیدن» (از هندواروپاییِ *gʷerh₃-)، که خود ترجمهٔ یونانیِ sarkophágos بوده است. هر دو ستاکِ لاتینیِ carn- را از ریشهٔ *(s)ker- «بریدن، پاره» نگه داشته‌اند، پس پیکانِ نورایی از خانهٔ لاتین درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/carnival\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. sker-1: 'Latin carō (stem carn-), flesh: CARNAGE, CARNAL, ..., CARNIVAL, ...; CARNIVOROUS, INCARNATE'; index 'CARNIVAL legh-' records the second element levāre.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. carnival, carnivorous\", \"stance\": \"supports\", \"note\": \"'carnival, n. — F. carnaval, fr. It. carnevale'; carnivorous from L. carnivorus, fr. caro, gen. carnis + vorare.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. caro\", \"stance\": \"supports\", \"note\": \"'Pline emploie carniuorus pour traduire σαρκοφάγος' — the Latin model of English carnivorous.\"}\n ]})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Indo-European\", \"words\": \"Skěl\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The root is real: PIE *(s)kel- 'to cut' (Pokorny 923-927, Watkins skel-1), whose Germanic nominal derivatives already include ON skil 'reason, discernment, knowledge (< \\\"incisiveness\\\")' and hence English SKILL, and Swedish skäl 'faculty of reason'. Nourai's particular form and gloss — 'Skěl : division, part, thought' — is Mann's: IEC 1155 has 'skēl- (long-grade of type skel- (1) ...) ‚division, part; cut, separation; discernment‘', and the very first cognates Mann lists there are 'Per. sikal ‚thought‘; sikalidan, inf. ‚think‘'. So the node reproduces its cited source faithfully. The reservation is that Mann's inclusion of the Persian words is not shared by Iranianists (see node 20): Cheung 2007 and Nyberg take sigāl- from us- + kar-, so the 'thought' element in the gloss rests on a derivation most specialists reject, even though *(s)kel- 'cut' > 'discern' is a normal development elsewhere.\",\n \"derivation_fa\": \"خودِ ریشه واقعی است: هندواروپاییِ *(s)kel- «بریدن» (پوکورنی ۹۲۳–۹۲۷، واتکینز skel-1) که مشتق‌های ژرمنیِ آن از پیش معنیِ «تشخیص» را دارند — اسکاندیناویِ کهن skil «خرد، تشخیص، دانش» (از «تیزیِ برش») و از آن SKILL انگلیسی، و سوئدیِ skäl «قوّهٔ عقل». اما صورت و معنیِ ویژه‌ای که نورایی آورده («Skěl: بخش، پاره، اندیشه») از آنِ مان است: در ص ۱۱۵۵ آمده «skēl- (گونهٔ کشیدهٔ skel- (1)) ‚بخش، پاره؛ برش، جدایی؛ تشخیص‘» و نخستین هم‌ریشه‌هایی که مان می‌آورد همین «Per. sikal ‚thought‘؛ sikalidan ‚think‘» است. پس گره مأخذِ خود را وفادارانه بازتاب می‌دهد. تحفظ در اینجاست که ایران‌شناسان (چونگ، نیبرگ) «سگالیدن» را از us- + kar- می‌گیرند (نگاه کنید به گرهٔ ۲۰)، پس جزءِ «اندیشه» در این معنی بر تحلیلی استوار است که بیشترِ متخصصان نمی‌پذیرند. «با احتیاط پذیرفتنی».\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1155\", \"status\": \"supports\", \"note\": \"Mann, IEC printed p. 1155 (IEC.txt leaf 638-639): 'skēl- (long-grade of type skel- (1), q.v.) “division, part; cut, separation; discernment” — Per. sikal “thought”; sikalidan, inf. “think”; Arm. xil “inquiry”; Alb. i hollë “thin, fine” ...' — Nourai's gloss and his Persian branch, verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 923-927 s.v. (s)kel-1 'to cut'\", \"stance\": \"partial\", \"note\": \"the root exists with the meaning 'schneiden', and the 'discernment' sense is present in the Germanic material (ON skil, Gothic skilja), but Pokorny lists no Iranian 'think' word under it.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. skel-1 'Also kel-. To cut.'\", \"stance\": \"partial\", \"note\": \"'6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “incisiveness”): SKILL' — supports 'division, part' and the semantic bridge to 'thought', but has no Iranian material.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 595 ff. s.v. (s)qel-\", \"stance\": \"partial\", \"note\": \"same root, same Germanic 'discern' words, no Iranian 'think' branch.\"}\n ]})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Old Iranian\", \"words\": \"kar 3, kâr 3; us-kâr-a\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Old Iranian preform is right, the Indo-European parent is not. Abolghasemi, Fe'l-ha-ye farsi-ye Dari p. 61 — Nourai's own source — reads: 'سگال ← فارسی میانه uskār < ایرانی باستان *us-kār-a ... us پیشوند فعلی است. kār صورت بالندهٔ ریشه است. صورت افزودهٔ آن kar است، به معنی اندیشیدن', i.e. NP segāl < MP uskār < Old Iranian *us-kār-a, with us- a verbal prefix and kār the lengthened grade of a root kar- 'to think' (his 'kar 3', numbered to distinguish it from kar- 'to do'). That much is standard. But modern Iranian etymology does not treat that kar- as a separate root descending from *(s)kel-: Cheung, Etymological Dictionary of the Iranian Verb (2007), files BMP ʾwskʾl- /uskar-/ 'to think, consider, discuss' and NP sigālīdan/sigāl- under *kar 'to do, make' with the preverb *us-, and gives the Indo-European etymon as '*kʷer- “to do, make, construct”, LIV 391 | Pok. 641'. Nyberg agrees on the Iranian side ('Belongs undoubtedly to Av. 2kar-... *ws- can only be the old prev. us-'). So the arrow IE Skel > Old Iranian kar is rejected by current scholarship in favour of PIE *kʷer-.\",\n \"derivation_fa\": \"صورتِ ایرانیِ باستان درست است ولی ریشهٔ هندواروپاییِ آن نه. ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» ص ۶۱ — همان مأخذِ نورایی — می‌نویسد: «سگال ← فارسی میانه uskār < ایرانی باستان *us-kār-a … us پیشوند فعلی است. kār صورت بالندهٔ ریشه است. صورت افزودهٔ آن kar است، به معنی اندیشیدن». تا اینجا پذیرفته است. اما ریشه‌شناسیِ امروزیِ ایرانی این kar را ریشه‌ای جدا و بازماندهٔ *(s)kel- نمی‌داند: چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» (۲۰۰۷) فارسی میانهٔ ʾwskʾl- /uskar-/ «اندیشیدن، سنجیدن» و فارسیِ «سگالیدن/سگال-» را ذیل *kar «کردن، ساختن» با پیشوندِ *us- می‌آورد و ریشهٔ هندواروپایی را «*kʷer- ‚کردن، ساختن‘، LIV 391، پوکورنی ۶۴۱» می‌گذارد. نیبرگ نیز در سمتِ ایرانی همین را می‌گوید («بی‌گمان به kar-ِ دومِ اوستایی می‌رسد؛ ws- جز پیشوندِ کهنِ us- نمی‌تواند باشد»). پس پژوهش امروزی پیکانِ «Skel ← kar» را رد می‌کند و به جای آن *kʷer- را می‌نشاند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%A7%D9%84%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:61\", \"status\": \"supports\", \"note\": \"Abolghasemi, printed p. 61 = FFD PDF page 66 (FFD_pages.txt \\\\f-block 65, tagged '[pdf page 66]'), s.v. سکالیدن: 'سگال ← فارسی میانه uskār < ایرانی باستان *us-kār-a. برای us → آرای. us پیشوند فعلی است. kār صورت بالندهٔ ریشه است. صورت افزودهٔ آن kar است، به معنی «اندیشیدن».' — exactly Nourai's 'kar 3, kâr 3 : to think ; us-kâr-a'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, s.v. *kar 'to do, make', pp. 235-239 (CHEUNG.txt lines 15768-15910; index 'sigalidan/sigal-, 238')\", \"stance\": \"contradicts\", \"note\": \"'*MIDDLE PERSIAN: ... || (+ *us-) BMP ʾwskʾl- /uskar-/ (caus.) “to think, consider, discuss”' and '*NWIR: ... (+ *us-) NP sigālidan/sigāl- “to think, meditate (mischief)”'; the entry closes '*PIE *kʷer- “to do, make, construct” = LIV: 391 | Pok.: 641'. Not *skel-.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. uskārtan (NYB_vol2_glossary.txt line 3858)\", \"stance\": \"contradicts\", \"note\": \"'uskārtan to consider, to deliberate, to discuss ... Belongs undoubtedly to Av. (448) 2kar-, v. 2kartak, *kartan, hangārtan, nikēritan, patkārītan. — ʾws- can only be the old prev. us-, which would, it is true, appear here as as-.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. kar- (col. 442 ff., 448)\", \"stance\": \"partial\", \"note\": \"Bartholomae's numbered Av. kar- entries are the authority Nyberg cites ('Av. (448) 2kar-'); the Avestan verb is a kar-, not a skel-/skar- form.\"}\n ]})\n\nnodes.append({\n \"id\": 21, \"lang\": \"Pahlavi\", \"words\": \"uskâr, uskârd\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi ʾwskʾl-tn' = uskārdan, present stem uskār-, 'to think, consider, discuss', with the perfect participle uskārd (BMP ʾwskʾlt), and the abstract uskārišn 'consideration, reflection'. MacKenzie's Concise Pahlavi Dictionary prints 'uskārdan, uskār- [ʾwskʾl-tn' | J ~, (N sigāl-)] think, consider, discuss. ~išn(īh): consideration, reflection' — note that MacKenzie himself gives the New Persian continuation sigāl-, i.e. the very next arrow in the chart. Nyberg documents the word in real texts (Kārnāmag VI.20, VIII.2; Vīdēvdād commentary). The form is the preverb us- 'up, out' + the causative stem kār- (Old Iranian *us-kār-aya-), with the regular Pahlavi -rd past stem.\",\n \"derivation_fa\": \"پهلویِ کتابیِ ʾwskʾl-tn' = uskārdan، ستاکِ حال uskār-، «اندیشیدن، سنجیدن، به بحث گذاشتن»، با اسم مفعولِ uskārd و نامِ مصدرِ uskārišn «سنجش، تأمّل». مکنزی در «فرهنگ کوچک پهلوی» می‌آورد: «uskārdan, uskār- [ʾwskʾl-tn'] … think, consider, discuss» و خودش دنبالهٔ فارسیِ نو یعنی sigāl- را هم در همان مدخل می‌گذارد — یعنی دقیقاً پیکانِ بعدیِ نمودار. نیبرگ نمونه‌های متنی می‌دهد (کارنامه ششم ۲۰ و هشتم ۲، تفسیرِ وندیداد). ساختِ واژه: پیشوندِ us- «بر، بیرون» + ستاکِ سببیِ kār- (ایرانیِ باستان *us-kār-aya-) با ستاکِ گذشتهٔ قاعده‌مندِ -rd در پهلوی. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%A7%D9%84%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:61\", \"status\": \"supports\", \"note\": \"Abolghasemi p. 61: 'سگال ← فارسی میانه uskār ...' and 'مادهٔ ماضی ... در فارسی میانه uskārd است، از ایرانی باستان *us-kār-ta' — both stems uskār / uskārd, exactly as Nourai prints them.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 84 (PHD.txt line 601; PHD_mackenzie.txt line 5070)\", \"stance\": \"supports\", \"note\": \"'uskārdan, uskār- [ʾwskʾl-tn' | J ~, (N sigāl-)] think, consider, discuss. ~išn(īh): consideration, reflection.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 3856-3858, 7390)\", \"stance\": \"supports\", \"note\": \"'uskār [ʾwskʾl] consideration, deliberation'; 'uskārišn ... theoretical speculation'; 'uskārtan to consider, to deliberate, to discuss: apāk spāhpatān uskārt ... KnS VI.20'; and the cross-reference 'sikāl, sigāl: uskārtan'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *kar, Middle Persian section\", \"stance\": \"supports\", \"note\": \"'(+ *us-) BMP ʾwskʾl- /uskar-/ (caus.) “to think, consider, discuss”'; forms cited: pres. 3pl. ʾwskʾlynd /uskarēnd/, ptcp. ʾwskʾlt /uskard/.\"}\n ]})\n\nnodes.append({\n \"id\": 22, \"lang\": \"Persian\", \"words\": \"segâl «سیگال ( سیکال )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MP uskār(dan) gives NP سگال segāl / sigāl (also spelt سیگال, سیکال) 'thought, design, (usually evil) intention', with the verb سگالیدن segālīdan 'to think, plot' and the verbal noun سگالش segāleš. Phonologically the initial cluster of us-kār- was reduced: the u- of the preverb was lost and the surviving s- attached to the following stem, whence si-/se-, while intervocalic -k- was voiced to -g- (the regular NP lenition seen in خاک/xāk-type pairs and in Nyberg's variant Paz. auaškardan); MacKenzie's entry already prints '(N sigāl-)' as the Persian continuation of uskār-. Nyberg's glossary cross-refers 'sikāl, sigāl: uskārtan'. The pejorative colouring Nourai notes ('a bad idea') is real and old — Cheung glosses NP sigālīdan 'to think, meditate (mischief)'. The Nezāmi line quoted in the entry ('باخود غزلی همی سگالید') shows the verb in classical use.\",\n \"derivation_fa\": \"«سگال / سیگال» (گونه‌های نوشتاری: سیگال، سیکال) «اندیشه، قصد (بیشتر بد)» از فارسی میانهٔ uskār(dan) است، با فعلِ «سگالیدن» و نامِ مصدرِ «سگالش». از نظر آوایی خوشهٔ آغازینِ us-kār- ساده شده است: واکهٔ پیشوند افتاده و «س» به ستاکِ پسین چسبیده و صورتِ si-/se- پدید آمده، و «ک» میان‌واکه‌ای به «گ» نرم شده است (همان نرم‌شدگیِ قاعده‌مندِ فارسی نو). مکنزی خود در مدخلِ uskār- دنبالهٔ فارسیِ «(N sigāl-)» را آورده و نیبرگ در واژه‌نامه ارجاع می‌دهد «sikāl, sigāl: uskārtan». بارِ منفیِ معنایی که نورایی یادآور شده («اندیشهٔ بد») نیز کهن و واقعی است؛ چونگ آن را «to think, meditate (mischief)» معنی می‌کند. بیتِ نظامی که در همان خانه نقل شده («باخود غزلی همی سگالید») کاربردِ کلاسیکِ فعل را نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%A7%D9%84%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:61\", \"status\": \"supports\", \"note\": \"Abolghasemi p. 61 heads the article سکالیدن and notes 'سگالید مادهٔ ماضیِ جعلی است، از مادهٔ مضارع ساخته شده است' before deriving سگال from MP uskār — Nourai's chain and his extra forms سگالیدن/سگالش.\"},\n   {\"ref\": \"MON:1903\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 2 p. 1903 is not page-mapped online (vajehyab/abadis give entry text without pagination) and the local MON OCR (MON_part1/2.txt) is unusable for Persian search. The gloss was checked instead against MacKenzie, Nyberg and Cheung, all of which agree.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. uskārdan\", \"stance\": \"supports\", \"note\": \"'uskārdan, uskār- [...| J ~, (N sigāl-)]' — MacKenzie himself names NP sigāl- as the continuation.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt line 7390)\", \"stance\": \"supports\", \"note\": \"index line 'sikāl, sigāl: uskārtan'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, s.v. *kar, NWIr. section (p. 238)\", \"stance\": \"supports\", \"note\": \"'(+ *us-) NP sigālidan/sigāl- “to think, meditate (mischief)”' — the NP form, the pejorative nuance, and the us- preverb.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC p. 1155 s.v. skēl-\", \"stance\": \"partial\", \"note\": \"'Per. sikal “thought”; sikalidan, inf. “think”' — the Persian word is right but Mann attaches it to *skel-, which Cheung and Nyberg reject.\"}\n ]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sek- 'to cut, cut off, sever' (Pokorny 895-896), with the extended roots *sked-, *skei-, *(s)kel-, *(s)kep-, *(s)ker- that Nourai groups with it\",\n \"note\": \"The root is real, the language label ('Indo-European') and the gloss ('to cut, scrape, separate, tear') are both right: Watkins glosses sek- 'to cut' and closes the entry 'See also extended roots sked-, skei-, sker-1, sker-4. [Pok. 2. sék- 895, sken-(d)- 929.]', which is exactly the umbrella Nourai builds (his part-2 list Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2). One bookkeeping point: none of the five Pokorny pages he cites is sek- itself — IEW has sek- 'schneiden' at 895-896, while 920 falls in skei- (919), 926 in (s)kel-1 (923-927), 930/931 in (s)kep-1/(s)kep-2 (930-933) and 941 in (s)ker-4 (938-947). Those are the pages for the extensions, which is coherent with a chart devoted to them, but a reader looking for the root itself is sent to the wrong pages. Wiktionary's reconstruction page likewise keeps *skey- as an 'ey-present' of *sek- but does not present *(s)ker-/*(s)kel- as extensions of it, so the umbrella is AHD's framing rather than today's consensus. Page 439 is part 2 of the chart; part 1 is elsewhere in the book. Entry 1 on the page (ROOT Seks) is a redirect to Sweks and is not verified here.\",\n \"note_fa\": \"ریشه واقعی است و هم برچسبِ زبان («هندواروپایی») و هم معنی («بریدن، خراشیدن، جدا کردن، دریدن») درست‌اند: واتکینز sek- را «بریدن» معنی می‌کند و مدخل را چنین می‌بندد: «ریشه‌های گستردهٔ sked-، skei-، sker-1 و sker-4 را نیز ببینید. [پوکورنی ۲. sék- ص ۸۹۵]» — و همین همان چتری است که نورایی برپا کرده (فهرستِ بخشِ دومِ او: Sked 1، Sker 2، Skei، Skhed، Skep، Skel 2، Skaf، Ker 2). یک نکتهٔ فنی: هیچ‌یک از پنج صفحهٔ پوکورنی که او آورده به خودِ sek- مربوط نیست؛ sek- «schneiden» در ص ۸۹۵–۸۹۶ است، حال آنکه ۹۲۰ در skei- (۹۱۹)، ۹۲۶ در (s)kel-1 (۹۲۳–۹۲۷)، ۹۳۰ و ۹۳۱ در (s)kep- (۹۳۰–۹۳۳) و ۹۴۱ در (s)ker-4 (۹۳۸–۹۴۷) می‌افتد. این صفحه‌ها صفحه‌های همان گسترش‌هاست و با موضوعِ نمودار سازگار است، ولی خواننده‌ای که پیِ خودِ ریشه باشد به صفحهٔ نادرست فرستاده می‌شود. ویکی‌واژه نیز *skey- را «حالِ ey-دارِ» *sek- می‌شمارد اما *(s)ker- و *(s)kel- را گسترشِ آن نمی‌داند؛ پس این چتر، چارچوبِ AHD است نه اجماعِ امروز. مدخلِ دومِ این صفحه (Seks) تنها ارجاع به Sweks است و بررسی نشد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sek-: '... Latin sēcula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”) ... See also extended roots sked-, skei-, sker-1, sker-4. [Pok. 2. sék- 895, sken-(d)- 929.]'\"},\n   {\"ref\": \"POK:920\", \"status\": \"partial\", \"note\": \"IEW 919-921 is skei- 'to work with a sharp instrument (cut, separate)'; p. 920 falls inside it. Relevant to the ski branch, not to sek- proper.\"},\n   {\"ref\": \"POK:926\", \"status\": \"supports\", \"note\": \"IEW 926 (POK_03.txt line 2155, page header '926' at line 2151), inside (s)kel-1 'to cut' 923-927, root extension skel(e)-p-: 'av. hu-kǝrǝpta- ‚schöngeformt‘' — the page that carries node 1.\"},\n   {\"ref\": \"POK:930,931\", \"status\": \"supports\", \"note\": \"IEW 930 (s)kep-1 'to cover' and (s)kep-2 'schneiden, schaben, hacken' (930-933, POK_full.txt block ending 'Page(s): 930-933', material Latin scapus, scopae, OHG skaft, OE sceafan) — the source of English shape/shave/shaft in node 12.\"},\n   {\"ref\": \"POK:941\", \"status\": \"supports\", \"note\": \"IEW 938-947 (s)ker-4, (s)kerǝ-, (s)krē- 'to cut'; p. 941 falls inside it, and 945 (Section II, skerī-) is the sub-entry Watkins cites for krei- > Latin cribrum, i.e. node 8.\"},\n   {\"ref\": \"IEC:640\", \"status\": \"supports\", \"note\": \"Mann p. 640, Kr̥t- (2) 'cut, blow' with 'Per. cf. sile, sili, sīlī “slap, blow”' — node 3.\"},\n   {\"ref\": \"IEC:1155\", \"status\": \"supports\", \"note\": \"Mann p. 1155, 'skēl- ... “division, part; cut, separation; discernment” — Per. sikal “thought”; sikalidan “think”' — node 19.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 895-896 s.v. 2. sē̆k- 'schneiden'\", \"stance\": \"supports\", \"note\": \"the root itself, with Latin secāre, OCS sěkǫ, OE sagu 'saw'; this, not 920/926/930/931/941, is the page for sek-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 595 ff. s.v. (s)qel-, (s)qel(e)-p-\", \"stance\": \"supports\", \"note\": \"the pre-1959 form of the same material, including 'av. hu-kǝrǝpta- ‚schöngeformt‘ ... s. auch u. *qrep- ‚Leib‘' (Bd. II 595).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC pp. 1154-1156 (skeiiō, skel- (1), skēl-)\", \"stance\": \"supports\", \"note\": \"Mann keeps skei-, skel- and skēl- as separate but adjacent 'cut/divide' roots, the arrangement Nourai's part-2 chart mirrors.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms ch. 9 'cut'\", \"stance\": \"silent\", \"note\": \"Buck treats the semantic field but does not adjudicate the root groupings, so nothing to add for or against the umbrella.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 439,\n \"book_page\": 409,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-439.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok', len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-439.py"
}
```


### [2026-09-14T02:16:15.140Z] TOOL RESULT

```
ok 22
```


## [2026-09-14T02:16:19.009Z] TOOL CALL #100: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-439.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 439"
}
```


### [2026-09-14T02:16:20.266Z] TOOL RESULT

```
JSON OK
nodes verified: 22/22
node verdicts: {'transcription_suspect': 1, 'disputed': 2, 'plausible': 5, 'confirmed': 14}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'not_checked': 4, 'partial': 1}
books consulted: {'supports': 32, 'partial': 13, 'contradicts': 4, 'silent': 10} | by book: {'KLN': 9, 'POK': 7, 'MON': 4, 'WLD': 3, 'AHD': 3, 'PHD': 3, 'ARY': 3, 'SKT': 3, 'LAT': 3, 'CHEUNG': 3, 'NYB': 3, 'BRT': 2, 'HUB': 2, 'HRN': 2, 'IEC': 2, 'VOP': 1, 'LKT': 1, 'FVQ': 1, 'AFM': 1, 'BQT': 1, 'PLA': 1, 'DEV': 1}
```


## [2026-09-14T02:16:40.020Z] AGENT

Done — `data/verification/page-439.json` written, `verify_check.py 439` shows **0 PROBLEM lines** (22/22 nodes).

**Page 439 (book p. 409), root Sek part 2 — 1 entry, 22 nodes** (entry 1 "Seks" is a redirect, skipped)

Verdicts: root **confirmed**; nodes **14 confirmed, 5 plausible, 2 disputed, 1 transcription_suspect**.
Ref checks: 19 supports, 1 partial, 4 not_checked (VOP unobtainable; MON page numbers not mappable online).

Disputed / suspect items:
- **#2 Persian xŭk «خوک»** — *disputed*. Nourai (following Horn §510 and Mo'in's footnote in BQT p. 794, which I read from the scan) clips it from Av. hū-kǝhrpa- "boar-shaped". Modern view (Hübschmann p. 215, Wiktionary, Aryanpur): NP xūk < MP xūg (MacKenzie p. 94) < PIr. *huHka- < PIE *suH- "pig"; nothing of -kǝhrpa- survives, and the "pig" sense is in hū-, not kǝhrp-. Belongs under his own ☞Su 2.
- **#20 Old Iranian kar 3/us-kâr-a** — *disputed*. FFD:61 (Abolghasemi) supports the Iranian chain verbatim, but Cheung 2007 files MP uskar-/NP sigālīdan under *kar "to do, make" = PIE *kʷer- (LIV 391, Pok. 641), and Nyberg refers it to Av. 2kar-. The IE parent *skel- is Mann's (IEC:1155) alone.
- **#1 Avestan "xerpta"** — *transcription_suspect*, **error_in: book**. The printed page (checked, copied to `sources/refs/ocr/BOOK/439.png`) reads exactly as extracted, so the extraction is faithful; Avestan has no initial x- here — correct form kǝrǝpta- / hu-kǝhrp- (BRT col. 1830). The same line's "hu-kehrpta" prints the k correctly. The derivation edge itself is fine: POK:926 gives av. hu-kǝrǝpta- under skel(e)-p- with Pokorny's own caveat about kǝhrp- "Gestalt" (p. 620).

Plausible: #3 sīlī (only Mann IEC:640 has an etymology at all), #5 French ski + #16 French carnaval (real donors Norwegian / Italian, skipped), #9 Arabic ġarbala (AHD/Klein/Etymonline give Late Latin cribellum; Wiktionary + Lokotsch prefer Aramaic ʿarbālā), #19 IE Skěl (root real, but the "thought" gloss depends on the rejected sigāl derivation).

**No extraction errors found** — the JSON matches the printed page throughout, including refs and the Nezāmi quote.

Root-level bookkeeping note for the owner: none of Nourai's POK pages (920, 926, 930, 931, 941) is sek- itself — IEW has sek- at 895–896; those five are the pages of the extensions skei-/(s)kel-/(s)kep-/(s)ker-. Recorded in the entry `note`.

New saved artifacts: `sources/refs/ocr/BQT/794.vision.txt` (Mo'in's خوک footnote, read from the archive.org scan leaf 254), `sources/refs/ocr/BOOK/439.png`, and 13 archived web sources via `fetch_source.py`.
