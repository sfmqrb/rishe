# Verification process log — verify-page-270


## [2026-09-06T20:54:50.820Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 270 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-270.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-270.json. Write /home/sfmqrb/git/rishe/data/verification/page-270.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 270` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:54:52.441Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:54:53.152Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:54:53.168Z] TOOL RESULT

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


## [2026-09-06T20:54:53.348Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-270.txt"
}
```


### [2026-09-06T20:54:53.368Z] TOOL RESULT

```
1	=== PDF page 270 (book page 240) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kleu 1 : to hear  (refs POK:605)
4	#1 (parent #0) [Avestan] refs=HRN:177 | sru 2, srav, xšnu, xšnaw : to hear
5	  #2 (parent #1) [Pahlavi] refs=FFD:64 | ašnŭdan : to hear
6	    #3 (parent #2) [Persian] refs=BQT:1304 | šenîdan «شنیدن» : to hear | extra: شنودن ، شنو ، حرف شنو
7	#4 (parent #0) [Avestan] refs=POK:605; KLN:1456; FFD:60 | sravah : word, speech ; srŭ-ta : speech ; sraw : to read ; srâw : to sing
8	  #5 (parent #4) [Persian] refs=BQT:1131,1302; MON; FRS:27 | sarvâ «سروا ( سرواد ، سرواده )» : poem, story | extra: سرود ، سرودن ، سراییدن ، سرای ۲
9	#6 (parent #0) [Avestan] refs=HRN:108; SNS:331 | hu-srav : well famed, famous ☞Su 1 ; dâuš-sravah : ill-famed ☞Dus
10	  #7 (parent #6) [Pahlavi] refs=BQT:748 | hu-srov : well-famed, title of kings and in-laws.
11	    #8 (parent #7) [Persian] refs=BQT:748,749 | xosrow «خسرو ( کسرىٰ )» : (well famed) king, ruler ; xosor «خُسُر ( خسور ، خسوره )» : father-in-law ; xošŭ «خُشو» : mother-in-law
12	  #9 (parent #6) [Pahlavi] refs=SNS:331 | du-srav : ill famed, infamous ☞Dus
13	    #10 (parent #9) [None] refs=None | 
14	#11 (parent #0) [Avestan] refs=POK:605 | sraothra, sraosha : ear, one who listens and follows
15	  #12 (parent #11) [Pahlavi] refs=BQT:1132 | srôsh : one who obeys (God)
16	    #13 (parent #12) [Persian] refs=BQT | sorŭsh «سُروش» : one of God's angels
17	#14 (parent #0) [Old Slavic] refs=KLN:1456 | slovo : word ; Slověninŭ : Slav
18	  #15 (parent #14) [Middle Greek] refs=KLN:1456 | slabnovus : Slav, also slaves taken from the Slavs
19	    #16 (parent #15) [Middle Latin] refs=None | slavous : Slav, slave
20	      #17 (parent #16) [French] refs=None | 
21	        #18 (parent #17) [Persian] refs=MON |  | extra: اسلاو ، چکوسلواکی ، یوگوسلاوی
22	        #19 (parent #17) [English] refs=None | Slav, Yugoslavia, Czechoslovakia, slave
23	#20 (parent #0) [Germanic] refs=AHD | hlusinôn : to listen ; hlŭdaz : loud
24	  #21 (parent #20) [English] refs=None | listen, loud
25	#22 (parent #0) [Latin] refs=AHD | cluere : to be named
26	  #23 (parent #22) [English] refs=None | client
27	
```


## [2026-09-06T20:54:55.125Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-06T20:54:56.538Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-270.json",
 "description": "Read page 270 extracted JSON"
}
```


### [2026-09-06T20:54:56.574Z] TOOL RESULT

```
{
  "pdf_page": 270,
  "book_page": 240,
  "entries": [
    {
      "root": {
        "name": "Kleu 1",
        "lang": "Indo-European",
        "refs": "POK:605",
        "gloss": "to hear"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:177",
          "words": [
            {"translit": "sru 2, srav, xšnu, xšnaw", "gloss": "to hear", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:64",
          "words": [
            {"translit": "ašnŭdan", "gloss": "to hear", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1304",
          "words": [
            {"translit": "šenîdan", "gloss": "to hear", "script": "شنیدن"}
          ],
          "script_extra": "شنودن ، شنو ، حرف شنو",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:605; KLN:1456; FFD:60",
          "words": [
            {"translit": "sravah", "gloss": "word, speech", "script": null},
            {"translit": "srŭ-ta", "gloss": "speech", "script": null},
            {"translit": "sraw", "gloss": "to read", "script": null},
            {"translit": "srâw", "gloss": "to sing", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1131,1302; MON; FRS:27",
          "words": [
            {"translit": "sarvâ", "gloss": "poem, story", "script": "سروا ( سرواد ، سرواده )"}
          ],
          "script_extra": "سرود ، سرودن ، سراییدن ، سرای ۲",
          "note": null,
          "quote": {
            "text": "چند دهی وعدهٔ دروغ همی - چند فروشی تو بر من این سروا",
            "poet": "Ormazdî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:108; SNS:331",
          "words": [
            {"translit": "hu-srav", "gloss": "well famed, famous", "script": null, "see": ["Su 1"]},
            {"translit": "dâuš-sravah", "gloss": "ill-famed", "script": null, "see": ["Dus"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "BQT:748",
          "words": [
            {"translit": "hu-srov", "gloss": "well-famed, title of kings and in-laws.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:748,749",
          "words": [
            {"translit": "xosrow", "gloss": "(well famed) king, ruler", "script": "خسرو ( کسرىٰ )"},
            {"translit": "xosor", "gloss": "father-in-law", "script": "خُسُر ( خسور ، خسوره )"},
            {"translit": "xošŭ", "gloss": "mother-in-law", "script": "خُشو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بد سگال تو و مخالف تو - خشوی جنگجوی با داماد",
            "poet": "Farrokhî"
          }
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "SNS:331",
          "words": [
            {"translit": "du-srav", "gloss": "ill famed, infamous", "script": null, "see": ["Dus"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:605",
          "words": [
            {"translit": "sraothra, sraosha", "gloss": "ear, one who listens and follows", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Pahlavi",
          "refs": "BQT:1132",
          "words": [
            {"translit": "srôsh", "gloss": "one who obeys (God)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "sorŭsh", "gloss": "one of God's angels", "script": "سُروش"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "لطف الـهی بکند کار خویش - مژدهٔ رحمت برساند سروش",
            "poet": "Hâfez"
          }
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Old Slavic",
          "refs": "KLN:1456",
          "words": [
            {"translit": "slovo", "gloss": "word", "script": null},
            {"translit": "Slověninŭ", "gloss": "Slav", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Middle Greek",
          "refs": "KLN:1456",
          "words": [
            {"translit": "slabnovus", "gloss": "Slav, also slaves taken from the Slavs", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Middle Latin",
          "refs": null,
          "words": [
            {"translit": "slavous", "gloss": "Slav, slave", "script": null}
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
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "اسلاو ، چکوسلواکی ، یوگوسلاوی",
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Slav, Yugoslavia, Czechoslovakia, slave", "gloss": null, "script": null}
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
            {"translit": "hlusinôn", "gloss": "to listen", "script": null},
            {"translit": "hlŭdaz", "gloss": "loud", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "listen, loud", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "cluere", "gloss": "to be named", "script": null}
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
            {"translit": "client", "gloss": null, "script": null}
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


## [2026-09-06T20:54:58.342Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','KLN','FFD','BQT','MON','FRS','SNS','AHD','WLD','BRT','PHD','NYB','SKT','IEC','SYN','HUB','CHEUNG','ARY','WEB','FSD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T20:55:00.762Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-06T20:55:05.416Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md"
}
```


### [2026-09-06T20:55:05.457Z] TOOL RESULT

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


## [2026-09-06T20:55:05.571Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -100"
}
```


### [2026-09-06T20:55:05.607Z] TOOL RESULT

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


## [2026-09-06T20:55:09.162Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"k̂leu\" POK_full.txt | head -40; echo \"=== alt\"; grep -n \"605\" POK_full.txt | head -5"
}
```


### [2026-09-06T20:55:09.224Z] TOOL RESULT

```
=== alt
33049:References: WP. I 605. 
33075:References: WP. I 605 f., WH. I 545 f., 570. 
35679:References: WP. I 599 f., WH. I 605 f., 618 f., Trautmann 371 f., Schwyzer Gr. Gr. I 514, 
47675:Page(s): 604-605 
51524:Page(s): 605-607
```


## [2026-09-06T20:55:09.714Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kleu\" POK_full.txt | head -40"
}
```


### [2026-09-06T20:55:09.762Z] TOOL RESULT

```
5404:enkel. Old Frisian onkel, onkleu. Modern High German Enkel, 
44780:The inanimate suffix -ur- . bret. kleur^ Gabelbaum am Wagen ') : 'lAAupioi , oi, lllyrians, 
44978:Aor. (£)k£kA£to, Doric k£vto = (£)k£Ato; [about k£A£uu) see below kleu-]; K£Aapu^u) 
47521:See also: s. still under kleu- " rinse '. 
47616:Root/ lemma: kleu- {a\so kleu-1) and klau- 
49036:assumption secondary lengthened grade *kleup/b-ov\e has added Gothic hiaupan'ruvi, 
51494:( *kleuos) "fame'; Pedersen Tochar. 225. 
51520:= "*will hear' from *kleua-s-id has future s). 
51555:Germanic *kleuo-)\ 
51565:applied, would be for kleu- : kel- the relation sreu-' flow ' : ser- either model or parallel.
```


## [2026-09-06T20:55:11.711Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51430,51600p' POK_full.txt"
}
```


### [2026-09-06T20:55:11.776Z] TOOL RESULT

```
'allows to hear', sruyate' is heard ', sruti-' the hearing '; 



Avestan surunaoltl {* klu-n-) 'hort, steht im Rufe, heiflt' etc., participle sruta-' heard, 
famous ', sm/Z-'das zu Gehorbringen, Vortrag'; 

Old Indie srotra-n. 'ear', Avestan srao^ra-n. ' the singing ' (= Old English hieodor. Old 
High German hllodai), Avestan sraota-n. ' the hearing ' (compare serb. slutlti), Avestan 
sraoman-n. ' ear, hearing ' (: Gothic hlluma). Old Indie sromata-n. 'good shout, call' (= 
Old High German hllumunt); 



Armenian lu' renowned, glorious ' (= kAut6(; etc.), /c//'"l<nowledge, rumor, tidings ', Isem, 
Aor. /i/ay'hear, heard' ( *Rlu-Re-)\ the -s- of thepresent tense is the most lil<ely -sRo-)\ 

gr. kA£(F)co, -opai, ep. kAeIw " praise' are secondary; ekAuov "heard' (= Old Indie 
sruvam), kAuGi, kskAuGi "hear!', kAut6(; "illustrious', kKzuoc, 'illustrious' (*kA£F£T0(;, as 
Y£V£Tr|, Latin genitus), KAr|i^u) " praise; shout, name' (*KA£F£[a]-i^cjo of e5-stem), KA£r|5u)v, 
KAri5obv, -di/of (*KA£F-r|5u)v) "shout, call', etc.; 

Latin clued, -ere (later also duo, -ere) " to hear, be spoken of, be said ' (e-verb with the 
zero grade Rlu-), c/uv/or{G\.) " that is known, well-known, famous, noted, celebrated, 
renowned ', />7cA//^5 "illustrious' (about Latin from-culto see below Rel-2^ incline '), Oscan- 
Umbrian only in names {Kluvatiis^ Clovatius ', Umbrian Kluviier^ Cluvii ' ); 

Old Irish cloth v\. "fame' (= Old Indie sruta-), cymr. clod^ praise, commendation, glory, 
fame, renown, esteem '; 

cymr. clywed^ the hearing, sense of hearing ', mcymr. clywaf, corn. clewar\ hear'; bret. 
clevout^heaf. Old Irish ro-clul-nethar {recons/erted with metathesis from *cll-nu-, Indo 
Germanic *RJ-) " hears ', Perf. 1. Sg. ro-cuala, cymr. clgleu^ hear'. Old Irish Konj. rocloor^ 
da^cf^Tore ', -cloth, newer -doss ' was heard '; Thurneysen Gr. 357, 439; 

Old Icelandic /7^(9d "listening, quietness; sound' (= Avestan sraota-). Old English hieodor 
"sound, tone, melody ', Old High German hiiodaru. "sound, tone, clangor ' (= Old Indie 
srotra-), Gothic hllumaru. ' ear, hearing ', PI. "ears' (= Avestan sraoman). Old High 
German hiiumunt. Modern High German Leumund{= Old Indie sromata-), participle 
*hlu^a-, *hluda- in Old High German HluderTch, Hlotharl, Old English Hlo^-wTg, Hlol=>-here 
etc.; besides with J (heavy basis, see above). Old High German hlut. Old English Old 
Saxon hlud. Modern High German laut, 

Latvian sludlnat^ announce, declare '; lengthened grade Lithuanian sloveaud slove 
"glory, magnificence, splendor', ablaut. East Lithuanian s/ai/e "fame'; 

Old Bulgarian slovg, slutl'caW, be illustrious', lengthened grade slavat "fame', 
therefrom slavltr make illustrious ', serb. slutTm, slutltr foresee, predict ' (Denom. a *slutb; 
sloven, slut^ suspicion ' is probably postverbal), s/y/yie "shout, call, names'; 

Tocharian AB Rlaw-^ announce, declare '; A Riots, B RIautso'ear, gill'. 

With West Indo Germanic guttural: alb. RJuhem'be called', gjuanj, Rjuanj^v\axr\e' 
(Pedersen IF. 5, 36). 



2. es-stem: Old Indie sravas-n. 'fame', Avestan sravah-n. "word', gr. KhtFoq "fame', 
lllyrian EN Ves-cleves{= Old Indie vasu-sravas' possessing good fame '), Latin c/uor{G\.) 
" glory, splendour, effulgence, the opinion which others have of one, estimation, reputation, 
credit, honour ', Old Irish c/J"fame' (but cymr. c/yw' ear, hearing ' is a new formation), this 
/yfrom the Gen. Sg. derives; Old Church Slavic 5/01/0 "word'; Tocharian A k/yw, B kalywe 

( *kleuos) "fame'; Pedersen Tochar. 225. 

3. s-extensions: Old Indie srosati^ hears, listens, conforms ', srusti-^ compliance, 
obsequiousness ', Avestan sraosa-^ ear, hearing ' etc.; 

Armenian lur closemouthed ' (k/us-r/-); 

Old Irish c/uas 'ear' {*klousta) = cymr. o/Js/" ear, hearing '; 

Old Icelandic h/er'das Lauschen' (from *hloza-, older *hluza-). Old High German hlosen 
"lend ear, listen ', Modern High German (Bavarian) Alemannian /osen6s.; Old Icelandic 
h/ust'ear' (= Old Indie srusti-). Old English hlyst' ear, hearing ', Old Saxon hlusti. " 
Gehor, Ohr, Horen, Lauschen ', Old Icelandic hlusta, Old English /7/ys/5/7 (engl. listen) 
"wake up, become alert, listen '; with J (as Old High German hlut, see above): Old High 
German lOstren, Modern High German (schwab. -Bavarian) /ausfern'\en6 ear, listen ', 
Modern High German lauschen ( *hlus-skdn)\ Old English hieor. Old Saxon hllor. Old 
Icelandic hlyr'c\\ee\C (= Old Bulgarian sluch-b); 

Old Bulgarian slysatrheaf, sluch-b' ear, hearing ', slusatl {serb. slusatl, also heavy 
basis as slysati) "hear'; 

Tocharian A klyos-, B klyaus-'heaf; A klosam, B klausane Dual "ears'. 

With West Indo Germanic gutturals: Messapic A/50/7/ "hear!' (: Old Indie srosi); 
Lithuanian klausau, -y//"hear', Latvian klausft' hear, obey ', Old Prussian klausTton 
"erhoren', Lithuanian paklusnus' obedient, submissive ' (against it Lithuanian klauslu'ask' 
= "*will hear' from *kleua-s-id has future s). 

References: WP. I 494 f., WH. 86 f., 237 ff., Trautmann 307 f., Specht Indo Germanic 
Dekl. 285, 333; Hj. Frisk, Goteborgs Hogsk. Arsskr. LVI 1950: 3. 
Page(s): 605-607 

Root / lemma: Rleu-2: *Rld[u]- : Rlu- 
Meaning: to rinse, clean, tear 



Root / lemma: Rleu-2. *Rld[u]-. Rlu-\ to rinse, clean, tear, derived from Root/ lemma: Rleu- 

1, RIeua- : RIO- : to hear, cry. 

Note: extension RIeu-d-, Latvian also Rlou-k-. 

Material: Gr. kAu^oj (*kAu5ju)) ' rinse, wash with water ', kAuSojv m. ' wave, billow, surf, 

rough water', KAuapa n., KAuapoc; m. " gurgle, sound made by water flowing over stones ', 

kAugthp m. " a clyster-pipe, syringe ', root nouns Akk. Sg. KAu5a " surge '; 

Maybe alb. Geg {*klusmos) klumesht, Tosc qumeshV milk' : gr. KAuap6(; m. " gurgle' : 

Latvian 5/5^/r/" milk'. 

Old Latin cluo^ to free from what is superfluous, make clean, make pure, clean, 
cleanse, purify' {*Rloud), Latin cloaca {cluaca, clovaca) ' drainage ditch, drainage canal '; 

altgal. Cluad, acymr. Clut, Ptol. KAcbra river name, engl. Clyde (Celtic *klouta)\ cymr. clir 
"clear, bright, cheerful, pure' {*klu-ro-s); 

Gothic hlutrs. Old English hlut(t)or. Old Saxon Old High German hlut(t)ar^ pure, clear, 
bright'. Modern High German lauter{*klud-ro-s)\ Old Norse hler^ sea' {*hlewa-, Indo 
Germanic *kleuo-)\ 

Lithuanian sluoju, slaviau, sluoti, dial. slavu{= Latin duo) ' sweep, wash away, whisk ', 
sluota^ besom ', Latvian sludta6s.; extension kldu-k-\n slauclt^ sweep, wash away, 
whisk', slauksef splash, fall violently and noisy ', slaukVxvi\\W, Lithuanian sliaukti, slaukyti 
" sweep, wash away '. 

Perhaps extension of *Rel- "humid, wet, damp', there also lie the consecutive roots of 
the basic: ^/ep-"humid, wet' (see there), klek-6s. (Lithuanian slaku, -e//"drip, trickle', slektl, 
sllknotr spray' etc.), kleg{h)- ds. (russ. s/eza "tears'. Old Church Slavic sIbzaAs.). If this 
applied, would be for kleu- : kel- the relation sreu-' flow ' : ser- either model or parallel. 

References: WP. I 495 f., WH. I 239 f., Trautmann 307. 
Page(s): 607 

Root / lemma: Rlou-nl- 
Meaning: hip 

Material: Old Indie sroni-m. f., Avestan sraonl-i. "buttock, hip, haunch'; 

Latin clOnls^ a buttock, haunch, rump of people and animals' {clunaculum^ small sword 
or dagger which one carries behind '); 

cymr. corn, clunt "hip, haunch', bret. M//? "buttock'; 



Old Icelandic hlaunx\. 'buttock'; 

Lithuanian slaunis^ femur, thigh, hip, haunch, ham ', Latvian s/auna'h'\p, haunch'; Old 
Prussian s/a^/7/5 'thigh'. 

The Lautform from gr. KAoviq, -loq ' coccyx, small triangular bone at the base of the 
spinal column ' is still unexplained. 

References: WP. I 499, WH. I 239, Trautmann 306, Specht Indo Germanic Dekl. 162. 
Page(s): 607-608 

Root / lemma: Roi-no- 

Meaning: grass 

Material: Gr. Koiva xopTO(; Hes. (perhaps Neutr. PI.); Lithuanian sienas, Latvian s/ens'hay' 

(Finnish loanword out of it signify 'hay, grass, herb'); Old Church Slavic seno^ any
```


## [2026-09-06T20:55:15.732Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51390,51432p' POK_full.txt"
}
```


### [2026-09-06T20:55:15.779Z] TOOL RESULT

```
See also: extension from Rel-2^ incline '; s. also under (s)kel-bev\6\ 
Page(s): 600-602 

Root / lemma: Rlep- {sRlep-1) 

Meaning: to cover, conceal, steal 

Material: Gr. kAshtu) (*KA£ni(ji)) "steal' (KSKAocpa, SKAannv and SKAscpGnv), kKzuoc, n., 

KAspija (out of it Latin clepta), KAcbi^j, KAonoq, KAon£U(; 'thief, KAonr) ' theft '; 

Latin clepo, -ere ' to steal '; 

Gothic Mfan'sieay {hliftus^MeV); 

Middle Irish cluain {*klopni-) f. 'deceit, flattery, insincere compliments', cluainech 
'deceitful'; 

Old Prussian auklipts{*-klept6s) 'hide, conceal'; s. also under klep-. 

With aniaut. 5/- from s/r/- seems related Lithuanian slepiu, s/ep// "conceal'. 

The meaning is made probably, that Rlep- extension from ^e/- 'conceal'; Middle High 
German hulft^ quiver ' seems to be justly zero grade our root form, as Old Prussian 
auklipts. Old Prussian ai//r//p/s indicate then West Indo Germanic guttural. 

References: WP. I 497, WH. I 232, Trautmann 137. 
Page(s): 604 

Root/ lemma: Rleu-1, RIeue-. Rlu- 

Meaning: to hear, cry 

Note: (extension a root Rel^\ 

Material: 1. Old Indie srnSti {*RJ-neu-) ' hears ', srudh/" hear' (= *kAu9i), participle sruta-{= 

KAuToq, Latin inclutus, Irish cloth v\.. Old High German Hlot-, Armenian lu) etc., sravayati 

'allows to hear', sruyate' is heard ', sruti-' the hearing ';
```


## [2026-09-06T20:55:16.474Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kleu-\\|k̑leu\\|ḱleu\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T20:55:16.523Z] TOOL RESULT

```
189:Most interesting are the cases where from two or more traditions (usually including Homer and the Rig-Veda) it is possible to reconstruct a poetic phrase or formula con- sisting of two members. Such are the expres- sions ‘“‘imperishable fame,” *klewos ndhg’hitom (kleu-', dhg“hei-); “holy (men- tal) force,” *isorom menos (eis-', men-'); and the “weaver (or crafter) of words,” the Indo- European poet himself, *wek”om teks-on (wek”, teks-). The immortality of the gods (*n-mrto-, from mer-?) is emphasized anew by the vivid verb phrase nek-' tera-?, “to overcome death,” appearing in the Greek word nektar, the drink of the gods. And at least one three-member formula (in the sense of the word in traditional oral poetry) can be reconstructed for the poetic language of prayer, on the combined evidence of four languages, Latin, Umbrian, Avestan, and Sanskrit: “Protect, keep safe, man and cat- tle!” (pa- wi-ro- peku).
638:kleu-1, To hear. I. Extended form *kleus- in Germanic *hleuza- in Old English hléor, cheek (< “side of the face” < “ear”): LEER. II. Zero-grade form *klu-. 1. Germanic *hlustjan in Old English Alystan, to listen: LIsT*. 2. Ger- manic *hlusin6én in Old English Alysnan, to listen: LIs- TEN. 3. Suffixed lengthened form *kli-to- in Germanic *hlidaz, “heard,” loud, in: a. Old English Alid, loud: Loup; b. Old High German Aldti, sound: ABLAUT, UM- LauT. III. Suffixed form *klew-yo- in Greek kleiein, to praise, tell: Cio. [Pok. 1. Rleu- 605.]
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1370:CLAN plat- CLANDESTINE kel-2 CLANG kleg- CLASMATOCYTE kel-1 cLass kele-2 CLAST kel-1 CLasTIC kel-1 CLATHRATE kleu-3 CLATTER gal-2 CLAUSE kleu-3 CLAVATE kleu-3 CLAVICHORD kleu-3 CLAVICLE kleu-3 CLAVICORN ker-1, kleu-3 CLAVIER kleu-3 CLAVIFORM kleu-3 CLAW gel-1
1371:CLAY gel-1 CLAYMORE kel-1, mé-3 CLEAN gel-2 CLEANSE gel-2 CLEAR kele-2 CLEAT gel-1 CLEAVE! gleubh- CLEAVE? gel-! CLEAVERS gel-1 CLEF kleu-3 CLEISTOGAMOUS_ kleu-3 CLEISTOTHECIUM dhé-1, kleu-3 CLEMATIS kel-1 CLENCH gel-1 CLEPSYDRA klep-, wed-! CLERK kel-1 CLEVER gleubh- CLEVIS gleubh- CLEW! gel-1 CLIENT klei- CLIMATE klel- CLIMAX Klei- CLIMB gel-1 CLINAL klei- CLINANDRIUM klei- CLINCH gel-1 CLINE klel-
1374:Cio kleu-1
1375:CLIP? gel-1 CLITELLUM klei- CLoAcA kleu-2 cLop gel-1 CLOISONNE kleu-3 CLOISTER kleu-3 CLONE kel-1 CLONUS kel-3 CLOSE kleu-3 CLOSURE kleu-3 CLOT gel-1
1376:CLOTH peie- cLoup  gel-1 cLouT gel-1 CLOVE! kleu-3 CLOVE? gleubh- cLoy kleu-3 CLOZE kleu-3 CLUB) gel-1
1378:CLUMP gel-1 CLUTCH! gel-1 CLUTTER gel-1 CLYSTER kleu-2 co- kom COADUNATE oi-no- COAGULUM_ ag- COAL g(e)u-lo- COALESCE al-3 COARCTATE ar- coasT kost- COBALT ku- cocciD kokkos coccus kokkos COCHINEAL kokkos COCHLEA konk(h)o- cock? ku- COCKAIGNE kak-2 COCKCHAFER gep(h)-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1711:KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
```


## [2026-09-06T20:55:32.353Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Slav\\b\" KLN_1966.txt | head -30; echo \"=== 1971\"; grep -n \"Sklabenos\\|Sklabos\\|Sclavus\\|Slovene\\|Slovenin\" KLN_1966.txt KLN_1971.txt | head -30"
}
```


### [2026-09-06T20:55:32.421Z] TOOL RESULT

```
883:OSlav.
982:Slav.
1246:■**<*lve,  tr.  v.  —  L.  absolvere,  ‘to  set  free’,  fr. •h-  and  solvere,  ‘to  loosen,  set  free'.  See  solve and  cp.  assoil.  Cp.  also  dissolve,  resolve. ^*orb,  tr.  v.  —  L.  absorbere,  ‘to  swallow  up’, fr.  ab-  and  sorbere,  ‘to  suck  in,  swallow  up’, which  is  cogn.  with  Arm.  arbi  (from.  *srbh-), ‘I  drank,  Gk.  poipeiv  (for  *apo<peLv),  ‘to  sup UP’>  Alb.  gerp  (for  *serbhd-),  ‘I  sip’,  OSlav. *rubati,  Lith.  surbiu,  surbti,  sribiu,  srebti,  ‘to •  Mir.  srub,  ‘snout’.  Cp.  absorption,  resorb, •*•*1  v.,  and  the  second  element  in  Sangui- ■orba.
1427:OSlav.  jezero,  ‘lake’.  The  derivation  of  Gk. ’Ayipav  fr.  Sr/op,  ‘woe’,  is  folk  etymology. Acheulean,  Acheulian,  adj.,  pertaining  to  the paleolithic  period  preceded  by  the  Chellean  and succeeded  by  the  Mousterian  (geology).  —  F. Acheulien,  from  the  name  of  the  village  St. Acheul,  near  Amiens,  in  France;  so  called  in allusion  to  the  remains  there  discovered, achieve,  tr.  v.  —  ME.  acheven,  fr.  OF.  (=  F.) achever,  ‘to  accomplish,  complete’,  fr.  VL.  *ac- capare,  ‘to  come  to  an  end’,  fr.  L.  ad,  to  ,and *capare,  a  verb  formed  from  the  stem  of  L. caput,  ‘head’.  Cp.  OProven?.  Sp.,  Port,  acabar, of  s.m.,  and  sec  a  and  chief.
1497:acrid,  adj.  —  A  blend  of  L.  deer  (fern,  acris ,  neut. acre),  ‘sharp,  bitter’,  and  acidus,  ‘sour’,  which are  both  related  to  L.  acus,  ‘needle’,  acies,  ‘sharp edge,  point,  the  front  of  an  army,  line  of  battle, battle  array’,  acuere,  ‘to  sharpen’,  fr.  I.-E.  base *ak-,  *aq-,  ‘sharp,  pointed’,  whence  also  Oscan acrid  (=  L.  deriter),  ‘sharply’,  Umbr.  per-acri, ‘fruitful,  fertile’,  Gk.  axpop,  ‘at  the  farthest  point, highest;  pointed’,  4x4),  ‘a  point,  edge’,  4x1?,  ‘a point’,  axavS-a,  ‘thorn,  prickle’,  4 kwv,  ‘a  jave¬ lin’,  4x|X(ov,  ‘an  anvil’,  OI.  asrih,  ‘edge’,  asman-, ‘stone,  rock,  sky’,  Avestic,  asman-,  of  s.m.  Lith. akmuo,  ‘stone’,  asmuo  ,‘sharpness’,  OSlav.  kamy (a  metathesized  form),  ‘stone’,  OIr.  er  (for •akros ),  ‘high’,  Arm.  as-eln,  ‘stone’  (the  force of  the  suff.  -eln  is  yet  unknown),  ON.  hamarr, OE.  hamor,  hamer,  etc.,  ‘hammer’.  Cp.  Gk. axpodtopai,  ‘I  hear,  listen’,  prop,  ‘have  a  sharp hearing’,  in  which  the  first  element  is  rel.  to Sxpo p,  ‘pointed,  sharp’.  —  Cp.  the  gradational variant  base  *oq-,  whence  Gk.  6£u p,  ‘sharp’, oxpip,  ‘peak,  hilltop',  OL.  ocris,  ‘a  rugged,  stony mountain’,  L.  mediocris,  ‘middling,  moderate, indifferent,  tolerable'  (orig.  ‘being  half-way  up the  height  of  a  mountain’),  occa,  ‘a  harrow’, OSlav.  ostru,  Lith.  aitrus  (for  *okro,  with  in¬ serted  /),  ‘sharp’,  Mir.  ochar,  W.  ochr,  ochyr, ‘edge,  corner,  border’.  Cp.  awn,  eager,  ear  of corn,  edge,  egg,  ‘to  urge’,  hammer.  Cp.  also Acaena,  acantha,  acanthion,  acantho-,  Accipi- ter,  acerb,  acescent,  acetum,  acid,  Acipenser, acme,  acne,  Acocanthera,  acor,  Acreinae,  acri¬ mony,  aero-,  acroama,  acrobat,  acropolis,  Ac¬
1503:acrisia,  n.,  condition  of  disease  with  no  symp¬ toms  to  establish  the  diagnosis.  —  Gk.  axptaloi, ‘want  of  judgment’,  fr.  axpixop,  ‘not  judged’, fr.  4-  (see  priv.  pref.  a-)  and  xpixop,  ‘separated, chosen,  decided,  judged’,  verbal  adj.  of  xpfveiv, ‘to  separate,  choose,  decide,  judge’.  See  critic, acritical,  adj.  —  Formed  with  adj.  suff.  -al  fr. Gk.  icxpiTop,  ‘not  judged’.  See  prec.  word, aero-,  acr-,  combining  form  meaning  ‘pertaining to  the  end,  extreme’.  — ■  Gk.  4xpo-,  fr.  dtxpop, ‘at  the  end,  at  the  top,  outermost’,  fr.  4x4), ‘edge’ ;  cogn.  with  L.  acer,  ‘sharp’,  OSlav.  ostru, Lith.  aStrus,  of  s.m.,  OIr.  er,  ‘high’.  See  acrid and  cp.  words  there  referred  to. acroama,  n.,  oral  teaching;  esoteric  teaching.  — L.,  fr.  Gk.  4xp6ajj.a,  lit.  ‘that  which  is  heard (with  pleasure)’,  fr.  4xpo4opxi,  ‘I  hear’,  orig. ‘I  have  a  sharp  hearing',  fr.  *4xp-ouct4,  ‘a  sharp hearing’,  compounded  of  Sxpop,  ‘pointed, sharp’,  and  Ion.,  Att.  oop,  gen.  ouaxop,  cor¬ responding  to  Gk.  o5p,  gen.  <8x6?,  ‘ear’.  For the  first  element  see  acrid  and  cp.  acropolis.  For the  second  element  see  ear,  ‘the  organ  of  hear¬ ing’,  and  cp.  oto-.  For  the  ending  see  suff.  -ma. acroama  tic,  adj.,  oral;  esoteric.  —  Gk.  4xpoa- (j.axix6p,  ‘pertaining  to  hearing’,  fr.  4xpoapa, ‘that  which  is  heard’.  See  prec.  word  and  -atic. Derivative:  acroamatic-s,  n. acrobat,  n.  —  F.  acrobate,  fr.  Gk.  4xpo(3axop, ‘walking  on  tiptoe’,  fr.  Sxpop,  ‘at  the  end,  outer¬ most,  highest’,  and  pax-,  ‘going’,  from  the  stem of  Patvav,  ‘to  go,  walk’.  (Cp.  (foxfip,  ‘passable’, verbal  adj.  of  (JatvEiv.)  For  the  first  element see  aero-,  for  the  second  see  base,  n.,  and  cp. the  second  element  in  aerobatics.
1866:afflict,  tr.  v.,  to  distress.  —  L.  ajflictare,  ‘to  dam¬ age,  harass,  torment,  distress’,  freq.  of  affigere (pp.  afflictus),  ‘to  cast  down,  throw  down,  over¬ throw’,  fr.  ad-  and  fligere  (pp.  flictus),  ‘to strike’,  which  is  cogn.  with  Gk.  <pXf|3eiv,  ‘to press,  crush’,  Lett,  blaizit,  ‘to  press,  crush, strike’,  bliezt,  ‘to  strike’,  Czech,  Pol.  blizna, ‘scar’,  OSlav.  blizi,  blizu,  ‘near’,  W.  blif,  ‘cata¬ pult’,  blifaidd,  ‘quickly’.  Cp.  conflict,  inflict, profligate,  thlipsis.
1872:Derivative:  affranchise-ment,  n. affray,  tr.  v.,  to  frighten.  —  ME.  afraien,  affraien, formed — with  change  of  prefix — fr.  OF.  esfreer, *esfreier  (F.  effrayer ),  ‘to  frighten,  terrify’,  fr. Gaul.-L.  *exfridare,  'to  put  out  of  peace’, fr.  L.  ex-,  ‘out  of’  (see  ex-),  and  Frankish *fridu,  ‘peace’,  which  is  rel.  to  OE.  fridu,  OHG. fridu,  ‘peace,  truce’,  fr.  Teut.  base  *fri-,  which corresponds  to  I.-E.  base  *pri-,  ‘to  be  friendly, to  love’,  whence  OSlav.  prijati,  ‘to  aid,  help’, prijatelfl,  ‘friend’,  01.  prija-,  ‘beloved’.  Cp. OProveng.  esfredar,  ‘to  frighten’,  which  also derives  fr.  Gaul.-L.  *exfridare.  See  free  and words  there  referred  to  and  cp.  esp.  defray. Derivative:  affray-er,  n.
2063:Ajuga,  n.,  a  genus  of  plants  of  the  mint  family; the  bugle  weed  ( bot .)  —  A  ModL.,  hybrid coined  fr.  Gk.  privative  pref.  a-  and  L.  jugum, ‘joke’  (see  jugular  and  yoke);  so  called  from  the seeming  absence  of  the  upper  lip  of  the  corolla, akasa.  n„  the  name  of  space  in  Sankhya  philo¬ sophy.  —  OI.  akasa-,  ‘space’,  formed  fr.  em¬ phatic  pref.  a  and  kdsate,  ‘appears,  shines  ,  prob. from  I.-E.  base  *quek~,  *qv'eg-,  whence  also Avestic  ( ashman ,  ‘eye’,  akasat,  ‘he  beheld  ,Gk. x£xpcop,  later  form  x6xpap  (prob,  for  *qwek- mor),  ‘sign,  token’,  OSlav.  kazq,  kazati,  ‘to show’.  Cp.  ukase.
2098:alb,  a  long  white  vestment.  — -ML.  alba  for  L. alba  ( vestis ),  ‘while  (garment)’,  fern,  of  albus, ‘white’;  cogn.  with  Gk.  aXcp 64,  ‘dull-white  lep¬ rosy’,  SXcpi,  aXtptvov,  ‘barley  meal’,  OHG. albi3,  elbi3.  OE.  elfet,  ‘swan’,  lit.  ‘the  white bird’,  OSlav.,  Russ,  lebedi,  Serb,  labud,  Pol. labgdi,  Czech  labud,  ‘swan’,  for  orig.  *olh-edi, *olb-fdi,  *olb-(>di,  ‘the  white  bird’.  Cp.  also  Arm. alauni,  ‘white  pigeon,  dove',  Alb.  el'p,  el'bi,  ‘bar¬ ley’,  Hitt,  alpash,  ‘cloud’.  Cp.  abele,  ablet,  al¬ bedo,  albescent,  albino,  albite,  albo-,  Albuca,  al¬ bugo,  album,  albumen,  albumin,  alburnum,  at- phitomancy,  aubade,  aube,  auburn,  daub.
2141:aldehyde,  n.  ( chem .)  —  Coined  by  the  German chemist  Justus  von  Liebig  (1803-73)  from  the abbreviation  of  alcohol  de/rw/rogenatum,  alco¬ hol  deprived  of  hydrogen  . aldeia,  n.,  hamlet.  —  Port,  aldeia.  See  aldea. alder,  n.,  tree  rel.  to  the  birch.  —  ME.,  formed with  excrescent  d  fr.  OE.  alor ,  which  is  rel.  to OS.  elora,  ON.  dir,  Dan.  die,  el,  Swed.  al, MDu.  else,  Du.  els,  OHG.  erila  (fr.  earlier elira),  G.  Erie,  fr.  Teut.  •atiso;  cogn.  with Russ,  dlicha  (for  *alisa-),  ‘alder’,  Pol.  olcha,  of s.m.,  OSlav.  jellcha,  L.  alnus  (for  *alsnos),  Lith.
2145:ale,  n.  —  OE.  ealo,  alo,  rel.  to  ON.  67,  and  cogn. with  L.  alumen,  ‘alum’,  fr.  I.-E.  base  *alu-, ‘bitter’.  OPruss.  alu,  ‘mead’,  Lith.  aids,  OSlav, old,  ‘beer’,  are  Teut.  loan  words.  Cp.  alum, alumina,  aluta,  alutaceous. aleatory,  adj.,  depending  on  chance.  L.  dlea- tdrius,  ‘pertaining  to  a  gamester’,  fr.  alea,  ‘die, game  of  hazard’,  prob.  meaning  orig.  ‘mere chance',  and  derived  fr.  Gk.  iXsoq,  a  collateral form  of  vjXeo^,  ‘wandering  in  mind,  distraught, foolish’.  See  Aleochara  and  the  adj.  suffixes  -ate and  -ory.
2179:Algernon,  masc.  PN.  —  Lit.  ‘with  mustaches  ,  fr. OF.  als  gernons.  OF.  als  (F.  aux)  stands  for  a les,  lit.  ‘to  the’  (pi.),  fr.  L.  ad-  (see  ad-)  and  the plural  of  the  article  le,  fr.  L.  ille,  ‘that  one  ; see  ille  and  cp.  words  there  referred  to.  OF.  ger- non  is  a  collateral  form  of  grenon,  ‘mustache  , fr.  VL.  *grandnem,  acc.  of  *grand,  a  word  of Teut.  origin.  Cp.  OHG.  grana,  OE.  granu ,  mus¬ tache’,  G.  Granne,  ‘awn,  beard’,  fr.  I.-E.  base *gher-,  ‘to  stick  out’,  whence  also  OSlav.  grani, ‘point,  edge’,  W.  gran,  ‘eyelid’,  MIr.  grend, ‘whiskers’.
2381:versity.  —  L.  alumnus,  ‘a  nursling,  foster-son, disciple’,  for  *alo-menos ,  prop.  pass.  pres.  part, of  alere,  ‘to  nourish’ ;  see  old  and  cp.  alt.  For the  suff.  *-menos  cp.  Gk.  -pevo?,  the  suff.  of  the med.  and  pass,  part.,  and  L.  fe-mina ,  ‘woman’, lit.  ‘suckling  (woman)’,  and  see  feminine.  Cp. also  the  suffixes  of  the  words  Aeschynomene, calumny,  catechumen,  clement,  column,  ecumen¬ ic,  energumen,  hapax  legomenon,  hegumen, noumenon,  phenomenon,  prolegomenon, alurgite,  n.,  a  purplish  manganese  mica  (mineral.) —  Formed  with  subst.  suff.  -ite  fr.  Gk.  AXonpy/j?, ‘genuine  purple  dye’,  lit.  ‘wrought  in  or  by  the sea’,  which  is  compounded  of  a X?  (fem.),  ‘sea’, and  sp-fov,  ‘work’.  See  halieutic  and  ergon, alushtite,  n.,  a  hydrous  aluminum  silicate  (min¬ eral.)  —  Named  after  Alushta  in  the  Crimea. For  the  ending  see  subst.  suff.  -ite. aluta,  n.,  a  kind  of  soft  leather.  —  L.,  for  alu-ta, lit.  ‘leather  prepared  by  means  of  alum’,  rel.  to alumen,  ‘alum’.  See  alum, alutaceous,  adj.,  resembling  aluta.  —  L.  alutacius, fr.  aluta.  See  prec.  word  and  -aceous. alveolar,  adj.,  pertaining  to  alveoli.  —  Formed with  suff.  -ar  fr.  L.  alveolus.  See  alveolus, alveolate,  adj.,  pitted  with  small  cavities,  as  a honeycomb.  —  L.  alveolatus ,  fr.  alveolus.  See next  word  and  adj.  suff.  -ate. alveolus,  n.,  a  small  cavity.  —  L.  alveolus ,  dimin. of  alveus,  ‘a  hollow,  cavity’,  which  is  rel.  to  al- vus,  ‘belly’,  and  cogn.  with  Gk.  auX6?,  ‘tube, pipe’,  gv-auXo?,  ‘channel,  riverbed’,  auXtov, ‘hollow  way,  defile,  ravine,  glen,  channel,  strait’, OS1.  ullji,  Lith.  aulys,  Lett,  aulis,  ‘beehive’,  lit. ‘a  trunk  hollowed  out’,  OSlav.  ulica,  ‘defile; courtyard’,  Lith.  aulas ,  Lett,  aule,  ‘leg  of  a boot’,  OPruss.  aulis,  ‘shinbone’.  Arm.  ui,  uli, ‘way’,  yli,  ‘pregnant’.  For  the  correspondence of  Gk.  xuXo  ?  and  L.  ah  us,  alveus,  cp.  Gk. veupov,  ‘nerve’,  with  L.  nervus ,  of  s.m.,  and Gk.  7ra0po?,  ‘little,  small’,  with  L.  parvus ,  of  s.m. For  the  ending  see  suff.  -ole.  Cp.  carol,  hy¬ draulic.
2389:(formed  on  the  analogy  of  the  plural  sumus,  ‘we are’),  OSlav.  jesmi,  Lith.  esmi,  OPruss.  asmai, OIr.  am,  ‘I  am’,  fr.  I.-E.  base  *es-,  ‘to  be’.  See esse  and  cp.  are,  art,  is.
2395:(whence  Siapav,  ‘to  cut  through,  clear  away’), and  cogn.  with  OSlav.  jama,  ‘a  pit’, amaranth,  n.,  1)  a  mythical  plant  that  never  fades; 2)  any  plant  of  the  genus  Amaranthus;  3)  purple color.  —  Gk.  apapavTO?,  ‘unfading ;  amaranth’, fr.  A-  (see  priv.  pref.  a-),  and  the  stem  of  pocpod- veiv,  ‘to  put  out,  quench,  extinguish,  to  make to  waste  away’,  fr.  I.-E.  base  *m'er-,  ‘to  rub, consume,  wear  away’;  see  smart,  v.,  and  cp. marasmus.  The  ending  of  amaranth  (for  amarant) is  due  to  the  influence  of  plant  names  formed with  Gk.  avffo;,  ‘flower’.
2425:ambi-,  before  a  vowel  amb-,  combining  form meaning  ‘both,  on  both  sides’.  —  L.  ambi-, amb-, ‘around,  round  about’,  rel.  to  ambo,  ‘both’,  and cogn.  with  Gk.  apcpt,  ‘round  about’,  OI.  abhi- fah,  Avestic  aiwi-to,  ‘on  both  sides’,  OE.  ymbe, OS.,  OHG.  umbi,  ON.  umb ,  um,  MHG.  umbe, iimbe,  G.  um,  Gaul,  ambi-,  OIr.  imb-,  imm-, imme-,  ‘round  about,  about’,  and  with  Gk.  ap.tpo>, ‘both’,  Toch.  A  ampi,  ampe,  B  ant-api,  OI.  ub- hiu,  Avestic  uwa,  OSlav.  oba,  Lith.  abu,  Lett. abi,  OPruss.  abbai,  Goth,  bai,  OE.  ba,  ‘both’. See  both  and  cp.  amphi-  and  the  first  element  in ambsace,  ancile,  ancillary,  ancipital,  umlaut.  Cp. also  ember  days.
2587:ana-,  before  a  vowel  an-,  pref.  meaning:  1)  up, upward;  2)  back,  backward,  against;  3)  again, anew;  4)  exceedingly;  5)  according  to.  —  Gk. ava-,  dtv-,  ‘up  to,  upward,  up,  toward;  exceed¬ ingly;  back,  backward;  against’,  fr.  ava,  ‘up, on,  upon;  throughout;  again’,  rel.  to  avw, ‘above’,  and  cogn.  with  Avestic  ana,  ‘on,  upon’, L.  an-  in  anheldre,  ‘to  pant,  gasp’,  Goth,  ana, OE.  on,  an,  OSlav.  na,  Lith.  mi,  OPruss.  no,  na, ‘on,  upon';  fr.  I.-E.  base  *ano-,  ‘on,  upon, above’.  Cp.  on  and  a-,  ‘on’.  Cp.  also  the  pref. in  anhelafion.
2616:‘to  push  back’,  fr.  dvd,  ‘back’  (see  ana-),  and xpouciv  (for  *xpouast.v),  ‘to  knock,  strike, push’,  which  is  rel.  to  Homeric  xpoalvstv  (prob. for  *xpouadv-teiv),  ‘to  stamp,  strike  with  the hoof’,  and  cogn.  with  OSlav.  su-krusg,  su-kru - Siti,  Russ.  krusit\  Lith.  krusu,  kruSti,  ‘to  smash, shatter’,  OSlav.  kruchu,  ‘piece,  bit  of  food’, anadem,  n.,  a  wreath,  garland.  —  L.  anadema,  fr. Gk.  dvd8/)pa,  ‘band,  headband’,  fr.  dvaSetv, ‘to  bind  up’,  fr.  dvd  (see  ana-)  and  8eTv,  ‘to bind’.  See  diadem.
2662:anarthrous,  adj.,  unarticulated.  —  Gk.  avapftpo?, ‘without  joints’,  fr.  av-  (see  priv.  pref.  an-)  and dpffpov,  ‘joint,  limb,  organ’.  See  arthritis.  For E.  -ous,  as  equivalent  to  Gk.  -09,  see  -ous. Anas,  n.,  the  genus  of  ducks  (zool.)  —  L.  anas, ‘duck’,  cogn.  with  Lith.  antis,  OPruss.  antis, OSlav.  pty,  ORuss.  utovi,  Serb,  utva  (fr.  *pt-), ON.  ond,  OF.  eened,  MDu.  sent,  OHG.  anut, MHG.  ant,  G.  Ente,  and  prob.  also  with  Gk. vVjaaa,  Att.  vijxxa,  Boeot.  vaaaa,  ‘duck’,  OI. atih,  ‘waterfowl’.  Cp.  Anatidae,  Nesonetta.  Cp. also  smew.
2760:gi,  engi,  MHG.  enge,  G.  eng,  Goth,  aggwus, ‘narrow’,  and  cogn.  with  OI.  amhu-,  ‘narrow’, arrihah,  ‘anguish,  need,  anxiety’,  Avestic  qzah-, ‘distress,  oppression’,  Gk.  ayyeiv,  ‘to  squeeze’ (esp.  the  throat),  ‘strangle,  throttle,  hang’, ayyovY),  ‘strangling,  hanging;  rope’,  ivyi, ayyou,  ‘near’  (lit.  ‘narrow’),  anaov  (for  *<5iyy-iov), ‘nearer’,  L.  angere,  ‘to  press  together,  throttle, torment’,  angustus,  ‘narrow’.  Arm.  anjuk,  ‘nar¬ row’,  OSlav.  qzQ,  qziti,  ‘to  narrow,  compress’, qzota,  ‘narrowness’,  'qzosti,  ‘a  narrowing,  nar¬ rowness’,  qziiku,  ‘narrow’,  Lith.  ahkstas,  ‘nar¬ row’,  fr.  I.-E.  base  *angh-,  ‘to  narrow,  com¬ press’  ;  the  corresponding  Celtic  base  is  *engh-, *%gh-,  whence  Bret,  enk ,  ‘narrow’,  Ir.  cumung, ‘narrow’,  Ir.,  W.  ing,  ‘distress’.  Cp.  agnail,  an¬ gina,  anguish,  anxious,  and  the  second  element in  cynanche,  quinsy,  squinancy,  Orobanche. Derivatives:  angr-y,  adj.,  angr-i-ly,  adv.
2766:Derivatives :  angiosperm-al,  angiosperm-atous, angiosperm-ic,  angiosperm-ous,  adjs. angle,  n.,  comer.  —  F.,  fr.  L.  angulus,  ‘angle, comer’,  which  is  cogn.  with  Arm.  angiun,  anki- un,  OSlav.  qg(u)lu,  ‘comer’,  OSlav.  qkotu, ‘hook’,  Lith.  anka,  ‘loop’,  OI.  angam,  ‘limb’, angulih,  angurih,  ‘finger,  toe’,  angusfhdh,  ‘big toe,  thumb’,  Avestic  angushta-,  ‘toe,  finger’,  OI. ankah,  ‘hook;  bent’,  ancati,  ‘bends,  curves’,  Gk. a'f/.oc,,  ‘a  bend,  hollow’,  dyxtov,  ‘elbow’,  dyxuXo?, ‘crooked,  curved’,  SyxOpa,  ‘anchor’,  L.  ancus, ‘crooked,  curved’,  OE.  ancleo,  ancleow,  ‘ankle’, OE.  anga,  OHG.  ango,  ‘hook’.  All  these  words derive  fr.  I.-E.  base  *ang-,  resp.  *anq-,  ‘to  bend’. Cp.  angle,  ‘fishhook’,  Angle,  anchor,  ancon, angula,  angular,  ankle,  ankylosis,  and  the  second element  in  triangle.  Cp.  also  the  second  element in  sarangousty.  The  above  I.-E,  words  stand  in gradational  relationship  to  Gk.  oyxo?,  L.  un¬ cus ,  ‘hook’,  Mir.  ecath,  ‘fishhook’;  cp.  Uncaria, unciferous,  uncinal,  uncinate,  uncinus,  uncus, aduncus,  Redunca.
2790:(iehthyol.)  —  L.  anguilla ,  ‘eel’,  prop,  ‘the  snake¬ like  fish’,  fr.  anguis,  ‘snake’;  see  next  word.  Cp the  cognate  Gk.  eyzeau?  (see  Encelia),  OPruss. angurgis,  Lith.  ungurys,  OSlav.  *qgor[  (appear¬ ing  in  Russ,  ugori,  Pol.  wfgorz),  ‘eel’,  which  all mean  derivatively  ‘the  snakelike  fish’.  It.  an¬ guilla,  F.  anguille,  Sp.  anguila,  Port,  enguia  and prob.  also  OSlav.  qgulja,  fegulja,  ‘eel’,  derive  fr.
2812:Derivative:  animadversive-ness,  n. animadvert,  intr.  v.,  to  criticize,  blame,  censure. —  L.  animadvertere,  contraction  of  animum  ad- vertere,  ‘to  direct  one’s  mind,  attend’,  fr.  ani¬ mum,  acc.  of  animus,  ‘mind’,  and  advertere,  ‘to turn  toward’.  See  animus  and  advert, animal,  n.  —  L.,  lit.  ‘a  living  being’,  fr.  animale, neut.  of  animalis,  ‘of  air,  living’,  fr.  anima, ‘breath  of  air,  air,  breath,  soul,  life’;  see  animus and  adj.  suff.  -al.  For  sense  development  cp.  Gk. £<oov,  ‘animal,  which  is  rel.  to  tj&W),  ‘life’,  and OE.  deor,  ‘a  wild  animal’,  lit.  ‘a  breathing  being’, which  is  cogn.  with  OSlav.  duchu,  ‘breath, spirit’,  dusa,  ‘soul’.  Cp.  also  Heb.  hayydh,  ‘wild animal,  beast’,  which  is  rel.  to  hdydh,  ‘he  lived’, hayyim,  ‘life’.
2828:animus,  n.,  1)  intention;  2)  animosity.  —  L., ‘soul,  spirit,  mind,  courage,  wish,  desire’,  rel.  to anima,  ‘breath  of  air,  air,  breath,  soul,  life’,  and cogn.  with  Gk.  avE|jto<;,  ‘wind’,  fr.  I.-E.  base *an-,  ‘to  blow,  breathe’,  whence  also  OI.  ani-ti, ana-ti,  ‘breathes’,  ani-lah,  ‘breath’,  OIr.  anal,  W. anadl,  MBret.  (with  metathesis)  alazn,  ‘breath’, OIr.  animm,  Co.,  Bret,  eneff,  ‘soul’,  Goth,  uz- anan,  ‘to  exhale’,  ON.  anda,  ‘to  breathe’,  andi, ond,  ‘breath,  soul,  spirit’,  OE.  edian  (for  *an- j>jan ),  ‘to  breathe’,  OSlav,  vonja,  ‘smell’.  Alb. Gheg  o/.Tosk  Jh/I  sweH’,  Toch.  A  afima.  Arm. anjn ,  ‘soul’.  Cp.  animadvert,  animal,  animal¬ cule,  animate,  animosity,  equanimity,  exanimate, exhale,  inhale,  longanimity,  magnanimous,  mag¬ nanimity,  pusillanimous,  pusillanimity,  unani¬ mous,  unanimity.  Cp.  also  ahura,  anemo-,  an- helation,  asthma,  asura,  prana, anion,  n.,  a  negatively  charged  ion  ( physical chem.)  —  Gk.  aviov,  neut.  of  avicbv,  pres, part,  of  avi£vai,  ‘to  go  up’,  fr,  ava  (see  ana-) and  isvai,  ‘to  go’,  which  is  cogn.  with  L.  ire, ‘to  go’.  See  itinerate.  The  word  anion  was  in¬ troduced  into  electricity  by  the  English  physi¬ cist  and  chemist  Michael  Faraday  (1791-1867); cp.  ion,  cation.
3045:apatite,  n.,  calcium  phosphate  fluoride  (mineral.) —  Formed  with  subst.  suff.  -ite  fr.  Gk.  drrdxY), ‘deceit’  (see  Apatela);  so  called  because  it  has been  mistaken  for  other  minerals, ape,  n.  —  ME.,  fr.  OE.  apa,  rel.  to  OS.  apo,  ON. api,  Du.  aap,  OHG.  ajfo,  MHG.,  G.  affe;  ac¬ cording  to  O.  Schrader  borrowed  fr.  OCelt. aPpava?,  a  word  glossed  by  Hesychius.  It  is  more probable,  however,  that  OE.  apa,  etc.,  are  Slav¬ onic  loan  words.  Cp.  ORuss.  opica,  Czech opice,  ‘ape’.
3052:of  s.m.,  ON.  jdfurr,  ‘prince’,  and  with  OSlav. vepri,  Lett,  vepris,  ‘wild  boar’.  The  a  in  L.  aper (inst.  of  *eper)  is  prob.  due  to  dissimilation  un¬ der  the  influence  of  caper,  ‘he-goat’.  Cp.  the first  element  in  Everard.
3187:applausive,  adj.  —  ML.  applausivus,  fr.  L.  ap¬ plausus.  See  prec.  word  and  -ive. apple,  n.  —  ME.  appel,  eppel  fr.  OE.  eeppel,  aepl, rel.  to  OS.,  OFris.,  LG.,  Du.  appel,  ON.  eple, epli,  Dan.  xble,  Swed.  apple,  Norw.  eple,  OHG. apful,  afful,  MHG.,  G.  apfel,  Crimean  Goth. apel,  and  cogn.  with  Gaul,  avallo  (pi  ),  ‘fruit , OIr.  ubull,  ‘apple’,  aball,  ‘apple  tree’,  W.  afall, of  s.m.,  afal,  Co.,  Bret,  aval,  ‘apple’,  Lith. dbalas,  obuolas,  Lett,  abudlis,  OPruss.  woble, ‘apple’,  OSlav.  abluko,  jabluko,  ‘apple’.  Cp.  L. Abella  (now  Avella),  name  of  a  town  in  Cam¬ pania.  lit.  ‘Apple  town’.
3282:arable,  adj.,  suitable  for  plowing.  —  F.,  fr.  L. arabilis,  fr.  arare,  ‘to  plow’  (whence  aratrum, ‘plow’),  fr.  I.-E.  base  *ard-,  ‘to  plow’,  whence also  Gk.  apouv,  OSlav.  orjq,  orati,  Lith.  ariu, arti,  ‘to  plow’,  Lett,  aru,  ‘I  plow’,  Goth,  arjan, OS.,  OE.  erian,  W.  arddu,  ‘to  plow’,  Mir.  airim, ‘I  plow’,  Gk.  itpoxpov,  Cret.  Stparpov,  Arm. araur,  Mir.  arathar,  OSlav.  ralo,  Lith.  drklas, ON.  arfir,  Toch.  AB  are,  ‘plow’,  Gk.  Spoupa, ‘arable  land’.  See  ear,  ‘to  plow’,  and  -able  and cp.  Arval.
3369:ardor,  ardour,  n.  —  ME.  urdeur,  fr.  OF.  ardour (F.  ardeitr ),  fr.  L.  ardorem,  acc.  of  ardor,  ‘heat’, fr.  ardere,  ‘to  burn'.  See  ardent  and  -or. arduinite,  n.,  a  zeolite  (mineral.)  —  Named  after the  Venetian  geologist  Giovanni  Arduino.  For the  ending  see  subst.  suff.  -ite. arduous,  adj.  —  L.  arduus,  ‘high,  lofty,  steep  ,  fr. I.-E.  base  *eredh-,  * erdh -,  'to  grow;  high’, whence  also  Avestic  er*dva-,  'high',  Olr.  ard, ‘high’,  Alb.  rit,  OSlav.  rastp,  ‘I  grow’.  Cp.  I.-E. base  *weredh-,  ‘to  grow;  high’,  whence  OI. urdhvah,  ‘high’,  vardhate,  ‘causes  to  grow,  in¬ creases',  Gk.  updo c  (for  *"opd56p;  cp.  Dor. jjopdo-),  ‘straight,  right,  erect’.  See  ortho-  and cp.  vriddhi.  For  E.  -ous,  as  equivalent  to  L.  -us, see  -ous.
=== 1971
KLN_1971.txt:223781:Slav, n. and adj. — G. Slave, fr. ML. Sclavus, 
KLN_1971.txt:223788:ML. Sclavus , Slavus, fr. MGk. ZxXdcpo<;, 
KLN_1971.txt:223805:Slav, Slovak, Slovene. Accordingly the name 
KLN_1971.txt:223833:Slavonian, adj. and n., Slovene. — Formed with 
KLN_1971.txt:223835:ited by the Slavs’, fr. Sclavus. See Slav and -an. 
KLN_1971.txt:224320:orig. meaning ‘Slav’. See Slav and cp. Slovene. 
KLN_1971.txt:224328:Slovene, n., one of the Slav people inhabiting 
KLN_1971.txt:270167:by the Serbs, Croats and Slovenes. — See prec. 
KLN_1966.txt:35506:Slav,  n.  and  adj.  —  G.  Slave,  fr.  ML.  Sclavus, Slavus,  fr.  MGk.  T,v./.ir[hoq.  See  slave. Derivatives:  Slav-ian,  Slav-ic,  Slav-ish,  adjs., Slav-ism,  n.,  Slav-ist,  n.,  Slav-ist-ic,  adj.,  Slav- ize,  tr.  v.,  Slav-iz-ation,  n. slave,  n.  —  ME.  sclave,  fr.  OF.  (=  F.)  esclave,  fr. ML.  Sclavus,  Slavus,  fr.  MGk.  SxXdj hoq, axXdpo c„  ‘slave’,  prop,  ‘a  slave  of  Slav  descent’, back  formation  fr.  MGk.  LxX«pr,v6i:,  ‘per¬ taining  to  the  Slavs’,  from  the  n.  ol  DxXafJrpioi (pi.),  ‘the  Slavs’,  which  was  formed — with  in¬ serted  x — fr.  OSlav.  Stovgninu,  ‘Slav’.  This sense  development  arose  in  the  consequence  of the  wars  waged  by  Otto  the  Great  and  his  suc¬ cessors  against  the  Slavs,  a  great  number  of
KLN_1966.txt:35507:whom  they  took  captive  and  sold  into  slavery. For  sense  development  cp.  OE.  wealh,  ‘slave, serf’,  prop,  ‘foreigner,  Briton,  Welshman’. OSlav.  Sloveninu  is  a  derivative  of  OSlav.  slovo, ‘word’,  fr.  I.-E.  base  *kleu-,  ‘to  hear’,  whence also  OI.  sravas-,  ‘praise,  glory’,  Avestic  sravah-, ‘word’,  Gk.  xXi o;,  ‘fame’,  L.  cluere,  ‘to  hear’, OE.  hlu-d,  ‘loud’.  See  loud  and  cp.  esclavage, Slav,  Slovak,  Slovene.  Accordingly  the  name Slav  lit.  means  ‘speaker’.  For  sense  develop¬ ment  cp.  Church  Slavic  Nemici,  ‘Germans’, which  is  rel.  to  nemu,  ‘dumb’.
KLN_1966.txt:35513:Slavonian,  adj.  and  n.,  Slovene.  —  Formed  with suff.  -an  fr.  ML.  Sclavonia,  ‘the  country  inhab¬ ited  by  the  Slavs’,  fr.  Sclavus.  See  Slav  and  -an. Slavonic,  adj.  and  n.,  Slavic.  —  See  prec.  word and  adj.  suff.  -ic.
KLN_1966.txt:35595:Derivatives:  slough,  tr.  v.,  to  cast  off;  intr.  v.,  to be  cast  off  (said  esp.  of  the  skin),  slough-y,  adj. Slovak,  n.,  one  of  the  people  inhabiting  Slovakia, i.e.  the  eastern  part  of  Czechoslovakia;  adj.,  of Slovakia.  —  Fr.  Slovak,  the  people’s  own  name, orig.  meaning  ‘Slav’.  See  Slav  and  cp.  Slovene. Derivative:  Slovak-ian,  adj.  and  n. sloven,  n.,  an  untidy  or  careless  person.  —  ME. sloveyn,  a  hybrid  coined  fr.  Du.  slof  ‘careless’, and  ME.  suff.  -ein,  -eyn,  fr.  OF.  -ain,  fr.  L.  -anus (see  -an).
KLN_1966.txt:35596:Derivatives:  sloven-ly,  adj.,  sloven-!i-ness,  n. Slovene,  n.,  one  of  the  Slav  people  inhabiting Carinthia  and  Styria;  adj.,  of  Slovenia.  —  G. Slowene,  fr.  the  people’s  own  name,  orig.  mean¬ ing  ‘Slav’.  See  Slav  and  cp.  Slovak.  Cp.  also Slavonian.
```


## [2026-09-06T20:55:47.391Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN offset check\"; python3 -c \"\nimport json; d=json.load(open('../refs_online.json'));\nfor k in ['HRN','BQT','FFD','SNS','FRS','KLN','POK']: print(k, d[k].get('page_offset'), '|', d[k].get('lookup_hint','')[:300])\n\""
}
```


### [2026-09-06T20:55:49.169Z] TOOL RESULT

```
== HRN offset check
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
FRS different edition — no mapping | Look up the headword (entries grouped by final letter); FRS_pages.txt has \f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
```


## [2026-09-06T20:55:50.335Z] TOOL CALL #14: Bash

```json
{
 "command": "pdftoppm -f 270 -l 270 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg270 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T20:55:52.655Z] TOOL RESULT

```
total 2000
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:55 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    242 Sep  6 16:55 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb  43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82276 Sep  6 16:46 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87489 Sep  6 16:55 pg270.png
```


## [2026-09-06T20:56:22.878Z] TOOL CALL #15: Agent

```json
{
 "description": "Web research Iranian branch",
 "model": "opus",
 "prompt": "You are helping verify etymologies from Ali Nourai's \"An Etymological Dictionary of Persian, English and other Indo-European Languages\" (1999), page 240 (PDF 270), root \"Kleu 1\" = PIE *ḱleu- \"to hear\" (Pokorny 605).\n\nResearch the IRANIAN branch on the web (Wiktionary en.wiktionary.org, Etymonline, Encyclopaedia Iranica iranicaonline.org, Wikipedia) and report findings. The chart claims:\n\n- ROOT [Indo-European] Kleu 1 \"to hear\" (POK:605)\n- #1 [Avestan] \"sru 2, srav, xšnu, xšnaw\" : to hear  ← from root\n- #2 [Pahlavi] \"ašnŭdan\" : to hear  ← from #1\n- #3 [Persian] šenīdan «شنیدن» : to hear (also شنودن، شنو، حرف شنو) ← from #2\n- #4 [Avestan] \"sravah : word, speech ; srū-ta : speech ; sraw : to read ; srâw : to sing\" ← from root\n- #5 [Persian] sarvâ «سروا (سرواد، سرواده)» : poem, story (also سرود، سرودن، سراییدن، سرای ۲) ← from #4\n- #6 [Avestan] \"hu-srav : well famed, famous ; dâuš-sravah : ill-famed\" ← from root\n- #7 [Pahlavi] \"hu-srov\" : well-famed, title of kings and in-laws ← from #6\n- #8 [Persian] xosrow «خسرو (کسرىٰ)» : (well famed) king ; xosor «خُسُر (خسور، خسوره)» : father-in-law ; xošū «خُشو» : mother-in-law ← from #7\n- #9 [Pahlavi] \"du-srav\" : ill famed, infamous ← from #6\n- #11 [Avestan] \"sraothra, sraosha\" : ear, one who listens and follows ← from root\n- #12 [Pahlavi] \"srôsh\" : one who obeys (God) ← from #11\n- #13 [Persian] sorūsh «سروش» : one of God's angels ← from #12\n\nKEY QUESTIONS to settle with sources:\n1. Is NP شنیدن šenīdan really from Av. sru- via a form with xšnu/xšnaw? Note Nourai lumps Av. sru- \"hear\" with xšnu- \"know/be satisfied\". Modern view: MP ašnūdan/ašnaw- and NP شنیدن — Cheung (Etymological Dictionary of the Iranian Verb) derives it from Proto-Iranian *sru- (with prothetic vowel and a x-/ initial?), or from *xšnu-? What do Wiktionary/Cheung/Hasandust say? Which is right — is the initial š- from *sr- or from *xšn-?\n2. سرود / سرودن / سراییدن / سروا — from Av. sraoθra / srav- ? What does Wiktionary say for سرود and سرودن and سراییدن?\n3. خسرو Xosrow ← MP Husraw ← Av. Haosravah- / hu-sravah- \"of good fame\". Confirm.\n4. Crucially: are خسر (xosor, father-in-law) and خشو (xošū, mother-in-law) really from hu-srav \"well-famed\"?? Modern scholarship derives them from PIE *sweḱuros / *sweḱrūs \"father-in-law/mother-in-law\" (Latin socer/socrus, Greek hekyros, Skt śvaśura-, Av. x˅asura-), i.e. from *swe- family words, NOT from *ḱleu-. Check Wiktionary for خسر / خسو / خشو and Proto-Iranian *hwasura-, and Pokorny *swekuro-. This is likely a DISPUTED node.\n5. سروش Sorūš ← MP srōš ← Av. sraoša- \"obedience, hearkening\", the yazata Sraosha. Confirm; Av. sraoθra- \"ear/hearing\"?\n6. Av. dāuš-sravah- \"ill-famed\" and MP dušraw / dušrav — confirm existence.\n\nFor EVERY web page you actually read, archive it by running:\npython3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note 'page 270, root Kleu 1, <what you used it for>'\n(batch several in one Bash call). Only report URLs you actually fetched AND archived.\n\nReport back: for each numbered claim, a verdict (confirmed / plausible / disputed) with the concrete forms and sound changes, plus the archived URLs. Be concrete about intermediate forms (Proto-Iranian, Avestan, Middle Persian per MacKenzie, New Persian). Do NOT write any report files; reply in your final message."
}
```


### [2026-09-06T20:56:24.907Z] TOOL RESULT

```
Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: a841b6ea4f5ebdaa0 (internal ID - do not mention to user. Use SendMessage with to: 'a841b6ea4f5ebdaa0', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do not duplicate this agent's work — avoid working with the same files or topics it is using.
output_file: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tasks/a841b6ea4f5ebdaa0.output
Do NOT Read or tail this file via the shell tool — it is the full subagent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```


## [2026-09-06T20:56:42.404Z] TOOL CALL #16: Agent

```json
{
 "description": "Web research Slavic/English branch",
 "model": "opus",
 "prompt": "You are helping verify etymologies from Ali Nourai's \"An Etymological Dictionary of Persian, English and other Indo-European Languages\" (1999), page 240 (PDF 270), root \"Kleu 1\" = PIE *ḱleu- \"to hear\" (Pokorny 605).\n\nResearch the SLAVIC / GERMANIC / LATIN branch on the web (en.wiktionary.org including Reconstruction:Proto-Indo-European/ḱlew-, Reconstruction:Proto-Slavic/slovo, Reconstruction:Proto-Slavic/slověninъ; etymonline.com) and report. The chart claims:\n\n- ROOT [Indo-European] Kleu 1 \"to hear\" (POK:605)\n- #14 [Old Slavic] \"slovo : word ; Slověninŭ : Slav\" ← from root (ref KLN:1456)\n- #15 [Middle Greek] \"slabnovus : Slav, also slaves taken from the Slavs\" ← from #14\n- #16 [Middle Latin] \"slavous : Slav, slave\" ← from #15\n- #17 [French] (empty node) ← from #16\n- #18 [Persian] اسلاو ، چکوسلواکی ، یوگوسلاوی ← from #17\n- #19 [English] \"Slav, Yugoslavia, Czechoslovakia, slave\" ← from #17\n- #20 [Germanic] \"hlusinôn : to listen ; hlūdaz : loud\" (ref AHD) ← from root\n- #21 [English] \"listen, loud\" ← from #20\n- #22 [Latin] \"cluere : to be named\" (ref AHD) ← from root\n- #23 [English] \"client\" ← from #22\n\nKEY QUESTIONS:\n1. Proto-Slavic *slovo \"word\" from PIE *ḱlewos \"fame\" — confirm (cf. Gk kleos, Skt śravas-, Av. sravah-). Wiktionary Reconstruction:Proto-Slavic/slovo.\n2. Is *slověninъ \"Slav\" really derived from slovo \"word\"? Modern scholarship (Vasmer, Wiktionary, Trubachev) — many consider the derivation from slovo a FOLK ETYMOLOGY and prefer a derivation from a hydronym/toponym *slova (cf. *slaviti / *slova river names), or leave it unexplained. Get the modern view precisely.\n3. The Greek/Latin chain: Byzantine/Medieval Greek Σκλαβηνός (Sklabēnós) → back-formation Σκλάβος (Sklábos) \"slave\" → Medieval Latin Sclavus/Slavus → Old French esclave → Middle English sclave → slave. Confirm on etymonline (words: slave, Slav) and Wiktionary. NOTE: Nourai's chart prints \"slabnovus\" (Middle Greek) and \"slavous\" (Middle Latin) — these look like garbled Sklabēnós and Sclavus. Report the correct forms.\n4. English \"listen\" ← OE hlysnan ← PGmc *hlusinōn; \"loud\" ← OE hlūd ← PGmc *hlūdaz. Confirm via etymonline.\n5. Latin cluēre \"to be named, be spoken of\" from *ḱleu- — confirm. THEN: is English \"client\" from cluere? Watkins/AHD puts CLIENT under root *klei- \"to lean\" (Latin cliens < clinare \"to lean\"). Check etymonline.com/word/client and Wiktionary for Latin cliens. Report whether Nourai's link client←cluere is wrong (a minority older view held cliens < cluere, e.g. in some 19th-c. dictionaries — note if you find that).\n6. Persian اسلاو / یوگوسلاوی / چکوسلواکی — modern Persian borrowings; are they via French (as the chart says) or via Russian/English? Note what you can find.\n\nFor EVERY web page you actually read, archive it by running:\npython3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note 'page 270, root Kleu 1, <what you used it for>'\n(batch several in one Bash call). Only report URLs you actually fetched AND archived.\n\nReport back per numbered claim: verdict (confirmed / plausible / disputed) with concrete forms, dates, and archived URLs. Do NOT write any report files; reply in your final message."
}
```


### [2026-09-06T20:56:43.764Z] TOOL RESULT

```
Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: aa665fa421593e623 (internal ID - do not mention to user. Use SendMessage with to: 'aa665fa421593e623', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do not duplicate this agent's work — avoid working with the same files or topics it is using.
output_file: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tasks/aa665fa421593e623.output
Do NOT Read or tail this file via the shell tool — it is the full subagent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```


## [2026-09-06T20:56:45.461Z] AGENT

Now the local reference lookups while those run.


## [2026-09-06T20:56:46.765Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 198 (=p.177)\"; awk 'BEGIN{RS=\"\\f\"} NR==199' HRN.txt | head -80"
}
```


## [2026-09-06T20:56:47.487Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 129 (=p.108)\"; awk 'BEGIN{RS=\"\\f\"} NR==130' HRN.txt | head -80"
}
```


### [2026-09-06T20:56:48.520Z] TOOL RESULT

```
=== HRN leaf 198 (=p.177)
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


### [2026-09-06T20:56:50.218Z] TOOL RESULT

```
=== HRN leaf 129 (=p.108)
— 108
486. yi^usur 'Schwiegervater.
aw. /asitru' 'Schwiegervater ; ai. imruru-; arm.
skesr]ah\ d. i. 'Mann der Scliwiegermutter (Hübsch-
mann, Xo. 253).
kuvd. /a2ur, xozJ)\ /aur 'Schwiegervater ; afy. s^or;
bei. n. vasarik 'Schwiegervater, vasar\2ä/t *Schwager
(405); wa;K'. yjtrs, sar. (LW.) Xasur.
•Vergl. /Hsrä (No. 487).
487. xusrfi, zesä^ /jisü^ /'es etc. 'Schwiegermutter.
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
V
(vd. 6 (9) Gl., Say. näsäy. 2, 35). Vergl. de Lagarde,
Semitica 1,41, Nöldeke, ZDMG. 32, 408; de Lagarde
*J Phlv. ;(Osak (Sternbild, Bund.); kurd. t*st, vasi^ krisl; afy. vazai;
bei LW. hösay, d. hösay (100).
2) Vd. 5 (43) (44) steht zwei Mal xösinUan,
```


## [2026-09-06T20:57:07.915Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"swekuro\\|sekuro-\\|Schwiegervater\" POK_full.txt | head -20"
}
```


### [2026-09-06T20:57:07.965Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:57:09.331Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"xusrav\\|husrav\\|Chusrau\\|Xusrau\\|husrau\" HRN.txt BRT.txt PHD.txt NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-06T20:57:09.389Z] TOOL RESULT

```
HRN.txt:10707:aw. husravah-; ai. sufjrdvas-.
HRN.txt:15348:Husravali- V^.
NYB_vol2_glossary.txt:979:Béhistan [byhstn'] n. pr. f. 285. — NP bih ‘quince’; already Justi, NB 67, inter- preted the second element as Skr stana- ‘bust’. ‘having breast like quinces’. Cf the epithet beh-pistän applied to a woman, Unvala, King Husrav 35 (§ 96). The same -stan in Zarri-stan (g.v.). Cf, on the other hand, Bthl., ZsR I, 15 no., V, 20.
NYB_vol2_glossary.txt:2079:husravéh abstr. of the preceding w.: renown 891. — Paz. xusrübi.
NYB_vol2_glossary.txt:4291:Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
NYB_vol2_glossary.txt:6943:xūnāhin: xYan-asén xunar: hunar xurahe: xYarrah xüram: huram xurdak: xtartak xurséd: xLarxšēt xusrüb: husrav xusrubi: husravčh
NYB_vol2_glossary.txt:7512:Xusrav: Xēsrūi
BRT.txt:30513:•  j.  yä  aAmäf{Sp.  297  m.)  staota  yasnya srävaymi  ahummca  vairttn  trävaygni aamca  vahislim  "husraväni"  afiasca vattuhil  yaoidä^äne  Ny.  1^.  8.
```


## [2026-09-06T20:57:13.541Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10690,10725p' HRN.txt; echo \"=== which leaf?\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:10706])\nprint('leaf', t[:idx].count('\\f'), '-> printed page', t[:idx].count('\\f')-21)\nEOF"
}
```


### [2026-09-06T20:57:15.244Z] TOOL RESULT

```
123. karp 'Körper* (päz. karaf), arm. LW. kerp fiogtfi}.
aw. kerp- 'Körper*; ai. kfp-; lat. corpus.
np. kcUbud, kälbed 'Form, Körper , phlv. kärf)ut bezw.
kalput^ vd. 5 (32) Gl., ys. 9 (46), Bhmyt., kürpat bezw.
kälpat, Men. (päz. kälbüd) ist gr. ^aXonodioi' 'Schuster-
^) West: *broken', doch scheint 'gefallen* besser zu passen.— 283 —
leisten', wie Fleischer schon längst gesehen hat
(vergl. Nöldeke, Pers. Stud. II, 38)^).
124. ha» 'Glocke, nur vd. U (48).
aw. kqstra^ 'Glocke*.
125. katär 'welcher von beiden?' (AW.-Komm., AV.).
aw. katära- 'welcher von beiden'; ai. katard-.
X.
126. 'fvafstar 'schädliches, ahrimanisches Getier.
aw. /jafstra- ; np. xeräster findet sich nur in Parsen-
schriften.
127. fiisrav 'berühmt, erlaucht', x^isravih.
aw. husravah-; ai. sufjrdvas-.
np. /usrev 'Herrscher beruht dagegen auf einer Ver-
allgemeinerung des Personennamens aw. Hnsravak-,
Ebenso ^Xosrö der Xosröe^' (Nöldeke ZDMG. 45, 133
Anm. 2).
M.
128. "tnänsr 'Wort (heiliges)'.
aw. mqd^ra-; ai. mäfitra-. Mehr ritueller t. t.
Tomaschek stellt wa;^. mutr 'Zauberspruch' dazu;
unsicher.
129. mar Verderblich, schädlich* (AW.-Komni., AV.).
aw. mairya- 'verderblich, schädlich*.
Zu np. mär Schlange' vergl. oben No. 977.
130. maranclnltan 'tödten, vernichten', häufig.
aw. \/marC', merencaite 'tödten, vernichten'; ai.
l/^mard-, marcdyati 'versehren, beeinträchtigen*.
131. fnarzttan 'coitiren', mar2(i)sn 'Coitus, etc., vergl.
oben unter np. mallden (No. 962).
»J Fr. Müller, WZKM. 5, 263 leugnet die Richtigkeit dieser
=== which leaf?
leaf 304 -> printed page 283
```


## [2026-09-06T20:57:15.973Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB husrav\"; sed -n '2070,2085p' NYB_vol2_glossary.txt; echo \"=== PHD grep\"; grep -n \"husraw\\|husrav\\|srōš\\|srōs\\|dušraw\\|ašnaw\\|ašnūd\\|srūd\\|srāy\\|srāy-\" PHD.txt PHD_mackenzie.txt | head -40"
}
```


### [2026-09-06T20:57:16.041Z] TOOL RESULT

```
=== NYB husrav
hu-ram [hwlm] cheerful, glad 67%; bliss- ful, of Paradise, comp. ~-tar 66’. — Paz. cüram; NP xurram; in some way or other to be connected with Av. (1511) ram- ‘to rest, to repose’. Cf the next w. and huraméh.
hu-rām [hwl’m] blissful, of Paradise 76}. 857-12, — Paz. hüräm, Skr v. šubhānanda ; < hu + rām < Av. (1524) räman- ‘rest, peace’, from the same root as the pre- ceding w.; cf rāmēnītār, rämisn; cf also NP ram.
hu-ramak [hwlmk'] having good herds of cattle 5076, with the gl. ku ramak 4 apdrik veh dānēt dästan ‘that is: it knows how to breed other cattle [than sheep, ete.] in the best way’. — V. ramak. Paz. hurama; translates Av. (1857) hvq0wa-.
huramēh abstr. of hu-ram (g.v.): ~ kartan to enjoy oneself 4?5.
hu-rät [hwlt'] of good munificence, mu- nificent 511, with the gl. ku rdteh veh dānēt kartan ‘that is: it knows how to practise munificence in the best way’. — V. rātēh.
hu-srav [hwslwb'] of good honour, re- nown; renowned, illustrious: comp. ~-tar
www .parsianjoman.org | col ak,
hu-srav
699. — OIr *hu-sravah-, Skr su-éravas-; Paz. zusrūb; MPrs adj. hwsrwg < *hu- srava-ka- (A-H II), v. srav and Xosrod.
husravéh abstr. of the preceding w.: renown 891. — Paz. xusrübi.
Hušētar [hwšytl] the first of the three still unborn sons of Zartuxšt who will appear in the trimillenial apocalyptic period: 7114. 9619.17.39. — Paz. Hušečar; from Av. (384) Uxsyat.orata-.
Hušētarmāh [hwšytlm”h] the second ap- ocalyptic son of Zartuxšt who will appear after Hušētar: 7114, 988-14.16, 999. 11017. — Paz. Huseöarmäh; from Av. (384) Uz- šyat.nomah-, cf the spelling ?wšytnms DkM 44! (-ms inverse spelling of -mah).
hušk [hwšk'] dry, withered 197. 4124, — Av. (1840) huska- = OP; MPrthPrs hwék; NP zusk, cf hošitan. — 12814 hwsky: read hösak, q. v.
hu-tarist [hwtlst'] beautiful all round 5771, v. s. v. hu-örön and turist.
hu-taštak [hwt&tk'] well moulded, pl. cas. obl. ~-dn well moulded, beautifully shaped bowls 6014. — Av. (1823) hutästa- from taš-, v. tasitan.
hu-tohmčh [hwtwhrayh] good parentage 3917, — Abstr. of hu-tohm ‘of good seed’, v. tohm.
=== PHD grep
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
PHD.txt:400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:719:acquired gūšūsrūd.
PHD.txt:1877:fame husrawih, nàm.
PHD.txt:1879:famous husraw, nāmčištīg, nāmīg.
PHD.txt:1965:flautist nāy-srāy.
PHD.txt:2126:good (a.) huda(ha)g, nēk(ēg), new, weh, xūb, hu-, P naxšag; ~ char- acter huxémih; — deed huwatršt, kirbag; — repute husrawih; — rule hupādixšāyīh; ~ ruler hupádix- šā(y); ~ speech hüxt; ~ spirit spenag mēnēg; ~ thought humat; of ~ behaviour hukunišn; of ~ character huxém; of — religion hudén; of — repute husraw; of — speech hu-éwaz, hu-gówisn; of ~ stock pad-góhr(ag); of ~ thought humenišn.
PHD.txt:2215:harpist čang-srāy, kennār-srāy.
PHD.txt:2328:house Кадар, mān(d), srāy, xān(ag); v. lady, master; — and home xān ud man.
PHD.txt:2587:learnt gēšēsrūd,
PHD.txt:3266:protect pàdan, pahréxtan, srāyidan; (by spell) afsüdan.
PHD.txt:3396:repute, good — husrawih.
PHD.txt:3667:sing srūdan.
PHD.txt:3668:singing srāyišn.
PHD.txt:4584:1-2čīnag čīnišn čegāmag čegām-iz Cer čēlāngar čēlān Celangar čērīh čērīh- čērīhistan čim čim-gūwāgīh čimīg 1%īdan čand, čang Cand- éandih éandal Čang-srāy čandišn L?griw! éandidan cob
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD.txt:4790:srāy l?syáy- srāyišnīh srāyišn sarāsar srayidan sraxtag wad! sargén srišwadag
PHD.txt:5037:kan- har(w)! kanār, kennir kanāragūmand kanārag kennārsrāy kóx&- kūxšīdan kox&isnig kóxXi&n kawādak köv
PHD.txt:5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
PHD.txt:5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
PHD.txt:5415:duSoxig dušox dušxwaršt dušhumat gūšūsrūd dušxwadāyīh dušāgāh dušāgāhīh dūšāram dušarz dušīh dujdānāg yojdahr yójdahrih yojdahrgar yējdahrgarīh dujdén dušgēwišn dujgand dujgandīh dujdēysšrīh dūšīzagīh dēšīzag dujdatt
PHD_mackenzie.txt:2981:husraw [hwslwb I (M hwsrwg), N xusraw] famous, of good repute.
PHD_mackenzie.txt:6546:excellent cabuk, pAhlom, pASom.                    fame husrawih, nam.
PHD_mackenzie.txt:6548:excess frehbud(ih).                                famous husraw, namcistig, niimig.
PHD_mackenzie.txt:6670:    madan.                                       kirbag; ,..., repute husrawih; ,...., rule
PHD_mackenzie.txt:6676:gazelle ahlig.                                   huden; of ,...., repute husraw; of ,....,
PHD_mackenzie.txt:7451:repute, good""" husrawih.                riding aswarih.
PHD_mackenzie.txt:11914:ustBfrit            \tdQ)\ tU't"           husrawih                 ~)~t"
PHD_mackenzie.txt:11915:awestar-                -\~t""             husraw
```


## [2026-09-06T20:57:28.507Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ašnūdan\\|asnudan\\|ašnaw\" PHD_mackenzie.txt | head; echo \"---\"; grep -n \"Srūš\\|Sr[uū][sš]\" PHD.txt | head -5; echo \"=== NYB srav/srōš/asnūdan\"; grep -n \"^srav\\|^srōš\\|^Srōš\\|asnūtan\\|ašnūtan\\|^srūd\\|^srāy\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T20:57:28.590Z] TOOL RESULT

```
9865:widerisnih       ""U ~~\           asnudanI
---
4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
=== NYB srav/srōš/asnūdan
3509:srav [slwb'] word, message 4474, 454. 5524, — Av. (1643 sq.) sravah-, cf söbär.
5355:srav-: apa-sds
5356:srav-: srutan
5357:sravah-: srav
```


## [2026-09-06T20:57:31.998Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"asnūtan\\|āsnūtan\\|asnūt\\|snūtan\\|snav\\|Srōš\\|srōš\\|srūtan\\|srūt \" NYB_vol2_glossary.txt | head -25; echo \"=== PHD ašnūdan entry\"; grep -no \"ašnūdan[^|]*|[^]]*]\" PHD.txt | head -5; grep -n \"ašnūdan\" PHD.txt | head -3"
}
```


### [2026-09-06T20:57:32.096Z] TOOL RESULT

```
3446:"snavišneh [snwšnyh] 40? uncertain: Pourušasp went down to the waters of the Daiti river pat meno? kāmakēh (g.v., with a gl, v.s. v. apäyistan) u (pat) menči "snavišneh with the gl. ku ménoyan hamé sit. As the gl. is intended to explain snavišneh the very common w. sit ‘use, advantage' is little appropriate; most probably it should be emended do *snūt. For a vb. *snütan *snav-, however, no other support can be found, at least for the present, than the isolated hapaxlego- menon snus, n. sg. of snut. FrO XII, with the Phl gl. sökenet ‘he does useful work, serves'. Bthl (1630) regards this as a parallel form of (559) xšnu- (xšnav-) adj. ‘satisfying’, subst. ‘fulfilment of one’s duty’ from (557 sqq.) xšnav- ‘to satisfy’ and ‘to be satisfied’, and translates it ‘giving (another) what belongs to him by right, satisfying (another)’; he thinks the n. pr. Snaoya- (Yt. 13?9) belongs to this root (1627). Thus *snūtan snav- (most probably a NW vb.) possibly ‘to fulfill one’s (religious) duty’ : ‘in fulfilment of his duty towards Heaven’ with the explanation ‘he fulfilled his duty to- wards the heavenly beings’ (??).
3570:sūtē-karēh [swtyklyhy] supplication, en- treaty 1284, — sūtē- probably < OP *euti- from Av. (1648) srūtt-, v.s. v. srūtan and cf srav and sobdr.
=== PHD ašnūdan entry
5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
```


## [2026-09-06T20:57:38.473Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"šnav\\|šnu-\\|snav\\|sraw\\|srav\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T20:57:38.534Z] TOOL RESULT

```
487:*baid ‘to split’, Skt. srav / plav = Ir. *hrau / *fraw ‘to flow’, Skt. kram / gam / dram 
9943:*SANSKRIT: srav ‘to flow" (RV+) = EWAia П: 784 
9947:*IE COGNATES: Gr. petv ‘to flow, stream’, Arm. afoganel ‘to irrigate’, Lith. sravéti 
20869:s(i)rew-/s(i)rid, s(i)rüd ‘to sort out, select, separate’, ? Wa. sraw-/Srawd- ‘to peel off 
29484:(\DNb 24 |, Hinz 1965: 229), SUBJ. 25р. axsnavahy <a-x-S-n-v-a-h-y> (DNb 29), IMPV. 2sg. äxsnudiy 
29504:isnaveesteen/isnav-, Ham. esnoftan/esnov-, Jow. ma-fnoft/a-fno- ‘to hear, listen’, 
29513:bá-šn-, Sorkh. b-ceSnu-/cesnu-, Lasg. b-ásnav- ‘to hear || (+ *a-) Zaz. 
29522:*SANSKRIT: ksnav ‘to whet, sharpen’ (RV+) = EWAia I: 441 
29536:*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 
45295:isnavoestaen/isnav-, 456 
45343:b-äsnav-, 457 
51553:ksnav, 457 
52032:srav, 141 
52696:sravéti, 141 
55468:*CiaH', *xšnav (s.v.)
```


## [2026-09-06T20:57:40.534Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29470,29560p' CHEUNG.txt"
}
```


### [2026-09-06T20:57:40.581Z] TOOL RESULT

```
*NEIR: Oss. І. exsyzgon, D. axsizge “pleasant; urgently needed’ 

© Considering the limited distribution, *xsij may be a regional borrowing. 
*PIE LIV: - | Pok.: 


*хф паш ‘to hear (< ‘to sharpen (the ears)’)’ 
*AVESTAN: ? Y Av. hu-xsnuta- (+ *hu- ‘well’) ‘well-sharpened’ (Yt 10.24, Yt 10.39). 
9 On Av. xsnu- see also Kellens — Pirart 1990: 233f. 


*OLD PERSIAN: (+ *4-) 4-xSn(a)u- ‘to hear’ (cf. Benveniste 1946: 47 ff.) = Kent: 182 
Pres. athem.: IND. Isg. äx$nümiy <a-x-8-nu-u-mi-i-y> (ХР1 26), med. "axsnauvaiy <a-x-8-n-u-[v]-i-y> 
(\DNb 24 |, Hinz 1965: 229), SUBJ. 25р. axsnavahy <a-x-S-n-v-a-h-y> (DNb 29), IMPV. 2sg. äxsnudiy 
<a-x-8-nu-u-di-i-y> (DNb 54). © On axšnümiy see Hinz 1969: 46. It is no doubt a late formation, on 
which see Mayrhofer 1991: 201. 


*MIDDLE PERSIAN: (+ *а-) MMP ’Snw-, ВМР ’Snw- /ä-Snü-/ ‘to hear, understand’ 
c DMMPP: 57b 


Pres.: IND. 3pl. MMP ’šnwynd (M49 II R,13, M382 II A,6(1769)), SUBJ. Zeg. MMP пуу (M219 II 
R,9), ІМРУ. Zeg. MMP ‘пуу (M219 II R,14); Partic.: perf. pass. MMP ’snwd (M176 I V,14) 
*PARTHIAN: ‘Snw- ‘to hear, hearken’? = DMMPP: 93b f. 

Pres.: IND. 35р. ‘Snwyd, ‘Snwyyd, 3pl. ‘Snwynd (SS 53), SUBJ. 15р. ‘Snw’n, 3sg. ‘Snw’h, 1р1. ‘Snw’’m, 
IMPV. 2sg. ‘Snw-, 2р1. ‘Snwyd, ‘snwyyd; Partic.: pres. *‘Snw’g (|SS 7 |), perf. pass. '$nwd; Inf.: ’snwdn 
(M4572 II Ri,9(1024)), “šnwdn 

*NWIR: (simplex or with *a-) NP sinudan, Sunudan, Sanidan/Sanav- ‘to listen, hear’, 
Kurd. (Sina) Zinaftin/Zinaw-, Awrom. aZn(aw)iäy/-Znaw- ‘to hear’, Fariz. bäsno 
‘hear !’, Abz. asnida/ó-Snónov-, Anar. -aSnofte/asnov-, Bakht. asnidan, Gil. (Rsht.) 
isnaveesteen/isnav-, Ham. esnoftan/esnov-, Jow. ma-fnoft/a-fno- ‘to hear, listen’, 
Gur. (Kand.) Sinäft-/-Snäw-, Meim. bem-efnofi/a-fno?-, Khuns. esnev-/esnift, 
esneva, Nn. asnufle/asnov-, Natan. -$novä/sänäv-, Qohr. asnófta/asnóv- ‘to hear’, 


*xSnau2 ? 457 


Semn. -snüá, Sang. -osnünd-/osnovaen-, Shamerz. -äšní-/šänám-, Siv. esn-/esni, Soi 
bá-šn-, Sorkh. b-ceSnu-/cesnu-, Lasg. b-ásnav- ‘to hear || (+ *a-) Zaz. 
asnawitiS/asnawen- ‘to hear’. Ф It is almost impossible to distinguish between ап 
initial prothetic vowel and the old preverb *a-, which can disappear or be 
assimilated after a tense marker. 

*NEIR: ? Wa. К$ыу-/К$әп- ‘to hear’, (caus.) К$ыу(ы)у-/К$оуоуа ‘to rebuke’ (rather 
*Hax$ ?) Ф The Wa. forms are "phonetically difficult to explain", Steblin- 
Kamenskij, ibid. 

*SANSKRIT: ksnav ‘to whet, sharpen’ (RV+) = EWAia I: 441 


«PIE *ksneu- ‘to sharpen’ = LIV: 373 | Pok.: 585 

*REFERENCES: Horn 1893: 177; Zhukovskij I: 20, 156; КРЕТ: 81a f., 140a f., 207b, 247a; Ivanow 1926: 
422; KPF II: 205; Christensen, Contributions I: 69, 167, 261; Christensen, Contributions II: 59, 116, 160; 
Abrahamian 1936: 113; Lambton 1938: 42b, 78a; MacKenzie 1966: 89; Nyberg II: 34b; WIM I: 68; WIM 
Ш: 104; Vahman — Asatrian 1991: 77; Werba 1997: 174; Paul 1998: 291; Steblin-Kamenskij 1999: 212; 
Lecoq 2002: 120, 122, 131, 133 (passim) 


*xÉnau^ ? ‘to exchange gifts (between host and guest) (whence: ‘to entertain, 
welcome (a guest), to thank, praise, etc.’)’ 
*AVESTAN: xšnu- ‘to entertain, welcome, take care of (a guest)’, OAv. xSanmanai 


"instead" (Y 29.9) = Liste: 17 

Pres. {1} athem.: OPT. 2sg. YAv. xsnuiiá (Y 68.9), med. OAv. xsnouuisà (Y 28.1); Pres. {2} athem. red.: 
ОРТ. 2sg. med. YAv. "kuxsnuuisa (FrW 7.2); Aor. s-: 3sg. INJ. OAv. xšnauš (Y 46.13, Y 51.12), med. 
3sg. YAv. xsnaosta (P 49), SUBJ. 15р. med. OAv. xSnaosai (Y 46.1), 3р1. OAv. xšnaošən (Y 30.5); 
Partic.: pres. (2) kuxsnuuana- (Yt 8.49, H 2.13), aor. OAv. xsnaosomna- (Y 46.18), perf. pass. xSnüta- (Y 
31.3, Y 51.9, Y 60.2); Caus.: pres. IND. 3sg. YAv. xsnauuaiieiti; Desid.: pres. IND. 15р. OAv. cixsnusa 
(49.1) 

*OLD PERSIAN: хёпи- ‘to be satisfied, glad’ > Kent: 182 

Partic.: perf. pass. xSnuta- <x-S-nu-u-t> (DNb 26) 

*MIDDLE PERSIAN: MMP ‘snwm- (denomin.) “о propitiate’ || BMP sn’dyn- /snayen-/ 
(sec. caus.) ‘to praise, propitiate’, BMP hwsnwtk /hosnud/ /husnüd/, BMP hwsnwtk 
/hosnudag/ /husnudag/ ? ‘satisfied, content > DMMPP: 94 

Pres.: IND. 3sg. MMP ‘snwmyd {hapax} || Caus.: pres. IND. 3sg. BMP sn'dynyt /Snayénéd/; Inf.: caus. 
BMP Ssn’dynytn /Snayénidan/; Partic.: perf. pass. BMP sn’dynyt /Snayénid/ 

*SOGDIAN: SSogd. ’xSnyBnt ‘hospitable, dienerfreundlich’
```


## [2026-09-06T20:57:53.030Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*srau\\|\\*srau ‘\\|srau1\\|srau2\\|\\*sraw\" CHEUNG.txt | head -20; echo \"---\"; grep -n \"sorud\\|surud\\|sarayidan\\|sarudan\\|srüdan\\|srūdan\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T20:57:53.091Z] TOOL RESULT

```
23313:*srau ‘to hear, listen’ 
58258:*srau (S.V.) 
---
23347:/srüd/; Inf.: BMP slwtn /srüdan/ || (+ *fra-) Pres.: IND. 35р. frsr‘’yyd, 3р1. MMP “frsr’ynd, SUBJ. 3pl. 
23368:*NWIR: NP surudan/saray-, Kurd. (Kurm.) stirin/strin-, stir- ‘to sing’, ? Bal. (EHB)
```


## [2026-09-06T20:57:55.078Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23313,23400p' CHEUNG.txt"
}
```


### [2026-09-06T20:57:55.124Z] TOOL RESULT

```
*srau ‘to hear, listen’ 

*AVESTAN: srao- ‘to hear, listen’ || (+ *abi-) ‘to hear, understand’ || (+ *upa-) ‘to hear 
upon, understand’ || (+ *fra-) ‘to be heard, known [pass., impers.]’ || (+ *ui-) ‘to 
learn, hear from’ = Liste: 66f. 

Pres. nu-: IND. 3sg. YAv. surunaoiti (Yt 10.107, FrW 10.41), 3sg. them. YAv. (auui) surunuuaiti (N 24, 
N 60), 3р1. YAv. ()upa.surunuuainti (N 21), ОРТ. Zeg. YAv. surunuiia (Y 68.9); Aor. {1} athem.: IND. 
med. 3р1. OAv. asruuätom (Y 30.3), med. 2р1. OAv. asrūdūm (Y 32.3), SUBJ. 3sg. YAv. srauuat (F 12), 
OPT. 1р1. OAv. srouummä (28.7), IMPV. 35р. OAV. sraotü (Y 45.6, Y 49.7, Y 49.9), 2р1. OAv. sraota (Y 
30.2, Y 33.11, Y 45.1); Aor. {2} s-: SUBJ. med. 15р. OAv. soraosane (Y 50.4); Perf.: IND. med. 15р. 
Y Av. susruiie (Yt 17.17), 1р1. sūsrūma (Yt 13.148); Partic.: pres. surunuuat- (Y 35.4, Yt 8.3, cf. Panaino, 
Tist. П: 91), caus. YAv. sräuuaiiant-, med. Y Ау. sräuuaiiamna-, desid. Y Av. susrusomna- (Yt 14.21), aor. 
{1} YAv. aiBisr(a)uuana- (V 3.40), aor. {2} them. YAv. sraosomna- (V 13.17 Ё), perf. pass. YAv. srüta- 
(N 37, Y 22.25, Y 25.6, etc.), OAv. frasrüta- (Y Y 50.8), YAv. frasrüta- (Y 27.7, Y 65.3, Yt 8.2); Inf.: 
pres. caus. OAv. sräuuaiienhe (Y 29.8), YAv. sräuuaiieiöiiäi (Vyt 46), aor. OAv. srüidiiai (Y 34.12, Y 
45.5); Pass.: pres. IND. med. 1sg. OAv. sruiie (Y 33.7), INJ. 3sg. YAv. visruiiata (Yt 13.91), aor. INJ. 
3sg. OAv. srauui (Y 32.7 f., Y 49.7, Y 49.9); Caus.: pres. IND. 35р. YAv. srauuaiieiti (V 18.9, N 26, 
VdPZ 18.51-52, etc.), 3du. YAv. srauuaiiato (N 23), 3pl. YAv. srauuaiieinti (N 29, N 31), INJ. 2sg. YAv. 
frasräuuaiiö (Y 9.14), 3sg. Y Av. frasräuuaiiat (Y 57.8, V 19.2, V 19.10), SUBJ. 1sg. YAv. srauuaiieni 
(Ny 4.8), 3sg. ҮАУ. fra.srauuaiiaiti (N 33, N 72), 3sg. YAv. fra.va sräuuaiiät (Y 19.6), 3pl. ҮАУ. 


*srag ? 357 


sräuuaiian (N 85), ОРТ. 25р. YAv. sräuuaiiöis (V 11.2, P 15), 35р. YAv. sräuuaiiöit (N, FrW 7.2), 1р1]. 
OAV. srauuaiiaemà (Y 49.6) 
*MIDDLE PERSIAN: MMP sr’y-, BMP sl’d- /sray-/ ‘to sing’ || (+ *fra-) MMP frsy- ‘to 


praise, laud’, frsr’’y- ‘to sing’ > DMMPP: 308b, 156b 

Caus.: pres. IND. 3pl. MMP sr’ynd’, sr'yynd, BMP sl’dynd /srayend/; Partic.: perf. pass. BMP slwt 
/srüd/; Inf.: BMP slwtn /srüdan/ || (+ *fra-) Pres.: IND. 35р. frsr‘’yyd, 3р1. MMP “frsr’ynd, SUBJ. 3pl. 
MMP prsr’y’nd, IMPV. 2pl. frsryyd; Partic.: perf. pass. MMP prsrwd ‘song’ 

*PARTHIAN: sr’w- (caus.) ‘to sing’ > Ghilain: 76 | DMMPP: 308b 

Pres.: IMPV. 2pl. sr’wyyd {hapax} 

*SOGDIAN: CSogd. sr’w- ‘to sing’ (< *to let it hear’), CSogd. sr’wtyty (obl. pl. f.) 
‘songs’ (C2 102R.30) || (+ *pati-) BSogd. ptsr’w ‘to consecrate (with a mantra)’ 
Pres.: IND. 3pl. CSogd. sr’wnt; ’z-Impf.: IND. 3pl. CSogd. sr’w’znt || (+ *pati-) Caus.: pres. OPT. 3sg. 
BSogd. ptsr’w’y 

*CHORESMIAN: šw- ‘to be heard’. 9 According to Samadi (l.c.) Chor. š'wt means 
“entschlüpfte’ (of words), for which she reconstructs: *fra-uata-, cf. Khot. hot- ‘to be 
able’, Pth. frwd ‘to understand, know’. The meaning may rather be ‘was heard’, as 
added by MacKenzie V: 73. Accordingly, the Chor. form is to be connected to *sru- 
‘to hear’. Since intervocalic -i- has usually been retained, §’wt cannot go back to 
pass. *sruja-, suggested by MacKenzie (l.c., also accepted by Sims-Williams 1989: 
263). The voiceless -t- may derive from *-St- (cf. mtyk ‘broken’ < *mastaka-, CLI: 
195), whence š wt < aor. stem (med.) *sraus-(ta-) ? © Samadi: 200 

*NWIR: NP surudan/saray-, Kurd. (Kurm.) stirin/strin-, stir- ‘to sing’, ? Bal. (EHB) 
sunid-/sun- ‘to hear’ 

*NEIR: Sh. Xin-/Xüd, (Baj.) Xan-, Rosh. Xan-, Orosh. Xan-/Xüd, Sarig. Xan-/Xid, Xüd, 
Yzgh. xan-/Xod ‘to hear’, Pash. Xayol/Sayom (caus.) ‘to show, teach, instruct’, Sh. 
(Вај.) Xanen-, Xinawen-, Sariq. Xandon- ‘to cause to hear’ || (+ *us-) Yi. usa-/usävd, 
M. ušáv-/ušávd ‘to call, shout’, ? Sh. xöy-/Xeyd, Rosh. Xeyt, Bart. Xoyd, Sariq. 
Xuy-/Xoyd ‘to read’ 

*SANSKRIT: Ѕгау ‘to hear’ (RV+) = EWAia II: 666 

© This root has an impeccable IE etymology. 

«PIE *Kleu- ‘to hear’ = LIV: 334 f. | Pok.: 605 f. 

*IE COGNATES: Gr. £xAvov ‘heard’, KAvtdc ‘famous’, Lat. cluére ‘to be called, to be 


mentioned’, Toch. käln- ‘to sound’, Latv. sludinät ‘to declare’, etc. 
*REFERENCES: EVP: 79; IFL П: 193b; EVS: 102b, 104b; Cabolov 1997: 73; Werba 1997: 246 f.; 
Steblin-Kamenskij 1999: 334; NEVP: 99; Korn 2005: 130, 147, 321, 383 


*srag ? ‘to esteem, be boasting’ 

*KHOTANESE: ssahana- ‘quality, virtue’ 

*NEIR: Pash. Xäy- ‘to like, prefer, esteem’ 

*SANSKRIT: ślāgh ‘to be boasting, praise, commend, trust in = EWAia П: 673 


358 *staH
```


## [2026-09-06T20:58:10.596Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg270.png"
}
```


### [2026-09-06T20:58:10.933Z] TOOL RESULT

```

```


## [2026-09-06T20:58:10.931Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T20:58:25.439Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 270 -l 270 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg270hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg270hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.33),int(h*0.55),int(w*0.68),int(h*0.66))).save('crop_slav.png')\nim.crop((int(w*0.20),int(h*0.13),int(w*0.80),int(h*0.28))).save('crop_top.png')\n\""
}
```


### [2026-09-06T20:58:29.022Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T20:58:31.182Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_slav.png"
}
```


### [2026-09-06T20:58:31.196Z] TOOL RESULT

```

```


## [2026-09-06T20:58:38.402Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 leaf 205 (p.748)\"; awk 'BEGIN{RS=\"\\f\"} NR==206' BQT_v2_pages.txt | head -60"
}
```


### [2026-09-06T20:58:39.972Z] TOOL RESULT

```
=== BQT v2 leaf 205 (p.748)
  ‫خس‌در دهان گرقتن‬                                                                              ‫‪1‬ع‬
                                                                                                 ‫‪۷‬‬


 ‫لباسی باشد که درویشان وفران پوشند وازآن‬              ‫جست ه بفتح اول بروزن مست» ماضی‬
 ‫یشمها وموبها اوبزان باشد‪ - ۷‬وخرقه ایرا لیز‬           ‫حستن و آزرده ساختن باشد بعنی مجروح کرد‬
 ‫کونند که از بارچپای الوان دوخته شده باشد ؛‬            ‫ویند‬ ‫وآزرده ساخت ‪ - ۱‬ورنگ ولون را نکیز‬
                       ‫وفتح اول هم آمده اس‬            ‫ویمعتی تفع وفایده هم‌هست ‪ -‬وبضم اول بمعتی‬
                                                      ‫حامه را لیز‬    ‫و آستن‬        ‫فرار و ارام باشد ‪-‬‬
 ‫خستو نه بضم اول بر وکزلنگونه ‪.‬‬
                                                                                               ‫گفتها ند‬

                                            ‫باشد‬       ‫خستر؟ ‪ -‬برورن کفتر‪,‬حثرات‌الارض‌را‬
 ‫وزن دسته ‪.‬‬   ‫اول بر‬    ‫حسته ‪ -‬بفتح‬
                                                           ‫کوند همچو مورو مار وموش وامثال آن‬
 ‫ثال آن باشدھ ‪-‬‬
              ‫ووزاردم]‬     ‫استخوان‌خرما وش‬
                     ‫لفتوالو‬                          ‫خستی ‪ = ۲‬بپروزن بستن بمعنی‌ مجر وج‬
 ‫ومجروح وزخم خورده وسماررا لیزکو ند ‪ 6‬ہے‬                              ‫کردن ‪ -‬ومجروح شدن باشد ‪.‬‬
    ‫مندخ‪-‬فوف‬
           ‫زومینی که آنرا شریکارده باش‬                ‫حستو ت بفتح اول بروزن بدخو » دانۀ‬
 ‫‪ -‬ونم اول بمعنیهی‬     ‫خاسته وبرخاسته هم هت‬
                                                      ‫میوهارا کوبند همچودانةٌ زآرلدو وشفتالو وخرما‬
                           ‫وبنورة دیوار باشد ‪.‬‬
                                                      ‫و مانند آن ‪ - ۴‬و م اول ناممکی از اکابر‬
 ‫حسته نك = بابای ابجد بروزن هرزه‬                      ‫وبزرکان چن است ‪ -‬واقرار واعتراف کننده را‬
‫لیزگفته‌اند(‪ -)۱‬وبمعنی‌جانورخز ندحهمبذظر آ مده خند ‪ .‬پارچه‌ای کروایند کهچون دستی بایایی‬
 ‫شکته باشد بدان بندند ‪ -‬و کی را تیز گوبند‬                                                      ‫است ® ‪.‬‬
 ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
 ‫وهرچیز که انرابرزخ‌بندند خواه پلرچه باشد‬              ‫افرار و اعتراف کنندکان و معترف شکدانرا‬
                                     ‫خواه هر هم‪.‬‬                                     ‫گویند ‪.‬‬
  ‫ان گر فتی‪ -‬بسنی‌خس‬
                   ‫خدسهدر‬                              ‫حستو انه = پم اول‌بروزن خرواله»‬

                            ‫‪ -:‬را و‬     ‫(‪)۲‬چك‪ .‬چش‬                   ‫)‪ (۱‬چك ‪,‬چش‪ :‬کونند ‪۳‬‬


                ‫«خراستر» (ه‪.‬م‪ = . ).‬خرفتر‪.‬‬            ‫مخفف‬
                                                         ‫‪۴‬‬               ‫رك ‪ :‬خستن ‪.‬‬      ‫‪۱‬‬
   ‫‪ - ۴‬هلوی ‪ 08152۷5‬ک(وفتن ‪.‬كتك زدن) «ناوادیا ‪ ۷۹۱2‬ورگ ‪ :‬اسفا! ‪:‬ص‪. ۲۸۱‬‬
    ‫هه بهلوی ‪6-4۵1‬‬               ‫‪.‬‬    ‫ورك ‪ 1‬استخوان‬    ‫هته(ه‪.‬م‪.).‬‬    ‫چ‬   ‫(ھ‪.‬م‪(.‬‬     ‫و‬     ‫‪۴‬‬

                                                            ‫‪۲ : ۱‬ص‪٩۸۱٥‬‏ رك ‪ :‬خستوان ‪:‬‬            ‫«اسفا‬

               ‫کرچه کوا تخواهندازختو‪.‬‬                      ‫بقرنل اوکوا کنراند دل‬
     ‫‪۰‬ت‪۹۰4‬‬
         ‫ر«ی ل‬
             ‫فای‬
               ‫فرخی س‬
    ‫ار«له ص ‪٩۸۱٩‬‏ ‪ ۰‬ارمنی ع ‪582701905‬‬
                                    ‫هف)‬
                                      ‫دتر‬
                                        ‫‪-‬هلوی ‪( 0200052‬مقر ‪ ,‬مع‬
                                                              ‫‪ ۱‬ب‬
                                                                          ‫‪.‬‬       ‫*اسفا! ‪ ۲ :‬ص ‪۵۸۱‬‬
           ‫زختواله جه مابه هت شوشتری؟‬                 ‫‪ - ۷‬نگر زسنك چهمابه بت کوهرسرخ‬
    ‫معروفی‌بلخی‪« .‬لت‌فری ‪۸44‬‬
    ‫‪ ۸‬ح هته(وم‪ 2152 ,158- ).‬استخوان(ه‪.‬م‪« ).‬اسفاا ‪ ۲:‬ص‪»۲4۱ ۰ ۷۱‬ورك‪:‬خستو‪.‬‬
   ‫‪« : ۲2۱‬روی زبيا مرحم دلهای‌خته‬         ‫‪ ۰‬رك ‪ :‬اسفاا ‪:‬‬
                                         ‫‪۲‬ص‬                          ‫اسم مفمول از «خ‪‎‬‬      ‫‪a‬‬
```


## [2026-09-06T20:58:47.633Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'خسرو' in p or 'خشو' in p or 'خسر ' in p:\n        print(i, 'printed~', i+543, [w for w in ['خسرو','خشو','خسر '] if w in p])\nEOF"
}
```


### [2026-09-06T20:58:49.590Z] TOOL RESULT

```
29 printed~ 572 ['خسرو']
37 printed~ 580 ['خسرو']
44 printed~ 587 ['خسرو']
57 printed~ 600 ['خسرو']
84 printed~ 627 ['خسرو']
108 printed~ 651 ['خسرو']
125 printed~ 668 ['خسرو']
127 printed~ 670 ['خسرو']
157 printed~ 700 ['خشو']
162 printed~ 705 ['خسرو']
169 printed~ 712 ['خسرو']
182 printed~ 725 ['خسرو']
187 printed~ 730 ['خسرو']
198 printed~ 741 ['خسرو']
201 printed~ 744 ['خسرو']
206 printed~ 749 ['خسرو', 'خسر ']
207 printed~ 750 ['خسرو', 'خسر ']
208 printed~ 751 ['خشو']
213 printed~ 756 ['خشو']
214 printed~ 757 ['خشو']
217 printed~ 760 ['خسرو']
226 printed~ 769 ['خسرو']
245 printed~ 788 ['خسرو']
246 printed~ 789 ['خشو']
252 printed~ 795 ['خسرو', 'خشو']
253 printed~ 796 ['خسرو', 'خشو']
254 printed~ 797 ['خشو']
257 printed~ 800 ['خسرو']
259 printed~ 802 ['خشو']
269 printed~ 812 ['خسرو']
270 printed~ 813 ['خسرو']
337 printed~ 880 ['خسرو']
369 printed~ 912 ['خسر ']
388 printed~ 931 ['خسرو']
394 printed~ 937 ['خسرو']
449 printed~ 992 ['خسرو']
473 printed~ 1016 ['خسرو']
474 printed~ 1017 ['خشو']
477 printed~ 1020 ['خسرو']
478 printed~ 1021 ['خسرو']
486 printed~ 1029 ['خشو']
523 printed~ 1066 ['خسرو']
537 printed~ 1080 ['خسرو']
555 printed~ 1098 ['خسرو']
556 printed~ 1099 ['خسرو']
559 printed~ 1102 ['خسرو']
572 printed~ 1115 ['خسرو']
588 printed~ 1131 ['خسرو']
589 printed~ 1132 ['خسرو']
591 printed~ 1134 ['خسرو']
609 printed~ 1152 ['خسرو']
617 printed~ 1160 ['خسرو']
636 printed~ 1179 ['خسرو']
648 printed~ 1191 ['خسرو']
672 printed~ 1215 ['خسرو']
678 printed~ 1221 ['خسرو']
```


## [2026-09-06T20:59:02.623Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (206,207):\n    print('#### index',i)\n    print(t[i][:4500])\nEOF"
}
```


### [2026-09-06T20:59:04.327Z] TOOL RESULT

```
#### index 206
  ‫با]س‬
     ‫ی‬


‫»ابه از‬
      ‫خسرو اقلیم چهادم کن‬                      ‫بدهن گرفتن است ککنهایه ازعاجزشدن وزیشهار‬
                      ‫آفتاب عالمتاب است ‪.‬‬                     ‫‪۱‬‬                    ‫خواستن باشد ‪.‬‬
‫حسرو انحم = بمعنی خرو اقلم‬                     ‫حسره بفتح اول و انی بر وزن شرر »‬
     ‫چهارم است که خورشید عالم|راست (‪.)۱‬‬        ‫و آن آیی است که در زمستان‬             ‫شخد‬
                                                                                       ‫اب‬‫بعنی‬
                                                                                            ‫بم‬
 ‫تا روزن ‪:‬کهادنی‪:.‬‬        ‫خسروانی‬              ‫مانندشیه‌بندد ‪ - ۱‬ویم اول و انی » پدر زن‬
‫نام لحنی است ازمسنفات باربد ‪ ,‬وآن نثری‌بوده‬                                   ‫وپدر شوهر باشد ‪۰ ۴‬‬
‫وطلقا‬ ‫است مسجم مشتمل بردعا وئنای خرو م‬
                                              ‫خسرو ‪ = ۴‬بضم‌اول وسکون‌نانی وفتح‬
‫نظم در آن بکار نرفته ‪,‬واین لحن داخل سی‌لحن‬
                                              ‫ثالث وواو سا کن؛ بمعنی‌ملك وامام‌عادل باشد؟ ‪.‬‬
 ‫مشهورنیست‪ .‬که |گرداخل باشد سی‌وبك میشود‬
                                               ‫ونام یادشاه کیان هم مت ‪٩‬‏ ‪ -‬وهرپادشاه‌صاحب‬
‫وشیخ‌نظامی سی وبك ورده است (‪ )۷‬وسی‌ویکم‬
 ‫همان رأنام رده و نوعی از زر رایج هم بوده‬     ‫شوکت را نیز گوبند ‪ -‬ویضم اول و ثانی وثالث‬
‫است‪ - ۸‬وهرچیزیرا که‌بس لطیف ونیکووبز رکه‬       ‫بمعنی خسراست که پدرزن وپدرشوهر باشد ‪٩‬‏ ‪-‬‬
‫باشد منوب بخرو ساخته خسروانی میگوبند‬                  ‫‪8.‬‬     ‫ومادرزن ومادرشوهر را نیز گوبند‬

                           ‫(‪ )۷‬چك ‪ ۰‬چش ‪ - :‬است ‪.‬‬            ‫(‪ )۱‬چك » چس‪ :‬باشد‪.‬‬

    ‫يدر ر‬          ‫‪_ ۴‬اوستا_‪.4۲184۷۸-‬هندی باستان ‪4‬‬         ‫‪ ۱‬ظ؛مصحففرده“(ھ‪.‬م‪).‬‬
  ‫بدرشوهر) «اسفاا ‪ ۲:‬ص ‪۸٩‬‏ و ‪ ۵۸‬؟ ورك ‪ :‬خسور ‪ ,‬خوره ‪ ,‬ورك ‪ :‬لفت فری ‪٩ - ۵۳۱‬‏ ‪.‬‬
  ‫‪ ۴‬بهلوی ‪:( ۷0۲5۱21‬يك شهرت) «منای‪ ۷2۲5-110 ۷۷۲‬اوستا ‪uh _ 012۷2۲5‬‏‬
  ‫‪ +‬اسفا ‪۱ ۲ : ۱‬ص‪ ( ) ۳۹‬بمعنی دك نامی و مشهور ) » سانسکربت ‪ « 52۷2۲115115‬بارتولی‬
 ‫*‪ .‬بازندلا ‪ « 2150‬متا ‪ ۹۳۱۰‬معرب آن کسری ؛ ‪ ۵‬مفاتیح خوارزمی‌ص ‪ ۹۷‬؟؛ نام‬                     ‫‪۸‬‬
                                     ‫جندتن از شاهان ابران ‪ -‬درپارسی بمعنی شاه گرفته شده ‪:‬‬
                                                           ‫شپنشها ملک خسروا خداوندا‬
                                                      ‫چوآفتاب توبی‌برهمه جهان تانان‪.‬‬

                                                  ‫«هعزی نیشابوری ‪:۸۳۵‬‬
                                               ‫از دساتدر‬   ‫‪ -. ۴‬به‌عنی آخیر ما‬
                                               ‫مراد‬    ‫®‬              ‫‪.‬‬   ‫>‬   ‫دانر‪۳‬؟‪۲‬‬   ‫‪ ۵‬فرهنك‬


                                                      ‫ارك خسرر ‪:‬‬                     ‫کیطسروست‪.‬‬
                                                 ‫از‪ :‬خرو ان (جمع) ‪-‬ی(نبت) ‪.‬‬                   ‫*‬
                                               ‫خسروانی گرد‬        ‫‏‪ _ A‬همه نا چو دره‌های‬
                                                 ‫کنب وار‬
                                                       ‫ارم تابد غر و‬
                                                 ‫فرخی سیستانی ‪« .‬رشددی»*‪.‬‬
                                                   ‫‪ #‬خسرواول رك ‪ :‬انوشروان ‪.‬‬
                                                ‫‪ #‬خسرو دوم حرو هرو هر ‪-‬پس‬
                                                ‫عرمز وچپارم ونوادة انوشروان» شاهنشاه ساسانی‬
       ‫خسر وروز درشکارگاه‬                             ‫‪(e.1‬‬        ‫(‏ ‪- ۰۵‬‬

#### index 207
  ‫جسوردن‬                                                                                                       ‫نله‬
 ‫خساث ‪ -‬بفتح اول وانی وسکون‌کافی»‬                                              ‫همجو خم خسروانی وامثالآن ‪.‬‬
 ‫خس وخاشاك وخاری‌باشد سه گوشه ‪-‬وخارهای‌سه‬                      ‫خسرو چهارم سریر ‪ -‬کناب‬
 ‫کوشهرانیز گوبند که انزدآهون‌دسرازسررامدشمن‬                                    ‫افزتآاب است باعتبار فلك چهارم‬
‫گذارند ودراطراف وجوالب حصار وقلعه ریزتلد‬                     ‫یه است از‬       ‫خسرو خکاونرا‪-‬‬
 ‫وبضم اول مطلق وقت رکاوبند اعم ازصبح وشام‬
                                                                ‫خورشید ‪ -‬ویادشاه مغرب را نیز گوبند ‪. ۱‬‬
‫زته‌اند ‪ -‬وبکر‬
             ‫وغیره ‪ -‬وتأخیرودرنگه رائیگزف‬
                                                               ‫حسر و داد وه رستنی وداروبی باشد‬
  ‫تکرهاکل‬
        ‫آشد‬
          ‫»ل معصفر با‬
                    ‫اول وسکون انی ک‬                            ‫کهآ نرا خولنجان کویند» وبسنی گفته‌اند درختی‬
‫کاجره‌خوانند وتخم| نرراخك‌دانه گوند رسربی‬
                                                             ‫است منسوب بانوشیروان‪ ,‬که‌چوب آن درخت را‬
                  ‫قرطم وحب‌المصفر نامند ® ‪.‬‬                    ‫خالولنجان خواندد‪ .‬وجمعی کودند نبانی‌است که‬
                      ‫خکانان" ‪-‬‬                                 ‫آنرا سفید تاك نامند و بکعرربمیةالبیضاخوانند‬
 ‫ی و تجس بجد ونفتش وجتجوی‬
            ‫بایغ باشد وبعربی استقصا خوالند ‪.‬‬
                                                               ‫و میوآن سرخ میباشد و بخوشة انگور شباهت‬
                                                               ‫‪۳‬‬   ‫داردوندان دوست رادیاغت دهنف» ودراختبارات‬

                                                                                ‫بجای حرف اول جیمآورده است‬
‫تخم کاژیره است و آنرا بعربی حب الصفر‬                         ‫خسرو زریی عطاه کنابه از‬
                                           ‫خوانند ‪.‬‬
                                                                                             ‫آفتاب عالمتاب اسب ‪.‬‬
‫اول وسکون ثانی ومیم»‬    ‫‪ .‬تک‬          ‫خم‬
                                                                ‫خسر و سيار گان = بمعنی خرو‬
                        ‫بمەنی جراحت باشد ‪.‬‬                     ‫که کنابه از آفتاب عالمتاب‬
                                                                                       ‫زرین عطا است‬
‫‪ = ۸‬بفتح‌اول بروزن پرئده »‬           ‫حسنده‬                                                                     ‫باشد ‪. ۴‬‬
                                                               ‫حسرو دشستم لهشت د اشاره به‬
‫حسودن = بروزن کشودن؛ درو کردن‬                                             ‫حضرترسول صلوات‌انه عليه وا لهاست‬
                                                               ‫خسروی ‪ ۴‬س نوعی از شراب عرفی‬
‫حسو و ب«روزن قصور‪ ,‬پدرشوهر ویدر‬
‫زرا کویند‪٩‬‏ ‪ -‬و بمعنی دروهم هست که بربدن‬                     ‫ت‌‌ بروزن علف» گردکان‌باشد که‬                 ‫حف‬

                                ‫غله وعلف باشد ‪.‬‬                                         ‫‪۱‬‬    ‫ف‬   ‫هم کو‬         ‫آترا جوز‬


‫صم اول وفتح دال امحد‪,‬‬
                    ‫ض‬   ‫ص‬     ‫حسوردن‬                                ‫‪۰‬لی است‬
                                                                          ‫حسق = بر وزن شفق ک‬
‫بمعنی خسودن است که بربدن ودرو کردن علف‬                         ‫و دعر دیعصفن‬   ‫تِِ‬           ‫آ نرا‪,‬صفاهاتی گل کاویشه‬


                                     ‫وغله باشّف ‪۰۱‬‬                                                             ‫خوانند ‪.‬‬


                                                                            ‫(‪ )۱‬چك » چش ‪:‬کافشه ‪.‬‬

   ‫‪ ۳‬ك مراد (اختمارات‪,‬دیعی) است ‪ .‬رك‪ :‬ص‌هشتاد وشش‌مقدمه‪.‬‬                            ‫‪۰‬‬   ‫خاور‬     ‫رك‪:‬‬   ‫_‬   ‫‪۱‬‬



           ‫صح نختن‌نمود روی بنظار کان‬                              ‫‪- ۴‬آمد بانگه‌خروس‌موذن میخوارگان‬
  ‫روی_بمشرق نهادخسروسا رگان‪...‬‬                  ‫که بکتف برفکندچادر (ب رگرفت‌جامة) بازارگان‬
      ‫‪ ۵‬منوچپری دامقالی ‪٩ ۵6۱‬‏ ‪.‬‬
                            ‫دانه ‪.‬‬    ‫‪ :‬خك‬    ‫رك‬    ‫_‬    ‫®‬                 ‫بیت‬
                                                                             ‫د‪+‬‬‫(رو‬
                                                                                 ‫‪ ۴‬از ‪:‬خ‬
  ‫‪ _ ۸‬لغتی‌درخز نده (ھ‪.‬م‪(.‬‬             ‫‪.‬‬   ‫_ رك ‪:‬خك‬            ‫‪۷‬‬        ‫‪ - ۱‬مصحف «خدکامار» («‪.‬م‪.).‬‬
```


## [2026-09-06T20:59:29.723Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nimport re\nfor i in range(200,240):\n    p=t[i]\n    if 'خشو' in p and ('مادر' in p):\n        print('#### idx',i,'printed~',i+543)\n        print(p[:3000]); print('-----')\nEOF"
}
```


### [2026-09-06T20:59:31.296Z] TOOL RESULT

```
#### idx 208 printed~ 751
 ‫‪Yg‬‬     ‫~‪m‬‬                                                                                      ‫‪‎‬هرو‬


‫بمعنی‬   ‫‪ -‬بر وزن رسیدن »‬         ‫خسدن‬                      ‫خسوره ه بم اول وفتح رای قرشت؛‬
‫استت که در زیر «ندان ترم کردن‬           ‫خایدن‬              ‫یمضی خور استت که پدر شوحو و پدر زن‬
                                                                                                    ‫يلد‪٩ ‎‬‬




                                                    ‫بیان دهم‬
             ‫در خای نقطه دار باشن نقطه دار مشتمل بر هفتاد و هفت‬

                                               ‫لغت و کنات‬

‫خشاوه » بکر اول بر وزن کلاوه ‪.‬‬                            ‫هس سم اول و سکون ثالی هً‬            ‫‪ ۱‬حش‬
‫ياكکردن باغ و زمینو کشت‌زار وزراعت‌باشد از‬                 ‫بمعتی ملدرزن ومادر شوهر باشد ‪ ۴‬؛ وبفتح اول‬
‫ویمعنی‌بیراستن‬   ‫>‬   ‫وخاشاك وعلفهای خودرو‬           ‫خی‬      ‫هم باینمه‌نی وهم بمعنی تند وتیز دوبدن آمده‬
 ‫هم هت که بریدن شاخهای زبادنی درخت‬                        ‫ات ‪ -‬و بيخ بغل را نیزکوبند و بعربی ابط‬
‫بسای وأو رای یی نقطه همآمده‬      ‫باشد؛ ویاشمعنی‬
                                                                                                   ‫خوانند ‪.‬‬   ‫‪je‬‬

                                           ‫‪.‬‬        ‫است‬     ‫خثاهی ‪ -‬بقتح اول و میم بر وزن‬
                                                            ‫زن‬      ‫مادر‬     ‫‪EER‬‏‬              ‫‪۰‬‬     ‫فلاخن‬
‫ضم اول بروزن‌همای بمعنی (‪)۱‬‬       ‫ه‬   ‫خثای‬
               ‫باشد ‪:‬‬   ‫نله‬   ‫کننده و ‪1‬‬        ‫خوش‬
                                                            ‫ومادر شوحراست » وبایئمعنی بضم اول هم آعده‬
                                                                                               ‫لت ‪. ۴‬‬
                                                            ‫خثا نیدن؟ ت بروزن رسانیدن‪ ,‬بدندان‬
‫‪۰‬آجر‬    ‫رشت‬    ‫هس بکراول‌بروزن‬        ‫حت‬



‫خام وپخته راگوبند ‪١‬‏ ‪-‬ونوعی از سلاح جنگه‬                                             ‫رش کردن باشد ‪.‬‬


      ‫نیز‪ 311501‬بپمن معالی کےنواد) رك خ‪:‬سر‪ ,‬خسوره‬                           ‫( ‪5‬‬      ‫اك‬
                                                                                      ‫اردر‬
                                                                                         ‫‏‪٩‬‬
         ‫‪9‬‬   ‫رك‪ :‬خشتامن» خش‬                     ‫‪.‬‬    ‫‪..‬خشتامن‬    ‫‪ ۳‬مقاءل«خر»(د‪.‬م ‪).‬ره خشامن‬


             ‫‪O‬‬                         ‫‪ - ۴‬اسدی کوبد ( لفت فری ‪TR‬‏‬
                                                                                   ‫) کوید ‪:‬‬   ‫(سمرقندى‬

                                   ‫بی شك ( بثك ‪ .‬دهخدا) لهنگ‌دارد دل را همی خشاید‬
              ‫ترسم که ناکوارد کایدون ته خرد خاید ‪» .‬‬
  ‫بیداست که خشانید» فعل ماضی استاز « ختایدن» ؛ دربن صورت مضارع آن «خشاند»‬
  ‫اشد ( ماتتد رساند از رسالیدن ) ته خشاید که باید ازمسدر خشودن (همجون کشاید از کشودن )‬
   ‫‪.‬هراً مصدرفمل بموزر‬
                     ‫یاخشابیدن(ه
-----
#### idx 213 printed~ 756
                                                                                                                ‫‪۷۲‬‬


 ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬
‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
 ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬
 ‫لون بای حطی هکمفته اند کهبر وزن بدیدار‬                                                             ‫درشت را گوشد ‪۳‬‬
                                                   ‫باشد ‪.‬‬         ‫خشنان ‪ -‬ب باضمول بر وزن برهان ‪۰‬‬
‫‪ -‬بر وزن بلنگ ‪ ,‬زاغ سر‬                    ‫حشنگ‬                                       ‫فرخنده وخجسته ومبارك راگوبند ‪.‬‬
‫وسر کجل و کجلی را کوبند ‪ -‬و مردم کچل را‬                           ‫ک=نابه ازمنافق‌بودن‬            ‫دن‬
                                                                                                  ‫شیلو‬
                                                                                                     ‫ش‬ ‫خ‬
                                           ‫تگبفزته‌اند‪.‬‬                                             ‫وطاق کردن باشد ‪.‬‬
         ‫‪۱‬‬       ‫‪۲‬‬     ‫معیم ‪. _ ۵‬‬
 ‫حشنو = بامول والك بروزن‌پر کو‪.‬‬                                   ‫خشی خاله = بروزن‌طر بخانه‪ .‬خانه‌ای‬
 ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
                                                                  ‫‪۰‬ویند که ازتی بوربا سازند ‪ -‬و خانه‌ای رانيز‬
                                                                                                            ‫گ‬
                    ‫ویفتح اول هم درست است ‪۴#.‬‬                      ‫گته‌اند که بر در ورنجرءآن خار شتری ندند‬
  ‫حشنی ‪ -‬بضم اول و کر الك بورزن‬                                    ‫و آب بر آن پاشند تاهوا و نیم سرد درون‬
                    ‫‪.‬‬        ‫ند‬
                              ‫وهبرا‬
                                  ‫گحش‬
                                    ‫معطی » زن فا‬                                                                         ‫ی‬
‫واو ‪۰‬‬    ‫بصم اول ونانی وسکون‬          ‫=‬   ‫حشو‬                     ‫= بقتح اول باسن بینقطه‬            ‫ر‪۶‬‬
 ‫مادر زن ومادر شوهر باشد ‪٩‬‏ ‪ -‬ویقتح اول در‬                        ‫بمعتی خشتنشار است که مرعابی‬            ‫بروزن طلبکار »‬



  ‫‪«- ۴‬خدن‌بروزن كتف سعتی‬               ‫ورك‪ :‬خشن‪,‬خشنار‪.‬‬                  ‫حشن سید نود“ «لفت‌قرس ‪۶‬‬          ‫‪ ۱‬کے‬

  ‫را شتافتن بخاتهاء‬      ‫بینم که مردمان مر گرمای‌سخت‬                  ‫‪#‬اهم‬       ‫‪۴‬‬    ‫ت‪۱‬شرح‌قاموی*‪.‬‬
                                                                                                  ‫ت»‬‫سس‬
                                                                                                     ‫شت ازهر چىز ا‬

  ‫زیر کد‪ 
-----
```


## [2026-09-06T20:59:43.090Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (588,589):\n    print('#### idx',i,'printed~',i+543); print(t[i][:3500]); print('====')\nEOF"
}
```


### [2026-09-06T20:59:45.172Z] TOOL RESULT

```
#### idx 588 printed~ 1131
 ‫‪۷۱۷ ۷۹‬‬

‫و سرزش کردن و طعنه زدن را یز گوبند ‪-‬‬                     ‫و اندام اطفال برآ دد ‪-‌ ۱‬‬                 ‫باشد که از سر وروی‬

               ‫وملامت کننده را هم مدگوبند ‪.‬‬                ‫و بکر اول وسکون ثافی وکاف ‪.‬سرخاب‌وسفید‬
  ‫ی‬
  ‫او‬‫رسی‬
      ‫بسرگره کر کاف فار‬                                   ‫و معتی‬       ‫مالند ‪-‬‬        ‫برروی‬      ‫آبی را گونن که زان‬

‫فرشت و ظهورها » عقده و گرهی را گونند که‌بر‬                                             ‫امتح‬      ‫و سقید هم اقا‬           ‫صرح‬




 ‫سزریت * د بتجنغاسی وکر‬
‫زای نقطه دار و سکون تحتانی و فوقالی» زریرا‬                                                           ‫‪.‬‬    ‫بلند‬
                                                                                                             ‫وخ‬‫گبی‬
                                                                                                                 ‫عر‬
‫کوبند که سر شمار کفار نموده از ایشان بطریق‬
                                                          ‫سر کت" ۔ بفتح الث بروزن هرشب ‪۰‬‬
‫جزبه بگیرند‪,‬چه گزیت بمعنی جزبه باشد‪.‬ا کر‬
 ‫کرت کے ات ازع وتا باتوی‬                                  ‫دام مطربی و سازنده‌ای‌بوده که درعهد خود لظیر‬
                                                                                                                      ‫نداشته ‪.‬‬
‫آنکه جزبه معرب آن است» لهایتش درفرهنگه‬
‫تحتالی نوشته‌شده‬     ‫وکون‬
                        ‫جپانگیری بفتح‌کاف س‬              ‫و سکون حای‬                       ‫سر کحلی ‪=-‬‬
                                                                                        ‫ابض‬
                                                                                      ‫لمك‬
             ‫مستند گردیده که‪:‬‬       ‫بود و ياين بت‬          ‫بی نقطه بروزن سرقفلی » هرچیز سیاه راگوبند‬
                                                                                 ‫وا تبرسباه را ا‬                         ‫وا‬
‫خراح قیصر روم است وسر کزیت جنم(‪)۱‬‬
     ‫بپای بند کی رام رای باجیپال‪٦.)۲(.‬‏‬                    ‫سر گر = بفتحاول‌بروزن‌زر کر“ کفشکر‬
‫سر گز ی * = بروزن برمزید » بمعنی‬                         ‫اول هم باین‬             ‫و کفش دوز را گونشد ؛‪ :‬وم‬
‫و زری باشد که از‬       ‫سر کزبت است که جزبه‬                 ‫معنی ‪ -‬و هم بمعتی بوزه فروش و بوزه‌سازباشد»‬
                                     ‫کفار گر دد ‪.‬‬         ‫چه سرشرایبرا کوبند که ازارد برنج سازند‪. ۴‬‬

 ‫زسارین نم اف فرسان با‬
  ‫لخی‬
    ‫یو‬‫اند‬
        ‫ووسف‬
           ‫اکول ک‬
                ‫کحر‬
                  ‫ککهان حاکم از‬
                                                          ‫سر گر ان = یک رکاف فارسی » کنابه‬
                                                               ‫مر وود‬             ‫وی‬           ‫و‬              ‫از کن انست‬
‫کوسفندويكکاوويكاس‌انتخاب و گزین‬            ‫اسب بك‬          ‫باشد ‪ -‬و متکیر را ایز گوبند ‪ -‬ودردسروملالت‬
                                    ‫کرده بگرند‪.‬‬                                                           ‫را همکنته‌اند ‪.‬‬

‫وکون سین بی‬
          ‫سر کی ه_بفتح‌کاف س‬                              ‫سر گردا ‪ -‬باکاف فارسی بر وزن یی‬
        ‫قطه (‪ , )۳‬نام مرغی است خوش آواز‪.‬‬                   ‫فرداء بمعنی سر گیجه باشد؛و آن‌علتی استآدمی‬
                                                                                               ‫را ومربی دوار خوانند ‪.‬‬
‫سر کش ‪ -‬بکااف بروزن هفرش ‪ ۰‬نام‬
 ‫خنیا گر ومطربی‌بوده بی‌عدبل ولظیر ‪ ۷‬کونابه‬                ‫‪-‬‬       ‫شد‬
                          
====
#### idx 589 printed~ 1132
  ‫سکه فروختن‬
           ‫ر‬                                            ‫‪۱‬‬                       ‫م‪۱ ۲‬ات‬
‫فایق باشد ‪ -‬و بمعنی ضابط‬       ‫گرری‬
                                  ‫کدندیوب‬       ‫سکش وسرشخ‬
                                                        ‫از مردم دبرآشنا باشد‪ -‬و اسب ر‬
                                ‫هم‌آمده است‬     ‫را کیوزیند ‪ -‬و مردم صاحب قوت وقدرت و نا‬
‫سر کو به ‪ = ۲‬بروزن منصوبه ‪ ۰‬کرز‬                                ‫فرمان ومفرور را یز گفته‌اند‪.‬‬
                               ‫گرانرا گونند ‪.‬‬
                                                 ‫سر گل = بفتحکاف فارسی‌بروزن صندل؛‬
 ‫سر کوتا ‪ = ۴‬بکسر اول وکضامف‌فارسی‬              ‫کویی باشد که طفلان از رسمان سازند وبدان‬
        ‫و فوقالی بالف کشیده » بلفت زند ب‬
‫وازند (‪)۱‬‬                                                                          ‫بازی کنند‪.‬‬

‫بمعنی راز باشد که سخن مخفی است ؛ و بفتح‬         ‫«کنابه از برگزبدن‬    ‫سر گله نهادن‬
‫اول هم بر آهفة است ‪ -‬وبمعنی‌داری کمدزدان‬                                 ‫واعتبار کردن باشف ‪.‬‬

                         ‫‪.‬‬    ‫یلزقاد‬
                                   ‫وزح‬
                                     ‫رآاا‬       ‫سر کنگییین ‪ ۱‬د بمعنی‌سکنجین‌است‪,‬‬
‫سچرلکكو ‏ بنتم جیم فارسی »‬                      ‫کربی باشد از سرکه وعسل‪,‬چه‌انگبین‬
                                                                               ‫ون م‬
                                                                                  ‫آ‬
 ‫کنابه از مردم فرومایه و بنقدر وقدمت رامین‬                                  ‫بمعنی مل است‬
                                     ‫باشد ‪# .‬‬
                                                ‫سر کوب = بروزن مرکوب‪ .‬بلندبی‬
‫بکس ها؛ کنابه‬   ‫ساله ‪.‬‬       ‫سر که ده‬
                                                 ‫را گوبند که بر قلعها و خالها مثرف باشد ‪-‬‬
                       ‫رنه باهد ‪.‬‬
                                ‫ادزکبین‬           ‫و بمء‌ئی طمنه و سرزش‌هم گفته‌اند ‪ -‬و حریف‬
 ‫سر که فر و ختن » کنابه از رش‬                   ‫آمده‬   ‫وصومت‬
                                                           ‫قوی و پرزور بود که بجنگه خ‬
      ‫روبی کردن و روی درهم کشیدن باشد ‪. ۴‬‬       ‫خصی را یز گوبند که در هرفن‌زبادنی‬
                                                                                ‫وشدش‪-‬‬
                                                                                    ‫با‬
                                                             ‫(‪ )۱‬چك ‪ :‬ژد ویاژند ‪.‬‬

  ‫‪۴‬از‪:‬سر ‪٣‬‏ کوب‬
              ‫ستکنجبین ‪- .‬‬                 ‫ک)ن=گین‬
                                                 ‫س‪.‬م‪.‬‬
                                                    ‫(ه‬          ‫ین‬
                                                                 ‫ب‪+‬‬‫گکه‬
                                                                     ‫اازنسر‬
  ‫‪» (8)8‬پپلوی ‪.28۳‬راز«بودکر ا‪.) ‎9‬‬      ‫‪ _ ۴‬هز‪4K . ‎‬‬          ‫(انة اسمآلت)‪.‬‬         ‫‪e‬‬
                                                  ‫‪E‬‬                            ‫‪۴‬‬
   ‫لظامی گنجوی‪ «.‬کنجینه ‪.۷۸‬‬     ‫ازچه گشتی چو شام‌سر که‌فروش ؟‬      ‫صبح وارم چودادی اوللوش‬

   ‫‪ #‬سرکه‪ -‬بکر اول و سوم ( درلېجة مرکزی) = سرکا (ه‪.‬م‪* )۰‬کیلکی‪261728‬؛‬
                                                   ‫می ترش شده بوسیلةٌ تخمیر » خل ‪.‬‬
                                                                     ‫بقه ازصفحهٌ ‪۹۲۱۱‬‬
  ‫نیت بلکه محتملا ازبعضی کتب معمول دارواخر دور ساسانی نقل شده‌اس
====
```


## [2026-09-06T20:59:54.028Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in range(585,605):\n    p=t[i]\n    hits=[w for w in ['سروش','سرود','سروا','سرواد'] if w in p]\n    if hits: print(i, 'printed~',i+543, hits)\nEOF"
}
```


### [2026-09-06T20:59:55.728Z] TOOL RESULT

```
585 printed~ 1128 ['سروش']
592 printed~ 1135 ['سروا']
593 printed~ 1136 ['سرود', 'سروا', 'سرواد']
594 printed~ 1137 ['سرود', 'سروا', 'سرواد']
595 printed~ 1138 ['سروش']
596 printed~ 1139 ['سروش']
597 printed~ 1140 ['سرود']
```


## [2026-09-06T20:59:58.398Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i in (593,594,595):\n    print('#### idx',i,'printed~',i+543); print(t[i][:3800]); print('====')\nEOF"
}
```


### [2026-09-06T21:00:00.296Z] TOOL RESULT

```
#### idx 593 printed~ 1136
  ‫سروچ‬                                                                                                     ‫¬‬
‫ګوبند که راست رود وآن را ياين اعبار آزاد‬              ‫میباشد ‪ :‬مکی‌سروآزاد و دیگری سروسهی‌وسیم‬
 ‫کفته‌ادد که از ید کی و داراستی ویبوستن‌بشاخ‬                                  ‫سرو ناز وهر يك درجای خود‬
‫یوبند هردرختیکه‬
              ‫وک‬‫دیگر فارغ است » ی‬                                            ‫خواهد آمد » وعربان سرو را‬
 ‫میوه ندهدآنرا آزاد خوانند چوون سرو موه‬
‫آزاد باشد» وجممی کفته‌اند عر‬       ‫ندهد ياين سیب‬
                                                                                ‫شجرة الحبه خوانند چه گوننه‬
                                                                             ‫هرجا که سروهست البته مارهم‬
‫درختی رکامالی و زوالی هت چنانکه کاهی‬
                                                                              ‫هست‪ .‬اکر بر کهآ نرابکوبند‬
 ‫که‬
  ‫ر‌ب‬
    ‫وی پژمرده و بی‬
                 ‫پر برکه و تازه اکستاه‬
                                                                             ‫و با سر که بیامیزند موی را‬
‫هيچيك از اینها نیت و همه وقت‬               ‫ورورا‬
                                               ‫س‬
‫سبز و تازه است و اژین علتها فارغ و این صقت‬                  ‫سرو‬                 ‫صاه کند‪ -‬ونام مکی‌ازیادشاهان‬


      ‫آزاد کان است پس بدین جهتآزاد باشد‪.‬‬              ‫یمن است که دختر بیکی از فرزندان فرسون‬
 ‫سر اول‪ - 4‬اول بروزن بزاله‪.‬طفی‬                                                                                  ‫داده بود ‪.‬‬

‫ین که‬
    ‫مو‬‫هشد‬
        ‫بودکه برسرآن خارهای نیز با‬                     ‫سر وا ‪ = ۱‬بروژن پروا» یمعتی حدیت‬
     ‫بحامه فرو رفت جدا کردن‌آن دشوار است‪.‬‬            ‫وعر حم‬
                                                          ‫و سخن باشد ‪ -‬و بمعنی آفانهٌ دروغ ش‬
‫سر وب ‪ - ۸‬بفتح‌اول وضم تالی‌وسکون‬                                                                          ‫گفته اند ‪. ۳‬‬
 ‫ثالث مجهول و بای ابجد ‪ .‬بلفت زسوی‌ازند(‪)۱‬‬            ‫»ام‌منظوم‬
                                                              ‫سرو اك ‪ - ۲‬بروزن فرهاد کل‬
            ‫بمعتی سخن باشد وبعربی کلامگویند‪.‬‬          ‫افون‬     ‫ویمعتی افانه و‬                   ‫شمر را کویند ‪- ۴‬‬        ‫و‬

‫ختح اول وفوقانی وثالت‬     ‫سر و تلك* "‬                                                            ‫وسرود همگفته‌اند ‪۰‬‬

‫مجهول بروزن عروسكك ‪..‬بمعنی شورش وآشوب‬                 ‫سرو اده * = بفتح اول بروزن‌شهزاده‪:‬‬
 ‫وغوغا باشد ؛ و باين معثی بفتح اولوئانیوفوقالی‬
             ‫حم کنته‌اند که بروژّن فرزدق باشد‪.‬‬       ‫قافیة شمر راکوبند ‪ ۱‬همچو بهار ونگار و هزار‬
                                                      ‫وزمین و کمن وامین»وحرف دال درین لفت‌ولفت‬
‫بفتح اول وضم تانی‌وسکون‬            ‫سر وج‬                             ‫ماقبل بثایر قاعده کلی نقطه‌دار است‪.‬‬
‫ثالث مجپول و جیم فارسی ‪ ۰‬دامدشتی است در‬
                                   ‫نواحی کرمان ‪.‬‬      ‫‪ ۲۰‬بکر واو ؛ سرویرا‬                          ‫د‬
                                                                                                   ‫زوا|‬
                                                                                                      ‫سر‬
                                                                         ‫(‪ )۱‬چك ‪ :‬ژند ویاژند ‪۰‬‬
                                       ‫‪:‬‬   ‫رك ‪ ۱‬سرواد ‪ 4‬سرواده‪ .‬ورك ‪ :‬ح ‪۸‬همین‌صفحه‬                     ‫‪_ ۱‬‬

            ‫چند فروشی بمن نو اين سرو سروا‪.‬‬              ‫‪ - ۴‬چند دهی وعد دروغ همی چند ؟‬
  ‫اورمزدی‪« .‬لفت فری ‪۷٩‬‏ ‪.‬‬
                                                        ‫‪.‬‬   ‫» سرود‬       ‫سروا‬   ‫‪ :‬سرواده»‬         ‫رك‬        ‫‪۴‬‬


         ‫بازار وفست سرواد‪.‬‬   ‫که رفت رة‬

   ‫لیی ‪ .‬ل٭فت فرس ‪۸°۱۹‬۔‬
                               
====
#### idx 594 printed~ 1137
   ‫‪۰‬؟(‪-۳۱۱‬‬                               ‫‪o‬‏‬    ‫‪«.‬‬                                    ‫فاون‬
                                                    ‫وسر خای‬
                                                          ‫سرو خشت ب=فتح اول ک‬
 ‫درخت سرو بسار بود ‪ -‬و نلم لحن دهم است‬
‫ازسی لحن باربد ‪ - ۴‬و نامقصبه ایست درملك‬             ‫شخصی را مخنی گوبندیا ازروی مهربالی اسیحتی‬
                                   ‫فاری ‪© .‬‬
                                                                             ‫لمابند » ار شنود ‪.‬‬
‫سروستاه = بر وزن کرم نکاه » نام‬                     ‫سروت = بنم اول بروزن دروده بمعنی‬
                    ‫ستیازقی ‪٩‬‏ ‪.‬‬
                               ‫واس‬
                                 ‫مایی‬
                                    ‫نو‬                ‫تفن کات بی درک و کوک‬
 ‫سرو سهی دبکر واو » سروی باشد‬                       ‫‪ - ۱‬و بمعنی رقص‬   ‫مرغان و آدمیان هم هست‬
     ‫ی‬
     ‫هچه‬ ‫ساشد‬
            ‫های آن راست میب‬‫خو‬
                            ‫ااخ‬
                              ‫دشو ش‬                 ‫وسماع نیز گفته‌اند ‪ -‬و بفتح اول بروزن سرمد‬
 ‫بممنی راست آمده است ‪ - ۷‬و نام لحن بازدهم‬           ‫بمعنی اول سرواد اکسهت‌نظم وشر وشمرواف‌انه‬
                   ‫است ازسی لبحانربد ‪. ۸‬‬                                       ‫وقصه باشد ؟ ‪۰# .‬‬

 ‫وسسریاه ‪ -‬بکر الك وتحتالی‌بالف‬                      ‫سر و دو کردن۔ یمعئی سرورودرهم‬
 ‫نلگاوورباند و آلرا بعربی‬        ‫رخ»ت‬
                                    ‫دیده‬
                                       ‫کش‬            ‫کشیدن است ‪ -‬کونابه ازخشمگین شدن‌وخطاب‬
                        ‫صنوبرالصفار خوانند ‪.‬‬                                   ‫وعتاب کردن باشد‪.‬‬
 ‫سر وش * = بضم اول بروزن‌خروش »‬                      ‫سروستان ‪ » ۴‬با ای قرشت بروزن‬
                                                                ‫وکسر" خا ‪۰‬‬   ‫(‪ )۱‬چك ‪:‬‬


    ‫‪ - ۱‬پهلوی ‪< 60۳3‬اووالا‪( 6۵0۲5 ,»۳۰۳‬رك ‪ :‬سرودن)«اسشق‪ . ۵۳۲۷‬بلوچی‪40785‬‬
    ‫(موسیقی)‪ ,‬اففانی ‪ (0۵۲85‬صنیف ‪ ,‬آهنگه) »اوستا ‪( 8/08۳5 -‬استماع) (رك ‪ :‬حوبشمانه‪:)۳۷‬‬
             ‫فکنده سوزآ شس در دل ستگه‪,‬‬                     ‫سرود پهلوی درنالة چنگ‬
     ‫لظامی گنجوی ‪ « .‬کنجینه‪»۷۸‬‬
             ‫‪ _ ۴‬از ‪ :‬سرو‪-۳‬ستان (یسوند مکان) ‪۰‬‬             ‫‪ - ۴‬رك ‪ :‬سروب » سرواد ‪-‬‬
    ‫گاه سرومتان زد امروز وکاهی اشکنه ‪.‬‬                ‫مطریان ساعت بساعت برنوای زیر ویم‬      ‫‪۴‬‬
   ‫« منوچهری دامفالی ‪۹۷٩‬‏ ‪.‬‬
   ‫*ه‪-‬لوی ‪١٥4٤1۷۲45‬‏ و بدانجا آثار فصری اعزهد ساسالی است ‪.‬ک<ربستنین ‪.‬‬
                                                                    ‫پ‬
                                  ‫‪۱‬‬                                            ‫ملسان ‪٩ ۹۷۲‬‏ ‪.‬‬
       ‫ساعتی سروستاه وساعتی باروزنه ‪.‬‬                 ‫‪ - ۱‬ساعتی سیوارتیر وساعتي كبك دری‬
   ‫« منوچهری دامفالی ‪۹۷٩‬‏ ‪.‬‬
                                                                      ‫رك‪ :‬سهی ‪.‬‬      ‫‪۷‬‬

        ‫نوبتی روشن چراغ ولوبتی کاویزنه ‪.‬‬              ‫‪ - ۸‬وی پالیزبان ونوبتی سروسهی‬
   ‫«منوچهری دامفالی ‪٩۷٩‬‏ ‪.‬‬
    ‫‏‪ - ٩‬اوستا‪ahsoars -‬‏ › پهلوی ‪« 558۲5‬اسشق ‪ . ۹۳۷2‬سرئوشه دراوستا بمعنی‌اطاعت‬
    ‫و مفارلبرداری ومخصوصا پیروی‌از اوامر خداوندی است » وآن از وبشة اوستایی ‪)۷2۲8-(۷۲5-‬‬
    ‫قه درصفحة ‪۳۳۱۱‬‬
    ‫‪ #‬سرودن ‪ -‬نم اول ودوم وفتح چهارم ‪ ۰‬از ‪ :‬سرو ‪٣‬‏ دن ( بسوند مصدری)‪ :‬پهلوی‬
    ‫تهال‪( ۳۹ 0‬آوازخواسن) «یبر گه‪ »۹۰۲‬اوستا رمشة‪( ۷375-‬شنیدن)‪ ,‬حندی باستان رشه‪۷2۳9-‬‬
                              ‫«استق ‪۵۳۷‬؛ آواز خوادن ؛ تفنی کردن » سراییدن (ه‪.‬م‪. ).‬‬

====
#### idx 595 printed~ 1138
                                                                                           ‫—‬     ‫لس‬
   ‫"روش‬


 ‫کال سال شممی بنام ابدان موسوم‌شده ‪» ۴‬وهر‬
 ‫یك آزین دوازده سروش بتدییر امور و مصالح‬                ‫پیغامآور بعاشمدوما ‪ -‬و مطلق فرشته رلایز‬
‫ماهی که هم نام اوست ممین‌است وهمچنین ندییر‬             ‫فری‬   ‫کفنته‌اند و بعربی ملك خوانند ‪ .‬وحکمای‬

  ‫کیانه‬ ‫امور و مصالحیکهدرهربك از روز های س‬             ‫کوبن دکه حق تعالی سی و پنج سروش آفربده‬
 ‫واقع میشود حواله بسروشی است که آن روزینام‬            ‫است ازآ جمله سی فرآنانند که روزهای سی‬
 ‫او موسوم است‪ .‬واین سروشها که بتدبیر روزها‬             ‫کانٌ هرماه از ماهپای شمسی ینام ابثان موسوم‬
 ‫قیام دارندکار کنانسروش‌هایی‌اند که بتدبیرماهها‬       ‫کشته ‪ ۱‬و پنج فردیگر آنکه پنجۀ دزدید هکه‬

 ‫اقدام مینمامند‪.‬پس هرروزی که بآننا‌ممامسوسوم‬
 ‫باشد سروشی که آن ماه ینام اوست و تدییر‬                ‫تفر ند که ماههای دوازده‬     ‫آن سی سروش‪:‬دوازده‬


  ‫‪ - ۴‬نج دزدیده را بنام پنج‬                   ‫‪ ۱‬در آین زرتشتی آبان را «ابزدان» نامند ‪.‬‬
   ‫کات (اوستا) امیدماند»اشحنن ‪ :‬اهنود ‪ ,‬اشتود‪ .‬سینتمد » وهوخشتر ؛ و هیشتواشت‪ .‬رك‪:‬خرده‬
                                         ‫‪ ۰ ۱۱۲‬ورك ‪ :‬بهترك (بپىزك) درهمین کتاب‬      ‫اوستا ‪ .‬بورداود ص‬

   ‫شش عدد ‪ ۲‬بان امشاسیندان (مهن فرختگان ) اند ‪ :‬ار دسپشت ‪ ,‬خرداد » امرداد ‪۰‬‬                ‫‪۳‬‬

   ‫وررأی ابنان لخت سپنتا مینو (خرد مقدس ) قرار داشته که‬
                                                      ‫شهربور » بهمن » اسپندارمة » د‬
  ‫جمعاهفت امشاسیند باشند»بمدها بجای او اهورمزدا گرذااشتند وگاه‌نیز «سروش»‪ 20508]5‬را‬
                                     ‫‪.‬‬   ‫برسر امشاسیندان قرار داده‌الد ‪ .‬رك ‪ :‬مزدینا ص ‪۷۵۱-۸۵۱‬‬

                                                                                   ‫بقه اصزفحهٌ ‪۲۳۱۱‬‬
   ‫بمعنی شنیدن آمده ‪ .‬درکانها بیشتر سرئوشه بهمن معنی باو شده ( سنا ق‪4‬ط‪4‬مهٌ ‪٩۱۰‬‏سنا‬
    ‫ترا‬‫سد‬ ‫ونین‬
             ‫اهمچ‬
                ‫‪ 0‬قطعةٌ ه وجزآن) ونيز دردیگر بخشهای اوستا بدین معنی بارهاآمده ‪ .‬و‬
   ‫سرئوشه بعنوان علم برای فرشته‌ای بادشده واومقامی مهم دارد و صفت (مهین) و (بزرکه) متصف‬
   ‫کردیده‌است (کانها‪.‬یسنا ‪ ۳۳‬قطمةٌ ‪ . )۵‬وی مظهر اطاعت نومايندة صفت رضا و تسلیم دربرابی‬
    ‫اوامراهورائی است ‪ .‬سروش ازجهت مقام بماهر برابراست و گاه اورا درجزو امشاسیندان‌مصوب‬
    ‫از فرشتگالی است که در روز رستاخیز بکار حاب‬               ‫دارند ‪ .‬در ادیبات متأخر زرتشتی » سروش‬
   ‫ومیزان کماشنه خواهدشد وزکاانها نیز برمیآید که این فرشته در اعمال روز جزا دخالت دارد‬
      ‫دی‬
       ‫زيك‬
         ‫یش پ‬
            ‫ارو‬
              ‫‪.‬هم در کنب متأخر زرتشتی و فرهنگهای فارسی »س‬
                                                        ‫(یسنا ‪ ۳‬قطمهٌ ‪ )۲۱‬و‬
   ‫وحافل وحی خوانده شده » ازابنرو کدتراب های فارسی اورا باجبرائیل سامی یکی دانتهاند ‪.‬‬
   ‫محافظت روز حفدهم هرماه بسروش ایزد سپرده‌شده ‪ .‬بیرولی درفهرست‌روزهای ابرانی(]تارالباقیه)‬
   ‫روز مزبور را «سروش» و درسفدی «سرش» و درخوارزمی «اسروف» بادکرده ‪ .‬در زبان فارسی کاه‬
                                                                ‫«سروش» بفرشتة مذ کور اطلاق شده ‪:‬‬
                    ‫سروش و ماه ومپر وچرخ واختر ‪.‬‬              ‫کوانان بس بود دادار داور‬
                                          ‫فرشته استعمال شده ‪:‬‬   ‫وگاه ‪.‬بمعنی مطلو‬    ‫ورامن ‪44c‬‏‬   ‫د وس‬


                     ‫نیایشهای بی اندازه بنمود‪.‬‬                  ‫سروشان را بنام‌ليك بستود‬
                                ‫«وس ورامین ‪ . 44‬مسمود سعد از روز سروش چنین بکاد‬
                            ‫رده ‪:‬‬
               ‫‪.‬‬   ‫باده خور و شمه مطرب لیوش‬               ‫روق‬     ‫امت که کون‬        ‫رور روش‬
           ‫‪.‬‬       ‫› مزدینا ‪04*-۸484‬‬      ‫‪4-۵4‬‬
                                             ‫رك‪ :‬روزشماری ‪۲‬‬        ‫‪ ۶‬معود سعد لاهوری ‪۳‬‬

====
```


## [2026-09-06T21:00:41.859Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(80,110):\n    p=t[i]\n    hits=[w for w in ['شنیدن','شنودن','شنو '] if w in p]\n    if hits: print(i,'printed~',i+1209,hits)\nEOF"
}
```


### [2026-09-06T21:00:43.800Z] TOOL RESULT

```
721
91 printed~ 1300 ['شنیدن']
94 printed~ 1303 ['شنیدن', 'شنودن', 'شنو ']
```


## [2026-09-06T21:00:46.234Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(t[94][:4000])\nEOF"
}
```


### [2026-09-06T21:00:48.105Z] TOOL RESULT

```
[pdf page 95]
هنوشه

شنوشه ۱ © بفتح اول وئالی‌بوا رکشیده
و شین شطه‌دار حفتوح « ‎lyn‏ باشد که از راه
دماغ بجلدی ونئدی ‎op plat‏ اختیار برآبدرآترا
پعربی عطسه کوبند ۰ و بکسر اول حم کفته‌اند
وبا سین ب‌قطه (۱) ‎gt‏ درست است چه‌درفارسی
سین وشن بپم تبدیل مییابند .
شنو لقن ۲ ه با تای ‎ets‏ بروزن
سیوشکن ۰ بلفت زندوپازند (۳) بمعنی ‏ لوشتن
باشد و شئولمی ‎st‏ لوسم و شنولید عنی
بنوسید .*
‎Mea‏ = بنتح اول وئالی‌بی نشدید مجمیع
آواز ها را گوبند ءموماً همچو صریر قلم ۴ -
و آوازنفیر و بای وسورنای - وآواز سبع‌وبهايم
و وحوش و طیور و مانند آن ۴ - و ‎het‏ اسب
را نیز کفته‌ادد خسوصآوآنرا بعربی صهیل‌خوانند
- و بمعنی چارشاخ دهقادان هم آمده است»,وآن
آلتی باشد ‎dents ule‏ دست و دسته‌ای‌بیز دارد
که ‎OL‏ غلهة کوفته‌شده را ‎oly‏ دهند نا ازکاه‌جدا
۰ (۱) چك :- بی نقطه .
‎de (t)‏ :

عشحه +

۱ سح سوسه ‎(pn)‏ < اشتوسه (هم) .
مولف خلط کرده است !

. ۵۰۷ ‏باروچا‎ : Ay. col
Jie ‏کلك اوبخندد‎ tas, ‏زگربه‎ - ۴

. ‏چك: با تا‎ (x)

ماس

شود - و پمعتی فرین وللشت هم حست ‎6٩‏ - وبا
تشدید تالی ‎Ret‏ اسب را گوبند.

شنی = بنتح اول بروزن دلی * گیاهی
باشد که از پوست ‎OT‏ رسمان سازند - وبمعنی
سینی هم کفته ‎al‏ وآن خوالی باشد که از طلا
وقره و مس و امثال ‎OT‏ سازند.

شنیدن 1 ه بفتح اول بروژن رسیدن »
معروف است و بعربی سماع گویند - و بمعنی
بوبیدن و بوی کردن لیز گفته الد ۷ - و بععنی
هجوم لمودن - و جمعیت کردن هم آمده‌است.

شنیز = بنتح اول بر وزن ‎gel‏ » چوب
آپنوی را کویند - و کمان ‎pb‏ اندازیرا ببز
کفته اند - و بضم اول مشفف شولیز است که
سیاه دانه باشد ۸ .

شنیژه = بنتح اول و زای فارسی‌بروزن
‎ame‏ (4) » رسمانی باشد که از پهنای کار
جولاهگان زباد آید و ‎LT‏ نبافند و بانگشت
پیچیده در کناری گذارند .

(۳) چك : ژند ویاژلد .
۴ - هزوارش نوشتن ,2111000180

ز خندة مه منجوق او بگرید جان .
مختاری غزاوی. افره ‎ery‏ نظام».

۴ - طبری ‎sherna‏ » مازندرالی کنوتی 52606 دواژه نامه ۲4۷4

دزآ گهی که ‎Aten‏ درون سیبده دمان

ie ‏رگ‎ ۵

ز بیم شنة او شیر بقکند چنگال .
‎Chante‏ رمذی. «لفت فری 4۷۲.

شنودن < اشنودن ‎(pe)‏ » پهاوی 25۳1018۳ , یازند

oxshnavamiy ‏اشنودن) « ازپارسی‌باستان‎ : sly) xshnddan . (;,:+) shnavesho
(yan) beshndstan ‏«هوبشمان-اسشق ۷۹۵ طبری‎ Sanagh ‏بلوچی‎ xshnd ‏ازرمشة‎
‏«راژءبامه6۱۲۰, کیلکی0(1:00۵۷25)2۳),‎ beshnossen,bashniissan,y ‏مازندرانی کنو‎
. 4٩۲۰ ‏سخن سال دوم شمارء ۸ ص‎ Alene « shonidan ‏تا جیکی‎

مرغ آزپس ‎OW‏ خوردن او ریزه نچیدی.

> کلتان ۱۰۹ ۰.

Gas ‏طمامش‎ sy ‏بجز‎ on - ۲

۸ - رگ : شولبر .
* شنودی - بنم اول و درم ‎gids‏ چهارم » ‎Cem) Gage‏ اشنودن ‎po)‏
```


## [2026-09-06T21:01:04.928Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"unüden\\|šunüden\\|snüden\\|snīden\\|senīden\\|snuden\" HUB.txt | head -20; echo \"--- HUB srūd\"; grep -n \"surūd\\|surüd\\|sarāī\\|srüd\\|sraosha\\|sraosa\\|srōš\" HUB.txt | head -20"
}
```


### [2026-09-06T21:01:04.981Z] TOOL RESULT

```
--- HUB srūd
6050:(suru) *Horn*, zd. srvd- ; sards der Engel' = zd. sraosa- ;
7569:Engel) ^ zd. sraosa-; suriidan singen, pr. sarayam, zd.
```


## [2026-09-06T21:01:08.600Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6040,6060p' HUB.txt; echo \"====\"; sed -n '7555,7590p' HUB.txt; echo \"=== leaf of 7569\"; python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (6050,7569):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    print(ln,'leaf',t[:idx].count('\\f'),'printed',t[:idx].count('\\f')-10)\nEOF"
}
```


### [2026-09-06T21:01:10.748Z] TOOL RESULT

```
bar etc.) oder ist iiberhaupt nicht sicher zu bestimmen.
.a)Vorschlag von a liegt vor in: abrii *Augen-
braue', skr. bhrU'\ aspand (isfand) *Raute', arm. spand, zd.
spenta-; asndsa {isnosa) 'das Niesen H. 90 und oben p. 15;
AfrSdun = Faredun, zd. ^raetaona- ; Afrdsiydh, zd. fran-
rasf^ u. 8. w.
b) Einschub von a in: baraz *Schmuck', zd. braza-
und baraza^] barezan, barejan 'Backofen*, Wrzl. iran. brij,
skr. bhrjj; xaridan *kaufen* (F. i. 8h. xirtdan), skr. ptc.
krUd^; sarai *Palast' = ap. *5raJa- (s. p. 74 und 199); saru
(suru) *Horn*, zd. srvd- ; sards der Engel' = zd. sraosa- ;
faraz *aufwarts*, skr. prad-; faramos Vergessen H. 812,
u. 8. w.
c) Vorschlag von i in: isparud *ein kleiner Vogel'
H. 78; istOx 'Zweig* H. 82; isfand *Raute*, isnGsa *Niesen
(siehe oben); ispar {sipar) 'Schild*, afgh. spar, phi. spar;
isparl (= sipart) Vollendet', phi. spurlk (oben p. 73) ; isped
(= siped) weiss, zd. spaeta-; istabr = sitabr H. 713;
Istaxr = phi. Sfaxr; istanba = sitanba H. 718; iskara
(Vullers: iskira) *Jagdhabicht* = sikara, u. s. w.
d) Einschub von i in: biradar *Bruder = ap. bra-
====
§ 102. Ap. s (= idg. k^) vor p (— idg. v), y, m und
r = phi. paz. np. s: asp *Pferd* = ap. aspa-; aspand
*Raute' = zd. spenta-; siped Veiss' = zd. spaeta-; sipihr
'Himmel* = ap. 2md-Qi-, skr. gvitra-; phi. harvisp jeder=^
ap. haruva- -)- vispa- ; mit Ausfall des p : suvHr *Reiter =
ap. asabara-] astar ^Maulesel' = ap. ^asatara-, skr. agva-
tara-; sa^ Hund', medisch andau, zd. spa; — siyah *schwsirz
•^ zd. syava- (aber kasaf 'Schildkrote' = zd. kasyapa-,
Auifallig ist' auch bal. gunas. Man hat fiir iran. Hinasa- =
ap. *vina9a- im Bal. *gtnas zu erwarten, das vielleicht duroh das ent-
lehnte np. gunah zu gunas geworden ist.~ 213 —
skr. kagyapa-); — dsmdn 'Himmer = ap. asman-am (ace);
— xusru *Schwiegermutter (auch xmfl u. s. w.) = skr.
gvagrU-] Xusrav = arm. Xosrov, zd. husravah-; Sards (der
Engel) ^ zd. sraosa-; suriidan singen, pr. sarayam, zd.
srU'\ sardi *Palast* = ap. "^srada-; surun 'Hinterbacken* =
zd. sraoni'^ surbj usrub *Blei* H. 728, oben p. 74; siristan
mischen*, skr. griS (siehe oben p. 75) ; sirisk *Tropfen = zd.
sraska-; surU *Horn', zd. srvd-; mit Umstellung von ausl.
sr in rs: ars 'Thrane* == zd. asm-.
Aber sayal ^Schakal* = skr. grgala- ist LW. aus dem
Indischen. Ueber sunudan *h5ren, pr. sinavam siehe oben
p. 82; uber aSk *Thrane' p. 15.
§ 103. Ap. rs (= idg. rk^) wechselte mit r^, wie
der Wechsel von np. rs mit hi zeigt:
a) gars *Haar (siehe oben p. 92 und 109) = phi. vars,
zd. varesa-; Pctrs =^ ap. Pdrsa-; gurs ^Hunger, gursina
hungrig* = ap. *vrsa', *vrsna' (neben gusna *hungrig*, von
tisna 'durstig beeinflusst, oben p. 92), dessen s freilich nicht
aus idg. k^ entstanden zu sein braucht. Np. Oarsdsp bei
Fird. ist aus ^Kirsasp = zd. keresaspa- entstellt.
b) iil = cihil Vierzig aus *^ihihl = "^cahihl = *cadf&
= ap. *da&vf&at' = zd. dadwar(e)sat'em, skr. datvarjgaU;
pahlu *Seite' = zd. peresu-^ paresu-^ skr. pargu-j ap. *pard^U',
Vgl. § 97: ap. rd- = np. hi
§ 104. Ap. 8 =^ iran. s, idg. sVh bleibt s im Np. :
=== leaf of 7569
6050 leaf 181 printed 171
7569 leaf 223 printed 213
```


## [2026-09-06T21:01:18.448Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==93' HUB.txt | head -50"
}
```


### [2026-09-06T21:01:20.085Z] TOOL RESULT

```
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
```


## [2026-09-06T21:01:33.877Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint('npages',len(t))\nfor i in (64,65,69,70):\n    print('#### pdf',i,'printed~',i-5); print(t[i][:2500] if i<len(t) else 'NA'); print('====')\nEOF"
}
```


### [2026-09-06T21:01:35.583Z] TOOL RESULT

```
npages 115
#### pdf 64 printed~ 59
[pdf page 65]
انا انا فعلهای فارسی دری
«ستاند» ج «ستانید» مادهٌ ماضی جعلی از «ستان» است.
۱ ستودن
ستود + فارسی میانه 5100 < ایرانی باستان ۹18-12*. برای 2 آراست. صورت
ضعیف 514۷ است و ريشهٌ 912۷ به معنی «ستودن» است.
ستای < فارسی میانه 513 < ایرانی باستان 8ر813۷-۵*. 278 نشانه‌ای بوده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است. ‎٩13‏ صورت بالاندةٌ ریشهٌ 312۷
است.
دا
سخت + فارسی میانه 3231 < ایرانی باستان ۶۵-1*. برای ۵ > آراست. 8 صورت
اصلی است و آن صورت ضعیف ريشهٌ 8 به معنی «کشیدن» است. برای
ضعیف‌کردن ريشه 8 حذف شده است.
سنج + فارسی میانه [828 < پهلوی اشکانی [8۵2 < ایرانی باستان ۵-[۶28*. برای 8 ->
آرای. [به جای ج آمده است.
سرشتن
سرشت < فارسی میانه 85151 + ایرانی باستان ۶713-1۵*. برای ۵ > آراست. کزرّه
صورت ضعیف ريشةٌ 8788 است و آن به معنی «چسباندن» است.
سریش < فارسی میانه 8783 < ایرانی باستان ۶۲۵15-2*. برای 2 > آرای.
«(سریش)» به معنی «رستنی‌ای که ... بعد از رسیدگی خشک کنند و آرد سازند و
کفشگران و صحافان چیزها بدان چسبانند.» (برهان قاطع)» از ریشهٌ 788 است.
سرودن
سرود + فارسی میانه ۶734 < ایرانی باستان ۹۳8-1۵" برای 1۵ > آراست. ‎٩۳3‏
‏صورت ضعیف ريشةٌ 818۷ است. به معنی «خواندن».

====
#### pdf 65 printed~ 60
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

====
#### pdf 69 printed~ 64
[pdf page 70]
ماده‌های ماضی و مضارع قارسی دری سس ۶۵
ی یف ۰
شیفت + ایرانی باستان 33۳۵-۲1۵*. برای 1۵ -> آراست. 0ه7537 صورت اصلی
آنه5۷* است. 0 پیش از 1 بدل به آ شده است. ريشهٌ 8۷۵10*به معنی «جنبیدن) است.
شیب < فارسی میانه 580 + ایرانی باستان 35۷/۵10-۵*. برای 2 > آرای.
«شیفته» صفت فاعلی گذشته از «شیفتن» است و در بیت زیر از گرشاسبنامةٌ اسدی
«(مشیب) به معنی («ناراحت مشو) به کار رفته است:
شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
فراموشیدن, فرموشیدن
فراموشید. فرموشید + فارسی میانه 1 ماد ماضی جعلی است. از ماده
مضارع ساخته شده است. در فارسی دری «فرامشت» بازماندة 11371۵31 فارسی میانه
است. 1۳30۵1 بازمانده 112-3-7108-1۵* ایرانی باستان است. برای 2 > آراست. 3و 5۵
هر دو پیشوند فعلی هستند. ريشةٌ کار" ظاهراً به معنی «فراموش‌کردن» است.
فراموش, فرموش < فارسی میانه 137۵5 < ایرانی باستان 172۵-3-۳۵5-۵*. برای 2
> آرای. 13۵05 صورت افزودةٌ ریشهٌ 05 است.
فرجامیدن
«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
فرستادن
فرستاد + فارسی میانه 1۲68130 1138110 هر دو ماده ماضی جعلی هستند. از 11

====
#### pdf 70 printed~ 65
[pdf page 71]
و فعلهای فارسی دری
ماده مضارع.
فرست س فارسی میانه 1۳681 ج ایرانی باستان - ها5زه ۳ *: فرستاده. قاقنه۲؟ صفت
[ مفعولی گذشته است از پیشوند فعلی 8 و هاگٌذ: صفت مفعولی گذشته از فا صورت
ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
قرشته از 121512-1۵ آمده است.
فرسودن
فرسودن. فرسای در فارمسی دری بسیط است. اما از نظر تاریخی از پیشوند 2 و
«سودن» و «سای) ساخته شده است + سودن.
فرمودن
فرمود « فارسی میانه 1۳۵7004 + 1۳2۵034 < ایرانی باستان 1۳۵-3-12*. برای 12 -> .
آراست. 178 پیشوند فعلی است. 33 ريشه است به معنی «اندازه گرفتن». 1۳۵/14 به‌قیاس
با فعلهایی چون 8737 و ۹۳84 به وجود آمده است. :
فرمای < فارسی میانه 172۵08 < ایرانی باستان ۴1۳۵-3-8 12 نشانه‌ای برده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
فروختن
فروخت < فارسی میانه 1۳071 < ایرانی باستان 1۵-0-1۵ *. برای ۵ > آراست. ۲۵
پیشوند فعلی است. 1 صورت اصلی 0 است. ۴ پیش از 1 به # بدل شده است. ۷1
صورت ضعیف ۷۷۵و آن به معنی «گفتن» است. ۱
فروش دج فارسی میانه 1۳05 ج 105 «<ایرانی باستان ۲۳۵-۵55 *. ‎٩‏ برای ساختن
ريشةٌ جدید به کار می‌رفته و 1 پیش از 5 به #بدل شده است.
فرهیختن
فرهیخت + فارسی میانه 1۳80451 < فارسی باستان 0۵-1۵ -1۳۵*. < ایرانی باستان

====
```


## [2026-09-06T21:01:49.294Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'شنودن' in p or 'شنید' in p or 'اشنو' in p:\n        print('#### pdf',i,'printed~',i-5); print(p[:2200]); print('====')\nEOF"
}
```


### [2026-09-06T21:01:51.054Z] TOOL RESULT

```
#### pdf 68 printed~ 63
[pdf page 69]
جوا را فعلهای فارسی دری
است. این ريشه به معنی «صبر کردنْ» است.

شکیب < فارسی میانه 51650 < ایرانی باستان 8-م۶۵1*. برای ۵ > آرای.

شمردن

شمرد + فارسی میانه 530076 < ایرانی باستان 1-37:۳4۵ط۵*. برای 18 -> آراست.
201 پیشوند فعلی است. ۳7337 صورت اصلی 55 است. ۵ بعد از آبه 5بدل شده است و
#به جای 27 در صورت ضعیف ريشه آمده است. ريشهٌ ۰1337 که صورت دیگرش 11۵7
است و از آن «آمار» آمده» به معنی «شمردن» است.

شمر, شمار < فارسی میانه 0570۱۶ 0337 < ایرانی باستان 1-57037-8ط۵*. برای 2
< آرای. 3۳37 صورت بالاندةٌ ريشةٌ ۸۸۲ است. 580۲ با حذف 4 از ۰5307۵
به‌قیاس با ۷8۵7 و ۷۷270 به‌وجود آمده است.

شناخت + فارسی میانه 5031. به جای 50371 باید 5034 می آمد» از 3۸3-18* ایرانی
باستان. ظاهراً به قیاس با فعلهایی چون ۹32و ‎٩381‏ بوده که 5371 به وجود آمده است.

شناس < فارسی میانه 5039 < ایرانی باستان 3503-6۵*. 58 برای ساختن ماد آغازی
به کار می‌رفته است. ريشهٌ 583*به معنی «شناختن» است.

شنودن :

شنود < فارسی میانه 25084 < ایرانی باستان ۴۹58-12 برای 1۵ > آراست. 7608
صورت ضعیف ريشهةٌ 7573۷ است» به معنی «شنودن».

«(شنید» و «شنفت» صورتهای دیگر «شتود» هستندء هر دو در فارسی دری به وجود
آمده‌اند.

شنو + فارسی میانه 252۷ ه ایرانی باستان 5۵۷-۵*. برای ۸ > آرای.

====
#### pdf 98 printed~ 93
[pdf page 99]
کب ال ات ی فعلهای فارسی دری
53 (ریشةٌ بالانده > 5۵ج) ۶۲ ای ده
۶۲۵ 40 (ريشه - خواستن) ۵۱
4 (< شیرء لبن) ۳۹ ای مهم

۱ ۷ (ريشه < شنودن) ۶۴ 2 (ر(ريشةٌ بالانده > 0۵5 ۵۱
اند + مها نا ان مه
83 (ريشه < شناختن) ۶۴ ۵3
4 ۶۴ نکن وه
۳۴8 0 (ريشه < نبرد کردن) ۴۷» ۴۸
ر(ريشةٌ ضعیف *52۷) ۶۴ ۴2
۶۴3 2 (ريشه < ستودن) ۸۲
0 (ريشةٌ ضعیف ۰۲۶320 ۶۹ ۸۲34۵
40 (ريشهٌ ضعیف > 5۵04ج) ۶۳ 40 (ريشةهٌ ضعیف -> 204) ۴۷
۶۳13 3
43 ۶۵ 12 ۴۷
0 (ريشه < جنبیدن) ۶۵ 1 (ريشه - زادن) ۵۷
ند اند مها 43 (ريشةٌ ضعیف > 2271) ۵۷
:0 قسقد: ۵۳
۵ 3 (ريشه < تحریک کردن) ۲۵
((ريشه - بانگ کردن) ۵۱ 14 ۵۷
اد وم 42 ۵۷
0 (ريشه < خفتن) ۵۰ ۵۱ 5 : (ريشه < پژمردن) ۴۳
ناد موه 5 (ريشةٌ ضعیف *27327) ۴۳

====
```


## [2026-09-06T21:02:02.401Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"husrav\\|hu-srav\\|dusrav\\|du-srav\\|dušrav\\|srav\\b\" SNS.txt | head -20; echo \"=== SNS pages grep\"; grep -n -i \"husrav\\|dusrav\\|dušrav\" SNS_pages.txt | head -10"
}
```


### [2026-09-06T21:02:02.457Z] TOOL RESULT

```
5487:.^LSrfi .^s^-i- rhusravlh: -^^v-***? 
11197:.ll/H^-^*^" 1633) /srav : jl sraota-:t- 
17996:•***<jt 'C^ •** :<*usrav: -iJ**** 
32409:husravlh 66/18 
33264:dusrav 331/18 
=== SNS pages grep
3454:                                                                                                                                                                       .^LSrfi .^s^-i-              rhusravlh: -^^v-***?
16086:                        husravlh 66/18
16318:dastOrlha 314/14            derang 185/9                 doxt 334/19                dusrav 331/18
```


## [2026-09-06T21:02:03.124Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سروا\\|سرواد\\|سرواده\" FRS_pages.txt | head -20"
}
```


### [2026-09-06T21:02:03.175Z] TOOL RESULT

```
274: ‫این بیان ناصرخسرواینست که قطران ازراه تعلیم و تمرین دگفرتن شعر‬
873:              ‫|نانکه ابو طاهر خسروانی گوید ‪:‬‬
970:     ‫‪۰‬‬     ‫(‪۰ )۶‬ج‬        ‫و بمن این سروا‬           ‫چند فروشی‬    ‫‪:‬‬    ‫* ‪ -‬ع مثال را ندارد » س‬
1097:                             ‫پنداری بود |چنانکه خسروانی گوید‪:‬‬
1520:                                                   ‫بترآبد یرون ‪ 1‬خسروانی گوید‪:‬‬
1892:          ‫نام شاعر[ی ]استاد بود بدخاررا ؛ ابوطاهر خسروانی گوید ‪:‬‬
2611:‫کران برهم بخشند » خسروانی گفت ‪:‬‬
2672:                              ‫و زنونتههمان بود خ»سروانی گفت ‪:‬‬
4221:                                            ‫ابتدای کارها باشد » خسروانی‬
4504:                                                            ‫دیگری از خسروانی‪:‬‬
4786:                                                   ‫گفت ‪:‬‬   ‫کل بود[ خسروانی‬
5106:                   ‫دیبایی باشد نك و نرم » ابوطاهر خسروانی گفت ‪:‬‬
5261: ‫‪ -۱‬چ سرواد شمر را خوانندوچنامه وچگامه‬                         ‫‪ - ۰‬این‌بیت درچ ول هست ‪.‬‬
5269:‫که رفت یکرها بازار وقیمت سرواد‬
8192:                                          ‫سر عقبه‌بود؟» خسروانی *‪ ۱‬گوید ‪:‬‬
8219:                         ‫‪ - ۱۱‬چ ‪ :‬ابدش در پیش ‪.‬‬      ‫شدة بوطاهر خسروانی است ‪۰‬‬
9557:                                                        ‫تظلم بود|خسروانی گفت‬
11615:                                             ‫تست اونئد [ خسروانی کفت ‪:‬‬
11729:              ‫بهار خانه است وشهریست بتر کستان [ خسروانی کود‪:‬‬
11732:‫شد؟ ]‬    ‫دو چشم خسروانی چون رود نگ‬
```


## [2026-09-06T21:02:12.173Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11190,11205p' SNS.txt; echo \"---17990\"; sed -n '17988,18005p' SNS.txt; echo \"=== dusrav entry\"; grep -n \"dusrav\\|dusrav-\" SNS.txt | head; grep -n -B3 -A3 \"dusrav\" SNS_pages.txt | head -20"
}
```


### [2026-09-06T21:02:12.251Z] TOOL RESULT

```
1Y/TT i5 (*=-»! ayl^-oi- L,!,) 

■r/vr^ fay*) 1 **"*) "A - <*u- :«flarW" 

■ u/a^ .^!^<ds^ :be srfld: t^*»j-D 

• J i^- :srudan:«Y , V-" 
.ll/H^-^*^" 1633) /srav : jl sraota-:t- 

^(.U.vtrfo.l^^U^U* (.b^jt,^ :sr6lcarn5m: .£ V e-KJV>*> 



AY 


---17990
» o6/X v5 (-,,*: jud: f¥ '•<&) «**tjfiyadi 



*>*< 



•***<jt 'C^ •** :<*usrav: -iJ**** 
f*j*ttW dusrab:^ UiSfc. 741)d3us. sravah-:^lL- j 

.O^/tf^'O^/'O^ :stadan: YNSBWN, tfi: >.: «*»*>*« 

• tV-Af/T^ 




=== dusrav entry
33264:dusrav 331/18 
16315-dastOr 314/5                denlh 193/14                 dost 331/14                dubSzag 328/18
16316-dastoran 314/8              den radan 193/11             sos 332/13                 Dufdav 329/22-335/1
16317-dastorlh 314/10             dSr 182/13                   dosend 334/18              ducmDbag 328/7
16318:dastOrlha 314/14            derang 185/9                 doxt 334/19                dusrav 331/18
16319-dast soy 187/19             der-zaraan 183/13            drayan javisnih 319/16     -dus 332/16
16320-dast sabtg 187/16           dSr zlvad 183/15             drayid 320/4               dus agah 332/19
16321-dast sustan 187/18          dfirzlvisnlh 183/17          drahra 341/19              dusax v 331/1
```


## [2026-09-06T21:02:13.388Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nn=0\nfor i,p in enumerate(pages):\n    if 'سروا' in p:\n        print('#### leaf',i)\n        # print context\n        import re\n        for line in p.split('\\n'):\n            if 'سروا' in line: print('   ',line.strip())\n        n+=1\n    if n>6: break\nEOF"
}
```


### [2026-09-06T21:02:15.129Z] TOOL RESULT

```
#### leaf 8
    ‫این بیان ناصرخسرواینست که قطران ازراه تعلیم و تمرین دگفرتن شعر‬
#### leaf 24
    ‫|نانکه ابو طاهر خسروانی گوید ‪:‬‬
#### leaf 26
    ‫‪۰‬‬     ‫(‪۰ )۶‬ج‬        ‫و بمن این سروا‬           ‫چند فروشی‬    ‫‪:‬‬    ‫* ‪ -‬ع مثال را ندارد » س‬
#### leaf 29
    ‫پنداری بود |چنانکه خسروانی گوید‪:‬‬
#### leaf 41
    ‫بترآبد یرون ‪ 1‬خسروانی گوید‪:‬‬
#### leaf 49
    ‫نام شاعر[ی ]استاد بود بدخاررا ؛ ابوطاهر خسروانی گوید ‪:‬‬
#### leaf 65
    ‫کران برهم بخشند » خسروانی گفت ‪:‬‬
```


## [2026-09-06T21:02:25.589Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17993,18000p' SNS.txt; echo \"---5480\"; sed -n '5480,5495p' SNS.txt; echo \"--- 11190\"; sed -n '11185,11200p' SNS.txt"
}
```


### [2026-09-06T21:02:25.648Z] TOOL RESULT

```
•***<jt 'C^ •** :<*usrav: -iJ**** 
f*j*ttW dusrab:^ UiSfc. 741)d3us. sravah-:^lL- j 

.O^/tf^'O^/'O^ :stadan: YNSBWN, tfi: >.: «*»*>*« 

---5480
I . W/H^ W£VZ>. 408)usa-fritay- :fc» 

" '•*-»■- * ^ j £*- Ju J 1 ( V») s 5stlg3nlha : -*oo*r.i>W**t?' l 
wstyk'nxjk^Sj^, {Mir. Man. II, 55) hwstyg'n:>;fc 

■ YA/1T^ (XoiuaZ, 160) 

.^LSrfi .^s^-i- rhusravlh: -^^v-***? 
{Miv.tf hwsrwg : jzti {AiWb. 1738) haosravah : fc» 

MaH. II, 55) 

• & ,>*>*• iS^jj** j' (/* 'J** 1 *f** '^** :hCi: ■*U*' 
CMan. Stud. 51) 'by'ws -^ -&~AiWb. 414) us-:' 3 - 


--- 11190

tY/YT^.^-r/IY^.fr/ir^ (4£IW>. 1634)sraosa-: fa- 

.t-At'j*J**j*irjj- :sroi ahrav: _yW* J ^^* 5 

1Y/TT i5 (*=-»! ayl^-oi- L,!,) 

■r/vr^ fay*) 1 **"*) "A - <*u- :«flarW" 

■ u/a^ .^!^<ds^ :be srfld: t^*»j-D 

• J i^- :srudan:«Y , V-" 
.ll/H^-^*^" 1633) /srav : jl sraota-:t- 

^(.U.vtrfo.l^^U^U* (.b^jt,^ :sr6lcarn5m: .£ V e-KJV>*>
```


## [2026-09-06T21:02:26.372Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf8',errors='replace').read().split('\\f')\nprint(t[26][:2500])\nEOF"
}
```


### [2026-09-06T21:02:28.375Z] TOOL RESULT

```
                                                  ‫‪۷‬‬
                                              ‫‪۱‬‬       ‫و‬
                                              ‫کیت‬
                                                   ‫ناطف ‪ ۱‬بود » عایان مرغزی کو بد ‪:‬‬
 ‫[ شمس دنیا توفخر دین منی ‪ .‬فخر دنیا توشمس دین ملی‪] ۲‬‬

  ‫ملی‬           ‫تو کییتای کجدینی‬                          ‫ور همه زندکان‪ ۴‬تر ینه ؟شوند‬


                                                   ‫ِ‬
                               ‫|ذانکه اورمز دی گوبد ‪:‬‬
                                                    ‫حدیث و افسانه باشد چ‬
                                       ‫وده دروغ هی چند‬
                                                     ‫چند دهی ع‬

   ‫چند فروشی بمن تواين سر و سرو!؟ ]‬
                                              ‫لا‬
                ‫تفسیر زند است و زند صحف ابراهیمبود » خسر وانی گفت ‪:‬‬

                                  ‫چوگلبن ازگل‪ ۲‬آتش نهاد وعکس افکند‬
 ‫وستا خوان‪۸‬‬          ‫بشاخ او بر "دراج کشت‬



 ‫‪ -۱‬الناطف نو ع من العلوا قال الجوهری هو القببط قال‌غبره لاتهبتنطف قبل استضراه‬
           ‫‪1۰‬‬                    ‫پر‬       ‫‪۳‬‬                            ‫‪۳‬‬     ‫‪۳‬‬   ‫ند‬   ‫‪۱‬‬   ‫‪۶‬‬   ‫‪۳‬‬
 ‫ودرا نجا بجای‬     ‫هست‬   ‫درس‬   ‫‪ 7‬کی این «ت ‪۳‬‬                ‫خثورنه (نا ج‌العروس)‬      ‫ای‌شصر فل‬

‫‪-۳‬ص‪:‬نیکوان ‪ ۰‬ظ ‪ :‬ریدکان‬         ‫الدین ضبط شده‪.‬‬            ‫بجر دبن وشمس دین فر الدین وشمس‬

 ‫‪ :‬ابرنهصحیح همين تربنه است که ضیط جهانگیر ی وعی است ازطه‌ام وخورش‬                                ‫‪3‬‬

 ‫که مردم فقیر ونا مرادآ نرادرآشهای آرد و جز آن ریخته بخورند » سنائی گوید ‪:‬‬
‫و حاو اش‬        ‫ببس از وفات چه لذّت ‪3‬‬              ‫ترربنه گر بخورد مرد سفله پیش ازمر کت‬
     ‫‪۰‬‬     ‫(‪۰ )۶‬ج‬        ‫و بمن این سروا‬           ‫چند فروشی‬    ‫‪:‬‬    ‫* ‪ -‬ع مثال را ندارد » س‬

 ‫یهدمست‬
      ‫‪ ۶‬استا وزند وستا » زتدصحف اا‬                 ‫‪٩‬‏ ‪3 -‬‬          ‫چنده فروشی بخبر و بأمن شروا‪.‬‬

 ‫شاح اویردراج‬       ‫‪۸-۰‬‬        ‫وج ‪ :‬بر ‪.‬‬           ‫‪ -۷‬ع ‪:‬تن ‪ .‬س‬             ‫واستا تفبرش بود‪.‬‬
                                                                      ‫شد استا خوان [کذا ]‬
                                                                                          ‫‪۰‬‬
```


## [2026-09-06T21:02:40.317Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sraoQra\\|sraodra\\|sraoöra\\|sraoBra\\|sraoθra\" BRT.txt | head -10; echo \"--- sravah\"; grep -n \"sravah-\\|sravah'\\|1637\\|1638\" BRT.txt | head -10; echo \"--- haosravah\"; grep -n \"haosravah\\|Jiaosravah\\|haosrav\" BRT.txt | head -10"
}
```


### [2026-09-06T21:02:40.386Z] TOOL RESULT

```
--- sravah
6393:•1  PüEjL   iu    Yl'/.  10   scheid'et    drei   kjXen   Asa  betet.."  H. /.  I  f.** ■il-nakr.ätii/r/ftar.äni^aldäsaki^ü.-.mecchi-,      Komp.  mit  AS.  im  1.  Glied.  —  Pü.:  ahräkih iJrT,  an  i /rtflai.    Aber  die  beigegebenen  Defi-        iläyiinih.    —    1)  Ausg.  trennt    —    ')  Wörtl. : nilionen  sind  undeutlich;   vgL  DsT.  ZA.  /.  9I. '      "ciii  (est)  ..?  eius  qui  .  .",  Bthl.  BB.5.  301; S.  noch  SWienAW.  6/.  839.  8:    .  .  dh'l})  . .  ii       anricblig  JN.  JAOS.  ]-4.  Lxi. a:,,  »,>i«  ,  ^jrdumänja^g  a„M.  |,  j   +asi>m.sravah- '>   n.   'der  As'Md-  i-
13520:•  j.  d9U§.sravah-  n.,  Plur.  'übler  Ruf, schlechter  Leumund':  ula  buya  ..  uta  'vä (AP.)  hacimnS  ".  .  und  Üblen  Ruf  mögest du  bekommen"  Y. //.  i.
13797:•  j.  dus.sravah'  Adj.  'der  einen  üblen Rur,  Leumund  hat,  Su7KXr)j^.
14980:•  j.  paiti.par^tö.-sravah-  Adj.  'der  die (heiligen)  Lehren  erfragt,  (durch  Fragen) erkundet  hat' :  narim  . .  vJdus^ga^sm  vtdul.- yasfiim  'vatahsm  mqsdrtm  V.  lÄ  5 1 ;  — ähravans  parsts.vaiarth5  'variks  Yt  5. 91 .
24087:•  j.  viJt'sravah-  m.  EN.  eines  Gläubigen: uxsänS  (sd.)  'vatihS  düralsrstahe  Yt 13.  129.
27089:1637
27190:•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
27292:1637
27294:1638
27377:•  j.,  g.  sravah-  n.  i)  'Wort'  (in  koll. Sinn),  (Plur.)  'Worte':  at  vS  ximaihyä asünä  va^ä  x^arai^yä (sA.)  vaintyä  'vi" Y.  2tV.  10.  a)  sva.  'Spruch,  Lehre': dusjastis  'vä  mSrindaiisA^  V.^2. 9;  10;  1 —  ya  ränhaym  (Sp.  iji?  u-)  'vanha*''  1 vahistät  syao%anäi  mantiVW  Y.32.  la;  —  j masda  al  insi  vahiHa  'vsscä  iyaohanäcä ' vao/ä  . .  isiidpm  (sd.)  stS/J  Y.  34.  is^^i  — yai  ta    'Vit  dtvn/ayan  ya  ..  al%rapaiayö\
--- haosravah
4810:1.  a)  "herausgehen  aus  — '  (Gen.):  vai- \anhS  (sd.)  n5/V  uzSis  (aSPrA.)  V.J.  15 PüZ.(?).  a)  'aufgehen',  von  Gestirnen: yaira  avat  hvars  uzliti'J^F.4h.  3) 'hin- auskommen über  — ,  über  werden',  mit Äaca  und  Gen.r  ya'ia  as»m  uzayeni  haia kavsis  haosravauhahe  Vt  i^.  32.
6305:•  j.  aäavasta-  n.  'Besitz,  Erwerb  des (höchsten)  Anrechts':^»  "^wä yäsämahi havauhum  't*m?a  haosravaahftn  Imru- mauii  Yt  10.33;  —  yüimäkim  yasnäica paimaUa  yal  am3sanam  spmtanqm  a/imä- ifM    hmHiauhäica    °täica  yal  taosyantqm
6372:•  j.  aää'vaohav- m,  EN.  eines  Gläubigem 'störend':  -mirmls  (als  NS.)  yaiia  kava ^ifh}us  hii'attdatihahe  asaonS  Vt. /J.  uo.     ^*haosrava  Vyt.  2  (?)'*.
6888:"  j-i  g-  'ahura-  m.  i)  jAw.  'Herr,  Macht- haber, Fürst":  'rO  *sästr)nqin  äaiiihupai/is VliJ.  37;  —  ^wqm  yazante  aurvanhB -ränhs  äai^hu.patayS  ¥1.5.85;  —  yim fnäml.  z'jrf^raytam)  vasiinte  'rät^hö  .  . ähuiryarffa  .  .  haosravatahanS  Yt  i4-  39;
7096:•  j.  ä'xrüra-  m.  EN.  eines  Gläubigen: "rahe  haosravanhalte  asifOHü  "des  A.,  Nach- kommens des  //.  .  ."  Vt.7y.137".
8253:dasin?m  'pa  karamm  aitiha  z^mS  Yt  10. 99;  —  dasin)m  hl  °pa  ars^sm  Vt  10, 100; 1 00';  —  dann?!»  'pa  sraxtim  N.  79 ;  7p';  — dasinqm  (sd.)  °pa  Yt.  13.6$.  7)  'in,  auf {auf  die  Frage  wo?):  a«/  .  .  rämyat  ioa •pa  imat  nmätani  Y.  iO.\;  —  yat  haosrava . .  *Om  kirpsim  (sd.)  'pa*^  tarn.  car?tqm  . . ¥1-/9.77.  b)  zeitlich,  a)  'bis  zu  -': danyimat  aipi  zrväram  "pa  särqm  */rasS.- kirntUn^    ^.62.%.  ß)    'beij    um':    ks
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
9578:kava  haosrava  *t?m  's>tn  upa  tarn  cantam  *  ,  „  .     ,  ,       ,      ,
9960:14— 16'5  {fanät)'");  — yS  aSa!sqm  sünqm (als  Obj.)  >(«/(■  V.y.8;  w.  i,' FrB.;  '— /anaiii'*  vispa^qm  anrB  mainyu/Yt.3.5; Y.1S.2  PüZ.; — 'vjspa  druxs  jattaiti'^  Yt 2. 1 1 ;  12;  —  ya'ha  ya^  . .  janyät  *n)r^ V./1V.T2;  —  janät'*  t?m  . .  haosrava "töten  soll  ihn  .  .  H."  Yt.g.iS,  i5.32; ig,  44';  —  yat  janatii  /litüsppm  raüe ^paiti.vazaityäi  (sd.)  Yt.  J5.  28;  —  na?^a manyete  (sd.)  jaynvä  na^a.äm  y?nqm sadayeiti  (sd.)  Yt  /o.  7 1 ;  —  taha  hunavS  . . jata  pai^yänU  Mt.iO.iiy,  80;  — yasca dilti  janat  .  .  vikrhm  V.  7.  51  PüZ.;  52 PüZ.,  y.'s.  4,  Yt.^.  2*;  —  jata  (2P.?) karapanS  cT^rJm  Y1.4.T,  — fanäni  äqma daev3.dat2m  V.  ip.  5;  $',  Yt.  4.  $;'  — rasm5.jat>m  va  dim  jainti  amff.jabm  (sd.) va  Yt  70.52;  74. 36f.4;  —  ka'^a  (sd.) nisMäiamal  ya'^a    hltri  jatiüma  Y.61.  $;
16700:\yeni  bast?m  ,  .  Yt.5,  '^J  —  haosrava  .  .
```


## [2026-09-06T21:02:51.479Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sraosa-  m\\|sraosa-  n\\|'Gehorsam'\\|Gehorsam\" BRT.txt | head -8; echo \"=== sraothra\"; grep -n \"sraoOra\\|sraoQra\\|sraodra-\\|sraofra\" BRT.txt | head -6; echo \"=== Haosravah entry\"; grep -n \"Haosravah-  m\\|Haosravah- \" BRT.txt | head -5"
}
```


### [2026-09-06T21:02:51.569Z] TOOL RESULT

```
5052:•  j.  avaS-ät  Adv.  'so',  in  zurückweisen- dem Sinn:  av  ila  sraoli  asta  "so  soll sich  hier  der  Gehorsam  einstellen"  Y. 5«.i.
7075:•  j.,  g.  ä-kä-  i)  Adj.  'manifestus';  a)  'der sehen  lässt,  wa^  er  tut,  sich  bei  dem  was er  tut  sehen  lässt,  es  offenkundig  tut': aiiyi^  kasHt  .  .  para.baraiti  'ka  (NS.) *hazatiha  *anskils>  iayusU.tJj;  6.  b)  'der sehcQ  lässt,  was  geschehen  ist',  spez.  von den  bei  der  äkä-  (s.  2)  Beteiligten,  'Offen- leger': hadä  asil  vakistScä  tiiananhä  xsa- 'irä.'a  yä  (NPn.)  /w  stanhai  a  pai^t  .  . 'ka  (NP.)  ar^ärSng  d^mänS  garö  Sfrao^äiiS "sammt  .  .  und  dem  Xs.,  welche  als  Offen- leger,  von  den  Frommen  ersehnt,  auf  dem Weg  zum  Haus  des  Lobs  den  Gehorsamen erwarten  werden"  Y.50,4'>.  2)  f.  'mani- festatio,  dilucidatio',  d.  i.  die  'Offenlegung' der  Taten  des  ersten  Lebens  bei  den  letzten Dingen  " :  dngvats  . .  yehyä  urvä  xraodattT (sd.)  cinvaiö  pinta  'kä  (Abi.)  "-  .  vor  der Offenlegung  an  der  Brlicke  des  Scheiders" V.  5/-I3;  —  ka  '^wöi  alu  'i,i  (NS.) arfdrSiig  ilyJ  "wird  deine  Offenlegung, o  A-,  den  Froramen  erwünscht  seini*"  Y. 4<V.8; — vahiitö  anktti  °>f(7j(AbL)-i-'?iV (sd.) ahüire  jasmtqm  Y.  60. 11.
9804:au  Gunsten  von  — ',  mit  Gen.  (statt  Dat): käram  hyJ^  däraya'vahaus  gaubalaiy  Bh. 3.  9;  —  hatnih^iyä  abava"  uiä  fravar- lais*agaubc^ta  Bh.2. 16".  a)m!tNeg, sva.  'den  Gehorsam  verweigern',  von Truppen;  käram  .  .  Ayi^  manä  naiy  gau- bataiy'&h.2.6,3.3,i4;2.T,\o;  —  käram .  .  hy^  manä  naiy  gaubätaiy^^  Bh.  2.  14. ntp.  gmoel  'er  sagt'  (vgl.j-ii/j*  g'"')''  np.  ^ly'ija^. —  'I  Text  unsicher.  —  'i  Konjunktiv?
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
13169:horsam) leisten':  vacS  .  .  ySi  mfft  ahmäi tiraohm  dqn  layasea  "das  Wort  .  .;  alle die  diesem  meinem  Wort  Gehorsam leisten  . ."  Y.  45.  5.  b)  '(distributionem) facere':  ta  daiaS.jspmta  mainya  ..  vidäi- tim  (sd.)  ranöibya   Y.  4".  6.  c)  '(pro-
13536:•  j.  dar3tö.sraoäa-  Adj.  'am  Gehorsam festhaltend,  fest  im  Gehorsam':  uxhm  . . 'Ä/n  F.jf.
14914:oMe  vals  'tyesti  (IS.)  *para.aij  ufa.vazata ''nairys.sanks  "eius  verbo  obediens  abiit . ." V.  22. 1 3,  3)  'Gehorsam,  Botmässigkeit't xlä^nmca  'ti.asllmca  dar3yBJCsa%r3in  x!a- "^ra/ie  A. /.  8.  Unklar;  l>m . . yasamaide ahmSi  nmünSi  .  .  'H.asti  gJu/  vacah- yekeia  ^t.15.  i.
14916:•  j.  paiti.astö.-va£ah-  Adj.  'des  Worten nan  beipflichte^  des  Wort  Gehorsam  findet': /i  F.jf.
=== sraothra
17952:•  j.  fra-sraoOra-  n.  lautes  Aufsagen' staeianqm  yesnyanam  , .  °%r>mca  Jramart- 'hrsmca  fragä^rgmca^'' frayaitlmcaY .  ^^.T , "^t-S-  7 ;  13-  3,  Y.  20. 5.       a)  insbes.  'Beten'
27229:•  j.  sraoOra-  n.  i)  'Gehör'  (nur Komp.)''.  3)  'Zugehörbringen,  Auf- sagen (der  (7jäas)':  ga^anam^a  'nm  Y. J.  4,  22.3;  —  *'ra  *nS^^  gähanqm  ratufris N.  22;  —  ys  ..  *aittim  dahm»m  gohanqm *'räii^  pairisiayäti  N.  44;  —  vahiitötäsis grihaya  -rfm  Vyt.  5^.
=== Haosravah entry
27190:•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
```


## [2026-09-06T21:03:04.155Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 kleu\"; grep -n \"k'leu\\|kleu-\\|kleu(\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"=== IEC\"; grep -n \"kleuō\\|kleuo\\|kleu-\\|kleuos\" IEC.txt | head -10; echo \"=== SYN hear\"; grep -n \"kleu\\|15.41\\|śru-\" SYN.txt | head -10"
}
```


### [2026-09-06T21:03:04.235Z] TOOL RESULT

```
=== WLD Bd1 kleu
41066:ai. croni- usw. als „K6rperaus- oder -einbiegung“ die w-Basis kleu- neben
46665:1.    kleu- „horen", vielfach im Sinne von „wovon man                                                                      viel hort, beriihmt,
46831: 2.     kleu- (klo[u]-, klu-)                        „spiilen,      rein      machen         ,
46832:                                                                                                         Erw. *kleu-d-,          lett.       auch
46884:      Petersson LUA. 1916, 60 f. halt '*kleu- fur Erweiterung eines *kel- „feucht,
46892:dies zutrafe,ware fur kleu- kel- das Verhaltnis sreu- „HieBen“         :                                                                        :   ser- ent-
47211:genommenen Gdbed. „biegen“ der Wz. *kleu-                                        s.   u. ldeu- „horen‘‘.
=== IEC
7332:kleuoros (kləuər-, kleu-) ‘warm, mild”
7335:kloueros, see kleuor-
8970:and for Celtic Kloust-) WP I, 494. Cf. Kleu-, kleu-, Klutos, etc. Skt. srustih, f. ‘obedience’; Av. srustis, f. “hear- ing’; srusta, pp.; Mir. closs, f., Ir. clos, id.; OE hlyst, f. ‘sense of hearing’; OS hlust, f. id.; OFris. best ‘noise’; ON hlust, f. “ear”; LG cf. lusteren, Du. luisteren, OFris. hlestia, Sw. lystra, v. ‘to listen’
=== SYN hear
5893:Most of the words for ‘ear’ belong to an inherited group. ‘These and the others, so far as their origin is clear, are related to words for ‘perceive, hear’ (15.11, 15.41),
5901:3. Ir. cliias, NIv. cluas, W. clust : ON hlust ‘ear’ (beside eyra, cf. Vigfusson s.v.), OE hlyst ‘hearing’, hlystan ‘hear, listen’ (NE listen), etc. fr. IE *fKleu-s-, beside *kleu- in Skt. gru-, Grk. kdb ‘hear’, etc., from which root also Skt, grotra- ‘hearing, ear’, Toch. A klots, B klautso ‘ear’ (SSS, 128, 129). Walde- P. 1.494 f. Pedersen 1.80,
5902:Br. skouarn, Corn. scovarn, W. ysgy- farn (obs.), etym. dub., but perh., fr. a *skeu- beside IE *keu- in Grk. xotw ‘per- ceive, hear’, Lat. cavére ‘beware’, Goth. hausjan ‘hear’, OF scéawian ‘look at’, etc. (15.41, 15.52). Henry 243. Win- disch ap. Ernault, Dict. étym. 377. Less probably Pedersen 2.53.
22826:NG BaBourss, xotAos ON holr Lat.  cavus Dan. hul It. cavo Sw. thdlig Fr. creux OE hol Sp. hueco ME _hol(we) Rum. gdunos NE hollow Ir. cilia, cilassach Du. hol Nir. cuasach OHG hol W. cau MHG hol Br. kleus NHG hohl
22843:nig, dub. but prob. Rae ae 2257: Ranilenheg 277. Bloch” : Port. owco, 0Co, prob. (de difficulties) fr. VLat. acuus ‘empty’. REW 9165. i 4 Rum. gdunos, deriv. of ORum. gaun fr, Vat. *cavo (-énis) ‘cavity’, fr. cavus (above, 1). REW 1794... Puscariu 700. 4, Ir, cilassach, NIr. cuasach, fr. ctlas thole’ : cia (above, 1). Br. kleus, fr. Fr. creua with 1 fr. kleuz ditch’. Henry 70. 5, ON holr, OE, OHG hol, etc., gen- eral Gme, (Sw. ihdlig, hdlig fr. hal ‘hole’, ab, fr. OSw. hul adj.), perh..: Grk. xavdés
25849:15.41 Hear
25926:W. clywed, Br. klevout, ‘hear’ (15.41), but used in Welsh of all Sense-percep- tions except sight (cf. Evans, s.v., Loth, RC 40.359), in Br. also ‘learn, under- stand’ and ‘smell’ (Ernault s.yv.).
25949:6. ChSl. poéuti, perfect. of éuli ‘rec- ognize, notice’, SCr. uti ‘hear’, Boh. iti ‘perceive, notice, smell’, Pol. czué ‘perceive, smell’, with sbs. ChSl. éuvisivo, Russ. éuvstvo (SCr. éuvstvo, old in this sense), whence Russ. ¢uvstvovat’ ‘feel, perceive’ : Grk. xoé ‘notice’, Lat. ca- vere ‘be on one’s guard, heed’, Grk. axobw, Goth. hausjan ‘hear’, etc. (15.41). Berneker 162f. Walde-P. 1.369.
26181:15.41 HEAR
26222:ey : 1036 15.41-15.44. The verbs for ‘hear’, de- noting the actual perception, may also be used for ‘listen’, especially in the im- perative. But generally there are also distinctive words for ‘listen’. Most of these are cognate with the words for ‘hear’, either those so used in the same language (NHG horchen : héren, NE harken : hear, Russ. slugat’ : sly- Sat’) or in other languages (NE listen, etc. : Grk. xAtw, etc.). In a Celtic group ‘listen’ rests on the notion of ‘be silent, be still’, which elsewhere is a sec- ondary association of ‘listen’ (cf. below, 4). Other secondary developments of ‘listen’ are ‘listen for’ > ‘watch for, wait for’ (OF hlosnian) and ‘be atten- tive to’, esp. ‘obey’ (Lat. auscultare, NHG gehorchen, Dan. lyde, Sw. lyda, Lith. klausyti, ChSl. poslusati, etc.).
```


## [2026-09-06T21:03:09.282Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46665,46700p' incoming/WLD/WLD_Bd1_pages.txt; echo \"== leaf\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n'); idx=sum(len(l)+1 for l in lines[:46664])\nseg=t[:idx]\nimport re\nm=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('last pdf page tag',m[-1] if m else None)\nEOF"
}
```


### [2026-09-06T21:03:11.443Z] TOOL RESULT

```
1.    kleu- „horen", vielfach im Sinne von „wovon man                                                                      viel hort, beriihmt,

            Ruhm";           set-Basis             l.ieiij-,           Jclu-    (vgl.    dazu Persson 652 gegen Schulze
            KZ. 27, 427).
     Ai. rrnoti „hort", cntdhi „hore“, Ptc. cruta (— y.hnog, inclutns , ir. cloth                                                                          n.,

ahd. Hlot-, arm. hi) usw.,                                  cracdyati                 ..laSt    horen", crnyate .,wird gehort",
criiti-      „das Horen";
   av. sarunaoiti ,,hort, steht im Rufe, heifit" usw. (s. Keller KZ. 39, 158ff.,
Bartholomae Airan. Wb. 1639f.. wo Formenbestand), Ptc. srfita- „gehort,
beriihmt'', * inti  ,,das zu Gehorbringen, Vortrag"; ai. crotra- n. „01ir\
av. srno&ra- n. „das Singen" (= ags. 1tic odor ahd. hlioilur ), av. sraota- n.                       ,


,,das Horen' (= got. hlhip, vgl. serb. shit Hi), av. snuman- n. „Geh6r“ (: got.
                        -




hlhma), ai. ctomata- n. „guter Ruf-‘ = ahd. hliumuni).                            >




   Arm. lu „kund (= yJ.vrog usw., s. Pedersen KZ. 39, B bS), lur „Kunde,
                                        1-




Geriicht, Nachricht '. Ison, Aor. liuij „hore, horte (Hiibschmann Arm. Gr. I
                                                                                                          1
                                                                                                              '


== leaf
last pdf page tag None
```


## [2026-09-06T21:03:18.282Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^client,\" KLN_1966.txt | head -2; grep -o \"client,  n\\.[^|]\\{0,400\\}\" KLN_1966.txt | head -2; echo \"=== SKT client\"; grep -o \"CLIENT[^.]\\{0,200\\}\\|client,[^.]\\{0,250\\}\" SKT.txt | head -3"
}
```


## [2026-09-06T21:03:19.155Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"listen,  intr[^|]\\{0,350\\}\" KLN_1966.txt | head -2; echo \"---loud\"; grep -o \"loud,  adj[^|]\\{0,350\\}\" KLN_1966.txt | head -2"
}
```


### [2026-09-06T21:03:20.182Z] TOOL RESULT

```
client,  n.  —  F.,  fr.  L.  clientem,  acc.  of  cliens, ‘retainer,  follower,  dependent’,  lit.  ‘one  who leans  on  another’,  fr.  I.-E.  base  *klei-,  ‘to  lean, incline’,  whence  also  L.  -clinare,  ‘to  bend,  turn’. See  clinical  and  cp.  words  there  referred  to.  The usual  derivation  of  L.  cliens  from  the  stem  of cluere,  ‘to  be  named’,  is  erroneous. Derivatives:  client-age, 
=== SKT client
```


### [2026-09-06T21:03:22.057Z] TOOL RESULT

```
listen,  intr.  v.,  to  glitter.  —  ME.  glisnen,  glist- nen,  fr.  OE.  glisnian,  rel.  to  OE.  glisian  and  to OFris.  glisa,  ‘to  shine’,  fr.  I.-E.  base  *ghleis-, enlargement  of  base  *ghel-,  *ghle-,  ‘to  gleam, glimmer’.  See  glass  and  cp.  words  there  referred to.  Cp.  also  next  word.
listen,  intr.  v.  —  ME.  listnen,  a  blend  of  ME.  listen (fr.  OE.  hlystan,  ‘to  hear,  listen’,  fr.  hlyst,  ‘a hearing’),  and  OE.  hlysnan,  ‘to  listen’ .which  is  rel. to  OE.  hlosnian,  ‘to  listen  in  suspense’,  OHG. hlosen,  ‘to  listen’,  *hlusken  (whence  MHG. luschen,  G.  lauschen),  ‘to  listen’  (cp.  also  ON. Must,  ‘hearing;  ea
---loud
loud,  adj.  —  ME.  loud,  fr.  OE.  hlud,  rel.  to  OS., OFris.  hlud,  MDu.  luut,  luud,  Du.  luid,  OHG. hlut,  lut,  MHG.  lut,  G.  luut,  ‘loud’,  fr.  I.-E.  pp. base  *klu-to-s,  whence  also  OI.  srutah,  Gk. xXut6<;,  ‘heard  of,  celebrated’,  L.  in-clutus,  in- clitus,  ‘celebrated,  famous’.  Arm.  lu,  ‘known’,
```


## [2026-09-06T21:03:27.570Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in شنیدن سرود سروش خسرو اسلاو; do echo \"=== $w in ARY\"; grep -n \"$w\" incoming/ARY/ARY_pages.txt | head -3; done"
}
```


### [2026-09-06T21:03:29.411Z] TOOL RESULT

```
=== شنیدن in ARY
1857:معنی این واژه در لاتین و زبان‌های رومانس» یونانی: شنیدن.
10590:جم این واژه در همه‌ی زبان‌های این فهرست به جز پهلزی :و فارسن "و بلوچی :و افقانی: شترایی» شعوره شنیدن)
=== سرود in ARY
1115:(110178۸0078) شعر عشقی يا رزمی می‌سرودند و در بزم‌ها با صدای آهنگین می‌خواندند..
1147:حاوی سرودهای نیایشآمیز بنام «پشت‌هاء (۷۸81778) و وردهایی برای طرد دیوها پنام «ویدیوداده ...۰
2264:چم این واژه در زبان ارمثی: سرود. ۰
=== سروش in ARY
=== خسرو in ARY
7109:۱ ۲ | خسرو
12385:وجود دارد. کاربرد آن توسط شاعران فارسی (طلاً خیام و امیرخسرو) نشان می‌دهد که این واژه از دیریاز در زبان
=== اسلاو in ARY
94:این نوادپرستان حتی «اسلاوهاء که به زبان‌های هند و اروپایی تکلم می‌کنند از نظر «پاکی نژادی»
205:هندی» اسلاوی» بالتیکه) و زبانهای سنتم 4 (ژرمنی» لاتین» یونانی» سلنیک). در زبانهای
235:... زبانی‌های واقع در خاور خود (یعنی بالتیک و اسلاوی) دارند. به عبارت دیگر تربیت جغرافیایی. :
```


## [2026-09-06T21:03:32.011Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10580,10600p' incoming/ARY/ARY_pages.txt; echo \"===7100\"; sed -n '7100,7125p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-06T21:03:32.068Z] TOOL RESULT

```
برتونی (18887000 ۰ :۷007 3 (8186) ,80(6(.133) ۱
رو اه 0/05
: ی 8 (100) ,ا53 18733 با
رد 4 (878ل0 ‎75٩‏ اک ی
را 8 (1.00)
سر برهان قاطع + ۱۱۴۲
یادداشت: ۱ 1 ۹ ۱
۲- واژه‌ی انگلیسی:10170 (آلماتی که 311۷۳ آلمانی 77 هل برنانی 17۳08ن61 لاتین ۲01.378 ملندی
0 فریزی کهن» 9ن13) نیز از قفین راجریشه است: قساً اختمال دار که اژهق قاری" شتیدن" نیز از همین
واجریشه باد (پارسی باستان ۹28713:۸1۷22879 پنهلری 5871001۸06 و 51120۸87308 زا 3300۸0قن
جم این واژه در همه‌ی زبان‌های این فهرست به جز پهلزی :و فارسن "و بلوچی :و افقانی: شترایی» شعوره شنیدن)
گوش؛ گوش کردن و واژه‌های وابسته به فهمیدن پا شنوایی.. .
اوستایی (47587۸4): ۸ لآ58 ایتالیایی للم ۰ ۲۵23۲۵
پهلری (۲متلل۸: 517 ,8838 ر87017 ۰" سررومانی (0ب(مهانم: دزد
بلرچی (246//7): 5885۴ ,ات810 گرتیکد (007[412): 10 :
سانسکریت (84(/3777): ۰" ۰ ایسلندی کهن (۷070:۸010(ی5 صت0):
0۸ ,کف ات0 0
برنانی 08810): زا دا آلمانی کهن 0570/0/0 بلط ضز0): 13703۲
لاتین (77۸ها): اند رت آلمانی (لفال05): 10
فرانسه (۳814): ۰ 0028 انگلیسی کهن (87۵18/0 ۰:02 11080
اسپانیایی (6۸(//320): زان دراه انگلیسی (577لق8۸/0): 100
===7100

‏ایتالیایی (مله7/): لهستانی (۳۵//53[7): ان 4۱ انا زرد

‏51065۸ ,810030 روسی (8/5514/4): 5326014 ,8781636001

‏رومانی (80۸6۸(/4/۷): 9008۸ ,لا801 ۰ صربی (58881۸00): شناد

‏گوتیک (ع/00774)-81۷۸1713۸ ,5۷۷۸11180 اسلرا کی (51.0140): 57016۸ ,5۷01607
[pdf page 241]
۱ ۲ | خسرو
1
لیتوانی ((27۸(/4لا). پسگشت‌ها شک رن درد
5 , ۸8 71ات5 ,0051308 4 و2
گالی (5/لا۸ت): 43 9 نقلق ملق
,077/86۴ 122 6 ی
آلبانی (/۸1۵۸/4۸): درد ۱ درا :۸0۸05 2 ۸/۵0
1 نگاا(اد ه اران
برهان قاطع : ۷۳۸
فرهنگ معین : ۱۳۳۰
اوستایی (۸۷874(۷): 111-5۸۷۸1 ۸آ5
پهلری (۲1هالامم):
,21787۸ ,11108817۷ پسگشت‌ها کت سا
کردی (0018): دنت وود
سانسکریت (54(/58777): 8178178۸۷۸8 5 (-1هت6) ,1037 (تاق)
ارمنی (/۸7۵48140): ابا 3 ‎)۲۸۸۵۲۲٩(‏ +3[ 2 لت مار
بونانی (قق0): 15 4 (۸3کته)) :0/1025
```


## [2026-09-06T21:03:47.417Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"سروش\" \"خشو\" \"سرواد\"; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done; echo \"=== sample سروش\"; grep -o \".\\{80\\}سروش.\\{150\\}\" MON_part1.txt | head -3"
}
```


### [2026-09-06T21:03:49.151Z] TOOL RESULT

```
=== سروش
MON_part2.txt:2
MON_part1.txt:3
=== خشو
MON_part2.txt:19
MON_part1.txt:32
=== سرواد
MON_part2.txt:0
MON_part1.txt:3
=== sample سروش
```


## [2026-09-06T21:03:52.177Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf8',errors='replace').read()\n    for w in ('سروش','سرواد'):\n        for m in re.finditer(w,t):\n            print(f,w,repr(t[max(0,m.start()-200):m.start()+250]))\n            print('---')\nEOF"
}
```


### [2026-09-06T21:03:54.135Z] TOOL RESULT

```
MON_part1.txt سروش 'بهشت ماه خردادماه» تير \nماه» مرداد ماه» شهر یور ماه» مهر ماه» آبان \nماه آذرماه؛ دی ماه» بهمن ماه اسفندارمد \n\n\n(شهر بور)» اسفندارمذ» خرداذ» سرداده \nدی\u200cبآذر آذر» آبان» خور ماه» تبر» گوش» \nدی\u200cبمهر» مهر» سروش» رشن» فروردین» \nبهرام» رام» باد» دی\u200cبدین» دین» ارد» اشتاذ) \nاسمان» زامیاد» مهر اسفند» انبران». \nپارشمن: 0 (ا.) بوست حبوانی» \nمخصوصاً پوست بز و گوسفند که برای \nنوشتن و چاپ پیرایند؛ پوست آهو. \n\nپارک: (.) باغ وسیع پر درخت برای \nگردش. شعار و غبر ه. '
---
MON_part1.txt سروش ' شبه به صدای خروس از \n\n\nگلوی او خارج گردد. \n\nخروس\u200cکولی: آ[۵۳۵۶-0۷ (امر .) (جان.) \nبرنده\u200cای است وحشی مانند خروس. دارای \nچشم\u200cهای درشت و پای\u200cهای دراز و بال\u200cهای \nبزرگ و دم پهن و کاکلی از پر بر سر دارد. \nخسروش: 5 [- اضرش - ضرش» \nخروشیدن] (ا.) بانگ و فریاد. \n\nخروشان: «0۳:(ص\u200cفا. خروشیدن) \nفریادکنان» نالان. \n\nسر وسید ل: 0۳08-1027 (م_سص\u200cل.) \nآخروشید» خروشد» خواهد خروشید» \nبخروش» خروشنده» خروشان» خروشیده] \nبانگ برزدن» فریاد کردن. \n\nخروه: 070*[- خروس] (.) خ'
---
MON_part1.txt سروش 'اغ (صوفیان). \nسروسامان:ز ۹27-00 (امر.) نظم و \nتر تیب» تک اسباب و لوزام زندگی: \nسروستان: -2۲۷: (امر.) جابی که در \nآن درخت سرو سیار باشد. \n\nسر و سر داشتن \nاف. ع.] سر و سر داشتن با کسی: با او رابطه \n9 \n\nسروش: : 50۲8 فرشته» ملک (مطلقاً). روز \nهفدهم از هر ماه شمسی. . (مست.) یکی از \nگوشه\u200cهای ماهور. \n\nسر و صدا؛ (تد..0-202)6602-]5۵ [ف. ع.] \n(امر .) (عم.) داد و فر باد. \n\nسر و صورت: 101721:-2۲-0؟ آف. ع.] (امر.) \n\n\n52]۲-0-56۲)۲(-086)80 \n\n\n۸51 فرهنگک فارسی م'
---
MON_part1.txt سرواد ' کاشی» شجرةه الحیاء. (مس.) \nنوایی است از موسیقی قدیم. \n\nسرو: 01:[- سروی - سرون] (.) شاخ \nجانوران (گاو» گوسفند» گاو میش و غبره). \nبالةٌ شراب. شاخ و میلاٌ درازی که بر روی \nحشرات است (فره.) \n\nسروا: 3 [- سرواد - سرواده] (.) شعر» \nسر ود. \n\nسروا: مه [- سرواز - سرباز] (ص\u200cمر.) \nعمارتی که پیشگاه آن کشاده بود) سرواز. \nسرواد: 0 (- سبرواده] (.) شعر» \nسر ود. \n\nسرواده: (0-)2۲۳۷202: [- سرواد] (ا.) شعر. \nقافیةٌ شعر. \n\nسروال: (۷2 [معر. شلوار] (.) شلوار» \nزیرجامه»'
---
MON_part1.txt سرواد 'جرةه الحیاء. (مس.) \nنوایی است از موسیقی قدیم. \n\nسرو: 01:[- سروی - سرون] (.) شاخ \nجانوران (گاو» گوسفند» گاو میش و غبره). \nبالةٌ شراب. شاخ و میلاٌ درازی که بر روی \nحشرات است (فره.) \n\nسروا: 3 [- سرواد - سرواده] (.) شعر» \nسر ود. \n\nسروا: مه [- سرواز - سرباز] (ص\u200cمر.) \nعمارتی که پیشگاه آن کشاده بود) سرواز. \nسرواد: 0 (- سبرواده] (.) شعر» \nسر ود. \n\nسرواده: (0-)2۲۳۷202: [- سرواد] (ا.) شعر. \nقافیةٌ شعر. \n\nسروال: (۷2 [معر. شلوار] (.) شلوار» \nزیرجامه» ج. سراو'
---
MON_part1.txt سرواد ' گاو میش و غبره). \nبالةٌ شراب. شاخ و میلاٌ درازی که بر روی \nحشرات است (فره.) \n\nسروا: 3 [- سرواد - سرواده] (.) شعر» \nسر ود. \n\nسروا: مه [- سرواز - سرباز] (ص\u200cمر.) \nعمارتی که پیشگاه آن کشاده بود) سرواز. \nسرواد: 0 (- سبرواده] (.) شعر» \nسر ود. \n\nسرواده: (0-)2۲۳۷202: [- سرواد] (ا.) شعر. \nقافیةٌ شعر. \n\nسروال: (۷2 [معر. شلوار] (.) شلوار» \nزیرجامه» ج. سراو یل. \n\nسروال: «2- ده [- ساروان] (امر.) ر ثیس» \n\n\nفرهنگگ فارسی \n\n\n۸۵۵ \n\n\nسرور.(نو) افسر. ارتش بالاتر از'
---
MON_part1.txt سرواد 'اٌ درازی که بر روی \nحشرات است (فره.) \n\nسروا: 3 [- سرواد - سرواده] (.) شعر» \nسر ود. \n\nسروا: مه [- سرواز - سرباز] (ص\u200cمر.) \nعمارتی که پیشگاه آن کشاده بود) سرواز. \nسرواد: 0 (- سبرواده] (.) شعر» \nسر ود. \n\nسرواده: (0-)2۲۳۷202: [- سرواد] (ا.) شعر. \nقافیةٌ شعر. \n\nسروال: (۷2 [معر. شلوار] (.) شلوار» \nزیرجامه» ج. سراو یل. \n\nسروال: «2- ده [- ساروان] (امر.) ر ثیس» \n\n\nفرهنگگ فارسی \n\n\n۸۵۵ \n\n\nسرور.(نو) افسر. ارتش بالاتر از ستوان یم \nو پایین تر از سرگرد؛ سلطان. \n'
---
MON_part1.txt سرواد 'ت است (فره.) \n\nسروا: 3 [- سرواد - سرواده] (.) شعر» \nسر ود. \n\nسروا: مه [- سرواز - سرباز] (ص\u200cمر.) \nعمارتی که پیشگاه آن کشاده بود) سرواز. \nسرواد: 0 (- سبرواده] (.) شعر» \nسر ود. \n\nسرواده: (0-)2۲۳۷202: [- سرواد] (ا.) شعر. \nقافیةٌ شعر. \n\nسروال: (۷2 [معر. شلوار] (.) شلوار» \nزیرجامه» ج. سراو یل. \n\nسروال: «2- ده [- ساروان] (امر.) ر ثیس» \n\n\nفرهنگگ فارسی \n\n\n۸۵۵ \n\n\nسرور.(نو) افسر. ارتش بالاتر از ستوان یم \nو پایین تر از سرگرد؛ سلطان. \n\nسرود. ۳۵ آواز نشاط\u200cانگی'
---
MON_part2.txt سروش 'عبارت ایشان. چون موبد موبدان از \nآفرین بپرداختی؛ پس بزرگان دولت \nدرآمدندی و خدمت\u200cها پیش آوردندی. \nآفرین موبد موبدان به عبارت ایشان: «شها! \nبه جشن فروردین» بماه فروردین» آزادی \nگزین» بروان و دين کیان» سروش آورد ترا \nدانایی و بینایی بکار دانی و دیرزیو با خوی \nهژیر و شادباضش بر تخت زرین و انوشه خور \nبجام جمشید و رسم نیأکان؛ در همت بلند و \n\n\nنوروز \nنیکوکاری و ورزش داد و راستی نگاهدار. \nسرت سبز باد و جوانی چو خوید. اسبت \nکامگار و پیروز و تیفت روشن و ک'
---
MON_part2.txt سروش ' پرستشگاه زردشتیان \nنوده و در آن یاه هوم را سی\u200cکوییده\u200cاند. \n(کذ.) فرج زن. \n\nهاونان: ممه۰2 ).٩(\u200f یکی از هشت متام \nروحانی دین زردشتی از این قرار: زئوتر» \nهاونن» اتروخش» فربر تره آبرت؛ آسناتر \nرشئویشکر» سروشاورز» زئونریا (زوت) \nرئیس این پیشوایان است و در میان دیگر \nهاو بان دارای نخستین بایه است. \nهاون\u200cدسته: (6-)۸5۱۸-.۱ (امر.) اسزاری \nاست از سنگ» چوب با فلز که به وسبلة آن \nچیزی را در هاون کوند. \n\nهاون\u200cکوب: ۰-0 [- همساون کونده] \n\n\n(ص\u200cفا.) آنکه در هاون'
---
```


## [2026-09-06T21:04:01.094Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg270.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/270.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


## [2026-09-06T21:04:01.129Z] TOOL CALL #63: Bash

```json
{
 "command": "sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-06T21:04:01.163Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


### [2026-09-06T21:04:01.195Z] TOOL RESULT

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
```


## [2026-09-06T21:04:03.286Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '60,140p' tools/verify_check.py"
}
```


### [2026-09-06T21:04:03.328Z] TOOL RESULT

```
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


## [2026-09-06T21:04:08.161Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-259.json'))\nprint(list(d.keys())); e=d['entries'][0]; print(list(e.keys()))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:1800])\n\""
}
```


### [2026-09-06T21:04:10.323Z] TOOL RESULT

```
['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes']
{
 "id": 1,
 "lang": "Avestan",
 "words": "zered, zaredaya; zraz-da, sraz-da",
 "verdict": "plausible",
 "derivation": "Avestan zərəd- n. and its -aya- stem zərəδaya- 'heart' are both real: Bartholomae, Altiran. Wb. col. 1692 lists 'g. (j.) zarəd- n. ‘Herz’' and 'j. zərəδaya- n. ‘Herz’', the latter also 'im Sinn von innerstes, Höchstes', quoting Vd. 1.3 zyamahe maiδīm … zərəδaēm 'the middle of winter and the heart of winter' — which is the exact source of Nourai's second gloss 'center' and of Klein's rendering 'middle' (KLN 352). Phonologically the Iranian word does not come from *ḱerd- by regular rule: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, hṛdaya-, PII *ȷ́ʰā́rd > Ir. *zard-), which Buck 251 calls an initial 'as if fr. IE gh, due to a blend with some other word' and Wiktionary marks 'unexplained voiced aspiration'; Pokorny 580 accordingly files it as a 'Reimwort zu ḱer(e)d-', i.e. gherd-, ghr̥d-, 'nur arisch'. The second pair zraz-dā-/sraz-dā- is a different matter: Bartholomae col. 1703 has 'j. zraz-dā- kompV. ‘vertrauen, glauben’' (Gathic adj. zrazdā- 'gläubig', Y.31.1; derivative zrazdāti- 'faith'), so the word and meaning are correct, but Pokorny 580 states expressly that it comes 'aus *srazdā- durch volksetym. Anlehnung an zərəd- ‘Herz’' — the s- form Nourai prints as 'sraz-da' is the reconstructed pre-form, not an attested Avestan variant, and the attachment to 'heart' is secondary folk-etymology on Pokorny's account. Modern work (Watkins, de Vaan 2008 s.v. crēdō, Wiktionary) restores the connection as a genuine PIE compound *ḱred-dʰeh₁- 'to place one's heart', with Ir. *ćrad- + dā-; on that view Nourai's arrow is right but the immediate parent is the oblique *ḱred-, not zərəd-.",
 "derivation_fa": "«زَرِذ» اوستایی zarəd- و ستاک -aya- ی آن zərəδ
```


## [2026-09-06T21:04:14.584Z] TOOL CALL #66: Bash

```json
{
 "command": "tail -40 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    try: d=json.loads(l)\n    except: continue\n    if 'page 270' in (d.get('note') or ''): print(d['url'])\n\""
}
```


### [2026-09-06T21:04:16.233Z] TOOL RESULT

```
https://fa.wikipedia.org/wiki/چکسلواکی
https://www.iranicaonline.org/articles/sraosa/
https://fa.wiktionary.org/wiki/یوگوسلاوی
https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf
https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf
https://lamtakam.com/dictionaries/dehkhoda/320125/سرود
https://abadis.ir/fatofa/سروا/
https://www.avesta.org/avdict/avdict.htm
```


## [2026-09-06T21:04:19.402Z] TOOL CALL #67: Bash

```json
{
 "command": "grep -c . data/verification/sources/web/index.jsonl; python3 -c \"\nimport json\nseen=[]\nfor l in open('data/verification/sources/web/index.jsonl'):\n    try: d=json.loads(l)\n    except: continue\n    if 'page 270' in (d.get('note') or '') or 'Kleu' in (d.get('note') or ''): seen.append(d['url'])\nprint(len(seen))\nfor u in seen: print(u)\n\""
}
```


### [2026-09-06T21:04:21.591Z] TOOL RESULT

```
2931
47
https://en.wiktionary.org/wiki/شنیدن
https://en.wiktionary.org/wiki/خسرو
https://en.wiktionary.org/wiki/خسر
https://en.wiktionary.org/wiki/سرودن
https://en.wiktionary.org/wiki/سروش
https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/slovo
https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/slověninъ
https://www.etymonline.com/word/slave
https://www.etymonline.com/word/Slav
https://www.etymonline.com/word/client
https://www.etymonline.com/word/listen
https://www.etymonline.com/word/loud
https://en.wiktionary.org/wiki/cluo
https://en.wiktionary.org/wiki/clueo
https://en.wiktionary.org/wiki/cliens
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱlew-
https://en.wiktionary.org/wiki/Σκλάβος
https://en.wiktionary.org/wiki/slave
https://en.wiktionary.org/wiki/اسلاو
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hlūdaz
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/swáćuras
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/kšnáwti
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/swéḱuros
https://en.wiktionary.org/wiki/خشو
https://en.wiktionary.org/wiki/شنفتن
https://en.wiktionary.org/wiki/نیوشیدن
https://en.wikipedia.org/wiki/Sraosha
https://en.wiktionary.org/wiki/hlysnan
https://en.wiktionary.org/wiki/sclavus
https://www.etymonline.com/word/*kleu-
https://www.etymonline.com/word/*klei-
https://fa.wikipedia.org/wiki/چکسلواکی
https://www.iranicaonline.org/articles/sraosa/
https://fa.wiktionary.org/wiki/یوگوسلاوی
https://en.wiktionary.org/wiki/%DA%A9%D9%84%DB%8C%D8%AF
https://en.wiktionary.org/wiki/%D8%A5%D9%82%D9%84%D9%8A%D8%AF
https://en.wiktionary.org/wiki/%CE%BA%CE%BB%CE%B5%CE%AF%CF%82
https://www.etymonline.com/word/lot
https://www.etymonline.com/word/close
https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%D8%AA%D9%86
https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D8%B4
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1leh%E2%82%82u-
https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf
https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf
https://lamtakam.com/dictionaries/dehkhoda/320125/سرود
https://abadis.ir/fatofa/سروا/
https://www.avesta.org/avdict/avdict.htm
```


## [2026-09-06T21:04:27.758Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport json,os\nwant={'https://en.wiktionary.org/wiki/خسر','https://en.wiktionary.org/wiki/خشو','https://en.wiktionary.org/wiki/شنیدن'}\nfor l in open('index.jsonl'):\n    try: d=json.loads(l)\n    except: continue\n    if d['url'] in want:\n        p=d.get('file') or d.get('path')\n        print('##',d['url'],p)\n        txt=open(p if os.path.exists(p) else os.path.join('.',os.path.basename(p)),encoding='utf8',errors='replace').read()\n        print(txt[:2500])\n        print('......')\nEOF"
}
```


### [2026-09-06T21:04:29.542Z] TOOL RESULT

```
## https://en.wiktionary.org/wiki/شنیدن data/verification/sources/web/b068ed16c5f59c47.txt
URL: https://en.wiktionary.org/wiki/شنیدن
FETCHED: 2026-09-06T20:57:15Z
STATUS: 200
TITLE: شنیدن - Wiktionary, the free dictionary

شنیدن - Wiktionary, the free dictionary 

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
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Usage notes 

 1.3.2 
 Conjugation 

 1.4 
 References 

 Toggle the table of contents 

 شنیدن 

 12 languages 

 فارسی 
 Na Vosa Vakaviti 
 Français 
 Magyar 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 Bahasa Melayu 
 Polski 
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

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [Term?] ( /⁠âšnūdan⁠/ , “ to hear, understand ” ) , [ 1 ] from Proto-Iranian *ā- + *xšnaw- ( “ to hear; to sharpen the ears ” ) . The prefix is from Proto-Indo-European *h₂éd ( “ at ” ) , while the root is from Proto-Indo-Iranian *kšnaw- , from Proto-Indo-European *ksnew- ( “ to scrape, sharpen ” ) . [ 2 ] Compare Central Kurdish ژنفتن ( žiniftin ) (in Sanandaj ), Zazaki eşnawitiş ( “ to hear ” ) , Northern Luri اشنںفتێ ( ešnəftı ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃu.niː.ˈdan/ , /ʃi.niː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [ʃʊ.niː.d̪án] 

 ( Dari, formal ) IPA ( key ) : [ʃʊ.niː.d̪án] 
 ( Kabuli ) IPA ( key ) : [ʃʊ.niː.d̪án] 

 ( Hazaragi ) IPA ( key ) : [ʃu.ni.d̪án] 

 ( Iran, formal ) IPA ( key ) : [ʃe.niː.d̪ǽn] , [ʃo.niː.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [ʃu.ni.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 šunīdán, šinīdán

 Dari reading ? 

 šunīdan

 Iranian reading ? 

 šenidan, šonidan

 Tajik reading ? 

 šunidan

 Audio ( Iran ) : ( file ) 

 Verb
 [ edit ] 

 شنیدن • ( 
......
## https://en.wiktionary.org/wiki/خسر data/verification/sources/web/5ed240a07851e472.txt
URL: https://en.wiktionary.org/wiki/خسر
FETCHED: 2026-09-06T20:57:16Z
STATUS: 200
TITLE: خسر - Wiktionary, the free dictionary

خسر - Wiktionary, the free dictionary 

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
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Conjugation 

 1.3.2 
 Antonyms 

 1.4 
 Verb 

 1.4.1 
 Conjugation 

 1.5 
 Verb 

 1.5.1 
 Conjugation 

 1.6 
 Noun 

 1.6.1 
 Declension 

 1.7 
 Noun 

 1.7.1 
 Declension 

 1.8 
 Noun 

 1.8.1 
 Declension 

 1.9 
 Noun 

 1.9.1 
 Declension 

 2 
 Egyptian Arabic 

 Toggle Egyptian Arabic subsection 

 2.1 
 Etymology 

 2.2 
 Verb 

 2.2.1 
 Conjugation 

 3 
 Persian 

 Toggle Persian subsection 

 3.1 
 Etymology 

 3.2 
 Pronunciation 

 3.3 
 Noun 

 3.3.1 
 Descendants 

 3.4 
 References 

 4 
 South Levantine Arabic 

 Toggle South Levantine Arabic subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Verb 

 4.3.1 
 Conjugation 

 Toggle the table of contents 

 خسر 

 12 languages 

 العربية 
 فارسی 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Кыргызча 
 Malagasy 
 Polski 
 پښتو 
 Русский 
 Türkçe 
 Walon 

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

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 See also: جسر and حشر 

 Arabic
 [ edit ] 

 Root 

 خ س ر ( ḵ s r ) 

 5 terms 

 Etymology
 [ edit ] 

 Possibly related to Hebrew חסר ( khasér , “ absent, missing ” ) or Egyptian ḫsr ( “ to dispel, to drive away ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /xa.si.ra/ 

 Audio : ( file ) 

 Verb
 [ edit ] 

 خَسِرَ • ( ḵasira ) I ( non-past يَخْسَرُ ( yaḵsaru ) , verbal noun خُسْرَان ( ḵusrān ) or خُسْر ( ḵusr ) or خَسَارَة ( ḵasāra ) or خُسُر ( ḵusur ) or خَسْر ( ḵasr ) or خَسَر ( ḵasar ) or خَسَار ( ḵasār ) ) 

 to lose 

......
## https://en.wiktionary.org/wiki/خشو data/verification/sources/web/057d6767cd8e4dd0.txt
URL: https://en.wiktionary.org/wiki/خشو
FETCHED: 2026-09-06T20:59:21Z
STATUS: 200
TITLE: خشو - Wiktionary, the free dictionary

خشو - Wiktionary, the free dictionary 

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
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.4 
 See also 

 Toggle the table of contents 

 خشو 

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

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Indo-Iranian *swaćrúH , from Proto-Indo-European *sweḱrúh₂ ( “ mother-in-law ” ) . Compare Sanskrit श्वश्रू ( śvaśrū ) .

 Pronunciation
 [ edit ] 

 ( Dari, formal ) IPA ( key ) : [xʊ.ʃuː] 

 ( Dari, formal ) IPA ( key ) : [xʊ.ʃuː] 
 ( Kabuli ) IPA ( key ) : [xʊ.ʃuː] 

 ( Hazaragi ) IPA ( key ) : [xu.ʃu] 

 Readings

 Dari reading ? 

 xušū

 Noun
 [ edit ] 

 خشو • ( xušū ) 

 ( chiefly Dari or uncommon ) mother-in-law 

 See also
 [ edit ] 

 مادرشوهر ( mâdar-šawhar ) 

 مادرزن ( mâdar-zan ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=خشو&oldid=80149037 "

 Categories : Persian terms inherited from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
 Persian lemmas 
 Persian nouns 
 Dari 
 Persian terms with uncommon senses 
 fa:Family 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 6 June 2024, at 11:59.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms o
......
```


## [2026-09-06T21:04:39.394Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport json,os,re\nwant={'https://en.wiktionary.org/wiki/سرودن','https://en.wiktionary.org/wiki/سروش','https://en.wiktionary.org/wiki/خسرو','https://en.wiktionary.org/wiki/خسر','https://en.wiktionary.org/wiki/شنفتن','https://en.wiktionary.org/wiki/نیوشیدن'}\nfor l in open('index.jsonl'):\n    try: d=json.loads(l)\n    except: continue\n    if d['url'] in want:\n        p=d.get('file') or d.get('path')\n        base=os.path.join('/home/sfmqrb/git/rishe',p) if not os.path.exists(p) else p\n        txt=open(base,encoding='utf8',errors='replace').read()\n        print('##',d['url'])\n        # print from first 'Etymology' after 'From Wiktionary'\n        i=txt.find('From Wiktionary, the free dictionary')\n        print(txt[i:i+2200].replace('\\n\\n','\\n'))\n        print('.....................')\nEOF"
}
```


### [2026-09-06T21:04:41.397Z] TOOL RESULT

```
## https://en.wiktionary.org/wiki/خسرو
From Wiktionary, the free dictionary
 Arabic
 [ edit ] 
 Etymology
 [ edit ] 
 Learned borrowing from Classical Persian خُسْرَو ( xusraw ) . Doublet of كِسْرَى ( kisrā ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /xus.raw/ 
 Proper noun
 [ edit ] 
 خُسْرَو • ( ḵusraw )  m 
 a transliteration of a Persian male given name 
 Derived terms
 [ edit ] 
 خُسْرَوِيّ ( ḵusrawiyy ) 
 Chagatai
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian خُسْرَو ( xusraw ) .
 Proper noun
 [ edit ] 
 خسرو • ( xsrw ) 
 a male given name 
 Descendants
 [ edit ] 
 Uzbek: Xusrav 
 Ottoman Turkish
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian خُسْرَو ( xusraw ) .
 Proper noun
 [ edit ] 
 خسرو • ( hüsrev ) 
 a male given name , Khusrev and Hüsrev 
 Descendants
 [ edit ] 
 Turkish: Hüsrev 
 → English: Khusrev 
 → French: Khousrev 
 → German: Chusrew 
 → Russian: Хусрев ( Xusrev ) 
 → Serbo-Croatian: Husrev 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: خسرو 
 Wikipedia fa 
 Etymology
 [ edit ] 
 Inherited from Middle Persian 𐭧𐭥𐭮𐭫𐭥𐭣𐭩 ( hwslwdy /⁠Husrōy⁠/ ) , 𐮰𐮵𐮽𐮹𐮵𐮱𐮵 ( hwslwb' /⁠Husrav⁠/ ) , from Old Median *Husravah , from Proto-Iranian *Hhucráwāh ( “ renowned, famous ” ) , from Proto-Indo-Iranian *Hsućráwās . Cognate with Avestan 𐬵𐬀𐬊𐬯𐬭𐬀𐬎𐬎𐬀𐬢𐬵𐬀 ( haosrauuaŋha , mythical figure ) (from an unattested {{m|ae|*husrauuō}), Ancient Greek εὐκλεής ( eukleḗs ) , Εὐκλῆς ( Euklês ) , Vedic Sanskrit सु॒श्रव॑स् ( suśrávas ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /xus.ˈraw/ 
 ( Dari, formal ) IPA ( key ) : [xʊs.ɾäw] 
 ( Dari, formal ) IPA ( key ) : [xʊs.ɾäw] 
 ( Kabuli ) IPA ( key ) : [xʊs.ɾäw] 
 ( Hazaragi ) IPA ( key ) : [xus.ɾäw] 
 ( Iran, formal ) IPA ( key ) : [xos.ɹow] 
 ( Tajik, formal ) IPA ( key ) : [χus.ɾäw] 
 Rhymes: -aw 
 Readings
 Classical reading ? 
 xusraw
 Dari reading ? 
 xusraw
 Iranian reading ? 
 xosrov
 Tajik reading ? 
 xusrav
 Noun
 [ edit ] 
 خسرو • ( xusraw / xosrov ) ( plural خسروان ( xusrawān / xosrovân ) , or خسروها ( xusraw-hā / xosrov-hâ ) , Tajik spelling хусрав ) 
 (great) king 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nich
.....................
## https://en.wiktionary.org/wiki/خسر
From Wiktionary, the free dictionary
 See also: جسر and حشر 
 Arabic
 [ edit ] 
 Root 
 خ س ر ( ḵ s r ) 
 5 terms 
 Etymology
 [ edit ] 
 Possibly related to Hebrew חסר ( khasér , “ absent, missing ” ) or Egyptian ḫsr ( “ to dispel, to drive away ” ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /xa.si.ra/ 
 Audio : ( file ) 
 Verb
 [ edit ] 
 خَسِرَ • ( ḵasira ) I ( non-past يَخْسَرُ ( yaḵsaru ) , verbal noun خُسْرَان ( ḵusrān ) or خُسْر ( ḵusr ) or خَسَارَة ( ḵasāra ) or خُسُر ( ḵusur ) or خَسْر ( ḵasr ) or خَسَر ( ḵasar ) or خَسَار ( ḵasār ) ) 
 to lose 
 to be deceived , beguiled , cheated , circumvented 
 to err , go astray , deviate from the right way , to become lost 
 to perish , die 
 Conjugation
 [ edit ] 
 Conjugation of خَسِرَ (I, sound, i ~ a, full passive, verbal nouns خُسْرَان , خُسْر , خَسَارَة , خُسُر , خَسْر , خَسَر , خَسَار )
 verbal noun
 الْمَصْدَر 
 خُسْرَان , خُسْر , خَسَارَة , خُسُر , خَسْر , خَسَر , خَسَار 
 ḵusrān , ḵusr , ḵasāra , ḵusur , ḵasr , ḵasar , ḵasār 
 active participle
 اِسْم الْفَاعِل 
 خَاسِر , خَسِر 
 ḵāsir , ḵasir 
 passive participle
 اِسْم الْمَفْعُول 
 مَخْسُور 
 maḵsūr 
 active voice
 الْفِعْل الْمَعْلُوم 
 singular
 الْمُفْرَد 
 dual
 الْمُثَنَّى 
 plural
 الْجَمْع 
 1 st person
 الْمُتَكَلِّم 
 2 nd person
 الْمُخَاطَب 
 3 rd person
 الْغَائِب 
 2 nd person
 الْمُخَاطَب 
 3 rd person
 الْغَائِب 
 1 st person
 الْمُتَكَلِّم 
 2 nd person
 الْمُخَاطَب 
 3 rd person
 الْغَائِب 
 past (perfect) indicative
 الْمَاضِي 
 m
 خَسِرْتُ 
 ḵasirtu 
 خَسِرْتَ 
 ḵasirta 
 خَسِرَ 
 ḵasira 
 خَسِرْتُمَا 
 ḵasirtumā 
 خَسِرَا 
 ḵasirā 
 خَسِرْنَا 
 ḵasirnā 
 خَسِرْتُمْ 
 ḵasirtum 
 خَسِرُوا 
 ḵasirū 
 f
 خَسِرْتِ 
 ḵasirti 
 خَسِرَتْ 
 ḵasirat 
 خَسِرَتَا 
 ḵasiratā 
 خَسِرْتُنَّ 
 ḵasirtunna 
 خَسِرْنَ 
 ḵasirna 
 non-past (imperfect) indicative
 الْمُضَارِع الْمَرْفُوع 
 m
 أَخْسَرُ 
 ʔaḵsaru 
 تَخْسَرُ 
 taḵsaru 
 يَخْسَرُ 
 yaḵsaru 
 تَخْسَرَانِ 
 taḵsarāni 
 يَخْسَرَانِ 
 yaḵsarāni 
 نَخْسَرُ 
 naḵsaru 
 تَخْسَرُونَ 
 taḵsarūna 
 يَخْسَرُونَ 
 yaḵsarūna 
 f
 تَخْسَرِينَ 
 taḵsarīna 
 تَخْسَرُ 
 taḵsaru 
 تَخْسَرَانِ 
 taḵsarāni 
 تَخْسَرْنَ 
 taḵsarna 
 يَخْسَرْنَ
.....................
## https://en.wiktionary.org/wiki/سرودن
From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian slwtn' ( srūdan , “ to sing, recite, play ” ) , from Proto-Iranian *crāwáyati , from Proto-Indo-Iranian *ćrāwáyati , from Proto-Indo-European *ḱlow-éye-ti , causative from *ḱlew- ( “ to hear ” ) . Compare Northern Kurdish stirîn ( “ to sing ” ) , stran ( “ song ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /su.ruː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [sʊ.ɾuː.d̪än] 
 ( Dari, formal ) IPA ( key ) : [sʊ.ɾuː.d̪än] 
 ( Kabuli ) IPA ( key ) : [sʊ.ɾuː.d̪än] 
 ( Hazaragi ) IPA ( key ) : [su.ɾu.d̪än] 
 ( Iran, formal ) IPA ( key ) : [so.ɹuː.d̪æn] 
 ( Tajik, formal ) IPA ( key ) : [su.ɾu.d̪än] 
 Rhymes: -an 
 Readings
 Classical reading ? 
 surūdan
 Dari reading ? 
 surūdan
 Iranian reading ? 
 sorudan
 Tajik reading ? 
 surudan
 Verb
 [ edit ] 
 سُرودَن • ( sorudan ) ( present stem سرای ( sorây, sarây ) ) 
 to sing , chant 
 to recite 
 to compose 
 Conjugation
 [ edit ] 
 This verb needs an inflection-table template .
 Derived terms
 [ edit ] 
 سرود ( sorud ) 
 سرود ملی ( sorud-e melli ) 
 سروده ( sorude ) 
 See also
 [ edit ] 
 خواندن ( xândan ) 
 سراییدن ( sorâyidan ) 
 References
 [ edit ] 
 MacKenzie, D. N. ( 1971 ), “srūdan”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=سرودن&oldid=81657571 "
 Categories : Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms inherited from Proto-Iranian 
 Persian terms derived from Proto-Iranian 
 Persian terms inherited from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Indo-European 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/an 
 Rhymes:Persian/an/3 syllables 
 Persian lemmas 
 Persian verbs 
 Hidden categories: Pages with entries 
 Pages with 1 entry 
 Requests for inflections in Persian verb entries 
 Requests for inflections in Persian entries 
 This page was last edited on 18 September 2024, at 2
.....................
## https://en.wiktionary.org/wiki/سروش
From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Inherited from Middle Persian slwš ( /⁠Srōš⁠/ ) , from Avestan 𐬯𐬀𐬭𐬊𐬱𐬀 ( sraoša , “ Sraosha ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /su.ˈroːʃ/ 
 ( Dari, formal ) IPA ( key ) : [sʊ.ɾóːʃ] 
 ( Dari, formal ) IPA ( key ) : [sʊ.ɾóːʃ] 
 ( Kabuli ) IPA ( key ) : [sʊ.ɾóːʃ] 
 ( Hazaragi ) IPA ( key ) : [su.ɾʊ́ːʃ] 
 ( Iran, formal ) IPA ( key ) : [so.ɹúːʃ] 
 ( Tajik, formal ) IPA ( key ) : [su.ɾɵ́ʃ] 
 Rhymes: -oːʃ 
 Readings
 Classical reading ? 
 surōš
 Dari reading ? 
 surōš
 Iranian reading ? 
 soruš
 Tajik reading ? 
 surüš
 Proper noun
 [ edit ] 
 سروش • ( surōš  / soruš ) ( Tajik spelling Сурӯш ) 
 ( Islam , poetry ) A messenger angel who brings good news from God , an Islamization of the Zoroastrian figure; often considered a Persian name or title of the archangel Gabriel . 
 ( Zoroastrianism , Iranian mythology ) Sraosha , yazata of conscience 
 a male given name , Soroosh 
 Derived terms
 [ edit ] 
 سروشی ( soruši , “ angelic ” ) 
 Descendants
 [ edit ] 
 → Azerbaijani: süruş 
 → Udi: соруш ( soruš ) 
 → Urdu: سروش ( saroš ) 
 Urdu
 [ edit ] 
 سروش 
 Etymology
 [ edit ] 
 From Classical Persian سروش ( surōš ) . 
 Pronunciation
 [ edit ] 
 ( Standard Urdu ) IPA ( key ) : /sə.ɾoːʃ/ 
 Rhymes: -oːʃ 
 Hyphenation: سَ‧روش 
 Noun
 [ edit ] 
 سَروش • ( saroś )  m ( Hindi spelling सरोश ) 
 ( Islam ) Gabriel , the archangel of revelation .
 a heavenly voice which comes from the divine , an unseen voice from Heaven ; the voice of an angel .
 ( by extension ) intuition .
 ( figurative ) good news .
 Derived terms
 [ edit ] 
 نَوائے سَروش ( navā-e-saroś , “ angelic voice ” ) 
 سَروشِ غَیب ( saroś-e-ğaib ) 
 References
 [ edit ] 
 “ سروش ”, in اُردُو لُغَت ( urdū luġat ) (in Urdu), Ministry of Education: Government of Pakistan, 2017 .
 Qureshi, Bashir Ahmad ( 1971 ), “ سروش ”, in Kitabistan's 20th Century Standard Dictionary , Lahore: Kitabistan Pub. Co. 
 Platts, John T. ( 1884 ), “ سروش ”, in A dictionary of Urdu, classical Hindi, and English , London: W. H. Allen & Co. 
 “ سروش ”, in ریخْتَہ لُغَت ( rexta luġat ) - R
.....................
## https://en.wiktionary.org/wiki/شنفتن
From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Inherited from Middle Persian . See شنیدن ( šinīdan  / šenidan ) for more.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʃi.nuf.ˈtan/ 
 ( Dari, formal ) IPA ( key ) : [ʃɪ.nʊf.t̪ʰán] 
 ( Dari, formal ) IPA ( key ) : [ʃɪ.nʊf.t̪ʰán] 
 ( Kabuli ) IPA ( key ) : [ʃɪ.nʊf.t̪ʰán] 
 ( Hazaragi ) IPA ( key ) : [ʃu.nuf.t̪ʰán] 
 ( Iran, formal ) IPA ( key ) : [ʃe.nof.t̪ʰǽn] 
 ( Tajik, formal ) IPA ( key ) : [ʃi.nuf.t̪ʰán] 
 Rhymes: -an 
 Readings
 Classical reading ? 
 šinuftan
 Dari reading ? 
 šinuftan
 Iranian reading ? 
 šenoftan
 Tajik reading ? 
 šinuftan
 Verb
 [ edit ] 
 شِنُفتَن • ( šinuftan / šenoftan ) ( present stem شنو ( šunaw, šinaw / šonov, šenov ) , Tajik spelling шинуфтан ) 
 to hear 
 to listen 
 Synonyms: گوش کردن ( gōš kardan  / guš kardan ) , گوش دادن ( gōš dādan  / guš dâdan ) , نیوشیدن ( niyōšīdan  / niyušidan ) 
 Usage notes
 [ edit ] 
 See usage notes under شنیدن ( šinīdan  / šenidan ) .
 Conjugation
 [ edit ] 
 Conjugation of شنفتن ( literary Iranian Persian )
 infinitive
 شنفتن ( šenoftán ) 
 stem
 present
 شنو ( šenow, šonow ) 
 past
 شنفت ( šenoft ) 
 participle
 present
 شنونده ( šenow, šonowandé ) 
 past
 شنفته ( šenofté ) 
 singular
 plural
 1 st person
 2 nd person
 3 rd person
 1 st person
 2 nd person
 3 rd person
 indicative
 aorist
 شنوم ( šenow, šonowam ) 
 شنوی ( šenow, šonowi ) 
 شنود ( šenow, šonowad ) 
 شنویم ( šenow, šonowim ) 
 شنوید ( šenow, šonowid ) 
 شنوند ( šenow, šonowand ) 
 present (imperfect)
 می‌شنوم ( mí-šenow, šonowam ) 
 می‌شنوی ( mí-šenow, šonowi ) 
 می‌شنود ( mí-šenow, šonowad ) 
 می‌شنویم ( mí-šenow, šonowim ) 
 می‌شنوید ( mí-šenow, šonowid ) 
 می‌شنوند ( mí-šenow, šonowand ) 
 present progressive
 دارم می‌شنوم ( dấram mí-šenow, šonowam ) 
 داری می‌شنوی ( dấri mí-šenow, šonowi ) 
 دارد می‌شنود ( dấrad mí-šenow, šonowad ) 
 داریم می‌شنویم ( dấrim mí-šenow, šonowim ) 
 دارید می‌شنوید ( dấrid mí-šenow, šonowid ) 
 دارند می‌شنوند ( dấrand mí-šenow, šonowand ) 
 present perfect
 شنفته‌ام ( šenofté-am ) 
 شنفته‌ای ( šenofté-i ) 
 شنفته است ( šenofté ast
.....................
## https://en.wiktionary.org/wiki/نیوشیدن
From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian ndwhšytn' ( niyō(x)šidan ) , from Proto-Iranian *ni- + *gáwšati , from Proto-Indo-Iranian *gʰáwšati . Compare Baluchi نگوشگ ( negóšag ) , Sanskrit घोषति ( ghoṣati ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ni.joː.ʃiː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Dari, formal ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Kabuli ) IPA ( key ) : [ni.joː.ʃiː.d̪án] 
 ( Hazaragi ) IPA ( key ) : [ni.ju.ʃi.d̪án] 
 ( Iran, formal ) IPA ( key ) : [ni.juː.ʃiː.d̪ǽn] 
 ( Tajik, formal ) IPA ( key ) : [ni.ju.ʃi.d̪än] 
 Rhymes: -an 
 Readings
 Classical reading ? 
 niyōšīdan
 Dari reading ? 
 niyōšīdan
 Iranian reading ? 
 niyušidan
 Tajik reading ? 
 niyušidan
 Verb
 [ edit ] 
 نیوشیدن • ( niyōšīdan  / niyušidan ) ( Tajik spelling ниюшидан ) 
 ( archaic or literary ) to listen ; to accept 
 Synonyms: گوش دادن ( gōš dādan  / guš dâdan ) , گوش کردن ( gōš kardan  / guš kardan ) 
 c. 1390 , Shams-ud-Dīn Muḥammad Ḥāfiẓ , “Ghazal 162”, in دیوان حافظ [ The Divān of Ḥāfiẓ ]‎ [1] : ز من بنیوش و دل در شاهدی بند
که حسنش بستهٔ زیور نباشد zi man biniyōš u dil dar šāhidē band
ki husn-aš basta-yi zēwar na-bāšad Listen to me and bind your heart to a beautiful person
Whose beauty is not bound to adornments. (Classical Persian transliteration) 
 ( obsolete ) to overhear 
 Conjugation
 [ edit ] 
 Conjugation of نیوشیدن ( literary Iranian Persian )
 infinitive
 نیوشیدن ( niyôšîdán ) 
 stem
 present
 نیوش ( niyôš ) 
 past
 نیوشید ( niyôšîd ) 
 participle
 present
 نیوشنده ( niyôšandé ) 
 past
 نیوشیده ( niyôšîdé ) 
 singular
 plural
 1 st person
 2 nd person
 3 rd person
 1 st person
 2 nd person
 3 rd person
 indicative
 aorist
 نیوشم ( niyôšam ) 
 نیوشی ( niyôši ) 
 نیوشد ( niyôšad ) 
 نیوشیم ( niyôšim ) 
 نیوشید ( niyôšid ) 
 نیوشند ( niyôšand ) 
 present (imperfect)
 می‌نیوشم ( mí-niyôšam ) 
 می‌نیوشی ( mí-niyôši ) 
 می‌نیوشد ( mí-niyôšad ) 
 می‌نیوشیم ( mí-niyôšim ) 
 می‌نیوشید ( mí-niyôšid ) 
 می‌نیوشند ( mí-niyôšand ) 
 present progressive
 دارم می‌نیوشم ( dấram mí-niyôšam ) 
 داری می‌نیوشی ( dấri
.....................
```


## [2026-09-06T21:04:49.373Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('5ed240a07851e472.txt',encoding='utf8',errors='replace').read()\ni=t.find('Persian\\n [ edit ]',t.find('Egyptian Arabic\\n [ edit ]'))\nprint(t[i:i+1600])\nEOF"
}
```


### [2026-09-06T21:04:51.762Z] TOOL RESULT

```
Persian
 [ edit ] 

 Etymology
 [ edit ] 

 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xu.ˈsur/ 

 ( Dari, formal ) IPA ( key ) : [xʊ.sʊɾ] 

 ( Dari, formal ) IPA ( key ) : [xʊ.sʊɾ] 
 ( Kabuli ) IPA ( key ) : [xʊ.sʊɾ] 

 ( Hazaragi ) IPA ( key ) : [xu.suɾ] 

 ( Iran, formal ) IPA ( key ) : [xo.soɹ] 

 ( Tajik, formal ) IPA ( key ) : [χu.suɾ] 

 Rhymes: -ur 

 Readings

 Classical reading ? 

 xusur

 Dari reading ? 

 xusur

 Iranian reading ? 

 xosor

 Tajik reading ? 

 xusur

 Noun
 [ edit ] 

 خسر • ( xusur / xosor ) ( Tajik spelling хусур ) 

 father-in-law 

 Descendants
 [ edit ] 

 Judeo-Tat: xysyr 

 References
 [ edit ] 

 Hayyim, Sulayman ( 1934 ), “ خسر ”, in New Persian–English dictionary , volume 1, Teheran: Librairie-imprimerie Béroukhim, page 717 

 Steingass, Francis Joseph ( 1892 ), “ خسر ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul, page 460 

 South Levantine Arabic
 [ edit ] 

 Root 

 خ س ر 

 1 term 

 Etymology
 [ edit ] 

 Inherited from Arabic خَسِرَ ( ḵasira ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /xi.sir/ , [ˈχisɪr] 

 Audio ( al-Lidd ) : ( file ) 

 Verb
 [ edit ] 

 خسر • ( ḵisir ) I ( present بخسر ( biḵsar ) ) 

 to lose 
 خسرو كل شي في القمار . ― ḵisru kull ši fi li-ʔmār. ― They lost everything gambling. 

 Conjugation
 [ edit ] 

 Conjugation of خسر 

 singular

 plural

 1 st person

 2 nd person

 3 rd person

 1 st person

 2 nd person

 3 rd pe
```


## [2026-09-06T21:05:30.667Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/extracted/batch/page-2[5-6]*.json')):\n    d=json.load(open(f))\n    pg=d['pdf_page']\n    for ei,e in enumerate(d['entries']):\n        for n in e['nodes']:\n            if not n['words'] and not n.get('script_extra'):\n                try: v=json.load(open(f'data/verification/page-{pg}.json'))\n                except: continue\n                for ve in v['entries']:\n                    if ve['entry']==ei:\n                        for vn in ve['nodes']:\n                            if vn['id']==n['id']:\n                                print(pg,n['id'],n['lang'],vn['verdict'],'|',vn['derivation'][:200])\nEOF"
}
```


### [2026-09-06T21:05:32.918Z] TOOL RESULT

```
252 2 Syriac disputed | The empty Syriac box stands for Classical Syriac ܟܣܐ kāsā 'cup', the word both of Nourai's references name at this point (Addi Shir s.v. كأس: 'وهو بالفارسية كاسه وبالآرامية ܟܣܐ وبالبابلية kāsu'; Jeffe
256 2 Pahlavi confirmed | The empty pass-through box stands for Middle Persian sar 'head', written with the Aramaic ideogram LOYŠE (< Aram. rēšā) and phonetically sl. Avestan/Old Iranian sarah- lost its s-stem ending in Middle
256 9 Middle Latin confirmed | The empty box stands for Medieval Latin carratus (also caratus), the form in which Arabic qīrāṭ entered western Europe — through the alchemical and assaying literature translated from Arabic in Spain 
256 10 French confirmed | The empty box stands for French carat, attested from the 14th century, taken from Italian carato (the Italian goldsmiths and bankers of Genoa, Venice and Florence being the intermediaries) rather than
256 18 Different Languages confirmed | A collector box: Nourai uses 'Different Languages' for the several branches through which the root reached English independently of the Greek and Iranian lines drawn above — Germanic (*hurnaz > OE hor
258 6 French confirmed | An empty pass-through box: the French link between Latin carbō and Persian کربن is carbone, the element name coined by Lavoisier's commission in 1787 (Méthode de nomenclature chimique) on Latin carbōn
258 12 French confirmed | Another empty pass-through box, and the only node on the page with no reference at all. The intended French link is céramique, attested from 1806 as an adjective and from the 1830s-40s as a noun for t
259 7 French confirmed | An empty pass-through box: the French stage through which the Latin cor-family reached English and (later) Persian. The relevant Old/Modern French forms are acorder 'agree, be in harmony' (12c., < Vul
262 4 Hindustani disputed | An empty pass-through box: Nourai means Hindustani (Urdu) but-kada(h) «بت‌کدہ» 'idol-temple', the unchanged Persian compound but 'idol' + -kada 'house of' taken over into Indo-Muslim usage. The word i
262 5 Portuguese disputed | The unnamed word is Portuguese pagode, first recorded in Duarte Barbosa's book of 1516 ('chamam a seus templos pagodes') and in the sense 'temple' from 1525; it is the immediate source of every Europe
263 8 None unverified | An empty box in the printed chart: the rectangle to the right of the Avestan čevîšî node carries no language label, no word and no reference (confirmed on the page image, site/pages/263.jpg). Nourai's
263 10 None unverified | A second empty box in the printed chart, drawn to the right of the mislabelled 'Old Persian' node and carrying no language, word or reference (checked on the page image). As with node 8 the box was ne
264 5 None unverified | Empty pass-through box: on the printed page (site/pages/264.jpg) an arrow runs from the 'Old Persian caune' box to a blank framed box at the right margin with no language label, no reference and no wo
```


## [2026-09-06T21:05:36.332Z] AGENT

Now I'll write the verification file.


## [2026-09-06T21:16:54.014Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build270.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Kleu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱleu- / *ḱlew- 'to hear' (Pokorny 1. ḱleu-, ḱleuǝ-, ḱlu-, pp. 605-607; Walde-Pokorny I 494 f.; Watkins/AHD kleu-1)\",\n \"note\": (\"Pokorny's entry 'Root/lemma: ḱleu-1, ḱleuǝ-, ḱlu-, Meaning: to hear, cry' occupies pp. 605-607, exactly Nourai's POK:605, and its material is the same set Nourai draws on: \"\n   \"Skt. śṛṇóti 'hears', śruta- 'heard, famous', Av. surunaoiti 'hört', srūta-, srūti-, sraoθra-, sraota-, sraoman-, Gk. klúō / kléos, Lat. clueō 'to be spoken of', \"\n   \"OIr. cloth 'fame', OE hlūd 'loud', hlysnan 'listen', OCS slovo 'word', slava 'fame', Lith. klausýti. \"\n   \"The language label 'Indo-European' and the gloss 'to hear' are both right; the modern reconstruction adds the palatal (*ḱ-, whence Indo-Iranian ś-/s-, Slavic s-, Gmc h-, Lat./Gk. k-) and separates two extensions, \"\n   \"the es-stem *ḱléwos 'fame' (Skt. śrávas-, Av. sravah-, Gk. kléos, OCS slovo) and the s-extension *ḱleus- (Av. sraoša-, OE hlyst, Lith. klausýti), both of which Nourai's chart uses. \"\n   \"Only one caveat matters for the page: Pokorny keeps *ḱleu- 'to hear' strictly apart from *ksneu- 'to sharpen' (POK 585), and the Persian verb شنیدن on this chart belongs to the latter (see nodes 1-3), \"\n   \"while Latin cliēns / English client belongs to *ḱlei- 'to lean' (see node 23).\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *ḱleu- «شنیدن» ریشه‌ای است پذیرفته و بی‌مناقشه؛ پوکورنی آن را در صفحات ۶۰۵ تا ۶۰۷ فرهنگ خود آورده و همان مواد نورایی را گرد کرده است: \"\n   \"سنسکریت śṛṇóti «می‌شنود» و śruta- «شنیده، نامور»، اوستایی surunaoiti و srūta- و sraoša-، یونانی klúō و kléos «آوازه»، لاتین clueō «نامیده شدن»، انگلیسی کهن hlūd «بلند» و اسلاوی کهن slovo «واژه». \"\n   \"برچسب زبانی «هندواروپایی» و معنای «شنیدن» هر دو درست است؛ ریشه‌شناسی امروزی تنها همخوان نخستین را کامی (*ḱ) بازسازی می‌کند و دو ستاک فرعیِ *ḱléwos «آوازه» و *ḱleus- را از هم جدا می‌شمارد که هر دو در همین نمودار به کار رفته‌اند. \"\n   \"دو نکتهٔ هشداردهنده: پوکورنی ریشهٔ *ksneu- «تیز کردن» (ص ۵۸۵) را از این ریشه جدا نگه می‌دارد و «شنیدن» فارسی از آن دومی است؛ و «client» انگلیسی به ریشهٔ *ḱlei- «خم شدن» می‌رسد نه به این ریشه.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/ḱlew-\", \"https://www.etymonline.com/word/*kleu-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:605\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt lines 51416-51560: 'Root/lemma: ḱleu-1, ḱleuǝ-, ḱlu- | Meaning: to hear, cry ... Page(s): 605-607'. Material includes 'Avestan surunaoiti (*ḱlu-n-) hört, steht im Rufe, heißt ... participle sruta- heard, famous', 'Avestan sravah- n. Wort', 'Avestan sraoša- ear, hearing', 'Latin clueō, -ēre to hear, be spoken of', 'Old Church Slavic slovo word', 'Old English hlyst ear, hearing, Old Icelandic hlusta, Old English hlysnan (engl. listen)', 'Old High German hlūt, Old English hlūd ... Modern High German laut'. Every branch Nourai draws is present on this page.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 494 f. (WLD_Bd1_pages.txt l. 46665)\", \"stance\": \"supports\",\n    \"note\": \"'1. ḱleu- „hören\\\", vielfach im Sinne von „wovon man viel hört, berühmt, Ruhm\\\"; set-Basis ḱleuǝ-, ḱlu-' — with 'av. surunaoiti', 'av. srōθra- n. „das Singen\\\"', 'ai. śrotra- n. „Ohr\\\"'. This is the page Pokorny cites as 'WP. I 494 f.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kleu-1\", \"stance\": \"supports\",\n    \"note\": \"'kleu-1, To hear. I. Extended form *kleus- in Germanic *hleuza- ... II. Zero-grade form *klu-. 1. Germanic *hlustjan ... 2. Germanic *hlusinōn in Old English hlysnan, to listen: LISTEN. 3. Suffixed lengthened form *klū-to- in Germanic *hlūdaz, \\\"heard,\\\" loud ... [Pok. 1. ḱleu- 605.]' — the same page reference Nourai gives.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 15.41 'Hear' and 4.22 'Ear'\", \"stance\": \"supports\",\n    \"note\": \"'fr. IE *ḱleu-s-, beside *ḱleu- in Skt. śru-, Grk. klúō \\\"hear\\\", etc., from which root also Skt. śrotra- \\\"hearing, ear\\\", Toch. A klots, B klautso \\\"ear\\\" ... Walde-P. 1.494 f.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. s.v. Kleustis\", \"stance\": \"supports\",\n    \"note\": \"'... WP I, 494. Cf. Kleu-, kleu-, Klutos, etc. Skt. śruṣṭiḥ f. \\\"obedience\\\"; Av. srušti- f. \\\"hearing\\\"; ... OE hlyst f. \\\"sense of hearing\\\" ... ON hlust f. \\\"ear\\\"'.\"}],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"sru 2, srav, xšnu, xšnaw\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Two of the four forms belong here and two do not. (a) Avestan √srav-/sru- 'to hear' is genuine and is the direct Iranian continuation of *ḱleu-: Bartholomae, Altiran. Wb. col. 1633 ff. gives the paradigm \"\n   \"(pres. nu-stem surunaoiti 'hört' < *ḱlu-neu-, aor. sraotū 'höre!', perf. pass. ptc. srūta- 'gehört'), and Cheung 2007 (Etym. Dict. of the Iranian Verb, s.v. *srau, p. 357) lemmatises Av. srao- 'to hear, listen' with \"\n   \"'PIE *ḱleu- \\\"to hear\\\" = LIV 334 f. | Pok. 605 f.' and the remark 'This root has an impeccable IE etymology.' Nourai's 'sru 2' is his own homonym numbering (sru 1 elsewhere = 'horn', Av. srū-). \"\n   \"(b) Avestan xšnu-/xšnav-, however, is a different verb of a different root. Bartholomae 557-559 glosses it 'befriedigen, zufrieden sein' and Cheung splits it into two lemmas — *xšnau1 'to hear (< to sharpen the ears)', \"\n   \"with Old Persian ā-xšnau- 'to hear' (Kent 182: āxšnaviy, āxšnudiy DNb 29, 54) and MP/Parthian ʾšnw-, and *xšnau2 'to entertain, welcome (a guest)' — and refers both to Skt. kṣṇav 'to whet, sharpen', \"\n   \"'PIE *ksneu- \\\"to sharpen\\\" = LIV 373 | Pok. 585'. Pokorny keeps 585 (ksneu-) and 605 (ḱleu-) rigorously apart, and Hübschmann (Pers. Stud. 82) says of the two in so many words that a root xšnū 'sich nicht mit zd. sru \"\n   \"vereinigen lassen würde'. So the arrow root -> xšnu/xšnaw is wrong: those forms hang from *ksneu-, not from *ḱleu-. Nourai has put them here because he needed a source for the š- of شنیدن (nodes 2-3).\"),\n \"derivation_fa\": (\"از چهار صورتی که نورایی در این جعبه آورده، دو تا به این ریشه می‌رسند و دو تا نه. الف) ریشهٔ اوستایی srav-/sru- «شنیدن» بازماندهٔ راستین *ḱleu- است؛ بارتولمه (فرهنگ ایرانی باستان، ستون ۱۶۳۳ به بعد) صورت‌های \"\n   \"surunaoiti «می‌شنود» (از *ḱlu-neu-)، sraotū «بشنو» و اسم مفعول srūta- «شنیده» را می‌آورد و چونگ (۲۰۰۷، ذیل *srau) می‌نویسد که «این ریشه ریشه‌شناسی هندواروپایی بی‌عیبی دارد» و آن را به *ḱleu- (پوکورنی ۶۰۵) بازمی‌گرداند. \"\n   \"ب) ولی xšnu-/xšnav- اوستایی فعلی جداگانه از ریشه‌ای دیگر است: چونگ آن را ذیل *xšnau «شنیدن (< تیز کردن گوش)» و *xšnau «پذیرایی کردن» آورده و هر دو را به *ksneu- «تیز کردن» (پوکورنی ۵۸۵) می‌رساند؛ \"\n   \"هوبشمان نیز (پژوهش‌های فارسی، ص ۸۲) صریحاً می‌گوید ریشهٔ xšnū «با sru اوستایی سازگار نمی‌افتد». پس پیوند ریشه به xšnu/xšnaw نادرست است و نورایی تنها برای توجیه «ش» آغازیِ «شنیدن» آن را اینجا نشانده است.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-Iranian/kšnáwti\", W + \"Reconstruction:Proto-Indo-European/ḱlew-\",\n             \"https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:177\", \"status\": \"partial\",\n    \"note\": \"Horn, Grundriss p.177 (HRN.txt leaf 198), no. 795: 'šunūden, šenīden \\\"hören\\\", Praes. šunev-em, šinev-em ... aw. √srav-, surunaoiti \\\"hören\\\"; phlv. vergl. āšnūtan, ašnuvēt \\\"hören\\\" ... ai. √śrav-, śṛṇóti \\\"hören\\\".' \"\n    \"Horn therefore does support srav- (and only srav-) as the etymon; he cites no xšnu-, and he adds a warning: 'Bartholomae, Studien II, 43 erklärt das np. š durch Übertragung; Fr. Müller, WZKM. IV, 355, ist wenig überzeugend.'\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1633-1639 (srav-, sraota-, srūta-); col. 557-559 (xšnav-)\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt has 'srav : sraota-' at AiWb. 1633 and 'sraoša-' at 1634 (both quoted in SNS's Avestan index); the xšnav- entries are glossed 'befriedigen, zufrieden sein', not 'hören' — i.e. Bartholomae does not put xšnu- with sru-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *srau p. 357 and *xšnau1/2 p. 456-457\", \"stance\": \"contradicts\",\n    \"note\": \"CHEUNG.txt l. 23313 '*srau \\\"to hear, listen\\\" ... «PIE *ḱleu- \\\"to hear\\\" = LIV: 334 f. | Pok.: 605 f.»'; l. 29477 '*xšnau1 \\\"to hear (< \\\"to sharpen (the ears)\\\")\\\" ... OLD PERSIAN: (+ *ā-) ā-xšn(a)u- \\\"to hear\\\" ... SANSKRIT: kṣṇav \\\"to whet, sharpen\\\" ... «PIE *ksneu- \\\"to sharpen\\\" = LIV: 373 | Pok.: 585»'. Two separate roots.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 82 (note to Horn 795)\", \"stance\": \"contradicts\",\n    \"note\": \"'Den Lautgesetzen nach wäre np. šunū-dan, pr. šinavam ... phl. ptc. āšnūt, pr. 3. sg. āšnavēt ... auf ein ap. *xšnavamiy, inf. *xšnutanaiy von einer Wrzl. xšnū zurückzuführen, die sich nicht mit zd. sru vereinigen lassen würde.'\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p. 182 s.v. xšnu-\", \"stance\": \"supports\",\n    \"note\": \"Kent lemmatises OP ā-xšnav- 'hear' (āxšnaviy DNb 29, āxšnudiy DNb 54) — the form Cheung and Mo'in both make the ancestor of شنودن; it is an xšn-, not an sr-, verb.\"}]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"ašnŭdan\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The Middle Persian verb is real: MacKenzie's Concise Pahlavi Dictionary lemmatises ašnūdan, ašnaw- 'hear' (Book Pahlavi ʾšnwtn', pres. ʾšnw-), and the Manichaean and Parthian evidence is identical \"\n   \"(MMP/Pth. ʾšnw- /āšnaw-/ 'to hear, hearken', inf. ʾšnwdn, ptc. ʾšnwd; Cheung 2007 s.v. *xšnau1). Its ancestry, however, is not the one drawn. The regular Middle Persian outcome of Old Iranian *xš- word-initially is š-, \"\n   \"and the ʾ- is the old preverb *ā- (or a prothetic vowel), so āšnaw- < OP ā-xšnau- 'to hear' < Proto-Iranian *ā-xšnau- < PII *kšnaw- < PIE *ksneu- 'to scrape, sharpen' (semantically 'to sharpen the ears'). \"\n   \"If the verb came from *ḱleu- one would expect *(a)srav-/*surūdan: that is precisely the Middle Persian outcome that does exist, MP srūdan, srāy- 'to sing, recite' (node 5). Horn himself only compared phl. āšnūtan with Av. srav- \"\n   \"'vergleiche' and left the š- unexplained; Hübschmann (Pers. Stud. 82) and Mo'in (Borhan-e Qāṭe' p.1303 fn.) both refer āšnūdan to OP ā-xšnavamiy instead.\"),\n \"derivation_fa\": (\"خودِ فعل فارسی میانه درست است: مکنزی در «فرهنگ کوچک پهلوی» ašnūdan / ašnaw- «شنیدن» را آورده و صورت‌های مانوی و پارتی نیز ʾšnw- است. ولی تبار آن آن‌گونه که نمودار نشان می‌دهد نیست. \"\n   \"در فارسی میانه xš- ایرانی باستان در آغاز واژه به š بدل می‌شود و ʾ- آغازین همان پیشوند فعلی *ā- (یا واکهٔ افزوده) است؛ پس āšnaw- از پارسی باستان ā-xšnau- «شنیدن» می‌آید و آن از ایرانی آغازین *ā-xšnau- و سرانجام از \"\n   \"*ksneu- هندواروپایی «تیز کردن (گوش)». اگر این فعل از *ḱleu- می‌آمد باید در فارسی میانه srav-/srūdan می‌شد — و همان صورت هم جداگانه وجود دارد (سرودن). هوبشمان و معین (حاشیهٔ برهان قاطع، ص ۱۳۰۳) هر دو آن را از āxšnavamiy پارسی باستان می‌گیرند.\"),\n \"sources\": [W + \"شنیدن\", W + \"Reconstruction:Proto-Indo-Iranian/kšnáwti\",\n             \"https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:64\", \"status\": \"contradicts\",\n    \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Darī, entry «شنودن» (FFD_pages.txt pdf p.69; the book's own root index on p.93 refers šnav to p.64): «شنود ← فارسی میانه (a)šnūd ← ایرانی باستان *šnu-ta ... šnu صورت ضعیف ریشهٔ šnav است، به معنی «شنودن». «شنید» و «شنفت» صورتهای دیگر «شنود» هستند» and «شنو ← فارسی میانه šnav ← ایرانی باستان *šnav-a». Abolghasemi reconstructs an Old Iranian root šnav / šnu, NOT srav — so the page Nourai cites gives a different parent from the one his arrow draws.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, s.v. ašnūdan (PHD.txt index l. 5118 'ašnawišn / ašnūdan')\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie lemmatises 'ašnūdan, ašnaw- hear' and, on the same page-range, 'srūdan, srāy- sing' and 'sraw [slwb'] word, spell' as separate entries — the two verbs are kept apart in Pahlavi itself.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II p. 179 s.v. *snūtan (glossary note)\", \"stance\": \"partial\",\n    \"note\": \"'For a vb. *snūtan snav-, however, no other support can be found ... Bthl (1630) regards this as a parallel form of (559) xšnu- (xšnav-) adj. \\\"satisfying\\\" ... from (557 sqq.) xšnav- \\\"to satisfy\\\"' — Nyberg too links the šn-/xšn- family to Bartholomae 557-559, not to sru-.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 82\", \"stance\": \"contradicts\",\n    \"note\": \"'phl. ptc. āšnūt, pr. 3. sg. āšnavēt (lies āšnavēt), pr. 3. pl. āšnavand ... auf ein ap. *xšnavamiy, inf. *xšnutanaiy von einer Wrzl. xšnū zurückzuführen, die sich nicht mit zd. sru vereinigen lassen würde.'\"}]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"šenîdan «شنیدن»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"New Persian شنیدن šenīdan / šunīdan 'to hear' with present stem شنو šenav- is the direct continuation of MP āšnūdan, āšnaw- with loss of the initial vowel (āšnūdan > šunūdan > šunīdan; the -īd- past stem is analogical, \"\n   \"beside the older شنفتن šunuftan and شنودن šunūdan which Nourai correctly lists as variants; the extras شنو 'hearing, listener' and حرف‌شنو 'obedient' are the bare present stem and a compound of it). \"\n   \"All of that is uncontroversial. What is disputed is the ultimate parent: Wiktionary (following Hasandust and Cheung) gives 'From Middle Persian /āšnūdan/ \\\"to hear, understand\\\", from Proto-Iranian *ā- + *xšnaw- \"\n   \"(\\\"to hear; to sharpen the ears\\\") ... the root is from Proto-Indo-Iranian *kšnaw-, from Proto-Indo-European *ksnew- (\\\"to scrape, sharpen\\\")', comparing Central Kurdish ژنفتن žiniftin and Zazaki eşnawitiş. \"\n   \"The Persian verb from *ḱleu- is not شنیدن but سرودن (node 5), and the Persian verb 'to listen' from yet a third root is نیوشیدن (< MP niyō(x)šīdan < *ni-gauš-). Nourai's chain root -> Av. srav- -> MP ašnūdan -> NP šenīdan \"\n   \"reproduces Horn 1893 (whose own note flags the difficulty) and has been abandoned by every 20th-century treatment.\"),\n \"derivation_fa\": (\"«شنیدن» فارسی نو با ستاک حال «شنو» دنبالهٔ مستقیم āšnūdan / āšnaw- فارسی میانه است با افتادن واکهٔ آغازین (āšnūdan > šunūdan > šunīdan)؛ ستاک گذشتهٔ -īd- قیاسی است و صورت‌های کهن‌تر «شنودن» و «شنفتن» \"\n   \"که نورایی هم آورده گواه آن‌اند، و «شنو» و «حرف‌شنو» همان ستاک حال و ترکیب آن‌اند. تا اینجا اختلافی نیست. آنچه مورد اختلاف است ریشهٔ نهایی است: ویکی‌واژه (به پیروی حسن‌دوست و چونگ) می‌نویسد که این فعل از فارسی میانهٔ \"\n   \"āšnūdan و آن از ایرانی آغازین *ā- + *xšnaw- «شنیدن؛ تیز کردن گوش» و سرانجام از *ksneu- هندواروپایی است، با هم‌ریشه‌های کردی سورانی «ژنفتن» و زازاکی eşnawitiş. \"\n   \"فعل فارسی‌ای که واقعاً از *ḱleu- آمده «سرودن» است و «نیوشیدن» هم از ریشهٔ سومی (*ni-gauš-) است. زنجیرهٔ نورایی بازتاب هرن (۱۸۹۳) است که خود او هم بر دشواری «ش» آغازین انگشت گذاشته بود، و پژوهش سدهٔ بیستم آن را کنار گذاشته است.\"),\n \"sources\": [W + \"شنیدن\", W + \"شنفتن\", W + \"نیوشیدن\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1304\", \"status\": \"contradicts\",\n    \"note\": \"Borhan-e Qāṭe', printed p.1303/1304 (BQT_v3_pages.txt pdf p.95) s.v. «شنیدن ۱ ـ بفتح اول بروزن رسیدن، معروف است و بعربی سماع گویند»; Mo'in's footnote to «شنودن» on the same page reads: «شنودن < اشنودن (ه‍.م)، پهلوی ašnūtan ... xšnūdan (اشنودن): از پارسی باستان āxšnavamiy، از ریشهٔ xšnū ... «هوبشمان-اسشق ۷۹۵»، طبری bešnōstan، مازندرانی ..., تاجیکی šonidan». The very reference Nourai cites derives the word from Old Persian ā-xšnav-, not from Avestan srav-.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in's own footnote in BQT (see ref_check) and Farhang-e Fārsi s.v. شنیدن\", \"stance\": \"contradicts\",\n    \"note\": \"Mo'in gives the same OP āxšnavamiy < xšnū derivation; he nowhere connects شنیدن with سرودن/سروش.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 795, p. 177\", \"stance\": \"supports\",\n    \"note\": \"Horn is the one source that supports Nourai: 'šunūden, šenīden \\\"hören\\\" ... aw. √srav-, surunaoiti \\\"hören\\\"' — but he immediately adds Bartholomae's ad-hoc 'Übertragung' explanation of the š- and calls Fr. Müller's alternative 'wenig überzeugend'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā, entry for the 'hear/ear' root (ARY_pages.txt l. 10590)\", \"stance\": \"partial\",\n    \"note\": \"«واژه‌ی انگلیسی loud ... نیز از همین واج‌ریشه است؛ ضمناً احتمال دارد که واژه‌ی فارسی \\\"شنیدن\\\" نیز از همین واج‌ریشه باشد (پارسی باستان āxšnavamiy، پهلوی ašnūtan/ašnūdan)» — Aryanpur treats the link as no more than a possibility and quotes the xšnav- forms while doing so.\"}]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"sravah; srŭ-ta; sraw; srâw\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The content is right, the labelling is loose. (a) Avestan sravah- n. is genuine: Bartholomae col. 1637 'j., g. sravah- n. 1) \\\"Wort\\\" (in koll. Sinn), (Plur.) \\\"Worte\\\"; 2) sva. \\\"Spruch, Lehre\\\"', the exact \"\n   \"cognate of Skt. śrávas-, Gk. kléos, OCS slovo, i.e. the PIE es-stem *ḱléwos. (b) 'srū-ta' is Av. srūta- 'heard, famous' (perf. pass. ptc. of srav-, Pokorny 605, Bartholomae 1638), and it is also the Old Iranian pre-form \"\n   \"*srū-ta from which Abolghasemi (FFD p.59) derives NP سرود — Nourai's gloss 'speech' is a compression of 'that which is recited'. (c) 'sraw' and 'srâw' are not Avestan citation forms at all: they are the Old Iranian root srav- \"\n   \"and its lengthened (causative) grade srāv- as Abolghasemi writes them (FFD pp.59-60: «srū صورت ضعیف ریشهٔ srav است ... srāv صورت بالاندهٔ ریشهٔ srav»), which in Middle Persian surface as sraw 'word, spell' (MacKenzie) \"\n   \"and srāy- 'to sing' (< *ḱlow-éye-, the causative 'to make heard'). Calling them Avestan is an inaccuracy of the box, not a false derivation: all four forms do descend from *ḱleu-.\"),\n \"derivation_fa\": (\"محتوای این جعبه درست است ولی برچسب زبانی آن دقیق نیست. الف) sravah- اوستایی واقعی است: بارتولمه (ستون ۱۶۳۷) آن را «واژه، سخن؛ گفتار، آموزه» معنی کرده و همان ستاک -es هندواروپاییِ *ḱléwos است \"\n   \"(هم‌ریشه با śrávas- سنسکریت، kléos یونانی و slovo اسلاوی). ب) srū-ta همان اسم مفعول اوستایی srūta- «شنیده، نامور» است و در عین حال صورت ایرانی باستانی است که ابوالقاسمی (فعل‌های فارسی دری، ص ۵۹) «سرود» را از آن می‌گیرد. \"\n   \"ج) sraw و srâw اصلاً صورت‌های اوستایی نیستند، بلکه ریشهٔ ایرانی باستان srav- و صورت «بالاندهٔ» آن srāv- به نگارش ابوالقاسمی‌اند که در فارسی میانه به sraw «سخن، ورد» و srāy- «سراییدن» رسیده‌اند. \"\n   \"پس اشکال تنها در نام‌گذاری زبان است، نه در پیوند ریشه‌شناختی: هر چهار صورت از *ḱleu- می‌آیند.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/ḱlew-\", W + \"سرودن\", \"https://www.avesta.org/avdict/avdict.htm\"],\n \"ref_check\": [\n   {\"ref\": \"POK:605\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt: '2. es-stem: Old Indic sravas- n. \\\"fame\\\", Avestan sravah- n. \\\"word\\\", gr. kléwos \\\"fame\\\" ... Old Church Slavic slovo \\\"word\\\"' and 'participle srūta- \\\"heard, famous\\\", srūti- \\\"das zu Gehörbringen, Vortrag\\\"'.\"},\n   {\"ref\": \"KLN:1456\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. slave (KLN_1966.txt l. 35506-7): 'OSlav. slovo, \\\"word\\\", fr. I.-E. base *kleu-, \\\"to hear\\\", whence also OI. śravas-, \\\"praise, glory\\\", Avestic sravah-, \\\"word\\\", Gk. kléos, \\\"fame\\\", L. cluere, \\\"to hear\\\", OE. hlūd, \\\"loud\\\".' Nourai's Avestan gloss 'word, speech' is Klein's.\"},\n   {\"ref\": \"FFD:60\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi p.59-60 (FFD_pages.txt pdf 64-65): «سرود ← فارسی میانه srūd ← ایرانی باستان *srū-ta ... srū صورت ضعیف ریشهٔ srav است، به معنی «خواندن»» and «سرای ← فارسی میانه srāy ← ایرانی باستان *srāva-ya ... srāv صورت بالاندهٔ ریشهٔ srav است» — the source of Nourai's 'srŭ-ta', 'sraw' and 'srâw'.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1637 s.v. sravah-\", \"stance\": \"supports\",\n    \"note\": \"'j., g. sravah- n. 1) \\\"Wort\\\" (in koll. Sinn), (Plur.) \\\"Worte\\\". 2) sva. \\\"Spruch, Lehre\\\"' with Gathic quotations Y.28.10, Y.32.9-12.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *srau, p. 357\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: MMP srʾy-, BMP slʾd- /srāy-/ \\\"to sing\\\" ... Partic.: perf. pass. BMP slwt /srūd/; Inf.: BMP slwtn /srūdan/ ... *NWIR: NP surūdan/sarāy- ... «PIE *ḱleu- \\\"to hear\\\" = LIV: 334 f. | Pok.: 605 f.»'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. sraw, srūd, srūdan\", \"stance\": \"supports\",\n    \"note\": \"'sraw [slwb'] word, spell. srawēnīdan, srawēn- [slwbyn-ytn'] report, broadcast' and 'srūd [slwt' | M srwd, N surōd] song' — Nourai's 'sraw' and 'srâw' are these Middle Persian shapes.\"}]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"sarvâ «سروا ( سرواد ، سرواده )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"سروا sarvā, with its by-forms سرواد sarvād and سرواده sarvāda, is a Dari word of the 10th-11th century meaning 'poem, verse, tale', preserved chiefly by the lexicographers; Asadi Ṭūsi's Loghat-e Fors \"\n   \"glosses it «حدیث و افسانه باشد» and quotes the very line Nourai prints, «چند دهی وعدهٔ دروغ همی چند / چند فروشی به من تو این سرو سروا» (Ormazdī). Formally it is *srav-ā-(da), i.e. the same Old Iranian stem srav- 'to recite' \"\n   \"as in سرود, extended with -āda/-āta (cf. the doublet سرود / سروده). The extras are the productive members of the family: سرودن sorūdan 'to sing, compose' < MP srūdan (perf. ptc. srūd) < PIr *srāwáyati < PIE *ḱlow-éye-ti, \"\n   \"causative 'to make heard'; سرود sorūd 'song, anthem' < MP srūd < OIr *srū-ta-; سراییدن sarāyīdan, a New Persian secondary infinitive built on the present stem سرای sarāy- < MP srāy- < *srāwaya-; and سرای ۲ 'singing, singer' \"\n   \"(the agent-stem in نغمه‌سرای, داستان‌سرای) — which must be kept apart from the homonym سرای 'house' (MP srāy < OP *srāda-, Hübschmann, Pers. Stud. 213). \"\n   \"Note that the causative stem *ḱlow-éye- had already specialised to 'sing, recite' in Iranian, which is why the Persian family means 'sing' where the Slavic and Germanic cognates mean 'word' and 'loud'.\"),\n \"derivation_fa\": (\"«سروا» و صورت‌های دیگرش «سرواد» و «سرواده» واژه‌ای دری از سده‌های چهارم و پنجم به معنی «شعر، سخن، افسانه» است که بیشتر در فرهنگ‌ها مانده است؛ اسدی طوسی در «لغت فرس» آن را «حدیث و افسانه» معنی کرده و همان بیتی \"\n   \"را که نورایی آورده گواه گرفته است: «چند دهی وعدهٔ دروغ همی چند / چند فروشی به من تو این سرو سروا» (اورمزدی). ساخت آن *srav-ā-(da) است، یعنی همان ستاک ایرانی باستان srav- «سراییدن» با پسوند -āda (مانند جفت «سرود / سروده»). \"\n   \"واژه‌های همراه نیز همگی از همین خانواده‌اند: «سرودن» از فارسی میانهٔ srūdan و آن از *srāwaya- ایرانی آغازین، ساختِ سببیِ *ḱlow-éye- «به گوش رساندن»؛ «سرود» از srūd فارسی میانه و *srū-ta ایرانی باستان؛ «سراییدن» مصدر جعلیِ \"\n   \"فارسی نو از ستاک حال «سرای»؛ و «سرای ۲» به معنی «سراینده» (در نغمه‌سرای و داستان‌سرای) که نباید با «سرای» به معنی «خانه» اشتباه شود (آن یکی از srāy فارسی میانه و *srāda- پارسی باستان است؛ هوبشمان، ص ۲۱۳). \"\n   \"معنای «سراییدن» در ایرانی از همان ستاک سببی «شنواندن» پدید آمده و از همین روست که خویشاوندان اسلاوی و ژرمنی آن معنای «واژه» و «بلند» دارند. ادعای نورایی درست است.\"),\n \"sources\": [W + \"سرودن\", \"https://abadis.ir/fatofa/سروا/\", \"https://lamtakam.com/dictionaries/dehkhoda/320125/سرود\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1131\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qāṭe' p.1131 (BQT_v2_pages.txt leaf 593): «سروا ۱ ـ بروزن پروا، بمعنی حدیث و سخن باشد ـ و بمعنی افسانهٔ دروغ هم گفته‌اند»؛ «سرواد ۲ ـ بروزن فرهاد، کلام منظوم و شعر را گویند ... و سرود هم گفته‌اند»؛ «سرواده ـ قافیهٔ شعر را گویند», with Mo'in's footnote quoting the Ormazdī couplet from لغت فرس ۷۹. Exactly Nourai's node.\"},\n   {\"ref\": \"BQT:1132\", \"status\": \"supports\",\n    \"note\": \"The facing page (leaf 594) carries «سرود» with Mo'in's footnote «پهلوی srōd < اوستا srav-, srao- (رک: سرودن) «اسشق ۵۳۷»؛ بلوچی srōd (موسیقی)، افغانی srōd» and «سرودن ... از: سرو + دن؛ پهلوی srōtan (آواز خواندن)، اوستا ریشهٔ srav- (شنیدن)، هندی باستان śrav-».\"},\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt): «سروا [ـ سرواد ـ سرواده] (ا.) شعر، سرود»؛ «سرواد [ـ سرواده] (ا.) شعر، سرود»؛ «سرواده [ـ سرواد] (ا.) شعر، قافیهٔ شعر».\"},\n   {\"ref\": \"FRS:27\", \"status\": \"partial\",\n    \"note\": \"Asadi's Loghat-e Fors: the entry is there — «سروا: حدیث و افسانه باشد، چنانکه اورمزدی گوید: چند دهی وعده دروغ همی چند / چند فروشی بمن تو این سرو سروا» (FRS_pages.txt leaf 26), plus «سرواد» at leaf ~90 — but the local copy is Eqbal's 1319 Tehran edition, whose pagination differs from the 1365 Kharazmi edition Nourai cites, so p.27 could not be checked as such.\"}],\n \"consulted\": [\n   {\"src\": \"FFD\", \"where\": \"Abolghasemi pp. 59-60 s.vv. سرودن، سرای\", \"stance\": \"supports\",\n    \"note\": \"«سرود ← فارسی میانه srūd ← ایرانی باستان *srū-ta» / «سرای ← فارسی میانه srāy ← ایرانی باستان *srāva-ya»; he adds the usage note that the modern pronunciation سُرای by analogy with سرود «قیاسی نادرست است».\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 213 (§102)\", \"stance\": \"supports\",\n    \"note\": \"'surūdan \\\"singen\\\", pr. sarāyam, zd. srū-' — and, two lines further, 'sarāi \\\"Palast\\\" = ap. *srāda-', which is the homonym سرای 'house' that must not be confused with سرای ۲ here.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. srūd, srūdan, srāy-\", \"stance\": \"supports\",\n    \"note\": \"'srūd [slwt' | M srwd, N surōd] song'; 'sing srūdan'; 'singing srāyišn' — and separately 'srāy [sd | N sarāy] house, hall', the distinct homonym.\"}]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Avestan\", \"words\": \"hu-srav; dâuš-sravah\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both compounds are attested. (a) Avestan hu-sravah- 'of good fame' (and the proper name Haosravah-, the Kayanian king Kai Haosravah, Yt. 5.49, 13.132, 15.32) is the exact equivalent of Vedic su-śrávas- and Greek \"\n   \"eu-kleḗs, i.e. hu- 'good' (PIE *h₁su-) + the es-stem sravah- 'fame' of node 4. (b) Avestan daoš.sravah- n. pl. is in Bartholomae col. 741: 'j. daoš.sravah- n., Plur. \\\"übler Ruf, schlechter Leumund\\\": ... uta būyā .. hacimnā \"\n   \"\\\"und üblen Ruf mögest du bekommen\\\" Y. 11.2', beside the adjective dus.sravah- 'der einen üblen Ruf, Leumund hat, δυσκλεής'. Nourai's 'dâuš-sravah' is a defensible transliteration of daoš- (the compound-initial form of duš-/dus- \"\n   \"'bad', PIE *dus-), and his cross-references ☞Su 1 and ☞Dus point to his own entries for those prefixes. The whole node is a straight and correct application of the es-stem *ḱléwos to the two Iranian prefixes.\"),\n \"derivation_fa\": (\"هر دو ترکیب در اوستا گواه دارند. الف) hu-sravah- «نیک‌نام» (و نام خاص Haosravah-، کیخسرو کیانی، یشت ۵/۴۹ و ۱۳/۱۳۲ و ۱۵/۳۲) درست برابر su-śrávas- ودایی و eu-kleḗs یونانی است: پیشوند hu- «نیک» \"\n   \"(از *h₁su- هندواروپایی) بر سر همان ستاک sravah- «آوازه» که در جعبهٔ پیشین آمد. ب) daoš.sravah- در فرهنگ بارتولمه (ستون ۷۴۱) چنین آمده است: «اسم خنثی، جمع، «بدنامی، آوازهٔ بد»»، در کنار صفت dus.sravah- «بدنام». \"\n   \"نگارش نورایی «dâuš-sravah» برگردانی پذیرفتنی از daoš- است، صورت ترکیبیِ duš-/dus- «بد» (از *dus- هندواروپایی). این جعبه کاربردی راست و درست از ستاک *ḱléwos با دو پیشوند ایرانی است؛ ادعای نورایی درست است.\"),\n \"sources\": [W + \"خسرو\", W + \"Reconstruction:Proto-Indo-European/ḱlew-\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:108\", \"status\": \"contradicts\",\n    \"note\": \"Horn's p.108 (HRN.txt leaf 129) does NOT deal with hu-sravah-: it contains nos. 486 'xusur \\\"Schwiegervater\\\". aw. x°asura- \\\"Schwiegervater\\\"; ai. śvaśura-' and 487 'xusrū, xešū, xisū, xes etc. \\\"Schwiegermutter\\\" ... ai. śvaśrū- \\\"Schwiegermutter\\\"; arm. skesur; lat. socrus; ksl. svekry.' Horn's actual treatment of the 'famous' word is no. 127, p.283: 'xusrav \\\"berühmt, erlaucht\\\", xusravīh. aw. husravah-; ai. su-śrávas-.' Nourai has cited the in-law page while drawing the fame-arrow — the root of the error that surfaces in node 8.\"},\n   {\"ref\": \"SNS:331\", \"status\": \"supports\",\n    \"note\": \"Tavoosi's Shāyast-nē-Šāyast glossary (SNS.txt l. 17996-7) has the entry 'dusrav / dusrab: ... (AiWb. 741) daoš.sravah-: اوستا', and its word-index (l. 33264) records 'dusrav 331/18' — Nourai's page 331 line 18. The companion entry 'husravīh: ... MPers hwsrwg ... (AiWb. 1738) haosravah-' is at l. 5487.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 741 (daoš.sravah-), col. ~750 (dus.sravah-), col. 1738 (Haosravah-)\", \"stance\": \"supports\",\n    \"note\": \"'j. daoš.sravah- n., Plur. \\\"übler Ruf, schlechter Leumund\\\"' (BRT.txt l. 13520) and 'j. dus.sravah- Adj. \\\"der einen üblen Ruf, Leumund hat, δυσκλεής\\\"' (l. 13797); Haosravah- as the name of the Kayanian king appears passim (l. 9128, 9578, 27190).\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. hu-srav\", \"stance\": \"supports\",\n    \"note\": \"'hu-srav [hwslwb'] of good honour, renown; renowned, illustrious ... — OIr *hu-sravah-, Skr su-śravas-; Paz. xusrūb; MPrs adj. hwsrwg < *hu-srava-ka-, v. srav and Xosrōi.'\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā, s.v. خسرو (ARY_pages.txt pdf p.241)\", \"stance\": \"supports\",\n    \"note\": \"Gives «اوستایی: HU-SRAVAH», «پهلوی: HUSRAV, HUSROV», «سانسکریت: su-śravas», Greek Chosroes, and cites «برهان قاطع: ۷۴۸؛ فرهنگ معین: ۱۳۳۰» — independently confirming that BQT p.748 is the خسرو page.\"}]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Pahlavi\", \"words\": \"hu-srov\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Middle Persian husraw is real and the arrow from Av. hu-sravah- is right: MacKenzie lemmatises 'husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good repute; ~īh: fame, good repute', and Nyberg derives it \"\n   \"'< OIr *hu-sravah-, Skr su-śravas-'. Phonetically Old Iranian *hu-srav-ah- > MP husraw (hu- 'good' retained before the cluster, the final syllable of the s-stem lost, -av- written -wb'/-w-), with the by-form husrōy that lies \"\n   \"behind Greek Chosroēs and Armenian Xosrov and behind the New Persian noun. The one thing wrong is the second half of Nourai's gloss, 'title of kings AND IN-LAWS'. No Middle Persian dictionary knows an in-law sense for husraw: \"\n   \"MacKenzie, Nyberg and the Frahang all give only 'famous, of good repute'. Nourai has taken the sense over from the Borhan-e Qāṭe' article خسرو (p.748/749), which does say «و بضم اول و ثانی و ثالث بمعنی خسر است که پدر زن و پدر شوهر باشد» — \"\n   \"but that entry is a lexicographer's conflation of two homonyms, and Mo'in's own footnote on the same page separates them (see node 8).\"),\n \"derivation_fa\": (\"husraw فارسی میانه واژه‌ای راستین است و پیکان آن از hu-sravah- اوستایی درست است: مکنزی آن را «نامور، نیک‌نام» معنی کرده و نیبرگ آن را از *hu-sravah- ایرانی باستان و su-śravas- سنسکریت گرفته است. \"\n   \"از نظر آوایی *hu-srav-ah- ایرانی باستان به husraw فارسی میانه رسیده (پیشوند hu- پیش از خوشهٔ همخوانی مانده و پایانهٔ ستاک -s از میان رفته) با گونهٔ husrōy که پشتِ Chosroēs یونانی و Xosrov ارمنی و «خسرو» فارسی نو است. \"\n   \"تنها ایرادِ این جعبه نیمهٔ دوم معنایی است که نورایی داده است: «لقب پادشاهان و خویشانِ سببی». هیچ فرهنگ پهلوی معنای «پدرزن/مادرزن» برای husraw نمی‌شناسد؛ این معنی از مقالهٔ «خسرو» برهان قاطع (ص ۷۴۸/۷۴۹) گرفته شده که دو واژهٔ \"\n   \"هم‌آوا را در یک مدخل درآمیخته است — و خودِ حاشیهٔ معین در همان صفحه آن دو را از هم جدا می‌کند.\"),\n \"sources\": [W + \"خسرو\", \"https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:748\", \"status\": \"partial\",\n    \"note\": \"Borhan p.748/749 (BQT_v2_pages.txt leaf 206) s.v. «خسرو ۴ ـ بضم اول و سکون ثانی ... بمعنی ملک و امام عادل باشد، و نام پادشاه کیان هم هست ... و بضم اول و ثانی و ثالث بمعنی خسر است که پدر زن و پدر شوهر باشد، و مادر زن و مادر شوهر را نیز گویند»; Mo'in's footnote 4 to it reads «پهلوی husrav (نیک‌نامی)، *hu-srav، اوستا haosravah- ... سانسکریت su-śravas، ... پازند xusrō ... معرب آن کسری». So BQT supports the Pahlavi form husrav and its Avestan source, but the in-law sense it also records is a homonym Mo'in himself footnotes separately.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. husraw\", \"stance\": \"partial\",\n    \"note\": \"'husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good repute. ~īh: fame, good repute' — 'famous' yes, 'in-laws' absent; the English-Pahlavi half of the dictionary likewise glosses 'famous husraw ... of good repute husraw'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.vv. hu-srav, Xosrōi\", \"stance\": \"partial\",\n    \"note\": \"'hu-srav [hwslwb'] of good honour, renown ... — OIr *hu-sravah-, Skr su-śravas-' and 'Xosrōi [hwslwd] ... Gr Xosroēs, NP Xusrav; Av. (1738) haosravah-. ... in the inscriptions: KZ Prth hwsrw, Gr. Xosroou' — again no in-law sense.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 213\", \"stance\": \"partial\",\n    \"note\": \"'Xusrav = arm. Xosrov, zd. husravah-' stands two lines after 'xusrū \\\"Schwiegermutter\\\" (auch xušū u.s.w.) = skr. śvaśrū-' — Hübschmann lists them adjacently as unrelated homonyms.\"}]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"xosrow «خسرو ( کسرىٰ )»; xosor «خُسُر ( خسور ، خسوره )»; xošŭ «خُشو»\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The node mixes one correct word with two that belong to a completely different PIE root, so the worst verdict applies. (a) خسرو xosrow '(great) king' is confirmed: NP xusraw < MP Husrōy / Husraw < Old Median *Husravah \"\n   \"< PIr *Hu-cráwāh 'renowned' < PII *Hsu-ćráwās, cognate with Vedic su-śrávas- and Gk. eu-kleḗs; Horn no. 127 (p.283) notes that the appellative sense 'ruler' 'beruht auf einer Verallgemeinerung des Personennamens aw. Husravah-' — \"\n   \"i.e. the Sasanian throne-name Xusrō I and II became a common noun 'king'. The Arabised كسرى Kisrā (Nourai's «کسرىٰ»), whence Kisrā/Chosroes in Arabic and Greek historiography, is the same word borrowed into Arabic. \"\n   \"(b) خسر xosor / خسور xosur 'father-in-law' does NOT come from hu-sravah-. It continues PIE *sweḱuros 'father-in-law' through PII *swáćuras > Avestan x°asura- > MP *xwasur > NP xusur/xosor, the exact cognate of Skt. śváśura-, \"\n   \"Lat. socer, Gk. hekyrós, OCS svekrъ, Goth. swaíhra. Horn no. 486 (p.108 — the page Nourai cites!) states it in so many words: 'xusur \\\"Schwiegervater\\\". aw. x°asura- \\\"Schwiegervater\\\"; ai. śvaśura-'. \"\n   \"(c) خشو xošū 'mother-in-law' (also خسرو xusrū, خشوه, خشوی in the older language) is the feminine of the same pair, PIE *sweḱruh₂ > PII *swaćrúH > Skt. śvaśrū-, Lat. socrus, OCS svekry; Wiktionary s.v. خشو: 'From Proto-Indo-Iranian \"\n   \"*swaćrúH, from Proto-Indo-European *sweḱrúh₂ (\\\"mother-in-law\\\")'. Horn no. 487 lists 'xusrū, xešū, xisū, xes' precisely under śvaśrū-. The reason Nourai (following the Borhan) went wrong is a genuine homonymy: \"\n   \"the older Persian word for 'mother-in-law' was xusrū, indistinguishable in the Arabic script from خسرو 'king', and the Borhan-e Qāṭe' merged them in one article. Mo'in's own footnotes on that page keep them apart — footnote 3 to \"\n   \"خسر gives «اوستا x°asura-، هندی باستان śvaśura- (پدر زن، پدر شوهر)», footnote 4 to خسرو gives «پهلوی husrav ... اوستا haosravah- ... سانسکریت su-śravas».\"),\n \"derivation_fa\": (\"این جعبه یک واژهٔ درست را با دو واژه از ریشه‌ای یکسره دیگر درآمیخته است. الف) «خسرو» به معنی «شاه بزرگ» تأیید می‌شود: فارسی نو xusraw از فارسی میانهٔ Husrōy/Husraw، از مادیِ باستان *Husravah، از ایرانی آغازین \"\n   \"*Hu-cráwāh «نامور»، هم‌ریشه با su-śrávas- ودایی و eu-kleḗs یونانی؛ هرن (شمارهٔ ۱۲۷، ص ۲۸۳) می‌افزاید که معنای عامِ «پادشاه» از «تعمیمِ نام خاص» خسرو انوشیروان و خسرو پرویز پدید آمده است. «کسریٰ» هم معرّب همین واژه است. \"\n   \"ب) اما «خسر/خسور» به معنی «پدرزن» هرگز از hu-sravah- نیامده است: این واژه دنبالهٔ *sweḱuros هندواروپایی است که از راه *swáćuras هندوایرانی به x°asura- اوستایی و سپس به xusur فارسی رسیده، هم‌ریشه با śváśura- سنسکریت، \"\n   \"socer لاتین، hekyrós یونانی و svekrъ اسلاوی. هرن در شمارهٔ ۴۸۶ — درست در همان صفحهٔ ۱۰۸ که نورایی به آن ارجاع داده — می‌نویسد: «xusur \\\"پدرزن\\\". اوستا x°asura-؛ سنسکریت śvaśura-». \"\n   \"ج) «خشو» به معنی «مادرزن» نیز مادینهٔ همان جفت است: *sweḱruh₂ هندواروپایی > śvaśrū- سنسکریت، socrus لاتین، svekry اسلاوی؛ ویکی‌واژه ذیل «خشو» همین را می‌آورد. سرچشمهٔ خطا هم‌آواییِ راستینی است: صورت کهن «مادرزن» در فارسی \"\n   \"xusrū بوده که در خط عربی از «خسرو» بازشناختنی نیست، و برهان قاطع هر دو را در یک مدخل آورده است — هرچند حاشیه‌های خود معین در همان صفحه آن‌ها را از هم جدا می‌کند. پژوهش امروزی این بخش از ادعای نورایی را رد می‌کند.\"),\n \"sources\": [W + \"خسرو\", W + \"خشو\", W + \"خسر\", W + \"Reconstruction:Proto-Indo-European/swéḱuros\", W + \"Reconstruction:Proto-Indo-Iranian/swáćuras\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:748\", \"status\": \"partial\",\n    \"note\": \"p.748/749 (leaf 206) gives all three words, but Mo'in's footnotes split them: fn. to «خسر»: «اوستا x°asura-، هندی باستان śvaśura- (پدر زن، پدر شوهر) «اسفا ۲: ص ۵۸۹ و ۵۸۰»؛ و رک: خسور، خشوره؛ و رک: لغت فرس ۵۳۱»; fn. to «خسرو»: «پهلوی husrav ... اوستا haosravah- ... سانسکریت su-śravas ... معرب آن کسری».\"},\n   {\"ref\": \"BQT:749\", \"status\": \"partial\",\n    \"note\": \"The continuation page (leaf 207) has «خسو ـ بروزن قصور، پدر شوهر و پدر زن را گویند» and «خسوره ـ بضم اول و فتح رای قرشت، بمعنی خسر است که پدر شوهر و پدر زن باشد»; the mother-in-law words «خش ـ بمعنی مادر زن و مادر شوهر باشد»، «خشامی» and «خشو ـ بضم اول و ثانی و سکون واو، مادر زن و مادر شوهر باشد» stand at pp. 751 and 756 (leaves 208, 213), not at 748-749.\"}],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Grundriss nos. 486-487, p. 108; no. 127, p. 283\", \"stance\": \"contradicts\",\n    \"note\": \"no. 486 'xusur \\\"Schwiegervater\\\". aw. x°asura- \\\"Schwiegervater\\\"; ai. śvaśura-; arm. skesrayr ... kurd. xazur, xezūr; afγ. sxor'; no. 487 'xusrū, xesū, xišū, xes etc. \\\"Schwiegermutter\\\". ai. śvaśrū- \\\"Schwiegermutter\\\"; arm. skesur; lat. socrus; ksl. svekry ... Vergl. xusur (No. 486)'. Against this, no. 127 (p.283) 'xusrav \\\"berühmt, erlaucht\\\" ... aw. husravah-; ai. su-śrávas-. np. xusrev \\\"Herrscher\\\" beruht dagegen auf einer Verallgemeinerung des Personennamens aw. Husravah-'.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 213 (§102)\", \"stance\": \"contradicts\",\n    \"note\": \"'xusrū \\\"Schwiegermutter\\\" (auch xušū u.s.w.) = skr. śvaśrū-; Xusrav = arm. Xosrov, zd. husravah-' — the two words listed in consecutive clauses with different etyma.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur s.v. خسرو (pdf p.241)\", \"stance\": \"supports\",\n    \"note\": \"For خسرو only: «اوستایی HU-SRAVAH؛ پهلوی HUSRAV, HUSROV؛ سانسکریت su-śravas؛ ارمنی Xosrov؛ یونانی Chosroes»; he gives no in-law sense under this headword.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in's BQT footnotes p.749 (cited above)\", \"stance\": \"contradicts\",\n    \"note\": \"The two etymological footnotes on the single printed page separate x°asura- (in-law) from haosravah- (fame) explicitly.\"}]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Pahlavi\", \"words\": \"du-srav\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian dušraw / dus-srav 'of ill fame, infamous' is the regular negative counterpart of husraw and continues Avestan duš.sravah- / daoš.sravah- (Bartholomae 741, 750): PIE *dus- 'bad, ill' + the es-stem \"\n   \"*ḱléwos > Ir. sravah- 'fame'. In Middle Persian the compound-final -ah- of the s-stem is lost as in husraw, giving duš-raw/dus-rav (written dwšslwb'). The word is attested in the Pahlavi Šāyast-nē-Šāyast, which is why Nourai \"\n   \"cites SNS:331 — Tavoosi's index records exactly 'dusrav 331/18'. The cross-reference ☞Dus is to Nourai's own entry for the prefix. New Persian keeps the family only in learned compounds (دشنام, دشوار, دژ-), the noun itself \"\n   \"having died out, which is presumably why the chart's Persian box below it (node 10) is empty.\"),\n \"derivation_fa\": (\"dušraw / dus-srav فارسی میانه «بدنام» درست همتای منفیِ husraw است و دنبالهٔ duš.sravah- / daoš.sravah- اوستایی (بارتولمه ۷۴۱ و ۷۵۰): پیشوند *dus- هندواروپایی «بد» بر سر ستاک *ḱléwos «آوازه». \"\n   \"در فارسی میانه پایانهٔ -ah- ستاک -s در ترکیب می‌افتد، چنان‌که در husraw، و duš-raw به دست می‌آید. این واژه در متن پهلویِ «شایست نشایست» به کار رفته و از همین رو نورایی به SNS:331 ارجاع داده است؛ نمایهٔ طاووسی هم دقیقاً \"\n   \"«dusrav 331/18» را ثبت کرده است. در فارسی نو خودِ این اسم از میان رفته و تنها پیشوند «دش-/دژ-» مانده است (دشنام، دشوار). ادعای نورایی درست است.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/ḱlew-\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:331\", \"status\": \"supports\",\n    \"note\": \"Tavoosi, Vāže-nāme-ye Šāyast-nē-Šāyast: glossary entry (SNS.txt l. 17996-7) 'dusrav / dusrab: ... (AiWb. 741) daoš.sravah-: اوستا' and word-index (l. 33264) 'dusrav 331/18'. The page and line Nourai cites is where the word stands in the text.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 741 and ~750\", \"stance\": \"supports\",\n    \"note\": \"'j. daoš.sravah- n., Plur. \\\"übler Ruf, schlechter Leumund\\\"' and 'j. duš.sravah- Adj. \\\"der einen üblen Ruf, Leumund hat, δυσκλεής\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, dušraw- family (dušxwaršt, dušgōwišn etc.)\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie's dictionary has a large duš-/dus- compound series ('dušox, dušxwaršt, dušgōwišn, dušdēn ...' — PHD.txt l. 5415) built on exactly this prefix, though he does not lemmatise dušraw itself.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. srav\", \"stance\": \"supports\",\n    \"note\": \"'srav [slwb'] word, message ... — Av. (1643 sq.) sravah-' — the second element of the compound, with the same Avestan reference.\"}]\n})\n\nN.append({\n \"id\": 10, \"lang\": None, \"words\": \"\",\n \"verdict\": \"unverified\",\n \"derivation\": (\"An empty box on the printed page (checked on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/270.png): the rectangle drawn to the right of the Pahlavi du-srav box carries no language label, \"\n   \"no word, no gloss and no reference — only the frame. The extraction is faithful (lang null, words []). What Nourai presumably meant to put there is the New Persian reflex of dušraw, but Modern Persian has no such noun \"\n   \"(only the productive prefix دش-/دژ- in دشنام, دشوار, دژخیم), which is very likely why the box was left blank. Nothing can be verified in it.\"),\n \"derivation_fa\": (\"جعبه‌ای است تهی در صفحهٔ چاپی (روی تصویر ۳۰۰ نقطه‌ای وارسی شد و در data/verification/sources/refs/ocr/BOOK/270.png نگهداری شده است): مستطیلی که در سمت راست جعبهٔ du-srav پهلوی کشیده شده نه برچسب زبانی دارد، \"\n   \"نه واژه، نه معنی و نه ارجاع. استخراج داده هم درست همین را نشان می‌دهد. گویا نورایی می‌خواسته بازماندهٔ فارسی نو dušraw را در آن بنویسد، ولی در فارسی امروز چنین اسمی وجود ندارد و تنها پیشوند «دش-/دژ-» مانده است \"\n   \"(دشنام، دشوار، دژخیم)؛ به همین سبب جعبه خالی مانده است. چیزی برای راستی‌آزمایی در آن نیست.\"),\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the printed chart.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, duš- entries\", \"stance\": \"silent\", \"note\": \"No Middle or New Persian noun *dušraw survives into Persian lexicography; only the prefix.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, دش-/دژ- entries\", \"stance\": \"silent\", \"note\": \"Mo'in has دشنام, دشوار, دژم etc. but no reflex of dušraw 'infamous'.\"}]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Avestan\", \"words\": \"sraothra, sraosha\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both nouns are real Avestan derivatives of srav-. (a) sraoθra- n.: Bartholomae col. 1637 '1) \\\"Gehör\\\" (nur Komp.); 2) \\\"Zugehörbringen, Aufsagen (der Gāθās)\\\"' — Pokorny 605 lists it beside Skt. śrótra- n. 'ear' \"\n   \"and OE hlēoðor, OHG hliodar 'sound'; the formation is *ḱleu-tro-, an instrument-noun 'means of hearing'. Nourai's gloss 'ear' comes from the Sanskrit cognate rather than from the Avestan usage, where the word is mostly \"\n   \"'recitation'. (b) sraoša- m. (Bartholomae 1634): the s-extension *ḱleus-, exactly Skt. śroṣa- / śruṣṭi- 'obedience, hearkening' and the same formation as Lith. klausýti, OE hlyst; in the Avesta sraoša- is both the abstract \"\n   \"'obedience, hearkening (to the divine command)' and the name of the yazata Sraoša, Ahura Mazdā's herald and the guardian of the soul on the Činvat bridge. Nourai's double gloss 'ear, one who listens and follows' captures \"\n   \"both nouns and both senses; the derivation from *ḱleu- is uncontested.\"),\n \"derivation_fa\": (\"هر دو واژه ساخته‌های راستین اوستایی از ریشهٔ srav- اند. الف) sraoθra- را بارتولمه (ستون ۱۶۳۷) «۱) شنوایی (تنها در ترکیب)؛ ۲) به گوش رساندن، از بر خواندنِ گاهان» معنی کرده است؛ پوکورنی (ص ۶۰۵) آن را در کنار \"\n   \"śrótra- سنسکریت «گوش» و hlēoðor انگلیسی کهن «آوا» می‌آورد. ساختش *ḱleu-tro- است، اسم ابزار به معنی «وسیلهٔ شنیدن»؛ معنیِ «گوش» که نورایی داده از هم‌ریشهٔ سنسکریت گرفته شده نه از کاربرد اوستایی. \"\n   \"ب) sraoša- (بارتولمه ۱۶۳۴) از ستاک گستردهٔ *ḱleus- است، درست همانند śroṣa-/śruṣṭi- سنسکریت و klausýti لیتوانیایی و hlyst انگلیسی کهن؛ در اوستا هم اسم معنی «فرمان‌برداری، گوش سپردن به فرمان ایزدی» است و هم نام ایزد سروش، \"\n   \"پیک اهورامزدا و نگهبان روان بر پل چینوت. معنای دوگانهٔ نورایی هر دو واژه را پوشش می‌دهد و پیوند با *ḱleu- بی‌مناقشه است.\"),\n \"sources\": [W + \"سروش\", \"https://www.iranicaonline.org/articles/sraosa/\", \"https://en.wikipedia.org/wiki/Sraosha\"],\n \"ref_check\": [\n   {\"ref\": \"POK:605\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt: 'Old Indic śrotra- n. \\\"ear\\\", Avestan sraoθra- n. \\\"the singing\\\" (= Old English hlēoðor, Old High German hliodar), Avestan sraota- n. \\\"the hearing\\\"' and, under the s-extension, 'Old Indic śroṣati \\\"hears, listens, conforms\\\", śruṣṭi- \\\"compliance, obsequiousness\\\", Avestan sraoša- \\\"ear, hearing\\\" etc.' Nourai's gloss 'ear, one who listens and follows' is a paraphrase of this very line.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. 1637 (sraoθra-), col. 1634 (sraoša-)\", \"stance\": \"supports\",\n    \"note\": \"'j. sraoθra- n. 1) \\\"Gehör\\\" (nur Komp.). 2) \\\"Zugehörbringen, Aufsagen (der Gāθās)\\\": gāθanąmca °rəm Y.3.4' (BRT.txt l. 27229); SNS's Avestan index cites 'sraoša-: (AiWb. 1634)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins kleu-1, section III\", \"stance\": \"partial\",\n    \"note\": \"Watkins keeps only the Germanic and Greek reflexes in his English-oriented list; the Iranian sraoθra-/sraoša- are absent — a silence, not a contradiction.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. Kleustis\", \"stance\": \"supports\",\n    \"note\": \"'Skt. śruṣṭiḥ f. \\\"obedience\\\"; Av. srušti- f. \\\"hearing\\\"; ... OE hlyst f. \\\"sense of hearing\\\"' — the same *ḱleus- family as sraoša-.\"}]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Pahlavi\", \"words\": \"srôsh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian Srōš [written slwš] continues Avestan sraoša- without difficulty: Av. -ao- > MP -ō-, Av. -š- kept, the thematic ending lost (sraoša- > srōš). In Zoroastrian Middle Persian literature Srōš is both \"\n   \"the abstract 'obedience' and, far more often, the yazata Srōš, protector of the soul for the three nights after death and one of the three judges at the Činvat bridge; the seventeenth day of every month is his. \"\n   \"Mo'in's footnote to the Borhan article سروش states it in exactly these terms: «اوستا sraoša-، پهلوی srōš. سرئوشه در اوستا بمعنی اطاعت و فرمانبرداری و مخصوصاً پیروی از اوامر خداوندی است، و آن از ریشهٔ اوستایی sru- (srav-) \"\n   \"که بمعنی شنیدن آمده». Nourai's gloss 'one who obeys (God)' is a fair rendering of that.\"),\n \"derivation_fa\": (\"Srōš فارسی میانه (نوشتهٔ slwš) بی هیچ دشواری دنبالهٔ sraoša- اوستایی است: -ao- اوستایی در فارسی میانه به -ō- بدل می‌شود، -š- می‌ماند و پایانهٔ ستاکی می‌افتد. در ادب زردشتی فارسی میانه «سروش» هم اسم معنیِ \"\n   \"«فرمان‌برداری» است و هم — بیشتر — نام ایزد سروش، نگهبان روان در سه شب پس از مرگ و یکی از سه داور پل چینوت؛ روز هفدهم هر ماه نیز به نام اوست. حاشیهٔ معین بر مدخل «سروش» برهان قاطع همین را می‌گوید: «اوستا sraoša-، پهلوی srōš. \"\n   \"سرئوشه در اوستا بمعنی اطاعت و فرمانبرداری و مخصوصاً پیروی از اوامر خداوندی است، و آن از ریشهٔ اوستایی sru- (srav-) که بمعنی شنیدن آمده». ادعای نورایی درست است.\"),\n \"sources\": [W + \"سروش\", \"https://www.iranicaonline.org/articles/sraosa/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1132\", \"status\": \"supports\",\n    \"note\": \"Borhan p.1132 (BQT_v2_pages.txt leaf 594), footnote 9 to the headword «سروش»: «اوستا sraoša-، پهلوی srōš «اسشق ۷۳۹». سرئوشه در اوستا بمعنی اطاعت و فرمانبرداری و مخصوصاً پیروی از اوامر خداوندی است، و آن از ریشهٔ اوستایی sru- (srav-) که بمعنی شنیدن آمده»; the note runs on to p.1133 with the whole account of the yazata.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Srōš (PHD.txt index l. 4782 'Srūš, srūšīg')\", \"stance\": \"supports\",\n    \"note\": \"MacKenzie lemmatises 'Srōš' and the adjective 'srōšīg' immediately beside 'srūd, srūdan' — same root, different formation.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 171 and p. 213\", \"stance\": \"supports\",\n    \"note\": \"'sarōš \\\"der Engel\\\" = zd. sraoša-' (p.171, in the list of words with prothetic/inserted a) and again in §102 p.213: 'Sarōš (der Engel) = zd. sraoša-'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. srav / Srōš\", \"stance\": \"supports\",\n    \"note\": \"Nyberg's glossary has 'srav [slwb'] word, message ... Av. (1643 sq.) sravah-' and cross-refers the srōš family to the same root.\"}]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"sorŭsh «سُروش»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian سروش sorūš (classical surōš) is inherited straight from MP Srōš with the usual prothetic/anaptyctic u- breaking up the initial sr- cluster, which Persian does not tolerate (cf. سرود < srūd, ستاره < stārag): \"\n   \"Wiktionary s.v. سروش: 'Inherited from Middle Persian slwš (/Srōš/), from Avestan sraoša (\\\"Sraosha\\\")'. In Islamic-period Persian the Zoroastrian yazata was reinterpreted as an angel bringing good tidings from God, often \"\n   \"identified with Gabriel — which is exactly Nourai's gloss 'one of God's angels' and the sense in his Ḥāfeẓ citation «لطف الهی بکند کار خویش / مژدهٔ رحمت برساند سروش». Mo'in glosses it «فرشته، ملک (مطلقاً)؛ روز هفدهم از هر ماه شمسی». \"\n   \"The word was passed on to Urdu (سروش saroś 'Gabriel; a heavenly voice') and Azerbaijani.\"),\n \"derivation_fa\": (\"«سروش» فارسی نو (در تلفظ کلاسیک surōš) میراثِ مستقیم Srōš فارسی میانه است با واکهٔ افزودهٔ آغازین که خوشهٔ sr- را می‌شکند — کاری که فارسی همواره می‌کند (سرود < srūd، ستاره < stārag). \"\n   \"ویکی‌واژه می‌نویسد: «به ارث رسیده از فارسی میانهٔ slwš (/Srōš/)، از اوستایی sraoša». در دورهٔ اسلامی ایزد زردشتی به فرشته‌ای بازتفسیر شد که مژدهٔ رحمت می‌آورد و بارها با جبرئیل یکی دانسته شده است — همان معنایی که نورایی داده و \"\n   \"همان که در بیت حافظِ گواهِ او دیده می‌شود. معین آن را «فرشته، ملک (مطلقاً)؛ روز هفدهم از هر ماه شمسی» معنی کرده است. این واژه به اردو (سروش saroś «جبرئیل؛ آوای غیبی») و آذربایجانی هم رفته است. ادعای نورایی درست است.\"),\n \"sources\": [W + \"سروش\", \"https://www.iranicaonline.org/articles/sraosa/\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"supports\",\n    \"note\": \"Borhan pp.1132-1133 s.v. «سروش»: «پیغام‌آور ... و مطلق فرشته را نیز گفته‌اند و بعربی ملک خوانند»، with Mo'in's long footnote on Sraoša as the yazata of obedience, his role at the resurrection, and the fact that «در ادبیات متأخر زردشتی ... حامل وحی خوانده شده، از این رو کتاب‌های فارسی او را با جبرائیل یکی دانسته‌اند».\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. سروش (MON_part1.txt)\", \"stance\": \"supports\",\n    \"note\": \"«سروش: srōš فرشته، ملک (مطلقاً). روز هفدهم از هر ماه شمسی. (مس.) یکی از گوشه‌های ماهور».\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p. 213\", \"stance\": \"supports\",\n    \"note\": \"'Sarōš (der Engel) = zd. sraoša-' — Hübschmann's own equation of the New Persian angel-name with the Avestan noun.\"}]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Old Slavic\", \"words\": \"slovo; Slověninŭ\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The first word is right, the second is the weak link. (a) Old Church Slavonic slovo (gen. slovese) 'word' is a textbook reflex of the PIE es-stem *ḱléwos: Proto-Slavic *slȍvo < Proto-Balto-Slavic *ślawas < *ḱléwos \"\n   \"'that which is heard, fame', with the regular satem s- from *ḱ and the Slavic ablaut family *slava 'glory', *sluti 'be renowned', *slyšati 'hear', *slušati 'listen'. It is the exact cognate of Av. sravah- (node 4), Skt. śrávas- \"\n   \"and Gk. kléos — the semantic drift 'fame' > 'word' being Slavic-specific. (b) *Slověninъ 'a Slav' from slovo, 'the people who speak (a language one understands)', is Klein's account and an old and popular one, but it is no longer \"\n   \"the mainstream analysis. Wiktionary's main entry derives it 'with *-ěninъ (\\\"-ian, inhabitant of\\\") suffixed to the root of *Slovǫta (\\\"the Dnieper\\\") or another, similar river name', on the morphological ground that \"\n   \"'*-ěninъ/*-janinъ is added only to geographical/territorial terms and place names', and files the derivation from slovo under 'Obsolete and alternative etymologies'; Vasmer had already rejected the connection with *slava as folk \"\n   \"etymology. Etymonline is softer ('probably related to *slovo ... which suggests the name originally identified a member of a speech community'), so the claim is not dead, but Nourai states as fact what modern Slavistics \"\n   \"treats as one superseded option.\"),\n \"derivation_fa\": (\"واژهٔ نخست درست است و واژهٔ دوم حلقهٔ سست این جعبه. الف) slovo اسلاوی کلیسایی کهن «واژه» نمونه‌ای درسی از بازتاب ستاک -es هندواروپاییِ *ḱléwos است: اسلاوی آغازین *slȍvo از بالتی‌ـ‌اسلاوی *ślawas از *ḱléwos \"\n   \"«آنچه شنیده می‌شود، آوازه»، با s- ساتمی از *ḱ و خانوادهٔ اسلاویِ *slava «شکوه»، *sluti «نامور بودن»، *slyšati «شنیدن». درست هم‌ریشهٔ sravah- اوستایی و śrávas- سنسکریت و kléos یونانی است و تحول معنایی «آوازه» به «واژه» ویژهٔ اسلاوی است. \"\n   \"ب) اما گرفتنِ *Slověninъ «اسلاو» از slovo — یعنی «مردمی که سخن می‌گویند» — روایت کلاین و روایتی کهن و رایج است ولی دیگر تحلیل غالب نیست. ویکی‌واژه در مدخل اصلی آن را از نام رودی مانند *Slovǫta (دنیپر) با پسوند *-ěninъ می‌گیرد، \"\n   \"با این استدلال ساختواژی که پسوند *-ěninъ تنها به نام‌های جغرافیایی می‌پیوندد، و اشتقاق از slovo را زیر عنوان «ریشه‌شناسی‌های منسوخ» آورده است؛ فاسمر هم پیوند با *slava را ریشه‌شناسی عامیانه خوانده بود. \"\n   \"پس این ادعا مردود قطعی نیست ولی نورایی چیزی را قطعی نوشته که اسلاوشناسی امروز آن را یکی از گزینه‌های کنارگذاشته می‌داند.\"),\n \"sources\": [W + \"Reconstruction:Proto-Slavic/slovo\", W + \"Reconstruction:Proto-Slavic/slověninъ\", \"https://www.etymonline.com/word/Slav\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1456\", \"status\": \"supports\",\n    \"note\": \"Klein s.v. slave (KLN_1966.txt l. 35506-7, printed p.1456): 'OSlav. Slověninŭ is a derivative of OSlav. slovo, \\\"word\\\", fr. I.-E. base *kleu-, \\\"to hear\\\" ... Accordingly the name Slav lit. means \\\"speaker\\\". For sense development cp. Church Slavic Němьci, \\\"Germans\\\", which is rel. to němъ, \\\"dumb\\\".' Nourai has transcribed Klein's page verbatim, including the ě of Slověninŭ.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 605-607, es-stem section\", \"stance\": \"supports\",\n    \"note\": \"'Old Church Slavic slovo \\\"word\\\"' listed under the es-stem beside Gk. kléwos and Av. sravah-; Pokorny says nothing about the ethnonym.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, s.v. slave\", \"stance\": \"partial\",\n    \"note\": \"Skeat gives the Slav > slave sense-development but does not commit to the slovo derivation of the ethnonym.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 15.41\", \"stance\": \"silent\",\n    \"note\": \"Buck lists the Slavic *slu-/*sly- verbs of hearing under the root but has no entry for the ethnonym.\"}]\n})\n\nN.append({\n \"id\": 15, \"lang\": \"Middle Greek\", \"words\": \"slabnovus\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"slabnovus\",\n \"correct_form\": \"Σκλαβηνός (Sklabēnós), pl. Σκλαβηνοί; short form Σκλάβος (Sklábos)\",\n \"derivation\": (\"The printed page really does read 'slabnovus' (verified on the 300-dpi render, copied to data/verification/sources/refs/ocr/BOOK/270.png), so the extraction is faithful and the error is Nourai's. The form he means is \"\n   \"Byzantine Greek Σκλαβηνός Sklabēnós / Σθλαβηνός Sthlabēnós, the 6th-century Greek rendering of Slavic *Slověninъ (Procopius, Jordanes' Sclaveni), with the epenthetic -k-/-θ- that Greek regularly inserts in the cluster σλ-. \"\n   \"From the plural Σκλαβηνοί 'the Slavs' Greek back-formed Σκλάβος Sklábos, attested c. 580, which by the 9th-10th century had acquired the sense 'slave' from the mass enslavement of Slavs in the Balkan and Ottonian wars. \"\n   \"Nourai's own gloss, 'Slav, also slaves taken from the Slavs', and the reference KLN:1456 are exactly Klein's account ('MGk. Sklábos, sklábos, \\\"slave\\\", prop. \\\"a slave of Slav descent\\\", back formation fr. MGk. Sklabēnós, \"\n   \"\\\"pertaining to the Slavs\\\"'). Two things went wrong in the printing: the k of Skl- was dropped, and the ending was Latinised to -ovus. The derivation drawn (Old Slavic -> Middle Greek) is correct.\"),\n \"derivation_fa\": (\"صفحهٔ چاپی به‌راستی «slabnovus» دارد (روی تصویر ۳۰۰ نقطه‌ای وارسی شد و در data/verification/sources/refs/ocr/BOOK/270.png نگهداری شده)، پس خطای خوانشِ اسکن نیست بلکه خطای چاپی خودِ کتاب است. \"\n   \"صورت درست Σκλαβηνός (Sklabēnós) یونانی میانه است، برگردانِ سدهٔ ششمیِ *Slověninъ اسلاوی (نزد پروکوپیوس و در Sclaveni یوردانس) با همان -k- میانجی که یونانی همواره در خوشهٔ σλ- می‌افزاید. \"\n   \"از جمعِ Σκλαβηνοί «اسلاوها» صورت کوتاهِ Σκλάβος (Sklábos) ساخته شد که از حدود ۵۸۰ میلادی گواه دارد و تا سدهٔ نهم و دهم، بر اثر بردگیِ انبوهِ اسلاوها در جنگ‌های بالکان و اوتونی، معنای «برده» گرفت. \"\n   \"معنایی که نورایی داده و ارجاع او به کلاین ص ۱۴۵۶ دقیقاً همان روایت کلاین است. دو خطا در چاپ رخ داده: افتادن k از Skl- و لاتینی‌شدن پایانه به -ovus. اما خودِ پیکانِ «اسلاوی کهن ← یونانی میانه» درست است.\"),\n \"sources\": [W + \"Σκλάβος\", \"https://www.etymonline.com/word/slave\", W + \"sclavus\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:1456\", \"status\": \"supports\",\n    \"note\": \"Klein p.1456 s.v. slave: 'ME. sclave, fr. OF. (= F.) esclave, fr. ML. Sclavus, Slavus, fr. MGk. Sklábos, sklábos, \\\"slave\\\", prop. \\\"a slave of Slav descent\\\", back formation fr. MGk. Sklabēnós, \\\"pertaining to the Slavs\\\", from the n. of Sklabēnoi (pl.), \\\"the Slavs\\\", which was formed — with inserted k — fr. OSlav. Slověninŭ.' Klein's 'Sklabēnós' is what the chart garbles.\"}],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. slave\", \"stance\": \"supports\",\n    \"note\": \"Skeat likewise routes English slave through OF esclave < Low Latin Sclavus < Greek Sklabos 'a Slavonian'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\",\n    \"note\": \"Grepped for 'Sklav', 'Sclav', 'esclave' — Lokotsch's remit is oriental loanwords and he has no entry for this Slavic-Greek chain.\"}]\n})\n\nN.append({\n \"id\": 16, \"lang\": \"Middle Latin\", \"words\": \"slavous\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"slavous\",\n \"correct_form\": \"Sclavus 'a Slav' / sclavus 'slave' (also Slavus)\",\n \"derivation\": (\"Again the printed page reads 'slavous' (checked on the page render), so the extraction is faithful and the mangled form is Nourai's own. The Medieval Latin word is Sclavus (with capital, 'a Slav', from Late Latin, \"\n   \"borrowed from Byzantine Greek Sklábos) and sclavus (lowercase, 'slave'), attested in the sense 'slave' from c. 800 in the Frankish and Ottonian sources; Slavus without the -c- is the later humanist spelling, which is presumably \"\n   \"what pulled Nourai's form towards 'slav-'. The -ous ending is simply wrong — no Latin form ends so. Nourai's double gloss 'Slav, slave' correctly reflects the capital/lowercase split, and the derivation Middle Greek -> Middle Latin \"\n   \"is exactly what Klein and every modern account give. Middle Latin sclavus is the source of Italian schiavo, Spanish esclavo, Old French esclave, German Sklave and Dutch slaaf.\"),\n \"derivation_fa\": (\"باز هم صفحهٔ چاپی «slavous» دارد (روی تصویر صفحه وارسی شد)، پس این هم خطای چاپی خودِ کتاب است نه خطای استخراج. صورت درست لاتین میانه Sclavus (با حرف بزرگ، «اسلاو»، وام‌گرفته از Σκλάβος یونانی) و sclavus \"\n   \"(با حرف کوچک، «برده») است که از حدود سال ۸۰۰ میلادی در منابع فرانکی و اوتونی به معنی «برده» گواه دارد؛ صورت Slavus بدون -c- املای متأخرِ دورهٔ اومانیستی است و گویا همان نورایی را به سوی «slav-» کشانده است. \"\n   \"پایانهٔ -ous یکسره نادرست است و هیچ صورت لاتینی چنین پایانه‌ای ندارد. معنای دوگانه‌ای که نورایی داده («اسلاو، برده») بازتاب درستِ همان دوگانگیِ حرف بزرگ و کوچک است و پیکانِ «یونانی میانه ← لاتین میانه» هم درست است. \"\n   \"sclavus لاتین میانه سرچشمهٔ schiavo ایتالیایی، esclavo اسپانیایی، esclave فرانسوی کهن، Sklave آلمانی و slaaf هلندی است.\"),\n \"sources\": [W + \"sclavus\", \"https://www.etymonline.com/word/slave\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the chart; the governing reference is the KLN:1456 of its parent.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p.1456 s.vv. slave, Slav, Slavonian\", \"stance\": \"supports\",\n    \"note\": \"'ML. Sclavus, Slavus' (both spellings given), and 'Slav, n. and adj. — G. Slave, fr. ML. Sclavus, Slavus, fr. MGk. Sklabēnos'; also 'ML. Sclavonia, \\\"the country inhabited by the Slavs\\\", fr. Sclavus'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. slave\", \"stance\": \"supports\",\n    \"note\": \"Skeat gives 'Low Lat. Sclavus, a slave, orig. a Slavonian'.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. des mots français d'origine orientale\", \"stance\": \"silent\",\n    \"note\": \"Grepped for 'esclave' and 'sclavus' — Devic's remit is oriental (Arabic/Persian/Turkish) loans; no entry.\"}]\n})\n\nN.append({\n \"id\": 17, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"An empty pass-through box; the French forms Nourai means are esclave 'slave' (Old French esclave, 12th-13th c., from Medieval Latin sclavus, with the prosthetic e- French regularly puts before Latin s + consonant, \"\n   \"as in escole, esprit) and the ethnonym Slave 'a Slav' (learned, from Medieval Latin Sclavus/Slavus). Both are well attested and both feed the two boxes below: esclave gives Middle English sclave > slave, and the Slave/-slave family \"\n   \"gives the country names Yougoslavie and Tchécoslovaquie which are the shape behind the Persian forms of node 18. The box is faithfully empty in the printed chart.\"),\n \"derivation_fa\": (\"جعبه‌ای گذری و تهی است؛ صورت‌های فرانسوی که نورایی در نظر داشته esclave «برده» است (فرانسوی کهن esclave، سدهٔ دوازدهم و سیزدهم، از sclavus لاتین میانه، با e- آغازینِ افزوده که فرانسوی همواره پیش از s + همخوان می‌آورد، \"\n   \"مانند escole و esprit) و نام قومی Slave «اسلاو» (وام‌واژه‌ای عالمانه از Sclavus/Slavus لاتین میانه). هر دو گواه استوار دارند و هر دو خوراکِ دو جعبهٔ زیرین‌اند: esclave به sclave انگلیسی میانه و سپس slave می‌رسد، و خانوادهٔ Slave \"\n   \"نام کشورهای Yougoslavie و Tchécoslovaquie را می‌سازد که صورت فارسیِ جعبهٔ بعدی از آن‌ها گرفته شده است. تهی‌بودنِ جعبه در چاپ اصلی هم همین‌گونه است.\"),\n \"sources\": [\"https://www.etymonline.com/word/slave\", W + \"slave\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box in the printed chart.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p.1456 s.v. slave\", \"stance\": \"supports\",\n    \"note\": \"'ME. sclave, fr. OF. (= F.) esclave, fr. ML. Sclavus' — the French stage explicitly.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. slave\", \"stance\": \"supports\",\n    \"note\": \"'F. esclave, a slave; Low Lat. Sclavus.'\"}]\n})\n\nN.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"(no transliterated word; script only: اسلاو ، چکوسلواکی ، یوگوسلاوی)\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"A 20th-century Persian borrowing box with no headword, only the three script forms. اسلاو eslāv 'a Slav', یوگوسلاوی Yugoslāvi 'Yugoslavia' and چکوسلواکی Čekoslovāki 'Czechoslovakia' are all modern loans, and French \"\n   \"mediation is likely but not documented. The phonetic evidence favours it: Persian renders the country names with final -ی, which matches French Yougoslavie / Tchécoslovaquie (French -ie > Persian -ی) rather than English \"\n   \"Yugoslavia / Czechoslovakia (which would give -یا, as in ایتالیا, استرالیا); and French was the dominant channel for Western vocabulary in Persian from the Qajar period through the first Pahlavi decades, when these two states \"\n   \"were founded (1918-1919). Wiktionary's Persian entry اسلاو gives pronunciation only, with no etymology section; the Persian Wikipedia article چکسلواکی cites Czech Československo and English Czechoslovakia, not French. \"\n   \"So the words and glosses are right, the route through French is a reasonable inference that no source states.\"),\n \"derivation_fa\": (\"جعبه‌ای است از وام‌واژه‌های سدهٔ بیستم، بی سرواژهٔ آوانویسی‌شده و تنها با سه صورت فارسی. «اسلاو»، «یوگوسلاوی» و «چکوسلواکی» هر سه وام‌واژهٔ نو هستند و میانجیگری فرانسه محتمل است ولی سندی برای آن نیافتم. \"\n   \"گواه آوایی به سود فرانسه است: فارسی پایانهٔ این دو نام کشور را «-ی» می‌آورد که با Yougoslavie و Tchécoslovaquie فرانسوی می‌خواند (پسوند -ie فرانسوی در فارسی «-ی» می‌شود) نه با صورت انگلیسی که «-یا» می‌داد (مانند ایتالیا و استرالیا)؛ \"\n   \"و از دورهٔ قاجار تا دههٔ نخست پهلوی، یعنی همان زمانی که این دو کشور بنیاد گرفتند (۱۹۱۸ و ۱۹۱۹)، فرانسه مجرای اصلی واژگان غربی در فارسی بود. مدخل «اسلاو» در ویکی‌واژه بخش ریشه‌شناسی ندارد و ویکی‌پدیای فارسی «چکسلواکی» را از \"\n   \"Československo چکی و صورت انگلیسی می‌گیرد نه از فرانسه. پس واژه‌ها و معناها درست‌اند و مسیر فرانسوی استنباطی پذیرفتنی ولی بی‌سند است.\"),\n \"sources\": [W + \"اسلاو\", \"https://fa.wiktionary.org/wiki/یوگوسلاوی\", \"https://fa.wikipedia.org/wiki/چکسلواکی\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"not_found\",\n    \"note\": \"Mo'in's Farhang-e Fārsi vol. 5-6 (a'lām) would carry اسلاو / یوگوسلاوی as proper names, but the local OCR (MON_part1/2, the lexicon volumes) has no such entry — grepped 'اسلاو', 'یوگوسلاوی', 'چکوسلواکی' with no hits in the dictionary text.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt\", \"stance\": \"silent\",\n    \"note\": \"No entries for اسلاو، یوگوسلاوی، چکوسلواکی in the available lexicon volumes; Nourai's 'MON' must point at vols. 5-6 (proper names), which are not in the local copy.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā (ARY_pages.txt l. 94, 205, 235)\", \"stance\": \"partial\",\n    \"note\": \"Aryanpur uses «اسلاو» / «اسلاوی» freely as the Persian name of the Slavic branch («زبان‌های بالتیک و اسلاوی») but gives no etymology of the Persian word itself.\"}]\n})\n\nN.append({\n \"id\": 19, \"lang\": \"English\", \"words\": \"Slav, Yugoslavia, Czechoslovakia, slave\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All four words are real and all four go back through Medieval Latin to Byzantine Greek and Slavic; only the routing through French is partly wrong. slave: Middle English sclave (c. 1300) < Old French esclave < \"\n   \"Medieval Latin sclavus — French mediation correct. Slav: attested in English from the late 14th century as Sclave, taken from Medieval Latin Sclavus (Klein: 'G. Slave, fr. ML. Sclavus, Slavus'), i.e. through Latin and German, not \"\n   \"through French; the modern spelling Slav dates from 1866, and the reduction of scl- to sl- is a regular English development (compare slate). Yugoslavia and Czechoslovakia are 20th-century state names built on Serbo-Croatian \"\n   \"Jugoslavija (jug 'south' + Slav) and Czech Československo, taken into English at the Paris peace conference of 1918-19, again not through French. So the etymological substance is right, the intermediary drawn for three of \"\n   \"the four words is not.\"),\n \"derivation_fa\": (\"هر چهار واژه راستین‌اند و هر چهار از راه لاتین میانه به یونانی بیزانسی و اسلاوی می‌رسند؛ تنها مسیرِ فرانسویِ نمودار برای سه‌تای آن‌ها نادرست است. slave: انگلیسی میانهٔ sclave (حدود ۱۳۰۰) از esclave فرانسوی کهن \"\n   \"از sclavus لاتین میانه — اینجا میانجیگری فرانسه درست است. Slav: از اواخر سدهٔ چهاردهم به صورت Sclave در انگلیسی گواه دارد و از Sclavus لاتین میانه (و از راه آلمانی) گرفته شده نه از فرانسه؛ املای امروزی Slav از ۱۸۶۶ است و ساده‌شدن \"\n   \"scl- به sl- تحولی قاعده‌مند در انگلیسی است (مانند slate). Yugoslavia و Czechoslovakia هم نام دو کشورِ سدهٔ بیستم‌اند، ساختهٔ Jugoslavija صربی‌ـ‌کرواتی (jug «جنوب» + Slav) و Československo چکی، که در کنفرانس صلح پاریس (۱۹۱۸-۱۹) وارد \"\n   \"انگلیسی شدند، باز هم نه از راه فرانسه. پس جانِ ریشه‌شناسی درست است و تنها واسطهٔ ترسیم‌شده برای سه واژه از چهار واژه درست نیست.\"),\n \"sources\": [\"https://www.etymonline.com/word/slave\", \"https://www.etymonline.com/word/Slav\", W + \"slave\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; the governing reference is KLN:1456 further up the chain.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p.1456 s.vv. Slav, slave, Slavonian, Slovak, Slovene\", \"stance\": \"partial\",\n    \"note\": \"'Slav, n. and adj. — G. Slave, fr. ML. Sclavus, Slavus, fr. MGk. Sklabēnos. See slave.' — via German, not French; 'slave, n. — ME. sclave, fr. OF. (= F.) esclave' — via French, as drawn.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. slave\", \"stance\": \"supports\",\n    \"note\": \"Skeat routes slave through French esclave, agreeing with the chart for that word.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 (A-...)\", \"stance\": \"silent\",\n    \"note\": \"Only volume 1 (A-) of the local Webster scan is available; the S- entries are in the missing volume 2.\"}]\n})\n\nN.append({\n \"id\": 20, \"lang\": \"Germanic\", \"words\": \"hlusinôn; hlŭdaz\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both Proto-Germanic forms are taken straight from Watkins/AHD and both are right. *hlusinōn 'to listen' is the zero-grade *ḱlu- plus the s-extension (*ḱleus-) plus a denominative suffix; it gives Old English hlysnan \"\n   \"(Mercian), Northumbrian lysna. (Wiktionary's Old English entry prefers the reconstruction *hlusnijaną — a variant of the same formation, not a different etymology.) *hlūdaz 'loud' is the PIE verbal adjective *ḱlu-tó- 'heard', \"\n   \"with a long ū whose origin Wiktionary calls unclear; it is the exact cognate of Skt. śrutá-, Gk. klytós, Lat. inclutus, OIr. cloth, Arm. lu, and gives OE hlūd, OS/OFris. hlūd, OHG hlūt (> German laut). Klein s.v. loud has the \"\n   \"same set: 'fr. I.-E. pp. base *klu-to-s, whence also OI. śrutáḥ, Gk. klytós, \\\"heard of, celebrated\\\", L. in-clutus'.\"),\n \"derivation_fa\": (\"هر دو صورت ژرمنی آغازین را نورایی مستقیم از واتکینز (AHD) گرفته و هر دو درست است. *hlusinōn «گوش دادن» از درجهٔ صفرِ *ḱlu- با گسترشِ -s (*ḱleus-) و پسوند فعلیِ اسم‌ساز است و به hlysnan انگلیسی کهن می‌رسد \"\n   \"(ویکی‌واژه بازسازیِ *hlusnijaną را ترجیح می‌دهد که گونهٔ همان ساخت است نه ریشه‌شناسی دیگر). *hlūdaz «بلند» همان صفت مفعولی هندواروپاییِ *ḱlu-tó- «شنیده» است با کشیدگیِ ū که سرچشمه‌اش روشن نیست؛ درست هم‌ریشهٔ śrutá- سنسکریت، \"\n   \"klytós یونانی، inclutus لاتین، cloth ایرلندی کهن و lu ارمنی، و در ژرمنی به hlūd انگلیسی کهن و hlūt آلمانی کهن (> laut) می‌رسد. کلاین هم ذیل loud همین‌ها را می‌آورد. ادعای نورایی درست است.\"),\n \"sources\": [W + \"Reconstruction:Proto-Germanic/hlūdaz\", \"https://www.etymonline.com/word/loud\", \"https://www.etymonline.com/word/listen\", W + \"hlysnan\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. kleu-1: 'II. Zero-grade form *klu-. 1. Germanic *hlustjan in Old English hlystan, to listen: LIST. 2. Germanic *hlusinōn in Old English hlysnan, to listen: LISTEN. 3. Suffixed lengthened form *klū-to- in Germanic *hludaz, \\\"heard,\\\" loud, in: a. Old English hlūd, loud: LOUD; b. Old High German hlūti, sound: ABLAUT, UMLAUT.' Nourai's two forms and two glosses are verbatim from this entry.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. loud, listen\", \"stance\": \"supports\",\n    \"note\": \"'loud, adj. — ME. loud, fr. OE. hlūd ... fr. I.-E. pp. base *klu-to-s, whence also OI. śrutáḥ, Gk. klytós, \\\"heard of, celebrated\\\", L. in-clutus'; 'listen ... fr. OE. hlystan ... and OE. hlysnan, \\\"to listen\\\", which is rel. to OE. hlosnian, OHG. hlosēn, *hluskēn (whence MHG. luschen, G. lauschen)'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 605-607, s-extension section\", \"stance\": \"supports\",\n    \"note\": \"'Old English hlyst \\\"ear, hearing\\\" ... Old Icelandic hlusta, Old English hlysnan (engl. listen) \\\"wake up, become alert, listen\\\"; with ū (as Old High German hlūt, see above)'.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.vv. listen, loud\", \"stance\": \"supports\",\n    \"note\": \"F&W gives the same OE hlysnan / hlūd starting points for the two words.\"}]\n})\n\nN.append({\n \"id\": 21, \"lang\": \"English\", \"words\": \"listen, loud\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both are inherited English words, not borrowings. listen: OE hlysnan > ME listnen; the modern -t- is secondary, from a blend with ME listen (< OE hlystan 'to hear', from the noun hlyst 'hearing'), the same intrusive \"\n   \"-t- as in glisten; the initial hl- simplified to l- in Middle English as in loud/hlūd's sister words hlāford > lord, hlǣfdige > lady. loud: OE hlūd > ME loud, direct continuation of PGmc *hlūdaz. Both are on Watkins's own \"\n   \"English word-list for kleu-1 (LISTEN, LOUD), and Nourai has simply copied that list. There is no dispute about either.\"),\n \"derivation_fa\": (\"هر دو واژه‌ای بومی‌اند نه وام‌واژه. listen: از hlysnan انگلیسی کهن به listnen انگلیسی میانه؛ -t- امروزی ثانوی است و از آمیختن با listen انگلیسی میانه (از hlystan «شنیدن»، از اسمِ hlyst «شنوایی») پدید آمده، \"\n   \"همان -t- میانجی که در glisten هم دیده می‌شود؛ خوشهٔ hl- آغازین نیز در انگلیسی میانه به l- ساده شده است، چنان‌که hlāford به lord و hlǣfdige به lady رسیده‌اند. loud: از hlūd انگلیسی کهن، دنبالهٔ مستقیم *hlūdaz ژرمنی آغازین. \"\n   \"هر دو در همان فهرستِ انگلیسیِ واتکینز ذیل kleu-1 آمده‌اند و نورایی همان را رونویسی کرده است. اختلافی در کار نیست.\"),\n \"sources\": [\"https://www.etymonline.com/word/listen\", \"https://www.etymonline.com/word/loud\", \"https://www.etymonline.com/word/*kleu-\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; the AHD of the parent node covers it, and Watkins's small-caps entries LISTEN and LOUD are the authority.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. listen, loud\", \"stance\": \"supports\", \"note\": \"Quoted under node 20.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. listen, loud\", \"stance\": \"supports\",\n    \"note\": \"Skeat gives OE hlysnan for listen and OE hlūd for loud, with the same IE comparison (Skt. śruta-, Gk. klytos).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index\", \"stance\": \"supports\",\n    \"note\": \"The index lines 'LISTEN kleu-1' and 'LOUD kleu-1' (AHD_watkins1985.txt) place both words under this root and no other.\"}]\n})\n\nN.append({\n \"id\": 22, \"lang\": \"Latin\", \"words\": \"cluere\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin clueō/cluō, -ēre 'to be called, be named, be spoken of, be reputed' is a genuine and uncontroversial reflex of *ḱleu-: Pokorny 606 has 'Latin clueō, -ēre (later also cluō, -ere) \\\"to hear, be spoken of, be said\\\" \"\n   \"(ē-verb with the zero grade ḱlu-)', with the derivatives cluor 'glory, reputation' and inclutus/inclitus 'illustrious'; Wiktionary lemmatises clueō 'From Proto-Italic *kluēō, from Proto-Indo-European *ḱlew-'. One caution: \"\n   \"Latin has a homonymous cluō 'to cleanse, purge' (whence cloāca) from PIE *ḱlewH- 'to rinse' (Pokorny's ḱleu-2, p.607) — a different root, not to be confused with this one. The node itself is right; the problem is what \"\n   \"Nourai hangs beneath it (node 23).\"),\n \"derivation_fa\": (\"فعل لاتین clueō/cluō, -ēre «نامیده شدن، آوازه داشتن، گفته شدن» بازتابی راستین و بی‌مناقشه از *ḱleu- است: پوکورنی (ص ۶۰۶) آن را «فعل ē-دار با درجهٔ صفرِ ḱlu-» می‌خواند و مشتقات cluor «آوازه» و inclutus «نامور» \"\n   \"را در پی آن می‌آورد؛ ویکی‌واژه هم آن را از *kluēō ایتالیایی آغازین و *ḱlew- هندواروپایی می‌گیرد. یک هشدار: لاتین فعل هم‌آوای دیگری دارد، cluō «شستن، پاک کردن» (که cloāca از آن است) از *ḱlewH- «شستن» (ریشهٔ دوم پوکورنی، ص ۶۰۷) \"\n   \"که ریشه‌ای جداست و نباید با این یکی درآمیخت. خودِ این جعبه درست است؛ اشکال در جعبه‌ای است که نورایی زیر آن آویخته (جعبهٔ بعد).\"),\n \"sources\": [W + \"clueo\", W + \"cluo\", \"https://www.etymonline.com/word/*kleu-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins's kleu-1 entry does NOT list Latin cluere at all (its Latin material is confined to what feeds English: CLIO from Greek, LEER, LIST, LISTEN, LOUD, ABLAUT, UMLAUT). So the AHD citation does not cover this node; the claim is nonetheless correct and is in Pokorny 606, which Watkins cross-references ('[Pok. 1. ḱleu- 605.]').\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 606\", \"stance\": \"supports\",\n    \"note\": \"'Latin clueō, -ēre (later also cluō, -ere) \\\"to hear, be spoken of, be said\\\" (ē-verb with the zero grade ḱlu-), cluor (Gl.) \\\"that is known, well-known, famous\\\", inclutus \\\"illustrious\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p.1456 s.v. slave (cognate list)\", \"stance\": \"supports\",\n    \"note\": \"'L. cluere, \\\"to hear\\\"' is listed among the *kleu- cognates — Klein's own placement of the verb under this root.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde-Hofmann, Lat. etym. Wb. s.v. clueo\", \"stance\": \"supports\",\n    \"note\": \"Pokorny's own reference for this word is 'WH. 86 f., 237 ff.' — Walde-Hofmann's clueō article, which gives the same IE connection.\"}]\n})\n\nN.append({\n \"id\": 23, \"lang\": \"English\", \"words\": \"client\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"English client (late 14th c., from Latin clientem, acc. of cliēns 'retainer, follower, dependant') is real, but modern scholarship does not derive it from cluere. The standard analysis takes cliēns as a participial \"\n   \"formation to *clinare 'to lean' — 'one who leans on another for protection' — i.e. PIE *ḱlei- 'to lean', the root of clinic, incline, decline, ladder, lean, lid. This is Watkins's own placement: the AHD index line reads \"\n   \"'CLIENT klei-', and Watkins's kleu-1 entry does not contain CLIENT — so the reference Nourai gives ('AHD') is the very authority that contradicts him. Klein is even blunter, s.v. client: 'lit. \\\"one who leans on another\\\", fr. \"\n   \"I.-E. base *klei-, \\\"to lean, incline\\\" ... The usual derivation of L. cliens from the stem of cluere, \\\"to be named\\\", is erroneous.' Etymonline agrees, listing client under *klei- and not under *kleu-. In fairness the older view \"\n   \"is not extinct — Wiktionary s.v. cliens still gives 'Possibly an alteration of cluēns, present active participle of clueō (\\\"to be called, named, esteemed\\\")' as its first option, with clīnō as the alternative — so the node is \"\n   \"disputed rather than simply wrong; but Nourai attributes the minority view to a source that holds the majority one.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی client (اواخر سدهٔ چهاردهم، از clientem لاتین، حالت مفعولیِ cliēns «پیرو، دست‌نشانده») واژه‌ای راستین است، ولی پژوهش امروزی آن را از cluere نمی‌گیرد. تحلیل معیار cliēns را ساختی صفتی از clīnāre «خم شدن» \"\n   \"می‌داند — «کسی که برای پناه بر دیگری تکیه می‌کند» — یعنی از ریشهٔ *ḱlei- «تکیه دادن»، همان ریشهٔ clinic و incline و decline و lean. جای‌گذاریِ خودِ واتکینز هم همین است: در نمایهٔ AHD می‌خوانیم «CLIENT klei-» و مدخل kleu-1 او \"\n   \"اصلاً نام client را ندارد؛ پس همان مرجعی که نورایی به آن ارجاع داده (AHD) ادعای او را رد می‌کند. کلاین از این هم صریح‌تر است و ذیل client می‌نویسد: «اشتقاق رایجِ cliens لاتین از ستاک cluere «نامیده شدن» نادرست است». \"\n   \"اتیمانلاین نیز client را ذیل *klei- می‌آورد. البته دیدگاه کهن یکسره نمرده است — ویکی‌واژه ذیل cliens هنوز «شاید دگرگون‌شدهٔ cluēns، اسم فاعل clueō» را گزینهٔ نخست می‌آورد — پس این جعبه «مورد اختلاف» است نه بی‌چون‌وچرا نادرست؛ \"\n   \"ولی نورایی دیدگاه اقلیت را به مرجعی نسبت داده که خودِ آن مرجع دیدگاه اکثریت را دارد.\"),\n \"sources\": [\"https://www.etymonline.com/word/client\", \"https://www.etymonline.com/word/*klei-\", W + \"cliens\", W + \"clueo\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The English box itself carries no reference; the AHD of its parent (node 22) is the governing citation and it contradicts the node — Watkins's index reads 'CLIENT klei-' (AHD_watkins1985.txt l. 1370) and his kleu-1 entry omits CLIENT entirely.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, index s.v. CLIENT and entry klei-\", \"stance\": \"contradicts\",\n    \"note\": \"Index: 'CLIENT klei-'; entry kleu-1's English list is 'LEER; LIST; LISTEN; LOUD; ABLAUT, UMLAUT; CLIO' — no CLIENT.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. client\", \"stance\": \"contradicts\",\n    \"note\": \"'client, n. — F., fr. L. clientem, acc. of cliens, \\\"retainer, follower, dependent\\\", lit. \\\"one who leans on another\\\", fr. I.-E. base *klei-, \\\"to lean, incline\\\", whence also L. -clinare ... The usual derivation of L. cliens from the stem of cluere, \\\"to be named\\\", is erroneous.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cliens\", \"stance\": \"contradicts\",\n    \"note\": \"Ernout-Meillet likewise attach cliēns to the *klei- 'lean' family (clīnō, clīvus, -clīnis), the analysis Klein and Watkins follow.\"}]\n})\n\ndoc = {\"pdf_page\": 270, \"book_page\": 240, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-09-06\",\n       \"entries\": [root]}\nopen('/home/sfmqrb/git/rishe/data/verification/page-270.json','w',encoding='utf-8').write(\n    json.dumps(doc, ensure_ascii=False, indent=2) + \"\\n\")\nprint(\"ok nodes\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build270.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-270.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 270"
}
```


### [2026-09-06T21:16:57.438Z] TOOL RESULT

```
ok nodes 23
JSON OK
nodes verified: 23/23
node verdicts: {'disputed': 6, 'plausible': 4, 'confirmed': 10, 'unverified': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'contradicts': 3, 'supports': 14, 'not_checked': 6, 'not_found': 1}
books consulted: {'partial': 12, 'contradicts': 10, 'supports': 37, 'silent': 7} | by book: {'HUB': 7, 'PHD': 7, 'KLN': 7, 'SKT': 6, 'BRT': 5, 'NYB': 5, 'MON': 5, 'ARY': 4, 'AHD': 3, 'POK': 3, 'CHEUNG': 2, 'HRN': 2, 'KNT': 1, 'FFD': 1, 'IEC': 1, 'SYN': 1, 'LKT': 1, 'DEV': 1, 'WEB': 1, 'FSD': 1, 'LEW': 1, 'LAT': 1}
```


## [2026-09-06T21:17:14.413Z] AGENT

Incorporating the Iranian branch findings into a few nodes.


## [2026-09-06T21:17:39.073Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\np='data/verification/page-270.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\nW=\"https://en.wiktionary.org/wiki/\"\n\n# node 1: sharpen the Avestan xšnu- point (Av. xšnu- = 'propitiate' only; the 'hear' sense is Old Persian)\nn=nodes[1]\nn['derivation']=n['derivation'].replace(\n \"Nourai has put them here because he needed a source for the š- of شنیدن (nodes 2-3).\",\n \"Worse, the gloss 'to hear' is wrong for Avestan specifically: in the Avesta xšnu-/xšnav- means only 'to satisfy, propitiate, entertain (a guest)' (Kanga's Avestan dictionary: xšnu 'to be pleased or propitiated', xšnaothra 'propitiation'); the 'hear' sense of this root is attested in OLD PERSIAN ā-xšnau- (āxšnaumiy, āxšnavahy, āxšnudiy), not in Avestan. Nourai has put the forms here because he needed a source for the š- of شنیدن (nodes 2-3).\")\nn['sources'].append(\"https://www.avesta.org/avdict/avdict.htm\")\n\n# node 2: MacKenzie's exact entry\nn=nodes[2]\nn['consulted'][0]['note']=(\"MacKenzie, Concise Pahlavi Dictionary p.13: 'āšnūdan, āšnaw- [ʾšnwtn' | M ʾšnwdn, ʾšnw- | N šunūdan, šunaw-] hear, understand', with āšnawāg 'hearing'; on the same page-range he lemmatises 'srūdan, srāy- sing' and 'sraw [slwb'] word, spell' as separate entries — the two verbs are kept apart in Pahlavi itself.\")\nn['sources'].append(W+\"Reconstruction:Proto-Indo-European/ḱlew-\") if False else None\n\n# node 6: note the Avestan adjective is reconstructed, the name is what is attested\nn=nodes[6]\nn['derivation']=n['derivation'].replace(\n \"is the exact equivalent of Vedic su-śrávas- and Greek eu-kleḗs, i.e. hu- 'good' (PIE *h₁su-) + the es-stem sravah- 'fame' of node 4.\",\n \"is the exact equivalent of Vedic su-śrávas- and Greek eu-kleḗs, i.e. hu- 'good' (PIE *h₁su-) + the es-stem sravah- 'fame' of node 4. (Strictly, what the Avesta attests is the vṛddhi-ed proper name Haosravah-/haosrauuaŋha-, glossed 'fair fame, good renown' and used of the Kayanian king; the plain adjective *husrauuō is reconstructed from it and from MP husraw — so Nourai's citation form hu-srav is a normalisation, not a quotation.)\")\nn['sources'].extend([\"https://en.wikipedia.org/wiki/Khosrow_(name)\",\n                     \"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/\"])\n\n# node 9: MacKenzie does lemmatise dušraw\nn=nodes[9]\nn['derivation']=n['derivation'].replace(\n \"The word is attested in the Pahlavi Šāyast-nē-Šāyast\",\n \"MacKenzie lemmatises it: 'dušraw [dwslwb] notorious, dishonoured' with the abstract dušrawīh 'dishonour, notoriety' — so the correct Middle Persian citation form is dušraw, not Nourai's hyphenated du-srav. The word is attested in the Pahlavi Šāyast-nē-Šāyast\")\nn['consulted'][1]={\"src\":\"PHD\",\"where\":\"MacKenzie 1971 s.v. dušraw\",\"stance\":\"supports\",\n \"note\":\"'dušraw [dwslwb] notorious, dishonoured; dušrawīh: dishonour, notoriety' — the Middle Persian word Nourai writes du-srav, standing in MacKenzie's large duš-/dus- compound series (dušox, dušxwaršt, dušgōwišn, dušdēn ...).\"}\nn['sources'].append(\"https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf\")\n\n# node 11: add Iranica's statement on sraoša and the sraoθra gloss\nn=nodes[11]\nn['derivation']=n['derivation'].replace(\n \"Nourai's double gloss 'ear, one who listens and follows' captures both nouns and both senses; the derivation from *ḱleu- is uncontested.\",\n \"Malandra in Encyclopaedia Iranica s.v. SRAOŠA puts it exactly so: 'It is derived from an s-extension of √sraw-/sru- \\\"to hear\\\" ... the basic meaning is \\\"to obey, be compliant\\\", that is, \\\"to hear and obey\\\"', comparing Ved. śruṣṭí- 'obedience' and Gathic a-srušti- 'disobedience'. Nourai's double gloss 'ear, one who listens and follows' therefore fits sraoša- well but is off for sraoθra-, whose Avestan sense is 'chanting, intoning' (cf. fra-sraoθra- 'singing, intoning'); 'ear' is the Sanskrit sense. The derivation of both from *ḱleu- is uncontested.\")\n\njson.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nopen(p,'a',encoding='utf-8').write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 -m json.tool data/verification/page-270.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 270"
}
```


### [2026-09-06T21:17:41.220Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 23/23
node verdicts: {'disputed': 6, 'plausible': 4, 'confirmed': 10, 'unverified': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'contradicts': 3, 'supports': 14, 'not_checked': 6, 'not_found': 1}
books consulted: {'partial': 11, 'contradicts': 10, 'supports': 38, 'silent': 7} | by book: {'HUB': 7, 'PHD': 7, 'KLN': 7, 'SKT': 6, 'BRT': 5, 'NYB': 5, 'MON': 5, 'ARY': 4, 'AHD': 3, 'POK': 3, 'CHEUNG': 2, 'HRN': 2, 'KNT': 1, 'FFD': 1, 'IEC': 1, 'SYN': 1, 'LKT': 1, 'DEV': 1, 'WEB': 1, 'FSD': 1, 'LEW': 1, 'LAT': 1}
```


## [2026-09-06T21:17:46.912Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,urllib.parse\nidx=set()\nfor l in open('data/verification/sources/web/index.jsonl'):\n    try: d=json.loads(l)\n    except: continue\n    u=d['url']; idx.add(u); idx.add(urllib.parse.unquote(u))\nd=json.load(open('data/verification/page-270.json'))\nused=set()\ndef coll(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': used.update(v)\n            else: coll(v)\n    elif isinstance(o,list):\n        for x in o: coll(x)\ncoll(d)\nmiss=[u for u in sorted(used) if u not in idx and urllib.parse.unquote(u) not in idx]\nprint('used',len(used),'missing',len(miss))\nfor u in miss: print(' MISSING:',u)\nEOF"
}
```


### [2026-09-06T21:17:48.773Z] TOOL RESULT

```
used 41 missing 1
 MISSING: https://en.wikipedia.org/wiki/Khosrow_(name)
```


## [2026-09-06T21:17:53.122Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wikipedia.org/wiki/Khosrow_(name)' --note 'page 270, root Kleu 1, node 6/8: attested Avestan Haosravah- vs reconstructed *husrauuo, Parthian hwsrw, Greek Osroes, Persian xosrow as common noun \"king\"' 2>&1 | tail -3"
}
```


### [2026-09-06T21:17:56.527Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/917e7a93c86dbcfa.txt
```


## [2026-09-06T21:17:59.019Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 tools/verify_check.py 270 && git status --short data/verification/page-270.json data/verification/sources/refs/ocr/BOOK/270.png"
}
```


### [2026-09-06T21:18:01.624Z] TOOL RESULT

```
nodes verified: 23/23
node verdicts: {'disputed': 6, 'plausible': 4, 'confirmed': 10, 'unverified': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'contradicts': 3, 'supports': 14, 'not_checked': 6, 'not_found': 1}
books consulted: {'partial': 11, 'contradicts': 10, 'supports': 38, 'silent': 7} | by book: {'HUB': 7, 'PHD': 7, 'KLN': 7, 'SKT': 6, 'BRT': 5, 'NYB': 5, 'MON': 5, 'ARY': 4, 'AHD': 3, 'POK': 3, 'CHEUNG': 2, 'HRN': 2, 'KNT': 1, 'FFD': 1, 'IEC': 1, 'SYN': 1, 'LKT': 1, 'DEV': 1, 'WEB': 1, 'FSD': 1, 'LEW': 1, 'LAT': 1}
?? data/verification/page-270.json
```


## [2026-09-06T21:18:25.073Z] AGENT

Page 270 (book p. 240), one entry, root **Kleu 1** = PIE \*ḱleu- "to hear" (POK 605). `verify_check.py 270`: 23/23 nodes, **0 PROBLEM lines**.

Verdicts — root: confirmed. Nodes: 10 confirmed, 4 plausible, 6 disputed, 2 transcription_suspect, 1 unverified.

Disputed:
- **#1 Avestan "sru 2, srav, xšnu, xšnaw"** — srav-/sru- is genuine, but xšnu-/xšnaw- belongs to PIE \*ksneu- "sharpen" (POK 585); and in Avestan xšnu- means only "propitiate, satisfy", the "hear" sense being Old Persian ā-xšnau-.
- **#2 Pahlavi ašnūdan** / **#3 Persian شنیدن** — from PIr \*ā-xšnau- < \*ksneu-, not \*ḱleu-. Nourai's own FFD:64 (Abolghasemi) reconstructs \*šnav/\*šnu, and his BQT:1304 (Mo'in) derives it from OP āxšnavamiy; Hübschmann p.82 says a root xšnū "sich nicht mit zd. sru vereinigen lassen würde". Only Horn 177 backs Nourai.
- **#8 Persian xosrow / xosor / xošū** — the chart's worst error. خسرو is right (< MP Husraw < \*hu-sravah-), but خسر/خسور "father-in-law" and خشو "mother-in-law" are from PIE \*sweḱuros / \*sweḱruh₂ (Av. x°asura-, Skt śvaśura-/śvaśrū-, Lat. socer/socrus). Horn no. 486-487 — on p.108, the very page Nourai cites — says so, as do Hübschmann p.213 and Mo'in's own footnote on BQT p.749. The trap is the homonymy of older NP xusrū "mother-in-law" with خسرو "king", which the Borhan merged in one article.
- **#14 Old Slavic Slověninŭ ← slovo** — Klein 1456 is quoted correctly, but Wiktionary/Slavistics now files this under "obsolete etymologies" and prefers a river-name base (\*Slovǫta), since \*-ěninъ attaches only to place names.
- **#23 English client ← cluere** — Watkins/AHD (the reference Nourai cites) puts CLIENT under \*klei- "lean"; Klein s.v. client: "The usual derivation of L. cliens from the stem of cluere ... is erroneous."

Transcription_suspect (both `error_in: "book"` — the printed page matches the JSON, verified on a 300-dpi render saved to `data/verification/sources/refs/ocr/BOOK/270.png`):
- **#15 Middle Greek "slabnovus"** → should be Σκλαβηνός (Sklabēnós); Klein's form, with the k dropped and a Latin -ovus ending.
- **#16 Middle Latin "slavous"** → should be Sclavus / sclavus.

No extraction errors found — every form checked against the page image matches the JSON, including the empty box #10 (a genuinely blank rectangle with no language label).

Other notes worth the owner's eye (recorded in the file, not verdict-changing): #7's Pahlavi gloss "title of kings **and in-laws**" has no support in any Pahlavi dictionary; #11's "ear" is the Sanskrit sense of śrótra-, Avestan sraoθra- means "chanting"; #4's "sraw/srâw" are Old Iranian/Middle Persian stems, not Avestan; #19's route via French is right for *slave* but wrong for *Slav*, *Yugoslavia*, *Czechoslovakia*.
