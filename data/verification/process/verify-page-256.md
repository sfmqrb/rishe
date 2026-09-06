# Verification process log — verify-page-256


## [2026-09-06T16:13:16.801Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 256 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-256.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-256.json. Write /home/sfmqrb/git/rishe/data/verification/page-256.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 256` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:13:18.500Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T16:13:19.210Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:13:19.225Z] TOOL RESULT

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


## [2026-09-06T16:13:19.519Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-256.txt"
}
```


### [2026-09-06T16:13:19.540Z] TOOL RESULT

```
1	=== PDF page 256 (book page 226) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ker 1 : head, horn  (refs POK:574; KLN:261,657)
4	#1 (parent #0) [Avestan] refs=AHD; POK:574; KLN:261 | sarah, sârah : head
5	  #2 (parent #1) [Pahlavi] refs=None | 
6	    #3 (parent #2) [Persian] refs=BQT |  | extra: سر ، افسر ، ساربان
7	سردار ، سالار ، سرشار
8	#4 (parent #0) [Avestan] refs=POK:574; BRT:1650; LEW:905 | srŭ 1, srvâ 1 : head, horn, nail ; srŭ-bhara, srvara : carried on the head, horn ☞Bher 1
9	  #5 (parent #4) [Persian] refs=BQT:1130; HRN:162 | sorŭ, sarŭn «سُرو ، سَرون ۱» : horn
10	#6 (parent #0) [Greek] refs=KLN:237 | keras, keration : little horn, also referred to the horned-shaped fruit of the carob tree
11	  #7 (parent #6) [Arabic] refs=KLN:237; TAD:60 | qirat : fruit of the carob tree which was used as a unit of weight.
12	    #8 (parent #7) [Persian] refs=None | qîrât «قیراط»
13	    #9 (parent #7) [Middle Latin] refs=None | 
14	      #10 (parent #9) [French] refs=None | 
15	        #11 (parent #10) [English] refs=None | carat
16	  #12 (parent #6) [English] refs=None | rhinoceros
17	#13 (parent #0) [Greek] refs=AHD:831 | hemi-kranion : pain in "one half of head"
18	  #14 (parent #13) [Latin] refs=None | hemi-crania
19	    #15 (parent #14) [French] refs=AHD:831 | migrene : headache
20	      #16 (parent #15) [Persian] refs=MON:4503 | mîgren «میگرن»
21	      #17 (parent #15) [English] refs=AHD:831 | migraine
22	#18 (parent #0) [Different Languages] refs=AHD | 
23	  #19 (parent #18) [English] refs=None | carrot, cheek, corner, horn
24	#20 (parent #0) [Sanskrit] refs=AHD:1522; KLN:657 | srnga : horn ; sringa-vera : horn-shaped root of ginger
25	  #21 (parent #20) [Pahlavi] refs=VDQ:42 | šanga-vîr, singiber
26	    #22 (parent #21) [Persian] refs=MON:1751; VDQ:42 | šangabîl «شنگبیل» : ginger
27	  #23 (parent #20) [Pali] refs=KLN:657 | singivera : ginger
28	    #24 (parent #23) [Greek] refs=KLN:657 | ziggiberis : ginger
29	      #25 (parent #24) [Arabic] refs=VDQ:238 | zanzabîl : ginger | NOTE: From Greek through Syriac.
30	        #26 (parent #25) [Persian] refs=MON:1751; VDQ:238 | zanjebîl «زنجبیل» : ginger
31	      #27 (parent #24) [Latin] refs=KLN:657 | gingiber, zingiber, zinziber
32	        #28 (parent #27) [Old French] refs=KLN:657 | gingiber, gingiver
33	          #29 (parent #28) [English] refs=AHD:667; KLN:657 | ginger, gingerale
34	--- entry 1 ---
35	ROOT Ker 2 -> redirect to Sek
36	
```


## [2026-09-06T16:13:22.743Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-256.json",
 "description": "Read page 256 source JSON"
}
```


### [2026-09-06T16:13:22.776Z] TOOL RESULT

```
{
  "pdf_page": 256,
  "book_page": 226,
  "entries": [
    {
      "root": {
        "name": "Ker 1",
        "lang": "Indo-European",
        "refs": "POK:574; KLN:261,657",
        "gloss": "head, horn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AHD; POK:574; KLN:261",
          "words": [
            {"translit": "sarah, sârah", "gloss": "head", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT",
          "words": [],
          "script_extra": "سر ، افسر ، ساربان\nسردار ، سالار ، سرشار",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:574; BRT:1650; LEW:905",
          "words": [
            {"translit": "srŭ 1, srvâ 1", "gloss": "head, horn, nail", "script": null},
            {"translit": "srŭ-bhara, srvara", "gloss": "carried on the head, horn", "script": null, "see": ["Bher 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:1130; HRN:162",
          "words": [
            {"translit": "sorŭ, sarŭn", "gloss": "horn", "script": "سُرو ، سَرون ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "زپیشانی هر یک از مرد و زن - سَرونی است برُسته چون کرگدن",
            "poet": "Nezâmî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:237",
          "words": [
            {"translit": "keras, keration", "gloss": "little horn, also referred to the horned-shaped fruit of the carob tree", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": "KLN:237; TAD:60",
          "words": [
            {"translit": "qirat", "gloss": "fruit of the carob tree which was used as a unit of weight.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "qîrât", "gloss": null, "script": "قیراط"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Middle Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "carat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "rhinoceros", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:831",
          "words": [
            {"translit": "hemi-kranion", "gloss": "pain in \"one half of head\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "hemi-crania", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": "AHD:831",
          "words": [
            {"translit": "migrene", "gloss": "headache", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:4503",
          "words": [
            {"translit": "mîgren", "gloss": null, "script": "میگرن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": "AHD:831",
          "words": [
            {"translit": "migraine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Different Languages",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "carrot, cheek, corner, horn", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:1522; KLN:657",
          "words": [
            {"translit": "srnga", "gloss": "horn", "script": null},
            {"translit": "sringa-vera", "gloss": "horn-shaped root of ginger", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Pahlavi",
          "refs": "VDQ:42",
          "words": [
            {"translit": "šanga-vîr, singiber", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "Persian",
          "refs": "MON:1751; VDQ:42",
          "words": [
            {"translit": "šangabîl", "gloss": "ginger", "script": "شنگبیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 23,
          "parent": 20,
          "lang": "Pali",
          "refs": "KLN:657",
          "words": [
            {"translit": "singivera", "gloss": "ginger", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 24,
          "parent": 23,
          "lang": "Greek",
          "refs": "KLN:657",
          "words": [
            {"translit": "ziggiberis", "gloss": "ginger", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 25,
          "parent": 24,
          "lang": "Arabic",
          "refs": "VDQ:238",
          "words": [
            {"translit": "zanzabîl", "gloss": "ginger", "script": null}
          ],
          "script_extra": null,
          "note": "From Greek through Syriac.",
          "quote": null
        },
        {
          "id": 26,
          "parent": 25,
          "lang": "Persian",
          "refs": "MON:1751; VDQ:238",
          "words": [
            {"translit": "zanjebîl", "gloss": "ginger", "script": "زنجبیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 27,
          "parent": 24,
          "lang": "Latin",
          "refs": "KLN:657",
          "words": [
            {"translit": "gingiber, zingiber, zinziber", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 28,
          "parent": 27,
          "lang": "Old French",
          "refs": "KLN:657",
          "words": [
            {"translit": "gingiber, gingiver", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 29,
          "parent": 28,
          "lang": "English",
          "refs": "AHD:667; KLN:657",
          "words": [
            {"translit": "ginger, gingerale", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ker 2",
        "redirect": "Sek"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T16:13:23.196Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:13:23.233Z] TOOL RESULT

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


## [2026-09-06T16:13:57.884Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','BRT','LEW','BQT','HRN','TAD','MON','VDQ']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700]); print()\n\""
}
```


## [2026-09-06T16:13:58.283Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,60p tools/verify_check.py"
}
```


### [2026-09-06T16:13:59.826Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghboo
```


### [2026-09-06T16:13:59.871Z] TOOL RESULT

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


## [2026-09-06T16:14:05.158Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==583' POK_01.txt | head -80"
}
```


## [2026-09-06T16:14:05.455Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ker-1\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T16:14:06.932Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T16:14:06.971Z] TOOL RESULT

```
618:ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
947:skribh-. To cut, separate, sift. Extension of sker-1. 1. Latin scribere, to scratch, incise, write: SCRIBBLE, SCRIBE, SCRIPT, SCRIPTORIUM, SCRIPTURE, SERIF, SHRIVE; ASCRIBE, CIRCUMSCRIBE, CONSCRIPT, DESCRIBE, INSCRIBE, MANUSCRIPT, POSTSCRIPT, PRESCRIBE, PRO- SCRIBE, RESCRIPT, SUBSCRIBE, SUPERSCRIBE, TRAN- SCRIBE. 2. Greek skariphos, scratching, sketch, pencil: SCARIFY}, [Pok. 4. sker-, Section II. 945.]
1230:ALOFT an!, leup- ALONE oi-no- ALONG §ant- ALOPECIA wip-é- ALPENHORN ker-1 ALPENSTOCK (s)teu- ALPHOSIS albho- ALSO al-5
1232:ALTER al-1 ALTERCATE al-1 ALTERNATE al-1 ALTHEA al-3 ALTHORN  ker-1 ALTIMETER al-3 ALTITUDE al-3 ALTO al-3 ALTOCUMULUS _al-3 ALTOSTRATUS _al-3 ALTRICIAL al-3 ALTRUISM al-1 ALULA aks- ALUMNUS al-3 ALVEOLUS aulo- ALWAYS wegh- ALYSSUM wikwo- AM es-
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1335:-CARPOUS kerp- CARPUS kwerp- CARRION sker-1 CARROT ker-1 CARRY kers-2 CART ger-2 CARUNCLE = sker-1 CARVACROL ak- CARVE gerbh- CASCADE kad- CASCARA kwét- CASE! kad-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1344:CHAP2 caupd CHAPITER kaput CHAPMAN caup6 CHAPTER kaput CHARACIN gher-4 CHARACTER gher-4 CHARD kars- CHARGE kers-2 CHARIOT kers-2 CHARISMA gher-5 CHARITY ka- CHARIVARI ker-1 CHARM! kan- CHARNEL sker-1 CHARY gar-
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1366:CIVIL kei-1 CLADOCERAN kel-1, ker-1
1370:CLAN plat- CLANDESTINE kel-2 CLANG kleg- CLASMATOCYTE kel-1 cLass kele-2 CLAST kel-1 CLasTIC kel-1 CLATHRATE kleu-3 CLATTER gal-2 CLAUSE kleu-3 CLAVATE kleu-3 CLAVICHORD kleu-3 CLAVICLE kleu-3 CLAVICORN ker-1, kleu-3 CLAVIER kleu-3 CLAVIFORM kleu-3 CLAW gel-1
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
```


## [2026-09-06T16:14:12.997Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 580 581 582 583 584; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -5; done"
}
```


## [2026-09-06T16:14:13.802Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"keras\" POK_full.txt | head -20; echo ---; grep -n \"srū\" POK_full.txt | head"
}
```


### [2026-09-06T16:14:14.691Z] TOOL RESULT

```
=== leaf 580 ===
=== leaf 581 ===
=== leaf 582 ===
=== leaf 583 ===
=== leaf 584 ===
```


### [2026-09-06T16:14:14.791Z] TOOL RESULT

```
3625:Old Irish a{/)cher' sharp (from the hoist)', because of the Gen. Sg. Akeras{PH in the 
46270:ablaut. Lithuanian keras^ hoher, verwitterter Baumstumpf; Staude ', keretr shoot in the 
50617:keras-\r\ gr. Kspac; 'horn' (Gen. ep. Kspaoc;, Attic -wc;, newer -aroc;, later Epic -aaroq) 
50677:Latin cerebrum^ brain ' {*keras-ro-m, compare gr. Kopapa); cervTx^ nape ' {*cers-vTc-)\ 
---
```


## [2026-09-06T16:14:17.587Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo -n \"$f pages=\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f; done"
}
```


## [2026-09-06T16:14:18.220Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '50590,50700p' POK_full.txt"
}
```


### [2026-09-06T16:14:19.517Z] TOOL RESULT

```
POK_01.txt pages=363
POK_02.txt pages=433
POK_03.txt pages=429
POK_full.txt pages=1
```


### [2026-09-06T16:14:19.560Z] TOOL RESULT

```
"head' (in the 2. syllable not genau = gr. Kspaqfrom Rera-siroru the heavy basis; 

the reduplication-grade of the first syllable, instead of *saras-, is carried previously by Indie 

or Proto Aryan from preceding Old Indie Gen. sFrsnah etc.), Gen. Old Indie sTrsnali, Abl. 

sTrsataii ( *Rrsn-tos : gr. KpaaTO(;); 



sriiga- {*Rr-n-go-) n. "horn', of /7-stenn *Rer-{e)n-\N\Vc\ perhaps originally bare nominative 
g, compare gr. KpayY^v 'crab' and from the i^basis gr. Kopu-YY-£Tv Kspari^Eiv (see also 
under about Irish congan); 

from the ^-basis Avestan sru-, srva-' horn; nail in fingers and toes ', srvara ^horned ' 
( *sru + bhara-), srvT-stay- " with horny barbs '; 

Armenian sar'height, acme, apex, slope' {Rero-); 

gr. Kap in hom. sni Kap ' on the head ', Hippokr. avaKap " up to or towards the head, 
upwards', originally probably *RerQeu. *Rer-ds {Kapoq), from which analogical Kap, Kopoc;; 
besides Kapa, Ionian Kapn " head'; an s- loose stem Kop- is decisive forsy-Kapoq (and a- 
Kapo(; with a- as zero grade to £v), ly-Kp-oq ' brain '; 

perhaps here Ionian KopTc;, -'iboq, Attic mplq, -Iboq f. " a shrimp or prawn ', Doric Kwpic; 
Koupi(; ds.; 

keras-\r\ gr. Kspac; 'horn' (Gen. ep. Kspaoc;, Attic -wc;, newer -aroc;, later Epic -aaroq) 
see below Latin cerebrum, 

*Kapaa- {*Reras-) in: Attic Kapa "head' (n. *Rer9S-n> *Kapaa), Ionian Kopn ds., oblique 
stem *krasn- (with -qt- for -/?-) Aeolic Gen. KpaoTOc;, out of it Kparoc;; hybridism are 
KapnaTO(; and Kapr|TO(; (*Kpc(av- = Old Indie sTrsn-); KOpnap; in addition KapouoGai ' sich 
schwer im Kopfe fijhlen '; hom. Kapnva Nom. PI. ' heads, mountain summits ' (secondary 
Sg. KQpnvov, Attic Doric Kopavov, Aeolic Kopavvo-), basic form *Kapaava PI.; compare M. 
Leumann Homer. Worter 159. 

Kapapa KscpaAr) Hes. (*Kapaa-pa; therefrom Kapcipwv, father of Kapavo(;); 

about Kpri5£|jvov, Doric KpaSsfjvov ' head fascia ' s. Schwyzer Gl. 12, 20; about hom. 
KaTOKpnGEv (= kqt' aKpr|6£v) s. Leumann Hom. Worter 56 ff.; 

perhaps Kpaaivw ' accomplish, complete, perform, execute, achieve, finish, fulfill '. If 
KpainaAr) " drinking-bout, intoxication, drunken headache ' is to be understood because of 
Latin crapulaas KpaiTraAr) ' drinking-bout, intoxication, drunken headache ' (in 2. part then 
naAAw), Kpa[a]i- could stand beside *Kapaa-pc(, as adjective e.g. Ku5i-av£ipa besides 
K05p6(;; 



*Kpaa- ( */cr9s-or *Kpaa-, *k/s-) in Attic KpaarrsSov " edge, border, skirt, esp. of cloth, 
Theoc.2.53; of the fringe or tassel worn by Jews, affection of the uvula, fimbria '; ajjcpi- 
Kpc(vo(; (*Kpaa-vo-) ' two-headed '; 

alb. Geg {*karena) krena, Tosc krereP\. ' heads', shqipja me dy krena^ double headed 
eagle', krye^ head' a Greek loanword (common alb. -n- > -r-), alb. krenar^ proud', kreu^ 
beginning', (through metathesis) i^kreu) krye^ head'. 

alb. Geg krena PI.' heads' = gr. neut. nom. pi. ionic apcpi-Kpnva " two-headed '. 

gr. EKOTOY-Kpavoc; " 100 headed ', Ionian sniKpnvov K£(paA65£a|Jov Hes., Attic Kpaviov 
"cranium', 6A£[vo]Kpavov, wAsKpavov 'elbow'; Kpavi^ai ettI KscpaAnv anoppTujai Hes. next 
to which with lengthened grade (: K£pa(;) Kspavi^ai KoAuppnaai Kupiarnaai Hes., vau- 
Kpc(pO(; ' the chief official of a division, of the citizens for financial and administrative 
purposes' (diss. vau-KAapoq, -KAr|po(;), Boeotian AaKpapiSaq from *Aa-Kpc(po(; " head of 
people '; in addition KpaTpa f. 'head', nijiKpaipa etc. (from *Kpaa-pia); 

ograde *Kopa- in Ionian Kopar), Attic Koppn, Doric Koppa " temple, flattened region on 
either side of the forehead, head' (Indo Germanic *kors-)\ 

of -(e)/^stem Rei{e)n- : Kpavo(; 'helmet' ( *krno-s)\ Kapvo(; ... pooKniJa, rrpopaTov Hes.; 
Kspvai, K£pva PI. 'transverse processes of the vertebrae' {*kern- or *kers-n); Kpayv^v 
'crab' (compare above Old Indie srhga-); unclear is the formation from Kspajjpu^, -uko(; " 
stag-beetle '; KapapO(; m. ' horned or cerambycid beetle, a prickly crustacean, crayfish, a 
light ship ' (> Latin carabus ds.), perhaps with maked. (?) derivative (gr. *-(poc;) to Kopic; ' 
shrimp (Crangon) and prawn (Palaemon) ', see above; but all doubtful. 

Von Rereu-: K6pu56(; m., f. ' crested lark ' (: Germanic herut- 'deer'); Koput;, -uQoc, 
"helmet', hom. Kupa Kopuaasrai " rears up ' K6pufjpO(;, Kopucpn ' acme, apex ', Kopunru) " 
butt with the head, the horns ', KopuyyETv Kepari^siv Hes. (to -yy- see above to sriiga-). 

Von Rerei- . KpT6(; "aries, ram' (compare in the meaning K£paaTn(;), ablaut, with Old 
Norse hreinn. Old English hran " reindeer '. 

Vereinzeltes: Koprriv rpv pouv. Kpr|T£(; Hes. (if *kr-ta^ the horned '); KupiiTU), Kupnpa^co 
" butt with the horns, like goats or rams ' (as Kopunru); *kor-)\ 

Latin cerebrum^ brain ' {*keras-ro-m, compare gr. Kopapa); cervTx^ nape ' {*cers-vTc-)\ 
cernuus, cernulus^ turning a somersault, stooping forwards, head-foremost ' ( *kers-nouos, 
if not rather loanword from gr., compare Kspavi^ai), cr5i6>/io "hornet' (see below). From (e)n- 



stem: cornu 'horn' (the i/-stem perhaps as gall. Kapvu^; " trumpet ' through amalgamation 
of /7- and ^stem); compare also lllyrian PN TpiKopviov (Moesia), PN Corn u/Jn us etc. 
(Krahe IF. 58, 222 f.) from */<m-; 

to crabro' hornet ' {*crasrd, Rerasron-) is placed (Indo Germanic fqs-en^: 

Maybe nasalized alb. ( *kerenza), grenze, grereza, grere, greth " wasp ' (common k- > g- 
gutturals in Celtic Baltic), (common alb. Tosc -n- > -/■-). 

Old High German hurnuz, hornaz, m., Old English hyrnet(u)^ hornet ' {*hurznuta)\ Dutch 
horzel{*hurzla-). Modern High German Horlitze; 

Lithuanian sirsei., s/rs/ysm., sirsuolis, old s/rsuo^ wasp', sirsuonas, sirsunas^ hornet ', 
Latvian sirsis. Old Prussian sirsilis " hornet '; 

russ. -Church Slavic (etc.) strtsenb " hornet, gadfly, brake', serb. srsljen " hornet '; 
compare Buga Kalba irsenove 11 91, 224;
```


## [2026-09-06T16:14:23.748Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '50540,50592p' POK_full.txt"
}
```


### [2026-09-06T16:14:23.804Z] TOOL RESULT

```
References: WP. I 427, Trautmann 305. 
Page(s): 583 

Root / lemma: Rers-2 
Meaning: to run 



Material: For palatales /^speaks aapaai apa^ai Hes., as Latin sarracum, serracum{\\.a\\aw 

-rr- from -as-) ' a foreign chariot ' could have originated lllyrian *sarsa = Indo Germanic 

*/(rsa; 

Note: [^->s-satem: Maybe pre-lllyrian substrate satem?] 

gr. £niKoupo(; "to help hurrying' ( *Rorsos); 

Note: 

The inanimate suffix -ur- . gr. sniKOupo^ "to help hurrying' : UAupioi , oi, lllyrians, UAupia , 
n, lllyria, also'lAAupi? , n, Adj. 'lAAupiKO? , n, 6v, lllyrian: -Kr|, the region or province of lllyria, 
lAAupi^O} , speak the lllyrian language, 'IAAupia:~hence Adv. lAAupiaTi. 

Latin curro, -ere "run' ( *Rrsd), cursus "run, flow', currus " cart ', equirria " chariot race ' 
{*equi-curria, from which assimilatorisch *equi-quirria av\6 Haplologic equirria); 

gall, carros. Latinized carrus^ carriage, cart ', Old Irish mcymr. carr, bret. /ra/r" biga, 
vihiculum ' {*l<rsos)\ compare mcymr. carrawci., ncymr. carrog^ torrent, stream ' {*l<arsal<a 
" the running '?), different above S. 532. 

alb. l<arroce^ cart' a Latin loanword. 

Middle High German hurren^ move quickly '; doubtful Old High German hros, -ses. Old 
Icelandic Old Saxon fiross. Old English fiorg^ horse, steed' {*hrussa-). Old Low German 
tiers 6s. {*fierssa-), because -s5-from one has understood in -sauslaut root maximally as 
consonant increase in a shortened name; hence rather to a dental extension (: Old Indie 
l<ijrdati^ hops, jumps ') the not palatalen root (s)l<er- "spring'; 

Armenian l<afl<'^ cart ' is probably loanword from Galatian. 

References: WP. I 428 f., WH. I 315 f. 
Page(s): 583-584 

Root / lemma: Rer-, Rera- : Rra-, Rerei-, Rereu- 

Meaning: head; horn, cow 

Material: Old Indie siras-u. (ved. only Nom. Akk.) "head, cusp, peak', Avestan saraii-u. 

"head' (in the 2. syllable not genau = gr. Kspaqfrom Rera-siroru the heavy basis; 

the reduplication-grade of the first syllable, instead of *saras-, is carried previously by Indie
```


## [2026-09-06T16:14:28.887Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=50576 && NR<=50900 && /Page\\(s\\)|Root \\/ lemma|References:/' POK_full.txt | head -20"
}
```


## [2026-09-06T16:14:29.456Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"1650\" BRT.txt | head -20"
}
```


### [2026-09-06T16:14:30.855Z] TOOL RESULT

```
References: WP. I 428 f., WH. I 315 f. 
Page(s): 583-584 
Root / lemma: Rer-, Rera- : Rra-, Rerei-, Rereu- 
Wrong etymology because alb. kau'ox' : Rumanian bou'ox' derived from Root / lemma: 
References: WP. I 403 ff., WH. I 164, 203 f., 206, 207, 276, 283 f., 284, 856, 858, 
Page(s): 574-577 
Root / lemma: Res- 
References: WP. I 448 f., WH. I 167, 178 ff. 
Page(s): 586 
Root / lemma: /ceub- 
References: WP. I 380 f. 
Page(s): 595 
Root / lemma: Reuk- 
References: WP. I 378. extension from Reu-2. 
Page(s): 597 
Root / lemma: /ceuR- RuR- 
References: WP. I 377, WH. I 218 f. 
Page(s): 597 
Root / lemma: Reu-1, Reus- : Ru- Rua-
```


### [2026-09-06T16:14:30.894Z] TOOL RESULT

```
27471:1650
```


## [2026-09-06T16:14:34.034Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27440,27530p' BRT.txt"
}
```


### [2026-09-06T16:14:34.079Z] TOOL RESULT

```
•rqm  Ytj.  128;  —  'rfm  vastrpm  Vd. 20';  —  va%r»m  *r?m  Yt  lo.  13a;  —  'ra uru^mJs  Yt.  13.  55;  —  yä  bari%ri  paraei 'raie  ".  .  des  vielen  Schönen"  YL/j.  9; —/r3  '«(APa)  *2u/  sispata(Sp.i6oj  o.) "pülcritudines  . ."  Yt.j,  7.  a)  'schtin anzuhören,  schön':  'rät/ namqnY.iß.i; Vi.  6.1;  —  uxhitn  'nm  T.jL;  —  'ra uxla  vaÜ  V.  2.  10  PüZ.;  —  'ra  (ISt) dahma  sfriiiY.22.^,  Unklar:  *'°nm''^ arvdu/Mmtt.Ösi?).  Wertlos:  -rä p^nss ähyala  Vyt,_jj.
KompA.,  E.J  Ableit.  —  Zu  iräy  f.  —  VgL srayah-,  sratsla-.  —  ai.  Irilä-,  'irlrä-  Adj.  — Fu. :  ntviai,  newak  pa  dilan,  nfwai  miäs.  — ')  Hds.  irira.  —  ')  Hds.  srir^m  und  irim,
•  y  sriraoxian-  m.  EN.  eines  Gläubigen : 'xfnS  aiaom  YL  y.  loi.
Komp.:  stira--{-ux!an-,  eig.  "ichane  Stiere habend'.
•  j.  srirä'vaohav-  m.  EN.  eines  Gläubigen : 'vaniSui  aiaoia  Yt.  J>  118.
Eig.  'schön  und  jut,  Kaktiiaia%ii' ;  vgl.  nnler m^idrÖTiaiiAav:
•  j.  aiirö.tara-  Adj.  (fem.  'rs-)  'der schönere' :  äal  mam  .  .  snram  haitlnt °ram  .  .  H.  2. 14.
kompar.  ans  srira-.  -~  Pfl.:  nniailar.
•  j.  srü-,  srvä-'>  f.  i)  'Nagel'  der  Finger und  Zehen:  paiti  te  m>rrfa  aiS^su/la  (sd.) ima  'va  (AP.)  va^ayant  V./7.9;  9;  — imsn  ts  'vh  minya  aisxt/fa  kyär»  arlta- yaslä  . .  "diese  Nägel  sollen  dir,  0 Vogel  A.,  als  Speere  dienen  . ,"  V.  17. 9; 10.  a)  Du.  '(beiderlei  Nägel  sva.)  die Nägel  der  Hände  und  FÜsse">:  yat  tarn ..varasasla  *hqm.räsayaj3ha ..  'vaf{AD.)ca *upa.%W3nsanAa  "wenn  du  dir.. und  die Nägel  zuschneidest"  V.  ij.  4;  —  ir  (Sp. 6a I  o.)  aisqm  paiti  *srvi  (AD.)'*  a^a äruxf  . .  upa.dvqtaiti  "auf  deren  Nägel kommt  ,.  herzugeflogen"  V.  7.  a4,  37,  g, 41;^.  14  (vio  sruye)**;  —  srvabya  marfim ava.kanSi/  "du  sollst  für  die  (abgeschnitte- nen) Nägel  ein  Loch  graben"  V.  ly. 7.  a)  'Hom'  der  Tiere  (und  tierähn- lichen Wesen,  s.  Komp.):  gSu/  .  .  yim upairi  sntye  (AD.)*'  sanal  (Sp.  1590  o.) amö  Yt,  14.  7.  a)  Piur.  mit  Aafia  Name eines  Sternbilds  (?) :  nitbayemi  m^ntuiSp. iiT4  0.)..nizbayemi  kapta  sraps  {AP.)i^ b.imya  V. /p.  4a,  3)  'Hom'  als  Stoff, 'Homstück'  (nur  Komp.  und  Ableit).
KompA.  (s.  auch  srvt.'),  E.;   Ableit.    —    np.
lurü  'Horn';  nbal.  vgl.  iruaie  Huf.  — Pa.s  irüv;  s.  noch  No.  $.  —  ')  D.  L  srui-'i irü-  wird  in  die  ö-DekL  überführt.  —  »)  Oder auch  der  beiden  Hände;  s.  Dbr.  V^S.  i, 143.  —  i)  NA.  h»t  dRn.  irvf,  srvf,  irnit;  s. aber  die  Var.  Vgl,  auch  srvT.itäy.  —  4)  D.  L inaie  [S  36S,  19),  die  them.  Form  gegenüber irvT.  —  5)  Pü. :  fehlt.
•  j.  srui-  Adj,  'hörend'.
KompA.,  E.  —  Zum  V.  irav —  ai.  'im/-,  imf.
—  5.  auch  zD  aimlim.
•  j.  sruta-"  Adj.  (fem.  •«-)  i)  'gehört*; a)  sva-  'dass  es  gehört  wird,  hörbar*  1  a/ijrs va  hl  dahmB  'tS  g-ä^S  da^aiti  *ratufril asruts  (sd.)  (arahtfril)  N.  25.  b)  sva. 'von  dem  man  hört,  bekannt,  berühmt': akurS  matdh  . .  Hö  atryene  ''vaijahe  . . yitnl!  xlaäB ..'IS  atryene  *valjaie  V.2.20; Y.p.  14;  —  'ta  F.  12.  j)  'zu  Gehör gebracht,  aufgesagt':  s.  srav-  Sp.  1641  o.
KompA.,  E.  —  PPfP.  tum  V.  trav.  —  ai. imtd-  Adj.,  mp.  srüt,  —  Fn.  (lu  1  a):  srüt, (iQ  I  b):  nämli,  {zu  3):  s.  Sp.  16*3,  No.  ig. 33,  35.  —  >)  Mit  H  V.  2.  30,  Y.  p.  14  und im  Komp.  nxit/rä  und  vT.
•  j.  srütatfaSri-  f.  EN.  der  Mutter  des Ux^atjrsta  (sd.)*':  katiyä  'f^ryS  a/acnyä YL/J.141.
*)  lodern  «ie  im  See  K^aaya  badend  von  dem dort  aufbewahrten  Samen  Zara%uitras  befruchtet wird;  s.  unter  xhidra-,  wo  Litt.
Eig.  'die  einen  berühmten  Vater  hat'<);  statt irula-f  nach  dem  Muster  von  tridaf-fAri-, JusTl  NB.  31 1.  —  «)  Im  Mp.  niflüf  fit,  SEE. *-.  105.
•  j.  srutay-  £  'Zugehörbringen,  Vortrag*. KompE.  —  Zum  V.  trav-,  —  ai.  itütay-  f. 'Hören  (nsw.)".
•  j.  trütar-  m.  'der  hört'  oder  'der  zu Gehör  bringt'.
KompE.  (in  EN.).  —  Zum  V.  srav-.    —  VgL
•  j.  *srutö.sp5da-'>  m.  EN.  eines  Gläu- bigen, Bruders  des  Wnzav.  TTTtvi  'ää (GD.)'J  aiaonä  "des  ff.  und  des  Sp.,  der beiden  . ."  Yt.  13. 1 1 5.
Eig.  'der  ein  berühmtes  Heer  hat  {Lmkarf  St.
—  ')  So  F  1 —  J)  Uothero.  —  ii  Eine  priester- liche  Deutung  Dk.  7.  7.  8.
•  g.  srüidyäi  Inf.  'zu  hören,  zu  verneh- men': vai)  sr°  hyat  marstaÜbyS  vahisttm "als  das  Wort,  das  zu  hören  den  Men- schen das  beste  ist"  Y.  4I5. 5 ;  —  sf  masdä /rävaocä  'tu  kund,  o  M.,  dass  man  es höre"  Y.,9^.  12.
mit  frä  in  pass.  Sinn  'audiri,  so  zu  wer- den,  dass  man  davon  hört,   bekannt  zu
dby  Google
i649
srutgaoäa-
zaenay-
1650
werden':  yS  . .  kv5  nä  */rair''^  *gnhwö "wer . .  er,  der  würdig  ist,  dass  man  von ihm  höre"  Y.46^,  13;  —  i!  vä  */rasr'''1 vasti  "oder  wer  will,  dass  man  von  ihm höre?"  Y.4^.  14.
Zum  V.  jrav-.  —  PQ,  (lu  Y.  ^j):  iräjiffn  da- hiJHlh,  (tn  y,  24)-  nigSSem,  SC;  ifnimi,  {lu Y.  46):  frac  sräyüit  dahibüh.  —  ")  ^k./irasr', s.  Var.
•  j.  srutgaoSa-  Adj,  'des  Ohren  hören, scharfhörig"':  mt^raiaf  .  .  °lS  hazanra.- yaoxsHS  YtJO.107;  19.35.
KoinpE.i  Ableit.—  Vgl  m.  h-ütiar^a^  Adj.
•  ]'.  snitgao^.'t^ma-  Adj.  'des  Ohren am  besten  hören,  der  am  besten  hört' a^arn  nafstMn  . .  yd  . .  'mS  asH  yezimnö (sd)  Yt  75.52.
•  j.  surunvata-  Adj.  'hörbar,  laut*:  hm yasai  °ta  yasna  sraoSifn  .  .  taokräiyU  Y. 57-3;  Vt.^.i8,  s.<).
FFP.  zum  V.  srav;  ^x,t  dem  Praes.  lo  turumi^ gebildet,  %  30fi.  11.  —  Pil.:  tiigöHhtömatid, Npü. :  Sunüda.
•  g.  suninvant-  Adj.  'belehrt,  gelehrt': 'Vatas(AP.)cä  asurunvatascä  '^■35.  4.
KompE.  —  PPA.  lum  V.  srav- ;  mm  Praes.  lo i»mfn^,eig. 'hörend,  lernend',  näml.  die  heilige Lehre.    —    Pü,!    äsnaväi  -  Sü.!    Initavän  -, eil. :  iui  fhtpaiisiän  Marl  iitcl. j.  srärim  N.  65:  lies  srlrim.
•  j,  srva-  n.  'Blei;  Gefäss  aus  Blei'; ayanhaintm  v3  °rttm  **  va  rättma  (sd.) xsa^ra  vairya  "in'>  einem  Gefäss  aus Eisen    oder   aus  Blei  . ."  V.16.6;  5.14;
— jr^i  'rum''>  jiai/iMHc^i {sd.)  V.p,  14;  — ildrun/aydiJ'  aom  'rum''>  paurva.raemäi (sd.)  . .  Y.g.  14.
Pü.  (lu  V.p.  14  3.St.):  truf,  (sonst)  snifi».  — '}  S.  Sp.  S9S  m.  mit  No.  1.  —  «)  D.  L  *sru-
•  j.  STvaena-  Adj.  'hörnen,  aus  Hom  be- stehend': 'na  a^qm  fnäml.  aurvatqm)  sa- fäahs  saranya  paiti%waritar3ks  (sd.)  Y. 57-2  7-
Ableit  aal  jr «-.  —  Pü. :  snrven  ').  —  ■)  Nicht 'bleiern',  vgl.  Pü.  zu  V.  p.  14  und  Hbm. PSt.  74-
•  j.  srvant-,  sravant-  "  Adj.  'schleichend, anschleichend':  -afa/J  (GS.)  F. /^.
mit  upa  'sich  (wie  ein  Raubtier)  heran- schleichend': sjmö  Cdcs  Winters')  ..  'vats V.  7.  37.
PPA.  am  ar.  'tsrau-,  einer  »-'Enreitcrung* (Prael.  20)  uis  *lsar.  in  u.  tsaraä  'er  (be> schleicht' ;  vgl.  iravuahav-  und  ai.  tiärav-  m. 'schleichende»  Tier';    femer  lU  aBvijrü%ra:
S.  lEt.  Bthl.  IF.  p.  276;  femer  Bloomfield IK.  4.  72.  JAOS.  z6.  CHX,  OsTMOFF  BB.  33. 257,  Flensburg  Stud.  7.  —  Pü.  tiu  F.):  äSiiip *Ha»t,  Aufregung',  (lu  V.):  <^>ar  Ut3p  kar, erL  I  Ssän  anilrth  hac  al.  —  1)  So  F. ;  S  26S.  1 1 .
•  j.  srvara-  Adj.  'gehörnt"':  asTm  'r^m .  .  yim  .  .  tairit?m  Y.g.  11.
Komp.:  irü-+*iarii;  %i6S.2T,  BTHL.BB./J. 14.  —  Pä.i  transskr.  (ddmbr),  —  >>  Die ionischen  Tiere  auf  den  Wandtläcben  in Peisepolis  sind  alle  gehörnt;  s.  trvÖJiana-; vgl.  DsT.  ZA.  /.  88  No.  31.  —  ')  Man  nahm das  Wort  als  EN. ;  1.  SBE.  iS.  374,  37-  i8S. ^7.  12,  vonStackelberg  WZKM.  ti.  340.
•  j.  srvä-  t:  s.  unter  srU-. KompA.
•  j.  srvo.zana-  Adj.  'zur  Hornrasse,  zur Rassc  der  Gehörnten  gehörig';  snaviihm yim  'n>m  Yt7p.  43.
Vgl.  ReMY  JAOS.  20.  70  und  zu  srvara-  No.  I.
•  j.  srvi^täy-  Adj.  'mithömemen  Widei- haJten',  vom  Pfeil ;  ifunqm  *kahrkäss.para- nam  zaranyS.zafram  °stayam  Yt, /o,  139.
'Komp.  mit  ND.  (*.  srü-  NÖ.  3)  im  1.  Glied; "iläy  f.,  zum  V.  ttä-,  s.  daiu  ZDMG.  4^.  665 und  mp.  ittnii.  Eig.;  'dem  ein  Horn(spltzen)- paar  als  Ständer  dient',  vom  Pfeil,  an  dem unterhalb  der  Spitze  ein  paar  Hornspitzen  als Widerhaken  eingesetzt  sind,  durch  die  er  in der  Wunde  zum  Stehen  gebracht  werden, festsitzen  solL
j.  tä  ¥4  a:  lies  :i;  s.  sam-.
j.  Eoräs ;  s.  unter  ioina-  und  zayan-.
•  j.  zaena-  m.  'Waffe':  vasrfm  . .  ama- vastpmfm  -nam  (GP.)  Yt.  70.  96  ";  96;  — hqm  *'tta  (AP.)"  stmbayalwtm  (sd.)  Yt  i. 27;  —  *tta  (IS.)  haHtma  hutniia  Yt. 10. 141.
KompE.  —  ai.  vgl.  Arläy-  f.  'Waffe'.  —  mp. sfn,  np.  :ii*.  —  Vgl.  saya-,  'za/nay-.  —  Pü. (zu  Yt.  /):  a-J^zär.  —  »  Vgl.  Yt.  /o.  132.— ')  NA.  tanva,  vgl.  Gdn.  KZ.  JO.  514.  S.  aber Pü.  und  die  Hds.
•  j.  zaenaDh'an-  Adj,  'wachend,  wach- sam': sraes?m..yd  anavanhabdsmra  'aha (NS.)  nipaili  tnazää  däman  Y.57.  16;  16, F.  20;  —  'K>ha  (NS.)  niJspBj^aJna  (sd.) ya&a  västryS  fsuyqs  V.  13. 46.
Ableit  a.ax  zalimh:  —  Pü.:  linävand,  pa  ünä-
•  j.  zaenay-  Adj.  "reg,  eifrig':  yas^a  hi .  .  väam    paifi    'nil   anhat    (näroL  sp£)
dby  Google
1651
"wenn  er  {der  Hund)  ..  eifrig  ist  mit  (der Stimme  sva.)  Bellen"  V.  /j.  40.
KompA.  —  VgL  lafmoB:  —  Pü.;  lüca  fa  in
i  ei  gffwiin  • .  apar  anhand  ait.
•  j.  zaenav-  f.  'Wehrgehänge'*':  yailqm zayanqm  raisWi  .  .  puxaa  'nätti  mat aiana  mat  "irisas  ayj.arfräil  ". .  das  Wehr- gehänge mit  dem  Köcher  sammt  30  eisen- spilzigen  Pfeilen"  V.  14. 9.
•)  Das  »on  der  linken  Hüfte  über  die  rechte Schulter  lief  und  insbetondere  «um  Tragen  des Köchen  dienie:  TgL  auf  der  Inschrift  toq  Ba- Aiitän  die  Figur  dei  hinter  dem  KOnig  ctehen- den  renere.
KompEi  —  np.  z!n  'Sattel'.  —  Pü. :  an.
•  j.  zalnah-  n.:  sva.  'xalman-  n. Ableit.   —    mp.  ün*;    i.  dazu  Btrl.  IF.  r2. IA2.
•  j.  zaenah'vant- Adj.  'wachsam,  regsam': mCir?m  . .  •narthuntim  Yt  /o.  61 ;  — *'na>3uhant>m     . .    yaka     taxmS    urvpa
A2.2'>,
rü. :  zhtävand.  —  >)  Vgl.  lU  aiinasan/;
•  j.  zaeni.buSra-  Adj.  'reg,  eifrig  wachend, wachsam':  spatam  .  .  °rmi  V.  y.  39.
VgL+Juira-EN.  — Pü.;  jFnäBan^ (erl. :  tuxiäk) dnp  rftk,  ctL:   ünSi  ^apel  'er  schläft  wach'.
•  g.  'zaeman-  n.  'Regsamkeit,  Munter-, Wachsein' :  ks  hvaph  c^afmmca  dät  'mäcä "wer  schuf  wohlwirkendSchlaf  und  Wachen" Y.  44. 5.
Zum  ai.  V.  MnlH  'incitat'.  —  Vgl.  *tainak; 'toimaii',  viaSäla-,  —  ai.  aiu-htaian-  Adj.  — Pü.:  imävxnälh,    eri.;  luxlSkih,    Sn.:  jägara-
•  j,  'zaeman-  Adj.  'regsam,  wach*:  •matiB F.  4  f.
Vgl.  ^xarmart:  —  Pü. ;  ttttävanä. g.  oMiinä  Y.  4/.  4:  s.  6ia-.
•  j.  zaeäa-  Adj.  'schauderhaft':  •/ff  F.  20. S.  auch  sminav;  sSiidiila:  —  Vfil.  mp.  (Pü.), np.  ujV«)  'schauderhaft',  got.  ingtiman  'er- *ebrecken';  IJtt.i  IF.  2.4,%,  GGA.  tSg6.  961, Hbm.  PSI.  70.  —  0  Das  freilich  auch  dem ai.  hffii-  entsprechen  könnte ;  vgl.  unter  zat- Sayamna:
•  ].,  g.  zaotar- ;  zaoSr-  m. 'Priester,  Ober- pricster';  y7  (näml.  zara'husirö)  *fä  a/ä tnzü/  .  .  kaya  (Sp.  46a  m.)  S.. 33.it;  be- nutzt Yt.  4.T.  yi  °ta  sarähustrS.  A)  im jAw.  Name  des  vornehmlich  mit  dem Vortrag  der  Gä'iäs  betrauten  Oberprie- sters, der  den  Gottesdienst  zusammen  mit sieben" Unterpriestem  (s.  'raiav-),  im  Not- fall aber  auch  allein  (s.  N.  Si,  Sp.  1653  ra.) vollzieht:    'lanm    asavanim    aiahe  ratäm
zaotar- A
1652
yasamaide  hävauämm  .  ,  Slravaxstm  .  , |G.j.s;  V,5,57,58;  —  vUäi  v!  anusa ipmtä  staotä  Uä  zbitä  . .  Y.14. 1 ";  Vr. 5.1; —  stofftarxa  'tanca  tiatania  Yt.j. i;  —  az3m  ..  'ta  rlrJ/ (Sp.  1327  o.) slaotanqm  yesnyanam  frasrao%r3mca  .  . fräyastlnüa  Vr.j.  7;  —  tum  tta  akra^m *sactasie  (Sp.  1607  o.)  *  'V1.3.  7;  — ya^a dis  atpm  y5  °ta  itva^ayemi  vi%vä  a^qm yasn»mca  vahmimca  . ,  Vr.  Jr.  1 9 ;  —  kaha 'la  xsata  vala  SfS  .  .  yazätte  Y,  6^.  9; 9,  Yt5.  131,  so.  120;  —  bfr7Z3in  barät  'la väiim  Aisbmra  pasia  banstna  Yt/7.61; 10. 137,  138;  —  dayata  . .  aps  ttiäva- yaia  '^re  yeztmnai  ahmaktm^a  maxda- yamanqm  fräyatsmnattam  .  .  Y.6S.  12; 2,  39.30;  —  hana^a  tu  tum  taj  mtcd^m ya^  'ta  hanayamnS  ättha  frayB.kumatB  . . Y. 55.30;  —  ar?dvT  .,  -5«  (statt  Gen.) väHm  paitiimarfmna  Yt  5.113;  —  daAmd •la  tanupiriia  (sd.)  upa.sraotarl!  N.jS; 3g^;  — surunaoiti  *'tai1  upa.sraotaraiiqm (sd.)nöit upa.sra0tarB  •tarB{GS.)'ta  raiufris N.  27;  2/';  ~  Si  '/arI{GS.)  iairim  ai^Aai myatdahe  *ayqn?  (ya/)  *ga%asca  fratrsva- yaiti  vantnca  af3he  (Sp.  108  m.)  *astvaite paiti.ähaySt  aka  ratul  '"Was  ist  das  Amt des  Z.  am  Tag  des  My."}'  'Dass  er  die G.  vorträgt  und  der  Gemeinde  auf  ihren Gesang  mit  <£iia  ratus  (msv.)  antwortet'" N.  72;  —  aat  *atravaxiahe  (sd-,  oämL  kai- rim  arahaf)  yat  . .  •Prälat  väcim  paiti.- aiaya^  H.  J3 ; — yaha  ahB  vairyS  'tä  frä ml  mrOt! . .  a%a  ratus  aiäi^^  kaca  fra aidva  vjtva  mraotü  "y.  a.  v.  soll  der  Z. aufsagen  . .  a.  r.  a.  h.  soll  der  wissende Gläubige  (sva.  die  Gemeinde,  s.  Sp.  250  0.) aufsagen"  V.J.  25;  25**,  N.jj*; —  kä^a 'ta  ga'ha  frasravayäilii  *>iaänlF.vacastasta (sd.)  *mahmya  vaca  sardkvstri  mana "'wie  soll  der  Z.  die  G.  vortragen?"  In der  (ersten)  Halbstrophe  (jeweils)  mit mittelstarker  Stimme  im  £<ir-i2^»jVnschen Zeitmass'"  N.j_j; — yat'ta  ahurtm  masdqm yazäiti  *mao^näi  barasmqn  paitiiareii  N. J0;~'ta  g}ui*paityapöis(%A.) paoiryO  */ra- »harsitti.  "/J-iyi; — yezica  *a!fe  ratavd  *ana- iaxta(sd.)*para.iyayanti  °ta  viipf.ratu^toais (sd.)  *ra!%wayeiii  N.  80;  —  'ta  *^anahaxtS parayat  dahistäi  arivacasttmäi  saoknm ralxsaiti  "ein  nichtqualifizirter  Z.  soll  weg- gehen und  das  Z.-Amt  einem  Überlassen, der  .  ."  N.  i¥o;    —    cvaiti    naram    *iaxlö
dby  Google
i6S3
zaotar-  Noten
'zaoSra-
```


## [2026-09-06T16:14:48.760Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} END{print NR}' LEW_1910.txt; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==917' LEW_1910.txt | head -40"
}
```


