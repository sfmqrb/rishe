# Verification process log — verify-page-87


## [2026-09-05T13:45:10.970Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 87 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-87.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-87.json. Write /home/sfmqrb/git/rishe/data/verification/page-87.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 87` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T13:45:12.405Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T13:45:13.105Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T13:45:13.120Z] TOOL RESULT

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


## [2026-09-05T13:45:13.363Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-87.txt"
}
```


### [2026-09-05T13:45:13.377Z] TOOL RESULT

```
1	=== PDF page 87 (book page 57) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhendh : to bind, fasten  (refs POK:127)
4	#1 (parent #0) [Avestan] refs=POK:127; BQT:449 | banda : band, tie ; paiti-band : to attach ☞Per 3
5	  #2 (parent #1) [Persian] refs=AHD:1509; BQT:305; SAP:491 | band «بند» : band, dam ; payvastan «پیوستن» : to attach ; dŭl-band «دولبند» : shawl, turban | extra: پیوند | NOTE: "dŭl: around" is an Arabic term.
6	    #3 (parent #2) [Persian] refs=FVF:98 | darband «دربند» : "enclosed area" ; bandar «بندر» : "enclosed area", port ☞Dhwer | extra: بنادر
7	    #4 (parent #2) [Turkish] refs=PHN:363 | tŭlbend : turban
8	      #5 (parent #4) [French] refs=None | 
9	        #6 (parent #5) [English] refs=AHD:1382 | turban
10	      #7 (parent #4) [Latin] refs=AHD:1380 | tulipa : tulip (due to its turban shape)
11	        #8 (parent #7) [English] refs=AHD; OEW:247 | tulip : this flower was first taken to England in 1575 from Persia via Turkey and Holland.
12	#9 (parent #0) [Old Persian] refs=SOD:105; KNT:199 | bandaka : slave
13	  #10 (parent #9) [Pahlavi] refs=MON:588; KNT:199 | bandak : slave
14	    #11 (parent #10) [Persian] refs=MON:588 | bandeh «بنده» : slave
15	#12 (parent #0) [Avestan / Old Persian] refs=POK:127; AEF:160; HUB:18 | basta : bundled up, fastened ; ham-basta : tied together, interwoven, spider web
16	  #13 (parent #12) [Persian] refs=KLN:152; BQT:164,173,278; AEF:159 | bastan «بستن» : to tie, close ; anbast «انبست» : tied together, dense, coagulated ; anfast «انفست» : spider web
17	#14 (parent #0) [Latin] refs=KLN:152,576 | fascis : bundle
18	  #15 (parent #14) [English] refs=KLN:152 | basket
19	  #16 (parent #14) [Italian] refs=KLN:576 | fascismo : bundle, (a political) group
20	    #17 (parent #16) [French] refs=None | fascism
21	      #18 (parent #17) [Persian] refs=MON:2471 | fâšîsm «فاشیسم» | extra: فاشیست
22	    #19 (parent #16) [English] refs=AHD:477 | fascism
23	#20 (parent #0) [Germanic] refs=AHD | band, binda, bund
24	  #21 (parent #20) [English] refs=AHD | band, bend, bond, bind, bundle, ribbon
25	#22 (parent #0) [French] refs=KLN:146 | bannier : band
26	  #23 (parent #22) [English] refs=None | banner
27	
```


## [2026-09-05T13:45:17.156Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-87.json",
 "description": "Read source JSON for page 87"
}
```


## [2026-09-05T13:45:17.166Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T13:45:17.203Z] TOOL RESULT

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


### [2026-09-05T13:45:17.208Z] TOOL RESULT

```
{
  "pdf_page": 87,
  "book_page": 57,
  "entries": [
    {
      "root": {
        "name": "Bhendh",
        "lang": "Indo-European",
        "refs": "POK:127",
        "gloss": "to bind, fasten"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:127; BQT:449",
          "words": [
            {"translit": "banda", "gloss": "band, tie", "script": null},
            {"translit": "paiti-band", "gloss": "to attach", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AHD:1509; BQT:305; SAP:491",
          "words": [
            {"translit": "band", "gloss": "band, dam", "script": "بند"},
            {"translit": "payvastan", "gloss": "to attach", "script": "پیوستن"},
            {"translit": "dŭl-band", "gloss": "shawl, turban", "script": "دولبند"}
          ],
          "script_extra": "پیوند",
          "note": "\"dŭl: around\" is an Arabic term.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVF:98",
          "words": [
            {"translit": "darband", "gloss": "\"enclosed area\"", "script": "دربند"},
            {"translit": "bandar", "gloss": "\"enclosed area\", port", "script": "بندر", "see": ["Dhwer"]}
          ],
          "script_extra": "بنادر",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Turkish",
          "refs": "PHN:363",
          "words": [
            {"translit": "tŭlbend", "gloss": "turban", "script": null}
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
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:1382",
          "words": [
            {"translit": "turban", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD:1380",
          "words": [
            {"translit": "tulipa", "gloss": "tulip (due to its turban shape)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD; OEW:247",
          "words": [
            {"translit": "tulip", "gloss": "this flower was first taken to England in 1575 from Persia via Turkey and Holland.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SOD:105; KNT:199",
          "words": [
            {"translit": "bandaka", "gloss": "slave", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Pahlavi",
          "refs": "MON:588; KNT:199",
          "words": [
            {"translit": "bandak", "gloss": "slave", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:588",
          "words": [
            {"translit": "bandeh", "gloss": "slave", "script": "بنده"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:127; AEF:160; HUB:18",
          "words": [
            {"translit": "basta", "gloss": "bundled up, fastened", "script": null},
            {"translit": "ham-basta", "gloss": "tied together, interwoven, spider web", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "KLN:152; BQT:164,173,278; AEF:159",
          "words": [
            {"translit": "bastan", "gloss": "to tie, close", "script": "بستن"},
            {"translit": "anbast", "gloss": "tied together, dense, coagulated", "script": "انبست"},
            {"translit": "anfast", "gloss": "spider web", "script": "انفست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "شهنشاهی که خیط شمس گردون - بود بر طاق ایوان وی انفست",
            "poet": "Shams Fakhrî"
          }
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:152,576",
          "words": [
            {"translit": "fascis", "gloss": "bundle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "KLN:152",
          "words": [
            {"translit": "basket", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 14,
          "lang": "Italian",
          "refs": "KLN:576",
          "words": [
            {"translit": "fascismo", "gloss": "bundle, (a political) group", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "fascism", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Persian",
          "refs": "MON:2471",
          "words": [
            {"translit": "fâšîsm", "gloss": null, "script": "فاشیسم"}
          ],
          "script_extra": "فاشیست",
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 16,
          "lang": "English",
          "refs": "AHD:477",
          "words": [
            {"translit": "fascism", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "band, binda, bund", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "band, bend, bond, bind, bundle, ribbon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 0,
          "lang": "French",
          "refs": "KLN:146",
          "words": [
            {"translit": "bannier", "gloss": "band", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 23,
          "parent": 22,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "banner", "gloss": null, "script": null}
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


## [2026-09-05T13:45:22.721Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','AHD','SAP','FVF','PHN','SOD','KNT','MON','AEF','HUB','KLN','OEW','TTS','LKT']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T13:45:23.376Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40 && echo --- && sed -n 1,80p tools/verify_check.py",
 "description": "List verification dir and check script"
}
```


### [2026-09-05T13:45:24.349Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


### [2026-09-05T13:45:24.391Z] TOOL RESULT

```
agent
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
---
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
```


## [2026-09-05T13:46:14.673Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK bhendh ===\"\ngrep -n -i \"bhendh\\|bhendh-\\|bhend\" POK_full.txt | head -20\necho \"=== POK_01 page 127 area ===\"\ngrep -n \"bhendh\" POK_01.txt | head -20",
 "description": "grep Pokorny for bhendh"
}
```


### [2026-09-05T13:46:14.726Z] TOOL RESULT

```
=== POK bhendh ===
9653:Root / lemma: band- {*bhend-) 
9661:band- {* bhend-): "drop' derived from a zero grade of Root/ lemma: au(e)-9, aued-, auer- 
=== POK_01 page 127 area ===
```


## [2026-09-05T13:46:16.741Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins bhendh ===\"\ngrep -n -i \"bhendh\" AHD_watkins1985.txt | head -20\necho \"=== KNT bandaka ===\"\ngrep -n -i \"bandaka\" KNT.txt | head -20\necho \"=== PHD bandag ===\"\ngrep -n -i \"bandag\\|bnd k\\|paywastan\" PHD_mackenzie.txt PHD.txt | head -30",
 "description": "grep AHD, Kent, MacKenzie"
}
```


### [2026-09-05T13:46:16.818Z] TOOL RESULT

```
=== AHD watkins bhendh ===
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
332:grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1288:BEND! bhendh- BEND? bhendh- BENEATH ni BENEDICTION deik-
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
=== KNT bandaka ===
=== PHD bandag ===
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD.txt:1341:connect paywastan.
PHD.txt:2506:join abyóxtan, āyēxtan, (āyēzīdan), paywastan.
PHD.txt:3591:servant bandag, kadagīg, kardespās, paristag, pēškār.
PHD.txt:4615:pattügih pattüg paywastan paywastag pattüdan pahikar 1-2pahikar- pahikardan pahikāf- pahikāftan pahikob- pahikoftan pahikar pahikaf- pahikafián pahikaftan payrastan payrog pahrmāh- pahrmāhāgīh pahrmāhišn paymāy- paymānīgīh paymānīg
PHD_mackenzie.txt:1488:bandag [bndk' 1 P bndg, N ,,-,a] servant.
PHD_mackenzie.txt:4167: paywand-, v. paywastan.
PHD_mackenzie.txt:4171: paywastan, paywand- [ptwstn l , ptwnd- M pywst, (pywyn-), N ......]
PHD_mackenzie.txt:6247:connect paywastan.                           cool down afsardan.
PHD_mackenzie.txt:6895: i,ttelligent frazanag.                       paywastan.
PHD_mackenzie.txt:7565:servant bandag, kadagig, kardespiis,      show nimiidan.
PHD_mackenzie.txt:8534:paywastan              "tbJ     1'" fJ
```


## [2026-09-05T13:46:24.466Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 135 (p.127) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==136' POK_01.txt | head -60",
 "description": "Print Pokorny page 127"
}
```


## [2026-09-05T13:46:25.349Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT leaf 214 (p.199) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==215' KNT.txt | head -60\necho \"=== KNT grep banda ===\"\ngrep -n \"banda\" KNT.txt | head -20",
 "description": "Print Kent p.199"
}
```


### [2026-09-05T13:46:26.218Z] TOOL RESULT

```
=== POK_01 leaf 135 (p.127) ===
enhülse'  (PL  von  holy),  bret; holc'h  ,cosse  de  lin',  vann.  pehl-en  (aus  *pehl-)  ds.,  gall.  bulga  ,Ledersac]i< (daraus  ahd.  hulga  ,lederner  Wasserbehälter*);  gall.  Belgae  ,die  Zornigen^
got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
aisl.  Partiz.  bolginn  ,geschwollen',  Kaus.  belgja  , aufschwellen  machen' as.  ags.  belgan  St.-V.  ,zornig  sein',  ahd.  belgan  ,aufschwellen',  refl.  ,zö^ nen',  afries.  Partiz.  ovirbulgen  ,erzürnt';
aisl.  bylgja  ,Woge',  mnd.  bidge  ds. ;  *bul{h)stra-  in  aisl.  bolstr  m.  ,Kisseii' ags.  bolster  n.  ,Polsteri  Kissen',  ahd.  bolstar  ds.,  ndl.  bolster , Fruchtbalg,  Hülse'
apr.  balsinis  ,Kissen'  (*bholghi-nos),  pobalso  , Pfühl',  lett.  pabälsts ,Kopfkissen'  (und  , Stütze',  s.  oben  S.  123);  slov.  blazina  ,Kissen,  Matratze] Bettpfühl;  Fuß-  oder  Handballen'  (und  , Dachbalken,  Querbaum  des* Schlittens,  Rungstock',  s.  oben  S.  123),  skr.  blazina  , Kopfkissen,  Polster^ti Federbett';  russ.  bolozem,  m.  , Schwiele,  Beule,  Leichdorn,  Hühnerauge^! (aber  russ.  dial.  bölozno  , dickes  Brett').  Hierher  wohl  als  ven.-ill.  Lw.^t apr.  balgnan  n.,  alit.  balgnas,  lit.  balnas  , Sattel'  (wohl  aus  ,Kissen').  Weitere  ' baltoslav.  Formen  s.  oben  S.  123.  -|
WP.  II  182  f.,  WH.  I  122.  Vgl.  über  gr.  nolyog  ,Ledersack'  Vendryes BSL.  41,  134  f.
bhen-  ,schlagen,   verwunden';    auch  von    durch    den   Schlag   böser   Geister bewirkter  Krankheit  (avest.;  vgl.  zu  diesem  Aberglauben  Havers  IF. 25,  380  f.) Av.  bqnaydn  ,sie  machen  krank',  banta-  , erkrankt,  siech'; got.  banja  , Schlag,  Wunde,  Geschwür',  aisl.  ben,  ags.  benn  f.,  as.  beni- tüunda   ,Wunde';    aisl.  bani   m.  ,Tod;    Mörder',   ags.  bana^    ahd.    as.  bano ,Totschläger,  Mörder',  ahd.  bano,  mhd.  hane,  ban  ,Tod,  Verderben';    viel- leicht auch  mhd.  bane,  ban  f.  und  m.  ,Bahn,  Weg'  als  ,*Durchhau  durch einen  Wald'  oder  ,*festgeschlagener  Weg';   mir.  epit  f.  , Hippe'  aus  *ek8- bhen-tl-  corn.  bony  ,Axt';  aber  cymr.  &on-cZws^ , Ohrfeige' enthält  bon  , Stock'. Av.  bata-j  wenn  ,geschrotet,  vom  Getreide',  könnte  als  *bhn-to-  verwandt sein,  ist  aber  wegen  der  unsichern  Bed.  nur  mit  Vorbehalt  zu  nennen. WP.  II  149,  Feist  80.
bbend'  etwa  ,singen,  schön  klingen,  jauchzen'.
Ai.  bhandate  , empfängt  jauchzenden  Zuruf,  wird  gepriesen,  glänzt', bhdndi§tha-h  ,am  lautesten  jauchzend,  gellend,  am  besten  preisend',  bhan-
w
127
. ,  ^,^    jauchzend^,  bhanddnä  , lustiges  Tönen,  Jauchzen^  (die  Bedeutungen T    bezweifelt);    schwundstufig    air.   mir
```


### [2026-09-05T13:46:27.772Z] TOOL RESULT

```
=== KNT leaf 214 (p.199) ===
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahyu- sb. ‘land, province, district’: GAv. :
daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘stranger, demon’ (5124.2, $153.IV, $166). Decl., 5183.1. See also visadahyu-.
dahyaus nsf. AmH 5, 8f (as Isf. §814b); DB 1.59; 2.28, 58, 59, 72; 3.9, 11, 20, 28, 66, 75, 79f; 5.4, 13f, 29f; DPd 6. dahydus-maty DB 4.39. dahyüum asf. (853, $72) AsH 8, 11, 13; DPd 15, 18; DNa 53. dahydvam (8124.VY) XPh 88, 58f. dahyaud (dahyuvd Wb.) isf. (M8, §124.2, 8137) DB 1.34.
dahyàva прі. ($124.7) DB 1.18, 17, 18, 28, 41; 2.6°; 4.33; DPe 7, 14; РМа 17, 39; DSe 15f, 32f; DSm 5°; XPh 15. dahyáva apf. DB 1.21, 47, 67; 4.92, XPh 31,35. dahyünüm gpf. DB 1.2; DBa 3; DPa 4; DPe 3; DNa 10; DSb 6f; DSe 9°; DZb 2{°, DZc 5; DE 15; XPa 7f; XPb 15; XPc 7; XPd 10f; XPf 10; XPh 8f; XSc 2°, ХЕ 15; XV 111; А:Ра 11f°; A’Sc 3f; Wb 5; We 6; Wd 6. dahyüv- näm (523.11) РР} 2; DH 1f. dahyusued lpf. DB 1.35.
DHum (842) asf. DSf 58; DSj 6°. DHyaum (553) А2Рә 26. -DHnám gpf. DSa 2; DSd 1; DSf 6; 056 1^; D8i 4°; DSk 2; РӘ 2°. DHyünam
LEXICON
DSy 2; ХР); АЧ; D'Sb 1; A’Sa 1; А84 1; А?На 1°; А?Не 8; A?Pa 11.
idi- vb. ‘see’: Av. *dá(y)- ‘see’ (Bthl. AW 124), NPers. diddn, Skt. dhi- ‘think’. didzy 2d sg. mv. (865, $129, 5209, $218.II, $237.1) DNa 41; DNb 57.
*di- vb. ‘take by force (a thing from a person, 2 acc.), deprive (a person of a thing, 2 acc.)’: Av. zinditi ‘harms’ (zyà-, Bthl. AYW 1700), Skt. jináti ‘oppresses’, jdyati ‘conquers’ ($88), ef. Gk. Bia ‘violence’. айтат Ist sg. imf. (5210.1, $226.II) DB 1.59. айта imf. (5210.1, $228.IT) DB 1.44f, 46, 66. ditam asm. past ріс. pass. (82421) DB 1.50. |
-di- enel. pron. ‘him, them’, usually with masc. antecedent: Av. di- (Bthl. AiW 684); start- ing by wrong division of pasdvad-im etc., where -im is acc. to *is, Lt. is, and extended (§195.II; Caland, KZ 42.173; Mt. MSLP 19.535, Gr. $166); on competition with pron. -%i-, see Bv. Gr. 645.
-dim asm. (5195.1) in pasdva-dim (with fem. an- tecedent) DNa 33; anu-dim DNb 16, 18; avabá- dim DNb 17; hau-dim ВЕ 32.
-diš apm. (8195.1) in tyà-di$ DB 1.65 (with collective sg. masc. antecedent); nazy-di& DB 4.78, 18; paribarüh?-di$ DB 4.74; vikanah*-dis DB 4.77; avafà-di$ DB 5.17, 33; ava-di$ DNa 21, DSe 20°, XPh 19; 00-015 DNb 46f (with nt. antecedent); hau-di$ DSs 6° (with antecedents of different genders). Written as separate word in drauga diš DB 4.34 (with fem. antecedents); pasdva diš DB 4.35; avaba diš DB 4.36.
daiy DB 5.11, as separate word, properly vi? with wrongly inserted divider following; read viy- ататда with Wb. ZfA 46.55, see under mard- (not apm. with Kent, JAOS 62.278; not gen.-dat. sg. with Wb. KIA 73n, Bv. Gr. $845, Gray AJP 53.69).
-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
didà- sb. ‘wall, stronghold, fortress’: N Pers. diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos,
191
NEng. dike, ditch (676.011, 588, §148.IV, 5166). Cf. also paradayadàm. й nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didäm asf. DB 2.78; DSe 48°; DSf 54.
dipi- sb. ‘inscription’: Elam. tup-pi, Akk. duppu (5152.1): borrowed from Sumerian dup- (Ву. Gr. §282; hardly contamination of Jran. *ripi- = Skt. lipi- ‘smearing, writing’, with Sum. dup-, as taken by Pisani, Riv. Stud. Or. 14.320, as Skt. lipi- ‘writing’ indicates writing with ink rather than engraving on stone) 4:4] nsf. DB 4.90, 91f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447.
dug- vb., see hadugá-.
Dubála- sb. ‘Dubala’, a district in Baby- lonia: Elam. du-ib-ba--- ($6, $107). Dubala пет. DB 3.79.
dūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dü
=== KNT grep banda ===
629:§39. Ошо Persian NASALS BEFORE CONSO- NANTS were omitted in the writing, except before y and v; such omitted sounds may be repre- sented by raised letters in the normalized tran- scription, when desirable: Лу = ha*tiy, Skt. sánti; kbujiye = Ka"büjya ‘Cambyses’, see Elam., Akk., Gk. transcriptions in Lexicon; bodeke = ba"daka, Phi. bandak; ера? = Ка"- pa"da, Elam. qa-um-pan-ias.
1393:Skt. sindhu-. afa"ga- ‘stone’, Av. asanga-. ba"daka ‘servant’, Phi. bandak, NPers. bándáh. a^lar ‘inside’, Skt. antár, Lt. inter.
5725:ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
```


## [2026-09-05T13:46:39.284Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_01 leaf 137 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==137' POK_01.txt | head -50\necho \"=== KNT page of line 5725 ===\"\nawk 'NR<=5725' KNT.txt | tr -cd '\\f' | wc -c",
 "description": "Pokorny bhendh entry + Kent page calc"
}
```


## [2026-09-05T13:46:40.704Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT banda ===\"\ngrep -n \"banda-\\|bandayeiti\\|paiti\\.band\\|basta-\" BRT.txt | head -30",
 "description": "grep Bartholomae"
}
```


### [2026-09-05T13:46:41.103Z] TOOL RESULT

```
=== POK_01 leaf 137 ===
.   bind    , melodisch^,    abret.  bann
canora^ '    WP.  II  151  f.
^eadh'  ,binden^
;^i.  hadhnäti,  erst  später  bandhati  ,bindet,  fesselt,  nimmt  gefangen, i\\iri  zus/,  av.  bandayaiti  , bindet',  Partiz.  ai.  baddhd-,  av.  ap.  basta-,  ai. hdndhana-  n.  ,das  Binden',  bandkd-h  m.  ,das  Binden,  Band',  av.  banda-  m. Bande  Fessel'  (:  aisl.  as.  bant,  ahd.  bant  n.,  nhd.  Band ;  got.  bandi,  ags. l^end  f.  ds.;  lit.  Jant^a , Vieh',  s.  unten);  ai.  bdndhu-h  m.  ,Verwandter'  (wie jfsydsQÖg).
Gr.  ftstcfia  ,Tau,  Seil'  (aus  *7tsv^a^a,  Schwyzer  Gr.  Gr.  I  287,  vgl. Bru<^mann  IF.  11,  104 f.,  auch  für  jtsa^ia  und  rcdafia),  ^tev&SQog  , Schwieger- vater* (*,durch  Heirat  verbunden') ;  hierher  nach  Pedersen  (REtlE.  1,  192) auch  ftdaxo)  , leide'  als  , werde  gebunden,  verstrickt',  wie  auch  lat.  offendö o-erate  ins  Unglück,  stoße  an',  defendö  ,lÖse  aus  der  Verstrickung';  Ttd&vr] (spät  belegt,  aber  alt),  mit  Hauchumstellung  hom.  att.  cpdrvr]  , Krippe' (Hhndh-nä'j  unter  einer  Gdbed.  ,geflochtener  Korb'  wie  kelt.  benna ,Wagenkorb');  thrak.  ßevd-  ,binden'  (vgl.  Kretschmer  Einl.  236);  alb.  bese , Vertrag;  Glaube,  Waffenstillstand';  lat.  offendimentum,  offendix  ,das  Kinn- band an  der  Priestermütze';  gall.  benna  ,genus  vehiculi',  galat.  Zeig  Biv- yiogj  cymr.  benn  ,Fuhrwerk'  (daraus  ags.  binn,  und  durch  roman.  Vermitt- lung nhd.  dial.  benne  , Wagenkasten',  ndl.  ben  ,Korb,  Mulde';  Gdf.  Hhendh- nä)'j  mir.  buinne  ,Band,  (Arm)reif'  (*bhondhia)]
got.  ags.  bindanj  aisl.  binda,  ahd.  bintan  ,binden',  got.  andbundnan  ,ge- löst  werden',  got.  bandi  usw.  s.  oben;  lit.  bendras  ,Teilhaber,  Genosse' (formantisch  gr.  Ttsvd-SQÖg  nahestehend),  bandä  ,Viehherde'  (eig.  ,das  an- gebundene Vieh').
Hierher  auch  got.  bansts  m.  , Scheuer'  (*bhondh-sti]  vgl.  in  anderer  Bed. afries.  böst  , eheliche  Verbindung'  aus  *bhondh-stu-  , Bindung';  ndd.  banse ,Kornraum,  Scheune',  ags.  *5ös,  engl,  boose  ,Viehstall',  ags.  bösig  ,Krippe', aisl.  bäss  m.  ,Raum  zum  Aufbewahren,  Viehstand'  {*band-sa-)',  jüt.  bende ,abgeteilter  Raum  im  Viehstall'  schließt  wohl  jeden  Zweifel  an  der  Ver- wandtschaft obiger  Gruppe  mit  binden  aus.
WP.  II  152,  WH.  I  102,  Feist  79,  80  f.,  93.
bbcngh-,  bhngh-  (Adj.  bbngbü-s)  ,dick,  dicht,  feist'.
Ai.  baJiü-  , dicht,  reichlich,  viel'  ,Komp.  Sup.  bamhlyas-,  bamhistha-  (= gr.  Ttaxvg)]    bahuld-  ,dick,  dicht,  ausgedehnt,  groß^  reichlich,  viel' (=  gr.
128
rtaxvKbg   Adv.  bei    Aristot.,    wenn   dies   nicht   jüngere    Bildung);    hdniha^'i (unbelegt)  ,mebrt  sich',  hhdrhhayate  ^befestigt,  stärkt';
av.  bazah-  n.  ,Höhe,    Tiefe',    basnu-  m.  ds.,   bal.   häz  ,viel',    baz  ;dicht'
gr.  Ttaxvg    ,dick,  dicht,  feist'   (Komp.  fc&aoiov),  na^oq   n.   ,Dicke'   (naci Ttccxvg  für  *7t6yxoQ  =  av.  bazah-  eingetreten),  näxeTog  ,dick;  Dicke';
aisl.  bingr  ,Haufen',  aschwed.  binge  ds.,  ahd.  bungo  ,Knolle',  nhd.  Bac) bunge]    dazu    mit   intens.  Kons.-Schärfung   aisl.    bunki    ,verstaute    Schiffst ladung',  norw.  bunka  (und  bunga)  ,kl
=== KNT page of line 5725 ===
223
```


### [2026-09-05T13:46:41.147Z] TOOL RESULT

```
=== BRT banda ===
11372:üyatis  axsaia  kauHy  .  .  mrasatiy  . .  D. 5.  3.  b)  im  Aw.:  ya  maninumlit  mya- dinqm  ..  upa.vaz^ilte  YL/_J.  64;  —  huxsa- "^röJfMäi^it  at  xsäir^m  illyät  yat  ahurai A.3,6;  —  nitjin»m(sd.)^it"^  apjrinayükim V.  j?.  38;  —  yä  umm  (sd.)  p»r?7Um  k»T3- naoiti  p?r7n^m/it  viyzärayäti  (sd.)  V.  22. I  s;  —  avatUim^il  bandayeiti  bantsmca  drütn I  ksrmaoiti  V.  22.  j ;  —  äsnqmlit"^  frasain- '  tm  Yt  10. 108,  1 10,  Y.  ö^.  1 1 ;  —  asnas- ät"^  xraitts  Yl  10. 107 ;  —  darrf^mUt"'' aipi   srvatum   Y.62.  3,  Yt/(J.  z6;  JJ.  54;
16676:banda-
16696:•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
16698:•  j.,  p. "band- V, 'binden'.  Pr^es.  8  *ba»ad-z band-'\  34  bandaya-.  —  PPfP.  basta-'^.
16709:•  j.  'baaha-  Adj,  'narkotisirt,  trunken':^  Kaus.'krankmachen':4*<'f(.._v^..aj'<M- damm  kundsm  -hftn  vJ.banh^  (sd.)  "^ .  t?mcit  bandayeiti  bant>mca(%t.)  drüm  km- '5-41-  naoiti  V.  22.  g-
16712:bqnaya-'\  —  PPfP.  banta-  (sbes.).  •  j.    (,   p.)   banda-    m.  'Bande,    Fessel':
17044:•  j.,  p.  basta-  Adj.  (fem.  •«■),  PPfP.: s.  'band-,
22390:'führen,  ziehen,  schleppen':  ^o^a  banda- yeni  ..franrasyänim  Uta  baitsm  vä%aymi Yt.p.  18;  ^yat ..  baslB  atakat  väiayamnS (pass.)  Yt  15.52;  —  z'itansi}  (sd.)  datvS .  .  urvämm  bast?m  väliayeiti  W.ir/.ti).
28803:•  j.  'haosravah-  m.  EN.  eines  irani- schen Königs  aus  der  A'uz'aj'dyiiastie:  arsa airyanqm  dahyunam  xJdhrai  hanktr^mH (sd.)  'va  (NS.)  Yt.5.49.  a)  sonst  mit kavay-:  ayaslam  amahrkim  bavdhi  ydkia kava  *'va  Az.7'>;  *Vyt.2'';  —  haomS .  . him  ja^yal . .  dazdi  mL.ya'ia  aam  banda- yeni  . ,  läirTm  fraarasyämm  . .  uta  bastftn upanayeni  bastsm  kavSi^  'vanhahe^  janäi t>m  kava  'va  .  .  pu%rü  iama  (sd.)  syä- var/anäi  Yti).  i7f.;  /p.77,  93,  ^5.32;  — ahurS  kava  'va  Ytig.yj;  —  uynm  ia- valm  i^amiS  .  .  yat  upa^hacat  kavaltn •vanhitn  Yt /p.  73f.;  S. /.  9;  —  yc^a  as>m uzayeni  ha^a  iavlfis 'vamkahe'^  Yt.  15.  2^ ; Ny.  J.  S ;  —  kavsis  kaosravatihs  ai'aonS  Yt J.?-i3a-
```


## [2026-09-05T13:46:54.244Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT col near banda ===\"\nsed -n '16670,16700p' BRT.txt | head -40\necho \"=== BRT paiti band ===\"\ngrep -n \"paiti\\.band\\|paitibanda\\|paiti-band\" BRT.txt | head -10",
 "description": "Bartholomae context"
}
```


### [2026-09-05T13:46:54.308Z] TOOL RESULT

```
=== BRT col near banda ===
■•Erweiteniiig'  ans  ia^-,  sd.;  S  1?ft  5-  —  "P- inssiäaH  'schenken'.  —  Pü.:  iaxiilani  s.  noch No.  1,  a,  5.  —  ■)  Pfi,  «L:  i'ästai  tu  pa  api- yasi  I  15  därrnd.  —  i>  D,  i.  das  jetit  noch lut  falschen  Religion  hälL  Pü.  etl.:  kti  an andar  därisn  afi  stänend.  —  3)  Vgl,  N.  /tf nnter  2.  Falsch  Dsr.  ZA.  /.  104.  —  *>  Ganz falsch  DsT.  ZA.  2.  144;    Tgl.  Hbm.  PSl  131
tn  np.  daxiüdan.  —  5)  Vgl.  zSL  Gun.  KZ.  JO. SI8.  Pü.  erl,:  ö  ariämUn.  —  *)  F I.  NA. "hA.  —  7)  An  den  folgenden  NP.  des  Pron. rel.  —  8)  Gdn.  BB.  l£.  258  will  'lurückgeben, vergelten'.     Das  väre  aber  doch  eher  paitiJf.
•  j.  bata-  Adj.  'geschrotet',  vom  Getreide:
dby  Google
9^5
bawra-
banda-
926
manä  'ks  (NPf.)  äh^is  ".  .  die  .  .  mir untertaa  waren"  Bh.  /.  7 ;  —  dadarÜs  .  . Manä  'ia*  Bh.^,  3,  2.  7;  6,  10,  14,^.6,  9, 14.  5- 1.
Eig.    'der   Qemands)  Fesseln  trägt'.   —    np.
ianfl'fl  'Sklave'.
•  j.  bawra-  m.
%risatanqm  'rc
"Biberkleider  1
Ytj.  129- Ableit.  ■ ahd.  bibar;
'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
)  Vgl.  ^baufray;  ^    mp.  b<ne/rat, .    a.  vgl.  babkräii-   Adj.    'rotbraan', auch  Tiernanie;  1.  noch  GlrPh.  /  b.  49.
•  j.  'bawray-m.'Biber',  f. 'Biberweibchen': yat  asti  'ris  sragsta  yä^a  yat  asti  gaonS.- t?ma  'ris  öavaili  upäpö  "da^  Biberweibchen ist  am  schönsten,  insofern  es  am  dichtesten behaart  ist;  der  Biber  ist  ein  Wassertier" Yt.5.129').
VgL  baniro;  —  ")  Ich  halte  das  Game  für spätere  Zotat,  nicht  nur  die  letzten  drei  Worte.
•  j.  Tiawray-  m.  Name  einer  Stadt, Babylon:  tarn  yazala  aus'..  dahakB  TSil\ paiti  daifihaove  Yt.  5.
VgL  iSiirav-.
•  j.  bawrinay-  Adj,  'vom  Biber  stammend, Biber"';  'wraini'^  (APn.)  vasträ  .  ,  Sma- tanam  bauiranqtn  (sd.)  Yt.5.  129.
Ableit.  aus  bawra-.  —  Vgl.  lit  bibrinis  {io- Stamm).  —  ')  Statt  •■wrim  geschr.,  S  ^S.  9. (S.  noch  ipmaiiil,  liispö .tailü,  iailayc^
•  j.  'baoha-,  bangha-''>  m,  i)  Name einer  Pflanze*'  (und  deren  Saft),  die  auch zur  Kind  sab  treibung  benutzt  wurde:  asia kana  frabaraiti  'him  vä  iaffym  vü  .  . kqmcii  Vä  vTtaananqtn  urvaranqm  V.  i^. 14.  z)  Name  eines  aus  jener  Pflanze hergestellten  Narkotikums '>  und  zugleich
dvär^nts  yä  bqnayitt  ahüm  maniSnS  "zu- sammen gingen  sie  darauf  zu  A.  über, durch  den  sie  das  Leben  der  Menschen krank  machen"  Y.^jo.ö".
Vgl.  got.Äoiy o 'Wunde',  ahd.  *a«fl' Verderben'». —  S.  auch  'band-.  —  Pü.;  vimärhtilan,  erl. : ähökcmian.  —  ■>  S  3g6.  3.  —  ')  Vgl.  dagegen IQ  ^aAümM-.  —  j)  Doch  a.  Zupitza  Gu(t,  30.
•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
KompE.  (fl*%  av).  —  PHP.  wm  V,  ian-,  — Vgl.  bazda-.  —  Pfi.:  vimär.
•  j.,  p. "band- V, 'binden'.  Pr^es.  8  *ba»ad-z band-'\  34  bandaya-.  —  PPfP.  basta-'^.
r)  'binden,  fesseln':  is'ar  pasca  puxl>m bandum  (sd.)  bandyät^''  Vd./3;  —  dazdi tm  .  .  ydha  .  .  bandayem  .  .  franrasyämm Uta  basttm  vätayeni  uta  bastfm  upana-
\yeni  bast?m  ,  .  Yt.5,  '^J  —  haosrava  .  .
=== BRT paiti band ===
```


## [2026-09-05T13:46:55.959Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN basket ===\"\ngrep -n -i \"^basket\\|basket, n\" KLN_1966.txt KLN_1971.txt | head -10\necho \"=== KLN fascis/fascism ===\"\ngrep -n -i \"fascism\\|fascis, \" KLN_1966.txt | head -10\necho \"=== KLN banner ===\"\ngrep -n -i \"banner\" KLN_1966.txt | head -10",
 "description": "grep Klein"
}
```


