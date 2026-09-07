# Verification process log — verify-page-335


## [2026-09-07T16:16:15.459Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 335 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-335.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-335.json. Write /home/sfmqrb/git/rishe/data/verification/page-335.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 335` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:16:17.568Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:16:18.300Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:16:18.347Z] TOOL RESULT

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


## [2026-09-07T16:16:18.832Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-335.txt"
}
```


### [2026-09-07T16:16:18.854Z] TOOL RESULT

```
1	=== PDF page 335 (book page 305) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mer 2
4	Mer-d, Mer-k
5	Mor-to
6	Smerd : to rub away, harm, die
7	destroy
8	mortal man
9	painful  (refs POK:735,970; AHD:1529)  PART 1
10	#1 (parent #0) [Avestan] refs=POK:735; BQT:1872,1934,1982-6; KLN:1005 | mar 2 : to die ; mahrka, marathyu : death ; mareta, maša : mortal man ; mardta : everyone ; gayo-mereta : perishable life, human ☞Gwei ; a-mereta, amaša : eternal
11	  #2 (parent #1) [Persian] refs=BQT; HRN:218-9; ZMA:21 | mordan «مردن ( مرگ )» : to die ; mard «مرد ( مردم )» : mortal man ; Kîŭmars «کیومرث» : "mortal world, man" ; amordâd «امرداد ( مرداد )» : "not mortal"
12	  #3 (parent #1) [Pahlavi] refs=SOD:219; BQT:2017 | murdyânag, mašyânag : mortal man ; maša : Adam ; mašyôi : Eve
13	    #4 (parent #3) [Persian] refs=SOD:218; BQT:2017 | mašyâ «مشیا» : Adam ; mašyâneh «مشیانه ( مشیوئی )» : Eve
14	  #5 (parent #1) [Avestan] refs=AEF:378; HRN:69 | awiš-mar, wizmar : to fade, wither | NOTE: HUB:41 does not agree with this derivation
15	    #6 (parent #5) [Persian] refs=BQT:400 | pajhmordan «پژمردن ( پژمریدن )» : to fade, wither
16	#7 (parent #0) [Avestan] refs=POK:737; KNT:203 | morandat, marenčaiti : destroys ; maraxš : spoil ; mared : destroy
17	#8 (parent #0) [Old Persian] refs=KNT:202,203; SOD:218,225 | mar, mariya : to die ; marta : dead ; martiya : mortal man
18	  #9 (parent #8) [Sogdian] refs=SOD:218 | marty : man
19	#10 (parent #0) [Old Persian] refs=KNT:203 | mard : crush ; mard-una : crusher of grapes into wine, wine merchant
20	  #11 (parent #10) [Persian] refs=KNT:203 | mol «مُل» : wine | NOTE: For another possible root of Persian "mol: wine" see root "Medhu".
21	#12 (parent #0) [Greek] refs=POK:736 | maraino : rub off ; marmaros : polished stone, rock ; marmaron : marble
22	  #13 (parent #12) [Persian] refs=MON:4045; BQT:1996 | marmar «مَرمَر ( مرمرین )» : marble stone
23	  #14 (parent #12) [Latin] refs=AHD:797 | marmor : marble
24	    #15 (parent #14) [French] refs=AHD:797 | marbre
25	      #16 (parent #15) [English] refs=AHD:797 | marble
26	#17 (parent #0) [Germanic] refs=AHD | marôn : goblin ; mur-thra : murder
27	  #18 (parent #17) [English] refs=AHD | nightmare ; murder
28	
```


## [2026-09-07T16:16:23.041Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-335.json",
 "description": "Read source JSON page 335"
}
```


### [2026-09-07T16:16:23.076Z] TOOL RESULT

```
{
  "pdf_page": 335,
  "book_page": 305,
  "entries": [
    {
      "part": 1,
      "root": {
        "name": "Mer 2\nMer-d, Mer-k\nMor-to\nSmerd",
        "lang": "Indo-European",
        "refs": "POK:735,970; AHD:1529",
        "gloss": "to rub away, harm, die\ndestroy\nmortal man\npainful"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:735; BQT:1872,1934,1982-6; KLN:1005",
          "words": [
            {"translit": "mar 2", "gloss": "to die", "script": null},
            {"translit": "mahrka, marathyu", "gloss": "death", "script": null},
            {"translit": "mareta, maša", "gloss": "mortal man", "script": null},
            {"translit": "mardta", "gloss": "everyone", "script": null},
            {"translit": "gayo-mereta", "gloss": "perishable life, human", "script": null, "see": ["Gwei"]},
            {"translit": "a-mereta, amaša", "gloss": "eternal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT; HRN:218-9; ZMA:21",
          "words": [
            {"translit": "mordan", "gloss": "to die", "script": "مردن ( مرگ )"},
            {"translit": "mard", "gloss": "mortal man", "script": "مرد ( مردم )"},
            {"translit": "Kîŭmars", "gloss": "\"mortal world, man\"", "script": "کیومرث"},
            {"translit": "amordâd", "gloss": "\"not mortal\"", "script": "امرداد ( مرداد )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SOD:219; BQT:2017",
          "words": [
            {"translit": "murdyânag, mašyânag", "gloss": "mortal man", "script": null},
            {"translit": "maša", "gloss": "Adam", "script": null},
            {"translit": "mašyôi", "gloss": "Eve", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "SOD:218; BQT:2017",
          "words": [
            {"translit": "mašyâ", "gloss": "Adam", "script": "مشیا"},
            {"translit": "mašyâneh", "gloss": "Eve", "script": "مشیانه ( مشیوئی )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Avestan",
          "refs": "AEF:378; HRN:69",
          "words": [
            {"translit": "awiš-mar, wizmar", "gloss": "to fade, wither", "script": null}
          ],
          "note": "HUB:41 does not agree with this derivation",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:400",
          "words": [
            {"translit": "pajhmordan", "gloss": "to fade, wither", "script": "پژمردن ( پژمریدن )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:737; KNT:203",
          "words": [
            {"translit": "morandat, marenčaiti", "gloss": "destroys", "script": null},
            {"translit": "maraxš", "gloss": "spoil", "script": null},
            {"translit": "mared", "gloss": "destroy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:202,203; SOD:218,225",
          "words": [
            {"translit": "mar, mariya", "gloss": "to die", "script": null},
            {"translit": "marta", "gloss": "dead", "script": null},
            {"translit": "martiya", "gloss": "mortal man", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Sogdian",
          "refs": "SOD:218",
          "words": [
            {"translit": "marty", "gloss": "man", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:203",
          "words": [
            {"translit": "mard", "gloss": "crush", "script": null},
            {"translit": "mard-una", "gloss": "crusher of grapes into wine, wine merchant", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "KNT:203",
          "words": [
            {"translit": "mol", "gloss": "wine", "script": "مُل"}
          ],
          "note": "For another possible root of Persian \"mol: wine\" see root \"Medhu\".",
          "quote": {
            "text": "به زرّینه جام اندرون لعل مل - فروزنده چون لاله بر زرد گُل",
            "poet": "Onsorî"
          }
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:736",
          "words": [
            {"translit": "maraino", "gloss": "rub off", "script": null},
            {"translit": "marmaros", "gloss": "polished stone, rock", "script": null},
            {"translit": "marmaron", "gloss": "marble", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:4045; BQT:1996",
          "words": [
            {"translit": "marmar", "gloss": "marble stone", "script": "مَرمَر ( مرمرین )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Latin",
          "refs": "AHD:797",
          "words": [
            {"translit": "marmor", "gloss": "marble", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": "AHD:797",
          "words": [
            {"translit": "marbre", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "AHD:797",
          "words": [
            {"translit": "marble", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "marôn", "gloss": "goblin", "script": null},
            {"translit": "mur-thra", "gloss": "murder", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "nightmare", "gloss": null, "script": null},
            {"translit": "murder", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T16:16:23.711Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:16:23.796Z] TOOL RESULT

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


## [2026-09-07T16:16:29.962Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KNT','HRN','HUB','SOD','BQT','MON','KLN','AEF','ZMA','BRT','PHD','NYB','WLD','IEC','SYN','LEW','SKT','CHEUNG']:\n    v=d.get(k)\n    print('===',k)\n    if v is None: print('  MISSING'); continue\n    print(json.dumps(v,ensure_ascii=False,indent=1)[:1400])\n\""
}
```


### [2026-09-07T16:16:31.670Z] TOOL RESULT

```
=== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbe
=== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local
=== KNT
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
=== HRN
{
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
}
=== HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
=== SOD
{
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
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 199
=== BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltex
=== MON
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
  "/home/sfmqrb/git/rishe/data/verif
=== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/s
=== AEF
{
 "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
 "kind": "catalog",
 "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
 "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "none online; proxy via HRN/HUB. || RE-SEARCH 2026-09: still catalogue/purchase only (Open Library record; iketab second-hand; digikala dkp-3058984 for the 2015 ed.). Publisher of the 2015 ed. is مهرافروز."
}
=== ZMA
{
 "title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995",
 "kind": "purchase",
 "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)",
 "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."
}
=== BRT
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
=== PHD
{
 "title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971",
 "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-concise-pahlavi-dictionary",
 "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).",
 "notes": "",
 "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"
}
=== NYB
{
 "title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)",
 "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg",
 "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
 "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.",
 "notes": " local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt"
 ],
 "cites": "page number of Nyberg, A Manual of Pahlavi, Part II Glossary (1974)"
}
=== WLD
{
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927
=== IEC
{
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
=== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
=== LEW
{
 "title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56",
 "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/lateinischesetym0000aloi",
 "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt",
 "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.",
 "notes": ""
}
=== SKT
{
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
}
=== CHEUNG
  MISSING
```


## [2026-09-07T16:17:06.568Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma mer ===\"; grep -n \"lemma: mer\" POK_full.txt | head -40\necho \"=== POK_full lemma smer ===\"; grep -n \"lemma: smer\" POK_full.txt | head -20\necho \"=== POK_full Page 735 ===\"; grep -n \"Page(s): 73[4-8]\" POK_full.txt | head -20\necho \"=== POK_full Page 969-971 ===\"; grep -n \"Page(s): 9[67][0-9]\" POK_full.txt | head -20"
}
```


### [2026-09-07T16:17:06.659Z] TOOL RESULT

```
=== POK_full lemma mer ===
40298:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
58134:< kw\; alb. proves that from Root / lemma: mer-2, *extended mer-ek-\ "to shimmer, shine' 
60116:Root / lemma: mer-4, mera- 
60176:Root / lemma: mer-5, mera- 
60183:Root / lemma: mer-5, mera-\ to rub, wipe; to pack, rob, derived from extended Root/ 
60285:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
60313:Root / lemma: mer-6, mer-s- 
=== POK_full lemma smer ===
78543:Root / lemma: smerd-, smord- 
78564:Root / lemma: smeru- 
=== POK_full Page 735 ===
59808:Page(s): 738 
59827:Page(s): 738 
59843:Page(s): 738 
59867:Page(s): 738 
59871:Page(s): 738 
59911:Page(s): 738-739 
60090:Page(s): 734 
60114:Page(s): 734 
60174:Page(s): 735 
60311:Page(s): 735-737 
60328:Page(s): 737-738 
=== POK_full Page 969-971 ===
77946:Page(s): 960 
77997:Page(s): 960-961 
78011:Page(s): 961 
78039:Page(s): 961-962 
78045:Page(s): 962 
78070:Page(s): 963-964 
78098:Page(s): 964 
78122:Page(s): 964 
78144:Page(s): 964-965 
78236:Page(s): 962-963 
78315:Page(s): 960 
78337:Page(s): 965 
78356:Page(s): 965 
78376:Page(s): 965-966 
78406:Page(s): 967 
78444:Page(s): 967-968 
78461:Page(s): 968 
78493:Page(s): 968 
78523:Page(s): 969 
78541:Page(s): 969
```


## [2026-09-07T16:17:07.839Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD mer- ===\"; grep -n \"^mer-\" AHD_watkins1985.txt | head; grep -n \"^smerd\" AHD_watkins1985.txt|head\necho \"=== KNT martiya ===\"; grep -n \"^martiya\\|^marta\\|^mariya\\|^mar-\\|^mard\\|Mardu\" KNT.txt | head -30"
}
```


### [2026-09-07T16:17:07.924Z] TOOL RESULT

```
=== AHD mer- ===
750:mer-'
752:mer-'. To flicker; with derivatives referring to dim states of illumination. 1. Suffixed form *mer-o- in Latin merus, pure, unadulterated (< “unmixed wine” < “clear liq- uid”): MERE!, 2. Extended form *merk- in Germanic *murgana- in: a. Old English morgen, morning: MORN, MORNING, MORROW; b. Middle Dutch morghen, morn- ing: MORGEN; Cc. Old High German morgan, morning: MORGANATIC. 3. Possibly extended root *merg~- in Ger- manic *merkwia-, twilight, in Old English mirce, dark- ness: MURK. [Pok. 2. mer- 733.]
753:mer-2, To rub away, harm. I. 1. Germanic *marén-, goblin, in Old English mare, mere, goblin, incubus: NIGHTMARE. 2. Greek marainein, to waste away, wither: MARASMUS; AMARANTH. 3. Probably suffixed zero-grade form *mr-to-, “ground down,” in Latin mortdrium, mor- tar: MORTAR. 4. Possibly extended root *merd- in Latin mordére (past participle morsus), to bite: MORDACIOUS, MORDANT, MORDENT, MORSEL; PREMORSE, REMORSE. 5. Possibly suffixed form *mor-bho- in Latin morbus, disease (but more likely of unknown origin): MORBID. II. Possibly the same root, but more likely distinct, is *mer-, “to die,” with derivatives referring to death and to human beings as subject to death. 1. Zero-grade form *mr- in: a. suffixed form *mr-tro- in Germanic suffixed form *mur-thra- in Old English morthor, murder: MUR- DER; b. suffixed form *mr-ti- in Latin mors (stem mort-), death: MORT!, MORTAL, MORTUARY; AMORTIZE, (IMMOR-
755:mer-3. To tie. Possibly in: a. Middle Dutch marren, to tie: MARLINE; b. Middle Low German méren, to tie: MooOR!. [Pok. 1. mer- 733.]
=== KNT martiya ===
584:By the Elam. writings: Атта (or Araza), Arbairé-, Armina, Asagaria, Paréava, Fravartis (also РЫ. fravartikdn), Margu&, Marduniya, -vard- in Ar- tavardiya, Vidafarna (also Av. хатто), Vidarna, Sparda, haumavargd: many of these confirmed also by Greek forms, ete.
1811:П. Secondary -па-, forming adjectives: para- na-, perhaps here kam-na; as mase. sb., drauja- па-, as nt. abstract pariy-ana-; forming hypo- coristic personal name, Aci-na-; perhaps Mardu- na- in Mardun-tya-; forming place names, with lengthening of preceding vowel, Varkàna- to varka-, Ha"-gmalàna- to ha?-gmala-; with -na- of uncertain origin, h*zdna- (see Lex. s.v.).
1838:I. Stems in -й-: adj. par-u-, ard-u- in personal name Ardu-mants-, va-u- in personal names Déraya-vau- Vau-misa- Vahau-ka-; substantives baru- in Gau-barw-a-, maršiy-u- ‘death’ in adj. uvd-marSiyu-, mard-u- in Marduniya-, Mag-u-, Hitd-u-, Marg-u-, Kür-u-, uncertain bat-u- in bátu- gara-; loanwords pir-u-, Ufrat-u-; restored loan- word agur-u-; uncertain as to stem, Qatag-u-, sikabr-u-.
1941:b. Names of other Persians: Artavardiya-, Ardumants-, Aspacanah- (M), Ulana-, Өилта-, Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, Marduniya-, Vaumisa- (with -s- which is not Per- sian nor Median), Vayaspara-, Vahauka-, Vahyaz- dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- manis-.
1956:IV. Still other names are appellatives indicat- ing the qualities of the persons, like the redupli- cated Dé-dar- ‘Bold’. Possibly *U-vazstra-, Vi- darna-, Vi-vàna- (given under П) also belong here. Or names may denote occupations, as per- haps in the adjectival derivative, possibly pa- tronymie, Mardun-iya- ‘Vintner’s son’.
3876:83 à : Vidafarnà : пато : V&yaspárahy& : puça : Parsa : Utàna : пата : Guxrahyá 84 : риса : Parsa : Gaubaruva : паша : Marduniyahyá : puça : Parsa : Vidarna : nama : Ва 85 gabignahya : puça : Parsa : Bagabux’a : пата : Dütuvahyahyà : риса : Pársa :
4859:Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
5775:mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
5780:marta- ріс. as ad]. ‘dead’: Av. marata-,-N Pers. murd, Skt. mrid-, Gk. Вротос (for *Sparós, with vowel assimilation), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
5785:martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ 16, 19, 21, 24; XPh 51. martiyà узш. "Ма 56. martiyam asm. DB 3.57; DNa 3; DNb 12, 22; DSe 3; DSf 2, 16f; DSs 2; DSt 3°; рле 2; DE 4f; XPa 2; XPb 4f; XPe 21; XPd 3f; XPf 3; XPh 3; XE 5; XV 4; A'Pa 3P; А°Не 3f; A?Pa 3f. martiyahyé gsm. DNa 4, 44; ОМ 3; DSe 4f; DSf
5789:mard- vb. ‘crush’: Av. marad- ‘destroy’, Skt. mrd- ‘rub, crush’, Lt. mordet ‘bites’, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.
5791:Marduniya- sb. 'Mardonius, father of Gobryas: Elam. mar-du-nu-ia, Gk. Марббио; per- haps deriv. to *marduna- ‘vintner’ (§144.IV, 8147. П, $153.1, $164.1V), ef. NPers mul ‘wine’, Skt. mydvikd- ‘grapevine’ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‘crush (the grapes in the wine-making)’. Marduniyahya gsm. DB 4.84.
```


## [2026-09-07T16:17:16.788Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### POK mer-4 / mer-5 blocks\"; sed -n '60110,60200p' POK_full.txt\necho \"###### POK mer-5 main\"; sed -n '60300,60340p' POK_full.txt"
}
```


### [2026-09-07T16:17:16.857Z] TOOL RESULT

```
###### POK mer-4 / mer-5 blocks
bathe, wallow '. 

References: WP. II 279 f., Trautmann 169, Specht Indo Germanic Dekl. 119. 

Page(s): 734 

Root / lemma: mer-4, mera- 

Meaning: to die 

Note: (= mer-5^ become faded ') 

Material: Old Indie marati, marate ^d'\es\ Armenian meranim^6\e\ gr. Efjoprsv " died ' Hes. 

(compare Lithuanian men's m., mirei. "death', merdeti^be dying'); causative Old Indie 

marayati' slays ', osset. /775/y/7"slay', Lithuanian marinti, serb. mdr/f/6s., etc.; zero grade 

Old Indie mr/yate^6\es', Avestan miryeite{= me'rye'te) ds.. Old pers. a-mariyata^he died ', 

Latin morior {*mr-idr) "I die, expire '; Balto-Slavic *m/re-\n Lithuanian mirstu, m/rt/^6\e', 

Latvian mirstu, m/rtds. (in addition Lithuanian m/re'the dead ', Latvian m/rejsm. " dying, 

death '); Old Church Slavic mtrg, mret/an6 -mbret/6s., Hittite me-ir-ta {mert) " died '. 



participle mf-to-^ dead ' in Old Indie mrta-= Avestan msrsta-^ dead ', Armenian mard 
"person' ("mortal, human being'), Latin Morta, "Death goddess', Balto-Slavic *mirta-^ dead 
' in Lithuanian mirtoji diena^ anniversary of somebody's death ', Old Church Slavic u- 
mrbtijeu. "death', etc.; ^-/77/-to- "immortal, living ' in Old Indie amrta-, Avestan amasa-, gr. 
apppoToq (Aeolic po for pa), therefrom apppoaioc; " belonging to the immortal '; from 
aM(3poTO(; abstracted ppoT6(; " perishable ' and pp6T0(; " blood that has run from a wound, 
gore, coagulated blood ' (M. Leumann, Homer. Worter 126 ff.). 

/77/-/'d-/77 "death' in Old Indie mrta-v\. "death'. Old High German mord. Old English Old 
Icelandic mordu. "murder' (besides *mr-tro-m\v\ Gothic maurt^ru.. Old English mordoru. 
"murder'). 

/T?/-/"/- "death' in Old Indie mrti-, Avestan msreti-, Latin mors, -tis, Lithuanian mirtis. Old 
Church Slavic si>-mrbtb {irorc\ *-mrbtb), serb. smft, etc. 

Maybe alb. /77c»/Y"funerar, /770/^e "death' a Latin loanword. 

/77/-/it/ "death' in Armenian mah, older marfr, with -//■ contaminated: Old Indie mrtyu-, 
Avestan msrs^yu- 6s. 

mor-to-^ perishable ' in Old Indie marta-, Avestan /77as5- "person', with sound change 
mareta-^ perishable, mortal, human being', gr. popT6(; "person, mortal, human being' Hes. 
(for *p6pT0(;); derived *mor-t/o-\n Old Indie martya-, Avestan masya-. Old pers. martiya-^ 
perishable, mortal, human being'. 

mf-u6-^ dead ' in Old Irish mart, cymr. etc. marw, gall. *marvos{U.-\-. 5387a); unclear 
gall. (?) Mori-marusa^ mortuum mare '; through influence oi mr-tu- to *mr-tu-o-\n Latin 
mortuus' dead ', Old Church Slavic mrbtvb {mrbtvb) ds. 

/77d/"0-5 "death' in Old Indie /77a/'a- "death', Lithuanian maras^ plague ', Old Church Slavic 
morb ds. 

After Thieme Studien 55 here (?) gr. papTU(; (*-p<;), -po(;, hom. papTupo(; " witness, 
testifier ' (" Schworender ') from * mrt-tur- {11) "the griping death ' (root /it/e/"- "catch'). 

References: WP. II 276, WH. 112 f., Trautmann 186 f., Thieme Studien 15 ff. 
Page(s): 735 

Root / lemma: mer-5, mera- 
Meaning: to rub, wipe; to pack, rob 



Note: 

Root / lemma: mer-5, mera-\ to rub, wipe; to pack, rob, derived from extended Root/ 

lemma: mah-1 \ to becl<on with the hand; to deceive + with formants -ra-: 

Material: Old Indie mrnati, mrnatT robs ', a-man-tar-^ robber ', amrnaV robbed ', malf-mlu- 

" robber'; but mrnati^ crushes, smashes ', murna-^ crushed, damaged, faded ' belong 

rather to mel-1, also maru-m. 'sand, desert, waste, wasteland, rock'; 

gr. [japaivu) " rub, wipe, consume, weaken'. Pass. " verzehre myself, verschwinde 

i 

allmahlich, ermatte ', |japaaM6(; ' Hinschwinden, Krafteverfall '; papva|jai ' fight '; 
Mappapo(; ' stone, boulder ' (compare Latin rupes : rumpo), later (after papfjaipoj) "white 
stone, marble ' (out of it Latin marmoi); 

###### POK mer-5 main
mer-s- 

Old Indie masam, masfm kar-^ pulverize ', masi-, masV powder '; 

Old High German morsar/^ mortar' (reshaped from Latin mortarium, s. S. 736), Middle 
High German zermursen ' crush, squeeze hard, squash ', md. zermorschen ds., Swiss 
morsen, mursen' crunch, shove ', Middle High German Low German mursch, murs. 
Modern High German morsch, Dutch morzelen^ grind '. 

References: WP. II 276 ff., WH. 42, 110 ff.; 
See also: identical with mer-4. 
Page(s): 735-737 

Root / lemma: mer-6, mer-s- 
Meaning: to bother, anger, etc.. 



Material: Old Indie mrsyate' forgets, neglects, forgives ', marsa-xw. " patience ', mrsa 
"free, wrong ', Kaus. marsayatT suffers, forgives '; Armenian moranam ^iorqei' (Meillet, 
Esquisse2 40); Gothic marzjan ^ anger' , Old English mierran. Old Saxon merrian. Old 
Frisian meria. Old High German marren, /77e/7'e/7 'hinder, disturb, bother'; Old English a- 
m/erran'spoW, Old Frisian mere'ban6, strap, manacle'; Lithuanian marsas^ oblivion ', in 
addition marsus^ forgetful ', Latvian aiz-marsai. 'forgetfulness'; Lithuanian mirstu, mifsti 
(only with uz-, pa-) and Latvian aiz-mirstu, a/z-m/rst lorgotten' , Lithuanian Kaus. mars/nt/" 
make forget '. 

References: WP. II 279, Trautmann 187. 
Page(s): 737-738 

Root / lemma: met- 

See also: see above S. 703 f. under me-2 and me-3. 

Page(s): 741 

Root / lemma: meug-1 

Meaning: to take by surprise, wily 

Material: Latin muger^ der Falschspieler beim WiJrfelspiel ' {*mug-ro-s^ lurking ');
```


## [2026-09-07T16:17:27.840Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### smerd block\"; sed -n '78535,78570p' POK_full.txt\necho \"###### grep maranc / mahrka in POK_full\"; grep -n -i \"maranc\\|marenc\\|mahrka\\|mahrk\\|marska\\|mrnati\" POK_full.txt | head -20"
}
```


### [2026-09-07T16:17:27.905Z] TOOL RESULT

```
###### smerd block
grayish brown ', Lithuanian pasme/t/" c\ou6y, dark become'. 

References: WP. II 692; 

See also: compare me/-6 above S. 720 f. 

Page(s): 969 

Root / lemma: smerd-, smord- 
Meaning: to stink 

Material: Gr. O|j6p5(jov£(; PI. "Stanker' Hes.; a|jop5o0v auvouaia^£iv; Lithuanian smirdziu, 
sm/rdet/ ^st\nk', Latvian sm/rdef6s., Lithuanian 5/77//'o'e/e "dwarf elder', s/775/'o'//7//"stinkend 
make', Latvian s/77e/io'e//s "Stanker', smards' fetidness ', Lithuanian smar[d]ve. Old 
Lithuanian smarstas' fetidness ' (also smarste, smarstvas, s/77a/'S55"schlechteres fat', 
actually " bad-smelling fat'). Old Prussian smorde^ alder buckthorn, alder dogwood '; Old 
Church Slavic smrbdeti, russ. smerdetb "stink', russ. smorod' fetidness ', smorodina' 
black currant ', poln. smrod, Czech smrad' fetidness '; in addition probably Latin merda 
"ordure, ordure of Leibes'. 

5/77e/'o'- "stink' is eine probably already Indo Germanic verselbstandigte use from 
{s)merd- in Modern High German schmerzen, Latin mordere, s. mer-, merd " chafe ' 
(above S. 736 f), originally also "beiftender smell, odor'. 



References: WP. II 691, WH. II 74 f., Trautmann 271, Vasmer2, 676, Specht KZ 62, 215. 
Page(s): 970 

Root / lemma: smeru- 

Meaning: grease, fat 

Material: Gr. probably apupi(; "Schmirgel zum Abreiben and Polieren', (a)|jupi^u) 'poliere 

through Reiben, anoint, smear, rub', [jupov n. "wohlriechendes Salbol, plant juice ', 
###### grep maranc / mahrka in POK_full
58828:Material: A. Old Indie mrnati, mrnatT crushes, grinds ', murna-^ wilted, limp' and " crushed 
60007:Latvian merga, ablaut. /775/ya 'handrail', perhaps Lithuanian marska^ linen, fishing net', 
60187:Material: Old Indie mrnati, mrnatT robs ', a-man-tar-^ robber ', amrnaV robbed ', malf-mlu- 
60189:" robber'; but mrnati^ crushes, smashes ', murna-^ crushed, damaged, faded ' belong 
60275:Old Indie Instr. Sg. mrc-a, Avestan maraxs^r\i\'c\, destruction ', Avestan maranca/t/ "\n\ures,
```


## [2026-09-07T16:17:29.464Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### POK_02 leaf for p.735-737 (leaf = p-344)\"; awk 'BEGIN{RS=\"\\f\"} NR==391||NR==392||NR==393' POK_02.txt | grep -n -i \"marmaro\\|maraino\\|papaivu\\|maranc\\|mahrk\" | head -20\necho \"### plain grep POK_02 marmor\"; grep -n -i \"marmaro\" POK_0*.txt | head"
}
```


### [2026-09-07T16:17:30.691Z] TOOL RESULT

```
### POK_02 leaf for p.735-737 (leaf = p-344)
### plain grep POK_02 marmor
```


## [2026-09-07T16:17:35.194Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '60240,60300p' POK_full.txt"
}
```


### [2026-09-07T16:17:35.242Z] TOOL RESULT

```
Old Indie mrdnati {mrdmta-, mrdita-), mardati, mardayati^ grinds, crushes, rubs ', 
Avestan 3. Sg. morandal {= mrnd-) " destroys ' (these Aryan words also are carried in Indo 
Germanic meld-, s. mel-1. Old Indie /77/o'/7a// perhaps instead of *mrnatti {*mr-n-ed-ti) 
through influence of mrnat/{see above S. 735); 

Armenian /77a/'/ 'fight, struggle'; 

gr. pap5r|v to pia^soGai yvvaiKaq ApinpaKiaJrai Hes. {*mrd-); apspSu) "rob' and " blind, 
darken', pspSsi kojAuei pAanrei Hes.; to Aor. ajJEpaai neologism aijeipoj; 

East Frisian murt^ crumbly mass, dust, powder'. Low German murten^ decompose ', 
Middle High German /t?^/^ 'stump', Swiss murz, morz^sxwaW shred'; 

Latvian merdeV let starve ' (latter meaning closer to Lithuanian merdeti, present 
merdmi, merdziu "die', that based on do- or d^opresent to *mer- "die', as also mer-d- "rub' 
would go back to o'opresent; is placed Latvian merdet Wkemse to mer-^d'\e'7); 

Latin mordeo, -ere, momordV to bite, bite into ' (= Old Indie mardayati, mamrde), also 
from feelings and sensations of taste; 

compare the 5-forms: 

gr. apspSvoc;, ap£p5aA£0(; "terrible, dreadful' ("*attritional '), Old High German smerzan 
"ache', 5/775/^0 "pain'. Middle Low German smerten. Low German Dutch smarten. Old 
English smeorfan ^ ache' , engl. 5/77a/Y "biting, sharp, witty ' and " nice, dainty'; compare also 
5/77er{/- "stink'. 

mer-k- 

Old Indie marcayat/" endangers, injures, hurts, disables, damages ', mrkta- "\n\ures, 
hurts, disables', marka-m. " dying, death' = Avestan /77a/7/'/ra- "death', conservative stem 



Old Indie Instr. Sg. mrc-a, Avestan maraxs^r\i\'c\, destruction ', Avestan maranca/t/ "\n\ures, 
hurts, disables, destructs '; Armenian more' young, tender' {*morkio-)\ 

perhaps alb. /770/7-' louse' ( *mdrko-' the scratching '? compare cpGsip ds.: cpGsipoj); 

Maybe alb. {*bddr) momlouse' : gr. cp9£ip ds.: cpGsipw : modern Greek ijjsipa : Basque 
(*9£ipu)) zorn" louse '. 

Note: 

It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
rnera-: to rub, wipe; to pack, rob, common lllyrian g'^h- > b. 

Latin /77i//ri/5 "mutilated' (out of it sizil. pupKoc; " dumb ') and murc/dus"\d\e, slack'; Middle 
High German /77c»/ye/7 'slack'. 

With ani. 5- Lithuanian smerkt/" condemn, censure, blame, reprobate, reprehend, 
declaim, deplore, sit in judgement ', 5/77a/'/r^s "cruel, savage', pa-smerkt/^spoW, Modern 
High German dial, schmorgen' starve, suffer'. 

Here (as " chaff ') Old English mearg^ sausage ' = Old Icelandic mgrr'6s., intestinal fat ' 
( *marhu-), redupl. gr. pipapKui; " blood sausage '; Hittite mar-kan-zi^ cut up '. 

see also /77e/ifr-i' "sullen' and 1. mei1(- " rotten, blight etc.'. 

mer-s-
```


## [2026-09-07T16:17:46.058Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '753,754p' AHD_watkins1985.txt\necho \"=== smerd in AHD ===\"; grep -n -i \"smerd\\|smord\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T16:17:46.126Z] TOOL RESULT

```
mer-2, To rub away, harm. I. 1. Germanic *marén-, goblin, in Old English mare, mere, goblin, incubus: NIGHTMARE. 2. Greek marainein, to waste away, wither: MARASMUS; AMARANTH. 3. Probably suffixed zero-grade form *mr-to-, “ground down,” in Latin mortdrium, mor- tar: MORTAR. 4. Possibly extended root *merd- in Latin mordére (past participle morsus), to bite: MORDACIOUS, MORDANT, MORDENT, MORSEL; PREMORSE, REMORSE. 5. Possibly suffixed form *mor-bho- in Latin morbus, disease (but more likely of unknown origin): MORBID. II. Possibly the same root, but more likely distinct, is *mer-, “to die,” with derivatives referring to death and to human beings as subject to death. 1. Zero-grade form *mr- in: a. suffixed form *mr-tro- in Germanic suffixed form *mur-thra- in Old English morthor, murder: MUR- DER; b. suffixed form *mr-ti- in Latin mors (stem mort-), death: MORT!, MORTAL, MORTUARY; AMORTIZE, (IMMOR-
‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
=== smerd in AHD ===
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
962:Sao Pain. Extension of mer-?. Germanic *smarta- in Old English smeart, causing pain, painful: SMART. [Pok. smerd- 970.]
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
```


## [2026-09-07T16:17:47.895Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN marble ===\"; grep -n \"^marble,\" KLN_1966.txt\necho \"=== KLN murder ===\"; grep -n \"^murder,\" KLN_1966.txt\necho \"=== KLN nightmare ===\"; grep -n \"^nightmare,\" KLN_1966.txt\necho \"=== KLN mortal ===\"; grep -n \"^mortal,\" KLN_1966.txt\necho \"=== KLN marasmus/marcescent ===\"; grep -n \"^marasmus,\\|^marcescent,\" KLN_1966.txt"
}
```


### [2026-09-07T16:17:47.981Z] TOOL RESULT

```
=== KLN marble ===
=== KLN murder ===
24687:murder,  n.  —  ME.  mordre,  morder,  morthre,  fr.
=== KLN nightmare ===
=== KLN mortal ===
24447:mortal,  adj.  —  ME.,  fr.  MF.  mortal,  mortel  (F. mor  tel),  fr.  L.  mortalis,  ‘mortal’,  fr.  mors,  gen. mortis,  ‘death’,  from  the  stem  of  morior,  mori,'  to die’;  which  is  cogn.  with  OI.  mrtih,  ‘death’, mriyate,  marati,  marate,  Avestic  miryeite,  ‘dies’, OI.  mart  ah,  ‘mortal,  man’,  Avestic  mereti-, Lith.  mirt'is,  OSlav.  sumriti,  of  s.m. ;  OI.  mrtdh, Avestic  mlreta-,  ‘dead’.  Arm.  mard,  ‘man’  (lit. •mortal'),  Gk.  (BpoToq  (for  *|xjipoToc),  ‘mortal’ (for  the  original  form  cp.  Gk.  afxfJpoTo;,  ‘im¬ mortal’),  OSlav.  mrutvii,  ‘dead’,  OSlav.  miro, mreti,  ‘to  die’,  umr&tije,  ‘death’,  Lith.  mirstu, mirti ,  ‘to  die’,  maras,  Lett,  meris,  ‘pestilence’, OIr.  marb,  W.,  Co.  marw,  ‘died’  (pp.),  OE. morp,  ‘murder’.  All  these  words  derive  fr.  I.-E. base  *mer-,  ‘to  die’,  which  is  orig.  identical  with base  *mer-,  ‘to  consume,  be  consumed’.  See morbid,  mordant  and  cp.  mort,  mortgage,  mor¬ tician,  mortify,  mortuary,  amortize,  immortal, immortelle,  ambrosia,  amrita,  smorzando.  Cp. also  murder,  murrain.
=== KLN marasmus/marcescent ===
22887:marasmus,  n.,  wasting  away  of  the  body.  — ModL.,  fr.  Gk.  papacrpog,  ‘consumption’,  fr. papoavciv,  ‘to  consume’,  fr.  I.-E.  base  *mer-,  ‘to rub,  consume,  wear  away’.  See  mar  and  cp. amaranth.
22896:marcescent,  adj.,  withering.  —  L.  marcescens, gen.  -entis,  pres.  part,  of  marcescere,  ‘to  wither, droop,  decay,  pine  away’,  inchoative  of  marcere, ‘to  wither,  droop,  be  faint’,  fr.  I.-E.  base  *mereq-, *merq-,  ‘to  decay,  rot’,  whence  also  Lith.  merkiu, merkti,  ‘to  soak,  steep’,  mirkstii,  mifkti,  ‘to  be soaked,  be  steeped’,  and  perh.  Gaul,  brads,  ‘a kind  of  com  used  for  making  malt’,  Mir. mraich,  braich,  W.  brack,  ‘malt’,  MIr.  bren,  W. braen  (for  * mrakno-),  ‘foul,  rotten’.  Cp.  im- marcessible.  I.-E.  base  *mereq-,  *merq-,  ‘to decay,  rot’,  is  orig.  identical  with  base  *merq-, ‘to  rub’,  enlargement  of  base  *mer-,  whence  OI. mrnati,  ‘crushes,  bruises’,  Gk.  papaivEiv,  ‘to put  out,  quench,  extinguish’.  See  smart,  v.  and cp.  marasmus,  amaranth,  marble.  Cp.  also  mar. For  the  ending  of  marcescent  see  suff.  -ent. march,  n.,  boundary.  —  ME.  marche,  fr.  OF. (=  F.)  marche,  ‘boundary,  frontier’,  fr.  Frank¬ ish  *marka,  which  is  rel.  to  OHG.  marca, marcha,  MHG.  marke,  G.  Mark,  ‘boundary, frontier’.  It.,  OProven?.,  Sp.  marca,  of  s.m.,  are also  Teut.  loan  words.  Sec  mark,  ‘boundary; sign',  and  cp.  marchioness,  marquis.
```


## [2026-09-07T16:18:02.503Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find leaf containing 'mortal, adj.' and 'murder, n.' and 'marble'\nfor pat in ['mortal,  adj.','murder,  n.','marble','nightmare','marmoreal','mar,  v']:\n    for i,l in enumerate(leaves):\n        if pat in l:\n            print(pat,'-> leaf',i)\n            break\n    else: print(pat,'NOT FOUND')\nEOF"
}
```


### [2026-09-07T16:18:03.866Z] TOOL RESULT

```
mortal,  adj. -> leaf 416
murder,  n. -> leaf 544
marble -> leaf 34
nightmare -> leaf 288
marmoreal -> leaf 503
mar,  v NOT FOUND
```


## [2026-09-07T16:18:15.580Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor i in [415,416,417,502,503,543,544]:\n    l=leaves[i]\n    head=' | '.join(x.strip() for x in l.split('\\n')[:6] if x.strip())\n    print(i,'::',head[:300])\nEOF"
}
```


### [2026-09-07T16:18:16.964Z] TOOL RESULT

```
nleaves 903
415 :: native’, fr.  L.  imaginatus,  pp.  of  imaginari.  See  next  word and  -ive. | Derivatives:  imaginative-ly,  adv.,  imaginative¬ ness,  n. | imagine,  tr.  and  intr.  v.  —  ME.,  fr.  MF.  (=F.) imaginer,  fr.  L.  imaginari,  ‘to  picture  to  oneself, imagine’,  fr.  imago,  gen.  -inis;  see
416 :: ,  fr.  L.  immobilis,  ‘immov¬ able’,  fr.  in-,  ‘not’,  and  mobilis,  ‘movable’.  See mobile. | immobility,  n.  —  F.  immobility,  fr.  L.  immobili- tatem,  acc.  of  immobilitas,  ‘immovableness’,  fr. immobilis.  See  prec.  word  and  -ity. immobilize,  tr.  v.  —  F.  immobiliser,  fr.  L
417 :: t word  with  suff.  -ce,  resp.  -cy. impendent,  adj.,  impending.  —  L.  impendens,  gen. -entis,  pres.  part,  of  impendere,  ‘to  hang  over’. See  impend  and  -ent. | impenetrable,  adj.  —  ME.  impenetrabel,  fr.  MF. (=  F.)  impenetrable,  fr.  L.  impenetrable,  ‘that cannot  be  pene
502 :: late,  tr.  v.  —  Back  formation  fr.  manipul¬ ation. | Derivatives:  manipulat-or,  n.,  manipulat-ory, adj. | manipulation,  n.  —  F.,  fr.  manipule.  See  maniple and  -ation. | manito,  manitou,  n.,  a  nature  spirit.  —  Algonqui- an,  lit.  ‘spirit,  god’. | •mankind,  n.  —  ME.;  comp
503 :: anx  cat. | many,  adj.  and  n.  —  ME.  mani,  moni,  meni,  fr. OE.  manig,  monig,  mxnig,  rel.  to  OS.  manag. Late  ON.  mangr,  Dan.  mangen,  Swed.  mangen, OFris.  manich,  menich,  MDu.  menich,  Du. menig,  OHG.  manag,  MHG.  manec,  G.  munch, Goth,  manags,  ‘many  a,  many’,  and  c
543 :: ng  see  suff.  -ity. mull,  tr.  v.,  1)  to  powder  (dial.  English) ;  to  muddle (dial.  English).  —  ME.  mullen,  ‘to  grind',  fr.  ME. mul,  mol,  ‘dust’,  fr.  OE.  myl,  ‘dust’,  which  is  rel. to  Swed.  mull,  MLG.,  MDu.,  Du.  mul,  ‘loose earth’,  G.  Mull,  ‘garbage’;  fr.  I.-E. 
544 :: like  a  mummy,  to  dry  up,  shrivel.  — F.  momifier,  compounded  of  momie,  ‘mummy’, and  -fier,  ‘to  make  into’,  fr.  L.  -  fiedre,  fr. facere,  ‘to  make,  do’.  See  mummy  and  -fy. mummy,  n.,  an  embalmed  body.  —  ME.  mummie, fr.  OF.  (=  F.)  momie,  fr.  ML.  mumia,  fr.  Ara
```


## [2026-09-07T16:18:26.936Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# leaf index per line\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in [24447,24687,22887,22896]:\n    print(ln,'leaf',m[ln],'approx printed page',(m[ln]-12)*2)\nleaves=t.split('\\f')\nfor i in [513,514,515]:\n    print('---- leaf',i, ' first heads:')\n    hs=[x.strip()[:60] for x in leaves[i].split('\\n')[:4]]\n    print(' | '.join(hs))\nEOF\necho \"=== marble entry ===\"; grep -n \"marble\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T16:18:28.352Z] TOOL RESULT

```
24447 leaf 539 approx printed page 1054
24687 leaf 544 approx printed page 1064
22887 leaf 503 approx printed page 982
22896 leaf 503 approx printed page 982
---- leaf 513  first heads:
gen.  -onis, ‘healing,  cure’,  fr.  medicatus,  pp.  of  me | Derivatives:  medicine,  tr.  v.,  medicin-al,  adj. and  n. | medico-,  combining  form  meaning  1)  ‘medical, medicinal’ | medieval,  mediaeval,  adj.,  pertaining  to,  or  sug¬ gest
---- leaf 514  first heads:
at’  (in  physics  it  is  used  in  the meaning  of  ‘a  mi | —  Compounded  of  mega-  and  Gk.  xeqpaXir), ‘head’.  See  | Megaceros,  n.,  a  genus  of  mammals  of  the  deer family | Megachile,  n.,  a  genus  of  bees  (zool.)  —  ModL., comp
---- leaf 515  first heads:
elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  re | Derivative:  meld,  n.,  the  act  of  melding, meld,  tr.   | meldometer,  n.,  an  instrument  for  measuring melting  po | marya,  of  s.m.  The  Greek  word  was  prob.  in¬ fluenced
=== marble entry ===
2077:L.  alabaster,  fr.  Gk.  aXafiaaxpop,  aXxfjaaxpov, fr.  earlier  dXdpaaxop,  fr.  Egypt  *a-la-baste, ‘vessel  of  the  goddess  Ebaste  (—  Bubaste).  See Frisk,  GEW.,  p.62  s.v.  dXdfixaxoc;.  Cp.  alley ‘choice  marble’.
2270:Derivative:  alley-ed,  adj. alley,  n.,  a  choice  marble.  —  Abbreviation  of alabaster;  so  called  because  it  was  orig.  made of  alabaster.
2932:anthraconite,  n.,  a  coal-black  marble  of  limestone (mineral.)  —  Formed  with  subst.  suff.  -ite  fr. Gk.  dvhpxli,  ‘coal’,  and  xovla,  ‘dust,  ashes; lye,  soap  powder;  lime’.  For  the  first  element see  anthrax.  Gk.  xovia  derives  fr.  xovtp,  ‘dust’, which  is  cogn.  with  L.  cinis,  ‘ashes’;  see  cine¬ rary.
5587:Derivatives:  breath-ed,  adj.,  breath-er,  n., breath-ing,  verbal  n.  and  pres.  part, breba,  n.,  fig  of  the  first  crop.  —  Sp.  breva,  meta¬ thesis  of  bevra,  of  s.m.,  fr.  L.  bifera,  fern,  of bifer,  ‘bearing  fruit  twice  a  year’,  which  is  com¬ pounded  of  bis,  ‘twice’,  and  ferre,  ‘to  bear, carry’.  See  bi-  and  bear,  ‘to  carry’, breccia,  n.,  a  rock  composed  of  angular  piece* (petrogr.)  —  It.,  ‘a  kind  of  marble  consisting  of angular  pieces’,  fr.  OHG.  brecha,  ‘a  breaking’, whence  also  F.  breche.  See  breach.
7699:Cinq  Ports,  a  group  of  towns  (orig.  five)  on  the southeast  coast  of  England.  —  F.,  ‘five  (sea) ports’.  See  cinq(ue)  and  port,  ‘harbor’, cinter,  cintre,  n.,  the  centering  of  an  arch  or bridge.  —  F.  cintre,  ‘curve,  bend’,  fr.  cintrer,  ‘to curve,  bend’,  fr.  VL.  *cincturare,  fr.  L.  cinctura, ‘cincture,  girdle’,  fr.  cinctus,  pp.  of  cingere,  ‘to gird’.  See  cincture  andcp.  words  there  referred  to. cion,  n.,  the  uvula.  —  Gk.  xtcov,  ‘pillar;  uvula’, cogn.  with  Arm.  siun,  ‘pillar’, cipher,  n.  —  ME.  cyphre,  fr.  OF.  cifre,  ‘zero’,  fr. Sp.  cifra,  fr.  Arab,  sifr,  ‘empty;  zero’  (fr.  safara, ‘was  empty’),  which  is  a  loan  translation  of  OI. sunyah,  ‘empty;  cipher  with  no  real  value;  zero’ (F.  chiffre,  ‘cipher’,  derives  fr.  It.  cifra,  of  s.m., fr.  ML.  cifra,  which  is  also  borrowed  fr.  Arab. sifr).  Cp.  MHG.  cifre,  ‘zero’  (whence  G.  Ziffer, ‘cipher’),  which  derives  fr.  OF.  cifre.  Cp.  deci¬ pher.  Cp.  also  zero,  which  is  a  doublet  of  cipher. Derivatives:  cipher,  tr.  and  intr.  v.,  cipher-er,  n. cipolin,  n.,  a  green  Italian  marble.  —  F.,  fr.  It. cipollino,  ‘a  little  onion’,  dimin.  formed  fr.  ci- polla,  ‘onion’,  fr.  L.  caepulla,  dimin.  of  caepa, cepa,  ‘onion’;  so  called  because  the  foliated form  of  this  marble  resembles  the  coats  of  an onion.  See  cibol  and  cp.  chive, cippus,  n.,  post,  inscribed  column  used  as  a  land¬ mark  (Roman  antiq.)  —  L.,  ‘post,  stake,  pillar, gravestone,  boundary  stone,  landmark’,  of  un¬ certain  origin.  It  is  possibly  rel.  to  L.  scipid, ‘staff,  and  cogn.  with  Gk.  crxEmov,  ‘staff, stick’,  ON.  skifa ,  OS.  skiDa,  etc.,  ‘disk,  slice’. See  sheave,  n.
```


## [2026-09-07T16:18:45.960Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[515][:4000])\nEOF"
}
```


### [2026-09-07T16:18:47.238Z] TOOL RESULT

```
elden,  ‘to  announce’,  fr. MHG.  melden,  ‘to  betray,  report’,  fr.  OHG. meldon,  of  s.m.,  which  is  rel.  to  OS.  meldon,  of s.m.,  OE.  meldian,  ‘to  declare,  tell,  display,  pro¬ claim',  OE.  meld,  ‘proclamation*,  Du.  melden, ‘to  report;  to  mention’,  and  perhaps  cogn.  with Lith.  meldiiu,  melsti,  ‘to  request,  pray'.  Arm. malt'em.  T  beg,  request’,  Hitt,  maid-,  ‘to  tell, pray’.
Derivative:  meld,  n.,  the  act  of  melding, meld,  tr.  and  intr.  v.,  to  blend.  —  A  blend  of melt  and  weld.
meldometer,  n.,  an  instrument  for  measuring melting  poinis.  —  Compounded  of  Gk.  |xeXoei.v, ‘to  melt",  and  fr£rpov,  ‘measure’.  See  meal, ‘edible  grain',  and  meter,  ‘poetical  rhythm’. Meleagris,  n.,  the  genus  of  turkeys  (ornithol.)  — ModL.,  fr.  L.  meleagris,  ‘guinea  hen’,  fr.  Gk. peXeaypii;,  which  is  of  uncertain  origin.  It  is perh.  cogn.  with  Avestic  mlr*ga,  ‘bird’,  Afghan
marya,  of  s.m.  The  Greek  word  was  prob.  in¬ fluenced  in  form  by  the  name  of  the  Greek  hero MsX£aYpoc,  Meleagrus,  son  of  Oeneus,  king  of Calydon.
melee,  mel6e,  n.,  conflict,  fray,  skirmish.  —  F. melee,  prop.  fem.  pp.  of  meler,  ‘to  mix,  mingle’. See  medley  and  cp.  melange, meli-,  combining  form  meaning  ‘honey’.  —  Gk. ptsXi-,  fr.  piXi,  gen.  [xeXito?,  ‘honey’,  which is  cogn.  with  L.  mel,  gen.  mellis,  ‘honey’.  See mel.
Melia,  n.,  a  genus  of  trees  (bot.)  ■ —  ModL.,  fr. Gk.  [zsXia,  ‘ash  tree’,  which  is  of  unknown origin.
Melianthaceae,  n.  pi.,  a  family  of  S.  African plants  (bot.)  —  ModL.,  formed  from  next  word with  suff.  -aceae.
Melianthus,  n.,  a  genus  of  S.  African  plants  (bot.)
—  ModL.,  compounded  of  Gk.  fi£Xi,  ‘honey’, and  Svfloi;,  "flower’.  See  meli-  and  anther.
melic,  adj.,  pertaining  to  song.  —  Gk.  |zeXuc6?, ‘of  a  song’,  fr.  ptiXoi;,  ‘limb,  joint ;  part  of  musi¬ cal  phrase;  song,  tune’,  which  is  perh.  cogn. with  Bret,  meli,  Co.  mal,  ‘knuckle,  joint’,  W. cym-mal,  ‘joint’,  and  with  Toch.  A  rndlk-,  ‘to join,  unite’.  Cp.  the  first  element  in  melisma, melodrama,  melody,  and  the  second  element  in philomel,  dulcimer.  For  the  ending  see  adj.  suff. -ic.  For  the  sense  development  of  Gk.  u£Xoi ; cp.  Ir.  alt,  ‘limb;  poem’.
Melica,  n.,  a  genus  of  grasses  (bot.)  —  ModL.,  fr. It.  melica,  meliga,  melga,  ‘sorghum’,  which prob.  comes  fr.  ML.  milica,  a  derivative  of  L. milium,  ‘millet’.  See  millet.
Melicent,  fem.  PN.  —  See  Milicent. meliceris,  also  melicera,  n.,  a  kind  of  tumor  (med.)
—  L.  meliceris,  fr.  Gk.  pisXixTjpii;,  ‘a  tumor looking  like  honeycomb’,  compounded  of  piXt, ‘honey’,  and  xz)p<k,  ‘beeswax’.  See  meli-  and cere.
melilot,  n.,  a  kind  of  clover.  —  ME.  mellilot,  fr. MF.  (=  F.)  melilot,  fr.  L.  melilotos,  ‘a  kind  of clover’,  fr.  Gk.  p.eXiXaiTO?,  peXtXtOTOV,  which is  compounded  of  piXt,  ‘honey’,  and  Xo>t6;, ‘lotus’.  See  meli-  and  lotus.
Melilotus,  n.,  a  genus  of  plants,  the  sweet  clover (bot.)  —  L.  melilotos.  See  melilot. melinite,  n.,  a  high  explosive  containing  chiefly picric  acid.  —  F.  melinite,  formed  with  subst. suff.  -ite.  fr.  Gk.  pTjXivop,  ‘pertaining  to  an apple’,  fr.  p,?)Xov,  ‘apple’.  See  Maius,  ‘the  genus of  apple  trees’,  and  cp.  the  second  element  in marmalade  and  in  camomile, meliorability,  n.,  the  capability  of  being  improv¬ ed.  —  Coined  by  the  English  philosopher  Jeremy Bemnam  (1748-1832)  fr.  L.  melior,  ‘better’. See  meliorate  and  the  suffixes  -able  and  -ity. meliorate,  tr.  and  intr.  v.  —  Late  L.  melioratus, pp.  of  meliorare.  ‘to  make  better,  improve’,  fr. melior,  ‘better’,  prob.  with  the  original  meaning ‘stronger’,  fr.  I.-E.  base  *mel-,  ‘strong,  great, numerous’,  whence  also  Gk.  paXa,  ‘very,  very
meliorism
```


## [2026-09-07T16:19:15.671Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ndef find(pat):\n    out=[]\n    for i,l in enumerate(leaves):\n        for m in re.finditer(pat,l):\n            out.append((i, l[max(0,m.start()-80):m.start()+700].replace('\\n',' ')))\n    return out\nfor pat in [r'nightmare,\\s+n',r'\\bmare,\\s+n',r'marble,\\s+n',r'marmoreal',r'murder,\\s+n']:\n    print('########',pat)\n    for i,s in find(pat)[:3]:\n        print('[leaf %d ~p.%d]'%(i,2*(i-12)), s[:800])\n        print('---')\nEOF"
}
```


### [2026-09-07T16:19:17.750Z] TOOL RESULT

```
######## nightmare,\s+n
[leaf 560 ~p.1096]  every  night. —  ME.,  fr.  nihtlich,  adj. See  night  and  adv.  suff.  -ly. nightmare,  n.,  1)  an  incubus;  2)  a  frightening dream.  —  Compounded  of  night  and  mare,  ‘in¬ cubus’. Derivatives:  nightmare,  tr.  v.,  nightmar-ish,  adj., nightmar-ish-ly,  adv.,  nightmar-y,  adj. nightshade,  n.,  any  of  various  poisonous  plants  of the  genus  Solanum;  the  belladonna.  —  ME. nighteschede,  fr.  OE.  nihtscada,  lit.  ‘shade  of night’  (see  night  and  shade) ;  so  called  in  allusion to  its  narcotic  or  poisonous  qualities.  Cp.  Du. nachtschade,  G.  Nachtschatten,  ‘nightshade’, nighty,  n.,  a  nightgown  or  nightshirt  (colloq.)  — -  Formed  fr.  night  with  dimin.  suff.  -y. nigrescence,  n.,  1)  process  of  becoming  black;  2) bl
---
######## \bmare,\s+n
[leaf 504 ~p.984]  Mars,  name  of  the  Roman  god  of  war. See  Mars  and  cp.  Marcia,  Mark, mare,  n.,  a  female  horse.  —  ME.  mere ,  mare,  fr. OE.  mere,  fem.  to  OE.  mearh,  ‘horse’;  rel.  to OS.  meriha,  ON.  merr,  OFris.  merrie,  MDu. merie,  Du.  merrie,  OHG.  meriha,  merha,  MHG. merhe,  G.  Mahre,  ‘mare’,  ON.  marr,  OFris. mar,  OHG.  mar  ah,  marh,  ‘horse’,  from  pre- Teut.  marka,  a  form  mentioned  in  Pausanias Periplous  and  referred  to  as  of  Gaulish  origin. Cp.  Ir.  and  Gael,  marc,  W.  march,  Co.  margh, march,  Bret,  marh,  ‘horse’.  Cp.  also  the  first element  in  marshal. mare,  n.,  the  sea.  —  L.  mare,  ‘sea’.  See  mere, ‘lake’. mare,  n.,  incubus.  —  ME.,  fr.  OE.,  rel.  to  ON.  and OHG.  mara,  MDu.  mare,  Du.  -me
---
[leaf 504 ~p.984] gh, march,  Bret,  marh,  ‘horse’.  Cp.  also  the  first element  in  marshal. mare,  n.,  the  sea.  —  L.  mare,  ‘sea’.  See  mere, ‘lake’. mare,  n.,  incubus.  —  ME.,  fr.  OE.,  rel.  to  ON.  and OHG.  mara,  MDu.  mare,  Du.  -merrie,  MHG. mar,  G.  Mahr,  ‘incubus’,  and  cogn.  with  the  first element  in  OIr.  Mor-rigain,  demoness  of  corpses (lit.  ‘queen  of  the  nightmare’),  Bulg.,  Serb.,  Pol. mora,  Czech  mura,  ‘incubus’.  Cp.  the  second element  in  nightmare.  Cp.  also  the  second  ele¬ ment  in  cauchemar. maremma,  n.,  marshy  land  near  the  seashore. It.,  fr.  L.  maritima,  neut.  pi.  of  maritimus,  ‘per¬ taining  to  the  sea,  near  the  sea’,  fr.  mare,  ‘sea’. Cp.  OF.  maresme,  Catal.  maresma,  ‘marsh’, which  are  of 
---
[leaf 504 ~p.984] t  in  marshal. mare,  n.,  the  sea.  —  L.  mare,  ‘sea’.  See  mere, ‘lake’. mare,  n.,  incubus.  —  ME.,  fr.  OE.,  rel.  to  ON.  and OHG.  mara,  MDu.  mare,  Du.  -merrie,  MHG. mar,  G.  Mahr,  ‘incubus’,  and  cogn.  with  the  first element  in  OIr.  Mor-rigain,  demoness  of  corpses (lit.  ‘queen  of  the  nightmare’),  Bulg.,  Serb.,  Pol. mora,  Czech  mura,  ‘incubus’.  Cp.  the  second element  in  nightmare.  Cp.  also  the  second  ele¬ ment  in  cauchemar. maremma,  n.,  marshy  land  near  the  seashore. It.,  fr.  L.  maritima,  neut.  pi.  of  maritimus,  ‘per¬ taining  to  the  sea,  near  the  sea’,  fr.  mare,  ‘sea’. Cp.  OF.  maresme,  Catal.  maresma,  ‘marsh’, which  are  of  the  same  origin,  and  see  maritime. Margaret,  fem.  PN.  —
---
######## marble,\s+n
[leaf 503 ~p.982] .  Hence  maravedi  prop,  meant ‘money  of  the  Almoravides’.  See  Marabout, marble,  n.  —  ME.  marbre,  later  changed  to marbel,  marble,  fr.  OF.  (=  F.)  marbre,  fr.  VL. marmorem,  acc.  of  L.  marmor  (a  neut.  noun, taken  in  VL.  for  masc.),  fr.  Gk.  pdcppapo;, ‘white,  glistening  stone’,  fr.  orig.  ‘stone,  rock’, rel.  to  papvapai,  ‘I  fight,  battle’,  lit.  T  strike myself’,  papaivoi,  ‘I  put  out,  quench,  extin¬ guish’,  and  cogn.  with  OI.  mrnati,  ‘crushes, bruises’,  fr.  I.-E.  bSse  *mer-,  ‘to  rub,  consume, wear  away’.  See  smart,  v.,  and  cp.  marmoreal. Cp.  also  marasmus,  amaranth.  The  sense  de¬ velopment  of  Gk.  pappapoi;  was  influenced  by pappatpeiv,  ‘to  shine’,  to  which,  however,  it  is not  rela
---
######## marmoreal
[leaf 503 ~p.982] E.  bSse  *mer-,  ‘to  rub,  consume, wear  away’.  See  smart,  v.,  and  cp.  marmoreal. Cp.  also  marasmus,  amaranth.  The  sense  de¬ velopment  of  Gk.  pappapoi;  was  influenced  by pappatpeiv,  ‘to  shine’,  to  which,  however,  it  is not  related.  OHG.  marmul,  murmul,  G.  Marmel, Murmel,  ‘marble’,  are  Latin  loan  words.  G. Marmor,  ‘marble’,  has  been  refashioned  after  L. marmor. Derivatives:  marbl-ed,  marbl-y,  adjs. marc,  n.,  refuse  of  fruit,  esp.  of  grapes.  —  F.,  lit. ‘something  trodden  or  beaten’,  fr.  marcher,  ‘to walk’,  in  the  original  sense  of  this  verb:  ‘to tread’.  Sec  march,  ‘to  walk’, marcasite,  n.,  a  native  iron  disulfide  FeSa  (min¬ eral.)  —  F.  marcassite,  fr.  ML.  marchasita,  fr. Sp.  marcax
---
[leaf 505 ~p.986] us,  ‘pure,  unmixed’. See  mere,  adj.  For  the  second  element  see  -lite. marmoreal,  adj.,  pertaining  to,  or  like,  marble. Formed  with  adj.  suff.  -al  fr.  L.  marmoreus, ‘made  of  marble,  resembling  marble’,  fr.  mar- mor,  ‘marble’.  See  marble. Derivative:  marmoreal-ly,  adv. marmoset,  n.,  a  small  monkey  of  South  and  Cen¬ tral  America.  —  ME.  marmusette,  fr.  MF. marmouset,  ‘grotesque  carved  figure'  [cp.  Rue des  Marmousets,  a  street  in  Paris,  in  which  there were  grotesque  figures  of  stone.  Referring  to this  street,  a  Latin  text  from  1280  speaks  of  duo marmoseti  lapidei  [‘two  stone  marmosets’  = two  grotesque  figures  of  stone’];  rel.  to  F. marmot.  Tittle  monkey;  puppet,  grotesque  fig¬ ure’, 
---
[leaf 505 ~p.986] le,  resembling  marble’,  fr.  mar- mor,  ‘marble’.  See  marble. Derivative:  marmoreal-ly,  adv. marmoset,  n.,  a  small  monkey  of  South  and  Cen¬ tral  America.  —  ME.  marmusette,  fr.  MF. marmouset,  ‘grotesque  carved  figure'  [cp.  Rue des  Marmousets,  a  street  in  Paris,  in  which  there were  grotesque  figures  of  stone.  Referring  to this  street,  a  Latin  text  from  1280  speaks  of  duo marmoseti  lapidei  [‘two  stone  marmosets’  = two  grotesque  figures  of  stone’];  rel.  to  F. marmot.  Tittle  monkey;  puppet,  grotesque  fig¬ ure’,  marmotter,  ‘to  mutter,  mumble'.  All  these words  are  prob.  of  imitative  origin.  Cp.  marmot, marmot,  n.,  a  burrowing  rodent.  —  F.  marmotte, prop,  ‘the  mumbling  (animal)',  fr.  marm
---
######## murder,\s+n
[leaf 544 ~p.1064] uromontite,  extramural,  in¬ tramural,  immure.  Cp.  also  mere,  ‘boundary’. murder,  n.  —  ME.  mordre,  morder,  morthre,  fr. murder 1016 1017 music OE.  mordor,  mordur ,  rel.  to  Goth,  maiirpr,  ‘mur¬ der’,  OE.  mord,  OS.,  OFris.  morth,  ON.  mord, Dan.,  Swed.  mord,  MDu,  moort,  mort,  Du. moord ,  OHG.  mord,  MHG.  mort,  G.  Mord, ‘murder’,  and  cogn.  with  L.  mors,  gen.  mortis, ‘death’,  mort,  ‘to  die’.  See  mortal. Derivatives:  murder,  v.  (q.v.),  murder-ous  (q.v.) murder,  tr.  v.  —  ME.  mortheren,  murtheren,  fr. OE.  myrddrian,  ‘to  murder’,  fr.  OE.  mordor, ‘murder’;  rel.  to  OF.  morthia,  OHG.  murthiren, Goth,  maiirprjan,  ‘to  murder’.  See  murder,  n. Derivatives:  murder-er,  n.,  murder-ess,  n. murderous,  adj. 
---
[leaf 544 ~p.1064] l.  to  OF.  morthia,  OHG.  murthiren, Goth,  maiirprjan,  ‘to  murder’.  See  murder,  n. Derivatives:  murder-er,  n.,  murder-ess,  n. murderous,  adj.  —  A  hybrid  coined  fr.  murder,  a word  of  Teut.  origin,  and  -ous,  a  suff.  traceable to  L.  -dsus. Derivatives:  murderous-ly,  adv.,  murderous-ness, n. mure,  tr.  v.,  to  enclose  within  walls,  immure.  — ME.  muren,  fr.  OF.  (=  F.)  murer,  fr.  L.  murare, ‘to  enclose  within  walls’,  fr.  murus.  See  mural. Murex,  n.,  a  genus  of  marine  gastropods  (zoo/.) —  L.  murex,  ‘purple  fish,  purple  dye’,  of  uncer¬ tain,  possibly  Mediterranean,  origin. muriate,  n.,  a  salt  of  hydrochloric  acid  ( chem .) —  See  next  word. muriatic,  adj., hydrochloric  (scil.  acid).  —  Coined
---
```


## [2026-09-07T16:19:28.342Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in [503,504,505,538,539,540,560]:\n    m=re.findall(r'[a-z]+ +1?\\d{3} +1?\\d{3} +[a-z]+', leaves[i])\n    m2=re.findall(r'\\b\\d{3,4}\\b', leaves[i])\n    print(i, 'hdr:',m[:3], 'nums:',m2[:12])\nprint('=== leaf 538/539 mortal context ===')\nfor i in (538,539):\n    idx=leaves[i].find('mortal')\n    print(i, leaves[i][:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T16:19:29.646Z] TOOL RESULT

```
503 hdr: [] nums: ['113', '1311', '311', '937', '1500', '1571', '385', '490', '1936', '938', '939']
504 hdr: [] nums: ['1678', '1874', '1786', '1889', '1569', '1625']
505 hdr: [] nums: ['940', '941', '1280', '1062']
538 hdr: [] nums: ['1837', '1913', '1786', '1889', '1837', '1805', '1844', '1830', '1004', '1005', '1707', '635']
539 hdr: [] nums: ['1817', '1791', '1872', '1834', '1919', '1006', '1007', '1797', '1858', '1859', '1920']
540 hdr: [] nums: ['1008', '1009']
560 hdr: [] nums: ['844', '1900', '1860', '1917', '1743', '1819', '1776', '1848', '1862', '1860', '1917']
=== leaf 538/539 mortal context ===
538 rt,  of  mordre,  ‘to  bite’,  fr.  VL.  "mordere (whence  also  It.  mordere,  OProveng.,  Sp., Port,  mordre),  fr.  L.  mordeo,  mordere,  ‘to  bite’, which  stands  for  *(s)mordeyo  and  is  cogn
539 he  family  Nymphalidae  ( entomol .)  — ModL.,  fr.  Gk.  Mopipci.  See  prec.  word, morpho-,  before  a  vowel  morph-,  combining  form meaning  ‘form,  shape’.  —  Gk.  p-opipo-,  [iopip-, fr.  [
```


## [2026-09-07T16:19:36.312Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ns=leaves[538]\nprint(len(s))\nprint(s[:3500])\nEOF"
}
```


### [2026-09-07T16:19:37.653Z] TOOL RESULT

```
11979
rt,  of  mordre,  ‘to  bite’,  fr.  VL.  "mordere (whence  also  It.  mordere,  OProveng.,  Sp., Port,  mordre),  fr.  L.  mordeo,  mordere,  ‘to  bite’, which  stands  for  *(s)mordeyo  and  is  cogn.  with OI.  mardayati,  mdrdati,  ‘rubs,  crushes’,  mfdnati, ‘presses,  rubs’,  Gk.  op.ep§v6g,  ofzepSccXsog,  ter¬ rible,  fearful’,  lit.  ‘rubbing,  crushing’,  OE. smeortan,  OHG.  smerzan,  ‘to  pain  ,  orig.  to bite’.  All  these  words  derive  fr.  I.-E.  base *(s)merd-,  a  -d-enlargement  of  base  *mer-,  ‘to rub,  pound,  consume,  wear  away,  exhaust, worry;  to  be  consumed’.  See  smart,  v.  and  cp. morbid,  morceau,  mordacious,  mordent,  morse, ‘a  brooch’,  morsel,  premorse,  remorse.  For  the ending  see  sulf.  -ant.
Derivatives:  mordant,  n.,  mordant-ly,  adv. Mordecai,  masc.  PN. ;  in  the  Bible,  the  cousin  of Esther,  who  saved  the  Jews  from  the  extermina¬ tion  planned  by  Haman.  —  Fleb.  Mortfkhay, spelled  also  Mordokhay,  fr.  Akkad.  Marduk (whence  Heb.  M^rodhakh,  name  of  the  chief god  of  the  city  of  Babylon,  whence  also  the Babylonian  PN’s  Mardukea,  Marduka. mordenite,  n.,  a  zeolite  (mineral.)  —  Named  after Morden  in  Nova  Scotia.  For  the  ending  see subst.  suff.  -ite.
mordent,  n.,  an  ornament  of  three  tones,  a  trill (mus.)  —  G.,  fr.  It.  mordente,  lit.  ‘biting’,  pres, part,  of  mordere,  fr.  VL.  "mordere,  correspond¬ ing  to  Classical  L.  mordere,  ‘to  bite’.  See  mor¬ dant  and  -ent.
more,  adj.  —  ME.  more,  fr.  OE.  mara,  ‘larger, greater,  more'  (used  as  compar.  of  mice),  ‘large, great,  much’) ;  rel.  to  OE.  ma,  ‘more’  (neut.  and adv.),  OS.  mera,  adj.,  mer,  adv.,  ON.  meiri,  adj., meirr,  meir,  adv.,  OFris.  mara,  mera,  adj.,  ma, me  (also  mar,  mer),  adv.,  MDu.  mere,  metre, adj.  and  adv.,  mee,  adv.,  Du.  meer,  adv.,  OHG. mero,  adj.,  mer,  adv.,  MHG.  mere,  adj.,  mer, adv.,  G.  mehr,  adj.  and  adv.  (cp.  the  adjectives with  double  compar.  suff.  Du.  meerder,  ‘more, greater’,  OHG.  meroro,  meriro,  ‘greater’,  MHG. merer,  metre,  G.  mehrere,  ‘several’),  Goth. maiza,  adj.,  mais,  adv.,  OE.  mSre,  OHG.  mari, ‘great,  glorious,  famous’,  and  cogn.  with  Aves- tic  mazjd,  ‘greater’,  OIr.  mor,  mar,  ‘great’,  mdu, mo,  ‘more’,  Homeric  Gk.  ^yxsof-ptopo?,  ‘great with  the  £yx°$  >  i-e-  ‘great  with  the  spear’.  Os- can  mais,  ‘more’.  Cp.  most.
Derivatives:  more,  n.  and  adv.
moreen,  n.,  a  coarse  fabric  of  wool  or  of  wool  and cotton.  —  Prob.  formed  fr.  moire  with  suff. -een.
morel,  n.,  an  edible  fungus.  —  F.  morille,  of  Teut. origin.  Cp.  OHG.  morhila ,  morhala  (MHG. morhel,  morchel,  G.  Morchel),  ‘morel  ,  dimin.  of moraha,  morha  (MHG.,  morhe,  morhe,  G. Mohre),  ‘carrot’,  which  is  rel.  to  OS.  morha, MLG.  more,  OE.  moru,  more,  ‘carrot’,  obsol.
E.  more,  ‘root’,  and  possibly  cogn.  with  Gk. (ra)  ppctxava,  ‘wild  herbs’,  OSlav.  mrkvy, ‘carrots’,  Russ,  morkov’,  Serb,  mrkva,  etc., ‘carrot’.  Cp.  Morchella.
morel,  n.,  the  black  nightshade.  —  F.  morelle,  fr. VL.  * maurella ,  fern,  of  * maurellus  ‘dark- colored’,  diminutive  formed  fr.  L.Maurus,  ‘inha¬ bitant  of  Mauretania’.  See  Moor  and  cp.  next word.  Cp.  also  OF.,  OProveng.  morel,  F. moreau,  ‘jet-black  horse’, morello,  n.,  a  bitter  variety  of  cherry.  —  It.,  fr. VL.  * maurellus ,  dimin.  of  L
```


## [2026-09-07T16:20:01.584Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/ref_page.py; echo ...; ls data/verification/sources/refs/ocr/ | head -30"
}
```


### [2026-09-07T16:20:01.631Z] TOOL RESULT

```
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
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
...
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-07T16:20:04.701Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT grep mahrka ===\"; grep -n -i \"mahrka\\|mahrk\" BRT.txt | head -10\necho \"=== BRT marэθyu ===\"; grep -n -i \"mar.thyu\\|maratyu\\|maroityu\" BRT.txt | head -5\necho \"=== BRT gaya ===\"; grep -n -i \"gaya-mar\\|gayo-mar\\|gaya.mar\" BRT.txt | head -5\necho \"=== BRT amaretat ===\"; grep -n -i \"amaratat\\|amoratat\\|ameretat\" BRT.txt | head -5"
}
```


### [2026-09-07T16:20:04.801Z] TOOL RESULT

```
=== BRT grep mahrka ===
2643:•  j.  aenaahe,  g.  +''oaöhe  Inf.  'einem (GÜubigen)  Gewalt  anzutun,  an  ihm  Ge- walttat zu  verüben'  a)  mit  Akk.:  hyal  mäi ärfg7-i'j  dläar>iat3  (sd.)  'nariAl  Y.  4^.  7  ;  I —yi  rä  mäi  yä  gaf^<i  (fazdg(sd.)  'naiihg\ \.46.B.  b)  mit  Gen.:  naeÜlcä  *atiha jässiti  .  .  mahrküi  (sd.)  ndit  -nanke  Y. (»5. II.  c)  mit  Pianü  und  Akk.:  Ayat •^natike  dng^'atö  S»ana  i^yPng  arghaya  (sd.) Y.^2.i6.
2923:•  Jt  g.  ao5ista-  Adj.  (fem.  °ta-)  "der  stärkste ; sehr  stark':  uyranqm  °to  Yt  ig.  38;  — iCfrpm  'um  bavähi  Az.j;  —  w/ra  ^aja- maide  'tä  {/ravasayd)  yazamaide  Yt  y. 75;  —  •/a«tfM  «A'  'Um  (statt  NS.)  Yt /Q.141; —  hitqnt  Avö  °tö  Y.29.3;  5.15, 'N't  10,98;  —  srao-hm  ,  ,  yünam  'tim  Y. ,T7-'3i  —  f ravasayd  . .  yä  °ta  vazintqm \x,  13.  a6;  17;  —  yei  hyqn  *asti.aoJaT?ha (sd.)  'ta  YtÄss; —  k»m  'ta  mahrka.. Oi'sd  (sd.)  yaxäite  V.  //.  2.  a)  ASn.  -tim als  Adv, ;  'bmca  . .  vaRiye,t»napiea  (sd.)  V. 3.30.
2989:aajiüa  mahrka  masyäka  da^'S  "so  yaz-lite .        j.  ai^ra./iii/im  N.  rr-.  lies  a:-%ta.fiiiiim,
3053:KompA.;  Ableit.  —  ai.  aghä-  Adj.:  n.  — iEl  vgl.  SÖITERI.IN  IF.  4-  92-  —  Pu-i  '■«/, vaiak,  (meiEl)  vattat.  —  D  Vgl.  iSt,  Lxndner Festgrass  Roth  214-  Pü-:  "pi"-  ä  oj:"  . .  äii  i vallar  lamaitän  rast/,  erl. ;  i  taarkusän  gmi'il\ S.  zu  mahrküSa-.  —  2)  Hds,  ayjwi.
3129:•  j.,  g.  axtay-  m,  'Leiden,  Schmerz,  Kiank- heit':  nöil  'ü/  pouru.mahrkb  tiöii  äkttis Yt.10,50;  —  ndit  'til  mit  mahrk5\.2.%, G.i,y,  —  'tiica  gannmca  V.7.57;  — 'iinqmca  aslanmanqmea  Y.  7/.  17;  V.  7. 59;  —  cvat . .  natu/  °iica  phatüa  ahitica fräsnaoiti  ¥.5.27;  —  yi  S  'til  ahmäi yim  'löyöi  (DS.)  Jax/A^isd.)  "der  du  auch Schmerz  bist  (bereitest)  dem,  dem  du Schmerz  zu  sein  (bereiten)  vorhast"  Y, jö.i;  —  *'eim  N./3'>.
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4475:•  j.  ain-iiltay-  f,  i)  'Unvermögen  (zu  — )': . .  nöil  aSavan>m  'tis  asiarayeiti  "so  macht das  Unvermögen  (es  zu  tun)  den  Gläubigen nicht  sandig"P.;2;  *K.ioi)'''.  2)  'Besitz-, Vermögenslosigkeit,  Armut':  paitistatSe 'tdii  daSi'S.frakarstaya  Yt.  /j.  130;  — yask>mca  mahrk>mla  .  .  °tlm  *ducHrim Yt.;o.iio.'>
4697:amahrka-  1 42
4704:•  j.  a-mahrka-  Adj.  'ohne  Tod':  ayaskim °k)in  bavähi  Az.  7;  —  ayaska  °ka  bavühi Yyt4-
4893:•  j.  a-yaska-  Adj.  'ohne  Kranltheit':  'kim amahrk»m  bavähi  Az.  7; —  "ka  amahrka bavähi  Vyt.4.
=== BRT marэθyu ===
=== BRT gaya ===
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
=== BRT amaretat ===
```


## [2026-09-07T16:20:13.839Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT mar- sterben ===\"; grep -n \"mar-\\s*.*sterben\\|'sterben'\" BRT.txt | head -8\necho \"=== BRT masya ===\"; grep -n -i \"masya-\\|masiya-\\|mairya\\|masyaka\" BRT.txt | head -8\necho \"=== BRT amasa ===\"; grep -n -i \"amasa-\\|ama.a  Spanta\\|ama.a.spanta\" BRT.txt | head -5\necho \"=== BRT maranc ===\"; grep -n -i \"maranc\\|mar.nc\\|marane\\|maraxs\" BRT.txt | head -8"
}
```


### [2026-09-07T16:20:13.949Z] TOOL RESULT

```
=== BRT mar- sterben ===
19936:•  ].,  p.  "mar-  V.  'sterben*.  Piaes.  27 mirya-'^,  mariya-; s-Aoi.  i  mari-, —  PPfP. varyta-;  PFP,  'imrt'^wa:  —    Vgl.    noch
24740:•  j.  raeS^  V.  'sterben',  uzw.  von  ahun- sehen  Wesen ■',  Praes.  27  inhya-;  Per£ I   iflrih:  ~  PPfP.  irista-.
=== BRT masya ===
2761:Z  verlangen,  dass  er  (dem  Freund)  Schutz gewähre"  Y.  7/.  13,  a)  statt  des  praed. Akk.  ein  Adv.:  yimS  avai^a  ktrsnaot yaia  dim  Ual  ahurö  mazäi  "V.  tat  so, wie  es  AhM.  von  ihm  verlangte"  V.  2. 31.  4)  spez.  'zu  hören  verlangen,  hören wollen':  ^J  tsi  asä  yi  asäi gius  ia/.i  (sd.) mraot  is3ntl  tnä  tu  isi  vohB  manaaAl "was  ,  .  kund  getan  hat,  hören  wollen  sie dasdurchdeinenKji/."  Y.4Ö.9.  a)  ohne Ob],":  at  tä  vaxfyj  is?ntd  "ich  will  davon reden  zu  denen,  die  hören  wollen"  Y. _jo.i;  47-6*>;  — yalüä  asnat  yaila  anrät (sd)  isa:iä  Y.  45- 1-  5)  'Jemand  (Akk.) angehen,  sich  an  ihn  wenden,  ihn  bitten': ise  'i/wqm  aAura  mazda  ptrsst  '^wqm  . . Yt  12. 1 ;  —  *yas»  tat  *afivataiti  (sd.) paranlarfm  (sd.)  isöit  N./2;  —  vayö  .  . harn  istmmm  painyätte  ".  .  stellt  sich ein  bei  dem,  der  sich  (an  ihn)  wendet" Yt-/>S3;  —  al  yastim  nsii  na  is7mnS (inpass.Bcd.)9*Jj'i7/(sd.)Y.4ö.6.  a)  mit Inf.:  amslacit  .  .  avaiahe  isinli  masya- kanhs  "die  ^Ienschen  bitten  die  Am.  um Beistand"  Aog.  41.  6)  'Jemand  (Akk.) angehen  (in  feindlichem  Sinn),  angreifen, nachstellen';  avae^amai  ^iff  pantö  yim isfnli    mi^röjiruiS  Yt.  io.45.  7)    'er-
3773:•  j.  a-bar«äiiav-  Adj.  'ohne  Gipfel',  d.  i. 'ohne  Oberherrschaft' (?):  -nva  pas(aila\ asara  (sd.)  masyakaäbyö  V.  2. 5  PüZ.  '>.
3817:•  j.  aiwi.ta£ina-  i)  Adj.  'heranlaufend, anspringend'  zur  Begattung,  vom  Kamel- hengst:  ustrake  vmairyaos  ,  .  °naAi  Yt 14.11.  i)  n.  'Herzulauf,  Anlauf  (nur Komp.).
5744:•  j.  a-sära-  Adj.  'ohne  Haupt',  d.  L  'ohne Oberhaupt,  ohne  Oberherm':  abarssnva (sd.)  pascaita  °ra  masyakaiihyl  V.  2,  5 PüZ,;  —  upa  aooaSsu  (sd.)  ranAayä  yS 'rS  (NP.)"  aiwySxsayeiiifi  "(das  Land) UAR.,  wo  die  wohnen,  die  keinen  Ober- herm haben"  V.  1. 19.
7611:j.  *9-vito.xra'8iy-'*:  °of-  Adj.  'des  Ein- sicht untüchtig  ist':  *janyöii  .  .  mairyaya ''iayd'>  (GSf.)  Y.mis- *v'i-iaxra.  (%  268.  57)  Adj. ;  iBed.  und  El,  s. /axma-.i)  —  Pü.:  fehlt;  Sü.i  paribbraflabiid- dhik.  —  I)  So  K  5  b,  J  a;  KA.  'j:arA'.  — a)  S  sfiiK  11  b.  —  3)  Oder  darf  man  an  mp. laxr,  np.  lalx  'bitter'  denken?
11558:Nebensinn;  avanksnsämi  *janyöis^'>  ünam (sd.)  mairyayh  . ,  yä  .  .  Y.  lo.  15;  — jaitUnqm  *upa  *di^»aähu  (sd.)  Y. /0. 17; —  vispe  yätavS  pairikäsla  vispa  *janayS (als  AP.)'>  yä  drvaitti  V.  20. 10.
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
13185:mit  a  1)  Akt.  'Jemandem  (Dat.)  etwas (Akk.)  zur  Vergeltung  schenken,  Jemandem heimzahlen  mit  —'(Akk.):  kahmilicit  hätqm jtfisqm  rahiäqm  örfä  (aSIA.)» '»>  ubBl^yä ahubyil  "zahl  Jedem  . .  heim  mit  der besten  Erquickung  fiir  beide  Welten"  Y. 3S-&-  2)  Med.  und  Akt  'an  sich  neh- men, sich  erwerben,  erhallen':  naiäs  a'ia .  .  süs  (sd.)  ya>a  him  adars  (3PPrA.)'*' masyaka  FrD.  j(?);  —  hyai  *3  bosilsisd.) vasasP  xsd^rahya  ^«(iSOM.)  Y.^lj.S;  — taoa  ayaol  yä^a  paoirim  *vTr5  ?r>tusqm fsd.)  adasle  Yt  S.  1 4.  3)  Akt,  mit  Lok.
=== BRT amasa ===
20592:•  j.  mustamaSa-  m.  'Myrte*:    'Id  F.  11. Ir.  *tnustainj-ta-1  Schwerlich  richtig  beieugf
=== BRT maranc ===
```


## [2026-09-07T16:20:22.194Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19920,19990p' BRT.txt"
}
```


### [2026-09-07T16:20:22.239Z] TOOL RESULT

```
•  j,  mamnvah-*)  :  mamnus-  Adj.,   PPfA:
')  VgU  lu  jafnn/ah-  No.  1.
•  j.  may- V. 'zu  Grunde  richten".  Praes.  2
maj-a^  (sSPrA.)  F.  6.
«L  minati  'er  mindert'  (usw.).  —  Pü. ;  vinäsisti 'Zerstörung';  vgl.  'vmilay-.  —  ')  Unsicher. j.  mayludivanam  N.  63 :   lies  myaxdoüanqm (soT).
•  j.  mayah-  n.  "Begattung,  Beischlaf: vaitumnfm  yä  fravSit  (Sp.  932  m.)  Yt, 79.80;  —  stryö  °yä  faryiufi^(_sd.)  upaväzB A.,;.4;  F.i/.
Et  ?  —  Vgl.  m J>i£ii™i/-.  —  Pü.  (iuF.):»iäi'H/(?); (luA.):  mäyaiän,  SS.:  strimailhiinäni ;  s.  dazu Bthl.  IF,  13.  147-
•  j,  mayä-  f.  'Freude,  Wonne;  Segen, Glück';  ä  tl baisata  irlra'S>ar»{%A.)vaah!its' mananhs  'yäfyj  (ah  Instr.)  Y.  70.  la;  — yii  n3it  a^ake  vahUtakt  *b?r3/a  Jraman- tahe  'yh  (AP.)  vaou  Y.48Q).
KompE.  —  Vgl.  mäyä:  —  ai.  Vgl.  miyas-  n.
—  Pü.:  (Jia)  fatmäa.
g,  mavae%>m  Y.  40,  l:  lies  mctva&im.
•  g.  *mavai9ya-'*  Adj.  'einem  wie  ich (es  bb),  meinesgleichen  (zu)gehörig':  räitt tsi  xrapaiti  (sd.)  ahmaX  iiyaj  aibT  hyat miidsm  *°%>m^'> /radaää'^a  daenabyB  masää uÄwrä!".. durch  deineOewährung  dessen,  was du  den  D.  als  den  meinesgleichen  gehöri- gen Lohn  bestimmt  hast,  aMAh."'V.40.i.
Ableit  aus  mavani-.  —  Pü. :  it  mild  S  matii- iän  I)  /räi  dalü  an  i  5  dcmkän  apäyet  dät.  — >)  SoPt4.  vgl.Pü.!  s.  in/a/o>^No.I.  Fslscli BB.  15.  259.  —  ')  Vgl.  tu  mavant- No.  I.
•  g.  maVant-  Adj.  'mir  ähnlich,  mit solchen  Eigenschaften,  wie  ich  sie  habe, einer  wie  ich';  nur  im  Sinn  von  Hch'  (d.  " Zara%us(rä):  mazdä  fryäi  %wävqs  (sd.) safyat  'vaitl  Y.  44.  i ;  —  ksm  nä  masdä 'vaitepHyam  dadät  hyai  mä  dngvä  dldar?- satsi^A.^  *ainati&i  "wen,  o  M,,  wird  man einem  wie  ich  als  Schützer  bestellen,  wenn mich  . ."  '^.46.  ^.
Ableit.  —  Ableit  aus  dem  Pion.  i.  Peis.  Sing.
—  al  Tgl.  mivatU-  Adj.    —    Pfi.  (lu  Y.  44^:
•  ].,  p.  "mar-  V.  'sterben*.  Piaes.  27 mirya-'^,  mariya-; s-Aoi.  i  mari-, —  PPfP. varyta-;  PFP,  'imrt'^wa:  —    Vgl.    noch
'sterben,   umkommen':  \pasäv^  k^bu-
'fl*   ''uvämarsiyus    (sd.)    amariyatä   BK
11;  —  'marsant-.         a)  von  rfamschen
Wesen'':  mairyS  drva  .  .jvü  üp^m  jainti..
ttSit  ava%a  rmrits  V.5.  36!!;  38; — yezi
ahmai  (Jmh)  *pu%ra    *miryeitii'>   Nik.  2;
nasäum  .  .  hiskunam  (sd.)    tarS  yar>
miritanqm  V.  Ä33;  — ya^a  vazaya^t
(sd.)  ,  .  tarS  yär>  mtntS  V.5.  36;   —
mfrits  FrW.  8.  2  (?),  Yt  4-  7  (?)■
mit  ava  dnwS.A*>:  yat  drvä  ava.- *tniryde^^  H.  2. 19;  —  iala  drvS  ava,- *mirya>3ha^^  H.  2.  34;  —  ava  hs  (nämL dan:ayasnö)  miryaite  V,  7. 37^;  —  yat maArkasB  ava.*miry3Ue^1'FtW.8.3;  i*;  — pourvS  drvS  ava.M»rstö  H.2.  34.
mit  fra  dnwS.A"':  s^äsaya  sT  vTspS anku! . ,  *jvaiti  a:fale  /ramiryeite  "durch Essen  lebt  die  ganze  Welt,  durch  Nicht- essen  verliert  sie  das  Leben"  ^■3-Zi- ai.  myläh;  vgl.  mriyäte;  v^.mTrad,  murda. — Pü.:  {/rd(\  murlan.  —  D  Statt  miiry-,  S  aSS. 40.  - —  =)  Im  Gegensatz  lu  rcü%;  para.riü%-; vgl.  Yt.  zj.  17  und  V.  S.  37f..  H.  3.  1,  16 und  19,  34.  So  im  A«.  überall  ansxer  in amarsanU.  —  3)  Hd*.  mairy'.  —  4)  So  K  30, M6.  —  5)  Hds.  yaouAa;  vgl.  S  afij.  30.  S. aber  Vyl.  63.  —  *)  Die  Hds.  haben  lu  FrW. S  zweimal  mtryäitt  (dessen  Schreibung  mit  f durch  die  spätere  Form  des  Worts  veranlasst ist)t  einmal  das  Ungetüme  miryaeiatüi  (oder •lalle),  nach  Dst.  ZA.  3.  8  'fulur  moyen'f!).
•  ].,  g.  'mar-  V.  "merken',  Praes.  3 tnara-,  4  mär«-'*  5  hilmar-,  26  mtUrya-, 30  (Iter.)  märaya:  —  PPfP.  'uurg/a-, 'martta-;  PFP.  hismairya-;  InE  m?tvtS, 'varpfat-üa,  •m»r7tayal-ca,  manhräi;  AbsoL 'tn?r3t»m,  'mgntqm.
i)  'etwas  (Akk)  merken,  im  Gedächtnis behalten,  dessen  eingedenk  sein' :  mat  täÜ vTspai^  ylfi  tsi  mq%ra  tnanntl  "mit  allen denen,  die  deiner  Worte  eingedenk  sind" y.43.1^; — ta  vs  urvotä  i&A.)  manntn .  .  sJngAamahX  Y.  31.  i.  a)  'merken auf—'  (Akk.):  ^ass  itthaire  . .  ave  aipi daß,yaniS..Aismar3ntB'^Uo.^S;  b)'be- merken':  karS  masyS yB  ranh^h .  .varjss.- '  stavanhm  äpS  urvaäim  marayäte  Yt. 14.29.         2)  Gebete  usw.  (Akk.)  'sich  ins
dby  Google
«I«
"*44
Gcdidinüs  zorlckiTdiai',  indon  nun  s^'jrmmaroite  A.^5;  —  j{U:a  ..  i«7M  . . m  fyrtanlrwi  odcT  Idsc  nann^nd  wieder-  m*räl  JrS  vi  mmrS  Jnm/^st . .  V.  tg.  6; ho\ti  jat  ja^  <^f  ..  äa}St  aoa  m^^ttm  —  ttjt^  Tt^iy*  ■  ■  f^^immr^wma  fnt- .  .  wLoirjli  V.J.  33t*';  —  mryjmatvm  .  .  martmma  SPm.)  Y.55.6; — yiai  ''fjtam^ iiim..bm  *ML3riMti-  ta^.yjKUfiVi.4,1:  räjm /ntmiargili  ü.  4^ ;  —  *MXavaa  rttüf — /ai  ma^rTm^ramrtnJ  'marä  rSYt.4,  frii  yazat  framaraUi  S-jS;  2/  ('Jlrl;  — 4;  —  yAS:a  . .  ijjam  akuKaJu  'zairydie  ya-Jltt  •A.\  aiti  framarmü  N.32;  2/%  2J; marJf*' ..  dr7m;jjit  . .  srsrayjt . .  ya^^iu  jd:  — *iKa'jmy*  *z^a  fram*r»mMf  S.2Ö. Y./5.6;  —  iti^3  jwxiird  .  .  mar»mna\ J^iftiLj  xanmmna  *tixijwaia  sl^syamna  ..\
II;  Si.
J.6; — lamtSt..mar>*ttm
a)  absohlt
(NPul,  ncdiem.  J .  ■  >K  <u/r» /•n'(<p j«£r  YL5.  S6.
fB-t  aäci  'JaDaoden  in  Gedanken  \a- vümcfaoi':  yai  b^Siä  cSp.  954  m.;  aäei.- SAdS  aisnjmartts^'  *fcttm  ''naram  tüs' ßmiOam  \t.i4-S4-
jDJt  tipa  I }  VGebete  o-d^)  anfaagfp,  rezi- detot':  upa  vä  ma^rrm  sffnt^m  wiaraita V.4.45".  ^>  '(«oen  Veitragi   durch
blosse  mündlicbeVaaiHvdimg,  auf  Tren  nnd Glauben  ohne  VeipfaiMtmg  abschLessen': i^  (nämL  wü^rl}  upaj»^nlS  A3m  as/jrmJ,- matS  h3u  a>atmay}.maz3  "der  ehte  {^a- iragl  wird  aof  Treu  nnd  Glauben  ge- schlossen, der  andere  nnt^  Vnplaiiduns eines  Asp^  der  dritte  . ."  V.  4.  48  '■'.
mit  paiti  \)  'sich  etwas  ins  Gedächtnis znrückjnfen':  itaeta  jai^a  .  .  T»r7Ümtna *sixvmita  säiayamHa  . .  päAtmanrnna (yPm.)w  Jramar^mna  .  .  Y.  55.  6;  — patHtmärtHtim  "'>  rpTTttubm  *sixäiUfm säcayani^m  .  .  Vjrt  32.  3)   Med.   'sieb
»chnend  denken  an  — ,  ach  sehnen  nach  — ' <Akk.V-  ääriM  jim  paitiimamiU pasvas'a .  .  ka/ia  nS  oin  tayarJt  tiärjs  \\.8,  5; 41,  48;  —  yä  fnämL  gäul)  vanta  (sd.i aämna  .  .  goT^aihlm  paiiismarrwina  Yl 10. 86;  —  andrt  . .  saeirt  i'statt  Gen.)  | T3äm    patäimarfmma    YL  5.  115;    — |
.  natTK  patäsmartmita  arat  .  .1
...        I
No.  L2.  —  'I  Nar  Vjt,  ohse Wen.  Das  i  wird  dird  das  ji«it]j>.fc**JT mp.  oda  iqt.  Won  *ciaalasst  b  '  -    —
S  Uds.  ^  <riu.    —    *!  Pk.-.
n'iMa   fcscbr.  ddpiuciii  Ott    -
Objekt  feUt.    —    ^  Npä.:  ii:i:ar
wjcik.  —  ;.■  I^ :  aüur  .ynd  e  "
äii  ijjai  e  ah^  —  *t  NA.  nckt  U  ■i^tt.a-
cnd  trennt  üa  a^  daTon  ab.  I^  teilt  hinter m^  ab,  da=n  lol^:  iifm  M  a  mfar  mMrüi ia:ä  ia  n*  ä  mirti.  VgL  Gof.  Snd.  /.  101. m.  ~  ")  S.  Ko.  I.  — I  "hoBem'.  —  ">  Das  Mibe Won  stefai  anck  N.  /o  24.  »4;  als  Eiläateras{ TOS  r^inisM.  a»A  PPGL  soD  ei  ^inan gelesen  «erden.  Idi  *eiB=le  ndmcb,  da» hier  ^ind-n  ■)«£■*  g«aeiat  ist;  »jL  St: dj'rrfl:^  tA.:  ffi.iitysü    nach  DsT.L
«   }.    T^iita   kS'ja  Man  taka  mai«  4im« 'JOMosiu  Yl  /2,  8 :  —  ?  — ,
•  g.  (,  j.)  maraot-  Adj^  WA.:  s.  'msr-, KompE.
•  jL  niarav-  m.  Name  eine-  Sudt  in Medien:  *nii  nSat^  vardmttam  miaJaiy Bh.  2. 6.
Lesnni;   nach  £=.;    der  Stein  lei^t  nnr  nock w* ;  Ri.  schätzt  das  Won  aaf  S  Bncfattaben.
|.  aiMFukt   P.  K>:    bes    ■«ir^rif.     S.  nntcr
;<$:  lies  mrif. -       I-  j.    ._ -.„^^  Adj.  (fem.  'na-),  PPM.: Jran^ay-^  *paitumarvnU^  '*  j^  atanniaitte  \     KompE.
.  /«/««.»    ToAmai-a   Y.  2J.  3;   —  yam  \  ,  j  ^narwmn-  n.  ImgcdädUntsbehaken': d&rat  paitumamtU"'^  mt^rH  ..  Vyt52.    I  jj«-a  Ära^*»tflü  ■»«  räwö  Ääw«'
mit  jyj  '(Gebete)  aufsagen,  rezitiren',  „^„  iitmui^  /ffrorr  Yr  r^  17 bes.  in  munnelnder  Weise:7i«ww  haptar^  Znm  V.  ».«r..  —  ABHilliEe  BOdsi^.  ObaL Äaitlm..Au/ram^nt^m{iiä.)/ramar^mnrm  j>*«M-n,-gr. i^»*:  in  »ciileicken?  SBnii. ^pass.)  Vr.  /tf.  o;  —  aJaaiapaifim  gJ>am  . . '  ZDMG-  -^S.  30>  Dann  ako  ar.  '»«r»^. Au/ram^r^itam  (sd.)  /ramar^mna in  (pass.)  •  i-  »^  mar^m  patriäm  V.  J.  43 Vr.i4.oC; — aioke  vahistahe  *b»r3]a  fra-  PüZ.:  —  ?  — . mar3taheY.48; — jiff. . r^^ Kaum  ratßm,m  y  nuüiim  Adr.:  s.  maiiya-.
dby  Google
i»4S
mahrkai
;i46
•  g.  mairiüta-  Adj.  'dei  am  besten  im Gedächtnis  hat,  merkt',  mit  Akk.  verb.: minda  sas^ar!  (sd.)  'ts  Y.  2g.  4.
Zum  V.  »mar-. —  Vi.:  ämärtnilär,  Sü,:  gatia- naiara^,
•  j.,  g.  mank-  V.  'töten,  zerstören',  uzw. vom  Töten  mid  ZerstSren  oÄurhcha SchUpfiingen').  Praes.8  m>Tvni-,  9  mjnfUa-, [12  +  13  Hurm^inT/],  1 6  (Des.)  mimanxia-, i-j{F]it)m^r>x^-'\  aj  m^rfftQ/a-^^;  s-AoT. I  manx^ :  rmrsxs:  —  PFP.  'imnxlyanta-y Inf.  fmr?^?ifyai,  mftfncyäi,  mahrkäi,  mahr- ka%äi.
'töten,  verderben,  zunichte  machen,  zer- stören, schädigen*:  nSii  . .  duf,sasliH3A.) aham  nurqryat  (3SOA.)**  Y,  45.  i;  — anaii  3  wtanahlm  ahüm  mtrfttgfäuye (2PPM.)s)  "auf  solche  Weise  zerstört  ihr das  geistige  Leben"  Y.  5J.  6 ;  —  HltrXm  . . yiin  nSit  mfryy^ntei^SBM.)''^  anrS  mainyus "..,den^jtf.nichtverderbenkann"Yt.iS44;
—  xsayamna  marr/ttUe  (3SPM.)**  gaiha , .  asahe  yaiia  tanda  yatumstita  mannclfa (3SOM.)  gal'^ä   alahe  V.  iS.  5$;  Y.  S.  $;
—  mä  mprmMnt!  (3SPrA.)"  gai'hä  .  . asahe  SrB._j;  — gandarzwjm  ..yS apatat .. m^nx/änS  ga^a  .  .   aiahe   Yt  ig.  41;
```


## [2026-09-07T16:20:31.669Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## HRN leaf 239-241 (pp.218-220)\"; awk 'BEGIN{RS=\"\\f\"} NR>=240 && NR<=242' HRN.txt | head -120"
}
```


### [2026-09-07T16:20:32.924Z] TOOL RESULT

```
########## HRN leaf 239-241 (pp.218-220)
— 218 ~
maretan-; plilv. mart, martum; ai. mdrta-, vergl.
mdrfya-; arm. mard 'Mensch' (H. No. 188).
kurd. mir *Mann ; bei. mar (224).
973. murden sterben', Praes. mlr-em, nturdär 'Leichnam' ^),
mlrämden.
g. martmmi; Kä§. mertdn, mardSn^ mardemun, bemert;
gel. wardmy mäz. bamardeni.
ap. l^mar-y amariyata 'sterben ; aw. 1/^mar-, fra-
mairy^it^; phlv. murtan^ nilret (vd. 5 (134) Gl.); ai.
[/^mar-^ mriydte 'sterben ; arm. meranim 'sterben' (H.
No. 195).
kurd. wmn 'sterben ; aiy.mral; oss. mälin 'sterben'
(178b), d. märiin, t. marin 'morden, tödten* (178c);
bei. mirag, n. miray (237); wa/. mari-am, mlrlt^ §iyn.
sar. mTram.
974. merz 'Landstrich*, Mark*, merj, merzban.
(aw.) merezu' *boundary of a country' (ZPGl.)^);
phlv. marjpün bezw. marzpcin (Kärn. 36), arm. LW.
marz^ marzpan.
got. marka 'Mark'; air. mruig, bruig; lat. margo
Rand' (weiteres bei Froehde, BB. VII, 327).
975. mury 'Vogel; Huhn, mury[abi 'Ente ^).
mäz. wary.
aw. mereya- 'Vogel'; phlv. mury, murv (auch Papyrus,
Hörn, ZDMG. 43, 51)^); ai. mrgd- 'Waldtiej-; Vogel*.
kurd. vergl. miräwi 'Ente* (H.-Sch.); afy. marya;
oss. d. t. mary 'Vogel* (179); bei. (LW.?) murg, n.
mury *Vogel, Huhn* (243).
*) Np. murderl (Sahn. I, 17, 72; 20, 44), murderlj ist unklar.
*) Merezu- im Awesta selbst gehört dagegen wohl nicht hierher.
Die sekundäre Bedeutung von gel. merz 'Damm, der durch einen Fluss
oder Sumpf oder auch durch ein Feld gezogen ist*, hat Melgunof
(vergl. ZDMG. 21, 233) zu der Zusammenstellung mit nhd. Marache^
Marschland verführt, die lautlich unmöglich ist.
') Käs. K. dagegen kargühl *Ente*.
*) Sekundäres v wie in phlv. marvärU^ np. mervärld gegen arab.
marjc^fl, gr. juaqyaqCrrji,
— 219 —
975**** nie%*y zum Viehfutter dienendes Gras', meryzar *()rt,
wo mery wächst', arab. LW. inarj *Wiese\
aw. mareyOr *Wiese' (Hübschmann, ZDMG. 46, 244
No. 75); arm. LW. warg 'Wiese', syr. LW. n:i*1D 'Wiese'.
kurd. mirkj merya 'Prairie'.
V
976. meryzenf merzyen, merzyän 'Kirchhof (Beleg bei SF).
merg Tod' -r phlv. özan *Da;Kma', np. (Riväyet)
meryözen (Darm es teter. Et. ir. II, 132).
Ganz unsicher, da die PehlevTform (NB. )XTN oder
JNin) unklar ist; die Verknüpfung mit ap. apadäna-
ist vollständig verfehlt.
977. merg *Tod'.
aw. mahrkor 'Tod*; phlv. marg\cirjan^ marißh 'Tod';
arm. vergl. waÄ, warA 'Tod' (H. No. 185).
kurd. merk 'Tod'; bei. mark; oss. d. t. marg *Gift'
(178 e).
Der Bedeutungswechsel im Ossetischen könnte als
ein Analogen vielleicht auch die Ableitung von np. mar
Schlange' aus l^mar^ sterben* bezw. deren Causativs
*tödten' rechtfertigen.
978. muzd, muzd 'Lohn, Preis', muzde {mizde) 'frohe Bot-
schaft'.
aw. mUda- 'Lohn'; phlv. m(i)zd (paz. mozd), mtizd
(AV.); ai. midhd- 'Kampf, Wettkampf; got. mizdö
'Lohn'.
oss. d. mizd, t. m^izd 'Bezahlung, Vergeltung, Lohn,
•Belohnung' (188).
Das u im Neupersischen ist auffällig.
979. me^^yiden saugen, schmecken', meze 'Wohlgeschmack',
meklden.
g. meöcLdmün\ Käs. Q. hdmij, K. bemüj, 7j, oermez;
Q. mitSn, K. vermSt {*mi/ten),
phlv. micUan (Bund.), midak 'Wohlgeschmack (Men.);
kurd, mltin^imlßim 'saugen'; bei. micagj n. misay 'saugen'
(235).
Von einer l^meq/c- 'saugen*.
980. miSe, muze 'Augenwimper, HJD (Jer. 9, 18).
g. müjeng; Käs. mejd, mujd^ mezL
— 220 —
kurd. miMnk, mizl, mujüal (H.-Sch.) ^Augenwimpern';
bei. micäc, n. misäs ^Augenwimpern*, daneben LW.
mizayän (236).
ai. nimis' 'Blinzeln, Zwinkern des Auges*, skr. nMsa-,
das Bartholomae ZDMG. 44, 553 vergleicht, stimmt
lautlich nicht zu np. kurd. i, g. /, bei. c (für letzteres
erscheint im nb. regulär s, vergl. Geiger, Dialekt-
spaltung, 83).
981. ^nest 'betrunken* 0-
aw. vergl. mada- 'Kausch trank* ; phlv. mast (PV.);
ai. mattd- 'trunken', vergl. |/"fwad-, mddati 'froh sein,
sich berauschen'.
Allgemein entlehnt; oss. d. mast, t. mäsf 'Galle,
Zorn' (181) ist wegen des Bedeutungswechsels un-
sicher.
982. ^nust 'Faust*.
mäz. mis (*nitist).
aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
(18) Gl.) 2), mtistih (AV.), must (PPGl.); ai. musti-,
kurd. mist, miste/c; af/. mmt^ müt; bei. LW. mtist
(172) ; wa;k'. mösty sar. mut
983. tniiSten 'reiben*.
aw. [/^marz-j marezaiti *fegen'; phlv. mmt^ mmt
(vd. 4 (7) (26) für aw. marsta-); ai. l/'mar/-, mdrsfi
'abwischen'.
kurd. mistin 'fegen'; af/. mu/al; bei. musag, n. musay
'reiben*, kratzen, streichen, salben, mahlen' (244).
Eine Doublette zu np. maltden (No. 962).
984. muy, möy 'Magier, Feueranbeter*^), möbed,
ap. magu-; aw. -moyu- in moyu.fbis-? (vergl. Geldner,
*) Irgendjemand hat, wie mir Herr Prof. Nöldeke sagt, irgendwo
(die SteUe war augenblicklich nicht aufzufinden) das als arabisch geltende
medhüs 'sinnlos* für ein persisches Wort (|/ mad' + hös 'Verstand, 8inn*J
erklärt. Ich denke aber, dann könnte es nur mesthös lauten.
') Ganz falsch war natürlich meine Bemerkung ZDMG. 48, 36
Note 34.
') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
und besonders zum 'Kneipwirt, Zecher* geworden (H ä f i ? häufig), vergl.
auch muybece^ muyän u. a. m.
```


## [2026-09-07T16:20:42.788Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### HRN p.217 (leaf 238-239)\"; awk 'BEGIN{RS=\"\\f\"} NR==239' HRN.txt | tail -30\necho \"##### HRN p.69 (leaf 90)\"; awk 'BEGIN{RS=\"\\f\"} NR==90 || NR==91' HRN.txt | head -80"
}
```


### [2026-09-07T16:20:44.193Z] TOOL RESULT

```
##### HRN p.217 (leaf 238-239)
nur dialektisch findet (vergl. z. B. Käs. K. /üi für
/ud sowie S. 188 Anm. 4) ; doch vergl. pei- (No. 345),
piyaz (No. 347*'***), fäyenej (No. 347*^*» Anm.), oMn
(No. 61), sowie engiiydn (AM. 11 Zeile 6 v. u.) neben
engudän, enjiidän Xaserpitium, Silphium*. Ich glaube
indess dennoch, dass mdye ebenso wie mäteries von
dem Stamm mät- bezw. mäter *Mutter abgeleitet sind.
An Zusammenhang mit ai. -maya-, welches Stotf-
adjectiva bildet, glaube ich nicht, trotz Bartho-
lomae, ZDMG. 40, 294 Anm. 1 (ai. siumya- steht
zu vereinzelt, um die Bedeutung 'Material* für maya-
erweisen zu können). Vergl. auch g. mäye etc. 'Mutter'
oben unter No. 956, Ende, welche die zweite Laut-
verschiebung bei mätar- zeigen.
Ist tnaddat in der Bedeutung 'Stoff' ganz sicher
arabisch ?
971. mer 'Zahl*.
aw. [/^mar', vergl. sumär (No. 791) ; phlv. marj
marak 'Zahl*.
Die dem Dativ und Accusativ, oder auch dem
Nominativ vorgesetzte Partikel mer ist wohl kaum
mit mer 'Zahl* identisch (die Ableitung derselben aus
matra-, an die Rückert, ZDMG. 8, 262, dachte, und
die auf dem Wege *mahr, *mar, mer lautlich möglich
wäre, wird dem Gebrauch des Wortes auch nicht ge-
recht).
972. jnerd 'Mann', merdum,
Kas. K. mird[i neben merd.
ap. vergl. marfiya- 'Mensch', vergl. iua^Ti[xd(ja =
av&()(07totfdyog, Ktes. bei Phot. 46 a; aw. mareta-j
##### HRN p.69 (leaf 90)
— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.
— 69 — '
810. perl 'Perl, guter Genius*.
aw. pairlkä' *Hure'; phlv. parlk, arm. LW. parik,
LW. af/. parT.
Nach Bartholomae, BB. 15, 9 ist die SiW. pairikä-
ursprünglich *die Fremde'.
811. perer Vorgestern, perejröz, pere\seb.
Kilo, perc; pere]sdl, pe7^i]söUf per]sew^ pörijsd.
aw. '^parö.ayare; phlv. parer.
kurd. picne (Houtum-Schindler), per; oss. vergl.
fal'iväre 'im vorvorigen Jahre' (274, 2); bei. parerl^
paireri^ n. paln (285).
812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
'bereuend', pesiman,
ap. patü r *wawc/- ; phlv. pasTmän (paz. pasemän) ;
ai. /)ra^^ -i- y/'yw^w- 'erwiedern, entgegenhalten'.
Die Entstehung der Form pesJmän ist ganz unklar ;
piz'' scheint aber sicher auf patis hinzuweisen. Der
Wechsel von z und s findet sich auch sonst dialectisch.
313. pi^fnurden, pezmurden 'erschlaffen, verblühein', pilOTi:!
(Is. 16, 8 u. ö.), plzmertden (Vis und Rämin, S. 47
V
Vers 16), pizmeranlden (Sahn. 85 Vers 433).
ap. paus bezw. aw. aiwis j- \^mar-,
piZ' Scheint wegen jüd.-pers. V\^ ein alter Fehler
für biZ" zu sein, (de Lagarde, Persische Studien,
75), doch findet sich piz- auch in pizöhiden und Ab-
leitungen (No. 314) und in pizmän (No. 312). Jeden-
falls spricht man heute p" (W o 1 1 a s t o n) ; das b
des Gazophylacium's (s. v. infracidirsi) kann
nichts beweisen. — Im Wesentlichen übereinstimmend
ist die Auffassung Nöldeke's, ZDMG. 45, 106
Anm. 3, welche ich erst nachträglich zu Gesicht
bekommen habe.
814. pizohlden 'erforschen, nachfragen*, pizöh, pizöhis^).
Reime z. B. Sahn I, 73 Vers 215, Sälin. I, 140 Vers 198. Die
Wörterbücher wissea nichts mehr voa einem Majhülvooal.
```


## [2026-09-07T16:20:52.096Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### HUB leaf 51 (p.41)\"; awk 'BEGIN{RS=\"\\f\"} NR==51 || NR==52' HUB.txt | head -70"
}
```


### [2026-09-07T16:20:53.398Z] TOOL RESULT

```
##### HUB leaf 51 (p.41)
— 40 —
ist unsicher; de Lagarde, Btrg. z. bactr. Lex. p. 55
ist schwerlich im Recht.
307. Fr. Muller WZKM. 6, 352 bemerkt mit Recht, dass
man fiir paz. awarvez Shk. 233 = arm. AprUSz (= Aprv^)
im Neupersischen *barvez anstatt parvez Victor, felix,
fortunatus' erwarten miisste. Ist es beeinflusst durch
p^rdz Victor, felix, faustus ?
308. Ich kann die ihrem Sinne nach zusammengehorigen
Worter (ZDMG. 44, 560) lautgesetzlich nicht ver-
einigen. Darmesteter liest mit Westergaard
paoirySnyaS' (von paoiry^i- aus *pdrvydni-^ vgl. afgh.
pSrune, Geiger, Etym. Nr. 170), das er mit ahuranfs
(von ahurani' ahurisch*) vergleicht und durch *die
(Wasser) des Paoirya (Zend-Avesta II, p. 418) iiber-
setzt. Aber Geldner liest paoirya^iny as- von paoirya^i-
= ap. *paruviyaini' = np. parvm?
309. Np. parhe» 'Enthaltsamkeit, Fasten', parMxtan *sich
enthalten' = paz. pahrez Min. GL 154, phi. pahrSd
'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
p. 62, Anm. 48, pClhredSnd *sie hiiten, pflegen ebenda
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
Bdh. Gl. 108, arm. parik ein Fabelwesen' (Eznik 97, 98),
np. pari 'Fee, EngeF.
312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
paz. poSetnan repentant', paSSmam 'penitence' Shk. 263,
Min. Gl. 157, phi. paSSmdnlh 'Reue* Phi. Min. p. 5, Z. X5,
— 41 —
Die Sanskritubersetzung giebt das paz. Wort durch
pagdnttdpin- Veuig* wieder. Es wird irgendwie zu zd.
pasda nachher und Wrzl. man *denken* gehOren und
urspriinglich *nachher-bedenkend* bedeutet haben.
313. Die von Noldeke und Horn erwahnte Form gu^s-
murdan des Judenpersischen zeigt, dass piSmurdan
'verwelken iiber alteres bizmurdan (Noldeke, ZDMG.
45, 106) auf *vizmurdan zuriickgeht. Damit fallt
Horn's Etymologic, insbesondere piz- aus patis.
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
*domu8 aestiva, aula, atrium, coenaculum, porticus =
arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
skemba- vd. 2, 26 ('Stiitzmauer Geldner, 'batiment
avec balcon* Darmesteter) stelle, zuriick. Im mittel-
persischen wurde *patskamb zu *paskamb, ehe pat-
(vor andern Consonanten als s, s, d) zu pai- wurde.
316. Np. past niedrig, gering' ist nicht = skr. upasti-,
das zu *bast geworden ware, sondem = *patta-y skr.
patita-, Vgl. oben Nr. 92.
317. Etym. dunkel, auch nach Fr. M tiller's Erklarung,
WZKM. 6, 184 (pistdn = pEstan Gl. and. Ind. 113 =
*payastdna', das zu zd. fStana- nicht stimmt).
318. 7m pus vgl. Spiegel, WZKM. I, 250.
219. Np. pasa/nd *angenehm, gefallig, gebilligt, will-
kommen', paz. pasandfdan *to approve* Skh. 263 ist mit
```


## [2026-09-07T16:21:17.959Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD murdan/mard/masy ===\"; grep -n \"^murdan\\|^mard \\|^mardom\\|^mardom\\|^mašy\\|^mahrag\\|^marg \\|^murd\" PHD.txt | head -20\necho \"=== PHD grep masya ===\"; grep -n -i \"masya\\|mahrag\\|mardom\" PHD.txt | head -20\necho \"=== NYB murdan ===\"; grep -n -i \"^murtan\\|^murdan\\|^mart \\|^martom\\|masya\" NYB_vol2_glossary.txt | head -20\necho \"=== CHEUNG mar ===\"; grep -n -i \"pazmurdan\\|pazmordan\\|pažmurdan\\|\\*marH\\|marH-\\|vi-mar\" CHEUNG.txt | head -20"
}
```


### [2026-09-07T16:21:18.044Z] TOOL RESULT

```
=== PHD murdan/mard/masy ===
492:murd 57 nāmčištīg
4837:mardomzadagih “94 PESTS
=== PHD grep masya ===
4837:mardomzadagih “94 PESTS
=== NYB murdan ===
2379:mähik [m’hyk] fish 942°; pl. cas. obl. w-än 8023. — Skr matsya-; Av. (1155) masya-; MPrth m’sy’g (MHC); MPrs mhyg; NP mahi.
2386:2. with -s- for -hr-: Misē; msyd msy’ny DkM 59314-15; with -rs- for -hr- : mrsy’ny (Tanbih, l.c., var. of Cod. L). — C. In Khwarizm mrd — mrd?nh (Birüni, l.e.); MPrs mwrdy’ng (A-H I, p. 220). Cf Chri- stensen, Le premier homme I, p. 9-10. The forms reconstructed and used by him: * Masyay — *Masyānay, are nowhere to be found, and fictitious. The forms Khwar. Mard ("Man") and MPrs fem. Murdiyänag are clearly WIr, and so are also Mihreh < NW *Midriya- and Misēh < SW "miciya-. The other forms are typical EIr, and betray the difficulty WlIranians felt in rendering the sound developed in EIr from -rt-, -r0-, -0r-, which must have been something like an unvoiced -r- or -l-, and which they analyzed as -hr-, -hl-, -rh-, -lh- or simply identified with their -§-. Cf the spellings of pahlom (g. v.); Av. agavan-, BP ahlav < artavan-; Av. ašsmaoya-, BP ^hlmwk: ahlamög, but KZK 1. 13 'iswmwky (in the parallel text SM 1. 20 ’himwky); hence the inverse spelling pwlsy for puhl ‘bridge’ (q. v.), SM 1. 43 (Arab mrsy’ny, v. above, is a mechanical rendering of a written BP form *mlsy’ny = mihriyäne). Consequent- ly, mahlé malhé māšē are Elr develop- ments of *martiya-; miše EIr develop- ment of *mißriya-, ci Sogd mys < midra. We have to do with two forms of different origin: 1. *martiya-, 2. *mi@riya-; as to this problem, cf Sven Hartman, Gayo- mart (1953), 45-64.
2460:mart [mlt'; commonly GBR’] a man; GBR’+1 = mart-ē with the indef. art
2473:martoméh [mltwmyh; *NSWT?-yh] the quality of being a human being, human nature 631. 80°.
2483:w., pl. cas. obl. hacis-—-àn men of higher rank than oneself, one’s superiors 704; pus i ~ the eldest son 318; nātrīk i ~ the First Lady (of the harem) 4121; kunom ~ hac I shall do greater things than... 5214; pat han 1 ~ gobišn in a loud voice 4521; — masist kirpak 6971; masist rah the most excellent way 761’; dipivaran mahist the Head Scribe 1118, 1821, 19%; mahist aštak 36°; — adv. by far 977°, — Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masista-; OP *ma- Oan-, comp. *madyah-, sup. madišta-; hence in Milr: NW mas (MPrth only adv.), comp. masdtar (v. the next w.), sup. masišt (MPrth msyšt), but SW "mah . (not attested so far), comp. mahy, méh (MPrs mhy A-H I) Paz. meh, mehe, „mahi; NP mih (used as pos.), sup. mahist (MPrs mhystg ‘presbyter’ A-H II). BP has taken over NW mas as pos. and comp., and as sup. both SW mahist and NW masist, but developed, according to the SW rule: -št- > -st-, to masist, a hybrid between SW and NW. Possibly, however, -s- was pronounced -h- through- out in SW; Paz. only mahest.
2591:murtan [YMYTWN-tn'; mwrtn!] mir- to die 321, 913 and passim; frót ~ 5471; be ~ 2133, 34lšete. — Av. (1142) Imar-, pres. mirya-, pt. morota-.
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-manihš Manuš-ciEra-: Manucihr maodanö.kara-: mustā- pät Imar- (mirya- morota-): murtan ?mar-: amar ?mar- + avis: ošmurtan maroz-: marzihistan maroza- -- pana-: marz- pan Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr
=== CHEUNG mar ===
17541:marde ‘to die’ || (+ *pari-) NP paZmurdan/pazmir- ‘to wither, fade’ || (+ *ui-) Bal. 
17641:*marHl 267 
17664:*marH! ‘to rub; crush’ 
17671:contain *marH', rather than *maz ‘to break’: all the attested forms have , /r/ without 
17695:268 *marH2 
17711:*marH ‘to block, hinder 
17983:*marH!, which is preferable: all the attested forms have , /r/ without the diacritic dot 
41302:pazmurdan/pazmir-, 
55778:*Hram (s.v.), *marH’, *raud, 
56178:*marH' , *pais, *uraiH, 
56895:*marH’, *raud 
57657:*dauH’, *garš, *marH!,
```


## [2026-09-07T16:21:30.905Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17490,17560p' CHEUNG.txt"
}
```


### [2026-09-07T16:21:30.950Z] TOOL RESULT

```
f.; Weber 1993: 105 £; Abaev, Slovar’ IV: 281 f.; Werba 1997: 310; Adams 1999: 453 f.; Cheung 2002: 
203; Shahbakhsh: s.v. mant- 


*тпаг ‘to die’ 

*AVESTAN: YAv. mar- ‘to die’ || (+ *aua-) ‘to die (off)’ || (+ *fra-) ‘to die, wither, 
wilt (to death)’ — Liste: 43 

MED.; Pres. -ja-: IND. 3sg. YAv. framiriieite (V 3.33), INJ. 25р. ҮАУ. auua.miriiagha (H 2.34), SUBJ. 
3sg. YAv. auua miriiaite (V 7.37); Partic.: fut. pass. ? YAv. framərə0Ba- (Yt 2.13), perf. pass. ҮАУ. 
morota- (V 5.36, V 5.38, V 8.33), YAv. auua.morota- (H 2.34) 

*OLD PERSIAN: mar- “о die” = Kent: 202b 

MED.; Pres. ja-: impf. IND. 35р. am(a)riyatä <a-m-r-i-y-t-a> (DB 1.43); Partic.: perf. pass. m(a)rta- 
<m-r-t- > ‘dead’ 

"MIDDLE PERSIAN: MMP myr-, ВМР myr- (YMYTWN-) /mir-/ ‘to die’ = DMMPP: 
236a 


*maré (mark) 265 


Pres.: IND. 3sg. MMP myryd, SUBJ. 152. MMP myr’m, 3sg. MMP *myr'd, OPT. 3sg. MMP myryh; 
Partic.: perf. pass. MMP mwrdg, BMP mwltk /murdag/ ‘dead’, MMP mwrd 


*PARTHIAN: myr- ‘to die" = Ghilain: 90 | DMMPP: 236a 
Pres.: IND. 3pl. myrynd; Partic.: perf. pass. mwrd ‘dead’ 


*KHOTANESE: mär- ‘to die’ = SGS: 109 

*SOGDIAN: BSogd. myr-, CSogd. myr-, MSogd. myr- ‘to die’ 

Pres.: IND. 3sg. BSogd. myrty, SUBJ. 2р1. SSogd. myr’6, 3р1. BSogd. myr’nt, etc. 

*CHORESMIAN: "my- ‘to die; be extinguished’ || (+ *pari-) prmy- ‘to wither, fade (of 
plants, fire)’ — Samadi: 113 

*BACTRIAN: pip- ‘to die’ > S-W, Bact.: 204b 

*NWIR: Widely attested: NP mir-/murdan, Bal. murt-/mir-, Kurd. (Kurm.) mirin/mir-, 
(Sor.) mirdin/mir-, Zaz. merdis/miren-, Abyan. mardan, Abz. marda/mér-, Anar. 
marte/mir-, Awrom. mardáy-/mur-, Fariz. -mard-/-mär-, Yar. -mard-/mer-, Gz. mér-/ 
märt, Gil. (Rsht.) mardoen/mir-, Gur. (Kand.) märd-/-mr-, Ham. märtän/mer-, Khuns. 
mir-/mert, Mah. märd, Nn. marte/mir-, Natan. mardän/mor-, Qohr. marda/mir-, 
Semn. -märd-/-mär-, Sang. -márt-/márcen-, Shamerz. -mörd-am-/mir-äm-, Siv. mer-/ 
mérd, mird, Soi bä-märd-/ä-mir-, Sorkh. -mord-/meer-, Lasg. -mard-/meer-, Tal. 
marde ‘to die’ || (+ *pari-) NP paZmurdan/pazmir- ‘to wither, fade’ || (+ *ui-) Bal. 
gimurt/gimur- ‘to die, wilt’ 

*NEIR: Oss. I. maelyn/mard, D. mzlun/mard, Sh. mar-/müd, Rosh. mir-/müg (etc.), 
M. тәг-/тәг-, Yi. mor-/mur-, Pash. mrol/mr-, Yghn. mir-/murta-, Wa. mor(o)y-/mort 
‘to die’, Oss. I. maryn/mard, D. marun/mard (caus.) ‘to kill, murder’ || (+ *pari-) Sh. 
(Baj.) parmir-/parmud, Wa. pormor-/pormord- ‘to wither’, Yi. parmorya ‘withering’ 
*MISC: Par. mer-/mur-, Огт. mr-/mulluk ‘to die’ = mr-/mo I(I)ók, mölok, Par. 
mér-/mat (caus.) ‘to kill’ 

*SANSKRIT: mar ‘to die’ (RV+) = EWAia II: 318 

© This root has an impeccable IE etymology. 

«PIE *mer- ‘to die’ = LIV: 439 f. | Pok.: 735 

*IE COGNATES: Hitt. /merzi/ ‘disappears’, /merta/ ‘he died’, Gr. € woptev ‘ané8avev, 


died’ (Hes.), Lat. morior, Arm. meranim, OCS mréti, Lith. mm ‘to die’, etc.
```


## [2026-09-07T16:21:47.703Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD leaf 284-285 (p.218-219) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==285' SOD_pages.txt | head -60"
}
```


### [2026-09-07T16:21:48.896Z] TOOL RESULT

```
=== SOD leaf 284-285 (p.218-219) ===
                                                                                                                      218
      mrt't rwc


     5453 mrt't rwc M, S     (^^^j^jjj^y^ r** jjj                5465 mrtymy =» mrtym}y
          martat-roc ^mwrt't rwc, 'mrtch, mrt-
                                                                 5466 mrtk S(AL) -> mrt'y
          seventh day of the month                               5467 mrt mrt B, S                            yt l^S j>
          GMS 86.138; Hen. iii B11R8; Fasts. 149.9; MDii B            mart mart <D<Av. mardta
            11R 8
                                                                      everyone, each
     5454 mrt'xmk    S(AL) ==» mrtynVk, mrtxmy(y)                     VJ 52, 277, 6a; BSTBL, Vim. 189; TSP 2.737,
     5455 mrt}y B                                           ^           12.30; GMS 493 n
          marti ©OP martiya =*mrty                               5468 mrtmync B                            J^'^s
          man                                                         martmenc
          SCE 374; 03 4: Frag. Len. 71.4; mrtK Anc. Lett.             human, humane
            255                                                       Frag. Len. 65, 5
     5456 mrtyh =* mry2, mry}                                    5469 mrts'r                (0>^>^
     5457 mrtymwt                                                     martsar (m's*) ®<*ima9ra+sdr
                              \                  OU^
          martoxmat (mrtymkt, mrtymH) ©pl.; ob. -y                    here, hither                   =»ms\ mc*
            =>mrtynVy
                                                                      GMS 301, 461; BBB b43, TSP; BSTBL; VJ; STii
          men                                                           9.11; BSTi A 22; MD
          SCE 531, 533, 544; TSP 5.3; STii 7, 14; mrtxmyt(tl    5470 mrtxm'nyGi) M                          J^^^y
            BSTBL; -mHu SCE; BSTBL; Dhu. 90; STii                    martoxmaneV-ya
            10.45; Frag. Len. 70.4, 932; ob. pi. mrtYmHy,            human, humane
            SCE 103; BSTBL, Dhu. 31; STii 7.32; Frag. Len.           BBB b39; GMS 1041
           mrtYmh O1 1 1                                        5471 mrtxmync M                             o^' W
    5458 mrtym'k B, S                                                martu/oxmenc
                                       (oy> j^, ^y
         matoxme (mrtymk, mrt'xmk) =»mrdxmy,                         human, humane
           mrtym'k, mrtxmy(y), mrtym'y                               GMS 1254
         man, human, mankind
                                                                5472 mrtxmy ptxwyny C                   j£+*\ ij&^j*
          -JJfc. SCE 360; J>>kt SCE; VJ; BSTBL; STii; MD;            martoxme- patxwene ©ace.
             Frag. Lcn.; -kwy SCE 204, 319; VJ 76, 1464; pi.         killer of man
             -(i)kt, MDii; Frag. Len^ pi. ob. -»kty, VJ 395;         C2, 3R15
             ->kty, BSTBL, Vim. 118; Hen. Tales. 474.9;
             mrtxmykt STii 10.54, 7.5                           5473 mrtxmy(y) M, C         (u>> ^~> j->)->'>^~ <{°y
                                                                     martoxme (mrt'xmk) ©pi. -/; ob. pi. -ty
    5459 mrtym'kw  B =$ mrtynVk                                        =»mrtym}k, mrdxmy, mrtym'y


I
    5460 airtynVn B                                    jU^           man, person
         martaxman ©gen. pi.                                         GMS 129, 966; Hen. Tales. 473; BBB; STi; STii;
         men
                                                                       MSP; BSTi; C2, abl. voc. mrtxm\ ace. mrtxmw,
         VJ 1048; SCE 538; GMS 969, 1261
                                                                       C2, gloss; pi. mrtxm())yt, BBB 505; GMS 1256;
    5461 mrtym't =» mrtym*t                                            BSTi; BSTii: C2; KG 185; pi. ob. mrtxmyty, STi
    5462 mrtym'y B, S                                                  10, 12; Sund. AoFviii 1981 p216; C2, MSP b31,
                                      (j^ ^^ ^)f^
         martaxme (mrtymy) ©pi. -/; ob. pi. ~ty                        71, 75, 8b 101, 128; KG 4
           =»mrtxmy(y), mrtymk, mrtym*t                         5474 mrty                            (j>^ >^ j>)>j>
         man
                                                                     marti/I
                                                                       «*mrt}y (mrtyy) ©<OP martiya-, Yaghn. morti
         SCE; BSTBL; Tales. 476.2, 481.47; pi. -y/, VJ 835;
```


## [2026-09-07T16:22:26.068Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 335 -l 335 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg335 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


## [2026-09-07T16:22:27.499Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','ARY','IRN']:\n    print('==',k, json.dumps(d[k].get('scans'),ensure_ascii=False))\n\""
}
```


### [2026-09-07T16:22:28.031Z] TOOL RESULT

```
total 16304
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 12:22 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb      471 Sep  7 12:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 12:18 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


### [2026-09-07T16:22:29.413Z] TOOL RESULT

```
== BQT [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
== MON null
== ARY [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"}]
== IRN [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "first_printed": 1, "last_printed": 210, "pdf_offset": 11, "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"}]
```


## [2026-09-07T16:22:38.347Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg335.png"
}
```


### [2026-09-07T16:22:38.968Z] TOOL RESULT

```

```


## [2026-09-07T16:22:38.965Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T16:22:55.452Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 400 BQT_v1_pages.txt; echo; echo \"=== count pdfpage tags ===\"; grep -c \"\\[pdf page\" BQT_v1_pages.txt\necho \"=== search پژمرد in v1 ===\"; grep -n \"پژمرد\\|پژمري\\|پژمری\" BQT_v1_pages.txt | head"
}
```


### [2026-09-07T16:22:55.516Z] TOOL RESULT

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

=== count pdfpage tags ===
0
=== search پژمرد in v1 ===
7513:کاهی تازماند و گاهی پژمرده و سرو از این ها
17812:و پژمرده شد - وفراهم آمد - ویین‌چین کردید.
24126:آقتاب - و پژمرده ار از مس
24134:پبضان باش که پژمرده‌شدموفراهم آمده است؟
25511:۱ - مصحف‌پرمابه؛ رك : پرمابه و پرمابون . ۲ - اسم مفعول از پژمردن, رك : پژمردن .
25512:پزمرالدن و پزمرالیدی - بکسس اول و ضم سوم و فتح هشتم , متمدی پژمردن ‏
25540:پرمرده شدن- و پژمرده کردن- ودرهم آمیختن
```


## [2026-09-07T16:22:57.056Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\necho \"=== v4 مشیا ===\"; grep -n \"مشیا\\|مشیانه\\|مشيا\" BQT_v4_pages.txt | head\necho \"=== v4 مرمر ===\"; grep -n \"مرمر\" BQT_v4_pages.txt | head\necho \"=== v3 کیومرث ===\"; grep -n \"کیومرث\\|كيومرث\" BQT_v3_pages.txt | head"
}
```


### [2026-09-07T16:22:57.131Z] TOOL RESULT

```
=== v4 مشیا ===
3978:مشنج - بنم اول و فتح ثانی و سکون مشیا ۷ - بنتح اول بروزن اشیا » بلفت
3996:و نیز مشیا ه اوستا ۸/]2810[/2 ( در کانپا 83388128 و 13287612 ) بمعنی‌فناپذیرء در گذشتنی »
3997:مردم و اضان آمده ( رك : مرد » مردم ) . در بندهشن پهلوی « مشیا » بمنزلهٌ 9آدم» و مشیوی
3998:2/129۵ بمنزلةٌ «حوا» درنزد اقوام سامی‌است « بشتها ۱:صس ۷۰-۹۹ و مشیوئی را «مشیانه»
5930:برها میداشتند . بقول بندهشن« مشیا > و مشیانه » (آدم وحوای آربائیان ) درچنین روزی تولد
=== v4 مرمر ===
3087:مرمر - بفتح دو میم » از بونانی 81۵۳78۳08 » عریی و ترکی « مرمر» « ژاپاس
3453:کته دا ۹ ۰ افتد ‎٩‏ - و خرمگی را دز مرمرژ میگوین دکه
6580:«میمه > نام دار دکه ممادن مرمرآن معروفت «کیهان . جغراقیای سیاسی ص2۰۵ > « ميمك >
11423:کند پست رستم بنیرو ترا هلاك‌آورد بی کمان مرمرا ...
12697:آب انگور و آب تیلوفل مرمرا از عبیر ومعك بدل.
13316:ازین آژغان پاک کن مرمرا همه آفرین از آفرینش ترا . »
18990:‎٩‏ - بپترین جامه‌ای بود هنگفت مرمرا اوستاد چوئین گفت.
20935:اففاق ومصلحت هم بنظر آمده است . رهر۸ - بنتح اول بروزن‌مرمر» بممتی
22402:چوکوه کوه فرو ربخت آهن و مرمر
=== v3 کیومرث ===
39858:‎ee‏ ۴ جزو اول ‎pl‏ نام «گی» <۳ کیه) است نه «کی» ۰ رلك: کیومرث ۰
45846:کیومرث را « کرشاه» فامیده‌اند وحمز؛ اسفهالی این کلمه را به
45849:کیومرث در کوه ‎ater jee‏ بدیین مناسبت اورا «گرشاه» گفتند .
45863:کوبند کیومرث آدم علیه‌اللام است و چون او
45866:زمین پادشاهی کرد کیومرث بود باین‌نام امیدند-
45884:‎٩‏ - رل :گیومرث » کیومرث .
```


## [2026-09-07T16:23:08.168Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\ndef pageof(path, lines, off):\n    t=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    tags=[(i+1,int(m.group(1))) for i,l in enumerate(t) if (m:=re.search(r'\\[pdf page (\\d+)\\]',l))]\n    print(path,'tags:',len(tags), tags[:3])\n    for ln in lines:\n        cur=None\n        for i,p in tags:\n            if i<=ln: cur=p\n            else: break\n        print('  line',ln,'-> pdf page',cur,'printed',None if cur is None else cur+off)\npageof('BQT_v4_pages.txt',[3087,3978,3996,5930],1917)\npageof('BQT_v3_pages.txt',[45846,45863,39858],1205)\nEOF"
}
```


### [2026-09-07T16:23:09.483Z] TOOL RESULT

```
BQT_v4_pages.txt tags: 553 [(1, 1), (2, 2), (23, 3)]
  line 3087 -> pdf page 79 printed 1996
  line 3978 -> pdf page 100 printed 2017
  line 3996 -> pdf page 100 printed 2017
  line 5930 -> pdf page 149 printed 2066
BQT_v3_pages.txt tags: 721 [(1, 1), (3, 2), (24, 3)]
  line 45846 -> pdf page 623 printed 1828
  line 45863 -> pdf page 624 printed 1829
  line 39858 -> pdf page 546 printed 1751
```


## [2026-09-07T16:23:18.327Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\ndef show(path,pdfpages,off,maxlines=12):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    blocks=re.split(r'(?=\\[pdf page \\d+\\])',t)\n    for b in blocks:\n        m=re.match(r'\\[pdf page (\\d+)\\]',b)\n        if m and int(m.group(1)) in pdfpages:\n            print('=== printed',int(m.group(1))+off)\n            print('\\n'.join(b.split('\\n')[:maxlines]))\nshow('BQT_v4_pages.txt',[17,65,66,67,68,69],1917,10)\nshow('BQT_v3_pages.txt',[667],1205,10)\nEOF"
}
```


### [2026-09-07T16:23:19.648Z] TOOL RESULT

```
=== printed 1934
[pdf page 17]
مادر آب وآش -۱۹۳
مادر آب و آتش - بکسر راق ‏ | خوانند . خوردن‌آن قوت باه دهد .
قرشت » کنایه ا زگربه کنندة بسوز است پمنی مادده ؟ - بکر ثاك و فتح رابع,نام
شخص ی که از روی سو زکربه کند . آولایتی است در عغرب زمین -
مادر باع - بکر رای قرشت (۰)۱ ماد‌ندر ۴ » با نون ودال ایجدیروزن
کنایه از زمین است که بعربی ار کوبند ‎٩‏ - | غارتگر , مغفف مادر اندر است که زن پدر
وباغ را هم کفته‌اند بطریق اضافه , باعتبار اشجار | باشد .3۶
و اثمار پمتی درختها و میوه‌ها - ماد - بنکون رای قرشت. معروف‌است
مادردخت جم دال ابجد وسکون | که بزبان عرمی حیه کوبند ۴ - و مخفف مادر
=== printed 1982
[pdf page 65]
مرجان_پرورده -۱۹۸۲
گوبند از دزیا میروید ‎٩‏ - و مروارید ریژه را بنظرآهده است .
نیز کوبند ۰ 8 مرجمك ۳ « بروزن مردمك,غله‌است
مرجان‌پروارده- ورهار :را که بعربی عدس خوانندش .
کنایه از لب ممشوق رن مرخُشه - باخاوشین
ومحبوب‌است- و کنایه ۳ قطه دار بر وزن اقمشه » در
از شراب انگوری هم 09 با فرهنگه ۴ بمعتی سخن باشد
هست .. ۰ ط که کلام است. ودرجایی دیگر ۰
مرجاده()- 2 : بر وزن طبقچه بمعنی نحس
=== printed 1983
[pdf page 66]
۱۹۸۳۳ مرداسفرمٍ

تالاب و استخر وآبگیر عمیق پرعرض و طول را | واين جشن را جشن لیلوف خوانند ودرین روزهی

گویند . حاجتی از پادشاه خواستی(٩)‏ البته روا شدی .3
مردا3 ۱ - بنم اول بر وزن خرداد , مر دار خانه - خانه ای راگویند در

نام فرشته ایست موکل بر قصل زمستان و ندبیر بازی نرد که مغرء در آن خانه در ششدر باهقدر

=== printed 1984
[pdf page 67]
مرداسنگه -۱۹۸2-

مرداسنگ ۱ « یم اول » بمعنی | خوردن آن با شراب کزندکی جانوراترا نافع
مردارستگه است, وآن جوهری باش د که ازسرب | است .
سازند ودرمرهم‌ها یکاربرند. ومعرب آن مرداسنج مرد هر - باکاف‌فارسی‌بروزن سردسیر.
است .8 سلاحی باش د کج مانند چوکان 8 .

مردان علوی - بتم عنبی‌شد۲ . هرد گیر آن ۱ - نام جدنی است که
کنایه ازهفت کو کب است که بعریی سبعةٌ سیاره مفان بعنی آتش پرستان در پنج روز آخر
=== printed 1985
[pdf page 68]
۱۹۸۰ مردمه
مر۸۵ ۱ - يك شخص واحد را کوبند روزی بمیرد و طریق‌کندن آن چنان است که
از آدمی ۴ و ترجمهٌ اسان است » و مرومان | اطرافآنراخالی کنند چنانکه باندك زور ی کندء
جمع آنت و مردمك تصفیرآن ۴ . شود و رسمانی بر آن
مردم آهنگ - بسمنی مردم هش بندند و سر ریسمان‌را ۵ بط
ومردم انداز باشد۴ - وسلاح کجی را نی زکوبند | بر کمرسگه‌نازیمحکم 4 ی
مانند چوکان وآ ترا مردکیر هم‌خوانند ومعرب [ سازند وشکاری در پیش منک
آن مردم‌آهنج است . آیسکه رهاکنندچون ‏ 8۲ ‎٩‏ درا
5 آدم زاده سا که امه ۱ ۸
=== printed 1986
[pdf page 69]
مردوی -وه۱۹-
عربان اسان المین خواتد ‎٩.‏ بماند - و شخصیرا نیز کوبند که ست وفرومایه
مردوی - بروزن اضوی کندای | کاد و بیکار و «یچ کار اشد وازوکاری برنیاید.
شامی راگویند - مرده سنگب ؟ - بنم اول و فتح سین
مرده‌دی! - با رای بی‌نقطه(۱)پروزن بی نقطه » بمعنی مرداسنگه ‎)٩(‏ است و آن
-فره‌چی.. مال و اسپابیراگویند که از کی بسن | جوهری باشد که ازسرب سازند . زخمها راعلاج
از مردن مانده باشد وبعربی میرأت خوانند. کند .
مرده دیگب ؟ - بازیادتی کاف,بممنی هرن ۴ - بفتح اول وسکون ای وزای
مرده ری باش دکه مال ومیرائی است که ازکی | نقطه دار » زمین را کویند 9 - و زمهنی را نیز
=== printed 1872
[pdf page 667]
کیسودار هرا

و مردم عامیرا کویند #۰
گیل‌دارگ * - بکس اول » چوبکی
باشد ‎Le‏ رنگ و ‎VAT‏ بماحل دریای خزر
يا پند و آنرا تر وماده میباشد ‎als rise‏ را ناف
است که کرم شکم باشد و معرب | ننجیل‌دارو است .
گیلك ۲ © باتانی‌مجهول‌بروزن میلك.
پزبان ‎OAT‏ - مردم عامی و روستایی و رعیت را
```


## [2026-09-07T16:23:35.920Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=\\[pdf page \\d+\\])',t)\nfor b in blocks:\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if not m: continue\n    p=int(m.group(1))+1917\n    for kw in ['مرگ','مردن','امرداد','مرداد']:\n        if kw in b:\n            # print first line (header) and the matching line\n            ls=[l for l in b.split('\\n') if kw in l]\n            print(p, kw, '|', b.split('\\n')[1][:60],'||', ls[0][:110])\nEOF"
}
```


### [2026-09-07T16:23:37.187Z] TOOL RESULT

```
1921 مرگ | ديباچة مجلد چهادم || بال ۱۰۹۳ هجری قمرگه یمنی يك‌سال - یاکمتر- پس ازتألیف کتاب,
1929 مرگ | ۰ || اول بطبم رسیده). بمیشی. ۱۲۲۳ یزدگردی < ۱۲۷۰هجری قمرگ.
1934 مردن | مادر آب وآش -۱۹۳ || بمعنی زبانکار وتباه کننده یکی است » ازمصدر 13387 اوستایی و پارسی باستان بمعنی مردن «فاب
1935 مردن | -۱۹۳۰- مارامیند || ( بیاد داشتن » از برخواندن » برشمردن ) است «* هرمزدنامه ص۳۸۶ +
1939 مردن | -۱۹۳۹- : ماژوستان || ۱ مار امار * آمار (.م.) از ربشهٌ - 13387 (بخاطر آوردن » شمردن) ر :اسشق
1978 مردن | مدیتا -۱۹۷۸- || ( عدد ) ر4 : اسشق ‎٩۹۷۱‏ . در اوستا - ۲138۳ بمعنی بیادداشتن و از برخواندن و برشمردن‌است.
1979 مردن | -۱۹۷۹- مراش || سراج‌آرد : «فوسی کوید که این حابی‌است که جولاهان در شمردن تارهای کربای کنند و گوبند
1981 مرگ | -۱۹۸۱- مرجان || ( مرده ) + ۴ - رك : مرداسنگه » مرده سنگه . رك : مرگو.
1982 مردن | مرجان_پرورده -۱۹۸۲ || ازربشه 3387 ( مردن ) [ ر4: مردن ] درگانها 1718۳318 و 13328802 ( ازهمان ريشه ) بعمنی
1983 مردن | ۱۹۸۳۳ مرداسفرمٍ || گذشتنی ونیست شدنی و مردم ) از مصدر 3387 اوستایی و پارسی باستان پمعنی مردن . جزعدوم
1983 امرداد | ۱۹۸۳۳ مرداسفرمٍ || ۱ - اسح « امرداد » است. در اوستا ۸۸7۳36۳6121 مرکب از دو جزه : جزه اول خود
1983 مرداد | ۱۹۸۳۳ مرداسفرمٍ || امور ومصالح ی که در ماه مرداد وروز مرداد واقع | افتد و نتواند بیرون آید () .
1986 مردن | مردوی -وه۱۹- || از مردن مانده باشد وبعربی میرأت خوانند. کند .
1995 مردن | -۱۹۹۰- م رکه || ( سم . زهر ) ؛ ازربشهٌ -1332۳ ( مردن ) * اسشق ۹۷۷ *.
1996 مرگ | مرکا م رکه -۱۹۹۹- || مرگام رک ۱ بفتح هر دو میم زاج زرد و بعرپی رهج‌الفار وسم‌الفار وتراب‌الهالك
2032 مردن | چوپ || مردن خوانند بفتح میم ودال ؛ و باغین نقطه‌دار | ایشان واورا ملوکا هم میگوبند ۴ - و بلفت زند
2057 مردن | و موبه || بمعنی شمردن زر وچیز دیگر باشد ۰ | خرسندی » بمعنی هنرءندی وسنمت گری باشد.
2067 مردن | سنهنها مهرملم || آنروزرا مپرکان نام کردند۱ و معنی آن مردن | است از موسیقی که‌آن را كوچك خوانند .
2072 مردن | میاسئو اسف مزا || ازحاب کردن وشمردن باشد بعنی‌مشمار وحصاب میان سرایی نگ < نوعی از انگور
2171 مردن | -۹۱۷۱- اموله || استی 23832708 , 8180218 ( حاب کردن » شمردن ) » سربکلی » شغنی 670-/[881738
2217 مردن | -۲۱۷-< حبوها || ( بمنی‌مار ‏ -1332۳ بمعنی شمردن ) است . آقای پورداود در شرح کلمه « مار "مر ( شفار ,
2238 مردن | بواد ۲۳۸ || است ی خود را ودیگران را خرد شمردن. غنیدن است ۹۴.
2318 مردن | بیان ششم || شمردن وخوب نداستن باشد - وبضم‌اول» بمهنی [ لجام وسیته بند و غیره ۷ - وجم‌اول بمعنی‌ترس
2362 مردن | بیان چهاردهم || هماد ؟ بفنح اول بروزنجماد.یمعنی | اندازه باشد - و حاب را ای ز گویند که شمردن
2394 مردن | هوشاز -۳۹۸- || (نامردنی, جاوید) «اسشق ۱۱۱۲ :
2408 مردن | هیگل نها || هیکل بحتی » کنابه ازمردن و وفات باشغه را گویند وآن پرنده‌ایست شکاری کوچکتر
```


## [2026-09-07T16:23:53.840Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=\\[pdf page \\d+\\])',t)\nfor b in blocks:\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if m and int(m.group(1)) in (622,623,624,625,667,668):\n        ls=b.split('\\n')\n        print('pdf',m.group(1),'printed(off1205)',int(m.group(1))+1205)\n        print('  ',ls[1][:80] if len(ls)>1 else '')\n        print('  ',ls[2][:80] if len(ls)>2 else '')\n        # find kiyumars lines\n        for l in ls:\n            if 'کیومرث' in l or 'گیومرث' in l:\n                print('   >>',l[:120])\nEOF"
}
```


### [2026-09-07T16:23:55.168Z] TOOL RESULT

```
pdf 622 printed(off1205) 1827
   ۱۲
   
pdf 623 printed(off1205) 1828
   کلت ‎AAT‏
   ‏گیل ‎pe - Ree‏ اول. زنگیرا گویشد
   >> کیومرث را « کرشاه» فامیده‌اند وحمز؛ اسفهالی این کلمه را به
   >> کیومرث در کوه ‎ater jee‏ بدیین مناسبت اورا «گرشاه» گفتند .
pdf 624 printed(off1205) 1829
   NAY
   
   >> کوبند کیومرث آدم علیه‌اللام است و چون او
   >> زمین پادشاهی کرد کیومرث بود باین‌نام امیدند-
   >> ‎٩‏ - رل :گیومرث » کیومرث .
pdf 625 printed(off1205) 1830
   ‎and‏ اما
   
pdf 667 printed(off1205) 1872
   کیسودار هرا
   
pdf 668 printed(off1205) 1873
   ۱ یله ۱ © بروزن حیله.نام جابی‌ومقامی
```


## [2026-09-07T16:24:13.406Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 300 python3 tools/ref_page.py BQT:1872 --image 2>&1 | head -40"
}
```


## [2026-09-07T16:24:15.031Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('formfeeds:', t.count('\\f'))\n# leaf containing line 25511\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i==25511: print('line 25511 leaf',leaf)\n    leaf+=l.count('\\f')\nprint('total leaves',leaf)\nprint('\\n'.join(lines[25495:25560]))\nEOF"
}
```


### [2026-09-07T16:24:21.441Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 667; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1872.png
REF: BQT:1872  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 667  OCR-lang: fas

کیودار -۱۸۷۰-
زنان است .#۴ و مردم عامیراکوبند .*
گیسو داد ۱ - با دال ابجد بر وزن گیل‌دارو ‎٩‏ - بکر اول . چوبکی
نیکوکار , معروف است ۴ - و کنایه از سید ۴ | باشد سیاه رنگه و آنر| بساحل دریای خزر
ومولازاده و پیرزاده هم هت . با پند و آنرا تر وماده میباشد «کدو وانه را تافع
گیل ؟ - با انی مجهول بروزن فیل ۰ |[ است که کرم شکم باشد و معرب آك چیل‌دارو ات .
کیلان را کوبند و آن ولایتی باشد معروف از گيلك ۱ « بائانی‌مجهول‌بروزن مبلك.
تبرستان - و بزبان کیلانی » رعیت و روستایی | بزبان کیلان مردم عامی و روستایی و رعیت را

۱- از : کیسول دار ( دارنده ). ۴ -بعنی صاح بکیسو .

۴ - بمناسبت آلکه در قدیم علوبان کیو داشتند . رك : کیسو .

۴ - پهلوی [غ03 ( رك : فهرست مارکوارت . شهرستانهای ابران » و رك : کربتنن.
ساسان ص ۲۰۹) بقوم ساکن کیلان اطلاق شده . رك :گیلان . - از :گیل (کیلان)
+ دارو ؛ لغة داروبی که درکنار دربای کیلان ( بحر خزر ) روید ( برهان در شرح : سغیر ) ۰
معرب آن جیل دارو . ‎٩‏ - درکیلکی اةاع ( اهلکیلان کیلانی ) فن :کیله » و
کیلکی لهجهٌ مردم کیلان راکویند .

0 یحو - بکر اول و ضم سوم ۳ کیس (۸.م.) از اوستایی 82688 ( رك :کیس ):
در اوراق مانوی بپهلوی 888۷8 ( کلاله : طرء ) ۰ 815۷۷80۷7 ( با عوی مجعد ) . آرمنی
7۳ ر(83. ۶ با , 17 , 8505 و...صقند۳ ۸1:04416 ۱۶ اقلا ۸ موصندصصعتن0
در پپلوی 888۵۳ «اوئوالا ۳۸۳ » ؛ موی بلند که ازپشت کردن تجاوز کند ( جمع آن؛ کیسوان,
کیسوها ) : ۶« شیادی کیسوان بافت بسورت علوبان ... » «کلستان ص ۵۳ >.

#لان - بکس اول از : گیل (وم.) + آن (پوند مکان) . پپلوی ابا 6 یعمنی
مملکت کیل ( 6781 ) ها . در نزد بودانیان 636186 « داثرة الممارف اسلام » . در اوستا
نام ناحیتی صورت ۷87612 آمده و خاورشناسان در تعیب محل آن اختلاف دارند . طیق سنت
آن . همان مملکت « پتشخوا رکر» ( طبرستان وکیلان ) است رك : پورداود . بشتها ج ۷۱
۱۹۴۱۸۱ وج اص ۷۵ متن و ح۱ . اندرآی همین ۵ ورنه > را ریشهٌ نام «کیلان»
دانته » ولی استاد بنونیست (درمذا کرء شفاهی) این حدی را رد کرده‌اند . چه ۷8 و ۷1 زبانهای
قدیم در فارسی به 80 و 81 تبدیل شود مانند وبشتاسی ۳ کشتاسپ » وراز < کراز » وبیستر -
کستر ؛ ولایت کیلان از ۳۹ درجه او ۲۸ دقیقه تا ۳۸ درجه و ۱۱ دقيقةٌ اعرض شمالی و از 4۸
درجه و44 دقیقه تا ۵*۰ درجه و۳۲ دقيقهٌ طول شرقی واقع شده . ازشمال محدود است ببحرخزر
و از مشرق بمازسران و از جنوب بقزوین وخصه و از مغرب بآذربایجان. طول‌آن ازشمالغربی
بجنوب شرفی ۲۲۵ و عرض‌آن از ۲۵ تا ۱۰۵ کیلومتر تغییر میکند .گیلان شامل نواحی ذیل
```


### [2026-09-07T16:24:22.741Z] TOOL RESULT

```
formfeeds: 776
line 25511 leaf 624
total leaves 776
3 اندوهگین و بی رونق باشد - و بمعنی روی
بخشکی آورده و نرنجیده ودرهم کشیده شده هم
فست ۷
بر مر بده ۲ بکسراول و رای فرشت
بتحتالی رسیده و فتح دال , بمعنی برزمرده باشد
کهغمناك واندوهگین وافرده گردیده و بی‌رواق
شده است 5
فزن - بر وزن و معنی زغن است که
غلیواج باشد.
۱ - شود دل بحرف فرآن به نشود بز به جزیژی فربه. سنابی غزنوی. «لفت نامه» .
۳۳ بر کاله, وظاهراً همین صورت صحیح است. «لخغت نامه». ‏ و
۴ - پارسی باستان_ 00202 ۵ + تافقا2 ؛ پپلوی 25۳15020 ( بازند 0ناعدم) ,
هندی باستانی ۳20 ۲+ 0224 (مخالت کردن » اعتراض کردن ) «اسشق ۳۱۷». رك: بشیمان.
ه‌ بت آندرین خانه بوده‌ام عپمان کرده ام شاد اژو دل بزعان ِ
عتصری بلخی. «لفت ناهه؟.
۱ - مصحف‌پرمابه؛ رك : پرمابه و پرمابون . ۲ - اسم مفعول از پژمردن, رك : پژمردن .
پزمرالدن و پزمرالیدی - بکسس اول و ضم سوم و فتح هشتم , متمدی پژمردن ‏
پژُمرده کردن ۰ اذبال :
همی پژمرانه رخ ارغوان کند نیره دبدار روشن روان .
فردوسی طوسی. «لغت نامد» , رك: بزمردن.
* پزمر دن و پزمریدن - بکسر اول و ضم سوم و فتح پنجم » پارسی باستان أکقا08 ( اوستا
0 )+--8031. پز ظاهرا اشتبا‌فدمی ا-ت بجای‌یژ 0120 . ویزدر پژوهیدن ویژمان هم
دیده میشود «اسشق ۰۳۱۳ درهندی باستان ۵۵۷۱ ( سفت #دن » سحی شدن) » ارمنی
۲ - 2 با 10[۲ - 2 5 ۲۱۴1۲0 -2 (یحی شدن) «یب رکه ۲۳۸ :۰ ۷۵۲۵8۵۶).  .‏
بقبه اسف ۳۵٩‏
کنندچنانك نن‌مردم مر پزشکی‌را وچنانك اندازه مرهندسد را...» «دانشنامه ی۵۷*.
۵ پزیدن - بفتح اول وچهارم. پختن («.م) - پخته‌شدن:
هرمیوم که ذرباغ جبان‌بد همه پخته‌است ای غورة چون سنگه تخواهی‌توزبدن.
مولوی بلخی رومی . ذلفت نامه * .
(برهان قاطع‌هه)ات
برخست باشد ۰ و آن کیاهی است خود روی
و خوشبوی مانند اسفناج که داخل آش کنند
چون در کوه و کنبذ باواز بلند چیزی بگویند
در جوا ب‌همانرا نو ند » وآن‌را بمرمی‌صد اخو انند.
یر ول - بروزن‌قبول, کمب پا واسشخوان
۱ شتالنگه را کوش وستان زنان راهم گفتهاند-
و گلوله‌ا ی که طفلان بدان بازی کنند - وبمعنی
فندق هم هست و آن را هفزی باشد که بخورند
پژولش ۲ ۰ بکر اول بر وزن
نکوهش , بمعنی پژهرده و پربشان و درهم
شده باشد .
پژ و لیف ۴ - بر وزن نکوهید » یعنی
عزمرده شد وآب وئاب در وی نماند .
بر و لیدن بکراول‌بروزن‌نکوهیدن:
پرمرده شدن- و پژمرده کردن- ودرهم آمیختن
ویرثان کردیدن بود ۵ - و بمعنی تداخل هم
آمده‌است که درهم‌شدن‌باشد. وباین‌معنی بفتح‌اول
هم گفته‌اند وصیحت کردن - وجم‌تجو وبازیری
(۱) خم۳ : گزند .
و تفحص نمودن را نیز گویند .
لیدم ۴
و له " - بر وزن تکوهیده »
یز مرده شده ونرم گردیده شدت و بی‌اب و تاب
شدم و ابترشده- وصیحت کرده شدموبازیری
کرده شده باشد .
بزوم هتح اول بر وزث سموم ه
فقبر و دروش و کدا و خوار و ی اعشبار را
ند
پژو مان - بايم بر رزن خموشان ؛
جمعم پژوم ات نی فقیران و درویشان
و کدابان! .
فر و لاس ح بروزن دربند » چوبی باشد
که درپس در گذارند تادر کشوده نگردد- وچوب
کازران را نیز گویند ۷ - و کنابه از مردم
پس درنشین ودیوت باشد, و باین معنی بفتح اود
```


## [2026-09-07T16:25:00.115Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=\\[pdf page (\\d+)\\])',t)\n# simpler\nfor b in re.split(r'(?=\\[pdf page \\d+\\])',t):\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if not m: continue\n    p=int(m.group(1)); pr=p+1205\n    if 'گیومرث' in b or 'کیومرث' in b:\n        hdr=[l for l in b.split('\\n')[1:4]]\n        print('pdf',p,'printed',pr,'|',' / '.join(x[:40] for x in hdr))\n        for l in b.split('\\n'):\n            if 'گیومرث' in l or 'کیومرث' in l: print('    >',l[:130])\nEOF"
}
```


### [2026-09-07T16:25:01.396Z] TOOL RESULT

```
pdf 546 printed 1751 | uw -۱۷- /  / پادشاهان بزرکتر باشد و بعربی ملك الملوك 
    > ‎ee‏ ۴ جزو اول ‎pl‏ نام «گی» <۳ کیه) است نه «کی» ۰ رلك: کیومرث ۰
pdf 557 printed 1762 | ‎“Ss‏ « پروزن سینه » بمعئی‌یمپری / و عداوت و آزارکیرا ‎Jo»‏ پوشیده داشتن / باشد .
    > ۰ ‏رد :گیومرث‎ ۳
pdf 623 printed 1828 | کلت ‎AAT‏ / ‏گیل ‎pe - Ree‏ اول. زنگیرا گویشد / که بر روی سنگه پیدا میشود ‎on yt,‏
    > کیومرث را « کرشاه» فامیده‌اند وحمز؛ اسفهالی این کلمه را به
    > کیومرث در کوه ‎ater jee‏ بدیین مناسبت اورا «گرشاه» گفتند .
pdf 624 printed 1829 | NAY /  / کیومرت را ۱ خوانند» ووجه تسمبه‌اش‌آادت
    > کوبند کیومرث آدم علیه‌اللام است و چون او
    > زمین پادشاهی کرد کیومرث بود باین‌نام امیدند-
    > ‎٩‏ - رل :گیومرث » کیومرث .
```


## [2026-09-07T16:25:24.314Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nfor b in re.split(r'(?=\\[pdf page \\d+\\])',t):\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if m and int(m.group(1)) in (668,669,670):\n        print('=== printed',int(m.group(1))+1205)\n        print(b[:1500])\nEOF"
}
```


### [2026-09-07T16:25:25.653Z] TOOL RESULT

```
=== printed 1873
[pdf page 668]
۱ یله ۱ © بروزن حیله.نام جابی‌ومقامی

‎Gh‏ = بر وزن فیلی » منسوب یکیل
راگوبند ۴ - و نام طاینه‌ای هم حست ازتر ‎OS‏
‏- و بعت ی کون دکیلی طایقه ای باشند. از کليم
پوشان ۴ .

‏گیهیا ؟ - بروزن سیمیا . بمعنی‌ریماز
است که نوعی از جامه و پارچة نفیس لطیف
باشد . ۰

‏گیی * ۰ بر وزن سین » بمعتی صاحب
وخداوند باشد چون با کلمه‌ای تر کیب کنندرسنی
درآ خر آن کلمه در آورند همجوغمگن‌وشرمگن-
و ‎ines‏ سفت هم‌هست هرگاه با واصف م رکب
سازند ؛ وبعضی کویند ‎gine,‏ پرامت که درمقابل
خالی ‎ath‏ چه کین در اصل آ کین بوده ومعنی
آن پر از غم وپر از شرم باشد .

‎Ga?‏ ه بر وزن سینه » مخفف آبگینه

‏کبرگان
‏است که‌آینه ‎Vash‏ .

‏گیو بکس اول و انی مجهول‌بروزن
دیو » نام پ سکودرز است که کیضرو را بعد از
‎JL cin‏ دید واز تر کستان ‎pl‏ آوردسویفتح
اول بروزن عمو؛ بمعنی کوبا باشد که‌سخنکننده
است ۷ - و زبافرا نیز کویند که بعربی ‎OS‏
‏خوانند ۸ - و بمعنی ‎Fatt‏ و ‎We‏ هم استعمال

‏میشود .

‏گیور = پروزن زیور » در لغت بمعنی
نقل کننده و سخن رالنده و قصه خوان و افنانه
کوی باشد - و در اصطلاح بمعنی حس مشترله
‎٩ ot‏ و آن اول فوتی است مرتب در مقدم
تجوف دماغ و اجتماع صور محسوسات پیش او
باشد که اکر او نباشد ما حکم توانيم کرد که
این سفید است وآن ‎ale‏ وین ساکن است‌وآن

‏متحرلك .
گی و گان "اه با ‎gt‏ مجهول و کاف
فارسی بروزن میهمان » نام ‎lle‏ است ایرانی

‏۱ - درکیلکی ‎tla [mard‏ ( روستایی + رعیت ) گویند . - « کیله » بفهوم ‎te‏

‏و مقامی خاص ‎aL‏ نشد , اما « گیله دولاب » موضعی است در طالش دولاب « کیهان . جفرافیای
میاسی ص۲۷۸ » و رگ :گیل دولاب « فرهنکه جفرافیابی ابران . ستاد ارتشج ۲ ص ۲45 ۰
۴ - از :گیل ‎CAC)‏ ( پسوند تبت ).

=== printed 1874
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
‎
=== printed 1875
[pdf page 670]
از کناب ‎ob,‏ قاطع درعرف لام با عروف تهجی ‎se‏
‏بر بیست و دو بیان و محثوی بر سبصد و هشتاد و شش
لت و ‎elf‏

بیان اول

در لام با الف مشتمل بر هفتاد و نه ‎cab‏ و کنایت

۶ لاس ‎NTs Vegan‏ وهرزه کوبی
و پر کوبی باشد ۱ - و در عریی بمعنی نه است

که تقیضآری باشد - وبمعنی نفی‌هم‌هست‌همچو
۷ اله الا ال . 1

وتان ۴ .

ats ‏با لامبروزن پا برجاه‎ - TV YY
‏تو پرتو و ته بر نه باشد - و نام نوعی از حلوا‎
- ‏هم هست‎

لاب = پروژن باب » ‎oth‏ بونانیآفتاب
را کوبند ؟- ونام‌پسرادری‌علیه‌السلام هم‌هست ‎٩۴‏
‏و بسی کویند نام حکیمی است که اصطرلاب را
او وضع کرده است ؛ و بسی دیگر گویند نام
بسن اسطر است » و اسطر نم پادشاهی بوده از

لا ۴ 2 بروزن تابه. بمعنی سخن‌باند

- و اظهار اخلاس با نیاز تمام را کویند- وبمعنی
چرب زبانی و چاپلوسی و تملق و ‎ID‏ وعجز

و یاز و خواهش هم‌هست ۵ - و فریب و بازی
۵ ل ( لام ) - حرف بیست و هفتم از الفبای فارسی وحرف بیست وسوم آزالفبای عربی
‎(on!)‏ و در حاب جمل ‎onl Soe WIT‏ حرف به «ر * ( رلك : ص بط مقدمهةٌ ملف )

بدل شود. ۱ ۰۷۰ اسم فاعل مرخم ‎col‏ در کلمات مر کب: ‎Vege‏ ژاژلا. رك:لاییدن.
۳ _ فقه‌اللَةٌ عامیانه. رك : اسطرلاب . ۴ - از: لا (طبغه) ‎H‏ بر(بمعنی‌علی‌عربی)
+۷ (طبقه) . ۴ « لاف ‎gal.‏ ع 1818. 18۳۵(خودستابی ۰ ‎SY) fuk ۰ GG‏

زن ) ) از ‎our‏ 120 ۵ . رك : هوبشمان ‎Mov‏ و رك : اسشق ‎tat‏ : کردی 1260
( استدعا « درخواست ) « ژابا س ۳۷۵ » ورك : لابیدن .
© - تواورا کنیلابه فردا به پیش فدا داری او را تن و جان خوش .
فردوسی طوسی « لفت نامه > .
```


## [2026-09-07T16:25:52.761Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON_part2 مرمر ===\"; grep -n -o \".\\{0,120\\}مرمر.\\{0,160\\}\" MON_part2.txt | head -6\necho \"=== MON_part2 مشیانه ===\"; grep -n -o \".\\{0,80\\}مشیانه.\\{0,140\\}\" MON_part2.txt | head -4\necho \"=== MON_part2 مل ===\"; grep -n -o \"^.\\{0,40\\}مُل.\\{0,140\\}\" MON_part2.txt | head -6\necho \"=== LEW marmor ===\"; grep -n \"marmor\" LEW_1910.txt | head -5\necho \"=== LAT marmor ===\"; grep -n \"marmor\" LAT.txt | head -5"
}
```


## [2026-09-07T16:25:55.290Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index MARD/MER ===\"; grep -n -i \"^MARD\\|^MER\\|MARMAR\\|MORTAL\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== HUB mard/murdan ===\"; grep -n -i \"marmar\\|mard\\b\" HUB.txt | head -10\necho \"=== SYN DIE / MAN ===\"; grep -n \"^4\\.7[0-9]\\|DIE (vb.)\\|4.75 DIE\" SYN.txt | head -10"
}
```


### [2026-09-07T16:26:00.712Z] TOOL RESULT

```
=== MON_part2 مرمر ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,160}
                          \___exceeds complexity limits


=== MON_part2 مشیانه ===
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,140}
exceeds complexity limits___/


=== MON_part2 مل ===
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


=== LEW marmor ===
13902:léso I 763, 766 léte, léetojo I 771 léteba (ksl.) I 771 lécha I 813 léjo I 764 lubste I 793 ljubo ... yubol793 Tubs I 793 hudoje I 791 lute [791 lego, lesti I 778 ledvye I 832 -leko, -lesti I 761 lesta (ksl.) I 783 leéo, lecatt I 745 loge I 828 loka I 745 losta I 757 loéo, -it1 I 743 magulitt se (skr.- ksl.) JZ 12 mato, mazati II 3 malo II 20 manetyja (ksl.) LL 33 manu, man (r.- ksl.) IZ 33 mara (r.-ksl.) IT 33 marmore (ksl.) II 42 maslo IT 3 mast II 3 materostvo IT 51 mati IL 50 medeo IT 59 mezda, mezdu II 58 meljo, mléti II 105 mene II $4 meto, mestt II 48, 81, 82, 83 mt IT 85 mighvs (s.-Kksl.) IT 86
=== LAT marmor ===
6250:au neutre comme les noms de matiere en latin, cf. marmor, ■plumbum, etc.
7752:brittaneum (britaniu *): deambulatorium marmoratum (Gloss.). De¬
18223:Sbur eat neutre coaae lea noas de aatifere: aurum, argentum, marmor,
36618:marmor, -oris n.: marbre; et obj et de marbre (statue, etc.) ou
36622:Derives: marmoreus; marmorosus; marmorarius; marmoratus, d'ou marmoro,
```


### [2026-09-07T16:26:00.787Z] TOOL RESULT

```
=== ARY latin index MARD/MER ===
1004:Merry Mebojo ne cella ibe pst Syesh gad Fabelabe 5»
2604:[MORTAL tee lyr |
2611:RAMAT: 45]: IMMORTALIS AAATINY yg 48
11126:MERETI LITHUANIAN) gi) (KURDISH) «52,8
13587:BARNHART: (MORTAL) 679 MERD, MER KURDISH) 52,5 |
13591:ONIONS: (MORTAL) 591 MARD ARMENIAN) |)
13593:MALLORY: 49 MORTALIS ALATIN) 5y3V
13594:Y4ar igh db, MORTAL (SY jIENGLISH) (gS!
13666:MER, MEIRTA HITTITE) ean AITALIAN) gist!
13674:BARNHART: (MORTAL) 679 (PORTUGUESE) Jai 4 que
13689:MARMOR NORWEGIAN) (53, MARMAR ARMENIAN) gs
13690:MARMER (DUTCH) giche MARMAROS GREEK) gli
13706:MARMAROS (gly so5ly 1 A305 19 59 cu! PS oJ Stew OL a aly Say
13848:MERG (SWEDISH) 3 yo MAGHZA HAFGHANI) (3.4) git
13850:MERG DUTCH) sacle MAJJAN (SANSKRIT) 2 Sie
14012:MERIEN BRETON) sin -MICA (FORMICA) ALATIN) ys
=== HUB mard/murdan ===
2172:farzcLna (= phi. frazdnak) ; maltdan (von mard- aus
5265:mard *Mann', marz 'Mark, Landstrich', mary *Gras, marg
6719:833, mard 972, nahard 1025, mrrf*/ 1078 u. s.w., die Infini-
6916:echten Np. durch mard vertreten; phi. ahrmok (specifisch-
8747:mardak 'Mannlein* von mard *Mann', andak wenig' von and
=== SYN DIE / MAN ===
7193:4.71 BEGET (of Father)
7248:4.72 BEAR (of Mother) Grk.  tlxrw yervdw Goth. gabairan Lith.  gimdyti NG yovi ON ala, feda (bera) Lett. dzemdét Lat. parere Dan. ffde ChSl.  roditi It. partorire Sw.  féda SCr.  roditi Fr. enfanter OE beran, cennan (fédan) Boh.  roditi Sp. parir ME bere Pol. — rodzié Rum. naste NE bear Russ. rodit’ Tr. do-fuismim, biru Du. baren Skt.  jan-, si Nir. _betrim, iuismim OHG (gi)beran, kindon Av. zan-, hu- W. planta, gent MHG (ge)bern, kinden
7260:4.73 PREGNANT Goth. inkilpo, pat es pees vos <2 ieee ON unguo, Ulett, hafan- ett. gr Grk. (yyvearpane” tb a id A di, med barni ChSl. neprazdtna NG pracgnans, GRE Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: ger; dreglig Boh. téhotna; brezt gravida, ncn a, P Sw. havande; draktig Pol. brzmienna, ciezarna te na Deine OE getacnod, bearn-éacen, Russ. beremennaja Fr encernle, 9” pee 4 med cilde Skt.  garbhini-, garbhavati-, Sp. prenada, Pets ME with childe, with barne etc. Rum. insdr Fie ut NE pregnant, with child Avy. pubra- lorrac . ; drachti Ir. ‘i hea- Du. zwanger; 9g Nir. bruinneach, tourch GHik. smaieee sach MHG _ swanger, trehtec, w. _ beichtog swere : razez, dougerez eee Breese eraeees NHG  schwanger; trdchtig
7309:4.732. Verbs for ‘conceive’ or ‘be pregnant’ are in part derivatives of the same root as ‘pregnant’, as for example Grk. xvéw, OE (ge)éacnian. But more commonly they are expressions for ‘re- ceive, take’ like Grk. cv\\ayBave, Lat. concipere which served as models for the greater part of the European terms, NIr. gabhaim, Goth. ganiman, OHG inifahen, NHG empfangen, Du. ontvangen, Dan. undfange (from MLG), Lett. zen‘emt, etc. Others mean essentially ‘begin’, Lith. pradéti, ChSl. zaceti, Russ. zacat’, etc.
7344:4.75 DIE; DEAD; DEATH
7452:4.77 CORPSE
7479:4.78 BURY (the Dead) Goth. ga-, us-filhan, gana- Lith. (pa)laidoti, pakasti
10153:4.70. REW 6450.
```


## [2026-09-07T16:26:09.923Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f,keys in [('MON_part2.txt',['مرمر','مشیانه','مشیا','امرداد'])]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for k in keys:\n        idxs=[m.start() for m in re.finditer(k,t)][:3]\n        print('####',k,len(idxs))\n        for i in idxs:\n            print('   ...',t[max(0,i-120):i+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T16:26:11.478Z] TOOL RESULT

```
#### مرمر 3
   ... ۲ آهک  کشته.   کلسیوم: (-۷2۱۹ (۱.) (شیم.) فلز ی است  دو ظرفیتی که اکثر املاحش غیر محلولند.  این فلز در طبیعت بصورت گچ و مرمر و گل  سفید فراوان است و اغلب آن را از تجزية  الکتریکی کلروردوکلسيم 1,0۵) بدست  می‌آورند. اين فلز از سرب نرم‌تر ولی از  سدیم سخت‌تر است و در هوا فاسد می‌شود  و به همین جهت آن را در نفت یا روغن  نگ
   ...  را  تجز به می‌کند و ثیدرات کلسیم می‌دهد. از  املاح فراوان اين فلز یکی کربنات کلسیم  است که سصورت سنکكٌ‌های آهکی و  سنگ مرمر و گل سفید (گل گیوه) در  طبیعت سیار فراوان می‌باشد. دیگر سو لفات  کلسیم است که آن هم بصورت گچ و آلباتر  در طیعت فراوان است؛ کالسیوم.   کلف: )۲۵۱ [- کلب - کلپ] (.) منقار  مرغ.   کلف: ۲۱۸ [ع.] (.) ر
   ... جزو میوه‌های بنم است و در هر غلاف  آن چندین دانه موجود است. اقسام مختلفی  که در ابران کشت می‌شو ند عبار تند ار:  لوبیای مرمری» لوبیای قرمز» لوبیای  چشم‌بلبلی» لوببای رسمی؛ لوبیای چینی؛  فصولیه» لوییاء. لوبیای دریایی: (گیا.) گیاهی  است از تبرة اسفناجیان که در سواحل در باها  می‌روید. ساقه‌ها و برگ‌هایش متقابل»  گل‌هایش ع
#### مشیانه 1
   ... یعنی «مهر) -  است. در روز مهر رت بر وهج) از ماه مهر  ایرانیان جشن بسیار بزرگی بر پا می‌داشتند. به  قول نندهشن «مشیا» و «مشیانه» را دم و حوای  آربایبان) در چنین روزی تولد بافته‌اند. این  جشن بزرگ شش روز طول می‌کشید از  ی کی اسب روز  سست و در ۳۳۹ روز باشده ختم  می‌شد. روز آغاز را «مهرگان عامه, و روز  انجام ر «مه رگان حاص
#### مشیا 2
   ... ة فروع - یعنی «مهر) -  است. در روز مهر رت بر وهج) از ماه مهر  ایرانیان جشن بسیار بزرگی بر پا می‌داشتند. به  قول نندهشن «مشیا» و «مشیانه» را دم و حوای  آربایبان) در چنین روزی تولد بافته‌اند. این  جشن بزرگ شش روز طول می‌کشید از  ی کی اسب روز  سست و در ۳۳۹ روز باشده ختم  می‌شد. روز آغاز را «مهرگان عامه, و روز  انجام ر «مه
   ... یعنی «مهر) -  است. در روز مهر رت بر وهج) از ماه مهر  ایرانیان جشن بسیار بزرگی بر پا می‌داشتند. به  قول نندهشن «مشیا» و «مشیانه» را دم و حوای  آربایبان) در چنین روزی تولد بافته‌اند. این  جشن بزرگ شش روز طول می‌کشید از  ی کی اسب روز  سست و در ۳۳۹ روز باشده ختم  می‌شد. روز آغاز را «مهرگان عامه, و روز  انجام ر «مه رگان حاص
#### امرداد 2
   ...  برج‌های ده ازده گانه است؛: از  این قرارند:   برج‌ها حمل ثور تقو" تبرطان: شاه متله  ماه‌ها _ فروردین اردیبهشت خرداد تیر امرداد شهریور  برح‌ها میزان عقرب قوس جدی دلو حوت  ماه‌ها مهر ‏ آبان آذر دی    ماه قمری: یک ماه از سال قمری و آن از    ریت ملال ماه آغاز می‌شود؛ ریت هلال  در دفعةٌ بعد ختم می‌شود. هر ماه قمری ۳۹  روز ب
   ...  آشکار خواهد زد و  از آن روز در وضع آب و هوا تحولی رخ  خواهد داد (فر عا.جما.) نفس دزده: (عم.)  بیش از نفس آشکار در نیمه امرداد و نيمة  بهمن ماه زمین نفسی می‌زند که به نفس دزده  معروف است و ظاهراً علت موسوم شده این  نفس به «دزده» این است که تغییرات حاصل  از آن چندان آشکار و بارز نیست و به کندی  صورت می‌گیرد (فرعا.جما.)
```


## [2026-09-07T16:26:12.227Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ntags=[(i+1,int(m.group(1))) for i,l in enumerate(lines) if (m:=re.search(r'\\[pdf page (\\d+)\\]',l))]\ndef pg(ln):\n    cur=None\n    for i,p in tags:\n        if i<=ln: cur=p\n        else: break\n    return cur\nfor ln in [13587,13689,13706,11126,2604]:\n    print(ln,'pdf page',pg(ln),'printed',(pg(ln) or 0)-1)\n    print('   ', '\\n    '.join(lines[ln-3:ln+3]))\nEOF"
}
```


### [2026-09-07T16:26:13.452Z] TOOL RESULT

```
13587 pdf page 466 printed 465
    REFERENCES betty MARTIYA :(OLD PERSIAN) kml 5+),
    POKORNY, = SOS*~*~S~S~S~«SSS MART, MARD APAHLAVD) a,
    BARNHART: (MORTAL) 679 MERD, MER KURDISH) 52,5 |
    DELAMARRE: (HOMME) 51 MAR HBALUCHI) gu '
    MACKENZIE: (MAN) 122 SANSKRIT) ny Site
    BUCK: 81, 79 MARTA, MARTYA, MANU-
13689 pdf page 469 printed 468
    " MARMOR DANISH) Sails ASANSKRIT) 2 Sie
    MARMOR _ (SWEDISH) «st MURNAS, MRNATI
    MARMOR NORWEGIAN) (53, MARMAR ARMENIAN) gs
    MARMER (DUTCH) giche MARMAROS GREEK) gli
    MARMUR POLISH) ileng} MARMOR LATIN) 3X
    MRAMUR (CZECH) So MARBRE (FRENCH) wil
13706 pdf page 469 printed 468
    Seetlaok
    sod 2B tad Stcasa 9 C4,Sibe 32 05ly gil poh
    MARMAROS (gly so5ly 1 A305 19 59 cu! PS oJ Stew OL a aly Say
    eaileat gabe
    MUZD ARURDISH) 6525 MIZHDA AAVESTAN) glo}
    (SANSKRIT) ey Suile MIZD, MOZD PAHLAVI) 6 shay
11126 pdf page 382 printed 381
    MURNAN OSHMAR, OSHMARTAN,
    MOURN HENGLISH) JS ‘OSHMURDAN, SHUMAR
    MERETI LITHUANIAN) gi) (KURDISH) «52,8
    SHIMARTIN, ASHMARDIN,
    ‘REFERENCES both, ISHMAR, ZHIMARTIN
    POKORNY, ——~—~=~S*~S*~S*~«S OCI AFGHAN) (,o4) lil
2604 pdf page 92 printed 91
    sda pl tigety & Wil OL 22 Sly cal ee
    , sere ga A GIS US 32 05a onl
    [MORTAL tee lyr |
    UN-KUNTHS GOTHIC) S56 AMERETAT:(OLD PERSIAN) Slut) oj),
    AM-MIVANT HITTITE) «20 AMURDAD PAHLAVI) 54
    A-KNATS __:(TOKHARIAN A) A 5)
```


## [2026-09-07T16:26:27.483Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### SYN 4.75\"; sed -n '7344,7400p' SYN.txt | head -45"
}
```


### [2026-09-07T16:26:27.531Z] TOOL RESULT

```
##### SYN 4.75
4.75 DIE; DEAD; DEATH
Grk (dr0)Ovpoxw} reByqxds; Goth. (ga)swiltan, gadaup- Lith. mir; numires; mir- Oavaros nan; daups; dau- lis
NG TréAaivw; Bapéivos; us Lett. irl; nuomiris; nave Oédvaros ON deyja, svelta; daudr, (mira, mirte)
Lat. mori; mortuus; mors, ddinn; daudi ChSl.  (u)mréti; mrittvit; nex Dan. d4¢; ddd; d¢d stimrwitt
It. morire; morto; morte Sw. dé; dod; déd SCr.  umrijeti; mrlav; smrt
Fr. mourir; mort; mort OE sweltan, steorfan, cwe- Boh. (u) mrfti; mrlvy; smrt
Sp. morir; muerto; muerte lan; déad; déap, Pol. umiéraé, umrzeé;
Rum. muri; mort; moarte swylt umorly; &mieré
Ir, at-balim, ba-; marb; ‘ME deye, swelte, sterve, Russ. wmirat’, umeret'; mer- bas, &c, bath quele; deed; deeth lvyj; smert!
Nir. do-gheibhim bas, éa- NE die; dead; death Skt. my-; myta-; myli-, ma- gaim; marbh; bas, Du. slerven; dood; dood rana-, mrlyu- éag OHG  sterban, touwen; tot; Av. mar-, ri8-; marata-,
W. marw; marw; angeu tod masa-; arista-, etc, ;
Br. mervel; maro; maro MHG sterben, touwen; lot; (ava)marali-, maro-
tot
dyu-, mahrka-, ete.
NHG  sterben; tot; tod
The plain bald words for ‘die’ are listed, with omission of the numerous euphemistic expressions like NE pass away, depart, expire, perish, Grk. (Biov) Tehevraw lit. ‘end one’s life, come to an end’, Lat. ex-, tnter-, per-ire, lit. ‘go from, ete.’, dé- ex-cédere lit, ‘depart’, etc., and likewise of vulgar expressions like NE croak, with the parallel Fr. crever, It. crepare (from Lat. crepare ‘crack, creak, rattle’) and NG YodS (Grk. yodiw ‘make a noise, knock, rattle’).
Most of the common words, except in Greek and Germanic, belong to an in- herited group, reflecting an IE root for ‘die’, whatever its ultimate semantic source. Others are originally euphemis- tie substitutes, cognate with words
meaning ‘be extinguished, endure pain’, ‘burn slowly, become stiff’, ete.
1. IH *mer- ‘die’, perh. ultimately the same as *mer- in words for ‘rub, crush’. Walde-P. 2.276. Ernout-M. 631 f.
Lat. mori, adj. mortuus, sb. mors (hence all the Romance forms); Ir. marb, NIr. marbh ‘dead’, W. marw ‘die, dead’, Br. maro ‘dead, death’ (hence mervel ‘die’); Lith. mirti, pple. (perfect.) numires, sb. mirtis, Lett. mirt, pple. nuomiris, sbs. mira, mirte (but both rare); ChSl. mréti, umréti, adj. mritvt, sb. stimriitt, and the other Slavic words (chiefly perfect. forms for the verb); Skt. my- (3 sg. pres. mriyate, and ma- rate), Av. 3 sg. pres. matryeiti, etc., OPers 3 sg. imperf. amariyatd, pples.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
aaa ca
morata-, masa-; sbs. tay ana-, mrtyur, Av. (ava) me Arm. meranim ‘die’; épBporos “immor- N mor®d ‘rourder’,
ie QroOvpoKe, perf. pple.
noKe ls ae dead’, sb. 4varos, redvnxos lit.) mebaivw
, OKO. NG (4robv me antMave), pple. mefa-
; dhvan- 176) + Sel ‘dark’ and ‘darkness’,
at *dhwena-, but further rot eonnectiOn Walde-P. 1.841. Otherwise Kent, Language 11.207 ff.
3, Lat. nex ‘violent death’ (vs. mors, above, 1), late sometimes also for natural ‘death’: Grk. vexpos, vexus Av. nasu- ‘corpse’ (4.77), Skt. nag-, Av. nas- ‘van- ish, perish’, Ir. éc, etc. (below, 4) ‘death’. Walde-P, 2.326. Ernout-M. 669 f.
4, Ir, at-balim (e.g. 3 sg. at-bail) = fas--bal- (with infixed pronoun, cf. Thuneysen, Gram. 267), OE cwelan, ME quele : W. aballw ‘fail, perish’, OHG, 08 quelan ‘endure torment’, Lith. geltz ‘sting, cause violent pain’, gelia ‘it hurts, galas ‘end’, OPruss. gallan a ete., IE *g¥el-. Walde-P. 1.690. nine 2.459f. Vendryes, RC ae ‘die’ (forms in Lewis-Pedersen ‘de ah “aes Gram. 461), vbl. n. bas en ic Mir. bath ‘death’, etym. dis- Skt one 'S orig. ‘go (forth)’ : Grk. Byy,
- agat Went’, IE * peg ‘g0? Peder. (eit, therwise, as a Celtic root ae
it See e neyeen RZ 37 ne Mir. bath), Thur- Walde.p, ier ar 20 (Gram. 450, 461), Die: « Che) With added suggestion of
- Gast ‘extinguish’, etc.).
Didar ons; ‘vet lala bas reg. for ‘die’, lit.
igitized by Arya Samaj Foundation Chennai and eGangotri
DILY FUNCTIONS AND CONDITIONS 287
Ir. éc, NIr. éag (hence vb. éagaim), W. angeu, Corn. ancow ‘death’ (Br. ankou ‘death’ personified) : Lat. nex ‘violent death’, etc. (above, 3). Peder- sen 1.46. Thurneysen, Gram. 127.
5. Goth. (ga)swiltan, ON svelia poet. (esp. ‘die of hunger, starve’, so NIcel., Dan., Sw.), OF sweltan, ME swelte ‘die’ (ME also ‘be oppressed with heat’, as NE swelter), OF swylt ‘death’ (ON sulir ‘hunger’), cf. OHG swelzan, MHG swel- zen ‘burn up (with hot love), dissolve in fire’, Crim. Goth. schuualt ‘death’, all with d-extension of *swel- in OE swelan ‘burn slowly’, Lith. sviltt ‘be scorched’, ete. Walde-P. 1.531 f. Falk-Torp 1204, 1208. Feist 468.
Goth. gadaupnan, daups, daupus, ON deyja (pple. dainn), daudr, daudi, and the Dan. and Sw. words, OE déad, déap (vb. lacking in OE, hence ME deye prob. fr. Norse), Du. dood, OHG touwen, tot, tod, etc. : Goth. diwans ‘mortal’, fr. an IE *dheu-, perh. connected further with *dhwena- in Grk. @avaros, etc. (above, 2), but ultimate relations of the various *dheu-groups uncertain. § Walde-P. 1.835 f. Falk-Torp 175. Feist 118.
OE steorfan, ME sterve (NE starve), Du. sterven, OHG sterban, MHG, NHG sterben : ON starfa ‘work, tire’, sijarft ‘tetanus’, LG starfen ‘become stiff, coagulate’, Lat. torpére ‘be stiff, numb’, Lith. tirpti ‘be numb’, etc., labial ex- tensions of IE *ster- in Grk. ozepeds ‘stiff, firm’, etc. Walde-P. 2.632. Falk- Torp 1159.
6. Lett. ndve ‘death’: navet ‘kill’, ChSI. navi, Goth. naus, ON nar ‘corpse’ (4.77), Lith. novytt ‘torture, kill’, ChSL., Boh. naviti ‘tire’, ete. Walde-P. 2.316. Mithl-Endz. 2.703 f.
7. Av. ri0- (3 sg. pres. iriéyeitz), pple. irista-, euphemistic terms for ‘die, dead’ always used of good beings (leaving forms of the inherited root, above, 1, for
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
288
```


## [2026-09-07T16:26:28.900Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### IEC mer-\"; grep -n \"^mer-\\|^mer[ōo]-\\|^mrto-\\|^morto-\\|^marmaro\" IEC.txt | head -20\necho \"##### WLD Bd2 mer- (WP II 276)\"; grep -n \"mer-\\s*'sterben'\\|mer- 'sterben'\\|marmaros\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T16:26:28.960Z] TOOL RESULT

```
##### IEC mer-
10658:mer- (mern-) (e-gde radical of type mr-, q. v. with extensions, and cf. mruos (moruos), etc. Per. cf. miram, inf. murdan die: Arm. mef- nim, meranim, aor, meraj, id.; merot, gs -i, ab. s. -av ‘mortal; Hitt. (queried) mernun, 1sg. (T die? or ‘cause to die") beside merr- die: W meru, inf. ‘droop’ beside merth, pl. -i, m. exhaustion’, fr. *mertis); Cor. cf. mernans, m. ‘death’; Latv. mernéju, et ‘starve’
##### WLD Bd2 mer- (WP II 276)
```


## [2026-09-07T16:26:44.094Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,45p' tools/fetch_source.py"
}
```


### [2026-09-07T16:26:44.136Z] TOOL RESULT

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
```


## [2026-09-07T16:26:59.409Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mer-\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CE%BC%CE%B1%CF%81%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%85%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%85%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%88%D9%85%D8%B1%D8%AB\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF%D8%A7%D8%AF\" \\\n \"https://www.etymonline.com/word/marble\" \\\n \"https://www.etymonline.com/word/murder\" \\\n \"https://www.etymonline.com/word/nightmare\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 335 root Mer 2: verifying Nourai's Avestan/Persian/Greek/Germanic derivations\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T16:27:09.855Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9b74a66299d6a23b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/587378081b1eb72b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b7007a777b99dde.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f12bce859ac2358d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/796c3d4466245560.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96efeb6259437ef9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ac315411a95650f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/044e2fe758196320.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4a844c991df741d5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0538cbaa7e728414.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b248da132582b19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8965fa4227e0420.txt
```


## [2026-09-07T16:27:13.633Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 9b74a66299d6a23b 587378081b1eb72b 7b7007a777b99dde; do echo \"######## $f\"; head -c 200 $f.txt; echo; grep -n -A6 -i \"^Etymology\\|Proto-Iranian\\|Middle Persian\\|From Proto\" $f.txt | head -40; done"
}
```


### [2026-09-07T16:27:14.858Z] TOOL RESULT

```
######## 9b74a66299d6a23b
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mer-
FETCHED: 2026-09-07T16:27:02Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/mer- - Wiktionary, the free dictionary


211: Proto-Iranian: 
212- Avestan: 𐬨𐬀𐬭𐬆𐬙𐬀 ( mar ə ta ) 
213-
214- Compounds:
215-
216- *m(o)r-bʰ(h₂)-o- ( “ looking like death? ” ) [ 16 ] 
217- Proto-Italic: *morfos 
--
225: Proto-Iranian: 
226- Gurani: مەردەی ( marday ) 
227-
228- Khotanese: [script needed] ( mär- ) 
229-
230- Kurdish:
231- Northern Kurdish: mirin 
--
237: Middle Persian: [script needed] ( myr /⁠mīr-⁠/ ) 
238- Persian: مردن ( mordan ) 
239- Tajik: мурдан ( murdan ) 
240-
241- Parthian: [Term?] ( /⁠myr⁠/ ) 
242-
243- Zazaki: merden 
--
252: Proto-Iranian: 
253- Younger Avestan: 𐬨𐬀𐬭- ( mar- ) 
254-
255- Root
256- [ edit ] 
257-
258- *mer- 
--
322: Requests for native script for Middle Persian terms 
323- Parthian term requests 
324-
325- This page was last edited on 24 August 2026, at 00:42.
326-
327- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
328-
######## 587378081b1eb72b
URL: https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF%D9%86
FETCHED: 2026-09-07T16:27:02Z
STATUS: 200
TITLE: مردن - Wiktionary, the free dictionary

مردن - Wiktionary, the free dictionary 

 
203: From Proto-Iranian *márti , from Proto-Indo-Iranian *márti , ultimately from Proto-Indo-European *mer- . Compare Persian مردن ( mordan ) .
204-
205- Pronunciation
206- [ edit ] 
207-
208- IPA ( key ) : /məɾdən/ 
209-
--
447: From Middle Persian YMYTWNtn' ( murdan ) , from Old Persian [script needed] ( mar- ) , from Proto-Iranian *márti , from Proto-Indo-Iranian *márti , ultimately derived from Proto-Indo-European *mer- ( “ to die ” ) . Compare Northern Kurdish mirin , Avestan 𐬨𐬀𐬭- ( mar- ) , Sanskrit मरति ( marati ) , Old Armenian մեռանիմ ( meṙanim ) , Old Church Slavonic мрѣти ( mrěti ) , Latin morior , English murder .
448-
449- Pronunciation
450- [ edit ] 
451-
452- ( Classical Persian ) IPA ( key ) : /mur.ˈdan/ 
453-
--
1406: Categories : Central Kurdish terms derived from Proto-Iranian 
1407: Central Kurdish terms derived from Proto-Indo-Iranian 
1408: Central Kurdish terms derived from Proto-Indo-European 
1409- Central Kurdish terms with IPA pronunciation 
1410- Central Kurdish lemmas 
1411- Central Kurdish verbs 
1412- Central Kurdish intransitive verbs 
1413: Persian terms inherited from Middle Persian 
1414: Persian terms derived from Middle Persian 
1415- Persian terms inherited from Old Persian 
1416- Persian terms derived from Old Persian 
1417: Persian terms inherited from Proto-Iranian 
1418: Persian terms derived from Proto-Iranian 
1419: Persian terms inherited from Proto-Indo-Iranian 
1420: Persian terms derived from Proto-Indo-Iranian 
1421: Persian terms derived from Proto-Indo-European 
1422- Persian terms with IPA pronunciation 
1423- Rhymes:Persian/an 
1424- Rhymes:Persian/an/2 syllables 
1425- Persian lemmas 
1426- Persian verbs 
1427- Persian terms with quotations 
######## 7b7007a777b99dde
URL: https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF
FETCHED: 2026-09-07T16:27:03Z
STATUS: 200
TITLE: مرد - Wiktionary, the free dictionary

مرد - Wiktionary, the free dictionary 

 Jump to co
2097: Inherited from Middle Persian [Book Pahlavi needed] ( mlt' /⁠mard⁠/ ) , [Book Pahlavi needed] ( GBRA /⁠mard⁠/ ) , from Old Persian 𐎶𐎼𐎫𐎡𐎹 ( martiya ) , from Proto-Iranian *mŕ̥tah , from Proto-Indo-Iranian *mŕ̥tas , and ultimately from Proto-Indo-European *mr̥tós ( “ dead, mortal ” ) , from *mer- ( “ to die ” ) ; whence also مردن ( mordan , “ to die ” ) , and مردم ( mardom , “ people ” ) . [ 1 ] Noun sense 2 is a semantic loan from English man .
2098-
2099- Cognates include Northern Kurdish mêr ( “ husband ” ) , Northern Luri میره ( mırə , “ husband ” ) , Pashto مېړۀ ( meṛə , “ husband ” ) , Sanskrit मर्त ( marta , “ mortal, man ” ) , Old Armenian մարդ ( mard , “ man ” ) , Ancient Greek βροτός ( brotós , “ mortal ” ) , and Latin mortuus ( “ dead ” ) 
2100-
2101- Pronunciation
2102- [ edit ] 
2103-
--
2344: Persian terms inherited from Middle Persian 
2345- Persian terms inherited from Old Persian 
2346: Persian terms derived from Proto-Indo-Iranian 
2347: Persian terms derived from Proto-Indo-European 
2348: Persian terms inherited from Proto-Iranian 
2349- Persian terms derived from Old Persian 
2350- Persian terms derived from the Proto-Indo-European root *mer- (die) 
2351: Persian terms inherited from Proto-Indo-Iranian 
2352: Persian terms derived from Proto-Iranian 
2353: Persian terms derived from Middle Persian 
2354- Persian semantic loans from English 
2355- Persian terms derived from English 
2356- Persian terms with IPA pronunciation 
2357- Rhymes:Persian/ard 
2358- Rhymes:Persian/ard/1 syllable 
2359- Persian dialectal terms 
--
2387: Requests for Book Pahlavi script for Middle Persian terms 
2388- Old Persian terms with non-redundant manual transliterations 
2389- Punjabi terms with non-redundant manual transliterations 
2390- Persian terms in nonstandard scripts 
2391- Persian links with redundant wikilinks 
2392- Persian links with redundant alt parameters 
2393- Persian links with manual fragments
```


## [2026-09-07T16:27:21.036Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f12bce859ac2358d 796c3d4466245560 96efeb6259437ef9; do echo \"######## $f\"; head -c 150 $f.txt; echo; grep -n -B2 -A8 -i \"Etymology\" $f.txt | head -50; done"
}
```


### [2026-09-07T16:27:22.269Z] TOOL RESULT

```
######## f12bce859ac2358d
URL: https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CE%BC%CE%B1%CF%81%CE%BF%CF%82
FETCHED: 2026-09-07T16:27:04Z
STATUS: 200
TITLE: μάρμαρος
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
162- μάρμᾰρον ( mármăron ) 
163-
164: Etymology
165- [ edit ] 
166-
167- Of uncertain origin. Based on the original sense of “stone; rock”, Frisk derives the word from the root of μᾰ́ρνᾰμαι ( mắrnămai , “ to fight; to battle ” ) (perhaps in a sense of “stone weapons”), with folk-etymological semantic influence from μαρμαίρω ( marmaírō , “ to sparkle ” ) ; others, such as Mazon, prefer to directly connect the word to μαρμαίρω ( marmaírō ) . Due to the lack of strong evidence of connection to other words, as well as perhaps the semantic category of “local rocks”, Beekes suggests Pre-Greek origin. [ 1 ] 
168-
169- An alternative theory by Roberts suggests a reduplicative formation from Proto-Indo-European *mer- ( “ to rub away; to cause harm; to die ” ) , in the sense of marble's fragility. [ 2 ] 
170-
171- Pronunciation
172- [ edit ] 
######## 796c3d4466245560
URL: https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%85%D8%B1
FETCHED: 2026-09-07T16:27:05Z
STATUS: 200
TITLE: مرمر - Wiktionary, the free dictiona
74-
75- 2.1 
76: Etymology 
77-
78- 2.2 
79- Noun 
80-
81- 2.2.1 
82- Derived terms 
83-
84- 2.2.2 
--
94-
95- 3.1 
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Noun 
103-
104- 3.3.1 
--
686-
687- مرمر 
688: Etymology
689- [ edit ] 
690-
691- Borrowed from either Classical Persian مرمر ( marmar ) or Arabic مرمر ( marmar ) , both from Ancient Greek μάρμαρος ( mármaros , “ marble ” ) .
692-
693- Noun
694- [ edit ] 
695-
696- مرمر • ( mermer ) ( definite accusative مرمری ( mermeri ) , plural مرمرلر ( mermerler ) ) 
--
759- [ edit ] 
760-
761: Etymology
762- [ edit ] 
763-
764- From Ancient Greek μάρμαρος ( mármaros ) .
765-
766- Pronunciation
767- [ edit ] 
768-
769- ( Classical Persian ) IPA ( key ) : /mar.ˈmar/ 
######## 96efeb6259437ef9
URL: https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%85%D8%B1%D8%AF%D9%86
FETCHED: 2026-09-07T16:27:06Z
STATUS: 200
TITLE: پژمردن - Wiktionary, t
```


## [2026-09-07T16:27:36.472Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nfor f,pat in [('96efeb6259437ef9','پژمردن'),('7ac315411a95650f','مل'),('044e2fe758196320','کیومرث'),('4a844c991df741d5','مرداد')]:\n    t=open(f+'.txt',encoding='utf-8').read()\n    print('########',f,pat, t.split('TITLE:')[1].split('\\n')[0][:60])\n    for m in re.finditer(r'Etymology\\n \\[ edit \\] \\n\\n(.{0,900}?)\\n\\n',t,re.S):\n        print('  --',m.group(1)[:900].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T16:27:37.790Z] TOOL RESULT

```
######## 96efeb6259437ef9 پژمردن  پژمردن - Wiktionary, the free dictionary
######## 7ac315411a95650f مل  مل - Wiktionary, the free dictionary
  --  From Proto-Iranian *mr̥ju- . Compare Persian مل ( mol ) and Talysh مل ( məl ) , مله ( məlla , “ neck ” ) .
  --  Inherited from Paisaci Prakrit 𑀫𑀼𑀮𑁆𑀮 ( mulla ) (compare Sauraseni Prakrit 𑀫𑀼𑀮𑁆𑀮 ( mulla ) ), from Sanskrit मूल्य ( mūlya ) . Cognate with Urdu مول ( mol ) , Nepali मुल्य ( mulya ) , Konkani मोल ( mōl ) , Assamese মূল্য ( muillo ) , Bengali মূল্য ( mullo ) and Sinhalese මිල ( mila ) .
  --  Inherited from Arabic مَلَّ ( malla ) .
  --  From Sanskrit मल ( mala ) , from Proto-Indo-European *melh₂- .
######## 044e2fe758196320 کیومرث  
######## 4a844c991df741d5 مرداد  مرداد - Wiktionary, the free dictionary
  --  From Middle Persian 𐭠𐭬𐭥𐭥𐭣𐭠𐭣 ( ʾmwrdʾd /⁠Amurdād⁠/ ) , lit. “immortality”; name of the sixth Amahraspand (divine deity) in Zoroastrianism. Compare مردن (mordan, “to die”).
```


## [2026-09-07T16:27:43.939Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"###### پژمردن file\"; sed -n '1,120p' 96efeb6259437ef9.txt | tail -90"
}
```


### [2026-09-07T16:27:43.988Z] TOOL RESULT

```
###### پژمردن file
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
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Verb 

 1.2.1 
 Conjugation 

 1.3 
 Further reading 

 Toggle the table of contents 

 پژمردن 

 4 languages 

 فارسی 
 Kurdî 
 Malagasy 
 Русский 

 Entry 

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
 Cite this page 
 Get shortened URL
```


## [2026-09-07T16:27:49.693Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('7ac315411a95650f.txt',encoding='utf-8').read()\ni=t.find('Persian\\n')\n# find all sections headed 'Persian'\nimport re\nfor m in re.finditer(r'\\n Persian \\n',t):\n    print('---', t[m.start():m.start()+900].replace('\\n',' ')[:900])\n    print()\nEOF"
}
```


### [2026-09-07T16:27:50.909Z] TOOL RESULT

```
---   Persian    Toggle Persian subsection    5.1   Etymology 1    5.1.1   Pronunciation    5.1.2   Noun    5.2   Etymology 2    5.2.1   Pronunciation    5.2.2   Noun    6   Punjabi    Toggle Punjabi subsection    6.1   Etymology    6.2   Pronunciation    6.3   Noun    6.3.1   Declension    6.4   References    7   South Levantine Arabic    Toggle South Levantine Arabic subsection    7.1   Etymology    7.2   Pronunciation    7.3   Verb    7.3.1   Conjugation    7.3.2   See also    8   Southwestern Fars    Toggle Southwestern Fars subsection    8.1   Noun    9   Torwali    Toggle Torwali subsection    9.1   Etymology    9.2   Noun    9.2.1   Derived terms    Toggle the table of contents    مل    13 languages    العربية   Deutsch   فارسی   Magyar   Bahasa Indonesia   日本語   한국어   Kurdî   Lietuvių   Malagasy   پنجابی   Русский   اردو    Entry    Discussion    English    Read    Edit    View histo
```


## [2026-09-07T16:27:54.954Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nimport re\nt=open('7ac315411a95650f.txt',encoding='utf-8').read()\n# locate the Persian language body: search for 'Etymology 1' occurrences after TOC\nidx=[m.start() for m in re.finditer(r'Etymology 1',t)]\nprint(idx)\nprint(t[idx[-1]-200:idx[-1]+1800])\nEOF"
}
```


### [2026-09-07T16:27:56.311Z] TOOL RESULT

```
[621, 1283, 2548, 14391]
 article on: مل 

 Wikipedia ps 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /mal/ 

 Noun
 [ edit ] 

 مل • ( mal )  m ( plural مله ( mlë ) ) 

 companion 

 comrade 

 friend 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Borrowed from Sogdian [script needed] ( mwδ /⁠muδ⁠/ ) or less likely from Bactrian μολο ( molo , “ wine ” ) , both from Proto-Iranian *mádu , from Proto-Indo-Iranian *mádʰu , from Proto-Indo-European *médʰu . Doublet of می ( mey ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈmul/ 

 ( Dari, formal ) IPA ( key ) : [mʊl] 

 ( Dari, formal ) IPA ( key ) : [mʊl] 
 ( Kabuli ) IPA ( key ) : [mʊl] 

 ( Hazaragi ) IPA ( key ) : [mul̥] 

 ( Iran, formal ) IPA ( key ) : [mol̥] 

 ( Tajik, formal ) IPA ( key ) : [mul] 

 Rhymes: -ul 

 Readings

 Classical reading ? 

 mul

 Dari reading ? 

 mul

 Iranian reading ? 

 mol

 Tajik reading ? 

 mul

 Noun
 [ edit ] 

 مل • ( mol ) 

 ( literary , archaic ) wine 
 Synonyms: شراب ( šarâb ) , ( literary ) می ( mey ) 

 Etymology 2
 [ edit ] 

 From Proto-Iranian *mr̥ju- . Cognate with Talysh مل ( məl ) , مله ( məlla , “ neck ” ) , Avestan 𐬨𐬆𐬭𐬆𐬰𐬎 ( mər ə zu , “ neck, vertebra ” ) . Central Kurdish مل ( mil , “ neck ” ) is loaned from Persian.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /mol/ 

 Noun
 [ edit ] 

 مل • ( mol ) 

 ( dialectal , Yazd , Kazerun ) neck 
 Synonym: گردن ( gardan ) 

 Punjabi
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Paisaci Prakrit 𑀫𑀼𑀮𑁆𑀮 ( mulla ) (compare Sauraseni Prakrit 𑀫𑀼𑀮𑁆𑀮 ( mulla ) ), from Sanskrit मूल्य ( mūlya ) . Cognate with Urdu مول ( mol ) , Nepali मुल्य ( mulya ) , Konkani मोल ( mōl ) , Assamese মূল্য ( muillo ) , Bengali মূল্য ( mullo ) and Sinhalese මිල ( mila ) .

 Pronunciation
 [ edit ] 

 ( Standard Punjabi ) IPA ( key ) : /mʊlːə̆/ 

 Noun
 [ edit ] 

 مُلّ • ( mull )  m ( Gurmukhi spelling ਮੁੱਲ ) 

 price ; worth 
 Synonym: قِیمَت ( qīmat ) 

 Declension
 [ edit ] 

 Declension of مل 

 singular

 plural

 direct

 مُلّ ( mull )
```


## [2026-09-07T16:28:08.487Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 0538cbaa7e728414 9b248da132582b19 a8965fa4227e0420; do echo \"######## $f\"; grep -n \"STATUS\\|TITLE\" $f.txt|head -2; python3 -c \"\nimport sys,re\nt=open('$f.txt',encoding='utf-8').read()\nprint(t[500:2600])\n\"; done"
}
```


### [2026-09-07T16:28:09.935Z] TOOL RESULT

```
######## 0538cbaa7e728414
3:STATUS: 200
4:TITLE: Marble - Etymology, Origin & Meaning
ion from marbra (mid-12c.), from Old French marbre (which itself underwent dissimilation of 2nd -r- to -l- in 14c.; marbre persisted in English into early 15c.), from Latin marmor , from or cognate with Greek marmaros "marble, gleaming stone," of unknown origin, perhaps originally an adjective meaning "sparkling," which would connect it with marmairein "to shine."

 Marblestone is attested from c. 1200, and the Latin word was taken directly into Old English as marma . German Marmor is restored Latin from Old High German marmul . Meaning "piece of sculptured or inscribed marble" (especially a marble tomb or tombstone) is from early 14c. Meaning "little ball of marble used in a children's game" is attested from 1690s; see marbles .
 also from early 14c. 

 marble (adj.) 

 late 14c., "consisting of marble," from marble (n.). Meaning "mottled like marble" is mid-15c. The earlier adjective in this sense was marbrin (early 14c.). From 1590s as "resembling marble in some figurative quality" (cold, hard, insensible, etc.). Marble cake is attested from 1864.
 also from late 14c. 

 marble (v.) 

 1590s (implied in marbled ), "to give (something) the veined and clouded appearance of marble," from marble (n.). Of meat with "veins" of fat, from 1770. Of books, "having the end papers or edges colored or stained in a conventional imitation of marble," 1670s. Related: Marbling .

 It is done in a trough of water covered by a layer of gum tragacanth mixed with a little ox-gall. The fluid colors are sprinkled or spattered over this layer with a brush in the arrangement intended for use or in a manner which will admit of producing the desired figuration by drawing a brass comb over the surface. The dampened paper, held by the ends, is lightly passed in a curve over this surface, taking up the colors, and finished by sizing and burnishing or calendering. [Century Dictionary, 1895]
 also from 1590s 

 Entries linking to marble 

 marbles (n.) 

 children's game, from plural of marble (n.); the game is recorded by that name by 1709 but is probably older (it was known in 13c. German a
######## 9b248da132582b19
3:STATUS: 200
4:TITLE: Murder - Etymology, Origin & Meaning
 1300, murdre , earlier morþer , from Old English morðor (plural morþras ) "secret killing of a person, unlawful killing," also "mortal sin, crime; punishment, torment, misery," from Proto-Germanic *murthran (source also of Goth maurþr , and, from a variant form of the same root, Old Saxon morth , Old Frisian morth , Old Norse morð , Middle Dutch moort , Dutch moord , German Mord "murder"), from suffixed form of PIE root *mer- "to rub away, harm" (also "to die" and forming words referring to death and to beings subject to death).

 The spelling with -d- probably reflects influence of Anglo-French murdre , from Old French mordre , from Medieval Latin murdrum , which is from the Germanic word. A parallel form murther persisted into 19c.

 In Old Norse, custom distinguished morð "secret slaughter" from vig "slaying." The former involved concealment, or slaying a man by night or when asleep, and was a heinous crime. The latter was not a disgrace, if the killer acknowledged his deed, but he was subject to vengeance or demand for compensation.

 Mordre wol out that se we day by day. [Chaucer, "Nun's Priest's Tale," c. 1386]

 Weakened sense of "very unpleasant situation" is from 1878. Inverted slang sense of "something excellent or terrific" is by 1940. As the name of a parlor or children's game, by 1933.
 also from c. 1300 

 murder (v.) 

 c. 1200 mortheren , "to kill, slay; kill criminally, kill with premeditated malice," from Old English myrðrian , from Proto-Germanic *murthjan (source also of Old High German murdran , German mördren , Gothic maurþjan , from Proto-Germanic *murthra- (see murder (n.)). But OED doubts the Old English verb survived into Middle English and thinks the modern word perhaps from the noun. Forms with -d- begin mid-14c. Meaning "spoil by bad execution" is from 1640s. Related: Murdered ; murdering .
 also from c. 1200 

 Entries linking to murder 

 burden (n.1) 

 "a load, that which is borne or carried," Old English byrðen "a load, weight, charge, duty;" also "a child;" from Proto-Germanic *burthinjo- "that which is borne" (source also of Ol
######## a8965fa4227e0420
3:STATUS: 200
4:TITLE: Nightmare - Etymology, Origin & Meaning
feeling of suffocation," compounded from night + mare (n.3) "goblin that causes nightmares, incubus." The meaning shifted mid-16c. from the incubus to the suffocating sensation it causes. Sense of "any bad dream" is recorded by 1829; that of "very distressing experience" is from 1831.

 Cognate with Middle Dutch nachtmare , German Nachtmahr . An Old English word for it was niht-genga . An 11c. gloss gives, for Latin Echo , Anglo-Saxon wudumær , a "wood-mere."

 In the Anglo-Saxon superstitions, the Echo was supposed to be a spirit which dwelt in the wilds and mocked people who passed there, as the night-mare tormented people in bed. [Thomas Wright, "Anglo-Saxon and Old English Vocabularies," 1884]
 also from c. 1300 

 Entries linking to nightmare 

 mare (n.3) 

 "night-goblin, incubus, oppressed sleep," Old English mare "incubus, nightmare, monster; witch, sorcerer," from mera, mære , from Proto-Germanic *maron "goblin" (source also of Middle Low German mar , Middle Dutch mare , Old High German mara , German Mahr "incubus," Old Norse mara "nightmare, incubus").

 This is from PIE *mora- "incubus" (source also of first element in Old Irish Morrigain "demoness of the corpses," literally "queen of the nightmare," also Bulgarian, Serbian mora , Czech mura , Polish zmora "incubus").

 Also compare French cauchemar "nightmare," with first element from Old French caucher "to trample" and second element from Germanic.

 All this is probably from PIE root *mer- "to rub away, harm" (also "to die" and forming words referring to death and to beings subject to death).

 The word in English now survives only in nightmare (q.v.). In a very early Anglo-Saxon text Latin echo is glossed with wudumer "*woodmare."

 night (n.) 

 late Old English niht (West Saxon neaht , Anglian næht , neht ) "the dark part of a day; the night as a unit of time; darkness," also "absence of spiritual illumination, moral darkness, ignorance," from Proto-Germanic *nahts (source also of Old Saxon and Old High German naht , Old Frisian and Dutch nacht , German Nacht , Old Norse natt , Gothic nahts ).
```


## [2026-09-07T16:28:28.915Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=\\[pdf page \\d+\\])',t)\n# find the block containing 'mer-' 'sterben' typical\nhits=[]\nfor b in blocks:\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if not m: continue\n    if re.search(r'mer-|mṛtá|mrto|marmaros|marainein|maraino',b):\n        hits.append((int(m.group(1)),b))\nprint('candidate pages:',[h[0] for h in hits][:40])\nEOF"
}
```


### [2026-09-07T16:28:30.255Z] TOOL RESULT

```
candidate pages: []
```


## [2026-09-07T16:28:33.853Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la incoming/WLD/ | head; echo; head -c 600 incoming/WLD/WLD_Bd2_pages.txt; echo; echo \"=== grep sterben ===\"; grep -c \"sterben\" incoming/WLD/WLD_Bd2_pages.txt; grep -n \"sterben\" incoming/WLD/WLD_Bd2_pages.txt | head -5"
}
```


### [2026-09-07T16:28:33.922Z] TOOL RESULT

```
total 146216
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 94865800 Sep  4 14:06 WLD_Bd2_1927_dli_106624_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2833963 Sep  4 14:06 WLD_Bd2_pages.txt

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
  J.   GUTTENTAG, VERLAGSBUCHHANDLUNG - GEORG
        REBIER - KARL J. TROBNER - VEIT & COMP.
central a     -              iJlGAL
    EIBRaKY,                 HI.
Am.
lh.^.JM.-..
0*11 No...Hl.l/.fE‘^/fV^;.
(pais?): p
=== grep sterben ===
25
9411:iiberstehn   sterben", perfungi „v5llig mit etwas fertig werden, uberstehn"
18140:3,    mer- „sterben“.
18172:anmer „unsterblich“, mah „Tod“ (s. o.); lit. miVs^w, mirti „sterben^', mer-
18174:mhrUi „ sterben “ {morz, umoriti, mr^iv^ s. o.).
18177:4 If., Arm. Gr. I 472f. usw., ^mer- „sterben-' gilt mit Eecht als ein friih-
```


## [2026-09-07T16:28:38.564Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18130,18200p' incoming/WLD/WLD_Bd2_pages.txt\necho \"=== page tags? ===\"; grep -c \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T16:28:38.628Z] TOOL RESULT

```
276                                                       mer-


mhd. hrehen^ aisl. hrja, hra „plotzlich aufleuchten‘^, got. hraJv atigins j,Augen-
blick’^ usw.      an, die     aber besser zu ai. hhrajati, bhra^ate (s. %hereg-^ hhereJc-)
gestellt    werden         (Lit. bei   Berneker II 85).

3,    mer- „sterben“.
     Ai.   mdrate „stirbt“; mriydte ds.,                   av. miryeite (^md'^ryeHe) ds.,   ap.   ama-
riyata „er starb“, =lat.            ai, Kaus. marayati „totet“, vgl. aksl. u-

moriti {u-marjati) „toten^; fo-Ptc. ai. mrtd-                        =
                                                 av. mdrdta- „gestorben, tot‘^,
ai. mrtd-m „Tod^, av. mdsa-             (^mrta-^ Bartholomae Wb. tl75j, ai.
amta- == av. am9sa- „unsterblicb“, arm. mard „Mensch^ {^mrtos\ abd.
mord^ ags. anord. mord                     n.    „Mord“ {^mHoni]         daneben "^mr-trom in got.
maurjn'     n.,   ags. niordor n.              „Mord“),    gr. figoTog „sterblich,m."Mensch“, a>-
^Qoro^ „unsterbiich'' (aus "^/ugaiog nach jLiogrog^ dvdgcoTiogy '&v7]r6g Hes.
umgefarbt, oder nach Debrunner GGA. 1910, 16 Aolismus; kaum nach
Brugmann-Thumb GrGr.^ 88 Bildung wie                   da nicht Nomen actionis
wie dieses); lQ.t mortims^ aksl. mr^tv^ „tot“ (Erweiterung Yon ’^mrtos nach
*g^T-uos „lebendig“ oder einem damit bildungsgleichen ^my-uo-s° s. unten
air. marh); o-stufiges ^o-Nomen ai. mdrta-h „ Sterblicher° Mensch“, av.
marota-, mardtan- ^ds."^, gr. jogjog (s. o.), ai. martya- „sterblich“, ap.
inartiya-^ av. masya- „Mensch“, ai. amartya- „unsterblich“ (ahnlich gr.
ajii^gooiog ds.)  tl-St ai, mrti-h „Tod‘S ay, msrdti- ds., lat. mors, -tis ds.,
                       ;



lit.        aksl. s^mr^i^ ds.; f?«-St. in arm. maA, alter marh „Tod“ (nach
Pedersen KZ. 39, 364; kaum                        =
                                   ai. mr^2/^<45 ay.mdr9pyu- „Tod^^, das
                                                                          eher
erst ar. Verquickung von -ti und /^/-St.); ai. mara-/^ „Tod, Pest‘^ lit. *ma-
ras, aksl. mor^ „Pest^; air. mnrh, cymr. usw, mariv „gestorben“ (kelt. ma-
ruos aus idg. mr-?/o-s, s. o Strachan Ec. 28, 202); arm, meranim „sterbe“,
                                           ,

anmer „unsterblich“, mah „Tod“ (s. o.); lit. miVs^w, mirti „sterben^', mer-
detl „im Sterben sein'', maras „Pest^^ (s. o.), lett. meris „Pest“, aksl. mre^f,
mhrUi „ sterben “ {morz, umoriti, mr^iv^ s. o.).
   Curtius^ 331, Pick            P
                          107, 284, 514, II^ 203, Hiibschmann Arm. St. I
4 If., Arm. Gr. I 472f. usw., ^mer- „sterben-' gilt mit Eecht als ein friih-
zeitig selbstandig gewordener Bedeutungsableger von mer „aufreiben^^
vgl. Grenzfalle wie f^iagaivco „reibe auf“, pass. „schwinde hin“,
                                                                  fAagao},i6g
^^^^I’w^lken       .       Lat. morhtis ist nicht von der Bed. „ sterben^ ausgegangen,
s.   mer „aufreiben'\
4.    mer- ,.aufreiben, reiben^* (Basen mer-, mera-),
      mrndti „zermalmt, zerdruckt, zerschlagt^, Ci-marlidr- „Yerderber^‘,
     Ai.
mfirnd „zermalmt, aufgerieben“ (z. T. auch Abkommlinge von *mel- ent-
haltend ?)
     Gr. fiagaivo) ,,reibe auf, verzehre, entkrafte^^, pass. „verzehre mich, ver-
schwinde allmahlich, ermatte“, fj-agaoudg „Hinschwinden, KrafteverfalP^;
uagvauai „kampfe^ (med. zu ai. mrndti zur Bed. vgl. arm. mart ,,Kampf“
                                                                 ;

u. mer-d-, viell. lat. Mars                    jLidgyagog „Stein, Pelsblock“ (vgl. rtipes       rumpo)^
                            ^          ;
                                                                                            :


spater (nach pagjuaigo}) „wei6er Stein, Marraor'' (daraus                        lat. marmor; s. Yf,
LEWb.2 s. V. m. Lit.):
     lat. mortarium „Morser“ (auf Gnind von *mr-^05 y,zerrieben^ oder '^mdr-
=== page tags? ===
0
```


## [2026-09-07T16:28:51.238Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=0\ntargets={5775:None,5780:None,5785:None,5789:None,5791:None}\nfor i,l in enumerate(lines,1):\n    if i in targets: targets[i]=leaf\n    leaf+=l.count('\\f')\nfor k,v in targets.items(): print('line',k,'leaf',v,'printed(=leaf-15)',v-15)\nEOF"
}
```


### [2026-09-07T16:28:52.539Z] TOOL RESULT

```
line 5775 leaf 226 printed(=leaf-15) 211
line 5780 leaf 226 printed(=leaf-15) 211
line 5785 leaf 227 printed(=leaf-15) 212
line 5789 leaf 227 printed(=leaf-15) 212
line 5791 leaf 227 printed(=leaf-15) 212
```


## [2026-09-07T16:28:59.027Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (225,226,227):\n    ls=[x for x in leaves[i].split('\\n') if x.strip()][:4]\n    print('leaf',i,'|', ' // '.join(x[:70] for x in ls))\n    import re\n    print('   nums:',re.findall(r'\\b\\d{3}\\b',leaves[i])[:8])\nEOF"
}
```


### [2026-09-07T16:29:00.335Z] TOOL RESULT

```
leaf 225 | BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy // brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. // brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with  // т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abb
   nums: ['862', '875', '111', '128', '154', '124', '223', '883']
leaf 226 | 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]ji // Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of th // (1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2,  // (2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 
   nums: ['418', '214', '831', '222', '234', '552', '302', '243']
leaf 227 | ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $1 // EU: ET TORR ON | // INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne - // LEXICON 203
   nums: ['109', '122', '242', '249', '203', '106', '122', '144']
```


## [2026-09-07T16:29:23.086Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD_mackenzie murdan/mard ===\"; grep -n -i \"murdan\\|^mard\\|mašyā\\|masyag\\|mardom\" PHD_mackenzie.txt | head -15\necho; echo \"=== NYB printed page of line 2386 ===\"\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0\nfor i,l in enumerate(lines,1):\n    if i==2386: print('line 2386 leaf',leaf,'printed',leaf-8)\n    if i==2591: print('line 2591 (murtan) leaf',leaf,'printed',leaf-8)\n    leaf+=l.count('\\f')\nEOF\necho \"=== SOD p.219 (leaf 286) head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==286' SOD_pages.txt | head -25"
}
```


### [2026-09-07T16:29:24.625Z] TOOL RESULT

```
=== PHD_mackenzie murdan/mard ===
393:denotes 'infinitive YMYTWNtn ' (= murdan), present stem
3465:mard [GBRA < A gbr); mltl 1M m(y)rd, N ......] man.
3466:mardan, rnar- [m)l-tn l ] perceive, notice, feel.
3469:mardana~ [mlt)nk I N ......a] manly, brave.
3472:mardom [AN8WTA < A )nfwt); mltwm 1M mrdwhm, N mardum] man,
3475:mardorn-zada~ [mltwm z)tk l IN mardum-zti'd] human being.
3571:mir-, v. murdan.
3610:murdan, mir- [YMYTWN-tn ' < A ymwtwn, '1/ mwt; mwltn l I M
3871:osmurdan,osmar-, (osmur-) [MNYTWN-tn l < A..Jmnh; 'wsmwltn l ,
3872:  'wsm'l- I M '(w)sm'r-, N fumurdan, fumar-] count, reckon; consider,
6260:  osmurdan, uskardan.                        corner gosag.
6278:contempt tarmenisnih.                        count osmurdan.
6385:demon dew, druz; female"'" eh; v.          die (v.) murdan, widardan, (widaS-
6807:hither or6n; awar!                             human being dopay, mardomzadag.
6808:hold dastan, griftan.                          humanity      mardomih,          mardom-

=== NYB printed page of line 2386 ===
line 2386 leaf 137 printed 129
line 2591 (murtan) leaf 148 printed 140
=== SOD p.219 (leaf 286) head ===
                                                             i_i                               __■_




 219
                                                                                                                        msnt
        martin(a) ? ©Khwar. mordan-, MP murdydnag;                  5488 ms* C, S                                ^»>tyJ ^J
          Pahl. masyanag
                                                                         masa ^mrts'r, mc1
        Eve, Mashiyane                                                   here, hitrier
        Hen. Magi. 138.17, 140n 4                                        STi 31.17, 69.6; BSTi 196-, C2, 23R12, 54V19; C1I
                                                                           1990 A9,/nVF5, Gil n p28
 5476 mrtyy M =» mrty
 5477 mrwrwd C                                                     5489 mspwyyc S               (^y^^j^JU^oU
                                                    *U3S
                                                                        mis-Puyec, mispuyic =»mys Pwyyc
        marw-ruS
                                                                        tenth month of the year
        Marv river
                                                                        MDii Nov. 4R1 p22; -y, Nov, 3R1 p21
        STii 3.30                                                  5490 mstVny B
                                                                        mastu/on/e/i
5478 mrws- C                              o^^r-J <0-> jo~o
     mrus ?                                                              drunkenness
```


## [2026-09-07T16:29:39.288Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=\\[pdf page \\d+\\])',t)\npat=re.compile(r'مُل|لعل مل|زرینه جام')\nfor b in blocks:\n    m=re.match(r'\\[pdf page (\\d+)\\]',b)\n    if not m: continue\n    if pat.search(b):\n        p=int(m.group(1))+1917\n        for l in b.split('\\n'):\n            if pat.search(l): print(p,'|',l[:150])\nEOF"
}
```


### [2026-09-07T16:29:40.746Z] TOOL RESULT

```
2071 | معروب )۰ 361 ۰ 13261 ۰ 3320 ( خوشهٌ انگور , شراب ) « ژابا ص 2۱۰ » قی د مُل (ضم)
```


## [2026-09-07T16:29:57.472Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT MURDER/MARE/MARBLE ===\"; grep -n \"^MURDER\\|^MARE\\|^MARBLE\\|^NIGHTMARE\\|^MORTAL\" SKT.txt | head\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor w in ['MURDER','MARE ','MARBLE']:\n    i=t.find('\\n'+w)\n    print('###',w, t[i:i+420].replace('\\n',' ') if i>0 else 'NOT FOUND')\nEOF"
}
```


### [2026-09-07T16:29:58.906Z] TOOL RESULT

```
=== SKT MURDER/MARE/MARBLE ===
### MURDER NOT FOUND
### MARE  NOT FOUND
### MARBLE NOT FOUND
```


## [2026-09-07T16:30:02.502Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"murder, sb\\|Murder\\b\" SKT.txt | head -6\necho ---\ngrep -n -i \"marble\" SKT.txt | head -4\necho ---\ngrep -n -i \"night-mare\\|nightmare\" SKT.txt | head -4"
}
```


### [2026-09-07T16:30:02.574Z] TOOL RESULT

```
1374:Bane.  harm.  (E.)  M.E,  bant.  K% bona,  a  murderer,  lane.  -^  Icrt.  bani ;  Dss. and  Swed.  bant,  death ;  Goth,  baiya,  f wound  ;  Gk.  ^vm,  murder,  ^oriir,  t munJerer.     (^BHAN.)     Dot.  biitiifuT.
12041:Murder,  Murther.  (E.)  M. morthrt.  AS.  ffK)rft<Jr.4-Goth. p.  We  also   find  A.  S.  »wrK.  I<
13449:parrioide.  (1)  themurdcjcrofs' (s>  murder  of  *  father.  i;F.  •(•i The  former  is  the  oHg.  tease,  w'  * to  F.  parricide,  I-  ptrriciM^  •  O' of  a  father.  — L.  parri ,  for  >•"*> form  of  pattr ;  mitrt^  to  uU  (1i 'CiJa,  a  slayerV     9.  The
18835:Suioide,  sclf*murder ;  one  who  dies  by his  own  hand.  (F.  — L.)  A  word  coined in  Eftgfand  (before  a.d.  i  7^0),  but  on  a  F. mo<lel ;  the  F.  sukidt,  oddly  enough,  was borrowed  from  us.  Like  homicide,  the word  has  a  double  meanmg,  (i)  answering to  L.  luicidium  *,  from  L,  shi,  of  himself and  •tidium,  a  slaying,  from  cttdcre^  to ■lay ;  (1)  —  L.  suidda  *.  from  L.  nti,  of  him- self, aua  ^((/a.  a  slayer.     See  Onaura.
23853:Burke,  to   murder  by  anHocatiea ; murder,    stifle.     1, Personal    name)     Fn the  name  of  Burkt,  an  Irishman  who  ca milled  murdcra  by  suffountion  ;  eaecuted I',dinburgh.  Jan.  jS,  1S39.
---
1459:ftM,  kn  AttoiiXTj.  (Ck.)  Namc<l it»  wrigbi.«»Gi.  3opvr»^i.  weight* t^6%,  bair7.  See  Qrftro  {i). rfUmm.  (lul.-Gk.l  Better  bari- ■  ■wntml  trrrn  for  a  deep  voice. » KonE^MW.  t  tontone.  —  Glc.  &apv-^ .deep;  uu]  v^rui.  a  tone:  we  Tone. Bit.  (F.  •  L.)  F.  basaiu.  -  L.  ta~ s  hml  kind  of  marble  in  i^thiopia.
11142:Marmoset,  a  small  Aitieric3n  monkey, (F.  — L.)  Much  older  than  the  discovery of  America ;  M.  E.  marmostttt,  a  kind  of ape  (Maundeville,  p.  aio).  —  O.  F.  mar- moset, F.  marmoHset, '  the  cock  of  a  cistern or  fountain,  any  flntick  image  from  who^e leats  water  trllleth,  any  puppet  or  andck;' Cot.  Thus  it  meant  a  grotesque  creature, '^fiS-  A  grotesque  ornament  on  a  fountain. Kormeci.  by  a  Parisian  change  of  r  to  /,  as in  chaise  for  ehaire,  (a  chnir).  from  Low  L. marmorelum,  a  thing  made  in  marble,  ap- plied to  fountains.  [Thus  the  rtu  dts  mar- mousfti  in  Paris  was  called  in  Low  Latin xticut  marmtrrtterttm ;  Littri.]  —  L.  marmor, marbie ;  sec  Marble.  %  This  seems  to  be quite  CDiitcL;  at  the  same  time,  the  trans- frrmce  in  sense  from  Mrinklng-fountain'  to 'afr  '  wta  oertMioiy  helped  on  by  confutiob
12065:leoes  of  marble.  Sec  (F.  •  L.
---
```


## [2026-09-07T16:30:07.850Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T16:30:07.895Z] TOOL RESULT

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


## [2026-09-07T16:30:12.898Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False,indent=1))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1800])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-07T16:30:14.191Z] TOOL RESULT

```
{
 "pdf_page": 316,
 "book_page": 286,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-06"
}
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتق
{
 "id": 1,
 "lang": "Avestan",
 "words": "mâtar",
 "verdict": "confirmed",
 "derivation": "Avestan mātar- f. ‘mother’ is the regular Iranian reflex of PIE *méh₂tēr (nom. *mātē, stem *māter-) via Proto-Iranian *máHtā: the PIE laryngeal *h₂ is lost with lengthening of the vowel, and *-ter- is retained. It is attested in the Younger Avesta (V. 12.1 yaṭ pitā vā mātā vā parəiriθyāiti ‘if father or mother dies’, Yt. 17.16, Y. 38.5 of animal mothers). Old Persian has the same stem, preserved only in the haplologised compound hamātā < *hama-mātā ‘having the same mother’ (Bisitun I 30, of Smerdis and Cambyses). Sanskrit mātár-, Greek Doric mātēr, Latin māter are the exact cognates, so the arrow root → Avestan is correct.",
 "derivation_fa": "اوستایی mātar- «مادر» بازماندهٔ قاعده‌مند هندواروپایی آغازین *méh₂tēr است که از راه ایرانی باستان *máHtā به اوستا رسیده؛ حنجرهٔ هندواروپایی افتاده و در عوض واکه کشیده شده است. این واژه در اوستای نو (وندیداد ۱۲،۱) گواهی دارد و در پارسی باستان تنها در ترکیب hamātā «همان مادری» (سنگ‌نوشتهٔ بیستون) مانده است. بارتولومه (فرهنگ ایرانی باستان، ستون ۱۱۶۷) و کنت همین را می‌گویند؛ پس این پیوند در نمودار نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%81%F0%90%AC%99%F0%90%AC%80%F0%90%AC%AD",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny p.694 (mā-3) does NOT list Avestan mātar-; the Avestan form stands in the neighbouring lemma 'mahter-' … 'Old Indic matar- ‘mother’, Avestan matar-, Armenian mayr … Page(s): 700-701' (POK_full.txt l.57703ff). So the claim is right but the page number should be 700."
  },
  {
   "ref": "SKT:336",
   "status": "partial",
   "note": "Skeat's entry is real but not on p.336 of the edition on disk: 'Mother (1), a female parent. [M.E.] moder. A.S. mōdor … + Du. moeder, Icel. mōðir … L. mater, Gk. mētēr, Skt. mātā, mātṛ … formed with Aryan suffix -tar (of the agent) from √MĀ, orig. to measure … Orig. sense uncertain, perhaps ‘manager’ of the household' — SKT.txt leaf 318, i.e. printed p. ~298 of the 1911 impression (leaf = printed+20); leaf 356 = p.336 is the 'Parity–Parsee' page. Content supports Av./Skt. mātar- as source of ‘mother’, but Skeat's own etymology is √MĀ ‘to measure’, i.e. ‘manager’, not Nourai's ‘feeder’."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "col. ~1167 (lea
```


## [2026-09-07T16:31:08.270Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==292' SOD_pages.txt | head -30"
}
```


### [2026-09-07T16:31:09.501Z] TOOL RESULT

```
       C2; Bcnv. Eti 324; BSTii 888.8                            5631 mync                                     jUc^ ju^w
 5622 myn      S                            <±jjui <»jLiP cjis        me(n)c (myc) ©adj. suf f.
       men ?                                                          GMS; BBB b9; C2
       thought                                                   5632 mynny C                               -Jun^fl*
       MDii, mynw; Frag. Len. 61.12; VJ n p93, 499                    mene ©pi. -f; ob. pi. -/y ^myn'ndyCy)
                                                                      inhabitant
 5623 myn-1                 (uy> ^r~> j->)o*j> j$*L- <OjuU
                                                                      C2, 54R23, 104V8, 9; BSTii 89423, 833.9
      men ©<*mdnya- ^nVyn-
      0<?)rematn, dwell                                          5633 mynsq C                                          jTu
      BBB p97 b91; GMS 683; VJ 534, 1364; TSP; STii;
                                                                      men(i)sk  ? (mynysq) -^myn-1
                                                                      resident, settler
        SCE 255; MD; C2; Frag. Len.; KG 2049; inf.
                                                                      BSTi 247; Gersh. JRAS 1946, 182
        myriyy TSP 12.55
5624 myn-2 B, S, C                                               5634 myny =» myn}y
                                  jsf^tfrfjt
     me/i/on ? ©Av. man; matnya-; Pahl. menidan                  5635 mynyq C                                         jfjA*
     (fo)think, (/<?)decide                                           menik =>myn*ndy(y)
                                                                      remaining
     VJ n p90; BSTBL, Dhu. 144, 156; Frag. 2a.24;
                                                                      STii 1.88
        MDii B-16, 6; TSP 12.58; myn>y, C2, 108V10,
        77R15; myn>wy VJ 6, lsg. impf. ?                         5636 mynysq      C =* mynsq
5625 myn-J B, M, C                        j^-u^iu^-^U            5637 myr     M       ;ujj^)<uii£ <*U ^ajjL jjj <jj
     men
                                                                                                                 (
      (fo)rcsemble                                                    meVir ? (mysy) -^myhrjmnw
      GMS 641; BBB b91; VJ n p93; C2, 31V15, 77V 5;                   sun, eleventh day of the month, Sunday
```


## [2026-09-07T16:31:17.403Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg335.png data/verification/sources/refs/ocr/BOOK/335.png\nls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-07T16:31:18.856Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T16:42:38.790Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-335.json <<'JSON'\n{\n  \"pdf_page\": 335,\n  \"book_page\": 305,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Mer 2, Mer-d, Mer-k, Mor-to, Smerd\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mer- 'to rub away, wear out, harm' (Pokorny 5. mer-, mera-, pp. 735-737, with the extensions mer-d- and mer-k-) and PIE *mer- 'to die' (Pokorny 4. mer-, p. 735), with the derivatives *mr-to- 'dead', *mor-to- / *mor-t-yo- 'mortal, man'; extended *smerd- 'pain, to bite, to stink' (Pokorny 969-970)\",\n      \"note\": \"Every element of the root box is a real reconstruction and the page numbers are right. Pokorny prints two adjacent lemmas on p.735: '4. mer-, mera-: to die' (with the note '= mer-5 become faded') and '5. mer-, mera-: to rub, wipe; to pack, rob' (pp. 735-737), and ends the second with 'See also: identical with mer-4' - i.e. Pokorny himself unites the two senses exactly as Nourai's box does. Walde-Pokorny II 276 says it explicitly: ‚mer- „sterben“ gilt mit Recht als ein fruehzeitig selbstaendig gewordener Bedeutungsableger von mer „aufreiben“‘ (WLD_Bd2_pages.txt, page header '276 mer-'). Mer-d and Mer-k are Pokorny's extensions inside mer-5 (pp.736-737): mer-d- with Av. morandat, Lat. mordeo, and mer-k- with Av. mahrka- 'death', maraxsh- 'ruin', maranca(i)ti 'destroys'. Mor-to 'mortal man' is Pokorny's 'mor-to- ‚perishable‘ in Old Indic marta-, Avestan masha- ... derived *mor-t/o- in Old Indic martya-, Avestan mashya-, Old Persian martiya-' (p.735). Smerd is Pokorny 970 'smerd-, smord-: to stink', which Pokorny derives from '(s)merd- in Modern High German schmerzen, Latin mordere, s. mer-, merd ‚chafe‘ (above S. 736 f.)'; Watkins/AHD glosses it 'smerd-. Pain. Extension of mer-2', which is Nourai's 'painful' word for word. The AHD numbering 'Mer 2' also follows Watkins ('mer-2, To rub away, harm'), not Pokorny's, and that is what Nourai cites. The only caveat is bibliographic: AHD:1529 is a page of the 1975/76 New College appendix, which is not open online; the same entry in the 1985 standalone Watkins edition is verified below.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۷۳۵ دو مدخل پشت سر هم دارد: mer-4 «مردن» و mer-5 «ساییدن، فرسودن» (۷۳۵–۷۳۷) و خود او در پایان مدخل دوم می‌نویسد «همان mer-4 است»؛ والده–پوکورنی (جلد ۲، ص ۲۷۶) روشن‌تر می‌گوید که «مردن» شاخهٔ معنایی مستقل‌شدهٔ «فرسودن» است. Mer-d و Mer-k همان گسترش‌های پوکورنی در صفحات ۷۳۶–۷۳۷ اند (اوستایی morandat و mahrka-، marancaıti) و Smerd همان smerd- صفحهٔ ۹۷۰ است که واتکینز آن را «درد، گسترشِ mer-2» معنی کرده است. پس ادعای نورایی درست است؛ تنها ارجاع AHD:1529 به پیوست چاپ ۱۹۷۵ است که به صورت آزاد در دسترس نیست و همان مدخل از چاپ ۱۹۸۵ واتکینز راستی آزموده شد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mer-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:735\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: mer-4, mera- | Meaning: to die | Note: (= mer-5 become faded)' ... 'Page(s): 735', immediately followed by 'Root / lemma: mer-5, mera- | Meaning: to rub, wipe; to pack, rob' ... 'Page(s): 735-737'. Same page also has 'mor-to- ‚perishable‘ in Old Indic marta-, Avestan masha- ... Old pers. martiya-'.\"},\n        {\"ref\": \"POK:970\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: smerd-, smord- | Meaning: to stink ... smerd- ‚stink‘ is ... a use from (s)merd- in Modern High German schmerzen, Latin mordere, s. mer-, merd ‚chafe‘ (above S. 736 f), originally also ‚beissender smell‘ ... Page(s): 970'. Nourai's gloss 'painful' matches Watkins' rendering of the same lemma.\"},\n        {\"ref\": \"AHD:1529\", \"status\": \"not_checked\", \"note\": \"The 1975/76 New College appendix (pp.1505-1550) is not open online. The same root in the 1985 Watkins standalone edition (AHD_watkins1985.txt l.753) reads 'mer-2, To rub away, harm ... II. Possibly the same root, but more likely distinct, is *mer-, ‚to die“ ... See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]' - i.e. the content Nourai cites, including the '2' of his 'Mer 2'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 276-277 (WLD_Bd2_pages.txt, page header '276 mer-')\", \"stance\": \"supports\", \"note\": \"'3. mer- „sterben“' with Av. miryeite, marata- 'gestorben, tot', masa- (*mrta-), amasa- 'unsterblich', arm. mard, ahd. mord, ags. mordor, got. maurthr, gr. brotos, ai. marta-, av. maratan-, ap. martiya-, av. masya- 'Mensch'; then '4. mer- „aufreiben, reiben“' with gr. maraino, marnamai, marmaros. Also the key sentence uniting the two senses (quoted in the note).\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt l.753-754 (mer-2) and l.962 (smerd-)\", \"stance\": \"supports\", \"note\": \"'mer-2, To rub away, harm. I.1. Germanic *maron-, goblin, in Old English mare ... NIGHTMARE ... 1.a. suffixed form *mr-tro- in Germanic *mur-thra- in Old English morthor, murder: MURDER ... 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-'; and 'smerd-. Pain. Extension of mer-2 ... [Pok. smerd- 970]'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.75 DIE; DEAD; DEATH, pp. 286-287\", \"stance\": \"supports\", \"note\": \"'1. IE *mer- ‚die‘, perh. ultimately the same as *mer- in words for ‚rub, crush‘. Walde-P. 2.276 ... Skt. mr-, Av. 3 sg. pres. miryeiti, OPers 3 sg. imperf. amariyata, pples. marata-, masa-; sbs. maratyu-, mahrka-'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt l.10658 s.v. mer- (mern-)\", \"stance\": \"supports\", \"note\": \"'mer- (mern-) ... Per. cf. miram, inf. murdan die; Arm. mernim, meranim ... Hitt. mernun ... W. meru ‚droop‘' - the same root, with the Persian verb as its reflex.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *mar 'to die', pp. 265-266\", \"stance\": \"supports\", \"note\": \"'This root has an impeccable IE etymology. PIE *mer- ‚to die‘ = LIV: 439 f. | Pok.: 735'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"mar 2; mahrka, marathyu; mareta, masa; mardta; gayo-mereta; a-mereta, amasa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All six items are genuine Avestan material from *mer-: (a) mar- 'to die' (Bartholomae col. 1143 'mar- V. ‚sterben‘. Praes. mirya-, mariya-; Aor. mari-; PPfP. marata-'), pres. mid. miryeite, with the compounds ava.miryeite and framiryeite; (b) mahrka- 'death' and marathyu- (marathyu-) 'death' - mahrka- belongs to the k-extension (Bartholomae col. 1145 'mark- V. ‚toeten, zerstoeren“ ... Inf. mahrkai, mahrkathai'), i.e. PIE *mer-k-, while maratyu- is *mr-tyu- (Skt. mrtyu-); (c) marata- and mashya- 'mortal man' = PIE *mor-to- and *mor-t-yo-, with the regular Avestan development of *-rt- to -sh- in mashya- (whence also masha-); (d) gayo.marata(n)- 'mortal life' (gaya- 'life' + marata-), the mythical first man, and (e) a-marata- / amasha- 'immortal' with the privative *n-, the epithet of the Amasha Spantas. The one soft spot is 'mardta : everyone': that is Nourai's spelling of the same marata-, and the gloss 'everyone' is not Avestan at all - it comes from Gharib's Sogdian entry 5467 'mrt mrt (mart mart) <Av. marata: everyone, each' (SOD p.218), where 'everyone' translates the Sogdian reduplication, not the Avestan word. So the item is a doublet of 'mareta' with a borrowed gloss.\",\n          \"derivation_fa\": \"همهٔ صورت‌های این جعبه اوستایی اند و از ریشهٔ *mer-: ستاک mar- «مردن» (بارتولومه، ستون ۱۱۴۳)، mahrka- «مرگ» که به گسترشِ کافی ریشه (*mer-k-) می‌رسد، marathyu- هم‌ریشه با سنسکریت mrtyu-، marata- و mashya- «مردنی، انسان» (در mashya- خوشهٔ *-rt- به -sh- بدل شده)، gayō.marata(n)- «زندگیِ میرا» و a-marata-/amasha- «بی‌مرگ» با پیشوند نفی. تنها ایراد آن است که «mardta: everyone» دوگانهٔ همین marata- است و معنای «همه‌کس» از مدخل سغدیِ غریب (mrt mrt، شمارهٔ ۵۴۶۷، ص ۲۱۸) آمده که ترجمهٔ تکرار سغدی است نه معنای واژهٔ اوستایی. در کل، ادعا با احتیاط پذیرفتنی است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"mardta : everyone\",\n          \"correct_form\": \"mareta (Av. marata-) 'mortal, man'; 'everyone' belongs to Sogdian mart mart\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mer-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:735\", \"status\": \"supports\", \"note\": \"p.735 (mer-4) lists 'participle mr-to- ‚dead‘ in Old Indic mrta- = Avestan marata-', 'n-mr-to- ‚immortal‘ ... Avestan amasa-', 'mr-tyu ‚death‘ ... Avestan maratyu-', 'mor-to- ... Avestan masa- ‚person‘, with sound change mareta-' - i.e. mar-, marata-, masa-, amasa-, maratyu- all on the cited page.\"},\n            {\"ref\": \"BQT:1872\", \"status\": \"supports\", \"note\": \"Borhan vol.3 scan pdf p.669 (the printed number on the neighbouring leaf OCRs as 1870/1872): entry 'gayomart' with Mo'in's footnote 'pahlavi Gayomart, avestai Gayō_maretan, Bartholomae 503 ... jozv-e aval „giv“ va „gaya“ be-ma'ni-ye jan va zendegi ast va jozv-e dovvom „martan“ sefat ast be-ma'ni-ye mordani va dargozashtani' - exactly Nourai's gayo-mereta.\"},\n            {\"ref\": \"BQT:1934\", \"status\": \"partial\", \"note\": \"Borhan printed 1934 (vol.4 pdf 17) is the mar/madar page; Mo'in's footnote there reads 'be-ma'ni-ye zabankar va tabah-konande ... az masdar-e MAR-e avestai va parsi-ye bastan be-ma'ni-ye mordan' - it supports the root mar- 'to die' but for the word mar 'snake', not for any word in this node.\"},\n            {\"ref\": \"BQT:1982-6\", \"status\": \"supports\", \"note\": \"Borhan printed 1982-1986 (vol.4 pdf 65-69) is the mard/mardom/mordan/mordad run; Mo'in's footnotes there give 'az rishe-ye MAR (mordan) [rk: mordan] dar gathaha MARETAN ... ' (p.1982), 'gozashtani va nist-shodani va mardom, az masdar-e MAR-e avestai va parsi-ye bastan be-ma'ni-ye mordan' (p.1983) and the AMERETAT footnote (p.1983).\"},\n            {\"ref\": \"KLN:1005\", \"status\": \"partial\", \"note\": \"In the 1966 two-volume edition p.1004-1005 (KLN_1966.txt leaf 538, which carries the running numbers 1004/1005) is the mordant-more page: 'All these words derive fr. I.-E. base *(s)merd-, a -d-enlargement of base *mer-, ‚to rub, pound, consume, wear away‘ ... See smart, v.' The Avestan forms Nourai wants are on the facing pages 1006-1007 s.v. mortal: 'cogn. with OI. mrtih, mriyate, marati, Avestic miryeite, ‚dies‘, OI. martah, ‚mortal, man‘, Avestic mereti- ... Avestic mireta-, ‚dead‘ ... All these words derive fr. I.-E. base *mer-, ‚to die‘, which is orig. identical with base *mer-, ‚to consume‘'. So the reference is right to within one leaf.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1143 and 1145-1146 (BRT.txt l.19936, l.19990ff; running head 'mahrkai 1146')\", \"stance\": \"supports\", \"note\": \"'j., p. mar- V. ‚sterben‘. Praes. mirya-, mariya-; s-Aor. mari-; PPfP. marata- ... ap. amariyata BK' and 'j., g. mark- V. ‚toeten, zerstoeren“ ... Inf. maranciyai, mahrkai, mahrkathai'; also col. 142 'a-mahrka- Adj. ‚ohne Tod‘'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 4.75, pp. 286-287\", \"stance\": \"supports\", \"note\": \"Buck's Avestan column for DIE/DEAD/DEATH: 'Av. mar-, rith-; marata-, masa-; ... (ava)marati-, maratyu-, mahrka-' - the same set of forms Nourai lists.\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib no. 5467, printed p.218 (SOD_pages.txt leaf 285)\", \"stance\": \"partial\", \"note\": \"'5467 mrt mrt B, S | mart mart <Av. marata | everyone, each' - the source of Nourai's 'mardta : everyone', but the gloss is the Sogdian reduplication's, not Avestan marata-'s.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 276\", \"stance\": \"supports\", \"note\": \"'av. marata- „gestorben, tot“, av. masa- (*mrta-, Bartholomae Wb. 1175), ai. amrta- = av. amasa- „unsterblich“ ... av. maratan-, av. masya- „Mensch“'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"mordan «مردن ( مرگ )»; mard «مرد ( مردم )»; Kîumars «کیومرث»; amordâd «امرداد ( مرداد )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Every word descends from the Old Iranian material of node #1. (a) mordan < MP murdan / pres. mir- (MacKenzie p.57 'murdan, mir- [YMYTWN-tn'] to die') < OIr. *mar- (Av. mar-, OP a-mariyata), with *mr-ta- giving MP murd, NP mord-; the verbal noun marg 'death' continues Av. mahrka- through MP marg (Horn no. 977 'merg ‚Tod‘: aw. mahrka- ‚Tod‘; phlv. marg'). (b) mard < MP mard (Book Pahlavi mlt', GBRA) < OP martiya- < PIr. *mrtah 'dead, mortal'; the plural-derived mardom < MP mardom (< *martuxma-, 'seed of man') means 'people'. (c) Kiyumars/Gayomard < MP Gayomart < Av. gayo.maratan- 'mortal life', the first man; the Arabised spelling with -th is late (Borhan itself notes the Persian original had no th). (d) amordad/mordad < MP Amurdad < Av. amaratat- 'immortality' (the abstract of a-marata-), the sixth Amahraspand and the fifth month; the popular form mordad is a haplology that reverses the sense, which is why purists write amordad. All four are the standard modern account.\",\n          \"derivation_fa\": \"هر چهار واژه ادامهٔ همان مادهٔ ایرانی باستان اند: «مردن» از فارسی میانهٔ murdan/mir- از ایرانی باستان *mar-، و «مرگ» از اوستایی mahrka- از راه فارسی میانهٔ marg (هرن، بند ۹۷۷)؛ «مرد» از فارسی میانهٔ mard از پارسی باستان martiya- (هرن، بند ۹۷۲)؛ «کیومرث» از فارسی میانهٔ Gayōmart از اوستایی gayō.maratan- «زندگیِ میرا» (حاشیهٔ معین در برهان قاطع، ص ۱۸۷۲–۴)، که ثای معرّب آن متأخر است؛ و «امرداد» از فارسی میانهٔ Amurdād از اوستایی amaratat- «بی‌مرگی»؛ صورت رایج «مرداد» از افتادن الف نفی پدید آمده و معنا را وارونه کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF%D8%A7%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:218-9\", \"status\": \"supports\", \"note\": \"Horn, Grundriss, pp.217-219 (HRN.txt leaves 239-240): no.972 'merd ‚Mann‘, merdum ... ap. vergl. martiya- ‚Mensch‘ ... aw. mareta-, maretan-; phlv. mart, martum; ai. marta-, vergl. martya-'; no.973 'murden ‚sterben‘, Praes. mir-em, murdar ‚Leichnam‘ ... ap. mar-, amariyata; aw. mar-, framairyeite; phlv. murtan, miret'; no.977 'merg ‚Tod‘: aw. mahrka- ‚Tod‘; phlv. marg'.\"},\n            {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' with Mo'in's footnotes, printed 1982-1986 (mard, mardom, mordan, mordad/amordad) and 1874 (gayomart) - quoted under node #1's ref_check; they give exactly this Avestan-to-Persian chain.\"},\n            {\"ref\": \"ZMA:21\", \"status\": \"not_checked\", \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian (1374) - refs_online.json records it as purchase-only; no open or lending copy found.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp.55, 57 (PHD_mackenzie.txt l.3465, 3472, 3610)\", \"stance\": \"supports\", \"note\": \"'mard [GBRA; mltl] man', 'mardom [ANSWTA; mltwm] man, mankind', 'murdan, mir- [YMYTWN-tn'] to die' - the Middle Persian links Nourai passes over silently.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.140\", \"stance\": \"supports\", \"note\": \"'murtan [YMYTWN-tn'; mwrtn] mir- to die ... - Av. (1142) mar-, pres. mirya-, pt. marata-'; and p.129 for Murdiyanag/Masyanag.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.465 and p.91 (ARY_latin_index_pages.txt l.13587, l.2604)\", \"stance\": \"supports\", \"note\": \"The mard entry lists 'MARTIYA (OLD PERSIAN), MART/MARD (PAHLAVI), MERD/MER (KURDISH), MAR (BALUCHI), MARTA/MARTYA (SANSKRIT)' with references to Pokorny, Barnhart (MORTAL) 679, MacKenzie (MAN) 122, Buck 81, 79; the mordad entry lists 'AMERETAT, AMURDAD (PAHLAVI)'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV s.v. *mar 'to die', p.265\", \"stance\": \"supports\", \"note\": \"'*NWIR: Widely attested: NP mir-/murdan ... MIDDLE PERSIAN: MMP myr-, BMP myr- (YMYTWN-) /mir-/ ‚to die‘ ... OLD PERSIAN: mar- ‚to die‘ = Kent: 202b'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"murdyânag, mašyânag; maša; mašyôi\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The forms are real Middle Persian, taken verbatim from Gharib p.219, but the gloss 'mortal man' is not theirs. Gharib's entry for Sogdian martin(a) 'Eve, Mashiyane' cites 'Khwar. mordan-, MP murdyanag; Pahl. masyanag' - i.e. Murdiyanag/Masyanag is the FEMALE of the pair, Zoroastrian mythology's first woman, while the male is Masya/Masi. Both continue Av. mashya- 'mortal, man' (node #1) with the Middle Persian suffix -anag: *mashya-anaka- > Masyanag. Nyberg (Glossary p.129) sets out the variants and states that 'the forms Khwar. Mard (‚Man‘) and MPrs fem. Murdiyanag are clearly WIr' - i.e. murdiyanag is the genuine south-western Iranian form beside the east-Iranian-looking mashyanag with -sh- for *-rt-. 'Masa : Adam' is the short form Masi/Masya; 'masyoi : Eve' is the Bundahishn variant Masyoi (Mo'in gives it in Latin script at Borhan p.2017). So: right forms, right root, wrong gloss and a female name presented as 'mortal man'.\",\n          \"derivation_fa\": \"صورت‌ها درست اند امّا معنی جابه‌جا شده است. غریب (ص ۲۱۹) در برابر سغدی martin(a) می‌نویسد «خوارزمی mordan-، فارسی میانه murdyānag؛ پهلوی mashyānag» و معنی را «حوا، مشیانه» می‌دهد؛ پس مشیانه/مردیانه نام زن نخستین است و نه «مردِ میرا». هر دو از اوستایی mashya- با پسوند -ānag ساخته شده اند؛ نیبرگ (واژه‌نامه، ص ۱۲۹) می‌گوید که murdiyānag صورت ایرانی غربی و mashyānag صورتی با دگرگونی شرقی *-rt- > -sh- است. پس ادعا با احتیاط پذیرفتنی است: ریشه درست، معنا نادرست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:219\", \"status\": \"supports\", \"note\": \"Gharib printed p.219 (SOD_pages.txt leaf 286), the entry running over from p.218: 'martin(a)? (c)Khwar. mordan-, MP murdydnag; Pahl. masyanag | Eve, Mashiyane | Hen. Magi. 138.17, 140n 4'. Nourai's 'murdyanag, masyanag' is copied from this line; the gloss there is 'Eve', not 'mortal man'.\"},\n            {\"ref\": \"BQT:2017\", \"status\": \"supports\", \"note\": \"Borhan printed 2017 (vol.4 pdf 100), Mo'in's footnote to masya: 'va niz masya-ye avesta [mashya] ... be-ma'ni-ye fanapazir, dargozashtani, mardom va ensan amade (rk: mard, mardom). Dar Bundahesh-e pahlavi „mashya“ be-manzele-ye Adam va „mashyoi“ be-manzele-ye Hava dar nazd-e aqvam-e sami ast ... va masyo'i ra „mashyaneh“ ...' - Adam, Eve, masyoi and masyaneh all on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.129 (NYB_vol2_glossary.txt l.2386)\", \"stance\": \"supports\", \"note\": \"'msyd msy'ny DkM 593.14-15 ... In Khwarizm mrd - mrd?nh (Biruni); MPrs mwrdy'ng (A-H I, p.220) ... The forms Khwar. Mard (‚Man“) and MPrs fem. Murdiyanag are clearly WIr, and so are also Mihreh < NW *Mithriya- and Miseh < SW *miciya- ... mahle malhe mase are EIr developments of *martiya-'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, searched (PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has mard, mardom, murdan but no entry for Masya/Masyanag (he omits mythological proper names), so it neither confirms nor contradicts.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan printed 2066 (vol.4 pdf 149)\", \"stance\": \"supports\", \"note\": \"'be-qowl-e Bundahesh „mashya“ va „mashyaneh“ (Adam va Hava-ye aryaian) dar chenin ruzi towallod ...' - again the pair as first man and first woman.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"mašyâ «مشیا»; mašyâneh «مشیانه ( مشیوئی )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The New Persian forms Mashya and Mashyaneh are the learned continuations of the Pahlavi pair of node #3: MP Masya/Masi 'the first man' > NP mashya, and MP Masyanag/Masyoi > NP mashyaneh (the -ag suffix regularly gives -a/-eh in New Persian: MP -anag > NP -aneh, as in payg > peyk, xanag > xaneh), with the variant mashyo'i taken straight from the Bundahishn. They are not inherited everyday words but names transmitted through the Zoroastrian tradition and the Persian rendering of the Pahlavi books, which is why Borhan-e Qate' and Mo'in discuss them under masya. The arrow Pahlavi to Persian is therefore correct.\",\n          \"derivation_fa\": \"«مشیا» و «مشیانه» صورت فارسی همان جفت پهلوی Māshyā/Māshyānag اند؛ پسوند -ag فارسی میانه به قاعده در فارسی نو به -ه بدل می‌شود (مانند xānag > خانه)، و صورت «مشیوئی» راست از بندهشن گرفته شده است. این دو واژه میراثی عامیانه نیستند بلکه از راه سنت زردشتی و متن‌های پهلوی به فارسی رسیده اند؛ به همین سبب برهان قاطع و حاشیهٔ معین آن‌ها را ذیل «مشیا» آورده اند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2017\", \"status\": \"supports\", \"note\": \"Borhan printed 2017 (vol.4 pdf 100) is the masya entry itself ('mashya - be-fath-e avval be-vazn-e ashya ...') with Mo'in's footnote naming mashya = Adam, mashyoi = Hava and masyaneh; the Persian spellings mashya and mashyaneh (masyo'i) are exactly Nourai's.\"},\n            {\"ref\": \"SOD:218\", \"status\": \"partial\", \"note\": \"Gharib printed p.218 has the Sogdian mrty/mrtxmy family ('5474 mrty ... (c)<OP martiya-, Yaghn. morti'), but the Masyanag material Nourai needs begins on p.219; the Persian forms themselves are not in Gharib at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (MON_part2.txt, Adena 2-vol abridgement)\", \"stance\": \"supports\", \"note\": \"'be-qowl-e Bundahesh „mashya“ va „mashyaneh“ (Adam va Hava-ye aryaian) dar chenin ruzi towallod yafte-and' - the same pair, in Mo'in's own words (page numbers of the 6-vol edition cannot be mapped in the abridgement).\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.129\", \"stance\": \"partial\", \"note\": \"Nyberg dismisses the reconstructions '*Masyay - *Masyanay' used by Christensen as 'nowhere to be found, and fictitious', while accepting the attested msy'/msy'ny; so the Persian mashya/mashyaneh reflect the attested Pahlavi spellings, not a reconstruction.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Avestan\",\n          \"words\": \"awiš-mar, wizmar\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Neither aiwish-mar- nor *vizmar- is an attested Avestan compound; both are reconstructions invented to explain NP pazmurdan, and modern Iranian etymology has abandoned them. Horn (Grundriss no.313, p.69) proposed 'ap. patis bezw. aw. aiwis + mar-' for pizmurden, and that is Nourai's 'awis-mar'. Huebschmann's Persische Studien p.41 - the reference Nourai's own NOTE flags - answers: 'Die von Noeldeke und Horn erwaehnte Form guzs-murdan des Judenpersischen zeigt, dass pizmurdan ‚verwelken‘ ueber aelteres bizmurdan auf *vizmurdan zurueckgeht. Damit faellt Horn's Etymologie, insbesondere piz- aus patis' - hence Nourai's second form 'wizmar'. Cheung's Etymological Dictionary of the Iranian Verb (2007, s.v. *mar 'to die', pp.265-266) settles it differently again: the prefix is *pari-, cf. Choresmian prmy- 'to wither, fade (of plants, fire)', Shughni (Baj.) parmir-/parmud, Wakhi parmor-/parmord- 'to wither', Yidgha parmorya 'withering', all beside NP pazmurdan/pazmir-. Avestan itself compounds mar- only with *ava- and *fra- (Cheung's Liste 43). So the parent box as drawn is not Avestan fact, and its prefix is wrong on the current view.\",\n          \"derivation_fa\": \"هیچ یک از دو صورت aiwish-mar و *vizmar در اوستا گواهی ندارد؛ هر دو بازسازی برای توضیح «پژمردن» اند. هرن (بند ۳۱۳، ص ۶۹) پیشوند را patiš/aiwiš دانست، ولی هوبشمان (مطالعات فارسی، ص ۴۱) بر پایهٔ صورت یهودی‌فارسی guž-murdan آن را رد کرد و *vizmurdan را پیش نهاد — همین که یادداشت خودِ نمودار به آن اشاره دارد. پژوهش امروزی (چونگ ۲۰۰۷، ذیل *mar) پیشوند را *pari- می‌داند، به گواهیِ خوارزمی prmy-، شغنی parmir-، وخی parmor- «پژمردن»؛ و در خود اوستا mar- تنها با ava- و fra- ترکیب شده است. پس پژوهش امروزی این جعبه را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%85%D8%B1%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AEF:378\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi is the Persian translation of Horn with Huebschmann's notes; refs_online.json records that no copy is online. It can be reached only through HRN/HUB, checked here. Mo'in's own footnote to pazmordan (Borhan p.400) cites the same work by entry number, 'ESHQ 313', i.e. Horn's no. 313.\"},\n            {\"ref\": \"HRN:69\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.69 no.313: 'pizmurden, pezmurden ‚erschlaffen, verbluehen‘, pizmerden ..., pizmeraniden (Sahn.). ap. patis bezw. aw. aiwis + mar-. piz- scheint wegen jued.-pers. ... ein alter Fehler fuer biz- zu sein (de Lagarde, Persische Studien, 75)'. So the aiwis-mar- of the chart is Horn's, quoted correctly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Huebschmann, Persische Studien p.41 no.313 (HUB.txt leaf 51)\", \"stance\": \"contradicts\", \"note\": \"'Die von Noeldeke und Horn erwaehnte Form guzs-murdan des Judenpersischen zeigt, dass pizmurdan ‚verwelken‘ ueber aelteres bizmurdan auf *vizmurdan zurueckgeht. Damit faellt Horn's Etymologie, insbesondere piz- aus patis.' The chart's NOTE reports this correctly.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV pp.265-266 s.v. *mar 'to die' (CHEUNG.txt l.17490-17545)\", \"stance\": \"contradicts\", \"note\": \"'*NWIR: ... Tal. marde ‚to die‘ || (+ *pari-) NP pazmurdan/pazmir- ‚to wither, fade‘ ... *CHORESMIAN: *my- ... || (+ *pari-) prmy- ‚to wither, fade (of plants, fire)‘ ... *NEIR: ... || (+ *pari-) Sh. (Baj.) parmir-/parmud, Wa. parmor-/parmord- ‚to wither‘'. Avestan is listed only with *ava- and *fra-.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Woerterbuch, searched for aiwis-mar- / vi-mar-\", \"stance\": \"silent\", \"note\": \"Under mar- 'sterben' (col.1143) Bartholomae records only the compounds with ava- and fra- (ava.miryeite, framiryeite); there is no aiwis- or vi- compound of this verb, which is why both parent forms are reconstructions.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"pajhmordan «پژمردن ( پژمریدن )»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The word is real and old (Shahnameh pazmuraned, Vis o Ramin pizmeridan) and it does belong to this root: it is a prefixed compound of the same verb as mordan, so the arrow to the Mer root is right. What is wrong is the prefix in the parent box. On the modern account (Cheung 2007) NP pazmurdan/pazmir- 'to wither, fade' goes back to *pari-mar-, the same formation as Choresmian prmy-, Shughni parmir-, Wakhi parmor- 'to wither'; *pari- gives Persian paz-/paj- exactly as in pazhuhidan and pazman, the two other words Huebschmann and Mo'in cite in the same breath. Huebschmann had already rejected Horn's patis-/aiwis- in favour of *viz-, and Mo'in's footnote to the Borhan entry repeats Horn's version with the caveat that 'paz is apparently an old error for baz'. Semantically the shift is 'to die (of a plant)' > 'to wilt, fade', the same shift Avestan shows in fra-mar- 'to die, wither'.\",\n          \"derivation_fa\": \"«پژمردن» واژه‌ای کهن است (شاهنامه: همی پژمراند رخِ ارغوان) و بی‌گفت‌وگو از همان ریشهٔ mar- «مردن» است؛ پس جهتِ پیکان درست است. امّا پیشوند آن بر پایهٔ پژوهش امروزی *pari- است نه aiwiš-؛ همان پیشوندی که در «پژوهیدن» و «پژمان» هم دیده می‌شود. حاشیهٔ معین در برهان قاطع (ص ۴۰۰) روایت هرن را می‌آورد و می‌افزاید که «پژ ظاهراً اشتباهی قدمی است بجای بژ». تحول معنایی همان «مردنِ گیاه» > «پژمردن» است. پس: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%DA%98%D9%85%D8%B1%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:400\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' vol.1, the pazmordan run (BQT_v1_pages.txt leaf 624, i.e. printed c.398-400): 'pazmordan va pazmoridan - be-kasr-e avval va zamm-e sevvom va fath-e panjom, parsi-ye bastan patis (avesta aiwis) + -mar. paz zaheran eshtebahi qadami ast be-jay-e baz *biz. Va viz dar pazhuhidan va pazman ham dide mishavad ‚ESHQ 313‘' - plus 'pazmoranidan ... hami pazmuraned rox-e arghavan (Ferdowsi)'. The entry, its Persian spellings and Nourai's derivation all sit here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.265 s.v. *mar\", \"stance\": \"partial\", \"note\": \"Confirms the word and the root but with a different prefix: '(+ *pari-) NP pazmurdan/pazmir- ‚to wither, fade‘'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no.313, p.69\", \"stance\": \"supports\", \"note\": \"Horn has the word with this meaning and root ('pizmurden ... ‚erschlaffen, verbluehen‘ ... + mar-'), differing only in the prefix.\"},\n            {\"src\": \"HUB\", \"where\": \"Huebschmann p.41 no.313\", \"stance\": \"partial\", \"note\": \"Accepts the root but replaces Horn's prefix with *viz-: 'pizmurdan ‚verwelken‘ ueber aelteres bizmurdan auf *vizmurdan zurueckgeht'.\"},\n            {\"src\": \"MON\", \"where\": \"Wiktionary (en) s.v. pazmordan, archived\", \"stance\": \"silent\", \"note\": \"The Wiktionary entry has the verb and its conjugation but gives no etymology section at all, so it adds nothing either way.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Avestan\",\n          \"words\": \"morandat, marenčaiti; maraxš; mared\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"This box is Pokorny's mer-d- and mer-k- extensions, quoted accurately. Av. 3sg. morandat (= *mrnd-) 'destroys' belongs to mer-d-, beside Skt. mrdnati/mardati 'grinds, crushes' and Lat. mordeo 'I bite'; Av. maranca(i)ti 'injures, destroys' and the s-aorist maraxsh- 'ruin, destruction' belong to mer-k-, beside Skt. marcayati 'injures' and marka- 'death' = Av. mahrka-. Bartholomae sets the whole family under one verb: 'mark- V. ‚toeten, zerstoeren“, und zwar vom Toeten und Zerstoeren ahurischer Schoepfungen. Praes. maranu-, maranca-, ... s-Aor. maraxsh-: mraxsh-; Inf. maranciyai, mahrkai' (col.1145-1146). Kent p.203 gives the d-form under Old Persian: 'mard- vb. ‚crush‘: Av. marad- ‚destroy‘, Skt. mrd- ‚rub, crush‘, Lt. mordet ‚bites‘, pIE *merd-', which is Nourai's 'mared : destroy'. The semantics ('rub away' > 'crush' > 'destroy') is exactly the bridge Walde-Pokorny uses to unite the two mer- roots.\",\n          \"derivation_fa\": \"این جعبه همان گسترش‌های mer-d- و mer-k- پوکورنی است. اوستایی morandat (از *mrnd-) «ویران می‌کند» هم‌ریشه با سنسکریت mrdnāti و لاتین mordeō است، و maraŋcaiti «می‌شکند، نابود می‌کند» با ماضیِ s-دارِ maraނš- به گسترشِ کافی می‌رسد که mahrka- «مرگ» نیز از همین جاست. بارتولومه (ستون ۱۱۴۵) همه را زیر فعل mark- «کشتن، ویران کردن» می‌آورد و کنت (ص ۲۰۳) صورت d-دار را. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mer-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:737\", \"status\": \"supports\", \"note\": \"Inside mer-5 (pp.735-737) POK_full.txt has 'Avestan 3. Sg. morandat (= mrnd-) ‚destroys‘' in the mer-d- section and, in the mer-k- section, 'marka- m. ‚dying, death‘ = Avestan mahrka- ‚death‘ ... Avestan maraxs ‚ruin, destruction‘, Avestan marancaiti ‚injures, hurts, disables, destructs‘' - the last two pages of the lemma, i.e. 736-737 as cited.\"},\n            {\"ref\": \"KNT:203\", \"status\": \"partial\", \"note\": \"Kent's Lexicon p.203 (KNT.txt leaf 227, running head 'LEXICON 203') has 'mard- vb. ‚crush‘: Av. marad- ‚destroy‘, Skt. mrd- ‚rub, crush‘, Lt. mordet ‚bites‘, pIE *merd- (Foy, KZ 35.48)' - it supports 'mared: destroy' but says nothing about maranca(i)ti or maraxsh-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1145-1146 (BRT.txt l.19990ff, running head 'mahrkai 1146')\", \"stance\": \"supports\", \"note\": \"'j., g. mark- V. ‚toeten, zerstoeren“ ... Praes. 8 maranu-, 9 maranca-, 16 (Des.) mimaraxsa-, ... s-Aor. maraxs: mraxs; PFP. maranciyanta-, Inf. maranciyai, mahrkai, mahrkathai' with the Vidivdad and Yasna citations.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 276-277\", \"stance\": \"supports\", \"note\": \"The same forms in Walde-Pokorny's mer- 'aufreiben' with its d- and k-extensions (ai. mrnati, gr. maraino, marnamai; and the k-forms with av. mahrka-).\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 mer-2, section I.4\", \"stance\": \"partial\", \"note\": \"'4. Possibly extended root *merd- in Latin mordere (past participle morsus), to bite' - Watkins keeps the d-extension but marks it 'possibly' and does not cite the Avestan forms.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Old Persian\",\n          \"words\": \"mar, mariya; marta; martiya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are Achaemenid Old Persian, and Kent's Lexicon gives them on precisely the pages cited. mar- 'die' is attested in the middle imperfect a-mariyata 'he died' (Bisitun I 43, of Cambyses), with the -ya- present *mr-ya- (Kent's 'mariya'); marta- is the perfect passive participle *mr-to- 'dead'; martiya- 'man, mortal man' is the *mor-t-yo- formation and the ordinary Achaemenid word for 'man' (DB I 21 and dozens more), the direct ancestor of NP mard. Old Persian therefore shows the same three grades as Avestan (full grade in the root, zero grade in the participle, o-grade in the noun) and the arrow root to Old Persian is correct.\",\n          \"derivation_fa\": \"سه صورتِ این جعبه همه پارسی باستانِ هخامنشی اند: mar- «مردن» در ماضیِ a-mariyatā «مرد» (بیستون ۱،۴۳ دربارهٔ کمبوجیه)، marta- «مرده» صفت مفعولی از *mr-to-، و martiya- «مرد، انسان» از *mor-t-yo- که واژهٔ معمولِ سنگ‌نوشته‌ها و نیای مستقیمِ «مرد» است. کنت (صفحات ۲۰۲ و ۲۰۳) هر سه را دقیقاً در همین صفحات می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:202,203\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 226 = printed p.202: 'mar- vb. ‚die‘: Av. mar-, pres. miryeite, Skt. mriyate, Lt. moritur, pIE *mer-. See also uvamarsiyu-, marika-, maria-, martiya-. amariyata imf. mid. DB 1.43' and 'marta- ptc. as adj. ‚dead‘: Av. marata-, N Pers. murd, Skt. mrta-, Gk. brotos ... pIE *mrtos'. Leaf 227 = printed p.203 (running head 'LEXICON 203') carries the long attestation list of martiya-.\"},\n            {\"ref\": \"SOD:218\", \"status\": \"supports\", \"note\": \"Gharib printed p.218: '5455 mrt'y B | marti (c)OP martiya | man' and '5474 mrty | marti/i ... (c)<OP martiya-, Yaghn. morti' - Gharib herself marks Old Persian martiya- as the comparandum.\"},\n            {\"ref\": \"SOD:225\", \"status\": \"not_found\", \"note\": \"Gharib printed p.225 (SOD_pages.txt leaf 292) is the myn-/myr run (myn-1 'remain, dwell', myn-2 'think', myr 'sun, Sunday'); nothing about martiya or mrty. The 225 of Nourai's 'SOD:218,225' could not be traced (it is not an entry number for this family either: nos. 5453-5490 are all on pp.218-219).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, sections 144.IV, 147.II and pp.202-203\", \"stance\": \"supports\", \"note\": \"Besides the lexicon entries, Kent's morphology lists 'marsiy-u- ‚death‘ in adj. uva-marsiyu-' and 'mard-u- in Marduniya-' among the u-stems, i.e. the same root family.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1143 (BRT.txt l.19936)\", \"stance\": \"supports\", \"note\": \"Bartholomae's headword is joint Avestan-Old Persian ('j., p. mar- V. ‚sterben‘') and cites 'ap. amariyata BK' (Bisitun) with 'uvamarsiyus'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 276\", \"stance\": \"supports\", \"note\": \"'ap. amariyata „er starb“ ... to-Ptc. ai. mrta- = av. marata- „gestorben, tot“ ... ap. martiya-, av. masya- „Mensch“'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.265\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: mar- ‚to die‘ = Kent: 202b. MED.; Pres. ja-: impf. IND. 3sg. am(a)riyata <a-m-r-i-y-t-a> (DB 1.43); Partic.: perf. pass. m(a)rta- ‚dead‘'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Sogdian\",\n          \"words\": \"marty\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Sogdian word is right and the etymology in Gharib's dictionary is the one Nourai copied: '5474 mrty | marti/i ... <OP martiya-, Yaghn. morti' (p.218), with the parallel entry '5455 mrt'y | marti (c)OP martiya | man'. The one correction a modern Iranist would make is the direction of the arrow: Sogdian is an East Iranian language and cannot descend from Old Persian, a South-West Iranian dialect. Sogdian mrty /marti/ 'man' continues Proto-Iranian *mrtya- directly (whence also the Sogdian compound mrtxmy 'man, person' < *mrtaxmaka-, and Yaghnobi morti), so it is a COGNATE of Old Persian martiya-, not a derivative of it. Gharib's '(c)OP martiya-' sign is a comparison mark, and Nourai has turned it into descent.\",\n          \"derivation_fa\": \"واژهٔ سغدی mrty /marti/ «مرد» درست است و غریب (ص ۲۱۸) هم آن را در برابر پارسی باستان martiya- می‌نشاند؛ امّا سغدی از شاخهٔ ایرانی شرقی است و نمی‌تواند از پارسی باستان (جنوب غربی) گرفته شده باشد؛ بلکه هر دو از ایرانی آغازین *mrtya- برآمده و هم‌ریشه (cognate) اند نه درپی. گواهِ این سخن، ترکیب سغدی mrtxmy «انسان» و یغنابی morti است. پس واژه درست است ولی جهتِ پیکان باید با احتیاط خوانده شود.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:218\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary printed p.218 (SOD_pages.txt leaf 285): '5474 mrty | marti/i | =>mrt'y (mrtyy) (c)<OP martiya-, Yaghn. morti' and '5455 mrt'y B | marti (c)OP martiya =>mrty | man | SCE 374 ...'. Also 5458 mrtym'k, 5473 mrtxmy(y) 'man, person' from the same stem.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 5455, 5458, 5473, 5474 (pp.218-219)\", \"stance\": \"supports\", \"note\": \"The whole Sogdian family: mrty 'man', mrtxmy(y) 'man, person', mrtym'k 'man, human, mankind', with attestations in SCE, VJ, BSTBL, C2.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.265\", \"stance\": \"partial\", \"note\": \"'*SOGDIAN: BSogd. myr-, CSogd. myr-, MSogd. myr- ‚to die‘' - Sogdian has its own inherited reflexes of the verb, which is why the noun too is inherited rather than borrowed from Old Persian.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 276\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny lists the *mor-t-yo- noun for Indo-Iranian generally ('ai. martya-, ap. martiya-, av. masya-'), i.e. a common Indo-Iranian formation, not a Persian innovation.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Old Persian\",\n          \"words\": \"mard; mard-una\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Half of this box is solid and half is Kent's guess. OP mard- 'to crush' is a real verbal root (Kent p.203: 'mard- vb. ‚crush‘: Av. marad- ‚destroy‘, Skt. mrd- ‚rub, crush‘, Lt. mordet ‚bites‘, pIE *merd- (Foy, KZ 35.48)'), and it is the d-extension of *mer- 'to rub away' - so the arrow from the root is right. 'mard-una : crusher of grapes into wine, wine merchant' is not an attested Old Persian word: it is Kent's tentative back-formation from the personal name Marduniya- (Greek Mardonios, the Mardonius of Herodotus, son of Gobryas), which Kent explains as 'perhaps deriv. to *marduna- ‚vintner‘ ... which possibly contains root mard- ‚crush (the grapes in the wine-making)‘', adding 'otherwise Justi, INB 195'. In his morphology he lists the name among 'names denoting occupations, as perhaps in the adjectival derivative, possibly patronymic, Mardun-iya- ‚Vintner's son‘'. So the form should carry an asterisk and the two 'perhaps'es Kent gives it.\",\n          \"derivation_fa\": \"نیمی از این جعبه مستند است و نیمی حدسِ کنت. ریشهٔ پارسی باستان mard- «خرد کردن، فشردن» واقعی است (کنت، ص ۲۰۳؛ اوستایی marəd-، سنسکریت mrd-، لاتین mordet) و همان گسترشِ d-دارِ *mer- است. امّا mard-una «فشارندهٔ انگور، می‌فروش» در سنگ‌نوشته‌ها گواهی ندارد؛ بازسازی *marduna- از نامِ خاصِ Marduniya (مردونیوسِ هرودوت) است که خودِ کنت آن را با دو «شاید» می‌آورد و نظرِ دیگرِ یوستی را هم یاد می‌کند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:203\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 227 (printed 203): 'mard- vb. ‚crush‘: Av. marad- ‚destroy‘, Skt. mrd- ‚rub, crush‘, Lt. mordet ‚bites‘, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.' and 'Marduniya- sb. ‚Mardonius, father of Gobryas‘: Elam. mar-du-nu-ia, Gk. Mardonios; perhaps deriv. to *marduna- ‚vintner‘ ... cf. NPers mul ‚wine‘, Skt. mrdvika- ‚grapevine‘ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‚crush (the grapes in the wine-making)‘'. Nourai's gloss is a compression of this sentence.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian sec. 156.IV (KNT.txt l.1956)\", \"stance\": \"partial\", \"note\": \"'Or names may denote occupations, as perhaps in the adjectival derivative, possibly patronymic, Mardun-iya- ‚Vintner's son‘' - Kent's own hedging.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny mer-5, pp.736-737 (mer-d- section)\", \"stance\": \"supports\", \"note\": \"'Old Indic mrdnati (mardati, mardayati) ‚grinds, crushes, rubs‘, Avestan 3. Sg. morandat ‚destroys‘ ... Latin mordeo ‚to bite‘' - the root mard- 'crush' is genuinely this extension of *mer-.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae AW col. 1151 (cited by Kent)\", \"stance\": \"partial\", \"note\": \"Kent refers to 'Bthl. AW 1151' for the *marduna- 'vintner' idea, i.e. the suggestion is Bartholomae's; the column falls in the mar-/mark- range of the dictionary verified above, and Bartholomae offers it as an etymology of the name, not as an attested common noun.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"mol «مُل»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real - mol/mul 'wine', a literary archaism of the classical poets, and Nourai quotes Onsori for it - but its modern etymology is not this root. Wiktionary, following the standard Iranist account, has: 'Borrowed from Sogdian mwd /mud/ or less likely from Bactrian molo ‚wine‘, both from Proto-Iranian *madu, from Proto-Indo-Iranian *madhu, from Proto-Indo-European *medhu. Doublet of mey.' That is, mol belongs with mey, mead, Sanskrit madhu - the root Nourai himself cross-references in the chart's NOTE ('For another possible root of Persian mol: wine see root Medhu'). The reason the word appears here at all is Kent's parenthesis under Marduniya-: 'perhaps deriv. to *marduna- ‚vintner‘ ... cf. NPers mul ‚wine‘', which was already a guess in 1950 and would in any case require an unexplained loss of the -d-. So the node is a legitimate reference to Kent but is superseded: the modern view puts mol under Medhu.\",\n          \"derivation_fa\": \"«مُل» واژه‌ای ادبی و کهن برای شراب است، امّا ریشه‌شناسی امروزی آن را از این ریشه نمی‌داند: به گواهی ویکی‌واژه و دیدگاه رایج، مُل وام‌واژه‌ای است از سغدی mwδ (یا کمتر احتمال باختری molo) از ایرانی آغازین *madu از هندواروپایی *medʰu، یعنی دوگانهٔ «می» و هم‌ریشه با سنسکریت madhu. خود نورایی هم در یادداشت به ریشهٔ Medhu ارجاع داده است. منشأ این جعبه تنها جملهٔ کنت (ص ۲۰۳) است که در توضیح نام Marduniya «قیاس کنید با فارسی mul شراب» را افزوده؛ پژوهش امروزی این را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:203\", \"status\": \"supports\", \"note\": \"Kent p.203 s.v. Marduniya- does contain the words Nourai relies on: 'perhaps deriv. to *marduna- ‚vintner‘ ... cf. NPers mul ‚wine‘, Skt. mrdvika- ‚grapevine‘ (Bthl. AW 1151; otherwise Justi, INB 195)'. The reference is quoted faithfully; it is the claim, not the citation, that modern scholarship rejects.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Wiktionary (en) s.v. mol, Persian Etymology 1, archived\", \"stance\": \"contradicts\", \"note\": \"'Borrowed from Sogdian mwd /mud/ or less likely from Bactrian molo (‚wine‘), both from Proto-Iranian *madu, from Proto-Indo-Iranian *madhu, from Proto-Indo-European *medhu. Doublet of mey.'\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.4, printed 2071 (vol.4 pdf 154)\", \"stance\": \"partial\", \"note\": \"Mo'in's footnote in the mo/mol run glosses 'mol (zamm)' beside Latin-script forms and 'khushe-ye angur, sharab' with a reference to Zhaba p.410; the note connects mol with the vine/wine vocabulary, not with mard- 'crush'.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent p.203, and Justi INB 195 as cited there\", \"stance\": \"partial\", \"note\": \"Kent expressly offers an alternative ('otherwise Justi, INB 195'), so even the source of the claim does not present it as established.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Greek\",\n          \"words\": \"maraino; marmaros; marmaron\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek marainein 'to waste away, wither, quench' is a certain member of this root: Pokorny puts it in mer-5 ('gr. maraino ‚rub, wipe, consume, weaken‘, Pass. ‚verzehre myself, verschwinde allmaehlich‘, marasmos ‚Hinschwinden‘') and Watkins gives it as mer-2, I.2 (whence MARASMUS, AMARANTH). marmaros/marmaron 'block of stone, marble' is the contested item. The traditional etymology, which Nourai follows through Pokorny 736, is: 'marmaros ‚stone, boulder‘ (compare Latin rupes : rumpo), later (after marmairo) ‚white stone, marble‘ (out of it Latin marmor)' - i.e. reduplicated *mer- 'rub, crush', with the 'gleaming' sense a secondary contamination from marmairein 'to sparkle'. Frisk keeps the root but derives it from marnamai 'to fight' (itself Pokorny's mer-5); Beekes (2010) rejects an IE source altogether and calls marmaros Pre-Greek, and Etymonline says simply 'of unknown origin, perhaps originally an adjective meaning ‚sparkling‘'. So maraino is confirmed, marmaros is a live dispute in which Nourai's source is the older consensus.\",\n          \"derivation_fa\": \"یونانی marainō «پژمرداندن، فرسودن» بی‌گمان از همین ریشه است (پوکورنی ذیل mer-5، واتکینز ذیل mer-2). امّا marmaros «سنگ، مرمر» مورد اختلاف است: پوکورنی (ص ۷۳۶) آن را از همین ریشه و به معنای نخستین «تخته‌سنگ» می‌داند که بعدها به قیاس marmairō «درخشیدن» معنای «سنگ سپید، مرمر» گرفته؛ فریسک آن را به marnamai می‌برد و بیکس (۲۰۱۰) ریشهٔ هندواروپایی را رد و آن را پیش‌یونانی (Pre-Greek) می‌شمارد. پس بخش نخست درست است و بخش دوم با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CE%BC%CE%B1%CF%81%CE%BF%CF%82\",\n            \"https://www.etymonline.com/word/marble\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:736\", \"status\": \"supports\", \"note\": \"Within mer-5 (735-737), the Greek section - which falls on p.736 of the printed lemma - reads: 'gr. maraino ‚rub, wipe, consume, weaken‘, Pass. ... marasmos ‚Hinschwinden, Kraefteverfall‘; marnamai ‚fight‘; marmaros ‚stone, boulder‘ (compare Latin rupes : rumpo), later (after marmairo) ‚white stone, marble‘ (out of it Latin marmor)'. Nourai's three Greek words and their glosses come from this passage.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"mer-5, pp.735-737\", \"stance\": \"supports\", \"note\": \"As quoted; Pokorny explicitly derives Latin marmor from the Greek word.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 277 (under '4. mer- aufreiben, reiben')\", \"stance\": \"supports\", \"note\": \"'Gr. maraino „reibe auf, verzehre, entkraefte“ ... marnamai „kaempfe“ ... marmaros „Stein, Felsblock“ (vgl. rupes : rumpo); spaeter (nach marmairo) „weisser Stein, Marmor“ (daraus lat. marmor; s. WH LEWb.2 s.v.)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.982 s.v. marble, and s.v. marcescent/marasmus\", \"stance\": \"supports\", \"note\": \"'fr. Gk. marmaros, ‚white, glistening stone‘, fr. orig. ‚stone, rock‘, rel. to marnamai, ‚I fight, battle‘, lit. ‚I strike myself‘, marainoi, ‚I put out, quench, extinguish‘, and cogn. with OI. mrnati, ‚crushes, bruises‘, fr. I.-E. base *mer-, ‚to rub, consume, wear away‘ ... The sense development of Gk. marmaros was influenced by marmairein, ‚to shine‘, to which, however, it is not related.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, mer-2 I.2\", \"stance\": \"partial\", \"note\": \"'2. Greek marainein, to waste away, wither: MARASMUS; AMARANTH' - Watkins keeps marainein under the root but does NOT list marmaros/marble there, which is a quiet vote for the sceptics.\"},\n            {\"src\": \"IEC\", \"where\": \"Wiktionary s.v. marmaros (archived), reporting Frisk, Mazon and Beekes\", \"stance\": \"contradicts\", \"note\": \"'Of uncertain origin. Based on the original sense of ‚stone; rock‘, Frisk derives the word from the root of marnamai ... others, such as Mazon, prefer to directly connect the word to marmairo. Due to the lack of strong evidence of connection to other words ... Beekes suggests Pre-Greek origin. An alternative theory by Roberts suggests a reduplicative formation from PIE *mer- (‚to rub away; to cause harm; to die‘), in the sense of marble's fragility.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"marmar «مَرمَر ( مرمرین )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian marmar 'marble' is a loanword from Greek marmaros, exactly as drawn. Mo'in says so in as many words in his footnote to the Borhan entry: 'marmar - be-fath-e do mim, az yunani marmaros; arabi va torki ‚marmar‘' (Borhan-e Qate' printed p.1996). The Greek word reached Persian in the Hellenistic/late-antique Near East along with the stone trade and the Byzantine-Sasanian building vocabulary, and it is shared with Aramaic/Syriac marmara, Arabic marmar and Turkish mermer (Wiktionary derives Turkish mermer 'from either Classical Persian marmar or Arabic marmar, both from Ancient Greek marmaros'), so an Aramaic or Arabic relay cannot be excluded for Persian either. The reduplicated shape was kept intact because Persian tolerates the mar-mar pattern; the adjective marmarin is the Persian -in suffix on the loan.\",\n          \"derivation_fa\": \"«مَرمَر» وام‌واژه‌ای است از یونانی marmaros؛ معین در حاشیهٔ برهان قاطع (ص ۱۹۹۶) به صراحت می‌نویسد: «مرمر — بفتح دو میم، از یونانی marmaros؛ عربی و ترکی مرمر». این واژه در دوران هلنی‌مأب و با دادوستدِ سنگ و اصطلاحات معماری به خاورمیانه راه یافت و با آرامی/سریانی marmarā، عربی مرمر و ترکی mermer مشترک است؛ پس واسطهٔ آرامی یا عربی را نمی‌توان رد کرد. «مرمرین» هم همان وام‌واژه با پسوند فارسیِ -ین است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%85%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%CE%BC%CE%AC%CF%81%CE%BC%CE%B1%CF%81%CE%BF%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1996\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' printed 1996 = vol.4 pdf p.79 (BQT_v4_pages.txt l.3087): 'marmar - be-fath-e do mim, az yunani MARMAROS; arabi va torki ‚marmar‘ ...'. The cited page is exactly right.\"},\n            {\"ref\": \"MON:4045\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi is online only as entry text (vajehyab/abadis) with no page mapping, and the local copy is the 2-vol Adena abridgement without the 6-vol pagination; p.4045 falls in vol.4, the volume of foreign words and compounds, which is where a Greek loan like marmar belongs, but the page itself could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p.468 (ARY_latin_index_pages.txt l.13689-13706)\", \"stance\": \"supports\", \"note\": \"The marmar entry lines up 'MARMAROS (GREEK), MARMOR (LATIN), MARBRE (FRENCH), MARMOR (DANISH/SWEDISH/NORWEGIAN), MARMER (DUTCH), MARMUR (POLISH), MRAMUR (CZECH), MARMAR (ARMENIAN), MURNAS/MRNATI (SANSKRIT)' - the Greek word as source and the Sanskrit root-forms as cognates.\"},\n            {\"src\": \"MON\", \"where\": \"Wiktionary (en) s.v. marmar, Persian section (archived)\", \"stance\": \"supports\", \"note\": \"'Persian: Etymology - From Ancient Greek marmaros', with the Turkish entry adding 'Borrowed from either Classical Persian marmar or Arabic marmar, both from Ancient Greek marmaros'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.982 s.v. marble\", \"stance\": \"supports\", \"note\": \"Confirms the Greek word's meaning and spread ('Gk. marmaros, ‚white, glistening stone‘'), the source of the Persian, Arabic and Turkish forms.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"marmor\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin marmor, -oris n. 'marble' is real and is the ancestor of the Romance and English words. Whether it was BORROWED from Greek, as the chart's arrow says, is the open question. Pokorny (p.736) and Walde-Pokorny (II 277) say plainly 'out of it Latin marmor' / 'daraus lat. marmor', and Klein agrees ('fr. VL. marmorem, acc. of L. marmor ... fr. Gk. marmaros'). Etymonline is more cautious: 'from Latin marmor, from or cognate with Greek marmaros' - i.e. both may be independent reflexes of a Mediterranean stone-word, which fits Beekes' Pre-Greek analysis of marmaros. Ernout-Meillet treat marmor as one of the neuter material-nouns (LAT.txt l.36618: 'marmor, -oris n.: marbre; et objet de marbre (statue, etc.)'). Given the doubt about the Greek word's own origin, the Greek-to-Latin arrow is likely but not certain, hence plausible.\",\n          \"derivation_fa\": \"لاتین marmor «مرمر» نیای واژه‌های رمانس و انگلیسی است؛ امّا اینکه وام‌گیری از یونانی باشد یا هم‌ریشهٔ مستقل، محل بحث است. پوکورنی (ص ۷۳۶) و والده–پوکورنی (جلد ۲، ص ۲۷۷) و کلاین می‌گویند از یونانی گرفته شده، ولی اتیمونلاین می‌نویسد «از یونانی یا هم‌ریشه با آن»، و اگر نظر بیکس دربارهٔ پیش‌یونانی بودنِ marmaros درست باشد، هر دو می‌توانند وام‌واژهٔ مدیترانه‌ای مستقل باشند. پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/marble\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:797\", \"status\": \"not_checked\", \"note\": \"AHD:797 is a main-dictionary page of the 1975/76 New College Edition (the entry 'marble'), not part of the Indo-European appendix; that edition is not open online and the local copy is the 1985 Watkins root-appendix, which has only 109 pages. The chain itself is verified from Klein, Pokorny, Walde-Pokorny and Etymonline below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"mer-5, p.736\", \"stance\": \"supports\", \"note\": \"'marmaros ... later (after marmairo) ‚white stone, marble‘ (out of it Latin marmor)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 277\", \"stance\": \"supports\", \"note\": \"'marmaros „Stein, Felsblock“ ... spaeter „weisser Stein, Marmor“ (daraus lat. marmor; s. WH LEWb.2 s. v. m. Lit.)'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt l.36618-36622\", \"stance\": \"partial\", \"note\": \"'marmor, -oris n.: marbre; et objet de marbre (statue, etc.) ... Derives: marmoreus; marmorosus; marmorarius; marmoratus, d'ou marmoro' - the Latin word and its family, without committing on the borrowing.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.982 s.v. marble\", \"stance\": \"supports\", \"note\": \"'fr. VL. marmorem, acc. of L. marmor (a neut. noun, taken in VL. for masc.), fr. Gk. marmaros'.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"French\",\n          \"words\": \"marbre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French marbre continues Vulgar Latin *marmorem (accusative of marmor, reanalysed as masculine) with the regular Gallo-Romance dissimilation of the first -m- to -b- before the second labial-nasal sequence, i.e. marmore > *marbre; the modern French form is unchanged marbre. Klein states the step exactly ('marble, n. - ME. marbre, later changed to marbel, marble, fr. OF. (= F.) marbre, fr. VL. marmorem'), and Etymonline dates the French word's own further dissimilation (of the second -r- to -l-) to the 14th century, which is why French kept marbre while English went to marble.\",\n          \"derivation_fa\": \"فرانسهٔ باستان marbre ادامهٔ لاتین عامیانهٔ *marmorem (حالت مفعولیِ marmor) است؛ میمِ نخست در مجاورت میمِ دوم به ب بدل شده (ناهمگونی/dissimilation): marmore > marbre. کلاین همین مرحله را می‌آورد و اتیمونلاین می‌افزاید که دگرگونی دوم (r به l) در فرانسه در سدهٔ ۱۴م رخ داد و انگلیسی آن را گرفت. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/marble\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:797\", \"status\": \"not_checked\", \"note\": \"See node #14: AHD:797 is a page of the 1975/76 main dictionary, not available online; the step Latin > Old French is confirmed from Klein p.982 and Etymonline.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.982 s.v. marble\", \"stance\": \"supports\", \"note\": \"'fr. OF. (= F.) marbre, fr. VL. marmorem, acc. of L. marmor'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt (Marble; Marmoset)\", \"stance\": \"supports\", \"note\": \"Skeat's Marmoset entry uses the same Latin-French chain ('from Low L. marmoretum, a thing made in marble ... - L. marmor, marble; see Marble') and notes the Parisian change of r to l.\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. marble (archived)\", \"stance\": \"supports\", \"note\": \"'from Old French marbre (which itself underwent dissimilation of 2nd -r- to -l- in 14c.; marbre persisted in English into early 15c.), from Latin marmor'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"marble\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English marbre (mid-12c.), borrowed from Old French, was altered to marbel/marble in the 14th century by dissimilation of the second -r- to -l-, a change Etymonline places in the same period in French itself; marbre survived in English into the early 15th century. Klein gives the same sequence ('ME. marbre, later changed to marbel, marble'). The English word thus stands at the end of the chain Greek marmaros (or a Mediterranean word shared with it) > Latin marmor > Old French marbre > English marble, and the derived senses (a sculptured marble, 14c.; the children's glass ball, 1690s) are internal English developments.\",\n          \"derivation_fa\": \"انگلیسی میانهٔ marbre (نیمهٔ سدهٔ ۱۲م) وام‌گرفته از فرانسهٔ باستان است که در سدهٔ ۱۴م با ناهمگونیِ r دوم به l به صورت marbel/marble درآمد؛ صورت marbre تا اوایل سدهٔ ۱۵م در انگلیسی ماند. پس زنجیرهٔ یونانی > لاتین > فرانسه > انگلیسی در نمودار درست است؛ معنای «تیلهٔ شیشه‌ای» از سدهٔ ۱۷م تحولی درون‌انگلیسی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/marble\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:797\", \"status\": \"not_checked\", \"note\": \"See node #14. The English step is confirmed from Klein p.982 and Etymonline s.v. marble.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.982 s.v. marble\", \"stance\": \"supports\", \"note\": \"'marble, n. - ME. marbre, later changed to marbel, marble, fr. OF. (= F.) marbre'.\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. marble (archived)\", \"stance\": \"supports\", \"note\": \"'mid-12c. ... dissimilation from marbra ... Marblestone is attested from c. 1200 ... Meaning ‚little ball of marble used in a children's game‘ is attested from 1690s'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt l.12065 (Marble)\", \"stance\": \"supports\", \"note\": \"Skeat's entry, though badly OCRed ('...ieces of marble. See (F.-L.)'), classifies the word '(F.-L.)', i.e. French from Latin, as here.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Germanic\",\n          \"words\": \"marôn; mur-thra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Germanic forms are Watkins' own reconstructions under this root and Nourai reproduces them faithfully. *maron- 'goblin, incubus' gives Old English mare/mere 'incubus', Old Norse mara, Old High German mara, German Mahr, and (with a Slavic branch: Polish zmora, Czech mura) points to a PIE *mora- 'incubus' understood as a derivative of *mer- 'to rub away, harm' - the nightmare being the being that 'presses, crushes' the sleeper. *mur-thra- (suffixed zero-grade *mr-tro-) gives Old English morthor 'murder' beside the shorter *mr-to-m in Old English morth, Old High German mord, Gothic maurthr; Latin mors, mortis is the same *mr-ti- formation. Pokorny p.735 lists 'mr-tro-m in Gothic maurthr, Old English mordor ‚murder‘' in the mer-4 'die' lemma.\",\n          \"derivation_fa\": \"هر دو صورت بازسازی‌های خودِ واتکینز اند: ژرمنیِ آغازین *marōn- «دیوِ خواب، بختک» که به انگلیسی کهن mare، نورسی mara و آلمانی Mahr رسیده، و *mur-θra- (از *mr-tro-) که انگلیسی کهن morðor «قتل» و گوتی maurþr از آن است؛ لاتین mors/mortis نیز همان ساختِ *mr-ti- است. پوکورنی در ص ۷۳۵ همین را می‌آورد. معنای «بختک» هم از مفهوم «فشردن و آزاردنِ خوابیده» می‌آید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nightmare\",\n            \"https://www.etymonline.com/word/murder\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mer-2 (AHD_watkins1985.txt l.753): 'I. 1. Germanic *maron-, goblin, in Old English mare, mere, goblin, incubus: NIGHTMARE' and 'II. 1. Zero-grade form *mr- in: a. suffixed form *mr-tro- in Germanic suffixed form *mur-thra- in Old English morthor, murder: MURDER'. Nourai's two Germanic forms and both glosses are taken from this entry, which is what his unpaginated 'AHD' citation refers to.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.984 s.v. mare 'incubus' and p.1016 s.v. murder\", \"stance\": \"supports\", \"note\": \"'mare, n., incubus. - ME., fr. OE., rel. to ON. and OHG. mara, MDu. mare, MHG. mar, G. Mahr, ‚incubus‘, and cogn. with the first element in OIr. Mor-rigain ... Bulg., Serb., Pol. mora, Czech mura, ‚incubus‘'; 'murder, n. - ME. mordre ... fr. OE. mordor, mordur, rel. to Goth. maurthr ... and cogn. with L. mors, gen. mortis, ‚death‘ ... See mortal.'\"},\n            {\"src\": \"POK\", \"where\": \"mer-4, p.735\", \"stance\": \"supports\", \"note\": \"'mr-to-m ‚death‘ in Old Indic mrta-, Old High German mord, Old English Old Icelandic mord ‚murder‘ (besides *mr-tro-m in Gothic maurthr, Old English mordoru ‚murder‘)'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt l.12041 (Murder)\", \"stance\": \"supports\", \"note\": \"'Murder, Murther. (E.) M.E. morthre. A.S. morthor. + Goth. ... We also find A.S. morth.'\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"nightmare; murder\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"nightmare is a Middle English compound (c.1300) of night + mare (n.) 'goblin that causes bad dreams, incubus', the latter from Old English mare < Proto-Germanic *maron- of node #17; the sense shifted in the mid-16th century from the incubus itself to the suffocating sensation it causes, and to 'any bad dream' by 1829. murder is Old English morthor (c.1300 murdre, earlier morther) 'secret killing', from Proto-Germanic *murthran, with the -d- spelling reinforced by Anglo-French murdre / Medieval Latin murdrum (itself from the Germanic word). Both are exactly the two English derivatives Watkins lists under mer-2, and Etymonline traces both to 'PIE root *mer- ‚to rub away, harm‘ (also ‚to die‘)'.\",\n          \"derivation_fa\": \"nightmare ترکیبی انگلیسی میانه (حدود ۱۳۰۰) از night و mare «بختک» است که خود از انگلیسی کهن mare و ژرمنی *marōn- می‌آید؛ در میانهٔ سدهٔ ۱۶م معنا از خودِ دیو به حالتِ خفگی و سپس (۱۸۲۹) به «خواب بد» منتقل شد. murder از انگلیسی کهن morðor «کشتن پنهانی» از ژرمنی *murþran است و دالِ آن زیر تأثیر فرانسهٔ انگلونورمن murdre تقویت شده. هر دو همان دو مشتقِ انگلیسی اند که واتکینز ذیل mer-2 می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nightmare\",\n            \"https://www.etymonline.com/word/murder\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 mer-2 ends each branch with the English word in capitals: '... Old English mare, mere, goblin, incubus: NIGHTMARE' and '... Old English morthor, murder: MURDER' - precisely this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. nightmare and s.v. murder (both archived)\", \"stance\": \"supports\", \"note\": \"nightmare: 'compounded from night + mare (n.3) ‚goblin that causes nightmares, incubus‘ ... All this is probably from PIE root *mer- ‚to rub away, harm‘'; murder: 'from Old English morthor ... from Proto-Germanic *murthran ... from suffixed form of PIE root *mer- ‚to rub away, harm‘'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1096 s.v. nightmare and p.1016 s.v. murder\", \"stance\": \"supports\", \"note\": \"'nightmare, n., 1) an incubus; 2) a frightening dream. - Compounded of night and mare, ‚incubus‘'; 'murder, tr. v. - ME. mortheren, murtheren, fr. OE. myrddrian ... See murder, n.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt l.12041\", \"stance\": \"supports\", \"note\": \"Skeat's Murder entry marks the word '(E.)', i.e. native English, from A.S. morthor - agreeing that it is inherited Germanic, not a Romance loan.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSON\npython3 -m json.tool data/verification/page-335.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 335"
}
```


### [2026-09-07T16:42:40.382Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 7, 'confirmed': 9, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 20, 'partial': 4, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 41, 'partial': 12, 'silent': 3, 'contradicts': 4} | by book: {'KLN': 7, 'WLD': 6, 'BRT': 5, 'CHEUNG': 5, 'MON': 4, 'POK': 4, 'SKT': 4, 'NYB': 3, 'KNT': 3, 'WEB': 3, 'SOD': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'HUB': 2, 'AHD': 2, 'SYN': 1, 'HRN': 1, 'IEC': 1, 'LAT': 1}
```


## [2026-09-07T16:42:54.928Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,unicodedata,re\nt=open('data/verification/page-335.json',encoding='utf-8').read()\nbad={}\nfor ch in set(t):\n    o=ord(ch)\n    if o<128: continue\n    name=unicodedata.name(ch,'?')\n    blk = 'FA' if 0x600<=o<=0x6FF or o in (0xFB8A,0x67E,0x686,0x698,0x6AF,0x6A9) else ('GRK' if 0x370<=o<=0x3FF else ('LAT-EXT' if o<0x250 else 'OTHER'))\n    if blk in ('OTHER',):\n        bad[ch]=name\nprint(bad)\nEOF"
}
```


### [2026-09-07T16:42:56.289Z] TOOL RESULT

```
{'ނ': 'THAANA LETTER NOONU', '–': 'EN DASH', '„': 'DOUBLE LOW-9 QUOTATION MARK', 'ʰ': 'MODIFIER LETTER SMALL H', '—': 'EM DASH', '“': 'LEFT DOUBLE QUOTATION MARK', '\u200c': 'ZERO WIDTH NON-JOINER', '‚': 'SINGLE LOW-9 QUOTATION MARK', 'ə': 'LATIN SMALL LETTER SCHWA', '‘': 'LEFT SINGLE QUOTATION MARK'}
```


## [2026-09-07T16:43:00.505Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -o \"maraނš-\" data/verification/page-335.json\npython3 - <<'EOF'\np='data/verification/page-335.json'\nt=open(p,encoding='utf-8').read()\nt=t.replace('maraނš-','marəxš-')\nopen(p,'w',encoding='utf-8').write(t)\nEOF\ngrep -c \"marəxš-\" data/verification/page-335.json; python3 -m json.tool data/verification/page-335.json >/dev/null && echo OK && python3 tools/verify_check.py 335 | tail -4"
}
```


### [2026-09-07T16:43:02.186Z] TOOL RESULT

```
maraނš-
1
OK
node verdicts: {'plausible': 7, 'confirmed': 9, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 20, 'partial': 4, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 41, 'partial': 12, 'silent': 3, 'contradicts': 4} | by book: {'KLN': 7, 'WLD': 6, 'BRT': 5, 'CHEUNG': 5, 'MON': 4, 'POK': 4, 'SKT': 4, 'NYB': 3, 'KNT': 3, 'WEB': 3, 'SOD': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'HUB': 2, 'AHD': 2, 'SYN': 1, 'HRN': 1, 'IEC': 1, 'LAT': 1}
```


## [2026-09-07T16:43:12.732Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\np='data/verification/page-335.json'\nd=json.load(open(p,encoding='utf-8'))\nn=0\nfor e in d['entries']:\n    for nd in e['nodes']:\n        for c in nd.get('consulted',[]):\n            w=c.get('where','')\n            if 'Wiktionary' in w and c['src']!='WIKT':\n                c['src']='WIKT'; n+=1\n            elif 'Etymonline' in w and c['src']!='ETYMONLINE':\n                c['src']='ETYMONLINE'; n+=1\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nprint('relabelled',n)\nEOF\npython3 tools/verify_check.py 335"
}
```


### [2026-09-07T16:43:14.008Z] TOOL RESULT

```
relabelled 7
nodes verified: 18/18
node verdicts: {'plausible': 7, 'confirmed': 9, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 20, 'partial': 4, 'not_checked': 6, 'not_found': 1}
books consulted: {'supports': 41, 'partial': 12, 'silent': 3, 'contradicts': 4} | by book: {'KLN': 7, 'WLD': 6, 'BRT': 5, 'CHEUNG': 5, 'WIKT': 4, 'POK': 4, 'SKT': 4, 'NYB': 3, 'KNT': 3, 'ETYMONLINE': 3, 'SOD': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'HUB': 2, 'AHD': 2, 'SYN': 1, 'MON': 1, 'HRN': 1, 'LAT': 1}
```


## [2026-09-07T16:43:37.746Z] AGENT

Done — `data/verification/page-335.json` written, valid JSON, `verify_check.py 335` reports 18/18 nodes and **0 PROBLEM lines**.

**Page 335 (book p. 305), root "Mer 2 / Mer-d, Mer-k / Mor-to / Smerd" — 1 entry, 18 nodes**
- Root: **confirmed** (POK 735 mer-4 "die" + mer-5 735-737 "rub"; POK 970 smerd-; Watkins mer-2 & smerd-; WP II 276 explicitly makes "die" an offshoot of "rub away").
- Node verdicts: **confirmed 9** (#2, #4, #7, #8, #13, #15, #16, #17, #18) · **plausible 7** (#1, #3, #6, #9, #10, #12, #14) · **disputed 2** (#5, #11).

**disputed**
- #5 Avestan `awiš-mar, wizmar` — neither is an attested Avestan compound; Horn's *patiš/aiwiš + mar-* was rejected by Hübschmann (HUB:41, cited in the chart's own note) in favour of *\*vizmurdan*, and Cheung (EDIV 265) settles on **\*pari-mar-** (Chor. prmy-, Shughni parmir-, Wakhi pərmor-). Avestan compounds mar- only with ava-/fra-.
- #11 Persian `mol` "wine" — modern view: loan from Sogdian mwδ (or Bactrian molo) < PIr *madu < PIE *médʰu, i.e. Nourai's own cross-referenced root "Medhu"; the chart's link rests only on Kent's 1950 parenthesis "cf. NPers mul" under the name Marduniya-.

**notable plausibles**: #1 "mardta : everyone" is a doublet of *marəta-* whose gloss was lifted from Gharib's Sogdian *mart mart* (SOD 5467, p.218) — the book prints "mardta", extraction faithful (`error_in: book`). #3 murdyānag/mašyānag are Gharib's/Nyberg's forms but denote **Eve**, not "mortal man". #9 Sogdian mrty is a cognate of, not a descendant of, OP martiya-. #10 *marduna- "vintner" is Kent's hedged back-formation. #12/#14 marmaros is Pre-Greek per Beekes; Etymonline has Latin marmor "from or cognate with" Greek.

**Reference checks**: 20 supports, 4 partial, 1 not_found, 6 not_checked. Confirmed page-exact: HRN 218-9, HRN 69, KNT 202/203 (verified against the running head "LEXICON 203"), SOD 218/219, BQT 1872 (گیومرث), 1982-6 (مرد/مردم/مردن/امرداد), 1996 (مرمر: «از یونانی marmaros»), 2017 (مشیا/مشیوی), 400 (پژمردن). Not confirmable: SOD:225 (that page is the myn-/myr run — **not_found**); KLN:1005 is one leaf off (p.1004-5 = mordant/(s)merd-, the Avestan forms are on 1006-7 s.v. mortal — partial); BQT:1934 supports mar- but for مار "snake"; AEF:378, ZMA:21, MON:4045, AHD:797 and AHD:1529 are not online (AHD root content verified in Watkins 1985 instead).

**Extraction errors for the owner: none** — I read the rendered page (copied to `data/verification/sources/refs/ocr/BOOK/335.png`) and the JSON matches the print everywhere, including "mardta", "awiš-mar, wizmar", the Onsorî verse and all Persian scripts. The only page feature absent from the JSON is an empty, unlabelled box drawn to the right of node #7, which carries no content.

12 web pages archived via `fetch_source.py`; BQT:1872 cached under `sources/refs/ocr/BQT/`.
