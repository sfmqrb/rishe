# Verification process log — verify-page-205


## [2026-09-06T02:19:02.839Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 205 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-205.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-205.json. Write /home/sfmqrb/git/rishe/data/verification/page-205.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 205` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:19:40.175Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:19:41.058Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:19:41.075Z] TOOL RESULT

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
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T02:19:41.604Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-205.txt"
}
```


### [2026-09-06T02:19:41.668Z] TOOL RESULT

```
1	=== PDF page 205 (book page 175) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwei : to live  (refs POK:467)
4	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1288; POK:467,750; SNS:173; SOD:91 | jiva, jîta, jva : living ; merezu-jîta : short lived, short ; hu-jyâti : healthy, prosperous ☞Su 1
5	  #2 (parent #1) [Pahlavi] refs=BQT:606,1038 | zivastan : to live ; zivandak : mercury, "living (metal)"
6	    #3 (parent #2) [Persian] refs=MON | zîstan «زیستن» : to live ; zendegî «زندگی (زنده)» : life ; jîveh «ژیوه (جیوه)» : mercury | extra: زیست ، زی ، آبزی
7	    #4 (parent #2) [Arabic] refs=PLA:102 | zîbaq
8	      #5 (parent #4) [Persian] refs=MON:1768 | zîbaq «زیبق» : mercury
9	#6 (parent #0) [Avestan] refs=BQT:1872 | gayô-maretan : perishable life (man) ☞Mer 2
10	  #7 (parent #6) [Persian] refs=BQT:1872; ZMA:21 | Kîŭmars «کیومرث» : "mortal man"
11	#8 (parent #0) [Avestan / Old Persian] refs=POK:467 | gaĕtha : to exist ; gaĕtha-nâm : existing things ; gaitha : living property, cattle
12	  #9 (parent #8) [Pahlavi] refs=HRN:212 | gětîk, gětě : world ; gěhân : world
13	    #10 (parent #9) [Persian] refs=BQT:1868 | gîtî «گیتی» : world ; keyhân «کیهان (جهان)» : world
14	#11 (parent #0) [Avestan] refs=POK:468 | žîra, â-žîra : alert
15	  #12 (parent #11) [Persian] refs=FAF:28 | zîrak «زیرک» : alert, smart ; âžîr «آژیر (ژیر)» : alert, warning siren, smart
16	#13 (parent #0) [Latin] refs=AHD | viva, vivere : to live, life
17	  #14 (parent #13) [French] refs=None | vitamine
18	    #15 (parent #14) [Persian] refs=MON | vîtâmîn «ویتامین» : vitamin
19	  #16 (parent #13) [English] refs=None | vital, survive, vitamin
20	#17 (parent #0) [Greek] refs=AHD | bios : life ; mikro-bios : little creature ; hu-giĕs : good life, good health ☞Su 1
21	  #18 (parent #17) [French] refs=None | microbe
22	    #19 (parent #18) [Persian] refs=MON:4500 | mîkrob «میکرب» : microbe
23	  #20 (parent #17) [English] refs=None | microbe, biology, hygiene
24	#21 (parent #0) [Greek] refs=AHD; OEW:135 | zoe : life ; zoidion : carved animal figure
25	  #22 (parent #21) [English] refs=OEW:135 | zoo, zoology ; zodiac
26	#23 (parent #0) [Germanic] refs=AHD | kwi-kwaz : living, full of energy
27	  #24 (parent #23) [English] refs=None | quick
28	
```


## [2026-09-06T02:19:44.872Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-205.json",
 "description": "Read source JSON page 205"
}
```


### [2026-09-06T02:19:44.954Z] TOOL RESULT

```
{
  "pdf_page": 205,
  "book_page": 175,
  "entries": [
    {
      "root": {
        "name": "Gwei",
        "lang": "Indo-European",
        "refs": "POK:467",
        "gloss": "to live"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:1288; POK:467,750; SNS:173; SOD:91",
          "words": [
            {"translit": "jiva, jîta, jva", "gloss": "living", "script": null},
            {"translit": "merezu-jîta", "gloss": "short lived, short", "script": null},
            {"translit": "hu-jyâti", "gloss": "healthy, prosperous", "script": null, "see": ["Su 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:606,1038",
          "words": [
            {"translit": "zivastan", "gloss": "to live", "script": null},
            {"translit": "zivandak", "gloss": "mercury, \"living (metal)\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "zîstan", "gloss": "to live", "script": "زیستن"},
            {"translit": "zendegî", "gloss": "life", "script": "زندگی (زنده)"},
            {"translit": "jîveh", "gloss": "mercury", "script": "ژیوه (جیوه)"}
          ],
          "script_extra": "زیست ، زی ، آبزی",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:102",
          "words": [
            {"translit": "zîbaq", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1768",
          "words": [
            {"translit": "zîbaq", "gloss": "mercury", "script": "زیبق"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:1872",
          "words": [
            {"translit": "gayô-maretan", "gloss": "perishable life (man)", "script": null, "see": ["Mer 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1872; ZMA:21",
          "words": [
            {"translit": "Kîŭmars", "gloss": "\"mortal man\"", "script": "کیومرث"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:467",
          "words": [
            {"translit": "gaĕtha", "gloss": "to exist", "script": null},
            {"translit": "gaĕtha-nâm", "gloss": "existing things", "script": null},
            {"translit": "gaitha", "gloss": "living property, cattle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "HRN:212",
          "words": [
            {"translit": "gětîk, gětě", "gloss": "world", "script": null},
            {"translit": "gěhân", "gloss": "world", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:1868",
          "words": [
            {"translit": "gîtî", "gloss": "world", "script": "گیتی"},
            {"translit": "keyhân", "gloss": "world", "script": "کیهان (جهان)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:468",
          "words": [
            {"translit": "žîra, â-žîra", "gloss": "alert", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "FAF:28",
          "words": [
            {"translit": "zîrak", "gloss": "alert, smart", "script": "زیرک"},
            {"translit": "âžîr", "gloss": "alert, warning siren, smart", "script": "آژیر (ژیر)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سپه را بیارای و آژیر باش - شب و روز با ترکش و تیر باش",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "viva, vivere", "gloss": "to live, life", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "vitamine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "vîtâmîn", "gloss": "vitamin", "script": "ویتامین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "vital, survive, vitamin", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "bios", "gloss": "life", "script": null},
            {"translit": "mikro-bios", "gloss": "little creature", "script": null},
            {"translit": "hu-giĕs", "gloss": "good life, good health", "script": null, "see": ["Su 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "microbe", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Persian",
          "refs": "MON:4500",
          "words": [
            {"translit": "mîkrob", "gloss": "microbe", "script": "میکرب"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "microbe, biology, hygiene", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; OEW:135",
          "words": [
            {"translit": "zoe", "gloss": "life", "script": null},
            {"translit": "zoidion", "gloss": "carved animal figure", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "English",
          "refs": "OEW:135",
          "words": [
            {"translit": "zoo, zoology", "gloss": null, "script": null},
            {"translit": "zodiac", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 23,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kwi-kwaz", "gloss": "living, full of energy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 24,
          "parent": 23,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "quick", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T02:19:45.544Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:19:45.580Z] TOOL RESULT

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


## [2026-09-06T02:19:50.943Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','HRN','PLA','SNS','SOD','ZMA','FAF','OEW','AHD','PHD','BRT','WLD','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T02:19:51.843Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -c 3000 data/verification/page-124.json",
 "description": "List verification dir and sample file"
}
```


### [2026-09-06T02:19:52.574Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}

FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


### [2026-09-06T02:19:52.620Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
---
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را ا
```


## [2026-09-06T02:19:55.905Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T02:19:55.951Z] TOOL RESULT

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


## [2026-09-06T02:19:57.904Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-127.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'}, ensure_ascii=False, indent=1)[:2500])\nprint('=== node ===')\nprint(json.dumps(e['nodes'][1], ensure_ascii=False, indent=1)[:2500])\n\"",
 "description": "Inspect page-127 structure"
}
```


### [2026-09-06T02:19:59.501Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "
=== node ===
{
 "id": 2,
 "lang": "Persian",
 "words": "dam «دَم»; damîdan «دمیدن»; damâ «دما»; Damâvand «دماوند»",
 "verdict": "disputed",
 "derivation": "Three of the four words are right, the fourth is not, so the node takes the worst verdict. (1) دم dam 'breath' < Middle Persian dam (Manichaean/Book Pahlavi dm-, /dam-/) < Proto-Iranian *damH- < PIE *dʰemH-; MacKenzie's Concise Pahlavi Dictionary has 'daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. ~išn: breath', and 'damidan [dmytn'] = daftan'. This is a different word from the homophone دم 'tail' (< dunb, Av. duma-), which Horn keeps apart as his no. 573. (2) دمیدن damīdan 'to blow, breathe' is the New Persian regularisation of MP daftan (past stem daft) on the present stem dam-: the inherited -ft- past was replaced by the productive -īd- suffix, exactly as MacKenzie's 'damidan = daftan' records; hence Horn no. 572 'dem \"Atem, Atemzug\", deme, demīden \"wehen, blasen\"'. (3) دما damā is a nominal derivative of dam with the abstract/nomen suffix -ā; Borhan-e Qāteʿ p.877 glosses it 'بمعنی دم و نفس باشد' with Moʿin's footnote '۱ رك: دم' ('see dam'), i.e. 'breath'. Nourai's gloss 'weather, heat' is the modern technical sense ('temperature', as in دماسنج 'thermometer'), which Aryanpur records explicitly; that sense is 20th-century, not classical, so the word is right but the gloss is anachronistic. (4) دماوند Damāvand does NOT belong here. In Islamic sources the name is written دنباوند dunbāvand, and Moʿin's own footnote on the page Nourai cites (BQT:878) reports Kasravi's derivation from دُما/دنب 'back, behind' + the suffix -vand (paired with نهاوند Nahāvand from نها 'front'); Wiktionary likewise gives 'from Middle Persian dmbʾwnd (dumbāwand)'. The 'mountain of vapour' reading is a folk etymology built on the homophony of dam 'breath/vapour' with dam < dunb 'tail, rear'. Nourai's own NOTE flags the conflict; modern scholarship sides with BQT:878 against the chart.",
 "derivation_fa": "از چهار واژهٔ این گره سه تا درست است و یکی نادرست، پس حکمِ گره همان بدترین حکم می‌شود. ۱) «دَم» به معنی نفس از فارسی میانهٔ dam (پهلویِ کتابی dm-)، از ایرانی باستان *damH-، از هندواروپایی آغازین *dʰemH- است؛ مکنزی در فرهنگ کوچک پهلوی می‌آورد: «daftan, dam- … breathe, blow؛ damišn نفس». این «دم» با «دمِ» هم‌آوایِ به معنی دنباله (از dunb، اوستایی duma-) یکی نیست و هرن هم آن دو را در شمارهٔ ۵۷۲ و ۵۷۳ جدا کرده است. ۲) «دمیدن» صورتِ قاعده‌مندشدهٔ فارسی نو از مصدرِ پهلویِ daftan است: ستاکِ حالِ dam- را گرفته و پسوندِ زایای -ید- ر
```


## [2026-09-06T02:20:49.004Z] AGENT

Now let me research. Starting with Pokorny for the root.


## [2026-09-06T02:20:52.005Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gᵘ̯ei-\\|gvei-\\|g^uei-\\|leben\" POK_01.txt | sed -n 1,40p\necho \"=== search gʷei ===\"\ngrep -n \"gu̯ei\" POK_01.txt | head -30",
 "description": "Grep Pokorny for gwei- root"
}
```


### [2026-09-06T02:20:52.072Z] TOOL RESULT

```
85:Ai.  ajriya-  .in  der  Ebene  befindlich'  =  gr.  äygiog  .auf  dem  Felde,  im Freien  wachsend  oder  lebend,  wild';  dygövsgog  .wild  lebend',  lat.  agrestis .ländlich,  bäurisch,  derb'.  (Über  got.  akran,  dt.  Eckern  s.  aber  unter  *ög- . wachsen'.)
255:av.  äyü  n.  , Lebensdauer^,  Gen.  yaos,  Dat.  yavöl,  Instr.  yavä,  davon yavaetät-  ,Dauer^,  yavaejl-  ,immer  lebend-;   yus  m.  ,Lebensdauer^;
256:Gr.  s-St. ;  kypr.  vSatg  t^av  (=  diä  ßlov);  suffixloser  Lok.  lakon.  aisg ,immer^;  hom.  alsl,  att.  dsi  (^^aLj^eOi),  Akk.  aatt.  auo  (*aLJ^oaa);  Dat.-Lok. ohne  Erweiterung  in  ion.  aa,  lesb.  ^l  {*aiJ^i)  (danach  dtdiog  ^ewig^,  drjv- aiog  ,langlebend^);  n-St.:  ald}v  m.  (und  f.  nach  aiü)g)  ,Lebenskraft,  Lebens- dauer"^, alsv  ,immer^;
964:Arm.  aganim  ,übernachte';  vair-ag  ,au£  dem  Lande  lebend',  aut'  ,Über- nachten,  Nachtruhe,  Station^
1366:men^  (und  .in  Saus  und  Braus   leben^;   vgl.  oben  mlid.  hüsen  ^schwelgen'), büsterlg  ^stürmisch^  aksl.  bysti-o  ^verschlagen^,  russ.  bijstryj  ^schnell;  scharf, sichtig;  reißend  von  der  Strömung*   {*bhüs-ro-). WP.  II  114  f.,  Trautmann  28,  39.
1372:Vgl.   mit   z.  T.    ähnlicher    Bed.    hhltd-    , aufsprudeln,    schwatzen',    bhel- , schallen'    und   bal-,  bal-bal-  unter  baba-   (z.  B.  lit.  blebenti   mit  dem  nhd.^ plappern  ähnlicher  Bildung).
=== search gʷei ===
```


## [2026-09-06T02:20:53.728Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jīti\\|ǰīti\\|hujyāiti\\|hu-jyāiti\\|mərəzu\\|merezu\" BRT.txt | head -30\necho \"=== žīra ===\"\ngrep -n \"žīra\\|zīra\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T02:20:53.813Z] TOOL RESULT

```
=== žīra ===
```


## [2026-09-06T02:20:59.512Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"467\" POK_full.txt | head -20\necho \"=== try lemma search ===\"\ngrep -n -i \"Page(s): 46[7-9]\" POK_full.txt | head",
 "description": "Search POK_full for page 467"
}
```


### [2026-09-06T02:20:59.594Z] TOOL RESULT

```
3990:(Germanic *alb-it-, -ut-) "swan', (forms -d- in animal names: s. Brugmann Grdr. I|2 1, 467, 
8839:References: WP. I 849 f., WH. I 467, Feist 113 f., Sievers-Brunner 121, 243, Wackernagel- 
33278:References: WP. I 564, WH. I 467 f., 538. 
38558:Page(s): 466-467 
38590:Page(s): 467 
38604:Page(s): 467 
39074:Page(s): 467-469 
44491:dark, gloomy, misty ', caditi^ become sooty ' (etc., s. Berneker 133, 467), perhaps Old 
48072:Brugmann l|2 1, 467), sapati^ curses ", -/e" declares, promises ". 
52071:References: WP. I 467. 
52336:References: WP. I 467. Different Specht Indog. Dekl. 252 f. 
72765:References: WP. II 467 f., WH. II 478, 504; 
85103:Latin taxus^ yew' (Benveniste Mel. Boisacq 1, 37 ff., Mayrhofer 1, 467 f.); 
92640:about Hittite hamesh{a)-, hameshant-^ spring ' s. A. Goetze Lg. 27, 471, 51, 467 ff., F. 
=== try lemma search ===
38571:Page(s): 469 
38590:Page(s): 467 
38604:Page(s): 467 
38675:Page(s): 469-470 
39074:Page(s): 467-469 
39836:Page(s): 469
```


## [2026-09-06T02:21:00.576Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f: $(grep -c $'\\f' $f) pages\"; done",
 "description": "Count POK pages"
}
```


### [2026-09-06T02:21:02.204Z] TOOL RESULT

```
POK_01.txt: 352 pages
POK_02.txt: 420 pages
POK_03.txt: 415 pages
```


## [2026-09-06T02:21:04.437Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '39020,39090p' POK_full.txt",
 "description": "Print POK_full lemma at 467-469"
}
```


### [2026-09-06T02:21:04.491Z] TOOL RESULT

```
Sardinian Logudoresu 



vida 



Sicilian 



vita 



Triestino 



vita 



Umbro-Sabino 



vita 



Wallon 



veye 



2. with ApiOTH, masc. pioTO(;; 'life, means of living, substance, the world, mankind, etc.'; 
Note: common lllyrian g"- > b-. 



with or. Lithuanian gaivus^a\er{, awal<e, smart, living '; 

verbal derivative: Old Indie y7i/a//i Avestan Jva/'t/ {\.e. jTva/t/) "lives', ap.y/Va" live!' = Latin 
v/vo, Old Church Slavic z/vg' live ' (Inf. z/t/see above), extended Lithuanian gyvenu' live 
'; Old Indie y»7i/a/A pra-jinosi^ be alive, get excited; stimulate, animate, refresh '. 

References: WP. I 668 ff., Meillet Introduction^ 165, Specht KZ. 62, 11 1, Schwyzer Gr. Gr. 
I 298, 300, 330, 5014, 6756, Trautmann 75 f. 
Page(s): 467-469 

Root / lemma: g^eb^- 

Meaning: womb; young of animal 

Material: Old Indie garbha-h, Avestan garawa- "womb, foetus', garabusu. " the young of 

an animal '; Old Indie sa-garbhya-h^ son of the same mother, brother and sister ' (= gr. 

a5£A(p£6(; ds.); 

gr. SsAcpuq, -uoc; f., Doric SsAcpua " womb, uterus' (see below); *5£A(poc; n. ds. as base 
from aSsAcpsoc; (Hom.) "couterinus, brother ' (*a-5£A(p£[a]-6^), next to which Attic a5£A(p6(; 
ds.; SsAcpa^ m. f. "piglet', 5£A(pi(;, hvo(; m. "dolphin', 5oAcp6(; n MHTpa Hes.; Specht (Indo 
Germanic Dekl. 268) reconstructs from gr. a5£Ai(p-r|p a5£A(p6q. AaKU)V£c; (Hes.) an 
originally root *g"el-\
```


## [2026-09-06T02:21:07.898Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=38700 && NR<=38790' POK_full.txt | grep -n \"Root / lemma\\|Meaning\" \necho \"---\"\ngrep -n \"Root / lemma\" POK_full.txt | awk -F: '$1>38600 && $1<39080'",
 "description": "Find lemma head for 467-469"
}
```


### [2026-09-06T02:21:09.755Z] TOOL RESULT

```
85:Root / lemma: aiu-, aju-\ 'vital energy, vitality' derived from reduced Root/ lemma: g^ei-S 
---
38606:Root / lemma: g'^eja- 
38677:Root / lemma: 5'"&/-5and g^eia-: g^fijie-: g^Olio-: gl"-, frequent, often with -:/- extended 
38784:Root / lemma: aiu-, aju-\ 'vital energy, vitality' derived from reduced Root/ lemma: g^ei-S 
39076:Root / lemma: g^eb^-
```


## [2026-09-06T02:21:12.269Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '38600,38700p' POK_full.txt",
 "description": "Print POK lemma gwei"
}
```


### [2026-09-06T02:21:12.327Z] TOOL RESULT

```
Old Norse kve\. " pen, fold, narrow enclosed passage ', kvJa^ coop, place in a pen or 
coop, pen '. 

References: WP. I 666. 
Page(s): 467 

Root / lemma: g'^eja- 

Meaning: to prevail, be mighty 

Material: Old Indie y>a,y/y^f. " suzerainty, sovereignty, political control ' (= gr. pia) = alb. f. 

{*g"eia) zija^ mourning, grieving, lamentation; act of feeling sorrow for someone's death; 

period of mourning; clothes worn by mourners; signs of mourning '. 

Old \r\d\c Jyana-m, JyanF-h ^ oppression, depression, exploitation, suppression \Jyayan' 

mightier, more prepotent \ jyestha-, Jyestha- " most incredible, strongest '■,Jayat/ {Peri. 

jigaya) " overmatched, overpowered, defeated ' (Avestan \v\t Jayai, full grade I the root, 'to 

defeat, conquer'), yay/s/7^- ' victorious \jetar- " defeating '; jinati {Vut jyasyati. Pass, jTy ate, 

participle y/7a-) ' beaten, overpowered, oppressed'; y/^/sa//" will defeat, conquer ' ( : Avestan 

Jijisaiti^ tries to attain for himself, cause to be found '), jigy'u- " victorious '; 

Old Indie y»7a// stands also for " bring about sth ', jyani-h a\so " decrease, loss' and is so 
both the extender of the palatal aniaut. root from Avestan zinat^ damages ', Old pers. 
adinat^buuQ about, take away, take off, remove ', participle Perf. Pass. dTta-, Avestan 
zyana, zyani-i. " damage, harm ', Inf. zyana/^to harm', Baluchi zinay^ seize, take forcibly; 
grasp, snatch, take abruptly, seize hastily, take away by force ' (external Aryan 
correspondences not known); 

Maybe alb. Geg mezane^ to gripe, capture ', Geg me uzane, Tosc zihem^ quarrel '. 



gr. pia " force, might, power ' Note: common lllyrian g"- > b-. (= Old Indie y/ya), piaco, 
pia^u) " force, coerce ', piaiO(; ' violent, brutal ', AvTi5iO(; probably = AvTipiO(;; pTvsTv ' futuerl 
', ^a£i pivsT Hes. " rape ' (whereas pTvsTv would have derived from a participle *pT-v6-(; = Old 
lndicy/-/7a-, Gramm.,); after Liden IF. 19, 328 with npers. gayad^ futuit ', Inf. gadan, gan, 
from a root *g"'ai- or (?) *g"'di-, which would be compatible only with the latter beginning 
with g^ei-as lengthened grade of the ogradation at most theoretically; 

Maybe alb. {*zyana) dhune^ force, violence, forcing, viciousness, rape ' : Old pers. adinat 
'bring about, take away, take off, remove ', participle Perf. Pass. 07?^-. 

with g'^eja-^ suppress, crush; repress ' appear also the following words for " exhaust, 
weaken, make feeble ', Intr. Pass. " go altogether, grow old, dwindle ' originally belonged 
together: 

Old Indie y//7a// also ' grows old \ jyan'hh^ senility ', ajyani-h^ immortality ',jTna-'age6, 
old', a-j7ta-' unbroken, unmarred, unscathed, undamaged ', a-jTti-h^ intactness, 
completeness, entireness, wholeness ',y/V/7-'old, fragile, easily broken; unstable, 
dilapidated, helpless ', Avestan yya-, present J/'na/t/" exhausts, weakens ', ajyamna-' not 
decreasing, inexhaustible ', wherefore Middle High German verquTnen, preterit quein^ 
dwindle away, decrease ', Old English cwTnan, a-cwTnan, preterit cwan' dwindle away, 
decrease, abate, pain, feel ill ', extended Old English cwincan, acwincan^ disappear, 
abate ' (Kaus. with ablaut neologism acwencan, engl. quench^ extinguish, put out '), and 
with /77-forms wfal. kwTmen^ pain, feel ill ', kwTmelig' softened, made soft; overindulged '. 

From Germanic seem in both meaning of colouring addable: 

Old Norse kveita^ dazzle, blind with bright light ' (o'-present); s-extensions Middle Low 
German quisten^ let perish, waste ', (7^/s/ "damage, loss', mnl. quisten^ rub, rub away, 
wear away, bruise, grind, bray triturate, rub against, wear', Gothic q/stjan ^spoW, Old High 
German quisti. " annihilation ', archwistan, f/rqu/stan 'spoW, destroy'. Old English cmesan' 
crush, squeeze hard, squash ', jut. /riws 'press, extract, squeeze ', nisi, kveisa^ stomach 
ache '; Norwegian kveisa^ verkummertes Geschopf ', kvisla^ dwindle away, decrease '; g- 
extension (fragmented reduplication?) Frisian kwTke, kwikken^ pinch, tweak, nip ', in the 
reduced meaning in Prussian queicheln^ fondle '. 

References: WP. I 666 ff., Schwyzer Gr. Gr. I 300, 694. 
Page(s): 469-470 

Root / lemma: 5'"&/-5and g^eia-: g^fijie-: g^Olio-: gl"-, frequent, often with -:/- extended 



Meaning: to live 
Material: A. from *g''eid: 

Old Indie y7i/a/i/-/7 "life' (see below), gaya-h^ house, courtyard, Hauswesen ' (see below); 

AvestanJ/'yaesa' you should live ' (2. Sg. present Med., orthemat. 2. Sg. Opt. for 
y/gayaesa); Jljf/sdnt/ {ong\na\\Y subjunctive) " be refreshed, nourished \Jaya- m. " incitation 
'; gaydxr\. 'life, lifetime, lifestyle ' (= Old Indie gaya-h^ house and courtyard, Hausweser^ ' = 
russ. ^oy "peace; salvation!'); Avestan gaeda. Old pers. ^a/z?a "entity, house and courtyard 



Armenian keam^ live ' {*gl'ya-ye-mi); Meillet Esquisse 110, 176. 

gr. hom. psoijai " I will live ' {*^z\zao\\a\\ SchwyzerGr. Gr. I 780, 788''); Note: common 
I Nyhan g"'- > b-. 

Lithuanian gajus' slightly healing '; Lithuanian gyju, gyti{*gTti-) " revive, recover, 
become healthy ' (in addition i-gyti-^ attain ', actually " live there '), Latvian dz?t^ heal; 
become healthy ', gydau^heaX, Latvian dziedet^\\ea\, cure' (MiJhlenbach-Endzelin I 559),
```


## [2026-09-06T02:21:18.975Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '38700,38790p' POK_full.txt",
 "description": "Print rest of POK gwei lemma"
}
```


### [2026-09-06T02:21:19.029Z] TOOL RESULT

```
become healthy ', gydau^heaX, Latvian dziedet^\\ea\, cure' (MiJhlenbach-Endzelin I 559), 
Old Church Slavic z///" live ' (present zivgsee below); in addition Old Church Slavic zitb 
"life' ( *gft/s), pa-zitb " pasturage, food, fodder, provender, esp. for cattle, grass, generally, 
any feeding-ground, any moist, grassy place, meadow '; 

Slavic *gojb " life' {*g"'q/o-s) in Old Russian ^oy"peace', old Serbo-Croatian goj ds., Old 
Czech /7oy "fullness, wealth' (: Old \nd\c gaya-h), causative Slavic *gq/7t/' make live ', 
Serbo-Croatian gdj/'t/^ care, fatten, overfeed ', etc.; 

Tocharian B sa/- " live ', Van Windekens Lexique 127. 

'^'^o-in: 

Avestan -Jyaiti- f. (in compounds) 'Wie' , Jyatus Gen., Jyatum Akk. "life' (in Old Indie if this 
became *Jya-tu-h aftery7i/5//to jTvatu-h)\ 

ep. Ionian ^cbw, gort Scbu) " live ' (from *^(ji)-i(ji), Indo Germanic *gzid-id), Aor. Epiwv 
( "(g^/io-zT? with vokal. /; which was presumably supported by piow), Attic ^w, ^pq, ^p (*^n,'£'. 
Indo Germanic *gZie-), ^w6q " living ', ^cbn "life', ^coov "animal'; gr. uyinc; "fit, healthy' {*su- 
g"lies " living well '); 



■^"/^ (except in baltosl. *gTti-, see above) in Avestan yavae-jT-^ perpetually living ', 
Avestan jTti- f. "life', Old Indie y/?5- 'agile, lively, rash, hasty', Avestan jTra- " brisk of mind, 
smart'; Old Prussian ^e//s 'bread'. Old Church Slavic zito^ corn, grain '. 

Maybe alb. Geg 5/a 'thing, property' : Old pers. ^5/z?a 'entity, house and courtyard '; 

With Indo Germanic ^^suffix {g'fg-): Old High German queh and quek. Gen. queckes^ 
living ', Modern High German keck, Swiss c/7ec/r 'strong, tight, firm' (A/rfrom a form with kw 
as Middle High German quicken' refresh '), Old English cwicu, cucu' living ', Old Norse 
kvikr, kykr{f\Vk. kykkvan) ' living ', also Modern High German Quecke, Old English cwice' 
orchard grass, cocksfoot grass, cock's foot' (from the extraordinary vitality and germ 
strength of the plant); 

Latvian o'z/^a'life' (as dzTveds.), dzfguoV live ' (as dzfvuotds). 

Latin i/Zge/'e'be lively ' separate from vegere' move, excite, quicken, arouse, be lively, 
active ' to, seems unjustified. Wood KZ. 45, 68 puts in a line an nord. kvikr eic. also plenty 
Germanic words for lively movement of all kind, thus except Old Norse kveikja ' animate, 
kindle, inflame', with other further formation Old English cwiferiTce Mn . 'keen, eager', engl. 
^^/VeA'agile, lively, nimble', Frisian kwistern' wave, wag (tail, etc.), sashay ', kwispein^ 
^u^^^^^|ruhig hii^^U^J^^^^ ', Swedish dial. /ri//7y' throw', jut. kwTdar' 3\qx\., 
awake, smart'. 

B. from *gZiou-, g'^u-: 

with f. Old Indie y/Va-' living, m. life'. Old pers.y/Va- Avestan yVa- (i.e.y/Va-) ' living ' = 
Latin vTvusds., Oscan bivusP\. ' ™', cymr. biw, corn, biw' horned cattle ' ('*living cattle 
'), Lithuanian gyvas, Latvian dzTvs, Old Church Slavic z/Vb ' living '; 



with Agr. ^\oc, 'life' {*g"'i-y-os), Gothic qius' living ' {gaqiunan' ovo^iv '), air, biu, beo, 
cymr. byw, bret. beo, corn, byw, bew' living ' (therefrom Celtic *bivo-tut-s\v\ Old Irish 
betiiu. Gen. betiiad= cymr. bywyd'Wie'); 

■^■^in Celtic *bitu-. Old Irish bifii {Gen. betiid), cymr. byd, bret. it'eo'' world'; 

Maybe alb. {*g"(ilid-te) bote'\Nor\6' : pioTOi;; 'life, means of living, substance, the world, 
mankind, etc' common Celtic - lllyrian gr. g"'- . b-. 



gall. Bitu-nges, i.e. ' Leute des Weltkonigs ' (compare the similar meaning from Avestan 
gae&3); besides zero grades Indo Germanic *g"eito-\n cymr. bwyd'e^X, acorn. buiV^\s\\, 



food', abret. boitolion' esciTens ', nbret. /7C»eo'"nourishment, food'; the disyllabic Old Irish 
biad. Gen. /?//o'" nourishment, dish, food' (previous *biveto-m). 

with /r-suffix: Latin vTvax^ tenacious of life, long-lived, vivacious, lively, vigorous ', similar 
formation with Lithuanian gyvokas' living ', distant Old Indie y7i/5/ra-ds.; 

with /-suffix: 1. with /"Old lndicy/V//a-/77" life, living being etc.', Lithuanian gyvata'W^e, 
livelihood, farm ' = Latin vfta 'life' ( *g"'Tuota) and Old Church Slavic zivoti^ m. 'life'. Old Indie 
JTvatha-h\ common Latin g"- > gv- > v-. 

Maybe alb.yie/a: Bolognese vetta: Bresciano eta: Latin K/Tg'life'. 

Note: 

Root / lemma: aiu-, aju-\ 'vital energy, vitality' derived from reduced Root/ lemma: g^ei-S 

and g^ejQ-: g^OJie-: g^OJio-: g'f-, frequent, often with -f/- extended: to live 



English
```


## [2026-09-06T02:21:30.226Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== hujyaiti ===\"; grep -n \"hujyäiti\\|hujyaiti\\|hu-jyäiti\\|jyäiti\" BRT.txt | head -10\necho \"=== gayo.maretan ===\"; grep -n \"gayö\\.maratan\\|gaya.maratan\\|gayo-maratan\\|maratan\" BRT.txt | head -10\necho \"=== gaetha ===\"; grep -n \"gaeda\\|gaeða\\|gaeQa\" BRT.txt | head -5\necho \"=== jira ===\"; grep -n \"jira\\|jîra\\|zira\" BRT.txt | head -10",
 "description": "Grep Bartholomae variants"
}
```


### [2026-09-06T02:21:30.344Z] TOOL RESULT

```
=== hujyaiti ===
20530:—  'r^m  .  .  haianragaoiim  .  .  bafvar».- iaimafum  ..  ai^afmm  jayaurvanhtm  Vt 70.  7;  —  °r?m  .  .  yahtnäi  mal'äia/um  frä- '^winsat . .  akurö  mazda  . .  karai^yö  paiti barfzaya  Yt  70.50;  —  surunuyä  nä  °ra yamahe  Yt  70.  32 ;  3» ;  —  usta  akmäi  ,  . yakmäi . .  zaota  asava  , ,  'rahe  vaca  yazäite rästun  ahmai  . .  °rB  ma2%anpm  Jcaraiti Yt  70. 137 ;  — yahmai .,*rB jasaiti  avaiiihe yö  baevariJpasanB  vIspB.vtövä  aiaoyamnB Yt  10.24;  —  '"'"  --yS  ■•  aivjyäiti  pasca ha  fräsm5.daitJm  . .  visptm  imat  adkäiti yal  atUan  zqm  asmattfmca  vatnm  zaslaya
=== gayo.maretan ===
=== gaetha ===
=== jira ===
3234:•  j.  adaoyöjiratav-  Adj.  'des  Verstand untrüglich  ist':  maoyö  aki  •tus  . .  vispö.- vinvh  Vt.  i2.i'K
12617:mainyJtd  'ttm  mafyäi^ia  faiti  nSüÜ^m  V. z.  39.  a)  von  sichtbaren  körperlichen Mängeln  und  Leiden:  anäisca  kannis^a ..ava  -/«(IS.)  daxstavatUa  yä  rßit  peuru.- jira  (sd.)  fradaxita  Yt  5.  93;  —  ma  a%ra fi-akavö  mä  apakavS  .  .  tnüta,iSm  anyqm •tanqm  (Gen,  part  als  Subj.)  yBt  hmti anrahe  mainySus  daxStim  (s.  o.)  V.  2.  29;
12623:•  j.  daxsta'vant-  Adj.  (fem.  'vaitf-)  'Merk- male, Zeichen  (körperlichen  Gebrechens) an  sich  tragend':  ava  daxsta  'vaniaCSP.) yä  tidil  pouru.jira  (sd.)  fradaxsta  Vt.  j. 93.  a)  nur  fem.  'mit  der  Regel  be- haftet, menstruirend''';  yai  ahmi  nmane .. tairika  •vaiH  anhat  V.  5. 59;  16.1;  — yB  nairikqm  cihravaillm  'Z'aitTm  voiuna- vaitlm  ,  .  xSudrh  avi  frattlutr^zaiti  V.  18. 67;  15.7;  —  näirikaya  ..  'vaityä  V.  16. 5.  «3.   »4-
13318:uzw.  I)  'worauf  einer  Recht  und  Anspruch hat,  gebühreod,  gehörig':  dahmS  ttiuruzäd {sd-)a(iilifyifjiracnS  'tyehe  draouanAö  "upa.- jananha  (sd.)  N.  17;  —  ySi  .  .  öhäityB.- draonarthasca  *h^n^  'lim  gSus  draonö upaStimttS  .  .  avarthabdanti  (sd.)  N.  52; $$.  n)  'dem  Gesetz  entsprechend': i)  subjektiv  'gesetzestreu,  dem  Gesetz  ge- horsam': aom  nanm  'tlm  yS  na  masi/tim yaswm  yaiaite  . .  YL/.  24;  —  ya^a  nä 'tyS  *däityäi  (s.  A)  *bairyetica  *^airyetica V.5.40.  2)  objektiv  'wie  es  vom  Gesetz bestimmt  ist,  gesetzlich,  vorschriftsmässig': vispaKa  . ,  'tya  (APd.)  ra^wya  frärai^ya (sd.)  aSahe  däiäts  F.4^;  —  i^tye  navatti astanam  (sd.)  ahäityö.aaAan%ranam  °tltn . .  Aankrftn  kirwnuyat  V.  i4~  17;  —  däyata "tya  (ISf.)  pairisti  (sdT)  V.  5. 2  PüZ.;  4  PüZ., *N.  JOJ;  —  'tlm  yasramca  vahmsmh  Yt  8. 56;  —  'tyqm  ävistJm  rd^ivyqm  ilvisilm Vr. //.  19;  —  'tyanqm  rd^wyanqm  hvar- ilanqm  syao^nanqm  vansäi  Vr.  i$.\;  — aesS  (Sp.  33  u.)  il  asti  °iyS  kata  ..  irisiahe V.  3.  II;  —  "tyS  *ainyS  havand  (sd.)  *'tyV'' *ainyS  ya%a  *va  °tyS  (NDm.)  kita  N. 107,  a)  von  giitav-  xa.   (Sp.  518  m,):
13533:•  j.  daratam  Absol.'>,  mit  <m//  'er  hält] sich  auf,  verweilt':  t3tn(s^)ai  uzira  yezi ahi  garö  d'  "wenn  du  dich  auf  dem  Berg aufhältst"  V.  2i.  5.
17608:•  j.  'fra-daxSta-  Adj.  'mit  einem  Zeichen versehen,  gezeichnet":  ava  daxsta  äaxsta- vanta  yä  nsit  pouru.jira  (sd)  °ta  (NPm.)
17654:•  j.  fra-pad-  :fra-bd-  m.  'Vorderteil  des menschlichen  Fusses,  Vorderfiiss',  vom Knöchel  bis  zu  den  Zehenspitzen:  dasiram {hdyum)  'hdtm  V.  8.  67,  68',  69,  <J.  24*;  — yat  nä  paurva  °bda  (AD.)  /rabdöjirajB frama&aiü  "wenn  Jemand  über  die  Spitzen der  Vorderfüsse  um  eines  Vorderfiisses Länge  hinauspisst"  V.  /<?.  40*';  —   °bda
19058:—  yii  n'  vistim  (sd.)  druats  N.  $4;  — daxita  .  .  ya  n-  pouru.jira  fradaxita  Yt 5-93;  —  ye^i  apsis{%A.)  (yai)  äat  n' apsil  N.  2Ö;  —  die  Verbalfonn  des  vor- hergehenden positiven  Satzes  ist  zu  er- gänzen: ya  paiti  ape  baraiti  n"  bansmaine N.&p;  6g-,  —  yS  gSui  uruäiwar}  kqm,- pa/räiti  (sd.)  .  .  yö  n'  iisa  V.  4.  48;'  — yat  dim  vaatat*rvistalha{%&.)  *vinääram n"  avaya  *vistaBiVa  N.16.        zu  la):  y^..
```


## [2026-09-06T02:22:01.043Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gaya-\\|gay a-\\|'Leben'\" BRT.txt | head -20\necho \"=== ===\"\ngrep -n \"Quecksilber\" BRT.txt PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt HUB.txt 2>/dev/null | head -20",
 "description": "Grep for gaya and Quecksilber"
}
```


### [2026-09-06T02:22:01.126Z] TOOL RESULT

```
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. anys.anyaeibyö}  ya^a  'gatm  iu^a  (sd.) '  und  Inf.:  naj/a  .  .  Aäu  ni  ahmat  haca •gsimi  ,  .  "Wie  weit  von  einander?  "SiQ  gstaot  isalta  frasBtÖit  »eil  apasüföil  (sd.) viel  als  eine  Schrittlänge  beträgt  .  ."  "^  .{'^rayamcina  gämanam  P.  2jj>.  3)  '(es) p.  S.                                                                     I  können,  vermögen,  (dazu)  im  Stand  sein',
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
3503:apa-gaya-
3506:•  j.  apa-gaya-  m.  'Ausscheiden  aus  dem LebcQ,  Ableben':  'gayehe  Y.  46.  4  PUZ,, 4g.  10  PiiZ.,  41.  3  PQZ.,  5j.  8  PüZ.,  16. 10  PüZ.,  62.  4  PiiZ.JJ
3785:•  j.  aibi.gaya-'\  aibi.gäya-'*  Adj.:  -?-, ständiges  Beiwort  des  Aiivisrüi^rima: aiwisrü'äirimsm  'gäim  Y. 2.9;  G.4-Si  — aiwisrO^rimäi  'gayiit  Y.  r.6';  G,  4. 1;  —
3799:•  j.  aibi.giya-  Adj.:  s.  unter  aibi^gaya-,
3899:•  j.  'aiwi-srüSrima-  m,  Gottheit  der vierten  der  fünf  (priesterlichen)  Tages- abteilungen'*, beigenannt  aib:.gaya-  (sd.): 'm^m  aibi.gaim  asavan^m  aSake  ratüm  Y. 2.6;  G..^.5;    —    'mäi  aibi^ayilt  Y. /.  6;
3959:I       VgL  Var.  —  »  Vgl,  igaya-  Ko.   1.  —  »)  Vgl.
7368:KompA.  —  Et.  ?  Anscheinend  a-yap-la-,  ZDMG. 4S.  501, —  np.  .lyißi^,  HüRN  UlrPh.  ^b.  44)0. —  K.:  .>p,tt!M,  lu  Y.  iS.  2  erl.!  p  l  dan  i»  (s.  lu %ra/./la-  No.  3);  Sü.  (zu  V.jj):  iamf,ldhah-am. (lu  V.  28.  a):  aisvaiyaia,  (zu  28.  7)1  ä^hya/ri, |iu  Y.  5J):  samfaltih ;  s.  noch  No.  2.  —  0  So Vi,  8.  49'.  /J-  '35  und  KompA.  —  •)  Pü.: vfieiht  ei  j^.'ii/  a/K  ay,i/i  iar  sahnjer  "Gift ward^von  ihm  gewünscht,  erlangt  von  Seiten des  S.".  —  3>  Vgl.  ^gaya-  No.  I.  —  41  Zum np.  yißan  %.  ap-  mit  No.  9.
10092:•  ii  %■  'gaya-  m,  'Leben;  Lebenszeit; Lebensführung':  gaimäi  ajysitlmcä  (sd.) Y.  jo. 4;  F. 2/,  27a,  N.(?j;  —  stans  'yehe Yt.  io.  71;  \.().  I  PuZ.;  —  apansm  'yehe Yl  /^.44;  —  akä  tu  nS  'yasc3  as/irttSscä (sd.)  Ryä  Y.  4/.  3;  —  *vijvähu  (sd.)  paiti tanuiu    astvä    'yJ    *d3ryeite    FrW.  4-  3 ;
10097:•  j.  'gaya-  m.  EN.  des  ersten  Menschen;
10099:Vgl,  igaya-.  Eig.  'Leben'  oder  'menschliches Leben'.  —  l'a.:  transskr.;  ^jhäh  zu  F.  2/  wird yä«  a  gaySmart  'Leben  und  G'  Qberselit. S.  noch  No.  I.  —  •)  Pü.:  yimän  gaySmarl,  als ob  der  Trat  *yava  gayS  maraia''  lautete.
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
11695:"  j-t  g-  jyätay-  f.  'Leben'.
11697:•  g.  Jyätav- :y>T/»-''  m.  'Leben':  talclt ma  mSnndm  (sd.)  JyStüm  Y.  J2.  11;  — ySi  gSus  mBrmdm  urvSxs.uxl{{&A^  jyötüm Y.J2. 12;  —  dus.sasti!  .  .  mSrindai  (sd.) .  .  jyatSus  .  .  xratOm  Y.  J2,  9 ;  —  yastim xia%raf  .  .  msi^at  (sd.)  jyätSui  vä  Y. 46- a;  —  ys  is  fymiä  hlmi^yai  (sd.) vas7.itSiscä  Y.  5^.  9 ;  —  avais  aibl  ying dairüT  nSitjyätJm  xiayamnfng  vasS  "durch die  (gerade),  die  sie  nicht  nach  Gefallen über  ihr  Leben  schalten  lassen"  Y.^2. I S-  2)  'Lebensunterhalt' :  y!  nsitjyötäm hanarf  (sd.)  vinastJ . .  "der  seinen  Lebcns- miterhalt  nicht  findet  ohne  .  ."  Y._j/.  15.
18296:aiaonyä,  4)  '«yJ  näifjä  *xhiwrä- spahe    a^tunyS,  5)   'nyä  nairyi  gaya-
20030:—  ya  räahaysn  sravaf»ha . .  'rptSnS(AF.) Y. 32.13.  a)  mit  'gaya-  (sd.,  auch  fdSt) EN.  des  ersten  Menschen:  'rata;  •n'^inS, 'rdiinl};  'ry'Sinat.
20320:KompE.  —  Vgl.  mayä;  auch  lEt.  ~  Pü.: [pa)  palman.  —   ')  Vgl.  ^gaya-  No.  1.
20321:•  p.  *inärgaya-''  Adj.  'aus  Mai^iane stammend;  Margianer":  dadarsi! .,  hama- ranam  akunaus  hadä  yatdis  Bh.  3.  ^.
20325:Ableil.  aus  margav;  mit  V^däAik  S  'OO  a.  — Vgl.  mätgaya-.
=== ===
HUB.txt:5825:zlvajjlva 'Quecksilber H. 683; suvaw 'ich gehe' H. 778 ; buvam
HUB.txt:5974:Dagegen zlva, jlva 'Quecksilber H. 683.
HUB.txt:8166:oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
HUB.txt:8188:II, 57; zarf 'tief = zd. jiafra-; ztva --^ jiva 'Quecksilber,
HRN.txt:455:/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
HRN.txt:6030:kurd. zive^ arm. ztpak 'Quecksilber*.- 152 —
```


## [2026-09-06T02:22:03.990Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD zīw ===\"; grep -n \"zīw\\|ziw\\|zīnd\\|zindag\\|zīwistan\\|ziwistan\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD gēt/gēh ===\"; grep -n \"gētīg\\|getig\\|gēhān\\|gehan\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD zīrag ===\"; grep -n \"zīrag\\|zirag\" PHD.txt PHD_mackenzie.txt | head",
 "description": "Grep MacKenzie"
}
```