### [2026-09-05T13:46:56.051Z] TOOL RESULT

```
=== KLN basket ===
KLN_1971.txt:26572:basket, n. — ME., fr. L. bascauda , ‘a brazen ves- 
KLN_1971.txt:34801:buck basket, n., a laundry basket. — See buck, 
KLN_1971.txt:37002:basket’, and rel. toxXw&etv, ‘to spin’. See Clotho 
KLN_1971.txt:38522:basket’, fr. Gk. xavaorpov, fr. xawa, ‘reed’. 
KLN_1971.txt:93320:basket, purse; treasury’, which stands for *bhid- 
KLN_1971.txt:152755:basket’, OE. txnen , ‘of twigs’, Norw. teinen, 
KLN_1971.txt:229070:basket’ (whence L. sporta, sportula, of s.m.), 
KLN_1966.txt:4520:basket,  n.  —  ME.,  fr.  L.  bascauda,  ‘a  brazen  ves¬ sel’,  referred  to  by  the  Roman  poet  Martial  as  an OBrit.  word;  cogn.  with  L .  fascis,  ‘bundle,  fag¬ got’  ;  see  fasces.  The  orig.  meaning  of  bascauda was  prob.  ‘wicker  basket’, bason,  n.  —  A  variant  of  basin.
=== KLN fascis/fascism ===
4520:basket,  n.  —  ME.,  fr.  L.  bascauda,  ‘a  brazen  ves¬ sel’,  referred  to  by  the  Roman  poet  Martial  as  an OBrit.  word;  cogn.  with  L .  fascis,  ‘bundle,  fag¬ got’  ;  see  fasces.  The  orig.  meaning  of  bascauda was  prob.  ‘wicker  basket’, bason,  n.  —  A  variant  of  basin.
4528:bast,  n.,  the  inner  bark  of  the  linden  tree.  —  ME., fr.  OE.  beest,  rel.  to  ON.,  OS.,  MDu.,  OHG., MHG.,G.,‘harf’,OHG.6ei/e«, ‘to  sew  with  bast’, and  prob.  cogn.  with  L.  fascis,  ‘bundle’,  see  fas¬ ces.  OE.  bxst,  etc.,  orig.  meant  ‘that  which  serves for  binding’.  OF.  bastir  (whence  F.  batir ),  ‘to build’,  is  a  loan  word  fr.  Frankish  *bastjan,  and orig.  meant  ‘to  sew  or  bind  with  bast’.  Cp.  baste, 'to  sew  loosely’.  Cp.  also  bastille,  bastion,  and the  second  element  in  bundobust.  For  sense  de¬ velopment  cp.  G.  Wand,  ‘wall’,  which  is  rel.  to wenden,  ‘to  turn,  twist’  (see  wand).
14406:fasces,  n.  pi.,  a  bundle  of  rods  containing  an  ax, carried  before  Roman  magistrates,  as  a  symbol of  authority.  —  L.  fasces,  ‘bundles’,  pi.  of fascis,  prob.  cogn.  with  Mir.  base,  ‘neckband’, W.  baich,  ‘load,  burden’,  OBrit.  bascauda,  ‘rins¬ ing  bowl  of  brass’,  Maced.  Gk.  fSamaoi  (pi.), ‘bundle  of  wood’,  OE.  bxst,  ‘inner  bark  of  the linden  tree’.  See  bast  and  cp.  basket.  Cp.  also fascia,  fascicule,  Fascism,  fess. fascia,  n.,  band;  a  horizontal  part  of  the  archi¬ trave  ( archit .)  —  L.,  ‘band,  fillet,  bundle’,  fr. fascis,  ‘bundle’.  See  prec.  word, fasciate,  fascia  ted,  adj.,  bound  with  a  band; grown  together.  —  L.  fasciatus,  pp.  of  fasciare, ‘to  bind  with  a  band,  to  swathe’,  fr.  fascia.  See prec.  word  and  the  adj.  suffixes  -ate  and  -ed. Derivatives:  fasciale-ly,  adv.,  fasciate-ly,  adv., fasciat-ion,  n.
14410:fascicule,  n.,  fascicle.  —  L.  fasciculus.  See  fascicle, fascinate,  tr.  v.,  to  attract,  charm.  —  L.  fasci- ndtus,  pp.  of  fascinate,  ‘to  enchant,  bewitch, charm’,  fr.  fascinum,  ‘charm,  witchcraft’,  which was  prob.  borrowed  fr.  Gk.  fldcoxavoi;,  ‘sorcer¬ er’,  but  was  later  formally  associated  with  L. fari,  ‘to  speak’,  or  with  L.  fascis,  ‘bundle’.  Gk. [Hdcoxavo {  (whence  paarxatveiv,  ‘to  bewitch’), prob.  derives  from  a  Northern — possibly Thracian — equivalent  of  Gk.  ipaoxsi v,  ‘to  say’, fr.  I.-E.  *bhe-sko-,  pres,  tense  enlargement  of base  *bha-,  ‘to  speak’,  whence  Gk.  qpirjfu,  ‘I  say’, 97}|iri,  ‘a  voice,  report’,  L.  fama,  ‘report,  rumor, tradition,  reputation’,  fari,  ‘to  speak’.  See  fame and  verbal  suff.  -ate.  L.  fascinum  is  not  related to  L.  fascis,  ‘bundle’.  See  Walde-Hofmann, LEW.,  I,  459,  and  Frisk,  GEW.,  I,  223-224.  For the  sense  development  of  Gk.  paerxavo?,  ‘sor¬ cerer’,  paaxalveiM,  ‘to  bewitch’,  from  a  base meaning  ‘to  speak’,  cp.  G.  besprechen,  ‘to  speak of;  to  charm’,  fr.  sprechen,  ‘to  speak’. Derivatives:  fascinat-ed,  adv.,  fascinal-ed-Iy, adv.,  fascinal-ed-ness,  n.,  fascinal-ing,  adj., fascinat-ing-ly,  adv.,  fascination  (q.v.),  fascinat- ive,  adj.,  fascinat-or,  n.
14411:fascination,  n.  —  L.fascinatid,  gen.  -dnis,  h.fasci- natus,  pp.  of  fascinare.  See  prec.  word  and  -ion. fascine,  n.,  a  bundle  of  sticks  used  to  fill  ditches, etc.  —  F.,  fr.  L.  fascina,  ‘a  bundle  of  sticks, fagot’,  Hr.  fascis,  ‘a  bundle’.  See  fasces  and  subst. suff.  -ine.
14412:Fascism,  n.  —  It.  fascismo,  formed  fr.  fascia, ‘bundle;  political  group,  organization’,  fr.  L.
=== KLN banner ===
4361:band,  n„  troop.  —  F.  bande,  fr.  OProven?.  banda, fr.  Goth,  bandwa,  bandwo,  ‘sign,  signal’.  See banner  and  cp.  disband.
4365:banderilla,  n.,  a  small  dart  with  a  streamer  thrust into  the  bull  by  the  banderillo.  —  Sp.,  dimin.  of bandera,  ‘banner’.  See  banner  and  cp.  next  word, banderole,  banderol,  n.,  a  small  streamer  at¬ tached  to  a  lance.  —  F.  banderole,  dimin.  of bandore,  banniere,  ‘banner’.  See  banner  and cp.  prec.  word.
4368:bandicoot,  n.,  a  kind  of  a  large  rat.  —  Telegu pandi  kokku,  lit.  ‘pig  rat’, bandit,  n.  —  F.,  fr.  It.  bandito,  prop.  pp.  of  ban- dire,  ‘to  banish’,  which  arose  from  a  blend  of Frankish  *bannjan ,  ‘to  banish’  (whence  F.  ban- nir,  E.  banish),  and  Goth,  bandwa,  ‘sign,  signal’. See  banner.
4386:banish,  tr.  v.  —  ME.  banishen,  fr.  OF.  baniss-. pres.  part,  stem  of  banir,  ‘to  proclaim ;  to  banish" (F.  bannir,  ‘to  banish;  to  expel"),  fr.  Frankish *bannjan,  which  is  rel.  to  Goth,  bandwjan,  ‘to make  a  sign,  to  signal’,  whence  It.  bandire. OProveng.  bandir,  ‘to  proclaim:  to  banish’.  See banner  and  cp.  band,  ‘troop’.  For  the  ending  see verbal  suff.  -ish.  OF.  banir,  etc.,  were  influenced
4395:Banksia,  n.,  a  genus  of  Australian  evergreen trees.  —  Named  after  the  famous  English  na¬ turalist  and  traveler,  Sir  Joseph  Banks  (1743- 1820).  For  the  ending  see  suff.  -ia. banner,  n.  —  ME.  banere,  fr.  OF.  baniere  (F.  ban- nitre),  which  is  prob.  a  blend  of  WTeut.  *banda, corresponding  to  Goth,  bandwa,  bandwo,  ‘sign, signal’  (whence  also  It.,  OProveng,  banda,  ‘band, troop’.  Late  L.  bandum,  ‘banner’,  banderia,  ba- neria,  ‘place  where  the  banner  is  set  up’,  OPro¬ veng.  bandiera  (whence  It.  bandiera,  F.  han¬ dier)’.  Sp.  bandera),  ‘banner’,  and  of  OF.  ban, ‘public  proclamation’.  Goth,  bandwa,  prob.  de¬ rives  fr.  I.-E.  base  *bendh-,  ‘to  bind  .  See  band, ‘tie’,  and  cp.  band,  ‘troop’,  banderilla,  banderole, banish,  pandour.  For  the  etymol.  of  OF .  ban  see ban,  ‘edict’.  MHG.  banier(e)  (whence  G.  Banner and  Panier ),  ‘banner’,  is  an  OF.  loan  word.
4399:Derivatives:  banner,  tr.  and  intr.  v.  \(obsol.), banner-ed,  adj.,  bann-er,  n.  ( obsol .),  banneret (q.v.)
4400:banneret,  n.,  order  of  knighthood ;  orig.,  a  knight who  could  lead  his  men  into  battle  under  his own  banner.  —  ME.  baneret,  fr.  OF.  baneret (F.  banneret),  a  derivative  of  baniere  (F.  ban¬ ner  e).  See  banner.
4401:banneret,  bannerette,  n.,  small  banner.  —  OF. banerete,  dimin.  of  baniere  (F.  banniere ).  See banner  and  -et,  -ette.
4402:bannerol,  n.,  banner  borne  at  a  funeral  and  placed over  the  tomb.  —  A  variant  of  banderole, bannock,  n.,  a  thick  flat  cake.  —  OE.  bannuc, ‘cake’,  fr.  Gael,  bonnach,  of  s.m. banns,  bans,  n.  pi.,  public  announcement  of  a marriage.  —  PI.  of  ban,  ‘edict’, banquet,  n.  —  F.,  fr.  It.  banchetto,  dimin.  of  ban¬ co,  ‘bench’.  See  bench  and  -et  and  cp.  banc, banco,  banket,  banquette.
10609:beat,  strike’,  Gk.  Oetvetv  (for  *ghwen-yein), ‘to  strike’,  cpAvot;  (for  *ghwonos),  ‘murder’.  Alb. gan,  ‘I  hunt’,  OSlav.  zenQ,  gunati,  ‘to  drive’, Lith.  genu ,  gihti,  ‘to  drive’,  geniu,  geneti,  ‘to  cut off  branches’,  OIr.  gonim,  ‘I  strike,  kill’,  gain, ‘a  wound’,  ON.  gunnr,  gudr,  OE.  gud,  ‘war, battle’,  gudfana,  ‘banner’.  Cp.  defense,  fend,  of¬ fend,  offense.  Cp.  also  phoenix,  the  first  element in  gonfanon,  Gunther,  and  the  second  element in  Bellerophon,  Tisiphone,  Triphasia  and Edith.  Derivatives :  defendant  (q.v.),  defend-er,  n. defendant,  adj.,  defending;  n.,  the  accused  party (law).  —  F.  defendant,  pres.  part,  of  defendre, fr.  L.  defendere.  See  defend  and  -ant. defenestration,  n.,  the  act  of  throwing  out  of  a window.  —  Formed  fr.  pref.  de-,  L.  fenestra, ‘window’  (see  fenestra)  and  suff.  -ation.  Cp. fenestration.
```


## [2026-09-05T13:47:22.874Z] TOOL CALL #15: Bash

```json
{
 "command": "pdftoppm -f 87 -l 87 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg87 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 87"
}
```


## [2026-09-05T13:47:24.552Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN tulbend/turban ===\"\ngrep -n -i \"tulbend\\|tulbend\\|turban\\|tulipe\" PHN.txt | head -20\necho \"=== LKT turban/tulpe ===\"\ngrep -n -i \"tulband\\|dulband\\|Turban\\|Tulpe\" LKT.txt | head -20",
 "description": "grep Pihan and Lokotsch"
}
```


### [2026-09-05T13:47:24.940Z] TOOL RESULT

```
total 29552
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 02:45 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83526 Sep  5 02:45 pg89.png
```


### [2026-09-05T13:47:24.993Z] TOOL RESULT

```
=== PHN tulbend/turban ===
3043:former le turban chez les peuples orientaux. Les Turcs l'ap-
4900:tant. Ces bonnets , qui se portent habituellement sous le turban ,
7014:pièce d'étoffe que l'on roule autour de la tête, turban. De là vient
9895:TURBAN, s. m. composé, (a.-p.)
9903:puissent porter un turban vert. — Le mot turban n'est, comme
10930:Turban , s. m. compose, (a.-p.) 363
=== LKT turban/tulpe ===
842:N.  pr.,  Provinz  in  Vorderindien ;  hieraus sp.  albengala  'sehr  feiner  Leinenstoff, mit  dem  die  Mauren  Spaniens  ihren Turban  schmückten'.  —  Als  Adj.  kommt das  Wort  in  engl,  betigal  light,  dlsch. bengalisches  Licht,  bengalische  Beleuch- tung vor:  Die  indischen  Fürsten  pflegten bei  ihren  Festen  ihre  Paläste  und  Gär- ten durch  eigenartige  Brennstoffe  in glänzend  bunte  Beleuchtung  zu  setzen. [DE  71.
1052:Calmak  'uuistolien,  umdrehen'  [Stamm saj,  caj.  cal  Vämbery  TktEtWb  S.  138, Nr.  149];  hieiaus  russ.  cal  'Tau,  Strick (zum  Anbinden  am  Ufer)',  Vb.  calW, caliwat'  'fe.stbinden,  am  Ufer  anmachen'. —  Aus  dem  tk.  subst.  Infinitiv  calma {der  tk.  eine  andere  Bedeutung  hat: 'das  Stofsen',  oder  'grob']  wurde  rum. cealma  'Turban,  Turhantuch',  russ.  buig. serb.  calma,  klruss.  calma  'Turban'. [Gorjajew  407.    Bern  SlEtWb  135.
1393:'Turban'  [aus  pers.  dil  'Herz'  Horn NpEt  S.  127,  Nr.  571  und  band,  Präsens- stamm von  bästän  'binden'  ebenda  S.  50, Nr. 219;  also  'herzentzückend'];  hieraus l  um.^M^pan'Musseline,  Kopftuch  daraus', tulhent  'Brautschleier',  turban  'Turban', bulg.  serb.  turban,  russ.  tjtirban;  afrz. tolleban,  frz.  turban,  it.  twhante,  sp.  pg. torbante  'Turban';  ndl.  tulband,  engl. turban,  dtsch.  Turban.  —  Aus  demselben Grundwort  ist  der  Name  der  Pflanze Tulipa  Gesneriana  entstanden;  i.  J.  1554 sah  sie  der  kaiserliche  Gesandte  BUS- BECK in  Adrianopel  und  nannte  die  weit offen  stehenden  Blumen  nach  ihrer  Ähn- lichkeit mit  dem  tk.-pers.  Worte  für 'Turban'  [die  Perser  und  Türken  nennen die  Tulpe  übrigens  nicht  so,  sondern peTS.lälä,  tk.lale]:  rv\m.  tuliiyan  [=  la- lea],  it.  tulijxino,  frz.  tulipe,  sp.  pg.  tu- lipa, tulipan;  dtsch.  Tulpe,  ndl.  ftclp, engl,  tulip;  russ.  tjul'pan,  öech.  poln. tulipan.  —  Ableitg.  sp.  torbandalo 'Hammerfisch'.  [ML  8974.  MWiD 11.5/116.
1500:N.  pr.,  Hauptstadt  von  Marokko:  hieraus die  Bezeichnung  der  Kopfbedeckung  der Muslimen ;  über  tk.  fes  wurde  rum.  fes, iTZ.fez;  fiel,  pheci  {—  kepi\,  dtsch.  Fez usw.  —  ,Die  heute  in  Europa  allgemein gebräuchliche  Bezeichnung  Fez  für  die in  den  verschiedensten  Formen  vor- kommende, fast  in  der  ganzen  muham- medanischen  Welt  übliche  rote  Kopf- bedeckung hat  mit  Fes,  der  Hauptstadt von  Marokko,  nichts  mehr  zu  tun,  wenn auch  der  Name  auf  Fes  als  dem  ursprüng- lichen Fabrikationsort  hindeuten  mag. Die  heutigen  Fese  stammen  fast  durch- weg aus  Europa,  insbesondere  aus  Öster- reich. In  der  Stadt  Fes  werden  nur spitz  zulaufende  Tarbusche  aus  grobem, rotem  Filz  mit  kleiner  blauer  Seiden- quaste hergestellt,  welche  hauptsächlich von  den  marokkanischen  Soldaten  unter einem  großen  weißen  Turban  getragen werden. "  Max  Freiherr  von  Oppenheim,
1558:'Handtuch,  Badeschürze'  [Dozy  Vetem 342] ;  hieraus  pg.  fota  'eme  Art  Turban' [so  auch  Constancio  Dice  571c;  dagegen 1
3030:'Tulpe,  Tulipa  persica'  [s.  auch  hier Nr.  544],  ebenso  tk.  lale;  hieraus  rum. lalea  'dass.';  serb.  lale  'dass.',  bulg.  lale 'dass.,  Mohn'.  [Mikl  SlEtWb  160  a. Bern  SlEtWb  688.
4193:'Edel,  vornehm',  Titel,  dei-  den  Nach- kommen Muhammads,  also  Fätimas  und 'Alis,  gegeben  wird ;  ihr  Abzeichen  ist der  grüne  Turban:  frz.  cMrif,  engl. sherif,  dtscb.  Scherif.  Aus  demselben Grundwort  sp.  jarifo  'schön,  schön  ge- kleidet'. [DE  355.  Devic  DEt  93.  Eguilaz 431.  ML  7676.
4502:Auch  täkija  'üntermütze,  d.  h.  weißes Käppchen,  das  unter  dem  Turban  ge- tragen wird'  [Dozy  Velem  280  f.] ;  hier- aus sp.  toca,  it.  tocco,  frz.  toque  'Barett, Käppchen',  siz.  toccu  'weißes  Käppchen, das  gewöhnlich  die  Köche  tragen';  dtsch. Tocke,  Tockhut  [für  Damen,  Modeaus- druck]. Über  tk.  takije  'Mütze'  wurde rum.  tichie,  chitie  'Käppchen'.  [Das Entstehen  von  o  in  den  rom.  Formen aus  ar.  ä  erklärt  sich  aus  der  Nachbar- schaft der  emphatischen  Laute  t  und  k, die  schon  im  Ar.  eine  Verdumpfung  der Vokale  hervorrufen.]  [Löbel  EITAP  95. GrSVociSic  248.    Lammens  Rem  241.
5061:2114 Tseu-tung  2188 r^i/ra  2100 Tulpe  544
5883:Teekessel  j.  1166 Teerjacke  929 re/f»M  1990 TheodoUth  896 Tintenkuli  1198 Tocfce  1997 To/fts  j.  1978 Tohuwabohu  2085 tolmetsche  mhd.  2078 Tombak  2012 Trabant  490 ^»•«■/■e  j.  2070 Trepang  2096 Trutschelmann  2033 Tm^  2097 Tm/^jc  544 Turban  544 tilrkenzen  2114 rwrifcw  2114
6218:turban  544
6717:trucheman  203') 1  iMZjpe  544 '  turban  544 I  <Mr6rtÄ  2110 '  <Mn;  2114  d 1  turquerie  2114 i  ('fcZ^  rfc;  Turquie  2114 I  turquoise  2114 I  tut(h)ie  2120 !  «.v/'Äon  1990
7245:turbante  544
7634:tabijn  133 taf  1981 taggerijn  2057 talisman  2077 talksteen  2003 tamarinde  2013 tangerijn  2057 teHef  2037 tartaan  2036 i^ee  415 toewan  2122 trabant  490 tripang  2096 tulband  544 «mZ/>  544 <Mr&j7/j  2110 turkoois  2114
8830:turban  544
9706:turban  544
```


## [2026-09-05T13:47:40.492Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg87.png"
}
```


### [2026-09-05T13:47:40.972Z] TOOL RESULT

```

```


## [2026-09-05T13:47:40.951Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T13:47:52.820Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nv=d['BQT']\nprint(json.dumps(v,ensure_ascii=False,indent=1))\n\"",
 "description": "BQT page offset info"
}
```


### [2026-09-05T13:47:54.580Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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
```


## [2026-09-05T13:47:54.829Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 انفست ===\"\ngrep -n \"انفست\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt 2>/dev/null | head -10\necho \"=== BQT v1 انبست ===\"\ngrep -n \"انبست\" BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt 2>/dev/null | head -10",
 "description": "grep Borhan for anbast/anfast"
}
```


### [2026-09-05T13:47:54.902Z] TOOL RESULT

```
=== BQT v1 انفست ===
=== BQT v1 انبست ===
BQT_alt_v1.txt:27866:شده‌باشد ودر اصل این لفت‌انبسته بروزن‌برجته 
BQT_v1_pages.txt:15778:۵ - همین وجه صحیح است. ر انبسته.
BQT_v1.txt:30510:۵ - همین وجه صحیح است. ر انبسته.
```


## [2026-09-05T13:47:59.261Z] TOOL CALL #20: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:173 2>&1 | head -60",
 "description": "Fetch BQT page 173"
}
```


### [2026-09-05T13:48:04.296Z] TOOL RESULT

```
no scan of BQT covers printed page 173 (see 'scans' in refs_online.json)
```


## [2026-09-05T13:48:10.182Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 383 384 392 393; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -25; done",
 "description": "Print BQT v1 leaves near printed 164/173"
}
```


### [2026-09-05T13:48:12.789Z] TOOL RESULT

```
===== leaf 383 =====
سب ی ٩5‏
| بودن بروزن افزودن, بربالای حم
چیدن باشد .
اثبوذن س با زال قطه‌دار بروزن‌اندودن,
بمعنی اسل‌کاینات و آفرینش باشد .
ایوس » بروزن اضوی , تخمی باشد
بنظر آحده است ۰
| بو سیدن - بانستانی مجپول بروزن
افزوییدن , بمعنی پدید آمدن و ظاهر شدن -
و موجود گردبدن باشد .
اثبوه » بروزن اندره » بمعنی‌فرورختن
دبوار باشد - و بمعتی پر و عملو و بسیار نیز
امده خواه بساری مردم و خواه چیزی دیگر
باشد - و دم قصبه است در بالای کوهی از
مضافات دیلمان .
اثبوی « بر وزن بدبوی » بعنی بوی
کردن باشد ٩‏ - و چیزی‌را نیز گوبند که ببوی
آهده و کندیده باشد - و مطلق‌بوی رانیز گونشد
خواه بوی خوب و خواه بوی بد باشد - و بوی
کننده را نیز کوش که فاعل باشد - و اهر باین
معنی هم هست عنی بوی کن و سوی ۰
) بو ی (۱) » بکربایحطی‌وسکون
دال ؛ یمنی بوی کرد -- و امر بجمم هم هست
بعتی بوی کنید و ببوید .
انبوییدن 0)- ممدر ابوی باشد
===== leaf 384 =====
انج - بفتح اول وسکون ثانی و جیم»
اطراف 2 روی و رخار ( ۱ ) باشد -
«بمعنی بیرون رفتن وبیرون کشیدن‌هم آمدم‌است
- وامر بان معنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند که‌بنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطه‌دار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزن‌بدبخت»
انش ‌ باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاك‌بروزن‌ب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتی‌و صحرادیست غیرمعلوم-
===== leaf 392 =====
اگارده است که افسانه و سر گذشت باشد .
انگاده ۱ ه بروزن عموارء ."هر چیز
"که افانه وس گذشت داشد - وباد گذشتها کردن
رانیز کوبند - و ازسر گرفتن سر گذشت وافانه
را عم گفته اند بطریق کنابه چنانکه ا گر کسی
بسیارومکرراز گذشته بگوید گویشدهانگاره‌میکند»
یعنی باز از سر هیگیرد - و پس پی خزنده از
شرم و حیا را نیز کوبند - وبمعتي دفتر وحساب
و نامه اعمال هم نوشتهاند .
انگادیدن ۱ » بر وزن ترسانیدن »
بمعنی هو رکردن وینداشتن ‏ و گمان بودن‌باشد .
اناد » با زای‌هوزبروزن پرواز .افزار
آن اووات است .
انگاشتی ۱ -بر وزن برداشتن. بمعنی
صور کردن و نداشتن و کمان بردن باشه. .-
انگام ۴ » بروزن و معنی‌هتگام است
که موسم و وفت باشد .
انگاهه ۲ - بر وزن و معنی هنک‌امه
۱ راد : انگاردن ۰
۳ ت ازمادهٌ اذیدمن» رژد انجمن.
ات
است که مجمع و انجمن بازیگران و قصهخوانان
ا لگیین ۴ - با بای‌ابجد بروزن‌عنبرین,
سل و شهد را گوبند .
انگیینه - بروزن شنبلیله , نام حلوامی
===== leaf 393 =====
مردم فررنگ «م هست ٩‏ ۰
الث و زای قطه‌دار ساکن » سلی باشد که بآن
زمن را هموار ساز ند ۹
انگز ح بفت اول و خم نالث: و کت
تابی و زای فارسی» آهنی باشد سر کج که فیلرا
بدان بهرطرف که خواهند بي‌ند .
انگژ د ۴ ختح اول دضم ثالث‌وسکون
انی و فتح زای فارسی ودال ابجد -اکن مطلق
صعفها را گویندعموعاً و صمفی باشد بغایت‌بدبوی
و آترا پعربی حلتیت خوانندو آنرا انگژدیسب
آن گون که سمغ درحت انگدان است و ال
آن انگدان ژد باشد بفتح زای فارسی چه ژد
بلفت فرس بمعنی صمغ است و آن گرم و خشكت
است در درجه سیم .
انگز لك . بازای هوز بروزن مرجمك ,
کجك فل را گونند و آن آلی باشد سر کج از
آهن که فیلبانان فیل رابدان بپرطرف که‌خواهند
برند . و بازای فارسی هم بنظر آهده است :
اآلگژ واه بکس نات و سکون زای
فارسی و واو بالف کشپده‌بروزن »نزل‌ها. جابی‌را
کودت که شنها گوتفندان زا چر ادا تک
دارند - و کوسفندانرا نیز گفته‌اند - ویمعنی‌دانه
و ختَهةٌ میوه ها هم آهده است .
انگشت برچشم نفادن
۱ نگژه ‌ ح با زای فارسی مفتوح‌بروزن
```


## [2026-09-05T13:48:25.979Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"اثبست\" \"انبست\" \"اثفست\" \"انفست\" \"اتبست\" \"اتفست\"; do echo \"== $w\"; grep -n \"$w\" BQT_v1_pages.txt | head -5; done\necho \"--- leaf of line 15778 ---\"\nawk 'NR<=15778' BQT_v1_pages.txt | tr -cd '\\f' | wc -c\nsed -n '15765,15790p' BQT_v1_pages.txt",
 "description": "Search Borhan variants for anbast"
}
```


### [2026-09-05T13:48:27.545Z] TOOL RESULT

```
== اثبست
== انبست
15778:۵ - همین وجه صحیح است. ر انبسته.
== اثفست
== انفست
== اتبست
== اتفست
--- leaf of line 15778 ---
419
و آن عددی بائد مجپول میان سه و نه و آنرا
بعربی بضع خوانند ۷" و سخن عجیب و سخن
از روی شكو رب‌رانیز کوبند - و بمعنی‌چندان
و چندین هم آمده است .
اناد - با انی مجپول بروزن دبوار .
وقت عمر باشدکه «نماز دیگرش نیز میگویند
چثانکه ثبگیر صبح را خوانند- و رامرفتن وقت
صررا ابوار کردن و وقت صبح را شبگیر مودن
کونند ۸ .
ی ان :
۹ اف اس دروآینت» ۷ رك : آبدند ۰
ایزد هت آسمان کرده است ادرفران
۴ در پارسی باستان 1008 , در پهلوی تط,
۵ - همین وجه صحیح است. ر انبسته.
لمنت ایشندجای برئن‌دیودژم «عنوچهری 6۵6
بقبه ازصفحهً ۱۹۸ایولز
ایو اد « بانانی مجهول بر وزن شیرازه
بمعتی آراسته و بیراسته باشه ۱ .
بسعنی ابواز است که آراسته و پیراسته باشد ۳ .
الوان ه بروز نکوان . صقه و طاق را
بند ۴ ,:
ابوانس بفتح‌اول وسکون ثانی‌وثالث
بالف کشیده و نون مکسود بین بی‌نقطةٌ ده .نام
شهری باشد از فریگگ ؛ و در آن شهر کیسای
است که هر سال در وفت تحویل آفتاب به برج
جدی مار بسیار می‌آبند و هربك را زتونی در
```


## [2026-09-05T13:48:38.154Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 380 381 382; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt; done",
 "description": "Print BQT leaves 380-382"
}
```


### [2026-09-05T13:48:40.676Z] TOOL RESULT

```
===== leaf 380 =====
که زر بائد! .۷
امی‌صادق - بنم اول , اشاره (۱) به
حضرت رسالت ناه صلوات‌اله علیه باشد .
امیله ه بروزن دلیله » بمعی‌آمله‌است
وان وهای باشد درهندوستان که درشکرپرورده
۲۳ وخورند .
ان - بفتح اول وسکون ثانی بلفت زند
ویازند(۲) والده را گویند که عادرباشد - وب‌عنی
آن هت که درمقابل این‌است؟ - وافاده فاعلیت
نز کند هر کاه که در آخر کلمه در آودند همجو
اقتان وخبزان .
انا قو لقن - با نای‌ترشت ونون وفوقانی
بروزن جفاجوی حن . بلفت زند وپازند(۲)بمعنی
گذاشتن ونهادن باشد؟ .۶
انار قر ها - ۳۳ رای شرشته. ۸
درخت انارست که در بستون واقه‌است . گویند
چون فرهاد از شنبدن فوت شیرین نيشه برس
خود زد دس تیشه خونآ لود کردید وا کوه بر
زمین افتاد وسرآن برزمین نشست » و چون آن
ازچوب انار بود بقدرت الهی سبزشد ودرخت آنار
۹۹ چك : شارت .
بهم رسید وانار آنرا چون باز کنند اندرون آن
سوخته وخاکستر شدء باشد . ۱
افار گیر ا - با کاف فارسی بتحتانی
رسیده و رای بی‌نقطه بالف کشیده . در فرهنگه
جهانگیری بممنی کو کدار وغور خشخاش باشد,
ودر صحاح الادوبه بجایرای بی نقطه آخرواوآعده
است - وخدخاش را نز کفته‌اند .
انار مثك ت بکسر عم وسکون شین
قرشت و کاف . نام دارویی است که ازهندوستان
آورند . و آن تخمی باشد سرخ دنگه و اندله
سبزی در میان دارد . و سرب دهان عصری
خوانند .
! ناطبطس باطایحعی سحتانی‌رسیده
وطای دیگر ببین بی نفطةٌ زده . لفتی است به
۴ - هز27 . چهلوی 6 بمعنی
مسر آعده و
===== leaf 381 =====
یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان
کن » باشد . وآن دانه ایست ساهرنگه بمقداو
جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون
بجنبانند مفز آن در درون وی صدا کند وآنرا
بشیرازی « کن ابلیس » خوانند نم کاف فارسی
ونون ۰ یعنی خایةٌ شبطان و بعربی حجرالولادة
گوبند . چه هرگاه در زیر زنان آستن دود
کنند زود بزایند و اکر باشیرزنان سح قکنند
وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
بوفت جماع بخود بر گیرد آستن قود.. گو یف
چونآنرا دردست گیرند وبا کسی مخاصمت کنند
برآ نکس غالب‌آیند .
| ناغاطسی - باغننقطه داربالفکفیده
وطای حطی مضموم بسین بی‌نقطه زده ۰ بونالی
سنکی باشد که چون آنرا بآب بسابند رنگی
مانند خون از آن برآید و با شیر زنان درچشم
چکانند ورم چشم و بیاری آب آمدن از چشم
رانافم‌است» وآن‌را بعربی‌حجر اناغاط یگویند .
افاغلس مه بن غین تقطه دار و لام
وسکون مین بی‌قطه ۰ بیونانی؟ دوایی است که
آنرا بفارسی مرذنگوش وبعربیآ ذان‌الفار گویند,
چه بر ک» آن بگوش موش میماند » باس رکه بر
کزیدگی عغرب مالنده نافم است
افا لیقی - با لام و قاف هر دو بتحتالی
رسیده . بلفت رومی دوابی که انرا انجرء
وتخم آنرا بذرالانجره گویندوبمربی قض‌خوانند.
انبارده
تخم آن مستعمل است . اکر مقدار سه درم از
آن باشیر گوسفند بخورند قوت‌باه دهد » ویضی
گویند انالیقی همان بذرالافجره است .
| ثاهیكف ؟ » با های‌تحتانی رسیدموبدال "
زده . بمعنی ناهمد است که ساره زهره باشد .
اب - بفتح اول و انی و سکون بای
ابجد . بادنجان را گوشد و آن ممروفست؟ »
بافراط خوردن آن جذام د ماع و بی‌خوایی
آورد» و بعضی گویند عرمی است ۱
ی رزن
افلاطون » حصار قلمه و جای محکم ر! کوشد -
انبار 1 ع بفتح‌اول‌بروزن زنگار «بمعی
لبریز و مملو و پر باشد - و فروربختن خانه
و افتادن دبوار و امثال الرا نیز گویندب ویمعنی
خی و خاشاله و فثلة اسان و س رکین خیوانات
دبگر باشد که توده کرده‌باشند و مزارعان‌برزمی
زراعت ریز ند واستخر وتالاب رائیز انبار گوینف
و بکر اول مخفف این بار است
انبادذ گی « بروزن و معنی انباششگی
اک ستتی. ود باه مت نب
| ثباددن ۱ « با دال ابجد بروژن‌وعنی
انباشتن است کهپر کردن و انبار کردن‌چیزی‌باشد
از چیزی دیگر
)۱ چك : ژند ویاژند .
۱ - بونانی2601185 «اشتبتگاس» ش بان 881021115 0استینگاس »0 202
«دزی»,
آلوده. جمما بعنی
داده‌اند ای کردند. ۶ بشت ۱
- بهلوی ۵2۸02۲ 0 از
۴ راك : لك ٩‏ ص۱۹۱ .
4 «مناس ۲۷۵ :
: : انبار) ۳ دن‌یسوند مصدری ۳
===== leaf 382 =====
اتبارش
که پر کرده باشد - و بمعنی پرنسمت و با نعست
هم اجه ات ۵
نبادش! -بروزن‌افزایش. پر کردنی‌را
کوبند . و آن چیزی باشد که جوف درون
چیزبرا بان پر کنند. وأنرا بعربی حشوخوانند.
انبار "سیر وزن دمساز » خومات و رفیق
و همتا را گویند . "
نباشت ۱0 بروزن برداشت ۳ ماضی
انباشتن است ععنی کر و ممل و گرداند ۰
۶ ۵۸۱ ه ۳ > ۳
انباشتی ۲۷ " سبروزن برداشتن,بسنی
پر کردن و مملو گردانیدن و آنبار نمودن باشد .
افیا ۴ - باغی تقطم‌دار .دوزن‌را گوبند
دیگری‌را انباغ باشد .8
اثبان باد - بکر نون و با بای ابجد
بروزن می‌دان‌کار. مردم فربه - و بیکاره وهیجکاره
را گوند ۰
برمی آورند .
اثبر ب بنتح اول وضم الث وسکون‌انی
و رای فرشت » التی باشد از آهن که ز رکران
و مسکران طلا و مس تفته دا بدان گیرند ,وبه
عربی کلوب خوانند .
۱ 1 از انبار شش بوند آسم
و
] ذیر وت ده بروزن‌عنزروت , امیودباشد
و آن میومایست معروف ۵ .
افیره - ینم ات بروزن‌قنجفه «هرجیز
موی رنخته را کونند عموماً وشتر موی ریخثه را
خصوصا ‏ و اسب و شتر آبکش را نز گفتماس
و در عربی شکنبه را گویند - و بمعنی دره کوه
نیز حست ؛ و بفتح ثالث بر وزن حنجره هم
آمفه ات .
اثیست - بروزنک‌بت : نلیط و بته
شده را کومند ۷ .
| ثیسقه - بر وزن برجسته ,هر چي زکه
آن بته و سخت شده باشد و بدشواری وا شود
و حل گردد - و شبر و ماست و خون بستهرانیز
گوبتد ٩‏ .
اثبله - بنتح اول و الث بروزن‌حنظله,
تمر هندی رأگویند و بهندی ابلی خوانتد ۰۷
انیمی ۸ س بکسر ثالث وقتح میم‌بروزن
صف‌شکن , بلفت زند و بازند (۳) انگور باشد
و بعربی علب گویند .
افیق یه - بروزن میغوب . فرش وساط
و گتردنی را گومشه. :
اثبو 4 - بر وزن منصوبه . ماشوره را
گویند - و وله آشابه و مانئد آنرا نیز
کفته‌اند .
۴ - پهلوی ۵:۳۰98۵1, 20۵۵2۵۷
۲
۴ ات ود اون
ت۱۳ تم ستد.
۸ حز2(8021130),
```


## [2026-09-05T13:48:50.769Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 389 390 391; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -70; done",
 "description": "Print BQT leaves 389-391"
}
```