### [2026-09-06T16:14:50.646Z] TOOL RESULT

```
305
---
```


## [2026-09-06T16:14:54.314Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"srva\\|srvara\\|srū\\|sru-\" LEW_1910.txt | head -20; echo \"=== cornu ===\"; grep -n \"^cornu\\|cornu,\" LEW_1910.txt | head -10"
}
```


### [2026-09-06T16:14:54.366Z] TOOL RESULT

```
593:ali- II 62 aluka- I 30 algdu I 759 ava- ,,jener“ I 87 ava, avah ,,herab* LY, MIE Za, ial avata-h I &2 avata-h I 82, 436 davati ,,fordert* J 81, If 229 -avati ,,merkt auf* I 80 avani- I 435 avar II 771 dvas-, avasd- I 81 avastad II 771 avasdna- II 45 avasita- II 545 avaskara-h I 205 avaskava-h II 411 davasyati II 545 dvi- II 229 avika-, avikd II 229 avitar- I 81 dvidvas- II 495 avocam II 824 asana- I 210 asitt- II 200 asusa-, asna- I 210 asnati I 210 asnoti IT 141 asman- I 5, 7, § asri- I 7 dsru-, asra- I 746 asva-h I 412 asvatara-h II 52 asvaratha I 60 agva I 412 astamda- II 200 asta, astdu II 199 asthivant- II 225 asakra- II 533 asana I 406 adsami- II 512 ast- I 406 dasita- I 65; II 515 dsinvan-, asinva- II 482 dsu- I 50, 419 asura-h I 419 asrk I 72
1699:srvad-, srvara I 208 zaén- ,,Winter‘‘
=== cornu ===
```


## [2026-09-06T16:14:55.175Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"keration\\|carob\\|qirat\\|qīrāṭ\\|carat\" KLN_1966.txt | head -30"
}
```


### [2026-09-06T16:14:55.229Z] TOOL RESULT

```
2171:algarroba,  n.,  1)  the  carob  tree;  2)  the  common mesquite  (Prosopis  juiiflora).  —  Sp.,  fr.  Arab. al-kharrdbah,  ‘the  carob’,  fr.  al-,  ‘the’,  and kharrdbah,  ‘carob  tree’.  See  carob. algarrobilla,  n.,  a  yellow  dye  from  the  seeds  and pods  of  Prosopis  juiiflora.  —  Sp.,  a  dimin. formed  fr.  algarroba.
4230:baccalaureate,  n.,  the  academic  degree  of  bach¬ elor.  —  ML.  baccalaureatus,  fr.  baccalaureus, fr.  baccalarius,  ‘the  holder  of  a  small  farm;  a young  man’,  which  is  of  uncertain  origin ;  influ¬ enced  in  form  by  L.  bacca,  ‘berry’,  and  laureus, ‘of  laurel’,  fr.  laurus,  ‘laurel’.  Cp.  bachelor.  For the  ending  see  subst.  suff.  -ate. baccara,  baccarat,  n.,  a  gambling  card  game.  — F.,  of  unknown  origin.
6451:caratch
6495:Caranx,  n.,  the  type  genus  of  the  Carangidae (ichthyol.)  —  ModL.  See  Carangidae. carapace,  n.,  the  covering  of  the  back  of  certain animals,  esp.  the  upper  shell  of  the  turtle,  crab etc.  — »  F.,  fr.  Sp.  carapacho,  which  is  of  un¬ known  origin.  Cp.  calipash,  calipee, carat,  n.,  unit  of  weight  for  precious  stones  and pearls.  —  F.,  fr.  ML.  carratus  (whence  also  It. carato),  fr.  Arab,  qirdt,  ‘fruit  of  the  carob  tree ; weight  of  4  grains’,  fr.  Gk.  xcps-nov,  ‘a  little horn;  fruit  of  the  carob  tree;  carat’,  dimin.  of xspxc,  gen.  y.scrroc,  ‘horn’.  See  horn  and  cp. com,  ‘hardened  skin’.
6496:caratch,  n.,  formerly,  a  tribute  imposed  by  the Arabs  and  Turks  upon  their  non-Mohammedan subjects.  —  Arab,  khardj,  kharj,  ‘tribute’,  bor¬ rowed  fr.  Aram,  kargd,  ‘tribute’,  through  the medium  of  Persian  (Aramaic  was  the  official language  of  the  Persian  kingdom  for  many centuries).
6575:carob
6578:carob,  n.,  a  tree  ( Ceratonia  siliqua );  its  seed  pod. —  F.  caroube,  fr.  ML.  carrubia,  carrubium ,  fr. Arab.  kharrdbah,  fr.  Aram,  harubhd,  ‘carob  tree, carob’,  which  is  rel.  to  Heb.  hardbh ,  of  s.m.  Cp.
7008:xEpa-ro-,  xepax-,  fr.  xepap,  gen.  xlpxxo p,  ‘horn’, which  is  cogn,  with  L.  cornu,  ‘horn’,  fr.  I.-E. base  *ker-,  ‘the  uppermost  part  of  the  body, head,  horn,  top,  summit’.  See  horn  and  cp. carat,  cervine,  crio-,  keratin.  Cp.  also  Acera- terium,  Acerates  and  the  second  element  in Dicruridae,  Dinoceras,  Megaceros,  rhinoceros, Triceratops.
7330:chemin  de  fer,  1)  railroad ;  1)  name  of  a  gambling game  resembling  baccarat.  —  F.,  ‘railroad’,  lit.
24894:nacarat,  n.,  1)  the  color  geranium  lake;  2)  Ane crepe  or  linen  of  this  color.  —  Sp.  nacarado,  fr. ndcar,  ‘mother-of-pearl’.  See  1st  nacre, nacelle,  n.,  1)  the  basket  attached  to  a  balloon; 2)  part  of  an  airship  containing  the  engines,  crew, cargo,  etc.  —  F.,  fr.  VL.  naucetla,  fr.  Late  L. navicella  (whence  also  It.  navicella),  ‘a  little  ship’, dimin.  of  L.  navis,  ‘ship’.  See  naval  and  -ella. nacre,  n.,  mother-of-pearl.  —  F.,  fr.  It.  naccaro (now  nacchera),  fr.  Arab.  naqqdrah,  ‘a  drum’,  fr. naqra1',  ’hollow,  cavity’,  fr.  naqara,  ‘he  hollowed out,  bored  out’,  which  is  rel.  to  Heb.  naqar, Aram.-Syr.  nlqar,  ‘he  bored,  bored  out,  dug’, Heb.  niqrdk  or  neqdrah,  ‘hole,  crevice’,  Ethiop. naqwara,  ‘he  was  one-eyed’,  Akkad,  naqaru,  ‘to
```


## [2026-09-06T16:15:12.097Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^90[0-9]$\\|^ *905 *$\" LEW_1910.txt | head; echo \"=== find srvara ctx ===\"; sed -n '1690,1710p' LEW_1910.txt"
}
```


### [2026-09-06T16:15:13.890Z] TOOL RESULT

```
=== find srvara ctx ===
skarana- I 317
skanda- II 489
staéra- II 592
staora- I 706. II 651 staxra- II 585, 678 stawra- II 641 star- ,,Stern“ II 587 star- ,,streuen‘‘ IT 590 sta(y)- ,,Haufen“ IT 593
staiti- IL 598 staya- ,,stellen“
II 597 stuna, stunad I 706 spaéta- II 806 spanah- I 152 sparatte ILI 572 sparaya- II 566 spas- I 87 spasyeitt II 570 spas-, spastar-
II 570 spa I 153 spa(y)- I 191 spanah- I 152 spama- II 581 spanta- II 337 spanvat II 569 sporazan- I 799 spinjauruska- I 839 sptta- II 806 snaezaity II 169 snaoda- II 183 snayewté II 172 snavara II 165 sya- II 495 syazd- I 193, 194 syamaka- I 216 syava- I 216 sraobra- I 238 sraoni- I 239 sraoman-, sraota-
I 238 sraosa I 238 srav-, sravah- I 238 sravayeitt I 238 srinav-, srinu- I 234 sru I 208 sriita- I 238, 690 strt- II 522, 594 srv- I 238
~ ip ea sd ie I aba aa A i wane Ff
srvad-, srvara I 208 zaén- ,,Winter‘‘
I 646 zaena- ,,Waffe‘‘
IT 576
zaotar-, zaoora I 563
zaos- I 629
zanat II 176
-zanta- I 598
zayan-, zayana- I 646
zayeite I 599 zar- ,,erzurnen‘‘ I 658 zara- ,,streben‘‘ I 658 zaranya- I 14 zarata- I 619 _ zairi-, zairita- 1514 zairina- I 619 zaurvan- I 619 zarsaya- I 413 zarsayamna- I 659 zarstwa- I 643 zazami I 641 za I 52 zata- I 598 zanaite I 599 zanu- I 589 zamaoya- I 590 zamdtar- I 590 zara- I 473 zamaka I 645 zerada I 272 zaradaya- I 857 zoizdista- I 523 za I 665 zu I 644 zurah- I 448 zbaramna- I 448 zyda I 62 zyo I 642 zya I 646 zrayah- I 608 zrazaa- I 287 zrvan- I 700 Savaite I 214 Sdta- II 406 Saiti- IT 406 saista- II 406
Walde-Hofmann, Register
Avestisch
8600ra- IT 461 Siyati- II 406 -smaraitt IT 67 syaodna-, syaoman- I 214 Syavatte I 214 Syata- II 406 Syetibyd II 406 gnatar- II 177 gnu- I 592 ha- ,,mit‘* IT 539 ha, hé Demonstr. Pron. I 722 haék- II 531 haééayat, haétah- LL 533 haétu- II 462 haoma- II 623 haoya- II 486 haogs- II 624 hakat II 519 hakerat II 511 haxa- II 550 haxay- II 519, 551 haxman- II 519 haéa II 507, 519 haéaiti II 519 hadé II 512 hadamoi I 369 hada I 251 haSré II 512 haidya- II 560 hapta II 518 han-_ ,,verdienen‘“‘ IT 514 hana- ,,alt‘* IT 514 hanaiti II 544 hanara II 507, 542 hant- II 516 ham II 539 hama- ,,jeder be- liebige®* JI 209, 539 hdma-_ ,,derselbe“ IT 589 hamaéstar- II 98 hamista- II 98 hamzambayati I 588 hava- II 626 har- II 523 harax*va'ti- II 525
```


## [2026-09-06T16:15:22.403Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l LEW_1910.txt; head -20 LEW_1910.txt; echo \"=== grep cornu ===\"; grep -n -i \"cornu\" LEW_1910.txt | head -10"
}
```


### [2026-09-06T16:15:22.455Z] TOOL RESULT

```
14865 LEW_1910.txt
eae hee ne
ee
Duquesne University:
joe Kt re |
* ee . ¥
c
'DOGERMANISCHE BIBLIOTHEK
-ZWEITE REIHE: WORTERBUCHER
____ Digitized by the Internet Archive in 2023 with funding from No Sponsor — re
mi https://archive.org/details/lateinischesetymO ) any * ; - % MANY ioe hie vel
AN
~ LATEINISCHES: ee “EYYMOLOGISCHES WORTERBUCH ee
A. WALDE Met
3, NEUBEARBEITETE AUFLAGE ron #
VON
J. B. HOFMANN . 2 : * A
REGISTERBAND
ZUSAMMENGESTELLT VON ELSBETH BERGER
HEIDELBERG 1956 1B
: AA. Fs
=== grep cornu ===
5680:Cornuinus I 276
```


## [2026-09-06T16:15:37.609Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"singivera\\|siṅgivera\\|zingiber\\|ziggiberis\\|gingivre\\|zanjabil\\|zanjabīl\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T16:15:37.684Z] TOOL RESULT

```
16161:ginger,  n.  —  ME.  gingevir,  gingivere,  fr.  OE. gingiber,  fr.  OF.  gingibre,  gingembre  (F.  gin- gembre),  fr.  L.  gingiber,  zingiber,  fr.  Gk.  ^ty- YijJepi?,  fr.  Pali  sihgivera-,  fr.  OI.  sphgavera-, ‘ginger’,  lit.  ‘hornlike’,  fr.  sfhgam,  ‘horn’,  and vera,  ‘body’;  so  called  in  allusion  to  the  horn¬ like  shape  of  the  root.  See  horn  and  cp.  Zingiber. Derivatives:  ginger,  tr.  v.,  ginger-y,  adj. gingerly,  adj.,  wary;  adv.  warily.  —  Of  uncertain origin;  possibly  formed  with  suff.  -ly  fr.  OF. genfor,  gensor,  ‘prettier’,  compar.  of  gent,  ‘of noble  birth,  noble,  gentle,  pretty’,  fr.  L.  genitus, ‘born’,  pp.  of  gignere,  ‘to  beget,  bear,  bring forth’.  See  genus.
```


## [2026-09-06T16:15:37.950Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ginger\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T16:15:38.000Z] TOOL RESULT

```
2508:Amomum,  n.,  a  genus  of  plants  of  the  ginger  fa¬ mily  ( bot .)  —  L.  amomum ,  ‘a  spice  plant’,  fr. Gk.  apcopov,  which  is  of  Sem.  origin.  Cp.  Mish- naic  Heb.  hdm&m,  of  s.m.,  and  Syr.  hamamd, Arab,  hamdma,  ‘a  spice  plant’,  which  prob.  de¬ rive  from  stem  i h-m-m,  ‘to  be  warm  .  See  Imma¬ nuel  Low.  Aramaische  Pflanzennamen,  Leipsic,
3576:asarabacca,  n.,  the  wild  ginger  (bot.)  —  Com¬ pounded  of  L.  asarum,  ‘hazelwort’,  and  bacca, ‘berry’.  See  Asarum  and  bacci-. asaron,  n.,  a  crystalline  compound,  found  espe¬ cially  in  the  oils  of  plants  of  the  genus  Asarum.
9947:Curculio,  n.,  a  genus  of  weevils  (entomol.)  —  L. curculio,  ‘a  grain  weevil’,  lit.  ‘a  winding,  twist¬ ing  (beetle)’,  fr.  I.-E.  base  *qer-,  ‘to  turn,  twist’, whence  also  L.  curvus,  ‘bent,  curved’.  See  curve. Curcuma,  n.,  a  genus  of  plants  of  the  ginger family  (hot.)  —  ModL.,  fr.  Arab,  ktirkum,  ‘saf¬ fron,  curcuma’.  See  Crocus  and  cp.  turmeric, curcumin,  n.,  the  coloring  substance  of  curcuma root  (C2,H20O6)  (chem.)  — -  Formed  fr.  prec. word  with  chem.  suff.  -in.
15697:Galilee,  name  of  the  northern  province  of  wes¬ tern  Palestine.  —  L.  Galilaea,  fr.  Gk.  raXiXata, fr.  Heb.  Haggdlil,  lit.  ‘the  district’,  shortened  fr. Gflil  haggoyim,  ‘the  District  of  nations’  (Is. 8:23).  Haggdlil  was  the  name  of  a  district  in  the hill  country  of  Naphtali  (see  Josh.  20:7  and 21:32).  and  it  was  only  at  a  relatively  later  period that  it  began  to  denote  the  territory  of  Palestine north  of  the  Emek  Jezreel  (Esdraelon).  For  the etymology  of  Heb.  galil,  ‘district’,  see  gelilah. galimatias,  n.,  jargon.  —  F.,  ‘nonsense,  gibberish  , prob.  a  deformation  of  Late  L.  balhmathia,  in¬ decent  songs'.  For  the  etymology  of  this  latter word  see  Du  Cange,  Glossarium  mediae  et  in- fimae  latinitatis,  s.v.  balare. galingale,  n.,  an  aromatic  root  of  the  ginger family.  —  OF.  galingal,  formed— through  the medium  of  MGk.  yaXxyyoc  and  ML.  galanga fr.  Arab,  khalanjdn,  fr.  Pers.,  ult.  fr.  Chin.  Ko- leung-keung,  lit.  ‘mild  ginger  from  the  region of  Kao’.
16006:genetic,  genial,  ‘mild’,  genie,  genital,  genitive,  ge¬ nius,  genre,  gens,  genteel,  gentile,  gentility,  gentle, gentleman,  Gentoo,  gentry,  genuine,  -geny,  ge- nyo-,  germ,  german,  germane,  germen,  germinal, Gerygone,  gingerly,  gonad,  gonidium,  gonorrhea, -gony,  heterogeneous,  homogeneous,  indigene, indigenous,  ingenuous,  innate,  Iphigenia,  Jataka, jaunty,  kin,  kinchin,  kind,  n.,  kind,  adj.,  kindred, king,  malign,  mirza,  miscegenation,  nascent, natal,  nation,  native,  nature,  nevus,  oogonium, perigonium,  Prajapati,  primogeniture,  progeny, shahzada,  Teiegonus,  ultimogeniture.
16161:ginger,  n.  —  ME.  gingevir,  gingivere,  fr.  OE. gingiber,  fr.  OF.  gingibre,  gingembre  (F.  gin- gembre),  fr.  L.  gingiber,  zingiber,  fr.  Gk.  ^ty- YijJepi?,  fr.  Pali  sihgivera-,  fr.  OI.  sphgavera-, ‘ginger’,  lit.  ‘hornlike’,  fr.  sfhgam,  ‘horn’,  and vera,  ‘body’;  so  called  in  allusion  to  the  horn¬ like  shape  of  the  root.  See  horn  and  cp.  Zingiber. Derivatives:  ginger,  tr.  v.,  ginger-y,  adj. gingerly,  adj.,  wary;  adv.  warily.  —  Of  uncertain origin;  possibly  formed  with  suff.  -ly  fr.  OF. genfor,  gensor,  ‘prettier’,  compar.  of  gent,  ‘of noble  birth,  noble,  gentle,  pretty’,  fr.  L.  genitus, ‘born’,  pp.  of  gignere,  ‘to  beget,  bear,  bring forth’.  See  genus.
18077:hormone,  n„  endocrine  gland  secretion  which stimulates  functional  activity  (physiol)  —  Gk. opptov,  ‘that  which  urges  or  arouses’,  pres.  part, of  oppav,  ‘to  set  in  motion,  urge,  stimulate’,  fr. 6p[xr),  ‘onset,  impulse’,  fr.  I.-E.  base  *ser-,  ‘to run,  flow’,  whence  also  Gk.  opop  (for  *<jopop), L.  serum,  ‘watery  fluid,  whey’.  See  serum  and cp.  words  there  referred  to.  The  word  hormone was  used  by  Hippocrates  to  denote  a  vital principle.  In  its  modem  sense  it  was  first  applied by  the  English  physiologist  Ernest  Henry  Star¬ ling  (1866-1927)  in  1903. horn,  n.  —  ME.,  fr.  OE.  horn,  rel.  to  ON.,  OFris., OHG.,  MHG.,  G.  horn,  Du.  horen,  hoorn,  Goth. haurn,  ‘horn’  and  cogn.  with  Gk.  xepxc,  Gala¬ tian  Gk.  xapvov,  L.  cornu,  OI.  sfhgam,  ‘horn’,  fr. I.-E.  base  leer-,  ‘the  uppermost  part  of  the  body, head,  horn,  top,  summit’,  whence  also  L.  cere¬ brum  (prob.  for  *kerls-rom), ‘brain’.  See  cerebrum and  cp.  hornet.  Cp.  also  hart,  hurt  and  the  sec¬ ond  element  in  krummhom,  waldhom.  Cp.  also cerato-,  cervine,  crio-,  com,  ‘hardened  skin’,  the first  element  in  ginger  and  the  second  element in  Capricorn,  unicorn.
31506:Derivatives:  race,  intr.  and  tr.  v.,  rac-er,  n., rac-ing,  verbal  n.  and  adj. race,  n.,  root,  esp.  ginger  root.  —  OF.  rate,  rais, fr.  L.  radicem,  acc.  of  radix,  ‘root’.  See  radix, race,  tr.  and  intr.  v.,  to  scratch.  — •  A  var.  of  raze.
34882:shandygaff,  n.,  mixture  of  beer  and  ginger  beer. —  Of  unknown  origin.
40492:turma,  n.,  troop,  squadron  of  horse  (Roman antiq.)  —  L.,  of  uncertain  origin.  It  is  possibly rel.  to  turba,  crowd’  (see  turbid), turmeric,  n.,  an  aromatic  plant  of  the  ginger  fam¬ ily  (Curcuma  longa).  —  Fr.  earlier  tormarilh,  tar- maret,  fr.  F.  terre  merite,  ‘saffron’,  fr.  ML.  terra merita  ( =  deserved  earth’),  a  folk-etymological corruption  of  Arab,  kurkum,  ‘curcuma’.  See Curcuma.
```