### [2026-09-06T02:22:04.086Z] TOOL RESULT

```
=== PHD zīw ===
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:766:alive zindag, zīwišnūmand.
PHD.txt:2037:free (a.) abēzār, āzād, harzag, kām- zīwišn; ~ from pargüd az.
PHD.txt:2415:independent kāmag-widār / -xwadāy kām-zīwišn.
PHD.txt:2618:life zindagih, zi(w)i&n(ih).
PHD.txt:2674:zindag.
PHD.txt:3433:revive zīwēnīdan.
PHD.txt:3434:reviver zīndakkar.
PHD.txt:4237:vivifier zīndakkar.
PHD.txt:4238:vivify zīwēnīdan.
PHD.txt:5060:ard! kūmistan kāmzīwišn kamagómand
PHD.txt:5086:zindagih
PHD.txt:5088:zindag
PHD.txt:5104:zēnāwand ayy e$ zēnabzār ` Cer WS zēndānīg oro S zēndān wo pS zēndānbān i^o "GO u$ mër: 15 S. ` mee Ziwénidan zindagih A$ 43 HS zēnīg, zīndag yr
PHD.txt:5489:dagr-zīwišn gilagobàr
PHD_mackenzie.txt:5792:zarwin [ziwp'n I P zrw)n] old age.
PHD_mackenzie.txt:5823: zindag [zy(w)ndk I M zyndg, N zinda] alive, living.
PHD_mackenzie.txt:5829: zistan, v. ziwistan.
PHD_mackenzie.txt:5831: ziwenidan, ziwen- [zywyn-ytn 1M zywyn-] vivify, revive.
PHD_mackenzie.txt:5929:alive zindag, ziwisnomand.                appearance Cihr, des(ag), paydiigih.
=== PHD gēt/gēh ===
PHD.txt:380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
PHD.txt:4769:1-%а2- sazāgīh sazāg sazāgwār sazistan Isazišnīh *sazīšnīg 1-2sazisn gētīg gētīgīg stāy- stāyišnīg stāyišn dīdār stārag stahm stambagīh stambag stahmīh stahmagīh stahmag stayidan sudab
PHD_mackenzie.txt:2505:gehan [gyh)n ' I = M, N gihiin, Jahan] world.
PHD_mackenzie.txt:2511:getig [gytYB, gytydy I M gytyg, N geti] I. the material world; 2. worldly.
PHD_mackenzie.txt:7131:mortal anosxwar, gehanig, marg-                nature Cihr(ag), gohr(ag); ciyunih;
PHD_mackenzie.txt:7979:whoredom rospigih.                     world axw(an), gehan; material
PHD_mackenzie.txt:7980:why ce ray, Cim (ray).                      getig, gumezagih.
PHD_mackenzie.txt:7981:wickedness dusih, wattarih.            worldly gehanig, getig(ig).
PHD_mackenzie.txt:8877:getig, sti
PHD_mackenzie.txt:8891:sto                   --.U\tu.'       getig
PHD_mackenzie.txt:8893:Sadwes                ~,~             getigig                 , UJ()J te..l.'
PHD_mackenzie.txt:9026:sahmgenih              ""'U \ \.s.6U'   gehanig                  \~\-"UU)
=== PHD zīrag ===
PHD.txt:2810:millennium hazirag.
PHD_mackenzie.txt:560:add    *huzirag [llwc'lk IN xujara] little, small, few.
```


## [2026-09-06T02:22:29.835Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== hu.jyaiti ===\"; grep -n \"hu\\.jyäiti\\|hu\\.jyaiti\\|hujyäti\\|hu\\.jyätay\\|jyätay\\|jyäiti\" BRT.txt | head -10\necho \"=== merezu ===\"; grep -n \"m*r*zu\\|marazu\\|mtrizu\\|mBrszu\" BRT.txt | head -10\necho \"=== gaetha as gaida/gaeda ===\"; grep -n \"gaid\\|gai%\\|ga%ä\\|gaeda\" BRT.txt | head -10",
 "description": "More Bartholomae greps"
}
```


### [2026-09-06T02:22:29.951Z] TOOL RESULT

```
=== hu.jyaiti ===
11695:"  j-t  g-  jyätay-  f.  'Leben'.
12903:•  g.  darvgö.jyätay-  f,  'langes,  dauerndes Leben':  apanS  {^.\  'Jyaitlm  ä  x/a^rpm.. ^■33-  5i    —    vTspä    ayärJ  (sd.)    "jyalSil
18156:•  j.  frädat-visp^.hujyätay-  ro.  Name einer  Gottheit,  'die  alles  fördert,  was  zum behaglichen  Menschenleben  gehört':  'Jyai- tlm  lard^uiirffJfimmca  a/ava/i^m  asahe ratüm  Y.  2.  6;  G.  4- 6;  —  'jyStSe  lara- 'huStrS.imtäica  . .  ra^we  Y.  i.  6.
18157:*)  Sie  steht  mit  AiwisrÜ%rima  und  auch  mit Zard^ailröjima  in  Verbindung;  s.  noch  Pü. Eig.  Bed. ;  s.  oben.  —  Pu.:/räj  dälär  1  har- visp  huiäyüttiA ')  buit  u  bar ,  SU. ;  yä  mülam phalam  fravardkayati.  —  ')  Statt  AnävilalA, s.  IQ  tispi^mJaijyätay-  No.  2.
20530:—  'r^m  .  .  haianragaoiim  .  .  bafvar».- iaimafum  ..  ai^afmm  jayaurvanhtm  Vt 70.  7;  —  °r?m  .  .  yahtnäi  mal'äia/um  frä- '^winsat . .  akurö  mazda  . .  karai^yö  paiti barfzaya  Yt  70.50;  —  surunuyä  nä  °ra yamahe  Yt  70.  32 ;  3» ;  —  usta  akmäi  ,  . yakmäi . .  zaota  asava  , ,  'rahe  vaca  yazäite rästun  ahmai  . .  °rB  ma2%anpm  Jcaraiti Yt  70. 137 ;  — yahmai .,*rB jasaiti  avaiiihe yö  baevariJpasanB  vIspB.vtövä  aiaoyamnB Yt  10.24;  —  '"'"  --yS  ■•  aivjyäiti  pasca ha  fräsm5.daitJm  . .  visptm  imat  adkäiti yal  atUan  zqm  asmattfmca  vatnm  zaslaya
24541:•  j.  vispö.hujyätay-  Adj.  '(der  alles  gute Leben  hat,  d.  i.)  der  alles  besitzt  und bietet,   was   zum   behaglichen  Leben  ge-
24549:KompE.  —  iBild.  des  Komp.  s.  lK.g.ao4. — Vgl.  vltpö.h«jyälay:  —  Pü. :  Aatvisp  husäyiSn'l iun  u  bar,  mit  der  ErL:  asi  De  itSn  gmoet [Aarvisf)  huihiihtih  bun  u  bar,  —  ')  NA.  ge- trennt. —  ')  Doch  wohl  alte  Verderbnis  aus kaSvSn;  s.  zu  hujyätay-,  Aiijitay-  und  fräda/,- vrsfqni.hHjy:
25777:'spalten':  ''s^yat  F.  12. mit  ava  und  parStt  'entzwei  spalten, zerspalten,  zerstören':  pairikaya  duiyüirya vupahe  a^hsu^  astvatd  paroit  pairi^nmt (sd.)  avhvam  ava.hisüyüt  Yt.  tV.  54'*. ai.  chidyalf,  ekhidt ;  mp.  apasihät  (s.  zu  tah-')  *), viiislai,  np.  gmiilan,  sbaL  titu/ag,  sisla.  — Vgl.  zEt.  Hbm.  ZDMG.  38.  425.  Bthi.  Stnd. 3.  4,  Bgm.  IF.  6.  92.  —  Pü.  (tu  F.):  *via- heia.  -~  ")  Vgl.  V.  /(f.  19.  —  a)  S.  ferner Pü.  lu  ajyamna-,  atisla-  (,  wo  avismiin  zu lesen),  jayäi,  'Jyä-,  frajyätay-,  sä-  (No.  3), j^Wa-,jKii&ä(;MK.>G]osi.23,  Sg.-Gloss.233b. —  J)  Geschr.  n  dd  at  statt  n  dd  adt ;  Mx.  6g.  36 hat  die  Bombay  er  Ausgabe  dddadi,  aber  die Kieler  zeigt  dd  dat.
=== merezu ===
35:Mein  Altiranisches  Wörterbuch  (AirWb.)  erhebt  den  Anspruch,  eine leidUch  vollständige  und  eimgermassen  wissenschatüiche  Zusammenstellung  des altiianischen  Sprachstoffs  zu  sein,  soweit  er  in  den  bis  jetzt  bekannten  Denk- mälern der  awestischen  und  altpersischen  Sprache  enthalten  ist
36:Für  die  altpersischen  Keilinschriften  habe  ich  die  Ausgabe  von  FHWeissbach und  WBang  zu  Grunde  gelegt  die  sich  in  Band  X,  Lieferung  i  der  'Assyrischen Bibliothek'  findet  Die  zweite  Lieferung  mit  Kommentar,  Wörterbuch  usw.,  die nach  der  Versprechung  auf  dem  Umschlag  der  ersten  schon  1894  fertig  sein  sollte, ist  bisher  nicht  erschienen.
37:In  der  Bezeichnung  der  Inschriften  habe  ich  aus  praktischen  Gründen  meine eigenen  Wege  gehen  müssen;  sie  waien  von  dem  Bestreben  bestimmt,  möglichst kurz  und  doch  deutlich  zu  sein.  Für  die  Inschriften  von  Bahistän  habe  ich  darum die  herkömmliche  Bezeichnung  durch  Bh.  belassen;  alle  übrigen  dagegen  —  mit Ausnahme  der  Siegelsteine  von  Privatpersonen,  auf  die  ich  mit  S.  /,  2  usw.  verweise —  bezeichne  ich  mit  dem  Namenssigel  ihres  Urhebers  —  K.  ^  Kyros,  D,  =  Darius, X.  -=  Xenes,  Am.  ■=  Artaxences  Mnemon,  Ao.  — '  Artaxences  Ochus  ■=—  und,  sofern er  mehr  als  eine  hinterlassen  hat,  einer  beigesetzten  Nummer,  wobei  mir  die  Reihen- folge bei  W.-B.  massgebend  war,  nur  dass  ich  zwischen  NRa  =  D,  6"  und  NRc  = D.  J  ein  D.  7  eingeschoben  habe,  das  die  bei  W.-B,  fehlende  zweite  Inschrift  von Xaki  i  üustam  meint  Praktische  Gründe  waren  es  auch,  die  mich  veranlasst habgn,  alle  Verweise  statt  wie  bisher  üblich  nach  Zeilen  vielmehr  nach  Abschnitten (Paragraphen)  zu  geben,  und  zwax  für  die  fünf  Inschriften  von  Bahistän  mit  je gesonderter  —  nicht  durchlaufender  —  Numerirung.  Ich  biete  im  folgenden  eine Cbersfcht  über  die  verschiedenen  Arten  der  Bezeichnung  (und  Anführung)  bei  W.-B., Spiegix  und  bei  mir.
171:genaue  Umsetzung,  wie  sie  Nöldeke  im  Lit  Centralblatt  iSg4.  151    fordert,  habe
172:ich  nur  in  Ausnahmsfällen  vorgenommen,  wenn  es  mir  zum  Verständnis  besonders
174:Wörter  und  die  wirklich  lesbaren  durch  verschiedenen  Druck  auseinanderzuhalten;
176:wo   man  sich  damit  begnügen  kann,   in  besonderen  Fällen  eine  Note  beizuf\]gen.
177:In  der  grossen  Mehrzahl  sind  ja  die  Ergänzungen  durch  Vergleichsstellen  gesichert
179:verbürgter  Ei^änzungen,  wie  sie  sich  bei  W,-B.  z.  B.  am  Ende  von  Bh.  2  und  j
181:Desgleichen  habe  ich  den  Wortfetzen  in  Bh.  5  und  D.  7  die  Aufnahme  ver- sagL  Wenn  nicht  eine  erneute  Untersuchung  der  Steine  wider  Erwarten  günstige Ergebnisse  liefert,  ist  ja  doch  nichts  damit  anzustellen.
=== gaetha as gaida/gaeda ===
9752:3)  Pa.:ir^'«J«.  -  *)  Vä.:sfhänän.-i)  Vgl.  I  ""^J"^"--   —    i>  Wo  die  üalavö  gai%ya  im
9753:Y.  ^.  12:   gai%S  frädö   mit   J<.   14:  /rWö  1  Einielnen    verieichnet    werden.    —    li    NA.
10008:1)  'kommen',  ohne  Zielangabe;  'her-, hinkommen,  sich  einstellen';  i)  von  Per- sonen: narpm^a  .  .  asnäatca  jas3nt>m düTäaila  Vyt  55;  Y.  jj.  4,  V.  75.  30,  Yt, ig.ii;  —  voha  gaidi  mananks  "komm mit  FJ/."  Y.2Ä6;  —  yahmi  spmta  'kwa mainyO  urvalsl  jasö  mazdä  x/a%ri!  ahml (Sp.  80.)  . .  "bei  welchem  Ende  du  mit deinem  heiligen  Geist,  o  M.,  kommen wirst,  .  ."  Y,  43-  ö;  —  kadä  mazdä  asä mai  ärmaitis  jimat  xfd^rä  husiitis  västra- vaitt  "wann,  0  M.,  wird  Arm.  sammt dem  A.  sich  einstellen,  sammt  dem  XI. das  weidereiche  schöne  Wohnen?"  Y. 4S.  11;  —  fraSa  frayaniu  U  maoö  (sd.) v»r3zyaauhavhs  jasmtu  Y,  10.  14;  Yt  8. 9.  2)   von  Geschehnissen,    Zuständen,
10316:Pü. :  ai!h/  glhäH'l  apar  pa  äyihiih  äyend,  erl.: uilr  apar  apar  äyind.  —  1)  DsT.  ZA.  3.  96: "ou  dans  des  alWes  et  vennes  des  marchan- dises",  Indem  er  gai%anqm  (Pü.)  vä  vayan- lanqm  liest  Unmöglich.  Pü.  muss  auch  für iiriiy'  öder  vay'  ein  anderes  Wort  vor  sich  ge- habt haben.  —  ')  S.  No.  i  und  gü%ä-  No.  2.
10330:*>  Sie  bilden  jedenfalls  den  ältesten  Bestand- teil    des  AweMa.    der   auf  die  Anfangszeit  dei urn^juii^i sehen  Religion  und  auf  deren  Begrün- der inrückfBbrt.  Die  Zusammenfassung  mehrerer Hymnen  {7:  Y.  38-34;  V-  Y.  43-46:  4:  Y.  47~ SO)  la  «incr  Cä%,i  (im  ireiteren  Sinn  und  di im  Gegensatz  zu  Hilay  'Kapitel')  hat  nur   < äusseren   Grund    gleichen    Strophenbaus.     ] Namen,  die  die  einzelnen  Gäi,ä&  und  ihre  l!älay% führen,  sind  durch  deren  Anfangsworte  bestimmt, ausgenommen  der  der  ersten  Gii%ä  {ahunimaia, sd.)-     Nach   den  fünf  Gä%ä%  werden  die  einge- schalteten letzten  fünfTage  des  Jahres  benannt; i.in  vaUilSülay- k.  Vgl- noch  Gdn.  GIrPh.2.  25. —  •♦)  S.  dazu  GlrPh.2.s8  oben.    Die  TOn  Bk. Stud.    /■  45z     ausgesprochenen    Anschauungen halte  ich  für  ganz  verfehlt  —  *•♦)  Es  geht  das aus  V.  10.  2  ff,,  N.  33  hervor.    Es  mögen  wohl auch  noch  Y.  73  und  /J  (Glaubensbekenntnis)  und jS  {fiüiö  Hnjärö)  dazu   gerechnet  worden  sein, die  ebenfalls  das   äussere  Merkmal   der  (><iä<rs, die  Längung  der  Endsilben  zur  Schau  tragen. KompA.,  E.,  Ableit-  —  Zum  aL  V-  gayali.  — ü.  gathä-    f.    —    Vgl,  *gi%r-a:    —    Pü. :   j^s. gäsäa  {Tr«ns6kr-);  *-  noch  No.  4.  ~  '>  Hds. giira.  —  ')  Hds.  2XaaXgae%äi  i.  oben  aE.  und gai%ä-  No.  I4.  —  ä  UAs.pä%ä.    —   4)  Pfl.: csän  ie  gäsän  fa   rat  /ranämiinlA   ape  franä-
12440:KonpA.,    E.    —    Et?    Gon.S  Versuch,   der '*daiaä-  und  *dainä-  etjrmologiich  gleichselit -  inm  V.  Väty)-  -  überzeugt  mich  nicht,    S. noch  No.  I.   —   np,  din.  —   Pü.:   den,   Sü.: dätih{%    —    I)  Wo  a?  im  Metram   für  iwei Silben   rechnet;    s.    'dainä-.     Also   wohl   ae ans  ar.  d^i^,  %  St. •  j.,  g.  'daena-  £  Hniieres  Wesen,  geistiges Ich,  Individualität',  öfters  kaum  übertrag- bar"; i)im  gAw.'':^<i/«J  maadapaour- vTm  gai%äslä  la^  'näs^  %wä  manankä xratüica"^  du,  qM.,  zu  Anfang  Individuen schufst  und  Individualitäten  durch  deinen Geist,   und  Verstandeskräfte"  Y.  3t.  1 46.  6;    —    nSit  nä    manä    ,  .   s}ngA3 xraiavö  .  .  varanä  (sd.)  .  .  uxla  .  .  }yi "hanä  .  .  "na  .  .  urvaaB  hacainil  Y.  4$. —  vaauklmcä  °nqm  ..  fstratam .. ärmaitim "^•37-  5i  —  ^^  ^'^  ux^äis  fyao%an3  'tiä (IS.)   a&m  spnvat  (sd.)  Y.5/.  ar;  —  y7 *iat  manS  vahyS . .  aSyaslä  (sd.)  kvö  'nqm iyaoiianacS  valanhScä  V.4S.4;   —  yqm yao/  (sd.)  •nqm  .,  dämyam  *hudJnao^ .. y.44.^;  —  yS  'nqm  vohü  ^sänltä  (sd.) ftananhä  Y.  49-  5 1  —  '?«"  ^^^  dqstvam (sd.)  'nayai  frävao'a  Y. 46^.7;  — frö  .  . a-sä    'na  fradaxsaya  (sd.)  Y.  j^.  13;    — AvB  tat  .  ,  ahtnäi  dazäz  (sd.)  'nayä  (IS.) z-aldMtttö  Y.57. 19";  —  mSnÜl  T  mqtdas- düm  *valds.düm  'näbll  aiyasta  (sd.)  ahBm yJ  . .  Y-53-  s";  — yas/ä  .  .  tarJ.mqsia  ,  . sao^aiUS   Sng  (sd.)   patdU  spmiä    'nä urvahs  .  .  ".  .  des  Saelyant  .  .  Ich  wird ihm  Freund  sein  ,  ."  Y.  45. 1 1***;  —  tJm aAfSfum  . .  'nä  saoiyantqm  yä  . .  urväxiat (sd.)  hyat  .  .  mTedtm  .  .  Y._j4.  '3;  —  yä "nü     vairXm    hanät   mjedtm    asahya  yssa astftt  (sd.)  Y.  54. 1 ;  —  hyai  'na  vakUn yBjpn  (sd.)  mlzdlH.49-  9;  —  ^y<'i  mlSdjm ^trtavai^lm   (sd.)  fradadä^S    'näbyni^  Y. 40.  I  ;    —    harthus  (sd.)  .  .  dadät   aAurS 'fiayüi  va^huyai  Y.  5j.  4;  —  'nayäi  va»- ktiy^i  yqm  ksi  Uyam  (sd.)  äatü  . .  ahuri>
13021:•  j.  dasa-  n.  'Gegenstand  der  fahrenden Habe,  Vennögensstlick'"*:  yaa  .  .  layul vS  Vfhrkö  vä  haca  gai%abyS  paraMaraiti •sa  (AP.)  "wenn  ,  .  ein  Dieb  oder  Wolf aus  dem  Anwesen  fahrendes  Gut  fort- schleppt" V.  13.10.
13415:—  nrmasf  lg  ahura  . .  "i^rlscii  pars  anyäis  ■ 'man  Ny.  J.  i ;  —  ahur?m  mazdqm  main- yaom  mainyavanqm  'manqm.. zara'iusfr?m\ spitamtm  gai%tm  gaii^yanam  'manqm  .  .  j ahümla  ratamcaVt.2.4;  Vd.2o;  —  ahurahe' mazdä ya'ha  'man  da'hatYt.ip.io;  —  vlspe\ te aAur3iiX3.V.YoV^..vanuATs  'man  asdonis .  .  y3il  dadaha  Y.  ji.  10;  Vr.  72.  4;  — . sraos^m  .  .  yS  .  .  nipaitt  mazda  'man  Y. , 57.16;  16,  31;  —  paoirys  mazd\ (GS.)  Y.57.  2;  —  ya'ia  aam  ammxtlm ava.barani  avi  mazda  'mabyB  Uta  aam apa.barani  uva  fu'itmca  tarsmmca  hala mazda  'mabyö  Yt9.9r.;  gf.^;  —  iir?hqm 'manqm  yai  ahurahe  mazda  Yt  7(),  1 8 ;  — ahuTTm  mazdqm  .  .  äätärfm  vahinqm 'manqm  Y.  16.  \\  —  vTspais  . .  yäii  sp?n- tahe  mainySu!  'man  Yt.Ä48;  lo.  142,  V. 5- 33t  'J-^S,  VyL5/;  —  vTspanqmca  ippn- tahe  mainySui  'manqm  aiaonqm  asaoni- nqmca^^  asahe  ra'^wqm\.i.\6;  —  avasö.- xid^rS  hyat  drvä  ..  nizbprttö  haia  spgntahe mainyius   'mabyS  Y,  Ä  6;   27.  2,  Vr.  72.  4;
15323:mit  apa  dnwS.:  yn  ga%ä  asrsvayö  afa tansm  *piTynti^'^''*  N.42.
18130:asaone  V.  2J.  i.  a)  bes.  mit  Beziehung a.\^gai%ä-  gebraucht'':  aAam  (Sp,  107  m.) dadäl  ahurö  ahmäi  gatisi  vohB  frädat manavha  ^.46- 13;  —  damam  . .  yä  mit gat^i  asa  fradöit  ha^mnä  (sA.)  Y. 44.10; —  vaM  manaivha yehyä  syao%anilis gaU'^S aia  frädfntl  (als  Pass.)  "mit  VAf.,  durch des  Tätigkeit  Haus  und  Hof  von  Asa  ge- fördert werden"  Y.4J.6;  —  Jat  ml ga^^t'r /rO^aya . .  var^aya  V.  2. 4 ; — az»m  tl  gaf^a Jrälayfni ..  vari^ayeai  V.  2.  5.  2)  Med. 'wachsen,  gedeihen':  haoma  raose  gara paiti  Uta  /rä^aS^a  vifpaiia  Y. /o.  4;  — neben  vartd-'.frainmnahe^  vanifmna/ie xrahwsmtiahe  suyamnaAe  V.4-2  Gl.
```


## [2026-09-06T02:22:40.765Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== gaetha head ===\"; grep -n \"gai%ä-\\|gae%ä-\" BRT.txt | head -6\necho \"=== merezu jiti ===\"; grep -n -i \"kurzlebig\\|jiti-\\|jTti-\" BRT.txt | head -10\necho \"=== jva ===\"; grep -n \"•  j\\.  jva-\\|jva-  Adj\\|jvant\\|jvaiti\" BRT.txt | head -10",
 "description": "Locate Bartholomae entries"
}
```


### [2026-09-06T02:22:40.861Z] TOOL RESULT

```
=== gaetha head ===
10330:*>  Sie  bilden  jedenfalls  den  ältesten  Bestand- teil    des  AweMa.    der   auf  die  Anfangszeit  dei urn^juii^i sehen  Religion  und  auf  deren  Begrün- der inrückfBbrt.  Die  Zusammenfassung  mehrerer Hymnen  {7:  Y.  38-34;  V-  Y.  43-46:  4:  Y.  47~ SO)  la  «incr  Cä%,i  (im  ireiteren  Sinn  und  di im  Gegensatz  zu  Hilay  'Kapitel')  hat  nur   < äusseren   Grund    gleichen    Strophenbaus.     ] Namen,  die  die  einzelnen  Gäi,ä&  und  ihre  l!älay% führen,  sind  durch  deren  Anfangsworte  bestimmt, ausgenommen  der  der  ersten  Gii%ä  {ahunimaia, sd.)-     Nach   den  fünf  Gä%ä%  werden  die  einge- schalteten letzten  fünfTage  des  Jahres  benannt; i.in  vaUilSülay- k.  Vgl- noch  Gdn.  GIrPh.2.  25. —  •♦)  S.  dazu  GlrPh.2.s8  oben.    Die  TOn  Bk. Stud.    /■  45z     ausgesprochenen    Anschauungen halte  ich  für  ganz  verfehlt  —  *•♦)  Es  geht  das aus  V.  10.  2  ff,,  N.  33  hervor.    Es  mögen  wohl auch  noch  Y.  73  und  /J  (Glaubensbekenntnis)  und jS  {fiüiö  Hnjärö)  dazu   gerechnet  worden  sein, die  ebenfalls  das   äussere  Merkmal   der  (><iä<rs, die  Längung  der  Endsilben  zur  Schau  tragen. KompA.,  E.,  Ableit-  —  Zum  aL  V-  gayali.  — ü.  gathä-    f.    —    Vgl,  *gi%r-a:    —    Pü. :   j^s. gäsäa  {Tr«ns6kr-);  *-  noch  No.  4.  ~  '>  Hds. giira.  —  ')  Hds.  2XaaXgae%äi  i.  oben  aE.  und gai%ä-  No.  I4.  —  ä  UAs.pä%ä.    —   4)  Pfl.: csän  ie  gäsän  fa   rat  /ranämiinlA   ape  franä-
18130:asaone  V.  2J.  i.  a)  bes.  mit  Beziehung a.\^gai%ä-  gebraucht'':  aAam  (Sp,  107  m.) dadäl  ahurö  ahmäi  gatisi  vohB  frädat manavha  ^.46- 13;  —  damam  . .  yä  mit gat^i  asa  fradöit  ha^mnä  (sA.)  Y. 44.10; —  vaM  manaivha yehyä  syao%anilis gaU'^S aia  frädfntl  (als  Pass.)  "mit  VAf.,  durch des  Tätigkeit  Haus  und  Hof  von  Asa  ge- fördert werden"  Y.4J.6;  —  Jat  ml ga^^t'r /rO^aya . .  var^aya  V.  2. 4 ; — az»m  tl  gaf^a Jrälayfni ..  vari^ayeai  V.  2.  5.  2)  Med. 'wachsen,  gedeihen':  haoma  raose  gara paiti  Uta  /rä^aS^a  vifpaiia  Y. /o.  4;  — neben  vartd-'.frainmnahe^  vanifmna/ie xrahwsmtiahe  suyamnaAe  V.4-2  Gl.
=== merezu jiti ===
=== jva ===
6958:•  j.  ahyäsä-"  fem.  Adj,  'die  Worte  ahyä '  •  j.  a-x'^sa-  n.  'Nichtessen':  s^älaya  vispö yäsä    enthaltend,    damit    beginnend':    'ia  '  afvhtts  .  .  jvaiti  "se  fi-amiryeite  V.^.33. Äaiii/ (sd.)'i   Y.  2<S'  Überschr.;    —    'sqm       Fa.:  Aa^  ax'arü-  - AaUlm  yazamaide  V,  a.S' is,
7220:•  j.  a-x'^äa-  n.  "Nichtessen":  ^aiaya  vTsps atihuS  .  .  jvaiti  'se  framiryelte  V._j.  33,
10078:1)  'leben,  am  Leben  sein':  Aaca  irista upa  jvantjm  V./O.i';  —  irJrPiidqm  .. jvantam  .  .  azStanam  Y.  24.  5;  —  :^a- saya  .  .  vTspS  atikus  *jvaiti'*  ax^äse  fra- miryeite  V.  .9.  33;  —  ||  ut~i  dargam  jtva (aSKA.)J'  "und  du  sollst  lange  leben" Bh.^.io,  16;  —  darpy)m  jva  ustn  jva (zSIA.)  A. /.  la;  — tä  xsapaiiB  ya.  *}Vähi "(all)  die  Nächte,  die  du  leben  wirst"  Y. 62.  10*'.  a)  mit  '[S>.gaya\  yavata  gaya
17809:•  j.,  g.''  fravaäay-  f.  ^Fravasay*'>,  Be- zeichnung für  das  dem  Gläubigen  eigene Unsterbliche,  das  Element,  das  schon  vor setner  Geburt  vorhanden  war  und  ihn  über- dauert. So  lang  der  Gläubige  lebt,  wacht seine  Fr.  als  Schutzgeist  Über  ihn.  Die Gesammtheit  der  Fr.  der  Gläubigen  aber spielt  eine  ähnliche  Rolle  wie  die  indischen pitärah,  die  römischen  ««««■:  'sayö  hütti^ Aatqm..aigAu^qm..bUsyantqin{Sf.^^i  m.) a!'aanqmYt.i3.2\;—ä  hätqmca  anhusqfnca zätanqmca  azätanqinca  asaonqm  ilajasmiu °sayd  Y.  öj.  6;  —  aat  anyaisqm  'say!> jvanqm  narqm  aiaonqm  aojyehfi .  ,  ya^a iristanqm  "aber  im  übrigen  sind  die  Fr. der  lebenden  Gläubigen  stärker  als  die der  gestorbenen"  Yl;_j.  17;  —  vispäbyö asaonibyS  *nbyS  y3  irlrüu/qm  .  .  yasia jvantqm  .  .  yäsca  narqm  azätanqm  Y. 24-5;  —  vispanqmca  änhqm  alaonqm asaoninqmla  ila  yaxamatde  °stm  Yt,  ij. 148';  —  neben  'aAs-,  *da?nä-  usw.; alaonqm  aiaoninqmla  ahümla  dafaqtnca baoiasca  urvarumca  °slmca  Y.  26'.  4;  — gai^ssca  asdsbJlca  us'tänqsca  kahrpasca Uvlilsca  baohasia  urvämmca  'sTmca  Y. 55,  I ;  —  xardkuitrahe  . .  'Am  . .  sravä  . . dainqm  . .  varvtifmca  tkais»nca  Y.  16. 2 ; —  manä  . .  dalnä  . .  urunS . .  'say!)  (als  AP.)
19948:mit  fra  dnwS.A"':  s^äsaya  sT  vTspS anku! . ,  *jvaiti  a:fale  /ramiryeite  "durch Essen  lebt  die  ganze  Welt,  durch  Nicht- essen  verliert  sie  das  Leben"  ^■3-Zi- ai.  myläh;  vgl.  mriyäte;  v^.mTrad,  murda. — Pü.:  {/rd(\  murlan.  —  D  Statt  miiry-,  S  aSS. 40.  - —  =)  Im  Gegensatz  lu  rcü%;  para.riü%-; vgl.  Yt.  zj.  17  und  V.  S.  37f..  H.  3.  1,  16 und  19,  34.  So  im  A«.  überall  ansxer  in amarsanU.  —  3)  Hd*.  mairy'.  —  4)  So  K  30, M6.  —  5)  Hds.  yaouAa;  vgl.  S  afij.  30.  S. aber  Vyl.  63.  —  *)  Die  Hds.  haben  lu  FrW. S  zweimal  mtryäitt  (dessen  Schreibung  mit  f durch  die  spätere  Form  des  Worts  veranlasst ist)t  einmal  das  Ungetüme  miryaeiatüi  (oder •lalle),  nach  Dst.  ZA.  3.  8  'fulur  moyen'f!).
20412:•  j.  murazujva-  Adj.  '-  ?  -  lebend': x^a/sata  mafyäkatihs ..'jvanfüS ..  mirnu.-
20719:mSi  y  tvSm  vidvä  (sd.)  Y.  48.  2 ;  — y  xsa- 'iirS  *grjhmS  hjsasat  aaüaAya  dtmäni  ma- natjhff..Jigfr)sat{zA.)Y.32.ii.  2) 'wenn' 3': ma  eis  ,  .  frarmharat  y  nsit  .  .  atnats Ytio.  uz.  a)  vorher  geht  ta  (Stverz., Sp.  612  in.):  tum  tä  daiiikävB  nipahi y  Auhnitlm  yaiayeiti  (sd.)  Yt./O.  78;  78; —  kai  tä  nara yaoidayqn  anhm  ..y  na- säum  franukarat  V.7. 2  3 ;  usw.  3 )  'dass', einen  Subjekts-  oder  Objektssatz  einleitend; a)  mit  Konj.;  a)  vorher  geht  tal:  taf  (Sp. 618  m.)  mazda  tava  xsdhr^m  y'  .  .  dähl drigaovi  (sd.)  vahyu  (wörtlich)  "das  ist (darin  besteht)  ..  deine  Macht,  dass  du  .." ^-53- 9.  ß)  voraus  geht  ta  (Sp.6i 2 m.): yäi  yO/tJ  /ramTma%a  (sd.)  y^  masya  ,  . vaxi?iili  daivS^ustä(%±)\.32.^.  b)Ver- bum  fehlt:  dastü  .  .  y  vS,  mqhra  srivTnt äradä\.28.T, —  £K//(Sp. 272  o.)^"  *aya»- haina  spar^a{sA.)  Yt  io.  129 Gl.  4)'auf dass,  so  dass,  damit';  a)  mit  Ind.:  a  ma äidSm  . .  y  sruyi  pari  (sd.)  *magaong  Y. 33- 1-  b)  mit  Konj.  (oder  Inj.):  aAyä yäsä  (sd.)  .  .  syaahana,  vaiahSui  xratüm manarvhS  y  xsnnlia  (sd.)  gSui^a  *urvq- n>m  Y.2ÄI'';  — aivä  vJspSng  äySi..y aiat  haca  jvamakT  {&A.)  Y.^J/.S;  —  tsm .,  varam i^t.) y^  fo%rdi  »r<A!/(sd.)  Y.j^. 4;  —  at  töi  myazdim  .  .  däma,  gag'hä vTspä  ..  */°*'  voAß  %raosta  (sd.)  manariha Y.J4.3";  —  ..hatayme..hutaosqin  anu- matSe  dalnayai  . .  y'^'^  ml  daSnqm  . .  zras- (sd.)ca  däl  . .  y^^  ml  vanzänüi  va^uklm dat  frasastim  YL 5.  26;  —  eaval  dbötUim ayantm  fararshacäiti {&A.)?  y'^  *frayar3ne va..  aiwyäs/isisd.)  atpAalii.g.  c)  mit Opt.:  tat  n3  ziTdvanöi (sA.)  vaoca  ..y°  jvantd vXspSiig  vauraya  (sd.)  Y.JJ.3.  a)  voraus geht  tat  (Sp.630  o.);  akyä  ..  nS  dStdl .. tat  ahya  y  tat  upa.jamyama  .  ,  Y.  ^o. 2.  d)  das  Verbura  fehlt;  frasravayö ava  diJkra  yim  dim  vasnat  *svistaih)a (sd.)  *vindän3m  nBtt  *ava  y"  *vistaliva N.  iö'".  Undeutlich:  y   ahmst  (Sp-
22748:kaus.  BedeuL  'überzeugen,  ■aitisiv',  Med.  I J  MäfyJ' .  .paruv  *%aäayä* . .  nailim  vama- 1 vätaiy  duruxtain  (sd.)  *maniyätaiy  Bh.  4- S;  —  tya^  manu  kartam  varnavatam  1 "^uvam  mJ/yJ*  *draujTyähy  {^A.)  Bh.  4.  6; — . .  nüram  %uväm  vamavaiSm  ty<^  mann  \ kartam  ai'a3ij(sd.)..Bh.4. 10.'!  a)gAw.  | insbes.  vom  Überzeugen  auf  religiösem  1 Gebiet,  sva.  'zum  Glauben  bringen,  be- kehren'; nur  Int.,  Med:  tat  nS  ..  vaolä^ kisvS .  .y3  jvantd  vispSng  väuraya  ( 1 SOM.) ". .  auf  dass  ich  alle  Lebenden  überzeugen  , kann"  Y.jr.  3;  —  >43  (näml,  viääitis)  zT- pourül  ispnts  väuraitl  "sie  wird  ja  noch ' viele,  die  hören  wollen,  veranlassen  sich zu  bekehren"  Y.  47-  6.  ")  'bekehren zu  — '  (Akk.) :  ana  mahrH  matist>m  väitröi- maidl  xrafsträ  hizvä  "mittelst  dieses  (Ver- heissungs)  Wortes  wollen  wir  die  Xr.  (das Raubgesindel)  mit  unsrer  Zunge  zu  dem bekehren,  was  das  grösste  ist"  Y.  28. S-  {varänJ  Y.j^j.  4:    lies  livarünT,    s.
24744:/ravasayü  jvanqm  . .  ao/yehl/ . .  yaka  iris-  "bii tanqm  Yt.  7^.  17;  — fravasibyS  yh  irJ-  VI** ri'^u/am  .  .  yUsca  jvantqm  Y.  24.  5;    ■ — ■ ,
24749:Vd.  2',  17;  —  cvant^tn  dräjg  sairi  ma/ya' in  —  (Akk.),  sich  hineinstecken':  tiltryJS iriste  z)mS  nthsite  .  .  sfmö  bavainli  V.  .  .  kthrptm  ral'i:Wayeiti  ".  .  nimmt  eine 7.4s;  — yS  narS  asaanH  trlri'iusö  Z7ml  sichtbare  Gestalt  an"  Yt,  Ä  13;  —  yeähe kihrpa  nikainti  V.  _j.  40  PüZ.;  —  yal  bä  . .  kfhrpasca  ya  raF^wayeiti  srfra  anusa- paili  fraSsi>m  sairi  tiikante  spänasla  nqm  ".  .  und  die  Gestalten,  die  er  an- irista  naraica  irista  V._j.8;  la,  36,  Ä  '  nimmt,  sind  die  schönen  (Gestalten)  der  .." 14;  —  ailala  arte  nasukas'd  nisAioafta(sä.)\Yt.  jj.St.  4)  trans,  'etwas  vermengen, avavat  haca  iristaiibyS  yaia  "irigäim  ,  vermischen  mit  —'{Instr,):  äat  *rai:'ä)wiska- V.  &  ri ;  —  iha  iristanqm  urvqnö yaza'\rahe  (sd.)  ya^  &aom?m  gava  * rafiwayät''^ iiiaide  ya  asaonqm  frarasayB\,26.  7;  i6.\baxsayaatea  ü.jö.  Undeutlich:  aiv(&a 7,  FrW.io.39;  —  sät>m  da%aiti  urvämm'^  asitäkrat  hävanänt  *rasiiwayeiti^''  N.Ä); asaonS  *iriri%änahe  P.24'';  J53';  — \ —  kahmäi  kala  * myazdavanam  myasde yat  irista  paiti  usihistqn  Vt,  7(j.  11;  — .raghwaiti  N.(ii,(J2*''. US  irista  paiti  araiiH  *vijvähu  paiti  ta-\  mit  upa  'eindringen  in  — '  (Akk.):  nasus nuiu  astvä  gayS  *däryeite  (sd.)  FrW.  4.  2 ;  ,  ,  yä  Äaca  irista  upa  jvant»n  upa.rai- s.  noch  *iri^yant-.  "hwaiti  "die  N.,  die  von  dem  Toten  aus  in
```


## [2026-09-06T02:22:50.892Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20408,20420p' BRT.txt\necho \"=== gaetha entry head search ===\"\ngrep -n \"gai%ä-  f\\.\\|gae%ä\\|Vermögen.*Habe\\|'Anwesen'\" BRT.txt | head -8",
 "description": "Read mərəzu-jva entry"
}
```


### [2026-09-06T02:22:50.964Z] TOOL RESULT

```
•  j.  "mflrKzu  F.  II. Ist  aus  minsu.jiiay-  oder  mirtm.jva-  loagelösL
—  Pü.:  aank.
•  j.  manizujitay-'*  i)  f.  -?-:  drvatqm datvayoinanqm  'dm  mafyanqm  V.  ig,  36, 29,  4i*>.  i)  Adj,— ?-:  il'afsata  ma^a- kär>hil  ..mfrizu.jva^hO  ..'jUayS^xVi.io.^Z.
Vgl,  m^rfcu.Jva-,  wonach  das  Wort  als  z.Teil Jitay  "Leben'  enthält;  s,  auch  Pü.  —  Pü.: aanka)*^!^!«.  —  ')  FrW.  getrennt—  >)  S. tnch  fiarajitay-  V.  73.  tl.  —  3)  S.  aber  lU 'nur/tin/:  —  4)  Mit  der  np.  Glosse :  räA  am 'Stiasscnräuber'.
•  j.  murazujva-  Adj.  '-  ?  -  lebend': x^a/sata  mafyäkatihs ..'jvanfüS ..  mirnu.-
jftayS  FrW.  10.  42.
\n\iliviiH;  Tgl.  /n  'nurtsai/-.
I  •  j.  msmzyumna-  Adj.  (fem.  'aJ-)  -  ?  - :
dby  Google
"75
murvzda-
mo]ii.tbiä-
176
=== gaetha entry head search ===
8047:•  j-.  g-  tätay-''  f.  i)  'Vermögen,  Können, Imslandsein,  Kiaff,  mit  Inf.:  Aat  vf  xsa- :^r^m  kn  'trfi'SS.)  iyao>amli  masda ya>ä *vä  ^kaxmi  (sd.)  asä  vokü  manatikä ^mydidyni  (sd.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  . .  'lfm  anum v)r?^r(qmnua  Yt.  ici.33;  —  ydi^a  , .  uz-
9742:—  yavanqm  .  .  västranqm  .  .  '•%anqmca  Wesen  und  Dingen  zum  (Reich  des)  Asa, ashaiiinqm  YtÄ29;  usw.;  —  s.  noch  zur  stofflichen,  sichtbaren  Welt  des  Asa Anhang  «.  2)  'Wesen'  im  Sinn  von  gehört':  'irj^räi  asake  °'^anqm  "um  zu 'Anwesen';  'Gehöft,  Haus  und  Hofs>,  schirmen  alles,  was  zum  Asa  gehört"  Vt. Hausstand  (ramilia)',  überhaupt  'Hab  und  /p.  48;  Y. 55.  3^  57.  17;  —  makrkai  alahe Gut' (im  Gegensatz  zu /<2ns-,/fl«a/-), 'weit-  '>anqm  Yt. /<).  50,  Y.(?.  8;  <?.  3,  V. /Ä  sSi lieber  Besitz*  (im  Gegensatz  zu  ankav-  —  asiby5  yli  urvätäiS  drRjS  asahyä  '^ii I  2);  Sing,  und  Plur.i  yi  .  .  varidayoSä  vTtn?r?ncaiti  (sd.)  Y.31.  1;  —  ^un  ''^ä yqm  nasdi/tqnt  '^qm  dr»^a  iax/ai ff.. (sd.)  amar/antis  ya  ahhe  Yt,  sf).  la;  — drufim ^■5'>-Z'>  — yä^a  ■  ■  v?hrkqm  azr5.dai)tTm\iti~barat  asahe  haca  ''iabyS  Yt.  ig.  93;  — fsd.)  -iaw  avi  frafiaiaiti'y.  18. 6 $'•'>■,  N.  —  s.  noch  Vt.  6'.  i  (unter  z).  a)  auch 3'Q);  —  spämm  dd^tm  ..''i^anqm  Aar»-  mA  astvanh  Adj.:  ktmat  atiAsus  astvatS ^räi  V./y.39";  — yesi  narü  ..  kafa  aoi  .  .  '''^abyö  *  astvaitibyS^^  asake  ^.13; ''iäbyS  pain.iri>:yeiii  Vd.  13;  —  cval  ns  —  gandartwim  , .  y3  apatat . .  m»r»xlam ä^rata  (sd.)  a>aurun?m  haca  *'%äbu^'>  °^J  astvaifiS  alake -Hx.  iQ.  i,\ ;  V./iV.  55, *parayät  N.  4;  —  yS  ^yujyasfim  //a.ft  .  SrB.j;  —  dar7sca(sd^  ddisat'^amfrixsyan- '"iabyd  paräiti    V.  13.  17**;    —  yas)  tat  tim  vTspqm  yqm  astvaiHm  gai'iqm  Yt.ig.
10330:*>  Sie  bilden  jedenfalls  den  ältesten  Bestand- teil    des  AweMa.    der   auf  die  Anfangszeit  dei urn^juii^i sehen  Religion  und  auf  deren  Begrün- der inrückfBbrt.  Die  Zusammenfassung  mehrerer Hymnen  {7:  Y.  38-34;  V-  Y.  43-46:  4:  Y.  47~ SO)  la  «incr  Cä%,i  (im  ireiteren  Sinn  und  di im  Gegensatz  zu  Hilay  'Kapitel')  hat  nur   < äusseren   Grund    gleichen    Strophenbaus.     ] Namen,  die  die  einzelnen  Gäi,ä&  und  ihre  l!älay% führen,  sind  durch  deren  Anfangsworte  bestimmt, ausgenommen  der  der  ersten  Gii%ä  {ahunimaia, sd.)-     Nach   den  fünf  Gä%ä%  werden  die  einge- schalteten letzten  fünfTage  des  Jahres  benannt; i.in  vaUilSülay- k.  Vgl- noch  Gdn.  GIrPh.2.  25. —  •♦)  S.  dazu  GlrPh.2.s8  oben.    Die  TOn  Bk. Stud.    /■  45z     ausgesprochenen    Anschauungen halte  ich  für  ganz  verfehlt  —  *•♦)  Es  geht  das aus  V.  10.  2  ff,,  N.  33  hervor.    Es  mögen  wohl auch  noch  Y.  73  und  /J  (Glaubensbekenntnis)  und jS  {fiüiö  Hnjärö)  dazu   gerechnet  worden  sein, die  ebenfalls  das   äussere  Merkmal   der  (><iä<rs, die  Längung  der  Endsilben  zur  Schau  tragen. KompA.,  E.,  Ableit-  —  Zum  aL  V-  gayali.  — ü.  gathä-    f.    —    Vgl,  *gi%r-a:    —    Pü. :   j^s. gäsäa  {Tr«ns6kr-);  *-  noch  No.  4.  ~  '>  Hds. giira.  —  ')  Hds.  2XaaXgae%äi  i.  oben  aE.  und gai%ä-  No.  I4.  —  ä  UAs.pä%ä.    —   4)  Pfl.: csän  ie  gäsän  fa   rat  /ranämiinlA   ape  franä-
```


## [2026-09-06T02:23:08.381Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN gitI ===\"; grep -n \"gîtî\\|gTtT\\|gitl\\|gêhân\\|gihän\\|gehän\\|Welt'\" HRN.txt | head -20",
 "description": "Grep Horn for gītī"
}
```


### [2026-09-06T02:23:08.437Z] TOOL RESULT

```
=== HRN gitI ===
3997:jehan, jihän 'Welt* s. gehän (No. 951).
8183:np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
8232:neupersische Form ist gehän (No. 951).
8238:951. gehän *Welt\ arab. LW. ßhan, jehän^),
8239:aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
10075:vergl. unter bayisten, oben No. 179) 1) aufgehängt,
11046:aw. sti- \Schöpfung, Welt'«) (ami. LW. asti-ß ^Welt'j
```


## [2026-09-06T02:23:10.430Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# leaf = printed + 21 -> printed 212 = leaf 233\nfor leaf in (233,):\n    print('--- leaf',leaf,'---')\n    print(pages[leaf][:3000])\nEOF",
 "description": "Print Horn page 212"
}
```