### [2026-09-05T13:48:52.487Z] TOOL RESULT

```
===== leaf 389 =====
اف
او رفتی . بکشب بای شد و آتش را بکشت
راندروی درمیان دربا کم کردید ..
سین می‌نقطه , نام یکی از حکمای بونان است
گوند درطبابت اعجاز مکاربردی ۴
نلم مکی از مبلوزان تورانیی است ۳
دوازده د بردست گر کین ملاد کشنه شد" شلد ,
| ند ۴ بسکون کاف , تسضر اند
است , واند عددی باشد مجهول میان سه و نه
و انرا بعربی بضم خوانند - وهرچیز کم را نیز
نس ,۰
ند گان بروزن بند گان ۰ نلم‌شهری
۳ است مایین سمرقند و چین ء معرب آن
اند دی نم‌اول وثالثولام ۳
نانی وسین م‌نقطه » نام شهرست درحدود حغرب
- ونام جزیره‌ای هم هست‌در بالای کوهی ؛ وبهر
دوممنی فتح اول و ثالث ورابع هم امده است
! ند مه ‌ بروزن صردهه: » باد آوردن
غمپای گذخنه باشد .
که درمقایل بیرون است
ی
خبون وبرادر اراس
«مناس۹ ۲۷ .راد: ۳
اند
کرداند . آنرا بعربی قوباکویشد .
افو ج -بروزن محلوج» بمعنی‌اندوب
است وآن جوششی است با خارش که عرب قوبا
شف
] ند و خقی* - بروزن‌افروختن» بمعنی
جمم کردن وفراهم آوردن باشد - بمعئی قرض
و ایس دادن ‌‌ زد ابیت
اند‌و.- وزن مقصود ۰ کاهمگل
) ندودن۱ - بروزن‌فرمودن . کاهگل
و کلابه مالیدن باشد - ومطلا وملمع کردن دا
نیز کوید .
ا فك و ۷ - بروزن سردوز؛ بمعنی‌فراهم
آورده وجمم کرده شده باشد - وامر باین حمنی
همست عنی جمع کن وفراه آور .
اندول بروزن ممقول ۰ کلیمی باشد
کهآنرا برچهارچوب بامیخها سکم کنندوبجهت
استراحت برآن نشینند . و این در ملك زنگبار
مصمول است »
| ندو ف » بنتح رابع وسکون نون‌ودال
ابجد » از انباع است بمعنی تار وعار که زبروزس
شده رازهم باشدم باشد .
آف‌وه٩‏ - بروزن انبوه , گرشکی ول
ودلگیربرا اگوبند ف
| زد و۸ چم ثالث » مخفف اندوه است
» و اوزن ۳6000۲ ومادر ۸5۷۵۵
۴ - نیز اندیرما, در اوستا
۴ پهلوی 12702۷ (کم »کمی)
فعه در صفحة ۱۷
===== leaf 390 =====
انسجان
که کرفتگی دل ودلگیری باشد .
اندهان بروزن مردمان ؛ جمم انده
باشد چنانکه جانور را جانوران ومردمرا عردمان
کویند . واین جمم بخلاف‌قیای است چه‌بنیراز
جاتور را بالف ونون جمع وان کرد .
نده‌قو و » بت دوقاف و سکون دو
واو ؛ دوایی‌است که آنرا حندقوفی‌خوانشد * کلف
را نافع است ,
انفی ‏ بر وزن لندی » بمعنی خاسه
باشد که درعقابل خرجی‌است - وبمعنی‌امیدواری
هم آمده است - وبجای لفظ بودکه.و باشد که
هم استعمال میکنند - وبمعنی‌آن لحظه هم‌هت
" وبمعنی تیزهم آمد» است که بعربی‌ایضا خوانند .
اند یدن عه بر وزن خندیدن . سمحنی
تعجب کردن باشد - و سخنی را ليز گونند که
از رویه خك وزرب تک کته شود .
اند یشه - بر وژن هم پیشه » بممنی
فکروخیال باشد - و بمعنی فری ویم هم آمده
است .
) ند باث بروزن نزديك , لفظی است
از کلمات تمنی که در غربی لیت و لعل وعسی
۱ -رك : اندوب واندوج .
بقیه ازصفحةٌ ۱۷۱
(9
کویند بعنی باشدکه و بود که و بابد که -
وبمعنی زبرا, که و از برای آن واز ابنجهت‌هم
گفته‌اند .
) نفد و ه با ذال قطه دار و رای‌بی شطه
پروژن لبلبو » پا زهر باشد و انرا فاد زهر نیز
کوبند , وبجای زال نقطه دار زای هوزهم آمده
اشنت: ۵
افر » بفتح اول وانی‌وسکونرای‌فرشت»
هرچیززشت وید را کوشد .
اثر وب بر وزن منکوب » جوششی
است با خارش که بمربی فوبا خوانند و بعضی
گونند جوهدی است که آنرا شارسی گر
و بتازی جرب خوانند , و با زای نتطه دار حم
کنته اند ۱ .
انز دو - شم اول و زای هوز و رای
فرشت بواو رسیده » سحنی بازهر است وفاد زهر
نی گونشه .
افز دوت »بر وزن و معنی عنزروت
است» وآن صمفی باشد نلخ که بیشتر درمرهمها
بکاربرند؟ وعتزروت معرب آنست » و در مود
الغضلا باین ععتی با ذال نقطه‌دار و بای آیجد ‌‌
آمده است که انذروب باشد .
۷ ره : اندوختن.
. درونی؛ داخلی . باطنی‎ > ٩
* بارتولمه ۹۸۸ * تیب ک۱۰۰۵ که
===== leaf 391 =====
رن
ار ه- باازای فارسی بر وزن غمزه ؛
مرجماث باشد و آثرا ببربی عد ی گویند .
انسته - بفتم اول و کسرثانی و سکون
سین بی‌قطه و فتح فوفالی 4 مقصورآ دته است»
وان بیخ کیاهی باشد خوشبوی که بعربی سعد
" گو بکف .
۰ ۰
انشانا - بفتم اول و سکون الی وشن
فرشت ونئای مثلته هردو مالف کشیفه » بسربالی
دوابی‌است که آنرا بغارسی مویزكك وبعربی زسبت
الجبل خوانند .
اتطلیون « با ای حطی ولام وتحتانی
بروزن عنبر گون , بلغت بونانی۱ فوی قزح را
کون دک هکمان شرطان باشد .
| نطی فیا۳ - بروزن‌افلونیا. بلفت‌ونانی
کاسنی شامی را گویند وآن سرد وتراست ودجگر
گرم را نافم باشد .9
اقاق »یک اول و سکون تانی وفای
بالف کشیده و بقاف زده ۰ روغن زءتون تازه را
گویند .
ات - بر وزن رحست  )۱(‏ همان
وخارت وزبانرا کویند که سمعنی غبن‌باشد - ودر
عربی بمعنی ننک و عار آمده است ۰
] نقست « بروزن , بدمست » پرده وتنیده
عنکبوت وا گوشد .
افقر دیا - بختح اول و فاف و سکون
ثانی و را و دال بی نقطه و تحتانی بالف کشیده »
لغتی است رومی و بعضی کوبند بونالی ۴ وممنی
آن مانند دل‌باشد وان چیزس تکهبلاد ر گوشد.
)۱( چاثه : زحمت.
۱ - بیونانی 50461105. «افتشنگای».
انگارده
بهترین وی آست که سیاه و فربه باشد و چون
بشکنند پر شیره بود . و آن گرم و خشك است
در چهارم» فوت حافظه دهد وذهن را تب زکند ,
و بعربی‌ثمرقالبلادر خوانند وبهندی بلاو مگویند.
قلیا - بکر اول و قاف و سکون‌ثانی
و لام و تحتانی بالف کدیده , بلفت احل فرب
دوایی است که آغرا بفارسی شنکار گویند وبعریی
شجرتالدم خوانند. وآن نوعی از سرخ مرداست.
بررکه آن سرخ بسياهی مابل میباشد بذ ییه بز
کوهی برخنازیی نهئد نافم بود؛ و بعضی گویند
لفت رومی است .
اون ه با قاف بروزن «یمون » بلفت
بونانی کل کنده را گویند وآن نوعی از کماةباشد
وآنرا بجهت فربهی حلوا کرده خورند. و بعربي
وردالمنتن )+( خوانند .
انگ . بغتح اول و سکون انی و کاف
فارسی . محر آب را گوبن که کوزه گران اژسفال
سازند و بجپت مرور کردن آب بهم وص لکنند.
و نام ولاتی است در هندوستان ۴ .
انگاد * - بروزن زیگار . بسنی‌صور
و پندارباشد که از پنداشتن‌است - و صور کننده
را نیز گوبند - و امر باین هعتی هم هست معنی
یشگار و انکارشی‌کن- وبمعتی انکاره نیز آمده
است که کار نانمام باشد .
نگاردن » بفتح ارل و دال ابید
وسکون نون . بمعنی‌پنداشتن وود کردنو کمان
بردن باشد .
انگار ده * » بنتح‌دالبروزن انگاشته,
اقشانة و .خن کذحت را کوش
۴ -عصحف انطویا: ۲84۳۷/۵۱5 < لك ۱
۴ سورك: آ نکن بت رله؛ انگاردن.
هه درصفحةٌ ۱۷۶
```


## [2026-09-05T13:49:01.839Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 524 525 526; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -60; done",
 "description": "Print BQT leaves around printed 305"
}
```


### [2026-09-05T13:49:03.715Z] TOOL RESULT

```
===== leaf 524 =====
بنابه
و پابان و یخ درخت ٩‏ - و اتهای هر چیز
وچیزی نیز هست که آترا آبکامه گود, و آن
نان خورشی است معروف و مشهور در صفاهان
- وتنه درخت‌را لیز کنبهادب ۴ وخوشة خرمارا
هم میگوند .
بنابه - بنتع ول و بای ایبد و ای
با فکشیده » بمعنی نوبت باشد چنانکه گویند
«بتابةً ماست» بمنی دوم ماست .
بناست « یک اول وثانی بالف کنیده
ء فتح سین بی قطه و بتای قرشت‌زده ۰ صمفی
باشد که آنرا کندر گوبند و بعربی صمغ البطم
خوانند , و خاصیت آن بمسطکی ترديك است
بناع - فتح‌اول بر وزن دماغ (۱)؛ تلر
رسبان خام را گزبند که بر دوك پیچیده شود
باشد ۴ .
او را بردارد - و کنابه از اطاعت و اناد کردن
عم هست .
بنام یکسر اول بر وزن نظلم ؛ بمعنی
همنام. باشد که بت رکی آداش ۴ کویند ۵ .
در محل تعجب کوبند - و بجهت دفع چشم زخم
نیز امتممال کنندچنانکه گوبند «نلم خداچه‌طده
و چالالك است »-وگاهی بجهت ضم یز کنته
میقود -
نا فج - بتح اول و ای بالف کشیده
و بنون و جیم‌زده م ابستی بناغ اس تکه آن‌دو
زن باشند که يك شوهر داشته باشنده هريك مر
دیگریزا بئان گزبند و بنانجه ( ۲ ) هم بنظر
آهده است‌و بعرین‌ضره خوالند.. و بضی‌مردی‌را
بناور بفتح اول و واو بروزن‌سراشر»
دیبل بز رکه را گونند وبمربی حبن خوانندبکسر
حای بي‌نقطه ؛ و بضم اول هم آمده است .
بناو ند یکسر اول و واو مفتوح به
داشتن چیزی باشد دزجایی» مثل .آنکه آجرا جر
التبا ۱ -ایا پای ابجد بروزن غنقا , آشی
باش دکه از ون بزند که حبةالخضراست» وآنشی
درخت بطم باشد و بشیرازیه بن گوینگ .
بن بخحت برد مین مالیدن - کنابن
از استواری بخت و دولت باشد .
بنبر بروزن ۳ دوای است کهآ نر ۱
ادت .
بثیل س با بای ابجد بروزن صندل » به
ممنی نرشی باشد عموعا- و سیب ترش راگوبند
خصوما .
. طبری 9658
۳ گلکی 9202 (هال) .
۴ ره : آداش .
زیرهای قاعلع 99)
===== leaf 525 =====
ی ۵( ح
نو هه » با نای فرشت بروزنمصومه,
نبانی است که مانند کشوث بردرخت زون‌وبادام
و انجیر پیچیده میشود. گرم و خشك است.
لنچ - بفتح اول بروزن رنج » دو ز ن که
بك شوهر دافته باشند هی يك مردیگربرا بنج
بافند ٩‏ - و نام وستئی هم هست که تفر آرا
بذرالبنج گوبند" وجربی شیکران خوانشد ۴ .
انحشات ۴ ه بکر اول و تالث.بمعنی
کتسداك [ ست که بمربی عصفور خوانند .
پنحشاك‌ رو ان ۴ - نم زای حوز
و واو بالف کشیده و بنون زده . لشان‌الصافیر
است و آن دوایی باشد تند و نیز شبیه بزبان
کنشك 4
تشه - بنم اول بر وزن تنبك » پنبة
محلوح و کلوله کرده را گونند بجهت رشن .
بنچه - نم اول و کسر انی و فتح‌جيم
فارسی » جمعی باشند مراصناف حرفت ورعیت‌را.
فا * ح بروزن چند » چند معنی‌دارد :
٩‏ - فاصلهٌ میان دو عنو که آنرا بعربی
متصل خوانند . ۲ - زنجیری که‌برهای‌دبوانگان
و کنهکاران نهند ۳.٩‏ - تنگهٌ آهنی که بجهت
استکام بر صندوق و کشتی و امثال آن زنند .
- ققل را گوبند . ه - مکر و حیله و زرق
رفرینو سالوسی‌باشد. ٩‏ - عهد و بیمان‌وشرطرا
(۱) چش :  -‏ وگردون .
۱ - رله: بناغ وینانج.
کویند « ثابتی ۱۹۷ ۰ .
گویند .
عقده و گره - وحبس بود ٩۰‏ - سدی کهدرییش
آپ بندند . ۱۰ - بمعنی خبال و مقام است‌مثل
آیکه کوبند «فلان در بند آزار فلان است؟ با
«دربند سفراست» بمنی در خیال آزار فلان و در
مقلم مفر است ۰ ۱۳
باشد . ۱۲ - ربسمان و طناب را گوبند . ۱۳ -
بند ترجیم و تر کیب بود» و آن یتی باشد که
۷ غم وه و محنت باشد . 4۸-
شه‌را بمد از چند بیت بردیف و قافِةٌ دبگر
بیاورند .۰ ۱6 - رهن و کرو را گویند
۵ - حیله و فن کشتی کیری باشد ۷ . ٩‏
جفت کاوبرا کویند که بجهت زراعت کردن
و گردون (۱) و ارابه راندن با هم بدارند. ۱۷-
طومار کاغذ باشد . و هر ده دسته از کاغذ را نیز
مك بندگوبند . ۱۸ - پی گرفتن آنجه عنیم
برده باشد و آنسه از غنیم در دارالحوب گیرند.
٩‏ - جمیم بندهارا کوبند همچو بند کارد
و بندششیر و بلد چافشور و شدخبا و ند تثبان
و امثال آن . _--
طمع و توقم را گوبند . ۲۲ - غلیواج بشد
و آن پرنده‌است ممروف . *
پنفاث ه نم اول » بروزن و معنی‌شاد
و پشتیبان باشد - واصل هرچیزرا نیز کوبند۸ .
بندار بم اول بروزن کل زار ۰ کسه
دار و خانفوار و صاحب تجمل و هکنت باشد -
۶ - نام ولاشی است ۰
: ۲ ص ۹۵ و ۷۱ .۰
٩ ابلم...‎
۸ رگ : شاد .
<گاه‌شماری»۲۰*.
===== leaf 526 =====
تدامیر ۱ ۱ ی
دوافروش ٩‏ - و کرانقروش را ی زکویند - ونم بنشر ح بت اول و تالش مروژن کندو ۰.
مکی از شمرای قدیم است ؟ . نام شهری است در دلایت فرچه - و بفتح اول
بنك‌اهیر ه بندست درحوالی‌شیرا زکه و ثالث بروزن‌لنگر ۰ محلی, باش د که قافلموتجار
نان متا لس ای نم خصی پر أ دق بای و رنه
او ساخت ؛ و بسن یکوبند مُردمافری برد امیر بند رد - ینتح اول و ثالث و سکون
تلم » پاراوه خود این بندرا ست ۴ ۰ ثانی ورایع و زای قظمحار , جوال‌دوزرا گوشد,
پندخت « بن اول و ثالث و سکون و بضم اول نیز آمده است . ۱
رخ عبر وف اجه وش برد مان
تا ثالی و وار و غین‌قطمدار » بندی باشد.کمیلچوب
فك « بنم اول بر وزن گنبد » بمعنی و علف و خا وگل در پیش آب بندند تا آب
اصل و بنیاآد هرچیز پاشد * . بلند شود و بزراعت دود .
۱ - < بنکدار . ۴ - مراد کما الدین ابوالفتح بندار بن ابونسر خاطری
رازی مداح ممعدالد, له دیلمی متوفی بسال۰1: و کونده فپلوبات است. « رود کی. غیسی ح ۳
س ۱۱۸۱ . ۳ ۴ - بند امیر در زمان عندالدولهٌ دیلمی (۳۷۲-۳۳۷) برای
مشروب کردن اراضی کربال علیا وسفلی بنا شده وبگفنة مقدسی وامترن‌درآن‌سنگهای سد بواسطة
سرب بهم متصل کردیده .در
آن مدل سصد چر خ‌ساخته
بودند که هر يك آسیابی را
بحرکت دز میآورده است »
وخود سطح آب را بالا برده
مخزن وسیعی تشکیل داده
مقداری ازبرا برای‌هنگام
خشکی ذخیره‌عیکرده است-
این سد چندین بار تا کنون
خراب‌شده] ترامرمت کرده‌اند
س ۰۲ . شیاین تلو ٩‏ این کمه وارد عربی سوربه و عصر شده
بسمتی جامگاه و مقام » مسل تجارت و معأملات پالکی و دستگاه ؛ شاه بندر بمعتی و کیل‌النجار
است و علاطین عثمانی شاه بندر را بغنسول های خود در خارجه اطلاق کرده‌اند. هراثرةاامعارف
آسللام». 1 - بشندروغ مسحف «بند ورغ» است و شمی رودکی را :
آب هرچه بیشتر یر و کند بند ورغ ست بوده (یوده . دهضدا) برکند
اط «بندرو غ» خوانده‌اند. وندورغ مر کب‌است از؛: ند - ور غ(ه. م) «رهشدا» «شی.رو دکی.
ج ۲ ص۱۳۱ >
۵ بداوسی - ركد پیداوسی.
```


## [2026-09-05T13:49:19.766Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 673 674 675; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -45; done",
 "description": "Print BQT leaves around printed 449"
}
```


### [2026-09-05T13:49:21.318Z] TOOL RESULT

```
===== leaf 673 =====
- ۷ -
پیالاد ۵ - بارای‌قرشت بروزن مینافام,
نام حصاری است ت عظیم‌و بز رگث.
بیل‌افکندن کنابه از عاجز کردن
باشد .
یل آهرو ۵ بامیم و رای بی ننطه
بر وزن قیراندود ؛ نوعی از امرود است و آن
صسوم‌ای باشد حعروف.
۰ فیلبا - با بای فارسی بالف ۳
نام حربه‌ایت ه بیشتر زنگان‌دارند - ونوعی
از قدح بزر کب شرامخواری باشد ۱ - و مرنی
است که بای ادمی ورم میکند و بز رکه میشود
و آنرا معربی داءالفیل خوانئد وستونی را فز
کویند که سفف برآن قرار کیرد .
یل لا لا- بابای ابد بروزن میرلالا »
توده وخرمن کرده وسیار را گویند - و کنابه از
ید 0 آمده است (۱).
یل با ‌‌ ستوتیرا گوین د که ا زگچ
2 بر بللای آن بابهای طاق
گذارند۴ ۰
کن ۲ یک از القاب رستم دستان گنت واسبرا
نیز کوبند .
شلسته بروزن سدسته, رخساره‌وروی‌را
گونند ‌ و یمعنی ساعذ دست‌هم مت وانگشت
(۱) چك: هم هست.
۱ - ر4 : بل بابه .
چو در پیلیای فدح م یکنم
:یلا .
(استخو ان) ۰ ستی
۷ - ركك : پیلگوش .
۸ - می خورکت باد نوش: برسمن وپیلگوش
پیل مرغ
دست رالیز گفته‌اند ض بهعتی عاج‌حم بظرآعده
ببران وسهاست واویردست رستم کته عیلا" 2
و بضم رابم سم سطبر وسخت راگویند. و کثابه
پیلخوش"۷ - با غین نقطه دار بر وزن
دیگه جوش .کلی است ازجنس سوسن‌وب ی کتار.
های‌آن خالهای سیاء و رخنهای کوچك باشد -
وگل نیلوفررا نیز کوبند- وچیزی هم هس تکه
خالك انداز گوبند .
یلگوش - با کاف فارسی » بر وزن
ومعتی پیلفوش است که نوعی ازسوسن۸ -ورکل
که ترا لوف گویند » را بمربی‌اصل‌اللوف
و کل ربواج دا نیز 27 و بعر بی 97
خوانند ۰
===== leaf 674 =====
پیل معلق در عوا
یل معلق درد هو کناب اژابیباهد
یی سه بر وزن زیلو ؛چویی .که بدان
مسواگ کنند وعریان اراك خوانند - و بار درخت
ارالك را نز گفته‌اند .
بیلو ) بفتح ثالت بر وژن بینوا ؛ دارو
فروش وعطار باشدا .
پیلو ار ۲ ت بسکون ثالث بروزن‌یشکاره
کتابه ازسیار بسیارباشد .
بو اه - بر وزن‌بیابایه ؛ مرغکی‌است
یله سس با ثانی مجهول بوزن حیله ,
اسل ابرمشم و غوزه ابرشم که کرم تنیده باشد
-رکرم ابرشم رادیز گویند ۴ و مطلقخر یضرا
هم کفته‌اند - ونوعی ا زگیاه ودارو باشد سوچشم
وبلك چشم را نیز بطریق تشبیه میگوبند - وهر
کره را گونند عموما - و گرهیرا کویندخصوسا
که درمیان دتبل بهم میرسد و ا آلرا بر لماور ند
دلیل نيكٌ نمیشود - وچرلك وربمی که‌ازمیان زخم
برمی آ ید وروان میشود - وسحرا و زمین خشك
< 46۵
شده باشد بمنی از دوطرف آن زمین دو رودخانه
میرفته باشد با يك رودخانه در شاخ شود و آن
زمین درمیان درابد - و بمعنی پیکان جر حم
امفط امن
فبله و د - بانانیمجهول بروزن‌تيش هکره
شخصی که دارو واجنای عطاری وسوزن و آبر‌شم
ومهره و امثال ان خانها گرداند وفروشده ِ
بل‌هوالی «کنابه از ابر باشد که
عربان سحاب گویند .
یمان - با میم بروزن کیوان, شرط
وعهد - و خویش وپیوند | گوید.
آداب جهانداری از مه بادکه‌اواين پیغعبرعجمان
9 3
لیها ٩4‏ ح بر وزن میخانه ؛ نلرفی که
بدان چیز ها پیمایند و انرا بعربی قفیز بروژن
مویز گوشد - ۳ قدح شرابخوریران ز گفته‌اند.
بیمانه بر شدن « کنانه ازصرباخر
رسیدن باشد .*
۴ از: پبل + وار(بار) مانند: خروار»
ومشانهةٌ علوی مردند.» «سهقی صس ۱۳۷*.
۴ بهمه شهر بود ازاو آذین
۵ - چو دریته باشد چهداند کسی
در بریشم چو کرم پبله زمن 5
عنصری بلخی. د لت فرس * 4۱-8؟.
که جوهر فروش است ببا پیلمور ؟
===== leaf 675 =====
بح
«یینکی» برروزن زیر کی غذودنی باشد
ین ۱ با نون بروزن لموء کشك‌باشد
که دوغ نرش خشك‌شده‌است‌ویعربی اقطوبتر کی
چکده رانیز گونشد که
روغن آ ترا نگرفته باشند ۰
ا۶ ۰
بنو له یپ مسکون‌کاف» سمعنئی بیتواست
که قروت و کشك باشد؟ .
پینو وا با واو بروزن گیسوها ۰ 9
آش است .
لیفه _ « بروزنکینه, پارچه که بر کفش
وجامه وخرقه دوزند- وپوست دست ویا واعضارا
یز گوبند که بسبب کار کردن سخت وسطبر شده
باشد .
بو ِ بقتح اول و تانی بواو کشیده ,
کلوخ را کونند که پارچپای گل خشكث شده‌باشد.
و با ثالث مجهول‌مرضی است که آنرا رشته گویشد
وازاعنای آدمی ۳ هی آ بد.
بو‌ار بروزن شیراز» شیر ه راگوننده
فقروت خوانند - وماست
وآنرا مرغ عیسی خوانند .
یواسته آم بروزن پبراسته . برج قلمه
وحصار -- وفصیل را گویه ,
یوس ه بکر اول و واو مجهول بر
وزن ف-وی, بمعنی انتظلار باشد- وطمم و توقعوا
فلز گویت ۳
لیو ست ع»_بفتح اول بر وزن لی‌بست ۰
ییعنی سوسته است که همیشه ودأیم وهدام باشلس
ویمعنی پیوند هم هست که ماضی پیوسئن وپیود
کردن و الحاق باشد- و باسطلاح .-حنفین‌وسول
سالك است از قید شید بدرجهٌ اطلاق حققت
اسدای ای فان لس ای
شد ۵ .
پیوستگان + مر کباترا گونند همچو
نبات وجماد وحیوان ٩‏ .»
مق ست4 » بروزن برجسته, بمعنی‌هميشه
ودایم باشد - ویمعنی پیوند کرده شده و در عم
پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
کون د که از بیاری کریستن تواند مخن گفتن
وگن کوند گر برمخنش أفد رد
. مازندرانی کتونی
برادران را بوسف چو داد گندم وجو
اگر بناعت مزجاه . پشم و پینو بود
۳ - رشك: سنو .
```


## [2026-09-05T13:49:33.447Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 28 (p.18) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==29' HUB.txt | head -40",
 "description": "Print Hübschmann p.18"
}
```


## [2026-09-05T13:49:34.508Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN band/bastan/bandar ===\"\ngrep -n \"bandar\\|band 'Band\\|bastan\\|band-i\\|banda 'Sklave\\|bende\" HRN.txt | head -30",
 "description": "grep Horn"
}
```


### [2026-09-05T13:49:34.945Z] TOOL RESULT

```
=== HUB leaf 28 (p.18) ===
- 18 -
aller Erklarungsversuche noch vollkommen dunkel.
Ap. Grundform *avamaiti-, zd. *avama^ti'?
110. Np. hamhd^ nach Zenker = 'Mitspieler ist gebildet
aiis ham 'derselbe' = ap. hama- und "^baz ^SpieF (vgl.
haz^. *Spier), also = Masselbe Spiel spielend'. Dagegen
braucht anhdx 'Genosse, Theilhaber nicht zu baxtan
spielen*, bdzi 'Spiel' zu geh5ren, sondern kann z. B.
zu skr. bhaj *Antheil geben, Antheil erhalten' (vgl.
'bhdjin theilhaftig*), zd. baz 'zutheilen* gehoren. Das
anlautende an- ist regelrecht aus ap. ham vor Ver-
schlusslauten entstanden (siehe den zweiten Theil
unter m),
114. Hier fehlt zd. hanjamana- *Versammlung'.
115. Trotz Horn's Hinweis auf ctdan = Wnmeln, lesen,
pflticken, schneiden' lasst sich anjtdan, pr. anfinam
(Sal. Shuk. p. 53) 'zersehneiden, zerstiickeln' (vgl.
anjan-tdan *findere') init skr. sam-ci *aufschichten, zu-
sammenlegen, ansammeln' nur schwer vereinigen. Phi.
andUan 'krunimen' habe ich friiher zu skr. anc *biegen'
gestellt.
117. Der „Bedeutungswechsel* von zd. hafitaday- 'zusam-
menlaufen lassen' zu np. anddz- Verfen, entwerfen,
messen' ist nicht erkl^rt. Die Laute stimmen.
120. Vgl. afgh. plandar *Stiefvater von plar 'Vater' wie np.
pidandar von pid = pidar. ^)
121. Np. andarx^ar *passend' stimmt nicht gut zur Wzl.
svar glanzen*. Auch ist es mit dieser Wurzel irn Zend
(von hvar- 'Sonne' und x^arenah- 'MajestS,t' abgesehen)
wie im Iranischen schlecht bestellt, da zd. x^'aretd- und
x'^ared^a- (bei Justi = Glanz) nicht 'Glanz' bedeuten.
122**" (p.254). Salem ann's Gleichung: ati/a8t*Spinngewebe'
= ap. *ha(n)basta' kann auch ich nicht fiir richtig halten.
Naher liegt es, np. anbast, anbasta *ligatus' = zd. ham
-\- basta- 'gebunden , skr. sambaddha^ *zusanimenge-
bunden, geschlossen' zu setzen.
') So Btimmt auch afgh. plar-marai 'Waise' zu np. pidar-murda
'Waise' - dem der Vater gestorben ist.
```


### [2026-09-05T13:49:34.982Z] TOOL RESULT

```
=== HRN band/bastan/bandar ===
2294:'Band'; phlv. bastan, band; ai. [/"bandh- , badhndü,
2383:230. bende *Sklave, Diener'.
2814:eine pir ergebende Oontraction aus paruviya' sehr unwahrscheinlich ist.
4851:Suffix -gän^ wie in x^idälgät?, bäzärgän^ bendegän (E[»igraphia indica
5537:621. rund, runde In Reisfeldern lebender Vogel*.
6682:Abendessen* (259); sar. /?/w, yidg. säm.
9675:hä-i maxfty ausgesprochen, z. B. bende-ye isläm.
11746:bendegan 539 Anm.
15701:I bastan 219.
```


