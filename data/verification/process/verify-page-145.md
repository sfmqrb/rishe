# Verification process log — verify-page-145


## [2026-09-05T20:08:37.001Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 145 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-145.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-145.json. Write /home/sfmqrb/git/rishe/data/verification/page-145.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 145` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:38.212Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:08:38.872Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:38.883Z] TOOL RESULT

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


## [2026-09-05T20:08:39.427Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-145.txt"
}
```


### [2026-09-05T20:08:39.446Z] TOOL RESULT

```
1	=== PDF page 145 (book page 115) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dwo : two  (refs POK:230;)
4	#1 (parent #0) [Avestan] refs=POK:230; KLN:440,1669; SOD:145 | dva, duva : two ; duva-dasa : twelve ☞Dekm ; dve-sate : two hundred ☞Dekm ; duvitya-kara : the other one ; biš : more
5	  #2 (parent #1) [Persian] refs=BQT:888,902,914; HRN:132; HUB:65 | do «دو ۱» : two ; devîst «دویست» : two hundred ; dîgar, degar «دیگر ، دگر» : other ; bîš 1 «بیش ۱» : more
6	#3 (parent #0) [Latin] refs=AHD; KLN:175 | bi, bis : two ; bis-coctus : cooked twice (biscuit) ☞Pekw ; duo : two ; duo-decem : two ten (dozen) ☞Dekm
7	  #4 (parent #3) [French] refs=KLN:175 | biscuit ; douzaine
8	    #5 (parent #4) [Persian] refs=MON:1572 |  | extra: بسکویت ، دوجین
9	    #6 (parent #4) [English] refs=KLN:175 | biscuit ; dozen
10	  #7 (parent #3) [English] refs=AHD | bicycle ; binary
11	#8 (parent #0) [Greek] refs=AHD | di, dis : two ; dia : through, across, apart ; di-ploos : twofold, pamphlet
12	  #9 (parent #8) [Greek] refs=AHD | dia-dein, dia-děma : a headband tied on two sides ☞Dě 1
13	    #10 (parent #9) [Persian] refs=MON:1603; BQT:921 | dayhîm «دیهیم» : crown
14	  #11 (parent #8) [Greek] refs=AHD | di-ploos : twofold, pamphlet, diploma
15	    #12 (parent #11) [French] refs=None | diplôme ; diplomate
16	      #13 (parent #12) [Persian] refs=MON:1590 |  | extra: دیپلم ، دیپلمات
17	      #14 (parent #12) [English] refs=AHD | diploma ; diplomat
18	  #15 (parent #8) [Greek] refs=KLN:440 | dia-bainein : going across (liquid in diabetic patients) ☞Gwa ; dia-luein, dialuses : to loosen (filter) apart, dialysis ☞Leu ; dia-phragna : completely enclosed ; dia-metros : (diameter line) that measures across ☞Me
19	    #16 (parent #15) [French] refs=None | 
20	      #17 (parent #16) [Persian] refs=MON | dîyâbet «دیابت» ; dîyâlîz «دیالیز» ; dîyâfrâgm «دیافراگم»
21	    #18 (parent #15) [Latin] refs=AHD | 
22	      #19 (parent #18) [English] refs=AHD | diabetes ; dialysis ; diameter
23	  #20 (parent #8) [Greek] refs=KLN:440; AHD:361 | dia-ballein : to throw across, slander ☞Gwel 1 ; diabolos : slanderer, devil
24	    #21 (parent #20) [Arabic] refs=BQT:83; FVQ:48 | eblis, iblis : devil
25	      #22 (parent #21) [Persian] refs=BQT:83 | eblîs «ابلیس»
26	    #23 (parent #20) [Latin] refs=AHD | 
27	      #24 (parent #23) [English] refs=AHD | devil
28	#25 (parent #0) [Germanic] refs=AHD | twai : two
29	  #26 (parent #25) [English] refs=None | two ; twelve ; twenty ; twice ; twin ; between
30	
```


## [2026-09-05T20:08:42.693Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-145.json",
 "description": "Show source JSON for page 145"
}
```


### [2026-09-05T20:08:42.778Z] TOOL RESULT

```
{
  "pdf_page": 145,
  "book_page": 115,
  "entries": [
    {
      "root": {
        "name": "Dwo",
        "lang": "Indo-European",
        "refs": "POK:230;",
        "gloss": "two"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:230; KLN:440,1669; SOD:145",
          "words": [
            {
              "translit": "dva, duva",
              "gloss": "two",
              "script": null
            },
            {
              "translit": "duva-dasa",
              "gloss": "twelve",
              "script": null,
              "see": [
                "Dekm"
              ]
            },
            {
              "translit": "dve-sate",
              "gloss": "two hundred",
              "script": null,
              "see": [
                "Dekm"
              ]
            },
            {
              "translit": "duvitya-kara",
              "gloss": "the other one",
              "script": null
            },
            {
              "translit": "biš",
              "gloss": "more",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:888,902,914; HRN:132; HUB:65",
          "words": [
            {
              "translit": "do",
              "gloss": "two",
              "script": "دو ۱"
            },
            {
              "translit": "devîst",
              "gloss": "two hundred",
              "script": "دویست"
            },
            {
              "translit": "dîgar, degar",
              "gloss": "other",
              "script": "دیگر ، دگر"
            },
            {
              "translit": "bîš 1",
              "gloss": "more",
              "script": "بیش ۱"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:175",
          "words": [
            {
              "translit": "bi, bis",
              "gloss": "two",
              "script": null
            },
            {
              "translit": "bis-coctus",
              "gloss": "cooked twice (biscuit)",
              "script": null,
              "see": [
                "Pekw"
              ]
            },
            {
              "translit": "duo",
              "gloss": "two",
              "script": null
            },
            {
              "translit": "duo-decem",
              "gloss": "two ten (dozen)",
              "script": null,
              "see": [
                "Dekm"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "KLN:175",
          "words": [
            {
              "translit": "biscuit",
              "gloss": null,
              "script": null
            },
            {
              "translit": "douzaine",
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
          "lang": "Persian",
          "refs": "MON:1572",
          "words": [],
          "script_extra": "بسکویت ، دوجین",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:175",
          "words": [
            {
              "translit": "biscuit",
              "gloss": null,
              "script": null
            },
            {
              "translit": "dozen",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "bicycle",
              "gloss": null,
              "script": null
            },
            {
              "translit": "binary",
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
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "di, dis",
              "gloss": "two",
              "script": null
            },
            {
              "translit": "dia",
              "gloss": "through, across, apart",
              "script": null
            },
            {
              "translit": "di-ploos",
              "gloss": "twofold, pamphlet",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "dia-dein, dia-děma",
              "gloss": "a headband tied on two sides",
              "script": null,
              "see": [
                "Dě 1"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:1603; BQT:921",
          "words": [
            {
              "translit": "dayhîm",
              "gloss": "crown",
              "script": "دیهیم"
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
              "translit": "di-ploos",
              "gloss": "twofold, pamphlet, diploma",
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
          "words": [
            {
              "translit": "diplôme",
              "gloss": null,
              "script": null
            },
            {
              "translit": "diplomate",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:1590",
          "words": [],
          "script_extra": "دیپلم ، دیپلمات",
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "diploma",
              "gloss": null,
              "script": null
            },
            {
              "translit": "diplomat",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 8,
          "lang": "Greek",
          "refs": "KLN:440",
          "words": [
            {
              "translit": "dia-bainein",
              "gloss": "going across (liquid in diabetic patients)",
              "script": null,
              "see": [
                "Gwa"
              ]
            },
            {
              "translit": "dia-luein, dialuses",
              "gloss": "to loosen (filter) apart, dialysis",
              "script": null,
              "see": [
                "Leu"
              ]
            },
            {
              "translit": "dia-phragna",
              "gloss": "completely enclosed",
              "script": null
            },
            {
              "translit": "dia-metros",
              "gloss": "(diameter line) that measures across",
              "script": null,
              "see": [
                "Me"
              ]
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {
              "translit": "dîyâbet",
              "gloss": null,
              "script": "دیابت"
            },
            {
              "translit": "dîyâlîz",
              "gloss": null,
              "script": "دیالیز"
            },
            {
              "translit": "dîyâfrâgm",
              "gloss": null,
              "script": "دیافراگم"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 15,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "diabetes",
              "gloss": null,
              "script": null
            },
            {
              "translit": "dialysis",
              "gloss": null,
              "script": null
            },
            {
              "translit": "diameter",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 8,
          "lang": "Greek",
          "refs": "KLN:440; AHD:361",
          "words": [
            {
              "translit": "dia-ballein",
              "gloss": "to throw across, slander",
              "script": null,
              "see": [
                "Gwel 1"
              ]
            },
            {
              "translit": "diabolos",
              "gloss": "slanderer, devil",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Arabic",
          "refs": "BQT:83; FVQ:48",
          "words": [
            {
              "translit": "eblis, iblis",
              "gloss": "devil",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "Persian",
          "refs": "BQT:83",
          "words": [
            {
              "translit": "eblîs",
              "gloss": null,
              "script": "ابلیس"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 23,
          "parent": 20,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 24,
          "parent": 23,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "devil",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 25,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "twai",
              "gloss": "two",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 26,
          "parent": 25,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "two",
              "gloss": null,
              "script": null
            },
            {
              "translit": "twelve",
              "gloss": null,
              "script": null
            },
            {
              "translit": "twenty",
              "gloss": null,
              "script": null
            },
            {
              "translit": "twice",
              "gloss": null,
              "script": null
            },
            {
              "translit": "twin",
              "gloss": null,
              "script": null
            },
            {
              "translit": "between",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:08:43.171Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:43.221Z] TOOL RESULT

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


## [2026-09-05T20:08:46.551Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && echo ---- && ls data/verification/ | head -50",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T20:08:46.600Z] TOOL RESULT

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
----
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
```


## [2026-09-05T20:08:47.963Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SOD','BQT','HRN','HUB','AHD','MON','FVQ']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Show ref metadata"
}
```


### [2026-09-05T20:08:49.764Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
```


## [2026-09-05T20:08:53.591Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-124.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False,indent=1))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Inspect a previous verification file"
}
```


### [2026-09-05T20:08:55.594Z] TOOL RESULT

```
{
 "pdf_page": 124,
 "book_page": 94,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05"
}
{
 "entry": 0,
 "root": "Dhě 2",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
 "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
 "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» 
{
 "id": 1,
 "lang": "Avestan",
 "words": "ma[n]dz-dha; ahura-mazdha",
 "verdict": "confirmed",
 "derivation": "The Avestan words are mazdā- / mazdah- n. 'memory, wisdom' and the divine name ahura- mazdā- 'Lord Wisdom' (Ahura Mazda). The second member really is this root: the compound is Proto-Indo-Iranian *mns-dʰeh₁- 'to set (something) in mind, commit to memory', i.e. *men- 'think' + *dʰeh₁- 'put'; Pokorny treats it under mendʰ- (Page(s): 730): 'Avestan mazda, mazdah- n. „Gedächtnis“, mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'. Nourai's odd transliteration 'ma[n]dz-dha / ahura-mazdha' is copied letter for letter from Klein s.v. Ormazd ('ma(n)dzdha-, ‘wise’, which is a compound formed from the I.-E. bases *men-dh- and *dhe- ‘to put, place’'); the actually attested Avestan spelling is mazdā-, so the -dh- here is Klein's etymologising respelling, not an Avestan form. The gloss 'done learning, wise' and the cross-reference to Men 1 are both correct.",
 "derivation_fa": "واژهٔ اوستایی mazdā- / mazdah- به معنی «خرد، یاد» و نام ایزدی ahura-mazdā- «سرورِ خرد» از ترکیب هندوایرانی آغازین *mns-dʰeh₁- «در یاد نهادن» ساخته شده است؛ یعنی ستاک *men- «اندیشیدن» به علاوهٔ همین ریشهٔ *dʰeh₁- «نهادن». پوکورنی این واژه را در صفحهٔ ۷۳۰ ذیل mendʰ- آورده (نه در صفحهٔ ۲۳۵ که نورایی ارجاع داده). املای غریبِ «ma[n]dz-dha» عیناً از کلاین (ذیل Ormazd) گرفته شده و صورت اوستایی واقعی mazdā- است. در مجموع ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Ahura_Mazda",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "POK:235",
   "status": "partial",
   "note": "POK_full.txt lines 22276-22510: the lemma at 'Page(s): 235-239' is 'dʰe-2, Meaning: to put, place, say' and it does NOT mention mazdā anywhere. Pokorny discusses mazdā s.v. mendh- at 'Page(s): 730' (line 59307: 'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'). The -dhā element is this root, so the claim holds, but the cited page is the wrong one."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "p.730 s.v. mendh- (POK_full.txt line 59307)",
   "stance": "supports",
   "note": "'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)' — the compound of *men-dh- + *dhē-."
  },
  {
   "src": "KLN",
   "where": "p.1096 s.v. Ormazd (KLN_1966.txt leaf 586)",
   "stance": "supports",
   "note": "'fr. Avestic Ahuramazda, lit. \"wise lord\", a compound of ahura- ... and ma(n)dzdha-, \"wise\", which is a compound formed from the I.-E. bases *men-dh- ... and *dhe-, \"to put, place\"' — Nourai's spelling and analysis come from here."
  },
  {
   "src": "BRT",
   "where": "Altiranisches Wörterbuch, passim (e.g. BRT.txt line 10715)",
   "stance": "supports",
   "note": "OCR of the headword column is unreadable, but the god's name is spelt mazdā / mazdå throughout the quoted Gāthā passages ('ahurō mazdā', 'ta
```


## [2026-09-05T20:09:30.794Z] TOOL CALL #8: Bash

```json
{
 "command": "ls site/pages/145.jpg 2>/dev/null; pdftoppm -f 145 -l 145 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg145 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 145 to PNG"
}
```


## [2026-09-05T20:09:32.137Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"du̯ō\\|dou̯-, du̯ō\\|Page(s): 228\\|Page(s): 230\" POK_full.txt | head -20",
 "description": "Find Pokorny dwo lemma"
}
```


### [2026-09-05T20:09:33.525Z] TOOL RESULT

```
site/pages/145.jpg
total 1812
drwx------ 2 sfmqrb sfmqrb   4096 Sep  5 16:09 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb 168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb 520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb 107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb  89133 Sep  5 16:09 pg145.png
```


### [2026-09-05T20:09:33.566Z] TOOL RESULT

```
23974:Page(s): 228-232
```


## [2026-09-05T20:09:36.761Z] TOOL CALL #10: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg145.png"
}
```


### [2026-09-05T20:09:37.286Z] TOOL RESULT

```

```


## [2026-09-05T20:09:37.283Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:09:49.978Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23940,24080p' POK_full.txt",
 "description": "Print Pokorny dwo lemma"
}
```


### [2026-09-05T20:09:50.030Z] TOOL RESULT

```
Old High German zwe(h)o. Old Saxon twe(h)o. Old English tweom. "doubt'. Old English 
be-twih, -tweoh^ between ', mid unctwTh^ between us both ' (compare above Gothic tweih- 
naf)\ 

from o^i/zs- from: Old High German zwisk. Old Saxon twisk^ twofold ', PI. "both' Dat. PI. 
Old High German {undar, en) zwisken. Modern High German zwischen; in addition Old 
English getwisam.. Old Saxon gitwiso. Middle High German zw/se//nc't\N\n'. 

With o'^/s- "twice' identical is o'^/s- "divided, asunder' in Gothic tm'sstandan'to divide' 
and den derivatives Old Norse /i/zs/ra "separate'. Middle Low German Old Frisian tm'st, 



Middle High German zty/s/ "discord (split)' and Middle English twist= Old Norse kvistr 
"twig, branch' (as also Bavarian zwist), further Old Norse kvTsli. " split branch or tools, arm 
of a river' (these with Indo Germanic ei)\ further Old Norse /i//s-i/a/' "twice', tvistr^ 
dichotomous, sad ' (= Old Indie dvistha-' ambiguous ', gr. *5iaT0(; in Siara^u) " doubt ', 
Indo Germanic *dui(s)-sto- : root sta-, at most du/s-to- \N\t\r\ formant -to-), Old English tw/'s/a 
" arm of a river ', twislian " bisect ', Old High German zwisila. Modern High German 
Zwieser divided object, twig, branch'. Middle High German zM//se/"double'; here very 
probably Aryan o'K/5-"hate' (see below *o'^e'/-"fear, dread'). 

Maybe alb. /77e 0^5/7 "apart, in two', dysh/"\.\No' 

6. Indo Germanic additional form cf/s-\n Latin d/s-, Old Saxon Old Frisian te-, ti-. Old 
English te-. Old High German zi-, ze- (new zir- through amalgamation from z/-an6 ir-) "dis- 
', Gothic dis- "apart' (probably borrowed from Latin, barely preceding from *tis- = Latin d/s- 
), alb. tsh- e.g. in tshk'ep ^ ur\p'\ck' , gr. 5ia (i.e. after pisra etc filled in *5i[a]a), e.g. 5ia-axi^w 
"through' : Latin discindo " to tear asunder, cut apart, cleave, divide, rend, tear ' ("*split in 
the middle '), as prefix also " through and through, thoroughly, all through ' = "very' (Aeolic 

References: WP. I 817 ff., WH. I 104 ff., 354 f., 381 ff., 860, 861, Feist 484 ff., Trautmann 
64, Schwyzer Gr. Gr. I 588 f., Wackernagel-Debrunner Old Indie Gr. Ill, 342 f. 
Page(s): 228-232 



Root / lemma: [do^i'T) : obh/; bh/ 

Meaning: around, from to, etc. 

Material: Old Indie abhi- prefix "from - to', ai6'/7/'preposition with Akk. "to', Gatha-Avestarf 

aibT,]ay. aiwi, avi, aoi. Old pers. abiyas prefix "to, around -', as preposition m. Akk. "to - 

toward ', with Lok. "about, in regard to' (in Aryan abhi\\es also partly */77/7/7/" before', see 

above S. 34); 

Latin Oit* "towards, to' appears only in the function, but not the sounds according to the 
partial successors from Indo Germanic obh/(see below epfj, 

Gothic bi. Old High German etc bi, bfirom - to (Gothic), with regard to, about' with Akk.; 
"an, by' with Dat. (Lok.), also with Instr., prefix "be-', s. also under arrici^i, above S. 34, 
which contains in final sound identical element; 



Old Church Slavic obb, obh as preverb ' around-, about-, to-' in obb-stojati ox obh-stojati 
"encircle', in compounds, as obbdou. 'treasure, tribute', in derivatives, as obbstb, russ.- 
Church Slavic obbCb "common' {*cb^i-tio-)\ intensified form obi- in russ -Church Slavic 
obichoditi' to walk around, perambulate '; the form o, Oi6» contains previous *op- 
(Lithuanian ap), see below epi. 

References: WP. I 124, Trautmann 1, Meillet Slave comm.2 155 f. 
Page(s): 287 

Root / lemma: eA^-2 

Meaning: fence, paling 

Material: Doubtful gr. oarpitjov "stall, hurdle ' ( 1x|h-//-o-)?? 

Old English eodorvn. " hedge, fence, dwelling; prince, lord' (ablaut. Middle Low German 
ader^ fence post '), Old High German etar. Modern High German Etterleuce, edge' (if in 
addition Bavarian ester, Swiss ester^ penstock '?), Old Icelandic y(?d^/'-/iy5d5/'-/'"edge, 
upper fence pole', perhaps Old English ed/'skm. " fenced pasture ', Bavarian /ss{e) 
"enclosed meadow' {*e6^-s/^); Old Bulgarian odrb^bed', odr/na ^ staW , russ. odr' 
scaffolding board ', Czech oo'/-" picket, pole', Serbo-Croatian odar, odr/na' encircling 
grapevine '. 

References: WP. I 121. 
Page(s): 290 

Root /lemma: ed'^- 

Meaning: sharp 

Note: 

From an older root /7e'^"'-e'/ derived: Root/ lemma: aR-, oR-\ "sharp; stone' and Root/ 

lemma: aiR-\ TR-\ "spear, pike', finally Root/ lemma: ed'^-: "sharp' [common lllyrian-Baltic 

gh- > d-. 

Material: Latin ebulus, -Ti. and -umu. " dwarf-elder (danewort, a fetid European species of 

elder, also dane's weed, dane's blood [said to grow on spots where battles were fought 

against the Danes]'; 

Note: common Latin g"- > b-, hence Latin ebulus < *heg"'-e/ where -el, -u/are diminutive 

formants. 

ablaut, (with /r-suffix) gall, and gallorom. oo'ocos "dwarf elder'; 

Old High German affub, attah. Old Saxon ao'^/r "dwarf elder' (borrowed from Celtic); 



Balto Slavic *edla- and *edli- f. 'fir' in 

Old Prussian addle {*edle), Lithuanian egle{ou\. of it dial, agle), Latvian eg/e6s. 
(secondary e-stem; -g- from -d-); 

Note: common lllyrian-Baltic gh- > c/- hence -g- from -o'-is wrong etymology. 

moreover probably Iterat. Lithuanian adyti^ prick ', Latvian ad?t^ knit ', compare 
Lithuanian adata' sewing-needle '; 

Church Slavic e\.c jela {* edia), russ. ye/6, Old Czech yeoyetc {*ed/f-). 

References: WH. I 14, 388 f., Trautmann 66. 
See also: from zum Folgenden {ed'^-2)7 
Page(s): 289-290 



Root / lemma: ed- {*hegh-) 

Meaning: to eat, *tooth 

Note: 

From an older root {*hegh-) derived Root/ lemma: ed- {* hegh-): "to eat, *tooth' and Root/ 

lemma: geirt!^-, gnp^-\ "to bite; tooth'
```


## [2026-09-05T20:09:53.844Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Meaning: two\" POK_full.txt | head; echo ---; sed -n '23700,23760p' POK_full.txt",
 "description": "Locate Pokorny two lemma start"
}
```


### [2026-09-05T20:09:53.913Z] TOOL RESULT

```
23722:Meaning: two 
---
5£im6(; m. "fear', 5£iv6(; "terrible', bz\kdq, "timorous, fearful; unlucky, lamentable ' 
(*5F£i£A6(;); 5i£p6q "to fear, dread' (*5Fi-£po(;); 

Latin d/rus' ill - omened, ominous, boding, portentous, fearful, awful, dread ' (from 
Servius to Aen. Ill 235 also as sabin. and Umbrian stated word, so that df- instead of b/- 
from *du/- as a dialectal sound development), with formants -ro- " before what one is afraid 
', as cla-rus^ audible, distinguishable '. 

5-extension in Old Indie dvestT hated, is hostile ', dvista- " detested ', dvesa-hm., 
dvesas- n. "hate', Avestan dvaes-, Jbaes-^be hostile to, mortify', participle Ibista-, dvaesah- 
, Waesah-' hostility'. Middle Persian i?e5 "affliction, mischief, probably to du/s-S. 232. 

Note: 

Reduplicated laryngeal in h2"ahre- > Avestan ae- 

References: WP. I 816 f., WH. I 353 f., Schwyzer Gr. Gr. I 7106, 769, 774. After 
Benveniste (briefl.) belongs the root as " be in doubt ' to consecutive dud(uj two'. 
Page(s): 227-228 

Root / lemma: dud(u) {*dhuei^ 

Meaning: two 

Grammatical information: m. (grammatical double form duudU), duaii. n., besides duel-, 

duo'h, dui- 

Note: compare the summary by Brugmann l|2 2, 6-82 passim. 

Material: 1. Old Indie m. dv'au, dva{ve6. also duvau, duva) = Avestan dvaxx\.. Old Indie f. 

n. c/i/e(ved. also duvi) = Avestan baei. and n. "two'; 

Note: 

Reduplicated laryngeal in h2"ahre- > Avestan ae- 



Instr. Dat. Abl. Old Indie d(u)vabhyam {has changed with a), Avestan dvaeibya {\N\\h old 
/■diphthong, as Lithuanian dv/em etc), Gen. Sg. Old Indie c{u)vayoh\ by compression of 
Old Indie d(u)va-: d^u)va-dasa^\T (== gr. 5oi)5£Ka); 

Armenian erku^i^No' (= Old Indie dva); 

gr. hom. 5u(F)u) (*5Fu) in 5u)-5£Ka), Gen. Dat. Ionian Attie 5uoTv, next to which 
uninflected hom. Attic Doric etc 5u(F)o (to form s. Schwyzer Gr. Gr. I 588 f.; to rudiment 
Indo Germanic *duds. Meillet BSL. 21, 273, due to Armenian erko-tasan\2, Latin duo- 
dem. Old Indie dva-ka- "the two together', but it could be directed after compositions with 
o-stems in the first part, as well as from Gothic Old Norse Old Saxon Old English Old 
Frisian wi-V we two ', Old Norse //, Old Saxon Old English git^you two'); 

alb. duxx\., duji. "two' {*duud, respectively *duuai)\ 

Latin o'i/c»(from *dud}, f. o'Z/ae (neologism), Umbrian (only with plur. inflection) durUom. 
m. "two' {*duds, *duur), desen-duf Akk. m. (12), du/r'two', tuva f\kk. n.; 

Old Irish dau, doHom. Akk. m. (= Old Indie dvau), before Subst. o'a (proclitic form), fem. 
dT{= Old Indie dve), neutr. da n-^two', acymr. bret. masc. dou, fem. cymr. dwy (etc); gall. 
VN Vo-cor-ii, l/c>-cc»/7//7(compare Tri-corii) with * u- besides du-\ compare Thurneysen Gr.
```


## [2026-09-05T20:10:00.941Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23760,23945p' POK_full.txt",
 "description": "Print rest of Pokorny duo lemma"
}
```


### [2026-09-05T20:10:01.003Z] TOOL RESULT

```
VN Vo-cor-ii, l/c>-cc»/7//7(compare Tri-corii) with * u- besides du-\ compare Thurneysen Gr. 
182; 

Gothic m. twai, f. twos, n. twa. Old Norse tueirm., tuaeri., tuaun.. Old English turn., twa 
f. (= Old Indie dve); Old High German zwenexu., zwa, zwoi., zweiu. etc (Old High 
German zweio^io two' Lok. Du. = Lithuanian dvfejau, dvfejaus); 

Lithuanian dum. (from *dvuo= Old Indie dva), dv/'t (= Old Indie dve); Latvian d/v/m. f. 
(from *duwii. n.). Old Prussian dwaim. f.; Old Church Slavic diDvam., dbvei. n.; 

Tocharian A m. wu, f. we, B m. f. ty/(neologism); compare above gall, vo-; Hittite ta-a-an 
(tan) " secondly, second ', ta-a-i-u-ga-as {tayugas) "two years old' (: Lithuanian dveigys 
"two years old animal'?). 

About the first part from sikogi, vTgintTe\.c (old dissimilation from *du7-, * due'hdRmtTll) s. 
uT-Rnjt-T twenty '. 

Note: 

The following dw- > b- is originally a Latin-italic. 



In compound Indo Germanic cfui- and from it under unclear condition developed c//-:0\d 
Indie dvf- (e.g. dv/-pad-' bipedal '), Avestan b/- (e.g. bi-mahya-^ lasting two months '), 
Armenian erki {erkeam^ biennial '), gr. 5i- (e.g. Sinouc;; da 5i(ppo(; ' curule chair, seat' was 
not 5i-, rather 5Fi-(ppo(;, if not perhaps dissimilatory loss of F is not against the following cp, 
also for other 5i- formation to consider from Indo Germanic *duh). Old Latin du'h, Latin b'h 
(e.g. duhdens, bidens, about forms as dienniums. WH. I under biennium, Sommer Hdb.^ 
223; (under the influence of common Celtic -ns-, -nt- > -nn-), Umbrian d'hfue^ cleft, parted, 
split ' probably sound pattern from duh). Old Norse tve- (also tvl-, see below). Old English 
twi-. Old High German zw'h (e.g. Old English twi-fete^ bipedal ', Old High German zwi- 
houbiV bicipital '), Lithuanian dv'h (e.g. dvi-gubas^ twofold ', Old Prussian dwi-gubbus). 

Ital. du- in Latin du-bius, -plus, -plex, -pondius, -centT, Umbrian tuplakfWk. Sg. n. " 
twofold ', du-pursus " on two feet ' is innovation after being perceived as du- stem from 
duo, also is to define du- in Umbrian duti^ again, a second time, once more, anew ', pali 
dutiyam " for the second time '; about Latvian du-celes " two-wheeled cart ' compare 
Trautmann 125, MiJhlenhach-Endzelin I 509, Endzelin Latvian Gr. 358. 

Zero grades duei-\v\ compounds is to be admitted for Celtic (e.g. Old Irish de-riad^ a 
span of horses, pair, two horses harnessed to an open car ', dfabur twofold ', cymr. dwy- 
flwydd'\>NO years old'; Old Irish dias^ duality of persons ' probably from * duejo-stho-) and 
for Germanic (e.g. Old Norse tuT-faldr^ twofold ' besides tuefaldr, Gothic tweifia-, probably 
n.. Old High German zwTfalu. besides gr. 5i-nA6(;, Latin duplus). 

duoi-\v\ Old English getwaefan, twseman^ separate, cut, clip' < *twaifjan, *twaimjan, 
perhaps also for the Aryan (Avestan baearazufra&ah- " two fingers wide ', dvaepa- n. 
'island'? or rather from duaji-, as probably Old Indie dvedha' twofold, (*divided) in two 
parts', compare o'lz/pa- "island' above S. 51); perhaps Phrygian GN Aoia(;, Gen. -avTOc; 
( *dyoi-nt) 'twin'. 

Note: 

Reduplicated laryngeal in h2"ahre- > Avestan ae- 

Slavic dvo, dvu-, dve- in compounds s. Berneker 247. 

2. ordinals: Old Indie dvitJya-, Avestan bitya-, dabitya-. Old pers. o^i/K/Z/ya- "second'; 
under duti^ again, a second time, once more, anew ' (probably replacement for *ditiirorr\ 
* du/t/om aiter du-, see above); Armenian erk/r, erkrord' second'; alb. i-dute; all new 
neologisms. 



3. Multiplikativadverb: c/uis'W\ce': Old Indie dvfh{ve6. also duvfh), Avestan bis, gr. b'\c„ 
Old Latin duis, Latin bis. Middle High German zty/A'twice' (but nir. fo-dT= Old Indie n. dve, 
Pedersen KG. I 301, II 127), Germanic myth. PN Tuisto^ hermaphrodite '; 

Maybe alb. dush"\n two'. 

through i/-forms extended Avestan bizval. Old Norse tysuar, tuisuar. Old High German 
zwiro, zwiror {zwiron, zwiront), with voiced ? z- reduction Old English twiwa, twiga, twia, 
tuwa, twie. Old Frisian twia, twera. Old Saxon twio; 

therefrom with formants -/ro-Old High German zwisic. Old Saxon twisic^ twofold ' (see 
below), probably also Armenian eridcs 'twice'; 

with Aforms Old English twisiian^ bisect ', /ty/s/a "confluence of two streams'. Modern 
High German Zwiesei^ bifurcation ' (perhaps restricted to *duis\v\ the meaning ' divided ', 
see below); 

with /-forms Old Indie dvita^ twofold, double' (therefrom dvaita-m^ duality '), ap. 
duvitaparnam' in two lines ', Gatha-Avestan o'a/Ma'again(?)'. 

4. multiplicative: gr. 5inA6(;, 5inA6o(;, Latin dupius, Umbrian dupia^ double, twice as 
large, twice as much ', Old Irish dTabul{ *duei-pio-, see also above Gothic tweifis), 
wherefore perhaps Avestan bifra- n. ' comparison, affinity ' (: root /7e/-'fold', compare with 
/-extension:) 

gr. 5inAaaioq {*pJt-io-), Ionian SiTrAnaioq ' waved with both hands ', Old High German 
zwifait6s. 

Gr. 5inAa^, Latin dupiex, Umbrian tupial<u. "duplex' (: root p/a'Ar- "flat, spread'); from Adv. 
z.B. duvi-^^a, o'l/e-dha (probably *dvaji-6'"a, that to be read in the oldest texts 3-syllable) " 
twofold, in two parts', wherewith the ending from Old Irish dede^ duality of things ' seems 
to be connected, as well as the from Old Low German twedi^\\a\f. Old English twaede^ 
two thirds ', Old High German zwitaran^ hybrid, mongrel, half breed ', Modern High 
German Z witter. 

Gr. 5ixc( " twofold, divided in two parts ' (after hom. 5ixn- 5ixou), next to which (through 
hybridization with *5i-9a to Old Indie dvidha) hom. 5ix6a " 5ixa ', therefrom Ionian 5i^6q " 
twofold ' (*5ix6j6(; or *5iKa6(;), and bxaaoq,, Attic bmoc, ds. (*5ix,i6(;, Schwyzer Gr. Gr. I 598, 
840); about Hittite dal<-sa-an^ half part ' s. Pedersen Hittite 141. 



Here also alb. dege' twig, branch, bough, brushwood ' {*duoi-ghS); 

Note: 

Alb. {*dhiuei-gha) dege^ twig ' : Old Indie f. n. dvS^two' : Lithuanian dve/gysm. ' biennial 
animal'; 

The origin of labialized Old laryngeals: 

common Albanian -hiue- > -e- ; Old Indie Lithuanian -hiue- > -ve-. 

Old High German zttv^'twig, branch' {*duei-gho). Old English /ty/g"twig, branch' {*dui- 
gho); Old Saxon tdg{d}. Middle Low German toch. Old High German zuog(o)^\.mQ, 
branch' are reshaped after cardinal forms with two-; 

Lithuanian dveigysrw. " biennial animal', serb. dv'izak^ biennial ram', old dviz^ biennial ' 
(: Hittite dayugas, see above). 

5. collective: Old Indie o'l/aya- "double' {dvaya-m' twofold creature, falsity ', nachved. 
"pair'), Dat. f. dvayyai= hom. ev 5oir|i; dvandvam "pair' (from ved. duva-duva^ every two '); 

gr. hom. 5oioj, 5oioi "double, two' (with preservation of -i- through influence of 
*5FoT[F]iv), £v 5oin " in doubt ' (Irish dTasixom * dueio-stho-?); 

Gothic Gen. PI. twaddje {corw^are with other ending Old Indie Gen. Dual dvayos, 
Lithuanian Gen. dviejij). Old Norse tueggia. Old High German zweiio. Old English m. 
twaegen, f. twa, n. /J "two' (see above Sievers-Brunner264), Nom. Akk. PI. Old High 
German zwei{*dueia), next to which from Indo Germanic *due/o-0\6 High German Middle 
High German zwl, g. zw/iesm.n. "twig, branch' (the /7-stem Old Norse /jya "doubt' 
presumably balanced from Nom. *tvljfa, Gen. tyju); 

Balto Slavic due/a- an6 duuaja- in Lithuanian dveji, f. dveJos'bNo' (the substantival n. 
Sg. in dveja //e/r "twice as much'); 

Old Church Slavic d{b)vq/7A6']. " twofold, two', d{b)vq/en. Subst. "two things' (therefrom 
derivatives as russ. o'i/oy/7dy"double', dvojn/" twins ', dvdjka^pa\r', dvojnfk^ zweidrahtiger 
paden ', dvoftb ' jj^^fl^aj^f jje teilen, zwei Faden zu einem izusammenj^ ^j^ ', etc, s. 
Berneker247). 

With -/70- (partly due to from duis): 



Armenian Ar/r//7 "double' from * (r)ki-rki-no-, Indo Germanic *dui-duis-no- {!) (L. Maries 
REtlE. 1,445); 

Latin bmf every two ' (distributive) and "two' (collective) from *duis-no- (= Germanic 
*twiz-na-)\ 

Germanic *twi-na-\v\ Old High German zwinal, zweneF born together, twin-born, twin- ', 
zwinilingru.. Middle High German zwinilTnu. "twin', *twai-na- in Old Saxon twene^two', Old 
High German zwene6s. (it has substituted with e instead of e/ after *zwe= Gothic twa/), 
Old High German zwein-zug. Old Saxon twen-tig. Old English twen-tig^lQ' (" Doppelzehn 

'); 

Maybe alb. 20, nje-zet^oue - ten', 40, oy-ze/"double - ten' 

Germanic *twiz-na-\v\ Old Norse tvennr, tvinnr^ twofold ', PI. tvenner^ zwei 
zusammengehorige ' (/K//7/75 "redouble'). Old High German zwirnen, -on^ zweifach 
zusammendrehen ', Middle High German zwirn. Middle Low German twern^ doppelt 
zusammengedrehter Faden ' probably = Old English twTn, holl. twijn^ linen thread, linen ' 
(Old English getwinne^ every two ', getwinnas^ twins ' is led back then to *twi-nja-). (under 
the influence of common Celtic -ns-, -nt- > -nn-). Besides due to *twTha-, Indo Germanic 
*duei-ko-, Gothic tweihnai^\.\No\ Old English Dat. tweonum, betweonum, engl. between^ 
between '; 

Lithuanian m. PI. dvynaT, russ. dvojni^ twins '. 

With -ko-. 

Old Indie dvika- " aus zweien bestehend, zweifach ' {dvaka- "in pairs, by pairs' 
connected after ekaka-); 

Old High German zwe(h)o. Old Saxon twe(h)o. Old English tweom. "doubt'. Old English 
be-twih, -tweoh^ between ', mid unctwTh^ between us both ' (compare above Gothic tweih- 
naf)\ 

from o^i/zs- from: Old High German zwisk. Old Saxon twisk^ twofold ', PI. "both' Dat. PI.
```


## [2026-09-05T20:10:16.257Z] TOOL CALL #14: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SOD','BQT','MON','FVQ','AHD','LEW','LAT','SKT','IEC','SYN','WLD']:\n    v=d.get(k,{})\n    print('==',k, '| offset:', v.get('page_offset'), '| hint:', str(v.get('lookup_hint'))[:400])\n    print('   local:', v.get('local_file'))\n\"",
 "description": "Print offsets and hints"
}
```


### [2026-09-05T20:10:18.018Z] TOOL RESULT

```
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
== SOD | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== MON | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
== FVQ | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
== LEW | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
== LAT | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
== SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
   local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
   local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
```


## [2026-09-05T20:10:22.110Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dwo-\\|^dwo\\b\\|^dwo\" AHD_watkins1985.txt | head -20",
 "description": "Find AHD dwo- root"
}
```


### [2026-09-05T20:10:22.171Z] TOOL RESULT

```
397:dwo-
413:dwo-. Two. I. Variant form duwo. 1. Germanic *twa, two,
```


## [2026-09-05T20:10:24.077Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==233||NR==232||NR==234 {print \"=== leaf \" NR-1 \" ===\"; print}' KLN_1966.txt | grep -n \"diabol\\|devil\\|dia-\\|διά\\|dis-\\|two\" | head -40",
 "description": "Check Klein leaf near p.440"
}
```


### [2026-09-05T20:10:25.851Z] TOOL RESULT

```
26:Derivatives:  delirious-ly,  adv.,  delirious-ness,  n. delirium,  n.,  a  violent  mental  excitement.  —  L. delirium,  ‘madness,  delirium’,  fr.  delirare,  ‘to turn  aside  from  the  furrow’,  whence  arose  the meanings  ‘to  deviate,  to  become  deranged, crazy  or  delirious’,  fr.  de-  and  lira,  ‘the  earth thrown  up  between  two  furrows,  furrow’.  L. lira  stands  for  *leisa  and  is  cogn.  with  Goth., OHG.  leisa  (in  wagenleisa),  ‘track  of  carriage wheels’,  MHG.  leise,  geleis,  G.  Geleise,  Gleis, ‘track’,  and  also  with  Goth,  lais,  ‘I  know’, laisjan,  OE.  liieran,  ‘to  teach’,  OE.  leornian,  ‘to learn’  (fr.  Teut.  base  *lais-,  ‘to  learn,  know, teach’,  orig.  ‘to  follow  or  find  the  track').  See learn  and  cp.  words  there  referred  to.  Cp.  also lirella.
70:demi-,  pref.  meaning  ‘half’.  —  F.  demi,  ‘half’,  fr. VL.  dimedius,  a  blend  of  L.  medius,  ‘middle’, and  dimidius,  ‘half’.  This  latter  is  a  back  forma¬ tion  fr.  dimidiatus,  ‘halved’,  pp.  of  dimididre, ‘to  halve’,  fr.  dis-,  di-,  and  medius,  ‘middle’. OProvenq.  demeg,  ‘half’,  also  derives  fr.  VL. dimedius.  See  di-,  ‘apart’,  and  cp.  medium.Cp. also  dimidiate,  demy  and  talmi  gold, demigod,  n.,  a  deified  hero.  —  Lit.  ‘half  god’,  a hybrid  coined  fr.  demi-  and  god. demijohn,  n.,  a  large  bottle  covered  with  wicker¬ work.  —  Alteration  of  F.  dame-jeanne,  for  Dame Jeanne,  ‘Lady  Jane’,  a  name  used  humorously to  denote  a  bottle;  see  dame  and  Jane.  The  al¬ teration  of  F.  dame  to  demi  in  English  demijohn is  due  to  a  confusion  with  F.  demi,  ‘half’  (see demi-).
71:demilune,  n.,  i)  a  half-moon,  crescent;  2)  a  cres¬ cent-shaped  outwork.  —  F.  demi-lune,  ‘half¬ moon’,  fr.  demi ,  ‘half’,  and  lime  (fr.  L.  liina), ‘moon’.  See  demi-  and  lune. demimonde,  n.,  a  class  of  women  of  doubtful social  standing.  —  F.  demi-monde,  lit.  ‘half¬ world’,  coined  by  Alexandre  Dumas  fils  in 1 855,  who  used  it  as  the  title  of  one  of  his  most successful  social  comedies.  For  the  etymology of  F.  demi  see  demi-.  F.  monde  derives  fr.  L. mundus,  ‘world’.  See  mundane, demirep,  n.,  a  woman  of  doubtful  reputation (slang).  —  Shortened  fr.  demi-reputation,  in which  demi  is  used  in  the  sense  given  to  it  in  F. demi-monde.  See  prec.  word  and  reputation, demise,  n.,  1)  transference  of  an  estate  by  death; hence  also  2)  death.  —  AF.,  prop.  fern.  pp.  of OF.  AF.  demetre  (whence  F.  demettre,  pp. demis,  fern,  demise),  ‘to  send  away,  dismiss’. See  demit.
```


## [2026-09-05T20:10:30.761Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '405,470p' AHD_watkins1985.txt",
 "description": "Print AHD dwo- entry"
}
```


### [2026-09-05T20:10:30.818Z] TOOL RESULT

```
drem-. To sleep. Suffixed zero-grade form “drm-yo- in Latin dormire, to sleep: DORMANT, DORMER, DORMITORY. [Pok. dré- 226.]
[dreug-. Dry. Germanic root. 1. Old English driigoth, drigath, dryness, drought: DROUGHT. 2. Suffixed form *drig-iz in Old English dryge, dry: DRY. 3. Suffixed variant form *draug-n- in Old English dréahnian, to strain, drain: DRAIN.]
[dub-. Also dup-. To drop, dip. Germanic imitative root. 1. Old English -doppa, a kind of bird (< “one that dips”): DIDAPPER. 2. Dutch doopen, to dip: DOPE. 3. Old English *dympel (diminutive with nasal infix), pool, dimple (> Middle English dimpel): DIMPLE. 4. Norwegian dumpa, to fall suddenly, akin to the Scandinavian source of Middle English dumpen, to dump: pump. [In Pok. dheu-b- 267.]]
[dud-. To shake, deceive. Germanic root. 1. Norwegian dudra, to quiver, akin to: a. Middle English daderen, to tremble: DODDER!; b. Middle English doder, vine (< “that which quivers in the wind”): DODDER2. 2. Middle English doten, to be foolish: DOTE. [In Pok. 4. dheu- 261.]]
[duellum. War. Latin noun (later form bellum) of un- known origin. BELLICOSE, BELLONA, DUEL; ANTEBEL- LUM, BELLIGERENT, POSTBELLUM, REBEL, (REVEL).]
dus-. Bad, evil; mis- (used as a prefix). Derivative of
deu-'. Greek dus-, bad: pys-. [Pok. dus- 227.]
dwei-. To fear. 1. Suffixed form *dwei-ro- in Latin dirus, fearful, horrible (originally a dialectal form): DIRE. 2. Suffixed form *dwey-eno- in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE. (This root originally meant “to be in doubt, be of two minds,” and is related to dwo-.) [Pok. dyei- 227.]
dwo-. Two. I. Variant form duwo. 1. Germanic *twa, two,
é
in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
@. Adverbial particle. Germanic *é in Old English a-, 2-, away, off: oaAKUM. [Pok. é 280.]
ed-. To eat; original meaning “‘to bite.” See dent-. 1. Ger- manic *etan in: a. Old English etan, to eat: EAT; b. Old High German ezzen, to feed on, eat: ETCH; c. Middle Dutch eten, to eat: orT; d. Germanic compound “fra- etan, to eat up (*fra-, completely; see per’), in Old English fretan, to devour: FRET). 2. Latin edere, to eat: EDACIOUS, EDIBLE, ESCAROLE, ESCULENT, ESURIENT; COMEDO, COMESTIBLE, OBESE. 3. Zero-grade form *d- in Latin compound prandium (< *pram-d-ium), “first meal,” lunch (*pram-, first; see per’): PRANDIAL. 4. Suf- fixed form *ed-un-d in Greek oduné, pain (< “gnawing care”); ANODYNE. [Pok. ed- 287.]
eg. I. Nominative form of the personal pronoun of the first person singular. For oblique forms see me-'. 1. Ger- manic *ek in Old English ic, I: I. 2. Extended form *egd in Latin ego, I: EGO, EGOIST, (EGOTISM). [Pok. e- 291.]
eg-. To lack. Suffixed (stative) form “*eg-é- in Latin egére, to lack, be in want: INDIGENT. [Pok. eg- 290.]
@g-. To speak. Suffixed zero-grade form “*ag-yo- in: a. Lat- in adagium, saying, proverb, “a speaking to” (ad-, to; see ad-): ADAGE; b. Latin prodigium, a portent, “a foretell- ing” (préd-, variant of pré-, before; see per'): PRODIGY. [Pok. @g- 290.]
eghero-. Lake. Possibly a suffixed variant form *agher-
16
el-2
ont- in Greek Akher@n, a river in Hades: ACHERON. [Pok. efhero- 291.]
eghs. Out. 1. Variant *eks in: a. Latin ex, ex-, out of, away from: EX!, Ex-; b. Greek ex, ek, out of, from: ECTO-, EXO-, EXOTERIC, EXOTIC; SYNECDOCHE. 2. Suffixed (com- parative) variant form *eks-tero- in Latin exterus, out- ward (feminine ablative extera, extra, on the outside): EXTERIOR, EXTERNAL, EXTRA-, STRANGE. 3. Suffixed (superlative) form in Latin extrémus, outermost (*-mo-, superlative suffix): EXTREME. 4. Suffixed form *eghs-ko- in Greek eskhatos, outermost, last: ESCHATOLOGY. [Pok. eghs 292.]
egni-. Also ogni-. Fire. 1. Latin ignis, fire: IGNEOUS, IGNITE; GELIGNITE, IGNITRON. 2. Sanskrit agnih, fire: Aanl. [Pok. egnis 293.]
@gvh-. To drink. Suffixed form *égvh-r-yo- in: a. Latin ébrius, drunk: INEBRIATE; b. Latin compound sdbrius (sé-, without; see s(w)e-).
ei-'. To go. 1. Full-grade form *ei- in: a. Latin ire, to go: ADIT, AMBIENT, (AMBITION), CIRCUIT, COITUS, COMITIA, EXIT!, EXIT?, INTROIT, ISSUE, OBITUARY, PERISH, PRAE- TOR, PRETERIT, SEDITION, SUBITO, SUDDEN, (TRANCE), TRANSIENT, (TRANSIT), (TRANSITIVE); b. Greek ienai, to go: ION; ANION, CATION, DYSPROSIUM. 2. Suffixed zero-grade form *i-t- in: a. further suffixed form *i-t-yo- in Latin initium, entrance, beginning (in-, in; see en): COMMENCE, INITIAL, (INITIATE); b. Latin comes (stem comit-), companion (< “one who goes with another”; com-, with; see kom): COUNT?; CONCOMITANT, CONSTA- BLE, (VISCOUNT). 3. Suffixed form ‘*i-ter in Latin iter, journey (> Late Latin itinerdre, to travel): (ERRANT), EYRE, ITINERANT, ITINERARY. 4. Extended form *yd- (< *yaa-) in suffixed forms *yd-no-, yd-nu- in: a. Latin Janus, archway, and Jdnus, god of doors and of the beginning of a year: JANITOR, JANUARY, JANUS; b. San- skrit ydnam, way (in Buddhism, “mode of knowledge,” “vehicle”): HiINAYANA, MAHAYANA. [Pok. 1. ei- 293.]
ei-2. Reddish, motley; yew. Suffixed form *ei-wo- in Germanic *iwaz, yew, in Old English iw, yew: yew. [Pok. 3. ei- 297.]
6ik-. To be master of, possess. 1.Germanic “aigan, to possess, in Old English dgan, to possess: OUGHT!, OWE. 2. Germanic participial form *aiganaz, possessed, owned, in Old English agen, one’s own: own. 3. Germanic prefixed form *fra-aihtiz, absolute possession, property (*fra-, intensive prefix; see per'), in Middle Low German and Middle Dutch vrecht, vracht, “earnings,” hire for a ship, freight: FRAUGHT, FREIGHT. [Pok. éik- 289.]
eis-1. In words denoting passion. 1. Suffixed form “eis-d- in Latin ira, anger: IRASCIBLE, IRATE, IRE. 2. Suffixed zero-grade form “is-(a)ro-, powerful, holy, in Greek hie- ros, “filled with the divine,” holy: HIERATIC, HIERO-; HIERARCH, (HIERARCHY), HIEROGLYPHIC, HIEROPHANT. 3. Germanic *isarno-, “holy metal” (possibly from Celtic), in Old English ise(r)n, iren, iron: IRON. 4. Suf- fixed o-grade form *ois-tro-, madness, in Greek oistros, gadfly, goad, anything causing madness: ESTRUS; (ES- TRONE). [Pok. 1. eis- 299.]
eis-2. Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]
ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.]
el-2. Red, brown (forming animal and tree names). 1. Ex-
el-?
tended form *elmo- in Germanic *elmo-, *almo- in Old English elm, elm: ELM. 2. Germanic extended form *aliza, alder, in Old English alor, alder: ALDER. 3. Possi- bly Old English ellen, ellzrn, the elder: ELDER?. 4. Ex- tended o-grade form “olki- in Germanic “alkiz, elk, in Old Norse elgr, elk, akin to Old English eolh, elk: ELK. 5. Perhaps Germanic extended form *alk- in Old Norse alka, auk: auK. 6. Extended form *elno- in Greek ellos, hellos, fawn: HELLEBORE. 7. Extended form *elani- in Lithuanian élnis, stag: ELAND. [Pok. 1. el- 302.]
el-3, To go. Suffixed extended form *ela-un-yo- in Greek elaunein, to drive (< “to cause to go”): ELASTIC, ELATER, ELATERITE; ELASMOBRANCH. [Pok. 6. el- 306.]
[elaia. Olive. Greek noun (earlier form elaiwd) of Medi- terranean origin. OIL, (-OLE), OLEAGINOUS, OLEASTER, OLEO-, OLIVE; (AIOLI), (ANELE), (PETROLEUM).]
elk-es-. Wound. Latin ulcus (stem ulcer-), a sore: ULCER. [Pok. elkos- 310.]
em-. To take, distribute. 1. Latin emere, to obtain, buy (> demere, to take away): ADEMPTION, EXAMPLE, (EXEM- PLARY), (EXEMPLIFY), EXEMPLUM, (EXEMPT), (IM- PROMPTU), PEREMPTORY, PREEMPTION, PREMIUM, PROMPT, (RANSOM), REDEEM, (REDEMPTION), (SAMPLE), VINTAGE. 2. Latin siimere (< *sus(e)m-), to take, obtain, buy (sus-, variant of sub-, up from under; see upo): SUMPTUARY, (SUMPTUOUS); ASSUME, CONSUME, PRE- SUME, RESUME, SUBSUME. [Pok. em- 310.]
en. In. 1. Germanic *in in: a. Old English in, in: IN; b. Germanic (comparative) *inn(e)ra in Old English innera, farther in, inner: INNER; C. Germanic *innan in Old English binnan, within (be, by; see ambhi + innan, in, within): BEN!. 2, Latin in, in-, in, into: EN-!, IN-?. 3. Greek en, en-, in: EN-2; ENKEPHALIN, PARENCHYMA, PARENTHESIS. 4. Suffixed form *en-t/e)ro- in: a. Latin intré, inward, within: INTRO-; INTRODUCE, INTROIT, INTROMIT, INTRORSE, INTROSPECT; b. Latin inird, inside, within: ENTER, INTRA-; INTRADOS, INTRINSIC. 5. Suf- fixed form *en-ter in Latin inter, inter-, between, among: ENTRAILS, INTER-, INTERIM, INTERIOR, INTERNAL. 6. Latin (superlative) intimus (*-mo-, superlative suffix), innermost: INTIMA, INTIMATE?. 7, Old Latin endo, Latin indu-, within, in industria, diligence, activity (*stru-, to construct; see ster-2): INDUSTRY. 8. Suffixed form *en- tos in: a. Latin intus, within, inside: DEDANS, INTESTINE, INTINE, INTUSSUSCEPTION; b. Greek entos, within: ENTO-. 9. Suffixed form *en-tero- in Greek enteron, entrails: ENTERIC, ENTERO-, ENTERON; DYSENTERY, MESENTERY. 10. Extended form *ens in: a. Greek eis, into: EPISODE; b. suffixed form *ens-6 in Greek esd, within: ESOTERIC. 11. Suffixed zero-grade form *n-dha possibly in Germanic *anda, *unda in Old English and, and: AND. [Pok. 1. en 311.]
en-. Year. Zero-grade form *n- in compound “per-n-yo-, of last year (see per’). [Pok. 2. en- 314.]
en-es-. Burden. Latin onus (stem oner-), burden: ONER- OUS, ONUS; EXONERATE. [Pok. enos- 321.]
engw-. Groin, internal organ. Suffixed zero-grade form *“ng»-en- in: a. Latin inguen, groin: INGUINAL; b. Greek adén, gland, gut: ADENO-; LYMPHADENITIS, SIALADENI- Tis. [Pok. engt- 319.]
epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
er-1, To move, set in motion. 1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron, second person singular and plural present of béon, to be:
ARE!, ART?. 2, Perhaps in Germanic suffixed form “er- n-os-ti- in Old English eornoste, zealous, serious: EAR- NEsT!. 3. Suffixed form *or-yo- in Latin oriri, to arise,
eu-!
appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]
er-2, Earth, ground. Extended form “*erf- in Germanic *erthé in: a. Old English eorthe, earth: EARTH; b. Middle Dutch aerde, eerde, earth (> Afrikaans aarde): AARD- VARK, AARDWOLF. [Pok. 4. er- 332.]
er-3. Base of designations of various domestic horned animals. Extended form *eri- in Latin ariés, ram: ARIES. [Pok. 2. er- 326.]
era-'. To row. 1. Variant form *ré- (< *rea-) in: a. Ger- manic *ré- in Old English réwan, to row: ROW?; b. suf- fixed form *ré-thra- in Germanic *réthra, rudder, in Old English réther, steering oar: RUDDER; Cc. suffixed form *ré-smo- in Latin rémus, oar: BIREME, REMEX, TRIREME. 2. Oldest variant form *sres- becoming *eré- in Greek triérés, trireme: TRIERARCH. [Pok. 1. er9- 338.]
ere-2. To separate. Variant *ré-, contracted from *reo-. 1. Suffixed variant form *rd-ro- in Latin rdrus, “having intervals between,” “full of empty spaces,” rare: RARE}, 2. Suffixed zero-grade form *ra-ti- in Latin ratis, raft (< “grating,” “latticework”): RATITE. 3. Suffixed length- ened-grade form *ré-ti- in Latin réte, r��tis, a net: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.]
ered-. High. Suffixed zero-grade form red-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.]
ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhus, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]
erkv-. To radiate, beam, praise. Sanskrit re, rk, “bright- ness,” praise, poem: Ric-VEDA. [Pok. erke- 340.]
ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
ers-2. To be wet. Variant form *ros- in Latin rés, dew: ROSEMARY. [Pok. 2. ere-s- 336.]
es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
esen-. Harvest, fall. O-grade form *osn- in Germanic *aznon, to do harvest work, serve, in Old English ear- nian, to serve, gain as wages: EARN}, [Pok. es-en- 343.]
esu-. Good. Extension of es-. Greek ews, good, combining form eu-, well: EU-. [Pok. esu-s 342.]
eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
6ti-. Eider duck. A probable root. Germanic *éthi in North Germanic *dthi in Old Norse Zdhr, eider: EIDER. [Pok. éti- 345.]
@tmen-. Breath. Sanskrit diman, breath, soul: ATMAN; MAHATMA. [Pok. ét-men- 345.]
eu-'. To dress. 1. Latin induere, to don (ind-, variant of
eu-?
in-, in, on; see en): ENDUE. 2. Latin exuere, to doff (ex-, off; see eghs): EXUVIAE. 3. Latin reduvia, fragment (red-, back, in reverse; see re-): REDUVIID. See extension wes-‘. [Pok. 2. eu- 346.]
eu-?. Lacking, empty. Extended forms *eua-, *wd-, *wa-. 1. Suffixed form *wo-no- in: a. Germanic *wanén in Old English wanian, to lessen, and wana, lack: WANE; b. North Germanic *wanatdn in Old Norse vanta, to lack: WANT. 2. Suffixed form *wd-no- in Latin vanus, empty: VAIN, VANITY, VAUNT; EVANESCE, VANISH. 3. Ex- tended form *wak- in Latin vacdre (variant vocdre), to be empty: VACANT, VACATE, VACATION, (VACUITY), VAC- UUM, VOID; (AVOID), (DEVOID), EVACUATE. 4. Extended and suffixed form *wds-to- in Latin vdstus, empty, waste (> vdstdre, to make desolate): WASTE; DEVASTATE. [Pok. 1. eu- 345.]
euedh-. Udder. 1. Suffixed zero-grade form *idh-r in Germanic *ddr- in Old English adder, udder: UDDER. 2. Suffixed o-grade form *oudh-r in Latin dber, “breast,” with derivative adjective aber, fertile: (EXUBERANT), EXUBERATE. [Pok. éudh- 347.]
```


## [2026-09-05T20:10:32.217Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^devil,\\|^diabolic\\|^diadem\\|^diploma\\|^diabetes\\|^dialysis\\|^diameter\\|^diaphragm\\|^biscuit\\|^dozen\\|^bis-\\|^di-,\\|^dia-,\" KLN_1966.txt | head -30",
 "description": "Locate Klein headwords"
}
```


### [2026-09-05T20:10:32.267Z] TOOL RESULT

```
5064:biscuit,  n.  —  F.  biscuit,  fr.  L.  bis  cactus,  ‘twice cooked’  (whence  also  It.  biscotto),  fr.  bis, ‘twice’  (see  prec.  word),  and  coctus,  pp.  of  co- quere,  ‘to  cook’.  See  cook,  n.,  and  cp.  bisque, bise,  n.,  a  dry  and  cold  north  wind.  —  F.,  fr. Frankish  *bisa,  which  is  rel.  to  OHG.  bisa,  G. Bise,  ‘bise’,  OHG.  bisdn,  ‘to  run  about’  (said of  cattle  attacked  by  gadflies),  OSwed.  bisa,  ‘to run’,  Dan.  bisse,  ‘to  run  in  agitation’ ;  not  re¬ lated  to  breeze.
11155:devil,  n.  —  ME.  devel,  fr.  OE.  deofol,  deoful,  fr. Eccles.  L.  diabolus,  fr.  Eccles.  Gk.  SixpoXo;, ‘devil’,  fr.  Gk.  SixfioXo;,  ‘slanderer’,  fr.  Stoc- [JxXXeiv,  ‘to  throw  across;  to  attack;  to  calum¬ niate,  slander’,  fr.  Six  (see  dia-)  and  (SxXXeiv, ‘to  throw’.  See  ballistic  and  cp.  diablerie,  dia¬ bolic,  Eblis.  Cp.  also  It.  diavolo.  Proven?.,  F., Catal.  diable,  Sp.  diablo.  Port,  diabo,  Goth. diabaulus,  which  all  derive  fr.  Eccles.  L.  dia¬ bolus.  OHG.  tiufal  (whence  MHG.  tiuvel,  G. Teufel,  prob.  also  MDu.  duvet,  Du.  duivel,  OS. diuVal,  ON.  djofull,  Dan.  djievel,  Swed.  djdvul) is  a  Goth,  loan  word.
11204:di-,  pref.  meaning  ‘apart,  asunder’.  —  L.,  form of  dis-  before  b,  d,  g,  I,  m,  n,  r,  v. di-,  pref.  meaning  ‘two,  double,  twice’,  used  esp.
11252:diameter,  n.  —  OF.  diametre  (F.  diametre),  fr. L.  diametros,  fr.  Gk.  SiapiExpog  (scil.  '(p<y.u.y.r), lit.  ‘a  diametral  line’.  See  dia-  and  meter,  ‘poet¬ ical  rhythm’.
11261:di-,  ‘two’,  and  Gk.  avt)7)p6g,  ‘flowery’,  fr.  5viffop, ‘flower’.  See  anther.
11268:diaphragmatic,  adj.,  pertaining  to  the  diaphragm.
11524:diplomacy,  n.  —  F.  diplomatic,  fr.  diplomate;  in¬ troduced  into  English  by  Edmund  Burke  (1729- 97).  See  diplomatic  and  -cy. diplomat,  diplomate.  —  F.  diplomate,  back  for¬ mation  fr.  diplomatique  in  agent  diplomatique, ‘diplomatic  agent’.  See  next  word.
12186:dozen,  n.  —  OF.  dozaine,  dosaine,  douzaine  (F. douzaine),  fr.  douze,  ‘twelve’,  fr.  L.  duodecim, ‘twelve’,  fr.  duo,  ‘two’,  and  decern,  ‘ten’.  See
```


## [2026-09-05T20:10:41.933Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py <<'EOF'\nimport sys\nf=sys.argv[1]; pats=sys.argv[2:]\ntxt=open(f,encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    for p in pats:\n        for m in re.finditer(p,l):\n            s=max(0,m.start()-100); e=min(len(l),m.start()+900)\n            print(f\"--- leaf {i} (KLNp~{i*2-24}..{i*2-23}) pat={p} ---\")\n            print(l[s:e].replace('\\n',' '))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py KLN_1966.txt 'diadem,' 'dia-,  pref' 'Eblis' 'diploma,  n' 'diabetes,' 'dialysis,' 'diaphragm,  n'",
 "description": "Extract Klein entries with leaf numbers"
}
```


### [2026-09-05T20:10:43.851Z] TOOL RESULT

```
--- leaf 87 (KLNp~150..151) pat=Eblis ---
e,  Belostoma,  bolide,  bolometer,  boule, ‘council’,  catabolism,  devil,  diabolic,  discobolus, Eblis,  ecbolic,  Elaphebolion,  emblem,  embolism, emboly,  hyperbola,  hyperbole,  metabolism,  pa¬ rable,  parabola,  parlance,  parley,  parliament, parlor,  parol,  parole,  periblem,  problem,  scy- balum,  symbol,  Tribolium,  Tribulus. ballistics,  n.,  the  study  of  projectiles.  —  See  prec. word  and  -ics. ballonet,  n.,  an  auxiliary  gas  or  air  bag  in  a  bal¬ loon  or  airship.  —  F.  ballonnet,  lit.  ‘a  small balloon’,  fr.  ballon.  See  next  word  and  -et. balloon,  n.  —  F.  ballon,  fr.  It.  pallone,  which  is formed  with  augment,  suff.  -one  fr.  palla,  ‘a ball’,  a  word  of  Teut.  origin;  see  ball,  ‘a  round body’,  and  -oon.  The  b  in  F.  ballon  (fr.  It.  pal¬ lone)  is  due  to  the  influence  of  F.  bade,  ‘ball’. Cp.  pallone. Derivatives:  balloon,  tr.  and  intr.  v.,  and  the hybrid  noun  balloon-ist,  n. ballot,  n.  —  F
--- leaf 91 (KLNp~158..159) pat=diabetes, ---
  anabas,  ana¬ basis,  -bates,  bathmism,  batophobia,  bema,  cata- basis,  diabase,  adiabatic,  diabetes,  ecbatic,  gyno- base,  hyperbaton,  metabasis,  Odobenus,  Ori- batidae,  parabasis,  presby-,  stereobate,  stylobate. As  a  term  of  chemistry  base  was  introduced  by the  French  chemist  Guillaume-Fran^ois  Rou- elle  (1703-70)  in  1 754- Derivatives  ;  base,  tr.  v.,  to  form  a  base  for; intr.  v.,  to  be  based  (on  or  upon  something); base-ment,  n. base,  adj.  —  ME.  bas ,  fr.  OF  (=  F.)  bas,  ‘low’, fr.  Late  L.  bassus,  ‘thick  fat,  stumpy’  (in  classical L.  occurring  only  as  a  cognomen);  of  un¬ certain  origin.  Cp.  abase,  bass  (music),  basset, basso,  bassoon,  debase. Derivatives:  base-ly,  adv.,  base-ness,  n. bash,  tr.  v.,  to  strike  violently.  —  Of  imitative origin.  Cp.  Swed.  basa,  Dan.  baske,  ‘to  strike’, bashaw,  n.  —  A  variant  of  pasha  (q.v.) bashful,  adj.  —  Aphetic  for  abash-ful.  See  abash an
--- leaf 240 (KLNp~456..457) pat=Eblis ---
  Six  (see  dia-)  and  (SxXXeiv, ‘to  throw’.  See  ballistic  and  cp.  diablerie,  dia¬ bolic,  Eblis.  Cp.  also  It.  diavolo.  Proven?.,  F., Catal.  diable,  Sp.  diablo.  Port,  diabo,  Goth. diabaulus,  which  all  derive  fr.  Eccles.  L.  dia¬ bolus.  OHG.  tiufal  (whence  MHG.  tiuvel,  G. Teufel,  prob.  also  MDu.  duvet,  Du.  duivel,  OS. diuVal,  ON.  djofull,  Dan.  djievel,  Swed.  djdvul) is  a  Goth,  loan  word. Derivatives:  devil-dom,  n.,  devil-ish,  adj.,  devil- ish-Iy,  adv.,  devil-ish-ness,  devil-ism,  n„  devil¬ ment,  n.,  devil-ry ,  n. devious 438 439 devious,  adj.,  roundabout,  circuitous.  —  L.  de- vius,  ‘off  the  high  road,  out  of  the  way,  devious’, fr.  de-  and  via ,  ‘way’.  See  via  and  cp.  deviate. For  E.  -ous,  as  equivalent  to  L.  -us,  see  -ous. Derivatives:  devious-ly,  adv.,  devious-ness ,  n. devise,  tr.  v.  —  OF.  deviser,  ‘to  divide,  distri¬ bute;  to  put  in  order;  to  chat’  (F.,  ‘to chat,  gos¬ s
--- leaf 241 (KLNp~458..459) pat=diabetes, ---
a-)  and  (fdai;,  ‘base’  (see  base,  n.);  so called  in  allusion  to  the  line  of  cleavage, diabetes,  n.,  a  disease  characterized  by  excessive discharge  of  urine  ( med .)  —  Medical  L.,  fr.  Gk. SiapvjT/;;,  lit.  ‘that  which  causes  a  going through’,  fr.  Sid  (see  dia-)  and  -pfjTr,:,  ‘that which  goes,  moves  or  flows’,  from  the  stem  of (8aiveiv,  ‘to  go’.  See  base,  n.  and  cp.  adiabatic. The  disease  was  called  Si'j.lprlTrlc  by  Aretaeus the  Cappadocian,  a  physician,  who  lived  in Alexandria  in  the  second  century  C.E.,  in  al¬ lusion  to  the  excessive  urination, diabetic,  adj.,  pertaining  to,  or  having,  diabetes. —  See  prec.  word  and  -ic. diablerie,  n.,  devilry.  —  F.,  fr.  diable,  ‘devil’,  fr. Eccles.  L.  diabolus,  fr.  Eccles.  Gk.  SidpoXo;, ‘devil’. See  devil.  For  the  etymology  of  F.  -erie  see  -ery. diabol-,  form  of  diabolo-  before  a  vowel, diabolic,  diabolical,  adj.,  pertaining  to  d
--- leaf 242 (KLNp~460..461) pat=diadem, ---
hia.  —  Formed  fr.  di-,  ‘two’,  Gk.  dSeXcpo;, ‘brother’,  and  suff.  -ous.  See  prec.  word, diadem,  n.,  crown;  fillet.  —  OF.  diademe  (F.  dia- deme),  fr.  L.  diadema,  fr.  Gk.  SidSrjpa,  ‘band, fillet,  royal  headband’,  fr.  SiaSciv,  ‘to  bind on  either  side’,  fr.  Sid  (see  dia-)  and  Seiv,  ‘to bind’,  fr.  I.-E.  base  *de(i)-,  *d1-,  ‘to  bind’, whence  also  OI.  dy-dti,  ‘binds’,  di-man,  'band, bond’.  Alb.  del ,  ‘sinew,  tendon’,  duai,  ‘sheaf’. See  desmo-  and  -ma  and  cp.  anadem.  Cp.  also Aditi,  Aditya. Derivatives:  diadem,  tr.  v.,  diadem-ed,  adj. diadoche,  n.,  succession.  —  Gk.  SiaSox?),  ‘succes¬ sion’,  rel.  to  81x80/0;,  ‘succeeding,  successor’, in  gradational  relationship  to  SiaSE/ea&ai,  ‘to succeed’,  lit.  ‘to  receive  one  from  another’,  fr. Sid  (see  dia-)  and  Sbyeabou,  ‘to  take,  accept, receive’,  fr.  I.-E.  base  *dek-,  *dok-,  ‘to  take,  re¬ ceive,  accept ;  acceptable,  becoming,  good’, whence
--- leaf 242 (KLNp~460..461) pat=diadem, ---
  duai,  ‘sheaf’. See  desmo-  and  -ma  and  cp.  anadem.  Cp.  also Aditi,  Aditya. Derivatives:  diadem,  tr.  v.,  diadem-ed,  adj. diadoche,  n.,  succession.  —  Gk.  SiaSox?),  ‘succes¬ sion’,  rel.  to  81x80/0;,  ‘succeeding,  successor’, in  gradational  relationship  to  SiaSE/ea&ai,  ‘to succeed’,  lit.  ‘to  receive  one  from  another’,  fr. Sid  (see  dia-)  and  Sbyeabou,  ‘to  take,  accept, receive’,  fr.  I.-E.  base  *dek-,  *dok-,  ‘to  take,  re¬ ceive,  accept ;  acceptable,  becoming,  good’, whence  also  L.  decere,  ‘to  be  seemly  or  fitting’. See  decent  and  cp.  words  there  referred  to. Diadochi,  n.pl.,  the  successors  of  Alexander  the Great;  hence  also  successors  (in  general).  — ModL.  Diadochi,  fr.  Gk.  SidSo/oi,  pi.  of  8id- 80x0;,  successor’.  See  prec.  word, diadochokinesia,  diadochokinesis,  n.,  the  normal v Si power  of  performing  alternating  movements (med.)  —  Medical  L.,  compounded  of  Gk. SidSo/o ;,  ‘succeedin
--- leaf 242 (KLNp~460..461) pat=dialysis, ---
ivatives:  dialogue ,  dialog,  intr.  and  tr.  v., dialogu-er,  n. dialyse,  v.  —  See  dialyze, dialysis,  n.,  separation  of  crystalloids  from  col¬ loids  (chem)  —  L.,  ‘separation’,  fr.  Gk.  8ia- Xuaig,  ‘separation,  dissolution’,  fr.  SiaXiieiv,  ‘to part  asunder,  break  off,  dissolve’,  fr.  8ia  (see dia-)  and  Xiietv,  ‘to  loose,  loosen’;  see  -lysis. The  word  dialysis  was  introduced  into  chemistry by  the  Scottish  chemist  Thomas  Graham  (1805- 69),  the  discoverer  of  this  process,  in  i86r. dialytic,  adj.,  pertaining  to  dialysis.  —  Gk.  81a- Xuxix6g,  ‘able  to  dissolve’,  fr.  SidXuxog,  ‘dis¬ solved’,  verbal  adj.  of  StaXiieiv,  ‘to  dissolve’. See  prec.  word  and  -ic. dialyze,  also  dialyse,  tr.  v.  (chem.)  —  Back  for¬ mation  fr.  dialysis. Derivative:  dialyz-er,  dialys-er,  n. diamagnetic,  adj.,  tending  to  take  a  position  at right  angles  to  the  direction  of  the  magnetic current.  —  Formed  fr.  dia-  an
--- leaf 243 (KLNp~462..463) pat=diaphragm,  n ---
Late L.  diaphoreticus,  fr.  Gk.  SiaupopTrjxtxSg,  fr.  81a- 9opetv.  See  prec.  word  and  -ic. diaphragm,  n.,  1)  muscular  partition  between  the thorax  and  abdomen;  2)  a  vibrating  membrane. —  Late  L.  diaphragma,  fr.  Gk.  8ia9paYp.ac,  ‘par¬ tition,  barrier;  muscle  which  divides  the  thorax from  the  abdomen’,  fr.  Six9payvuvai,  Six- 9pa<joeiv,  ‘to  divide  off,  barricade’,  fr.  81a  (see dia-)  and  9payvuvai,  9p<xaaetv,  ‘to  enclose, fence  round’,  which  is  cogn.  with  L.  farcire,  ‘to stuff’,  frequens,  gen.  -ends,  ‘thronged,  pressed together’.  See  farce,  ‘to  stuff,  cram’,  and  cp. frequent. Derivatives:  diaphragm,  tr.  v.,  diaphragm-al, adj. diaphragmatic,  adj.,  pertaining  to  the  diaphragm. i 'ax ( —  Formed  with  suff.  -ic  fr.  8ia9paY(jta,  gen. 8ta9piYffaTO?-  Sec  prec.  word. Derivative:  diaphragmatic-al-ly,  adv. diaphysis,  n.,  1)  the  shaft  of  a  long  bone  (hot.)', 2)  an  abnormal  prolongation  of  the  axi
--- leaf 248 (KLNp~472..473) pat=diploma,  n ---
7X67)015, there  can  be  no  Greek  adjective  of  the  form 8177X075x1x65  either.  See  diploic, diploma,  n.  —  L.  diploma,  fr.  Gk.  8(77X07  [xx, ‘anything  double,  folded  paper,  license’,  fr.  81- 77X06V,  ‘to  bend  double,  to  double’,  fr.  8177X605, 8177X065,  ‘double’.  See  diplo-  and  -oma  and  cp. double. Derivatives:  diploma,  tr.  v.,  diplomacy  (q.v.), diplomat  (q.v.),  diplomatic  (q.v.),  diplomat-ist, n.,  diplom-at-ize,  intr.  v. diplomacy,  n.  —  F.  diplomatic,  fr.  diplomate;  in¬ troduced  into  English  by  Edmund  Burke  (1729- 97).  See  diplomatic  and  -cy. diplomat,  diplomate.  —  F.  diplomate,  back  for¬ mation  fr.  diplomatique  in  agent  diplomatique, ‘diplomatic  agent’.  See  next  word. Derivative :  diplomate,  tr.  v. diplomatic,  adj.  —  F.  diplomatique,  fr.  ModL.  di¬ plomatics,  formed  with  suff.  -icus  fr.  diploma, fr.  Gk.  8(77X01  ;xa.  See  diploma  and  -atic. Derivatives:  diplomatic-al,  adj.,  diplomatic-a
--- leaf 270 (KLNp~516..517) pat=Eblis ---
 helped’,  Arab.  ‘ adhara , ‘he  excused,  exculpated ;  he  helped,  aided’.  Cp. Azariah,  Ezra. Eblis,  n.,  the  prince  of  the  fallen  angels  ( Arabian religion).  —  Arab.  Iblts,  aphetic  for  Gk.  810c- (3oXo<;,  ‘slanderer’,  in  Eccles.  Gk.  ‘devil’.  It  is very  probable  that  Gk.  StafloXo?  came  into Arabic  through  the  medium  of  Syriac  and  that the  first  syllable  of  the  Greek  word  was  mis¬ taken  for  the  Syriac  genitive  particle  di  and  sub¬ sequently  dropped.  See  devil, ebon,  n.,  ebony  (poetic).  —  ME.  eban,  fr.  L.  ebe¬ nus.  See  ebony. ebonist,  n.,  a  worker  or  dealer  in  ebony.  — Formed  fr.  ebony  with  suff.  -ist. ebonite,  n.,  vulcanite.  —  Formed  fr.  ebony  with subst.  suff.  -ite. ebonize,  tr.  v.,  to  stain  wood,  so  as  to  make  it resemble  ebony.  —  Formed  fr.  next  word  with suff.  -ize. ebony,  n.  —  OF.  ebaine  (F.  ebdne),  fr.  L.  ebenus (whence  also  OHG.,  MHG.  ebenus,  G.  Eben- hoiz),
--- leaf 826 (KLNp~1628..1629) pat=diadem, ---
ee  syn-)  and Seap.6;,  ‘band’,  which  is  cogn.  with  &ia-§7)pia, ‘a  headband,  fillet’.  See  diadem, syndesmosis,  n.,  articulation  of  parts  of  bones  by means  of  ligaments  (anat.)  —  Formed  with  suff. -osis  fr.  Gk.  auvScauoc,  ‘that  which  binds  to¬ gether’.  See  prec.  word. syndetic,  adj.,  connecting. — Formed  with  adj.  suff. -ic  fr.  Gk.  a'jvSexo;,  ‘bound  together’,  verbal adj.  of  auvSeiv,  ‘to  bind  together',  whence  also auvSeapioc,  ‘that  which  binds  together’.  See prec.  word  and  -etic. syndic,  n.,  the  accredited  agent  or  manager  of  a corporation,  esp.  of  a  university.  —  F.,  fr.  Late L.  syndics,  fr.  Gk.  auvStxo;,  ‘one  who  helps  in a  court  of  justice,  advocate’,  fr.  auv  (see  syn-) and  Slxrj,  ‘custom,  usage;  judgment,  justice’, which  is
```


## [2026-09-05T20:10:56.058Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\ndef show(i,n=1400):\n    print(f\"=== leaf {i} (pp.{2*i-42}-{2*i-41}) ===\")\n    print(leaves[i][:n].replace('\\n',' '))\nfor i in (108,109,241,855,856,857):\n    show(i)\nEOF",
 "description": "Print Klein leaves for pp.174-175, 440-441, 1668-1673"
}
```


### [2026-09-05T20:10:58.046Z] TOOL RESULT

```
=== leaf 108 (pp.174-175) ===
unning  to  aid’,  lit.  ‘running  on  hearing  a  cry’, fr.  (3ot),  ‘a  cry,  shout’,  and  -8p6[xoi;,  ‘running’, which  is  rel.  to.  Spoken;,  ‘a  running’.  For  the first  element  see  reboant  and  cp.  Boethusian,  for the  second  see  dromedary. Boehmeria,  n.,  a  genus  of  plants  of  the  nettle family  {hot)  —  ModL.,  named  after  G.R. Boehmer,  professor  at  Wittenberg  (1723-1803). For  the  ending  see  suff.  -ia. Boer,  n.  —  Du.  boer,  ‘peasant,  farmer’.  See  boor. Boethusian,  n.,  a  member  of  a  Jewish  sect  rel.  to the  Sadducees.  —  Heb.  Baylust,  ‘follower  of BaytBs  (=  Boethus)’,  fr.  Gk.  povjftos  (whence L.  Boethus),  name  of  a  priest,  whose  son  was made  high  priest  by  Herod  the  Great.  See  Jo¬ sephus,  Antiquitates,  19,  5,  §  3.  Ilorrr)6c  lit. means  ‘assisting,  helpful’.  It  is  a  derivative  of por;,  ‘a  cry,  shout’;  see  Boedromion. bog,  n.  —  Gael,  or  Ir.  bog,  ‘soft’,  whence  bogach, ‘bog’. Derivative :  bog,  tr.  and  intr.  v. bogey,  bogie,  n.,  ghost,  bugbear.  —  See  bogle and  cp.  bogy. boggle,  intr.  v.  and  n.  —  See  bogle, bogie,  n.  —  A.  var.  of  bogey, bogie,  n.,  a  truck.  —  Of  uncertain  origin, bogle,  boggle,  n.,  —  a  specter.  Scot,  bogle,  bogill, ‘goblin,  specter’,  rel.  to  bug,  ‘bugbear’,  bogey, bogy. bogus,  adj.,  sham.  —  Of  uncertain  origin
=== leaf 109 (pp.176-177) ===
  ME.  bond,  a var.  of  band.  See  band,  ‘a  tie’,  and  cp.  the  first element  in  bonspiel. Derivatives:  bond,  tr.  v.,  bond-ed,  adj. bond,  n.,  serf  (archaic).  —  ME.  bond,  ‘husband, householder’,  fr.  OE.  bonda,  ‘householder’,  fr. ON.  bondi,  for  biiandi,  ‘householder’,  lit.  ‘dwel¬ ler’,  fr.  bua,  ‘to  dwell,  build’.  See  be,  build,  and cp.  Boer,  boor,  booth,  bound,  adj.,  bower,  ‘ar¬ bor’,  byre,  and  the  second  element  in  husband. bondage,  n.  —  ML.  bondagium,  fr.  OE.  bonda, ‘householder’.  See  bond,  ‘serf,  and  -age. bondman,  n.  —  Compounded  of  bond,  ‘serf’,  and man. bone,  n.  —  ME.  ban,  bon,  fr.  OE.  ban,  ‘bone’,  rel. to  OS.,  OFris.  ben,  ON.  bein,  Dan.,  Swed.  ben, MDu.,  Du.  been ,  OHG.,  MHG.,  G.  bein,  ‘bone’. Cp.  the  first  element  in  bonfire  and  in  banstickle. Derivatives:  bone,  tr.  v.,  bon-ed,  bon-y,  adjs. bonfire,  n.  —  ME.  bonefire,  banefire,  orig.  ‘fire made  of  bones’;  see  bone  and  fire.  —  Cp.  Ri¬ chard  Broxton  Onians,  The  Origin  of  European Thought,  Cambridge,  1951,  p.268.  Note  1. Derivative:  bonfire,  tr.  and  intr.  v. bongo,  n.,  a  large  antelope.  —  Native  name, bonhomie,  n.,  good  nature.  —  F.  bonhomie ,  com¬ pounded  of  bon,  ‘good’,  and  homme,  ‘man’.  See bonus  and  homage. Boniface,  masc.  PN.  —  L.  Bonifacius,  Bonifa
=== leaf 241 (pp.440-441) ===
 deity. dewan,  n.,  minister  of  finance,  chief  officer  in  In¬ dia.  —  Arab,  and  Pers.  diwdn;  see  divan.  The orig.  sense  of  Pers.  diwdn  was  ‘register’,  whence developed  the  senses  ‘register  of  accounts;  de¬ partment  of  accounts:  ministry  of  finance; minister  of  finance’. devvanee,  dewany,  n.,  the  office  of  a  dewan.  — Hind,  diwani,  fr.  Pers.  diwani,  fr.  diwdn.  See prec.  word. Dewitt,  dewitt,  tr.  v.,  to  lynch.  —  After  the brothers  Cornells  and  Jan  De  Witt,  Dutch statesmen,  murdered  by  a  mob  in  1672. dexiocardia,  n.,  an  abnormal  condition  in  which the  heart  is  on  the  right  side  ( anal .)  —  Medical L.,  compounded  of  Gk.  SsEloc,  ‘on  the  right hand',  and  x.xp Six,  ‘heart’.  See  dexter  and cardiac. dexter,  adj.,  on  the  right-hand  side.  —  L.  dexter, ‘on  the  right  hand',  whence  arose  the  meanings ‘skillful,  favorable,  propitious,  fortunate’;  cogn. with  Gk.  Sc-  irepo;,  ‘on  the  right  hand’,  and  with OI.  daksinah,  daksinah,  ‘on  the  right  hand, southern,  skillful’,  Avestic  dashina-,  ‘on  the right  hand’,  Gk.  Se'io:,  ‘on  the  right  hand, fortunate,  clever’,  OSlav.  desnu,  Lith.  desinas, ‘on  the  right  hand’,  Lith.  desine,  ‘the  right hand',  Goth,  taihswa,  OHG.  zeso,  ‘on  the  right hand',  OIr.  dess,  on  the  right  hand,  southern’, W.  
=== leaf 855 (pp.1668-1669) ===
,  ‘deceiver’,  fr. OI.  sthagah,  of  s.m.,  fr.  sthagati,  ‘conceals’, which  is  cogn.  with  Gk.  axbfci v,  L.  tegere,  ‘to cover’.  See  thatch. Derivatives :  thuggee  (q.v.),  thugg-ess,  n. thuggee,  n.,  murder  as  carried  out  by  thugs.  — Hind,  thagi,  fr.  thag,  ‘a  deceiver’.  See  prec.  word. Thuja,  n.,  a  genus  of  plants,  the  arbor  vitae  (but.) —  ModL.,  fr.  Gk.  (H>(a,  name  of  an  African tree,  prop,  ‘a  tree  the  wood  of  which  was  burnt for  sacrificial  purposes’,  fr.  fhkiv,  ‘to  sacrifice’, prop,  ‘to  cause  to  smoke’.  See  thyme  and  cp. thyine. Thule,  n.,  classical  name  of  the  northernmost  part of  the  world.  — -  L.  Thule,  Thyle,  fr.  Gk. 0oiiXr],  0uXt).  Cp.  thulium, thulia,  n.,  thulium  oxide  (chem.)  —  ModL.,  coin¬ ed  by  the  Swedish  chemist  Per  Teodor  Cleve (1840-1905)  in  1879  fr.  Thule,  name  of  the  north¬ ernmost  land  in  the  world, thulite,  n.,  a  variety  of  zoisite  (mineral.)  —  Form¬ ed  fr.  Thule  with  subst.  suff.  -ite. thulium,  n.,  a  metallic  element  belonging  to  the rare  earths  ( chem .)  — -  ModL.,  coined  by  the French  chemist  Paul  fimile  Lecoq  de  Boisbau- dran  (1838-1912)  in  1886  from  prec.  word.  See J.  Newton  Friend,  Man  and  the  Chemical  Ele¬ ments,  London,  1951,  p.  182. thumb,  n.  —  ME.  thoume,  thoumbe,  thombe,  fr. OE
=== leaf 856 (pp.1670-1671) ===
and cp.  words  there  referred  to. Thysanoptera,  n.  pi.,  an  order  of  insects,  the  thrips (entomol.)  —  ModL.,  compounded  of  Gk.  &'i- aoevot;,  ‘tassel’,  and  7TTEpov,  ‘wing'.  See  prec. word  and  ptero-. Thysanura,  n.  pi.,  an  order  of  insects,  the  bristle- tail  (entomol.)  —  ModL.,  compounded  of  Gk. fhicravoi;,  ‘tassel’,  and  oupa,  ‘tail’.  See  thysano- and  uro-,  ‘tail-’. thyself,  pron.  —  ME.  thi  self,  fr.  earlier  the  self, fr.  OE.  pe  selfum,  dat.  of  pu  self,  ‘thou  thyself’; ME.  thi  self  was  influenced  by  ME.  hire  self, ‘herself’. tiara,  n.,  head  dress.  —  L.  tiara,  fr.  Gk.  vtapa, which  is  of  Oriental  origin. Tiarella,  n.,  a  genus  of  plants,  the  false  miterwort (bot.)  —  A  ModL.  hybrid  coined  fr.  Gk.  xiapa (see  prec.  word)  and  L.  dimin.  suff.  -ella;  so  call¬ ed  in  allusion  to  the  form  of  the  pistil.  The  cor¬ rect  form  would  be  Tiaryllium,  fr.  Gk.  flap  a and  the  Gk.  dimin.  suff.  -liXXtov. tibia,  n.  —  L.  tibia,  ‘shin  bone,  pipe',  which  is  of uncertain  origin.  Cp.  tige,  tigella. tibial,  adj.,  pertaining  to  the  tibia.  —  L.  tibialis, fr.  tibia.  See  prec.  word  and  adj.  suff.  -al. tibio-,  combining  form  meaning  ‘pertaining  to the  tibia  and’  —  Fr.  L.  tibia,  ‘shin  bone’.  See tibia. tic,  n.,  a  spasmodic  motion  of  cert
=== leaf 857 (pp.1672-1673) ===
ze.  —  Obsol.  F.  tiphanie, fr.  Late  L.  theophania,  ‘manifestation  of God’ ;  see  theophany.  The  word  tiffany  was  orig. used  as  a  synonym  of  epiphany.  Its  sense  devel¬ opment  into  ‘a  silk  gauze  fabric’  has  not  yet been  explained  in  a  satisfactory  manner, tiffin,  n.,  luncheon  (Anglo-Ind.)  —  Prob.  formed • —  with  change  of  suff.  —  fr.  tiffing,  verbal  n.  of tiff,  ‘to  drink’.  See  tiff,  ‘liquor’, tige,  n.,  the  shaft  of  a  column  (archil.)  ;  stem  of  a plant  (bot.)  — -  F.,  fr.  L.  tibia,  ‘shin  bone;  pipe'. See  tibia  and  cp.  next  word, tigeiia,  tigelle,  n.,  a  primitive  stem  (bot.)  —  Mod- L.,  fr.  F.  tigelle,  dimin.  of  tige,  ‘stalk,  stem’.  See prec.  word  and  -ella. Derivative:  tigell-ate,  adj. tiger,  n.  —  ME.  tigre,  fr.  OF.  (=  F.)  tigre,  fr.  L. tigris,  fr.  Gk.  riypt?,  prop,  ‘the  swift  animal’, a  word  of  Iranian  origin.  Cp.  Avestic  tiyrish, ‘arrow’,  tiyra-,  ‘pointed’.  These  words  are  deriv¬ atives  of  I.-E.  base  *(s)teig-,  ‘to  prick,  stick, pierce’.  Cp.  Gk.  Tlypt?  (whence  L.  Tigris),  ‘the Tigris  river’,  lit.  ‘the  swift  river’,  and  see  stick, v.,  and  words  there  referred  to. Derivatives:  tiger-ish,  adj.,  tiger-ish-ly,  adv., tiger-ish-ness,  n.,  tiger-ly,  adj.,  tigress  (q.v.), tigrine  (q.v.) tight,  adj.  —  ME.  thight,  tight
```


## [2026-09-05T20:11:12.663Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\npats=[r'two,\\s+adj',r'twelve,\\s+adj',r'twenty,\\s+adj',r'twice,\\s+adv',r'twin,\\s+adj',r'between,\\s+',r'biscuit,\\s+n',r'bis,\\s+adv',r'^bi-,\\s+pref',r'dia-,\\s+pref']\nfor i,l in enumerate(leaves):\n    for p in pats:\n        m=re.search(p,l,re.M)\n        if m:\n            print(f\"### leaf {i} pp.{2*i-42}-{2*i-41} :: {p}\")\n            print(l[max(0,m.start()-60):m.start()+700].replace('\\n',' '))\n            print()\nEOF",
 "description": "Find Klein two/twelve/bis/dia entries"
}
```


### [2026-09-05T20:11:14.915Z] TOOL RESULT

```
### leaf 99 pp.156-157 :: between,\s+
ecause  the  Gauls  extracted  tar from  it;  see  bitumen. between,  prep,  and  adv.  —  ME.  bitweonen,  bi- twenen,  bitwene.  fr.  OE.  betweonum,  fr.  be-,  ‘by’, and  tweonum,  dative  pi.  of  tweon,  ‘double, twain’,  which  is  rel.  to  Goth,  tweihnai,  ‘two each’,  fr.  twa,  ‘two’.  See  be-,  twain,  two,  and cp.  next  word. betwixt,  prep,  and  adv.  —  ME.  betwixe,  fr.  OE. betweox,  betweohs,  betwux,  betwyx,  fr.  pref.  be-, ‘by’,  and  a  form  of  twa,  ‘two’;  cp.  OHG.  zwisk, zwiski,  MHG.  zwisc,  ‘twofold’,  OS.  twisk,  ‘be¬ tween’,  Du.  tussen,  G.  zwischen,  of  s.m.  See between.  For  the  final  -t  cp.  against,  amongst, etc. Beulah,  fern.  PN.  —  Heb.  be'iildn,  ‘married  wom¬ an’,  fern.  pp.  of  bd‘a

### leaf 100 pp.158-159 :: ^bi-,\s+pref
 rel.  to  bhfunih, bhdman-,  ‘earth,  world’.  See  bhava. bi-,  pref.  meaning  ‘two’.  —  L.  bi-,  ‘twice,  double’, fr.  bis,  ‘twice’,  cogn.  with.  OI.  dvi-,  Gk.  81- (for  8fi-),  OE.  fwi’-,  ‘twice,  double’.  See  bis  and cp.  di-,  ‘two’,  dis-,  twi-,  two.  Cp.  also  binary, combine,  barouche,  breba. biangular,  adj.,  having  two  angles.  —  Formed  fr. bi-  and  angular. biannual,  adj.,  occurring  twice  a  year.  —  Formed fr.  bi-  and  annual. Derivative:  biannual-Iy,  adv. Bianca,  fern.  PN.  —  It.,  prop.  fern,  of  bianco ‘white’,  rel.  to  F.  blunc,  fern,  blanche,  ‘while’. See  blank  and  cp.  Blanch. bias,  n.,  1)  slant;  2)  prejudice.  —  F.  biais,  ‘slope, obliquity,  bias’,  prob.  fr.  OProveng.  bi

### leaf 103 pp.164-165 :: biscuit,\s+n
ement  in  bevue  and  the  second element  in  tSte-bcche. biscuit,  n.  —  F.  biscuit,  fr.  L.  bis  cactus,  ‘twice cooked’  (whence  also  It.  biscotto),  fr.  bis, ‘twice’  (see  prec.  word),  and  coctus,  pp.  of  co- quere,  ‘to  cook’.  See  cook,  n.,  and  cp.  bisque, bise,  n.,  a  dry  and  cold  north  wind.  —  F.,  fr. Frankish  *bisa,  which  is  rel.  to  OHG.  bisa,  G. Bise,  ‘bise’,  OHG.  bisdn,  ‘to  run  about’  (said of  cattle  attacked  by  gadflies),  OSwed.  bisa,  ‘to run’,  Dan.  bisse,  ‘to  run  in  agitation’ ;  not  re¬ lated  to  breeze. bisect,  tr.  v.,  to  cut  in  two.  —  Formed  fr.  bi-  and L.  secare,  pp.  sect  us,  ‘to  cut’.  See  section. Derivatives:  bisect-ion,  n.,  bisect-or,  n. bisexual, 

### leaf 103 pp.164-165 :: bis,\s+adv
  bear,  carry’.  See  bear,  ‘to  carry’,  and cp.  berth. bis,  adv.,  twice.  —  L.  bis,  fr.  OL.  dvis,  cogn.  with OI.  dvih,  Avestic  bish,  Gk.  8t?,  MHG.  zwis, ‘twice’,  Goth.  I  vis-,  ‘in  two,  asunder’,  ON.  tvis- tra,  ‘to  divide’.  See  bi-  and  cp.  two,  twi-,  twist. Cp.  also  the  first  element  in  bevue  and  the  second element  in  tSte-bcche. biscuit,  n.  —  F.  biscuit,  fr.  L.  bis  cactus,  ‘twice cooked’  (whence  also  It.  biscotto),  fr.  bis, ‘twice’  (see  prec.  word),  and  coctus,  pp.  of  co- quere,  ‘to  cook’.  See  cook,  n.,  and  cp.  bisque, bise,  n.,  a  dry  and  cold  north  wind.  —  F.,  fr. Frankish  *bisa,  which  is  rel.  to  OHG.  bisa,  G. Bise,  ‘bise’,  OHG.  bisdn,  ‘to  run  abo

### leaf 286 pp.530-531 :: between,\s+
  of  interaneus, ‘that  which  is  within’,  fr.  inter,  ‘between, among’.  See  inter,  prep.,  and  cp.  enteric, entero-. entrain,  tr.  and  intr.  v.,  to  put  or  go  aboard  a train.  —  Formed  fr.  ist  en-  and  the  noun  train, entrain,  tr.  v.,  to  draw  on  or  along.  —  F.  en- trainer,  fr.  ist  en-  and  trainer,  ‘to  draw’.  See train,  v. entrammel,  tr.  v.,  to  put  into  trammels.  — Formed  fr.  ist  en-  and  trammel, entrance,  n.,  the  act  of  entering.  —  OF.,  fr.  en¬ tree.  See  enter  and  -ance. entrance,  tr.  v.,  to  put  into  a  trance.  —  Formed fr.  ist  en-  and  trance. Derivatives:  entrance-mem,  n.,  entranc-ing,  adj., entranc-ing-ly,  adv. entrant,  adj.,  entering;  n.,  one  who  enters.  —

### leaf 287 pp.532-533 :: between,\s+
nter-.  —  Fr.  F.  entre, ‘between,  among’,  fr.  L.  inter,  of  s.m.  See  ist enter-. entreat,  tr.  and  intr.  v.  —  ME.  entreten,  fr.  OF. entraiter,  ‘to  treat’,  fr.  ist  en-  and  trailer,  ‘to treat’.  See  treat. Derivatives :  entreat- ing,  adj.,  entreat-ing-ly,  adv. entreaty,  n.  —  Formed  fr.  entreat  on  analogy  of treaty. entree,  entree,  n.,  1)  entrance,  right  to  enter; 2)  a  course  of  meal.  —  F.  entree.  See  entry, entremets,  n.,  side  dish,  extra  dish.  —  F.,  fr.  entre mets,  ‘between  dishes’.  See  ist  entre-  and  mess, entrench,  intrench,  tr.  v.  —  Lit.  ‘to  surround with  entrenchments’;  formed  fr.  ist  en-  (resp. in-,  ‘in’)  and  trench. Derivatives:

### leaf 432 pp.822-823 :: between,\s+
al-ity,  n.,  intent ional-ly, adv. inter,  prep.,  among,  between,  occurring  in  Latin phrases  occasionally  used  in  English,  as  inter alia,  ‘among  other  things’.  —  L.  inter,  fr.  I.-E. *enter  or  'nter,  ‘between,  among’,  whence  also Oscan  anter,  Umbr.  anter,  ander-,  OI.  antar, Avestic  antar*,  OPers.  antar,  ‘among,  between’, OI.  dntarah,  ‘inner,  interior’,  antrdm,  ‘intestine’, Toch.  B  etsar,  ‘within’.  Arm.  lnder-k ‘  (pi.),  ‘in¬ testines’,  Gk.  evTcpa  (pi.),  ‘intestines’.  Alb. nder,  ‘between,  in’,  OSlav.  qtru,  ‘between’, qtroba,  ‘entrails’,  jgtro,  ‘liver’,  OIr.  eter,  etar, etir,  OW.  it  hr ,  Co.  ynter,  Bret,  entre,  ‘among, between’,  Goth,  undar,  OHG.  untar,  OE.  under, in  the  sen

### leaf 433 pp.824-825 :: between,\s+
interest’,  prop, subst.  use  of  L.  interesse,  ‘to  be  between,  lie between;  to  take  part  in;  to  import,  be  of  in¬ terest’,  fr.  inter-  and  esse,  ‘to  be’ ;  see  esse.  The alteration  of  earlier  E.  interess  to  interest  is prob.  due  to  the  influence  of  OF.  interest (whence  F.  imeret),  ‘interest’,  a  word  derived  fr. L.  interest,  ‘it  imports,  it  is  of  interest’,  which was,  however,  taken  for  a  noun  in  the  sense of  ‘that  which  imports  or  is  of  interest’.  Cp.  G. Interesse,  ‘interest’,  which  also  derives  fr.  ML. interesse  (see  above). interest,  tr.  v.  —  Fr.  interess'd,  pp.  of  earlier English  interess,  ‘interest’.  See  interest,  n. Derivatives:  interest-ed,  adj.,  intere

### leaf 434 pp.826-827 :: between,\s+
ition,  n.  —  L.  interpositio,  gen.  -dnis,  ‘a putting  between,  insertion’,  fr.  interpositus, pp.  of  interponere,  ‘to  put  between,  insert’, fr.  inter-  and  ponere,  ‘to  put,  place’.  See position. interpret,  tr.  and  intr.  v.  —  OF.  interpreter,  fr. L.  interpretari,  ‘to  explain,  expound’,  fr.  inter- pres,  gen.  -pretis,  ‘an  agent  between  two  parties, explainer,  expounder’,  lit.  ‘mediator’.  For  the first  element  see  inter-.  The  second  is  rel.  to  L. pretium,  ‘price,  value’;  see  price  and  cp.  words there  referred  to. interpretable,  adj.  —  Late  L.  interpretabilis,  fr. L.  interpretari.  See  prec.  word  and  -able. Derivatives:  interpretabil-ity,  n.,  interpretable- ness,  n.,  interpret

### leaf 435 pp.828-829 :: between,\s+
the  inside,  inwardly’,  fr.  inter, ‘in  the  midst  of,  between,  among’,  and  secus, ‘beside,  by,  along’.  For  the  first  element  see inter,  prep.  L.  secus  orig.  meant  ‘following’ ; and  is  rel.  to  sequi,  ‘to  follow’.  See  sequel  and cp.  second.  Cp.  also  extrinsic. Derivatives:  intrinsic-al,  adj.,  intrinsic-al-Iy, adv.,  intrinsic-al-ness,  n. intro-,  pref.  —  L.  intro,  ‘into  the  inside,  within’, for  *intero-,  fr.  *interus,  ‘on  the  inside,  inward’. See  interior. introduce,  tr.  v.  —  L.  intrdducere,  ‘to  lead  in, bring  in;  to  introduce;  to  bring  forward;  to institute,  originate’,  fr.  intro-  and  diicere,  ‘to lead,  conduct,  guide’.  See  duke  and  cp.  words there  referred  to. introdu

### leaf 520 pp.998-999 :: between,\s+
. p.ex-,  (J.E&-,  fr.  uexa,  ‘in  the  midst  of,  among, between,  with’,  cogn.  with  Goth,  mip,  OHG. mit,miti,  MHG.  mit.  mite,  G.  m/7.  OFris.  mith, mithi,  OS.  mid,  midi,  ON.  med,  OE.  mid,  mid, ‘with,  together  with,  among’,  and  prob.  also metabasis metatnetic with  Gk.  [tiaoc,,  L.  medius ,  ‘middle’,  OE.  midd, etc.,  ‘mid’.  See  meso-,  media,  ‘voiced  stop  con¬ sonant’,  and  cp.  mid,  middle  and  the  first  ele¬ ment  in  midwife. metabasis,  n.,  transition  (esp.  in  rhet.,  from  one subject  to  another) ;  change  (med.)  —  ModL.,  fr. Gk.  psTafSocais,  ‘a  passing  over,  changing',  fr. p.ETa£laivEiv,  ‘to  pass  over’,  which  is  formed  fr. (jletk-  (seemeta-)  and  pcdvsiv,  ‘to  go’.  See  base,

### leaf 525 pp.1008-1009 :: between,\s+
h,  mip,  ON.  med,  ‘with’,  and  cogn.  with Gk.  pcxi,  ‘between,  among,  with,  after’;  see meta-.  For  the  second  element  see  wife. Derivatives:  midwife,  tr.  v.,  midwifery  (q.v.) midwifery,  n.  —  A  hybrid  formed  fr.  midwife and  -ery,  a  suff.  of  Romance  origin, mien,  n.,  manner,  demeanor,  appearance.  F. mine,  ‘look,  appearance,  mien’,  borrowed  fr. Bret,  min,  ‘beak,  muzzle,  nose’;  prob.  influ¬ enced  in  meaning  by  the  verb  de-mean. miff,  n.,  a  trifling  quarrel;  tr.  v.,  to  put  or  be  out of  humor.  —  Orig.  exclamation  of  disgust.  Cp. G.  muffen,  ‘to  sulk’. might,  v.,  past  tense  of  may.  —  ME.  mighte,  fr. OE.  meahte,  mihte ,  past  tense  of  magan,  ‘to  be able’.  See  may,  

### leaf 883 pp.1724-1725 :: twelve,\s+adj
elifto,  zwelefto,  MHG.  zwelfte,  G.  zwolfte, ‘twelfth’. twelve,  adj.  and  n.  —  ME.  twelf,  twelve,  fr.  OE. twelj,  rel.  to  OS.  twelif,  ON.  tolf,  Swed.  tolf, Dan.,  Norw.  tolv,  OFris.  twelef,  twelif,  MDu. twalef,  Du.  twaalf,  OHG.  zwelif,  MHG.  zwelif, zwelef,  zwelf,  G.  zwolf,  Goth,  twalif.  These words  are  compounds  meaning  lit.  ‘two  left  after (ten)’,  ‘two  added  (to  ten)’.  For  the  first  element see  two.  The  second  element  is  cogn.  with  L.  lin- quere,  Gk.  Aeitteiv,  ‘to  leave  behind’ ;  see  loan, relinquish  and  ep.  eleven.  Outside  Teutonic  cp. Lith.  dvy-lika,  ‘twelve’,  which  is  the  exact  equiv¬ alent  of  the  above  Teut.  words,  not  only  in meaning  but  also  in  derivati

### leaf 883 pp.1724-1725 :: twenty,\s+adj
numeral  suff.  -th.  Cp.  OE.  twentigoda,  ‘twen¬ tieth’. twenty,  adj.  and  n.  —  ME.  twenti,  fr.  OE.  twentig, twentig,  contraction  of  *twegentig,  rel.  to  OS. twentig,  OFris.  twintich,  Du.  twintig ,  OHG. zweinzug,  MHG.  zweinzec,  zwenzic,  G.  zwanzig. All  these  words  are  compounds  lit.  meaning ‘two  tens’.  Cp.  Goth,  twai  tigjus,  ‘two  tens’,  i.e. ‘twenty-,  and  see  twain,  two  and  -ty,  suff.  de¬ noting  multiples  of  ten. twi-,  pref.  meaning  two.  —  ME.,  fr.  OE.  twi-, ‘two,  double’,  rel.  to  OS.,  OFris.  twi-,  ON.  tv/-, tve-,  MLG.  twe-,  Du.  twee-,  OHG.,  MHG.  zwi-, G.  zwie-,  and  cogn.  with  OI.  dvi-,  Gk.  Si-  (for OL.  dvi-  (whence  L.  bi-),  Lith.  dvi-.  See bi-,  di-,  ‘two’,  a

### leaf 883 pp.1724-1725 :: twice,\s+adv
with  two blades',  compounded  of  twi-  and  bill,  ‘ax’, twice,  adv.  —  ME.  twies,  formed  fr.  OE.  rwigea, twiga,  twiwa,  ‘twice’,  with  -es,  gen.  suff.  used  ad¬ verbially;  rel.  to  OE.  twi-,  ‘two,  double'.  See twi-  and  adv.  suff.  -s. Derivative:  twic-er,  n. twiddle,  tr.  and  intr.  v.,  to  twirl  idly.  —  Prob.  of twig tympanum i  ooo iooy imitative  origin.  Cp.  ON.  tvidla,  ‘to  stir,  mix up’,  and  E.  tweedle. Derivatives:  twiddle,  n.,  twiddl-er,  n.,  twiddl-ing, twiddl-y,  adj. twig,  tr.  and  intr.  v.,  to  understand  (slang).  — Gael,  tuig  or  Ir.  tuigim,  twuigim,  ‘I  under¬ stand'. twig,  n.,  a  slender  branch.  —  ME.  twigge,  fr.  OE., rel.  to  MLG.  twich ,  MDu.  twijch,  Du.  twijg, OHG

### leaf 883 pp.1724-1725 :: between,\s+
 Bo- noncini). twiddle 'tween,  prep.  —  Abbreviation  of  between, tweet,  interj.  and  n.,  a  chirping  sound;  intr.  v., to  utter  a  tweet.  —  Imitative.  Cp.  twitter, tweeze,  n.,  a  case  of  surgical  instruments  (obsol.) —  For  twees,  an  aphetic  form  of  etwees,  pi.  of etwee,  fr.  F.  etui,  ‘case,  box,  sheath’.  See  etui, tweeze,  tr.  v.,  to  pluck  with  or  as  with  tweezers (colloq.)  —  Back  formation  from  next  word, tweezers,  n.  pi.,  small  pincers  used  for  grasping small  objects.  —  Alteration  of  tweeze,  n.,  after scissors. twelfth,  adj.  and  n.  —  ME.  twelfthe,  fr.  earlier twelfte,  fr.  OE.  twelfta,  fr.  twelf( see  twelve);  cp. ON.  tolfti,  Swed.  tolfte,  Dan.,  Norw.  tolvte, OFris.

### leaf 884 pp.1726-1727 :: two,\s+adj
ter-ing-ly,  adv. ‘twLxt,  prep.  —  Aphetic  for  betwixt, two,  adj.  and  n.  —  ME.  two,  earlier  twa  (fern,  and neut.),  twei,  earlier  tweien,  twein  (masc. ;  whence E.  twain),  fr.  OE.  twa  (fem.  and  neut.),  twegen (masc.),  tu  (neut.),  rel.  to  OS.  twene  (masc.), twa,  two  (fem.),  twe  (neut.),  ON.  tveir  (masc.), tvxr  (fem.),  tvau  (neut.),  OFris.  twene  (masc.), twa  (fem.  and  neut.),  Du.  twee,  OHG.,  MHG. zwene  (masc.),  zwo,  zwa  (fem.),  zwei  (neut.),  G. zwei,  Goth,  twai  (masc.),  twos  (fem.),  twa  (neut.), fr.  I.-E.  base  *duwo-,  *duwou-,  *dwd(u)-,  ‘two’, whence  also  OL  dvau,  dva  (masc.),  dve  (fem.  and neut.),  Avestic  dva,  Toch.  wu  (masc.),  we  (fem.), B.  wi  (for  *dwu,  resp.

### leaf 884 pp.1726-1727 :: twin,\s+adj
nd  drill. Derivatives:  tweill,  tr.  v.,  twill-ed,  adj. twin,  adj.  and  n.  — •  ME.,  fr.  OE.  twinn ,  rel.  to ON.  tvinnr,  tvennr,  ‘double,  twin',  ODan.  tvin- ling,  OSwed.  tvinlinger,  MLG.  twelink,  MDu.  t  we¬ ll  tic,  Du.  tweeling,  ‘twin’,  OHG.  zwinal,  ‘double’, z winding,  MHG.  zwinelinc,  zwillinc,  G.  Zwilling, ‘twin’,  and  cogn.  with  L.  bini,  ‘two  each’,  Lith. dvynit ,  ‘twins'.  See  twain,  two  and  cp.  next  word. Derivatives:  twin,  intr.  and  tr.  v.,  twinn-ed,  adj., twinn-er,  n.,  twinn-ing,  n. twine,  n.,  a  strong  thread  consisting  of  twisted strands.  —  ME.  twin,  fr.  OE.  twin,  ‘linen’,  orig. ‘a  double  or  twisted  thread',  rel.  to  Du.  twijn, dial.  Swed.  tvinne,  LG.  twern

### leaf 884 pp.1726-1727 :: between,\s+
irst  element  in  twayblade and  the  second  element  in  between,  betwixt.  Cp. also  bi-,  bis-,  deuce,  di-,  ‘two’,  dis-,  double, doubt,  dozen,  dual,  dubious,  duel,  duet,  duplex, dvaita,  dvandva,  dyad,  the  first  element  in  ba¬ lance,  barouche,  bevue,  biscuit,  doab,  dopatta, dubash,  and  the  second  element  in  combine, rebel,  revel,  sapsago,  tete-beche. -ty,  suff.  forming  abstract  nouns.  —  ME.  -te, -tee,  fr.  OF.  -te  (F.  -r^),  fr.  L.  -tatem,  acc.  of -tas,  which  is  prop,  a  fusion  of  the  suffixes  -id (appearing  in  words  like  juven-ta,  ‘youth’,  vi-ta, for  *vivi-ta,  ‘life’)  and  -ti.  L.  suff.  -tas  (gen.  -ta- tis)  is  cogn.  with  Gk.  -tyj;  (gen.  -ttjtoc  ) ,  OI. -tati-.  Cp.  e

### leaf 888 pp.1734-1735 :: between,\s+
 inferior,  infernal,  infra.  —  Cp.  also I.-E.  *nter,  ‘between,  among’,  whence  OE.  un¬ der,  OHG.  untar,  Goth,  undar,  ‘among’,  OI. antar,  ‘among,  between’,  L.  inter,  ‘between, among’,  Gk.  evxepa,  ‘intestines’.  See  inter, prep.,  and  cp.  words  there  referred  to. Derivatives:  under,  adv.  and  adj. under-,  pref.  —  From  prec.  word, undercroft,  n.,  a  crypt.  —  Compounded  of  under and  obsol.  croft,  ‘vault’,  which  is  borrowed  fr. VL.  crupta,  fr.  L.  crypta,  fr.  Gk.  xpujrxr,,  ‘crypt, vault’ ;  see  crypt. undergraduate,  adj.  and  n.  —  A  hybrid  coined  fr. under  and  graduate,  a  word  of  Latin  origin. undercurrent,  n.  —  A  hybric  coined  fr.  under  and current,  a  word  of  Latin  origi

### leaf 889 pp.1736-1737 :: between,\s+
en.  Cp.  F.  entreprendre,  ‘to  undertake’, fr.  entre,  ‘between,  among’,  and  prendre,  ‘to take’. Derivatives:  undertak-er,  n.,  undertak-ing,  n. and  adj.,  undertak-ing-ly,  adv. underwrite,  tr.  and  intr.  v.  —  Loan  translation  of L.  subscribere,  fr.  sub,  ‘under’,  and  scribere,  ‘to write’.  See  under  and  write. Derivatives:  underwrit-er,  n.,  underwrit-ing,  n. undies,  n.  pi.,  women’s  underwear  (colloq.)  — Formed  from  the  abbreviation  of  underwear with  -ies,  pi.  of  dimin.  suff.  -y. undine,  n.,  a  female  water  sprite.  — -  G.,  fr.  F.  on- dine,  introduced  by  the  French  poet  Pierre  de Ronsard  (1524-85)  fr.  ModL.  undina,  a  word coined  by  Paracelsus  fr.  L.  unda,  ‘wave’.  See undate
```


## [2026-09-05T20:11:25.852Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i in (99,100,103,241,242,248,270,883,884):\n    l=leaves[i]\n    nums=re.findall(r'\\b1?\\d{2,4}\\b',l)\n    print(i, [n for n in nums if len(n)>=3][:20])\nEOF",
 "description": "Find running head numbers per leaf"
}
```


### [2026-09-05T20:11:27.594Z] TOOL RESULT

```
99 ['1797', '166', '1779', '1848', '1779', '1848', '167', '1813']
100 ['166', '169', '615', '1947']
103 ['1863', '1921', '1903', '1825', '1870', '1744', '1829', '1802', '1850', '1933', '1530']
241 ['1672', '1774', '1862', '1805', '1833', '1830', '1770', '1847', '1807', '440', '441']
242 ['1805']
248 ['065', '1778', '1862', '5015', '015', '1729', '0177', '454']
270 ['497']
883 ['1666', '1692', '1763']
884 ['516', '1839', '1914']
```


## [2026-09-05T20:11:47.725Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(870,900):\n    l=leaves[i]\n    nums=[n for n in re.findall(r'\\b1[67]\\d\\d\\b',l)]\n    head=re.findall(r'^\\s*\\S+\\s',l[:60])\n    print(i, nums[:8], repr(l[:40].replace('\\n',' ')))\nEOF",
 "description": "Scan Klein leaves 870-900 for page numbers"
}
```


### [2026-09-05T20:11:49.378Z] TOOL RESULT

```
870 ['1642', '1643'] ',  v.,  and  -ation  and cp.  L.  transp'
871 ['1644'] 't.,  lit. ‘the  woman  led  astray’,  pp'
872 ['1643', '1647'] ',  Tremandra,  Tremella,  tremulous,  tr'
873 ['1795'] 'rank (Roman  antiq.)  —  L.  triarii,  f'
874 ['1613'] 'ivision  of  their  in¬ testines. tricli'
875 [] 'gonometric,  trigonometr-ic-al, adjs. tr'
876 ['1776', '1654'] 'x,  gen.  tripli- cis.  See  triplex  an'
877 ['1746'] '  pp.  of  terere  ‘to  rub, thresh,  gr'
878 ['1707', '1657'] 'T),  ‘tongue  of  the  balance,  balance'
879 [] '� I.-E.  base  *tro-g-,  *tri-g-  is  an'
880 ['1661', '1689', '1662'] 'orcer,  trusser,  trousser,  torser  (F.'
881 ['1742', '1780', '1664', '1665'] ',  suff.  corresponding  in  meaning  to'
882 [] '(=  F.  ton¬ neau),  ‘cask,  tun’,  dimi'
883 ['1666', '1692', '1763'] 'turriculated,  adj.,  resembling  a  sma'
884 [] "of  two',  fr.  did,  ‘two’. Derivatives"
885 [] 'Truravov, ‘kettledrum’.  See  tympanum  '
886 ['1771'] '(i.e.  ‘alms,  charity’).  Cp. the  seco'
887 ['1675'] 'rich’.  The  first  element  is  rel.  t'
888 ['1724', '1676', '1785', '1776'] 'mbrella,  adj.  and  tr.  v. umbrette,  '
889 ['1748', '1679'] 'nd  adj.,  understand- ing-ly,  adv.,  u'
890 ['1680', '1781'] '  universolog- ist,  n. univocal,  adj.,'
891 ['1755'] '  the  past  participle. urea,  n.,  cry'
892 ['1748', '1779'] 'us.  See  use, n.,  and  -age. usance,  '
893 ['1786', '1649'] 'id.  Cp.  also uvea,  uvula. uvanite,  n'
894 ['1795'] 'andering’,  formed with  gerundive  suff'
895 ['1661', '1730', '1671', '1640', '1707', '1691', '1779', '1787'] ',  bodies  of  those  who were  slain  i'
896 ['1692'] '��,  nr^  (Hesychius), ‘web’,  L.  pannu'
897 ['1657'] '  —  A  hybrid  coined  fr.  vari¬ ola  '
898 ['1763', '1763', '1694', '1695'] 'agential  suff.  -or. vau,  also  waw,  '
899 ['1696', '1793'] '  F.)  veine,  fr.  L. vena,  ‘blood  ve'
```


## [2026-09-05T20:12:16.023Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 153 (p.132) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==154' HRN.txt | head -60",
 "description": "Print Horn p.132"
}
```


## [2026-09-05T20:12:17.018Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB leaf 75 (p.65) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==76' HUB.txt | head -60",
 "description": "Print Hübschmann p.65"
}
```


### [2026-09-05T20:12:17.669Z] TOOL RESULT

```
=== HRN leaf 153 (p.132) ===
- 132 —
591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
phlv. depäk {S«äy. näsäy. 4, i), arm. LW. dipak, syr.
LW. :i2n.
Die Etymologie ist nicht sicher, da im Sanskrit nur
Formen mit T, nie solche mit e vorkommen.
592. dlden 'sehen, dld 'Anblick; sehend', didär,
ap. i^dai-, didiy sehen'; aw. l/'rföi-, a]di^aifi:
phlv. dUan; ai. V^dhäi-, didhye.
kurd. dUin *sehen' ; af/. Udal ; bei. dU, diMr (LW.),
dtdö:^ ^Augapfel'; wa/. didig-am.
593. "des, -dis, -des gleichend, ähnlich*.
aw. dareS' 'Blick* (yt. 19, 94); ai. dfc- *das Sehen;
sehend*, -dfga- '-Aussehen; -sehend*.
Der r- Vokal ist hier durch e vertreten, wie in heSe
(No. 256). Aw. daesa- (yt. 13, 104), das Darmeste-
ter als *Traum' nimmt, ist zu unsicher, um ver-
glichen werden zu können.
594. deg *Topf*, vergl. dez, deze,
phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^
tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*.
LW. kurd. dizik; af/. deg^ decka; bei. deg, dez, dPd,
Oegci (59); wa/. dlg^ sar. deg.
Zu ai. \/'deh', degdhi 'bestreichen, kitten', got. deignn
'kneten, aus Thon formen*.
595. dlger, dediger (Vis und Rämin, S. 29 V. 5 v. u.)^)
anderer ; sidlger^ süHg ein Drittel* (AM. 110 Zeile 2 v. u.).
ap. *duvit%yam karam (Darmesteter, Et. ir. I, 150,
183); phlv. datlgar, vergl. dat (Fr. Müller, WZKM.
5, 262).
bei. n. m, n (386) (vergl. Bartholomae, ZDMG.
44, 554).
^) Das sein g von fingö {ng = ngli) bezogen haben könnte, wo-
gegen aber gr. &iyydvü} spricht. Also standen wohl schon im Indo-
germanischen gh und g neben einander.
y
2) duSlger will Salomann im Sähnäme herstellen, M61. asiat.
IX, 281/5; vorgl. Ilorn, KZ. 32, 578 No. 2.
```


### [2026-09-05T20:12:19.680Z] TOOL RESULT

```
=== HUB leaf 75 (p.65) ===
— 65 -
aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
das haufig vorkommt, auf mp. dsh zuriick?
589. Bei Rosen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
Weise', zd. dis Veisen', osset. dwd%8}n zeigen u. &. w.
Also doeh -dEs = zd. ^da^a-, auch wenn dies nicht
rait daesa- yt. 13, 104 (*Traumbild'?) identisch ist.
594. Wenn dBz, deza *Kochtopf zu got. deigan *kneten, aus
Thon formen* (Wzl. dhig%) gehOrt, ist es verwandt mit
Nr. 563 diz, dSz *Burg', s. oben. Ob auch deg *Koch-
topf dazu gehort, ist fraglich, da 1) idg. dhig^h durch
skr. dBgdhiy digdha- nicht gesichert ist (vgL Brug-
mann, Grundriss I, p. 344) und 2) idg. dhoi^ho- im
Neup. zu *d^y werden miisste. Np. d^ (afgh. LW.
dEg *Kesser) setzt ap. ^daika- voraus. Phi. dSg 'Kesser
(Gl. and Ind. 288) kann eine junge Form sein. Zu d.
Tiegel u. s. w. vgl. Kluge, Wb. 5. Aufl. s. v.
595. Piige hinzu : paz. dddlgar ^secondly, other' Shk. 240,
Min. Gl. 53, did 'second' Shk. 241, Min. Gl. 61, dadum
'second' Shk. 240. Dieses paz. did ist direct = ap.
duvitiya- *der zweite . Vgl. WZKM. 5, 262.
596. Die kurdische Form lautet dem *Gesicht' bei Socin,
kurd. Sammlungen II, p. 307 ; afgh. lies ISmq.
599. Besser *daidavara- (Fe&tungBmsiuer*)^) Sils *daigavara-
anzusetzen, vgl. oben Nr. 594 und 563. Anders Fr.
Mil Her, WZKM. 8, 95 {^daya-vara- *Scheidemauer).
Falls dtvar (mit i) die urspriingliche Form ist (vgl.
afgh. LW. dlval *a wall'), ware dUvdr iiber *diyvar =
*did-vclr auf ap. *dida-vara- zuriickzufiihren. Alles
unsicher. Nebenform dwal JRAS. 1893, 463.
600. NSldeke macht mich darauf aufmerksam, dass im
ersten Verse von Vis u Ramin ra Dativpartikel (und
niar an Nominativ) ist.
>) Vgl. bara I diz *Mauer der Festung' Fird. I, 452, 325.
HUbsohmann, Peraisohe Studien. 5
```


## [2026-09-05T20:12:30.215Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"biš\\|bēš\\|bes 'mehr'\\|beš\" HRN.txt | head -20; echo \"=== search 'mehr'\"; grep -n \"^[0-9]*\\. *b[eē]š\" HRN.txt | head",
 "description": "Search Horn for bēš"
}
```


### [2026-09-05T20:12:30.264Z] TOOL RESULT

```
=== search 'mehr'
```


## [2026-09-05T20:12:31.781Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 345 346 359 360 371 378 379; do echo \"=== BQT_v2 leaf $L (approx p.$((L+543))) ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -25; done",
 "description": "Print BQT vol2 candidate leaves"
}
```


### [2026-09-05T20:12:33.477Z] TOOL RESULT

```
=== BQT_v2 leaf 345 (approx p.888) ===
‫دندان فرش ‪:‬‬                                                                                        ‫و‬‫‪7‬‬


 ‫وثابه ازبرابر کردن‪ -‬وخصومت ورزندن‬
                                 ‫باشد ک‬                                                          ‫هم هٽ ‪.‬‬
                        ‫کودنه خواستن هم هست ‪.‬‬            ‫دندان ]ریز ‪ ۱‬با مزه بالف‬
                                                         ‫کشده وبای فارسی » بمعژی خلال اشد و آن‬
                                                         ‫چوبی با اسنخوانی است که مبان دندانها را (‪)۱‬‬
                                                         ‫باکت کنند ؛ و بفتح همزه همآمده است که‬
 ‫دندان داشتی سکابه از چشم‌داشت‬
                                                                                       ‫دندان ایریز باشد ‪.‬‬
 ‫و لوقع داشتن باشد ‪ -‬کونابه ازکینه ورزیدن‪-‬‬
‫وفدام لمردن هم‬
             ‫و در کاری بسیار بجد شدن ا‬
                                                         ‫‪-‬باشین نقطه داره‬         ‫دندان ] پربش‬
                                          ‫‪۰‬‬   ‫ھت‬         ‫بروزن ومعنی دندانآ پریز است که خلال باشد ؛‬
                                                                               ‫وبفتح همزه هم درست است ‪.‬‬
‫دندان ادن = بممنی چسبیدن باشد‬
                                                          ‫د ند آن ‪ ۲‬فریز‪ = ۴‬بابفراو‪.‬زن‌ومعنی‬
 ‫‪.-‬وکنابه ازبرابری کردن ‪ -‬وخصومت ورزسن‬                                   ‫دندانآ پربزاست که خلال باشد ‪.‬‬
                 ‫و کینه خواستن هم هت ‪.‬‬
                                                          ‫دندان] فریش ‪ = /‬بروژن وهی‬
      ‫لطهف‬
         ‫ای ق‬
            ‫بن ب‬
=== BQT_v2 leaf 346 (approx p.889) ===
 ‫‪۳‬‬                                                                                             ‫دسسان کاو‬

 ‫واین رسع دقردیم متمارف بوده است وآنرا هزد‬          ‫دفدان پریش است که خلال و دندان یاکه کن‬

                          ‫دندان هم میگویته ‪۱‬‬                                                          ‫باشد ‪.‬‬
‫دندان فمای ؟ ‪ -‬کنابه ازختمآلود‬                      ‫د ندان کاو‪ ۱)۰( ۱‬باکاف‌بالف کشیدہ‬
  ‫اهر‬
    ‫هک‬‫ظیند‬  ‫وغضاکه باشد ‪ -‬و کسی را نی‬
         ‫ازکو‬                                           ‫بواو رده » چیزیکه بدان دندان خلال کنند ‪۹‬‬


             ‫وفروتلی کند ‪.‬‬       ‫ز‬‫عضبج‪-‬‬
                                      ‫ور ون‬
                                          ‫قه‬        ‫د ندان کر دن » کنابه‌ازاعراش کردن‬
 ‫دند ان نماید ‪ ۴‬بمنی‌خوشحال‌شود‬                                                    ‫سومضایقه نمودن باشد ‪.‬‬
 ‫و خندد ‪ -‬وماضی غضبنا کهشدن تورسالیدن‬                ‫دندان کنان ‪ - ۲‬ختحکاف ک‪.‬نابهاز‬
‫بعنی تره‌اند ‪ -‬و درعضشب‬      ‫وعجز کردن هم هت‬
                                                     ‫قطم طمم ‪ -‬وبی‌وقری و بی‌قراری و زاری ‪-‬‬
               ‫شود ‪ -‬وزاری کند وعاجز گردد ‪۰‬‬
                                                    ‫ورسوایی باشد ‪ -‬ویضم‌کاف ک»نابه از رسوا کنان‬
 ‫دندان نمودن = کنابه ازترسیدن‪.‬‬                                                    ‫وخوار و زار کنان باشد ‪.‬‬
 ‫وترسالیدن ‪ -‬و عاجز شدن ‪ -‬وزاری کردن ‪-‬‬
 ‫وتهدمد نمودن باشد‪ -‬وخوشحال گردیدن وخنده‬            ‫د ند ان کندن » کنابه ازفطع طمح‬
                       ‫کردنرا نیز گونند ‪. ۵‬‬                                     ‫کردن باشد ‪.‬‬
 ‫‪۵‬ندا ‪ - ۱ 4‬بر وزن مردانه ک‪.‬نگرة‬                     ‫دندان ګگوساله ‪ -‬نوعی ازتیر باشد‬
=== BQT_v2 leaf 359 (approx p.902) ===
 ‫دوکار ‪:‬‬                                                                                                        ‫تس‬


‫پبازرا گوبند‬      ‫انی وساد بی قطه‪ .‬بلغت ادلمغرب‬              ‫بمعنی دشوینه است که ظرف شیر دوشیدن‬
                                                                                                                ‫باشد ‪¥.‬‬
                              ‫وبعربی صل خوانند *‬
                                                             ‫‪۰‬‬        ‫‪۰‬‬    ‫‪۰‬‬     ‫‪"°‬‬              ‫‪۴‬اه‬   ‫ه‬   ‫‪۵‬‬

‫تخم‬     ‫کو کو »‬   ‫بروزن‬   ‫باقاف‬    ‫‪-‬‬   ‫قوه‬   ‫دو‬
                                                                                                           ‫باشد ‪۰‬‬    ‫‪“a‬‬   ‫‪۱‬‏‬
‫زردك صحرابی است‌وییخ آن شقاقل است ‪.‬و گیاه‬
‫آنرا خرس گیاه خوانند » چه خری آنرا بسیار‬                         ‫دشویز ‪ - ۱ ۵‬بازای«وزبروزن‌یوشد‪.‬‬
                                                                                                 ‫دختر بکر را گونند ‪۰‬‬
                                        ‫دوست مسدارد ‪۰‬‬
                                                             ‫دو طفل بسند یف ه ‪-‬کنابه ازمردمان‬
‫بسکون سین بی نقطه ‪,‬‬                    ‫دو فوس‬
‫لغتی است بونانی ‪ ۱‬بمعنی دوقو که تخم زردك‬                                                    ‫چشم باشد ‪.‬‬
 ‫صحرایی‌باشد‪ .‬وبعضی کویندنوعی ازآست ودآرا‬                        ‫دو طقل نود ‪ -‬بمعنیدوطفل‌بندیده‬
‫بشیرازی بدران خواشد ‪ ,‬وبعضی دبگ رکفته اند‬                                        ‫است که مردمان چشم باشد ‪.‬‬

              ‫فمس صحرایی است‬     ‫رتخ‬‫کوس‬
                                      ‫دوق‬                        ‫از دو لب مهوت‬   ‫کنابه‬       ‫=‬    ‫طوطی‬         ‫دو‬



=== BQT_v2 leaf 360 (approx p.903) ===
  ‫‪ ۵‬ات‬   ‫تن‬
                                                                                                    ‫د وگاله‬


 ‫دول = بانالیمجهول بروزن غول د؛لو‬                        ‫دگوافه ‪ ۱‬ه باخفای ثانیوکاف فارسی‬
 ‫آبکتی رگاویند‪ - 9‬و برح دلو را گیفزته‌اند‬                ‫بند و صف آن يك‬ ‫پروزن فلانه ‪ ,‬عدد دگوورا‬
  ‫که بر جحبازدهم باشد ازدوازده بروج فلکی ‪1‬‬                ‫لماز همست ٍِ‪.‬‬  ‫ت‬‫کدو ر‬‫به از‬    ‫او‬‫کتن‪-‬‬‫اس‬
 ‫ویمعتی مکار ومحیل وشطاح ‪ -‬وبی‌حیا ‪ -‬وسفله‬
 ‫هم هت ‪ ۷‬و‪-‬دولآمارا نگیوزبند‪ , ۸‬و آن‬                     ‫گواو مره بکسر واو دوبم ک؛نایه‬
                                                                                     ‫د‬
                                                          ‫واوزمین را بز‬
                                                                      ‫ازشب وروز باشد ‪ -‬وبرج ور ک‬
‫ظرقی باشد مربع و مخروطی شکل که آبرا از‬
                                                                                                    ‫تفا‬         ‫کو‬
 ‫چوب سازند و در مر کز مخروطی آن سوراخی‬
 ‫کنند ومحاذی سوراخ سنگه آسیا نصب نمایند‬                  ‫«کنایه‌از آسمان‌وزمین‬     ‫دو گاهو اره‬
‫و پراز غلهسازند ‪ -‬و تیرکشتی را لفیزته اند‬                                                                 ‫‪.‬‬     ‫ات‬
 ‫وآن چوب بلندی باشد کهدر وسط کشتی بپرای‬
 ‫کنند ‪ -‬وبه‌عنی که وخربطه همآمده است‌چه‬                   ‫را کوبند که در آن‬            ‫کی‬
                                                                                        ‫چسبد‬
                                                                                           ‫و و‬
                                                                                             ‫کوقجه‬
                                                                                                 ‫صند‬
 ‫که وخربطه که‌برمیانندند دولمیان خوانند‬                   ‫دوك و گروهةٌ ریسمان و پنبه گذارند » وبعربی‬
 ‫وتح ثالی » پوست بيخ درخت‬
=== BQT_v2 leaf 371 (approx p.914) ===
 ‫در ند‬                                                                                                      ‫‪۱۱‬‬
‫ذیر ننگ س بنتح اول و تایقرشت‬                                         ‫ګلی امت که آنراکاو‬
                                                                                      ‫دبد نگاو =‬
‫وسکون نون وکاف فارسی ک»نایه ازدلبا است که‬                           ‫چشم گوبند ‪ -‬ولوعی از سلاح و جامه باشد که‬
                               ‫عالم سفلی باشد ‪.‬‬                     ‫پوشند ‪ -‬و نام لوعی از انگوز هم‬            ‫ردورزجنگه‬
                                                                    ‫‪ -‬وستارژ دبران را نگیوزیند » واو یکی‬            ‫حت‬
 ‫دیرر ند سور = بفتح اول و کسر‬
‫نقطه » بمعنی دبرتنگه است که‬         ‫‪۳‬‬        ‫هر دو رای‬                ‫از منازل قمراست و بمریی عین‌الئور خوانند ‪.‬‬
               ‫کنابه دابزنا وعالم سقلی باشد ‪.‬‬                        ‫دید گاه = باکاف فارسی‌بروزن نیمه‬
 ‫دیردی ‪ = ۲‬بکر اول و زای هوزء‬                                                          ‫جها»ی نشستن دیده‌بان باشد ‪.‬‬
                                                                                                                 ‫را‬
 ‫بمعمی بسیاریمان وزلد کالی‌کن ‪ -‬ونام روزییست‬                         ‫دیده کنان د بنم کاف و دون بالف‬
                ‫وهفتم است ازماههای ملکی ‪.‬‬                           ‫کشیده وبنون زده " کذابه ازنگاه‪.‬كردن و تأمل‬
                                                                                                ‫لمودن درکاری باشد ‪.‬‬
‫= کنابه ازدتیااست زیرا‬      ‫دار سیتحی‬
‫که‌آن مانند سپنج که خائة علفی‌است بقا وتباتی‬                         ‫دیده گه = بففتحاکرافسی بورزن‬
                                                                    ‫نیمه ره » مخفف دبده گاه است که جلی نشستن‬
                                                     ‫ندارد ‪.‬‬

                                                                                                       ‫دیده بان باشد ‪.‬‬

 ‫مردن‪ :‬و فوت شدن باشد ‪ -‬وکنایه از دورشدن‬                             ‫دیده‌ور شدن ه کنابه از رسدن‬
                                    ‫‪.‬‬       ‫©‬        ‫هم هت‬           ‫بجیز هاباشد چنانکه هت ونظرالداختن چنانکه‬
 ‫دی مکافات ‪ -‬کتابه از دبیا عوالم‬                                                                                ‫باد ‪.‬‬
                                            ‫سفلی باشد ‪.‬‬              ‫كر ب=فتح اول بر وزن غير » معبد‬
=== BQT_v2 leaf 378 (approx p.921) ===
      ‫اه‬                                                                      ‫دبوار خانه روزن شدن‬

‫آرا‬
  ‫وسکون دوسین و فوقانی ‪ ۰‬دوابی است که ن‬                            ‫از قپر وغضب هم نوشته‌اند ‪.# ۷‬‬
‫انده قوقو گونند وبرکلف وبهق مالند تبافاعشد »‬         ‫ررنو‌شدن‪ ».‬کناه‬               ‫نه‬
                                                                                    ‫خواار‬
                                                                                        ‫ذی‬
‫واگرطفلی دبر بحر کت بد چون برومالند زود‬                                  ‫از خراب دن خانه باشد ‪.‬‬
                                                     ‫ديو ار گر = دبوارساز ‏ وگل‌کار وینارا‬
‫دیوال ‪ ۴‬سبا لام" بروزن ومعنی دیوار‬                                                            ‫گونشد ‪.‬‏‬
‫است» چه درفارسی راولام بهم تبدیل مییایند ‪#.‬‬
‫‪۰‬‬    ‫فرشت‬     ‫رای‬   ‫بفتح‬   ‫دیواله رو‬
‫شخصی‌را کوبند کهمدابنوندانهاسلوك کند وبراه‬                                ‫عاجز وزبون هدن باشد ‪.‬‬
                                            ‫رود ‪.‬‬    ‫همز هو بای‌فارسی‬   ‫د یو اسست ‪ ۴‬یک‬


    ‫‪ - ۱‬نظر بتصور مهيب و هولناك بودن دبوان‪ « .‬هرچیز را که از افراد خودفوی جثه‌تر‬
     ‫و بزرکترباشد بدیو اضافت نمابند (با بفول که آنهم دو موهوم است) مثلاکمان بز رکه راکمان‬
     ‫دیو خوانندیسنی دبورامیدابد‪ .‬نوعی ازاسیست‌را که ‪-‬اق وبرگهآن ازامتال بزرکنراست دیوامیت‬
    ‫گوبند ‪ .‬کلوخ کلانرا دیو کلوخ » عنکبوت برزکه را دیوپا» زبراکه بابپای بزرکه و بلند‬
     ‫دارده و گردناد را که بلند شود ديو باد گوشد»‪ 9‬انجمن آرا» ولىز ‪ :‬دیوحان › دیوچه‪ ,‬دیوخاره‬
                       ‫دبودار » دیودل» دیوزای» دیوسار » دیوگ » دیو گندم‪ .‬ورك‪ :‬فاب ‪ ۱‬ص ‪٩۹۱.‬‏‬
    ‫‪ 2‬وجنگه کرد‬      ‫دبوار («‪.‬م‪).‬‬   ‫‪-‬‬   ‫‪۴‬‬           ‫امست («‪.‬م‪).‬‬    ‫از ‪ :‬دنو (ھ‪.‬م‪4 (.‬‬          ‫‪۳‬‬

    ‫بسیار بدرارك » و کشتن کرد فراوانی بدر شارستان » در گرکوی عاقبت بستد » و ارك را و قلمة‬
=== BQT_v2 leaf 379 (approx p.922) ===
  ‫ديو دولت‬                                                                               ‫‪٩۱‬‬
‫باشد ساء رتگك ‪ .‬چون‬       ‫کفته‌اند » و آن‌کرهی‬        ‫دیو پا ‪ - ۱‬با نانی مجهول وبای فارسی‬
                                                      ‫بالف کشیده » عنکیوت‌را کو‌ند و نگایماهی‌هم‬
 ‫ه شور کنند هر‬ ‫اهنگر‬
                   ‫خشبش‬
                      ‫را خشك کرده در‬                 ‫هت که آنرا انده قوفو و حندقوقی خوالند ‪٩‬‏‬
  ‫شرشه کهدنرجااباشد بشکند وگیاهی همهت‬                       ‫ودیو پای نگیفزتداند باضافةٌ تحتالیآخر ‏‬

                                                     ‫دیو باد ‪ ۱‬با نانی مجهول وبای ابجد‬
                             ‫ِ‬   ‫مدان اندام خار اد‬
                                                     ‫بروزن دبوزاد ؛ بمعنی گردباد است ‪ -‬وبادنندی‬
 ‫دیو خار ‪ ۰ ۱‬با خای شطه دار(‪ )۱‬بر‬                    ‫ویند که هوا را تاريبك سازد ‪ -‬و جنون‬  ‫گز‬
                                                                                           ‫را ل‬
 ‫پرخار؟ وآراسفید‬      ‫وزن پیشکار " درختی است‬                              ‫ودیوانگی را گنفزته‌اند ‪-‬‬
      ‫خار وخفچه گوبند وبعربی عوسج خوانند‪.‬‬            ‫جنهیول و بای ابجد‬
                                                                     ‫بلنوك = بما ا‬
                                                                                 ‫ك‬
    ‫ن‬    ‫دیودار ‪ ۰ ۱‬باانی مجه‬
    ‫وولزبر‬                                            ‫بروزن ررشخند ‪ ۰‬نام روزشانزدهم باشد از هرماه‬
 ‫و صاوس‬       ‫سروباشد؟‬   ‫از درخت‬    ‫بعلدار ‪ .‬لوعی‬     ‫ملکی‪ -‬ولقب قارن برادر زاد جمشید هم هست‬
 ‫هندی را نیز گویند و بعربی شجرةااجن خوانند‬            ‫چه او را فارن دبواند مبگفته‌اند و طرمورث‪-‬‬
‫و دراختبارات شجرةالله نوشته‌اند ؛ وبضی گویند‬          ‫وجمشید را هم میگویند‪ .‬ونام داروبی هم‌هست‪.‬‬
‫ای دارد که‬    ‫درختی امست مانند درخت کاج وشره‬
                                                      ‫دیو جامه ‪ ۰ ۱‬با ای مجهول » نوعی‬
‫علاح لقوه میکند ‪ -‬و مردم دیواله و مصروع‌را‬            ‫از جامةٌ پوستین باشد که آنرا واروله میپوشند‬
```


## [2026-09-05T20:12:48.543Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor vol in ('BQT_v2_pages.txt',):\n    leaves=open(vol,encoding='utf-8',errors='replace').read().split('\\f')\n    for pat in ['دویست','دیهیم','دیگر','دگر']:\n        hits=[i for i,l in enumerate(leaves) if pat in l]\n        print(vol,pat,hits[:20])\nEOF",
 "description": "Locate BQT v2 headwords"
}
```


### [2026-09-05T20:12:50.509Z] TOOL RESULT

```
BQT_v2_pages.txt دویست [385]
BQT_v2_pages.txt دیهیم [282, 463]
BQT_v2_pages.txt دیگر [2, 11, 16, 20, 27, 31, 35, 37, 39, 42, 44, 46, 49, 57, 60, 63, 73, 78, 80, 82]
BQT_v2_pages.txt دگر [28, 94, 153, 156, 202, 211, 225, 240, 270, 299, 300, 303, 337, 376, 400, 423, 466, 511, 534, 547]
```


## [2026-09-05T20:13:01.930Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (282,463,385):\n    l=leaves[i]\n    print(f\"=== leaf {i} (~p.{i+543}) len={len(l)} ===\")\n    for pat in ('دیهیم','دویست'):\n        j=l.find(pat)\n        if j>=0: print('   ...',l[max(0,j-300):j+300].replace('\\n',' '))\nEOF",
 "description": "Inspect BQT leaves with dayhim/devist"
}
```


### [2026-09-05T20:13:03.532Z] TOOL RESULT

```
=== leaf 282 (~p.825) len=4784 ===
   ...                                       ‫آهده است ‪. ۸‬‬                                                           ‫داها ‪ .‬بروژن باها ء یمعنی دره و عار‬                                                                                                                       ‫کوه باشد ‪.‬‬ ‫وميم » بمعنی دیهیم است که تاج مرصع باشد ‪.‬‬                                                              ‫داهل ‪ - °‬نم ثالك بر وزن ک کل ‪.‬‬  ‫دای ‪ -‬بروزن‌لای‪.‬هرچینه‌ورده‌ومرتبه‌را‬                        ‫‪3‬‬    ‫از دبوارکلی ‪۰‬‬       ‫کون‬                                                              ‫آ
=== leaf 463 (~p.1006) len=4097 ===
   ...  ۳‬ح ‪« : »۳‬کلمة زاوش با زواش که در همة فرهنکها‪‎‬‬                                                         ‫آقای پور داود نوشته اند بش‬   ‫ضبط است وشمرای قدیم بمعنی مشتری امتعمال کرده‌اند بنظز میرسد که مانندکلمات درهم ودیتار‪‎‬‬   ‫( خدای بررکه ) مشتق باشد ‪ .‬اورمزدی‪‎‬‬                ‫والمای و دیهیم و غیره اصلا بونانی واز زوس ‪81062‬‬                                                                                                  ‫کفت‪: ‎‬‬                ‫ترا بهره کرده سعادت زواش‪. ‎‬‬                          ‫حودات را داده بهرام نخس‬   ‫د تفل ‪‎‬سرف ‪. ٩۲۱۳‬‬  ‫یاهلاتسرهش ‪‎‬رهشناربا ‪
=== leaf 385 (~p.928) len=2137 ===
   ...                               ‫راا ی‬                          ‫ای‬                                                                    ‫(‪ )۱‬چك ‪ :‬موم ‪.‬‬   ‫‏‪ ٩‬د حرف دوازدهم از الفبای فارسی وحرف دهم ازالفبای عربی (ابتث) وحرف بستم‬   ‫از حروف ابجد ‪ ,‬وآنرا ر ‪ ۵۲‬وراه ‪ ۰۵۲‬نامند و درحساب جمل دویست گر ند‪ .‬این حرف به «ل»‬                                   ‫[ك ‪ :‬س بح از ديباچة مولف ] ‪ .‬و «ن» تبدیل شود ‪.‬‬                                                                                ‫ر‬  ‫(عرب ) ابوزنانی ‪ 0016۸‬بمعنی صمفی که از‬ ‫‏‪ = ۱١‬رانینا = رائینا ‏ راتینج م‬   ‫‪.» ۹۱‬رك ‪:‬
```


## [2026-09-05T20:13:18.778Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(365,400):\n    l=leaves[i]\n    if re.search('هیم|هبم|بهیم', l):\n        for m in re.finditer('هیم|هبم', l):\n            print(i, i+543, repr(l[max(0,m.start()-200):m.start()+200].replace('\\n',' ')))\nEOF",
 "description": "Search BQT for dayhim near p.910-940"
}
```


### [2026-09-05T20:13:20.601Z] TOOL RESULT

```
365 908 'بر وزن شبخیزی ک\u202c                          \u202bاست که زراعت کننده ومز آرع باشد\u202c   \u202bوععنی\u200cدهقان\u202c                                                        \u202bو دهقان معرب آنست \u202a -\u202cومردم تاربخی و تاریخ\u202c \u202bثالی و هیم»\u202c    \u202bبفتح اول وسکرن\u202c   \u202b\u202a-\u202c\u202c   \u202bدهم\u202c                                        \u202bویند \u202a. ۴\u202c\u202c                                                                                       \u202bگز\u202c\u202bدان را ن\u202c   \u202b\u202a۰'
368 911 '۱\u202cص \u202a۱۲٤:۲\u202c\u200f »\u202a .\u202cآنجه کهدرآغاز کتاب\u202c                                                  \u202bتصغیر ) « اسشق \u202a» ۱۰\u202c؛ معرب د\u202c                                                                          \u202bبرای تفهیم موضوع کتاب نویسند \u202a.\u202c\u202c                                                                                                \u202bیه از صفحهٌ \u202a۷۰٩\u202c\u200f\u202c    \u202bاینکه سه روز موسوم به«دی» باهم اشتباء نشوندنام\u200cهريك ر'
381 924 '  \u202bدهیم\u202c                                                                                            \u202b\u202a۲۱\u202c\u202c                 \u202bهت که بعربی سنای گوبند \u202a.\u202c\u202c                  \u202bدیو کلو چ \u202a = ۱\u202cبضم کاف ولام بواو\u202c'
381 924 '        \u202bآبادانی دور باشد \u202a -\u202cوجایگاه خراب و خرابه \u200f\u202c                                                           \u202bوچراگاه دور را نیز گفته\u200cالد \u202a -\u202cوسردسیر را هم\u202c          \u202bدهم\u202c           \u202bوبعضی کوبند دبهیم افسری\u202c \u202bتیمن وتبر ك بربالای\u202c    \u202bبوده که آ را درقد\u202a.\u202cیم سهت\u202c                                                       \u202bمیگونشد\u202a..\u202c\u202c \u202bسرپادشاهان مویباخته\u200cاند کولاه مرصع را فيز\u202c                   \u202bجن\u202c '
383 926 '             \u202bشوت\u202c\u202bهشدچ\u202c \u202bبار\u202c                                                                \u202bنرع وزرع ازبپ\u202c \u202b« لفت فری \u202a » ۸۲۲\u202cاین کلمه و معنی با همین شاهد در لغت امه عجیبی که در حاشيةٌ لغت لام\u202c   \u202bهبماین\u202c\u202bاسدی آقای نخجوانی است دیده میشود و لغوبین دیگر لیز عین آنرا بپمین صورت و\u202c \u202bشاهد می\u200cآورند » لکن بگمان من اکر شمرواقعاً از رودکی باشد (وکمان لمیکنم که باشد ) در\u202c  \u202bاین لفت ومعنای آن پیدا شده است'
```


## [2026-09-05T20:13:28.136Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(leaves[381])\nEOF",
 "description": "Print BQT leaf 381 in full"
}
```


### [2026-09-05T20:13:29.871Z] TOOL RESULT

```
  ‫دهیم‬                                                                                            ‫‪۲۱‬‬
                ‫هت که بعربی سنای گوبند ‪.‬‬                  ‫دیو کلو چ ‪ = ۱‬بضم کاف ولام بواو‬
 ‫دو مشنگ‪ -‬بفتح میم وشین‌قطه‌دار‬
                              ‫ډ‬                            ‫کشیده وبجیم فارسی زده» طفل مصروع و کودگ‬
 ‫وسکون نون وکاف فارسی» بمعنی کاومشنگه(‪)۱‬‬                                          ‫نفته راگویند ‪.‬‬
                                                                                               ‫گر‬‫ج‬
 ‫است » وآن نوعی ازحبوب باشد که چون پوست‬                   ‫ديو کلوخ ‪ ۴‬کدلوخهای بزرکهرا‬
                ‫آلرا بکنند بعدس مقشر ماند ‪.‬‬                ‫گویند که در وقت شیار کردن از زمین بر خیزد‬
‫ديو فك ‪ -‬بر وزن ربوند ‪ ,‬هام داروبی‬                                                         ‫وبر اطراف ریزد‪.‬‬
                                     ‫است دوایي ‪.‬‬           ‫دگینودم" د بر وزن دیو مردم »‬
                                                           ‫نوعی از گندم است که هر دو دانه دريك علاف‬
‫وزن موه ‪ ۰‬کرم پبلة‬         ‫‪-‬ر‬
                            ‫دوه * ب‬
                                  ‫ب‬
                                 ‫گاوشد ‪.‬‬
                                       ‫ابرشم ر‬             ‫ند ‪.‬‬
                                                              ‫ونهیرا‬
                                                                   ‫گ‌دا‬
                                                                      ‫میباشد ؛ وبعضی خوش بزر که بی‬
 ‫‪-‬نابه ازاقالیم سبعه‬
                   ‫دیو هفت در ک‬                           ‫دلو گیر ‪ -‬باانی مجهول بروزن شیر‬
                                                           ‫کیره کسی را گوبند که او را گجرنفته باشد ‪-‬‬
 ‫درو هفت سر کنابه از شب است‬                                ‫‌یکه دبورا بگیرد ‪ -‬و نام شهری است در‬
                                                                                              ‫پکا‬
                                                           ‫ملك دکن " و درین زمان بدولت آباد شهرت‬

‫هم میشود ‪ -‬کور زمین را فگیفزته اند باعتبار‬                                                               ‫دارد ‪.‬‬
                       ‫هفت اقلیم وهفت طبقه ‪3.‬‬            ‫‪-‬رعی از قماش باشدکه‬
                                                                           ‫دیو گیری ن‬
                                                                 ‫در دب وگر میبافند که آن دوك آباد امت‬
 ‫دھو ل ‪ -‬بارال بثانی مجپول رسیده‬
                               ‫ی‬
‫وهای بواو کشده وبلام زده ‪ ۰‬بمعدی آخرداهول‬                  ‫دیو لاخ ‪ » ۴‬بالام بالفکشیده وبخای‬
                                                          ‫نقطه دار زده » جا ومقام دیو راگویند چه لاخ‬
‫ديهيم ‪- ۱‬بکس هابزوزن تعظیم »‬                              ‫بمعنی مان است همچو سنگه لاخ و رود لاخ‬
                       ‫هخصوص بادشاهان‬
                                    ‫اجى ک م‬                ‫وکلمةٌ لاخ بغیرازین سه موضم جای دبگرنيامده‬
                          ‫تخت‬     ‫ممعنی‬   ‫و‬   ‫‪77‬‬   ‫است‬
                                                          ‫و صبحرا وخارستالی‌را نگدوزبند که از‬             ‫است؟ ‏‬
                        ‫از‬                                 ‫آبادانی دور باشد ‪ -‬وجایگاه خراب و خرابه ‏‬
                                                          ‫وچراگاه دور را نیز گفته‌الد ‪ -‬وسردسیر را هم‬
         ‫دهم‬           ‫وبعضی کوبند دبهیم افسری‬
‫تیمن وتبر ك بربالای‬    ‫بوده که آ را درقد‪.‬یم سهت‬                                                       ‫میگونشد‪..‬‬
‫سرپادشاهان مویباخته‌اند کولاه مرصع را فيز‬                   ‫جن‬     ‫دڼو مر د" ‪ -.‬دراصطلاح مى‬
                                              ‫گوشد ‪.‬‬       ‫ومردم مفد ومفتن باشد ‪ -‬و لومی ازحیوان هم‬
                                                         ‫مشتگه)‪.‬‬    ‫کاو مغك س‬             ‫چش‪:‬‬   ‫((‬


  ‫از ‪ :‬دیو ‪ +‬لاخ ( يسولف‬                                 ‫رك ‪:‬‬                         ‫‪:‬‬    ‫رك‬    ‫‪8‬‬

          ‫اهرمن لاخ‪.‬‬    ‫لاخ ‪۰‬‬    ‫لام »کوج ‪ ۰ ۷‬حندولاج ‪3‬‬                    ‫نسر‬   ‫‪۴‬ك‬             ‫مکان ) ‪.‬‬
   ‫ءنبت وتصفیر) = دبوك د=بوچه‪ ,‬دراوراق مانوی بپارنی ‪8۷/4‬‬
                                                       ‫‪ :‬دیو‪( +‬‬                       ‫از‬         ‫‏‪e‬‬




                                ‫(کرم)‪ .‬درپهلوی ‪ 12۷6‬که خرفتری محوب شده (شابد ‪ :‬زالو) ‪.‬‬
         ‫‪Henning, A list of Middle‬‬                       ‫‪Persian...,‬‬   ‫‪BSOS , IX , 1,p.82, 90.‬‬
   ‫‪ ( 2۲۵1‬افر ) بادشاه ابران بسته میشد ف«رهنك‬                    ‫رکه‬
                                                                 ‫د‬    ‫اسلو لوار ا رشته "مخصوصاً بنو‬
                                                                   ‫کاری‬
                                                                   ‫نیگ‪-‬لیی ‪ .‬لبدل واسکات › ‪.‬‬
                                                                                           ‫اات‬
                                                                                             ‫پو‬
                                                     ‫* ده ‪ -‬بکرارل ‪.‬رك ‪ :‬ده (بکراول) ‪.‬‬
```


## [2026-09-05T20:13:48.762Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(286,300):\n    l=leaves[i]\n    if 'ابلیس' in l or 'ابلبس' in l:\n        print('=== leaf',i,'===')\n        print(l[:3500])\n        break\nelse:\n    hits=[i for i,l in enumerate(leaves) if 'ابلیس' in l]\n    print('hits',hits[:20])\nEOF",
 "description": "Find Eblis in Borhan vol1"
}
```


## [2026-09-05T20:13:49.272Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ leaf 65 (p.48) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==66' FVQ_pages.txt | head -50",
 "description": "Print Jeffery p.48"
}
```


### [2026-09-05T20:13:51.476Z] TOOL RESULT

```
=== leaf 293 ===
پوت
ابنکاد ‏ بر وت شب کون گفق
وزراعت را گونند .
ال - بنتح اول و ضم انی وسکون لام.
دوابی است که بشیرازی «بل شیرین» گوند و
طرائیث و طرئوث همانست ؛ و از جملهٌ قابضات
باشد و عنم خون رفتن از بینی و مقعد و جمیع
اضا کند - و مکر انی فاقل صفار است که
آنرا «هیل» کومند و در طمام کنند ۱ . *
الق ایام یکی قاف » کنایه‌از
دنیا و روز کار است باعتبار روز و شب .
الق چرخ » بنتح جم . کناب‌ازب
و روز است - و کنایه از روز کارهم هست .
ابلاك ه بنتح اول و لام و سکون انی
و کاف فارسی هر چیز دورنگه را کویند عموعا
وسیاء وسفید را خصوصاً - وابلق معرب آنست ۴
- وبکر انی و سکون تاكث و رایع شراره
(۱) چب؟ : - است. خم۳ : کقته‌اند.
ابوخذا
آش‌را کونند ۴ . وباین معنی بفتح اول و ثانی
وثاك هم آمده است ۴ .
۲ طوج 9 ت‌ بروزن محلوح, قندسفدرا
گویند - و بعضی شکر سفید و قند سوده را
ابلوح کفته اند ؛ و باجیم فارسی هم درست
است (۱).
ا لوگ - بر وزن مقلوك » مردم متافق
و دورنگگ - و فضول را گوبند . #
ابناخون « با نون و خای نقطه دار
و واو مجهول بر وزن افلاطون , قلعه و حصار
وجای عتکي رآ گویده »و یتست چم اون
بی‌ثانی ۷ هم بنظی آمدم است (۲) .
ابو خدا ۷ - با خای قطه داد و
لام و سین بی نقطه بر وزن آبو دردا » دوابی است
که اورا ۳ شنار خوانند ُ ب رگ آن سیاه
بسرخی‌هایل می‌باشد . اکریاشراب خورندشکم‌را
(۷) خم۳ : - است. (۳) خم۳: آنرا.
۴ رك : « علیقات توروزنامه ۱۱ ».
طبری 021 (نعله) « واژه نامه ۱۲۷ ».
۵ - معرب آبلوج فارسی :
نت عطار ای‌جوان ابلوج من هست نیکویی‌تکلف » بی‌سخن
مننوی . ۱ لفت نامه » .
٩‏ - نی انباخون ؛ ودرنسخه ای ازفرهنکه اسدی : انباجون
دلفت نامه . .  .‏ ۷ - مصحف انضا و اتخوسا < لخت‌ناحه ». ابلك و دانةٌ آن
* بلق - ابلق نوعی اسب است برنگه ابلك :« اسب ابلق ناستوده است ونيك خود کم
بود .» « قابوسنامه » رك : نوروزنامه س ۵۳ : ۱۵ و۱۱ -۱۱۱ .و رل : ابلك .
۵ ابلیس - این‌درید نوخته : « اکر ابلسی عربی باشد اشتفاق‌آن از ابلس یبلی بمعنی
سانقی خن کده وین ای ازارشت دا سای انت» متهناوعر ایح مه را مولتات دقن
آورده . ابلیس ا زکلمةٌ بونانی 121۵00105 بمعنی کذاب ونمام که از نامهای شیطان است گرفته
شده «نفی * « جفری ۸-6۷ *. ای - ازعربی « این» بمعنی پسرء درآشوری بابلی
۷ , عری 067 , آرامی 0۲2 . در لغات جنوب الجزیره وحبشه 960 « و لفنسون ۲۸۳*.
```


### [2026-09-05T20:13:53.305Z] TOOL RESULT

```
=== FVQ leaf 65 (p.48) ===
48 FOREIGN VOCABULARY OP THE QUR J AN
more than " the adversary ", and particularly in the ecclesiastical
writers he becomes the chief of the hosts of evil. It is in this sense that
xli I appears in the Qur'an, so we are doubly justified in looking
for a Christian origin for the word.
One theory is that it came through the Syriac, the * being taken
as the genitive particle, 1 a phenomenon for which there are perhaps
other examples, e.g. mi^j for 8ia<f)covd? (ZA, xxiv, 51), ^uJ for
SiKaarri? (ZDMG, 1, 620)\ jUa? j for 8v<rVTpLa(tivyrr,ZweiGedichte,
i, 119 n.). The difficulty is that the normal translation of 6
is ] t rO^s), the accuser or calumniator, both in the Peshitta (cf. Matt, iv)
and in the ecclesiastical literature. There is a form *QDQ^jO, a trans-
literation of &a/3oAoy, but PSw, 874, quotes this only as a dictionary
word from BB. There is apparently no occurrence of the word in the
old Arabic literature, 2 so it was possibly a word introduced by
Muhammad himself. If we could assume that some such form as
.fnnV^>>% W as colloquially used among the Aramaic-speaking Christians
with whom Muhammad came in contact, the above explanation might
hold, though one would have to assume that the j had been dropped
by his informants. The alternative is that it came into Arabic directly
from the Greek, and was used by the Arabic-speaking Christians
associated with the Byzantine Church. 3
Grimme, ZA, xxvi, 164, suggested that it might have come from
8. Arabia, perhaps influenced by the Eth. -^-flA-ft. This, however,
is apparently a rare word in Eth., the usual translation for &a/3oAoy
being rt/8/TJ, though sometimes PV} is used (James iv, 7 ; 1 Pet. v,
8, etc.). Moreover, even if there were anything in Grimme's theory
that this was the form that crossed over into Arabia, his further
supposition that the ^jf was taken to bo the S. Arabian H --- (* w
very far fetched.
1 So Horovitz, A'6 T , 87. Mingana, Syriac Influence, 89, thinks rather that it
was the fault of some early scribe or copyist who mistook the initial Dal for an Alif.
2 The verses in Ibn Hisham, 318 and 516, noted by Horovitz, are from the period
of the Hijra and so doubtless influenced by Muhammad's usage. They would seem
fatal, however, to Mingana's theory.
3 Kiinstlinger, " Die Herkunft des Wortes Iblia im Kuran," in Rocznik Orjen-
tolistyczny, vi (1928), proposes the somewhat far-fetched theory that Iblis is derived
from the Jewish Belial by deliberate transformation.
```


## [2026-09-05T20:14:09.027Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD entry ~145 ===\"; grep -n \"^ *145 \\|^145 \" SOD.txt | head; echo \"--- page 145 => leaf 211\"; awk 'BEGIN{RS=\"\\f\"} NR==212' SOD_pages.txt | head -40",
 "description": "Check Gharib Sogdian 145"
}
```


### [2026-09-05T20:14:10.751Z] TOOL RESULT

```
=== SOD entry ~145 ===
8486:145  »qwc-   M  cr*iJ 
31753:145 
--- page 145 => leaf 211
                                                                                                     ■■■■Ml


 6wy5r                                                                                                                  146


 3684 6wr5r       S                                   j^>           tail
         5uydar (SwYth) ©ob. -yh =»8Ywt-(h),                        BBB f8; VJ 1419; MSP p45 bl41, 159-60,
           5wYtrt(h), 8wx8r
                                                                      dwmpy, bill
         daughter                                              3697 Swmph B, S =* 8wm
         Anc. Lett. 3a 1.27
                                                               3698 8wn      M =* 5n, 8>wn
 3685 6\YYtC,) M                    <u>*>^jj)>^                3699 8wnplk B                            -u*,fi
      5uYd(a) (8wxth, dwYt(,)) ©f. n. =»SYwt-(h)                    8um/nb/pc (8wnpy) ©Pahl. dumbag =»5wm
      daughter                                                      tail
      BBB c22; Tales. 472.38; GMS 421, 940, 1170; C2,               SCE120 140; MSP bl80; EGSii 94; Bailey. Prolexis.
          26R8; SwYtK VJ 1009, 1135, 1485; TSP 2.150;
          Hen. JRAS 1944, 137.7; EGSii
                                                              3700 5wnpy S ** 8wnpJk
3686 dwYtc,) C ==» 8wyi(,)                                    3701 dwr C                                     o~ojj^<jjj
3687 6wYth -* 8wYSr                                                 Sur
                                                                    far    ©ob. -y =*8wr(h), 8wrtr
3688 6wYtrt(h)       M                              jl^*
                                                                   STi 52.5, 81.15; STii 3.17; BSTi 178-9; C2 gloss.
      6uYdart ©ob. pi. -fy =*8wYSr, 8wYt(>)
      daughters                                               3702 dwrVy C                                        ^^
      Hen. Talcs. 486, 6, 7, 10; GMS 1231                           8urawc =>dwr
                                                                    distance
3689 5wk} B                                  Uwot^
                                                                    BSTii905, 2;C2, 57V2, 61V16
     8oka, loka
       ~*rwk    ©Skt. loka ©nom. ->; ob. -y(h)
                                                              3703 5wr(h)      B, M, S        (u>> >^~* ^)^~~^j>> o>>
      world
                                                                    8ur    ©Av. OP dura ©ob. -y(h) =»dwr
      SCE; BSTBL, Dhu. 161; TSP 2.576, 8.85; SwkK                   far
          Frag. Len. 32.11; dwkyh Dhy. 399                          GMS 353; VJ; BSTBL; TSP 13.28 etc.; SCE 50, 96,

3690 5wk} pr6wk> B                                                    333; Frag. Lcn. 44.7, 92, 16; Talcs. 481, 46;
```


## [2026-09-05T20:14:18.039Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *[0-9]\\{3,4\\} 5w\\b\\|^ *[0-9]\\{3,4\\} 5w[\\\"'‚]\" SOD.txt | head -20; echo ---; grep -n -B2 -A6 \"^ *two$\" SOD.txt | head -60",
 "description": "Search Gharib for Sogdian two"
}
```


### [2026-09-05T20:15:28.280Z] TOOL RESULT

```
---
```


## [2026-09-05T20:15:32.659Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"two$\\|two \" SOD.txt | grep -i \"5w\\|dw\\|8w\" | head -20; echo \"=== leaf 210-212 headers\"; python3 - <<'EOF'\nleaves=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'\\bdw\\b|\\b8w\\b', l) and ' two' in l:\n        print(i, i-66)\nEOF",
 "description": "Find Sogdian two entry"
}
```


### [2026-09-05T20:15:34.663Z] TOOL RESULT

```
=== leaf 210-212 headers
90 24
210 144
```


## [2026-09-05T20:15:37.824Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nl=leaves[210]\nfor m in re.finditer(r' two', l):\n    print(repr(l[max(0,m.start()-500):m.start()+200]))\n    print('-----')\nEOF",
 "description": "Print Sogdian two context"
}
```


### [2026-09-05T20:15:39.897Z] TOOL RESULT

```
' 512; GMS 1186; Frag. Len. 120, 5; MSP\n 3661 SstNvch       M, S                            Jljb<j»\n                                                                        b32, 101 elO\n        5(a)/i/ostauc ©<*dusta-wauc(=dustaw(an)+auc)\n          =»5stwc, 6ystwc                                       3673 5w> B,M                            (u>=* >=■** >>)j*\n        poverty                                                      5wa\n                                                                     two (dw>) ©<*d(u)wa ^^             5yP-, SyPty-\n        GMS 119, 1080; KG 336; W-Lii: Gropp. 38; BBB\n          633                                                         EGSii 139; GMS 501, 1316, 13'
-----
'9; ace. dwy, C2, 6V 13\n3662 8st)wcy B                                     jlyU*^\n     6ostauce/i ?\n                                                                3674 dw> =* 6w>\n                                                                3675 dw*psynty C                         j^^-Ji- <t>r^>>\n        poor 2a.7\n        Frag.                                                        dwa-pasynt/de\n                                                                      bisected, halvedidivided into two parts)\n3663 6st>y B                   :              <^u\n     5iste (5st-) ©*dista; fdais- ©pp. ^Systk                         C2,22V12, 66V 10 n p59, 11-12\n     built\n                           '
-----
"st>y B                   :              <^u\n     5iste (5st-) ©*dista; fdais- ©pp. ^Systk                         C2,22V12, 66V 10 n p59, 11-12\n     built\n                                                                3676 8wa-puxay\n                                                                     dw* pwx'y C                                    o^vj->\n        VJ 14b; dsty, Sund. AI 28, 1988 pl8l\n                                                                     bisected, halvcdidivided into two parts)\n3664 Sstw'n B, M                                    jlyli*^\n                                                                     Sund. AoFiii 1975 p65, 22 p67 n50\n     5(a)stwan (dstw'n) ©"
-----
"'n B, M                                    jlyli*^\n                                                                     Sund. AoFiii 1975 p65, 22 p67 n50\n     5(a)stwan (dstw'n) ©*dus-tuwdn            ©pi. -(•, ob.\n         pi. ~ty =>cstw>n, dystw*n                              3677 dw'ryt C                            \\jj>> *^ia-*r ^\n                                                                     6wa-ret\n       poor\n       W-Lii; Frag.2a.12.21; VJ 49, 51, 77, 122; TSP                 having two faces\n         2.1178, 12.21; BSTBL, Intox. 10; Tales. 486.23;             Sund. AI 1988, 181\n         BSTii 885.3, 894.18; C2, 51V 6, 54R 18, 51R3,          3678 Sw'sp'rm'k     C                "
-----
"   6wa-ret\n       poor\n       W-Lii; Frag.2a.12.21; VJ 49, 51, 77, 122; TSP                 having two faces\n         2.1178, 12.21; BSTBL, Intox. 10; Tales. 486.23;             Sund. AI 1988, 181\n         BSTii 885.3, 894.18; C2, 51V 6, 54R 18, 51R3,          3678 Sw'sp'rm'k     C                     ^j;*^^\n         105V 6\n                                                                     5wa-sfarme ^sp^rntfk\n3665 dstw^      C => Sstw>n                                          bisexuaK/iavzng two kinds of pudenda)\n                                                                     SCE 356\n3666 Sstwc S                                       is>Jj~>*j*\n     6ostauc (dstwc) ^Sst'wch         "
-----
'ik\n       Sats/c-roc  =»5scy(y), 5yscy(y)                               twenty-second\n       eighth and fifteenth and twenty third day of                  C2, 56R2\n         the month\n                                                                3683 dw^ng\'n  M                                      ^\n                                                                     5wa-zangan\n       MDii P120, mzySts "fifteenth day"; Hen.\n         Orientalia. 8, 95                                           of two kinds\n3671 5tw =» 8t-                                                      BBB 525\n'
-----
```


## [2026-09-05T20:15:49.642Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in بسکویت دوجین دیپلم دیپلمات دیابت دیالیز دیافراگم دیهیم; do echo \"== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null; done",
 "description": "Grep Mo'in files for loanwords"
}
```


### [2026-09-05T20:15:51.589Z] TOOL RESULT

```
== بسکویت
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
== دوجین
MON_part1.txt:1
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
== دیپلم
MON_part2.txt:1
MON_part1.txt:5
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1
incoming/MON/MON_2vol_Adena_v1_djvu.txt:5
== دیپلمات
MON_part2.txt:0
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part1.txt:1
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
== دیابت
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
MON_part1.txt:1
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
== دیالیز
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
== دیافراگم
MON_part1.txt:3
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1
MON_part2.txt:1
== دیهیم
MON_part1.txt:5
MON_part2.txt:4
incoming/MON/MON_2vol_Adena_v1_djvu.txt:5
incoming/MON/MON_2vol_Adena_v2_djvu.txt:4
```


## [2026-09-05T20:15:54.478Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in دوجین دیپلمات دیابت دیافراگم دیهیم; do echo \"===== $w\"; grep -o \".\\{160\\}$w.\\{200\\}\" MON_part1.txt | head -3; done",
 "description": "Show Mo'in contexts"
}
```


### [2026-09-05T20:15:56.279Z] TOOL RESULT

```
===== دوجین
===== دیپلمات
===== دیابت
===== دیافراگم
===== دیهیم
```


## [2026-09-05T20:15:59.816Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor w in ['دوجین','دیپلمات','دیپلم','دیابت','دیافراگم','دیهیم']:\n    print('=====',w)\n    for m in list(re.finditer(re.escape(w),t))[:3]:\n        print(repr(t[max(0,m.start()-250):m.start()+250]))\nEOF",
 "description": "Show Mo'in contexts via python"
}
```


### [2026-09-05T20:16:01.610Z] TOOL RESULT

```
===== دوجین
'.) (مست.) نوعی \nتار که دارای دو تار (سیم) است؛. \n\nدو تخمه: (0-)0-۱02052 (ص\u200cمر.) هر باه \nو جانور که از دو جنس مختلف بوجود آمده \nباشد. مولودی که پدر او سیاه و مادرش \nسفید باشد با بعکس ؛ دو تبره. حرامزاده» \nخشوک. \n\nدونهی: ار (ص\u200cمر .) لاس آستر \nشلد ۵. \n\nدوجین: 11 (ق\u200cمر.) دوازده عدد از مک \nشیم » ستهٌ دوارده تایی. \n\nدوچرحه: (0-)10-272 (امر .) دستگاهی \nاز وسایل نقلیه که با چرخ\u200cهای دندانه\u200cدار به \nوسبلةٌ گردش زنجری به حرکت آید. \nدوجندان: 62001-0-.010 (ق\u200cمر.) دو برانر» \nدوحورلقا: 10.0۸ آف. ع.] (کد.) \nعقل '
===== دیپلمات
'است. دیب حسروی: جامه \nحریر ادشاهی. (اخ.) گنج سیم از گنج\u200cهای \nسر قرو گنج دیبه. \n\nد\u200c یپلم: ههام۵ (.) گواهی\u200cنامه (تحصیلی). \nپروانه. \n\nدییلمات: 0۱ (ص مر . آمر .) آنکه از \nامور سیاسی مطلع است؛ سیاستمدار» سائس. \n\n\nدییلماتیک: 10100121-۳ (ص\u200cمر.) مر بو ط \nبه دیپلمات؛ سیاسی. هیشثت دییلماتیک: \nمجموع نمایندگان دول خارجه در پایتخت \nیک کشور. \n\nپپلماسی : 01010751 (امر.) مسجموعه \nقواعدی که از روابط بين دول بحث کند؛ \nدیپلمه: 6 (ص مر .) آنکه دارای \nدیپلم است؛ دارندةٌ گواهینامه. \nدیجور:. و [ع.] (ص.) ساه» تاریک \n(م'
===== دیپلم
'ه\u200cنامچه: (م-)مک- 050 [ع. ف.] \n(امر. مسصف.) چک و سند و قبالهً اجارهة \nملکی يا کالایی؛ اجاره\u200cنامه. \n\nاحاره: (-)6222 [- اجازت. ع. اجازة] \n(مصعم.) دستوری دادن» روا داشتن» \nرخصت دادن. صله و جایزه دادن به کسی. \n(امص.) دستوری» اذن» رخصت. (.) کتیبه؛ \nتقریر» دیپلم. (ف.) گواهیی که در میان اهل \nسنت عالمی به کسی دهد در روابت از او. \nگواهیی که در میان امامیه عالمی دهد به کسی \nکه او صلاحیت فتوی دارد. (حق.) تنفی \nکردن عقدی که بطور فضولی انجام یافته» به \nوسیلةٌ شخصی که عقد ف ضولی مربوط به \nشخص با مال او بوده اس'
'است. دیب حسروی: جامه \nحریر ادشاهی. (اخ.) گنج سیم از گنج\u200cهای \nسر قرو گنج دیبه. \n\nد\u200c یپلم: ههام۵ (.) گواهی\u200cنامه (تحصیلی). \nپروانه. \n\nدییلمات: 0۱ (ص مر . آمر .) آنکه از \nامور سیاسی مطلع است؛ سیاستمدار» سائس. \n\n\nدییلماتیک: 10100121-۳ (ص\u200cمر.) مر بو ط \nبه دیپلمات؛ سیاسی. هیشثت دییلماتیک: \nمجموع نمایندگان دول خارجه در پایتخت \nیک کشور. \n\nپپلماسی : 01010751 (امر.) مسجموعه \nقواعدی که از روابط بين دول بحث کند؛ \nدیپلمه: 6 (ص مر .) آنکه دارای \nدیپلم است؛ دارندةٌ گواهینامه. \nدیجور:. و [ع.] (ص.) ساه» تاریک \n(م'
' .) آنکه از \nامور سیاسی مطلع است؛ سیاستمدار» سائس. \n\n\nدییلماتیک: 10100121-۳ (ص\u200cمر.) مر بو ط \nبه دیپلمات؛ سیاسی. هیشثت دییلماتیک: \nمجموع نمایندگان دول خارجه در پایتخت \nیک کشور. \n\nپپلماسی : 01010751 (امر.) مسجموعه \nقواعدی که از روابط بين دول بحث کند؛ \nدیپلمه: 6 (ص مر .) آنکه دارای \nدیپلم است؛ دارندةٌ گواهینامه. \nدیجور:. و [ع.] (ص.) ساه» تاریک \n(مداده شب). \nدید: ٩34\u200f (مص\u200cخم.) دیدن» ریت کردن. \n() بینایی (قسوه)» ن_ظر. حاصل دیدن. \nدیدوبازدید: ملاقات خویشان و دوستان \nیکدیگر را. \nدیدار: 01427 ((مص.) دید'
===== دیابت
' بد ین با رد ی دین» \nکو رف ضح.گاهی نیز «دی» را «د سن») \nگفته\u200cاند و «دین بآذر, از اینروست ولی \n\n\nقدیم داده\u200cمی\u200cشد.) \n1 02۷ (عد. کسری) یکث جزو از \n\n\nترجمه صحیح است. 02015 «ردی» است و \n«دین» نحر بف است؛. \n\nدی: آ (ق.) روزگسذشته» دبروز. شب \nگذشته» دشبت. \n\nدیابت: »ره (.) (بز.) مرضی که به \nسبب ازدیاد مقدار خون تولید گردد) \nدیار: ۹۲ [ع. باشنده] (.) کسی» کسی. \nدباری. احدی. \n\nدیار: 13:۳5 [ع.] (ص. ۱.) دیرنشین» ساکن \nدیر و صومعه. \n\nدیار: ۲ (ع.] () ج. دار. خانه\u200cها» مسا کن. \nشهر» مدینه. سرزمین." \n\n\nدیافراگم فر'
===== دیافراگم
'ه» دشبت. \n\nدیابت: »ره (.) (بز.) مرضی که به \nسبب ازدیاد مقدار خون تولید گردد) \nدیار: ۹۲ [ع. باشنده] (.) کسی» کسی. \nدباری. احدی. \n\nدیار: 13:۳5 [ع.] (ص. ۱.) دیرنشین» ساکن \nدیر و صومعه. \n\nدیار: ۲ (ع.] () ج. دار. خانه\u200cها» مسا کن. \nشهر» مدینه. سرزمین." \n\n\nدیافراگم فرهنگ فارسی معین ۷۹ \n\n\nدیافرا گم: مود ره (۰.) (عک.) سوراخ \nجلو دوربین عکاسی که نسبت به کمی یا \nزیادی نور» آن را تنگ و کشاد می\u200cکنند. \n(بز.) حجاب حاجز. \n\nدیالکتیک: جدل» روش \nمحادله منطقی. مناظر ه. منطق مکتب کارل \nما کس. \n\nدبالمه: (0-) 1221622 '
'ربه \nتنفس می\u200cکنند و آن عبارت از دو توده \nاسفنجی قابل ارتجاع است که در قفس سینه \nجای دار ند. رنگ آنها در اشخاص مسن \nخاکستری و در جوانان و اطفال گلی رنگ \n\n\n.۹۴ فرهنگ فارسی معیر شش انداز \n\n\nاست. هر شش به شکل هرمی است که در \nرأآسش در بالا و قاعده\u200cاش روی دیافراگم \nقرار کرفته» وزنش در مردها ۱۲۰۰ و در \nرن\u200cها ۰ ۰ کرم است. شش راست بزر کتر \nاز شش چپ است و در سطح خارجیش دو \nشیار دیده می\u200cشود که به سه قطعه تقسیم \nمی\u200cگردد ولی شش چپ دارای یک شیار و \nناحیةٌ مقعری دارد که قلب در آن جای \nمی\u200cگیرد. شش\u200cها از عقب به '
'رم است. شش راست بزر کتر \nاز شش چپ است و در سطح خارجیش دو \nشیار دیده می\u200cشود که به سه قطعه تقسیم \nمی\u200cگردد ولی شش چپ دارای یک شیار و \nناحیةٌ مقعری دارد که قلب در آن جای \nمی\u200cگیرد. شش\u200cها از عقب به ستون مهره\u200cها و \nاز جلو و پهلوها به دنده\u200cها و از پایین به \nدیافراگم محد\u200cود می\u200cشو ند؛ ر به» جگر سقك. \nشش \u200cانداز: (فد. 37:422)664 [- \nشش\u200cاندازه] (ص\u200cفا.) کسی که شش بجول \nبازی کند. کسی که نرد بازد» نراد. کسی که \nششگوی الوان مدور از چوب یا غیر آن به \nهر دو دست بگیرد و بر هر دستی سه عدد؛ \nدر هوا اندازد و کیرد بطور'
===== دیهیم
'ش و انا اون \nافسائه؛ (6-)215372 [- فسانه - آفسانه] (ا.) \nسرگذشت قصه داستان. مثل (سایر) \nافستتایندن: 252-17 [- فس\u200cاییدن] \n(مص\u200cم.) رام کردن (جانوران). جادو کردن؛ \nسحر کردن. \n\nافسد: 0۱ [ع.] (ص تسفضد.) تسباه\u200cتر) \nفاسد تر» تبه کار تر. \n\nافسر: ۲م (.) تأج» دیهیم» کلاه بادشاهی. \nافسر: ۲ (.) (نط.) کسی که در نظام \nدارای درجه باشد؛ صاحیمنصب. ضمح. \nفرهنگستان این کلمه را به معنی فوق از انگٌ. \n7 فر. ۲عزمز1]ه 13 فته! \n\nافسسر و 2150702)6(8-1 (حامص.) \nپژمردگی. اندوهگینی. انجماد. دلسردی. \nافسر دن: ۵507-127 [فسردن'
'لمخرج را از قبیل وب پم و رک - گم با \nهم قافیه کنند» مثلا از ۱ \nقافه و سک و شکد. \n\n\nاکل: ۵8 [ع.] (مصم.) خوردن» (.) خور. \n\n\nاکل از قفا: (مج.) کاری از غیر طریق اصلی \nو متعارف انجام دادن. \n\nاکلیل: (ع.] (ا.) تاج» افسر دسهيم. \nسر بند؛ ج . اکالیل. ۰ (گیا.) دیهیم. (نق.) گردی \nاست ِ ره رنگ\u200cهای طلابی» نقر ه\u200cای» \nسبز و غیره. \n\nاکمال: اقست [ع.] (مصم.) کامل کردن؛ \nتمام نمودن» رسانیدن: اکمال نفوس؛ ج. \nاکمالات. \n\nاکمل: 21 [ع.] (ص\u200cتفض.) تمامتر» \nکاملتر» رسیده\u200cتر» رساتر. به نحو اکمل: به \nطریق کاملتر» به نحو اتم '
'زی: 21-12 (امر.) (گیاء) گیاهی \nاست از تبرة بادنجانیان که علفی است و \nبعض گونه\u200cهایش بصورت درختچه\u200cاند. \nبرگ\u200cهای آن پهن و گل\u200cهایش منظم و گل \nآذینش گرزن است. میوه\u200cاش سته می\u200cباشد؛ \nانگور روباه» عنب\u200cالعلب. \nتاج\u200cگذاری: آ2022۲-1-.۱ [معر. ف.] \n9 آیین | نهادن دیهیم بر سر بادشاهی \nنوء جشن تاج گذاردن پادشاهان؛ تتویج» \nتاجور: ۱-57 (ص\u200cمر.) دارای تاج با افسر. \nبادشاه» سلطان. \n\nتاجیک: :211 [- تاجک > تازیک (به \nیک معنی) - تاژیک» تر. تات. (رعیت) + \nچیک (پس. تصغیر و تحقیر)] غیر ترک \n(عموماٌ)» آنکه ترک و مغولی نباش'
```


## [2026-09-05T20:16:08.459Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:16:08.467Z] TOOL RESULT

```


```


## [2026-09-05T20:16:11.000Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/ARY/ARY_latin_index_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nfor w in ['DWO','DUWO','DVO']:\n    for m in list(re.finditer(w,t))[:4]:\n        print(w, repr(t[max(0,m.start()-200):m.start()+300]))\nEOF",
 "description": "Search Aryanpur index for DWO"
}
```


### [2026-09-05T20:16:13.015Z] TOOL RESULT

```
DWO 'LITHUANIAN) gl CUATRO SPANISH) «lial ;\nCHETRI LATVIAN) (3) QaTTRO AUTALIAN gilla) 4"\nHOLD IRISH) gS 53 3) PATRU Tdleomatiany gs,\nCHETHAIR, CETHIR QUATRO PORTUGUESE) Sis\nPETOR, PEDWAR —x(GAULISH) JS FIDWOR GOTHIC) S55\nPETGUAR, PEDWAR (WELSH) 5) OLD SCANDINAVIAN) 4S 5-4!\nPEVAR ABRETON) ig FIJORIR\nFIJORIR s(OLD NORSE) 9S 355\nFIUWAR {OLD SAXON) oS gp-S\n\x0c[pdf page 229]\nte |\n‘ONIONS: (FOUR) 373 ‘REFERENCES onthe\nSKEAT: (FOUR) 224 POKORNY. Te oan\nAMINDAROY: my 1. OUR) 227 BARNHART: (FOUR) 404\noid avr s'
DWO 'ERTIG (DUTCH) ,s.cle CUARENTA (SPANISH) lily!\nCZERDZIESCI POLISH) Slomg) QUARANTA AITALIAN) pissy)\nCHTYRICET (CZECH) Se PATRUZECI —-(RUMANIAN) lay,\nSHTYRIDSAT (SLOVAK) Shel QUARENTA (PORTUGUESE) Jt\nFIDWOR, TIGJUS (GOTHIC) eS\nREFERENCES both (OLD SCANDINAVIAN) pS (5h!\nPOKORNY =—~SS~S*~*~*~*«S FJORIR TIGIR\nBARNHART: (FORTY) 403 FJORIR TIGIR(OLD NORSE) 45 555\nMACKENZIE: (FORTY) 115 HOLD SAXON) ofS gi pS te\nONIONS: (FORTY) 372 FIWARTIG, FIARTIG\nSKEAT: (FORTY) 223 OLD FRISIAN) oS 52.3\nave ieGoby FEUW'
DWO ' DU KURDISH) 535\nTvo NORWEGIAN) «5335 DU ABALUCHI) x gh\nTWEE (DUTCH) gale DVA :(AFGHANI) (y~%,) itil\nHOLD CHURCH SLAVIC) 4 (51 ‘WU, WE -(TOKHARIAN A) A 5 os\nDUVA, DIVE wi i (TOKHARIAN B) B 5 \\n5\nDWA, DWOJKA (POLISH) gleng) DVAU, DVA (SANSKRIT) cy Sie\nDVA, DVE (RUSSIAN) 5 ERKU ARMENIAN) «gs!\n| DVA, DVE CZECH) Sey DUO, D¥o (GREEK) gli\nDVA, DVEI- SLOVAK) jel DUO, DUAE LATIN) op3V\nDU, DVI LITHUANIAN) gly} DEUX (FRENCH) Wil\nDAU, DO =——(OLD IRISH) 5 543.,! Dos SPANISH) glilyel\nDOU, DWY (GAULISH) JF DU'
DWO 'DREDS OF PERSIAN\nFORDS WITH KNOWN PAHLAVI OR AVESTAN COGNATES OR ROOTS. SOME OF\n‘THESE ARE PROBABLY INDO-EUROPEAN; MANY ARE PROBABLY NOT. _\n2- WHERE POSSIBLE, 1 HAVE GIVEN COGNATES OF EACH PERSIAN HEADWORDL\nN KURDISH, AFGHANI, BALUCHI AND OTHER IRANIAN LANGUAGES, 4\n3- TO DEMONSTRATE THE KINSHIP OF OTHER INDO-EUROPEAN LANGUAGES, I , .\niAVE GIVEN AS MANY ,COGNATES IN SANSKRIT, GREEK, LATIN, GERMAN,\nINGLISH, RUSSIAN, ETC, AS POSSIBLE.\n"4 MUCH OF WHAT Is PRESENTED IN THIS BOOK HAS BEEN GLEANED FROM\n'
DUWO 'EUVE (FRENCH) «il\nFEDB HOLD IRISH) oS 54) 2 VIUDA SPANISH) g\\i\\yal\nGWEDDW (WELSH) 535 VEDOVA ITALIAN) gids)\nVADUVA H(RUMANIAN) gles\nREFERENCES beth, VIUVA (PORTUGUESE) Jas »\nPOKORNY. —SSS*~«dRT LID wIDUWO AGOTHIC) S36\nBARNHART: (WIDOW) 1235 {OLD HIGH GERMAN) oS glT\nDELAMARRE: (EUVE) 43 WITUWA i\nMACKENZIE: , (WIDOW) 140 WITWE GERMAN) glT :\nBUCK: 131 WIDEWE (OLD ENGLISH) oS pK! i\nONIONS: (WIDOW) 1006 wiIDOW ENGLISH) edt i\nSKEAT: (WIDOW) 7/5 WEDUWE, WEEUW = (DUTCH) «sala H\nrer ‘gb oly OLD CHURCH SL'
```


## [2026-09-05T20:16:18.457Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'DU KURDISH', t)\ns=t.rfind('[pdf page', 0, m.start()); \nprint(t[s-2500:m.start()+1500])\nEOF",
 "description": "Print Aryanpur TWO entry"
}
```


### [2026-09-05T20:16:20.284Z] TOOL RESULT

```
KA 24S gllT YDOK iS
|
|
|
OLD HIGH GERMAN) of gilt DAM, DAMISHN — (PAHLAVI) 15 he
DAMPH DIMIN, DUMUN —-(OSSETIC) gus)
| DAMPF (GERMAN) iT DEM ARURDISH) 52,5
i *DAMP — (OLD ENGLISH) 5 pul) DAM BALUCHI) gz yh
DAMP, DANK (ENGLISH) 55S! SANSKRIT) <p Suile
DYNG, DAMP DANISH) Sail DHAM., DHAMITI
DUNKEN (SWEDISH) 55 yo OLD SCANDINAVIAN) 46 ghey!
| DUNKEN NORWEGIAN) 53,5 DUMBA
eS
[pdf page 282]
TAY | (Coan 5 9G O95 si" 9 DAMS ni” pF 4) Odes
REFERENCES beth DOMPIG DUTCH) sacha
POKORNY, = ——SO™S~*~S~S~S~«B DUMPIU LITHUANIAN) ge
BARNHART: (DAMP) 250 DANGA LATVIAN) (3) gi)
‘MACKENZIE: (BREATH) 105 DUMSLE (OLD PRUSSIAN) 5 e3.4
SKEAT:
(DAMP) 153, (DUMPS) 185
Ave eb ob,
lentlaol
deka ty UY
AC ets” 2 He) a9 JS pL” ob "ba" oly -Y
p53 299 eaghy Ob ey} GUL; 52 oN) on! PET
Sy Sd eS bel 2 3s cal
DIMMIG ADANISH) S\asi3 DAMIDAN, DAFTAN :(PAHLAV2) 5 shy
DAAM (NORWEGIAN) «63,3 DUMUN, DIMIN ——(OSSETIC) 31
OLD CHURCH SLAVIC) 345 5941 DEM- s (KURDISH) 52,5
DUMO, DOTI (SANSKRIT) 2 Sule
DUMIU, DUMTI (LITHUANIAN) (gi -5 DHAMATI, DHAMYATE, DHMAYATE
DEIM, DEM (OLD IRISH) oS 53) THEMEROS GREEK) gli
DANKUISH (HITTITE) cx HOLD SCANDINAVIAN) 46 chu!
DAMR, DIMMR .
‘REFERENCES bncathay (OLD FRISIAN) ‘epS 5353 ah
POKORNY = SSOS*~*~*~«ST DIUNK, DIMM”:
BARNHART: (DIM) 279 OLD HIGH GERMAN) pS glJT
MACKENZIE: (BREATHE) 105 ‘TIMBER, TUNKAL
ONIONS: (DIM) 268 DUNKEL (GERMAN) glsT
SKEAT: (DIM) 170 DIMM — (OLD ENGLISH) of gS
MS ‘; cbt dby DIM ENGLISH) 5u3&3\
[pdf page 283]
uv
ewtlosb
. py eS il-
ye sere OTs li gliy U5 09 Sls ot pe
ae Sj ond gla aah 5 9) Sea sobs 2 Sls ot
ZAHN (GERMAN) gait DANTA, DANTAN  (AVESTAN) os!
TOTH — (OLD ENGLISH) 1S) DANTAN (OLD PERSIAN) deol, e+
TOOTH ENGLISH) gaSi\ DAD, DANDAN (PAHLAVI) shay
TAND DANISH) jails DANDAG (OSSETIC) gos!
TAND SWEDISH) ity DIDAN, DINDAN (KURDISH) 52,8
TAND NORWEGIAN) 5333 DANTAN, DATAN — (BALUCHD) ge gh
TAND DUTCH) ta DAN, SANSKRIT) 2 Sila
DZIEGNA (POLISH) iting) DANT-, DANTAM, DATAS, DANTA
DANTIS (LITHUANIAN) gz) ATAMN ARMENIAN) «+,
DET OLD IRISH) [35 545 p! GREEK) iy
DANT (WELSH) 59 ODON, ODOUS, ODONTOS
DANT ABRETON) 53.4 DENS, DENTIS LATIN) 3
DENT FRENCH) si
‘REFERENCES beth DIENTE SPANISH) gps!
POKORNY SOSCS~*~S*~«S DENTE ITALIAN) ,p\s'e\
BARNHART: (TOOTH) 1150 DINTE (RUMANIAN) ges,
DELAMARRE: (DENT) 97 DENTE (PORTUGUESE) Js 4
MACKENZIE: (TOOTH) 137 ‘TUNTHUS, AGOTHIC) S38
BUCK: 231 (OLD SCANDINAVIAN) 45 $b)
ONIONS: (TOOTH) 931 TONN
SKEAT: (TOOTH) 654 TAND {OLD SAXON) pS gi pS
ME i gbG day TOTH (OLD FRISIAN) S539
ZAND «(OLD HIGH GERMAN) 4 gall
[pdf page 284]
TROT eg
ZWEL GERMAN) gt DAE, DVA, DO AAVESTAN) «glee 3)
TWA OLD ENGLISH) pS god! DUVITIYA (OLD PERSIAN) lurk, go Jk
TWO ENGLISH) Si DO PAHLAVI) 65 sha,
TO (DANISH) Saito DUVA AOSSETIC) ue)
TVA SWEDISH) (545 yo DU, DU KURDISH) 535
Tvo NORWEGIAN) «5335 DU ABALUCHI) x gh
TWEE (DUTCH) gale DVA :(AFGHANI) (y~%,) itil
HOLD CHURCH SLAVIC) 4 (51 ‘WU, WE -(TOKHARIAN A) A 5 os
DUVA, DIVE wi i (TOKHARIAN B) B 5 \n5
DWA, DWOJKA (POLISH) gleng) DVAU, DVA (SANSKRIT) cy Sie
DVA, DVE (RUSSIAN) 5 ERKU ARMENIAN) «gs!
| DVA, DVE CZECH) Sey DUO, D¥o (GREEK) gli
DVA, DVEI- SLOVAK) jel DUO, DUAE LATIN) op3V
DU, DVI LITHUANIAN) gly} DEUX (FRENCH) Wil
DAU, DO =——(OLD IRISH) 5 543.,! Dos SPANISH) glilyel
DOU, DWY (GAULISH) JF DUE AITALIAN) gd)
DY, DYJ, pu ALBANIAN) UST DOI, DOUA :(RUMANIAN) gly y
TA, TAN | HITTITE) cca DoUS PORTUGUESE) gi
TWAL, TWOS, TWA (GOTHIC) S36
‘REFERENCES benhey (OLD SCANDINAVIAN) 5 $b!
POKORNN SSO*C*~*~CS*~*~«S TVEIR, TVR
BARNHART: (TWO) 1179 HOLD SAXON) ipSigigSte 4%’
DELAMARRE: (DEUX) 211 TWENE, TWA KS
MACKENZIE: (TWO) 138 4OLD FRISIAN) AS S23
ONIONS: (TWO) 952 TWENE, TWA
SKEAT: (TWO) 676 :(OLD HIGH GERMAN) 45 gist
MAA sabi chy ‘ZWENE, ZWO
[pdf page 285]
ee Le
Seo nea aes to aan
a : . RUSSIAN) 3) DUD, DUT (PAHLAVI) 5 34
DIM SERBIAN) gp DU, DUMAN (KURDISH) 52,5
DiM (BOHEMIAN) goa DUT BALUCHI) gx se
DUMAI LITHUANIAN) ol Lo HAFGHANI) (4) git
DUMI LATVIAN) (3) gx TUTE :(TOKHARIAN B) B 5 j)58
DUMIS (OLD PRUSSIAN) nS 3.2 (SANSKRIT) ex, Sie

OLD IRISH) oS S44 p\ DHUMAS, DHUMAYATI
DUMACHA, DE THUMOS GREEK) gli
TUHH, TUHBIMA = — (HITTITE) «2a FUMUS (LATIN) oa
FUMEE (FRENCH) ih
‘REFERENCES enthag HUMO (SPANISH) plays!
POKORY. OSSC*~*~*«S FUMO AUTALIAN) gids
BARNHART: (FUME) 413 FUM {RUMANIAN)
```


## [2026-09-05T20:16:29.411Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4",
 "prompt": "Give the full Persian etymology section for بیش (bīš) 'more': what Middle Persian, Old/Proto-Iranian and PIE forms it comes from, and any cognates (Avestan, Sanskrit) cited. Quote verbatim."
}
```


## [2026-09-05T20:16:31.127Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85",
 "prompt": "Give the full etymology of Persian دیهیم (dayhīm) 'crown/diadem' verbatim: source language, intermediate forms, any mention of Greek diadēma, Aramaic/Syriac mediation."
}
```


### [2026-09-05T20:16:36.628Z] TOOL RESULT

```
# Etymology of Persian دیهیم (dayhīm)

Based on the Wiktionary entry, here is the traced origin:

The word derives from **Middle Persian** _dīyēm/dīdēm_ ("diadem"), which came from **Parthian** _dīδēm/dīdēm_ ("half-crown, flower-crown"). The ultimate source is **Ancient Greek** _διάδημα_ (diádēma).

The documented chain shows: Ancient Greek → Parthian → Middle Persian → Modern Persian.

There is no mention in the provided content of Aramaic, Syriac, or any Semitic language mediation in this etymological pathway.
```


### [2026-09-05T20:16:37.396Z] TOOL RESULT

```
# Persian Etymology for بیش (bīš) 'more'

Based on the Wiktionary article, here is the etymology section verbatim:

**Middle Persian origin:**
"From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[script needed\] (wyš /⁠wēš⁠/, "more")"

**Borrowed source:**
"probably [borrowed](/wiki/Appendix:Glossary#loanword "Appendix:Glossary") from [Avestan](https://en.wikipedia.org/wiki/Avestan "w:Avestan") _[𐬠𐬌𐬱](/w/index.php?title=%F0%90%AC%A0%F0%90%AC%8C%F0%90%AC%B1&action=edit&redlink=1 "𐬠𐬌𐬱 (page does not exist)")_ (biš, "twice"), from _[𐬛𐬀𐬌𐬠𐬌𐬙𐬌𐬌𐬀](/wiki/%F0%90%AC%9B%F0%90%AC%80%F0%90%AC%8C%F0%90%AC%A0%F0%90%AC%8C%F0%90%AC%99%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%80#Avestan "𐬛𐬀𐬌𐬠𐬌𐬙𐬌𐬌𐬀")_ (daibitiia)"

**Cognates cited:**
The article cites Avestan forms but does not provide explicit PIE reconstructions or Sanskrit cognates for this "more" sense. No additional proto-forms are documented in Etymology 1.
```


## [2026-09-05T20:16:46.619Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0g%CA%B7%C3%B3%D0%BD",
 "prompt": "Does this page exist? If not say so."
}
```


## [2026-09-05T20:16:47.829Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC",
 "prompt": "Give the Ancient Greek etymology of διά verbatim: what PIE form it comes from, whether it is connected with δύο 'two' / δίς, and what Beekes or others say."
}
```


### [2026-09-05T20:16:48.779Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:16:54.834Z] TOOL RESULT

```
# Ancient Greek Etymology of διά

According to the Wiktionary entry, διά derives from the Proto-Indo-European form **\*dwís** ("twice, in two"). The article states it comes "From \*δισά (disá), from Proto-Indo-European *dwís."

The word is indeed connected to related Greek terms: "related to δίς (dís, 'twice') and δύο (dúo, 'two')."

Regarding scholarly sources, Beekes's *Etymological Dictionary of Greek* is cited as a reference work, though the specific content of his analysis is not quoted in detail on this page. The entry also references Pokorny's Indo-European etymological dictionary as a source.

The word shares cognates with Latin *dis-* and Gothic *dis-*, reflecting its Proto-Indo-European origins centered on the concept of duality or division.
```


## [2026-09-05T20:17:01.133Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dw%C3%B3h%E2%82%81",
 "prompt": "Give the reconstruction, its meaning, the descendants in Proto-Indo-Iranian/Avestan/Old Persian, Latin, Ancient Greek and Proto-Germanic, and any note about Pokorny's page number."
}
```


## [2026-09-05T20:17:03.022Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%DA%AF%D8%B1",
 "prompt": "Give the etymology of Persian دیگر (digar) 'other' verbatim: Middle Persian form, Old Persian/Proto-Iranian antecedents, and any mention of *duwitiya-kara-."
}
```


### [2026-09-05T20:17:07.154Z] TOOL RESULT

```
# Proto-Indo-European *dwóh₁ (Two)

**Reconstruction:** *dwóh₁

**Meaning:** "two"

**Key Descendants:**

- **Proto-Indo-Iranian:** *dwáH
- **Latin:** duō (via Proto-Italic *duō)
- **Ancient Greek:** δύο/dúwo (via Proto-Hellenic *dúwo)
- **Proto-Germanic:** *twai

**Pokorny Reference:** Pages 228-232 in volume 1 of *Indogermanisches etymologisches Wörterbuch* (1959)

**Additional Notes:** The reconstruction exhibits gender and case inflection variations. Alternative forms include *dwó and *duwó (uninflected). The term generated numerous derived formations including *dwi- (compounds), *dwiplós ("double"), and *dwís (adverbial). Descendants appear across all major Indo-European branches, from Anatolian languages like Hittite (ta-) to Tocharian forms (wu, we, wi).
```


### [2026-09-05T20:17:08.389Z] TOOL RESULT

```
# Etymology of Persian دیگر (digar)

Based on the Wiktionary entry, here's the etymological chain:

**Middle Persian:** The entry states it was "Inherited from Middle Persian [script needed] (dtykl /⁠dūdīgar⁠/, 'second')."

**Proto-Iranian:** The Middle Persian form derived from "Proto-Iranian _[\*dwitī́yakarah](/wiki/Reconstruction:Proto-Iranian/dwit%C4%AB%CC%81yakarah)_."

The Persian term ultimately traces back to this Proto-Iranian ancestor *dwitī́yakarah, which contains the element you asked about. The documentation notes this Proto-Iranian root as the source, showing the linguistic connection across historical language stages from ancient Iranian languages through Middle Persian to modern Persian.
```


## [2026-09-05T20:17:13.261Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D9%84%D9%8A%D8%B3",
 "prompt": "Give the Arabic etymology of إبليس (Iblīs) verbatim: whether it is from Ancient Greek διάβολος, any Syriac mediation, and alternative theories."
}
```


## [2026-09-05T20:17:13.966Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/diadem",
 "prompt": "Give the etymology of diadem verbatim, including the Greek diadema, diadein 'to bind across' analysis."
}
```


### [2026-09-05T20:17:20.226Z] TOOL RESULT

```
# Etymology of Diadem

According to the Online Etymology Dictionary, **diadem** originates from the following linguistic path:

The term entered English around 1300 from Old French *diademe* and Latin *diadema*, meaning "cloth band worn around the head as a sign of royalty." The Latin term derives from Greek *diadēma*, which refers to "the headband worn by Persian kings and adopted by Alexander the Great and his successors."

The Greek root breaks down as follows: *diadein* means "to bind across," composed of *dia* (meaning "across" or "through") plus *dein* (meaning "to bind"). The *dein* component relates to *desmos* ("band") and traces back to the Proto-Indo-European root *\*dē-* meaning "to bind."

The word's related form is *Diademed*.
```


### [2026-09-05T20:18:27.701Z] TOOL RESULT

```
# Etymology of إبليس (Iblīs)

According to the Wiktionary entry, there are two primary theories:

**Greek Origin Theory:**
The term is "theorised to come from Ancient Greek _διάβολος_ (diábolos, 'devil, accuser, slanderer')."

**Arabic Root Theory:**
Alternatively, scholars propose it originates from the Arabic trilateral root ب ل س (b l s), meaning "despairing [of God's mercy] or confounded [and unable to see the right course]" from the verb _أَبْلَسَ_ (ʔablasa). However, this etymology presents a linguistic challenge: the _if'īl_ form pattern is "usually associated with words of non-Arabic origin," making the Arabic derivation less likely.

**Syriac Mediation:**
The source makes no mention of Syriac mediation as a pathway for either etymology.

The entry notes that إبليس is "not attested before the Qurʾān," indicating its documented usage begins with Islamic scripture.
```


## [2026-09-05T20:18:36.276Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/devil",
 "prompt": "Give the etymology of devil verbatim: Old English deofol, Late Latin diabolus, Greek diabolos, diaballein 'to throw across / slander', and the Septuagint/Christian-Latin route."
}
```


## [2026-09-05T20:18:36.769Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/diploma",
 "prompt": "Give the etymology of diploma and diplomat verbatim: Greek diploma 'paper folded double', diploun, diploos, and how French diplomate arose."
}
```


### [2026-09-05T20:18:42.243Z] TOOL RESULT

```
# Etymology of Devil

**Old English Root:**
"Old English _deofol_ 'a devil, a subordinate evil spirit afflicting humans'" derives from Late Latin.

**Latin Development:**
The Late Latin _diabolus_ spread across Romance languages, appearing in Italian _diavolo_, French _diable_, and Spanish _diablo_.

**Greek Origin:**
Late Latin borrowed from "Ecclesiastical Greek _diabolos_," which in Jewish and Christian contexts meant "the Devil, Satan." In broader usage, it signified "accuser, slanderer."

**Semantic Root:**
The Greek term came from _diaballein_, understood as "to slander, attack," with the literal meaning "to throw across." This compound breaks down as _dia_ ("across, through") plus _ballein_ ("to throw").

**Religious Translation Path:**
In biblical translation, _diabolos_ functioned as a loan-translation of the Hebrew _satan_. Jerome's Latin Vulgate maintained this terminology, though Greek texts originally distinguished between _diabolos_ and _dæmon_—a distinction that blurred in English and Germanic languages.
```


### [2026-09-05T20:18:44.161Z] TOOL RESULT

```
# Etymology of Diploma and Diplomat

**Diploma's Greek roots:**
The word traces to Greek *diploma*, meaning "licence, chart," originally denoting "paper folded double." This derives from *diploun* (to double, fold over) and *diploos* (double).

**Diplomat's French origin:**
The term *diplomat* emerged through French *diplomate*, which was formed on the model of *aristocrate* from *aristocratie*. This French coinage drew from Modern Latin *diplomaticus* (1680s), which itself came from Latin *diploma*.

The semantic evolution shows how a physical description—paper folded in two—transformed into documents conferring official authority, eventually extending to diplomatic practice and the professionals who conduct international negotiations.
```


## [2026-09-05T20:18:51.291Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%B3%D8%AA",
 "prompt": "Give the etymology of Persian دویست (devist) 'two hundred' verbatim: Middle Persian form, Proto-Iranian *dwaisatam or similar, and the components."
}
```


## [2026-09-05T20:18:57.000Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dw%C3%B3h%E2%82%81\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%DA%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D9%84%D9%8A%D8%B3\" \\\n \"https://www.etymonline.com/word/diadem\" \\\n \"https://www.etymonline.com/word/devil\" \\\n \"https://www.etymonline.com/word/diploma\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 145, root Dwo: verification of nodes (bīš, dayhīm, Greek dia, PIE *dwóh₁, dīgar, Iblīs, diadem, devil, diploma)\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:18:57.187Z] TOOL RESULT

```
# Etymology of Persian دویست (devist)

Based on the Wiktionary entry, here's the etymological chain:

**Direct inheritance:** The word is "Inherited from Middle Persian [Term?] (/⁠duwēst⁠/), from Avestan _𐬛𐬎𐬎𐬈𐬯𐬀𐬙𐬈_ (duuesate)."

**Components:** The entry indicates the term is cognate with Sogdian (dwyst), suggesting a shared root structure across Iranian languages denoting the number 200.

**Note:** The Middle Persian form itself is incomplete in this source—marked as "[Term?]"—meaning the original Wiktionary entry lacks the full Middle Persian spelling. The Avestan form *duuesate* represents the oldest documented ancestor, from which the Middle Persian *duwēst* and modern Persian *devist* descend through regular sound changes in the Persian language family.
```


### [2026-09-05T20:19:01.451Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/77992dbe2e233ee1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/22664546d4c2399f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ba2cd5b97ae1a117.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/abebbc69c48591f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a26284431abb318.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a53489ea5f59e303.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f1c56c359bf99e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16a4afca74afceb4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7f955aa20b06f7e.txt
```


## [2026-09-05T20:19:20.704Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"dvadasa\" \"duua\" \"daibitya\" \"daibitiia\" \"biš\" \"bis-\" \"dvaesate\" \"duuaesate\"; do echo \"== $w\"; grep -n \"$w\" BRT.txt | head -4; done",
 "description": "Grep Bartholomae for Avestan numerals"
}
```


## [2026-09-05T20:19:22.277Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%B3%D8%AA\" --note \"page 145, root Dwo: Persian devist 'two hundred' < MP duwest < Av. duuesate\" 2>&1 | tail -1",
 "description": "Archive devist source"
}
```


### [2026-09-05T20:19:22.447Z] TOOL RESULT

```
== dvadasa
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
6603:*aAu>fia,ra  *ratumaca  Vr.  2.  7 ;  —  iva  asti spa  pasus.haumS  (sd.)  dsityS.gälul  V.  ;j. 1 7  ;  —  a?vahe  , .  anasaen^  zänu.dräja  asti a/riiisisd.)  V.lS.ii;  —  andvlm  ..y^  asti avat'aiti  mass yd^a  . .  Y.  65. 3 ;  —  astila  "' im  S.I  ataiti  bqzS  yavaiii  .  .  Y.ig.-};  — dvadasaf»hä'ir9m  asti  ayrim  ayar?  F.  27  b
8443:baiäni  .  .  dafyunam  YL  j.aj;  —  yat  hi  f i?*^'  ^-Bl}  —  >''^--'  '^^  gj^>ä  vlm<i 'm^m  paiti  var^nahi  upimät  varsa  hiku  t^J  N.jj-aM^fl/  vä yd^ra  >'u-aya,?h?m bavät"^^  ihm  zu  Oberst  de^  Kopfs  von  (sd.)  N. /o;  —  rtf.J(Lok.)  »rfj  F.27b(?f; den  Spitzen  her  die  Haare  trocken  werden"  — -»«.  i"^«,  ^.aibya,  v,iya*"\  vay.,sKit. V.Ä38;  — der  Zahl  nach:  dvadasa  vltära  «^'^J'^  *;2b;  —  »i-a  F.5. (sd.)  'ma  (PfPm.)  «air«  . .  „tar^a  xn-as  ^_Xr  \.  i  -i's  ^^.  iz.  37-  Un,geLehrt ..    mtjma  \.I4.\^  a)    IS.    '»la    als       steht  Yt.  5.  93  in  F  i  n>w.  »ra  statt  .n,i,  m
13962:•  j.  dvadasa-  Adj.  'der  zwölfte':  aAmat  j  mit  us  Kaus.  'hinauf,  in  die  Höhe  fliegen Aaca  garays  fraoxfyan  .  .  'sff  wrift'^aa}  machen':  päurvö  (sd.)  .  .  yat  dim  usca YtJO.2;  /.8,  V./4.9;—  's^m  asan/iamta  \"^'^>;'^"i  ■■  ^raitaonö  narrfahe  hArpa -  ~  ■■         -  •  YL5. 61.
== duua
== daibitya
13918:•  g.  daibitya-  Adj.:  s.  unter  bitya-.  ,Myana  dva    hqmina    V,/.3;  5.27,  7.52, .g.daibi5yat»t-Adj..PPA.:s.unter/i«>«/-.;^'-'^-45^'5-3,F./;-^<'a^a/4<rA«^«-
17263:•  j.  bitya-'>,  g.  daibitya-'',  p.  duvitiya- Adj.  (fem.  'ya-)  'der  zweite':  paoirys gairil hqm.hiUat  ,  .  haraiti  barl  °iyS  T^r^azS gairi/ Yt.  ig.  1;  j.7,  14.7,  Y.(?.6,  7,  Y.4.3,
== daibitiia
== biš
== bis-
14726:~  I  daibil-,  ibis-,  2  7  daibifya-,  tbilya-,
14731:"  yaskanqm  yaskffJtmgm  janüt  .  .  Iballayät ...„.„Z"    -  16*';    —   tbis'yant-,  daibis-
18877:•  j.  näfyö.tbis-  Adj.  'der  die  Familien- angehörigen, Geschlechts  verwandten  be- feindet'; inä  nS . .  dusrfta»a»Ae . .  mä  'IbÜe Y.  65.  7.
30354:•  i.  hu-bis-  Adi.  (auch  fem.)  'der  gute  -t,    ^  .,.,,,
== dvaesate
== duuaesate
```


### [2026-09-05T20:19:24.728Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1a2d0d76dac58efe.txt
```


## [2026-09-05T20:19:32.155Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zweimal\" BRT.txt | head -5; echo ---; grep -n \"'zwei'\" BRT.txt | head -8; echo ---; grep -n \"zweihundert\" BRT.txt | head -5",
 "description": "Grep Bartholomae for zweimal/zwei"
}
```


### [2026-09-05T20:19:32.229Z] TOOL RESULT

```
4574:aiitaräis  in  lesen.  —  »)  FoY  KZ.  33.  42  will pnra^  jtatt  o"/^r  lesen;  s.  «bei;  lO.  iSt.  — 3)  lli'i./räiinSiilarf.'Fü.: ..  andari.— <}  HAs. fehlend ;  s.  aber  Pü.,  die  zweimal  andar  bielet. —  9  Uiw.  Plnr.;  vU.  nur -als  Venrcler  des AP.
7730:Ableit.  (mit  p-)  aus  *jrj!-ui-')  'recht  spre- chend' sva.  'des  Wort  für  giltig,  voll  ange- sehen wird' 3),  zum  V.  z'iii--,  S  P".  2  n.  — <)  Hds.  vTr/m,  wie  zweimal  zuvor;  ZDMG. 4j.  669.  —  a)  I  durch  Dissimilation  mit  dem folgenden  J-Laut,  die  eingetreten  sein  muss, bevor  ir.  j-i  lu  jAw.  ati  wurde.  —  3)  Vgl. zur  Sache  Vd.  iS,  Bthl.  IF.  //.  128,  Menaht
7950:direkte  Rede,  Zitat  od,  dgl,;  a)  adjekti- visch: a^a  'mqm  (APm.)  vacff  dnn/a- yöis  .  . :  asiiunqm  .  ,  frava^ayS  .  ,  Yt.  /  J. 2o£;  Jo,V.'*'().i2,27,*/7.S,  N.71;  V.().z8, II. \,  Y. 6^.10  (wo  "mq);  —  'mal  vacB framrü:  nimS  .  .  V./9.18;  —  a'i:a  -mä nUmSnls  . .  framrva:  payusca  ahmt  . .  Yt. /,  11;  —  'me  vala  ä'Mtlm  framrva: ahyä  yäsa  . .  "die  folgenden  Worte  sprich zweimal:  ahyU  y  .  ."  V.  70.  3;  ir,  5,  7, 15;  - —  li  'maiy  martiyil  hamataxsd'tä  anu- siyä  mana:  vi^dJ'/ama  nilma"  ..  Bh.  ..^.  18; 18.  b)    substantivisch:     'mal  sanhsis
10042:'aufziehen,  grossziehen':  bis  hapta  pui^rqm ga'iwqm  «i/(7MJ/V"'""zweimalsiebcn junge Hunde  soll  er  gross  ziehen"  V.  14. 16.  2)  'heraufkommen  zu —,  erstehend sich  einstellen  bei  -';  a)  mit  Lok.:  Aya^ US  asa  naptyassu  naßuca  türahya  uzjSn (jSPr.^.)  '**  fryanahya  aoJyaisR  "wenn sich  das  Asa  bei  den  preislichen  Enkeln und  Nachkommen  des  Tlsrers  Fryana  ein- stellen wird"  Y..rf6".  12.  b)  mit  Dat.: US  na  aMbai  vTse  Jamyal  ahnica  xsa- ^mm^a..  Y.60.  2;  —  ta  iiö  ama  tä  v)r»- %rayna  ,  .  usjamyqn  ya  staota  yesnya  Y. i5-  3-  3)  'ausschlagen,  gereichen  zu  — '
10074:onter  Jnsattl-.  —  "»  Vgl.  Yt,  10.  8.  —  ")  Nur zweimal  vom  selben  Stamm.  Ob  statt  IS.  nach dem  Muster  fem.  J-Slämme,  bei  denen  LS. und  IS.  lusammcntieleQ?  —  n)  Besser /ajä.- R>',  %  268.  57.    —    131  Them.    —    '*)   Hds.
---
---
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
```


## [2026-09-05T20:19:39.943Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"saite\\|sate\\b\" BRT.txt | grep -i \"dva\\|duu\\|dve\" | head -5; echo \"---21255\"; sed -n '21255,21266p' BRT.txt | head -20",
 "description": "Look for Avestan two hundred"
}
```


### [2026-09-05T20:19:40.008Z] TOOL RESULT

```
6962:i)  die  Richtung  auf  den  Sprechenden  zu angebend  'her,  heran,  herzu',  nur  in  äca paraca  'her  und  fort'  sva.  'hin  und  her, hin  und  zurück'*':  'hrixsaparim  hahräkgm (sd.)  *xh'ai  xsa/nd  aca  paraia  N.4;  — pairika  ,  .  3ca  paraca  dvaraiH  YtÄ  54; —  v?r>^raynpm  ..  yö ..  äca  paraca  p}r?- saite  Yt.14.4-j.  ")  anschliessend  'dazu, dazu  auch,  und  auch':  a?s^  zi  vnxs  . . */ramrva»ö  a  vacO  afiunS  vairyö  fraoxtd .  .  spanvanti  H. /.4;  —  hä  hama  pairi- säiU  frapaya  (sd.)  daühus  ä  upaosatfh- väsca  Yt ig.\\  —  yS  H  axtÜ  akmäi  yJm axtsysi  (sd.)  dstihg  ^.36.  i ;  —  'kwSi  as *ärmaitis  ^w!  ä  gStt^  tasä  (sd.)  as  Y.31. 9.  a)  wiederholt  'et  ,  .  et',  nach- gestellt: akunm  mazdqm  amruyi  (sd.) nmänake  nmänS.patsis  ratüm  ä  viss  Tlspa- tsis  ratüm  ä'  .  .  daiähupatOts  ratüm  3 Y.  lg.  I.  a)  in  Verbindung  mit  (vor-
11160:•  j.  ca9-war«-sant-  fem.  Zw.  'vierzig': ^a'^u/arasla  a^a  garayl  .  .  'satimca  (ab Nom.)''  dvai^a  saite  dvai^a  hazaj»re  "es gibt  so  2244  Berge"  Yt./p.?; — paruäla 'sat>mea  maiiysizarmtayehe  (%A^  . .  "45  . ." A.j.  7.  a)  mit  Gen.:  'sat?m  (Alck.)'* aiwigämanqm  V.  2.  41;  5. 93,  /2. 14,  *Y. 65.4»,  ^Vi/p.
11763:—  tat  yat  kaemahe  draonS  Y.  /o,  1 5 ;  — tl yii puira  ^raaaonahe'S.4i.; — gai'^yäi tl  (NDf.)  yöi  abds.tfme  {sA.)  Yt5.34;  — *tam  (APm.)  yat3i  t3m(J)  pairi.jasäi  .  . *yqm  amssS  spmti  Y.70.1;  —  tftn  i'ira hanjassnte  yat  * ma'hrim.spsnttm.balsazam V.  7. 44.  III)  In  folgenden  Fällen  ent- spricht unser  unbestimmtes  Pron.  'ein'  (vgl. ^aita-  Sp.  17  o.);  a)  adjektivisch:  upa  tqm vanam  vasaite  xraozdvanqmca  (sd.)  van- dt-anamia  V.5.1,  b)  substantivisch  :/.i(W sl  hl  ^parftd.tanunam  itanhaiti  yahmat haca  t9m  ava^aofanti  (sd.)  N.  42.      a)  mit  |
13924:'fesseln  sva.  einschränken,  Einhalt  tun';  I''''^''"'? ''"«^'' *'i'«^'''^(s'i-)*''«''"'-'i'''?"' m  aihms  «r'>  dyätam  (3SIM.,  in  pass.  1  "■  ■  zwölf.."  F.27a;  —  cäkwarasca  ai,a Sinn)  paia  nmim  pattz^*  *sysdäm  (sd.)  k'^'IVi'  ca^warisatimla  (sd.)  dvaila  (Nn.) y.  ^.  j.  \saite  dvatca    kaza»re  Yt.ig.-j;    —    duye
14891:Entgelt)  dafür':  äa^  mqm  tarn  *^aisaxyilii ..  dahäni  tl  aStahe  'ti  V.22.  2f.'3>;  — iat  astahe  'ti  ..  azaeta  (Sp.  2240.)  V. iK  68**;  —  ait»)n>m  ijaoiinanqm  .  . altahe  'ti  .  .  duye  saite  upaeananqm  upä- «3(V  (Sp.  224  m.)  V.  4.  2o'4).  '4)  zur Bezeichnung  der  Ursache  und  Urheber- schaft, sowie  des  Mittels  'per';  i)  mit  Akk.; a)  'mittelst':  frasnatse  .  .  ayryqm  (sd) 'ti  usnäitlm  V,  Ä  98;  —  mi^ra  ahura  .  . yasamaide  .  .  urvarä  'ti  batvsmanyä  Yt. 10. 145  (s.  2a);  —  yasiä  Hl . ,  väHm  °ti tofnis  {sd.)  anhat  V.  7^,  40;  — aitakmllyus 'ti'>^  AirÄ^w  V./5.ai,  43.  b)'wegen, propter':  aitahmSyiti  'ti"'''  varsla  syao^na V.  75. 10.  2)  mit  Lok.;  a)  'mittelst': ahura  mi>ra . ,  urvaräÄu  *ti  bar)smanyähu .  .  äyese  yati  Y.  2,  11  (s.  i  a);  —  */tahmäi tl  aioahmi  'ti  vaSs  . .  /ravaktm  (sd.)  H. /.  I*'; —  handaitim  staotanqm  yesnyanqm yasamaide  apan3J»may3  (sd.)  °tl  va^astaltä Y.sS.S'^-l  b)  'durch':  saräku^lrahe  . . yakmi  'ti  .  ,  *asim.srav3  (sd.)  vTsruyaia Yty.  91.  c)  'wegen,  propter':  nSil.. ahmi  'ti  nairi  dva  *mainyu  r}na  (sd.)  ava.- stäahat  V.  7. 52.  3)  mit  Gen, ;  a)  'mittelst'; yqm  yazata  zarä^uströ  . .  humatahe  °ti manavAlF    Yt.  16.  6;    6'.  b)    'wegen,
---21255
Unklar:  P.54.
ai.  yäccil  Adv.  'wenn  auch'.  —  Pö.  (lu  N.) : ka<i;  (lu  F.):  hakarÜ;  (zu  Y.):  hin.  —  »  Vt. //.  55  steht  in  gleichem  Sinn  y<U  .  .  aal.
•  j.  yat  paiti "  adv.-artige  Verb. ;  sie  leitet überall  einen  Satz  ein,  der  auf  eine  Frage antwortet;  i)  'wo,  ubi':  kva..z)mö  säist)in1 ■  •  yl  ^''  p^iti  fraistim  kärayeiti  .  . yavanqtttca  västranqm{sd.)ca  V.  J.  4;  i, 2.  5i  6,  8—13*,  32.  2) 'wenn,  wofern': kaf  asti  damaya  uruhwan  {sd)i  ..  ya^ w/rim  paiti  yaokarsti  (sd.)  V.  _j.  30;  — kö  .  .  tarn  . .  x^nUvayeitil  ..yat  bä  paiti .  ,  naire  aSaone  vtnzyät  asaya  daoäiti  V.
3-  34;  35-
Eig.  'in  quo';  ASn,  ausj-a-.  —  Pü.i  ku  pa an  apar,  ku  pa  öi  apar.  —  ')  Stets  durch  ein Wort  getrennt.
•  j.  yat  vä"  partikelhafte  Verbindung; J)  zur  Trennung  von  Satzteilen  im  Sinn des  lat.  vel.  Sie  tritt  1)  zum  letzten  von zwei  oder  mehreren  Satzteilen:  ä%rat  haca . .  alsmq  frasaocayähi  (sd.)  y°  vä  aSan- hqm  urvaranqm  yat  ätn.ci%ranqm  V.S. 75.  a)  beim  zweiten  und  den  folgenden steht  ^ä:   yö  .  .  dahmim  *jainti  andus
vä  ayfyS.staor3m  vä  Hstaartm  vay  masa-
nhiM  V  ^ar^m  (sd.)  N.  45''.  i)  zum zweiten  und  den  folgenden:  ahunim  vai- rJm  frasrävaySis  tis'rll  y  v  xJvaf  y  v° nava  V.  sj.  6;  6'.  a)  beim  ersten  steht 'vä:  frasrävayamnake  vä  ..  ^=»'  v'  '*yas- n?m  *yaz>mnake  N.20; — gSus  malsmana . .  %ris  vä  sämqn  y  V  xSva/  y  V  nava V.5.  51.  3)  zu  allen:  yas/a  .  .  bayam
. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
Undeutlich:  y  v°  ya^a  *U£ayarvm  y (v)  ya^a  xiapamn  N.  47-  [V-A*.  75  z.SL: streiche  vä;  s.  Sp.  41a  m.]  yat  vä  mit yat  als  Konjn.  s,  unter  '^a/.
Aus  yat  (Konjn.?,  Part.  ?)-(- »wä  erwachsen.  — VgL  y^a  vä,  —  Pü.  (beim  »weiten  und  den folgenden  Malen):  aläv;  s.  lu  3vä.  —  >)  Ein- mal {N.  ^51  getrennt.  —  >)  So  T;  Aasg.  yi. —  3)  So  T.  Ausg.  yäJ.  —  4)  Vgl.  N.  fo, Sp.  1260  m.
•  p.  yanaiy  Adv.  'wo,  worin':  i'iwa*  stä- nam  (sd.)  iauv  niyaüäya*  kt^tanaiy  y dipim  naiy"  nipi^täm  akunaus  ".  ,  ohne (aber)  eine  Inschrift  darin  anbringen  zu lassen"  X.7.  3.
```


## [2026-09-05T20:19:50.528Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"dw'sty\\|duwist\\|dwyst\" \"dydym\\|dedem\\|dydm\" \"dwdyk\\|dudīgar\\|dudigar\" \"^dō\\b\\|do\\b.*two\"; do echo \"== $w\"; grep -n -i \"$w\" PHD.txt PHD_mackenzie.txt 2>/dev/null | head -4; done; echo \"=== NYB\"; grep -n -i \"dydym\\|dēdēm\\|dwdyk\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-05T20:19:52.312Z] TOOL RESULT

```
== dw'sty\|duwist\|dwyst
== dydym\|dedem\|dydm
== dwdyk\|dudīgar\|dudigar
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:3548:second didom, dudigar.
PHD.txt:5298:dudīgar
PHD_mackenzie.txt:7518:safJlower zardak.                          second didom, dudigar.
== ^dō\|do.*two
PHD_mackenzie.txt:2004:do [2, TLYN' < A tryn I M dw, N du] two.
PHD_mackenzie.txt:2014:do-saxwan [2 shwn ] two-tongued, deceitful.
=== NYB
```


## [2026-09-05T20:19:57.426Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"diadem\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt HUB.txt 2>/dev/null | head -10",
 "description": "Search local refs for diadem"
}
```


### [2026-09-05T20:19:57.486Z] TOOL RESULT

```
HUB.txt:494:psak 'Diadem, Krone, Kranz').
HUB.txt:2021:Dazu arm. xoir *Kopf band, Diadem'. Horn vermeidet
HUB.txt:7079:xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
HUB.txt:7124:deutet arm. xoir 'Diadem* auf parth. *a*5tT = ap. xauda-
HUB.txt:7167:*Helm* = syr. NTIH 'diadema', Brockelmann p. 105, arm.
```


## [2026-09-05T20:20:17.708Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(340,380):\n    l=leaves[i]\n    # persian-digit running head at top\n    head=l[:200]\n    d=re.findall(r'[۰-۹]{2,4}',head)\n    first=re.sub(r'\\s+',' ',l[:60])\n    print(i, d, first[:55])\nEOF",
 "description": "Show BQT v2 running heads 340-379"
}
```


### [2026-09-05T20:20:19.439Z] TOOL RESULT

```
340 []  ‫هواس‬ ‫نگیفزت
341 []  
342 []  ‫بیان ه
343 []  
344 [] ‫و آنر! حب‌الخطای وحب‌اللاطین خوانند ‪ ۴‬؛‬ ‫اصاری ش
345 [] ‫دندان فرش ‪:‬‬ 
346 []  ‫‪۳‬‬ 
347 []  
348 []  ‫یات‬ 
349 []  ‫دواله‬ 
350 []  ‫=‬ ‫با بای ایجد بروزن رومال »‬ ‫دبوال‬ 
351 []  
352 []  ‫پوس‬ ‫کون طای ب
353 []  ‫حودله‬ 
354 []  ‫‪4‬‬ 
355 []  ‫دز رو‬ 
356 [] ‫پاسس‬ 
357 []  ‫دوس‬ 
358 []  ‫—~‪—~AAA‬‬ 
359 []  ‫دوکار ‪:‬‬ 
360 []  ‫‪ ۵‬ات‬ ‫تن‬ 
361 []  
362 []  ‫هت‬ 
363 []  ‫دپهنجی‬ 
364 []  ‫‪-‬‬ ‫‪۰‬‬ ‫یت‬ 
365 []  
366 []  ‫=‬ ‫‪6 ۵‬‬ ‫‪۱‬‬ 
367 [] ‫دي‬ 
368 []  ‫سره‬ 
369 []  ‫دور‬ 
370 []  ‫=‬ 
371 ['۱۱']  ‫در ند‬ 
372 []  ‫‪n‬‬ ‫‪Sh‬‬ 
373 []  ‫دطروجاش‬ 
374 []  ‫‪-4۱-‬‬ 
375 []  
376 []  ‫‪6‬‬ 
377 ['۱۷']  
378 []  ‫اه‬ 
379 []  ‫ديو دولت‬
```


## [2026-09-05T20:20:25.223Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nleaves=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,(p) in ((348,888),(362,902),(374,914)):\n    print(f\"########## leaf {i} = p.{p} ##########\")\n    print(leaves[i][:2600])\nEOF",
 "description": "Print BQT pages 888, 902, 914"
}
```


### [2026-09-05T20:20:26.781Z] TOOL RESULT

```
########## leaf 348 = p.888 ##########
    ‫یات‬                                                                                     ‫دله گرقه‬

‫دلین ‪ = ۴‬بر وزن رسیدن ‪ .‬بمعئی‬
 ‫دوبدن بنشاط و بخوشحالی براه رفتن باشد ® ‪-‬‬           ‫نعمت الهی باشد ‪ -‬و بمعنی خوشحال و شادمان‬

 ‫وبمعنی ازجای دآر‪.‬دن ‪ -‬وازخشم وقپرجوشیدن‬            ‫را لىز‬   ‫و تند براه رونده و دوفده‬        ‫هم همست‬

                                   ‫همگفته‌اند ‪:‬‬                                              ‫کفهداند ‪.‬‬


         ‫راه رفته ناشد ‪۳‬‬   ‫بخوشحالی‬    ‫خرام ده و‬
                                                     ‫وخوشحالی‌بخرامی‪ -‬وبعریی‪ ۴‬مردم دون وخیی‬
                                                                                            ‫رکاویند ‪.‬‬


                                         ‫بان نورد هم‬


 ‫‪ ¥‬دو ] تش ‪-‬کنابه از دوب معشوق | وزن روارو » دویدن بهرطرف باشد از پی‌هم ‪-‬‬
‫شوخصی را نکیوزبند که خدمات جزئی باو‬                                                               ‫باشد‬
     ‫رجوع باشد وهرساعت اورا بکاری فرستند ‪.‬‬
                                                    ‫دواج ‪ = ۲‬بفتح اول بر وزن رواج »‬
‫دوادی ت بفتح اول بر وزن نهاری »‬                                             ‫یمعنی لحان باشد ‪. ۸‬‬
‫از آن به‌ینج‬   ‫رایج ازطلا که هرك‬   ‫زری‌بوده‌است‬


 ‫وال ابجد بد | شیالی خرح میشده " وشیانی زری بوده الزای‬
                                                     ‫دوادو ‏‪ = ٩‬بفتح اول د‬

       ‫(عر) بتشدید اخرآمده ‪.‬‬
                           ‫‪۴‬‬                   ‫؟ ‪۴‬‏ رك‪ :‬دیدن ‪.‬‬          ‫رك ‪ :‬دنه ‪.‬‬      ‫‪۱‬‬
   ‫از ‪ :‬دن ‪٣‬‏ بدن(یسوند مصدری) ‪.‬هندی باستان » ره ‪_131d‬‏ ‪62040020 ,‬‬                      ‫‪۴‬‬
                                                                  ‫(دویدن) د اسشق ‪ 6۷۵‬دوم “ ‪.‬‬

  ‫بر خم همی خرامی و بردن همی‌دلی ‪.‬‬                 ‫‌بهرمی‌شینی و ب رگل همی خوری‬
                                                                              ‫®ل‪-‬‬
                                                                                ‫گ‬
  ‫«‪+‬ءنوچهری دامفانی ‪۹۰۱٩‬‏ ‪.‬‬
   ‫‪ - ۷‬طبری [‪ .2۷04‬ز‪( 4۷40‬لحاف)‪ .‬مدارزانی‬                    ‫‪ - ۷‬اسم‌مقمول از«دنیدن» ‪.‬‬
                                      ‫کنوی [‪ . ۵۷61‬ز‪ . 24‬زا ‪2[ .‬ظ‪ 0‬دواژه نامه ‪. 4۹۳۰‬‬
           ‫همی غلطم اندرمیان دواح ‪.‬‬                     ‫یمآگه از اسل وفرع خراج‬                ‫‪۸‬‬
  ‫فردوسی‌طوسی‪« .‬چهارمقاله‪.>۸4‬‬
                       ‫‏‪ - ٩‬از ‪ :‬دو (دویدن) ‪( ۱ +‬واسطه) ‪ +‬دو (ایسا) ‪.‬‬
 ‫که ‪« ۷۵-۸۵‬منای‬
              ‫‪ #‬دو ‪ -‬م اول (‪ , )00‬پهلوی ‪ , 80‬از ره ل‪« © 13۷‬ریی‬
 ‫‪.‬ردی لال ‪.‬‬‫‪ > ۲۷‬با
########## leaf 362 = p.902 ##########
    ‫هت‬                                                                                             ‫دوبره‬
                                                                  ‫‪۷.‬‬   ‫بدان دوات مر کب را برهم زد‬

‫تحتانی مجهول ولام» بمعنی مکر وحیله باشد‪.‬‬           ‫دو بر‪ = ۵‬بروزن کبیره؛ دوالونسمه‌ای‬
‫و ابررشم گنده را نیزگوبند که از پیله‌ای (‪)۱‬‬                                   ‫باشد که مدان قماربازاد‪4 .‬‬
          ‫‪۰‬‬
    ‫آن باشد ‪.‬‬       ‫ورن‬
                      ‫ر د‬
                        ‫دکرم‬
                           ‫حاصل شودکه دو‬           ‫بضم اول وفتح ثالث وسکون‬                ‫يوك‬
                                                                                            ‫د‬
                                                                  ‫کاف » کنانه از دم آخرمردن باشد ‪۱‬‬




                                            ‫بیان بیستم‬
              ‫ددرال بی‌نقطه بهاای هوز مشتمل بر بنجاه لفت و کنات‬
‫وفر باد رایز گفته‌اند؛ ومعنی اول با زای نقطه‌دار‬     ‫علری‬   ‫‪.‬‬    ‫بقتح اول و سکون الى‬       ‫‌‬   ‫‪3‬‬


                         ‫است معین که ‪,‬عربی‌عشره گوبند ‪ -‬وامرمعروف | هم پنظرآمده است ‪. ۴‬‬
‫دهار ‪ -‬و وهاژ با زای هوز و زای‬                       ‫ونهی منکر را نیز گفته‌الد ‪ -‬ویکسراول معروف‬
‫است که درمقابل شهرباشد ‪ - ۴‬وامر بدادن هم | فارسی هر دو آمده است بر وزن نماز * بانگ‬
 ‫وفریاد ونعره راکوبند ‪ -‬وبک‌راول دره وشکاف‬                                             ‫رای بل ‪2‬‬
 ‫‪۵‬هار = بروزن بهار ‪,‬غار ودره وشکاف | کوه را ‪۵‬؛ وبمعنی اول بکسراول » وبمعنی‌ثالی‬


                                                   ‫(‪ )۱‬چك ‪ :‬پیله» خم ‪ :‬بكپیله ‪.‬‬
  ‫‪- ۱‬یپلوی(‪*121‬اونوالا ‪ ¥‬اوستا ‪, 2531‬هندی باستان ‪» 266‬ارمنی‪ .]52‬کردی وبلوچیع‬
  ‫‪ .021 8‬افتانی ‪ 92۱‬استی‪ . 581‬وخی‪ 821. 5201‬شربکلی ‪ .5601‬شغنی‪521 . 501‬‬
  ‫ختنی ‪« 2521‬بیلی‪ .‬روز کارنوج؛ شمارة‬          ‫نوم وسنگل جى ‪ " 5314‬منجیع ‪ « 021‬اسذق‪۷۸‬‬
  ‫‪ ۰‬بارسی باستان‬    ‫دبه ‪ .‬یپلوی ‪hêd‬‏ »‪ 2‬تاوادها ‪۶۴‬‬     ‫=‬    ‫‪۳‬‬             ‫‪.‬‬    ‫گیلکی ‪2‬‬     ‫‪* ۲6‬‬    ‫‪ ۳‬ص‬

   ‫‪.‬ردی ‪. 112‬اففانی ع تال‬‫‪1‬ا‪ . 73‬هندی‌باستان‪ 11158 -‬ک‬‫‪( 00‬سرزمین) » اوستا ق‬
      ‫بلوچی ع ‪ 01‬و تا « اسشق ‪۸‬ه» ورك ‪ :‬هوبشمان ابا ک›یلکی ‪ . 6‬رك‪ :‬ده‌بوید‪.‬‬
                               ‫‪« - ۴‬دهار ‪ ,‬غار وشکاف کوه بود » اسدی (طوسی) گوید ‪:‬‬

     ‫زبان چون درخت ودهان چون دهار»‪.‬‬                             ‫بکابك پراکنده بر دشت وغار‬
  ‫د لفت فری ‪. ۸۵۱‬‬
                                 ‫© _ مصحف « دهار > (هدم‪. ).‬‬               ‫رك ‪ :‬دهاز ‪.‬‬      ‫‪۴‬‬
  ‫هندی باستان‬      ‫)‪.‬‬   ‫ددن ( پسوند مصدری‬   
########## leaf 374 = p.914 ##########
 ‫‪-4۱-‬‬                                                                                      ‫دنگ‬
                           ‫آهنین باشد ‪٩‬‏ ‪.‬‬       ‫واز بونه برآورند تفلکه در ته بوته مانده باشد‬
 ‫د یگ بر دینگ = بکسراولوسکون‬                     ‫مرقشیشاست » وآنرا دیفروجس بحذف الف یز‬
                                                ‫کفته‌اند ‪ .‬چون ارا سحق کنند وبرموی غلیظ‬
‫کاف آخر بر وزن بیخ ببریخ » م رکه موش‬                              ‫افشانند رقیق وترم کرداند ‪#.‬‬

                                                  ‫دلگ » بکسراول وسکون‌انی معروف‬
                                                ‫و کاف فارسی » بمعنی دی باشد که روز گنشته‬
                                                ‫است ‪ - ۱‬و بعربی خروس را کوبند ‪ - ۴‬و با‬
 ‫خسس‬   ‫و‬   ‫و دال بی نقطه ‪ ,‬کنابه از مردم شل‬
                                                 ‫تحتالی مجپول» ظرفیکه درآن چیزی پزند؟ ‪-‬‬
                                     ‫باشد ‪3.‬‬
                                                 ‫وتوپ بزر که رالیز گویند که بدانکلوله برقلمه‬
‫دیل ‪ -‬بر وزن فل » بمعتی تقعاه است‬                                                        ‫اندازند ‪.‬‬
 ‫که طرف خط باشد چه‌تعرف نقطه بطرف خط‬             ‫دیگ افز ار ‪ - ۴‬افزار دبک را‬
‫کرده اند ‪ -‬ودل را نیز گوبندکه بعربی قلب‬          ‫گوند‪ .‬یعنی آنچه دردیگه طمام ریز ندازنشود‬
                                                 ‫و کشمش وبادام وفلفل ودارچینی وقرلفل وزبره‬
‫کوسفندان وکاوان و دیگر چاریابان در آنجا‬          ‫ومانندآن ویعربی تابل خوانند وجمع‌آن توّابل‬
                                     ‫باشند ‪.‬‬             ‫است ‪ -‬ودنگه بزر که را نگیفزته‌اند ‪.‬‬

 ‫دیلم = با اول بتحتالی مجهول رسینه‬               ‫دیگ اورار ‪٩‬‏ با واو بوررن‬
 ‫اکیلان‬
      ‫وفتح لام وسکون میم‪ ,‬نام شهپری است ز‬        ‫ومعنی‌دیگه افزاراست که نخود وبادام کوشمش‪-‬‬
 ‫وموی مردم! لجاپیچیده ومجد میباشد و یشتر‬                   ‫ردنگه بز ر گے باشد ی‬     ‫وداروی کرم ‪۳‬‬


 ‫حربة ایشان تبر هیزم شکنی و زویین (‪ )۱‬امت‬        ‫‪-‬عنی‌دیکدان وسه با‬
                                                                  ‫دیگ پایه بم‬

                                                                   ‫(‪ )۱‬چك‪ :‬ژوبین ‪.‬‬

                          ‫تازی ‪.‬‬   ‫ک)اباف‬
                                        ‫‪ ( ۴‬عر‬                      ‫‪.‬‬   ‫‪ :‬دی‬   ‫رك‬    ‫‪۱‬‬


   ‫(دبکه)) از بارسی باستان_ ‪861120‬‬     ‫بقول هوبشمان دنگه فارسی (اففالیع ع‬            ‫‪۴‬‬
  ‫کردی ع‬     ‫ید بد آمده‪ .‬عکل بهلوی ‪gêd‬‏ (دنگه) هیأت عازه انت از آن د هوشمان ‪>» 14۹۵‬‬
  ‫‏‪ , dîzik‬افتانی ع ‪ . 26060 , 884‬بلوچی ع‪ 1862 1064 . 21 4‬وخی‌وسر بکلی‬
```


## [2026-09-05T20:21:35.123Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg145.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/145.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T20:21:35.194Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:21:36.527Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%AC%DB%8C%D9%86",
 "prompt": "Does Wiktionary have an entry for Persian دوجین 'dozen'? If so give its etymology (French douzaine or Russian дюжина?)."
}
```


### [2026-09-05T20:21:38.607Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:21:44.532Z] TOOL CALL #66: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/145.png",
 "description": "Verify page image copied"
}
```


### [2026-09-05T20:21:44.580Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 89133 Sep  5 16:21 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/145.png
```


## [2026-09-05T20:21:58.008Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN 13.32 TWO\"; grep -n \"13.32\\|13\\.32\" SYN.txt | head -5; echo \"== IEC dwo\"; grep -n \"^duō\\|^dwō\\|^duo-\\|^duu\" IEC.txt | head -10; echo \"== WLD band3 duo\"; grep -n \"duō(u)\\|duuo\\|dṷō\" WLD_band3.txt | head -5",
 "description": "Grep Buck, Mann, Walde index"
}
```


### [2026-09-05T20:21:58.098Z] TOOL RESULT

```
== SYN 13.32 TWO
23366:13.32 Onn
23835:Except for some suffix-variation and actual substitution in the case of ‘one’ (13.32), the IE words for ‘one’ to ‘ten’ have persisted everywhere with only slight changes other than phonetic; like- wise the IE word for ‘hundred’, while for ‘thousand’ there are several different groups.
== IEC dwo
2622:duuoim, dat. of type *duuó, see duðu, etc. Gk. duoin; Go. twaim; OHG zweim; OCS cf. düvéma; Li. dviem; Latvian diviem, id.
== WLD band3 duo
```


## [2026-09-05T20:22:01.422Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"13.33\\|‘two’\" SYN.txt | head -8; echo ---; sed -n '23380,23400p' SYN.txt; echo \"=== IEC duðu\"; grep -n \"duðu\\|duou\" IEC.txt | head -6",
 "description": "Buck TWO section and Mann duo"
}
```


### [2026-09-05T20:22:01.495Z] TOOL RESULT

```
3297:Russ. dvojurodnyj brat, dvojurodnaja sestra, the adj. being a cpd. of coll. dvoje ‘two’ with rodnyj ‘own’ fr. rod ‘family’, so a sort of ‘second-line brother’.
9422:2. Lat. cépa (> Rum. ceapd, OF. cive, Ir. ciap in folichep ‘porrum, capil- losa cepa’, OF ctpe; late dim. cépulla > It. ctpolla, Sp. cebolla, OHG zwibolla, etc. [pop. association with words for ‘two’ and ‘ball’]; MHG zibolle > Lith. cibulé, Boh. cibule, Pol. cebula; MLG sipolle > Lett. stpuols), with Grk. dial. kami’ ra oxopoda. (Hesych.), loanword fr. un- known source. Ernout-M. 176. Walde- H. 1.201. REW 1817, 1820. Vendryes, De hib. voc. 124. Weigand-H. 2.1355.
11725:Grk. @ipa; Lat. forés (pl.); Ir. dorus, Nir. doras, W. drws (Pedersen 2.20), W., Br. dor; Goth. daur, OF duru, OHG turi, ete., general Gmc. for ‘door’, be- side OE dor ‘gate’ (but not always dis- tinguished fr. durw ‘door’), OHG-NHG tor ‘gate’; Lith. durys (pl.), ChSl. dvirt (mostly pl. dviri), etc., general Balto- Slavic; Skt. dvar- (mostly in dual or pl.; d for dh by analogy of dvau ‘two’), dvara-, Av. dvar-, OPers. duvara-, NPers. dar; Arm. durn; Alb. deré.
12626:Several of the words for ‘fork’ as an agricultural implement, ‘pitchfork’, are connected with words for ‘branch’, or as orig. ‘two-pronged’ derived fr. words for ‘two’.
12631:4. ON kvisl (esp. epd. myki-kvisl ‘dung-fork’), also ‘branch or fork of a tree or river’, prob. (with initial k for Die OE twisla ‘branch of a river’, OHG zwisi- la ‘forked object, branch’, derivs. of ON tveir, ete. ‘two’. Falk-Torp 607 f.
12634:heytjtiga, hgtyv ‘pitchfork’), deriv. of ON weir, etc. ‘two’. Falk-Torp 450f.
13217:ON kvistr, mostly ‘small branch, twig’ (Dan. kvist, Sw. qvist ‘twig’), ME twist, twyste (cf. NED s.v.), cf. ON hkvisl ‘fork, branch’ (of a river, etc.), fr. Gmc. twis- (Goth. twis- ‘apart’), IE *dwis in Lat. bis, early Lat. duis ‘twice’: IE dwou- ‘two’ (cf. below, OE twig, etc.). Walde-P. 1.820. Falk-Torp 607 f.
13225:OE twig, twigge (ME, NE twig ‘smal] branch, twig’, but in OR general ‘branch’, cf. Gospels, Mk, 13.28, Mt. 24.32, of the branches of the fig tree also Jn. 12.13 palm-treowa twigu), Dit twijg, OHG zwig (mostly ‘twig’, of. Graff 5.729; but also ‘branch’, ef, Tatian 116.4, 5), MHG zuice (likewise mostly ‘twig, sprout, cutting’), NHG 2weig, all derivs. of IE *dwi-, *dwei-- *dwou ‘two’, like ON kvistr, etc., above. Here also OHG zuog, OS tg, with vowel from the numeral. Walde-P. 1.819, Note the opposite tendencies of usage in Eng- lish (‘branch’ > ‘twig’) and German (‘twig’ > ‘branch’).
---
NG moaérns ON
(fjoldi, mergd, mengi) Lett. kvantitate (daudzums)
Lat. quantitas Dan.  kvantitet ChSl. (mitnogisivo)
It. quantita Sw. kvantitet SCr. _ kolitina
Fr. quantité OE (menigu) Boh. _ koltkost
Sp. cantidad ME —quantite(e) Pol. tlosé
Rum. cantitate NE quantity Russ. kolitestvo :
Ir. meit Du. hoeveelheid Skt. pra-mana-, part- Nir. méid OHG (managi) mana-, mana-, ete. W. maint MHG (menige) Av.
Br. ment NHG quantitdt
‘Quantity’ in the abstract is a sophis- ticated notion. It was expressed in Greek by rogérns, perhaps a coinage of Aristotle, meaning literally the ‘how- much-ness’, which the Romans rendered by the equivalent quantitas, whence, di- rectly or by further semantic borrowing, most of the European terms.
The nearest equivalent, preceding the adoption of these terms, would be the words for ‘great quantity or number’,
which might come to be used for ‘quan- tity’ in general, just as words for ‘great size’ furnished most of the words for ‘size’ (12.52). Some of them are quot- able for ‘quantity, amount’ or ‘number in the abstract, as Grk. a)j6os (‘amount of the penalty, ‘number’ of the ships etc.), Lat. magnitadd or multitado, Russ. mnozesivo, ete. Accordingly, such words are entered in the list (but in parentheses where abstract forms are lacking
916
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj
they are omitted from jut ‘op, since they are obvious {he discus ’ nonates of the words for gar (13.15) or ‘great, large iguchy i060). ar equivalents to ( 0 ne Am ia are NE amount, fr. vb. oe ie _ ‘mount’ (fr. OFr. amonter, u! vane i nd monte), hence ‘rise 1n quantity * aber’ (similarly Fr. montant, etc.) ; Lp amount’? (> Fr. at. st mme, N ; ie of summus ���highest’. 1, Grk. xoodrns (Aristot.), fr. mécos thow much?” which served as a model for
Ist, quantitas fr. quantus. Hence the
ther
Many of the words for ‘number’ are tomnected with the words for ‘reckon, tount', these of various sources. Some cS the notion of ‘arrangement, ‘er, or ‘distribution’. tot - apBuds, beside ynpiros ‘un- ie, Ze "Exdpiro. ‘picked sol- tthe : ® root of dpapicxw ‘fit to- Bags a its cognates in other lan- ay 4 ae reflect such second- benee ‘py arrange, reckon, count’, Rent, ad ’ ee through ‘arrange- t Rie Gs : Skt. rta- ‘suitable, "Secon ed time, season’, Lat. and &D, Tr ’ Judge » ratio ‘reckoning’, “it, OF rim ‘number’ (be-
lo 8 git 1 4), Mee 749 Walde-P. 1.75, Persson, Bei-
Foundation Chennai and eGangotri
=== IEC duðu
2561:du- (reduced element of duou, duð ‘two’, q. V.) Lat. du-plus; OE tū; Li. du; Per. du; G cf. Zu-ber “tub?
2622:duuoim, dat. of type *duuó, see duðu, etc. Gk. duoin; Go. twaim; OHG zweim; OCS cf. düvéma; Li. dviem; Latvian diviem, id.
2633:duəi, fem. form of duðu, q. v. Tokh. A we, B wi; Alb. dý; OBr. & Br. diu; W dwy; MHG zwei; OE twa; OCS dvé; Li. dvi. (Latv. divas, f. “2? is a ‘new’ formation). Cf. WP I, 817
2660:duindiló, ið — duðu, duuou, duo
2673:duðu, etc. Skt. dvitáh “second form of Agni'; dvitiyah ‘second’; Av. bityo; Ober, duvitiya-; Per. dütà; Tokh. A wät, B wate; Alb. i dytë, id. beside dys, aor. dyta ((repeat', vi: Umb. cf. duti (again': Alb. së dyti, id.)
12096:oKtou (okto, oKdo, oKdou, oKdmi) “eight. Cf. eK- (oK-) and duou (?). WP I, 173 Skt. astaü, astá (perh. 2 tetrads'. MacDonell); Av. asta; Per. hast (infl. of haft geven: Oss. ast; Tokh. A okát, B okt; Arm. ut, i-st.; Gk. októ; Lat. octó; Alb. tetë (aphetic w. added -të); Olr. ocht; Br. eiz; W wyth; Cor. eth; OHG ahtowi, pl.; MHG ehtewe, pl. beside aht, eht; Go. ahtau; OE eahta; ON átta; cf. vari- ants in OCS osmí (and com. Sl.); Li. aštuoni CG Lat. octoni ‘eight each"); Latv. astoni, id.
```


## [2026-09-05T20:24:08.342Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"DIADEM\" AHD_watkins1985.txt | head -3; echo \"== SKT\"; grep -n \"^DIAMETER\\|^DIAPHRAGM\\|^DIABETES\\|^DEVIL\\|^DOZEN\\|^BISCUIT\\|^TWO\\|^TWELVE\" SKT.txt | head -10",
 "description": "Check Watkins DIADEM and Skeat entries"
}
```


### [2026-09-05T20:24:08.399Z] TOOL RESULT

```
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
== SKT
```


## [2026-09-05T20:24:16.977Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:32:26.041Z] TOOL CALL #70: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build145.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dw%C3%B3h%E2%82%81\"\nW_BIS = \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4\"\nW_DAY = \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%87%DB%8C%D9%85\"\nW_DIA = \"https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%AC\"\nW_DIG = \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%DA%AF%D8%B1\"\nW_DVS = \"https://en.wiktionary.org/wiki/%D8%AF%D9%88%DB%8C%D8%B3%D8%AA\"\nW_IBL = \"https://en.wiktionary.org/wiki/%D8%A5%D8%A8%D9%84%D9%8A%D8%B3\"\nE_DDM = \"https://www.etymonline.com/word/diadem\"\nE_DVL = \"https://www.etymonline.com/word/devil\"\nE_DPL = \"https://www.etymonline.com/word/diploma\"\n\nPOK_Q = (\"POK_full.txt line 23722: 'Root / lemma: duō(u) ... Meaning: two ... Grammatical information: \"\n         \"m. (grammatical double form duuōu), duai n., besides duei-, duoh, dui-' with 'Page(s): 228-232' \"\n         \"at line 23974.\")\n\nnodes = []\n\ndef N(i, lang, words, verdict, der, der_fa, sources, refchk, cons, **extra):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": der, \"derivation_fa\": der_fa, \"sources\": sources,\n         \"ref_check\": refchk, \"consulted\": cons}\n    d.update(extra)\n    nodes.append(d)\n\n# ---------------- node 1 ----------------\nN(1, \"Avestan\", \"dva, duva; duva-dasa; dve-sate; duvitya-kara; biš\", \"plausible\",\n  \"Avestan duua-/dva- 'two' (nom.-acc. dual masc.) is the regular Iranian continuant of PIE *dwoh1, \"\n  \"matching Sanskrit dvau/dvā; Pokorny cites it in the first line of the lemma ('Old Indic m. dvau, dva \"\n  \"= Avestan dva'). duuadasa- 'twelve' is likewise attested (Bartholomae s.v. 'dvadasa- Adj. \\\"der zwölfte\\\"' \"\n  \"and 'der Zahl nach: dvadasa vītāra', BRT.txt lines 13962, 8443) and is the compound d(u)va + dasa 'ten' \"\n  \"that Pokorny equates with Greek δώδεκα. 'Two hundred' is not a single word but the phrase duye saite \"\n  \"(fem. dual of sata- 'hundred'), quoted by Bartholomae from Vd. 4.20 ('duye saite upaeananąm') and Yt. 19.7 \"\n  \"('dvaica saite dvaica hazaŋre'); Nourai's 'dve-sate' is that phrase, and Wiktionary derives NP دویست \"\n  \"straight from Avestan duuesate. Two items in this box are not right as labelled. (1) duvitya-kara is not \"\n  \"Avestan: Bartholomae's entry reads 'j. bitya-, g. daibitya-, p. duvitiya- Adj. \\\"der zweite\\\"' (BRT.txt \"\n  \"line 17263) and Mann has 'Av. bityō; OPer. duvitiya-' (IEC.txt line 2673), so the duvitiya- shape is the \"\n  \"Old Persian ordinal; the compound itself, *duvitiyam karam 'the second time/turn', is Darmesteter's \"\n  \"reconstruction, cited as Old Persian by Horn no. 595 on the very page Nourai gives (HRN p.132). \"\n  \"(2) Avestan biš means 'twice', not 'more': Pokorny lists it under '3. Multiplikativadverb dwis \\\"twice\\\": \"\n  \"Old Indic dvíḥ, Avestan biš, gr. δίς, Old Latin duis, Latin bis', and Bartholomae quotes 'biš hapta \"\n  \"puθrąm ... \\\"zweimal sieben junge Hunde\\\" V. 14.16' (BRT.txt line 10042). The sense 'more' belongs only \"\n  \"to the Persian descendant in the next box.\",\n  \"صورت اوستایی duua-/dva «دو» بازماندهٔ منظم *dwoh₁ هندواروپایی آغازین است و با سنسکریت dvau برابر می‌ایستد؛ \"\n  \"duuadasa- «دوازده» و عبارت duye saite «دویست» (دوگانِ مادینهٔ sata- «صد») هر دو در اوستا گواهی شده‌اند و \"\n  \"بارتولومه آنها را از وندیداد ۴٫۲۰ و یشت ۱۹٫۷ نقل می‌کند. اما دو نکته درست نیست: duvitya-kara اوستایی نیست؛ \"\n  \"بارتولومه صورت اوستایی را bitya-/daibitya- و صورت duvitiya- را پارسی باستان می‌داند، و ترکیب \"\n  \"*duvitiyam karam بازسازی دارمستتر است که هرن (ص ۱۳۲) آن را پارسی باستان می‌خواند. دیگر آنکه biš اوستایی \"\n  \"«دوبار» است نه «بیشتر»؛ پوکورنی آن را ذیل قید تکرارِ dwis «دوبار» در کنار δίς یونانی و bis لاتینی آورده و \"\n  \"معنی «بیشتر» تنها از آنِ بازماندهٔ فارسی است. پس ادعای نورایی در کلیت پذیرفتنی است ولی برچسب زبانی و \"\n  \"معنی دو واژه اصلاح می‌خواهد.\",\n  [W_PIE, W_DVS],\n  [{\"ref\": \"POK:230\", \"status\": \"supports\",\n    \"note\": \"Pokorny's lemma duō(u) 'two' runs pp.228-232 (POK_full.txt lines 23722-23974), so p.230 is inside it; \"\n            \"it gives 'Old Indic m. dvau, dva (ved. also duvau, duva) = Avestan dva', 'd(u)va-dasa 12 (= gr. δώδεκα)', \"\n            \"'2. ordinals: Old Indic dvitīya-, Avestan bitya-, dabitya-, Old pers. duvitiya- \\\"second\\\"' and \"\n            \"'3. Multiplikativadverb: dwis \\\"twice\\\": Old Indic dvíḥ, Avestan biš, gr. δίς, Old Latin duis, Latin bis'.\"},\n   {\"ref\": \"KLN:1669\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 leaf 884 (running heads 1668/1669) s.v. 'two': 'fr. I.-E. base *duwo-, *duwou-, *dwō(u)-, \"\n            \"\\\"two\\\", whence also OI. dvau, dva (masc.), dve (fem. and neut.), Avestic dva' — exactly the Avestan form of this box.\"},\n   {\"ref\": \"KLN:440\", \"status\": \"not_found\",\n    \"note\": \"Klein 1966 leaf 241 carries the running heads 440/441 and holds diabetes/diablerie/diabolic; there is no \"\n            \"Avestan numeral material on it. The page is right for nodes #15/#20, not for this box.\"},\n   {\"ref\": \"SOD:145\", \"status\": \"supports\",\n    \"note\": \"Gharib, SOD_pages.txt leaf 210 (printed p.144/145), entry 3673: 'δwʾ B, M — δwa — two (dwʾ) © <*d(u)wa' — \"\n            \"the Sogdian cognate with the Proto-Iranian preform Nourai's arrow assumes.\"}],\n  [{\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, BRT.txt lines 13962, 17263, 10042, 14891\", \"stance\": \"partial\",\n    \"note\": \"'j. dvadasa- Adj. \\\"der zwölfte\\\"'; 'j. bitya-, g. daibitya-, p. duvitiya- Adj. \\\"der zweite\\\"'; \"\n            \"'biš hapta puθrąm ... \\\"zweimal sieben junge Hunde\\\" V. 14.16'; 'duye saite upaeananąm ... V. 4.20'. \"\n            \"Supports dva, dvadasa and duye saite, but assigns duvitiya- to Old Persian and biš to 'twice'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 2673 s.v. duōu\", \"stance\": \"partial\",\n    \"note\": \"'duōu, etc. Skt. dvitáḥ; dvitīyaḥ \\\"second\\\"; Av. bityō; OPer. duvitiya-; Per. dūtā' — again Avestan bityō vs Old Persian duvitiya-.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_latin_index_pages.txt pdf page 284 s.v. TWO\", \"stance\": \"supports\",\n    \"note\": \"'DAE, DVA, DO (AVESTAN); DUVITIYA (OLD PERSIAN); DO (PAHLAVI)' with references to Pokorny and MacKenzie — \"\n            \"Aryanpur too splits the Avestan and Old Persian forms exactly as Bartholomae does.\"}])\n\n# ---------------- node 2 ----------------\nN(2, \"Persian\", \"do «دو ۱»; devîst «دویست»; dîgar, degar «دیگر ، دگر»; bîš 1 «بیش ۱»\", \"plausible\",\n  \"دو do 'two' < Middle Persian dō (MacKenzie: 'do [2, TLYN' < A tryn | M dw, N du] two'), from Old Iranian *duwa, \"\n  \"with the regular loss of the final vowel and of intervocalic -w-; Mo'in's footnote to the دو entry in Borhān \"\n  \"p.888 gives the Pahlavi and Avestan antecedents. دویست devīst 'two hundred' continues MP duwēst, itself the \"\n  \"univerbation of the Avestan phrase duuesate (duye saite), the Avestan diphthong -ai- giving MP -ē- and NP -ī- \"\n  \"(Wiktionary; Sogdian dwyst is the exact cognate). دیگر / دگر dīgar 'other, second' < MP dudīgar / didīgar 'second' \"\n  \"(MacKenzie: 'dudigar [dtykl | M dwdygr, N digar] second'), from Proto-Iranian *dwitīya-kara- 'the second turn'; \"\n  \"Horn no. 595 (p.132) sets out the chain 'dīger, dedīger \\\"anderer\\\" ... ap. *duvitīyam karam (Darmesteter) ... \"\n  \"phlv. datīgar', and Hübschmann's addendum on p.65 adds 'paz. dadīgar \\\"secondly, other\\\" ... Dieses paz. did ist \"\n  \"direct = ap. duvitiya- \\\"der zweite\\\"'. The dropping of the first syllable (*duwitīgar > dudīgar > dīgar) is the \"\n  \"same kind of haplology that gives دی from dudīg. بیش bīš 'more' is the weakest link: Middle Persian has wēš \"\n  \"'more' with initial w-, and Wiktionary derives it from MP wēš 'probably borrowed from Avestan biš \\\"twice\\\", from \"\n  \"daibitiia'. The b- of the New Persian form beside MP w- shows the word is not a plain phonetic inheritance, so \"\n  \"the tie to *dwo- is likely (via the adverb 'twice' > 'more') but not demonstrable.\",\n  \"«دو» از فارسی میانهٔ dō (مکنزی: do … N du) و آن از ایرانی باستان *duwa؛ «دویست» از فارسی میانهٔ duwēst که خودْ \"\n  \"یک‌واژه‌شدهٔ عبارت اوستایی duye saite است و ای‌کشیدهٔ فارسی میانه در فارسی نو به «ی» بدل شده (هم‌ریشه با سغدی dwyst). \"\n  \"«دیگر/دگر» از فارسی میانهٔ dudīgar «دومین» و آن از ایرانی *dwitīya-kara-؛ هرن در شمارهٔ ۵۹۵ (ص ۱۳۲) همین زنجیره را \"\n  \"می‌آورد و هوبشمان (ص ۶۵) صورت پازند dadīgar و برابری آن را با duvitiya- پارسی باستان تصریح می‌کند؛ افتادن هجای \"\n  \"نخست (dudīgar > dīgar) قلب و کاهش عادی فارسی است. اما «بیش» جای درنگ دارد: صورت فارسی میانه wēš است و \"\n  \"ویکی‌واژه آن را «احتمالاً وام‌گرفته از biš اوستایی به معنی دوبار» می‌داند؛ اختلاف w/b نشان می‌دهد که این واژه \"\n  \"میراث آوایی مستقیم نیست. پس سه واژهٔ نخست قطعی و «بیش» با احتیاط پذیرفتنی است.\",\n  [W_DVS, W_DIG, W_BIS],\n  [{\"ref\": \"BQT:888\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ vol. 2, BQT_v2_pages.txt leaf 348 = printed p.888 (running heads ۹۱۱ on leaf 371 and ۹۱۷ on \"\n            \"leaf 377 fix printed = leaf + 540). The page carries Moʿin's footnote to the cross-referenced headword دو: \"\n            \"«# دو - م اول (do)، پهلوی dō، از ...» with the Avestan form following.\"},\n   {\"ref\": \"BQT:902\", \"status\": \"partial\",\n    \"note\": \"Leaf 362 = p.902 is the opening of «بیان بیستم: در دال بی‌نقطه با های هوز» (the ده chapter); its etymological \"\n            \"footnotes are for ده/دهار, not دویست. The دو- compounds run a few pages earlier, so the page number is \"\n            \"roughly but not exactly the one wanted.\"},\n   {\"ref\": \"BQT:914\", \"status\": \"partial\",\n    \"note\": \"Leaf 374 = p.914 has دیگ، دیگ‌افزار، دیگ‌بر, with Moʿin's footnote citing Hübschmann for دیگ ('بقول هوبشمان \"\n            \"دیگ فارسی … از پارسی باستان'); the headword دیگر falls just after it.\"},\n   {\"ref\": \"HRN:132\", \"status\": \"supports\",\n    \"note\": \"Horn, HRN.txt leaf 153 = printed p.132, no. 595: 'dīger, dedīger (Vis und Rāmin) \\\"anderer\\\"; ap. *duvitīyam \"\n            \"karam (Darmesteter, Ét. ir. I, 150, 183); phlv. datīgar' — precisely Nourai's arrow duvitya-kara → dīgar.\"},\n   {\"ref\": \"HUB:65\", \"status\": \"supports\",\n    \"note\": \"Hübschmann, HUB.txt leaf 75 = printed p.65, addendum to no. 595: 'paz. dadīgar \\\"secondly, other\\\" Shk. 240 … \"\n            \"Dieses paz. did ist direct = ap. duvitiya- \\\"der zweite\\\".'\"}],\n  [{\"src\": \"PHD\", \"where\": \"MacKenzie, PHD_mackenzie.txt line 2004 and PHD.txt line 316\", \"stance\": \"supports\",\n    \"note\": \"'do [2, TLYN' < A tryn | M dw, N du] two' and 'dudigar [dtykl | M dwdygr, N digar] second'; the English index \"\n            \"(PHD.txt line 3548) has 'second didom, dudigar'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 595, p.132\", \"stance\": \"supports\", \"note\": \"see ref_check — Horn's own chain for dīgar.\"},\n   {\"src\": \"HUB\", \"where\": \"p.65, addendum to no. 595\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt pdf p.284 s.v. TWO\", \"stance\": \"supports\",\n    \"note\": \"Persian دو with Pahlavi DO, Avestan DVA, Old Persian DUVITIYA, referring to Pokorny and MacKenzie.\"}])\n\n# ---------------- node 3 ----------------\nN(3, \"Latin\", \"bi, bis; bis-coctus; duo; duo-decem\", \"confirmed\",\n  \"Latin duo 'two' continues *duwō directly (Pokorny: 'Latin duo (from *duō), f. duae (neologism)'). bis 'twice' is \"\n  \"from Old Latin duis < *dwis, the same adverb as Greek δίς and Avestan biš (Klein p.174: 'bis, adv., twice. — L. bis, \"\n  \"fr. OL. dvis, cogn. with OI. dvíḥ, Avestic bish, Gk. δίς'); the combining form is bi-. bis coctus 'twice cooked' \"\n  \"(two separate words in Latin, coctus being the participle of coquere) is the phrase behind biscuit, and Nourai's \"\n  \"cross-reference ☞Pekw for coctus is right (PIE *pekw- 'to cook'). 'duo-decem' is Nourai's transparent hyphenation; \"\n  \"the attested Latin word is duodecim 'twelve', duo + decem, and the ☞Dekm cross-reference is again correct.\",\n  \"duo لاتینی مستقیماً بازماندهٔ *duwō است و bis «دوبار» از لاتینی کهن duis و آن از *dwis؛ کلاین (ص ۱۷۴) همین را \"\n  \"می‌گوید و δίς یونانی و biš اوستایی را هم‌ریشهٔ آن می‌شمارد. عبارت bis coctus «دوبار پخته» سرچشمهٔ biscuit است و \"\n  \"duodecim «دوازده» از duo + decem. نگارش «duo-decem» تجزیهٔ خودِ نورایی است نه صورت گواهی‌شده. ادعای نورایی درست است.\",\n  [W_PIE],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. dwo- (AHD_watkins1985.txt line 413): 'II. Adverbial form *dwis ... 2. Latin bis (combining \"\n            \"form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT' and 'III. Inflected form *duwo. 1. Latin duo, two: DEUCE, DOZEN, \"\n            \"DUAL, DUET, DUO-; DUODECIMAL'.\"},\n   {\"ref\": \"KLN:175\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 leaf 103 (printed pp.174-175) has both 'bis, adv., twice. — L. bis, fr. OL. dvis' and 'biscuit, n. — \"\n            \"F. biscuit, fr. L. bis coctus, \\\"twice cooked\\\" ... fr. bis, \\\"twice\\\", and coctus, pp. of coquere, \\\"to cook\\\"'.\"}],\n  [{\"src\": \"POK\", \"where\": \"p.228-232 s.v. duō(u)\", \"stance\": \"supports\",\n    \"note\": \"'Latin duo (from *duō), f. duae'; 'Old Latin duis, Latin bis'; 'Italic du- in Latin du-bius, -plus, -plex, \"\n            \"-pondius, -centī'.\"},\n   {\"src\": \"KLN\", \"where\": \"pp.174-175\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt line 13217\", \"stance\": \"supports\",\n    \"note\": \"'fr. Gmc. twis- (Goth. twis- \\\"apart\\\"), IE *dwis in Lat. bis, early Lat. duis \\\"twice\\\": IE dwou- \\\"two\\\"'.\"}])\n\n# ---------------- node 4 ----------------\nN(4, \"French\", \"biscuit; douzaine\", \"confirmed\",\n  \"Old French bescuit / biscuit (12th c.) is a calque-loan of Latin bis coctus, the twice-baked bread that kept on \"\n  \"shipboard; French kept the two elements welded (bis + cuit, past participle of cuire < coquere). douzaine is douze \"\n  \"'twelve' (< Latin duodecim, with -o- from duo and regular loss of the medial -de-) plus the collective suffix -aine \"\n  \"(< Latin -ēna, as in dizaine, centaine); Klein s.v. dozen gives 'OF. dozaine, dosaine, douzaine (F. douzaine), fr. \"\n  \"douze, \\\"twelve\\\", fr. L. duodecim, \\\"twelve\\\", fr. duo, \\\"two\\\", and decem, \\\"ten\\\"'.\",\n  \"biscuit فرانسوی از عبارت لاتینی bis coctus «دوبار پخته» است (نان دوبارپختهٔ دریانوردان) و douzaine از douze «دوازده» \"\n  \"(از duodecim لاتینی) به‌علاوهٔ پسوند جمعی -aine (از -ēna لاتینی، مانند dizaine و centaine). کلاین ذیل dozen همین \"\n  \"زنجیره را می‌آورد. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"KLN:175\", \"status\": \"partial\",\n    \"note\": \"Klein pp.174-175 (leaf 103) carries biscuit ('F. biscuit, fr. L. bis coctus'); douzaine is treated in the same \"\n            \"work but under dozen (leaf ~256), not on p.175.\"}],\n  [{\"src\": \"KLN\", \"where\": \"pp.174-175 s.v. biscuit; s.v. dozen\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. dwo-, II.2 and III.1\", \"stance\": \"supports\",\n    \"note\": \"BISCUIT is listed under Latin bis and DOZEN under Latin duo, i.e. both French words are filed under this root.\"}])\n\n# ---------------- node 5 ----------------\nN(5, \"Persian\", \"(script only) بسکویت ، دوجین\", \"plausible\",\n  \"بسکویت beskovit is French biscuit taken into Persian in the late Qajar/early Pahlavi period along with the rest of \"\n  \"the European confectionery vocabulary; the Persian spelling with -و- renders French /ɥi/ and the final -t is the \"\n  \"French orthographic -t pronounced in the borrowing. دوجین dojin 'a dozen' is glossed by Moʿin «دوازده عدد ...؛ ستهٔ \"\n  \"دوازده‌تایی»; Nourai's French douzaine is possible, but the Persian shape /dojin/ with its -j- and final -in matches \"\n  \"Russian дюжина (itself borrowed from French douzaine) at least as well, and the word belongs to the trade vocabulary \"\n  \"in which Russian loans are common in Persian. The ultimate French/Latin origin is not in doubt; the immediate donor is.\",\n  \"«بسکویت» وام‌واژه‌ای است از biscuit فرانسوی که در اواخر دورهٔ قاجار همراه واژگان قنادی اروپایی وارد فارسی شد. \"\n  \"«دوجین» را معین «دوازده عدد» معنی می‌کند؛ خاستگاه نهایی آن بی‌گمان douzaine فرانسوی است، اما شکل آوایی /dojin/ با \"\n  \"дюжина روسی (که خود از فرانسه گرفته شده) سازگارتر می‌نماید و این واژه در زبان بازرگانی رواج یافته که در آن \"\n  \"وام‌واژه‌های روسی فراوان است. پس مسیر مستقیم وام‌گیری قطعی نیست هرچند اصل فرانسوی/لاتینی درست است.\",\n  [],\n  [{\"ref\": \"MON:1572\", \"status\": \"not_checked\",\n    \"note\": \"Only the two-volume abridgement of Moʿin is on disk, whose pagination differs from the six-volume print Nourai \"\n            \"cites, so p.1572 cannot be located. The abridgement does carry the headword «دوجین: دوازده عدد ...؛ ستهٔ \"\n            \"دوازده‌تایی» (MON_part1.txt), but has no entry for بسکویت.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دوجین\", \"stance\": \"partial\",\n    \"note\": \"«دوجین: (ق‌مر.) دوازده عدد ...، ستهٔ دوازده‌تایی» — the word and its meaning, without an origin tag in the abridgement.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, searched vols 1-2\", \"stance\": \"silent\",\n    \"note\": \"Neither بسکویت nor دوجین occurs; a 1652 dictionary cannot contain nineteenth-century European loans, so its \"\n            \"silence is expected and carries no weight against the arrow.\"}])\n\n# ---------------- node 6 ----------------\nN(6, \"English\", \"biscuit; dozen\", \"confirmed\",\n  \"Middle English bisquite/besquite is Old French biscuit, borrowed in the 14th c.; the modern English spelling was \"\n  \"re-Frenchified in the 16th c. (earlier bisket). dozen is ME dozeine from OF dozaine; Klein: 'dozen, n. — OF. dozaine, \"\n  \"dosaine, douzaine (F. douzaine), fr. douze, \\\"twelve\\\", fr. L. duodecim.' Watkins files both English words under dwo-.\",\n  \"biscuit انگلیسی در سدهٔ چهاردهم از فرانسوی گرفته شده (صورت میانه bisket که بعدها املای فرانسوی را بازیافت) و \"\n  \"dozen از dozaine فرانسوی کهن. کلاین و واتکینز هر دو واژه را ذیل همین ریشه می‌آورند. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"KLN:175\", \"status\": \"partial\",\n    \"note\": \"Klein pp.174-175 gives biscuit; the entry for dozen ('OF. dozaine ... fr. L. duodecim') stands elsewhere in the \"\n            \"same dictionary (KLN_1966.txt line 12186).\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. biscuit (p.175) and s.v. dozen\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. dwo-\", \"stance\": \"supports\",\n    \"note\": \"'Latin bis ... : BI-, BIS; BAROUCHE, BISCUIT' and 'Latin duo, two: DEUCE, DOZEN, DUAL, DUET, DUO-'.\"}])\n\n# ---------------- node 7 ----------------\nN(7, \"English\", \"bicycle; binary\", \"confirmed\",\n  \"binary is Late Latin binārius 'consisting of two', from bīnī 'two by two', which Watkins derives from the suffixed \"\n  \"form *dwis-no- (the same formation as Old English twinn 'twin'); it enters English in the 1590s of numbers and is \"\n  \"generalised in the 19th c. bicycle is a modern hybrid: French bicycle (1868) and English bicycle (1868) from Latin \"\n  \"bi- 'two' + Greek kuklos 'wheel', so only its first element belongs to this root — the box is right about the Latin \"\n  \"prefix but the word is a nineteenth-century coinage, not an inherited Latin word.\",\n  \"binary از binārius لاتینی متأخر و آن از bīnī «دوتا دوتا» است که واتکینز آن را از صورت پسونددار *dwis-no- می‌گیرد \"\n  \"(همان ساختی که در twin انگلیسی هست). bicycle واژه‌ای برساختهٔ سدهٔ نوزدهم است از پیشوند لاتینی -bi و kuklos یونانی \"\n  \"«چرخ»؛ پس تنها جزء نخست آن به این ریشه می‌رسد. ادعای نورایی در اصل درست است، با این یادآوری که bicycle واژهٔ \"\n  \"لاتینی موروثی نیست.\",\n  [],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. dwo-: '10. Suffixed form *dwis-no- in ... b. Latin bini, two by two, two each: BINAL, BINARY; \"\n            \"COMBINE'; BICYCLE falls under the prefix BI- listed at II.2.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwo-, II.2 and II.10b\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein leaf 100, p.169 s.v. bi-\", \"stance\": \"supports\",\n    \"note\": \"'bi-, pref. meaning \\\"two\\\". — L. bi-, \\\"twice, double\\\", fr. bis, \\\"twice\\\", cogn. with OI. dvi-, Gk. δι- (for \"\n            \"δϝι-), OE. twi-, \\\"twice, double\\\". See bis and cp. di-, \\\"two\\\", dis-, twi-, two. Cp. also binary, combine.'\"}])\n\n# ---------------- node 8 ----------------\nN(8, \"Greek\", \"di, dis; dia; di-ploos\", \"confirmed\",\n  \"Greek δίς 'twice' is *dwis, with the regular Greek loss of the digamma (Klein: 'Gk. δι- (for δϝι-)'), and δι- is its \"\n  \"combining form. διά 'through, across, apart' belongs here too, though less obviously: Wiktionary derives it 'from \"\n  \"*δισά (disá), from Proto-Indo-European *dwís', 'related to δίς (twice) and δύο (two)', with the -α remodelled on \"\n  \"μετά, παρά; Pokorny says the same at the end of the lemma (p.232, §6): 'Indo-Germanic additional form dis-: Latin \"\n  \"dis-, ... gr. δια (i.e. after μετα etc. filled in *δι[α]α), e.g. δια-σχίζω \\\"through\\\" : Latin discindo \\\"to tear \"\n  \"asunder\\\" (\\\"*split in the middle\\\")'. The semantic bridge is 'in two' > 'apart' > 'through, across'. διπλόος \"\n  \"'twofold' is *dwi-plo- (Watkins 12). One gloss slips: 'pamphlet' is not a sense of the adjective διπλόος but of the \"\n  \"derived neuter noun δίπλωμα, which the chart gets right in node #11.\",\n  \"δίς یونانی «دوبار» بازماندهٔ *dwis است با افتادن واو (δϝι- > δι-) و δι- صورت ترکیبی آن است. διά «از میان، در سرتاسر، \"\n  \"جدا» نیز به همین ریشه می‌رسد: ویکی‌واژه آن را از *δισά و در نهایت *dwís می‌داند و پوکورنی در پایان همین مادّه \"\n  \"(ص ۲۳۲) صریحاً διά را کنار dis- لاتینی می‌نهد؛ تحول معنایی «به دو نیم» ← «جدا» ← «از میان» است. διπλόος «دولا» از \"\n  \"*dwi-plo- است. تنها معنیِ «رساله» از آنِ اسم δίπλωμα است نه صفت διπλόος. ادعای نورایی درست است.\",\n  [W_DIA],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. dwo-: '3. Greek dis (combining form di-), twice: DI-1' and '12. Compound *dwi-plo-, twofold ... in \"\n            \"Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA'. The AHD index likewise files DI-1, DICHO-, DIDYMOUS under dwo-.\"}],\n  [{\"src\": \"POK\", \"where\": \"p.232, §6 of the lemma duō(u)\", \"stance\": \"supports\",\n    \"note\": \"'Indo Germanic additional form dis-: Latin dis-, ... gr. δια (i.e. after μετα etc filled in *δι[α]α), e.g. \"\n            \"δια-σχίζω \\\"through\\\" : Latin discindo \\\"to tear asunder, cut apart\\\" (\\\"*split in the middle\\\")'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein leaf 100 s.v. bi-; leaf 242 s.v. diadem\", \"stance\": \"supports\",\n    \"note\": \"'Gk. δι- (for δϝι-)'; the dia- entries all cross-refer to 'dia-' as a single prefix.\"}])\n\n# ---------------- node 9 ----------------\nN(9, \"Greek\", \"dia-dein, dia-děma\", \"confirmed\",\n  \"διαδέω 'to bind round, bind on either side' = διά + δέω 'to bind' (PIE *deh1(y)- 'to bind', Nourai's ☞Dě 1 and \"\n  \"Watkins's dē- 'to bind', under which the AHD index files DIADEM). The derived neuter διάδημα is 'band, fillet, royal \"\n  \"headband' — specifically the fillet worn by the Achaemenid kings, taken over by Alexander and his successors, which \"\n  \"is how a Greek word for a Persian object could later travel back east. Klein (p.443): 'diadem, n., crown; fillet. — \"\n  \"OF. diademe, fr. L. diadema, fr. Gk. διάδημα, \\\"band, fillet, royal headband\\\", fr. διαδεῖν, \\\"to bind on either \"\n  \"side\\\", fr. διά (see dia-) and δεῖν, \\\"to bind\\\"'. Etymonline reads διά here as 'across, through' rather than 'on two \"\n  \"sides', so Nourai's gloss 'tied on two sides' follows Klein and is a defensible but not the only rendering.\",\n  \"διαδέω یونانی «گِرد چیزی بستن» از διά و δέω «بستن» (ریشهٔ *deh₁- «بستن») ساخته شده و اسم آن διάδημα «نوار، سربند \"\n  \"شاهی» است؛ همان نوار سرِ شاهان هخامنشی که اسکندر و جانشینانش برگرفتند. کلاین (ص ۴۴۳) دقیقاً همین تحلیل را دارد. \"\n  \"ترجمهٔ نورایی «بسته‌شده از دو سو» از کلاین گرفته شده؛ اتیمانلاین διά را اینجا «از عرض، دورِ» می‌خواند. ادعای نورایی درست است.\",\n  [E_DDM],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"The AHD index (AHD_watkins1985.txt line 1424) files 'DIADEM dē-', i.e. Watkins hangs the word on the root of \"\n            \"δεῖν, not on dwo-; the διά element is what belongs here, and Watkins does put DI-1 under dwo-. So the AHD \"\n            \"supports the compound analysis but files the word under the second element.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 242 (pp.442-443) s.v. diadem\", \"stance\": \"supports\",\n    \"note\": \"'fr. Gk. διάδημα, \\\"band, fillet, royal headband\\\", fr. διαδεῖν, \\\"to bind on either side\\\", fr. διά (see dia-) \"\n            \"and δεῖν, \\\"to bind\\\", fr. I.-E. base *de(i)-, *dī-, \\\"to bind\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"index s.v. DIADEM\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 10 ----------------\nN(10, \"Persian\", \"dayhîm «دیهیم»\", \"confirmed\",\n  \"Persian دیهیم dayhīm 'crown, royal diadem' is Greek διάδημα, but it did not come in through books: the route is \"\n  \"Parthian dyd(y)m /dīδēm/ 'flower-crown, half-crown' → Middle Persian dīdēm / dīyēm → New Persian dayhīm, i.e. the \"\n  \"Greek word was taken over in the Arsacid period, its intervocalic -δ- weakened to -y-, and the New Persian spelling \"\n  \"shows a secondary -ه- (Wiktionary). Borhān-e Qāṭeʿ p.921 gives the sense the chart gives: «دیهیم ... تاجی که مخصوص \"\n  \"پادشاهان است ... و بعضی گویند دیهیم افسری بوده که آن را در قدیم جهت تیمن و تبرک بر بالای سر پادشاهان می‌آویخته‌اند؛ \"\n  \"کلاه مرصع را نیز گویند». Moʿin, in a footnote elsewhere in the same volume (p.1006), lists دیهیم together with درهم، \"\n  \"دینار، الماس as words 'اصلاً یونانی'. So the arrow is right; what the chart omits is the Parthian/Middle Persian relay.\",\n  \"«دیهیم» وام‌واژه‌ای است از διάδημα یونانی، اما نه به‌واسطهٔ کتاب: مسیر آن پارتی dīδēm «تاج گل، نیم‌تاج» ← فارسی \"\n  \"میانه dīdēm/dīyēm ← فارسی نو «دیهیم» است؛ یعنی وام‌گیری در دورهٔ اشکانی رخ داده، دالِ میان‌واکه‌ای به «ی» نرم شده و \"\n  \"«ه» در املای فارسی نو ثانوی است. برهان قاطع (ص ۹۲۱) همان معنی «تاج ویژهٔ پادشاهان» را می‌دهد و معین در حاشیه‌ای \"\n  \"دیگر (ص ۱۰۰۶) «دیهیم» را در کنار درهم و دینار و الماس «اصلاً یونانی» می‌خواند. ادعای نورایی درست است، جز آنکه \"\n  \"حلقهٔ پارتی و فارسی میانه در نمودار نیامده است.\",\n  [W_DAY, E_DDM],\n  [{\"ref\": \"BQT:921\", \"status\": \"supports\",\n    \"note\": \"Borhān vol. 2, BQT_v2_pages.txt leaf 381, whose running head OCRs as «۲۱» (= ۹۲۱): «دیهیم - بکسر ها، بر وزن \"\n            \"تعظیم، تاجی که مخصوص پادشاهان است ... وبعضی گویند دیهیم افسری بوده که آن را در قدیم جهت تیمن و تبرک بر بالای \"\n            \"سر پادشاهان می‌آویخته‌اند، کلاه مرصع را نیز گویند.» The gloss 'crown' is exactly Nourai's.\"},\n   {\"ref\": \"MON:1603\", \"status\": \"not_checked\",\n    \"note\": \"Only the two-volume Moʿin abridgement is on disk; its pagination differs from the six-volume print, so p.1603 \"\n            \"cannot be located. The abridgement does use دیهیم as a gloss word (s.v. افسر «تاج، دیهیم، کلاه پادشاهی» and \"\n            \"s.v. اکلیل).\"}],\n  [{\"src\": \"BQT\", \"where\": \"vol. 2 p.921; and Moʿin's footnote at p.1006 (leaf 463)\", \"stance\": \"supports\",\n    \"note\": \"p.1006 footnote: «... بنظر میرسد که مانند کلمات درهم و دینار و الماس و دیهیم و غیره اصلاً یونانی و از زوس \"\n            \"Zeus ... مشتق باشد» — Moʿin explicitly counts دیهیم among the Greek loans in Persian.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, searched for diadem / dydym\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no dīdēm entry; the Middle Persian form is known from Manichaean \"\n            \"and Parthian material rather than from the Book-Pahlavi glossary.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, searched 'Diadem'\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's Diadem references (pp. ~40, 180, 190) concern Armenian xoir and Old Persian xauda-, not دیهیم.\"}])\n\n# ---------------- node 11 ----------------\nN(11, \"Greek\", \"di-ploos\", \"confirmed\",\n  \"διπλόος / διπλοῦς 'twofold, double' is the compound *dwi-plo- ('two-fold'), the exact counterpart of Latin duplus, \"\n  \"with the second element from PIE *pel- 'to fold'. From it the verb διπλόω 'to double, to fold over' and from that \"\n  \"the neuter δίπλωμα 'anything folded double; a folded paper; a licence' — originally the folded sheet of a Roman \"\n  \"official pass. Klein (p.454): 'diploma, n. — L. diploma, fr. Gk. δίπλωμα, \\\"anything double, folded paper, license\\\", \"\n  \"fr. διπλοῦν, \\\"to bend double, to double\\\", fr. διπλόος, διπλοῦς, \\\"double\\\"'.\",\n  \"διπλόος «دولا» ترکیب *dwi-plo- است، برابر دقیق duplus لاتینی، که جزء دوم آن از ریشهٔ *pel- «تا کردن» است. از آن \"\n  \"فعل διπλόω «دولا کردن» و از این فعل اسم δίπλωμα «چیز تاشده، برگ تاشده، پروانه» ساخته شده که در اصل برگهٔ تاشدهٔ \"\n  \"گذرنامهٔ رسمی رومی بوده است. کلاین (ص ۴۵۴) همین را می‌گوید. ادعای نورایی درست است.\",\n  [E_DPL],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. dwo-, 12: 'Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, \"\n            \"twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS'.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 248 (pp.454-455) s.v. diploma\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. dwo-, 12\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 12 ----------------\nN(12, \"French\", \"diplôme; diplomate\", \"confirmed\",\n  \"French diplôme (1650s) is Latin diploma, taken over as a term of the new science of charters; from it Modern Latin \"\n  \"diplomaticus (1680s) and French diplomatique, first of documents ('agent diplomatique', an agent accredited by \"\n  \"letters patent), then of politics. diplomate is a back-formation of the 1790s from diplomatique in agent \"\n  \"diplomatique, cut to the model of aristocrate beside aristocratie (Klein; Etymonline). So the French box is the \"\n  \"hinge at which 'folded document' became 'diplomacy'.\",\n  \"diplôme فرانسوی (سدهٔ هفدهم) همان diploma لاتینی است که در دانش نوخاستهٔ سندشناسی به کار رفت؛ از آن \"\n  \"diplomaticus لاتینی نو و diplomatique فرانسوی پدید آمد که نخست وصف سند بود («agent diplomatique»، فرستاده‌ای که \"\n  \"با فرمانِ رسمی اعتبار می‌یابد) و سپس وصف سیاست. diplomate در دههٔ ۱۷۹۰ به قیاس aristocrate از aristocratie از \"\n  \"diplomatique ساخته شد. پس تحول معنایی «برگهٔ تاشده» ← «فرمان رسمی» ← «دیپلماسی» در فرانسه رخ داده است. \"\n  \"ادعای نورایی درست است.\",\n  [E_DPL],\n  [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this box.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 248 s.v. diplomacy, diplomat\", \"stance\": \"supports\",\n    \"note\": \"'diplomat, diplomate. — F. diplomate, back formation fr. diplomatique in agent diplomatique, \\\"diplomatic \"\n            \"agent\\\"'; 'diplomacy, n. — F. diplomatie, fr. diplomate; introduced into English by Edmund Burke'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. dwo-, 12\", \"stance\": \"supports\", \"note\": \"DIPLOMA listed under this root.\"}])\n\n# ---------------- node 13 ----------------\nN(13, \"Persian\", \"(script only) دیپلم ، دیپلمات\", \"confirmed\",\n  \"دیپلم and دیپلمات are French diplôme and diplomate, taken into Persian with the French-modelled schooling and \"\n  \"diplomatic service of the later Qajar period (Dār al-Fonūn and after); the whole French family came with them — \"\n  \"دیپلمه 'holder of a diploma', دیپلماتیک, دیپلماسی. Moʿin's entries confirm both senses: «دیپلم: گواهی‌نامه (تحصیلی)؛ \"\n  \"پروانه» and «دیپلمات: آنکه از امور سیاسی مطلع است؛ سیاستمدار». The final -e of French diplôme is dropped and the \"\n  \"circumflex vowel rendered by a short e, the normal treatment of French loans in Persian.\",\n  \"«دیپلم» و «دیپلمات» وام‌واژه‌های فرانسوی‌اند که با نظام آموزشی و دستگاه سیاسی فرانسوی‌مآبِ اواخر قاجار (دارالفنون و \"\n  \"پس از آن) وارد فارسی شدند و همراه خود «دیپلمه»، «دیپلماتیک» و «دیپلماسی» را آوردند. معین می‌نویسد: «دیپلم: \"\n  \"گواهی‌نامهٔ تحصیلی؛ پروانه» و «دیپلمات: آنکه از امور سیاسی مطلع است؛ سیاستمدار». افتادن -e پایانی و کوتاه‌شدن مصوت، \"\n  \"رفتار عادی فارسی با وام‌واژه‌های فرانسوی است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"MON:1590\", \"status\": \"partial\",\n    \"note\": \"The page cannot be checked (only the two-volume abridgement is on disk), but that abridgement has the entries: \"\n            \"«دیپلم: گواهی‌نامه (تحصیلی). پروانه.» «دییلمات: آنکه از امور سیاسی مطلع است؛ سیاستمدار، سائس.» «دیپلماتیک»، \"\n            \"«دیپلماسی»، «دیپلمه» (MON_part1.txt).\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دیپلم، دیپلمات، دیپلماتیک، دیپلماسی\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, searched vols 1-2\", \"stance\": \"silent\",\n    \"note\": \"absent, as expected of a 1652 dictionary; no bearing on a modern French loan.\"}])\n\n# ---------------- node 14 ----------------\nN(14, \"English\", \"diploma; diplomat\", \"plausible\",\n  \"Only half of this box came through French. diplomat (1813) is indeed French diplomate. diploma, however, entered \"\n  \"English in the 1640s straight from Latin: Klein has 'diploma, n. — L. diploma, fr. Gk. δίπλωμα', with no French \"\n  \"stage, and Etymonline agrees (Latin diploma, 'official document'). The adjective diplomatic likewise comes from \"\n  \"Modern Latin diplomaticus by way of French diplomatique, and diplomacy was introduced into English by Edmund Burke \"\n  \"from French diplomatie. So the arrow French → English is right for diplomat and wrong for diploma.\",\n  \"تنها نیمی از این جعبه از راه فرانسه آمده است. diplomat (۱۸۱۳) همان diplomate فرانسوی است، اما diploma در دههٔ ۱۶۴۰ \"\n  \"یکسره از لاتینی به انگلیسی رفته؛ کلاین می‌نویسد «diploma — L. diploma, fr. Gk. δίπλωμα» و هیچ حلقهٔ فرانسوی \"\n  \"نمی‌آورد. صفت diplomatic از diplomaticus لاتینی نو از راه diplomatique فرانسوی و اسم diplomacy را ادموند برک از \"\n  \"diplomatie فرانسوی وارد انگلیسی کرد. پس پیکان «فرانسوی ← انگلیسی» برای diplomat درست و برای diploma نادرست است؛ \"\n  \"ادعای نورایی با احتیاط پذیرفتنی است.\",\n  [E_DPL],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. dwo-, 12 lists DIPLOMA among the English derivatives of Greek diploos — but says nothing about the \"\n            \"route, which is where the chart slips.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 248 s.v. diploma, diplomat\", \"stance\": \"contradicts\",\n    \"note\": \"'diploma, n. — L. diploma, fr. Gk. δίπλωμα' (no French stage) beside 'diplomat, diplomate. — F. diplomate'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. dwo-, 12\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 15 ----------------\nN(15, \"Greek\", \"dia-bainein; dia-luein, dialuses; dia-phragna; dia-metros\", \"transcription_suspect\",\n  \"The four compounds are all real and all built on διά, but two of the forms as printed are wrong. διαβαίνειν 'to step \"\n  \"across, go through' gives διαβήτης, which Aretaeus of Cappadocia coined in the 2nd c. CE for the disease, 'lit. \"\n  \"\\\"that which causes a going through\\\" ... in allusion to the excessive urination' (Klein p.440) — Nourai's parenthesis \"\n  \"'liquid in diabetic patients' and his ☞Gwa (Watkins gwā- 'to go') are both right. διαλύειν 'to loosen apart' gives \"\n  \"διάλυσις 'separation, dissolution', which Thomas Graham took over for the chemical process in 1861 (Klein p.443); \"\n  \"the chart's 'dialuses' is a misprint for dialusis. 'dia-phragna' has no existence: the Greek word is διάφραγμα \"\n  \"'partition, barrier; the muscle which divides the thorax from the abdomen', from διαφράσσειν / διαφράγνυναι 'to \"\n  \"divide off, barricade' (Klein p.444) — the printed page 115 really does read 'dia-phragna', so the extraction is \"\n  \"faithful and the error is the book's; the gloss 'completely enclosed' also reverses the sense, which is 'fenced \"\n  \"off, partitioned'. διάμετρος (γραμμή) 'the line that measures across' is correct, and ☞Me (Watkins mē-2) is Watkins's \"\n  \"own filing.\",\n  \"هر چهار ترکیب واقعی‌اند و همه بر διά ساخته شده‌اند، اما دو صورت چاپی نادرست است. διαβαίνειν «از میان گذشتن» اسم \"\n  \"διαβήτης را می‌دهد که آرتایوس کاپادوکیایی در سدهٔ دوم میلادی برای این بیماری ساخت و اشاره به پرادراری دارد (کلاین \"\n  \"ص ۴۴۰). διαλύειν «از هم گشودن» اسم διάλυσις «جدایی، گسیختن» را می‌دهد که توماس گراهام در ۱۸۶۱ برای فرایند شیمیایی \"\n  \"به کار برد؛ «dialuses» غلط چاپی به‌جای dialusis است. «dia-phragna» اصلاً وجود ندارد: صورت درست διάφραγμα «دیوارهٔ \"\n  \"جداکننده، حجاب حاجز» از διαφράσσειν «سد کردن، جدا کردن» است. تصویر صفحهٔ ۱۱۵ نشان می‌دهد که خودِ کتاب «dia-phragna» \"\n  \"چاپ کرده است؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن. معنی «completely enclosed» نیز وارونه است و باید «جداشده، \"\n  \"بخش‌بندی‌شده» باشد. διάμετρος «خطی که از عرض اندازه می‌گیرد» درست است.\",\n  [E_DDM],\n  [{\"ref\": \"KLN:440\", \"status\": \"partial\",\n    \"note\": \"Klein 1966 leaf 241 carries the running heads 440/441 and does have diabetes there ('Medical L., fr. Gk. \"\n            \"διαβήτης, lit. \\\"that which causes a going through\\\", fr. διά ... and -βήτης ... from the stem of βαίνειν, \"\n            \"\\\"to go\\\" ... The disease was called διαβήτης by Aretaeus the Cappadocian ... in allusion to the excessive \"\n            \"urination'), but dialysis (leaf 242, pp.442-443), diaphragm (leaf 243, pp.444-445) and diameter (leaf 242) \"\n            \"stand on the following pages, not on 440.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaves 241-243 s.vv. diabetes, dialysis, diaphragm, diameter\", \"stance\": \"contradicts\",\n    \"note\": \"'diaphragm, n. ... Late L. diaphragma, fr. Gk. διάφραγμα, \\\"partition, barrier; muscle which divides the thorax \"\n            \"from the abdomen\\\", fr. διαφράγνυναι, διαφράσσειν, \\\"to divide off, barricade\\\"' — the correct form is \"\n            \"diaphragma, not the book's 'dia-phragna', and the sense is 'partitioned off', not 'completely enclosed'. \"\n            \"'dialysis, n. ... fr. Gk. διάλυσις, \\\"separation, dissolution\\\", fr. διαλύειν' — so dialusis, not 'dialuses'. \"\n            \"'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros, fr. Gk. διάμετρος (scil. γραμμή), lit. \\\"a \"\n            \"diametral line\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index, AHD_watkins1985.txt line 1424\", \"stance\": \"supports\",\n    \"note\": \"'DIABETES gwā-', 'DIALYSIS leu-1', 'DIAMETER mē-2', 'DIAPHRAGM bhrekw-' — the second element of each compound \"\n            \"is filed under a different root, exactly as Nourai's ☞Gwa, ☞Leu, ☞Me cross-references do; the di(a)- element \"\n            \"is what stays under dwo-.\"}],\n  error_in=\"book\", book_prints=\"dia-phragna\", correct_form=\"dia-phragma\")\n\n# ---------------- node 16 ----------------\nN(16, \"French\", \"(no words given)\", \"confirmed\",\n  \"The empty French box stands for diabète, dialyse, diaphragme (and diamètre), the French forms in which this Greek \"\n  \"medical vocabulary was standardised in the 18th-19th c. and from which it passed, with French pronunciation, into \"\n  \"Persian in the next box. French took them from Latin/New Latin, not from Greek directly.\",\n  \"این جعبهٔ خالی نمایندهٔ صورت‌های فرانسوی diabète، dialyse، diaphragme (و diamètre) است؛ همان قالبی که واژگان پزشکی \"\n  \"یونانی در سده‌های هجدهم و نوزدهم در فرانسه یافت و از همان‌جا با تلفظ فرانسوی به فارسی رسید. فرانسه این واژه‌ها را \"\n  \"از لاتینی و لاتینی نو گرفته است نه یکسره از یونانی. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this box.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.v. diameter\", \"stance\": \"supports\",\n    \"note\": \"'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros' — Klein documents the French stage for this family.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. دیابت، دیافراگم\", \"stance\": \"supports\",\n    \"note\": \"Moʿin enters the words in their French shape (دیابت، دیافراگم), the French forms being the immediate models.\"}])\n\n# ---------------- node 17 ----------------\nN(17, \"Persian\", \"dîyâbet «دیابت»; dîyâlîz «دیالیز»; dîyâfrâgm «دیافراگم»\", \"confirmed\",\n  \"All three are twentieth-century medical loans from French: diabète > دیابت, dialyse > دیالیز, diaphragme > \"\n  \"دیافراگم, the French nasal-free consonant clusters being kept and the French final -e dropped. Moʿin has «دیابت: \"\n  \"مرضی که به سبب ازدیاد مقدار قند تولید گردد» and «دیافراگم: سوراخ جلو دوربین عکاسی ...؛ (پز.) حجاب حاجز» — the \"\n  \"second entry shows the word had already acquired its photographic sense from French too. دیالیز is later and is not \"\n  \"yet in the abridged Moʿin.\",\n  \"هر سه وام‌واژهٔ پزشکی سدهٔ بیستم از فرانسه‌اند: diabète ← «دیابت»، dialyse ← «دیالیز»، diaphragme ← «دیافراگم»؛ \"\n  \"خوشه‌های همخوانی فرانسوی نگه داشته شده و -e پایانی افتاده است. معین می‌نویسد «دیابت: مرضی که …» و «دیافراگم: سوراخ \"\n  \"جلو دوربین عکاسی …؛ (پز.) حجاب حاجز» که نشان می‌دهد معنی عکاسی آن نیز از فرانسه آمده است. «دیالیز» متأخرتر است و \"\n  \"در تلخیص فرهنگ معین نیامده. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Nourai cites Moʿin without a page. The abridged Moʿin on disk has «دیابت: (پز.) مرضی که ...» and «دیافراگم: \"\n            \"(عک.) سوراخ جلو دوربین عکاسی ...، (پز.) حجاب حاجز» (MON_part1.txt); دیالیز is not in the abridgement.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. دیابت، دیافراگم\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vols 1-2\", \"stance\": \"silent\",\n    \"note\": \"none of the three occurs; expected for modern loans.\"}])\n\n# ---------------- node 18 ----------------\nN(18, \"Latin\", \"(no words given)\", \"confirmed\",\n  \"The empty Latin box is Medical/New Latin diabētēs, dialysis, diametros — the layer through which the Greek words \"\n  \"reached the western learned languages. Klein documents each: diabetes 'Medical L., fr. Gk. διαβήτης'; dialysis \"\n  \"'L., \\\"separation\\\", fr. Gk. διάλυσις'; diameter '... fr. L. diametros, fr. Gk. διάμετρος'.\",\n  \"این جعبهٔ خالی نمایندهٔ صورت‌های لاتینی/لاتینی نوِ diabētēs، dialysis و diametros است؛ همان لایه‌ای که واژگان یونانی \"\n  \"از راه آن به زبان‌های علمی اروپایی رسیده‌اند. کلاین برای هر سه همین را ثبت کرده است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins's dwo- entry does not itemise these words (his index files them under gwā-, leu-1, mē-2), but the Latin \"\n            \"relay is not in question.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaves 241-243\", \"stance\": \"supports\",\n    \"note\": \"'diabetes, n. ... Medical L., fr. Gk. διαβήτης'; 'dialysis, n. ... L., \\\"separation\\\", fr. Gk. διάλυσις'; \"\n            \"'diameter ... fr. L. diametros, fr. Gk. διάμετρος'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index line 1424\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 19 ----------------\nN(19, \"English\", \"diabetes; dialysis; diameter\", \"plausible\",\n  \"diabetes (1560s) and dialysis (1580s in rhetoric, 1861 in chemistry) did come into English from Latin, as the chart \"\n  \"draws it. diameter did not: Klein gives 'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros', i.e. the word \"\n  \"reached Middle English (late 14th c., Chaucer) through Old French, and the same is true of the whole geometrical \"\n  \"vocabulary of that date. The box is therefore right for two words of three.\",\n  \"diabetes (سدهٔ شانزدهم) و dialysis (نخست در بلاغت و از ۱۸۶۱ در شیمی) همان‌گونه که نمودار نشان می‌دهد از لاتینی به \"\n  \"انگلیسی رفته‌اند، اما diameter چنین نیست: کلاین می‌نویسد «diameter — OF. diametre, fr. L. diametros»؛ یعنی این واژه \"\n  \"در اواخر سدهٔ چهاردهم از راه فرانسوی کهن به انگلیسی میانه رسیده، چنان‌که کل واژگان هندسی آن دوره. پس دو واژه از سه \"\n  \"واژه درست است و ادعای نورایی با احتیاط پذیرفتنی است.\",\n  [],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins lists the English words but not their route; the route is what the chart gets partly wrong.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaves 241-242 s.vv. diabetes, dialysis, diameter\", \"stance\": \"contradicts\",\n    \"note\": \"'diameter, n. — OF. diametre (F. diamètre), fr. L. diametros' — an Old French, not a direct Latin, transmission.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index line 1424\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 20 ----------------\nN(20, \"Greek\", \"dia-ballein; diabolos\", \"confirmed\",\n  \"διαβάλλειν is literally 'to throw across/through', hence 'to set at variance, to attack with words, to slander' \"\n  \"(διά + βάλλειν, Nourai's ☞Gwel 1 = Watkins gwelə-1 'to throw', under which the AHD index files DEVIL and DIABOLIC). \"\n  \"The agent noun διάβολος 'slanderer, accuser' is the word the Septuagint chose to render Hebrew śāṭān 'the accuser', \"\n  \"and Ecclesiastical Greek then made it the name of the Devil — the semantic step that carries the whole rest of this \"\n  \"branch, into Latin, into Germanic, and into Arabic.\",\n  \"διαβάλλειν به‌لفظ «از این‌سو به آن‌سو افکندن» است و از آنجا «میان دو کس افکندن، بدگویی کردن، تهمت زدن» (διά + \"\n  \"βάλλειν). اسم فاعل آن διάβολος «بدگو، تهمت‌زن» همان واژه‌ای است که ترجمهٔ سبعینی برای «شیطان» عبری (śāṭān «متهم‌کننده») \"\n  \"برگزید و یونانی کلیسایی آن را نامِ ابلیس کرد؛ همین تحول معنایی است که تمام شاخهٔ لاتینی، ژرمنی و عربی این نمودار بر \"\n  \"آن استوار است. ادعای نورایی درست است.\",\n  [E_DVL],\n  [{\"ref\": \"KLN:440\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 leaf 241 (running heads 440/441): 'diablerie, n., devilry. — F., fr. diable, \\\"devil\\\", fr. Eccles. \"\n            \"L. diabolus, fr. Eccles. Gk. διάβολος, \\\"devil\\\"', with the full analysis on the facing leaf s.v. devil: \"\n            \"'fr. Gk. διάβολος, \\\"slanderer\\\", fr. διαβάλλειν, \\\"to throw across; to attack; to calumniate, slander\\\", \"\n            \"fr. διά (see dia-) and βάλλειν, \\\"to throw\\\"'.\"},\n   {\"ref\": \"AHD:361\", \"status\": \"not_checked\",\n    \"note\": \"A page of the main 1975/76 American Heritage Dictionary (not the Indo-European appendix), which is not openly \"\n            \"readable; p.361 in that edition falls in the d- range and would be the DEVIL entry. The Watkins appendix \"\n            \"instead files DEVIL and DIABOLIC under gwelə-1, exactly Nourai's ☞Gwel 1.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaves 240-241 s.vv. devil, diablerie, diabolic\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index, AHD_watkins1985.txt line 1424\", \"stance\": \"supports\",\n    \"note\": \"'DEVIL gwelə-1', 'DIABOLIC gwelə-1' — the βάλλειν element under the throwing root, the διά element under dwo-.\"}])\n\n# ---------------- node 21 ----------------\nN(21, \"Arabic\", \"eblis, iblis\", \"confirmed\",\n  \"Arabic إبليس Iblīs, the Qurʾānic name of the Devil, is not attested before the Qurʾān. Jeffery's discussion on the \"\n  \"page Nourai cites (FVQ p.48) argues it is Greek διάβολος in its Christian sense: 'It is in this sense that [Iblīs] \"\n  \"appears in the Qurʾān, so we are doubly justified in looking for a Christian origin for the word. One theory is that \"\n  \"it came through the Syriac, the [d] being taken as the genitive particle ... The alternative is that it came into \"\n  \"Arabic directly from the Greek, and was used by the Arabic-speaking Christians associated with the Byzantine \"\n  \"Church.' Klein s.v. Eblis says the same: 'Arab. Iblīs, aphetic for Gk. διάβολος ... It is very probable that Gk. \"\n  \"διάβολος came into Arabic through the medium of Syriac and that the first syllable of the Greek word was mistaken \"\n  \"for the Syriac genitive particle di and subsequently dropped.' The rival native derivation from the root ب-ل-س \"\n  \"(ʾablasa 'to despair') is an Arab grammarians' etymology; the ʾifʿīl pattern is normally reserved for foreign words, \"\n  \"which tells against it. Nourai's direct Greek → Arabic arrow matches Jeffery's second alternative; the Syriac relay \"\n  \"is the more usual view and is missing from the chart.\",\n  \"«ابلیس» نام قرآنی شیطان است و پیش از قرآن گواهی ندارد. جفری در همان صفحه‌ای که نورایی ارجاع داده (ص ۴۸) آن را \"\n  \"διάβολος یونانی در معنای مسیحی‌اش می‌داند و دو راه پیشنهاد می‌کند: یکی از راه سریانی، که در آن هجای نخست (di-) به \"\n  \"غلط حرف اضافهٔ اضافی سریانی d- پنداشته و افتاده است، و دیگری وام‌گیری مستقیم از یونانی به دست مسیحیان عرب‌زبان. \"\n  \"کلاین نیز ذیل Eblis همین را می‌گوید. ریشه‌شناسی رقیب، یعنی اشتقاق از ریشهٔ «ب‌ل‌س» (أبلس «نومید شد»)، ریشه‌شناسی \"\n  \"نحویان عرب است و وزن «إفعیل» معمولاً ویژهٔ واژه‌های بیگانه است و همین بر ضد آن گواهی می‌دهد. پیکان مستقیم \"\n  \"«یونانی ← عربی» نورایی با گزینهٔ دوم جفری می‌خواند؛ واسطهٔ سریانی که رأی رایج‌تر است در نمودار نیامده. ادعای نورایی درست است.\",\n  [W_IBL],\n  [{\"ref\": \"FVQ:48\", \"status\": \"supports\",\n    \"note\": \"Jeffery, FVQ_pages.txt leaf 65 = printed p.48 (printed = leaf − 17): the whole page is the Iblīs discussion, \"\n            \"quoted above, with parallels 'for διαφωνία', 'for δικαστής', 'for δυσεντερία' showing the same Syriac \"\n            \"mis-division of an initial di-.\"},\n   {\"ref\": \"BQT:83\", \"status\": \"supports\",\n    \"note\": \"Borhān vol. 1, BQT_v1_pages.txt leaf 293 = printed p.83, Moʿin's footnote 5: «ابلیس - ابن‌درید نوشته: اگر ابلیس \"\n            \"عربی باشد اشتقاق آن از ابلس یبلس ... است ... ابلیس از کلمهٔ یونانی διάβολος بمعنی کذاب و نمام که از نامهای \"\n            \"شیطان است گرفته شده، «نفیسی»، «جفری ۴۷-۴۸».» Moʿin states Nourai's claim and cites the very Jeffery pages.\"}],\n  [{\"src\": \"FVQ\", \"where\": \"Jeffery p.48\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 270 (printed pp.497-498) s.v. Eblis\", \"stance\": \"supports\",\n    \"note\": \"'Eblis, n., the prince of the fallen angels (Arabian religion). — Arab. Iblīs, aphetic for Gk. διάβολος, \"\n            \"\\\"slanderer\\\", in Eccles. Gk. \\\"devil\\\". It is very probable that Gk. διάβολος came into Arabic through the \"\n            \"medium of Syriac and that the first syllable of the Greek word was mistaken for the Syriac genitive particle \"\n            \"di and subsequently dropped.'\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1 p.83, Moʿin's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 22 ----------------\nN(22, \"Persian\", \"eblîs «ابلیس»\", \"confirmed\",\n  \"Persian ابلیس eblīs is the Arabic word taken over unaltered with the Qurʾān and Islamic learning from the 8th c. on; \"\n  \"it stands in Persian beside the inherited اهریمن and the equally Arabic شیطان, and is the name rather than the \"\n  \"common noun (شیطان being generalisable, ابلیس not). Borhān's headword and Moʿin's footnote on the same page (p.83) \"\n  \"are the source Nourai cites, and they trace the word beyond Arabic to Greek διάβολος — so this is a Greek word that \"\n  \"reached Persian by an Arabic detour, not from Byzantium directly.\",\n  \"«ابلیس» فارسی همان واژهٔ عربی است که از سدهٔ دوم هجری با قرآن و دانش اسلامی بی‌تغییر وارد فارسی شد و در کنار \"\n  \"«اهریمن» ایرانی و «شیطان» عربی نشست؛ برخلاف «شیطان» اسم خاص است نه اسم عام. مدخل برهان قاطع و حاشیهٔ معین در همان \"\n  \"صفحه (ص ۸۳) که مأخذ نورایی است، واژه را از عربی فراتر برده و به διάβολος یونانی می‌رساند. پس این واژه‌ای یونانی است \"\n  \"که با میانجی عربی به فارسی رسیده، نه مستقیم از بیزانس. ادعای نورایی درست است.\",\n  [W_IBL],\n  [{\"ref\": \"BQT:83\", \"status\": \"supports\",\n    \"note\": \"Borhān vol. 1 leaf 293 = p.83 carries the Persian headword and Moʿin's etymological footnote quoted at node #21.\"}],\n  [{\"src\": \"BQT\", \"where\": \"vol. 1 p.83\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt\", \"stance\": \"silent\",\n    \"note\": \"The abridged Moʿin has no separate ابلیس entry with an origin tag; the full six-volume edition (and the \"\n            \"Aʿlām volumes) treat it under the proper names.\"}])\n\n# ---------------- node 23 ----------------\nN(23, \"Latin\", \"(no words given)\", \"confirmed\",\n  \"The empty Latin box is Ecclesiastical/Late Latin diabolus, borrowed from Ecclesiastical Greek διάβολος in the \"\n  \"earliest Christian Latin (Tertullian onward) and kept by Jerome in the Vulgate for Hebrew śāṭān. It is the source of \"\n  \"Italian diavolo, Old Provençal/French/Catalan diable, Spanish diablo, Portuguese diabo and Gothic diabaúlus, and of \"\n  \"the Germanic words in the next box.\",\n  \"این جعبهٔ خالی نمایندهٔ diabolus لاتینی کلیسایی است که در کهن‌ترین لاتینی مسیحی (از ترتولیان به بعد) از διάβολος \"\n  \"یونانی وام گرفته شد و ژروم در ترجمهٔ وولگاتا آن را برابر «شیطان» عبری نگه داشت. همین صورت سرچشمهٔ diavolo ایتالیایی، \"\n  \"diable فرانسوی و کاتالانی، diablo اسپانیایی، diabo پرتغالی و diabaúlus گوتی است. ادعای نورایی درست است.\",\n  [E_DVL],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"The Watkins index files DEVIL under gwelə-1 rather than dwo-; the Latin relay itself is uncontroversial and is \"\n            \"set out in Klein.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 240 s.v. devil\", \"stance\": \"supports\",\n    \"note\": \"'Cp. also It. diavolo, Provenç., F., Catal. diable, Sp. diablo, Port. diabo, Goth. diabaulus, which all derive \"\n            \"fr. Eccles. L. diabolus.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index line 1424\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 24 ----------------\nN(24, \"English\", \"devil\", \"confirmed\",\n  \"Old English dēofol / dēoful 'a devil' was borrowed from Late Latin diabolus in the conversion period (7th-8th c.), \"\n  \"well before the Norman Conquest, and gives ME devel > devil; the -f- is the West Germanic voicing of intervocalic \"\n  \"Latin -b-. Klein: 'devil, n. — ME. devel, fr. OE. deofol, deoful, fr. Eccles. L. diabolus, fr. Eccles. Gk. διάβολος, \"\n  \"\\\"devil\\\" ... OHG. tiufal ... is a Goth. loan word.' Etymonline adds that in the Greek Bible diabolos was a \"\n  \"loan-translation of Hebrew satan, and that Latin and Germanic blurred the distinction between diabolus and daemon.\",\n  \"«deofol» انگلیسی کهن در دورهٔ مسیحی‌شدن (سده‌های هفتم و هشتم میلادی) و پیش از فتح نورمن از diabolus لاتینی متأخر وام \"\n  \"گرفته شد و از راه devel انگلیسی میانه به devil رسید؛ «f» آن نتیجهٔ واک‌دارشدن «b» میان‌واکه‌ای لاتین در ژرمنی غربی \"\n  \"است. کلاین همین زنجیره را می‌آورد و می‌افزاید که tiufal آلمانی علیای کهن خود وام‌واژه‌ای گوتی است. ادعای نورایی درست است.\",\n  [E_DVL],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins's index has 'DEVIL gwelə-1'; his dwo- entry does not list DEVIL, because he files the compound under \"\n            \"its second element. The διά element is nevertheless this root.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 240 (pp.438-439) s.v. devil\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins index line 1424\", \"stance\": \"partial\", \"note\": \"see ref_check.\"}])\n\n# ---------------- node 25 ----------------\nN(25, \"Germanic\", \"twai\", \"confirmed\",\n  \"Proto-Germanic *twai (masc. nom.), f. *twōz, n. *twa, is the regular outcome of PIE *dwoh1 with Grimm's Law d > t \"\n  \"and loss of the *-w- after the diphthong; it is attested as Gothic twai, twōs, twa, and continued by Old Norse \"\n  \"tveir, Old English twēgen / twā, Old High German zwēne / zwō / zwei. Pokorny: 'Gothic m. twai, f. twos, n. twa. Old \"\n  \"Norse tueir m., tuær f., tuau n. Old English tu m., twa f. (= Old Indic dve)'. Nourai's 'twai' is the Gothic \"\n  \"nominative used, as often in the book, to stand for the Germanic form.\",\n  \"*twai ژرمنی آغازین (نرینه، فاعلی) بازماندهٔ منظم *dwoh₁ است: «د» هندواروپایی بنابر قانون گریم به «ت» بدل شده و «و» \"\n  \"پس از مصوت مرکب افتاده است. این صورت در گوتی twai (مادینه twōs، خنثی twa) گواهی شده و در نورس کهن tveir، انگلیسی \"\n  \"کهن twēgen/twā و آلمانی علیای کهن zwēne/zwō/zwei ادامه یافته است. پوکورنی همین فهرست را می‌آورد. صورت «twai» در \"\n  \"کتاب، چنان‌که شیوهٔ نورایی است، همان فاعلیِ گوتی است که به‌جای صورت ژرمنی نشسته. ادعای نورایی درست است.\",\n  [W_PIE],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins s.v. dwo-: 'I. Variant form duwo. 1. Germanic *twa, two, in: a. Old English twā, two ...; b. Old English \"\n            \"twēgen, two ...: TWAIN.'\"}],\n  [{\"src\": \"POK\", \"where\": \"p.228-232, POK_full.txt line 23763\", \"stance\": \"supports\",\n    \"note\": \"'Gothic m. twai, f. twos, n. twa. Old Norse tueir m., tuær f., tuau n. Old English tu m., twa f. (= Old Indic dve).'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 884 (pp.1668-1669) s.v. two\", \"stance\": \"supports\",\n    \"note\": \"'... ON. tveir (masc.), tvær (fem.), tvau (neut.) ... Goth. twai (masc.), twos (fem.), twa (neut.), fr. I.-E. \"\n            \"base *duwo-, *duwou-, *dwō(u)-, \\\"two\\\".'\"}])\n\n# ---------------- node 26 ----------------\nN(26, \"English\", \"two; twelve; twenty; twice; twin; between\", \"confirmed\",\n  \"Every one of the six is in Watkins's dwo- entry. two < OE twā (fem./neut.), the masculine twēgen surviving as twain; \"\n  \"twelve < Germanic *twa-lif- 'two left (over from ten)', the second element being the root of Gothic -laibjan / Latin \"\n  \"linquere 'to leave', whence OE twelf; twenty < Germanic *twēgentig 'twice ten' (OE twēntig); twice < OE twiga, \"\n  \"twigea 'twice' with the adverbial genitive -es added in Middle English (ME twies); twin < OE twinn, getwinn from \"\n  \"*dwis-no- (the exact counterpart of Latin bīnī); between < OE betwēonum, be- 'by' + the dative plural of tweon, \"\n  \"related to Gothic tweihnai 'two each', i.e. 'at the middle point of two'. All six are inherited, not borrowed, which \"\n  \"is why the box needs no reference.\",\n  \"هر شش واژه در مدخل dwo- واتکینز آمده است: two از twā انگلیسی کهن (صورت نرینهٔ twēgen در twain مانده)؛ twelve از \"\n  \"*twa-lif- ژرمنی «دوتا مانده از ده» که جزء دومش هم‌ریشهٔ linquere لاتینی «واگذاشتن» است؛ twenty از *twēgentig «دو \"\n  \"ده»؛ twice از twiga انگلیسی کهن با پسوند قیدی -es؛ twin از *dwis-no- که برابر دقیق bīnī لاتینی است؛ و between از \"\n  \"betwēonum یعنی be- «به» و صورت دربرداشتِ tweon، هم‌ریشه با tweihnai گوتی «دوتا دوتا»، به معنی «در میانهٔ دو». همهٔ \"\n  \"این‌ها میراثی‌اند نه وام‌واژه، و از همین رو نمودار برای این جعبه ارجاعی نمی‌دهد. ادعای نورایی درست است.\",\n  [W_PIE],\n  [{\"ref\": \"none\", \"status\": \"not_checked\",\n    \"note\": \"the chart gives no reference for this box; the parent box's AHD reference covers it, and Watkins lists all six words.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwo- (AHD_watkins1985.txt line 413)\", \"stance\": \"supports\",\n    \"note\": \"'Old English twā, two: TWO'; '*twa-lif-, \\\"two left (over from ten),\\\" twelve ... TWELFTH, TWELVE'; \"\n            \"'*twēgentig, \\\"twice ten\\\" ... TWENTY'; 'Germanic *twiyes in Old English twige, twiga, twice: TWICE'; \"\n            \"'*twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN'; '*bi-twihna and *bi-twisk, \\\"at the \"\n            \"middle point of two\\\" ... BETWEEN, BETWIXT'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 leaves 99, 883-884\", \"stance\": \"supports\",\n    \"note\": \"'between, prep. and adv. — ME. bitweonen ... fr. OE. betweonum, fr. be-, \\\"by\\\", and tweonum, dative pl. of \"\n            \"tweon, \\\"double, twain\\\", which is rel. to Goth. tweihnai, \\\"two each\\\", fr. twa, \\\"two\\\"'; 'twelve ... \"\n            \"compounds meaning lit. \\\"two left after (ten)\\\"'; 'twenty ... lit. meaning \\\"two tens\\\"'; 'twin ... cogn. with \"\n            \"L. bini, \\\"two each\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt line 13217\", \"stance\": \"supports\",\n    \"note\": \"'fr. Gmc. twis- (Goth. twis- \\\"apart\\\"), IE *dwis in Lat. bis, early Lat. duis \\\"twice\\\": IE dwou- \\\"two\\\"'.\"}])\n\nentry = {\n    \"entry\": 0,\n    \"root\": \"Dwo\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *dwóh₁ (older notation *duwō(u), *dwō(u)) 'two' — Pokorny 228-232 duō(u); Watkins/AHD dwo-\",\n    \"note\": (\n        \"The root box is right on all three counts: Pokorny's lemma is 'duō(u), Meaning: two', 'Page(s): 228-232', so \"\n        \"Nourai's POK:230 points inside it, and Watkins's appendix has 'dwo-. Two. ... [Pok. duō(u)- 228.]'. The \"\n        \"language label 'Indo-European' and the gloss 'two' need no correction. The chart's architecture is also right \"\n        \"where it is least obvious: putting the whole Greek δια- family under 'two' looks odd, but Pokorny himself ends \"\n        \"this lemma (p.232, §6) by deriving Greek δια from the extended form *dis- < *dwis-, alongside Latin dis-, and \"\n        \"Wiktionary reconstructs διά 'from *δισά, from Proto-Indo-European *dwís'. Four things need correcting in the \"\n        \"branches rather than the root. (1) Node #1 files duvitya-kara as Avestan; Bartholomae, Mann and Aryanpur all \"\n        \"give the Avestan ordinal as bitya-/daibitya- and duvitiya- as Old Persian, and Horn (the page Nourai cites) \"\n        \"calls *duvitiyam karam Old Persian too. (2) In the same box Avestan biš is glossed 'more'; it means 'twice' \"\n        \"(Pokorny's Multiplikativadverb dwis; Bartholomae's 'biš hapta ... zweimal sieben'), the sense 'more' belonging \"\n        \"only to Persian bīš, whose link to it Wiktionary itself calls 'probably'. (3) Node #15 prints 'dia-phragna', \"\n        \"which is no Greek word: the form is διάφραγμα, and the printed page 115 shows the error is the book's, not the \"\n        \"extraction's; 'dialuses' for dialusis is a second slip in the same box. (4) Two of the English boxes route \"\n        \"words through the wrong intermediary: diploma came into English straight from Latin, not through French \"\n        \"(node #14), and diameter came through Old French, not straight from Latin (node #19). Everything else — the \"\n        \"Latin and French biscuit/dozen chain, the whole diadem → dayhīm and diabolos → Iblīs branches, and all six \"\n        \"Germanic words — checks out, and on the two most interesting Persian nodes Nourai's own references (Borhān \"\n        \"p.83 with Moʿin's footnote, Jeffery p.48, Borhān p.921, Horn p.132, Hübschmann p.65) say precisely what his \"\n        \"arrows say.\"\n    ),\n    \"note_fa\": (\n        \"خودِ ریشه بی‌گمان درست است: پوکورنی مادّهٔ duō(u) «دو» را در صفحات ۲۲۸–۲۳۲ آورده و ارجاع نورایی (ص ۲۳۰) درون \"\n        \"همان دامنه است؛ واتکینز نیز در پیوست فرهنگ American Heritage همان را با «dwo-. Two» ثبت کرده است. برچسب \"\n        \"«هندواروپایی» و معنی «دو» هر دو درست‌اند. ساختار نمودار نیز در جایی که غریب می‌نماید درست است: نهادنِ همهٔ \"\n        \"خانوادهٔ یونانی -δια ذیل «دو» عجیب به نظر می‌رسد، اما پوکورنی خود در پایان همین مادّه (ص ۲۳۲) διά را از \"\n        \"*dis- < *dwis- می‌گیرد و ویکی‌واژه نیز آن را از *δισά و *dwís می‌داند. چهار لغزش در شاخه‌ها هست: \"\n        \"۱) duvitya-kara اوستایی نیست بلکه duvitiya- پارسی باستان است (بارتولومه، مان، آریان‌پور و خودِ هرن در همان \"\n        \"صفحهٔ ۱۳۲)؛ ۲) biš اوستایی «دوبار» است نه «بیشتر»، و معنی «بیشتر» تنها از آنِ «بیشِ» فارسی است که پیوندش با \"\n        \"این ریشه را ویکی‌واژه هم «احتمالی» می‌خواند؛ ۳) «dia-phragna» واژهٔ یونانی نیست و صورت درست διάφραγμα است — \"\n        \"تصویر صفحهٔ ۱۱۵ نشان می‌دهد که خطا از چاپِ کتاب است نه از خوانش اسکن، و «dialuses» به‌جای dialusis لغزش دوم \"\n        \"همان جعبه است؛ ۴) در دو جعبهٔ انگلیسی مسیر وام‌گیری نادرست است: diploma یکسره از لاتینی به انگلیسی رفته نه از \"\n        \"راه فرانسه، و diameter برعکس از راه فرانسوی کهن آمده نه مستقیم از لاتینی. باقی نمودار — زنجیرهٔ \"\n        \"biscuit/dozen، شاخهٔ دیهیم و شاخهٔ ابلیس، و هر شش واژهٔ ژرمنی — درست است، و در دو گرهِ مهمِ فارسی، مأخذهای خودِ \"\n        \"نورایی (برهان قاطع ص ۸۳ با حاشیهٔ معین، جفری ص ۴۸، برهان ص ۹۲۱، هرن ص ۱۳۲، هوبشمان ص ۶۵) دقیقاً همان را \"\n        \"می‌گویند که پیکان‌های او می‌گویند.\"\n    ),\n    \"sources\": [W_PIE, W_DIA],\n    \"ref_check\": [\n        {\"ref\": \"POK:230\", \"status\": \"supports\", \"note\": POK_Q +\n         \" Page 230 lies inside the lemma, whose §1 has 'Old Indic m. dvau, dva ... = Avestan dva', §2 the ordinals, \"\n         \"§3 'dwis \\\"twice\\\": ... Avestan biš, gr. δίς, Old Latin duis, Latin bis', §4 'gr. διπλός, διπλόος, Latin \"\n         \"duplus', and §6 the Greek δια / Latin dis- extension.\"}],\n    \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW pp.228-232 s.v. duō(u) (POK_full.txt lines 23722-23974)\", \"stance\": \"supports\",\n         \"note\": POK_Q},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dwo- (AHD_watkins1985.txt line 413)\", \"stance\": \"supports\",\n         \"note\": \"'dwo-. Two. I. Variant form duwo. 1. Germanic *twa, two ... [Pok. duō(u)- 228.]' — the same root, the same \"\n                 \"Pokorny page, and the same set of branches (Germanic, Latin bis/duo, Greek dis/diploos) the chart draws.\"},\n        {\"src\": \"KLN\", \"where\": \"Klein 1966 leaf 884 (printed pp.1668-1669) s.v. two\", \"stance\": \"supports\",\n         \"note\": \"'fr. I.-E. base *duwo-, *duwou-, *dwō(u)-, \\\"two\\\", whence also OI. dvau, dva (masc.), dve (fem. and \"\n                 \"neut.), Avestic dva, Toch. wu (masc.), we (fem.)' — with the cross-reference list 'bi-, bis-, deuce, di-, \"\n                 \"\\\"two\\\", dis-, double, doubt, dozen, dual, dubious, duel, duet, duplex ... biscuit', i.e. Klein's own \"\n                 \"family is Nourai's chart.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt lines 2561, 2633, 2673\", \"stance\": \"supports\",\n         \"note\": \"'du- (reduced element of duou, duō \\\"two\\\") Lat. du-plus; OE tū; Li. du; Per. du'; 'duəi, fem. form of \"\n                 \"duōu ... Cf. WP I, 817'; 'duōu, etc. ... Av. bityō; OPer. duvitiya-; Per. dūtā'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt line 13217\", \"stance\": \"supports\",\n         \"note\": \"'IE *dwis in Lat. bis, early Lat. duis \\\"twice\\\": IE dwou- \\\"two\\\". Walde-P. 1.820.' — Buck's citation \"\n                 \"'Walde-P. 1.817-820' is the Walde-Pokorny treatment that Pokorny 228-232 revises.\"},\n        {\"src\": \"ARY\", \"where\": \"Aryanpur, ARY_latin_index_pages.txt pdf page 284 s.v. TWO\", \"stance\": \"supports\",\n         \"note\": \"Persian دو with 'DAE, DVA, DO (AVESTAN); DUVITIYA (OLD PERSIAN); DO (PAHLAVI); DUVA (OSSETIC); DU (KURDISH)', \"\n                 \"referring to Pokorny, Barnhart, MacKenzie, Onions and Skeat.\"}],\n    \"nodes\": nodes,\n}\n\nout = {\n    \"pdf_page\": 145,\n    \"book_page\": 115,\n    \"verified_by\": \"claude-opus-5\",\n    \"verified_on\": \"2026-09-05\",\n    \"entries\": [entry],\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-145.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"nodes:\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build145.py",
 "description": "Build page-145.json"
}
```


### [2026-09-05T20:32:31.816Z] TOOL RESULT

```
nodes: 26
```


## [2026-09-05T20:32:36.261Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-145.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 145",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T20:32:38.194Z] TOOL RESULT

```
JSON OK
nodes verified: 26/26
node verdicts: {'plausible': 5, 'confirmed': 20, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_found': 1, 'partial': 12, 'not_checked': 6}
books consulted: {'partial': 9, 'supports': 41, 'silent': 6, 'contradicts': 3} | by book: {'KLN': 19, 'AHD': 14, 'BQT': 6, 'MON': 5, 'POK': 3, 'ARY': 2, 'PHD': 2, 'HUB': 2, 'SYN': 2, 'BRT': 1, 'IEC': 1, 'HRN': 1, 'FVQ': 1}
```


## [2026-09-05T20:32:56.509Z] AGENT

Verification of PDF page 145 (book p. 115, root **Dwo** "two") is written to `/home/sfmqrb/git/rishe/data/verification/page-145.json`; `verify_check.py 145` reports 26/26 nodes and **0 PROBLEM lines**.

**Counts** — root: 1 confirmed. Nodes: 20 confirmed, 5 plausible, 1 transcription_suspect. Ref checks: 18 supports / 12 partial / 1 not_found / 6 not_checked. Books consulted: 41 supports / 9 partial / 3 contradicts / 6 silent.

**Flagged items**
- `transcription_suspect` #15 (Greek): the book prints **`dia-phragna`**; no such Greek word — it is διάφραγμα (`dia-phragma`), and the gloss "completely enclosed" reverses the sense ("partitioned off"). Page image checked: the printed page really reads "dia-phragna", so `error_in: "book"` — the extraction is faithful. Same box, `dialuses` is a misprint for *dialusis* (διάλυσις).
- #1 Avestan (`plausible`): `duvitya-kara` is **Old Persian**, not Avestan (Bartholomae: "j. bitya-, g. daibitya-, p. duvitiya-"; Horn p.132, the cited page, calls *duvitiyam karam Old Persian); and Avestan `biš` means "twice", not "more".
- #2 Persian (`plausible`): do / devīst / dīgar solid (MacKenzie, Horn 595, Hübschmann p.65 all quoted); بیش only "probably" from Av. biš (MP has wēš with w-).
- #5 Persian (`plausible`): بسکویت from French is fine; دوجین may have come via Russian дюжина rather than direct French douzaine.
- #14 (`plausible`): *diploma* entered English straight from Latin, not through French (only *diplomat* is French).
- #19 (`plausible`): *diameter* came through Old French, not straight from Latin.

**No extraction errors** — the JSON matches the printed page everywhere I checked (including the odd forms `dia-phragna`, `dialuses`, `duo-decem`, `dve-sate`).

Notable confirmations: Pokorny himself derives Greek διά from *dwis at the end of this very lemma (p. 232), so the whole dia- branch is legitimately under "two"; Borhān p.83 carries Moʿin's footnote deriving ابلیس from Greek διάβολος and citing "جفری ۴۷-۴۸" — i.e. Nourai's own two references agree with each other and with Jeffery p.48; Borhān p.921 (leaf located by running head ۹۲۱) has the دیهیم entry, and Wiktionary supplies the missing Parthian dīδēm → MP dīdēm relay. `KLN:440` on node #1 is a `not_found` (that Klein page is diabetes/diabolic, nothing Avestan). Page image archived at `data/verification/sources/refs/ocr/BOOK/145.png`; ten web sources archived via `fetch_source.py`.