## [2026-09-06T16:15:45.487Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\n\""
}
```


### [2026-09-06T16:15:47.481Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-06T16:15:52.594Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\n# compute leaf index per line\nleaf=0\nres={}\ntargets={6495:'carat',7008:'cerato',16161:'ginger',18077:'horn',6451:'caratch-hdr'}\nfor i,l in enumerate(lines,1):\n    if i in targets:\n        res[targets[i]]=leaf\n    leaf+=l.count('\\f')\nfor k,v in res.items():\n    print(k,'leaf',v,'-> printed pages ~',(v-12)*2,(v-12)*2+1)\nEOF"
}
```


### [2026-09-06T16:15:54.964Z] TOOL RESULT

```
caratch-hdr leaf 135 -> printed pages ~ 246 247
carat leaf 136 -> printed pages ~ 248 249
cerato leaf 148 -> printed pages ~ 272 273
ginger leaf 355 -> printed pages ~ 686 687
horn leaf 400 -> printed pages ~ 776 777
```


## [2026-09-06T16:15:58.846Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==137' KLN_1966.txt | head -4; echo \".....\"; awk 'BEGIN{RS=\"\\f\"} NR==137' KLN_1966.txt | tail -4"
}
```


### [2026-09-06T16:16:00.853Z] TOOL RESULT

```
  ‘cart,  waggon’,  Bret,  karr,  ‘chariot’,  L. carrus,  of  the  same  origin  and  meaning,  gave birth  to  ONF.  car,  F.  char.  L.  currus,  ‘chariot’, is  independent  of  the  above  Celtic  words,  but cognate  with  them.  See  course  and  cp.  career, cargo,  caricature,  cariole,  cark,  caroche,  car-
roccio,  carry,  carriage,  charabanc,  charge,  chariot. Derivative:  car,  tr.  and  intr.  v. carabao,  n.,  water  buffalo.  —  Sp.,  from  Philip¬ pine  native  name.
Carabidae,  n.  pi.,  a  family  of  beetles  ( entomol .)  — ModL.,  formed  with  suff.  -idae  fr.  Gk.  vAcyfio-, ‘homed  beetle’.  See  scarab  and  cp.  Caridea. carabineer,  n.,  a  mounted  soldier  armed  with  a carbine.  —  F.  carabinier,  fr.  carabine,  ‘carbine’. See  carbine.
carabinieri,  n.  pi.,  the  Italian  police.  —  It.,  pi.  of carabiniere,  fr.  F.  carabinier.  See  carabineer, caracal,  n.,  a  kind  of  lynx.  —  F.,  fr.  Turk,  qarah qulak,  ‘black  ear’.
.....
Derivative:  carcinomat-ous,  adj. carcinoma toid,  adj.,  having  the  shape  of  a  car¬ cinoma  (med.)  —  Compounded  of  Gk.  xap- xivcopx  (see  prec.  word)  and  -ostSfjc,  ‘like’,  fr. eTSoc,  ‘form,  shape'.  Sec  -oid. carcoon,  n.,  manager,  clerk  ( Anglo-lnd .)  —  Ma¬ rathi  karkiin,  fr.  Pers.  kar-kun,  'manager’,  lit. ‘doer  of  what  is  to  be  done',fr.  I.-E.  base  *q"'er-, ‘to  make,  form,  shape'.  See  Sanskrit  and  cp. words  there  referred  to.
card,  n.,  a  machine  for  combing  hair,  wool,  etc.  — F.  carde,  ‘chard,  teasel,  card",  fr.  OProveng.  ear- do,  back  formation  fr.  cardar,  ‘to  card’,  fr.  L. carduus,  ‘thistle’,  which  is  related  to  carro,  car- rere,  ‘to  card  (wool)’,  from  a  basic  form  *carri- dus,  ‘that  which  scrapes’,  fr.  I.-E.  base  *qars-, 'to  scrape,  scratch,  rub’.  See  harsh  and  cp.  car- doncillo,  cardoon,  Carduus,  Carex,  carline  thistle, carminative,  carrizo,  chard, card,  tr.  v.,  to  comb  with  a  card.  —  F.  carder, fr.  carde.  See  prec.  word.
Derivatives:  eard-ed,  adj.,  card-er,  n. card,  n.,  a  piece  of  pasteboard  for  playing.  —  F. carte,  fr.  Late  L.  carta,  ‘a  leaf  of  paper;  paper’, fr.  L.  charta,  ‘a  leaf  of  the  Egyptian  papyrus; papyrus;  paper',  fr.  Gk.  yip rqp,  of  s.m.,  a foreign  word,  possibly  of  Egypt,  origin.  Cp. carte  blanche,  carte  de  visite,  cartel,  cartoon, cartouche,  cartridge,  cartulary,  chart,  charter, ecartc,  skat.
Cardamine,  n.,  a  genus  of  plants  of  the  mustard family  (hot.)  —  ModL.,  fr.  L.  cardamina,  fr.  Gk. xxpSxaivr,,  ‘a  kind  of  cress',  a  word  formed  by Dioseorides  fr.  xxpSxpov,  ‘cress",  which  is  of  un¬ certain  origin.  Cp.  next  word, cardamom,  cardamum,  n.,  an  aromatic  fruit.  — F.  c
```


## [2026-09-06T16:16:16.167Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(125,160):\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', leaves[i])\n    print(i, nums[:4], leaves[i][:40].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:16:18.363Z] TOOL RESULT

```
125 ['218', '219'] cabalist,  n.,  a  student  of  cabala. 
126 [] n.  — -  L.,  ‘a  prickly  plant’,  fr. 
127 [] isy.  —  F.,  ‘hypocrisy’,  for¬ med  fr
128 ['222', '223'] ia and  adj.  suff.  -ate  and  cp.  dis
129 ['224', '225']  cp.  -pod.  Gk.  xAXo7t68lov  came  int
130 ['226', '227'] lo-  and  melancholy. Calonyction,  n., 
131 ['228']   camel with  suff.  -eer. Camelidae,  n
132 ['230'] n or  index  (of  the  sundial)’,  OL.  
133 ['232', '233']   days.  —  L.  caniculdris,  fr. eanicu
134 ['234', '235']   chant),  ‘corner’.  See  cant,  ‘slope
135 ['236', '237']  Gk.  xojrrsiv,  ‘to  strike,  cut,  cut
136 ['238', '239']   ‘cart,  waggon’,  Bret,  karr,  ‘chari
137 ['240'] ardamome,  fr.  L.  cardamomum,  fr.  Gk
138 ['243']  was  associated  by  legend, cariing,  
139 ['244', '245'] rro-,  xapjr-, fr.  xap7TOg,  ‘wrist’.  
140 ['246', '247']   called  scientifically Crotalus  terri
141 ['248', '249'] ixed  below  a chair  leg.  —  Formed  f
142 ['250', '251'] - i I * T -r m m Derivatives:  catamit-e
143 [] ,  ‘to  rob’). Derivative:  caterpillar,
144 ['254'] urning  pain’,  coined  by  the  Ameri¬ 
145 [] suff.  used  to  form  abstract  nouns. 
146 ['256', '257']   whole  and  cp.  words  there  referre
147 ['258', '259', '260', '261']  sense,  arose  G. Tausendgiildenkraut, 
148 [] erived  from a  language  of  Asia  Mino
149 ['262', '263']  adj.,  pertaining  to  modeling  in  wa
150 ['264', '265'] ��one who  speaks  (in  a  certain  mann
151 ['266', '267'] d  cypress’,  fr. Chamaedaphne chap 266 
152 ['268', '269']  —  Coined  fr.  prec.  word  on  analog
153 ['270', '271'] erm’,  dissimilated  fr.  *gen-men  (see
154 ['272', '273']  color’,  fr.  T.-E.  base  *ska(i)-, ‘t
155 ['275'] See  alchemy  and  -ist.  Derivative:  c
156 ['276', '277'] ophistry.  — - F.  chicanerie,  fr.  chi
157 [] nee. Chinook,  n.,  a  N.  American  Ind
158 ['280', '281'] m .) —  Coined  fr.  chlor(ine)  and  al
159 ['282', '283'] d  to.  For  the  second  element  see -
```


## [2026-09-06T16:16:29.087Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^cerebrum\\|cerebrum,  n\" KLN_1966.txt | head; echo ===; sed -n '/^cerebrum,/,+8p' KLN_1966.txt | head -20"
}
```


### [2026-09-06T16:16:31.189Z] TOOL RESULT

```
Exit code 1
7031:cerebrum,  n.,  the  main  part  of  the  brain  (anal,  and zool.)  —  L.  cerebrum,  ‘brain’  (prob.  for  *kerfs- rom),  fr.  I.-E.  base  *ker-,  ‘the  uppermost  part of  the  body,  head,  horn,  top,  summit’,  whence also  OI.  siras,  ‘head,  summit’,  sirsam,  ‘head’, Avestic  sarah-,  ModPers.  sar,  ‘head’,  Arm.  sar, ‘top’,  Homeric  Gk.  xxp,  ‘head’.  Ion.  xxpr,,  Att. xxpx,  xpx;  (poetic  form  for  xxpa).  Ion.  xapr;vov, Att.  and  Dor.  xapivov,  ‘head’,  Gk.  xpxvtov, ‘skull’,  ON.  hjarni,  Du.  hersenen,  OHG.  hirni, MHG.  hirne,  G.  Hirn,  Gehirn,  ‘brain’.  Cp. cranium  and  words  there  referred  to.  Cp.  also cemuous,  cervical,  cheer,  coryphaeus,  the  first element  in  cervelat,  charivari,  sarangousty,
(eval):2: == not found
```


## [2026-09-06T16:16:35.853Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(350,360):\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$', leaves[i])\n    print(i, nums[:4], leaves[i][:40].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T16:16:37.797Z] TOOL RESULT

```
350 ['648'] t,  race’.  See genns  and  verbal  suff
351 ['650', '651'] v.,  gentlewoman-ly,  adj.,  gentle- wom
352 [] cp. georgic. Derivatives:  Georgi-an,  a
353 ['033'] of  garash  (Qal),  gerash  (Pi'el), ‘he
354 []  by  the English  poet  William  Wordswo
355 ['658']   ancient  Hebrew  form of  this  letter
356 ['659', '660'] ost’.  See  gelid  and  adj. suff.  -al 
357 ['661']   ^Xteiv,  ‘to  become  warm’, yXtocpo?,
358 [] )  — Formed  with  subst.  suff.  -ite  
359 ['664', '665'] ’.  See  gullet,  and  cp.  glutton, deg
```


## [2026-09-06T16:16:44.935Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ zanjabil ===\"; grep -n \"Zanjab\\|zanjab\\|زنجبيل\\|Zingiber\" FVQ.txt | head -20"
}
```


### [2026-09-06T16:16:44.982Z] TOOL RESULT

```
=== FVQ zanjabil ===
9732:J J (Zanjabil). 
9759:where the cxcgetes differ as to whether Zanjabll is the name of the
```


## [2026-09-06T16:16:46.051Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD qirat ===\"; grep -n \"قيراط\" TAD_pages.txt | head -10; echo \"=== TAD zanjabil ===\"; grep -n \"زنجبيل\" TAD_pages.txt | head -5"
}
```


### [2026-09-06T16:16:46.111Z] TOOL RESULT

```
=== TAD qirat ===
2330:‫الخرنوب وعلى حبة الخرنوب أيضا وكان الاقدمون يزئون الذهب بالقيراط أي‬
=== TAD zanjabil ===
```


## [2026-09-06T16:16:47.901Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9725,9790p' FVQ.txt"
}
```


### [2026-09-06T16:16:47.941Z] TOOL RESULT

```
before Islam " sed fortasse ludaei Arabici W2T sensu eleemosynarum 
adhibuerunt " (so Torrey, Fowulation, 48, 141). Noldeke, however 
(Ne,ue Beitraye, 25), is inclined to believe that the specializing of the 
word for alms was due to Muhammad himself. 3 



J J (Zanjabil). 

Ixxvi, 17. 
Ginger. 

1 Vide also Bell, Origin, 51. It is possible that the Phlv. JfaSJ dakia of PPGl, 



104, may be from the Hiinie origin. Frahany, Glossary, p. 87. 

2 The origin of this idea, of course, is in the Qur'iiii itself, cf. ix, 104. 

3 See also Bell, Origin, 80; SchuHhesH, in ZA, xxvi, 1.50, 151 ; Ahrens, Muhammad, 
180; Von Kremer, Streifz-Uge. p. xi ; Horovitz, JFX, 206. Wensinck, Joden, 114, 
says : " Men zal misHchien vragen of tot cle Mekkaansehc instcllingen niet de zakat 
behoort. En men zou zich voor dczo meening op talrijke Mekkaansche openbaringen 
kunnen bcroepen waar van zakat gesproken wordt. Men vergeto echter niet, dat het 
woord zakat *^J, het Joodseho 11137, verdionste beteekcnt. Deze naam is door de 
Arabische Joden of door Mohammed uitsluitend op het geven van aalmoczen en daarna 
op de aalmoes zelf toegepast." 



154 FOREIGN VOCABULARY OF THE QUR^AN 

It occurs only in a passage descriptive of the delights of Paradise, 
where the cxcgetes differ as to whether Zanjabll is the name of the 
well from which the drink of the Redeemed comes, or means the spice 
by which the drink is flavoured (vide Tab., Zam., and Baid. on the 
passage and LA, xiii, 332). 

There was fairly general agreement among the early authorities 
that it was a Persian word. ath-Tha'alibl, Fiqh, 318, and al-JawallqlJ 
Mu'arrab, 78, give it in their lists of Persian loan-words, and their 
authority is accepted by as-Suyuti, Itq, 321 ; Mutaw, 47 ; and al- 
Khafajl, 99. ^ 

The Mod. Pers. word for ginger is JJlXxi (Vullers, Lex, ii, 472 ; 

cf. also ii, 148) from Phlv. Jb^^c^j singafler, 1 which is the source 
of the Arm. A, W n L / L , 2 and the Syr. ^.S^JI ; Aram. X^3HT. 8 
The ultimate source seems to have been the Skt. ^np%T> 4 Pali 
singiv&ra, from which comes the Gk. Qyyi&tpis? There can be 
little doubt that the word passed into Arabic from Syr. and was 
thence borrowed back into Persian in Islamic times. 6 It occurs in the 
early poetry 7 and so was evidently an early borrowing. 



(Zawj). 

Occurs frequently in many forms, cf. ii, 33. 
A pair, species, kind, sex, couple, companion, spouse. 
It is a very early loan-word in Arabic from Gk. {eDyoy through 

1 So Vullers, Lex, ii, 148, and cf. Pnhlttri Texts, ed. Jamasp Ar-una, p. 31. 

2 Hubschmann, Arm. (Jramm, i, 238.
```


## [2026-09-06T16:16:49.347Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2315,2345p' TAD_pages.txt; echo \"=== page tag ===\"; awk 'NR<=2330 && /\\[pdf page/ {p=$0} END{}' TAD_pages.txt; grep -n \"\\[pdf page\" TAD_pages.txt | awk -F: '$1<2330' | tail -3"
}
```


### [2026-09-06T16:16:51.869Z] TOOL RESULT

```
‫وهو'لة عار ب ذا تستة وتاك توافق كثارة العيرادة‬               ‫وونانى ‪0‬‬         ‫قيثار‬

‫أما الزياب فله أربعة أوتار ثم ان « قيثار » تقل من اليوناية إلى العبرانية‬
                                                           ‫‪ 2‬قبتراس ‪ 6‬دائيال ‪ : +‬ه‬
‫(‪ )1‬همتاها في المر بيه القعير ‪ .‬وفي اعطلاح ارباب السياسة مأمور ثرسله دولة الى دولة‬
‫أحجندية لاحل جا ‪ 3‬حقوكها وتمارتما ونبمتها وكان القنصل ‪ 5‬الجمهورية الرومانيه ما عت‬   ‫حرق‬

                                      ‫المقام الأول من الولاة تكون له سلطة ملك الي مبنة ‪+‬‬
                                    ‫ساي سم‬


    ‫وناتي ‪80‬م ومنه الانكيزي مو وهو الحندب البحري‬                     ‫قريدس‬

‫اليوناني ومعناه قرن صغير ويطلق على قرن‬             ‫دوعا‬     ‫ل‬          ‫قراط‬

‫الخرنوب وعلى حبة الخرنوب أيضا وكان الاقدمون يزئون الذهب بالقيراط أي‬
                                        ‫حبة الخرتوب وكل ‪5‬ح‪4‬بة نساوي أأوقية‬
      ‫معنأه مشمّم وبراد به مرحم ضمّد به‬               ‫بوناني ‪06‬‬      ‫قيروطي‬
                             ‫قينةسأي بنتنيةف الأضل العتراق ماعة ارائنة‬
                                     ‫دك »‬
                ‫كابلا ‪ -‬ايطالي ‪2‬ااعومهه معناء معبّد أيكنيسة صغيرة‬
‫كاتدرائية ‪ -‬منسوب الى ‪20060‬ادك اليونائي الذي مدا واس و‪ 1‬سي‬

‫وبراد بهكنيشةكرسي المطران لان كرسي المطران أي عرشه نصب بهاعادة‬
                        ‫كاويك د نانى وعانادط]ه»! معناء جامع شامل عام‬
                                ‫كاغد ‪ --‬فارسي ‪ 2‬كاغد » معناة ورقزمقة‬

‫نفاينية ‪ 2500121‬وهوصمغ شجرة تنبت في المند والصين‬
                                               ‫كاافلويروس‬
                    ‫”‬        ‫واليابانأبيض لماعشفاف قابل الاحتراق طب ةو‬
  ‫‪6‬‬                ‫‪0‬‬‫هعناه خادم الاله‬
=== page tag ===
```


## [2026-09-06T16:17:05.758Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" TAD_pages.txt | awk -F: '$1<2330{last=$0} END{print last}'; grep -n \"pdf page\" TAD_pages.txt | awk -F: '$1>2330{print; exit}'"
}
```


### [2026-09-06T16:17:07.862Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:17:08.550Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شنگبیل ===\"; grep -n \"شنگبیل\\|شنگویر\\|شنگبيل\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON زنجبیل ===\"; grep -n \"زنجبیل\\|زنجبيل\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== MON میگرن ===\"; grep -n \"میگرن\\|ميگرن\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-06T16:17:08.645Z] TOOL RESULT

```
=== MON شنگبیل ===
=== MON زنجبیل ===
MON_part2.txt:1393:پاشند. ( گیا.) زنجبیل شامی. 
MON_part2.txt:73254:(کد.) آفتاب. نان زنجبیلی (زنجفیلی): قسمی 
MON_part2.txt:73255:نان که در آن زنجبیل داخل کنند. نان سفید: 
MON_part1.txt:45610:زنجبیل و غیره). (1.) زنجبیل. (مس.) یکی از 
MON_part1.txt:71763:زنجبیل: 72012011 [ع. زنجفیل - جنزبیل 
=== MON میگرن ===
MON_part2.txt:70555:میگرن: 0 زر ] (۱.) (بز.) صدای شقی.
```


## [2026-09-06T16:17:13.202Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON zanjabil ctx ===\"; sed -n '71758,71775p' MON_part1.txt\necho; echo \"=== MON migren ctx ===\"; sed -n '70548,70565p' MON_part2.txt"
}
```


### [2026-09-06T16:17:13.274Z] TOOL RESULT

```
=== MON zanjabil ctx ===

زنجاب: 0 ,30- ,20۳ [ - زنح آب] (امر.) 
زنج درخت که هنوز سفت و منجمد نشده. 
(پز.) ترشحات کم و بیش چسبناک و آب 
شکل خارج شده از زخم‌های جلدی ملتهب. 
زنجبیل: 72012011 [ع. زنجفیل - جنزبیل 
- زتربیل] (ا.) (گیا.) گیاهی است پایا از تیرة 
زنجسل‌ها از راستة تک لبه‌بی‌ها که دارای 
ریزوم غده‌یی ناهموار و ۳ تا ۴ ساقةٌ بکسالة 
به ارتفاع ۳۰ سانتیمتر تا یک متر است. 
برگ‌هایش متناوب و دراز و نوک تیز و 
دارای یک رکبرگک اصلی مشخص و 


این گیاه به غلاف بزرگک و شکافداری منتهی 
می‌گیرد. گل‌هایش مجتمع بصورت سنبله و 
از فلس‌های نازکث پوشیده شده‌اند. رنگ 
گل‌ها مایل به زرد و دارای لکه‌های متمایل 

=== MON migren ctx ===
شاهت دارند. نمو اعضای تناسلی آنها دچار 
وقفه می‌شود و منظره صورت مات و رنگ 
پبریده و بوست بدن خشک و کلفت و 
چروک‌خورده است. بینی آنها پهن و در 
وسط فرورفته و لب‌ها کلفت و غالبا 
تر ث خورده است» میکزادم. 

میگرن: 0 زر ] (۱.) (بز.) صدای شقی. 
می‌گسار تک ۲ )۱۱۵۷ [ < 
میگسارنده] (ص‌فا.) می‌خوار» باده‌نوش؛ 
شراب‌خور. باده‌دهنده» ساقی. 

میگو: 0۱2۷۵-۵0۵ (.) (جان.) جانوری 
است از -اخه بسندباییان و از رده 


سخت بوستان و از دسته 4 خرچنک‌های دراز 
که دارای جنة کوش است. باهای
```


## [2026-09-06T16:17:23.150Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== shangabil variants MON ===\"; grep -n \"شنگب\\|شنگو\\|شنکب\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== BQT v2 sarun ===\"; grep -n \"سرون\" BQT_v2_pages.txt BQT_v1_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T16:17:23.228Z] TOOL RESULT

```
=== shangabil variants MON ===
MON_part2.txt:67145:نمکك. راید شنگول (و) 
MON_part2.txt:67146:منگول: (عم.) شاد و با نشاط. صیج: - شنگول 
MON_part2.txt:67149:فرزند بز هستند و گرگ شنگول و منگول را 
MON_part1.txt:81893:خوشة انگور» آش انگورء اشنگور» اش 
MON_part1.txt:86927:شنگ: 12:6 [قس. شنگول] (ص.) خوش 
MON_part1.txt:86930:راهزن. شنگول؛ شادمان. حیله گر محیل. 
MON_part1.txt:86967:٩ ۷ +‏ فرهنگ فارسی سود 3 شنگول 
MON_part1.txt:86970:شنگول: [0-ومعة [شنگل ] (ص.) شوخ و 
=== BQT v2 sarun ===
BQT_v1_pages.txt:10010:مسرونشد (4) . آن جدا توان کرد . 4
BQT_v1_pages.txt:11146:سرون آب است و از آب بر آمده است نی‌است
BQT_v1_pages.txt:19176:ببالای تو درچمن سرونیست
BQT_v1_pages.txt:20320:حردم بسرون افتد ص و شخصی را نیز گونن که
BQT_v1_pages.txt:26830:و ستین » لباسیاست‌مسرونه۹ .و کنابه
BQT_v1_pages.txt:27266:رباعی سلطان را از کدورت بسرون آورد :
BQT_v1_pages.txt:32405:رنگه بتیغ اسرون, شاخ زد و آرمید.
BQT_v2_pages.txt:520:   ‫‏‪۲ ۱ Jl andhara‬نونک للاسم رد‌عقاوم«باجنپ هدودح‪.‬یکسرون ‪ ۱۱ ۰۹۲4‬‏‪G.‬ها‪11‬خا‪_1‬‬
BQT_v2_pages.txt:917:  ‫وجزیره ایت درمیان دربا؟‪ -۱‬و انسرون دهابرا‬          ‫تکلتمایی است که هوشنک درعلم حکمت‌عملی‬
BQT_v2_pages.txt:4393:     ‫سرون آوردن آب وحر آن کنند‪-‬‬                            ‫کودی استوانه شکل عم‌قی که در زمن جهت‬                    ‫‪۱‬‬
```


## [2026-09-06T16:17:27.953Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 BQT_v2_pages.txt; grep -n \"pdf page\" BQT_v2_pages.txt | head -3; grep -n \"pdf page\" BQT_v2_pages.txt | tail -3"
}
```


### [2026-09-06T16:17:28.026Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
```


## [2026-09-06T16:17:29.616Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1130 2>&1 | head -60"
}
```


### [2026-09-06T16:17:31.438Z] TOOL RESULT

```
no scan of BQT covers printed page 1130 (see 'scans' in refs_online.json)
```


## [2026-09-06T16:17:33.544Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d.get('scans'),ensure_ascii=False,indent=1))\nprint(d.get('page_offset'))\nprint(d.get('lookup_hint'))\n\""
}
```


### [2026-09-06T16:17:35.274Z] TOOL RESULT

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
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-06T16:17:41.282Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (585,586,587,588,589):\n    print('==== leaf',i,'====')\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-06T16:17:43.278Z] TOOL RESULT

```
684
==== leaf 585 ====
                                                                                                                         ‫‪٩۷۷۴‬‬

‫و زلد گی و تری‬                ‫و زای هوز ‪ ,‬کنابه از حات‬                                                       ‫وقصود است‪.‬‬
                                                                                                                      ‫از مدعا م‬
 ‫وناز کی عیش ‪ -‬وجوان صاحب دولت وکامکار ‪-‬‬
                                                                              ‫و معامله‬         ‫از سراسیمه شدن و ترك دادن م‬
                                                ‫‪۰‬‬   ‫باشد‬      ‫ویادشاه‬




 ‫سر سری = بر وزن مرمری ‪ ۰‬مردم‬                                                                                     ‫و مردن باشد ‪١‬‏‬
 ‫فرومایه راگوبند ‪ -‬و ست گرفتن‌کارها ورعایت‬
 ‫آا را بواجبی نکردن ‪ -‬وکار آسان‌باشد‬
                                   ‫حقوق ه‬                                                      ‫کار و مپم و مقصود ومدعا باشد ‪. ۳‬‬
‫بی فکر‬       ‫سڪخن‬      ‫و‬    ‫کنابه از کار پی تامل ‪-‬‬               ‫و‬   ‫_‬
                                                                             ‫سرر = بفتح اول و ثالی و سکون زای‬
‫الفهم‪ -‬واسب‌سربع السیر‬               ‫ربیهوده‌رخام ‪ 6‬وسر‬
                                                                             ‫انند که بنابان بدان کچ‬
                                                                                                  ‫شلددار (‪ » )۱‬ماله گرو‬
       
==== leaf 586 ====
   ‫)‪۷۱‬ات‬

‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬
                                                                                     ‫شتاچه‬
                                                                                         ‫لبریز اس‬
   ‫آردثور‬
        ‫بلخکه کلهای سفید مابل بسرخی دا‬
‫و کی گونند کل ان‬          ‫آزاد درخت ءیگوند‬
                                                    ‫سر شب = بروزن هرشب ؛ بمعنی‌شاهین‬
                       ‫درخت سر شك نام دارد ©‬
                                                                    ‫باشد وآن جالوربست شکاری ‪.‬‬
 ‫سر شك ‪ ۲‬تش ه کنابه از فطرحامی‬                      ‫بکر اول و انی بر وزن‬            ‫سر شت ‪۲‬‬
          ‫می‌چکد‪.‬‬    ‫است که از هیزم تر اش‬           ‫بهشت ‪ ,‬خلقت و طیئت و هاب طبع و طبیمت ‪۴‬‬
 ‫ترشی‬   ‫کنابه از‬    ‫انگیین =‬     ‫‪2‬‬                   ‫غطشوته‬
                                                          ‫وخوی آدمی راگویند ‪ -‬وبمعنی مآخلو‬
                                                                ‫و ماضیآغشته کردن هم حست‪* .‬‬
 ‫رسکه‬
    ‫چواشنیی است که مرکب ازآب وعسل و‬
               ‫باشد ‪ -‬و دوشاب را نبزگفته‌اند‪.‬‬      ‫ثالث بروزن فرقف ‪ .‬نام‬           ‫ح‬
                                                                                   ‫ففت=‬
                                                                                      ‫رش‬‫سب‬
‫سرشك شور ‪ -‬بکسکان‪ .‬کناب‬                            ‫غله‌ایت شبی
==== leaf 587 ====
                                                                                                     ‫‪۷۱۲6-‬‬

‫است وآنرادای ترکی نیز خواند؛ ویکسر لول‬                    ‫باشد که‌در‬     ‫وآن برده‌ای‬       ‫اة‬    ‫سرشکوان‬        ‫نمی‬


                                                                                ‫پیش عروی آویزند ‪.‬‬
‫سرغینه ‪ = ۴‬بروزن چرمینه ‪ ۰‬بمعنی‬                            ‫شروی = بر وزن بدبوی * سرتراش‬    ‫س‬
                                                           ‫و حجام وا گوند ‪ -‬و نوعی از گل هم هت که‬
 ‫سرغین است که ای تر کی باشد و آترا سوردلی‬
                                                                          ‫بدان سرشوبند وگل سرشوی کوبند‪.‬‬
‫»‬       ‫‪ -‬بفتح اول وثانی بروزن صدف‬      ‫سرف‬

‫کردن‬       ‫درد گلو وسنه را گونند که بسب سرفه‬
                                                           ‫نقشی و شانی است که در‬                    ‫شیت‬
                                                                                                      ‫ررا‬
                                                                                                        ‫قن و‬
                                                                                                           ‫شی‬
                                                                      ‫حاشية قرآن دجهت هر ده آ مت كلاد ‪٩‬‏ ‪.‬‬
‫بهم رسیده باشد ؛ و نم اول و تالی هم‌باین‌معتی‬
‫رض‌اول‬          ‫خار ددن‌کام آمده ارت‬    ‫‪ -‬وهم نمی‬            ‫سر عطه آدم ‪ ۰‬کنابه از ی‬

==== leaf 588 ====
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
                        ‫جپانگیری بفتح‌کاف س‬              ‫و سکون حای‬                     
==== leaf 589 ====
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
```


## [2026-09-06T16:17:52.925Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',errors='replace').read().split('\\f')\nimport re\nfor i in range(588,600):\n    if 'سرون' in t[i] or 'سرو ' in t[i] or 'کرگدن' in t[i]:\n        print('==== leaf',i,' page~',i+543,'====')\n        print(t[i][:2500])\nEOF"
}
```


### [2026-09-06T16:17:55.192Z] TOOL RESULT

```
==== leaf 589  page~ 1132 ====
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
                                                             ‫(‪ )۱‬چك ‪ :‬ژد و
==== leaf 591  page~ 1134 ====
                                                                                               ‫هه‬‫‪-‬‬

 ‫سر مو تثه دبا تای قر(شت‪)۱‬بروزن‬                       ‫وب‬
                                                       ‫رلکم‬
                                                          ‫طف‬                ‫ان‬
                                                                             ‫هردمو‬
                                                                                 ‫آو‬        ‫مك‬
                                                                                            ‫مهاپیش‬
                                                                                                 ‫شد‬
     ‫شیوب و شور وغوغا باشد‪.‬‬
                          ‫آعت‬
                            ‫زلبورك ‪ .‬بم‬             ‫طفلی را‬           ‫نت‬
                                                                       ‫ااکر‬
                                                                          ‫وهدو‬
                                                                             ‫تك ن‬
                                                                                ‫سبکرنار مام‬
‫سر مور ه = بروزن هر روزه ‪ ۰‬کفشی‬                     ‫گرفتن همان خود سربر کنار مامك نهد وبازی‬
                                                                                         ‫را ازسر کیرد ‪.‬‬
‫باشد که بر بالای موزه پوشند و در ماوراوالثهر‬
                                 ‫‪.‬‬       ‫متعارفت‬    ‫سرماهی ‪ - ۲‬بر وزن خرکاهی ‪.‬‬
‫سرمه ‪ -‬بضْم اول و فتح ثالث ‪ ,‬معروف‬                 ‫ماهیانه و مقرری باشد که درهرسر ماه بنوکر‬
       ‫و‬                   ‫ی‬         ‫ا‬        ‫اخ‬
                                                        ‫وامثال آن دهند وآلرا عربی مشاهره گوند‪.‬‬

‫و نام قربه‌ای هم حت از قرای فار یکه درآن‬             ‫سرهج ‪ - ۲‬بنتحاول و میمسوکون‬
                               ‫سرمه خیزد ‪.‬‬           ‫ثالی و جیم » دوابی است که آنرا اسفناج رومی‬
‫سرمة خاك لین ‪ -‬سرمه ای بود که‬                       ‫هر دو میباشد ‪.‬‬           ‫ایی‬
                                                                               ‫حیرو‬
                                                                                  ‫صتال‬
                                                                                     ‫گوبند وآن بس‬
‫خسرو پروبز داشت ‪ .‬کوبند هر که بکباردرچشم‬            ‫و بجوشاننده‪ .‬آب آرا‬             ‫صحرایی آنرا نکد‬
‫زلی که مشیمه درشکمش مانده باشد بشورد در کشیدی تا بك
==== leaf 592  page~ 1135 ====
   ‫‪ ۳۱‬ات‬
 ‫و لبلابرا نیزکوبند‪,‬وآن‬    ‫حطی حم آمده است ‪-‬‬
                                                  ‫سر نامه = بروزن هتکامه ‪ ۰‬لجه‌بر سر‬