### [2026-09-06T02:23:12.844Z] TOOL RESULT

```
412
--- leaf 233 ---
— 212 —
949. (feU ^Welt\
aw. ga^^ya- 'irdisch'; phlv. getlk^).
Mot savant; die den Lautgesetzen entsprechende
neupersische Form ist gehän (No. 951).
950. ges, gesü 'Locken, öelock'.
aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
netes Haar (ZBÖL); phlv. g^s^ arm. syr. LW. ges,
ü^: *Haar\
oss. d. yesä, t. qts *Borste*.
951. gehän *Welt\ arab. LW. ßhan, jehän^),
aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
r:} (de La gar de, Semitica I, 59).
L.
952. lfrJ)e, läwe 'Schmeichelei, Bitte', lähidefi,, laf 'Prahlerei*.
skr. l^lap' (ai. rap-), Idpati 'schwatzen', vergl.
ud + lap' 'liebkosen .
siyn. I6w-am, sar. lew-am 'reden, sprechen, sagc^n';
af/. laudal 'sagen, erzählen'.
953. leh 'Lippe*, vergl. lefj^ leföe.
Käs. lew; kauk.-bergjüd. low,
phlv. lap; lat. labium; nhd. lAppe (vgl. Kluge,
Etymolog. Wörterbuch s. v.).
kurd. liw 'Lippe'; bei. lap (216); wa;^. law^ lafc,
sangl. law,
954. listen 'lecken*, Praes. les-em, lestden.
Kää. Z. bSles,
phlv. listan, l(i)stan (AV.); ap. l/^*lais- {V^leig^h- + ,<?);
vergl. ai. [/'reh-^ rehmi, skr. teÄ-, lehnii 'ich lecke*;
arm. lizeniy lizum etc. (H. No. 123); wa/. li/'am.
^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
gethih, und so ist also wohl auch im Pehlevl get(Ofi zu lesen. Np. geil
geht aber jedenfalls auf ein, dann allerdings falsches, phlv. ge Ik zurück.
Ist get(i)h etwa von st(Oh beeinflusst?
*) Eine persische Etymologie (von jehlden) siehe Vis und Rämln,
Seite 83 Vers 17.
```


## [2026-09-06T02:23:23.833Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor l in 5820 5970 8160 8184; do echo \"--- $l ---\"; sed -n \"${l},$((l+12))p\" HUB.txt; done",
 "description": "Read Hübschmann jīva contexts"
}
```


## [2026-09-06T02:23:24.114Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6025,6040p' HRN.txt",
 "description": "Read Horn zīve context"
}
```


### [2026-09-06T02:23:25.650Z] TOOL RESULT

```
--- 5820 ---
379, oben p. 47; tuvan Sermogend' H. 401; javecl Wig
H. 414; javan, juvan Miingling H. 429; jOi, jo ^Kaiial* H.
431; damdan 'laufen H. 585; duoest 'zweihiindert' H. 586;
d^ *Damon H. 598; dtcar^ dXval *Mauer H. 599; ravan
'Seele', phi. ruvdn, zd. urvan- H. 625; zarvan 'Zeit* H. 659;
zlvajjlva 'Quecksilber H. 683; suvaw 'ich gehe' H. 778 ; buvam
'bin H. 233; sunavam 'hore* H. 795; farvar \Sommerhaus
H. 823; gav 'Rind' H. 888; guvalidan waehson* H. 939; nav
'Eanal, R5hre' H. 1024; nuvazdah neunzehn H. 1048, navad
neunzig'^) H. 1049; navardldan *zusammenwickeln' H. 1050;
havan *M5rser* H. 1089; yavar 'Stossel* H. 1125 u. s. w.
Auslautendes av wird au {ou) gesproclien : jan 'Gerste* (afgh.
jau) H. 428: nau neu' H. 1045; sau *geh*, ipt. zu savam;
--- 5970 ---
phi. zlvandak 'lebendig' Gl. and Ind. 152;
paz. pSy (lies ptg) = phi. pig oder plk Shk.
263, bal. p^g, nb. ^ty 'Fett* ans ^plvaka-; np.
pfA *Talg, Fett\ skr. ptvasd- *fett' (obenp. 46).
Dagegen zlva, jlva 'Quecksilber H. 683.
b) -ava- wird zu D : furod 'hinunter — skr. pravdta\
furosam Verkaufe' aus *fravaxsamij
yo2f 'Jagdleopard*= a,rm,yovaz, yavaz.
Vgl. auch sukDra (? neben sukurra, sukra u. s. w.)
patina testacea = arm. skavarak ^Schiisser; np. fordiydn
(neben fravardiyan), gr. Oovpiiyap = vtxvla (Menander,
vgl. § 135, 2, y), arm. hroUic^ hrort-ic (gen. pi.) ein Monats-
name (?); pron. di = ap. gen. avahya?
--- 8160 ---
§ 120. Ap. i (= idg. g^^ g^h) im Aniaut = np. j,
z und 2:
a) = np. j im N. pr. Jamasp, jamasp = phi. famdsp,
arm. jamasp (PerserkSnig, Sebeos p. 19) = zd. jamaspa-^
aber gd. dBjamaspa-, syr. Zdmasp, gr. Zafidanjjg Tab. 142;
javidan *kauen\ afgh. zOvql, ksl. zwati (Wrzl. iran. jyu^
oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
unter c).
b) ^=np. z: zadan 'schlagen' = zd. ap. jan, skr. han\
zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
jycL-; zistan 'leben', zd. skr. jiv\ zahr (oben p. 71), arm.
zahr 'Gift' = zd. *fal^ra-; zdv 'Spalt' H. 649, oben p. 68
und 70.
--- 8184 ---
p. 69; iang 'Host' = np. iang^ zang; zangar 'Griinspan =
np. zangar, zangar.
c) ^= np. z: zala 'Hagel* (aus ^zardak = arisch
*^'harda^>), siehe oben p. 72, anders Bartholomae, Studien
II, 57; zarf 'tief = zd. jiafra-; ztva --^ jiva 'Quecksilber,
arm. liptik = '^Hhak (oben p. 72), zu skr. jTva- 'lebendig.
Die Wrzl. jw 'leben' liegt also als jiv, Hv (in pva, Hva)
und zlv (in zMan) vor.
*) Bal. z = iran. z^ aber bal. j -- iran. j (Geiger, Lautlehre
p. 35 und 28) ; afgh. z oder j (inl. selten auch i) = iran. ar, aber afgh.
z oder ,/ = iran j (Geiger, Etym, und Jjautl. p, 50 und 47).— 230 -
§ 121. Ap. j, z im inlaut = np. /, z und z\
a) ap. j nach n = np. /: ahanjidan 'ziehen, phi.
```


### [2026-09-06T02:23:25.717Z] TOOL RESULT

```
lesenes hiöT (llückert, ZDMG. 8, 285, Salemann-
Shukovski, Pers. Gr. § 45 Anm.).
iünhär, zinhär s. unter np. düsten (No. 527).
*J West vergleicht hierzu das np. funbelcgto) irmäit 'llcue*.
^) Skr. Jivaha- 'lebündijj, lebhaft*; LW. arab. zifjoq , syr. 'VTi
kurd. zive^ arm. ztpak 'Quecksilber*.- 152 —
z.
684. £äle 'Hagel, Keif.
Ri.hrädünl' 'Hagel'; gr. ;faAa^a; hdt, (jranclo; ksl.
fjradü.
Nöldeke (mündliche Mitteilung). Neupersische
Grundform *zrade^ *zärde.
Diese Etymologie verdient vor der meinigen (KZ.
32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
los den Vorzug.
685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
```


## [2026-09-06T02:23:45.509Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1/v2 ژیوه ===\"; grep -n \"ژیوه\\|زیوه\\|زیبق\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20\necho \"=== incoming v3/v4 ===\"; grep -n \"ژیوه\\|زیبق\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -10",
 "description": "Grep Borhan for mercury words"
}
```


### [2026-09-06T02:23:45.650Z] TOOL RESULT

```
=== BQT v1/v2 ژیوه ===
BQT_v2_pages.txt:3590:‫وبعربی زیبق خوانند ‪ . ۵‬طبیمت آن گرم باشد‬                    ‫جیقوت بسر وزن فرتوت ت»وبره‬
BQT_v2_pages.txt:3631:     ‫ژیوه («‪.‬م‪» ).‬اورامانی ‪. 4« ۷12‬اورامان‬        ‫© =‬             ‫نود («‪.‬م‪: ).‬‬   ‫مصحف‬      ‫‪۴‬‬
BQT_v2_pages.txt:3633:         ‫وجهنده | مفح» صماب درفارسی ژیوه با ج وه نامسده شده(و زب معرب أ لت )وآناز همن صقت‬
BQT_v2_pages.txt:24231:‫برافتادن بود ‪ -‬و حم‬      ‫را نز کنته‌اند که مذرف‬                  ‫وسیماب و زیبق را بیزمیگوبند ‪ -‬وبائانی مشدد‬
BQT_v2_pages.txt:29963:‫بزبان ارباب عمل که کیمیا گرانند وعربان زیبق‬                     ‫در‬
BQT_v2_pages.txt:31325: ‫سیماب باشد و معرب آن زیبق است‌وبعربی‌فرار‬             ‫آژیر استکهآبکیر وتلاب کوویباشد کهآب‬
BQT_v2_pages.txt:40599:‫گوبند ومعرب آن زیبق باشد و جزواعظم! کسیو‬              ‫چوبهایی است که برزسگران بر دوطرف چوبی‬
=== incoming v3/v4 ===
incoming/BQT/BQT_v4_pages.txt:22032:یوسف زیبق نقاب « کنا + از بود؟ -- را 5
incoming/BQT/BQT_v3_pages.txt:50823:و بامطلاح کیمیا گران سیماب و زیبق پاك‌وصاف
```


## [2026-09-06T02:23:46.531Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"zi'baq\\|zībaq\\|zi-baq\\|zaibaq\\|Quecksilber\\|زئبق\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Grep Asbaghi for zībaq"
}
```


### [2026-09-06T02:23:46.604Z] TOOL RESULT

```
1374:Sr- äbaqg: "Quecksilber" pers. 5 aus dem pers. dr abki "flüssig, wässerig" 
8131:0,2 - Biwa: "Quecksilber" aus dem pers. „,,; Ziwa mp. „ırg Zivandak "das 
10629:LU - zäbig: "Quecksilber" pers. s,» giwa, >, ziwe ı MP. He ziwandak 
11366:"Quecksilber" pers.
```


## [2026-09-06T02:23:51.022Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor l in 8125 10620 11360; do echo \"--- $l ---\"; sed -n \"${l},$((l+14))p\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; done",
 "description": "Read Asbaghi entries"
}
```


### [2026-09-06T02:23:52.628Z] TOOL RESULT

```
--- 8125 ---
scheinlich stammt es von ou fgilän aus, aram. er . 


Ar- Bili: Nisba v. Zilän s. Zilän. 


0,2 - Biwa: "Quecksilber" aus dem pers. „,,; Ziwa mp. „ırg Zivandak "das 


Lebende" ar. c3.) zibag > 


FL 


--- 10620 ---
@r, - rIn: "Schmutz" = rim q. v. 


>») - riwand = rawand q. v. 


tm 


LU - zäbig: "Quecksilber" pers. s,» giwa, >, ziwe ı MP. He ziwandak 
"das Lebende" « 


oUL-LE - zäbulistän: "eine Provinz im Osten des Irans" —T MP. yyendıys 

--- 11360 ---
O9 - zaitün: 


zarfin q. v. 


"Quecksilber" pers. 


"quecksilbern" 3, 


jiL4 , hebr. nır.
```


## [2026-09-06T02:24:01.906Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['PLA'],ensure_ascii=False,indent=1))\"\necho \"=== find page tag near zabiq ===\"\ngrep -n \"pdf page\" incoming/PLA/PLA_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace')\nlines=t.readlines()\nlast=None\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: last=m.group(1)\n    if 'zäbig' in l or 'zibag' in l or 'ziwandak' in l:\n        print(last, i, l.strip()[:160])\nEOF",
 "description": "Find PLA page for zībaq"
}
```


### [2026-09-06T02:24:03.855Z] TOOL RESULT

```
{
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
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "first_printed": 1,
   "last_printed": 300,
   "pdf_offset": 0,
   "lang": "deu+ara"
  }
 ],
 "cites": "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
}
=== find page tag near zabiq ===
None 5957 Lebende"            ar. c3.) zibag               >
None 7981 LU        -       zäbig:           "Quecksilber"                        pers.     s,»      giwa,     >,    ziwe     ı      MP. He     ziwandak
None 8000 &>-           zibuf:              "Richtblei"              pers.        65.      zäbig.
None 8583 So) - zibag:            "Quecksilber"             pers.        2 aus     pers. o„>            Biwe TI mp. ons ziwandak.
None 8586 SF - zibagi:                  "quecksilbern"             3,
```


## [2026-09-06T02:24:09.648Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\npython3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor target in ('So) - zibag','LU        -       zäbig','Biwa: \"Quecksilber\"'):\n    idx=[i for i,l in enumerate(lines) if target in l]\n    for i in idx:\n        pre='\\n'.join(lines[:i])\n        leaf=pre.count('\\f')+1\n        print(target,'| line',i,'leaf',leaf,'printed page',leaf-15)\nEOF",
 "description": "Compute PLA printed pages"
}
```


### [2026-09-06T02:24:11.385Z] TOOL RESULT

```
So) - zibag | line 8583 leaf 166 printed page 151
LU        -       zäbig | line 7981 leaf 155 printed page 140
```


## [2026-09-06T02:24:17.916Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA\npython3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=5957\nleaf=('\\n'.join(lines[:i])).count('\\f')+1\nprint('leaf',leaf,'printed',leaf-15)\nprint('\\n'.join(lines[5950:5962]))\nEOF",
 "description": "Locate Ziwa entry page"
}
```


### [2026-09-06T02:24:19.742Z] TOOL RESULT

```
leaf 117 printed 102
       scheinlich               stammt          es von       ou fgilän                 aus,     aram.      er              .


Ar-         Bili:        Nisba        v.       Zilän    s.    Zilän.


0,2 -         Biwa:      "Quecksilber"                 aus    dem pers.                „,,; Ziwa        mp. „ırg           Zivandak           "das
       Lebende"            ar. c3.) zibag               >


                                                                         FL
```


## [2026-09-06T02:24:28.540Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"کیومرث\\|گیومرث\" BQT_v4_pages.txt | head -10\necho \"=== گیتی ===\"; grep -n \"گیتی\" BQT_v4_pages.txt | head -10\necho \"=== page tags ===\"; grep -n \"pdf page\" BQT_v4_pages.txt | head -3",
 "description": "Grep Borhan v4"
}
```


### [2026-09-06T02:24:28.634Z] TOOL RESULT

```
10986:بود که کیومرث ... دیو را بکشت . و بسیارکونه کفته‌اند لکن چون درستی آن ندانم بدین
19492:از کیومرث برنخت لشته چهل‌سال‌پادشاهی کرد | خواب و بیداری که سالك را درآن(۱) فیضی از
=== گیتی ===
3770:۱۳ مععلهٌ گیتی‌فروز
3792:مشخش ۱ - بنتح ارل ونانی وسکون مشعلةٌ گیتی فر ون * - بسنیمسلة
8832:ابا ( ایا . دهخد!) خورشید سالارانگیتی سوار رزم ساز وکرد نتوه . >
18436:بدهنا.ه گیتی بباراسشست بدان نامه نام نکو خواستست
=== page tags ===
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
```


## [2026-09-06T02:24:32.343Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\"",
 "description": "Show BQT and MON ref info"
}
```


### [2026-09-06T02:24:33.810Z] TOOL RESULT

```
{
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
}
{
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
}
```


## [2026-09-06T02:24:43.882Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nd={}\nfor b in blocks:\n    m=re.search(r'\\[pdf page (\\d+)\\]',b)\n    if m: d[int(m.group(1))]=b\nfor p in range(658,674):\n    b=d.get(p,'')\n    hits=[w for w in ('گیتی','کیومرث','گیومرث','کیهان','گیهان') if w in b]\n    print(p, hits, b[:80].replace('\\n',' '))\nEOF",
 "description": "Scan BQT v3 pages for gītī/Kayūmars"
}
```


### [2026-09-06T02:24:45.653Z] TOOL RESULT

```
658 [] [pdf page 658] را  بازی کردن و خواه بز رکه باشد از برای توپ ومنجنیق ‎٩‏ - و پمعن
659 [] [pdf page 659] کون ژده  ‎OS"‏ ژ۵ه (۱) = ‎ce‏ زای‌فارسی‌ودال  ‏ابجد بروزن شورمزه 
660 [] [pdf page 660] lA  و جرم آسمان است - و کنابه از کوا کب هم هست .  گوهر ] گین ۱ - 
661 [] [pdf page 661] کرهربدن  گو هر یفن - یمنی چیزی را بچیزی عوض و بدل کردن ۰  ‎CH”‏ ب
662 [] [pdf page 662] —\ave—  ‎pe AS‏ وزن فیس » ظرف ‎sly‏ شیر و ماست را گویشد .  ‏گوی س
663 [] [pdf page 663] بیان هیجد هم  در ‎SE‏ فارسی ۳ ها ‎atts‏ بر پاتزده لغت و ‎cal‏  ۱۴
664 [] [pdf page 664] ۱۸۹۷  باشد که خدای تعالی عالم را بیافرید .  wees ‏-بروزن سمن‌زاره
665 ['گیتی'] [pdf page 665] ‎AST‏ نمناك هدوت ‎ol”‏ فهناگ » بکر ها و فتح ‎oy‏ | باشد چه کیتی ب
666 [] [pdf page 666] NAMA  واو شش ماه بر و شش ‎ole‏ ماده میباشد » وبسنی گوبند یکسال تر
667 ['کیهان'] [pdf page 667] کیسودار هرا  و مردم عامیرا کویند #۰ گیل‌دارگ * - بکس اول » چوبکی 
668 ['کیهان'] [pdf page 668] ۱ یله ۱ © بروزن حیله.نام جابی‌ومقامی  ‎Gh‏ = بر وزن فیلی » منسوب 
669 ['گیهان'] [pdf page 669] که پر او کرازه نام داشته . گیومرت؟ ه بقتح اول و الی بثالث کشیده و
670 [] [pdf page 670] از کناب ‎ob,‏ قاطع درعرف لام با عروف تهجی ‎se‏ ‏بر بیست و دو بیان
671 [] [pdf page 671] " لایدن - ۱۸۷5 دادن را هم میگویند ۱ - و چیزی ‎jth‏ گویند که از سر
672 [] [pdf page 672] و۱۸۷  ‎Oy = ‘ey‏ شاخ » بمعنی‌جای ومقام باشد لیکن بدون ت رکیب کفته
673 ['کیهان'] [pdf page 673] لادن  ان ۱ - بر وزن دادن ۰ توعی از مشمومات است نی بوی ‎oS‏ و آن ‎
```


## [2026-09-06T02:24:51.725Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nfor f in ('BQT_v3_pages.txt','BQT_v3_pages_faseng.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for b in t.split('\\f'):\n        m=re.search(r'\\[pdf page (\\d+)\\]',b)\n        if m and int(m.group(1)) in (665,669):\n            print('=====',f,m.group(1))\n            print(b[:2600])\nEOF",
 "description": "Print Borhan pages 1868 and 1872"
}
```


### [2026-09-06T02:24:53.261Z] TOOL RESULT

```
Exit code 1
===== BQT_v3_pages.txt 665
[pdf page 665]
‎AST‏ نمناك هدوت
‎ol”‏ فهناگ » بکر ها و فتح ‎oy‏ | باشد چه کیتی بمعنی جهان و نوردیدن بمعنی
بروزن ‎he‏ غمثاك » ‎coh‏ که آیرا خرفه | کردیدن است - و کنابه از آفتاب عالمتاب است-
‎le Bel 9 ge‏ و کنایه از اسکندر هم هست - و اسب را نیز

‏گیبر = بفتح اولوضم بای ایجدو. کوش
‎gh‏ و رای قرشت » لوعی زان ‎as‏ ده گیچ = بکر اول وسکون ‎BE‏ وجیم»

‎Gof ot‏ اول وفوقالی‌وسکون بمعنی پربشان ویر کنده خاطر باشد - وتخصی
‎gl‏ وتحتالی» دابا وروز کار و جهان را کویند ۴ را نیز گویند که بسیب صدحه دماغ او پریشان
- و ‎ga‏ زمین هم هست - و کلی است پسیار | شده باشد - و احمق و ابله ومتحیر و س رکنته
خوشبوی که از دربای بسرء آورید ۴ ؛ و پا نی | و حیرانرا نیز گویند ۸ ؛ و باین ممنی با جیم
مثلثه هم بنظرآمده است درموبدالفتلا . فارسی هم پنظر آمده است - وخودستای وصاحب

‏کت - ‎ae‏ عجب وتکبر را هم کفته‌اند .

‎1 ۲ Lis ‏بان * پیعتی تگاه دارند‎ oF
‏اولوفتح جیم.بسنی‎ GS = * ‏و رو زکلر است که کتابه ازپادشاه هقت اقلیم‌باشد گیچه‎
‏چه کیتی بمعنی دلیا وبان نگاهدارنده ومحافظت | کیج‌است که پربشان وپرا گند‌ومتحیروس سکشته‎
. ‏کننده را گویند‎

‏گیتی 1092 ‎ene‏ با وزای‌فارسی,
بممنی ‎bis‏ طلب وطالب دلیا باشد چهکیتی‌بمعنی
دنیاویژوه وطالب وخواهان وجوبان‌باشد- ‏ و کنابه
از پادشاه است + گیل = پکسر اول وسکون ثانی و دال
گیتی نورد ۷ - بسنی جهن کرد | ابجد. مغ کوشت‌ربارا کوبند که فلیواج‌است۱۱,

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

===== BQT_v3_pages.txt 669
[pdf page 669]
که پر او کرازه نام داشته .
گیومرت؟ ه بقتح اول و الی بثالث
کشیده ومیم مفتوح برا وتای فرشت زده؛ نخستین
کیرا کوبند که در عالم پادشاهی کرد و ‎tt‏
‏تر کیبی اين لفت زند؛ کوبا است چه کیو بمعنی
‎FS‏ ومرت بمعتی زنده‌آمده است ودر ‎he‏
‏متأخرین ‎GK‏ تلژی و ‎athe GLE‏ مشهور است
و حالآنکه اين رسم قارسی قدیم است ود رکلام
فارسی قدیم ثای مثلثه نيامده است » اله‌اعلم.

گیوه ‎gt b=‏ معروف بروزن میوه »
نام پادشاه زمین خاوران است و اوکی ازمبارزان

NAY

شاه کیخضرو بن سیاوخش بوده ۴ - و با ثانی
مجپول . نوعی از کفش ویای افزار اس تکهروی
آرا از ربمان دوزند و ته آنرا از لته سازند
‎SLT,‏ جامگی نیز گوبند .

گیه ۴ = بپور ها بروزن سیه, مخفف
کیاء باشد که علف است.

HE ‏وفتح ثانی و‎ Il SG - * AQ
‏پالف کشیده . بلفت زند ویازند(۱) گیاه وعلف را‎
. ‏گویند‎
‎. ‏گیهان ۲ © یفتح اول بروزن پیمان‎
. ‏یمعنی دنبا وروز گار وجپان باشد‎

)4( چك : ژند و پاژند .

۱ - پهلوی ‎.Gaydmart‏ اوستابی ‎Gayd_maretan‏ » بارتولمه ۵۰۳ » دنیب ‎F‏

ص ۰۸۰ . جزء اول « کیو» و«کیه © بمعنی جان و زندکی است و جزء دوم « مرتن © صفت‌است
بمعنی‌مردلی ود رگذشتنی | وبتعبیر دبگر مردم ( چون بشرفانی است » او را مردلی و در گذشتنی
نامیدماند ) « پورداود . پشتها ج ۷ ض 4۷-8۱ * . .۰ ۲ - صحیح نیست» ‎By‏ :کیو .
۴ 02۵۷6 « فپرست ولف» :
فروتر ازو ‎9S‏ رزم زن ‎Soe‏ پیروز ولشکرشکن .
فردوسی طوسی*شاهنامة بخ ج ص ۱۲۷۹ طبق ‎Pitas‏ و در متن : فزونتر ازوقارن رزم زن.
‎l= ۴‏ («م) 5 قراتی از رسم‌الخط پهلوی . ‎SNS) Ay‏

‎AST‏ ] و رك : باروچا س ۱۹۲ . ‎oles Vo‏ پپلوی 86180 ( دیا ) جمع حالت
اضافی ازاوستابی - 888002 ( ۰88612080650 ) > 5 ‎oS‏ ص ۸۰ » ‎doy‏ : اسشق -حوبشمان
‎MeN‏

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'BQT_v3_pages_faseng.txt'
```


