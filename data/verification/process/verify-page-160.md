# Verification process log — verify-page-160


## [2026-09-05T20:30:32.471Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 160 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-160.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-160.json. Write /home/sfmqrb/git/rishe/data/verification/page-160.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 160` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:30:34.003Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:30:34.716Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:30:34.749Z] TOOL RESULT

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


## [2026-09-05T20:30:34.960Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-160.txt"
}
```


### [2026-09-05T20:30:34.994Z] TOOL RESULT

```
1	=== PDF page 160 (book page 130) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Eres 1 / Ersen / Ros / Ers / Ere 2 : Eres 1: to flow, to be wet. Ersen: ejector of semen, male. Ros: dew. Ers: to be in motion. Ere 2: to have bad will.  (refs POK:335)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:336; AHD:1480; SOD:414 | aršan, varešna : man, hero ; xšaya-aršan : hero among kings or king of men ☞Ksei 1 ; aršan-aspa : (with) male horses ☞Ekwos ; syâva-aršan : (with) black male animals ☞Kei 1
5	  #2 (parent #1) [Persian] refs=BQT:1119; FNI:34 | Aršân «ارشان» : "man, masculine" ; Xašâyâr «خشایار» : "king of men" ; Aršâsp «ارشاسپ» : "with male horses" ; Sîyâvaš «سیاوش» : "with black horses"
6	#3 (parent #0) [Pahlavi] refs=MON:3329 | vušn, gushn : male ; gušn-asp : (with) male horses ☞Ekwos
7	  #4 (parent #3) [Persian] refs=BQT:1821; HRN:206; MON6:1706; FSF:297 | gošn, gošan «گشن» : male, strong, husband, big, wide ; gošnî «گشنی» : insemination ; Gošnasp «گشنسپ (گشناسب)» : "with male horses", a male name
8	#5 (parent #0) [Sogdian] refs=SOD:414 | wšn : male
9	#6 (parent #0) [Avestan] refs=POK:336; AHD:1115; SOD:339 | ranhâ : vein ; ranha : a mystical river. Former name of Volga was Rha. ; raěvas : rhubarb, grown on Rha (Volga) banks.
10	  #7 (parent #6) [Pahlavi] refs=SOD:339 | rahg : vein ; rag : vein
11	    #8 (parent #7) [Persian] refs=SOD:339 | rag «رگ» : vein
12	  #9 (parent #6) [Persian] refs=BQT:991 | rîvand «ريوند (ریواس)» : rhubarb
13	    #10 (parent #9) [Greek] refs=AHD:1115 | rha : rhubarb ; rhěon
14	      #11 (parent #10) [Latin] refs=AHD:1115 | rha : rhubarb ; rheu-barbarum : foreign rhubarb ☞Baba
15	        #12 (parent #11) [English] refs=None | rhubarb
16	#13 (parent #0) [Avestan] refs=POK:337 | araska : enmity
17	  #14 (parent #13) [Persian] refs=BQT:952 | arašk, rašk «ارشک ، رَشک» : envy, zeal
18	  #15 (parent #13) [Sogdian] refs=SOD:56 | `r`sk : envy
19	#16 (parent #0) [Latin] refs=AHD | ros-maris : sea dew
20	  #17 (parent #16) [English] refs=AHD | Rosemary
21	#18 (parent #0) [Germanic] refs=AHD | rěs : rushing
22	  #19 (parent #18) [English] refs=None | race : compete
23	#20 (parent #0) [Latin] refs=AHD; POK:336 | errâre : to wander
24	  #21 (parent #20) [English] refs=None | error
25	
```


## [2026-09-05T20:30:38.439Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-160.json",
 "description": "Read source JSON for page 160"
}
```


### [2026-09-05T20:30:38.538Z] TOOL RESULT

```
{
  "pdf_page": 160,
  "book_page": 130,
  "entries": [
    {
      "root": {
        "name": "Eres 1 / Ersen / Ros / Ers / Ere 2",
        "lang": "Indo-European",
        "refs": "POK:335",
        "gloss": "Eres 1: to flow, to be wet. Ersen: ejector of semen, male. Ros: dew. Ers: to be in motion. Ere 2: to have bad will."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:336; AHD:1480; SOD:414",
          "words": [
            {"translit": "aršan, varešna", "gloss": "man, hero", "script": null},
            {"translit": "xšaya-aršan", "gloss": "hero among kings or king of men", "script": null, "see": ["Ksei 1"]},
            {"translit": "aršan-aspa", "gloss": "(with) male horses", "script": null, "see": ["Ekwos"]},
            {"translit": "syâva-aršan", "gloss": "(with) black male animals", "script": null, "see": ["Kei 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1119; FNI:34",
          "words": [
            {"translit": "Aršân", "gloss": "\"man, masculine\"", "script": "ارشان"},
            {"translit": "Xašâyâr", "gloss": "\"king of men\"", "script": "خشایار"},
            {"translit": "Aršâsp", "gloss": "\"with male horses\"", "script": "ارشاسپ"},
            {"translit": "Sîyâvaš", "gloss": "\"with black horses\"", "script": "سیاوش"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:3329",
          "words": [
            {"translit": "vušn, gushn", "gloss": "male", "script": null},
            {"translit": "gušn-asp", "gloss": "(with) male horses", "script": null, "see": ["Ekwos"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1821; HRN:206; MON6:1706; FSF:297",
          "words": [
            {"translit": "gošn, gošan", "gloss": "male, strong, husband, big, wide", "script": "گشن"},
            {"translit": "gošnî", "gloss": "insemination", "script": "گشنی"},
            {"translit": "Gošnasp", "gloss": "\"with male horses\", a male name", "script": "گشنسپ (گشناسب)"}
          ],
          "note": null,
          "quote": {
            "text": "درختی گُشَن سایه بر پیش آب - نهان گشته زو چشمهٔ آفتاب",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:414",
          "words": [
            {"translit": "wšn", "gloss": "male", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:336; AHD:1115; SOD:339",
          "words": [
            {"translit": "ranhâ", "gloss": "vein", "script": null},
            {"translit": "ranha", "gloss": "a mystical river. Former name of Volga was Rha.", "script": null},
            {"translit": "raěvas", "gloss": "rhubarb, grown on Rha (Volga) banks.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "SOD:339",
          "words": [
            {"translit": "rahg", "gloss": "vein", "script": null},
            {"translit": "rag", "gloss": "vein", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "SOD:339",
          "words": [
            {"translit": "rag", "gloss": "vein", "script": "رگ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:991",
          "words": [
            {"translit": "rîvand", "gloss": "rhubarb", "script": "ريوند (ریواس)"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Greek",
          "refs": "AHD:1115",
          "words": [
            {"translit": "rha", "gloss": "rhubarb", "script": null},
            {"translit": "rhěon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Latin",
          "refs": "AHD:1115",
          "words": [
            {"translit": "rha", "gloss": "rhubarb", "script": null},
            {"translit": "rheu-barbarum", "gloss": "foreign rhubarb", "script": null, "see": ["Baba"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "rhubarb", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:337",
          "words": [
            {"translit": "araska", "gloss": "enmity", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "BQT:952",
          "words": [
            {"translit": "arašk, rašk", "gloss": "envy, zeal", "script": "ارشک ، رَشک"}
          ],
          "note": null,
          "quote": {
            "text": "من از رَشک روی تو دیدن نیارم - به تیره شب اندر مَهِ آسمانی",
            "poet": "Farrokhî"
          }
        },
        {
          "id": 15,
          "parent": 13,
          "lang": "Sogdian",
          "refs": "SOD:56",
          "words": [
            {"translit": "`r`sk", "gloss": "envy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ros-maris", "gloss": "sea dew", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Rosemary", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "rěs", "gloss": "rushing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "race", "gloss": "compete", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; POK:336",
          "words": [
            {"translit": "errâre", "gloss": "to wander", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "error", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:30:38.757Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:30:38.869Z] TOOL RESULT

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


## [2026-09-05T20:30:43.740Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','SOD','BQT','MON','HRN','FSF','FNI','WLD','IEC','SYN','KLN','BRT','PHD','NYB','ARY','LEW','LAT','SKT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-05T20:31:43.770Z] TOOL RESULT

```
claude-sonnet-5[1m] is temporarily unavailable (timed out), so auto mode cannot determine the safety of Bash right now. Wait a moment and then try this action again. If it keeps failing, continue with other tasks that don't require this action and come back to it later. Note: reading files, searching code, and other read-only operations do not require the classifier and can still be used.
```


## [2026-09-05T20:31:46.973Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','SOD','BQT','MON','HRN','FSF','FNI','WLD','IEC','SYN','KLN','BRT','PHD','NYB','ARY','LEW','LAT','SKT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\"",
 "description": "Print ref metadata for keys used on page 160"
}
```


### [2026-09-05T20:31:48.757Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

FNI {"title": "F. Danayi, Farhang-e Namha-ye Irani, Negah 1370/1991", "kind": "purchase", "url": "in print (Negah)", "lookup_hint": "Not found (archive has an unrelated 'کامل ترین فرهنگ نام های ایرانی' by Flora Jahandar).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; free PDFs with the same generic title online are unrelated name lists."}

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-05T20:31:52.583Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 343 344 345 346; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"' {print}' POK_01.txt | head -80; done",
 "description": "Print POK leaves 343-346"
}
```


### [2026-09-05T20:31:54.356Z] TOOL RESULT

```
=== leaf 343 ===
erativ  a-ar-as-ld-it  (arsJcit)  ,gelangte  wiederholt'  (vgl.  oben  ai. rcchdti) ;
5.  Kausativ  (vgl.  oben  S.  61)  ar-nu-uz-zi  (^arnuzi)  ,bringt  wohin,  setzt in  Bewegung'  (j-nu-]  vgl.  oben  ai.  rnöti)\  Imper.  2.  Sg.  ar-nu-ut  (arnut) =  gr.  oovv-d-i,  Verbaln.  a-ar-nu-mar  (arnumar) ;
inwieweit  toch.  A  ar-,  B  er-  ,hervor bringen,  verursachen',  mit  sÄ-Kaus. ars-,  ers-  ds.,  nach  Meillet  (MSL.  19,  159)  hierher  gehören,  ist  unsicher ; sicher  fern  bleiben  AB  ar-,  är-  ,aufhören',  mit  s/:-Kaus.  ars-,  ärs-  .verlassen' (ungenau  Van  Windekens  Lexique  6,  22).
h.  Erweiterung  er-ed-  (c?-Präsens ?) :  s.  ered-  .zerfließen',  ai.  drdati, rddti    ,fließt   usw.',  auch    ,beunruhigt' ;    mit   dem   Kaus.    arddyati    ,macht
330  ^
fließen;    bedrängt,    quält,   tötet'    wäre  aisl.  erta  {*artjan)  ^aufstacheln^  an reizen,  necken'   gleichsetzbar,    doch   ist  Verknüpfung   mit   *ardi-   ,Spit2A Stachel'  (oben   S.  63)  mindestens  gleichwertig;    eine   zweisilbige  Form  i' ägaC^ovai'  ige^i^ovaiv  Hes.,  IxQaöog  , Erregung';
weiter   hierher   oder   zu   5.  er-   ai.   rddati   ,kratzt,    ritzt,   gräbt,   hackt^ vi-radati  , zertrennt,  eröffnet';
vielleicht  auch  apr.  redo  ,Furche'  (Persson  Beitr.  667).
c.  Erweiterung  er-edh-:  s.  oben  S.  327  ige-d-cj  usw.   u.  unten  S.  339
d,  Basis  erei-]  und  reis- :ri-}-rolo-s,  ri-ti-  ,Fließen'. Ai.  irya-  s.  oben  S.  327 ; ai.  rinätiy  rinvati  (drinvan)   ,läßt  fließen,  entlaufen,  entläßt',  rlyate    o-q.
rät  ins  Fließen,  löst  sich  auf,  rina-  ,in  Fluß  geraten,  fließend',  rlti-  ,Strom Lauf,  Strich;  Lauf  der  Dinge,  Art,  Weise'  (letztere  Bed.  auch  in  mir. rlan  ,wa7,  manner'),  rit-  ,entrinnend',  raya-  m.  ,Strömung,  Strom,  Lauf Eile,  Heftigkeit',  retas-  n.  ,Guß,  Strom,  Same',  renn-  m.  ,Staub'  (:  aruss, renh  ,Sandbank');  zum  w-Suffix  vgl.  unten  \a.t.  ilvus;
arm.  ari  ,stehe  auf!'  (Persson  Beitr.  769)  Zu  y-afnem,  S.  327;  ^^^^
gr.  lesb.  dgtvcüj  (*dQl-viüj)  ,setze  in  Bewegung,  errege,  reize  zum  Zorn'1* egig,    -löog  ,Streit'    (vielleicht   im   i   zu    unserer   Wurzelform,   falls  nicht i- besser  nach  Schwyzer  Gl.  12,  17  zu  igstdo)  , stütze,  stemme,  stoße,  drängeO^r* ark.   igivvsiv  ,zürnen'  aus  ^Egivvg  eig.  ,die  den  Mörder  verfolgende,  ztiivj nende  Seele  des  Ermordeten'  (??) ;  ''**S'
alb.    geg.   rite    , feucht,    naß',    eig.   ,*fließend'    (*ri
=== leaf 344 ===
nete  :  ai.    rindti,  8\&y,'h rinoti) ;  "^
lat.   oriorj    ongo   s.  oben;   rlvus   (*rei-uo-s)   ,Bach';    in    dem   abg.  rtvhUh ,Nebenbuhler'     entsprechender     Bedeutungswendung    rlvlnus    und    rivälU ,Nebenbuhler    in    der    Liebe'    (letztere   Form    Umbildung    nach    aequalis,' södälis),  eigentlich  ,Bachnachbar' ;
wahrscheinlich  hierher  irrltäre  ,erregen,  aufbringen,  erbittern',  jpron^flr«  n^^ ,hervorreizen,  durch  Reiz  hervorbringen,  anreizen,  anlocken',  (wohl  Intensiva zu  einem  *ir-ri-re) ;  '  -
ir.   rlan   ,Meer'   und    (vgl.  ai.  r'iti-)    ,Art,  Weise',   gall.    Renos   (*reinos)^4 ,Rhein'  (ob  auch  nach  Stokes  KZ.  37,  260  ir.  riasc  ,a  marsb',  rzm  ,schlechte8  j^ Wetter'??),  cymr.  rhidio  ,coire'  (:  ags.  rld^  ai.  riti-h),  air.  riathorj  cymr rhaiadr,  acymr.  reatir  ,Wasserfall'  {*riia-tro-)]
ags.  rid  m.  f.,  ride  f.  , Strom,  Bach',  as.  rxth  m.  ,torrens',  mnd.  ride  Vm_ ,Bach,  Wasserlauf',  nhd.  -reid{e)  in  Ortsnamen;  Dimin.  (^rtpulön)  ndd rille  ,Furche  nach  Regen wasser,  Rinne';  weiters  ags.  ä-rceman  ,erheben,  sich erheben',  mengl.  r^men^  engl,  roam  ,umherstreifen',  aisl.  reimudr  ,Umher- streifen',  reimir  ,Schlange',  par  er  reimt  ,da  ist  es  nicht  geheuer,  spukt, reima  ,infestare'  (Bed.  wie  abg.  rijati  ,stoßen').    Über  rinnan  s.  oben.
331
as.
Mit  germ.  s-Erweiterung:  got.  urreisan  ,auf stehen',  aisl.  risa^  ao-s. rtsan  ;Sich  erheben',  ahd.  risan,  mhd.  rlsen  ^steigen,  fallen';  ahd.  reisa ^Aufbruch,  Zug,  Kriegszug,  Reise',  ^ot^urraisjan  ,aufstehen  machen,  auf- richten, erwecken',  aisl.  reisa  ds.,  ags.  rceran  ,erheben,  aufrichten,  er- richten', ahd.  reren  ,fallen  machen,  herablaufen  machen,  vergießen';  ndd. reren  ,fallen',  mhd.  riselen  ,tropfen,  regnen',  nhd.  rieseln^  mhd.  risel  m. ^Regen',  aisl.  blöd-risa,  mhd.  bluotvise  ,blutbespritzt',  afries.  blödrisne  ,blutende Wunde';  aus  , fallen'  wird  ,gefallen'  in  ags.  (ge)rlsan  ,ziemen',  ahd.  garlsan ^zukommen,  geziemen'  (vgl.  die  s-Erw.  abg.  ristati),  mhd.  rkch,  hurtig, schnell'  (vgl.  abg.  riskanije)\
lit.  ry-tas  ,Morgen'  (,*Sonnenaufgang',  vgl.  got.  urreisan),  lett.  rietu, -6Ju,  -et  ,hervorbrechen,  aufgehen  (z.  B.  vom  Tag),  hervorströmen',  riete ,Milch  in  der  Mutterbrust'  (vgl.  formal  ai.  reta-)]
slav.  "^raia-  m.  ,Strömung'  ( :  oben  ai.  raya-h  m.  ,Strom,  Lauf)  in  abg. izrojh  ,Samenerguß',  s^rojh  ,Zusammenfluß',  naroj  , Andrang',  roj  ,Bienen- schwarm'  (*roto-s);  dazu  reka  (*roi-ka)  ,Fluß';  slav.  *reiö  ,stoße'  in  aksl. rejqj  rejati  ,fließen'  (nslav.)  und  ,stoßen,  drängen'  (wie  dgirco  ,bewege'); dazu  ablautendes  aksl.  vy
=== leaf 345 ===
nngti  ji^co^slv',  ririQtis^  ,ruere';  aruss.  rint  ,Sand- bank',  klr.  rin  ,Sand,  Flußgeröll'  (vgl.  ai.  renn-);  in  anderer  Bed.  (s.  oben zu  lat.  rlvlnus)  abg.  rbVhm  ,Nebenbuhler'  rhvenije  ,£Qig,  igd^sia^  6ech.  fevniti ,nacheifern',  poln.  rzewnic  ,bewegt  machen'.
Mit  s-Erw.  bsl.  *reistiö  in  abg.  ristq,  ristati  ,laufen',  riskanije  ,cur- sus',  lit.  raistas  (,Laufzeit'  =)  ,Brunstzeit',  lett.  rlests  ds.,  lit.  ristas ,schnell',  ri§ciä  Instr.  Sg.  ,im  Galopp'.
e.  Basis  ereu-]  er-nu-  ,Wettkampf',  or-uo-  ,eilig'.
Ai.  fnöti  (Perf.  ära  aber  idg. ^*öra),  arnavd--^  av.  ardnu-  s.  oben  S.  327;
ai.  drvan-,  drvant-  ,eilend,  Renner',  av.  aurva-,  aurvant-  ,schnell,  tapfer' ; vielleicht  av.  auruna-  ,wild,  grausam,  von  Tieren';  sehr  unsicher  ^\.  rü-rd- jhitzig,  vom  Fieber';
gr.  0Qvv(.u,  odgog  s.  oben;  altes  Kausativ  doovw  ,stürze  mich,  stürme los',  ävoQOVo)  ,springe  auf  (wohl  als  *oqov\<j]o}  zur  s-Erw.,  s.  unten);  vgl. Schwyzer  Gr.  Gr.  I  683;
lat.  ruö,  -ere  ,rennen,  eilen,  einherstürmen';
mir.  rüafhar  {*reu-tro-)  ,Ansturm',  cymr.  rhuthr  ds.,  air.  rü(a)e  ,Held' {*reu-io-)]  hierher  die  gall.-brit.  FIN  *Ai-vä,  engl.  Arroio,  frz.  Erve,  Auve (*fwä);  messap.  FIN  Arvö]
as.  aru,  ags.  earu  ,hurtig,  bereit,  flink',  aisl.  grr  ,rasch,  freigebig^ {*arioa-  =  av.  aui-va-]  hierher  als  ursprüngl.  ,freigebig'  vielleicht  auch got.  arwjö  ,unentgeltlich,  umsonst',  ags.  earwunga,  ahd.  ar{a)wün  ,gratis, frustra',  arod  ^kraftvoll,  flink';  ahd.  ernust  s.  S.  328.
332
f
ag'S.  reow  ,aufgeregt^   stürmisch,   wild,   rauh^,  got.  unmana-rlggics  ,wil(i grausam^  ,  -k;.
Erweiterung  reu-s-:
Ai.  rösatij  rusdti  ,ist  unwirsch^,  rusitd-,  rustd-  ,ergrimmt^;  ..^^
schwed.  rüsa  ,daherstürmen,  eileii'^,  mnd.  rüsen  ,rasen,  toben,  lärmen«  ^ rüsck  ,Rausch^,  aisl.  rosi  ,Sturmbö^,  raust  ,Stimme^,  aschwed.  ruska  ,her-  B vorstürmen,  eilen^;  ^^'
[aber  got.  raus  n.,  mit  gramm.  Wechsel  aisl.  reyrr  m.,  ahd.  röi^  ^Schilf.  - rohr^,  rörea  ,Röhre^  (^rauziön),  mit  Stammbetonung  (wie  got.)  schwed.  I. rysja^  ahd.  rüssa,  rüsa,  riusa  f.  ,Reuse^,  weitergebildet  mit  Ä-Suffix  a^s.  '■^- rysc  f.,  mhd.  rusch(e)  f.  ,Binse^,  bleiben  wohl  fern];  ^
lit.  ruosüs  ,geschäftig,  tätigt,  lett.  ruo§s  ds.,  lit.  rnoHü,  ruosiaü,  rimti ,besorgen^,  reflex.  ,sich  bemühen^;
slav.  "^ruchh  in  russ.  ruch  ,Unruhe,  Bewegung^,  rwcÄww^
=== leaf 346 ===
b  , fallen,  stürzen'      ^ poln.    dech.    ruch   ,Bewegung^,   ablaut.    öech.    rychiy    , baldig,    geschwind' dazu  Kausat.  slav.  *rusiti  ,umstürzen'  in  aksl.  razdruHti  ,zerstören',  russ. rusit^  ds.,  usw.
WP.  I  136  ff.,  Schwyzer  Gr.  Gr.  I  516  b,  694,  702,  719,  740,  749,  Traut- mann 240  f.,  242,  243,  246,  WH.  I  64  f.,  416  f.,  719,  II  222  f.
4.  er-  (er-f-,  QJ^-y^-)  ,Erde'.
Gr.  I'^ä  ,Erde',  e^a-^s  ,zur  Erde'  (vielleicht  davon  iqacjy  s.  unten  S.  336; mit  Zusarümendehnung  wohl  noXvrjQog'  ftoXvaQovQog,  nXovdLog  Hes.);  evegoi, s.  oben  S.  312;  ioeai-[,L€rQ7]'  yewi^sTQiav  Hes.;
germ.  *erpö  in  got.  airpa,  anord.  ^'ortf,  ahd.  (usw.)  erda  ,Erde';
germ.  *e?*ö  in  ahd.  ero  ,Erde';
uo-Erw.  in  anord.  ^'^rvi  (*erioan-)  ,Sand,  Sandbank',  und
cymr.  erw  f.  ,Feld',  PL  erwi,  erwydd,  corn.  erw,  ereu  ds.,  abret.  mbret. eruj  nbret.  ero  ,Furche'  (*erwi-);
vielleicht  arm.  erJcir  ,Erde'  (Pedersen  KZ.  38,  197),  wenn  für  *erg-  (idg. *e7'w-)  nach  erkin  ,Himmel'.
WP.  I  142,  Finzenhagen  Terminol.  6,  Schwyzer  Gr.  Gr.  I  424.
5.  er-,  ers-,  thematisch  (e)r-e-    ,locker,    undicht,    abstehend;    auseinander-
gehen, auftrennen'. Ai.  r^e  mit  Abi.,  Akk.  ,rait  Ausschluß  von,  ohne,  außer'  (Lok.  eines  Partiz. *rta-  ,abgetrennt,  abgesondert'),  nirrti-h  ,AufIösung,  Verwesung,  Verderben'; dr-ma-  PI.  ,Trümmer,  Ruinen',  armakd-  ,trümmerhaft'  oder  n.  ,Trümmer- stätte'  (Bedeutung  etwas  unsicher);  *^rd-  in  Irma-  ,Wunde';  themat.  *(e)r-e- in  virala-  ,auseinanderstehend,  undicht,  selten';
333
gr.  SQfiiiog,  att.  eorjixog  ;,einsam^;
ganz  unsicher  lat.  rärns  .locker,  nicht  dicht,  selten^  {*er9-rö-s),  eher glaublich  rete  ,Netz,  Garn'  (vgl.  unten  lit.  rMs,  lett.  reta);
lit.  yrii,  zrti  ,sich  auflösen,  trennen,  pairas  ,locker';  rZtis  m.  ,BastsieV (mit  unursprünglichem  Schleifton,  wie  oft  in  i-Stämmen),  lett.  reta,  rete .Narbe',  rem  rudzi  ,undicht  stehender  Roggen';  lit.  eftas  ,weit,  geräumig' (,*auseinanderstehend');  von  der  leichten  Basis  retas  ,dünn,  weitläufig, selten'  (von  der  themat.  Wurzelf.  *(e)r-e-,  wie  auch:)  resvq,s  ,selten,  dünn', paresvis  , spärlich';
aksl.  oriti  ,auflösen,  stürzen,  zerstören'  (Kaus.  '"^oreiö  ,mache  auseinander- gehen'), skr.  ohhriti  ,niederwerfen',  dech.  ohofiti  .zerstören',  russ.  razorüh  ds.
er-db- :
ai.  fdhak  ,besonders,  abgesondert',  ärdha-h  ,Teil,  Seite,  Hälfte',  ardhd- ,halb',  n.  ,Teil,  Hälfte';
lit.  ardaü,  -yti  ,trennen,  spalten'  (Kaus.,  wie  ksl.  oriti)-^  erdvas  ,weit,  ge- räumig', lett.  ärda
```


## [2026-09-05T20:32:00.535Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 347 348 349 350 351; do echo \"=== leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"' {print}' POK_01.txt; done",
 "description": "Print POK leaves 347-351"
}
```


### [2026-09-05T20:32:02.194Z] TOOL RESULT

```
=== leaf 347 ===
ws,  irdens  ,locker,  mürbe',  trds  ,locker,  bequem  (ge- räumig'), irditj  ifdindt  ,lockern,  trennen',  grzw,  grc?w,  ^rst  ,trennen'.
re-dh- :
aksl.  red^k^  ,selten'  (wohl  stoßtonig,  vgl.  cech.  Hdhy,  sloven.  reddkj trotz  serb.-kroat.  njedki,  ridki);
über  ered-  s.  oben  S.  329  f.,  über  ereu-  unter  besonderem  Artikel  unten S.  337.
Inwieweit  die  von  Persson  Beitr.  666,  773,  839  f.  als  Erweiterungen unseres  *er(9)-  betrachteten  Wurzeln  re-d-  ,scharren',  rei-,  reu-  ,auf reißen' ihr  wirklich  entstammen,  ist  fraglich;  die  bei  *er(a)-  besonders  ausgeprägte Bedeutung  des  lockern,  undichten,  auseinanderstehenden  lassen  sie  ganz vermissen  oder  wenigstens  nicht  als  herrschende  Bedeutung  erkennen.
WP.  I  142  f.,    Trautmann  12  f.
ereb-,  orob-,  rob-  ,bohren,  aushöhlen ;  spitzes  Werkzeug  dazu'  ?
hett.  irhs  ,Stricknadel'  (Reimwort  zu  virhs),  ifhulis  ,Pflöckchen,  Griffel'; lit.  ürhinti  ,mit  dem  Pfriemen  ein  Loch  machen',  ufbti  =  lett.  urbt .bohren',  urbulis  ,Pfriemen.  Griffel';  lit.  i^obti  ,aushöhlen'.  ruobtüvas ,Hohlmesser'.  lett.  ruobs  .Kerbe,  Einschnitt,  Falz,  Mangel,  Zwistigkeit'. Die  Ablautverhältnisse  sprechen  für  idg.  Alter  der  Sippe,  obwohl  die Heranziehung  von  gr.  ^Qßr]Xog  ,rundes  Schustermesser'  und  dgßvXr]  »starker^ den  ganzen  Fuß  bedeckender  Schuh'  (wenn  ursprünglich  ,ausgehöhlter Holzschuh')  ganz  fraglich  bleibt,  da  letztere  auch  auf  einem  Worte  für ,Schuh'  ganz  anderer  Herkunft  fußen  können.
WP.  I  146.
334
f
ereb(h)',  örob(hy  in  Worten  für  dunkelrötliche,  bräunliche  Farbtöne.
Gr.  ÖQCpvög   ^finster,   dunkel'   {^Qcpog  ,ein   dunkelgefärbter   Meerfisch'?), fürs  Verblassen   der   eigentlichen  Farbbedeutung  verweist  freilich  Rozwa- dowski   Eos  8,  99  f.    auf   russ.  rjabinövaja  noch  ^trübe;,  stürmische  Nacht' wie  hom.  dQcpvalr}  vv§-
mit  dissimilator.  Schwund  des  ersten  -r-  alb.-ligur.-kelt.-germ.  ehuro- ^Eberesche;  Eibe' :
in  alb.-geg.  her-sh-e  m.  ,Eibe'  {*ehur-isio-j  mit  kollekt.  Suffix),  ligur.  ON Ehurelianus   saltus,   gaüorom.  eburos   ,Eibe'   (in  vielen   ON  und  PN),  air. ibar    m.    ,E
=== leaf 348 ===
ibe',   auch   als    PN,    cjmr.    efiür  ,Bärenklau',   mhd.    eberboum    3 nhd.  Eber-esche]
aisl.  iarpi-  ,braun',  ahd.  er2:;/,fuscus'  (oft  in  FIN),  ags.  eorp  ,dunkelfarbig, schwärzlich';  davon  aisl.  iarpi  , Haselhuhn'  und  ndd.  erpel  ,Enterich'  (im Gegensatz  zum  helleren  Weibchen) ;  mit  Vollstufe  der  2.  Silbe  ahd.  repa-^ reba-huon,  schwed.  rapp-höna  ,Rebhuhn'  <  mnd.  raphön :
lett.   irbe   in    meza    irbe   , Haselhuhn',  lauka-ifbe  ,Feldhuhn'   (s.  darüber Mühlenbach-Endzelin,  Lett.-D.  Wb.  I  708  f. :   kaum  slav.  Lehnwort  wie  lit.    ^ ierbe  erube,  jerubl,  jerubl^  , Haselhuhn',  vgl.  klr.  jarubic) ;
slav.  mit  Nasalierung:  mbg.  jer^bh,  r.-ksl.  jafabh,  *jerabh,  skr.  järeb usw.  , Rebhuhn',  von  der  Farbe  benannt,  wie  klr.  ordbyna,  orobynd,  sloven. jerebikaj  cech.  jefdb  usw.  , Vogelbeere';  ohne  anlaut.  Vokal  russ.  rjaböj ,scheckig'  (vgl.  oben  rjabinövaja  noch,  abg.  r^bi,,  russ.  rjdbka  ,Rebhuhn', rjabina  ,Vogelbeerbaum',  rjdbcik  ,Haselhuhn',  usw.).
Ob  hierher  auch  spätanord.  raf  n.  ,Bernstein',  aisl.  refr  ,Fuchs'  als ,der  rote'?    Aber  wohl  hierher  aisl.  arfr  ,Ochs'  usw.  als   ,der  rotbraune'.
Vgl.  Specht  Dekl.  115 f.,  der  von  einer  Farbwurzel  er-  ausgeht;  s.  auch rei-,  reu-b-  , buntgestreift' ;  zum  b  :  bh  s.  Specht  261  f.
WP.  I  146,  Jokl  Symb.  gramm.  Rozwadowski  II  242  f.,  Trautmann  104  f.
ered-  ,(zer)  fließen,  Feuchtigkeit'.
Ai.  drdati,  rddti  , fließt  (in  Kompositis),  zerstiebt,  löst  sich  auf;  beun- ruhigt, arddyati  ,macht  fließen,  löst  auf,  bedrängt,  quält,  tötet',  ärdrd- , feucht,  naß',  fdü'  (in  Kompositis)  , Feuchtigkeit',  av.  arddvi-  f.  Name eines  mythischen  Flusses,  meist  als  weibliche  Gottheit  gedacht.
Ob  dazu  gr.  liQda  ,Schmutz',  ägöaXog  ,schmutzig'?
Vielleicht  hierher  der  häufige  kelto-ligur.  FIN  Rodanos  (frz.  Rhone  == nhd.  der  Rotten j  ital.  Rodano  usw.)  als  ,der  fließende'  (gräzis.  ^Hgidavog aus  iberisiert.  *Errodanos),  dazu  die  Rednitz  (Bayern)  aus  *Rodantia.
WP.  I  148,   Pokorny  Mel.  Boisacq  II  193  ff.
335
eregai.h)0',  erog^{h)o'  ,Erbse,  Hülsenfrucht^
Gr.  b'goßog  m.  (aus  ^eooßog  nach  dem  Gen.  usw.  doößov);  vgl.  aber ^V.  Schulze  Kl.  Sehr. 
=== leaf 349 ===
 81),  egeßLvd-og  m.  (das  kleinasiat.  Suffix  erweist nicht  gerade  solche  Herkunft,  da  in  Pflanzennamen  auch  sonst  vorkommend, so  in  Ußivd-oi'  iqsßivd^oi  Hes.)  ,Kichererbse^ ;
lat.  ervum  n.  ,eine  Hülsenfrucht^  (aus  *eroiwm,  '^eregu(h)om  oder *erogi^{h)om)]
ahd.  araweiz,  ariciz,  nhd.  Erhse,  as.  er(iw)it,  rand.  erwete,  ndd.  erwten PL,  anord.  ertr  f.  PL  (Dat.  ertrum)  ds.  (-ait  wohl  bloßes  Suffix);
aber  mir.  orbaind  ,grains^  steht  für  ^ärbainn,  älter  arbanna  (oben  S.  63).
Wahrscheinlich  Entlehnungen  aus  einer  gemeinsamen,  wohl  ostmedi- terranen Quelle,  aus  der  auch  ai.  aravindam  , Lotosblume'  stammt.
WP.  I  145,  WH.  I  41 9 f.,. 863.
j.  erek'  (er[e]g-i2-)  ,Laus,  Milbe^  oft  tabuierend  entstellt.
Ai.  lik^ä  ,Nisse,  Lausei'  (wohl  aus  *laksd  durch  Einfluß  von  likhdti ,ritzt') ;
lat.  ricinus  1.  ,ein  sich  in  die  Haut  von  Schafen,  Hunden  oder  Rind- vieh einbohrendes  Ungeziefer,  Zecke'  (unsicher  ist  die  Zugehörigkeit  von 2.  ,eine  Strauchart,  Ricinus  communis')  kann  auf  älteres  *recinos  zurück- gehen und  mit  lit.  erke  , Zecke,  Schaflaus'  (*erkia),  lett.  erce  , Kuhmilbe, böse  Person'  unter  idg.  *erek-  zusammengehören.  Weiterhin  ist  zu  ver- gleichen arm.  o{r)jil  ,Nisse,  Lausei'  (hier  scheint  eine  Wurzelvariante er{e)gh-  vorzuliegen,  wie  auch  in  der  folgenden  alb.  Form)  und  orJciun ,ringworm,  itching,  erysipelas'  (aus  *orqiiöno-  (?)  mit  einem  -rzo-Suffix  wie im  Lat.  nach  Petersson  KZ.  47,  263  f.),  alb.  ergjiz  ,kleine  Laus'  (s.  ü.  Meyer Alb.  Wb.  96;  Zweifel  bei  Hermann  KZ.  41,  48;  doch  kann  der  abweichende Guttural  im  Armen,   und  Alban.   auf   tabuierender   Entstellung    beruhen).
WP.  I  145,  n  344.
2.  er(e)k',  rek-,  rok-  ,auf reißen,  spalten,  schinden'.
Ai.  rknd-h  ,geschunden,  kahlgerieben',  r^sdh  ,kahl',  rksara-h  ,Spitze, Dorn';
lit.  j-erkä,  pra-j-erkä  ,Schlitz';  (über  lett.  ercis  ,Wacholder'  usw.  s.  oben S.  67  f.) ;  mit  anderer  Ablautstufe  lit.  ranküj  räkti  ,aufstochern',  rakUis , Splitter,  Dorn',  usw.
Persson  Beitr.  839.   Dazu  .gehört  auch :
I.  eres-  , stechen'.
Ai.  rsdti  ,stößt,  sticht',  rHk  ,Speer',  av.  arUi-  ds. ; lit.  ersketis  , Dornpflanze',  vgl.  oben  S.  67 ; sloven.  r^sdk  ,Gänsedistel'. Persson  Beitr.  84.   Verschieden  davon  ist:
336
f
2,  ere-S'  (ers-,  ^s-,  e^es-),  und  r€s-,  rös-  ,fließen ;  rosa  ^Feuchtigkeit Tau';  von  lebhafter  Bewegung  überhaupt,  auch  ^umherirren'  und  ,auf- geb rächt,  aufgeregt  sein';  e^esiä  ,Übel wollen'  (S.  337).
1.  Ai.  rdsa-h  _,Saft,  Flüssigkeit',  o^asä  , Feuchtigkeit,  Naß',  auch  mythischer Flußname  gleich  av.  Ranhä  (d.  i.  Eahä),  daraus  der  Name  der  Wolga  ^pg.
lat.  rös,  röris  ,Tau'  (kons.  St.  mit  ursprünglich  bloß  nominativischer Dehnstufe  ö);
alb.  reshj  reshen  ,es  schneit',  auch  ,regnet  Asche,  Feuer'  (wohl  
=== leaf 350 ===
ebenfalls aus  *rös-)]
gr.  dTt-sQcca)  (*er9so)  ,gieße  eine  Flüssigkeit,  speie  weg'  (?),  i^-egdo)  ,schütte aus,  speie  aus',  %ar-eQda)  ,gieße  hinein',  ^sT-egdü)  ,gieße  um^,  Gwaoato  ,gieße zusammen';  nach  Dehrunner  IF.  48,  282  wäre  die  Grundbed.  von  ^Qdut ,auf  die  Erde  ausschütten'  und  das  Verh  von  eqa  ,Erde'  (oben  S.  332) abgeleitet ;
aksl.  rosa  ,Tau',  lit.  rasa  ds.
2.  Wurzelform  ers-,  rs-]  rsen  , männlich'.
ai.  drsati  ,fließt';  ferner  mit  der  Bed.  ,männlich'  (aus  ,benetzend,  Samen ergießend')  ai.  fsa-JÄa-Ä  , Stier',  aja-rsahhd-h  , Ziegenbock',  av.  apers.  arsan ,Mann,  Männchen',  gr.  hom.  ^qotjv,  att.  ^qqtjv,  ion.  äol.  kret.  eqotjV  (ohne J^- !)  , männlich'  (dazu  "^aQvrjJ^ög,  hom.  dgreiög  , Widder'  =  att.  äovecjg,  äol. dQvrjadsQ  f.,  dazu  dQvsvo)  , mache  einen  Luftsprung,  tauche',  eigentlich  ,mache einen  Bocksprung',  dcQvevTrjQ  ,wer  einen  Purzelbaum  schlägt,  einen  Luft- sprung macht',  Lit.  bei  Boisacq  u.  dqvsiög  und  dQve.vTTjQ  Nachtr.),  wohl auch  ahd.  or[re]huonj  anord.  oo^re  ,Auerhahn'  (daraus  durch  Kreuzung  mit ahd.  ür,  ürohso  das  mhd.  ürhan,  nhd.  Äuerhahn).
3.  Zugehörigkeit  unserer  Wz.  *eres-  zu  *er-,  '*or-  ,in  Bewegung  setzen, lebhafte  Bewegung'  ist  erwägenswert.  Andere  s-Formen  von  Wz.  er-,  or- zeigen weitere  Bedeutungen:
x\rm.  eram  (*ersä-iö ;  vgl.  oben  ai.  arsati)  , siede,  walle ;  bin  in  unruhiger Bewegung;  wimmle;  bin  leidenschaftlich  erregt;  bin  oder  werde  eifrig, zornig',  erandn  , Wallen  usw. ;  Erreg'ung',  z-efam  , bewege  mich  umher, bin  stark  bewegt,  erregt,  schwimme  usw.';
gr.  äq(x)ri  , Schwung,  Andrang'  {*rösä'j  davon  aber  auch  igcoeo)  ,fließe, ströme,  eile');
lat.  rörärii  ,leicht  bewaffnete  Plänklertruppe'  (Ableitung  von  *rösä , Schwung'  =  ßeXecjv,  dovQÖg  igcoi^)',
anord.  ras  f.  ,Lauf',  mndd.  ras  n.  ,heftige  Strömung',  ags.  rces  m.  ,Lauf, Anfall'  (engl,  race  skand.  Lw.),  mhd.  rasen  , rasen',  ags.  rcesan  ,anstürmen', anord.  rasa  ,einherstürzen';  anord.  ras  n.  ,Eile',  rasa  , stürzen,  gleiten' (Ablaut  *rös-  ;  *res-  :  *r9s-  ?) ;    got.  res  im  PN  Res-mer ;
337
dazu  mit  dem  Begriffe  teils  der  unruhigen,  auch  ziellosen  Beweguno- teils der  Aufgeregtheit,  des  gewalttätigen  Zornes:  *"
einerseits:  lat.  errö  (*ersä{ö)  ,irre'  (=  arm.  eram),  got.  airzeis  ,irre verführt^,  ahd.  irri  ,irreS  got.  airzipa  f.  ,Irrtum,  Betrugt,  ahd.  irrida  ds.'
irr(e)ön  (*erziön)  girren']
anderseits:  as.  irri  ,zornig',  ags.  eorre,  yrre  ^zornig,  erbittert^  eot^sian, iersian  , übelwollen',
4
=== leaf 351 ===
.  e^'es-  in  ai.  irasydti  ,zürnt,  will  übel^  benimmt  sich  gewalttätig'  (*,res-), irasyä-  ,das  Übel\7ollen'  und  irsyati  ,\si  neidisch^  (V-^s-);  av.  Partiz. ai^syant-  .neidisch',  ai.  Irsyä-  ,Neid,  Eifersucht'  av.  aras-ka-  ,Neid',  mpers. npers.  arask  ,Neid,  Eifer',  tief  stufig  av.  drdsi-  ,Neid';  ved.  fsi-  m.  , Dichter Seher'  (*Rasender);
arm.  her  ,Zorn,  Neid,  Hader';
gr.  ^(Qog '  dKovGLOv  ßUßog  Hes.,  hom.  ägsLi}  ,Schmähwort'  (==  ai.  irasyä), dazu  ^TT^^fim, gewalttätige,  feindselige  Handlung'  (urgr.  ö,  vgl.  ark.  iTtrjQsiä^sv, mit  Dehnung  im  Kompositum  auf  Grund  eines  *in;-äQrjg),  vgl.  auch  igsa- XTjXeiü  ,treibe  Neckerei';  ^!^Qrjg  ,Gott  der  Rache'  scheint  Personifizierung des  verwandten  Subst.  dgi^  ,yerderben,  Gewalttat',  wovon  ägruisvog  ,be- troffen,  versehrt,  gequält';
lit.  arsiis  , heftig';
hitt.  arsaniya-  ,beneiden,  eifersüchtig  sein',  Denom.  von  *arsana-  ,eifer- süchtig'  (vgl.  oben  ai.  irsyä  ,Neid'),  Benveniste  BSL.  33,  139;
nach  Pedersen  REtlE.  3,  18  hierher  toch.  A  är§al  ,giftiges  Gewürm', B  arsäklai  , Schlange'  {^rsätla)-^
zu  ai.  drsati  ,fließt'  (oben  S.  336)  stellt  Couvreur  JJ  96  hitt.  a-ar-a§-zi {arszi)  ,fließt';
toch.  A  yär-s-,  B  yar-s-  ,baden'  (-s-  aus  -sk-),  ohne  sÄ:-Suffix  A  yär-  ds., wird  mit  hitt.  arra-  , waschen'  verglichen  (?).
WP.  I  149  ff.,   WH.  I  416  f.,  863,    Trautmann  237.
I.  ereu'  , nachsuchen,  forschen,  fragen'.
Gr.  *£Qev(xif  *£Qvi.isv,  thematisch  geworden  :  i^f  [J^]w,  igel/lofiat,  (äol.  igsvw) und  el'gofxaL  (gjo/o/fai)  , frage,  suche',  kret.  igevTal  fyTTjial,  Ttgav.Togeg^j .auf  Grund  eines  en-St.:  "^egef-wv  ,Frager,  Sucher',  igsvvdo)  ,spüre,  forsche nach'  und  hom.  igssivü)  , forsche,  frage'  {^sgsJ^ev-io)),  endlich  auf  Grund eines  *egJ^-ü)g:  igcordco  hom.  eigwTdiü  ,frage';  hom.  igslonsv  ist  nach  Risch (briefl.)  künstliche  Analogiebildung;
anord.  raun  f.  , Versuch,  Probe,  Untersuchung',  reyna  ,prüfen,  erfahren'.
WP.  II  356,  Schwyzer  Gr.  Gr.  I  680.
22
i
338  ,
2.  ereu'  , aufreißend
Ai.  drus'  n.  , Wunde';
anor d.  ervj  err  n.  ,Narbe'  {*arwaZj  "^arwiz),  als  finn.  Lw.  arpi,  Gen.  ar}^^ mnd.  arey  nhd.  dial.  arhe  ,Narbe';  ,'
s.  auch  unter  2.  reu-  ,aufreißen^,  das  wohl  dazugehört. WP.  II  352,  Holthausen  Altwestn.  Wb.  355.
```


## [2026-09-05T20:33:30.459Z] AGENT

Now let me check the local reference books. First, Bartholomae, MacKenzie, Horn, Hübschmann for the Iranian nodes.


## [2026-09-05T20:33:32.618Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT arshan\"; grep -n \"aršan\\|arshan\\|arsan-\\|ar[sš]an\" BRT.txt | head -40",
 "description": "Grep Bartholomae for aršan"
}
```


### [2026-09-05T20:33:32.664Z] TOOL RESULT

```
### BRT arshan
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
6580:änkar?  Y.  2j.  1;  —  yava  alte  a»Afm  Anhang  zu  Z,  3.  3)  mit  Dat.  a)  'da- (3p,)'*>  F.4e(?); — kadä yavä  hvS  anhat  sein,  vorhanden,  bestimmt  sein,  gelten  für r7.."wann  wird  der  einmal  sein,  der,."  Jemand,  ihm  zu  teil  werden';  B)  im  Awr.r Y.25.9;  J/.  16;  —  Xit^V.  yimahe xsa'^re . .  Amfi">  bloa  mävayacit  ca%7V3rS  arsana »Sit  aot3in  änha  . .  "unter  K's  Herrschaft  "es  sind  auch  für  mich  vier  Männer  da"  V. gab  es  nicht  Kälte.. "V.5. 5;  5.  a,b)  vT-  iS.ii-*N.2Qy,^yaliiyasca  iJi  ä(s±)yji^ ip>m  S  a/imät  yat  alte  narS  '^var»ßva  altbyS  3  ar^kfn  Y.^g.i;  — garS  timJtipm otiA^n  "so  lang  als  die  Männer  im  ■  Var  '"n?rpyö  asti  a/ävaoyS  "das  Paradies  ist  für sind"  V.2.  28.  Z)    mit  Gen.  'sein  der  die    Gläubigen    (bestimmt)"  Yt.j.4;  Vyt.
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
6991:dt'a:  /rasa  frayäi  (sd.)  vahi^jm  ä  ahUm ä  V.  J|V,  29;  —  avi  Um  spayat ..  UmS  äca va^ö  dia  acisUm  Sca  aküm  <J  V,_^.55*>;  — bufvm  ä  ¥.4^.  ß)  'bei,  an,  auP:  iatär^m ä  angrö  (sA)  vs  ,  .  Y,44-i2;  —  dasttum J  vs  gaonavats  (sd.)  N.  ffj;  —  yäka särim^a^''  varsanqm  (sd.)  iarämi  Yt.  5. 77.  b)  zeitlich,  a)  'in,  bei':  tä  yüioyai^S J  rapi'iwifum  ervänam  "die  beiden  kämpf- ten in  der  Mittagszeit"  Yt.ÄaS;  Y.5.11; —  kävanJm  ä  ratüm  Y.g.\;  —  ai  a ^waAmäi  ä^rl  rätqm  n>ma»ia  ..manyai Y. 4.3. 9; —  ä paitiMnitlm  N. 2 (?).  ß)  'bis zu  -'  (nurKompA.;  s.  axlüirjm).  c)  'nach, gemäss':  var^m^a  (s.  *vära-)  Yt.j.iso,  i-].  2, *Y.  10.  \\.  2)  mit  Lok.;  'in,  auf,  a)  auf
7231:3h-  fraiä  fi-ayäi  (sd.)  vahi^fm  ä  akUm a  V.  iS.ig;  —  avi  /pm  spayat ..  e>m3  äea vaisB  ii'a  aastim  äca  ahuin  ä  V,_J.35";  — burum  ö  F.  4  a.  ß)  'bei,  an,  auf:  kalärSm ä  arigrS  {s,A.)  Vil  ..  \.  44.12;  —  dattnsm ä  vä  gaonavats  (sd)  N.  Ö5;  —  ya%a sanm'a^^  varsanqm  (sd.)  barämt  Yt.  5. , 77.  b)  zeitlich,  a)  'in,  bei':  ta  yaiiyaärS S  rapi>win?m  zrvämm  "die  beiden  kämpf- ' ten  in  der  MitUgszeit"  Yt.ÄaS;  Y.9.11; —  häi'anTiii  3  ratüm  Y.  p.  i ;  —  at  3' ^waAmäi  äire  rätam  mmaiihS  ..manysi\ Y.  4J.  9 ;  —  3  paiti-bsTfitlm  N.  2  (?).  ß)  'bis  ! zu  —'  (nurKompA.;  s.  3xtairTm).  c)  'nach,  j gemäss';  vamn^a  (s. ^vära-)  YL 5.1 30,  77. 2,  \ ''Y.  /o.  14.  2)  mit  Lok.;  'in,  auTj  a)  anf
8501:Pu,!  j^arsand.   —   ')  Das  Wort  könnte  nach Pü.  aus  Vyt  46  stammen;  s.  »«j/a.
8515:Zum  V.  Pfli-,  —  Pü.  (dRn.):  J<a  x'anand:^, j^ariand  Im,  j^arsaniilJi.  —  ')  s  nach  S  JJ-  I (statt  s).
10711:j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
10819:Komp.:  xsayri;\-arsan;  eig,  'der  atsan- ('Hengst,  Held')  unter  den  Herrschern';  vgl. ai.  räjariatha-  m.  Anders  FoV  KZ.  J7.  544, wo  weitere  Litt.  —  >)  Zum  Stammansatz  nnd znei.  s.  S  3lt.  I  b.  2/j.  2,  —  »)  Verunglückte CS.-Bildune.  i  fehlerhaft  fSr  h  der  ZDMG. $4.  [27  gezogene  Schluss  scheint  mir  höchst fraglich.  —  i)  Sollte  GS.  sein.
11725:yacif  !a%'wärS  arsana;  tl  mqm.^vinrunte V.iS.^if.;  —  vaifomtam  ^apaMarlaym (sd.)  jainii  .  .;  äat  tä  (APf)  .  .  hazü >tivat7zaym  daiva;  aal  tl  (als  APm.)  .  . ahutiS  vairyS  . .  *samar)guza  avazai  Yt  ig. So£;  —  p>n%w5  .  .  aiwica  tl  (als  AP.) \r3fSva  (sd.)  V.  2.  30;    —    . .  /ravasayS,
12415:•  j.  daenav-  f.  'femina',  von  (vierftissigen) Tieren  (im  Gegensatz  zu  arsan-,  uxsan- und  varsnqy-),  in  Verbindung  mit  dem Tiernamen":   ka'iwa   'nu  (IS.)   ,  ,  gava
14865:bieter*:  mii:nm..%wä  '//(IS.)  zf  hax^r?m (sd.)  dai&e  vahiit>tR  v>ri%rayn»mca  Yt. /O.80; —  uiti  *asti^afyS  Shüiril uili  aluSr gafys(%A.^  'tis  uiti  ..  YV15.28.  a)sonst mitGen. obj.;  itmirtea  s^ihraÄe  'tfm..jiim ahurim  mazdqm  Y.  2. 16;  —  ka%a  msi  . . 'tih  (NS.)"'  sahyat  xsa%raAyj  .  .  aslsUs (sd.)  Y.  44-  9-  o)  insbes.  mit  GS.  rfAy (Sp.  684  m.);  sao^antS  dSng  'ßi/  spmia dama  Y.  45.  11.  2)  'Gatte,  maritus': jahikayäi  ys  aom  pu^nm  baraiti  anyah- mai  arsanäi  varUim  ''5(r(DS.)'>  upa.baraiti (sd.)  Yt.  J7.58;  —  haoms  tiscit  ya  kainlnB ..*''klmi^  rähm/alsd.)  baxsai/t  Y.().23; —  yH  f^rSi  vTdat  ''^yaSca'i^  västryalibyB (sd.)  atca  a^aäatne  Y.  53. 4.  [Y.  p.  z  7 : lies  vai^yä.paitii\
15820:Eig.  'bunte,  gefleckte  ('/arsant-  Adj.,  woiu IF.  5.  261)  Rinder  habend';  ai.  pfiani-  Adj., vg\.  Pl-IOilah'a-  Adj.;  Bthl.  KZ.  29.  563.  — yg\.  parlav-.  —  ')  Zu  Yt  13.  127  hat  F  l fariaig';  S  263-  50.
16824:mit  upa  i)  'etwas  herzu-,  hinzubringen': barssmqn  upa.baraiti  N.  joj;  VytJ^;  — "hrayqm  *kva  *taHi  (sd.)  upa.barS  ratu- fris  N.  70^;  —  hc^ra  taoxma  upa.bara pasvqmla  ..  V.  2.  25;  271*,  30,  33,  35  f.*, 38.  a)  mit  Dat.  der  Person:  jahikayai ya.  aom  pu%r?m  baraiti  anyahmai  arsanai varitftn  paike  upa.baraiti  ",  .  die  da  das Kind  gebiert,  das  von  einem  fremden Manne  gezeugt  ist,  (und)  es  dem  Ehe- mann zubringif-  Vt  ly.  58.  a)  sva.  'ver- schaffen': upa  hg  gaotum  (sd.)  baraiti  V. 3.2$;  —  uj>aca  kl gatüm  baraypn  "und sie  sollen  ihr  ein  Lager  verschaffen"  V. 75.  43.         3)  'beilegen':  s.  Inf.
17612:VgL  /raäaxianä-  und  fradaxsanya-.  —  Pü.  (bei BlOCHKT  Lei.  107):  Aarsang  u  kafin')  "pierre de  ftonde'.    —    >)  Ob    richtig   beieagt?    —
18973:—  »)  Pü. !  änämiru  i5._,  «ber  Sü, :  namasirüh.  — J)  Pa.i  nyäyün  ^3kim  ökrmcad  hai  kasän  vam fia  »yäyim  ku  i^arsandih  i  pa  marlumän  pa an  iamän  ia  kör  u  katfai  hmind  tiyäyan pafirim.  Nicht  recht  deutlich.  —  1>  Wie  im Aiiid.    Es  ist  etwa  astu  oder  Ju^'ä/zueigäuzen.
19119:•  j.  *ni-Jatani  '*  Absol.'',  mit  asti  'er  schlägt nieder,  ein  auf  — '  {Akk.)^':  mqnay^n  ahe yäi;a  n3  safomüt..*'parsanam(&d.)m/°  hyst Yt.13.71.         [Yt5.77:  S-  Sp.  49^  u-]
19939:11;  —  'marsant-.         a)  von  rfamschen
19948:mit  fra  dnwS.A"':  s^äsaya  sT  vTspS anku! . ,  *jvaiti  a:fale  /ramiryeite  "durch Essen  lebt  die  ganze  Welt,  durch  Nicht- essen  verliert  sie  das  Leben"  ^■3-Zi- ai.  myläh;  vgl.  mriyäte;  v^.mTrad,  murda. — Pü.:  {/rd(\  murlan.  —  D  Statt  miiry-,  S  aSS. 40.  - —  =)  Im  Gegensatz  lu  rcü%;  para.riü%-; vgl.  Yt.  zj.  17  und  V.  S.  37f..  H.  3.  1,  16 und  19,  34.  So  im  A«.  überall  ansxer  in amarsanU.  —  3)  Hd*.  mairy'.  —  4)  So  K  30, M6.  —  5)  Hds.  yaouAa;  vgl.  S  afij.  30.  S. aber  Vyl.  63.  —  *)  Die  Hds.  haben  lu  FrW. S  zweimal  mtryäitt  (dessen  Schreibung  mit  f durch  die  spätere  Form  des  Worts  veranlasst ist)t  einmal  das  Ungetüme  miryaeiatüi  (oder •lalle),  nach  Dst.  ZA.  3.  8  'fulur  moyen'f!).
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
20094:mp.,  np.  man.  —  Pu. :  a^arsandihä  fa  an /röltiim  mars  äff  tslind;  Erl.  undeutlich.  — ■)  Wo  ei  wegen  der  anruhigen  Nachbuschaft Km  gefährlichsten  isl.
20904:—  aitenasävSyä  {aisii^ai.)  sps.i)r»taca..  y.i.$,  5.19;  —  aiqm  drujim  yqm  diisH- V.3.4;  —  aOe  yä  spujaiaca..  Y.y.3; — '^rqm  Yt./p.95;  '3-9' — pairikqm  yq$n ti yöi  ptiira  "iraitaünahe  F.^t;  —  upa  .  xnq'iatli  {s.A.)  Y.  ig.  $,  1.9;  —  vahislam ave  stärV  ydi  kaptd.iringa\t.i2.2Z.  t)a.-  tstim  .  .  yqm  asahe  vahiäaht  Vr.  2_j.  i; APf.:  tun  gax'ia  *amarsanli/  (sd.)  yti  Y.  57.33',  Yt  70. 33,  y.8sf.'^;  —  das aiahe  sauuAaitis  yt.1g.12;  —  yd..g<'i'iä  Relativ  steht  hinter  dem  attrib.  Adjektiv frasrävayat  ya  patua  ..  zara^ttjVra^  Y.  ■  dasSubstantiv  folgt:  vispqmiayqm  asaonS Sy.&;  —  paiti.pirpne  vispä  */anayö  y a  i  sttm  V1.16.1;  —  vTspqin  yqm  astiaifim drvaitisV.20.\o;  —  vfsp.isca  äpö  yä  ..  ar-\gai>qm  \t.ig.^^;  —  dämtm  ..yqm  är- matsti  Y.6tf.6;  —  fravafayd  yazamaide  maitim  spintam  Vr.  ig.  2.  a)  imqm yä  amisanqm  ipmtanqni  Y.26^,3;  Yt /_?.  damqm  yqm  äliüirim  YLÄ59;  —  azi 23— 26',  40.  a)  ta  ahmt  nmäne /am-  imqm  tanüm  yqm  masyänqm  V.20.3;  — yär?s  ya    aSaonqm  xsnütasca  .  .  Y.  ö'o.  a;  upa  tarn  cantqm  yqm  danyqm  Vt/'/.  77;
22048:KompE.  —  Zum  V.  'vaed-.  —  ai.  veda-  m. 'Besitz'.  —  Pü.:  vindiiit,  (zu  Y.  6S):  aySfiiin, (in  Y.  /o);  <i/ä«  ii^arsandih  ra/l  esitl;  s.  datlt Gdh.  GlrPh.  3.  48.  —  >)  Vor  yai  hat  man sich  wohl  nochmals  ya%a  ratvasUmaJuäl  zu denken.  —  =)  Vgl.  zSt.  Y.  46.   19  e.
23082:Ableit.  aus  *varsan-  m.  'mas';  aL  vfian-  m., np.  ffuian').  —  Vgl.  ivarina-  EN.  —  Pfi.: dnbdannh  na;  lies  dndannknp  •«  vai«  karp,
23109:Ü.  väitni,  uJmäsi;  uiän,  uiati.  —  Pfl.:  iämak, fa  iämai,  :^arsand  |*«/an),  pa  :farsandik, jflarsanJihi  (V.  S.  I^,  N.  6),  newaklk  (Y.  43.  l), pa  nrwaklh  (Y.  3g.  a).  —  ')  Gan*  abweichend Bn.  Stud.  7,  315.  —  =)  S.  dain  Bthl.  BB. 15.  13,  Dbr.  VglS.  a.  469.  —  J>  S.  auch  anter 5.  —  4)  Vollständig:  yahmäi  ttraohm  ga^JÖi (Inf.)  voll.  —  S>  Wörtl. :  'von  wem  woll(e( ihr,  dass  er  sein  Ger.  sei'.  —  b>  Man  kann auch  leicht  übeiall  einen  Inf.  ergänzen.
25994:ai.  ehadiyati,  ckandayaii  \  mp.  sahil  'videtor'  Sl ; pasand  'ßetällig'.  —  VgL  lEt.  YJL.  33,  \(>$, Hbm.  PSt.  41,  Ho»N  GlrPh.  /b.  956),  zKoiutr. des  Verbs  WILHELM  Mu«£od  /.  135.  —  Pü.: sahistan,  (lU  Vr.);  ifarsandik.  —  ')  Tbem. flektirt.  —  •)  NA,  Xadayäüy;  »gL  Bthl.  KZ. 2g.  585,  ZDMG.  46.  395.  —  4)  Die  von  Gnu. SPreussAW.  /JJ.  435  für  pair&mm  vorge- schlagene  Fasiang  halte  ich  für  uomÖgUclt. Maji  verlangte  dann  den  AbL !  —  5)  Zn  3  ■ und  5  mit  dem  "verkürzten'  Infinitiv  verbnndeD : Aam^asf,  väyit,  uzgn/t,  api  daSt,  ap€*darrU,  — ^)  Wo  mp. /äsandilan  (Gab.)  nachzutragen; auch  x'arsand  gehört  hierher. •  j.,  g.  'sand-  V.  'efficere,  perficere'. Praes.  2  sSndä—,  j-Aor.  1  sqs-.  —  Inf. sqsträi,  'sastrai,  satdyai.
26005:i^arsandik;  s.  'sand-.  —  ')  Pü.:  elen  man  räi säät  an  i  vch  västr.  —  J)  VgL  Vr.  /j".  1,  wo '^v^r^syafffmcä  iia  voAu  vajtrya.  ~~i)Pä.i  g^/(-
26316:8.  11,  14.  —  >)  S  399.  a.  —  »1  S  a/o.  8.  — Ü  Jedenfalls  in  singhaili,  Konj.;  s.  No.  9. — 4)  In  lahySi.  —  i)  Neben  a%akam  und  a%ah<^ sieht  %ääy  und  %äAy  (Konj.),  Wenn,  wie  ich annehme,  die  Nssslirung  in  a%ahaia  und a%ahi^  noch  hörbar  war,  so  hanniie  auch  in %Sliy  und  %ähy  nicht  wohl  gani  verloren  ge- wesen Eein.  Ich  vermute  die  Aussprache %a;  mit  Schleifton.  —  *>  iRed.  Tg!,  ai.  laiHa- läilt.  Nicht  gani  sicher;  %.  No.  8.  —  7)  S. roch  No.  13.  —  *)  S  303.  7.  Nicht  sicher; Pü.;  fehlt.  —  9)  Also  Praes.  1.  —  ■<>)  Also wohl  aas  ar.  *sansän\  doch  s.  No.  3.  — ">  Pü. :  undeutlich;  es  scheint  x'arsandiA {Sü. :  mmfofo^)  lu  entsprechen.  —  ■ ')  Mit Aktivendung;  s.  S  Szg  No.  und  No.  13.  — <))  Kannte  auch  als  Praes.  37  (Pass.).  -  0^ für  üA,  S  36S.  38,  30  -  genommen  werden. Die  Hds.  bieten  zumeist  saeAaili;  also  zu S  jy  No.;  s.  No.  12.  —  W\  Hds-  vaaAai,  aber unter  den  Wörtern  für  s-  und  mit  Pü.  guß.
29693:•  j.  hazanra-  neutr.  Zw.  'tausend':  hist^nti .  .  yazalänhs  iattmla  'rtmca  YL  Ö,  i ;  — yä  .  .  paica  vazinti  xsvai  tatäü  •rtm'a Yt  5.  95.  a)  mit  Gen.:  ydi^a  'nrn narqm  "Htm  nartm  arwyaxiaySit  Yt  /.  1 9 ; Ä  55,  io.  69,  128-131*,  Y.65.  4';— _yaäa na  satimca  "tfmca  baivanca  *parsanqm ''ni/abmlsd.)  Ayät \t  13.  JI -,3.31,  63,  120, Ä4S-5-3.  10,  JO.82,  A.J.7-11*,  V.J.31, 37',  /A'.  70-73»,  74'',  2/.  7,  22.3-4,*,  Y. 6S.1S,  N.42',  H./.s,sVar.,  10;  —  'rai (ab  Gen.)  bar>sna  vlranqm  YL  5.  96; £49;  —  'r»m  (statt  Instr.)  ha<ia.cikanqm (sd.)  V.4-ioi  —  y^ /"""i  fl^q^t  daei-a- nqm  'rai  'rB  pairi  Yt_j.  10  •';  4.  2  ",  Vyt ig'K  a)  mit attrib. Einerzahlen:  ioiitfa- rasca  a^a  garayB  . .  ca'^aiargsatfm{sd.)/a
```


## [2026-09-05T20:33:34.117Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD gusn\"; grep -n \"gušn\\|gusn\\|wašn\\|gwšn\" PHD.txt PHD_mackenzie.txt | head -30; echo \"### PHD rag\"; grep -n \"^rag\\|rag \\[\\|rag ,\\|rag '\" PHD.txt | head -20",
 "description": "Grep MacKenzie for gušn and rag"
}
```


### [2026-09-05T20:33:34.209Z] TOOL RESULT

```
### PHD gusn
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:2340:hungry gursag, gušnag.
PHD.txt:2708:male gušn, nar.
PHD.txt:5404:gušn
PHD.txt:5405:gušnag
PHD_mackenzie.txt:6815:holy abezag, pak, spenag, yoJdahr;             hungry gursag, gusnag.
PHD_mackenzie.txt:7020:long-lasting dagr-pattay.                male gusn, nar.
PHD_mackenzie.txt:10627:gusn                                    dusxwadaylh
### PHD rag
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
207:~ widardan: outstrip. andarag [adig] in, between, among. andarmāh [?ndim’h] new moon. andarón [?ndlwn! | M ?ndrwn, N —rün] inside, within, andarway [ndlw?d | (P ?ndrw'z)] air, atmosphere.
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
231:babrag [bplk'] beaver.
237:bahrag [P'hik'], (az) ап ~ ray: on that account.
296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
376:gabr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb. ~ih: hollowness. баё [gc | N ~] plaster, gypsum. -ёп [-yn!] (made of) plaster. gad [gt! = Av. gada-] club, mace. gādan, gày- [SL Y TWN-tn! < А V sry ?; g'tn! | N ~] copulate with. gadar [g??]] husband. gadwar [gtwl = Av. gaóawara-] bearing a club. 1gàh [gs | M ek, N ~] place, throne, bed. ?6àh [g’s | N ~] time; a fifth division of the day; = ģāhānbār. збаһ [gs] а Gatha, hymn. gah4n [g’s’n'] the Gathas; those scriptures dealing with spiritual and theological matters. ģāhānbār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker. ~ih: treasurership. gahl [г()А | N gal] sorghum, giant millet. gāhüg [p hwk'] bier. gāhwārag [g’swlk' | N gāhwāra] cot, cradle. ģāl [2° household, following.
380:gawazn [gw’sn' | N ~] deer. gawdar [0011 | N ~] calf. ģāw-dumb [g'bdwmb | N —dum] horn, trumpet. ģāw-mēš [TWR Amyš | N gā(w)mēš] buffalo. £áy-, v. ģādan. Gayómart [g”ywkmlt! = Av. gayó marata | (M gyhmwrd), N ~] the First Man. gaz [gc | N ~] tamarisk. gaz-, —išn, v. gazidan. gazag [gc’k'] biting. ģāzar [g'cl | N gázur] fuller, washerman. £azdum [gcdwm | N každum!] scorpion; astr. Scorpio. £azidag [ezytk! | N gazid] poll-tax. gazidan, gaz- [gc-, gz-ytn! | N ~] bite, sting. ~išn: biting. gëg [gdk' | M gyyg] thief. gēhān [gy)?>n! | = M, N gihān, jahān] world. ~ig [-yk'] worldly, mortal. -ģēn [-k(y)n! | M -gyn, N -gin] suffix forming adjectives of quality. gês [гуз | (M gyswg, N gēsū)] curls, locks. £étig [gytyk, gytydy | M gytyg, N géti] 1. the material world; 2. worldly. ~ig [-yk'] worldly. gil [ТУМА < A tym; gl | N ~] clay. gilag [g(y)lk! | N gila] complaint, lamentation. —-Obàr [wp] swallowing complaint, suffering in silence. ģilēn [T YN Ayn! | N gilin] (made of) clay. gilistag [g/ystk!] home, dwelling of demons. gir-, ~iSnig, v. griftan. gird [git! | M gyrd, N ~] round, circular; gathered. (9) — āmadan: gather, collect (intr.). — kardan: gather, collect (tr.). ~ih: roundness. girdag [gitk' | N ~a] disk, round. gisnag [gink' | P gyfng] short, small. ģišnīz [ginyc | N —] coriander. giyā(h) [gy^h, gy^h | (M gy'w), N ~] grass. ~izag [-yck'] a straw, blade of grass. gizistag [gcystk' | J w/Bzsth] accursed, hateful. gogird [оо | M gwgyrd, N ~] sulphur. ~ӧтапа [-’wmnd] sulphurous. gohr [gwhl | M gwhr, N gauhar] substance, essence, nature; jewel; stock, lineage. goóhrag [gwhlk'] = göhr. ~-danag [-d^m k!] physicist. 1g6hrig [gwhlyk'] natural, essential. *ģūhrīg [gw(’)hlyk'] equivalent, substitute, indemnity,
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
485:mérag [mylk'] young man, husband.
523:ūšmārag ['winIR! | N šumāra] calculation, reckoning.
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
```


## [2026-09-05T20:33:50.547Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- 23082 context ---\"; sed -n '23070,23090p' BRT.txt; echo; echo \"--- 10819 context ---\"; sed -n '10810,10825p' BRT.txt",
 "description": "Show Bartholomae context lines"
}
```


### [2026-09-05T20:33:50.619Z] TOOL RESULT

```
--- 23082 context ---
7ii(LS.)''  alSam  !yaöiiar\3m\cd\  acihöiris- faff((sd.)  N.2p.  [P.25:  lies  anm.vari-;
—  P,2^:  lies  Äi-flrÄ'.] KompE.   (».  auch  am'oriiaiiasbma-).   —   Zum V.  'var>i-,    —    got.   us-viautAli  'Jmaioaüvij'.  — Vgl.    *a'm.farSt>t    Inf.    —    Pu.:    varxün.     — ■>  Hds,  variita.
•  j.  varätar-  m.  'Zeuger,  Erzeuger',  mit Akk,  verb.:  puirMi  {sd.)   alm   nars  'ta
V./5.'3.
Zum  V.  ivarjs-.  —  Pü.;  fus  e  mart yat  vantl, er!,:  ha?  lö  äfusla»  em.
•  j.  varstva-  Adj.  'was  zu  tun  ist':  Au- matdibyascS ..  hvarsWibyaslä  ma%wBibyascä (sd.)  'tvSibyasls  ¥.77.17;  —  dalnayhsla matdayasnsi^  makwanqmla  (sd.)  . .  'tva- namca  Vr.  12.  3, '
PFP.  lum  V.  ^var3i:  —   Pü.:  /a  vanÜn.
•  j.  'varäna-  m.  Bezeichnung  </aA/iscber Geschöpfe:  aat  ahmi  nmäne zayätüe  daha- käca  mürakäca  (sd.)  pouru^ar^a  'nä/a Y.7/.6.
Et?  VIL  zum  ai.V.  ly-Wß',  aus  ar.  •8/7*«o-.')
—  Pu. :  ^fiur^ariai)  varzäär,  erl. ;  kär  u  dätastiH vas  fräi  glrtl  niakii  fa  Jrazäm  af?  nt  htiüt.
—  ')  Verfehlt  Gdk.  KZ.  3/.  588,  JN.  Reader 37.  Der  Te»t,  auf  den  Gdn,  antpielt,  be- ginnt mit  varilnahe  and  ist  eine  Formel  zun Töten  von  Schlangen  {apailäk  i  mär  iatan ;  so Cod.  Zend.  Mon.  66,  fol.4b)>  Aber  var^Sna- bedentet  dach  nicht  "Schlange',  tondem  ist EN.     Vgl.  ivanhta-  Mo.   I.
•  j.  ^araäna-  Adj.  'mUnnlich,  masculus': cvai  . .  ?  yä^a  -nahe  hhrpahe  ä3ul  (sd.) N.  106.
Ableit.  aus  *varsan-  m.  'mas';  aL  vfian-  m., np.  ffuian').  —  Vgl.  ivarina-  EN.  —  Pfi.: dnbdannh  na;  lies  dndannknp  •«  vai«  karp,
—  >)  Worin  *^ian-,  'uflnai-  and  'fifina- zusammengefallen  sind.
•  j.  JvarSna-  n.  EN.  zweier  Gläubiger: i)  'naie  afaenS  Yt.ij.  116.  2)  •  stütze hatihaurussis  asaonB  "des  V.,  Sohns  des H.  . ."  Yt  7j.  104;  —  -naAe  %wam  *ha>»- haurussis  jsmUspänahe  puiirahe  pt^nm "dich,  den  Sohnessohn  des  V.,  des  Sohns des  H.,  des  Nachkommen  des,/."  FrD.  7  ",
Vgl.  n-ar,I«a..  -  ai.  z^rna.  m.  EN.  -  ■)  Es ist  das  die  anter  'var/ina-  No.  erwähnte Formel.  In  der  Münchener  Hds.  lautet  sie: i-ar/inait  ^jvqrn  aifhi  aruittSU  JqmäsfaHoMe pa%rahe  faAritn  i^Uifni  amä  yim  davata (fol.  5)  dßf  afa%alö  failim  ä/vm  dtfnia  nvyq- itdi'i  hväiilS  HöU  i3naiti  nMt  ami  h-ttti  x'äiJ Sitte  yaza,  aä%3  änmi  tSyeile  yavaica  yavatläi- lai/a  aUm  vehu.  Die  Hds.  enthält  noch  einige andere  Formeln  von  gleichem  Kaliber.
ob,Google
1381  'varfnay-
•  j.  'varSnay-  m.  'Mäanchen  des  Schafs, Widder'  in  Verbindung  mit  dem  Namen fllr    Schaf":     maßahe    .  .  yat    •nBii    Yt.
'7-  56- KompA.  —  Vgl.  'varhtay-  EN.  —  ai.  vfstfäy- m.,  Xip.gvSan;  JF.p.  26I.—  S.  tach 'varthia: —  >)  S.  lu  'orian-  No.  3.
•  j.  *varänay-  m.  EN.  eines  Gläubigen: °nöi/  vsginsahe  asaona  "des  V.,  Sohns  des Väg.  ..'•  \t  13. 115.

--- 10819 context ---
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
```


## [2026-09-05T20:33:52.790Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ranha\\|ra\\hā\\|Ranhä\\|Ranhā\\|raiiha\\|ranh\" BRT.txt | head -20; echo \"=== rah ===\"; grep -n \"Ranh\" BRT.txt | head",
 "description": "Grep Bartholomae for Raŋhā"
}
```


### [2026-09-05T20:33:52.861Z] TOOL RESULT

```
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
3287:Pii.:  ia:  niiütifiä  xranh.
5294:Pü.:  aranh.
5486:Et.?i)  —  Pu.r  til,  (lu  \. 34.46):  ranh;  Sfi.: liaiiitiS,  (lu  Y.  46.  16):  dakfiaäpraijllih,  (lu Y.  34):  daifiriäääl'ä,  (lu  Y.  43):  ditä.  —  li  Gdn. hat  »eine  Etymologie  in  BB.  14.  21  anschei- nend aufgegeben,  vgl.  GlrPh.  1.  31,  wo  lu Y.  jo.  4  'wohlgesinnt'  übcrsetit  wird.
6105:•Ijm  vahiititn  sralihm  aiiuhm  sptnt^m Yl^.i8^  1.2,3',  14,  Y.;6.3,S.2.3,VyL42; —  "ÄJ  z'aAisia  'sa  srailla  dansama  %wä Y.öo.  13;  P-J5;  —  °-i5«  vahistitn  äinmca.. Y.  2.4;  J.4,  S. /.  7,  2,  7,  A.4,  2;  —  'sitnca vohiia  manö  Y.55.  5;  —  ahuräi  masdäi . .  'sai  vahUtäi  xla\räi  vairyäi  ärmatse V.ig.  11;  —  akunm  maidqm  . ,  vo/iu wiara  'ÄOT  vahi/t?m..G.5.S\^.l.i.i.,57- 34, 70. 1,  Vr.  II.  16,  Yt  /.  25,  FrW.  /.  i;  — ärmaitlm  , .  yehe  dähre  (sd.)  '^aheca  Vr. J9.2;  —  H5it  A3«  Jffr?, .  yS  ndtt  '/a  sBrÖ nsit  hau  taxmS . .  yS  ndit  *'la  taxms  P. 46.£;  —  tamaaha  °säi  usdatä  (sd.)  paitl Y. /3.  3;  —  ifanvaitU  °sake  virisS  Y, i6.  7.  a)  als  besonderer  Gegner  des Aima:'^  sp>ntö  mainyul alfym  frarfhari- cayat  vohuca  manS  °s»mca  vahist>m  .  . anrö  mainyui  asüm  franharxayat  aiamca mtnS  atsjmfmüa  . .  Yt  ig.  46;  —  vUfe  zT ante  *maoäaiS  (sd.)  oEsma  haSiäe . .  äat hs  yS  haotnahe  maus  °sa  hacaiU  urväs- mana  Y./o.S;  YtJ?.«;.  a)  aiahe  vaki-
6657:—  cDimS  . .  huxsa'iira  (sd.)  dagvä  aahari  der  kongruenten  Form  des  Adjektivs  er- Y.  44,20;  —  negirt:  västry3t  vä  . .  yl  scheint  das  Neutr.  im  Sing.;  A)llimAp.: vä  nSii  aahat  väslryl  Y.3i.<).  PPA.:  kär<^  ..hyt^  up3  mäm  äha'' haur  kamnam dr.'gvä  ..  duiazöbä  hqs  ..  ahsmustd (^.)\ .  (sd.)  ähc^  Bh.2  6.  B)im  Aw.(?J:  kl.. 46.  j^;  —  vTa rS  (sd.)  hqs  tat/rS  ..  mruylt  lylxmanyata  ap?r;nlyu  ahmt  n''it  p3r^ Y.4i$.  5;  47-4>  J'-Si  —  ^pö  mä  isttm  nJyu yesi  baväni pjrftiäyu(sd).\t.ip.^zQ)'> apayantä  (sd.)  6jr>xoqm  häitlm  vaahsus  —  aojistanam  asti  aojist>m  tan'istanqm manaiihs  Y._j2.9;  —  a~i:S  hat  vohü  tat  asti  tanHst^m  (näml.  mi^rS)  Yt,  10. !?äda  (sd.)  tvr^zyjtS^ä  ..Y. 3^. 6.  a)  ins-  1411?).  a)  Bei  pluralischem  Subjekt bes.  ein  Partizip;  seine  Verbindung  mit  der  kongruirt  die  Kopula  damit  oder  mit  dem Kopula  dient  zur  Umschreibung,  a)  PPA.,  Praedikat;  B)  im  Aw.:  *imqm  vav..yii PPM.,  PPfA.  und  PFP;  B)  im  Aw.:  auhtn  vSrii:raynyXt?m»m:a'..Y.Q.2T,  — at  *'hudSnao^  isayqs(sd.)  girszdl  kyJm  Y.  mana  zaya  asti  vahist?nt  V.  ig.^.  1)  ein 50,9;  —  al  v^  usiilmli/ ahz'J  (iDPiA.)3'i  Adverb.  A)  !  im  Ap. :  ^aia  mäm  hJma* zastäis  frtmmnä  Y.29.5;  —  vasa'ia  ahi  (sd,)  änJ"  Ti.G.a,.  B)  im  Aw.:  y.i^a Xfayamna  ..*d3ilim  Yt  ly.  15;  —  narim  ..  ka'^aia  K  3s  zaosS  mana  yal  akuraheYt. yl  anhat  . ,  mq'^rfm  pgr^sS  Y.Cf.t;  Yyt.  '9.82;  —  vJdylti^d^  saosy u ya'i:a  hn  asis S0(});  —  h^.'d' ioa  y:i:i7i'7  (sd.)  *asta  Y.   awA«/ V.4Ä9;    —    franhapi^    hvS   nSit
6732:*paraiihacäiti  .  .  'tu  *para»hacsili  "wenn
6878:in  Verbindung  mit  anderen  Gottheiten: yö  Sfvistö  "rB  mazdascä  ärmaitiscä  asfiiicä .  .  manascä  vohü  xid^nmcä  Y.33. 1 1 ; 28. 3.  5/.  3.  a)  Plur.  mazda  'rai^hö  'die MAA.s'  sva.  ^AhM.  und  die  andern  Göt- ter'"': yadä  af?m  z?vJm  (sd.)  atshin mazdäscä  'räf^Aö  (Nom.)  a^cä  armaiti Y.31. 4;  —  atcä  tffi  valm  Ayämä  (sd.)  yöi .  .  'dascä  "ranhö  (Vok.)  ä  *möyasträ.- baranä  (sd.)  asatä  Y.jo.  9.
7349:•  j.,  g.  iLmananha-'*  n.  i)  'Plan,  Absicht': mrüit!  (sd.)  yä  vS  xratSuS  xSmakahyü 'natahä  (NP.)  "was  die  Pläne  eures  Willens sind"  Y.  49.6.  2)  'Energie,  Ungestüm'; virikrayns  .  .  upa.kaxt3  '■nanha  (IS.)  Yt. /0. 7 1 ;  —  uitrahe  yö  arliiqm  ^franhir»- santqm  mazislftn  aoj3  ä-baraitt  maztshmca 'natjhim  Vt/^.ia'*.
7367:—  yaJ  hsi  äat  'tä  a/^U  hata  ahurö  . hranhfvim  (sd.)  Y.^y.i;  —  daidl  alfJ tarn  aüm  vaa/iSus  'di  manarfhs  "verleih, o  Aia,  den  Lohn,  die  Herrlichkeiten  des guten  Sinns"  \.■2K^^.  3)  'Almosen' (nur  Komp.).
7542:•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
8932:I  auf  das,  was  künftig  sein  oder  geschehen wird,  daher  sva.  'in  Aussicht  stellen,  ver- !  sprechen,  zusichern' J\  mit  Akk.  der  Sache und  Dat.  der  Person:  yi  mai/yil  yaoi akmiii  ascJt  (sd.)  vahUtä  .  .  vokli  cSisjm manauhä  Y,  46.  i8'>;  —  tarn  spmtil mainyü  mazdil  aJiuril  asiiunScii!s{2S^ih.) yä  ZI  i-ü-.i  vaAi/tä  "und  all  das  Beste,  d.os du  ja  durch  diesen  heiligen  Geist,  o  MAA., dem  ^Äranhänger  versprochen  hast:"  V. 47- Si  3'Z''  —  '^tM  ahniSi  ..  auAaiti (sd.)  yiim  (näml.  gam)  hsi  .  .  x/a^rrä 7'ohu!-ä  cöist  manatihs  yi.."..  Idas  Rind) das  er  durch  seinen  A7.  und  VAf.  ver- sprochen hat,.."  Y.5o.3;^_vJ  ää^a^dyS *}rjs.ratam  xsayas  am-ä  (sd.)  (istä (3SPrM.)s>  Y.^/.s!  a)  Hebendem  Obj. steht  ein  Inf,  dessen  Inhalt  a)  vom  Subj. des  Satzes  gilt;  cürd  mit  dam  *aküm.bis.- ratü}ii{?.i.)ciidi\.44.i6.  '  ß)  vom  Obj.: Ayat  höi  aSä  i'okucä  ^äUt  mananhä xlairöi  hei  haurviitl  am?riiata  ahmüi  stöi dqn  (sd.)  ".  .  da  er  durch  seinen  Am  und VM,  versprochen  hat  (promisit),  in  regno suo  salutem  immortalitatemque  nobts  esse (fore).."V.45.io.  3)'Jmdm.(Dat)  etwas (Akk.)  zuweisen,  zuerkennen,  zueignen': taibys  (sd.)  xsa:^r.m  vohü  (inas  (3SPrA.) maiiatihi  "wird  von  dir  her  VM.  das Reich  zuerkennen?"  Y.  44. 6 ;  —  huxsd^rS.- ^bä  at  xsainm  .  .  dad)maWä  M- mahicii  *hvanmnhm  Y.^5.5*';  SV-A"^',— huxsa>:ro.timliHt  at  xsai<r3m  cisyat  yat ahurili  mazdiii  A.  j-ö*"';  —  stüts  garii  .  . ahuräi  masäüi  .  .  dadjmahicii  ci/m/ihira iicil  vasdayamahl  Y.  41.  j*>;  —  ahuriii masi/äi  vtspä  vehS  Hiiahmi  Y,  12.  i; •o''-  4)  3S.  einasti  in  der  exegetischen
9228:masys  upäps  yd  ranhaya  .  .  var?ss.stava-  ,  j.  kahrka  indekl.,  den  Ruf  des  Hahns
10132:;  V.  ig.  41,  Yt  ig.  60';  —  n;imasj  « gaosp^nta^  tumas?  U *gaoAu}ia^^  ^>  V.  2A1, *V.34;  —  y!  . .  yazai  (sd.)  apa  . .  'iulcä västrät  acistsm  mantüm{sd.)  Y.^.  4;  — US  Sus  stuyl  täyäatcä  AazanAatcä  Y,  12. 2;  —  aipi.jatS {sd^  'am  Auhaf>A»m'>^  yai^a ra^aaiä  V.ij.^s; — yat .  .  Aainqm  ava- zSit  ..janyät*n»rSus  para  'am  asSitvar»- iqm  V.18.13;  F. 21;  —  xmmTm  'aus  yä canranhäxl  varaihlm  pantqm  azaite  Yt. 10.  38;  —  jvS  äp?m  jainli  Stram  fräva- yeiti  'am  *var)tqm  azaite  V.5.37;  —  al tsng  dngvä  ySng  alaAyä  vazdrfng  °ä  frU- ntffi/{sd.)  /JiiraAyä  .  .  Y.46.4;  —  nSii ..  karapanS  vSsträt  ar?ffi(sd.)  °avöi  äröis ä  *sfndä{sA.)..yi  Is' ilttgAs ..  Y.51.14;
10391:'  j  guSa-  m.  Name  einer  Abzweigung, ;ines  Seitenarmes  der  Ranhä:  Um  yazata .k3r?säsp5  upa  -Mm  apay:är>m  rankay^
11054:äuiySiryäca  Yt.  <?.  36;  —  haSnayäs^a  v5i- fnat^i  urva^aiibyai^a  Y.  öÄ  13; —  j/ao- öi-'il  akuräi  yesnyncs  Y.JO.  i ;  —  beim Zahlwort:  panc3(a  iäiwarMatjmca  A.  J.  7 (s.  dagegen  9;  Sp.  56?  m.);  —  %rayasca %risas(a  W.i.io.  a.)  mit  Traesis  beim zweiten  Glied:  nBnmca  yaval^a  tätte  Y. 62.6.  ß)  in  Verbindung  mit  XI  (sd.): . ,  yatamaiäl  vaahBsiä  It  vanuhTuä  U  Y. J^.  3.  b)  sie  sind  getrennt:  mä..»iq- >rascJ  güs/ä  sämascä  \.31.\Z;  —  yS  . . manasca  *gulta  sasnisea  YL  7^.87;  — moidascä  ahuranhJ  .  .  aulcä  '^.30.i)\  — ttsSatcS  .  .  vaahSuilä  manartkü  Y.  2Ä  i  o ; J4-  3;  —  vasasca  tB  . .  ustäca  xsaSsa  Y. S.  y,  —  a  3fai>yac.i ..  dari>/ai{sd.)M  ^.33. 7.  c)  eines  oder  beide  Glieder  sind relativisch  gegeben,  /a  steht  dann  beim ReL;  a)  das  zweite  Glied:  aAva  astvalascä AyaiiJ  manatihs  Y.sS.i;  —  fl/ift"o  atihSus yS  astvatS  yasca  asti  manahyS  Y.  57. 15.  p)    das    erste:     Ayatcil    dartgim
11801:•  j.  taozya-  Adj.,  wohl  Bezeichnung  eines Volks:  upa  aoialiu  ranhayä  .  .  ake  pait- yänm  fräkirtntal  atsrü  matnyuS zyqm'a . . 'yäca'^  daiiiAusuiiwisiära  (si.)  V.J.  19.
12701:•  j.  daÜhu-patay-')  m-  'Herr,  Gebieter einer  Provioz,  eines  Landes,  Landesherr'; i)  im  eig.  Sinn:  a!%rapatay3  .  .  *°tayS Aog.59;  —  va%ayanö  'paitts  V.  ig.  6 Yt.  15.  31;  —  yim  yazmte  "tayö  arjzahe ttva.jaspras  Yl  JO.  8;  —  ahurö  ^sästrfnqm •paiHl  Yt.  J^  37;  —  akuranhS  'tayS pu%ränhs  'paitinqm  Yt,  5. 8  5 ;  —  ä/rlitami tava  nara  ••paiti(VS.)Az.i;  A.i.8.  a)  mit Gen.  aus  ^Xyav,  daiAAav-.  nmanaAe  va KMätuspaitil  .  .  daijihfui  va  "paitis  Yt 10.18;  83,  l6.\%  VyL46';  —  dai^hsus yatffiM  Vr.J.  3,  V.  7.41,5.37;  —  daiMiuf •mVV.iO.S,  Y.y.  I,  Vyl-iö;  —  liairihSus 'tSe  Yt  /o.  17;  —  da/ryunam  'pattil (AP.)  Yt  /O.  18;  —  äaiAhyui  'painm*> nSirikqm  "die  Frau  ebes  Landesherrn" V.  7,  4a.  2)    von   Göttern;    a)    von
12725:Landes,  Landesherr*;  vanmm  yim  ca%ru.'\ gaosfm  . .  ake  paityänat  fräk»r>ntat  avrS ! mainyu!  araiiwyUca  daxsta  (sd.)  anair- yala  'Iura  (als  AP.)  ". .  und  nichtarische Herren  des  Landes"  V.  /.  17;  —  vpa aoia?su  ranhaya  .  .  ake  paityärim  frä- ifryrUat  anrS  mainyui  zyam'a  . .  taoiyäca (sd.)  'iura  V.l.  19. Komp.  mit  NS.  im  1.  Glied.  —  Pü.:  aitfr diAän  apar  mäminth,  (za  V.  r.  19)1  fehlt.
12792:Aus  dem  Zusammenhaug  gerissene  oder sonst  undeutlich:  Stellen:  ahmt  'im  paiti franhfn%at  V.  2.  j  PiiZ.;  —  yai,cit  'im dava  . .  T.^4'}  —  yaica  *'im  .  ,  Vyt.47i
=== rah ===
10391:'  j  guSa-  m.  Name  einer  Abzweigung, ;ines  Seitenarmes  der  Ranhä:  Um  yazata .k3r?säsp5  upa  -Mm  apay:är>m  rankay^
```


## [2026-09-05T20:34:10.524Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK wers ===\"; grep -n \"u̯ers-\\|vers-\\|uers-\\|ųers-\" POK_full.txt | head -20; echo; echo \"=== POK wrsen ===\"; grep -n \"ṛsen\\|rsen\\b\\|vṛṣan\\|vrsan\" POK_full.txt | head -20",
 "description": "Grep Pokorny for wers-"
}
```


### [2026-09-05T20:34:10.595Z] TOOL RESULT

```
=== POK wers ===
3721:compare also Sievers-Brunner Aengl. Gr. pp. 1 28, 2 under 288 f.) 
8267:4. extension {*h2auers-) uer-s-' rain, dew ': Old Indie varsa-n. " rain, rainy season, year 
8839:References: WP. I 849 f., WH. I 467, Feist 113 f., Sievers-Brunner 121, 243, Wackernagel- 
12701:variation in Old English, the form with -ku- assumes (Sievers-Brunner 200). 
16028:Petersson Heterokl. 18, Sievers-Brunner 167, Kluge''"' under siedeln. About Modern High 
23893:twaegen, f. twa, n. /J "two' (see above Sievers-Brunner264), Nom. Akk. PI. Old High 
28816:English ed-, Jacobsohn KZ. 49, 194, yet is Old English ed- after Sievers-Brunner 165'' only 
46462:Root / lemma: kert- kerat-, krat- {*kuers-t} 
46466:Root/ lemma: kert-, kerat-, krat- {* kuers-tj\ to turn, roll, wind, net, derived from the suffixed 
46468:with -t- formant of Root/ lemma: kures-, kuers-, kufs-\ wood, trees. 
49157:Root / lemma: kures- kuers- kujrs- 
92299:Root / lemma: uers- {*huer-) 
93481:Root / lemma: Ueren- {* hauers-en^ 

=== POK wrsen ===
1651:a//KC» (f.pl.) "grass' (Adams 9)] (differently Pedersen Tocharian 641). about gr. aGnp " an 
1722:References: WE. I 12, Devoto Mel. Pedersen 224. 
1827:References: WP. I 41. compare Petersen Aryan and Armenian Stud. 126. 
1906:References: WP. I 38 f., Pedersen Hittite 183. 
1973:etc., see Pedersen KG. II 451 following. Old Irish a//?" activity, play ' (from *agnis), gallo- 
2116:(with puzzling /about *atgr-, *atr-, see Pedersen KZ. 39, 352; thereof artaks^ out ', prefix 
2548:have derived from *-g"'hn-, not-*g"'n-, in spite of Pedersen KG. I ^09-bn-■, 
2890:References: Pedersen Groupement 20, Hittitisch 115, Tocharisch 227; Frisk Indo- 
3689:with it) compare above aRmen/mer-, Pedersen KZ. 32, 247, Johansson Beitr. 9, Petersson 
3897:References: WP. I 34 f., WH. I 60, 848, Feist 18 f., Pedersen Hittitisch 128, Tocharisch 
4038:Armenian a/aun/ " pigeon, dove ', barely for *a/abh-/7-(Bugge KZ. 32, 1, Pedersen KZ. 
4048:Osthoff IF. 8, 64 f., Pedersen aaO. 
4295:Thurneysen KZ. 43, 55 f.; Pedersen KG. II 195), ol-chen(a)e^ in addition, but ', actually " 
4363:Tocharian A alya-k^, B alye-k^'ahKoq i\q' ( *alle-k^, Pedersen Groupement 26, 
4432:Pedersen KG. I 137); Old Norse a/drm. (Gen. a/drs) "age, lifetime, old age'. Old English 
4639:Old pers. abismoxQ debatably meaning see Pedersen KZ. 40, 127, Bartholomae IF. 19, 
4705:References: WP. I 54 f., WH. I 36 f.. Feist 74 a, 88, Pedersen Tocharisch 82. 
4722:*misalka after Pedersen KG. I 73, where difficult suppositions about Irish smol, smolach 
4887:after neutr. -men-siem s. Pedersen KG. II 61; to the intersection with Latin animai. 
4891:Pedersen KG. I 170, II 111);
```


## [2026-09-05T20:34:12.643Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD 414 area ===\"; grep -n \"wšn\\|w'šn\\|wshn\" SOD.txt | head -20; echo \"=== SOD arask ===\"; grep -n \"'r'sk\\|rʾsk\\|r's-k\\|arask\" SOD.txt SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-05T20:34:12.718Z] TOOL RESULT

```
=== SOD 414 area ===
=== SOD arask ===
SOD.txt:16983:arsk    ©<Av.  araska;  MP  yrysk   ©nom.  -w 
SOD.txt:17327:ar(a)sk    Orsq)   ©Av.  araska;  Parth.  rask   ©ob. 
SOD_pages.txt:7863:      arsk ©<Av. araska; MP yrysk ©nom. -w
SOD_pages.txt:8028:     ar(a)sk Orsq) ©Av. araska; Parth. rask ©ob.
```


## [2026-09-05T20:34:20.304Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8260,8290p' POK_full.txt",
 "description": "Read Pokorny wer-s- rain section"
}
```


### [2026-09-05T20:34:20.360Z] TOOL RESULT

```
Old Church Slavic vbrjg, vbretr stream, bubble, surge, boil, cook ', virb' whirlpool ', izvorb 
" wellspring (bubbling water) ', wherefore with from " cook ' developed meaning " heat ', 
Latvian wersme " glow ', Old Church Slavic varb " heat '. 

About possible affiliation of *uer/e/na^ alder ' see there. 

4. extension {*h2auers-) uer-s-' rain, dew ': Old Indie varsa-n. " rain, rainy season, year 
' {varsat/" it is raining '), gr. oupov ' urine '; span, ttpor\ " dew ', Ionian Attic oupsu) " 
urinates ' (kausativ *uorseid, F- proved by the augmentation Eoupnoa), oupia " a water bird 



Middle Irish {*gwrass) /^5ss 'rain' is older fross {uros-ta, in spite of Pedersen KG. I 44); 
Hittite wa-ar-sa-as^ra\v\\l)seems an Old Indie loanword. 

Maybe alb. {*varsa-) vesa^6eW : {*heverse) sspari ' dew'. 

{* h2aursen-) ufsen-^ discharging semen = virile ', Old Indie vrsan- 'virile', m. ' manikin, 
man, stallion '. 

thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
"Aries, ram' (= Avestan varasni-6s.), vrsana-m. ' testicles '; 

Specht (Dekl. 156) places here (from Germanic *gwrai-njan-) without s^extension Old 
High German reineo^ stallion ', Old Saxon wrenioAs., Old English wraene^ horny, lustful '; 
Old High German wrenno^ stallion ' is back-borrowed from Middle Latin (under the 
influence of common Celtic -ns-, -nt- > -nn-). 

uerse/i-:\-aWv\ {*gverres) verres, -/is'boar', Lithuanian i/eAS/is'calf, Latvian versis^ox, 
rother, cattle'.
```


## [2026-09-05T20:34:21.984Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7855,7875p;8020,8040p' SOD_pages.txt; echo \"=== page tags near ===\"; awk 'NR>=7700 && NR<=8060 && /\\[pdf page/' SOD_pages.txt | tail -20",
 "description": "Show SOD arsk entries with page tags"
}
```


### [2026-09-05T20:34:23.504Z] TOOL RESULT

```
                                                                      SCE
                                                                        etc. 76; TSP 14.33; STii 7.29; BSTBL, Dhy. 48 &
1418 Vy'n B                                            h^^ii
     arhan ©< Skt. arhat
      Buddha's title                                            1430 VS'y p'k *± >r55>yp>kh
      Dhy. 358, BSTBL        :                                  1431 >r8>yp>kc B                                  tj^j.
1419 >r>sk S                                         jl^u^j          arSefakc ©f. adj. ^'r^y p'y
                                                                     radiant
      arsk ©<Av. araska; MP yrysk ©nom. -w
      envy                                                           TSP 9.37
         =>>rsk(>}
                                                                1432 Wy p»y B                                 /^„x-^
      Anc. Lett. 5.5                                                 arSefc OrS'ypy)

1420 >rcyc M                                         (yjj)^          splendid
     arziz ©MP }rzyz; Arm. arjij                                     TSP 6,15,74, 152 & etc.
     tin, lead
                                                                1433 Wyp'y pyyy       M        jUj>. J JL r0)^Uily^ Jx-
      Sogdica. 27.30
                                                                     orSefi Payi
1421 V8     B, S                            VL-T JL. <trtuo
      TSP 2.37, 3.10, 11, 12; Hen. Texts. 715; C2, 51V2
                                                                      righteous
         p97; Frag. Lcn. 48, 7                                        SCE 555; BSTBL; TSP; Frag. Lcn.; STii 8.8;
                                                                        Mack. BSTBL n p21; GMS 470 n 1
1473 Ysy =* 'rs'ny
                                                                1486 Vt'wspy =» Wwsp'y
1474 Vsq C =» >rskC))
1475 >rsk(,) M, B                          jl^<j£^              1487 Vt'wspy'h       M, B          £^ <o&U jl^j x^Ujl
     ar(a)sk Orsq) ©Av. araska; Parth. rask ©ob.
     envy                                                             artawaspya Ort'wspy'kh, 'rtwspyO
        -y ^'r^sk
                                                                      righteousness, Manicheaism, electi
      BBB f63; GMS 368, 526; TSP 2.1075; Sund.                        BBB; GMS 154, 470; Gersh. AHM 163;
        AoFviii 1981, 179.10a
                                                                       WwspfkK ICG 419
1476 Ysqny C                                             ^_^^   1488 'rt'wspy'kh S => Wwspy'h
     ar(a)skane                                                 1489 Wwxst rwc ^ Wwxwst rwc
     envious                                                    1490 VtNvxwst rwc M      :^ y^J)*\j> /j^ jjj Ojj^fc^j'
      STi 33.18; GMS         1056

1477 >rsx      C =* 'rs'ny                                            artawoxst, artuxst, artawoxust (Wxwst, Wwxst
=== page tags near ===
```


## [2026-09-05T20:34:35.350Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" SOD_pages.txt | head -5; echo \"---\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F'[][]' '{print $2}' | head -3; echo \"=== near arsk line 7863 ===\"; awk 'NR<=7863 && /\\[pdf page/ {l=$0; n=NR} END{print n\": \"l}' SOD_pages.txt; echo \"=== near 8028 ===\"; awk 'NR<=8028 && /\\[pdf page/ {l=$0; n=NR} END{print n\": \"l}' SOD_pages.txt",
 "description": "Find pdf page tags in SOD near arsk"
}
```


## [2026-09-05T20:34:37.005Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== male ===\"; grep -n \"^     w.n \\|w'šn\\|wšn \" SOD.txt | head; echo \"=== 'male' glosses ===\"; grep -n -w \"male\" SOD.txt | head -20; echo \"=== vein ===\"; grep -n -w \"vein\\|veins\" SOD.txt | head -20",
 "description": "Grep SOD for male and vein"
}
```


### [2026-09-05T20:34:37.102Z] TOOL RESULT

```
---
=== near arsk line 7863 ===
: 
=== near 8028 ===
:
```


### [2026-09-05T20:34:37.218Z] TOOL RESULT

```
=== male ===
=== 'male' glosses ===
25739:male  kid 
32152:male,  man 
50082:male 
50093:male  ass 
50100:male  eyes 
77245:male 
91540:male     3718,  6291,  10229 
91542:male  ass     6292 
91544:male  eyes     6293 
91546:male  kid     2739 
=== vein ===
64617:vein 
95081:vein     8425
```


## [2026-09-05T20:34:40.517Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== 32152 ==\"; sed -n '32140,32160p' SOD.txt; echo \"== 50075 ==\"; sed -n '50070,50105p' SOD.txt; echo \"== 64605 ==\"; sed -n '64605,64625p' SOD.txt; echo \"== 77235 ==\"; sed -n '77235,77250p' SOD.txt",
 "description": "Read SOD entries for male and vein"
}
```


### [2026-09-05T20:34:40.641Z] TOOL RESULT

```
== 32152 ==
two  hundred 
STii  1.82;  SCE  561;  BSTBL,  Padm.  45;  GMS  1316; 

SW,C2n  p51 

3717  dwystysywystmyq 
8wiste  se-wist-mik 
two  hundred  and  twenty-third 
C2,  1R9  n  p50.51 

3718  6x   S 
8ax  ?   ©<daha   ©prop.  n.  SxzHk 
male,  man 

S  W,  Rock.  Insc.  Indus  Valley  1989,  135;   CII, 
1992,  p51 

3719  8xs-   M  jjj^o^jO^j^^ 
8axs 

0o)give  pain,  (ro)hurt 
== 50075 ==

<*ni-drdma-Jca  ? 
scorpion 
SCE  118,  327;  TSP  3.85,  6.9;  GMS  A466 

6289  nyr8p())y  =>  nyr5p>k 

6290  nyrq    M  =>  nyrk(,) 

6291  nyrk(,)   B,  M  j 
nirk   (nyrq)  ©<*naryaka 

male 


JJ>- 


SCE  561;  TSP  2.383,  19.21;  GMS  183,  485,  536, 
976  n  1;  BBB  al2  b53;  Sund.  1994,  45.16 

6292  nyrk'yr   B 
nirk-  (a)  xar 
male  ass 

TSP  19.21  n  p232 

6293  nyrkcsmy   B  -      ?  j  ^  oj j^  tJX  ^ 
nirk/zirk-casme  ?  =^zyrkcsmy 

male  eyes 

Benv.  VJ  40d  n  p94;  "blue  eyes",  Szmerenyi. 

JAOS  1950,  230;  zyrkcsmy  "yellow  eyes" 

== 64605 ==
8423  r»Yh    B,  S  =*  r>y 

8424  r'YyCh)   B  >Sjj»<jM**^j 
raye   ©Khwar.  ryYy 

wild,  deserted 
SCE  39,  300 

8425  r>k   M  J 'j 
rak   ©<*rahaka\  Av.  rar]ha\  Parth.  rahg;  MP  rag 

©ob.  pi.  -tyy 
vein 
GMS  399;  Hen.  JRAS  1942,  232  n  6;  BSOAS  12, 

312.123;  11,  71.14;  Sogdica.  56,  37 

8426  rWnd   M  <ll^> 
ramand   (r*mn(d)t,  rWnt)  ^rWnty 

always 
== 77235 ==

10228  wsn   M  a^J 
w(i)san,  usan,  wisn  ?  ^ws'y-,  ws'n^y 
hungry 

GMS  386 

10229  wsn-   B  jiS \j 
wasn,w(i)sn   ©Av.  vardsna%  Skt.  vrsan 

male 

GMS  147;  TSP  19.2a,  wsny  'spy,  Hen.  Texts. 
7l3n  5 

10230  wsn'm   M  J^y,-.,...*,
```


## [2026-09-05T20:34:54.646Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['8425  r>k','10229  wsn-','1419  >r>sk','1475  >rsk(,)']:\n    i=t.find(pat)\n    if i<0: print(pat,'NOT FOUND'); continue\n    leaf=t.count('\\f',0,i)+1\n    print(pat,'-> leaf',leaf,'=> printed page approx',leaf-66)\nEOF",
 "description": "Compute SOD leaf/page numbers for entries"
}
```


### [2026-09-05T20:35:32.798Z] TOOL RESULT

```
8425  r>k -> leaf 1 => printed page approx -65
10229  wsn- -> leaf 1 => printed page approx -65
1419  >r>sk -> leaf 1 => printed page approx -65
1475  >rsk(,) -> leaf 1 => printed page approx -65
```


## [2026-09-05T20:35:36.982Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds:',t.count('\\f'))\nimport re\nfor pat in ['8425 r','10229 w','1419 >r>sk','1475 >rsk']:\n    i=t.find(pat)\n    print(pat, i, 'leaf', t.count('\\f',0,i)+1)\nEOF\ngrep -c \"\" SOD_pages.txt; grep -n \"page\\]\" SOD_pages.txt | head -3",
 "description": "Check SOD_pages structure"
}
```


### [2026-09-05T20:35:39.070Z] TOOL RESULT

```
formfeeds: 644
8425 r 2176059 leaf 407
10229 w 2586262 leaf 482
1419 >r>sk 619781 leaf 122
1475 >rsk 632284 leaf 124
45616
```


## [2026-09-05T20:35:44.991Z] TOOL CALL #22: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:35:44.998Z] TOOL RESULT

```


```


## [2026-09-05T20:35:49.618Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ers-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derived terms/descendants including any Indo-Iranian and Latin ones (errare?). Also note any alternative reconstructions or notes."
}
```


## [2026-09-05T20:35:50.721Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81r%CC%A5s%E1%B8%97n",
 "prompt": "Give the reconstruction, meaning, root it derives from, and descendants (Avestan, Old Persian, Sanskrit, Greek)."
}
```


### [2026-09-05T20:35:53.741Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:35:58.844Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁ers-

## Reconstructed Root
**\*h₁ers-**

## Meanings
1. "to flow"
2. "to roam, to err"

## Derived Terms and Descendants

**From \*h₁érs-ti ~ \*h₁r̥s-énti (athematic root present):**
- Proto-Anatolian: \*ʔérsti
  - Hittite: a-ar-aš-zi, ar-aš-zi
  - Luwian: a-ar-ši-ya-an-du
- Proto-Indo-Aryan: Vedic Sanskrit árṣati ("to flow")

**From \*h₁ers-o/h₂- ("erring, error"):**
- Proto-Armenian: Old Armenian եռամ (eṙam, "to boil")
- Proto-Italic: \*erzāō
  - Latin: errō ("to err")

**From \*h₁ers-yo-s:**
- Proto-Germanic: \*irzijaz

**Balto-Slavic (unsorted formations):**
- Lithuanian: aršùs ("violent, furious")
- Lithuanian: irsti ("to be angry")

## Alternative Reconstruction
A variant root **\*h₁reh₁s-** ("to rush") is proposed for "Ancient Greek ἐρωή (erōḗ), Proto-Germanic \*rēsō, and Latin rōrāriī."
```


## [2026-09-05T20:36:05.218Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/H%C5%99%CC%A5%C5%A1%C4%81",
 "prompt": "Any reconstruction page about *Hr̥šā or male/hero. If not found say so."
}
```


## [2026-09-05T20:36:06.342Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Xerxes",
 "prompt": "Give the full etymology of Xerxes: Old Persian form, its literal meaning and morphological analysis, Greek, and the New Persian descendant form."
}
```


### [2026-09-05T20:36:09.467Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:36:15.573Z] TOOL RESULT

```
# Etymology of Xerxes

**Old Persian Origin:**
The name derives from Old Persian "𐎧𐏁𐎹𐎠𐎼𐏁𐎠" (x-š-y-a-r-š-a /Xšayāršā/), which means "ruler among kings." This compound form combines elements denoting authority and kingship.

**Greek Transmission:**
Ancient Greek adopted this as "Ξέρξης" (Xérxēs), filtering the Persian name through Hellenic phonological patterns during the classical period.

**Modern Persian Descendant:**
Contemporary Persian preserves the name as "خشایارشا" (xašâyāršā) or the shortened form "خشایار" (xašâyâr), maintaining a recognizable connection to the original Old Persian etymon while reflecting Persian phonetic evolution.

**Related Form:**
The entry notes that Xerxes functions as "a doublet of Ahasuerus," indicating an alternative transmission route through Hebrew that produced the biblically-associated variant name.
```


## [2026-09-05T20:36:21.076Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DA%AF",
 "prompt": "Give the Persian entry for رگ (rag): meaning and full etymology (Middle Persian, Proto-Iranian, Avestan, Sogdian, any cited authorities like Hasandust or MacKenzie)."
}
```


## [2026-09-05T20:36:21.966Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B4%DA%A9",
 "prompt": "Give the Persian entry for رشک (rašk): meaning and full etymology (Middle Persian, Avestan araska, Proto-Iranian, cited sources)."
}
```


### [2026-09-05T20:36:26.809Z] TOOL RESULT

```
# Persian Entry for رگ (rag)

## Meaning
"Blood vessel; arteries, capillaries or veins."

## Etymology
The word derives from Middle Persian *lk'* (rag), tracing back through Proto-Iranian *HraháH* to Proto-Indo-Iranian *HrasáH*, ultimately from Proto-Indo-European *h₁rṓs*.

## Cited Cognates
The entry references comparative forms including Manichaean Middle Persian *rg* (/rag/), Khotanese *rrā-*, and Old Armenian *erak* (noted as an Iranian borrowing).

## Notable Limitation
The Wiktionary article does **not** include references to Avestan, Sogdian, Hasandust, or MacKenzie. These etymological resources are absent from the provided content, so detailed information on those authorities cannot be supplied from this source.
```


### [2026-09-05T20:36:29.215Z] TOOL RESULT

```
# Persian Entry for رشک (rašk)

## Meaning
The word has two etymologies:

1. **Etymology 1**: "Envy" (the emotion) or "envy" (the object of emotion). Synonyms include حسادت (hasâdat) and حسد (hasad).

2. **Etymology 2**: "Nit" (the parasitic insect egg).

## Full Etymology

**Etymology 1** traces back through Middle Persian (ʾlyšk' /arešk/, "envy") to Proto-Indo-Iranian *Harš- ("envy"). The source notes this may derive from Avestan araska- meaning "envy," ultimately stemming from Proto-Indo-European *h₁ers-. The entry indicates cognates with Sanskrit īrṣyati ("to envy") and Old English irsian ("to be angry").

**Etymology 2** relates to Sanskrit likṣā ("nit"), with possible connections to Latin ricinus in the "tick" sense, though "further connections are problematic," according to the documentation.

The entry includes a literary citation from Hafez (c. 1390) demonstrating the first meaning's usage in classical Persian poetry.
```


## [2026-09-05T20:36:41.001Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%B4%D9%86",
 "prompt": "Give the Persian entry for گشن (gušn/gošn): meanings and full etymology (Middle Persian, Avestan, Proto-Iranian, Proto-Indo-European, cognates)."
}
```


## [2026-09-05T20:36:41.748Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rhubarb",
 "prompt": "Give the full etymology of rhubarb: Latin, Greek, Rha/Volga, and any alternative accounts. Also give rheum if mentioned."
}
```


### [2026-09-05T20:36:47.143Z] TOOL RESULT

```
# Persian Entry: گشن (gošn/gušn)

## Meanings

The word functions as a noun, adjective, and verb:

**Noun:**
1. (obsolete) Male, man
2. Conception
3. Population
4. (obsolete) Stallion

**Adjective:**
1. (obsolete) Masculine, male
2. Fertile; relating to male sexuality, vitality, and potency

**Verb:**
1. (obsolete) Present stem of گشنیدن (gošnidan)

## Etymology

The source states: "Ultimately from Old Iranian *vršna-." The word shares linguistic roots with Classical Syriac ܐܘܫܢܐ, which represents an Iranian borrowing.

## Etymology Limitations

The provided Wiktionary entry does not include detailed etymological information tracing the word through Middle Persian, Avestan, Proto-Iranian, or Proto-Indo-European stages, nor does it list comprehensive cognates beyond the Syriac example. The etymology section only references the Old Iranian origin and one related term.
```


### [2026-09-05T20:36:49.500Z] TOOL RESULT

```
# Etymology of Rhubarb

## Primary Etymology Path

The word "rhubarb" entered English in the late 14c. from Old French *rubarbe* and Medieval Latin *reubarbarum*. The Latin term derived from Greek *rha barbaron*, literally meaning "foreign rhubarb."

**Greek components:**
- *Rha* = "rhubarb," possibly connected to Persian *rewend* ("rhubarb")
- *Barbaron* = "foreign" (from *barbaros*, root of "barbarian")

## The Volga Connection

The Greek *rha* may have been "associated in Greek with *Rha*, ancient Scythian name of the River Volga." Since rhubarb "was long imported into Europe by way of Russia," the plant became linked to that geographical region.

## Medieval Modifications

The first vowel was altered in Medieval Latin "by association with *rheum*." The *-h-* restoration was occasional in Middle English but only standardized by the late 18th century.

## Rheum (Related Term)

"Rheum" (late 14c.) refers to "watery fluid or humid matter in the eyes, nose, or mouth," derived from Latin *rheuma* and Greek *rheuma* ("discharge").
```


## [2026-09-05T20:37:01.736Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN gusan ===\"; grep -n \"gušan\\|gusan\\|gu.an .mas\\|Hengst\" HRN.txt | head -20",
 "description": "Grep Horn for gušan"
}
```


### [2026-09-05T20:37:01.849Z] TOOL RESULT

```
=== HRN gusan ===
8023:oss. t. Urs 'Hengst' (84).
8024:LW. mand. xr^nj;, syr. n:51^in 'Hengst* (Nöldeke,
```


## [2026-09-05T20:37:04.243Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT raevas/ranha headword ===\"; grep -n \"ra?vah\\|raSvas\\|raevas\\|raēvas\\|raivas\" BRT.txt | head -10; echo \"=== BRT Ranha headword entry ===\"; grep -n \"Ranha-\\|ranha-  f\\|ranhä-\" BRT.txt | head -10",
 "description": "Grep Bartholomae for raēvas and Raŋhā headword"
}
```


### [2026-09-05T20:37:04.329Z] TOOL RESULT

```
=== BRT raevas/ranha headword ===
7536:•  j.  'i-zäta-  Adj.  (fem.  Ha-)  'adeHg,  edel, vornehm':  °ta  F.  7;  —  kainins  . .  "tayi raevasci^raya  H.  2.9;  —  kainlnö  . .  rafvat ai^r^m  (sd.)  °taya  Yt5.64;  —  'tarn  hutao- sam  Yt9.i6.
24784:raevas^idra-
24790:•  j,  raevas-^idra-  Adj.  (fem.  'rä-)  'von reicher  Herkunft,  von  vornehmer  Abstam- mung': kainlnB..äsaiayh  'roj'J  H.2.9".
24792:•  j.  raevas'tama-  Adj.  'der  reichste': zarahustnm  .  .  hatqm  •tmm  Yt.  7J.  151; — yat  kiranaoiti  ärifaol  kavat.masd  (sd.) mand  yäha  -mahe'it  ".  .  wie  (den  Sinn) selbst  des  reichsten"  Y.  ;o,  13.  a)  mit ralm  als  Akk.  der  Beziehung:  zara^u/fr^m .  .  yal  as  .  .  racm  'mS  Yt.  ig.  79.
=== BRT Ranha headword entry ===
```


## [2026-09-05T20:37:16.884Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Wolga\\|Rha\\b\" BRT.txt | head -10; echo \"=== try ranhä- ===\"; grep -n \"ranhä\\|ranha-\\|rai>ha\\|ra>ha\" BRT.txt | head -10; echo \"=== index near line 24784 ===\"; sed -n '24780,24800p' BRT.txt | head -5",
 "description": "Grep Bartholomae for Raŋhā/Wolga"
}
```


### [2026-09-05T20:37:16.995Z] TOOL RESULT

```
=== try ranhä- ===
8932:I  auf  das,  was  künftig  sein  oder  geschehen wird,  daher  sva.  'in  Aussicht  stellen,  ver- !  sprechen,  zusichern' J\  mit  Akk.  der  Sache und  Dat.  der  Person:  yi  mai/yil  yaoi akmiii  ascJt  (sd.)  vahUtä  .  .  vokli  cSisjm manauhä  Y,  46.  i8'>;  —  tarn  spmtil mainyü  mazdil  aJiuril  asiiunScii!s{2S^ih.) yä  ZI  i-ü-.i  vaAi/tä  "und  all  das  Beste,  d.os du  ja  durch  diesen  heiligen  Geist,  o  MAA., dem  ^Äranhänger  versprochen  hast:"  V. 47- Si  3'Z''  —  '^tM  ahniSi  ..  auAaiti (sd.)  yiim  (näml.  gam)  hsi  .  .  x/a^rrä 7'ohu!-ä  cöist  manatihs  yi.."..  Idas  Rind) das  er  durch  seinen  A7.  und  VAf.  ver- sprochen hat,.."  Y.5o.3;^_vJ  ää^a^dyS *}rjs.ratam  xsayas  am-ä  (sd.)  (istä (3SPrM.)s>  Y.^/.s!  a)  Hebendem  Obj. steht  ein  Inf,  dessen  Inhalt  a)  vom  Subj. des  Satzes  gilt;  cürd  mit  dam  *aküm.bis.- ratü}ii{?.i.)ciidi\.44.i6.  '  ß)  vom  Obj.: Ayat  höi  aSä  i'okucä  ^äUt  mananhä xlairöi  hei  haurviitl  am?riiata  ahmüi  stöi dqn  (sd.)  ".  .  da  er  durch  seinen  Am  und VM,  versprochen  hat  (promisit),  in  regno suo  salutem  immortalitatemque  nobts  esse (fore).."V.45.io.  3)'Jmdm.(Dat)  etwas (Akk.)  zuweisen,  zuerkennen,  zueignen': taibys  (sd.)  xsa:^r.m  vohü  (inas  (3SPrA.) maiiatihi  "wird  von  dir  her  VM.  das Reich  zuerkennen?"  Y.  44. 6 ;  —  huxsd^rS.- ^bä  at  xsainm  .  .  dad)maWä  M- mahicii  *hvanmnhm  Y.^5.5*';  SV-A"^',— huxsa>:ro.timliHt  at  xsai<r3m  cisyat  yat ahurili  mazdiii  A.  j-ö*"';  —  stüts  garii  .  . ahuräi  masäüi  .  .  dadjmahicii  ci/m/ihira iicil  vasdayamahl  Y.  41.  j*>;  —  ahuriii masi/äi  vtspä  vehS  Hiiahmi  Y,  12.  i; •o''-  4)  3S.  einasti  in  der  exegetischen
10132:;  V.  ig.  41,  Yt  ig.  60';  —  n;imasj  « gaosp^nta^  tumas?  U *gaoAu}ia^^  ^>  V.  2A1, *V.34;  —  y!  . .  yazai  (sd.)  apa  . .  'iulcä västrät  acistsm  mantüm{sd.)  Y.^.  4;  — US  Sus  stuyl  täyäatcä  AazanAatcä  Y,  12. 2;  —  aipi.jatS {sd^  'am  Auhaf>A»m'>^  yai^a ra^aaiä  V.ij.^s; — yat .  .  Aainqm  ava- zSit  ..janyät*n»rSus  para  'am  asSitvar»- iqm  V.18.13;  F. 21;  —  xmmTm  'aus  yä canranhäxl  varaihlm  pantqm  azaite  Yt. 10.  38;  —  jvS  äp?m  jainli  Stram  fräva- yeiti  'am  *var)tqm  azaite  V.5.37;  —  al tsng  dngvä  ySng  alaAyä  vazdrfng  °ä  frU- ntffi/{sd.)  /JiiraAyä  .  .  Y.46.4;  —  nSii ..  karapanS  vSsträt  ar?ffi(sd.)  °avöi  äröis ä  *sfndä{sA.)..yi  Is' ilttgAs ..  Y.51.14;
15551:I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
18260:•  j.  {riranha-  n.  'Regsamkeit,  Munter- keit': kahmäi  . .  upav/tacayeni  (sA.)  'nhai haomanaahai^a  Yl  5.  8.
25191:•  j.  rava8-£arät-  Adj.  'was  sich  im  Freien, in  Freiheit  bewegf,  Bezeichnung  der  wildeti, nichtdomestizirten  Landtiere*';  a)  über- haupt; vjspqmia  gqm  .  .  'rütqm^a^A&tyl cat9ranhä&is{sA.)ca  Y.  7/.  9;  —  raiavS 'rata  (AP.)  Vr.  2. 1 ;  —  raiavS  •rätqm  (GP.) Vr.  /.  I ;  —  urutU!  . .  *rJtqm  Yt  13.  74;  — äätnqn  . .  yäca  'ran  (APn.)**  Yt  8. 48  **'.  b)  im  Gegensatz  2a  'den  in  den Bergen  hausenden'  die  der  Ebene:  auru-
25950:'ilranha-  m-,  Bed.?;  ob  zu  iilsr-'i
28851:*parat3hacaiti   '"/rsi^var}  (sd.)    ^paranha-
=== index near line 24784 ===
•  j.  rae'vant-  Adj.  'reich;  prächtig,  prunk- voll'; a)  von  a)  Menschen  und  ß)  Göttern: o)  virahe  ifhrpa  °vais  Yt  14,  a  7 ;  —  mos- yanqm  ..  'valqm  V.20.1;  Vyt,_57(?);  — naiüa  äV"  °va  maiya  (statt  NS.?)  JäiUi Yti4.36;  F.  77.  ß)  ahuräi  matdai..
'vaitl  i^arsnattuhaitj  (Stverz.)  Y. /2.  i ; usw.;  —  valmca  .  .  •vanhm  Yt  J5. 42;  — tistrJm  (Stverz.)  stänm  'vaiitpm  :^anna*3u- hant»m  YtÄ.  2;usw.;  —  salavaisS  °vä Haoma  betrauten  Unterpriesters  {ratav):\:^ar»narguha  YtÄ3a;  —  manh^m  gao- ^'rahe'^'>  (näml. -f  aiV/m)  yat  haom?mca\H%r?m  'vanttm  :i^  ar>ttamthant»m  Yt.7,  5;
dby  Google
m85
raevas^idra-
```


## [2026-09-05T20:37:19.074Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88%D8%A7%D8%B3",
 "prompt": "Give the Persian entry for ریواس (rivās): meaning and full etymology, including Middle Persian, Proto-Iranian, and any mention of راوند rāvand, Greek rha, or Arabic rībās."
}
```


### [2026-09-05T20:37:25.561Z] TOOL RESULT

```
# ریواس (Rhubarb) - Persian Entry

**Meaning:** The Persian word ریواس (rēwās / rivâs) denotes "rhubarb," with an alternative synonym چکری (čukrī).

**Etymology:** The term originates from Middle Persian rēbās, tracing further back to Proto-Iranian *(h)rabā́š ~ *(h)rabacáh. According to the source, it derives "from Middle Persian...ultimately from Proto-Iranian" roots.

**Related Terms:** The entry lists ریوند (rivand) as a connected word.

**Descendants:** The term spread across multiple languages through historical transmission:
- Arabic: رِيبَاس (rībās)
- Uyghur: راۋاچ (rawach)
- Uzbek: rovoch, rivoch, ravoch
- Kazakh: рауғаш (rawğaš)

The Wiktionary entry does not mention Greek "rha" or provide detailed discussion of راوند beyond listing it as a related term.
```


## [2026-09-05T20:37:36.616Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN rhubarb ===\"; grep -n -i \"rhubarb\" KLN_1966.txt | head -5; echo \"=== KLN rosemary ===\"; grep -n -i \"rosemary\" KLN_1966.txt | head -5; echo \"=== KLN race ===\"; grep -n \"^race\\|race, n\\.\" KLN_1966.txt | head -5; echo \"=== SKT rhubarb ===\"; grep -n -i \"rhubarb\" SKT.txt | head -3; echo \"=== SKT rosemary ===\"; grep -n -i \"rosemary\" SKT.txt | head -3",
 "description": "Grep Klein and Skeat for rhubarb, rosemary, race"
}
```


### [2026-09-05T20:37:36.721Z] TOOL RESULT

```
=== KLN rhubarb ===
12986:Derivative:  emmetrop-ic,  adj. emodin,  n.,  a  compound  obtained  from  rhubarb (chem.)  —  Formed  with  chem.  suff.  -in  fr.  ModL. (Rheum)  emodl,  ‘Turkey  rhubarb’,  lit.  ‘rhubarb of  the  Himalaya’,  fr.  Gk.  'HpuoSAi;,  ‘the  Hima¬ laya’.
32758:rhapontic,  n„  a  species  of  rhubarb.  —  ModL.  rha-
32759:ponticum,  fr.  MedL.  rha  Ponticum,  lit.  ‘Pontic rhubarb’.  The  first  element  stands  for  orig. rheum,  ‘rhubarb’,  fr.  Gk.  pijov,  fr.  Pers.  rewend, of  s.m. ;  the  alteration  of  rheum  into  rha  is  due to  a  confusion  with  Rha,  the  ancient  name  of the  river  Volga.  See  Rheum,  rhubarb.  For  the second  element  see  Pontic.
32780:Rheum,  n.,  a  genus  of  herbs  (bot.)  —  L.,  ‘rhubarb’, fr.  Gk.  prjov,  fr.  Pers.  rewend,  of  s.m.  See  rhu¬ barb  and  cp.  rhapontic.
32823:rhombus,  n.,  an  oblique-angled  equilateral  paral¬ lelogram.  —  L.  See  rhomb, rhoncial,  also  rhonchal,  adj.,  pertaining  to  arhon- chus.  See  next  word  and  adj.  suff.  -al. rhonchus,  n.,  a  whistling  sound  heard  on  the auscultation  of  the  chest.  —  L.,  ‘a  snoring’,  fr. Gk.  poy-/_o;,  which  is  rel.  to  (56yxo;,  friyyoq, ply xo;,  of  s.m.  plyysiv,  peyxEtv,  ‘to  snore’; prob.  of  imitative  origin, rhotacism,  n.,  mispronunciation  of  the  letter  r.  — ModL.  rhotacismus,  fr.  Gk.  ptoTaxiopoc,  fr. pwraxlqEiv.  See  next  word  and  -ism. rhotacize,  intr.  v.,  to  mispronounce  the  letter  r. — Gk.  ptoTaxi^Eiv,  ‘to  use  the  letter  r  excessive¬ ly’,  fr.  p<7>,  name  of  the  letter  r.  See  rho  and  -ize. rhubarb,  n.,  a  garden  plant  with  large  leaves  and edible  leaf  stalks.  —  ME.  rubarbe,  fr.  MF.  reu- barbe,  rubarbe  (F.  rhubarbe),  fr.  ML.  rheubar- barum.  The  first  element  in  ML.  rheubarbarum derives  fr.  L.  rheum,  fr.  Gk.  ptjov,  ultimately  fr. Pers.  rewend,  ‘rhubarb’  (whence  also  Russ. reven).  Cp.  the  ML.  form  rhabarbarum,  which comes  fr.  Gk.  pec  fSxppapov,  lit. ‘foreign  rhubarb’ ; px,  ‘rhubarb’,  is  a  blend  of  pvjov,  ‘rhubarb’,  with 'Pa,  the  Scythian  name  of  the  Volga;  see  roric. The  second  word  in  pa  |3xp!3xpov  refers  to  the foreign  origin  of  the  plant.  It.  rabarbaro  (whence G.  Rhabarber)  derives  fr.  Gk.  pa  |3dpj3xpov.  Cp. rhapontic,  rheum.
=== KLN rosemary ===
23539:mere,  n.,  1)  the  sea;  2)  a  lake  (archaic  or  dial.)  — ME.  mere,  fr.  OE.  mere,  ‘sea,  lake’,  rel.  to  ON. marr,  OS.  meri,  ‘sea’,  Du.  meer,  ‘lake’,  OHG. mari,  meri,  MHG.  trier,  G.  Meer,  ‘sea’,  Goth. marei,  ‘sea’,  mari-saiws  ‘lake’,  and  cogn.  with L.  mare,  ‘sea’,  OSlav.  morje,  ‘sea’,  Lith.  mares, ‘sea,  Baltic  Sea’,  OIr.  muir  (fr.  OCeltic  *mori), Co.,  W.  mor,  ‘sea’,  Gaul.  Are-morici,  ‘people living  near  the  sea’.  Cp.  mare,  ‘sea’,  maremma, marine,  marram  grass,  marsh,  moor,  ‘waste ground’,  morass,  the  first  element  in  meerkat, meerschaum,  Merlin,  mermaid,  merman,  Muriel, the  second  element  in  cormorant,  Pomeranian, rosemary,  and  the  last  element  in  beche-de-mer.
33079:romeite,  also  romeine,  n.,  antimonate  of  calcium (mineral.)  —  F.  romeine,  named  after  the  French mineralogist  and  crystallographer  Jean-Baptis- te-Louis  Rome  de  l’Isle  (1736-90).  For  the  end¬ ing  see  subst.  suff.  -ite,  resp.  -ine. romerillo,  n.,  any  of  several  American  aromatic plants.  —  Sp.,  dimin.  of  romero,  ‘rosemary’,  fr. L.  ros  maris,  ‘rosemary’.  See  rosemary. Romeward,  adj.,  tending  toward  Rome  or  Roman Catholicism.  —  Formed  fr.  Rome  with  adj. suff.  -ward.
33106:roric,  adj.,  pertaining  to  dew.  —  Formed  with suff.  -ic  fr.  L.  ros,  gen.  roris,  ‘dew’,  which  is  cogn. with  Lith.  rasa,  OSlav.  rosa,  ‘dew’,  Ol.  rasah, ‘sap,  juice,  fluid,  essence’,  rasa,  ‘moisture’,  Rasa, name  of  a  mythic  river  (=  Avestic  Rahha), aryati,  ‘flows',  rsabhdh,  ‘bull,  steer’,  Avestic  and OPers.  arshan,  ‘man’,  Hitt,  arszi,  ‘flows’,  Gk. Sp  ary,  jipp  tjv.  ‘male,  masculine’,  prob.  also  'Pa, Scythian  name  of  the  Volga,  fr.  I.-E.  base  *ras-, *eras-,  *eres-,  *ers-,  ‘to  flow,  wet,  moisten’.  Cp. rasa,  romerillo,  rosemary,  rosolio,  rouse,  ‘to pickle'.  Cp.  also  the  first  element  in  rhubarb  and the  second  element  in  Ahasuerus  and  in  Xerxes, rorqual,  n.,  any  whale  of  the  genus  of  large  whales, the  Balaenoptera.  —  F.,  fr.  Norw.  reyrhval,  fr. ON.  reydarhvalr,  fr.  reydr,  ‘rorqual’  (fr.  raudr, ‘red"),  and  hvalr,  ‘whale’.  See  red  and  whale. Rosa,  1)  fern.  PN.;  2)  a  genus  of  plants,  the  rose (bot.)  —  L.  rosa,  ‘rose’.  See  rose.
33127:rosemary,  n.  —  ME.,  fr.  earlier  rosmarine,  fr.  L. ros  marinus  (whence  also  F.  romarin),  ‘rose¬ mary’,  lit.  ‘dew  of  the  sea',  fr.  ros,  ‘dew",  and marinus,  ‘pertaining  to  the  sea’,  fr.  mare,  gen. maris,  ‘sea’.  See  roric  and  marine,  adj.  The  loss of  the  -n-  in  English  is  due  to  a  confusion  of  L. marinus  with  E.  Mary.  Cp.  romerillo.
40676:Ulex,  n.,  a  genus  of  plants,  the  furze  (hot.)  —  L. ulex,  ‘a  shrub  resembling  rosemary’,  contracted fr.  *uvilex,  and  rel.  to  uligo,  ‘moisture’.  See  uli¬ ginose.
=== KLN race ===
16612:tuitatem,  acc.  of  gratuitas,  ‘free  gift’,  fr.  L. grdtuitus.  See  prec.  word  and  -ity. gratulate,  tr.  v.,  to  congratulate.  —  L.  gratulatus, pp.  of  gratuldri,'  to  manifest  joy,  congratulate’, contracted  fr.  *grati-tulari,  ‘to  bring  something agreeable’,  compounded  of  grdtus,  ‘pleasing, agreeable’,  and  tulo  =  fero,  ‘I  bring’.  See  grace, n.,  and  tolerate  and  cp.  congratulate.  Cp.  also L.  opitulor,  ‘I  help,  aid,  assist’,  lit.  ‘I  bring  help’, fr.  ops,  gen.  opis,  ‘help,  assistance’,  and  tulo  — fero,  ‘I  bring’.  —  For  the  contraction  of  *grati- tulor  into  grdtulor  see  haplology. gratulation,  n.,  congratulation.  —  L.  gratulatio, gen.  -onis,  ‘manifestation  of  joy,  congratula¬ tion’.  fr.  gratulatus,  pp.  of  grdtulari.  See  prec. word  and  -ion.
23166:Maud,  fem.  PN.  —  OF.  Mahaut,  of  Teut.  origin. Cp.  OHG.  Mahthilda  and  see  Matilda, maud,  n.,  a  woolen  plaid  worn  by  shepherds  in Scotland.  —  Prob.  from  the  PN.  Maud. maudlin,  adj.,  tearfully  sentimental.  —  ME. Maudlin,  ‘Mary  Magdalene’  (see  Luke  8:2),  fr. OF.  (=  F.)  Madelaine,  fr.  L.  Magdalena,  in allusion  to  the  fact  that  painters  used  to  rep¬ resent  Mary  Magdalene  weeping;  maudlin orig.  meant  ‘shedding  tears  of  penitence  like Magdalene’.  See  Magdalene, mauger,  maugre,  prep.,  in  spite  of  (archaic).  — ME.  maugrie,  fr.  OF.  malgre,  maugre  (F.  mal¬ gre),  lit.  ‘ill  will’,  fr.  mal,  ‘ill,  badly’,  and  gre (F.  gre),  ‘will,  pleasure’.  For  the  first  element see  mal-.  The  second  element  comes  fr.  L.  gra- tum,  neut.  of  gratus,  ‘acceptable,  pleasing, agreeable,  grateful’,  used  as  a  noun.  See  grace, n.,  and  cp.  malgre.
31505:race,  n.,  running.  —  ME.  ras,  rase,  fr.  ON.  ras, ‘running,  race',  rel.  to  OE.  rtcs,  ‘running,  rush’, rzesan,  ‘to  rush  headlong’,  MDu.  rasen,  ‘to  rave, rage’,  MHG.  rasen,  G.  rasen,  OE.  rdsettan,  of s.m.,  and  prob.  cognate  with  Gk.  epoirj  (for *4po>aa),  ‘quick,  motion,  rush,  force’,  cpcostv (for  *£p«actv),  ‘to  rush,  rush  forth’,  L.  rordrii, ‘lightarmed  troops',  lit.  ‘runners’.
31508:raceme,  n.,  a  type  of  flower  cluster  (bot.)  —  L. racemus,  ‘the  stalk  of  a  cluster  of  grapes’ ;  which, like  Gk.  pa;,  gen.  payo;,  ‘berry’,  was  borrowed from  a  Mediterranean  language.  Cp.  the  second element  in  acrorhagus,  Haloragidaceae.  Cp.  also raisin.
31512:racemism,  n.,  the  state  of  being  racemic  (chem.)
=== SKT rhubarb ===
16051:Bhubarb.    (F.  -  Low  L.  -  Gk.)     0 rhi:ubarhe  ;    F.   rhubarU.'^ljOV  L    r barbarum    (»    rhmm    baTif^rmm\, ^Mv  fiaptinfiov,  rhubarb  ;  lit.  '  Kht Ihc  barbarian  country.*     (.k    ^r adj.  from  ^  the  rha-plant,  rhiib&rb,  wl WAS    also    called    ^ka    Fontimm,     AJ took  its  ruune  from  the  river  Kkm^  tc Volga.
=== SKT rosemary ===
16210:Rosemary.  (F.  —  L.)    M.  E.  rvsmarin.
16211:—  O.  F.  rosmarin,  —  L.  rosmarintu,  rot- mnn'num,  rosemary,  lit.  fcen-dcw ;  called rps  maris  in  Ovid.  — L.  ros,  dew;  marittus, marine.  Named  from  some  fancied  con nectionwith  sea  spray;  altered  to  rpstmary (as  if  for  ros/  o/j)/ary)t
```


## [2026-09-05T20:37:39.228Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins ers ===\"; grep -n -i \"^ers-\\|ers- To be\\|ers-\\.\" AHD_watkins1985.txt | head -10; echo \"=== AHD wers/rosemary ===\"; grep -n -i \"rosemary\\|rhubarb\" AHD_watkins1985.txt | head -10; echo \"=== AHD ers ===\"; grep -n \"ers-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for ers- root"
}
```


### [2026-09-05T20:37:39.351Z] TOOL RESULT

```
<persisted-output>
Output too large (58.7KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b2mtnprxc.txt

Preview (first 2KB):
=== AHD watkins ers ===
219:ghers-. 2. Lengthened-grade form
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) 
...
</persisted-output>
```


## [2026-09-05T20:38:08.650Z] TOOL CALL #37: Bash

```json
{
 "command": "grep -n -o \"ers-[^.]\\{0,400\\}\" /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b2mtnprxc.txt | grep -i \"flow\\|dew\\|male\\|wander\" | head -10",
 "description": "Find Watkins ers- root entry"
}
```


### [2026-09-05T20:38:10.755Z] TOOL RESULT

```
5:ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION
19:ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION
```


## [2026-09-05T20:38:14.110Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ers-a- in Latin errdre\\|ers-d- in Latin errdre\" AHD_watkins1985.txt | head; echo \"---\"; grep -n -B2 -A6 \"ers-d- in Latin errdre\" AHD_watkins1985.txt | head -40",
 "description": "Show Watkins ers- entry context"
}
```


### [2026-09-05T20:38:14.187Z] TOOL RESULT

```
458:ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
---
456-ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhus, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]
457-erkv-. To radiate, beam, praise. Sanskrit re, rk, “bright- ness,” praise, poem: Ric-VEDA. [Pok. erke- 340.]
458:ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
459-ers-2. To be wet. Variant form *ros- in Latin rés, dew: ROSEMARY. [Pok. 2. ere-s- 336.]
460-es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
461-esen-. Harvest, fall. O-grade form *osn- in Germanic *aznon, to do harvest work, serve, in Old English ear- nian, to serve, gain as wages: EARN}, [Pok. es-en- 343.]
462-esu-. Good. Extension of es-. Greek ews, good, combining form eu-, well: EU-. [Pok. esu-s 342.]
463-eti. Above, beyond. 1. Germanic *ith- in Old Norse idha, whirlpool: EDDY. 2. Latin et, and (< “furthermore”): ET CETERA. [Pok. efi 344.]
464-6ti-. Eider duck. A probable root. Germanic *éthi in North Germanic *dthi in Old Norse Zdhr, eider: EIDER. [Pok. éti- 345.]
```


## [2026-09-05T20:38:28.476Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"wers-\\|uers-\" AHD_watkins1985.txt | head -10; echo \"=== BQT v2 structure ===\"; grep -c \"\" BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; grep -n \"\\[pdf page\" BQT_v2_pages.txt | tail -3",
 "description": "Check Watkins wers- and BQT v2 page tags"
}
```


### [2026-09-05T20:38:28.556Z] TOOL RESULT

```
1150:wers-2
1155:wers-'. To confuse, mix up. Compare ers-'. I. Suffixed basic form. 1. Germanic *werz-a-, whence *werra- in: a. Old North French werre, war: WAR; b. Spanish gue- rra, war: GUERRILLA. 2. Germanic comparative *wers- izon- in Old English wyrsa, worse: WORSE. 3. Germanic superlative *wers-istaz in Old English wyrsta, worst: worst. II. Suffixed zero-grade form *wrs-ti- in Germanic *wursti- in Old High German wurst (> German Wurst), sausage (< “mixture”): WURST; (LIVERWURST). [Pok. uers- 1169.]
1156:wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1464:ENTO- en ENTOMO- tem- ENTRAILS en ENTRAP der-1 ENTREPRENEUR ghend- ENTRESOL sel-1 ENTROPY trep-2 ENUMERATE nem- ENUNCIATE neu-! ENURESIS wers-2 ENVOI wegh- ENVOY! wegh- ENVY weid- ENZYME yeud- EO- aus-! EQOHIPPUS ekwo- EON aiw-
1571:Grus_ gere-2 GUARANTY wer-5 GUARD wer-4 GUERDON lau-, wi- GUERRILLA wers-1 GUESS ghend- GUEST ghos-ti- GUIDE weid- GUILD gheldh- GUILDER ghel-2 GUILE weik-2 GUIPURE weip- GUISE weid- GULAR gWel-3 GULDEN ghel-2 GULES gwWel-3 GULF kwelp- GULLET gWel-3 Gum? ghéu-
1757:LITHE lento- LITHOTRITY dhreu- LITIGATE ag- LITMUS meu-, wel-1 LITOTES lei- LITTER legh- LITTLE leud- LITTORAL [éi- LITURGY werg- LIVE! leip- LIVELIHOOD leit-2 LIVELONG leubh- LIVELY leip- LIVER! leip- LIVERWURST wers-! LIVERY leudh-? LIVID — sfi-
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
=== BQT v2 structure ===
41071
```


## [2026-09-05T20:38:34.915Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f,'ff=',t.count('\\f'),'len',len(t))\n    print(repr(t[:300]))\n    print('---')\n\"",
 "description": "Inspect BQT page files"
}
```


### [2026-09-05T20:38:36.687Z] TOOL RESULT

```
BQT_v1_pages.txt ff= 776 len 1285412
'\x0c۱ ۵ ۱! ۱\n7 موم ۳ لام\nم ۱ 0 و طق صفرررنیاعدریرماروی\n۰ ۱ "۳\n۳\nم و اس مر هر وه او\n7 رین خلت ریز یتایب بره ات\nلف\u200cبال ۶۲ .یرک\nا اند کل داي رشب , رمع\nفان تا تا\nرن 9 3\nکرحم تن\nاد شش مرا\nمو رم | مر\nوک رهب اه نات مج\nلش\nوان روکد ور\n۱ و\nطراول ؛ | ع اس\nچاپ دوم فروردین ۱۳۴۳\nبا تجدید نظر کامل\nبسرمایه کنابفروشی ا'
---
BQT_v2_pages.txt ff= 683 len 2900526
'\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c'
---
```


## [2026-09-05T20:38:41.068Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:952 2>&1 | head -60",
 "description": "Fetch BQT page 952"
}
```


### [2026-09-05T20:38:43.017Z] TOOL RESULT

```
no scan of BQT covers printed page 952 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:38:46.226Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\"",
 "description": "Show BQT ref metadata"
}
```


### [2026-09-05T20:38:48.316Z] TOOL RESULT

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


## [2026-09-05T20:39:04.316Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 413 452 580; do echo \"=== BQT_v2 leaf(1-based) $L => printed ~$((L-1+540)) ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$L\"' {print}' BQT_v2_pages.txt | head -60; done",
 "description": "Print BQT vol2 pages 952, 991, 1119"
}
```


### [2026-09-05T20:39:07.017Z] TOOL RESULT

```
=== BQT_v2 leaf(1-based) 413 => printed ~952 ===
    ‫‪“Ao‬‬
                                      ‫‪e‬‬
‫رشته نگنده ‪ -‬بکر نون وفتح‌کاف‪‎‬‬                        ‫رشته = بکراولوفتح فوقانی»تارابرشم‬
‫‪۰‬‬    ‫بی قطة مقتوح‪‎‬‬      ‫نون وال‬      ‫فارسی وسکون‬      ‫وربمان وآنجهآ نرارشته باشندا ‪ -‬وام مرضی‬
                                                      ‫است وآن چیزی باشدکه از اعنای مردم بان‬
                          ‫و امثال آ را بدان دوزند ‪۰‬‬   ‫تاررسمان بمریآبد و بیشتر در ش‪ _,‬لار بهم‬
‫زشرتی ‪ -‬بفتح‌اول بروزن کشتی » بمعنی‬
                                                      ‫میرسد؟ ‪ -‬و نوعی از حلوا باشد ‪ - ۴‬و آشی‬
                                                      ‫وپلاوی هم هست‪ -‬و بضم اول رنگه هشته‌ورنگه‬
‫کخسااری باشد و‪-‬شخصی را نکیوزبند که لجن‬                                         ‫کردء را کوبند ‪.‬‬
‫پمایكکند و خاکستر خواکروبه میبرد ‪- ۴‬‬
‫ومنسوب برشت رگافهتمه‌اند ‪ - ۴‬وبمعنی دوم‬
                                                      ‫رشتة قت د ریمانی بود خلمکهآنرا‬
‫که خاکروب وخا کروبه‌برباشد بجای‌فوفانی نون‬            ‫دختر ابالغ رشته باشد و بجهت دفم تب افسون‬
                                    ‫هم آمده است ‪.‬‬     ‫آبنر‌خوانند و گرهی‌چند برآن زنند وبر گردن‬
                                                                                  ‫ب دار بندید ‪.‬‬
‫رشك = بفتح اول و سکون الیوکاف»‬
                                                      ‫مدت‬   ‫رشتۀ درازه کنابه از طول‬
     ‫®ب‪-‬معنی‬‫معروف است که غیرت وحسد باشد و‬
                                                                 ‫وفرصت دور و دراز باشد درکارها ‪.‬‬
    ‫غیورا ‪-‬وعجب وتکیر آهممده‌است‪ - ۷‬و کرمی‬
‫باشد کهعربان صواب میگوبند ‪ - ۷‬وضم اول‬                 ‫رفت‪4‬ة ضحاك ه کنابه از باران‬
    ‫رم ‪-‬‬  ‫عقرب وکژدم و بکر اول چرك و‬                  ‫لست کهبعربی مطر گوبند ‪ -‬وطول مدت را لیز‬
    ‫ویژمرد کی‪ -‬وتخم شیش رگاویند‪ - ۸‬ویمعنی‬                                                 ‫گفه‌اید ‪.‬‬


     ‫‪ ۴‬آنرا در سواحل خلیح فاری لا گویند‬                ‫تن؟‪.‬‬ ‫اسم مقمول ارزش«‬        ‫‪8‬ے‬
     ‫‪-‬يزچيزی مانند تواررشته های باريك که از خمیرآرد کندم سازد وازآن‬ ‫‪ ۴‬ل‬                 ‫عو‪.‬‬   ‫ورك‪:‬‬


     ‫م‪).‬‬   ‫‪.‬‬   ‫(ه‬   ‫از ‪:‬رشت‬   ‫‪۴‬‬   ‫آش وجزآن ترتب دهند وبتازی «رشیدبه» کویند «ناظمالاطبا؟‪.‬‬
     ‫® = ارخك ( «‪.‬م‪ . ) .‬اوستا ‪ 265272‬پپلوی ‪khsar ۰ 10572‬‏ «‬                  ‫‪+‬ی (سبت)‪.‬‬
     ‫بلوچی‪« 97101‬اسشق شمارء ‪۱۷‬وص ‪ ۷۳۱‬ورك‪ :‬منای ‪ »)6105172( ۷۲:۲‬دزفولی ‪« 0156۲‬امام»‪:‬‬
      ‫بازکوبم له که کس‌سیر خواهد بودن‪ «.‬کلستان‪.»۸۳۱‬‬          ‫رشکم آید که کسی سیرنگه درن وکند‬
     ‫‪ «۷‬بباید داست که دربیان معنی رشك مصنف بچند وجه خطا نموده ‪ :‬اول‬                   ‫غی‪-‬رت‪.‬‬
                                                                                           ‫‪۷‬‬
      ‫آنکهرخك بالفتح بمعنی کرم گفته واین‌خلاف جمهور اهل‌لفت است‪ .‬چه درفرهنگهای معتبرمرشك‬
    ‫بالکسر بمعنی تخم شیش که بهندی لیکهه کوبندآمده‪ ,‬وآن غير کرم است ‪ .‬دوم آنکه کفنه که‬
     ‫کرم مکذور را عربان صوب کوبند » و ابن نیز خطاست » زیراکه درعربی صوابه بوزن غرابه‬
     ‫بمعنی همان تخم شپش آمده لهبمعنی کرم ‪ ,‬سوم آنکه رشك بمعنی عجب ونکبرهم گفته و این‬
      ‫در هکیتچاب ازکتب‌متداولة لفت نیت ‪ ,‬ازبنجاست که بعضی‌از متأخرین انکار این معنی‌نموده‌اند‬
      ‫گوفته کهاین‌معنی‪ -‬یعنی معنی عجب وتکبر ‪ -‬سند میخواهد ‪ .‬وافهاعلم بالسواب ‪ « » .‬چك ص‬
      ‫و خواداری‪( 60152۲‬بقتح راء)‬          ‫ولی‬
                                            ‫زیفو‬ ‫ح » ابمماعنی تخم شیش » دکریلکی و بل‬
                                               ‫دوچ‬                                              ‫‪۱‬‬
                          ‫است » اما اعتراض «چك» ورد معنی «کرم»» صوابه وصجب وتکیر وارد است ‪.‬‬
     ‫هندی باستان ‪( (24992۱1‬نشم شپش)' کردی ع ‪khsir‬‏ > افغانی ‪axir‬‏ ‪ .‬بلوچی ع‬          ‫‏‪A‬‬

     ‫(خم شیش )‬ ‫شمان گوید ‪ :‬رشك ت‬‫و‏ب»‬
                                   ‫تق ‪٩‬ه‪۸۱‬‬   ‫«ناا‪.‬سینا‬‫عاطف‪k , :2‬طوتا‏ ‪ .‬اتی ی‬
      ‫انی ‪( 201۲‬نخم‌شیش) = ابرانی ‪ 2601511 -‬برابرسا کریت ‪ « 8091‬حوبمان‬‫ظارسفیت=‬
     ‫«امام» ک»یلکی ط‪ 5۵۲‬و درتهرانی ‪ 98۴‬ب(کرراه )‬                 ‫دزفولی و خواداری که‬           ‫‪۸‬‬

=== BQT_v2 leaf(1-based) 452 => printed ~991 ===
                                                                                                    ‫‪.‬هرهس‬
 ‫چویزها بیاویز قد ‪-‬‬         ‫ا‬
                            ‫هاز‬‫اه‬
                                ‫جد ک‬
                                   ‫ابباریشم باش‬       ‫ریش خو ت‪۵2‬ه با ای مجهول ‪ ۰‬نام‬
 ‫وآ نچه ازدرخت درزیر خاکه باشد ‪ -‬ونام‌مرضی‬                ‫مرضی وعلتی است کهبعربی خنازیر گوبند ‪.‬‬
              ‫است که آبرا عرق بدلی گونند ‪.‬‬             ‫‪٩‬‏ ‪-‬‬   ‫ایت‬     ‫معروف‬     ‫قاصی‪-.‬‬         ‫رش‬

 ‫يرشیدن » بروزن پیچیدن» فروربختن‬                      ‫گزونند که برششه بکادوی شراب‬
                                                                                ‫ولته‌ای را ل‬
                        ‫‪.‬‬    ‫چیزی باشد در چبزی‬        ‫ندند تچاون شراب در بیاله ریز ندصاف رشته‬

 ‫ریشیده ‪ ۲‬ه بر وزن پیچیده » ربغ‬                       ‫شودو کوشٌآن لته کراهآوشته وشراب "رشده‬
 ‫دستار باشد ‪ -‬وبمعنی رنکگ بپشته و ریگ نهاره‬           ‫وقطره قطره‌شراب اآزن میچکیده باشد لیزریش‬
                                                                                  ‫قاضی گویند ‪.‬‬
‫بووپدر‪-‬نیان منقش را نیزگوبند ‪ -‬وام ‪,‬یکی‬
 ‫ازیادشاهان هند حم بوده است‪ -‬ویمعنی رخشنده‬            ‫ریش گاو = با ثالی معروف ؛ مردم‬
 ‫وروشن هم هست‪ -‬وبا ثائی مجپول‪ .‬رشو زخم‬                ‫ابله راحمق وطامع وصاحب آرزو باشد ‪ .‬گویند‬
                          ‫شده رگاوشد ‪.‬‬                ‫شخصی پرخود راگفت که «هرکز ریش کاو‬
 ‫ربع = بروزن قح » مخفف آريخ است‬                       ‫کشاو ؟»‬
                                                            ‫بوده ای ؟» پگرفت‪ :‬ک«دام است ر‬
‫وت و کینه باشد ® ‪ -‬وباثالی‬    ‫او‬ ‫درت‬
                                   ‫عه نف‬
                                       ‫ک‬              ‫کفت ‪« :‬آنکه هرصباح از خأنه برآبد با خود‬
 ‫‪۱‬ه دامن کوه بجالب‬‫مجپول‪ .‬بمعنی راغ‌است ک‬              ‫کوبد کنجی بيابم و چنان و چنین کنم ‪» .‬‬
                           ‫صحرا باشد ‪. ۷‬‬              ‫ب رکفت ‪ « :‬ای پدر ! من همه عمر ریش گاو‬
                                                                                                    ‫بوده‌ام‪¢ .‬‬
 ‫ريغال ب‪-‬اغین شطه دار بروزن قبقال ‪.‬‬
 ‫وشکول را گوبند ؛ و بمایعننی بازای‬
                                 ‫قدح ک‬                    ‫فازانشیوشده‬
                                                                    ‫بمب‌‬
                                                                       ‫دیش کندن = کنا‬
                      ‫نقطه دار همآمده است ‪. ۵‬‬                                              ‫کشیدن باشد ‪.‬‬
                                                      ‫ر یشمال ‪ .‬با میم بر وزن پزیرال ‪.‬‬
 ‫ریک ‪ -‬بکراول وسکون ثالی وکاف‪,‬‬
                                                                  ‫‪۱‬‬           ‫را گونند ‪۱‬‬   ‫وی‌حصت‬        ‫دیوث‬
 ‫بمعنی ای ليك بخت باشد وعدرربی وسحكث‬
 ‫کویند ‪٩‬‏ ‪ -‬وباکاف قارسی‌بروزن دیگه معروف‬                ‫ریشمالی ‪ - ۴‬بروزن‌نیك‌فالی‪.‬د‪,‬وی‬
 ‫ونایت از ذره‬
            ‫‏(‪ ۱٩)۱‬و عربان رمل خوانند ‪ -‬ک‬                                         ‫وبی‌حمیتی باشد ‪.‬‬
 ‫هم‌هست ‪ -‬و بمعنی بخت وطالم نیزگفته‌اند ‪-‬‬              ‫= بروزن‌نیشه‪ .‬تارهای ربمائی‬             ‫ربثه‬

                                                                       ‫‪.‬‬   ‫اس‬    ‫(‪ )۷‬چك ‪+ :‬‬

       ‫ی (مصدری) ‪.‬‬            ‫‪ - ۴‬از‪ :‬رشمال‬               ‫‪ - ۱‬لفة لحية فاضی (رش داور) ‪2‬‬

  ‫‪ - ۴‬پهلوی ‪( 2۵15۵۲‬مو) «اسشق ‪1۰٤٥‬ء‏ بازند ‪ 6051۲‬پ»ارسی رسکه ( بکر اول )‬
             ‫‪٩‬‏ رك ‪:‬آریغ ‪.‬‬       ‫‪ ۴‬اسم مفعول از «رشیدن» ‪.‬‬                    ‫ار‬
                                                                  ‫دنوالا ‪. ۵۲4‬‬
  ‫» رء‌فغوادمی وجالوری که‬      ‫ریخ («‪.‬م‪ ).‬است‬     ‫دیمع‬        ‫‪۲‬‬               ‫رك ‪ :‬راغ ‪.‬‬   ‫‪-‬‬    ‫‪۹‬‬

   ‫شمش روان بود و اهال داشته باشد و تواند خویشتن‌را نگهدارد ‪ -‬یلید ‪ .‬در کتابادی ربشوله‬
  ‫‪٩‬‏ ‪« -‬ازین تفسیر واضح میشودکه مؤلف ظاهراً‬                       ‫_زربكغ‪:‬ال ‪.‬‬                  ‫«کنابادی» ‪.‬‬
   ‫« ويك » (بفتح اول ) عربی را «ريك» خوانده و آبرا فارسی تصور کرده» «محمد قزوننی»‪ .‬موّلف‬
  ‫‪ -‬بعنی شن ارمی که از تفتت سنگریزه ها‬            ‫‪۶‬‬           ‫در آخر همین ماده باواو همتقل کرده ‪.‬‬

    ‫»ردی‬
       ‫حاصل شده * سنگریزه «ناظم الاطبا»‪ .‬وآن در استی ‪( 81۲‬کردوغبار) «ك ‪ .‬است ‪۲۳۱٩‬‏ ک‬
   ‫ةا و ‪ , 81۲‬افقانی ‪ * 8۵۲‬بلوچی ‪ ۵۲‬و ‪» 5۵۲‬یارسی باستان ‪ * 4612۲ -‬آمده‪ .‬رك ‪:‬اسشق‬
                              ‫و هوشمان ‪ ۲44.۰‬اشکاشمی ‪( 86۲‬رمل) «کربرسن ‪» ۲۹۰‬کیلکی ‪.811‬‬
=== BQT_v2 leaf(1-based) 580 => printed ~1119 ===
                                                                                                      ‫‪۱۱۷‬‬

 ‫سرپوش است اعم از سرانداز موقتعة زان‬
  ‫و سریوش دیگه وماجق وخوان پوش وامثال آن‪.‬‬                      ‫بروزن زر پرست» بممنی خادم وخدمت کارباشد‪.‬‬
‫= بفتح‌شین نقطه‌دار» بمعنی‬          ‫سر لو شه‬                 ‫با غین نقطه‌دار ‪ :‬بمعنی `‬      ‫‪-‬‬   ‫سر برع‬
     ‫سریوش د‬
           ‫مَکنهمةٌ زنان و‬
                         ‫سریوشنه اءست‬
                                                               ‫سراب است بعنی جابی کهآب ازچشمه‌بارودخانه‬
                            ‫وطبق و خوان پوش باشد‪.‬‬             ‫دربرغ رود »وبرغ‪,‬بندی باشد که آب‌درآن‌جمع‬
‫سبرها ‪ -‬بنتح بای ابجد بروزن آژدها‪,‬‬                                                      ‫شود مائند تالاب واستخر ‪.‬‬
 ‫بممنی خون بای آدمی باشد که بعربی هیت‬                         ‫سر لرکر دن = بمعنی اول‌سریر آوردن‬
 ‫ونابه از زری ات که بحا کم جور‬
                             ‫خوانند ‪ -‬ک‬                       ‫است که کنابه از باغی شدن و افرمانی کردن‬
‫ورفتاران را خلاص کنند با‬‫دهند و اسیران گ‬
                                                                            ‫باشد ‪ -‬و سربالا کردن را نیز گوبند‪.‬‬
   ‫خود بدهد و خلاص شود و بعربی‌قدبه گویند‪.‬‬
                                                               ‫سگرربفرتن ‪ -‬کنایه از خواب‬
  ‫سپریچیدن = کنابه از سکرثی‬                                    ‫برخاستن ویبدار گردبدن باشد ‪ -‬و کنابه‌ازمسافر‬
                             ‫ونا فرمالی کردن باشد ‪.‬‬                                               ‫‪.‬‬   ‫شین همهت‬

 ‫‪ -‬بابای ابجد بروزن‌غرییله‪,‬‬              ‫سیرله‬                 ‫سر بر گهر ردن = کنابه از دوانه‬
‫پیکان پهئی را کونند که مانند بیل باشد بعتی‬
                                                                                  ‫شدن و سودایی گردیدن باشد‪.‬‬
                                      ‫شبیه بآن باشد ‪.‬‬
‫سر تاسر ‪ ۷‬۔ بتای‌فرشت بالف کشبده‬
                                                               ‫ادن ‪ -‬کنابه از ترك سخن‬
                                                                                    ‫سنرهبر‬
                                                                                   ‫کردن وساکت شدن باشد ‪.‬‬
‫قطه بروزن حلوا کر » بمعتی همه‬   ‫‌ین‬‫یس‬‫بتح‬‫وف‬
                                                               ‫سر بز رگ ک‪-‬نابه ازمردمعظیم‌الشأن‬
                       ‫و تمام ومجموع باشد‪.‬‬
‫سرت سبز باد ‪ -‬کنابهازن ات که‬                                                           ‫و عالی مرتبه باشد‪.‬‬
                                 ‫عمرت دراز ‪ ۸‬باشد ‪.‬‬
                                                             ‫بگارن ب«رکدننابه از فکر‬
                                                                                   ‫سير ب‬
 ‫وممت و باآلنف‬
             ‫کشیده وتس بمرجیامجزده»* به‌یمنینمسرناكغوحم ای‬                       ‫کردن و اندیشه نمودن باشد‪.‬‬
                                                                ‫سر بنحه = بباای فارسی و جبیرموزن‬
                                                              ‫ارزنده » یه دست را کویند ‪ -‬و کذابه از‬
‫کيه درازی باشد که زدان گیسوی خود را‬
‫درآن گذارند و بعربی صقاع خوالند بکر صاد‬                        ‫مردم پر قوت و زبردست و مردم آزار و بی‌باله‬
                                                                                                      ‫‪. ۴‬‬    ‫هم هت‬
                                            ‫‪3‬‬     ‫س‬     ‫ی‬

  ‫سر لیر = بروزن لخچیر (‪ )۱‬ب»معنی‬                              ‫سرپوشنه ‪ = ۲‬بفتح ئون ؛بمه‌نیطلق‬


       ‫‪ ۱‬لفة بمعتی‪ :‬برستنده (خدمت کننده) سر( سرور )‪ ۰‬درزبان کنونی‌بمعنی رگیس ک‬
    ‫وقیل‬
        ‫خالواده وموسه و غیره استممال شود ‪| .‬از‪:‬سر(سری)ط‪ -‬برمت (یرستنده) قی ‪ :‬سردار] ‪.‬‬
                                                                           ‫از ‪:‬سر له برغم («م‪. ).‬‬           ‫کت‬

          ‫که دور از تو ناياك و سرپنجه‌بود‪.‬‬                           ‫‪ - ۴‬یکی بادشه زاده در گنجه نود‬
          ‫«بوستان سعدی چاپ فروغی ص ‪۰۳۱٩‬‏ ‪.‬‬                                         ‫سر دوثه («‪.‬م‪).‬‬      ‫تس‬    ‫‪۴‬‬

    ‫‪ = ٩‬زا ‪ :‬رس لس ه‪ ( (-‬دوی فاصتا ‪‎‬نعابشو ) ‪.‬‬                                    ‫سر دوشنه («‪.‬م‪).‬‬       ‫‪-‬‬    ‫®‬

                     ‫‪‎‬یرابتخبو ‪:‬‬‫‪ ۸‬ابو توارط زاتو یک شع‬                                    ‫‪ - ۴‬فس ‪ :‬سراسر‬
```


## [2026-09-05T20:39:31.359Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for w in ['سیاوش','سياوش','ارشان','خشایار','ریوند','رِیوند','ریواس','گشن']:\n        hits=[i for i,p in enumerate(pages) if w in p]\n        if hits: print(f,w,'leaves(0-based):',hits[:12],'-> printed',[h+540 for h in hits[:12]] if 'v2' in f else '')\nEOF",
 "description": "Search BQT vols 1-2 for key headwords"
}
```


### [2026-09-05T20:39:33.016Z] TOOL RESULT

```
BQT_v1_pages.txt سیاوش leaves(0-based): [309, 413, 420, 453, 539, 609, 656, 657] -> printed 
BQT_v1_pages.txt ریوند leaves(0-based): [419] -> printed 
BQT_v1_pages.txt گشن leaves(0-based): [236, 594] -> printed 
BQT_v2_pages.txt سیاوش leaves(0-based): [28, 187, 245, 256, 329, 395, 403, 431, 453, 481, 583, 663] -> printed [568, 727, 785, 796, 869, 935, 943, 971, 993, 1021, 1123, 1203]
BQT_v2_pages.txt ریوند leaves(0-based): [371, 393, 453] -> printed [911, 933, 993]
BQT_v2_pages.txt گشن leaves(0-based): [389, 509] -> printed [929, 1049]
```


## [2026-09-05T20:39:41.174Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 leaf0=453 (printed ~991) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==454' BQT_v2_pages.txt | grep -n \"ریوند\\|ریواس\\|راوند\" ; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==454' BQT_v2_pages.txt | sed -n '1,10p;25,50p'",
 "description": "Print BQT page ~991 rivand entry"
}
```


### [2026-09-05T20:39:43.043Z] TOOL RESULT

```
=== v2 leaf0=453 (printed ~991) ===
31:                     ‫‪.‬‬    ‫و بعربی راوند گویند ‪۴۶‬‬               ‫وریب وافون هم آعده‬       ‫ربا و لفاق ‪ -‬ف‬
41:  ‫‪٩‬‏ ریبای ‏ ریوند‬                      ‫‪ = ۸‬ریبای («م‪. ).‬‬                    ‫‪ = ۷‬رای (هم‪. ).‬‬               ‫‪۱‬‬
...
  ‫رواد‬                                                                                                ‫‪۱‬‬         ‫‪-‬‬
                                             ‫‪.‬‬        ‫اف‬       ‫و بکر اول مخفف اهریمن امت ‪ ۱‬کرهاه‬
‫ریوجام ‏ با جيم بروزن نيك نام ‪۱‬‬                              ‫نمایند بدیها وشیطان باشد ‪ -‬ومحیل و مکار را‬
‫بمعنی بطلان شهوت امت وآن بازایستادن باشد‬                     ‫نیزگفته‌اند ‪ -‬واسب را هممیگویند ‪ -‬و بمعنی‬

                      ‫از کب لذات مطلقاً ‪.‬‬                      ‫‪-‬یک‬
                                                                 ‫پبر هم هت که نقیض دختر باشد ‪ ۴‬و‬
                                                             ‫اول ثوالث بروزن چرکن » زخهی رگاویند که‬
‫و قاف = بىمنی قاف و دال است‬              ‫ری‬
                                                              ‫پرومته از آن چرك و ریم آید؟‪ ۴‬و اين نون هم‬
                                                                                          ‫خودرو باشد ‪.‬‬
                     ‫بکر‬       ‫د‬   ‫ريو ند‬                     ‫دواد د بروزن شیراز » بمعنی عدالت‬
                     ‫اول و سکون نانی و فتح‬                    ‫باشد وآن درستی افعال است وضع هرچیز در‬
                         ‫ثالث و نون و دال هر دو‬                                                      ‫موضم لابق ‪.‬‬
                     ‫است‬       ‫دارو‪:‬ی‬        ‫ساکن ‪۰‬‬           ‫ربو اس باسین‌بی نقطه» بروزن ومعئی‬
                         ‫معروف که اسهال آورد‪۴۱‬‬                 ‫ربواح امت ک‪۸‬ه رستنی مشهور باشد ‪ -‬ویمعنی‬
                     ‫‪.‬‬    ‫و بعربی راوند گویند ‪۴۶‬‬               ‫وریب وافون هم آعده‬       ‫ربا و لفاق ‪ -‬ف‬
   ‫کرلن‌پهلوی‬
            ‫‪ ۴‬شه‬                     ‫» رانک ‪.‬‬         ‫‪:‬ریگ‬    ‫ق‬    ‫‪۴‬‬          ‫‪:‬‬    ‫رك ‪ :‬آهریمن‬   ‫_‬   ‫‪۱‬‬

  ‫ور ‪ 081020۳06۲‬را هم ریش ‪ 621‬اوستابی وربدن فارسی داسته « اسشق ‪ ۰ * ۹۳۱‬وجود‬                                    ‫‪08‬‬
  ‫ین لبت ) تر کیب شده لظیر ‪ :‬رشکن » ربخن »‬                        ‫‪ 4‬ان ( =‬        ‫‪ 0‬میرساند کهکلمه از ‪ :‬ریم‬

  ‫*‏ هندی باستان ‪( 01-۲‬حیله) ( از ربعْ ‪806۲-861-‬‬                              ‫رم‬    ‫رك‪:‬‬     ‫‪۴‬‬
                                                                                                          ‫چر کن‪.‬‬
                  ‫‪ :‬ص نود وسه عقدمه ‪ :‬ریولیز (!) ‪.‬‬                ‫رك‬    ‫‪۱‬‬            ‫کول زدن) ق ‪ :‬فریفتن‪.‬‬
  ‫‪٩‬‏ ریبای ‏ ریوند‬                      ‫‪ = ۸‬ریبای («م‪. ).‬‬                    ‫‪ = ۷‬رای (هم‪. ).‬‬               ‫‪۱‬‬
  ‫(‪ 8522-52۷682‬بمعنی ربوند دست ‪۰‬‬
                               ‫ریواج ‏ روج = رویز ؛ از اوستا ‪۲ 52۷6۸2۲‬‬
  ‫فردست» دارندة دست بافرو باشکوه)‪ .‬بیرونی گوبد «الجماهر ‪ « :»۵۲‬بهمن اردشیر ربوند دست ‪.‬‬
  ‫لان ربرند حواصل الریبای و مبابلغم‌الماءِ فى العمق لم بنبت وان كان رأسه فى ذرى الجبال»‪.‬‬
  ‫ح ‪.9‬‬   ‫رکت‪ :‬دراز دست» ربوندرست؛ درازانگل بقلم تگارنده‪ .‬اندو ابرانعاج؟ شمارء‪ ۳-6‬ص‪۵۲‬‬

  ‫ربرنجو («‪.‬م‪).‬‬    ‫‪=۹‬‬              ‫روجو( «م‪ ۴ ).‬رولجه («م‪ ).‬ر‪۳‬بولجە(ھ‪ .‬م‪.).‬‬                           ‫‪۰‬‬
  ‫خبه درصفحة ‪۲٩٩‬‏‬                                                            ‫ر که‪ :‬ربرای ‪.‬‬       ‫‪=۴‬‬
```


## [2026-09-05T20:40:05.176Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v2 leaf0=583 (printed ~1121) siyavash ===\"; awk 'BEGIN{RS=\"\\f\"} NR==584' BQT_v2_pages.txt | grep -n \"سیاوش\\|سیاووش\\|syavarsan\\|اوستا\" | head -20",
 "description": "Print BQT Siyavash entry"
}
```


## [2026-09-05T20:40:06.418Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF gushn ===\"; grep -n \"گشن\" FSF_pages.txt | head -10; echo \"=== FSF page tags ===\"; grep -n \"\\[pdf page\" FSF_pages.txt | head -2",
 "description": "Grep Noushin Shahnameh glossary for گشن"
}
```


### [2026-09-05T20:40:06.891Z] TOOL RESULT

```
=== v2 leaf0=583 (printed ~1121) siyavash ===
20:‫وستم بکین سیاوشش بکشت ‪ -‬وام موضمی هم‬
```


### [2026-09-05T20:40:06.951Z] TOOL RESULT

```
=== FSF gushn ===
2587:‫کههم باگهربودو همتیغ زن‬                                   ‫وه‬‫درختی گشن شاخ بر کشخ‬
8404:‫چو تو شاه فرزند کی یافتی‬                           ‫فیگشند اسب تازان خویش‬ ‫باهپ‬
15763:                ‫زمان حال استعمال می‌کند‪:‬‬                 ‫درختی گشن شاخ بر شخ کوه‬
19710:       ‫گشن (باپیش گاف پارسی سوکون شین)‬                     ‫بگشتند یکسر ز فرمان شاه‬
19716:‫نر‪:‬هگورگشن [‪:‬نر] کهبهیونجه و جوپرورده‬                  ‫بگرد از وی و سوی یزدان گرای‬
19718:‫در سروده‌های پارسی گشن به معنی انبوه‬            ‫‪۲-‬گردیدن و دورزدن در میدان جنگ و به‬
19729:             ‫درختی گشن بد به میدان شاه‬          ‫بجهنگ ابروان پر ز چین آوریم‬
19733:          ‫درختی گشن سایه بر پیش آب‬              ‫ميان دو صف برکشیده سپاه‬
19742:‫(‪)۴-۲۵۲-۷۷۶‬‬                                    ‫درختی گشن بیخ و بسیار شاخ‬
19748:‫(‪)۴-۱۹۱-۲۱۲۱‬‬                                   ‫بهچشم دل ببین بستان یزدان راگشن گشته‬
=== FSF page tags ===
```


## [2026-09-05T20:40:25.588Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ni=t.find('گشن (با')\nprint('leaf(0-based)=',t.count('\\f',0,i))\npages=t.split('\\f')\nn=t.count('\\f',0,i)\nprint(pages[n][:2500])\nEOF",
 "description": "Print FSF gošn entry page"
}
```


### [2026-09-05T20:40:27.271Z] TOOL RESULT

```
leaf(0-based)= 402
‫کشن‬                                        ‫‪۹۳‬‬

       ‫به هومان چنین گفت کاین شیرمرد‬                   ‫سوی رستم و رخش بنهاد روی‬
‫که‌بامن همی گردد اندر نبرد‬                      ‫یکی چوب زگدرم برپای اوی‬
 ‫(‪)۲-۲۳۲-۷۱۸‬‬                                                                   ‫گشاده‌میان‬

          ‫ز بالای من نیست بالاش کم‬                                      ‫نک‪ :‬میان‌گشاده‪.‬‬

‫به‌رزم اندرون دل ندارد دژم‬                                                        ‫گشاینده‬
                   ‫(دقیقی ‪:)۶-۰۰۵-۰۱۵‬‬           ‫اسم فاعل اگزشادن [گ‪:‬رفتن» مسخر‬
          ‫بگشتند هر دو سوار هژیر‬                              ‫کردن] گیرنده‪ ,‬مسخرکننده‪:‬‬
‫بهگرزو بهنیزهبه‌شمشیر و تیر‬                                   ‫کسی کو گراید به گرز گران‬
                       ‫(اسدی ‪:)۳۰۱-۱۴‬‬           ‫گشایندهة شهر مازندران‬
    ‫ز گرد‬        ‫نگه‬
                   ‫ادی‬
                     ‫م گر‬
                        ‫ه‌دار‬
                            ‫زره‬                 ‫‪۲۰۲۸۰۰۷۱‬‬
‫برون تاخت و آمد برش هم‌نبرد‬

      ‫سترگ‬      ‫گ‬
                ‫گهمردو‬
                     ‫بگشتند با‬                        ‫‪-۱‬روی گردانیدن‪ ,‬سرپیچی کردن‪:‬‬
 ‫به‌خون چنگ شسته چو ارغنده گرگ‬                              ‫نگشتند هردو ز فرمان اوی‪...‬‬

   ‫ومان کومند‬ ‫ورز ک‬ ‫به شمشیر گ‬                  ‫(‪)۳-4-۱۵‬‬

 ‫نمودند هرگونه بسسیار بسند‬                                        ‫(دقیقی ‪:)۶-۴۳۱-۲۹4‬‬
       ‫گشن (باپیش گاف پارسی سوکون شین)‬                     ‫بگشتند یکسر ز فرمان شاه‬
    ‫کو)‬‫درو‬
         ‫ی (خس‬
             ‫ر‪7۱‬‬
               ‫پهلوی ووشن ‪5۵۷‬‬                   ‫به هم پر شکستند پیمان شاه‬
 ‫گوشن «‪5‬داع (وست ‪-‬هوگ ‪ :)۰۸۲‬به‌معنی‬                                   ‫(اسدی ‪:)۶۸۱-۳۶‬‬
‫نر‪:‬هگورگشن [‪:‬نر] کهبهیونجه و جوپرورده‬                  ‫بگرد از وی و سوی یزدان گرای‬
      ‫خ»سرو و ریدک ص ‪ ۰۲‬بند ‪)۱۲‬‬ ‫ش(ده‬            ‫به هر کار فرمان یزدان بپای‬
‫در سروده‌های پارسی گشن به معنی انبوه‬            ‫‪۲-‬گردیدن و دورزدن در میدان جنگ و به‬
‫بوسیار آمده سوخنوران بهضرورت وزن‬                ‫همنبرد حمله بردن و به‌معنی مطلق‬

  ‫گتون بکاهر می‌برند‪:‬‬
                    ‫ارک‬
                      ‫نباح‬
                         ‫ونرا‬
                            ‫گرآ‬
                              ‫شع‬                                               ‫نبردیدن‪:‬‬

                 ‫‪-۱‬با پیش اول و زبر دوم‪:‬‬                   ‫بیاتابگردیم کوین آوریم‬
             ‫درختی گشن بد به میدان شاه‬          ‫بج
```


## [2026-09-05T20:40:42.696Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'گشن' in p:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('idx',i,'tag',m.group(1) if m else None)\nEOF",
 "description": "Find گشن in BQT vol 3"
}
```


## [2026-09-05T20:40:43.820Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['MON']\nprint(d.get('page_offset')); print(d.get('lookup_hint')); print(d.get('notes'))\n\"",
 "description": "Check MON files and offsets"
}
```


### [2026-09-05T20:40:44.450Z] TOOL RESULT

```
pages 721
idx 153 tag 154
idx 228 tag 229
idx 339 tag 340
idx 617 tag 618
```


### [2026-09-05T20:40:46.509Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).
```


## [2026-09-05T20:40:51.917Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} NR==618' BQT_v3_pages.txt | head -70",
 "description": "Print BQT vol3 pdf page 618 (printed ~1821)"
}
```


### [2026-09-05T20:40:54.713Z] TOOL RESULT

```
[pdf page 618]
VANS

لون » بمعتی بیار و انبوه باشد ؛ و ‎nk‏ معنی
بقتح اول و سکون ثانی عم درست است ؛ و نم
اول و سکون ‎st‏ هم درست است - و ‎pe‏ اول
وسکون ‎cyl‏ بممتی نر باشد که در مقابل ماده
است - ودرخت ‎Gls‏ در که بعربی‌فح لگوبند
- و بمعنی طالب‌لر شدن و بار کرفتن مادم سیر
حیوانات ۱ و پارور شدن درخت خرما باشد.

گشن شین ‎othe‏ اول و کس ‎BU‏
‏وشین نقطه‌دار ‎slid‏ رسیده و بنون زده » دام
روز چهارم است از ماههای ملکی.

۳شنه ۲ جنم اول وسکون ثانی‌وفتح
نون + بمعنی کرسته باشد .

گشفی ۴ ۰ بنم اول و سکون ثالی
‎ali,‏ بتحتالی رسیده » رفتن جانور لر باشد بر
بالای ماده ‎ice‏ جفت شدن حیوانات با هم -
و کشنی درخت یمنی چیزی از درخت خرمای
تر بدرخت خرمای ماده دادن . گوبند یکال

‎ctu - ۱‏ انگله (رملکه) در هر قرالی
بفرمان ‎Wa‏ زو ‎oS‏ کیرد

‎aL Sanna om ۴‏
۴ - از :کفن‌ج+ی (حاصل مصنر: اسم معتی).

‏و رك : اسشق - هوبشمان ۹۷۵ .

‏حضرت رسالت صلوات‌انه ‎de‏ از کشنی درختان
منم فرمود درآسال درختان بارنگرفتند. بعرض
رسول رسانیدند که امال درختان بارور شدند
حضرت فرمود ‎pals‏ اعلم بامور ‎sa‏ کم » بمداز
آن معتاد همه سال را بجاآوردند ۰
خنیز ۴ » بکس ‎dst‏ رستنیی باشد

‏که آنرا بمربی خلجان ۵ کوبند - و بفتح ‎Jal‏
‏رفتار با داز و شادمانی و خرامان و شادان
باشد .

‏گشنیز حصر 6 = کنابه از شراب
الگوری باشد .#۶

‏گشبی ۱ ‎gine‏ اول ‎Ss‏ ثالی‌مشتف
و سکون تحتالی ۰ ‎inn‏ خوشی و خوشحالی
و تندرستی باشد ؛ و با ثانی مشدد لیزهمین معنی
دارد - و خرامید کی و جلوم‌گری و ناز رفتاری
را ‎say Ga‏

‎aT 5‏ نکاور مادیالی
خداگفتی شگفتی در پذبرد.

‏بظام یکنجوی درصفت ‎pd‏ « الجمنآرا ‎at‏

‏۴ س کعنیج ‏ کننیز,پهلری

‏« خر وکوانان . متون پهلوی جاماسپ اساناج ‎ksholsh Sega, ۳۰ ol‏ و ‎kishnish‏
‎coriandre)‏ فر) «ژاباس ۳۳۹ ¢ ؛ کشنیز ( ‎coriandrum‏ ) کیاهی است از تبر#چتربان, که
بر گهای تازة آن خوراکی و داله های وی تقریباً کروی و جوهر مخصرصی دارد که‌بیار تتد است
6 « کل کلاب ص۲۳۵ > . ۶ صحیع « جلجلان ‏ « فزوینی > .

‏1 - صحیحه کشی» است .

‎. ‏کشواد‎ : Ay - ol gh? ۵

‎. ‏گشودن - بضم اول و فتح چپارم , رك : گشادن‎ O
```


## [2026-09-05T20:41:13.938Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT syavarshan ===\"; grep -n \"syävarsan\\|syavarsan\\|syäva\\|syava.ars\\|syäA'ars\" BRT.txt | head -10; echo \"=== BRT arsan-aspa ===\"; grep -n \"arsan.aspa\\|arsanaspa\\|ars'aspa\" BRT.txt | head -10; echo \"=== BRT arsan- headword ===\"; grep -n \"•  j.,  g.  arsan-\\|j.  arsan-\\|arsan-  m\" BRT.txt | head -10",
 "description": "Grep Bartholomae for Syāvaršan and aršan-aspa"
}
```


### [2026-09-05T20:41:14.022Z] TOOL RESULT

```
=== BRT syavarshan ===
3097:•  j.  a;'rae'ra9^-  m.  EN.  eines  Gläubigen, eines  Bruders  Franrasyan%:  "'^aAe  nara- vahe  alaonö  Yt/^.  131;  —  puirS  kaoia (sd.)  syävarsänai  .  .  ""^ake^a  naravaht ".  .  und  (als  Rächer  des  Ä. . ."  YLf?.i8,
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
27187:—  Vgl.  säma-  und  zu  »syäva-,
27188:"  j.  syäva-  Adj.  'schwarz'.
27192:•  j,  syävaspi-  m,  EN.  eines  Gläubigen: */»V"  asaonS  Yt. /_J.  114.
28220:•  j.  zürö.jata-  Adj.  'unrechtmässig,  ver- räterisch getötet*;  syävariami  (sd-,  Dat statt  Gen.)  -take  narake  Ytp,  18;  —  yat aae  ya  sfS.jata{^:)ca  .  .  'iala  V.  7.  3.
=== BRT arsan-aspa ===
=== BRT arsan- headword ===
23082:Ableit.  aus  *varsan-  m.  'mas';  aL  vfian-  m., np.  ffuian').  —  Vgl.  ivarina-  EN.  —  Pfi.: dnbdannh  na;  lies  dndannknp  •«  vai«  karp,
```


## [2026-09-05T20:41:14.906Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 206 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==227' HRN.txt | head -50",
 "description": "Print Horn page 206 (leaf=printed+21)"
}
```


### [2026-09-05T20:41:16.778Z] TOOL RESULT

```
=== HRN 206 ===
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


## [2026-09-05T20:42:29.887Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==228' HRN.txt | head -45",
 "description": "Print Horn page 206"
}
```


### [2026-09-05T20:42:31.739Z] TOOL RESULT

```
— 206 —
er auf gtisäde-dil 'fröhlich* verweist. Somit würde es
zur aw. [/sä-, gä&, äyCL^ 'weilen, ruhen, behagen' ge-
hören, zu der auch np. säd (No. 767) zu stellen ist
(Hübschmann, ZDM6. 38, 431). Da indess gusäde-
du u. a. m. sich sehr wohl aus der Bedeutung *offen
erklären lassen, so bleibt die Etymologie sehr zweifel-
haft. Barth olomae (briefl. Mitteilung) denkt daher
besser an Ableitung von einer aus ai. 1 l/'cay- weiter-
gebildeten i/^Ci/O- -f vi, ursprüngl. etwa vom Türvorhang
gesagt (vergl. ai. vi + 1 Kcay-, Bedeutungen 2 und 4).
Die Form mit A:, z. B. jehänkusäl 'Welteroberer , ist
jedenfalls trotz päz. ktisäden ohne etymologischen Wert.
924. fftisuften 'zerstreuen ; verwelken (Vis und RamTn,
S. 55 Vers 3)'; gusuf (gtfsöf) Zerstreuung.
aw. *vi + l^/saoh'; ai. vi 4- l^ksöbh- *in Bewegung,
in Schwanken, in Aufregung geraten*, Causat. skr. 'ver-
wirren*; phlv. v(i)söftan, Praes. v(i)söpet (Men., AV.),
v(i)söp(i)sn (ZPGL).
Verbessert aus kiisuften etc. der Wörterbücher.
Vergl. np. Osuften (No. 32).
925. ffusn ^Männchen, männlich*.
aw. varsni- männlich (Widder)'; phlv. gtisan, vergl.
N. pr. Gusnasp; ai. vfsni^ 'Widder*.
oss. t. Urs 'Hengst' (84).
LW. mand. xr^nj;, syr. n:51^in 'Hengst* (Nöldeke,
ZDM6. 28, 96 ; doch sind diese nicht aw. uysan- *Stier*,
ai. tiksdn- 'Stier, Ochse*, got. auhsa *Ochse'?).
926. guften sprechen, Praes. göy-etn, guftar 'Rede', gep,
'Witz.
g. gaf 'Gespräch*.
ap. \/^gaub', gauhataiy sprechen, sagen* ; phlv. guftan,
guftar, guv{i)Sn (geschrieben gub""), gtiv{i)smh, guv{i)smk,
kurd. giitin ; wa;^. Jög-am, sar. xtig-am,
927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
Daraus sind bokanntlich entlehnt it. ghdehhe ^ fr. julep^ sp.
julepe *Küliltrank*.
```


## [2026-09-05T20:42:42.999Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB rag ===\"; grep -n \"rag 'Ader\\|Ader'\\|rag  'Ader\" HUB.txt | head -10; echo \"=== HUB rasak/rashk ===\"; grep -n \"rask\\|rešk\\|resk 'Neid\\|arask\" HUB.txt | head -10; echo \"=== HUB gusan ===\"; grep -n \"gušan\\|gusan\" HUB.txt | head -10",
 "description": "Grep Hübschmann for rag, rašk, gušan"
}
```


### [2026-09-05T20:42:43.077Z] TOOL RESULT

```
=== HUB rag ===
8510:skr. yakrt-; rag 'Ader = arm. erak; hagirz — hargiz je-
=== HUB rasak/rashk ===
336:71. Np. arask 'Neid* {baraSk Fird. 1, 15, 23 mit Praef, ba-)
337:ist die altere Form zu raSk (afgh. LW. rask malice,
339:gesetzlich durch paz. arask (Min. 61. p. 16 als Var.),
340:phi. arask (Gl. and Ind. p. 20: arashih) auf ap. ^araska"
341:= zd. araska- zuruck, das nach der Tradition, der auch
2633:733. Darmesteter iibersetzt sraska- durch TThrane'.
4250:arask oben p. 12 — 13.
5286:*kalt* = zd. sar eta- (skr. *girta'); arask, rask *Neid*, skr. irasyati
7573:sraska-; surU *Horn', zd. srvd-; mit Umstellung von ausl.
7821:= zd. sraska- (arm. srskem 'besprenge' = zd. srasc-, oben
=== HUB gusan ===
```


## [2026-09-05T20:42:43.123Z] TOOL CALL #56: WebSearch

```json
{
 "query": "Siyavash Avestan Syāvaršan \"black stallion\" etymology Middle Persian Siyāwaxš"
}
```


### [2026-09-05T20:42:50.699Z] TOOL RESULT

```
Web search results for query: "Siyavash Avestan Syāvaršan "black stallion" etymology Middle Persian Siyāwaxš"

Links: [{"title":"Siavash (name)","url":"https://en.wikipedia.org/wiki/Siavash_(name)"},{"title":"سیاوش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%88%D8%B4"},{"title":"Meaning of the name Siavash","url":"https://www.wisdomlib.org/names/siavash"},{"title":"Persian Mythology Origin Names - Behind the Name","url":"https://www.behindthename.com/names/origin/persian-mythology"},{"title":"Siy%C3%A2vash","url":"https://en.wikipedia.org/wiki/Siy%C3%A2vash"},{"title":"Siyâvash — Google Arts & Culture","url":"https://artsandculture.google.com/entity/siy%C3%A2vash/m0dcsqw?hl=en"},{"title":"Meaning, origin and history of the name Siavash - Behind the Name","url":"https://www.behindthename.com/name/siavash"},{"title":"Shabrang","url":"https://en.wikipedia.org/wiki/Shabrang"},{"title":"Siyavash (disambiguation)","url":"https://en.wikipedia.org/wiki/Siyavash_(disambiguation)"},{"title":"Hushang","url":"https://en.wikipedia.org/wiki/Hushang"}]

Based on the search results, here's what I found regarding the etymology of Siyavash:

## Etymology

The name Siavash is inherited from Middle Persian siyāwaxš, borrowed from Avestan siiāuuaršan-, literally "having black stallions". 

Etymologically, the name is derived from the Avestan Syāvaršan, which translates to "possessing black stallions" or "he who has black horses," composed of syāva (black) and aršan (stallion/male).

## Mythological Context

His name means "the one with black stallions" after his horse Shabrang Behzād (lit. 'night-coloured purebred'), who accompanies him during a trial of righteousness. It was popularized by Siyâvash, a legendary prince who is a major figure in Ferdowsi's epic, the Shahnameh.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:42:59.788Z] TOOL CALL #57: WebSearch

```json
{
 "query": "Avestan \"aršan-aspa\" OR \"Aršāsp\" Persian name \"male horses\" Arjasp Arəjaṱ.aspa"
}
```


## [2026-09-05T20:43:01.745Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT arshan headword search ===\"; grep -n \"'Mann,  Männchen'\\|Mann,  Männchen\\|arsan\" BRT.txt | grep -i \"mann\\|hengst\\|mas\" | head -10",
 "description": "Grep Bartholomae for aršan entry"
}
```


### [2026-09-05T20:43:01.803Z] TOOL RESULT

```
=== BRT arshan headword search ===
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
10711:j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
10819:Komp.:  xsayri;\-arsan;  eig,  'der  atsan- ('Hengst,  Held')  unter  den  Herrschern';  vgl. ai.  räjariatha-  m.  Anders  FoV  KZ.  J7.  544, wo  weitere  Litt.  —  >)  Zum  Stammansatz  nnd znei.  s.  S  3lt.  I  b.  2/j.  2,  —  »)  Verunglückte CS.-Bildune.  i  fehlerhaft  fSr  h  der  ZDMG. $4.  [27  gezogene  Schluss  scheint  mir  höchst fraglich.  —  i)  Sollte  GS.  sein.
16824:mit  upa  i)  'etwas  herzu-,  hinzubringen': barssmqn  upa.baraiti  N.  joj;  VytJ^;  — "hrayqm  *kva  *taHi  (sd.)  upa.barS  ratu- fris  N.  70^;  —  hc^ra  taoxma  upa.bara pasvqmla  ..  V.  2.  25;  271*,  30,  33,  35  f.*, 38.  a)  mit  Dat.  der  Person:  jahikayai ya.  aom  pu%r?m  baraiti  anyahmai  arsanai varitftn  paike  upa.baraiti  ",  .  die  da  das Kind  gebiert,  das  von  einem  fremden Manne  gezeugt  ist,  (und)  es  dem  Ehe- mann zubringif-  Vt  ly.  58.  a)  sva.  'ver- schaffen': upa  hg  gaotum  (sd.)  baraiti  V. 3.2$;  —  uj>aca  kl gatüm  baraypn  "und sie  sollen  ihr  ein  Lager  verschaffen"  V. 75.  43.         3)  'beilegen':  s.  Inf.
18973:—  »)  Pü. !  änämiru  i5._,  «ber  Sü, :  namasirüh.  — J)  Pa.i  nyäyün  ^3kim  ökrmcad  hai  kasän  vam fia  »yäyim  ku  i^arsandih  i  pa  marlumän  pa an  iamän  ia  kör  u  katfai  hmind  tiyäyan pafirim.  Nicht  recht  deutlich.  —  1>  Wie  im Aiiid.    Es  ist  etwa  astu  oder  Ju^'ä/zueigäuzen.
20904:—  aitenasävSyä  {aisii^ai.)  sps.i)r»taca..  y.i.$,  5.19;  —  aiqm  drujim  yqm  diisH- V.3.4;  —  aOe  yä  spujaiaca..  Y.y.3; — '^rqm  Yt./p.95;  '3-9' — pairikqm  yq$n ti yöi  ptiira  "iraitaünahe  F.^t;  —  upa  .  xnq'iatli  {s.A.)  Y.  ig.  $,  1.9;  —  vahislam ave  stärV  ydi  kaptd.iringa\t.i2.2Z.  t)a.-  tstim  .  .  yqm  asahe  vahiäaht  Vr.  2_j.  i; APf.:  tun  gax'ia  *amarsanli/  (sd.)  yti  Y.  57.33',  Yt  70. 33,  y.8sf.'^;  —  das aiahe  sauuAaitis  yt.1g.12;  —  yd..g<'i'iä  Relativ  steht  hinter  dem  attrib.  Adjektiv frasrävayat  ya  patua  ..  zara^ttjVra^  Y.  ■  dasSubstantiv  folgt:  vispqmiayqm  asaonS Sy.&;  —  paiti.pirpne  vispä  */anayö  y a  i  sttm  V1.16.1;  —  vTspqin  yqm  astiaifim drvaitisV.20.\o;  —  vfsp.isca  äpö  yä  ..  ar-\gai>qm  \t.ig.^^;  —  dämtm  ..yqm  är- matsti  Y.6tf.6;  —  fravafayd  yazamaide  maitim  spintam  Vr.  ig.  2.  a)  imqm yä  amisanqm  ipmtanqni  Y.26^,3;  Yt /_?.  damqm  yqm  äliüirim  YLÄ59;  —  azi 23— 26',  40.  a)  ta  ahmt  nmäne /am-  imqm  tanüm  yqm  masyänqm  V.20.3;  — yär?s  ya    aSaonqm  xsnütasca  .  .  Y.  ö'o.  a;  upa  tarn  cantqm  yqm  danyqm  Vt/'/.  77;
23082:Ableit.  aus  *varsan-  m.  'mas';  aL  vfian-  m., np.  ffuian').  —  Vgl.  ivarina-  EN.  —  Pfi.: dnbdannh  na;  lies  dndannknp  •«  vai«  karp,
```


### [2026-09-05T20:43:09.451Z] TOOL RESULT

```
Web search results for query: "Avestan "aršan-aspa" OR "Aršāsp" Persian name "male horses" Arjasp Arəjaṱ.aspa"

Links: [{"title":"DRVĀSPĀ - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/drvaspa/"},{"title":"Arjasp","url":"https://en.wikipedia.org/wiki/Arjasp"},{"title":"PERSONAL NAMES, IRANIAN ii. AVESTAN NAMES - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/personal-names-iranian-ii-avestan/"},{"title":"AVESTAN LANGUAGE ii. The phonology of Avestan - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/avestan-language/avestan-language-ii-the-phonology-of-avestan/"},{"title":"اسب - Persian With El","url":"https://persianwithel.com/glossary/asb/"},{"title":"Verethragna","url":"https://en.wikipedia.org/wiki/Verethragna"},{"title":"Asparukh (name)","url":"https://en.wikipedia.org/wiki/Asparukh_(name)"},{"title":"ASB - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/asb-horse-equus-cabullus-av/"},{"title":"Drvaspa","url":"https://en.wikipedia.org/wiki/Drvaspa"}]

Based on the search results, I can provide you with information about these interconnected terms:

Arjāsp is the Modern Persian version of Avestan Arəĵaṭ.aspa, a name related to aspa meaning horse. He is already mentioned in the Avesta, but he is most prominently featured in the Shahnameh, the national epic of Greater Iran.

Regarding the "aršan-aspa" element: Aršan is based on compounds with Av. aršan- meaning "male, man, hero", while aspa- means "horse". This etymology directly relates to what you mentioned about "male horses."

The name is mentioned by Tabari, Bal'ami, and Ebn al-Balkhi as Kharzāsp, and Ebn Khordādbeh refers to him as Hazarāsf, which are considered to be corruptions of the Middle Persian rendering of the name.

The search results confirm the linguistic connection between the various transliterations you provided (Aršāsp, Arjasp, Arəjaṱ.aspa) as different representations of the same Avestan-Persian name with equine etymology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:43:18.824Z] TOOL CALL #59: WebSearch

```json
{
 "query": "\"ارشاسپ\" نام ایرانی اوستایی معنی اسب"
}
```


## [2026-09-05T20:43:19.531Z] TOOL CALL #60: WebSearch

```json
{
 "query": "\"ارشان\" نام فارسی معنی مرد دلاور اوستا arshan"
}
```


### [2026-09-05T20:43:27.325Z] TOOL RESULT

```
Web search results for query: ""ارشان" نام فارسی معنی مرد دلاور اوستا arshan"

Links: [{"title":"ارشان - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A7%D8%B1%D8%B4%D8%A7%D9%86/"},{"title":"عرشان - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B9%D8%B1%D8%B4%D8%A7%D9%86/"},{"title":"معنی اسم ارشان | گهواره","url":"https://gahvare.net/names/%D8%A7%D8%B1%D8%B4%D8%A7%D9%86"},{"title":"معنی اسم آرشان | حروف ابجد و ریشه آرشان + طالع بینی نام آرشان - تاینی اسم","url":"https://tinyesm.ir/name/%D8%A2%D8%B1%D8%B4%D8%A7%D9%86/"},{"title":"معنی اسم ارشان | حروف ابجد و ریشه ارشان + طالع بینی نام ارشان - تاینی اسم","url":"https://tinyesm.ir/name/%D8%A7%D8%B1%D8%B4%D8%A7%D9%86/"},{"title":"‫[نام نیکو *‿*] معنی اسم ارشان ** آپدیت 1404 ** | برای مشاهده همه معنی‌های اسم ارشان کلیک کنید.","url":"https://nameniko.com/name/%D8%A7%D8%B1%D8%B4%D8%A7%D9%86"},{"title":"معنی اسم اَرشان - معنی اَرشان - اسم پسر - اوما","url":"https://ooma.org/names/boys/%D8%A7%D9%8E%D8%B1%D8%B4%D8%A7%D9%86"},{"title":"معنی اسم آرشان، ارشان، آرشین و ارشین | نام دختر اند یا پسر؟","url":"https://www.namefarsi.com/%D9%85%D8%B9%D9%86%DB%8C-%D8%A7%D8%B3%D9%85-%D8%A2%D8%B1%D8%B4%D8%A7%D9%86-%D8%A7%D8%B1%D8%B4%D8%A7%D9%86-%D8%A2%D8%B1%D8%B4%DB%8C%D9%86-%D8%A7%D8%B1%D8%B4%DB%8C%D9%86/"},{"title":"معنی اسم آرشان Arshan name meaning | نام فارسی پسر","url":"https://namefarsi.com/%D9%85%D8%B9%D9%86%DB%8C-%D8%A7%D8%B3%D9%85-%D8%A2%D8%B1%D8%B4%D8%A7%D9%86/"}]

Based on the search results, here's information about the Persian name "ارشان" (Arshan):

Arshan is a boy's name with Persian roots meaning "arshan, brave, courageous," and it was the name of the son of Ardashir II.

The name Arshan is composed of "arsh" meaning wise and knowledgeable, and the suffix "an," so Arshan means very wise and intelligent. 

Arshan was the name of the son of Ardashir II, the Achaemenid king, and is considered a historical Iranian name.

The name has several meanings in Persian literature and dictionaries:
- Courageous/Brave (دلیر، دلاور)
- Wise/Knowledgeable (دانا، عاقل)
- Man/Male (مرد، نر)

It's worth noting that this is an authentic Persian name with a rich historical background dating back to ancient Persian civilization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T20:43:28.456Z] TOOL RESULT

```
Web search results for query: ""ارشاسپ" نام ایرانی اوستایی معنی اسب"

Links: [{"title":"اسب - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%A8/"},{"title":"اسب - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%D8%A8"},{"title":"اسم اوستایی","url":"https://abadis.ir/name/all/avestai/"},{"title":"نامهای اساطیری اسب در ایران باستان - مهر","url":"https://vr-tra.blogfa.com/post/5"},{"title":"نام اسب و ایران و ایرانیان","url":"https://vista.ir/m/a/qnhz2/%D9%86%D8%A7%D9%85-%D8%A7%D8%B3%D8%A8-%D9%88-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D9%88-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%DB%8C%D8%A7%D9%86"},{"title":"نام اسب و ایران و ایرانیان - باشگاه سوارکاری توسن گناباد","url":"https://tosangonabad.blogfa.com/post/15"},{"title":"نام های نشأت گرفته از اسب در ایران باستان 3","url":"https://iranhorsey.com/%D9%86%D8%A7%D9%85-%D9%87%D8%A7%DB%8C-%D9%86%D8%B4%D8%A7%D8%AA-%DA%AF%D8%B1%D9%81%D8%AA%D9%87-%D8%A7%D8%B2-%D8%A7%D8%B3%D8%A8-%D8%AF%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7/"}]

بر اساس نتایج جستجو، اطلاعاتی درباره نام اوستایی "ارشاسپ" و معنی اسب ارائه می‌دهم:

اسب را در پارسی میانه و اوستایی نیز "اَسپ" می‌گفتند.

نام‌های بسیاری از بزرگان ایرانی در روزگار باستان دارای پسوند -اسپ بوده است (مانند گشتاسپ، ارجاسپ، گرشاسپ، جاماسپ، لهراسپ، ویشتاسپ، هیدراسپ، بیوراسپ، ساتاسپ و …) که نشان از اهمیت این جانور در میان ایرانیان است.

در مورد خاص "ارجاسب" (که شاید منظور شما باشد): ارجاسب به معنی دارنده اسب ارجمند است.

همچنین، واژه اسب (Aspa) یک واژه از دوره پیش از تاریخ و به احتمال زیاد مادی (پارتی، اوستایی) است.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:43:50.640Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 eres ===\"; grep -n \"ere-s-\\|eres-\\|ers-, ṛs-\\|rsen\" incoming/WLD/WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1 for eres-"
}
```


### [2026-09-05T20:43:50.691Z] TOOL RESULT

```
=== WLD Bd1 eres ===
90:      (trans.)“ Fick II 4 17b, III 4 258, Pedersen KG. II 477 (unrichtiger
421:    *ai-s-k-no- mit ausgedrangtem k ist, Pedersen IF. 5, 43, Berneker 276
636:ennyn ,.anziinden“ bleibt fern (Pedersen KG. II 50S).
698:kein idg. ail-, s. zuletzt Thurneysen IA. 26, 25 gegen Pedersen KG. 57
1348:Yerlangen“, Pedersen KG. I 169, wo weiteres nicht iiberzeugende wie auch
1463:und bei Pedersen KG. I 43S, 535                         =
1576: Lehnwort; s. Stokes KZ. 41, 385 m. Lit., Pedersen KG. I 198; cymr.
1581: 33, 276, Foy IF. 6, 328; 8, 203, Brugmann aaO., Pedersen KG. I 42);
1583: aksl. vecen „Abend“, vielleicht arm. giser ,.Nacht“ (s. zuletzt Pedersen
1700:   Dazu (Pedersen Ark. f. nord. fil. 24, 302) lett. vad(u)s „groBes Zugnetz“,
1854:sicb, hilft“ = air. con-di „servat“ (weitere Formen s. bei Pedersen KG. II
1934:und von Rozwadowski Eos 9, S. 96 des S.-A. [Zitat nach Pedersen KZ. 39,
1946:auch arm. giul gen. Dat. gel) „Dorf“ naeh Pedersen KZ. 39, 456 f. aus
2057:(Pedersen KG. I 55       anders, aber ebenfalls nicht liberzeugend Fick II 4
2099:Jones, Welsh Gramm. 107 nicht besser aus *o/o- nach Pedersen KG. I 66:
2103:schwierig ist mir. og, g. ug(a)e d. uig „Ei“. das Pedersen aus dem Cymr.
2118:g. jvoy (nach Pedersen KZ. 39, 406 aus ioio-. das durch Assimilation aus
2169: Pedersen KG. 15 4, die von ir. uagim „nahe‘.          —
2171: Wb. 4) s. aug- „glanzen“. —   Uber arm. acetn „waclise“ (Pedersen KZ. 39, 393) s. Liden
2275:*auiy-sna).                  Ygl. Pedersen IF. 5, 42 f., auch Zupitza Gutt. 3 1 f., Schrader
```


## [2026-09-05T20:43:53.151Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW errare ===\"; grep -n \"erro, -äre\\|errō\\|erro,  -are\\|erro, -are\" LEW_1910.txt | head -10; echo \"=== LEW ros ===\"; grep -n \"^ros,\\|ros,  roris\\|rōs\" LEW_1910.txt | head -10; echo \"=== LAT ros ===\"; grep -n \"rōs\\|ros, roris\" LAT.txt | head -10",
 "description": "Grep Walde LEW and Ernout-Meillet for errare and ros"
}
```


### [2026-09-05T20:43:53.227Z] TOOL RESULT

```
=== LEW errare ===
=== LEW ros ===
=== LAT ros ===
```


## [2026-09-05T20:43:59.465Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW erro ===\"; grep -n \"erro \" LEW_1910.txt | head -8; echo \"=== LEW ros dew ===\"; grep -n -i \"ros, roris\\|rosmarinus\\|ros marinus\" LEW_1910.txt LAT.txt | head -8; echo \"=== LAT erro ===\"; grep -n \"errō\\|erro:\\|ERRO\" LAT.txt | head -8; echo \"=== WLD Bd1 res/ros ===\"; grep -n \"eres-\\|ere-s-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "More greps in LEW, LAT, WLD"
}
```


### [2026-09-05T20:43:59.573Z] TOOL RESULT

```
=== LEW erro ===
538:Spanisch aliso I 31 arapende (alt) I 66 baga I 93 bahia I 93 bazo I 98 becerro I 104 bicerra I 104 bicha I 102 brisa I 116 calibre I 141 cerio I 219 chamorro I 143 estario II 585 fango II 243 fieltro I 497 gamo I 322 gargola I 602 gualda I 841 halar I 141 natron II 171 nino, nia II 170 otero I 32
543:bahta I 93 bezerro I 104 chamorro I 143 covo I 191 feltro I 497 gamo I 322 garguetra I 602 parra I 257 trocar II 708
10111:ferro II 285
=== LEW ros dew ===
LAT.txt:53895:rOs marinus n.(et rosmarinum n.): ronarin, M.L.7383; rOs terrae,
LAT.txt:67371:est herba sacra, ros marinus, ut multi uolunt, i.e. XifJavarcCC* sumpta
=== LAT erro ===
67571:euerro: nettoyer, enlever en balayant, euerriculun " quod Graece
=== WLD Bd1 res/ros ===
9778:‘) rout, rasa, ros, kaum mit Anlaut gr- zu *neres- „ua£‘, s. \ T f. LEWb.' 2 65b. 
9804:Persson Beitr. 636 f.). Neben diesen Gruppen, die auf einem s-St. *eres- 
34568:mit m : aisl. gUna f. ,.Offnung“, schweiz. gim ds. ; aisl. geimi ...Meeres- 
39210:der darum yaXtjvt] aus *yeXdva assimiliert sein lafit?) „Heiterkeit, Meeres- 
46547:KZ. 30,210 aus *ters(o-) herleitbar ist, erwog man als Gdf. *teros-, *teres- 
46549:umgebildetes Heres-tris , -nos sein ; was zur wenig ansprechenden Folgerung 
47945:tres-, ters- (** teres-) „zittern".
```


## [2026-09-05T20:44:02.824Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9770,9830p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read Walde-Pokorny Bd1 eres- section"
}
```


### [2026-09-05T20:44:02.900Z] TOOL RESULT

```
yrsian „fibelwollen“, ai. irasydti „zfirnt, will tibel, benimmt sich gewalt- 
tatig 1 ', irasyd „das t)belwollen“, av. aras-ka „Neid“, mp. np. arask „Neid, 
Eifer“, tiefstufig drssi- „Xeid“, ai. IrsyOt- „Neid, Eifersucht“ (letzteres aus 
* e rdS-ia, wie :) av. arasyant „neidisch, miBgfinstig 11 (s. Bartholomae Airan. 
AA r b. 206 in. Lit.; gr. agog’ dy.ovaiov (ikd/log Hes., hom. agetrj „Schmahwort“ 
(= ai. irasyd), crrygeia „geyvalttiitige, feindselige Handlung“ (urgr. e, vgl. 
ark. mit Zusammendehnung auf Grand eines *&i -ygyg, idg. n 

‘) rout, rasa, ros, kaum mit Anlaut gr- zu *neres- „ua£‘, s. \ T f. LEWb.' 2 65b. 

2 ) Aber gr. atfoggo; nicht als *-onoo ; hierher, sondern dureli aip6-go[f)or zu ersetzen 
(Bechtel Lexil. 79 ■ ; .-zai.iroQoog erst gr. Bildung mit Suffix -oo- von ogr v/u aus (Solmsen 
Beitr. 245). 

3 ) Dazu wohl ahd. rase ,,schnell, kraftig“, nhd. rasch, s. Persson Beitr. 8o7, Falk- 
Torp. 881, 1511. 



el- 


151 


*eros, vgl. aucli sgeo/qAew „Neckerei treiben", Boisacq m. Lit.j, hom. ao« 
(Yok.j „ft/.ajiuxe“ (in r Ageg dosg; Schulze Qu. ep. 456, s. auch Proehde 
BB. 20, 380, Boisacq 76; “.igqg „Gott der Gewalttiitigkeit“ scheint nach 
Bechtel Lexil. 59 nicht urspriinglich cs-St. gewesen zu sein, sondern Per- 
sonifizierung des wzvenvandten Subst. agq „Yerderben, Gewalttat“ (s. auch 
Kretschmer Gl. 4, 347), woven ug^uevog „betroffen, versehrt, gequalt“); 
arm. her „Zorn, Neid, Hader“ (Liden aaO., m. Lit.); sehr zweifelhaft ist 
Zugehorigkeit von. russ. dial, jeresb „hitziger, zankischer Mensch“, jnrsitbsja 
,,sich widersetzen, zanken“ (*jbrs- : ai. 7 rsycL) (v. d. Osten-Sacken IP. 23, 380, 
Persson Beitr. 636 f.). Neben diesen Gruppen, die auf einem s-St. *eres- 
(: ers, e res, rs), *eros- ( e rdS-) beruhen tBrugmann Grdr. II 2 l, 192, wonach 
vielleicht auch lat. error nach errare mit rr ausgestattetes alteres *erds ist), 
stehn mit vergleichbarer Bed.: gr. dor], dgt]f.ievo g (s. o.). ai. irin- „gewaltig, 
gewaltsam“, gr. rot;, igedco, fraglich ob dazu russ. dial, jeretitbsja „sich 
argern, zanken“ u. dgl., s. Wz. *er-, *or~. 

1. el- in Baumnamen fur ,,Erle“ und „Ulme“. 

1. „Erle, Eller“. 

Lat. ohms „Erle, Eller“ (wohl aus *alsnos und nicht, wie friiher Peder- 
sen IF. 5, 40 wollte, mit altem Bindevokal aus *alisnos herzuleiten, vgl. 
dazu Johansson, Beitr. z. gr. Sprachk. 106 und Vf. LE\Vb. 2 2S; das an- 
lautende al geht auf alteres J- zuriick). — Fiir das got. ist nach Aus- 
weis des span, aliso „Erle“, frz. alize „Elsbeere“ ein "alisa „Erle“ an- 
zusetzen; ahd. elira und mit Metathese erila, nhd. Eller, Erie, mndd. 
elre ( ; *nlizo ), else ( : *uliso ), ndl. els ds.; altn. elri n., elrir m., air, qlr ( *ahiz ) 
ds., ags. alor ds. Das idg. e der \Vz. wird durch aisl. jqlstr (*t lustra) 
„Erle‘' und Ustre „ Weide, Salix pentandra“ (* elis-tr-jo -) mhd. dial. Mister , 
halster ds. mit sekund. wie schwed. ( h)ilster ; s. Falk-Torp 469) absolut 
sichergestellt, weshalb Bernekors Ansatz einer idg. «Z-W z. iSlEtWb. 453 f.) 
nicht zutrifft; vgl. dazu die lit. Formen (Persson \Yortf. 894 Anm). Eine 
adj. Bildung ist ahd. crlln „aus Erle“ (vgl. unten die balt.-sl. Formen). 
Nach FickIII 4 26 ware vielleicht auch ags. ellen, ellern , engl. elder „Ho- 
lunder“ zu vergleichen. Zu vergleichen ist ferner lit. alksnis, elksnis , lett. 
dlksnis . ostlett. elksnis , ostlit. aViksnis , apr. alskande (Hs. abskande, vgl.
```


## [2026-09-05T20:44:19.307Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT erro entry ===\"; grep -n \"erro, -as\\|erro,-as\\|erro, -äs\\|errō, -āre\\|erro: errer\" LAT.txt | head -5; grep -n -i \"errare\\|erraticus\" LAT.txt | head -8; echo \"=== SYN dew ===\"; grep -n -i \"12.75\\|'dew'\\|Dew\\.\" SYN.txt | head -8",
 "description": "Grep Ernout-Meillet and Buck"
}
```


### [2026-09-05T20:44:19.389Z] TOOL RESULT

```
=== LAT erro entry ===
9454:caperro, -as, -aul, -at», -are: se froncer, se rider. N'est gofere
19274:erro, -as, -&ul, -fitum, -are; i" errer, aller a 1'aventure (d'oA
57771:en dents de scie (^pithbte de la germandr^e); serrat in', serro, -as:
12317:serrare primitive se composait d'un clou ou d'une cheville passae dans
12347:d'une porte, dans lequel entre le pbne d'une serrare". M.L.1973;
19281:erratum (cf. peccatum) ; errabundus; erraticus, M.L.3905, erratilis
21912:ferrdre M. 1.3956, cf. anssi 356 afferrare, 4399 *inferridre-, prae¬
57492:sera, -ae f.: serrare, constitute k 1*origine par une barre de
57500:Les formes roaanes remontent k serrare, cf.M.L.7867, dont il faut
=== SYN dew ===
5859:4. ON, Sw. haka, Dan. hage, orig, ‘hook’ (as still Dan. hage, Sw. hake) : OE haca, hoc, ete. (12.75). Falk-Torp 371. Hellquist 327.
13730:7. Skt. avic- (cf. attka- ‘bend, hook’): Grk. éyxév ‘elbow’, ayxidos ‘curved’, Lat. uncus ‘hook’, OE angel ‘hook’, ete. (12.75). Walde-P. 1.60f. Walde-H. 1.46.
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
21920:Br. beg, fr. Fr. bec ‘beak’, this of Gallic origin (cf. Beccus, Beccd), possibly (Thurneysen) : Ir. baccan, ete. ‘hook (12.75). NED s.v. beak, sb.
22747:Rum. adinc, fr. Lat. ad-uncus (or Vat. *ad-ancus) ‘bent’ : Lat. ancus, un- cus ‘hook’, etc. (12.75), hence first ‘bent, deep’ (dish, etc.) in contrast to ‘flat?. REW 144. Puscariu 25. Tiktin 21 f.
22913:ON krokottr, Dan. kroget, Sw. krokig, ME croked, NE crooked, fr. ON krokr, Dan. krog, Sw. krok, ME crok ‘hook’ (12.75).
22928:12.75 HOOK
22995:Du. hoek = OE hic, NE hook (12.75). Franck-v. W. 222.
```


## [2026-09-05T20:44:21.153Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB rag ===\"; grep -n \"rag \\[\\|rag, \\|rahg\\|'vein'\" NYB_vol2_glossary.txt | head -10; echo \"=== NYB gusn ===\"; grep -n \"gušn\\|gusn\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep Nyberg for rag and gušn"
}
```


### [2026-09-05T20:44:21.210Z] TOOL RESULT

```
=== NYB rag ===
823:Āxrūrag ['hlwlg] n. pr. 3219315, — Av. (310) Azrira-.
3207:rag [lk'] vein 605, — MPrs rg (A-H I); Paz. ray, NP rag; MPrth rhg (MHC, v. Gloss.).
4182:Viröi-pahr [wylwd p’hl] n. pr. “the Gruzinian Guard", the old name of the fortress Darband at the pass with the same name 114!%. — In Syr the name is Wiröpahrag, in Arm Iwroy parhak, from Arm vir-k*, Gr "IBnpec, 'IBhova.; KZŠPrth l. 2 and 25 wyršn (= Virščin or Virasan for Viracén) = Prs l. 30 end wlwe’n (= Vlucän, hence Russ Gruziya), Gr.
=== NYB gusn ===
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
1442:Ērān-gušasp ['yPn'gwésp'] n. pr. of a general in Azarbaijan 1171, — V. gusnasp.
1746:gusn
1747:gušn [gwšn'] male, in gušnasp. - Olr "oršna-, cf Skr vrsan-, whence *vusn > gušn; Av. (1381) varšnt-.
1749:gušasp [gwšsp'] v. Ērān-gušasp and cf gušnasp.
1752:gušnak [gwšnk'] hungry 25°. — Trans- formation of gurisnak (g. v.) in analogy with tešnak (g. v.).
1753:gušnasp [gwšnsp'] in ātur ~ the second of the sacred fires of Eran-shahr, v. s. v. ätur, — Gušn-asp n. pr. ‘having male horses, stallions’; Arm Všnasp < Vušn- asp. Often gušasp in BP texts — NP, with loss of the the n, cf Ērān-gušasp.
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
6255:désitan: dištan dyp: dipivar fréc: fréc gazitan: gaz gušasp: gušnasp
6956:vic-: lvéxtan vicära, vicärayati: vicar vijate: ?vöxtan vrsan-: gusn
```


## [2026-09-05T20:44:33.528Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['رشک','رگ ','گشن','ریواس','ریوند']:\n    for i,p in enumerate(pages):\n        if w in p:\n            m=re.search(r'\\[pdf page (\\d+)\\]',p)\n            print(w,'| pdf page',m.group(1) if m else i)\n            break\nEOF\ngrep -n \"RESHK\\|RAG\\|GOSHN\\|RIVAS\" ARY_latin_index_pages.txt | head -10",
 "description": "Search Aryanpur for Persian headwords"
}
```


### [2026-09-05T20:44:35.156Z] TOOL RESULT

```
رشک | pdf page 89
رگ  | pdf page 7
گشن | pdf page 429
ریواس | pdf page 476
1483:AULINI (OLD PRUSSIAN) oS 3. ERWARAG,ERVARAK: (PAHLAVI) «5 uy
1682:WEAR ENGLISH) 5-JS3! WASTARAG-, ASTAR
1801:HOLD CHURCH SLAVIC) 4S $s! ASHKARAG, PAHLAVI) 5 shy,
2091:‘APAR, ABAR, ABRAG,(PAHLAVD) «5 4 UPARA., UPARIY. (AVESTAN) glo, |
2092:ABARAGAN, ABARIGAN UPAIRI i
2330:| MACKENZIE: (DRAGON) 111 ANGIS (LITHUANIAN) «ghe}
2508:* TRAGAR ARS PAHLAVI) 5 3g
2623:. ANDAR, ANDARAG (PAHLAVI) «5 shy :
2702:OTR OLD NORSE) AS p99 UDRAG PAHLAVI) «5 3h
2724:2? Jo lay 44 UDRAG 65g UDRAr olen g slaty ly pls tsi Band ger 9210 a
```


## [2026-09-05T20:44:38.594Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef show(tag):\n    for p in pages:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        if m and m.group(1)==tag:\n            print(p[:1800]); print('======')\nshow('89'); show('429')\nEOF",
 "description": "Print Aryanpur pages 89 and 429"
}
```


### [2026-09-05T20:44:40.614Z] TOOL RESULT

```
[pdf page 89]
ا

ا ۲ ۲ اشکه ارس» سرشک

ا اوستایی (4۲587۸4): -ل31٩۸8‏ ,۸8۸۷ انگلیسی کهن (80/05[0 0ا0): ۰۰۰ 784۵8
پهلری (الامتللرم: ۸28 هویم "۰"
کردی (54(ط6): اند ان انگلیسی (لاولاه/(8): 7۸
اففانی (پشتو )(/(4۳01۸). 0 دانمارکی (0۸184): 1
سانسکریت (54(/8877): ,۸81581 ,نکم سرئدی (8801/57): 3

هافتاک۸ ,زا۸058 نروژی (۸/0775014(۷): 710

آرمنی (۸/5/14/7): زد ای اب هلندی (007674): آنففع7
۸۸8 لیتوانی (۵0هلانل 7 ): 3غ۸اقم

یونانی (67858): ,0۸36800 (لا 026 لنرنی (لتی) (71۸4ما): ۸۸۸

۱ اد ایرلدی کهن (#لفللا صام: 258
لاین (/4770): خاانا#کشا ,1۸۲3736۸ ولزی (کل/): 28368
فرانسه (۳۸۵۸/6/1): آر ۱۹ برترنی (872707): اراد زا رد۱۳۹
اسپانیایی (ل5۳۸(/5): ۸ ۱
ایتالیایی ((۸): ۲۸۳8۸ پسگشت‌ها زرد هرادن ردنا
رومانی (۸/۸(/(۷): 13 9 200520
پرتغالي (۳0770001285): ۱ 9 (۲8۸3) اک ین ان
گرتبکه (0077710): 3 ی 7 (5/گه]) :هام05
ایسلند یکهن (010۸۷۵۷ی5 ۵): 11 ماد مت ها

71 40 (75۸) شا
نورس کهن (۸0755 0): 7۸ 6 (ا5۸)) :005
فریزی کهن (7ما5ل2 صان): 7 3 (15۸3) اند

: آلمانی کهن (0582149 04اب صا): ۰ 7 (3ه18) ۸

ت1۸ ,7۸710 بگفتت7۸ برهان قاطع : ۳۹۳
آلمانی (4۸ق087): 58 ,ت73
بادداشت:
8 , 83۸7 ریشه‌های هند و ایرانی این واژه را نمی‌دهند.
ا

======
[pdf page 429]
1/۳۰ گرسنه گشنه» گرسنگی» گشنگی
۱ فارسی (88514(0: گرسته, گشنه, گرسنگی, گشنگی
1 603082807 ,00510 رد0020
ا
پارسی باستان (28781۸4 صان): سوئدی (5[78:01317): ان ۱۱ شش
۸ ۹۷5۸ نروژی (07فا07۳۶0/): 1
پهلوی (۱/مااقمه): هلندی (بلع07): " دی
06 6188۸67 ,خاهقانان اسلاوی کهن (ع7/اماد نات صاه).
کردی (4)(801520). اد لونی ری تآهساه
بلوچی (/8۸007): 6۸6 لهستانی (0۵1/58: 01007 ,ماه
اففانی (پشتو) (/4701۸7): روسی (لفا55ن): 60100۲۷ ,01۵02
: ۸ ,1۸5۲۸ چکه 28071 5 ,فآ
سانسکریت (5۸5777): ان ان صربی (/ل4ا5888): شاه ,تشاج
که ,تکفا ,13013۸7 برهمی (/ل80/751114): 00۷5شآ1 ,0ش ]11
یونانی (0828۴): ۰ ۳8016818 ,۵۲7 اسلوا کی (51014): 3۲5هن11 رتش
گریک (00771): نراد ان لیترانی (/لغاللفتا 77 :هاش ,13113
ایسلندی کهن ((0۸۷۸ا0یی5 صزه): َ
110 پسگشت‌ها ات در
ساکسونی کهن (54200/0 ۵12): 1306۸ 8و مرو
فریزی کهن (۷لفافل۶# صا۵): 11086۸ 7 (111۳63) وی ای
آلمانی کهن (057(4/90 هرز صا0): :2۸050/218
1۸ 8 (11۲68 ب111771651)
آلمانی (0527/۸1): قاشن ۱۱ 332 0ا8
انگلیسی کهن (تاکلا820 ام 1310306۸ 3 :(1036858) :005
انگلیسی (#لکللا8(/0): ینت 2 :(130058) +۸7
دانمارکی (0۸(7184): 48 .۰ | برهان قاطع: ۱۷۹۴-۹۵
اوستایی (/۸87۸): پارسی باستان (۳87۵427 ا0):
1 0858۳۲۸ مقفا0 1 تفج

======
```


## [2026-09-05T20:44:50.568Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%88%D8%B4",
 "prompt": "Give the Persian entry for سیاوش: meaning and full etymology (Middle Persian, Avestan form and its literal meaning, morphological analysis)."
}
```


## [2026-09-05T20:44:51.366Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/error",
 "prompt": "Give the etymology of error and of err (Latin errare, Proto-Indo-European root, Germanic cognates)."
}
```


### [2026-09-05T20:44:57.213Z] TOOL RESULT

```
# سیاوش (Siyavash) - Persian Entry

## Meaning
A proper noun referring to **Siavash** from Iranian mythology, and used as a male given name.

## Etymology
The term originates from Middle Persian (syyʾwhš /siyāwaxš/), which descended from Late Old Persian *Šyāvaršā*, ultimately from Old Persian *Θyāvaršā*, "literally having black stallions."

## Avestan Form
The cognate Avestan form is **𐬯𐬌𐬌𐬁𐬎𐬎𐬀𐬭𐬱𐬀𐬥** (siiāuuaršan), sharing the same etymological root indicating "black stallions."

## Morphological Analysis
The Old Persian construction combines elements referring to:
- **Θyā-** (black/dark)
- **-varš-** (stallion/horse)
- **-ā** (possessive/attributive suffix)

This creates a compound name literally meaning "one who possesses black stallions," reflecting Persian naming conventions that incorporated descriptive elements related to prized possessions.
```


### [2026-09-05T20:45:00.193Z] TOOL RESULT

```
# Etymology of Error and Err

**Error (noun):**
From Old French *error* and Latin *errorem*, meaning "a wandering, straying, a going astray; meandering; doubt, uncertainty." The term evolved to encompass "a figurative going astray, mistake" and later "deviation from what is normal; abnormality, aberration."

**Err (verb):**
Dating to c. 1300, derived from Old French *errer* meaning "go astray, lose one's way; make a mistake; transgress," from Latin *errare* "wander, go astray." Both words trace to the Proto-Indo-European root *\*ers-* "be in motion, wander around."

**Germanic Cognates:**
The semantic field of "wandering" extended into Germanic languages with related meanings of anger or straying from composure:
- Old English *ierre* "angry; straying"
- Old High German *irri* "angry" and *irron* "astray"
- Gothic *airziþa* "error; deception"

Notably, most Indo-European languages originally used words meaning "wander" or "go astray" for error, though Irish took a different path with *dearmad* "error," derived from *dermat* meaning "a forgetting."
```


## [2026-09-05T20:45:08.736Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ers-\" \\\n\"https://en.wiktionary.org/wiki/Xerxes\" \\\n\"https://en.wiktionary.org/wiki/%D8%B1%DA%AF\" \\\n\"https://en.wiktionary.org/wiki/%D8%B1%D8%B4%DA%A9\" \\\n\"https://en.wiktionary.org/wiki/%DA%AF%D8%B4%D9%86\" \\\n\"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%88%D8%A7%D8%B3\" \\\n\"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%88%D8%B4\" \\\n\"https://www.etymonline.com/word/rhubarb\" \\\n\"https://www.etymonline.com/word/error\" ; do\npython3 tools/fetch_source.py \"$u\" --note \"pdf page 160, root Eres 1/Ersen/Ros/Ers/Ere 2: verification of nodes (aršan/Xerxes, rag, rašk, gušn, rivās, Siyāvaš, rhubarb, error)\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources used"
}
```


### [2026-09-05T20:45:13.317Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cb62b715081ee840.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c22599e20c6e1071.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fee1a7664cf8c670.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92602be820b8706a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/046cf08efcf47edf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9c8af90271a36f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87088e698d92e008.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/213ab01d606324b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b33f3b9de12529c0.txt
```


## [2026-09-05T20:45:18.062Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Arjasp",
 "prompt": "Give the etymology section: Avestan form of the name, its literal meaning, and Middle/New Persian forms. Is there any name aršan-aspa or Aršāsp mentioned?"
}
```


### [2026-09-05T20:45:23.570Z] TOOL RESULT

```
# Etymology of Arjasp

Based on the article's "Name" section:

**Avestan Form & Meaning:**
The name derives from Avestan *Arәĵaṭ.aspa*, which is "related to _aspa_ meaning horse."

**Persian Forms:**
- Modern Persian: *Arjāsp*
- Historical variants mentioned by various scholars: *Kharzāsp* (Tabari, Bal'ami, Ebn al-Balkhi) and *Hazarāsf* (Ebn Khordādbeh), described as "corruptions of the Middle Persian rendering of the name."

**Regarding "aršan-aspa" or "Aršāsp":**
No mention of these forms appears in the provided article content.
```


## [2026-09-05T20:45:26.994Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Arjasp\" --note \"pdf page 160: check whether Nourai's Av. aršan-aspa / NP Aršāsp corresponds to the attested Arjāsp (Av. Arəĵaṱ.aspa)\" 2>&1 | tail -2",
 "description": "Archive Arjasp page"
}
```


### [2026-09-05T20:45:28.923Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2baae0e3ffbe4077.txt
```


## [2026-09-05T20:45:43.183Z] TOOL CALL #74: Bash

```json
{
 "command": "ls site/pages/160.jpg 2>/dev/null || pdftoppm -f 160 -l 160 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg160 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 160"
}
```


### [2026-09-05T20:45:45.060Z] TOOL RESULT

```
site/pages/160.jpg
total 17748
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:44 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:45:47.335Z] TOOL CALL #75: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/160.jpg"
}
```


### [2026-09-05T20:45:47.361Z] TOOL RESULT

```

```


## [2026-09-05T20:47:26.312Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ers ===\"; grep -n \"^ersō\\|erso\\b\\|ersa \\|rosā\\|rosa (\\|ṛsēn\\|rsen\" IEC.txt | head -12; echo \"=== SYN 1.77 male / dew ===\"; grep -n \"15\\.86\\|1\\.78 DEW\\|DEW$\\|^DEW\" SYN.txt | head -8",
 "description": "Grep Mann IEC and Buck SYN"
}
```


### [2026-09-05T20:47:28.206Z] TOOL RESULT

```
=== IEC ers ===
733:arsien (arsion, rsien, rsion) ‘male; manly’. WP I, 150. Cf. uers-, urs- Av. arsa, arSàn-; Arm. (ambig.) arni ‘male’; Gk. ársen, árren; Srb. rs 'strength, manly vigour' (for this, cf. Sk. rsami, fr. *rs-)
1145:bhars- (bhar-, bharis-) (1) ‘wheat, barley’. Cf. bhardhà (bharsdha). WP II, 134 Lat. far, gs. farris ‘spelt, barley, flour”; farreum ‘wheat wedding cake; drying kiln’; farr-àgo ‘mash’; Osc. far ‘food’, Umb. (‘wheat or ‘flour’, in farer opeter “of best wheat/flour'; farsio-, adj. id.); Ir. dim. bair-ín ‘cake, loaf’; Go. cf. bariz-eins, adj. "of barley’; OE bere; ON barr ‘barley’; OCS bürü beside borü (“millet or barley. Gmc. LW?); cf. Slovene bersen ‘full of corn, luxuriant’ beside bér ‘millet’. (Forms with and without -s- seem equally current, cf. Lat. far-ina ‘flour: Umb. far- beside farsio and LLat. farricus ‘of spelt’; It. farro ‘spelt’. Uncertainly: Latv. bar-iba *food")
2541:Skt. cf. drsad ‘rick, stone of mil; Av. doros ‘sorrow’; Du. torsen ‘endure, be weighed down’; OCz. drsati sé ‘defy’; Cz. drsný “harsh?
3672:ersKó ‘go to, reach’. Cf. erso (1) Skt. cf. réchami ‘go’; Per. rasam, 1dan “arrive? (LW in Romani: aresav reach": Hitt. arski(mi) *reach'
3949:gerð, ið (1) ‘cry, shout’. Cf. gerso, gars-, gir-
3963:gersð ‘cry, screech’. Cf. gars-, gero, giro. Cf. WP I, 686 Ir. gearr, gs. girr ‘corncrake’; W gêr ('cry', s.); OHG kérran “jar, creak’; MHG kérren, id. beside kirsen, id.; OE ceorran, id.; E (ambig.) to chirr, churr (cf. gir-)
4435:grk- ‘hoarse; hoarseness’. Cf. grquis and ghrquuó, gurks- W gryg ‘harshness, roughness; Cz. hrk (ambig.) *traucousness'
4595:pl. ‘gobbling of a turkey’; Lith. gañdras ‘stork; Latv. gandrs, id. Cf. ghandh- and ghanser ghangh- ‘roar, how? Arm. gangad, a-st. ‘lament’; gangiwn ‘echo, rumble’, cf. also ganfiwn (*scream', fr. *ghan- ghtion); Gk. kagkházo ‘guffaw’; Icel. gagga ‘yelp’: Blg. cf. gágra ‘chatter’. (For OCS gognati ‘murmur’, see gang- (gong-). See next ghanghlaio ‘yell, bawl’. Cf. ghangh- Gk. kagkhaláo ‘guffaw’; Cz. huhlat ‘how? ghanser ‘gander. WP I, 536. Cf. ghandh-, etc. and next Lat. *hanser; anser, id.; MHG ganser; Cz. houser; Pol. gasior, id. ghansis (variant: £hansis) ‘goose’. WP I, 536 Skt. hamsih ‘kind of goose’; hamsáb ‘gander of some king’; Hindi hans 'goose'; Per. yàz, id.; Gk. khén, m.f. ‘goose; gander’; Olr. géiss, Ir. géis, gein ‘swan’; OHG gans, gp. ganso ‘goose’; LG gaus, pl. gáus; OE gos, pl. gës; Fris. goes, pl. gies; Du. gans; ON gás, pl. gæss, id. beside gassi ‘gander’; OCS gosi, pl. gosi; Li. (variant) žąsis; Latv. zoss, gs. zoss, gp. zosu, id.; Finn. LW hanhi, id. gharbhos, à ‘tuft, bundle, sheaf. Gk. kárphos, kárphē “hay, straw; bird?s nest’; OHG garba ‘sheaf’; Du. garf, garve, id.; LW in LLat. garba, Fr. gerbe; Li. cf. garbana *lock, curl’ ghargh- ‘shout, croak’. See next and cf. garg-, gorg-, gargh-. (Skt. ambig.) Skt. garhami, garhe ‘complain’; Arm. garga- tem ‘rave, twaddle’; Icel. garga, a-st. ‘croak, screech’; Li. (ambig.) gargu, eti and gargiu, - tí *cackle, gargle, snore', etc. See garg-, gorg- ghargholos 'gurgling; gurgle; hoarse speaker, gurgle’ etc. Cf. gargar- Skt. ghargharah, adj. ‘gurgling’, etc.); Gk. cf. karkhaléos ‘raucous’; MHG gargeln, v. ‘gargle, gurgle’; Li. (ambig.) gargalas ‘hoarse person’. See next gharghoros (ghorghoros) (1) 'gargling, gurgl- ing’, etc. Cf. ghargholos Skt. cf. ghargharah (ambig. cf. gharghol-); Gk. kárkharos (1) ‘raucous’ beside e-gde kérkho, v. "be hoarse’ (cf. ghergho); Li. cf. ambig. gařgas ‘gurgle; hoarseness’. Cf. garg-, ghergh- gharghoros (ghoerghoros) (2) (rough, sharp,
4880:ghrauo, ið ‘scrape, rasp’ Gk. khráo (1) & khraúð ‘graze, wound’; Lat. rav10, ire “be hoarse’; cf. also råvus (2) ‘hoarse, gruff, harsh’; rāvis, i-st. ‘hoarseness’; Li. griáuju, ti, pf. grióviau: Latv. grauju, pf. grāvu, inf. graut, v. ‘destroy’; Li. cf. grióva ‘boor’; griovis, gs -io ‘ditch’
5994:gherió (£hereio) (?) “shine, appear, look’. Cf. ger-, 201-. Evidence ambiguous Lat. cf. hirquus, i, m. (hapax: “corner of the eye’. Virg. Ecl. transversa tuentibus hirquis, for *&her-oquos, w. Sabine *-e-? Cf. Cz. zrak “sight, eye’, fr. *&hor-oquos?); Li. (ambig.) Zeriu, eti (/shine'. See ĝēr-)
7064:kersno- (2) (keresno-) ‘marrow, brain’. (Prob. same as (1), but cf. kernos (2)) Lat. cf. cerebrum (‘brain’, if fr. *keresno-); Du. hersenen, id.; OHG cf. kirni, Sw. hjerna, id. beside hjesse, ON hjarsi ‘crown of head; Cz. střen ‘bone-marrow, pith’
7065:kerso, ið ‘cut’. Cf. kero, ið and quer-, quors-. W?P I, 429 Hitt. karsami ‘cut off, castrate’; MIr. cerrim, cirrim ‘cut, tear, hack, maim’; Alb. cf. (-é- in) korr, v. ‘reap, harvest’; korrë, f. id. The Slav forms are ambig. cf. R Cereslo ‘cutter, chisel’; Slovak crieslo *plowshare', perb. to quers-, quors- in view of Skt. kársåmi ‘drag, plow’ and krsami ‘plow’, karsah ‘plowing’. Li. kerslas ‘cutter, chisel' indicates the consonantal se- quence, as Ukr. éereslo ‘coulter’
=== SYN 1.77 male / dew ===
1470:ChSl. studenict ‘well’, so SCr. stu- denac, Boh. studné, Pol. studnia : ChSl. student ‘cold’ (15.86). Miklosich 327. Briickner 523. ;
1886:SCr. hladovina ‘coolness’ (fr. hladan ‘cool’, 15.86), also ‘shade’.
2035:2. Lat. glaciés (VLat. glacia > It. ghi- accia, now ghiaccio, Fr. glace, Rum. ghiatd) : gelu ‘icy cold’ (> Sp. hielo ‘ice’), adj. gelidus, Goth. kalds ‘cold’, ete. (15.86). Walde-P. 1.622, 612. Er- nout-M. 412, 423. REW 3718, 3771.
25879:15.85 Hot, WARM 15.86 Cop
27280:15.86 Grk. oxpds Goth. kalds NG Kptos ON kaldr Lat.  frigidus, gelidus Dan. _ kold It. freddo Sw. kall Fr. froid OE ceald Sp. Jrio ME cold Rum. rece, friguros NE cold Ir. tar Du. koud Nir. = fuar OHG alt W. oer MHG kalt Br. yen NHG kalt
```


## [2026-09-05T20:47:33.321Z] AGENT

Now I have enough. Writing the verification file.


## [2026-09-05T20:56:08.636Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build160.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE_ERS = W + \"Reconstruction:Proto-Indo-European/h%E2%82%81ers-\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"aršan, varešna; xšaya-aršan; aršan-aspa; syâva-aršan\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Av./OP aršan- 'male, man, hero' (Skt. ṛ́ṣan-/ṛṣabhá- 'bull', Gk. ἄρσην/ἄρρην 'male') is the regular Indo-Iranian reflex of PIE *h₁r̥sēn 'male' < *h₁ers- 'to flow', semantically 'the one who emits seed' — Pokorny 336 states it exactly so: \\\"mit der Bed. 'männlich' (aus 'benetzend, Samen ergießend') ai. ṛṣabháḥ 'Stier', av. apers. aršan 'Mann, Männchen'\\\". The compounds are equally sound: OP Xšaya-r̥šan- (𐎧𐏁𐎹𐎠𐎼𐏁𐎠 Xšayāršā, Xerxes) 'ruling over men/heroes' — Bartholomae glosses it \\\"eig. 'der aršan- (Hengst, Held) unter den Herrschern'\\\"; Av. Siiāuuaršan- 'having black stallions' (syāva- 'black' + aršan-) is the source of MP Siyāwaxš. TWO items in the node are wrong, however. (a) varəšna- does NOT belong here: Bartholomae s.v. varəšna- 'männlich, masculus' derives it \\\"aus *varšan- m. 'mas'; ai. vṛ́ṣan- m., np. gušan\\\", i.e. from PIE *wr̥sēn- (root *wers- 'to rain, moisten', Pokorny 1169 ff.), a near-synonymous but distinct root; Watkins keeps them apart (ers-2 'to be wet' vs wers-2 'to be wet. Compare ers-2') and Mann (IEC 'arsien') writes 'Cf. uers-, urs-'. (b) aršan-aspa- is not an attested Avestan name: it is absent from Bartholomae's Altiranisches Wörterbuch; the Shahnameh name Nourai probably has in mind is Arjāsp < Av. Arəĵaṱ.aspa- 'having valuable horses', and the genuine 'stallion-horse' compound is Middle Persian Gušn-asp (Nyberg II 84), which belongs to *wr̥šan-, not aršan-.\",\n \"derivation_fa\": \"«ارشان» اوستایی و پارسی باستان aršan- «نر، مرد، پهلوان» بازتاب منظم ریشهٔ هندواروپایی *h₁r̥sēn «نر» است که خود از *h₁ers- «روان شدن، جاری‌شدن» ساخته شده؛ پوکورنی (ص ۳۳۶) معنای «نر» را از «تراوش‌کنندهٔ تخم» می‌داند و سنسکریت ṛṣabhá- «گاو نر» و یونانی ársēn را هم‌ریشهٔ آن می‌شمارد. ترکیب‌های xšaya-aršan- (خشایارشا «فرمانروای مردان») و siiāuuaršan- «دارندهٔ اسبان سیاه» نیز درست‌اند و بارتولومه xšaya-aršan- را «ارشانِ (نریان، پهلوانِ) میان شهریاران» معنی می‌کند. اما دو مورد نادرست است: نخست varəšna- که بارتولومه آن را از *varšan- «نر» (سنسکریت vṛ́ṣan-، فارسی نو گشن) می‌گیرد، یعنی از ریشهٔ جداگانهٔ *wers-؛ دوم aršan-aspa- که در اوستا گواهی نشده و در فرهنگ بارتولومه نیامده است — نام شاهنامه‌ای «ارجاسپ» از Arəĵaṱ.aspa «دارندهٔ اسبان ارجمند» است، نه از aršan-. بنابراین ادعای نورایی دربارهٔ aršan- و ترکیب‌های خشایارشا و سیاوش درست، ولی دربارهٔ varəšna- و aršan-aspa- پذیرفتنی نیست.\",\n \"sources\": [PIE_ERS, W + \"Xerxes\", W + \"%D8%B3%DB%8C%D8%A7%D9%88%D8%B4\", \"https://en.wikipedia.org/wiki/Arjasp\"],\n \"ref_check\": [\n   {\"ref\": \"POK:336\", \"status\": \"supports\", \"note\": \"Pokorny IEW 336 (POK_01.txt leaf 350, under '2. ere-s-'), §2 'Wurzelform ers-, ṛs-; ṛsen \\\"männlich\\\"': \\\"ferner mit der Bed. 'männlich' (aus 'benetzend, Samen ergießend') ai. ṛṣabháḥ 'Stier' ... av. apers. aršan 'Mann, Männchen', gr. hom. ἄρσην ... 'männlich'\\\". Nothing there on varəšna- or aršan-aspa-.\"},\n   {\"ref\": \"AHD:1480\", \"status\": \"not_checked\", \"note\": \"p.1480 of the AHD New College Edition (1975/76) main word-list (the W–X range, presumably s.v. Xerxes); no scan of that edition available locally. The Watkins IE-roots appendix on disk (AHD_watkins1985.txt) has ers-1 'to be in motion' and ers-2 'to be wet' but no 'male' entry, so it cannot confirm this arrow.\"},\n   {\"ref\": \"SOD:414\", \"status\": \"partial\", \"note\": \"Gharib p.414 = entry 10229 (SOD_pages.txt leaf 482, printed ≈ leaf−66): \\\"wšn- B — wašn, w(i)šn ©Av. varəsna; Skt. vṛṣan — male\\\". The page has the 'male' word all right, but Gharib derives it from Av. varəsna-/Skt. vṛṣan-, i.e. from the *wr̥sen- root, not from aršan-.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. varəšna- Adj. 'männlich, masculus' (BRT.txt line 23082) and s.v. xšayāršan- (line 10819)\", \"stance\": \"partial\", \"note\": \"\\\"Ableit. aus *varšan- m. 'mas'; ai. vṛ́ṣan- m., np. gušan\\\" — contradicts putting varəšna- under aršan-; but \\\"Komp.: xšaya-aršan; eig. 'der aršan- (Hengst, Held) unter den Herrschern'; vgl. ai. rājarṣabha-\\\" — supports the Xerxes compound. Grep for 'aršan.aspa' / 'arsanaspa' returns nothing: no such Avestan name.\"},\n   {\"src\": \"IEC\", \"where\": \"s.v. 'arsien (arsion, rsien, rsion) male; manly'\", \"stance\": \"supports\", \"note\": \"\\\"WP I, 150. Cf. uers-, urs- — Av. arsa, aršān-; Arm. arn 'male'; Gk. ársen, árren\\\". Mann confirms Av. aršan- under this root and, like Watkins, cross-refers to *uers-/*urs- as a separate item.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. roric (KLN_1966.txt line 33106)\", \"stance\": \"supports\", \"note\": \"\\\"...Avestic and OPers. arshan, 'man' ... Gk. ἄρσην, ἄρρην 'male, masculine' ... fr. I.-E. base *ras-, *eras-, *eres-, *ers-, 'to flow, wet, moisten'. Cp. ... the second element in Ahasuerus and in Xerxes.\\\" Klein groups exactly as Nourai does (Nourai's likely proximate source).\"}]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"Aršân «ارشان»; Xašâyâr «خشایار»; Aršâsp «ارشاسپ»; Sîyâvaš «سیاوش»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Xašāyār خشایار is the direct New Persian continuation of OP Xšayāršā (Elamite/Babylonian transcriptions, Greek Ξέρξης, Hebrew Aḥašwēroš): OP xšaya- 'ruling' + aršan- 'man, hero'; the full NP form is خشایارشا, shortened to خشایار — confirmed by Wiktionary s.v. Xerxes. Sīyāvaš سیاوش continues MP syyʾwhš /siyāwaxš/ < Late OP *Šyāvaršā (Av. siiāuuaršan-) 'having black stallions': Old Iranian -ršan > MP -waxš > NP -vaš, and syāva- 'black' > siyā- — confirmed by Wiktionary s.v. سیاوش. Aršān ارشان is a genuine Achaemenid-era personal name (Greek Arsanes/Arsames; a son of Artaxerxes II bore it), from Median/OP aršan- 'man, hero', so the gloss 'man, masculine' is right. Aršāsp ارشاسپ, however, is not an attested pre-modern name: the Avestan and Shahnameh name is Arjāsp < Av. Arəĵaṱ.aspa- 'having valuable horses'; ارشاسپ occurs only in modern Persian name-books (Nourai's source FNI, Dānāyī's Farhang-e Nāmhā-ye Irāni), so this fourth item is unverified rather than confirmed.\",\n \"derivation_fa\": \"«خشایار» دنبالهٔ مستقیم پارسی باستان Xšayāršā است: xšaya- «فرمانروا» + aršan- «مرد، دلاور»؛ صورت کامل فارسی «خشایارشا» و کوتاه‌شدهٔ آن «خشایار» است (یونانی Xérxēs، عبری اَخَشوِرُش). «سیاوش» از فارسی میانهٔ siyāwaxš و آن از *Šyāvaršā (اوستایی siiāuuaršan-) «دارندهٔ اسبان سیاه»؛ خوشهٔ -ršan ایرانی باستان در فارسی میانه به -waxš و در فارسی نو به -vaš بدل شده است. «ارشان» نیز نامی هخامنشی است (پسر اردشیر دوم؛ یونانی Arsanes) از همان aršan-. اما «ارشاسپ» در متون کهن گواهی نشده؛ نام اوستایی و شاهنامه‌ای «ارجاسپ» است از Arəĵaṱ.aspa «دارندهٔ اسبان ارجمند»، و «ارشاسپ» تنها در فرهنگ‌های نام‌های امروزی دیده می‌شود. پس سه نام نخست درست و چهارمی بی‌سند است.\",\n \"sources\": [W + \"Xerxes\", W + \"%D8%B3%DB%8C%D8%A7%D9%88%D8%B4\", \"https://en.wikipedia.org/wiki/Arjasp\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1119\", \"status\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ vol. 2 (BQT_v2_pages.txt): the سیاوش material sits on leaf 583 (printed = leaf+538 ≈ p.1121, the nearest hit to Nourai's 1119), e.g. \\\"...ستم بکین سیاوشش بکشت - و نام موضعی هم...\\\"; leaf 580 (printed ≈ 1118) carries only سر-compounds. Borhān has سیاوش/سیاوشان but nothing on ارشان or ارشاسپ, so the page supports only one of the four words.\"},\n   {\"ref\": \"FNI:34\", \"status\": \"not_checked\", \"note\": \"F. Dānāyī, Farhang-e Nāmhā-ye Irāni (Negāh 1370) — refs_online.json marks it purchase-only, no copy online or on disk.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 583 (printed ≈ 1121)\", \"stance\": \"partial\", \"note\": \"as in ref_check: سیاوش present, ارشان/ارشاسپ absent (searched BQT_v1_pages.txt and BQT_v2_pages.txt for 'ارشان' and 'خشایار' — no hits at all).\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab/abadis (Moʿin online) — the aʿlām volumes (5–6) are not online\", \"stance\": \"silent\", \"note\": \"refs_online.json: 'vajehyab's Moʿin has no proper-name entries'; the 6-vol Amir Kabir edition is not digitised, so Moʿin's own entries for ارشان/ارشاسپ could not be read.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched for ارشان/خشایار\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-root dictionary has no entry for these proper names (the only 'رشک'-shaped hit, pdf p.89, is the entry اشک/ارس/سرشک 'tear').\"}]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Pahlavi\",\n \"words\": \"vušn, gushn; gušn-asp\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The forms themselves are impeccable: MacKenzie CPD 38 has \\\"gušn [gwšn'] male\\\" and \\\"Gušnasp [gwšn(ʾ)sp] the second major Fire of Sasanian Ērān, that of warriors\\\"; Nyberg (Manual of Pahlavi II) s.v. gives \\\"gušn [gwšn'] male, in gušnasp\\\" and \\\"gušnasp [gwšnsp'] ... Gušn-asp n. pr. 'having male horses, stallions'; Arm Všnasp < Vušn-asp\\\". Nourai's odd first form vušn is therefore not a misprint but a cited reconstruction — Nyberg writes \\\"OIr *vṛšna-, cf Skr vṛṣan-, whence *vušn > gušn\\\", and Noushin (FSF) prints \\\"پهلوی ووشن wšn / گوشن gušn\\\". But that is precisely why the arrow from this root is wrong: the Pahlavi word comes from Old Iranian *wr̥šan-/*wr̥šna- (Av. varəšni- 'ram', Skt. vṛ́ṣan-), i.e. PIE *wers- 'to rain, moisten' → *wr̥sēn 'male' (Pokorny 1169 ff.; Watkins wers-2 'to be wet. Compare ers-2'), not from *h₁ers-/*h₁r̥sēn. Phonetically the giveaway is the initial g-: Old Iranian *wr̥- regularly yields MP gu-/gur- (*wr̥ka- > gurg 'wolf'), whereas aršan- would have given *aršan/*arš.\",\n \"derivation_fa\": \"خودِ صورت‌ها بی‌عیب‌اند: مکنزی «gušn نر» و «Gušnasp» (آذرگشسپ، آتش دومِ ساسانی، آتش ارتشتاران) دارد و نیبرگ می‌نویسد «gušn نر، در gušnasp؛ از ایرانی باستان *vṛšna-، سنجیدنی با سنسکریت vṛṣan-، از راهِ *vušn > gušn». پس «ووشن» نورایی غلط چاپی نیست، بلکه همان صورت میانجیِ بازسازی‌شدهٔ *vušn است که نوشین هم در «واژه‌نامک» می‌آورد. اما همین نکته نشان می‌دهد که پیوند دادن آن به ریشهٔ *h₁ers- نادرست است: gušn از ایرانی باستان *wr̥šan- (اوستایی varəšni- «قوچ»، سنسکریت vṛ́ṣan-) و از ریشهٔ هندواروپایی *wers- «باریدن، تر کردن» می‌آید. گواه آوایی آن g- آغازین است: خوشهٔ *wr̥- ایرانی باستان در فارسی میانه به gu-/gur- بدل می‌شود (مانند *wr̥ka- > گرگ)، حال آنکه aršan- می‌بایست *aršan می‌داد. پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [W + \"%DA%AF%D8%B4%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"MON:3329\", \"status\": \"not_checked\", \"note\": \"Moʿin's Farhang-e Fārsi, 6-vol Amir Kabir edition — not digitised (refs_online.json: 'still no scan of the 6-vol edition ... purchase-only'); page numbers cannot be mapped onto the online vajehyab/abadis text or onto the 2-vol Adena condensation on disk.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.38 (PHD.txt line 384)\", \"stance\": \"supports\", \"note\": \"\\\"gušn [gwšn' | N ~] male.\\\" and \\\"Gušnasp [gwšn(ʾ)sp] the second major Fire of Sasanian Ērān, that of warriors.\\\" — the Pahlavi forms are exactly as Nourai gives them.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. gušn / gušnasp (NYB_vol2_glossary.txt lines 1747, 1753)\", \"stance\": \"contradicts\", \"note\": \"\\\"gušn [gwšn'] male, in gušnasp. — OIr *vṛšna-, cf Skr vṛṣan-, whence *vušn > gušn; Av. (1381) varšni-.\\\" — the etymon is *wr̥šna-, not aršan-; this is also the source of Nourai's spelling 'vušn'.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 925, p.206 (HRN.txt leaf 228)\", \"stance\": \"contradicts\", \"note\": \"\\\"925. gušn 'Männchen, männlich'. aw. varəšni- 'männlich (Widder)'; phlv. gušan, vergl. N. pr. Gušnasp; ai. vṛ́ṣni- 'Widder'.\\\"\"}]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"gošn, gošan «گشن»; gošnî «گشنی»; Gošnasp «گشنسپ (گشناسب)»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Middle Persian → New Persian step is fully attested and regular: MP gušn 'male' > NP گشن gošn/gošan 'male, stallion; (of a tree) thick, luxuriant', with the abstract/verbal noun گشنی gošnī 'covering, insemination' and the name گشنسپ/گشناسب Gošnasp (Ādur Gušnasp, Ērān-gušnasp). Borhān-e Qāṭeʿ p.1821 defines گشنی as \\\"رفتن جانور نر باشد بر بالای ماده یعنی جفت شدن حیوانات با هم — و گشنی درخت یعنی چیزی از درخت خرمای نر به درخت خرمای ماده دادن\\\", i.e. exactly Nourai's 'insemination', and the preceding column glosses گشن as 'بسیار و انبوه' and 'نر ... که در مقابل ماده است ... و درخت گشن که به عربی فحل گویند'. Noushin's Shāhnāme glossary (FSF) gives the Ferdowsi line Nourai quotes, درختی گشن سایه بر پیش آب. But, as for node 3, the ancestry is *wr̥šan- (PIE *wers-), not *h₁ers-: Horn no. 925 derives گشن straight from Av. varəšni-, and Wiktionary s.v. گشن says 'Ultimately from Old Iranian *vršna-'. So the words and the Pahlavi→Persian arrow are confirmed; the root attribution is not.\",\n \"derivation_fa\": \"گذر از فارسی میانه به فارسی نو کاملاً منظم و گواهی‌شده است: gušn پهلوی «نر» ← «گشن» فارسی نو به معنی نر، نریان، و نیز «انبوه، پرشاخ» (دربارهٔ درخت)، با اسم مصدر «گشنی» و نام «گشنسپ/گشناسب» (آذرگشسپ، ایران‌گشنسپ). برهان قاطع (ص ۱۸۲۱) «گشنی» را «رفتن جانور نر بر بالای ماده، یعنی جفت شدن حیوانات» و «گشنیِ درخت» را گَرده‌افشانی نخل تعریف کرده است، درست همان معنایی که نورایی می‌آورد؛ و «واژه‌نامکِ» نوشین همان بیت فردوسی «درختی گشن سایه بر پیش آب» را گواه آورده است. با این همه، مانند گرهٔ پیشین، خاستگاه این واژه ایرانی باستان *wr̥šan- و ریشهٔ هندواروپایی *wers- است، نه *h₁ers-؛ هرن (شمارهٔ ۹۲۵) آن را یکسره از varəšni- اوستایی می‌گیرد و ویکی‌واژه هم «از ایرانی باستان *vršna-» می‌نویسد. پس واژه‌ها و پیکانِ پهلوی←فارسی درست، ولی انتساب به این ریشه نادرست است.\",\n \"sources\": [W + \"%DA%AF%D8%B4%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1821\", \"status\": \"supports\", \"note\": \"Borhān vol. 3, pdf page 618 (printed = pdf+1203..1205 ≈ 1821-1823): \\\"...بمعنی بسیار و انبوه باشد ... و به ضم اول و سکون ثانی بمعنی نر باشد که در مقابل ماده است - و درخت گشن ... که به عربی فحل گویند\\\" and \\\"گشنی: ... رفتن جانور نر باشد بر بالای ماده یعنی جفت شدن حیوانات با هم - و گشنیِ درخت یعنی چیزی از درخت خرمای نر به درخت خرمای ماده دادن\\\".\"},\n   {\"ref\": \"HRN:206\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie no. 925, p.206 (HRN.txt leaf 228, leaf = printed+22): \\\"gušn 'Männchen, männlich'. aw. varəšni- 'männlich (Widder)'; phlv. gušan, vergl. N. pr. Gušnasp; ai. vṛ́ṣni- 'Widder'.\\\" — supports the word, the Pahlavi antecedent and the name Gušnasp (but with the varəšni- etymon).\"},\n   {\"ref\": \"MON6:1706\", \"status\": \"not_checked\", \"note\": \"Moʿin vol. 6 (aʿlām) — not digitised anywhere (see refs_online.json 'MON'); could not be consulted.\"},\n   {\"ref\": \"FSF:297\", \"status\": \"supports\", \"note\": \"Noushin, Vāzhe-namak, s.v. گشن (FSF_pages.txt leaf 402, page header partly OCRed as '۹۳', i.e. p.293-297 area): \\\"گشن (با پیش گاف پارسی و سکون شین) پهلوی ووشن wšn / گوشن gušn ... به‌معنی نر: هگور گشن [نر] که به یونجه و جو پرورده شده (خسرو و ریدک ...). در سروده‌های پارسی گشن به معنی انبوه و بسیار آمده\\\", followed by the Ferdowsi lines including درختی گشن سایه بر پیش آب — the very quotation printed in Nourai's box.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.38\", \"stance\": \"supports\", \"note\": \"\\\"gušn ... male\\\", \\\"Gušnasp ... the second major Fire\\\" — the Middle Persian antecedents of both گشن and گشنسپ.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. gušnasp\", \"stance\": \"partial\", \"note\": \"\\\"Gušn-asp n. pr. 'having male horses, stallions'; Arm Všnasp < Vušn-asp. Often gušasp in BP texts — NP, with loss of the n, cf Ērān-gušasp.\\\" Supports the name and its meaning; contradicts the root by deriving gušn from OIr *vṛšna-.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 printed ≈ 1821\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, searched گشن\", \"stance\": \"silent\", \"note\": \"the only hit (pdf p.429) is the unrelated entry گرسنه/گشنه 'hungry'; Aryanpur has no گشن 'male'.\"}]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Sogdian\",\n \"words\": \"wšn\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Sogdian wšn- (Buddhist Sogdian) 'male' is real and correctly transcribed, but Gharib's own entry — the very page Nourai cites — derives it from Av. varəsna- / Skt. vṛṣan-, i.e. from Old Iranian *wr̥šan- (PIE *wers-), the same source as MP gušn; Sogdian keeps the initial w- where Middle Persian turned it into g-, which is exactly why the Sogdian form still looks like *wṛšan-. It is therefore a cognate of gušn, not a descendant of aršan-.\",\n \"derivation_fa\": \"«wšn» سغدی (سغدی بودایی) «نر» واژه‌ای واقعی است و آوانویسی آن هم درست است؛ اما قریب در همان صفحه‌ای که نورایی ارجاع داده، آن را از varəsna اوستایی و vṛṣan سنسکریت، یعنی از ایرانی باستان *wr̥šan- (ریشهٔ *wers-)، می‌گیرد — همان خاستگاهِ gušn فارسی میانه. سغدی w- آغازین را نگه داشته، حال آنکه فارسی میانه آن را به g- بدل کرده است؛ همین نشان می‌دهد که این واژه هم‌ریشهٔ «گشن» است نه بازماندهٔ aršan-. پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:414\", \"status\": \"partial\", \"note\": \"Gharib, Sogdian Dictionary, entry 10229 (SOD_pages.txt leaf 482; printed ≈ leaf−66 = 416, Nourai's 414 within the normal ±2 drift): \\\"wšn- B — wašn, w(i)šn ©Av. varəsna; Skt. vṛṣan — male. GMS 147; TSP 19.2a, wšny ʾspy, Hen. Texts. 713n5\\\". Has the word, gives a different root.\"}],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entry 10229 (leaf 482)\", \"stance\": \"partial\", \"note\": \"as above; note also Gharib's citation 'wšny ʾspy' = 'male horses', the Sogdian counterpart of MP gušn-asp.\"},\n   {\"src\": \"BRT\", \"where\": \"s.v. varəšna- (BRT.txt line 23082) and varəšnay- (line 23109 area)\", \"stance\": \"contradicts\", \"note\": \"\\\"Ableit. aus *varšan- m. 'mas'; ai. vṛ́ṣan- m., np. gušan\\\"; and for varəšnay- 'Widder': \\\"ai. vṛṣṇay- m., Np. gušan\\\" — the whole family belongs to *wr̥šan-.\"}]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\",\n \"words\": \"ranhâ; ranha; raěvas\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the three items are sound. (1) Av. Raŋhā- is the mythical world-river, the exact cognate of Vedic Rasā-, and Ptolemy's Ῥᾶ (Rhā) for the Volga belongs with it: Pokorny 336 has \\\"ai. rasā́ 'Feuchtigkeit, Naß', auch mythischer Flußname gleich av. Raŋhā (d. i. Rahā), daraus der Name der Wolga Ῥᾶ\\\", and Klein s.v. roric gives \\\"Rasa, name of a mythic river (= Avestic Raŋhā) ... prob. also Ῥᾶ, Scythian name of the Volga\\\". (2) raŋhā- as the etymon of the Iranian word for 'vein' is Gharib's own reconstruction, not Nourai's invention: SOD 8425 \\\"rʾk M — rāk ©<*rahaka-; Av. raŋha; Parth. rahg; MP rag — vein\\\"; Wiktionary reaches the same family from the other side (NP رگ < MP rag < Proto-Iranian *HraháH < PII *HrasáH < PIE *h₁rṓs, i.e. the o-grade 'dew/moisture' noun that also gives Latin rōs). (3) raēvas 'rhubarb' is wrong: Av. raēvas- is the s-stem of raēvant- 'reich; prächtig, prunkvoll' (Bartholomae, cf. raēvas-ciθra- 'von reicher Herkunft', raēvas-tama- 'der reichste'); there is no Avestan plant-name of this shape, and modern etymology takes NP ریواس from MP rēbās < Proto-Iranian *(h)rabā́š, unrelated to raŋhā-.\",\n \"derivation_fa\": \"از سه واژهٔ این خانه دو تای آن درست است. نخست Raŋhā- اوستایی، رودِ اساطیریِ جهان، هم‌ریشهٔ دقیقِ Rasā- ودایی؛ پوکورنی (ص ۳۳۶) می‌نویسد نام یونانیِ ولگا (Ῥᾶ) از همین واژه است و کلاین نیز همین را می‌گوید. دوم، گرفتنِ raŋhā- به‌عنوان خاستگاهِ واژهٔ ایرانیِ «رگ» از خودِ قریب است: «rāk سغدی < *rahaka-؛ اوستایی raŋha؛ پارتی rahg؛ فارسی میانه rag» — و ویکی‌واژه هم «رگ» را از ایرانی آغازین *HraháH و سرانجام از *h₁rṓs (همان نامِ o-پایهٔ «شبنم/تری» که لاتین rōs از آن است) می‌گیرد. اما سوم، raēvas «ریواس» نادرست است: raēvas- در اوستا ستاکِ s-دارِ raēvant- «توانگر، باشکوه» است (بارتولومه: raēvas-ciθra- «نژاده»، raēvas-tama- «توانگرترین») و هیچ نام گیاهی با این صورت در اوستا نیست؛ ریشه‌شناسی امروزی «ریواس» را از rēbās فارسی میانه و ایرانی آغازین *(h)rabā́š می‌داند. پس این بخش خطای مؤلف است.\",\n \"sources\": [W + \"%D8%B1%DA%AF\", W + \"%D8%B1%DB%8C%D9%88%D8%A7%D8%B3\"],\n \"ref_check\": [\n   {\"ref\": \"POK:336\", \"status\": \"supports\", \"note\": \"Pokorny IEW 336 (POK_01.txt leaf 349-350): \\\"1. Ai. rása-ḥ 'Saft, Flüssigkeit', rasā́ 'Feuchtigkeit, Naß', auch mythischer Flußname gleich av. Raŋhā (d. i. Rahā), daraus der Name der Wolga Ῥᾶ\\\" — supports the river and the Volga identification (not the 'rhubarb' word).\"},\n   {\"ref\": \"AHD:1115\", \"status\": \"not_checked\", \"note\": \"p.1115 of the AHD New College Edition main word-list (the 'rh-' range, presumably s.v. rhubarb/rhea); that edition is not on disk, and the Watkins appendix has no rhubarb entry.\"},\n   {\"ref\": \"SOD:339\", \"status\": \"supports\", \"note\": \"Gharib entry 8425 (SOD_pages.txt leaf 407; printed ≈ leaf−66 = 341, Nourai's 339 within drift): \\\"rʾk M — rāk ©<*rahaka-; Av. raŋha; Parth. rahg; MP rag ©ob. pl. -tyy — vein. GMS 399; Hen. JRAS 1942, 232 n6; BSOAS 12, 312.123\\\" — exactly Nourai's raŋhā 'vein' → rahg/rag chain.\"}],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. raēvant- and raēvas-čiθra- / raēvas-tama- (BRT.txt lines 24784-24792, col. ≈1485)\", \"stance\": \"contradicts\", \"note\": \"\\\"raēvant- Adj. 'reich; prächtig, prunkvoll'\\\"; \\\"raēvas-čiθra- Adj. 'von reicher Herkunft, von vornehmer Abstammung'\\\"; \\\"raēvas-tama- Adj. 'der reichste'\\\" — raēvas- is the s-stem of 'rich', not a plant name. Bartholomae's Raŋhā appears only in compounds (aoδa- 'Quelle der Raŋhā', gaoša- 'Seitenarm der Raŋhā').\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. roric (KLN_1966.txt line 33106)\", \"stance\": \"supports\", \"note\": \"\\\"Rasa, name of a mythic river (= Avestic Raŋhā), arṣati 'flows' ... prob. also Ῥᾶ, Scythian name of the Volga, fr. I.-E. base *ras-, *eras-, *eres-, *ers-, 'to flow, wet, moisten'.\\\"\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 150 f.\", \"stance\": \"supports\", \"note\": \"footnote there: \\\"rouś, rasa, ros ...\\\" and the summary \\\"Neben diesen Gruppen, die auf einem s-St. *eres- (: ers, ərəs, ṛs), *eros- (ərəs-) beruhen\\\" — the same *eres-/*eros- s-stem base that gives rasā/raŋhā and rōs.\"}]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Pahlavi\",\n \"words\": \"rahg; rag\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Iranian *rahaka- 'vein' gives Middle Persian rag (Book Pahlavi lk', Manichaean rg) and Parthian rahg, the -h- being preserved in Parthian and lost between vowels in Middle Persian with contraction *rahag > rag. Nyberg's glossary has \\\"rag [lk'] vein 605, — MPrs rg (A-H I); Paz. ray, NP rag; MPrth rhg\\\", and Gharib's Sogdian entry cites the same pair (\\\"Parth. rahg; MP rag\\\"). Nourai's only slip is the language label: rahg is Parthian, not Pahlavi in the narrow (Middle Persian) sense — though 'Pahlavi' in the older usage covers both.\",\n \"derivation_fa\": \"*rahaka- ایرانی میانه «رگ» در پارتی به rahg و در فارسی میانه به rag رسیده است؛ پارتی h میان‌واکه‌ای را نگه داشته و فارسی میانه آن را انداخته و *rahag را به rag کوتاه کرده است. نیبرگ در واژه‌نامهٔ خود می‌آورد: «rag [lk'] رگ ...؛ فارسی میانهٔ مانوی rg؛ پازند ray؛ فارسی نو rag؛ پارتی rhg». قریب هم در مدخل سغدیِ rāk همین جفت را می‌آورد. تنها خردهٔ کار نورایی برچسبِ زبان است: rahg پارتی است نه فارسی میانه — هرچند «پهلوی» در کاربرد قدیم هر دو را دربر می‌گیرد. ادعای نورایی در اصل درست است.\",\n \"sources\": [W + \"%D8%B1%DA%AF\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:339\", \"status\": \"supports\", \"note\": \"Gharib entry 8425: \\\"rāk ©<*rahaka-; Av. raŋha; Parth. rahg; MP rag — vein\\\" — both of Nourai's forms, with the reconstruction *rahaka-.\"}],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. rag (NYB_vol2_glossary.txt line 3207)\", \"stance\": \"supports\", \"note\": \"\\\"rag [lk'] vein 605, — MPrs rg (A-H I); Paz. ray, NP rag; MPrth rhg (MHC, v. Gloss.).\\\" — assigns rahg to Parthian, rag to Middle Persian.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD, searched 'rag'\", \"stance\": \"silent\", \"note\": \"no headword rag in the Concise Pahlavi Dictionary text on disk (the word is attested in the Bundahišn anatomy chapters that MacKenzie's short glossary omits).\"}]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Persian\",\n \"words\": \"rag «رگ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP رگ rag 'vein, blood-vessel' continues MP rag unchanged (Book Pahlavi ideogram-free spelling lk', Manichaean rg), from Proto-Iranian *HraháH- (< PII *HrasáH-, PIE *h₁rṓs 'moisture, dew, sap'), so it is the same noun as Vedic rasā́- 'moisture, liquid' and, at one remove, Latin rōs. The 'vein' sense is the old 'channel of fluid' sense of the root. Armenian erak 'vein' is an early Iranian loan from the same word (Hübschmann), which fixes a pre-Sasanian date for the form.\",\n \"derivation_fa\": \"«رگ» فارسی نو بی‌هیچ دگرگونی از rag فارسی میانه مانده است و آن از ایرانی آغازین *HraháH- (< هندوایرانی *HrasáH-، هندواروپایی *h₁rṓs «تری، شبنم، شیره») می‌آید؛ پس همان اسمی است که در ودایی rasā́- «تری، مایع» و با یک واسطه در لاتین rōs «شبنم» دیده می‌شود، و معنای «رگ» همان معنای کهنِ «مجرای مایع» است. ارمنی erak «رگ» وام‌واژه‌ای ایرانی از همین واژه است (هوبشمان)، که کهنگیِ صورت را پیش از دورهٔ ساسانی نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B1%DA%AF\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:339\", \"status\": \"supports\", \"note\": \"Gharib entry 8425 explicitly lists the Middle Persian antecedent 'MP rag' of NP رگ alongside the Sogdian cognate rāk < *rahaka-.\"}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt line 8510)\", \"stance\": \"supports\", \"note\": \"\\\"...rag 'Ader' = arm. erak...\\\" — Armenian erak 'vein' equated with NP rag (an Iranian loan in Armenian).\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. rag\", \"stance\": \"supports\", \"note\": \"\\\"Paz. ray, NP rag\\\" — the direct MP > NP line.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss, searched 'rag'/'Ader'\", \"stance\": \"silent\", \"note\": \"no separate numbered entry for rag found in HRN.txt.\"}]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"rîvand «ريوند (ریواس)»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The word is genuine and the gloss is right: Borhān-e Qāṭeʿ p.991 has \\\"ریوند: به کسر اول و سکون ثانی و فتح ثالث ... دارویی است معروف که اسهال آورد، و به عربی راوند گویند\\\" and, in the next column, \\\"ریواس ... رستنی مشهور\\\". What is disputed is the parent arrow. Nourai derives rīvand from an Avestan raēvas 'rhubarb', but no such Avestan word exists (see node 6); Moʿin's own footnote on that Borhān page connects ریوند only with Av. raēvant- 'rich, splendid' in the personal-name sense (Bīrūnī's بهمن اردشیر ریوند دست 'long-handed'), not with the plant. Modern Iranian etymology takes ریواس from MP rēbās, Proto-Iranian *(h)rabā́š ~ *(h)rabacáh (whence also Arabic رِيبَاس rībās, Uzbek ravoch), and treats ریوند/راوند as its by-form. So the Persian word is the right starting point for the Greek and Latin words below it, but it does not come from Nourai's Avestan etymon.\",\n \"derivation_fa\": \"خودِ واژه اصیل است و معنای آن هم درست: برهان قاطع (ص ۹۹۱) می‌نویسد «ریوند: ... دارویی است معروف که اسهال آورد، و به عربی راوند گویند» و در ستون بعد «ریواس ... رستنی مشهور». آنچه پذیرفتنی نیست پیکانِ بالادست است. نورایی «ریوند» را از raēvas اوستایی «ریواس» می‌گیرد، حال آنکه چنین واژه‌ای در اوستا نیست (نگاه کنید به گرهٔ ۶)؛ حاشیهٔ معین در همان صفحهٔ برهان تنها «ریوند» را در معنای نام خاص با raēvant- «توانگر، باشکوه» می‌سنجد (به گواهِ «بهمن اردشیر ریوندْدست» در الجماهرِ بیرونی)، نه در معنای گیاه. ریشه‌شناسیِ امروزی «ریواس» را از rēbās فارسی میانه و ایرانی آغازین *(h)rabā́š ~ *(h)rabacáh می‌داند (که «ریباس» عربی هم از آن است) و «ریوند/راوند» را گونهٔ همان می‌شمارد. پس واژهٔ فارسی سرچشمهٔ درستِ صورت‌های یونانی و لاتینِ زیرین است، ولی از آن ریشهٔ اوستایی نمی‌آید.\",\n \"sources\": [W + \"%D8%B1%DB%8C%D9%88%D8%A7%D8%B3\", \"https://www.etymonline.com/word/rhubarb\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:991\", \"status\": \"supports\", \"note\": \"Borhān vol. 2, leaf 453 (printed = leaf+538 = 991): \\\"ریوند = به کسر اول و سکون ثانی و فتح ثالث و نون و دال هر دو ساکن. داروی است معروف که اسهال آورد و به عربی راوند گویند\\\"; same page \\\"ریواس: با سین بی‌نقطه، بروزن و معنی ریواج است که رستنی مشهور باشد\\\". Supports the word and the gloss; the footnote there links ریوند only to Av. raēvant- as a personal name.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p.991 with Moʿin's footnote 9\", \"stance\": \"partial\", \"note\": \"as above — Moʿin gives 'ریواج ~ ریوج = ریویز؛ از اوستا raēvant-' for the name, and quotes Bīrūnī's الجماهر on بهمن اردشیر ریوندْدست; nothing connecting the plant to Avestan.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. rhubarb / Rheum / rhapontic (KLN_1966.txt lines 32758, 32780, 32823)\", \"stance\": \"supports\", \"note\": \"\\\"L. rheum, fr. Gk. ῥῆον, ultimately fr. Pers. rewend, 'rhubarb' (whence also Russ. reven')\\\" — Klein takes the Persian word as the ultimate source of the Greek, exactly the direction Nourai draws.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin online (vajehyab/abadis)\", \"stance\": \"silent\", \"note\": \"not consulted for a page-level citation; the 6-vol edition is not digitised and Nourai cites no MON page here.\"}]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Greek\",\n \"words\": \"rha; rhěon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek ῥῆον (rhēon) is the ordinary Greek name of the drug and, per Klein, comes ultimately from Persian rewend (the Middle-Persian/early-New-Persian form of ریوند), taken over through the Pontic-Caspian drug trade; the doublet ῥᾶ (rhā) is, in Klein's words, \\\"a blend of ῥῆον 'rhubarb' with Ῥᾶ, the Scythian name of the Volga\\\", the river down which the root reached the Black Sea (Ptolemy already calls the Volga Ῥᾶ, and Ammianus knows rha as both river and plant). Etymonline agrees: \\\"Rha = rhubarb, possibly connected to Persian rewend ... associated in Greek with Rha, ancient Scythian name of the River Volga\\\".\",\n \"derivation_fa\": \"ῥῆον یونانی نام رایجِ این دارو در یونانی است و بنا بر کلاین سرانجام از فارسی rewend (صورت فارسی میانه/فارسی نوِ آغازینِ «ریوند») گرفته شده و از راه بازرگانیِ دارو در کرانهٔ دریای سیاه و خزر به یونانی رسیده است. گونهٔ دوم، ῥᾶ، به گفتهٔ کلاین «آمیزه‌ای است از ῥῆον با Ῥᾶ، نام سکاییِ ولگا» — همان رودی که ریشهٔ گیاه از آن سو به دریای سیاه می‌آمد؛ بطلمیوس نیز ولگا را Ῥᾶ می‌نامد و آمیانوس هر دو کاربرد را می‌شناسد. اتیمانلاین هم همین را می‌گوید. پس ادعای نورایی درست است، هرچند «ریوند ← ῥᾶ» در واقع دو راهِ درهم‌تنیده است: وام‌گیریِ ῥῆον از فارسی و همانندسازی آن با نام رود.\",\n \"sources\": [\"https://www.etymonline.com/word/rhubarb\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1115\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition p.1115 (the 'rh-' range) — that edition is not available on disk or online in a readable scan; the Watkins IE-roots appendix has no rhubarb article.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. rhubarb and Rheum (KLN_1966.txt lines 32780, 32823)\", \"stance\": \"supports\", \"note\": \"\\\"Rheum, n. ... L., 'rhubarb', fr. Gk. ῥῆον, fr. Pers. rewend, of s.m.\\\"; \\\"ῥᾶ, 'rhubarb', is a blend of ῥῆον, 'rhubarb', with Ῥᾶ, the Scythian name of the Volga\\\".\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Rhubarb (SKT.txt line 16051)\", \"stance\": \"supports\", \"note\": \"\\\"Gk. ῥᾶ βάρβαρον, rhubarb; lit. 'rha of the barbarian country' ... ῥᾶ the rha-plant, rhubarb, which was also called ῥᾶ Ποντικόν; it took its name from the river Rha, the Volga.\\\"\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, not searched for this item\", \"stance\": \"silent\", \"note\": \"Klein and Skeat already cover the chain; no further English dictionary consulted for the Greek link.\"}]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Latin\",\n \"words\": \"rha; rheu-barbarum\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin took over both Greek forms: rhēum (Pliny, Ammianus' rha) as the plant/drug name, and, in Medieval Latin, the calque-compound rheubarbarum ~ rhabarbarum from Greek ῥᾶ βάρβαρον 'foreign rhubarb' (Skeat: \\\"lit. 'rha of the barbarian country'\\\"). Klein notes the double form: \\\"ML. rheubarbarum ... The first element derives fr. L. rheum, fr. Gk. ῥῆον ... Cp. the ML. form rhabarbarum, which comes fr. Gk. ῥᾶ βάρβαρον\\\". The one caveat, which Nourai's box does not mark, is chronological: rheubarbarum is Medieval, not Classical, Latin, and its first vowel was refashioned after rheum; and βάρβαρον here does not go with Nourai's cross-reference ☞Baba but is the ordinary Greek βάρβαρος 'foreign'.\",\n \"derivation_fa\": \"لاتین هر دو صورت یونانی را گرفت: rheum (پلینیوس؛ rha نزد آمیانوس) در معنای گیاه و دارو، و در لاتین سده‌های میانه ترکیبِ rheubarbarum ~ rhabarbarum از یونانیِ ῥᾶ βάρβαρον «ریواسِ بیگانه» (اسکیت: «ریواسِ سرزمین بربر»). کلاین می‌نویسد جزء نخستِ rheubarbarum از rheum لاتین و آن از ῥῆον یونانی است، و صورت rhabarbarum یکسره از ῥᾶ βάρβαρον آمده. تنها نکته‌ای که در نمودار نورایی نیامده تاریخِ آن است: rheubarbarum لاتینِ میانه است نه کلاسیک، و واکهٔ نخستِ آن به قیاسِ rheum بازسازی شده؛ افزون بر این βάρβαρον همان «بربر، بیگانه»ی یونانی است و ربطی به ارجاعِ نورایی به ریشهٔ Baba ندارد.\",\n \"sources\": [\"https://www.etymonline.com/word/rhubarb\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1115\", \"status\": \"not_checked\", \"note\": \"same as node 10: the cited AHD New College page is not accessible; the local Watkins appendix does not treat rhubarb.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. rhubarb (KLN_1966.txt line 32823)\", \"stance\": \"supports\", \"note\": \"\\\"ML. rheubarbarum. The first element in ML. rheubarbarum derives fr. L. rheum, fr. Gk. ῥῆον ... Cp. the ML. form rhabarbarum, which comes fr. Gk. ῥᾶ βάρβαρον, lit. 'foreign rhubarb'.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rhubarb\", \"stance\": \"supports\", \"note\": \"\\\"Low L. rheubarbarum (= rheum barbarum), Gk. ῥᾶ βάρβαρον, rhubarb\\\" — with the explicit 'Low Latin' (i.e. Medieval) label that Nourai omits.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, searched 'rheum'/'rha'\", \"stance\": \"silent\", \"note\": \"no entry: Ernout-Meillet covers Classical Latin and does not treat the Medieval compound.\"}]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"English\",\n \"words\": \"rhubarb\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English rubarbe (late 14c.), from Old/Middle French reubarbe, rubarbe (Modern French rhubarbe), from Medieval Latin rheubarbarum; the -h- was restored in learned spelling and only became standard in the late 18th century. Klein: \\\"ME. rubarbe, fr. MF. reubarbe, rubarbe (F. rhubarbe), fr. ML. rheubarbarum\\\". Nourai's arrow Latin → English is therefore right in substance but skips the French intermediary that both Klein and Skeat make the immediate source.\",\n \"derivation_fa\": \"انگلیسیِ میانه rubarbe (اواخر سدهٔ چهاردهم) از فرانسویِ میانه reubarbe/rubarbe (فرانسویِ امروز rhubarbe) و آن از لاتینِ میانهٔ rheubarbarum؛ حرف h در املای عالمانه بازگردانده شد و تنها از اواخر سدهٔ هجدهم رواج یافت. کلاین می‌نویسد: «ME rubarbe، از MF reubarbe/rubarbe، از ML rheubarbarum». پس پیکانِ «لاتین ← انگلیسی» در اصل درست است، ولی واسطهٔ فرانسوی را که کلاین و اسکیت هر دو خاستگاهِ بی‌واسطه می‌دانند نادیده گرفته است.\",\n \"sources\": [\"https://www.etymonline.com/word/rhubarb\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. rhubarb\", \"stance\": \"supports\", \"note\": \"\\\"ME. rubarbe, fr. MF. reubarbe, rubarbe (F. rhubarbe), fr. ML. rheubarbarum.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rhubarb\", \"stance\": \"supports\", \"note\": \"\\\"(F. — Low L. — Gk.) ME. rubarbe; F. rhubarbe ... Low L. rheubarbarum\\\" — labels the word French-mediated.\"}]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Avestan\",\n \"words\": \"araska\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. arəska- 'envy, grudge' is a ka-derivative of the *eṛes- 'to bear ill will' branch of the root (Skt. irasyáti 'is angry, wishes ill', īrṣyā́- 'envy', Av. arəšyant- 'envious', OE eorsian 'to be angry'). Pokorny lists it at 337 verbatim: \\\"av. arəs-ka- 'Neid', mpers. npers. arask 'Neid, Eifer'\\\", and Walde-Pokorny I 150 has the same string. Nourai's gloss 'enmity' is a shade off — the sources render it 'Neid' = 'envy', which is the gloss he gives the Persian and Sogdian children; but the derivation itself is exactly right and Nourai's page reference is spot-on.\",\n \"derivation_fa\": \"arəska- اوستایی «رشک، بدخواهی» ساختی با پسوند -ka از شاخهٔ *eṛes- «بدخواهی داشتن» همین ریشه است (سنسکریت irasyáti «خشم می‌گیرد، بد می‌خواهد»، īrṣyā́- «رشک»، اوستایی arəšyant- «رشک‌ورز»، انگلیسی کهن eorsian «خشمگین شدن»). پوکورنی در ص ۳۳۷ عیناً می‌نویسد: «av. arəs-ka- 'Neid'، mpers. npers. arask 'Neid, Eifer'»، و والده-پوکورنی (ج ۱ ص ۱۵۰) نیز همین را دارد. تنها خرده آنکه نورایی آن را «دشمنی» ترجمه کرده، حال آنکه منابع «رشک/حسد» می‌آورند — همان معنایی که خودِ او برای فرزندان فارسی و سغدیِ این خانه آورده است. ارجاع صفحهٔ او دقیق است و ادعایش درست.\",\n \"sources\": [PIE_ERS, W + \"%D8%B1%D8%B4%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"POK:337\", \"status\": \"supports\", \"note\": \"Pokorny IEW 337 (POK_01.txt leaf 351), §4 'eṛes-': \\\"ai. irasyáti 'zürnt, will übel' ... av. Partiz. arəšyant- 'neidisch' ... av. arəs-ka- 'Neid', mpers. npers. arask 'Neid, Eifer', tiefstufig av. arəši- 'Neid'\\\" — Nourai's arrow and his page number are exact.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny, Vergl. Wb. Bd. I 150 f.\", \"stance\": \"supports\", \"note\": \"\\\"...ai. irasyáti 'zürnt, will übel, benimmt sich gewalttätig', irasyā́ 'das Übelwollen', av. arəs-ka 'Neid', mp. np. arask 'Neid, Eifer' ... (s. Bartholomae Airan. Wb. 206)\\\".\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 206 (as cited by Walde-Pokorny)\", \"stance\": \"supports\", \"note\": \"WP I 150 refers to Bartholomae AiW 206 for arəska-/arəšyant-; the OCR of BRT.txt at that column is too corrupt to quote directly, but WP's citation and Hübschmann's independent reference to 'zd. araska-' both point there.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib entries 1419 and 1475\", \"stance\": \"supports\", \"note\": \"both Sogdian entries give the etymon as \\\"©Av. araska\\\" — third-party confirmation that the Avestan form is real and means 'envy'.\"}]})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\",\n \"words\": \"arašk, rašk «ارشک ، رَشک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. arəska- gives Middle Persian ʾlyšk' /arēšk/ 'envy' (Pazand arask, Manichaean), whence New Persian ارشک arašk, aphaeretically رشک rašk — the loss of the initial short a- being the ordinary Persian treatment of an unstressed prothetic vowel (cf. ارشک/رشک beside برشک with the preposition ba-). Hübschmann, Persische Studien no. 71, sets this out: \\\"Np. arask 'Neid' (barašk Fird. 1,15,23 mit Praef. ba-) ist die ältere Form zu rašk ... paz. arask (Min. 61 p.16 als Var.), phl. arask ... auf ap. *araska = zd. araska- zurück\\\". Moʿin's footnote in Borhān-e Qāṭeʿ p.952 gives the same chain (= ارشک، اوستا arəska-، پهلوی arēšk). Note the homonym رشک 'nit' (Skt. likṣā́-, cf. Latin ricinus), which Borhān and Wiktionary keep apart and which Nourai rightly does not bring in.\",\n \"derivation_fa\": \"arəska- اوستایی در فارسی میانه arēšk «رشک، حسد» شده (پازند arask) و از آن «ارشک» و با افتادنِ الفِ آغازین «رَشک» فارسی نو پدید آمده است؛ افتادنِ واکهٔ کوتاهِ آغازینِ بی‌تکیه در فارسی قاعده‌مند است (سنجیدنی با «بَرَشک» در فردوسی که پیشوندِ به- آن الف را نگه داشته). هوبشمان در «پژوهش‌های فارسی»، شمارهٔ ۷۱، همین را می‌گوید: «arask فارسی نو صورت کهن‌ترِ rašk است ... پازند arask، پهلوی arask ... به پارسی باستان *araska = اوستایی araska- بازمی‌گردد». حاشیهٔ معین در برهان قاطع (ص ۹۵۲) نیز همین زنجیره را می‌آورد. یادآوری: «رشک» به معنی «تخم شپش» واژه‌ای دیگر است (سنسکریت likṣā́-) که برهان و ویکی‌واژه آن را جدا می‌کنند و نورایی هم به‌درستی وارد این نمودار نکرده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B1%D8%B4%DA%A9\", PIE_ERS],\n \"ref_check\": [\n   {\"ref\": \"BQT:952\", \"status\": \"supports\", \"note\": \"Borhān vol. 2 leaf 413 (printed = leaf+538 = 951-952): headword \\\"رشك = بفتح اول و سکون ثانی و کاف، معروف است که غیرت و حسد باشد\\\", with Moʿin's footnote 6 \\\"= ارشک (ه.م.). اوستا [araska-] پهلوی [arēšk] ... بلوچی ... رک: هوبشمان\\\" (Latin script mangled by the OCR but the structure is unmistakable). Footnote 8 on the same page handles the homonym رشک 'nit' from Old Indian likṣā́.\"}],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 71 (HUB.txt lines 336-341)\", \"stance\": \"supports\", \"note\": \"\\\"Np. arask 'Neid' (barašk Fird. 1, 15, 23 mit Praef. ba-) ist die ältere Form zu rašk ... paz. arask (Min. 61 p.16 als Var.), phl. arask (Gl. and Ind. p.20: arashih) auf ap. *araska = zd. araska- zurück\\\".\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny IEW 337\", \"stance\": \"supports\", \"note\": \"\\\"mpers. npers. arask 'Neid, Eifer'\\\" — Pokorny names the New Persian word itself.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt searched رشک\", \"stance\": \"silent\", \"note\": \"no headword رشک in Aryanpur; the single substring hit (pdf p.89) belongs to the entry اشک/ارس/سرشک 'tear'.\"}]})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Sogdian\",\n \"words\": \"`r`sk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian ʾrʾsk / ʾrsk (Buddhist, Manichaean and Christian Sogdian, entries 1419 and 1475 in Gharib) 'envy' is the direct Sogdian reflex of Av. arəska-, with the prothetic ʾ- kept where Persian later lost it; Gharib lists the Middle Persian and Parthian cognates in the same breath (\\\"MP yrysk\\\", \\\"Parth. rask\\\"), which shows the word across all three Middle Iranian languages. Nourai's page number is exact.\",\n \"derivation_fa\": \"«ʾrʾsk / ʾrsk» سغدی (در سغدیِ بودایی، مانوی و مسیحی؛ مدخل‌های ۱۴۱۹ و ۱۴۷۵ در فرهنگ قریب) «رشک» بازتابِ مستقیمِ araska- اوستایی است؛ سغدی الفِ آغازین را نگه داشته، حال آنکه فارسی نو آن را انداخته و «رشک» ساخته است. قریب در همان مدخل هم‌ریشه‌های فارسی میانه (yrysk) و پارتی (rask) را نیز می‌آورد، که گواهِ حضورِ این واژه در هر سه زبانِ ایرانی میانه است. شمارهٔ صفحه‌ای که نورایی داده دقیق است و ادعای او درست.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:56\", \"status\": \"supports\", \"note\": \"Gharib entry 1419 sits on SOD_pages.txt leaf 122; printed = leaf−66 = 56, i.e. Nourai's page exactly. \\\"1419 ʾrʾsk S — arsk ©<Av. araska; MP yrysk ©nom. -w — envy. Anc. Lett. 5.5\\\"; and entry 1475 \\\"ʾrsk(ʾ) M, B — ar(a)sk (ʾrsq) ©Av. araska; Parth. rask — envy. BBB f63; GMS 368, 526; TSP 2.1075\\\".\"}],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 1419 / 1475 (leaves 122, 124)\", \"stance\": \"supports\", \"note\": \"as above; note the word is attested as early as the Ancient Letters (4th c. CE).\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny IEW 337\", \"stance\": \"partial\", \"note\": \"gives Av. arəska- and MP/NP arask but not the Sogdian form, which Pokorny's Iranian material generally omits.\"}]})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Latin\",\n \"words\": \"ros-maris\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin rōs, rōris 'dew' is the o-grade noun of the root (= Lith. rasà, OCS rosa 'dew', Skt. rasā́- 'moisture'); Watkins puts it under \\\"ers-2. To be wet. Variant form *ros- in Latin rōs, dew: ROSEMARY. [Pok. 2. ere-s- 336.]\\\". The plant-name really does appear in Latin both as rōs marīnus 'sea dew' and, with the genitive, as rōs maris — Skeat notes it is \\\"called ros maris in Ovid\\\", and Klein cites Spanish romero 'rosemary' \\\"fr. L. ros maris\\\". So Nourai's form ros-maris is not a misprint but the attested variant.\",\n \"derivation_fa\": \"rōs، rōris لاتین «شبنم» صورتِ o-پایهٔ همین ریشه است (برابر با rasà لیتوانیایی، rosa اسلاوی کهن، rasā́- سنسکریت «تری»)؛ واتکینز آن را زیر «ers-2 «تر بودن»؛ گونهٔ *ros- در لاتین rōs «شبنم»: ROSEMARY [پوکورنی ص ۳۳۶]» می‌آورد. نامِ گیاه در لاتین هم به‌صورت rōs marīnus «شبنمِ دریا» و هم با اضافهٔ اضافی rōs maris آمده است؛ اسکیت یادآور می‌شود که «اووید آن را ros maris می‌نامد» و کلاین هم romero اسپانیایی را «از لاتین ros maris» می‌گیرد. پس صورتِ ros-maris نزد نورایی غلط چاپی نیست بلکه گونهٔ گواهی‌شده است. ادعای او درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins, AHD IE-roots appendix, entry ers-2 (AHD_watkins1985.txt line 459): \\\"ers-2. To be wet. Variant form *ros- in Latin rōs, dew: ROSEMARY. [Pok. 2. ere-s- 336.]\\\" — Nourai's unpaginated 'AHD' citation is verified against the appendix itself.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. roric and romerillo (KLN_1966.txt lines 33106, 33079)\", \"stance\": \"supports\", \"note\": \"\\\"L. ros, gen. roris, 'dew', which is cogn. with Lith. rasa, OSlav. rosa, 'dew', Ol. rasah 'sap, juice, fluid' ... fr. I.-E. base *ras-, *eras-, *eres-, *ers-, 'to flow, wet, moisten'\\\"; and \\\"Sp. romero, 'rosemary', fr. L. ros maris\\\" — the exact form Nourai prints.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rosemary (SKT.txt lines 16210-16211)\", \"stance\": \"supports\", \"note\": \"\\\"L. rosmarinus, rosmarinum, rosemary, lit. sea-dew; called ros maris in Ovid. — L. ros, dew; marinus, marine.\\\"\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny IEW 336\", \"stance\": \"supports\", \"note\": \"\\\"lat. rōs, rōris 'Tau' (kons. St. mit ursprünglich bloß nominativischer Dehnstufe ō); ... aksl. rosa 'Tau', lit. rasà ds.\\\"\"}]})\n\nnodes.append({\n \"id\": 17, \"lang\": \"English\",\n \"words\": \"Rosemary\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English rosmarine (also Old English rōsmarīnum, a learned borrowing) from Latin rōs marīnus, whence also French romarin. Klein: \\\"rosemary, n. — ME., fr. earlier rosmarine, fr. L. ros marinus (whence also F. romarin), 'rosemary', lit. 'dew of the sea' ... The loss of the -n- in English is due to a confusion of L. marinus with E. Mary.\\\" So the modern spelling is folk-etymological (rose + Mary), a re-analysis that has nothing to do with either the rose or the Virgin — the plant is literally 'sea dew'. Nourai's arrow is correct; the AHD citation is verified through Watkins' entry ers-2, which lists ROSEMARY as the English outcome.\",\n \"derivation_fa\": \"انگلیسیِ میانه rosmarine (و پیش از آن rōsmarīnum در انگلیسی کهن، وامی عالمانه) از لاتین rōs marīnus، که فرانسویِ romarin نیز از همان است. کلاین می‌نویسد: «rosemary از rosmarine کهن‌تر، از لاتین ros marinus «شبنمِ دریا» ... افتادنِ -n- در انگلیسی از آمیختنِ marinus لاتین با نامِ Mary است». پس املای امروزی ریشه‌شناسیِ عامیانه است (rose + Mary) و نه با گُلِ سرخ پیوند دارد و نه با مریم مقدس؛ معنای تحت‌اللفظیِ واژه «شبنمِ دریا»ست. پیکانِ نورایی درست است و ارجاعِ AHD او با مدخلِ ers-2 در پیوستِ واتکینز که ROSEMARY را برآیندِ انگلیسی می‌شمارد راستی‌آزمایی شد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins ers-2 (AHD_watkins1985.txt line 459) names ROSEMARY as the English descendant of Latin rōs.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. rosemary (KLN_1966.txt line 33127)\", \"stance\": \"supports\", \"note\": \"\\\"ME., fr. earlier rosmarine, fr. L. ros marinus (whence also F. romarin), 'rosemary', lit. 'dew of the sea' ... The loss of the -n- in English is due to a confusion of L. marinus with E. Mary.\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Rosemary\", \"stance\": \"supports\", \"note\": \"\\\"M.E. rosmarin. — O.F. rosmarin. — L. rosmarinus ... altered to rosemary (as if for rose of Mary).\\\"\"}]})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Germanic\",\n \"words\": \"rěs\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *rēs- 'rushing, running' is Watkins' own reconstruction under this root, quoted almost verbatim by Nourai: \\\"ers-1. To be in motion. 1. Variant form *rēs- in Germanic *rēs- in Old Norse rās, rushing: RACE-2\\\". Pokorny 336-337 gathers the same material: \\\"anord. rās f. 'Lauf', mndd. rās n. 'heftige Strömung', ags. rǣs m. 'Lauf, Anfall' (engl. race skand. Lw.), mhd. rāsen 'rasen', ags. rǣsan 'anstürmen'\\\", set beside Gk. ἐρωή 'Schwung, Andrang' and Lat. rōrāriī. (Wiktionary now prefers to derive this sub-group from a variant root *h₁reh₁s- 'to rush' rather than from *h₁ers- proper — a refinement, not a refutation.)\",\n \"derivation_fa\": \"*rēs- ژرمنیِ آغازین «تاختن، شتافتن» بازسازیِ خودِ واتکینز زیرِ همین ریشه است و نورایی آن را تقریباً واژه‌به‌واژه آورده: «ers-1 «در جنبش بودن». ۱. گونهٔ *rēs- در ژرمنی، در نورسِ کهن rās «تاخت»: RACE²». پوکورنی (ص ۳۳۶–۳۳۷) همین داده‌ها را گرد آورده است: «نورسِ کهن rās «دویدن»، آلمانیِ میانهٔ پست rās «جریانِ تند»، انگلیسیِ کهن rǣs «دویدن، یورش» (انگلیسیِ race وام‌واژه‌ای اسکاندیناویایی است)»، در کنارِ ἐρωή یونانی «خیز، هجوم» و rōrāriī لاتین. ویکی‌واژه امروز این زیرگروه را به گونهٔ ریشهٔ *h₁reh₁s- «شتافتن» می‌برد نه یکسره به *h₁ers-، که پالایشِ نظر است نه ردِ آن. ادعای نورایی درست است.\",\n \"sources\": [PIE_ERS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins ers-1 (AHD_watkins1985.txt line 458): \\\"ers-1. To be in motion. 1. Variant form *rēs- in Germanic *rēs- in Old Norse rās, rushing: RACE-2. 2. Form *ers-ā- in Latin errāre ... [Pok. 2. ere-s- 336.]\\\" — Nourai's Germanic form and gloss are taken straight from here.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny IEW 336-337 (leaf 350)\", \"stance\": \"supports\", \"note\": \"\\\"anord. rās f. 'Lauf', mndd. rās n. 'heftige Strömung', ags. rǣs m. 'Lauf, Anfall' (engl. race skand. Lw.), mhd. rāsen 'rasen', ags. rǣsan 'anstürmen', anord. rasa 'einherstürzen' ... got. rēs im PN Res-mer\\\".\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. race, n., running (KLN_1966.txt line 31505)\", \"stance\": \"supports\", \"note\": \"\\\"ME. ras, rase, fr. ON. rās, 'running, race', rel. to OE. rǣs, 'running, rush', rǣsan, 'to rush headlong' ... and prob. cognate with Gk. ἐρωή ... L. rorarii, 'light-armed troops', lit. 'runners'.\\\"\"}]})\n\nnodes.append({\n \"id\": 19, \"lang\": \"English\",\n \"words\": \"race\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English race 'a running, a contest of speed' is Middle English ras/rase, borrowed from Old Norse rās 'running, race' in the Scandinavian-contact period (the native Old English cognate rǣs 'a running, rush' died out); Pokorny marks it explicitly \\\"engl. race skand. Lw.\\\" and Klein gives the same. The homonym race 'breed, ethnic group' (16th c., from French race, Italian razza) is a wholly different word and Nourai correctly does not bring it in — his gloss 'compete' pins the right one.\",\n \"derivation_fa\": \"«race» انگلیسی به معنی «دویدن، مسابقهٔ سرعت» از انگلیسیِ میانه ras/rase و آن وام‌واژه‌ای است از نورسِ کهن rās «تاخت، مسابقه» در دورهٔ تماس با اسکاندیناوی‌ها؛ هم‌ریشهٔ بومیِ انگلیسیِ کهن، rǣs «دویدن، یورش»، از میان رفت. پوکورنی صریحاً می‌نویسد «engl. race وام‌واژه‌ای اسکاندیناویایی است» و کلاین نیز همین را می‌گوید. واژهٔ هم‌آواى race به معنی «نژاد» (سدهٔ شانزدهم، از race فرانسوی و razza ایتالیایی) یکسره واژهٔ دیگری است و نورایی به‌درستی آن را وارد نکرده؛ معنایی که او داده («رقابت کردن») همان واژهٔ درست را نشان می‌دهد. ادعای او درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (the parent node carries 'AHD').\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. race, n., running\", \"stance\": \"supports\", \"note\": \"\\\"ME. ras, rase, fr. ON. rās, 'running, race'\\\" — Klein keeps this separate from race 'breed', which he derives from F. race, It. razza.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins ers-1\", \"stance\": \"supports\", \"note\": \"\\\"Old Norse rās, rushing: RACE-2\\\" — the superscript 2 is precisely the 'contest of speed' homonym.\"}]})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Latin\",\n \"words\": \"errâre\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin errāre 'to wander, go astray' comes from *ers-ā- (Proto-Italic *erzāō), with the regular Latin change of intervocalic *-rs- to -rr- by assimilation, exactly parallel to Armenian eṙam 'I boil, am agitated' (< *ersā-yō). Pokorny 337 sets them side by side: \\\"einerseits: lat. errō (*ersā(i)ō) 'irre' (= arm. eṙam), got. airzeis 'irre, verführt', ahd. irri 'irre'\\\". Watkins ers-1 §2 gives \\\"Form *ers-ā- in Latin errāre, to wander: ERR, ERRATIC, ERRATUM, ERRONEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]\\\", and Wiktionary reconstructs the same chain PIE *h₁ers- > *h₁ers-o/h₂- 'erring' > Proto-Italic *erzāō > Latin errō. Both of Nourai's citations here are verified.\",\n \"derivation_fa\": \"errāre لاتین «سرگردان شدن، گمراه شدن» از *ers-ā- (ایتالیکِ آغازین *erzāō) می‌آید؛ خوشهٔ *-rs- میان‌واکه‌ای در لاتین به‌قاعده با همگونی به -rr- بدل شده است، درست همان‌گونه که ارمنی eṙam «می‌جوشم، در جنبش و آشفتگی‌ام» (< *ersā-yō) نشان می‌دهد. پوکورنی (ص ۳۳۷) این دو را کنارِ هم می‌گذارد: «lat. errō (*ersā(i)ō) 'گمراهم' (= arm. eṙam)، got. airzeis 'گمراه'، ahd. irri». واتکینز نیز زیر ers-1 می‌نویسد «گونهٔ *ers-ā- در لاتین errāre: ERR، ERROR، ABERRATION [پوکورنی ۳۳۶]»، و ویکی‌واژه همین زنجیره را بازسازی می‌کند. هر دو ارجاعِ نورایی در این خانه راستی‌آزمایی شد و ادعای او درست است.\",\n \"sources\": [PIE_ERS, \"https://www.etymonline.com/word/error\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins ers-1 §2 (AHD_watkins1985.txt line 458): \\\"Form *ers-ā- in Latin errāre, to wander: ERR, ERRATIC, ERRATUM, ERRONEOUS, ERROR; ABERRATION.\\\"\"},\n   {\"ref\": \"POK:336\", \"status\": \"supports\", \"note\": \"The root entry '2. ere-s-' begins on IEW 336 and the Latin material stands on the following page (337, POK_01.txt leaf 350): \\\"lat. errō (*ersā(i)ō) 'irre' (= arm. eṙam)\\\". Watkins likewise cites '[Pok. 2. ere-s- 336]' for errāre, so Nourai's 336 matches the standard way of citing this article.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 151\", \"stance\": \"supports\", \"note\": \"\\\"...wonach vielleicht auch lat. error nach errāre mit rr ausgestattetes älteres *erōs ist\\\" — WP treats errāre/error under the same *eres-/*eros- s-stem base.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. errō (LAT.txt line 19274)\", \"stance\": \"supports\", \"note\": \"\\\"erro, -as, -aui, -atum, -are: 1° errer, aller à l'aventure ...\\\" with derivatives errātum, errābundus, errāticus — confirms the Latin verb and its meaning (the etymological paragraph is not legible in this OCR).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC, searched 'erso'\", \"stance\": \"partial\", \"note\": \"Mann has 'erskō \\\"go to, reach\\\"' (a different formation) and 'arsien \\\"male\\\"' but no separate *ersā- article; silent on errāre.\"}]})\n\nnodes.append({\n \"id\": 21, \"lang\": \"English\",\n \"words\": \"error\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English error is Middle English errour, from Old French error/errur, from Latin errōrem (nom. error) 'a wandering, straying; uncertainty', the action noun of errāre; the verb err (c. 1300) came in by the same route through Old French errer. Etymonline traces both to \\\"PIE root *ers- 'be in motion, wander around'\\\" and notes the Germanic cognates of the same root that took the 'anger/straying' turn (OE ierre 'angry; straying', OHG irri, Gothic airziþa 'error, deception') — the branch Nourai labels 'Ere 2: to have bad will'.\",\n \"derivation_fa\": \"«error» انگلیسی از انگلیسیِ میانه errour، از فرانسویِ کهن error/errur، و آن از لاتین errōrem (فاعلی error) «سرگردانی، گمراهی؛ تردید» است که اسم‌مصدرِ errāre باشد؛ فعلِ err (حدود ۱۳۰۰ م.) هم از همان راه و از errer فرانسویِ کهن آمده است. اتیمانلاین هر دو را به ریشهٔ هندواروپاییِ *ers- «در جنبش بودن، سرگردان بودن» می‌برد و هم‌ریشه‌های ژرمنیِ همان ریشه را که به معنای «خشم/گمراهی» گراییده‌اند برمی‌شمارد: ierre انگلیسیِ کهن «خشمگین؛ گمراه»، irri آلمانیِ علیای کهن، airziþa گوتی «خطا، فریب» — همان شاخه‌ای که نورایی «Ere 2: بدخواهی داشتن» نامیده است. ادعای او درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/error\"],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node (the parent Latin node carries 'AHD; POK:336').\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins ers-1 §2\", \"stance\": \"supports\", \"note\": \"ERROR is listed among the English descendants of Latin errāre under this root.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, s.v. err/error\", \"stance\": \"supports\", \"note\": \"Klein's entry chain ME errour < OF error < L. errōrem < errāre matches Etymonline; consulted via the same 'roric'-family cross-references and the standard entry.\"}]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Eres 1 / Ersen / Ros / Ers / Ere 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁ers- 'to flow; to be wet; to be in motion, roam' (Pokorny '2. ere-s- (ers-, ṛs-, eṛes-), und res-, ros-', IEW 336-337), with the derivatives *h₁r̥sēn 'male' (Nourai's 'Ersen'), *h₁rṓs / *ros- 'dew' (his 'Ros') and *h₁eres- 'to bear ill will' (his 'Ere 2')\",\n \"note\": \"The five-part root box is a faithful abstract of a single Pokorny article. IEW 336 opens: \\\"2. ere-s- (ers-, ṛs-, eṛes-), und res-, ros- 'fließen; rosā Feuchtigkeit, Tau'; von lebhafter Bewegung überhaupt, auch 'umherirren' und 'aufgebracht, aufgeregt sein'; eṛesiā 'Übelwollen' (S. 337)\\\" — which is exactly Nourai's 'Eres 1: to flow, to be wet' + 'Ros: dew' + 'Ers: to be in motion' + 'Ere 2: to have bad will'; and §2 of the same article, \\\"Wurzelform ers-, ṛs-; ṛsen 'männlich'\\\", is his 'Ersen: ejector of semen, male' (Pokorny even gives the same semantic bridge, 'aus benetzend, Samen ergießend'). Watkins splits the article into ers-1 'to be in motion' and ers-2 'to be wet', both referred back to '[Pok. 2. ere-s- 336]'. Wiktionary's *h₁ers- has 'to flow' and 'to roam, to err', and puts *rēsō/ἐρωή under a variant root *h₁reh₁s-. The language label 'Indo-European' and the glosses are therefore right. TWO caveats, both carried into the nodes below: (a) Nourai's page reference POK:335 is one page early — p.335 of IEW is eregʷ(h)o- 'pea' and erek- 'louse'; the article he is summarising runs 336-337. (b) the 'Ersen' branch as he populates it mixes in the descendants of a genuinely different root, *wers-/*wr̥sēn- 'male' (Pokorny 1169 ff.; Watkins wers-2 'to be wet. Compare ers-2'), which is where Avestan varəšna-, Pahlavi gušn, Persian گشن and Sogdian wšn belong — nodes 3, 4 and 5 of this chart and one word of node 1.\",\n \"note_fa\": \"جعبهٔ پنج‌بخشیِ ریشه در واقع چکیدهٔ وفادارانهٔ یک مدخلِ پوکورنی است. پوکورنی در ص ۳۳۶ چنین آغاز می‌کند: «۲. ere-s- (ers-, ṛs-, eṛes-) و res-, ros- «روان شدن؛ rosā تری، شبنم»؛ به‌طور کلی از جنبشِ تند، و نیز «سرگردان شدن» و «برانگیخته و خشمگین بودن»؛ eṛesiā «بدخواهی» (ص ۳۳۷)» — که دقیقاً برابر است با «Eres 1: جاری شدن، تر بودن»، «Ros: شبنم»، «Ers: در جنبش بودن» و «Ere 2: بدخواهی داشتن» نزد نورایی؛ و بندِ دومِ همان مدخل، «صورتِ ریشه ers-, ṛs-؛ ṛsen «نر»»، همان «Ersen» اوست، حتی با همان پلِ معناییِ «از تر کننده، فروریزندهٔ تخم». واتکینز این مدخل را به ers-1 «در جنبش بودن» و ers-2 «تر بودن» بخش می‌کند و هر دو را به «[پوکورنی، ۲. ere-s-، ص ۳۳۶]» بازمی‌گرداند. ویکی‌واژه نیز *h₁ers- را «روان شدن» و «سرگردان شدن، خطا کردن» معنی می‌کند. پس برچسبِ زبان (هندواروپایی) و معناها درست است. دو نکته اما هست: نخست آنکه ارجاعِ POK:335 یک صفحه زودتر است — صفحهٔ ۳۳۵ به eregʷ(h)o- «نخود» و erek- «شپش» می‌پردازد و مدخلِ موردِ نظر در صفحه‌های ۳۳۶–۳۳۷ است. دوم آنکه شاخهٔ «Ersen» چنان که نورایی پُر کرده، بازماندگانِ ریشهٔ دیگری، یعنی *wers-/*wr̥sēn- «نر» (پوکورنی ص ۱۱۶۹ به بعد)، را نیز در خود جای داده است؛ اوستایی varəšna-، پهلوی gušn، فارسی «گشن» و سغدی wšn به آن ریشه تعلق دارند، نه به این یکی.\",\n \"sources\": [PIE_ERS],\n \"ref_check\": [\n   {\"ref\": \"POK:335\", \"status\": \"partial\", \"note\": \"IEW p.335 (POK_01.txt leaf 348-349) carries 'eregʷ(h)o-, erogʷ(h)o- \\\"Erbse, Hülsenfrucht\\\"', '1. erek- \\\"Laus, Milbe\\\"' and '2. er(e)k-'; the article Nourai abstracts, '2. ere-s- (ers-, ṛs-, eṛes-), und res-, ros-', begins at the top of p.336 (leaf 349) and runs through p.337 (leaves 350-351). One page early; the content is otherwise exactly what he reports, and his node-level citations POK:336 and POK:337 are precise.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 336-337 (POK_01.txt leaves 349-351)\", \"stance\": \"supports\", \"note\": \"\\\"2. ere-s- (ers-, ṛs-, eṛes-), und res-, ros- 'fließen; rosā Feuchtigkeit, Tau'; von lebhafter Bewegung überhaupt, auch 'umherirren' und 'aufgebracht, aufgeregt sein'; eṛesiā 'Übelwollen' (S. 337)\\\"; §2 \\\"Wurzelform ers-, ṛs-; ṛsen 'männlich'\\\"; §4 \\\"eṛes- ... av. arəs-ka- 'Neid', mpers. npers. arask\\\". WP. I 149 ff. is Pokorny's own back-reference.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny, Vergl. Wb. der idg. Sprachen Bd. I 149-151\", \"stance\": \"supports\", \"note\": \"\\\"Neben diesen Gruppen, die auf einem s-St. *eres- (: ers, ərəs, ṛs), *eros- (ərəs-) beruhen (Brugmann Grdr. II²1, 192, wonach vielleicht auch lat. error nach errāre mit rr ausgestattetes älteres *erōs ist)\\\"; with av. arəs-ka, mp./np. arask on the same page and footnote 1 on 'rouś, rasa, ros'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, AHD IE-roots appendix, ers-1 and ers-2 (AHD_watkins1985.txt lines 458-459)\", \"stance\": \"supports\", \"note\": \"\\\"ers-1. To be in motion. 1. Variant form *rēs- in Germanic *rēs- in Old Norse rās, rushing: RACE-2. 2. Form *ers-ā- in Latin errāre ... [Pok. 2. ere-s- 336.]\\\" and \\\"ers-2. To be wet. Variant form *ros- in Latin rōs, dew: ROSEMARY. [Pok. 2. ere-s- 336.]\\\" — three of Nourai's five glosses verbatim.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary, s.v. arsien 'male; manly'\", \"stance\": \"supports\", \"note\": \"\\\"WP I, 150. Cf. uers-, urs- — Av. arsa, aršān-; Arm. arn 'male'; Gk. ársen, árren; Srb. rs 'strength, manly vigour'\\\" — supports the 'Ersen' formation while, like Watkins, flagging *uers-/*urs- as a distinct comparandum.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, s.v. roric (KLN_1966.txt line 33106)\", \"stance\": \"supports\", \"note\": \"\\\"L. ros, gen. roris, 'dew' ... Rasa, name of a mythic river (= Avestic Raŋhā), arṣati 'flows', ṛṣabhāḥ 'bull, steer', Avestic and OPers. arshan, 'man', Hitt. arszi, 'flows', Gk. ἄρσην, ἄρρην 'male' ... prob. also Ῥᾶ, Scythian name of the Volga, fr. I.-E. base *ras-, *eras-, *eres-, *ers-, 'to flow, wet, moisten'. Cp. rasa, romerillo, rosemary ... the first element in rhubarb and the second element in Ahasuerus and in Xerxes.\\\" This single Klein entry contains almost the whole of Nourai's chart and is very probably his model.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dict. of Selected Synonyms, searched 'dew'/'male'\", \"stance\": \"silent\", \"note\": \"the OCR of SYN.txt does not yield the 1.78 'dew' or 15.x 'male' sections cleanly; no usable passage found.\"}],\n \"nodes\": nodes}\n\ndoc = {\n \"pdf_page\": 160,\n \"book_page\": 130,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-160.json', 'w', encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok', len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build160.py",
 "description": "Build page-160.json"
}
```


### [2026-09-05T20:56:11.291Z] TOOL RESULT

```
ok 21
```


## [2026-09-05T20:56:16.336Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-160.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 160",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T20:56:18.101Z] TOOL RESULT

```
JSON OK
nodes verified: 21/21
node verdicts: {'disputed': 6, 'plausible': 2, 'confirmed': 13}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'not_checked': 10, 'partial': 3}
books consulted: {'partial': 7, 'supports': 36, 'silent': 9, 'contradicts': 4} | by book: {'KLN': 11, 'SKT': 5, 'BRT': 4, 'NYB': 4, 'POK': 4, 'BQT': 3, 'ARY': 3, 'PHD': 3, 'SOD': 3, 'WLD': 3, 'IEC': 2, 'MON': 2, 'HRN': 2, 'HUB': 2, 'LAT': 2, 'AHD': 2, 'WEB': 1}
```


## [2026-09-05T20:56:23.351Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-160.json'))\ns=d['entries'][0]['nodes'][8]['words'][0]['script']\nprint(repr(s));print([hex(ord(c)) for c in s])\n\"",
 "description": "Check yeh character in rivand script"
}
```


### [2026-09-05T20:56:25.410Z] TOOL RESULT

```
'ريوند (ریواس)'
['0x631', '0x64a', '0x648', '0x646', '0x62f', '0x20', '0x28', '0x631', '0x6cc', '0x648', '0x627', '0x633', '0x29']
```


## [2026-09-05T20:57:09.497Z] AGENT

Done. `data/verification/page-160.json` written; `verify_check.py 160` reports **0 PROBLEM lines** (21/21 nodes).

**Page 160 (book p.130) — root "Eres 1 / Ersen / Ros / Ers / Ere 2"**

- Root: **confirmed** (1). Nodes: **confirmed 13, plausible 2, disputed 6**.
- ref_checks: 17 supports, 3 partial, 10 not_checked. Books consulted: 36 supports, 7 partial, 4 contradicts, 9 silent (POK, WLD, AHD/Watkins, IEC, KLN, SKT, BRT, NYB, PHD, HRN, HUB, SOD, BQT, FSF, LAT, ARY, MON).

Disputed / problem items:
- **Nodes 3, 4, 5 (Pahl. vušn/gušn, NP گشن gošn/گشنی/گشنسپ, Sogd. wšn)** — words and MP→NP chain all confirmed (MacKenzie, Nyberg, Horn 206, BQT 1821, FSF), but they descend from Old Iranian ***wr̥šan-** (PIE *wers-), not *h₁ers-. Nyberg: "OIr *vṛšna-, cf Skr vṛṣan-, whence *vušn > gušn"; Horn no. 925 derives گشن from Av. varəšni-.
- **Node 1, word `varešna`** — Bartholomae: "Ableit. aus *varšan- 'mas'; ai. vṛ́ṣan-, np. gušan" — same wrong-root problem; and **`aršan-aspa`** is unattested in Bartholomae (the real name is Arjāsp < Av. Arəĵaṱ.aspa 'having valuable horses'). Node marked disputed for those two words; aršan-, xšaya-aršan-, syāva-aršan- are confirmed.
- **Node 6, word `raěvas` "rhubarb"** — Av. raēvas- is the s-stem of raēvant- "rich, splendid" (Bartholomae), not a plant name. The other two words (Raŋhā the river/Volga Ῥᾶ; raŋhā as etymon of "vein") are confirmed by Pokorny 336, Klein and Gharib 8425.
- **Node 9 (rîvand)** — word real (BQT 991) but modern etymology takes ریواس from MP rēbās < PIr *(h)rabā́š, not from Av. raēvas; the Greek/Latin/English chain below it is confirmed (Klein: Gk ῥῆον < Pers. rewend; ῥᾶ blended with the Volga name).
- **Node 2 (plausible)** — خشایار، سیاوش، ارشان confirmed; **ارشاسپ** not attested pre-modern (only in modern name-books).

Reference-page notes for the owner:
- **POK:335 on the root box is one page early** — Pokorny's "2. ere-s-" article is IEW 336–337 (p.335 = 'pea'/'louse'). Nourai's node-level POK:336 and POK:337 are exact, as are SOD:56 / SOD:339 / SOD:414, BQT:952 / 991 / 1821, HRN:206, FSF:297 and both unpaginated AHD citations (verified verbatim in Watkins' ers-1 / ers-2).
- Not checkable: AHD:1480, AHD:1115 (1975/76 New College main word-list, no scan), MON:3329, MON6:1706 (6-vol Moʿin not digitised), FNI:34 (purchase-only). BQT:1119 only partially supports node 2 (سیاوش present at printed ≈1121; ارشان/ارشاسپ absent from Borhān).

Extraction fix for the owner (minor, data only): node 9 script `"ريوند (ریواس)"` uses Arabic yeh U+064A in ريوند while the printed page shows Persian yeh (ریوند) — the parenthesised ریواس already uses U+06CC. Otherwise the JSON matches the printed page exactly (checked against `site/pages/160.jpg`), including "vušn, gushn", "raěvas" and "ros-maris", all of which are faithful to the book.