‫رستنیی باتد که بردرخت پیچد و بعربی هشقه‬                ‫لینده‬
                                                           ‫اال‬
                                                             ‫رلسفل‬
                                                                 ‫رمح‬
                                                                   ‫بان‬
                                                                     ‫کتات‌ها لومند که در قل‬
 ‫خوانند ؛ و باين معتی باثالی مفتوح ایز بنظر‬
    ‫تنی‬‫ش فنو‬
           ‫کلهٌ‬
              ‫آمده است ‪ -‬و فنی باشد ازجم‬
                                                   ‫و ی کوبند سرنامه عنوان است یآعنچه‌بر‬
                                                                               ‫بالای نامه فوبسند‪.‬‬
 ‫‪«.‬گیری » وآن چنان است که کشتی گیر بای‌خود‬

 ‫را بپای دبگری بندکند و اورا بینداژد و آنرا‬         ‫رخکه‬
                                                       ‫سوکلون آ‬
                                                              ‫وما‬
                                                                ‫سر نای ‪ = ۲‬ض‬
 ‫بعربی شغزییه خوالند ‪ -‬و بمعنی ربسمالی باشد‬       ‫‪ ۰‬بمعنی نای رومی است که سرنا‬        ‫بیاحطشید‬
                                                                                             ‫با‬
 ‫خاك پنهان‬      ‫ور‬
                 ‫زدی‬
                   ‫رکنن‬‫دفه‬
                         ‫که بکر آنرا حل‬                         ‫باشد ؛ و محذف الف هم‌آمده است‪.‬‬
 ‫سازند و سر دیگر را شخصی گرفته در کمین‬            ‫سر نج ‪ = ۴‬بکر اول و انی و سکون‬
 ‫بنشیند تا آدمی با جانوری که پای درآن میان‬         ‫ثالث و جيم » سنج را کوبند‪ .‬وآن دوپاره روی‬
     ‫نید آن شخص بوی خود کشد واورایگیرد‪.‬‬
                                                  ‫تنک‌باشد مانند طبق بکنیاره‌وبریشت آن قبه‌ای‬
  ‫‪.‬ر‬
   ‫سر و له = بفتح الث و بای ابجد س‬                ‫سازند و بتدی برآن‌تعبیه کنند و بردست گرفته‬
 ‫کرده وریش فيد پاسبانانرا گویند‪.‬چه لوبه بر‬        ‫زلند تا صدا در آید و بشتر بالقاره‬       ‫گیگ‬
                ‫وزن توبه بمءنی پاسبان است ‪. ۴‬‬      ‫و دهل وامثال آن‌لوازند ‪ -‬و قلمی وسرب‌سوخته‬
  ‫سر شوت ‪ -‬حک ازل وفضای‌ازل‌است‬                    ‫را کلبوزبند وآن‌رنگی است که نقاشان‌ومصوران‬
         ‫بعتی آلجه در روز ازل تفدیر شده باشد‪.‬‬     ‫بکار برند و آن درفایت حمرت میباشد چه باطن‬
 ‫بروزن‬                                           
==== leaf 593  page~ 1136 ====
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
 ‫وغوغا باشد ؛ و باين معثی ب
==== leaf 594  page~ 1137 ====
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
   ‫*ه‪-‬لوی ‪١٥4٤1۷۲45‬‏ و بدانجا آثار فصری اعزهد ساسالی است ‪.‬
==== leaf 596  page~ 1139 ====
  ‫‪۱۳‬‬                                                                                        ‫سروشه‬

                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
 ‫وح‌اول بمعنی‌سرین است که شت‌گاه‌مردمان‬            ‫=‬     ‫ومصالح آن‌روز می‌پردازد‪ .‬بنابرآن بجهت‌شرف‬
                         ‫وکفل چاربابان باشد ‪۰ ۴‬‬        ‫آن روز راعد کنند وجشن سازند » ولیزهر کدام‬
 ‫وتا‬      ‫ر‬     ‫کاله‬       ‫ك‬        ‫سر ونار‬             ‫از سروشها بمحافظت جوهری وعنصری مقرراست‬
  ‫راگوبند چه ناز بمعتی لورسته عم آمده | ت‬                ‫چنانکه خرداد بآرب مو کل است و اردیبهشت‬
‫سوروبرا یزکوبند که شاخپای آن بهر طرف‬                    ‫بآرتش و مرداد براشجار وبافی سروشرابمحافظت‬
                                                       ‫آیچه در بل نام آن سروش مقرر ات ‪ -‬ونام‬
                                        ‫ماوزسیقی ‪.‬‬      ‫ن بدست‌اوست‬   ‫اند‬‫گست ب‬
                                                                             ‫ملکی دز هست که ربا‬
                                                       ‫و تدییر امور و مصالحی که در روز سروش وافع‬
   ‫کوون‬
      ‫سروق = بفتح اول وضم اسنی‬
‫که شاخ‬        ‫است‬   ‫سرون‬       ‫ثالث و تحتالی ‪« ۰‬معنی‬
                                                         ‫رموز حفدهم باشد‬
                                                                       ‫است ‪ -‬و نا‬     ‫لق‬
                                                                                       ‫عدو‬
                                                                                         ‫تب‬‫عود‬
                                                                                             ‫می‬
                                                       ‫از هرماه شمسی ‪ .‬نك است دراعن روزدعا کردن‬
‫ویضم اول سرین و کقل‬        ‫‪-‬‬    ‫کوسفند و کاوباشد ©‬
                                                                   ‫ونبشآکده رفتن و بافی امور بداست‪.‬‬
                                    ‫هرد وچاروا ‪٩‬‏ ‪.‬‬

‫سر و یس د بااول و تحتالی مجپول بر‬                        ‫وه ‪ = ۱‬بن اولوفتح شین‌رشت‪.‬‬
                                                                                  ‫سر ش‬
‫وزن نوکیسه » قوس قزح رکاویند ‪ - ۷‬ومهر‬                    ‫بممنی سروش است جکبهرئیل باشد خصوصاً ‪-‬‬
                    ‫های سنگین را هممیگوند ‪.‬‬                                   ‫وملائکةٌ دیگر عموماً ‪.‬‬
‫سر ‪ = ۵‬بفتح اول وثالی » زر رایج تمام‬                     ‫سر ول ‪ -‬بفتح اولبروزن ملول‪ ,‬بمعنی‬
 ‫تسف‬    ‫
==== leaf 599  page~ 1142 ====
                                                                                          ‫پا احد‬

‫شنجرف سوخته است » بعنی شنجرف عملی‬                    ‫بخورند وبعد‬       ‫مات‬
                                                                         ‫منداوب‬
                                                                              ‫سبزی وتاز کی بیز‬
 ‫که آنرا اسزیماب سازند نآهنکه اکزان‬                 ‫کفش‪-‬‬     ‫سازند و‬   ‫کنند وآرد‬    ‫از رسد کی خشك‬


                                      ‫برآ ورند ‪.‬‬     ‫چبانند ‪٩‬‏ ‪-‬‬       ‫ان‬
                                                                        ‫بزدها‬
                                                                            ‫چی‬        ‫فان‬
                                                                                        ‫حناو‬
                                                                                           ‫کصرا‬

   ‫لی‬
    ‫االی‬
       ‫تر ث‬
          ‫حلوک‬
             ‫تاو‬
               ‫ونم‬
                 ‫سرلن ‪- ۴‬ب‬                                                                    ‫‪.‬‬    ‫جلد‬
 ‫ولون ساکن » شتگاه آدمی‪ -‬و کفل وساغری‬
                                                    ‫سر لع ه بفتح اول و کر انی وسکون‬                  ‫‪۰‬‬
                      ‫حیوانات دنکر ‪ ۴‬ك‬
                                                     ‫تحتانی ر غین اقطه‌دار ‪ ۰‬خوشه انگور بردأله‌باشد»‬

  ‫سر یانفکندن کدنایه اززاچانرو‬                           ‫بند خوش انگوری باهشدنکوهز‬
                                                                                 ‫وضی‬
                                                                                   ‫کبع‬
                                                                                     ‫و‬
                           ‫شتن باشد ‪.‬‬     ‫مرب‬
                                            ‫و‬                            ‫‪.‬‬   ‫درست لشده بادث‬       ‫دالهاش‬

‫سر بنگاه = بمنی مطلق شتگاه باشد‬                     ‫سر یقون ‪ « ۲‬بفتح اول و ضم قاف‬
  ‫عموماً ‪ -‬وبمعنی تخت بادشاحان پود خصوصاً ‪.‬‬          ‫وسکون واو و لون » لغتی است سربالی وبمعنی‬


                                              ‫بيان دهم‬

 ‫سز گی پ=قتح اول و سکون‌انی وکاف‬                    ‫سز ا * ‪ .-‬بفتح اول بروزن جزا ء پاداش‬
 ‫سختی ورلج‬         ‫نی‬
                    ‫مهع»‬ ‫فارسی بتحتانی رس‬
                       ‫بید‬                          ‫را‬     ‫فق‬
                                                            ‫وارا
```


## [2026-09-06T16:18:09.470Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',errors='replace').read().split('\\f')\nprint(t[596][-1800:])\nEOF"
}
```


### [2026-09-06T16:18:11.237Z] TOOL RESULT

```
ا هممیگوند ‪.‬‬                                   ‫وملائکةٌ دیگر عموماً ‪.‬‬
‫سر ‪ = ۵‬بفتح اول وثالی » زر رایج تمام‬                     ‫سر ول ‪ -‬بفتح اولبروزن ملول‪ ,‬بمعنی‬
 ‫تسف‬    ‫عبار باشد»وآن نقیض قلب است که اسره‬               ‫حقد باشد»‌وآن بدکوبی و غیبت مردم در خاطر‬
‫‪ -‬وآب عمیقی که از سر مردم بگذرد ‪ -‬و هر‬                   ‫نگاهداشتن است وطالب فرصت‌بدی کردن بودن‪.‬‬

 ‫چیزی لیکو و راست و بی عیب ‪ - ۸‬و خلاصه‬                   ‫سر ون = بفتح‌اول بروزن زبون » بمعنی‬

                     ‫‪:‬‬   ‫‪ :‬سرو‬    ‫رك‬    ‫‪۴‬‬        ‫ترديك لفط اوستابی «سروش» («‪.‬م‪۲ ).‬‬      ‫‪۱‬‬

               ‫سرولی است بر رسته‌چون کر گدن‪.‬‬                 ‫ز پیشانی هربك از مرد وزن‬
   ‫نظامی کنجوی‪ .‬ک«نجینه ‪۸۸۰‬‬
   ‫‪ = ۴‬سرین ( «م‪ » ) .‬اوستا ‪ ( 1002۳3 -‬تپیگاه ) » پهلی ‪)ras‬‏ ‪01۲25 ۰‬‬
   ‫(سرین)‪,‬هندی باستان ‪( 1۵۵۳9 -‬سرین‪ ,‬ران » تپیگاه) ل»توانی ‪ , 5101212۹‬لانینی ‪610016‬‬
   ‫بوتانی ‪ » )( »51061‬بلوچی ‪ ( 0۵۲25‬کمر ؛ تپیگاه ) «اسشق ‪ .۷۳۷0‬هوبشمان‌کوید ‪ :‬سیت‬
       ‫شن‬
        ‫دایومن‬
             ‫فظرسی «سرین» ‏ بلوچی ‪ 06725‬از ‪ # 6۳5‬و فارسی «سرون »از ‪ ۵ 00۲5‬بر‬
                                                                           ‫یت «حوبشمان ‪: ۷۳۲۷‬‬
               ‫گرچه برتابد آن میان وسرون‪.‬‬                      ‫کفش با سلاح بشکفتم‬
   ‫شهد بلخی‪«.‬لفت فرس ‪۹۷۳٩‬‏ ‪.‬‬
                                   ‫‏‪ « Cupressus sempervirens = ¢‬یتباث ‏‪. “AY‬‬
   ‫‪ - ۷‬مصحفهسد که»‬                ‫‪ -‬رك‪ :‬سرون ‪٩‬‏ سرین ‪.‬‬            ‫‪ _ ۵‬رك ‪ :‬سرو ‪ ۰‬سرون ‪.‬‬
                                                                              ‫س دکیس («‪.‬م‪۱ ).‬‬    ‫>‬

               ‫پیرزن کرک باشد‪ .‬او بره بود‪.‬‬                  ‫‪ - ۸‬مادرم کفت کو زلی سره بود‬
       ‫تظامی کنجوی‪ «.‬کنجینه‪»۸۸‬‬
   ‫(برهانقاطع ‪)۷۴۱‬‬
```


## [2026-09-06T16:18:34.667Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"surū\\|surú\\|sarūn\\|sarún\\|surûn\\|Horn'\" HRN.txt | head -20; echo \"=== leaf 183 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==184' HRN.txt | head -50"
}
```


### [2026-09-06T16:18:37.174Z] TOOL RESULT

```
6406:734. serTfy sm% serfm *Horn'.
=== leaf 183 ===
— 162 -
732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
{*sires)j siriäem 'Leim* *).
aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
phlv. sristan^ sresct (PPGh); ai. skr. [/^rres-^ (^les-^
rlisyatl Verbinden, zusammenfügen'.
sar. xlr/'am ^vermischen, mengen etc.'
733. sirUk "Tropfen .
aw. sraska- 'Hagel' (Justi); für srasc- nimmt
Geldner, KZ. 27, 252 die Grundbedeutung giessen*
an, aw. sraska- bedeutet vielleicht 'Reif, Nebel'.
Unsicher.
734. serTfy sm% serfm *Horn'.
aw. srvä' *Klaue, Hörn'; phlv. srüh (d.i. srtn^), snw.
bei. srunbe^ surum 'Huf (348) -).
7»>r>. suvTiden singen, Praes. seräy-em^ seräf/tden 'singen;
sprechen (Sahn. I, 70 Vers 156), seräyis^ siirüd Lied'.
aw. l'^sruv-, (^aus. srävayeüi; phlv. srüfan 'recitiren',
srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
^rävdyati.
wa/. sirav-am^ sar. nasrav-am 'recitiren*.
736. seröä 'Engel' (Vis und RämTn, S. 37, V. 4 v. u.).
aw. Sraosa-; phlv. Srös, vergl. asrös ungehorsam*
(aw. asraosa-),
737. snrTniy surtn 'Hinterbacken, Hinterer.
aw. sraoni- *Hüfte*; phlv. sarük, vd. 8 (178) (181),
sarin 'Hinterer (Bund.) , sar'mak (PPGl.) ; ai. grmü'
'Hinterbacke, Keule, Hüfte'; lit. szlaimis, lat. cliinis,
gr. XA0I7C,' (?), ahd. hlatm ^).
bei. saren 'Lenden, Hüften* (338, wohl in sarzn zu
ändern, vergl. Hübschmann, ZDMG. 44, 555 unter
No. 2) ; wa/. simj, siyn. saun, sar. xdiin,
738. seztden sich ziemen, passen, sezä, sezäyiden.
phlv. sacifan^ sacPt (päz. sazed, saSSd), sacäk.
*) Afy. LW. s(fle/ -, i<(dex'
^) Geiger wirft np. sum^ suub *Huf* fälschlich mit serüu *Horn*
zusammen; vergl. No. 745.
*) Arm. srunl^ ^Schienbeine, Waden', das auch seiner Bedeutung
nach nicht paast, gehört nicht liierher (Fl übschmann, No. 260).
```


## [2026-09-06T16:18:59.901Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sālār\\|sälär\\|salar\\|sārbān\\|särbän\\|sarbán\\|afsar\\|afsär\" HRN.txt | head -20"
}
```


### [2026-09-06T16:18:59.948Z] TOOL RESULT

```
1281:aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
1284:phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
6084:692. sälär 'Anführer'.
6086:(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
15618:artestärän sälär 24.
16826:sälär 692.
```


## [2026-09-06T16:19:02.792Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1275,1292p' HRN.txt; echo \"=== 692 ===\"; sed -n '6080,6098p' HRN.txt; echo \"=== sarbān ===\"; grep -n \"Kameeltreiber\\|Kameltreiber\\|sarban\\|särbän\" HRN.txt | head"
}
```


### [2026-09-06T16:19:02.860Z] TOOL RESULT

```
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
werden kann.
*) ewsün (Vullers).
=== 692 ===
'Herbst, Jahr (mit Zahlen)'.
oss. d. särdä, t. särd 'Sommer* (223).
Allg. entlehnt: kurd. af/. bei. (235) säl; wa/. sdl,
sar. säL
692. sälär 'Anführer'.
aw. *särö,dära' ; phlv. sälar, \idQa(jTaöa()av\öaXdvrji^
(Procop. Pers. I, 7, 11 u. ö.), arm. LW. s(dar, spajsalar,
np. serdär (phlv. sardär) ist eine junge Bildung, da
man sonst seryär erwarten müsste.
Vergl. No. 726.
693. sämän 'Ordnung, Grenze; Hausgerät etc.'.
phlv. sämän, bezw. sahmän (z. B. AV. 'boundary-
mark'), arm. LW. sahman o()ocj oQ^o/ndc^ -nQoacayua (de
Lagarde, No. 1934).
Zu ai. [/'gad' etc. (Fr. Müller, WZKM. 5, 262).
(\)8än 'Wetzstein.
Siehe efsan (No. 98) 0.
*) Nachträglich sei hier noch np. sumhäde (goschr. sunb"), Käs.
K. sunbötä, arab. LW. sunbäSaj^ sunhäSat (Bibl.' geogr. arab. IV, 277)
=== sarbān ===
```


## [2026-09-06T16:19:21.097Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:19:21.123Z] TOOL RESULT

```


```


## [2026-09-06T16:19:26.000Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B9%9Bh%E2%82%82nom",
 "prompt": "What is the PIE root for 'horn/head' given here (*ḱerh₂- ?), its meaning, and the descendants listed (Latin cornu, Greek keras, Avestan, Sanskrit śṛṅga)?"
}
```


## [2026-09-06T16:19:26.586Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carat",
 "prompt": "Full etymology of carat: the chain from Greek keration through Arabic qirat, Medieval Latin, Italian, French, English. Dates."
}
```


### [2026-09-06T16:19:28.041Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T16:19:34.014Z] TOOL RESULT

```
# Etymology of Carat

The word "carat" traces back through multiple languages to ancient practice. It originated from the Arabic *qirat*, meaning "fruit of the carob tree" and also "weight of 4 grains." This passed into Medieval Latin as *carratus* and Italian as *carato*, then into Old French *carat* by the 14th century, eventually entering English in the late 1400s.

## Historical Significance

"Carob beans were a standard in the ancient world for weighing small quantities." The Greek term *keration* (carob seed) literally meant "little horn," deriving from *keras* (horn). This connection to horns stems from the Proto-Indo-European root *ker-.

## Modern Usage

Initially, carat denoted gold fineness, with the measurement representing proportions of pure gold. By the 1550s, it became standardized as gold purity measurement. Later, "as a measure of weight for diamonds or other precious stones, carat is attested from 1570s in English."

In contemporary American English, *karat* specifically refers to gold alloy proportions, while *carat* measures precious stone weight.
```


## [2026-09-06T16:19:37.586Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1er-",
 "prompt": "List the reconstructed roots spelled ker-/ḱer- here and which one means 'head, horn'. Give its descendants."
}
```


## [2026-09-06T16:19:38.230Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/migraine",
 "prompt": "Full etymology of migraine: Greek hemikrania, Late Latin hemicrania, Old French migraine/migraigne, Middle English. Dates."
}
```


### [2026-09-06T16:19:42.935Z] TOOL RESULT

```
# Proto-Indo-European ḱer- Roots

Based on the Wiktionary page, there are **three distinct reconstructed roots** spelled *ḱer-:

1. **ḱer- (ḱerh₁-, ḱreh₁-)**: "to grow, to make grow, to nourish"

2. **ḱer-**: "to plait, weave" or "rope, string"

3. **ḱer-**: Alternative reconstruction of *ḱerh₂-

## Regarding "Head, Horn"

The page does not contain any root meaning "head" or "horn." None of the three *ḱer-* entries documented here carries that semantic value. The first relates to growth/nourishment, the second to weaving/fibrous materials, and the third is noted as an alternative form of another root.

If you're seeking a Proto-Indo-European root for "head" or "horn," it would be listed under a different entry—not among these *ḱer-* reconstructions.
```


### [2026-09-06T16:19:44.342Z] TOOL RESULT

```
# Etymology of Migraine

The word "migraine" originates from Late Latin *hemicrania*, meaning "pain in one side of the head." This term combines Greek elements: *hēmi-* ("half") and *kranion* ("skull").

The word entered English in the late 14th century as *migrane*, borrowed from Old French *migraine* or *migraigne*. The etymology reflects the condition's characteristic feature—pain affecting one side of the head rather than the entire head.

An alternate form, *megrim*, became common from the 15th century onward but is now considered archaic or obsolete. Beyond its medical sense, *megrim* was also used to describe depression or whimsical fancies.

The Greek root *kranion* connects migraine to other medical and anatomical terms, tracing back to the Proto-Indo-European root *\*ker-* meaning "horn" or "head."
```


## [2026-09-06T16:19:49.673Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1erh%E2%82%82-",
 "prompt": "What is the meaning of *ḱerh₂-, and what derived terms/descendants are listed (e.g. *ḱrh₂nom horn, *ḱérh₂s head, Latin cornu, Greek keras, Avestan sarah/sruua, Sanskrit śṛṅga)?"
}
```


## [2026-09-06T16:19:51.237Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%B1%D8%A8%D8%A7%D9%86",
 "prompt": "Persian ساربان: etymology and meaning. Does it derive from sār 'camel' or from sar 'head'?"
}
```


### [2026-09-06T16:19:56.107Z] TOOL RESULT

```
# Etymology of Persian ساربان (sārebān)

Based on the Wiktionary entry, the word does **not** derive from either "sār" (camel) or "sar" (head). Instead, it is "Borrowed from either Parthian or Sogdian" sources, both meaning "caravan."

The etymological path traces to ancient trade languages rather than Persian roots. Both proposed source languages yield the same semantic field: the word refers to someone leading or managing caravans, not to camels or heads specifically.

The two documented meanings are:
1. A caravan leader (archaic)
2. A camel-keeper (archaic)

These occupational definitions align with the caravan-related etymology from Parthian or Sogdian, not from Persian morphological elements.
```


### [2026-09-06T16:19:57.081Z] TOOL RESULT

```
# Proto-Indo-European Root *ḱerh₂-

## Primary Meanings

The reconstructed root *ḱerh₂- has three distinct etymologies:

1. **"Head, top; horn"** - the most prominent sense
2. **"To break, shatter"**
3. **"To mix"**

## Major Derived Terms and Descendants

**Nominal derivatives related to "head/horn":**
- Ancient Greek: κέρας (kéras, "horn")
- Latin: cornū ("horn"), derived from Proto-Italic *kornū
- Sanskrit: शृङ्ग (śṛ́ṅga, "horn, tusk")
- Old Irish: sirwis (from Proto-Balto-Slavic)
- Lithuanian: kárvė ("cow," from collective form)
- Old Armenian: սար (sar, "tip, top; mountain")

**Animal-related terms:**
- Proto-Celtic *karwos and Proto-Germanic *herutaz both mean "deer, stag"

**Other formations:**
- Latin cernuus ("head-nodding," compound with *new-, meaning new)
- Greek κεραυνός (keraunós, "thunderbolt," from "shattering")
- Latin crābrō ("hornet," literally "the horned one")

The root demonstrates extensive branching across Indo-European language families with semantic consistency.
```


## [2026-09-06T16:20:04.058Z] TOOL CALL #54: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B3%D8%A7%D8%B1%D8%A8%D8%A7%D9%86&action=raw\" | head -60"
}
```


## [2026-09-06T16:20:05.026Z] TOOL CALL #55: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B3%D8%B1%D8%B4%D8%A7%D8%B1&action=raw\" | head -40; echo \"=== afsar ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A7%D9%81%D8%B3%D8%B1&action=raw\" | head -40"
}
```


### [2026-09-06T16:20:05.989Z] TOOL RESULT

```
==Persian==

===Alternative forms===
* {{alt|fa|ساروان|tr=sârevân}}

===Etymology===
Borrowed from either {{bor|fa|xpr|𐫘𐫀𐫡𐫤||caravan|ts=sārt}} or {{bor|fa|sog|tr=sʾrth|ts=sārt|t=caravan}}.

===Pronunciation===
{{fa-IPA|sāri`bān}}

===Noun===
{{fa-noun|tr=sârebân|pl=ساربانان|pl2=ساربان‌ها}}

# {{lb|fa|archaic}} [[caravanner]], [[caravaneer]] {{gloss|leader of caravan}}
#* 12th century, {{w|Saadi}}, ''Divan'' (Ghazaliyyat), [https://ganjoor.net/saadi/divan/ghazals/sh268/ 268]:
#*: {{quote|fa|ای '''ساربان''' آهسته رو کآرام جانم می‌رود <br> وآن دل که با خود داشتم با دلستانم می‌رود|tr=ay '''sāribān''' āhista rān k-ārām-i jānam mē-rawad <br> w-ān dil ki bā xud dāštam bā dilsitānam mē-rawad}}
# {{lb|fa|archaic}} [[camel]]-[[keeper]]
#* 11th century, {{w|Abulfazl Bayhaqi}}, ''{{w|Tarikh-i Bayhaqi}}'', Adib, page 453, cited in "ساربان", ''Dehkhoda Dictionary'':
#*: {{quote|fa|امیر حاجب سباشی را گفت '''ساربانان''' را بباید گفت تا اشتران دوردست تر نبرند.|tr=amir hājib sabāšī rā goft '''sāribānān''' rā bibāyad goft tā ušturān dur-dast-tar nabarand.|t=Amir Hajib told Sabashi that the '''camel-keepers''' should be told not to bring the camels any farther.}}

====Synonyms====
* {{l|fa|قافله‌سالار|tr=qâfele-sâlâr}}
* {{l|fa|کاروان‌سالار|tr=kârvân-sâlâr}}

====References====
* {{R:Dehkhoda}}

{{C|fa|Occupations}}
```


### [2026-09-06T16:20:08.299Z] TOOL RESULT

```
==Persian==

===Pronunciation===
{{fa-IPA|sarˈšār}}

===Adjective===
{{fa-adj|tr=saršâr}}

# [[brimful]], [[overwhelmed]]
#: {{syn|fa|لبریز|tr=lab-riz}}
#: {{ux|fa|'''سرشار''' از هیجان|tr='''saršâr''' az hayajân|t='''overwhelmed''' with excitement}}
#: {{ux|fa|.قلب او '''سرشار''' از عشق خداوند است|tr=qalb-e u '''saršâr''' az ešq-e xodâvand ast.|His/her heart is '''overflowing''' with the love of God.}}

====Descendants====
* {{desc|ur|سرشار|bor=1|tr=saršār}}=== afsar ===
==Gawar-Bati==

===Etymology===
{{bor+|gwt|ps|افسر}} or {{bor|gwt|ur|افسر}}, from {{der|gwt|en|officer}}.

===Noun===
{{head|gwt|noun|g=|tr=afsar}}

# [[officer]]

{{C|gwt|Occupations}}

==Persian==
{{was fwotd|fa|2025|February|20}}

===Pronunciation===
{{fa-IPA|af`sar}}

===Etymology 1===
{{inh+|fa|pal|tr=’p̄ysl|ts=aꞵesar}}. Further possibly containing a deformed prefix to {{m|fa|سر|tr=sar|t=head}} and a clipped ending after a {{inh|fa|ira-pro|*upasarah}}.

====Noun====
{{fa-noun|tr=afsar|pl=افسرها}}

# {{C|fa|Headwear|Monarchy}} {{tlb|fa|archaic}} [[crown]], [[diadem]]
#: {{syn|fa|تاج|tr=tâj|کلاه|tr2=kolâh|دیهیم|tr3=deyhim|اکلیل|tr4=eklil}}
#* '''10th Century CE''', [[w:Ferdowsi|Ferdowsi]], ''[[w:Shahnameh|Shahnameh]]''
#*: {{quote|fa|که جاوید باد '''افسر''' و تخت او<br>ز خورشید تابنده‌تر بخت او|tr=ki jāwēd bād '''afsar''' wa taxta 'ō<br>zi xwaršēd tābanda-tar baxta 'ō|t=May his '''crown''' and throne be ever-lasting<br>May his fortune be brighter than the sun}}

=====Descendants=====
* {{desc|az|əfsər|bor=1}}
* {{desc|ota|افسر|tr=efser|bor=1}}
** {{desc|tr|efser}}

=====See also=====
* {{l|fa|افسار|tr=afsār|t=headstall}}

===Etymology 2===
{{ety|fa|:bor|en:officer|text=+|tree=1}}
```


## [2026-09-06T16:20:17.157Z] TOOL CALL #56: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%E0%A4%B6%E0%A5%83%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A4%B5%E0%A5%87%E0%A4%B0&action=raw\" | head -40; echo \"=== ARABIC zanjabil ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B2%D9%86%D8%AC%D8%A8%D9%8A%D9%84&action=raw\" | head -60"
}
```


### [2026-09-06T16:20:19.416Z] TOOL RESULT

```
==Sanskrit==

===Alternative forms===
{{sa-alt}}

===Etymology===
{{etymon|sa|:der|pra:𑀲𑀺𑀁𑀕𑀺𑀯𑁂𑀭|:influence|शृङ्ग॑|tree=1}}
{{sanskritism|pra|𑀲𑀺𑀁𑀕𑀺𑀯𑁂𑀭}}, with influence of {{l|sa|शृङ्ग|t=horn}}, borrowed from {{bor|sa|oty|𑀇𑀜𑁆𑀘𑀺𑀯𑁂𑀭𑁆|t=ginger root}}, equivalent to {{cog|ta|இஞ்சி||ginger}} + {{l|ta|வேர்||root}} (whence {{cog|ta|இஞ்சிவேர்|t=ginger root}}).

===Pronunciation===
{{sa-IPA}}

===Noun===
{{sa-noun|m}}

# [[ginger]]

====Declension====
{{sa-decl-noun-m}}

====Descendants====
* {{desc|fa|شنگویر|tr=šangevir|alts=1|bor=1}}

===Further reading===
* {{R:MW|1087|col=2}}

{{C|sa|Zingiberales order plants|Vegetables}}=== ARABIC zanjabil ===
{{also|زنجبیل}}
==Arabic==

===Alternative forms===
* {{alter|ar|زَنْجَفِيل|زَنْجَبِير||dialectal}}

===Etymology===
{{etymon|ar|:bor|syc:ܙܢܓܒܝܠ<id:ginger>|id=plant|tree=1}}
From {{bor|ar|syc|ܙܢܓܒܝܠ|tr=zangabīl}}, {{m|syc|ܙܢܓܒܝܪ|tr=zangabīr}}, from {{der|ar|pra-sau|𑀲𑀺𑀁𑀕𑀺𑀯𑁂𑀭}}, {{m|pra-sau|𑀲𑀺𑀁𑀕𑀯𑁂𑀭}}, from {{der|ar|oty|𑀇𑀜𑁆𑀘𑀺𑀯𑁂𑀭𑁆}}.

===Pronunciation===
{{ar-pr|زَنْجَبِيل}}

===Noun===
{{ar-noun|زَنْجَبِيل|m}}

# [[ginger]]
#* {{RQ:Qur’an|76|17|passage=وَيُسْقَوْنَ فِيهَا كَأْسًا كَانَ مِزَاجُهَا '''زَنْجَبِيلًا'''|t=And they will be provided to drink a cup, the flavour/mixture of which is ginger.}}

====Declension====
{{ar-decl-noun|زَنْجَبِيل}}

====Descendants====
* {{desc|am|ዝንጅብል|bor=1|tr=zənǧəbəl|alts=1}}
* {{→}} Gurage:
*: {{desc|gru|ጃንጅብል|tr=ǧanǧəbəl|sc=Ethi}}
*: {{desc|stv|ጃንጅብል|tr=ǧanǧəbəl|sc=Ethi}}
*: {{desc|wle|ዝንጅብል|tr=zənǧəbəl|sc=Ethi}}
* {{desc|he|זַנְגְּבִיל|tr=zangəḇī́l|bor=1}} {{q|if not from Aramaic}}
* {{desctree|fa|زنجبیل|tr=zanjabil|bor=1}}
* {{desc|sw|tangawizi|bor=1}}
** {{desc|bou|sangaizi|bor=1}}
** {{desc|kam|tangaisi|bor=1}}
** {{desc|lg|entangawuuzi|bor=1}}
** {{desc|dav|sangaizi|bor=1}}
* {{desc|tig|ዝንጅብል|tr=zənǧəbəl|bor=1}}
* {{desc|ti|ጅንጅብል|bor=1|tr=ǧənǧəbəl}}

{{C|ar|Ginger family plants|Spices}}

==Hijazi Arabic==
[[File:Gingembre.jpg|thumb|upright=1.15|{{lang|acw|زَنْجَبيل}}]]

===Etymology===
{{ety|acw|:inh|ar:زَنْجَبِيل|text=+|tree=1}}

===Pronunciation===
* {{IPA|acw|/zan.d͡ʒa.ˈbiːl/}}

===Noun===
{{acw-noun|g=m|head=زَنْجَبيل|tr=zanjabīl}}

# [[ginger]]

==South Levantine Arabic==

===Etymology===
{{ety|ajp|:inh|ar:زَنْجَبِيل|text=+|tree=1}}

===Pronunciation===
```


## [2026-09-06T16:20:38.914Z] TOOL CALL #57: Bash

```json
{
 "command": "ls site/pages/256.jpg 2>/dev/null; pdftoppm -f 256 -l 256 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg256 && echo ok"
}
```


### [2026-09-06T16:20:41.085Z] TOOL RESULT

```
site/pages/256.jpg
ok
```


## [2026-09-06T16:20:41.696Z] TOOL CALL #58: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B4%D9%86%DA%AF%D9%88%DB%8C%D8%B1&action=raw\" | head -30; echo \"=== ziggiberis ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%CE%B6%CE%B9%CE%B3%CE%B3%CE%AF%CE%B2%CE%B5%CF%81%CE%B9%CF%82&action=raw\" | head -30"
}
```


### [2026-09-06T16:20:43.720Z] TOOL RESULT

```
==Persian==
{{wp|fa:}}

===Alternative forms===
* {{alter|fa|شنگویل|tr1=šangevil|شنگبیر|tr2=šangebir|شنگبیل|tr3=šangebil}}

===Etymology===
{{etymon|fa|:bor|sa:शृङ्गवेर|tree=1}}
{{bor+|fa|sa|शृङ्गवेर|tr=śṛṅgavēra}}. {{doublet|fa|زنجفیل|tr1=zanjefil|زنجبیل|tr2=zanjebil}}.

===Pronunciation===
{{fa-IPA|šangevir}}

===Noun===
{{fa-noun|tr=šangevir}}

# [[ginger]]