## [2026-09-05T13:49:44.822Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN anfast/anbast ===\"\ngrep -n -i \"anfast\\|anbast\\|Spinngewebe\" HRN.txt | head -20\necho \"=== HRN 219 context ===\"\nsed -n '2285,2310p' HRN.txt\necho \"=== HRN 230 context ===\"\nsed -n '2375,2400p' HRN.txt",
 "description": "Horn entries 219, 230, anfast"
}
```


### [2026-09-05T13:49:44.883Z] TOOL RESULT

```
=== HRN anfast/anbast ===
=== HRN 219 context ===
g. vistara 'Bett, Bettzeug .
vi-\- [/^star- 'ausbreiten, *vistarana-; vergl. gusf erden
(No. 921).
Da np. bister nicht *Kleid' bedeutet, so hat Fr.
Müller (WZKM. 4, 259) kein Recht, es — abgesehen
von der Nebenform guster — von aw. vastra- ab-
zuleiten.
219. besten 'binden', Praes. bend-em., bend,
ap. basta^ gebunden'; aw. [/"band- 'binden', banda^
'Band'; phlv. bastan, band; ai. [/"bandh- , badhndü,
bandhd",
kurd. bastin, bandim; oss. d. battun, t. bäffin (59);
bei. bandag, n. banday, band (25, 26, vielleicht LW.);
wa;^. wändam, §ij/n. sar. windam.
220. biis 'Hals, Mähne (des Pferdes)' ^).
aw. 6ama- 'Rücken des Pferdes ; oss. d. barze, t. bärz
'Nacken' (55).
^) Daneben ftts, wohl falsch. Es kommen eine ganze Reihe
unberechtigter / vor.— 51 —
Dazu LW. bei. busk, Pferdename, arm. hars
(Hübschmann, ZDMG. 44, 560).
221. beS-, bis-, Praefix, s-; vergl. usnäti (No. 89).
ap. abis *bei, zu; aw. aitris,
bei. sa- (360) (?).
de Lagarde, Persische Studien, 74. Doch kommt
man auch aus, wenn man überall mit Hübschmann
=== HRN 230 context ===
(Studien II, 94).
^) Hübschmann, No. 61, wirft zwei verschiedene arm. bun
zusammen. Vergl. auch S. Bugge KZ. 32, 5, der Indog. Forsch. I,
455 noch arm. p^unj dazu stellt.— 53 —
(vgl. de Lagarde, GgA. 1871 Seite 1103, 1104);
2) *6epäck', phlv. bunak *Gepäck, La^er', Nöldeke,
ZDM6. 46, 143 (vergl. bei. bunag, n. bunay (41)
*Gepäck').
230. bende *Sklave, Diener'.
ap. ba(n)daka- 'Sklave*; phlv. bandak,
231. henefSe Teilchen, bunefse^ binefse; bunefs *blau'
(Sahn. I, 48 Vers 265, 107 Vers 839)\
mäz. venewse,
phlv. vanawsak, vanatcsa Teilchen (Bund.).
ar. LW. banafsaj, syr. LW. <3J^E>:32 (de Lagarde,
Ges. Abh. 22), arm. LW. maniisak (de Lagarde,
No. 1427).
232. heng 'Bilsenkraut', bengi 'sinnlos '), vergl. metig *Hanf .
aw. batiha- ein Narcoticum, vergl. Banga-; skr.
bhatigä- 'Hanf; ein aus Hanfsamen bereitetes Nar-
coticum'; arm. LW. bang voaxiaiiiog, ar. LW. banj; af;\
bang 'RsLiif; nhd. Bangenkraut 'Schierling* (Grimm,
Wörterbuch I, 1105).
russ. penka, poln. pienka, czech. pcnek, p6nka scheinen
entlehnt (Hehn, Kulturpfl. 484). ^
233. huden 'sein, Praes. buv-em'^ vergl. bos-em, bad; buvis, 0Ou)
```


## [2026-09-05T13:49:54.011Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^122\\|122\\^\\|122a\\|122 \\.\" HRN.txt | head -10\necho \"---\"\ngrep -n \"Spinnge\\|Spinnwebe\\|anfa\\|ambast\" HRN.txt | head -20",
 "description": "Find Horn 122a"
}
```


### [2026-09-05T13:49:54.068Z] TOOL RESULT

```
1452:122. endöyiteu 'sammeln, erwerben', Praes. endöz-em,
9782:122. Anm. In dem Dialekte der kaukasischen Bergjuden
9787:122**''' enfest 'Spinnengewebe'.
10685:122. karlnttan 'schneiden; schaffen (von Anröniainyuä)',
11767:bevberüsän 122^« N.,
---
963:Die Bedeutungen von ap. l/^hanj-, frahanfam *ich
3648:ai. tfsna-; arm. vergl. farsamim welken', anfarsam
3971:nur 'Stütze, Mittel zu halten etc.*) ; bei. Janfar Mühle,
5163:aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
```