## [2026-09-06T02:25:12.919Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nprint('nleaves',len(blocks))\nfor leaf in (66,498):\n    print('===== leaf',leaf,'printed',leaf+540,'=====')\n    print(blocks[leaf][:2200])\nEOF",
 "description": "Print Borhan vol2 pages 606 and 1038"
}
```


### [2026-09-06T02:25:14.745Z] TOOL RESULT

```
nleaves 684
===== leaf 66 printed 606 =====
  ‫‪ ۵‬ات‬   ‫مت‬
                                                                                                                ‫چاپلوی‬
 ‫جداگردیده را بکیوزبند ‪ ۵‬و آنرا بعریی صبره‬        ‫را یز کون دکه اکر‬                   ‫اسب رهواری‬               ‫و‬   ‫باشد =‬

                      ‫خوالند بضم صاد بی‌نقطه ‪.‬‬               ‫را غلط نکند ‪# ۱‬‬                     ‫راه‬
                                                                                                   ‫ننهن پدراو‬
                                                                                                            ‫ززبا‬
                                                                                                               ‫تا‬

 ‫چاچله ‪ -‬تمچی رمس وام ‪.‬کش‬
              ‫‪۶.‬‬
               ‫و بای افزار چرمی راگویند ‪٩‬‏ ‪#‬‬
                                                   ‫چاپلوس ‪ ۴۰‬بکون بای فارسی‬
                                                   ‫ولام بواومجهول کشیده و(‪ )۱‬بین بی‌اقطة زده؛‬
‫چادر ترسا = وطا وجامه ای باشدزرد‬                       ‫شخصیرا گوبند کهبچرب زبانی وسخنهای‌شیرین‬
‫و کبود درهم بافته ‪ -‬و کنابه از شفق و روشنابی‬      ‫وا بای‬
                                                       ‫و فروتئی کردن مردم را فریب دهد ؛ ب‬
                             ‫انتاب هم هت ‪.‬‬                                             ‫|جد هم آمده امت ‪.‬‬
                                                                                                       ‫ب‬

 ‫جادر کاقودی ‏ کنابه از سفیدی‬                           ‫کناوافو‪.‬‬
                                                               ‫وکو‬
                                                                 ‫‪ ۰‬چاہوك د بنم ثالث زس‬
                             ‫صبح صادق باشد ‪.‬‬                         ‫چست وچالاك وجلد راکوبند ‪. ۴‬‬
 ‫جادر کحلی = کتابه ازآسمان ‪-‬‬                       ‫‪۰‬‬    ‫بواو کشده‬     ‫با تای فرشت‬                ‫‪-‬‬     ‫جاتو‬

                         ‫وب تاريك است ‪*.‬‬
                                       ‫ش‬          ‫دزدانرا از حلق | ویزند‪.‬‬                   ‫ان‬    ‫رسمائی با‬
                                                                                        
===== leaf 498 printed 1038 =====
   ‫خر و‬                                                                    ‫زبیری‬
 ‫نزحیری د کنابه از دیوانه بادد ‪[| .‬وسخن سرابی وقصه‌خوابی‌باشد وکنابه‌ازسخنان‬
 ‫و لاطاتل‬     ‫بی لفم و بی معلی و هرزه و بیهوده‬                    ‫گ‬                                       ‫‪۰‬‬       ‫‪۰‬‬
   ‫‪۹‬‬                                                            ‫اندگان‬   ‫ر نج يان ‪ .‬کنابه از‬
 ‫گفتن و هرزه درایی کردن ‪ -‬و لاف زدن هم‬                                 ‫‪9‬‬               ‫بر‬
                                                                                             ‫باشد ‪.‬‬
                               ‫هت ؟ ‪.‬‬                                 ‫کر‬                   ‫‪۳‬‬
                                                 ‫و‬             ‫ن خای‬      ‫و ثالی و‬        ‫اول‬   ‫ر لح = بف‬
 ‫اول و سکون ثائی و دال‬            ‫» بفتح‬        ‫رلك‬              ‫‪.‬‬          ‫‪۳‬‬          ‫ِِ‬                ‫ِ‬
                                                               ‫قطه‌دار ‪ ۰‬معر ورف است وآنرا زیشدان‌هم کوبند‬
 ‫دعری‬      ‫أبجد » تامکتایی است که ابراهیم زردشت‬                                                               ‫‪1‬‬

 ‫شده است ‪۰‬‬
                      ‫ِ‬                     ‫‪۱‬‬
                ‫میکر د که از آسمان برای من ازل‬
                                                               ‫وبعربی‌ذفن خوانن‌د ‪٩‬‏ ‪ -‬و بمعنی‌مطلق سخن(‪)۱۱‬‬
  ‫‪:‬‬           ‫‪E‬‬           ‫‪ERE‬‏‬         ‫کوبند‬                       ‫ر‬
                                                                ‫هرزه‬     ‫آمده است عموما‪ .‬و سخنان بقیقحم‬
 ‫‪E‬‏‬        ‫ان‬         ‫رم‬     ‫بصعت‬                     ‫‪E‬‏‬       ‫ولاطابل ویپوده وخالی از معنی و لاف و کزاف‬
  ‫وند دونك اند اصزحف‬
                   ‫دوگ رگوبند زبنداز‬                                                              ‫‪۷‬‬   ‫انه خا‬
‫دو قسم از اقام آن ‪ - ۵‬ونام‬                  ‫عمن»ی‬
                                                ‫یاهی‬
                                                   ‫ابر‬                               ‫رت‬               ‫‏‪EE‬‬
       ‫‪۱‬‬          ‫‪۱‬‬              ‫‪9‬‬      ‫‪1‬‬             ‫‪۱‬‬        ‫ر نخ بر حون ردن = کابه ا
```


## [2026-09-06T02:25:29.065Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in (3585,3625):\n    pre='\\n'.join(lines[:target])\n    leaf=pre.count('\\f')\n    print('line',target,'leaf',leaf,'printed',leaf+540)\nblocks=t.split('\\f')\nfor leaf in (66,67,68):\n    pass\nEOF\ngrep -n \"جیوه\" BQT_v2_pages.txt | head",
 "description": "Locate jīveh entry leaf"
}
```


### [2026-09-06T02:25:30.934Z] TOOL RESULT

```
line 3585 leaf 63 printed 603
line 3625 leaf 64 printed 604
3621:                                          ‫نیزاید ‪.‬‬          ‫جیوه ‪ -‬بروزن میوه » سیماب رگاویند‬
9974:‫‌ بقتح اول وتم انی و سکون‬                ‫جیوه‬
29961:‫جیوه است‬     ‫باشد که‬       ‫‪a‬‏ بمعنی زاووق‬    ‫صماروع‬             ‫رواغار = با غین قطه‌دار (‪ )۲‬بر وزن‬
31347:                                                ‫‪۰‬‬                  ‫جیوه («م‪. ).‬‬                 ‫‏‪٩‬‬
40626:  ‫‪- ۸‬از‪ :‬سیم‪ +‬آب؛ وسیم‌خودبمعنی جیوه مده ‪:‬‬                       ‫م‪.‬‬  ‫وه»‪.‬‬‫سی« س‬
```


## [2026-09-06T02:25:35.753Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=t.split('\\f')\nfor leaf in (64,65):\n    print('===== leaf',leaf,'printed ~',leaf+540)\n    print(blocks[leaf][:3000])\nEOF",
 "description": "Print Borhan jīveh page"
}
```


### [2026-09-06T02:25:37.803Z] TOOL RESULT

```
===== leaf 64 printed ~ 604
 ‫—‬         ‫=‬

                                                                                     ‫جیغوت‬
‫وبعربی زیبق خوانند ‪ . ۵‬طبیمت آن گرم باشد‬                    ‫جیقوت بسر وزن فرتوت ت»وبره‬
‫و پسنی گوند سرد و تر است در دویم » شیش‬
                                                              ‫و سبدیرا کوبند که ازلیف خرما بافند ‪. ۱‬‬
‫جرب وحکه را نافع باشد »‬          ‫وکنه را بکشد ؛‬        ‫چيك جيك (‪ - ۴ )۱‬بکر هردوجي ‪۱‬‬
‫صعیدآن باين طربق کنندکه بتانند(‪)۲‬سیماب‬                  ‫وسکون هردوتحتالی وکاف راز اقام جانوران‬
‫ووزن‬
   ‫رآ و بالیم وزن آن قلمی داخل کنند ب‬                                                   ‫و مرعان باشف ‪.‬‬
‫هردو زاج سوخته وبوزن زاج خشت بخته‌وبوزن‬
                                                        ‫»‬    ‫جيل دارو ‪e‬‏ معرب گیل داروست‬
‫مجموع تلك بربان کرده که لآوچة کوهی باشد»‬                ‫چون شکنند‬
                                                                ‫چوبی باشد سیاه رنگ و‬
‫وهمه رادرصلابه انداخته‌باب‌تر نجوان‌میوه‌ایست‬                                                      ‫ون‬
                                                                                                    ‫آ‬
                                                            ‫مزآن فتقی بود‪ .‬منفصت آن بسیار است ‪*.‬‬
‫ممروف‪ ,‬بایندتا ليك سابیده شود » بعد از آن‬
‫اررا‬
   ‫دردیگی نوکه بگل‌اندودة باشند کرده س‬
                                                        ‫جمی ه بر وزن کین › صفات زشت را‬
‫نشد تابریان‬
          ‫نآت‬
            ‫کته‬
              ‫محکم ببنداد وآهسته آه‬                            ‫گوبند » وصوفیه تعییر ازآن بنفی کنند ‪.‬‬
                                                        ‫جیناك ی بانون بروزن يباك حای‬
‫شود ‪,‬وهمچنین تا هفت نوبت باآبتراج بسایند‬
‫در‬        ‫و در دبك کنند و بربان سازند » باعدزآن‬                                ‫و مکان و مقلم را کویند ‪۰‬‬

‫شیشه‌ای که بگل‌حکمت‌اندوده باشند کنندو آتش‬                  ‫چینه‌ود ؟ = بروزنکینه‌ور‪ .‬پل‌صراط‬
‫ارم ارم میکرده باشند تا تصعید کند » وهمچنین‬                                                    ‫رکاوشد ‪.‬‬
‫سه مرتبه تصعید کنند‪,‬تا] نکه‌مانند دانهٌ مروارید‬             ‫جیو اك = بروزن‌فرهاد‪ .‬بسشی ورع‌است‬
                                                                    ‫که پرهیز کاری وکر شپوت باشد‪.‬‬
‫سفید گردد » وآن س‌قاتل است ویکارهای دیبگر‬
                                          ‫نیزاید ‪.‬‬          ‫جیوه ‪ -‬بروزن میوه » سیماب رگاویند‬




                                        ‫(‪ )۷‬چك‪ :‬ستند (‪)۱‬‬             ‫(‪ )۱‬چك ‪ :‬جبگهجیگه (‪.‬‬

     ‫طبری ‪) - [61‬از ( موت کنجتك) «نصاب طیری‪۳۷۲‬؟ ‪.‬‬                    ‫‪۳‬‬         ‫‪ :‬جفت‪.‬‬    ‫رکه‬      ‫ˆ‬

     ‫قرائتی از كاك بهلوی )لاچ بممنى جا «بونکر*‪ »۸‬رك‪ :‬جا (حاشه)‪.‬‬                  ‫‪ _ ۴‬از‬
     ‫ژیوه («‪.‬م‪» ).‬اورامانی ‪. 4« ۷12‬اورامان‬        ‫© =‬             ‫نود («‪.‬م‪: ).‬‬   ‫مصحف‬      ‫‪۴‬‬
     ‫در اوسا ‪4۷‬ز آمده که در پهلوی ‪ 12002۷12‬شده بمعذی زنده ونز به‌عنی گردنده‬                       ‫‪.۸‬‬
         ‫وجهنده | مفح» صماب 
===== leaf 65 printed ~ 605
                                  ‫گفتار ششم‬

     ‫تبجی‬            ‫رب‬
                   ‫واف‬   ‫از کاب پرهان قاطع درحرف جیم فار‬
                       ‫حسی‬
        ‫هبتتی بربيست و دو بیان و محتوی بر ششصد و سیزده‬
                                                 ‫لف‬
                                            ‫کتنوات‬
                                            ‫بیان اول‬

                 ‫در جیم فارسی باالف مشتمل بر نود و هفت لفت و کنات‬

‫قرشت (‪ )۱‬بروزن آبادی ‪ ۰‬بان فطیر نازك باشد‬          ‫‪ #‬چاه مروف است ومشهور بجای‪۰ ۷‬‬
‫اتزپپنند وبرروی تابه‬
                   ‫سدس‬
                     ‫که خمیرآ را با‬                ‫وآن برکی است که از چين وخطا آورند و در‬
                                           ‫پر لد‬    ‫آب جوشانده مانند قهوه خورند‪ ,‬وخاصت آن‬
 ‫چا بك ‪ = ۲‬بصم بای ابجد و سکون‬                     ‫روت شراب رادف عکند ‪ .‬گوبند‬    ‫ضست‬
                                                                                   ‫مار ا‬
                                                                                       ‫بسب‬
    ‫ت‬
    ‫چو‬‫چفافبوك است که جلد‬
                       ‫کاف » مخ‬                    ‫مردم تبت ببب آنکه شراب بيار میخورند‬
‫تازبانه همآمده‬      ‫ع‪-‬‬
                   ‫نی‬ ‫ماشد‬
                         ‫یب‬‫وردف‬
                              ‫ولاك وظ‬
                                    ‫ا‬              ‫وعرب آن صا ‪۴‬‬ ‫ند م‬     ‫رشك‬
                                                                           ‫خت م‬
                                                                              ‫یقیم‬
                                                                                 ‫مرا ب‬
                                                                                     ‫آن‬
                                           ‫ات‬                                         ‫باشد ‪.‬‬

 ‫چابکی ؟ ‪ -‬بمعنی جلدی وچالاکی‬                      ‫جابانی » با بای فارسی و نای‬
                                             ‫‪aaa‬‬



                                                                    ‫‪ :‬و ٿا‪.‬‬   ‫(‪)۱‬چك‬



  ‫٭‪(- €#‬ج بکس » جیم فارسی) حرف هفتم از الفبای فارسی است ‪ .‬در زبان عرب‬
  ‫دارند ‪ .‬وآن‌گاه به ”ش‪٣‬‏ و گاه به « ز >‬     ‫وجودندارد ودر حاب جمل ماد جم آبرا سه مصوب‬

   ‫به «» » ودرتعریب ب«هص» و «ش» تبدبل کردد‬          ‫)ه‬
                                                     ‫گا‬‫ولف‬
                                                         ‫بدل شود ( رك ‪ :‬ص بح دبباچة مۇ‬
                                                              ‫مانند چغانی » صغانی و شفالی ‪.‬‬
          ‫‪ - ۴‬معرب چای «صای» و «شای» امت ‪ .‬رك ‪ :‬چای ‪.‬‬     ‫رك‪ :‬چای ‪.‬‬  ‫‪۱‬‬

   ‫؟ ‪ -‬پهلوی ‪ 60۳86‬ابرانی‌باستان‪ ۵ 26-1۳26-‬ارمنی ‪ ۰‬ع کلقا‪(8‬قابل‌انستاء‬
   ‫نرم » زرنگك) ‏ دیز ارمنیع ‪( ۳60‬شتاب) «ییبرك ‪۲٤٩‬‏ « مسینا ‪ « ۷۳۱۷‬افا ‪ ۱ :۱‬ص‪ ۹۷۲‬؛ ‪۷‬‬
  ‫ص ‪ ۱۸۱‬ورك‪ :‬چابوکه ‪« :‬منافم سفر ‪ ...‬يطناجیفه راست ‪ :‬لضتین بازر گانیکه باوجود‬
       ‫نعمت و مکنت غلامان کونیزکان دارد دلاویز وشاکردان
```


## [2026-09-06T02:26:01.067Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== zivastan variants across refs ===\"\ngrep -rn \"zivastan\\|zīvastan\\|ziwastan\\|zīwastan\" --include=*.txt . 2>/dev/null | head\necho \"=== BQT_v2 زیستن footnote ===\"\ngrep -n \"زیستن\" BQT_v2_pages.txt | head",
 "description": "Search for zivastan form"
}
```


### [2026-09-06T02:26:01.138Z] TOOL RESULT

```
=== zivastan variants across refs ===
(eval):3: no matches found: --include=*.txt
=== BQT_v2 زیستن footnote ===
29740:                                                     ‫از _‪۷‬از ( ‪ 00151۷12‬زیستن) «ریی‬             ‫‪71‬‬
30739:                                                                                  ‫خوردن‌برای زیستن و ک‬
```


## [2026-09-06T02:26:02.795Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG jyaH / ziy ===\"; grep -n \"ǰiH\\|\\*ǰiau\\|ziy-\\|ǰīw\\|jīw\\|ǰwa\" CHEUNG.txt | head -20\necho \"=== CHEUNG zīstan ===\"; grep -n \"zīstan\\|zistan\" CHEUNG.txt | head -10",
 "description": "Grep Cheung"
}
```


### [2026-09-06T02:26:02.879Z] TOOL RESULT

```
=== CHEUNG jyaH / ziy ===
14986:*NWIR: NP zistan/ziy- ‘to live’, Kurd. Ziyan/Zi-, Ard. zo/za-, Awrom. Ziwäy/-Ziw-, 
22222:Ard. süziya/süziy-, Awrom. sotáy/soc- (intr.), Fariz. -sut-/-suj- (intr.), -sujin- (tr.), 
30090:bear’, Yi. ziy-/zuy- ‘to bear a child’, Yghn. Zuta ‘child, son’ || (+ *a-) ? Wa. 
41704:zistan/ziy-, 223 
43545:süziya/süziy-, 339 
50562:ziy-/züy-, 466 
=== CHEUNG zīstan ===
14986:*NWIR: NP zistan/ziy- ‘to live’, Kurd. Ziyan/Zi-, Ard. zo/za-, Awrom. Ziwäy/-Ziw-, 
21226:BMP scstn /sazistan/ || (+ *pati-) Pres. IND. 1sg. BMP ps’cm /passazum/, 3sg. BMP ps’cyt /passazéd/, 
41704:zistan/ziy-, 223
```


## [2026-09-06T02:26:05.650Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14960,15000p' CHEUNG.txt",
 "description": "Read Cheung *jyaH entry"
}
```


### [2026-09-06T02:26:05.696Z] TOOL RESULT

```
*SOGDIAN: SSogd. ’zw-, BSogd. (’)zw-, CSogd. Zw-, MSogd. jw- ‘to live’ || (+ 
*abi-) BSogd. ‘Bz’y, MSogd. Bjy ‘to grow, add’ || (+ *a-) BSogd. ’’z’y- ‘to be born’, 
CSogd. ’Z’w- (caus.) ‘to cause to live, give life to’ || (+ *ham-) MSogd. ’nz’w ‘to 
wake up, resuscitate’ 

Pres.: IND. 15р. SSogd. ’zw’m, 3sg. BSogd. zwt, 3р1. BSogd. ’zw’nt, SUBJ. 15р. SSogd. ’zw’n, OPT. 
2sg. CSogd. Zwy, IMPV. 2pl. CSogd. Zwtt, ’z-Impf.: IND. Isg. CSogd. *Zw’zw; Pret.: tr. 3sg. CSogd. 
Zw’d’rt, Fut.: IND. 1sg. CSogd. Zwng’, 2р1. CSogd. Zwtq' || (+ *abi-) Pres.: IND. 3sg. BSogd. ’Bz’yt, 
BSogd. 'BZ'yt, dur. MSogd. Bjytskwn; Impf.: IND. 3sg. BSogd. B’zy || (+ *a-) Pres.: IND. 3sg. BSogd. 


*jaiH2 223 


"z'yt, SUBJ. 3sg. MSogd. "it ‘will be born’; Impf.: IND. 3sg. BSogd. ’’z’y; Pret.: intr. IND. 3pl. 
BSogd. "zyt'nt; Partic.: pres. CSogd. ’Z’wny ‘life-giving’; Caus.: pres. IND. 35р. CSogd. "Zwt, impf. 
IND. 35р. CSogd. mZ'w, pret. tr. 3sg. CSogd. ’Z’wd’rt || (+ *ham-) Caus.: pret./perf. IND. 3sg. MSogd. 
"nz'wt ó 'rt (MKG: 524) 

*CHORESMIAN: zyw- ‘to live, become alive’, zywy- (caus.) ‘to make alive, 
resuscitate’ = Samadi: 267 

*BACTRIAN: oo- ‘to live’, Govóóuo ‘living’ || (+ *abi-) ofGv- ‘to continue’ = S-W, 
Bact.: 193a, 173b 

*NWIR: NP zistan/ziy- ‘to live’, Kurd. Ziyan/Zi-, Ard. zo/za-, Awrom. Ziwäy/-Ziw-, 
Gur. (Kand.) Zrá/-Ziá- ‘to live, be alive’, NP zindah, Jow. dzande, Tr. Zän(da), Varz. 
jenda ‘alive, living’, Kurd. Zin ‘life’, Tr. zayaya/zay- ‘to give birth’ 

*NEIR: Yzgh. Zaw-/Zod ‘to revive after an illness’, Yghn. žu- ‘to live’, Pash. zwak, 
Zwand ‘life’ 

*MISC: Par. janó ‘alive’ 

*SANSKRIT: Jiv ‘to live’ (RV+) = EWAia I: 594 

«PIE *g"eIHs-, *e"ieH;-/*g" Hbi- ‘to live’ © LIV: 215 f. | Pok.: 467 f. 

*IE COGNATES: Lat. vivo, OCS Zivo, Lith. gyju, Latv. dzīvu ‘I live’, Toch. saw- ‘to 
live’
```


## [2026-09-06T02:26:07.367Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=29740\npre='\\n'.join(lines[:i]); leaf=pre.count('\\f')\nprint('leaf',leaf,'printed',leaf+540)\nprint('\\n'.join(lines[i-25:i+6]))\nEOF",
 "description": "Locate zistan footnote page"
}
```


### [2026-09-06T02:26:08.979Z] TOOL RESULT

```
leaf 500 printed 1040
                            ‫مگفته اند ‪.‬‬
                                                                                   ‫وبلبل باشد ‪, .‬‬
                                                                                   ‫_‬
‫رنده پیل ‪ -‬بکسر اول »یعتی فيل‬                            ‫زرندو اف ؟ = با واو » پررزن ومعنی‬

         ‫می‌نقطه ‪۰‬‬      ‫)س( چك‪:‬‬           ‫(‪)۲‬چك ‪ :‬باشند ‪.‬‬             ‫)‪ (۱‬چك ‪ :‬بای مجهول‪.‬‬

     ‫بزلددج ‪ .‬باقوت درمعجم البلدان گوبد ‪ :‬زلدنة‪.‬‬              ‫وب‬
                                                               ‫ل ؟‬
                                                                 ‫ملنجی‬
                                                                     ‫‪ ۸‬زتد‬        ‫‪ ۱‬مصحف‬

     ‫بفتح‌اول وسوم وچهارم ‪ .‬قربة بزرکی از قرای بخارا بماوراء النهر ‪ . ..‬وبدین قربه منسوب أست‬
              ‫‪ :‬زند یاف ‪.‬‬      ‫؟ ‪۴‬‏ رك‬        ‫‪3‬‬   ‫جامه‌ها مشهورست‬   ‫زندنجه» بزبادت جيم وای ¿ن‬   ‫ثاب‬
                                                                                                  ‫‪۵‬‬
     ‫از دساتیر *فرهنگ دساتیر ‪. ۹4۲‬‬                ‫‪۴‬‬        ‫در معجم الان وحدودالعالم لبامده ‪۰‬‬        ‫‪۴‬‬

                             ‫‪« 6‬زندواف مرغ هزاردستان‌بود‪ ۰‬عنصری (بلخی) گوید‪:‬‬
             ‫سرابنده‌ثان اکزلو زندواف » ‪.‬‬         ‫فزابند‌شان خویی ازچپرولاف (ناف )‬
     ‫«لفت فری ‪۳4۹٩‬‏ ‪.‬‬
                     ‫‪ - ¥‬رك‪ :‬زند ‪.‬‬          ‫« زند و اوستا ‪ . ۴‬رك‪ :‬زند » اوستا ‪.‬‬   ‫مخفف‬     ‫‪۹‬‬

  ‫‪ -‬مشق ازابرالی باستان‬         ‫‪ . ۸‬بهلوی ‪( 20012‬حی) از ‪ 12002۷1112‬بایسوند ‪3 -‬‬
              ‫زرده ‪۰‬‬           ‫۾ =‬           ‫که ‪٩۲۰‬‏ ‪.‬‬
                                                     ‫از _‪۷‬از ( ‪ 00151۷12‬زیستن) «ریی‬             ‫‪71‬‬

                      ‫و‬                  ‫‪ 1220022‬ا‬                  ‫کر‬    ‫‏‪« zîndakîh‬یبر گ‪.»۵۹۵۲‬‬

 ‫(‬     ‫اطع ‪eF‬‏‬        ‫هران‬
                         ‫( پ‬
                                                                                                  ‫‪ ۳۵‬پات‬
```


## [2026-09-06T02:26:27.555Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 750 ===\"; grep -n \"Page(s): 750\" POK_full.txt | head\necho \"=== mregh ===\"; grep -n \"mre.h-u-\\|mreghu\\|brachys\\|kurz \" POK_full.txt | grep -i \"brachy\" | head -5",
 "description": "Find Pokorny 750"
}
```


### [2026-09-06T02:26:27.632Z] TOOL RESULT

```
=== POK 750 ===
61433:Page(s): 750 
61457:Page(s): 750 
61470:Page(s): 750 
61512:Page(s): 750 
61556:Page(s): 750 
61581:Page(s): 750-751 
61591:Page(s): 750 
=== mregh ===
```


## [2026-09-06T02:26:28.726Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS ===\"; grep -n \"zīw\\|ziw\\|zīnd\\|zind\" SNS_pages.txt | head -10\necho \"=== SOD ===\"; grep -n -i \"'to live'\\|to live\" SOD_pages.txt | head -10",
 "description": "Grep SNS and SOD"
}
```


### [2026-09-06T02:26:28.814Z] TOOL RESULT

```
=== SNS ===
=== SOD ===
10404:         GcOgive life, (/cOcause to live                                   2302 >zcy>t S
37854:(to)cause to live 2288                        4752,5033,8640,8645,9519,             clothing 4067, 10602
```


## [2026-09-06T02:26:32.857Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (61433,61457,61470,61512,61556,61581,61591):\n    # find preceding Root/lemma\n    for j in range(ln-1,max(0,ln-200),-1):\n        if 'Root / lemma' in t[j]:\n            print(ln, '|', t[j].strip(), '|', t[j+2].strip() if j+2<len(t) else '')\n            break\nEOF",
 "description": "List Pokorny lemmas on page 750"
}
```


### [2026-09-06T02:26:34.491Z] TOOL RESULT

```
61433 | Root / lemma: mo[u]-lo- : mu-lo- | Meaning: root, plant
61457 | Root / lemma: moz-g-o-, moz-g-en-, mos-k-o- | 
61470 | Root / lemma: mozgho-s | Meaning: young bull
61512 | Root / lemma: md[u]-ro- : mu-ro- | Meaning: stupid, crazy
61556 | Root / lemma: mregh-m(n)o- | Meaning: brain
61581 | Root / lemma: mreghu- m/ghu- | 
61591 | Root / lemma: mrk- |
```


## [2026-09-06T02:26:37.260Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61558,61585p' POK_full.txt",
 "description": "Read Pokorny mreghu- entry"
}
```


### [2026-09-06T02:26:37.312Z] TOOL RESULT

```
Root / lemma: mreghu- m/ghu- 
Meaning: short 



Material: Prakr. muhu-, Avestan marazu-jTti-, -jva-^ (3paxupiO(; ', sogd. murzak^shox{'\ 
Maybe alb. murr/z'haw, hawthorn, thorn-apple, brier, whitethorn, short shrub' : sogd. 
murzak' short'. 

gr. ppaxu(; 'short', ppaxsa " shallow place '; in addition ppaxiwv ' upper arm ', 
comparative besides ppaaawv; 

Latin brevis (at first from Fem. *bre(x)uf) 'short', bruma ' the winter solstice, winter, 
coldness' ( *brevi-ma, *breu-ma "time of short days'); 

Maybe alb. i6'/y/r7a'hoar, rime, frost, hoarfrost' a Latin loanword. 

Goth\c gamaurgjan ^ shorten'. Old High German murgf/)' short', murgfar/lraW, 
breakable'. Old English /t?//^© 'pleasant', engl. merry. 

References: WP. II 314, WH. 1115. 
Page(s): 750-751 

Root / lemma: mrk- 
Meaning: edible root, carrot
```


## [2026-09-06T02:26:44.035Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1288\" KLN_1966.txt | head -5\necho \"=== quick ===\"; grep -n \"^quick\\|quick, adj\" KLN_1966.txt KLN_1971.txt | head -5\necho \"=== zoo/bio ===\"; grep -n \"cp. Avestan jva\\|Avestan jva\\|Av. jva\\|Avestan jvaiti\" KLN_1966.txt KLN_1971.txt | head -5",
 "description": "Grep Klein"
}
```


### [2026-09-06T02:26:44.140Z] TOOL RESULT

```
31391:1288
=== quick ===
KLN_1971.txt:48110:quick sound, twang’, xXi^etv (for *xXdty-iciv), 
KLN_1971.txt:69065:quick enough’. These words prob. derive fr. 
KLN_1971.txt:69815:quickly. Cp. daggle, dhobi. 
KLN_1971.txt:89432:quick*. Cp. eyelet, ogle and the second element 
KLN_1971.txt:94978:quickly. — ME. floteren, fr. OE. floterian, ‘to be 
=== zoo/bio ===
```


## [2026-09-06T02:26:46.595Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31380,31420p' KLN_1966.txt",
 "description": "Read Klein p.1288"
}
```


### [2026-09-06T02:26:46.676Z] TOOL RESULT

```
quern,  n.,  a  primitive  hand  mill.  —  ME.  querne, fr.  OE.  cweorn,  rel.  to  ON.  kvern,  Dan.  kvsern, Swed.  qvarn,  OFris.  quern ,  Du.  kweern,  OHG. quirn,  chwirna,  Goth,  qairnus  (in  asiluqairnus), and  cogn.  with  OI.  grava,  ‘stone  to  crush  the soma’.  Arm.  erkan,  ‘millstone’,  Lith.  girna, ‘millstone’,  girnos  (pi.),  ‘hand  mill’,  Lett. dzirnas  (pi.),  OPruss.  girnoywis  (pi.),  of  s.m., OSlav.  IrBnSvi  (pi.),  ‘mill’,  OIr.  brao,  brd,  W. breuan,  OCo.  brou,  ‘hand  mill’.
querulous,  adj.,  fretful.  —  ML.  queruldsus,  fr.  L. querulus,  ‘complaining’,  fr.  queri,  ‘to  complain’. See  quarrel,  ‘dispute’,  and  -ous.
Derivatives:  querulous-ly,  adv.,  querutous-ness, n.
query,  n.  —  Anglicized  fr.  L.  quaere,  imper.  of quaerere,  ‘to  seek,  ask’,  which  is  of  uncertain origin.  Cp.  quaere.  Cp.  also  acquire,  acquisition, conquer,  conquest,  disquisition,  exquisite,  in¬ quest,  inquire,  inquisition,  inquisitive,  perquisite, prerequisite,  quaestor,  querido,  quest,  question, request,  require,  requisite,  requisition. Derivatives:  querist,  n.  (q.v.),  query,  tr.  and  intr. v.,  query-ing-ly,  adv.
quest,  n.  —  ME.  queste,  fr.  OF.  queste  (F.  quete), prop,  ‘the  act  of  seeking’,  VL.  quaesita,  for  L. quaesita,  fern.  pp.  of  quaerere,  ‘to  seek,  ask’, used  as  a  noun.
quest,  intr.  and  tr.  v.  —  ME.  questen,  fr.  MF. quester,  fr.  OF.  queste.  See  quest,  n.
Derivative:  quest-er,  n.
question,  n.  —  ME.  questioun,  fr.  OF.  (=  F.) question,  fr.  L.  quaestionem,  acc.  of  quaestid,  ‘in¬ quiry,  question’,  fr.  quaerere  (pp.  quaesltus),  ‘to seek,  ask’.  See  query  and  cp.  words  there  referred to.  For  the  ending  see  suff.  -ion.
question,  tr.  and  intr.  v.  —  MF.  (=  F.)  question- ner,  fr.  question.  See  question,  n.
Derivatives:  question-able,  adj.,  question-abil¬ ity,  n.,question-abie-ness,  n.,question-abl-y,  adv., questionary  (q.v.),  question-er,  n.,  question-ing- ly,  adv.,  question-less,  adj.  and  adv.
questionary,  adj.,  1)  having  the  form  of  a  question ; 2)  asking  questions.  —  Late  L.  quaestionarius.
1288
fr.  L.  quaestid.  See  question,  n.,  and  adj.  suff.  -ary. questionary,  n.,  a  questionnaire.  —  Either  fr.  ML. quaestionarium,  questidndrium  (prop.  neut.  of the  Late  L.  adj.  quaestionarius,  used  as  a  noun, see  questionary,  adj.),  or  fr.  F.  questionnaire  (see next  word).
questionnaire,  n.,  a  list  of  formal  questions.  —  F., ‘list,  set  of  questions,  questionnaire’,  fr.  ques¬ tion.  See  question,  n.,  and  2nd  subst.  suff.  -ary. quetzal,  n.,  1)  name  of  a  bird  of  brilliant  plumage in  Central  America;  2)  the  monetary  unit  of Guatemala.  —  Amer.  Sp.,  fr.  Nahuatl  quetzalH, lit.  ‘tail  feather’.
queue,  n.,  1)  (her.)  the  tail  of  a  beast;  2)  plait  of hair  worn  hanging  down  behind ;  pigtail ;  3)  a line  of  persons  waiting  for  their  turn.  —  MF. (=  F.),  fr.  OF.  coe,  fr.  L.  coda,  secondary  form of  cauda,  ‘tail’.  See  caudal  and  cp.  cue,  ‘tail’. Derivative:  queue,  intr.  v. quibble,  n.,  a  petty  evasion.  —  Dimin.  of  obsol. quib,  fr.  L.  quibus,  dat.  or  abl.  pi.  of  qui,  ‘who, which',  used  frequently  in  legal  documents.  See who,  what  and  cp.  quid,  ‘essence’,  quiddity. Derivatives:  quibble,  intr.  v.,  quibbl-er,  n. quick,  adj.,  1)  living,  alive  (archaic)-,  2)  rapid, swift;  3)  prompt;  done  promptly;  4)  alert.  — ME.  quik,  quike,  ‘alive,  lively’,  fr.  OE.  ewieu, ‘living,  alive’,  rel.  to  OS.,  OFris.  quik,  ON. kvikr,  ‘living,  alive’,  Du.  kwi(e)k,  ‘lively,  bright, sprightly’,  OHG.  quec,  chec,  cheh,  MHG.  queck, kec,  ‘lively’,  G.  keck,  ‘bold’,  fr.  Teut.  *q"'iqwa-, ‘living,  alive’,  fr.  l.-E.  *gwigwos,  fr.  base  *gwei-, ‘to  live’,  whence  Goth.  *qius,  gen.  qiwis,  ‘alive’, OI.  jivdh,  ‘alive’,  jfvati,  Avestic  jvaiti,  ‘lives’, OPers.ffva-,  ‘living’,  Gk.  [3toc  (prob.  for  *(3ifoi;, fr.  I.-E.  *gwiwos),  ‘life,Jhe  course  of  life’,  £ijv (fr.  I.-E.  *gwie-),  ‘to  live’,  dorr,,  ‘life’,  L.  vivus, (for  *gwiwos),  ‘living’,  vivo,  there  (for  *gwiwd), ‘to  live’,  vita  (for  *gwiwita),  ‘life’,  OSlav.  iivo, liti,  ‘to  live’,  iivu,  ‘alive’,  iivotu,  ‘life’,  Lith. gyvas,  ‘living,  alive’,  gyratd  '(eternal)  life’,  OIr. biu,  beo,  W.,  Co.  byw,  Bret,  beo,  ‘alive’,  OIr. beothu,  bethu  (for  *biwotut-),  ‘life’,  biad,  'means of  life’,  OIr.  bith,  W.  byd,  'world',  Toch.  A  fol, B  caul,  ‘life’,  A  sofi,  B  saigfe,  'people'  (lit.  ‘the living  ones’),  B  faya/p, ‘he  lives’,  Arm.  keam((ot *gwiya),  ‘I  live’.  Hitt,  huish-  is  not  cognate.  Cp. quitch.Cp.  also  bio-, hygiene,  jiva,  vital  and  words there  referred  to.  Cp.  also  zodiac,  zoetic,  zoo- and  the  second  element  in  usquebaugh,  whisky. Derivatives:  quick,  adv.  and  n..  quick-en,  tr.  and intr.  v.,  quick-ly,  adv.,  quick-ness,  n. quick,  tr.  and  intr.  v.  —  ME.  quiken,  fr.  OE.
cwician,  fr.  ewieu,  ‘living,  alive'.  See  quick,  adj. quicksilver,  n.  —  ME.  quiksilver,  fr.  OE.  cwicseol- for,  lit.  ‘quick  (i.e.  living)  silver’,  loan  transla¬ tion  of  L.  argentum  vivum,  ‘mercury’,  whence also  MDu.  quicsilver  (Du.  kwikzilver),  OHG. quecsilbar  (MHG.,  G.  quecksUber)  and  It.  ur¬ ge  nto  vivo,  F.  vif-argent.  See  quick  and  silver. Derivatives:  quicksilver,  tr.  v.,  quicksilver-ing, n.,  quicksilver-y,  adj.
quid,  n.,  for  chewing.  —  ME.  quide,  ‘cud’,  fr.  OE. ewidu.  See  cud.
Derivative:  quid,  tr.  and  intr.  v.,  quidd-er,  n. quid,  n.,  essence,  quiddity.  —  L.,  ‘what,  some¬ thing,  anything’,  neut.  of  quis,  ‘who’,  cogn.  with OE.  hwa,  ‘who’,  hwiet,  ‘what’.  See  who,  what, and  cp.  quibble,  quiddity,  quiddle,  quip, quid,  n.,  pound  sterling,  sovereign  (Brit.  Slang).
—  Of  uncertain  origin;  possibly  fr.  L.  quid, ‘what,  something,  anything’.  See  quid,  ‘essence’.
quiddity,  n.,  1)  the  essence  of  a  thing;  2)  quibble.
—  ML.  quidditas,  lit.  ‘whatness’,  formed  fr.  L. quid,  ‘what',  on  analogy  of  qualitas,  ‘quality’. See  quid,  ‘essence’,  and  -ity  and  cp.  quiddle.
quiddle,  intr.  v.,  to  trifle.  —  Prob.  formed  fr. quid,  ‘essence,  quiddity’,  on  analogy  of  verbs like  piddle,  twiddle,  etc.
Derivative:  quiddl-er,  n.
quid  pro  quo,  something  for  something.  —  Latin.
See  quid,  ‘essence,  quiddity’,  and  pro-, quiesce,  intr.  v.,  to  become  quiet.  —  L.  quiescere, ‘to  rest,  repose',  an  inchoative  verb  formed  fr. quies,  gen.  quietis,  ‘rest’.  See  quiet,  n.  and  -esce and  cp.  acquiesce.
quiescence,  quiescency,  n.  — -  Late  L.  quiescentia, fr.  L.  quiescens,  gen.  -entis.  See  next  word  and -ce,  resp.  -cy.
quiescent,  adj.,  quiet,  still.  — •  L.  quiescens,  gen. -entis,  pres.  part,  of  quiescere,  ‘to  rest,  repose’. See  quiesce  and  -ent.
Derivative:  quiescent-ly,  adv. quiet,  n.  —  ME.,  fr.  L.  quies,  gen.  quietis,  ‘rest, repose,  quiet’,  fr.  I.-E.  base  *qweye-,  *qwi(y)e-, ‘to  rest,  repose,  be  comfortable’,  whence  also the  second  element  in  L.  tranquillus  (for  *trans- quilnos),  ‘quiet,  still’,  and  Goth.  Iveila,  OE. hwil,  ‘space  of  time’.  See  while  and  cp.  acquiesce, acquit,  coy,  quiet,  adj.,  quietus,  quite,  quittance, acquiesce,  acquit,  requiem,  tranquil, quiet,  adj.  —  Fr.  L.  quietus,  'calm,  at  rest’,  fr. quies,  gen.  quietis,  ‘rest’.  See  quiet,  n. Derivatives:  quiet-en,  tr.  and  intr.  v.,  quiet-ly, adv.,  quiet-ness,  n.
quiet,  tr.  v.,  to  cause  to  be  quiet;  intr.  v.,  to  be¬ come  quiet.  —  L.  quietare,  ‘to  quiet,  calm',  fr. L.  quies,  gen.  quietis.  See  quiet,  n.
Derivative:  quiet-ive,  adj. quietism,  n.,  a  religious  movement  based  on mysticism,  founded  by  Molinos  (1640-97),  a Spanish  priest,  in  Rome.  —  It.  quietismo,  lit. ‘passiveness",  fr.  quieto,  ‘calm,  at  rest’,  fr.  L. quietus.  See  quiet,  adj.,  and  -ism. quietist,  n.,  an  adherent  of  quietism.  —  See  prec. word  and  -ist.
Derivative:  quietist-ic,  adj. quietude,  n.,  quietness.  —  MF.  (=  F.)  quietude, fr.  Late  L.  quietudd,  ‘quietude’,  fr.  L.  quietus. See  quiet,  adj.,  and  -ude. quietus,  n.,  final  acquittance;  death.  —  Fr.  ML. phrase  quietus  est,  ‘he  is  quit',  fr.  L.  quietus.  See quiet,  adj.
quill,  n.,  the  hollow  stem  of  a  feather.  —  ME.
quil,  rel.  to  LG.  quiele,  MHG.  kil,  G.  Kiel ;  of unknown  origin.
Derivatives:  quill,  tr.  v.,  to  fold  into  rolls  re¬ sembling  a  quill,  quill-ed,  adj.,  quill-er,  n.,  qui til¬ ing,  n.
quillet,  n.,  a  quibble  (archaic).  —  Prob.  a  corrup¬ tion  of  L.  quidlibet,  ‘what  you  please’,  fr.  quid, ‘what’  (see  quid,  ‘essence’)  and  libet,  ‘it  pleases’. See  libidinous  and  cp.  quodlibet. quilt,  n.,  padded  or  lined  bed  covering.  —  ME. quilte,  fr.  OF.  coilte,  cuilte,  ‘quilt,  mattress’,  fr. L.  culcita,  ‘a  sack  filled  with  feathers,  wool,  etc., mattress,  bolster’,  which  is  perh.  cogn.  with  OI. kurcah,  ‘bunch,  tuft  of  grass’.  Cp.  counterpane, coutil,  cushion,  quoit.
Derivatives:  quilt,  tr.  v.,  quilt-ed,  adj.,  quilt-er, n.,  quilt-ing,  n.
quin-,  form  of  quino-  before  a  vowel, quinary,  adj.,  arranged  in  fives.  —  L.  quinarius, ‘consisting  of  five,  containing  five’,  fr.  quini,  ‘five each’,  which  is  rel.  to  quinque,  ‘five’.  See  quinque- and  adj.  suff.  -ary.
quinate,  adj.,  composed  of  five  leaflets  (bot.)  — Formed  with  adj.  suff.  -ate  fr.  L.  quini,  'five each’.  See  prec.  word.
quinate,  n.,  quinic  acid  (chem.)  —  Formed  with chem.  suff.  -ate  fr.  Sp.  quina.  See  quinine, quince,  n.  —  ME.  quynce,  pi.  of  quyne ,  quine,  fr. OF.  cooin,  coin  (F.  coing),  fr.  VL.  codoneum,  fr. L.  cotoneum  (scil.  malum),  a  collateral  form  of cydonium  (malum),  fr.  Gk.  xuSclmov  |zaXov (lit.  ‘apple  of  Cydonia’),  popular  transformation of  xu86p.aXov,  ‘quince’.  This  latter  word  was interpreted  as  a  compound  xuSo-jxxXov  and  its first elementassociatedwithKoSrovia,  a  town  on the  north  coast  of  Crete,  as  if  xuSouaXov meant  ‘apple  of  Cydonia’.  In  reality,  however, xu86p .aXov  is  a  loan  word  from  an  ancient  lan¬ guage  of  Asia  Minor  and  was  brought  from Greece  to  Italy  through  the  medium  of  the Etruscans.  Cp.  Kutuviov,  a  town  in  Lydia,  lit. ‘Quince  Town’,  It.  cotogno,  OProven?.  codonh, Catal.  codony,  OHG.  quitina  (MHG.  quiten,  G. Quitte),  ‘quince’,  which  are  all  borrowed  ult.  fr. Gk.  xu86[zxXov.  Cp.  Cotoneaster,  Cydonia,  and the  second  element  in  melocoton. quincentenary,  adj.,  pertaining  to  five  hundred years;  n.,  a  five-hundredth  anniversary.  —  Ir¬ regular  formation  fr.  L.  quinque,  ‘five’  (see  quin¬ que-)  and  centenary,  ‘a  period  of  a  hundred years’.  Cp.  quingentenary. quincuncial,  adj.,  of  the  form  of  a  quincunx.  —  L. quincuncidlis,  fr.  quincunx,  gen.  quincuncis.  See next  word  and  adj.  suff.  -al. quincunx,  n.,  an  arrangement  of  five  objects  so that  one  is  at  each  corner  of  a  square  and  one  in the  middle.  —  L.  quincunx,  gen.  quinquncis,  ‘five twelfths',  abbreviation  of  *quinqu(e)-uncis,  ‘five twelfths’,  fr.  quinque,  ‘five’,  and  uncia,  ‘ounce’. See  quinque-,  ounce,  ‘a  weight’,  and  cp.  uncia. quinetum,  n.,  a  mixture  of  alkaloids  from  the  bark of  red  cinchona  (pharm .)  —  Coined  by  the
quingentenary
Dutch  scientist  Dr.  De  Vrij  fr.  quin-  and  L. -etum,  a  sulT.  denoting  a  group  of  plants,  as  in arboretum,  ‘a  place  grown  with  trees’  (see  arbo¬ retum ).
```


## [2026-09-06T02:26:54.963Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gwei-\\|gwi-wo-\\|gwiwo\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins for gwei-"
}
```


### [2026-09-06T02:26:55.066Z] TOOL RESULT

```
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
```


## [2026-09-06T02:27:07.895Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T02:27:07.941Z] TOOL RESULT

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-06T02:27:15.111Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%AC%DB%8C%D9%88%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%88%D9%85%D8%B1%D8%AB\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%DB%8C%D8%AA%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D8%AC%D9%87%D8%A7%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 205, root Gwei: Persian outcomes (jiveh, zirak, Kayumars, giti, jahan)\"\ndone",
 "description": "Archive Wiktionary Persian pages"
}
```


### [2026-09-06T02:27:21.498Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7691c57653540166.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d02d6622d11cfc9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/044e2fe758196320.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96273060a788192d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9d2f873f1e1c8d6.txt
```


## [2026-09-06T02:27:24.988Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 7691c57653540166 2d02d6622d11cfc9 044e2fe758196320 96273060a788192d d9d2f873f1e1c8d6; do\necho \"##### $f\"; grep -n -A14 -i \"Etymology\" $f.txt | head -50; done",
 "description": "Read etymologies from archived pages"
}
```


### [2026-09-06T02:27:26.588Z] TOOL RESULT

```
##### 7691c57653540166
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
75-
76- 2 
--
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Noun 
92-
93- 2.4.1 
94- Descendants 
95-
96- Toggle the table of contents 
97-
98- جیوه 
99-
--
168: Etymology
169- [ edit ] 
170-
171- Borrowed from Classical Persian جِیوَه ( jīwa , “ mercury ” ) .
172-
173- Noun
174- [ edit ] 
175-
176- جیوه • ( cive, cıva ) 
177-
178- mercury , quicksilver 
179- Synonym: سیماب ( simab ) 
180-
181- Derived terms
182- [ edit ] 
--
238: Etymology
239- [ edit ] 
##### 2d02d6622d11cfc9
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Descendants 
72-
73- Toggle the table of contents 
74-
75- زیرک 
76-
--
142: Etymology
143- [ edit ] 
144-
145- Inherited from Middle Persian [Book Pahlavi needed] ( zylk /⁠zīrak⁠/ ) (Manichaean Middle Persian 𐫉𐫏𐫡 ( zyr ) ).
146-
147- Pronunciation
148- [ edit ] 
149-
150- ( Classical Persian ) IPA ( key ) : /ziː.ˈrak/ 
151-
152- ( Dari, formal ) IPA ( key ) : [ziː.ɾák] 
153-
154- ( Dari, formal ) IPA ( key ) : [ziː.ɾák] 
155- ( Kabuli ) IPA ( key ) : [ziː.ɾák] 
156-
##### 044e2fe758196320
##### 96273060a788192d
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.5 
74- Proper noun 
75-
76- 1.6 
77- References 
78-
79- Toggle the table of contents 
--
157: Etymology
158- [ edit ] 
159-
160- From Middle Persian gytyḵ ( gētīg , “ the material world; worldly ” ) .
161-
162- Pronunciation
163- [ edit ] 
164-
165- ( Classical Persian ) IPA ( key ) : /ɡeː.ˈtiː/ 
166-
167- ( Dari, formal ) IPA ( key ) : [ɡiː.t̪ʰíː] , [ɡäj.t̪ʰíː] 
168-
169- ( Dari, formal ) IPA ( key ) : [ɡiː.t̪ʰíː] , [ɡäj.t̪ʰíː] 
170- ( Kabuli ) IPA ( key ) : [ɡiː.t̪ʰíː] , [ɡäj.t̪ʰíː] 
171-
##### d9d2f873f1e1c8d6
70: Etymology 
71-
72- 2.2 
73- Noun 
74-
75- 2.2.1 
76- Related terms 
77-
78- 2.2.2 
79- Descendants 
80-
81- 2.3 
82- Proper noun 
83-
84- 2.3.1 
--
93: Etymology 1 
94-
95- 3.1.1 
96- Pronunciation 
97-
98- 3.1.2 
99- Noun 
100-
101- 3.1.2.1 
102- Alternative forms 
103-
104- 3.1.2.2 
105- Derived terms 
106-
107- 3.1.2.3 
--
117: Etymology 2 
118-
119- 3.2.1 
120- Pronunciation 
121-
122- 3.2.2 
123- Adjective 
124-
125- 3.3 
126- References 
127-
128- Toggle the table of contents 
129-
130- جهان 
131-
--
219: Etymology
220- [ edit ]
```


## [2026-09-06T02:27:29.940Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### jiveh persian section\"; sed -n '230,270p' 7691c57653540166.txt\necho \"### jahan persian\"; sed -n '215,265p' d9d2f873f1e1c8d6.txt",
 "description": "Read Persian sections"
}
```