{{C|fa|Ginger family plants}}=== ziggiberis ===
==Ancient Greek==

===Etymology===
{{etymon|grc|:der|pra-sau:𑀲𑀺𑀁𑀕𑀺𑀯𑁂𑀭<id:ginger>|id=ginger|tree=1}}
Via unattested {{bor|grc|ira-mid|-}} from {{der|grc|pra-sau|𑀲𑀺𑀁𑀕𑀺𑀯𑁂𑀭}}, which see for comparisons.<ref>{{R:grc:Beekes|page=501|head=ζιγγίβερις}}</ref>

===Pronunciation===
{{grc-IPA|ζῐγγῐ́βερῐς}}

===Noun===
{{grc-noun|ζιγγίβερῐς|ζιγγῐβέρεως|f|third}}

# [[ginger]]
#* {{grc-cite|Diosc.||2|190}}

====Inflection====
{{grc-decl|ζιγγίβερῐς|εως|form=F-sing}}

====Descendants====
* {{desc|el|ζιγγίβερη|g=f|ζιγγίβερι|g2=n|ζίγγιβερ|g3=n|ζινζίβεριν|g4=n|ζιντζίβερ|g5=n|ζιτζίβερ|g6=n|ζιτζίβερι|g7=n|ζιτζίβερις|g8=f}}
* {{desctree|bor=1|la|zingiberi}}
* {{desc|bor=1|tmr|זַנְגְּבִילָא|tr=zingivila}}
** {{desc|bor=1|he|גִּנְבָּר|tr=ginbār}}

===References===
{{reflist}}

===Further reading===
* {{R:grc:LSJ}}
* {{R:grc:Bailly}}
```


## [2026-09-06T16:20:51.086Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg256.png"
}
```


### [2026-09-06T16:20:51.454Z] TOOL RESULT

```

```


## [2026-09-06T16:20:51.451Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:21:04.048Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 256 -l 256 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg256_hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg256_hi.png'); print(im.size)\n# crop persian box region: from 200dpi coords x 960-1190, y 285-390 -> scale 3\nim.crop((2850,830,3600,1180)).save('crop_p3.png')\nim.crop((2700,3020,3600,3200)).save('crop_cheek.png')\n\""
}
```


### [2026-09-06T16:21:08.128Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-06T16:21:10.459Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_p3.png"
}
```


### [2026-09-06T16:21:10.475Z] TOOL RESULT

```

```


## [2026-09-06T16:21:14.752Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_cheek.png"
}
```


### [2026-09-06T16:21:14.764Z] TOOL RESULT

```

```


## [2026-09-06T16:21:17.744Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg256_hi.png')\nim.crop((2950,3320,3950,3500)).save('crop_cheek2.png')\n\""
}
```


### [2026-09-06T16:21:19.874Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:21:22.847Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_cheek2.png"
}
```


### [2026-09-06T16:21:22.860Z] TOOL RESULT

```

```


## [2026-09-06T16:21:33.414Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT karat/qirat ===\"; grep -n -i \"qirat\\|qīrāṭ\\|karat\\b\\|Karat\" LKT.txt | head -10\necho \"=== LKT ingwer/zanjabil ===\"; grep -n -i \"ingwer\\|zangabil\\|zindschabil\\|singabera\" LKT.txt | head -10"
}
```


### [2026-09-06T16:21:33.494Z] TOOL RESULT

```
=== LKT karat/qirat ===
2551:'KameP  [eigentlich  'Schnelligkeit  ha- bend'], hieraus  wahrscheinlich  pers. kärwän  oder  käricän  'Kamelzug,  Reise- gesellschaft', in  alle  europäischen  Spra- chen übergegangen:  rum.  caravanä, chervanä,  it.  caravana,  carovana,  pg. sp.  caravana,  frz.  caravane;  engl,  cctra- van,  ndl.  karavaan;  dtsch.  Karawane, schwed.  fcßj'afrtn;  vxxss.  karawan,  bulg. kerwan,  serb.  karawan,  öech.  karavana, poln.  karaivana.  Mit  pers.  säräi  'Palast' [Horn  NpEt  S.  161,  Nr.  727]  ergibt  sich die  Bezeichnung  für  die  Herbergen  der Karawanen :  känvänsäräl.  Hieraus  rum. cherväsärie  'Lagerhaus,  Stapelplatz',  it. caravanserraglio,  frz.  caravanserail,  pg. caraicansarä ;  dtsch.  A'^rrtwanserai;  russ. karatvanseraj  [vgl.  Karl  Müller,  Die Karawanserai  im  Vorderen  Orient.  Ber- hn  1920].  [Klutre  227/228.  FR.  MÜL- LER in  WZKM  V,  354.
2570:1085.  Pers.  käränfll: 'Gewürznelke'  [wohl  aus  dem  Sskr.], hieraus  mit  volksetymologischer  Um- bildung gr.  KapuöqpuXXov,  aber  mgr. KapoüjaqpouX,  Kapou|U(pi\;  hieraus  it. garofano,  siz.  galofaru  'Nelke',  frz. giroße  'Nelke',  giroflSe  'Levkoje',  prov. kat.  sp.  girofle,  pg.  girofre  'Nelke',  rum. garoufä,  carofil,  garofil;  aus  dem  Frz. wurde  engl,  gilliflower  [mit  Anlehnung an  flotver  'Blume',  ja  sogar  weiter  noch JuUflower  mit  Verkennung  und  ganz falscher  Deutung  des  ersten  Bestand- teiles] 'Nelke'.  Dtsch.  in  der  Aachener Mundart  Groffelsnagel  'Gewürznelke' [wie  ja  die  Nelke  wie  die  Gewürznelke ihren  Namen  'Nägel'  wegen  ihrer  Ge- stalt erhalten  haben,  z.  B.  engl,  clove, it.  chiovo  di  garofano,  frz.  clou  de  girofle, poln.  gwozdzik  von  gwozdz  'Nagel',  ndl. nagelbloem  und  kruidnagel  und  'Ge- tvilrznägelcheri'  im  Deutschen].  Bulg. kalamfir,  karamfil,  serb.  karatnfil.
2571:1086.  Ar.  karaTTän: 'Rotfüßiges  Rebhuhn';  hieraus  mit  ar. Art.  sp.  alcaravan  [Dicc  Gast  III  b], pg.  alcaraväo  [Constancio  Dicc  45  b] 'Rohrdommel,  Botaurus  stellaris  Steph.' [DE  85].
2775:'Für  Gold  und  Diamanten  gebrauchtes Gewicht'  [aus  gr.  Kepdxiov,  dieses  nach der  Form  der  Früchte  des  Johannisbrot- baumes, Ceratonia  siliqua,  eigentlich 'Hörnchen',  benannt];  hieraus  sp.  qui- late,  pg.  quirate,  quilate;  mlat.  (bei  den Alchemisten)  carrätus,  it.  carato,  frz. carat,  rum.  carat;  dtsch.  Karat,  engl. carat;  russ.  karat.  —  [Eine  andere  Ab- leitung, die  zwar  der  ursprünglichen Schreibung  Garat  besser  gerecht  wird, aber  dennoch  mit  Rücksicht  auf  die anderen  europäischen  Formen  abgelehnt werden  muß,  gibt  aus  dem  Jüd.-Dtsch. Ave-L  IV,  302.]  [DE  327.  Eguilaz  474. Devic  DEt  85.    ML  6906.    Kluge  227.
5789:1068 A'ar«i*('  1004 Karaffe  689 Karakal  1081 ifa>-rt<  1182 Karawane  1075 Karatvanserai  1075 Karbatsche  1279
=== LKT ingwer/zanjabil ===
1926:'Eine  dem  Ingwer  verwandte  Pflanze, Galanga'  aus  Indien  und  China,  die  im MA  im  Orient  und  Okzident  als  Arznei- kraut benutzt  wurde;  hieraus  mgr.  yc- XcIyt«,  mlat.  galanga,  it.  galanga,  afrz. galange,  garingal,  frz.  le  galanga,  sp. pg.  galanga;  mengl.  galingale,  galger ['lebhaft  sein'],  engl,  galingale,  dtsch. Galgant{'w\xvzQ\);  russ.  bulg.  kalgan,  serb. galgan,  cech.  galgän,  poln.  galgan, 'galgant.  [Nach  Hirth  ChinFW  201/203 ist  ar.  halangän  auf  chin.  ko-Uung- kiung,  d.  h.  milder  Ingwer  von  Kao- tschau-fu,  einem  Regierungsbezirke,  aus dem  die  Galgantwurzel  besonders  be- zogen wird,  zurückzuführen.  In  der  Tat wird  der  Galgant  von  IBN  HURDADBA um  875  als  chinesisches  Erzeugnis  er- wähnt; er  muß  vor  dem  12.  Jahrhundert durch  Vermittlung  der  Araber  bis  nach
3058:1314.  Mal.  lempüjaiig: 'Zingiber  cassumunar'  [Pijn  210a;  viel- leicht aus  lampü  'übermäßig'  mit  Hin- weis auf  die  Stärke  des  Gewürzes]; hieraus  frz.  lampoujane  'Art  Ingwer'. [Devic  DEt  150.
4360:'Ingwer,  Zingiber  olficinarum  Roscoe' [eigentlich  'horiiarlig' ;  so  sind  die  Wur- zeln des  braunen  oder  gemeinen  Ing- wers tatsächlich  beschaffen];  mit  Schwin- den des  vokalischen  r  wurde  ar.  zen- §ehll,  tk.  zingifre  sowie  gr.  Zi-fYißepn;, lat.  zingiber  und  hieraus:  iL  zenzovcro, zenzero,  gengioi-o,  aprov.  gingebre,  frz. gingembre,  kat.  gingebre,  sp.  gengibre, agengibre,  pg.  gengibre,  gengivre,  rum. ghimber,  zingifil,  zinzifil ;  ndl.  gemher, engl,  ginger,  dtsch.  Ingtver  [mit  Abwurf des  Anlautes  wie  bei  den  folgenden Formen];  russ.  imbir,  inbir,  klruss.  im- bir,  poln.  imbier,  jembier,  cech.  zätcor, serb.  dzendzefil,  dumbir  [über  ung. gyönibir'].  [Dozy  Oost  40/41.  Kluge 215/216.    Bern  SlEtWb  259.
4589:Ebenso  hind.  tasar  'Schiffchen  des  We- bers' ;  hieraus  engl,  tussah,  tusseh,  dtsch. Tussaseide,  eine  Art  geringwertiger  Seide, die  von  verschiedenen  Seidenraupen, z.  B  Antheraea  paphia,  hergestellt  wird. [Hobson-Jobson  945/946.
4846:N.  pr.,  Gebirge  in  der  chin.  Provinz Fukien,  auf  dessen  Abhängen  lange  Zeit der  beste  Tee  gezogen  wurde.  Die  lokale Aussprache  des  ersten  Bestandteiles  [der zweite  heißt  'Gebirge',  vgl.  Tien-shaii 'Himmelsgebirge']  ist  bohi  und  ging  so ins  engl,  bohea  in  der  Bedeutung  'Tee' über,  z.  B.  Pope,  Rape  of  tbe  lock, Canto  IV,  156;  heute  ist  engl,  bohea eine  geringwertige  Sorte  schwarzen  Tees.
4942:!^215.  Ar.  /idwär: 'Zitwerwurzel  (ingwerartiges  Gewürz)' [aus  pers.  zädtvät'] ;  hieraus  sp.  cedoaria, pg.  zeduaria,  it.  zettovario,  frz.  zedoaire, nilat.  zeduarium;  russ.  cytwar,  klruss. eetwar,  cytwar,  poln.  cytwar,  bulg.  c«Y- ^^;ar;  dtscii.  Zitwer,  engl,  zedoary.
5782:Imam  905 iM«^/cÄ  909 JweZ/^o  909 Ingwer  1930 Intarsia  1706 Islam  915 /so^  566
```


## [2026-09-06T16:21:34.702Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ginger/carat ===\"; grep -n \"^ginger\\|^carat\\|^carob\\|^rhinoceros\" SKT.txt | head -10\necho \"=== HJB ginger ===\"; grep -n -i \"GINGER\" HJB.txt | head -6"
}
```


### [2026-09-06T16:21:34.766Z] TOOL RESULT

```
=== SKT ginger/carat ===
7729:gingerly,  with  soft  steps.  (Scand.) iPropcTly  with  toUcring  or  slovr  steps.— [Swed.  diaL  ging^>>,  guf'g'ih  to  go  gently, totter  ;  frequent  form  from  Icel.  ganga,  to E^  4r  I(  appears  to  have  been  c^dly  con* 'ftucd  wiihgiugtrl
=== HJB ginger ===
143:The  words  with  which  we  have  to  do,  taking  the  most  extensive  view  of the  field,  are  in  fact  organic  remains  deposited  under  the  various  currents of  external  influence  that  have  washed  the  shores  of  India  during  twenty centuries  and  more.  Rejecting  that  derivation  of  elephant*  which  would connect  it  with  the  Ophir  trade  of  Solomon,  we  find  no  existing  Western term  traceable  to  that  episode  of  communication  ;  but  the  Greek  and  Roman commerce  of  the  later  centuries  has  left  its  fossils  on  both  sides,  testifying to  the  intercourse  that  once  subsisted.  Agallochum,  carba^us,  camphor, sandal,  musk,  nard,  pepper  (Wire/w,  from  Skt.  pippali,  *long  pepper'),  ginger (^tyyi^pis,  see  under  Ginger),  lac,  costus,  opal,  malabathrum  or  folium  indicum, beryl,  sugar  {adjcxap,  from  Skt.  sarkara,  Prak.  saJdcara),  rice  (Upvia,  but  see  s.v.), were  products  or  names,  introduced  from  India  to  the  Greek  and  Roman world,  to  which  may  be  added  a  few  terms  of  a  different  character,  such  as Bpax/taret,  ^apfidyes  {sramanas,  or  Buddhist  ascetics),  ^;Xa  ffayaXLpa  koI  <r<urafi[va (logs  of  teak  and  shisham),  the  ffdyycLpa  (rafts)  of  the  Periplus  (see  Jangar in  Gloss.)  ;  whilst  dindra,  dramma,  perhaps  kastira  (*  tin,'  Kaafflrepos),  kasturl (*musk,'  Koardpiov,  properly  a  different,  though  analogous  animal  product), and  a  very  few  more,  have  remained  in  Indian  literature  as  testimony  to  the same  intercourse.t
1540:1768-71.— "When  men  it  (the  mango)  Is made  into  attiar:  for  this  the  kernel  is taken  out,  and  the  space  filled  in  with ginger,  pimento,  and  other  spicy  ingredi- ents, after  which  it  is  pickled  in  vinegar." -^Stavorvnus,  i.  287.
2181:1548.— "In  the  Renda  do  Bad,  or  Betel duties  at  Ooa  are  included  Betel,  arsaua* jacks,  green  ginger,  oranges,  lemons,  fiffs, coir,  mangos,  citrons." — Botelho,  Tombo,  48. The  Port,  also  formed  a  word  ariqueira  for the  tree  bearing  the  nuts.
2493:1506. — '*  In  Cananor  el  suo  Re  si  b  sentil,  e qui  nasce  sz.  (%.«.  zenseri  or  *  ginger ') ;  ma  li ez.  pochi  e  non  cusi  boni  oome  quelli  de Colcut)  e  suo  peso  si  chiama  baar,  ohe  sono K.  (Cantari)  4  da  lisbona."— /2e^a2um«  dt Leonardo  Ca'  Jicuser,  26.
3703:BLAGK  PABTBIDGE,  s.  The popular  Indian  name  of  the  common francolin  of  S.E.  Europe  and  Western Asia  {Francolinus  vulgaris^  Stephens), notable  for  its  harsh  quasi-articulate call,  interpreted  in  various  parts  of  the world  into  very  different  syllables. The  rhythm  of  the  call  is  fairly  re- presented by  two  of  the  imitations which  come  nearest  one  another,  viz. that  given  by  Sultan  Baber  (Persian^  : ^Shlr  daram,  skahrak^  (Tve  got  milk and  sugar '  I)  and  (Hind.)  one  given  by Jerdon  ;  *  Lahsan  piydz  adrak '  (*  Garlic, onion,  and  ginger  !)  A  more  pious  one is :  Khudd  teri  kudrat,  '  Qoa  is  thy strength  ! '  Another  mentioned  by Capt.  Baldwin  is  very  like  the  truth  : *  Be  quick,  pay  your  aebts  ! '  But  per- haps the  Greek  interpretation  recoraed by  Athenaeus  (ix.  39)  is  best  of  all : rpls  ToTs  KOKOJ^pyois  xaxd  *  Three-fold  ills to  the  ill-doers  !  *  see  Marco  Poloy  Bk.  i. ch.  xviii.  and  note  1 ;  [Burton,  Jr. NighUy  iii.  234,  iv.  17].
4101:1554.~(At  Goa).  "And  the  excise  from grarden  stuff  under  which  are  comprised these  things,  vis. :  Radishes,  beetroot,  gar- lick,  onions  green  and  dry,  ^en  tamarinds, lettooes,  eonbaUngvaSf  ginger,  oranges, dill,  coriander,  mint,  cabbage,  sutea mangoes,  brinjelas,^  lemons,  gourds,  cit- rons, cucumbers,  which  articles  none  may sell  in  retail  except  the  Bendeiro  of  this excise,  or  some  one  who  has  got  permission from  him.  .  .  ."—S.  Botelho,  Tombo,  49.
```


## [2026-09-06T16:21:46.925Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4355,4362p' LKT.txt; echo \"=== 1182 hdr ===\"; sed -n '2770,2778p' LKT.txt"
}
```


### [2026-09-06T16:21:46.998Z] TOOL RESULT

```
[Sskr.  srgäla.
XIV,  240/249;  mit  lautgeschichtlichen und  kulturhistorischen  Gründen  zurück- gewiesen von  Joseph  Schmidt,  A  persza saman  etymonja  in  Nyelvtudomänyi Közlemenyek  XLLV,  470/474.
1929.  Sskr.  srgäla:
T.anis  aureus,  Schakal',  ebenso  pers. säyäl,  tk.  sakal,  cakal;  hieraus  rum. ceacal,  it.  sciacallo,  afrz.  jachal,  frz. chacal;  engl,  jackal,  ndl.  jakhals [mit  volkselyinologischer  Umgestaltung], dtsch.  Schakal;  russ.  sakal,  cakal,  bulg. serb.  sakal,  cech.  sakal,  poln.  szakal 'Goldvvolt'.
1930.  Sskr.  sriig-avera;
'Ingwer,  Zingiber  olficinarum  Roscoe' [eigentlich  'horiiarlig' ;  so  sind  die  Wur- zeln des  braunen  oder  gemeinen  Ing- wers tatsächlich  beschaffen];  mit  Schwin- den des  vokalischen  r  wurde  ar.  zen- §ehll,  tk.  zingifre  sowie  gr.  Zi-fYißepn;, lat.  zingiber  und  hieraus:  iL  zenzovcro, zenzero,  gengioi-o,  aprov.  gingebre,  frz. gingembre,  kat.  gingebre,  sp.  gengibre, agengibre,  pg.  gengibre,  gengivre,  rum. ghimber,  zingifil,  zinzifil ;  ndl.  gemher, engl,  ginger,  dtsch.  Ingtver  [mit  Abwurf des  Anlautes  wie  bei  den  folgenden Formen];  russ.  imbir,  inbir,  klruss.  im- bir,  poln.  imbier,  jembier,  cech.  zätcor, serb.  dzendzefil,  dumbir  [über  ung. gyönibir'].  [Dozy  Oost  40/41.  Kluge 215/216.    Bern  SlEtWb  259.
1931.  Tk.  Staiubul:
N.  pr.,  Name  der  europäischen  Haupt- stadt der  Türkei,  auch  Istambul  [aus gr.  eiq  xäv  -nöXiv];  hieraus  serb.  stambol, russ.  stambulka ,  dtsch.  Stutnbulina 'schwarzer  tk.  Gehrock'.  [Gorjajew  342. Mikl  SlEtWb  320  a.
=== 1182 hdr ===
1180.  Tk.  kir:
'Schmutz',  dazu  Adj.  kirli  'schmutzig' [vom  Stamme  kir  'schmieren,  Farbe, Schmutz'  Vämbery  TktEtWb  S.  89, Nr.  92];  hieraus  bulg.  kir  'Sehmutz  am Körper',  kirliiv  'schmutzig',  russ.  kir 'mit  Naphtha  getränkte  Erde'.  [Bern SlEtWb  505.
1181.  Ar.  kirä':
'Miete,  Mietpreis'  [Vb.  karä  'mieten,  ver- mieten'] ;  hieraus  mit  ar.  Art.  und  Imäla [ä  >  e]  sp.  alquile,  alquiler,  pg.  alquile, alquiler  'Miete',  Vb.  sp.  pg.  alqutlar 'vermieten'  [pg.  nur  bei  Tieren  gesagt, sonst  alugar  <^  lat.  adlocare];  über  tk. kira  wurde  rum.  chiriä  'Miete',  chirigiü 'Fuhrmann',  bulg.  kirija  'Fuhrlohn, Fracht,  Miete',  kiradzija  'Fuhrmann, Mieter',  serb.  kirija  'Miete,  Fracht', kiridzija  'Fuhrmann'.  —  [ML  4692  sp. alqueire  gehört  nicht  hierher,  s.  hier Nr.  1174a.]  [DE  186.  Eguilaz  250. Bern  SlEtWb  505.
1182.  Ar.  kirät:
'Für  Gold  und  Diamanten  gebrauchtes Gewicht'  [aus  gr.  Kepdxiov,  dieses  nach der  Form  der  Früchte  des  Johannisbrot- baumes, Ceratonia  siliqua,  eigentlich 'Hörnchen',  benannt];  hieraus  sp.  qui- late,  pg.  quirate,  quilate;  mlat.  (bei  den Alchemisten)  carrätus,  it.  carato,  frz. carat,  rum.  carat;  dtsch.  Karat,  engl. carat;  russ.  karat.  —  [Eine  andere  Ab- leitung, die  zwar  der  ursprünglichen Schreibung  Garat  besser  gerecht  wird, aber  dennoch  mit  Rücksicht  auf  die anderen  europäischen  Formen  abgelehnt werden  muß,  gibt  aus  dem  Jüd.-Dtsch. Ave-L  IV,  302.]  [DE  327.  Eguilaz  474. Devic  DEt  85.    ML  6906.    Kluge  227.
1183.  Tk.  kireg:
'Kalk'  [Kelekian  Kämüs  1066] ;  hieraus bulg.  kirec,  serb.  krec  'dass.'.
1184.  Pers.  kirpic:
```


## [2026-09-06T16:21:48.214Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"GINGER\\b\" HJB.txt | head; echo \"=== HJB srngavera ===\"; grep -n -i \"sringavera\\|srmgavera\\|singabera\\|zingiber\" HJB.txt | head"
}
```


### [2026-09-06T16:21:48.277Z] TOOL RESULT

```
10130:GINGER.
10132:GINGER,
20759:[1598. — ".6inger  by  the  Arabians,  Persians and  Turkes  is  ciUled  GengibU  (see  GINGER), in  Gusurate,  Decan,  and  Bengala,  when  it  is fresh  and  green  Adrac,  and  when  dried snkte."— Ltn«-A<rf«n,  Hak.  Soc.  ii.  79.]
=== HJB srngavera ===
10142:^  aXNGEB,  s.  The  root  of  Zingiber ofjicinaUy  Roxb.  We  cet  this  word from  the  Arabic  zdnjafn^  Sp.  agengibre ((U-zdnjabU\  Port,  gingibrty  Latin teingiheTy  Ital.  zenz/ero^  gengiovOy  and many  other  old  forms.
23372:c.  A.D.  540.— "Zador(t.«.  ««rfoana<),galan- gae,  ligustici,  seselis,  cardamomi,  piperis longi,  piperis  albi,  cinnamomi,  zingiberis, seminis  Smymii,  caryophylli,^  phylli,  sta- chyos,  myrobalanl,  phu,  costi,  soordii,  sil- phii  vel  laserpitii^  rhei  barbarici,  poeoniae ; alii  etiam  arbons  nucis  viscum  et  paliuri semen,  itemque  saxifragum  ac  oasiam  ad- dun  t  ;  ex  his  singulis  stateres  duos  oom- misceto.  ..."
```


## [2026-09-06T16:21:50.931Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10142,10165p' HJB.txt"
}
```


### [2026-09-06T16:21:50.980Z] TOOL RESULT

```
^  aXNGEB,  s.  The  root  of  Zingiber ofjicinaUy  Roxb.  We  cet  this  word from  the  Arabic  zdnjafn^  Sp.  agengibre ((U-zdnjabU\  Port,  gingibrty  Latin teingiheTy  Ital.  zenz/ero^  gengiovOy  and many  other  old  forms.
The  Skt.  name  is  sringaveroy  pro- fessedly connected  with  sringay  *a horn,'  from  the  antler-like  form  of  the root.  But  this  is  probably  an  intro- duced word  shaped  by  this  imaginary etymology.  Though  ginger  is  culti- vated all  over  India,  from  the  Hima^ laya  to  the  extreme  south,*  the  best  is grown  in  Malabar,  and  in  the  language
*  "Rheede  says:  *BtUin  in  sylvls  et  deserUs reperitur '  (Fort.  Mai.  xi.  10)t  But  I  am  not  aware or  any  botanist  having  found  it  wild.  I  suspect that  no  one  has  lookeafor  it"~>i!Mr  /.  D,  Hoour.
of  that  province  ^Mala^filam)  green ginger  is  called  incht  and  tnchi-ifery  from inaUy  *root.*  Inehi  was  probably  in an  earlier  form  of  the  language  titUhi or  chdfiehiy  as  we  find  it  in  Canarese still  9&tUiy  which  is  perhaps  the  true origin  of  the  H.  ionth  for  *dry  ginger,' [more  usually  connected  with  Skt- sunthdj  stmthy  '  to  dry  '1
It  woulcl  appear  tnat  the  Arabs^ misled  by  the  form  of  the  name, attributea  zanjabU  or  zinjabUy  or ginger,  to  the  coast  of  Zinj  or  Zanzi- bar ;  tor  it  would  seem  to  be  ginger which  some  Arabic  writers  speak  of as  *the  plant  of  Zinj.'  Thus  a  poet quoted  by  Kazwini  enumerates  among tne  products  of  India  the  Aair  al-Zdntj or  Arbor  ZingitanOj  along  with  shisham- wood,  pepper,  steel,  «c.  (see  Gilde- meideTy  218).  And  Abulfeda  says  also : **At  Melinda  is  found  the  plant  of Zinj "  (Geog.  by  Reinaud,  i.  267).  In Marino  Sanudo's  map  of  the  world also  (c.  1320)  we  find  a  rubric  connect- ing Zinziber  with  Zinj,  We  do  not inaeed  find  ginger  spoken  of  as  a  pro- duct of  eastern  continental  Africa, though  Barbosa  says  a  large  quantity was  produced  in  Madagascar,  and Varthema  says  the  like  of  the  Comoro Islands.
c.  A.D.  65.— "Ginger  {ZiyYificpis)  is  a special  kind  of  plant  produced  for  the  most part  in  Troglodytic  Arabia,  where  they  use the  green  plant  in  many  ways,  as  we  do  rue Miyayov),  boiling  it  and  mixing  it  with arinks  and  stews.  The  roots  are  small,  like those  of  ofpemSf  whitish,  and  peppery  to the  taste  and  smell.  .  .  ." — DioscortdeSy  ii. cap.  189.
c.  A.D.  70.— "This  pepper  of  all  kinds  is most  bitinff  and  sharpe.  .  .  .  The  blaoke  is more  kindly  and  pleasant.  .  .  .  Many  have taken  Ginger  (which  some  call  Zimbiperi and  others  Zlnigiberi)  for  the  root  of  that tree ;  but  it  is  not  so,  although  in  tast  it somewhat  resembleth  pepper.  ...  A  pound of  Ginger  is  commonly  sold  at  Rome  for  6 deniers.  .  .  ." — Pliny ,  by  Ph,  Hollandy xii.  7.
c.  620-30.- "And  therein  shall  they  be given  to  drink  a  cup  of  wine,  mixed  with the  water  of  Zeojebil.  .  .  ."^Tke  Koran y ch.  Ixxvi.  (by  &i/e).
c.  940. — "Andalusia  possesses  considerable silver  and  quicksilver  mines.  .  .  .  'niey  ex- port from  it  also  saffron,  and  roots  of  ginger (?  *aruk  a/-iai|jaha)."— JTo^'Ait,  i.  867.
1298.— < '  Good  ginger  (gmgibra)  also  grows here  (at  Goilum— see  Qtn]j01l)i  a-nd  it  is known  by  the  same  name  of  Coilwrniny  after> the  country.  "<^ifam>  Poloy  Bk.  III.  ch.  22«
GINGERLY.
375
GINGHAM,
e.  1848.— "Qiengioiro  ri  h  di  pin  msniere, cioe  belledi  (aee  001JHTBT),  e  eolombmo.  e I'ocfctwo,  e  detti  nomi  portano  ner  le  oontnde. onde  aono  nati  ispeaalmento  u  eoUmbino  e  il tMcAiwo,  che  pnmieramento  il  belledi  nasoe in  molte  oontrade  deU'  India»  e  il  oolombiiio DMoe  nel  Isola  del  Colombo  d'  India,  ed ha  la  soona  sua  piaoa^  e  delicata,  e  oenerog- nola ;  e  il  miochino  viene  dalle  oontrade  del Mecca  .  .  .  e  ragiona  che  il  buono  ^ensioYo dura  buoDO  IOanni,"&o. — PegoloUt,  inVella Decmut,  iii.  881.
o.  1420. — "His  in  reffionibus  (Malabar)  gin- IPOmt  oritur,  quod  baUdi  (see  COUinSY), ffebdi  et  neli*  vulgo  appellatur.  Radices sunt  arbonun  dnorum  cubitomm  altitudine, faUis  mi^^nis  instar  enulae  (elecampane), duTO  oortice,  veluti  arondinum  radices,  quae fmctom  teipnt ;  ex  eis  extrahitur  gingioer, quod  immistum  dneri,  ad  solemque  ex- poaitam,  triduo  exsiccator."— iVi^   Conii,  in
JPOffffio.
1580. — In  a  list  of  draffs  sold  at  Ormuz WB  find  ZeniQsl  da  bull  (presumably  from
„        mordaci „        Meccbini „        beledi Zeniero  oondito  in  giaga  (preserved in  Jaggery  fy--6'(uparo
m  Jaggery  T BaOri,  f.  54.
GINGERLY,  s.  A  coin  mentioned u  passing  in  Arabian  ports  by  MiUmm (L  87,  91).  Its  country  and  propr name  are  doubtful.  [The  following ouotations  show  that  Gingerlee  or morgelin  was  a  name  for  part  of  the E.  coast  of  India,  and  Mr.  Whiteway (see  OnVGELI)  conjectures  that  it  was so  called  because  the  oil  was  produced there.]  But  this  throws  no  light  on the  gold  coin  of  Milbum.
W8(V81.~"  The  form  of  the  pass  given  to ships  and  vessels,  and  Register  of  Passes giTwi  (18  in  all),  bound  to  Jafnapatam, Manilla,  Mocha,  Gfaigsrlee,  Tenasserim, &C."— ^orf  St,  Geo.  Cons,  Notes  and  ExU., App.  Na  ill.  p.  47.
1701.— The  Carte  Mariiu  depuit  SuraUe JKtqu'au  Detroit  de  Malaca^  par  le  R.  P^re P.  r.  Tachard,  shows  the  coast  tract  between Ve$egaipaiam  and  lagrenaU  as  €toigttli]L
1758.  —  "  Some  authors  give  the  Coast between  the  points  of  Devi  and  Ghtudewari, the  name  of  the  Coast  of  QeiveUn.  The Portagaese  ffive  the  name  of  Oenelim  to the  plant  which  the  Indians  call  EUu,  from vMch  they  extract  a  kind  of  dl,**^D'Anville. 134.
[Mr.  Pringle  {Diary  Fort  St,  Geo,  1st  ser. m.  170)  identifies  the  Gingerly  Factory  with Vingapatam.    See  also  i.  109 ;  ii.  99.]
```


## [2026-09-06T16:22:01.095Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n \"^sar \\|^sar,\\|srūw\\|sruw\\|singaber\\|sangwir\\|^sar$\" PHD_mackenzie.txt PHD.txt 2>/dev/null | head -20\necho \"=== NYB sar ===\"; grep -n \"srūv\\|srūw\\|sar- 'head\\|sar 'head\" NYB_vol2_glossary.txt | head -10"
}
```


## [2026-09-06T16:22:01.702Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sarah-\" BRT.txt | head -5"
}
```


### [2026-09-06T16:22:02.788Z] TOOL RESULT

```
=== PHD ===
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:2313:horned srūwar.
PHD.txt:2314:horny srūwēn.
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD_mackenzie.txt:4493:sar [LOY8E < A T'lh; sll M ST, N -] head; top, summit; end, begin-
PHD_mackenzie.txt:6784:hence parron.                                  horny sruwen.
=== NYB sar ===
4291:Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
```


### [2026-09-06T16:22:02.833Z] TOOL RESULT

```
25757:•  j.  urvi-sarah-  Adj.  'mit  spitz  zulaufen- dem Kopf,  mit  spitzer  Schnauze',  vom Igel:  spätam  sTzdnm  'sanm'^ yim  vanha- parsm  (sd.)  V.  13.  2.
```


## [2026-09-06T16:22:09.440Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sarah-  n\\|sarah- n\\|•  j.  sarah\\|g.  sarah\" BRT.txt | head -5; echo ===; grep -n \"sarah\" BRT.txt | head -12"
}
```


### [2026-09-06T16:22:09.545Z] TOOL RESULT

```
Exit code 1
(eval):2: == not found
```


## [2026-09-06T16:22:11.722Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sarah\" BRT.txt | head -12"
}
```


### [2026-09-06T16:22:11.771Z] TOOL RESULT

```
2463:paiti  vä  xsa/ne  . .  nöit  . .  aiähe  ayqn  nöit aiiihä  xiapö  .  .  Yti.iS;  —  asankatca iöi'irSatca  ..  kaoa  nö  ahmäii*  asarahaica läiiraiüi  ..V.ff.Sif.;  55'\  56i\Y.^S.2; — sraoi»m  .  .  yö  dalnöJiisö  *da?nayä  . .  aya dalnaya  . .  Y,  57. 24;  —  , .  parö  jbi^anbyö .  .  alsqm  tbifyaniqm  Yt-  io.T%i.;  —  yaoz- däiqm  saeirqm  . .  änhqm  zaoiranqm  Yt. io. lai f.;  Y.2(j. 2;  —  vä^^m  srJr^m  .. ahmya  väse  Yt/o.  12411;  5.11;  —  äp)m andvim  . .  *atihasca  mi  *aSva^hä  apö ¥.(75.1—5;  5,  V.ö,32  (aitiha);  —  nmS- mm  .  ,  äat  ahe  nmänahe  V.^.3;  14,  40; —  narö  . .  äat  aisam  naram  aivS  iri^yai (vat  antarp  *n3rius  .  .  V.j.z?;  5.43,  44, A.4.6,  Yt.iO,i37;  —  ygi  nmüni  hqm. barämahi  . .  äat  pascaeta  ahe  nmänahe , .
6268:'laona^a  (statt  Gen.)  sarahustrahe  Y.  Ä I ;  —  'säum  (VS.)  zara%ustra  V.  2, 2,  4. 2,
9772:•  j.  gaeiSya-,  gae*ya-'>  Adj.  (fem.  ya-)  sehen  Baums*>:  ma  attmyöahurs  masäa 'stofflich  lebendig,  materiell'«:  vlspqm  ^urvarA  baSsasyä  uz^artm  paoirls  . .  dyum asaom  stm  ..  mainynnmca  '>yamc<i  Y.  '■„im  pairiyi.20.i,;  —  'mm  sünm  mazda- J5.1;  —  asmawm  ..  '■'ihm  ''i^yayn  r^jfy^  Yt.j.30,  S.a.  7;  —  'noAe  sarahe si5is'  Vr.  7.  4;    —    zaraiuitnm  .  .  -är«  I  mazdmätahe  Yt.  i.  30,  S.  /.  7.
10894:digslen  ist  zufrieden  gestellt  zu  werden': sarahusirym  ..  hätqm  '»mm  Yty.  152.
12404:—  aii'afitS  ahi  abatthö  tarn  yö  aAurS mazda  "V.  ig,  2q;  —  cisca  tarn  caraitis ahi  yqm..iäraitinqm..sraistqm  dädansa Vyt.57(?)*>;  — s.  noch  V.  2. 43  bei  i  und "  Bh.  4. 6,  15  bei  3.  3)  1  im  Ap.  voi dem  veraJlgemeineraden  kä  (Sp.  42a); tuvam  k3  Ayc^  aparam ..patiparsäAy'Bh. ^.6J>;  15^;  —  tuvam  kä  xsäya^iyt^  hy(^ aparam  *ahy  Bh.4, 19,  5,  14.  \  4)  sonst beliebig;  a)  an  der  Spitze  des  Satz(teil)es; o)  unmittelbar  vor  Vok.:  tvim  mazäa ahura  frs  mü  sXsä  ..Y.zS.w.  ß)  sonst: tarn  mafhanahe  pSta  nipäta  ahi  adrmqm Yt:  io.  80;  80,  29*,  V.  ig.  6,  VyL  22,  2^, —  iäm  aisqm  tbi^yatam  tum  aliqm tbalsaauhatqm  fialsä  sSndayeAiYtlo.'j6;\ 23'.  »9tJ,  78',  5-  87.  IS-  55-  b)  in andrer  Stellung;  a)  unmittelbar  vor  Vok.: aoa  nS  tarn  mi^ra  .  .  dayU  Yt.  10.  94;  Y. 37.36;  —  äatmltüm  aridvl  sUre  anakite .  .  piium  ralcaya  Yt5. 77;  —  aai  tarn sarahuitra  .  .  V.g.  12,  10.  18;  — -  3af ya/  /am  tara%uftra  .  .  V.  //.  4;  Vyt. 4-3-  ß)  sonst:  *pouru.narim  tarn  kin- näH  ..  Y.  io,  13;  —  i^a  ml  tsm  kam.- caranuha  .  .  Yt //,  60;  —  Aanalsa'  ta tarn  tat  mlzd^m  yal  ..  Y.  5p.  30;  — äa^  mqm  tQm  fiaonayeke  '^.ii.i;  V.  22. I.  9t  Vyt  13  rSt;  — •  aal  tarn  pascatta  .. V.  i".  4;  Vyt^/;  —  yat  tum  ainim  avaS- fiäiS  .  ,  H.a.  13;  — •  yaha  tarn  trftvd (sd.)  vaia/ghe  V,5. 17,  ai;  Vyt i2.
12762:sarahuäröY.g.i;  'Vt.S.$j,  lO.  ixi,  I2.i,
16322:•  j.  pouru.x''ar9nah-  Adj.  'der  viel  Herr- lichkeit, Glanz  besitzt,  hoheitsvoll';  °nat»Ad (NS.)''  asava  sarahusIrSY .ig.y, — 'nanha (VS.)"'  ahura  mazda  Vyt.  2.^'*;  —  yasata 'naiaha  (AP.)  yasata  pouru.bailaza  Ny.5. 6 ; —  yazata  'nanha  (VP.)  Ny.  J.  1 1 ;  — jc^arj»?  "««»^iffi  (ASm.  statt  n.)  Yt.iÄi.
20259:—  kar)taHt..yH  myrSire  sarahu  'kanqm Yt.  10. 40;  —  k»m  . .  'ka  (IS.?)  dagbs  aoüf (sd.)  yasaiU  V.  ly.  i.
22154:nehmen':  vJsmU  aval  vlssnta^a  *mazyasat . .  fravaiayS  "sie  stellen  sich  dazu,  sie stellen  sich  auch  zu  noch  grösserem  be- reit . ."  YLiy.73;  —  at»m  aita  zaota  vUäi staotanqm  yesnyanam  frasraohnm^a . .  "ich will  es  als  Z.  übernehmen:  das  laute  Auf- sagen . ."  Vr._j.  7.  3)  '(herantreten  um zu  —  sva.)  sich  bereit  stellen,  dran,  drauf aus  gehen  (etwas)  zu  (tun),  es  übernehmen zu  — ,  bereit  sein  zu  — ',  mit  Inf.:  visaraha mi  .  .  mprvis  ifri/a(sd.)ca  dalnayili  V. 2. 3 ;  —  vlsaiti^''  dim  frayrSrayS  nStt frayräyräyätiisä.)  N.  ig;  —  visaiti^  ainyB "usyS  (sd.)  «JiV  ainyB  rviismnS  *llstrydte ava  *vlsaae*l  ^naihaxit  ästryeite  "der  eine zeigt  sich  bereit  zu  . .,  der  andere  nicht; der  sich  weigert,  versündigt  sich.  Sind beide  bereit,  so  geschieht  überhaupt  keine  ; Versündigung"  P.  57;  —  hyat  vUJntä  j (sPPrM.)  ängvant^m  avB  kyatcä  .  .  "weil ' sie  drauf  ausgehen,  dem  Z^ru^läubigen 'Propheten)  zu  helfen,  und  dass  (s.  3  a)  . ." Y.^2.  14;  —  nimahl  usSmahl  tumatihl vjsämaidi  V.  $8. 3.  a)  negirt  mit  Inf. a)  'sich  weigern  (etivas)  zu  (tun)':  yas^a  . . imq  vacS  nsit  *vfsaite''^  framrüile  i&A.)  Y. A4;  —  yS  hl  *ap)r3n3mnäi  (sd.)  nött vUäiti^  ''framrüiU  N.  /J;  —  vgl.  noch 3^Ts>mna-.  ß)  'es  nicht  fertig  bringen, nicht  vermögen  zu  (tun)':  t^it  vjsmte  asäni avasyäi  "nicht  vermögen  Steine  (ihn)  zu treffen"  Yt  /.  1 8  *'.  3  a)  'darauf  ausgehen dass  — '  {hya£):  hyat  vUSntä  dngvantjm "vff  (s.  3)  hyaliä  gäus  Jaidyäi  mraol  Y. ,?2.  14.  vliäi'>'>  FrD.  ö(?).  [vJs^rUi
25004:'huItraAe  .  ■  yim  istn  aniisa  sppnta  . .  ahüm  'huiirai  Vr.  12.  i;  —  Zw«  'tum  yatamaide 'tBmca  gai^anam  Yty.92;  91,  Vr.  2.  4, '_>-/«  sarahuHrstn  Y.  70. 1 ;  —  amtrptstö 16.  3;  —  ya%ä  aha  (Sp.  a8a  o.)  vairyö  '^wS  S.  /.  7  '"';  —  kaurvatats  "5aiff  S.  /. (näml. »araättÄrff)  ai-S  °(uP^  a/ätc'it  Äa^'a'6'°>; —  ä%rS  ahurahe  matdä  '%wS  b^rp- ..  dazdä{5Ü.)  Y.  27.  13;  —  yat  dim  (näml.  j  «n/J  yS  asahe  Y.  22.  4;  1.  17,  4.  2;  — tarahuttrfm)  aküm{Si^.  282  o^ca  Hümca  .'hwasca  bfrgzats"^  H.4S;  Vr.^.6;  — adadaj  Y.  iff.  12;  —  zara%ustrS  .  .  'iu/\  avi  iava  'tvS  (VS.)  bima"^ yasmm  g?r?Q- astvaihyB  gal%ayä  bansnul  bipaÜista-^maAi  \x.21.3;  —  kaya  °tavöt  nmänyS naya  Yt.  ig,  41;  —  s.  noch  Yt  8.  ^^' vTy^ö  santumS  dähyumö  tarähustrS  puxtiJ unter  7.  ß)    AHM.  tÜT    die   gtsammle   äfjAam  daÄyurtamyä  anyä  ra/sit..ühru.-
25757:•  j.  urvi-sarah-  Adj.  'mit  spitz  zulaufen- dem Kopf,  mit  spitzer  Schnauze',  vom Igel:  spätam  sTzdnm  'sanm'^ yim  vanha- parsm  (sd.)  V.  13.  2.
28619:—  jahikayai:  mJ  Al  (fem.)  avi  pahm ava.hilta  Yt.j7.57;  N.jo  (nSit  At);  — zaohrä  .  .  bansma  .  .  pasUm  .  .  ma  Al (Plur.)  mairyS  g»urvayöil  (Sp.  537  o,)  .  . yai  sl  mairys  gpurvayai  Yt.  A*.  s8ff.;  — ipa  . .  ava  Al  baraym  . .  djuru  upa  tarn manaoisnm  V.jj.30;  Ä.S',  9.40,  49; — yS imqm  zqm  aiwi.vfnsyöti  . .  upa  hl  (fem.) gasrwm  baraiti  V._y.3S;  YL/7,21,  V./5.43 (zu  a);  —  p)r?sat  sarahuilrs  .  .  paiti  it aoxta  ahurS  mazd'j  H. /.  iE;  J,  A.  4-6. P.  27,  FrW.  10. 40;  —  iiyri/  . .  lata  dim ahurS  mazdä  avan  . .  pairi  ll  .  .  mihrS
```


## [2026-09-06T16:22:27.967Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/carat\" \\\n \"https://www.etymonline.com/word/migraine\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱerh₂-\" \\\n \"https://en.wiktionary.org/wiki/ساربان\" \\\n \"https://en.wiktionary.org/wiki/افسر\" \\\n \"https://en.wiktionary.org/wiki/سرشار\" \\\n \"https://en.wiktionary.org/wiki/शृङ्गवेर\" \\\n \"https://en.wiktionary.org/wiki/زنجبيل\" \\\n \"https://en.wiktionary.org/wiki/شنگویر\" \\\n \"https://en.wiktionary.org/wiki/ζιγγίβερις\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 256, root Ker 1, verification of Nourai's derivations\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T16:22:34.567Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/55b165b34373067b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6eef3d1fa4dc91ac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/681863361c9aa760.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08a61888c451ebaa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e3285ee7c44fbf3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93e106c536308300.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/491c1d13f518086f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c3caa4ef09c36f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3eacded550b54360.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de93310015e0c85b.txt
```


## [2026-09-06T16:22:38.859Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://www.etymonline.com/word/ginger\" \\\n \"https://www.etymonline.com/word/rhinoceros\" \\\n \"https://www.etymonline.com/word/cheek\" \\\n \"https://www.etymonline.com/word/cheer\" \\\n \"https://en.wiktionary.org/wiki/سرو\" \\\n \"https://en.wiktionary.org/wiki/قیراط\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 256, root Ker 1\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T16:22:43.198Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5dbedf1571fdbf3e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f4b91dcfa77f94ff.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b203e60b46f0aab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fa64bc71436cd6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9cc10fa9768dcc42.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/afd2b19d5d085f82.txt
```


## [2026-09-06T16:22:46.106Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== cheek ===\"; head -40 2b203e60b46f0aab.txt | tr -s '\\n' ' ' | head -c 1500; echo; echo \"=== cheer ===\"; head -40 3fa64bc71436cd6f.txt | tr -s '\\n' ' ' | head -c 1200"
}
```


### [2026-09-06T16:22:46.163Z] TOOL RESULT

```
=== cheek ===
URL: https://www.etymonline.com/word/cheek FETCHED: 2026-09-06T16:22:41Z STATUS: 200 TITLE: Etymonline - Online Etymology Dictionary Etymonline - Online Etymology Dictionary Search Log in Columns Forum Apps Premium Log in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple. About Who Did This Sources Introduction Links Support Premium Patreon Donate with PayPal Merch Apps Get Chrome Extension Get iOS App Get Android App 
=== cheer ===
URL: https://www.etymonline.com/word/cheer FETCHED: 2026-09-06T16:22:42Z STATUS: 200 TITLE: Cheer - Etymology, Origin & Meaning Cheer - Etymology, Origin & Meaning Search Log in Columns Forum Apps Premium Log in Advertisement Remove Ads Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads. Origin and history of cheer cheer (n.) c. 1200, "the face, countenance," especially as expressing emotion, from Anglo-French chere "the face," Old French chiere "face, countenance, look, expression," from Late Latin cara "face" (source also of Spanish cara ), possibly from Greek kara "head" (from PIE root *ker- (1) "horn; head"). From mid-13c. as "frame of mind, state of feeling, spirit; mood, humor." By late 14c. the meaning had extended metaphorically to "state or temper of mind as indicated by expression." This could be in a good or bad sense ("The feend ... beguiled her with treacherye, and brought her into a dreerye cheere," "Merline," c. 1500), but a positive sense, "state of gladness or joy" (probably short for good cheer ), has predominated since c. 1400. The meaning "that which makes cheerful or promotes good spirits" is from late 14c. The meaning "s
```


## [2026-09-06T16:22:51.343Z] TOOL CALL #77: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=cheek&action=raw\" | sed -n '/^==English==/,/^===Pronunciation/p' | head -20"
}
```


### [2026-09-06T16:22:53.043Z] TOOL RESULT

```
==English==
{{wp}}

===Etymology===
From {{inh|en|enm|cheeke}}, {{m|enm|cheke}}, {{m|enm|cheoke}}, {{m|enm|choke}}, from {{inh|en|ang|ċēce}}, {{m|ang|ċēace}}, {{m|ang|ċēoce|t=cheek; jaw}}, from {{inh|en|gmw-pro|*kākā}}, {{m|gmw-pro|*keukā|t=jaw, cheek}}, from {{inh|en|gem-pro|*kēkǭ}}, {{m|gem-pro|*keukǭ|t=jaw; palate; pharynx}}, perhaps from {{der|en|ine-pro|*ǵyewh₁-|t=to chew}}.

Cognate with {{cog|stq|Sooke|t=cheek}}, {{cog|fy|tsjeak|t=jaw}}, {{cog|nl|kaak|t=jaw; cheek}}, {{cog|sv|käke|t=jaw; jowl}}, {{cog|no|kjake|t=jaw}}, {{cog|non|kók|t=mouth; gullet}}.

===Pronunciation===
```


## [2026-09-06T16:24:14.327Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['TAD'];print(d.get('page_offset'));print(d.get('lookup_hint'))\n\"\ncd data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',errors='replace').read()\nlines=t.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i==2330: print('leaf',leaf); break\n    leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-06T16:24:15.838Z] TOOL RESULT

```
86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
leaf 63
```


## [2026-09-06T16:24:21.746Z] TOOL CALL #79: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg256.png data/verification/sources/refs/ocr/BOOK/256.png && ls -la data/verification/sources/refs/ocr/BOOK/256.png"
}
```


### [2026-09-06T16:24:21.813Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 83469 Sep  6 12:24 data/verification/sources/refs/ocr/BOOK/256.png
```


