# Verification process log — verify-page-278


## [2026-09-06T21:18:53.357Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 278 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-278.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-278.json. Write /home/sfmqrb/git/rishe/data/verification/page-278.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 278` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:18:54.509Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:18:55.255Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:18:55.274Z] TOOL RESULT

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


## [2026-09-06T21:18:55.771Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-278.txt"
}
```


### [2026-09-06T21:18:55.798Z] TOOL RESULT

```
1	=== PDF page 278 (book page 248) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ksei 1, Qsěi : to be able to, to qualify, to rule  (refs POK:626; KLN:272)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:626; KNT:181; SPG:215 | xšây, xši 2 : to rule, to qualify ; xšača : king, ruler ; xša-thra, xšathra : "having a king", kingdom | NOTE: "-thra, -tra" are Avestan suffixes meaning "having, owner of".
5	  #2 (parent #1) [Pahlavi] refs=BQT:626; HRN:177; HUB:83 | šâh : king ; šěr : lion ; šatr : kingdom, town
6	    #3 (parent #2) [Persian] refs=POK:626; BQT:648; ZMA:25 | šâh «شاه» : king ; šîr 2 «شیر ۲» : lion ; šahr «شهر» : town city ; čak «چَک» : a promissory note, check
7	      #4 (parent #3) [Arabic] refs=KLN:272 | 
8	        #5 (parent #4) [French] refs=None | 
9	          #6 (parent #5) [English] refs=KLN:272,946 | check, chess, checkmate ☞M.v.t
10	#7 (parent #0) [Avestan] refs=HRN:100,177; KLN:1110,1386; BQT:1316 | arta-xšatra : just king ☞Ar ; paiti-xšatra : protecting king ☞Pa ; xšathra-vairya : choice kingdom ☞Wel 1 ; xšathra-dâra : holder of city, mayor ☞Dher 1 ; xšatra-pavan : protector of kingdom ☞Pa
11	  #8 (parent #7) [Persian] refs=BQT; ETM:67 | ardešîr «اردشیر» : the just king ; pâdešâh «پادشاه» : protecting king ; šahrîvar «شهریور» : desired kingdom ; šahrdâr «شهردار» : mayor | extra: شهریار
12	  #9 (parent #7) [Greek] refs=ETM:67 | sâtrâpěs : governor
13	    #10 (parent #9) [French] refs=ETM:67 | satrape : governor
14	      #11 (parent #10) [Persian] refs=ETM:67 | sâtrâp «ساتراپ» : governor
15	#12 (parent #0) [Avestan] refs=AHD:1480 | xšâya-aršân : king of men ☞Eres 1
16	  #13 (parent #12) [Persian] refs=BQT; ZFS:52 | xašâyâr «خشایار» : "king of men"
17	  #14 (parent #12) [Greek] refs=AHD:1400 | xerexes : a king of Persia who invaded Greece 480 BC
18	    #15 (parent #14) [English] refs=AHD | Xerexes
19	#16 (parent #0) [Pahlavi] refs=HRN:171; FFD:62 | šâyîtan : to be able to, deserve
20	  #17 (parent #16) [Persian] refs=BQT:1237 | šâyestan «شایستن» : to deserve, qualify | extra: شایسته ، شایان ، شایگان ، شاید
21	#18 (parent #0) [Sogdian] refs=SOD:26,28 | `xš`y : to rule ; xšae-wan : title of some kings
22	  #19 (parent #18) [Persian] refs=SOD:26,28 | afšîn «افشین» : title of some kings, a male name
23	
```


## [2026-09-06T21:18:59.155Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-278.json",
 "description": "Read source JSON page 278"
}
```


### [2026-09-06T21:18:59.202Z] TOOL RESULT

```
{
  "pdf_page": 278,
  "book_page": 248,
  "entries": [
    {
      "root": {
        "name": "Ksei 1, Qsěi",
        "lang": "Indo-European",
        "refs": "POK:626; KLN:272",
        "gloss": "to be able to, to qualify, to rule"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:626; KNT:181; SPG:215",
          "words": [
            {"translit": "xšây, xši 2", "gloss": "to rule, to qualify", "script": null},
            {"translit": "xšača", "gloss": "king, ruler", "script": null},
            {"translit": "xša-thra, xšathra", "gloss": "\"having a king\", kingdom", "script": null}
          ],
          "script_extra": null,
          "note": "\"-thra, -tra\" are Avestan suffixes meaning \"having, owner of\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:626; HRN:177; HUB:83",
          "words": [
            {"translit": "šâh", "gloss": "king", "script": null},
            {"translit": "šěr", "gloss": "lion", "script": null},
            {"translit": "šatr", "gloss": "kingdom, town", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:626; BQT:648; ZMA:25",
          "words": [
            {"translit": "šâh", "gloss": "king", "script": "شاه"},
            {"translit": "šîr 2", "gloss": "lion", "script": "شیر ۲"},
            {"translit": "šahr", "gloss": "town city", "script": "شهر"},
            {"translit": "čak", "gloss": "a promissory note, check", "script": "چَک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ز هیتال تا پیش رود برَک - به بهرام بخشید و بنوشت چَک",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "KLN:272",
          "words": [],
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
          "refs": "KLN:272,946",
          "words": [
            {"translit": "check, chess, checkmate", "gloss": null, "script": null, "see": ["M.v.t"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:100,177; KLN:1110,1386; BQT:1316",
          "words": [
            {"translit": "arta-xšatra", "gloss": "just king", "script": null, "see": ["Ar"]},
            {"translit": "paiti-xšatra", "gloss": "protecting king", "script": null, "see": ["Pa"]},
            {"translit": "xšathra-vairya", "gloss": "choice kingdom", "script": null, "see": ["Wel 1"]},
            {"translit": "xšathra-dâra", "gloss": "holder of city, mayor", "script": null, "see": ["Dher 1"]},
            {"translit": "xšatra-pavan", "gloss": "protector of kingdom", "script": null, "see": ["Pa"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT; ETM:67",
          "words": [
            {"translit": "ardešîr", "gloss": "the just king", "script": "اردشیر"},
            {"translit": "pâdešâh", "gloss": "protecting king", "script": "پادشاه"},
            {"translit": "šahrîvar", "gloss": "desired kingdom", "script": "شهریور"},
            {"translit": "šahrdâr", "gloss": "mayor", "script": "شهردار"}
          ],
          "script_extra": "شهریار",
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Greek",
          "refs": "ETM:67",
          "words": [
            {"translit": "sâtrâpěs", "gloss": "governor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": "ETM:67",
          "words": [
            {"translit": "satrape", "gloss": "governor", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "ETM:67",
          "words": [
            {"translit": "sâtrâp", "gloss": "governor", "script": "ساتراپ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AHD:1480",
          "words": [
            {"translit": "xšâya-aršân", "gloss": "king of men", "script": null, "see": ["Eres 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT; ZFS:52",
          "words": [
            {"translit": "xašâyâr", "gloss": "\"king of men\"", "script": "خشایار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Greek",
          "refs": "AHD:1400",
          "words": [
            {"translit": "xerexes", "gloss": "a king of Persia who invaded Greece 480 BC", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Xerexes", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:171; FFD:62",
          "words": [
            {"translit": "šâyîtan", "gloss": "to be able to, deserve", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "BQT:1237",
          "words": [
            {"translit": "šâyestan", "gloss": "to deserve, qualify", "script": "شایستن"}
          ],
          "script_extra": "شایسته ، شایان ، شایگان ، شاید",
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:26,28",
          "words": [
            {"translit": "`xš`y", "gloss": "to rule", "script": null},
            {"translit": "xšae-wan", "gloss": "title of some kings", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Persian",
          "refs": "SOD:26,28",
          "words": [
            {"translit": "afšîn", "gloss": "title of some kings, a male name", "script": "افشین"}
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


## [2026-09-06T21:18:59.716Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:18:59.748Z] TOOL RESULT

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


## [2026-09-06T21:19:05.643Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','KNT','SPG','HRN','HUB','BQT','ZMA','ETM','AHD','ZFS','FFD','SOD','BRT','PHD','NYB','MON','ARY','CHEUNG','WLD','IEC','SYN','LKT','SKT','PLA','AFM']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-06T21:19:07.479Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

SPG {"title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)", "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)", "kind": "archive_djvu", "url": "https://archive.org/details/diealtpersische00spiegoog", "identifier": "diealtpersische00spiegoog (Eranische Alterthumskunde: in.gov.ignca.11987 vol.1, in.ernet.dli.2015.529286 vol.2, in.ernet.dli.2015.103474 vol.3)", "local_file": "/home/sf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ZFS {"title": "Mohsen Abolghasemi, Zaban-e Farsi va Sargozasht-e An, Hirmand 1375/1996", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand. Other Abolghasemi titles are open on archive.org and parsianjoman, not this one."}

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG MISSING

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
```


## [2026-09-06T21:19:16.211Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=633 && NR<=636 {print \"=== leaf \" NR \" ===\"; print}' POK_01.txt | head -200"
}
```


### [2026-09-06T21:19:17.832Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:19:20.239Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) leaves, $(wc -c <$f) bytes\"; done"
}
```


### [2026-09-06T21:19:22.170Z] TOOL RESULT

```
POK_01.txt: 363 leaves, 981836 bytes
POK_02.txt: 433 leaves, 1137861 bytes
POK_03.txt: 429 leaves, 1170809 bytes
POK_full.txt: 1 leaves, 3971883 bytes
```


## [2026-09-06T21:19:24.571Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=281 && NR<=283 {print \"=== leaf \" NR \" ===\"; print}' POK_02.txt"
}
```


### [2026-09-06T21:19:26.381Z] TOOL RESULT

```
=== leaf 281 ===
dryes  RC  44,  313  ff.,  Specht  KZ.  68,  193  ff.  wäre  idg.  *Ä:^erp! tabuistische  Metathese  zu  ^perk^:.-  ,Leben,  Welt,  Eiche*  (got.  fairhus ,Welt*).
WP.  I  486  f.,  WH.  I  277  f.
2.  krep-  s.  oben  S.  567  ff.  unter  1.  ker-.
1,  krep-  ,stark,  fest*;  nur  germ.  und  slav.
Aisl.  hrcefa  ,ertragen*  (vgl.  russ.  krepithsja  ,ausdauern,  beharren*);  abg. krep^,  kräp^k^  ,f est,  stark* ;
cymr.  craff  ,schnell*  aus  aisl.  krappr  ds.  (=  krappr  ,engS  S.  388). WP.  I  487.
2.  krep-  s.  oben  S.  581  unter  kerdp-,
I.  kret-  , schütteln*  (ob  als  ,stoßen*  mit  kret-  , schlagen*  identisch?  oder  Er- weiterung von  sker-  , drehen,  kreisend  schwingen*?).
Lit.  kreciüj  krSsti  , schütteln,  schüttelnd  streuen*,  Iter.  kratau,  -yti  ds., kretü  kreteti  ,sich  hin  und  her  bewegen,  sich  schütteln,  schlottern*,  lett. krest  ,schütteln*,  Iterat.  kratit,  kr^tulis  ,Art  Sieb*  (lett.  kraitdt  ,taumeln* Entgleisung  von  einem  *krit-  aus) ;
mir.  crothaim  ,schüttle*,  gall.-rom.  '^■crottiäre  ,schütteln* ;
ahd.  redan  ,sieben*,  nhd.  mdartl.  räder,  rädel  ,Sieb*;  aisl.  hradr  ,schnell*, ags.  ArcBjb,  hrcßd  ,schnell,  behend*,  engl,  rather  ,lieber*,  ahd.  hrad,  hrat ,velox,  strenuus* ;  aisl.  hrceda  ,erschrecken  (trans.)*,  hrceddr  ,entsetzt* ;
auch  ags.  ä-hreddan  ,befreien,  retten*,  ahd.  retten  ,bewegen,  treiben; befreien,  retten'  als  ,von  der  Gefahr  wegstoßen*?
WP.  I  484,  Mühlenbach-Endzelin  II  274,  261,  256.
621
jcret'  »schlagen*;  wohl  ursprünglich  mit  1.  Jcret-  identisch.
Qr.  y.QÖTog  ,jedes  durch  Schlagen,  Stampfen,  Klatschen  entstehende Geräusch*;  %Qoreiv  ,klatschen,  klopfen,  schlagen*, x^dra^oi^, Klapper',  yiQÖzacpog ^Schläfe*  (eigentlich  ,*das  Klopfen*);  ,Berghang;  Seite*,  ^qoxacpig  ,Spitz- hammer* ;
dazu  mit  ursprüngl.  wohl  bloß  präsentischer  Nasalierung  aisl.  hrinda, hrattj  ags.  hrindan,  hi^and  ,stoßen*;
vielleicht  die  slav.  Sippe  von  ahg.  krostg^  krotiti  ,zähmen*,  krot^k^  ,sanft, mild,  mäßig*,  wenn  ursprüngl.  , durch  Prügeln  mürbe  machen'?
WP.  I  484  f.,  Berneker  624.
X.  kreu-,  kreuo-ikrü-  1.  ,dickes,  stockendes  Blut,  blutiges,  rohes  Fleisch*, vermutlich  ,g
=== leaf 282 ===
eronnen  (vom  Blut)*,  dazu  eine  2.  Gruppe  kreus-,  krus- für  ,Eis  (als  erstarrendes),  Kruste  (ursprüngl.  von  Eis  oder  Wund- schorf), Eisscholle,  Erdscholle*  (s.  unten)  und  verbal , frieren,  schaudern (Gänsehaut)*,  kreus-s-  n.  ,rohes  Fleisch*,  krouio-  n.  ,Blut*,  krü-s  f.  ,Blut*.
A.  Ai.  kravis-  n.  ,rohes  Fleisch*  (=  gr.  x^f/ag),  kravyam  n.  ,Blut* (*krouio-  =  apr.  krawian  n.),  krü-rd-  ,blutig,  grausam*  =  av.  xrüra-  ,blutig, grausig,  grausam*  (:  lat.  crüdus?)  im  Kompositum  mit  i-  für  ro-St.,  av. xrvi-dru-  ,der  eine  blutige  Holzwaffe  führt*,  d.  i.  xruvi-dru-,  av.  xrü-  f., xrüm  (=  xruvdm)  Akk.  , Stück  blutiges  Fleisch*,  xt-vant-  (d.  i.  xrüvant-) ,grauenhaft,  grausig*  ( :  lat.  cruentus),  xrvlSyant-  ,blutdürstig,  Grausen  er- regend*, xrüta-  ,grausig,  grausam*,  xrünya-  n.  ,Bluttat,  blutige  Mißhand- lung*, xrüma-  ,grauenhaft,  grausig*;  mit  einer  Bedeutung  ,*geronnen'  = ,dick,  hart*,  ai.  krüddyati  , macht  dick,  fest*,  av.  xrnzdra-  ,hart*  (daneben wieder  mit  i-  statt  ro-St.  im  Kompositum  xru^di-vacah-  ,mit  derber,  lauter Stimme  sprechend*),  xraoidva-  ,hart*;
gr.  yiqeag  n.  ,Fleisch*  (^krmds)]
lat.  cruentus  ,blutig*  (s.  oben),  cruor  m.  ,das  rohe,  dicke  Blut*  (*kreuös)j osk.  krustatar  ,crusta  tegitor*  (Denom.  von  *krus-ta),  lat.  crusta  , Kruste, Rinde,  Schorf*,  ursprüngl.  ,das  fest  gewordene  Blut  auf  einer  Wunde* (*krüs-ta),  crüdus  ,roh,  rauh,  hart*  (*krü-do-),    crüdelis  ,grausam,  herzlos*;
gall.-rom.  crödios  ,hart*  {*kroudios)-
mir.  cru  (j^krüs).  Gen.  crduj  crö  (*kruuos)j  cymr.  craUj  corn.  crow  (^kruua) ,Blut*  (s.  Pedersen  KG.  I  61,  251  f.,  II  97,  Lohmann  ZceltPh.  19,  63  f.),  air. crüaid  (*kroudis)  ,hart,  fest*,  bret.  kriz  (*krüdis)  ,cru,  cruel*  (Pedersen KG.  I  207 ;  nicht  Lw.  aus  lat.  crüdus) ;  das  d  im  Kelt.  und  Lat.  durch Dissimil.  aus  r?
lit.  kraüjas  ,Blut*  (:  ai.  kravya-m),  apr.  crauyo,  krawian  ds.,  lit.  krüvinas ,blutig',  krüvinu  ,mache  blutig*,  Partiz.  krüvintas  ,blutig  gemacht*,  lett. kreve  ,geronnenes  Blut,  Schorf,  Kruste';
622  •
slav.    *kry   (*krüs\    Gen,    *krzve  ,Blut'  in    slov.    krt,    apoln.   kry^  aksL^ krzvh-,    aksl.  ki-bVhm  ,blutig*  (=  lit.  kriimnas)-^  ^
ahd.  (h)rö,  (h)rawer,  as.  Arä,  ags.   hreaw,  aisl.   Ärär  ,roh*  {*hrawa-),
B.  Skyth.  *xrohu-kasi-j  gr.  KavY^aaig  , Kaukasus*  (als  ,eis-glänzend^)  •
gr.  r()  xovog  ,Frost'  (=  *x^?;ö'og?),  y.Qvoraivü)  ,mache  gefrieren',  ^^Qvaialloö  ** ,Eis;  Kristalls  x^vjwdg  ,Frost'  (*x^t'(r^dg),  von  x^vog  abgeleitet  (?)  x^rd^t^  ' »schauerlich*,  'kqvsqöq  »schauerlich,  grausam*;
ai
=== leaf 283 ===
sl.  hriösay  kraus  , schaudern',  hrjöstr  n.  , rauher  Boden'  (:  lat.  crusta) ahd.  (h)roso,  (h)rosa  ^Eis,  Kruste'  (dazu  auch  der  Name  des  Monte  Rosa) ags.  hrüse  ,Erde,  Grund'  (diese  s-Formen  in  Beziehung  zu  rd  y,Qvog  und  :)
lett.  kruvesisj  kruesis  ,gefrorener  Kot',  lit.  atkrüsti,  Prät.  -krüsau  ,wieder- aufleben,  von  Erfrorenem'  (,*auffrieren') ;  Mühlenbach-Endzelin  II  291.
Ohne  -s-  vermutlich  norw.  dial.  ryggja  ,schaudern'  (vgl.  x^vf^dg),  viel fraglicher  ags.  hreoh  ,rauh  (vom  Wetter),  betrübt,  wild'.
WP.  I  479  f.,  WH.  I  294  ff.,  Trautmann  141  ff.,  J.  Markwart  Morgen- land 1  (1922),  3  ff.
2.  kreu-  ,zusammenstürzen,  stürzen,  fallen';  nur  germ.  und  halt.
Aisl.  hrun  n.  , Zusammenbruch',  hrynia  ,fallen';
apr.  krüt  ,fallen',  kruwis  ,Fall'  (aber  lett.  kruts  ,steil  abfallend,  steil abhängend'  als  Lw.  zu  klr.  krutoj  ,gewunden,  steil,  schroff',  s.  unter  kert- jdrehen');  vielleicht  lett.  kräulis  ,Absturz',  kräiija  ,steiles  Ufer',  krauta  ,Ufer*;
mit  -s-  ags.  hreosan  , stürzen';
mit  -d-  aisl.  hrjöta  ,stürzen,  springen',  mhd.  ritzen  ,sich  eilig  bewegen';    .
mit  -t-  ags.  hrldig  »schneebedeckt',  aisl.  hrodi  ,Abfair,  hrydr  ,es  bricht  ^ hervor'  (von  Dampf,  Feuer  u.  dgl.),  hrydja  ,naßkaltes  Wetter,  Regen  und  % Schnee'.  ^
WP.  I  480,  Trautmann  143,  Wissmann  Nom.  postverb.  127.
3.  kreu-,  krou-s-  ,stoßen,  schlagen,  zerschlagen,  brechen'.
Die  unerweiterte  Wurzel  vielleicht  in  ahd.  {h)riuwan  ,betrüben,  ver- drießen', nhd.  reuen^  ags.  hreowan  ,betrüben',  aisl.  hryggr  »betrübt',  ags. kreow  ds.,  f.  ,Reue',  ahd.  (h)riuwa  ,Reue'  (anders  Persson  Beitr.  178); über  abg.  krupa  »Brocken,  Krümchen'  (wäre  eine  jp-Erweiterung)  s.  unter kreup-  »Schorf.
krous-:gr.  ycQova)  »stoße,  schlage'  (Hqüiigü),  vgl.  sy,QOvad"r]v,  -AQOVGTeog] XQOvaTixög  ,stoßend,  widerhallend');  hom.  ^igoalvw  ,schlage»  stampfe»  vom Pferde'  (*yiQovaaviü)),  yiQOLÖg  »abgebrochen»  beschädigt'  (Hgovaiög);
aisl.  hrosti  m.  »gemaischtes  Malz';
lit.  krusü,  kriiUi  (kriüHi)  ,stampfen,  zerstoßen',  krusä  f.  ,Hagel',  lett. krusa  »Hagel'»  lit.  Iter.  kriauäaü,  -yti,  lett.  krause
```


## [2026-09-06T21:19:32.330Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=285 && NR<=288 {print \"=== leaf \" NR \" ===\"; print}' POK_02.txt"
}
```


### [2026-09-06T21:19:34.224Z] TOOL RESULT

```
=== leaf 285 ===
sel',  ndl.  remmen  ,(ein  Rad) hemmen,   sperren'   (,*mit   einem    Balken'),    ^01"^^*^^^^    auch    aisl.    hrefni
624  •
»unterste  Planke  überm  Schiffsboden*  und  got.  hramjan  ,kreuzigen'  {^ ,an  ein  Gestell  heften');
russ.  kröray  PL  »Webstuhl',  zakromü^  »mit  Brettern  umstellen',  klr.  pry. kromyty  »bändigen',  russ.  s-krömnyj  »bescheiden'  usw.
WP.  I  487  f.
kr{6)k-sko-,  -u-  ,Arm  u.  dgl.'?
Ai,  kisku-  m.  »Vorderarm;  Stiel  einer  Axt;  ein  Längenmaß'  (mind.  für *krsku-) ;
alb.  krake  ,Oberarm,  Schulter»  Flügel'  {""krok-sko-?)  ]
wahrscheinlich  zu  lit.  kdrka  »Schweinefuß»  Vorderbein  des  Schweines*, ablaut.  ostlit.  kirkälis  m.  »Stelze';
slav.  *korka  f.  in  sloven.  krdka^  krdda  »Schweinefuß*;
daneben  slav.  *korkb  in  bulg.  krak  »Bein»  Fuß*,  russ.  ökorok  »Schinken*; dazu  ablaut.  slav.  *krok^  m.  in  skr.  ki^ok  (Gen.  kroka),  öech.  krok  »Schritt* und  slav.  *korakh  m.  in  skr.  koräk,  sloven.  kordk  ds.
Ganz  unklare  Ablautverhältnisse.
WP.  I  488»  Trautmann  118.
krüs-  »Unterschenkel»  Bein'.
Arm.  srun-k'  PI.   (Gen.  srvanc,  sruni-c)  »Schienbein,  Wade*  (*/crüs-m-)ji lat.  crüs,  -ris  n.  »Unterschenkel»  Bein*. WP.  I  489»  WH.  I  295.
krut-  »Wölbung»  Brust»  Bauch*.
Mir.  crott  f.  »Höcker»  Harfe*»  nir.  cruit  ds.»  altbrit.-gall.  crotta  »Harfe*, cjmr.  crwth  m.  »Höcker»  Geige'»  croth  f.  »Bauch»  uterus»  vulva*;
lit.  krütis  »weibliche  Brust*»  krütine  »Brust*»  lett.   kriits  »Hügel»  Brust*. Wohl  zu  kreu-  »wölben*»  s.  unter  (s)ker-j  (s)kereu'  »drehen*. WP.  I  485,  489»  Specht  Idg.  Dekl.  77  2.
ksä-  »brennen  (versengt»  dunkel  V  ?)*  ?
Ai.  ksäyati  »brennt'»  ksäti-  f.  »Glut*»  ksämd-  »versengt»  ausgedörrt»  ver- trocknet*»   ksärd-   »brennend»    ätzend*;    Kaus.   ksäpdyati   »macht    brennen*;
zu  letzterer  p-Yovm  vielleicht  arm.  cav  »Schmerz*»  casnum  »zürne*»  Aor. caseay  (»*hitzig  sein*;  s  =  ps-)]  zu  ksämd-  wohl  arm.  camaJi  »trocken* (die  arm.  Worte  weisen  auf  ks-).
WP.  I  500»  Frisk  Nominalbild.  6 ;  s.  unter  ks'n-ro-.
625
;eip-,  kseih-  , werfen,   schwingend   schleudern,   in   schwingender   heftiger Bewegung  sein'.
Ai.  kßipdti   ,wirft,    schleudert',  Kaus.  ksepdyati,    ksiprd-h   ,schnell';    mit Media  aksl.  osiba-jg,  -ti  ,sich  abwenden',  russ.  lihdth  , werfen',  sibkij  ,schnell', ^sibdth  , abschlagen',  osibdhsja  ,sich  irren'. WP.  I  501.
fs-en-,  ks-es-,  ks-eu-  s.  oben  S.  585  f.  unter  kes-.
ics^-J'o-  ,trocken';   vom  Himmel  und  Wetter  auch  ,trocken  =  hell,  klar'. Gr.  ^€q6v  (nur  Akk.)
=== leaf 286 ===
  , festes,  trockenes  Land',  dehnstufig  ^rjgög  ,trocken, dürr' ;  vgl.  oben  S.  624  ai.  ksärd- ;
lat.  serescunt  (Lucil.  I  306)  ,(die  Kleider)  trocknen  (in  der  Sonne)', serenus  ,heiter,  hell,  klar,  trocken'  (vom  Himmel  und  Wetter) ;
ahd.  serawen  ,trocken  werden,  tabescere,  languere,  marcere',  mhd.  nhd. Serben  ,verdorren,  welk  werden' ; toch.  A  ksär{k)  ,Morgen'?
Daß  ks^-ro-  eine  Erweiterung  von  ksä-  ,brennen,  versengen'  sei,  ist  wahr- L     scheinlich. i       WP.  I  503,  Schwyzer  Gr.  Gr.  I  329.
kseuhh-  ,schwanken,  in  schwingender  Bewegung  sein'.
Ai.  ksübhyatij  ksöbhate  (ksubhnöti,  -näti)  ,schwankt,  zittert',  ksöbJiayati ,setzt  in  Bewegung',  ksöbha-  m.  , Schwanken,  Erschütterung';  av.  x§aob- ,in  Aufregung  geraten'  (xsufsqn),  npers.  ä-mftan^  ä-§öftan  ,in  Bewegung versetzen',  ä-söb  , Verwirrung,  Tumult';
poln.  chybac  ,schaukeln,  hin  und  her  bewegen' ;  cJiybki  ,behend,  rasch' ;  klr. chybdty  ,zweifeln,  unschlüssig  sein',  chyba  (*ksüba)  , Mangel,  Fehler'  usw.
WP.  I  502  f.,  Trautmann  144.
kseud-  jklein  stampfen'.
Ai.  ksödati  ,stampft,  zermalmt',  ksöda-  m.  ,Stoß,  Stampfen,  Zermalmen; Mehl,  Pulver,  Puder',  ksudrd-  ,klein;  niedrig,  gemein',  Komp.  ksödlyas-] ksudrd-  n.  ,Stäubchen';
abg.  chud^ ', klein-,    gering,   schlecht',    Komp.  chuzdhjh   (:  ai.  ksödiyas-).
Machek  (Slavia  16,  174)  nimmt  als  ursprüngl.  Bedeutung  ,mager'  an (cech.  chudy  ,mager'),  das  er  somit  zu  ai.  ksudhyati  ,hungert',  ksödh-uka- ,hungrig'  stellen  möchte.
Verbindung  von  ai.  ksudrd-  mit  av.  x§udra-  ,flüssig*  (s.  2.  kseud-)  versucht Batakrishna  Ghosh  (Les  formations  nominales  en  p^  S,  21)  zu  begründen.
WP.  I  502.
40
626  •
kpei'  ,siedeln,  sich  ansiedeln,  eine  Niederlassung  gründen*.
Ai.  ksiti,  hsiydti  ,weilt,  wohnt',  av.  saeiti  ds.,  ai.  ksiti',  av.  Hti-  ,Wohn.' platz,  SiedelungS   ai.  kskra-,   av.  söid-ra-  n.  ,Gnindbesitz,  Wohnplatz',  ^j^ Jcsema-  m.  ,ruhiges  Verweilen';
arm.  sen.  Gen.  Hni  ,bewohnt,  bebaut,  Dorf  (:  gr.  xzrotW);
gr.  'ATL^cü  ,gründe',  iv-KTifj^svog  ,wohl  gehaut,  wohl  bestellt',  iv'/.TLTog  ^. rteQiy.TLOvsg,  Tteqiy.Tkai  ,Um wohner,  Nachbarn',  d(X(pLy,TLOvsg  ,Herumwohnende* (zur  Form  df.icptxrvovsg  Lit.  bei  Boisacq  525  Anm.  2),  xr/ö-tg  , Anbauung' Ansie
=== leaf 287 ===
delung',  rhod.  xroivä  , Wohnsitz,  Gemeindebezirk',  auch  xTtAog  ,ruhig» (eigentl.  ,an  die  Siedelung  gebannt,  gezähmt') ;  gehört  wohl  zum  Folgenden:
kpe(i)-,  kp9(i)-  ,erwerben,  Verfügung  und  Gewalt  worüber  bekommen*.
Ai.  ksdyati  ,besitzt,  beherrscht'  (*kp9i'eti)  =  ay.  xsayati  ,hat  Macht Gewalt,  herrscht,  verfügt  worüber,  besitzt',  xsayö  , Macht';  ai.  ksatrd-  a, , Herrschaft',  av.  ap.  ksad'va-  n.  ,Herrschaft,  Reich;  Herrschergewalt* (urar.  Neubildung  zu  ksayati)^  apers.  x§äyad-iya-  ,im  Besitz  der  Herrscher« gewalt,  König'  (npers.  §äh),  Xsayärsan-  ,Xerxes'  (x§aya-arsan-.  jHeldea beherrschend');
gr.  %tdo{.iaL  ^erwerbe'  (=  k§ayati\  Perf.  ytexrrj^ai  ,besitze*,  Yxeavov  (mit unklarem  s)  ,Besitz,  Eigentum,  Vermögen*,  poet.  ytTeag,  Dat.  PL  -nTsaTsaaip ds.,  y,v7j(.icc  n.  ,Erwerb,  Besitz,  Eigentum',  yirfjvog  n.,  PI.  ,Besitz,  Vermögen*, Sg.  ,das  einzelne  Stück  Vieh' ;  mit  demselben  Anlautverhältnis  wie  zwischen xTsivo)  :  gort.  %aTaa-/,eviß  auch  att.  0t Ao-cx^t  [17g]  =  -xrijTiyg;  durch  Kreu- zung von  ey^y.Tr](Tig  und  l'^-Ttäaig  (:  näfxa)  dial.  eyuräffLg  ,Landerwerb'.
WP.  I  504,  BSL.  38,  143,  Schwjzer  Gr.  Gr.  I  325  f.,  5196.
ku-,  kus-  in  Worten  für  ,Kuß'   (vgl.  hu-  S.  103).  ]
Gr.  Tivvsa),  savaaa  ,küssen'  (ne-Infixpräsens  *y,v-vs-a-\_(.iL]).  Mit  Hemmung der  Lautverschiebung  im  Schallworte  aisl.  koss,  ags.  coss,  ahd.  kus  ,Kuß', aisl.  kyssa,  ags.  cyssan,  ahd.  küssen  ,küssen';  got.  kukjan,  ofries.  kükken scheint  daraus  in  der  Kindersprache  umgebildet  zu  sein  ;
hitt.  3.  PL  kuiuassanzi  ,sie  küssen'.
Ähnlich  ai.  cnsati  , saugt',  cuscusä  , Schmatzen  beim  Essen*.
WP.  I  465,  Kuiper  Nasalpräs.  151.
kü-  ,spitz,  Spieß'.
AL  §ü-la'  m.  n.  ,Spieß,  spitzer  Pfahl;  stechender  Schmerz*,  arm.  slaJt (aus  *sulak)  , Spieß,  Dolch,  Pfeil*,  air.  cuil  ,culex',  cymr.  cylion-en  ds., lat.  Culex  ,Mücke';
ai.  §ü-ka-  m.  n.  , Stachel  eines  Insekts,  Granne  des  Getreides*,  av.  sü-ka- f.  ,Nadel',  np.  sözan  ,Nadel',  sök  ,Ähre,  Granne';  zweifelhaft  präkr.  osukkai ,wetzt,  schärft';
627
lat.  cuneus  ,Keil'  (auf  Grund  von  ku-no-  , Spitze'). ^yp.  I  465,  WH.  I  302  f.,  308.
i^idh'  ,Mist,  Kot'  ?  ?
Gr.  va-ytvd-d'  vdg  d(p6dsvi.ia  Hes.,  xvd-cüdsog'  dvaöa^iov  Hes.,  ywdiföv  ^oneQ^ia' Hes. ;  lit.  Mdas,  lett.  süds  ,Mist,  Kot*. WP.  I  467.  Anders  Specht  Indog.  Dekl.  252  f.
iku  ,Nachahmung  des  Kuckucksrufes'.
Ai.  köJcüd-  m.  ,der  indische  Kuckuck',  köka-  m.  ,Kuckuck'  (auch  ,Gans;
=== leaf 288 ===
 "VVolf  s.  unter  kän).
Gr.  xoxxt'g,  'V/og  m.  ,Kuckuck'  (dissim.  aus  *xi;xxi;-),  xdxxc  ,Ruf  des Kuckucks',  xoxxv^w  ,rufe  Kuckuck';
lat.  cucülus  ,Kuckuck'  (unmittelbar  von  *cucü  gebildet);
mir.  cüach  (oder  Neubildung-  zu  air.  cöiK^kovik-s,  Gen.  cüäch?),  cjmr. cog  ,Kuckuck';  nhd.  (ohne  Lautverschiebung  infolge  stets  nebenhergehender Neuschöpfung)  Kuckuck;
lit.  kuküoti,  lett.  kukuot  ,Kuckuck  rufen' ;  serb.  kükavica  , Kuckuck', russ.  kuküsa  usw.  ds.,  r.  kukuvdth  usw.  ,wie  ein  Kuckuck  rufen'.
WP.  I  466  f.,  WH.  I  299.
'  kup-  , Schulter'  (germ.  mit  anlaut.  s-).
Ai.  §upti-y  av.  swpti-  ,Schulter';  alb.  sujp  , Schulter,  Rücken'  (ohne  for- mantisches  -t-)]  mnd.  schuft  m.,  ostfries.,  ndl.  schoft  , Vorderschulterblatt einer  Kuh,  eines  Pferdes'  {*skuftu-).
WP.  I  467.
kuak-.    Einzelsprachliche    Nachahmungen    des    Froschlautes    und   Entenge- schnatters. Gr.   xoaj    ,vom   Quaken    des    Frosches',    lat.    coaxare    , quaken'    (wohl Nachbildung   von   xoa^),    dt.    quack^    quacken    ,von   Fröschen ;    schnattern (Ente)  usw.',  schwed.  mdartl.  kvaka  ,schnattern  wie  eine  Ente',  aisl.  kvaka ,zwitschern',  russ.  kvdkath  ,quaken',  u.  dgl. WP.  I  468.
kuat^h)-  ,gären,  sauer  werden,  faulen';  kuät-so- :  küt-so-  , Gärstoff'. Ai.  kvdthati  ,siedet,  kocht',  kväthd-  m.  ,Decoct';
got.  Jvapö  f.  , Schaum',  Jvapjan  ,schäumen',  schwed.  dial.  hvä  (*hvapa) , Schaum',  ags.  hwaperian^  hiooperian  ,schäumen,  branden' ;
lat.  caseus  ,Käse'  (von  *cäso-  aus  *kuat-so-  , Geronnenes',  ablautgleich mit  abg.  kvas^]  das  Fehlen  des  u  harrt  noch  der  Erklärung);
abg.  kvasi,  ,Sauerteig,  säuerliches  Getränk'  (kuät-so-)  usw.,  schwundstufig a.h g.  v^(sykysngt^,  -kysHi  ,sauer  werden',  kyseh  ,sauer'  (-s-  aus  ^  +  *);
40*
628  •
lett.  küsät    ,wallen,    sieden',    küsuls    ,SprudelS    auch    wohl    küstu,    Jt ,schmelzen';    der   aus    ,gären,    sauer   werden'    entwickelte  Begriff   ,fatjle^. schlägt  die  Brücke  zu  ksl.  k^shm  ,langsam';    vgl.   lett.   kust   »schmelze» tauen  —  ermüden',  kusinät  ,müde  machen' ;  lett.  kusls  ,steif,  schwächliclii lit.  dial.  kHÜas,  kuslüs  ,schwächlich',  apr.  ucka  kuslaisin  »schwächst*.  M
WP.  I  468,  WH.  I  176  f.,  Trautmann  147.
1.  kuei-,  kuei-no-  ,Schlamm,  Kot,  beschmutzen'.
Mit  Formans -12(0)- :lat.  caenum  , Schmutz,  Kot,  Unflat',  ohscEnua^ scaenus  (Rückbildung  aus  *obscenare)  ,sch mutzig,  ekelhaft,  unsittlicj|t (caenum  urbanisiert  für  plebejisches  *cenum  aus  ^coinom,  *quoinom\  iV con-quinäre  ,beschmutzen,  besudeln',  c
```


## [2026-09-06T21:19:48.244Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"checkmate\" KLN_1966.txt | head -20; echo ---; grep -n \"shāh mātā\\|shāh māt\\|sháh mát\\|shah mat\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T21:19:48.307Z] TOOL RESULT

```
7296:check,  n.,  i)  a  sudden  stop,  restrain,  repulse; 2)  in  chess,  an  attack  upon  the  king.  —  ME. chek,  fr.  OF.  eschec  (whence  F.  echec),  ‘check (at  chess);  defeat,  blow,  loss’,  fr.  earlier  eschac, borrowed  (through  the  medium  of  Spanish  and Arabic)  fr,  Pers.  shah,  ‘king’  (in  the  Arab.-Pers. phrase  shah  mat,  ‘the  king  is  dead’),  fr.  OPers. xshaya-,  ‘king’,  which  is  rel.  to  xshaya&iya-, ‘power’,  fr.  I.-E.  base  *qpe(i)-,  *qfe(i)-,  ‘to  rule’, whence  also  OI.  ksayati,  ‘possesses,  rules’,  ksat- ram,  ‘rule,  dominion’,  Gk.  xTaopat,,  T  get,  ac¬ quire’.  See  satrap,  shah  and  cp.  checkmate,  chess, checker,  exchequer,  Kshatriya.  Cp.  also  the  first element  in  Ahasuerus,  Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. checker,  chequer,  n.,  a  pattern  resembling  a  chess¬ board.  Shortened  fr.  OF.  eschekier  (F.  echi- quiet),  ‘chessboard’,  fr.  ML.  scaccarium,  ult. fr.  Pers.  shah,  ‘king’.  Sec  check,  ‘a  sudden  slop’, and  cp.  exchequer.
7298:checkers,  chequers,  n.,  a  game  played  on  a checkerboard;  draughts.  —  From  prec.  word, checkmate,  interj.  —  ME.  chek  mat,  fr.  OF.  eschec et  mat  (F.  echec  et  mat),  fr.  Sp.  jaque  y  mate,  fr. Arabo-Pers.  shah  mat,  ‘the  king  is  dead’  (whence also  It.  scaccomatto).  See  check,  ‘a  sudden  stop’ and  cp.  mate,  ‘checkmate’.
7299:Derivatives:  checkmate,  n.  and  tr.  v. cheeky,  adj.,  divided  into  squares  of  alternate tincture.  —  Formed  fr.  check,  n.,  ‘a  sudden stop’,  with  adj.  suff.  -y.
23103:mat,  adj.,  dull  (said  of  color  or  a  surface).  —  F., ‘dull,  lusterless,  unpolished’,  fr.  OF.  mat,  ‘de¬ feated,  afflicted,  depressed,  dejected;  dull’,  fr. Arab,  mat  in  the  sentence  mat  ash-shah,  ‘the king  has  died’.  The  word  mat,  orig.  used  only as  a  term  of  chess,  gradually  developed  also  the meanings  ‘faint,  feeble,  dull-colored .  See checkmate  and  cp.  matador,  mate,  adj. matador,  n.,  1)  the  man  who  kills  the  bull  in  the bullfight ;  2)  one  of  the  three  chief  cards  in  the game  of  ombre  and  quadrille.  —  Sp,,  ‘killer, murderer’,  fr.  matar,  ‘to  kill,  murder’,  fr.  Arab. mdta,  ‘he  died’.  Cp.  checkmate.  Cp.  also  mat, ‘dull’.
23106:Derivative:  match,  tr.  v. matchet,  n.  —  A  var.  of  machete, mate,  tr.  v.,  to  checkmate;  to  overcome.  —  ME. maten,  fr.  OF.  mater,  ‘to  checkmate;  to  defeat, overcome’,  fr.  mat,  ‘checkmated ;  defeated,  over¬ come’.  See  cp.  mat,  ‘dull’.
23107:mate,  n.,  checkmate.  —  ME.  mat,  fr.  MF.,  fr.  OF. See  prec.  word.
---
```


## [2026-09-06T21:20:00.762Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find page markers\nfor i,l in enumerate(lines):\n    if 7280<i<7300 or 23090<i<23110:\n        s=l.strip()\n        if len(s)<20: print(i, repr(s))\n\""
}
```


### [2026-09-06T21:20:02.544Z] TOOL RESULT

```
7289 'cheat'
```


## [2026-09-06T21:20:06.907Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xšāya\\|xshaya\\|xsaya\\|xSaya\" KNT.txt | head -30"
}
```


### [2026-09-06T21:20:06.956Z] TOOL RESULT

```
2043:Acc. Pl. martiyd, xSayatiyd, hamigiyà, Saké, ауа, ufra&ta.
2489:pIE *mé- ‘measure’ in pAr. *má-ja-, Skt. máyate: OP imf. mid. -amáyalü in frémdyala ‘com- manded'. On OP xSaya-, see $218.
2950:§283. Тнв Parricrptes in OP have no peculi- arities of syntax. The following are examples of their uses: as attributive adjective, axSatd DPe 23; as appositive adjective, marta XPh 48; predicate adjective to a nom., zinuta DNb 26, xSayamna DNb 15, бакаа DB 1.38; predicate adjective to an accusative, ditam DB 1.50, duruatam DB 4.44f; predicate nominative without the copula, serving as finite verb, paraità DB 2.32f; substantivized
3067:VIII. Subordinate clauses may stand either be- fore or after the main clause; the order of the ele- ments in them is the same as the order in main clauses, though the verb is more likely to stand in final position. Occasionally a word belonging to the clause stands before the relative or conjunc- tion which introduces it: DB 4.37 tuvam Ка xSaya- iya hya aparam ühy ‘thou who shalt be king hereafter’, 4.67f, 4.87, cf. especially ОМ 21f, 24f. In one phrase an adjective belonging to the ante- cedent is incorporated within the relative clause: DB 2.31, 2.51 kära hya hamiciya manā nary gauba- іаїу ‘the rebel army which does not call itself mine’, ef. DB 2.84 kdram hamigiyam hya mand nau gaubülauy.
3430:1 Àriyáramna : xSayaftya : vazraka : xSayaé 2 iya : xsüyafiyànàm : xSayafiya : Parsa
3431:3 : Cispais : xšãyaðiyahyā : риса ; HaxdmaniSah 4 ув : парӣ : Вапу : Áriyáramna : xšāyaðiya 5 :iyam : dahyau§ : Parsa : tya : adam : dárayá 6 miy : hya : uvaspà : umartiyü : mana : baga 7 : vazraka : Auramazda ; frábara : vašnā : Au 8 ramazdàáha : adam : xXàyafiya : iyam : da 9 hyauS : amiy : 80у : Anyaramna
3438:1 Ar&àma : xSayatiya : vazraka : x
3439:2 Wàyaliya : xSayafliyánàm : x
3441:5 :08ty : Arsama : xSayaéiya : Au
3450:CMa = Cyrus, MunaHAB (PASARGADAR) А, 1 adam : Kürus : xSaya 2 уа : Haxamanisiya TRANSLATION or CMa: I am Cyrus the King, an Achaemenian.
3460:1 : adam : Dàrayavaus : xSayafiya : vazraka : xšāyaðiya : xáüyatty
3463:4 Darayavaus : xSayafflya : manā : pita : Vistàspa : Vistaspahyd : pità : Ars
3469:10 : xSayafiyaé : dha : adam : navama : IX : duvitiparanam : vayam : хёйуай
3472:13 айту : Dārayavauš : xSayafiya : ima : dahyava : {уа : mand : paliyaisa : vain
3478:2] uš : xšāyaðiya : atar : ima : dahyáva : martiya : hya : agriya : ha : avam : u
3483:27 tiy : Dárayavaus : xSayafiya : ima : tya : mand : kartam : pasàva : уаба : xš
3485:29 à : hauvam : 1dà : xšāyaðiya : dha : avahyà : Kabüfiyahya : bra
3492:44 : Darayavaus : xSayafiya : айа : xSacam : tya : Gaumáta : һуа : magus : adin
3496:48 v :xšāyaðiya :abava —— :08tiy : Dàrayavaus : xSayafiya : naiy : aha : martiya : 49 naiy : Разза : naiy : Mada : пазу : amàxam : taumáyà : kaSeiy : һуа : avam : Gau 50 matam : буз : magum : xSacam : ditam : caxriyà : kiraSim : hac& : багат : а 51 tarsa : kàram : vasiy : av&janiy& : һуа : paranam : Bardiyam : adánà : avahyar 52 айу : кагат : avájaniyà : mátyamà&m : xénàsátyy : tya : adam : naiy : Bard
3513:59 mi : dahyàus : Mādaiy : avadasim : avajanam : xSacamsim : adam : adinam : va 60 sna : Auramazdiha : adam : xSayaéiya : abavam : Auramazdà : xsagam : manā : fr
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3592:49 dam : іу : Därayavauš : xšāyaðiya : pasáva : Vaumisa : nàma : Pārsa : manā : ba
3600:57 kartam (айу: Dàrayavaus : xšāyaðiya : patiy : duvitiyam : ham
3607:64 :08tiy : Dirayavaus : xšāyaðiya : pasáva : adam : nijàyam : haca :
3623:80 abava : karahya :ava6a : абаһа : adam : xšāyaðiya : amiy : Asagarta
3634:9] uzmayapatiy :akunavam p :8tly : Daravavaus : xšāyaðiya : ma : tya : ma
3635:92 nā : kartam : Mādaiy : йу : Dàrayavaus : xSayafiya : Parüava : uta : Var
3675:І :08tiy : Darayavaus : xšāyaðiya : pasáva : adam
3696:$ rmapadahya : mahya : I : rauca : 0akatam : dha : avaflásàm : hamaranam : ka 9rtam : 88у : Darayavaus : xSayafiya : pasiva : dahy&us : ma
```


## [2026-09-06T21:20:11.639Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=195 && NR<=197 {print \"=== leaf \" NR \" ===\"; print substr($0,1,3000)}' KNT.txt"
}
```


### [2026-09-06T21:20:13.652Z] TOOL RESULT

```
=== leaf 195 ===
пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (as gen.; §313.1[). Aršämahyā gsm. DB 1.3, 5; DBa 4, 6.
arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200.
avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt 2°; рле, 1; DE 3; XPa 2; XPb 3; XPe 2; XPd 2; XPf 2, 28; XPh 2, 37; XE 4; XV 3; А?Ра 2f^; A’H 3; A*Pa 2f. avamsam DB 2.20, 821; 3.31, 85; 5.8. auahya gsm. DB 1.29; 3.70; 4.48f. алапа absm. DSf 81. араш npm. DB 5.15, 31°; DSf 48, 50°, 51, 53, 54. avaiy apm. DB 2.77; 4.69. avaišām gpm. DB 4.51.
avém asf. DSE 27; alva]m-c* (= -ciy, 852.1) DB 5.26; ava as asf. (856.V) XPh 33. [ора npf. DNa 39.
ava nsn. DB 1.20, 447; DNb 10, 11, 20, 22; DSf 42. ava-maiy DSj 4; 051 46. ava-di$ DNa 21; DSe 20°; XPh 19. avaš-ciy (89. VT, $105) DNb 55. ava asn. DB 1.62; DNa 20, 37, 49; DSa 4; DSe 19°, 32°, 34, 44°; DSf 20°; XPa 16; XPb 25; XPf 39, 42; XPg 10; XPh 18, 42. ava-taiy DB 4.76, 79. avas-cty DNb 5f, 57; XPa 20; ХРе 14; ХРЇ 48. арапа absn. DSe 88. avand isn. XPh 49, 51f.
’ava- prefix ‘away, down’: GAv. avd, LAV. ava, Skt. dva; with verbs ar-, *kan-, gam-, jan-, à-jan-, !rad-, sta-, hard-. Cf. JAOS 62.274-5,
avd adv. ‘thus’, correlative to уаба: perhaps isn. of !а0а-, but more probably error for атаба ($52.УТ), by omission of one character, as taken by MB Cr. $59; see also avdkara-. DB 4.51.
OLD PERSIAN
avakanam, see ?kan-.
avdkara- adj. ‘of such sort’: avd ‘thus’ + kara- ‘doer’ (§160.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in haka
=== leaf 196 ===
's avabäštā adj. apm. 'thus standing".
avadà (ie. avadá) adv. ‘there, then’: LAv. атаба; from 'ava- + suffix seen in OP «dà (319.1). Usually resumptive of an immediately preceding place-phrase, which is thus made locative (so al- ways in DB except 1.85, 88; 2.24; 3.74; 4.81; 5.24, 28). See also avadasa.
(1) ‘there’: DB 1.85, 88, 92; 2.9, 23, 24, 28, 34, 39, 44f, 54, 59, 66, 96; 3.5, 23, 34f, 44, 61, 66; 4.81; 5.24, 28; XPh 40. avada-Sim (8135) DB 1.59; avadd-Sim DB 3.74; avada-šiš DB 3.52.
(2) ‘then ’: DNa 42.
avadasa adv. ‘from there, from then’: avadd- + abl. -ša (5191.1; ВЫ, AiW 170, with lit.; against his view, Ву. Gr. §325), always after hacd. (1) ‘from there’: DB 1.37; 342, 80; DSf 47. (2) ‘from then’: DSe 47f.
LEXICON
avaparü phrasal adv. ‘along there’: ava asn. + postpos. pard (S191.IV). DB 2.72; 3.792.
avastü- sb. ‘leather’ (König, Klotho 4.45-6): etymology uncertain ($145). avastlälylä] 15. DB 4.89f (JAOS 62.267); hardly стаз уот) as read and restored by KT, which could be only an un- augmented imf. of ava- + stā-. Probably not а reference to the Avesta, as suggested by Wb. ZDMG 61.730.
dvahana- sb. ‘village’ (5166): deriv. (8147.1) of à + vah- ‘dwell’, Av. vah-, Skt. vas-, Gm. Wesen ‘being’. dvahanam DB 2.33; DSf 46.
avahar|da| DB 2.94, see hard-.
avahya- denom. vb. ($217) ‘ask for help’: Av. avahya-, Skt. avasya- in dsm. pres. ріс. avasyaté (RV 1.116.283), to Av. avah- ‘aid’, Skt. dvas- (Jn. JAOS 27.190, MB Gr. §209, Bv. Gr. $193). pali- + avahya- ‘ask for help’: patiydvahyaty ($140.11) Ist sg. imf. mid. DB 1.55.
avahyarddty phrasal adv. (§191.1V) ‘for this reason’: avahyd ($185) gen. of !ava-, + rüdiy ‘on account of’, q.v. For phrasing, cf. Gk. rovrov évexa, robvexa, Lt. huius ret causd; JAOS 35.322-9. DB 1.6f, 51; 4.47, 62; DBa 9f.
asa- sb. ‘horse’ (590, $143.IIT): Med. aspa-, Av. aspa-, Skt. déva-, Lt. equos, pIE *ekyos. See also Asagarta-, asabüra-, aspa-. asam asm. (col- lective, $255) DB 1.87.
Asagarta- sb. ‘Sagartia’, a northwestern prov- ince of the Persian Empire (§29.n2, $81): Elam. ad]. a&-Sa-kar-tt-a, Akk. adj. sa-ga-ar-ta-a-a, Gk. Yayapria. Probably asan- ‘stone’ (with Med. s < pIE Ё; $9.1, 587) + *garta- ‘cave’ (Skt. gdria-), ‘Land of Stone-Cave Dwellers’ ($161.10, §166.1; Bthl. AiW 207, zAiW 119-20); hardly asa- ‘horse’ (with OP s < plE ky, §90) + *garta- ‘wagon’ (Skt. gária-), ‘Land of Horse-drawn Wagons’. See also Asagartiya-. Asagartansm. DPe 15. Asagartam asm. DB 4.23. Asagartaty lsm. DB 2.80f; 4.22; DBg 8f.
Asagartiya- adj. ‘Sagartian’: adj. to preced-
ing (§144.111, $159). Asagarfiya nsm. DB 2.79;
4.20f.
asan- sb. ‘stone’: plE *aken- (§9.V, $87, §155.1), ef. asman-. See also Asagaria-. ай (8124.5, $187) nsm. DSf 40f; but see also under daru-.
173
asabára- sb. ‘horseman’: NPers. suvdr, cf. also Tedesco, ZII 2.40-1; asa- ‘horse’ ($126) + bára- 'earri
=== leaf 197 ===
3. asmanam (853) A?Pa 3.
ašnaiy adv. ‘near’, lsn. of ašna- ‘near’ (Hz. Ap] 98-9), Av. dsna- ‘near’, in loc. dsnaé-ca, asne ‘near’, abl. asna ‘from near’; from pAr. root end- ing in $ or 2 (pIE Ё or ў: Skt. aánóti ‘attains’ and djatt ‘drives’ hardly suit); not *à-zd-na-, pte. to à + *had- ‘herangehen’ (Bthl. AiW 1755; but *had-, which always has prefix d, is only a semantic vari- ation of thad- ‘sit’), cf. Skt. dsanna- as adj. ‘near’ (Bthl. AW 220). Possibly from plE *afijh- ‘choke, throttle’, cf. Lt. атаб, Gk. &yxw, sb. Lt. angor, Av. azah-, Skt. qhas-: *afijh- + pte. -no- (806, §147.1, $191.11I, $243); for semantics, cf. Gk. &yx« adv. ‘near’ (JAOS 62.276-7). Not ‘on the march’, to pAr. root *aé-, Skt. djatt, Lt. agit (Bthl. А 264); nor ‘m friendship’ on the basis of the Elam. kanna ети git (WB; KT); nor ‘at peace’, cf. Av. dxsitd ‘peace’, dx Sta- ‘peaceful’ (Ву. BSLP 31.2.67-9). Elam. kan- recurs as the translation of dausid ‘friend’, but this meaning eliminates only ‘on the march’, since ‘friendship’, ‘peace’, and ‘nearness’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
агай adv. “known ОСА: azdà "thus", Phi. ага,
174
Skt. addhá ‘surely’, from pAr. *adzdhà (885); cf. MB Gr. §118. DB 1.32; DNa 43, 45; DNb 50.
tah- vb. ‘be’: Av. ah- Skt. as-, Gk. tert, Lt.
esl, Gt. ist, pIE *es-. See also hafya-, А@їуй- bau$na-. Conj., $208.
amiy ist sg., Av. ahmi, Skt. dsmz, Gk. Lesb. tume, Att. eui, NEng. am (5118.11, $226.1): AmH 9; DB 1.12, 39, 53, 75, 79; 2.10, 15, 80; 3.25, 81; 49, 11, 14°, 17, 19, 22, 25, 27, 30; DBb 5, 7; DBe 8f; DBd 4f, 7; DBe 6, 9; DBE 4f; DBg 7f; DBh 5f, 9; Рві 6, 10; DB} 5; DNa 35; DNb 6f, 7, 8, 1f, 13, 15, 26, 27, 34, 40, 42, 43, 44, 51; Die Т; A? He 18.
азу, Ау. asti, NPers. dst, Skt. ásti (5116, 5228.1): DB 4.46, 51; DNb 54f, 56; DSe 37; XPh 30.
a'mahy, Av. mahi, Skt. smds-1, Gk. Dor. dues 8118.11, §230.1): DB 1.7f, 11; DBa 12, 18.
ha"tiy 3d pl, Av. honti, Skt. sánti, Gk. Dor. iy i, Ове. sent ($89, §122, §232.1): DB 4.61, 63°.
Gham ist sg. imf., Skt. ham, Gk. Hom. ўа (867.II, §122, 6226.1): DB 1.14; 2.6, 12; 377; 4.63 bis, 64. алат XPh 15f ($53, $131; hardly with Hz. AMI 8.65, ApI 63-4).
аһа imf. *éset (5228.11), but Av. às from *ést: DB 1.21, 22, 29, 30, 36, 45f, 48, 62, 86, 89; 2.13, 181, 19, 24 bis, 94, 95; 3.8, 30, 70; 4.8; 5.20; DNa 38; DSe 32°; DSf 16, 57°; DSj 3°, 4, 4^; DSI 5; DZc 19°; XPF 18, 19, 22, 30, 38; XPh 35, 42.
dha" 3d pl. imf., Skt. dsan (5239.1: §274.n1): DB 1.8 (8259), 10, 38, 42, 56, 90, 96; 2.27, 36, 42, 47, 56, 70, 98; 3.19, 40, 47, 63, 69, 89; 4.51; 5.15°, 31°; DBa 18, 16; DNa 39°.
üha"tá За pl. imf. mid. ($236.11, §274.n1) DB 1.19, 58; 2.77; 3.75, 90°, 02; 4.81; XPf 29. алача (636.1Уе) DB 3.49, 51.
ahaniy 19% sg. subj., Skt. ísánz (5226.1): XPh 47, 48 (-d- extended from rest of tense, acc. to Ogden ap. Kent,
```


## [2026-09-06T21:20:22.883Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /x[SŠš]a[cç]a-? *sb|xSaya.iya- *sb|Xsayar[s5S]|Xšayārš/ {print \"=== leaf \" NR \" ===\"; print substr($0,1,4000)}' KNT.txt | head -120"
}
```


### [2026-09-06T21:20:26.104Z] TOOL RESULT

```
=== leaf 39 ===
e constructio ad sensum rather
than syntactical error; examples in $258.IIT. V. Miscellaneous errors concerned with cases
and genders:
AmH 2 Parsd for loc. (§314.b); 5 tya as asf. (= уат); 81 уат dahydus, nom. for loc. (8814.b).
AsH 2 Рага, nsm. for isf. (852.1); 9 tya ukdram uvaspam, nt. for fem. буйт ukdrém waspam (possibly by imitation of the phrasing seen in DSf 11, where the agreement is with nt. z5acam). І
XPh 33 ava (for айт) dahydvam.
АЧ hya (пега. for gsm.) imam (asm. for nsm. iyam) bdtugara siyamam (asm. for nsm. -ma).
A’Se 4f [тат (asf. for asn. ima) hadiš; 6 tya (for asf. уйт) afagainàm.
Аа 3 imam (asf. for nsn. ima) hadi’.
CHAPTER Ш.
$58. Tug PIE Souwps, whose history will be traced down into OP, were the following:
1, Vowels: pure  semi-consonantal short: eoa | iur[mn reduced: 39 long: 200  Vürlmi
IJ. Diphthongs: short: e? o1 ai at eu ow aw au long: 2100014  ёибийи III. Consonants: voiceless voiced non- aspi- non- asp. rate — asp. asp. Stops Nasals labial р ph Б № m dental { h d di n palatal k fh ĝ jh À pure velar 9 gh g gh | a labiovelar @ qth g g*h Clusters dental ist isth бй ага Continuants (voiced, except s) sibilants 8 2 liquids lr semivowels ju
Remarks on the list of pIE sounds:
OLD PERSIAN
A'Ha 7 imam (asm. for asn. ima) iya; so also : А%а 5 (restored). : АзРа 22f imam ustasaném afaganam (for nom. : iyam ušlašanā adagaind) müm (perhaps for . mana) upd mam kartā. ; A3Pa 26 {уа mam kartā (perhaps for mand kartam). : $67. NEOLOGISMS IN THE LATER INSCRIPTIONS, . that is, after Xerxes, may perhaps be counted аз : errors, though susceptible of explanation. There : are the following, all new formations for the . genitive—presumably after the gen. zšāyaðiyahyā, with which the genitives of the royal name were constantly associated, and gen. Arlazsagahyá:
 Haxámanisahyá AmH 3f.
Düárayavausahyà in A'I, A’Sa, А?Не, and re- stored in Ае; Dárayavasahyà in А?На.
Xšayāršahyā їп A‘'Pa, АЧ, A?Ha; Xšayärcahyā ($49b) in A’Sa; XSaydrsahyd ($187) in A*Hc.
PHONOLOGY
A. I have omitted from this list (a) Brugmann's р ph ё Bh; sounds of problematic nature which are posited to explain the occurrence of dental stops in Greek corresponding to sibilants in other ЈЕ languages; (b) Sturtevant’s г and preaspirated continuants,? which also explain only certain peculiarities of development in Greek; (c) Brug- mann’s sh and zh? from s after voiceless and voiced aspirated stops, no distinctive product of which appears in any IE language; (d) short and long vocalic й and т, since they were non- phonemic, and so rare that they seem not to occur in the extant words of OP.
B. Not all the sounds in the list were phonemic: ñ and » developed only from a nasal standing before palatal and velar stops respectively; z developed only from s before voiced stops and after voiced aspirated stops, and in the voiced dental clusters.
C. There is no need for a special symbol to denote velar g, since the Aryan developments (873.I-III) distinguish velar g from palatal ў.
D. The dental clusters were clusters consisting
1 Brugmann, Gdr.? 1.790-3; cf. §102. ? Sturtevant, ІН Laryngeals §80b, 573-577. * Brugmann, Gdr.? 1.721, 124;
PHONOLOGY 25
of three phonemes each, but of such peculiarity in their developments in the separate languages as to deserve places in the list; they originated in pre-Indo-Hittite from the following combina- tions:
isi <ttdt
isth < th-t th-th t-th d-th
dzd < t-d d-d
dzdh < dh-t dh-th dh-d dh-dh th-d t-dh th-dh d-dh
The most important of these are the combina- tions of t d dh with ¢ of a suffix.
E. Of the ‘reduced vowels’, ъ is a reduction of e; ъ is a reduction of 0; ə is a reduction of ё 0 d.
$59. Tae О1р Psrstan Sounpbs are repre- sented, in the normalized orthography, by the following equipment of graphic signs:
Vowels: atu adit D
=== leaf 69 ===
ed on -vand- (pIE -џепі-) or on zero grade $
ES OM = AM epu ein bo Ny SNS БАМЫ
paps PEE Rs
pro Se yok
also in A'ura- d
-vat- (pIE -021-); more probably they are made -
upon vat-: ar-uwant- in aruvas-ta-, sikaya "-want- in `
Sikaga^uval-i-, hara^-uvant- in Hara*uvat-i-. )
NOUN STEMS 58
$168. OTHER Noun AND ADJECTIVE STEMS END- ING IN CONSONANTS are to be found listed among Root Nouns and Adjectives, $142.
5169. Noun AND Apsective COMPOUNDS IN ОР, apart from phrasal adverbs (§191.1V), may have as prior element an inseparable adverb as in a- zsata- ,"u-cüra-, dus-iydra-, ham-arana- (8268); or a prepositional adverb, as in apa-dàna-, pati-kara- (5268); or a noun or adjective stem! They have as second element a noun or adjective stem, which may receive an additional suffix.
Only compounds of stem + stem will be here discussed. Either stem may itself be a compound; either stem may already have one or more suffixes. The initial syllable of the first element, especially in adjectives, may show vriddhi or lengthening of the vowel, as in dáraniya-kara- ‘gold-worker’ to daranzya- ‘gold’; less often this appears in the sec- ond part, as in Baga-yadi- 'god-worshipping (month)’, where it is seen in both parts, and in asa-bàra- ‘horse-borne’, where it indicates passive meaning.
Compound adjectives with second elements of a specific gender assume the genders of their de- rived meaning and use, with change of form if necessary. Thus the masc. name Hazd-manis
‘Having the mind of a friend, Achaemenes’ has a
neuter stem as its second element, used without change in the masculine adjective as noun; the masc. adjective tigrarauda- ‘wearing a pointed cap’ has as second element the fem. zaudà- ‘cap’.
Derivative adjectives to compounds may be made by the addition of suffixes; Haxamanis-iya- ‘Achaemenian’ to Hazámanis-, Asagart-iya- ‘Sa- gartian’ to Asa-garia-.
Compounds of stem + stem, so far as they oc- .
cur in OP, may be divided into (1) Determinative Nouns and Adjectives, dependent and descrip- tive; (2) Possessive Adjectives, dependent and
! In Cica-tazma- the prior element is not the bare Stem, but the stem with an added nasal, attested in the transliterations into Elam., Akk., and Greek. This nasal ean hardly be the acc. ease-ending (as tentatively sug- gested by Bthl. AiW 587); it seems unexplainable except as a transfer from some other ера, in which & nasal in this position was justified (Schulze, KZ 33.216.n3; Richter, IF 9.208-4; Foy KZ 37.504-5). Cf. Gk. 'Aprga- Bápys (Hdt. 1.114-6, 9.122; Aesch. Pers. 29, 302, 971) = OP *Artam-bara ‘Aria-upholder’, where the prior ele- ment seems to be in the accusative (ef, Stonecipher, Graeco-Persian Names 27).
descriptive; (3) Participial Adjectives, the prior element governing the second. Adjectives of all these classes may become nouns аз names of per- sons and places.
The following will not be dealt with here, be- cause of uncertainties or difficulties in their inter- pretations; but some information may be found in the Lex. s.vv.:
Common nouns: d6ahavaja, ^uàdà-.
Personal names: Ka™bijiya-, Gaumáta-, Cišpi-.
Place names: Uvddatcaya-, Uvürazmi-, Paifi- yauvada-. |
Personal and place names of Elamite, Akkad- ian, and Armenian origin also cannot be discussed among OP compounds.
$160. DETERMINATI VE NOUNS AND ADJECTIVES, compounded of stem + stem; the prior element determines or limits the second.
I. Dependent determinatives, the prior element standing in some case relation to the second:
a. Accusative:
hamarana-kara- ‘battle-making’; züra-kara- ‘evil- doing’; ddraniya-kara- 'gold-working'; ciyd- kara- ‘doing how much’, ava-kara- ‘doing that’.
arSti-bara- 'spear-bearer'; vaga-bara- ‘bow-bearer’ ; taka-bara- ‘petasos-wearing’.
z5aca-püvan- ‘kingdom-protecting, satrap’; du- varði- (for *duvar-varði-) ‘doorway-covering, col- onnade’; hauma-varga-, maz-dah-, bátu-gara-, see Lex. s.vv.
Arta-vardiya- ‘J
=== leaf 170 ===
m?yà : vazrakáyà : 5 Vištāspahyā : pu
DZc = Darius, SUEZ C.
147
6 ca : Haxdmanistya TRANSLATION OF DZb: ... (= ing two words).
DNa 8-12, lack-
1 baga : vazraka : Auramazdà : һуа : avam : asmànam : ada : һуа : imam : büm
2 im : ada : һуа : martiyam : ada : hya : šyātim : ada : martiyahy
3 à : һуа : Darayavaum : XSyam : akunaus : hya : Dárayavahaus : Хуй : xfaga 4 m : frübara : tya : vazrakam : tya : waspam : umartiyam : adam : Darayavaus :
5 XS : vazraka : XŠ : XSyanam : XŠ : dahyünám : vispazanünàm : XŠ : ahyay 6 à : bümiy& : vazrakáyà : düraiy : apiy : Vistáspahyá : puça : Ha
7 ximanistya : бу : Darayavaus : XS : adam : Pürsa : amiy : acá : Pa
8 rsà : Mudráyam : agarbayam : adam : niyastayam : mam : yauvtyá
9ш: katanaiy : haca : Piráva : nàma :
rauta : tya : Mudràyaly : danuvatiy : ab
10 iy : draya : tya : haeá : Рагва : aitiy : pasdva : iyam : yauviya : akaniya : 11 avafá : yaf : adam : niyastàyam : utd : nāva : àyatà : haca : Mudra 12 уй : tara : imam : yauviyim : abiy : Pársam : араба : yatà : mim : Ката : dha
| Nores то DZc: The Fragment has *' ^ albiy [: draya
and #1 akani}ya : a|vafà. š
TRANSLATION OF DZe:
$1. 1-4. ... (= РМа 1-6, with one change of order); who upon Darius the King ... (= DSf 11-2).
82. 4-7. ... (=DNa 8-18).
§3. 7-12. Saith Darius the King: I am a Per- sian; from Persia J seized Egypt; І gave order to dig this canal from a river by name Nile which flows in Egypt, to the sea which goes from Persia. Afterward this canal was dug thus as I had ordered, and ships went from Egypt through this canal to Persia thus as was my desire.
DE = Darius, ErvEND.
1 baga : vazraka : Auramazda 2 : һуа : imam : bümim :
3 ada : һуа : avam : asmá
4 nam : ada : hya : martiya 5 m : ada : hya : уай
6 m :adà : martiyahya :
7 hya : Dàrayavaum : xšāya 8 булаш : akunaus : aiva
9 m : parünàm : х$йуа@ 10 iyam : aivam : parünàm 1l : framátàram : adam : 12 Dàrayavaus : xSdyaai 18 ya : vazraka : xSdya6tya : 14 xSiyaüryànàm : xà
15 dyabiya : dahyünüm : pa
16 ruzanànàm : х$йуаб
17 iya : ahydya : bümiy
18 à : vazrakayà : düraiy
19 :apiy : Vistaspahy
20 à : puça : Haxamanisiya TRANSLATION OF DE:
§1. 1-11. ... (= DNa 1-8). 82. 11-20. ... (= РМа 8-10), containing many men, ... (= DNa 11-3).
DH = Darius, HAMADAN.
1 Dürayavaus : XS : vazraka : XS : XSyanüm
. XŠ : dahy ^
2 üvnàm : Vistispahya : puça : Haxāmanišiya :
3 айу: Darayavaus : X8 : ima : x agam :tya :
ada
4 m : dárayàmiy : һаса : Sakaibiš : tyaiy : pa
5 ra :Sugdam : amata : yité :à : Kūšā : һас:
Hida
: tyamaiy :
Aurama
7 zdà : {тарага : һуа : таба : bagānām : m 8 ām : Auramazda : pàtuv : utàmaiy : vitam
6 uv : amata : y8tà : à : Spardà
Nore то DH: Our text follows the line-divisions of the copy on the gold plate.
TRANSLATION oF DH: $1. 1-2. ... (= DPh 1-3). $2. 8-8. ... (=DPh 3-10).
XPa = XERXES, PERSEPOLIS A. 1 baga : vazraka : Auramazdà : һуа : imam : bimim->a
```


## [2026-09-06T21:20:30.784Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=200 && NR<=215 {print \"=== leaf \" NR \" ===\"; print substr($0,1,200)}' KNT.txt"
}
```


### [2026-09-06T21:20:32.699Z] TOOL RESULT

```
=== leaf 200 ===
 by Hz, ApI 71-2).
ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasia
=== leaf 201 ===
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.
Uvárazm
=== leaf 202 ===
to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25.
Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadocian’: Ela
=== leaf 203 ===
om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24.
akariya imf. pass. (585.1, §9
=== leaf 204 ===
ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, desp
=== leaf 205 ===
, 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21,
181
28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 62, 67 bis, 70, 72, 7
=== leaf 206 ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, р
=== leaf 207 ===
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- 
=== leaf 208 ===
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-c
=== leaf 209 ===
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, 
=== leaf 210 ===
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-
=== leaf 211 ===
1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16.
=== leaf 212 ===
 word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
See also wla
=== leaf 213 ===
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.
=== leaf 214 ===
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for
=== leaf 215 ===
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.
Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.
dahy
```


## [2026-09-06T21:20:37.869Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=204 && NR<=206 {print \"=== leaf \" NR \" ===\"; print}' KNT.txt | grep -n \"xša\\|xSa\\|zSa\\|x8a\\|xáa\\|Xšay\\|X8ay\\|Xsay\" | head -40"
}
```


### [2026-09-06T21:20:40.152Z] TOOL RESULT

```
29:‘possesses’, Gk. xraoua ‘I acquire’, кттна ‘piece of property’, pIE *gbei- (§102). See also zšaça-, z5dyafiya-, XSaydrsan-. xSayamna nsm. ptc. mid. (§213, §241) DNb 15.
30:upari + xšay- ‘rule over’: upariyalxSayazy] 1st sg. imf. mid. DB 4.64f. (Tm. Lex. 85) is an er- roneous restoration for upariyalyalm as read by Cameron (already conjectured by Wb. KIA 66, ZDMG 61.729). |
50:X Saya[rsiha] gsm. XPi; [XfayárMüha XH. X Saydrsahyd ($57) А!Ра 14f; АЛ bis; A?Ha 3, 3f. Xéayárcahyü (849b) A’Sa 2 bis. Xšayāršähyā А?Не 12, (as nom., $818.1) 12f. Xarsada&yà, q.v.
```


## [2026-09-06T21:20:42.274Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=204 && NR<=206 {print}' KNT.txt | sed -n '20,60p'"
}
```


### [2026-09-06T21:20:44.046Z] TOOL RESULT

```
m
LEXICON
Éa-at-tar-ri-da, Akk. ha-5a-at-ri-it-t; shortening of compound name ($145, $164.TIT) such as *X saéra- dára- (foundin Phl., cf. Justi, INB 176). Хата nsm. DB 2.15; 4.19; DBe 6.
тќас̧а- sb. ‘kingship, kingdom’: Av. zšaðra-, NPers. šähr ‘city’, Skt. ksatrd-, pIE *gpetro-, deriv. of root in OP aSay- (§78, §148.III). See also Artazšaça-, XSafrita-, xXagapávan-. — r$acam nsn. DB 1.44, 45; DPh 4; DH 3. z3agam asn. DB 1.12, 25 bis, 26, 41, 42f, 50, 60, 61, 80f; DPd 3; DSf 10f; DSm 3°; DSp 2°; DZe 3f; XPa 19; XPb 291; XPd 19; XPf 46; XPg 14; XSe 5; XV 27°; A'Pa 24^; Ас 18, 19f. zšaçam-šim DB 1.59.
z5acapüvan- sb. ‘satrap’: Gk. сатраттв; x3aqa- + root pä- ‘protect? + suffix -van- (§155.IV, 6160.19). =ёас̧араәа nsm. (§124.5, §187) DB 3.14, 56.
z3an- vb., see axsata-.
aSap- sb. ‘night’: Av. zšap-, NPers. 40, Skt. ksap- ($102, $142). зарад gst. DB 1.20 (for case, 5188.11, cf. Skt. gen kgapas . . . usras ‘night and day’, RV 6.52.15, 7.15.8; gen. riming with ace. rauca in phrase, $318, rather than acc. zšapam re- made to zšapa to rime with rauca).
asay- vb. ‘tule’: Av. zíü(y)., Skt. ksdyate
‘possesses’, Gk. xraoua ‘I acquire’, кттна ‘piece of property’, pIE *gbei- (§102). See also zšaça-, z5dyafiya-, XSaydrsan-. xSayamna nsm. ptc. mid. (§213, §241) DNb 15.
upari + xšay- ‘rule over’: upariyalxSayazy] 1st sg. imf. mid. DB 4.64f. (Tm. Lex. 85) is an er- roneous restoration for upariyalyalm as read by Cameron (already conjectured by Wb. KIA 66, ZDMG 61.729). |
pali- + z$ay- ‘have lordship over’: patiyarša- yaiy lst sg. imf. mid. ($213, $238.11) DNa 19; DSe 171; XPh 17.
asdyabiya- sb. ‘king’; possibly in original adj. use, ‘royal’, DB 1.8 (Bthl. AiW 553): рАг. *kšäzatia- (Med. -0у-, Bv. Gr. $147, Hz. AMI 3.97; not orig. -0110-, as Mt. Gr. $147 had it), to root in OP zšay- (59.111, 580, $126, $144. VT). xsayabiya nsm. AmH 1, 1f, 2, 4, 8, 10; AsH 1, lf, 2f, 5; CMa 1f; CMb 1°; CMe^; DB 1.1 bis, 2 bis, 4, 6, 9, 11, 12, 13, 14, 18, 21, 24, 27, 277f, 29, 35, 44, 48 bis, 60, 61, 71f, 72, 78, 75, 76, 81f, 83, 90f; 2.1, 5f, 8, 11, 11°, 14, 17°, 18, 29, 37, 48, 49, 91, 64
, 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21,
181
28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 62, 67 bis, 70, 72, 7161, 80, 86f, 87, 88; 5.1, 3f, 14f, 18, 20f, 301, 34; DBa 1, If, 2, 21, 5, 9, 14; DBb 6; DBc 6f; DBd6f; DBe 9; DBF 5f; DBg 6f; DBh 8f; DBi 9f; DB) 4f; DPa 1, 2, 3; DPd 5, 6, 19; DPe 1, 2, 3, 6, 19; DNa 8, 9, 10, 11, 15, 31, 34, 40, 48; DNb 5f, 59; DSb 2, 3f, 5f, 7; DSI lf; D8m 6°; DE 12f, 13, 14f, 16f; XPa 6, 7 bis, 8, 11, 18; XPb 12, 13, 14f, 16, 22; XPd 9 bis, 10, 11, 15; XPe 1, 2; XPf 8f, 9, 10, 11f, 16, 25f, 28, 35, 36, 44; ХРе 2, 6; XPh 7, 7f, 8, 9, 14, 15, 29, 29f, 56f; X82 1, 2; XSc 1°, 1, 1f°, 8°, 3f°; XE 121, 13f, 14f, 16; XV 10 bis, 11, 12f, 17, 17f; A!Pa 9°, 10°, 11°, 12°, 171, 20; Ае 2, 2°, 3, 4; A*Pa 5f ($2478), 9 bis, 10, 11, 21f, 24; Wa 3f; Wb If, 2f, 4f, 5f; We 2f, 3f, 5f, 6f; Wd 3, 4, 5f, 6f; AVsb-d.
z5dyaüiyam asm. AsH 7f; DPd 2f; DNa 5, 6f, 391; DNb 4f; DSm 4; DSt 5f°; DE 7f, 9; XPa 4, 5; ХРЬ 7f, 9f; XPd 5f, 7; XPf 5, 6f, 281; XPh 4f, 5f; XE 8, 10; XV 6, 7f; А!Ра 6°, 7°; MPa 7.
asdyahiyahya gsm. AmH 3; AsH 3f; CMb 2; DB 3.59; DPd 10f; DNe 2; DNd 1f; XPa 10; XPb 19f; XPd 13f; XPe 3f; XPf 14; XPh 11; XSc 2; XE 191; XV 15; А!Ра 15°, z5iyatiya as gsm. ($818.П) АзРа 121, 14, 15, 16, 17f.
хїйуабтуб npm. DB 1.8 (or nsf. adj. ?), 10, 10; 4.51; DBa 13, 16, 17f.
тїйуабёшй apm. DB 4.7, 32.
asayahiyandm gpm. AmH 2; AsH 2; DB 1.11; DBa 2; DPa 2f; DPe 2f; DNa 9; D8b 4f; DE 14; XPa 7; XPb 13f; XPd 10; XPe 2f; XPf 9; XPh 8; XSc 1; XE 14; XV 11; A!Pa 10f°; Wb 3f; We 4f; Wd 4f. zíayatiyanám (552.11) А? 2f; A’Pa 10. On the title "king of kings', see von Wesen- donk, Or. Stud. Pavry 488-90.
XŠ пз. (842) DPb; DPh 1 ter, 4; DSa 1 bis, 2, 3; DSc bis; рва 1 bis, 1° bis, 3°; DSe 8°, 8, 9°, 10°, 14°, 31°, 42, 50°; DSf 6 quater, 8, 55°; DSg 1° quater, 3°; DSi 1, I? ter, 3; DSj 1 bis, 1°, 2°, 5; DSk 1 bis, 2, 4; DSm 1° bis, 2°, 3°; Обр 1°; DSo 3°; DSt 7°, 10°; DSy 1 bis, 2 bis; DZb 1, 2 bis, 3°; DZe 5 ter, 5°, 7; DH 1 ter, 3; ХРе 6 ter, 7, 10, 11; ХР} quinquies; АЧ ter; D’Sa 2°; D’Sb 1° ter, 1, 8°; А?8а 1 quater; A’Sb ter; A?Sd 1 quater, 2; A*Ha 1 bis, 1° bis; A?Hb; A?He 7, 8 ter, 16 bis; SDa; SXa 2; SXb 2; SXc 1; XVs; AVsa.
Хт asm. DSe 5, 6; ХРе 4, 5; D'Sa 3; А?Не 5, 6. XSyam DSf 4, 4f, 10, 15; 17; DSi 8°; DSn 2; DSp 2; DZe 3.
182
Xšyā gsm. DZc 3; A!He 10, 11, 12,13. X Shyà DPe; DPi; ХРе 9, 14; XP^; XPk; XH; АЧ bis; D'Sb 2°; A’Sa 1, 2 bis, 3; A'Sb; Ае 0; A?Ha 2, 3, 3°, 4. XSahyi (853) А84 2. XSyahya XP}; XSyahiya (827) XPjv. XS as gsm. (8313.1) A!Hb.
XSanam gpm. XPc6. XSyánàm Га 11; DSc; DSd 1; DSe 8f; DSf 6; DSg 1°; DSi 1°; DS} 1; DSk 1f; DSm 1°; DSy 1; DZb 2; Рӯе 5; ХР}; АЧ; D'Sb 1°; A’Sa 1; A'8d 1; A?Ha 1°; A’He 8. XSyanam (§52.11]) DPh 1; DH 1. XSyana (§52.V) A?Sb.
X SaydrSan- sb. ‘Xerxes’: Elam. ik-Se-ir-28-Sa, АКК. hi-&-"-ar-áa, Gk. ép£ns: from хќауа- ‘king’, Ау, z&aya-, to root z$ay-, + arsan- ‘male’ ($181): ‘Hero among Kings’, cf. Skt. rdja-rsabha- (Bthl. AiW 550; but Hz. AMI 1.121n, Bv. Gr. §290, take second part to be arša- ‘just’, on which cf. §162.n1, $187.n2; ef. also Hz. AMI 7.82-137, esp. 135-6, on which see Henning, BSOS 10.502-3). Decl., 6187.
Хїауйгёй пэт. XPa 6, 11, 17; XPb 116, 21, XPc 6, 9; XPd 8f, 15; XPe 1; XPf 8, 15, 27, 44; XPg 1; XPh 7, 18, 28f, 56; XP} bis; XPk; XSa 1; XSe 1°, 3°; ХЕ 12; XV 9, 16; А!Ра 19f; A?Pa 16, 16f (both as gen., $313.ITI); Ха 1; SXb 1f; SXe 1; XVs.
XSayarsam asm. XPa 4; XPb 7; ХРе 4; XPd 5; XPf 5; XPh 4; XE 7f; XV 6.
X Saya[rsiha] gsm. XPi; [XfayárMüha XH. X Saydrsahyd ($57) А!Ра 14f; АЛ bis; A?Ha 3, 3f. Xéayárcahyü (849b) A’Sa 2 bis. Xšayāršähyā А?Не 12, (as nom., $818.1) 12f. Xarsada&yà, q.v.
тёпа- vb. "learn, come to know, know’: Av. xind-, Skt. jñā-, Gk. yeyrwoxw, Lt. gnóscó, NEng. know, pIE *gné- (806, $110, 8212). See also zínav-, dan-. | adünà imf. (NPers. dánàm, 568, $210) DB 1.51; DSq 3. x&ndsahy 2d
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
Gaubarwa- sb. ‘Gobryas’, ally of Darius against Gaumata: Flam. kam-bar-ma, Akk. gu-ba- ru-’, Gk. TwBpins; from gav- ‘cattle’ + *baruva-, cf. Skt. bharu- ‘lord’, to vb. bar- ($85.П, $101, $122, $142, $143.II, $150, $1581, $160.Ib): ‘Cattle- Possessor’ (Justi, IFA 17.111; otherwise Foy, ZDMG 54360). Gaubaruva nsm. DB 4.84; 5.7, 9, 11; DNe 1.
```


## [2026-09-06T21:21:08.723Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB leaf 93 (p.83) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==93 || NR==94 {print \"--leaf\",NR\"--\"; print}' HUB.txt"
}
```


### [2026-09-06T21:21:10.990Z] TOOL RESULT

```
=== HUB leaf 93 (p.83) ===
--leaf 93--
~ 82 —
795. Der Zusammenstellung stehen verschiedene Bedenken
entgegen. Nach der Analogie von np. kunam (= ap.
*kunaumii/ = iran. *krnaumi) : inf. kardan sollte man
np. *8unam (= iran. *8rnaumi, vgl. bal. sun-ay horen*) :
inf. *surudan oder surudan (das als causat. Inf. vor-
liegt, vgl. Nr. 735) erwarten. Den Lautgesetzen nach
ware np. Sunu-dan, pr. sinavam (sammt Neben-
formen), paz. snavesn *the hearing Min. Gl. 188, sna-
wasni Shk. 267, xsnudan „for aSnudan*" Shk. 254,
phi. ptc. Osnut ^) , pr. 3. sg. dsnpet (lies Osnavet),
pr. 3. pi. Osnupand (lies dsnavand) Gl. and Ind. p. 30
auf ein ap. *xsnavamiyy inf. *xsnutanaiy von einer
Wrzl. xsnU zuriickfiihren, die sich nicht mit zd. sru
vereinigen lassen wiirde. Ueber welche Hindemisse
man hinwegsetzen muss, um von sunudan auf die
Wurzel iran. sru zu kommen, zeigt Fr. Mil Her, WZKM.
4, 355. >
796. Lies zd. *xsaodraka" und ^xSaoda- (vgl. die Nachtrage
bei Horn, p. 259). Zd. "^xsaodraka^ ware im Np. zu
Hohra, *sOra geworden. Np. Sohar wird angelehnt
sein an pidar u, s. w. wie pusar, pisar (aus pus) etc.
Zu mazend. sf vgl. sivend. st *Gatte*, Journ. asiat.
1893, p. 257, kurd. s« ZDMG. 38, 76, kas. m Shuk.
p. 157.
799. Dazu g. siv-sar unter dem Kopf ZDMG. 36, 70, sTvend.
si unter (Journ. asiat. 1893, p. 254).
800. Vgl. bal. sSp-mar *eine Schlangenart' (Geiger Nr. 370),
np. mar i Sebd (KZ. 27, 107 Anm., Darmesteter,
Etud. iran. II, 221) = zd. azayo xsva^wMho *Vipem'
vd. 18, 65 (Spiegel 129) -= phi. mar (i) s(S)pah
1st phi. sSpak von mir und Darmesteter richtig fiir
s(a)pak der Ausgabe (Phi. Vd. 207, Z. 6 und 7 v. u.)
corrigirt, so setzt dies im Verein mit bal. sepmar ein
ap. *x8aipa- oder ^xsvaipa-- voraus, das dem skr. ksip ')
') Man konnte auch *xinui etc lesen, aber anlaut. xs war sohon
im Pehlevi zu s geworden.
') Dazu nach de Saussure MSL. 7, p. 76 auoh lat. aipare
'hinstrecken'.
--leaf 94--
— 83 —
noch nfther stehen wtirde als die KZ. 27, 107—108
besprochenen Zendfonnen, die zu einer arischen Wurzel
ksvib Oder kSvibh geh5ren.
801. Dazu arm. asxSt Vothbraun* (vom Pferd), phi. sBtvars
'rothhaarig Bdh. Gl. 192, kurd. SS Tuchs* (Pferd)
Socin, kurd. Samnil. II, 317, si 'alezan', hespisi 'un
cheval alezan* Justi-Jaba Diet.
803. Zd. xsa^rya- ist im Neup. durch sahn vertreten.
Also Ser 'L5we' davon zu trennen.
804. Phi. SSpOk (Jasna 61, 11) = ap.*ariaipa- oder *xsvaipa-?
Vgl. oben Nr. 800.
805. Arm. gund 'Abtheilung eines Heeres, Corps, Schar'
(bei den S^ltesten Schriftstellern) = arab. /wwd, pi.
junud^ ajndd 'Soldaten*, syr. guddd *Schar', mand. gunda
(N5ldeke, Mand. Gr. 78), phi. gund weisen in ihrer
Uebereinstimmung auf urspr. anl. g, nicht v, Im
Armen. findet sich g = pers. g aus v erst bei Schrift-
stellern des 7. Jhd., wahrend gund (mit g) im 5. Jhd.
belegt und vor diesem entlehnt ist. Daher Zusammen-
hang mit skr. vpida- oder zd. vq^toa- unwahrsehein-
lich.
806. Die Zusammenstellung widerspricht alien Lautgesetzen.
808. Lies ap. Vindafamd (im Nominativ, Thema Vinda-
famah-), Np. farrux gliicklich' = phi. farraxv setze
ich = ap. *fama(h)uvan' (mit Suffix van fiir ursp. vant),
vgl. WZKM. 7, 377 ; np. farxunda glUcklich' = phi.
*farraxvand'ak = ap. *farna{h)uvanta' aus *farnah-
vant?^) Die Nebenform farrah (von farr) geht nicht
auf ein phi. *farnak, sondern, wie np. farrihl *Herr-
liehkeit* zeigt, auf ein phi. ^farreh (vgl. syr. B^l^niB
Farrahanns N. pr. bei Hoffmann, Ausziige p. 72) =
ap.*/arwaAa- (oder ein ahnlich erweitertes farnah-) zu-
riiek, vgl. np. xurrah = paz. x^areh Min. Gl. {x^arehe
Shk. 255) = zd. x^arenaflha- (oder ein sLhnlich er-
weitertes x^arenailh').
*) YgL zd. ac^arenahha nom. sg., afarenafihvanta instr. sg.,
x'arenanhuniem = x^arenahhentem ace. sg.
6*
```


## [2026-09-06T21:21:19.087Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=197 && NR<=199 {print \"--leaf\",NR\"--\"; print}' HRN.txt"
}
```


### [2026-09-06T21:21:20.749Z] TOOL RESULT

```
--leaf 197--
- 175 -
in [/skar- dev PI), 'spähen, suchen, durchforschen,
Gegenden durchwandern, Iierumgehen', wa;^. sktlr-an},
sar. /kar-am. Die letzten Bedeutungen könnten auch
auf l/^rförr- (vergl. PW.) führen.
787. sikäften 'spalten', I^raes. sikäfeni i^Pgäf AM. S. 84
Zeile 7).
Ka§. vesköw (Inipt.).
phlv. skaft, y. 10 (29), vergl. patkaftan (AV.);
kurd. sikiwin, biskiwin aufblühen', sikeivf, askavf 'Höhle'
(H.-Sch.). LW. Sikaftm 'abtrennen, lostrennen, köpfen .
Zu gr. (Ty.d7iT(o 'graben, hacken (Nöldeke, münd-
liche Mitteilung). Durch diese schöne Entdeckung
wird die bisher nur für europäisch gehaltene Wurzel
slc^ap' bezw. sk-ah- 'schaben, graben* als indogermanisch
erwiesen. Die Bedeutung graben' ist bei np. käftev^
kämden (No. S:^^) noch erhalten^).
788. H'ikesten 'zerbrechen*, Praes. siken-ew,
aw. \^8caüd'^), scindai/^Urzerhrechen ; phlv. skastan
(Men.).
kurd. LW. sikestin, sikinändin (Causat.); oss. sädfjn,
sätfin 'brechen, bersten, zerbrechen' (221).
ap. *skanamij/ (aus ^skadnämiy)^ 9. Cl.; ai. [/'ched-
'spalten gehört nicht hierher, vergl. Hübschmann,
ZDMG. 38, 424.
sikuften, sikäften aufblühen* s. np. bisköfe (No. 223).
789. sei 'Schenkel', seieng (Sileng) ; vergl. selvär 'Hosen*.
gr. (jxfkog (Justi, Litbl. f. or. Phil. I, 65; aber
nicht gehört hierher arm. srwwÄ 'Schienbeine, Waden*,
srnapan '^vq^ii^^ vergl. Hübschmann, No. 260).
np. selvär ist weit entlehnt, vergl. öa(jäßapa (Photius,
Pollux u. ö.), arab. sarbäl, sarväl, kurd. selvär,
sarval, salval (H.-Sch.), af/. bei. (249) salvär, oss.
salbaro (H. S. 130), wa;^. savdlak, minj. soäl u. s. w.
*J Erst jetzt besteht Feistes kulturgeschichtliche Bemerkung
unter got. skahun (No. 499j zu Recht.
') So setze ich die Wurzel nach Barth olomae, Stadion II, 4,
97, 104 an.
--leaf 198--
— 176 —
790. suma 'ihr.
aw. ynsmäka-, gä»*^. /smäka- euer; päz. suma; ai.
yuämdka-; arm. yer 'euer (H. No. 176).
oss. d. sinaxy t. suma/ ihr, euch' (225); bei. savä-
"\\\v\ saraiy 'euer (365).
791. stifnar *Zahl, Anzahl', summden (mit her- erzählen*).
g. simärtmün; Kä§. V. veresmörtdn , Q. öresmärdeff^
K. esmördemün, Z. veresmdrt^),
aw. I/"r/?ar-, märay^iti 'bemerken, sieh merken*
(y. 32, 6); phlv. sVmär (vd. 9 (132) Gl.), vergl.
ösmartan^ ösmar (Bund.), anösmär 'ungezählt' (Men. 49,
22); ai. {^smar- gedenken'.
kurd. azmardin (H.-Sch.), zimärtin zählen'.
np. sumurden (gegenüber ämär^ mer) ist aw. aim-r-
mar- {aiwisrnaretö), das allerdings yt. 14, 34 eine ganz
andere Bedeutung hat; np. nehmür 'zahllos hat die
ursprüngliche Form der Wurzel, smor-, am Besten
erhalten. Wegen phlv. ösmartan darf bei sumurdmi
nicht Entstehung im Satzsandhi angenommen werden.
792. sinä, sinäh 'Schwimmen', sinär, sinärlden.
aw. l^snClr, US snayaeta 'sich waschen'; ai. l^snä-,
sndii- 'sich baden.
oss. t. nähi 'baden', d. a^snun^ t. a^snin 'waschen*
(196).
Die Nebenformen sinäb^ sinäv, sinävtden erklären
sich entweder wie deryäw (No. 561) oder sie gehen
auf [/^S7iav' {gi\ vsio 'schwimmen', äol. raa», vavftt
'fliessen') zurück.
np. s ist im Satzsandhi oder durch Übertragung
entstanden.
793. Hnäyiten 'erkennen', Praes. sinäs-efn, shuls.
ap. /snäsatiy 'solle kennen'; phlv. snäxtav, sfinaPf,
snäsüntän.
kurd. 7fäfiin 'erkennen*, ez dinäsim.
Gehört zur arischen [/'San- (wie ap. adma, np.
*) Nirgends findet sich in den Dialekten das np. //.
--leaf 199--
^_ 177 -
dänisfen). Über den Vorschlag des ap. ;^ vergl. Bar-
tholomae, Ar. Forsch. III, 20, Indog. Forscli. I, 185;
Fr. Müll er' s Bemerkungen dagegen (WZKM. 4, 309,
348) hat Bartholomae soeben schlagend widerlegt
(Indog. Forsch. II, 260 folg.). Ap. /Jnas- entspricht
genau lat. gnösc-ö,
795. Hunüden, senlden *hören', Praes. sunev-em, sinev-em,
usnüden , Tliy^^N'O (Is. 1 , 2) , sinuften , sunuften,
sinuväntden (AM. S. 261 Zeile 1).
g. äsnuftmün.
aw. l/^srar-, surunaoiti 'hören'; phlv. vergl. äsnütan,
asnuvet *hören [srütan heisst nur 'recitiren etc.*] ; ai.
l^p'av- gfnoH *hören*.
bei. stway (353).
Bartholomae, Studien II, 43 erklärt das np. s
durch Übertragung; Fr. Müller, WZKM. IV, 355,
ist wenig überzeugend.
796. Höher {*söhr) *Gatte'.
aw. ^ysaudraka-, vergl. ;^i'wc/rflf- 'Same', /sdudra-,
np. söi^) *Gatte', phlv. söl (vd. 15 (29) Gl.) setzen
ein aw. ^/sauda- voraus, das diosolbe Bedeutung wie
^'yjaudraka- hatte.
797. sehr \Stadt', vergl. s(~u\ säristdn, sdrsän (Sahn. I, 209
Vers 1431/5).
ap. xsatf'a- 'Reich, Land'; aw. /sa^ra-; phlv. snirj
mtrestän, päz. sahr, suhrastän (PI^Gl.), chald. ft^lTki'nx,
de Lagarde, Semitica I, 42; ai. Icsaträ-.
Allgemein entlehnt.
Ein altes sehri 'edel* (aw. yßatirya-, ai. HatHya-)
scheint noch durchzuschimmern im ar. LW. sahnyatun,
PL sahärty 'persisches oder kurdisches Ross' (de Goeje,
Bibl. geogr. arab. IV, 277).
798. sehryär 'Herrscher*.
aw. *xia3rö.dära' ; phlv. (Inschr.) satrdarän.
*) Reimt auf möt, 8ähn. I, 155 Vera 472, öi, I, 43 Vers IGT.
Mazend.-Dial. bat o'in aufTallip^o.'» s/, wio auch ;///• (*ITjijir') otc.
Uorii, Gruuilri.<<s d. iieiip. KtynioI<>(;-i(>. 12
```


## [2026-09-06T21:21:32.397Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN p.100 (leaf122) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==122 {print}' HRN.txt; echo; echo \"=== HRN p.171 (leaf193) ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=192 && NR<=193 {print \"--\",NR,\"--\";print}' HRN.txt"
}
```


### [2026-09-06T21:21:34.541Z] TOOL RESULT

```
=== HRN p.100 (leaf122) ===
--- 100 -^
Lässt sich lautlich nicht mit skr. kSupa- 'Staude,
Busch', wozu es vielfach gestellt wird, vermitteln ; nur
das kurd. sltv, sowie die Formen der Pämirdialekte
könnten zu dem Sanskrit stimmen.
449. eögän 'Schläger (im Ballspiel)'^).
Das Wort sei hier nur wegen seiner in semitischen
Sprachen vorkommenden Formen angeführt, welche
ich der Freundlichkeit Herrn Prof. Nöldeke's ver-
danke.
*syr. |W':51l^tDN (wie Fraenkel, Fremdwörter, S. 291
das entstellte ^''jlt'ICOl^N verbessert); arab. sauljän;
phlv. jNJIDIli (Kam.), wie vielleicht auch die np. Neben-
form öölgän in cöhgän zu emendiren ist. In jüngeren
arab. Texten (1001 Nacht) erscheint jNt'Di:!, das nicht
aus JNÄlli erklärt werden kann .
450. cun Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
phlv. digün *wie?* {ci + aw. gaona-), cigämh, vergl.
np. cigüne (vergl. zeryün aus aw. zairLgaona-, No.661).
451. ci(h), ci (AM.) was?, wie?\ cirä warum?*.
ap. üyakaram, -ciy (enclit.); aw. eis, cit; päz. ci/i
(phlv. no); ai. -6it (enclit.).
af}'. ca 'was?; einige*; oss. d. ci, ci, t. ci 'was, was
für ein, welch?' (322).
Als Encliticon hat Salemann, Mel.asiat.IX,241 altes
ap. ciy, aw. cit in den dialektischen tnvn ji auch ich*
(Lokalität Sih dih bei Isfahän), memc *ich auch*, öle
'er auch' (Güräni), sowie in mehreren gebräuchlichen
neupersischen Worten erkannt {kes, heö, hergiz^ mz^
egerci, herci temämter), die sämmtlich an ihrem Orte
aufgeführt sind. Im PehlevT wird das Encliticon noch
») Im Journal Bomb. Br. R. As. Sog. 1891, Vol. XVIII, 39 ff. hat
Jivanji Jamshedji Modi kürzlich die Stellen gesammelt, an denen
bei Firdüsl vom Ballspiel die Rede ist (The Game of Ball-Bai -- Chowgän-
gui — among the ancient Persians, as described in the Epic of Fir-
dousij.
') Cu ist metrisQh nur kurz, die Länge dazu ist cün (Rüokert,
ZDMO. 10, 133). Cünän z. B. äähn. I, 148 Vera 354, cümn 157 Vers 523.

=== HRN p.171 (leaf193) ===
-- 192 --
— 170 -
Die Ableitung von np. Mm aus aw. ysäfniya-
(üarniesteter, Et. ir. I, 82, II, 161) ist sehr an-
sprechend, wennschon mir eine Grundform ^/sampHya-
nicht wahrscheinlich ist. Bei einer so starken Con-
traction konnte auch schliesslich der auslautende Nasal
noch in Mitleidenschaft gezogen werden, vergl. np.
Behräm gegenüber Varahrän; g. cum bei Beresine,
II, 24, VIII, 1 ist gewiss erst sekundär wie cübän
statt sübän (No. 776).
769. San 'ihr (Enclit.).
ap. sam (Enclit.) ; phlv. -^dn,
770. sdnzdeh sechzehn'.
aw. /svasjlasa 'sechzehnter ; phlv. säncdahiim ^).
af/. späras ; kurd. LW. säfizdeh,
np. sänzdeh ist durch das ihm vorhergehende pämdeh
beeinflusst.
771. smie 'Kamm'.
Käs. K. yö\sen (?).
phlv. sänak 'Kamm' (AV.); gr. xrf4', icrivinv (Hesych),
indog. he-n (Hübschmann, ZDMG. 44, 560).
bei. sak *Kamm' (445), dagegen LW. sänug 'Pferde-
strieger (866).
772. sah 'König, Herrscher, sähäne, sälü, sähin 'Falke'-).
ap. /ßäyadiya- 'Herrscher; päz. sah (PPGL), ^syäv
aaa, Ksoiiavöad (Agathias 261, 5, 264, 1).
Allgemein entlehnt (meist mit der speciellen Be-
deutung 'Perserkönig), wie auch säht (z. B. oss. d. sai
'Fünfkopekenstück', bei. säht 'Zweiannastück' (256);
dagegen in der Bedeutung *Landstrasse' in skr. säht,
Weber, Monatsber. BAW. 1879, 812).
778. sähensfih 'König der Könige'.
ap. yßäyad iyänäm ysäyadiya *der Könige König',
Vergl. Seite 128 Note 6.
^) * Sähen ^ vorgl. arm. LW. .^aJien.
-- 193 --
- 171 —
Saa^isaa (Amin. Marc XIX, 2, llj^); arm. LW.
sahartsali,
774. HayiHteii *öiuh ziemen, können'-), Prae«. myed (Im-
person.).
aw. \^xsuy-, /sat/ft^ 'im Stande sein, vermögen ;
phlv. my(i)stan^ sät/at; lat. queö (^'qiiejo).
775. Seh *Nacht\
K5§. mc,
ap.;firt/yii]«?Ä Mes Nachts* ; aw. /sap', /sapan- Nacht*:
phlv. sap, saw(ik\ vergl. Sapak, N. pr. (Hörn, Mit-
teilungen, Heft IV, 29 No. 15); ai. ksdp-.
kurd. sew ; afy. spa ; oss. ä/jaw (44) ; bei. sap (862) ;
wa/. LW. smJ, sij'n. sa6, sar. /at, minj. ;^srfw?a, /asa/rr/.
Der ;<-Stamm findet sich vielleicht noch in np.
sebänröz^) (AM. sehärözT , wie jüd.-pers. ""'iNO^iJ),
sebänffäh, sebdnböl, sebänver u. a. m. erhalten.
77G. sahän Hirte, siiwän, IN2iir (Is. 1, 24).
Kas. cepän, cüptm, cap6 (vergl. V^ullers cüpdn),
aw. ysti.päna-; phlv. spän *Hirte' (AV.), supän
(FP61.), arm. LW. spat (aw. *ßu,paUi')^).
kurd. siwan ; aty. spün 'Hirt*, spankai 'Schäferbube' ;
bei. sipänk, n. mwäuK, safänk 03(57) ; wa/. s/)JJw, süpiin.
Die dialektischen c«/?i7w (auch kurd. cuwän 'Hirt',
cöpän 'Fleischer) sind jung. Das i der kurd. und
beluc. Form ist ebenfalls jung, es ist erst nachträg-
lich zwischen die zusammengerückte Gruppe sp, sw
getreten, also *sup% ^suw" — ^sp'', ^sw'* — siw"^ sip"
(Geiger* s Etymologie *sa — Praeüx — und |/^pö*- ist
falsch).
777. Htäften 'eilen', Praes. sitäb-em^ sitab, DNDl^iN (Jer.
48, 16).
*J E. Drouin*s Lesung suhanum uut* Münzen (Kevuc niumiä-
matique, 1890, S. 361) ist ebenso verfehlt, wie seine Qemmenentzifferungeii
(vergl. ZDMG. 45, 429 folgg.).
') Vergl. oben No. 179 Anm. _
5) IV^u/^ijufQoy, H. 8. Jarret, Aln-i Akbari-Transl. Vol. II, 13
Anm. 2.
*) Ilübsohmann, ZDMG. 44, 5ß0.
```


## [2026-09-06T21:21:49.472Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pädisäh\\|pädsäh\\|padisah\\|pädtsäh\\|Ardesir\\|Ardasir\\|ardaslr\\|Artaxerxes\" HRN.txt | head -20"
}
```


### [2026-09-06T21:21:49.521Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:21:52.412Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dsäh\\|dtsäh\\|dsah\\|desir\\|dasTr\\|dasir\" HRN.txt | head -20; echo ---; grep -n \"pati.*sah\\|Herrscher'\" HRN.txt | head"
}
```


### [2026-09-06T21:21:52.476Z] TOOL RESULT

```
9378:wiidsähl Fol. 38 (Berliner Handschrift Ms. orient. Fol. 535).
---
2680:ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
```


## [2026-09-06T21:21:55.537Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2660,2700p' HRN.txt; echo \"=== which leaf ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:2679])\nprint('leaf', t[:idx].count('\\f')+1)\nEOF"
}
```


### [2026-09-06T21:21:57.676Z] TOOL RESULT

```
265. />flcZ 'Schützer, gewaltig ^).
27äd setzt ein ap. ^päta- (Suffix ta- wird bekannt-
lich auch gelegentlich zur Bildung von Nom. ag. ver-
wandt) Schützer voraus; ap. "^pätar- (aw. pätar-, ai.
jmtdr-) müsste im Np. als pädar erscheinen 2).
§i/n. päda 'Hirte*.
*) In den Wörterbüchern finde ich keinen Beleg; aber Sadi hat
in seinem Commentar zu Häfiz, Ghazel No. 11, Beit 2 einen Vers
Enveri's (ed. Brockhaus, S. 56). Er erklärt das Wort durch türk.
ulu 'gross*.
*) Bartholomae wiU nach brieflicher Mitteilung *pcUas 'schützend*
lieber als neuen Nominativ zu päJtam d. i. pät-am (Brugmann, Grund-
riss II, 367) auffassen.- 61 -
265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
pädosn,
phlv. pätdah(i)sn {paiti -f dah(i)sn), päz. pädaisn^
pädaän 'Vergeltung'.
Aus dem Pärsismus übernommenes Wort. Vergl.
np. dasen (No. 528).
266. pädiSäh *König'.
ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
(übersetzt im Kommentar aw. x^<^y(^^^<^' Vermögend,
erlaubt ; Herrscher) ^).
267. päde 'Heerde'^), padehan.
ap. aw. skr. päta- 'beschützt, bewahrt'.
268. pädyäb, pädyaw rituelle Waschung.
aw. paüyäpa- ; phlv. pätt/äp, pOtyapih,
Rituelles Pärsenwort.
269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
phlv. pätyavand 'kräftig'.
paiti + l/^««?-, aw. *paityavanU (Part. Praes.).
270. pär 'das vergangene Jahr', pärsal^ parm.
skr. vergl. panit 'im vergangenen Jahre' ; arm. heru
Vergangenes Jahr' (H. No. 167).
kurd. (LW.) par\ af/. parös-; oss. d. fdi% t/aron
'im vorigen Jahre' (277) ; bei. pari, n. pän (293) ; wa;^.
pardy sar. parvus (vergl. gr. nigvöi).
Ap. paruva- 'früher (aw. paurva-) ist schon im
Pehlevi aufgegeben worden; np. pärav alte Frau' ist
nicht belegt.
*) Zu phlv. pata^sa, np. padisäh als t. t. beim Ehesohluss vergl.
=== which leaf ===
leaf 83
```


## [2026-09-06T21:22:13.363Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD šāh/šahr/šāyist ===\"; grep -n \"^šāh\\|^šahr\\|^šāyist\\|šahr \\[\\|šāh \\[\\|šāyist \\[\\|xšahr\\|šagr\\|^šēr\" PHD.txt | head -20; echo \"=== PHD alt ===\"; grep -n \"šagr\\|šahr\\b\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T21:22:13.427Z] TOOL RESULT

```
=== PHD šāh/šahr/šāyist ===
582:šāh 79 Sifténag
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
1507:deceased anēšagruwān; v. blessed.
2569:late (deceased) anūšagruwān, hufra- ward.
2642:lion šagr.
4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
4563:šāh
4567:šāhesprahm šāyēd šāzdah
4849:šāhān šāh! marag bambign! marz
=== PHD alt ===
```


## [2026-09-06T21:22:21.149Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"šagr \\[\" PHD.txt | head -5; echo ---; grep -o \"šagr \\[[^]]*\\][^.]*\\.\" PHD.txt | head -5; echo \"=== padixsay ===\"; grep -o \"pādixšāy[^.]*\\.\\|pādixšā[^.]*\\.\" PHD.txt | head -5; echo \"=== artaxsahr/ardaxsir ===\"; grep -no \"Ardaxšīr[^.]*\\.\\|ardaxšīr[^.]*\\.\" PHD.txt | head -5"
}
```


### [2026-09-06T21:22:21.284Z] TOOL RESULT

```
---
=== padixsay ===
pādixšā(y)] without authority, powerless.
pādixšā(y) [dušp*thš*(d)) evil ruler.
pādixšā(y) [hwp?thš”(d)) good ruler.
pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized.
pādixšā(y).
=== artaxsahr/ardaxsir ===
912:ardaxšīr.
```


## [2026-09-06T21:22:24.953Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"[Šš]agr[^.]\\{0,120\\}\\.\" PHD.txt | head -8; echo \"=== pādixšāyīh line ===\"; grep -no \"pādixšā(y) \\[SL[^|]*|[^]]*\\][^.]*\\.\" PHD.txt|head -3; echo \"=== ardaxsir context ===\"; sed -n '912p' PHD.txt | cut -c1-600"
}
```


### [2026-09-06T21:22:26.822Z] TOOL RESULT

```
šagruwān; v.
šagruwān, hufra- ward.
šagr.
=== pādixšāyīh line ===
538:pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized.
=== ardaxsir context ===
backgammon nēwardaxšīr.
```


## [2026-09-06T21:22:30.586Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"[Ss]agr \\[[^]]*\\][^.]*\\.\\|[Šš]agr \\[[^]]*\\][^.]*\\.\" PHD.txt | head; echo ---; grep -n \"Sagr\" PHD.txt | head -5"
}
```


### [2026-09-06T21:22:30.656Z] TOOL RESULT

```
562:sagr [sg] | N sēr] sated, satiate.
---
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
2600:Leo Sagr.
```


## [2026-09-06T21:22:40.410Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"x[sš]a.ra.vairya\\|xsa9ra\\|xsa8ra\\|xsaOra\" BRT.txt | head -20; echo \"=== search generally ===\"; grep -c \"\" BRT.txt"
}
```


### [2026-09-06T21:22:40.465Z] TOOL RESULT

```
29441:•  j.  hamö.xsaOra-  Adj.  'allherrschendj AllheiTSchei':  säsia  daiMiul 'rö'^t.i3.\%, ^%  '5-  S^j  ^4-  13;  —  s3%rasiil  'rahe  Yt iO.  109.
=== search generally ===
30725
```


## [2026-09-06T21:22:42.499Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vairya\" BRT.txt | head -20"
}
```


### [2026-09-06T21:22:42.552Z] TOOL RESULT

```
5117:sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern .  .  y3  asti  'vaiti  masö  yd^a  vJspa  ima äpS  Y.  65. 3 ;  — yash  . .  "vant^m  (als  ASn.) mass  vikilnayät  ya'ia  hi  tanus  atphat  V. 7.51.  a)  mit  ya'i:a  yat  'wie  wenn,  als ob':  °vaia  aejanha  yd^a  yat  panca  narS "mit  solcher  Kraft,  als  ob  es  fiinf  Männer wären"  V.  75. 10  PiiZ.  2)  'dass':  asti  sl
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
5922:•  j.  *"a-srävayamna-''  Adj.  'was  nicht  auf- gesagt, rezitirt  wird':  'ii3t  paiti  ahuiia^ vairyat  "ohne  dass  der  AhV.  rezitirt  wird" N.  tiS'
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6377:•  j.  aSa'vam- fem.  Adj,  Fem.  zu  fl/äi^M-  eines  Gläubigen'':  Ha  (als  GS.)  nama (sd,):  A?  pta  .  .  asaonaslä  "vairyasiU  sluis  asaond  Vt.  75, 1 20.
6379:ai.  vgL  ftävari-  fem.  Adj-,  S  ?Q7.  2.  —    Pü.:       stammt  wolil  aus  dem  Namen  asim.yelihe.ra3li •liräiiA  tjmai;  vgl.  vairya:  (sd). —  >>  VgL  über  ihn  Bd.  ^p.  5,  Dd. 90.  3.
6436:•  j,  aäta  indekl.''  Zw.  'acht':  yetihe  -ta (als  Nora.)  ratayS  (sd.) . .  anfmire  Yt  lo. 4S;  V.  76".  10*;  —  -ia  aurvanSS  (sd.)  Yt ig,y,  —  °ta  vasanS  (sd.)  Yt  ig.  z;  —  'ta (als  Akk.)  akuna  vairya  frasrävaydil  V. 11. 8;  —  *'ta  (als  Gen.)  gavqm  azinqm ar>jö  F.  _yh;  —  °ta  sota  upäzananqm "800  .  ."  V,4. 14;  14;  —  'ta  (als  Instr.) saläis  halaci^anani  "mit  800  .  ."  V.  4. S.  [Yt().  3o;'lies  asta.aurv'\  —  V. y.  44:  lies  aHa.b°^
6790:103.         A)  sonst  mit  vairya-  Adj.  (dem  vatum  . .  ah'  ^a.näs}m  vakista.näs^m  (sd.)
6796:g,  6,  2 1 ;  —  'ns  vairy3  fraoxts  H.  7. 4 ;  —  '  J-  'ahuimant-  Adj.  'der  emen  Aha  be- tam  paoiryd  zara>ustra 'npfn  vatrlm  fra-'^'^^'  stets  neben  ra/»;«^;,/.  (sd):  *"».a/'> irävayJvTb>r^>wa>,tfm{%^),lxtairJm{sA.)  ratumai  vaktnmi  vaocata  wzs  tin%n  Aha apar?tn  xraozdyehya  (sd.)  frasräiti  V.o.  "°°  ^"^"^  *""  '  "^^  "^°°'^t  das  beste" i4;V.in.2,YtiQ.8i;—panra  'na  vairya  P-'^'?)i  —  'mais  raiumatö  alaonö  asahe JrasravaySisW.n.z;    77.6,   7Ä43,  70.  zi;   '•■^^Sa-J  Vr.7.5J>;  —   'm^^m  rafummism
6797:-  .  .  'nasca  vairyan /rasravayeiti\i.50;.f''^-''""''  ''"'^'  r*'«"'  "y^"  ■  -  ^'^  ='  "^^ —zaola{sA.)..zaolarsgatava*'n^mvairTm  °'"'':1  ,  '"^-^  '■''^'««'■''''  >^  '"5«'-^" Aa^rJ^.Tyj«/  N.&;  —  ^vaiti  naram  ..  """'f^^  den,  der  emen  ^/5s  und  Äo/aj/ ■laota  ifA.)  ratufni 'tum  vairim  frasrao-  besitzt,...  Der  nämlich  besiut  emen -4-4fi ^ehe  N.  20;  -   'n?mca  vairtm  srSvayeni  '^^  ^"^""Ik  «^^  '  ■"  ^J"  "-^V,       ,-
6801:yät K.4.%;  ■''N.  (iS;  —  'nahe  vairyehe  asaya frasrütahe  Y.27.7,  Vr.72.2;  7,4,  2.6,  Y. 7p.  2 1 ;  —  'nahe  vairyehe  arsuxoahe  växs y.^.i;  Vr.  70.2;  —  'nanqm  vairyanqm N.  702;  —  'n^m  vairlm  yazamaide  Y.  13. 8;  7.26,  61,1,  Vr.74.3;  —  'nJ  vairyS vacqm  j'irUrajqst^mäYl.  il.y,  —  sraohm .  .  yeAlie  'ns  vairyg  snatiis  vuata  Y.  57. 22;  — jainti   mqm   'na    vairy.
7365:ayasata    °ta    xiaira  vairya  V.  20,3(?)"
7883:1)  'hin  zu  gehen  zu -',  mit  Dat. ■>  (statt  ,_(,aj«,j,-  Vr.;5.2;  V.jff.i^s'  (wo  "0,7),  2;. Akk.):  husiti  ..  äanyuMti  (sd.)  ite  vJse  (,^  Yti-agS;  —  aim  mSt  'äS  iw/y  (sd.) afrXnümi  yahmat  haca  . .  ".  .  in  (dessen) ' yj  „5  a?i-ö  . .  Y.  2(J.8;  —  iv//tt  -ö«  . .  hvar- Haus  zu  gehen,  von  dem  .  .'■  ^.6S.^lt)m  lyaoi:ni>m  S-s^i^i; —ya>a  yat '<.a 14.  a)'einzugehenauf-':iJOTff^^ä^W/|ana/rj'rf  daiühus  hakat  m^a  us./raraysil moi  data  danga/tya  *yaoi  ySm  vä  *nagas  (sd.)  YL  75.68;  V. 5.56,  y.55;  —  ime  nö däfMt  its  vairya  stdt/isd.)  "..ihn  sollt  ihr|.  .  aspa  para  *miira  *'c,a'>  iiaymU  (sd.) mir  gewähren,  auf  den  einzugehen  keiner  yt.io.  42;  60;  —ha  hl  asti  ä>a  ..aipi.- euch  zwingen  kann,  (den  Wunsch) .."  Y.  panmnäi  'oa  aSaone  V.Ä107;  —  ktj'M 43-^'h-  'ffff(sd.)''oa  alsum  agate  Y.ig.^i;  —  'oa
8408:•  j.  upäpa-  Adj.  (fem.  'pä-)  i)  'im  Wasser befindlich,  lebend,  hausend':  dsman  . . yäca  °^ii(NPn.)  ysca  upasma  Ht.8.^%-,  — vjspamca  gqm  'pqmca  upasmqmca  "all Getier,  das  im  Wasser  und  auf  dem  Land lebt"  Y.  77.9";  —  ratavS  °panqm..  upas- manqm  Vr. /.i;  Yt/j.74;  —  ratavö  'pa .  .  upasma  Vr.  2.  i ;  —  karB  masys  'ps bütte  ..   vairyanqm   V.iff.^s;  Yt/^.  29;
8857:(sA)  Jasti  N,/oj; — ^kaAyl^^"^  dahmanqm sao^räoa  (si)  *ratu/rU  N,  40 ;  —  draos (sd.)  z-iJ  paiti  söinma  unam  vä  katcit  vS paiti  sidaranqm  N.  IQO;  —  kahmäicit yanhqm  jasS  Yt  13.  41;  41,  V.  7.  7: —  yahmäl  kahmäiHt  na^nanqtn  va ä'ird  baoiöTm  baraiti  ahmst  kahmätHi naimanam  .  .  paiH.jasalH  ütars welcher  (Seite)  her  nach  irgend Seite  der  Wind  des  Feuers  Geroch  ver- breitet, von  der  her  nach  irgend  einer Seite  wendet  sich  ^.."  V.iV.So; — pasBm .  .  7-ohu^aorvm  vä  käcit  (IS.)  vä  gaona- nqm  hamS4;aontm  (sd.)  Yt.  8.  58;  *Aog. »7;  —  di^e  saite  kahyJat . ,  xrafstranqm V.  16.12;  —  kasatinm  kaAhhcit  va^wa- nqm  A.  j,  11;  — 'in  Verbindung  mit  anya- A(tj.  '.ilius  (]uispiam':  anys  kasat  ar?hsiis astiatö  N.  6j.  a)  Piur.  im  Sinn  unsres zurück  weisenden  'welche,  solche', Zeichnung  einer  uobestimniten  Zahl:  äjal aaaelqm  . .  hj/il  (APa)  upaÄsSi  (sd.)  N. io().  a)sva.|jedermann,  jeder,  quisque' fravalayS  . .  ijp^m  aZi?mnil  (sd.)  havä käHt  (NSf.)  näfäi  ". .  suae  quaeque  origini" Yt.  13. 66;  —  äai  anyähu  ratufrisu  latai>rS *kai3h^scil^^  bar?smqn  frastaraitys  (sd.) N.  ;o2;  —  sdäi  (sdl)  *Aahyä^t^*^  paiti V.33. 1 1.  a)  mit  Gen.  part:  hazatinm vairyaiiqm  . .  kßsalia  alsqm  vatryanqm  . . "tausend  Seebuchten  .  .  und  jede  dieser Seebuchten  . ."  Y.  Ö5.4;  4;  —  kasHt avAius' (sd.)  aslvate  F.  36';  P.  y,  V.  7.50, iO- 19,  P.43  (kakynat);  —  Hat  vö  kasat masyjiiqm  .  .  ¥1/5.53;  Vr.^.5;  — yäva- ranJ  kascit  sao^antqm  Y.12.J;  —  iäat tanuHam  V.  16.10;  —  ka^häscit  tanunqm H.  /.  5 ;  —  kahmai^t  häiqm  "Jedem  der Seienden"  Y.J5.8;  /fl.ii',  F.^b'«;  — kakyäcii  hstqm  V, /2, 4;  —  ijmcit  paiti cairusanqm  (Stverz.)  V.tf. 31  usw.;  — a^'ahe  pasvd  {sA.)  ..  aliiqm  *kakmaicit*''^ td'ia  */rayarihqm  (sd.)  N.  65.  a)  mit
9204:mit /rJ  'durch  Einfurchen  herstellen':  (sSPrM.)  Vt.ij.  107;  —  aü?..  fr  acaraiti karsasiit  (sd.)  frakirayjis  tiyra  xi'a'ira  \*antan.ar/6}m  nm3nahe  Yt.  iS.  4;  3;  — *vairya  V.^,  10;  11',  F. 5;  —  nava  karsa.vasS.xsa^rS  (näml.  jran//')  *fracaraite  aoi frakJrayat  "neun  Furchstreifen  zog  er"  ^y^m  ..  gas%qm  ¥.57.34;  —ya'i:a..anJzarvtä \.22.ao; — yS  ZJinS  tisrS  kari^a/rak3ra-\.  .  yahm  (näml.  fravasayS)  fra^ara'imie yHH  N.;o/;  YL4.63.  (2PPM-)  ¥1/^.34.         2)  mit  Akk.  'hinzu
9354:•  j.  'kar§a-'>  m.,  n.  i)  'Furche,  Furch- strich, -streifen  (auf  dem  Erdboden)':  yj t»mS  tisrö  *'/ä  (APn.)  frakärayeiti  ava  1 ika  bartnti  (sd.)  *yavahe  ",  ,  drei  Fur- chen . ."  N,  }0i;  —  äva.dasa  'sa  /rakä- rayÖM  "zwölf  Furchstriche  sollst  du  ziehen" V,  5.  1 1  *';  —  'säsat  (APm,)'*  frakäraySis tiyra  Xioira  ^vairya  "Furchstriche  sollst du  ziehen  mit  einem  spitzen  Metallstuck" \.g.  10";  zit  *F.53)j  —  nava  v'^  (APn.) ß-äiJrtiyiat  V. 22.20.  2)  'Bezirk,  Gau'<>: **a>  F.  5;  —  y3  hudaind . .  vlspa  -sS  (als AP.)  rJoayäti  Yt  4.  9  (?).  |
9959:—  anyii  akmäi  yd  Janaiti'''  frala  kusaiti (näml.  hlm)  V.5.34;  Yt.<^8(?); — jainti mqm  ahuna  vairya  avavata  snaiiiia yäha  ..    Yt. /?.  20;  j.  lo-is'»    {jaiiitt),
10722:—  voAa  kv5  '^ra  as3m  vacaitha  ^ao'i-ana Aapil{sd.)  Y.31.  22;  —  vaAü  "^rvm  vairim bäg}m  aiblJ)airist>m  *vJdll>mnäi  (sd.)  .  , asä  antari.iarain  Y.5J.  i;  —  vohü  °%r3m ISi  mazdä  ahurä  apalmä  vispäi  yavi  Y. 41.2;  —  maiää  .  .  vairya  stöisisd.)  yä 'iwahmT  'Hröi  väcT  Y.  43- 13;  3^.  6,  34. 10,  49-5;  —  ahurä  ,  .  %wahmT  ä  ''hrsi
```


## [2026-09-06T21:22:51.883Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Herrschaft'\" BRT.txt | head -20"
}
```


### [2026-09-06T21:22:51.933Z] TOOL RESULT

```
10724:anas/i  (sd.)  Y.  20.  3;  —  voAu  'inm  ya;a- maideYr.  20.  i .  3)  'Herrschaft'  in  konkre- tem Sinn  (nur  Komp.).  A)  als  Gottheit (Am3iaSp3nta)''>;  i)  im  gAw.:  yl  s^visIS (sd.)  ahurä  mazdäscä  ärmaitiUä  ahmcä., manasLil  voAu  ''i:rimca  Y.  33.11;  —  al va  yazäi  . .  mazda  ahurä  Aadä  (sd.)  asä vahistäca  mananha  ""hräca  Y.  50. 4;  — asibyö   mazda    ahurB   särimnS  (sd.)    vohü
10754:um  die  Herrschaft':  haomB  . .  kmsSnJm apa-xid^rim  (sd.)  nilähaya^  yd  raosta  (sd.) 'mya  (IS.)  Y.p.  24.
10812:KompA.  —  Zum  V.  xiä{y)-.  —  ai.  kräya-  m. 1)  'Herrscher'  RV.  8.  15.  9.  a)  'Herrschaft' 7.  46-  ^■  —  Pu.  (lu  F.):  ™4,  (lu  V.);  paUxÜh, Sä,:  pärthivah.  —  i)  So  K.,
12899:•  j,  darUT-ö.x^a^Ta-  n.  'lange  Herrschaft': 'ärjM  xsa'israke  A  /.  8.
```


## [2026-09-06T21:22:54.198Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10700,10730p' BRT.txt; echo \"#### 10800-10830\"; sed -n '10800,10830p' BRT.txt"
}
```


### [2026-09-06T21:22:54.273Z] TOOL RESULT

```
Az-j;  — yim  yimim  't>m  Yt/p.  31;  — yimäi  °t5i  V./^.  39;  — yimat  haia  "iäi YL/^.35-
KonripA.,  E. ').  —    \'gl.  axsattta-,    - ■Sonne'.  —  Pü.!  rSht.  (lu  Y.  26J:  ; 2  a):  j-am  JS.  —  OS  20?-  2  »E-  —  ")  S.  noch unter  kvanxia^la-,
•  '].  xsaetö.puOrya-  n.  'Besiu  herrlicher
xsaSra-  1  i
542
Söhne':  haomS  daaaiti ..''^rim  Uta  asava.- frasaintTm  X.g.tt.
Ableit  aus  *j:jii//ö^iro- Adj.  —  Pü.:  hurdiiin
fius,  Sü.:  diftimän  putra^.
•  j.  xsao9ah-  n.  'Fluss,  Strömung,  Wasser- Schwall';  airy!>.layamm  .  ,  yahmya  äpu navaya  .  .  °taipha  %waxhnle  Yt  10. 14.
:.  ifidas-  n.  —  Vgl.  lu  xsusla-. j.  xloodrinum  V.  16.  7:  lies  xsävd'. j.  xiaudrim  N.  6!# :  lies  xläud:
•  j.  xsaob-  V.,  nur  Praes.  14  (Inkoh.) vu/sa-^^  'in  Aufregung  geraten', /u/  aspanqm  sri/a  (sd.)  xsufsqn  Yt./o.
j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
dby  Google
543  x5a*ra-  I  3
'hnm^a  YL  13.  88.  a)  mit  Gen.  'über  -' (s.  3  a):  ya>^a  aztm  up^mim  °'^r>in  baväni vispanqm    äaRyunqm    Yt5.  22.  3)   im
gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
kavä  vistäsps  magaAyä(^.)  'hrä  nasal., astlm  Y.5J.  16;  —  tu  v7  masdil  .  .'dSisä möi  isteis  (%A.)  -'hnm  Y.j/.a;  benutzt Vyt.  46.  b)  mit  InE:  ial  vi  xsair^m kii  Jltis  (sd.)  syadäaiiifi  mazda  Y.  34. j.  2)  'Henschgebiet"';  i)  II  im  Ap.-, mäm  ^ur^mazdi  päluv  utamaiy  °~ii''am via  tyt^  maiui  tartam  X.J.  4;  2.3,  4. 3.  2)   im  jAw.:  ya>a  .  .  masa  °>ra
riivänäni  as.faäna  slüi.bax.Hira..as.baourva ni'jatu.pitu  Yt. 5.130;  J7.7;  —  ktthmrti.. uyr?m  '^rtm  x^at/iisajct^m  pouru.spä'i»m,. paitiMdiiäm  Yt.  /o.  109;  111;  —  '%räi hank?r)mö  {%A.)  kaosrava  Yt.  5.  49;  —  iri- ^ini>m  '"inm  zajaiii\t'i.i$o(?)'K  3)im gAw.-.ys  ''^rJ  *gr3hmS  Aisaiat(sd.)  acisla- Ayä  dsmäm  inana*»hs\.3-i.\y  a)  ins- bes.  vom  aiiariscben  Reich,  dem  Aiifent-
xäadra-  A  i
544
halt  der  Götter  und  Seligen;  aät'  ii.  oder mit  näherei  Bestimmung  (durch  Adj.  oder Gen.);  a)  im  gAw.:  yn  vi  abi/ra{sd.)  lä '>raiyäY.33.i2; — gaf'iti  vTspä  a  "^röi *yj  vohü  %raostäisd.)  mananhä  Y.34.2;
—  ya^ra  vanhSul  mananhs  Tstä  (sd.) ''hr3mY.46.16;  —  voAs  °^nm  mananhJ mazda  dadat  ahurB  "durch  VM.  wird (ihm)  MAh.  das  Reich  verleihen"  Y.  j/. aij  —  at  mazda  laibyö  °^rptn  voAs manat»h3  *vöivTdaill{sä.)  aeibyS  saste(ad.) y5i  .  .  Y.30.8;  —  a/m  (sd.)  asäi  fo/iu •^nm  manaaha  Y. 46.10;  —  taibyS  '^rvm voAB  ^nas  (sd.)  manaisAä  Y.44-  6;  — ka'^ä..pailis>  sahyit '^rakyä  snsvä  'hrä (AP.)  %wävqs  aslstls'  (sd.)  mazda  Y.  44- 9; — yasibyö  '"hrsmla  * aysSjtvamium  (sd.) i'ar^daitT  ärmaiüs  Y,  2Ä3;  —  *^!ng.- datvsifi {sd.)  °%r!!i  hyat  armailisY. 43.16;
—  voAa  kv5  '^ra  as3m  vacaitha  ^ao'i-ana Aapil{sd.)  Y.31.  22;  —  vaAü  "^rvm  vairim bäg}m  aiblJ)airist>m  *vJdll>mnäi  (sd.)  .  , asä  antari.iarain  Y.5J.  i;  —  vohü  °%r3m ISi  mazdä  ahurä  apalmä  vispäi  yavi  Y. 41.2;  —  maiää  .  .  vairya  stöisisd.)  yä 'iwahmT  'Hröi  väcT  Y.  43- 13;  3^.  6,  34. 10,  49-5;  —  ahurä  ,  .  %wahmT  ä  ''hrsi
yavsi  vjspai  fraßtarihs  aiihamä  Y.4^.8; — ka  tsi  vauAsus  mazda  °%raAya  Isti^{sd.) . .  maibyS  aAura  Y.  48.  8;  —  ku^rä  ^wS '•'irä  (NP.)  mazdä  "wo  sind  deine  Reiche, o  Af.?"  Y.  5/.  4;  —  mazdäi  avaj  °^/v« Ayat  Aöi  voAa  vaxsal  (sd.)  manatjAa  Y. 31. 6j  —  apsnd  (sd.)  dar^S.jyäitlm  *ä °%r>m  vaaASui manatfAs  "..  zu  dem  Reich des  VM."  Y._jj.  5;  57. 18;  —  va»hsus '^rä  (AP.)  manat^AB  . .  ärmailis  vaxst Y.34. 11;  —  asfmcä  .  .  ''hnmiS  Aaurva- tsts  ".  .und  das  Reich  der  Wohlfahrt"  Y.34~ i; — ySzSm  zr.nslyänAö  (sd.)  TsS  "ärjMÄl savatiAqm  "..  Reich  des  (ewigen)  Nutzens" Y.  2Ä  9';  —  Ayai  .  .  cöist  (sd.)  'hröi  Aöi Aaurvütä  anurplätä  .  .  dqn  .  .  Y.  45- 10.  ß)    im  jAw.:   ya^ia    asai    '^rym
anas/i  (sd.)  Y.  20.  3;  —  voAu  'inm  ya;a- maideYr.  20.  i .  3)  'Herrschaft'  in  konkre- tem Sinn  (nur  Komp.).  A)  als  Gottheit (Am3iaSp3nta)''>;  i)  im  gAw.:  yl  s^visIS (sd.)  ahurä  mazdäscä  ärmaitiUä  ahmcä., manasLil  voAu  ''i:rimca  Y.  33.11;  —  al va  yazäi  . .  mazda  ahurä  Aadä  (sd.)  asä vahistäca  mananha  ""hräca  Y.  50. 4;  — asibyö   mazda    ahurB   särimnS  (sd.)    vohü
dby  Google
545
xSaSrH-  A  2
x§a{h-ö.kämyä-
546
ntanauhl  '%r3J  hcUü  paitt.mraot  asä  kuL- haxa  Y.32.  2;  —  mazdä  , .  vokü  uxfya (sd.)  manavAä  °hr3  aiälä  ustä  tanüm Y._jj.  10;  —  yahmi  spfntJ  %wä  mainyU urvafse  jass  mafsds  "ärä  ahmt{s,A.)  voha mananha  Y.43.6;  —  aAmäicä  «ärJ  (als Sah].)  ^^ /asaj  (sA.)  mananha  voha  asaüä Y.3Q.  7;  —  ahmsi  dqn  (sd.)  .  .  mazdä •^rJ  armaitf  ahurS  Y.  47.  i;  —  kj  binx- 'iqm  täil  ''hrJ  mal  ärmaitim  ^..44.1;  — kada  masda  ala  mal  ärmai/i/ /imaj  (sd.) •^ra  Y.48.11;  — yqm  Asi  °'^ra  voAuäi cdiit  (sA)  tnananhi  Y.^o.y,  —  mazdi dadät . .  haurvat3  aminlätasca  . .  asahyica ..  •UraAyä  sarS  (sd.)  Y.^jj.ai.  a)  im YHapt,  mit  va^hav-K^y.as>m..vahist>m ..vohuia  maiid ..  vokucä  '"hrsm  \.3~.i,i.\ —  asäatcä  hacä  varahsuseä  mananhs  vatf- ksusca  'hrai  Y. J5. 10.  a)  im  jAw.,  mit va i rya- Adj. :  '^rtm  vairTm  amihm  sptn- hm  yazamaide  S. 2.  4 ;  Vr.  20.  i;  —  ahurS mazdä  . .  vohu  manö . .  ahm  vahist»m  .  . ''i:r>m  VairTm  .  ,  spmta  ärmaitis  .  .  Y. 57.  24;  1.1  f.,  /tf.  3,  Yt/.  25,  4.  i;  —  ahu- rake  maxdä  .  .  vanh^us  mananhB aiahe ..'"hrahe  vairyeke..  Y.70.2;  —  aku- rai  masdäi  . .  aläi  . .  °^rai  vairyät  armatSe V,  iff.  iii  G.J.  s;  —  vaAu  manauha  haH- mnS  aläca  .  .  '^r3ca  ya  vairya  FrW.  /, I ;  —  viscihnm  dim  ayasata  Syapta  (sd.) ■ira  vairyaY.2Q-^(J\  k)  xlaiirahe  vair- yeht  a)  (nämlich  mS)  heisst  der  6.  Monat im  Jahr:  pancaca  haptaitttn  *pailisJiahyehe (sd.)  '"hrahe  vairyehe  anayranqm  A.  3. 9.  ß>    (nämlich    ayani)    heisst    der  4.
#### 10800-10830
S45;  %.  die  freilich  verderbten  Erläuterungen
tmil  iapiii  rU)  lu  N.  4.
•  j.  x§apar-  n.  'Nacht'  i)  im  Gegensatz zum  Tag:  yai  vä  ya'ia  *uzayamn  yai ya'i^a  'pamm^^  ti.47(?).  2)  als  Zeit von  Sonnenuntergang  zu  Sonnenuntergang 'Tag  und  Nacht,  Tag'  (nur  Komp.).
KompE.  — Vgl,  Ji'fl/i-.  —  Pü.:  fehlt.  —  0  Them.
•  j,,  g.  xSapä-  f.'>  'Nacht',  im  Gegensatz zum  'l'ag:  yä  usi  arjm.pi^wn  (sd.)  °pa'a Y.  44.  5 ;  —  *cim  ..  va  ..  ayar>  alva  vä 'pa  Aog.57;  *F.27b'>;  — ya'ira  mit  -pa nöit  t3mä  Yt  10.50.
KompA.  —  Vgl.  xsap-.—  Pü.:  sap.—  ')  Nur NS.  'fia,  vgl.  ä/a  V.  7.  16  und  das  Aiiid. i/apäiAii.  xsapa  als  NS.  aas  xiafan-  zu  neh- men, halte  ich  nicht  für  richtig,  —  ')  Hds. xiafa;  1.  freilich  S  S.
•  j.  xäapä-yaoiia-  Adj.  'in  der  Nacht  sich heimisch  iiihlend,  mit  der  Nacht  vertraut': (der  Hund  ist)  'yaens  yaüa  täyus  V.  /_;. AT,  47-
j.  xiafa  F.  «7  b:  lies  xsapa;  %.  noter  xtapä:
•  j.   xsafnya-   n.    'Nacht-,    Abendmahl':
ax^afii  (sd.)  'nim  is>mns  Yt  i4- 10.
Abteil,  aus  xsapan..  —  Vgl.  xläfnya:  —  Npö. : undeutlich, j.,  g.  xtay'  Verbalf.:    %.  unter   xiUji)-  und iay.
•  j-i  g-  (1  P-)  tSaya-  m.  'Herrscher,  Fürst, König':  hS  anhaiti  iasu/tfinff (sd.)  'yS kascit  maiyanqm  Ytrj.i8;*F.j'';  —  dasts mazdä  °yäcä  "gib  es,  o  M.  und  König, (dass  . .)"  Y.  2.8. 7.
KompA.  —  Zum  V.  xiä{y)-.  —  ai.  kräya-  m. 1)  'Herrscher'  RV.  8.  15.  9.  a)  'Herrschaft' 7.  46-  ^■  —  Pu.  (lu  F.):  ™4,  (lu  V.);  paUxÜh, Sä,:  pärthivah.  —  i)  So  K.,
•  j.  xSayat-vak-  Adj.  'der  zu  reden  ver- mag, des  Wortes  mächtig  ist':  'växsF.je.
Pü. ;  pälixsäh  i  g^uiim/iS.
•  j,,  g.  xSayant-  Adj.,  PPA,:  s.  xsä(y)-. KompEL  [s.  auch  axsyani-).
•  j.,  g.  xäayanuia,  *mana-  Adj.  (fem. =wJ.),  PPM.:  s.  xlä[y)-.
KompA.,  E.  (s.  auch  axsyamna-). j.  xJayasra  Y.  //.  17:  e.  xiT:
•  p.  xäayäräan-'*  m.  EN.  eines  persischen Königs,  Xerxes,  Sohns  Darius  L;  adam 'iä'^  x^äyaiiyt^  *vazark^  ..  dilrayi^va- Aaus  xsJya'iiyahyä pu^^f^  *haxämani^iy<^ X.7.2,  5;  8;  —  %ätly  -ya  x/äyahiy<^  X. i.Z,  4,  2. 3,5.3,  .^.3,  7.3;  —  trura*maedä .  ,  hyJ'  'ism  (AS.)"'  x^yakiyam  akunaui X.  I.  I,  6.  1;  —  -yircahyd'^  dürayJ'va- ''usakyd  x^,lya~^iyaAyJpuk''^^Am.i;  — artax/a'i''aky3  'yärcakyä*'  xläya'hiyahyä />uh''a''ä  Am.  j; —  arioxlayä  'iä^'>  xi'a- ya'hiyt^^'^  'pu^a"  's'a  därayc^va^ui'i^  xla- yaiiyJ^^  piii^"^  Ao.  1. 2.  [S.  noch  zu xarlädafyn^
Komp.:  xsayri;\-arsan;  eig,  'der  atsan- ('Hengst,  Held')  unter  den  Herrschern';  vgl. ai.  räjariatha-  m.  Anders  FoV  KZ.  J7.  544, wo  weitere  Litt.  —  >)  Zum  Stammansatz  nnd znei.  s.  S  3lt.  I  b.  2/j.  2,  —  »)  Verunglückte CS.-Bildune.  i  fehlerhaft  fSr  h  der  ZDMG. $4.  [27  gezogene  Schluss  scheint  mir  höchst fraglich.  —  i)  Sollte  GS.  sein.
•  g.  xsayö  Inf.  'um  zu  verderben':  hyat va  aka  manaahä  ySrtg  dalvSng  akascä mainyus'  aiä  syao^aram  vahi»hS  yä  fia- cinas  dn^iant-'m  x^  "welches  (Tun)  er'' und  der  böse  Geist  sammt  bösem  Denken
dby  Google
55»
x5ä(y)-
xää(y)-  mit  frä
55a
und  bfisem  Reden  euch,  die  Dalva,  was er  den  ZVi^fgenossen "  gelehrt  hat,   um (den  Menschen)  zu  verderben"  Y._j2.s. Za  ü.  V.  i^naA' 'er  Tcrnichtet',  gr.^SiV»;  vgl. *S^;  Bthl.  ZDMC.  50.  711,  —  Pü,!    tt/rär SSel  i  ciSn  Ah  hai  H  i  drvand pätixiähih  "der sie   lehrt,   die  Herrschaft   stsmmc  von   dem I>r".  —   >)  Der  Irrlehrer,   Ton  dem  auch  Y. 32.  6   die  Rede  ist;    s.  noch  No.  2.     Dafür, dass  das  erste  Sabjekt  nicht  ausdrQcklich  be- zeichnet ist,  vgl.  Sp.  5<36  0.  und  die  RV.-Slellen g]-häm  indraica  gacehatam,  a  yäd  ruhava  vänt- nasea  navam  (n.  a. ;  *.  Hask£i,L  JAOS.  ii.  66), die  insofern  der  obigen  ähneln.  —  ')  E»  ist ein  bestimmter,  der  neuen  Lehre  feindlicher Fürst  gemeint;  vgl.  drigvant-  I  a  a  0. j.  xsavaiditn  Vd.  p:  s.  xit/id-  mit  Na.  4. j.  xlm/as:  lies  xivaS.
•  ]•>  g-i  P-  xSä(y)-  V,  'vermögen'.  Praes. 3  jc/a-"  [,  25  ar/ayÄV],  2^  x^aya-,  'xsya-'''. i)  'Macht  haben,  Gewalt  haben,  herr- schen über  — ,  schalten,  verfügen  über  — , besitzen';  mit  a)  Gen.:  iüm  äxs'ieii'  ana- xitsiiia   .  .  xsayeke  dahyunqm  Yt.  10.  29;
—  vasasca  tu  -.  .  ustaca  xlada  (iSOM.) havanqm  dämanqmY.S.$;FiW.4.2  {x/a- yeni);  —  yat  xSayata  .  .  dalvatiqm  .  .  Yt. ig.26;  —  Auxsa^rä  xlStUqm  mä  nS*dus^ xfa%rä  xsSntä  "gute  Herrscher  sollen, nicht  schlechte  über  uns  herrschen"  Y, 4*-S;  —  huxsahras{%A)la  nS  .  .  xsaits (3SOM.)  Y.^j.2;  —  kadä  vasiä  yesX  lakyä xsaya'ha  mazda  a/ä  yehyä  mä  äi^is{sA.) dval^ä  "wann  werde  ich  erkennen,  ob  ihr über  jedweden  Macht  habt,  o  M.,  A.,  von dem.."Y.4Ä9;  —  x^ayqs  mazdä  ahura yehyä^  mä  aihlsc!^  dvaS%ä  "der  du,  oMAh. die  Macht  hast  über  jedweden,  von  dem mir  Verderben  droht"  Y.J2.16; daintl  nSit  jySßui  (sd.)  xsayamn7ng vass  Y._j2.is;  —xiayqs  a«W(GD.;  Sp, 242  m.)  Y.jj.s;  —  masS  xsayete  i^arinatihi "sie  verfügt  über  (so)  grosse  Hoheit"  Yt 5.96;  —  yadä  asSÜ  maHyi  vasS  xsayä "wann  ich  erst  (selbst)  nach  Gefallen  über m^in  Verdienst  schalten  werde"  Y.  50. 9.  ß)  Lok.:  nascis  xsayät..at3r5  mainyui :^aisu  dämühu  FrW.  4. 2.  3)  'Macht, Berechtigung  haben  zu  — ,  (es)  können, dürfen',  mit  Inf.:  xsayette  hl  .  .  ^risum aitahe  a^i   (sd.)    apauharstSe   V.  5.  26;
—  ^ka   *xsayeleO   *ana  .  .   haxtHt  (sd.) N.f);  —  y^  ■  •  irizux'jai  vacai>hqm  xs: yamnS  hisvS  vasS  "der  nach  Gefallen  die Worte  einer  Zunge  zu  bewahrheiten  ver-
mag" Y._j/.  19;  —  vasaha  ahi  xsayamna (NSf.)  lanuye  ifarmanke  ^daitim  (sd.) YL/7.15.         I,  2  a)  'mit  Gen.  und  Infi
```


## [2026-09-06T21:23:11.058Z] TOOL CALL #32: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-06T21:23:11.100Z] TOOL RESULT

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
```


## [2026-09-06T21:23:21.015Z] TOOL CALL #33: Bash

```json
{
 "command": "grep -n \"\\[pdf page\" data/verification/sources/refs/BQT_v2_pages.txt | head -3; echo ---; python3 -c \"\nimport re\nt=open('data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(t))\nprint(t[:1500])\n\""
}
```


### [2026-09-06T21:23:23.761Z] TOOL RESULT

```
---
2900526
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬




                   ‫چاپ افست رشدبه‬
                   ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬
‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬

‫داربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد وسی ودو ) نگارنده از‬
                                                                ‫ی‬
‫خوانند گان فاضل درخواست کرد که اطلاعات خودرا درموضوعهای مختلف کتاب تراسا‬
‫دربارة لغات مربوط بلهجه‌های محلی وشاهدهای شان ونادر مرفوم‌دارند‪ .‬چندتن دعوت‌وبرا‬
‫اجات کردند وشغاهاً وکا اطلاعاتی دردسترس مصحح گذاشتند‪ .‬وماآنچهرا که‌توانستيم‬

‫درحواشی کتاب حاضر با ذکرنام آنان جای دادیم» ودربنجا با سیاسگزاری اسامی‌ابشان‌را‬
                     ‫باذ کرلهجه‌هابی که از آنها لغاتی را توضیح داده‌اند بادميکتيم ‪۰‬‬
 ‫امام (محمدعلی) (دزفولی)؛ لسانسية دانشکده ادیات و دیرادبیات فارسی در‬
                                       ‫بغداد (لغات دزفولی وانه کی از لغات شوشتری)‪.‬‬
‫دبیرساقی(محمد) ‪ ۰‬فارغالتحصیل دور کدتری ا
```


## [2026-09-06T21:23:36.374Z] TOOL CALL #34: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -50"
}
```


### [2026-09-06T21:23:36.419Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1261.png
1261.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1296.png
1296.txt
1296.vision.txt
1297.png
1297.txt
1298.png
1298.txt
1299.png
1299.vision.txt
1300.png
1300.txt
1300.vision.txt
1302.png
1302.txt
1302.vision.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
```


## [2026-09-06T21:23:38.983Z] TOOL CALL #35: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1237 --image 2>&1 | tail -40"
}
```


### [2026-09-06T21:23:46.803Z] TOOL RESULT

```
است - و والی و حاکم سیستان را نیز کوبندچه | است که‌متقی‌وپرهی زکاروسالح‌ولیکو کردارباشد۸ه ۰
سیستالرا لیمروزهم میخوانند . شاه يك اسبه - کنایه از خورشید
شاه وار ؟ <- با واوبالف کشیده‌بروزن | جهان گرد باشد -
۰ هرچز خوب راگود: ق بادشاهان "
ام دار » هرچیز خوب راکویند کهلابق بانشاعات | شاهین ‎٩‏ - بر وزن لاچین » معروف
باشد ازجواهر‌واسباب‌وخانه‌وامثال آن عموماودزی
که‌یی‌همتا بودخضوما وآ ترا دربتیم هم میگوب: است » و آن‌پرنده ای
۳ میور را دنم 6۳ ۳ ۶ | باعد شکاری وزنده‌از خ
ه ور5 ۰ < بروزن لاجوده. بسی | چنی سیامچشم نوزباند هه
هاله وطوق وخرمن ماه باشد. ترازوو چوب ترازو را ۱
شاهه - بنتح ثالك . ام شهری بوده‌بتا | نیز کویند - ویمدتی 6 /
کردة یدر سودابه در هاماوران و تولد سودابفزن تکیه کاءهم بنظر آهده : ۹ * 7
کیتاوی درآان شهرشده . است . بویا ٍ
شاهی ؟ -بر وزن ماهی . بمعنی شایان ۱۰ -
پادشاهی و سروری باشد - و نام شاعری هم بوده بایای<طی بروزن‌پایان. شاهین
است 8 سونام‌حلوایی است‌بسیاراطیف ولذید که‌از | مخفف شایگان است که بمعنی لایق وسزاوارودر
فشاسته‌و تخم‌مر غ‌ساز ندسونام‌زری‌ودرمی‌هم‌هست؟٩‏ ۰ | خور باشد - وهرچیز خوب را نیز کفته‌اند خواءه
شاهیدن ۷ بروزن چاهیدن, بمعنی | لابق پادشاه باشد وخواه امرا - و بمعمنی روا هم
پادشاهی کردن و بزرکی نمودن باشد - و بمعنی | اهست که بمربی جایز کویند - وممکن را ابیز
پارایی و بندکی کردن و صلاح و نقوی داشتن | کفته‌اند که درمقابل واجب باشد.*
۹ -رك4. نیمروز. ؟ - از: شاه + وار(پوند نسبت واصاف ولیاقت) : «دری شاهوار

ازصدف رحم بمهبط ظپورآمد.» «سندباد نامه۶۲؟ .۰ ۳ ه- شابورد (د.م (. ار ‌- از :شاء ی
(مصدری) . 8 - آقملك بن‌ملك جمال‌الدین قیروز کوهی معروف‌بامیر شاهی سبزواری‌متوفی
بسال۸۵۷ قمری.ر4:نذ کرء دولنشاه چاپ‌لیدنس۲۹ ‎٩‏ ببعد. ‎٩‏ -از:شاه + ی(سیت) * [70[2
(ر4: ربال). سکهٌ مسی بایکلی که ارزش آن بيت‌يك قران است ۰ کیلکی 51 ( مخفف آن).

۷ -از:شاه ۳ بدن (پوند مصدری). ۸ ر4:شاهیدن. ‎٩‏ - چنین مینماید که صفت «شاهین»
از وازه شاه درآ مده واين پر تده بمناسیت شکوه, وتوالاییوتقدی خود (شاه‌مرغان) خوآنده شده باشد
(قی :شاهیاز.م.م. ). شایدهم شاهین‌همان سثنه 928682 (ر4: سیمرغ) باشد که دراوستا نام عقاب
(< آله) امت. درلهجه‌ای بهیأت شائین 58028 بجای مانده است . «کایگر . فرهنگه ایران
شرقی.صس ۱6۱۹۶ فاب ۱ ص۳۱۶ .۰ ۹۰ - اسم فاعل از «شاستن».

* شاید بود - ر4 : شاسته بود .۰
# شایستن - بکرسوم » پپلوی 585215188 *- 5821120 (نواستن » فادر بودن) »
آزريشة اوستایی-55122(نواستن) (ر4 :شاه شهر) «بار تولمه 200۱ «ییب ر که4۲۱۶ «اسشق,هوبدمان

۵۸ کگیلکی58002 [502(عایدرفتن)*81128] 82-508(شاید کفتر) ؛سزاوار بودن,لایق
ومناسب بودن: «ملك کفتا هرآ بنه مارلخردمندیکافی‌باید تا قدییرمملکت رابناید» « کلستانمچ.
```


## [2026-09-06T21:23:55.611Z] TOOL CALL #36: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1237 --image 2>&1 | head -8"
}
```


### [2026-09-06T21:23:57.520Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1237.png
REF: BQT:1237  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 28  OCR-lang: fas

۱۲۳۷ شخامان
سوجای نشتن پادشاهان باشد - ونوعی ازعمارت | هم هست و ظاهرآً باین معنی با شاهندن صحیف
هم هت . خوانی شده باشدء, آمه اعلم.

شاه نیم روز ۱ - کنایه از آفتاب شاهیده ه بروزن‌چاهیده,بمعنی‌شاهنده
```


## [2026-09-06T21:24:01.815Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('data/verification/sources/refs/ocr/BQT/1237.png')\nprint(im.size)\nw,h=im.size\nim.crop((0,int(h*0.78),w,h)).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1237_foot.png')\n\"; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T21:24:04.867Z] TOOL RESULT

```
(1650, 2546)
total 23176
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:24 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb  969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     396 Sep  6 17:19 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb   97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44171 Sep  6 17:16 pg277.png
```


## [2026-09-06T21:24:08.047Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1237_foot.png"
}
```


### [2026-09-06T21:24:08.070Z] TOOL RESULT

```

```


## [2026-09-06T21:24:26.627Z] TOOL CALL #39: Bash

```json
{
 "command": "cat > data/verification/sources/refs/ocr/BQT/1237.vision.txt <<'EOF'\n[BQT p.1237, Mo'in's etymological footnote, read from the page image]\n* شایستن ـ بکسر سوم ، پهلوی shâyîtan – shâyistan (توانستن ، قادر بودن) ،\nازریشهٔ اوستایی xshây (توانستن) (رک: شاه ، شهر) «بارتولمه ۵۵۱» «بیرکه ۲۱۵» «اسنق ، هوبشمان\n۷۷۴» ، گیلکی sha shoon (شایدرفتن) ، na_sha guftan (نشاید گفتن) ؛ سزاوار بودن ، لایق\nو مناسب بودن: «ملک گفتا هرآینه مرا لختی خردمندی کافی باید تا تدبیر مملکت را بشاید» «گلستان...»\n* شایدبود ـ رک: شایستهٔ بود.\n۱۰ ـ اسم فاعل از «شایستن».  (بالای صفحه: شاهین ... «کایگر، فرهنگ ایران شرقی ص۱۶۴» فاب ۱ ص۳۱۴)\n[headwords on the page: شاه نیم روز، شاه یک اسبه، شاهوار، شاهه، شاهی، شاهیدن، شاهین، شایان، شایسته]\nEOF\necho saved"
}
```


### [2026-09-06T21:24:26.675Z] TOOL RESULT

```
saved
```


## [2026-09-06T21:24:29.315Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:648 --image 2>&1 | head -60"
}
```


### [2026-09-06T21:24:31.231Z] TOOL RESULT

```
no scan of BQT covers printed page 648 (see 'scans' in refs_online.json)
```


## [2026-09-06T21:24:35.130Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='BQT_v2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n pages',len(pages))\n# find persian page numbers? show a few page heads\nfor i in (100,200,300):\n    print('---',i,'---')\n    print(pages[i][:300])\nEOF"
}
```


### [2026-09-06T21:24:37.549Z] TOOL RESULT

```
n pages 684
--- 100 ---
      ‫‪4 -‬‬                                                                                  ‫‪ -‬چهمة قر کون‬
‫از‬      ‫کتابه‬     ‫جشمة نوريخش ه‬                                   ‫آقتلب الت ‪٩‬‏ ‪ -‬وماه را نیزکوبند ‪-‬‬
 ‫خورشید انور ‪ -‬وآب حبوان _ و دهان محشوق‬                    ‫حشمة قبر 
--- 200 ---
   ‫ره‬      ‫سل‬                                                                                         ‫خروه‬

 ‫فقیرآنرا با خرما بکوبند وبخوردد ؛ بواینمعتی‬         ‫والث مجهول بر‬
                                                                 ‫‪ -‬نم اول ث‬                  ‫خروه‬
‫باتشدید(‪)
--- 300 ---
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف ان
```


## [2026-09-06T21:24:42.294Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-06T21:24:43.964Z] TOOL RESULT

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
```


## [2026-09-06T21:24:50.049Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (86,108):\n    print('==== leaf',i,'(printed ~',i+540,')====')\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-06T21:24:51.978Z] TOOL RESULT

```
==== leaf 86 (printed ~ 626 )====
   ‫یروت‬                                                                                                  ‫چراغ منان‬
    ‫انازفراخیعیش ک‬
 ‫وثرت‬                                        ‫وسکون غین نقطه دار وفتح لام ک‪۰‬رم شب‌تاب‌را ‪ ۱‬معدوله‬
                                            ‫هت‬
           ‫وبیاری علف دواب باشد ‪# . ۷‬‬                                                      ‫کوبند ‪.‬‬
                                                                                           ‫‪۱‬‬
‫رب بهلو‪ -‬کنابه اکزی است که‬    ‫ج‬          ‫ی‬ ‫ر‬ ‫و‬ ‫گ‬ ‫ن‬ ‫ا‬ ‫‌‬ ‫ب‬ ‫ا‬ ‫ر‬ ‫ش‬ ‫ز‬ ‫ا‬ ‫ه‬ ‫ب‬ ‫ا‬ ‫ه‬
                                                                         ‫ن‬ ‫ک‬ ‫ن‬ ‫ا‬ ‫ف‬ ‫م‬ ‫‌‬ ‫ع‬ ‫ا‬ ‫جر‬
     ‫‪۱‬‬                ‫‪۱‬‬               ‫‪|۱‬‬                                                    ‫باشد ‪. ۴‬‬
‫مردم از پپاوی او فابده و لقم بابند ‪ -‬وفربه را‬                                                        ‫‪2‬‬             ‫‪۰‬‬
                     ‫گیوزیند که قض لامر باشد ‪.‬‬                   ‫چراغ واده ‪ «۴ ۳‬با رای فروعت‬
‫جرف دسنتس د اکیی ج‪51‬ل‪3‬د ‪2‬وا اب‬                            ‫و‪٠‬‏‬    ‫ررنام عا دیل ور باکت که‬
                                                                ‫‪O‬‬
                                                                ‫ام روشن کنند ت‪3‬‏ا باد نکشد ‪ .‬و مشکوة‬ ‫ان‬
 ‫‪ - ۸‬وعالب ‪۱‬هذه ‪۰‬شده ‪-‬‬          ‫>‬
                                ‫د‬  ‫‪۳‬‬
                                  ‫من‬ ‫‪-‬تر‬  ‫‪۰5‬‬
                                       ‫‪5‬روه‬ ‫وشىرىن‬                                    ‫‪۱‬‬
                                                          ‫‪۱‬‬                                        ‫‪۳‬‬         ‫‪4‬‬
                                                                                                             ‫همان ‪۱‬‬
              ‫وصاحب همت ‪-‬خرودمند باشد ‪# .‬‬
‫جر ر ان کیرا گونند که‌بسخنان‬
                                                          ‫چر اگر ‪٣‬‏ باکاف فارسی بروزن‪-‬ر اسر * ‪۱‬‬
                                                          ‫‪۱‬‬
                                                                                      ‫حبواتات چرنده را گودند ‪.‬‬
 ‫خوش دل مردم رابجالب خودراغب گرداند ومردم‬                       ‫جر ام د بروزن‌عوام‪ .‬چراگاه حوانات‬
‫ونابه از چایلوس ‪ -‬و فریب‬
                       ‫را از خود کند ‪ -‬ک‬                                                        ‫و علف زار باشد ‪.‬‬
                                    ‫‪.‬
==== leaf 108 (printed ~ 648 )====
  ‫رد ات‬                                                                                          ‫جاده‬




‫چکاو د بتح اول و ثالیبالفکشیده‬                   ‫دوخ چکاد ‪ 9‬بمعنی اصلم ‪۴‬باشد ‪ -‬ومر کوه‬
 ‫کیناجشك برزکه‌تر‬
                ‫زد ک‬
                   ‫بواوزده» پرنده‌ایست ان‬         ‫را (‪۱-‬گ)وبنه خصوساً ‪ ۴‬وبمعنی‌سپر هم‌هست‬
 ‫ووش آواز هم میشود (‪ » )۳‬و او را بعربی‬
                                     ‫خ‬                                     ‫که‌عربی جنه خوانند ‪. ۴‬‬
‫ابوالملیح خوانند ‪٩۱‬‏ ‪ -‬و چفاله را نگیوزیند ‪.‬‬      ‫جکاده ‪ » 3‬بروزن کباده‪ ,‬بمعنی چکاد‬
   ‫د‬
   ‫نو‬‫چافند‬
         ‫و آن چوبی باشدکهمیان آنرا بشک‬           ‫احت که تارکهسر ‪ -‬وبالای پیشالی ‪ -‬وسر کوم‬
‫جلاجل برآن صب کنند وسرآوازه خوانان بدان‬                ‫وسپر باشد که ترکان قلخان (‪ )۲‬گوبند ‪.‬‬
 ‫‪-‬ام‌نقمه‌ایست ازموسیقی‬
                      ‫اصول تگاهدارند ‪ ۱۱‬وی‬
                                                  ‫جکاسه = بفتح اول و سین بی نقطه‬
 ‫که آنرا نوای چکاوکے همخوانند ‪٩۷-‬‏ ونوعی‬          ‫‪.‬اریشترا گویند؛ وباشین قطمدار‬
                                                                              ‫خ‬                  ‫ا‬
 ‫کو تف‬       ‫ازمرغابی هم هتت که آنرا ترخات‬
                                                                                            ‫حم آمده است‬
‫چکا وش بر وزن تبارکے » نام توایی‬
                                                  ‫بفتح اول بر وزن هلاک‪: ‎‬‬                        ‫‪r‬‬
‫است اموزسیقی ‪ - ۳۱‬و مرغی باشدببزر کی‬              ‫_‬      ‫ناصید گویند‬       ‫کهسر‬         ‫ا‬        ‫ا‬
‫خوانند ؛‬      ‫ولیح‬
                 ‫ابرلهم‬
                      ‫وق‬‫کنجشك واعرببان‬
 ‫و بعضی گونند پرنده ات که آنرا سرخاب‬              ‫وو لهنوس ومندورنوس را هم کویند ‪- ۷‬‬
                                   ‫هکیویند ‪.۴۷‬‬
                                                  ‫وآنرا نیز کویند که در اوکوهر سوراخ کند‪. ۸‬‬
                                                   ‫جامه؟ ‪ 8‬بفتحآولوهیم بروزن نعامه‪.‬‬
 ‫چکاو گاه = بکون رابع بر وزن‬                          ‫طنلعی است باابیات‬
                                                                      ‫مآ‬‫و‬                   ‫یاند‬
                                                                                               ‫ور‬‫کیدہ‬
                                                                                                    ‫قص‬
‫| قرارگاه ‪ ,‬جابی است در گوشۀ کمان که کره سه‬
                                                   ‫متوازية متشار که درق
```


## [2026-09-06T21:25:03.217Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (106,107):\n    print('==== leaf',i,'(printed ~',i+540,')====')\n    print(t[i][:2600])\nEOF"
}
```


### [2026-09-06T21:25:05.449Z] TOOL RESULT

```
==== leaf 106 (printed ~ 646 )====
                                       ‫بیان چهار دهم‬


‫بمعنی چفاچاق است که صدا وآوازپیاپی خوردن‬           ‫جتح اول و سکون ثالی » چر ی‬        ‫چق د‬

                      ‫تیر باشد برجابی ‪.‬‬
‫چشماق ‪ -‬بروزن ومعنی چضماق است‬                     ‫آن جدا شود ‪ -‬و بتم اول مخفف چوق است ‪۰‬‬
   ‫که آش زه باشد ‪ .‬گوبند ترکی است ‪. ۴‬‬              ‫و آن چوی بات که بر کردن کاو گردونکش‬

‫جعماق‬       ‫مضفف‬   ‫بروزن خندی؛‬   ‫=‬   ‫حمق‬
                                                  ‫نهندا ؛ وکاهی ربکاو کردن‌هم‌اطلاق کنند ‪.۱‬‬
                          ‫اکستهآ تش زله باشد‪..‬‬     ‫بفتح اول و جیم فارسی‬         ‫جتاچاق؟‬
‫چشنف‌ر * ‪ -‬بم‌اول وثالی وسکون نون‬                 ‫بروزن رقاراق » صدا و آوازیایی خوردن تر باشد‬

‫ودال امجد مضموم برای قرشت زده » نام حوسعی‬                                                 ‫برجایی ‪-‬‬
                                                  ‫جتاچق؟ ‪ -‬بفتح اول و جیم فارسی ؛‬



                                       ‫بیان پانزدهم‬

‫چك » تح اول وسکون الی » بمعنی | ومنشور ‪ -‬و قبالهٌ خانه و باغ اومثال‌آن باشد »‬
‫مومرب آن صك امت ‪ ۷‬بفتح صاد ‪ -‬و آواز‬                ‫تب‬   ‫حەت‬
                                                          ‫و‬   ‫ویماله ‪-‬‬    ‫‪-‬‬   ‫وظقه و مواجب‬   ‫برات‬



 ‫‪ - ۴‬اسم صوت » درترکی« چقاچق »‬                   ‫رکه ‪ :‬چغ » جغ » جوع » بوغ ‪.‬‬          ‫‪۱‬‬
                           ‫ك‪.‬‬
                            ‫چےو‬
                              ‫اچا ک‬
                                  ‫عچکا‬
                                     ‫چه ‪:‬‬
                                        ‫بقتح اول و چپارم بهمین معنی « جننابی ‪ .»۶۸۲‬رک‬
        ‫‪.‬‬      ‫‪:‬ر‬
                ‫ند‬‫نکه‬
                    ‫‪۵‬چ ر‬              ‫ق‪.‬‬
                                       ‫مماخ‬
                                          ‫چهق‪ :‬چش‬
                                                ‫ورک‬‫‪.‬‏ ‪۴‬‬             ‫اچ‪:‬اق‬
                                                                        ‫فکه‬
                                                                          ‫چر‬‫‪۴‬‬
  ‫‪ - ۱‬معرب آن«صاث» و «شك» و«شاکه»‪ .‬و درترکی نیز «چك» بمعنی کره(عقده)‪.‬بند‪,‬‬
  ‫دفتر » ورقهٌ گواهی ‪ .‬فباله " اعضاء وبخت آهده «جفتابی ‪ .۶۸۲‬در انگلیی ‪ 0606‬و درفرانسه‬
  ‫علا‪»]۵0‬؛ درفرهنك‌های اروپایی وبتبع ابشان مژلف تفی‌کلمه را از ‪ 0 606216‬انگلیسی‌بمعنی‬
  ‫رسد کی کردن » خبط کردن ومقابله گرفته‌الد آون ازانگلیی وارد فرانسوی شده » ولی استعمال‬
 ‫اکیلمنهدرفارسی قدیم است چنانکه فردوسی‌بمعتی معاهده وصدیق نامهآورده (رك‪ :‬فهرست ولف) ‪:‬‬
            ‫ارز بود‬    ‫وی‬
                        ‫اگر چند 
==== leaf 107 (printed ~ 647 )====
                                                                                            ‫]‪0‬‬

‫لب ازچهارجااب بجول باد که آنرا‬
                             ‫جلابك‬
                                 ‫او‬                     ‫زخمتيغوصدایی که‌ازچیزی برآبدهمچوشکستن‬
‫دزد همگوبند ‪ -‬و کردکانی که مخزآن باسالی‬                 ‫چوب ولی وخوردن چیزی برچیزی وامثال‌اینها‪-‬‬
‫برنباید ‪ -‬و بمعتی صف ربع هم هست که من‬                   ‫وسخن را لیزگوبند چه چکدان بمعنیمخندان‬
                            ‫باشد یعنی هشت بك ‪.‬‬         ‫باشد ‪ -‬و بمعنی قطره ‪٩‬‏ ‪ -‬و چکیدن هم‌هست‪.‬‬
‫چکا چا" ‪ -‬تح اول و ثالیو جیم‬                            ‫و بان معنی بکسراول هم آهده است ‪ -‬ومشتة‬
‫فارسی هردوبالف کشیده و کاف ساکن ‪ ,‬آولز‬                  ‫حلاجان ‪ -‬وچویی بودپنج شاخه ودسته دباارندام‬
‫وسدای ضربت یغ وشمشیر وگرز باشد که از‬                    ‫پنجهُ دست کهدهقانان بدان غله کوفته‌شده را(‪)۱‬‬
                                      ‫یی هم زلند ‪۲‬‬
                                                        ‫برباد دهند تا ازکاه جدا گردد و بعربی مدری ‪۴‬‬
 ‫زرن بلارك »‬‫ول ب‬
               ‫جکاچك » تم او‬                            ‫خوانند ‪ -‬و بربدن شاخ درخت انگور و غیره‬
 ‫مخفف چکاچا کے است‪ ۷‬که صدای‌زدن شمشیر‬                   ‫ویمعتی‬     ‫باشد ‪ -‬و معدوم ونابود را همکفته‌اند‬

 ‫وگرز باشد از پی‌هم ‪ - ۸‬وصدای برهم خوردن‬                ‫فك اسفل هم هست که چانه و زشدان مردم‬
 ‫ویند ‪ 7-7‬وضم هر دوجیم فارسی »‬
                             ‫گز‬‫دندان را ن‬               ‫وحیوانات دیگرباشد ‪ -‬و بترکی‪ ۴‬امربکشیدن‬
 ‫سخنی و خبری را (‪ )۲‬گویند که درافواه افتد ‪.‬‬            ‫است یمتی بکش ‪ -‬و بضم اول مخفف چوك است‬
 ‫حگاد‪ = ۹‬بقتح اول بروزن‌سواده بالای‬                    ‫که آلت تناسل باشد ‪ - ۴‬و بزبان ترکی اهر‬
 ‫صروبالای بشایرا گویند عموما‪.‬چه بلفت‌بهلوی‬               ‫وبکر‬        ‫بزالو زدن بود بعنی بزالو درآی ‪۵‬‬

                                          ‫(‪ )۷‬چش ‪ :‬چیزیرا‪.‬‬            ‫(‪ )۱‬چش ‪ :‬کوفته شفه‪.‬‬

                                ‫‪.‬دهخدا)‬   ‫بکن(یکی‬     ‫لسود ازس تدره خا‬     ‫چکه‪:‬چکی‌خون‬      ‫=‬   ‫‪۱‬‬
  ‫صمتن را سرازتیغ جاك‬

  ‫«لفت فرس ‪5۰۳۰‬‬
                   ‫‪ - ۴‬صحیح مذری و مذراة (هردو بکس اول) است ‪« .‬اقرب‌الموارد» ‪.‬‬
             ‫‪.‬‬   ‫چوك‬   ‫‪:‬‬   ‫رك‬     ‫‪۴‬‬         ‫‪- ۴‬رتکی آذری ‪( 26‬بکش) [یکرکاف ] ‪.‬‬
                           ‫( بزانوشتن) ‪.‬رك ‪ :‬چوك ‪.‬‬        ‫‪ ۵‬درتر کی آذری ‪kam‬‏ ‪60 -‬‬
  ‫جقلجاق‪.‬‬   ‫رك‪ :‬جاجاك»‬          ‫جخاجح ‪۲ ۰‬‬    ‫چفاچق‪.‬‬   ‫جقاجاق؛‬    ‫رك ‪ :‬چکاچك‪.‬‬   ‫‏‪ ٩‬ت‪ --‬اسم سوت‬

                                                                   ‫‪
```


## [2026-09-06T21:25:27.542Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport json,re\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\nfor p in ('1237','1316','1310','1320'):\n    print(p, m.get(p))\nEOF"
}
```


### [2026-09-06T21:25:29.225Z] TOOL RESULT

```
1237 28
1316 107
1310 101
1320 None
```


## [2026-09-06T21:25:32.744Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages_faseng.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,blk in enumerate(t):\n    if '[pdf page 107]' in blk[:200] or '[pdf page 107]' in blk:\n        print('found at',i); print(blk[:3500]); break\nEOF"
}
```


### [2026-09-06T21:25:34.608Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'incoming/BQT/BQT_v3_pages_faseng.txt'
```


## [2026-09-06T21:25:37.547Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor blk in t:\n    if 'pdf page 107]' in blk[:300]:\n        print(blk[:3500]); break\nEOF"
}
```


### [2026-09-06T21:25:39.476Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
721
[pdf page 107]
شهربار سوت
شهر یار ۱ - با ‎ct‏ کدیدموبرای | ام ماه هشتم ۴ باشد از سال شممي + وآن‌بودن
قرشت زده ۰ پادشاهی را کوشد که‌ازهمٌپادشاهان | آفتاب است دز برج سنبله - و نام فرشته ایست
عص خود ‎Srp‏ باشد - ‎AW‏ وبزرکهتهر | موکل ‎AT‏ و موکل برجمیع فلزات وندبیر
‎eb‏ میگویند . امور و مصالح ‎ole‏ شهربور که روزچهارم است از
۲ ۹ ماه 2 تعلق_ دارد ۰ درین روز منان
شهریده ۲ ‎ngs‏ ید ای | ‎et‏ زو ی
‎wey on : | sou aS‏ سازند بنایر قاعدژ ‎SS‏ لرد
پرا کند» و پریشان شده و از هم‌پاشیده - ‎gies‏ ن مت است که‌چون تامروز با نام ماموافد
و ‎a Soe‏ باشد. ایثان معتبر است که‌چون ‎Sy rl‏ با نام ماء‌موافق
شم ر ۳ ۳۹ آید ‎as‏ بابدکرد و ببپ ‎SGT‏ دربن روزتولد
مر 7 4 ‎Oe‏ تس تک | داراب ‎ott ily‏ بود جشن ‎wile‏ وعیدکنند.
شهرپور است که ماء هشتم ۴ ‎goat‏ باشد - ‎(a‏ ۰ ان ۷ = ‎Gt‏ فار بالف
روز چهارم است از هرماه شمسی * . سهر بور لان " = ‎SEL‏ فارسیب
شهر بود ۱ - با وار بروزن برزیگر, | کشیده وینون زده » نام روز چهارم است ازماه

۱ - پهلوی ‎Yiyyl » shabrdar‏ ۱۹۵ ) و 524۳5۳80۳27 ( نگاهبان شهر ) . از
‎dar +(_,+) shathr‏ (از: داشتن) دیب که۲۱4». اوسنا - ‎syle: OxShathrO. dara‏
(کتیبه‌ها) ‎ads = ۴ . ۷ peels Shatrdardn‏ (هم) .

۴ - مخفف ‎ee?‏ بور» (هم.) . ۴ صحیح «شتم» است .
۴ - چو در روز شهربرآهد بشهر ز شادی همه شهر را داد بهر .

لبیبی . «انجمن آراه ورگ نح ‎٩‏ .

۱ - دراوستا ‎xshathra vairya‏ , پپلوی ‎shatrivar‏ مر کب ‎xshathra_:;1‏
‏که در اوستا ویارسی باستان وسالسکریت بمعنی کشور وپادشاهی است (رله: شهر) وجزو دوم صفت
است از - ۷2۲ ۵ بمعنی برگزیدن » برتری دادن و گروبدن 1 وثیربه بعنی برگزیده, ‎Rwy‏
‏مر کب یمنی کشور منتخب با پادشاهی بر گزبده . ايين کیب بار ها در اوستا بمعنی بهشت با
کشور ‎GL-T‏ اهورمزدا آمده - ‎jay‏ نام امشاسیندی است که نگهبانی ششمین ماه سال وچهارمین
ررز ماه بدهسپرده شده . وی درجوان برین ‎Sala‏ پادشاهی ایزدی و فر و اقتدار خداوندی است
ودرجهان مادی پاسبان ‎ot‏ میباشد . در کتاب الازهنة والامکنه تألیف امام ابوعلی مرزوقی
اصفهایی ( متوفی 4۷۸ < . ) بجای شهرربور «شهربر» ( «م ) ‎eel‏ التفپیم مسحح همایی ص
۶ و فردوسی طوسی لیزهشهیر» آورده :

زشهری بادی تو ‎Si‏ نام بزرگی و فر و هثر (ورك: : ح ‎Ae‏
‏آبوریان بیرولی درفهرست روزهای ابرانی نام این ررز را « شهریور * و درسفدی « خستشور ©
(حستدور ..ن ‏ ل ۰ ) ودرخوارزمی ‎ory AF‏ باد کرده . در کالشی ‎sharir mAh (OAS)‏
نام ماه دهم سال است «روزنامة کیلاشهر سال اول شمارة ۲۲: زندکی وعروسی ساکنن‌جنگل»,
درطبری 5]187۷10,مازسرانی کنونی ‎sharvare m4: sharvire ma. sharvine m4‏
‎oly?‏ نامه 1۷۵ وص ‎٩۲۵۸‏ . مسعود سعدلاهوریگوید:
ای‌تنت‌رازبیکو بیز یور شهر»روزیست روزشه_بور. «دبوانمسعود۹ ‎٩۵‏ ورك: ‎slaty‏ ۰۷۱-۱۹

۲ - از : شهربور (هم.) ‎A‏ کان ( پوند سبت - جشن ) جشنی که درشهربور روز
(چهارمین روز) از شهرربورماء (شذمین ماء) درامران باستان برپا میداشتند. «پورداود. بختها ج(ص
۳ «خرده اوستا ۰۲۰۵ .
```


## [2026-09-06T21:25:54.409Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xs'y\\|xš'y\\|xšy\\|xsy'wn\\|xš'wn\\|xšēwan\\|xsewan\" SOD.txt | head -20; echo \"=== search 'to rule' ===\"; grep -n \"to rule\" SOD.txt | head -20"
}
```


### [2026-09-06T21:25:54.471Z] TOOL RESULT

```
12196:(3)xsewan   Cysywn)  ^'Ysy'wn,  xsywn 
12203:(a)xsewane,  oxsyone   ©<*xsaivanaka  ©ob.  pi. 
12327:(o)xsewan   Oysywn)   ^ys'ywn,  'xs'ywn 
12333:(s)xsewanken 
12341:svida-,  Yaghn.  xsift   =>xsy(3t,  'xs'yPt- 
12407:(o)xsewane   ©*xsaivanaka-   =>Pyy  >ysywny, 
21434:2083  'xs'y-   M  Q^J'^bJ^J  <o^oJa.U 
21441:2084  'xs'ypt-,  S  ^ 
21447:2085  'xs'ywn   S  \^  Loy^ 
21448:axsewan  ^ysy'wn 
21580:(o)xsewan(a)kya  ? 
21586:axsewane   Oxsywn'k)  ^ysywny,  xsywny(y), 
21593:axsewane-Payi 
21599:sxsewanemec   ^MLK'mync,  'ysywn^mync, 
24848:Paye/i  axsewane   Oysywny  'PcmpS'k) 
57017:7330  prxs'y-   S  j^^^  t^J'dy^'^j^J^J'^ 
57027:parxsyakc  ?  ©<xsi-  krti  --^prxs'y- 
74882:9897  w'xs'yk'  S,  M 
80166:10654  xs'y-  =*  yxs*y- 
80231:xsewankya,  xsowanakya   ^xsywnqy* 
=== search 'to rule' ===
```


## [2026-09-06T21:25:56.853Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21425,21460p' SOD.txt; echo \"#### 12190-12215\"; sed -n '12190,12215p' SOD.txt"
}
```


### [2026-09-06T21:25:56.920Z] TOOL RESULT

```
-tyK  Hen.  Tales.  470.47 

2082  'xs'wnmync   M  (^ioL.<^li 
oxsawanmenc   =>'xsywnymync 

royal 
GMS  1103 

2083  'xs'y-   M  Q^J'^bJ^J  <o^oJa.U 
(o)xsay   (xs*y-)  ^'ys'y- 

Go)rule 

GMS  1086;  C2  n  p51;  Sund.  Man.  Lett.  310.16 

2084  'xs'ypt-,  S  ^ 
oxsipd   OxsyPt-)  ©Av.  xsvipta  ^ysyPt,  xsypt 
milk 

KG  504,  -y,  505;  MSP  a5 

2085  'xs'ywn   S  \^  Loy^ 
axsewan  ^ysy'wn 

lament 
MSP  bl69 

2086  'xsn'qc  =>  'fsn'qc 

2087  'xsn'm   M  y^tjJj^x* 


83 


#### 12190-12215

dirt,  mixture  ? 
TSP  9.63  n221,  233 

726  'Ys'ywn   B  o^ 

(3)xsewan   Cysywn)  ^'Ysy'wn,  xsywn 
lamentation,  crying 

GMS  1084;  VJ;  TSP  6.92;  SCE  477;  Frag.  Len.  60, 
5;  -y  83  a  11 

727  'ys'ywn'k   B  ,li 
(a)xsewane,  oxsyone   ©<*xsaivanaka  ©ob.  pi. 

-ty  -^'xsywnCy),  xsywny(y),  ^sywn'k,  MLK(,) 
king,  ruler 
BSTBL,  Dhu.  37(N),  136,  266,  255;  Vsywrtyty, 

Dhu.  55 

728  >Ysd,r-   C  j^jUT 
ayasSar   ©perf.  st.  «>Yz-.  'yst- 

(/£>)bcgin 
BSTi  31.186
```


## [2026-09-06T21:26:11.017Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12315,12350p' SOD.txt; echo \"#### pages file\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (92,93,94,95):\n    print('=== leaf',i,'(printed ~',i-66,') ===')\n    print(t[i][:900])\nEOF"
}
```


### [2026-09-06T21:26:12.803Z] TOOL RESULT

```
fourth  day  of  the  month 
MDii  p94.5  A-9R5;  MDiii 

743  ^sy'k-   B  oj^j^tjxyr 
(o)xsaye/-yak  ?   ©<*xsawaya\  Yaghn.  xisoy 

©inf. 
0c?)gnaw 
SCE  83;  Gersh.  BSOAS  17,  481;  IF  1970,  304 

744  >YsyVn   S  */<Jj^ 
(o)xsewan   Oysywn)   ^ys'ywn,  'xs'ywn 
lamentation 

GMS  1084;  Hen.  Tales.  483.10;  MDii  p47.15 

745  >Ysy>wnkyn   S  J*Jofs~ 
(s)xsewanken 

mourner 
Frag,  Len.  39.6 

746  >ysypt   B,  S  ^ 
(o)xsi(3d   ©Av.  xsvipta-i  Parth.  syfu  Khot. 

svida-,  Yaghn.  xsift   =>xsy(3t,  'xs'yPt- 


-I  ioJjU^S  iali- 


—j -J  i  J3j~*  ie\~- 


milk 
#### pages file
645
=== leaf 92 (printed ~ 26 ) ===
                                                                                                                            )ysykn5h
27

      first                                                                   (to)gct angry
      GMS 994, 1331, 1296                                         •^if        Anc. Lett. 3.23; GMS 870
684 >ftrt-       M                                                       697 'yr'nwkCw) S                                         fU.
      (o)ftart       ©pt. st. =»>Ptyr-, *J3t>rt                              (o)yrank
                                                                             rank     ?, yranuk ?

      (to)pass
                                                                              MDii pl20n 11
      GMS 169, 318
                                                                         698 VP-        S(AL) =* yr[3-
685 'yS^ >z2        
=== leaf 93 (printed ~ 27 ) ===
*ysyktc                                                                                                             28


 710 >ysyktc S                                      ^r^-^'    725 >Ys>yn B                                   ? J^J
     axsckac (ysyknSh) ©f. adj.                                    (o)xsen ? (YS}yn)
                                                                   dirt, mixture ?
     (f rom) Akhsekal
     MDiii p90                                                     TSP 9.63 n221, 233
                                                              726 'Ys'ywn      B                                o^
 711 ^syn =* 'ys'ynh
                                                                   (3)xsewan Cysywn) ^'Ysy'wn, xsywn
 712 >Ys,m    S(MD)=» xs'm                                         lamentation, crying
 713 •y^w'n     S                            *- ^.hJ+J A <&     
=== leaf 94 (printed ~ 28 ) ===
                                                                                                                      'Yt'w
 29
                                                                   milk
 735 >Ysnyrkc,) B                                       uUj
       (o)xsnirk ? Oysnyrkh) =^xsnyrk(>1                           VJ 6a, 1029; BBB plOl; Tales. 486.22; GMS 243
       mark, target                                            747 >ysyptk B, S                               ^
       GMS 976 nl; TSP 7.198, 22.7; BSTBL, Dhy.                    (o)xsi(3de OysyPty) ©Yaghn. xsift-, Khwar.
         85(N), 154, 224, 333; -\ Dhy. 226; pi. -tt Dhy.             xwflcy =>xsyPt
         371; -w, Karab. Insc. 19.7; -h, VV-Li 71                  milky, milk
 736 'ysnyrkh S => >Ysnyrk(,)                                     BSTBL, Vim. 25; VJ 6", 1029; BBB plOl cl8
 737 >Ysp- B,S                    
=== leaf 95 (printed ~ 29 ) ===
 ^tSv
                                                                      satisfied                                            30
 760 'yt'w1    B =» >ytyt
                                                                      VJ 112 & etc.; Tales. 475.30
 761 }Ytc S                                         J*(f <floj
     ay(^)c, ayac Oyc) ©f. adj. =»Yy\ Yc                         774 'yws'nty'kh S                           o.U>Jtl5j^>
        all, complete                                                 (o)xusandyak ^Yws'nty'kh, xwsndy*
                                                                      satisfaction
        GMS   1273; W-Li 94.2
                                                                      MDii Nov, 5, 11
762 ^tmzyn => ^ytmzyn
                                                                 775 >yws-      B, S                 u^*ry      o-^J^y-
763 »ytw
```


## [2026-09-06T21:26:27.337Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (91,93):\n    print('=== leaf',i,'===')\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-06T21:26:28.992Z] TOOL RESULT

```
=== leaf 91 ===
                                                                                                                           26

     'dyqmyc


                                                                          1981 p231
          custom, way, manner
          BSTii 893.6; Benv. Et. 2, JA 1959, 125; S W, C2,         673 'frytystr C
            31V6, 30n p75                                              afritistar, afritestar

     663 'dyqmyc        C                          ^lu^j^              most praised
         a8ikmec                                                       BSTii 886.14; C2, 51V 14
         habitual                                                  674 'frywn     M, C                                 CjtJ^J^
          BSTii 910.52; C2, 61V22; Bcnv. Et. 1, 318, JA                afriwan =»*Prywn, *frywn, *prywn      ji J * 'J^
            1955                                                       praise, blessing
                                                                       BBB; GMS 1084; STi 34.1, 52.11; STH3.38, 6.24;
     664 >dysn C                                  JUx^^!
         a5cs(o)n ©<*ham-daisana        -^nSysn                         BSTii: C2 gloss. +kwn- "to praise"
         model, sample, example                                   675 'frywncyq M, C                             yjl cj^
                                                                      afriwancik
          BSTii 886.18, 903.6; C2, 31R14, 51V18, 57R6;
                                                                       praise, blessing
            Bcnv. Et. 2.123     :
                                                                       BBBc26;GMS 1015; STi 34.5
     665 'dy(y) C          (j^>^ jj>)u*^<uSjhuJ'                  676 'fsn*qc C                                ^l>^>1 <^!^
         a5e (*5y) ©ace. }dw-t abl. }d\ pi. -/; ob. pi. -ty
           =»»5>kw                                                    Oxsn'qc) ©*fra-san
         somebody                                                      trepidation
                                                                       C2, lV9n p51
         STi; STii; BSTi; BSTii; C2 gloss.; S W, SGI 1986,
           408                                                    677 >fsnyh M                                          jUil
                                                                      afs(o)nc ?
    666 'fVnpa      B, S =» )fcmb8(8)                                 spreading

    667 
=== leaf 93 ===
*ysyktc                                                                                                             28


 710 >ysyktc S                                      ^r^-^'    725 >Ys>yn B                                   ? J^J
     axsckac (ysyknSh) ©f. adj.                                    (o)xsen ? (YS}yn)
                                                                   dirt, mixture ?
     (f rom) Akhsekal
     MDiii p90                                                     TSP 9.63 n221, 233
                                                              726 'Ys'ywn      B                                o^
 711 ^syn =* 'ys'ynh
                                                                   (3)xsewan Cysywn) ^'Ysy'wn, xsywn
 712 >Ys,m    S(MD)=» xs'm                                         lamentation, crying
 713 •y^w'n     S                            *- ^.hJ+J A <&        GMS 1084; VJ; TSP 6.92; SCE 477; Frag. Len. 60,
     (5)xsawan -^YS'wn'k, xs'wn, 'xs'w'n                             5; -y 83 a 11
     king ?, rule ?
                                                              727 'ys'ywn'k     B                                   ,li
     Karab. Insc. 20.21
                                                                   (a)xsewane, oxsyone   ©<*xsaivanaka ©ob. pi.
714 >YS,w,n)h   B, S                              o^^U               -ty -^'xsywnCy), xsywny(y), ^sywn'k, MLK(,)
     (3>xsawana Oys'wnyh, ^s'w^h)                                  king, ruler
                                                                   BSTBL, Dhu. 37(N), 136, 266, 255; Vsywrtyty,
     rule, power         *
     BSTBL, Intox. 8; Karab. Insc. 16.5; MDii                        Dhu. 55

                                                              728 >Ysd,r-   C                               j^jUT
715 'ys'w'ncyk S                                oJaL-^U.
    (o)xsawancik                                                   ayasSar ©perf. st. «>Yz-. 'yst-
                                                                   (/£>)bcgin
     kingship, rule                                                BSTi 31.186
     Karab. Insc. 18.15; CII 1990 E 3
                                                              729 >Ys5rkt,k B                               jyU,
716 >Ys,w>n6Vy S                                       ^U         (o)xsa5r-kate, xsa9r-kote ©<*xsa6ro-Icrtaka
    (o)xsawan5are, xsonSare       Oys'wnS'ry)                     (made for)king, kingly
```


## [2026-09-06T21:26:45.011Z] TOOL CALL #52: Bash

```json
{
 "command": "pdftoppm -f 278 -l 278 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg278 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg278.png"
}
```


### [2026-09-06T21:26:47.061Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 89267 Sep  6 17:26 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg278.png
```


## [2026-09-06T21:26:49.365Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg278.png"
}
```


### [2026-09-06T21:26:49.814Z] TOOL RESULT

```

```


## [2026-09-06T21:26:49.812Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T21:27:01.784Z] TOOL CALL #54: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg278.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/278.png && echo ok"
}
```


### [2026-09-06T21:27:01.846Z] TOOL RESULT

```
ok
```


## [2026-09-06T21:27:03.969Z] TOOL CALL #55: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T21:27:03.977Z] TOOL RESULT

```


```


## [2026-09-06T21:27:08.483Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%B1",
 "prompt": "Give the Persian entry for شیر: the etymology of شیر \"lion\" (šir/šēr) in full — Middle Persian form, Proto-Iranian reconstruction, cognates — and also شیر \"milk\" and any note distinguishing them."
}
```


## [2026-09-06T21:27:12.515Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-",
 "prompt": "What does this page say? I am looking for the PIE roots *tḱey- \"to settle\" and *tkʷeh₁- \"to acquire, gain power\". Report the reconstruction, meaning, and derived Indo-Iranian forms (Sanskrit kṣáyati, Avestan xšayeiti, xšaθra-, Old Persian xšāyaθiya-)."
}
```


### [2026-09-06T21:27:14.738Z] TOOL RESULT

```
# Persian شیر - Etymology

## شیر "Lion" (šir/šēr)

**Middle Persian form:** 𐫢𐫃𐫡 (šgr /⁠šagr, šēr⁠/, "lion; (astronomy) Leo")

**Proto-Iranian reconstruction:** *xšiHrám

**Cognates:** The term appears across related languages including Burushaski and Central Kurdish, sharing the same Proto-Iranian root.

## شیر "Milk" (šir/šīr)

**Middle Persian form:** 𐫢𐫏𐫏𐫡 (šyyr /⁠šīr⁠/, "milk")

**Proto-Iranian reconstruction:** *xšiHrám, from Proto-Indo-Iranian *kšiHrám

**Key distinction:** The two terms derive from different Middle Persian origins and represent separate etymological paths, though both trace to ancient proto-language roots. The "lion" sense originates from a Middle Persian astronomical/animal term, while "milk" connects through the Indo-Iranian language family's proto-forms.
```


### [2026-09-06T21:27:19.601Z] TOOL RESULT

```
# PIE Root *tḱey- Analysis

## Reconstruction and Meaning

The page documents **\*tḱey-** (imperfective), with three related meanings:
1. "to cultivate"
2. "to settle"
3. "to live"

## Etymology

According to the source, this root represents "a reanalysed root of *tḱéyti, from *teḱ- ('to sire, beget') + *-éyti" or alternatively derives from a zero-grade formation.

## Indo-Iranian Derivatives

The page lists several Indo-Iranian descendants:

- **Sanskrit**: Forms like क्षेम (kṣema) and क्षिति (kṣití) are documented
- **Avestan**: Various reconstructed forms including šaiiana and šiti are noted
- **Proto-Indo-Iranian**: Reconstructions like *ćšáyma- and *ćšitíš are provided

However, the specific modern Persian or Sanskrit forms you mention (kṣáyati, xšayeiti, xšaθra-, xšāyaθiya-) do not appear explicitly on this particular page, which focuses on the *tḱey- root rather than *tkʷeh₁-.
```


## [2026-09-06T21:27:27.975Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87",
 "prompt": "Persian شاه: give the full etymology (Middle Persian, Old Persian xšāyaθiya-, Proto-Iranian, PIE root) and any note on derived words like شهر, پادشاه, and the borrowing into Arabic/European chess terms."
}
```


## [2026-09-06T21:27:29.484Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%87%D8%B1",
 "prompt": "Persian شهر \"city\": give the full etymology — Middle Persian šahr, Old Persian xšaça-, Avestan xšaθra-, Proto-Iranian, PIE root and the semantic shift from 'kingdom/dominion' to 'city'."
}
```


### [2026-09-06T21:27:35.009Z] TOOL RESULT

```
# Persian Etymology of شاه (šāh)

## Full Etymology Chain

The word شاه traces back through multiple historical layers:

**Middle Persian**: 𐭬𐭫𐭪𐭠 (mlkʾ /šāh/) 
**Old Persian**: 𐏋 (XŠ /xšāyaθiya/, "king")
**Proto-Iranian**: *xšáyati
**Proto-Indo-Iranian**: *kšáyati ("he rules, he has power over")
**Proto-Indo-European**: *tek- ("to gain power over, gain control over")

## Core Meaning

The root fundamentally expresses power and rulership, evolving from the general Indo-European concept of gaining control into the Persian designation for a monarch.

## Related Persian Derivatives

The page notes several compounds using شاه as a component, including شاهنامه (šāhnāme, "Book of Kings") and شاهزاده (šāhzāde, "prince").

## Chess Terminology Legacy

The word's most significant modern legacy appears in chess vocabulary. Arabic borrowed شاه, which subsequently entered European languages via Medieval Latin *scaccus, eventually yielding English "check" and "chess."
```


### [2026-09-06T21:27:36.739Z] TOOL RESULT

```
# Etymology of Persian شهر (šahr) - "city"

The word traces back through several linguistic layers:

**Middle Persian:** شهر (šahr) - the direct ancestor form

**Old Persian:** 𐎧𐏁𐏂𐎶 (xšaça-) - earlier attestation of the root

**Avestan:** 𐬑𐬱𐬀𐬚𐬭𐬀 (xšaθra-) - ancient Iranian religious texts

**Proto-Iranian:** *xšaθram - reconstructed prehistoric form

**Proto-Indo-Iranian:** *kšatrám - the deepest reconstructed level, meaning "kingdom/dominion"

**Proto-Indo-European:** *tek- - the ultimate root meaning "to receive"

## Semantic Shift

The word underwent significant semantic evolution: it originally denoted "kingdom" or "dominion" in its Indo-Iranian ancestor forms, then narrowed to mean "city" or "town" in Persian and its descendants. This reflects how political administrative centers became synonymous with urban settlements themselves.

The term's descendants include Turkish şehir, Albanian sheher, and Serbo-Croatian šȅher, all borrowed from Ottoman Turkish.
```


## [2026-09-06T21:27:44.424Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek-",
 "prompt": "Give the reconstruction, meaning, and all derivatives listed for this PIE root, especially the Indo-Iranian (Sanskrit kṣáyati, kṣatrá-, Avestan xšayeiti, xšaθra-, Old Persian xšāyaθiya-) and Greek (κτάομαι) ones. Also note any mention of Pokorny's numbering or alternative reconstructions like *tkʷeh₁-."
}
```


## [2026-09-06T21:27:46.007Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/satrap",
 "prompt": "Give the full etymology of \"satrap\" including Greek satrapes, Old Persian xšathrapavan, and the meaning of the elements. Also anything on \"Xerxes\" if mentioned."
}
```


### [2026-09-06T21:27:53.242Z] TOOL RESULT

```
# Proto-Indo-European *tek- Root Analysis

## Reconstruction and Meaning

The PIE root **\*tek-** has two distinct meanings:

1. **Root 1**: "to take by the hand; to receive, obtain"
2. **Root 2**: "to weave"

## Major Derivatives

### Indo-Iranian Descendants
- Sanskrit: **kṣáyati** (from \*tkh₁-éy-e-ti, meaning "to rule, have power over, control")
- Sanskrit: **kṣatrám** (from \*tk-e-tróm, related to rulership/power)
- Old Persian: **xšāyaθiya-** ("king")
- Ossetian: **æxsin** ("lady, mistress")

### Greek Descendants
From \*tk-eh₁- formation:
- **κτάομαι** (ktáomai) - "to possess"
- **κτῆμα** (ktêma) - "possession"
- **κτῆνος** (ktênos) - "livestock"
- **κτῆσις** (ktêsis) - "possession"

### Other Major Branches
- **Latin**: texō (from Root 2, "to weave")
- **Hittite**: tákkišzi (from Root 2)
- **Germanic**: þigjaną (Proto-Germanic)

## Source References

Per Pokorny (1959), this root appears at pages 1057-1058 of the *Indogermanisches etymologisches Wörterbuch*. Helmut Rix's *Lexikon der indogermanischen Verben* (2001) also documents both roots.

## Reconstruction Note

Root 2 shares semantic overlap with \*teḱ-, and only Old Armenian conclusively indicates the plain velar *k*.
```


### [2026-09-06T21:27:53.464Z] TOOL RESULT

```
# Etymology of Satrap

**Full Etymology Chain:**

The word "satrap" entered English in the late 14c. from Latin *satrapes*, which derived from Greek *satrapēs* or *exatrapēs*. These Greek forms traced back to Old Persian *xšathrapavan-*, literally meaning "guardian of the realm."

**Component Elements:**

The Old Persian term breaks down into two parts:
- *xšathra-*: "realm, province" (related to *xšayathiya* meaning "king")
- *pavan-*: "guardian" (stemming from the PIE root *\*pa-* meaning "to feed; to guard, protect")

**Semantic Development:**

Originally denoting a provincial governor in ancient Persia, the term was "extended by late 14c. to any autocratic superior" and figuratively to despotic officials serving tyrants, a usage reflected in Medieval Latin and Romance languages.

**Note on Xerxes:**

The page does not mention Xerxes. However, it does reference the shah connection—the Old Persian root *xšayathiya* ("king") relates to the title "shah," though these represent different etymological paths rather than direct connections to Xerxes specifically.
```


## [2026-09-06T21:27:57.859Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/check",
 "prompt": "Give the full etymology of \"check\" (both the chess sense and the bank-draft/cheque sense), \"chess\", and \"checkmate\": Persian shah, Arabic, Old French eschec, and what it says about the origin of \"cheque\" (whether from Persian/Arabic sakk or from check 'to stop')."
}
```


## [2026-09-06T21:28:00.096Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/afsin-title",
 "prompt": "What does Encyclopaedia Iranica say about the title Afšīn: its etymology (Sogdian xšēwan / Old Iranian form), whose title it was, and the historical bearer Ḥaydar b. Kāvūs?"
}
```


### [2026-09-06T21:28:02.242Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T21:28:04.273Z] TOOL RESULT

```
# Etymology of Check, Chess, and Checkmate

## Check
The word originates from chess terminology around 1300. It derives from Old French *eschequier* ("check at chess"), which traces back through Vulgar Latin *scaccus* to Arabic *shah* and ultimately Persian *shah* meaning "king." The term later extended to mean "sudden stoppage, hindrance, restraint" (1510s), leading to financial uses like the banking instrument.

## Cheque/Check (Bank Draft)
The etymology notes: "the financial use for 'written order for money drawn on a bank, money draft' (1798, often spelled *cheque*), which was probably influenced by exchequer." The document does not confirm whether the banking sense derives from Persian/Arabic *sakk*, only that it may have been influenced by the word *exchequer*.

## Chess
The page references chess terminology but doesn't provide separate etymology for "chess" itself beyond noting its connection to *eschequier* and the Arab *shah*.

## Checkmate
Dated to mid-14c., this term comes from Old French *eschec mat* via Arabic *shah mat*, literally "the king died," combining the same Persian royal term with an Arabic phrase indicating defeat.

All three words share the Persian *shah* as their ultimate origin.
```


## [2026-09-06T21:28:14.939Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%DB%8C%D9%86",
 "prompt": "Persian افشین (Afšin): etymology — is it from Sogdian xšēwan / Old Iranian *xšāwan- \"ruler\"? Give the full etymology and meaning."
}
```


## [2026-09-06T21:28:15.575Z] TOOL CALL #65: WebSearch

```json
{
 "query": "Afshin title Ushrusana etymology Sogdian xšēwan Old Iranian *xšāwan ruler"
}
```


### [2026-09-06T21:28:20.667Z] TOOL RESULT

```
# Afshin Etymology

Based on the Wiktionary entry provided, here's the documented etymology:

**Etymology:** The word is "possibly borrowed from Bactrian *Afšiiano*, related to Middle Persian *Pišīn* or cognates in other Middle Iranian languages, especially Sogdian, of unknown ultimate origin." The entry notes it's "akin to Avestan *pisinah-* and Old Armenian *Apʻšin/Ōšin*."

**Meaning:** It's a male given name in Persian, derived from Middle Persian.

**Important caveat:** The source document does *not* mention Sogdian *xšēwan* or the Old Iranian root *xšāwan-* meaning "ruler" that you reference. Your proposed etymology doesn't appear in this Wiktionary entry. The actual etymology explicitly states the ultimate origin is "unknown," suggesting scholarly uncertainty about the deeper linguistic roots you're citing.
```


### [2026-09-06T21:28:24.886Z] TOOL RESULT

```
Web search results for query: "Afshin title Ushrusana etymology Sogdian xšēwan Old Iranian *xšāwan ruler"

Links: [{"title":"An Etymology of the Sogdian Title “Afšīn” - borderlessblogger","url":"https://borderlessblogger.com/2023/09/21/an-etymology-of-the-sogdian-title-afsin/"},{"title":"Ikhshid","url":"https://en.wikipedia.org/wiki/Ikhshid"},{"title":"Akhshunwar","url":"https://en.wikipedia.org/wiki/Akhshunwar"},{"title":"Principality of Ushrusana","url":"https://en.wikipedia.org/wiki/Principality_of_Ushrusana"},{"title":"Iranians in China - Wikipedia","url":"https://en.wikipedia.org/wiki/Iranians_in_China"},{"title":"Turgar","url":"https://en.wikipedia.org/wiki/Turgar"},{"title":"Sogdia - Wikipedia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"SOGDIANA ii. Historical Geography - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sogdiana-historical-geography/"},{"title":"Rakhanch","url":"https://en.wikipedia.org/wiki/Rakhanch"},{"title":"Afshin - Wikipedia","url":"https://en.wikipedia.org/wiki/Afshin"}]

Based on the search results, here's what I found regarding the etymology of Afshin in relation to Ushrusana:

The rulers of the Principality of Ushrusana were known by their title of Afshin.

Regarding the etymology, according to B. Gharib's Sogdian-Persian-English dictionary, the origin of Afšīn is specifically *xšaēwan containing the elements *xšay "to dominate, to rule" and -wan(ē) "doer".

It is not difficult to infer fronting in variations of *xšaēwan, including (ə)xšēwanē > axšēwan > Afšīyan. This sound change (fronting of initial /x/ to /f/) is a known phonological feature of Sogdian.

The broader context shows that the title is of Iranian origin; scholars have derived it variously from the Old Iranian root khshaeta, lit. 'shining, brilliant', or from khshāyathiya, 'ruler, king'.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T21:28:34.596Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"satrap, n\" KLN_1966.txt | head -3; echo ---; grep -o \"satrap,[^|]\\{0,700\\}\" KLN_1966.txt | head -2; echo \"=== padishah ===\"; grep -o \"padishah[^|]\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== Xerxes ===\"; grep -o \"Xerxes[^|]\\{0,400\\}\" KLN_1966.txt | head -3; echo \"=== Artaxerxes ===\"; grep -o \"Artaxerxes[^|]\\{0,400\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T21:28:36.319Z] TOOL RESULT

```
---
satrap,  shah  and  cp.  checkmate,  chess, checker,  exchequer,  Kshatriya.  Cp.  also  the  first element  in  Ahasuerus,  Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. checker,  chequer,  n.,  a  pattern  resembling  a  chess¬ board.  Shortened  fr.  OF.  eschekier  (F.  echi- quiet),  ‘chessbo
satrap,  n.,  1)  governor  in  a  province  in  ancient Persia;  2)  a  despotic  ruler.  —  ME.,  fr.  L.  satra- pes,  fr.  Gk.  e^xTpxTtvjC,  aaTpxTTTjp,  fr.  OPers. xshaftrapavan-,  ‘ruler  of  the  province’,  com¬ pounded  of  xsha&ra-,  ‘province’,  and  a  deriva¬ tive  of pd(y)-,  ‘to  guard,  protect’,  which  is  rel.  to Oil  pati,  ‘guards,  protects’.  The  first  element  is rel.  to  OPers.  xshaya-,  ‘king’,  xshayafHya-, ‘power’,  and  cogn.  with  Gk.  XTxaOxt,  ‘to  pos¬ sess’,  fr.  I.-E.  base  *qpe(i)-,  *qpei-,  ‘to  possess, rule’;  see  shah  and  cp.  check,  ‘sudden  stop’.  For the  second  element  see  food  and  cp.  words  there referred  to.
=== padishah ===
padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. che
padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referre
padishah);  influenced  in  form  by  Turkish baskak,  ‘governor’.  See  Houtsma,  The  Encyclo¬ paedia  of  Islam,  III,  1 1 14,  and  cp.  bashaw, pashalik,  also  pashalic,  n.,  the  jurisdiction  of  a pasha;  the  province  governed  by  a  pasha.  — Turk.,  fr.  pasha,  ‘pasha’,  and  -lik,  suff.  of  qual¬ ity.  See  pasha  and  cp.  the  suff.  in  beylik. pashm,  n.,  wool  obtained  from  the
=== Xerxes ===
Xerxes.  —  Heb.  Ahashwerosh  (al¬ so,  in  the  kethib  of  the  Book  of  Esther  10:1, Ahashresh),  fr.  OPers.  Xshaydrshan-  (whence also  Gk.  Eip5r
Xerxes, ahead,  adv.  and  adj.  — -  Formed  fr.  a-,  ‘on’,  and head.
Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘a
=== Artaxerxes ===
Artaxerxes,  de¬ scribed  by  Xenophon  in  his  Anabasis.  —  Gk. dvdpatru;,  ‘a  going  up,  an  expedition  up  from the  coast’,  fr.  dva(ia(vsi.v,  ‘to  go  up’,  fr.  dvx
Artaxerxes  Lon- gimanus  and  empowered  by  him  to  restore Jerusalem  and  rebuild  its  walls;  b)  the  Book  of Nehemiah,  one  of  the  books  of  the  Bible.  — Heb.  N(hemydh,  lit.  ‘the  Lord  comforts’.  For the  first  element  see  Nahum,  for  the  second  see Elijab.
```


## [2026-09-06T21:28:50.345Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Xerxes\" AHD_watkins1985.txt | head -10; echo \"=== ers ===\"; grep -n \"^ers-\\|ers-\\. *To\\|ers-1\\|ers-2\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-06T21:28:50.406Z] TOOL RESULT

```
102:The comparative study of Indo-European poetics has shown that such compounds were considered particularly apt for elevated, for- mal styles of discourse; they are a salient characteristic especially of Indo-European poetic language. In addition, it is amply clear that in Indo-European society the names of individual persons—at least in the priestly and ruling (or warrior) classes—were formed by such two-member compounds. Greek names like Sophocles, “famed for wisdom,” Celtic names like Vercingetorix, “warrior- king,” Slavic names like Wenceslas, “having greater gory,” Old Persian names like Xerxes, “ruling men,” Germanic names like Bertram, “bright raven,” are all compounds. The type goes as far back as Proto-Indo-Huropean, even if the individual names do not. English family names continue the same tradition with such types as Cartwright and Shake- speare, as do those of other languages, like Irish (O’)Toole, “‘people’s valor.”
=== ers ===
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
458:ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
459:ers-2. To be wet. Variant form *ros- in Latin rés, dew: ROSEMARY. [Pok. 2. ere-s- 336.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1150:wers-2
1156:wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
```


## [2026-09-06T21:28:59.302Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"tk[a-z]*ei-[^.]\\{0,300\\}\" AHD_watkins1985.txt | head -5; echo \"=== index SHAH ===\"; grep -o \"SHAH [a-z()é-]*\" AHD_watkins1985.txt|head -3; grep -o \"SATRAP [a-z()é-]*\" AHD_watkins1985.txt|head -3; grep -o \"CHECK[A-Z]* [a-z()é-]*\" AHD_watkins1985.txt|head -5; grep -o \"CHESS [a-z()é-]*\" AHD_watkins1985.txt|head -3"
}
```


### [2026-09-06T21:29:01.083Z] TOOL RESULT

```
tkei-
tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  s
tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
tkei-
=== index SHAH ===
SHAH poti-
SHAH tké-
SATRAP pase
CHECK tké-
CHECKMATE tké-
CHESS deuk-
```


## [2026-09-06T21:29:04.182Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"tké-\\.[^[]\\{0,700\\}\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -3; echo \"=== tkei ===\"; grep -o \"tkei-\\. *[A-Z][^[]\\{0,600\\}\\[Pok[^]]*\\]\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-06T21:29:06.257Z] TOOL RESULT

```
tké-. To gain control of, gain power over. 1. Possibly in Indo-Iranian suffixed form *ksa-tram in: a. Sanskrit ksatram, rule, power, and ksayati, he rules: KSHATRIYA; b. Old Persian khshathra-, kingdom, province, in com- pound khshathra-pava, protector of the province (see pa-): SATRAP. 2. Possibly in Indo-Iranian *ksayati, has power over, rules, in Old Persian khshayathiya-, king, whence Persian shah, king: CHECK, SHAH; CHECKMATE. [Pok. Rthé(i)- 626.]
=== tkei ===
tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.]
```


## [2026-09-06T21:29:20.445Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD p.62 ===\"; python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\nfor i,b in enumerate(t):\n    if 'شایست' in b or 'شاي' in b:\n        print('--- block',i,'---'); print(b[:1200]); \n        if i>0 and i<len(t): pass\nEOF"
}
```


### [2026-09-06T21:29:22.188Z] TOOL RESULT

```
=== FFD p.62 ===
115
--- block 66 ---
[pdf page 67]
ار فعلهای فارسی دری
سودن
سود < فارسی میانه 80 + ایرانی باستان ۴۹-12۵ برای 2 > آراست. 5 صورت
: ضعیف ريشةٌ 52۷و آن به معنی «سودن» است.
سای < فارسی میانه 537 < ایرانی باستان ۵72-:۹37*. 272 برای ساختن مادهٌ مضارع
از ريشه به کار می‌رفته است. 839 صورت بالاندةٌ 82۲ است.
ساپ, ساو, که در فارسی دری به کار رفته‌اند» بازمانده‌های 83# پهلوی اشکانی
هستند. 378[2* ایرانی باستان در فارسی میانه به صورت 37 و در پهلوی اشکانی به
صورت 7 درآمده است.
شایسترد
شایست < فارسی میانه 19ر52. 1 مادهٌ ماضی جعلی و از مادهٌ مضارع ساخته
شده است.
شای < فارسی میانه 33 < ایرانی باستان 8-ر۹83*. برای 2 -> آرای. 529« صورت
بالاندة ريشهٌ وهکدو آن به معنی «توآنابودن» است.
شتافتن
شتافت < فارسی میانه 53130» صورت کهنتر 2۳15130 + ایرانی باستان ۵01-3110 *
برای 18 -> آراست. 201 پیشوند فعلی است. ۰8130 صورت بالاندةٌ ريشهٌ ۰۶127 صورت
اصلی 131 است. 0 پیش از 1به ؟بدل شده است. ريشهٌ به معنی «فشار آوردن» است.
در فارسی میانه 55131127 به معنی «فشارآوردن» و «اشتافتن» است.
شتاب + فارسی میانه 053180» صورت کهنتر 2۳8130 + ایرانی باستان 201-8130-8*.
برای ۵ سه آرای.
شدن
شد < فارسی میانه 504 + ایرانی باستان 50-1۵*. برای 1۵ > آراست. 80 صورت
ضعیف ريشةٌ 5۵7و آن به معنی «رفتن» است.
```


## [2026-09-06T21:29:32.981Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"šāyistan[^|]\\{0,200\\}\\|šāyist[^|]\\{0,150\\}\" NYB_vol2_glossary.txt | head -5; echo \"=== NYB šahr ===\"; grep -o \"šahr[^|]\\{0,200\\}\" NYB_vol2_glossary.txt | head -5; echo \"=== NYB šāh ===\"; grep -o \"šāh [^|]\\{0,150\\}\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-06T21:29:35.179Z] TOOL RESULT

```
šāyist butan something from which no harm
šāyist ‘splendor quo nullus pulchrior esse poterat’, a *splend- our that was the most beautiful. ever existent 717-18; or the prep. is changed into an adv. 
šāyistan.— MPrs k’, where ? is only the sign of a final d : kd (cf. s. v. be), as evi- denced by the forms with enclitics: km = kä-m, ks’n = kd-šān, and by FrP 25: "MT: kk = ka; Av. (436) kat "when ?". Not to
šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the proble
šāyistan 1214-17, — The inf. serving as the complement of ~ is placed before or (commonly) after it. — Av. (551 sq.) xšay- ‘to have power’; MPrs Syd ‘it is possible’ (A-H II); MPrth šh- ‘to be able’; Paz. šāy
=== NYB šahr ===
šahr 136.
šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313;
šahr [’rthstl, inser. 'rthštr] n. pr. HajA:3. HajB:3. ŠPrs:2. 6. Prth:2. 6; 1091. 11016, hence
šahran [rthštľn'] patron. 1097.
šahr; OP Arta-xšaca-; KZŠ, Gr. v. Apta- Eeto, -Eep, -Ero (the common Gr. ’Apra- Eep&ng is influenced by HépEns); NP Ar- dašīr. Ci Bailey, BSOAS XIII, 1949, 123. Hence
=== NYB šāh ===
šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other subst
šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sa
šāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- throne
šāh the present King of Kings, Divine Khosroes 109?!, — Prth
šāh KnS V, 1). Itis of course pos- sible that ~ is ultimately derived from the national name of the Kurds, who were notorius nomad  cattle-breeders (BQ no
```


## [2026-09-06T21:29:41.972Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"Artaxšahr[^|]\\{0,600\\}\" NYB_vol2_glossary.txt | head -3"
}
```


### [2026-09-06T21:29:44.069Z] TOOL RESULT

```
647:Artaxšahr [’rthstl, inser. 'rthštr] n. pr. HajA:3. HajB:3. ŠPrs:2. 6. Prth:2. 6; 1091. 11016, hence
648:Artaxšahran [rthštľn'] patron. 1097.
763:Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epo
```


## [2026-09-06T21:29:46.401Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '640,660p' NYB_vol2_glossary.txt"
}
```


### [2026-09-06T21:29:46.442Z] TOOL RESULT

```
a-rödiSnik ['Iwdšnyk] unborn 88?. - From rustan (g. v.). Paz. substitutes azāišnī = a-zäyisnik from zätan (q. v.).
*arók Plwk'] "light, *aperture through which light passes (?) 102*. — Quite un- certain. All MSS have this reading; Dha-
www.parsianjoman.org | ool wok
*arok
bhar’s emendation: HD-wk' = évak, seems little probable. Av. (1487) ä-raok- ‘to shine’ Vd. 239,
ars ['ls] tear 9317. — MPrs "rs (Sogd. 2731); NP ars.
artži [’lt’y], artäk [*lt*k] righteous 2214, 239. 249. 128%; vāt 1 ~ the good wind (wind sent by the Righteous Powers) 717.23 Plek]. — artāi < *artāv < OP artävä, the nom. sg. of artävan-, is the genuine Prs form of the w. which appears in the religious language as ahlav (q. v.); final -v > -y is the common rule in SW. — artak is only a secondary spelling of artāi; Ps. also ’U’dy = artäi. MPrs abstr. Pyy (S) = Ps. "'lP?dyhy, v. Sogd 504 (and 31). — Artäk Virdz n. pr.: v. Viraz.
Artaxšahr [’rthstl, inser. 'rthštr] n. pr. HajA:3. HajB:3. ŠPrs:2. 6. Prth:2. 6; 1091. 11016, hence
Artaxšahran [rthštľn'] patron. 1097.
ArtaxSér ['Ithšdl] = Artaxsahr, 1-17, passim. 117°. 1201-2 (v. also nev-— and Véh-—), Artašēr [ltšdl] 11571. 116? sq. — Olr Arta-xsadra-, cf s. v. Art-vahist and šahr; OP Arta-xšaca-; KZŠ, Gr. v. Apta- Eeto, -Eep, -Ero (the common Gr. ’Apra- Eep&ng is influenced by HépEns); NP Ar- dašīr. Ci Bailey, BSOAS XIII, 1949, 123. Hence
Artaxšērān [’lthsdl’n'] 1413. 1512-17, Arta- šērān [*ltšdl*n'] 114-116, patron.
artēštār ['Ityšt'l] warrior; 4517 ~-éh = 7-6 with -yh for the indef. art. -ē; pl. cas. rect. ~ 28. 6617; pl. cas. obl. —-än 168. 119%, — Borrowed and remodelled (cf below artik) from Av. (1506) radač-štar- ‘he who stands on the chariot’ (ef s. v. rahy); Paz. pl. cas. obl. ar(a)tištārg (Mx).
arteštirčh the warrior class 5519; on 4517 v. above.
artik ['1tyk] war 121%, — MPrs ’rdyg (S, A-H I); Paz. ardi (SGV).
aržanik
Art-vahišt [?rtwhšt'] 402; Urt-vahiSt Pwrtwhst'] 39%,  A&a-vahist [?šwhšt'] 394-5, 401-4, 589. 593, 9727 one of the Amahraspands (g.v.). — art, urt < OlrSkr rta- ‘the right cosmic order, the divine law’, Av. (192) arata-, (349) orota-, (229 sqq.) aša- + vahista- (v. vahišt) 'the best, the heavenly law'. Asa-vahist is directly borrowed from Av. (233 sgg.); also the name of the 2nd month of the year and the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. Cf ahlav, ahläi, artči; Arta-xšahr "he whose dominion is (de- termined) by the divine law’.
arvand [lwnd] swift 228. — Av. (200) aurvant-.
Arvand-üsp [~-’sp'] n. pr. 1175, — Av. (200) Aurvat-aspa-.
arvandéh valour, gallantry 55’.
arvēs [Iwys] rope 15%’. — MPrs *w<ys>, Sogd. 2732; NP arves ‘a hair rope’; from Av. (1533 sq.) urvaés- ‘to turn, to twist’, MPrth pres. ?rws- (= arvis-) ‘to turn towards .. ” (A-H III); Ghilain 49.
Aryan (Prth) Pry’n] = Erän (v. Er),
```


## [2026-09-06T21:29:56.314Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"افشین\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null; echo \"=== ARY headwords ===\"; grep -n \"شهریور\\|ساتراپ\\|افشین\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY shah ===\"; grep -n \"SHAH\\|XSHAYA\\|KSEI\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T21:29:56.407Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
MON_part1.txt:0
MON_part2.txt:0
=== ARY headwords ===
=== ARY shah ===
1012:(PATIXSHAYATHIYA 3, gah, PATCAX: gl
4229:POWER ENGLISH) goSSi PADIXSHAYA-, PATI-
6119:POKORNY = SSSSC*« AYU, AYUSHAH (SANSKRIT) cy Sib.
8265:DEDEIKHELOS, AGREEK) gly DAOZHAHVA, DVAESH-, DVAESHAH-
8266:DEIDEMON, DEIMOS, DEILOS DUSHAHU <(OLD PERSIAN) inl .go\
9058:| AMIDDLE HIGH GERMAN) sly laJ’ °- RAESHYEITI, RAESHAH
10733:OLD CHURCH SLAVIC) 9 59! SHAH, SHAX BALUCHD) ges
10839:GREEK) (gli XSHAYATI, XSHAYO, XSHI-
10843:‘REFERENCES cath SHAH, SHATHR — (PAHLAVI) 5
10845:PoKORM t™C*~=<CS~s*~‘CSs*~*«S SHAH, PADSHAH (KURDISH) 53,6
```


## [2026-09-06T21:29:59.216Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10830,10870p' incoming/ARY/ARY_latin_index_pages.txt; echo \"#### find pdf page tag\"; awk 'NR>=10800 && NR<=10870 && /pdf page/' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-06T21:30:00.979Z] TOOL RESULT

```
eA dS 9 GSE 3 Hig SSS abel ee Als cal glial a te Gok) ate 2 F

5 ebeloat Se lng a dls hla e025 ads 04F le Ase!

RG meee |

KSI, KSAYATI, KSATRA MAVESTAN) gla s!

GREEK) (gli XSHAYATI, XSHAYO, XSHI-
KHTAOMAL, KHTENA (OLD PERSIAN) sleet, go),
KSHATHRA,, XSHAYTHIYA,

‘REFERENCES cath SHAH, SHATHR — (PAHLAVI) 5

PoKORM t™C*~=<CS~s*~‘CSs*~*«S SHAH, PADSHAH (KURDISH) 53,6

‘MACKENZIE: (KING) 120 SHAH HBALUCHI) gs)

| BUCK: (RULE) 1319-1321, HAFGHAND) (5-4) gli)

(KING) 1321-1322 PACHA, PACHAH, CHAH

id) ebb oly SANSKRIT) 4 S—ile

deatlaa

Sead 6 pid Dae lig 9 ESS 9 05s gel

[MOR tenor |

XSHAP, XSHAPAN  :(AVESTAN) ls!

‘REFERENCES cathe XSHAP «(OLD PERSIAN) kal, go J)

POKORNY, =OSOs=~=“C=*i‘SC‘SRD SHAB, SHAWAX —_{PAHLAVD) 14

DELAMARRE: 195 ‘AxsAW AOSSETIC) gay)

MACKENZIE: (NIGHT) 125 SHEW KURDISH) (52,6
BUCK: 992 SHAP ABALUCHD) gr se ;
#### find pdf page tag
[pdf page 373]
```


## [2026-09-06T21:30:10.964Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Av. xšayeiti\\|xsayeiti\\|OPers. xšāyaθiya\\|xsayathiya\\|Skt. ksatra\\|ksatra-\" SYN.txt | head -10; echo \"=== IEC ===\"; grep -n \"kþē\\|ksatra\\|ksayati\" IEC.txt | head -10"
}
```


### [2026-09-06T21:30:11.031Z] TOOL RESULT

```
1711:4. Other Skt. words besides star-, tara-, are mostly such as are applied to any heavenly body, as bha- fr. bha- ‘shine’, jyotis- fr. jyut- ‘shine’, naksatra- of obscure orig.
33138:power, rule’ (with sbs. Skt. ksatra-, Av. zsabra-, OPers. xsa6"a- ‘rule, realm’, Av. Saya- ‘ruler, king’, OPers. sxéaya-
=== IEC ===
```


## [2026-09-06T21:30:13.127Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33125,33160p' SYN.txt"
}
```


### [2026-09-06T21:30:13.190Z] TOOL RESULT

```
OE reccan mostly ‘tell, narrate’, but also ‘rule’ (Bosworth-Toller s.v. vii) : Lat. regere ‘direct, rule’, etc. (above, 2).
ME reule, NE rule, fr. OFr. reuler, fr. Lat. régulare ‘regulate’, fr. régula ‘rule’ : regere (above, 2).
ME, NE govern, fr. Fr. gowverner (above, 2).
OHG hérison, hérreson, MHG hersen, herschen, NHG herrschen (MLG her- schen > Dan. herske, Sw. herska), fr. OHG héro, hérro, NHG herr ‘master’ (19.41). Falk-Torp 401. Weigand-H. 1.855. Kluge-G. 247.
MHG, NHG regieren, Du. regeeren, fr. Fr. régir, Lat. regere (above, 2).
5. Lith. valdyti, Lett. valdit, ChSl. vlastt, vladq, SCr. vladati, Boh. vlddnouti, Pol. wtadaé (Russ. vladet’ mostly ‘pos- sess, own’) : Goth. waldan, etc. (above, 4). As loanwords fr. Gmc. Stender- Petersen 213 ff.
Lith. viespatauti, fr. vieXpatis ‘ruler, Lord’ (19.41). For current use, cf. Fraenkel, Z. sl. Ph. 6.90.
Pol. rzqdzié, fr. sb. rzqd ‘order, row’ and ‘rule’ = ChSI. redii, Boh. fad ‘order, arrangement, regulation’ : Lith. rinda ‘row, rank’, prob. Lat. ordd ‘row, order’, ete. Briickner 474. Walde-P. 1.75, 2.368.
Russ. pravit’ = ChSl. praviti ‘guide’, fr. pravi ‘straight’ (12.73).
6. Skt. ¢a@s- ‘command’ (18.45) and ‘rule’.
Skt. /si- ‘possess, rule’, Av. 27- ‘have
Digitized by Arya Samaj Foundation Chennai and eGangotri
SOCIAL RE
power, rule’ (with sbs. Skt. ksatra-, Av. zsabra-, OPers. xsa6"a- ‘rule, realm’, Av. Saya- ‘ruler, king’, OPers. sxéaya-
LATIONS 1321
Oiya- ‘king’) : Grk. xréouac ‘possess’. Walde-P. 1.405. Barth. 550, 551, 553. Skt. z¢- ‘own’ (11.12), also ‘rule’.
19.32 KING
Grk.  Bacvdebs (vat poet.), Goth. piudans Lith. karalius
Byz. pnt ON konungr, bjddann Lett. karalis, k'énin’’ NG  Baotdebs, pop. Dan.  konge ChSl.  césar’t, kral’t
Baotdtas Sw. konung SCr. kralj Lat. rex OE cyning, péoden Boh. krdl It. re ME kyng Pol. krél Fr. Tot NE king Russ. korol’ Sp. rey Du. koning Skt. rdjan-, raj- Rum. rege OHG  kuni(n)g Av. xsaya-, OPers. Tr. rt MHG kunec xsayabiya- NIr. 7% NHG kénig W. brenin, teyrn Br. roue
The title of ‘king’ has been, in the course of history, applied not only to the rulers of independent states, even great empires (before the rise of a superior title ‘emperor’, 19.34), but also to the petty chiefs of tribes or clans. Cf. NED s.v. king.
1. IE *rég-, fr. the root *reg- in Lat. regere ‘direct, guide, rule’, etc. (19.31) Walde-P. 2.362 ff. Ernout-M. 864.
Lat. réx, gen. régis (> the Romance words; but Rum. rege modern; older cratu, fr. Slavic kral’t); Gall. -rix in Dumno-riz, etc., Ir. ri, gen. rig (W. rhi arch. ‘lord, nobleman’), OCorn. ruy, Br. roue, MBr. roe (Pedersen 1.51; or Br. forms fr. Fr. roi ?); Skt. (Vedic) raj-, but commonly n-stem rajan-; cf. Goth. reiks ‘ruler’, loanword fr, Celtic.
2, Grk. Baothebs, NG pop. Baodrds, without etym. (connection with ads people’ impossible) and prob. of pre- Greek origin. Boisacq 115f. Wacker- nagel, Sprachl. Untersuch. zu Homer 212, Kretschmer, Glotta 10.222. Wie- ewiez, Hos 31.526 ff.
Grk. ayat, dial. favat, poet. word often applied to kings but also to gods and heroes, ‘lord, master’ (for Hom. use
of avat vs. Baoidebs, cf. Wackernagel, op. cit. 209 ff.), possibly : Skt. van- ‘win, gain’, etc. (Schwyzer, Glotta 6.86), but more prob. of pre-Greek origin. Cuny, Rev. ét. anc. 16.297. Debrunner in Ebert, Reallex. 4.2.527. Smieszek, Eos 31.547 ff.
In Byzantine times Bactdebs was ‘em- peror’, the regular title of the Roman emperor and the Persian ‘king of kings’ (19.34). For ‘king’ Lat. réx was adopted, e.g. pnt TorOwv, pre dpayxwv, etc. Theo- phanes (1.472f. DeBoor) notes the crowning of Charlemagne, s7£ trav dpay- Kwy, &S Bactdeds ‘Pwyaiwy. But generally the German emperors were not accord- ing the emperor title by the Byzantine court. NG pias ‘king’ in cards.
3. W. brenin : W. bry ‘high’, Ir. bri, W. bre ‘hill’, Skt. brhant- ‘great, high’ (cf. fem. brhatt-, Ir. Brigit ‘the exalted one’), Av. barazant- ‘high’, ete. Walde-P. 2.173. Pedersen 1.100.
W. teyrn ‘ruler, king. : Ir. tigerne ‘master, lord’ (19.41). Here also W. mechdeyrn, OBr. machtiern (‘tributary prince’), OCorn. mychtern (reg. word for ‘king’, Williams Lex. 260), epd. with word seen in Ir. mac, W. mach ‘bond
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
?
1322
surety’. Loth, L’&migration bretonne en Armorique 218 ff., Voc. vieux-bret. 182. Thurneysen Z. celt Ph. 19.130. Otherwise (but to be rejected) Pedersen 1.137 and Ifor Williams, BBCS 10.39 ff.
4, Goth. piudans, ON pjddann, OF péoden, derivs. of Goth. biuda, ON )jo0, OE féod ‘people, nation’ (19.22).
ON konungr, OF cyning, etc. (with short forms OF cyng, etc.), general Gmc. except Goth. : Goth. kunz, OE cyn, etc. ‘family, race’ (NE kin), but prob. more directly as patronymic of ON konr ‘man of noble birth’, OF cyne-, OHG kuni- in epds., hence orig. ‘descendant of one of noble birth’. Falk-Torp 563. Weigand- H. 1.1108. NED s.v. king.
5. Lith. karalius (> Lett. karalis), fr. the Slavic (below, 6). Brickner, SI. Fremdwéorter 90. Miihl.-Endz. 2.160.
```


## [2026-09-06T21:30:22.162Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\ni=t.find('[pdf page')\nprint(t[:200])\nEOF\ngrep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3"
}
```


### [2026-09-06T21:30:23.778Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D
```


## [2026-09-06T21:30:27.761Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# find the leaf containing \"405\" page marker near ks- roots\nimport re\nfor i,b in enumerate(t):\n    if 'ksayati' in b or 'kṣáyati' in b or 'ksatra' in b.lower():\n        print('---',i,'---'); print(b[:1800]); print()\nEOF"
}
```


### [2026-09-06T21:30:29.514Z] TOOL RESULT

```
leaves 895
--- 31 ---
                                                                  aueg-, aug-, ug-                                                            23

ckan „vermehrt, schwanger“ (aber                                                 trotz     Schroder Ablautst. 58 nicht bair.
iciech „iippig“ als redupl. *(e)u-eu(e)L-), lit. augu, dugti „wachse“, auginii, -mti
„wachsen                               „heranwachsen“, iigis „Wuchs. Jahres-
                   lassen, erziehen”, pa-ugeti
wuchs“,              audzindt „aufziehen“, apr. auginnons ppa. „gezogen“
                 lett.       atidzel,
(usw., s. Leskien Abl. 313 f.), alett. aukts „hoch“ = lat. audits, lett. aiigt
„wachsen“, wie auch apr. aucktai- ri kijskan „Obrigkeit“, aucktimmien „Yor-
steher“, woneben mit dem s des -es-St. (s. u.) lit. attkstas      lett. atigsts „hoch“                                ,




(:   lat.   auqustus „erhaben“), apr. auck-stimiskan fem. (acc.) „Obrigkeit“ (s. bes.
Bezzenberger BB. 23, 295), apr. augus „geizig“                                                      (als       „mehrend“),           lit.   dugu-
vias, lett. aug tons „Wachstum“;
     ai.    ugra- „gewaltig“ (Komp. Sup. ojiyas-, djiitha- „der kraftige, kraftigste“)
= av. ugra- „stark, kraftig                               11
                                                               (komp. Sup. aojyah-,                  aojista-).

     es-St. ai. ojas- n. „Kraft, Starke“, av. aojah-, aogah- (ebenso r-St. aogard)
                              :!
„Kraft, Starke                     ,
                                        lat.       augustus s. o. (ebenso                    lit.   usw. aukstas)             ;
                                                                                                                           

--- 512 ---
504                                                          kpei            qpep)-, qpe i)-


     DaB mit Anlaut k[s]u- auch ags. hwilpe „ein schreiender Meervogel",
ndl.  wulp ,.Regenpfeifer“, nd. {reycn- wilp, ivalp, wolp ds verwandt seien    )




(-p
    - aus -pp- aus -jm-h, ist ein schwanke Konstruktion; wohl zu aisl.
hvellr ,.gellend" usw. (s. qkeZ).


kpei-        ,,siedeln, sich                ansiedeln, eine Niederlassung griinden".
     Ai. kheti, kbiyati ,,weilt, wohnt”, av. saeiti ds..                                            ai. ksiti-,              av. iiti- „Wohn-
platz,       Siedelung”,                ai.       ksetra -,         av. soidr'- n. ,,Grundbesitz, \Yohnplatz“, ai.
kitma- m. ,.ruhiges Verweilen";
  arm. (Hiibschmann StraBburger Festschrift 1901, 70 f.              bUn, Gen sini                                       !




..bewohnt. bebaut, bliihend, Dorf, Weiler” (vgl.bes.gr, y.xoivu)\
  gr. y.xpm ,,grflnde‘‘, evy.xif.ievog ..wohl gebaut (Haus, Stadt', wohl an-
gebaut, bestellt (Land/      ex-y.xtxog ds., TxsQixxiovsg, jzEgiy.ztzcu ,.Umwohner,
                                                    -
                                                        ,



Nachbarn". auq ly.rioveg .,herumwohnende‘' (zur Form apcpiy.xvovsg Lit. bei
Boisacq 525 Anm. 2        y.xLoig  ,,Anbauung, Ansiedelung“, y.xoiva iRhodos,
                                              ,



Karpathos) „\Vohnsitz, Gemeindebezirk”, auch y.xiXog „ruhig, still'' (eigentl.
„an die Siedelung gebannt, gezakmt" nach Osthoff, Patrubany’S Sprachw.
Abh. II 72 ff., 30 f. Par. I 68; nicht zu lat silco nach Froehde BB. 21, 329,
                         1




Brugmann I 2 791                        —
                        aber nicht mehr IF. 17, 320             Bechtel Lexil 206,     

--- 846 ---
S38                                                          dhey-


widerwartig, ekelhaft, scheuBlich" als „infolge des Geruches widerwartig“
(s. auch u. *bhoidho-) aus *ftddos auf Grand eines Adj. *fuios.

     Anord. dyja „schfitteln“                 (s. o.).

   Got. dauns „Geruch, Dunst", anord. daunn „Gestank“ (vgl. alb. dej fiber                                     ;


ahd. nbd. dunst s. unter der Wzf. *dheues); anord. dunn m. „Daune
(daraus mnd. dune, wo von wieder nhd. Daune; vgl. mndl. donst „Daunen,
Staubmehl“ — dt. Dunst; s. Falk-Torp u. dun); as. dununga „deliramen-
tum“ (a oder (it Holthausen KZ. 47, 310).
    Lit. duja „Staubchen“, duje „Daune“ (aber pridvejas „dumpfig“ ist
Lesefehler, siehe Berneker 236; Persson Beitr. 743 stellt lit. dvylas
,, schwarz, schwarzkopfig, vom Rinde“ unter einer Wzf. *dhu-ei- hierher,
die mir aber nicht feststeht; vielleicht aus *dujilas und naher zu duje                                            ,


duja als „staubfarben“; gegen Yerbindung mit lat. Mlis „Galle“ unter *du-
tlo,      W. Meyer KZ. 28, 169, spricht cymr.                            I   mstl „Galle“,   s.   *bistlo-).
     Slav, duja, duti              (z.   B. russ. duju, dutb) ,,blasen. wehen“, ablautend *dyjq
in sloven, dijcm, f7t7i„wehen, duften, leise atmen“; aksl. dunn dunqti „blasen“
(ablautend mit    ai. dhu-noti, - nati gr. dvvco; s. Berneker 236, von der
                                                         ,


Osten-Sacken IF. 33, 214).
   Alles Wesentliche bei Curtius 5 258, vgl. noch Fick I 4 75, 245, 465,
III 4 206 f., Osthoff MU. 4, 23 f., Schulze Qu. ep. 312 ff., Hirt Abl. 104,
Reichelt KZ. 39, 71, Persson Wzerw. bes. 55f., 81 f., Beitr. 652f. (usw.)
743 f., Berneker 236 f. Ygl. noch das vielleicht ursprungsgleiche *dheu-
„laufen,            ri
```


## [2026-09-06T21:30:33.165Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[513][:2200])\nEOF"
}
```


### [2026-09-06T21:30:34.839Z] TOOL RESULT

```
                                          i                                                             :                                                     ;




                                                                 qpen-            — q”hpei-                                                              505

Kretschmer aaO.; Yermittlung mit der Sippe von na/ia, gxdoaodai                                                                                         siehe
lieu- „schwellen“) ist unmoglich trotz J. Schmidt PI. 41 1 ff. (xxij-                                                                    :    *txjx&-   nach
dem Yokal geregelt) und Hirt IF. 17, 390 (qpuc-, woraus qpe- und quP-\
aber ixa/ua hat n- aus Am-!).                                      Fern bleibt gr. icppifiog „machtig, gewaltig,
edel“           BB. IS, 226 f.; scheitert am Labiovelar, der dann wegen
             (Collitz
ixp&ijuog der Wz. zuzuteilen ware; mit Schmidts obiger Lehre nicht glaub-
lich so zu verbinden,                         daB man an /?- aus g“ vor                                         i,      z.   B. in fttog      ,
                                                                                                                                                  erinnert)
ebenso lat. satelles                    (s.   Yf. LEWb.'2                     s. v.).



q|)en- ,,verletzen, toten“.
  Ai. ksandti „verletzt, verwundet“ (die weM-Bildung spatatt. xxetvvpu xxeov-                                                                       ,



w/u xxivvvf.u hat damit keinen geschichtlichen Zusammenhang. s. Brug-
mann II' 3. 328), aor. ksanisthah, Ptc. ksata „verletzt, vernichtet, zerstort“,
                 2



aksata- ,,unverletzt = ap. axsata- „unverletzt“
                    <;



   Gr. xxeivo) (xxevcb, xaxexxova, sxxaxo. xxdptevog) „toten“, avdQoxxaob]
,,Mannermorden“, naxQoxxovog „Vatermorder“; xaxaxaivaj, xaxexavov mit
diss. r-Schwunde gegen das x der Praep., wonach dichterisch auch ein
Simplex xaivco xexova (Kieckers IF. 36, 233 f. also nicht idg. Wechsel
                                 ,                                                                          ;
```


## [2026-09-06T21:30:42.910Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[512][1500:4500])\nEOF"
}
```


### [2026-09-06T21:30:44.522Z] TOOL RESULT

```
iedelung gebannt, gezakmt" nach Osthoff, Patrubany’S Sprachw.
Abh. II 72 ff., 30 f. Par. I 68; nicht zu lat silco nach Froehde BB. 21, 329,
                         1




Brugmann I 2 791                        —
                        aber nicht mehr IF. 17, 320             Bechtel Lexil 206,                          —   ,


s.   iiber dieses u. **ei ,.entsenden, los-, nachlassen”);
      lat.   situs   ..gegriindet                           (urhs       a Philippa         sita),       gelegen.              wohnend”               zu-
sammengeflossen mit situs „stehngelassen; beigesetzt, von Toten‘ das samt                                                          :




sirw, 2)ono ))Ositus zu *sei- .,entsenden”, s. d.; situs in alien seinen Bedd.
mit OsthotF aaO letzterer Sippe zuzuweisen, verwehrt vor allem die Bed.
     gegriindet").
  Vgl. Froehde BB. 1, 198, Collitz BB. 18, 214, Kretschmer KZ. 31,429,
Brugmann I'2 675, 790, Yf. LEWb. 2 u. sittis.
      Ahd.     Si-dal,       as.    sethal                  „Sitz, Wohnsitz“, ahd. sidilo agricola''                                   s.   u.       sed-
,,sitzen"       idg. *sc[d]-tlo-,                           de Saussure Msl 6, 246ff. ).
      Lit.   szrimyna, abg. sctnija „Gcsinde a s. u. kei- „liegen‘‘.


qpe ij-, qpa(i - „erwerben, Verfiigung und Gewalt woriiber bekommen”'.
      Ai. ksuyati „besitzt, herrscht' [*qpoi-eti)
                                                                    1
                                                                                         = av. xsayeiti „hat Macht, Gewalt,
herrscht,        verfiigt               woriiber,                  besitzt",       ai.    ksatra- n. „Herrschaft“,                          av.       ap.
av a&ra- n. ,.Herrschaft, Reich  Herrschergewalt" urar. Neubildung zu ksuyati,
                                                               ;




indem dessen y als Praesenssuffix gefiihlt wurde, Kretschmer KZ. 31, 430f.
auch der Typus datrd- n. .,Gabe“, idg. *d-e-trom zu do-, wirkte mit ap.                                                                          ,


xmyadiyn- „im Besitz der lie rrsche rge wait        s. dazu Bartholomae Airan.
                                                                                             "'




\Yb. 553 f. m. Lit.    Xsayurban „Xerxes
                                    ,                                               ".


   Gr. y.xdouau „crwerbe‘ = kinynti), Pf. xexttj/icu „besitze“, xxeavov (vvolil
diss aus ’y.xd-avov, und erleichtert durch eine Flexion y.xaexat       *y,zeopai                                                       :




aus y.raoiiai) „ Besitz, Eigentum, Vermogen“, y.xeag, Dat. PI. y.redxEooiv ds.,
y.xijfiu ..Erwerb. Besitz, Eigentum", y.xfjvog n.. PI. .Besitz, Vermogen, auch                          ,


bes. an Herden        Sg. ,.das einzelne Stuck Yieh
                               ",                        mit demselben Anlaut-                      "
```


## [2026-09-06T21:30:51.882Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"Scheck[^|]\\{0,400\\}\" LKT.txt | head -4; echo \"=== Schach ===\"; grep -o \"Schach[^|]\\{0,500\\}\" LKT.txt | head -4; echo \"=== sakk ===\"; grep -o \"[sS]akk[^|]\\{0,300\\}\" LKT.txt | head -5"
}
```


### [2026-09-06T21:30:53.985Z] TOOL RESULT

```
Schecke'];  hieraus  sp.  barajado, pg.  baralho  'bunt'  und  als  Verb  sp.
Scheck.  Vgl.  noch  frz.  dchec  'Miß- erfolg, Schlappe'.  —  [Das  Wort  Schach suchte  als  urgermanisch  zu  erweisen M.  MAY  in  Zeitschrift  des  Dtsch.  Allg. Sprachvereins  (1895)  X:  Entgegnung. Zum  5.  Hefte.  S.  1/4  ]  [DE  352.  Eguilaz 391.  Kluge  4.  382.  ML  7669.  Gor- jajew  419.
Scheck  1762 Scheich  1775 Schellack  1295 «■cAer/f  1852 Schibbolet  1891 schicker  ].  1787  b Schicksei' j.  1789 Schikane  434 Schin(hiindchen )  420 Schlamastik  j.  1920 Schlammassel  j.  1920 SfA/t«/'  j.  1804 Schlemiel  1882 Schlemihl  1882 Schlimasdlnik  j.  1920 Schlimasel  j.  1920 Schmuck  1946 Schmiere  (stehen)  j.  1813 Schmu  (machen)  j.  1884 .Sc/if/i?iZ  j.  1811 ÄcÄ»«««  j.  1884 sc
=== Schach ===
Schachspiel)'  [vgl.  jedoch hier  Nr.  605],  frz.  alfier  'Fahnenträger'; russ.  faris,  poln.  farys  'Beduinenhäupt- ling', serb.  (alt  und  selten)  fariz  'Pferd' [über  mgr.  qpdprii;];  mhd.  väris,  färis 'Roß'.  [DE  113.  Devic  DEt  17.  ML 3199.  Gorjajew391.  Bern  SlEtWb  279. Karlowicz  421.
Schach  neben  dem König  [säh  s.  hier  Nr.  1762]  nicht  die Königin,  sondern  der  Wesir  die  Haupt- figur war,  wurde  hieraus  afrz.  ferce, fierge,  nfrz.  vierge  [mit  volksetymolo- gischer Umdeutung  zur  „Dame"],  prov. fersa  ;  bulg.  serb.  ferz,  russ.  ferz'  'Dame oder  Königin  (im  Schachspiel)'.  [Mikl SlEtWb  58a.  Bern  SlEtWb  280/281. ML  3266.
Schachfigur  mit alfäris^sp.  alferez  usw.  [s.  hier  Nr.  591] vermengt  worden  [vgl.  ähnlich  russ. usw.  slon  'Elefant'  und  'Läufer  im Schachspiel',  MSISI  774/775];  die  Folge hiervon  war  eine  Änderung  in  der  Auf- fassung der  betr.  Figur:  der  Kriegselefant wurde  zum  Fahnenträger,  Läufer,  frz. sogar  durch  volksetymologische  Um- deutung  zum  Hofnarren  [die  somit  frei- gewordene Rolle  des  Elefanten  wurde auf  den  Turm  übertragen].  Im  einzel- nen ist  it.  alfido,
Schachspiel  im  kai- serlichen Schatz  zu  Nürnberg  enthält noch  Elefanten!]  [DE  113/114  u.  302. Eguilaz  167.  ML  3291.  Bern  SIEtWb 281.
=== sakk ===
sakkcV  in  einem  über den  Rücken  gelegten  Ziegenfell  trägt. [Hobson-Jobson  92.
sakku  'Sack; Büßergewand',  ZAkkFW  67];  hieraus gr.  adKKO«;,  lat.  Saccus  und  die  roman. Formen  it.  sacco,  sard.  saccu,  prov.  frz. kat.  sac,  sp.  saco,  pg.  sacco,  rum.  sac; engl,  sack,  ndl.  zak,  dtsch.  Sack,  dem. engl,  satchel.  dtsch.  Säckel  'Geldbeutel'; russ.  sak  'Erds
sakkos, bulg.  serb.  saA-os  'Pluviale,  Oberkleid  der Bischöfe'.  In  fig.  Bedeutung  wird  sp. saqiiear,  it.  saccheggiare,  frz.  sacrager 'plündern';  dtsch.  Sackmann  'Räuber' [vgl.  die  gefürchteten  Straßenräuber Konstantinopels,  ciaraldar,  d.  h.  'Sack- männer', die  ihre  Opfer  in  Sä
sakka 'spalten'],  'einseitiges  Kopfweh';  hieraus sp.  jaqueca,  pg.  xaqueca,  enxaqueca 'dass.,  Migräne'.  [DE  217.  Eguilaz  512. ML  7673.
sakk:
```


## [2026-09-06T21:30:57.548Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"sakk:[^|]\\{0,700\\}\" LKT.txt | head -3; echo \"=== 1762 säh ===\"; grep -o \"1762[^|]\\{0,900\\}\" LKT.txt | head -3"
}
```


### [2026-09-06T21:30:59.412Z] TOOL RESULT

```
sakk:
=== 1762 säh ===
1762]  nicht  die Königin,  sondern  der  Wesir  die  Haupt- figur war,  wurde  hieraus  afrz.  ferce, fierge,  nfrz.  vierge  [mit  volksetymolo- gischer Umdeutung  zur  „Dame"],  prov. fersa  ;  bulg.  serb.  ferz,  russ.  ferz'  'Dame oder  Königin  (im  Schachspiel)'.  [Mikl SlEtWb  58a.  Bern  SlEtWb  280/281. ML  3266.
1762,  also  eigentlich  'Beschülzer- Konig'],  Titel,  der  dem  Sultan  der  Türkei zukam:  tk.  padysah;  hieraus  rum.  pa- di§ah,  padifach;  dtsch.  Padischa,  poln. padyszach  usw.
1762,  also  wörtlich 'der  königliche'  sc.  Vogel],  ebenso  tk.; hieraus  bulg.  sahin  'Falke';  rum.  §oim 'dass.',  fig.  'kühner  Mensch'.
```


## [2026-09-06T21:31:03.129Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"1762\\. *[^|]\\{0,900\\}\\|1762 *säh[^|]\\{0,900\\}\" LKT.txt | head -3; echo \"===\"; grep -no \"np\\. *säh *'König'[^|]\\{0,800\\}\" LKT.txt | head -3; echo \"=== sakk entry ===\"; grep -n \"sakk:\" LKT.txt | head; "
}
```


### [2026-09-06T21:31:06.287Z] TOOL RESULT

```
ugrep: error: error at position 633
0-\xbf]|\xf4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,900}
                        exceeds complexity limits___/


===
=== sakk entry ===
4071:1795.  Ar.  sakk:
```


## [2026-09-06T21:31:09.404Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4065,4085p' LKT.txt; echo \"#### 1762\"; grep -n \"^1762\\.\\|1762\\. *Np\\|1762\\. *Pers\" LKT.txt | head; grep -n \"1762\" LKT.txt | head -20"
}
```


### [2026-09-06T21:31:09.479Z] TOOL RESULT

```
1792.  Ar.  sakika:
'Eine  Seite  des  Kopfes'  [vom  Vb.  sakka 'spalten'],  'einseitiges  Kopfweh';  hieraus sp.  jaqueca,  pg.  xaqueca,  enxaqueca 'dass.,  Migräne'.  [DE  217.  Eguilaz  512. ML  7673.
1793.  Ar.  sakima:
'Halfter' ;  hieraas  sp.  jäquima,  pg.  xd- quema  [Constancio  Dicc  974a]  'dass.'. [DE  353.    Eguilaz  512.
1794.  Pers.  säkirlät:
'Mit  Kermes  oder  Cochenille  rot  gefärbtes Kleid'  [aus  ar.  siklät  >  dtsch.  Siklat, 'schwerer  farbiger  Seidenstoö',  das  selbst aus  lat.  cyclas.  gr.  KUKXdi;  stammt], hieraus  mlat.  scarlatum  'Scharlach  als Stoß',  it.  scarlatto,  afrz.  escarlate,  nfrz. icarlate,  sp.  pg.  escarlata ;  engl,  scarlet, mhd.  scharlät,  ndl.  scharlaken  [mit  An- lehnung an  laken  'Tuch'],  dtsch.  Schar- lach; das  letztere  Wort  auch  zur  Be- zeichnung einer  Krankheit,  ebenso  frz. fihre  scarlatine,  russ.  skarlatina,  poln. szkarlatyna,  cech.  Sarlatina.  [Eguilaz 391.    ML  7661.    Gorjajew  322.
1795.  Ar.  sakk:
'Zweifel,  Schwierigkeit',  vulg.  mit  Art. es-sekk;  hieraus  sp.  (alt)  enjeco,  pg.  en- xeco  'Schwierigkeit,  Schaden,  Strafe'. [DE  261.    Eguilaz  390.    ML  7686.
1796.  Ar.  sakkä': 'Wasserträger',  ebenso  tk.  ['der  gegen Lohn  Wasser  transportiert'  im  Gegen- satze zum  sugu,  sngy  'der  auf  eigene Rechnung  mit  Wasser  hausieren  geht', vgl.  MO  XVII,  142,  Nr.  7];  hieraus  mit ar.  Art.  sp.  azacdn  'Wasserträger;  Ecken- steher' [Dicc  Gast  295bl,  pg.  oQacal 'Wasserträger  und  -Verkäufer';  rum. saca  'Wasserkarren,  -faß  der  Wasser-
143
[Ar.  sakkat.
träger',  sacagiu  'Wasserträger'].  [DE 221/222.  Eguilaz315.  Löbel  EITAP  79.
1797.  Ar.  sakkät:
'Althändler,  Trödler';  aus  sük  as- »akkätln  'Markt  der  Trödler'  wurde  sp. zacatin  'Plätzchen  oder  Straße,  wo  Tröd- ler wohnen',  'kleiner  Platz',  siz.  zügatu 'Delikatessenhandlung;  Ort  von  zweifel- haftem Rufe'.  [DE  356/358.  Eguilaz 517.    GrSVodSic  250.
1798.  Tk.  saklii:
[Vom  Stamme  jak,  sak  'recht,  wach; wach  sein,  beobachten,  hüten'  Vämbery TktEtWb  S.  1 1 1,  Nr.  122],  Infin.  saklamak 'verbergen,  bewahren,  schützen';  hieraus russ.  saklja  'Hütte  der  Bewohner  im Kaukasus'.
1799.  Ar.  sakr:
'Jagdfalke  Falco  sacer';  hieraus  mlat. sacer  [die  Form  dieses  Wortes  ist  viel- leicht in  Anlehnung  an  gr.  lepal  <^  iepö? gewählt  worden],  mgr.  odKpe,  kat.  sp. pg.  sacre,  frz.  sacre,  it.  sncro,  pg.  gafaro 'Falke';  dtsch.  Sackerfalk,  engl,  saker, sacre;  russ.  sokol,  klruss.  poln.  sokol, öech.  sokol,  serb.  soko,  bulg.  soA-o^  'Falke'. —  Die  Jagd  mit  Falken  erlebte  im  MA im  feudalen  Europa  eine  hohe  Blüte, schrieb  doch  FRIEDRICH  II.  sogar  ein Buch  de  arte  venandi  cum  avibus.  Von Deutschland  und  Byzanz  verbreitete  sich dieser  Sport  zunächst  in  das  östliche Europa  und  dann  bei  den  Völkern  Asiens, bes.  an  den  mittelasiatischen  Höfen  und bei  den  Nomaden  der  Steppe  und  den Beduinen  der  Wüste.  Bei  den  letzteren ist  sie  in  manchen  Gegenden  noch heutigen  Tages  eine  eifrig  betriebene Beschäftigung.  [DE  33S.  Eguilaz  488. Suohlati,  Die  dtsch.  Vogelnamen.  Straß- burg 1909.    S.  333/334.
1800.  Tk.  saksy:
'Blumentopf,  Porzellan vase'  [Kel6kian Kämüs  659a,  mit  Abbildung];  hieraus rum.  sacsie  'Blumentopf.
1801.  Tk.  sakyz:
#### 1762
1498:'Feldherr,  Vezier'  [zu  pers.  färzänä 'weise,  gelehrt'  Horn  NpEt  S.  1 81 ,  Nr.  8 1  ö]; da  im  orientalischen  Schach  neben  dem König  [säh  s.  hier  Nr.  1762]  nicht  die Königin,  sondern  der  Wesir  die  Haupt- figur war,  wurde  hieraus  afrz.  ferce, fierge,  nfrz.  vierge  [mit  volksetymolo- gischer Umdeutung  zur  „Dame"],  prov. fersa  ;  bulg.  serb.  ferz,  russ.  ferz'  'Dame oder  Königin  (im  Schachspiel)'.  [Mikl SlEtWb  58a.  Bern  SlEtWb  280/281. ML  3266.
3673:1604.  Pers.  päilisäli: 'König'  [aus  pers.  päd  'Schützer'  Horn NpEt  S.  60,  Nr.  265,  und  säh,  s.  hier Nr.  1762,  also  eigentlich  'Beschülzer- Konig'],  Titel,  der  dem  Sultan  der  Türkei zukam:  tk.  padysah;  hieraus  rum.  pa- di§ah,  padifach;  dtsch.  Padischa,  poln. padyszach  usw.
4010:'Falke  Falco  peregrinus'  [aus  pers.  sah 'König',  s.  hier  Nr.  1762,  also  wörtlich 'der  königliche'  sc.  Vogel],  ebenso  tk.; hieraus  bulg.  sahin  'Falke';  rum.  §oim 'dass.',  fig.  'kühner  Mensch'.
4018:'Fumaria  officinalis  Erdrauch'  [aus  pers. säh,  s.  hier  Nr.  1762,  und  tär  'feucht, frisch,  zart'  Horn  NpEt  S.  85,  Nr.  382], ebenso  tk.  sahtere,  sahtere  [Kelekian Kämüs  717a];  hieraus  rum.  safterea, saftirea  'dass.'.
4858:fäm'  und  pers.  säht,  s.  hier  Nr.  1762; Tielleichl  ist  auch  ytyr  tk.  Wort  mit  der Bedeutung  'Geranium']  oder  'Geraniunr, so  auch  tk.  (Kelekian  KämOs  851  h] : hieraus  rum.  indi-i^aim,  andri^ea  'Ge- ranium'.
5683:laA  1762
5707:Abessinier  765 Abschach  1762 ^6«  1 4ö<<'z  1 Äbtissin  1 Acarnar  St.  33 acheln  j.  42 Achelputz  j.  42 Achernar  St.  33 Achltischemali  St.  902 Adamsapfel  19 Adniiral  69  a admirät  inhd.  69  a ^/ft;  1063 Agger- Agger  30 .4^Äa  28
5874:Saccharin  1855 ÄicÄ;  1781 SäcAreZ  1781 Sacker  falk  1799 Sackmann  1781 &'a/^«n  1752 Äa/"«/-«  1879 Ärt/'/jaw  1769 SaA/-«w  2178 Sa^o  1761 Sahara  1766 Sniga(antilope)  1774 Salangan  1844 Äa^pft  2001 Sa/t;p  2001 Äa/i««-  1567 Salniter  1567 salomonisch  1881 Sambuk  1824 sambaztac  ahd.  1742 sameztag  nihd.  1742 Samatag  1742 Samum  1819 Sandel(holz)  1825 Sapeke  1835 Sarafan  1845 Sarazene  1856  c Sarsche  1878 Sarong  1862 Safa«'  1867 Äa<m  2188 S(,/rt  1869 Schabbes  j.  1742 Schabbesgoj  j.  728 Schabracke  395 Schach  1762 Schacherjude  1763 schachern  j.  1763 schachtnott  1443 schachzabel  mhd.  1762 Schachzngel  1762 Schäfzngel  1762 si-haqgün  mhd.  434 Sc-Äa/i  1762 Schakal  1929
5877:Schäker  1788 schäk-ern  1788 Schakren  j  17i>8 Schal  1802 Schalet  ].  1804 Schalotte  119 Schamane  1928 Schanifott  653 schamponieren  417 Schanze  1059 Scharlach  1794 scharlät  iiilid.  1794 Scharriic'arri  1849 Schasmin  942 Schauhe  737 Schaum pun  417 Sc/iaii/e  j.  1927 Äc/iea«  St.  1771 Schebecke  1740 Scheck  1762 Scheich  1775 Schellack  1295 «■cAer/f  1852 Schibbolet  1891 schicker  ].  1787  b Schicksei' j.  1789 Schikane  434 Schin(hiindchen )  420 Schlamastik  j.  1920 Schlammassel  j.  1920 SfA/t«/'  j.  1804 Schlemiel  1882 Schlemihl  1882 Schlimasdlnik  j.  1920 Schlimasel  j.  1920 Schmuck  1946 Schmiere  (stehen)  j.  1813 Schmu  (machen)  j.  1884 .Sc/if/i?iZ  j.  1811 ÄcÄ»«««  j.  1884 schmusen  j.  1884 Schmuser  j.  1884 Schoberbartel  j.  259 schofel  j.  1751 Äf/io^e  j.  1927 Schübe  mhd.  737 Schuhjack  1679 SefeZ^os  j.  184  a sf/"eZ«  j.  2210
6031:charpoy  381 chaUti  'l  F87 fhecl-  1762 checkniaie  1443 cheechfc  419 chcenar  i'lb cheese  430 cÄeroo<  1888 chei'ub  1165 fÄfss  1762 chicane(ry)  434 chiffonnier  1893 chimistry  1157 cÄtwa  421 ching-ching  422 chop(-suey)  418 cÄunA-  1831 1787  a cimetar  1910 cinnabar  1827
6223:sÄrtÄ  1762
6418:eangiar  814 lanqitc  104'! caolin  1060 eapoc  1067 capoqiiier  1067 cäpres  978 carflW  1004 caraf(f)e  689 caragtieuse  1079 carambolier  1084 cara/  1182 cararane  1075 earavans6rail  1075 carcan  1096  b carcas  nifz.  2081 car^i  1073 carmaniine  1161 carmentine  1161 carniin  1219 carquois  2081 carthame  1262 caroube  832 earouge  832 earri  1087 casaque  1143 casauba  1108 casba(h)  1108 casoar  1119 casuarine  1119 cauris  1133 caviar  851 cMratier  303 censal  1836 chabraque  395 cÄaca?  1929 chachia  1865 chagrin  1760 fÄöÄ  1762 1802
6419:chalemine  afz.  1149 chamau  1928 chameau  653 chanipac  390 charahia  674 charchan  afz.  1096  h cÄeftec  1740 cA^f/jia  1865 cÄ«l-  1775 cÄ^gM«  1762 chercant  afz.  1096  b cÄ^ri/  1852 chh-ubin  1165 chervis  1095 chevilles  980 chicanc  434 chicoter  434 cÄ»7f«  afz.  1893 chijfon(nier)  1893 cÄ?';fre  1894 chimie  1157 chiroui  1095 rirfr«"  1787  a
6478:I  ^6«s  892 I  ecatlate  1794 I  Schalotte  119 :  ^cZ/^-cfs;  1762
6479:ichiquier  1762 .  ecume  de  mer  1416 :  erfttY/i;  768 ,  ef(f)endi  557 I  igyptien  1222 I  ^/e//a  1304 I  cZ(7«?;)ar  629 1  ilixir  903
7168:salamiltcchi  siz.  1803 salibba  siz.  1808 salnitro  1567 nandalo  1825 mrabanda  1850 saracenico  1856c saracinare  1856c saracino  1856c sargia  1878 sasinä  dial.  839 «öya  siz.  1791 sayuni  siz.  1791 sbaragliare  225 sbaragltno  225 sbaraglio  225 scacchiero  1762 scacco  1443.  1762 scalogno  119 scansia  1059
7632:saffraan  2178 sagaai  2181 sa/eÄ;  1780 saZej)  2001 saroeng  1862 schaak(spel)  1762 schabrak  395 schacheraar  1762 schacheren  1762 Schariaken  17'J4 schellak  1295 schibboleth  1891 segrijn(leer)  1760 sene  (blad,  -boom)  1822 senil(boom)  1822 senneblad  1822 s*M-e?  1880 sirocco  1856 siroop  1838 sJaaZ  1802 s/o/"eZ  1751 sjorklamp  687 sjorren  687 sjorring  687 sjortauw  687 swa^"  1946 sofa  1935
7771:s^acÄ  1762
8466:xaque  1762
8589:escac  1762
```


## [2026-09-06T21:31:17.268Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/^1762\\./{f=1} f{print} /^1763\\./{if(f)exit}' LKT.txt | head -40"
}
```


### [2026-09-06T21:31:18.876Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T21:31:20.983Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1761\\.\\|1762\\.\\|1763\\.\" LKT.txt | head; "
}
```


### [2026-09-06T21:31:21.030Z] TOOL RESULT

```
4004:1761.  Mal.  sägü: 'Mehlartiges  Pflanzenmark'  [Pijn  ISSa; die  von  Seiler  DKiL  IV,  332  angegebene Bedeutung  'Brot'  ist  erst  sekundär]  aus der  Palme  Metroxylon  laeve  Hart.,  die überall  im  mal.  Archipel  und  den Philippinen,  bes.  aber  auf  den  Molukken, heimisch  ist  und  für  die  Eingeborenen dieselbe  Bedeutung  hat  wie  der  Reis  für die  Chinesen  oder  das  Getreide  für  die Europäer.  Hieraus  frz.  sagou,  der  Baum sagomer,  sagoutier,  sp.  sagü;  engl,  sago, dtsch.  Sago;  russ.  sago.  —  [Den  ersten Sago  brachte  MARCO  POLO  i.  J.  1295 nach  Venedig,  vgl.  MP  445.]  [MMM  48. Devic  DEt  2U0.  Hobson-Jobsun  780/781.
4007:1763.  Hebr.  sähar:
```


## [2026-09-06T21:31:23.271Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4005,4007p' LKT.txt"
}
```


### [2026-09-06T21:31:23.315Z] TOOL RESULT

```
17G2.  Pers.  sah: 'König,  Herrscher'  [Horn  NpEt  S.  170, Nr.  772];  hieraus  zur  Bezeichnung  des Kaisers  von  Persien  u.a.  rum.  §ah,  ^ach; russ.  sah,  bulg.  serb.  sah,  öech.  sach, poln.  stach;  frz.  chah;  dtsch.  Schah,  engl. shah.  Aus  dem  beim  Schachspiel  üb- lichen Ausruf:  säh  mät  [s.  hier  Nr.  1443] entstand  allgemein  der  Name  für  dieses Spiel:  rum.  sach,  it.  scacco,  prov.  escac, frz.  ^chec,  gewöhnlich  erhecs,  sp.  jaque [nur  im  Zurufe  jaque  mate],  pg.  xaque; ndl.  schaakspel,  eugl.chpss,  disch.  Schach, Abschach  [in  Lessings  Nathan  II,  1]; russ.  Sah,  bulg.  sah,  cech.  sach,  poln. szach;  das  'Schachbrett'  heißt  danach it.  scacchiero,  frz.  Miiquier,  sp.  jaquel; russ.  Sahmaty;  mhd.  schdchzabel  [<  lat. tabula],  hieraus  dial.  Schachzagel,  Schäf- zagel  [also  volksetymologisch  als  'Schafs- schwanz' gedeutet,  vgl.  Andresen  DVE 29].  Endlich  wurde  aus  afrz.  eschec  zur Bezeichnung  eines  'Zahlscheins'  [Vor- schlag des  Deutschen  Allgemeinen Sprachvereins]  engl,  check,  frz.  cheque.
dtsch.  Scheck.  Vgl.  noch  frz.  dchec  'Miß- erfolg, Schlappe'.  —  [Das  Wort  Schach suchte  als  urgermanisch  zu  erweisen M.  MAY  in  Zeitschrift  des  Dtsch.  Allg. Sprachvereins  (1895)  X:  Entgegnung. Zum  5.  Hefte.  S.  1/4  ]  [DE  352.  Eguilaz 391.  Kluge  4.  382.  ML  7669.  Gor- jajew  419.
1763.  Hebr.  sähar:
```


## [2026-09-06T21:31:31.110Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM صك ===\"; grep -n \"الصك\\|( صك )\\|صَك\" AFM.txt | head -10; echo \"=== PLA sakk ===\"; grep -n \"sakk\\|ṣakk\\|Sakk\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10"
}
```


### [2026-09-06T21:31:31.183Z] TOOL RESULT

```
=== AFM صك ===
1029:بتك الفارسية ماخوذة من ܦܬܩܐ الآرامية ومعناها البطاقة والرسالة والصك وهى 
=== PLA sakk ===
13825:Su. sakk: "Gerichtsakt" aus dem pers. sedek _>tk. cek, engl. check, 
13833:Se - sakäk: Pl. v.cw sakk s. sakk.
```


## [2026-09-06T21:31:33.915Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13810,13840p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-06T21:31:33.960Z] TOOL RESULT

```
Suas - saClik = sa 1lük q- v. 


slao- sagäna: '"Kastagnetten; in Spanien übl. Handklappinstrument aus zwei 
miteinander verbundenen bewegl. am Daumen befestigen Hartholzschalen"!" 
<< pers. sl“, Sagäne ı wahrscheinlich ein Dual v. mp. sj:? &öbak "zwei 
kleine Holzstücke". 


>92. sifahbad: "General" = isfahbad q. v. 


„>#- sagqr: "Rad" = saqr u. zaqr q. V. 2, 


Su. sakk: "Gerichtsakt" aus dem pers. sedek _>tk. cek, engl. check, 
frz;, cheque. 
Scheck geht aller Wahrscheinlichkeit nach auf das pers. tschäk 
"Urkunde, Vertrag" zurück 3, 
Dtsch. Scheck: "Anweisung (an eine Bank od. an die Post) auf Zahlung 


von Geld an einen Dritten" pers. > ar. > lat. > £rz. *. 
Se - sakäk: Pl. v.cw sakk s. sakk. 


=> - salib: "das Kreuz" Nabiga 2, 10 ist bekanntlich durch 
Vermittlung des aramäischen \aD 3 , $a"by aus pers. Jo Lallpä 
entlehnt. Danach ist Gesenius Hwb. IX. 710. Sp. 1. z. 15 
a. f. zu berichtigen. Die Wurzel «Je ist aber auch echt Anrk. 
55, 11. °.
```


## [2026-09-06T21:31:43.805Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"Check,[^|]\\{0,600\\}\" SKT.txt | head -3; echo \"=== Chess ===\"; grep -o \"Chess,[^|]\\{0,400\\}\" SKT.txt | head -3; echo \"=== Satrap ===\"; grep -o \"Satrap,[^|]\\{0,400\\}\" SKT.txt | head -3; echo \"=== Shah ===\"; grep -o \"Shah,[^|]\\{0,300\\}\" SKT.txt | head -3"
}
```


### [2026-09-06T21:31:45.418Z] TOOL RESULT

```
Check,  a  sudden  stop,  repulse.  (F.— Pen.)  M.  E.  ehek.  a  stop ;  also  check  I  in playing  chess.  The  word  is  due  to  the game,  which  is  very  old.  The  orig.  sense of  check  was  '  king  1  ie.  mind  the  king«  the king  ii  in  danger.  —  O.  F.  esehec,  '  a  check at  cDe«»-p1ay,'  Cot.  *  Pers.  xAjM,  a  kinc, king  at  chess ;  whence  skAh-mAl,  check- mate, Ut.  *  the  king  is  dead.*  from  m^t,  he is  dead.  Simibrly  we  have  F.  hhte,  a check,  repulse,  defeat,  pi.  iihe<$,  che^ ; Ital.  scatcQ,  a  square  of  a  chess-board,  also a  check,  defeat.
=== Chess ===
=== Satrap ===
Satrap,  a  Persian  viceroy.  (F.-L.-»Gk.
=== Shah ===
Shah,  king  of  I'crsia.  (Pcrs.)  Pen. thiih,  a  king.     Sec  Oheok.     Dev./a-sha.
```


## [2026-09-06T21:31:54.719Z] TOOL CALL #92: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Afshin",
 "prompt": "What is the etymology and meaning of the title Afshin (Afšīn)? Which dynasty/principality used it, and what Old Iranian/Sogdian form is it derived from?"
}
```


## [2026-09-06T21:31:56.594Z] TOOL CALL #93: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87",
 "prompt": "Persian پادشاه: give the full etymology — Middle Persian pādixšāy/pādixšāh, Old Persian *pati-xšāya-, the meaning of the elements pati- and xšāy-, and the semantic development."
}
```


### [2026-09-06T21:32:00.564Z] TOOL RESULT

```
# Etymology and Historical Use of Afshin

**Etymology and Meaning:**
The term traces back through linguistic history: "_Afšīn_ is form of the Middle Persian _Pišīn_, which traces back to Avestan _Pisinah_." In Persian mythology, it represented "the name of a grandson of Kay Kawad," establishing ancient roots for this designation.

**Historical Use:**
Afshin functioned as a princely title rather than merely a personal name. Specifically, "it was the title of the rulers of Principality of Ushrusana in Transoxiana before the Muslim conquest of Persia." The Sogdians also adopted this title for their leadership roles.

**Linguistic Origins:**
The name derives from Old Iranian sources, with Avestan (_Pisinah_) as the ultimate ancient source, evolving through Middle Persian forms before becoming the Persian name used historically across Central Asian principalities and dynasties.
```


### [2026-09-06T21:32:02.915Z] TOOL RESULT

```
# Etymology of Persian پادشاه (Padishah)

Based on the Wiktionary entry, here's the etymological breakdown:

## Source Languages
The word is "inherited from Middle Persian" with the form showing as /⁠pādixšā(y)⁠/. The entry indicates it descended from Old Persian elements, though the exact Old Persian reconstructions aren't fully detailed in this excerpt.

## Semantic Development
The Middle Persian root carried the meaning of "ruler, powerful, authoritative, authorized." This reflects a compound structure combining two conceptual elements related to sovereignty and authority.

## Component Elements
While the Wiktionary page doesn't explicitly parse the individual morphemes in the excerpt provided, the pattern *pati-xšāya- suggests:
- A prefix relating to power or rulership
- A suffix connected to kingship or royal authority

The term evolved through Chagatai, Ottoman Turkish, and numerous other languages (Arabic, Hindustani, Russian, Turkish, etc.), consistently maintaining its meaning as "king," "monarch," or "sovereign" across these linguistic descendants.
```


## [2026-09-06T21:32:17.701Z] TOOL CALL #94: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D8%B1\" \\\n\"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87\" \\\n\"https://en.wiktionary.org/wiki/%D8%B4%D9%87%D8%B1\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tek-\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-\" \\\n\"https://www.etymonline.com/word/satrap\" \\\n\"https://www.etymonline.com/word/check\" \\\n\"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%DB%8C%D9%86\" \\\n\"https://en.wikipedia.org/wiki/Afshin\" \\\n\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87\" ; do\ntimeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 278, root Ksei 1 (PIE *tek-/kþē(i)- 'to rule'): sah, sahr, sir, satrap, check/cheque, afsin, padesah\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T21:32:23.547Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ff12e8ca683ab8a4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08564bdd8f4ed805.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9a4edd205263c319.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b04829f7b6ec4520.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/acc6fd901ca285c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35670c7edeb259e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a95a973950d3ea79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/13e7658ca7df9a16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c8a325b587923e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa431033bede9965.txt
```


## [2026-09-06T21:32:27.875Z] TOOL CALL #95: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['SPG'].get('local_file'), d['SPG'].get('page_offset'))\"; ls -la data/verification/sources/refs/ | grep -i spg"
}
```


### [2026-09-06T21:32:29.641Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/SPG_keilinschriften1881.txt Keilinschriften 1881: leaf = printed + 11 for the texts, leaf = printed - 29 for the Glossar (e.g. leaf 182 = p.211). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
-rw-rw-r--  1 sfmqrb sfmqrb   466443 Sep  4 14:06 SPG_keilinschriften1881.txt
```


## [2026-09-06T21:32:32.625Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=185 && NR<=188 {print \"--leaf\",NR,\"--\"; print substr($0,1,2200)}' SPG_keilinschriften1881.txt"
}
```


### [2026-09-06T21:32:34.339Z] TOOL RESULT

```
--leaf 185 --
OIiOSSAB, 213
anzunehmen, dass im zweiten Theiie des Comp, a zu elidiren und zml
statt zam'i zu lesen sei. Im Awestä tritt in diesem Falle Verhärtung
des z zu s ein. Cf. khraozhdisma, varedushia, so dürfte es auch im
Altp. gewesen sein.
üvärazaniiya «7f -f^ ^, ^f f^^f ^zi n Mr) Choras-
mien Bh. I, 16. I, 16. Nebenform des vorhergehenden Wortes.
üsatashana «Tf f^ StTtT << S:<) Aufbau, Hochbau acc,
usatashanäm P, 29. Von tash = aw. tas , behauen, verfertigen und us, auf.
Vshka «7f << y^) trocken gen. ushkahyä. I, 13. Aw. hushka,
neup. v^Lai^ skr. ^ushka.
Uzamä {i^ }^^} ^)]) y^^) Kreuz oder Galgen uzamayäpatiy
Bh. II, 76. 91. III, 52. Ueber die Etymologie des Wortes cf. oben
p. 97.
Uhyäma «"jj <^< ]ir m "^y'^) "• pr-» Name einer Festung in
Armenien, Bh. II, 44.
Ka (f^) pron. interrog. wer, voc, masc. kä (cf. Gr. § 39) Bh.
IV, 37. 41. 67. 70. 87. seq. ciy: kashciy (cf. Gr. § 55) Bh. I, 49. 53.
Aw. ka neut. kad, dass.
Kaufa (f^ <7| f«) Berg, Bh. T, 37. III, 44. Huz. f]D Pärsi
koh, neup. ^S* Im Aw. findet sich kaofa von den Höckern des Kameeis
gebraucht. Vd. XXÜ, 10. Cf. neup. zj»^.
Katapafuka (T^ riffT ^ TfT"" 4^ T^:) kappadocisch, Name
des Landes Kappadocien. Bh. I, 15. I, 12. NRa, 28.
Kan (f^ ^^) graben, behauen, inf. kahtanaiy Szb, 9. K, 21.
aor. pass. akäniy Szb, 10. Aw. kan, skr. khan dasselbe.
+. ava werfen? imperf. 1. ps. aväkanam Bh. I, 86. Cf. neup.
^JuJot, was aber eher aiwikan ist. Im Aw. hat avakan die Be-
deutung ausgraben. Cf. Vd, XV, 110. avakana, Keller ibid.
+ ni eingraben, vernichten. 3. ps. sg. imperat. nikanfuv Bh.
IV, 80. Im Aw. wird nikan namentlich vom Begraben der Todten
gebraucht. Cf. z. B. Vd. UI. 27. 40. XII, 32. u. a. m.
+ vi zerstören. 3. ps. sg. imperf. v'iyaka Bh. I, 64. Im Aw.
vikan dass. cf. z. B. Vd. III, 43. 47. VII, 128. 129.
Kamna (f^ — fff ^^) wenig nom. neut. kamnam Bh. II, 19. 24.
instr. masc. kamnaibish Bh. I, 56. II, 2. III, 41. 70. üeber die Bedeutung
des Wortes vgl. oben p. 88.
--leaf 186 --
214 GL088AB.
Kampada (f^ ^ 7t) Name einer medischen Provinz, bei den Alten
Cambadene genannt, sie lag südwestlich von Ekbatana Bh. II, 27. „The
tract of country adjoining Bisutiin, on the left bank of the Gämäsäb,
retains to the present day the title of Chamäbatän." Rawünson im
Journal of the Roy. Geographica! Society IX, 112.
Karnhujiya (fc r:T 4^ ^4^ ff Mr) Kambyses. nom. Bh. 1,
28. 30. 31. 32. 33. 43. acc. Kamhufiyam Bh. I, 45. 46. abl. Kambi^'^iyä
Bh. I, 40. gen. Kambufiyahyä Bh. I, 29. 30. 39. Man hat längst bemerkt,
dass das Wort in den indischen Ländernamen Kamboja und den
Stammesnamen Kamoj bei den K&firs in Kabul sich wiederfindet. Cf.
Lassen: Zeitschr. für die Kunde des Morgenl. II, 57. Ind. Alterth'ums-
kunde I, 439. Rawlinson, Journ. of the R. As. Soc. XI, 97. Bekanntlich
führte auch ein Strom im nördlichen Medien, der heutige Gori, den
Namen Kambyses.
Kar (f^ ^T) machen, thun cl. 5. praes. conj, 2. ps. sg. Kuna-
vähy Bh. IV, 75. 79. imperf. 1. ps. sg. ak'unavam Bh. I, 62. 63. 68.
72. 87. II, 20. 76. 83. 91. III, 31. 52. 84. IV, 3. 6. 40. 41. 45. 59. 60.
65. 89. V, 2. 8. 34. NRa, 49. 51. D, 13. 14. E, 17. A, 27. S, 4. 3. ps.
sg. ak^maush. Bh. II, 23. 85. III, 5. 16. 56. IV, 10. 12. 15. 18. 20. 23.
26. 28. 31. 34. 35. V, 10. 0, 8. B, 6. Szb) 3. NRa, 5. 34. D, 4. 15.
E, 6. A, 8. C, 4. 11. F, 9. K, 7. 20. 23. P, 8. Solöcistisch auch afiunash:
S, 3. 1. ps. plur. ak'umä Bh. I, 90. 94. 96. II, 68. 70. D, 17. 3. ps. plur.
ak'unava Bh. II, 34. 39. 45. 54. 59. 96. III, 37. 44. 60. 65. V, 6. NRa, 20.
Perf. 3. ps. pot. cakhriyä Bh. I, 50. Medium imperf. 3. ps. sg. akunavatä
NRa, 37. mit passiver Bedeutung, 3. ps. pl. aKunavantä Bh. III, 12, auch
3, ps. sg. ak'utäBh, I, 47. Passiv imperf. 3. ps. sg. ak'unavyaiä Bh. I, 20. 24.
Infinitiv : carianaiy Bh. I, 94. II, 33. 38. 44. 53. 58. 67. III, 36. 43. 59. 64.
Part. pass. kartam. Bh. I, 27. II, 27. 37. 42. 47. 57. 62. 92. 98. III, 9.
10. 19. 21. 40. 47. 63. 68. 75. IV, 2. 42. 46. 49. 51. 54. NRa) 48. 51.
D, 14. 15. 19. E, 19. A, 23. 25. 30. C, 13. 14. K, 27. Solöc. karia L
und kartä P, 31. 35, an letzterer Stelle wol Participialperfectum.
+ pari behüten, bewahren praes. conj. 2. ps. s%, pa
--leaf 187 --
* aLOBSAB. 215
Kära (T^ lYjf ^t) 1) der Handelnde. Der handelnde Theil der
Bevölkerung, sowol im Krieg' als im Frieden, daher nach Umständen
2) das Heer Bh. I, 85. II, 18. 25. 30. 35. 40. 46. 50. 55. 60. 87, III, 3.
17. 26. 32. 38. 45. 58. 61. 66. acc. käram Bh. I, 82. 86. %%. 95. II, 19.
20. 25. 35. 41. 46. 55. 61. 68. 72. 81. 83. 87. lü, 1. 4. 7. 15. 17. 29.
38. 42. 46. 54. 57. 61. 66. V, 7. I, 21. instr* kärä, Bh. I, 93. II, 22. 67. 85.
m, 15. 33. 36. 72. 85. V, 9. genit. kärahyä III, 69. 3) überh. die
Leute, die Angehörigen des Staates nom. Bh. I, 33. 40. 50. 79.
II, 16. 75. 90. III, 15. 80. I, 22. acc. käram, Bh. I, 51. 52. 66. 78.
II, 83. III, 84. IV, 34. instrum. kärä. I, 8. gen. kärahyä. Bh. I, 31. 38.
64. 75. II, 10. 15. 80. III, 24. IV, 55. 58. Cf. neup. ^L5^ ^Iv^li" u. A.
Kuganakä {i^ 4^ iy\^ ^{)Zi^\) Name einer Stadt in der
Persis, wahrscheinlich an den Gränzen von Susiana Bh. II, 9.
K'udXu)rush (^f 4^ i^ ^{^ <7f <<) "• pr- Name einer Stadt
im östlichen Medien Bh. II, 65. Ich lese Kurfur'ush, indem ich annehme,
dass ^^T abgekürzt statt d'u steht.
Kur'u (^y ^^ ^i^ ^7l) "• pr- Kyrus. nom. K-ur"ush M, 1. gen.
K'uraush Bh. I, 28. 39. 53. III, 25. IV, 9. 27. b, 5. h, 6. Der Name
Kuru ist zwar nicht mit aw. hvare, neup, \y^ Sonne identisch, wie die
Griechen wollen (dies müsste altp. uwara heissen), wol aber mit dem
indischen Kuru cf. Kuhn Beiträge I, 32 flg.
Kushiya (^f 4^ ^ ff f^— ) n. pr. Name eines Volkes nom. plur.
K'usiyä NRa) 30. Lassen und Rawlinson denken an die Koaaaioi^ Oppert
an die Kuschiten, die }0\2 der Bibel. Vgl. oben p. 119.
«TTM.
Khshatra (^^ff << ^) die Herrschaft, das Reich nom. acc.
khshatram Bh. I, 12. 25. 26. 41. 42. 44. 45. 50. 59. 60. 61. 80. H, 3.
Szb) 3. D, 19. E, 19. A, 29. K, 26. aw. khs'athram dasselbe, ob neup.
y^ von khs'athra oder von s*dithra abzuleiten sei, ist mir noch
zweifelhaft.
Khshafrapävan (^^ff << fl ^ Hl ""^^ ^K) ^®r Satrape nom.
khshairapävä Bh. III, 14. 55. Von khshatra und pä, beschützen.
Khshathrita (^^f f << W;^ T U ^'^'T) N. pr. Name eines Empörers
in Medien Bh. II, 15. IV, 19. e, 6. (Westergaard liest den Namen
Khshatharita. Cf. Gramm. § 4. 3).
Khshapa {4^4^ << ^) Nach
--leaf 188 --
216 OIi068AB«
Khshäyathiya («ff << ^| f<- y<y f T f<«-) König, nom. M, 1.
Bh. I, 1. 2. 4. 6. 9. 11. 12. 13. 14. 18. 21. 24. 27. 29. 85. 44. 4& 60.
61. 71. 72. 73. 75. 76. 81. 83. 90. II, 1. 5. 8. 11. 14. 17. 18. 29. 37.
43. 49. 57. 64. 66. 70. 78. 80. 91. 92. lü, 1. 9. 11. 20. 21. 28. 29. 40.
49. 53. 63. 68. 74. 75. 82. IV, 1. 3. 11. 17. 21. 25. 31. 33. 36. 37.40.
43. 45. 50. 53. 57. 59. 62. 67. 70. 72. 76. 80. 86. V, 1. 3. 15. 19. 21.
31. 35. a, 1. 2. 5. 9. 14. b, 6. c, 5. d, 6. e, 9. f, 5. g, 6. h, 8. i, 9.
j, 4. 0, 12. 13. 14. 16. H, 5. 6. 12. I, 1. 2. 3. 6. 19. B, 1. 2. 3. Na) Sza)
Szb) 5. 7. NRa) 8. 9. 10. 11. 15. 31. 34. 40. 48. NRb) 5. D, 6. 7. 8. 11. 18.
6, 1. 2. E, 9. 10. 11. 15. A, 12. 13. 14. 16. 22. C, 6. 7. 10. 11. F, 12. 13.
14. 16. 19. K, 10. 11. 12. 17. Qa) Qb) S, 1. P, 7. 11. 12. 14. 15.16.18.20.
21. 23. 28. 32. — acc. khshäyathiyam 0, 7. 9. H, 2. Szb) 3. NRa) 5. 6. 33.
NRb) 4. D, 4. 5. E, 5. 7. A, 7. 9. C, 4. 5. F, 8. 10. K, 6. 7. P, 9. gen.
khshäyathiyahyä Bh. III, 58. H, 10. Szb) 3. NRc) 2. NRd) 1. D, 10.
6, 3. E, 13. A, 19. C, 9. 14. F, 19. K, 15. — plur. noiiK khshäyathiya
Bh. I, 8. 10. IV, 5. 51. a, 13. 16. 17. acc, khshäyathiya Bh. IV, 7. 32.
gen. khshäyathiyänäm Bh. I, 1. 2. a, 2. 0, 14. I, 2. B, 2. Szb) 5.
NRa, 9. D, 7. G, 2. E, 10. F, 14. K, 11. Solöc. khshäyathiyänäm P, 13.
üeber die Etymologie des Wortes cf. oben p. 81.
Khshayärshä («ff "^ |<i- ^y HY<< TTl) "• pr. Xerxes nom.
Khshayärshä, D, 6. 11. 17. G, 1. E, 8. 15. A, 11. 21. C, 6. 9. F, 12.
K, 9. 16. Qa, 1. P, 21. 22. acc. Khshayärshäm D, 4. E, 5. A, 7. C, 4. F, 7.
K, 6. Solöc. gen. Khshayärshahyä S, 2. Der erste Theil des Wortes
stammt entschieden vom aw. khs'i können, mächtig sein, der letzte
Theil mag arshan Auge (wie in Qyävarshan) oder arshan» Mann sein,
doch ist dies nicht ganz sicher.
Khshi («ff << TT) herrschen. Im Aw. khs'i, skr. xi.
+ pati: beherrschen. 1. sg. imperf. med. patiyakhshaiy ich be-
herrschte. NRa) 19. Cf. oben die Bemerkungen zu d. St.
Kkshnäs («ff ^ E:^ fTl ^) kennen, praes. coiy. 2. p. sg. sq.
d'ish: khshnäsähad'ish NRa, 42. 3. ps. khshnäsätiy Bh. I, 52. Cf. ^jJCSLu
im Neupersischen und den anderen neuöränis
```


## [2026-09-06T21:34:46.247Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"\\*xšay[^|]\\{0,300\\}\\|xšaH[^|]\\{0,200\\}\" CHEUNG.txt | head -6; echo \"=== ISS ===\"; grep -no \"kṣatra\\|ksatra\\|xšaθra\" ISS_alt_DKS.txt | head -5"
}
```


### [2026-09-06T21:34:47.954Z] TOOL RESULT

```
29127:xšaH ‘to rule, be lord of’ 
=== ISS ===
1133:ksatra
4216:ksatra
5134:ksatra
7777:ksatra
7777:ksatra
```


## [2026-09-06T21:34:50.128Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29120,29160p' CHEUNG.txt"
}
```


### [2026-09-06T21:34:50.176Z] TOOL RESULT

```
*REFERENCES: Ivanow 1926: 419; Abaev, Slovar’ IV: 226 


*xSaH 451 


*xšaH ‘to rule, be lord of’ 

*AVESTAN: xšā- ‘to be able; rule, be lord of = Liste: 17 

Pres. aia-: IND. 2sg. OAv. xsaiiehi (Y 44.15), med. 2sg. YAv. xSaiiehe (Yt 10.29), med. 3sg. ҮАУ. 
xsaiiete, 2р1. OAv. xšalla08 (Y 48.9), med. 3pl. YAv. xsaiiente (Yt 17.7, ms. F1), INJ. med. 3sg. ҮАУ. 
xsaiiata, SUBJ. 15р. (?) OAv. xsaiia (Y 50.9), YAv. xsaiieni (FrW 4.2), 3sg. YAv. xsaiiat (FrW 4.2), 
OPT. 35р. Y Av. xSaiidit (Y 9.5), IMPV. 2sg. (?) OAv. xsaiia (Y 28.7); Aor. them.: INJ. med. 3р1. OAv. 
х$әша (Y 48.5), OPT. med. 25р. Y Av. xsaesa (Y 8.5, rep.), med. 3sg. OAv. xsaeta (Y 41.2), IMPV. med. 
3р1. OAv. xsöntam (Y 48.5); Partic.: pres. xsaiiant-, pres. med. xSaiiamna- ‘being able to’ (Yt 10.23, Yt 
10.37, Yt 10.110). © YAv. xšaiiðit is discussed by Hoffmann 1976: 607f.; Kellens 1984: 311, fn. 1; 
Kellens 1984а: 270 £.; Paul 1998: 314a f. || With regard to xSaiiamna-, cf. Gershevitch 1959: 178, ad 23: 
"It seems that the middle ptc. xSayamna- with a finite verb always indicates that the subject can, or may, 
perform the action expressed by the finite verb". 

*OLD PERSIAN: (+ *upari-) upari-xsa- ‘to rule over’ || (+ *pati-) pati-xsa- ‘to have 
lordship over’ = Kent: 181a 

МЕР); Pres. аја-: impf. IND. med. 159. "upariyaxsayaiy <u-p-r-i-y-a-[y]-m> (DB 4.64), patiyaxsayaiy 
<p-t-i-y-x-8-y-i-y> (DNa 19, XPh 17), <[p]-[t]--y-[x]-[8]-[y]-[i]-[y]> (DSe 17); Partic.: pres. med. 
xsayamna- (DNb 15) 

*MIDDLE PERSIAN: MMP $^y- ‘to rule, have power; be able/worth/worthy [+ inf.]’, 
MMP S’yh- ‘to be king’, rule, come into a position of authority’, ВМР gd S^y- 
/Say-/ ‘to be able, possible; to be worthy’ || (+ *pati-) BMP p’ths’d, p’ths’dy (BMP 
ҮТ") /pädixsä(y)/ ‘ruler, sovereign, over-lord; authorised’ = DMMPP: 315a 

Well attested: Pres.: IND. 3sg. MMP S’yhyd, BMP Sdt s’dyt /Sayed/, 1р1. BMP $’yym /sayém/, 3р1. 
BMP $’dynd /sayénd/, etc. 

*PARTHIAN: šh- ‘to be able [+ inf. || (+ *pati-) pd(y)xs’- ‘to rule, be lord of 
c Ghilain: 88 | DMMPP: 315b 

Pres.: IND. 159. sh'm, 2sg. Shyh, 35р. Shyd, Shyyd, 3pl. Shynd, SUBJ. 2sg. "sh’h, 1р1. sh’m, 2pl. sh’d,
```


## [2026-09-06T21:34:55.407Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29160,29200p' CHEUNG.txt"
}
```


### [2026-09-06T21:34:55.457Z] TOOL RESULT

```
Pres.: IND. 159. sh'm, 2sg. Shyh, 35р. Shyd, Shyyd, 3pl. Shynd, SUBJ. 2sg. "sh’h, 1р1. sh’m, 2pl. sh’d, 
OPT. Shyndy(y)h; Partic.: pres. ’xSynd ‘prince’, perf. pass. Sh’d || (+ *pati-) Pres.: IND. 3pl. pdyxs’hynd; 
Partic.: perf. pass. П pdyxs’h’d ‘rule’ 

*SOGDIAN: BSogd. "xs^y-, CSogd. xSy- ‘to rule’ 

Impf.: IND. 3sg. CSogd. xSy’, 3р1. BSogd. ’xs’y’nt 

*CHORESMIAN: m/xh- ‘to rule, govern’ = Samadi: 236 

*BACTRIAN: þu- ‘to be able; can’ = S-W, Bact.: 235 

*NWIR: NP Säyistan/säy- ‘to be appropriate’, Abyan. esö/s-, Abz. ašo/š-, Nn. Sa/si, 
Qohr. ašā/š- ‘to be able’, (impers.) NP säyad ‘perhaps’ (< ‘it is fitting’), Kurd. (Sor.) 
Siyan/sé- ‘to be appropriate’, Zaz. Sinayis (Sayis)/Sen- ‘to be able (to do something)’, 
Anar. (impers.) mi-Sum, mi-Sowume, Fariz. -5-, Yar. ši-, Gz. šā-/šā, Isfah. (supplet. 
tundn) Sa- ‘to be able’ 

*SANSKRIT: ksay, Кѕа ‘to rule, have power, own’ (RV) = EWAia I: 426 

© The Indo-Iranian formations (Skt.) ksa-, (Ir.) *xsa- are connected to the ‘guard, 
supervise’ forms (*Нахё, Av. aißiiäx$-, etc.) by Lipp (LIV: Lc.), who therefore 
adopts the earlier suggestion of Wüst 1966: 80 f., 83 f. A convincing explanation of 
the semantical aspects is lacking though. Since the political and cultural context of 


452 *xšal 


ksa- and *xsa- respectively is still not clear to us, the postulation of further IE 
connections remains elusive. Gr. ктдрол ‘I obtain’, ктёото, xtpata (pl. tant.) 
“property, goods’ are most often cited as possible cognates. 


«PIE? c LIV: 618 f. | Pok.: 626 
*REFERENCES: KPF I: 136a f.; Ivanow 1926: 422; Christensen, Contributions I: 156; Abrahamian 1936: 
132; WIM II/1: 83; Werba 1997: 281; Cabolov 1997: 72; Lecoq 2002: 187 f. (passim) 


*x8ai ‘to be anxious, worried, weep, lament’
```


## [2026-09-06T21:35:02.655Z] AGENT

Now I'll write the verification file.


## [2026-09-06T21:43:17.725Z] TOOL CALL #100: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build278.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Ksei 1, Qsěi\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *tkʷeh₁(i)- / *tk-eh₁(i)- 'to acquire, get power over, rule' (Pokorny kþē(i)-, kþə(i)- p.626; Watkins/AHD tḱē- 'to gain control of, gain power over'; Wiktionary files it under *tek- 'to take by the hand, receive, obtain'). Indo-Iranian *kšay- / Proto-Iranian *xšaH- 'to rule'.\",\n \"note\": \"Nourai's headword 'Ksei 1, Qsěi' is simply his rendering of Pokorny's two adjacent entries on p.626, kþei- 'siedeln, sich ansiedeln' and kþē(i)-, kþə(i)- 'erwerben, Verfügung und Gewalt worüber bekommen'. Everything on this page belongs to the SECOND root ('to acquire power, rule'), and the gloss 'to be able to, to qualify, to rule' matches it exactly; the language label 'Indo-European' is right. Klein (Nourai's other root reference) sets up the same base *qþe(i)-, *qþēi- 'to possess, rule'. The Indo-Iranian branch (Skt. kṣáyati, kṣatrá-; Av. xšayeiti, xšaθra-; OP xšāyaθiya-) is beyond doubt; the wider IE equation with Gk. κτάομαι 'I acquire' is the standard handbook view (Pokorny, Walde-Pokorny, Watkins, Buck, Klein) but Cheung (2007: 451) calls further IE connections 'elusive'. Note also that the chart's own NOTE about the suffix (see node 1) is wrong.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tkʷeh₁(i)- «به دست آوردن، چیرگی یافتن، فرمان راندن»، که پوکورنی آن را در صفحهٔ ۶۲۶ زیر kþē(i)- آورده و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage آن را tḱē- «چیرگی یافتن» می‌نامد. برچسب زبانی و معنایی که نورایی داده است درست است؛ سرواژهٔ «Ksei 1, Qsěi» تنها آوانگاری خود اوست از دو مدخل پیاپی پوکورنی در همان صفحه (یکی به معنی «سکنی گزیدن» و دیگری به معنی «چیرگی یافتن»)، و همهٔ شاخه‌های این نمودار به مدخل دوم بازمی‌گردد. شاخهٔ هندوایرانی (سنسکریت kṣáyati و kṣatrá-، اوستایی xšayeiti و xšaθra-، پارسی باستان xšāyaθiya-) قطعی است؛ هم‌ریشگی با یونانی κtáomai دیدگاه رایج کتاب‌های مرجع است، هرچند چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ص۴۵۱) پیوندهای فراتر از هندوایرانی را «نامطمئن» می‌خواند. ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/tek-\", W+\"Reconstruction:Proto-Indo-European/tḱey-\", W+\"%D8%B4%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"POK:626\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt leaf 286-287 (printed pp.626-627): 'kþe(i)-, kþə(i)- „erwerben, Verfügung und Gewalt worüber bekommen“. Ai. kṣáyati „besitzt, beherrscht“ (*kþəi-eti) = av. xšayati „hat Macht, Gewalt, herrscht“ ... apers. xšāyaθiya- „im Besitz der Herrschergewalt, König“ (npers. šāh), Xšayāršan- „Xerxes“'. Exactly the page and exactly the claim; note that p.626 also carries the neighbouring root kþei- 'siedeln'.\"},\n   {\"ref\": \"KLN:272\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 s.v. 'check' (KLN_1966.txt line 7296): 'fr. Pers. shah, ‘king’ ... fr. OPers. xshaya-, ‘king’ ... fr. I.-E. base *qþe(i)-, *qþēi-, ‘to rule’, whence also OI. ksayati, ‘possesses, rules’, ksatram, ‘rule, dominion’, Gk. κτάομαι, ‘I get, acquire’.' Same root, same gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.504 (incoming/WLD/WLD_Bd1_pages.txt leaf 512)\", \"stance\": \"supports\",\n    \"note\": \"'qþe(i)-, qþə(i)- „erwerben, Verfügung und Gewalt worüber bekommen“. Ai. kṣayati „besitzt, herrscht“ = av. xšayeiti ... ai. kṣatra- n. „Herrschaft“, av. ap. xšaθra- ... ap. xšayaθiya- ... Xšayāršan „Xerxes“.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. tḱē-\", \"stance\": \"supports\",\n    \"note\": \"'tḱē-. To gain control of, gain power over. 1. ... Sanskrit ksatram, rule, power, and ksayati, he rules: KSHATRIYA; b. Old Persian khshathra-, kingdom, province, in compound khshathra-pava, protector of the province: SATRAP. 2. ... Old Persian khshayathiya-, king, whence Persian shah, king: CHECK, SHAH; CHECKMATE. [Pok. kþē(i)- 626.]'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 19.31 'Rule', pp.1319-1321\", \"stance\": \"supports\",\n    \"note\": \"'Skt. kṣi- ‘possess, rule’, Av. xši- ‘have power, rule’ (with sbs. Skt. kṣatra-, Av. xšaθra-, OPers. xšaça- ‘rule, realm’, Av. xšaya- ‘ruler, king’, OPers. xšāyaθiya- ‘king’) : Grk. κτέομαι ‘possess’. Walde-P. 1.405. Barth. 550, 551, 553.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH\", \"stance\": \"partial\",\n    \"note\": \"'*xšaH ‘to rule, be lord of’ ... «PIE? c LIV: 618 f. | Pok.: 626'. Cheung confirms the Iranian root and Pokorny's page but adds: 'Gr. κτάομαι ‘I obtain’ ... are most often cited as possible cognates ... the postulation of further IE connections remains elusive.'\"},\n   {\"src\": \"IEC\", \"where\": \"grepped IEC.txt for kþē / ksayati / ksatra\", \"stance\": \"silent\",\n    \"note\": \"Mann's comparative dictionary returned no hit for this root under the spellings tried.\"}\n ],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"xšây, xši 2; xšača; xša-thra, xšathra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three forms are real and correctly attached to the root, but two of the glosses and the chart's NOTE are wrong. (a) Av. xšā(y)- / xši- 'to have power, rule, be able' (3sg. xšayeiti, mid. xšayete; OP pati-xšaya- 'have lordship over', upari-xšaya- 'rule over') = Skt. kṣáyati, from PIE *tk(ʷ)eh₁(i)- — correct. (b) OP xšaça- (Av./Ir. *xšaθra-, with the regular Old Persian change θr > ç) means 'kingship, kingdom, realm', NOT 'king, ruler' as the chart glosses it; the Old Persian word for 'king' is xšāyaθiya- (< *xšāya-θiya-, 'in possession of the ruling power'). (c) Av. xšaθra- n. 'rule, dominion, realm' (Skt. kṣatrá-) is an Indo-Iranian neuter in *-tra-/-tram formed to the verb (an action/instrument suffix, Pokorny/Walde-Pokorny call it 'urar. Neubildung zu kṣayati'); the chart's NOTE that '-thra, -tra are Avestan suffixes meaning \\\"having, owner of\\\"' is simply not correct, and the derived gloss '\\\"having a king\\\", kingdom' should be dropped in favour of plain 'dominion, kingdom'.\",\n \"derivation_fa\": \"هر سه صورت واقعی‌اند و درست به ریشه بسته شده‌اند، اما دو معنی و یادداشت نمودار نادرست است. اوستایی xšā(y)-/xši- «توانستن، چیرگی داشتن، فرمان راندن» (سوم‌شخص xšayeiti) و پارسی باستان pati-xšaya- «سروری کردن» با سنسکریت kṣáyati هم‌ریشه‌اند و از هندواروپایی آغازین *tkʷeh₁(i)- می‌آیند. اما xšaça- پارسی باستان (که از *xšaθra- ایرانی باستان با تحول آوایی θr > ç پدید آمده) به معنی «شهریاری، کشور، فرمانروایی» است، نه «شاه»؛ واژهٔ پارسی باستان برای «شاه» xšāyaθiya- است. همچنین پسوند -θra/-tra در xšaθra- پسوند سازندهٔ اسم مصدر/ابزار هندوایرانی است (مانند kṣatrá- سنسکریت) و آن‌گونه که یادداشت کتاب می‌گوید پسوند دارندگی («دارندهٔ ...») نیست؛ پس معنی «دارای شاه» پذیرفتنی نیست. با این ملاحظات، ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"%D8%B4%D8%A7%D9%87\", W+\"%D8%B4%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK:626\", \"status\": \"supports\", \"note\": \"See root ref_check: Pokorny p.626-627 lists exactly av. xšayati, ai. kṣatrá-, av./ap. xšaθra-, apers. xšāyaθiya-.\"},\n   {\"ref\": \"KNT:181\", \"status\": \"supports\",\n    \"note\": \"Kent, Old Persian, Lexicon pp.180-182 (KNT.txt leaves 204-205): 'xšaça- sb. ‘kingship, kingdom’: Av. xšaθra-, NPers. šahr ‘city’, Skt. kṣatrá-, pIE *kþetro-, deriv. of root in OP xšay-'; 'xšay- vb. ‘rule’: Av. xšā(y)-, Skt. kṣáyate ‘possesses’, Gk. κτάομαι ... pIE *kþei-'; 'xšāyaθiya- sb. ‘king’ ... to root in OP xšay-'. Note Kent's gloss of xšaça- is 'kingship, kingdom', not 'king, ruler'.\"},\n   {\"ref\": \"SPG:215\", \"status\": \"supports\",\n    \"note\": \"Spiegel, Die altpersischen Keilinschriften (1881), Glossar p.215 (SPG_keilinschriften1881.txt leaf 187): 'Khshatra ... die Herrschaft, das Reich ... aw. khšathram dasselbe'; 'Khshathrapāvan ... der Satrape ... Von khshatra und pā, beschützen'; p.216: 'Khshāyathiya ... König'; 'Khshi ... herrschen. Im Aw. khši, skr. kṣi. + pati: beherrschen ... patiyakhshaiy'. This is evidently where Nourai's pair 'xšây, xši 2' comes from. Spiegel adds that he is unsure whether NP šahr goes back to xšaθra or to šōiθra-; modern work (Horn, MacKenzie, Kent) settles it on xšaθra.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 542-545 and 550-552\", \"stance\": \"supports\",\n    \"note\": \"'j., g. xšaθra-, p. xšaça- n. „imperium, regnum, Herrschaft, Reich“'; 'j., g. (? p.) xšaya- m. „Herrscher, Fürst, König“'; 'j., g., p. xšā(y)- V. „vermögen“ ... „Macht haben, Gewalt haben, herrschen über“'. Bartholomae's gloss for xšaθra- is 'Herrschaft, Reich' — i.e. dominion, never '\\\"having a king\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.504\", \"stance\": \"partial\",\n    \"note\": \"Explicitly calls xšaθra-/kṣatrá- an 'urar. Neubildung zu kṣayati, indem dessen y als Praesenssuffix gefühlt wurde' — i.e. an Indo-Iranian *-tra- noun to the verb, which contradicts the chart's note on the suffix.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH\", \"stance\": \"supports\",\n    \"note\": \"Full paradigm: 'AVESTAN: xšā- ‘to be able; rule, be lord of’ ... OLD PERSIAN: (+ *upari-) upari-xša- ‘to rule over’ || (+ *pati-) pati-xša- ‘to have lordship over’ = Kent: 181a'. Cheung even cites Kent p.181, Nourai's own page.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 19.31-19.32, pp.1319-1322\", \"stance\": \"supports\",\n    \"note\": \"'OPers. xšaça- ‘rule, realm’, Av. xšaya- ‘ruler, king’, OPers. xšāyaθiya- ‘king’' — confirms that xšaça- is 'realm', not 'king'.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"šâh; šěr; šatr\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the three words are right and the third is not. MP šāh 'king' (Book Pahlavi written with the Aramaic ideogram MLKA, Manichaean šh) continues OP xšāyaθiya-: initial xš- had already become š- in Pahlavi (Hübschmann, Pers. Studien p.82 n.2: 'anlaut. xš war schon im Pehlevi zu š geworden') and *xšāyaθiya > *šāhīy > šāh by loss of the intervocalic θ/y and contraction. MP šahr 'land, country; city' (Book Pahlavi štr', which is exactly Nourai's 'šatr'; Manichaean šhr) continues OP xšaça- / Av. xšaθra- 'dominion', with the semantic slide 'dominion' > 'territory, land' > 'city'. But MP šēr 'lion' does NOT belong here: MacKenzie's Concise Pahlavi Dictionary has no entry šēr and refers 'šēr, v. šagr', the Pahlavi word being šagr [šgl], and the English-Pahlavi index gives 'lion šagr'. Hübschmann, on the very page Nourai cites (HUB:83, no. 803), says of Av. xšaθrya-: 'Zd. xšaθrya- ist im Neup. durch šahrī vertreten. Also šēr \\\"Löwe\\\" davon zu trennen' — 'therefore šēr \\\"lion\\\" is to be separated from it'. Wiktionary likewise takes Persian شیر 'lion' from MP šgr /šagr/, a word of separate (and still obscure) origin.\",\n \"derivation_fa\": \"دو واژه از سه واژه درست است و سومی نادرست. فارسی میانهٔ šāh «شاه» (در پهلوی کتابی با هزوارش MLKA) دنبالهٔ xšāyaθiya- پارسی باستان است؛ خوشهٔ آغازین xš در پهلوی به š بدل شده بود (هوبشمان، مطالعات فارسی، ص۸۲ پانویس) و *xšāyaθiya با افتادن θ میان‌واکه‌ای و ادغام به šāh رسیده است. فارسی میانهٔ šahr (نوشتهٔ štr'، همان «šatr» نورایی) دنبالهٔ xšaça- پارسی باستان و xšaθra- اوستایی است با تحول معنایی «فرمانروایی» ← «سرزمین» ← «شهر». اما šēr «شیر (درنده)» به این خانواده تعلق ندارد: مکنزی در فرهنگ کوچک پهلوی مدخل šēr را به šagr [šgl] ارجاع می‌دهد و هوبشمان دقیقاً در همان صفحه‌ای که نورایی به آن ارجاع داده (ص۸۳، شمارهٔ ۸۰۳) می‌نویسد که xšaθrya- اوستایی در فارسی نو «شهری» شده است «پس šēr «شیر» را باید از آن جدا دانست». ویکی‌واژه نیز «شیر» درنده را از šagr فارسی میانه می‌گیرد. بنابراین پژوهش امروزی این جزء از ادعای نورایی را رد می‌کند.\",\n \"sources\": [W+\"%D8%B4%DB%8C%D8%B1\", W+\"%D8%B4%D8%A7%D9%87\", W+\"%D8%B4%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:626\", \"status\": \"not_found\",\n    \"note\": \"Borhan-e Qate' printed p.626 is in volume 2, in the چ section (BQT_v2_pages.txt leaf 86 = چراغ / چراگاه); there is no شاه / شیر / شهر entry anywhere near it. The Borhan pages that do carry Mo'in's notes on this family are ~646-648 (چک), 1237 (شایستن) and 1316 (شهریار، شهریور), all cited elsewhere on this same chart. BQT:626 looks like a slip for POK:626, which stands one box above.\"},\n   {\"ref\": \"HRN:177\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie, no.797 (p.177): 'šahr „Stadt“ ... ap. xšaça- „Reich, Land“; aw. xšaθra-; phlv. šatr, šatrestān; pāz. šahr, šahrastān; ai. kṣatrá-' — this is where Nourai's Pahlavi form 'šatr' comes from. Horn no.772 (p.170) 'šāh „König, Herrscher“ ... ap. xšāyaθiya-'. Horn says nothing here about šēr 'lion'.\"},\n   {\"ref\": \"HUB:83\", \"status\": \"contradicts\",\n    \"note\": \"Hübschmann, Persische Studien p.83, no.803 (HUB.txt leaf 94): 'Zd. xšaθrya- ist im Neup. durch šahrī vertreten. Also šēr „Löwe“ davon zu trennen.' The page Nourai cites explicitly forbids connecting šēr 'lion' with the xšaθra- family.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.79-80\", \"stance\": \"partial\",\n    \"note\": \"'šāh [MLKA < A mlk’; šh | M šh, N ~] king'; 'šahr [štr’ | M šhr, N ~] land, country; city'; but 'šēr, v. šagr' and (English index) 'lion šagr' — supports šāh and šahr, contradicts šēr.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. Artaxšēr, šahr\", \"stance\": \"supports\",\n    \"note\": \"'Artaxšēr = Artaxšahr ... OIr Arta-xšaθra-, cf s. v. Art-vahišt and šahr; OP Arta-xšaça-' — confirms MP šahr < *xšaθra-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH, 'MIDDLE PERSIAN'\", \"stance\": \"supports\",\n    \"note\": \"'MMP šʾy- ‘to rule, have power; be able’, MMP šʾyh- ‘to be king, rule’ ... BMP pʾtxšʾd /pādixšā(y)/ ‘ruler, sovereign’' — the Middle Persian continuation of the root.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"šâh «شاه»; šîr 2 «شیر ۲»; šahr «شهر»; čak «چَک»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Three of the four are right. NP شاه < MP šāh < OP xšāyaθiya-; NP شهر < MP šahr < OP xšaça- / Av. xšaθra-, and the modern sense 'city' is the end of the chain 'dominion > land > town'. NP چَک 'written order, deed, promissory note' is genuinely old: Mo'in's footnote to the چك entry of Borhan-e Qate' (vol.2, ~pp.646-648) states 'معرب آن «صاک» و «شک» و «شاکه» ... در انگلیسی check و در فرانسه chèque؛ در فرهنگ‌های اروپایی ... کلمه را از to check انگلیسی ... گرفته‌اند ... ولی استعمال این کلمه در فارسی قدیم است چنانکه فردوسی بمعنی معاهده و صدیق‌نامه آورده' and quotes the very Šāhnāma line the chart prints. Nourai's implicit claim that چک belongs to the same root as شاه is, however, unsupported by any source — no book consulted derives چک from xšaθra-/xšāyaθiya-; it stands in the box only because the borrowing route to English 'check' happens to run parallel to that of chess. And شیر 'lion' does not belong at all: NP šēr/šir 'lion' < MP šagr, separate from this root (Hübschmann no.803, MacKenzie s.v. šagr, Wiktionary). NP شیر 'milk' is a third, again unrelated, word.\",\n \"derivation_fa\": \"سه واژه از چهار واژه درست است. «شاه» از šāh فارسی میانه و آن از xšāyaθiya- پارسی باستان؛ «شهر» از šahr فارسی میانه و آن از xšaça-/xšaθra- با تحول معنایی «فرمانروایی ← سرزمین ← شهر». «چَک» به معنی «سند، قباله، برات» واژه‌ای کهن است؛ معین در حاشیهٔ برهان قاطع (ج۲، حدود ص۶۴۶ـ۶۴۸) می‌نویسد معرّب آن «صک» است و همان بیت شاهنامه را که نورایی آورده گواه می‌گیرد و تصریح می‌کند که برخلاف فرهنگ‌های اروپایی، این واژه در فارسی قدیم به کار می‌رفته است. با این همه هیچ منبعی «چک» را به ریشهٔ xšaθra- بازنمی‌گرداند و جای آن در این جعبه تنها به سبب هم‌مسیری وام‌گیری با «شاه/شطرنج» است. «شیر ۲» (درنده) نیز به این خانواده تعلق ندارد و از šagr فارسی میانه است. پس ادعای نورایی دربارهٔ «شیر» را پژوهش امروزی رد می‌کند و دربارهٔ «چک» تنها مسیر وام‌گیری آن درست است، نه هم‌ریشگی‌اش با «شاه».\",\n \"sources\": [W+\"%D8%B4%DB%8C%D8%B1\", W+\"%D8%B4%D8%A7%D9%87\", W+\"%D8%B4%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK:626\", \"status\": \"supports\", \"note\": \"Pokorny p.626 explicitly gives 'apers. xšāyaθiya- ... (npers. šāh)'.\"},\n   {\"ref\": \"BQT:648\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol.2, the چك entry with Mo'in's footnote (BQT_v2_pages.txt leaf 106-107, printed ≈646-648 on the +540 offset): 'چك ... بمعنی برات و وظیفه و مواجب ... و منشور - و قبالهٔ خانه و باغ ... معرب آن صك است' and the footnote 'معرب آن «صاک» و «شک» و «شاکه» ... در انگلیسی check و در فرانسه chèque ... ولی استعمال این کلمه در فارسی قدیم است چنانکه فردوسی ... آورده'. Covers چک and the Ferdowsi verse; it says nothing about شیر.\"},\n   {\"ref\": \"ZMA:25\", \"status\": \"not_checked\",\n    \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian (Bonyad-e Neyshabur 1374) — refs_online.json records it as purchase-only, with no open or lending copy.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"nos. 772 (p.170) and 797 (p.177)\", \"stance\": \"supports\",\n    \"note\": \"'šāh „König, Herrscher“ ... ap. xšāyaθiya-' and 'šahr „Stadt“ ... ap. xšaça- „Reich, Land“ ... Allgemein entlehnt'.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. صك ṣakk\", \"stance\": \"supports\",\n    \"note\": \"'ṣakk: „Gerichtsakt“ aus dem pers. čedek > tk. çek, engl. check, frz. chèque. Scheck geht aller Wahrscheinlichkeit nach auf das pers. tschāk „Urkunde, Vertrag“ zurück.' Confirms Persian چک as the source of Arabic صك.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, s.v. شاه (Latin index, pdf p.373)\", \"stance\": \"supports\",\n    \"note\": \"Lists for شاه: Avestan KSI, KSAYATI, KSATRA; Old Persian XSHAYATI, KSHATHRA, XSHAYATHIYA; Pahlavi SHAH, SHATHR; Kurdish SHAH, PADSHAH; references Pokorny, MacKenzie (KING) 120, Buck (RULE) 1319-1321, (KING) 1321-1322. An independent modern Persian handbook agreeing with the chart on شاه/شهر — and it does not list شیر.\"},\n   {\"src\": \"PHD\", \"where\": \"s.v. šagr / šēr\", \"stance\": \"contradicts\",\n    \"note\": \"'šēr, v. šagr'; English index 'lion šagr' — NP شیر 'lion' descends from MP šagr, not from this root.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"(no words printed)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The empty Arabic box is the transmitting stage for both of the words that go on to French and English. (a) Persian شاه entered Arabic unchanged as شاه, and the chess call شاه مات 'the king is māt (helpless/dead)' — with Arabic māta 'he died' reinterpreting Persian māt 'stumped, helpless' — spread with the game from the ʿAbbasid court westwards from the 8th-9th c. (b) Persian چَک 'deed, written order' was arabicised as صَكّ (pl. صِكاك/صُكوك), a standard chancery term of the ʿAbbasid period; Asbaghi lists it among the Persian loanwords in Arabic.\",\n \"derivation_fa\": \"این جعبهٔ خالی مرحلهٔ میانجی عربی است برای هر دو واژه‌ای که به فرانسه و انگلیسی می‌رسند. نخست «شاه» فارسی که بی‌تغییر به عربی رفت و در عبارت شطرنجی «شاه مات» به کار رفت (مات فارسی به معنی «درمانده» در عربی با فعل مات «مرد» یکی گرفته شد) و از سدهٔ دوم و سوم هجری با خود بازی از دربار عباسی به مغرب‌زمین رسید. دوم «چَک» فارسی که در دیوان‌های عباسی به صورت «صَکّ» (جمع: صکوک) معرّب شد؛ اصباغی آن را در شمار وام‌واژه‌های فارسی در عربی آورده است. ادعای نورایی دربارهٔ این مرحله درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/check\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:272\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. check: 'borrowed (through the medium of Spanish and Arabic) fr. Pers. shah, ‘king’ (in the Arab.-Pers. phrase shah mat, ‘the king is dead’)'; and s.v. check/cheque: 'comes fr. Arab. ṣakk, ‘agreement, contract’, fr. Pers. čāk'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PLA\", \"where\": \"s.v. صك ṣakk\", \"stance\": \"supports\",\n    \"note\": \"'ṣakk ... aus dem pers. čedek > tk. çek, engl. check, frz. chèque ... pers. > ar. > lat. > frz.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no.1762 (Pers. šāh)\", \"stance\": \"partial\",\n    \"note\": \"'Aus dem beim Schachspiel üblichen Ausruf: šāh māt entstand allgemein der Name für dieses Spiel: it. scacco, prov. escac, frz. échec ... engl. chess' — supports the Arabic-mediated chess chain, but Lokotsch routes English check/cheque through OF eschec rather than through Arabic ṣakk.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, grepped for صك\", \"stance\": \"silent\",\n    \"note\": \"No entry for صك found in AFM.txt (the only hit for صك is inside the بتك entry, about Aramaic ptqʾ).\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"French\", \"words\": \"(no words printed)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The empty French box stands for Old French eschac/eschec (12th c.) 'check at chess', pl. esches (whence English 'chess'), eschec et mat 'checkmate', eschequier 'chessboard, exchequer' > modern French échec, échecs, échiquier. Old French took the word from Arabic šāh through Spanish/Italian (Sp. jaque, It. scacco), the Vulgar-Latin form being *scaccus. For the money sense, modern French chèque is itself a 19th-c. loan back from English — so on the 'promissory note' branch the French box is chronologically downstream of English, not upstream of it, which is the one weak link in the chart's line.\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ فرانسهٔ باستان eschac/eschec (سدهٔ دوازدهم میلادی) «کیشِ شطرنج» است، جمع آن esches (خاستگاه chess انگلیسی)، و نیز eschec et mat «کیش و مات» و eschequier «صفحهٔ شطرنج»؛ در فرانسهٔ امروز échec، échecs، échiquier. فرانسهٔ باستان این واژه را از عربی شاه و از راه اسپانیایی و ایتالیایی (jaque، scacco) گرفت، با صورت لاتینی عامیانهٔ *scaccus. اما در شاخهٔ «سند/برات»، chèque فرانسوی خودْ وام‌واژه‌ای از انگلیسی در سدهٔ نوزدهم است؛ پس در آن شاخه ترتیبِ نمودار (فرانسه پیش از انگلیسی) وارونه است.\",\n \"sources\": [\"https://www.etymonline.com/word/check\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The book prints no reference on this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no.1762\", \"stance\": \"supports\",\n    \"note\": \"'prov. escac, frz. échec, gewöhnlich échecs ... das „Schachbrett“ heißt danach ... frz. échiquier ... Endlich wurde aus afrz. eschec zur Bezeichnung eines „Zahlscheins“ ... engl. check, frz. chèque.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Check\", \"stance\": \"supports\",\n    \"note\": \"'M.E. chek, a stop; also check! in playing chess ... O.F. eschec, ‘a check at chess-play,’ Cot. — Pers. shāh, a king ... whence shāh-māt, checkmate.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. check, checker, checkmate\", \"stance\": \"supports\",\n    \"note\": \"'ME. chek, fr. OF. eschec (whence F. échec) ... fr. earlier eschac'; 'checker ... shortened fr. OF. eschekier (F. échiquier), ‘chessboard’, fr. ML. scaccarium'.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"check, chess, checkmate\",\n \"verdict\": \"plausible\",\n \"derivation\": \"'Chess' and 'checkmate' are certain: ME ches(se) < OF esches, plural of eschec, and ME chek mat < OF eschec et mat < Arabo-Persian šāh māt; the ultimate source is Persian šāh 'king', so the arrow back to node 3 is right. 'Check' in the chess/stop sense is equally certain (ME chek < OF eschec). The debated word is 'check/cheque' meaning a written order on a bank (1798, often spelt cheque): Nourai routes it through Persian čak > Arabic ṣakk, and that is exactly Klein's view ('Most philologists derive this word from check in the sense ‘a sudden stop’. It is more probable, however, that check ... comes fr. Arab. ṣakk ... fr. Pers. čāk'), shared by Asbaghi and by Mo'in in his Borhan footnote. Etymonline/OED and Lokotsch instead derive it from check 'sudden stoppage', influenced by exchequer. Both camps have standing; the chart follows the minority (Klein) position without saying so.\",\n \"derivation_fa\": \"«chess» و «checkmate» قطعی‌اند: انگلیسی میانهٔ ches از esches فرانسهٔ باستان (جمع eschec) و chek mat از eschec et mat که خود از «شاه مات» عربی‌ـ فارسی است؛ پس پیوند آن‌ها با «شاه» درست است. «check» به معنی «کیش، بازداشتن» نیز از همان eschec است. اما دربارهٔ «check/cheque» به معنی «حواله بر بانک» (۱۷۹۸ م.) اختلاف هست: نورایی آن را از «چک» فارسی و «صکّ» عربی می‌گیرد و این دقیقاً دیدگاه کلاین است («بیشتر زبان‌شناسان این واژه را از check به معنی توقف می‌گیرند، ولی محتمل‌تر آن است که از صکّ عربی و آن از چاک فارسی باشد») و اصباغی و معین نیز همین را می‌گویند؛ در برابر، اتیمآنلاین و آکسفورد و لوکوچ آن را از همان check «توقف» با تأثیر exchequer می‌دانند. هر دو دیدگاه پشتوانه دارند؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/check\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:272\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. check (KLN_1966.txt line 7296) gives both the chess chain and, s.v. check/cheque, the Arab. ṣakk < Pers. čāk derivation — exactly Nourai's two lines.\"},\n   {\"ref\": \"KLN:946\", \"status\": \"supports\",\n    \"note\": \"Klein vol.2 s.vv. mat / mate / matador (KLN_1966.txt line 23103): 'mat ... fr. Arab. māt in the sentence māt ash-shāh, ‘the king has died’. The word māt, orig. used only as a term of chess ... See checkmate.' This is the 'M.v.t' cross-reference on the box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Check, Shah\", \"stance\": \"supports\",\n    \"note\": \"'The orig. sense of check was ‘king’, i.e. mind the king, the king is in danger'; 'Shah, king of Persia. (Pers.) Pers. shāh, a king. See Check.'\"},\n   {\"src\": \"LKT\", \"where\": \"no.1762\", \"stance\": \"contradicts\",\n    \"note\": \"On the money word Lokotsch says 'Endlich wurde aus afrz. eschec zur Bezeichnung eines „Zahlscheins“ ... engl. check, frz. chèque, dtsch. Scheck' — i.e. from šāh via eschec, not from čak/ṣakk.\"},\n   {\"src\": \"PLA\", \"where\": \"s.v. صك ṣakk\", \"stance\": \"supports\",\n    \"note\": \"'Scheck geht aller Wahrscheinlichkeit nach auf das pers. tschāk „Urkunde, Vertrag“ zurück ... pers. > ar. > lat. > frz.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. tḱē-\", \"stance\": \"supports\",\n    \"note\": \"Lists CHECK, SHAH, CHECKMATE among the English descendants of the root (via Old Persian khshayathiya-).\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Avestan\",\n \"words\": \"arta-xšatra; paiti-xšatra; xšathra-vairya; xšathra-dâra; xšatra-pavan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All five compounds are real, but the language label is only half right and two of the analyses are loose. Genuinely Avestan are xšaθra- vairya- 'the Desirable Dominion' (an Amǝša Spǝnta and the name of the 6th month and 4th day; vairya- is the verbal adjective of var- 'to choose', so 'chosen, desirable' — Nourai's 'choice kingdom' is accurate) and *xšaθrō.dāra- 'holder of the realm' (Horn's reconstruction behind Pahlavi inscriptional šatrdārān). The other three are Old Persian, not Avestan: Arta-xšaça- (Kent; = Av. *Arta-xšaθra-) 'whose dominion is through Arta/Truth' (Nyberg: 'he whose dominion is determined by the divine law'), so 'just king' is a paraphrase rather than a translation; xšaça-pāvan- 'protector of the realm' (Kent p.181, with pā- 'to protect' + -van-), the source of Greek satrapēs; and 'paiti-xšatra' — the actual form is OP *pati-xšāya- (Horn no.266: 'ap. *pati-xšāyaθiya-'; Cheung: OP pati-xša- 'to have lordship over'; MP pādixšā(y) 'ruler, authoritative'), so the second element is xšāya- 'ruling', not xšaθra- 'kingdom', and pati- means 'over, chief', not 'protecting'.\",\n \"derivation_fa\": \"هر پنج ترکیب واقعی‌اند، اما برچسب زبانی تنها نیمه‌درست است و دو تحلیل نیز مسامحه‌آمیز. به‌راستی اوستایی‌اند: xšaθra- vairya- «شهریاری برگزیده» (یکی از امشاسپندان و نام ششمین ماه و چهارمین روز؛ vairya- از ریشهٔ var- «برگزیدن») و *xšaθrō.dāra- «دارندهٔ شهریاری» که هرن آن را در پس šatrdārān کتیبه‌های پهلوی بازسازی کرده است. سه ترکیب دیگر پارسی باستان‌اند نه اوستایی: Arta-xšaça- «آن‌که شهریاری‌اش بر پایهٔ اَرته (راستی) است» (نیبرگ)، پس «شاه دادگر» تعبیر آزاد است نه ترجمه؛ xšaça-pāvan- «نگاهبان کشور» (کنت، ص۱۸۱) که خاستگاه satrapēs یونانی است؛ و «paiti-xšatra» که صورت درستش *pati-xšāya- است (هرن، شمارهٔ ۲۶۶؛ چونگ: pati-xša- پارسی باستان «سروری کردن»؛ pādixšā(y) فارسی میانه)، پس جزء دوم xšāya- «فرمانروا» است نه xšaθra- «کشور»، و pati- به معنی «بر، سر-» است نه «نگاهدارنده». با این ملاحظات ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/satrap\", W+\"%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:100\", \"status\": \"not_found\",\n    \"note\": \"Horn p.100 (HRN.txt leaf 122) is nos. 448-451: kušk?, čōgān 'polo stick', čun, či — nothing to do with these compounds. The Horn entries that do support this box are no.266 pādišāh (p.61) and nos. 797-798 šahr / šahryār (p.177). HRN:100 appears to be a wrong page number.\"},\n   {\"ref\": \"HRN:177\", \"status\": \"supports\",\n    \"note\": \"Horn no.798 (p.177): 'šahryār „Herrscher“. aw. *xšaθrō.dāra-; phlv. (Inschr.) šatrdārān.' — exactly the chart's 'xšathra-dâra'.\"},\n   {\"ref\": \"KLN:1110\", \"status\": \"partial\",\n    \"note\": \"Klein s.v. padishah: 'Turk. padishah, fr. Pers. padshah, which is compounded of pad, ‘master’, and shah, ‘king’. The first element is rel. to OPers. pati, Avestic paiti-, OI. patiḥ, ‘master, husband’.' Klein has the same first element paiti-, but the second element is šāh (< xšāya-), not xšaθra-, and 'master' rather than 'protecting'.\"},\n   {\"ref\": \"KLN:1386\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. satrap: 'fr. Gk. σατράπης, ἐξατράπης, fr. OPers. xshathrapavan-, ‘ruler of the province’, compounded of xshathra-, ‘province’, and a derivative of pā(y)-, ‘to guard, protect’.'\"},\n   {\"ref\": \"BQT:1316\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p.1316 (vol.3, pdf p.107), Mo'in's footnotes: 'شهریار ... پهلوی shahrdār ... و xshathradar (نگاهبان شهر). از shathr (شهر) + dār (از: داشتن) ... اوستا xshathrō.dāra ... شهریار Shatrdārān (کتیبه‌ها)'; and 'در اوستا xshathra vairya، پهلوی shatrivar، مرکب از xshathra که در اوستا و پارسی باستان و سانسکریت بمعنی کشور و پادشاهی است (رک: شهر) و جزو دوم ... از var- بمعنی برگزیدن ... پس ترکیب یعنی کشور منتخب یا پادشاهی برگزیده'. Precisely the two Avestan compounds of this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.181\", \"stance\": \"supports\",\n    \"note\": \"'xšaça-pāvan- sb. ‘satrap’: Gk. σατράπης; xšaça- + root pā- ‘protect’ + suffix -van-'; the same lexicon has Artaxšaça- and *pati-xšaya-.\"},\n   {\"src\": \"BRT\", \"where\": \"cols. 542-546 s.v. xšaθra-; col. 12899 darəγō.xšaθra-\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae has 'xšaθrəm vairīm yazamaide' and 'xšaθrahe vairyehe' as the name of the 6th month and 4th day — confirming xšaθra- vairya- as a genuine Avestan compound.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, s.v. Artaxšēr / Art-vahišt\", \"stance\": \"supports\",\n    \"note\": \"'OIr Arta-xšaθra-, ... OP Arta-xšaça-; ... NP Ardašīr'; s.v. Art-vahišt: 'Arta-xšahr „he whose dominion is (determined) by the divine law“'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.79, 68\", \"stance\": \"supports\",\n    \"note\": \"'šahrewar [štrywr] Best Rule, the third Amahraspand ... cal. 6th month; 4th day'; 'šahryār [štrdʾl] lord, sovereign, ruler'; 'pādixšā(y) [ŠLYTA < A šlyṭ; pʾtxšʾ(d) | M pʾtxšʾ] ruler; powerful, authoritative, authorized'.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\",\n \"words\": \"ardešîr «اردشیر»; pâdešâh «پادشاه»; šahrîvar «شهریور»; šahrdâr «شهردار» (+ شهریار)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Each of the four Persian words does continue the compound the chart puts above it. اردشیر < MP Ardaxšīr / Artaxšēr < OP Artaxšaça- (Nyberg: 'Artaxšēr ... OIr Arta-xšaθra-; OP Arta-xšaça- ... NP Ardašīr'), the Greek transcriptions Ἀρταξέρξης showing the same name. پادشاه < MP pādixšāy/pādixšāh < OIr. *pati-xšāya- 'ruling over' (the -h of pādšāh being reinforced by شاه); Horn no.266 'ap. *pati-xšāyaθiya-; phlv. pātaxšā(h)'. شهریور < MP šahrewar < Av. xšaθra- vairya-, the Amǝša Spǝnta and the 6th month of the Zoroastrian year, so the gloss 'desired kingdom' is right. شهریار < MP šahryār < *xšaθrō.dāra- (Horn no.798; Pahlavi inscriptional šatrdārān); شهردار 'mayor' is a modern administrative coinage on the same two elements (شهر + دار) rather than an inherited form, which is why the book prints it with شهریار in brackets beside it.\",\n \"derivation_fa\": \"هر چهار واژهٔ فارسی به‌راستی دنبالهٔ همان ترکیب بالای خود هستند. «اردشیر» از Ardaxšīr/Artaxšēr فارسی میانه و آن از Arta-xšaça- پارسی باستان (نیبرگ)؛ صورت یونانی Ἀρταξέρξης همان نام است. «پادشاه» از pādixšāy/pādixšāh فارسی میانه و آن از *pati-xšāya- ایرانی باستان (هرن، شمارهٔ ۲۶۶: «pātaxšā(h) پهلوی»)، که پایانهٔ آن در فارسی نو زیر تأثیر «شاه» به -شاه بدل شده است. «شهریور» از šahrewar فارسی میانه و آن از xšaθra- vairya- اوستایی، نام امشاسپند و ششمین ماه سال، پس معنی «شهریاری برگزیده» درست است. «شهریار» از šahryār فارسی میانه و آن از *xšaθrō.dāra-؛ اما «شهردار» ساختی نو (شهر + دار) است نه صورتی موروثی، و به همین سبب کتاب «شهریار» را در کنار آن در کمانک آورده است. ادعای نورایی درست است.\",\n \"sources\": [W+\"%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87\", W+\"%D8%B4%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p.1316 (vol.3 pdf 107) carries Mo'in's footnotes on both شهریار (پهلوی shahrdār / xshathradār، اوستا xshathrō.dāra، شهریار Shatrdārān کتیبه‌ها) and شهریور (اوستا xshathra vairya، پهلوی shatrivar) — see node 7.\"},\n   {\"ref\": \"ETM:67\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374 — refs_online.json: no digital copy on any permitted platform, catalogue/purchase only.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. Artaxšēr\", \"stance\": \"supports\",\n    \"note\": \"'Artaxšēr ... = Artaxšahr ... OIr Arta-xšaθra- ... OP Arta-xšaça-; ... NP Ardašīr. Cf. Bailey, BSOAS XIII, 1949, 123.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp.68, 79\", \"stance\": \"supports\",\n    \"note\": \"'pādixšā(y) ... ruler; powerful, authoritative, authorized'; 'šahrewar ... Best Rule, the third Amahraspand ... cal. 6th month; 4th day'; 'šahryār ... lord, sovereign, ruler'.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 266 (p.61) and 798 (p.177)\", \"stance\": \"supports\",\n    \"note\": \"'pādišāh „König“. ap. *pati-xšāyaθiya-; phlv. pātaxšā bezw. pātaxšah'; 'šahryār „Herrscher“. aw. *xšaθrō.dāra-; phlv. (Inschr.) šatrdārān.'\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Greek\", \"words\": \"sâtrâpěs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek σατράπης (also ἐξατράπης, ξατράπης in the older inscriptions and in Xenophon) is a 5th-c. BCE borrowing of the Old Persian/Median administrative title xšaça-pāvan- (Median *xšaθrapāvan-) 'protector of the realm'; the alien initial cluster xš- was rendered ἐξ- or simply σ-, and the Iranian -pāvan- gave -πης through the stem -πα(F)ν-. Herodotus uses the noun and its derivatives for the governors of the Achaemenid provinces. The arrow from the compound in node 7 is exactly right — except that the source is Old Persian/Median, not Avestan as the parent box is labelled.\",\n \"derivation_fa\": \"واژهٔ یونانی σατράπης (و صورت‌های کهن‌تر ἐξατράπης و ξατράπης نزد گزنفون و در کتیبه‌ها) وام‌واژه‌ای است از سدهٔ پنجم پیش از میلاد از عنوان دیوانی پارسی باستان/مادی xšaça-pāvan- (مادی *xšaθrapāvan-) «نگاهبان کشور». خوشهٔ آغازین xš که در یونانی ناآشنا بود به ἐξ- یا تنها σ- بدل شد و جزء ایرانی -pāvan- به -πης انجامید. هرودوت این واژه را دربارهٔ فرمانداران ساتراپی‌های هخامنشی به کار برده است. ادعای نورایی درست است؛ تنها باید افزود که خاستگاه پارسی باستان (یا مادی) است نه اوستایی.\",\n \"sources\": [\"https://www.etymonline.com/word/satrap\"],\n \"ref_check\": [\n   {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi — not available in any digital form (refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.181\", \"stance\": \"supports\",\n    \"note\": \"'xšaçapāvan- sb. ‘satrap’: Gk. σατράπης; xšaça- + root pā- ‘protect’ + suffix -van- ... xšaçapāvā nsm. DB 3.14, 56.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. satrap\", \"stance\": \"supports\",\n    \"note\": \"'ME., fr. L. satrapes, fr. Gk. σατράπης, ἐξατράπης, fr. OPers. xshathrapavan-, ‘ruler of the province’.'\"},\n   {\"src\": \"SPG\", \"where\": \"Spiegel, Keilinschriften, Glossar p.215\", \"stance\": \"supports\",\n    \"note\": \"'Khshathrapāvan ... der Satrape nom. khshathrapāvā Bh. III, 14. 55. Von khshatra und pā, beschützen.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.79 s.v. šasab\", \"stance\": \"partial\",\n    \"note\": \"'šasab [šhrp | (P šhrb)] satrap' — shows that the title also had an inherited Middle Persian continuation, independent of the Greek line.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"French\", \"words\": \"satrape\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French satrape is a learned borrowing (attested from the 14th c.) of Latin satrapes/satrapa, itself from Greek σατράπης; the word enters the western European languages as a term of ancient history and is then extended figuratively to 'petty despot, autocratic official'. English satrap follows the same Latin-French route in the late 14th c.\",\n \"derivation_fa\": \"«satrape» فرانسوی وام‌واژه‌ای کتابی است (از سدهٔ چهاردهم میلادی) از لاتینی satrapes/satrapa و آن از σατράπης یونانی. این واژه نخست همچون اصطلاحی تاریخی وارد زبان‌های اروپای غربی شد و سپس معنی مجازی «فرمانروای خودکامهٔ کوچک» یافت. «satrap» انگلیسی نیز از همین راه لاتینی‌ـ فرانسوی در اواخر سدهٔ چهاردهم وارد شده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/satrap\"],\n \"ref_check\": [\n   {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi — no accessible copy.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. satrap\", \"stance\": \"supports\", \"note\": \"'ME., fr. L. satrapes, fr. Gk. σατράπης' — the Latin stage that French satrape shares.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Satrap\", \"stance\": \"supports\", \"note\": \"'Satrap, a Persian viceroy. (F.-L.-Gk.)' — Skeat's formula 'French from Latin from Greek' is exactly this chain.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"sâtrâp «ساتراپ»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Modern Persian ساتراپ is a 20th-c. learned re-borrowing from European (French/English) usage, adopted with the rise of Persian scholarship on the Achaemenids; it is not an inherited word, and the chart is right to draw it from the French box rather than from Old Persian. It is therefore a complete round trip: OP xšaça-pāvan- > Greek > Latin > French > New Persian. Worth adding that Persian did keep an inherited descendant of the same title in Middle Persian šasab / šahrab 'satrap' (MacKenzie), which ساتراپ has not replaced but simply post-dates.\",\n \"derivation_fa\": \"«ساتراپ» در فارسی امروز وام‌واژه‌ای کتابی از سدهٔ چهاردهم خورشیدی است که همراه با رواج پژوهش‌های هخامنشی از فرانسه/انگلیسی گرفته شده است؛ واژه‌ای موروثی نیست و نمودار به‌درستی آن را از جعبهٔ فرانسه گرفته است. بدین‌سان یک چرخهٔ کامل پدید آمده: xšaça-pāvan- پارسی باستان ← یونانی ← لاتینی ← فرانسوی ← فارسی نو. افزون بر این، دنبالهٔ موروثی همین عنوان در فارسی میانه به صورت šasab/šahrab «ساتراپ» بازمانده است (مکنزی). ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/satrap\"],\n \"ref_check\": [\n   {\"ref\": \"ETM:67\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi — no accessible copy.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.79\", \"stance\": \"partial\",\n    \"note\": \"'šasab [šhrp | (P šhrb)] satrap. ~agān [-ygʾn] satrapal' — the inherited Middle Persian form, showing that ساتراپ cannot be a direct continuation.\"},\n   {\"src\": \"MON\", \"where\": \"grepped MON_part1/2 and the Adena 2-vol djvu for ساتراپ\", \"stance\": \"silent\",\n    \"note\": \"No hit; the word is absent from the searchable Mo'in text on disk (it is a modern technical term).\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Avestan\", \"words\": \"xšâya-aršân\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The compound is real and correctly analysed, but it is Old Persian, not Avestan: Xšayāršan- is the royal name attested in the inscriptions of Xerxes I (r. 486-465 BCE), Bartholomae listing it under 'p.' (altpersisch) and Kent under Xšayāršan-. It is xšaya- 'ruling' (to xšay-) + aršan- 'male, man, hero': Bartholomae 'eigentlich „der aršan- (‘Hengst, Held’) unter den Herrschern“; vgl. ai. rājarṣabha-'; Kent 'Hero among Kings'; Watkins glosses it 'ruling men'. So Nourai's 'king of men' is a fair rendering, and the cross-reference to his root 'Eres 1' (aršan-) is right; only the language label should read Old Persian.\",\n \"derivation_fa\": \"این ترکیب واقعی است و تحلیل آن هم درست، اما پارسی باستان است نه اوستایی: Xšayāršan- نام شاهانه‌ای است که در کتیبه‌های خشایارشا (۴۸۶ـ۴۶۵ پیش از میلاد) آمده و بارتولومه آن را با نشانهٔ «p.» (پارسی باستان) و کنت در واژه‌نامهٔ خود ثبت کرده‌اند. ساخت آن xšaya- «فرمانروا» (از ریشهٔ xšay-) + aršan- «نر، مرد، پهلوان» است؛ بارتولومه: «در اصل یعنی aršan (نریان، پهلوان) در میان فرمانروایان»، کنت: «پهلوان در میان شاهان»، واتکینز: «فرمان‌راننده بر مردان». پس ترجمهٔ نورایی «شاه مردان» پذیرفتنی است و ارجاع او به ریشهٔ «Eres 1» (aršan-) درست؛ تنها برچسب زبان باید «پارسی باستان» باشد.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/tek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1480\", \"status\": \"not_checked\",\n    \"note\": \"AHD:1480 is a page of the body of the American Heritage Dictionary, New College Edition (1975), which is not among the local scans (the Watkins appendix on disk is the 1985 standalone reprint). The corresponding appendix entry, tḱē-, was checked and supports the root; and Watkins' introductory essay (p.102 of the 1985 ed.) names 'Old Persian names like Xerxes, ‘ruling men’' as a model Indo-European compound.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.181\", \"stance\": \"supports\",\n    \"note\": \"'Xšayāršan- sb. ‘Xerxes’: Elam. ik-še-ir-iš-ša, Akk. ḫi-ši-’-ar-ša, Gk. Ξέρξης: from xšaya- ‘king’, Av. xšaya-, to root xšay-, + aršan- ‘male’: ‘Hero among Kings’, cf. Skt. rāja-ṛṣabha- (Bthl. AiW 550).'\"},\n   {\"src\": \"BRT\", \"where\": \"col. 551 s.v. Xšayāršan-\", \"stance\": \"supports\",\n    \"note\": \"'p. Xšayāršan- m. EN. eines persischen Königs, Xerxes, Sohns Darius I ... Komp.: xšayā-+aršan-; eig. „der aršan- (‘Hengst, Held’) unter den Herrschern“; vgl. ai. rājarṣabha- m.' Note Bartholomae's language tag is 'p.' = Old Persian.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.504\", \"stance\": \"supports\", \"note\": \"'ap. xšayaθiya- „im Besitz der Herrschergewalt“ ... Xšayāršan „Xerxes“.'\"},\n   {\"src\": \"SPG\", \"where\": \"Spiegel, Keilinschriften, Glossar p.216\", \"stance\": \"partial\",\n    \"note\": \"'Khshayārshā n. pr. Xerxes ... Der erste Theil des Wortes stammt entschieden vom aw. khši „können, mächtig sein“, der letzte Theil mag aršan „Auge“ ... oder aršan „Mann“ sein, doch ist dies nicht ganz sicher.' Spiegel (1881) still hesitated over the second element; Bartholomae and Kent settled it on aršan- 'male, hero'.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"xašâyâr «خشایار»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"خشایار (fuller خشایارشا) is the modern Persian form of Old Persian Xšayāršā, and the gloss 'king of men' repeats the correct analysis of the Old Persian name. But it is not an inherited word: the Sasanian and Islamic tradition preserved no memory of Xerxes (the Šāhnāma has no such king), and خشایارشا/خشایار entered Persian only after the decipherment of the cuneiform inscriptions in the 19th c., becoming a common given name in the 20th. So the arrow from the Old Persian compound is right in substance but represents a scholarly restoration, not a continuous Middle-to-New Persian transmission.\",\n \"derivation_fa\": \"«خشایار» (صورت کامل‌تر: خشایارشا) برگردان فارسی امروزین نام پارسی باستان Xšayāršā است و معنی «شاه مردان» همان تحلیل درست نام پارسی باستان است. اما این واژه موروثی نیست: سنت ساسانی و اسلامی هیچ خاطره‌ای از خشایارشا نگاه نداشته بود (در شاهنامه چنین شاهی نیست) و «خشایارشا/خشایار» تنها پس از خوانده‌شدن کتیبه‌های میخی در سدهٔ نوزدهم به فارسی راه یافت و در سدهٔ بیستم نام خاص رایجی شد. پس پیوندی که نمودار می‌کشد از نظر محتوا درست است ولی بازسازی علمی است، نه تحول پیوستهٔ فارسی میانه به فارسی نو. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/tek-\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"not_checked\",\n    \"note\": \"The chart gives no page for BQT here; Borhan-e Qate' is a 17th-c. dictionary of classical Persian and would not be expected to have خشایار as a headword (the Achaemenid names entered Persian only in the 19th-20th c.).\"},\n   {\"ref\": \"ZFS:52\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Zaban-e Farsi va Sargozasht-e An (Hirmand 1375) — refs_online.json: nothing digitised on any permitted platform.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Lexicon p.181-182\", \"stance\": \"supports\",\n    \"note\": \"Full Old Persian paradigm Xšayāršā / Xšayāršam / Xšayāršahyā, with the etymology 'from xšaya- ‘king’ + aršan- ‘male’'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 551\", \"stance\": \"supports\", \"note\": \"'p. Xšayāršan- ... EN. eines persischen Königs, Xerxes'.\"},\n   {\"src\": \"MON\", \"where\": \"grepped the Mo'in text on disk\", \"stance\": \"silent\",\n    \"note\": \"No etymological note on خشایار found in the searchable Mo'in files; the name belongs to vols 5-6 (aʿlām), which are not on disk.\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Greek\", \"words\": \"xerexes\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Greek name is Ξέρξης, Xérxēs (gen. Ξέρξου); no Greek form 'xerexes' exists. The printed page of the book itself reads 'xerexes' (I rendered PDF page 278 at 200 dpi and read it), so this is Nourai's own misprint and the JSON extraction is faithful. The word itself is right where the chart puts it: Ionian Greek took over Old Persian Xšayāršā in the early 5th c. BCE, rendering the initial cluster xš- as ξ- and adding the Greek masculine -ης; it appears in Aeschylus' Persians (472 BCE) and throughout Herodotus. The gloss is also right: Xerxes I invaded Greece in 480 BCE (Thermopylae, Salamis).\",\n \"derivation_fa\": \"نام یونانی Ξέρξης (Xérxēs) است و صورتی به شکل «xerexes» در یونانی وجود ندارد. خودِ صفحهٔ چاپی کتاب (صفحهٔ ۲۷۸ پی‌دی‌اف، که آن را با تفکیک ۲۰۰ نقطه بر اینچ تصویر و خوانده‌ام) «xerexes» دارد؛ پس این خطای چاپی کتاب است و خوانش اسکن درست انجام شده. خودِ پیوند درست است: یونانی ایونی در آغاز سدهٔ پنجم پیش از میلاد نام پارسی باستان Xšayāršā را گرفت، خوشهٔ آغازین xš را به ξ بدل کرد و پایانهٔ مذکر -ης افزود؛ این نام در نمایش‌نامهٔ «پارسیان» آیسخولوس (۴۷۲ پ.م.) و سراسر تاریخ هرودوت آمده است. معنی‌ای هم که کتاب داده درست است: خشایارشای یکم در ۴۸۰ پ.م. به یونان لشکر کشید.\",\n \"error_in\": \"book\",\n \"book_prints\": \"xerexes\",\n \"correct_form\": \"Xérxēs (Ξέρξης)\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/tek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1400\", \"status\": \"not_checked\",\n    \"note\": \"A page of the body of the AHD New College Edition (1975), not among the local scans; the Watkins appendix on disk has no page numbering of that dictionary. The 1985 Watkins introduction (p.102) does name 'Old Persian names like Xerxes, ‘ruling men’'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Ahasuerus / Xerxes\", \"stance\": \"supports\",\n    \"note\": \"'Heb. Ahashwerosh ... fr. OPers. Xshayārshan- (whence also Gk. Ξέρξης)'. Klein spells the Greek Ξέρξης.\"},\n   {\"src\": \"KNT\", \"where\": \"Lexicon p.181\", \"stance\": \"supports\",\n    \"note\": \"'Xšayāršan- sb. ‘Xerxes’: Elam. ik-še-ir-iš-ša, Akk. ḫi-ši-’-ar-ša, Gk. Ξέρξης'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. Artaxšēr\", \"stance\": \"supports\",\n    \"note\": \"'the common Gr. Ἀρταξέρξης is influenced by Ξέρξης' — again the form Ξέρξης, never *Ξερεξης.\"},\n   {\"src\": \"BOOK\", \"where\": \"printed page 278 of the dictionary, rendered to data/verification/sources/refs/ocr/BOOK/278.png\", \"stance\": \"supports\",\n    \"note\": \"The printed Greek box reads 'xerexes : a king of Persia who invaded Greece 480 BC' and the English box 'Xerexes' — the extraction reproduces the page exactly.\"}\n ]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"Xerexes\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The English name is Xerxes, taken from Latin Xerxes < Greek Ξέρξης; the spelling 'Xerexes' printed here is the same misprint as in the Greek box above, and the extraction is faithful to the page. Otherwise the arrow is correct: English has the name only through the classical historians, which is why it keeps the Greek shape rather than any Iranian one, and Hebrew Ahašwērōš (Ahasuerus of the Book of Esther) is the parallel Semitic borrowing of the same Old Persian name.\",\n \"derivation_fa\": \"صورت انگلیسی این نام Xerxes است که از لاتینی Xerxes و آن از Ξέρξης یونانی گرفته شده؛ املای «Xerexes» در این جعبه همان خطای چاپی جعبهٔ یونانی است و خوانش اسکن با صفحهٔ چاپی مطابقت دارد. جز این، پیوند درست است: انگلیسی این نام را تنها از راه تاریخ‌نگاران کلاسیک می‌شناسد و به همین سبب صورت یونانی آن را نگاه داشته است؛ «اَحَشوِروش» عبری (اخشورش کتاب استر) نیز وام‌گیری موازی سامی از همان نام پارسی باستان است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"Xerexes\",\n \"correct_form\": \"Xerxes\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/tek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"No page given; the AHD New College Edition body is not among the local scans. The Watkins appendix root tḱē- (checked, supports) is the part of AHD that is on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. Ahasuerus\", \"stance\": \"supports\",\n    \"note\": \"'Heb. Ahashwerosh ... fr. OPers. Xshayārshan- (whence also Gk. Ξέρξης)' — Klein's headword spelling of the English name is Xerxes.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, introductory essay p.102\", \"stance\": \"supports\",\n    \"note\": \"'Old Persian names like Xerxes, “ruling men”, are all compounds' — the English form is Xerxes.\"},\n   {\"src\": \"BOOK\", \"where\": \"printed page 278 (data/verification/sources/refs/ocr/BOOK/278.png)\", \"stance\": \"supports\",\n    \"note\": \"The printed English box reads 'Xerexes'; the JSON matches the page, so the fault is the book's.\"}\n ]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"Pahlavi\", \"words\": \"šâyîtan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian šāy- 'to be able, be fitting, be worthy' continues Old Iranian *xšāya- (Av. xšay- 'to have power, be able'), with the usual Pahlavi loss of the initial x- before š. The standard infinitive is šāyistan (MacKenzie: 'šāyistan, šāy- [šʾd-stn’ | M šʾy-, N ~] be able; be worthy'; Nyberg: 'Av. xšay- ‘to have power’; MPrs šyd ‘it is possible’; MPrth šh- ‘to be able’'), and Abolghasemi analyses the past stem šāyist as a secondary formation made from the present stem. Nourai's form šāyītan is not an invention: Mo'in's footnote in Borhan-e Qate' p.1237 gives precisely 'پهلوی shâyîtan – shâyistan (توانستن، قادر بودن)' as a pair, and Nourai copies Mo'in's own transliteration letter for letter.\",\n \"derivation_fa\": \"ستاک šāy- فارسی میانه به معنی «توانستن، سزاوار بودن، شایسته بودن» دنبالهٔ *xšāya- ایرانی باستان (اوستایی xšay- «توانستن، چیرگی داشتن») است، با افتادن x آغازین پیش از š که در پهلوی قاعده است. صورت مصدری رایج šāyistan است (مکنزی: «šāyistan, šāy- توانستن، شایسته بودن»؛ نیبرگ: «اوستایی xšay-؛ فارسی میانه šyd؛ پارتی šh-»)، و ابوالقاسمی ستاک گذشتهٔ šāyist را ساختی ثانوی از ستاک حال می‌داند. صورت šāyītan که نورایی آورده ساختگی نیست: معین در حاشیهٔ برهان قاطع ص۱۲۳۷ دقیقاً می‌نویسد «پهلوی shâyîtan – shâyistan (توانستن، قادر بودن)» و نورایی همان آوانگاری معین را واژه به واژه برداشته است. ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B4%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:171\", \"status\": \"supports\",\n    \"note\": \"Horn no.774 (p.171): 'šāyisten „sich ziemen, können“, Praes. šāyed (Impersonal). aw. xšay-, xšayeite „im Stande sein, vermögen“; phlv. šāy(i)stan, šāyat; lat. queō.'\"},\n   {\"ref\": \"FFD:62\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi, Feʿl-hā-ye Fārsi-ye Dari (FFD_pages.txt, pdf page 67 = printed p.62): 'شایستن: شایست < فارسی میانه šāyist، مادهٔ ماضی جعلی و از مادهٔ مضارع ساخته شده است. شای < فارسی میانه šāy < ایرانی باستان *xšāy-a- ... šāy صورت بالاندهٔ ریشهٔ xšā(y)- و آن به معنی «توانا بودن» است.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.79\", \"stance\": \"supports\",\n    \"note\": \"'šāyistan, šāy- [šʾd-stn’ | M šʾy-, N ~] be able; be worthy. šāyēd [šʾ(d)yt’ | N šāyad] one can, it is possible. šāyendag [šʾdyndk’] able, worthy.'\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. šāyistan\", \"stance\": \"supports\",\n    \"note\": \"'Av. (551 sq.) xšay- ‘to have power’; MPrs šyd ‘it is possible’ (A-H II); MPrth šh- ‘to be able’; Paz. šāy...'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH\", \"stance\": \"supports\",\n    \"note\": \"'MIDDLE PERSIAN: MMP šʾy- ‘to rule, have power; be able/worth/worthy [+ inf.]’ ... BMP šʾy- /šāy-/ ‘to be able, possible; to be worthy’ ... NWIR: NP šāyistan/šāy- ‘to be appropriate’.'\"},\n   {\"src\": \"BQT\", \"where\": \"p.1237, Mo'in's footnote\", \"stance\": \"supports\",\n    \"note\": \"'شایستن ـ بکسر سوم، پهلوی shâyîtan – shâyistan (توانستن، قادر بودن)، از ریشهٔ اوستایی xshây (توانستن) (رک: شاه، شهر)' — saved as data/verification/sources/refs/ocr/BQT/1237.vision.txt.\"}\n ]\n})\n\nN.append({\n \"id\": 17, \"lang\": \"Persian\", \"words\": \"šâyestan «شایستن» (+ شایسته، شایان، شایگان، شاید)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP شایستن 'to be fitting, to deserve, to be worthy' (present stem شای-) is the direct continuation of MP šāyistan/šāy-, and Mo'in's footnote in Borhan-e Qate' p.1237 traces it to 'ریشهٔ اوستایی xšāy (توانستن)' with a cross-reference to شاه and شهر — i.e. to exactly the root of this chart. The four extra forms the book adds are all built on the same stem: شایسته (past participle > adjective 'worthy'), شایان (present participle in -ān 'befitting'), شایگان (< MP šāyagān 'royal, fit for a king', with the adjectival -gān), and شاید (3sg. present, impersonal 'it is possible, perhaps'), which Cheung glosses 'NP šāyad ‘perhaps’ (< ‘it is fitting’)'.\",\n \"derivation_fa\": \"«شایستن» فارسی نو (ستاک حال: شای-) دنبالهٔ مستقیم šāyistan/šāy- فارسی میانه است، و معین در حاشیهٔ برهان قاطع ص۱۲۳۷ آن را به «ریشهٔ اوستایی xšāy (توانستن)» بازمی‌گرداند و به «شاه» و «شهر» ارجاع می‌دهد؛ یعنی درست به همان ریشهٔ این نمودار. چهار صورت افزودهٔ کتاب همگی بر همین ستاک ساخته شده‌اند: «شایسته» (اسم مفعول و سپس صفت)، «شایان» (اسم فاعل با پسوند -ان)، «شایگان» (از šāyagān فارسی میانه «درخور شاه، شاهانه» با پسوند -گان) و «شاید» (سوم‌شخص مفرد حال، بی‌شخص: «رواست، شاید»)، که چونگ آن را چنین معنی می‌کند: «شاید فارسی نو «احتمالاً» < «سزاوار است»». ادعای نورایی درست است.\",\n \"sources\": [W+\"%D8%B4%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1237\", \"status\": \"supports\",\n    \"note\": \"The headword شایستن with Mo'in's footnote is on Borhan p.1237 exactly as cited (BQT vol.3, pdf p.28; page image and my transcription saved as data/verification/sources/refs/ocr/BQT/1237.png and 1237.vision.txt): 'شایستن ـ بکسر سوم، پهلوی shâyîtan – shâyistan (توانستن، قادر بودن)، ازریشهٔ اوستایی xshây (توانستن) (رک: شاه، شهر) «بارتولمه ۵۵۱» ... سزاوار بودن، لایق و مناسب بودن'. The same page carries شایان and شایسته, two of the four extra forms.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.79\", \"stance\": \"supports\",\n    \"note\": \"'šāyistan, šāy- ... be able; be worthy. šāyēd ... | N šāyad] one can, it is possible' — MacKenzie himself equates the Pahlavi form with NP šāyad.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH, 'NWIR'\", \"stance\": \"supports\",\n    \"note\": \"'NP šāyistan/šāy- ‘to be appropriate’ ... (impers.) NP šāyad ‘perhaps’ (< ‘it is fitting’), Kurd. (Sor.) šiyān/šē- ‘to be appropriate’, Zaz. šinayiš (šayiš)/šēn- ‘to be able’.'\"},\n   {\"src\": \"FFD\", \"where\": \"printed p.62\", \"stance\": \"supports\",\n    \"note\": \"'شای < فارسی میانه šāy < ایرانی باستان *xšāy-a-' — Abolghasemi's account of the New Persian verb.\"}\n ]\n})\n\nN.append({\n \"id\": 18, \"lang\": \"Sogdian\", \"words\": \"`xš`y; xšae-wan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Sogdian forms are in Gharib's dictionary in Nourai's own transliteration. The verb is entry 2083 ‘xšʾy- (Manichaean), (ə)xšāy 'to rule', with Buddhist Sogdian ‘γšʾy- and Christian Sogdian xšy- (Cheung p.451: 'BSogd. ‘γšʾy-, CSogd. xšy- ‘to rule’'). The noun is entry 727 ‘γsʾywnʾk, (a)xšēwane / əxšyōne < *xšaivanaka- 'king, ruler', beside entry 713 ‘γšʾwʾn (ə)xšāwan 'king, rule', 714 (ə)xšāwana 'rule, power' and 715 (ə)xšāwancīk 'kingship'. The whole family is the Sogdian branch of the same root: Old Iranian *xšāy- with the agent suffix *-wan- ('the one who rules'), the initial cluster surviving as ʾγš-/ʾxš- with a prothetic vowel because Sogdian did not tolerate initial xš-. Entry 729 ‘γšδrktʾk xšaθr-kate < *xšaθro-kṛtaka- 'made for a king' shows the xšaθra- member of the family in Sogdian too.\",\n \"derivation_fa\": \"هر دو صورت سغدی در فرهنگ سغدی قریب و با همان آوانگاری‌ای که نورایی به کار برده آمده است. فعل، مدخل ۲۰۸۳ است: ʾxšʾy- (سغدی مانوی) «فرمان راندن»، با صورت‌های بودایی ʾγšʾy- و مسیحی xšy- (چونگ ص۴۵۱). اسم، مدخل ۷۲۷ است: ʾγsʾywnʾk = (a)xšēwane / əxšyōne از *xšaivanaka- «شاه، فرمانروا»، در کنار مدخل‌های ۷۱۳ (ə)xšāwan «شاه، فرمانروایی»، ۷۱۴ (ə)xšāwana «فرمانروایی، قدرت» و ۷۱۵ (ə)xšāwancīk «شهریاری». همهٔ این خانواده شاخهٔ سغدی همان ریشه است: *xšāy- ایرانی باستان با پسوند فاعلی *-wan-، و خوشهٔ آغازین با واکهٔ افزودهٔ آغازین (ʾγš-/ʾxš-) نگاه داشته شده، زیرا سغدی خوشهٔ آغازین xš- را برنمی‌تابید. مدخل ۷۲۹ (xšaθr-kate از *xšaθro-kṛtaka- «ساختهٔ شاه») نشان می‌دهد که عضو xšaθra- این خانواده نیز در سغدی هست. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:26\", \"status\": \"not_found\",\n    \"note\": \"Gharib's printed p.26 (SOD_pages.txt leaf 91) runs from entry 662 ‘δyqmyc to 677 ‘fsnyh — ʾδ-/ʾfr-/ʾfs- words, nothing from this family. The verb ʾxšʾy- is entry 2083, on printed p.83.\"},\n   {\"ref\": \"SOD:28\", \"status\": \"supports\",\n    \"note\": \"Gharib p.28 (SOD_pages.txt leaf 93) carries exactly these words: '713 ‘γšʾwʾn S ... (ə)xšāwan ... king ?, rule ?'; '714 ‘γšʾwʾn(h) B, S (ə)xšāwana ... rule, power'; '715 ‘γšʾwʾncyk S (ə)xšāwancīk ... kingship, rule'; '727 ‘γsʾywnʾk B (a)xšēwane, əxšyōne ©<*xšaivanaka ©ob. pl. -ty ... king, ruler'; '729 ‘γšδrktʾk B (ə)xšaθr-kate ... ©<*xšaθro-kṛtaka (made for) king, kingly'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib entry 2083 (printed p.83)\", \"stance\": \"supports\",\n    \"note\": \"'2083 ‘xšʾy- M (ə)xšāy (xšʾy-) → ‘γšʾy- (to) rule. GMS 1086; C2 n p51; Sund. Man. Lett. 310.16' — the verb of Nourai's box, with the backtick spelling he reproduces.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.451 s.v. *xšaH, 'SOGDIAN'\", \"stance\": \"supports\",\n    \"note\": \"'SOGDIAN: BSogd. ‘γšʾy-, CSogd. xšy- ‘to rule’. Impf.: IND. 3sg. CSogd. xšyʾ, 3pl. BSogd. ‘γšʾyʾnt.'\"},\n   {\"src\": \"ISS\", \"where\": \"Bailey, grepped ISS_alt_DKS.txt for kṣatra / xšaθra\", \"stance\": \"silent\",\n    \"note\": \"The Khotanese material on disk returned no entry bearing on the Sogdian forms of this box.\"}\n ]\n})\n\nN.append({\n \"id\": 19, \"lang\": \"Persian\", \"words\": \"afšîn «افشین»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Afšīn (Arabic أفشين) was the hereditary title of the princes of Usrūšana in Sogdian-speaking Transoxiana, best known from Ḥaydar b. Kāvūs al-Afšīn, the ʿAbbasid general who crushed Bābak and was executed in 841; it survives in modern Persian as a male given name. Deriving it from the Sogdian word of node 18 is the mainstream view and rests on exactly the entry Nourai cites: Gharib's *xšaivanaka-/(ə)xšēwan(e) 'king, ruler' (*xšāy- 'to rule' + agent -wan-), whence with the ordinary Sogdian-to-Arabic fronting of the initial cluster (ə)xšēwan > *axšēwan > Afšīn. There is however a rival etymology in circulation for the personal name: Wiktionary and the English Wikipedia article derive Persian افشین from Middle Persian Pišīn, Avestan pisinah- (with Bactrian *Afšiiano and Armenian Apʻšin/Ōšin), calling the ultimate origin unknown. Since Nourai's source is the specialist Sogdian dictionary and the title is a Sogdian office, his line is the better supported one, but the competing derivation keeps this short of 'confirmed'.\",\n \"derivation_fa\": \"«افشین» (عربی: أفشين) عنوان موروثی شاهزادگان اُشروسنه در فرارود سغدی‌زبان بود و بیش از همه از حیدر بن کاووس افشین، سردار عباسی، شناخته می‌شود که بابک را شکست داد و در ۲۲۶ ق کشته شد؛ در فارسی امروز نام خاص مردانه است. گرفتن آن از واژهٔ سغدی جعبهٔ پیشین دیدگاه رایج است و دقیقاً بر همان مدخلی تکیه دارد که نورایی به آن ارجاع داده است: (ə)xšēwan(e) < *xšaivanaka- «شاه، فرمانروا» در فرهنگ قریب (از *xšāy- «فرمان راندن» + پسوند فاعلی -wan-)، که با پیش‌شدگی خوشهٔ آغازین در گذر به عربی به صورت *axšēwan > Afšīn درآمده است. با این حال ریشه‌شناسی رقیبی نیز هست: ویکی‌واژه و ویکی‌پدیای انگلیسی «افشین» را از Pišīn فارسی میانه و pisinah- اوستایی می‌گیرند و خاستگاه نهایی را ناشناخته می‌خوانند. چون منبع نورایی فرهنگ تخصصی سغدی است و این عنوان خودْ منصبی سغدی بوده، خط او پشتوانهٔ بهتری دارد، ولی وجود دیدگاه رقیب مانع از «تأیید کامل» می‌شود.\",\n \"sources\": [W+\"%D8%A7%D9%81%D8%B4%DB%8C%D9%86\", \"https://en.wikipedia.org/wiki/Afshin\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:26\", \"status\": \"not_found\",\n    \"note\": \"Gharib's printed p.26 has no word of this family (entries 662-677, ʾδ-/ʾfr-/ʾfs-).\"},\n   {\"ref\": \"SOD:28\", \"status\": \"supports\",\n    \"note\": \"Gharib p.28, entry 727: '‘γsʾywnʾk B (a)xšēwane, əxšyōne ©<*xšaivanaka ©ob. pl. -ty → ‘xšywn(y), xšywny(y), ... MLK(,) king, ruler' — the etymon Nourai's afšīn presupposes, including the Aramaic ideogram MLK 'king'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib entries 713-715, 727 (p.28)\", \"stance\": \"supports\",\n    \"note\": \"The set (ə)xšāwan 'king', (ə)xšāwana 'rule, power', (a)xšēwane < *xšaivanaka- 'king, ruler' provides the exact base for the title of the Usrūšana princes.\"},\n   {\"src\": \"MON\", \"where\": \"grepped MON_part1/2 and MON_2vol_Adena for افشین\", \"stance\": \"silent\",\n    \"note\": \"No hit; the entry would fall in Mo'in's aʿlām volumes (5-6), which are not on disk.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, grepped for Afšīn\", \"stance\": \"silent\",\n    \"note\": \"Not treated among the Persian loanwords in Arabic in Asbaghi's dictionary.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 278,\n \"book_page\": 248,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [root]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-278.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(N), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build278.py && python3 -m json.tool data/verification/page-278.json > /dev/null && echo JSON_OK"
}
```


### [2026-09-06T21:43:22.513Z] TOOL RESULT

```
written 19 nodes
JSON_OK
```


## [2026-09-06T21:43:27.541Z] TOOL CALL #101: Bash

```json
{
 "command": "python3 tools/verify_check.py 278"
}
```


### [2026-09-06T21:43:29.516Z] TOOL RESULT

```
nodes verified: 19/19
node verdicts: {'plausible': 7, 'disputed': 2, 'confirmed': 8, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_found': 4, 'contradicts': 1, 'not_checked': 11, 'partial': 1}
books consulted: {'supports': 49, 'partial': 6, 'contradicts': 2, 'silent': 6} | by book: {'PHD': 8, 'CHEUNG': 5, 'NYB': 5, 'KLN': 5, 'KNT': 5, 'BRT': 4, 'PLA': 4, 'LKT': 3, 'SKT': 3, 'MON': 3, 'WLD': 2, 'HRN': 2, 'AHD': 2, 'SPG': 2, 'BOOK': 2, 'SOD': 2, 'SYN': 1, 'ARY': 1, 'AFM': 1, 'BQT': 1, 'FFD': 1, 'ISS': 1}
```


## [2026-09-06T21:43:52.814Z] AGENT

Verification of PDF page 278 (book p. 248) is complete: `/home/sfmqrb/git/rishe/data/verification/page-278.json`, `verify_check.py 278` reports 19/19 nodes and 0 PROBLEM lines.

**Page 278 — root "Ksei 1, Qsěi" (PIE *tkʷeh₁(i)- / Pok. kþē(i)- 626), 1 entry, 19 nodes**
- Root: confirmed (POK:626, KLN:272, WLD I.504, Watkins tḱē-, Buck 19.31 all agree; Cheung 451 cites Pok. 626 but calls the Greek link "elusive").
- Node verdicts: 8 confirmed, 7 plausible, 2 disputed, 2 transcription_suspect.
- Ref checks: 18 supports, 1 partial, 1 contradicts, 4 not_found, 11 not_checked (ETM, ZMA, ZFS, AHD body pages — none digitised).

**disputed**
- Nodes 2 & 3 — Pahlavi *šēr* / Persian شیر ۲ "lion": does NOT belong to this root. MP is *šagr* (MacKenzie refers "šēr, v. šagr"); and Hübschmann p.83 no.803 — the very page Nourai cites (HUB:83) — says "Also šēr 'Löwe' davon zu trennen". Everything else in those boxes (šāh, šahr/šatr, čak) is confirmed.

**transcription_suspect (book misprints, extraction faithful)**
- Node 14 Greek `xerexes` and node 15 English `Xerexes` → should be Ξέρξης / Xerxes. Verified against the printed page (copied to `data/verification/sources/refs/ocr/BOOK/278.png`); `error_in: "book"`.

**Other findings worth the owner's eye (no data fix needed)**
- BQT:626 (node 2) is not_found — Borhan p.626 is the چراغ section; looks like a slip for POK:626. HRN:100 (node 7) not_found — Horn p.100 is čōgān/čun/či; the right Horn pages are 61 and 177. SOD:26 not_found — the Sogdian verb ʾxšʾy- is entry 2083 on p.83, not p.26 (SOD:28 is exact).
- Node 1: OP *xšaça-* means "kingdom", not "king, ruler"; and the chart's NOTE that "-thra/-tra are Avestan suffixes meaning 'having, owner of'" is wrong (it is the IIr. *-tra- action noun) → node marked plausible.
- Nodes 7 & 12 are labelled "Avestan" but *Arta-xšaça-*, *pati-xšāya-*, *xšaça-pāvan-* and *Xšayāršan-* are Old Persian; only xšaθra-vairya- and *xšaθrō.dāra- are Avestan. Also "paiti-xšatra" should be *pati-xšāya-.
- Node 6: the chess/checkmate line is certain; the bank "cheque" line (چک > Ar. صكّ) follows Klein, Asbaghi (PLA) and Mo'in's Borhan footnote, against Etymonline/OED/Lokotsch — a real scholarly split, hence "plausible".
- New evidence saved: `data/verification/sources/refs/ocr/BQT/1237.vision.txt` (Mo'in's footnote giving *shâyîtan – shâyistan*, the source of Nourai's Pahlavi form) and `.../ocr/BOOK/278.png`. 10 web pages archived via fetch_source.py.

**No extraction errors found** — the JSON matches the printed page throughout, including the شهریار bracket on node 8 and the Ferdowsi چک verse.