### [2026-09-06T02:27:30.023Z] TOOL RESULT

```
### jiveh persian section

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 ژیوه ( žive ) 

 Etymology
 [ edit ] 

 From a hypothetical Middle Persian [script needed] ( zywk' /⁠*zīwag⁠/ , “ mercury ” ) , whence also Classical Syriac ܙܝܘܓ ( zīwag ) . From Middle Persian [script needed] ( zy(w)ndk' /⁠zīndag, zīwandāg, zībandāg⁠/ , “ living ” ) , from [script needed] ( zyw /⁠*zīwa-,*zība-⁠/ , “ live ” ) , from Old Persian 𐎪𐎡𐎺 ( ji-i-v /⁠jīva⁠/ ) , from Proto-Indo-European *gʷih₃wós . Compare semantically Latin argentum vivum, Serbo-Croatian živa and English quick and quicksilver . Compare the Iranian borrowings: Old Armenian սնդիկ ( sndik ) , Arabic زِئْبَق ( ziʔbaq , “ mercury ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /d͡ʒiː.ˈwa/ 

 ( Dari, formal ) IPA ( key ) : [d͡ʒiː.wá] 

 ( Dari, formal ) IPA ( key ) : [d͡ʒiː.wá] 
 ( Kabuli ) IPA ( key ) : [d͡ʒiː.wá] 

 ( Hazaragi ) IPA ( key ) : [d͡ʒi.wá] 

 ( Iran, formal ) IPA ( key ) : [d͡ʒiː.vé] 

 ( Tajik, formal ) IPA ( key ) : [d͡ʒi.vá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 jīwa

 Dari reading ? 

 jīwa

### jahan persian

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian جهان ( jahān ) .

 Noun
 [ edit ] 

 جهان • ( cihan ) 

 world 
 16th ce. , Kânûnî Sultan Süleyman , Muhibbi : خلق ایچره معتبر بر نسنه یوق دولت كبی . اولمیه دولت جهاندہ بر نفس صحت كبی Halk içre muʿteber bir nesne yok devlet gibî. Olmaya devlet cihân da bir nefes sıhhat gibî. Among people, nothing is respected like prosperity; yet in this world , no prosperity is worth a single breath of health 

 universe 

 Related terms
 [ edit ] 

 جهان‌نما ( cihan-numa ) 

 Descendants
 [ edit ] 

 Turkish: cihan 

 Proper noun
 [ edit ] 

 جهان • ( cihan ) 

 a male given name , Jahan , from Persian 

 Descendants
 [ edit ] 

 Turkish: Cihan 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [script needed] ( gyhʾn' /⁠gēhān⁠/ , “ worldly creatures; world ” ) , [ 1 ] from Old Persian *gaiθānām genitive plural of *gaiθā , from Proto-Iranian *gayθaH ( “ life, means of subsistence ” ) . [ 2 ] Equivalent to [Book Pahlavi needed] ( gyẖ /⁠gēh⁠/ ) +‎ [Book Pahlavi needed] ( ʾn /⁠-ān⁠/ ) . [ 3 ] Doublet of کیهان ( kayhān ) .

 Pronunciation
 [ edit ]
```


## [2026-09-06T02:27:42.252Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -30 044e2fe758196320.txt",
 "description": "Check Kayumars page"
}
```


### [2026-09-06T02:27:42.314Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%88%D9%85%D8%B1%D8%AB
FETCHED: 2026-09-06T02:27:20Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T02:27:45.853Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%DA%98%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-\" \\\n \"https://www.etymonline.com/word/vitamin\" \\\n \"https://www.etymonline.com/word/microbe\" \\\n \"https://www.etymonline.com/word/zodiac\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 205, root Gwei: azir; PIE root page; vitamin/microbe/zodiac chains\"\ndone",
 "description": "Archive more sources"
}
```


### [2026-09-06T02:27:50.758Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/39c736d684184612.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/11a8a29828871f6e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f275f830b52b41f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35e75158f5fb6534.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de8e260d885636b6.txt
```


## [2026-09-06T02:27:54.012Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"### AZIR\"; grep -n -A8 \"Etymology\" 39c736d684184612.txt | sed -n '1,60p' | tail -30\necho \"### PIE\"; grep -n -B2 -A25 \"Root\\b\" 11a8a29828871f6e.txt | sed -n '1,60p'",
 "description": "Read āžīr and PIE pages"
}
```


### [2026-09-06T02:27:54.085Z] TOOL RESULT

```
### AZIR
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.4 
--
141: Etymology
142- [ edit ] 
143-
144- Borrowed from Avestan , etymologically related to زیرک ( zīrak , “ clever ” ) and چیره ( čēra , “ dominant , victorious ” ) .
145-
146- Pronunciation
147- [ edit ] 
148-
149- ( Classical Persian ) IPA ( key ) : /ʔaː.ˈʒiːr/ 
### PIE
60-
61- 1.1 
62: Root 
63-
64- 1.1.1 
65- Alternative reconstructions 
66-
67- 1.1.2 
68- Derived terms 
69-
70- 1.2 
71- References 
72-
73- Toggle the table of contents 
74-
75- Reconstruction:Proto-Indo-European/ gʷeyh₃- 
76-
77- Add languages 
78-
79- Reconstruction 
80-
81- Discussion 
82-
83- English 
84-
85- Read 
86-
87- Edit 
--
132- [ edit ] 
133-
134: Root
135- [ edit ] 
136-
137- *gʷeyh₃- [ 1 ] 
138-
139- to live 
140- Antonym: *mer- 
141-
142- Alternative reconstructions
143- [ edit ] 
144-
145- *gʷyeh₃- [ 2 ] [ 3 ] 
146-
147- Derived terms
148- [ edit ] 
149-
150- Terms derived from the Proto-Indo-European root *gʷeyh₃- (105 c, 0 e) 
151-
152- *gʷéyh₃-ti ~ *gʷih₃-énti ( athematic root present ) 
153- Proto-Hellenic: *gʷéyomai ( subj. ) 
154- Epic Greek: βείομαι ( beíomai ) , βέομαι ( béomai , future verb of βιόω ( bióō ) ) 
155-
156- *gʷoyh₃-éye-ti ( causative ) 
157- Proto-Balto-Slavic: *gájīˀtei 
158- Proto-Slavic: *gojìti ( see there for further descendants )
159-
```


## [2026-09-06T02:27:59.117Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 6f275f830b52b41f 35e75158f5fb6534 de8e260d885636b6; do echo \"##### $f\"; sed -n '1,10p' $f.txt; grep -n -i -m1 -A12 \"vitamin (n\\|microbe (n\\|zodiac (n\" $f.txt; done",
 "description": "Read etymonline entries"
}
```


### [2026-09-06T02:28:02.886Z] TOOL RESULT

```
##### 6f275f830b52b41f
URL: https://www.etymonline.com/word/vitamin
FETCHED: 2026-09-06T02:27:49Z
STATUS: 200
TITLE: Vitamin - Etymology, Origin & Meaning

Vitamin - Etymology, Origin & Meaning 

 Search 
 Log in 

23: vitamin (n.) 
24-
25- 1920, originally vitamine (1912) coined by Polish biochemist Casimir Funk (1884-1967), from Latin vita "life" (see vita ) + amine , because they were thought to contain amino acids. Related: Vitaminic .
26-
27- The terminal -e formally was stripped off when scientists learned the true nature of the substance; -in was acceptable because it was used for neutral substances of undefined composition. The lettering system of nomenclature ( Vitamin A, B, C, etc.) was introduced at the same time (1920).
28- also from 1920 
29-
30- Entries linking to vitamin 
31-
32- amine (n.) 
33-
34- "compound in which one of the hydrogen atoms of ammonia is replaced by a hydrocarbon radical," 1863, from ammonia + chemical suffix -ine (2).
35-
##### 35e75158f5fb6534
URL: https://www.etymonline.com/word/microbe
FETCHED: 2026-09-06T02:27:50Z
STATUS: 200
TITLE: Microbe - Etymology, Origin & Meaning

Microbe - Etymology, Origin & Meaning 

 Search 
 Log in 

23: microbe (n.) 
24-
25- popular name for a bacterium or other extremely small living being, 1878, from French microbe , "badly coined ... by Sédillot" [Weekley] in 1878 from Latinized form of Greek mikros "small" (see micro- ) + bios "life" (from PIE root *gwei- "to live"). Intended to mean literally "a small living being," the use of bios is incorrect, as in modern science generally (see bio- ); in Greek the compound would mean "short-lived."
26- also from 1878 
27-
28- Entries linking to microbe 
29-
30- microbial (adj.) 
31-
32- "of or pertaining to microbes," 1879, from Modern Latin microbion (see microbe ) + -al (1).
33-
34- bio- 
35-
##### de8e260d885636b6
URL: https://www.etymonline.com/word/zodiac
FETCHED: 2026-09-06T02:27:50Z
STATUS: 200
TITLE: Zodiac - Etymology, Origin & Meaning

Zodiac - Etymology, Origin & Meaning 

 Search 
 Log in 

23: zodiac (n.) 
24-
25- "belt of constellations around the ecliptic," within which the planets move, late 14c., zodiak , from Old French zodiaque and directly from Latin zodiacus "zodiac," from Greek z ō diakos (kyklos) "zodiac (circle)," literally "circle of little animals," from z ō idion , "sign of the zodiac, sculptured figure of an animal," diminutive of z ō ion "animal" (from PIE root *gwei- "to live").
26-
27- Libra is not an animal, but it was not a zodiac constellation to the Greeks, who reckoned 11 but counted Scorpio and its claws (including what is now Libra) as a "double constellation." Libra was figured back in by the Romans.
28-
29- In Old English the zodiac was twelf tacna "the twelve signs," and in Middle English also Our Ladye's Waye and the Girdle of the Sky .
30- also from late 14c. 
31-
32- Entries linking to zodiac 
33-
34- zodiacal (adj.) 
35-
```


## [2026-09-06T02:28:16.942Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== زیبق ===\"; grep -n \"زیبق\" MON_part1.txt MON_part2.txt | head -5\necho \"=== میکرب / میکروب ===\"; grep -n \"میکرب\\|میکروب\" MON_part1.txt MON_part2.txt | head -5\necho \"=== ویتامین ===\"; grep -n \"ویتامین\" MON_part1.txt MON_part2.txt | head -5\necho \"=== ژیوه/جیوه ===\"; grep -n \"ژیوه\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in 2-vol text"
}
```


### [2026-09-06T02:28:17.072Z] TOOL RESULT

```
=== زیبق ===
MON_part2.txt:54257:مرکور: کتامههه (.) جیوه» زیبق. ضصح. 
MON_part2.txt:62922:(زیبق) مقتول: جیوه‌ای که آن را به وسیلة 
MON_part1.txt:21296:و جبروت. بحر دمان زیبق عمل: ( کد.) ابری 
MON_part1.txt:49349:جیوه: (1۷4)6 [- ژیوه > زیبق» معر.] (.) 
=== میکرب / میکروب ===
MON_part1.txt:4095:آزمایشگاه‌ها برای کشت میکرب‌ها بکار 
MON_part1.txt:4838:اور ادرار به وسیلةٌ میکرب مخصوص و نیز 
MON_part1.txt:11780:میکرب‌ها را نابود می‌کند و در تداوی بعضی 
MON_part1.txt:11870:وسایل علمی میکرب‌های وی کشته شده 
MON_part1.txt:24869:میکرب‌ها مخلوطند و در امراض عفونی 
=== ویتامین ===
MON_part1.txt:12902:بر اثر فقدان ویتامین ث در بدن پیدا شود. و 
MON_part1.txt:28709:علاوه بر بد رنگ شدن ویتامین‌های خود را 
MON_part1.txt:30025:ذخیره‌ای و ویتامین و اسیدی و آبدار قرار 
MON_part1.txt:33897:ک وگردی و ویتامین‌های مختلف و بکث قند 
MON_part1.txt:65853:ویتامین د () و کمبود املاح کلسیم در بدن 
=== ژیوه/جیوه ===
MON_part1.txt:49349:جیوه: (1۷4)6 [- ژیوه > زیبق» معر.] (.)
```


## [2026-09-06T02:28:22.382Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ویتامین\\|ویتامین:\\|میکرب:\\|میکروب:\" MON_part1.txt MON_part2.txt | head -10\necho \"---\"\ngrep -n \"ویتامین\" MON_part2.txt | head -10",
 "description": "Find Mo'in headwords"
}
```


### [2026-09-06T02:28:22.460Z] TOOL RESULT

```
MON_part1.txt:65853:ویتامین د () و کمبود املاح کلسیم در بدن 
MON_part2.txt:8534:ویتامین‌های ,3و ,3و ) همراه با اسید 
MON_part2.txt:22475:ویتامین ۸) به منظور حفظ طروات پوست 
MON_part2.txt:70425:میکرب: ۵ (.) (بز.) هر یک از 
MON_part2.txt:87635:ویتامین: مأصقآ۷ (.) (بز.) ماده‌ای که به 
MON_part2.txt:87645:ویتامین‌ها: 2-م1ه)[۷ [ج. ویتامین | (امر.) 
MON_part2.txt:87669:ویتامین عامل نمو بدن و عامل ضد خشکی 
MON_part2.txt:87671:ویتامین در نسزد انسان ابتدا منجر به 
MON_part2.txt:87677:ویتامین ۸ در بدن سبب کم شدن گلبول‌های 
MON_part2.txt:87704:ویتامین ۸ و در روغن نارگیل به تنهایی یافت 
---
8534:ویتامین‌های ,3و ,3و ) همراه با اسید 
22474:دارای ویتامین‌های مسختلف (خصوصاً 
22475:ویتامین ۸) به منظور حفظ طروات پوست 
87635:ویتامین: مأصقآ۷ (.) (بز.) ماده‌ای که به 
87640:ساختن ویتامین نیست» علیهذا بایستی از 
87642:امراض ناشی از فقدان ویتامین را آویتامینوز 
87645:ویتامین‌ها: 2-م1ه)[۷ [ج. ویتامین | (امر.) 
87667:فرانسه نام گذاری کرده‌اند: الف - ویتامین 
87668:محلول در چسربی: ۱ -ویتامین ۸ -این 
87669:ویتامین عامل نمو بدن و عامل ضد خشکی
```


## [2026-09-06T02:28:34.487Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint('SOD leaves',len(b))\n# printed page ≈ leaf - 66\nfor leaf in (157,):\n    print(b[leaf][:1500])\nEOF",
 "description": "Print Gharib Sogdian page 91"
}
```


### [2026-09-06T02:28:36.482Z] TOOL RESULT

```
SOD leaves 645
 'zynt


                                                                   2324 >zn,ny C                                             92
                                                                                                                      ♦xJfol^l
       pl32 S =» 'zy'nt
 2311 >zynt                                                             azanne ©pi. -t ^z'nny
                                                                        confessor
 2312 vzyr S                            £^ «>j <f jj t/W                 BSTii 883.19; C2 gloss, n p86
      az/zy/zar ? ©ace. -w, ob. - >; pi. -f
      armour                                                       2325 Wptnym           B                            j>Jj<jj^
         MDii pi 52.5; MDiii                                             (o)zna-patnem
                                                                           =»jn}ptnym         Ozn'ptnym, 'nz'ptfym)

 2313 >zyrt S                                                (^          adviser
      (o)zyart (zyrt) =»jyrt
      quickly                                                            TSP 2.1155, 12.70; Gersh. Advice. 78bf; Hen.
      Hen. Tales. 475.11                                                   Tales. 480.13, 48ln 6

 2314 'zYw(h) B,S                          ^^'J^'J1^               2326 'zn^tnym         M(S) =* Wptnym
      azy/xu Czy'w)                                                2327 *znt C                                         <uo5<jb-k
```


## [2026-09-06T02:28:36.525Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *91 \\|^91 \" SOD_pages.txt | head -5\necho \"--- SNS ---\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nprint('SNS leaves',len(b))\nimport re\nfor i,blk in enumerate(b):\n    if 'zīw' in blk or 'ziw' in blk or 'zīnd' in blk:\n        print(i, blk[:200].replace('\\n',' '))\n        break\nEOF",
 "description": "Look up SOD entry 91 and SNS"
}
```


### [2026-09-06T02:28:38.139Z] TOOL RESULT

```
--- SNS ---
SNS leaves 243
```


## [2026-09-06T02:28:43.276Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nfor leaf in (156,158):\n    print('=== leaf',leaf,'===')\n    print(b[leaf][:1800])\nEOF",
 "description": "Print Gharib pages around 91"
}
```


### [2026-09-06T02:28:45.120Z] TOOL RESULT

```
=== leaf 156 ===
                                                                                         Mil

                                                                                                                                  'zyd-

 91
                                            'jf>\
         C2 gloss, n p63                                  ilfjijT           2300 >zbr-    C
 2287 >z)t,qt M                                                                  zPar ^zP^r-
                                                                                                                             jl^if
                                                                                                                             ■j   olj
                                                                                                                                     l
                                                                                                                                         jj




         azate-t        (»z>tk) ©pi.                                             (r<9)cross over
                                                       <o'                       STii 1.21; GMS 158n 1,240
         nobles
                                                                            2301 >zc C
         'z'w - C 22.76
         Sogdica.
                                                                                 azc, azac ©f. adj. =*>zty
 2288                                       tjj^p sJUj t^ihJiXj                  free woman, noble
         azaw      Ozw-)     -^nz'wt-                                                                                        jU <rJU
                                                                                 C2, 54R13
       
=== leaf 158 ===
                                                              mimmmmmm      mamim                                §M*m*



 93

                                                                                                                           'zw'st-
                                                                         VJ; GMS 97, 181; BBB b72
2336 'zrw' B       (^bjd^J><(J'j*j*''Sjt'WjjJ
     (a)zarwa (zrwn) =*zrw>                                      2347 >zw                                      (Jj^jl^j^
     Zurvan(M), Brahma(B)                                                azu   Czwty, >zwZY) ©Av. azdm-, OP adam\
      VJ 910; W-Li; Hen. Tales. 485; TSP; BSTBL,
                                                                           Parth. az ©Isg. pron. nom. ^mn1, zw, 'my1
        Vim. 129
                                                                         GMS 1338;. >zw ty, VJ 389, 1217 & etc.; >zwZY,
                                                                           BSTBL, Dhy. 308, BBB pl21
2337 'zrync- S                        o^J'^ jT O-^ob*;
     (o)zrenc ^zr'yt-, zr'ync-, zrync-                           2348 >zw-       B,S                            Q>fj*j<&-±j
      0<?)save, (redeliver                                               (o)zaw, (a)zu    =*jw-, zw-, zw-
      MDii pl23.19 n pl26; AVS 123
                                                                         GMS 264, 574 n 1; VJ 1371; TSP; MDii; Tales.
                                                                         0<?)live
2338 >zt C                                             J>^                 476.4; AVS 81
     azt ©pp.
      born                                                       2349 'zw- ■* ,z,w-
```


## [2026-09-06T02:30:05.242Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"zyw\\|zīwistan\\|zīwišn\\|to live\\|zindag\" SNS.txt SNS_pages.txt 2>/dev/null | head -10\necho \"=== leaves ===\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt',encoding='utf-8',errors='replace').read()\nb=t.split('\\f')\nfor leaf in (173,):\n    print(b[leaf][:900])\nEOF",
 "description": "Check SNS for zīw"
}
```


### [2026-09-06T02:30:07.588Z] TOOL RESULT

```
SNS.txt:10552:)yw:^V (iter. Man. II, 54) zyw : fli {AiWb . 502) 
SNS.txt:30041:zyw 170/19 
SNS_pages.txt:7172:                         )yw:^V         (iter. Man.          II, 54)              zyw      :   fli {AiWb .     502)
SNS_pages.txt:15435:                                                             zyw 170/19
=== leaves ===
                                                                                                                                                .




                                            Li; o-rfb uL*jlj
                                                                                                                                               lU^bi*                                                 n«
^ly-j^T            K:kara               karaistan:        wu>iij*j£> : TjA—
                               :   ;l
                                                                                                     >^r^^"l^:nislnan: y TyBWN, >n'                                                       „__
                                                                                                                      >                                                       ^^
```


## [2026-09-06T02:30:12.833Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=7172\nleaf='\\n'.join(lines[:i]).count('\\f')\nprint('leaf',leaf)\nprint('\\n'.join(lines[i-14:i+8]))\nEOF",
 "description": "Context of SNS zyw entry"
}
```


### [2026-09-06T02:30:14.503Z] TOOL RESULT

```
leaf 101
                                                   J I>1^.. c iL--jljil l>!j               :zen af zar:            *-^«^*£
                                                                                      .*ii» c ^L. 0rfj      :zin:v-J
                       {Arm Gram 151) zen                    :           ^jl AiWb 1650) zaena:
                                                                                           .                            fc-

                       infzar          +(jJ».y^e4j zln: ^.                  (tfir. Man. Ill,              65)zyn:^6
                        Noldeke ZDMG.                32,         408.             ;i&      Aar-^jiB .^lyl                          16

                                           .f/1T*S          -f -*>->W
                                                                                 awa«ar :^                (OVP£.    23_

                                                                              abS^Jij.jl^i :zlvad: *>***>
                          gay      :   >;, (A {fife.         609)           jlva-: ^jois ^Iva-: ^1 fc-
                         )yw:^V         (iter. Man.          II, 54)              zyw      :   fli {AiWb .     502)
                                                        •
                                                            TT/TY^                    tfir*.   Wan. Ill, 56)                       Y»


                                 US AiMi            ^^Aoi^.^i^-^i^jj rzlvisnlh: -*0*0*
                                          »
```


## [2026-09-06T02:30:28.291Z] TOOL CALL #66: Bash

```json
{
 "command": "ls site/pages/205.jpg 2>/dev/null; pdftoppm -f 205 -l 205 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg205 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 205"
}
```


### [2026-09-06T02:30:30.702Z] TOOL RESULT

```
site/pages/205.jpg
total 27264
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:30 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    2406 Sep  5 22:24 arm198b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3399 Sep  5 22:24 arm198c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3342 Sep  5 22:24 arm198.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   91088 Sep  5 22:21 bqt90.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51583 Sep  5 17:08 build173.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59926 Sep  5 17:11 build174.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64448 Sep  5 17:12 build175.py
-rw-rw-r-- 1 sfmqrb sfmqrb   69033 Sep  5 17:13 build177.py
-rw-rw-r-- 1 sfmqrb sfmqrb   75374 Sep  5 17:12 build180.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43965 Sep  5 17:11 build181.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64481 Sep  5 17:11 build182.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47920 Sep  5 17:11 build183.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62604 Sep  5 17:16 build184.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63773 Sep  5 17:17 build186.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62923 Sep  5 22:13 build189.py
-rw-rw-r-- 1 sfmqrb sfmqrb   39603 Sep  5 22:25 build190.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26679 Sep  5 22:22 hdr88.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12667 Sep  5 22:22 hdr89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3536 Sep  5 17:04 jang.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   45630 Sep  5 22:22 jaurb.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    4880 Sep  5 22:24 latin198b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3543 Sep  5 22:24 latin198.png
-rw-rw-r-- 1 sfmqrb sfmqrb     310 Sep  5 22:16 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb   84301 Sep  5 17:17 mk176.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68808 Sep  5 17:15 mk178.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1688 Sep  5 22:17 p190_eb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1093 Sep  5 22:17 p190_emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102711 Sep  5 22:17 p190hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5540 Sep  5 22:17 p190_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3718 Sep  5 22:21 p199_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4112 Sep  5 22:21 p199_pgang.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34164 Sep  5 22:21 p199_pgang_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53414 Sep  5 17:03 pg183.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79537 Sep  5 17:09 pg185.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72425 Sep  5 17:08 pg186.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60458 Sep  5 22:26 pg188.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65970 Sep  5 22:17 pg190.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78016 Sep  5 22:20 pg191.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71828 Sep  5 22:17 pg192.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75938 Sep  5 22:27 pg195.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85794 Sep  5 22:23 pg198.png
-rw-rw-r-- 1 sfmqrb sfmqrb  128252 Sep  5 22:21 pg199hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78587 Sep  5 22:19 pg199.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78934 Sep  5 22:22 pg200.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75609 Sep  5 22:18 pg203.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87032 Sep  5 22:30 pg205.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   55520 Sep  5 22:22 rootbox.png
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep  5 22:19 tad60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33410 Sep  5 22:22 vtra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
-rw-rw-r-- 1 sfmqrb sfmqrb     738 Sep  5 17:04 xang.txt
```


## [2026-09-06T02:30:33.635Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg205.png"
}
```


### [2026-09-06T02:30:34.091Z] TOOL RESULT

```

```


## [2026-09-06T02:30:34.088Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:31:40.452Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT jira ===\"; grep -n \"jTra\\|jira-\\|behende\\|'geschickt'\" BRT.txt | head -10\necho \"=== HRN zirak ===\"; grep -n \"zirek\\|zīrek\\|zirak\" HRN.txt | head -5\necho \"=== NYB getig/ziwistan ===\"; grep -n \"gētīk\\|getik\\|gēhān\\|gehan\\|zīwistan\\|ziwistan\\|zīwandag\" NYB_vol2_glossary.txt | head -10",
 "description": "Check jīra, zīrak, Nyberg"
}
```


