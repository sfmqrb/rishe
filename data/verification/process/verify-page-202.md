# Verification process log — verify-page-202


## [2026-09-06T02:17:39.917Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 202 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-202.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-202.json. Write /home/sfmqrb/git/rishe/data/verification/page-202.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 202` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:17:41.558Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:17:42.225Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:17:42.241Z] TOOL RESULT

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


## [2026-09-06T02:17:42.486Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-202.txt"
}
```


### [2026-09-06T02:17:42.506Z] TOOL RESULT

```
1	=== PDF page 202 (book page 172) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwa, Gwâ, Gwen 2 : to walk, to step, to come, to go  (refs POK:463)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:463; KLN:318 | gam : to come, step ; jam, jantu : to go
5	#2 (parent #0) [Avestan] refs=POK:463 | gâman : step ; a-gam : to come ☞Apo ; ni-gama : come down (in sheath) ☞Nî ; paiti-gama : come forth (with a message) ☞Per 3
6	  #3 (parent #2) [Persian] refs=HRN:11; BQT:434,1765,2223; SPG:217 | gâm «گام» : step ; âmadan «آمدن ( آینده )» : to come ; nîyâm «نیام» : sheath ; payâm «پیام ( پیامبر ، پیغام ، پیغمبر )» : message
7	#4 (parent #0) [Avestan] refs=BQT:166,1451 | fra-jâma : gone forward (to a destination) ☞Per 1 ; han-jâma : conclusion ☞Sem 1 ; han-jâmana : coming together ☞Sem 1
8	  #5 (parent #4) [Persian] refs=ETM; FFD | farjâm «فرجام ( فرجامیدن )» : end ; anjâm «انجام ( انجامیدن )» : conclusion ; anjoman «انجمن» : society, meeting
9	#6 (parent #0) [Avestan / Old Persian] refs=POK:463; KNT:183 | gât, gâthu, gâv, gâtuš : place, seat, throne ; gâtu-bar : (baby) carriage ☞Bher 1
10	  #7 (parent #6) [Persian] refs=BQT:1771,1773 | gâh 2 «گاه ۲» : place, position, rank | extra: دانشگاه ، خانگاه ، خانقاه ، گهواره
11	  #8 (parent #6) [Arabic] refs=FVF:144 | jâh : rank
12	    #9 (parent #8) [Persian] refs=MON | jâh «جاه» : position
13	#10 (parent #0) [Old Persian] refs=BQT:2368; KNT:212 | ham-gmatana, hangmatâna : (a place for) coming together ☞Sem 1
14	  #11 (parent #10) [Persian] refs=BQT:2368 | Ekbâtân «اکباتان (همدان)»
15	#12 (parent #0) [Avestan / Old Persian] refs=PLA:146; NYB:228; SBK:203 | jamâna : a step (period) of time ; thamân : time
16	  #13 (parent #12) [Persian] refs=MON:1746 | zamân «زمان» : time
17	  #14 (parent #12) [Arabic] refs=PLA:146; NYB:228 | zamân : time | NOTE: KLN:951 derives this from Akkadian "Simânu: appointed time".  NYB:228 claims they are ultimately from Old Persian "jamâna:time".
18	    #15 (parent #14) [Persian] refs=MON:1746 | mozmen «مزمن» : old ; azmaneh «ازمنه» : times
19	#16 (parent #0) [Avestan / Old Persian] refs=BQT:2383 | gâma : a step (period) of time ; han-gâma : at the same time, during ☞Sem 1
20	  #17 (parent #16) [Persian] refs=BQT:2383 | hengâm «هنگام» : during | extra: ناهنگام ، شب هنگام
21	
```


## [2026-09-06T02:17:45.957Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-202.json",
 "description": "Read source JSON for page 202"
}
```


### [2026-09-06T02:17:45.998Z] TOOL RESULT

```
{
  "pdf_page": 202,
  "book_page": 172,
  "entries": [
    {
      "root": {
        "name": "Gwa, Gwâ, Gwen 2",
        "lang": "Indo-European",
        "refs": "POK:463",
        "gloss": "to walk, to step, to come, to go"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:463; KLN:318",
          "words": [
            {"translit": "gam", "gloss": "to come, step", "script": null},
            {"translit": "jam, jantu", "gloss": "to go", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:463",
          "words": [
            {"translit": "gâman", "gloss": "step", "script": null},
            {"translit": "a-gam", "gloss": "to come", "script": null, "see": ["Apo"]},
            {"translit": "ni-gama", "gloss": "come down (in sheath)", "script": null, "see": ["Nî"]},
            {"translit": "paiti-gama", "gloss": "come forth (with a message)", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:11; BQT:434,1765,2223; SPG:217",
          "words": [
            {"translit": "gâm", "gloss": "step", "script": "گام"},
            {"translit": "âmadan", "gloss": "to come", "script": "آمدن ( آینده )"},
            {"translit": "nîyâm", "gloss": "sheath", "script": "نیام"},
            {"translit": "payâm", "gloss": "message", "script": "پیام ( پیامبر ، پیغام ، پیغمبر )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گفت مرا دولت نو : راه مرو رنجه مشو - زانک من ازلطف و کرم سوی توآینده شدم",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:166,1451",
          "words": [
            {"translit": "fra-jâma", "gloss": "gone forward (to a destination)", "script": null, "see": ["Per 1"]},
            {"translit": "han-jâma", "gloss": "conclusion", "script": null, "see": ["Sem 1"]},
            {"translit": "han-jâmana", "gloss": "coming together", "script": null, "see": ["Sem 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "ETM; FFD",
          "words": [
            {"translit": "farjâm", "gloss": "end", "script": "فرجام ( فرجامیدن )"},
            {"translit": "anjâm", "gloss": "conclusion", "script": "انجام ( انجامیدن )"},
            {"translit": "anjoman", "gloss": "society, meeting", "script": "انجمن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:463; KNT:183",
          "words": [
            {"translit": "gât, gâthu, gâv, gâtuš", "gloss": "place, seat, throne", "script": null},
            {"translit": "gâtu-bar", "gloss": "(baby) carriage", "script": null, "see": ["Bher 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1771,1773",
          "words": [
            {"translit": "gâh 2", "gloss": "place, position, rank", "script": "گاه ۲"}
          ],
          "script_extra": "دانشگاه ، خانگاه ، خانقاه ، گهواره",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Arabic",
          "refs": "FVF:144",
          "words": [
            {"translit": "jâh", "gloss": "rank", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "jâh", "gloss": "position", "script": "جاه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:2368; KNT:212",
          "words": [
            {"translit": "ham-gmatana, hangmatâna", "gloss": "(a place for) coming together", "script": null, "see": ["Sem 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "BQT:2368",
          "words": [
            {"translit": "Ekbâtân", "gloss": null, "script": "اکباتان (همدان)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "PLA:146; NYB:228; SBK:203",
          "words": [
            {"translit": "jamâna", "gloss": "a step (period) of time", "script": null},
            {"translit": "thamân", "gloss": "time", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:1746",
          "words": [
            {"translit": "zamân", "gloss": "time", "script": "زمان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "همی خواهم از روشن کردگار - که چندان زمان یابم از روزگار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "Arabic",
          "refs": "PLA:146; NYB:228",
          "words": [
            {"translit": "zamân", "gloss": "time", "script": null}
          ],
          "script_extra": null,
          "note": "KLN:951 derives this from Akkadian \"Simânu: appointed time\".  NYB:228 claims they are ultimately from Old Persian \"jamâna:time\".",
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "MON:1746",
          "words": [
            {"translit": "mozmen", "gloss": "old", "script": "مزمن"},
            {"translit": "azmaneh", "gloss": "times", "script": "ازمنه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:2383",
          "words": [
            {"translit": "gâma", "gloss": "a step (period) of time", "script": null},
            {"translit": "han-gâma", "gloss": "at the same time, during", "script": null, "see": ["Sem 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "BQT:2383",
          "words": [
            {"translit": "hengâm", "gloss": "during", "script": "هنگام"}
          ],
          "script_extra": "ناهنگام ، شب هنگام",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T02:17:46.412Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:17:46.478Z] TOOL RESULT

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


## [2026-09-06T02:18:01.781Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','KNT','BQT','MON','HRN','SPG','ETM','FFD','FVF','FVQ','PLA','NYB','SBK','BRT','PHD','HUB','ARY','AFM']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


## [2026-09-06T02:18:02.217Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-06T02:18:03.441Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SPG {"title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)", "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)", "kind": "archive_djvu", "url": "https://archive.org/details/diealtpersische00spiegoog", "identifier": "diealtpersische00spiegoog (Eranische Alterthumskunde: in.gov.ignca.11987 vol.1, in.ernet.dli.2015.529286 vol.2, in.ernet.dli.2015.103474 vol.3)", "local_file": "/home/sf

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

SBK {"title": "M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942", "kind": "archive_djvu", "url": "https://archive.org/details/1_20250928_20250928_1159 (3 vols; vol 1 = سبک شناسی_1)", "lookup_hint": "grep in SBK.txt (raw djvu, no page breaks); use inside.php with doc='سبک شناسی_1'. Later printings keep the 1st-edition pagination approximately; verify.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt"], "page_offset": null, "covers_etymology": false, "notes": "Persian OCR fair. galaxy_ub2007_yahoo_20151117 is another (tiny-OCR) copy."}

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
```


### [2026-09-06T02:18:05.227Z] TOOL RESULT

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
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
   "stance": "silent",
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
```


## [2026-09-06T02:18:11.191Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==119' POK_02.txt | head -80",
 "description": "Print Pokorny page 463"
}
```


## [2026-09-06T02:18:12.404Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gʷā-\\|gṷā-\\|gwā-\\|guā-\" POK_02.txt | head -30",
 "description": "Grep Pokorny for the root"
}
```


### [2026-09-06T02:18:12.734Z] TOOL RESULT

```
%^ot^w  ,die  Oberfläche  eines  Körpers  berühren  oder  bestreichen, färben,  beflecken',  x^w^ta,  -arog  ,Haut,  Hautfarbe,  Farbe,  Schminke',  x^ota,  .^M att.  xQOCi  , Körperoberfläche,  Haut,  Farbe'  (*x^w/-jtß) ;  "
gall.  *grava  ,Kies^,  cymr.  grOj  acorn.  groUj  mcorn.  groiv  ,Sand^,  mbret. grouanenn  ds.,  nbret.  gro{a)  f.  , Sandstrand*,  groan,  grouan  ,gravier'  (Voka- lismus unklar) ;
aisl.  grjön  n.  , Grütze  (*geschrotetes  Korn)',  mhd.  grien  m.  n.  ^Kiessand; sandiges  Ufer',  mnd.  gren  , Sandkorn*  (*ghreuno-]  auch  norw.  isl.  grugg n.  ^Bodensatz*  aus  *gruwwa-  als  ,sandartiger  Rückstand*).
Da  die  erweiterte  Wz.  ghreu-d-  mehrfach  auf  das  seelische  Gebiet  ange- wendet ist  (,im  Gemüte  hart  berühren*),  vermutet  man  auch  Zugehörig- keit von   ahd.  ingrüen,    mhd.   grüen,   grüiven   , schaudern,    fürchten',   mhd.
461
griul,  griuioel  ;Schrecken,  Greuel',  ahd.  grüsön,  grüwisön  , Schrecken empfinden',  nhd.  ,grauSj  grausen^  usw.,  ahd.  grunuy  -nnes  ,Jammer,  Elend', griuna  , Begierde,  Heftigkeit,  Grausamkeit'  u.  dgl.
Erweiterung-  ghreu-d-:
ahd.  *ßrgriozan  ,zerreiben*,  Partiz.  ßrgrozzen,  mhd.  ver-j  dnrcli-griezen ^in  kleine  Teile  zerreiben';  aisl.  grjöt  n.  (a-St.)  , Stein,  Grieß',  ags.  greot n.  ,Sand,  Staub,  Erde',  as.  griot  n.  ,Sand,  Ufer',  ahd.  griozj  mhd.  griez  m., n.  , Sandkorn,  Sand,  Ufergrieß',  nhd.  , Grieß'  (germ.  *greuta-  , Gestein, Sand,  Kies'  auch  in  VN  Greutungi  , Strandbewohner'  und  in  finn.  riutta , Sandbank,  Klippe');
aisl.  grautr  m.  , Grütze'  (,grohgemahlenes') ;  ags.  great  ,grobkörnig, groß,  dick'  (engl,  great),  afries.  grät,  as.  gröt,  ahd.  mhd.  gröz  ,groß',  mhd. auch  ,grob,  dick'  (germ.  *grauta-)  ;   über  aisl.  grotti  , Mühle'  s.  unter  gliren- ;
ags.  grytt  , Grütze'  (engl,  grits  ,ds.,  grober  Sand'),  ahd.  gruzzi,  mnd. griltte  , Grütze'  (germ.  *grut{a-)]  ags.  grüt  (Dat.  gryt)  t  ,grobes  Mehl, Treber',  afries.  gret  ,Sand',  mhd.  grüz  m.  ,Sand,  Getreidekorn',  nhd. Graus  , Sandkorn,  Schutt,  Geröll',  mnd.  grüt  ,Porsch  als  Gärungsmittel', ndl.  gruit  ,Malz,  Hefe,  Bodensatz',  norw.  grüt  n.  ,Bodensatz';  ags.  grot n.  , grobes  Mehl'  (germ.  *gruta-)  •
mit  Formans  -to-  oder  -so-:  mnd.  grüs,  gros  , zerbröckelte  Steine,  Kies';
bsl.  *grüdiö  , stampfe'  in  lit.  grudziu  oder  grüdau,  grüsti  , stampfen  (Gerste zur  Graupenbere
```


### [2026-09-06T02:18:12.827Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:18:19.735Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gehen,  kommen\\|gehen, kommen\" POK_02.txt | head -20; echo ---; grep -n \"gᵘ̯ā\\|g^ā-\\|gṷem\\|g^em\" POK_02.txt | head",
 "description": "Search Pokorny for gehen kommen"
}
```


### [2026-09-06T02:18:19.834Z] TOOL RESULT

```
1790:g^a.',  g"em-  ^gehen,  kommen;  zur  Welt  kommen^  geboren  werden^;  g^tp-ti-s i.,  g^em-tu-s  m.  ,Gang,  Schritt'^  Verbaladjektiv  g^m-to-s. I.  g^ä-:
2063:vorliegt  (Pedersen  IF.  5,  47 ;  vielleicht  als  ""ged-s-os  zum  allerdings  nag Herten  lit.  gaüdinu-,  -inti  ^schrecken^,  üsi-gq,stü,  -gandaü  'gq.sti  ,erschreckei intrans/,  Ugqstis  .Schrecken',  Scheftelowitz  IF.  33,  155).  Ob  hierher  kelj Häs-  .sterben'?  (s.  unter  g'^em-,  g'^ä-  .gehen,  kommen');
6090:Vielleicht  ai.  mani-  ,Perle',  manika-  m.  »(runder)  Wassertopf';  gr.  (xoXetv , gehen,  kommen'  (Aor.),  Präs.  ßlojaxu),  Perf.  (xs^ßXü}v,a]  eßXo)'  i(pdvr]' aüT6-(.ioXoq  , Überläufer',  TtQO-fioXrj  , Auslauf  eines  Berges,  Flusses',  ^oXsvo) »beschneide  die  Pflanzenschößlinge' ;
---
```


## [2026-09-06T02:18:20.446Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gam-\\|gátu\\|gātu\" POK_full.txt | head -20; echo ===; grep -n \"463\" POK_full.txt | head -5",
 "description": "Search POK_full"
}
```


### [2026-09-06T02:18:20.508Z] TOOL RESULT

```
Exit code 1
26674:PI. " men, people', also in verbal prefix Aryan ni- "in, into', e.g. Old Indie nfgam-, Avestan 
26675:n/gam-^enter into a condition'; 
29081:Material: Old Indie a, Avestan Old pers. 5" in, to there ', e.g. a-gam-^ near to, draw near, 
38456:Konj. *g"'emet/"\n Old \nd'\c gam-at, -anti, Ga\ha-/Kves\.av\ Jama'ti, jima'tr, Opt. g"'m-/et\n 
(eval):1: == not found
```


## [2026-09-06T02:18:23.670Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1782,1830p' POK_02.txt",
 "description": "Print Pokorny gwa entry"
}
```


### [2026-09-06T02:18:23.742Z] TOOL RESULT

```
poln.  gruz  , Schutt^  MörteP,  PI.  ^Trümmer,  Ruinen^,  klr.  kru£  ^Trümmer' PI.    ,Schutt'    (schwerlich    aus    mhd.    grüs    ,Graus^    wegen:)    poln.    grnzla  " ,KlumpenS  osorb.  hruzia  , Erdkloß,  Klumpen,  Scholle^  *  "  ^
Erweiterung  gJireu-hh-i
vermutlich  in  den  germ.  Gruppen  von  nhd.  Griebe  (ahd.  griuho,  gnoho)] Griehsj  vielleicht  auch  groh ;  vgl.  mit  germ.  p,  norw.  mdartl.  grüpa^  graun^ ,groh  mahlen,  schroten',  g'fojpaj  grypja  ds.,  gro'p  n.  ^geschrotetes  KoriLi grobes  Mehl'.
WP.  I  648  ff.;  Trautmann  99.
ghroud-  von  gewölbten  Körperteilen;  nur  kelt.  und  germ.
Air.  grüad  (n.  es-St.)  , Wange',   cymr.  grudd  ds.,   corn.   grud  ,maxilla'« ags.  greada  m.  ,Busen'. WP.  I  658.
Gu,  Gu  und  GS.
5^5
g^a.',  g"em-  ^gehen,  kommen;  zur  Welt  kommen^  geboren  werden^;  g^tp-ti-s i.,  g^em-tu-s  m.  ,Gang,  Schritt'^  Verbaladjektiv  g^m-to-s. I.  g^ä-:
Ai.  ß-gä-ti  ;geht^  (=  gr.  *ßLßrjGi,  vgl.  lak.  3.  Sg.  ßlßavxi,  hom.  Partiz. ^£/?(fg  ,mit  großen  Schritten  einhergehend*^^  dazu  auch  hom.  ßißaad-oyv), Aor.  d-gä-m  ^ich  kam  hin,  ging  weg^  (av.  Inj  unkt,  gät  ,er  wird  hin- kommen^) =  arm.  kam  ^stehe^,  gr.  eßr]Vy  dor.  sßßv  ,ich  machte  mich  auf,
'S';
ai.  gätram  ,Glied,  Körper^;  gätü-h  ,Gang,  Weg,  Raum,  Orf^,  av.  gätu-s ,Ort,  Liegerstatt,  Sessel,  Thron^,  apers.  ^äi^w  ds. ;  ai.  vi-gäman-  n.  ,Schritt^ (^prthü-pra-gäman-  ,weiterschreitend^ ;  vgl.  gämin-  ,gehend^,  Weiterbildung eines  o-St.  gäma-h)^  av.  gä-man-  n.  ,Schritt^,  ai.  gäya-m  ,Schritt^  in  iiru-gäyd- ,weiterschreitend,  weit'  (vom  Weg),  av.  gäya-  (Akk.  gäim)  ,Schritt'  (mit Formans  -ya-);
arm.  kam  ,stehe^  ( :  gr.  eßrjv)  ;
gr.  *ßlßr]GLj  ßißdg,  kßrjv  s.  oben;  ßrjzaQfiög  ,Tanz'^,  ßr]raQ{.i(Dv  ,Tänzer*^ (aus  *ßäTog  oder  *ßacä  ,das  Fußaufsetzen^  -]-^'?.""  ,Gefüge^);  äi.LcpLGßrjiiw,  ion. a(.iq)L(TßäT€(jü  ,streite'  (,nach  zwei  Seiten  auseinandergehend^),  ßfj!,ia  n.  ,Schritt^ ablautend  ßioixög  m.  ,Tritt,  Stufe,  Gestell,  Altar^;  Infinitiv  ßrjf,ievaL]  ßrjXög m.  ,Türschwelle^;  ßsßr^log,  dor.  ßeßaXog,  kyren.  ßdßctXog  ,betretbar,  un- geweiht^  (Gegensatz  von  icßarog  ,unvergänglich,  heilig^;  tiefstufig  ßeßaiog ,sicher^  (*gut  gangbar) ;  ßdörjv  Adv.  ,im  Schritt^ ;  ßdöog  m.  ,Weg',  ßa&^ög m.  , Stufe,  Schwelle,  Schritt^,  ßdd^qov  ,Grundlage'^,  ifj,ßdTr]g  ,Männerschuh'^ ;
alb.  ngä  ,ich  laufe'  (*ga-niö)]
lit.  dial.  göti  ,gehen';  lett.  gäj^i  (Prät.  zu  iet)  ,ich  ging'  (setzt  ein  Präs. ^gäiö  voraus,  dessen  j  präsensbildend  sein  wird),  davon  weiter  gäjums ,Gang,  Reihe';  gäita  ,Gang'  (mit  analogischem  ai,  Endzelin  Lett.  Gr. S.  678);  gätis  PL  ,Fluglöcher  der  Bienen';  lit.  pröga  ,Gelegenheit,  Frist' (Präfix  *prai  -\-  gä) ;  lit.  gätve  ,Straße,  Viehtrift',  lett.  gatva  ,Weg,  Durch-
gang' sind  germ.  Lw.
Vielleicht  hierher  auch  die  kelt.  Worte  für  ,sterben'  (als  , fortgehen', ix  ßqoTvbv  ßfjvat),  wie  air.  bald  ,stirbt'  (*bä-a-ti  aus  *g^ä-)j  at-bath  ,starb' {*-gud-t  .  .),  bath  ,Tod'  =  cymr.  bad  ,Pest',  bret.  bad  ,Betäubung',  corn. bad-us  ,wahnsinnig';  air.  bäs  ,Tod'  ist  nach  gnäs  ,Gewohnheit'  usw.  gebildet.
464
Trotz  Thurneysen  Gr.  §§  547,  728  ist  ein  Stamm  hus-  nicht  nachzuweisenj  |^ s.  richtiger  Pedersen  Litteris  2,  89  f.  -^^'
2.  g'iem-'.  ^:},'
Unthematisch  *{e)-gi}em-t  (>  *e-guen-t),  -gMm-te,  -gnm-ent  im  ai.  Aor.  dgan,  '-  ■ gan  (g  für  j  nach  Formen  mit  ursprünglichem  *g^7ri-,  *gum-'^  1.  Sg.  dgamam\ dgata   {*g'^m-),  dgman,   dgmata]    gthav.    3.  Sg.   Inj.   uz-J9n,   3.  PI.   ^»T/ian;
arm.  3.  Sg.  ekn  ,er  kam'  (=  ai.  dgan)-,  über  die  noch  unklare  1.  Sg.  eki, 3.  PI.  ekin  siehe  Meillet  Esquisse  134  f.;
gr.  ßdTTjv  3.  Du.,  vnsQßäaav  3.  PL  wohl  zur  Wurzelf.  *^?^ä-;
Konj.  *gi^emeti  in  ai.  gdm-at,  -anti,  gthav.  jamaHi,  jimaHi]  Opt.  gurji. jet  in  ai.  gamyät,  av.  jamyät,  ap.  jawjä''  {J  für  g  aus  Formen  mit  hoch- stufigem idg.  *guem-) ;  ags.  cyme  s.  unten ;
thematisch:  hochstufig  ai.  gdmati,  av.  jamaiti  ,geht'  (ai.  gamdyati ,läßt  kommen,  führt  herbei^  av.  jämayeiti  ^briogt  zum  Weichen'),  tiefstufig; ai.  (Opt.  Aor.)  gamit,  gamimay  gamemahi,  wohl  auch  Aor.  dgamat]  PerL^ ja-gdma  ,ich  ging'  (vgl.  got.  1.  PL  qemum);  av.  frä-ymat  (gthav.  -g'maQ] ,er  kam  hinzu',  apers.  a-gmatä-,
osk.  kümhened  ,convenit',  cebnust  (aus  *ce-henust)  ,(huc)  venerit',  umbrj &ewws<,  benurent  ,venerit,  -int';  lat.  Konj.  advenam  (über  n  für  w  s.  unten;* vielleicht  mit  analogischem  -en-  nach  den  Formen  wie  lat.  veniöj  ventumy venl) ;
got.  qiman  (Prät.  qam,  1.  PL  qemum:  ai.  1.  Sg.  Perf.  ja-gäma),  ahdj queman  und  (tiefstufig?)  coman  =  ags.  cuman,  anord.  Äöma  ,kommen^\ ags.  Konj.  Präter.  (alter  Optat.)  c2/we  {^gu^m-l-t)]
toch.  A  kam-,  kum-,  B  kam-,  kam-,  sem  ,kommen'.
io-Präsens  *gum-{ö  in  gr.  ßaivo)  .gehe'  (Fut.  ßrjooixai  usw.),  lat.  veni^ ,komme'  mit  sehr  altem  Wandel  von  -mi-  zu  -ni- ;  nach  Schwyzer  Gr.  Gr.  I, 309  könnte  das  n  auch  von  Formen  wie  av.  jantu  (*g^em-tu-),  arm.  ekn (*e-guem-t)  bezogen  sein;  zu  venimus  stimmt  got.  qemum-,
sAro-Präsens  * gurri-skö  :  2Ä.  gdcchati,  SLV.jasaiti  ,er  geht',  gr.  ßäoTis  ^ehl komm!'  toch.  A  kumnäs  ,er  kommt',  Med.  kumnästär,  B  känmasträ.
Verbaladjektiv:  ai.  gatd-h  ,gegangen',  av.  gata-  ds.,  gr.  ßazög  ,gangbar' {*gum-to-s),  lat.  in-ventus.
Andere  Nominalbildungen:
ai.  gdti-}^  f.  ,GaDg',  av.  aiwi-gati-  ,das  Herbeikommen  =  Eintreten, Beginnen',  gr.  ßäoig  f.  ,Schritt;  Grundlage'  (*gum-ti-s),  lat.  con-venti-ö ,Zusammenkunft',  got.  gaqum^s  ,Zusammenkunft'  {*-gifm-tis),  anord.  saTH- kund  f.  ds.,  ahd.  cumft,  nhd.  Ankunft ;  ai.  gdntu-h  m.  ,Gang,  Weg',  lat.  i adventus,  -üs  ,Ankunft';  got.  qums  ,Ankunft'  (*gi^e'^-is),  ags.  cyme^  ahd. cumi'j   •&[.  gamya-  ,wohin  man  gehen   kann  oder  soll',  osk.  kümbennieis
465
Ten.   conventüs^ ;  ahd.  biquämi  ^bequem^  (vgl.  ^bekömmlich^)^  ags.  gecweme
no-enehni;  passend^^  anord.  hvcemr  ^zum  Kommen  berechtigt  oder  im- tinde^;  kväma  f.  ,Kommen^  Besuch^^  köma  ds. ;
toch.  A  kzim-j  AB  kam-j  A  kam-,  B  sem-  ^kommen^;,  A  kumnds,  Med. htiinndstdr  ^kommt^,  A  kakmu,  B  kekamu  ,gekommen^
^lit  einer  Bed. -Entwicklung  ,{2,mv  Welt)  kommen^  =  _,geboren  werden^:
av.  ni-jämayeinti  _,sie  bringen  zum  Gebären^  (*ni-jäma-  ^GeburtQ;
crr.  i'ßäS-r]'  iysvvsd-r]  Hes. ;
alban.  pre-gjim  ^Gastmahl  bei  der  Erstgeburt^;
lit.  gemü,  gimti  ^geboren  werden^  =  lett.  dzemu,  dzimt  ds.,  lit.  glmstu (zum  Akzent  siehe  Schulze  KZ.  45,  230)  =  lett.  dzwistu  ds.,  lit.  gimine Familiö^  gymis  ^Geburt^,  gämas  ^Angeborenes^,  Kausat.  gammti  ^Kinder erzeugen,  Vieh  züchten^,  lett.  dzimts  ^angeboren,  erbgehörig,  leibeigen^, Jzlmsa  ,Geburt'  =  apr.  gimsenin  Akk.  Sg.  ,Geburt^,  apr.  gemton  ,gebären^, qemmons  Partiz.  Perf.  ,geboren^
WP.  I  675ff.,  MeiUet  Esquisse^  134f.,  Schwyzer  Gr.  Gr.  I  309,  689, 742»,  7072,  Trautmann  76,   Pedersen  Toch.  170  ff.,  221,  234.
&^Udh-  ,eintauchen,  untersinkend
Ai.  gdhate  ,taucht,  dringt  ein^,  Partiz.  gädka-h  ,tief,  stark,  fest^,  gähd-h ,Tiefe,  das  Innere^;  mit  a:  gähana-,  gdhvara-  ,tief,  dicht^,  n.  ,Tiefe,  Ab- o-rund, Dickicht^,  dur-gdha-m  ,böser  Ort  oder  Weg^ ;
das  Partiz.  gädhd-  ist  wohl  Analogiebildung  nach  Wurzeln  mit  ai.  k  = idg.  gh]  gädhd-  ,seicht^,  m.  n.  ,Un tiefe,  Furt^  ist  vielleicht  aus  einem  ai. Wurzelnomen  gä  (zu  idg.  g^ä-  ,Gang^)  +  ^^^  ^Is  ,(Über)gang  gewährend^ zu  erklären;
av.  Akk.  PI.  vi-gä&ö  ,Schluchten^  (:  ai.  vi-gähd-)  ,sich  eintauchend^, schwundstufig  guda-  ,Tiefe^;
gr.  ßfjoaa,  dor.  ßäoaa  {*ßad-ia)  f.  ,Talgrund,  Schlucht^;  ßaooog  n.  ds. {*ßad-oog),  schwundstufig  ßvd-ög,  ßvoaög  , Tiefe,  Meeresgrund^  mit  ß  statt  y nach  ßfjaaa;  Ußvoaog  ,wo  sich  nicht  tauchen  läßt,  grundlos,  Tiefe^,  ßdd-og n."  ,Tiefe^;  ßev&og  ,Tiefe^  sekundär  nach  Ttevd-og  :  TiaS^og]
```


## [2026-09-06T02:18:37.770Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT gātu ===\"; grep -n \"gātu\\|gatu-\\|gätu\" BRT.txt | head -20; echo \"=== BRT gāman ===\"; grep -n \"gāman\\|gäman\\|gaman-\" BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T02:18:37.847Z] TOOL RESULT

```
=== BRT gātu ===
4651:V.  p.  g;  — yahmya  staritasca  gätuS  'nyas^a  yat,  ISn.  'nya  als  Adv. :  sbes.  Vgl,  ferner (NPf.)  ..    avarf/ä    Yt/j.  7;  V.  5.39,  ig.   'anya.
5342:•  j.  arä^av-  m.  Name  des  vor  dem Zaotar  stehenden  Steintisches,  der  den Morser  und  andre  Opfei^eräte  trägt*': jautorj  (sd.)  däitys  gätui . .  mat?mäi  °raet apa-sritd  N.jS.
7136:[  da^at  . .  '"krasca  . .  paitHarat  N.  ■j4;  — j  iävanänS  (sd.)  dilityS  gätus  fralarqn  barts- ,  mqn  aparqm  ''i<ri)  N.79;  79 ; — '"ai^a  yff  dim *frähincin  (sd.)  *antarp  'tartmca  barsmaca \  ". .  zwischen  dem  Feuer  und  dem  B.  (an ■  der  Opferstätte)"  N.  08''\  c)  GS.  mit I  ta/nav-  m.  Flur.  'Feuergluten'  sva.  'Fieber- lanfälle':  kö pagiryS..'%rS  tafnus  därayat tanaot  haca    masyehe  V.  20.  i.  d)    Es
7296:•  j.  äbint-  m.  Bezeichnung  des  vierten Unterpriesters  (ratav),  der  das  beim Gottesdienst  nötige  Wasser  zu  bringen hat:  iiprn  'hns  (NS.)  äbarät  "der  Ab. soll  das  Wasser  herzutragen"  N.  77;  — 'Um  asiäya  Vr.^.i;  G.^.5,  F.j;^/ra- hr»>revä  'te  i'-i  V.5,57;  58;  —  -ts  (GS.) Vyt/j;  —  Du,  mit  sraosävars-.-  Du.: *'anaiwiarjtvs.gätu  (sd.)  aäa  'ta  (ND,) *sraoIävar?za  vlcarayat?m  N.  75.
13223:der  Gerichtssprache  '(einen  Termin)  an- sagen (lassen),  mitteilen':  yö  *pir>n3mtMi nöit  paiti jia'iiliti  gätumca  *varasca  (sd.) F.  40***.  Wertlos:  nizdasca  narS  dar>/f nm  paiti  dyaiti  Vd.  2.
15163:mit  ham  'sich  einstellen  bei  -'  (Akk.): vay5  . .  niUmaiSva  (sd.)  gätuh)a  . .  harn
16342:.von  Staub"  V.p.  31;  —  yat  aZsa  (nämL daxmö)  'nu  raf^wäl  (sd.)  V.  7.  50;  — hiku  'nu  (NS.)  gätu  nilayaSa  "trockener
16803:1.  7  (wo  abari'tä);  —  inanä  t^ure^maxda  113.  8)  'reiten',  Akt  und  Med.'*>; upasiatn  baratuv  D.^j;  —  i^ure^masda-  a.)  absolut:  taünef  .  .  bartntö  (NP.)  «ä"? maiy  ufastam(Stvaz.)  aiara^Sh.i.9usv.;i  ^asiamianti  vasMtd  .  ,  Yt.  10.  20;  — — yaha  ml  barm  upasiam  Yt  13.  t;  5. 63; —  barimnö  vä  vazfituUS  vä  N.  ^',  — hä  mihara  aamala..iA.lOS;  —  kaxatfrfm  kvaipäi  naire  bargmnäi  Y.  65.  4;  — tl  .  .  taoiranam  bar3m  Yt5.63;  — yeä  'baräna-.  b)  mit  Akk.:  yai  baraia il  a^n  baraiti  aisaam  Y.  62.  9;  —  j"a>v-  a^rTm  mainyüm  framiUm  (sd.)  aspake '^anam  fa  *barytqm^^  .  .  raoynoAe  "als  JbArpa..Yt!g.29.  Undeutlich:  jra  «ara Speise  soll  ihm  gebracht  werden  . ."  H.  gätum  baraiu  (3DPM-)  F.  ^  d;  —  pas^a
17023:•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]
17025:•  ].,  g.  baraziäta-  Adj.  'der  höchste,  hüchst- gelegene':  'te paiti  bantaAi  Aaraiiyg paiti bansayä  Y.  57.  19;  —  'taiibyS  gairibyö V. 2. 22;  —  'laihiaia  paiti  gätuha  V, 6^.45;  —  urvaranqm  .  ■  ysi  hftiii ..  'taca V.  2.  28; —  imä  raoiä  't?m  bar»zimanqm
17033:•  j,  bar9ziS.havant-  Adj,  'mit  Polstern, Kissen  versehen*:  gätu  ..  *'vafifym(ASm. statt  n.)  Yt5.  loa''; — gOtui paiH  .  .  ySi tnra  'vants  Yt  17.  i  o ;  —  gatava . .  'vatiiö
17682:betrauten  Unterpriesters  (ra/av-) :  äat  'iari (GS.,  näml.  kairim)  yal  a%rasca  alvqm hraxiim  yaoida^ai  barismanca  frahm ähralca  yasf0.k»r>taiibyd paiti.barät  "(das Amt)  des  Fr.  (ist),  dass  er  eine  Ecke  (ein Viertel)  des  Feuers  gehörig  in  Stand  setzt und  die  .^.-Stengel  herbei  und  dem  Feuer bei  jedem  yenhi-hStqm-Qi€at'(.  (Brennholz) hinzubringt"  N.  ■]4;  —  ava^a  "ta  *zaohrä frabaröit  N.  68;  —  'lar^  däityS  gätus *haoyqm  upa  %raxiiin  fratarqn  bansmqn "des  Fr.  gehöriger  Platz  (ist)  auf  der linken  Seite  vor  dem  B"  N. 75";  81, *Vyt  15";  —  paoiryS  .  .  kavanämm  (sd.) ..  astayeiti  ..  '^ritlm  'tat>m  N,  i'2;  — 'tänm  ästäya  Vr,^.  i;  G._J.  5;  —  ätra- 7'ax/e  vä  'itre  va  V.5.  $7;  58;  —  Va  N. 7J,  *6yi\ Elg.  'der  herzuträgt'.  —  Vgl.  ax.  fräb/iatiar-  m.
18684:—  apqm  napät>m  .  .  yS  nirSus  daha  yO n^rfu/^i  taiasa  Yt/5.  51; — ya>a  nars vay%an?m  "wie  der  Kopf  eines  Menschen" V.ö".a2;Äa3,F.jc,P.j4;  —  narqm  näiri- nqmca  .,  ti  hrmava  mti-viaire  djyammm Visp?m  3  afimät  yat  aSe  narS  "var^/iva anhm  V.2.27C;  —  cvaiti  narqm  ..xaota ratufris  N.  20;  —  yS  narS  kimSgatvS  . . anya  dva  vä  nara  , .  3at  aSsqm  narqm  .. cvat  antari  ^mr^us^'^  V.5.27;  4.i,ä,;- — yä  nara  (NS.)  gätum  baraite  F.^d;  N. 64;  —  paoifTtn  upa  may^m  frä.nasus (sA)  nartm  (statt  NS.)  bavaiti  V.  g. j8.  A)  Gegenüber  einem  attributiven a)  Substsl,  b)  Adj.  oder  c)  Proa  tritt nar-  vielfach  so  zurück ,  dass  wir  es  un- übersetzt  lassen  können;  es  gilt  das  ins- besondre vom  NS,  nä,  der  dabei  meist in  der  Stellung  der  Enklitika  —  hinter  dem ersten  Hochton  des  Satz-  oder  Versteils  — auftritt  a)9>  cvat  na"'^  3%rava  (sd.)  .  , *parayäl  ". ,  (ein  Mann,  der  Priester  ist, sva.)  ein  Priester  .  ."  N,  ^;  —  ydha  na taxmS  ra%a2stä  .  .  kaca  saltät  (sd.)  .  . paiti.ynUa  YtiJ.Sj.  b)  tts  nä  sayeiti (sd.)  vyäxanS  Yt  13.16;  53,  V.5. 40;  — paeiryeheca  na  myatdahe  aZaiit  (sd.)  .  . raius  , .  ratunafm  ayasnXm  (sd.)  daste  A. 3.  7;  8— 12*;  —  daxma  .  .  yahmya  nars irisla  nthayänte  V.3.Q;  Vd.  2',  17,  Vyt 12;  —  kva  narqm  iristanqm  tansm barama  V.  (j.  44;  —  kat  /a'(Sp,  612) nara  iristd  . ,  nasus  upaMvqsaiti  V,  7. 1;
19128:•  j.  ni'tama-  Adj.  (fem.  'ms-)  'der  unterste, am  tiefsten  befiadliche'  (nach  Lage,  Grösse, Zahl,  Dauer  usw.):  °ma?hia  gätuha  hasa- t9rS.Umahvaca  "an  den  tiefstgelegenen  und ganz  finsteren  Orten"  Yt  15. 53  {?);  —  'macit avatlqm  stsrqm  (sd.)  ya'ha  .  .  "die  klein- sten .  ."  F.  4  a;  —  cvatbya  nä  'maübya havana^bya  (sd.)  ratufri^  "wie  gross mindestens  . ."  N.  108;  —  fratamim  dat'ä- hSus  nava  Pfriems  (sd.)  .  .  m^»nts . .  'ntü ft'jrJ  V.2.  30;  30'';  —  *äjata  nU  *''ma'^ bansmana  ratu/ris  'Ü.QO;  —  *cvaia  (sd.) nä  *'ma'^  vaca  gahä  srävayS  ratufril "quanta  minima  voce , ."  N.  27;  —  dvadasa Vitara  (sd.)  upima  nava  . .  mäb>ma  xi^a/. . 'ttia  (NPm.)  V.  14.  14;  —  cvat  'mum haslnm  (sd.)  anhat  .  .  N.  J/;  —  'macit *haoma.küiiil  hazatgraynyai  astt  dalvanqm "auch  die  geringfügigste  //! -Kelterung  dient dazu  tausend  D.   zu   töten"    V,  70.  6;  6*;
20209:7.71;  —  Aväo  (Stvcrz.)  tl  VMVzyqa  aSe yöi  'na  V.5.  10  usw.;  3.  13%  5.  42,  6.  6, ff.  49,  Vd.  if{,  ig,  20;  —  a/fata  hl  alte 'na  .  .  ava.kan»m  ava.kanaym  V.  8. J.  18,  5.13,  14,41.42.43.61,6.7,  46,  51, 7. 12,5.39',  i4'T,  iS.3,  12;  —  aäahe yat 'nahe  aitayh  näirikayä  V.  16. 13;  —  mSca pascaSct  °na  tarn  sam  käraytn  V,  6. 2 ',  3.4.  6,3.ao,'S.ii',az',  37,  N./O^;  — vasä  pasiaita  'na  (ab  AP.)  vlmätasSt vlma%ayania  V.  7.  40;  38*;  —  kahmäi •nanqm  har?%r?m  barät  V. /j.  17;  N.  6j; — yuto  gätus . .  anyaeibyO  'na^iyüY.^.^^. ^.  33,  Vyt4i5;  —  °«^  "Ä«  sfrivana^Sii (sd.)  aväjanim  FrW.  <?.  i ;  F.  //,  Vd.  y; y?  «^Äfl  'naifva  °nS  aojanS  .  .  ya'hma aiahe  gafhh  tnff7y»nie  avi  tu  dim äisyata  (sd.)  Y.  Ä  3 ;  —  yasca  aäaesqm 'nanqm  . .  imq  vaS!  nnil  *vTsaite  framruite (sd.)  attam  (Sp.  19  u.)  ä  yätumanahe  jasaitt Y.Ä4.  '  [Y.J2.2:  liesMäsrfaj";  — N.ft: lies  myazdävanam^
21106:•  j.  yaJoit  Konjn.  r)  'sofem',  mit  Praes.: y  azle  framarpnti  '"yatöit'^  ratufryJ  "so- fem sie  die  Gebete  sprechen,  sind  sie  r." N.53;  83.  a)  mit  Opt.;  im  Nachsatz «So:  *_f*  *nasn)m  *yärf  *g3^ä  asrävayS hyat  a^a  .  ,  "sofem  er  ein  halbes  Jahr lang  die  G.  aufzusagen  unterlässt,  so  . ." li.44.  2)  'auf  dass',  mit  Konj.:  iart- zistaisva  paiti  gätusva  . .  y°  äim  avazanqn (sd.)  V.  6'.45.  3)  'bis  dass',  mit  Opt: vTsppm  3  ahmiii  y  upa.Jassit  .  .  tanam V.  6'.  27,  4)  'als  ob',  mit  Konj.:  nöit vanks ..  syaoiin^in  vfr?3yäti  y  ..puüraie fra  natsim  (sd.)  tiasam  pacät . .  V.iÖ.iy.
21245:At/  Aumayalfa  ..  ana%amaide  Vr.J2.4;  — ka  afaa  aSsjtaitÜ  yä  vispim  imat . .  an- /aiti?  ,  ,  y  /raoirisaiti  pairi  dusma- taäbyasca . .  H.  /.  1 6  f.  3)  mit  Opt :  alrnq ß-asapcayaAi{sd,)..y  [va\..ätrpm  uzdarxa (sd.) ..vT/a  bareil..  V.S.j s-  VII)räumUch 'wo'j  nur  b)  im  jAwr.:  iva  aitaAe  nari gätui  atfAal  ..  ?  ..  y  atsAat  aiAAä  B»mS vT.aps.t>mim(sd.)ca  ..  V.j,  15;  10,18;  — a/lfm  nmarigm  y  also  na  para.trikyat  V, 5.41;  —  abda(^d.)ca  iaa  (Sp.  364  u.)  sa- dayät  y-  ioa  pasSus  . .  päiim  vamaiU  V. 2.24; — tä  jäfl(Sp.  364U.)  _)-*  narö  p»n- IfnieYti^.  27.  VIU)  vergleichend 'wie'; a)  im  gA^y.  'so  gut  als',  mit  Opt :  *'AaÜy<>.- dvalsi  (sd.)  hy  isöya  drfgväite  .  .  hyim Y.43.Z.  b)  im  jAw.:  ana  'kwä yama yagane  . .  yas?^^  %wa  yazata  vTitasps  Yt /7. 61;  —  Ay  paourvim  tat  ustfmim(&d.)- ät  Y.56.1,  Vr.().  7.
21510:•  j.  yahmya  Adv.  'wo,  ubi' :  yai  bä  paiti fraishm  daxma  (NPm.)  uzdaSza  (sd.)  kir- yeinie  y  narS  irtsta  moayeinteV.3.');i2, 7.  54i  —  tl  narB  xsd^ra  (APn.)  xsqymte ,,  y  stariiatca  gätus  .  .  Yt/7.  7;  — arpdvJm  (ASf.)  , ,  y  ('ubi'  statt  'in  qua') ahurS  masdh  ..  niva^ayal  Yt.5.  85.
25491:•  j.  iristö.kasa-  m.  Totenwärter':  kva aita/ie   nars   gätus    anhat   yat    'sähe    V,
26080:•  j.  saire.hya-  n.  'Vorrichtung  zum  Dörren von  Mist"',  Mistdarre':  yff  ätr^m  °hyai haca  däitim  gätutn  avi  ava.iaraiti  V. Ä83.
=== BRT gāman ===
2706:•  j,  aevo.gaya-  n.  'Längenausdehnung  |(>ij«(i">  me  yaoidäiUm  "ihr  könntet  mich eines  Schritts,  eine  Schrittlänge';  Äa/ ^«i-a  ,  purifiziren"  V.Äioo.  1,2  a)  mit  Gen. anys.anyaeibyö}  ya^a  'gatm  iu^a  (sd.) '  und  Inf.:  naj/a  .  .  Aäu  ni  ahmat  haca •gsimi  ,  .  "Wie  weit  von  einander?  "SiQ  gstaot  isalta  frasBtÖit  »eil  apasüföil  (sd.) viel  als  eine  Schrittlänge  beträgt  .  ."  "^  .{'^rayamcina  gämanam  P.  2jj>.  3)  '(es) p.  S.                                                                     I  können,  vermögen,  (dazu)  im  Stand  sein',
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
10341:•  j.  gäman-  n.  'Schritf:  paeirJm  °ma frabaraf  yS  nars  asaonB  urva  humate  paiii nidiäial  "primum  gradum  profcrt  ,  .  de- ponit  .."H. 2.15;  15-1,  33;  —  kaka  (sd.) '^rigäiml  yaia  'man  haniayata  V.p.  g;  9; —  fialla.-ismta  . .  apasBiffit (so.)  '^rayam- cina  -manqm  P.  23.  a)  als  Masseinheit : yä^a  vS  °ma  dvala  *diisaca  *antar>.ii,wqm (sd.)F.27a;  —  tat*°/naAva'^  *irigamimY. 27  b  K'>.        [Yt.  70.  52:  lies  %wafa^,inf.'\
10350:•)  D.  i.  drei  Fuss  oder  zwei  Ellen;  s.  Pu. Vgl.  gäman-,
11160:•  j.  ca9-war«-sant-  fem.  Zw.  'vierzig': ^a'^u/arasla  a^a  garayl  .  .  'satimca  (ab Nom.)''  dvai^a  saite  dvai^a  hazaj»re  "es gibt  so  2244  Berge"  Yt./p.?; — paruäla 'sat>mea  maiiysizarmtayehe  (%A^  . .  "45  . ." A.j.  7.  a)  mit  Gen.:  'sat?m  (Alck.)'* aiwigämanqm  V.  2.  41;  5. 93,  /2. 14,  *Y. 65.4»,  ^Vi/p.
14670:•  j.  Sri-sant-  fem.  Zw.  'dreissig*:  yiA  htnti a^ake  ratavS  %rayasi!a  'sqsca  (Nom.)  Y, /.  10;  —  'satim  (als  Nora.)''  ayiihrimahe (sd.)  mi^raAe  anayranqm  A.  3.  10;  F. 23.  a)  mit  Gen.:  °satpm  (Akk)"'  aiwi.- gämanqm  "dreissig  Jahre  lang"  Yt  15.29; 10.122,  Y.4.ig',  6.11',  Ä94,  12.1,  18. 74.  a)  attrib,  gebraucht:  mal  'sqs (statt   Instr.)"  /radaxsanyais  \.  14.  q;  9,
19067:die  Modusform  des  vorausgehenden  posi- tiven Satzes  zu  ergänzen:  v>r3zyät  usaiii «*  *anusaiti  N.  ö";  V.  <?,  37, 39;  —  nalca .  .  *Aau  na. .  isaita  /rasBtsit  n'  apaiütBit (sd.)  'äirayqmcina  (Sp.  595  o.)  gämanqm P,  23;  —  (^ai)  na  datvayasnäi  . .  *caiaiiet . .  dahmS  niuruzdö  (nämL  casaiti) . .  *pairi.- gjnptayat  paiti  zimanaya  (sd.)  «°  *anaipi.' ggrgptayJt  paiti  N./7;  Y.8.\y, — fra  ml gaowa  zasayqn  mib^rgta(sd.)  n'  ainizb^yta V.  ^.  3  7 ;  —  aiwyästa  .  .  ga^ä  sravayat n'  anaiwyästa  N.  .^J.  Anhang  zu  II:
28449:nasca  pascalta  *käu  nS  akmat  kaca  gataot isalta  frasütöit  ttsit  apalüiStt  '^rayqmana gämanqm  "und  dann  wird  der  Mann  nicht mehr  fähig  sein,  sich  von  diesem  Ort  nach vom  oder  hinten  zu  entfernen,  auch  nicht drei  Schritte"  P.:;^.
```


## [2026-09-06T02:18:39.730Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT gathu ===\"; grep -n \"gāθu\\|ga-a-thu\\|gathu\\|gāthu\" KNT.txt | head -20; echo \"=== KNT hangmatana ===\"; grep -n -i \"hangmatāna\\|hagmatāna\\|hangmat\\|hagmat\\|Ecbatana\" KNT.txt | head -20",
 "description": "Grep Kent"
}
```


### [2026-09-06T02:18:39.809Z] TOOL RESULT

```
=== KNT gathu ===
=== KNT hangmatana ===
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Áriaramnes and grandfather of Darius. Note that the two inscriptions are both on gold tablets and found at or near Ecbatana
1321:-gmata- ‘gone’, to root gam-, in pardgmaté hagmata Hagmatüna-.
1970:regularly given; but it is given with names of provinces only when there is a list of all or several, and is omitted with some larger districts (Kar- тала, Varkàna), with cities (Pársa, if = ‘Persepo- пе’; Passiyduvdda ‘Pasargadae’; Hagmatana 'Ecba- tana’; Arbatra ‘Arbela’; Babirus ‘Babylon’), and with well-known rivers (Ufrätuš ‘Euphrates’;
1975:Мада ‘Media’: including districts Asargarta (given as administrative province in DPe 15), Kapada, Nisdya, Raga; city Hagmatäna; towns KuduruS, Māruš; fortress, Sikayawvatis.
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2907:past participle has active meaning, as in DB 2.32, E | 38, 43, 52, 571, 3.65 hamiciya hagmaté paraità ‘the =$
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3595:52 Syava : yatà : Arminam : parárasa : pasàva : hamiçzyā : hagmatà : paraitā : pa ^
3601:58 iciyd : hagmata : paraità : patiš : Vaumisam : hamaranam : cartanaly : Au
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at my palace entrance, all the people saw him. Afterward I impaled him at Ecbatana; and the men who were his foremost followers, those at
3681:Ecbatana within the fortress I (flayed and) hung -
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
4886:After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the name of Imanish. At the approach of Darius the Elamites were terrified, and seized Martiya and killed him (§22-§23) Darius now sent a force of Persians and Medes under Arta- vardiya, a Persian officer, against Vahyazdata, who had made himself King in Persia; he himself, with the rest of the Persian force, went on into Media (§41) and at Kunduru was attacked by Phraortes himself and his army, on I 25, 521/0 (§31). Phraortes’ army was routed; he himself es- caped with a few horsemen, but was overtaken and captured at Raga, and mutilated and put to death with torture at Ecbatana ($32). From Raga Darius sent a force of Persians to reinforce Hystaspes in Parthia (§36).
```


## [2026-09-06T02:18:45.966Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Hagmatàna-\\|Hagmatāna-\\|Hagmatana-\\|Ecbatana’\" KNT.txt | head; echo \"=== gathu lexicon ===\"; grep -n \"throne\" KNT.txt | head -20",
 "description": "Kent lexicon entries"
}
```


### [2026-09-06T02:18:46.036Z] TOOL RESULT

```
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
=== gathu lexicon ===
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been set up in the time of Artaxerxes П as part of an anti-Cyrus propaganda, since Cyrus the Great had dethroned Arsames, and Cyrus the Younger came very near de- feating and killing Artaxerxes II at Cunaxa (cf. JAOS 66.206-12). The gold tablet A?Hc may have been a third in the same series; all three are in Old Persian only. *Cf. especially Schaeder, SbPAW 1931.636-42. 4 They are hardly to be ascribed to Cyrus the Younger, despite Wb. ZDMG 48.653-65 (cf. also KIA lxvii-bax) on CMa, which alone was known to him; for the opposing view, cf. Hz. Klio 8.1 ff. * Though perhaps not much used by him. The other three known inscriptions of Cyrus the Great are in Akkadian; but Strabo 15.3.7-8 (page 730), on the authority of Onesicritus, states that the tomb of Cyrus at Pasargadae bore at least two inscriptions, one being bilingual, Greek and Persian. We need attach no importance to the identification of the languages by Onesicritus, but the account indicates that Cyrus had inscriptions engraved in more than one language; in which case it is unlikely that his own vernacular was omitted. Cf. JAOS 66.206-12; but also Hinz, ZDMG 96.343-9.
823:III. The labels of the throne-bearers in DN and A?P are sometimes written with the plural of the ethnic, or with the province-name for the ethnic; we give the examples, with a literal translation:
2707:D. Abnormal uses: The locative sometimes re- places the ablative with hacã, to denote place from which: Ласа Babiraw ‘from Babylon’ (DSf 33; but the abl. in Маса Babiraus DB 2.64), Ласӣ Hidaw (DSf 44, DPh 7, DH 5f); and once even without the preposition: XPf 32-4 yabimary рий DérayavauS gdbavd axiyava ‘when my father Darius went from the throne (= died)’.
3321:the appearance of the front of a Persian palace. The central panel contains the doorway to the tomb behind. The upper part of the cross is occupied by a throne platform, supported by 30 throne-bearers in two lines; Darius stands on a basis of three steps, facing right toward an altar, while beyond the altar there floats in the air the figure of Ahuramazda. At the extreme left of the field are three attendants of Darius, arranged vertically one above the other, the lowest one being on a level with the lower line of throne- bearers.
3322:The inscription Nag$-i-Rustam a is inscribed behind the figure of Darius; first OP in 60 lines, then a second column of Elam. in 48 lines, finally, outside the niche on the adjacent rock the АКК. in 36 lines. Inscription b stands on the two sides of the door in the center of the crossbeam: OP in the panel to its left, in 60 lines; Elam., 43 lines, in the panel to the right, with an Aramaic version in 25 lines at the bottom; in the last panel to the right, the Akk. version in 39 lines, with the space of one line vacant between lines 31 and 32. In- scription с, trilingual, 2 lines for each language, is attached to Darius’s spear-bearer, the topmost figure of the three at the left margin behind the king: d, trilingual, the OP filling 2 of the 5 lines of text, is attached to his bow-bearer, standing beneath the spear-bearer. Inscriptions 1 to xxx, trilingual, attach to the throne-bearers, but not all of them are legible.
3397:А?Р = Artaxerxes II ов III, PERsEPOLIS: Trilingual, labeling the throne-bearers of the south tomb. Davis, JRAS 1932.373-7 and Plates 2-3; Hz. ApI 46-50 No. 24 (1938); Sen, OPI 172-8 (1941).
4114:$4. 30-47. Saith Darius the King: Ahuramazda, when hesaw thisearth m commotion, thereafter be- stowed it upon me, made me king; I am king. By the favor of Ahuramazda I put it down in its place; what 1 said to them, that they did, as was my desire. If now thou shalt think that “How many are the countries which King Darius held?” look at the sculptures (of those) who bear the throne, then shalt thou know, then shall it become known to thee: the spear of a Persian man has gone forth far; then shall it become known to thee: a Persian man has delivered battle far indeed from Persia.
4530:$4. 27-43. Saith Xerxes the King: Other song — of Darius there were, (but)—thus unto Ahura- mazda was the desire—Darius my father made me _ the greatest after himself. When my father Darius went away from the throne, by the will of Ahura. mazda I became king on my father’s throne. When I became king, I built much excellent (construc- tion). What had been built by my father, that I protected, and other building f added. What more- over I built, and what my father built, all that by the favor of Ahuramazda we built.
4843:Ail the accounts, literary and inseriptional, are presented and evaluated by Weissbach in PW, Suppl.-Bd. 4.1132~44, s.v. Kyros. His conelusions are as follows: Of the sons of Teispes, Ariaramnes was king in Persis (then called Parsua) and Cyrus I was king in the city (or district?) Anshan, lymg between Persis and Elam, or possibly farther north, between Persis and Media. On coming to the throne of Anshan, Cyrus IT found Arsames ruling in Parsua, and shortly deposed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
4851:The Magus Patizeithes had been left by Cambyses as managing steward of his palace at Susa, and he was one of the few who knew of the death of Smerdis. He had himself à brother who greatly resembled Smerdis in appearance, and, says Herodotus, this brother's name was also Smerdis. Patizeithes put his brother Smerdis on the throne, under the pretense that he was Smerdis son of Cyrus and brother of Cambyses. The false Smerdis, by not admitting to his presence any one who had known the true Smerdis, successfully con- cealed his true identity for some time (61-2). But the news reached Cambyses in Egypt, and he knew the truth, because Prexaspes assured him that he had slain the real Smerdis. Resolved to fight the usurper, he leaped upon his horse to lead his army back to Susa, but as he did во he accidentally struck the point of his sword into his thigh, and from the wound he died (63-6). Thus the false Smerdis ruled for some months; but a Persian
4853:nobleman, Otanes son of Pharnaspes, suspecting his identity, managed by a ruse to prove it to himself (67-9), and secured the help of five other trusted noblemen, to whom there was added Darius, who had come to Susa from his father Hystaspes, governor of Persia (70; see App. IIT). Darius insisted on immediate action against the two Magi (71-3). Helped by the confusion follow- ing the public confession of Prexaspes that he had murdered the true Smerdis, and by his suicide, the seven men burst into the presence of the two Magi and slew them (74-9). They then agreed upon a method of selecting one of their number to hold the throne, and Darius, aided by the trickery of his groom Oebares, was the winner (80-8).
4903:In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
4905:after his accession to the throne, as to which should have the succession. On the advice of Damaratus, exiled king of Sparta, Xerxes went to his father and pressed his claim on the ground that he was the oldest son of Darius the King, while Artobazanes was only the oldest son of Darius the private individual. Darius approved the claim, though perhaps the argument was not really needed (Atossa as daughter of Cyrus must have had great influence with Darius, and Xerxes was probably the ablest of Darius's sons), and named Xerxes to succeed him. Before he had finished the preparations for the campaigns, Darius died; whereupon Xerxes ascended to his father's throne.
5353:gafu- sb. ‘place, throne, place of battle’
```


## [2026-09-06T02:18:50.827Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5345,5365p' KNT.txt; echo \"=== Hagmat ===\"; grep -n \"Hagmat\" KNT.txt | sed -n '1,40p' | cut -c1-200",
 "description": "Kent gathu- and Hagmatana entries"
}
```


### [2026-09-06T02:18:50.910Z] TOOL RESULT

```
(670, 5101, $1431). диа adm. ($189) DB 274, — |
| КИ adven as n Le ЧЕР Г PERDE :
ок ALES
e
LESIN EI EOE PE EERE СООТУ
I aen i bag ih oea CAU Lin aE M iig Án
LEXICON
89. gaušāyā idm. (5189; with sg. ending, Lg. 19.225) DNb 53.
gafu- sb. ‘place, throne, place of battle’
(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
gad- vb., see jad-.
Ga*dara- sb. ‘Gandara, Gandaritis’, a prov- ince of the Persian Empire: Elam. gan-da-ra, Akk. gan-da-ri. See also Gadáraya-. Сайдта nsm. DB 1.16; DPe 1.18; DNa 24f; DSe 24°; DSm 9°; XPh 25. Gadārā absm. DSf 34.
Ga"déraya- adj. ‘Gandarian’: adj. to preced- ing ($144.III, $167). Gadàraya пзш. APP 12.
Ga*dutava- sb. ‘Gandutava’, a district in Arachosia: Elam. gan-du-ma-+. Cf. Tm. Lex. 86. Gadutava пет. DB 3.66.
gan- vb., see jan-. gand- vb., see gasta-.
gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.
ava- + gam- ‘go down, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
=== Hagmat ===
1321:-gmata- ‘gone’, to root gam-, in pardgmaté hagmata Hagmatüna-.
1970:regularly given; but it is given with names of provinces only when there is a list of all or several, and is omitted with some larger districts (Kar- тала, Varkàna), with cities (Pársa, if 
1975:Мада ‘Media’: including districts Asargarta (given as administrative province in DPe 15), Kapada, Nisdya, Raga; city Hagmatäna; towns KuduruS, Māruš; fortress, Sikayawvatis.
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
```


## [2026-09-06T02:18:58.062Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if 'gafu- sb.' in p or 'Надтаій' in p or ('Hagmat' in p and 'Ecbatana' in p and 'nsf' in p):\n        print('PAGE index',i,'(0-based) -> printed approx',i-15)\n        print(p[:200].replace('\\n',' | '))\n        print('---')\nEOF",
 "description": "Locate Kent pages"
}
```


### [2026-09-06T02:18:59.847Z] TOOL RESULT

```
PAGE index 205 (0-based) -> printed approx 190
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52. | azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. 
---
PAGE index 206 (0-based) -> printed approx 191
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46). | рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f. | ham- + gam- ‘come
---
```


## [2026-09-06T02:19:06.335Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Ecbatana\" KNT.txt | cut -c1-300 | tail -6; echo ===; grep -n \"ha\\\"gmatà\\|ha\\\"gmata\\|hagmatā\\|Hagmatāna\\|Надтаійла\" KNT.txt | cut -c1-250",
 "description": "Find Kent Hagmatana lexicon entry"
}
```


### [2026-09-06T02:19:06.395Z] TOOL RESULT

```
Exit code 1
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Áriaramnes and grandfather of Darius. Note that the two inscriptions are both on gold tablets and found at or near Ecbatana
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, J
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at my palace entrance, all the people saw him. Afterward I impaled him at Ecbatana; and the men who were his foremost followers, those at
3681:Ecbatana within the fortress I (flayed and) hung -
4886:After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the name of Imanish. At the approach of Darius the Elamites were terrified, and seized Martiya and killed 
(eval):1: == not found
```


## [2026-09-06T02:19:30.537Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Hamadan\\|Ecbatan\" KNT.txt | cut -c1-160; echo \"=== ham- section ===\"; grep -n \"ha\\\"gmatā\\|ha\\\"gmata\\|gmatana\\|gmatäna\\|gmatina\" KNT.txt | cut -c1-200",
 "description": "Search Kent for Ecbatana lexicon"
}
```


### [2026-09-06T02:19:30.604Z] TOOL RESULT

```
122:І The Inscription and Sculptures of Darius the Great at Behistan.............. II The Gold Tablet of Hamadan ПІ The Daiva Inscription of Xerxes
312:A? = Artaxerxes П or ПІ Н = Hamadan А? = Artaxerxes ПІ M = Murghab W = Weight of Darius І = incerto loco S = Seal Vs = Vase
333:Elam, at Susa; in Media, at Hamadan and the not too distant Behistan and Elvend; in Armenia, at Van; and along the line of the Suez Canal. They are mainly i
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Ária
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been
649:has Х and DH, but not BU. At Susa, Darius 3 I varied from the use of none to the use of XŠ $ only, and that of XS DH BU AM, so far as they $ occur (on DSe
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату dra
3289:AsH = Авѕлмев, Hamapan: OP only, 14 lines, on a gold tablet in three pieces, complete except for lower right corner; about 9 x 13 em.; found at Hama
3295:DB = Dans, BeursTAN: The inscription of Behistan, trilingual, is inscribed on the face of a gorge in the cliff rising on the left-hand side of the main car
3355:DE = Darius, Exvenn: Trilingual, each version in 20 lines, in a niche cut in the face of Mt. Elvend, one hour's riding time southwest of Hamadan; probably 
3396:A?Hc = Artaxerxes 11, Hamapan c: OP only, in 20 lines on a gold tablet, about 13 x 18 cm.; found at Hamadan; see §18 n2. AUPope, The Hlustrated London New
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at m
3681:Ecbatana within the fortress I (flayed and) hung -
4886:After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya
=== ham- section ===
1970:regularly given; but it is given with names of provinces only when there is a list of all or several, and is omitted with some larger districts (Kar- тала, Varkàna), with cities (Pársa, if 
1975:Мада ‘Media’: including districts Asargarta (given as administrative province in DPe 15), Kapada, Nisdya, Raga; city Hagmatäna; towns KuduruS, Māruš; fortress, Sikayawvatis.
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea
3621:78 gmatanaty : atar :didim :frahajam : ðātiy : Dárayavaus : x3
```


## [2026-09-06T02:19:37.211Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"batana\\|bataná\\|Ьat\" KNT.txt | cut -c1-200 | tail -20; echo \"=== find lexicon h area ===\"; grep -n \"hacā- \\|hacā prep\\|hamiciya- adj\\|hama- adj\" KNT.txt | cut -c1-200",
 "description": "Kent lexicon h-section"
}
```


### [2026-09-06T02:19:37.284Z] TOOL RESULT

```
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Áriaramnes and grandfather of Darius. Note t
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea
3680:Thereafter I sent an army in pursuit; Phraortes, seized, was led to me. I cut off his nose and ears and tongue, and put out one eye; he was kept bound at my palace entrance, all the people saw hi
3681:Ecbatana within the fortress I (flayed and) hung -
4886:After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the na
=== find lexicon h area ===
```


## [2026-09-06T02:19:48.204Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nprint('total pages',len(pages))\nfor i in range(204,216):\n    p=pages[i]\n    print('=== idx',i,'len',len(p))\n    print(p[:300].replace('\\n',' | '))\nEOF",
 "description": "Inspect Kent page structure"
}
```


### [2026-09-06T02:19:49.901Z] TOOL RESULT

```
total pages 232
=== idx 204 len 3917
, 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, | 181 | 28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 62, 67 bis, 70, 72, 7161, 80, 86f, 87, 88; 5.1, 3f, 14f, 18, 20f, 301, 34; DBa 1, If, 2, 21, 5, 9, 14; DBb 6; DBc 6f; DBd
=== idx 205 len 3954
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52. | azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. 
=== idx 206 len 3865
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46). | рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f. | ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43,
=== idx 207 len 3864
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. | | Citcizr
=== idx 208 len 3744
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231. | abi- + jav- caus. ‘promote, increase, add to’: abiyaj
=== idx 209 len 3897
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3. | tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31. | | tar- vb. ‘cross over’: Av. tar
=== idx 210 len 3740
1) XPh 23. | tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16. . tyaišām gpf. DSm 6°; XPh 15. | tya nsn. (M0) DB 1.27, 61, 67; 2.91; 3.10, 20, 58, 76; 4.1f, 42, 49°, 53;
=== idx 211 len 3945
 word of uncertain meaning, Sb 3. | Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339. | See also wlanwaniya-.  Ganwaniya.nsm. DNb 42. | 188 | * | bard- sb. ‘year’: Av. sarad- ‘year’, NPers. säl, Skt. Sardd- ‘autumn’ (§31
=== idx 212 len 4061
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis
=== idx 213 len 3951
5-6). | Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240),
=== idx 214 len 4046
Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. | Daha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26. | dahyu- sb. ‘land, province, district’: GAv. : | daltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘strang
=== idx 215 len 4103
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136). | duradasa
```


## [2026-09-06T02:19:58.365Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'gmat[aä]na|gmatina|Ecbatana',p) and 'sb.' in p:\n        print('idx',i)\n        print(p[:2500])\n        print('#####')\nEOF",
 "description": "Find Kent Hagmatana lexicon page"
}
```


### [2026-09-06T02:19:59.942Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:21:13.045Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\bhaca\\b.*prep|hamigiya- |haruva|hadis|hai\\?ya',p):\n        print('idx',i, p[:400].replace('\\n',' | '))\n        print('---')\nEOF",
 "description": "Find Kent h-section pages"
}
```


### [2026-09-06T02:21:14.851Z] TOOL RESULT

```
idx 30 padahya, Skt. gharmá-; дата-, Av. sarad-; darga-, Av. daraga-, Skt. dirghd-; baršnā, Av. instr. barasna; martiya, Skt. mártya- . | ardastana- ‘window-frame’, Elam. har-da-i5-da- па. | tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffix -ske-; but Skt. trásati from "ireseti. 1 cartanaty: the c shows that a front vowel formerly 3 stood immediately a
---
idx 53 ess a cognate from another ТЕ branch can be adduced. pIE *selyo- ‘all’, OP haruva-, Av. haurva-, Skt. | sárva-, Gk. Ion. oos, Att. ddos. pIE *pelu-, OP paru-, Skt. purá-, Gk. rodv-. pIE *leugos, OP rauca, Skt. rócas, cf. Gk. Аі | ‘white’. pIE *syel-nos, OP -farna in Vi"da-farnà, Av. | z"aronó ‘royal splendor’, cf. Gk. thas =“ | ness’ from *syel-ns. | pIE *g%el- in ОР car- in abicariš ‘pasture land’, ‘$ | т J | 
---
idx 54 ; but in Ау. it is subject to many graphic alterations: | OP yabā, Skt. ydtha. OP yadataty ‘he worships’, Skt. ydjale, Gk. | ето (PIE 1- > Gk. А). | OP dérayatty ‘he holds’, Skt. dhardyatt. OP vayam ‘we’, Skt. vayám. OP draya ‘sea’, Av. zrayó, Skt. jrdéyas-. After consonants also, pIE 7 remains unchanged | 39 | in OP and in Skt., but it is regularly written -y- ($25): | | root, kan- ‘dig’ + pass. -ya-, in aka
---
idx 81 * Lg. 15.175-6; for other in- terpretations of these two forms, see Lex. s.vv. * Lg. 15.170. | ТҮ. Acc. vilam, inst. 0100, loc. 1019710, to stem við- from pIE *yik-, also have the regular endings: acc. -m, inst. -ë or -0, loc. -1, here with added -@ because 110010 is a true locative in use. | V. Inst. pl. viðbiš and abis show the regular | -bhis seen in Skt. -bhis, Av. -bi; -6b- as a cluster remains by 
---
idx 82 lauviyà with 7408 (§48 for -auv-), to a positive *tau-ma- ‘strong’; cf. Skt. nsm. sthdviyan to positive sthi-rd-. | Comp. stem vah-yas- in Vahyaz-dàta- (for г, see §120), to positive va*-u- ‘good’, Skt. vásu-, cf. Lex. s.v. va^u-. | Superl. nsm. ma£isla ‘greatest’, asm. тай ат, with -isto-; cf. Av. masista-, Gk. Dor. дйкитто to px pos. | Superl. asn. duvazs[talm as adv. ‘for a very long | time’, Skt. ddvi
---
idx 85 en in Lt. nt. *ed in ec-ce ‘lo’; on it also is formed the ism. OP and, GAv. and, with the inst. ending -na scen in tyand. | $200. THe DEMONSTRATIVE PRONOUN ‘THAT’ was in OP ava-, found also in Av. (Skt. only gen. du. 2005). The extant OP forms are: | Mase. | Fem. Меш. | Sg. Nom. ava ava avas-ciy | Ace. отат ат ava avas-cry | Inst. avand | Abl. avand avand | Gen. avahya Pl Nom. - шту  apà] adi | Ace. азай | Сеп. avais
---
idx 111 ws in OP: | (a) Future conditions occur only addressed to an idealized hearer in the second person; the pro- tasis has the subjunctive in the second person, and the apodosis has a command or a prayer or a future statement; see $278.Ша. General relative clauses with the subjunctive are often a virtual substitute for this form of the condition; see §278 IIb. | | (b) A future less vivid condition, with o
---
idx 134 e palace’. | TRANSLATION oF CMb: Cyrus the Great King, son of Cambyses the King, an Achaemenian. He says: When ... made ... | CMc = Сүвоѕ, Murcuas C. Каги$ : zšīyaðiya : vazraka : Hazüámamstya | TRANSLATION or CMe: Cyrus the Great King, | an Achaemenian. | DB = Darius, BEHISTAN. | Text or DB, Coromn I: | 1 : adam : Dàrayavaus : xSayafiya : vazraka : xšāyaðiya : xáüyatty | 2 апат : xSdyafiya : Parsaiy : xSdyafiya 
---
idx 140  káram : tyam : hamiciyam : aja : vasiy : Güravüharahya : mah | 62 ya : jiyamnam : рабу : avatiSàm : hamaranam : kartam : pasàva : Vaumisa | 63 :cità : mim : amanaya : Árminiy&ty : yata : adam : arasam : Madam | 64 :08tiy : Dirayavaus : xšāyaðiya : pasáva : adam : nijàyam : haca : | 65 Babiraus : айуауаш : Madam : уада : Madam : parárasam : Kud"ru$ : nama : | 66 vardanam : Мадалу : avada : hauv : Fravartis 
---
idx 148 паша : Marduniyahyá : puça : Parsa : Vidarna : nama : Ва 85 gabignahya : puça : Parsa : Bagabux’a : пата : Dütuvahyahyà : риса : Pársa : | 86 Ardumanis : nàma : Vahaukahyà : puça : Pársa, „ 87 iya : tuvam : kā : xSdyafiya : һуа : aparam :  Bhy^: Буйло : imaigim : martiyind : àtiy : Dürayavaus : xšāyaðiya : vaSnà : Au i(mà)m : dipim : aniyaðă : adam : akunavam : раат : ariya : aha : utd : av ast | 88 m
---
idx 161 ase, slung over his left shoulder, and holds a battle-ax in his hand; ef. JNES 4.233. | TRANSLATION OF DN, MINOR INSCRIPTIONS: DNe: Gobryas, a Patischorian, spear-bearer of | Darius the King. | DNd: Aspathines, bowbearer, holds the battle-ax of Darius the King. | DN 1: This 15 the Persian. | DN II: This is the Mede. | TEXTS WITH NOTES AND TRANSLATION | DN III: This is the Elamite. | DN IV: This is the Parthian. | D
---
idx 163  : BUyàa : Vistispahya : риса : Haxáma | 8 nisiya : бану : Darayavau’ : XS : Auramazdà : | 9 hya : mafiista : bagānām : hauv : mam : ada : ha | 10 w : mam : XSyam : akunaus : haumaiy : ima : xša П gam : frábara : tya : vazrakam : {уа : uvaspam : uma 12 rtiyam ;'valnà : Auramazdaha " hya : mand : pita 13 : Vištāspa : uta : ArSdma : һуа : manā : niyàka : | 14 tyà : орӣ : ajivatam : yadiy : Auramazda : ma | 15
---
idx 170 : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv | Nove TO XPa: 1? Hārämanišiya, incorrect engraving for Házà-. | TRANSLATIO
---
idx 175 id, until I completed the work. | &4d. 46-56. Thou who (shalt be) hereafter, if thou shalt think, “Happy may I be when living, and when dead may I be blessed," have respect for that law which Ahuramazda has established; worship Ahuramazda and Arta reverent(ly). The man who has respect for that law which Ahura- mazda has established, and worships Ahuramazda and Arta reverent(ly), he both becomes happ
---
idx 176 zSaqam : Ша : атану : kartam | Хоть то XV: The entire line 25 is clearly legible in the photograph reproduced by Lehmann, SbPAW 1900.1.628 Taf. 2. | TRANSLATION OF XV: | §1. 1-9. A great god is Ahuramazda, the great- est of gods, ... (= XPa 1-6). | §2. 9-16. ... (= XPa 6-11). | §3. 16-27. Saith Xerxes the King: King Darius, who was my father—he by the favor of Ahura- mazda built much good (construction), an
---
idx 177 this palace, by the favor of Ahuramazda, I after- wards built (to completion). | A’Sa = ARTAXERXES II, Susa А. | 1 Qty : Artaxfagà : XS : vazraka : XS : XŠyänām : XŠ : DHyinim : XS : ahyiya : BUyà : Darayavausahya : XShya : риса : D | 2 ürayavaufahyü : Artaxšaçāhyā : XShya : puça : Artaxsagahyà : Xšayārcahyā : XShya : риса : XSayarcahya : Dara | 3 yavaudahyd : XShyà : puça : Dérayavausahya : Vi Stáspahya 
---
idx 222 -. — fra&aram asn. XPf 26f, 37. | Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. 
---
```


## [2026-09-06T02:22:03.255Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### BRT jantu\"; grep -n \"jantu\" BRT.txt | cut -c1-400 | head -5; echo \"### BRT hanjamana\"; grep -n \"ha.jamana\\|hqm.jasaiti\\|hanjamana\\|hqmjamana\" BRT.txt | cut -c1-400 | head -8; echo \"### BRT frajam\"; grep -n \"frajam\\|frajasaiti\\|fra.jam\" BRT.txt | cut -c1-300|head -8",
 "description": "Bartholomae lookups"
}
```


### [2026-09-06T02:22:03.350Z] TOOL RESULT

```
### BRT jantu
10636:KompA.  —  El.?J)  —  Pü.  (zu  1);  xral  slarl*), Sü.  1  buddhija4a^,  buddhinaslah,  (zu  Y.  34.  g): ksudrajantui,  erl,:  duflasv.ipadai  pärvaliyah; (lu  l)  xta/sir  (Transskr.).  "  ')  daäiäücä  . . mafyäiirä  sind  attributiv  gedacht.  —  'i  Wie solche  hundertweis  zu  erschlagen  als  verdienst- liches Werk  gilt;  s.  auch  j-rn/j/riJf a«-.  —  31  Die Zerl
### BRT hanjamana
17874:reden, besprechen':  vlspalfO  ^frasnailü vTspaäa  hanjamanalsä  yaU  apinsaltim (3D.,  Augm.)  mazda sca  xardhustrasca "bei  allen  Besprechungen,  bei  allen  Zu- sammenkünften, bei  denen  sich  bespra- chen . ,"  Y.  72.  5.  a)  mit  Angabe des  'mit  — '  durch  o)  Instr.:  anulAaxs *armaitis  matnyS  *p»r3saite ya'hra  ma/%a (ad.)  Y.J7. 12;  —  hs  aSava  yail  p3r3iai dng
20235:—  kai  afava  'da  vanat  drvant»m  Yt./,  aS; — pata  nS  ibifyantaipairi  °</jj(als  Vok.)/a armaitiica  SrB.j;  —  hanjamanaisü  yai/ apmsalhm  'd3s^  sara'küitraslä  Y.  12.  5 ;
23944:•  j.  vi-£ar3na-  n.  Trennungsstelle,  Stelle, wo  sich  der  Weg  teilt":  pa%amcS  *'rjnä'> .  .  pahqmia  hanjamana  Y,  4-3.  i ;  — fakqm  '.  .  paiti  'na  Yt  //.  4,  Vyt.  54.
24412:—  °/i7?j(i/n(GPm.)Ä  ra%wqm  'panqm- (GPf.>o  'ratufriünqm  Vr.g.y;  —  'pa- nqm  (GPm.)  arinäm  . .  'panqm'  (GPf.) häirisinqm'  Y.  65.  2;  1.  12»,  2.  11,  g.  18, 2Ö'.2,  7-9^  27.1,  62.8,  77,8,  Ytj.2a,  50, Ä'.39,  70.  145.  J2.  17,  /J.  145'.  '48^  77.1, 1S.6,  ig. 35,  V.  2.  a7f.<,  7j.  16,  7Ä70,  Ny. 4. 1'.  FrW.  7. 1,  N.  22, 3S,  3g,  5g,  Vyt. 50, 
29334:hanjamana-  1770
### BRT frajam
3296:doppelt: 'et  ,  ■  et':  a^ra  aö-  frajasaiti baxta{sd.)  fl'>°  nijasaiti  V.5.8;  —  am»sa sptntl  , .  ao°  M-lta  (sd.)  ao°  büta  haca vanhaot  manaifhöYx.ii.\2.
3432:•  j.,  g.  a'^Tä  Adv,  1)  räumlich  'hier;  da- hin' :  °ra  pasiaHa  vazaile  vats  . .  värsmca ..  avi  asä  Yt.Ägs;  /p.69;  —  «a/  °ra vicarmti  .  .  yty.49;  V.  J7,s; — yai  °ra para.jasaiti  ..  ya^ra  .  .  Ytio.ioi;  — *'fa')  *a'^viayaM/tJin (s<i.) yaira ..N.  1
8843:S4-J3',  —  *a/  aitahe  paiti  .  .  axaBa  V. JÄ68; — /fl/(ASn.)*'  alsa  nätrika paoifim :^ar»%anam  c^aräl  "was  soll  die  Frau  als erste  Speise  gemessen?"  V.5.S0;  —  Ictm (ASn.)3>  haxa  ha^  "baraiti  (sd.)  Y.tfa.S; 20,4;  —  kJng  ä  vaiihSus  fimat  mananhd /isti/{s
10059:gehen,  sich  daran  machen  etwas  zu  tun' (Inf.):  yS  anyeÄe  dahmahe  hansma  *fra- st»r»nti  {sA.)  frajasaiti  li.104.  3)  mit antar»  und  Akk.  'hineinkommen  zwischen  — , unter  — ':  yim  antar»  vastr^m  frajasai yim antar»  shit»m  rätum  frajasät  "wenn  er unter  
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%
25131:•  j.  *'rapiOTwina- "  Adj.  (fem.  °«a-)  'den Rapiärwina  betreffend,  ihm  gebührend': kahmäi  haca  ^•'^winanqm''* gä%anqm  ratu- fris  frajasaiti  N.  49.
25873:bis  — ,  sich  erstrecken,  dauern  von  —  {haÜa mit  Abi.)  bis  -'  (Dat):  kahmät  haca  uSa- hinanant  gä^anam  ratufrii frajasaitii^A^  f haca  *maS)yayat  x!apai*ia  vaxlai  pairi. - sacäiti  ". .  sie  dauert  von  Mitternacht  bis Sonnenaufgang"  'Ü.46;  47,  49i  5^*41^'^')
28987:v^  tyä  Aacäma''  Aami%'iya  abavcC  Bh. 2.  2;  s,  ?.  5,  13',  5.  I.  i)zeiUich'\Qn. -  an,  inde  ab';  a)  im  jAw.:  ana  niam yasnayazaesa..A°  hU  vaxsa^ ä  Aufräsrnd.- diitsil  Yt.  5.  91 ;  —  kaAmai  A'  usaAinanqm gähantim  ratu/ri^  frajasaiti  N.  46;  *4y, *48,  4g,
```


## [2026-09-06T02:22:04.669Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### PHD\"; grep -n -i \"^gāh\\|gāh \\[\\|nyʾm\\|nyām\\|paygām\\|zamān\\|anǰaman\\|hangām\\|āmad\" PHD.txt | cut -c1-250 | head -30",
 "description": "MacKenzie lookups"
}
```


### [2026-09-06T02:22:04.729Z] TOOL RESULT

```
### PHD
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n
175:-üg [> | M Ze, N -a] suffix forming agent nouns from present stems. a-gàh [?g's] without rank. āgāh [?k’s | M ?g(h), N <] aware, knowing. ~ih: knowledge. ügahénidan, абваһёп- [A?^syn-ytn!] inform. ügandan, Agan- [’kn-dn' | P ?gn
247:~-gāh [-g’s] sleeping-platform, bench, couch.
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Ma
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. 
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym�
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. 
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATW
676:zamān 98 zāyistan
677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-,
859:ascendant ul-āmadān.
1282:come āmadan, madan; awar!;
1775:enter andar āmadan | šudan.
2327:hour zamān(ag).
2379:immediately hamzamān.
2791:message paygām.
2792:vidi aštag, bayaspān, paygām-
2963:occasion bar, jar, hangām.
3210:prescribed zamānīg.
3457:rise abar āmadan, abar àxistan, ul āmadan.
4017:time амат, bar, gah, hangām, jar, zamān(ag), zurwán.
4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām
5064:zardčūbug zam zamīg zamān zastan zafar zadar zadan zadüg
5502:dagrzamān
5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
```


## [2026-09-06T02:22:12.267Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gāh \\[\\|gāh\\[\\|hangām\\|nyām\\|niyām\\|paygām\\|anjaman\\|hanjaman\\|frazām\\|frajām\\|anǰaman\\|āmadan, āy\\|gām \\[\" PHD.txt | cut -c1-300 | head -20",
 "description": "PHD more lookups"
}
```


### [2026-09-06T02:22:12.335Z] TOOL RESULT

```
175:-üg [> | M Ze, N -a] suffix forming agent nouns from present stems. a-gàh [?g's] without rank. āgāh [?k’s | M ?g(h), N <] aware, knowing. ~ih: knowledge. ügahénidan, абваһёп- [A?^syn-ytn!] inform. ügandan, Agan- [’kn-dn' | P ?gnd, N ~] fill, stuff. a-ganj [Аис !] penniless. 
247:~-gāh [-g’s] sleeping-platform, bench, couch.
352:frazāmēnīdan, frazāmēn- [plc*myn-ytn!] = frazāftan.
353:frazām-pērēzīh [p/c”*m pylwcyh] final victory.
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audien
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh,
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanne
867:assembly hanjaman.
1296:community hanjaman; wālan.
1308:completion bowandagih, frazāmišn, hanjām.
1340:congregation hanjaman.
2083:gathering  čīnišn, ` harróbiin(ih); (group) gund, hanjaman.
2791:message paygām.
2792:vidi aštag, bayaspān, paygām-
2963:occasion bar, jar, hangām.
4017:time амат, bar, gah, hangām, jar, zamān(ag), zurwán.
4211:victory abarwézih, pērēz(gar)īh; final ~ frazām-pērēzīh.
4661:frazānagīh ^3» > O° frazanag 13 d o frazām $ à o frazám- -S à оу
4662:frazāmēn- - "edo frazāmēnīdan WO rā à o
4663:frazām-pērēzīh va eye à оу frazaftan we” à Q frazēn, parzin w Ф оу
```


## [2026-09-06T02:22:12.658Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### HRN\"; grep -n -i \"âmadan\\|āmadan\\|amadan\" HRN.txt | cut -c1-200 | head -20",
 "description": "Horn lookups"
}
```


### [2026-09-06T02:22:12.713Z] TOOL RESULT

```
### HRN
```


## [2026-09-06T02:22:19.353Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nprint(d[21][:3000])\nEOF",
 "description": "Horn page 1"
}
```


### [2026-09-06T02:22:21.041Z] TOOL RESULT

```
412
— XVI —
gaben der Wörterbücher über i/äi bezw. väV'i majhül oder
maräf; leider bezeichnen auch die jüdisch-persischen Bibel-
übersetzungen ebenso wie Muvaff'aq diese Vocale nur selten.
Da Vullers für eine ganze Reihe Wörter keine Be-
lege aus den von ihm benutzten Originalwörterbüchern
giebt und es daher öfter scheinen könnte, als sei eine
Vocabel selten oder ungebräuchlich, während sie ganz ge-
wöhnlich ist^), so habe ich in derartigen Fällen aus dem
Ferheng-i Residl (ed. by Maulawi Zulfaqär 'Ali
and Maulawi 'Aziz Urrahmän, Calcutta, 1875) und aus
Shams i Fachrii Ispahänensis lexicon persicum (ed.
Carolus Salemann, Casani 1887), als den zwei am
Bequemsten zugänglichen, gedruckten neupersischen Ori-
ginallexicis, Belegstellen angeführt. Dazu kommt noch der
V
F^erheng-i Jehänjgrrl, den ich in der mir mit grösster
Liberalität zur Benutzung überlassenen Handschrift der
hiesigen kaiserl. Universitäts- und Landesbibliothek ein-
sehen konnte. In der Anführung solcher Belegstellen hätte
Setzung ist ganz falsch ; auch dürfte ja nicht sir auf sir reimen). Auch
I, 225 Vers 1759 hat Vullers falsch corrigirt, doch bleiben genug
äusserlich ganz unverdächtige Yerse übrig.
Die philosophische Fakultät der Münchener Universität hat als
Preisaufgabe für das Jahr 1892/93 (nach den Zeitungsmitteilungen) *eine
systematische Zusammenstellung alles dessen* verlangt, Vas sich aus
den Endreimen in Firdüsl^s Sahnäme für die damals herrschende Aus-
sprache, vor allem ö und e betrefiTend, ergiebt*. Trotz der Beschränkung
der Aufgabe (ev. Ausschluss des Alt- und Mittelpersischen) auf eine
blosse, ^systematische , nach grammatischen, lexico-grammatischen Ge-
sichtspunkten geordnete Materialsammlung, um als Basis kräftiger
spraohvergleichender Behandlung zu dienen', dürfte ihre Bearbeitung
eben wegen der notwendigen Sammlung des umfangreichen Materials
für einen Studenten noch recht schwierig sein, zumal dieser gründlich
Firdüsl vorstehen müsste und sich nicht etwa auf die Leetüre der End-
reime beschränken dürfte. Ich habe selbst schon seit einiger Zeit für
eine ähnliche Untersuchung systematisch zu sammeln angefangen. Bei
dieser Gelegenheit erlaube ich mir zu bemerken, dass ich beabsichtige,
eine umfangreichere, aesthetische Arbeit über das SähnSme und den
epischen Stil der Perser zu veröffentlichen, zu welcher die Vorstudien
allerdings erst für den ersten Band der Leydener Ausgabe gemacht sind.
*) So ist Fr. Müller (WZKM. 5, 185) sogar zu der Meinung
gekommen, np. bh isteu sei uugebräuchlich.
```


## [2026-09-06T02:22:27.823Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kommen'\" HRN.txt | cut -c1-200 | head -20; echo \"=== gam ===\"; grep -n \"np\\. gäm\\|gäm  \\|gäm,\" HRN.txt | cut -c1-200 | head -10",
 "description": "Horn search kommen"
}
```


### [2026-09-06T02:22:27.905Z] TOOL RESULT

```
5429:kommen', wörtl. 'sich auf den Weg machen'?**)
5456:ftd' 'richtig, vollkommen' zu gehören (ursprünglich
=== gam ===
```


## [2026-09-06T02:22:32.939Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (33,34,40,44,45,46):\n    print('=== leaf',i)\n    print(d[i][:700])\nEOF",
 "description": "Horn find page 11"
}
```


### [2026-09-06T02:22:34.433Z] TOOL RESULT

```
=== leaf 33
12 -
49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen.
Im Awesta und Altindischen wird die Bedeutung
gnädig sein, verzeihen' durch das Wurzeldeterminativ
d aus der [/^merg- ^abwischen' gewonnen, vergl. aw.
merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
87, während Brugmann, Indog. Forsch. I, 171 auch
an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt).
50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis,
phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ;
lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum
=== leaf 34
13
umgekehrt osk. mo-, umbr. ero- jener' gegenüber ap.
aita-, aw. aesa-, skr. esd-. Die Dehnung des ä ist
speciell mittel-neupersisch.
Darmesteter's Etymologie (aus ap. aniya-) ist
falsch, denn ap. aniya- hätte im Np. kaum etwas
anderes als m oder in werden können. Zudem kommt
das Ideogramm "]; nur durch Nachlässigkeit der
Schreiber für aw. anya- vor; das letztere Wort wird
vielmehr regulär durch ""XDi wiedergegeben. Im
Ya^^nöbi hat sich anya- in Form und Bedeutung sehr
getreu bewahrt; hier findet sich ani mUi am andern
Tage*, any adam ein anderer Mensch', anyokai 'anders-
wo* (Salemann, Mel. asiat. IX, 234); vergl. auch
wa/. sar. yan anders* (Tomaschek, Pämir-Dial. 817).
Daneben ü in np. aö
=== leaf 40
- 19 --
76. ezdehä 'Drache'.
aw. azis dahakö; phlv. aze dahäk, arm. LW. azdahak.
arm. azdahak beweist, dass im Mittelpersischen az-,
nicht a/- gesprochen wurde; in jüd.-pers. xmiX ist z
nur ausnahmsweise durch i bezeichnet, während es
sonst durch T ausgedrückt wird *).
aw. azi' 'Schlange'; phlv. az; ai. ähU; arm. ?i'^);
minj. yiz selbst ist sonst im Np. verloren gegangen.
77. esp, esb 'Pferd'.
ap. Aspa[cana-, uv]aspa- fschöne Pferde habend');
aw. aspa- 'Pferd'; phlv. asp; ai. dgva-,
kurd. hasp; af>'. fls, aspa (fem.) 'Pferd, Stute'; oss.
d. äfsä, t. yäfs 'Stute' (41); bei. aps, haps (LW. asp)
(4); wa;K. yas, minj. ydsap, yasp,
ap. asa[hara' und np. es[^^r (No. 86) stützen sich
gegenseitig un
=== leaf 44
OQ
94. efrö^/ten anzünden, erleuchten', Praes. efröz-em^
ewrö/fen [heme-werözT AM. 239 Zeile 1 v. u.), jn5n5N,
furö/ten, furözis^ furöy etc.
aw. aiwi + [^ruc- 'anzünden*; phlv. afröxtan,
a/röcmn, afröcimtan ; skr. abhi + [/'ruc- 'leuchten'.
kurd. vergl. ci]rüstin 'leuchten', dici\rüsi (3. Sg.).
95. ef%är 'Werkzeug', ewzar 'Organ' (AM.).
phlv. afzär 'Werkzeug, "ITZN (Talmud).
Zu ai. 1 V^hur-, Nöldeke, ZDMG. 32, 408.
96. efzuden 'zunehmen, vermehren*, Praes. efzdy-ew,
eirzäden (AM. ; hah-wezäi, 235 Zeile 2), fuzüden, efzün^
fuzün^ efzayis etc.
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^a
=== leaf 45
— 24 —
102. ef San den ausschütten', ^'sawrfew.
aw. aiwi + ßünayeinü *sie weiden aus , yt. 14, 56
(Geldner, 3 Yasht, 88) (?); phlv. aßäntan,
103. ef gen den 'wegwerfen', ßgenden^ ewgenden (AM.),
jn::5x (Is. 14, 12).
Kaum etwas anderes als aw. aiwi + [^kan-, wenn-
schon die Bedeutung nicht passt; phlv. afgantan
(Bund.) 'wegwerfen'.
Ein ganz anderes Verbum scheint efgenden, ewgenden
einfüllen, auffüllen zu sein, vergl. AM. 82 Zeile 1 *in
die Harnröhre einführen, einfüllen , 145 Zeile 3 v. u.
'in die Nase einführen, einfüllen* u. ö. (mit und ohne
bäz, letzteres z. B. 50 Zeile 4)^). Post häz ewgened
bei demselben Autor ^bewirkt Abschuppung der Haut'
(140 Zeile 2) gehört natürlich zu efgenden weg
=== leaf 46
— 25 -
105. eknün jetzt', kunän,
ap. *kanüna7n, vergl. nun (No. 1052).
106. eger wenn , egerdi^ ger,
Zusammenhang mit phlv. akarc, np. hergiz (No. 1092)
ist wohl unzweifelhaft; päz. agar,
Ap. %akaram 'ein Mal', Darmesteter, Et. ir.
I, 245. Vergl. Fr. Müller, WZKM. 5, 66.
107. em *ich bin etc.
ap. amii/ 'ich bin' ; aw. ahmi ; phlv. nin -\- am etc.
(päz. hom etc.); ai. dsnii; arm. em (H. No. 93).
kurd. im etc. (Justi, S. 240); af^'. am, yam etc.
Wohl nach hest (vergl. No. 1094) und ap. ha(n)tiy,
aw. henti, ai. sänti: est sind dann auch die anderen
Formen des Praesens mit anlautendem h versehen
worden : päz. hom^ liend (Men.) — übrigens könnte hier
auch der Anlaut des aramäischen mn mitgewirkt
```


## [2026-09-06T02:22:39.666Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[32])\nEOF",
 "description": "Horn page 11"
}
```


### [2026-09-06T02:22:41.263Z] TOOL RESULT

```
- 11 -
44. äleyten 'springen, ausschlagen (vom Pferde)*, Praes.
alezed^)^ alezende^ alezTden^),
got. laikan springen, hüpfen*, laiks Tanz'; lit. laujytl
*wild umherlaufen (von jungen Pferden, Rindern auf der
Strasse)*; air. löeg 'Kalb*, (bei Feist).
kurd. helezium 'ich tanze*, lizim 'ich spiele', Inf.
leiztin.
Die Etymologie stammt von Justi, Dict. kurde-
frangais.
45. ätnäj 'Pflugsterz'.
g. matk (Houtum-Schindler, ZDMG. 36, 70).
arm. mac (de Lagarde No. 1413, Htibschmann
No. 186).
Die Lautverhältnisse von äinaj und mätk passen
nicht zu einander (vgl. auch Bartholomae, Studien
II, 24).
46. ümäden 'zurecht machen, rüsten*, ämUden, Praes.
ämäy-em, ämüy-em,
ap. vergl. ämäta- erprobt*; aw. ämata-, ämayäont^^
sie sollen sich versuchen',
oss. t. amain 'erbauen' (176).
47. äniär 'Berechnung', ämäre,
aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
skr. a + V^smaV" (nicht belegt).
48. ätneden 'kommen*, Praes. äy-em (s. No. 60).
ap. ä+ [/^gam-, äjannya 'er käme*; aw. ci+ [/'(/am-,
ägemat; phlv. nrntan, ämatan (PPGl.) ').
Mit Mahjalvokal (FJ.).
^) FR hat einen Beleg aus Siräj eddin:
(Metr. Xeftf)
tie/s^ cun ser^ gesf bestezed
tevsen-äsä beher süy älezed.
*) Beiläufig bemerkt, findet sich bure als Imperativ *komm* ausser
im Kurdischen (Houtum-Schindler) und bei Shukovski dialektisch
auch bei Bäbä Tähir *Uryän aus Rei (Huart, Journ. asiat, Si^me s^rie,
vol. VI, 519).
```


## [2026-09-06T02:22:53.229Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"گام\" BQT_v1_pages.txt | head -5 | cut -c1-200; echo \"### v1 page 434 lookup\"; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nprint(pages[1][:300])\nEOF",
 "description": "Check BQT v1 structure"
}
```


### [2026-09-06T02:22:54.915Z] TOOL RESULT

```
217:۵۳ ۲۰۱۵0 ج) درهنگام اقامت چند روزرَء خود دراه مارس ۱۷۵
286:اينکه اوستا در هنگام تاخت وتاز تازیان و پس از آن دریورش مفول وتتار
1811:التتوی بسال ۱۰۲ درهند نوشته بعنی‌درهمان‌هنگامی که محمد حسین ین خلب
2097:آبادی عالم لغوی معروف متوفی‌در ۸۱۷ هنگامی که کتاب قاموس البحیط را
3692:جواب قطعه های جوهر و فدا هريك دو قطعه سروده اند . در همیت هنگام
### v1 page 434 lookup
777
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
بسرمایه کنابفروشی اب
```


## [2026-09-06T02:23:08.349Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'));import sys\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"; echo \"=== tool ===\"; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/ref_page.py",
 "description": "BQT offsets and ref_page tool"
}
```


### [2026-09-06T02:23:10.027Z] TOOL RESULT

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
=== tool ===
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


## [2026-09-06T02:23:19.729Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nimport re\ndef getpage(f,tag):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for p in pages:\n        if f'[pdf page {tag}]' in p:\n            return p\n    return None\nfor f,pdfp,label in [('BQT_v3_pages.txt',560,'BQT:1765 gām'),('BQT_v3_pages.txt',566,'BQT:1771 gāh'),('BQT_v3_pages.txt',568,'BQT:1773 gāh'),('BQT_v3_pages.txt',246,'BQT:1451 farjām')]:\n    p=getpage(f,pdfp)\n    print('=========',label)\n    print((p or 'NOT FOUND')[:1500])\nEOF",
 "description": "BQT v3 pages"
}
```


### [2026-09-06T02:23:21.746Z] TOOL RESULT

```
========= BQT:1765 gām
[pdf page 560]
۱ ۷۹۳-

eee » ‏دار‎ abet ‏بکون زای‎ = JP
‏و لب باعضو دیگر را بدندان‎ - Vast ‏دندان‎
‏که‌بدان‎ AT, - ‏کرفتن وخاییدنرا نیز گوبند؟‎
‏ببرندگ - و مقراض‎ UT poy ‏ونقره ومس‎ WE
Pas ‏راهم گفته انس ومنقاشی که باآن‌س‌شم عکیر‎
‏وموی چینه را هم گفته‌اند © (۱) — وعلف‌چاروا‎
‏را بیزمیگویند ۷ - وبمعنی اخذ وجرهم‌هست.‎
‏ومفارة کوه را نیز گفته اند ۷ - وجایی‎ Hey
‏وسوراخیر! نیز گویند که د رکوه با درزمین‌سحرا‎
‏بکنند تادر وقت ضرورت آدمی _ با گوسفند در‎
‏آنجا رود - وصومعه را هم میگوبند که درس‎
‏تازی‎ GL ‏معنی‎ on ‏؛ و‎ Vash ‏کوه ساخته‎
. ‏آمده است‎ ۳
ASW
Te ‏جا ومقام باشد‎

گازركگ - صفیر کازر است - و

پرنده‌ای‌را نیز گویند که پیوسته در کنارهای آب
نشیند ودم خود را جنباند وبر زمین زند وعربان
صو هکویندش .

(۱) خم : ی زگویند .

(class) BAZ SL. ۱

‎hh OS ©‏ فارسی » بمعنی

‏۴ - باین معنی« ‎SW‏ 5 استعمال شود.

‏گازه
‎ISU”‏ گاه - نام ‎col page‏ درشیراز

‏که‌شیخ‌سعدی‌علیهالرحمه درآ نجاآسودهاست٩‏ -
و نام مقامی ‎col‏ در هراتکه خواجه مدا

‏انصاری در ‎lat‏ مدفون است +

‎OSU”‏ » بروزن تازه 1 زسمالیراکویند
که در روزهای عید وجشن از بام ‎ale‏ با شا
درخت آویزند و برآن نشینند و در هوا ‎wal‏
‏وروند ‎YY‏ وریسمانیرا یز گویند که‌دوشکیرابر
‎oT‏ نعبیه کنند و اطفال را در ‎OT‏ خوابایده
بجنباتند تا بخواب رود و ‎UT‏ صربی ارجوحه
خوانند*۱- و ‎LG‏ فالیز بانرا هم گفته اند که در
صحرا از چوب وعلف سازند۱9- وشتگاه‌چوین
را گویند نی خاله‌ای که از چوب وتخته‌سازند
‎Masts We LT,‏ و ‎yaw‏ کمیتگاه سیاد
باشد که از شاخ‌درخت سازند ودرعقب ‎eT‏
‏تا صیدش له بیند وآترا آفتاب خانةً سیاد هم
میگویند۱۱- وصومعة س رکومرا 55 کفته‌اند۱۱؛
و
========= BQT:1771 gāh
[pdf page 566]
۱۷۹۹

هم هست سبز رنگ شببه بل .

او ذهیی- کنابه از آن قوتی است
.که خدای ‎Js‏ در ‎Sp‏ زمین خلق ‎oS‏
‎aa‏
‏"1959 = کی را ‎SaaS‏ بی
ورزش کشتی گیری و ریاشت آموختن فنون آن
در ‎cule‏ زور وقوت باشد .

گاوذهره - سنگی ‎dan Sash‏
زهرة کاومتکون‌شود ‎savy‏ گویندرمیان‌شیردان
کاوبپم میرسد و آن در لون و خاصیت مانند
پازهر باشدوبعربی حجرةالبقر خوانند؟ ؛وه‌مرب
آن جاو زهرج ‎oy‏ و آن سنگه نیز در گوسفند
‎cal‏ شود و آن مانند زرد تخم مرغ زرد

است

میباشد؟ - ویمعنی‌پددل هم‌آمده اس ت که بعربی
‎an Sole‏ .

‎Wm FIL UP‏ سین ‎gg‏ نقطه بر وزن
کارزار . بمعنی ‎BBL IT‏ آست‌چه ساربمعنی مانند
باشد - وبمعنی کاوچهر نیز آمده اس ت که کرز
فریدون ‎col‏ وآترا از آهن ‎pole‏ گاومیش
ساخته ‎Sarg‏ .

‎SUP‏ ساهری = ,کرتالت. کاوی‌بود
که سامری زر کر از طلا ساخته بود و شرح

‏)0 چش : کاوسر () .

‏کارش نه لیسیده

‏وسط ‎OT‏ در لفت کاوزر (۱) ‎Lat Se‏ .

‏گاوسر۷- بروزن دادگر » بمعنی
کاوساراست که کرزفربدون باشد وآترا کلوسره
هم گویند با زیادتی ها درآخی +

‏اف سفالین- سراحیرنظرفیرا گویند
که آنرا از سفال ‎Wale‏ ساخته باشند .

‎» Gy oT ‏بر وزن‎ » Re
‏زهره گوبند و بس‌یی‎ IT ‏سنگی باشد که‎
‏حجرةالبقر خوانند ۸ - وچوبی را نیز گفته اد‎
‏که کاو را بدان‌رانند ۰ وباین معنی‌باشین شطمدار‎
۰ ٩ ‏مم آمده ات‎

‎SUP‏ یمین - سراحی رثرفیراکوبند
که از نقره صورت کاو ساخته بائند همجنانکه
کاو زرین را از طلا -

‎iol”‏ 5 با شن تقطمداربروزن
‎oT‏ رنگ , چوبی باشد که برسرآن ‎Mee‏

‏آهن صب کنند و خر وکاوبدان رانند. ووجه
‎Ls‏ آن کاو تند کن‌باند چه نگ بمعتی‌نند
° آمده است +

‏گاوش نه لیحیده(۲) - ‎Ses‏
‏کنایه کیرا کوبند که عجب‌رتکبری داردوسخت

‏وست روز
========= BQT:1773 gāh
[pdf page 568]
۱۷۷۱
‎OPIVP‏ ه با زای ‎abs‏ دار بر وزن
ایدن,زهرة کار راکویند. چیزی با مد
سنکه وآن‌از زهره کاوبرآید چنانکهحجر التیس
از زهر؛ کاو کوهی بر میاّید و رنکه آن مانشد
زرد تضم مرغ باشد. وچون از زهره کاو برآرند
‎op oy‏ واندك زمانی که در ده گیر ند سشت و
محک‌شود وآنرا ‎Byer‏ زهرء کاو هم میگوبند و

معرب ‎OT‏ جاویزن باشدا .

گافا یس - با اك بتحنانی کنید»
و ‎es‏ بی ‎ed‏ زده . ظرفی را کون دکه شیر
ودوغ ذر آن کنند ؛ وبا شین نقطه دار هم آمده

۱ - رك :کاو زهره ‎WT‏ سنگه .

گاهبارها
است ۴ .
گاه = بر وزن ماء . تخت پادشاهان
وکرسی زرین را گوبند ۴ - وبمعنی وقت‌وزمان
باشد ۴ وبوته‌ای که ‎Wh‏ و نقرء وامثال ‎OT‏ درآن
بگدازند ۵ ب وصبح صادق را لیز کوبند-وبمعشی
جا و محل و مقام هم هست لیکن باین ععنی
بدون تر کیب کفته مشود" همجو بار کامولشکر
گاه وخیمه ‎Ol ats AT‏ - وستارٌ جدی را هم
‎pte an Ce‏ چیم ۷ وآن ستاره ‎cal‏ نزديك
بقطب شمال «
‎Absa?‏ - با رای قرشت بروزن

۴ -آیا مصحف* کاو دوش*نست؟ «دهخدا؟.

در خراسان « کاودوش» گونند ( ظرف شیر دوشیدن ) > فرهنکه نظام» . د رکناباد 005 ‎gaw‏

( ظرف دوشیدن شیر ) ۶ کنابادی © ۰

؟ - پارسی ‎gathu - ott‏ )> مکان »

تخت) , اوستا - 88101 ( جا » تخت ) ؛ پپلوی 885 ۰ حندی باستان - 84 ‎eal)‏ روش) ©
‎ual‏ 80121 - «استق ‎cane‏ ارمنی ‎Bah‏ (تخت » کرسی ‎(Ay‏ هوبشمان ۸۸۹ نیز در
اوستا ‎gathu‏ ابرانی باستان - 8۵1011 «بارتولمه ۲۵۱۷ «نب رکه ص ۷۸ - ۰۷۹ .

۴ - باین معنی هم بصورت اسم ‎Tiles‏ : گاه ‎lane‏ گاه کوشش؛ وهم بصورت پوند

زمان : سحرگاه » صبحگاه 6 شامگاه .

‎٩‏ شپان ز خدمت‌او ازعوار ‎db‏ شوند

‏۱ ره :دح .

‏برآن مثال که سیم گداخته درگاه.
«فرخی ‎Joe‏ ص۳46٩‏ .۰

‏۷ - باين ععنی د
========= BQT:1451 farjām
[pdf page 246]
—~\ter—

مم درست است .

ف رخجسته ۱ - بن ناك ‎chs‏ جم
و سکون سین ؛ بمعنی مبارك و میمون ‎Fath‏ -
ونام نوعی از کل است (۱) - و مطرب وسازنده
را نی زگوبند .

فرخجی ۷ = بفتح اول وثانی‌وسکون
ثالت وجیم بتحتانی کشیده ۰ بمعنی پلشتی وزشتی
وزبونی وبدی باشد .

فرخخ دود ‎che‏ اولون‌نیانشدید
و سکون تالت و رای بی‌نقطه بواو کشیده وبزای
نقطه‌دار زده ۰ نام پرد‌است ازموسیقی وصونی‌از
مصنفات باربد . و بقول شیخ نظامی نام‌لحن‌بست
وهفتم است ازسی‌لحن باربد .

‎O19 ES‏ - با زای قطه‌واربالف کشید.
و بدال بی ‎Abe‏ زده ۰ بمعنی مبارك زاد باشدچه
فرخ ‎om‏ عبارك آمده است - و نام فرشته‌ای‌هم
— موکل بر زمین +

‏9 خسته = بفتح اول والك بروزن سر

‏(۱) چك : کلست .
)£( چك : قطائف .

‎. ‏چك : قطائف‎ (x)

‏فرخشه

‏بسته » بمعتی خنته و برزمین کشیده باشد؟ .

‏فرخش * = بنتح اول و تانی بروزن
بدخش ۰ بمعنی کفل اسب واستر و کاو و دبگر
چهار پایان باشد .

‎GSS‏ = بروزن ب رکشته » نانی‌باشد
کوچك که از خمیر سازند و درون آنرا از مغز
بادام و پسته و لوزینهای ‎Sar‏ پر ‎PES‏ برروی
تایه پزند و شیر قند بر ‎OT‏ ربخته بخورندو آترا
بعربی قطابف(۲) خوانند ‎٩‏ - و بمعنی ‎ors‏
‏کشیده هم‌آمده است ۷ ۰

‏فرخشور ۸ = بفتح‌اول‌وثانی‌بروزن(۳)
سقذقور . پیفمبر و رسول را گویند .

‏فرخشه * - بفتح ‎Jal‏ وثالك و رابع»
بمعنی فرخشته است که نان کوچك پر مغز پسته
ولوزینه ‎ath‏ ؛ و بستی گویند نانی است که از
نشاسته و لوزینه پزند و بمربی قطیفه خوانند
و پضی دیگر کوبند فرخشه ‎a)‏ قطایف (4)

‏است .

‏(۳) چك : بوزن .

‏۱ - از : فر (پیشوند) + خجته ‎Cen)‏ اسشق ۸۰۷ .
۴

‏- این غم ‎Jo‏ برد يك ره ‎Ope‏ هزیمت کشت برد

‏فر خسته فر فروردین پدید آورد ورد .

‏: فرخج
```


## [2026-09-06T02:23:34.786Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n \"فرجام\" BQT_v3_pages.txt | head -10 | cut -c1-150; echo \"=== pdf page tags near ===\"; python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor p in t:\n    if 'فرجام' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('pdf page',m.group(1) if m else '?', '-> printed ~', int(m.group(1))+1205 if m else '?')\nEOF",
 "description": "Find farjām in BQT v3"
}
```


### [2026-09-06T02:23:36.445Z] TOOL RESULT

```
17742:بکوشیم و فرجام کار آن بود
=== pdf page tags near ===
pdf page 244 -> printed ~ 1449
```


## [2026-09-06T02:23:42.067Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; grep -n -i \"fraj\\|frazam\\|hanjam\\|hanjaman\\|anjuman\\|hangam\\|niyam\\|paigam\\|payghām\\|gama\" BQT_v3_pages_faseng.txt | head -20 | cut -c1-250",
 "description": "Latin etyma in BQT v3"
}
```


### [2026-09-06T02:23:42.144Z] TOOL RESULT

```
ugrep: warning: BQT_v3_pages_faseng.txt: No such file or directory
```


## [2026-09-06T02:23:45.572Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; ls; echo ===; python3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (245,246,247):\n        print('#### pdf',m.group(1))\n        print(p[-1800:])\nEOF",
 "description": "Print BQT v3 pages 245-247 tails"
}
```


### [2026-09-06T02:23:47.361Z] TOOL RESULT

```
Exit code 1
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
(eval):1: == not found
```


## [2026-09-06T02:23:50.701Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'PYEOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (245,247,248):\n        print('#### pdf',m.group(1))\n        print(p[-1600:])\nPYEOF",
 "description": "BQT v3 nearby pages"
}
```


### [2026-09-06T02:23:52.453Z] TOOL RESULT

```
#### pdf 245
س‌اولوضمالی‌وسکون
‎ott‏ وفوقانی ‎Dk‏ کشیده و برای قرشت زده »
بمعنی فروشندهباشدیعتی شخ که‌چیزی میفروشد.

‏فرخچ ۸ ‎gly Jl pe‏ و سکون
‎elt‏ و جیم ‎ould‏ کفل اسب و دیگر حیوانات
را گوبند - و بمعنی زشت و نازیبا هم کفته اند
— و بععنی رشوت و پاره نیز آمده است ؛ وباجیم

‎farxar - ۱‏ فارسی ( بمعنی ‎po‏ ومعبد (بتخانه) ) از ‎U5‏ سفدی ‎Brgh’r‏ مأخون
است ( .500 ‎oT, ) Gauthiot,JA.,1911,[,pp.53‏ خود از2 ۷108 سانسکرت کرفته
شد که اين کلمه خود در فارسی بصورت « بهار © درآمده ‎ty.‏

‎Henning, Sogdian loan— words..., BSOS.X.1, p. 94.

‎(Bargh4r) farkharus ‏فقه‌اللفه‌کمة‎ bod ‏از‎ : aig cosy ‏مینورسکی باستناد قول‎

‎canis‏ ۷102۳2 مرتبط ‎cos‏ بلکه‌کلمه‌ایست ایرانی‌ازربتة ‎paru - xuvathra‏ ® ( پر
از شادی ) . ركك : .7-8 ,]2024 , 1928, ‎Benveniste, Bull . Soc. Ling.‏

‏« میلورسکی . حدود ۷۹۳ ح ۷ >

‏۴ « فرخار بز رکه > در تبت است . مولف حدودالمالم در « سخن اندر ناحیت تبت و

‏شهر های وی » آرد : «کرسانك از تبت است و اندر وی بتخانه‌های بزرگه است » آنرا فرخار
‎Sy‏ خواشد > « حدودالمالم > 4۸ > وآن در ‎col Lhasa‏ « میلورسکی. حدود ‎۲٩۳‏ > .
ونیز فرخار نام شهریست در طالقان ( ماوراءالتهر ( « حدود . میئورسکی ص ۳۳۰ , ۳۵۰ > -
لترنج ‎(ta)‏ کوید : در میان شهرهای ختل . یکی فرغان با فرغار است که در کنار رودی

‏بهمن نام جای دارد . ۴ ‎(pa) Gent‏ ۴ - مسحف « فرخال >
‎=e‏ فرخواکه (هم) . ۱ - «سبط . فرخال » ( السامی‌فی‌الاسامی چاپ
تهران ص ۱۹) :

‏زلف فرخالت ز سرتا پا گرفت.
فیروز مشرقی «فرهنگه ‎tells‏
‏فرخش ‏ پرخج ** پرخش ‏ «فرخج»

‏سرو ‎gee‏ ترا در مشك تر

‏۲ ۳ مخفف « فروختار © ‎=A Cem)‏
فشره بود بعنی پلید وزشت . لبیبی گوید :
ای بلفرخج ‎ol‏ همیدون فرخج نامت فرخج و کنیت ملعونت بلفرخج >
« لفت فرس ‎٩۰‏ ورك :ص۷۳ > ورك : فرخجی .

#### pdf 247
P‏ ممدوله ‎iE,‏
‏فارسی_بروزن افلاك , قلیه و گوشتابه را گوشد
که بر بالای آن تخم مرغ بریزلد و بخورندچه
فر یممنی ‎Ve‏ وخواکه تخم مرغ‌رااگویند.

‏8 خود - با واو ممدوله بروزن‌صرص,
گنر گاءآب راگوند - و بر وزن )0( فنفور.
هم بمعتی گذ رگاه آب باشد و هم ‎sed hee‏ را

‎ALS ‏و آن پرندء‌یست کوچکتر از‎ ue
‏پفتح اول و سکون انی‎ ٩ ‏فرخوی‎

‏وضم ‎Ell‏ و سکون رابع و تحتانی » بمعنی‌خلق

‏نم خذای نفطه‌دار() باشد و اخلاق‌جمع آلست.

‏فر خو یفن ‎٩‏ - بفتحاولوناك‌وسکون

‏(۱) چك : بوزن . ‎)٩(‏ چش : نمود . (۳) چك : بوزن .

‏(6) چك :- ابجد . )0( چك : بوزن . ‎)٩(‏ چك : منم خا .

‎Coe) ‏رك : فرخمیدن . ۴ ه فخیدن‎ ٩
: ‏اسدی (طوسی) گوید‎ ath ‏فرخنج ؛ صیب‎ « - ۴
. ۷۳ ‏مرا از توفرخنج جز درد نیست . چومن سوخته درجهان فردنیست.  " لغت فرس‎
.۳ ۲۹۵ ‏صفت ) اسر . تبعات‌ج ۱ص‎ plete) andes!  عرف ‏از‎ ۴
ep: ۳ ‏ی‎ Sas ۸ ‏قی ۰ فرخ « اسشق‎

‏۵ خرم‌آن فرخنده طالم را که چشم بر چنین روی اوفتد هر پامداد".
> گلتان ۱۶0 ©
‎٩‏ < پرخو (هم.) , رك : پرخویدن ...۰ ۰-۷ فرخو, پا کردن کشت و باغ
‎oy‏ . لبیبی گوید : .

‏مر کشت راخوافکن بیرو ( خودافکن نبرو. طبق ‎he‏ بعنی‌قوت ورشوت و کوت.دهضدا)
زر را ( رز را . دهشدا ) باست خودکن فرخو. » « ‎cal‏ فری ۸۱۳ *.
۸ - 121۴۷88 » بادآور سقدی ‎frxw’k‏ است که از-1781322 ( تکه‌تکه کردن,
بقطمات بربدن )آمده. ‎chy‏ فرهنگ پارسی‌میانه بسغدی چنین آمده : پارسی ‎m= ‘skangul.‏
‎frxw’k sax‏ ( رك : 59 . ‎Manich. Bet- und Beichtbuch , p‏ ) [رك: اعکند]
معنی اصلی سفدی ‎fraxwak‏ و پارسی ‎ishkanag ot.‏ چنین ‎oy‏ ( چیزی پربده با شکسته
بقطعات کوچك ودر آش (با آبگوشت ) گذاشته ‎Henning , Sogdian loan-words...,(‏
‎BSOS.X.1,p.99.‏ ورد : فرخاکه . ‎٩‏ - از: فر ( پیشوند ) ۲- خوی ‎Gem)‏
‏۰ - از : فرخو ‎(pm)‏ دیدن ( پسوند مصدری ).

#### pdf 248
( وندیداد ‎J‏ کرد ۳ بند ۱۸ ‎oS Bt‏ ه بند 44 ) وآن مرکبست از دوجزو : پیشوند 02151
با 07 بمعنی کردا گرد وپیرامون ؛ دوم 18622 از مصدر 4262 یمعنی انباشتن و روبپم‌چیدن
و دیوارگذاشتن . در زمان هخامنشیان » در ایران زمین بزرکک و درسراسر قلمرو آنان بنصوس
درآسیای صفیر پلیری دثزها - یا فردوسها - که باغهای ‎AL yy‏ های با شکوه پادشاه
و ‎bash ts‏ ( حاکمان ) و بزرگان ابران بوده ۰ شبرتی داشت . این محوطه‌ها چنانکهسکرر
کزنفون ( در « کورش‌نامه » وه انباز ‎Ce‏ و پلوتارخس مینوبسند درختان آنبوه وتناور داشتندوآب
در ‎Tole‏ نها روان بود . چارپابان بسیار برای شکار درآنها پرورش می‌بافتند. شاهنشاهان هخامنشی
خثشرپاونهای خود را در ابجاد اینگونه باغها در فلمرو حکومت خود تشویق میکردند . اینگوله
پار کها که در سرزمین ونان وجود نداشت ‎pW SG‏ انظار بونایان را متوجه خودکرد وآنان نیز
همان نام ایرانی را صورت ۵2۳8061505 بکار بردند . در اکدي متأخر ‎Pardisu‏ و در عبری
‎pardes‏ ( پارك با باغ ) و درآرامی وسربانی نیزهمین‌کلمه با ‎Sail‏ تفاوتی و در ارمتی۵۳088
) باغ ) همه از ربشة ایرانی هستند ‎LI.‏ « پاردس» در زبان عبری پس از مهلجرت بهودیان‌ببابل
در قرن ششم ق.م. بعاربت کرفته شده وچندین بار در قسمتهای مختلف توراة بکاررفنه . دربخشهای
قدیم توراة - یمنی آن قسمتی که پیش ازفرن پثیعم ق.م. لوشته شده بهشت ودوزخ مفهوم‌روشن
وصریحی ندارد ‎UB.‏ فردوی که ‎hy‏ در فرآن‌آمده » از ‎op‏ بپود وعیسوی باسلامرسیده‌است
‎ol pie‏ قرآن ‎litte‏ فردوی ‎Ny‏ بمعنی ‎alas Sot, bb‏ , اما اختلافشان درین !. مت که نج
نوع باغ و بوستان با جنت و ‎clade‏ .گفته شدکه درتوراة چندین بار ۳۵۳65 عبری بکار
بقیه درصفحهٌ ‎NEON‏

‏۵ فردا - بفتح اول وسوم پردا («.م.)؛ پهلوی ‎VN Sy rfratak‏ شهمیرزادی

‏5 .«که. ۰۰۱۹۹۲ گپلکی 137186 : روزآباده - روز ی که پی از امروزخواهدآمد.
```


## [2026-09-06T02:24:00.955Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'PYEOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (243,244):\n        print('#### pdf',m.group(1),'printed ~',int(m.group(1))+1205)\n        print(p)\nPYEOF",
 "description": "BQT farjām entry"
}
```


### [2026-09-06T02:24:02.471Z] TOOL RESULT

```
#### pdf 243 printed ~ 1448
[pdf page 243]
فربود
8 99 ۱ ۰ با بای ابجدبروزن‌فرموده
یمعنی راست ودرست ‎ath‏ چه فربود کیش‌وفربود
دی نکیرا گونند که در کیش وملت ومذهب‌خود
راست ودرست باشد .

فر بودگ ؟ = بروزن‌امودی ‎ine‏
‏فربود دین است ‎TOT,‏ باشد که دردین وملت
خود ‎cl)‏ و درست باشد .۷

‎wr‏ ۴ = بفتح اول وسکون انی‌وبای
ابجد بتحتالی‌رسیده. بمعنی فربه باشد که‌درمقابل

‏لاغر است .

‎Foss‏ با بای ابجد . بر وزن
ومعتی فرفیون است » ون داروبی باشد دوابی.

‏وا

‏فرت ‎oie‏ اول وسکون ثالیوفوفانی»
تانه و تارهای جامه ‎ath‏ که جولاهگان بجهت
یافتن آراسته و مرتب ساخته باشند - ‎ping‏ اول
گیاهی است که درد شکم را سود دارد وروشن
کردن و صاف کردن دل را نیز گویشد بربانت
وطاعت و آنرا بعربی مجاهده خوانندث .

‎۳ air ۵

‏فر ناش.۱ ح_باتای‌قرشت بروزن‌پررخاش»
بمعنی وجود است که در برابرعدم باشد .

‏فر نوت ۲ = بانای‌فرشت بروزن‌مر ‎shy‏
‏پرسالتخورده وخرف شده واز کار رفته را گوبند.

‏فر وث 4 = باواومجپول بروزنمحمود,
‎aw‏ فرتوت است که پیرسالخورده واز کارافتاده

‏وخرف باشد .

‏چون ب رگز ند گی‌جانورانوسکگ دبوانه طلاکنند
فر ود * - بنتحاول ‎lt‏ وسکون‌انی

‎. ‏باشد‎ gl

‎fraybut ۰ ‏مناعت ؛ تکیر « تاوادیا ص۱۸۱‎ caw fre - DOL ‏در پهلوی‎ ٩
, . ‏کیوان است‎ ST BS Lay ‏متن‎ Cove ‏(کترت . افراط ) « مناس‎

‎= frapth sale < ‏رك:فربود . ۴ - ازاوستا -2 2۳00100۷ = فربی‎ - ۴
۰۷۹۱ ‏شکند گماندك‎ « ) Sle . ‏(فربه‎ Pit sol. = padh ‏فی پازند‎ .ofrapithwa_? ‏ایستا‎
‏اسشق‎ « farbé ‏باستان - ۳۳۵810۷ , وخی ع 82۳01 , سریکلی‎ sae . ۸۱۳ olay?
Henning, A list of Middle persian..., ) ‏(چاق‎ frhyw ‏در اوراق‌مانوی‌بپارتی‎ ۳
BSOS,IX, |,p.82.

‏= فرفبون ‎(pe)‏ = افریون » عربی ازیوتاتی ‎Euphérbion‏ ذ عقار ۰۲۵ .

‏۴ - فریبون (جم‌اول) = ‎cévadille‏ (فی) ‎crave‏

‎٩‏ - در فرهنگه ‎le‏ « فرتود » بممنی روشن ساختن دل و ‎hake‏ قلب است برنج و
ربانت و پرستش ‎Ob py‏ که بتازی مجاهده کویند و ‎Leg‏ لفظ اتراقمت چه حکیم اشراقی را
+ فرتودی » گویند . از ‎whe‏ این ممنی معلوم و مرقوم گردیده (۱) « فرهنگه دسائیر ۷۵۹ ۰ .

‏-ظ . ‎ALS STS) SL,‏ . ۷ فرنود ! کردی ع 070066] (عجوزه)
‎LIS?‏ س ۲۹۰ » «فرتوت . سخت پیر و خرف باشد . رودکی (سمرقندی) گوید :
دولت او مرا بکرد جوان.» ‎cal?‏ فری 90

‎(pe) og pm A‏ قس : توت تود : « یکی را زنی صاحب جمال جوان در گذشت
و مادر زن فرتوت بعلت کابین درخانه متمکن بمالد. » «کلتان ‎VEE‏

‎«٩‏ فرتور ؛ عکس بود شم

‎.» ۱۹4 ‏می از قدح: فتاده برسفف سرا چوآب روشن. » « لت فری‎ od
‏این‌کلمه. (پرتوی می ) [با: قرتو می بکسر واو. مم. ) تبوده وغلطخوانده‌شده‌است؟ (دهخدا).‎ LT
+ td : ‏بفتح اول وکسرسوم » رك‎ ado

‏پیر فرتوت گشته بودم سخت

‏) برهای قاطع ۱۸ )

#### pdf 244 printed ~ 1449
[pdf page 244]
60۱

و رابع و رای قرشت » بمعتی عکس باشد؛ و با
رابع‌مجهول بروزن مخمور, یز همین معنی دارد
که عکس باشد .

‎J‏ وگ ۱ = ‎dle ain‏ بمه‌نی
بر-تواست و آن‌مرغی‌باشد که بعربی‌خطاف ‎A SF‏

‏فرج © بنتح اول؛بروزن ومعی ارج‌است
که بمعتی قدر و قیمت و مرتبه وحد ‎Fath‏ -
ودرعربی‌بمعنی شکافتن و وابردن اندوه - وشکاف
چیزی - و سوراخ پس وپیشآدمی- وجای ترس
‎gee‏ - وما ‎ow‏ هردو پای اسب باشد ۴ .

‏فرجاد ۴ ‎ele‏ بروزن فرهاد »
بمعنی فاشل ودان#مند ‎atl,‏ 2

‏فرجاد - با جیم . ممرب‌پر کازاست 8
‎Tol,‏ باشد که ‎Oly‏ دابره کشند.

‏5 جام 1 ه بروزن و معنی انجام‌است
که ‎aes‏ انتها وآخر بائد .

‏ف جامگاه ‎GEL oo‏ فارسی بر وزن
بهرام شاه ۰ به‌عتی کور است که قبر باشد وآن
جابی است که آدمی را ‎aa‏ ازرحلت ازدنبادران
جا نهند .

‏)1( چگ : سو

‏۱ - ممحف * فرستوك » ‎Cem)‏

‏۱) چك :

‏فرخا

‏ف رجف - بوزن ‎camel‏ پدر جد را گویشد

‏که پدر سیم (۱) است خواه مادری باشد خواء
پدری .

‏فر منك ۲ ه بروزن و معنی ارجمند

‏است که صاحب و خداوند قدر و مرتبه باشد -

‏وبمعنی زيبايي هم آمده ات
قرجود * » بر وزن متمود ۰ ‎gon‏
‏معجزه و اعجاز باشد » و اعجاز خلاف عادتی‌است
که از انبیا و کرامات از ‎Uy!‏ بظپور میرسد.
فرح - بتح
نقطه‌دار ‎OTL‏ . بمعی مبارك وخجته ومیمون
‎ath‏ - و بمعنی زیبا روی‌هم آمده است‌چه‌اصل
‎ol‏ لغت فررخ است . فریمعنی ‎bed‏ ورخ رویرا
کویند ‎٩‏ - و نام روز دویم ‎)٩(‏ است از ‎Las‏
‎oo‏ سالهای ملکی - و بنتح اول و ثانی
ساکن. درعربی جوجة ‎gp‏ خانگیباشد وشات
تازه را نیز گوند که از تخم ودانه سر بر آورده
‎ath‏ ونزديك بان شده که دوسه شاخ شود*۱.
فرخا ۱ خای نقطه‌دار بروزن فردا .
بمعنی فراخی و کشاد کی باشد ‎٩۱‏ - و محنت

‏ار وضم تانی مشدد وخای

‏دوم .

‏۴ - رك : ورج » فرجمند .

‏۴ - (عر) فرح ( پفتح اول ) اندام شرم جای - جای ترسنالك - شکاف ‎Qe‏ هردو ‎Sh‏
‏اسب کشادن ‎ph‏ دوچیز را - دور کردن غم . ركث : منتهی‌الارب » شرح قاموس .

‎pF sl Sisk, . ‏ظ‎ - ۴
‏از‎ frajaminitan, frajam ‏مناسی ۲۷4 » و‎ « frazham ‏پپلوی‎ - ۲

‏ص ۲44 .

‏6 رك : پرکار » ورك : دزی ج ۲

‏پارسی باستان ‎ofrajdma_‏ ( از ‎gam_ in,‏ « رفتن ») « استق ۸۱۸ ‎٩‏ < انجام وفرجلم. آخر

‏کار بود ۰ فردوسی (طوسی) کوید :
بکوشیم و فرجام کار آن بود

‏کد فرمان و رای جهانبان بود.»

‏«لفت‌فری ۳۳۹ >.

‏۷- از : فرج («م.) + مند ( پوند اصاف ) . ۸ - از ‎als‏ « فرهنگه
دساتیر ‎٩ . ۰ ۲۵٩‏ - در پپلوی 8۲12۷( تابان . مجلل » پرتوافکن,زیبا «خوشبخت).

‏ایرانی‌باستان ‎ofarnahva‏ , ازن)20 01860210۷ از- ‎ohvarnahvant‏ , قی : فارسی:

‏فرخنده « تیب کك ص ۷۶ » و ‎dy‏ : اسشق - هویتمان ۸۰۸ .
دفراخا ۲ ‎Cea)‏

‏شرح فاموی . ۱ - مخفف

‏۱ رك : منتهی‌الارب .
```


## [2026-09-06T02:24:11.803Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'PYEOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nwant={451:2368,466:2383,306:2223}\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in want:\n        print('#### pdf',m.group(1),'printed',want[int(m.group(1))])\n        print(p)\n        print()\nPYEOF",
 "description": "BQT v4 cited pages"
}
```


### [2026-09-06T02:24:13.667Z] TOOL RESULT

```
#### pdf 306 printed 2223
[pdf page 306]
۲۲۲۳۳ یم
نیاز ارم ۱ « بفتح اول و رای قرشت | نون » بممنی قسد وآهنگه نکردن ودست بطرف
بر وزن لیاسایم » معروف است بمنی آزار ندهم | چیزی دراز شمودن باشد - و بمعنی نیفکندن
-بممتی آزرده نشوم هم‌آمده است .48 و لینداختن - وناله نکردن و ثالیدن هم آمده
نیاز ومند ۲ يم دابع وسکود‌واوه است. .
بممنی‌لیازمنداست که محتاج وحاجنمند باشد. نیاگان ۱ - باعاف فارسیبروزن‌بیابان,
نیازی - بروزن حجازی, بامطابفه‌است | بهمنی اجداد پدری ومادری باشد +
از اففان - ومعشوق و محبوب و دوستدار را نیز نیا ۷ » بکسرارل بروزن حام.بممنی
کوبند ۴ . غلاف شمشیر است ۸ - ومیان و وسط لیخ وغیر
نیاز یان ۴ < بروزن حجازبان , بممنی | تیغرا نیز کوبند. هرچیز باشد ‎٩‏ - ویممتی‌تموی
حاجنمندان باشد - وکنایه ازعاشقان هم‌هست. | هم بنظر‌آمده است *۱- و چوب ین خیش رالیق
نیاز یدن * - بنتح اول ودال وسکون | کفته‌اند ۰۱۱ وآن چوبی است که برزیگران در
۹ -ر4 : آزاردن . ۴ - از: ییاز (ه.م.) طومند ( پوند اصاف *- مند) <
برازمند (م.) ۳ - از : لیاز (.م.) ی (نبت و اصاف) » حاجتمند (ر4 : بیازبان) ‌
وبممنی ممشوق :
چون این سلام زان لیازی شد نامزد شکیب سازی ...
نظامی کنجوی « رشیدی » .
دلم خستَةٌ نت زان » ای‌بیازی! که روزی لیاسایی از باز بازی -
مختاری غزدوی « فرهنگه نظام ».
ی - جمع « لیازی » (ه.م.) 8 - منفی « بازیدن > (ه.م.)
۹ جع «یا» (.م.) ؛ پهلوی 6۵5 ا8 رنه (رك : نیا )» درفارسی 8828( اسشق
۲ دارمتتر. تنبعات چاص ۱۲۳ » ولی بعضی «لیاکان» خوانند :
روان لیاکان ما خو شکنید دل بد سگلان پرآت شکنید. ‏ :
فردوسی طوسی « شاهنامةٌ بخ ج۱ ص۲۵۱*.
۷ - پارسی‌باستان ۰88182002 قس:ساسکربت 81 (پیشوند) ۳ 2189804-۰822
( کنجایش ) . قی : پیام . وجه اشتقاق قطمی لیست « اسشق ۰.۶۱۰۹۳
۸ - غلاف شمشیر وخنجر وکارد . السامی‌فی‌الاسامی‌در معنی فغلاف» » ارس مهذب‌الاسماه
در معنی* غلاف > همین‌کلمه راآورده اند « فرهنکه نظام » :
«مان تیز خنج رکشید از نیام نه بگشاد راز ونه برگفت نام...
فردوسی طومی « شاهنامةٌ بخ ج۱ ص ۵۹
‎٩‏ - بممتی وسط تیخ هوکز نیامده بلکه بممنی وسط هرچیز «میان» است ده « بیام »
سراج‌اللغات بنفل « فرهنگه نظام ج ۵ ص مب >. *۴- ۸« بممتی تعوبف « پنام» است یبای
فارسی». (سراح‌اللغات. ایضاً) - ۱ السامی‌فی‌الاسامی در معثی «المقوم» (عر) (همین‌کلمه
راآورده) فره هنگه نظام» .
۰ نیازهند - بکسر اول و فتح میم . از : لیاز ۳ مند ( پموند اتصاف ) ۳ لیازومند
(وم.) ؛ حاجتمند :
هر که برخود در سوال گشاد تا بمبرد لیازمند بود . «کلتان س ۱۲۳*.


#### pdf 451 printed 2368
[pdf page 451]
همشوند تس هخا
عالمتاب است چه با عیسی علیه اللام درايك | دارند- وبمعنی موافق* ومتابع وهمرازهم‌هست-
آشمان‌اند۹ #۰ : ویمعنی راضی وشاکر وخرسند۹ - وراضی شدن
همخوند بفتح اول وخای نقطه‌دار | و شاکر بودن و خرسند کزدیدن هم بنظن آهده
وواو معدوله پروزن همچند » مخفف هم‌خداوند است۷ .
است‌وآفراخواجه تاش‌هم میگوبندینی دوشخص همداستانی۸ - بانای قرشت بروزن
که يك صاحب و يك خداوند داشته باشند ؟ - | عرش‌آشیانی » زریرا کوبند که از رعایا در وجه
ویممنی شطهةٌ مقابل ونفیض وشد هم بنظن آمده | خراج ومال وجهات میگیرند و بمبی مال‌الرضا
است۴ . خوانند واین درزمان انوشیروان پیداغد وقبل‌از
همداستان؟ - دوک را کوبند که آن قوت لایموتی برعایا میدادند و آاچه س
پهوسته‌با هم مخ نکنند وحکایت بگوبندوصحبت | رسانیده بودند از ایغان میگرفتند.۹ ##

۹ - صحیح : دريك آسماست. ر4: همایةٌ مسیح. ۲ - ر4 : خوند ,

۴ - رشیدی بهمین‌ممنی آورده است. .۴ - از: هم (پیشوند اغترا4) ۳ داستان(۸.م ).

- نخون پد رکشت همداستات ز دانا غنیدستم این داستان .

فردوسی طوسی «فرهنکه نظام» .

۹ - «همداستان خرسند باشد.» «سحاح الفرس لسغ طاعتی» -

۷ - باین معنی همداستانی است. ر4 :۸ ۸ - از : همداستان (۸.م.) 1
ی (خاصل مصدر » اسم معنی) ؛ موافقت :

پندی و همداستانی کنی که جان داری و جالستان ی کتی.

فردوسی طوسی (کشته شدن آبرج بدمت برادران) «شاهنامة بخ ج ۹*۱

۹ -« درتاریخ طبری آورده که نوشیروان همةٌ رعیت را گرد کرده همةٌ زمین‌هارامساحت
نموده » بهمداستانی- که آنرا هرسال سه بار وبا چهار پاربدهند خراج قرارداد » ولهذا آن‌خراج
را همداستانی بمنی مال‌الرضا نام نهاد.» «جهانگیری» ولی درسخ تاریخ بلعمی (ترجمة طبری) که
در دستری ها بوددرفصل «درن کرخبر عدل انوشروان وخراح‌لهادن برولایتها» با وجود شرح چنین
خراج » نام «همدامتانی» باد شده است . همچنين درشاهنامةٌ فردوسی در عنوان «بخشید ن کسری
پادشاهی را بچهاربهروتدبیر کردن‌خراج را» ذ کراین‌کلمه نیامده. ر4: شاهنامدیخ ج ۸ص ۲۳۱۶
‎٩‏ ووقصل بند ۲۳۱۹ - *۲. درفپرست ولف هم‌کلمه فقط بمعتی مذکور درح ۸ آهده است . .

5 همخوابه - بفتح اول وواومعدوله‌وقتح باء (درنلفظ کنوی بکسرباه) از: هم (پیشوند
اختر41) + خواب ۸ (پودد) ؛ زوجهٌ مرد » همرء هم بالین هم بستر » کل ی که پادیگری در
يلك بستر بخواید :

ور لبود دلبر همخوابه پیش دست توا ن کرد درآغوش خوبش.

«گلتان صس ۶۱۲4

۵ همدان - بنتح اول ودوم» پهلوی ۴18224088 «مار کوارت » شم‌رستانهای ابران
مس » پارسی‌باستان 13(81221282) 118 « کنت. پارسی‌باستان ۲ 112081081288۲۱
«اغپیگل‌س 4 ۰۲۸ ۳ ۳۵81278 که‌پایتخت شاهیدرعهد. مادهابود. درعیلامی18-228 ۰88-702
آکدی 9-88-338-12-01 ۰ بودانی ۳8۵)858ع۸ "۰ 786841۵088 محتملا مشتق از

بقیه در حاشیةٌ صفحهٌ بعد


#### pdf 466 printed 2383
[pdf page 466]
نها هنوناس
هام۱« بر وزن اندام , بمعنی وت هنگفت؟ (۱) - بنتح اول وفای‌ساکن
وزمان وگاء باشد؟ - و بمعنی موسم وقصل هم | پر وزن انگشت » بمعن ی کنده و اسطبر و ضشخیم
آمده ات - وبممتی هنگامه هم‌کفته اند که | باشد۸ . واين ممتی‌را برجامه و پارچةٌ پوشیدای
مجمع وانجمن ومعر که باشد۴ . بیشتر اطلاق کنند؟ ؛ وبم اول‌هم آمده است-
هنگامه ؟ - بر وزن شهنامه ‏ مجمع وکنایه ازبیار هم هست ؛ و صاحب موْبدالقضلا
وجمعیت مردم ومم که بازیگران وقصه خوابان | بجای نون تای قرشت آورده است که هتگفت
رخواس کوبان وامثال آن باشد . باشد ودر جای دیگر نیز بای قرشت نوشته‌اند.
هنامةه طفلان - کنایه از دبا اه اعلم۱۶.
وعالم است. َ هنگه < بفتح اول وکاف فارسی‌وسکون
هنگامه گیر* - مک هکیروبازیکر | تایه مخفف هنگامه است. که مجمع وم که
را کویند . باشد .
هنگامی؟ - بروزن بدنامی » ترجمة مد - بنتح اول ومیم و سکون ثانی
خلق‌الامه است یعنی‌جانوری که درساعت موجود ودال, سبزیی‌را کوین د که برروی آب بهم‌رند.
شود همچو پشه ومگی ومانند آن . هنو تاس۱۱- بنتم ارل ونالی بواو
() چش: هنکفت .
- پارسی باستان -#38882002 ( وقت . زمان ) » قس: اوستابی-219/1.88102
(زمستان). پپلوی 228480 (پازند 88280) «امشق ۱۱*۹ ۰ ارمنی2888770 (دفعه, مرنبه)
[88880 4 «یکبار, یکدشه؟] و ( نیزه همچنین ) . «هوبشمان ۴۱۱۳۹ ؛کردی 21084
(زمان) ۰ کردی‌ع 0 دابا س۹4۵۳ ۰
۴ - دگرینجه آنديشة جامه کرد ( جمشید ) که پوشند هنگام بزم و نبرد :
فردوسی طوپی «شاهنامدیخ اج ص۲۳*.
۴ - ای شکته حن تو هنگا کل باده عغرت فکن در جام کل .
وصاف (الحضرة) «رشیدی» .
۴ سهنگام («م.) ؛کیلکیم 138883708 (غوغا . شلوغی) رك : هنکامه کیر .
لیر بمعنی وقت وزمان است (ر4: هنگام) :
چر هنکامةٌ خواب بودش بخفت ببازارکان چیز دیگر نگفت.
فردوسی طوسی « رشیدی؟ .
از: هنگامه (م.) ۳ کیر(گیرده) . ‎٩‏ - بمعنی مذ کوراظ . بر ساختةٌ
فرقهٌ آذرکیواست . ۷ -کردی 81۳۷ 10ظ دز نع 12ظ-02۳ لغة بمعنی بارکران
ومجازً مزاحم, کل‌کننده .
۸ - فرستادم بخدمت رقعةٌ ری بدست پهلوی هنگفت ولمتر.
ابن یمین فربومدی «رشیدی؟ .
‎٩‏ - بپترین جامه‌ای بود هنگفت مرمرا اوستاد چوئین گفت.
منائی غزلوی «رشیدی؟ .
۳ با ناه تصحیف است . ۱ ظ. برساخته فرقهٌ آذرکیوان است.
```


## [2026-09-06T02:24:40.662Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'PYEOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor p in t:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (562,570):\n        print('#### pdf',m.group(1),'printed',int(m.group(1))+1203)\n        print(p)\nPYEOF",
 "description": "BQT gām and gāh pages"
}
```


### [2026-09-06T02:24:42.355Z] TOOL RESULT

```
#### pdf 562 printed 1765
[pdf page 562]
-۱۷۹۵-
مانند غوز؛ لاله و در درون ‎OT‏ چند ‎Sls‏ کندم
نارسیده ‎ath‏ وخوردن ‎OT‏ مستی‌آوردها کربیشتر
خورند مردم را پی‌شمورکند و دبوانه سازد ۱ -
‎ay‏ © پروزن لاله . بممنی دور است
که در مقابل نزديك ‎Fash‏ - وکلولاینبه‌برزده
‎ere,‏ کرده را نیز گوبند که ‎cam‏ رشتن‌مهیا
کنند؟ - وبمعتی جوال هم آمده است؟ و آن

ظرفی است که از پشم وموی بافند . #
گام = بروزن لام . مسافت ما ‎Whee‏

gue ap
‏تا بنگه و کال بنگه بدیوانگیکشند‎

را گویند در وقت راء رفتن6 - و بمعتی قدم لیز
بنظرآمدماست که ازیاشنٌیاباشدتاسرانگعتان هو
‎ney‏ لجام اسب هم آمده است ۷ - و روستا
ودهکده را یز گوبند و ‎gm Sip‏ ده را کم
میگوند ۷ .

کامیش+ مخفف کاومیش‌است‌وآن
جانوری ‎ath‏ از جن سکاو.

‎OW”‏ بروزن جان,بهمنی‌لایق وسزلوار
‎٩ ach‏ - وپلدشاه وسلاطین رانیز کوبندویسنی

‏دبوانه باد خصم تو از ‎KIT, ey‏ -

‎AB pe ‏سوزلی‎

‏وبخاطر میرسد که ‎GE‏ تازی ‎atl‏ وممنی تر کیبی بنگگ خام یعنی ‎Kis‏ صرف . فرشیدی» .

‏۴ - رك :کال , گالیدن .
کلمه آمده «فرهتگه ‎lla‏ +

‏۴ - در السامی فی‌الاسامی در هعنی فسلیله» (عی)این
‎jem ۴‏ . طبری ۰88۷ ‎eval oS lads‏

‎. hs ‏نامه۰1۹۱ . در اراك (سلطان آباد) 80218 «مکی‎ oily ‏د‎ ghal, gal, gual
aye ۰۷۷ ‏«یب رکه ص‎ BAM ‏اوستا - 827040 «بارتولمه۵۲۲» ۰ پهلوی‎ - ٩
۰ ۰۳۵۹ ‏(قدم . لحظه, زمان) , زازا 841۳026 (بکقدم , کمی) «ژابا‎ BAW ‏کردی‎

‎: ‏«لگام»‎ Gane - ۱

‏ز ‎tle‏ شمی فلك ز رکند که تا گردد

‏ستام وکام ورکاب براق تو زر کند .
سوزنی سمرقندی « فرهنگه ‎dts‏ » ۰

‏۲ - برای این معنی این بیت مولوی را (درباب میل نداشتن طفل به بیرون آمدن از

‏شکم مادر) شاهد آورده‌اند :
که اکر بیرون فتم زين شهر وکام
ولی صحیح اين بیت چنین است :
که اکر بیرون فتم زین شهر وکام

‏. ای عجب بینم بدیده این مقلم =

‏ای عجب بینم بدیده این مقام.
«مثنوی چاپ کمن دفترسوم ‎ANTS‏

‏و« کام» بمعنی مراد ومقصود است. » وطبق ‎tau‏ علاءالدوله س ۲۹۷ :

‏که اگربیرون هم زین شب رکام

‏ای عجب دیگر ببینم این مقلم»

‏درین صورت عمنی واضح است . «لفظ «کام» بمعتیده: هندی است واصله کاوّن»باتلفظ ‏

‏مخصوص نون غنه‌است .۰ «فرهنگه نظام» -

‏۸ رك : کاومیش. ‎٩‏ -پوند میت

‏ولیاقت است: شایگان )= شاهگان) موب بشاء ولایق‌شاه؛ رایگان ‎(AG)‏ مشوب‌براه .
چیزی که دراه بابند. ‎cde‏ برای اشتقاق این‌پسوند, ‎dy‏ دارستتر. تبعات ج۱ص۱۵۷-۱۵۱ ۰
‎gusto‏ - بفتح دال , گریختن - دورشدن ۰ رگ : گال .- خروشیدن » فرباد کردن :

‏سلیمان چون زمرغآن قصه بشنید

‏بتندید 9 بجوشید و بگالید ‎ .‏ -

‏عطاریابوری «فرهنگه تظم >

#### pdf 570 printed 1773
[pdf page 570]
oS -۱۷۷۳<

آدم علبه‌اللام کرده ومبادی‌این ایام بر تقدیری
است که ‎Lis‏ مترقه را در آخر بهمن ماه
آفزایند وبهمن ‎ole‏ را می وپنج ‎BS‏ و بسنی
کوینداو لکاء‌اول بست‌وشتم اردی‌بهشت‌ماه‌قديم
است,واولگاه دوم(۱) بیست وششم تبرماه؛ وأول
گاء سیم شانزدهم شهربور ‎cle‏ واول گاه چهارم
پانز دهم‌مهرماه. واولکه‌پنجم بازدهم‌دیناه» واول
‎ol‏ ششم سی‌ویکم اسقند ماء است که اول‌خماةً
مترقه وآخر اسقندار ماه باشد ؛ وجمعی دیگر
کویند که اول گاه اول بازدهم دبماه‌قديم» واول
کامدوم( ۱)بازدهم اسفندارماه؛ واول کامسیم یت

وشنم اردی بهشت ‎cole‏ و ‎AF Jyh‏ چپارم بست
وششم‌خردادماه, ‎AT gly‏ پنجم شانزدهم شهربور
‎sale‏ واو لکاه ششم سی و یکم ‎MILT‏ است که
‎Ls Syl‏ مسترقه باشد .

گاهنگان! ‎oy b=‏ درآخر بروزن
ناهتگام. کاهکشان را گویند. و ‎OT‏ چیزی باشد
سفید که شبها در آسمان لماید و بعریی مبعرء
خوانند .
گاهواد ۵" - با ‎aly‏ بروزن ماهءپاره,
کهوازه را کویند وبعربی مهد خوانند .

‎oly‏ دوم(۰)

‏در ‎GE‏ فارسی با بای ابجد مشتمل بر هفت ‎ca)‏
‏گببمی؟ = بفتح‌اول و کسرثالی‌وسکون باشد که از آن ‎es‏ وطبق وکاسه و امثال ‎OT‏

‏بای ابید (۲) دوم(۱) و هیم مکور بنون زده» سازند ۴ - ونام شهری است از ولایت بجوروآن
بلفت زند و پازند در يك ‎Ae‏ بمعنی پست ور | مایین‌کامل وهندوستان ‎ily‏ است 6 - وخیمه‌ای
مقابل ‎athe‏ ودر ‎Sap Tes‏ پشت در ‎ath‏ دوه را یز کوبند که بيك ستون برپای کنندسوبمعنی
نوشته بودند» ‎aily‏ اعلم. خود وخفتان ‎ani,‏ بدان ماند از آهن هم‌آمده

‏گر فتح‌اول وثانی بروزن سفره‌سنگی ‎P‏ است ۷ - ‎ping‏ اول وسکون‌ثانی» هم‌بمعتی‌خود

‏)( چش : دوم ۰ )4( خم : ۱ - امد .

‎SY‏ مسعف «کاهکتان» . ۴ - ظ. از: گاه ‎(cas)‏ ۲ واره ‎cat ys)‏ ازمصتر
‎Dar‏ [بردن ] لفة حامل تخت ( کودله) ‏ کپواره (مخفف) ‏ کاواره 6 پهلوی 880۷2781
«تاوادیا ۱5۱ ‎Bhehvar€ ps5.‏ > ژابا ی ۳۷۳ . ۴ - » ‎g(a)bibmiman‏ «
‎pusht syle Zababmamna‏ ( پثت ) ‎Say?‏ ص۸۷ وه*۱> .

‏۴ - زین ‎dbl:‏ بسی ترا ‎ol, wt we‏ سرد و ‎Ks‏ کین .

‎. ‏«رشیدی»‎ SPF GU
‏سواراست او پلکه صد هزار سوار‎ eh vw 6
‏پرب ن گواء منت آنکه دیده حوب (جنگه) کیر.‎
 »یدیشر# ‏جهانگیری»‎ « gah ‏عتصری‎
‎- ‏ره کر درفهرست‌شاهناماٌ و لف« کیر» و «گیر» هردو آمده‎ ٩
```


## [2026-09-06T02:24:53.015Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"paigam\\|patigam\\|paitigam\\|hanjaman\\|hanjam\\|anjuman\" BQT_v1_pages.txt | head -20 | cut -c1-300",
 "description": "BQT v1 Latin etyma"
}
```


### [2026-09-06T02:24:53.066Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:24:56.467Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor leaf in (652,653,654,655,656):\n    p=t[leaf]\n    print('#### leaf',leaf)\n    print(p[:900])\nPYEOF",
 "description": "BQT v1 leaves near payām"
}
```


### [2026-09-06T02:24:58.148Z] TOOL RESULT

```
777
#### leaf 652
. بودان تروش
فوفانی ورای بی‌نقطه وسکون واو وشن‌نقطه دار"
نام ساحخری بوده که درزمان خود عثل و مائند
نداشته ۷ . ۱
فوران دخت س من داد بی نقطه
وسکون خای نقطه دار و تای فرشت بمعنی پسر
است نه دختر » نه يك پسر بلکه چندین پسر
است ؛ چه پوران جمع سر باشد» وان نام دختی
خسرویرویز است که پیش ازآزرمیدخت پادشاهی
کرده راورا بدین نام ازجهت آن خوانده‌اند که
ازوکارهای مردانه بظهور آهده است وأورا نوران
سل ملوله تر کسنان‌وده؟
مجهول و را و دال بی نقطه و کاف فارسی بالف
کشفه و بنون زده » مناید دائست که فارسیان
خمسه مسترف4۶ه را بر پنج روزآخرآ بان ماه می-
افزایندکه مجموعه ده روژ شود وآن ده روز را
پورد گان مبگویند» ودراین روزها جشن سازند
وشادی‌تمایند و آنراجشن بورد کان‌خوانند,ومعرب
آن فوردجان است؟ .
9
پوددیان - با بای حطی » بر وزن
و ممنی پورد گان است که ایام جشن پارسیان
باشد .
و د شسب * «پورمعلوم» پفتح‌شن قمله
دار وسکون سین بي نقطه و بای ابجد » نام پدر
پو دعنقا - لفب زال پدر رستم است»
چه کویند او را سیمرغ بز رکه ک
#### leaf 653
4 ۷۲۷-
ود یان - بکرثاك بر وزن‌حوربان»
۱ رای شهر کنوح۱ هم هست -
و زای هوز » پبرامونو کردا کرد دهان حیوانات
باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
ساق درخت هم امده است.و نقار مرغاثرا نیز
کفته‌اند» و با زای فارسی م ۲۳
۰ ۳۹
پورش ۴ - با ابی مجهول بر وزن
سوزش » بمعتی عذر ومعذرت‌وعذرآوردن‌ومعذرت
خواستن باشد .
لودن » بر وزن سوزن » زمینی را
گویند. که بجهت زرات کردن پاك کرده
بشند .
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
پوست باد کر دن -کنابه از طبار
نه دلی نمودن وراز گفتن باشد .
پوست یرای - با بای فارسی
حطی زده » چرم کر و دیاغ را کویند .
بوست دادن » کنابه از اظهار ته
دلی نمودن وماف
#### leaf 654
یوستین بگازر ۱
وعیب جوننده باشد ۰
(وستیی در بدن » کنابه از افثای
راز کردن باشد .
کردن. وعیب نمودن باشدا .
که بر وقت رشتن مردوك محند.
زره وجوشن را گویند - وامربردورشدن‌ویکناری
رفتن هم عست یمتی از راء دورشو - ونام کیاهی
است کهآ نرا میکویشد وشافپا میسازند واز جانب
ارمن می‌آورند و آنرا پوش دربندی میخوانند .
نقری را نافم است » و شیاف خوزی همان‌است.
و‌شا؟ - با ات بالفکشیده. پوشنده
وپوشند کی را گونند؟ .*
بو شث با ثانی‌مجهول بررزن‌حوشك»
بزبان ماوراء النه رگربه را گویند و بعربی سنود
خوانند؟ .
بو شگان - با انی مجهول ر فتح الث
وک‌اف فارسی بر وزن م وکشان. نام نوایست‌از
موسیقی - و بمعنی مغیبات‌هم‌هست بعنی‌چیهابی
که درعالم غیبت‌اند- وبسکون ثالث بروزن‌دوستان
نام جایی و مقامی است نردبك‌به نیشابورومقامی
۱ "۳ رژ۵: دوست کردن.
5 ود: بوشنج ۰ 3 له: بوشث.
۵ - کلکی 0۲ .
اسشق ۳۳۹
8۷ سم
است از مقامات سالك که آنرا بعربی غیب‌الفیب
مفدس تجلی لماید وفانی درحق ومافی در وگردد.
بو شنگ سب با ثانی مجپول بر وزن
هوشنگه , نا
#### leaf 655
و
پولاب بر وزن دولاب » بم‌نی
حس باشد و پولاپی‌حسی, بعنی‌|نچه بحس ونظر
درآ مد ۱ ۰
که از آن‌کارد و شمشیر واعثال‌آن سازند -وتیغ
و شمشیر را نیز گویند - و نام پهلواتی است
ای ال اج و نام دو ست ماز ندرانی و اورا بولاد
غندی میگفته‌اند عم غین نقطه دار - و ب‌عنی
و3 هم هست.
ولاد خسای « کنابه ازاس‌سرزور
ماشفد .
و لادد که م کنابه‌از اسب‌پرزورباشد.
بو لادسنحان کنانه از دلاوران
وسارزان واساحه داران باشد ۰
بو لاد هندی ۰ کنابه‌ازشیترهندی
باشد 5 3 ۰
4و لافی ع با ثانی حجهول بی وژن
طولافی » نوعی از اش‌ارد باشد .
و [4 س با ثانی محپول بر وزن لوله .
خریره مضمحل شده را کویند - وهندوانه‌ومیوه
های دمگر را نز گفته‌اند که درون آنها نرم
. فوبه
و ضایع شده باشد .
زسن را گونند که تکلتو باشد .
وک - بر وزن جوی. بمعنی پوبه‌باشد
که رفتار متوط است یعنی نه نند و نه آهسته,
و بعضی رفتار تند را گوشدب واعر بدیشمه‌نی «م
ست ععنی راه رو وقدم‌بردار .
پو با ۶ بروزن کویا» رونده‌را گویشد
- و بعضی دونده را نز گفته‌اند .
بویان ۴ زان جو ب
#### leaf 656
4 بفتح اول وسکون ثانی » کلمه‌است
که هنگام تصین با حیرتآمیخته برزبان رانن
وتکرار نیز کننه؟ ۰
یاه » بر وزن بهانه . چوبکی باشد
که درود گران درشکاف چوبی که باره‌مشکافند
فرو برند و کفشگران مابین کفثر و فاب نهند
و گاهی در زیر در گذارند تا سته و کشوده
کی
4 4 بفتح هردو بای فارسی وسکون
تین با حيرتآمخت هگوشد .
بر * بم اول بر وزن ظهر ؛ مدرسةٌ
جهودان را گویند - و بقتح اول دك حصه از چپار
حصه روز و چهار حصهثش باشد چه شبانروزیرا
بهشت حصه کرده حربك را پهر گویند. واین در
هندومتان یشتر مصطلح است .
۱ - رك؛ په‌به » امروز به‌به گوبند .
۳
۵۵
ومحافنت باشد .
هر ه داد - با دال ابجد بر وزن
هرزه کار ۰ باس دار ومحافظت کنشدمرا گوند.
پهلو- بفتح اول و سکون ثانی وضم لام
بواو کشیده, معروف‌است وبعربی‌جنب خوانند ۴
- و بفتح لام شهر را کویند مطلفاً چه پهلوی
بمعنی شهري باشد - و تواحی اصفپان را تیز
کنته‌اند و مردم شجاع و دلاور باشد - ومردم
بزر که وصاحب حال راهم میگویند چه مراد از
راه پهلوی‌راه بزرگان بزدانی‌است *ونام ولاشی
هم
```


## [2026-09-06T02:25:04.378Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (659,660,661,662):\n    print('#### leaf',leaf)\n    print(t[leaf][:1600])\nPYEOF",
 "description": "BQT v1 payām page"
}
```


### [2026-09-06T02:25:06.295Z] TOOL RESULT

```
#### leaf 659
ی
بهنا 4 بروزن مستانه , نوعی‌از میمون
باشد- وکلیچةٌ روغنی را لبز گود .
هنال بروزن کمند. دامی باشدکه‌بدان
آهو گیر ند.
(م ی و - بروزن فدفور » چیزیست مانند
دستنبوی که بزبان عرب آن را حنظل خوانند
وقنامالنمام(۱) همان‌است- ویمعنی بهی‌نیز هست
که خرزحره باشد .
44 س ختح ارل وثانی و تالث . بمعتی
بهن‌است» و آن شیری باشد که سیب مهربانی
بیار دریستان مادر طفیان کند - وبسکون ثانی
چوکان بازی و کوی بازی باشد - و نوعی از
سازند و گوی را در آن نهاده بر خوا اندازند
وچون تزديك بزمین رسد باز بهمان پهنه‌میز نند
[۴ نگذارد که برزهن آید ی تمفصل رسانند ۰
وآن‌را جربی طبطا بکوبند- و پهنی ران آذمی
و حیوانات دیگر باشد از جاب درون و آن را
بربی قطن خوانند - و بمعنی میدان هم آمده
خوانند وچوبی باشد مخروطی تراشیده که‌اطفال
رسمانی برآن پیچند و نوعی برزمین اندازند که
تادیرباز بگردد ۱ .
ی « بنتح اول بر وزن سهی ۰ حنظل
باشد و آنراخریز؛ تلخ‌هم هت و خرزهرمرا
چوکان را نیز گوشد که سر آنرا مانشدکفه یز پهی خوانند ؟ .
بیان بیست ویکم
ی ه بنثح اول و سکون الی » ممروف
است» و آن چیزی‌باشد که بر کمان وزین اسپ
وب تیرجایی که پیکان درآ نکنندیبند. وجربی
عصب کویند. و مضفف پای است که بمربی رجل
خوانشد ۴ - و نشان بای باشد که نقش‌فدم‌است ۴
ودئبال و پس وعقب. و تعافب. و قصد و اراده -
ونشان - و پی‌بردن بعنی نشان یافتن - و بمعنی
برای و بهر بیز حست چنانکه گوبند * از پی
فلان کار» بعنی از برای فلان کار واز بهر فلان
چیز - و بمعتی بار و مرنبه هم آمده است مثل
آنکه گونند فچند پی» مراد آن باشد که چند
مرتبه وچند پار- وتلب و طافت را نیز کفته‌اند -
؟ - باين معتی در اسطلاح علمی
۴ . رك: ا.
بقیه از صفحة 4۳۲
مشق ۰۳۶۹
۴ - پهلوی 09220 2 اونوالا 6 ۸
#### leaf 660
یاب
وبکر او عخفف یه بات دکه درچراغ سوزند
- وشمم تیز سلزند ۷ -
یمیت بروزن سراب. بمعنی پاباباست
که ین‌حوض وته جربا باشد وبعربی قمع رکوبند -
وتهات عرچیز را تز کفتهاعد - و بمعنی تاب
لبادم بر وزن زباده . هعروف است
که قض سواره باشد ۴ - ونام مکی‌از مپرهای
شطرنح عم حست - و نم کلی است ممروف -
از عردم یی سواد باشد یمنی علم و فنلی کسب
تکروه بلشد .
یباده نهادن-کنابه از زبون داتن
وعلجز اتکلشتن باشد . 9۶
ار دشتی- بکسر .اول و زای هوز ۰
دوآنی است که *ن را جربی صل‌الفار خوانند .
کوبنه اکر حوش بخورد میمیرد , و از خواص
او اتت که اک رک رکه بای بربر که آن ,گذارد
حمین که مزدارد لنگه شده باشد وگن سای
توقف کند الیته بفتد وبمیرد .
هیا لش یا کاف . تسیر پیاز است -
مه
وکیاهی را لیز کون دکه ازآن بوربا بافند -
و نوعی از کرز باشدکه سر. آن را با زنجیر
چو کن خوانند ۴ - ونام قربه‌ایت دردامن کوه
معدن لمل ۵ .
یا کیی- املیباشد قیمتی۷ ومنسوب
بقربه مازك را نیز گویند.
فاد یز « بکس لام و سکون تحتالی
و زای نقطه دار . نوعی از از دشتی باشد
بسیار است
ید ۳۹۹
یار موص ح بکسر زای حوز ؛ بیخی
وعنصل واسقیل همان است و بسنی‌آن را قردمانا
گومئد .
پیادی- بروزن حجازی . نوعی از لمل
قیمتی باشد ۷ - ونوعی از گرز هم مت و آن
چنان است که چند کوی فولادی را بچند زنجیر
کنند وآنرا بترکی چوکن کوند ۸ . جد
ی ۷ » بروزن‌سلام» بمعنی خبر وییفامباشد
۱ رگ : بیه . ۴ رگ : بایاپ . ۴ - پارسی باستان ۵06024812
(قس: سانکرت قا0942, ۰۳208۵1162 معرب بیدق) «اسشق ۰۳4۷ و نیزیاده معرب آست.
دقی؟ » ۴ ر: پیازی. ۵ رك : پیاز کی , 1 - محه‌دین ابراهیم بن
ساعد: اصاری درتض‌التخاثر (صس ۱6) کوید: «ومنه (بلخش < لعل) مابشبه الافوت البهرمالی
وحرف بالیاز کی وهو اعلاها واغلاها.» مسحح کتاب درحاشهٌ همان‌صفحه‌نوشته؛ «هبيجيك ارلغویان
قدیم وجدید این‌لقظ رایاد نکردماند وکمه برای ناو ا
#### leaf 661
و۳ ««
پیاهو - با های هوز بر وزن ترازو .
هم عده است کهخالة شش بهلو 7
اری ماشد ٩‏ ۰
فیتا۵؟ - بانای قرشت؛ زد زن و معنی
ت بلغت زند و بازند (۱).
لیترسب؟ - بدر اول و سکون ثانی
و .فوفانی و رای می نقعله مفتوح بسن مي نقمله
وبای فارسی زده , نام بدر پورشسپ اسث که جد
یفام است
برست ات .
شقات- با تای قرشت بر وزن مخك »
کرمیست که جامهای ایرشمی را خورد وضایع
و ۵
له بروزن هیج . بمعتی تاب و حلقه
و خم باشف ب و کنابه از رشك و حند هم
هست .
پیچبا * - با بای فارسی بسر وزن
پیشوا . خرچنکه را کویند که بمربی سرطان
خوانند .
پیچاگ - بای مجهول بروزن قیجك ۰
(۱) چك: ژد و پاژند :
۱ ‌- ره 5 آهویای.
۶ اسشق+ ۳4عرك : بیام.
و مربی آن دا عشقه و لبلاب خوانند ۷ -
و کرو ابرشم و رسمانب و سربند زن را
دا
لین » بروزن ربوند . عصانه ویتانی
بند زنان را گومند .
لیچه » با نانی مجهول بوزن رشه .
و عذقه کویندشی  .۷‏ و زلف عملی دا نیز
گویند- و طر؛ زلف و کا کل را حم کقتماند که
پیچند و برمکدیگر گرء زتند - وموی بلف وا
نیز گفنه‌اند و بعربی عفاص خوانند- و پیرایهای
هم هست از عرصع که برسی عووی بتد کنتد -
و بوشش بالای در خائه را تیز کفتماند- و سعتی
رمز وایىا و اشارء عم حست ۸ 3
یچیه سحرچیز را که یچیده باشتد
عموما ودست برنجا ی که آنرا چها رکوشه اه
تام و متا
لیخ بکر اول و سکون تانی و خای
نقطم‌دار , چرك کوشپا و کنجهای چشم را گوبند
۳ آبی که از چشم بی آید و مر کانها را برحم
چسباند, وبعربی‌رمص‌خوانتد. ۱
بخال"- بروزن قتال. فنأة حرتاتوا
که عربان رمص خوانند - و بسی درد و ه
بگفتش همه راز , بایور شپ
۴ - امروز سد 10( :م) گویند ۰
۳ رك : سك .
ت _ اسم مفعول از: بیجیدن.
زرانشت هرلم-
«مزدیسنا ی ۷۰ وجدول برایر ص14>.
۵ رك : پنجیا . ۱ ر4 : یسجه
#### leaf 662
تشن
ولای‌هرچیز وضله حرشیتی را کوشد ازحیوانات
پیتتن" -بروزن ربختن,بممنی پیچیدن
باشف . ۱
یتخس" بروزن ک رکس . بممنی کمان
بردن واز روی گمان فهمیدن وراه بچیزی بردن
باشد .
سای ارل و تاك پر مك
- و چیزی که 9 فرم شده باشد -
و درمانده و عاجز شده را نیز کویند - و بمعئی
هی بست 4 دبوار ی که بیخ
ومحبری ومتحصن و کرفتاروبندی رانیز گفته‌اند
و بد بو و متعفن و گندیده شده را ه مگویند »
وبضم الث یز آمده است .
پیخسته ح بر وزن برجنه » بمعنی
زیر بای نرم شدم و عاجز ودرمانده - و محبوی
و گرفتار - و بد بو و متعفن - وکمان بردن را
- و در
زر کوسد ری ی رس اسر میتی
ره
بزور باشد ۰
بمعنی ترت ومرت وتار وعار و بفایده - وهرچه
از تف آش زرد وضایع شده باشد ِ#
ید اد بر وزن شداد ؛ بمعني بیدا
وظاهر باشد .
فيك او سی» بنتح واو و سین بی نفطه
بتحنانی کشیده . درمی که در زمان کیان رایج
بوده و هردرمی به‌ینج دینار خرج میشد, وبکسر
واو هم بنظر آمده ات :۷
پیر ؟ بروزن وه‌متی پدر |
اب گوند ۵ ۰
یر ا ۲ - با انی مجهول بروزن گیرا »
و سر تراش که موی زبادتی رابکند و باغبان که
؟ - در لغت فرس اسدی ( ص۳۹ )
اف ز چونن حقیر ومی‌هنی رد3
وتو
رك ؛ پشته .
" هز از وصد و شصت قنطار بود
که بر پپلوی موبد پلرسی
۵ درفارسی نیز
. کردی واففانی ۳3۲ .فی :
درم بد کزو پنج دینار بود
همی نامبردش به پیداوسی. فردوسی طوسی.
۴ کیلکی ۳66۲ .
۳۵۰
«2. ۲ص ۱۹6*.
4 یبدا
ابرانی باستان 0۵0۷263 ۵
۹ - ره ویزاسم
```


## [2026-09-06T02:25:20.218Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor leaf in range(658,672):\n    p=t[leaf]\n    if 'پیغام' in p or 'یغام' in p:\n        print('#### leaf',leaf)\n        # print footnote area\n        print(p[-1400:])\nPYEOF",
 "description": "BQT v1 payghām footnote"
}
```


### [2026-09-06T02:25:21.819Z] TOOL RESULT

```
#### leaf 671
 پيك بفتح اول وکاف فارسی باکاف تازی, ازاوستابی ۳20112 ۵ لفة بمعنی پیادم
۱ معرب آن‌فیج .سشق ۳۵۹.
‌ یکان - بفتح اول . اوستایی (9) 0هع + 02161 (180 کندن). ارمنی [مه‌اعم
0 « استق ۲ ۶ , پهلوی 0 « اونوالا ۲ده » ؛ توكك تيز تس و دیزه ح
ین و ستسان:
پرندمایست شکاری از جنس باشه ۱ -و بمنی
یود » بنتح اول و شم ثالث بر وزن
طیفور , دهان تنکه و مرطبان کوچك و امثال
آن را گوبند , وبکسس اولعم درست است .
فیقو له بی وزن زنگوله , بمعنی
پیغله است که کنج و كوشة خانه- وکنج. و كوشة
چشم باشد- و بیراهه رانیژ گویند که نقض راه
رت ۳۹
فیقون ‏ بروزن میمون ؛ عبد و پیمان
بقبه از صفحه 444
۱ ۵ پیشیی - از: پیش + ین (نسبت)؛ مقدم. سایق» قدامی - کهنه عتیق. عم پیشی »
علم الهی و ماجمد الطبیمه : «اما علم نظاری سه گونه است: یکی را علم برین خوانند وعلم پیشین
وعلم آفچه سیبر, طبیمت است خوانند...» « دانشنامه ص ٩٩‏ .
۵ پیغام - بفتح اول. هم‌ریشه وهم محنی پیام «اسشق ص ۸۰ ر: پیلم وپیتام. درزبا کی
00 «کربرسن ۰۹۰ ,کیلکی صفاو(26 .
۵ یغامیر وعخفف آن یغمبر ار بات اب ام بیغام ۳ بر (مخنف
برنده)" دراستی ۳6610171۳26 با 02011۳0۳6۲ « . است ۱۲ » »گیلکی ۳۹
رسول . کبکه پیفام می‌برد یامی‌آورد-. کس یکه ازجاب خدا مأمور هدابت خلق است : «ازهر
اين همی عیراث ماند علم پیغمبر بوصی و از وصی بامام و از اما بحجت » «کنف سپ ۱
سجتاای ص 1۱۵؟.
۵ یخامیری و پیخمبری - م رکب از: ییفامبر (پیغمبر) ۳+ ی ( مصدري )؛ رسالت ؛
یفام بردن- نبوت: «بسیاری پیغمبران‌بمین برشریمت پیغمیزان پیشین بودند وغدتی برآن شریمت
همی کار کردند ؛ وبه پیذامبری رسیدند.» < کشف المحجوب سجسانی ص۷*.
```


## [2026-09-06T02:25:32.429Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in range(370,400):\n    p=t[leaf]\n    if 'انجمن' in p or 'انجام' in p:\n        print('#### leaf',leaf)\n        print(p[:400])\n        print('---footnotes---')\n        print(p[-1200:])\n        print()\nPYEOF",
 "description": "BQT v1 anjoman page"
}
```


### [2026-09-06T02:25:34.573Z] TOOL RESULT

```
#### leaf 385
- بو -
) فحل س بفتم اول وکسر ثالث و سکون
نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳
عالمتاب است .
انجمن! - ینم اك و قح میم وسکون
نون ۰ مجلس و مجمم را کویشد - بمعنیکروه
انحوج - بروزن محلوح , چوب عود
باشد ؛ و بهترین وی‌آن تکهدر ته آب‌شیند .
کونند عود یخ درختی است که آنرا میکنند
و در زیر خاكث دفن میکنند تا مدنی همین بعداز
آن برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی 
---footnotes---
ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
کندنای کوهی باشد که‌بمربی حشیشةالکلب‌خوااند
و صوف‌الارض نب زکویند - و دشوار زابیدن زنان
را سودمند بود - و بفارسی بمعثی دبزه‌ریزه کرده
شده باشد .
انحیر بر وزن
زنجیس ۰ میوه است
معروف -ومطلق‌سوراخ
را کویندعموماسوسوراخ
کون,! خصوصا - ونام
جوی ات درهرات
و آنرا جوی‌انجیل بلام
هم میگویند .
انجیر ۸3 ه ناممیوءاست درهندوستان
) نحیر دن « بنتح‌اول ودال ابجدیروزن
شمشیر زن» بمعنی سوراخ کردن باشد, چه‌انجیر
بممتی سوراخ است .
انجیره * بروزنزتجیره ۰ بمعنی‌آنجیر
۲ ۰ و ره : دائرمالمعارف اسلام .
9 افجرك .
بمعنی پاشیدن , جممعا : از هم پاشیدن .

#### leaf 387
-۱۹۹ -
)اد « بروزن پرواژ ؛ ممنی شسد -
و میل نمودن - و حمله کردن باشد - و امر
باين معنی هم هست عنی فص دکن ومیل تمای -
است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱
و بممنی مصدرهم افخة ابت که انداختن ,اشد.
انداده ۷ » بروزن خمیازه ۰ یمانتهر
چیز را گویند - و فیای کردن و اندازه گرفتن
را نیز گفته‌اند , و تعرببش بهندسه کرده‌اند ۴ -
۰ بمعنی قدرت و فوت هم آمده است :
) ند ام ۴ « بروزن انجام , معروفت که
بدن ر
---footnotes---
ان کل و کچ بریام
ودیوار مالند - وشکوه وشکات - +غیبت رألیز
نند .
)ندایش بر وزن افزاش ؛ بسسنی
کاهگل کردن و گلابه و گچ‌مالیدن باشد .
| ند ایشگر ه بنتح تاف فارسی‌وسکون
رای فرشت. کاهگل و کلابه بربام ودیوار مالندمرا
گومثف .
آبدربایست
آثای4 « بروزن هسابه , بمعنی‌انداوه
. است که مالةٌ اسادان کل کار باشد - و شکوه
وشکایت - وغیبت را نیز گویند .
ودال بی‌نقطه مفترح بخای نفطه‌دار وسن بی‌لقَطةٌ
زده » حمات کننده ودشت ویتاه را گوشد ۰
اند خس و اده » اندخی‌سملوم. وواو
بالف کشنده و رای بی‌نقطة عفتوح ۰ قلعه وصاز-
وجایگاه ب ویناه رتکه گاه ماشد - و بناه دنله
ویشتیوانرا دز کنته‌انه 3
| فد جسیدن » بر وزن کم رضیدن ,
.حمایت سودن وپشتی کردن وپشاه دادن- و پناء
کرفتن باشد .
| فك ر؟ » بروزن بندر » بسعثی در باشد
وعریی فی کوبند حمجتانکه الدران و اندر خانه
هنی درون ودرخانه - و افاده ععنی شرت 0
میکند چون بامادر ویدر وخواهر وپرادر کیب
کنند همجو: مادراندر و پدر اندر و خواعر اندر
ار آب » بروزن منجلاب » شهری
است از ولات بدخشان مایین هندوستانوغزلن -
اندر بای » با بلی ایجد بروزن‌صتدل
سای ۰ بمعنی ضروری و حلجت و محتاح البه
وذربایست باشد 9 - ونگون‌وسرازیر وآوشه را
لیز گوبند ٩‏ .
) ندر 1 یست ه بکرتحتالی و کون
سین و فوقانی بمعنی اندربای است که ضروری
وحاحت ومحتاج اله باشف
انداختن .
۴ ماس *: پارسی باسسان؟,8]142.
۱ .رك : اندروای.

#### leaf 392
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
بمعنی هو رکردن 
---footnotes---
گاره‌میکند»
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
است و ان قلن باشد که نيك بقوام آورده‌باشند
و برطبقی ریزند تا سخت‌شود و دندان کیر گردد .
انگدان ه بنم نالك ودال بالف کشیده
بروزن مردمان , شنای را گوبند یمنی دمومردم؛
و آن جانوری باشد وحشی شبیه بادمی ؛ و در
جاوتری میگوبند واه اعلم - و نام درختی حم
نقطهدار هم آمذه است - و نام قربه‌است‌ازفرای
کاشان که بانگوان اشتهار دارد.
انگرده ۳ بشم ثالث بروزن‌افرده. دانةً
انگور که از خوشه جدا شده باشد . ۱
افگر یز - بکون‌نالت بروزن‌دنگریز,
رستنی باشد و گل‌آن مانندگل خسك زرد.متود
و اطراف آن خار دارد و انرا بعربی قرطم بری
خوانند » و بیونانی طریفان کویند - و نوعی از
شه ازصفحهٌ ۱۷۳
يب ۲۳۵ ۰ رك : انگزد .
« نیب گی۰۹٩‏ >.
```


## [2026-09-06T02:25:42.633Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[385]\nprint(p)\nPYEOF",
 "description": "BQT v1 leaf 385 full"
}
```


### [2026-09-06T02:25:44.281Z] TOOL RESULT

```
- بو -
) فحل س بفتم اول وکسر ثالث و سکون
نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳
عالمتاب است .
انجمن! - ینم اك و قح میم وسکون
نون ۰ مجلس و مجمم را کویشد - بمعنیکروه
انحوج - بروزن محلوح , چوب عود
باشد ؛ و بهترین وی‌آن تکهدر ته آب‌شیند .
کونند عود یخ درختی است که آنرا میکنند
و در زیر خاكث دفن میکنند تا مدنی همین بعداز
آن برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی باشد .
افحوخ - بررزن مطبوخ . چن‌وشکن
روی و اندام باشد از عابت چیری دا سبسد: ۳
و بژمرده شدن میوه را نیز گفته اند - و بمعنی
آب ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
کندنای کوهی باشد که‌بمربی حشیشةالکلب‌خوااند
و صوف‌الارض نب زکویند - و دشوار زابیدن زنان
را سودمند بود - و بفارسی بمعثی دبزه‌ریزه کرده
شده باشد .
انحیر بر وزن
زنجیس ۰ میوه است
معروف -ومطلق‌سوراخ
را کویندعموماسوسوراخ
کون,! خصوصا - ونام
جوی ات درهرات
و آنرا جوی‌انجیل بلام
هم میگویند .
انجیر ۸3 ه ناممیوءاست درهندوستان
) نحیر دن « بنتح‌اول ودال ابجدیروزن
شمشیر زن» بمعنی سوراخ کردن باشد, چه‌انجیر
بممتی سوراخ است .
انجیره * بروزنزتجیره ۰ بمعنی‌آنجیر
۲ ۰ و ره : دائرمالمعارف اسلام .
9 افجرك .
بمعنی پاشیدن , جممعا : از هم پاشیدن .
```


## [2026-09-06T02:25:59.148Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### AHD\"; grep -n \"gwa-\\|gwā-\\|gwem-\\|gʷem\" AHD_watkins1985.txt | head -10 | cut -c1-500; echo; echo \"### CHEUNG gam\"; grep -n \"^\\*gam\\|\\*gam \\|gam¹\\|\\*gam-\" CHEUNG.txt | head -10 | cut -c1-300",
 "description": "AHD and Cheung"
}
```


### [2026-09-06T02:25:59.222Z] TOOL RESULT

```
### AHD
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, 
685:lenk-. To bend. Germanic */engwa- in Old Norse lyng, heather: LinG?. [Pok. lenk- 676.]

### CHEUNG gam
1816:s.v. *gam-) || (+ *para-) napoßap- ‘to bring forth, produce’ || (+ ham-) 
7307:*gam! *to come" 
7346:*gaml 99 
7357:*OLD PERSIAN: *gam- ‘to go’ (not attestested as simplex) || (+ *aua-) ‘to go down, 
7446:*gam2 ? 101 
7495:*gam? ? ‘to press, extort’ 
7521:*gamp/b! ? *to move to ? 
7549:*gamp/b? ? ‘to labour, exert’ 
8351:Abaev, l.c., have a different origin: < *gam ‘to come’. 
34048:*gam-, 99
```


## [2026-09-06T02:26:00.426Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### NYB p228\"; python3 - <<'PYEOF'\nd=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nprint(d[236][:2500])\nPYEOF",
 "description": "Nyberg page 228"
}
```


### [2026-09-06T02:26:02.218Z] TOOL RESULT

```
### NYB p228
295
 [wtyst'] a linear measure, a span = 12 finger-breadth 93°. — Av. (1440) vitasti-
viturt [wtwlt'] v. vitartan.
viyak [wy’k; Prth ’TRH] place: õi ~ ku on the spot where HajB:8; space HajA:8. B:9. - P2:6 wy’k BYN: read wy’ wyt = u yávet (q. v.).— < *vi-vāha-ka from Av. (1394) ?vah- ‘to stay’, Junker, WuS XII, 1929, 148; elsewhere gyw’k = giyäk (q. v.).
Vivanghänän [wywngh’n’n'] patr. of Vi- vanghān the father of Yam (Yima) 47°. 1015, — Vivanghän is in itself a patr., Av.
217
viyiftan
(1451) vivanghana-, from (1452) Vivah- vant-, the old Aryan name of Yima’s father (RV Vivasvant).
*viyän [+wyd°n'] tent; ~ kartan to pitch the tents 2022-24, — In the MSS the initial w- is wanting; corrected by Henning, BSOAS X, 1942, 951n. 1. Ps. wyd'n; MPrth wd?n ‘tent’, Arm. lw. vran; NP kiyän mis- reading of giyän. FrP, Cod. S, XVII, 9: wyd'n [Phl.] kunand [NP].
iyiyäpän [wyd” p’n'; 426 wy?p?n'] deluded, seduced 90°; charmed, enamoured (pat) 426. — Paz. vyävan, vičiva, Skr. v. vimugdha, vimohita (SGV), vikala (Mx); < *vi-dä- pana-, middle pt. of vi + caus. of *dap-, identical with Av. (679sg.) dab- ‘to deceive’, which has got its -p from the pt. dapta-; pass. viyüpihistan v. below. Hence viyāpānīk ‘magician’, Bailey ZP 27 n. 2.
2viyapan [wyd’p’n'] waste, desert, v. ban; < *vivāpāna- (with dissimilation of the second -v- > -y-, cf s. v. vihēž) middle pt. of Av. (1346) vap-: vivapat ‘he de- vastated'; ef Junker, WuS XII, 1929, 143 sg.
viyäpänöh seduction, inveiglement 9024, from lvtyāpān.
v. next w. — 2. to devastate 1079, from toiyāpān.
viyapihistan [~-yhstn'] to let oneself be seduced 9074, v. !oiyüpàn.
viyiftan [wdyptn'] vihčp- [wyhyp-] to seduce: ke viyift vihepet he who seduces a seduced 82° according to Cod. K; it could also be translated: he who, himself being seduced, seduces (others), cf Arab dalla wa-adalla. The passage deals with the sin of male homosexual intercourse, for which the basic text is Vd. 832: arša- ca vaēpyē arša-ca vačpayo a male who is the passive partner, and a male who is the active partner in the intercourse. The Phl. translations show a remarkable
www.parsianjoman.org | jl, - JU P J 8 lvl 9929
viyiftan
embarrassment in dealing with these terms. The translator of Vd. 8%, who quite correctly felt that vačpyo is a pass., borrowed the Av. vb. (1322 sg.) vaēp- (otherwise not attested in Milr as far as I know) and formed from it the pass. pt. viftak, then, likewise correctly interpret- ing vaepayö (vačpayant-) as an act., form- ed from viftak the caus.
```


## [2026-09-06T02:26:09.990Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nd=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (246,247,248):\n    print('#### leaf',i)\n    t=d[i]\n    import re\n    print(t[:2600])\nPYEOF",
 "description": "Nyberg glossary z pages"
}
```


### [2026-09-06T02:26:11.586Z] TOOL RESULT

```
#### leaf 246
yat-o.
yütango(k) [y’tngwk] solicitor 70%, — Paz. jädangö; < *ydtana- = *ydta- (v.s. v. yāt) + go < gov from guftan (-k is spurious, ef. s. v. z"étodàt). Commonly yätak-göb from yātak = yät; Arm. lw. jatagov (Hbschm.).
www.parsianjoman.org | Col )b
yat-ó
yat-6 [yt’w'] (Prth) till until 272, — MPrth yd ^w or yd alone, v. Henning, List 89; BSOAS XII, 1947, 52. I cannot accept any of his etymological attempts. In my opinion, yat < yatam*, pt. of yam- (v. s. yatak), ‘held on’ (ava ‘to’) used adverbially, cf Hom. oys8óv (from Eyw) + gen. ‘close by’. Cf yumē.
yütük [y’twk'] sorcerer, wizard, of the enemies of the Zoroastrian religion, pas- sim; pl. eas. obl. —-än 46%. 5018, 8721, 9027; sorceress 10°; sorcery 4374. 447, — Av. (1283 sq.) yätu-; Paz. jädu; NP jadi.
yātūkēh sorcery, witchcraft, gl. to apé- dāt (g. v.) 3716,
yātūkihā through sorcery 4819,
yavar [y’wl; Prs inser. y'wly] time, oc- casion: pat hän ~ ka on the occasion when P1:2; fratom ditikar u sitikar ~ first time, a second time, a third time 4617-18; —-& [y’wl + 1] once and for all 1016. — MPrth y wr; MPrs Zr (A-H II), jr (BBB); Paz. jävar; < *yäva-vara-, v. next w.
yāvēt [y"wyt'; inser. y’wyt] perpetuity: yat-6 róc ~ for all time, in perpetuity 2728. — P2:5-6 read 'nwšky (6) wy’wyt štly = anēšaky (6) u yāvēt-šahrv immortal and with eternal rule (bahu- vrihi; thus justly Frye, AO XXX, 1966, 86; clear on the photograph of Professor Luschey; my reading was that of Herz- feld, who put at my disposal a photo- graph of small size and his own tran- script; the correct reading was con- firmed on my personal visit to the monument 16. 10. 1971). — MPrth y^wyd in the expressions ^w ywyd ywyd and ^w y^wyd y’wyd’n (S), yem ywyd y’wyd’n (A-H III, BBB) ‘in secula seculorum'; Av. (1264 yav- and 1266 yavaētāt-) ya- vaēca yavaētātaēca id.; yāvēt < the nom. *yāvaitās from *yāvaitāt- (in Av. shorten- ing of -āu- > -av- and -āi- > -ay- before a vowel is the common rule). NP jāvīd.
226
.yazet
yāvētak eternal: nām i ~ 95,
yāvētān perpetual, eternal: ~ rēcān in eternity 272°. - MPrth y^wyd?n, ^w y’wyd’n ‘eternally’; MPrs Z’yd’n (S, A-H II), j”yd*n (BBB); Paz. jāvada (SGV); NP jüvidàn.
yāvētānakān for all eternity 103?9, yazdān [yzd'n'] v. yazet.
Yazdēkirt [yzdykrt'], Yazdkirt [yzdkrt'] Sassanid king (Y. I, son of Shapur III, 399-420) 114". 1158-7, 116'9. 117!9. — Cf MPrth yzdygyrd ‘divine’; Arab Yaz- dajird.
Yazdekirtän, Yazdkirtan,
preceding name: Vahräm 114%. 115°. 11733.
patr. of the (g. v.) z —
yazet [Prs inscr. and Ps. yzdty, BP yzdt'], pl. cas. obl. yazatān [yzt’n] HajB: 2. 4, commonly yazdän [inser. yzd’n, BP y
#### leaf 247
zd?n'] Prth yazatān [y?ztn] HajA:3.4. SPrth 5.7.12, god: Atur ~ 252; Gosurvan ~ 3476-27; Nerösang ~ 60°; Mihr ~ 961; hin ~ (se. Zartuxst) vànom 61°; ~ a god, or possibly already (as in the Ps.) God 11918; — ~ as pl. cas. rect.: hamak ~ 104* (together with pl. cas. obl. amah- raspandan and martomčin used as pl. cas. rect.); — pl. cas. obl. yazdan (ete.) a) gen., often placed before its subst.: pat yazdan hayyäreh 314-15, 121* (but pat hayyd- reh i y. 50%); yazdān xvēš hom 6219;
. i yazdan, passim; — b) dat.: yazdan u Sähpuhry xūp sahät it may seem good to ... P 2: 7. 8-9; api-š kämak ... apürik yazdän it is the wil ... of the other gods 5911; — c) after prep.: andar yazdän 172, 70%; apāk mēnē- yan yazdän 7418, 7922; pat yazdan 841’; hac yazdän inser. passim; — d) agent: 38?. 459. 5517, 10311; — e) instead of cas. rect. pl. 3417. 8815. — Borrowed from Av. (1279 sq.) yazata-, hence the irregularities of the forms: yazét cf Syr n. pr. Yazid- panüh; NP izad < yazad, cf izišn < yazisn. MPrthPrs yzd, pl. yzd?n.
WWW .parsianjoman.org | oe ww
(Yaz)et-yad
227
yuvat-sritak
(Xaz)ét-yüd n. pr. of the scribe of P 1, v. l. 12. — “Worshipper of the god": -yad from yad-, the SW form of yaz-, v. yastan.
yazišn [ycšn'] performance of religious service, worship, sacrifice 5314. 959." eto. passim. — V. yastan.
yö-drün [ywdlwny] harvester 12816 - yo- < Av. (1265sq.) yava- ‘corn’ + drun-, pres. st. of drütan, NP durüdan dirav- ‘to reap’, v. Barr s. v.
yöd- [ywd-] pres., 3d p. sg. yodet [ywdty] (the wind) blows 1284. — OP yaud- ‘to be in commotion’, Av. (1231 sq.) yaoz-, v. āyūz-, cf dhdyénitan.
yujiyast [ywcy’st'] a measure of distance 505. 5418. — Av. (1301 sq.) yujyastt-.
yumé [ywmyd, yum?y] together: ~ var- zišneh sexual intercourse 4319; jointly 110?9, — Paz. jumē, Skr. v. saha, samaväya (SGV IV, 101); Bailey, ZP 154; from yam-, cf s. v. yatak; cf also yat-o.
tyumbišneh [*ywmbšnyh] det. v. n.: star ~ the motion of the stars 109%. — Paz. junb- ‘to move’, v.n. junbasn; junbä ‘mover’ (SGV); NP junbidan; cf MPrth ywb- ‘to lament, to mourn’. — Text: ynbsnyh; it would have been better to correct it to ywnb- = Paz. NP.
yūnānāyik [ywn’n’yk] adj. Greek 11114. — OP yauna- ‘Tonian’.
yuvan [ywd'n', for ywb'n' with a b joined to the left] youth, a young man 135. 744; 12000 mart ~ 12028. — Av. (1305) yvan-, yavan- ; Ps. abstr. ywb’nyhy, MPrth yw’ngft (S), Paz. jugnī (Aog). — NP javān.
yuvat [ywbt', cf the spelling of the preceding w.] separately, differently: 1. kē ~ ~ pat har hazārak sar hac čiščin Evak ravét of whom each in turn will come at the beginning of every millenium 7115-16, —
#### leaf 248
utuatā, *vivatà instr. adv. of *vi-vat- *'separation, dispersion’, derived from the prep. vi as are fröt (q. v.) < *fravatä instr. of *fra-vat- (Olnd pravat- ‘mountain slope’, pravatä ‘down’) and OInd ni-vat- ‘depth’ from ni-, ud- vat- ‘height’ from ud-, ā-vat- ‘vicinity’ from d. — In compounds the antonym of ham-; examples v. below.
yuvatak separated, detached 631°. 677. 747, 169. — Paz. NP judi. Probably formed analogically after its antonym hamäk.
yuvat-datistan [-DYN’] of diverging decision, or judgment: pat vinäs — not consenting to sin in his decisions 65?”, opp. pat kirpak hamdatistan (g. v.).
yuvat-dātistānēh [-d’tst’nyh] lawless- ness, anarchy 108*; perverted judgment 11023,
yuvat-kēš [-kyš] having a differing reli- gion, unbeliever, pl. cas. obl. —-än 64%. — V. kēš.
yuvat-ristak [— lystk'] having different, diverging customs, heterodox 10918. — 10917. restore the reading ywbt' slytk'n', v. yuvat-srītak.
yuvat-ristakéh [— 1st-] heterodoxy 1083.
yuvat-sritak [— slytk'] "text not handed down (in the common traditional way): apük hamäk čišin ~-Gn mnó(k» nask ošmurt (together with =) including all these texts which were not handed down in the ordinary way he reckoned the nasks anew 109!" (restore the text of the MS and Madan!). — Av. (1637 sq.) sray- ‘to lean’; FrO XIIe srita = api- spürt (v. this w.). The secondary texts
www.parsianjoman.org | ool wok
15*
yuvat-sritak
alluded to here are probably inserted in the Pāci nask (no. 6, DkM 682-684).
yuvattar [ywbtl] v. yuvat. yuvattaréh contrariety, adversity 121, 7716,
yuvat-vēnišnēh sight 11024,
[-wynSnyh] perverted
zafar [zpl] mouth, of Ahrimanic beings 40!?. 486. — Av. (1657) zafar-; cf dahän.
zahr [z’hl] poison 919-?!, 103. 2516, 2814, 76°. — MPrth jhr; Arm. lw. Zahr; MPrs zhr (A-H I); NP zakr; < *ja@ra- ‘means for killing’, v.s. v. zatan (because of -hr Prs zahr must have been borrowed from NW).
zahyāi [zhy’y] depth 92°. 935. - < *zafydi, v. zufr; Ps. z(wp]?dy; MPrs zwp*y (List 90); Paz. zufaé (SGV); cf pahnäi.
zam- (Prth) [z?m- to let go, to shoot off (an arrow): kē tigr 6 hō šit" [zmywd] *zāmēd whoever (shall shoot off his arrow on to this cairn =) shall hit this cairn with his arrow HajA: 13-14. — Av. (496 init.) jämayeiti caus. of (493 sgg.) gam-, pres. jam- (etc.), v.s. v. āmatan; MPrth j’m’dn 7?m- ‘to convey, to conduct’, Ghilain 72. The optative in *-ēvd is still unexplained (wanting in MPrth). As the Aram. alphabet used in the official Prth. script had no special sign for Z and j the letter z had to serve also for these sounds: jām-, žām- could only be spelt z"m-. In Prs j-, ž had changed i
```


## [2026-09-06T02:26:16.506Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nd=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[248][2500:6000])\nPYEOF",
 "description": "Nyberg zamān entry"
}
```


### [2026-09-06T02:26:18.138Z] TOOL RESULT

```
 had to serve also for these sounds: jām-, žām- could only be spelt z"m-. In Prs j-, ž had changed into z, but a secondary j- had developed from initial y, which was maintained in the spelling in spite of the new pronunciation (in books a point is often placed beneath it); this y-, now pronounced j-, could then if necessary be used to render a Prth j-.
```


## [2026-09-06T02:26:20.756Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"zamān \\[\\|zamän \\[\\|zamān\\b\" NYB_vol2_glossary.txt | head -10 | cut -c1-400",
 "description": "Nyberg zamān"
}
```


### [2026-09-06T02:26:20.814Z] TOOL RESULT

```
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — x
```


## [2026-09-06T02:26:25.806Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nd=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[249][:3500])\nPYEOF",
 "description": "Nyberg leaf 249"
}
```


### [2026-09-06T02:26:27.412Z] TOOL RESULT

```
 A fine example is the Prth. n. pr. z’hyn KZŠ Prth 1. 24 = Prs 1. 30 y’dyn, Gr. v. Atenv (du- for j-). Cf next w.
zaman [zm'n'], jaman [ym’n'; ‘DN? 972.19.19, 997, 10322, 10422] time, passim;
228
zan
yuxt [ywht'] a pair: č-yurt [HN? ~, v. 8. v. e] for év-yuxt, a bahuvrihi: having, implying one pair (playing a game) = a game 1187. 119%, 1201. — Av. (1301) ydata- ‘a team of horses’; NP juft < *juxt ‘a yoke, a couple, a pair’, from yaog-, V.S. v. apiyuat.
~ handäzxt he (the astrologer) calculated the time 7°; né dagr ~ bavét ka it will not be long before 2511, 2975; vārān ~ the rainy season 97%; jāyišn u zaman <i> brihčnišn rad (because of Fortune, and for the sake of Destiny's time =) by Fortune, and because the time appointed by Destiny was at hand 14!? [the izdfat after zamdn is necessary; ~ brihénisn cannot mean ‘the predestination of Time; in that case "brihčnišneh would be in- dispensable]; — adverbial: cé — be vitart? at which time did they pass? 74; hec ~ mà pai do not stop a single moment 10?9; dagr ~ 76°, dérang ~ 915 for a long time; ham ~ immediately 1679; — together with other temporal ws.: 3 rēc ~ xtdst he pondered for three days 11816; 121%; — with prep.: andar ~ in due time 2?! etc.; andar ham ~ at the same moment 12%; andar hàn ~ at that time, then 971, 10322; hambun-ic ~ nč never 9719; han and ~ cand as long as 997; adak apar pat (hàn) ~ about that time 4219, 61°; pat har gah u ~ 71%; apar pat han ~ ka at the time when 41%, — ~ as a metaphysical entity 1095; pat ~ + akanärak (g.v.) 778. — MPrth jmn; Arm. lw. Zam, Zamanak (v. next w.); M Prs zm’n; Paz. jamqn (SGV), zamq; NP zamün; zaman and zamdn loaned into Aram and Arab. From gam-, v. āmatan and zàm-.
zamünak [zm’nk'] period, epoch 105%, 10611,
zan [NYSH; zn'] woman, wife, passim; pl. eas. obl. —-än [NYSH-n'] 823, 915
WWW .parsianjoman.org | oe zl ww
(used as cas. rect. pl.). 1411. 5312; dāt i —-ün marriageable age 14°; ~ kartan to marry 6316, ~ xdstan id. 675; kē 6 ~ + kārān šavet 834: Paz. 6 zan 1 kasą ‘to (other) people’s woman’, using the same expression as 6926 where adultery is meant: (Phl) hac — % kasān pahréxtar bas ‘keep away from (people's =) other men’s woman’; West referred both pass- ages to adultery, translating in both places ‘wives of others’, but the Skr v. differentiates: 69?8 stritah anyegām pra- yatnakārī bhava (adultery), but 834 yo nārīū. kesämeit prayäti (fornication). This being so, zan i kärän 83% must be the original reading, only it should be read zanē-kārān, pl. cas. obl. of *zanē-kār, a bahuvrihi ‘having (exercising) women’s profession’ = a prostitute, v.s. v. kar. — Av. (603) jani-; MPrth jn, pl. jnyn (S); MPrs zn, pl. zn "yn, znyn; Paz. zani, jan; NP zan.
izanak [znk'] jaw 50%. - MPrth zne (S); NP zanas.
2zanak (Prth) [znk] kind, sort; hō [LH- w] — ... kü in such a way ... that HajA: 8 = Prs ēgēn... kū. — Olr "zana- — Skr jana- 'race, man, tribe': OP vispa- z
```


## [2026-09-06T02:26:34.760Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['PLA'].get('page_offset'),'|',d['PLA'].get('lookup_hint'))\"; echo ===; grep -n \"zamān\\|zaman\" incoming/PLA/PLA_pages.txt | head -20 | cut -c1-300",
 "description": "Asbaghi zamān"
}
```


### [2026-09-06T02:26:37.229Z] TOOL RESULT

```
Exit code 1
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
(eval):2: == not found
```


## [2026-09-06T02:26:40.596Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; python3 - <<'PYEOF'\nd=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\np=d[145]  # leaf 146 (1-based) = printed 131?  printed = leaf-15\nprint('leaf 146 -> printed', 146-15)\nprint(p[:1500])\nPYEOF",
 "description": "Asbaghi page layout check"
}
```


### [2026-09-06T02:26:42.143Z] TOOL RESULT

```
302
leaf 146 -> printed 131
dagan                                                                131                                       rätilag


@&)>- dagan:           "Grübchen"               1 aus        pers.    &% zanah    1      syr.    PO     PP.)    2,


05> -         dJagana s. dagan.

©#> - dagün:               Pl. v. (>, dagan s. dagan.

ıl.)- damä:           "atmen"           aus     dem pers. y, dam 3,

—L5    - danab:            Pl.        v... danb        s.     danb.


3-          danb:     "Schwanz;               Ende"    pers.5 dum mp.                 6,        dumb,


a.)     -    danba     s.    d         b.


25     -     dunüb:        Pl.        v..,;    danb     s.    danb.


Ol»>         - dinübän:               "langgeschwänzt".


>     - gain:         "Mangel"              pers.     „|,     ziyan     “m.       irus    Ziyäan   <aw.    zyäna,    talm.
       Lw.        zyy’n”         5,


                                                                      [E)




ob- rä’ig:                 "gängig,            gefragt"        sub          räyig u.gl,, rawäß.

gun           -     rätiyänaß:              '"Resina"        pers.    6,


LS)               - ratiyänagf: Nisba v. p2u|;l, rätiyänaf ga. v.

 Sry - ratilaf = rätinag                              s. rätinag 7,



1.    Kiyas.          v.
2.    Brockelmann                s.    v.
9.    Addai         Scher        s.    v.
4.    ebda.
5.    ebda.
6.    ebda.
7.    ebda,.
```


## [2026-09-06T02:26:46.647Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; python3 - <<'PYEOF'\nd=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[160][:2200])\nPYEOF",
 "description": "Asbaghi page 146"
}
```


### [2026-09-06T02:26:50.668Z] TOOL RESULT

```
zufäna                                                                                  146                                                    zanburak



ob;          -           zufäna:            "Zunge;           Spitze         am        Pferdezügel"             aus   pers.      zaban        q.    v.


&»,-         zift:              "mit         Harz          od.    Pech      bestreichen;               verpichen"           s.    flg.    pers.             ?.


au)-         zift:              "Fichtenharz;                     Pech".


_>3-         zagar:                   "Rad"       Metathese             v. & Carb.

        .                    =, =                                                                                              9
a»           -           zuläbi:            "gezuckerter                Pfannkuchen!                 pers.       2, syr.      Kan,


as); _ zaläbiyya = zuläbI s. zuläbl *.

&P,; - zuläli:                              PI.       v.     zilliyya         s.        zilliyya.

aus,             -       zalabiya:                für        zalabiyya            q.    v.

a;           - zilliyya:                         "ungestreifte wollene                          Decke ohne Haar"                      pers.         zilu .

lo,     - zaman:                       "Zeit,           Epoche,         Jahreszeit,              Saison!"         pers.    QJL;    prth.           Jm’n
            mp.                       \rt5 Zzamän,            paz.         jaman,
            zaman            u.        jaman          sind       Über      das         Aram.    ins    Ar.       gelangt.
        v.               Verb &,; ämadan                      "kommen" T                 mp. yre® ämatan              am.        / ap. gam              5, mand.
            zaman                 .


«2%; - zamänT:                              "zeitlich,             weltlich"                 Nisba    v.     zamän.


eb)                  - zamanidin:                     "zu eben          der Zeit".

>,>%)                -    zamäward:               "Speise            aus     Mehl,           Mandeln       u.    Honig"       pers.      7,


Zur) -
```


## [2026-09-06T02:26:59.852Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"simanu\\|simānu\\|Sivan\" KLN_1966.txt | head -10 | cut -c1-400; echo \"=== KLN come ===\"; grep -n \"base \\*g\\^wem\\|gwem-\\|g\\*wem\\|\\*g\\*em-\" KLN_1966.txt | head -10 | cut -c1-300",
 "description": "Klein lookups"
}
```


### [2026-09-06T02:26:59.946Z] TOOL RESULT

```
23223:mazuma,  n.,  money  (U.S.  Slang).  —  Yiddish,  fr. Mishnaic  Heb.  n/zumman,  ‘designated,  fixed, appointed’,  used  (in  the  pi.  me zummantm)  in Medieval  Heb.  Responses  in  the  sense  of  ‘cash’. Mishnaic  Heb.  rrfzumman  is  passive  part  of zimmen,  ‘he  invited,  designated,  appointed, fixed’,  a  verb  denominated  fr.  Heb.  ziman,  ‘ap¬ pointed  time,  t
31088:pursuivant,  n.,  1)  an  officer  ranking  below  a  her¬ ald;  2)  a  follower,  attendant.  —  ME .pursevant, fr.  OF.  porsuiant,  porsivant  (F.  poursuivant), pres.  part,  of  porsuir,  porsivre,  ‘to  pursue’.  See pursue  and  cp.  pursuant.
34836:Shabuoth,  n.  pi.,  the  Feast  of  Weeks,  celebrated on  the  6th  (in  the  Diaspora  also  on  the  7th)  of Sivan.  —  Heb.  shabhu'dth,  pi.  of  shabhu“‘, ‘week’,  rel.  to  shebha ‘  (masc.),  shibh'ah  (fern.), ‘seven’.  Cp.  Aram.  sh*bha‘  (masc.),  shabh'a, Ugar.  shb'  (masc.),  shb't  (fem.),  Arab,  sab' (masc.),  sab'J'  (fern.),  Ethiop.  sab'u  (masc.), s
=== KLN come ===
4506:base,  n.,  bottom;  foundation,  pedestal.  —  F.,  fr. L.  basis,  fr.  Gk.  (idci^,  ‘a  stepping,  step,  pede¬ stal,  foot,  base’,  from  the  stem  of  (3aivto,  ‘I  go’, which  prob.  stands  for  *(3avLCt>,  fr.  *P<x|z-io), fr.  l.-E.  base  *gwem-,  'to  go;  to  come’, 
8320:come,  intr.  v.  —  ME.  cumen,  comen ,  fr.  OE.  cu- man,  rel.  to  OS.  cuman,  ON.  koma,  OFris.  cuma, Du.  komen,  OHG.  queman,  koman,  MHG.  Ao¬ men,  G.  konimen,  Goth,  qiman,  ‘to  come’,  fr. I.-E.  base  *gu'em-,  ‘to  go;  to  come’,  whence  also OI.  gdrnati,  g
20132:*gwem-,  ‘to  go,  to  come’.  See  come  and  cp.  the first  element  in  Juggernaut, jaggery,  n„  coarse  dark  brown  sugar.  —  Angli¬ cized  fr.  Hind,  jagri,  fr.  OI.  sarkara,  sarkarah, ‘sugar’.  Accordingly  jaggery  is  prop,  a  doublet of  sugar  (q.v.)
30211:pp.  of  praevenire,  ‘to  come  before,  to  anticipate’, in  Late  L.  also  ‘to  prevent’,  fr.  prae  (see  pre-) and  venire,  ‘to  come’,  fr.  I.-E.  base  *gwem-,  ‘to come’,  whence  also  Goth,  qiman,  OE.  cuman, ‘to  come’.  See  come  and  cp.  venue,  ‘arri
30714:fr.  I.-E.  base  *gwem-,  ‘to  come’,  whence  also Goth,  qiman,  OE.  cuman,  ‘to  come’.  See  come and  cp.  venue,  ‘arrival’.  Cp.  also  provenience. Provencal,  adj.  and  n.  —  F.,  fr.  Provence,  fr.  L. provincia  (see  province) ;  so  called,  because  the Romans
```


## [2026-09-06T02:27:15.617Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"appointed time\" KLN_1966.txt KLN_1971.txt | head -20 | cut -c1-300; echo \"=== come entry ===\"; sed -n '8320,8326p' KLN_1966.txt",
 "description": "Klein appointed time / come"
}
```


### [2026-09-06T02:27:15.733Z] TOOL RESULT

```
KLN_1971.txt:147159:‘appointed time’. 
KLN_1971.txt:153316:fasts. — Heb. md'ed , ‘appointed time, appoint- 
=== come entry ===
come,  intr.  v.  —  ME.  cumen,  comen ,  fr.  OE.  cu- man,  rel.  to  OS.  cuman,  ON.  koma,  OFris.  cuma, Du.  komen,  OHG.  queman,  koman,  MHG.  Ao¬ men,  G.  konimen,  Goth,  qiman,  ‘to  come’,  fr. I.-E.  base  *gu'em-,  ‘to  go;  to  come’,  whence  also OI.  gdrnati,  gacchati,  ‘he  goes’,  gatdh,  ‘gone’, Avestic  jamaiti,  ‘goes’,  Toch.  A  kakmu,  B  ke- kamu,  ‘come’  (pp.),  A  kumnds,  ‘comes’,  B  kam- naskem,  ‘they  come’,  Arm.  ekn  (for  *e-gwem-t), ‘he  came’,  Gk.  (Bcdvo  (prob.  for  *(3avtco  fr.
ulm),  ‘I  go’,  L.  venib  (prob.  for  *g"mib),  ‘I come',  Mir.  beim  for  *ben-smen ),  ‘pace,  step’, Lith.  gemit,  gimti,  ‘to  be  born’,  lit.  ‘to  come’. Cp.  the  collateral  base  *gwa-  in  OI.  agarn  (aor.), Gk.  c[3r,v  (aor.),  ‘I  went’,  Gk.  ‘pace,  step’,
Siuiior,  ‘altar’,  Lett,  gaju,  ‘I  went’,  gatwa,  ‘pas¬ sage’,  Alb.  ngd,  ‘I  run’.  Cp.  welcome.  Cp.  also base,  n.,  and  words  there  referred  to.  Cp.  also venue,  ‘arrival’,  and  words  there  referred  to. Cp.  also  agama,  jagat.
come-at-able,  adj.,  accessible.  —  Formed  fr. come,  at,  and  -able.
comedian,  n.  —  F.  comedien,  fr.  comedie ,  ‘com- medy’.  See  comedy  and  -an. comedienne,  n.  —  F.  comedienne,  ‘an  actress  in comedy’,  fem.  of  comedien.  See  prec.  word, comedietta,  n.,  a  short  comedy.  —  It.  (now commedietta),  dimin.  of  comedia  (now  comme- dia),  ‘comedy’,  fr.  L.  edmoedia.  See  comedy, comedo,  n.,  blackhead  ( med .)  —  L.  comedo,  ‘a glutton’,  rel.  to  comedere,  ‘to  eat  entirely  up’, fr.  com-  and  edere,  ‘to  eat’.  See  edible  and  cp. comestible.
comedy,  n.  —  F.  comedie,  fr.  L.  edmoedia,  fr.  Gk. xu>|j.o)Sia,  ‘comedy’,  fr.  xa>|xo>86<;,  ‘comic  actor’ (orig.  ‘singer  in  the  xcojjioi;  or  comic  chorus’), contraction  of  xo>[xaoiS4s,  which  is  compound¬ ed  of  xcufxoi;,  ‘revel,  carousal,  merry-making.
318
```


## [2026-09-06T02:27:22.483Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^951$\\|^ *951 *$\" KLN_1966.txt | head; echo ===; awk 'NR>=1 && /^ *951 *$/{print NR}' KLN_1966.txt | head",
 "description": "Find Klein page 951"
}
```


### [2026-09-06T02:27:24.197Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T02:27:26.825Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"951\" KLN_1966.txt | grep -v \"[a-zA-Z]951\\|951[a-zA-Z]\" | head -20 | cut -c1-160",
 "description": "Klein page 951 marker"
}
```


### [2026-09-06T02:27:26.890Z] TOOL RESULT

```
436:Holthausen,  F.,  Etymologisches  Worterbuch  der  englischen  Sprache,  3rded.,  Gottingen,  1949. Koehler,  L.,  and  W.  Baumgartner,  Lexicon  in  Veter
2075:alabandite,  n.,  manganese  sulfide  (mineral.)  — Named  after  Alabanda  in  Asia  Minor.  For  the ending  see  subst.  suff.  -ite. alabarch,  n„ 
5238:blurb,  n.  —  Coined  by  the  American  journalist Frank  Gelett  Burgess  (1866-1951)  in  1907. blurt,  tr.  v.  —  Of  imitative  origin.  Cp.  Sc
5325:bonfire,  n.  —  ME.  bonefire,  banefire,  orig.  ‘fire made  of  bones’;  see  bone  and  fire.  —  Cp.  Ri¬ chard  Broxton  Onians,  The  Origi
10394:dawsonite,  n.,  a  basic  aluminum  sodium  carbo¬ nate  (mineral.)  —  Named  after  the  Canadian geologist  Sir  John  William  Dawson  (1865- 1951
33929:Derivatives:  Scandinavi-an,  adj.  and  n. scandium,  n.,  name  of  a  metallic  element  belong¬ ing  to  the  rare  earth  group  (chem.)  —  ModL.
39170:Thule,  n.,  classical  name  of  the  northernmost  part of  the  world.  — -  L.  Thule,  Thyle,  fr.  Gk. 0oiiXr],  0uXt).  Cp.  thulium, thulia,  n.
```


## [2026-09-06T02:27:30.710Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^[0-9]\\{3\\}$\" KLN_1966.txt | awk -F: '$2>=945 && $2<=960' | head -20",
 "description": "Klein page markers 945-960"
}
```


### [2026-09-06T02:27:32.485Z] TOOL RESULT

```
23043:945
23090:946
23091:947
23142:948
23155:949
23169:950
23233:953
23300:957
23340:958
```


## [2026-09-06T02:28:43.074Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23169,23235p' KLN_1966.txt | cut -c1-260",
 "description": "Klein pages 950-953"
}
```


### [2026-09-06T02:28:43.139Z] TOOL RESULT

```
950
maund
mande,  fr.  MDu.  mande  (Du.  mand),  ‘basket'.
Cp.  F.  marine,  ‘hand  basket ,  which  derives  fr. MDu.  mantle,  avar.  of  mande. maund,  tr.  and  intr.  v.,  to  beg  (slang).  —  Prob.  fr.
F.  mendier ,  ‘to  beg’,  fr.  L.  mendicare  (whence also  It.  mendicare,  Sp.,  Port,  mendigar).  See mendicant.
maunder,  intr.  v.,  1)  to  wander  about  aimlessly;
2)  to  mutter,  mumble.  —  Prob.  freq.  of  maund,
‘to  beg’.
Derivative:  maunder-er,  n. maundy,  n.,  1)  ceremonial  washing  of  the  feet  of poor  people;  2)  distribution  of  alms.  —  ME. maunde,  fr.  OF.  mande,  fr.  L.  manddtum,  ‘com¬ mand’,  prop.  neut.  pp.  of  mandare,  ‘to  commit to  one�
Maundy  Thursday,  n.,  Thursday  preceding  Eas¬ ter.  —  From  prec.  word.
Maurice,  masc.  PN.  —  F.,  fr.  Late  L.  Mauritius, Mauricius,  fr.  L.  Maurus,  ‘inhabitant  of  Maure¬ tania,  Moor’,  fr.  Gk.  Maupo?.  See  Moor.
Mauser,  n.,  a  kind  of  rifle.  ■ —  Named  after  the brothers  Mauser  who  invented  it  (in  the  second half  of  the  19th  cent.)
mausoleum,  n.,  a  magnificent  tomb.  —  L.  mauso¬ leum,  fr.  Gk.  MauatoXetov,  ‘tomb  of  Mausolus (king  of  Caria)’,  fr.  MouJocaXo?,  ‘Mausolus’, erected  by  his  widow  queen  Artemisia;  used apellatively,  the  word  denotes  any  magn
Derivative:  mausole-an,  adj. mauvais,  adj.,  false,  worthless;  used  in  French terms  (as  in  mauvais  sujet,  ‘worthless  fellow  , mauvaise  honte,  ‘bashfulness’,  lit.  ‘bad  shame  ).
_  F.  mauvais  (fern,  mauvaise),  ‘bad’,  fr.  VL.
malifdtius,  ‘who  has  a  bad  lot’,  which  is  com¬ pounded  of  L.  mains,  ‘bad’,  and  fatum,  ‘fate’; see  male-  and  fate.  For  the  formation  of  the word  cp.  the  PN.  Bonifatius,  lit.  ‘of  good  luck’ (see  Boniface).
mauve,  n.  and  adj.,  purple  dye.  —  F.,  fr.  L.  mal- va,  ‘mallow’.  See  mallow, maverick,  n.,  unbranded  cattle.  —  Named  after Samuel  A.  Maverick  (died  in  1870),  a  civil  en¬ gineer  in  Texas,  in  allusion  to  his  unbranded ca
mavis,  m,  the  song  thrush.  —  ME.'  mavys,  fr. IviF.  (=  F.)  mauvis,  rel.  to  Sp.  malvis,  malviz; of  unknown  origin.  MBret.  milhuit  (whence ModBret.  milc'huid,  milfid),  is  a  French  loan word.
mavrodapbne,  n.,  name  of  a  modern  Greek  wine.
_ ModGk.,  lit.  ‘black  laurel',  fr.  Late  Gk.  p.au-
po;,  ‘black,  dark’,  and  Gk.  8i<pvr„  ‘laurel’. See  Moor  and  Daphne.
maw,  n.,  1)  the  stomach  of  an  animal,  specif,  the fourth  stomach  of  a  ruminant;  2)  the  craw  or crop  of  a  bird;  3)  the  air  bladder  of  a  fish.  — ME.  mawe,  maugh,  fr.  OE.  maga,  rel.  to  OFris. maga ,  ON.  magi,  Swed.  mage, 
mage,  G.  Magen,  ‘stomach’,  and  cogn.  with  W. megin,  ‘bellows’,  and  prob.  also  with  Lith. makas,  Lett,  maks,  OSlav.  moSina,  ‘bag,  pouch'. Rhaeto-Romanic  magun,  ‘stomach’,  and  It. magune,  ‘crop  of  a  bird’,  are  Teut.
Derivatives:  mawkish-ly,  adv.,  mawkish-ness,  n. mawworm,  n.,  worm  infesting  the  stomach.
Compounded  of  maw  and  worm, maxilla,  n.,  jaw  or  jawbone.  —  L.,  ‘jawbone, jaw’,  dimin.  of  mala,  ‘cheekbone,  jawbone; cheek’;  see  mala.  Maxilla  stands  to  mala  as axilla,  ‘armpit’,  stands  to  ala,  ‘wing’, maxillary,  a
—  L.  maxillaris,  fr.  maxilla.  See  prec.  word  and adj.  suff.  -ary.
maxilliform,  adj.,  having  the  form  of  a  maxilla.
—  See  maxilla  and  -form.
maxim,  n.,  precept,  principle.  —  ME.  maxime,  fr. MF.  (=  F.)  maxime,  fr.  ML.  maxima  (short  for L.  maxima  sententia,  ‘the  greatest  sentence ), fern,  of  maximus,  ‘greatest’.  See  maximum, maximal,  adj.,  highest,  greatest.  —  
maximite,  n.,  a  synonym  of  cordite.  —  Named after  Hudson  Maxim  (1853-1927),  its  inventor. For  the  ending  see  subst.  suff.  -ite. maximize,  tr.v.,  to  raise  to  the  highest  possible degree.  —  Coined  by  the  English  philosopher Jer
n.  —  L.,  neut.  of  maximus,  greatest’, for  *mag-s6mos,  superlative  of,  and  from  the same  base  as  magnus,  ‘great’.  See  magnum  and cp.  major.
maxwell,  n.,  an  international  magnetic  unit.  — Named  after  the  Scottish  physicist  James  Clerk Maxwell  (1831-79).
may,  auxil.  v.  —  ME.  mai,  mei,  fr.  OE.  mxg,  I am  able’  (inf.  magan,  ‘to  be  able’),  rel.  to  OS. mugan,  OFris.  muga,  ON.  mega,  Norw.  moga, Dan.  maatte,  Swed.  mi,  MDu.  moghen,  Du. mogen,  OHG.  magan,  mugan,  MHG.  mugen, m
ct
ment’,  (i^yavr],  ‘means,  invention,  machine’, OSlav.  mogq,  mosti,  ‘to  be  able’,  moSti,  ‘power; force’.  OPruss.  massi,  T  can’,  is  a  Teut.  loan word.  See  mechanic  and  cp.  main,  might,  dis¬ may,  Hogen  Mogen  and  the  
may,  n.,  a  maiden  (archaic).  —  ME.  may,  mey, fr.  OE.  maeg,  ‘woman,  virgin’,  rel.  to  OE.  mxged, mxgd,  ‘maid’.  See  maiden  and  cp.  mayweed. May,  n.,  the  fifth  month  of  the  year.  —  ME.  mai, fr.  OF.  (=  F.)  mai,  fr.  
Mayaca,  n.,  a  genus  of  plants  (hot.)  —  ModL.,  of S.  Amer.  Indian  origin.
Mayaceae,  n.  pi.,  the  mayaca  family  (hot.)  — ModL.,  formed  fr.  prec.  word  with  suff’.  -aceae. mayaceous,  adj.  —  See  prec.  word  and  -aceous. maybe,  adv.  —  Compounded  of  may,  auxil.  v., and  be.
mayday,  an  international  radiotelephone  dis¬ tress  signal.  —  F.  m’aidez,  ‘help  me",  fr.  apos¬ trophized  form  of  me,  ‘me’  (fr.  L.  me)  and  im- per.  of  aider,  to  help’  (fr.  L.  adjutare).  See  me and  aid,  v.
mayhem,  n.,  the  maiming  of  a  person  (law).  — ME.  maym,  fr.  AF.  mayhem,  mahaim,  ‘injury’, corresponding  to  OF.  mehaigne,  mahaigne,  me- haing,  of  s.m.,  fr.  OF.  mahaignier,  ‘to  ‘injure’. See  maim.
mayonnaise,  n.,  a  creamy  sauce  made  of  egg yolks,  oil  and  vinegar.  —  F.,  short  for  sauce mayonnaise,  for  sauce  mahonnaise,  ‘sauce  of Mahon*;  so  called  fr.  Mahon,  a  town  on  the island  of  Minorca,  in  commemoration  of  the cap
Derivatives:  mayor-al,  adj.,  mayoralty  (q.v.), mayor-ess,  n.
mayoralty,  n.  —  ME.  mairaltee,  fr.  MF.  mairalte, fr.  maire,  ‘mayor’.  See  mayor,  adj.  suff.  -al  and suff.  -ty.
mayweed,  n.,  the  stinking  camomile.  —  For * maythe-weed,  fr.  OE.  magede,  magode,  mse- gede,  ‘the  stinking  camomile’,  which  is  prob. rel.  to  OE.  mxged,  mxgd,  ‘maid';  see  maiden and  cp.  may,  ‘a  maiden’.  For  the  second  
—  Named  after  Mazapil,  in  Zacatecas,  Mexico. For  the  ending  see  subst.  suff.  -ite.
mazard,  n.,  1)  a  mazer  (obsol.);  2)  the  head  or skull  (obsol.)  —  Altered  fr.  mazer.
Mazdaism,  also  Mazdeism,  n.,  Zoroastrianism.
—  See  Ormazd  and  -ism.
mead
maze,  tr.  v.,  to  bewilder;  to  confuse.  —  ME. masen,  mazen,  ‘to  confuse,  puzzle’,  fr.  OE. rnasian  in  amasian,  ‘to  confuse,  confound’, which  is  rel.  to  OE.  amasod,  ‘confused,  con¬ founded’,  and  prob.  also  to  Norw.  m
maze,  n.,  a  labyrinth.  —  ME.  mase,  maze,  fr. masen,  mazen.  See  maze,  v.
Derivatives:  maz-y,  adj.,  maz-i-ly,  adv.,  maz-i- ness,  n.
mazer,  n.,  a  large  drinking  bowl.  —  ME.  maser, ‘maple  wood ;  bowl  made  of  maple  wood’,  fr. OF.  masere,  ‘maple  wood’,  which  is  of  Teut. origin.  Cp.  ON.  mosurr,  ‘maple  wood’,  mosurr bolli,  ‘bowl  made  of  maple  wood
which  stands  for  *p.aY-ia,  fr.  (xacraco  (for  *pd- yito),  ‘I  squeeze,  press  into  a  mold,  knead’, whence  also  ftayii;  ’kneaded  mass,  cake’,  fj.ee- ysus,  ‘one  who  kneads,  baker’.  See  macerate  and cp.  magma.
mazuma,  n.,  money  (U.S.  Slang).  —  Yiddish,  fr. Mishnaic  Heb.  n/zumman,  ‘designated,  fixed, appointed’,  used  (in  the  pi.  me zummantm)  in Medieval  Heb.  Responses  in  the  sense  of  ‘cash’. Mishnaic  Heb.  rrfzumman  is  passive  pa
mazurka,  mazourka,  n.,  1)  a  lively  Polish  dance; 2)  music  for  this.  —  Pol.  mazurka,  ‘a  woman  of the  province  Mazovia  (in  Poland)’, mazzard,  n.,  wild  sweet  cherry  (Prunus  avium).  — Fr.  earlier  mazer  (see  mazer) ;  so  call
mead
meco-
MDu.mede,  Du.  mee,  OHG.  metu,  MHG.  mete, met ,  G.Me/,‘mead’,  fr.I.-E.  base*meff/m-,‘honey, sweet  drink',  whence  also  Ol.mddhu, ‘sweet,  sweet drink,  wine,  honey’,  Toch.  B  mit,  honey  ,  Gk. (a£$u,  ‘wine’,  [xe^uetv,  ‘to  b
meadow,  n.  —  ME.  medwe,  medewe,  fr.  OE.  mSd- we,  gen.  of  mid  (see  prec.  word);  rel.  to  Du. made,  G.  Matte,  ‘meadow’,  and  to  OE.  mzp, ‘harvest,  crop’,  OHG.  mad,  ‘a  mowing ,  fr. WTeut.  *mdpa-,  lit.  ‘that  which  is 
Derivative:  meadow-y,  adj. meager,  meagre,  adj.  —  ME.  megre,  fr.  OF. maigre,  magre,  megre  (F.  maigre),  fr.  L.  macer, ‘lean,  thin’,  which  is  cogn.  with  Gk.  paxp6?, ‘long’,  OE.  mseger,  ON.  magr,  MDu.  magher, Du  mager,  OHG
Derivatives:  meager-ly,  meagre-ly,  adv.,  meager¬ ness,  meagre-ness,  n.
meal,  n.,  edible  grain.  —  ME.  mele,  fr.  OE.  me  hi, rel.  to  OS.  me/e,  ON.,  Swed.,  Norw.  mjdl,  Dan. met  OFris.  mele,  MDu.  mele,  Du.  meet,  OHG. melo,  MHG.  mel,  G.  Mehl,  ‘meal’,  orig.  ‘that which  is  ground’,  and  rel.  
95Z
953
sense  development  cp.  Rum.  tandr,  young  ,  fr- L.  tener,  ‘soft,  tender’),  OPruss.  maldaisin  (acc.), ‘youngest’,  maldian,  ‘foal’,  OSlav.  mladu,  Russ. molodH,  ‘young’,  OE.  meltan,  mieltan,  ‘to  melt', prob.  also  OIr.  me
Derivatives:  meal-y,  adj.,  meal-i-ness,  n. meal,  n.,  food  taken  at  one  time.  —  ME.  mele,  fr. OE.  mil,  ‘mark,  sign ;  measure;  fixed  time;  time for  taking  food,  meal’,  rel.  to  ON.  mal,  ‘meas¬ ure,  time,  meal’,  OFris.  m
```


## [2026-09-06T02:28:55.131Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"sivan\\|siwan\\|sim[aä]n\" KLN_1971.txt | head -10 | cut -c1-250; echo \"=== zeman/zaman in KLN ===\"; grep -n -i \"zeman\\|zamàn\\|zaman\" KLN_1966.txt | head -10 | cut -c1-200",
 "description": "Klein Sivan/zaman"
}
```


### [2026-09-06T02:28:55.217Z] TOOL RESULT

```
147158:derive directly or indirectly fr. Akkad, simanu , 
196308:fr. OF. porsuiant , porsivant (F. poursuivant), 
219547:Sivan. — He b. shdbhu' , 3th , pi. of shabhd a \ 
=== zeman/zaman in KLN ===
23223:mazuma,  n.,  money  (U.S.  Slang).  —  Yiddish,  fr. Mishnaic  Heb.  n/zumman,  ‘designated,  fixed, appointed’,  used  (in  the  pi.  me zummantm)  in Medieval  Heb.  Responses  in  the
```


## [2026-09-06T02:28:57.483Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '147145,147170p' KLN_1971.txt",
 "description": "Klein 1971 simanu passage"
}
```


### [2026-09-06T02:28:57.550Z] TOOL RESULT

```
yeiic, ‘one who kneads, baker’. See macerate and 
cp. magma. 

mazuma, n., money (Cl.S. Slang). — Yiddish, fr. 
Mishnaic Heb. m^zumman, ‘designated, fixed, 
appointed’, used (in the pi. m*zummdntm) in 
Medieval Heb. Responses in the sense of ‘cash’. 
Mishnaic Heb. m^zumman is passive part of 
zimmen, ‘he invited, designated, appointed, 
fixed’, a verb denominated fr. Heb. z*man, ‘ap- 
pointed time, time’, which is rel. to Aram. 
z 6 man, Syr. z*bhan, zabhna , Arab, zaman , za- 
man, Ethiop. zaman, ‘time’. All these words 
derive directly or indirectly fr. Akkad, simanu , 
‘appointed time’. 

mazurka, mazourka, n., 1) a lively Polish dance; 
2) music for this. — Pol. mazurka , ‘a woman of 
the province Mazovia (in Poland)’, 
mazzard, n., wild sweet cherry ( Prunus avium). — 
Fr. earlier mazer (see mazer) ; so called in allu- 
sion to the knotty appearance of the wood, 
me, pers. pron. — ME. me, fr. OE. me, rel. to 
ON., Goth. mik y OHG. mih, G. mich, ‘me’ ‘(acc.), 
ON. mer, OHG., MHG., G. mir , Goth, mis, 
‘me’ (dat.), and cogn. with OI., Avestic ma, OI.
```


## [2026-09-06T02:29:15.424Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,40p' /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T02:29:15.475Z] TOOL RESULT

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
```


## [2026-09-06T02:29:21.164Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-\" \\\n \"https://en.wiktionary.org/wiki/زمان\" \\\n \"https://en.wiktionary.org/wiki/جاه\" \\\n \"https://en.wiktionary.org/wiki/انجمن\" \\\n \"https://en.wiktionary.org/wiki/گاه\" \\\n \"https://en.wiktionary.org/wiki/نیام\" \\\n \"https://en.wiktionary.org/wiki/پیغام\" \\\n \"https://en.wiktionary.org/wiki/آمدن\" \\\n \"https://en.wiktionary.org/wiki/هنگام\" \\\n \"https://en.wiktionary.org/wiki/انجام\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 202, root Gwa/Gwem, checking Nourai's Iranian derivations\" 2>&1 | tail -1\ndone",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-06T02:29:28.948Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a66b309163ff6ce8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9a98d7bb3ece8bc3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/04e15978808644e0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bfaa3a28a7334bd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b571c26450759f84.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7cd92a2725db60e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29061e5b190a4ba3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a56a33dafaea2faa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/914f3ecc7de978ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec4339cba2f13d11.txt
```


## [2026-09-06T02:29:32.740Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 9a98d7bb3ece8bc3 04e15978808644e0; do echo \"########## $f\"; python3 - \"$f.txt\" <<'PYEOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('Persian')\nprint(t[:60])\nfor kw in ['Etymology']:\n    for m in re.finditer(kw,t):\n        print('---',t[m.start():m.start()+700].replace('\\n',' '))\nPYEOF\ndone",
 "description": "Read zamān and jāh wiktionary"
}
```


### [2026-09-06T02:29:34.356Z] TOOL RESULT

```
########## 9a98d7bb3ece8bc3
URL: https://en.wiktionary.org/wiki/زمان
FETCHED: 2026-09-06
--- Etymology    2.3   Pronunciation    2.4   Noun    2.4.1   Declension    2.4.2   Derived terms    2.4.3   Descendants    2.5   References    3   Central Kurdish    Toggle Central Kurdish subsection    3.1   Etymology    3.2   Pronunciation    3.3   Noun    4   Chadian Arabic    Toggle Chadian Arabic subsection    4.1   Etymology    4.2   Adverb    4.2.1   Usage notes    4.3   References    5   Khalaj    Toggle Khalaj subsection    5.1   Noun    5.1.1   Declension    6   Malay    Toggle Malay subsection    6.1   Noun    7   Ottoman Turkish    Toggle Ottoman Turkish subsection    7.1   Etymology    7.2   Noun    7.2.1   Declension    7.2.2   Derived terms    7.2.3   Descendants    8   Persian  
--- Etymology    3.2   Pronunciation    3.3   Noun    4   Chadian Arabic    Toggle Chadian Arabic subsection    4.1   Etymology    4.2   Adverb    4.2.1   Usage notes    4.3   References    5   Khalaj    Toggle Khalaj subsection    5.1   Noun    5.1.1   Declension    6   Malay    Toggle Malay subsection    6.1   Noun    7   Ottoman Turkish    Toggle Ottoman Turkish subsection    7.1   Etymology    7.2   Noun    7.2.1   Declension    7.2.2   Derived terms    7.2.3   Descendants    8   Persian    Toggle Persian subsection    8.1   Etymology    8.2   Pronunciation    8.3   Noun    8.3.1   Derived terms    8.3.2   Descendants    9   South Levantine Arabic    Toggle South Levantine Arabic subsection 
--- Etymology    4.2   Adverb    4.2.1   Usage notes    4.3   References    5   Khalaj    Toggle Khalaj subsection    5.1   Noun    5.1.1   Declension    6   Malay    Toggle Malay subsection    6.1   Noun    7   Ottoman Turkish    Toggle Ottoman Turkish subsection    7.1   Etymology    7.2   Noun    7.2.1   Declension    7.2.2   Derived terms    7.2.3   Descendants    8   Persian    Toggle Persian subsection    8.1   Etymology    8.2   Pronunciation    8.3   Noun    8.3.1   Derived terms    8.3.2   Descendants    9   South Levantine Arabic    Toggle South Levantine Arabic subsection    9.1   Etymology    9.2   Pronunciation    9.3   Noun    9.4   Adverb    9.4.1   See also    Toggle the table of
--- Etymology    7.2   Noun    7.2.1   Declension    7.2.2   Derived terms    7.2.3   Descendants    8   Persian    Toggle Persian subsection    8.1   Etymology    8.2   Pronunciation    8.3   Noun    8.3.1   Derived terms    8.3.2   Descendants    9   South Levantine Arabic    Toggle South Levantine Arabic subsection    9.1   Etymology    9.2   Pronunciation    9.3   Noun    9.4   Adverb    9.4.1   See also    Toggle the table of contents    زمان    23 languages    العربية   فارسی   Na Vosa Vakaviti   Français   Hrvatski   Magyar   Bahasa Indonesia   日本語   ಕನ್ನಡ   한국어   Kurdî   Limburgs   ລາວ   Lietuvių   Malagasy   Minangkabau   Bahasa Melayu   Polski   پښتو   Русский   Тоҷикӣ   Türkçe   中文   
--- Etymology    8.2   Pronunciation    8.3   Noun    8.3.1   Derived terms    8.3.2   Descendants    9   South Levantine Arabic    Toggle South Levantine Arabic subsection    9.1   Etymology    9.2   Pronunciation    9.3   Noun    9.4   Adverb    9.4.1   See also    Toggle the table of contents    زمان    23 languages    العربية   فارسی   Na Vosa Vakaviti   Français   Hrvatski   Magyar   Bahasa Indonesia   日本語   ಕನ್ನಡ   한국어   Kurdî   Limburgs   ລາວ   Lietuvių   Malagasy   Minangkabau   Bahasa Melayu   Polski   پښتو   Русский   Тоҷикӣ   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View histor
--- Etymology    9.2   Pronunciation    9.3   Noun    9.4   Adverb    9.4.1   See also    Toggle the table of contents    زمان    23 languages    العربية   فارسی   Na Vosa Vakaviti   Français   Hrvatski   Magyar   Bahasa Indonesia   日本語   ಕನ್ನಡ   한국어   Kurdî   Limburgs   ລາວ   Lietuvių   Malagasy   Minangkabau   Bahasa Melayu   Polski   پښتو   Русский   Тоҷикӣ   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download
--- Etymology  [ edit ]    Root    ز م ن ( z m n )    11 terms    From a form of Aramaic 𐡆𐡌𐡍𐡀 ( zmnʾ ) , from a late pronunciation of Old Persian *jamānā ( “ time ” ) (from which Middle Persian 𐫉𐫖𐫀𐫗 ( zmʾn /⁠zamān⁠⁠/ ) , 𐭥𐭣𐭭𐭠 ( ODNA /⁠zamān⁠/ ) ), from Proto-Iranian *ǰámaHnaH , see there for more.   Pronunciation  [ edit ]    IPA ( key ) : /za.maːn/    Noun  [ edit ]    زَمَان • ( zamān )  m ( plural أَزْمِنَة ( ʔazmina ) )    ( uncountable and countable ) time   Synonym: زَمَن ( zaman )   Coordinate term: مَكَان ( makān )    age (A particular period of time in history)   season   أَزْمِنَةُ ٱلسَّنَةِ هِيَ: ٱلْخَرِيفُ وَٱلشِّتَاءُ وَٱلرَّبِيعُ وَٱلصَّيْفُ ʔazminatu s-sanati hiya: l-ḵarīfu waš-ši
--- Etymology  [ edit ]    From Proto-Iranian *hijwáH (compare Persian زوان ( zavân ) / زبان ( zabân ) , Pashto ژبه ( žəba ) , Avestan 𐬵𐬌𐬰𐬎𐬎𐬁 ( hizuuā ) ), from Proto-Indo-Iranian *ȷ́iȷ́ʰwáH (compare Sanskrit जिह्वा ( jihvā ) , Hindi जीभ ( jībh ) ), from Proto-Indo-European *dn̥ǵʰwéh₂s (compare Old Prussian insuwis , Russian язы́к ( jazýk ) , French langue , English tongue ).   Pronunciation  [ edit ]    IPA ( key ) : /zmaːn/    Hyphenation: ز‧مان    Noun  [ edit ]    Northern Kurdish   ziman    Central Kurdish   زمان ( zman )    زمان ( ziman )    tongue    language    Chadian Arabic  [ edit ]    Etymology  [ edit ]    Inherited from Arabic زَمَان ( zamān ) .   Adverb  [ edit ]    زمان • ( zamān
--- Etymology  [ edit ]    Inherited from Arabic زَمَان ( zamān ) .   Adverb  [ edit ]    زمان • ( zamān )    long ago   2019 , الكتاب المقدس بالعربي الدارجي هنا تشاد [ The Bible in Chadian Arabic ]‎ [2] , N'Djamena: Alliance biblique du Tchad, أعمال الرُسُل [ Acts ] 15:18: الْمَعْرُوف منِ زَمَان [he has made these things] known from the earliest times .    used to form the past tense of the copula : was , were   هو زمان كريم ― hu zamān karīm. ― He was generous.    Usage notes  [ edit ]    The past tense of the copula is usually implicit, however زمان or كان can also be used to express the past notion. While زمان is uninflected, كان changes in form according to the subject. [ 1 ]    References  
--- Etymology  [ edit ]    Borrowed from Classical Persian زَمَان ( zamān ) .   Noun  [ edit ]    زمان • ( zamân )    time   Synonym: وقت ( vaḳd )    Declension  [ edit ]    Declension of زمان ( zamân )    singular   plural   nominative   زمان ( zamân )    زمانلر ( zamânlar )    definite accusative   زمانی ( zamânı )    زمانلری ( zamânları )    dative   زمانه ( zamâna )    زمانلره ( zamânlara )    locative   زمانده ( zamânda )    زمانلرده ( zamânlarda )    ablative   زماندن ( zamândan )    زمانلردن ( zamânlardan )    genitive   زمانك ( zamânıñ )    زمانلرك ( zamânlarıñ )    Possessive forms   1st person singular   singular   plural   nominative   زمانم ( zamânım )    زمانلرم ( zamânlarım )    de
--- Etymology  [ edit ]    From Middle Persian 𐭥𐭣𐭭𐭠 ( ODNA /⁠zamān⁠/ ) , 𐭦𐭬𐭠𐭭𐭩 ( ẕmʾn' /⁠zamān⁠/ ) , 𐭦𐭬𐭭𐭩 ( zmn' /⁠zamān⁠/ ) , 𐫉𐫖𐫀𐫗 ( zmʾn /⁠zamān⁠/ ) , from Old Persian *jamānā ; see there for more.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /za.ˈmaːn/    ( Dari, formal ) IPA ( key ) : [zä.mɑ́ːn]    ( Dari, formal ) IPA ( key ) : [zä.mɑ́ːn]   ( Kabuli ) IPA ( key ) : [zä.mɑ́ːn]    ( Hazaragi ) IPA ( key ) : [zä.mɔ́ːn]    ( Iran, formal ) IPA ( key ) : [zæ.mɒ́ːn]    ( Tajik, formal ) IPA ( key ) : [zä.mɔ́n]    Rhymes: -aːn    Readings   Classical reading ?    zamān   Dari reading ?    zamān   Iranian reading ?    zamân   Tajik reading ?    zamon   Noun  [ edit ]    زمان • (
--- Etymology  [ edit ]    Inherited from Arabic زَمَان ( zamān ) .   Pronunciation  [ edit ]    IPA ( key ) : /za.maːn/ , [zaˈmæːn] , [zaˈmaːn]    Audio ( Amman ) : ( file )    Noun  [ edit ]    زمان • ( zamān )  m ( plural زمانات ( zamānāt ) )    time , period , era ( in the past )   كان عايش على زمان الأتراك . kān ʕāyeš ʕala zamān il-ʔatrāk He lived in the Ottoman period. (literally, “ He was living in the time of the Turks. ”)    ( definite ) long ago   انتا متذكر كيف كانت أيّام زمان ؟ enta mitzakker kīf kānat ʔayyām zamān ? Do you remember how the old days used to be? (literally, “ Do you remember how the days of long ago were? ”)    Adverb  [ edit ]    زمان • ( zamān )    (in a) long time 
########## 04e15978808644e0
URL: https://en.wiktionary.org/wiki/جاه
FETCHED: 2026-09-06T
--- Etymology    1.2   Pronunciation    1.3   Noun    1.3.1   Derived terms    Toggle the table of contents    جاه    7 languages    فارسی   Magyar   Kurdî   Malagasy   پښتو   Русский   Türkçe    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Etymology  [ edit ]    Borrowed fr
--- Etymology  [ edit ]    Borrowed from Arabic جَاه ( jāh ) , from Middle Persian [Book Pahlavi needed] ( gʾs ) , 𐫃𐫀𐫍 ( gʾh /⁠gāh⁠/ , “ place, throne, bed; time ” ) . Doublet of گاه ( gâh ) , see there for more.    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈd͡ʒaːh/    ( Dari, formal ) IPA ( key ) : [d͡ʒɑːʱ]    ( Dari, formal ) IPA ( key ) : [d͡ʒɑːʱ]   ( Kabuli ) IPA ( key ) : [d͡ʒɑː]    ( Hazaragi ) IPA ( key ) : [d͡ʒɔː]    ( Iran, formal ) IPA ( key ) : [d͡ʒɒːʱ]    ( Tajik, formal ) IPA ( key ) : [d͡ʒɔʱ]    Rhymes: -aːh    Readings   Classical reading ?    jāh   Dari reading ?    jāh   Iranian reading ?    jâh   Tajik reading ?    joh   Noun  [ edit ]    Dari   جاه    Ira
```


## [2026-09-06T02:29:45.752Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in a66b309163ff6ce8 b571c26450759f84 7cd92a2725db60e6 29061e5b190a4ba3; do echo \"########## $f\"; python3 - \"$f.txt\" <<'PYEOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nprint(t[:60])\nidx=[m.start() for m in re.finditer(r'Etymology  \\[ edit \\]',t)]\nfor i in idx[:6]:\n    print('---',t[i:i+800].replace('\\n',' '))\nPYEOF\ndone",
 "description": "Read wiktionary gāh, niyām, payghām, PIE"
}
```


### [2026-09-06T02:29:47.445Z] TOOL RESULT

```
########## a66b309163ff6ce8
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Ind
########## b571c26450759f84
URL: https://en.wiktionary.org/wiki/گاه
FETCHED: 2026-09-06T
########## 7cd92a2725db60e6
URL: https://en.wiktionary.org/wiki/نیام
FETCHED: 2026-09-06
########## 29061e5b190a4ba3
URL: https://en.wiktionary.org/wiki/پیغام
FETCHED: 2026-09-0
```


## [2026-09-06T02:29:53.224Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in a66b309163ff6ce8 b571c26450759f84 7cd92a2725db60e6 29061e5b190a4ba3 a56a33dafaea2faa 914f3ecc7de978ef ec4339cba2f13d11 bfaa3a28a7334bd4; do echo \"########## $f\"; python3 - \"$f.txt\" <<'PYEOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nprint(t[:55].replace('\\n',' '))\nidx=[m.start() for m in re.finditer(r'Etymology',t)]\nseen=0\nfor i in idx:\n    seg=t[i:i+600].replace('\\n',' ')\n    if 'edit' in seg[:30] or 'From' in seg[:120]:\n        print('---',seg); seen+=1\n    if seen>=4: break\nPYEOF\ndone",
 "description": "Extract etymology sections"
}
```


### [2026-09-06T02:29:55.281Z] TOOL RESULT

```
########## a66b309163ff6ce8
URL: https://en.wiktionary.org/wiki/Reconstruction:Prot
--- Etymology  [ edit ]    Perhaps some variation or gradation of *gʷeh₂- , hypothetically seen also on the pairs *men-dʰ(H)-  : *meh₂-dʰ(H)- and *drem-  : *dreh₂- ( “ to run ” ) . This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term.    Root  [ edit ]    *gʷem- ( perfective ) [ 1 ] [ 2 ]    to come , [ 3 ] to step [ 4 ]   Synonyms: *gʷeh₂- , *melh₃-    Derived terms  [ edit ]    Terms derived from the Proto-Indo-European root *gʷem- (98 c, 0 e)    *gʷém-t ~ *gʷm-ént ( athematic root aorist )    *gʷe-gʷóm-e ~ *gʷe-gʷm-ḗr ( stative )    *gʷm̥-sḱé-ti ( sḱe
########## b571c26450759f84
URL: https://en.wiktionary.org/wiki/گاه FETCHED: 2026-0
--- Etymology 1  [ edit ]    From Middle Persian [Book Pahlavi needed] ( gʾs ) , 𐫃𐫀𐫍 ( gʾh /⁠gāh⁠/ , “ place, throne, bed; time ” ) , from Old Persian [script needed] ( gāθu- , “ place; throne, chair ” ) , from Proto-Iranian *gātu- / *gāθu- , from Proto-Indo-Iranian [Term?] , from Proto-Indo-European *gʷem- ( “ to step ” ) . Cognate with Avestan 𐬔𐬁𐬙𐬎 ( gātu , “ place, seat, throne ” ) and Sanskrit गातु ( gātú , “ going; way; place ” ) , and Northern Luri گێ ( gı , “ time, shift ” ) . Compare the Iranian borrowings: Old Armenian գահ ( gah ) , Classical Syriac ܓܗܐ ( gāhā ) , Arabic جَاه ( jāh ) . Do
--- Etymology 2  [ edit ]    Inherited from Middle Persian [Book Pahlavi needed] ( gʾs /⁠gāh⁠/ , “ Gatha ; hymn, song ” ) , from Avestan 𐬔𐬁𐬚𐬁 ( gāθā , “ Gatha ; song ” ) , from Proto-Indo-Iranian *gaHtʰás ( “ song ” ) from Proto-Indo-European *g⁽ʷ⁾eH-tHó-s , from the root Proto-Indo-European *g⁽ʷ⁾eH- ( “ to sing, cry ” ) .   Noun  [ edit ]    گاه • ( gāh / gâh ) ( Tajik spelling гоҳ )    ( archaic ) hymn , song    ( Can we verify ( + ) this sense?) Gatha , the most archaic segment of the Avesta , composed by Zoroaster himself   Derived terms  [ edit ]    دستگاه ( dast-gâh , “ dastgah ” )   سه‌گاه 
--- Etymology  [ edit ]    Inherited from Sanskrit घास ( ghāsa ) .   Noun  [ edit ]    گاهُ • ( gāhu )  m ( Devanagari गाहु )    grass , forage , fodder , hay    References  [ edit ]    Parmanand, Mewaram ( 1910 ), “ گاهُ ”, in Sindhi-English Dictionary , Hyderabad, Sindh: The Sind Juvenile Co-operative Society    Khānu, Balocu (1960– 1988 ), “ گاهُه ”, in Jāmiʻ Sindhī lughāta (in Sindhi), Hyderabad, Sindh: Sindhī Adabī Borḍ    Retrieved from " https://en.wiktionary.org/w/index.php?title=گاه&oldid=91602607 "   Categories : Persian terms with IPA pronunciation   Rhymes:Persian/aːh   Rhymes:Persian/
########## 7cd92a2725db60e6
URL: https://en.wiktionary.org/wiki/نیام FETCHED: 2026-
--- Etymology  [ edit ]    Inherited from Middle Persian 𐫗𐫏𐫏𐫀𐫖 ( nyyʾm ) , 𐫗𐫏𐫀𐫖 ( nyʾm /⁠niyām⁠/ ) . Based on an Old Persian *nidāmān- ( “ covering, envelope ” ) .   Cognate to Wakhi [script needed] ( naẟün , “ scabbard ” ) and Sanskrit निधानम् ( nidhānam , “ act of laying down, depositing, deposit; keeping; preserving; place where something is deposited or kept, receptacle ” ) .   Also borrowed into Biblical Hebrew נָדָן ( nāḏā́n ) found in the Tanakh only in 1 Chronicles  21:27 and into Biblical Aramaic , Jewish Palestinian Aramaic , Jewish Literary Aramaic , נִידְנַה ( niḏnā ) , נִדְנַה ( niḏnā
########## 29061e5b190a4ba3
URL: https://en.wiktionary.org/wiki/پیغام FETCHED: 2026
--- Etymology  [ edit ]    Inherited from Middle Persian pgtʾm , compare Manichaean Middle Persian pygʾm , Sogdian [script needed] ( patγām ) , Northern Kurdish pêxemet ( “ sake, in the name of ” ) , pêxem ( “ barrier, obstacle; from the sense of "come against" ” ) , Central Kurdish پێخەم ( pêxem , “ barrier, hindrance; answer ” ) . Ultimately from Old Iranian , from Proto-Iranian *pati- ( “ against ” ) + a formation derived from Proto-Iranian *gam- ( “ to come ” ) , the latter from Proto-Indo-Iranian *gam- , from Proto-Indo-European *gʷem- ( “ to come, step ” ) . Compare also Iranian borrowings: 
--- Etymology  [ edit ]    Borrowed from Classical Persian پَیْغَام ( payġām ) .   Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /pɛː.ɣɑːm/    Audio ( Pakistan ) : ( file )    Rhymes: -ɑːm    Noun  [ edit ]    پَیغام • ( paiġām )  m ( Hindi spelling पैग़ाम )    message   Synonyms: خَبَر ( xabar ) , سَنْدیش ( sandeś ) , سَماچار ( samācār ) , رِسالَہ ( risāla )    advice    References  [ edit ]    “ پیغام ”, in اُردُو لُغَت ( urdū luġat ) (in Urdu), Ministry of Education: Government of Pakistan, 2017 .   “ پیغام ”, in ریخْتَہ لُغَت ( rexta luġat ) - Rekhta Dictionary [ Urdu dictionary w
########## a56a33dafaea2faa
URL: https://en.wiktionary.org/wiki/آمدن FETCHED: 2026-
--- Etymology  [ edit ]    From Proto-Iranian *ā- + *gam- ( “ to come ” ) , from Proto-Indo-European *h₂éd ( “ to, at ” ) + *gʷem- ( “ to walk, to step, to come ” ) ; [ 1 ] [ 2 ] [ 3 ] exact cognate with English advent , and partial cognate with English come . The present stem comes from Proto-Indo-European *h₁ey- ( “ to go ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔaː.ma.ˈdan/    ( Dari, formal ) IPA ( key ) : [ʔɑː.mä.d̪án]    ( Dari, formal ) IPA ( key ) : [ʔɑː.mä.d̪án]   ( Kabuli ) IPA ( key ) : [ʔɑː.mä.d̪án]    ( Hazaragi ) IPA ( key ) : [ʔɔː.mɔː.d̪án]    ( Iran, 
########## 914f3ecc7de978ef
URL: https://en.wiktionary.org/wiki/هنگام FETCHED: 2026
--- Etymology  [ edit ]    From Middle Persian [script needed] ( hngʾm /⁠hangām⁠/ , “ time, occasion ” ) ; by surface analysis , هن ( han , “ alternative form of همـ ( ham- , “ co- ” ) ” ) +‎ گام ( gām , “ step ” ) . [ 1 ] Akin to Old Armenian հանգամանք ( hangamankʻ , “ details, circumstances, way ” ) , an Iranian borrowing.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /han.ˈɡaːm/    ( Dari, formal ) IPA ( key ) : [häŋ.ɡɑːm]    ( Dari, formal ) IPA ( key ) : [häŋ.ɡɑːm]   ( Kabuli ) IPA ( key ) : [ʔäŋ.ɡɑːm]    ( Hazaragi ) IPA ( key ) : [ʔäŋ.ɡɔːm]    ( Iran, formal ) IPA ( key )
########## ec4339cba2f13d11
URL: https://en.wiktionary.org/wiki/انجام FETCHED: 2026
--- Etymology  [ edit ]    Borrowed from Classical Persian اَنجام ( anjām ) .   Noun  [ edit ]    انجام • ( anjām )  m    end , conclusion , outcome    tip , extremity    Persian  [ edit ]    Etymology  [ edit ]    From Middle Persian [Term?] ( /⁠hanǰām⁠/ , “ end, completion, outcome ” ) , from Old Persian [script needed] ( *hanǰāma- , “ end, conclusion ” ) , from Proto-Iranian *ham- + *gam ( “ to come ” ) , ultimately from Proto-Indo-European *gʷem- ( “ to go, stand ” ) . Compare Sanskrit संगम ( saṃgama ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.ˈd͡ʒaːm/    ( Dari, 
--- Etymology  [ edit ]    From Middle Persian [Term?] ( /⁠hanǰām⁠/ , “ end, completion, outcome ” ) , from Old Persian [script needed] ( *hanǰāma- , “ end, conclusion ” ) , from Proto-Iranian *ham- + *gam ( “ to come ” ) , ultimately from Proto-Indo-European *gʷem- ( “ to go, stand ” ) . Compare Sanskrit संगम ( saṃgama ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.ˈd͡ʒaːm/    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒɔːm]    ( Iran, formal ) IP
--- Etymology  [ edit ]    Borrowed from Classical Persian انجام ( anjām ) , from Middle Persian [script needed] ( hanǰām , “ end, completion, outcome ” ) .   Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /ən.d͡ʒɑːm/    Audio ( Pakistan ) : ( file )    Rhymes: -ɑːm    Noun  [ edit ]    اَن٘جام • ( añjām )  m ( Hindi spelling अंजाम )    end , finishing    result , conclusion   اس کا انجام ٹھیک نہیں ہو گا۔ is kā añjām ṭhīk nahī̃ ho gā The result of it won't be right.    Declension  [ edit ]    Declension of انجام    singular   plural   direct   اَن٘جام ( añjām )    اَن٘جام ( añjām )    
--- Etymology  [ edit ]    From Urdu انجام ( anjām ) .   Noun  [ edit ]    انجام ( anjām )    end , finishing    result , conclusion    Retrieved from " https://en.wiktionary.org/w/index.php?title=انجام&oldid=91032234 "   Categories : Pashto terms borrowed from Classical Persian   Pashto terms derived from Classical Persian   Pashto lemmas   Pashto nouns   Pashto masculine nouns   Persian terms inherited from Middle Persian   Persian terms derived from Middle Persian   Persian terms inherited from Old Persian   Persian terms derived from Old Persian   Persian terms derived from Proto-Iranian   Per
########## bfaa3a28a7334bd4
URL: https://en.wiktionary.org/wiki/انجمن FETCHED: 2026
--- Etymology  [ edit ]    Borrowed from Persian انجمن ( anjoman , “ meeting, assembly ” ) , from Middle Persian 𐭧𐭭𐭰𐭬𐭭 ( hanjaman , “ congregation, assembly, community ” ) , itself from Avestan 𐬵𐬀𐬧𐬘𐬀𐬨𐬀𐬥𐬀 ( haṇjamana , “ assembly ” ) .   Noun  [ edit ]    انجمن • ( encümen ) ( definite accusative انجمنی ( encümeni ) , plural انجمنلر ( encümenler ) )    society , association , club , circle , a group of people who meet to engage in a common interest   Synonyms: جمعیت ( cemʼiyet ) , محفل ( mahfil )    convocation , assembly , meeting , reunion , any gathering of persons for a specific purpose   Synon
--- Etymology  [ edit ]    From Middle Persian 𐭧𐭭𐭰𐭬𐭭 ( hanjaman , “ congregation, assembly, community ” ) , from Avestan 𐬵𐬀𐬧𐬘𐬀𐬨𐬀𐬥𐬀 ( haṇjamana , “ assembly ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.d͡ʒu.ˈman/    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒu.mán]    ( Iran, formal ) IPA ( key ) : [ʔæn.d͡ʒo.mǽn]    ( Tajik, formal ) IPA ( key ) : [ʔän.d͡ʒu.mán]    Rhymes: -an    Readings   Classical reading ?    anjuman   Dari reading ? 
--- Etymology  [ edit ]    Borrowed from Classical Persian انجمن ( anjuman , “ meeting, assembly ” ) . First attested in c. 1564 as Middle Hindi انجمن ( anjmn /⁠anjuman⁠/ ) . [ 1 ]    Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /ən.d͡ʒʊ.mən/    Rhymes: -ən    Hyphenation: اَنْ‧جُ‧مَنْ    Noun  [ edit ]    اَنْجُمَنْ • ( anjuman )  f ( Hindi spelling अंजुमन )    meeting , assembly , gathering   Synonym: مَحْفِل ( mahfil )   1981 , “ دل چیز کیا ہے آپ مری جان لیجئے ”, in Akhlaq Mohammed Khan (lyrics), Mohammed Zahur Khayyam (music), Umrao Jaan , performed by Asha Bhosle : اس انجمن میں
```


## [2026-09-06T02:30:32.967Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### PLA jah\"; grep -n \"jāh\\|gāh\\b\" incoming/PLA/PLA_pages.txt | head -10 | cut -c1-250; echo; echo \"### AFM jah\"; grep -n \"جاه\" AFM_pages.txt | head -8 | cut -c1-200; echo; echo \"### CHEUNG gam entry\"; sed -n '7307,7330p' CHEUNG.txt",
 "description": "jāh in Asbaghi/Addi Shir; Cheung gam"
}
```


### [2026-09-06T02:30:33.062Z] TOOL RESULT

```
### PLA jah

### AFM jah
1118:* (الجاهة ) الصخرة العظيمة المستديرة تعريب كله
1193:* ( الجهوّري» المرتفع العالي معرب عن جاهوار ومعناه ذو القدر وامازلة
1203:فالجاهنبار الاول هو اليوم امسن من بشهن ارد بوخت 0 بنرا علدهم
2958:بارس والغطر يس ) الظالم ܔ 273 أي جاهل وامق‎ ( +
3126:( القسج ) رسول السلطان القادم على رجاه [معو اع بيك ومنة 3 )!1
4473:جاهجور هه

### CHEUNG gam entry
*gam! *to come" 

*AVESTAN: gam- ‘to come’ || (+ *apa-) ‘to go away, leave’ || (+ *abi-) ‘to come at’ || 
(+ *aua-) ‘to go, come down to’ || (+ *a-) ‘to come’ || (+ *upa-) ‘to come to, attain’ || 
(+ *uz-) ‘to rise; to mature, become an adult (of children)’ || (+ *pati-) ‘to go/come 
to, approach; to return, go/come back’ || (+ *para-(ä-)) ‘to depart, leave’ || (+ *pari-) 
‘to go around, into, reach, approach’ || (+ *fra-) ‘to come to, reach’ || (+ *ni-) ‘to 
come off, down’ || (+ *ham-) ‘to come together, assemble, convene’ = Liste: 18f. 
Pres. inch.: IND. 35р. ҮАУ. jasaiti (Y 8.4, Yt 10.24, Yt 10.46, etc.), ajasaiti (Aog. 51), YAv. us.jasaiti (Yt 
10.50), ҮАУ. paiti.jasaiti (V 13.1, Yt 10.69), Y Av. para.jasaiti (Yt 10.101), YAv. frajasaiti (Vd 5.8 £.), 
Y Av. fra.jasaiti (N 46 ff., N 104), Y Av. nijasaiti (V 5.8 f.), Y Av. han.jasaiti (N 42), 1р1. med. OAv. райт 
Jjasamaidé (Y 36.1, Y 36.3 ff., Y 39.5), 3р1. act. YAv. uzjasonti (V 1.14), YAv. han.jasonti (V 2.12 ff., V 
2.16, V 19.27), med. YAv. YAv. han.jasante (N 62), INJ. 250. OAv. jaso (Y 43.6, Y 43.12), Y Av. apa.- 
Jasö (H 2.16), 3sg. OAV. jasat (Y 30.7, Y 51.15), ҮАУ. apa.jasat (V 2.23), OAv. upä.jasat (Y 30.6), OAv. 
pairi.jasat (Y 43.7, Y 43.9, Y 43.11, etc.), ҮАУ. apa.jasat (V 2.23), 3du. YAv. jasatom (Yt 19.82), med. 
OAv. jasaétam (Y 30.4), 3р1. YAv. jason (Yt 13.1, Yt 13.19, V 1.14), 3pl. med. YAv. "hanjasonta (Y 
2.8x, V 2.8), SUBJ. 1sg. YAv. jasani (Yt 12.4), YAv. nijasani (Yt 15.28), med. OAv. jasai (Y 28.2, Y 
51.22), OAv. pairijasäi (Y 50.8), 25р. YAv. auua.jasähi (V 19.18), med. Y Av. jasai (Vyt 22), 3sg. YAv. 
jasaiti (Yt 4.1, Yt 12.6, Yt 13.20), YAv. jasat (Yt 19.11, Yt 19.89, V 5.45, etc.), YAv. apa ... jasat (V 
7.39), Y Av. "a.jasat (N 19), ҮАУ. ajasat (Yt 14.2, Yt 14.7, Yt 14.9, etc.), YAv. uzjasat (V 15.15), YAv. 
frajasat (Vd 15.23), Y Av. nijasaiti (ViD 19), Y Av. nijasat (V 5.45), Y Av. vijasaiti (Yt 13.44, Yt 13.94), 
Y Av. vijasat (Yt 10.89), med. ? Y Av. han.jasäite (N 42.43C), 34и. Y Av. paiti.jasato (V 9.54 f., V 9.57, V 
13.53 ff.), 3р1. YAv. jasanti (Yt 8.29, Yt 8.61, Yt 13.70, Yt 14.53), ҮАУ. jasan (V.44 f), YAv. uz-jasan 
(V 15.21), YAv. frajasan (V 6.26, V 6.46, V 8.73), YAv. han.jasänti (N 65), med. YAv. hanjasante (Yt
```


## [2026-09-06T02:30:39.199Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7350,7450p' CHEUNG.txt | grep -n \"PIE\\|MIDDLE PERSIAN\\|NEW PERSIAN\\|OLD PERSIAN\\|Pok\\|LIV\\|āmad\" | head -20; echo \"---\"; sed -n '7415,7446p' CHEUNG.txt",
 "description": "Cheung gam summary"
}
```


### [2026-09-06T02:30:39.266Z] TOOL RESULT

```
8:*OLD PERSIAN: *gam- ‘to go’ (not attestested as simplex) || (+ *aua-) ‘to go down, 
16:*MIDDLE PERSIAN: MMP md, BMP mt- /mad-/ (pret. stem) ‘to come’, MMP z’m- ‘to 
---
Williams 1983: 50: "The importance of the derivation of Sogd. f3^m- from *fra- 
jama- is that it removes the principal witness to the O. Iran. base *sam- ‘to send’ 
postulated by Henning, Sogdica, 23-4. ... O. Iran. *Sam- ‘to send’ should therefore 
be discarded from the etymologist's vocabulary.". 

(+ *ati-) Well attested: Pres.: POT. intr. CSogd. tyt’ bntsq; Pret.: 2sg. BSogd. tyt’ys CSogd. tytys (Weber 
1970: 206), 3pl. MSogd. tyt’nd; Perf.: IND. 1sg. BSogd. tytk "ym (cf. GMS: $847), etc. || (+ *a-) Well 
attested: Pres.: POT. 25р. dur. SSogd. L’ *”’yt Byskwn ‘you cannot come’; Pret.: intr. IND. 1sg. SSogd. 
”ytym, 3sg. SSogd. "yt ‘came’, SSogd. L’? "yt ‘he didn't come’, etc. || (+ *para-(a-)-) Well attested: 
Pret.: intr. IND. 3sg. SSogd., BSogd. pr’’yt, CSogd., MSogd. pr’yt, etc. || (+ *fra-) Well attested: Caus.: 
pres. IMPV. 2sg. SSogd. ’B5’m, impf. IND. 15р. CSogd. f's"mw, 3sg. SSogd. B's^m, CSogd. f’s’m, etc. 
*CHORESMIAN: z’my- (caus.) ‘to bring, present’ || (+ *ati-) cyd- (supplet. forms of 
су-) || (+ *a-) m['z^my- (caus.) ‘to bring’ || (+ *fra-) fry’mk ‘adult’ || (+ *ni-) m/nys- 
‘to arrive’, m/ny’sy- (new caus.) ‘to bring, present’ = Samadi: 261, 55, 10, 124 f. 
*BACTRIAN: бороуо ‘time’ || (+ *à-) aya- (orig. caus.) ‘to bring’ || (+ *uz-) “vGyapo 
‘produce’ || (+ *pati-) nıdoyano-Bapyo ‘ambassador’ > S-W, Bact.: 176b f., 178a 
*NWIR: NP zaman ‘time’, Kurd. (Kurm.) сау (Ё) ‘time, moment’, NP gam ‘step, 
pace’, Kurd. (Kurm.) gav ‘step’ (< NP ?) || (+ *a-) Widely attested: NP атааап/ 
(suppet. äy-) ‘to come’, Kurd. hatin/ (supplet. &-) ‘to arrive’, Bal. atk/ (supplet. ay-), 
Zaz. amiyayis/ (supplet. yen-), Abyan. ammayan, Anar. yumy-/ (supplet. ei, ey-), 
Awrom. amáy/ (suppet. a-), Fariz. -ma-/ (supplet. -t-), Yar. -mi-, ma, -me-/ (supplet. 
-j-), Gz. ümé, ümä/ (supplet. ry-), Gil. (Rsht.) amon-/ (suppet. aj-), Ham. omiän/ 
(supplet. y-), Isfah. undán/ (supplet. y-), Bakht. avedan, avaidan, awaidan / (supplet. 
aly-), Meim. be-mej-/ (supplet. a-ij-), Nn. omiye-/ (supplet. y-, impv. yur-), Natan. 
b-am-/ (supplet. j-), Qohr. móda/tt-, Semn. bi-ám-/ (supplet. -i-), Shamerz. -ämi-/ 
ám-/ (supplet. (impv.) bid ‘come’), Sist. om(a)dä/ (supplet. a), Siv. amé(y)/ (supplet. 
ё(у)-), Soi -mäd-, -med-, -müd-/ (supplet. аё), Sorkh. -ám-/ (supplet. г-), Lasg. 
-am-/ (supplet. &j-) ‘to come’ || (+ *pati-) NP pay(g)am ‘message’, NP pay(g)ambar 
‘Apostle, Prophete (esp. Mohammad)’ || (+ *ham-) NP anjuman ‘company, 


*gam2 ? 101
```


## [2026-09-06T02:30:45.396Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7446,7500p' CHEUNG.txt | head -40; echo \"=== search PIE gwem in cheung ===\"; grep -n \"PIE \\*g\\\"em\\|PIE \\*g.em-\\|Pok.: 463\\|Pok: 463\" CHEUNG.txt | head",
 "description": "Cheung PIE note"
}
```


### [2026-09-06T02:30:45.475Z] TOOL RESULT

```
*gam2 ? 101 


assembly, club’. © The variant NP paygam is probably a borrowing from Parthian 
(or "North-Western" Ir.), cf. Nyberg 1974 II: 149b f. 

*NEIR: Wa. yat-/yat- ‘to reach, arrive’, Oss. I. opd D. ğædæ ‘kind, sort’, Rosh. 
yamönd, yamund, Orosh. yümön ‘spring festival at the beginning of field-work in 
spring’, Khf. yamundinc ‘10th month (in spring)’ || (+ *apa-) Oss. avgeed ‘childbirth 
and the post-natal period’ || (+ *ati-) Sh. (Baj.) (supplet. deó-)/ded, Rosh. (supplet. 
indiö-)/indayd, Bart. (supplet. indió-)/indiód, Sariq. (supplet. diö-)/deyd, (supplet. 
dis-)/dayd, Y ghn. (supplet. tis-, tes-)/táxta ‘to enter’, Yghn. diyäta / (supplet. divár-, 
dévár-/déwár- < *ati-bar'-) ‘to insert, introduce’ || (+ *à-) Sangl. oyoó, Ishk. dyad 
‘came’ (pret. supplet. of is-, *a-Hai-), (old caus.) Yzgh. aZam-/aZomt ‘to send’, (?) 
Wa. wbiz(bi)m-, woz(o)m-/wozomd- ‘to bring, carry, deliver’ || (+ *uz-) Pash. 
zyumai ‘waterwheel’ || (+ *fra-) Yghn. fSom-, fiSóm-/f()sSómta ‘to send’, Oss. 
ræğæd ‘ripe, mature’, Sh. (Baj.) faryemc, Rosh. faryemc ‘heifer’, Pash. waryumai ‘a 
male kid’, Yi. feryámo, M. fräyomiy ‘he-goat (1 yr)’, Yghn. faryümé ‘female calf, 
heifer’, (?) Wa. r(e)yum ‘heifer’, royd ‘young she-goat (of about 2 yrs)’ || (+ *niz-) 
Yghn. Ziyáta/ (supplet. Zivär-, Zévár-, Ziwár- < *niz-bar'-) ‘to bring, lead, drag, pull 
out’, (inch.) Sh. (Baj.) nayjis-/nayjid, Rosh. nawjis-/nawZod, Bart. nawZis-/nawZód, 
Sariq. narjis-/narjed ‘to pass through, by, return’ || (+ *ham-) Oss. I. egged, D. 
enged ‘sufficient, complete’ (with influence from simplex) 

*MISC: ? Par. zah-, Orm. záy-/zàk, jaw-/jök ‘to arrive’ = zey-/zäk || (+ *a-) Раг. aya 
“һе came’ (supplet. of Ze-) || (+ *pati-) Arm. (LW) patgam ‘message’ || (+ *fra-) Par. 
rhayam ‘spring’ 

*SANSKRIT: gam ‘to move, to go, to come’ (RV+) = EWAia I: 465 f. 

Ó In many Ir. languages, the root *gam! is part of a suppletive paradigm with *Hai. 
On the relationship between *gam' and *gaH! see also Klingenschmitt 1989: 81. 
«PIE *g”em- ‘to go; come’ = LIV: 209 f. | Pok.: 464 f. 

*IE COGNATES: Gr. Batvo ‘I go’, Arm. екп ‘came’, Lat. venire, Goth. giman, Engl. 


to come, etc. 

*REFERENCES: KPF I: 132b, 204a f., 242a f.; Ivanow 1926: 419; EVP: 89; IIFL I: 302a f., 414b, 232a, 
=== search PIE gwem in cheung ===
7054:«PIE *g"eH,- ‘to go, stride’ = LIV: 205 | Pok.: 463 f. 
7478:«PIE *g”em- ‘to go; come’ = LIV: 209 f. | Pok.: 464 f.
```


## [2026-09-06T02:30:55.910Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### AHD gwa\"; sed -n '530,545p' AHD_watkins1985.txt | cut -c1-400; echo; echo \"### HUB\"; grep -n \"gāh\\|gâh\\|zamān\\|hangām\\|anjuman\\|niyām\\|payġām\\|gām\" HUB.txt | head -15 | cut -c1-200",
 "description": "AHD gwa entry and Hübschmann"
}
```


### [2026-09-06T02:30:55.985Z] TOOL RESULT

```
### AHD gwa
*kunnan in Old English cunnan, to know, know how to, be able to (Old English first and third singular can from Germanic *kann from o-grade *gona-): CAN}, CON2, CUN- NING; b. Germanic causative verb *kannjan, to make known, in Old English cennan, to declare, and Old Norse kenna, to name (in a formal poetic metaphor): KEN, KENNING; c. Germanic *kunthaz in Old English cath, known, well-known, usual, 
gras-. To devour. 1. Germanic *krasjon-, fodder, in Old English cresse, czrse, cress: CRESS. 2. Suffixed form *gras-men in Latin gradmen, “fodder,” grass: GRAMA, GRAMINEOUS. 3. Suffixed form *gras-ter-, ‘the de- vourer,” dissimilated in Greek gastér, stomach, belly: (GASTRIC), GASTRO-, GASTRULA; EPIGASTRIUM. 4. Redu- plicated form “*gar-gr- dissimilated in Greek gangraina, gangrene: GAN
[grat-. Also krat-. To scratch. Germanic root. 1. Ger- manic *krattén in Middle Dutch cratsen, to scrape: SCRATCH. 2. Germanic *grat- in Old French grater, to scrape: GRATE}; REGRATE. [Pok. gred- 405.]]
[gravo-. Also grafo-. A designation of rank, later corre- sponding with the feudal title of count. West Germanic noun. Middle Dutch grave, count: MARGRAVE, PALS- GRAVE.]
greut-. To compress, push. 1. Germanic *kridan in Old English criidan, to press, hasten: CROWD!, 2. Germanic *krudam in Old English crod, a squeezing (> Middle English crud, crudde): CRUD, CURD. [Pok. greut- 406.]
gre-no-. Grain. 1. Germanic *kornam in: a. Old English corn, grain: CORN}; b. Old English derivative noun cyr- nel, seed, pip: KERNEL; c. Old High German korn, grain: EINKORN. 2. Latin grdnum, grain: GARNER, GRAIN, GRAM2, GRANADILLA, GRANARY, GRANGE, GRANITE, GRANULE, GRENADE; FILIGREE. [In Pok. ger- 390.]
gru-. To grunt. Imitative. 1. Germanic *grun- in Old English grunnian, to grunt, probably akin to Old English grunettan, to grunt: GRUNT. 2. Germanic intensive form *grunnatjan in Old High German grunniz6n, to grunt: GRUDGE. 3. Latin grunnire, grundire, to grunt: GRUNION. [Pok. gru- 406.]
gva-. Also grem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumo6n-, he who comes, a guest, in compound *wil-ku- mon-, a desirable guest (*wil-, desirable; see wel-2), in Old English wilcuma, a welcome guest, and wilcume, the greeting of welcome: WELCOME; C. compound *bi-kuman, to arrive, come to be (*bi-, intensive prefix; see ambhi), in Old English bec
24
g”elbh-
(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or
g”ele-'
shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM
25
g"hi-
sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré

### HUB
7684:ap. ham- = np. aw- in anjuman Tersammlung = zd. han-
8199:sanj *anhangen') ; anjuman 'Versammlung - zd. hanjamana- ;
9109:anbcLstan, anbCLr , anjuman , . andarn, angCLrden u. s. w.
```


## [2026-09-06T02:31:03.644Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### WLD\"; grep -n \"gehen, kommen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5 | cut -c1-300; echo; grep -n \"gātu\\|gätu\\|gäman\\|gāman\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5 | cut -c1-300",
 "description": "Walde-Pokorny lookups"
}
```


### [2026-09-06T02:31:03.719Z] TOOL RESULT

```
### WLD
41900:g“a- , gehen, kommen“ s. u. g^em-.
```


## [2026-09-06T02:31:05.952Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### SYN come/time\"; grep -n \"gᵘ̯em\\|g^uem\\|gwem\\|g\\*em\" SYN.txt | head -8 | cut -c1-300; echo \"### IEC\"; grep -n \"gātu\\|gāmā\\|gāman\" IEC.txt | head -8 | cut -c1-250",
 "description": "Buck and Mann"
}
```


### [2026-09-06T02:31:06.025Z] TOOL RESULT

```
### SYN come/time
17514:2. IE *g*em-, *g'd-. 1.675 ff. Ernout-M. 10883 ff.
### IEC
5292:gumtes (come, gone; coming, going’. Cf. gumtis. Variant gumtus Skt. gatáh; Av. gata; Gk. batós; Lat. in-ven- tus; Go. -kunds, cpds.; Li. gimtas ‘born’; Latv. dzimts ‘inborn, native’; dzimta ‘birth’. Variant in *-us: Skt. gatüh;
```


## [2026-09-06T02:31:10.287Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"g\\^em-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8 | cut -c1-300; echo \"=== context ===\"; grep -n -A4 \"^g\\^em-\\|g\\^em- ,gehen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20 | cut -c1-400; echo \"### SYN 17510\"; sed -n '17505,17520p' SYN.txt | cut -c1-400",
 "description": "WLD gem entry and Buck"
}
```


### [2026-09-06T02:31:10.378Z] TOOL RESULT

```
41900:g“a- , gehen, kommen“ s. u. g^em-. 
=== context ===
### SYN 17510
aVIc Words for ‘com ? e’ (except
Digitized by Arya Samaj Foundation Chennai and eGangotri
OCOMOTION, TRANSPORTATION, NAVIGATION 693 10.47 GO Goth. gaggan, -leipan, -stei- Lith. ili tpt, gee gan ; Lett.  zel, pret. gaju Ci TT ate wd- ON — ganga, fara, lida ChSl. iti, choditi Me He (Oe are) Dan. gaa (fare) SCr. iti, hoditi [a dere, ea) ead Sw. 4 (fara) Boh. ili, choditi __andare he lab OE gangan, gan, faran, Pol. —_i8¢, chodzié ie aller, vat, *7 wadan Russ. idli, chodit’ op. tr, 
Lett. nakt) are compounds of IE *ez- with prefixes meaning ‘to’ or the like (cf. Grk. eic-exue ‘go to, come’).
Grk. épxouat, aor. 7APov, though listed only under ‘come’, in accordance with what eventually became their prevailing use, are also frequently ‘go’, especially in Homer, and regularly in amépxopar ‘go away’.
On the Celtic words for ‘go’ and ‘come’, cf. esp. Vendryes, RC 46.217 ff.
1. I *ei-, extended *ya-. Walde-P. 1.102 ff. Ernout-M. 303 ff. Walde-H. 1.406 ff.
*ei-. Grk. due (but mostly fut. in sense); Lat. ire (> Sp. ir, Fr. fut. iraz, It. inf. ire, imperat. tte, etc.); Lith. eztz, Lett. iet, ChSl. it, SCr. 767, Boh. jiti, Pol. is¢, Russ. idti, Skt. 2- (38g. ett), Av. i- (88g. aeiti, OPers. aitiy); Hitt. im- perat. 2sg. it, 2pl. ten (Sturtevant, Hitt. Gram. 95).
*yG-. Skt., Av. ya- : Lith. joti, Lett. jat, ChSl. jachati ‘ride’, etc.; uncertain Goth. iddja, OE éode ‘went’, which, moreover, do not coincide (Feist 288 f.) ; Toch. A yd- ‘go’ (SSS 423, 458); Hitt. ya- ‘go, march’ (Sturtevant, Hitt. Gloss. 184).
2. IE *g*em-, *g'd-. 1.675 ff. Ernout-M. 10883 ff.
*gxem-. Girk. Baivw “go, walk’; Lat.
Walde-P.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
694 SELECTED INDO-EUROPEAN SYNONYMS
venire ‘come’ (> the Romance words) ; Goth. giman, OE cuman, etc., general Gme. for ‘come’; Skt., Av., OPers. gam- ‘go, come’ (Skt. gacchati, Av. fasaiti, sko- presents like Grk. Bacxw; Av. Jam- without prefix mostly ‘come’; also Av., OPers. a-jam- ‘come’, whence NPers. amadan ‘come’); Toch. kém-, kum-, etc. ‘come’ (SSS 428 f.).
*gra-. Grk. aor. &8nv, Dor. é8av; Skt. aor. agam, pres. jigali; Av. aor. gat; Lett. gaju ‘went’ (pret. to zet).
```


## [2026-09-06T02:31:19.778Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"gátu\\|gätu-s\\|Liegerstatt\\|Sessel, Thron\" WLD_Bd1_1930_dli_70244_djvu.txt | head -8 | cut -c1-350; echo \"=== gaman ===\"; grep -n \"Schritt\" WLD_Bd1_1930_dli_70244_djvu.txt | sed -n '1,12p' | cut -c1-300",
 "description": "WLD gātu / gāman"
}
```


### [2026-09-06T02:31:19.863Z] TOOL RESULT

```
35252:oder Liegerstatt : nd. (und entlehnt hd.) Lot, hole ..Schuppen, Stall, Hiitte' , 
42675:„Ort, Platz; Liegerstatt, Sessel, Thron“, ap. ga&u (# aus t vor v, Bartho- 
=== gaman ===
22913:groBe Schritte machen"; wozu auch russ. sigz „Fischname“, wie Salm zu 
30722:krdkati „schreiten“ usw., slav. *korako- in skr. koruk „Schritt“, horde di 
30723:„schreiten" usw., slav. *kroko- in ksl. o-krociti „cingere“, skr. krdk „Schritt u , 
32119:distinguere“, mit ham- „colligere, (Schrittlangen aneinander legen"; np. 
37000:ghengh- „schreiten; Schritt, Sehenkelspreize, Schamgegend“. 
37002:Ai. jamhas- n. ., Schritt, Flfigelschlag“, jmgha „Unterschenkel“, av. zanga- 
37008:lit. z eng iii , zeiigti „schreiten“, pmzunga „tJbertretung“, zingsnis ,, Schritt"'; 
37026:air. ceimm , cymr. corn, cam, bret. camm „Schritt“; B. bei Fick II 4 77 ver- 
41076:lat. grudior, -7 „sehreiten“, grail us, -us „Schritt, Stufe“, grallae „Stelzen“ 
41081:got. grips (nur Acc. sg. grid) „Schritt, Stufe“ (wo fur allerdings Siebs KZ. 
41083:mhd. grit „Schritt“, griten „die Beine auseinanderspreizen“, nhd. bail-. 
41084:gritt ,,Schritt‘‘, gritten „die Beine spreizen“, grittel „die Gabel, die die
```


## [2026-09-06T02:31:22.546Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '42665,42700p' WLD_Bd1_1930_dli_70244_djvu.txt | cut -c1-300",
 "description": "WLD gātu context"
}
```


### [2026-09-06T02:31:22.608Z] TOOL RESULT

```
gjem-, g«a- 


677 


aged s. Delbrfick Grdr. IY 77; *g!!«~ eigentlich „den Full aufsetzen 11 ); 
ai. galram „Glied, Korper“; ai. gata-h „Gang, Weg, Raum, Ort“, av. gatu-s 
„Ort, Platz; Liegerstatt, Sessel, Thron“, ap. ga&u (# aus t vor v, Bartho- 
lomae Grd. d. iran. Phil. I 8); gr. pgraq/xog „Taktschritt“, Pgidgycov „Tanzer“ 
(aua oder *fidru „das Fu8aufsetzen“ + dgju-og, -ovia ,,im Schreiten 

EbenmaB, Takt haltend“, oder dissimiliert aus *p a ro(o)-a on a j v ..die FtiBe, 
Glieder harmonisch bewegend" mit einem *pdr gov „FuB, Glied“ = ai. gatram , 
Brugmann BSGW. 1899, 199 Anm. 1 ), djugnopgrem, jon. a/xquoflmeco (ebenso, 
oder mit a aol. dor.) „streite“ (auf Grund von *pdrog oder *pa.za. „das 
Schi’eiten“, also „nach zwei Seiten auseinandergehend“; jon. a durch An- 
lehnung ans Ptc. pdzog), vgl. u. lett. gat is (fiber das imYokal widerstrebende 
herakl. Povpijtig unsicherer Bed. s. Boisacq 127 Anm. 2); ai. v i-gaman- n. 
„Schritt“ ( prthii-pragaman - „weitschreitend“; vgl. ai. gamin- ,.gehend“, 
Weiterbildung eines o-St. *ga-ma ), av. gaman- n. „Schritt“, gr. (tijuerai Inf., 
fifjfxa n. j^ritt 1 * {mno^uf.ioov Aeseh. ^ie ein Pferd einherschreitend‘‘), ab- 
lautend gr. pcoyog „Tritt, Stufe, Gestell, Altar“ (nicht besser als *g'tom-os 
zur Wzf *g 1 iem-, Prellwitz 2 71 zw.); ai. gnya-m „Schritt“ in uru-gayd- 
„weitschrittig, sich weithin verbreitend, weit (Weg) 1 '", av. gaya- (acc. gaim) 
„Sehritt“, aevd-gdya- ,,ein Schritt“ (mil Formans -ya-\ erweisen ebenso- 
wenig eine ursprfingliche Wzf. *gai- wie aor. aglsta , dgliata) ; gr. Pgldg 
„Tfirschwelle“, pepg/.og, dor. pepdXog „betretbar, ungeweiht 1- (Gegensatz 
von apazog „unverganglich, heilig' 1 ); tiefstufig pepaiog „sicher“ (*„gut 
gangbar“); fiddyv Adv. „im Schritt“, fiadog „Weg“, p adi£co „gehe einher“, 
pa&juog „Stufe, Schwelle, Schritt*% ftddoov „Grundlage“, eypaxyg (aucb 
e/ufiag-, -pad og, Fraenkel KZ. 42, 256) „Mannerschuh“; alb. nga ..ich laufe" 
(G. Meyer Alb. Wb. 305, Gdf. *ga-nio ); lett. gdju (Praet. zu iet) „ich ging“ 
(setzt ein Praes. *gu[d voraus, dessen j trotz Wiedemann Lit. Praet. 142
```


## [2026-09-06T02:31:37.460Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 202 -l 202 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg202 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 202"
}
```


### [2026-09-06T02:31:40.063Z] TOOL RESULT

```
total 27424
drwx------ 2 sfmqrb sfmqrb   12288 Sep  5 22:31 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   68598 Sep  5 22:30 build186.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   59730 Sep  5 22:31 mk193.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   98287 Sep  5 22:31 pg202.png
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


## [2026-09-06T02:31:43.003Z] TOOL CALL #79: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg202.png"
}
```


### [2026-09-06T02:31:43.588Z] TOOL RESULT

```

```


## [2026-09-06T02:31:43.586Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:32:01.763Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"\" SBK.txt; grep -n \"جمانه\\|ثمان\\|زمان.*معرب\\|معرب.*زمان\" SBK.txt | head -10 | cut -c1-250",
 "description": "Bahar Sabk-shenasi zamān"
}
```


### [2026-09-06T02:32:01.829Z] TOOL RESULT

```
22036
6136:هیرپتایشنی » ودین‌فرشکرتی ۰ پتوندپتایشنی‌وروان گروثمانی دارند.» 
7685:ومالك الاشتر.... و کتاب شوریء مقتل‌عثمان‌رمقتل حسین(ع)و کتاب‌معویه‌د يزيد 
8513:خود ایچه نین «خواچه» دده است . ملاحظه شود در«اخواند کار» : لقب سلاطین آلعثمان» 
9461:ز : گروتمان-گروثمان گرزمان (ملکوت ) 
12653:و تر کستان و هند و عثمانی‌دایر ورایج بوده و مراسلات درباری و واقعه نگاریوتواریخ 
18779:ایوعثمان‌الدمشقی ۱۵۶
```


## [2026-09-06T02:32:03.512Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### FFD farjam/anjam\"; grep -n \"فرجام\\|انجام\\|جام\" incoming/FFD/FFD_pages.txt | head -10 | cut -c1-200; echo \"### SPG\"; ls | grep -i spg",
 "description": "FFD and SPG availability"
}
```


### [2026-09-06T02:32:03.583Z] TOOL RESULT

```
### FFD farjam/anjam
127:آنجافت انجام
131:فرجافت فرجام
391:فعل واداری فعلی است که دلالت می‌کند بر این که کسی را وادار به انجام‌دادن کاری
406:فعل آغازی فعلی است که بر شروع انجام‌دادن یا گرفتن کاری دلالت می‌کند.
424:فعل آرزویی فعلی است که برداشتن آرزوی انجام‌دادن یاگرفتن کاری دلالت می‌کند.
453:در ایرانی باستان برای گزارش عملی متعدی» که در گذشته انجام داده شنده» راه
674:در اصل بر انجام گرفتن کار به سوی متکلم دلالت می‌کرده است. 734 صورت اصلی 739
858:انجامیدن
860:«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
861:«انجام» در فارسی میانه 1272[311 بوده است.
### SPG
SPG_keilinschriften1881.txt
```


## [2026-09-06T02:32:13.119Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; grep -n -A6 \"^فرجامیدن\\|فرجامیدن\" FFD_pages.txt | head -30 | cut -c1-300; echo \"=== anjamidan ctx ===\"; sed -n '855,870p' FFD_pages.txt",
 "description": "FFD farjāmidan entry"
}
```


### [2026-09-06T02:32:13.189Z] TOOL RESULT

```
870:«به‌هم آوردن») است. «آمدن» و «فرجامیدن) هم از 8/1370 آمده‌اند > «آمدن؛ و
871:«فرجامیدن».
872-
873-انداختن
874-انداخت + فارسی میانه 8228371: طرح کردن» برنامه‌ریزی کردن. سعدی در بوستان
875-[pdf page 37]
876-انا ی فعلهای فارسی دری
877-می‌گوید:
--
1775:فرجامیدن
1776-«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
1777-فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
1778-صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
1779-آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
1780-به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
1781-«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
=== anjamidan ctx ===

انبار + فارسی میانه 127003 < ایرانی باستان 1۵:۳-037-2*. برای 2 -> آرای.

انجامیدن

«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
«انجام» در فارسی میانه 1272[311 بوده است.

بازماندةٌ 31-12[-82۳* ایرانی باستان است. برای 1۵ -> آراست. 1470 پیشوند
فعلی است. 31[ به جای 370[ آمده است. در فارسی میانةٌ مانوی 18۳831۲ و 82۳2211
به‌جای 1۵0[311 آمده است.

انجام ج فارسی میانه 822[370 + ایرانی باستان 370-8[-822*. برای 2 -> آرای. 1
پیشوند فعلی است. 8/[370 صورت بالاندهٌ ریشهٌ 8/1270 به معنی «حرکت کردن» است.
صورت بالاندةُ ريشهٌ 8/[87 معنی واداری دارد و با پیشوند فعلی 1۵70 به معنی
«به‌هم آوردن») است. «آمدن» و «فرجامیدن) هم از 8/1370 آمده‌اند > «آمدن؛ و
```


## [2026-09-06T02:32:24.983Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \"https://en.wiktionary.org/wiki/مزمن\" \"https://en.wiktionary.org/wiki/Ecbatana\" \"https://en.wiktionary.org/wiki/گام\" \"https://en.wiktionary.org/wiki/فرجام\"; do python3 tools/fetch_source.py \"$u\" --note \"page 202, root Gwa/Gwem: Arabic z-m-n derivatives, Ecbatana, gām, farjām\" 2>&1 | tail -1; done",
 "description": "Archive four more pages"
}
```


### [2026-09-06T02:32:30.004Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3b300eb615a1bc09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d947687fca46a06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bbdb2037f34cbfd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/50dedec463b5f514.txt
```


## [2026-09-06T02:32:34.165Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 3b300eb615a1bc09 3d947687fca46a06 1bbdb2037f34cbfd 50dedec463b5f514; do echo \"##### $f\"; python3 - \"$f.txt\" <<'PYEOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nprint(t[:55].replace('\\n',' '))\nidx=[m.start() for m in re.finditer(r'Etymology',t)]\nc=0\nfor i in idx:\n    seg=t[i:i+500].replace('\\n',' ')\n    if 'edit' in seg[:30]:\n        print('---',seg); c+=1\n    if c>=3: break\nPYEOF\ndone",
 "description": "Read the four pages"
}
```


### [2026-09-06T02:32:35.952Z] TOOL RESULT

```
##### 3b300eb615a1bc09
URL: https://en.wiktionary.org/wiki/مزمن FETCHED: 2026-
--- Etymology  [ edit ]    Of the root ز م ن ( z m n ) from زَمَان ( zamān , “ time ” ) .   Pronunciation  [ edit ]    IPA ( key ) : /muz.min/    ( Kuwait ) IPA ( key ) : /mʊzmɪn/    Adjective  [ edit ]    مُزْمِن • ( muzmin ) ( feminine مُزْمِنَة ( muzmina ) )    chronic    Descendants  [ edit ]    → Ottoman Turkish: مزمن ( müzmin )   Turkish: müzmin    → Persian: مزمن    Persian  [ edit ]    Etymology  [ edit ]    Borrowed from Arabic مُزْمِن ( muzmin ) .   Adjective  [ edit ]    مزمن • ( mozmen )
--- Etymology  [ edit ]    Borrowed from Arabic مُزْمِن ( muzmin ) .   Adjective  [ edit ]    مزمن • ( mozmen )    chronic    Retrieved from " https://en.wiktionary.org/w/index.php?title=مزمن&oldid=88967014 "   Categories : Arabic terms belonging to the root ز م ن   Arabic 2-syllable words   Arabic terms with IPA pronunciation   Gulf Arabic terms with IPA pronunciation   Arabic lemmas   Arabic adjectives   Persian terms borrowed from Arabic   Persian terms derived from Arabic   Persian lemmas   Pers
##### 3d947687fca46a06
URL: https://en.wiktionary.org/wiki/Ecbatana FETCHED: 2
--- Etymology  [ edit ]    From Latin Ecbatana , from Ancient Greek Ἐκβάτανα ( Ekbátana ) , from Old Iranian ; see Old Persian 𐏃𐎥𐎶𐎫𐎠𐎴 ( Hangmatāna ) for more. Doublet of Hamadan .   Pronunciation  [ edit ]    IPA ( key ) : /ɛkˈbætənə/    Proper noun  [ edit ]    Ecbatana    ( historical ) The ancient capital of Media , in modern-day Iran , and subsequently a royal residence of Persian and Parthian kings.   Related terms  [ edit ]    Hamadan    Translations  [ edit ]    capital of Media   Akkadian: 𒆳
--- Etymology  [ edit ]    From Ancient Greek Ἐκβάτανα ( Ekbátana ) , itself from Old Persian 𐏃𐎥𐎶𐎫𐎠𐎴 ( Ha(n)gmatāna ) .   Pronunciation  [ edit ]    ( Classical Latin ) IPA ( key ) : [ɛɡˈba.ta.na]    ( modern Italianate Ecclesiastical ) IPA ( key ) : [ekˈbaː.ta.na]    Proper noun  [ edit ]    Ecbatana   n   pl ( genitive Ecbatanōrum ) ; second declension    Ecbatana (the ancient capital of Media , in modern-day Iran )   Declension  [ edit ]    Second-declension noun (neuter), with locative, plural o
--- Etymology  [ edit ]    Borrowed from Latin Ecbatana , from Ancient Greek Ἐκβάτανα ( Ekbátana ) , from Old Persian 𐏃𐎥𐎶𐎫𐎠𐎴 ( Ha(n)gmatāna ) .   Pronunciation  [ edit ]    IPA ( key ) : /eɡbaˈtana/ [eɣ̞.β̞aˈt̪a.na]    Rhymes: -ana    Syllabification: Ec‧ba‧ta‧na    Proper noun  [ edit ]    Ecbatana   f    ( historical ) Ecbatana (the ancient capital of Media , in modern-day Iran )   Retrieved from " https://en.wiktionary.org/w/index.php?title=Ecbatana&oldid=89290292 "   Categories : English terms b
##### 1bbdb2037f34cbfd
URL: https://en.wiktionary.org/wiki/گام FETCHED: 2026-0
--- Etymology  [ edit ]    Inherited from Proto-Iranian *gáHma , from Proto-Indo-Iranian *gáHma , from Proto-Indo-European *gʷéh₂-mn̥ ~ *gʷh₂-mén-s , from *gʷeh₂- ( “ to step ” ) . Cognate with Persian گام , Avestan 𐬔𐬁𐬨𐬀𐬥 ( gāman ) , Northern Kurdish gav , Ancient Greek βῆμα ( bêma ) , Sanskrit प्रगामन् ( pragāman ) .   Noun  [ edit ]    گام • ( gám )    step    See also  [ edit ]    قدم ( qadam )    Iraqi Arabic  [ edit ]    Root    گ و م    1 term    Etymology  [ edit ]    Etymology tree   Proto-S
--- Etymology  [ edit ]    Etymology tree   Proto-Semitic   Arabic قَامَ ( qāma )   Iraqi Arabic گام    Inherited from Arabic قَامَ ( qāma ) .   Pronunciation  [ edit ]    IPA ( key ) : /ɡaːm/    Verb  [ edit ]    گام ( gām ) I ( non-past يگوم ( ygūm ) )    to stand    to start doing something   Conjugation  [ edit ]    Conjugation of گام    singular   plural   1 st person   2 nd person   3 rd person   1 st person   2 nd person   3 rd person   past   m    گمت ( gimit )    گمت ( gimit )    گام ( gām 
--- Etymology  [ edit ]    Inherited from Sanskrit ग्राम ( grāma , “ village ” ) , ultimately from Proto-Indo-European *h₂ger- ( “ to gather ” ) .   Pronunciation  [ edit ]    IPA ( key ) : /ɡaːm/    Noun  [ edit ]    گام • ( gām )  m ( plural گام , Devanagari गाम )    village   سُہ گَو گام روزنہِ ― su gav gām rōzni ― He went to the village to live    Derived terms  [ edit ]    گامُک ( gāmuk , “ villager ” )    Persian  [ edit ]    Persian Wikipedia has an article on: گام    Wikipedia fa    Pronunci
##### 50dedec463b5f514
URL: https://en.wiktionary.org/wiki/فرجام FETCHED: 2026
--- Etymology  [ edit ]    From Middle Persian [script needed] ( plcʾm /⁠frazām⁠/ ) , from Proto-Iranian *fra- ( from Proto-Indo-Iranian *pra- , from Proto-Indo-European *pro- ) + Proto-Iranian *ǰám- ( from Proto-Indo-European *gʷem- ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /far.ˈd͡ʒaːm/    ( Dari, formal ) IPA ( key ) : [fäɾ.d͡ʒɑːm]    ( Dari, formal ) IPA ( key ) : [fäɾ.d͡ʒɑːm]   ( Kabuli ) IPA ( key ) : [fäɾ.d͡ʒɑːm]    ( Hazaragi ) IPA ( key ) : [fäɾ.d͡ʒɔːm]    ( Iran,
```


## [2026-09-06T02:32:56.623Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"θaman\\|hamān-\\|Vamana\\|ßaman\" BRT.txt | head -5 | cut -c1-200; echo \"--- BRT jamana ---\"; grep -n \"jamana\\|jäman\\|jamāna\" BRT.txt | head -6 | cut -c1-250; echo \"--- KNT thaman ---\"; grep -n \"amana-\\|θamāna\\|Oamana\" KNT.txt | head -5 | cut -c1-200",
 "description": "Search for thamān"
}
```


### [2026-09-06T02:32:56.717Z] TOOL RESULT

```
--- BRT jamana ---
17874:reden, besprechen':  vlspalfO  ^frasnailü vTspaäa  hanjamanalsä  yaU  apinsaltim (3D.,  Augm.)  mazda sca  xardhustrasca "bei  allen  Besprechungen,  bei  allen  Zu- sammenkünften, bei  denen  sich  bespra- chen . ,"  Y.  72.  5.  a)  mit  
20235:—  kai  afava  'da  vanat  drvant»m  Yt./,  aS; — pata  nS  ibifyantaipairi  °</jj(als  Vok.)/a armaitiica  SrB.j;  —  hanjamanaisü  yai/ apmsalhm  'd3s^  sara'küitraslä  Y.  12.  5 ;
23944:•  j.  vi-£ar3na-  n.  Trennungsstelle,  Stelle, wo  sich  der  Weg  teilt":  pa%amcS  *'rjnä'> .  .  pahqmia  hanjamana  Y,  4-3.  i ;  — fakqm  '.  .  paiti  'na  Yt  //.  4,  Vyt.  54.
24412:—  °/i7?j(i/n(GPm.)Ä  ra%wqm  'panqm- (GPf.>o  'ratufriünqm  Vr.g.y;  —  'pa- nqm  (GPm.)  arinäm  . .  'panqm'  (GPf.) häirisinqm'  Y.  65.  2;  1.  12»,  2.  11,  g.  18, 2Ö'.2,  7-9^  27.1,  62.8,  77,8,  Ytj.2a,  50, Ä'.39,  70.
29334:hanjamana-  1770
--- KNT thaman ---
```


## [2026-09-06T02:33:18.347Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/جاه/\" --note \"page 202 node 9: Mo'in's entry for جاه (origin tag)\" 2>&1 | tail -1; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/زمان/\" --note \"page 202 node 13: Mo'in's entry for زمان\" 2>&1 | tail -1",
 "description": "Fetch Mo'in entries via abadis"
}
```


### [2026-09-06T02:33:24.235Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/722c70423ed8f5dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0958b5544989892.txt
```


## [2026-09-06T02:33:28.108Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 722c70423ed8f5dc b0958b5544989892; do echo \"##### $f\"; grep -o \"فرهنگ معین.\\{0,400\\}\" $f.txt | head -2; echo; grep -o \"\\[ع\\.\\].\\{0,120\\}\\|\\[په\\..\\{0,120\\}\" $f.txt | head -4; done",
 "description": "Extract Mo'in entries"
}
```


### [2026-09-06T02:33:30.010Z] TOOL RESULT

```
##### 722c70423ed8f5dc
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

##### b0958b5544989892
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-06T02:33:36.022Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"زمان\" MON_part2.txt 2>/dev/null | head -3 | cut -c1-200; echo \"---\"; grep -n \"(ع\\.)\\s*زمان\\|جاه\" MON_part1.txt 2>/dev/null | head -5 | cut -c1-200",
 "description": "Mo'in local OCR"
}
```


### [2026-09-06T02:33:36.133Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
541:غایتی: تا به حدی. تا این غایت: تا این زمان» 
687:غد: 4:[ع.] (. ق.) فردا. (توسعاً) زمان 
3551:غیت امام زمان (مهدی(ع)) پس از پایان 
---
1278:جاه و جلال. سیار سفید و درخشان. فصیح و 
1383:خوی» عرق. آبرو؛ اعتار» جاه. آب‌رخ 
1416:رخ. اعستبار» قدرء» جاه» شرف عرض» 
1420:اب روی. اعتبار» قدر» جاه» شرف عرض.» 
2636:ار تزین: 0 (.) (فز.) جاه جهنده»
```


## [2026-09-06T02:33:41.127Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^جاه\\|جاه: \\|جاه(\" MON_part1.txt | head -5 | cut -c1-250; echo \"===\"; grep -n \"زمان: \\|زمان(\\[ع\" MON_part2.txt MON_part1.txt | head -5 | cut -c1-250",
 "description": "Mo'in headwords"
}
```


### [2026-09-06T02:33:41.231Z] TOOL RESULT

```
1278:جاه و جلال. سیار سفید و درخشان. فصیح و 
7665:جاهل تر» ناآ گاه تر. 
18534:جاهلیت عرب بود؛ هواشناسی از روی 
38156:جاه و حلال» خدم و حشم» سامان رک 
47042:جاه: 126 [- جاه معر.] (.) مقام» منزلت؛ 
===
MON_part2.txt:16372:بود که آبا بود... قد زمان: پبو سته» همیشه» 
MON_part2.txt:31356:گرزمان: -8۵۲02 ,22۲2۳018 (.) عرش خداء 
MON_part2.txt:89421:روزه: ببوسته» همواره. هر زمان: هر وقت. 
MON_part2.txt:90103:همسزمان: [- هرزمان] (ق.) هر 
MON_part2.txt:91019:یکسان. (ق.) باز» نیز. همان زمان: (ق.) همان
```


## [2026-09-06T02:33:45.719Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '47036,47050p' MON_part1.txt",
 "description": "Mo'in jāh entry context"
}
```


### [2026-09-06T02:33:45.793Z] TOOL RESULT

```
رنگک. نغام. 

جاوید؛ 0 (ص. ق.) اسدی» دایمی» 
جاویدان: :127-74 [- جویدن] (سص‌م.) 
(جاوید» جاود» خواهد جاوید» بجاو 
جاونده» جاویده) جویدن» مضغ کردن. 
جاه: 126 [- جاه معر.] (.) مقام» منزلت؛ 
درجه» رته. جلال» فر و شکوه. 

جاهد: ۵ (ع.] (افا.) جهد کننده؛ 
کو شنده» ساعی. 

جاهل: 6 (ع.] (افا. ص.) نادان؛ ج. 
جهال؛ جهلاء جهله. (عم.) لات؛ لوطی. 
جاهلیت: 12۳0-10۰ (ع. جساهلية]
```


## [2026-09-06T02:33:53.313Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^زمان\\|زمان:\" MON_part2.txt MON_part1.txt | head -8 | cut -c1-250; echo \"=== azmena ===\"; grep -n \"ازمنه\" MON_part1.txt MON_part2.txt | head -4 | cut -c1-200",
 "description": "Mo'in zamān entry"
}
```


### [2026-09-06T02:33:53.406Z] TOOL RESULT

```
MON_part2.txt:6173:زمانی نیست. شاخه‌های آن دراز و باریک با 
MON_part2.txt:6830:زمان) بعد» بس. از فرود: از بعد» از پس. (.) 
MON_part2.txt:7824:زمان ( گذشته حال يا آینده) کند؛ ج. افعال. 
MON_part2.txt:9292:زمان؛ در اندر» درون. 
MON_part2.txt:11740:زمانی (دستور ۰:۳ فرع. سج.) (تص.) 
MON_part2.txt:16372:بود که آبا بود... قد زمان: پبو سته» همیشه» 
MON_part2.txt:16781:زمان انجام می‌گردد؛ بدین جهت تشکیلات 
MON_part2.txt:21139:زمان قدیم به آن یک قسم مهره بازی 
=== azmena ===
MON_part1.txt:18832:هنگام‌ها؛ روزکارها ساعات» ازمنه. اوقات 
MON_part1.txt:19328:آوازها. (سد.) نقراتی چند است در ازمنه 
MON_part1.txt:36650:به ترتیب ازمنه تنظیم شده باشد. ضح.- 
MON_part1.txt:36662:ازمنه‌ای که هنوز شواهد و آثار آن موجود
```


## [2026-09-06T02:34:17.371Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; grep -o \"Arabic.\\{0,600\\}\" 04e15978808644e0.txt | head -3; echo \"=== count langs ===\"; head -c 1500 04e15978808644e0.txt | tail -c 900",
 "description": "Check Arabic section of جاه page"
}
```


### [2026-09-06T02:34:19.135Z] TOOL RESULT

```
Arabic جَاه ( jāh ) , from Middle Persian [Book Pahlavi needed] ( gʾs ) , 𐫃𐫀𐫍 ( gʾh /⁠gāh⁠/ , “ place, throne, bed; time ” ) . Doublet of گاه ( gâh ) , see there for more. 
Arabic 
Arabic 
=== count langs ===
sian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Derived terms 

 Toggle the table of contents 

 جاه 

 7 languages 

 فارسی 
 Magyar 
 Kurdî 
 Malagasy 
 پښتو 
 Русский 
 Türkçe 

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

 Borrowed from Arabic جَاه ( jāh ) , from Middle Persian [Book Pahlavi needed] ( gʾs ) , 𐫃𐫀𐫍 ( gʾh /⁠gāh⁠/ , “ place, throne, bed; time ” )
```


## [2026-09-06T02:34:48.051Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nd=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\nimport re\n# find leaf containing '217'\nfor i,p in enumerate(pages):\n    if re.search(r'\\bgam\\b',p) and ('Gehen' in p or 'gehen' in p or 'kommen' in p):\n        print('leaf',i,p[:400].replace('\\n',' '))\n        break\nPYEOF",
 "description": "Spiegel check"
}
```


### [2026-09-06T02:34:49.894Z] TOOL RESULT

```
leaves 224
leaf 188 GliOSSAB. 217 Gaumäta (^ff^^ff "^T^T Hf ^T'T) n. pr. Gaumäta, Name eines Magiers, nom. Bh. I, 36. 44. 46. 64. 70. IV, 7. b, 1. acc. Gaumätam Bh. I, 49. 54. 57. 73. IV, 81. Gatisha (^f T*^ ^7? <<) P ^ r. acc. dual, oder plur. gaushä. Bh. II, 74. 89, Aw. gaosa, neup. ^yl' dass. Gand'utava (^ff" i^} i^ ^fff "^TE) npr. Gandutava, Name einer Gegend im westlichen Arachosien. Bh. III, 65. Vergi. die krit
```


## [2026-09-06T02:34:52.681Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'PYEOF'\nd=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[188][:2500])\nPYEOF",
 "description": "Spiegel p.217 glossary"
}
```


### [2026-09-06T02:34:54.380Z] TOOL RESULT

```
GliOSSAB. 217
Gaumäta (^ff^^ff "^T^T Hf ^T'T) n. pr. Gaumäta, Name eines
Magiers, nom. Bh. I, 36. 44. 46. 64. 70. IV, 7. b, 1. acc. Gaumätam
Bh. I, 49. 54. 57. 73. IV, 81.
Gatisha (^f T*^ ^7? <<) P ^ r. acc. dual, oder plur. gaushä. Bh. II,
74. 89, Aw. gaosa, neup. ^yl' dass.
Gand'utava (^ff" i^} i^ ^fff "^TE) npr. Gandutava, Name
einer Gegend im westlichen Arachosien. Bh. III, 65. Vergi. die krit.
Note zu d. St.
Gandära (^ff*" TT fTf H^)^- P^- Name einer Gegend am Indus,
den Griechen unter dem Namen ravc^agtrii;, FavSaQixt] bekannt Bh. I, 16.
I, 18. NRa, 24. Cf. über dieses Land besonders: Lassen die altpersi-
schen Keilschriften p. 110 not. Indische Alterthumskunde I, 422.
gam (^ff^ "^Tff) gehen, zuweilen zu gma, jam umgestaltet. Huzv.
pno pärsi madan == altp. gmatanaiy.
+ ä: kommen, herkommen Aorist fünfte Bildung (cf. Gramm.
§ 67) 3. ps. sg. äjam'iyd H, 19. neup. ,j4X«l-
+ ham zusammenkommen Participialperf. plur. hangmaiä Bh.
II, 32. 38. 43. 52. 58. III, 64.
+ parä fortgehen, reichen 3. ps. sg. imperf.pä'r^^»?flrf^NRa,44.
garb {i^X^ ^) t:.)) ergreifen Imperf. 1. ps. sg. agarMyam
Bh. II, 4. IV, 7. 32. V, 26. 28. Szb) 8. NRa) 17. 3. ps. sg. agarUya
Bh. III, 73. 87. V, 12. 3. ps. plur. agarUya Bh. D, 13. 88. III, 48. 49.
Medium imperf. 3. ps. sg. agarMyatä Bh. I, 42. 43. 81. III, 81. mit
passiver Bedeutung Bh. II, 73. Aw. gerew, geurvayemi dass. neup. ^j^y-
Garmapada {i^lT ^T "^TfT ^ ^) n. pr. Name eines Monates bei
den alten Persern, gen. Garmapadahya Bh. I, 42. III, 7. 46. Der erste
Theil des Wortes ist wol = aw. garemo, Wärme, cf. neup. ^S^ pada
aber = aw. padha neup. ^., Fussspur, Spur.
Gasta {iyir^ t^ ^TfT) widerwärtig, fem. nom.^^.gasiä NRa,ö7.
Ueber die Gründe, welche uns nöthigen, diese Bedeutung anzunehmen,
cf. oben die Bem. zu d. St.
Gäthu (^TT"^ fff y^y ^7?) 1) Ort, Platz instr. gäthvä an seinem
Orte, an seinem Platze, cf. Gr. § 75. Bh. I, 62. 66. 69. NRa, 36. 2) Thron
acc. gäthutn NRa, 41. Aw. gätu, neup. »LjJ beide Wörter mit denselben
Bedeutungen.
/^^(K^""<Tf IT) verbergen.
+ apa dasselbe, conj. praes. 2. ps. apagaudayähy Bh. IV, 55. 57.
imperf. 2. ps. apagaudaya (mit abgeworfenem Augment vor ma cf.
Gr. § 65). Bh. IV, 54. Aw. güz, skr. guh verbergen.
```


## [2026-09-06T02:35:01.640Z] TOOL CALL #95: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-06T02:35:01.699Z] TOOL RESULT

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
```


## [2026-09-06T02:35:04.366Z] TOOL CALL #96: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T02:35:04.409Z] TOOL RESULT

```
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


## [2026-09-06T02:35:09.431Z] TOOL CALL #97: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg202.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/202.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T02:35:09.519Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T02:44:09.358Z] TOOL CALL #98: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build202.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 202,\n \"book_page\": 172,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Gwa, Gwâ, Gwen 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465\",\n   \"note\": \"Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.\",\n   \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/gʷem-\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:463\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')\", \"stance\": \"supports\",\n     \"note\": \"'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.').\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line ~539)\", \"stance\": \"supports\",\n     \"note\": \"'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)\", \"stance\": \"supports\",\n     \"note\": \"'*gam¹ \\\"to come\\\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §10.47/10.48 (SYN.txt line 17514 f.)\", \"stance\": \"supports\",\n     \"note\": \"'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \\\"go, come\\\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \\\"come\\\"; also Av., OPers. ā-jam- \\\"come\\\", whence NPers. amadan \\\"come\\\")'.\"},\n    {\"src\": \"KLN\", \"where\": \"p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)\", \"stance\": \"supports\",\n     \"note\": \"'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"gam : to come, step; jam, jantu : to go\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Indo-Iranian inherits PIE *gʷem- as the root gam- (Skt. gam-, Av. gam-, OP gam-). In Avestan the root appears in two guises that Nourai lists side by side: (a) gam- proper, in the perfect and in nominal derivatives (gāman-, gata-), and (b) jam-, the regular Avestan outcome of the full-grade *gʷem- (PIE labiovelar *gʷ- > Indo-Iranian *ǰ before front vowel of the thematic/subjunctive stems: *gʷem-e-ti > Av. jamaiti 'goes'), beside the inchoative present jasaiti < *gʷm̥-sk̑e-ti. jantu- is the tu-stem *gʷem-tu- 'a going, coming' (= Skt. gántu-, Lat. adventus), which Pokorny prints on the same page. Old Persian has the root only in compounds (ā-gam-, ham-gam-, parā-gam-), and there too the reflexes with j- (ājamiyā 'may he come') alternate with the g- of the participles (paragmatā, hangmatā). Nourai's glosses 'to come, step' / 'to go' are correct.\",\n     \"derivation_fa\": \"ریشهٔ هندواروپایی *gʷem- در هندوایرانی به‌صورت gam- بازمانده است (سنسکریت gam-، اوستایی gam-، پارسی باستان gam-). در اوستایی دو گونه در کنار هم دیده می‌شود که نورایی هر دو را آورده است: نخست gam- که در ستاک‌های اسمی و کامل می‌ماند (gāman-، gata-)، و دوم jam- که پیامد آوایی قانونمند *gʷ- در ایرانی است (واک‌گونهٔ لبی‌کامی هندواروپایی پیش از واکهٔ پیشین به ǰ بدل می‌شود: *gʷem-e-ti > اوستایی jamaiti «می‌رود»)؛ ستاک حال آغازی نیز jasaiti < *gʷm̥-sk̑e-ti است. jantu- همان ستاک tu-دار *gʷem-tu- «رفت، آمد» است (هم‌ریشه با gántu- سنسکریت و adventus لاتین) که پوکورنی در همان صفحهٔ ۴۶۵ آورده. در پارسی باستان این ریشه تنها با پیشوند به‌کار رفته (ā-gam-، ham-gam-، parā-gam-). ادعای نورایی در این گره درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/gʷem-\", W + \"آمدن\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:463\", \"status\": \"supports\",\n       \"note\": \"POK_02.txt p.464-465 (the continuation of the entry that begins on 463): 'thematisch: hochstufig ai. gámati, av. jamaiti „geht“', 'sk̑o-Präsens *gʷm̥-sk̑ō: ai. gácchati, av. jasaiti „er geht“', and 'nach Schwyzer … könnte das n auch von Formen wie av. jantu (*gʷem-tu-) … bezogen sein'. All three of Nourai's forms are there.\"},\n      {\"ref\": \"KLN:318\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 8320, s.v. 'come' (page number 318 printed at the foot of the block): 'fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati, “he goes”, gatáh, “gone”, Avestic jamaiti, “goes”'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Lexicon p.183 s.v. gam- (KNT.txt, the 'gaθu- … gam- vb.' block)\", \"stance\": \"supports\",\n       \"note\": \"'gam- vb. “come”: Av. gam-, Skt. gam-, Gk. βαίνω, Lt. veniō, Gt. qiman, pIE gʷem- (§101, §244)', followed by the attested OP compounds 'ā + gam- “come”: ājamiyā opt.', 'ava- + gam-', 'parā + gam-: paragmatā', 'ham- + gam- “come together, assemble”: haⁿgmatā npm. past pte.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹ 'to come' (CHEUNG.txt line 7307 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: gam- “to come” || (+ *apa-) … (+ *ā-) “to come” … (+ *pati-) “to go/come to, approach” … (+ *fra-) … (+ *ni-) “to come off, down” … (+ *ham-) “to come together, assemble, convene”'; the paradigm section gives 'Pres. inch. IND. 3sg. YAv. jasaiti', 'ind. YAv. jamaiti'. '*OLD PERSIAN: *gam- “to go” (not attested as simplex)'.\"},\n      {\"src\": \"SPG\", \"where\": \"Die altpersischen Keilinschriften, Glossar p.217 (SPG_keilinschriften1881.txt leaf 188)\", \"stance\": \"supports\",\n       \"note\": \"'gam … gehen, zuweilen zu gma, jam umgestaltet. Huzv. mtn, pārsi madan == altp. gmatanaiy. + ā: kommen, herkommen … ājamiyā … neup. āmadan. + ham zusammenkommen Participialperf. plur. hangmatā.' Spiegel's page is exactly Nourai's SPG:217.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.vv. gam-, jasaiti (BRT.txt)\", \"stance\": \"supports\",\n       \"note\": \"Bartholomae's dictionary carries the root under both shapes; the derivatives Nourai draws from it (gāman-, hanjamana-, frajasaiti, nijasaiti, paiti.jasaiti) are all listed as separate articles — e.g. 'j. gāman- n. „Schritt“' (line 10341) and 'hanjamana- 1770' (line 29334).\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Avestan\",\n     \"words\": \"gâman : step; a-gam : to come; ni-gama : come down (in sheath); paiti-gama : come forth (with a message)\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Three of the four items are exact. (1) Av. gāman- n. 'step' is a man-stem to the *gʷā-/gā- half of the root (= Skt. vi-gāman-, Gk. bêma); Bartholomae glosses it 'Schritt' and cites its use as a unit of measure. (2) Av. ā-gam- 'to come' (pres. ā-jasaiti, aor. subj. ā-jamat̰) is the ancestor of NP āmadan. (3) Av. paiti-gam- 'to come back, come to' gives the verbal noun *paiti-gāma- 'that which comes back, an answer/message', whence Parthian patgām, MP paygām, NP payām/payğām. (4) The weak link is 'ni-gama : come down (in sheath)': Av. ni-gam- (Cheung: '(+ *ni-) to come off, down'; Pokorny s.v. ni- 'Old Indic ní-gam-, Avestan ni-gam- “enter into a condition”') is a genuine compound, but the parenthesis '(in sheath)' is not a meaning of it — it is imported backwards from Persian nīyām 'sheath', which modern scholarship derives from *ni-dā- (see node 3). So the node's forms are real; one of its glosses is an etymological back-formation.\",\n     \"derivation_fa\": \"سه واژه از چهار واژهٔ این گره درست است. gāman- اوستایی «گام» ستاکی است با پسوند -man- از نیمهٔ *gā- همین ریشه (هم‌ریشه با vi-gāman- سنسکریت و bêma یونانی) و بارتولمه آن را «Schritt» و یکای اندازه‌گیری معنی کرده است. ā-gam- «آمدن» (حال ā-jasaiti) نیای «آمدن» فارسی است و paiti-gam- «بازآمدن، به‌سوی کسی آمدن» اسم‌مصدرِ *paiti-gāma- «پیام» را می‌سازد که به پارتی patgām و فارسی میانه paygām می‌رسد. تنها گره‌گاه، ni-gama است: این فعل مرکب اوستایی («فرودآمدن، درآمدن») به‌راستی وجود دارد — چونگ و پوکورنی هر دو آن را آورده‌اند — اما معنای «فرودآمدن در نیام» که نورایی در کمانک افزوده، معنای این فعل نیست بلکه از واژهٔ فارسی «نیام» به عقب بازخوانده شده است (نگاه کنید به گرهٔ ۳). پس صورت‌ها درست‌اند و تنها یکی از معناها ساختگی است.\",\n     \"sources\": [W + \"پیغام\", W + \"آمدن\", W + \"نیام\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:463\", \"status\": \"supports\",\n       \"note\": \"Pokorny's entry (pp.463-465) has 'av. gā-man- n. „Schritt“' on p.463 and, for the compounds, 'av. frā-ymat̰ (gthav. -gʷmat̰) „er kam hinzu“, apers. ā-gmatā'. For ni-gam- see POK_full line 26674: 'also in verbal prefix Aryan ni- \\\"in, into\\\", e.g. Old Indic ní-gam-, Avestan ni-gam- \\\"enter into a condition\\\"' — i.e. the compound exists, but with no sheath in sight.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"s.v. gāman- (BRT.txt line 10341, col. 522 in Mo'in's citation)\", \"stance\": \"supports\",\n       \"note\": \"'j. gāman- n. „Schritt“: paoirīm °ma frabarat̰ … „primum gradum profert“ H.2.15 … a) als Masseinheit: yaθa vā °ma dvaēta …'. Mo'in (Borhān 1765 n.5) cites this very column as 'بارتولمه ۵۲۲'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 677\", \"stance\": \"supports\",\n       \"note\": \"'ai. vi-gāman- n. „Schritt“ (pr̥thú-pra-gāman- „weitschreitend“ …), av. gāman- n. „Schritt“, gr. bēmenai Inf., bêma n. „Schritt“'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, preverb list (CHEUNG.txt line 7307 ff.)\", \"stance\": \"partial\",\n       \"note\": \"Lists Av. gam- with '(+ *ā-) “to come”', '(+ *pati-) “to go/come to, approach; to return”' and '(+ *ni-) “to come off, down”' — confirming all four compounds as verbs, but giving ni-gam- no nominal 'sheath' sense; Cheung's New-Persian harvest of *gam¹ includes pay(g)ām but not nīyām.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"gâm «گام» : step; âmadan «آمدن ( آینده )» : to come; nîyâm «نیام» : sheath; payâm «پیام ( پیامبر ، پیغام ، پیغمبر )» : message\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Three of the four words are textbook cases of this root; the fourth is not. gām: Proto-Iranian *gāma- (Av. gāman- 'step', PIE *gʷeh₂-mn̥) > MP gām > NP گام; Kurdish gav is the same word. āmadan: Av./OP ā-gam- > MP āmadan (past stem āmad, Spiegel's equation 'Huzvāreš mtn, pārsi madan == altp. gmatanaiy'), with the suppletive present stem āy- < PIE *h₁ey- 'to go' — which is why Nourai's parenthesis آینده belongs to a different root, though he does not say so. payām: *pati-gāma- > Parthian patgām / Sogdian patγām > MP paygām > NP پیغام, and by loss of the intervocalic spirant پیام; پیغمبر/پیامبر is payğām + -bar 'bearer'. nīyām 'sheath', however, is not from *ni-gam-: Wiktionary (with Wakhi naẟün and Sanskrit nidhāna- as cognates) takes MP niyām from Old Persian *nidāmān- 'covering, envelope', to *ni-dā- 'to lay down' (PIE *dʰeh₁-), the same word that Biblical Hebrew borrowed as נָדָן (1 Chr 21:27) and Aramaic as nidnā. The -d- of Wakhi naẟün cannot come from *-g-. Nourai's own source concedes the point: Mo'in (Borhān p.2223 n.7) offers 'Old Persian *ni-gāma-, cf. Skt. ni- + …-gāma “capacity”; cf. payām' but adds 'وجه اشتقاق قطعی نیست' (“the etymology is not certain”). Because one word of the node is rejected by modern scholarship, the node takes the worst verdict.\",\n     \"derivation_fa\": \"سه واژه از چهار واژهٔ این گره از نمونه‌های کلاسیک این ریشه‌اند و یکی نه. «گام» از ایرانی آغازین *gāma- (اوستایی gāman- «گام»، هندواروپایی *gʷeh₂-mn̥) از راه فارسی میانهٔ gām به فارسی نو رسیده و «گاڤ» کردی نیز همان است. «آمدن» از ā-gam- اوستایی/پارسی باستان است؛ اشپیگل در واژه‌نامهٔ خود (ص ۲۱۷) برابری «هزوارش mtn = پارسی madan = پارسی باستان gmatanaiy» را آورده است. ستاک حال «آی-» از ریشهٔ دیگری (*h₁ey- «رفتن») است و بنابراین «آینده» که نورایی در کمانک آورده، از این ریشه نیست. «پیام» بازماندهٔ *pati-gāma- است: پارتی patgām، سغدی patγām، فارسی میانه paygām، فارسی نو «پیغام» و با افتادن غ «پیام»؛ «پیغمبر/پیامبر» نیز مرکب از پیغام + بَر است. اما «نیام» از *ni-gam- نیست: ویکی‌واژه آن را از پارسی باستان *nidāmān- «پوشش، غلاف» از *ni-dā- «نهادن» می‌گیرد و واکهٔ ذال در واخی naẟün و سنسکریت nidhāna- گواه آن است؛ همین واژه به عبری کتاب مقدس nāḏān و به آرامی nidnā وام رفته است. خود معین در حاشیهٔ برهان (ص ۲۲۲۳) پس از آوردن *ni-gāma می‌نویسد «وجه اشتقاق قطعی نیست». پس در این گره سه واژه پذیرفتنی است و «نیام» را پژوهش امروزی رد می‌کند.\",\n     \"sources\": [W + \"گام\", W + \"آمدن\", W + \"پیغام\", W + \"نیام\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:11\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no.48 on printed p.11 (HRN.txt leaf 32): '48. āmeden „kommen“, Praes. āy-em (s. No. 60). ap. ā + √gam-, ājamiyā „er käme“; aw. ā + √gam-, āgemat̰; phlv. āmtan, āmatan (PPGl.)'. Exactly Nourai's arrow for آمدن (and Horn's cross-reference to no.60 is the separate āy- present).\"},\n      {\"ref\": \"BQT:1765\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāṭeʿ printed p.1765 (= scan pdf 562, running head ۱۷۶۵), s.v. گام, Mo'in's footnote 5: 'اوستا -gāman «بارتولمه ۵۲۲»؛ پهلوی gām «نیبرگ ص ۷۷»؛ کردی gāv (قدم، لحظه، زمان)' — Av. gāman- > Phl. gām > NP گام, as drawn.\"},\n      {\"ref\": \"BQT:2223\", \"status\": \"partial\",\n       \"note\": \"Borhān printed p.2223 (= v4 pdf 306), s.v. نیام, Mo'in's footnote 7: 'پارسی باستان *ni-gāma؛ قس: سانسکریت ni (پیشوند) + …-gāma (گنجایش). قس: پیام. وجه اشتقاق قطعی نیست «اشتقاق ۱۰۹۳»'. Mo'in does propose *ni-gāma — Nourai's source — but explicitly marks the etymology as uncertain.\"},\n      {\"ref\": \"BQT:434\", \"status\": \"partial\",\n       \"note\": \"Borhān v1 leaf 660 (printed ~434) has the headword 'پیام — بروزن سلام، بمعنی خبر و پیغام باشد'; Mo'in's own note stands with پیغام on the next opening (leaf 671, footnote to printed p.444): 'پیغام … هم‌ریشه و هم‌معنی پیام «اشتقاق ص ۸۰»؛ پیغامبر و مخفف آن پیغمبر مرکب از پیغام + بر (مخفف برنده)'. The Persian side of Nourai's arrow is confirmed; the Old Iranian antecedent is given only by cross-reference.\"},\n      {\"ref\": \"SPG:217\", \"status\": \"supports\",\n       \"note\": \"Spiegel, Die altpersischen Keilinschriften, Glossar p.217 (SPG_keilinschriften1881.txt leaf 188), s.v. gam: '+ ā: kommen, herkommen … 3. ps. sg. ājamiyā … neup. آمدن' and, three articles later, 'Gāthu 1) Ort, Platz … 2) Thron … Aw. gātu, neup. گاه'. Nourai's page reference is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict., s.vv. āmadan, paygām, gām\", \"stance\": \"supports\",\n       \"note\": \"PHD.txt gives 'come āmadan, madan', 'message paygām', 'rise abar āmadan … ul āmadan' in the English-Pahlavi index and the Pahlavi spelling 'paygām' (line 4718); the Middle Persian links MP āmadan / paygām > NP آمدن / پیغام are MacKenzie's own.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, *NWIR section (CHEUNG.txt line ~7430)\", \"stance\": \"partial\",\n       \"note\": \"'*NWIR: NP zamān “time”, Kurd. (Kurm.) gav “step”, NP gām “step, pace” … || (+ *ā-) NP āmadan / (supplet. āy-) “to come” … || (+ *pati-) NP pay(g)ām “message”, NP pay(g)ambar'. Cheung confirms gām, āmadan and payām for this root and does NOT list nīyām.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab/abadis copy of Farhang-e Fārsi (fetched, JS-only)\", \"stance\": \"silent\",\n       \"note\": \"abadis.ir/fatofa/زمان and /جاه returned only the site chrome (client-rendered), so Mo'in's own entries could not be read online; the local MON OCR does not carry a clean headword block for these words.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Avestan\",\n     \"words\": \"fra-jâma : gone forward (to a destination); han-jâma : conclusion; han-jâmana : coming together\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Two preverbs on the same root. *fra-jāma- 'a going forth (to the end)' is the verbal noun of Av./OIr. fra-gam- / fra-jam- 'to come forth, reach' (Av. frajasaiti, Old Av. frā-gʷmat̰); *ham-jāma- 'a coming together, completion' and its -ana- derivative *ham-jamana- 'assembly' belong to Av. ham-gam-/han-jas- 'to come together, convene'. Avestan actually attests the noun haṇjamana- 'assembly, meeting' (Bartholomae col. 1770; Y. 12.5 hanjamanaēšu 'at the gatherings'); *fra-jāma- and *han-jāma- are reconstructed from the Middle Persian frazām/frajām and hanjām. Nourai labels the box 'Avestan', which is right for hanjamana- and defensible for the other two only as Old Iranian reconstructions — Mo'in and Abolqāsemi both write them as Old Persian *fra-jāma- / *ham-jāma-.\",\n     \"derivation_fa\": \"این گره دو پیشوند را بر یک ریشه می‌نشاند. *fra-jāma- «به‌پیش‌رفتن، به سرانجام رسیدن» اسم‌مصدرِ fra-gam-/fra-jam- ایرانی است (اوستایی frajasaiti، گاهانی frā-gʷmat̰)، و *ham-jāma- «به‌هم‌آمدن، پایان» با مشتق -ana-دار آن *ham-jamana- «انجمن» از ham-gam-/han-jas- «گرد آمدن» است. از این سه، تنها haṇjamana- «انجمن، گردهمایی» در اوستا گواه دارد (بارتولمه ستون ۱۷۷۰، یسنه ۱۲.۵)؛ دو صورت دیگر از روی فارسی میانهٔ frazām/frajām و hanjām بازسازی شده‌اند. برچسب «اوستایی» برای hanjamana- درست است، اما معین و ابوالقاسمی دو صورت دیگر را «ایرانی باستان/پارسی باستان» می‌نویسند. در کل ادعای نورایی درست است.\",\n     \"sources\": [W + \"انجمن\", W + \"فرجام\", W + \"انجام\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1451\", \"status\": \"supports\",\n       \"note\": \"The Borhān page Nourai means is printed p.1449 in the scan (v3 pdf 244; the volume's running numbers drift by ~2 pages around here), s.v. فرجام, Mo'in's footnote 2: 'پهلوی frazhām «مناسی ۲۷۴» و frajāmīnītan، frajām از پارسی باستان *frajāma (از gam «رفتن») «اشتقاق ۸۱۸»'. That is precisely the arrow fra-jāma > farjām, root gam-.\"},\n      {\"ref\": \"BQT:166\", \"status\": \"not_found\",\n       \"note\": \"Borhān v1: the انجمن headword sits on leaf 385 of BQT_v1_pages.txt ('انجمن — بفتح اول و فتح میم و سکون نون. مجلس و مجمع را گویند'), i.e. printed p.164-166 as cited, but the footnote band of that leaf was lost in the djvu OCR, so Mo'in's etymological note itself could not be read. Vol. 1 is not in the ref_page.py scan list, so the page image could not be rendered either.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. col. 1770 s.v. haṇjamana- (BRT.txt lines 17874, 20235, 29334)\", \"stance\": \"supports\",\n       \"note\": \"'vīspāišū frašnāišū vīspāišū hanjamanaēšū yaθa apərəsatəm … „bei allen Besprechungen, bei allen Zusammenkünften“ Y.12.5'; the index line 'hanjamana- 1770' gives the column. The Avestan noun is real and means 'assembly'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. hanjaman, hanjām, frazām\", \"stance\": \"supports\",\n       \"note\": \"PHD.txt: 'assembly hanjaman', 'congregation hanjaman', 'completion bowandagīh, frazāmišn, hanjām', 'frazāmēnīdan, frazāmēn- = frazāftan'. The Middle Persian continuations of both compounds are in MacKenzie.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt lines 7684, 8199)\", \"stance\": \"supports\",\n       \"note\": \"'ap. ham- = np. aw- in anjuman „Versammlung“ = zd. han-' and 'anjuman „Versammlung“ = zd. hanjamana-'. Hübschmann equates NP انجمن directly with the Avestan word.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"farjâm «فرجام ( فرجامیدن )» : end; anjâm «انجام ( انجامیدن )» : conclusion; anjoman «انجمن» : society, meeting\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are the regular New Persian continuations of the node above. فرجام < MP frazām (Book Pahlavi plcʾm) / frajām < OIr. *fra-jāma-, the -z- of the Book-Pahlavi spelling being the south-western treatment of Old Iranian *j before ā, the -j- of frajām the north-western (Parthian) one; the denominative فرجامیدن is built on the noun. انجام < MP hanjām < OIr. *ham-jāma-, with the regular Persian loss of initial h- and the reduction ham- > an- before a consonant (the same an- as in انباز, اندام). انجمن < MP hanjaman < Av. haṇjamana- 'assembly', with the same h-loss and with unstressed -a- > -o-/-u- in the second syllable (anjuman/anjoman). Abolqāsemi's Feʿl-hā-ye Fārsi-ye Dari, one of Nourai's two cited sources here, gives the chain verbatim.\",\n     \"derivation_fa\": \"هر سه واژه دنبالهٔ قانونمند گرهٔ بالایند. «فرجام» از فارسی میانهٔ frazām (به خط پهلوی کتابی plcʾm) یا frajām از ایرانی باستان *fra-jāma- است؛ «ز» صورت جنوب‌غربی و «ج» صورت شمال‌غربی (پارتی) همان واج ایرانی باستان است، و «فرجامیدن» مصدر جعلی از همین اسم است. «انجام» از فارسی میانهٔ hanjām از *ham-jāma- است، با افتادن «ه» آغازین و کوتاه‌شدن ham- به an- پیش از همخوان (همان an- که در «انباز» و «اندام» می‌بینیم). «انجمن» از فارسی میانهٔ hanjaman از haṇjamana- اوستایی «گردهمایی» است، با همان افتادن «ه» و بدل‌شدن واکهٔ بی‌تکیهٔ هجای دوم به o/u. ابوالقاسمی در «فعل‌های فارسی دری» — یکی از دو مأخذ خود نورایی — همین زنجیره را آورده است؛ پس ادعای نورایی درست است.\",\n     \"sources\": [W + \"فرجام\", W + \"انجام\", W + \"انجمن\"],\n     \"ref_check\": [\n      {\"ref\": \"FFD\", \"status\": \"supports\",\n       \"note\": \"Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari (FFD_pages.txt): stem list 'آنجافت – انجام / فرجافت – فرجام' (lines 127, 131); s.v. انجامیدن (line 858 ff.): 'مادهٔ ماضی «انجام» در فارسی میانه hanjām بوده است … بازماندهٔ *ham-jāma- ایرانی باستان است … انجام < فارسی میانه hanjām < ایرانی باستان *ham-jāma- … صورت بالندهٔ ریشهٔ gam به معنی «حرکت کردن» است … «آمدن» و «فرجامیدن» هم از gam آمده‌اند'; s.v. فرجامیدن (line 1775 ff.): 'فرجام < فارسی میانه frazām < ایرانی باستان *fra-jāma-'.\"},\n      {\"ref\": \"ETM\", \"status\": \"not_checked\",\n       \"note\": \"ETM = Abolqāsemi, Rišešenāsi (Etimoloži), Qoqnus 1374. refs_online.json records it as catalogue-only: 'RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only.' Its sister volume FFD (checked above) says the same thing.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. hanjaman, hanjām, frazām, frazāmēnīdan\", \"stance\": \"supports\",\n       \"note\": \"'assembly hanjaman', 'completion … frazāmišn, hanjām', 'frazām-pērēzīh “final victory”', 'frazāmēnīdan, frazāmēn- = frazāftan'. The Middle Persian forms required by the arrow all exist.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt line 8199)\", \"stance\": \"supports\",\n       \"note\": \"'anjuman „Versammlung“ = zd. hanjamana-' — Hübschmann's own equation, i.e. the New Persian word is the Avestan one.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, *NWIR section\", \"stance\": \"supports\",\n       \"note\": \"'(+ *ham-) NP anjuman “company, assembly, club”' is listed among the New Persian reflexes of *gam¹.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"gât, gâthu, gâv, gâtuš : place, seat, throne; gâtu-bar : (baby) carriage\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The core of the node is right: Av. gātu- (stem gātav-/gātu-) 'place, seat, throne' and OP gāθu- (nom. gāθuš, instr. gāθavā, acc. gāθum) are the tu-stem of the *gʷā- half of the root, literally 'the going, the standing-place' (= Skt. gātú- 'way, place'). Nourai's 'gât' is the bare stem, 'gâthu' the Old Persian gāθu-, 'gâtuš' the Old Persian nominative. But 'gâv' is not a form of this word: the printed page really does read 'gâv' (verified on the page image), so this is Nourai's own misprint — almost certainly for the Avestan strong stem gātav- (Bartholomae writes gātav-/gāθu-), the -tav- having lost its -t-. It cannot be Av. gav- 'cow', which is a different word. gātu-bar 'litter, carriage' is the compound gātu- + bar- 'to bear' (PIE *bʰer-, Nourai's cross-reference 'Bher 1'), the ancestor of NP گهواره/گاهواره 'cradle', for which Mo'in reconstructs 'گاه + واره (from bar- “to bear”), Pahlavi gāhvārak'.\",\n     \"derivation_fa\": \"هستهٔ این گره درست است: gātu- اوستایی (ستاک gātav-/gātu-) «جا، نشستنگاه، تخت» و gāθu- پارسی باستان (نهادی gāθuš، ابزاری gāθavā) ستاکِ tu-دارِ نیمهٔ *gā- همین ریشه‌اند، به معنای تحت‌اللفظی «جای رفتن/ایستادن» (هم‌ریشه با gātú- سنسکریت «راه، جا»). «gât» همان ستاک برهنه، «gâthu» صورت پارسی باستان و «gâtuš» صورت نهادی آن است. اما «gâv» صورتی از این واژه نیست؛ تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «gâv» چاپ کرده است، پس این خطای چاپی نورایی است و به احتمال بسیار صورت درست gātav- (ستاک قوی اوستایی نزد بارتولمه) بوده که «ت» آن افتاده است؛ با gav- اوستایی «گاو» ربطی ندارد. gātu-bar نیز مرکب gātu- + bar- «بردن» (هندواروپایی *bʰer-) است و همان است که معین در حاشیهٔ برهان برای «گهواره/گاهواره» می‌آورد: «از گاه + واره از مصدر bar [بردن]، پهلوی gāhvārak».\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"gât, gâthu, gâv, gâtuš\",\n     \"correct_form\": \"gātu-, gātav- (Av.) / gāθu-, gāθuš (OP)\",\n     \"sources\": [W + \"گاه\"],\n     \"ref_check\": [\n      {\"ref\": \"KNT:183\", \"status\": \"supports\",\n       \"note\": \"Kent, Old Persian, Lexicon p.183: 'gāθu- sb. “place, throne, place of battle” (JNES 4.49-50): Av. gātav- gāθu-, NPers. gāh, Skt. gātu-, to pAr. root gam-, pIE *gʷem- “come” (§68, §81, §158.II, §179.n2). gāθum asm. DNa 41f. gāθavā 1sm. … XPf 33'. Note that Kent writes the Avestan strong stem 'gātav-' — the form Nourai's 'gâv' has mangled.\"},\n      {\"ref\": \"POK:463\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.463 in the same entry: 'ai. gātú-ḥ „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. s.v. gātu- (cited by Mo'in as col. 517)\", \"stance\": \"supports\",\n       \"note\": \"The word runs through BRT.txt in dozens of citations as 'gātu(š)' — e.g. 'yahmya stərətasca gātuš', 'daityō gātuš „der gehörige Platz“' (N.75), 'gātu … xᵛaršti.starətu' (V.7.14) — always 'place, seat', never a form *gāv.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 677\", \"stance\": \"supports\",\n       \"note\": \"'av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu (θ aus t vor u, Bartholomae Grdr. d. iran. Phil. I 8)' — including the phonetic note that OP θ here comes from t before u, which is why the two languages differ.\"},\n      {\"src\": \"SPG\", \"where\": \"Glossar p.217 s.v. Gāthu\", \"stance\": \"supports\",\n       \"note\": \"'Gāthu 1) Ort, Platz, instr. gāthvā „an seinem Orte“ … 2) Thron, acc. gāthum NRa,41. Aw. gātu, neup. گاه, beide Wörter mit denselben Bedeutungen.'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Persian\",\n     \"words\": \"gâh 2 «گاه ۲» : place, position, rank (extras: دانشگاه ، خانگاه ، خانقاه ، گهواره)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OP gāθu- / Av. gātu- > MP gāh (Book Pahlavi gʾs, Manichaean gʾh) > NP گاه 'place, throne, position, rank': Old Iranian intervocalic *-θ-/-t- of the tu-stem is lost and the word ends in -āh (compare rāθa- > rāh). The New Persian word keeps both halves of the old meaning, the spatial ('place, throne': تخت‌گاه, بارگاه) and the derived temporal ('time': صبحگاه, هنگام), which is why Nourai numbers it 'gāh 2' against the homonym gāh 'Gatha, song' < Av. gāθā. The extras are compounds of it: دانشگاه 'university' (a 20th-c. coinage, دانش + گاه), خانگاه > Arabicised خانقاه 'khanqah', and گهواره/گاهواره 'cradle' = گاه + واره (bar- 'to bear'), i.e. the node-6 compound gātu-bar. It is worth noting that the same Middle Persian gāh was borrowed outward into Old Armenian gah 'throne' and Syriac gāhā, which is the network Wiktionary lists.\",\n     \"derivation_fa\": \"«گاه» از فارسی میانهٔ gāh (پهلوی کتابی gʾs، مانوی gʾh) و آن از gāθu- پارسی باستان و gātu- اوستایی است: همخوان میان‌واکه‌ای ستاک tu-دار افتاده و واژه به -āh پایان یافته است (قس rāθa- > راه). فارسی نو هر دو معنای کهن را نگه داشته است: مکانی («جا، تخت، مقام» در تخت‌گاه، بارگاه) و زمانی («وقت» در صبحگاه، هنگام)؛ به همین سبب نورایی آن را «گاه ۲» شماره زده تا از «گاه» به معنی «گاثا، سرود» (از gāθā اوستایی) جدا شود. ترکیب‌های حاشیه نیز از همین‌اند: «دانشگاه» (ساختهٔ سدهٔ چهاردهم خورشیدی)، «خانگاه» که معرّب آن «خانقاه» است، و «گهواره/گاهواره» یعنی گاه + واره از bar- «بردن» — همان gātu-bar گرهٔ ۶. همین واژه به ارمنی کهن gah «تخت» و سریانی gāhā نیز وام رفته است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"گاه\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1771\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāṭeʿ printed p.1771 (= v3 pdf scan p.568, running head ۱۷۷۱), s.v. گاه: 'بر وزن ماه. تخت پادشاهان و کرسی زرین را گویند – و بمعنی وقت و زمان باشد … و بمعنی جا و محل و مقام هم هست'; Mo'in's footnote 3: 'پارسی باستان gathu (مکان، تخت)، اوستا gātu (جا، تخت)؛ پهلوی gās … ارمنی gah (تخت، کرسی) … هوبشمان ۸۸۹؛ … بارتولمه ۵۱۷؛ نیبرگ ص ۷۸-۷۹'. This is Nourai's arrow, source and all.\"},\n      {\"ref\": \"BQT:1773\", \"status\": \"supports\",\n       \"note\": \"Same volume, printed p.1773 (v3 pdf 570), s.v. گاهواره: Mo'in's footnote 2 'ظ. از: گاه + واره (پسوند) از مصدر bar [بردن]، لغةً حامل تخت (کودک) – گهواره (مخفف) – گاواره؛ پهلوی gāhvārak «تاوادیا ۱۵۱»' — the source of the extra گهواره and of node 6's gātu-bar.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, s.vv. gāh, a-gāh, āgāh\", \"stance\": \"supports\",\n       \"note\": \"PHD.txt line 175: 'a-gāh [ʾgʾs] without rank. āgāh [ʾkʾs | M ʾg(h), N ~] aware, knowing'; line 247 '~-gāh [-gʾs] sleeping-platform, bench, couch'; the index line 4017 gives 'time … bar, gāh, hangām, jar, zamān(ag), zurwān'. Middle Persian gāh has exactly the two senses (place/rank and time).\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, s.v. جاه (MON_part1.txt line 47042)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in tags جاه '[- گاه معرّب]' (the OCR renders the bracket as '[- جاه معر.]', but the format '[- X معر.]' means “from X, Arabicised” and X can only be گاه), 'مقام، منزلت، درجه، رتبه، جلال، فر و شکوه' — i.e. Mo'in himself makes گاه the source of Arabic جاه, corroborating nodes 8-9 from this node.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann (cited by Mo'in at Borhān 1771 n.3 as p.889)\", \"stance\": \"supports\",\n       \"note\": \"Mo'in's footnote credits 'هوبشمان ۸۸۹' for the Armenian loan gah 'throne, chair' beside NP گاه; the local HUB.txt (Persische Studien) does not carry that page (it is Hübschmann's Armenische Grammatik), so the citation is verified only at second hand.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Arabic\",\n     \"words\": \"jâh : rank\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle/New Persian gāh 'place, throne, rank' was taken into Arabic as جاه jāh 'rank, dignity, standing'. The consonant substitution is the standard one for Persian loans in Arabic, since Arabic has no /g/: Persian g- is rendered by ج j- (gawhar > jawhar, gurbuz > jarbaz, gulāb > julāb), and Persian -āh is kept as -āh. Semantically only the 'rank, standing' branch of the polysemous Persian word was borrowed. Arabic lexicographers of the classical period (Lisān al-ʿArab, and Lane after them) instead explained jāh as a maqlūb, a metathesis of وجه wajh 'face, favour, esteem'; that is an Arabic-internal folk analysis which modern scholarship has abandoned in favour of the Iranian source, and Mo'in explicitly tags the word معرَّب 'Arabicised'. Nourai's own reference here, Emām Šuštari's Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi, is a specialist dictionary of exactly such loans.\",\n     \"derivation_fa\": \"«گاه» فارسی میانه/نو به معنی «جا، تخت، مقام» به عربی راه یافته و به‌صورت «جاه» (منزلت، آبرو) درآمده است. ابدال آوایی همان ابدالِ همیشگی وام‌واژه‌های فارسی در عربی است، زیرا عربی واج /g/ ندارد و آن را با «ج» می‌نویسد (گوهر > جوهر، گربز > جربز، گلاب > جلاب)، و «-اه» پایانی دست‌نخورده می‌ماند. از میان معناهای چندگانهٔ واژهٔ فارسی تنها شاخهٔ «مقام و منزلت» وام گرفته شده است. فرهنگ‌نویسان کهن عرب (لسان‌العرب و پس از آن لِین) «جاه» را مقلوبِ «وجه» می‌دانستند؛ این ریشه‌شناسی درون‌عربی امروز کنار گذاشته شده و معین نیز واژه را صریحاً «معرّب» گاه می‌داند. مأخذ خود نورایی، «فرهنگ واژه‌های فارسی در زبان عربی» امام شوشتری، فرهنگی است ویژهٔ همین وام‌واژه‌ها. ادعای نورایی درست است.\",\n     \"sources\": [W + \"جاه\", W + \"گاه\"],\n     \"ref_check\": [\n      {\"ref\": \"FVF:144\", \"status\": \"not_checked\",\n       \"note\": \"FVF = S.M.A. Emām Šuštari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi (Tehran 1347). refs_online.json marks it 'website' only: noorlib.ir/book/view/105056 needs a browser page-viewer and ketabnak needs a login; it is not on archive.org, so p.144 could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. جاه (MON_part1.txt line 47042)\", \"stance\": \"supports\",\n       \"note\": \"'جاه: [- گاه، معرّب] (اِ.) مقام، منزلت، درجه، رتبه، جلال، فر و شکوه' — Mo'in derives the Arabic/Persian جاه from گاه and marks it Arabicised.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, ج section (PLA_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"Grepped PLA_pages.txt for 'jāh' and 'gāh': no entry. Asbaghi's list of Persian loans in Arabic does not include جاه, so his silence neither supports nor contradicts.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"Grepping 'جاه' in AFM_pages.txt returns only الجاهة 'large round rock', الجهوري (from جاهوار), جاهجور and جاهل — no article on جاه 'rank'.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Persian\",\n     \"words\": \"jâh «جاه» : position\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A round trip: Persian گاه was Arabicised as جاه (node 8) and then re-entered New Persian as an Arabic loanword, جاه 'position, dignity, standing', so that Persian now has the doublet گاه ~ جاه, the second being merely the first in Arabic dress. It is treated as an Arabic word by Persian lexicographers (Mo'in's tag) and behaves as one, taking Arabic-style derivatives and collocations (جاه و جلال, ذوالجاه). Wiktionary states the chain explicitly: 'Persian جاه: borrowed from Arabic جاه (jāh), from Middle Persian gʾs, gāh “place, throne, bed; time”. Doublet of گاه.'\",\n     \"derivation_fa\": \"این گره یک رفت‌وبرگشت است: «گاه» فارسی در عربی «جاه» شد (گرهٔ ۸) و سپس همان «جاه» به‌عنوان وام‌واژهٔ عربی به فارسی بازگشت، چنان‌که امروز فارسی دو صورت «گاه» و «جاه» را در کنار هم دارد و این دو دوگانه (doublet) یکدیگرند. فرهنگ‌نویسان فارسی «جاه» را واژه‌ای عربی می‌شمارند و خودِ واژه نیز مانند واژه‌های عربی رفتار می‌کند و ترکیب‌های عربی‌گونه می‌سازد (جاه و جلال، ذوالجاه). ویکی‌واژه همین زنجیره را می‌آورد: «فارسی جاه، وام‌گرفته از عربی جاه، از فارسی میانهٔ gāh «جا، تخت؛ زمان»، دوگانهٔ گاه». ادعای نورایی درست است.\",\n     \"sources\": [W + \"جاه\"],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\",\n       \"note\": \"Nourai cites MON without a page; the entry is Mo'in's جاه (MON_part1.txt line 47042): 'جاه: [- گاه، معرّب] (اِ.) مقام، منزلت، درجه، رتبه' — the Persian word, tagged as the Arabicised form of گاه, with exactly the gloss 'position' Nourai gives.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. جاه\", \"stance\": \"supports\",\n       \"note\": \"See the ref_check: Mo'in has the word with the origin tag, and neighbouring entries جاهد, جاهل, جاهلیت are marked plain '[ع.]' (Arabic), while جاه alone gets the معرّب tag — i.e. Mo'in distinguishes it from genuinely Arabic-root words.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. gāh (indirect)\", \"stance\": \"supports\",\n       \"note\": \"MacKenzie's MP gāh [gʾs] 'place, throne, time' is the form Arabic borrowed; the Persian جاه therefore stands to گاه as an Arabic-mediated doublet of the same Middle Persian word.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"Old Persian\",\n     \"words\": \"ham-gmatana, hangmatâna : (a place for) coming together\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian Ha(n)gmatāna- (cuneiform h-g-m-t-a-n, the nasal not written, whence Kent's superscript notation haⁿgmatāna) is the name of the Median capital. It is transparently ham- 'together' + the zero-grade participle *gmata- 'come' (Kent: '-gmata- “gone”, to root gam-, in paragmatā, haⁿgmatā, Hagmatāna-') plus the place-forming suffix -na-, i.e. 'the place of coming-together, the assembly-place' — the same formation as the participle haⁿgmatā 'assembled' used six times in the Bisotun inscription (DB 2.32, 38, 43, 52, 58; 3.65). Nourai's two spellings are Kent's participle stem (ham-gmata-) and the toponym; the gloss is the standard one.\",\n     \"derivation_fa\": \"«هگمتانه» (پارسی باستان Ha(n)gmatāna-، در خط میخی h-g-m-t-a-n که «ن» غنه در آن نوشته نمی‌شود و از این‌رو کنت آن را با «ن» کوچک بالانویس می‌نگارد) نام پایتخت ماد است. ساخت آن روشن است: پیشوند ham- «با هم» + صفت مفعولی بی‌درجهٔ *gmata- «آمده» + پسوند مکان‌ساز -na-، یعنی «جای گردآمدن، انجمن‌گاه». همین صفت مفعولی haⁿgmatā «گردآمده» شش بار در سنگ‌نبشتهٔ بیستون آمده است (بند ۲.۳۲، ۳۸، ۴۳، ۵۲، ۵۸ و ۳.۶۵). دو صورتی که نورایی آورده، یکی ستاک صفت مفعولی و دیگری خود نام‌جای است و معنایی که داده همان معنای پذیرفتهٔ همگان است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"Ecbatana\"],\n     \"ref_check\": [\n      {\"ref\": \"KNT:212\", \"status\": \"partial\",\n       \"note\": \"Kent's own analysis is in the file, though the H-page of the Lexicon (printed 212-213) is missing from this OCR: line 1321 reads '-gmata- “gone”, to root gam-, in paragmatā, haⁿgmatā, Hagmatāna-', and the gam- article (Lexicon p.183) ends 'ham- + gam- “come together, assemble”: haⁿgmatā npm. past pte. (§101, §244) DB 2.32, 38, 43, 52, 58; 3.65. See also Hagmatāna-.' The claim is Kent's; only the cited page itself could not be displayed.\"},\n      {\"ref\": \"BQT:2368\", \"status\": \"supports\",\n       \"note\": \"Borhān printed p.2368 (= v4 pdf 451), Mo'in's footnote 5 s.v. همدان: 'پهلوی Hamadān «مارکوارت، شهرستانهای ایران»، پارسی باستان Ha(n)gmatāna «کنت، پارسی باستان»، … «اشپیگل» … که پایتخت شاهی در عهد مادها بود. در عیلامی ʾa(g)-ma-da-na، آکدی a-ga-ma-ta-nu، یونانی Agbatana / Ekbatana … محتملاً مشتق از …' (the note runs on to the next page).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Old Persian, §250 and text of DB (KNT.txt lines 1975, 2038, 2704, 3619)\", \"stance\": \"supports\",\n       \"note\": \"'Māda “Media”: … city Hagmatāna'; the locative 'Hagmatānaiy' in the case-list; and DB 2.76 'pasāvašim Hagmatānaiy uzmayāpatiy akunavam “afterwards I put him on the stake at Ecbatana”'.\"},\n      {\"src\": \"SPG\", \"where\": \"Glossar p.217 s.v. gam\", \"stance\": \"supports\",\n       \"note\": \"'+ ham zusammenkommen, Participialperf. plur. hangmatā Bh. II, 32. 38. 43. 52. 58. III, 64.' Spiegel already analyses the participle as ham + gam.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wb. (Old Persian section)\", \"stance\": \"silent\",\n       \"note\": \"Bartholomae's dictionary treats Avestan and Old Persian together but has no separate article on the Median toponym; grepping 'hagmat/hangmat' in BRT.txt returns nothing.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Persian\",\n     \"words\": \"Ekbâtân «اکباتان (همدان)»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Two continuations of node 10. The Persian city name همدان Hamadān is the direct descendant: OP Ha(n)gmatāna- > Middle Persian Hamadān (with loss of the -g- cluster and of the final -a) > NP همدان. اکباتان Ekbātān, by contrast, is the round-trip form: the Greeks heard the Median name as Ἐκβάτανα Ekbátana (Herodotus onwards, Greek k rendering the Iranian -g- and the initial h- being dropped), Latin took it as Ecbatana, and modern Persian re-borrowed that European shape as اکباتان — which is why the two names stand side by side in the box, as Wiktionary puts it, 'Doublet of Hamadan'. Nourai gives no gloss for the node, but the parenthesis (همدان) is his own identification and is correct.\",\n     \"derivation_fa\": \"این گره دو دنبالهٔ گرهٔ ۱۰ را در کنار هم می‌گذارد. «همدان» بازماندهٔ مستقیم است: پارسی باستان Ha(n)gmatāna- > فارسی میانه Hamadān (با ساده‌شدن خوشهٔ -gm- و افتادن پایانه) > فارسی نو همدان. اما «اکباتان» صورت رفت‌وبرگشتی است: یونانیان نام مادی را Ἐκβάτανα (اکباتانا) شنیدند — «ه» آغازین افتاده و «گ» ایرانی با «ک» یونانی نوشته شده — لاتین آن را Ecbatana گرفت و فارسی امروز همان صورت اروپایی را دوباره وام گرفت. پس «اکباتان» و «همدان» دوگانهٔ یکدیگرند، چنان‌که ویکی‌واژه نیز می‌نویسد. کمانکِ «(همدان)» در نمودار از خود نورایی است و درست است.\",\n     \"sources\": [W + \"Ecbatana\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2368\", \"status\": \"supports\",\n       \"note\": \"Mo'in's footnote 5 to Borhān p.2368 s.v. همدان (v4 pdf 451) sets out exactly this: 'پهلوی Hamadān … پارسی باستان Ha(n)gmatāna «کنت» … در عیلامی …، آکدی …، یونانی Agbatana / Ekbatana …' — the Persian, Greek and cuneiform names of one place.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Old Persian, §18 n.2 and the DB translation (KNT.txt lines 472, 477, 3680)\", \"stance\": \"supports\",\n       \"note\": \"Kent identifies the site: 'the two inscriptions are both on gold tablets and found at or near Ecbatana (Hamadan) in Media' and translates DB 2.76 'Afterward I impaled him at Ecbatana'.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, aʿlām volumes (not in the local OCR)\", \"stance\": \"silent\",\n       \"note\": \"Mo'in's proper-name volumes (5-6) are not among the local MON OCR files, so his اکباتان/همدان article could not be consulted; Borhān 2368 (above) carries the same author's note.\"}\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"jamâna : a step (period) of time; thamân : time\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The first word is right and is the heart of the whole zamān complex: Old Persian *jamānā- / Old Iranian *ǰamāna- is an -āna- derivative of the root in its j-shape (see node 1), literally 'a going, a course' and thence 'a period, time' — the same semantic step English makes in 'the passage of time'. Nyberg states it flatly at the page Nourai cites, and Cheung lists 'NP zamān “time”' among the reflexes of *gam¹. The second word, 'thamân', is the problem: no such form exists in Bartholomae, Kent, Nyberg or Cheung (grepped BRT.txt, KNT.txt and NYB_vol2_glossary.txt for θaman-/thaman-/Vamana: nothing). The printed page really does read 'thamân' (checked on the page image), so this is the book's own error, not the extraction's. The likeliest original is žamān, i.e. the Parthian/north-western form jmʾn = žamān that Nyberg gives on the very page Nourai cites ('MPrth jmn; Arm. lw. žam, žamanak'), whose ž- Nourai's typesetting has turned into 'th-'; a second possibility is that it is simply a doubled, garbled printing of zamān.\",\n     \"derivation_fa\": \"واژهٔ نخست درست و در واقع کلیدِ همهٔ این بخش است: *jamānā- پارسی باستان (ایرانی باستان *ǰamāna-) مشتقی است با پسوند -āna- از همان ریشه در صورت j-دار (گرهٔ ۱)، به معنای تحت‌اللفظی «رفتن، سیر» و از آنجا «دوره، زمان» — همان تحول معنایی که در «گذشتِ زمان» فارسی نیز هست. نیبرگ در همان صفحه‌ای که نورایی یاد کرده این را صریح می‌گوید و چونگ نیز «NP zamān» را در شمار بازمانده‌های *gam¹ می‌آورد. اما واژهٔ دوم، «thamân»، در هیچ‌یک از بارتولمه، کنت، نیبرگ و چونگ یافت نشد. تصویر صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «thamân» چاپ کرده است، پس خطای چاپ کتاب است نه خطای خوانش اسکن. محتمل‌ترین صورت درست žamān است، یعنی همان صورت پارتی/شمال‌غربی jmʾn = žamān که نیبرگ در همان صفحهٔ ۲۲۸ آورده («MPrth jmn؛ وام‌واژهٔ ارمنی žam، žamanak») و «ژ» آن در حروف‌چینی نورایی به «th» بدل شده است؛ احتمال دوم آن است که صورتی مغلوط از خودِ zamān باشد.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"jamâna : a step (period) of time ; thamân : time\",\n     \"correct_form\": \"*jamāna- (OP *jamānā-); the second form is most likely žamān (Parthian jmʾn)\",\n     \"sources\": [W + \"زمان\"],\n     \"ref_check\": [\n      {\"ref\": \"NYB:228\", \"status\": \"supports\",\n       \"note\": \"Nyberg, Manual of Pahlavi II (Glossary) p.228 (NYB_vol2_glossary.txt leaf 249, the leaf carrying the running number 228), s.v. zamān: 'zamān [zmʾnʼ], jaman [ymʾnʼ; ʾDNʾ] time, passim … MPrth jmn; Arm. lw. žam, žamanak; MPrs zmʾn; Paz. jamą̇n, zamą̇; NP zamān; zaman and zamān loaned into Aram and Arab. From gam-, v. āmatan and žām-.' Every element of Nourai's node 12/14 claim is on that page.\"},\n      {\"ref\": \"PLA:146\", \"status\": \"supports\",\n       \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen p.146 (PLA_pages.txt leaf 161), s.v. zaman: '„Zeit, Epoche, Jahreszeit, Saison“ pers. زمان; prth. jmʾn, mp. zamān, paz. jaman. zaman u. jaman sind über das Aram. ins Ar. gelangt. v. Verb آمدن āmadan „kommen“, mp. āmatan, av./ap. gam, mand. zaman.'\"},\n      {\"ref\": \"SBK:203\", \"status\": \"not_checked\",\n       \"note\": \"SBK = Bahār, Sabk-šenāsi. The local SBK.txt is a raw djvu dump with no page breaks or page markers, so p.203 cannot be located; grepping for زمان + معرّب and for ثمان turned up no etymological discussion of the word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, *NWIR and *BACTRIAN sections\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP zamān “time” …' and '*BACTRIAN: ζοροχο “time”' are listed as reflexes of *gam¹, i.e. Cheung too derives 'time' words from this root; his *MIDDLE PERSIAN line has 'MMP zʾm- “to …”' beside the pret. stem mad-.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. zamān (PHD.txt line 677)\", \"stance\": \"partial\",\n       \"note\": \"'zamān [ʾDWMA < A ʿdw; gwnʾ, zmn! | M zmn, N ~] time, hour. ~ag [zmʾnk!] = zamān. *zamānīg [zmʾnykʼ] prescribed.' MacKenzie gives the Middle Persian word and its Aramaic ideogram but, as always, no etymology — he confirms the form, not the derivation.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"silent\",\n       \"note\": \"Grepped BRT.txt for jamāna/jāman/θaman: the Avestan dictionary has no *jamāna- 'time' and no θamān-. This is why Mo'in, Nyberg and Asbaghi all label the word Old Persian / Old Iranian rather than Avestan — Nourai's box label 'Avestan / Old Persian' is half right.\"}\n     ]\n    },\n    {\n     \"id\": 13,\n     \"lang\": \"Persian\",\n     \"words\": \"zamân «زمان» : time\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The inherited line: Old Persian *jamānā- > Middle Persian zamān (Book Pahlavi zmnʼ / the Aramaic ideogram ʿDNʾ, Manichaean zmʾn) > NP زمان. The south-western treatment turns Old Iranian *ǰ- into z- (compare *ǰan- > zadan, *ǰāmātar- > dāmād's north-western/south-western pairs), while the north-west keeps ǰ/ž — hence Parthian jmʾn = žamān and Pazand jamą̇n beside Middle Persian zamān. Persian زمان is therefore NOT a re-borrowing from Arabic زمان (node 14) even though the two are homographs: it comes down the Iranian line directly, as Wiktionary sets out ('From Middle Persian zamān … from Old Persian *jamānā'). Ferdowsi's line quoted in the box uses it in its plain sense 'time, span of life'.\",\n     \"derivation_fa\": \"این گره خطِ ارثی واژه است: پارسی باستان *jamānā- > فارسی میانهٔ zamān (به خط پهلوی zmnʼ و با هزوارش ʿDNʾ، در مانوی zmʾn) > فارسی نو «زمان». در گویش جنوب‌غربی، «ǰ» ایرانی باستان به «ز» بدل می‌شود (قس *ǰan- > زدن) حال آنکه شمال‌غربی «ج/ژ» را نگه می‌دارد؛ از این‌روست که در کنار zamān فارسی میانه، صورت پارتی jmʾn = žamān و پازند jamą̇n داریم. نکتهٔ مهم آنکه «زمان» فارسی وام‌واژهٔ عربی نیست — هرچند با «زمانِ» عربی (گرهٔ ۱۴) هم‌نویسه است — بلکه از راه ارثی ایرانی به فارسی رسیده است، چنان‌که ویکی‌واژه می‌نویسد. بیت فردوسی در جعبه نیز همین معنای ساده «زمان، مهلت عمر» را دارد. ادعای نورایی درست است.\",\n     \"sources\": [W + \"زمان\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:1746\", \"status\": \"not_found\",\n       \"note\": \"Mo'in's Farhang-e Fārsi p.1746 could not be read: the local OCR (MON_part1/part2.txt) has no clean headword block for زمان (only compounds such as 'قد زمان', 'هر زمان'), and the web copies of Mo'in (abadis.ir/fatofa/زمان, fetched) render their content in JavaScript, so the archived text contains only the site chrome.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.228 s.v. zamān\", \"stance\": \"supports\",\n       \"note\": \"'zamān [zmʾnʼ], jaman … NP zamān … From gam-, v. āmatan and žām-' — Nyberg puts the MP > NP step and the root in one line.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. zamān (PHD.txt line 677)\", \"stance\": \"supports\",\n       \"note\": \"'zamān … | M zmn, N ~] time, hour' — MacKenzie's 'N ~' means the New Persian form is identical, i.e. MP zamān = NP زمان.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, *NWIR section\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP zamān “time”' heads the list of New Persian reflexes of the root.\"}\n     ]\n    },\n    {\n     \"id\": 14,\n     \"lang\": \"Arabic\",\n     \"words\": \"zamân : time\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic زمان/زمن zamān/zaman 'time' is an Iranian loan that reached Arabic through Aramaic. The route, as Nyberg and Asbaghi state it, is Old Persian *jamānā- > Parthian žamān / Middle Persian zamān > Imperial and later Aramaic zĕmān (Syriac zabnā, Mandaic zaman; Hebrew זְמָן in the late books, Daniel, Esther, Nehemiah) > Arabic زمان, whence a fully naturalised Arabic root ز م ن with verb زَمِنَ and the derivatives of node 15. Wiktionary's Arabic entry is explicit: 'From a form of Aramaic zmnʾ, from a late pronunciation of Old Persian *jamānā “time”.' Nourai's NOTE on this node is accurate on both counts and states a real dispute: Klein does derive the word from Akkadian (see the ref_check), and Nyberg does claim the Iranian source. On which side modern scholarship stands: the Iranists (Nyberg 1974, Asbaghi 1988, Cheung 2007, Wiktionary) take the Iranian origin as established, and this is now the majority view; the Akkadian derivation, championed by Semitists of Klein's generation (and still defended for Aramaic zĕmān by e.g. Kaufman's Akkadian Influences on Aramaic), survives as a minority alternative. Nourai has represented the disagreement fairly.\",\n     \"derivation_fa\": \"«زمان/زمن» عربی وام‌واژه‌ای ایرانی است که از راه آرامی به عربی رسیده. مسیر آن، چنان‌که نیبرگ و اصباغی می‌نویسند، چنین است: پارسی باستان *jamānā- > پارتی žamān / فارسی میانه zamān > آرامی zĕmān (سریانی zabnā، مندایی zaman؛ عبری זְמָן در بخش‌های متأخر تورات مانند دانیال و استر و نحمیا) > عربی «زمان»، و سپس در عربی ریشهٔ سه‌همخوانیِ کاملاً بومی‌شدهٔ ز م ن با فعل «زَمِنَ» و مشتقات گرهٔ ۱۵ پدید آمده است. ویکی‌واژه نیز صریح می‌گوید: «از صورتی از آرامی zmnʾ، از تلفظ متأخر پارسی باستان *jamānā». یادداشتی که نورایی زیر این گره آورده در هر دو بخش درست نقل شده و اختلافی واقعی را بازمی‌تاباند: کلاین به‌راستی واژه را از اکدی simānu «وقتِ مقرر» می‌گیرد و نیبرگ به‌راستی آن را ایرانی می‌داند. داوری امروزی: ایران‌شناسان (نیبرگ ۱۹۷۴، اصباغی ۱۹۸۸، چونگ ۲۰۰۷، ویکی‌واژه) خاستگاه ایرانی را پذیرفته‌اند و این دیدگاه اکنون رأی غالب است؛ نظر اکدی، که سامی‌شناسانِ نسل کلاین از آن دفاع می‌کردند، هنوز به‌عنوان دیدگاه اقلیت باقی است. نورایی این اختلاف را منصفانه گزارش کرده است.\",\n     \"sources\": [W + \"زمان\"],\n     \"ref_check\": [\n      {\"ref\": \"PLA:146\", \"status\": \"supports\",\n       \"note\": \"Asbaghi p.146 s.v. zaman: 'pers. زمان; prth. jmʾn, mp. zamān, paz. jaman. zaman u. jaman sind über das Aram. ins Ar. gelangt. v. Verb آمدن āmadan „kommen“, mp. āmatan, av./ap. gam, mand. zaman.' The Arabic word is listed in a dictionary of Persian loans in Arabic — exactly Nourai's arrow, including the Aramaic mediation.\"},\n      {\"ref\": \"NYB:228\", \"status\": \"supports\",\n       \"note\": \"Nyberg p.228 s.v. zamān: '… NP zamān; zaman and zamān loaned into Aram and Arab. From gam-, v. āmatan and žām-.' This is verbatim the claim Nourai's NOTE attributes to NYB:228.\"},\n      {\"ref\": \"KLN:951\", \"status\": \"supports\",\n       \"note\": \"Checked because the chart's NOTE cites it. Klein, s.v. 'mazuma' (the block whose page number is 951 in the 1966 two-volume edition; KLN_1971.txt line 147147 ff.): 'Heb. zᵉman, “appointed time, time”, which is rel. to Aram. zᵉman, Syr. zᵉbhan, zabhnā, Arab. zaman, zamān, Ethiop. zaman, “time”. All these words derive directly or indirectly fr. Akkad. simānu, “appointed time”.' Nourai's report of Klein is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹\", \"stance\": \"supports\",\n       \"note\": \"Cheung's Iranian-verb dictionary lists NP zamān under *gam¹ without qualification, i.e. the modern Iranist handbook treats the 'time' word as Iranian in origin.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n       \"note\": \"No article on زمان in AFM_pages.txt; Addi Shir's list of Persian Arabicisms does not include it, presumably because by his day the word was felt to be wholly Arabic.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. mazuma (p.951)\", \"stance\": \"contradicts\",\n       \"note\": \"As quoted above, Klein makes Hebrew/Aramaic/Arabic/Ethiopic 'time' all descend 'directly or indirectly' from Akkadian simānu, i.e. he contradicts the Iranian source. This is the dispute the chart's own NOTE records.\"}\n     ]\n    },\n    {\n     \"id\": 15,\n     \"lang\": \"Persian\",\n     \"words\": \"mozmen «مزمن» : old; azmaneh «ازمنه» : times\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Once زمان had been naturalised in Arabic (node 14), Arabic morphology went to work on the new root ز م ن and Persian then borrowed the products back. مزمن mozmen is the Form-IV active participle مُزْمِن of أَزْمَنَ 'to last a long time, become chronic', hence 'chronic, inveterate, long-standing' — Nourai's gloss 'old' is a loose but not wrong rendering, though the usual Persian sense is 'chronic' (بیماری مزمن). ازمنه azmena is the Arabic broken plural أَزْمِنَة of زمان on the pattern afʿila, 'times, epochs' (ازمنهٔ گذشته). Both are Arabic-made words on a Persian-made root, so the loop Persian > Aramaic > Arabic > Persian closes twice over.\",\n     \"derivation_fa\": \"پس از آنکه «زمان» در عربی بومی شد (گرهٔ ۱۴)، صرف عربی بر ریشهٔ نوپدید «ز م ن» کار کرد و فارسی فرآورده‌های آن را دوباره وام گرفت. «مزمن» اسم فاعلِ باب افعال (مُزْمِن) از «أزمن» به معنی «دیرپاییدن، کهنه و مزمن شدن» است، یعنی «دیرینه، مزمن»؛ معنای «old» که نورایی داده برگردانی آزاد ولی نادرست نیست، هرچند کاربرد رایج فارسی «مزمن» است (بیماری مزمن). «ازمنه» جمع مکسر عربی «زمان» بر وزن أفعِلَة است، یعنی «زمان‌ها، روزگاران» (ازمنهٔ گذشته). هر دو واژه ساختهٔ صرف عربی بر ریشه‌ای ایرانی‌تبارند؛ پس چرخهٔ فارسی > آرامی > عربی > فارسی دوباره بسته می‌شود. ادعای نورایی درست است.\",\n     \"sources\": [W + \"مزمن\", W + \"زمان\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:1746\", \"status\": \"not_found\",\n       \"note\": \"As for node 13: Mo'in p.1746 is not readable in the local OCR (MON_part1/part2.txt carry only running uses of ازمنه, e.g. 'هنگام‌ها؛ روزگارها، ساعات، ازمنه، اوقات', not the headword block), and the abadis/vajehyab copies of Mo'in are JavaScript-rendered, so the archived page text contains no entry.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. mazuma (p.951)\", \"stance\": \"supports\",\n       \"note\": \"Klein's article shows the same Semitic denominative machinery at work on this root in Hebrew: 'Mishnaic Heb. mᵉzumman is passive part. of zimmen “he invited, designated, appointed, fixed”, a verb denominated fr. Heb. zᵉman, “appointed time, time”' — the exact parallel to Arabic أزمن > مزمن.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi p.146\", \"stance\": \"supports\",\n       \"note\": \"Asbaghi lists the Arabic derivatives built on the loan alongside it: 'zamānī “zeitlich, weltlich“ Nisba v. zamān', 'zamanidin “zu eben der Zeit“' — i.e. the root was productive in Arabic, which is the precondition for مزمن and ازمنه.\"}\n     ]\n    },\n    {\n     \"id\": 16,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"gâma : a step (period) of time; han-gâma : at the same time, during\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The same *gāma- 'step' as in node 3, here taken temporally: a 'step' of time is a moment, a season, an occasion (compare Latin tempus beside Greek temnō 'cut', or English 'a spell'). *ham-gāma- is 'a stepping-together, a coinciding', hence 'the (right) time, the occasion, during'. Middle Persian has hangām 'time, occasion' (MacKenzie), Pazand hangām, and the compound was borrowed into Old Armenian as hangamankʻ 'circumstances, way'. Nourai labels the box 'Avestan / Old Persian'; the compound is not directly attested in either corpus and both Mo'in and Wiktionary reconstruct it as Old Persian *hangāma-, so 'Old Persian' is the accurate half of the label.\",\n     \"derivation_fa\": \"همان *gāma- «گام» گرهٔ ۳ است که این‌بار در معنای زمانی به کار رفته: «گامی» از زمان یعنی لحظه، هنگام، فصل (قس tempus لاتین در کنار temnō یونانی «بریدن»). *ham-gāma- یعنی «هم‌گام‌شدن، هم‌زمان‌افتادن» و از آنجا «وقت مناسب، در هنگامِ». فارسی میانه hangām «وقت، هنگام» دارد (مکنزی) و همین واژه به ارمنی کهن hangamankʻ «احوال، شیوه» وام رفته است. برچسب «اوستایی/پارسی باستان» را باید با احتیاط خواند: این ترکیب نه در اوستا و نه در سنگ‌نبشته‌های هخامنشی گواه مستقیم ندارد و معین و ویکی‌واژه هر دو آن را «پارسی باستان *hangāma-» بازسازی می‌کنند؛ پس نیمهٔ «پارسی باستان» برچسب درست است. جز این، ادعای نورایی درست است.\",\n     \"sources\": [W + \"هنگام\", W + \"گام\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2383\", \"status\": \"supports\",\n       \"note\": \"Borhān-e Qāṭeʿ printed p.2383 (= v4 pdf 466), s.v. هنگام: 'بر وزن اندام، بمعنی وقت و زمان و گاه باشد – و بمعنی موسم و فصل هم آمده است'; Mo'in's footnote 1: 'پارسی باستان *hangāma- (وقت، زمان)، قس اوستایی *hankāma-…؛ پهلوی hangām (پازند hangām) «اشتقاق ۱۱..»؛ ارمنی hangam (دفعه، مرتبه) … «هوبشمان ۱۱۳..»؛ کردی hingām (زمان)'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, index s.vv. occasion, time\", \"stance\": \"supports\",\n       \"note\": \"PHD.txt line 2963 'occasion bar, jar, hangām' and line 4017 'time … bar, gāh, hangām, jar, zamān(ag), zurwān' — MP hangām is real and means 'time, occasion'.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch\", \"stance\": \"silent\",\n       \"note\": \"Grepping BRT.txt for hangāma-/hankāma- returns nothing: Bartholomae has the noun gāman- 'step' but no *ham-gāma- compound, confirming that the Avestan half of Nourai's language label is a reconstruction rather than an attestation.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 677\", \"stance\": \"partial\",\n       \"note\": \"Walde-Pokorny lists the simplex 'av. gāman- n. „Schritt“' and the parallel *gāma- o-stem behind Skt. gāmin-/gāma-, i.e. the base of Nourai's gāma-, but no compound with ham-.\"}\n     ]\n    },\n    {\n     \"id\": 17,\n     \"lang\": \"Persian\",\n     \"words\": \"hengâm «هنگام» : during (extras: ناهنگام ، شب هنگام)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OP *hangāma- > MP hangām > NP هنگام 'time, season, occasion, at the time of'. The word keeps its ham-/han- prefix intact (unlike انجام, where ham- became an-), because before the velar g the nasal simply assimilates to [ŋ]; Wiktionary analyses it synchronically as هن (han-, variant of هم- 'co-') + گام 'step'. The derivatives in the box behave regularly: ناهنگام 'untimely' with the negative prefix نا-, and شب‌هنگام 'at night-time' as an adverbial compound of the type صبحگاه, i.e. the same 'time' sense that گاه carries in node 7. The dictionary sense Nourai gives, 'during', is the adverbial use (هنگامِ ... 'at the time of').\",\n     \"derivation_fa\": \"پارسی باستان *hangāma- > فارسی میانه hangām > فارسی نو «هنگام» به معنی «وقت، موسم، گاه، در زمانِ». برخلاف «انجام» که پیشوند ham- در آن به an- کاهش یافته، در «هنگام» پیشوند دست‌نخورده مانده است، زیرا «م» پیش از «گ» تنها به غنّهٔ [ŋ] همگون می‌شود؛ ویکی‌واژه آن را در تحلیل هم‌زمانی «هن (گونهٔ هم-) + گام» می‌داند. ترکیب‌های حاشیه نیز قانونمندند: «ناهنگام» با پیشوند نفی «نا-» و «شب‌هنگام» ترکیب قیدی از گونهٔ «صبحگاه»، یعنی همان معنای زمانی که «گاه» در گرهٔ ۷ دارد. معنایی که نورایی داده («during») همان کاربرد قیدی «هنگامِ ...» است. ادعای نورایی درست است.\",\n     \"sources\": [W + \"هنگام\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2383\", \"status\": \"supports\",\n       \"note\": \"The Borhān page cited is the هنگام article itself (printed p.2383, v4 pdf 466), with Mo'in's footnote 1 giving 'پارسی باستان *hangāma- (وقت، زمان) … پهلوی hangām (پازند hangām)'; the same page carries هنگامه, هنگامه‌گیر and هنگامی, and a Ferdowsi line for the sense 'time'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, index s.vv. occasion, time, immediately\", \"stance\": \"supports\",\n       \"note\": \"'occasion bar, jar, hangām'; 'time āwām, bar, gāh, hangām, jar, zamān(ag), zurwān'; 'immediately hamzamān' — the MP antecedent of هنگام and, incidentally, of هم‌زمان.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *gam¹, *NWIR section\", \"stance\": \"partial\",\n       \"note\": \"Cheung's New Persian list under *gam¹ has gām, āmadan, pay(g)ām, anjuman and zamān but not hangām; since he is cataloguing verbs and their nominal derivatives, the omission of this particular compound noun is not a disagreement.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (local OCR)\", \"stance\": \"partial\",\n       \"note\": \"MON_part1.txt line 18832 glosses a lemma with 'هنگام‌ها؛ روزگارها، ساعات، ازمنه، اوقات', showing Mo'in treats هنگام as a plain 'time' word and pairs it with the Arabic ازمنه of node 15; his own هنگام headword block is not legible in this OCR.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-202.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build202.py",
 "description": "Write page-202.json"
}
```


### [2026-09-06T02:44:11.761Z] TOOL RESULT

```
written 79602
```


## [2026-09-06T02:44:17.479Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-202.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 202",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T02:44:19.181Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 13, 'plausible': 1, 'disputed': 1, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 22, 'partial': 3, 'not_found': 3, 'not_checked': 3}
books consulted: {'supports': 34, 'partial': 6, 'silent': 8, 'contradicts': 1} | by book: {'PHD': 9, 'CHEUNG': 8, 'BRT': 7, 'MON': 6, 'KNT': 3, 'SPG': 3, 'WLD': 3, 'HUB': 3, 'PLA': 2, 'AFM': 2, 'KLN': 2, 'NYB': 1}
```


## [2026-09-06T02:44:38.159Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-202.json` written; `verify_check.py 202` reports 17/17 nodes, 0 PROBLEM lines.

**Page 202 (book p. 172), root "Gwa, Gwâ, Gwen 2" = PIE \*gʷem-/\*gʷeh₂- (Pokorny 463-465) — root confirmed.**
Node verdicts: 13 confirmed, 1 plausible, 1 disputed, 2 transcription_suspect.
Ref checks: 22 supports, 3 partial, 3 not_found, 3 not_checked. 12 books consulted (34 supports, 1 contradicts).

- **disputed — #3 نیام nîyâm "sheath"**: modern scholarship (Wiktionary, with Wakhi *naẟün*, Skt. *nidhāna-*, Hebrew loan *nāḏān*) derives it from OP \*ni-dāmān- "covering" (root \*ni-dā-), not from \*ni-gam-. Nourai's own source concedes it: Mo'in (Borhān 2223 n.7) offers \*ni-gāma but adds «وجه اشتقاق قطعی نیست». The node's other three words (gām, āmadan, payām) are confirmed; worst-verdict rule applied.
- **transcription_suspect — #6 "gâv"** (in "gât, gâthu, gâv, gâtuš"): the printed page really shows *gâv*, so **error_in: book** — Nourai's misprint for Av. strong stem *gātav-* (Kent p.183 writes "Av. gātav- gāθu-"). Rest of node confirmed.
- **transcription_suspect — #12 "thamân : time"**: printed as such (**error_in: book**); no such form in Bartholomae, Kent, Nyberg or Cheung. Most likely žamān (Parthian jmʾn), which Nyberg gives on the very page cited. The other word, *jamāna*, is fully confirmed.
- **plausible — #2**: forms all real, but the gloss "ni-gama: come down (in sheath)" is back-formed from نیام.
- Chart's NOTE on Arabic زمان checked and correct on both sides: Klein p.951 (s.v. *mazuma*) really does derive it from Akkadian *simānu*; Nyberg p.228 really does say "zaman and zamān loaned into Aram and Arab. From gam-". Modern Iranist consensus (Nyberg, Asbaghi 146, Cheung, Wiktionary) backs the Iranian origin.
- **No extraction errors** — the JSON matches the printed page exactly (page image saved to `data/verification/sources/refs/ocr/BOOK/202.png`).
- Note for the owner: Nourai's `BQT:1451` is printed p. **1449** in the scan (v3 offset drift); `BQT:166` (انجمن) is on the right leaf but its footnote band is lost in the vol-1 djvu OCR and vol 1 has no page-image fallback. FVF:144, ETM and SBK:203 were unreachable.