## [2026-09-06T16:24:29.589Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/cheek\" --note \"pdf page 256, node 19, cheek is not from PIE ker- (head/horn)\" 2>&1 | tail -1"
}
```


### [2026-09-06T16:24:31.897Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ea38a8b0204bd049.txt
```


## [2026-09-06T16:33:45.763Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-256.json <<'JSONEOF'\n{\n  \"pdf_page\": 256,\n  \"book_page\": 226,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ker 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱerh₂- 'head, top; horn' (Pokorny: 'ḱer-, ḱerə- : ḱrā-, ḱerei-, ḱereu-', Meaning 'head; horn, cow', IEW 574-577)\",\n      \"note\": \"The root box is right in every particular: Pokorny's article on pp. 574-577 is headed 'Ḱer-, Ḱerə- : Ḱrā-, Ḱerei-, Ḱereu-' with the meaning 'head; horn, cow', and its material begins 'Old Indic śiras- n. \\\"head, cusp, peak\\\", Avestan sarah- n. \\\"head\\\" ... from the u-basis Avestan sru-, srva- \\\"horn; nail\\\", srvara \\\"horned\\\" (*sru + bhara-)'. Watkins/AHD spells the same root *ker-1 'horn, head' and gathers under it exactly Nourai's English harvest (HORN, CORNER, CARROT, CARAT, RHINOCEROS, MIGRAINE, CRANIUM, CEREBRUM) plus 'Persian sar, head: SIRDAR'. Modern reconstruction adds the laryngeal: *ḱerh₂-. Nourai's label 'Indo-European' and gloss 'head, horn' are correct; the only substantive problems on the page are (a) ساربان in the Persian box, which is not from sar 'head' but from Parthian/Sogdian sārt 'caravan', (b) the English word 'cheek' in node 19, a misprint for 'cheer', and (c) the ginger branch, where śṛṅgavera is now known to be a Dravidian loan reshaped by folk etymology and Arabic zanjabīl reached Arabic through Syriac from Middle Indic, not from Greek. NOTE: the printed page carries SEVEN Persian words in node 3 (سر ، افسر ، افسار ، ساربان ، سردار ، سالار ، سرشار); the extraction dropped افسار.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱerh₂- «سر، تارک؛ شاخ» است که پوکورنی آن را در فرهنگ خود (صص ۵۷۴–۵۷۷) با همین معنی «سر؛ شاخ، گاو» آورده و در همان‌جا اوستایی sarah- «سر» و srū-/srvā- «شاخ، ناخن» و srvara- «شاخ‌دار» را ذیل آن جای داده است. واتکینز نیز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage همین ریشه را *ker-1 «شاخ، سر» می‌نامد و واژه‌های horn، corner، carrot، carat، rhinoceros، migraine، cerebrum و «فارسی sar (سر)» را زیر آن گرد می‌آورد. پس ادعای نورایی در بارهٔ خودِ ریشه و برچسب زبانی و معنی آن درست است. اشکال‌های صفحه در گره‌هاست: «ساربان» از «سر» نیست بلکه وام‌واژه‌ای است از پارتی/سغدی sārt «کاروان»؛ واژهٔ انگلیسی cheek در کادر «Different Languages» خطای چاپی کتاب به جای cheer است؛ و شاخهٔ زنجبیل نیازمند تصحیح است، زیرا śṛṅgavera سنسکریت خود وام‌واژه‌ای دراویدی است که با ریشه‌شناسی عامیانه به śṛṅga «شاخ» بسته شده، و «زنجبیل» عربی از سریانی و آن از هندی میانه آمده، نه از یونانی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱerh₂-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:574\", \"status\": \"supports\", \"note\": \"Pokorny IEW 574-577 (POK_full.txt, the 'Page(s): 574-577' article): 'Root / lemma: Ḱer-, Ḱerə- : Ḱrā-, Ḱerei-, Ḱereu- / Meaning: head; horn, cow / Material: Old Indic śiras- n. \\\"head, cusp, peak\\\", Avestan sarah- n. \\\"head\\\" ...'. Exactly Nourai's root, language label and gloss.\"},\n        {\"ref\": \"KLN:261\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. 'cerebrum' (KLN_1966.txt line 7031, leaf 148 = printed pp. 261-262): 'L. cerebrum, \\\"brain\\\" (prob. for *kerəs-rom), fr. I.-E. base *ker-, \\\"the uppermost part of the body, head, horn, top, summit\\\", whence also OI. śiras ..., Avestic sarah-, ModPers. sar, \\\"head\\\" ...'.\"},\n        {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. 'ginger' (KLN_1966.txt line 16161, leaf 355, whose running numeral is 658, i.e. pp. 657-658): 'ME. gingevir ... fr. L. gingiber, zingiber, fr. Gk. ζιγγίβερις, fr. Pali siṅgivera-, fr. OI. śṛṅgavera-, \\\"ginger\\\", lit. \\\"hornlike\\\", fr. śṛṅgam, \\\"horn\\\", and vera, \\\"body\\\"'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 403 ff.\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line for this article reads 'References: WP. I 403 ff., WH. I 164, 203 f., 206, 207, 276, 283 f., ...', i.e. Walde-Pokorny I 403 ff. is the parent treatment of the same root.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ker-1 (= AHD New College appendix p. 1522)\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt line 618: 'ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. ... IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; ... RHINOCEROS ... 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain ... [Pok. 1. ker- 574.]'\"},\n        {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/ḱerh₂-\", \"stance\": \"supports\", \"note\": \"'*ḱerh₂- : head, top; horn', with Ancient Greek κέρας, Latin cornū, Sanskrit शृङ्ग (śṛ́ṅga), Old Armenian սար sar 'tip, top' among the descendants.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"sarah, sârah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan sarah- is a neuter s-stem 'head' (Yasna, Yašt, Vīdēvdād; cf. the compound urvi-sarah- 'with a pointed head', said of the hedgehog, Vd. 13.2), the exact match of Vedic śiras- and of Greek κάρα / κρᾶς. It continues PIE *ḱérh₂-s / oblique *ḱrh₂-es- from *ḱerh₂- 'head, horn'; Avestan and Indic show the reduplicated-vowel first syllable (Ind. śiras- for expected *saras-) that Pokorny discusses on p. 574. Nourai's second spelling 'sârah' is only his rendering of the lengthened-stem/oblique form; the dictionary form attested in Bartholomae and Pokorny is sarah-.\",\n          \"derivation_fa\": \"«سر» در اوستایی به صورت sarah- (ستاک s-دار خنثی) به معنی «سر» گواهی شده است، مثلاً در ترکیب urvi-sarah- «تیزسر» (وصف خارپشت، وندیداد ۱۳٫۲). این واژه دنبالهٔ صورت هندواروپایی آغازین *ḱérh₂-s (حالت غیرفاعلی *ḱrh₂-es-) است و درست هم‌ریشهٔ سنسکریت śiras- و یونانی κάρα/κρᾶς. پوکورنی (ص ۵۷۴) و کلاین (ص ۲۶۱) هر دو همین را می‌گویند. صورت دوم «sârah» که نورایی آورده در فرهنگ‌ها سرواژه نیست و تنها گونهٔ نگارشی اوست. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱerh₂-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:574\", \"status\": \"supports\", \"note\": \"POK_full.txt, article 'Page(s): 574-577': 'Old Indic śiras- n. ... \\\"head, cusp, peak\\\", Avestan sarah- n. \\\"head\\\"'.\"},\n            {\"ref\": \"KLN:261\", \"status\": \"supports\", \"note\": \"Klein s.v. cerebrum (leaf 148 ≈ p.261): '... whence also OI. śiras, \\\"head, summit\\\", śīrṣam, \\\"head\\\", Avestic sarah-, ModPers. sar, \\\"head\\\", Arm. sar, \\\"top\\\", Homeric Gk. κάρ, \\\"head\\\"'.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins ker-1, section IV 'Extended form *keras-. ... 2. Persian sar, head: SIRDAR.' (AHD_watkins1985.txt line 618).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb., s.v. urvi-sarah- (BRT.txt line 25757)\", \"stance\": \"supports\", \"note\": \"'j. urvi-sarah- Adj. \\\"mit spitz zulaufendem Kopf, mit spitzer Schnauze\\\", vom Igel' — the s-stem sarah- 'head' is the second member; the simplex entry itself is at col. ~1565 and was not recoverable from the OCR.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 574\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 403 ff.\", \"stance\": \"supports\", \"note\": \"cited by Pokorny as the parent treatment ('WP. I 403 ff.').\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty pass-through box stands for Middle Persian sar 'head', written with the Aramaic ideogram LOYŠE (< Aram. rēšā) and phonetically sl. Avestan/Old Iranian sarah- lost its s-stem ending in Middle Persian and became the bare noun sar 'head; top, summit; end, beginning' (MacKenzie, CPD p. 74), which is the direct ancestor of New Persian سر.\",\n          \"derivation_fa\": \"کادر خالی «پهلوی» نمایندهٔ فارسی میانهٔ sar «سر» است که در کتابت پهلوی با هُزوارش آرامی LOYŠE (از rēšā آرامی) نوشته می‌شد. پایانهٔ ستاک s-دارِ ایرانی باستان (sarah-) در فارسی میانه از میان رفت و واژه به صورت sar «سر، تارک، آغاز و انجام» درآمد (مکنزی، فرهنگ کوچک پهلوی). ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. sar (PHD_mackenzie.txt line 4493)\", \"stance\": \"supports\", \"note\": \"'sar [LOYŠE < A rʾšh; sl | M sr, N -] head; top, summit; end, beginning'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary\", \"stance\": \"silent\", \"note\": \"grep for a separate sar 'head' headword in NYB_vol2_glossary.txt returned only compounds and proper names (e.g. Xōsrōi); no independent entry found.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"سر ، افسر ، [افسار] ، ساربان ، سردار ، سالار ، سرشار\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Five of the seven words are right and one is wrong. سر sar 'head' < MP sar < Av. sarah- (confirmed). افسر afsar 'crown' < MP abesar/afsar, from Proto-Iranian *upa-sarah- / *abi-sara- 'that (which is) upon the head' — Horn, Grundriss no. 99 'efser \\\"Krone\\\", aw. *aiwi-sara-, phlv. afsar \\\"Krone\\\"'. افسار afsār 'halter, headstall' (printed on the page but dropped by the extraction) belongs with افسر, from *abi-sāra- 'what goes round the head'. سردار sardār 'commander' = sar + dār- 'holding', MP sardār; سالار sālār 'leader' is the older formation, MP sālār < Av. *sārō.dāra- (Horn no. 692, who notes that np. sardār 'ist eine junge Bildung, da man sonst *saryār erwarten müsste', i.e. sālār is the inherited form and sardār the transparent re-formation). سرشار saršār 'brimful' = sar 'top, brim' + šār (from šār-/šārīdan 'to pour, flow'), so 'flowing over the brim'. But ساربان sārbān 'caravan-leader, camel-keeper' does NOT contain sar: it is a borrowing of Parthian sārt / Sogdian sʾrth 'caravan' (itself ultimately Skt. sārtha- 'caravan') plus the agent suffix -bān; the long ā and the -t- of the source form rule out sar 'head'. Nourai's own reference BQT is silent on any sar-etymology for it.\",\n          \"derivation_fa\": \"از هفت واژهٔ این کادر شش‌تا درست است و یکی نادرست. «سر» از فارسی میانهٔ sar و آن از اوستایی sarah- است. «افسر» از فارسی میانهٔ abesar/afsar، از ایرانی آغازین *upa-sarah- «آنچه بر سر است» (هرن، بند ۹۹: «efser \\\"تاج\\\"، اوستایی *aiwi-sara-، پهلوی afsar»). «افسار» — که در متن چاپی هست ولی در استخراج JSON افتاده — هم‌خانوادهٔ «افسر» است، از *abi-sāra- «آنچه گرد سر می‌گردد». «سردار» ترکیب شفافِ سر + دار است و «سالار» صورت کهن‌تر آن، از پهلوی sālār و اوستایی *sārō.dāra- (هرن، بند ۶۹۲ تصریح می‌کند که «سردار» ساختی جوان است، وگرنه انتظار *سریار می‌رفت). «سرشار» = سر (لبه) + شار (از شاریدن «روان شدن») یعنی «لبریز». اما «ساربان» از «سر» نیست: وام‌واژه‌ای است از پارتی sārt / سغدی sʾrth «کاروان» (خود از sārtha- سنسکریت) با پسوند فاعلی ‑بان. پس این یک بند از ادعای نورایی را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ساربان\",\n            \"https://en.wiktionary.org/wiki/افسر\",\n            \"https://en.wiktionary.org/wiki/سرشار\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT\", \"status\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ (with Moʿin's notes) has all these headwords, but the citation is given without a page and Borhān offers no etymology tying ساربان to سر; Moʿin's footnotes on the س pages of vol. 2 (BQT_v2_pages.txt, leaves ~585-600) give Avestan/Pahlavi antecedents for سرو/سرون/سرین but none for ساربان.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 99 (p. 21) and no. 692 (p. 152)\", \"stance\": \"supports\", \"note\": \"no. 99 'efser \\\"Krone\\\". aw. *aiwisara-; phlv. afsar \\\"Krone\\\"'; no. 692 'sālār \\\"Anführer\\\". aw. *sārō.dāra-; phlv. sālār ... np. serdār (phlv. sardār) ist eine junge Bildung, da man sonst *seryār erwarten müsste.' Horn has no entry deriving sārbān from sar.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. ساربان\", \"stance\": \"contradicts\", \"note\": \"'Borrowed from either Parthian 𐫘𐫀𐫡𐫤 (sārt, \\\"caravan\\\") or Sogdian sʾrth (sārt, \\\"caravan\\\")'; synonyms قافله‌سالار، کاروان‌سالار. So sārbān is 'caravan-man', not 'head-man'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. افسر\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian ʾp̄ysl (aβesar). Further possibly containing a deformed prefix to سر (sar, \\\"head\\\") ... from Proto-Iranian *upasarah'; 'See also افسار (afsār, headstall)'.\"},\n            {\"src\": \"PHD\", \"where\": \"CPD s.v. sar\", \"stance\": \"supports\", \"note\": \"'sar ... head; top, summit; end, beginning' — the MP base of sar, sardār, sālār, saršār.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"srŭ 1, srvâ 1; srŭ-bhara, srvara\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The derivation is right but two of Nourai's glosses are not. Avestan srū- / srvā- f. is the u-stem of the same root (*ḱrh₂-u-); Bartholomae, Altiranisches Wörterbuch col. 1649-1650, glosses it '1) \\\"Nagel\\\" der Finger und Zehen ... 2) \\\"Horn\\\" der Tiere' — 'nail' and 'horn', NOT 'head' (the 'head' sense belongs to the s-stem sarah- of node 1). srvara- Adj. is glossed by Bartholomae simply 'gehörnt' (horned), with the analysis 'Komp.: srū- + *bara-', i.e. 'horn-bearing' from bar- 'to carry' (Nourai's ☞Bher 1 cross-reference is therefore correct), not 'carried on the head'. Pokorny prints the same: 'from the u-basis Avestan sru-, srva- \\\"horn; nail in fingers and toes\\\", srvara \\\"horned\\\" (*sru + bhara-), srvī-štay- \\\"with horny barbs\\\"'. Nourai's *srū-bhara with aspirated bh- is the Indic shape of the second member; the Iranian form is *-bara-.\",\n          \"derivation_fa\": \"اشتقاق درست است ولی دو معنی که نورایی داده دقیق نیست. اوستایی srū-/srvā- (مؤنث، ستاک u‑دار همان ریشه، *ḱrh₂-u-) در فرهنگ بارتولومه (ستون ۱۶۴۹–۱۶۵۰) چنین معنی شده است: «۱) ناخنِ دست و پا ۲) شاخِ جانوران» — یعنی «ناخن» و «شاخ»، نه «سر»؛ معنی «سر» از آنِ ستاک sarah- (گرهٔ ۱) است. صفت srvara- را نیز بارتولومه تنها «شاخ‌دار» معنی می‌کند و آن را ترکیب srū- + *bara- (از ریشهٔ bar- «بردن») می‌داند؛ پس ارجاع نورایی به ریشهٔ Bher درست است، اما ترجمهٔ «carried on the head» نادرست است و باید «شاخ‌دار / شاخ‌بَر» باشد. پوکورنی نیز همین را می‌گوید. صورت *srū-bhara با bh دمیده شکل هندی است؛ در ایرانی *-bara- است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱerh₂-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:574\", \"status\": \"supports\", \"note\": \"POK_full.txt, ker- article: 'from the u-basis Avestan sru-, srva- \\\"horn; nail in fingers and toes\\\", srvara \\\"horned\\\" (*sru + bhara-), srvī-štay- \\\"with horny barbs\\\"'.\"},\n            {\"ref\": \"BRT:1650\", \"status\": \"supports\", \"note\": \"BRT.txt col. 1649-1650: 'j. srū-, srvā- f. 1) \\\"Nagel\\\" der Finger und Zehen ... 2) \\\"Horn\\\" der Tiere ... np. surū \\\"Horn\\\"; Pa. srūv'; and on the same column 'j. srvara- Adj. \\\"gehörnt\\\" ... Komp.: srū- + *bara-'. Confirms the forms and the compound analysis, but glosses only 'nail, horn' — not 'head'.\"},\n            {\"ref\": \"LEW:905\", \"status\": \"not_checked\", \"note\": \"only the Registerband (Walde-Hofmann, 3rd ed., Heidelberg 1956) is on disk as LEW_1910.txt; its Avestan index lists 'srū I 208' and 'srvad-, srvara I 208', i.e. these Avestan forms are cited in Walde-Hofmann Band I p. 208, not p. 905. The page Nourai cites could not be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"CPD p. 76 s.v. srū, srūwar\", \"stance\": \"supports\", \"note\": \"'srū [slwbʾ | N surū(n)] horn, nail, prong'; 'srūwar [slwbwl] horned'; 'srūwēn [slwbynʾ] horny' — the Middle Persian continuations of Av. srū- and srvara-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 403 ff. (via Walde-Hofmann Register I 208)\", \"stance\": \"supports\", \"note\": \"the Register volume routes Av. srū-/srvara to the Latin cornū/cervus articles of the same root.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"sorŭ, sarŭn «سُرو ، سَرون ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سُرو surū / سَرون sarūn 'horn' continues Avestan srvā- through Middle Persian srū(w) (MacKenzie writes 'srū [slwbʾ | N surū(n)] horn, nail, prong'): the Old Iranian initial cluster sr- was resolved in New Persian by an anaptyctic vowel (sr- > sur-), and the -n of سرون is the same secondary nasal ending seen in Middle Persian srūw > surūn. Horn, Grundriss no. 734 (p. 162) states it verbatim: 'serū, surū, serūn \\\"Horn\\\". aw. srvā- \\\"Klaue, Horn\\\"; phlv. srūh (d.i. srūv), Balochi srunbe, surum \\\"Huf\\\"'. This is not the same word as سرین surīn 'buttock' (Av. sraoni-, Horn no. 737), with which Moʿin's footnote in Borhān partly conflates it. Nourai's Nezāmī verse — 'ز پیشانی هر یک از مرد و زن / سَرونی است برُسته چون کرگدن' — is the very verse printed under سَرون in Borhān-e Qāṭeʿ.\",\n          \"derivation_fa\": \"«سُرو / سَرون» فارسی نو دنبالهٔ srvā- اوستایی است از راه فارسی میانهٔ srū(w): خوشهٔ آغازینِ sr- ایرانی باستان در فارسی نو با واکهٔ میانجی شکسته شده (sr- > سُر-) و ‑ن پایانیِ «سرون» همان پایانهٔ ثانویِ فارسی میانه است. هرن در «مبانی ریشه‌شناسی فارسی نو»، بند ۷۳۴ (ص ۱۶۲) عیناً می‌نویسد: «serū، surū، serūn \\\"شاخ\\\"؛ اوستایی srvā- \\\"سُم، شاخ\\\"؛ پهلوی srūh (یعنی srūv)». مکنزی نیز srū را «شاخ، ناخن» معنی می‌کند و صورت فارسی نو را surū(n) می‌آورد. این واژه با «سرین» (اوستایی sraoni-، هرن بند ۷۳۷) یکی نیست، هرچند حاشیهٔ معین در برهان قاطع تا اندازه‌ای آن دو را در هم آمیخته است. بیت نظامی که نورایی نقل کرده همان بیتی است که در برهان ذیل «سَرون» آمده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/سرو\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:162\", \"status\": \"supports\", \"note\": \"HRN.txt line 6406 (leaf 183 = printed p. 162), entry no. 734: 'serū, surū, serūn \\\"Horn\\\". aw. srvā- \\\"Klaue, Horn\\\"; phlv. srūh (d.i. srūv), Balochi srunbe, surum \\\"Huf\\\" (348).' Exactly Nourai's arrow.\"},\n            {\"ref\": \"BQT:1130\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ vol. 2, BQT_v2_pages.txt leaf 596 (printed ≈ p. 1139 ±3 by the running-head offset), s.v. سَرون: 'سرون = بفتح اول بروزن زبون، بمعنی ...' with the very verse Nourai quotes, 'ز پیشانی هر یک از مرد و زن / سرونی است برُسته چون کرگدن — نظامی گنجوی، «گنجینه» ۸۸'; the neighbouring headword سروق is glossed 'بمعنی سرون است که شاخ گوسفند و گاو باشد'. Nourai's page number is ~9 pages low relative to this scan's numbering.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"CPD p. 76 s.v. srū\", \"stance\": \"supports\", \"note\": \"'srū [slwbʾ | N surū(n)] horn, nail, prong' — MacKenzie himself gives the New Persian outcome surū(n).\"},\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 1650\", \"stance\": \"supports\", \"note\": \"the srū-/srvā- entry closes 'np. surū \\\"Horn\\\"; nbal. vgl. sruaie Huf. — Pa. srūv'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"partial\", \"note\": \"Hübschmann is cited by Moʿin's Borhān footnote (p. 73) for the pair سرین/سرون, distinguishing NP سرین (< *srauni-) from سرون; grep of HUB.txt for 'surū' returned no separate article.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"keras, keration\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek κέρας (gen. κέρατος) 'horn' is the s-stem *ḱerh₂-s- of the root, Pokorny's 'keras- in gr. κέρας \\\"horn\\\"' (IEW 575). Its diminutive κεράτιον 'little horn' became the Greek name of the pod and, above all, the seed of the carob tree Ceratonia siliqua (the tree itself κερατέα/κερατωνία, named from the horn-shaped pod). Because carob seeds are remarkably uniform in mass, κεράτιον was already in Hellenistic times a standard small weight (1/3 of an obol, later 1/24 of a solidus). Klein s.v. carat: 'Gk. κεράτιον, \\\"a little horn; fruit of the carob tree; carat\\\", dimin. of κέρας, gen. κέρατος, \\\"horn\\\"'.\",\n          \"derivation_fa\": \"یونانی κέρας (اضافی κέρατος) «شاخ» همان ستاک s-دارِ ریشه است (*ḱerh₂-s-) که پوکورنی در ص ۵۷۵ ذیل keras- آورده است. مصغّر آن κεράτιον «شاخک» نام غلاف و به‌ویژه دانهٔ درخت خرنوب (Ceratonia siliqua) شد، چون غلاف آن شاخ‌مانند است. از آنجا که دانه‌های خرنوب وزنی یکسان دارند، κεράτιον از دورهٔ هلنیستی واحد وزنِ خردی شد (یک‌سوم اوبولوس و بعدها یک بیست‌وچهارمِ سولیدوس). کلاین (ص ۲۳۷–۲۳۸) دقیقاً همین را می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carat\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:237\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6495 (leaf 136, whose running numerals are 238-239, adjoining Nourai's 237), s.v. carat: '... fr. Arab. qirāt, \\\"fruit of the carob tree; weight of 4 grains\\\", fr. Gk. κεράτιον, \\\"a little horn; fruit of the carob tree; carat\\\", dimin. of κέρας, gen. κέρατος, \\\"horn\\\". See horn and cp. corn, \\\"hardened skin\\\".'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 575\", \"stance\": \"supports\", \"note\": \"'keras-: gr. κέρας \\\"horn\\\" (Gen. ep. κέραος, Attic -ως, newer -ατος ...)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins ker-1 IV.1\", \"stance\": \"supports\", \"note\": \"'IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; ... RHINOCEROS, TRICERATOPS.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1182 (Ar. kirāt)\", \"stance\": \"supports\", \"note\": \"'[aus gr. κεράτιον, dieses nach der Form der Früchte des Johannisbrotbaumes, Ceratonia siliqua, eigentlich \\\"Hörnchen\\\", benannt]'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Arabic\",\n          \"words\": \"qirat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic قيراط qīrāṭ 'carob seed; a small weight (1/24 of a dīnār, 1/20 of a mithqāl)' is a loan of Greek κεράτιον, taken over in the Near East along with the Byzantine weight system (Greek -tion rendered by Arabic -ṭ with emphatic ṭāʾ, the initial κ- by q-, and the Greek e coloured to ī in an open syllable). The word is pre-Islamic in Arabic usage and appears in the ḥadīth literature as a fraction of the dīnār. Al-ʿUnaysī, Tafsīr al-alfāẓ al-dakhīla, gives it as a Greek loan in so many words.\",\n          \"derivation_fa\": \"«قیراط» عربی (دانهٔ خرنوب؛ واحد وزن برابر یک بیست‌وچهارمِ دینار) وام‌واژه‌ای است از یونانی κεράτιον که همراه با نظام وزن بیزانسی به خاور نزدیک راه یافت: κ آغازین به ق، پایانهٔ ‑τιον به ‑اط (با طای مفخّم) و e یونانی در هجای باز به ī بدل شده است. این واژه پیش از اسلام در عربی به کار می‌رفته و در حدیث به عنوان کسری از دینار آمده است. طوبیا العنیسی در «تفسیر الألفاظ الدخیلة» صریحاً آن را یونانی می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carat\", \"https://en.wiktionary.org/wiki/قیراط\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:237\", \"status\": \"supports\", \"note\": \"Klein s.v. carat: 'fr. Arab. qirāt, \\\"fruit of the carob tree; weight of 4 grains\\\", fr. Gk. κεράτιον'.\"},\n            {\"ref\": \"TAD:60\", \"status\": \"supports\", \"note\": \"TAD_pages.txt line 2330 (leaf 63 ≈ printed pp. 57-59, Nourai cites 60), s.v. قراط/قيراط: 'يوناني ... ومعناه قرن صغير ويطلق على قرن الخرنوب وعلى حبة الخرنوب أيضا وكان الاقدمون يزنون الذهب بالقيراط أي حبة الخرنوب' — 'Greek ... it means \\\"little horn\\\", and is applied to the carob pod and also to the carob seed; the ancients weighed gold by the qīrāṭ, i.e. the carob seed.' Exactly Nourai's claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1182 'Ar. kirāt'\", \"stance\": \"supports\", \"note\": \"'\\\"Für Gold und Diamanten gebrauchtes Gewicht\\\" [aus gr. κεράτιον ...]; hieraus sp. quilate, pg. quirate, quilate; mlat. (bei den Alchemisten) carrātus, it. carato, frz. carat, rum. carat; dtsch. Karat, engl. carat; russ. karat.'\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. p. 85 (cited by Lokotsch)\", \"stance\": \"supports\", \"note\": \"Lokotsch's bibliography line for the entry reads '[DE 327. Eguilaz 474. Devic DEt 85. ML 6906. Kluge 227.]', i.e. Devic gives the same Greek > Arabic > Romance route.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"qîrât «قیراط»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian قیراط qīrāt is an unaltered Arabic loan of the Islamic period, taken over with the Islamic weight and coinage system; it retains the Arabic emphatic ṭāʾ in spelling although Persian has no emphatic consonants, the hallmark of a written Arabic borrowing. In Persian it denotes both the jeweller's carat and, in older usage, a twenty-fourth part (e.g. of an estate).\",\n          \"derivation_fa\": \"«قیراط» در فارسی وام‌واژه‌ای است از عربی که در دورهٔ اسلامی همراه با نظام وزن و ضرب سکه وارد شده است. نگه داشتن «ط» در املا — با آنکه فارسی واج مفخّم ندارد — نشانهٔ روشن وام‌گیری کتابی از عربی است. در فارسی هم به معنی «قیراط» جواهرفروشان است و هم در کاربرد کهن به معنی «یک بیست‌وچهارم» (مثلاً از یک ملک). ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/قیراط\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. قیراط\", \"stance\": \"supports\", \"note\": \"Moʿin marks it as an Arabic loan [ع.] like all قـ + ط words; the OCR of MON_part2 preserves the headword but not a legible etymological bracket.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rīše-hā\", \"stance\": \"silent\", \"note\": \"grep of ARY_latin_index_pages.txt for 'QIRAT'/'KARAT' returned nothing; Aryanpur's IE-root dictionary does not treat Arabic-mediated loans of this kind.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box stands for Medieval Latin carratus (also caratus), the form in which Arabic qīrāṭ entered western Europe — through the alchemical and assaying literature translated from Arabic in Spain and Sicily in the 12th-13th centuries. Lokotsch specifies 'mlat. (bei den Alchemisten) carrātus'; Klein gives 'ML. carratus (whence also It. carato)'. The doubled -rr- and the -atus ending are the Latin adaptation of the Arabic qīrāṭ with its long ā.\",\n          \"derivation_fa\": \"کادر خالی نمایندهٔ لاتینی میانه (قرون وسطایی) carratus/caratus است؛ همان صورتی که «قیراط» عربی از راه آن به اروپای باختری رسید، یعنی از میان نوشته‌های کیمیاگری و عیارسنجی که در سدهٔ ۱۲ و ۱۳ میلادی در اسپانیا و سیسیل از عربی به لاتینی ترجمه می‌شد. لوکوچ می‌نویسد «لاتینی میانه (نزد کیمیاگران) carrātus» و کلاین «ML. carratus (whence also It. carato)». دوگانه‌شدن ‑rr‑ و پایانهٔ ‑atus سازگارسازی لاتینیِ qīrāṭ عربی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carat\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; it is covered by the KLN:237 citation of its parent.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966, p. 238 s.v. carat\", \"stance\": \"supports\", \"note\": \"'F., fr. ML. carratus (whence also It. carato), fr. Arab. qirāt'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1182\", \"stance\": \"supports\", \"note\": \"'mlat. (bei den Alchemisten) carrātus, it. carato, frz. carat'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box stands for French carat, attested from the 14th century, taken from Italian carato (the Italian goldsmiths and bankers of Genoa, Venice and Florence being the intermediaries) rather than directly from the Latin: Etymonline gives 'Medieval Latin carratus, from Arabic qirat ... Italian carato, then into Old French carat by the 14th century'. Nourai's Middle Latin > French link therefore compresses one step (the Italian), but the direction and chronology are right.\",\n          \"derivation_fa\": \"کادر خالی نمایندهٔ فرانسویِ carat است که از سدهٔ چهاردهم میلادی گواهی شده. این واژه از ایتالیایی carato گرفته شده — زرگران و صرافان جنووا و ونیز و فلورانس واسطهٔ آن بوده‌اند — نه یکسره از لاتینی. اتیمانلاین می‌نویسد که qirāṭ عربی به لاتینی میانه carratus و ایتالیایی carato و از آنجا در سدهٔ چهاردهم به فرانسوی carat رسید. پس زنجیرهٔ نورایی یک حلقه (ایتالیایی) را نادیده گرفته اما جهت و زمان‌بندی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carat\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966, p. 238 s.v. carat\", \"stance\": \"supports\", \"note\": \"'carat, n., unit of weight for precious stones and pearls. — F., fr. ML. carratus'.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dict. étym. des mots ... dérivés de l'arabe\", \"stance\": \"silent\", \"note\": \"grep of PHN.txt for 'carat'/'qirat' produced no usable hit in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"carat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English carat is borrowed from French carat in the late 15th century, first as a measure of the fineness of gold (24 carats = pure gold, i.e. 24 carob seeds to the solidus), then from the 1570s as the jeweller's weight for diamonds and other precious stones. American English later split the spelling, keeping karat for gold fineness and carat for gem weight. Klein and Watkins both file it under the Greek keras branch of *ker-1.\",\n          \"derivation_fa\": \"«carat» انگلیسی در اواخر سدهٔ پانزدهم از فرانسوی carat وام گرفته شد، نخست به معنی درجهٔ خلوص زر (۲۴ قیراط = زر ناب، یعنی ۲۴ دانهٔ خرنوب در برابر یک سولیدوس) و از دههٔ ۱۵۷۰ به بعد به معنی واحد وزن الماس و سنگ‌های گران‌بها. در انگلیسی آمریکایی بعدها املای karat برای خلوص زر و carat برای وزن گوهر از هم جدا شد. کلاین و واتکینز هر دو آن را ذیل شاخهٔ κέρας یونانی از ریشهٔ *ker-1 می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carat\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins ker-1 IV.1\", \"stance\": \"supports\", \"note\": \"'Greek keras, horn: CARAT ...'; and the index line 'CARAT ker-1'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1182\", \"stance\": \"supports\", \"note\": \"'... frz. carat, rum. carat; dtsch. Karat, engl. carat; russ. karat.'\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"rhinoceros\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English rhinoceros (c. 1300, from Latin rhinoceros) goes back to Greek ῥινόκερως, a compound of ῥίς / gen. ῥινός 'nose' and κέρας 'horn' — 'nose-horned'. The second member is the same κέρας of node 6, so the arrow from the Greek box is right; the box is a shortcut that omits the Latin and Old French relay (Lat. rhinoceros > OFr. rinoceros > ME rinoceros).\",\n          \"derivation_fa\": \"«rhinoceros» انگلیسی (از حدود ۱۳۰۰ میلادی، از لاتینی rhinoceros) به یونانی ῥινόκερως بازمی‌گردد که ترکیبی است از ῥίς/ῥινός «بینی» و κέρας «شاخ»، یعنی «بینی‌شاخ» (کرگدن). جزء دوم همان κέρاسِ گرهٔ ۶ است، پس پیکان نمودار درست است؛ فقط کادر، حلقه‌های لاتینی و فرانسوی کهن را (rhinoceros > rinoceros) نادیده گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/rhinoceros\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins ker-1 IV.1\", \"stance\": \"supports\", \"note\": \"'Greek keras, horn: CARAT, CERASTES, KERATO-; ... CLADOCERAN, KERATIN, RHINOCEROS, TRICERATOPS.'\"},\n            {\"src\": \"KLN\", \"where\": \"1966, s.v. cerato- (line 7008, leaf 148 ≈ p.272)\", \"stance\": \"supports\", \"note\": \"'κερατο-, κερατ-, fr. κέρας, gen. κέρατος, \\\"horn\\\" ... See horn and cp. carat, cervine, crio-, keratin. Cp. also ... the second element in Dicruridae, Dinoceras, Megaceros, rhinoceros, Triceratops.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Greek\",\n          \"words\": \"hemi-kranion\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ἡμικρανία / ἡμικράνιον 'pain in one half of the head', a technical term of Greek medicine (Galen, 2nd c. CE), is ἡμι- 'half' (PIE *sēmi-) + κρανίον 'skull, upper part of the head'. κρανίον is Pokorny's suffixed extended form *ḱros-no- of this very root (IEW 576: 'Attic κρανίον \\\"cranium\\\"'), so the arrow from the root box is correct. Nourai's 'hemi-kranion' is the neuter variant of the better-attested feminine ἡμικρανία, which is the form that actually passed into Latin.\",\n          \"derivation_fa\": \"یونانی ἡμικρανία / ἡμικράνιον «درد نیمهٔ سر» اصطلاحی است در پزشکی یونانی (جالینوس، سدهٔ دوم میلادی) و ترکیبی است از ἡμι- «نیم» (هندواروپایی *sēmi-) و κρανίον «کاسهٔ سر». پوکورنی (ص ۵۷۶) κρανίον را صورت گسترده و پسوندداری از همین ریشه می‌داند (*ḱros-no-)، پس پیکان نمودار درست است. صورتی که نورایی آورده (خنثی) گونهٔ کم‌کاربردتر است؛ آنچه به لاتینی راه یافت صورت مؤنث ἡμικρανία بود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/migraine\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:831\", \"status\": \"supports\", \"note\": \"AHD's 'migraine' entry (New College ed. p. 831) traces the word to Late Latin hemicrania < Greek hēmikrania; the appendix root entry (AHD_watkins1985.txt line 618) has 'ker-1 ... 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 576\", \"stance\": \"supports\", \"note\": \"'gr. ἑκατογ-κρανος \\\"100 headed\\\", ... Attic κρανίον \\\"cranium\\\", ὠλέκρανον \\\"elbow\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"1966, s.v. cerebrum (p. 261)\", \"stance\": \"supports\", \"note\": \"'... Gk. κρανίον, \\\"skull\\\" ... Cp. cranium and words there referred to.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"hemi-crania\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Late Latin hemicrania is a straight medical borrowing of Greek ἡμικρανία, current in the Latin translations of Greek medicine from late antiquity onwards (Caelius Aurelianus, and the Salernitan tradition). It is one of the many Graecisms of Latin medical vocabulary and was never a native Latin formation.\",\n          \"derivation_fa\": \"لاتینی متأخر hemicrania وام‌واژه‌ای یکسره پزشکی از یونانی ἡμικρανία است که از اواخر دورهٔ باستان به بعد در ترجمه‌های لاتینیِ طب یونانی (کائلیوس آورلیانوس و سنت سالرنو) رواج داشته است. این واژه ساخت بومی لاتینی نیست، بلکه از شمار همان یونانی‌گرایی‌های فراوانِ واژگان پزشکی لاتینی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/migraine\"],\n          \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own.\"}],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966, s.v. migraine\", \"stance\": \"supports\", \"note\": \"Klein derives migraine from OF. migraine, from Late L. hemicrania, from Gk. hēmikrania.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde-Hofmann Registerband\", \"stance\": \"silent\", \"note\": \"no entry for hemicrania in the index volume on disk; the word is a late Graecism outside Walde-Hofmann's inherited-lexicon scope.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"French\",\n          \"words\": \"migrene\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French migraine / migraigne (13th c.) is the popular development of Late Latin hemicrania: the unstressed initial he- was lost (aphaeresis, as in Lat. episcopus > OFr. evesque), *emicrania > *micrania, the intervocalic -cr- was voiced and the ending re-shaped by the very productive suffix -aigne / -aine (< Lat. -ānia), giving migraigne, migraine. The word kept the medical sense 'headache, half-head pain' throughout.\",\n          \"derivation_fa\": \"فرانسویِ کهن migraine/migraigne (سدهٔ سیزدهم) دنبالهٔ عامیانهٔ hemicrania لاتینی متأخر است: هجای بی‌تکیهٔ آغازین he- افتاده (همان فرایندی که episcopus را به evesque رساند)، *emicrania > *micrania، سپس ‑cr‑ میان‌واکه‌ای واک‌دار شده و پایانه با پسوند بسیار زایای ‑aigne/‑aine (از ‑ānia لاتینی) بازساخته شده است. معنی پزشکی «سردرد، درد نیمهٔ سر» در سراسر این تحول پایدار مانده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/migraine\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:831\", \"status\": \"supports\", \"note\": \"AHD s.v. migraine (p. 831): 'Middle English migrane, from Old French migraine, from Late Latin hemicrania, from Greek hēmikrania: hēmi-, half + kranion, skull.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. migraine\", \"stance\": \"supports\", \"note\": \"same chain OF migraine < Late L. hemicrania < Gk. hēmikrania.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. migraine\", \"stance\": \"supports\", \"note\": \"'The word entered English in the late 14th century as migrane, borrowed from Old French migraine or migraigne'; from Late Latin hemicrania 'pain in one side of the head'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"mîgren «میگرن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian میگرن mīgren is a 20th-century borrowing of French migraine, taken over with the rest of the French medical vocabulary that entered Persian through the Dār al-Fonūn and the Iranian physicians trained in France; the final -e of French migraine is rendered by -en in Persian spelling because the source is the spoken French [miɡʁɛn]. Moʿin's Farhang-e Fārsi gives it as a headword glossed with the Arabic-Persian medical term صداع شقی 'hemicranial headache', i.e. a calque of the Greek sense.\",\n          \"derivation_fa\": \"«میگرن» فارسی وام‌واژه‌ای است از فرانسویِ migraine در سدهٔ چهاردهم خورشیدی، همراه با انبوه واژگان پزشکی فرانسوی که از راه دارالفنون و پزشکان فرانسه‌دیده وارد فارسی شد. تلفظ فرانسویِ [miɡʁɛn] است، از این‌رو در فارسی «میگرن» نوشته می‌شود نه *میگرین. معین در «فرهنگ فارسی» این سرواژه را با معادل پزشکی «صداع شقی» (سردرد نیمهٔ سر) معنی کرده که خود گَرته‌برداری از معنی یونانی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/migraine\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:4503\", \"status\": \"partial\", \"note\": \"the printed page number (Moʿin vol. 4, the volume of foreign compounds) could not be mapped in the OCR on disk, but the entry itself is there: MON_part2.txt line 70555 'میگرن: [فر.] (ا.) (پز.) صداع شقی' (the origin bracket is garbled by the OCR to '0 زر ]'), i.e. Moʿin does carry میگرن as a European loan with the sense 'half-head headache'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. میگرن (MON_part2.txt line 70555)\", \"stance\": \"supports\", \"note\": \"'میگرن: ... (ا.) (پز.) صداع شقی' — a noun of the medical register glossed 'hemicranial headache'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rīše-hā\", \"stance\": \"silent\", \"note\": \"grep for MIGREN/MIGRAINE in ARY_latin_index_pages.txt returned nothing; the book covers inherited Indo-European vocabulary, not modern European loans.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"migraine\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English migraine is attested from the late 14th century as migrane, borrowed from Old French migraine; the popular English descendant of the same word, megrim, is current from the 15th century and now obsolete, while the modern spelling and pronunciation of migraine were re-borrowed from French in the 18th century. AHD files it under the root *ker-1 through Greek kranion.\",\n          \"derivation_fa\": \"«migraine» انگلیسی از اواخر سدهٔ چهاردهم به صورت migrane گواهی شده و وام‌واژه‌ای است از فرانسویِ کهن migraine. صورت عامیانهٔ همان واژه در انگلیسی، megrim، از سدهٔ پانزدهم رایج بوده و امروز متروک است؛ املا و تلفظ کنونی migraine در سدهٔ هجدهم دوباره از فرانسوی گرفته شد. فرهنگ American Heritage آن را از راه κρανίον یونانی ذیل ریشهٔ *ker-1 جای می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/migraine\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:831\", \"status\": \"supports\", \"note\": \"AHD s.v. migraine, p. 831, with the root reference to ker-1; the appendix (AHD_watkins1985.txt line 618) lists MIGRAINE under 'ker-1 ... 4. Suffixed extended form *kros-no- in Greek kranion'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. migraine\", \"stance\": \"supports\", \"note\": \"ME migrane < OF migraine < Late L. hemicrania.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. migraine\", \"stance\": \"supports\", \"note\": \"'late 14c. as migrane ... An alternate form, megrim, became common from the 15th century onward but is now considered archaic or obsolete.'\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Different Languages\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A collector box: Nourai uses 'Different Languages' for the several branches through which the root reached English independently of the Greek and Iranian lines drawn above — Germanic (*hurnaz > OE horn), Italic (Lat. cornū > OFr. corniere > corner), and the Greek κάρα/καρωτόν line. The reference 'AHD' is to Watkins' root article, which does exactly this gathering.\",\n          \"derivation_fa\": \"این کادر یک «کادر گردآور» است: نورایی عنوان «زبان‌های گوناگون» را برای شاخه‌های چندگانه‌ای به کار می‌برد که این ریشه، جدا از خط یونانی و ایرانیِ بالای صفحه، از راه آن‌ها به انگلیسی رسیده است — ژرمنی (*hurnaz > انگلیسی کهن horn)، ایتالیک (لاتینی cornū > فرانسوی کهن corniere > corner) و خط یونانی κάρα/καρωτόν. ارجاع «AHD» به مقالهٔ ریشهٔ واتکینز است که دقیقاً همین گردآوری را می‌کند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins ker-1 assembles Germanic *hurnaz (HORN), Latin cornū (CORN2, CORNEA, CORNER, CORNET, CORNU ...), Greek karōton (CARROT) and Greek karā (CHEER) under one root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 574-577\", \"stance\": \"supports\", \"note\": \"the same article gathers Latin cornū, Old High German hurnuz, Greek κάρα, κρανίον etc.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 s.v. horn (leaf 400 ≈ p. 777)\", \"stance\": \"supports\", \"note\": \"'ME., fr. OE. horn ... cogn. with Gk. κέρας, Galatian Gk. κάρνον, L. cornu, OI. śṛṅgam, \\\"horn\\\", fr. I.-E. base *ker-, \\\"the uppermost part of the body, head, horn, top, summit\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"carrot, cheek, corner, horn\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Three of the four are right, the second is a misprint. CARROT: Old French carotte < Late Latin carōta < Greek καρωτόν, so named from the horn-like shape of the root — Watkins, ker-1 §I.5c 'Greek karōton, carrot (from its hornlike shape): CARROT'. CORNER: Anglo-French cornere, from Old French corne 'horn, corner' < Vulgar Latin *corna < Latin cornū — Watkins ker-1 §I.1b lists CORNER among the cornū derivatives. HORN: OE horn < Proto-Germanic *hurnaz < zero-grade *ḱr̥-n- — Watkins ker-1 §I.1a. But CHEEK does not belong to this root at all: English cheek < ME cheke < OE ċēce/ċēace 'cheek, jaw' < Proto-West-Germanic *kākā/*keukā < Proto-Germanic *kēkǭ/*keukǭ 'jaw, palate, pharynx', perhaps from PIE *ǵyewh₁- 'to chew'. What Watkins actually lists under ker-1 §I.5a is CHEER (Greek karā 'head' > Late Latin cara 'face' > OFr. chiere > ME chere), and the AHD index prints 'CHEER ker-1' with no entry for CHEEK at all. The printed page of the book itself reads 'carrot, cheek, corner, horn' (verified on the page image at 600 dpi, copy saved to data/verification/sources/refs/ocr/BOOK/256.png), so this is Nourai's own misprint for 'cheer', not an extraction error.\",\n          \"derivation_fa\": \"از چهار واژهٔ این کادر سه‌تا درست است و دومی خطای چاپی. carrot: از فرانسویِ کهن carotte، از لاتینی متأخر carōta، از یونانی καρωτόν که به سبب شکل شاخ‌مانند ریشه‌اش چنین نام گرفته (واتکینز، ker-1، بند ۵ج). corner: از انگلوفرانسه cornere، از corne فرانسویِ کهن «شاخ، گوشه»، از cornū لاتینی (واتکینز، بند ۱ب). horn: از انگلیسی کهن horn، از ژرمنی آغازین *hurnaz، از درجهٔ صفرِ *ḱr̥-n- (بند ۱الف). اما cheek به‌هیچ‌روی از این ریشه نیست: از انگلیسی میانهٔ cheke و انگلیسی کهنِ ċēce/ċēace «گونه، آرواره»، از ژرمنی آغازین *kēkǭ «آرواره، کام»، شاید از ریشهٔ *ǵyewh₁- «جویدن». آنچه واتکینز زیر ker-1 آورده cheer است (یونانی κάρα «سر» > لاتینی متأخر cara «چهره» > فرانسویِ کهن chiere > انگلیسی cheer)، و در نمایهٔ AHD نیز «CHEER ker-1» آمده و اصلاً مدخلی برای CHEEK نیست. تصویر صفحهٔ چاپی (با تفکیک ۶۰۰ نقطه بر اینچ) نشان می‌دهد که خودِ کتاب «cheek» چاپ کرده است؛ پس این خطای چاپی نورایی است، نه خطای خوانش اسکن.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"carrot, cheek, corner, horn\",\n          \"correct_form\": \"carrot, cheer, corner, horn\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/cheek\",\n            \"https://www.etymonline.com/word/cheer\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; the parent box cites AHD, which is the source checked below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, ker-1 and the index (AHD_watkins1985.txt lines 618, 1335, 1348, 1394)\", \"stance\": \"contradicts\", \"note\": \"the root article has '5. Suffixed form *kr-ā- in: a. Greek karē, kara, head: CHARIVARI; CHEER; ... c. Greek karōton, carrot: CARROT'; the index lines read 'CARROT ker-1', 'CORNER ker-1', 'CHEER ker-1' — there is no 'CHEEK ker-1' anywhere in Watkins.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. cheek\", \"stance\": \"contradicts\", \"note\": \"'From Middle English cheeke, cheke ... from Old English ċēce, ċēace, ċēoce (\\\"cheek; jaw\\\"), from Proto-West Germanic *kākā, *keukā ... from Proto-Germanic *kēkǭ, *keukǭ (\\\"jaw; palate; pharynx\\\"), perhaps from Proto-Indo-European *ǵyewh₁- (\\\"to chew\\\")'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. cheer\", \"stance\": \"supports\", \"note\": \"'c. 1200, \\\"the face, countenance\\\" ... from Late Latin cara \\\"face\\\" ... possibly from Greek kara \\\"head\\\" (from PIE root *ker- (1) \\\"horn; head\\\")' — i.e. cheer, not cheek, is the word that belongs here.\"}\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"srnga; sringa-vera\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"श‍ृङ्ग śṛ́ṅga- n. 'horn, tusk' is genuinely from this root: Pokorny (IEW 575) analyses it as *ḱr̥-n-go-, an extension of the n-stem *ḱer-(e)n-, and Klein cites 'OI. śṛṅgam, \\\"horn\\\"' under horn. That half of the box is confirmed (though Mayrhofer treats the -g- formation as unclear). But शृङ्गवेर śṛṅgavera- 'ginger' is not a Sanskrit compound of śṛṅga 'horn' + vera 'body' at all: it is a Sanskritisation of Middle Indic (Prakrit) siṃgivera, itself borrowed from Old Tamil/Dravidian iñci-vēr 'ginger root' (Tamil இஞ்சி iñci 'ginger' + வேர் vēr 'root'; Malayalam inchi-ver), and the 'horn' analysis is a folk etymology invented in India to make the loan look Sanskrit. Yule and Burnell had already said so in 1903: 'The Skt. name is sringavera, professedly connected with sringa, \\\"a horn\\\", from the antler-like form of the root. But this is probably an introduced word shaped by this imaginary etymology ... in Malayalam green ginger is called inchi and inchi-ver, from ver \\\"root\\\".' Nourai here reproduces Klein's and AHD's older analysis; modern scholarship rejects it.\",\n          \"derivation_fa\": \"«شریگ / śṛ́ṅga-» سنسکریت به معنی «شاخ» به‌راستی از همین ریشه است: پوکورنی (ص ۵۷۵) آن را *ḱr̥-n-go-، گسترشی از ستاک n-دارِ *ḱer-(e)n-، تحلیل می‌کند و کلاین نیز آن را ذیل horn می‌آورد؛ پس این نیمهٔ کادر درست است (هرچند مایرهوفر ساخت ‑g‑ را روشن نمی‌داند). اما śṛṅgavera- «زنجبیل» هرگز ترکیب سنسکریتِ śṛṅga «شاخ» + vera «تن» نیست: این واژه سنسکریتی‌شدهٔ صورت هندی میانه (پراکریت) siṃgivera است که خود وام‌واژه‌ای است از دراویدیِ کهن iñci-vēr «ریشهٔ زنجبیل» (تامیلی iñci «زنجبیل» + vēr «ریشه»؛ ملیالمی inchi-ver)، و تحلیلِ «شاخ» ریشه‌شناسی عامیانه‌ای است که در هند ساخته شد تا وام‌واژه سنسکریت بنماید. یول و برنل در «هابسون‑جابسون» (۱۹۰۳) پیش‌تر همین را گفته بودند. نورایی در اینجا تحلیل کهنِ کلاین و AHD را بازمی‌گوید؛ پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/शृङ्गवेर\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1522\", \"status\": \"partial\", \"note\": \"the AHD appendix page for ker-1 (New College ed. p. 1522) does not in fact list Sanskrit śṛṅga at all; what it gives is 'Greek keras, horn' and the Germanic/Latin forms. AHD's word entry 'ginger' (p. 667, see node 29) is the place where AHD gives 'from Sanskrit śṛṅgavera : śṛṅgam, horn + vera, body'. So the citation supports the traditional analysis but not on the page cited.\"},\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 657 s.v. ginger: '... fr. OI. śṛṅgavera-, \\\"ginger\\\", lit. \\\"hornlike\\\", fr. śṛṅgam, \\\"horn\\\", and vera, \\\"body\\\"; so called in allusion to the hornlike shape of the root.' This is exactly Nourai's claim — and exactly the analysis now regarded as folk etymology.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp. 374-375 s.v. GINGER\", \"stance\": \"contradicts\", \"note\": \"'The Skt. name is sringavera, professedly connected with sringa, \\\"a horn\\\", from the antler-like form of the root. But this is probably an introduced word shaped by this imaginary etymology ... in the language of that province (Malayalam) green ginger is called inchi and inchi-ver, from ver, \\\"root\\\".'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. शृङ्गवेर\", \"stance\": \"contradicts\", \"note\": \"'Sanskritism of Prakrit siṃgivera, with influence of शृङ्ग (\\\"horn\\\"), borrowed from Old Tamil iñcivēr (\\\"ginger root\\\"), equivalent to Tamil இஞ்சி (\\\"ginger\\\") + வேர் (\\\"root\\\")'.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 575\", \"stance\": \"supports\", \"note\": \"for śṛṅga alone: 'śṛṅga- (*ḱr̥-n-go-) n. \\\"horn\\\", of n-stem *ḱer-(e)n- ... compare gr. κραγγών \\\"crab\\\"'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1930 'Sskr. śṛṅgavera'\", \"stance\": \"partial\", \"note\": \"Lokotsch heads the article with the Sanskrit and glosses it '[eigentlich \\\"hornartig\\\"; so sind die Wurzeln des braunen oder gemeinen Ingwers tatsächlich beschaffen]' — the traditional analysis again, but he derives Arabic and Greek in parallel from the Indic form, not one from the other.\"}\n          ]\n        },\n        {\n          \"id\": 21,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"šanga-vîr, singiber\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Persian form of the ginger word certainly existed and is the link between India and both Persian شنگبیل and the Semitic forms: Jeffery (Foreign Vocabulary of the Qurʾān p. 154, following Vullers, Lex. ii 148 and the Pahlavi Texts) cites 'Phlv. singaβēr' as the source of Armenian and Syriac forms. Nourai's šanga-vīr is a legitimate rendering of that (*šanga-vēr / singabēr), and Wiktionary reconstructs Persian شنگویر šangevir as a direct descendant of Sanskrit śṛṅgavera. What is wrong is the second word in the box: 'singiber' is not a Pahlavi form but the Latin (gingiber/zingiber) shape of node 27, so it does not belong in a Pahlavi box. The form is not in MacKenzie's Concise Pahlavi Dictionary (grep of PHD returns srū, srūwar, srub but no singaber), so it rests on Vullers and the Zoroastrian Middle Persian glossaries.\",\n          \"derivation_fa\": \"صورتی فارسی میانه از نام زنجبیل بی‌گمان وجود داشته و حلقهٔ پیوند میان هند و هم «شنگبیل» فارسی و هم صورت‌های سامی است: جفری در «واژه‌های دخیل در قرآن» (ص ۱۵۴) به پیروی از فولرس و متون پهلوی صورت singaβēr پهلوی را سرچشمهٔ صورت‌های ارمنی و سریانی می‌داند، و ویکی‌واژه «شنگویر» فارسی را وام مستقیم از śṛṅgavera سنسکریت می‌شمارد. پس «šanga-vîr» نورایی پذیرفتنی است. اما واژهٔ دوم کادر نادرست جای گرفته: «singiber» صورت پهلوی نیست، بلکه همان صورت لاتینی (gingiber/zingiber) گرهٔ ۲۷ است. این صورت در فرهنگ پهلویِ مکنزی نیامده (جست‌وجو تنها srū و srūwar و srub را می‌دهد) و تکیهٔ آن بر فولرس و واژه‌نامه‌های پهلوی زردشتی است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/شنگویر\"],\n          \"ref_check\": [\n            {\"ref\": \"VDQ:42\", \"status\": \"partial\", \"note\": \"VDQ (Badreʾi's Persian translation of Jeffery) is not on disk and noorlib's viewer is JS-only; checked in the original instead — Jeffery, FVQ p. 154 note 1 and text: 'The Mod. Pers. word for ginger is زنجبیل (Vullers, Lex, ii, 472; cf. also ii, 148) from Phlv. singaβēr, which is the source of the Arm. ... and the Syr. ...'. So the Pahlavi form is Jeffery's, but Jeffery cites it as singaβēr, not šanga-vīr, and he says nothing about a Pahlavi 'singiber'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (grep of PHD.txt / PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"no entry for singaber / šangavēr; MacKenzie's s-section runs 'srēš, srū, srub, srūdan, srūwar, srūwēn, stabr ...' with no ginger word.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān pp. 153-154\", \"stance\": \"supports\", \"note\": \"'... from Phlv. singaβēr, which is the source of the Arm. and the Syr. ... The ultimate source seems to have been the Skt. śṛṅgavera, Pali siṅgivera.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. شنگویر\", \"stance\": \"supports\", \"note\": \"'Borrowed from Sanskrit शृङ्गवेर (śṛṅgavēra). Doublet of زنجفیل and زنجبیل'; alternative forms شنگویل، شنگبیر، شنگبیل.\"}\n          ]\n        },\n        {\n          \"id\": 22,\n          \"lang\": \"Persian\",\n          \"words\": \"šangabîl «شنگبیل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian شنگبیل šangabīl (also شنگویر šangevir, شنگبیر šangebir, شنگویل šangevil) 'ginger' is the inherited Iranian form of the Indian word — borrowed from Sanskrit/Middle Indic śṛṅgavera through Middle Persian *šangavēr/singabēr, with the regular Persian variation r ~ l in the second syllable (šangevir ~ šangevil ~ šangebil) and voicing of the medial v > b. It is therefore a doublet of زنجبیل zanjabīl (node 26), which reached Persian by the long way round through Syriac and Arabic.\",\n          \"derivation_fa\": \"«شنگبیل» فارسی (و گونه‌های شنگویر، شنگبیر، شنگویل) صورت ایرانیِ برجای‌ماندهٔ نام هندی زنجبیل است: وام‌واژه‌ای از śṛṅgavera سنسکریت/هندی میانه از راه فارسی میانهٔ *šangavēr/singabēr، با ابدال قاعده‌مند ر ~ ل در هجای پایانی (شنگویر ~ شنگویل ~ شنگبیل) و بدل شدن v میانی به b. بنابراین «شنگبیل» دوگانهٔ (doublet) «زنجبیل» است — همان واژه که راه دورتری را از هندی به سریانی و عربی و سپس فارسی پیموده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/شنگویر\", \"https://en.wiktionary.org/wiki/शृङ्गवेर\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1751\", \"status\": \"not_found\", \"note\": \"grep of MON_part1/MON_part2 for شنگبیل، شنگویر، شنگب returned nothing; the OCR of Moʿin on disk has زنجبیل (MON_part1 line 71763, in the ز section, which is where p. 1751 falls) but no شنگبیل headword. Nourai's page number therefore looks like the زنجبیل page rather than a شنگبیل page.\"},\n            {\"ref\": \"VDQ:42\", \"status\": \"partial\", \"note\": \"not accessible (noorlib is JS-only, no local copy); the corresponding passage of the original, Jeffery FVQ p. 154, gives the Pahlavi and Persian forms but writes the Modern Persian as زنجبیل, not شنگبیل.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. شنگویر\", \"stance\": \"supports\", \"note\": \"'Alternative forms: شنگویل (šangevil), شنگبیر (šangebir), شنگبیل (šangebil). Borrowed from Sanskrit शृङ्गवेर (śṛṅgavēra). Doublet of زنجفیل and زنجبیل.'\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (OCR on disk)\", \"stance\": \"silent\", \"note\": \"no شنگبیل headword recoverable; the ش section of MON_part1 (lines ~86927 ff.) runs شنگ، شنگول with no ginger word in the OCR.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. GINGER\", \"stance\": \"partial\", \"note\": \"Yule and Burnell record the Indian and Arabic forms but not the Persian شنگبیل.\"}\n          ]\n        },\n        {\n          \"id\": 23,\n          \"lang\": \"Pali\",\n          \"words\": \"singivera\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pali siṅgivera- 'ginger' is the Middle Indic form of the word — the regular Prakrit outcome of the cluster (Skt. śṛṅga- > Pali siṅga-) applied to the Dravidian loan. It is this Middle Indic form, not the Sanskritised śṛṅgavera, that was actually exported westwards by the Indian Ocean spice trade, which is why the Greek, Syriac and Arabic forms all show si-/zi- rather than śṛ-. Klein gives 'fr. Pali siṅgivera-' in the ginger chain.\",\n          \"derivation_fa\": \"پالیِ siṅgivera- «زنجبیل» صورت هندی میانهٔ واژه است: خوشهٔ سنسکریتِ śṛṅga- در پالی به siṅga- بدل می‌شود و همین قاعده بر وام‌واژهٔ دراویدی نیز اِعمال شده است. آنچه بازرگانی ادویه در اقیانوس هند به باختر صادر کرد همین صورت هندی میانه بود، نه صورت سنسکریتی‌شدهٔ śṛṅgavera؛ به همین سبب است که صورت‌های یونانی و سریانی و عربی همگی si-/zi- دارند نه śṛ-. کلاین (ص ۶۵۷) نیز در زنجیرهٔ ginger «از پالیِ siṅgivera-» می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/शृङ्गवेर\", \"https://en.wiktionary.org/wiki/ζιγγίβερις\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 657 s.v. ginger: 'fr. L. gingiber, zingiber, fr. Gk. ζιγγίβερις, fr. Pali siṅgivera-, fr. OI. śṛṅgavera-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"AHD s.v. ginger (p. 667)\", \"stance\": \"supports\", \"note\": \"'from Greek zingiberis, from Pali siṅgivera, from Sanskrit śṛṅgavera'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Ancient Greek ζιγγίβερις, etymology\", \"stance\": \"partial\", \"note\": \"the Greek is derived from Sauraseni Prakrit siṃgivera rather than from Pali specifically — i.e. from Middle Indic generally, which includes Nourai's Pali.\"}\n          ]\n        },\n        {\n          \"id\": 24,\n          \"lang\": \"Greek\",\n          \"words\": \"ziggiberis\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Greek ζιγγίβερις 'ginger' is first attested in Dioscorides (De materia medica ii.189, c. 65 CE, who says it grows 'for the most part in Troglodytic Arabia') and in Pliny as zimpiberi/zingiberi. Its ultimate source is certainly Middle Indic siṃgivera / siṅgivera; the point on which modern scholarship differs from Klein (and hence from Nourai) is the route: Beekes (Etym. Dict. of Greek, p. 501) and Wiktionary posit an unattested Middle Iranian intermediary rather than a direct Pali > Greek transfer, which explains the voicing of the initial (s- > z-) and of the -g-. The arrow is therefore right in substance but omits an Iranian relay.\",\n          \"derivation_fa\": \"یونانی ζιγγίβερις «زنجبیل» نخستین بار در «مواد دارویی» دیوسکوریدس (۲٫۱۸۹، حدود ۶۵ میلادی) و نزد پلینیوس به صورت zimpiberi/zingiberi گواهی شده است. سرچشمهٔ نهایی آن بی‌گمان صورت هندی میانهٔ siṃgivera است؛ اختلاف پژوهش امروزی با کلاین (و در نتیجه با نورایی) بر سر مسیر است: بیکس در «فرهنگ ریشه‌شناختی یونانی» (ص ۵۰۱) و ویکی‌واژه واسطه‌ای ایرانی میانه (گواهی‌نشده) را فرض می‌کنند، نه انتقال مستقیم پالی به یونانی؛ همین واسطه واک‌دار شدن آغازهٔ s- به z- و نیز ‑g‑ را توضیح می‌دهد. پس پیکان در اصل درست است اما یک حلقهٔ ایرانی را نادیده گرفته. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/ζιγγίβερις\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 657: 'fr. Gk. ζιγγίβερις, fr. Pali siṅgivera-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. ζιγγίβερις (citing Beekes p. 501)\", \"stance\": \"partial\", \"note\": \"'Via unattested Middle Iranian from Sauraseni Prakrit siṃgivera'; descendants listed include Latin zingiberi and Jewish Babylonian Aramaic זַנְגְּבִילָא.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. GINGER, quotation from Dioscorides ii.189\", \"stance\": \"supports\", \"note\": \"'Ginger (Ζιγγίβερις) is a special kind of plant produced for the most part in Troglodytic Arabia' — the earliest Greek attestation, c. A.D. 65.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1930\", \"stance\": \"partial\", \"note\": \"'mit Schwinden des vokalischen r wurde ar. zenǧebīl, tk. zingifre sowie gr. Ζιγγίβερις, lat. zingiber' — Lokotsch makes Arabic and Greek parallel offshoots of the Indic word, not one from the other.\"}\n          ]\n        },\n        {\n          \"id\": 25,\n          \"lang\": \"Arabic\",\n          \"words\": \"zanzabîl\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Arabic word is زنجبيل zanjabīl (Qurʾān 76:17, 'a cup whose mixture is zanjabīl'), so the book's 'zanzabîl' with z for ج is a misprint in the printed page (verified on the page image; the extraction is faithful). More important is the arrow: Nourai draws Greek ζιγγίβερις > Arabic and annotates 'From Greek through Syriac', but no source says Syriac took the word from Greek. Jeffery, whose Persian translation (VDQ) is Nourai's own reference, writes (FVQ 154): 'The Mod. Pers. word for ginger is زنجبیل ... from Phlv. singaβēr, which is the source of the Arm. and the Syr. ܙܢܓܒܝܠ; Aram. זנגבילא. The ultimate source seems to have been the Skt. śṛṅgavera, Pali siṅgivera, from which comes the Gk. ζιγγίβερις. There can be little doubt that the word passed into Arabic from Syr.' — i.e. Syriac got it from Middle Persian/Middle Indic, and Greek is a sister branch, not the ancestor. Wiktionary agrees: Arabic زنجبيل < Syriac ܙܢܓܒܝܠ zangabīl < Sauraseni Prakrit siṃgivera < Old Tamil. Lokotsch likewise makes ar. zenǧebīl and gr. Ζιγγίβερις parallel derivatives of the Indic form. The Arabic form was early enough to appear in pre-Islamic poetry, and Arab lexicographers (Thaʿālibī, Fiqh 318; al-Jawālīqī, Muʿarrab 78) list it among the Persian loanwords.\",\n          \"derivation_fa\": \"صورت درست عربی «زنجبیل» است (قرآن، انسان ۱۷: «کأساً کان مزاجها زنجبیلاً»)؛ آنچه در کتاب چاپ شده — «zanzabîl» با z به‌جای ج — خطای چاپیِ خودِ کتاب است (بر روی تصویر صفحه بررسی شد؛ استخراج JSON وفادار است). مهم‌تر، جهت پیکان است: نورایی ζιγγίβερις یونانی را سرچشمهٔ صورت عربی می‌گیرد و در حاشیه می‌نویسد «از یونانی از راه سریانی»، حال آنکه هیچ منبعی نمی‌گوید سریانی این واژه را از یونانی گرفته است. جفری — که ترجمهٔ فارسی کتابش (VDQ) خودِ مأخذ نورایی است — در ص ۱۵۴ می‌نویسد که «زنجبیل» فارسی از پهلوی singaβēr است و همین صورت پهلوی سرچشمهٔ صورت‌های ارمنی و سریانی است، و سرچشمهٔ نهایی śṛṅgavera سنسکریت و siṅgivera پالی است «که ζιγγίβερις یونانی نیز از آن آمده»، و «تردیدی نیست که این واژه از سریانی به عربی رسیده». یعنی یونانی شاخهٔ خواهر است نه نیا. ویکی‌واژه و لوکوچ نیز همین را می‌گویند. صورت عربی چنان کهن است که در شعر جاهلی آمده، و لغویان عرب (ثعالبی، فقه‌اللغة ۳۱۸؛ جوالیقی، المعرّب ۷۸) آن را در شمار وام‌واژه‌های فارسی آورده‌اند. پژوهش امروزی مسیرِ نمودار را رد می‌کند.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"zanzabîl\",\n          \"correct_form\": \"zanjabīl (زنجبيل)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/زنجبيل\"],\n          \"ref_check\": [\n            {\"ref\": \"VDQ:238\", \"status\": \"contradicts\", \"note\": \"VDQ is Badreʾi's Persian translation of Jeffery and is not on disk (noorlib viewer is JS-only), so the original was read instead: FVQ pp. 153-154 (FVQ.txt lines 9732-9770). Jeffery derives Syriac ܙܢܓܒܝܠ from Pahlavi singaβēr and treats Greek ζιγγίβερις as a parallel derivative of Skt./Pali; he never routes Syriac through Greek. So Nourai's own reference does not support the Greek > Arabic arrow, and his NOTE 'From Greek through Syriac' misreports it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān, pp. 153-154 s.v. زنجبيل\", \"stance\": \"contradicts\", \"note\": \"'The Mod. Pers. word for ginger is زنجبیل ... from Phlv. singaβēr, which is the source of the Arm. and the Syr. ...; Aram. זנגבילא. The ultimate source seems to have been the Skt. śṛṅgavera, Pali siṅgivera, from which comes the Gk. ζιγγίβερις. There can be little doubt that the word passed into Arabic from Syr. and was thence borrowed back into Persian in Islamic times. It occurs in the early poetry and so was evidently an early borrowing.'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. زنجبيل (Arabic)\", \"stance\": \"contradicts\", \"note\": \"'From Syriac ܙܢܓܒܝܠ (zangabīl), ܙܢܓܒܝܪ (zangabīr), from Sauraseni Prakrit siṃgivera, siṃgavera, from Old Tamil iñcivēr.' No Greek link.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1930\", \"stance\": \"partial\", \"note\": \"'mit Schwinden des vokalischen r wurde ar. zenǧebīl, tk. zingifre sowie gr. Ζιγγίβερις, lat. zingiber' — Arabic and Greek as parallel outcomes of Skt. śṛṅgavera.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. GINGER\", \"stance\": \"partial\", \"note\": \"'We get this word from the Arabic zanjabīl, Sp. agengibre (al-zanjabīl), Port. gingibre, Latin zingiber ...' — the Arabic form is zanjabīl/zinjabīl, never *zanzabīl.\"}\n          ]\n        },\n        {\n          \"id\": 26,\n          \"lang\": \"Persian\",\n          \"words\": \"zanjebîl «زنجبیل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian زنجبیل zanjabīl is the Arabic word taken back into Persian in the Islamic period — a round trip: an Indian word entered Middle Persian as *singabēr, passed from there into Syriac zangabīl and from Syriac into Arabic zanjabīl, and the Arabic form was then re-borrowed into New Persian, displacing the inherited شنگبیل (node 22) in ordinary use. Jeffery states the round trip explicitly ('borrowed back into Persian in Islamic times'), and Moʿin's Farhang-e Fārsi tags the headword [ع.] 'Arabic' with the variants زنجفیل، جنزبیل. The word is a doublet of شنگبیل.\",\n          \"derivation_fa\": \"«زنجبیل» فارسی همان واژهٔ عربی است که در دورهٔ اسلامی به فارسی بازگشته — یک سفر رفت‌وبرگشت: واژه‌ای هندی به فارسی میانه (*singabēr) رسید، از آنجا به سریانی zangabīl و از سریانی به عربی «زنجبیل» رفت، و سپس صورت عربی دوباره به فارسی نو وام گرفته شد و جای «شنگبیل» بومی (گرهٔ ۲۲) را در کاربرد عادی گرفت. جفری این چرخه را صریحاً می‌نویسد: «و از آنجا در دورهٔ اسلامی دوباره به فارسی وام داده شد». معین نیز در «فرهنگ فارسی» سرواژه را با نشانِ [ع.] و گونه‌های «زنجفیل» و «جنزبیل» آورده است. پس «زنجبیل» و «شنگبیل» دو صورتِ دوگانهٔ یک واژه‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/زنجبيل\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1751\", \"status\": \"supports\", \"note\": \"MON_part1.txt line 71763: 'زنجبیل: [ع. زنجفیل - جنزبیل - زنجبیل] (ا.) (گیا.) گیاهی است پایا از تیرهٔ زنجبیل‌ها ...' — Moʿin marks it an Arabic loan with the variants زنجفیل، جنزبیل, and p. 1751 falls in the ز section of his lexicon.\"},\n            {\"ref\": \"VDQ:238\", \"status\": \"supports\", \"note\": \"for this node the reference does say what the arrow says: Jeffery (FVQ 154, of which VDQ is the translation) — 'There can be little doubt that the word passed into Arabic from Syr. and was thence borrowed back into Persian in Islamic times.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 153-154\", \"stance\": \"supports\", \"note\": \"see the quotation above; also 'ath-Thaʿālibī, Fiqh, 318, and al-Jawālīqī, Muʿarrab, 78, give it in their lists of Persian loan-words'.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. زنجبیل\", \"stance\": \"supports\", \"note\": \"'[ع. زنجفیل - جنزبیل - زنجبیل]'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"زنجبيل, Descendants\", \"stance\": \"supports\", \"note\": \"Persian زنجبیل is listed among the descendants of the Arabic word (alongside Hebrew, Amharic, Swahili tangawizi).\"}\n          ]\n        },\n        {\n          \"id\": 27,\n          \"lang\": \"Latin\",\n          \"words\": \"gingiber, zingiber, zinziber\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin zingiber(i) is a direct loan of Greek ζιγγίβερις in the medical and culinary literature of the early Empire (Pliny, NH xii.7, 'which some call Zimpiberi and others Zinigiberi'; Apicius; Celsus). In Late and Medieval Latin it developed the variants zinziber (with the regular Late-Latin assibilation of -g- before a front vowel) and gingiber (with dissimilation of the two z-/dz- sounds to g-), the last of which is the ancestor of the whole Romance and Germanic series. All three of Nourai's forms are attested.\",\n          \"derivation_fa\": \"لاتینیِ zingiber(i) وام مستقیمی است از ζιγγίβερις یونانی که در ادبیات پزشکی و آشپزیِ اوایل امپراتوری روم دیده می‌شود (پلینیوس، تاریخ طبیعی ۱۲٫۷: «آنچه برخی Zimpiberi و دیگران Zinigiberi می‌نامند»؛ آپیکیوس؛ کِلسوس). در لاتینی متأخر و قرون وسطایی گونه‌های zinziber (با سایشی‌شدن قاعده‌مندِ ‑g‑ پیش از واکهٔ پیشین) و gingiber (با ناهمگون‌سازی دو صامت z/dz به g) پدید آمد و همین صورت اخیر نیای کل زنجیرهٔ رومانس و ژرمنی است. هر سه صورتی که نورایی آورده گواهی شده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ginger\", \"https://en.wiktionary.org/wiki/ζιγγίβερις\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 657 s.v. ginger: 'fr. OF. gingibre, gingembre (F. gingembre), fr. L. gingiber, zingiber, fr. Gk. ζιγγίβερις'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. GINGER, Pliny quotation (xii.7)\", \"stance\": \"supports\", \"note\": \"'Many have taken Ginger (which some call Zimbiperi and others Zinigiberi) for the root of that tree ... A pound of Ginger is commonly sold at Rome for 6 deniers.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1930\", \"stance\": \"supports\", \"note\": \"'... sowie gr. Ζιγγίβερις, lat. zingiber und hieraus: it. zenzovero, zenzero, gengiovo, aprov. gingebre, frz. gingembre ...'\"},\n            {\"src\": \"Wiktionary\", \"where\": \"ζιγγίβερις, Descendants\", \"stance\": \"supports\", \"note\": \"'Latin zingiberi' listed as a borrowing from the Greek.\"}\n          ]\n        },\n        {\n          \"id\": 28,\n          \"lang\": \"Old French\",\n          \"words\": \"gingiber, gingiver\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The step Latin > Old French > English is correct, but the two forms in the box are not quite the Old French ones. Klein, whom Nourai cites, gives 'OF. gingibre, gingembre (F. gingembre)' for Old French and 'OE. gingiber' for Old English, with 'ME. gingevir, gingivere'; the attested Old French forms are gingibre / gingivre / gingembre, with the -bre/-vre cluster, not gingiber/gingiver. Nourai has apparently taken Klein's Old English gingiber and the Middle English gingivere and relabelled them Old French. The phonetics of the real chain: ML gingiber > OFr. gingibre with regular apocope of the Latin final vowel and epenthesis in the -br- cluster; the b then spirantised to v in part of the tradition (gingivre), whence Middle English gingivere.\",\n          \"derivation_fa\": \"حلقهٔ لاتینی > فرانسویِ کهن > انگلیسی درست است، اما دو صورتی که در کادر آمده دقیقاً صورت‌های فرانسویِ کهن نیستند. کلاین — که خودِ مأخذ نورایی است — برای فرانسویِ کهن gingibre و gingembre می‌آورد و gingiber را صورتِ انگلیسیِ کهن و gingevir/gingivere را صورت انگلیسیِ میانه می‌داند. صورت‌های گواهی‌شدهٔ فرانسویِ کهن gingibre/gingivre/gingembre‌اند با خوشهٔ ‑bre/‑vre، نه gingiber/gingiver. چنین می‌نماید که نورایی صورت انگلیسیِ کهن و میانهٔ کلاین را به فرانسویِ کهن نسبت داده است. آواشناسی زنجیرهٔ راستین: gingiber لاتینی میانه > gingibre فرانسویِ کهن با افتادن قاعده‌مندِ واکهٔ پایانی لاتینی و واکهٔ میانجی در خوشهٔ ‑br‑؛ سپس b در بخشی از سنّت به v سایشی شده (gingivre) و از آن gingivere انگلیسیِ میانه پدید آمده است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ginger\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:657\", \"status\": \"partial\", \"note\": \"Klein 1966 p. 657 s.v. ginger reads 'ME. gingevir, gingivere, fr. OE. gingiber, fr. OF. gingibre, gingembre (F. gingembre), fr. L. gingiber, zingiber' — the Old French forms are gingibre/gingembre; gingiber is Klein's OLD ENGLISH form, so Nourai's box mislabels it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1930\", \"stance\": \"partial\", \"note\": \"'aprov. gingebre, frz. gingembre, kat. gingebre, sp. gengibre, agengibre, pg. gengibre, gengivre' — the Romance forms all have the -bre/-vre cluster.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt found only 'gingerly' (a different word, from Swedish dial. gingla); the 'ginger' entry itself is missing from this OCR.\"}\n          ]\n        },\n        {\n          \"id\": 29,\n          \"lang\": \"English\",\n          \"words\": \"ginger, gingerale\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ginger is a double inheritance: Old English had already borrowed the Latin form as gingifer/gingiber, and Middle English gingivere, gingevir was reinforced by Anglo-French/Old French gingivre — the two merged into ME ginger. Ginger ale is a much later transparent compound of the 19th century (the drink, first commercialised in Ireland and North America in the 1850s-1860s), Nourai's 'gingerale' being simply the run-together spelling. AHD s.v. ginger (p. 667) gives the same chain back to Sanskrit; Watkins files GINGER under ker-1 through the Sanskrit 'horn' word.\",\n          \"derivation_fa\": \"«ginger» انگلیسی میراث دوگانه‌ای است: انگلیسیِ کهن پیش‌تر صورت لاتینی را به شکل gingifer/gingiber وام گرفته بود، و انگلیسیِ میانهٔ gingivere/gingevir با صورت انگلونورمان/فرانسویِ کهن gingivre تقویت شد و این دو در ginger انگلیسیِ میانه یکی شدند. «ginger ale» ترکیبی شفاف و بسیار متأخر است (این نوشابه در دههٔ ۱۸۵۰–۱۸۶۰ در ایرلند و آمریکای شمالی تجاری شد) و املای سرهم «gingerale» از آنِ نورایی است. فرهنگ American Heritage (ذیل ginger، ص ۶۶۷) همین زنجیره را تا سنسکریت می‌برد و واتکینز GINGER را از راه واژهٔ «شاخ» سنسکریت ذیل ker-1 می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/ginger\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:667\", \"status\": \"supports\", \"note\": \"AHD New College ed. p. 667 s.v. ginger: 'Middle English gingivere, from Old English gingifer and Old French gingivre, both from Medieval Latin gingiber, from Latin zingiber, from Greek zingiberis, from Pali siṅgivera, from Sanskrit śṛṅgavera'.\"},\n            {\"ref\": \"KLN:657\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 657: 'ginger, n. — ME. gingevir, gingivere, fr. OE. gingiber, fr. OF. gingibre, gingembre ...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1930\", \"stance\": \"supports\", \"note\": \"'... ndl. gember, engl. ginger, dtsch. Ingwer [mit Abwurf des Anlautes] ...'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. GINGER\", \"stance\": \"supports\", \"note\": \"'GINGER, s. The root of Zingiber officinale, Roxb. We get this word from the Arabic zanjabīl, Sp. agengibre (al-zanjabīl), Port. gingibre, Latin zingiber, Ital. zenzero, gengiovo, and many other old forms.'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-256.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-06T16:33:48.559Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T16:33:52.974Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/verify_check.py 256"
}
```


### [2026-09-06T16:33:55.310Z] TOOL RESULT

```
nodes verified: 29/29
node verdicts: {'confirmed': 21, 'disputed': 3, 'plausible': 4, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 22, 'not_checked': 9, 'partial': 6, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 49, 'silent': 8, 'contradicts': 7, 'partial': 9} | by book: {'Wiktionary': 11, 'LKT': 10, 'KLN': 8, 'HJB': 6, 'POK': 5, 'PHD': 5, 'AHD': 5, 'MON': 4, 'Etymonline': 3, 'FVQ': 3, 'BRT': 2, 'WLD': 2, 'ARY': 2, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'DEV': 1, 'PHN': 1, 'LEW': 1, 'SKT': 1}
```


## [2026-09-06T16:34:17.021Z] AGENT

Page 256 (book p. 226) verified — `data/verification/page-256.json`; `verify_check.py 256` reports 29/29 nodes, 0 PROBLEM lines.

**Verdicts:** root confirmed (1). Nodes: 21 confirmed, 4 plausible, 3 disputed, 1 transcription_suspect.

**Disputed / flagged**
- **#3 Persian box — ساربان**: not from *sar* "head"; it is Parthian *sārt* / Sogdian *sʾrth* "caravan" + ‑بان (Wiktionary; Horn has no sar-etymology). The other six words (سر، افسر، افسار، سردار، سالار، سرشار) check out — Horn nos. 99 and 692 confirm افسر and سالار.
- **#19 English "cheek"**: `transcription_suspect`, `error_in: book`. Watkins/AHD lists **CHEER** under *ker-1* (Gk. *kara* → LL *cara* → OFr *chiere*); cheek is OE *ċēce* < PGmc *\*kēkǭ*, unrelated. The printed page (checked at 600 dpi, PNG saved to `data/verification/sources/refs/ocr/BOOK/256.png`) really prints "cheek" — Nourai's misprint, not an extraction error.
- **#20 Sanskrit śṛṅgavera**: not śṛṅga "horn" + vera "body". It is a Sanskritism of Prakrit *siṃgivera* < Old Tamil *iñci-vēr* "ginger root"; the "horn" analysis is folk etymology (Hobson-Jobson 374–375 already said so). Nourai follows Klein/AHD here. (śṛṅga "horn" itself is fine, Pokorny 575.)
- **#25 Arabic zanzabîl**: two problems. The Arabic is **زنجبيل zanjabīl** — the book prints "zanzabîl" (book misprint, extraction faithful). And the arrow Greek → Arabic contradicts Nourai's own reference: Jeffery FVQ 153–154 (= VDQ) derives Syriac *zangabīl* from Pahlavi *singaβēr* and treats Greek ζιγγίβερις as a sister branch; Wiktionary and Lokotsch agree.

**Plausible (with reasons in the file):** #4 (Bartholomae glosses Av. srū-/srvā- "nail, horn", not "head"; srvara- = "horned", not "carried on the head"), #21 ("singiber" is the Latin form, not Pahlavi), #24 (Beekes: Greek via an unattested Middle Iranian relay, not straight from Pali), #28 (Klein's "gingiber" is Old *English*; the OFr forms are gingibre/gingivre).

**Extraction error for the owner to fix**
- Node 3 (`page-256.json` source): the printed Persian box has **seven** words — سر ، افسر ، **افسار** ، ساربان ، سردار ، سالار ، سرشار. `script_extra` in `data/extracted/batch/page-256.json` omits **افسار**.

Reference checks: 22 supports, 6 partial, 1 contradicts (VDQ:238), 1 not_found (MON:1751 for شنگبیل — Moʿin's OCR has no such headword; 1751 is the زنجبیل page), 9 not_checked (mostly refs-less nodes; LEW:905 unverifiable — only the Walde-Hofmann Registerband is on disk, and it places Av. srū/srvara at Bd. I 208). BQT:1130 does support #5: Borhān vol. 2 leaf 596 carries سَرون with the exact Nezāmī verse Nourai quotes, though at printed p. ≈1139 in this scan.