## [2026-09-05T13:49:56.494Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9780,9800p' HRN.txt",
 "description": "Horn Nachtrag 122a enfest"
}
```


### [2026-09-05T13:49:56.534Z] TOOL RESULT

```
meiner Meinung durchweg umBt gelesen werden.
113. Statt ferjaftm (Zeile 7) lies phlv. fraj(a)ftan.
122. Anm. In dem Dialekte der kaukasischen Bergjuden
finden sich ähnlich dtf/, mu-Hu/um 'nähe bezw. 'ich
'j Ziiffleioh mit VorbeRBorung einip^or Druckfehler.- 254 —
nähe' von duyße und furux, mu-furu/jim Verkaufe
bezw. 'ich verkaufe' von fitruyde.
122**''' enfest 'Spinnengewebe'.
ap. Via(m)haMa- (Säle mann, Shams i Fachrii
Ispahänensis lexicon persicuni, Casani 1887, S. 155 a).
Unsicher, man müsste eine Arabisirung annehmen.
Erst nacliträglich sehe ich die in dem genannten
Werke S. 184 im Index verzeichneten 9 Etymologieen
Salemanns, von denen sclion 2 oben erwähnt sind
(s. äfdum, No. 38 und gerzmän^ No. 906****). Np. häsre
V
'Beackerung (Vullers), Acker (SF) aus aw. väsfra-,
hevberüsän 'Volk, Gemeinde* (Varianten bei Vullers
s. V. berpernsän) aus phlv. varav(i)m und urmek —
russ. armydki 'Armäck, kameelhaarener , langer,
breiter Bauernrock' sind zweifelhaft, zu medhüs vergl.
```


## [2026-09-05T13:50:14.227Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ham basta ===\"\ngrep -n \"basta-\" BRT.txt | head -20\necho \"=== KNT basta ===\"\ngrep -n \"basta-\\|basta \" KNT.txt | head -10",
 "description": "Bartholomae/Kent basta"
}
```


### [2026-09-05T13:50:14.290Z] TOOL RESULT

```
=== BRT ham basta ===
16698:•  j.,  p. "band- V, 'binden'.  Pr^es.  8  *ba»ad-z band-'\  34  bandaya-.  —  PPfP.  basta-'^.
17044:•  j.,  p.  basta-  Adj.  (fem.  •«■),  PPfP.: s.  'band-,
=== KNT basta ===
947:*bhndh-to-, OP basta- ($85), Skt. baddhá-, cf. Eng. bound. negative prefix *n- in a-zSatna-, a-xsala-, etc. *sm-dhe, OP hadà, Skt. sahá ‘with’. I. Before a vowel ог; or у, pIE » and m must,
1210:Sometimes OP has sí instead of st; this is probably analogical to the -sf- of dental stems, such as basta- to plE *bhendh-, gasta- ‘evil’ to рЇ® *gendh- (cf. §85), since pIE Ё and §(h) gave OP @ and d in other forms of the paradigm.! The examples are:
1490:azdi and Aura-maedüh-, with -dzdh-, see $85; for basta- and gasta-, with participial -tst- re- placing -dzdh-, see §85.
1633:(1) Neg. a- before consonants, an- before vowels, from *n-; prefix ha- and ham- similarly (= Skt. sa- and sam-). Root final before dental suffixes: pIE gh and gh-t > gdh, replaced by the product of gt in OP: adurujiya and duruxiam (878.11, $242). pIE dh and dh-| > dedh, re- placed by the product of fst in OP: ba*daka and basta (§85, §242). |
2627:(§58.D), Skt. baddhá-, but Av. basta-, OP basta-. pIE *gendh-: OP gasta- ‘evil’, cf. Skt. gandhd-
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
3532:82 буа : pasiva : adam : fràifayam : Üvjam : hauv : Аспа : basta : anayatà : abiy : ma
3618:75 iy : І casam : avajam : duvarayamaiy : basta : adáriya : haruva$im : К
3633:90 maiy : basta : adáriya : haruvasim : kara : avaina : pasavasim : Arbair&yá :
3764:88 düha : Vidafarnà : Babiruviya : aja : uta : basta : anaya : Varkazanahya : màhy& : XXII : ra 89 ucabié : dakata : аһа: avafà : атат : Arzam : hya : Nabukudracara : a
```


## [2026-09-05T13:50:15.464Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK fascis ===\"\ngrep -n \"fascis\\|bhasko\" POK_full.txt POK_01.txt | head -20\necho \"=== IEC bhendh ===\"\ngrep -n -i \"bhendh\\|bhondh\" IEC.txt | head -10\necho \"=== SYN bind ===\"\ngrep -n \"bhendh\" SYN.txt | head -10",
 "description": "Pokorny fascis, Mann, Buck"
}
```


### [2026-09-05T13:50:15.549Z] TOOL RESULT

```
=== POK fascis ===
POK_01.txt:1514:lat.  fascia  ,Binde,  Band,  Landstreifen^,  fascis  ,Bund,  Bündel,  Paket; das  Rutenbündel  mit  hervorragendem  Beil  als  Zeichen  der  Herrscher- gowal t^;
POK_full.txt:10565:Latin fascia^ bandage, band, girdle, girth, strap, land stripe ', fascis^ alliance, bundle, 
POK_full.txt:31449:Old Irish grinne {*grend-n-io-) "bundle, fagot, bunch, fascis'; (common Celtic -ns-, -nt- > 
=== IEC bhendh ===
1203:bheidh- (bheidhtis, bheistis, tio) “stability; pledge; faith". WP II, 139 Gk. (Hom.) peisa ((peace' or “confidence. Context: ‘his heart rested in —; Daco-Moe- sian -beista (in the name Bura-beista, partly glossed in Gk. Aria-peithes); Lat. cf. fid- ücia beside (1) in fides (but fidus); Alb. besé *pledge, trust; Gaul. cf. bessu (queried: *cus- tom); Olr. béss, id.; Br. boaz, pl. boasiu, id. (Note: some Greek examples containing peis- derive from a root bhendh-, q.v.). Cf. bhoidh-
1226:bhendh- ‘bind’. WP II, 152 Skt. badhnāmi, -nīmi (radical: bandh-); Per. bandam; Thrac. bend-; Gk. cf. peisma (‘cable’, fr. *bhendhsmn-); Cf. Lat. of-fendix; Go. -bindan, and comm. Gmc. Per. LW in Arm. band “prison”
1227:bhendheros, bhendhros ‘kinsman, mate’. WP II, 152 Gk. pentherós, pentherá 'father-, mother-in- law’; Li. befidras ‘colleague’; adj. jointe’); Latv. biedrs, id.
1444:bhndh- “bound; binding'. See bhendh-. WP cf. II, 152 Skt. baddháh; Oss. cf. bándàn ‘string’; Tokh. B cf. panto ‘peace’; Gk. cf. em-pásso ^weave- in, embroider’; lá-pathos (Cpitfall'. Cf. ləu- catch") beside Hes. pásma ‘peduncle’; prob. also páthne, beside phátne ('stable, manger’. For sense cf. MHG banse: EME boose); Lat. cf. (e- or zero-grade) of-fendix ('slipknot, strap-buckle" or sim.); Ir. bann ‘bond, belt, hinge, chain, law’; Br. bann ‘skein’; MHG bunt, -des ‘band, fetter, knot; OE bund ‘bundle’; ON cf. bundinn ‘sheaf. Variant (*bhndhtó-) in Av. bastō, Per. baste
1507:bhendhos, à, us “band, thong; company. WP II, 152. Cf. bhendh-, bhndh- Skt. bandháh, bándhuh; Av. bañdð; Per. band; LW in Arm. band; Lat. & LLat. funda (2) ‘bezel; satchel, wallet; Go. bandi and comm. Gmc., also as LW in It. Fr, etc.; ON (uml.) bendi, benda “band, cord" beside bendr ‘bent’; Li. bandà Cherd LW?)
1508:bhondhst- (extn. of bhondh-, q. v.) Olr. béss ‘custom’; MHG bast ‘seam; bark beside buost ‘bastrope’; Go. bansts Chan", i-st.); OFris. boste ‘pledge of marriage’); ON bast “cord of inner bark’, cf. val-bost *hilt- thong. (A form *bhondhs- is represented in MHG banse; ON báss; EME boose, boosy)
16681:som-. The following cpds. arise in the lan- guages as given -bheudh- in Skt. & ON; -bhondh- in Skt. Av. ON; -bhüt- in Skt. E Gmc. (cf. MHG samfte ‘easy, slow, comfortable’: OE séfte "soft -dhét- in Skt. & Li.; -dhrt- in Skt. & Arm., cf. -dhor- in Li. sán-daras, -dara: -eimi in Skt. & (variant) Latv. cf. sa-eju; sa-eima, f.; -dhos, -dha in Skt. Slav & Balt.
17312:-stos (-stom) (1) noun-formant, extending verbal root, giving an active mng. Cf. Av. basto (“bundle?: bhendh-); Per. baste ‘bound’; Arm. Gut. gs; put'o (“haste, zeal: speud-); Alb. bisht (*tail': bhid-); Go. maíh- stus, m. (dung': migh-); Du. mest, G Mist, id.; E. Du. mist (fog: migh-); G. EM dunst, Du. dons, OE düst (vapour: dhum-); Go. lustus (/desire': Iubh-); MHG list, sm. & sf. id.; luste, adj. “pleasant? (see next); OHG herbist, sm. (harvest, autumn": kárp-); G Rost (rust: rudh-); MHG last, sm., OE hlæst, sn. (“bur- den": cf. OHG. OE hladan, sv. 6); OCS otü- pustü ((remission': paus-); Cz. rost, m. Cgrowth': ordh- or ard-); Li. spaüstas (“press- button’: speud-)
17313:-stos (-stus) (2) adjective-formant extending a símplex Per. baste (“bound?: bhendh-); Gk. gnostós Cknown": £ndu-); Alb. i angshtë (^wild, rug- ged": angh- or angh-); i lashtë ('early': lad-); Lat. angustus (‘narrow’: angh- or angh-); au- gustus (high': aug); MHG cf. luste (‘plea- sant’: lubh-); OCS pustü (‘empty’: paus-); OPr. pausto, id.; Gk. cf. ápaustos, adj. (“un- ceasing’); Li. añkštas (‘narrow’: ang- or angh-); áukštas (“high?: aug-)
=== SYN bind ===
3526:2. Grk. sevfepds, in Homer only ‘wife’s father’, later generalized at the expense of éxupds (and sometimes used also for ‘son-in-law, brother-in-law’), fem. evOepa : Skt. bandhu- ‘relative’, bandh- ‘bind’, IE *bhendh-. Walde-P. 2.152.
13766:1, IE *bhendh-. Feist 93,
18291:and cdiste fr. NE coach. _ W. ben (men) : Gall. benna ‘genus vehiculi’, Grk. ¢arvn ‘crib, manger’, orig. of wickerwork, fr. IE *bhendh- in Skt. bandh-, Goth. bindan ‘bind’, etc. Walde- P. 2.152.
34224:5. Lith. bendras (also as sb. ‘partner, companion’), fr. IE *bhendh- ‘bind’ in Goth. bindan, Skt. bandh-, etc. (9.16). Walde-P. 2.152.
```


## [2026-09-05T13:50:22.564Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1500,1525p' POK_01.txt\necho \"--- page? ---\"\nawk 'NR<=1514' POK_01.txt | tr -cd '\\f' | wc -c\necho \"=== POK_full around 10565 ===\"\nsed -n '10550,10575p' POK_full.txt",
 "description": "Pokorny context for fascis"
}
```


### [2026-09-05T13:50:24.501Z] TOOL RESULT

```
WP.  II  135,  WH.  I  96,  Specht  Dekl.  87.
bharek'i-  oder  bhetek^-  ,vollstopfen,  zusammendrängen^.
Gr.  (pQdooio,  cpqctTTO)  {*q)gay.i(o  aus  *bhrku-)  ,schließe  ein,  umhege,  dränge zusammen^,  cpqay.xög  ^eingeschlossen*^,  mit  sekund.  y:  Aor.  icpQocyrjv  (Schwy- zer  Gr.  Gr.  I  760),  cpQayixoQ  usw.,  epid.  cpäqyixa  aus  '^(paqY,a^ia,  ÖQV-(p\_Q](XYaoq ,hölzerner  Verschlagt,  dazu  q)VQyiog-  TsTxog  Hes.;
111
1  t  farciö,  -Ire  ,(voll)stopfen^  mästen^^  fartxts  ,gestopft,  dicht^,  vielleicht f^^qa-ens,  -tis  ^gedrängt  voll,  zahlreich,  häufig^;
Ir   harc  f.  _, Ansturm  (bes.  der  Wellen/;  hingegen  stammt  mir.  harc  L F  stuu'^^  ^^'0^1  ^^^^  gallo-rom.  *har{i)ca  ^Holzhaus^  (vgl.  Bollelli  L'It.  dial.
17,  i47°f.);
toch   A  präkär,  B  präkre  ,fest^  (Van  Windekens  Lexique  100).
\VP.  II  134 f-;  ^VH.  I  456  f.,  Loth  RC.  38,  303 f.    Zweifel  bei  EM  332.
bbares-  ,Gerste^
Lat.  fctr  (eig.  farr),  farris  n.  ,Dinkel,  Spelt;  Schrot,  MehP  aus  *far(o)s, *far(e)zes  (bzw.  *fars,  *fars-es)  =  osk.  far^  umbr.  far]  lat.  farina  ,MehF Caus  *farrlna)^  farreus  ==  umbr.  farsio,  fasiu  ,farrea^;  got.  hariz-eins C=3  lat. /arma)  ;aus  Gerste^,  aisl.  harr  m.  ,Korn,  Gerste^,  ags.  here  ,Gerste^ (*b(ir(a)z-,  bzw.  *ha7'(i)z-)]  aber  slav.  *barsina-  in  aksl.  brahno  ,Nahrung^, skr.  bräsno  ,Mehl^,  russ.  börosno  ,Roggenmehl^,  nach  Jokl  Miletic-Festschr. (1933)  119  ff.  vielmehr  zu  1.  bher-  ,tragen^    Vgl.  auch  hhares-  S.  109.
WP.  I  134,  WH.  I  455  f.,  864.
bbasko-,  etwa  ,Bund,  Bündelt
Maked.  ßdayuoL '  ös(Tf4,ol  cpovydvcov  und  ßaa-/,svTai '  (paGylösg  (dies  die  echt oT.  Lautform),  äy/AXai  Hes.;  vielleicht  hierher  gr.  qxxa/.coXog  ,Ledersack^;
lat.  fascia  ,Binde,  Band,  Landstreifen^,  fascis  ,Bund,  Bündel,  Paket; das  Rutenbündel  mit  hervorragendem  Beil  als  Zeichen  der  Herrscher- gowal t^;
mir.  basc  , Halsband^,  abrit.  bascauda  ,eherner  Spülkessel^  (vielleicht  ur- .sprüngl.  ein  irdenes  über  einem  geflochtenen  korbartigen  Gerippe  ge- formtes und  gebranntes  Gefäß),  cymr.  baich  , Bürde,  Last^,  mbret.  bech, nbret.  beac'h  ds.;  gallo-rom.  *ambi-bascia  ,Last^,  alyonn.  ambaissi  ,mesure pour  les  fagots^  (Jud  Rom.  47,  481  ff.).
WP.  II  135  f.,  WH.  I  97,  459  f.
bhSsO'  oder  bheso-  ,größere  Raubvogelart^
Ai.  bhäsa-h  ,ein  bestimmter  Raubvogel^;   gr.  hom.  att.  q)i^yr]  ,eine  Adler- art,  wahrscheinlich   Vultur    monachus^  aus  *bhäs-na  oder   *bhes-nä]  auch *bhänä  (zu  1.  bhä-)  wäre   möglich. WP.  II  135.
bhät-  :  bhot'  ,schlagen,  stoßend
Lat.  fatuus  ,blödsianig,  fade  von  Geschmack^  (*vor  den  Kopf  geschla- gen, stumpf);  gall.  Lw.  lat.  battuö,  -ere,  jünger  battö  ,schlagen,  klopfen, stampfen'^,  daraus  rückentlehnt  cymr.  bathu  ,Münzen  schlagen^,  vgl.  auch
112
gall.  anda-hata  ,Blindkänipfer;  Gladiator,  der  mit  einem  Helm  ohne  Öffni gea  kämpft';  mit  ä:   russ.  haH  ^Eichenstock,   KnütteF,    skr.  hdtati  ,scl gQn,   klopfen^;   vielleicht   auch    (mit  ä)    russ.  hötath   ^trampeln,   schauke! usw.;   vielleicht   älter    däa.  had   ^Kampf;  Schade^,   mnd.  hat  ^Schade, glück*^;,  iihd.  Blutbad.
Unklar  ist  das  Verhältnis  zu  *hliäut-  (s.  unten);  ist  statt  Hhät-  etj *bhuät-  anzusetzen,  oder  liegt  eine  Wz.  *bhä-  mit  verschiedenen  Forma tien  zugrunde,  die  vielleicht  in  lat.  fämex,  -icis  ,Blutunterlauf'  (*durj| Schlag  entstandene  Blutgeschwulst)  vorliegt?
WP.  II  126  f.,  WH.  I  46,  99,  452,  464.
1.  bhMu'  :  bha-  ,schlagen,  stoßend
--- page? ---
120
=== POK_full around 10565 ===

Note: 

Root/ lemma: b^asko-: "bundle, heap' is a truncated formation of an older root *b'^eA'^-sko 

from which derived both Root/ lemma: b^^ed^.^; -to bow, bend' and Root/ lemma: b^asko- 

: "bundle, heap' (see below). The alledged root *bhed*^-5Ao derived from b^eig!^- [common 

lllyrian -gb-> -db-]. 

Material: Maked. paoKioi Ssapoi cppuyavcjov and paoKsuTai (paaKi5£(; (these genuine gr. 

vowel form), ayKoAai Hes.; perhaps here gr. (paoKLokoq " leather sack '; 

Latin fascia^ bandage, band, girdle, girth, strap, land stripe ', fascis^ alliance, bundle, 
parcel; the fasces with excellent hatchet as a token of the imperious power '; 

Note: common Latin ph- > f- shift 

Maybe alb. i6'as/7/re "together, bound', it'asMo/T/" put together, unite', basbkel\eece (a 
bundle of wool)'. 

Note: 

Alb. proves that from an early root *bheig!^- [common lllyrian -gb-> -db-] derived Root/
```


## [2026-09-05T13:50:45.605Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T13:50:45.611Z] TOOL RESULT

```


```


## [2026-09-05T13:50:48.534Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بنده ===\"\ngrep -n \"بنده\" MON_part1.txt | head -5\necho \"=== MON فاشیسم ===\"\ngrep -n \"فاشیسم\\|فاشیست\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -8\necho \"=== ARY latin index band ===\"\ngrep -n -i \"bhendh\\|BANDA\\|BAND \" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "grep Mo'in and Aryanpur"
}
```


### [2026-09-05T13:50:48.615Z] TOOL RESULT

```
=== MON بنده ===
1881:با آب و مواد چسبنده» که به وسیلةٌ قلم موی 
2142:| بنده, 
2156:اجل: اه ل. ۰ (ص.) آبنده» يس آینده. 
2829:ازاده؛ (0-)22202 (ص.) آنکه بنده کس 
2830:ناشد» حر)؟ مق. بنده» عند. آزاد کرده» 
=== MON فاشیسم ===
MON_part2.txt:4253:سیاسی فاشیسم باشد. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4253:سیاسی فاشیسم باشد. 
=== ARY latin index band ===
2724:2? Jo lay 44 UDRAG 65g UDRAr olen g slaty ly pls tsi Band ger 9210 a
3672:BANDAYAITI —:(SANSKRIT) 21 Sit BASTA (OLD PERSIAN) slenly go
3774:BAND (OLD FRISIAN) oS 53.3 BANDA AVESTAN) gers)
3775:(OLD HIGH GERMAN) pf glST BAND (OLD PERSIAN) lea
3776:BANT, BANTA BAND L(PAHLAV!) 5 shay
3777:BAND (GERMAN) galt BERBEND, BENDIK (KURDISH) 62,6
3778::(OLD ENGLISH) Si BAND :(AFGHANI) Gy) il
3780:BAND ENGLISH) p=S&i\ BANDHA
3782:BAND (SWEDISH) «5h yo -FEND (DEFEND, MATIN) ZV 4
3783:BAND NORWEGIAN) $333 OFFENDS) | *
```


## [2026-09-05T13:50:53.966Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/turban",
 "prompt": "Give the full etymology entries for turban and, if present on the page, tulip: source languages, dates, forms (Turkish tülbent, Persian dulband/dolband), and what is said about the first element dul-."
}
```


## [2026-09-05T13:50:55.539Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%86%D8%AF%D8%B1",
 "prompt": "Give the Persian entry بندر (bandar): etymology (is it from بند band + -ar? or from Sanskrit?), meaning 'port', and any Arabic borrowing note (banādir)."
}
```


### [2026-09-05T13:51:00.606Z] TOOL RESULT

```
# Etymology of Turban and Tulip

## Turban
**Date:** 1560s
**Etymology chain:** French *turbant* (15c.) → Italian *turbante* (Old Italian *tolipante*) → Turkish *tülbent* "gauze, muslin, tulle" → Persian *dulband* "turban"

The source notes that "the change of -l- to -r- may have taken place in Portuguese India and subsequently spread to other European languages." A potential Latin connection to *turbo* ("spinning top, that which whirls") is mentioned as possibly coincidental but potentially influential on European forms.

## Tulip
**Date:** 1570s
**Etymology chain:** Dutch or German *tulpe*, French *tulipe* → Turkish *tülbent* "turban," also "gauze, muslin" → Persian *dulband* "turban"

The flower received this name from "the fancied resemblance of the flower to a turban." The full Turkish form appears in Italian *tulipano* and Spanish *tulipan*, though Germanic languages dropped the *-an* suffix.

## Note on *dul-*
The page provides no analysis of the first element *dul-* in Persian *dulband*. The etymology terminates at the Persian form without further etymological breakdown.
```


### [2026-09-05T13:51:00.812Z] TOOL RESULT

```
# Persian Entry: بندر (bandar)

**Etymology:**
The Persian etymology is incomplete. The entry notes a possible composition from بند (band, "band, tie") + در (dar, "door"), stating this "makes phonetic and semantic sense, but is there literature to confirm this?" No Sanskrit origin is indicated for the Persian term itself.

**Meaning:**
Port or harbour. The entry lists "port" and "harbour" as primary definitions.

**Arabic Borrowing:**
Classical Persian بَنْدَر (bandar) was borrowed into Arabic, where it appears as بَنْدَر (bandar) with the plural form بَنَادِر (banādir). The entry explicitly states the Arabic term was "Borrowed from Classical Persian."
```


## [2026-09-05T13:51:07.653Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/basket",
 "prompt": "Give the etymology of basket: is it derived from Latin fascis or bascauda? What does it say about the origin being obscure?"
}
```


## [2026-09-05T13:51:07.969Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/banner",
 "prompt": "Give the etymology of banner: Old French baniere, Late Latin bandum, Gothic bandwa 'sign' — and what PIE root is given for bandwa?"
}
```


### [2026-09-05T13:51:12.656Z] TOOL RESULT

```
# Etymology of Basket

The origin of "basket" is disputed. According to the source, the word comes from Anglo-French *bascat*, but its ultimate origin remains unclear. One theory proposes a Latin connection: it may derive from Latin *bascauda* ("kettle, table-vessel"), which the Roman poet Martial supposedly traced to Celtic British origins, potentially linking it to Latin *fascis* ("bundle").

However, the Oxford English Dictionary is skeptical of this theory. The source notes that "there is no evidence of such a word in Celtic unless later words in Irish and Welsh, sometimes counted as borrowings from English, are original."

Regarding obscurity, the entry explicitly states the word's origin is "of obscure origin despite much speculation." This indicates that despite various theories and scholarly debate, etymologists cannot definitively establish where "basket" truly originated.
```


### [2026-09-05T13:51:13.691Z] TOOL RESULT

```
# Etymology of Banner

According to the Online Etymology Dictionary, the word "banner" traces back through several languages:

**Etymology Chain:**
- Old French *baniere* ("flag, banner, standard")
- Late Latin *bandum* ("standard")
- Gothic *bandwa* ("a sign")

**PIE Root:**
The Proto-Indo-European root given is **\*bha-** (1), meaning "to shine." The entry states that *bandwa* comes from "suffixed form of PIE root *\*bha-* (1) 'to shine.'"

This etymological connection links "banner" to the concept of something visible and conspicuous—fitting for a distinguishing military or heraldic standard.
```


## [2026-09-05T13:51:21.196Z] TOOL CALL #41: WebSearch

```json
{
 "query": "دولبند dulband etymology Persian turban دستار برهان قاطع"
}
```


## [2026-09-05T13:51:22.376Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/dulband",
 "prompt": "Is there a Persian entry dulband/دولبند? Give its etymology and meaning if present."
}
```


### [2026-09-05T13:51:24.519Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T13:51:30.138Z] TOOL RESULT

```
Web search results for query: "دولبند dulband etymology Persian turban دستار برهان قاطع"

Links: [{"title":"دلبند - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AF%D9%84%D8%A8%D9%86%D8%AF"},{"title":"turban - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/turban"},{"title":"Turban","url":"https://en.wikipedia.org/wiki/Turban"},{"title":"Persian: Turban -> dulband | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-turban-dulband.2299714/"},{"title":"Hejazi turban","url":"https://en.wikipedia.org/wiki/Hejazi_turban"},{"title":"The turban","url":"https://www.custom-qamis.com/en/blog/presentation-of-the-blog/the-turban"},{"title":"Sarpech","url":"https://en.wikipedia.org/wiki/Sarpech"},{"title":"Turban (disambiguation)","url":"https://en.wikipedia.org/wiki/Turban_(disambiguation)"},{"title":"دولبند - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D9%84%D8%A8%D9%86%D8%AF"}]

Based on the search results, here's what I found about the etymology and usage of دولبند (dulband):

## Etymology and Meaning

Dulband is a Persian word referring to a type of headwear based on cloth winding, and it's also the root of the word "tulip".

## Linguistic Journey

The English word "turban" was borrowed through a linguistic chain: from Classical Persian دلبند (dulband), to Ottoman Turkish دلبند (tülbent), to Italian turbante, and finally to Middle French turbant.

## Etymology Theories

One theory about the word's composition comes from an 1903 Anglo-Indian dictionary, which claims that the "dul" element of dulband is from Arabic دول, which connotes turning or rotating (i.e., the process of wrapping or tying a turban).

## Modern Usage

Interestingly, while "dulband" was used in Classical Persian, the word never made it into Modern Persian, which uses 'ʿammāme' from Arabic. However, in Modern Turkish the cognate word 'tülbent' is still used, but only to mean 'muslin, gauze'—the cloth a turban is often made of.

Regarding the other terms you mentioned (دستار and برهان قاطع), these don't appear in the search results, so I cannot provide information about them at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T13:51:35.947Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"dulband\\|dulband\\|TURBAN\" HJB.txt | head -20",
 "description": "grep Hobson-Jobson turban"
}
```


### [2026-09-05T13:51:35.992Z] TOOL RESULT

```
1657:to  controL  Since  the  annexation  of the  Fanjab,  however,  they  have  ceased to  give  trouble.  The  Akalee  is  dis- tinguished by  blue  clothing  and  steel armlets.  Many  of  them  also  used  to carry  several  steel  ckaknu  (CHUCKEB) encircling  their  turbans.  [See  Ihhetson^ Panjah  Eth/nog.^  286 ;  Madagan^  in Panjab  Census  Rep.,  1891,  i.  166.]
2901:1731. — "The  Bnaign  (as  it  proved,  for  his fint  appearance,  being  undressed  and  in  his bansroa  coat,  I  did  not  know  him)  came  off from  his  cot^  and  in  a  ver^  haughfy  manner cried  oat,  *None  of  your  disturbance,  Grentle- men.'  "—In  Wheeler,  iii.  109.
3677:„  "...  the  85th  Regiment,  commanded by  Major  Popham,  which  had  lately  behaved in  a  mutinous  manner  .  .  .  was  broke  with infamy.  .  .  .  The  black  officers  with  halters about  their  necks,  and  the  sepoys  stript  of their  coats  and  turbands  were  drummed  out of  Uie  Cantonments."— /n<iia  Gazette,  March 30.
3741:BOBBEBY,  8.  For  the  origin  see BOBBEBY-BOB>  A  noise,  a  disturbance, a  row.
3753:BOBBEEY-PAGEI,  s.  A  pack  of hounds  of  different  breeds,  or  (oftener) of  no  breed  at  all,  wherewith  young officers  hunt  jackals  or  the  like ;  pre- sumably so  called  from  the  noise  and disturbance  that  such  a  pack  are  apt to  raise.  And  hence  a  '  scratch  pack ' of  any  kind,  as  a  *  scratch  match'  at cricket,  &c.  (See  a  quotation  under BUNOW.)
5424:1672. — "They  call  the  common  priests Caiis,  or  by  another  name  Schierifi  (see 8HEsEEF)i  who  like  their  bishops  are  in  no way  distinguished  in  dress  from  simple  lay- men, except  by  a  bigger  turban  .  .  .  and  a longer  mantle.  .  .  ."—P.  Viiuxnzo  Maria,  66.
5800:1662. — "Turbans,  long  coats,  trowsers, -shoes,  and  sleeping  on  ch£rpddB,  are  quite  un- usual. " — J{,  of  Mir  Jum/a's  Invasion  (^  Assam, -tranal.  by  Blochmann,  J.A.S.B.  xli.  pt.  i.  80.
6547:(a.)  s.  A  quoit  for  playing  the English  game ;  but  more  properly the  sharp  quoit  or  discus  which  con- stituted an  ancient  Hindu  missile weapon,  and  is,  or  was  till  recently, carried  by  the  Sikh  fanatics  called Akdli  (see  AKALEE),  generally  en- circling their  peaked  turbans.  The thing  is  described  by  Ta vernier  (E.  T. ii.  41  :  [ed.  Ball,  i.  *82])  as  carried  by a  company  of  Mahommedan  Fakirs whom  he  met  at  Sherpiir  in  Quzerat. See  also  Lt.-CoL  T.  Lewin,  A  Fly,  &c., p.  47  :  [Eijerton,  Handbook,  PI.  15,  No. 64].
7929:OULQEE,  s.  A  jewelled  plume surmounting  the  sirpeth  or  aigrett* upon  the  turban.  ShakesDear  gives kalghi  as  a  Turki  word.  [Ratts  gives ka^hdy  kalghly  and  refers  it  to  SkU kalaiOy  'aspire.']
7930:c.  1514. — ''In  this  manner  the  peo^e  of B&r&n  catch  great  numbers  of  herons.  Tlie KiUd-M;  ['Plumes  worn  on  the  cap  or turban  on  great  occasions. '  Also  see  Pvi^ab Trade  Heporif  Appi.  p.  cczv.]  are  of  the heron's  feathers." — Baher^  164.
7969:1810.— "They  generally  have  the  turbans and  <mniniiir»himH«  of  the  same  colour,  by way  of  livery."— Tri//tdiii«m,  F.  M,  i.  274.
7971:1880.—".  .  .  The  Punjab  seems  to  have found  out  Manchester.  A  meeting  of  native merchants  at  Umritsur  .  .  .  describes  the e£Fect8  of  a  shower  of  rain  on  the  English- made  turbans  and  Kumiiierlrands  as  if  their heads  and  loins  were  enveloped  by  layers  of starch."— Pumper  MaU,  June  17.
11551:1670.— They  desire  that  dungarees  may be  supplied  thence  if  possible,  as  "they were  not  procurable  on  tne  CrOaiit  of  India* by  reason  of  the  disturbances  of  Sevajee." — Notei  and  Ext$.,  Pt.  i.  2.
12567:1809. — *^  On  pa^ng  a  yisit  to  any  Asiatic Prince,  an  infenor  receives  from  him  a complete  dress  of  honour,  consisting  of  a khelant,  a  robe,  a  turban,  a  shield  and sword,  with  a  string  of  pearls  to  go  round the  neck."— Ld.  Vaieniiay  i.  99.
12848:1574.— "These  Persians  are  also  called lUd  Turl-Sf  which  I  believe  is  because  they have  behind  on  their  Turbants,  Bed  Marks, as  Cotton  Bibbands  &c.  with  Bed  Brims, whereby  they  are  soon  discerned  from  other Nations."— Aowflo//,  178.
13502:1613.— "The  Macareo  of  waves  is  a  dis- turbanoe  of  the  sea,  like  water  bailing,  in which  the  sea  casts  up  its  waves  in  foam. For  the  space  of  an  Italian  mile,  and  within that  distance  onlv,  this  boiling  and  foaming^ occurs,  whilst  aU  the  rest  of  the  sea  is smooth  and  waveless  as  a  pond.  .  •  .  And the  stories  of  the  Malays  assert  that  it  l» caused  by  souls  that  are  passing  the  Ocean from  one  region  to  another,  or  going  in  ea/ilas- from  the  Golden  Chersonesus  ...  to  the- river  Ganges." — Oodinho  de  Eredia^  f.  4l9. [See  Skeat,  Malay  Magic,  10  teq.]
14287:**  So  saying,  Buddh Silently  laid  aside  sandals  and  staff. His  sacred  thread,  turban,  and  cloth,  and
15068:sense  as  our  word,  quoting  the  Arabian Nights  (Macnaghten's  ed.,  L  176,  and iL  159X  in  both  of  which  the  word indicates  the  material  of  Afine  turban. [Burton  (i.  211)  translates  *  Mosul stuflf,'  and  says  it  may  mean  either  of <  Mosul    fashion,'    or    muslin.]     The
15775:"In  the  enumeration  of  certain objects,  the  Malay  has  a  peculiar idiom  which,  as  far  as  I  know,  doea not  exist  in  any  other  language  of  the Archipelago.  It  is  of  the  same  nature as  the  word  *head,'  as  we  use  it  in  the tale  of  cattle,  or  '  sail '  in  the  enumera- tion of  ships  ;  but  in  Malay  it  extends to  many  familiar  objects.  Alai^  of which  the  original  meaning  has  not been  ascertained,  is  applied  to  such tenuous  objects  as  leaves,  grasses,  &c. ; Batana,  meaning  *  stem,'  or  '  trunk,'  to trees,  Iocs,  spears,  and  javelins ;  Bantak^ of  which  the  meaning  has  not  been ascertained,  to  such  oojects  as  rings  ; Bidangy  which  means  'spreading'  or 'spacious,'  to  mats,  carpets,  tnatch, sails,  skins,  and  hides ;  Biji^  *  seeds,^ to  corn,  seeds,  stones,  pebbles,  gems,, eggs,  the  eyes  of  animals,  lamps,  and candlesticks,"  and  so  on.  Crawfurd names  8  or  9  other  terms,  one  or other  of  which  is  always  used  in company  with  the  numeral,  in  en- numerating  different  classes  of  objects^ as  if,  in  English,  idiom  should  compel us  to  say  *two  stems  of  spears,'  *four spreads  of  carpets,'  *six  corns  of diamonds.'  As  a  matter  of  fact  we do  speak  of  20  head  of  cattle,  10  JiU  of soldiers,  100  sail  of  ships,  20  pieces  of cannon,  a  dozen  stand  of  rifles.  But still  the  practice  is  in  none  of  these cases  obligatory,  it  is  technical  and  ex- ceptional ;  insomuch  that  I  remember,, when  a  boy,  in  old  Reform-Bill  days» and  when  disturbances  were  expected in  a  provincial  town,  hearing  it  stated by  a  well-informed  lady  that  a  great proprietress  in  the  neighbourhood  M*as so  alarmed  that  she  had  ordered  from town  a  whole  stand  of  muskets  I
16465:[PAMBBE,  s.  An  ai-ticle  of  dress which  seems  to  have  been  used  for various  purposes,  as  a  scarf,  and perhaj)S  as  a  turban.  Mr.  Y.usul  Ali {Mwiograph  on  Silk  Fabrics,  81)  classes it  among  'fabrics  which  are  simply wrapped  over  the  head  and  shouldera by  men  and  women ' ;  and  he  adds : "The  Pamii  is  used  by  women  and children,  generally  amongst  Hindus." His  specimens  are  some  3  yards  long by  1  Droad,  and  are  made  of  pure  silk or  silk  and  cotton,  with  an  ornamental border.  The  word  does  not  appear  in the  Hind,  dictionaries,  but  Molesworth has  Mahr.  |w?marl,  *a  sort  of  silk  cloth.'
```


## [2026-09-05T13:51:37.023Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D9%84%D8%A8%D9%86%D8%AF",
 "prompt": "Give the full Classical Persian entry دولبند (dulband): etymology (compound analysis, first element dul-), meaning, descendants (Ottoman Turkish tülbent, Italian turbante, tulip)."
}
```


### [2026-09-05T13:51:43.493Z] TOOL RESULT

```
# دولبند (Dulband) - Classical Persian Entry

## Etymology
The word is a compound formation: دول (dōl, "revolving") + بند (band, "band, tie"). As noted in the source, it's cognate with Northern Kurdish *dorbend* ("frame").

## Meaning
This archaic Persian term encompasses three related senses:
1. A turban or the sash/wrapping of a turban
2. A diadem or crown
3. A hat

## Descendants
The entry documents one key descendant: **Ottoman Turkish دلبند (dülbend)**, with a note indicating "further descendants" exist through that Ottoman form.

## Note on Extended Descendants
While the prompt mentions Italian *turbante* and the word "tulip," these specific terms and their etymological connections to دولبند are **not documented in the provided Wiktionary entry**. The source only traces the descent to Ottoman Turkish, which then spawned additional descendants not detailed here.
```


## [2026-09-05T13:51:52.747Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB TURBAN headword ===\"\ngrep -n \"TURBAN\\|Tulipan\\|dulband\\|tulband\" HJB.txt | head -10\necho \"=== SOD bntk / entry 105 ===\"\ngrep -n \"βntk\\|Bntk\\|bntk\\|servant\\|slave\" SOD_pages.txt | head -20",
 "description": "Hobson-Jobson turban, Sogdian"
}
```


### [2026-09-05T13:51:52.811Z] TOOL RESULT

```
=== HJB TURBAN headword ===
22559:TURBAN,
22564:This,  however,  is  quite  inconsistent with  the  history  of  the  word.  Wedge- wood's  suggestion  that  the  word  may be  derived  from  Fr.  turhiriy  *a  whelk,' is  equally  to  be  rejected.  It  is  really a  corruption  of  one  which,  though  it seems  to  be  out  of  use  in  modern Turkish,  was  evidently  used  by  the Turks  when  Europe  first  became familiar  with  the  Ottomans  and  their ways.  This  is  set  forth  in  the  quota- tion below  from  Zedler's  Lexicon, which  is  corroborated  by  those  from Rycaut  and  from  Galland,  &c.  The proper  word  was  apparently  dulband, Some  modern  Persian  dictionaries  give the  only  meaning  of  this  as  *a  sash.' But  Meninski  explains  it  as  *  a  cloth of  fine  white  muslin;  a  wrapper  for the  head ' ;  and  Viillers  also  gives  it this  meaning,  as  well  as  that  of  a  *  sash or  belt.'*      In  doing    so    he  quotas
22566:Shakespear's  Diet.,  and  marks  the  use as  *  Hindustani-Persian.'  But  a  merely Hindustani  use  of  a  Persian  word could  hardlv  have  become  habitual  in Turkey  in  the  15th  and  16th  centuries. The  use  of  dulband  for  a  turban  was probably  genuine  Persian,  adopted  by the  Turks.  Its  etymology  is  ap- parently from  Arab,  dul,  ^volvere,^ admitting  of  application  to  either  a girdle  or  a  head-wrap.  From  the Turks  it  passed  in  the  forms  Tulipant, Tollibany  TurbatUy  &c.,  into  European languages.  And  we  believe  that  the flower  tulip  also  has  its  name  from  its resemblance  to  the  old  Ottoman  tur- ban, [a  view  accepted  by  Prof.  Skeat (Concise  Did.  s.v.  tulip,  turban)].*
22576:*  Bu8bec<][  (1554)  says :  " .  .  .  ingens  ubique florum  copia  offerebstur,  Narcissorum,  Hyacin- thornra,  «t  eorum  quos  Turcae  Tulipan  vocant," —Epist.  L  Bl2e>ir  ed.  p.  47.
22577:TURBAN,
=== SOD bntk / entry 105 ===
2330:and slaves - the total Sogdian population of that                colophon says it was srYc'nch kndh (the city of SrY
3204:                            slave        Olr. *bandaka~         with Olr. */0rl and, in a parallel way, /z/ with Olr.
8391:                                                                         attendant, servant
8397:      servant                                                            (o)spasc    Osp'sy) ©MP    fsp\syg    ©pi. -t(hh ob.
8399:                                                                         servant
8405:1598 Vnch        B, S                        I^jl^&.gi                  attendant, servant, attached to service
8413:1599 'sp'nt'rmS =» spnd)rmd                                             girl-servant, maid
8420:                                                                        girl-servant, maid
11354:                                                                    servant, slave
11377:2652 pntJ B, S                                                         servant, slave
11398:     servant, slave                                               2671 pr-    B, M, S    (u>>>-
13599:                                                                  slave girl, female servant
13604:      judge                                                         TPS 1959, 10; 5}y pwsty, Frye 15, 16, 21 "slave
13609:      judge, judging justly                                       document about a slave girl
14791:     indifferent, negligent                                                obedient, enslaved
24184:     slave girl, concubine
24196:     concubine, slave girl                                          dirt
29343:                                                                    servant
38109:document about a slave girl 3455      dropping      1951                      easier 4484
38161:elephant keeper    8328                        enslaved    3907                        Eve    5475
```


## [2026-09-05T13:51:59.911Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3190,3215p' SOD_pages.txt\necho \"=== page tag ===\"\nawk 'NR<=3204' SOD_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -2\necho \"=== 2652 pntk ===\"\nsed -n '11370,11385p' SOD_pages.txt",
 "description": "Sogdian bandaka entry"
}
```


### [2026-09-05T13:52:01.703Z] TOOL RESULT

```
                     brin                                                     M kmby                   Av. kamna-
 /pay/ pY-           lord,g god      OP    baga-
                                     * a- bar a-                  uzb         M wjp\ terror            Av. azoba
 /apar/      *fir-
 /Yrap;              understand                                               C }wzb-
              YrP-                   *grba-
 Yarp/                                                            2) [d] occurs after n and z.

 2) /5/ Voiced dental spirant < *d:
 /8as/ 6s-              ten         Av. dasa-
 /m66an/     mySyn       middle        Av. maidydna-           113. To this, the loss of initial Olr. */», common to most
 /p*8/       p>6         foot          Av. pdd-                     Eastern Iranian languages, should be added.
 3) /y/ Voiced velar spirant < *g:                             114. These examples show the allophone [ts] of [c\
                                                       xxxni
                            slave        Olr. *bandaka~         with Olr. */0rl and, in a parallel way, /z/ with Olr.
  Pande       B finth
              M findyh                                          */drl. The B and some                  M    forms     still    keep   the
                                                                historical spelling.
  azdyu       B >ztyw       exiled       Olr. *uzdahyu-
  3) [;] occurs after n:                                        /se/               B ^Sry, sy,             three        Av. tfraya-
                                                                                   M 'dry, C jy
  anjaman     M ynjmn-        assembly      *ham-gamana-
                                                                /wispise/          Bwyspydr*k\
                                                                                   M wyspsy                prince      Av. visopuOra-
  4) [g] occurs after n:
  angust      B ynkwst;    finger        Av. angusta-
=== page tag ===
=== 2652 pntk ===
      (3and (bnt1) ©Yaghn. vant ©ace. -w; pi. -ff
      bond, fetter                                                2666 bntsq =» p-, pw-
      TSP 9.115, 129; SCE 362; BSTBL, Dhu. 202; Frag.             2667 pnty     S =» bnty
         Len. 46.16; Hen. JRAS 1944, 138; C2 gloss.;
                                                                  2668 bnty     C                                    J&sj^^
         flnth, MSP bl04
                                                                       Pande (pnty) ©pi. -u ob. pi. -ry; voc. bnty
2652 pntJ B, S                                                         servant, slave
     Pand (Pnd\ bnr) ©3pl. pres.; ind. & subj. &                       STi 8.11, 45.7; Sund. AoFviii 1981 p214; STii 6.8;
         impf. =>P-t Pw-, wPnd                                            BSTi 130 etc.; BSTii; C2 gloss.; bnt\ STi 47.6;
       GMS 787, 795, 798, 799; AVS 227-8                                 C2, 22R7; bntyu STii 4.25, 3.28; bntyty, STi
2653 pnt3 S                                                <=«,          39.6; C2, 23V28-, CII, 1990 p82
                                                                  2669 bntypy C
       Pand                                                                                                       ( jG-i-j)jl»Of-^j
       parcel                      r
                                                                       Bande pay ^Pntp's'k                               ~3'J>*J
```


## [2026-09-05T13:52:10.778Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nL=$(awk 'NR<=11377' SOD_pages.txt | tr -cd '\\f' | wc -c); echo \"leaf=$L printed≈$((L-66))\"\ngrep -n \"\\[pdf page\" SOD_pages.txt | head -3",
 "description": "Find SOD printed page for entry 2668"
}
```


### [2026-09-05T13:52:12.449Z] TOOL RESULT

```
leaf=170 printed≈104
```


## [2026-09-05T13:52:19.467Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4245,4260p' MON_part2.txt\necho \"=== MON بنده entry ===\"\nsed -n '2140,2160p' MON_part1.txt",
 "description": "Mo'in fascism and bandeh context"
}
```


### [2026-09-05T13:52:19.532Z] TOOL RESULT

```
فاش شدن ۱-04۸۱ [ع. ف.] (مسصل.) 
آشکار شدن» ظاهر شدن. فاش شدن خبر: 
برا کنده شدن خر. 

فاشوریدن: 27 (مص‌ل.) تحر یک 
شدن, برانگیخته شدن. 

فا ستشت. اعأَک] (ص.) آنکه پبر و شلک 
سیاسی فاشیسم باشد. 

فاصل: اد [ع ۰] (افا.) جدا کننده دو چبز 
از هم. . حد فاصل: آنجه میان دو چیز فاصله 
باشد؛ پرزخ. خط فاصل: خطی که دو چیز را 
از هم جدا کند. جدا کنننده حق از باطل. 
قاطم . 

=== MON بنده entry ===

اتیه: (»)2(ناة [ع.] (افا. نث.) مونث آتسی» 
| بنده, 

آثاره ۲ (ع.] (ا.)+ ج. اثر؛ نشان‌هاء نشانه‌ها. 
آثار سفلی: اثرهای طبایع و آثار چها رگانه. 
آثار علوی [ع. الا ثار العلوية] (امر.) نزد قدما 
یکی از شعب طبیعی» در معرفت علل 
حدوت حوادث جوی. 

آجر: 2 (معر. آگور] (.) خشتی که در 
کوره پخته باشنده خشت بخته. 

اجل: ا2[2 ,101 ( 0( 2 با صدا! از گلو 
بر آید» آروع. آرغ. 

اجل: اه ل. ۰ (ص.) آبنده» يس آینده. 
مدت‌دار) دیرآینده. آخرت؛ مق. عاجل. 
آجودان: 2012۳ افسری (صاحب منصبی) 
که نزد افسر عالی‌رتبه خدمت کند. افسری 
(عاعت‌شصی) که انی سحوله ا یط وت
```


## [2026-09-05T13:52:29.088Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) section for بنده: its origin tag (e.g. [په.] Pahlavi) and glosses. Also quote the لغت‌نامه دهخدا etymology if it mentions Pahlavi bandak or Old Persian bandaka."
}
```


## [2026-09-05T13:52:34.973Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/turban' --note 'page 87, root Bhendh, node 4-6: turban < Fr turbant < It turbante < Turkish tülbent < Persian dulband' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://www.etymonline.com/word/basket' --note 'page 87, root Bhendh, node 15: basket of obscure origin, not from Latin fascis' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://www.etymonline.com/word/banner' --note 'page 87, root Bhendh, node 22-23: banner < OFr baniere < LL bandum < Goth bandwa, PIE *bha- to shine' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/بندر' --note 'page 87, root Bhendh, node 3: Persian bandar = band + dar; Arabic loan banadir' >/dev/null 2>&1; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/دولبند' --note 'page 87, root Bhendh, node 2: Classical Persian dulband = dol revolving + band' >/dev/null 2>&1; echo DONE; tail -6 data/verification/sources/web/index.jsonl",
 "description": "Archive web sources"
}
```


### [2026-09-05T13:52:36.990Z] TOOL RESULT

```
# Etymology of بنده (Bande)

## From Farhang-e Mo'in (معین)

The dictionary entry shows: **(بَ دِ) [په.] (اِ.)** indicating Pahlavi origin. The glosses provided are: "1 - God's creature 2 - slave 3 - servant, slave 4 - obedient, submissive 5 - I, this servant"

## From Dehkhoda Dictionary

Dehkhoda traces the word through historical Persian: *"from the infinitive 'bastan' (to bind), plural bandagan. In Pahlavi: 'bandag' (بندک). In Old Persian: 'bandaka.'"* The dictionary notes these forms meant slave or servant, with the root sense of "one who is bound."

## Etymology Chain

The documented progression shows:
- **Old Persian**: *bandaka*
- **Pahlavi**: *bandag* 
- **Persian**: *bande* (derived from the infinitive "bastan")

This represents a continuous Iranian linguistic development rather than a borrowed term, with the semantic evolution from the literal sense of "bound" to the social role of "servant/slave."
```


### [2026-09-05T13:52:39.229Z] TOOL RESULT

```
DONE
{"url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86", "file": "data/verification/sources/web/745e236e6d16c36d.txt", "fetched": "2026-09-05T13:51:24Z", "status": 200, "bytes": 3533, "title": "برازیدن - Wiktionary, the free dictionary", "note": "page 91 verification (Bher5/bhreu-, Bhereg)"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0reh%E2%82%81%C7%B5-", "file": "data/verification/sources/web/96ce948a8f51f3ef.txt", "fetched": "2026-09-05T13:51:37Z", "status": -1, "bytes": 39, "title": "", "note": "page 91, root Bhereg 'to shine'"}
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%A7/", "file": "data/verification/sources/web/c6d1088929ab0d82.txt", "fetched": "2026-09-05T13:52:26Z", "status": 200, "bytes": 4251, "title": "بلوا - معنی در دیکشنری آبادیس", "note": "page 91, Persian balvâ: Dehkhoda/Mo'in entry"}
{"url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D9%89", "file": "data/verification/sources/web/1ddec17b8b6fd73d.txt", "fetched": "2026-09-05T13:52:27Z", "status": -1, "bytes": 39, "title": "", "note": "page 91, Arabic balwā root b-l-w"}
{"url": "https://en.wiktionary.org/wiki/بندر", "file": "data/verification/sources/web/cd47b1fe14463023.txt", "fetched": "2026-09-05T13:52:38Z", "status": 200, "bytes": 13080, "title": "بندر - Wiktionary, the free dictionary", "note": "page 87, root Bhendh, node 3: Persian bandar = band + dar; Arabic loan banadir"}
{"url": "https://en.wiktionary.org/wiki/دولبند", "file": "data/verification/sources/web/069fc96d7641819e.txt", "fetched": "2026-09-05T13:52:39Z", "status": 200, "bytes": 3681, "title": "دولبند - Wiktionary, the free dictionary", "note": "page 87, root Bhendh, node 2: Classical Persian dulband = dol revolving + band"}
```


## [2026-09-05T13:52:48.136Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D9%87/' --note 'page 87, root Bhendh, node 11: Mo\\'in and Dehkhoda on Persian bandeh < Phl bandag < OP bandaka' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0end%CA%B0-' --note 'page 87, root Bhendh: PIE *bhendh- to bind' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/fascism' --note 'page 87, root Bhendh, nodes 16-19: fascism < It fascismo < fascio < L fascis' 2>&1 | tail -2\ngrep -c . data/verification/sources/web/index.jsonl\ngrep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.jsonl | tail -12",
 "description": "Archive more sources"
}
```


### [2026-09-05T13:52:49.805Z] TOOL RESULT

```
Exit code 1
(eval):6: unmatched "
```


## [2026-09-05T13:52:54.554Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D9%87/' --note \"page 87, root Bhendh, node 11: Moin and Dehkhoda on Persian bandeh < Phl bandag < OP bandaka\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0end%CA%B0-' --note \"page 87, root Bhendh: PIE bhendh- to bind\" 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/fascism' --note \"page 87, root Bhendh, nodes 16-19: fascism from It fascismo from fascio from L fascis\" 2>&1 | tail -2\ngrep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.jsonl | tail -10",
 "description": "Archive more sources"
}
```


### [2026-09-05T13:52:57.946Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a76aaae41a31ded3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53419b8c90931a51.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e89f3fd83c4004f6.txt
"url": "https://abadis.ir/fatofa/%D8%A8%D9%84%D9%88%D8%A7/"
"url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D9%89"
"url": "https://en.wiktionary.org/wiki/بندر"
"url": "https://en.wiktionary.org/wiki/دولبند"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berhtaz"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/berk%C5%8D"
"url": "https://en.wiktionary.org/wiki/breath"
"url": "https://www.etymonline.com/word/braise"
"url": "https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D9%87/"
"url": "https://www.etymonline.com/word/fascism"
```


## [2026-09-05T13:53:01.636Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -n \"turban\\|basket\\|banner\\|bend\\|bʰendʰ\\|b%CA%B0end\" data/verification/sources/web/index.jsonl | tail -8",
 "description": "Verify archived urls"
}
```


### [2026-09-05T13:53:01.679Z] TOOL RESULT

```
862:{"url": "https://www.etymonline.com/word/turban", "file": "data/verification/sources/web/7d1c22c026822efc.txt", "fetched": "2026-09-05T06:41:28Z", "status": 200, "bytes": 6824, "title": "Turban - Etymology, Origin & Meaning", "note": "page 87, root Bhendh, English/French chain (turban, tulip, banner, basket)"}
863:{"url": "https://www.etymonline.com/word/tulip", "file": "data/verification/sources/web/e1bd5e76455966e8.txt", "fetched": "2026-09-05T06:41:28Z", "status": 200, "bytes": 7189, "title": "Tulip - Etymology, Origin & Meaning", "note": "page 87, root Bhendh, English/French chain (turban, tulip, banner, basket)"}
864:{"url": "https://www.etymonline.com/word/banner", "file": "data/verification/sources/web/fd4aa9cfa016978e.txt", "fetched": "2026-09-05T06:41:29Z", "status": 200, "bytes": 6467, "title": "Banner - Etymology, Origin & Meaning", "note": "page 87, root Bhendh, English/French chain (turban, tulip, banner, basket)"}
865:{"url": "https://www.etymonline.com/word/basket", "file": "data/verification/sources/web/1233e4c816dc4e0c.txt", "fetched": "2026-09-05T06:41:29Z", "status": 200, "bytes": 6627, "title": "Basket - Etymology, Origin & Meaning", "note": "page 87, root Bhendh, English/French chain (turban, tulip, banner, basket)"}
869:{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0end%CA%B0-", "file": "data/verification/sources/web/53419b8c90931a51.txt", "fetched": "2026-09-05T06:41:30Z", "status": 200, "bytes": 6435, "title": "Reconstruction:Proto-Indo-European/bʰendʰ- - Wiktionary, the free dictionary", "note": "page 87, root Bhendh, PIE reconstruction and descendants"}
```


## [2026-09-05T13:53:14.435Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN turban ===\"\ngrep -n \"turban, n\\|tulip, n\" KLN_1966.txt KLN_1971.txt | head -6\necho \"=== SKT turban/tulip ===\"\ngrep -n -i \"TURBAN\\|TULIP\" SKT.txt | head -6",
 "description": "Klein/Skeat turban tulip"
}
```


### [2026-09-05T13:53:14.548Z] TOOL RESULT

```
=== KLN turban ===
KLN_1971.txt:255005:tulip, n. — F. tulipe, earlier tulipan (cp. It. tulipa- 
KLN_1971.txt:255237:turban, n. — F. turban , earlier turbant, tulban. 
=== SKT turban/tulip ===
11726:mite  (z),  a  verv  &maU  portion.    (P M.  E,   mite.  -  O.   Du.   mijt,  mUt,  ■ small  coin,  a  mite.     Lit  '  cut  small  ;* Teuc.  base  MIT,  to  cut  (above). Mitigate.   (L.)     From  pp.  of  L. gart,  to  make  gentle.  ••  L*  mitis^  £( 'igare,  for  agerr^  to  make. Mitre,  a  head-dress,  esp.  for  a (F.-L.-Gk.)    O.F.  mi'/«-L.tw** cap.  —  Gk.  ^tirpa,  a  belt,  girdle. 61lct.  turban.
19814:Toil  (1  J,  labour;  to  labour.  (F. M  £.  toti,  disturbance,  titmalt;  Ml pull  about  (the  sense  having  son altered). »0.  F.  (ouilier,  to  entangie, together,  mix  coafuserity,  tronbte.  Ai Cotgrave.  Frob.  from  a  ftequenticiv of  U.  H.  G.  nitcchen  (G.  tU£Xtn\  to  1 pull  quickly ;  cf.  O.  H.  G.  aoeciJa,  t tear,  snatch  away,  ifigSn,  to  Icat,  pi derivatives  from  O.  H.  G.  tihaet  (.G.J to  pull;  see  Tow  (i).  %  7W  k derived  from  O.  Da.  htyUn^  t» manuie  land,  but  it  is  impossible  10  4 it  from  this  source;  the  M.  E.  u completely  at  vaiiance  with  this  \-iri
20281:vuffix  -d,^r  (  '  L.  -d/K^Mw),  — Lk  tut  us, ort  for  tuitus  (above). tutal&r.  (U)     L.  tutr/arii,  protecting, L  fut-ur,  short  for  tuttus  (above). tutor.  (.!' )    I'  /w/tfT.  a  guardian,  tutor. t^.  tut'US  (aVove). KUip :  see  Turban. ^Imbl«,    vb.     (£.)      M.  E.    tmmhien  ; !f|HcnL  oi  tpmhfn^  tumd^n,  to  tuinMc  —
20296:Turban.  (F  -  Ital.  -  Turk.  -  Pcrs.  - Hind.)  Foinierly  turhant,  turribant^  tur^ band'y  also  toliffant,  tulipant,  tuhinxnt.  —  F, turhantt  turban,  a  turban  ;  Col.  —  Ital.  tur^ hanttt  'atuibant;'  Hono.  — Turk. /m/^cm^ vulgar  form  ofduiftna'.  a  turban.  —  Per&.</irA band,  a  turban.  —Hind.  dulKind,  a  turban. tulip,  a  flower.  (F.  -  Ital.  -  Turk.  - Per».-Hiwd.)  F.  tulifft.  also  tuJifnin,  a tulip;  so  called  from  its  likeness  to  a  turban.
20297:—  Ital.  tuiifa^  tulipano,  a  tulip.  — Turk.  /W- bind,  a  turban  (above).
23360:tulip — turban.
```


## [2026-09-05T13:53:24.287Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD index RIBBON ===\"\ngrep -o \"RIBBON [a-z()*-]*\" AHD_watkins1985.txt | head -3\necho \"=== CHEUNG band ===\"\ngrep -n \"\\*band\\|BAND\" CHEUNG.txt | head -10",
 "description": "AHD ribbon, Cheung band"
}
```


### [2026-09-05T13:53:24.345Z] TOOL RESULT

```
=== AHD index RIBBON ===
=== CHEUNG band ===
1593:*band ‘to bind’ 
1601:*OLD PERSIAN: *band- ‘to bind’ || (+ *ui-) ? El-OP hh.mi-ban-da PN (= OP 
1611:*band 5 
2543:water), curdle (of yoghurt)’. © These forms are perhaps contaminated with *band 
34025:*band-, 4 
55305:*band (s.v.), *čap, *darz, 
55765:*band, *daH', *hHai, Soul. 
56936:*band (s.v.), *darb 
57667:*band (s.v.)
```


## [2026-09-05T13:53:26.847Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1590,1625p' CHEUNG.txt",
 "description": "Cheung *band entry"
}
```


### [2026-09-05T13:53:26.895Z] TOOL RESULT

```
*REFERENCES: ESIJa II: 67 f. 


*band ‘to bind’ 

*AVESTAN: YAv. band- ‘to bind’ = Liste: 37 

Pres. {1} аја-: IND. 35р. YAv. bandaiieiti (V 22.5, V 5.8 Ё), INJ. Zeg YAv. bandaiiat (Y 11.7, Yt 19.77), 
med. 3sg. YAv. bandaiiata (Yt 5.128), SUBJ. 159. YAv. bandaiieni (Yt 9.18), 3sg. YAv. bandaiiaiti (Vn 
96), YAv. bandaiiät (Y 11.7); Pres. {2} them.: IND. 15р. YAv. bandami (Yt 4.5) 

*OLD PERSIAN: *band- ‘to bind’ || (+ *ui-) ? El-OP hh.mi-ban-da PN (= OP 
*vibanda-, Gershevitch apud Hinz 1975: 259; Hinz -Koch 1987: 919) = Kent: 199b 
Partic.: perf. pass. basta- <b-s-t> (DB 1.82, DB 2.75, DB 2.90, DB 5.26) 

*MIDDLE PERSIAN: BMP bnd- (’SLWN-) /band-/ ‘to bind, fetter’, MMP bn ‘bondage, 
prison; band’ || (+ *pati-) MMP pywyn- ‘to bind, join’ || (+ *pari-) BMP plwnd- 
/parwand-/ ‘to surround, enclose, contain, comprise’ || (+ *ni-) ? MMP nwn- ‘to 
begin’ > DMMPP: 108a, 291b, 248a 


*band 5 


Pres.: IND. 3sg. MMP "bynyd, 3р1. MMP bynynd, SUBJ. 2sg. MMP “bynyh, 3р1. MMP byn’nd; Partic.: 
perf. pass. MMP bstg, BMP bstk /bastag/, MMP bst, bst, Inf.: BMP bstn /bastan/, MMP bstn || (+ *pati-) 
Pres.: IND. 2sg. MMP pywynyy, 3pl. BMP ptwndynd /paywandend/; Partic.: perf. pass. MMP pywst, 
BMP pywst /paywast/; Inf.: BMP ptwstn /paywastan/; Partic.: perf. pass. MMP pywst, BMP pywst 
(YK‘YWMWN-)yt /paywast éstéd/ || (+ *pari-) Partic.: perf. pass. BMP plwstk /parwastag/ || (+ *ni-) 
Pres.: IND. 3sg. MMP nwnyd, 3р1. nwnyyd; Partic.: perf. pass. MMP nwyst, nwyst 

*PARTHIAN: bnd- ‘to bind’, IPth. bs- ‘to construct (a bridge)’ || (+ *pati-) pdbnd- ‘to 
bind’ || + *fra-) frbst- (pret. stem) ‘to close, clog, stop up’ || (+ *ui-) wbst- (pret. 
stem) ‘to undo, take off = Ghilain: 54 f., 55 | DMMPP: 108a, 268b f., 154b, 337b 
Pres.: IND. 3sg. bndyd, 3р1. bndynd; Partic.: perf. pass. bst “уа; Partic.: perf. pass. bst, IPth. bsty; Inf.: 
IPth. bstny || (+ *pati-) Pres.: IND. 3sg. pdbndyd; Partic.: perf. pass. pdbst || (+ *fra-) Partic.: perf. pass.
```


## [2026-09-05T13:54:36.546Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN leaf 394 (p.363) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==395' PHN.txt | head -30",
 "description": "Pihan p.363 turban"
}
```


### [2026-09-05T13:54:38.234Z] TOOL RESULT

```
=== PHN leaf 394 (p.363) ===
TUR 363
poli de Barbarie (f-^l cT^!^ darâhauhu» elgharb), capitale
d'une Régence de l'Afrique septentrionale, placée sous le gou-
vernement d'un bey ou pacha nommé par la Porte.
TRUCHEMAN, s. m. (a.)
{j^j3 [tardjoumân] interprète, dérivé de ^j3 [tardjam] traduire.
— Ce mot est une variante de drogman, qui est beaucoup plus
usité. — Voyez Drogman.
TURBAN, s. m. composé, (a.-p.)
Mjii [dulbend] formé de l'arabe Jj^ [dawl] tour, et du persan
[bend] bande, bandeau. Coiffure orientale à l'usage des
Arabes et des Turcs , et qui consiste en une longue pièce d'é-
toffe roulée avec plus ou moins d'élégance autour du a^sUo
[fâqiyah]j sorte de calotte. Cette étoffe est le plus souvent de
couleur blanche. Les musulmans issus de la race de Mahomet,
et considérés comme chérifs ou nobles, sont les seuls qui
puissent porter un turban vert. — Le mot turban n'est, comme
on le voit, qu'une corruption du terme oriental dulbend.
TURC, fém. TURQUE, subst. et adj. (a.)
^ji [tourk] , pluriel Jt^l [àtrâk] , dérivé du verbe arabe dij3
[tarak] quitter, abandonner, par exemple , le sol natal , les Turcs
étant considérés comme nomades. L'adjectif arabe se forme en
ajoutant un ^^ y au mot *àjJ [tourk] , et s*écrit ainsi : i^j^
[totirÂ:tyy] , féminin H^S^ \iJOur\wfyai[. — Les Turcs originaires
d'Asie s'appellent plus spécialement (^^^ [tor^mon] dont nous
avons fait Tubgomans ; et l'on entend par Turkbstan (u^^^'***^)
le pays situé à l'orient de la mer Caspienne, et habité par les
```


## [2026-09-05T13:54:38.438Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD RIBBON ===\"\ngrep -o \"RIBBON[^ ]* [a-zA-Z()*-]*\" AHD_watkins1985.txt | head -5\necho \"=== NYB bandak ===\"\ngrep -n \"bandak\\|bandag\" NYB_vol2_glossary.txt | head -5\necho \"=== WLD Bd2 152 ===\"\ngrep -n \"bhendh\\|bhend\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "AHD ribbon, Nyberg, Walde-Pokorny"
}
```


### [2026-09-05T13:54:38.517Z] TOOL RESULT

```
=== AHD RIBBON ===
=== NYB bandak ===
901:bandak
911:bandak [bndk! ;inscr. «BD-k]servant, slave SPrs: 16; 319, 516; pl. cas. obl. ~ -än 713. -
913:bandak
914:OP bandaka-; MPrth bndg; MPrs bng = bannag < bandak; Paz. banda, NP bandah.
2463:13%, but cas. obl. marté in the compound marté-karp 1049, v. karp; pl. cas. rect. ~ 5112; pl. cas. obl. —-än [GBR?-n']: gen. 28, 1512, 2523.27, P2:5 (GBR’-n); dat. 5312; agent 5319; — bandak ~ a slave 51$; varzékar =--ē a farmer 14"; ~ 4 artēštār the warrior 1316; magvé-~, még-~, v. magi; — as a mere indef. pron. 20°. 6615. 6815, 7039; — ~ 4 ahlav 3915. 829, but in pl. cas. obl. ahlavan —-än, druvandan ~-n 5312-13, — Av. (1148) marata- mars- tan-, whence MPrth mrd = Paz. NP mard ; Av. more common (ibid.) mašya- < martya- = OP martiya-, whence MPrs myrd.
=== WLD Bd2 152 ===
8047:KZ. 39, 269 f. als *bandn- zu binden, "^bhendh-, was auch nicht durch die
9054:G. Mever Wb. 36 zu "^bhendh- ,.binden"; iiber biJ ,,Eid'‘ s. bhoidh- ,,zwingen‘’r
9440:"^bhend- wegen but ,, Putter" usw.), gegen den mit dt Bauch s. u. bheug-
9527:bhendh- „wacli sein, wecken         geweckt, geistig rege, aufmerksam sein, er-
9832:                                                bLongh-j bhngb            bhend-                                 151
9882:bhend- etwa ,,singen, schon klingen, jauchzen".
9903:152                                       bhendh-
9918:bhendh- „binden‘^
9946:m. Lit.; Gdf. ^bhendh-na; nicht besser dariiber AYiedemann BB. 28, 61); mir.
```


## [2026-09-05T13:54:49.719Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o -i \"ribbon[^,]\\{0,30\\}\" AHD_watkins1985.txt | head -5\necho \"=== WLD bhendh ===\"\nsed -n '9903,9950p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "AHD ribbon and Walde-Pokorny bhendh"
}
```


### [2026-09-05T13:54:51.511Z] TOOL RESULT

```
ribbon
ribbon
ribbon: TAENIA; POLYTENE. [Pok. 1. t
=== WLD bhendh ===
152                                       bhendh-


   got.    batim jjbesser^^,   batists „best“,   aisl.   betre,      beztr,   ags.   bet{^re,   betst^

ahd.           beipst, nhd. besser, best; aisl. bati m, „Yerbesserung, Heil",
          bei^^ir,
afries. bata m. „Vorteil, Gewimi‘‘, mnd. bate „VerbesseruBg‘' ; got. gabatnan
„zunutze kornmen*", aisl. 6a^wa „besser werden^^, ahd. ba^^m ds.; got. bota
.jVorteil, ITutzen", aisl, ags. bot „Yerbesserung, Schadeuersatz^^, ahd. 6wog(a)
„Yergutung, Besserung, Heilung‘‘, nhd.              Schon wegen der Bed. frag-
wurdig    vergleicht Stokes   KZ. 40, 245  nicht exist, ir. baid „dauerhaft“.



bhendh- „binden‘^
   Ai. badhndti, erst spater bandhati (s. Meillet Msl. 17, 194) „bindet, fesselt,
nimmt gefangen, fiigt zs.“, av. bandayaiti (sehr unsicher bandaiti, s. Meillet
aaO. und Bartholomae Airan. Wb. 926) „bindet‘^, Ptc. ai. baddhd-, av. ap.
basta-, ai.  bdndhana- n. „das Binden“, bandhd- m. „das Binden, Band^‘, av.
banda- m. „Bande, Fessel“ (; aisl. as. bant, ahd. bant n. got. bandi, ags. bend f.
                                                                       ;


ds. ; lit.        „Yieh“, s. u.); ai. bdndhii- m, „Yerwandter‘' (wie nevd'SQog),
    Gr. Tteiofin „Tau, Sei?^ (aus fur "^nevd-juia geneuertem ^nhoya, s. Brug-
mann IF. 11, I04f., auch fiir neafjia und ndojna), jzevdegog „Schwiegervater‘^
(„durch Heirat verbunden“); nadvr] (spat belegt, aber alt), mit Hauch-
umstellung horn. att. cpdxvri „Krippe“ {*bhndJi-na; Liden BB. 21, 109 f. unter
einer Gdbed. „geflochtener Korb“ wie kelt. henna „AYagenkorb‘''; Solmsen
KZ. 42, 219 als „Stelle, wo das Tier im Stall angebunden wird“); thrak.
pevd^ „binden“ (vgl. Kretschmer Einl. 236); alb. bese „Yertrag, Glaube,
Waffenstillstand“ (s. Johansson IP. 19, 114ff. m. Lit.); lat. offendimentnm,
offendix „das Kinnband an der Priestermiitze"          gall, benna „genus vehi-
                                                                 ;


culi“ cymr. benn „FtLhTwerk“ (Lw.         in Belgien banne, nhd. mdartl. benne
                                           :



„Wagenka8ten“, ndl. ben „Korb, Mulde'A Liden aaO., Yf. LEAYb.^ u. benna
m. Lit.; Gdf. ^bhendh-na; nicht besser dariiber AYiedemann BB. 28, 61); mir.
buinne „Band, (Arm)reif“ (wenn ^bJiondhia^ Stokes BB. 23, 49; gegen Zu-
ruckfuhrung von air. bes{s) „Gewohnheit, Sitte'^ auf ein *bliendJi-tu oder
dgl. „*Bindung“ AYindisch IP. 3, 76 ff., Foy IF. 6, 331, Johansson IP. 19,
ll4ff., Thurneysen Hdb. 126, wendet sich wohl mit Eecht Pedersen KG. I
```


## [2026-09-05T13:55:05.138Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 497 498; do echo \"===== leaf $L =====\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -30; done",
 "description": "BQT leaves near printed 278"
}
```


### [2026-09-05T13:55:06.932Z] TOOL RESULT

```
===== leaf 497 =====
ایوان و مفه را گویند , و تک اول حم آهده
است .
بسك - بنتم اول و ثانی بالف کشیده
و بکاف زد» ؛ ناچی‌را کویند که از کلهاو رباحین
واسپرغنها و ب رکه مورد سازند , و یادشاهان
وبزر کان روز های عید و جشن ومردمان درروز
دامادی برسر گذارند , و پا پای فارسی هم بنظی
اهده است .
بسا ز لعج س بفتح اول ونون بروزنابارج»
کیاهی است بهیأت‌هز اریای و رنگش مانندرونای
سرخ میباشد» و برپوست آن گرهها بود. چون
آنرا بشکنند دروتش زردیرآبد.
بساو ند ۱ بروزن دمارند. فاف؛شر
باشد - و هر دوچیز راکه با میگ سقاشستین
داشته باشند نیز بساوند گوشد . .
بسباس ‏ بروزن کربای ۰ حرزه و بی
معنی را گوبند - و درعربی بزباز راکویند ۴
بسباسا؟ بن‌دوم بالف کشیده‌سربانی
نوعی از حرمل عربی است » و آن دوابی باشد
که بر که آن‌مانند ب رگ‌بیدبود لیک نکوچکتر
ازاست » ر کل آن مانشد باسمن سفیدو خوشبو
۱ "۳ راد: بساوند.
۴ - ر8 : سبای .
مباشد ۰ وحرهل عر نی زا سوتانی مولی‌تکولام
و شارسی صنمل دانه خوانند ؟ .
بسیایه - با بای فارسی بروزن همابه »
داروبی باشد وان بخ کیاهی است کرء دار شبیه
دارد» و بتازی اضراس‌الکلب وافب‌الحجر خوانئد.
مسهل سود آست ۵
پست » بنم اول و سکون ثانی وقوقانی»
===== leaf 498 =====
بستان تم اول بروزن برهان » کلزار
و کلسان‌را کوشد , ومشفف بوستان هم‌هت كِ
و جابی‌را نیز کویند که میوه‌های‌خوشبوق‌در آنجا
همرسد .
پستان‌افرود - کلیات سرم‌رنگ
و بی‌بوی که آنرا تاج خروس وگل بوسف نز
کوبند . وصنی اسیرغمرا که‌طیمران باشد بستان
افروز.میگویند . و بجای فا بای فارسی‌هم آمده
است .
بستان یر | -
کوبند که باغبان باشد .
بستان‌شی لن - نام توابی است از
خوسیقی .
بستاو لك » بفتح واو بروزن گل مانند؛
زمين پشته پشته زاءکونندکه کنل و کردوه‌باشد
و زمی ناهموار را نیز کنتداند . ۶
سبتتع ع نم اول و سکون انی و فتح
فوقانی و جیم ما کن , معرب بتکه است وآن
صمقی بائد که کندر گویندش » و اب یکوند
بستر ] هگ بر ارو سکون‌انی
و فتح ثالث و رای می نفطه بالف کشیده و حای
باغ ببراش دهنده را
۳ رگ : سنوه.
۱ ۳۹
مفتوح بنزن و کاف زده » جمعتین لحاف و مالن
باشد » و یی چادرثبی را کنته‌اندکه بر زوی
نزالی پوشند -
بستر دن » بروزن حلبردن »نع وکردن
و باكساختن باشد ۴
لستر سهنف‌دو » کنابه ازآش
```


## [2026-09-05T13:55:15.291Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg87.png data/verification/sources/refs/ocr/BOOK/87.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T13:55:16.803Z] TOOL RESULT

```
total 1892
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 09:55 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
```


## [2026-09-05T13:55:25.847Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -60 data/verification/sources/web/53419b8c90931a51.txt",
 "description": "Read archived PIE bhendh page"
}
```


### [2026-09-05T13:55:25.883Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0end%CA%B0-
FETCHED: 2026-09-05T06:41:30Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/bʰendʰ- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/bʰendʰ- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection
```


## [2026-09-05T13:55:28.220Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '60,160p' data/verification/sources/web/53419b8c90931a51.txt | grep -v \"^ *$\" | head -60",
 "description": "Read PIE bhendh content"
}
```


### [2026-09-05T13:55:29.950Z] TOOL RESULT

```
 1.1 
 Root 
 1.1.1 
 Derived terms 
 1.1.2 
 Descendants 
 1.2 
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ bʰendʰ- 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *bʰendʰ- [ 1 ] [ 2 ] [ 3 ] [ 4 ] 
 to bind 
 bond 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *bʰendʰ- (82 c, 0 e) 
 *bʰéndʰ-e-ti ( thematic root present ) 
 Proto-Germanic: *bindaną ( see there for further descendants )
 Proto-Indo-Iranian: *bʰándʰati 
 Proto-Indo-Aryan: *bándʰati 
 Sanskrit: बन्धति ( bándhati ) ( see there for further descendants )
 *bʰondʰ-éye-ti ( causative ) 
 Proto-Germanic: *bandijaną ( “ to bind, restrain ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *bʰandʰáyati 
 Proto-Indo-Aryan: *bandʰáyati
```


## [2026-09-05T13:56:26.812Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:03:52.561Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk87.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0end%CA%B0-\"\nW_BANDAR = \"https://en.wiktionary.org/wiki/بندر\"\nW_DULBAND = \"https://en.wiktionary.org/wiki/دولبند\"\nE_TURBAN = \"https://www.etymonline.com/word/turban\"\nE_TULIP = \"https://www.etymonline.com/word/tulip\"\nE_BANNER = \"https://www.etymonline.com/word/banner\"\nE_BASKET = \"https://www.etymonline.com/word/basket\"\nE_FASCISM = \"https://www.etymonline.com/word/fascism\"\nA_BANDEH = \"https://abadis.ir/fatofa/%D8%A8%D9%86%D8%AF%D9%87/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"banda; paiti-band\", \"verdict\": \"plausible\",\n \"derivation\": \"Av. banda- m. 'Bande, Fessel' (Bartholomae, AiW col. 925-926, s.v. banda-) is the o-grade noun *bʰondʰ-o- built to the Avestan verb band- 'binden' (pres. stem bandaya-, ppp. basta-, AiW col. 926), so the arrow root -> Avestan banda- is exact. Nourai's second form paiti-band 'to attach' is not attested in Avestan: Bartholomae has no paiti.band- entry, and Cheung (EDIV s.v. *band- 'to bind') records the *pati- compound only from Middle Iranian on (MMP pywyn- 'to bind, join', BMP paywastan/paywand-, Parthian pdbnd-). It is thus an Old Iranian reconstruction *pati-band- 'to bind on(to)', correctly pointing forward to NP payvastan (the chart's arrow to Per 3), but the label 'Avestan' overstates the evidence.\",\n \"derivation_fa\": \"اوستایی banda- «بند، زنجیر» صورت اسمی درجهٔ o از ریشهٔ هندواروپایی *bʰondʰ-o- است و بارتولومه (فرهنگ ایرانی باستان، ستون ۹۲۵–۹۲۶) آن را ذیل فعل اوستایی band- «بستن» (ستاک حال bandaya-، صفت مفعولی basta-) آورده است؛ تا اینجا ادعای نورایی درست است. اما صورت دوم یعنی paiti-band در اوستا گواهی نشده است: بارتولومه چنین مدخلی ندارد و چونگ در فرهنگ ریشه‌شناختی افعال ایرانی، ترکیب *pati- را تنها از دورهٔ ایرانی میانه (فارسی میانهٔ مانوی pywyn-، پهلوی paywastan/paywand-، پارتی pdbnd-) ثبت می‌کند. پس درست‌تر آن است که این صورت را ایرانی باستان بازسازی‌شدهٔ *pati-band- بدانیم که سرچشمهٔ «پیوستن» فارسی است؛ برچسب «اوستایی» اندکی فراتر از شواهد است.\",\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:127\", \"status\": \"supports\", \"note\": \"Pokorny IEW 127-128 s.v. bhendh- 'binden': 'av. bandayaiti ,bindet', Partiz. ai. baddha-, av. ap. basta-, ... av. banda- m. ,Bande, Fessel''  (local POK_01.txt, leaf 137 = printed 127/128). banda- is exactly the form of the node.\"},\n   {\"ref\": \"BQT:449\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaf 675 (printed ~449-450) carries the پیوست / پیوستن / پیوسته block ('بمعنی پیوند هم هست که ماضی پیوستن و پیوند کردن و الحاق باشد'); it documents the Persian word the arrow points to, but no Avestan paiti-band form appears in the OCR of that page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 925-926 s.v. banda-, band-\", \"stance\": \"supports\", \"note\": \"'j. (, p.) banda- m. \\\"Bande, Fessel\\\"' and 'j., p. band- V. \\\"binden\\\". Praes. band-, bandaya-. PPfP. basta-' (grep 'banda-' in BRT.txt, lines 16676-16712). No paiti.band- entry.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *band- 'to bind'\", \"stance\": \"partial\", \"note\": \"'*AVESTAN: YAv. band- to bind'; the *pati- compound is listed only under Middle Persian/Parthian: '(+ *pati-) MMP pywyn- to bind, join', 'BMP ptwstn /paywastan/'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.152\", \"stance\": \"supports\", \"note\": \"'bhendh- \\\"binden\\\" ... av. bandayaiti \\\"bindet\\\", Ptc. ai. baddha-, av. ap. basta-, ... av. banda- m. \\\"Bande, Fessel\\\"'.\"}\n ]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"band «بند»; payvastan «پیوستن»; dŭl-band «دولبند»\", \"verdict\": \"plausible\",\n \"derivation\": \"NP بند band 'tie, bond; dam' continues MP band [bnd] 'bond, link' (MacKenzie, CPD 17) < OIr. *banda- = Av. banda-, with no phonetic change at all; Watkins/AHD lists precisely this word under bhendh- ('Persian band, band, bandage, also a river levee'), which is Nourai's AHD:1509 and which also licenses his gloss 'dam'. پیوستن payvastan 'to join' goes back to MP paywastan, pres. paywand- (CPD 67; Cheung, EDIV s.v. *band- with *pati-) < OIr. *pati-band-: prefix pati- > MP pay- (intervocalic *-t- weakened and the -i- became the glide -y-), and the past stem *pati-basta- > paywast shows the regular Iranian -st- from *-d-t-; the chart's extra پیوند paywand is the present stem used as a noun. دولبند dulband 'turban, sash' is the same band with a first element whose analysis is contested: Pihan (Dict. étym. des mots ... dérivés de l'arabe, du persan ou du turc, p.363) and Yule-Burnell's Hobson-Jobson s.v. TURBAN take dul as Arabic دول dawl 'tour, turning' - this is exactly Nourai's note; Lokotsch no.544, following Horn no.571, reads it instead as Persian dil 'heart' ('heart-captivating'); Wiktionary analyses دول dōl 'revolving' as Persian (cf. N. Kurdish dorbend 'frame'). The band element is certain on every account.\",\n \"derivation_fa\": \"«بند» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ band [bnd] «بند، پیوند» (مکنزی، فرهنگ کوچک پهلوی، ص ۱۷) و آن از ایرانی باستان *banda- = اوستایی banda- است و هیچ دگرگونی آوایی در آن رخ نداده؛ واتکینز در پیوست ریشه‌های هندواروپایی نیز همین واژه را («Persian band ... also a river levee») ذیل *bʰendʰ- آورده است، پس معنی «سد» که نورایی داده درست است. «پیوستن» از پهلوی paywastan (ستاک حال paywand-) و آن از ایرانی باستان *pati-band- است: پیشوند pati- در فارسی میانه به pay- بدل شده و ستاک گذشتهٔ *pati-basta- با تحول قاعده‌مند d+t > st به paywast رسیده است؛ «پیوند» همان ستاک حال در جایگاه اسم است. دربارهٔ «دولبند» اختلاف هست: پیهان (ص ۳۶۳) و هابسن‑جابسن جزء نخست را عربی «دَوْل» به معنی چرخیدن می‌دانند (همان که نورایی در یادداشت آورده)، لوکوچ (شمارهٔ ۵۴۴) به پیروی هرن آن را «دل» فارسی می‌خواند، و ویکی‌واژه «دول» را واژه‌ای ایرانی به معنی «چرخان» می‌گیرد. جزء دوم یعنی «بند» در هر سه تحلیل قطعی است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_DULBAND, E_TURBAN],\n \"ref_check\": [\n   {\"ref\": \"AHD:1509\", \"status\": \"supports\", \"note\": \"AHD New College appendix = Watkins 1985 s.v. bhendh-: '5. Persian band, band, bandage, also a river levee: BUND1; CUMMERBUND. [Pok. bhendh- 127.]' (AHD_watkins1985.txt, bhendh- entry).\"},\n   {\"ref\": \"BQT:305\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 525 (printed ~305) is the long بند article with 22 senses, incl. no.9 'سدی که در پیش آب بندند' (a dam built across water) and no.12 'ریسمان و طناب' - exactly the glosses 'band, dam'.\"},\n   {\"ref\": \"SAP:491\", \"status\": \"not_checked\", \"note\": \"Sayyah, Farhang-e Sayyah, is purchase-only (fidibo); no copy on disk or on archive.org (refs_online.json kind='purchase').\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p.17 s.v. band; p.67 s.v. paywastan\", \"stance\": \"supports\", \"note\": \"'band [bnd | = P, N ~] bond, link'; 'paywastan, paywand- [ptwstn', ptwnd- | M pywst, N ~] join, connect'.\"},\n   {\"src\": \"PHN\", \"where\": \"p.363 s.v. TURBAN\", \"stance\": \"supports\", \"note\": \"'دلبند [dulbend] formé de l'arabe دول [dawl] tour, et du persan بند [bend] bande, bandeau' - Pihan is the source of Nourai's note that dul is Arabic.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 544\", \"stance\": \"contradicts\", \"note\": \"Lokotsch: pers. dulband 'Turban' [aus pers. dil 'Herz' (Horn NpEt S.127 Nr.571) und band, Praesensstamm von bastan 'binden'; also 'herzentzueckend'] - i.e. the first element is Persian dil, not Arabic dawl.\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. TURBAN (line 22564)\", \"stance\": \"supports\", \"note\": \"'The proper word was apparently dulband ... Its etymology is apparently from Arab. dul, \\\"volvere\\\", admitting of application to either a girdle or a head-wrap.'\"}\n ]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"darband «دربند»; bandar «بندر»\", \"verdict\": \"plausible\",\n \"derivation\": \"دربند darband is transparently dar 'door, gate, pass' (MP dar < OIr. *duar-, PIE *dʰwer-, which is Nourai's cross-reference to Dhwer) + band 'shut, barred', hence 'closed pass, defile' - the name of the Caspian Gate Darband/Derbent, and in common use for 'enclosed area, cul-de-sac'. بندر bandar 'harbour, port' is taken by Wiktionary as the same two elements in the reverse order, band + dar, an analysis it says 'makes phonetic and semantic sense, but is there literature to confirm this?'; the word is not attested in Middle Persian and appears only in Classical NP, so the derivation is likely but unproven. Mo'in's footnote to the Borhan article بندر (BQT vol.1, printed ~306) documents the onward loan: 'این کلمه وارد عربی سوریه و مصر شده بمعنی جامگاه و مقام، محل تجارت ... شاه بندر بمعنی وکیل التجار است' - Persian bandar was borrowed into Syro-Egyptian Arabic with the broken plural بنادر banādir (the chart's extra) and into Ottoman usage as شاه‌بندر 'consul'.\",\n \"derivation_fa\": \"«دربند» آشکارا مرکب است از «در» (فارسی میانه dar، از ایرانی باستان *duar-، هندواروپایی *dʰwer- که ارجاع نورایی به ریشهٔ Dhwer به همین سبب است) و «بند»، یعنی «گذرگاه بسته، تنگه» - نام دربند قفقاز و نیز به معنی «جای محصور، بن‌بست». «بندر» را ویکی‌واژه ترکیب همان دو جزء با ترتیب وارونه، یعنی «بند + در» می‌داند و خود می‌افزاید که این تحلیل از نظر آوایی و معنایی درست می‌نماید ولی پشتوانهٔ پژوهشی روشنی ندارد؛ این واژه در فارسی میانه گواهی نشده و تنها از فارسی دری به بعد دیده می‌شود. در حاشیهٔ معین بر مدخل «بندر» در برهان قاطع (ج ۱، ص ~۳۰۶) آمده است که این واژه وارد عربی شام و مصر شده و «شاه‌بندر» به معنی وکیل‌التجار است؛ جمع مکسر عربی آن «بنادر» است که در نمودار هم آمده. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_BANDAR],\n \"ref_check\": [\n   {\"ref\": \"FVF:98\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e vazheha-ye farsi dar zaban-e arabi, exists only as a page-viewer on noorlib.ir (refs_online.json kind='website', no local file, browser required); could not read p.98.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol.1 leaf 526 (printed ~306), s.v. بندر with Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"'بندر ... محلی باشد که قافله و تجار ...' with the footnote 'این کلمه وارد عربی سوریه و مصر شده ... شاه بندر بمعنی وکیل التجار است و سلاطین عثمانی شاه بندر را به کنسولهای خود در خارجه اطلاق کرده‌اند. (دائرةالمعارف اسلام)' - i.e. Persian > Arabic, as the chart's بنادر implies.\"},\n   {\"src\": \"MON/Wiktionary\", \"where\": \"en.wiktionary.org/wiki/بندر\", \"stance\": \"partial\", \"note\": \"'possibly بند (band) + در (dar)' with an explicit editorial doubt; the Arabic entry records 'Borrowed from Classical Persian بندر, plural بنادر (banādir)'.\"}\n ]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Turkish\", \"words\": \"tŭlbend\", \"verdict\": \"confirmed\",\n \"derivation\": \"Ottoman Turkish تلبند tülbend / dülbend is a straight borrowing of Classical Persian dulband, with Turkish front-vowel harmony (u > ü) and the usual d- ~ t- fluctuation; in Turkish the sense narrowed from 'turban' to 'the muslin/gauze it is wound from', which is all modern Turkish tülbent means. Skeat s.v. TURBAN: 'Turk. tulbend, vulgar form of dulband, a turban. - Pers. dulband, a turban.' Lokotsch no.544 gives the same: pers. dulband > tk. tülbend 'Musseline, Kopftuch daraus', tülbent 'Brautschleier', turban.\",\n \"derivation_fa\": \"«تلبند/دلبند» ترکی عثمانی وام‌واژهٔ مستقیم «دولبند» فارسی است؛ در ترکی به سبب هماهنگی واکه‌ای u به ü بدل شده و ابدال معمول d ~ t نیز رخ داده است. معنای واژه در ترکی از «دستار» به «پارچهٔ نازکی که دستار از آن می‌پیچند» محدود شده و تركی امروز tülbent را تنها به معنی «ململ، تور» به کار می‌برد. اسکیت و لوکوچ (شمارهٔ ۵۴۴) هر دو همین مسیر را ثبت کرده‌اند. ادعای نورایی درست است.\",\n \"sources\": [E_TURBAN],\n \"ref_check\": [\n   {\"ref\": \"PHN:363\", \"status\": \"partial\", \"note\": \"Pihan p.363 s.v. TURBAN gives the Persian دلبند dulbend and its analysis (Arabic dawl + Persian bend) and says 'Le mot turban n'est ... qu'une corruption du terme oriental dulbend', but he labels the word '(a.-p.)' Arabo-Persian and does not set out the Turkish intermediate stage that this node asserts.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Turban\", \"stance\": \"supports\", \"note\": \"'F. turbant ... - Ital. turbante ... - Turk. tulbend, vulgar form of dulband, a turban. - Pers. dulband, a turban.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 544\", \"stance\": \"supports\", \"note\": \"'hieraus tk. tülbend \\\"Musseline, Kopftuch daraus\\\", tülbent \\\"Brautschleier\\\", turban \\\"Turban\\\"'.\"}\n ]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"plausible\",\n \"derivation\": \"Empty pass-through box; the French link is turbant (15c.), modern turban. The standard authorities insert an Italian stage that the chart's arrow Turkish -> French leaves out: Etymonline 'from French turbant (15c.), from Italian turbante (Old Italian tolipante), from Turkish tülbent'; likewise Skeat, Klein and Lokotsch 544 (tk. > it. turbante, frz. turban). The l > r dissimilation is placed by Etymonline in Portuguese India rather than in Turkish or French.\",\n \"derivation_fa\": \"این خانه در کتاب تهی است و تنها حلقهٔ فرانسوی زنجیره را نشان می‌دهد: فرانسوی turbant (سدهٔ ۱۵م) و سپس turban. همهٔ مرجع‌های معتبر (اتیمانلاین، اسکیت، کلاین، لوکوچ ۵۴۴) میان ترکی و فرانسوی یک مرحلهٔ ایتالیایی (turbante) می‌گذارند که نمودار آن را انداخته است؛ ابدال l به r را نیز به قلمرو پرتغالی هند نسبت می‌دهند نه به ترکی یا فرانسوی. بنابراین جهت کلی درست است ولی زنجیره ناقص است.\",\n \"sources\": [E_TURBAN],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1971 ed. s.v. turban\", \"stance\": \"supports\", \"note\": \"'turban, n. - F. turban, earlier turbant, tulban.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 544\", \"stance\": \"partial\", \"note\": \"'afrz. tolleban, frz. turban, it. turbante, sp. pg. torbante \\\"Turban\\\"' - Italian stands beside French in the chain.\"}\n ]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"turban\", \"verdict\": \"confirmed\",\n \"derivation\": \"English turban is first recorded in the 1560s, borrowed from French turbant/turban; earlier English spellings (turbant, turribant, tolibant, tulipant - Skeat) still show the -l- of the Turkish form. The sense stayed 'oriental head-wrap' throughout. The whole chain Persian dulband > Turkish tülbend > Italian turbante > French turbant > English turban is uncontroversial.\",\n \"derivation_fa\": \"واژهٔ انگلیسی turban از دههٔ ۱۵۶۰م گواهی شده و وام‌گرفته از فرانسوی turbant/turban است؛ صورت‌های کهن‌تر انگلیسی (turbant، turribant، tolibant، tulipant) هنوز l صورت ترکی را نگه داشته‌اند. معنای واژه در سراسر این راه همان «دستار شرقی» مانده است. کل زنجیره «دولبند فارسی › تلبند ترکی › turbante ایتالیایی › turbant فرانسوی › turban انگلیسی» مورد اتفاق است و ادعای نورایی درست است.\",\n \"sources\": [E_TURBAN],\n \"ref_check\": [\n   {\"ref\": \"AHD:1382\", \"status\": \"not_checked\", \"note\": \"the main-dictionary pages of the AHD New College ed. (1975/76) are not on disk (only Watkins' IE-root appendix); archive.org's americanheritag00morr is lending-restricted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. turban\", \"stance\": \"supports\", \"note\": \"'turban, n. - F. turban, earlier turbant, tulban.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Turban\", \"stance\": \"supports\", \"note\": \"'Formerly turbant, turribant, turband; also tolibant, tulipant, tulbant. - F. turbant ... Ital. turbante ... Turk. tulbend.'\"},\n   {\"src\": \"HJB\", \"where\": \"s.v. TURBAN\", \"stance\": \"supports\", \"note\": \"'From the Turks it passed in the forms Tulipant, Tolliban, Turbant, &c., into European languages.'\"}\n ]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"tulipa\", \"verdict\": \"plausible\",\n \"derivation\": \"There is no classical Latin tulipa: the form is New Latin, a botanical coinage of the mid-16th century (Gesner 1561; later Linnaeus' genus Tulipa), made from the same Turkish tülbend. Lokotsch no.544 documents the origin of the name: in 1554 the imperial ambassador Busbecq saw the flowers at Adrianople and named them after their likeness to the Turkish-Persian word for 'turban' ('Narcissorum, Hyacinthorum, et eorum quos Turcae Tulipan vocant', Busbecq Epist. I) - and he notes that Persians and Turks themselves call the tulip lāla, not tülbend. The vernacular chain is Turkish tülbend > Italian tulipano/tulipa, French tulipe, Spanish tulipán. Nourai's box is therefore right about the source and about the turban-shape motivation, but 'Latin' should be read as Neo-Latin botanical nomenclature, and the immediate mediators are Italian and French.\",\n \"derivation_fa\": \"«tulipa» واژه‌ای لاتینی کلاسیک نیست؛ ساختهٔ لاتینِ نو و اصطلاح گیاه‌شناسی سدهٔ شانزدهم است (گسنر ۱۵۶۱م و سپس نام جنس در رده‌بندی لینه) که از همان «تلبند» ترکی گرفته شده است. لوکوچ (شمارهٔ ۵۴۴) گزارش می‌کند که در ۱۵۵۴م بوسبک، سفیر امپراتور، این گل را در ادرنه دید و آن را به سبب شباهتش به دستار، به همان واژهٔ ترکی‑فارسی نامید؛ و می‌افزاید که ایرانیان و ترکان خود لاله می‌گویند نه تلبند. زنجیرهٔ زبان‌های زنده چنین است: tülbend ترکی › tulipano/tulipa ایتالیایی › tulipe فرانسوی › tulipán اسپانیایی. پس انگیزهٔ معنایی («به شکل دستار») درست است ولی برچسب «لاتین» را باید لاتینِ نو خواند و واسطه‌های اصلی ایتالیایی و فرانسوی‌اند.\",\n \"sources\": [E_TULIP],\n \"ref_check\": [\n   {\"ref\": \"AHD:1380\", \"status\": \"not_checked\", \"note\": \"AHD main-dictionary page; the New College edition is not on disk (only Watkins' appendix).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 544\", \"stance\": \"supports\", \"note\": \"'Aus demselben Grundwort ist der Name der Pflanze Tulipa Gesneriana entstanden; i.J. 1554 sah sie der kaiserliche Gesandte Busbeck in Adrianopel und nannte die weit offen stehenden Blumen nach ihrer Aehnlichkeit mit dem tk.-pers. Worte fuer \\\"Turban\\\" ... it. tulipano, frz. tulipe, sp. pg. tulipa, tulipan'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. tulip\", \"stance\": \"partial\", \"note\": \"'F. tulipe, also tulipan, a tulip; so called from its likeness to a turban. - Ital. tulipa, tulipano, a tulip. - Turk. tulbend, a turban' - Skeat routes it through Italian, with no Latin stage.\"}\n ]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"tulip\", \"verdict\": \"plausible\",\n \"derivation\": \"English tulip is first attested in the 1570s and comes, per Etymonline, from Dutch or German tulpe / French tulipe (the Germanic forms dropped the -an of tulipano/tulipan, which Italian and Spanish kept). Nourai's route 'from Persia via Turkey and Holland' and the date 1575 fit the horticultural history well enough - Busbecq's bulbs went from Constantinople to Vienna, thence to Clusius, who moved to Leiden in 1593 and made the Dutch trade possible; tulips were being grown in England by c.1578-1582 - but the word itself entered English from Dutch/French, not from a Latin tulipa, so the drawn arrow Latin -> English is a simplification.\",\n \"derivation_fa\": \"واژهٔ انگلیسی tulip از دههٔ ۱۵۷۰م گواهی شده و بنا بر اتیمانلاین از هلندی یا آلمانی tulpe و فرانسوی tulipe گرفته شده است؛ زبان‌های ژرمنی پایانهٔ ‑an صورت‌های tulipano/tulipán را انداخته‌اند. گزارهٔ نورایی («نخستین بار در ۱۵۷۵ از ایران از راه ترکیه و هلند به انگلستان برده شد») با تاریخ باغبانی سازگار است: پیازهای بوسبک از استانبول به وین و از آنجا به کلوسیوس رسید و او در ۱۵۹۳ به لیدن رفت و تجارت هلندی لاله را ممکن ساخت. با این همه، خودِ واژه از هلندی/فرانسوی به انگلیسی رسیده است نه از لاتینی tulipa؛ پس پیکان نمودار ساده‌سازی شده است.\",\n \"sources\": [E_TULIP],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"no page number given; the AHD main dictionary is not on disk.\"},\n   {\"ref\": \"OEW:247\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984), is lending-only on archive.org (refs_online.json kind='archive_restricted'); djvu.txt returns 401.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. tulip\", \"stance\": \"supports\", \"note\": \"'tulip, n. - F. tulipe, earlier tulipan (cp. It. tulipano)' - French/Italian, no Latin.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 544\", \"stance\": \"supports\", \"note\": \"'dtsch. Tulpe, ndl. tulp, engl. tulip'.\"}\n ]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Old Persian\", \"words\": \"bandaka\", \"verdict\": \"confirmed\",\n \"derivation\": \"OP ba(n)daka- (written b-d-k, the nasal not being written before a stop) is a -ka- derivative of *banda- 'bond, fetter', literally 'the one who wears someone's fetters/bonds'; it is the standard Achaemenid term for a loyal subject of the king (Bisotun 1.19, 2.20 etc.). Kent, Old Persian, Lexicon p.199: 'ba\\\"daka- sb. \\\"subject, servant\\\" ... Phl. bandak, NPers. bandah; deriv. of OP *ba\\\"da- \\\"bond, fetter\\\", Av. banda-, Skt. bandha-, to pIE root *bhendh-.' Nourai's gloss 'slave' follows Horn no.230 ('ap. ba(n)daka- \\\"Sklave\\\"') and Mo'in; Kent's 'subject, vassal' is the better rendering of the royal-inscription usage.\",\n \"derivation_fa\": \"«bandaka-» پارسی باستان (به خط میخی b-d-k، چون نون پیش از همخوان بی‌واک نوشته نمی‌شد) مشتق ‑ka از *banda- «بند، زنجیر» است، یعنی «کسی که بند کسی را بر خود دارد»، و در کتیبه‌های هخامنشی (بیستون ۱٫۱۹ و ۲٫۲۰) اصطلاح رسمی «رعیت وفادار شاه» است. کنت در واژه‌نامهٔ پارسی باستان (ص ۱۹۹) می‌نویسد: bandaka- «تابع، خدمتکار»، پهلوی bandak، فارسی نو «بنده»، مشتق از *banda- و از ریشهٔ هندواروپایی *bʰendʰ-. معنی «برده» که نورایی آورده از هرن (شمارهٔ ۲۳۰) و معین گرفته شده؛ ترجمهٔ دقیق‌تر همان «بندهٔ شاه، تابع» است. ادعای نورایی درست است.\",\n \"sources\": [A_BANDEH],\n \"ref_check\": [\n   {\"ref\": \"KNT:199\", \"status\": \"supports\", \"note\": \"KNT.txt line 5725: 'ba\\\"daka- sb. \\\"subject, servant\\\" (cf. Koenig ...): Phl. bandak, NPers. bandah; deriv. of OP *ba\\\"da- \\\"bond, fetter\\\", Av. banda-, Skt. bandha-, to pIE root *bhendh-'. Page 199 of the Lexicon, exactly as cited.\"},\n   {\"ref\": \"SOD:105\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 2668 on printed p.~104-105 (SOD_pages.txt leaf 170): 'bnty ... servant, slave'; the grammatical introduction (p.xxxiii) lists 'Pande / B finth ... slave, Olr. *bandaka-'. So SOD:105 is the page with the Sogdian reflex of *bandaka-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 230\", \"stance\": \"supports\", \"note\": \"'bende \\\"Sklave, Diener\\\". ap. ba(n)daka- \\\"Sklave\\\"; phlv. bandak.'\"},\n   {\"src\": \"KNT\", \"where\": \"p.199 and Sec.39\", \"stance\": \"supports\", \"note\": \"also Sec.39: 'bdk = ba\\\"daka, Phl. bandak' (nasal omitted in writing before stops).\"}\n ]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Pahlavi\", \"words\": \"bandak\", \"verdict\": \"confirmed\",\n \"derivation\": \"MP bandag [bndk'] 'servant, slave' continues OP bandaka- without change beyond the regular Middle Persian weakening of final -aka > -ag (the Book Pahlavi spelling bndk' preserves the older -ak). MacKenzie, CPD 17: 'bandag [bndk' | P bndg, N ~a] servant'. Nyberg, Manual of Pahlavi II s.v.: 'bandak [bndk'; inscr. BD-k] servant, slave ... OP bandaka-; MPrth bndg; MPrs bng = bannag < bandak; Paz. banda, NP bandah.' Nourai's transliteration bandak follows the Book Pahlavi orthography rather than the pronounced bandag - both are current.\",\n \"derivation_fa\": \"فارسی میانهٔ bandag (به خط پهلوی bndk') «بنده، خدمتکار» دنبالهٔ بی‌واسطهٔ bandaka- پارسی باستان است؛ تنها تحول، نرم‌شدن قاعده‌مند پایانهٔ ‑ak به ‑ag در فارسی میانه است که املای پهلوی صورت کهن‌تر را نگه داشته. مکنزی (فرهنگ کوچک پهلوی، ص ۱۷): bandag «خدمتکار»؛ و نیبرگ در واژه‌نامهٔ راهنمای پهلوی: «bandak [bndk'؛ کتیبه‌ای BD-k] خدمتکار، برده ... پارسی باستان bandaka-، پارتی bndg، پازند banda، فارسی نو بنده». خوانش «bandak» که نورایی آورده بر پایهٔ نویسه‌گردانی است نه تلفظ. ادعای نورایی درست است.\",\n \"sources\": [A_BANDEH],\n \"ref_check\": [\n   {\"ref\": \"KNT:199\", \"status\": \"supports\", \"note\": \"Kent p.199 s.v. ba\\\"daka- explicitly gives 'Phl. bandak'.\"},\n   {\"ref\": \"MON:588\", \"status\": \"supports\", \"note\": \"Mo'in's entry بنده (read via abadis.ir, section فرهنگ معین) is tagged '[په.]' = Pahlavi, i.e. Mo'in derives the NP word from Pahlavi, as the chart's Pahlavi > Persian arrow requires.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p.17 s.v. bandag\", \"stance\": \"supports\", \"note\": \"'bandag [bndk' | P bndg, N ~a] servant.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II, Glossary s.v. bandak\", \"stance\": \"supports\", \"note\": \"'bandak [bndk'; inscr. BD-k] servant, slave ... OP bandaka-; MPrth bndg; MPrs bng = bannag < bandak; Paz. banda, NP bandah.'\"}\n ]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"bandeh «بنده»\", \"verdict\": \"confirmed\",\n \"derivation\": \"NP بنده banda/bande is MP bandag with the regular loss of the final -g of the -ag suffix in New Persian (MP bandag > NP banda, exactly as MP zindag > NP zinda). Semantically it kept both the concrete 'slave, bondsman' and, from early Islamic times, the religious 'servant (of God)' and the polite first person 'this servant, I'. Dehkhoda: 'from the infinitive bastan, plural bandagan; in Pahlavi bandag; in Old Persian bandaka'. Mo'in tags the word [په.] (Pahlavi).\",\n \"derivation_fa\": \"«بنده» در فارسی نو از bandag فارسی میانه است با افتادن قاعده‌مند g پایانی پسوند ‑ag (همان‌گونه که zindag به «زنده» رسیده است). واژه هم معنی عینی «برده، غلام» را نگه داشته و هم از دورهٔ اسلامی معنی دینی «بندهٔ خدا» و کاربرد ادبی ضمیر اول‌شخص («بنده») را یافته است. دهخدا می‌نویسد: «از مصدر بستن، جمع: بندگان؛ در پهلوی bandag، در پارسی باستان bandaka» و معین نیز آن را با نشان [په.] می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [A_BANDEH],\n \"ref_check\": [\n   {\"ref\": \"MON:588\", \"status\": \"supports\", \"note\": \"Mo'in s.v. بنده (via abadis.ir): '(بَ دِ) [په.] (اِ.) ۱- مخلوق خدا ۲- برده ۳- خدمتکار ۴- مطیع ۵- من، این بنده' - Pahlavi origin tag, glosses 'slave, servant'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 230\", \"stance\": \"supports\", \"note\": \"'bende \\\"Sklave, Diener\\\". ap. ba(n)daka- \\\"Sklave\\\"; phlv. bandak.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II s.v. bandak\", \"stance\": \"supports\", \"note\": \"'... Paz. banda, NP bandah.'\"},\n   {\"src\": \"MON\", \"where\": \"Dehkhoda quoted at abadis.ir/fatofa/بنده\", \"stance\": \"supports\", \"note\": \"'از مصدر بستن ... در پهلوی bandag، در پارسی باستان bandaka'.\"}\n ]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Avestan / Old Persian\", \"words\": \"basta; ham-basta\", \"verdict\": \"plausible\",\n \"derivation\": \"basta- is the perfect passive participle of band- 'to bind' in both languages: Av. basta- (Bartholomae AiW col. 926, 'PPfP. basta-') and OP basta- <b-s-t>, attested at DB 1.82, 2.75, 2.90, 5.26 ('duvarayamaiy basta adariya', 'he was held bound at my gate'); phonetically *bandʰ-to- > *bad-ta- > basta-, the -st- being the regular Iranian outcome of a voiced aspirate before -t- (Kent Sec.85). ham-basta 'tied together' is a different matter: it is not attested in Avestan or Old Persian, but reconstructed from the New Persian word - Horn, Nachtraege no.122a, quoting Salemann's edition of Shams-i Fakhri's lexicon, sets up ap. *ha(m)basta- for NP enfest 'Spinnengewebe' and immediately adds 'Unsicher, man muesste eine Arabisirung annehmen'; Huebschmann p.18 rejects the equation for anfast altogether while accepting np. anbast/anbasta 'ligatus' = zd. ham + basta-. So 'tied together, interwoven' is well founded, but the third gloss 'spider web' rests on a conjecture that Nourai's own two references dispute.\",\n \"derivation_fa\": \"«basta-» در هر دو زبان صفت مفعولی فعل band- «بستن» است: اوستایی basta- (بارتولومه، ستون ۹۲۶) و پارسی باستان basta- که در بیستون (۱٫۸۲، ۲٫۷۵، ۲٫۹۰، ۵٫۲۶) گواهی شده است، مانند «duvarayāmaiy basta adāriya» یعنی «بسته بر درگاه من نگاه داشته شد»؛ از نظر آوایی *bandʰ-to- › *bad-ta- › basta- و خوشهٔ st همان نتیجهٔ قاعده‌مند همخوان دمیدهٔ واک‌دار پیش از t در ایرانی است (کنت، بند ۸۵). اما «ham-basta» در اوستا و پارسی باستان گواهی نشده و تنها بازسازی از روی واژهٔ فارسی است: هرن در تعلیقات (شمارهٔ ۱۲۲‑الف) به نقل از تصحیح زالمان بر فرهنگ شمس فخری، برای «انفست» صورت *ha(m)basta- را پیشنهاد می‌کند و بی‌درنگ می‌افزاید «نامطمئن است؛ باید معرّب‌شدن را فرض کرد»؛ هوبشمان نیز در ص ۱۸ این برابری را برای «انفست» رد می‌کند ولی «انبست/انبسته» را = ham + basta اوستایی می‌پذیرد. پس دو معنی نخست پذیرفتنی است و معنی سوم («تار عنکبوت») بر حدسی استوار است که خودِ مرجع‌های نورایی آن را رد کرده‌اند.\",\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:127\", \"status\": \"supports\", \"note\": \"Pokorny 127: 'Partiz. ai. baddha-, av. ap. basta-' - both language labels of this box are Pokorny's own.\"},\n   {\"ref\": \"HUB:18\", \"status\": \"partial\", \"note\": \"Huebschmann, Persische Studien p.18, no.122a: 'Salemann's Gleichung: anfast \\\"Spinngewebe\\\" = ap. *ha(n)basta- kann auch ich nicht fuer richtig halten. Naeher liegt es, np. anbast, anbasta \\\"ligatus\\\" = zd. ham + basta- \\\"gebunden\\\", skr. sambaddha- ... zu setzen.' Supports ham-basta 'tied together', denies the 'spider web' sense.\"},\n   {\"ref\": \"AEF:160\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e eshteqaq-e farsi (the Persian translation of Horn with Huebschmann's notes) is not online (refs_online.json kind='catalog'); the corresponding German original, Horn's Nachtraege no.122a, was read instead - see the derivation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 926 s.v. band-, basta-\", \"stance\": \"supports\", \"note\": \"'j., p. band- V. \\\"binden\\\" ... PPfP. basta-'; separate entry 'j., p. basta- Adj. (fem. -a), PPfP.: s. band-'.\"},\n   {\"src\": \"KNT\", \"where\": \"p.199 / Sec.85 / DB texts\", \"stance\": \"supports\", \"note\": \"'basta- to pIE *bhendh-' (Sec.85); text occurrences DB 1.82 'basta anayata', DB 2.75 'duvarayamaiy basta adariya'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *band-, Old Persian\", \"stance\": \"supports\", \"note\": \"'Partic.: perf. pass. basta- <b-s-t> (DB 1.82, DB 2.75, DB 2.90, DB 5.26) = Kent: 199b'.\"}\n ]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"bastan «بستن»; anbast «انبست»; anfast «انفست»\", \"verdict\": \"disputed\",\n \"derivation\": \"بستن bastan 'to bind, close' (pres. band-) is MP bastan/band- (MacKenzie CPD 17) < OIr. *band-/*basta-, so the past stem is the old participle basta- - Horn no.219: 'besten \\\"binden\\\", Praes. bend-em ... ap. basta \\\"gebunden\\\"; aw. band- \\\"binden\\\", banda- \\\"Band\\\"; phlv. bastan, band' - confirmed. انبست anbast 'dense, coagulated' is confirmed both lexically and etymologically: Borhan (vol.1, printed ~162-164) 'انبست: غلیظ و بسته شده را گویند', and Huebschmann p.18 sets np. anbast, anbasta 'ligatus' = Av. ham + basta-, with the regular Iranian ham- > an- before a stop. انفست anfast 'spider web' is the disputed item: the word is real - Borhan (printed ~173-175): 'انفست: پردهٔ تنیدهٔ عنکبوت را گویند', and the chart's shahed is from Shams-i Fakhri, whose lexicon (ed. Salemann 1887, p.155a) is the ultimate source of the etymology - but Horn (Nachtrag 122a) calls the derivation from *ha(m)basta- 'unsicher' because the f would require an Arabicised transmission, and Huebschmann flatly refuses it. Modern Persian etymology has not rehabilitated it. Verdict for the node = the worst of the three.\",\n \"derivation_fa\": \"«بستن» (ستاک حال «بند‑») از فارسی میانهٔ bastan/band- و از ایرانی باستان *band-/*basta- است؛ ستاک گذشته همان صفت مفعولی کهن basta- است. هرن (شمارهٔ ۲۱۹) می‌نویسد: «بستن، ستاک حال bend-؛ پارسی باستان basta \\\"بسته\\\"؛ اوستایی band- \\\"بستن\\\"، banda- \\\"بند\\\"؛ پهلوی bastan, band» - این بخش بی‌گمان درست است. «انبست» نیز هم از نظر واژگانی و هم ریشه‌شناختی تأیید می‌شود: برهان قاطع (ج ۱، ص ~۱۶۲–۱۶۴) «انبست: غلیظ و بسته شده را گویند»، و هوبشمان (ص ۱۸) آن را برابر ham + basta اوستایی می‌گیرد؛ پیشوند ham- ایرانی پیش از همخوان بست‌شده در فارسی به an- بدل می‌شود. اما «انفست» به معنی تار عنکبوت مورد اختلاف است: خودِ واژه واقعی است (برهان، ص ~۱۷۳: «انفست: پردهٔ تنیدهٔ عنکبوت را گویند») و شاهد شمس فخری نیز در نمودار آمده، ولی هرن (تعلیقات ۱۲۲‑الف) گرفتن آن را از *ha(m)basta- «نامطمئن» می‌خواند چون f جز با فرض معرّب‌شدن توجیه نمی‌شود، و هوبشمان یکسره ردش می‌کند. پس داوری کلی این خانه بر پایهٔ بدترین جزء آن است: پژوهش امروزی «انفست» را نمی‌پذیرد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:164\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 382 (printed ~162-164): 'انبست - بروزن ...: غلیظ و بسته شده را گویند' followed by 'انبسته: هر چیز که آن بسته و سخت شده باشد ... و شیر و ماست و خون بسته را نیز گویند' - exactly Nourai's gloss 'dense, coagulated'.\"},\n   {\"ref\": \"BQT:173\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 391 (printed ~173-175, the leaf ends with the continuation note 'بقیه در صفحهٔ ۱۷۶'): 'انفست - بروزن بدمست: پردهٔ تنیدهٔ عنکبوت را گویند' - the gloss 'spider web' is Borhan's.\"},\n   {\"ref\": \"BQT:278\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaves 497-498 (printed ~277-278) carry the بست / بستان / بستر block, i.e. the بستن article region cited.\"},\n   {\"ref\": \"KLN:152\", \"status\": \"partial\", \"note\": \"Klein p.152 is the basket / bast page; s.v. bast he connects OE baest with L. fascis, but there is no Persian bastan there. The citation seems to belong with node 14/15 rather than with this node.\"},\n   {\"ref\": \"AEF:159\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's translation of Horn is not online; the German original (Horn no.219 'besten') was read instead and supports bastan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 219 (p.50)\", \"stance\": \"supports\", \"note\": \"'besten \\\"binden\\\", Praes. bend-em, bend, ap. basta \\\"gebunden\\\"; aw. band- \\\"binden\\\", banda- \\\"Band\\\"; phlv. bastan, band; ai. bandh-.'\"},\n   {\"src\": \"HUB\", \"where\": \"p.18 no.122a\", \"stance\": \"partial\", \"note\": \"accepts 'np. anbast, anbasta \\\"ligatus\\\" = zd. ham + basta-', rejects Salemann's anfast = ap. *ha(n)basta-.\"},\n   {\"src\": \"PHD\", \"where\": \"p.17 s.v. bastan\", \"stance\": \"supports\", \"note\": \"'bastan, band- [ASLWN-tn' ... | M bstn, P bnd-, N ~] tie, bind.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *band-, Middle Persian\", \"stance\": \"supports\", \"note\": \"'Inf.: BMP bstn /bastan/, MMP bstn'.\"}\n ]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"fascis\", \"verdict\": \"disputed\",\n \"derivation\": \"Latin fascis 'bundle, faggot; the bundle of rods carried before a magistrate' is not put under *bhendh- by any standard authority. Pokorny gives it its own root: p.111 'bhasko-, etwa \\\"Bund, Buendel\\\": Maked. baskioi ... lat. fascia \\\"Binde, Band\\\", fascis \\\"Bund, Buendel, Paket\\\"; mir. basc \\\"Halsband\\\", abrit. bascauda ... cymr. baich \\\"Buerde, Last\\\"'. Klein s.v. fasces agrees: 'L. fasces ... pl. of fascis, prob. cogn. with Mir. basc \\\"neckband\\\", W. baich \\\"load, burden\\\", OBrit. bascauda ... Maced. Gk. baskioi, OE baest'. The root there is *bʰasko-, with no nasal infix and no dental, so it cannot be derived from *bhendh-; a semantic link ('bundle' ~ 'bind') is all that connects the two. Nourai's KLN:152,576 citations do not support the arrow he draws.\",\n \"derivation_fa\": \"واژهٔ لاتینی fascis «دسته، بسته؛ دستهٔ ترکه‌های نشان قدرت مقامات رومی» در هیچ‌یک از مرجع‌های معتبر ذیل *bʰendʰ- نیامده است. پوکورنی آن را زیر ریشهٔ جداگانهٔ *bʰasko- «دسته، بسته» در ص ۱۱۱ می‌آورد، در کنار مقدونی baskioi، ایرلندی میانه basc «گردن‌بند»، بریتونی باستان bascauda و ولزی baich «بار»؛ کلاین نیز ذیل fasces همین را می‌گوید. ریشهٔ *bʰasko- نه میان‌وند خیشومی دارد و نه همخوان دندانی، پس نمی‌تواند از *bʰendʰ- برآمده باشد و تنها پیوند این دو، شباهت معنایی «بسته/بستن» است. ارجاع‌های خودِ نورایی (کلاین، ص ۱۵۲ و ۵۷۶) نیز این پیکان را تأیید نمی‌کنند؛ پژوهش امروزی این انتساب را رد می‌کند.\",\n \"sources\": [E_FASCISM],\n \"ref_check\": [\n   {\"ref\": \"KLN:152\", \"status\": \"contradicts\", \"note\": \"Klein p.152 s.v. bast: OE baest 'prob. cogn. with L. fascis, \\\"bundle\\\", see fasces' - a cognate claim within a different root, not descent from bhendh-.\"},\n   {\"ref\": \"KLN:576\", \"status\": \"contradicts\", \"note\": \"Klein s.v. fasces: 'L. fascis, prob. cogn. with Mir. basc \\\"neckband\\\", W. baich \\\"load, burden\\\", OBrit. bascauda \\\"rinsing bowl of brass\\\", Maced. Gk. baskioi (pl.) \\\"bundle of wood\\\", OE baest \\\"inner bark of the linden tree\\\"' - i.e. Pokorny's *bhasko-, not *bhendh-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.111 s.v. bhasko-\", \"stance\": \"contradicts\", \"note\": \"'bhasko-, etwa \\\"Bund, Buendel\\\" ... lat. fascia \\\"Binde, Band\\\", fascis \\\"Bund, Buendel, Paket\\\" ... WP. II 135 f., WH. I 97, 459 f.' The bhendh- entry on p.127-128 does not mention fascis.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.152 (bhendh-) vs II 135f (bhasko-)\", \"stance\": \"contradicts\", \"note\": \"the bhendh- article lists only lat. offendimentum, offendix for Latin; fascis is treated at WP II 135f under bhasko-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhendh-\", \"stance\": \"silent\", \"note\": \"the bhendh- entry lists Germanic, Celtic (benna > bin), Persian band and Sanskrit badhnati only - no Latin fascis.\"}\n ]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"basket\", \"verdict\": \"disputed\",\n \"derivation\": \"English basket cannot be derived from Latin fascis. Klein, on the very page Nourai cites, writes: 'basket, n. - ME., fr. L. bascauda, \\\"a brazen vessel\\\", referred to by the Roman poet Martial as an OBrit. word; cogn. with L. fascis, \\\"bundle\\\"; see fasces' - i.e. bascauda is a cognate (a Brittonic word within the *bhasko- family), not a descendant of fascis. Etymonline is more sceptical still: basket (from Anglo-French bascat) is 'of obscure origin despite much speculation', and the OED doubts the bascauda connection because 'there is no evidence of such a word in Celtic'. Either way the drawn arrow Latin fascis -> English basket is wrong in form and in direction.\",\n \"derivation_fa\": \"واژهٔ انگلیسی basket را نمی‌توان از fascis لاتینی گرفت. کلاین در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد: «basket از انگلیسی میانه، از لاتینی bascauda \\\"ظرف برنجی\\\" که مارتیالیس شاعر رومی آن را واژه‌ای بریتانیایی می‌خواند؛ هم‌ریشه با fascis لاتینی» - یعنی bascauda هم‌ریشه است نه فرزندِ fascis. اتیمانلاین محتاط‌تر است و ریشهٔ این واژه را «با همهٔ گمانه‌زنی‌ها ناشناخته» می‌خواند و می‌افزاید که فرهنگ آکسفورد پیوند با bascauda را نمی‌پذیرد چون «نشانی از چنین واژه‌ای در زبان‌های سلتی نیست». در هر دو حال، پیکانِ «fascis لاتینی › basket انگلیسی» از نظر صورت و جهت نادرست است.\",\n \"sources\": [E_BASKET],\n \"ref_check\": [\n   {\"ref\": \"KLN:152\", \"status\": \"partial\", \"note\": \"Klein p.152 s.v. basket: 'ME., fr. L. bascauda ... cogn. with L. fascis, \\\"bundle\\\"; see fasces. The orig. meaning of bascauda was prob. \\\"wicker basket\\\"' - a cognate, not the parent form Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. basket\", \"stance\": \"partial\", \"note\": \"Skeat likewise gives the Celtic/bascauda line rather than fascis.\"},\n   {\"src\": \"POK\", \"where\": \"p.111 s.v. bhasko-\", \"stance\": \"partial\", \"note\": \"'abrit. bascauda \\\"eherner Spuelkessel\\\" (vielleicht urspruenglich ein irdenes ueber einem geflochtenen korbartigen Geripp geformtes Gefaess)' - bascauda sits beside fascis under *bhasko-, not under bhendh-.\"}\n ]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Italian\", \"words\": \"fascismo\", \"verdict\": \"confirmed\",\n \"derivation\": \"Italian fascismo (1919-21) is derived from fascio 'bundle, sheaf; group, league' (< L. fascis) with the suffix -ismo; Mussolini's Fasci italiani di combattimento (1919) took their name from the political fascio of the 1890s, itself reinforced by the Roman fasces as an emblem of authority. Klein s.v. Fascism: 'It. fascismo, formed fr. fascia, \\\"bundle; political group, organization\\\", fr. L. fascis'. Nourai's gloss 'bundle, (a political) group' is really the gloss of fascio, not of fascismo, which is the -ism abstract; the edge Latin fascis -> Italian is otherwise exact.\",\n \"derivation_fa\": \"«fascismo» ایتالیایی (۱۹۱۹–۱۹۲۱م) از fascio «دسته، بافه؛ گروه، اتحادیه» (از fascis لاتینی) با پسوند ‑ismo ساخته شده است؛ «فاشی‌های ایتالیایی نبرد» که موسولینی در ۱۹۱۹ بنیاد نهاد، نام خود را از همان fascio سیاسی دههٔ ۱۸۹۰ گرفتند و نشان تبرِ ترکه‌های رومی (fasces) نیز آن را تقویت کرد. کلاین می‌نویسد: «It. fascismo از fascia \\\"دسته؛ گروه سیاسی\\\" از fascis لاتینی». معنایی که نورایی داده («دسته، گروه سیاسی») در واقع معنی fascio است نه fascismo که اسم معنی با پسوند ‑ism است؛ جز این، پیکان از fascis لاتینی درست است.\",\n \"sources\": [E_FASCISM],\n \"ref_check\": [\n   {\"ref\": \"KLN:576\", \"status\": \"supports\", \"note\": \"Klein s.v. Fascism (line 14412): 'Fascism, n. - It. fascismo, formed fr. fascia, \\\"bundle; political group, organization\\\", fr. L. [fascis]'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. fasces, fascia, fascine\", \"stance\": \"supports\", \"note\": \"the whole fasc- family (fascia, fascicule, fascine, Fascism, fess) is referred to L. fascis.\"},\n   {\"src\": \"WEB\", \"where\": \"s.v. fascism\", \"stance\": \"supports\", \"note\": \"the standard English dictionaries all give It. fascismo < fascio < L. fascis.\"}\n ]})\n\nnodes.append({\n \"id\": 17, \"lang\": \"French\", \"words\": \"fascism\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The French word is fascisme (with fasciste, first attested 1921-22); 'fascism' is not a possible French form. I rendered pdf page 87 at 200 dpi and read it: the printed box does read 'French | fascism', so the extraction is faithful and the defective form is Nourai's own - he simply repeated the English spelling in the French box. The step itself is right: Persian فاشیسم reached Persian through French, and French fascisme is a borrowing/calque of Italian fascismo.\",\n \"derivation_fa\": \"صورت درست فرانسوی fascisme است (و صفت آن fasciste، نخستین کاربرد ۱۹۲۱–۱۹۲۲م)؛ «fascism» در فرانسوی صورت ممکنی نیست. صفحهٔ ۸۷ پی‌دی‌اف را با تفکیک‌پذیری ۲۰۰ نقطه بر اینچ رندر و خواندم: در خانهٔ چاپی کتاب هم دقیقاً «French | fascism» آمده است، پس خطای خوانش اسکن نیست و اشتباه از خود کتاب است؛ نویسنده املای انگلیسی را در خانهٔ فرانسوی تکرار کرده. خودِ حلقه درست است: «فاشیسم» فارسی از راه فرانسوی آمده و fascisme فرانسوی نیز وام‌واژهٔ fascismo ایتالیایی است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"fascism\",\n \"correct_form\": \"fascisme\",\n \"sources\": [E_FASCISM],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. Fascism\", \"stance\": \"partial\", \"note\": \"Klein routes English Fascism straight from Italian fascismo; the French form he would cite is fascisme.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt line 4253\", \"stance\": \"supports\", \"note\": \"Mo'in s.v. فاشیست tags it '[فر.]' = French, so Mo'in too has the French stage that this box represents.\"}\n ]})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"fâšîsm «فاشیسم»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Persian فاشیسم fāšism and فاشیست fāšist are 20th-century borrowings from French fascisme/fasciste, as the -ism/-ist shape and the š for French sc [s]... (in fact Persian took the pronounced [fa'ʃism] of the Italian-French word) show; Mo'in marks فاشیست explicitly '[فر.]' (French). The word entered Persian in the Reza Shah period along with the rest of the European political vocabulary that came through French.\",\n \"derivation_fa\": \"«فاشیسم» و «فاشیست» در فارسی وام‌واژه‌های سدهٔ بیستم‌اند و از فرانسوی fascisme/fasciste گرفته شده‌اند؛ همان‌گونه که ساخت ‑یسم/‑یست و تلفظ «ش» نشان می‌دهد. معین در فرهنگ فارسی ذیل «فاشیست» نشان [فر.] یعنی فرانسوی می‌گذارد. این واژه در دورهٔ رضاشاه همراه با انبوه واژگان سیاسی اروپایی که از راه فرانسوی به فارسی راه یافت، وارد زبان شد. ادعای نورایی درست است.\",\n \"sources\": [E_FASCISM],\n \"ref_check\": [\n   {\"ref\": \"MON:2471\", \"status\": \"supports\", \"note\": \"MON_part2.txt line 4253: 'فاشیست [فر.] (ص.) آنکه پیرو مسلک سیاسی فاشیسم باشد' - Mo'in tags the word French, which is exactly the arrow drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. فاشیست\", \"stance\": \"supports\", \"note\": \"origin tag [فر.].\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwoerter im Arabischen\", \"stance\": \"silent\", \"note\": \"a modern Europeanism, outside the scope of the Arabic-loan literature; nothing found.\"}\n ]})\n\nnodes.append({\n \"id\": 19, \"lang\": \"English\", \"words\": \"fascism\", \"verdict\": \"confirmed\",\n \"derivation\": \"English fascism/fascist are borrowed directly from Italian fascismo/fascista in 1921-22, in reports of Mussolini's movement; the chart's arrow Italian -> English is correct and independent of the French branch. The ultimate Latin source fascis is right; only the attachment of fascis to *bhendh- (node 14) is at fault.\",\n \"derivation_fa\": \"واژه‌های انگلیسی fascism و fascist در ۱۹۲۱–۱۹۲۲م، در گزارش‌های مربوط به جنبش موسولینی، مستقیماً از ایتالیایی fascismo/fascista وام گرفته شده‌اند؛ پس پیکان «ایتالیایی › انگلیسی» درست و مستقل از شاخهٔ فرانسوی است. سرچشمهٔ نهایی یعنی fascis لاتینی نیز درست است و تنها ایراد کار، پیوند دادن fascis به ریشهٔ *bʰendʰ- (خانهٔ ۱۴) است.\",\n \"sources\": [E_FASCISM],\n \"ref_check\": [\n   {\"ref\": \"AHD:477\", \"status\": \"not_checked\", \"note\": \"AHD main-dictionary page 477; the New College edition is not on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. Fascism\", \"stance\": \"supports\", \"note\": \"'Fascism, n. - It. fascismo, formed fr. fascia ... fr. L. fascis.'\"},\n   {\"src\": \"WEB\", \"where\": \"s.v. fascism\", \"stance\": \"supports\", \"note\": \"Webster's likewise: from Italian fascismo, from fascio bundle, political group.\"}\n ]})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Germanic\", \"words\": \"band, binda, bund\", \"verdict\": \"confirmed\",\n \"derivation\": \"Watkins/AHD s.v. bhendh- sets out exactly these three Germanic grades: full grade *bindan (Old English bindan 'to bind'), o-grade *bhondh- > Germanic *band- (Old English bend 'band, ribbon', Old Norse band 'band, fetter', Old French bande from a Germanic source), and zero grade *bhndh- > Germanic *bund- (MHG bunt 'league', Middle Dutch bondel 'bundle'). Nourai's 'band, binda, bund' is a compact way of writing that ablaut triad.\",\n \"derivation_fa\": \"واتکینز در پیوست ریشه‌های هندواروپایی ذیل *bʰendʰ- دقیقاً همین سه پایهٔ ژرمنی را می‌آورد: درجهٔ کامل *bindan (انگلیسی باستان bindan «بستن»)، درجهٔ o یعنی *bʰondʰ- › ژرمنی *band- (انگلیسی باستان bend «نوار»، نورس باستان band «بند، زنجیر») و درجهٔ صفر *bʰndʰ- › ژرمنی *bund- (آلمانی میانهٔ علیا bunt «اتحادیه»، هلندی میانه bondel «دسته»). «band, binda, bund» که نورایی نوشته صورت فشردهٔ همین سه‌گانهٔ ابلاوت است و درست است.\",\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. bhendh-: '1. Germanic *bindan in Old English bindan, to bind: BIND ... 2. O-grade form *bhondh- in Germanic *band- ... 3. Zero-grade form *bhndh- in Germanic *bund- ...'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.128\", \"stance\": \"supports\", \"note\": \"'got. ags. bindan, aisl. binda, ahd. bintan \\\"binden\\\", got. bandi usw. ... got. bansts m. \\\"Scheuer\\\" (*bhondh-sti)'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.16 'bind'\", \"stance\": \"supports\", \"note\": \"'IE *bhendh-. Feist 93' for Goth. bindan; Walde-P. 2.152.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.vv. bhendh-, bhendhos\", \"stance\": \"supports\", \"note\": \"'bhendhos, a, us \\\"band, thong; company\\\" ... Go. bandi and comm. Gmc.'\"}\n ]})\n\nnodes.append({\n \"id\": 21, \"lang\": \"English\", \"words\": \"band, bend, bond, bind, bundle, ribbon\", \"verdict\": \"plausible\",\n \"derivation\": \"Five of the six are exactly Watkins' list under bhendh-: BIND (< OE bindan), BEND1/BEND2 (< OE bendan 'to bend', originally 'to string a bow'), BAND1 (partly < ON band, partly < Old French bande of Germanic origin), BOND (a variant of band), BUNDLE (< Middle Dutch bondel). RIBBON is the doubtful one: it is not in the Watkins index under bhendh-, and Etymonline derives it from Old French riban, variant of ruban (13c.), 'of unknown origin, possibly from a Germanic compound whose second element is related to band'; Wiktionary suggests Middle Dutch ringhband 'necklace' (ring + band). If that compound analysis is right the word does belong here through its second element, so the entry is defensible but not established.\",\n \"derivation_fa\": \"پنج واژه از شش واژهٔ این خانه دقیقاً همان‌هایی است که واتکینز ذیل *bʰendʰ- آورده: bind (از انگلیسی باستان bindan)، bend (از bendan «زه کردن کمان»)، band (بخشی از نورس باستان band و بخشی از فرانسوی bande با اصل ژرمنی)، bond (گونهٔ band) و bundle (از هلندی میانه bondel). اما ribbon مورد تردید است: در نمایهٔ واتکینز ذیل این ریشه نیامده و اتیمانلاین آن را از فرانسوی باستان riban، گونهٔ ruban (سدهٔ ۱۳م)، «با اصل ناشناخته» می‌داند و تنها احتمال می‌دهد که مرکبی ژرمنی باشد که جزء دومش با band پیوند دارد؛ ویکی‌واژه هلندی میانهٔ ringhband «گردن‌بند» را پیشنهاد می‌کند. اگر این تحلیل درست باشد، واژه از راه جزء دوم به این ریشه می‌رسد. پس فهرست با احتیاط پذیرفتنی است.\",\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. bhendh- yields BIND, WOODBINE, BEND1, BEND2, BAND1, BOND, BUND1, BUND2, BUNDLE, BIN, BANDANNA, CUMMERBUND; the index entries confirm 'BAND1 bhendh-', 'BEND1 bhendh-', 'BOND bhendh-', 'BIND bhendh-', 'BUNDLE bhendh-'. RIBBON does not appear in the index under this root - the word 'ribbon' occurs in the entry only as a gloss of Old English bend.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. band, bend, bond, bind, bundle\", \"stance\": \"supports\", \"note\": \"Klein derives all of these from the Germanic *bindan/*band- family.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. ribbon\", \"stance\": \"partial\", \"note\": \"Skeat too treats ribbon as an Old French word of doubtful origin, not straightforwardly Germanic band.\"}\n ]})\n\nnodes.append({\n \"id\": 22, \"lang\": \"French\", \"words\": \"bannier\", \"verdict\": \"disputed\",\n \"derivation\": \"The form printed in the book is 'bannier'; the Old French word is baniere (modern French banniere), and I checked the page image - the misprint is Nourai's, not the extraction's. On the substance, modern scholarship derives the word from a different root. Klein p.146, the page Nourai cites, is the outlier that supports him: 'banner, n. - ME. banere, fr. OF. baniere ... prob. a blend of WTeut. *banda, corresponding to Goth. bandwa, bandwo, \\\"sign, signal\\\" ... and of OF. ban ... Goth. bandwa prob. derives fr. I.-E. base *bendh-, \\\"to bind\\\"'. But Watkins/AHD indexes BANNER under bha-1 'to shine', and Etymonline: 'Late Latin bandum \\\"standard\\\", from Gothic bandwa \\\"a sign\\\", from suffixed form of PIE root *bha- (1) \\\"to shine\\\"' - the semantic path is 'that which is made visible/signals', not 'that which binds'. Kroonen and Wiktionary agree with the *bʰeh2- derivation.\",\n \"derivation_fa\": \"صورتی که در کتاب چاپ شده «bannier» است؛ صورت درست فرانسوی باستان baniere و فرانسوی امروز bannière است، و با خواندن تصویر صفحه روشن شد که این خطای چاپی خودِ کتاب است نه خطای خوانش اسکن. اما ایراد اصلی محتوایی است: پژوهش امروزی این واژه را به ریشهٔ دیگری می‌برد. کلاین (ص ۱۴۶) که نورایی به او ارجاع می‌دهد تنها مرجعی است که با او هم‌رأی است: «banner از انگلیسی میانه banere، از فرانسوی باستان baniere ... آمیزه‌ای از ژرمنی غربی *banda برابر با bandwa گوتی \\\"نشانه\\\" ... و bandwa گوتی احتمالاً از پایهٔ هندواروپایی *bendh- \\\"بستن\\\" است». در برابر، واتکینز در پیوست AHD واژهٔ BANNER را ذیل bha-1 «درخشیدن» می‌آورد و اتیمانلاین می‌نویسد: «از لاتینی متأخر bandum \\\"درفش\\\"، از گوتی bandwa \\\"نشانه\\\"، از صورت پسوندی ریشهٔ هندواروپایی *bʰeh₂- \\\"درخشیدن\\\"»؛ یعنی راه معنایی «آنچه دیده و نشان داده می‌شود» است نه «آنچه می‌بندد». کرونن و ویکی‌واژه نیز همین را می‌گویند. پس پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"error_in\": \"book\",\n \"book_prints\": \"bannier\",\n \"correct_form\": \"baniere / bannière\",\n \"sources\": [E_BANNER],\n \"ref_check\": [\n   {\"ref\": \"KLN:146\", \"status\": \"supports\", \"note\": \"Klein s.v. banner: 'ME. banere, fr. OF. baniere (F. banniere) ... Goth. bandwa, prob. derives fr. I.-E. base *bendh-, \\\"to bind\\\". See band, \\\"tie\\\"' - Klein does support Nourai here, but he is the minority view and he writes the form as baniere, not bannier.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"contradicts\", \"note\": \"the index reads 'BANNER bha-1', i.e. Watkins files banner under bha-1 'to shine', not under bhendh-.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. banner\", \"stance\": \"partial\", \"note\": \"Skeat likewise takes it from OF baniere and Late Latin bandum, without a bhendh- attachment.\"},\n   {\"src\": \"POK\", \"where\": \"p.127-128 s.v. bhendh-\", \"stance\": \"silent\", \"note\": \"no Romance banner word is listed under bhendh-.\"}\n ]})\n\nnodes.append({\n \"id\": 23, \"lang\": \"English\", \"words\": \"banner\", \"verdict\": \"confirmed\",\n \"derivation\": \"The edge itself is right: Middle English banere (c.1200) is from Old French baniere 'flag, standard', and the modern spelling with -er is the usual English adaptation of French -iere. What is wrong is the branch's attachment to *bhendh- one step above (node 22): Etymonline and Watkins take the Gothic bandwa 'sign' behind Late Latin bandum from PIE *bha- (1) 'to shine', so the whole banner branch does not belong on this chart.\",\n \"derivation_fa\": \"خودِ این حلقه درست است: banere انگلیسی میانه (حدود ۱۲۰۰م) از baniere فرانسوی باستان به معنی «درفش، بیرق» گرفته شده و املای امروزی با ‑er همان برگردان معمول ‑ière فرانسوی در انگلیسی است. آنچه نادرست است، پیوند یک پله بالاتر (خانهٔ ۲۲) است: اتیمانلاین و واتکینز واژهٔ گوتی bandwa «نشانه» را که پشتِ bandum لاتینی متأخر است، از ریشهٔ هندواروپایی *bʰeh₂- «درخشیدن» می‌دانند؛ پس این شاخه اصلاً جای خود را در این نمودار ندارد.\",\n \"sources\": [E_BANNER],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of Nourai's own.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. banner\", \"stance\": \"supports\", \"note\": \"'banner, n. - ME. banere, fr. OF. baniere (F. banniere)' - the English<-French step is beyond doubt.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. banner\", \"stance\": \"supports\", \"note\": \"same chain ME banere < OF baniere.\"}\n ]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Bhendh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰendʰ- 'to bind'\",\n \"note\": \"Pokorny IEW 127-128 s.v. bhendh- 'binden' (= WP. II 152); Watkins/AHD 'bhendh-. To bind. [Pok. bhendh- 127]'; Wiktionary *bʰendʰ- 'to bind'. Nourai's headword spelling, the language label 'Indo-European' and the gloss 'to bind, fasten' are all correct and POK:127 is the exact page on which the entry begins. Cross-cutting comments on the chart: (a) the Iranian half of the tree (banda-, basta-, bandaka-, band, bastan, bandeh, payvastan) is solid and is confirmed by Bartholomae, Kent, MacKenzie, Nyberg, Horn, Cheung and Borhan alike; (b) the Latin fascis branch (nodes 14-19) does not belong to this root at all - Pokorny puts fascis under *bhasko- (p.111) and Klein, whom Nourai cites, agrees; (c) the banner branch (nodes 22-23) belongs to *bʰeh2- 'to shine' via Gothic bandwa 'sign' in Watkins and Etymonline, although Klein p.146 (Nourai's reference) does support the bhendh- derivation; (d) the anfast 'spider web' item (nodes 12-13) rests on a conjecture of Salemann's that Horn called 'unsicher' and Huebschmann rejected outright. No extraction errors were found: the JSON matches the printed page 87 (book p.57) in every box, including the book's own defective French forms 'fascism' and 'bannier'.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰendʰ- «بستن» است؛ پوکورنی (ص ۱۲۷–۱۲۸)، والده‑پوکورنی (ج ۲ ص ۱۵۲)، واتکینز در پیوست فرهنگ American Heritage و ویکی‌واژه همگی همین صورت و معنا را می‌آورند، و ارجاع POK:127 دقیقاً صفحهٔ آغاز مدخل است. دربارهٔ کل نمودار چهار نکته گفتنی است: یکم، نیمهٔ ایرانی درخت (banda-، basta-، bandaka-، بند، بستن، بنده، پیوستن) استوار است و بارتولومه، کنت، مکنزی، نیبرگ، هرن، چونگ و برهان قاطع همه آن را تأیید می‌کنند. دوم، شاخهٔ fascis لاتینی (خانه‌های ۱۴ تا ۱۹) اصلاً از این ریشه نیست؛ پوکورنی fascis را ذیل *bʰasko- در ص ۱۱۱ می‌آورد و کلاین نیز - که خودِ نورایی به او ارجاع داده - همین را می‌گوید. سوم، شاخهٔ banner (خانه‌های ۲۲ و ۲۳) نزد واتکینز و اتیمانلاین از راه bandwa گوتی به ریشهٔ *bʰeh₂- «درخشیدن» می‌رسد، هرچند کلاین (ص ۱۴۶) با نورایی هم‌رأی است. چهارم، «انفست» به معنی تار عنکبوت بر حدس زالمان استوار است که هرن آن را «نامطمئن» خوانده و هوبشمان یکسره رد کرده است. هیچ خطای استخراجی یافت نشد: داده‌های JSON با صفحهٔ چاپی ۸۷ (ص ۵۷ کتاب) در همهٔ خانه‌ها یکی است، از جمله در صورت‌های معیوبِ خودِ کتاب یعنی «fascism» فرانسوی و «bannier».\",\n \"sources\": [W_PIE],\n \"ref_check\": [\n   {\"ref\": \"POK:127\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 137 (printed 127/128): 'bhendh- \\\"binden\\\": ai. badhnati, erst spaeter bandhati \\\"bindet, fesselt\\\", av. bandayaiti \\\"bindet\\\", Partiz. ai. baddha-, av. ap. basta-, ... av. banda- m. \\\"Bande, Fessel\\\" ... WP. II 152'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.152\", \"stance\": \"supports\", \"note\": \"'bhendh- \\\"binden\\\". Ai. badhnati ... av. bandayaiti ... Ptc. ai. baddha-, av. ap. basta-, ... av. banda- m. \\\"Bande, Fessel\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhendh-\", \"stance\": \"supports\", \"note\": \"'bhendh-. To bind. ... [Pok. bhendh- 127.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. bhendh-, bhndh-, bhendhos\", \"stance\": \"supports\", \"note\": \"'bhendh- \\\"bind\\\". WP II, 152. Skt. badhnami ...; Per. bandam; Thrac. bend-; Gk. peisma; Lat. of-fendix; Go. -bindan'; 'bhendhos ... Av. bando; Per. band'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.16\", \"stance\": \"supports\", \"note\": \"'IE *bhendh-' for Goth. bindan etc., citing Walde-P. 2.152.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 87,\n \"book_page\": 57,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-87.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"nodes:\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk87.py",
 "description": "Write page-87 verification JSON"
}
```


### [2026-09-05T14:03:56.079Z] TOOL RESULT

```
nodes: 23
```


## [2026-09-05T14:04:00.475Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-87.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 87",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T14:04:02.813Z] TOOL RESULT

```
JSON OK
nodes verified: 23/23
node verdicts: {'plausible': 8, 'confirmed': 10, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'partial': 6, 'not_checked': 12, 'contradicts': 2}
books consulted: {'supports': 40, 'partial': 10, 'contradicts': 4, 'silent': 3} | by book: {'KLN': 8, 'SKT': 7, 'LKT': 5, 'POK': 4, 'CHEUNG': 3, 'PHD': 3, 'HRN': 3, 'MON': 3, 'BRT': 2, 'WLD': 2, 'HJB': 2, 'KNT': 2, 'NYB': 2, 'AHD': 2, 'WEB': 2, 'PHN': 1, 'BQT': 1, 'MON/Wiktionary': 1, 'HUB': 1, 'PLA': 1, 'SYN': 1, 'IEC': 1}
```


## [2026-09-05T14:04:11.287Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT banner ===\"; grep -n -i \"^Banner\\|Banner\\.\" SKT.txt | head -3\necho \"=== SKT basket ===\"; grep -n -i \"Basket\" SKT.txt | head -3\necho \"=== SKT ribbon ===\"; grep -n -i \"Ribbon\\|Riband\" SKT.txt | head -3\necho \"=== WEB fascism ===\"; grep -n -i \"fascismo\" WEB_vol1.txt | head -3\necho \"=== KLN band tie ===\"; grep -n \"band,  n\\.\\|bundle,  n\" KLN_1966.txt | head -5",
 "description": "Verify remaining consulted claims"
}
```


### [2026-09-05T14:04:11.408Z] TOOL RESULT

```
=== SKT banner ===
1384:BANNER.
17240:Sign.  (F-L.)    O.  F.  «^. - L  n>iwwi, a  mnrk.    Dar.  tipt,  verb;  sign-at-upt.  from the  pp.  of  the  L.  verb  signare,  to  sign. ^noiant  (i),  a  banner.  slandatV\xArtx.
=== SKT basket ===
1498:Basket.  (C.)  M.  E.  *a.t^/.- W.  Ajr^/t/; Com.  bai(et/\  Irish  Itascnd;  Gael.  Inmaid,  a basket     Perhaps  from  \V.  basf;,  a  platting.
2554:Cabbage  (a),  to  steal.  (F.)  F.  eabasser^ to  put  into  a  basket.  —  F.  cabas^  a  basket ; of  unknown  oiigin.
3039:Carpenter.  (K.-C.)  O.K.  enrffntier (F.  charpcutier),  —  Low  L.  airpcntarius^ troin  carpimtart,  to  work  in  timber.^L. Mfpfnfum,  H  carriage ;  a  word  of  Celtic origin,  w  Gael,  and  Irish  cardaJ,  a  carriage, chariot,  litter;  Irish  card,  a  basket,  litter, carriage,  phmk  ;  Gael  cat'r^,  chariot,  ship, plank.
=== SKT ribbon ===
3629:oookade,  a  knot  of  ribbon  on  a  h (F.)  F.  coq%iaT\U,  fern,  ^{t^quard, also  ce^uart/t,  Sonne/  i  fa  efcmonii,  *l bonnet  or  cap  worn  proudly,'  Cot.  K01 with  sufHx  -on/  from  F.  c^y,  a  cock  (£n the  bird's  cry).
16056:Bibald.    (F.  -  Tcui.)      M.  E. riband. ^O.Y.ribiUd',  Y.  fit-am^ ^\Jim\ ribaldus,   a  ruffian  :  cf.  Low  L    HUiM. prostitute.      Of   Tcut.   ori"-'     —  '* ir//J,  M.  II.  G.  r//<  a  p. W/vr,  lo  loy  with  a  fcmalj  ni
16058:Biband.  Bibbon.  {t.)    Koi  aUie< band;    the    final   d  is  ejicroceuL      M-M W^ff .  — Irish  ribif,  a  ribbon,  from  riAt,  *.| flake,  hair,  ribbon  :  Gad.  nb/an.  ■ fdlet,    from   rib,   ribe,    a    hair,   rag, latter ;   \V.  rhihin,  a  &Ucak.  trom atjeaV
=== WEB fascism ===
70971:fas/cism (fash/izm or fas’), n. [It. fascismo, from fascio, a political group, an organization, a club, from L. fascis, a bundle or packet.]
=== KLN band tie ===
4359:band,  n.,  a  tie.  —  ME.,  fr.  ON.  band,  rel.  to  OS., Swed.,  Du.,  G.  band,  OHG.,  MHG.  bant,  Goth. bandi,  lit.  ‘that  which  binds’,  fr.  I.-E.  base *bendh-,  ‘to  bind’,  whence  also  OI.  bandhdh,  ‘a tying,  fastening;  band,  bandage’,  Mir.  bainna, ‘bracelet’ ;  F.  bande,  ‘band’,  is  a  Teut.  loan  word. See  bind  and  cp.  bend,  bond.  Cp.  also  bandage, bandanna,  bandhava,  bandhu,  bandoleer,  and the  second  element  in  ribband,  ribbon,  roband, seerband.
5859:buncombe,  n.  —  A  spelling  var.  of  bunkum, bundle,  n.  —  ME.  bundel,  fr.  MDu.  bundel,  a collateral  form  of  bondel,  dimin.  of  MDu.  bont (whence  Du.  bond),  ‘bundle’,  rel.  to  Du.  binden, ‘to  bind".  Cp.  MHG.,  G.  bundel,  ‘bundle’,  di¬ min.  of  MHG.  bunt,  resp.  G.  Bund,  ‘bundle’, and  OE.  byndele,  ‘a  binding’,  and  see  bind.  For the  ending  see  dimin.  suff.  -le.  Cp.  bunt,  n. Derivatives:  bundle,  tr.  and  intr.  v.,  bundl-er,  n. bundobust,  n.,  regulation,  settlement  (Anglo- Ind.)  —  Hind,  and  Pers.  band-o-bast,  lit.  ‘tying and  binding’.  Hind,  band  derives  fr.  OI.  band, ‘a  tying’,  fr.  OI.  handhati,  ‘he  ties  up,  binds’; see  bind.  For  Pers.  bast,  ‘a  binding’,  see  bast, bundook,  n.,  a  rifle.  —  Hind.,  fr.  Arab,  bunduq, ‘missile',  orig.  ‘weapon  made  in  Venice",  fr. Bunduqtyah,  the  Arabic  name  of  Venice,  the  city once  so  famous  for  its  manufacture  of  cross¬ bows  and  small  arms.  This  etymology  is  corro¬ borated  by  the  circumstance  that  bunduqtyah means  also  "musket,  rifle".  Cp.  also  Al-Bandu- qant,  ‘the  man  of  the  crossbow",  a  surname  of the  caliph  Harun-al-Rashid. bung,  n.,  a  large  stopper.  —  MDu.  bonghe,  fr.  F. bonde,  fr.  Gaul.  *bunda,  whence  also  OProv- en?.  bonda.  Cp.  OIr.  bonn,  Gaelic  and  Ir.  bonn, W.  bon,  ‘base,  sole  of  the  foot".  MHG.  bunt punt,  spunt  (whence  G.  Spund ),  ‘bung",  are Romance  loan  words.  See  Bloch-Wartburg, DELF.,  p.  75  s.v.  bonde.
8977:contraband,  n.  — -  F.  contrebande,  fr.  earlier  It. contrabando  (now  spelled  contrabbando),  fr. contra-  and  bando,  ‘proclamation’.  See  ban, ‘edict’,  and  cp.  words  there  referred  to. Derivatives:  contraband,  adj.,  contraband-age.
18274:Derivative:  hurtle,  n. hurtleberry,  n.  —  See  whortleberry, husband,  n.  —  ME.  husbonde,  ‘master  of  a  house, husband’,  fr.  OE.  husbonda,  ‘master  of  a  house’, fr.  ON.  hiisbondi,  ‘householder;  husband’, which  is  shortened  fr.  husbuandi,  a  word  lit. meaning  ‘dwelling  in  the  house’,  compounded of  ON.  hits,  ‘house’,  and  buandi,  ‘dwelling’,  prop, pres.  part,  of  bua,  ‘to  dwell’.  See  house  and bond,  ‘serf’.
29078:platband,  n.  ( archit .)  —  F.  plate-bande,  lit.  ‘a  flat band’,  fem.  of  plat,  ‘flat’,  and  bande,  ‘a  band’. See  plat,  ‘piece  of  ground’,  and  band,  ‘a  tie’, plate,  n.,  thin  sheet  of  metal,  etc.  —  ME.  plate, fr.  OF.  plate,  ‘sheet  of  metal’,  prop.  fem.  of  plat, ‘flat,  even’,  used  as  a  noun,  fr.VL.  *plattus,  fr.  Gk. -Xaxu;,  ‘flat,  wide,  broad’.  See  place  and  cp. plat,  ‘piece  of  ground’,  plat,  ‘course  at  a  meal’. Cp.  also  the  second  element  in  vamplate. Derivatives:  plate,  tr.  v.,  plat-ed, plate- fid.  adjs., plat-er,  n.,  plat-ing,  n.
```


## [2026-09-05T14:04:22.403Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1380,1392p' SKT.txt",
 "description": "Skeat banner entry"
}
```


### [2026-09-05T14:04:22.459Z] TOOL RESULT

```
bank  (a>,  for  money.    (F.-TeuJ banque,  a  money-changer's  tabic  or -O.  Du.  bamk,  M.  H.  G.  bant,  « Uble.
bankrupt  (F.- Ital. -Tent. Modified  from  F.  bcxn^juetvu by  a  knowledge  of  the  rein' to  I..  — >'■"    »•-'  .-  ^  "<■ bn.L
—  M.  M.G.  bftnct  a  tKUcli;  and   i^,  rwm^l (em.  of  mftui,  i»p.  of  r>tm/<ft,  to  faieak.    |
baaqikot  (F.«-Tcut)    Y.  Samtrnti  $i
BANNER.
^^  B  MBsD  bencfa  or  Ubie ;  dimin. ^Kvlif.  H.G.  6a$te,  a  bench.  Ublc.
^^mmk,  •  tench,    tabic,   bonk   for nSmA.  snd  Vm.  6imk ;  G.  bank. MK^BAlUMret :  see  Bind. ^■k*  ft  cake;  (C.)  OmL  ^ffmK^,  a
i
BARD.
29
fil.  of  B&a,  q.  ?. IL  (K.-T«ul.)     See  B&nk. (Jjin.)    A  fowl  from  Baniatti,
r«  nSSiaj.    (Unknown.)
■a  Infiinl.  (E,)  Prob.  for IbV,  CBt  wnpped  in  twaddling  bands ; loufe  dbnlR.  uflu  -Aii^.  See  Bind. gr«Ji>  •  tf<c  (Skt.)  An  KiigUsh. bmIvv  Mine  for  the  tree.  So  called IC  wttA  M  a  nmrkct-fiUae  for  mer- 'Uuuijrau.'  at  we  teimed  them ; Il«H!wn,  Trm*cU,  cd.  1665,  pp. t.  A0iy»  a  merchant. Uvc  (ACncui.}    The  native
```


## [2026-09-05T14:04:27.692Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"banneret\\|baniere\\|bandum\" SKT.txt | head -8",
 "description": "Skeat banner/banneret"
}
```


### [2026-09-05T14:04:27.750Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:04:34.307Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ban/ner, n\\|banner, n\\.\" WEB_vol1.txt FSD_vol1.txt 2>/dev/null | head -5",
 "description": "Webster/Funk banner"
}
```


### [2026-09-05T14:04:34.393Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:04:37.204Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"bandum\" WEB_vol1.txt FSD_vol1.txt LKT.txt DEV.txt 2>/dev/null | head -6",
 "description": "search bandum in Webster/Funk"
}
```


### [2026-09-05T14:04:37.278Z] TOOL RESULT

```
WEB_vol1.txt:15661:or city. ban’nêr, n. [ME. banere; OFr. banere, baniere; . bandum, from Goth. bandwa, a sign.] of (fag, a military ensign or standard; an man oem Hee the Star-Spangled Ban- ; y with banners. A ae Streamer, formerly borne at the end of a an or spear, as the standard of a military i potas ere point, i rf 0 7, the upper petal of a papiliona-
WEB_vol1.txt:41686:con/tra-band, a. [It. contrabbando, from L. conira, against, and LL. bandum, bannum, a proclamation.] prohibited or excluded by roclamation, law, or treaty; forbidden by aw to be exported or imported.
FSD_vol1.txt:35032:4.  [China.]  One  of  the  eight  divisions  of  the  imperial Manchu  army,  each  having  its  peculiar  banner;  also,  a division  of  a   Mongol  tribe.  5.  Bot.  The  large  upper petal  of  a   papilionaceous  blossom;  the  vexillum.  G.  Her , A   small  flag,  nearly  square,  or  a   pennant  with  the  points tom  off.  7.  A   vanedike  form  of  railroad  switch-target. 8.  [Slang,  U.  S.]  A   can  of  beer  shared  by  several drinkers.  9.  [Hist.]  A   company  of  men  following  a banner.  [ME.  feanere,  <   OF.  banxere,  <   LL.  banderia, banner,  <   bandum,  standard,  <   MHG.  band,  band, strip  of  cloth,  or  <   a   stem  seen  in  Goth,  bandwa, bandird,  sign,  token.  Both  <   stem  of  band.]  ban'erf.
FSD_vol1.txt:78400:Woolsey  Inter.  Law  p.  324.  is.  1891.] 2.  Contrary  to  or  outside  of  the  law;  as,  a   contraband distillery.  [<  It.  contrabbando,  <   L.  contra  (see  con- tra-) +   EL.  bandum,  bannum;  see  ban1,  n.J  —   contra- band goods,  goods  smuggled  into  a   country.
```


## [2026-09-05T14:05:02.785Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/patch87.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\np=\"/home/sfmqrb/git/rishe/data/verification/page-87.json\"\nd=json.load(io.open(p,encoding=\"utf-8\"))\nN={n[\"id\"]:n for n in d[\"entries\"][0][\"nodes\"]}\n\n# node 15: replace vague SKT note with the real quote\nfor c in N[15][\"consulted\"]:\n    if c[\"src\"]==\"SKT\":\n        c[\"where\"]=\"s.v. Basket\"\n        c[\"note\"]=\"'Basket. (C.) M.E. basket. - W. basged; Corn. basket; Irish bascod; Gael. bascaid, a basket. Perhaps from W. basg, a platting.' - Skeat takes it as a Celtic word, not from Latin fascis.\"\n\n# node 21: Klein's ribbon remark supports Nourai; Skeat contradicts\nfor c in N[21][\"consulted\"]:\n    if c[\"src\"]==\"KLN\":\n        c[\"where\"]=\"p.146 s.v. band 'a tie'\"\n        c[\"stance\"]=\"supports\"\n        c[\"note\"]=\"'band, n., a tie. - ME., fr. ON. band, rel. to OS., Swed., Du., G. band, OHG., MHG. bant, Goth. bandi, lit. ‘that which binds’, fr. I.-E. base *bendh-, ‘to bind’ ... See bind and cp. bend, bond. Cp. also bandage, bandanna ... and the second element in ribband, ribbon, roband, seerband.' - Klein does put the second element of ribbon here, which is Nourai's warrant for including it.\"\n    if c[\"src\"]==\"SKT\":\n        c[\"where\"]=\"s.v. Riband, Ribbon\"\n        c[\"stance\"]=\"contradicts\"\n        c[\"note\"]=\"'Riband. Ribbon. (F.) Not allied to band; the final d is excrescent. M.E. riban ... - Irish ribin, a ribbon, from ribe, a hair, flake, ribbon; Gael. ribean, a fillet' - Skeat denies the connection with band outright.\"\n\n# node 22: replace the unreadable Skeat entry with Funk & Wagnalls\nfor c in list(N[22][\"consulted\"]):\n    if c[\"src\"]==\"SKT\":\n        c[\"src\"]=\"FSD\"\n        c[\"where\"]=\"vol.1 s.v. banner\"\n        c[\"stance\"]=\"supports\"\n        c[\"note\"]=\"'[ME. banere, < OF. banere, < LL. banderia, banner, < bandum, standard, < MHG. band, band, strip of cloth, or < a stem seen in Goth. bandwa, bandwa, sign, token. Both < stem of band.]' - Funk & Wagnalls, like Klein, refers both possible sources to the stem of band, i.e. to *bhendh-.\"\n\n# node 23: replace Skeat with Webster (Skeat's OCR of the banner article is illegible)\nfor c in list(N[23][\"consulted\"]):\n    if c[\"src\"]==\"SKT\":\n        c[\"src\"]=\"WEB\"\n        c[\"where\"]=\"vol.1 s.v. banner\"\n        c[\"stance\"]=\"supports\"\n        c[\"note\"]=\"'ban'ner, n. [ME. banere; OFr. banere, baniere; LL. bandum, from Goth. bandwa, a sign.]' - the ME banere < OF baniere step is common ground; Webster, like Etymonline, stops the chain at Gothic bandwa 'sign'.\"\n\n# node 19 / 16: Webster quote made exact\nfor nid in (16,19):\n    for c in N[nid][\"consulted\"]:\n        if c[\"src\"]==\"WEB\":\n            c[\"where\"]=\"vol.1 s.v. fascism\"\n            c[\"note\"]=\"'fas/cism (fash'izm or fas'), n. [It. fascismo, from fascio, a political group, an organization, a club, from L. fascis, a bundle or packet.]'\"\n\n# node 3: rename the odd src key\nfor c in N[3][\"consulted\"]:\n    if c[\"src\"]==\"MON/Wiktionary\":\n        c[\"src\"]=\"Wiktionary\"\n\nwith io.open(p,\"w\",encoding=\"utf-8\") as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/patch87.py && python3 -m json.tool data/verification/page-87.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 87",
 "description": "Patch consulted notes and re-verify"
}
```


### [2026-09-05T14:05:04.731Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 23/23
node verdicts: {'plausible': 8, 'confirmed': 10, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'partial': 6, 'not_checked': 12, 'contradicts': 2}
books consulted: {'supports': 41, 'partial': 8, 'contradicts': 5, 'silent': 3} | by book: {'KLN': 8, 'LKT': 5, 'SKT': 5, 'POK': 4, 'CHEUNG': 3, 'PHD': 3, 'HRN': 3, 'MON': 3, 'WEB': 3, 'BRT': 2, 'WLD': 2, 'HJB': 2, 'KNT': 2, 'NYB': 2, 'AHD': 2, 'PHN': 1, 'BQT': 1, 'Wiktionary': 1, 'HUB': 1, 'PLA': 1, 'SYN': 1, 'IEC': 1, 'FSD': 1}
```


## [2026-09-05T14:05:14.933Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport json, io\np=\"data/verification/page-87.json\"\nd=json.load(io.open(p,encoding=\"utf-8\"))\nn=[x for x in d[\"entries\"][0][\"nodes\"] if x[\"id\"]==18][0]\nn[\"derivation\"]=(\"Persian فاشیسم fāšism and فاشیست fāšist are 20th-century borrowings from French fascisme/fasciste: \"\n \"the abstract suffix -isme > Persian -یسم and the agent suffix -iste > -یست are the standard shapes of the whole \"\n \"French-mediated political vocabulary that entered Persian in the Reza Shah period (سوسیالیسم، کمونیسم، ناسیونالیسم), \"\n \"and the š of فاشیسم reflects the French/Italian pronunciation [faʃism] rather than any Latin spelling. \"\n \"Mo'in marks فاشیست explicitly '[فر.]' = French, which is exactly the arrow drawn.\")\njson.dump(d, io.open(p,\"w\",encoding=\"utf-8\"), ensure_ascii=False, indent=2)\nio.open(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 -m json.tool data/verification/page-87.json >/dev/null && python3 tools/verify_check.py 87 | head -4\nhead -c 3 data/verification/page-87.json | xxd | head -1",
 "description": "Fix node 18 wording, final check"
}
```


### [2026-09-05T14:05:17.135Z] TOOL RESULT

```
ok
nodes verified: 23/23
node verdicts: {'plausible': 8, 'confirmed': 10, 'disputed': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 16, 'partial': 6, 'not_checked': 12, 'contradicts': 2}
00000000: 7b0a 20                                  {.
```


## [2026-09-05T14:05:32.678Z] AGENT

Page 87 (book p. 57), root **Bhendh** — one entry, 23 nodes, all verified. `verify_check.py 87`: **0 PROBLEM lines**.

**Verdicts:** root confirmed · nodes: 10 confirmed, 8 plausible, 4 disputed, 1 transcription_suspect. Ref checks: 16 supports, 6 partial, 2 contradicts, 12 not_checked (SAP, FVF, AEF, OEW and the AHD main-dictionary pages are not obtainable).

**Disputed**
- #14 Latin `fascis` — Pokorny puts fascis under *bʰasko-* (p. 111, with Mir. *basc*, OBrit. *bascauda*), not under bhendh- (p. 127); Klein, the reference Nourai himself cites, says the same.
- #15 English `basket` — Klein p. 152 makes *bascauda* a **cognate** of *fascis*, not a descendant; Etymonline/OED: "of obscure origin".
- #13 Persian `bastan; anbast; anfast` — bastan and anbast confirmed (Horn 219; Hübschmann p. 18 = Av. *ham+basta-*), but `anfast` "spider web" rests on Salemann's conjecture, which Horn (Nachtrag 122a) calls "unsicher" and Hübschmann rejects outright.
- #22 French `bannier` — Watkins indexes BANNER under *bʰeh₂-* "to shine" (Goth. *bandwa* "sign"), as does Etymonline; Klein p. 146 and Funk & Wagnalls are the minority that support Nourai.

**transcription_suspect**
- #17 French `fascism` — not a possible French form (fascisme). Checked the rendered page: **the book prints "fascism"**, so the error is Nourai's, not the extraction's. `error_in: "book"`.

**No extraction errors** — the JSON matches printed p. 87 box for box, including the book's own defective "fascism" and "bannier".

Notable findings: Pihan p. 363 is the exact source of Nourai's note that *dul-* is Arabic *dawl* "tour" (Hobson-Jobson s.v. TURBAN agrees; Lokotsch 544/Horn read Persian *dil* "heart" instead) — so #2 is plausible, not wrong. SOD:105 checks out as Gharib's page with Sogdian βnty < Olr. \*bandaka-. Kent p. 199 and Nyberg confirm the OP → Phl → NP *bandaka/bandag/banda* chain verbatim. Page image archived to `data/verification/sources/refs/ocr/BOOK/87.png`; 9 web sources archived via fetch_source.py.