### [2026-09-06T02:31:40.552Z] TOOL RESULT

```
=== BRT jira ===
11245:*lära.  Adj.,  zum  \.lar.;  ai.  Wro- Adj.  —  Pü.: tartarlum.  —  >>  FMÜLLERs  Zusammenstellung des  Worts  mit  arm.  tarlat  ■geschickt'.  WZKM. 8.  361  ist  ohne  Wert.  Das  arm.  LW.  farlar stammt  aus  ir.  *iarlara-,  das  zu  ai.  calara- Adj.   'geschickt'   gehört;   s.   dazu  Wn.  AiOr.
13079:KompA.,  E.;  AbLeit.  —  Zum  V.  dqh-,  IF.  7. 214.  —  u.  daimä-  Adj.  'geschickt'.  —  Pü. ; Jahm  (Transskr.),  mit  der  Eit.  (lu  Y.  32):  vPh mar/;  Sä. :  utiantah.  —  ')  Hds.  madahmö.  — >)  Hds.  lahmö,  s.  aber  Pü.  —  »  Das  Wort Kört  den  Sinn  und  ist  sicher  211  streichen,  da Ja'Knabe' im  Folgenden  enthalten  ist. —1)  Nur dieser;  TgL  Yt,  $.  93,  N.  10$. Baitholomai.  AldiuL  Wb.
29136:Pü.;  apäk  Kkt{ai). j.  haia.ztm%rd.iaräi  Yt.  5.  I9:  lies  haia  t'. ■  j,  haSa.hunara-  Adj.  'geschickt':  narfm ..  mqzdnm  'rtm  lanu.mqhr^m  V.  it?.  51; —  mazdrö  'rS  ianu.makrS  Yt.  j.  91.
=== HRN zirak ===
6006:681. zirek 'klug, entschlossen', äHr,
=== NYB getig/ziwistan ===
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
1655:gēhān [gyh’n'] pl. and coll., the world of creatures, men and animals, esp. the world of man: astömandän ~ 3913; han 4 mänisnömand (q.v.) göspandömand ~ 5714-15; herds of grazing animals 4913; — the material world in general: 21. 418 etc. passim. — < *gaidānām, gen. pl. of Av. (476 sqq.) gaēdā-; OP gai0à- “live-stock’; Aram. lw. (Targ, Talm) gyty ‘herds’; MPrth gyh (< gaia) ‘world’, pl. gyh?n ‘worlds’; Paz. geha; NP gehän, gihän, jihän. Cf gétah.
1660:gétik [gytyk] terrestrian, subst. pl. the material, terrestrian beings, cas. obl. —-ün [eytyk'n'] 8811135, 897, 9314, 1052; — yazdän + getikän the terres- trian gods 34!” (for cas. rect., mixed constr.) — MPrs gytyg ‘world’ (A-H II); Paz. pl. gēdya, ge0ia, Skr. v. thalokiyäh, thacarinah.
2524:mēnišn (mynšn'] thinking, thought, mind: together with gób?sn and kunišn v. göbisn ; Zartuxšt had ~ 4 fräröntar hac hamak gēhān a mind more righteous than (that of) all human beings 54%; ~ i fräröneh the way of thinking of honest people 6414; — ~ nihátan 6 to contemplate, to set one's mind on 5??*; 6 hän i ölsän ~ apar Sut hénd they inspired them 403-4; v. also apakandan, bastan, bastišn, nihä- tan, čpastan, viskaftan, vinäsitan; — pat ~ 4 Pourusäsp bim apakand 481911; pat ~ in my mind, through my inner senses 51%; hàn + či dētsr pat ~ his (spiritual) eye in his mind = his inner intuition 5226-27,
2539:spannäk ~ 659, spenäk (-nāt) ~ 10215-17, 10312, 106% = Av. Spanta-Mainyu-; 3 ~ 654; ~ i véh a good spirit, opp. ~ % vattar an evil spirit 651; pl. the celestial gods, pl. cas. obl. ~-dn 40%. 578, 5924, 7218, 7416, 8917.25, with the app. yazdan 7413-18; opp. gétikan, v. getik, 34". 2. the heavenly world, the beyond, opp. geteh, getah 3612, 629.1", 6819-20, 723; har 4 m opp. hir i getäh 6814, 798-11-12, 8023.25; šahr t ~ the realm of Heaven 667; mizd i ~ the reward of Heaven 62°. 658. — Av. (1136) mainyaoya-, adj. of mainyu- (v. s. v. dušmen); Paz. mainyč, minč etc.; NP minč ‘heaven’. The spelling mdnwd of FrP 1 (glossed by mynwy) is constant throughout the whole of BP, and must not be emended to mynwg or mynwk. An adj. mēnēk < *mainyava-ka- is so far only attested in MPrs: mynwg $h ‘the Heavenly King‘ (List 85), and the abstr. mynwgyh ‘the quality of possessing an animal spirit (menög)’, of the body, as opposed to gy’n and rw’n ‘the soul’, a purely Manichean terminology quite for- eign to Zoroastrianism. The Zoroastrians have always understood mönöi as an adj., rendering it in Skr by paralokiya, paralokacara, Sünyacärin (‘existing in the air-space', e.g. 7712. 8514-18), adrsya ‘in- visible’ (SGV), only in the sense of B 2 by a subst.: pat mēnči 723 Skr. v. paraloke. The construction of this adj.: optional addition of the ending -č and position before its head w., is taken over from the NW area, and known from Bal., where the adj. is regularly placed before its headw. and may, or may not, take the ending -e (thus Gilbertson) or -e, -en (thus Longworth Dames; traces of this ending in BP v.s. v. harvistén harvén, névakén). When this construction was borrowed by the SW language the ending -€ was mistaken for the izäfat; hence the translations of the Dasturs: paralokīyā yà buddhih for menöye xrat, ete.
3099:patvastan patvand-, to bind, to attach, to join: Tir patvast 7'-® meaning not clear: (joined to [the planet] Tir =) be- ing in conjunction with it (?); han hom andar hàn draxt bà patvast this haoma was attached to this tree 4015; cë rād ka mē- noyan u gētīkān dāntšn u kār-ākāhēh har 2 band 6 to patvast? 8811-1? (v. s. v. band); 12017-18, — < pati + band-, v. bastan; MPrs. pywst; Paz. paé- vastan; NP pai- vastan.
3270:rat [lt'] "genius", divinity or tutelary spirit presiding over one of the categories or classes into which all beings and things of the good creation are divided: ap?-Sün ~ Gēpet and their genius is G. 8674-25; Zartuxšt is ašūkān ~ the genius of (all) the Righteous 106!; he is in Avestan terminology the ahü and ratu of the world, hence the abstr. ahü-u-ratü-eh 4 gēhān 55%. — Av. (1498 sqq.) ?ratu-; NP rad ‘intelligent, learnd', ‘a high priest of the Magi'. As to the doctrine, v. Modi, Ceremonies 330—334.
3885:uzvühik ["wzw'hyk] brought out, spread abroad: yazdān ... andar gēhān ~ srav burt the message was announced to the world by the gods 55**, v. next w.
4891:gaidā-: gēhān
5147:gač0a: gēhān, gētāh fra-gam-: fražaftan gāman-: gam Gandarewa: Gandarv ganti-: gandakēh Gao-cidra: Göcihr lgaona-: gönak lgaona-: cigön gaosponta-: Göspand gaoyaoti-: gäviyöt gaoša-: gos
```


## [2026-09-06T02:31:50.233Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6000,6024p' HRN.txt",
 "description": "Read Horn 681 zīrek"
}
```


### [2026-09-06T02:31:50.277Z] TOOL RESULT

```
ertanih, erman(i)sn 'niedrigen Sinnes' (Men.) ^); ai. vergl.
ddhara',
kurd. i^r; [af;'. lar; oss. t. dälä 'hinunter 0^8)1;
bei. LW. deräy n. serä, ser 'unter, unterhalb, am Fusse
von (63), ir, er (169); arm. LW. zil 'soprano' (IT üb seh -
mann, ZDMG. 35, 129, No. 22; 46, 259 No. 12).
681. zirek 'klug, entschlossen', äHr,
ai. Jlnt' 'rasch, lebhaft, thätig; aw. Jlra-, jirö.sdrö
(Geldner, 3 Yasht, 64).
af/. 0ir 'eilig'; arm. LW. 217' Vacker, ausdauernd'
(llübschmann, S. 12).
682. iiiire 'Kümmel'.
skr. jtraka- 'Kümmel*; \\}\\\\, zärak, vd. 18 (67) Gl.,
nach Haug, aber gewiss nicht richtig].
Kann in einer der beiden Sprachen Lehnwort sein.
683. eisten 'X^haxi , Praes. ziy-em; zinde; ztve^ jlve 'Queck-
silber'*'^).
Käs. ßgd^ jandd, vHandö (s. v. zinde),
ap. l^i^^-, jii'ähy 'leben'; aw. Jvaiti, d. i. jloaiti
(yt. 24, 1); phlv. zivastany z'w{i)sn, zivet (3. Sg.),
zwanddk; ai. V^jw-, jivati; arm. keam 'leben', keanfi
'Leben', kendani 'lebendig* (H. No. 142).
kurd. mn, zin 'leben'; af/. 2vand, zvandim 'Leben,
Sein , zvandai 'lebendig'.
Dazu vielleicht auch hedi, d. i. ein aus bizi ver-
```


## [2026-09-06T02:32:23.833Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT jiva ===\"; grep -n \"jīva\\|jiva\" KNT.txt | head -8\necho \"=== KNT gaitha ===\"; grep -n \"gaiθā\\|gaitha\" KNT.txt | head -5",
 "description": "Grep Kent"
}
```


### [2026-09-06T02:32:23.896Z] TOOL RESULT

```
=== KNT jiva ===
500:j'va-diy Аа 3; but jiva, jiwahyà, ajivetam, jwà twice each, in inscriptions of Darius and Xerxes.
928:*g*iuos ‘living’, OP jiva, Skt. јаз, Lt. vivos. *dhi-dhi (8129), OP imv. didiy ‘see’, cf. NPers. didén ‘to see’, Skt. root dhì- ‘think’.
1409:Lt. divos. pIE *g*uo- ‘living’, OP jiva, Skt. jivd-s, Lt.
1533:*7"02- in guzddm ‘cattle’ (oi proved by the lack of palatalization of the g), *g*i- in jiva ‘living’.
2515:OP іту. jivà ‘live!’ from pIE "*g*i-ue; OP 3d du. imf. ajivatam; cf. Skt. jivati ‘he lives’: unless *g*iye- is really a broken reduplication *g*f-g*e- to the root *g*ei- ‘live’, with dissimilative loss of the second g, cf. Lt. vivo ‘I live’, vivos ‘living’, Ose. npm. bivus ‘living’, but oEng. cwicu "living", NEng. quick, Gm. queck, erquicken. $217. Tae Present-Tense System or DE-
2574:$229. Tug Personal ENDINGS оғ THE THIRD Duar Activg. This occurs in OP only in ajivatam ‘(the two) were living’, with ending agreeing with the Greek primary ending in present óperov ‘(the two) are bearing’, pIE -tom. In the corresponding imperfect, Gk. Dor. гферётау and Skt. dbharatém both have analogically lengthened vowels.
2604:I. The second smgular active of thematic stems is the stem without suffix: jivà, Skt. jiva; pari-bará, Skt. bhára, Gk. $€pe; parsa, Skt. prechd, Lat. posce. That of non-thematic stems has an accented -dhi, attached to the zero grade of the root: pIE *i-dht, OP -idiy in paraidiy and paridiy, Skt. tht, Gk. 16; pIE *gthn-dht, OP jadiy, Skt. jaht; OP pädiy, didiy (5129), G-rsnudiy.
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
=== KNT gaitha ===
```


## [2026-09-06T02:32:26.756Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 gwei leben ===\"; grep -n \"g\\^ei-\\|g'\\''ei-\\|gu̯ei-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== SKT quick ===\"; grep -n \"^Quick\\|Quick, \" SKT.txt | head -5\necho \"=== KLN microbe/zodiac/vitamin ===\"; grep -n \"microbe, n\\|zodiac, n\\|vitamin, n\" KLN_1966.txt | head -5",
 "description": "Grep WLD, Skeat, Klein"
}
```


### [2026-09-06T02:32:26.842Z] TOOL RESULT

```
=== WLD Bd1 gwei leben ===
=== SKT quick ===
=== KLN microbe/zodiac/vitamin ===
```


## [2026-09-06T02:32:36.020Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT quick ===\"; grep -n -i \"quick (1)\\|QUICK\\b\" SKT.txt | head -5\necho \"=== KLN 1971 microbe ===\"; grep -n \"microbe\" KLN_1971.txt KLN_1966.txt | head -5\necho \"=== KLN 1971 vitamin ===\"; grep -n \"vitamin\" KLN_1966.txt | head -5",
 "description": "Retry Skeat and Klein greps"
}
```


### [2026-09-06T02:32:36.110Z] TOOL RESULT

```
=== SKT quick ===
2314:Brisk.  (C.)  W.  bfys^,  quick:  Gael. briofg,  quick,  lively.  Allied  lo  Gael,  brietg, to  start  with  surprise,  leap  for  joy  ;  Irish briox^,  a  start,  a  bounce.
3208://r(/4i/^w,5peed.  —  L.«/^r,  quick.  (y^KAL.) accelerate.  (L.)    L.  acceUratM,  W-^^ a^ceUrare,  to  quicken.  •  L.  fl^--  (for  aJ) ;  and <£ier,  quick.
3559:Clever.  (F.-L.;  tenfmed  with  E.)  !■ BnUcr's  Hudibnu  (1663).  It  took  the  pl«c« of  M.  E.  dtlivrr,  quick,  nimble.  Ch.  proL 84.«»0.  F.  dtlivrt.  free,  prompt,  alcit; compounded  from  L.  de^  prefix,  and  /IBrr. free ;  see  Deliver.  But  apparently  confused with  M.  K.  (livir^  ft  claw,  also  as  adj.  rci'!^ to&eiie,  allied  to  Climb.Cloavei*^  %  Not from  A.  S.  gltiiw,  M.  E.  ^rt(,  skilfal ;  itill less  from  G.  klugW
6376:fast  (3),  to  abstain  from  food.  (£.)  A.  5. fiTf/dH,  orig.  to  moke  fast,  observe,  be strict :  from  fast  (above).  -4-  Du.  vastiH. Van./aj/t,  Swed.and  \cc\.fasta,  O.fasttn. ^^^^  (3)>  quick.  (Scasd.)  A  peculiar use  of /ai/  (i)  above;  this  use  is  Scnnd. Cf.  Iccl.  drtkita  fast,  to  drink  hard,  sofa fast,  to  be  fast  aalecp,^^/r  /  vrrkum^  harti
6379:at  work ;  &C.    It  means  firm,  close,  urgent, quick.
=== KLN 1971 microbe ===
KLN_1971.txt:29897:amphibious, bathybius, cenobite, microbe, hy- 
KLN_1971.txt:150952:microbe, n., a minute organism; popular name 
KLN_1971.txt:151101:microzyme, also microzyma, n., a zymotic microbe 
KLN_1966.txt:5041:bio-,  combining  form  meaning  ‘life’.  —  Gk.  (3io-, fr.  pios,  ‘life’,  dissimilated  fr.  *pi Foq,  fr.  I.-E. *glciwos;  cogn.  with  Goth,  qius,  OE.  cwicu, ‘living’.  See  quick,  and  cp.  vital,  zoo-.  Cp.  also biosis,  biotic,  and  the  second  element  in  aerobic, amphibious,  bathybius,  cenobite,  microbe,  hy¬ giene,  Limnobium,  Lithobius,  macrobiotic,  ne¬ crobiosis,  Rhizobium,  symbion,  symbiosis, biochemistry,  n.,  chemistry  dealing  with  animal and  plant  life.  —  See  bio-  and  chemistry, biogen,  n.,  a  protoplasmic  unit  ( biol .)  —  Coined by  the  German  physiologist  Max  Verwom (1863-1921)  in  1903  fr.  bio-  and  -gen. biogenesis,  n.,  the  theory  that  living  organisms can  only  arise  from  pre-existing  living  matter (biol.)—  Coined  by  the  English  biologist  Thomas Henry  Huxley  (1825-95)  in  1870  fr.  Gk.  pto?, ‘life’,  and  y^veoic,  ‘origin,  source’.  See  bio-  and genesis  and  cp.  abiogenesis. biogenesist,  n.,  one  who  believes  in  the  theory  of biogenesis.  —  See  prec.  word  and  -ist. biogenetic,  biogenetical,  adj.,  pertaining  to  bio¬ genesis.  —  See  biogenesis  and  -etic,  resp.  also  -al. Derivative:  biogenetic-al-ly,  adv. biogeny,  n.,  biogenesis.  —  Compounded  of  bio- and  -geny.
KLN_1966.txt:23818:microbe,  n.,  a  minute  organism;  popular  name for  a  bacterium.  —  Coined  by  the  French  sur¬ geon  Sddillot  in  1878  fr.  Gk.  pixpd?,  ‘small’, and  plo?,  ‘life’.  See  micro-  and  bio-.
=== KLN 1971 vitamin ===
2485:amidogen,  n.,  the  hypothetical  univalent  radical NH2  (chem.)  —  Coined  fr.  amido-  and  -gen. amidst,  prep.  —  Formed  with  excrescent  -t  fr. ME.  amiddes  (which  was  formed  with  adv.  gen. suff.  -s  fr.  amidde,  see  amid,  prep.)  For  the  -t cp.  against,  amongst,  betwixt,  whilst. amine,  amin,  n.,  a  compound  obtained  by  re¬ placing  hydrogen  atoms  of  ammonia  by  hydro¬ carbon  radicals  (chem.)  —  Coined  from  the  first syllable  of  ammonia  and  chem.  suff.  -ine.  Cp. amide  and  vitamin.  Cp.  also  imine. amino-,  combining  form  meaning  ‘pertaining  to, or  containing,  the  radical  NH2’  (chem.)  —  See prec.  word  and  cp.  deaminate. amir,  n.  —  See  ameer.
4122:avion,  n.,  an  airplane.  —  F.,  coined  by  the  French engineer  Clement  Ader  (1841-1925)  in  1875  fr. L.  avis,  ‘bird’.  See  aviary, avitai,  adj.,  ancestral.  —  Formed  with  adj.  suff. -al  fr.  L.  avitus,  ‘pertaining  to  a  grandfather, ancestral',  fr.  avus,  ‘grandfather’,  whence  avun¬ culus,  ‘uncle  on  the  mother’s  side’.  See  uncle, avitaminosis,  n.,  lack  of  vitamins  in  one’s  food ( biochem .)  —  A  ModL.  hybrid  coined  fr.  priv. pref.  a-,  vitamin  and  suff.  -osis. avizandum,  n.,  consideration  (Scot.  law).  —  ML., gerundive  of  avizare.  See  advise.  For  other  Latin gerundives  used  in  English  cp.  agenda  and words  there  referred  to.
11162:devise,  n.,  the  act  of  devising;  a  will  (law).  OF. devise,  ‘division;  will,  testament’,  fr.  deviser,  ‘to divide,  distribute’.  See  devise,  v. devitalize,  tr.  v.,  to  deprive  of  vitality.  —  Formed fr.  de-  (in  the  privative  sense  of  this  prefix)  and vitalize.  Derivative:  devitaliz-ation,  n. devitaminize,  tr.  v.,  to  deprive  of  vitamins.  — Formed  fr.  de-  (in  the  privative  sense  of  this prefix),  vitamin  and  suff.  -ize.
11163:Derivative:  devitaminiz-ation,  n. devitrification,  n.  —  Sec  next  word  and  -fication. devitrify,  tr.  v.,  to  deprive  of  glassy  character.  — Formed  fr.  de-  (in  the  privative  sense  of  this prefix)  and  vitrify.
32849:Derivatives:  ribbon-ed,  adj.,  ribbon-y,  adj. Ribes,  n.,  a  genus  of  shrubs,  the  currant.  —  ML., fr.  Arab,  ribas,  ‘sorrel’,  fr.  Pers.  revas. riboflavin,  n.,  a  factor  of  the  vitamin  B  complex C17H20O#N4.  —  Coined  fr.  ribose  and  flavin. ribose,  n.,  a  pentose  sugar.  —  Formed  with  subst. suff.  -ose  fr.  G.  Ribon(sdure),  a  tetrahydroxy acid,  whose  first  element  is  an  alteration  of  E. arabinose,  fr.  L.  Arabicus,  ‘Arabic,  Arabian’; see  Arabic  ( Sdure ,  the  second  element  in  Ribon- sdure,  means  ‘acid’.)
```


## [2026-09-06T02:32:38.207Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nb=t.split('\\f')\nprint('leaves',len(b))\nfor i,blk in enumerate(b):\n    if 'leben' in blk and ('vivos' in blk or 'vivus' in blk or 'quicu' in blk or 'cwicu' in blk):\n        print('LEAF',i, blk[:400].replace('\\n',' '))\n        break\nEOF",
 "description": "Find WLD gwei entry"
}
```


### [2026-09-06T02:32:39.869Z] TOOL RESULT

```
leaves 895
LEAF 677                              y                                                                       -                                                                           g" e i(°)-                                                669  ahd. knu-u) in ep. jon. fcoco, gort. Scorn „lebe“ (aor. ifMwv aus *gu iio-m mit vokal. i, das vermutlich durch fitoco gestiitzt wurde, atfc. £co, tfjg, Qf\ fiir
```


## [2026-09-06T02:32:48.155Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Funk\" KLN_1966.txt | head -3\necho \"=== zodiac ===\"; grep -n \"zodiac\" KLN_1966.txt | head -3\necho \"=== WLD leaf677 content ===\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[676][:1500])\nEOF",
 "description": "Klein vitamin/zodiac; WLD context"
}
```


### [2026-09-06T02:32:50.088Z] TOOL RESULT

```
=== zodiac ===
2371:Aludra,  n.,  name  of  a  constellation  in  the  zodiac.
3264:Aquarius,  n.,  a  constellation  and  the  eleventh sign  of  the  zodiac  (astron.)  —  L.,  ‘water  carrier’, prop,  the  adj.  aquarius,  ‘pertaining  to  water’. See  aquatic  and  cp.  prec.  word.  L.  Aquarius  as the  name  of  one  of  the  signs  of  the  zodiac  is  a loan  translation  of  TSpoxoo?,  ‘the  water- pourer’,  the  old  Greek  name  of  this  constellation, aquatic,  adj.  —  F.  aquatique,  fr.  L.  aqudticus, ‘found  in  the  water,  watery’,  fr.  aqua,  ‘water’, which  is  cogn.  with  Goth,  aka,  ‘river,  waters, OHG.  aha,  OFris.  d,  e,  ON.  6,  OE.  ea,  ‘water’, OHG.  auwia,  ouwa,  MHG.  ouwe,  G.  Au,  mead¬ ow  watered  by  a  brook’,  ON.  Asgir,  name  of the  god  of  the  sea,  ON.  ey,  OE.  leg,  ‘island’, Hitt,  akw-anzi,  ‘they  drink’;  cp.  the  Russian river  name  Oka,  and  the  second  element  in Sca(n)din-avia.  See  island  and  cp.  eagre,  tidal wave’,  ewer,  eyot.  Cp.  also  aquacade,  aquatint, aqueduct,  aqueous,  aquiline,  Aquilo,  gouache, Scandinavia.  For  the  ending  see  suff,  -atic. Derivatives:  aquatic-al,  adj.,  aquatic-al-ly,  adv. aquatint,  n.,  a  kind  of  engraving  with  aqua  fortis. —  It.  acquatinta,  fr.  L.  aqua  tincta,  'dyed  water’, fr.  aqua,  ‘water’,  and  tincta,  fern.  pp.  of  tingere, ‘to  dye’.  See  aquatic  and  tinge, aqua  tofana,  a  poisonous  liquid,  probably  of  ar¬
3428:Aries,  n.,  1)  a  constellation;  2)  the  first  of  the signs  of  the  zodiac  ( astron .)  —  L.  aries,  gen. arietis,  ‘lamb’,  cogn.  with  Arm.  or-oj  (assimil.  fr. *er-oj),  ‘lamb’,  Gk.  epi-ipop,  ‘kind’,  Olr.  heirp, ‘kid’,  Mir,  earb,  of  s.m. aright,  adv.  —  Formed  fr.  a-,  ‘on’,  and  right, aril,  n.,  an  accessory  covering  of  seeds  (bot.)  — Late  L.  arillus,  ‘dried  grape’, arioso,  adj.,  melodious;  adv.,  in  a  melodious way  ( mus .)  —  It.,  formed  fr.  aria,  ‘melody’,  with suff.  -oso  (corresponding  to  L.  -dsus).  See  aria and  adj.  suff.  -ose.
=== WLD leaf677 content ===
66b                                                                                   g”ei(o)-


Liden BB. 21, 102ff.) mhd. verquinen x),                                                            praet. quein .,hinschwinden", ags.
cwlnnn, a-eivinan , praet. avCoi ,,hinschwinden, abnehmen, krankeln", er-
weitert ags. cwincan dcivincnn „verschwinden. abnehmen (Kaus. mit Ab-
                                                                                                                                 -
                                                                                                                                     '
                                                 ,


lautneubildung acioencan, engl. quench ,.loschen“), und (nach Wood KZ.
-15, 64) mit >«-Formans wfiil. Liclnien ..krankeln", kiv7melig ..venveichlicht"
                                 2
(weiteres          s. u.).
                                     )

      Aus     dem Germ,                              scheinen                    in    beiden         Bedeutungsfarbungen anreihbar
    nach Wood KZ. 45, 64 f.):
     anord. kveita „iiberwaltigen" rZ-Praes.); s-Erweiterungen mnd. quisten „um-
                                                                             ;




kommen lassen, verschwenden",4»<s/ ,,Schaden, Yerlust", mnl. quisten „terere,
atterere,friare‘ , got. qistjan „verderben“ dies schon beiFickIII 4 63), ahd. quist
                             -
```


## [2026-09-06T02:33:00.458Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT zodiac/quick/vital ===\"; grep -n -i \"zodiac\\|Quick, living\\|Vital\\.\" SKT.txt | head -6\necho \"=== FSD vitamin ===\"; grep -n -i \"vitamine\\|vitamin,\" FSD_vol4.txt FSD_vol3.txt 2>/dev/null | head -5\necho \"=== WEB microbe ===\"; grep -n -i \"microbe\" WEB_vol1.txt | head -3",
 "description": "Grep Skeat, F&W, Webster"
}
```


### [2026-09-06T02:33:00.563Z] TOOL RESULT

```
=== SKT zodiac/quick/vital ===
21828:Zodiac :  sec  Zoology.
21832:ZODIAC
21833:Gto,  an  imaginftiy  belt  in  the  heavens, ing  the  twelve  Ji,f9u.  (F.  — L.~Gk.) z^ttf.  — L.  AH/eonu'.  ~  Gk.  (wfltcuK^s, zodiacal  circle ;  so  called  from  con- the  twelve  constellations  chiefly ited  by  animals.  — Gk.  {«Aia«^,adj., ig  to  animals.  ■*■  Gk.  (9;8iof,  a  small ;  dimin.  of  C«'o*'>  *  Hving  creature
=== FSD vitamin ===
=== WEB microbe ===
81431:2. a microbe; any microorganism, especially one of the bacteria, causing disease. 5
```


## [2026-09-06T02:33:45.404Z] AGENT

Now let me save the page image for audit and write the verification file.


## [2026-09-06T02:33:47.813Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg205.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/205.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T02:33:47.901Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T02:43:29.669Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build205.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-\"\nJIVEH = W + \"%D8%AC%DB%8C%D9%88%D9%87\"\nZIRAK = W + \"%D8%B2%DB%8C%D8%B1%DA%A9\"\nGITI  = W + \"%DA%AF%DB%8C%D8%AA%DB%8C\"\nJAHAN = W + \"%D8%AC%D9%87%D8%A7%D9%86\"\nAZIR  = W + \"%D8%A2%DA%98%DB%8C%D8%B1\"\nEV = \"https://www.etymonline.com/word/vitamin\"\nEM = \"https://www.etymonline.com/word/microbe\"\nEZ = \"https://www.etymonline.com/word/zodiac\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"jiva, jîta, jva; merezu-jîta; hu-jyâti\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The substance of the box is right; two of the citation forms are not. (1) Avestan jva- / jīva- 'living' and Old Persian jīva- are the direct u̯-stem continuants of PIE *gʷih₃-wo-: Pokorny 467-469 lists 'Old Indic jīva- \\\"living, m. life\\\", Old pers. jīva-, Avestan jva- (i.e. jīva-) \\\"living\\\" = Latin vīvus', and Bartholomae's verb entry jī-/jva- 'leben, am Leben sein' quotes the Old Persian imperative 'utā dargam jīva' (Bh 4.10, DPd) 'and may you live long'. Kent, Old Persian, §217, derives OP jīva 'live!' from pIE *gʷi-we and cites the 3rd dual imperfect ajīvatam '(the two) were living' (XPf 20-25). (2) 'jîta' is not an attested Avestan word: the abstract noun is jīti- f. 'life' (Pokorny p.468 '*gʷī-... Avestan jīti- f. \\\"life\\\"'), an i-stem, and it means 'life', not 'living'. (3) Likewise 'merezu-jîta': Pokorny 750-751 under *mreǵʰu- 'short' prints 'Avestan mərəzu-jīti-, -jva- \\\"βραχύβιος\\\"' (short-lived), and Bartholomae has both mərəzu.jītay- and mərəzu.jva- 'kurz(?) lebend'. So the compound is real and Nourai's gloss 'short lived' is Pokorny's own, but the second member is -jīti-/-jva-, not -jīta-. (4) hu-jyāiti- is genuine: Bartholomae gives jyātay- f. / jyātav- m. 'Leben' and the compounds vīspō.hujyātay- '(der alles gute Leben hat) der alles besitzt und bietet, was zum behaglichen Leben gehört' and frādat̰-vīspąm.hujyāitim 'die alles fördert, was zum behaglichen Menschenleben gehört', which is exactly Nourai's 'healthy, prosperous'; his spelling 'hu-jyâti' drops the diphthong of -jyāiti-. The printed page (pdf 205, saved as sources/refs/ocr/BOOK/205.png) shows 'jîta' and 'merezu-jîta', so the JSON is a faithful reading and the inaccuracy is the book's.\",\n \"derivation_fa\": \"محتوای این جعبه درست است اما دو صورت اوستایی آن دقیق نیست. اوستایی jva-/jīva- و پارسی باستان jīva- «زنده» بازماندهٔ مستقیم صورت *gʷih₃-wo- هندواروپایی‌اند؛ پوکورنی (ص ۴۶۷–۴۶۹) همین را می‌آورد و کنت در دستور پارسی باستان صورت امری jīva «زندگی کن!» (بیستون ۴٫۱۰) و ajīvatam را شاهد می‌گیرد. اما «jîta» صورتی اوستایی نیست؛ آنچه هست jīti- (نامِ مادّهٔ i-ستاک) به معنای «زندگی» است، نه «زنده». همچنین ترکیب «کوته‌زیست» در پوکورنی (ص ۷۵۰) به شکل mərəzu-jīti- و mərəzu-jva- ثبت شده است. hu-jyāiti- «زندگی خوش، کامروایی» نزد بارتولمه درست است (jyātay- «زندگی»). تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «jîta» را چاپ کرده، پس خطا از کتاب است نه از خوانش اسکن.\",\n \"error_in\": \"book\",\n \"book_prints\": \"jiva, jîta, jva ; merezu-jîta ; hu-jyâti\",\n \"correct_form\": \"jva-/jīva- 'living'; jīti- f. 'life' (not jîta); mərəzu-jīti- / mərəzu-jva- 'short-lived'; hu-jyāiti- 'good living'\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"KLN:1288\", \"status\": \"supports\", \"note\": \"Klein 1966 p.1288 s.v. 'quick': 'fr. Teut. *qwiqwa-, \\\"living, alive\\\", fr. I.-E. *gwigwos, fr. base *gwei-, \\\"to live\\\", whence Goth. *qius ... OI. jivah, \\\"alive\\\", jivati, Avestic jvaiti, \\\"lives\\\", OPers. jiva-, \\\"living\\\", Gk. bios ... L. vivus ... vita'. The page carries exactly the Avestan/Old Persian pair Nourai puts in this box (KLN_1966.txt, page marker '1288' at line 31391).\"},\n   {\"ref\": \"POK:467,750\", \"status\": \"supports\", \"note\": \"POK_full.txt: lemma 'gʷei-3 and gʷeiə- ... Meaning: to live', Page(s) 467-469, with 'Old pers. jīva- Avestan jva- (i.e. jīva-) \\\"living\\\" = Latin vīvus'; and lemma 'mreghu-, Meaning: short', Page(s) 750-751, 'Prakr. muhu-, Avestan mərəzu-jīti-, -jva- \\\"βραχύβιος\\\"'. Both cited pages say what the box says, except that the compound's second member is -jīti-/-jva-.\"},\n   {\"ref\": \"SNS:173\", \"status\": \"partial\", \"note\": \"Tavoosi's Shāyast-nē-Shāyast glossary does carry the entry (SNS_pages.txt leaf 101, right column): 'zīvad' with 'Av. jīva-, Skt. jīva-, gay (AiWb. 609), zyw (AiWb. 502), žyw (Mir. Man. II, 54)', followed by 'zīvišnīh'. The scan's printed page numbers could not be mapped to leaf 101, so the '173' itself is unverified.\"},\n   {\"ref\": \"SOD:91\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p.91 (SOD_pages.txt leaf 156) has entry 2288 'azaw (ʾzw-) → nzʾwt-', and the verb is spelled out on p.93 as '2348 ʾzw- B,S (a)zaw, (a)zu = jw-, zw-, žw- ... live'. The Sogdian cognate of the box is therefore on the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AirWb. s.v. jī-/jva-, jyātay-, mərəzu.jītay-, mərəzu.jva-, vīspō.hujyātay- (BRT.txt lines 10078, 11695, 20408, 20412, 24541)\", \"stance\": \"supports\", \"note\": \"'1) leben, am Leben sein: haca irista upa jvantəm V.10.1 ... || utā dargam jīva \\\"und du sollst lange leben\\\" Bh.4.10'; 'jyātay- f. \\\"Leben\\\"'; 'mərəzu.jva- Adj. \\\"-?- lebend\\\"'; 'vīspō.hujyātay- Adj. \\\"(der alles gute Leben hat, d. i.) der alles besitzt und bietet, was zum behaglichen Leben gehört\\\"'.\"},\n   {\"src\": \"KNT\", \"where\": \"Old Persian §217, §229, §290 (KNT.txt lines 2515, 2574, 2967)\", \"stance\": \"supports\", \"note\": \"'OP imv. jīvā \\\"live!\\\" from pIE *gʷi-ue; OP 3d du. impf. ajīvatam; cf. Skt. jīvati \\\"he lives\\\" ... cf. Lt. vivo \\\"I live\\\", vivos \\\"living\\\", Osc. bivus, OEng. cwicu \\\"living\\\", NEng. quick'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 467-469 and 750-751\", \"stance\": \"supports\", \"note\": \"see ref_check; Pokorny is the source of both halves of the box.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary\", \"stance\": \"silent\", \"note\": \"grep of IEC.txt for 'jiva', 'gwei', 'merezu' returned no usable entry (OCR of the transliteration is too damaged to search reliably).\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"zivastan; zivandak\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both words are genuine Middle Persian, and the derivation from the Old Iranian root is uncontested; the two things to correct are a reading and a gloss. (1) 'zivastan' is Horn's 1893 reading of Book Pahlavi ⟨zywstn'⟩: Grundriss no. 683 prints 'phlv. zīvastan, z'w(i)šn, zīvēt (3. Sg.), zīvandak'. MacKenzie's 1971 Concise Pahlavi Dictionary reads the same spelling as 'zī(wi)stan, zī(w)- [zywstn' | M zywystn, zyw-, N zīstan] live', i.e. zīwistan, and Moʿin's footnote in Borhān (p.~1038) also writes zīvistan; so the form in the chart is a superseded reading rather than an error of substance. (2) zīwandag is attested, but it means 'living, alive', not 'mercury': Hübschmann, Persische Studien, records 'phl. zīvandak \\\"lebendig\\\" Gl. and Ind. 152' and expressly separates it from 'zīva, jīva \\\"Quecksilber\\\" H.683'. What is true — and is presumably what Nourai compressed — is that the mercury word is built on it: Asbaghi, Persische Lehnwörter im Arabischen p.102, derives Arabic zībaq from 'pers. žīwa, žīwe ← MP zīwandak \\\"das Lebende\\\"', and Moʿin's footnote to Borhān s.v. جیوه says the same ('در اوستا žīv- آمده که در پهلوی zīvandak شده بمعنی زنده'). Phonetically MP zīw- shows the regular Southwest-Iranian treatment of Old Iranian ǰ- before ī as z- (Hübschmann §120b: 'zīstan \\\"leben\\\", zd. skr. jīv-'), against the ž-/j- of the mercury word, which Hübschmann §120c takes as a dialect or Northwest form.\",\n \"derivation_fa\": \"هر دو واژه پهلویِ اصیل‌اند و پیوندشان با ریشهٔ ایرانی باستان تردیدناپذیر است؛ تنها دو نکته باید اصلاح شود. نخست، «zivastan» خوانشِ هرن (۱۸۹۳، شمارهٔ ۶۸۳) از ⟨zywstn'⟩ است؛ مکنزی همان املا را zī(wi)stan یعنی zīwistan می‌خواند و حاشیهٔ معین بر برهان قاطع نیز zīvistan نوشته است، پس صورتِ نمودار خوانشی کهنه است نه غلط. دوم، zīwandag در متون پهلوی به معنای «زنده» است، نه «جیوه»؛ هوبشمان صریحاً آن را از zīva/jīva «جیوه» جدا می‌کند. آنچه درست است این است که نامِ جیوه بر همین صفت ساخته شده: اصباغی (ص ۱۰۲) عربیِ زیبق را از فارسیِ ژیوه و آن را از پهلویِ zīwandak «زنده» می‌گیرد و معین هم در حاشیهٔ برهان همین را می‌گوید. از نظر آوایی ǰ ایرانی باستان پیش از ī در فارسی میانهٔ جنوب‌غربی به z بدل شده (zīstan) و صورتِ ژ/ج‌دار (ژیوه) گویشی است.\",\n \"sources\": [JIVEH],\n \"ref_check\": [\n   {\"ref\": \"BQT:606\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ, entry جیوه ('بروزن میوه، سیماب را گویند ... و بعربی زیبق خوانند'), BQT_v2_pages.txt leaf 64 (printed ≈604-606; the file's leaf→page offset drifts ±2 in this stretch). Moʿin's footnote there: 'در اوستا žīv- آمده که در پهلوی zīvandak شده بمعنی زنده و نیز بمعنی گردنده و جهنده ... در فارسی ژیوه با ج «جیوه» نامیده شده (و زیبق معرب آن است)'. Exactly the Pahlavi→Persian→Arabic chain of the chart.\"},\n   {\"ref\": \"BQT:1038\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 500 (printed ≈1038-1040), footnote 8 on زنده: 'پهلوی zīndak (حی) از zīvandak با پسوند -ak ... از žīv- (zīvistan زیستن) ... zīndakīh'. Confirms both zīwandag and the infinitive, and gives the modern reading zīvistan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.99 (PHD.txt line 680)\", \"stance\": \"partial\", \"note\": \"'zī(wi)stan, zī(w)- [zywstn' | M zywystn, zyw-, N zīstan] live. zī(w)išn [zywšn'] life; livelihood. zīwēnīdan, zīwēn- vivify, revive. zindag [zy(w)ndk' | M zyndg, N zinda] alive, living.' MacKenzie has zindag but not a separate zīwandag, and no mercury sense.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for zīwistan / zīwandag returned nothing: Shkand-Gumānīg Wizār and the Bundahišn texts Nyberg glosses do not use the verb in the passages he indexes.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 683 (HRN.txt line 6021 ff., p.151)\", \"stance\": \"supports\", \"note\": \"'zīsten \\\"leben\\\", Praes. zīy-em; zinde; zīve, jīve \\\"Quecksilber\\\" ... ap. jīva-, jīvāhy \\\"leben\\\"; aw. jvaiti, d. i. jīvaiti; phlv. zīvastan, z'w(i)šn, zīvēt (3. Sg.), zīvandak'. This is where Nourai's spelling 'zivastan' comes from.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.~186 and §120-121 (HUB.txt lines 5970, 8166, 8188)\", \"stance\": \"partial\", \"note\": \"'phl. zīvandak \\\"lebendig\\\" Gl. and Ind. 152 ... Dagegen zīva, jīva \\\"Quecksilber\\\" H.683'; and 'zīva ~ jīva \\\"Quecksilber\\\" ... zu skr. jīva- \\\"lebendig\\\". Die Wrzl. jīv \\\"leben\\\" liegt also als jīv, žīv (in žīva, jīva) und zīv (in zīstan) vor.' Hübschmann keeps the adjective and the metal name apart.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.102\", \"stance\": \"supports\", \"note\": \"'žīwa: \\\"Quecksilber\\\" aus dem pers. žīwa, mp. zīwandak \\\"das Lebende\\\", ar. zībaq' — the mercury word is derived from zīwandak.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"zîstan «زیستن»; zendegî «زندگی (زنده)»; jîveh «ژیوه (جیوه)»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three, and the three extra forms in the box (زیست، زی، آبزی), continue Middle Persian zīw-. (1) زیستن zīstan < MP zī(wi)stan; the intervocalic -w- of the present stem zīw- was lost before the New Persian ending, giving زی‌ zī-/زیَد zīyad, with the old -w- still visible in Awromani ziwāy and Kurdish ziyān; Cheung, Etymological Dictionary of the Iranian Verb, s.v. *jaiH2 (p.223) lists 'NP zīstan/zīy- \\\"to live\\\" ... NP zindah', ultimately '*PIE *gʷeiH₃-, LIV 215 f., Pok. 467 f.'. زیست is the past stem used as a noun ('life, biology'), زی the bare present stem, آبزی 'aquatic (organism)' a modern compound آب + زی of exactly that stem. (2) زندگی is the abstract in -ī of زنده zenda < MP zindag [zy(w)ndk'] < zīwandag, i.e. zīw- + the participial suffix -andag, contracted; Moʿin's footnote on Borhān p.~1038 spells the contraction out: 'پهلوی zīndak از zīvandak با پسوند -ak'. (3) ژیوه/جیوه 'mercury': Wiktionary derives جیوه from a Middle Persian *zīwag ⟨zywk'⟩ 'mercury' (whence also Syriac ܙܝܘܓ zīwag), itself from zīndag/zīwandāg 'living', from Old Persian jīva-, from PIE *gʷih₃wós, and compares Latin argentum vīvum and English quicksilver for the naming motive; Horn no. 683 already had 'zīve, jīve \\\"Quecksilber\\\"' in the same entry as zīsten.\",\n \"derivation_fa\": \"هر سه واژه و سه صورتِ افزودهٔ جعبه (زیست، زی، آبزی) دنبالهٔ ستاکِ پهلویِ zīw- اند. «زیستن» از zī(wi)stan پهلوی است؛ واوِ میان‌واکه‌ایِ ستاکِ حال zīw- در فارسی نو افتاده و «زی/زیَد» به دست آمده، ولی در کردی «ژیان» و اورامی ziwāy هنوز پیداست (چونگ، ذیل *jaiH₂، ص ۲۲۳). «زیست» ستاکِ گذشته در کارکردِ اسم و «آبزی» ترکیبِ نوساخته از آب + زی است. «زندگی» اسم مصدرِ «زنده» است و «زنده» از zindag پهلوی که خودْ کوتاه‌شدهٔ zīwandag است (حاشیهٔ معین بر برهان). «ژیوه/جیوه» از فارسی میانهٔ *zīwag «جیوه» است که بر همان صفتِ «زنده» ساخته شده؛ همان انگیزهٔ نام‌گذاری که در لاتینِ argentum vivum و انگلیسیِ quicksilver دیده می‌شود. ادعای نورایی در این گره درست است.\",\n \"sources\": [JIVEH],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʿin, Farhang-e Fārsi, s.v. جیوه: '[= ژیوه > زیبق، معر.]' (MON_part1.txt line 49349) — Moʿin himself makes جیوه the Persian original and زیبق its Arabicised form. No page number is given by Nourai, and the six-volume edition is not online, so the page cannot be checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Etym. Dict. of the Iranian Verb, *jaiH2, p.223 (CHEUNG.txt line 14986)\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP zīstan/zīy- \\\"to live\\\", Kurd. žīyan/žī-, Awrom. žiwāy/-žiw-, ... NP zindah ... *SANSKRIT: jīv- \\\"to live\\\" ... «PIE *gʷeiH₃-, *gʷieH₃- ... LIV: 215 f. | Pok.: 467 f.'\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 683 (p.151)\", \"stance\": \"supports\", \"note\": \"'zīsten \\\"leben\\\", Praes. zīy-em; zinde; zīve, jīve \\\"Quecksilber\\\"'; footnote: 'Skr. jīvaka- \\\"lebendig, lebhaft\\\"; LW. arab. zi'baq, syr. ..., kurd. zīve, arm. zpak \\\"Quecksilber\\\"'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ p.~604-606, s.v. جیوه, with Moʿin's footnote\", \"stance\": \"supports\", \"note\": \"'جیوه ـ بروزن میوه، سیماب را گویند ... و بعربی زیبق خوانند'; footnote 'در اوستا žīv- ... در پهلوی zīvandak ... در فارسی ژیوه با ج «جیوه» نامیده شده'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.99\", \"stance\": \"supports\", \"note\": \"'zī(wi)stan ... N zīstan'; 'zindag ... N zinda'; the Persian outcomes are named in the entries themselves.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Arabic\",\n \"words\": \"zîbaq\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic زِئْبَق ziʾbaq / زِيبَق zībaq 'mercury' is a Persian loanword, not a Semitic root formation: the shape CiCCaC with a hamza inserted to break the -īb- is a typical Arabic accommodation of a foreign disyllable. Asbaghi, Persische Lehnwörter im Arabischen p.102, gives 'žīwa: \\\"Quecksilber\\\" aus dem pers. žīwa, mp. zīwandak \\\"das Lebende\\\", ar. zībaq', and repeats it under the Arabic headword on p.151 ('zībaq: \\\"Quecksilber\\\" pers. žīwa, žīwe ← MP zīwandak'). Horn no. 683 had already listed 'LW. arab. ziʾbaq' beside Syriac and Armenian zpak among the borrowings of Persian žīva, and Wiktionary lists Arabic زِئْبَق among the Iranian borrowings of جیوه. The word entered Arabic through the alchemical/medical literature of the 8th-9th centuries (Jābir, al-Rāzī), where سیماب/زیبق is a standard technical term, and thence into Andalusi Arabic and Spanish azogue. Nourai's arrow (Pahlavi → Arabic) is right in substance; strictly the immediate donor is the Persian form žīwa/žīwag rather than zīwandag itself.\",\n \"derivation_fa\": \"عربیِ «زِئبَق/زیبَق» به معنی جیوه وام‌واژه‌ای ایرانی است، نه ساختهٔ ریشه‌ای سامی؛ همزهٔ میانی برای شکستنِ خوشهٔ -īb- افزوده شده است. اصباغی (ص ۱۰۲ و ۱۵۱) آن را از فارسیِ ژیوه/ژیوه‌گ و آن را از پهلویِ zīwandak «زنده» می‌گیرد و هرن (شمارهٔ ۶۸۳) نیز «LW. arab. zi'baq» را در کنار صورت‌های سریانی و ارمنی می‌آورد. راهِ ورودِ واژه ادبیاتِ کیمیا و پزشکیِ سدهٔ دوم و سومِ هجری است. جهتِ فلشِ نورایی درست است؛ تنها دقت این است که وام‌دهندهٔ بی‌واسطه صورتِ فارسیِ ژیوه است نه خودِ zīwandag.\",\n \"sources\": [JIVEH],\n \"ref_check\": [\n   {\"ref\": \"PLA:102\", \"status\": \"supports\", \"note\": \"Asbaghi p.102 (PLA_pages.txt leaf 117; printed page = leaf − 15): 'žīwa: \\\"Quecksilber\\\" aus dem pers. žīwa mp. zīwandak \\\"das Lebende\\\" ar. zībaq'. The cited page says precisely what the arrow says.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 683 footnote (HRN.txt line 6030)\", \"stance\": \"supports\", \"note\": \"'Skr. jīvaka- \\\"lebendig, lebhaft\\\"; LW. arab. ziʾbaq, syr. ..., kurd. zīve, arm. zpak \\\"Quecksilber\\\"' — Arabic is explicitly marked a loanword (LW) from the Persian.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān p.~604-606, Moʿin's footnote s.v. جیوه\", \"stance\": \"supports\", \"note\": \"'... در فارسی ژیوه با ج «جیوه» نامیده شده (و زیبق معرب آن است)' — 'zībaq is its Arabicised form'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.v. quicksilver\", \"stance\": \"partial\", \"note\": \"'quicksilver ... fr. OE. cwicseolfor, lit. \\\"quick (i.e. living) silver\\\", loan translation of L. argentum vivum' — Klein has no Arabic entry, but he documents the same 'living metal' naming motive that produced žīwa/zībaq.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\", \"note\": \"grep of AFM.txt for زیبق returned no hit (the OCR of the Arabic headword list is incomplete in this stretch).\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Persian\",\n \"words\": \"zîbaq «زیبق»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"زیبق zībaq in Persian is the Arabicised form of the native ژیوه coming home — a round trip Persian žīwa → Arabic zībaq → Persian زیبق, and therefore a doublet of جیوه. Moʿin marks it as such in his own dictionary ('جیوه: [= ژیوه > زیبق، معر.]', i.e. 'zībaq, muʿarrab'), and the Borhān footnote quoted above says '(و زیبق معرب آن است)'. In Persian usage زیبق belongs to the learned register — pharmacology, alchemy and the medical translations from Arabic — beside the everyday سیماب and جیوه; the Borhān itself glosses several plant and mineral names with 'و معرّب آن زیبق است'. Nourai's arrow (Arabic → Persian) is right, and the box correctly keeps it separate from جیوه in node 3 rather than deriving one Persian form from the other.\",\n \"derivation_fa\": \"«زیبق» در فارسی همان «ژیوه»ی معرّب‌شده است که دوباره به فارسی بازگشته؛ یعنی چرخه‌ای از فارسی ← عربی ← فارسی، و از این رو دوگانهٔ «جیوه» به شمار می‌رود. معین خود در فرهنگش می‌نویسد «جیوه: [= ژیوه > زیبق، معر.]» و حاشیهٔ برهان قاطع نیز می‌گوید «و زیبق معرب آن است». کاربردِ «زیبق» در فارسی ادبیِ داروشناسی و کیمیا است، در برابرِ «سیماب» و «جیوه»ی رایج. فلشِ نورایی (عربی ← فارسی) درست است و به‌درستی این صورت را از «جیوه» جدا نگاه داشته است.\",\n \"sources\": [JIVEH],\n \"ref_check\": [\n   {\"ref\": \"MON:1768\", \"status\": \"partial\", \"note\": \"The six-volume Moʿin is not digitised, so p.1768 could not be opened; the two-volume Adena condensation carries the same statement s.v. جیوه ('[= ژیوه > زیبق، معر.]', MON_part1.txt line 49349) and lists زیبق as a synonym of جیوه (MON_part2.txt lines 54257, 62922). Content supported, page number unchecked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, several loci (BQT_v2_pages.txt lines 24231, 29963, 31325, 40599; BQT_v3_pages.txt line 50823)\", \"stance\": \"supports\", \"note\": \"'وسیماب و زیبق را بیزمیگویند'; 'ومعرب آن زیبق باشد'; 'بزبان ارباب عمل که کیمیاگرانند وعربان زیبق' — زیبق is used throughout as the Arabic equivalent of سیماب/جیوه.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.102 / p.151\", \"stance\": \"supports\", \"note\": \"the Arabic zībaq is itself derived from Persian žīwa, so the Persian زیبق is necessarily a re-borrowing.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Avestan\",\n \"words\": \"gayô-maretan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan gayō.marətan- is the name of the first man in the Zoroastrian tradition, literally 'mortal life' or 'life (that is) mortal': gaya- m. 'life, lifetime, way of life' (Bartholomae s.v. ¹gaya- 'Leben; Lebenszeit; Lebensführung', with the gāthic dative gaiiōi) + marətan- 'mortal, one who is to die' (root mar- 'to die', cf. Skt. márta-). Bartholomae's own note on ²gaya- 'EN. des ersten Menschen' says 'Vgl. ¹gaya-. Eig. \\\"Leben\\\" oder \\\"menschliches Leben\\\"'. gaya- itself is the o-grade nominal *gʷoy-o- of the same root as jva-/jīva-, which is why Pokorny puts it in the gʷei-3 lemma ('Avestan gaya- n. \\\"life, lifetime, lifestyle\\\" = Old Indic gaya-ḥ ... = Russ. goj'). Nourai's gloss 'perishable life (man)' is an accurate paraphrase, and the cross-reference to his chart 'Mer 2' (the root *mer- 'to die') is the right place for the second member.\",\n \"derivation_fa\": \"اوستایی gayō.marətan- نامِ نخستین انسان در سنت زردشتی است و لفظاً «زندگیِ مردنی» معنا می‌دهد: gaya- «جان، زندگی، زیست» به‌علاوهٔ marətan- «مردنی، درگذشتنی» از ریشهٔ mar- «مردن». بارتولمه ذیل gaya-ی دوم (نام خاص) می‌نویسد «قس gaya-ی یکم؛ در اصل یعنی زندگی یا زندگیِ انسانی». خودِ gaya- صورتِ o-پایهٔ *gʷoy-o- از همان ریشهٔ jva-/jīva- است و پوکورنی آن را در همین مادهٔ ص ۴۶۷ آورده است. برگردانِ نورایی و ارجاعش به ریشهٔ Mer 2 برای جزء دوم درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1872\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1872 (vol.3 scan, pdf page 669; printed = pdf + 1203), footnote 1 to the entry گیومرت: 'پهلوی Gayōmart. اوستایی Gayō_maretan، بارتولمه ۵۰۳ ... جزء اول «گیو» و «گیه» بمعنی جان و زندگی است و جزء دوم «مرتن» صفت است بمعنی مردنی و درگذشتنی، وبتعبیر دیگر مردم ... پورداود، یشتها'. Exactly Nourai's analysis, with Bartholomae col. 503 as the authority.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AirWb. col. 503 f., s.v. ¹gaya-, ²gaya- (BRT.txt lines 10092, 10097-10099)\", \"stance\": \"supports\", \"note\": \"'¹gaya- m. \\\"Leben; Lebenszeit; Lebensführung\\\"'; '²gaya- m. EN. des ersten Menschen ... Vgl. ¹gaya-. Eig. \\\"Leben\\\" oder \\\"menschliches Leben\\\"'; the Pahlavi rendering is quoted as 'yān a gayōmart'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Gayōmart (PHD.txt line 380)\", \"stance\": \"supports\", \"note\": \"'Gayōmart [gywkmlt' = Av. gayō marətan | (M gyhmwrd), N ~] the First Man' — MacKenzie equates the Pahlavi name with the Avestan compound directly.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 467 (POK_full.txt line 38684)\", \"stance\": \"supports\", \"note\": \"under gʷei-3: 'gaya- n. \\\"life, lifetime, lifestyle\\\" (= Old Indic gaya-ḥ \\\"house and courtyard\\\" = russ. goj)' — gaya- belongs to this root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Persian\",\n \"words\": \"Kîŭmars «کیومرث»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian کیومرث Kayūmars (also گیومرت, and in the Šāhnāme کیومرث) is the regular continuation of Middle Persian Gayōmard/Gayōmart ⟨gywkmlt'⟩, itself Avestan gayō.marətan-. The sound history is straightforward: initial g- before the front glide was affricated/fronted to k- in the Islamic-period spellings (the Borhān prints گیومرت beside کیومرث), Middle Persian -ō- gave -ū-/-ow-, and the final dental was written with ث in Arabic-script orthography — which the Borhān explicitly calls an innovation: 'ودر لغت متأخرین ... مشهور است و حال آنکه این رسم فارسی قدیم است و در کلام فارسی قدیم ثای مثلثه نیامده است'. Nourai's gloss '\\\"mortal man\\\"' matches Moʿin's own footnote gloss of the compound. The second reference ZMA:21 (Jonaydi, Zendegi va Mohājerat-e Āryāʾiyān) could not be consulted.\",\n \"derivation_fa\": \"«کیومرث» فارسیِ نو دنبالهٔ قاعده‌مندِ Gayōmard/Gayōmart فارسی میانه و آن از اوستایی gayō.marətan- است. gِ آغازی در املای دورهٔ اسلامی به ک بدل شده (برهان هر دو صورت گیومرت و کیومرث را دارد)، ō فارسی میانه به ū/ow، و دندانیِ پایانی با «ث» نوشته شده است — و برهان قاطع خود این «ث» را نوآوریِ متأخران می‌داند: «در کلام فارسی قدیم ثای مثلثه نیامده است». معنایی که نورایی داده («مردِ مردنی») همان است که معین در حاشیه آورده. مأخذ دومِ او (ZMA:21، جنیدی) در دسترس نبود.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1872\", \"status\": \"supports\", \"note\": \"Borhān p.1872 (vol.3 scan pdf 669): headword 'گیومرت ... نخستین کسی را گویند که در عالم پادشاهی کرد ... چه کیو بمعنی [جان] و مرت بمعنی زنده آمده است ودر لغت متأخرین ... و حال آنکه این رسم فارسی قدیم است ودر کلام فارسی قدیم ثای مثلثه نیامده است'; footnote 1 as quoted on node 6.\"},\n   {\"ref\": \"ZMA:21\", \"status\": \"not_checked\", \"note\": \"Fereydun Jonaydi, Zendegi va Mohājerat-e Āryāʾiyān (Bonyād-e Neyshābur 1374) is purchase-only; refs_online.json records that no open or lending copy exists on archive.org, ketabnak or noorlib.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Gayōmart\", \"stance\": \"supports\", \"note\": \"'Gayōmart [gywkmlt' = Av. gayō marətan | (M gyhmwrd), N ~]' — the '~' means the New Persian form is identical in shape, i.e. Kayūmars.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān p.1872, footnote 1 (Moʿin, citing Pourdāvūd, Yašthā)\", \"stance\": \"supports\", \"note\": \"'... او را مردنی و درگذشتنی نامیده‌اند) «پورداود، یشتها»'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"gaĕtha; gaĕtha-nâm; gaitha\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The words and the root attribution are right; the gloss on the first is not. Avestan gaēθā- is a feminine noun, never a verb, so 'to exist' is wrong: Bartholomae glosses it (1) the living beings, 'die stoffliche, sichtbare Welt', (2) '\\\"Wesen\\\" im Sinn von \\\"Anwesen\\\"; Gehöft, Haus und Hof, Hausstand (familia), überhaupt Hab und Gut ... weltlicher Besitz', which is Nourai's third gloss 'living property, cattle'. 'gaĕtha-nâm' is not a separate lexeme either but the genitive plural gaēθanąm 'of the living beings / of the possessions' — and Nourai is right to single it out, because that case form is the etymon of Pahlavi gēhān (node 9). 'gaitha' is simply the Old Persian shape of the same word: Pokorny 467 prints 'Avestan gaēθā, Old pers. gaiθā \\\"entity, house and courtyard\\\"', and Nyberg glosses 'OP gaiθā- \\\"live-stock\\\"'. The root connection is Pokorny's own — gaēθā- is a θā-derivative of the same gaya-/*gʷei- stem as node 6.\",\n \"derivation_fa\": \"واژه‌ها و انتسابشان به این ریشه درست است، اما معنای نخستین نادرست. اوستایی gaēθā- اسمِ مادّهٔ مؤنث است و هرگز فعل نیست، پس «to exist» خطاست؛ بارتولمه آن را چنین معنی می‌کند: ۱) آفریدگانِ زنده، جهانِ مادّی و دیدنی، ۲) «خانه و کاشانه، خانمان، دار و ندار، مالِ دنیوی» — که همان معنای سومِ نورایی («مِلک و ستور») است. «gaētha-nâm» هم واژهٔ جداگانه نیست، بلکه صورتِ جمعِ اضافیِ gaēθanąm است؛ ولی جدا آوردنش هوشمندانه است، چون همین صورت ریشهٔ «گیهان» پهلوی است (گرهٔ ۹). «gaitha» نیز صورتِ پارسی باستانِ همان واژه است. پیوند با ریشهٔ *gʷei- را خودِ پوکورنی (ص ۴۶۷) می‌آورد.\",\n \"sources\": [JAHAN],\n \"ref_check\": [\n   {\"ref\": \"POK:467\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma gʷei-3, p.467-469: 'Avestan gaēθā, Old pers. gaiθā \\\"entity, house and courtyard\\\"', immediately after 'gaya- \\\"life, lifetime, lifestyle\\\"'. Both forms of the box are on the cited page and both are put under this root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AirWb. col. 476-479, s.v. gaēθā- (BRT.txt line 9742)\", \"stance\": \"partial\", \"note\": \"'... zur stofflichen, sichtbaren Welt des Aša gehört ... 2) \\\"Wesen\\\" im Sinn von \\\"Anwesen\\\"; \\\"Gehöft, Haus und Hof\\\", Hausstand (familia), überhaupt \\\"Hab und Gut\\\" (im Gegensatz zu tanū-, ...), \\\"weltlicher Besitz\\\"'. A noun, not a verb — so Nourai's 'to exist' is a mis-gloss, though 'existing things' and 'living property, cattle' are right.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. gēhān (NYB_vol2_glossary.txt line 1655)\", \"stance\": \"supports\", \"note\": \"'< *gaiθānām, gen. pl. of Av. (476 sqq.) gaēθā-; OP gaiθā- \\\"live-stock\\\"; Aram. lw. (Targ., Talm.) gyty \\\"herds\\\"; MPrth gyh (< gaiθa) \\\"world\\\"' — confirms both the Old Persian form and the genitive plural that Nourai lists.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon\", \"stance\": \"silent\", \"note\": \"grep of KNT.txt for gaiθā returned nothing: the word is not attested in the Achaemenid inscriptions, so Kent's lexicon has no entry (Nyberg's 'OP gaiθā-' is a reconstruction from the Avestan/Parthian evidence).\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 951 (p.212)\", \"stance\": \"supports\", \"note\": \"'gehān \\\"Welt\\\" ... aw. gaēθā (gaēθanąm); phlv. gehān' — Horn cites the genitive plural in exactly the shape Nourai's box gives.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"Pahlavi\",\n \"words\": \"gětîk, gětě; gěhân\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Two different formations from the same Avestan noun, and Horn's page 212 — the page Nourai cites — separates them exactly as the chart does. (1) gētīg/gētīh 'the material world; worldly' (MacKenzie 'gētīg [gytyk, gytydy | M gytyg, N gētī] 1. the material world; 2. worldly'; Nyberg 'gētīk [gytyk] terrestrian, subst. pl. the material, terrestrian beings') goes back to the Avestan adjective gaēθya- 'irdisch' with the productive Middle Persian adjective suffix -īg; Horn no. 949 'gētī \\\"Welt\\\", aw. gaēθya- \\\"irdisch\\\"; phlv. gētīk'. Nourai's second form gětě is the variant gētēh/gētīh that Horn discusses in the footnote to that entry ('Die Syrer schreiben ... gethīh, und so ist also wohl auch im Pehlevī getīh zu lesen'). (2) gēhān is not a singular at all but the frozen genitive plural: Nyberg, '< *gaiθānām, gen. pl. of Av. gaēθā-', with intervocalic -θ- > -h- and the Avestan gen. pl. ending -ānąm giving the Middle Persian plural-looking -ān; MacKenzie 'gēhān [gyhʾn' | = M, N gihān, jahān] world'.\",\n \"derivation_fa\": \"دو ساختِ متفاوت از یک واژهٔ اوستایی، و درست همان‌گونه که هرن در صفحهٔ ۲۱۲ (همان صفحه‌ای که نورایی ارجاع داده) از هم جدایشان می‌کند. نخست gētīg/gētīh «جهانِ مادّی، این‌جهانی» از صفتِ اوستاییِ gaēθya- «زمینی» با پسوندِ زایای -īg فارسی میانه؛ هرن شمارهٔ ۹۴۹: «gētī \\\"Welt\\\"، اوستایی gaēθya- \\\"irdisch\\\"، پهلوی gētīk». صورتِ دومِ نورایی (gětě) همان gētēh/gētīh است که هرن در پانوشتِ همان مدخل بحث می‌کند. دوم gēhān که اصلاً مفرد نیست، بلکه صورتِ جمعِ اضافیِ *gaiθānām است (نیبرگ)؛ θ میان‌واکه‌ای به h بدل شده و پایانهٔ -ānąm به -ān رسیده. مکنزی: «gēhān … N gihān, jahān».\",\n \"sources\": [GITI, JAHAN],\n \"ref_check\": [\n   {\"ref\": \"HRN:212\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.212 (HRN.txt leaf 233): '949. gētī \\\"Welt\\\". aw. gaēθya- \\\"irdisch\\\"; phlv. gētīk. Mot savant; die den Lautgesetzen entsprechende neupersische Form ist gehān (No. 951).' and '951. gehān \\\"Welt\\\", arab. LW. jīhān, jehān, aw. gaēθā (gaēθanąm); phlv. gehān'. Both Pahlavi words of the box are on the cited page with these etymologies.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.36 (PHD.txt line 380)\", \"stance\": \"supports\", \"note\": \"'gēhān [gyhʾn' | = M, N gihān, jahān] world. ~īg [-yk'] worldly, mortal.'; 'gētīg [gytyk, gytydy | M gytyg, N gētī] 1. the material world; 2. worldly.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.vv. gēhān, gētīk (lines 1655, 1660)\", \"stance\": \"supports\", \"note\": \"'gēhān [gyhʾn'] pl. and coll., the world of creatures, men and animals ... < *gaiθānām, gen. pl. of Av. gaēθā- ... Paz. gehā; NP gehān, gihān, jihān. Cf. gētah.'; 'gētīk [gytyk] terrestrian ... MPrs gytyg \\\"world\\\" (A-H II); Paz. pl. gēθya, geθia'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān p.1868, Moʿin's footnote 4 to گیتی\", \"stance\": \"supports\", \"note\": \"'اوستا -gaēθa- ... پازند gētī, gētīh، پهلوی gētēh ... هوبشمان ۹۴۹ ... و قس: گهان، جهان' — Moʿin gives the same two Pahlavi shapes (gētēh/gētīh) that Nourai's 'gětîk, gětě' renders.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"Persian\",\n \"words\": \"gîtî «گیتی»; keyhân «کیهان (جهان)»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The two Persian words are doublets of one Avestan noun, and Horn's page 212 states the relation exactly: گیتی gītī is a 'mot savant', a learned borrowing straight from the Pahlavi book-form gētīg/gētīh (Wiktionary: 'From Middle Persian gytyk (gētīg, \\\"the material world; worldly\\\")'), while the phonetically regular outcome is گیهان gēhān > جهان jahān. In جهان the g- of gēhān was palatalised to j- (the ordinary New Persian treatment before a front vowel, as in Horn's 'arab. LW. jīhān, jehān'), and کیهان keyhān/kayhān is the same gēhān with the initial stop kept unvoiced in the learned reading — Wiktionary calls جهان and کیهان doublets outright, from Middle Persian gēhān, from Old Persian *gaiθānām, gen. pl. of *gaiθā, from Proto-Iranian *gayθaH 'life, means of subsistence'. Nourai's box therefore correctly puts گیتی and کیهان/جهان side by side under one Pahlavi parent.\",\n \"derivation_fa\": \"این دو واژهٔ فارسی دوگانه‌های یک نامِ اوستایی‌اند و هرن در صفحهٔ ۲۱۲ همین را می‌گوید: «گیتی» واژه‌ای عالمانه (mot savant) و وام‌گرفته از صورتِ کتابیِ پهلوی gētīg/gētīh است، حال آنکه بازماندهٔ قاعده‌مند و آواییِ همان ریشه «گیهان» و از آن «جهان» است. در «جهان» گِ آغازی پیش از واکهٔ پیشین به ج بدل شده — همان دگرگونیِ همیشگیِ فارسی نو — و «کیهان» همان گیهان است با خوانشِ عالمانه و بی‌واک. ویکی‌واژه «جهان» و «کیهان» را صریحاً دوگانه می‌خواند، از gēhān فارسی میانه، از *gaiθānām پارسی باستان، از ایرانی آغازین *gayθaH. چیدمانِ نورایی درست است.\",\n \"sources\": [GITI, JAHAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:1868\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.1868 (vol.3 scan, pdf page 665), entry گیتی 'بمعنی دنیا و جهان' with the compounds گیتی‌نورد, گیتی‌فروز; Moʿin's footnote 4: 'اوستا -gaēθa- ... پازند gētī, gētīh، پهلوی gētēh ... هوبشمان ۹۴۹ ... و قس: گهان. جهان.' The page also carries the گیهان entry with the footnote 'پهلوی gēhān (دنیا) جمع حالت اضافی از اوستایی -gaēθanąm' on p.1872.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss nos. 949 and 951, p.212\", \"stance\": \"supports\", \"note\": \"'gētī ... Mot savant; die den Lautgesetzen entsprechende neupersische Form ist gehān (No. 951)'; '951. gehān \\\"Welt\\\", arab. LW. jīhān, jehān'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. gēhān, gētīg\", \"stance\": \"supports\", \"note\": \"'gēhān ... N gihān, jahān'; 'gētīg ... N gētī' — MacKenzie names both New Persian outcomes.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. gēhān\", \"stance\": \"supports\", \"note\": \"'Paz. gehā; NP gehān, gihān, jihān'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11,\n \"lang\": \"Avestan\",\n \"words\": \"žîra, â-žîra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The adjective is real and belongs here, but its Avestan shape is jīra-, with the palatal ǰ, not žīra-: Pokorny p.468, in the *gʷī- section of this root, prints 'Old Indic jīrá- \\\"agile, lively, rash, hasty\\\", Avestan jīra- \\\"brisk of mind, smart\\\"', and Horn no. 681 gives 'ai. jīrá- \\\"rasch, lebhaft, thätig\\\"; aw. jīra-, jīrō.sāra- (Geldner, 3. Yašt 64)'. Formally jīra- is *gʷih₃-ro-, the zero grade of the root with the adjectival suffix -ro-, so 'quick, lively' is the primary sense and 'alert, clever' the derived one — the same shift as in Latin vīvāx or English lively/quick-witted. Nourai's ž- is an anticipation of the Middle/New Persian consonant (the by-form ژیر beside زیرک), not the Avestan letter. The prefixed variant 'â-žîra' is not a lemma in Bartholomae; New Persian آژیر is analysed as ā- + žīr, and Wiktionary describes آژیر only as 'Borrowed from Avestan, etymologically related to زیرک', without an attested *ā-jīra-.\",\n \"derivation_fa\": \"این صفت واقعی است و به همین ریشه تعلق دارد، اما صورتِ اوستایی‌اش jīra- با جیمِ کامی است، نه žīra-: پوکورنی در بخشِ *gʷī- همین ماده (ص ۴۶۸) می‌آورد «سنسکریت jīrá- \\\"چابک، سرزنده\\\"، اوستایی jīra- \\\"تیزهوش، زیرک\\\"»، و هرن نیز در شمارهٔ ۶۸۱ همین دو را کنار هم می‌گذارد. از نظر ساخت، jīra- همان *gʷih₃-ro- است، یعنی درجهٔ صفرِ ریشه با پسوندِ صفت‌سازِ -ro-؛ پس معنای نخستین «چابک، تیز» است و «زیرک» تحولِ معناییِ آن. «ژ»ی نورایی صورتِ فارسیِ میانه/نو را پیش‌انداخته است. صورتِ پیشوندیِ â-žîra نیز در فرهنگ بارتولمه مدخل ندارد؛ «آژیر» فارسی را ā- + ژیر تحلیل می‌کنند و ویکی‌واژه تنها می‌گوید «وام‌گرفته از اوستایی، هم‌ریشه با زیرک».\",\n \"sources\": [AZIR, ZIRAK],\n \"ref_check\": [\n   {\"ref\": \"POK:468\", \"status\": \"supports\", \"note\": \"POK_full.txt, within lemma gʷei-3 (pp.467-469), the *gʷī- paragraph: 'Avestan yavae-jī- \\\"perpetually living\\\", Avestan jīti- f. \\\"life\\\", Old Indic jīrá- \\\"agile, lively, rash, hasty\\\", Avestan jīra- \\\"brisk of mind, smart\\\"'. Pokorny confirms both the word and its membership in this root; the spelling is jīra-, not žīra-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 681 (HRN.txt line 6006, p.151)\", \"stance\": \"supports\", \"note\": \"'681. zīrek \\\"klug, entschlossen\\\", āžīr. ai. jīrá- \\\"rasch, lebhaft, thätig\\\"; aw. jīra-, jīrō.sāra- (Geldner, 3. Yašt 64). afg. žīr \\\"eilig\\\"; arm. LW. žir \\\"wacker, ausdauernd\\\"'. Horn puts zīrak and āžīr together under Avestan jīra-, exactly the arrow Nourai draws.\"},\n   {\"src\": \"BRT\", \"where\": \"AirWb.\", \"stance\": \"silent\", \"note\": \"greps of BRT.txt for jīra-/žīra- and for a prefixed ā-jīra- produced only unrelated hits (pouru.jira in Yt.5.93 and the compound adaoyō.jīratav- 'des Verstand untrüglich ist' at line 3234); the OCR of the ǰ- section is too damaged to confirm the simplex entry, and no ā- compound surfaced.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, IE roots s.v. gʷei-\", \"stance\": \"silent\", \"note\": \"the appendix lists only the branches with English reflexes (quick, vital, bio-, zoo-, hygiene); the Iranian jīra- adjective is not mentioned, which is not a disagreement.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12,\n \"lang\": \"Persian\",\n \"words\": \"zîrak «زیرک»; âžîr «آژیر (ژیر)»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"زیرک zīrak is a straight inheritance: MacKenzie has 'zīrak [zylk' | M zyr, N ~] wise, clever', and Wiktionary 'Inherited from Middle Persian zylk (zīrak) (Manichaean Middle Persian zyr)', which continues Avestan jīra- with the diminutive/adjectival -ak (< *-aka-) and the regular Southwest-Iranian development of the initial. آژیر āžīr is the harder of the two. Its classical sense is 'wary, on guard', which is precisely how Ferdowsī uses it in the verse printed in the box — 'سپه را بیارای و آژیر باش / شب و روز با ترکش و تیر باش' ('marshal the army and be on your guard') — and Horn no. 681 lists āžīr in the same entry as zīrek, i.e. from the same Avestan adjective, with a prefix ā-. Wiktionary agrees that آژیر is 'Borrowed from Avestan, etymologically related to زیرک'. The third gloss, 'warning siren', is 20th-century: the classical adjective was re-used by the Farhangestān for the alarm device, so it is a modern semantic extension and not part of the inherited word. Nourai's own reference for this box (FAF:28, Daneshgar's Farhang-e Aʿlām-e Fārsi) is not obtainable.\",\n \"derivation_fa\": \"«زیرک» میراثِ مستقیم است: مکنزی «zīrak … دانا، هوشیار» را ثبت کرده و ویکی‌واژه آن را از zīrak فارسی میانه (مانویِ zyr) می‌گیرد، که خود از jīra- اوستایی با پسوندِ -ak (از *-aka-) ساخته شده است. «آژیر» دشوارتر است: معنای کلاسیکش «هوشیار، برحذر» است، دقیقاً همان که فردوسی در بیتِ چاپ‌شده در جعبه به کار برده («سپه را بیارای و آژیر باش…»)، و هرن آن را در همان مدخلِ zīrek و از همان صفتِ اوستایی با پیشوندِ ā- می‌آورد؛ ویکی‌واژه هم آن را وام‌گرفته از اوستایی و هم‌ریشهٔ «زیرک» می‌داند. اما معنای «سوتِ خطر» ساختهٔ سدهٔ بیستم و برساختهٔ فرهنگستان است، نه بخشی از واژهٔ کهن. مأخذی که نورایی برای این جعبه آورده (FAF:28) در دسترس نیست.\",\n \"sources\": [ZIRAK, AZIR],\n \"ref_check\": [\n   {\"ref\": \"FAF:28\", \"status\": \"not_checked\", \"note\": \"A. Daneshgar, Farhang-e Aʿlām-e Fārsi (Hafez Novin 1370): refs_online.json records 'none online ... nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores)'. Could not be consulted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.99 (PHD.txt line 680)\", \"stance\": \"supports\", \"note\": \"'zīrak [zylk' | M zyr, N ~] wise, clever' — the Middle Persian ancestor of زیرک, with the New Persian form identical.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 681, p.151\", \"stance\": \"supports\", \"note\": \"'zīrek \\\"klug, entschlossen\\\", āžīr. ... aw. jīra-' — Horn treats both Persian words of this box as reflexes of the one Avestan adjective.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, s.v. آژیر (BQT_v2_pages.txt line 31325)\", \"stance\": \"partial\", \"note\": \"the Borhān's آژیر there is glossed 'آبگیر و تالاب' ('pond'), a homonym; the Borhān does not carry the 'wary' sense at that entry, so it neither supports nor contradicts the etymology of the adjective.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13,\n \"lang\": \"Latin\",\n \"words\": \"viva, vivere\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin vīvus 'alive' (the chart's 'viva' is its feminine) and the denominative vīvō, vīvere 'to live' are the Italic reflexes of the same *gʷih₃-wo- as Avestan jīva-. The Proto-Indo-European labiovelar *gʷ- became Latin v- through *gʷ > *gw > v (Kent: 'common Latin gʷ- > gv- > v-'), so *gʷīwos gave vīvus and *gʷīwō gave vīvō, with vīta 'life' < *gʷīwotā (Pokorny: 'Lithuanian gyvatà \\\"life, livelihood\\\" = Latin vīta \\\"life\\\" (*gʷīwotā)'). Watkins/AHD sets it out as 'I.2.a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CONVIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gʷi-wo-tā in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN.' The pass-through box is therefore accurate; the only quibble is that the dictionary lemma is vīvus, not vīva.\",\n \"derivation_fa\": \"لاتینِ vīvus «زنده» (صورتِ «viva»ی نمودار مؤنثِ همان است) و فعلِ برساختهٔ vīvō, vīvere «زیستن» بازتابِ ایتالیکِ همان *gʷih₃-wo- اند که در اوستایی jīva- شده است. لبی‌کامیِ *gʷ- هندواروپایی در لاتین از راهِ *gw به v رسیده، پس *gʷīwos به vīvus و *gʷīwō به vīvō بدل شده، و vīta «زندگی» از *gʷīwotā است. واتکینز در پیوستِ فرهنگ American Heritage همین را می‌آورد. جعبه درست است؛ تنها نکته آنکه صورتِ مدخلی vīvus است نه viva.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 540), s.v. gʷei-: 'I.2.a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: ... VIVA, VIVACIOUS, VIVID; CONVIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gʷi-wo-tā in Latin vita, life: VIABLE, VITAL ... VITAMIN. [Pok. 3. gʷei- 467.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.v. quick\", \"stance\": \"supports\", \"note\": \"'L. vivus, (for *gwiwos), \\\"living\\\", vivo, -ere (for *gwiwō), \\\"to live\\\", vita (for *gwiwita), \\\"life\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 468-469\", \"stance\": \"supports\", \"note\": \"'with f. Old Indic jīva- \\\"living\\\", Old pers. jīva-, Avestan jva- ... = Latin vīvus'; 'Lithuanian gyvatà \\\"life, livelihood\\\" = Latin vīta \\\"life\\\" (*gʷīwotā)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 668 f. (WLD_Bd1_pages.txt leaves 676-677)\", \"stance\": \"supports\", \"note\": \"the gʷei(ə)- entry that Pokorny abridges; leaf 677 carries the header 'gʷei(ə)- 669' with the Greek and Germanic material, the Latin material standing in the same article.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14,\n \"lang\": \"French\",\n \"words\": \"vitamine\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word is built on Latin vīta, but it is a 20th-century laboratory coinage, and the coiner was not French: Etymonline records 'vitamin (n.) 1920, originally vitamine (1912) coined by Polish biochemist Casimir Funk (1884-1967), from Latin vita \\\"life\\\" (see vita) + amine, because they were thought to contain amino acids ... The terminal -e formally was stripped off when scientists learned the true nature of the substance.' Funk published the term in London (Journal of State Medicine, 1912); French vitamine, German Vitamin and English vitamine are all the same neologism spreading in the same decade. Nourai's box is therefore right that Persian ویتامین came in through French — Moʿin tags the Persian word as a European borrowing and prints the Latin-letter form beside it — but wrong to imply that French was where the word was made. The empty-gloss pass-through box is otherwise accurate.\",\n \"derivation_fa\": \"این واژه بر پایهٔ vīta لاتین ساخته شده، اما برساختهٔ آزمایشگاهیِ سدهٔ بیستم است و سازنده‌اش فرانسوی نبود: کازیمیر فونکِ لهستانی در ۱۹۱۲ در لندن آن را به صورت vitamine ساخت (از vita لاتین + amine)، و «e» پایانی در ۱۹۲۰ افتاد. صورت‌های فرانسوی، آلمانی و انگلیسی همه همین نوواژه‌اند که در یک دهه پخش شد. پس اینکه نورایی «ویتامین» فارسی را از راهِ فرانسه می‌داند پذیرفتنی است — معین هم آن را وام‌واژهٔ اروپایی می‌شمارد — ولی نمی‌توان گفت واژه در فرانسه ساخته شده است.\",\n \"sources\": [EV],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷei-, I.3\", \"stance\": \"supports\", \"note\": \"'Further suffixed form *gʷi-wo-tā in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN' — the appendix routes vitamin through Latin vīta, as the chart does.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. amine, avitaminosis (lines 2485, 4122)\", \"stance\": \"partial\", \"note\": \"'amine ... Coined from the first syllable of ammonia and chem. suff. -ine. Cp. amide and vitamin.'; 'avitaminosis ... A ModL. hybrid coined fr. priv. pref. a-, vitamin and suff. -osis.' Klein confirms the vita + amine composition but says nothing about a French stage.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15,\n \"lang\": \"Persian\",\n \"words\": \"vîtâmîn «ویتامین»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"ویتامین is a straightforward 20th-century European loan into Persian, taken in with the rest of the modern medical vocabulary and, like most of that layer, mediated by French: Moʿin's dictionary enters ویتامین with the Latin-script French headword beside it and the subject tag (بز.) 'biology', and derives the compound ویتامین‌ها and the loan آویتامینوز (French avitaminose) from it — the presence of the French-shaped derivative آویتامینوز rather than an English-shaped one is itself evidence for the French route. The Persian spelling ویتامین preserves the French pronunciation with initial v- and final nasal-free -in.\",\n \"derivation_fa\": \"«ویتامین» وام‌واژه‌ای اروپایی از سدهٔ بیستم است که همراهِ واژگانِ پزشکیِ نو و — مانند بیشترِ آن لایه — از راهِ فرانسه وارد فارسی شده است. معین در فرهنگ خود «ویتامین» را با صورتِ لاتینِ فرانسوی و نشانهٔ موضوعیِ (بز.) آورده و مشتقِ «آویتامینوز» (فرانسویِ avitaminose) را نیز ثبت کرده است؛ همین صورتِ فرانسوی‌شکلِ مشتق، خود گواهِ مسیرِ فرانسوی است. املای فارسی هم تلفظِ فرانسوی را نگاه داشته.\",\n \"sources\": [EV],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʿin, entry ویتامین (MON_part2.txt line 87635) with the Latin-script European headword and the tag '(بز.)'; the run-on entries ویتامین‌ها (line 87645) and the note 'امراض ناشی از فقدان ویتامین را آویتامینوز [گویند]' (line 87642) show the French-based terminology. No page number was given by Nourai.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (2-vol. Adena condensation), s.v. ویتامین\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt / ARY_latin_index_pages.txt for ویتامین returned nothing; Aryanpur's book covers inherited Indo-European vocabulary, not modern European loans.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16,\n \"lang\": \"English\",\n \"words\": \"vital, survive, vitamin\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three reach English through Latin vīta/vīvere. vital: Middle English vital, from Old French vital, from Latin vītālis 'of life', from vīta. survive: Middle English surviven, from Anglo-French survivre, from Latin supervīvere 'to outlive', super- + vīvere. vitamin: as at node 14, Funk's 1912 vitamine, respelled 1920. Watkins/AHD lists exactly this set under the root — 'Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CONVIVIAL, REVIVE, SURVIVE' and 'Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN' — so the box needs no reference of its own.\",\n \"derivation_fa\": \"هر سه واژه از راهِ vīta/vīvere لاتین به انگلیسی رسیده‌اند: vital از vītālis لاتین از طریق فرانسهٔ کهن؛ survive از supervīvere لاتین (super- + vīvere) از راهِ انگلونورمان؛ و vitamin همان برساختهٔ فونک در ۱۹۱۲. واتکینز در پیوستِ American Heritage دقیقاً همین سه واژه را ذیل این ریشه فهرست کرده است، پس این جعبه به مأخذِ جداگانه نیاز ندارد.\",\n \"sources\": [EV],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent Latin box carries AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷei-, I.2.b and I.3\", \"stance\": \"supports\", \"note\": \"'... REVIVE, SURVIVE'; '... VIABLE, VITAL; LIGNUM VITAE, VITAMIN'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.v. quick\", \"stance\": \"supports\", \"note\": \"'Cp. also bio-, hygiene, jiva, vital and words there referred to' — Klein's own cross-reference list from the root article to vital.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17,\n \"lang\": \"Greek\",\n \"words\": \"bios; mikro-bios; hu-giĕs\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three are ancient Greek; the middle one is not. (1) βίος bíos 'life' is *gʷi-wo-s, dissimilated from *βίϝος: Klein, 'Gk. bio-, fr. bios, \\\"life\\\", dissimilated fr. *biwos, fr. I.-E. *gwiwos; cogn. with Goth. qius, OE. cwicu, \\\"living\\\"'. (2) ὑγιής hygiḗs 'healthy' is a genuine ancient compound and Watkins analyses it exactly as Nourai does: 'IV. Prefixed and suffixed form *su-gʷiə-es- (*su-, well; see su-), \\\"living in good condition,\\\" in Greek hugiés, healthy: HYGEIA, HYGIENE'; Pokorny p.468 the same, 'gr. hygiḗs \\\"fit, healthy\\\" (*su-gʷiies \\\"living well\\\")'. The cross-reference to Nourai's own 'Su 1' chart for the first element is right. (3) 'mikro-bios' is not a Greek word at all: microbe was coined in French in 1878 by the surgeon Charles-Emmanuel Sédillot from μικρός + βίος (Klein: 'Coined by the French surgeon Sédillot in 1878 fr. Gk. mikros, \\\"small\\\", and bios, \\\"life\\\"'), and Etymonline adds that the compound is badly formed — 'in Greek the compound would mean \\\"short-lived\\\"'. So the box mixes a 19th-century neologism in among two inherited Greek words.\",\n \"derivation_fa\": \"از سه واژهٔ این جعبه دو تا یونانیِ باستان‌اند و یکی نه. «βίος» از *gʷi-wo-s است که از *βίϝος همگون‌زدایی شده (کلاین: هم‌ریشه با qius گوتی و cwicu انگلیسی کهن). «ὑγιής» نیز ترکیبی اصیل و باستانی است و واتکینز همان تحلیلی را می‌دهد که نورایی داده: *su-gʷih₃-es- «خوش‌زیست»، پس ارجاعِ او به نمودارِ Su 1 برای جزء نخست درست است. اما «mikro-bios» اصلاً واژهٔ یونانی نیست: microbe را در ۱۸۷۸ جراحِ فرانسوی سدیّو از μικρός و βίος ساخت، و به گفتهٔ Etymonline ترکیبش هم نادرست است، چون در یونانی معنای «کوته‌عمر» می‌دهد. پس در این جعبه یک نوواژهٔ سدهٔ نوزدهم در میانِ دو واژهٔ اصیلِ یونانی نشسته است.\",\n \"sources\": [EM],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. gʷei-: 'II. Suffixed zero-grade form *gʷi-o- in Greek bios, life (> biotē, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS'; 'IV. Prefixed and suffixed form *su-gʷiə-es- ... in Greek hugiés, healthy: HYGEIA, HYGIENE'. AHD supports bios and hygiēs, and lists MICROBE as a modern derivative of bios — not as a Greek word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. bio- (line 5041) and microbe (line 23818)\", \"stance\": \"partial\", \"note\": \"'bio- ... fr. Gk. bios, \\\"life\\\", dissimilated fr. *biwos, fr. I.-E. *gwiwos ... Cp. also ... microbe, hygiene'; 'microbe, n. ... Coined by the French surgeon Sédillot in 1878 fr. Gk. mikros, \\\"small\\\", and bios, \\\"life\\\".'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 468\", \"stance\": \"supports\", \"note\": \"'ep. Ionian zōō ... \\\"live\\\" ... gr. hygiḗs \\\"fit, healthy\\\" (*su-gʷiies \\\"living well\\\")'; and under B, 'Agr. bíos \\\"life\\\" (*gʷi-w-os)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18,\n \"lang\": \"French\",\n \"words\": \"microbe\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French microbe was coined in 1878 by the surgeon Charles-Emmanuel Sédillot, who proposed it to the Académie des Sciences as a general term for the minute organisms that Pasteur's work had brought to attention, replacing the confusing 'bacterium/vibrio/monad' terminology. Klein: 'microbe, n., a minute organism; popular name for a bacterium. — Coined by the French surgeon Sédillot in 1878 fr. Gk. mikros, \\\"small\\\", and bios, \\\"life\\\"'; Etymonline dates the English borrowing to the same year and quotes Weekley's verdict that it was 'badly coined ... by Sédillot'. The French word spread across Europe within a decade, which is how it reached Persian (node 19). This pass-through box is exactly right.\",\n \"derivation_fa\": \"واژهٔ فرانسویِ microbe را در ۱۸۷۸ شارل امانوئل سدیّوِ جراح ساخت و به فرهنگستان علوم فرانسه پیشنهاد کرد تا نامی همگانی برای موجوداتِ ریزی باشد که کارهای پاستور آنها را به میان آورده بود. کلاین: «ساختهٔ سدیّوِ جراحِ فرانسوی در ۱۸۷۸ از mikros و bios یونانی». همین واژه در یک دهه در سراسر اروپا پخش شد و از همان راه به فارسی رسید (گرهٔ ۱۹). این جعبه کاملاً درست است.\",\n \"sources\": [EM],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.~960 s.v. microbe (KLN_1966.txt line 23818)\", \"stance\": \"supports\", \"note\": \"'Coined by the French surgeon Sédillot in 1878 fr. Gk. mikros, \\\"small\\\", and bios, \\\"life\\\". See micro- and bio-.'\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary (WEB_vol1.txt line 81431)\", \"stance\": \"supports\", \"note\": \"'a microbe; any microorganism, especially one of the bacteria, causing disease' — the sense in which the French word was borrowed.\"}\n ]\n})\n\nnodes.append({\n \"id\": 19,\n \"lang\": \"Persian\",\n \"words\": \"mîkrob «میکرب»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"میکرب/میکروب mikrob is the French microbe taken into Persian in the late Qajar / early Pahlavi period along with the rest of the vocabulary of modern medicine and public health; the -b of the Persian reflects the French final consonant, and the spelling میکرب without the waw is the older orthography that Nourai reproduces from Moʿin (modern usage writes میکروب). Moʿin enters it with the European headword and the subject tag (بز.) 'biology', and the derived compounds (میکرب‌کش, میکرب‌شناسی) are built on it in Persian. No Arabic or Ottoman intermediary is needed: French was the language of Iranian medical training (the Dār al-Fonūn) in the period when the word entered.\",\n \"derivation_fa\": \"«میکرب/میکروب» همان microbe فرانسوی است که در اواخر قاجار و اوایل پهلوی همراه با واژگانِ پزشکی و بهداشتِ نو وارد فارسی شد؛ «ب» پایانی بازتابِ همخوانِ پایانیِ فرانسوی است و املای «میکرب» بی‌واو، همان املای کهن‌ترِ معین است که نورایی نقل کرده. معین آن را با صورتِ اروپایی و نشانهٔ (بز.) آورده و ترکیب‌هایی چون «میکرب‌کش» و «میکرب‌شناسی» در فارسی بر آن ساخته شده است. به میانجیِ عربی یا عثمانی نیازی نیست، چون زبانِ آموزشِ پزشکی در دارالفنون فرانسه بود.\",\n \"sources\": [EM],\n \"ref_check\": [\n   {\"ref\": \"MON:4500\", \"status\": \"partial\", \"note\": \"The six-volume Moʿin (vol. 4 = foreign compounds, where p.4500 would fall) is not digitised; the two-volume Adena condensation carries the entry 'میکرب: [European headword] (بز.)' (MON_part2.txt line 70425) and many run-on uses (میکرب‌ها, میکرب‌کش, MON_part1.txt lines 4095, 11780, 24869). Content supported, page number unchecked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (2-vol. Adena), s.v. میکرب\", \"stance\": \"supports\", \"note\": \"see ref_check; the entry is tagged as a European scientific loan.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. microbe\", \"stance\": \"supports\", \"note\": \"establishes the French origin and the 1878 date, which fixes the earliest possible date for the Persian borrowing.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20,\n \"lang\": \"English\",\n \"words\": \"microbe, biology, hygiene\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are modern learned formations on Greek material of this root. microbe was borrowed from French in 1878 (node 18). biology is German Biologie (Treviranus and Lamarck, 1802) from βίος + -λογία, borrowed into English 1819. hygiene is French hygiène, from Greek ὑγιεινή (τέχνη) 'the healthful art', from ὑγιεινός, from ὑγιής — the *su-gʷih₃-es- compound of node 17. Watkins/AHD carries the whole set under this root: 'BIO-, BIOTA, BIOTIC; AEROBE, ... MICROBE ...' and 'HYGEIA, HYGIENE'; Klein's article on quick likewise ends 'Cp. also bio-, hygiene ...'.\",\n \"derivation_fa\": \"هر سه ساخته‌های عالمانهٔ نو بر پایهٔ مادّهٔ یونانیِ همین ریشه‌اند: microbe در ۱۸۷۸ از فرانسه وام گرفته شد؛ biology از Biologie آلمانی (تروویرانوس و لامارک، ۱۸۰۲) از βίος + -λογία، که در ۱۸۱۹ به انگلیسی رسید؛ و hygiene از hygiène فرانسوی، از ὑγιεινή (τέχνη) یونانی «هنرِ تندرستی»، از ὑγιής که همان ترکیبِ *su-gʷih₃-es- گرهٔ ۱۷ است. واتکینز همهٔ این‌ها را ذیل همین ریشه فهرست کرده است.\",\n \"sources\": [EM],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent Greek box carries AHD.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷei-, II and IV\", \"stance\": \"supports\", \"note\": \"'BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE ...'; 'in Greek hugiés, healthy: HYGEIA, HYGIENE'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.vv. bio-, biogenesis, microbe\", \"stance\": \"supports\", \"note\": \"'bio-, combining form meaning \\\"life\\\" — Gk. bio-, fr. bios, \\\"life\\\" ... Cp. also ... microbe, hygiene'; the biology-family entries (biogen, biogenesis, biogeny) all stand under it.\"}\n ]\n})\n\nnodes.append({\n \"id\": 21,\n \"lang\": \"Greek\",\n \"words\": \"zoe; zoidion\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"ζωή zōḗ 'life' and ζῴδιον zṓidion belong to the *gʷyō- variant of the root, the one that gave the Greek verb ζῆν/ζώω 'to live': Watkins, 'III. Variant form *gʷyō- (< *gʷyoh₃-). 1. Greek zōē, life: AZO-, (DIAZO). 2. Suffixed form *gʷyō-yo- in Greek zōion, zōidion, living being, animal: (-ZOA), -ZOIC, ZOO-, ZOON, -ZOON'; Pokorny p.468, 'ep. Ionian zṓō, Cret. dṓō \\\"live\\\" (from *gʷyō-yō) ... Attic zō ... zōós \\\"living\\\", zōḗ \\\"life\\\", zōion \\\"animal\\\"'. ζῴδιον is the diminutive of ζῷον, and Nourai's gloss 'carved animal figure' is the concrete sense it has in Greek — a small figure or image of an animal, whence the astrological 'sign of the zodiac': Skeat, 'Gk. zōidiakos, adj., pertaining to animals; Gk. zōidion, a small [figure]; dimin. of zōion, a living creature'.\",\n \"derivation_fa\": \"«ζωή» و «ζῴδιον» به گونهٔ *gʷyō- این ریشه تعلق دارند، همان که فعلِ یونانیِ ζῆν/ζώω «زیستن» از آن است؛ واتکینز: «گونهٔ *gʷyō-: یونانی zōē \\\"زندگی\\\"؛ با پسوند *gʷyō-yo- در zōion, zōidion \\\"جانور\\\"». پوکورنی (ص ۴۶۸) نیز zōós «زنده»، zōḗ «زندگی» و zōion «جانور» را می‌آورد. ζῴδιον مصغرِ ζῷον است و معنایی که نورایی داده («پیکرکِ کنده‌کاری‌شدهٔ جانور») همان معنای عینیِ آن در یونانی است، که از آن معنای نجومیِ «برجِ فلکی» پدید آمده؛ اسکیت نیز همین را می‌گوید.\",\n \"sources\": [EZ],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷei-: 'III. Variant form *gʷyō- (< *gʷyoə-). 1. Greek zōé, life: AZO-, (DIAZO). 2. Suffixed form *gʷyō-yo- in Greek zōon, zōion, living being, animal: (-ZOA), -ZOIC, ZOO-, ZOON, -ZOON.'\"},\n   {\"ref\": \"OEW:135\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984), is lending-only on archive.org (identifiers originofenglish00jose / originsofenglish0000ship, djvu.txt returns 401/403) and search-only on HathiTrust; p.135 could not be opened.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 468\", \"stance\": \"supports\", \"note\": \"'ep. Ionian zṓō, gort. dṓō \\\"live\\\" (from *gʷyō-yō, Indo Germanic *gʷyō-yō) ... Attic zō, zēis, zēi (*gʷyē-), zōós \\\"living\\\", zōḗ \\\"life\\\", zōion \\\"animal\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. Zodiac (SKT.txt line 21833)\", \"stance\": \"supports\", \"note\": \"'Gk. zōidiakos, zodiacal circle; so called from the twelve constellations chiefly [represent]ed by animals. — Gk. zōidiakos, adj., [pertain]ing to animals. — Gk. zōidion, a small [figure]; dimin. of zōion, a living creature.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 22,\n \"lang\": \"English\",\n \"words\": \"zoo, zoology; zodiac\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"zoology is a 17th-century Modern Latin formation zoologia from ζῷον + -λογία; zoo is the clipping of 'Zoological Gardens' (London, 1847). zodiac is older and comes by the Romance route: Etymonline, 'zodiac (n.) \\\"belt of constellations around the ecliptic\\\" ... late 14c., zodiak, from Old French zodiaque and directly from Latin zodiacus \\\"zodiac\\\", from Greek zōdiakos (kyklos) \\\"zodiac (circle)\\\", literally \\\"circle of little animals\\\", from zōidion, \\\"sign of the zodiac, sculptured figure of an animal\\\", diminutive of zōion \\\"animal\\\" (from PIE root *gwei- \\\"to live\\\")'. So Nourai's two-word box is right, and he is right to keep zodiac on the zōidion line rather than the zōē line.\",\n \"derivation_fa\": \"«zoology» ساختی لاتینِ نو از سدهٔ هفدهم است (zoologia از ζῷον + -λογία) و «zoo» کوتاه‌شدهٔ Zoological Gardens (لندن، ۱۸۴۷). «zodiac» کهن‌تر است و از راهِ زبان‌های رومی آمده: از اواخر سدهٔ چهاردهم، از zodiaque فرانسهٔ کهن و zodiacus لاتین، از zōdiakos (kyklos) یونانی «دایرهٔ جانورکان»، از zōidion «نشانِ برج، پیکرکِ کنده‌کاری‌شدهٔ جانور»، مصغرِ zōion. پس جعبهٔ نورایی درست است و به‌درستی «zodiac» را بر خطِ zōidion نشانده، نه بر خطِ zōē.\",\n \"sources\": [EZ],\n \"ref_check\": [\n   {\"ref\": \"OEW:135\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 p.135: lending-only on archive.org, search-only on HathiTrust; not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Zodiac (SKT.txt lines 21828-21833)\", \"stance\": \"supports\", \"note\": \"'Zodiac: see Zoology.' and 'an imaginary belt in the heavens [contain]ing the twelve [signs]. (F. — L. — Gk.) ... L. zodiacus. — Gk. zōidiakos ... — Gk. zōidion, a small [figure]; dimin. of zōion, a living creature.' Skeat files zodiac and zoology together, exactly as this box does.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷei-, III.2\", \"stance\": \"supports\", \"note\": \"'(-ZOA), -ZOIC, ZOO-, ZOON, -ZOON' — the zoo-/zoology family under this root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 23,\n \"lang\": \"Germanic\",\n \"words\": \"kwi-kwaz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *kwikwaz 'alive' continues *gʷih₃-wo- with the regular Grimm's-law treatment of the labiovelars (*gʷ > *kʷ) and a reduplicative-looking assimilation of the second *w to *kw. Watkins reconstructs it as 'Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS'; Klein writes 'fr. Teut. *kwikwa-, \\\"living, alive\\\", fr. I.-E. *gwigwos'. Pokorny p.468 lists the same set: 'Old High German queh and quek, gen. queckes \\\"living\\\", Modern High German keck ... Old English cwicu, cucu \\\"living\\\", Old Norse kvikr, kykr \\\"living\\\"'. Nourai's gloss 'living, full of energy' covers both the inherited 'alive' and the German development to keck 'bold, pert'.\",\n \"derivation_fa\": \"ژرمنیِ آغازینِ *kwikwaz «زنده» دنبالهٔ *gʷih₃-wo- است با تحولِ قاعده‌مندِ قانونِ گریم برای لبی‌کامی‌ها (*gʷ به *kʷ) و همگونیِ واوِ دوم. واتکینز آن را *kwi(k)waz بازسازی می‌کند و انگلیسی کهنِ cwic/cwicu را از آن می‌گیرد؛ کلاین می‌نویسد «از ژرمنیِ *kwikwa- \\\"زنده\\\"، از هندواروپاییِ *gʷigʷos». پوکورنی (ص ۴۶۸) نیز queh/quek آلمانی علیای کهن، cwicu انگلیسی کهن و kvikr نورس کهن را در همین ماده آورده است. معنایی که نورایی داده («زنده، پرجنب‌وجوش») هم معنای موروثی و هم تحولِ آلمانیِ keck «گستاخ» را می‌پوشاند.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gʷei-: 'I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- (< *gʷiə-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER ...'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.v. quick\", \"stance\": \"supports\", \"note\": \"'rel. to OS., OFris. quik, ON. kvikr, \\\"living, alive\\\", Du. kwi(e)k, OHG. quec, chec, cheh, MHG. queck, kec, \\\"lively\\\", G. keck, \\\"bold\\\", fr. Teut. *kwikwa-, \\\"living, alive\\\", fr. I.-E. *gwigwos, fr. base *gwei-, \\\"to live\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 468\", \"stance\": \"supports\", \"note\": \"'With Indo Germanic g-suffix (*gʷi-gʷ-): Old High German queh and quek, gen. queckes \\\"living\\\", Modern High German keck ... Old English cwicu, cucu \\\"living\\\", Old Norse kvikr, kykr \\\"living\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 668-669\", \"stance\": \"supports\", \"note\": \"the gʷei(ə)- article (WLD_Bd1_pages.txt leaves 676-677) carries the same Germanic material (ags. cwīnan, quick-family) that Pokorny abridges.\"}\n ]\n})\n\nnodes.append({\n \"id\": 24,\n \"lang\": \"English\",\n \"words\": \"quick\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English quick is the direct native reflex: Old English cwic, cwicu 'living, alive' > Middle English quik, quike > quick, with the modern sense 'rapid' developing out of 'lively' in Middle English while the old sense survives in fossils — 'the quick and the dead', 'cut to the quick', 'quicksilver' (Old English cwicseolfor, a loan translation of Latin argentum vīvum), and 'quick with child'. Klein sets out the whole history at p.1288: 'quick, adj., 1) living, alive (archaic); 2) rapid, swift ... ME. quik, quike, \\\"alive, lively\\\", fr. OE. cwicu, \\\"living, alive\\\" ... fr. Teut. *kwikwa- ... fr. base *gwei-, \\\"to live\\\"'. This is the one node in the chart where the English word is inherited rather than borrowed, and Nourai has it in the right place.\",\n \"derivation_fa\": \"انگلیسیِ quick بازماندهٔ مستقیم و موروثی است: انگلیسی کهن cwic/cwicu «زنده» به انگلیسیِ میانه quik و از آن quick. معنای امروزیِ «تند» در انگلیسی میانه از «سرزنده» پدید آمده، ولی معنای کهن در ترکیب‌های سنگ‌واره‌ای مانده است: the quick and the dead، cut to the quick، و quicksilver (انگلیسی کهن cwicseolfor، گرته‌برداری از argentum vivum لاتین). کلاین در صفحهٔ ۱۲۸۸ همهٔ این تاریخچه را می‌آورد. این تنها گرهٔ نمودار است که در آن واژهٔ انگلیسی موروثی است نه وام‌گرفته، و نورایی آن را در جای درست نشانده است.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent Germanic box carries AHD, and Klein's p.1288 (cited on node 1) is the article on this very word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.vv. quick, quicksilver\", \"stance\": \"supports\", \"note\": \"'quick, adj., 1) living, alive (archaic); 2) rapid, swift ... ME. quik, quike, \\\"alive, lively\\\", fr. OE. cwicu, \\\"living, alive\\\" ... fr. Teut. *kwikwa- ... fr. base *gwei-, \\\"to live\\\"'; 'quicksilver, n. — ME. quiksilver, fr. OE. cwicseolfor, lit. \\\"quick (i.e. living) silver\\\", loan translation of L. argentum vivum'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. gʷei-, I.1.a\", \"stance\": \"supports\", \"note\": \"'Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt found only 'quick' used as a gloss inside other entries (brisk, accelerate, fast); the OCR of Skeat's own Q section did not surface the headword.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Gwei\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gʷeyh₃- (Pokorny 'gʷei-3, gʷeiə-, gʷii̯ē-, gʷi̯ō-, gʷī-, frequent, often with -u̯- extended') 'to live'\",\n \"note\": \"The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended. Meaning: to live', with 'Page(s): 467-469', so Nourai's 'Gwei : to live' with POK:467 reproduces Pokorny's own heading and page; Watkins in the AHD appendix has 'gʷei-. Also gʷeiə-. To live ... [Pok. 3. gʷei- 467]'; Wiktionary reconstructs *gʷeyh₃- 'to live' (alternative *gʷyeh₃-); Cheung, for the Iranian verb, writes '*jaiH2 ... «PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \\\"to live\\\" © LIV: 215 f. | Pok.: 467 f.'. What is striking about this chart is how much of it is simply Pokorny's own article rearranged: pages 467-469 contain, in order, Avestan gaya- and gaēθā-/Old Persian gaiθā, Avestan jīti- and jīra-, Old Persian jīva-/Avestan jva-, Greek bios, zōḗ, zōion and hygiḗs, Latin vīvus/vīvō/vīta, and Old English cwicu / OHG queh — that is, every branch of the page except the modern coinages. Klein's article 'quick' (p.1288, Nourai's own citation on node 1) carries the same set in one paragraph. Three things need qualifying rather than correcting: the Avestan citation forms in node 1 ('jîta', 'merezu-jîta' for jīti-, mərəzu-jīti-/-jva-); the gloss 'to exist' given to the noun gaēθā- in node 8; and the presence of two 19th/20th-century neologisms ('mikro-bios' in the Greek box, 'vitamine' in the French box) among inherited words. Everything on the Iranian side — zīwistan/zīwandag → زیستن/زنده/ژیوه, the Arabic round trip زیبق, gayō.marətan- → کیومرث, gaēθanąm → gēhān → گیتی/کیهان/جهان, jīra- → زیرک/آژیر — checks out against Horn, Hübschmann, MacKenzie, Nyberg, Bartholomae, Asbaghi and Moʿin's footnotes on the very Borhān pages Nourai cites.\",\n \"note_fa\": \"جعبهٔ ریشه از هر سه جهت درست است: پوکورنی مادّهٔ «gʷei-3 و gʷeiə-…» را با معنای «زیستن» در صفحات ۴۶۷–۴۶۹ آورده، پس هم صورت و هم برچسبِ زبان و هم معنا و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است؛ واتکینز نیز همین را می‌گوید و ویکی‌واژه آن را *gʷeyh₃- بازسازی می‌کند و چونگ در فرهنگِ فعلِ ایرانی ذیل *jaiH₂ همین ریشه را می‌آورد. نکتهٔ چشمگیر این است که بیشترِ نمودار در واقع بازچینشِ همان مقالهٔ پوکورنی است: اوستایی gaya- و gaēθā-، پارسی باستان gaiθā، jīti- و jīra-، jīva-/jva-، یونانی bios و zōḗ و hygiḗs، لاتین vīvus و vīta، و انگلیسی کهن cwicu همه در همان سه صفحه‌اند. سه نکته باید روشن شود، نه اصلاح: صورت‌های اوستاییِ گرهٔ ۱ («jîta» به‌جای jīti-)، معنای نادرستِ «to exist» برای اسمِ gaēθā- در گرهٔ ۸، و حضورِ دو نوواژهٔ سدهٔ نوزدهم و بیستم (mikro-bios و vitamine) در کنارِ واژه‌های موروثی. تمامِ بخشِ ایرانیِ نمودار — از zīwistan تا «زیستن» و «زنده» و «ژیوه»، چرخهٔ «زیبق»، gayō.marətan- تا «کیومرث»، gaēθanąm تا «گیهان/گیتی/کیهان/جهان»، و jīra- تا «زیرک/آژیر» — با هرن، هوبشمان، مکنزی، نیبرگ، بارتولمه، اصباغی و حواشیِ معین بر همان صفحاتِ برهانِ قاطع که نورایی ارجاع داده می‌خواند.\",\n \"sources\": [PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:467\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 38677-38790: 'Root / lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended || Meaning: to live || Material: A. from *gʷei-: Old Indic jīvatu-ḥ \\\"life\\\", gaya-ḥ \\\"house, courtyard\\\" ... Avestan gaēθā, Old pers. gaiθā \\\"entity, house and courtyard\\\" ... References: WP. I 668 ff. ... Page(s): 467-469.' Exactly the root box as drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix s.v. gʷei- (AHD_watkins1985.txt line 540)\", \"stance\": \"supports\", \"note\": \"'gʷei-. Also gʷeiə-. To live. I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- ... [Pok. 3. gʷei- 467.]' — the same root, gloss and Pokorny page.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 668-669 (WLD_Bd1_pages.txt leaves 676-677, running head 'gʷei(ə)-')\", \"stance\": \"supports\", \"note\": \"the source article that Pokorny 467 abridges, with the Germanic and Greek material set out at length ('mhd. verquīnen ... ags. cwīnan ... got. qistjan').\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1288 s.v. quick\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. *gwigwos, fr. base *gwei-, \\\"to live\\\", whence Goth. *qius ... OI. jivah ... Avestic jvaiti ... OPers. jiva- ... Gk. bios ... zōē ... L. vivus ... vita ... OIr. bith, W. byd, \\\"world\\\" ... Cp. also zodiac, zoetic, zoo-.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, *jaiH2, p.223\", \"stance\": \"supports\", \"note\": \"'«PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \\\"to live\\\" © LIV: 215 f. | Pok.: 467 f. *IE COGNATES: Lat. vivo, OCS živǫ, Lith. gyju, Latv. dzīvu \\\"I live\\\", Toch. śaw- \\\"to live\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"grep of SYN.txt for the root shapes produced no clean hit (the OCR mangles the labiovelar notation); Buck's chapter 4.74 'live' was not located in the text file.\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 205,\n \"book_page\": 175,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-205.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build205.py",
 "description": "Write page-205 verification JSON"
}
```


### [2026-09-06T02:43:32.548Z] TOOL RESULT

```
ok 24
```


## [2026-09-06T02:43:37.439Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-205.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 205",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T02:43:39.471Z] TOOL RESULT

```
JSON OK
nodes verified: 24/24
node verdicts: {'transcription_suspect': 1, 'plausible': 6, 'confirmed': 17}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 4, 'not_checked': 9}
books consulted: {'supports': 52, 'silent': 8, 'partial': 7} | by book: {'KLN': 10, 'PHD': 7, 'HRN': 7, 'POK': 6, 'BQT': 6, 'AHD': 6, 'BRT': 4, 'NYB': 4, 'SKT': 3, 'KNT': 2, 'PLA': 2, 'WLD': 2, 'MON': 2, 'IEC': 1, 'HUB': 1, 'CHEUNG': 1, 'AFM': 1, 'ARY': 1, 'WEB': 1}
```


## [2026-09-06T02:44:00.323Z] AGENT

Done — `data/verification/page-205.json` written, valid JSON, `verify_check.py 205` shows **0 PROBLEM lines** (24/24 nodes).

**PDF page 205 (book p. 175) — root Gwei "to live" (one entry, 24 nodes)**

Verdicts: root **confirmed**; nodes **17 confirmed, 6 plausible, 1 transcription_suspect**. Ref checks: 17 supports, 4 partial, 9 not_checked. 19 books consulted.

- Root confirmed exactly: Pokorny IEW 467-469 "gʷei-3 … to live"; AHD/Watkins "[Pok. 3. gʷei- 467]"; Cheung *jaiH₂ = PIE *gʷeiH₃-. Much of the chart is Pokorny's own article rearranged.
- **transcription_suspect — #1 (Avestan/OP) "jîta", "merezu-jîta"**: no Avestan *jīta-; the forms are jīti- f. "life" and mərəzu-jīti-/-jva- "short-lived" (POK 750-751, Bartholomae). `error_in: book` — the printed page shows "jîta" (image saved to `sources/refs/ocr/BOOK/205.png`); extraction is faithful.
- Plausible, with reasons given in the file: #2 (Pahlavi "zivastan" is Horn's 1893 reading of zīwistan; zīwandag means "living", not "mercury" — the metal name is built on it, per Asbaghi p.102 and Moʿin); #8 (gaēθā- is a noun, so the gloss "to exist" is wrong; "existing things"/"cattle" are right); #11 (Avestan form is jīra-, not žīra-; no attested *ā-jīra-); #12 (āžīr's "siren" sense is a 20th-c. Farhangestān revival); #14 (vitamine was coined by Casimir Funk in London 1912, not in French); #17 ("mikro-bios" is not Greek — Sédillot's 1878 French coinage).
- Strong confirmations on the Iranian side: Horn p.212 (the cited page) has both gētīk and gēhān < gaēθā (gaēθanąm); Nyberg "gēhān < *gaiθānām, gen. pl."; Borhān p.1868 and p.1872 (Moʿin's footnotes) confirm گیتی, گیهان and Gayōmart = Av. gayō.marətan (Bartholomae col. 503); Borhān p.~604-606 and ~1038-1040 confirm the ژیوه/زیبق and زنده/زیستن footnotes; Asbaghi p.102 confirms Arabic zībaq ← Persian žīwa ← MP zīwandak; Klein p.1288 (s.v. quick) covers the Latin, Greek, Germanic and Avestan/OP boxes in one article.

**No extraction errors** — the JSON matches the printed page in every box, including the Persian script and the Ferdowsī verse.

Not obtainable: ZMA:21 (Jonaydi, purchase-only), FAF:28 (Daneshgar, not digitised), OEW:135 (Shipley, lending-only). MON page numbers (1768, 4500) unverifiable — the 6-vol Moʿin is not online; content checked in the 2-vol condensation. BQT leaf→page offsets run ~2 pages off Nourai's numbers in vol. 2 (noted in the file).
