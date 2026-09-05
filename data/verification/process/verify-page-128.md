# Verification process log — verify-page-128


## [2026-09-05T20:02:35.036Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 128 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-128.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-128.json. Write /home/sfmqrb/git/rishe/data/verification/page-128.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 128` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:02:36.481Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:02:37.396Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:02:37.466Z] TOOL RESULT

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


## [2026-09-05T20:02:38.027Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-128.txt"
}
```


### [2026-09-05T20:02:38.322Z] TOOL RESULT

```
1	=== PDF page 128 (book page 98) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dher 1 : to hold firmly, keep  (refs POK:252)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:252 | dâr 2, dr : to hold
5	  #2 (parent #1) [Pahlavi] refs=FFD:43,52 | dâštan : to have ; pad-en-dâštan : to take, consider
6	    #3 (parent #2) [Persian] refs=BQT:810; FFD:43 | -dâr 3 «ـدار ۳» : a suffix meaning owner, holder ; dâštan «داشتن» : to have, own ; pendâštan «پنداشتن» : to think, consider | extra: پندار
7	  #4 (parent #1) [Persian] refs=BQT:840; HRN:116,123 | darmân «درمان» : cure ; dârŭ «دارو» : medicine | NOTE: ETM:65 suggests a different root for "dârŭ:medicine". See Deru 1
8	  #5 (parent #1) [Avestan] refs=BQT:1055; HRN:117 | zaenô-hara : hold your weapon, beware ☞Ghei 2
9	    #6 (parent #5) [Persian] refs=BQT:1055 | zenhâr «زنهار» : beware | extra: زینهار
10	#7 (parent #0) [Avestan] refs=POK:252,258 | dereza : to hold together, close, tighten
11	  #8 (parent #7) [Persian] refs=HRN:122; CEL3:254; MON:1510 | darz «درز» : seam ; darzî «درزی» : tailor ; darzmân «درزمان» : thread ; darzan «درزن» : needle | extra: درزه
12	  #9 (parent #7) [Avestan] refs=BQT:170; HRN:122 | han-dareza : pull together, unite, fortify ☞Sem 1
13	    #10 (parent #9) [Persian] refs=BQT:170 | andarz «اندرز» : advice
14	#11 (parent #0) [Old Persian] refs=AHD:335 | dâr : to hold ; dârayat-vahu : he holds goodness ☞Su 1
15	  #12 (parent #11) [Persian] refs=BQT:813; TZF:13 | Dârîuš «داریوش» : Darius, king of Persia ; dârâbgard «دارابگرد» : "city of Dârâb" ☞Kwer | extra: دارا ، داراب
16	#13 (parent #0) [Sogdian] refs=SOD:135 | d`r : to hold, have
17	#14 (parent #0) [Sanskrit] refs=POK:252 | dhar : to hold, keep ; bhaga-dhara : holder of happiness ☞Bhag
18	  #15 (parent #14) [Hindustani] refs=HJB:49; KLN:140 | bahaudur : a title of respect in India
19	    #16 (parent #15) [Mongolian] refs=HJB | bahâdŭr : brave
20	      #17 (parent #16) [Persian] refs=HJB:49; BQT; MON | bahâdor «بهادر» : brave
21	#18 (parent #0) [Latin] refs=AHD | firmus : firm, strong
22	  #19 (parent #18) [English] refs=AHD | firm, farm, confirm
23	#20 (parent #0) [Greek] refs=AHD | thornus : support, seat
24	  #21 (parent #20) [English] refs=None | throne
25	
```


## [2026-09-05T20:02:41.586Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-128.json",
 "description": "Read source JSON for page 128"
}
```


### [2026-09-05T20:02:41.636Z] TOOL RESULT

```
{
  "pdf_page": 128,
  "book_page": 98,
  "entries": [
    {
      "root": {
        "name": "Dher 1",
        "lang": "Indo-European",
        "refs": "POK:252",
        "gloss": "to hold firmly, keep"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:252",
          "words": [
            {"translit": "dâr 2, dr", "gloss": "to hold", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:43,52",
          "words": [
            {"translit": "dâštan", "gloss": "to have", "script": null},
            {"translit": "pad-en-dâštan", "gloss": "to take, consider", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:810; FFD:43",
          "words": [
            {"translit": "-dâr 3", "gloss": "a suffix meaning owner, holder", "script": "ـدار ۳"},
            {"translit": "dâštan", "gloss": "to have, own", "script": "داشتن"},
            {"translit": "pendâštan", "gloss": "to think, consider", "script": "پنداشتن"}
          ],
          "script_extra": "پندار",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:840; HRN:116,123",
          "words": [
            {"translit": "darmân", "gloss": "cure", "script": "درمان"},
            {"translit": "dârŭ", "gloss": "medicine", "script": "دارو"}
          ],
          "note": "ETM:65 suggests a different root for \"dârŭ:medicine\". See Deru 1",
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:1055; HRN:117",
          "words": [
            {"translit": "zaenô-hara", "gloss": "hold your weapon, beware", "script": null, "see": ["Ghei 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1055",
          "words": [
            {"translit": "zenhâr", "gloss": "beware", "script": "زنهار"}
          ],
          "script_extra": "زینهار",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:252,258",
          "words": [
            {"translit": "dereza", "gloss": "to hold together, close, tighten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "HRN:122; CEL3:254; MON:1510",
          "words": [
            {"translit": "darz", "gloss": "seam", "script": "درز"},
            {"translit": "darzî", "gloss": "tailor", "script": "درزی"},
            {"translit": "darzmân", "gloss": "thread", "script": "درزمان"},
            {"translit": "darzan", "gloss": "needle", "script": "درزن"}
          ],
          "script_extra": "درزه",
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Avestan",
          "refs": "BQT:170; HRN:122",
          "words": [
            {"translit": "han-dareza", "gloss": "pull together, unite, fortify", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:170",
          "words": [
            {"translit": "andarz", "gloss": "advice", "script": "اندرز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "AHD:335",
          "words": [
            {"translit": "dâr", "gloss": "to hold", "script": null},
            {"translit": "dârayat-vahu", "gloss": "he holds goodness", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "BQT:813; TZF:13",
          "words": [
            {"translit": "Dârîuš", "gloss": "Darius, king of Persia", "script": "داریوش"},
            {"translit": "dârâbgard", "gloss": "\"city of Dârâb\"", "script": "دارابگرد", "see": ["Kwer"]}
          ],
          "script_extra": "دارا ، داراب",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:135",
          "words": [
            {"translit": "d`r", "gloss": "to hold, have", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:252",
          "words": [
            {"translit": "dhar", "gloss": "to hold, keep", "script": null},
            {"translit": "bhaga-dhara", "gloss": "holder of happiness", "script": null, "see": ["Bhag"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Hindustani",
          "refs": "HJB:49; KLN:140",
          "words": [
            {"translit": "bahaudur", "gloss": "a title of respect in India", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Mongolian",
          "refs": "HJB",
          "words": [
            {"translit": "bahâdŭr", "gloss": "brave", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "HJB:49; BQT; MON",
          "words": [
            {"translit": "bahâdor", "gloss": "brave", "script": "بهادر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "firmus", "gloss": "firm, strong", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "firm, farm, confirm", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "thornus", "gloss": "support, seat", "script": null}
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
            {"translit": "throne", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:02:42.202Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:02:42.252Z] TOOL RESULT

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


## [2026-09-05T20:03:08.020Z] TOOL CALL #5: Bash

```json
{
 "command": "ls tools/ && sed -n '1,60p' tools/verify_check.py && echo ---- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'));print(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\"",
 "description": "Inspect verify_check and prior page format"
}
```


### [2026-09-05T20:03:09.911Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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
----
{"entry": 0, "root": "Dhem", "verdict": "confirmed", "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'", "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.", "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.", "sources": ["https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86", "https://en.wiktionary.org/wiki/%D8%AF%D9%85"], "ref_check": [{"ref": "POK:247", "status": "supports", "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."}], "consulted": [{"src": "WLD", "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)", "stance": "supports", "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."}, {"src": "CHEUNG", "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)", "stance": "supports", "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"}, {"src": "AHD", "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)", "stance": "silent", "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."}, {"src": "IEC", "where": "Mann, d-section (grep 'dhem' in IEC.txt)", "stance": "silent", "note": "Mann has dhen
```


## [2026-09-05T20:03:10.084Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FFD','BQT','HRN','CEL3','MON','AHD','TZF','SOD','HJB','KLN','ETM','SIN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-05T20:03:11.829Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

CEL3 null

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadab

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo
```


## [2026-09-05T20:03:17.827Z] TOOL CALL #7: Bash

```json
{
 "command": "ls site/pages/128.jpg 2>/dev/null; pdftoppm -f 128 -l 128 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg128\" 2>&1 | head; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null",
 "description": "Render printed page 128"
}
```


## [2026-09-05T20:03:18.170Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dher-\" POK_01.txt | head -40",
 "description": "Grep Pokorny for dher-"
}
```


### [2026-09-05T20:03:20.102Z] TOOL RESULT

```
site/pages/128.jpg
Could not write image to /pg128.png; exiting
total 8
drwx------ 2 sfmqrb sfmqrb 4096 Sep  5 16:01 .
drwx------ 4 sfmqrb sfmqrb 4096 Sep  5 16:02 ..
```


### [2026-09-05T20:03:20.144Z] TOOL RESULT

```
568:andher-,  näher-  ,Spitze,  Stengel^. .  Nur  griechisch:  äd-riQ  ,Hachel  an  der  Ähre,  Lanzenspitze^,  ävSeqi^ , Halmspitze,  Halm^,  dy-9-soiy.og  ,Halm,  StengeP,  dvd-SQSwv  ,Kinn^  als  ,bärtige, struppige  Stelle^,  dyi}oLay.og  ,der  gemeine  KerbeP,  benannt  nach  seinen stachligen  Früchten,  (Jv^^»?^^;;,  dvdQ7]d(bv  ,Wespe,  Waldbiene^,  Wortausgan g nach  TEvd-Qrjvrj  ,Hornis^,  Tav-d-qr^dibv  ,Wespe'^  (hierher  vielleicht  ävd-QCjnog aus  *äv^QO-a)7iog  .mit  bcärtigem  Gesicht  =  Mann^,  dann  ,Mensch^,  Güntert Heidelberg.  SB.  1915,  Abb.  X?;  vgl.  auch  Schwyzer  Gr.  Gr.  I  426^ Nach  Kretschmer  Gl.  28,  246  aus  ^avdg-WTiög,  der  Spiritus  asper  von ögacü  usw.  übertragen?);  ob  auch  dd-dgr]  (^dO-aoßä),  dd-rjoä  ,Weizenmehl- brei,  Speltgraupen^  (von  Plin.  n.  h.  22,  121  allerdings  als  ägypt.  Wort bezeichnet)?
2931:Die  kelt.;,  tochar.  und  baltoslav.  Worte  könnten  auch  zu  3.  dher-  gehöre
3106:halt,  drittel-  ^stark^  (=  gallorom.  *drüto-s,  g-r.  PN  Jqvtwv)  in  lit.  drutaSj drlütas  ;Stark;  dick^,  apr.  im  PN  Drutemie,  ON  Druthayn,  DvuthelaukPM] o-ehört  zu  apr.  druicis  m.  ^Glaube^^  druiui  L,  drmvlt  ^glauben*  (*druweti: ahd.  trüen),  na-po-druwisnan  ^Vertrauen^  Hoffnung^  Neben  lit.  drütas  aucli drüktas;  s.  unter  2.  dher-.
3570:..  dber-,  dherg-  in  kons.  Erweiterungen  .trüber  Bodensatz  einer  Flüssig- keit, auch  allgemeiner  von  Schmutz,  Widerlichkeit,  von  quatschigem Wetter,  von  trüben  Farbentünen  usw.;  verbal:  Bodensatz  und  Schlamm aufrühren,  trübend  Ursprüngl.  eins  mit  dher-  ,Unrat,  cacare^
3592:2.  dher-,  dhero-  ,halten,  festhalten,  stützen'.
3646:^,  dher-,  dhereu-,  dhrBn-  Schallwurzel  , murren,  brummen,  dröhnen'.
3666:5.  dher-,  dhrei-d-  ,Unrat,  cacäre'  (ob  verwandt  mit  1.  dher- , trüber  Boden-
3667:satz' und  4.  dher-?).
3943:got.    drauhsnös    f.  PI.  ,Brocken,    Brosamen';    wohl    als    Umstellung    aus  % *dkrüs-kna    mit    halt,   drushi    nächst   verknüpf  bar;    Einmischung   eines  zu  ' nhd.  trocken,  ags.  dreahnian  —  s.  2.  dher-,  dhreugh-  ,halten'  —  gehörigen. Wortes   würde   allenfalls    beide   überlieferten   Formen  als  wirklich  gespro- chene zu  betrachten  gestatten;  aber  vgl.  daneben  got.  drausnös  ds. ;  —
```


## [2026-09-05T20:03:28.668Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3592,3600p' POK_01.txt && echo \"=== POK_full search ===\" && grep -n \"dher-2\\|dher-\\s*2\\|halten, festhalten\" POK_full.txt | head -20",
 "description": "Read Pokorny dher-2 entry"
}
```


### [2026-09-05T20:03:28.744Z] TOOL RESULT

```
2.  dher-,  dhero-  ,halten,  festhalten,  stützen'.
Ai.  dhar-  ,halten,  tragen,  stützen,  erhalten,  aufrecht  halten'  (Präs.  meist dhärdyati]  Perf.  dadhära,  dadhri]  dhj-td-:  dhdrtum)  Pass.  ,zurückgehalten werden,  fest  sein,  sich  ruhig  verhalten',  av.  dar-  ,halten,  festhalten,  zu- rückhalten; woran  festhalten,  es  beobachten  (ein  Gesetz);  fest  im  Ge- dächtnis halten;  mit  den  Sinnen  auffassen,  vernehmen;  sich  aufhalten, weilen'  (därayeiti  usw.,  Partiz.  dardta-),  ap.  därayämiy  ,halte',  npers.  Inf. dästan^  osset.  Inf.  dai-iin,  daryWj
ai.  dhdrana-  ,tragend,  erhaltend',  dliarüna-  , haltend,  stützend;  n.  Grund- lage, Stütze',  dhärana-  ,haltend;  n.  das  Halten,  Zurückhalten' =  av.  därana- n.  ,Mittel  zum  Zurückhalten',  ai.  dhartdr-  und  dhdntar-  m.  ,Halter', dharitrl  ,Trägerin',  dhartrd-  n.  ,Halt,  Stütze'  .=  av.  darddra-  n.  ,das Festhalten,  Begreifen',  ai.  dhdrma-  (=  Isit.  firmus)  m.  , Satzung,  Sitte,  Recht, Gesetz',  dharmän-  m.  ,Halter',  dhdrman-  n.  ,Halt,  Stütze,  Gesetz,  Brauch', dhdrlmani  Lok.  ,nach  der  Satzung,  nach  Brauch',  dhäraka-  ^haltend;  m. Behälter',  dhrti-  f.  ,das  Festhalten,  Entschlossenheit',  dx-dhr-d-  ,festhaltend',
253
Ahrl  (oder  sadhrlm)    Adv.    ;,auf    eia    Ziel   hinhaltend,   einem    Ziele   zu%
ji^^'m-anc-  ;nach  einem  Ziele  hin  gerichtet,  vereint,  zusammen';  didhlHä ^*     Vbsicht  zu  stützen",  av.  dldardsatä  ,er  schickt  sich  an^;
über  ai.  cZÄiVa-  ,fest^  s.  Wackernagel  Ai.  Gr.  I  25;
arm.  vielleicht  c^ac^ar  (redupl.)  , Aufenthalt,  Ruhe^  (,*Einhalten^,  vgl.  die Bed.  ,weilen,  sich  ruhig  verhalten^,  dadarem  ,nehme  ab  (vom  Wind)^,
1  ^^  ags.  darian  ,latere^,  ndl.  bedaren  ,ruhig  werden  (vom  Wind,  Wetter)^;
=== POK_full search ===
```


## [2026-09-05T20:03:30.055Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dherāgh\\|dheragh\\|dhergh\\|dereg\\|dərəz\\|darəz\" POK_full.txt POK_01.txt POK_02.txt 2>/dev/null | head -30",
 "description": "Grep Pokorny for dhergh"
}
```


### [2026-09-05T20:03:30.121Z] TOOL RESULT

```
POK_01.txt:3003:dereg- :
POK_01.txt:3008:deregh'  (s.  Persson  Wzerw.  26,  Berneker  254  und  212  m.  Lit.) ;
POK_01.txt:3701:Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
POK_full.txt:19100:dereg- : 
POK_full.txt:19112:deregh-{see Persson root extension 26, Berneker254 and 212 m. Lithuanian): 
POK_full.txt:20641:Maybe alb. Geg {dheragh-) terhek^'QuW, drag' : Polish targac ' carry ' [common alb. -g- > -
```


## [2026-09-05T20:03:46.361Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=3592 && NR<=3720' POK_01.txt | grep -n \"^\\s*25[5-9]\\s*$\\|^\\s*26[0-2]\\s*$\" ; echo \"--- headwords near\"; awk 'NR>=3592 && NR<=3760' POK_01.txt | grep -n \"^[0-9]*\\.\\?\\s*dh\" | head -30",
 "description": "Locate Pokorny pages 255-260"
}
```


### [2026-09-05T20:03:48.017Z] TOOL RESULT

```
48:255
64:256
84:257
117:259
--- headwords near
1:2.  dher-,  dhero-  ,halten,  festhalten,  stützen'.
36:dheregh'  _,halten,  festlialten;  fest':
40:dheregh'  ,festhalten,  fest':
46:dhereugh-r
49:1.  dhreugh-  gehören   ags.  dryge  , trocken',   drtahnian  .austrocknen,  seihen _  mit  h  statt  ^?  — ,  anord.  draugr  ^verdorrter  Baumstamm',  ahd.  truchan .trocken') ;
60:dhren-:
75:5.  dher-,  dhrei-d-  ,Unrat,  cacäre'  (ob  verwandt  mit  1.  dher- , trüber  Boden-
95:dherebh'  , gerinnen,  gerinnen  machen,  ballen,  dickflüssig'.
104:dheregh-  mit  Formans  -(e)s-  und  -no-  in  Namen  beerentragender  strau- chiger Pflanzen,  bes.  auch  von  solchen  Dornsträuchern,  woraus  z.  t1 ,Dorn'?    Zweifelhafte  Gleichung.
112:dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
154:4.  dheu-,  dheuO'  (vermutlich:  dhue-,  vgl.  dio  Erw.  dhue-k-,  dhä-s-)  ,stieben, wirbeln,  bes.  von  Staub,  Rauch,  Dampf;  wehen,  blasen,  Hauch,  Atem; daher  dampfen,  ausdünsten,  riechen,  stinken;  stürmen,  in  heftiger, wallender  Bewegung  sein,  auch  seelisch;  in  heftige,  wirbelnde  Bewe- gung versetzen,  schütteln';  Nominalbildungen:  dhü-li-,  dhü-mo-.
```


## [2026-09-05T20:03:48.754Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"darəz\\|darez\\|dar\\^ez\\|dräjaya\\|drazh\\|handarəz\\|handarez\\|hSndarez\" BRT.txt | head -30; echo \"=== BRT dar- ===\"; grep -n \"1\\. dar-\\|dar- \\[1\\]\" BRT.txt | head",
 "description": "Grep Bartholomae for darez"
}
```


### [2026-09-05T20:03:48.828Z] TOOL RESULT

```
=== BRT dar- ===
```


## [2026-09-05T20:03:57.132Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== p256 region (dheregh halten) ===\"; sed -n '3624,3640p' POK_01.txt; echo; echo \"=== p258 region (dheregh drehen) ===\"; sed -n '3695,3712p' POK_01.txt",
 "description": "Read Pokorny dheregh entries"
}
```


### [2026-09-05T20:03:57.188Z] TOOL RESULT

```
=== p256 region (dheregh halten) ===
vielleicht  mit  Formans  -go- :  lett.  därgs  ^teuer,  kostbar*^,  aksl.  dragz russ.  dörog,  skr.  dräg  ds.;
hitt.  tar-ah-zi  {tarhzi)  ^kanri;,  besiegt'  (*dhT'-?)  gebort  eher  zu  4.  ter^
Gutturalerweiterungen:
dheregh'  _,halten,  festlialten;  fest':
Av.  drazaite,  Inf.  dräjaidhe  ^»halten,  an  sich  halten,  führen',  upadar zuvainti  ,sie  halten  durch  =  setzen  durch,  bringen  fertig',  wozu  ai.  -dhrk. (nur  Nom.)  in  Kompositis  ,tragend';  diese  Form  (*dhrgh-s)  zeugt  für  Anlaut dh-  der  ar.  -und  daher  wohl  auch  slav.  Sippe;
aksl.    drbzOj    dr^zati  ,halten,   innehaben'   (usw.,  s.  Berueker  2ö8);   r^gg drogd  , Wagenbaum,  Verbindungsstange  der  Vorder-  und  Hinterachse  dos Wagens',  Dem.  drözki  PL  ,leichter,  kurzer  Wagen',  daher  nhd.  Droschke,
Als  nasalierte  Formen  dazu  av.  dranjaUi  , festigt,  kräftigt,  bestärkt' ä-drdnjayeiti  ,setzt  fest',  Desiderativ  didrayzaite  ,sucht  für  sich  zu  sichern^' Partiz.  draxta-'^  auch  av.  drdnjayeitij  dädräjöU,  Partiz.  draxta-  ,auswendi<^ lernen,  memorierend  Gebete  murmeln'  (vgl.  ksl.  ivriditi  ,festmachen' : russ.  tverdith  ,aus wendig  lernen');  mir.  dringid  ,er  ersteigt',  dreimm  ,Er- klimmen'  (,*sich  festhaltend  klettern');  kymr.  dringo  ,steigen,  klettern'* anord.  drangr  ,hoher  Fels',  drengr  (*drangja-)  ,dicker  Stock,  Säule'  (und übertr.  ,junger  Mann'),  aksl.  drggz  ,Stange,  Schlagbaum';  anders  Specht Dekl.  139.
dheregh'  ,festhalten,  fest':
ai.  dfhyati,  dfmhati  (d^mhäti)  ,macht  fest',  Partiz.  dj-dhd-  ,fest',  drahydt- ,tüchtig',  av.  dar9zayeiti , bindet  fest,  fesselt',  Desid.  dlddvdzaiti^  dardza-  m. ,das  Befestigen,  Binden,  Fassen,  Greifen',  ddrdz-  f.  , Bande,  Fessel',  ddrdzra- ,fest',  wohl  auch  npers.  darz  ,Naht'  und  ähnliche  iran.  Wörter  für  ,Faden nähen';
thrak.  GN  Darzales]
wahrscheinlich  lit.  dirzas  ,Riemen',  difzmas  ,stark',  apr.  dlrstlan  ,kräftig, stattlich',  dirz-tü,  difzti  ,zäh,  hart  werden';
lit.  dafzas  ,Garten',  lett.  därz  , Garten,  Hof,  Einfriedigung'  kaum  aus *zardas  (vgl.  lit.  zardis  , Roßgarten',  zdrdas  , Hürde')  umgestellt  (anders Mühlenbach-Endzelin  I  448  f.),  sondern  zu  dirzas  (oben)  und  ahd.  zarge, mhd.  zarge  f.  , Seiteneinfassung  eines  Raumes,  Rand';
slav.  *dhrz^  ,kühn,  verwegen'  in  aksl.  dl^z^J  sloven,  drz,  cech.  drzyy russ.  derzkij  ds.  und  aksl.  di-ozn^j  drbzn^ti  ,sich  erkühnen,  wagen',  russ. derznüth  usw.
dhereugh-r
awnord.  driügr  ,aushaltend,  stark,  voll',  driügum  ,sehr',  aschw.  drygher , ansehnlich,    stark,    groß',    nordfries.    dreegh    ,fest,    ausdauernd'   (aber  zu
255
1.  dhreugh-  gehören   ags.  dryge  , trocken',   drtahnian  .austrocknen,  seihen _  mit  h  statt  ^?  — ,  anord.  draugr  ^verdorrter  Baumstamm',  ahd.  truchan .trocken') ;

=== p258 region (dheregh drehen) ===
dheregh-  mit  Formans  -(e)s-  und  -no-  in  Namen  beerentragender  strau- chiger Pflanzen,  bes.  auch  von  solchen  Dornsträuchern,  woraus  z.  t1 ,Dorn'?    Zweifelhafte  Gleichung.
Ai.  dräksä  ,Weintraube';
gallorom.  *dragenos  ,Dorn*,  air.  draigen  m.  , Schlehdorn*,  cymr.  drae^ m.,  nbret.  di^ean  , Dornstrauch'  (kelt.  "^drageno-  aus  *dhr^gli-)'^
vielleicht  auch  ahd.  tirn-pauma  ,cornea  silva*,  tyrn,  dirnhaum  ,cornus*^^ nhd.  dial.  di(e)rle,  dirnlein  ,Kornelkirsche',  Schweiz,  tierlij  falls  nicht! aus  dem  Slav.  in  sehr  alter  Zeit  entlehnt;
lit.  dngnes  PL,  lett.  drigenes  ,schwarzes  Bilsenkraut'  (vgl.  Mühlenbach-1 Endzelin  I  498),    falls  nicht  aus  dem  Slav.  entlehnt;
russ.  dereuj  deren  , Hartriegel,  Kornelkirsche',  skr.  drijen,  öech.  drin  ds. poln.  (alt)  drzon  jBerberitze',  kaschub.  drbn  , Dornen',  polab.  dren  ,Dorn'.
Germ.-sl.  Grundf.    kann   "^dherghno-   sein    und    stünde    dem   freilich   in seiner   Bed.    , Schößling,    Zweig',    PL  ,junges    Gebüsch'    erheblich    anders- gefärbten gr.  TQ€xyog  (Hes.,  anthoL),  tsqxvoq  (Maximus),  kypr.  t«  zsQxvija  ^  • sehr  nahe.
WP.  I  862  f.,  Pedersen  KG.  I  97,  M.-L.  2762.
dheregh-  {dhrgh-nä-)  , drehen,  winden,  wenden'  (auch  , spinnen,  nähen*).
Npers.  darz,  darza  ,Naht*,  darzmän,  darznän  , Faden*,  darzan  ,NadelV pehl.  darzik  , Schneider';
arm.  dafnam  (*darjnam),  Aor.  darjay  ,sich  wenden,  sich  drehen,  sich kehren;  zurückkehren*,  dafn  , bitter,  herbe*  (vgl.  oivog  zgerrsTac  u.  dgl.), darj  jWendung,  Umkehr,  Rückkehr*,  Kaus.  darjucanem  ,verto,  averto, converto,  reddo*;
alb.  dreth  (St.  *dredh-),  Aor.  drodha  ,umdrehen,  zusammendrehen, zwirnen,  spinnen*,  alb.-skutar.  nnrize  ,Windel*  (n-dred-ze)-  nach  Pedersen Hitt.  123,  125,  Toch.  Spracbg.  20  hierher  hitt.  tar-na-ah-hi  ,ich  stecke ein,  lasse  hinein*,  toch.  A  tärnä-,  tärk-,  Prät.  A  cärk,  B  carka  , lassen, entlassen'  (?).
WP.  I  863,  Liden  Arm.  St.  101  ff.,  Meillet  Esquisse^  111,  Kuiper  Nasal- präs. 151.  '^^
259
dbers'  , wagen,  kühn  sein',  älter  ,angreifen,  losgehen*  (auch  mit  -i-,  -u- erweitert).
Ai.  dhrs-nö-ti,  dhdrs-ati  ,ist  dreist,  mutig,  wagt',  ährsü-  (Gramm.),  dhrsat Jierzhaft'  (=  av.  dard^at),  dhrsnii-  ,kühn,  tapfer,  mutig,  dreist,  frech', dhfstd-  ,keck,  frech',  dhfsüa-  ,kühn,  mutig',  dädhrsi-  ,beherzt,  kühn',  mit Objekt  dharsayati  ,wagt  sich  an,  vergreift  sich,  bewältigt',  dharsana-  n. , Angriff,  Mißhandlung',  dharsaka-  ,angreifend,  über  etwas  herfallend';  av. darsam  Adv.  ,heftig,  sehr',  darsi-,  darsyu-,  darsita-  ,kühn',  apers.  adar^- nau§  ,er  wagte',  dädarsi-  EN;
gr.  lesb.  -d-sgaog  n.  ,Mut,  Kühnheit'  (hom.  QsgalTrjg  ,Frechling'),  mit aus  dem  Adj.  verschleppter  Tief  stufe  ion.  altatt.  d^ccQOog  (att.  ^agoog)  ds., att.  d-gdaog  n.  ,Mut,  Kühnheit;  Verwegenheit,  Frechheit',  d-aqüeu),  d^aggeo) ,bin  mutig',  S-agavg  (rhod.  QaQGvßiog,  ther.  Qhagvfxaqhog),  d-gaavg  ,kühn, mutig;  verwegen,  frech'  (=  ai.  dlifsu-),  lesb.  Adv.  -S^goaecjg,  Mgavvog mutig,  getrost,  vertrauend'  (*-9-ag(To-avvog)]
lat.  infestus  , feindlich*,  infestäre  , feindlich  behandeln,  angreifen'  und manifestus   , handgreiflich,   auf  der  Tat  ertappt;    offenkundig'   (*dhers-to-)]
```


## [2026-09-05T20:03:58.832Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 BRT.txt; echo; echo \"=== search darez variants ===\"; grep -n -i \"dar\\.z\\|dsrez\\|darez\\|d3r3z\" BRT.txt | head -20",
 "description": "Inspect BRT.txt format"
}
```


### [2026-09-05T20:03:58.894Z] TOOL RESULT

```
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  
=== search darez variants ===
12956:mit  3  'fesseln':  HltryB  .  .  avqm  pairi- kam  adafTtayäti  bibdailla  . .  vUpabäailla .  .  ya^a  hataanm  narqm  Bim  narvm adarstaySit  Yt.  Ä  55.  Undeutlich  ;/ii«r- yqm  htm  vanm  *ad3r3zaySii  hg .  .  N.j". joit/ra  und  nT  'festmachen  sva.  unschäd- lich machen' :  aitahmaiat  nidanzaym  (sd.) fra  kimcil  nidamaym  ".  .  (so)  sollen  sie ihn  (den  Hund)  unschä<9ich  machen"  V. 13'  31-
```


## [2026-09-05T20:04:21.840Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD dher ===\"; grep -n \"dher-\\|dhergh\\|dher\\b\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for dher"
}
```


### [2026-09-05T20:04:21.886Z] TOOL RESULT

```
=== AHD dher ===
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
376:dher-'
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
378:dher-2
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
384:dhgvher-. To run. Perhaps Greek phtheir, louse: (ICH), PHTHIRIASIS. [Pok. g¥hdher- 487.]
773:ndher-. Under. 1. Germanic *under- in Old English under, under: UNDER. 2. Latin inferus, lower: INFERIOR. 3. Latin infernus, lower: INFERNAL, (INFERNO). 4. Latin infra, below: INFRA-. [Pok. ndhos 771.]
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivatives statira, height, stature, and statuere, to set up, erect, cause to stand: STAGE, STANCE, STANCH, (STANCHION), (STANZA), STATOR, (STATUE), STATURE, STATUTE, STAY!, STET; ARREST, CIRCUM- STANCE, CONSTANT, CONSTITUTE, CONTRAST, (COST), DESTITUTE, DISTANT, ESTANCIA, EXTANT, INSTANT, IN- STITUTE, OBSTACLE, OBSTETRIC, (OUST), PROSTITUTE, REST?, RESTITUTE, RESTIVE, SUBSTANCE, SUBSTITUTE, SUPERSTITION. 4. Suffixed form *std-men- in Latin std- men, thread of the warp (a technical term): STAMEN, STAMMEL. 5. Suffixed form *std-mon- in Greek stémén, thread: PENSTEMON. 6. Suffixed form “s¢d-ro- in Russian staryi, old (“long-standing”): STARETS. II. Zero-grade form *st- (before consonants). 1. Nasalized extended form *sfa-n-t- in Germanic *standan in: a. Old English standan, to stand: STAND; b. Old English understandan, to know, stand under (under-, under; see ndher): UN- DERSTAND; Cc. Old French estandard, rallying place: STANDARD; d. secondary zero-grade form in Germanic *stund-6 in Old English stund, a fixed time, while: STOUND. 2. Suffixed form *sé-tyo- in Germanic *stath- Jon- in Old Norse stedhi, anvil: strTHY. 3. Suffixed form *sta-tlo- in Germanic *stathlaz in Old English stathol, foundation: STADDLE, STARLING?. 4, Suffixed form *sta-mno- in Germanic *stamniz in Old English stefn, stem, tree trunk: sTeM!. 5. Suffixed form *sta-ti- in: a. Germanic *stadiz in (i) Old English stede, place: STEAD (ii) Dutch stad, place: STADHOLDER (iii) Old High Ger- man stat, place: SHTETL; b. Latin stati6, a standing still: STATION; C. Latin -stitium, a stoppage (in solstitium, solstice; see sawel-): ARMISTICE; d. Greek stasis, a standing, a standstill: sTAsIs; HYPOSTASIS, ICONOSTASIS, IsOSTASY. 6. Suffixed form *sfo-to- in Greek statos, placed, standing: STATIC, STATICE, STATO-; ASTASIA, ASTATINE. 7. Suffixed form “sta-no- in: a. Latin désti-
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE aiw- AGENDUM ag- AGENT ag- AGERATUM gere-1 AGGLOMERATE gel-1 AGGLUTINATE gel-1 AGGRAVATE gWere-2 AGGREGATE ger-? AGGRESS ghredh- AGGRIEVE gWere-2 AGHAST gheis- AGILE ag-
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1390:CONFECT dhé-1 CONFEDERATE bheidh- CONFER bher-1 CONFESS bha-2 CONFETTI dhé-1 CONFIDANT bheidh- CONFIDE bheidh- CONFIDENT bheidh- CONFIGURATION dheigh- CONFIRM dher-2 CONFLAGRANT bhel-1 CONFLAGRATION bhel-1 CONFLATE bhié-2 CONFLICT bhiig- CONFLUENT bhieu- CONFORM merph-
1409:Dart dhabh- DAINTY dek-1 DAIRY dheigh- DAISY agh-2, okw- DALE dhel- DALLES dhel- DAMAGE dap- DAME deme-! DAMN dap- DAMNIFY dap- Dan? deme-! DANDELION dent- DANE dan- DANEGELD gheldh- DANELAW dan-, legh- DANGER deme-1 DaNIsH dan- DAPPER dheb- DARE dhers- DARK dher-! DASTARD dhé-2 DASYURE dens-2 DATE do- DATIVE do- DATUM do- DAUB _albho- DAUGHTER dhugheter- DAUNT deme-2 DAWN agh-2
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
1498:FARCE bhrekw- FARCI bhrekw. FARCY bhrekw- FARE per-2 FARINA bhares- FARINACEOUS _bhares- FARM dher-2 FARRAGINOUS_ bhares- FARRAGO bhares- FARRIER ferrum FARROW! porko- FART perd- FARTHING kWetwer- FARTHINGALE virére FASCES bhasko- FASCIA bhasko- FASCICLE bhasko- FASCINATE bhasko- FASCINE bhasko- FASCISM bhasko- FASHION dhé-1 FAST! past-
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1512:FIRE piir- FIRKIN kWetwer- FIRM dher-2 FIRMAMENT dher-2 FIRN pert
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
2263:SIRDAR dher-2, ker-1 SIRE sen-!
```


## [2026-09-05T20:04:22.649Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN pages around 116-123 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==138||NR==139' HRN.txt | head -60",
 "description": "Read Horn pages 116-117"
}
```


### [2026-09-05T20:04:24.551Z] TOOL RESULT

```
=== HRN pages around 116-123 ===
— 116 —
'setzen, machen, schaffen ; phlv. dätan; ai. l^dhä-,
dädhati; arm. dnel setzen' (H. No. 84).
522. (Tür 'Baumstamm, Holz', dann,
aw. däuni' 'Holz'; phlv. dar, dann 'hölzern (vd. 7
(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
*Holz\
np. durük 'dünnes Holz' (unbelcgt) gehört dagegen
zu ai. drü' 'Holz, Baum', gr. d(jvg Baum, Eiche', d()ior
{*ö(jfoi') 'Gehölz', ksl. drüvo (d. i. '^'drvo), got. friu 'Holz,
Baum'.
LW. kurd. dar; bei. dar (55).
523. därü, därUt *Ai'znei; Schiesspulvor', vergl. der man
(No. 554).
l^dhar- 'halten', vergl. aw. drva- gesund; phlv. därük
'Arznei'.
LW. kurd. af/. bei. (56) därü,
524. dm*e 'Gehalt, Salair'.
aw. dadra- 'Geschenk, Gabe'; phlv. ddsr; ai. däfra-
'Gabe'.
Hörn, KZ. 32, 584 No. 15.
525. (IffS 'Sichel'.
ai. dätra- 'Sichel'; phlv. das (AV.).
afy. lür 'Sichel'; LW. kurd. bei. (76) das,
526. däS 'Ofen*.
Zu [/'dagli' (aw. dajjz-, ai. rfa/i-), brennen (Nöldeke,
mündliche Mitteilung).
527. dästen 'halten, besitzen', Praes. där-em, dar, dara,
g. dartmfm; Käs. dörtän^ dördhi, dörd^nmn^ dort.
ap. l/^rfar-, darayamiy, adäraya 'halten, besitzen';
aw. [/^dar-^ däray^M; phlv. dästan^ dar-am, dar(i)sv^
dästar [syr. LW. *T1, ödg (de Lagarde, Ges. Abh.
33) sind verlesen (Nöldeke, Tabarl-Übersetzung,
447)] ; ai. [/^dhar-, dharäyati,
kurd. 'dar (LW.); af/. laral; oss. t. daf-in (102);
bei. (L W. ?) darag , n. daray (75) ; wa/. va-dür-am,
sar. ö6r-am.
Gehört hierher vielleicht auch zJnhär, zinhnr 'Schutz,
— 117 —
Sicherheit etc.*, ursprünglich 'hüte dich vor diesem,
halte dich von diesem zurück', wovon dann zTnharT
und nach dem FS sogar zinhariden gebildet wurden?
Allerdings wüsste ich dann nicht die Messung von
zinhar als Amphimacrus bei FirdüsT zu erklären, die
mir jedenfalls (vergl. Indog. Forsch. II, 185) für
iranischen Ursprung des Wortes zu sprechen scheint
(anders Nöldeke, Pers. Stud. II, 46, dessen Erklärung
aus dem aramäischen *inT, wie er selbst zugiebt,
wegen des t Bedenken erregt).
528. danen 'Geschenk, Gabe'.
g. däsn.
phlv. dah(i)Sn ; vergl. padäsn (No. 265*'^'').
529. däy 'Brandmal*, dey.
aw. daya-\ phlv. däy (vd. 15 (48) Gl.); ai. ddha-
'Brand*, skr. ni]däghd' 'Hitze*, Sommer'; lit. dagä 'heisse
Zeit, Sommer.
LW. kurd. afy. däy; bei. däg, n. day (52).
580. {\)ääm 'Haustier, zahmes Tier.
ai. l/"rfam-, d!(^wyci^i"zähmen, zahm sein'; gr. öujiidATjQ
'Stier; lat. domäre; air. dam 'Ochs, Stier ; got. ga-
```


## [2026-09-05T20:04:43.774Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=144 && NR<=146' HRN.txt",
 "description": "Read Horn pages 122-124"
}
```


### [2026-09-05T20:04:45.627Z] TOOL RESULT

```
— 122 —
Anm., Ar. Forsch. III, 22 Anm. 2) geben. Skr. djfdhä-
müsste also aw. *dereMa- entsprechen.
duriixs s. unter direfs (No. 553).
549. dei*:^, derze 'Naht', derzmän, demen, derzl (syr. LW.
pm), Käään Q.K. darzln 'Nadel' ').
g. dastmün, he-darze 'ich nähe*; Kjiö. hidastdn,
oadasten, vödastemän (S. 126).
aw. dereza- 'Fessel*, l/^rfar^-2f- 'festmachen'; ai. [y^darh-,
cte/fAöv/a-* befestigen', arm. (Zer/c/ifc 'Schneider (Schuster)*,
derjan 'Faden', handerj 'Kleid' (Hübschmann, No. 81).
oss. dares 'Kleid' (101).
Wahrscheinlich gehört np. enderz 'Rat, Ermahnung*
(phlv. andarj bezw. andarz) zu derselben Wurzel (mit
Praellx ham),
550. (lerd 'Schmerz'.
Wohl zu ai. 1 [/^dar- 'spalten, zerreissen, bersten
machen* (Hörn); vergl. got. tairan, ahd. zeraii, nhd.
zehren,
phlv. d(irt (vd. 20 (13)), dartak 'geplagt' (AV.); arm.
vergl. trtnm 'betrübt* (?) (Hübsch mann No. 278).
LW\ kurd. bei. (47) dard.
Nöldeke (mündliche Mitteilung) möchte derd zu
np. äzar (No. 20) stellen.
551. darust 'gesund, richtig, duriistl; vergl. tendumstX
aw. ^drva- + asti- gesunden Leibes* , oder wohl
besser drva- + sü- (vergl. aw. ayösti-), wie mir Bar-
tholomae vorschlägt; ap. diiruva- 'gesund'; phlv.
duritst^ durustih; ai. dhncvd- 'fest, bestimmt, bleibend'.
LW. kurd. durust 'wahr'; bei. driist 'voll, ganz,
vollständig' (86); wa/. drust, driist 'ganz, vollständig.
Anders Fr. Müller, WZKM. 5, 66; vergl. aber
unter np. dire/t (No. 548).
552. durust 'rauh, grob, stark, durustt,
ap. iXrfars- 'wagen', adarmans, darsma 'heftig, sehr';
aw. \/dar€S' 'wagen', darsi-; ai. \/dharS', dhfmoii
'J Unter sozen (Öcitc HDJ.
— 123 —
Als eine Bestätigung für diese Etymologie dient der
Umstand, dass Herr Prof. Nöldeke mir dieselbe
ebenfalls mitteilte; er war besonders von ai. (Ißtä- in
der Bedeutung *keck, frech' ausgegangen ^).
553. direfS Fahne, Banner'.
aw. drafsa- 'Banner -); phlv. draß^ arm. LW. draus;
ai. drapsd' 'Tropfen*.
oss. LW. (jrisa Tahne (von JStackelberg, Fünf
oss. Erz. 81).
Die ursprüngliche Bedeutung von ar. drapsd- ist
unsicher; Fick, Vorgl. Wörtbch. ^ I, 241, setzt
zweifelnd 'flutend, wallend' als solche an. Np. direfs
soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
direfsiden, jüd.-pers. t^l^E»*!"! (Is. 41, 25) (phlv. draßntk
zitternd', AV. , drafset Bund.); in dieser Bedeutung
scheint ein Zusammenhang mit np. duru/s (so hiutet
die ursprüngliche Vokalisation), diiriiysün, duruyßlden
V
vorhanden zu sein, wie denn auch im 8<ähnäme oft
die Formen in den Varianten durcheinander gehen
(z. B. I, 107 Vers 839). Duriiyß etc. halte ich für
Composita, wohl mit Praep. ati, deren zweites Glied
ruys (No. 610) ist.
551. derniän *Arzenei', vergl. darß (No. 523), dermene'^)
^Absinth'.
i^dhar- 'halten', vergl. aw. drva- gesund'; phlv.
darwan 'Arzenei'.
LW. kurd. af/. bei. (48) darmän,
555. durüd, duröd (8ähn. I, 50 Vers 301, 170 Vers 751),
'Segenswunsch, Gebet'.
*j Vergl. auch SFgnirt^? *Frecliling*.
'-) *Banner', nicht Waife, wie Darmes t et ci-, Et. ir. II, 273 über-
Hetzt. Auch im Sähnäme heisst direfs niemals Lanze'. Mand. LW.
Nii^£»NT1 bedeutet *Kreuz* (Nöldeke, Mand. Gramm. 309 Nore i).
Greldner^s Übersetzung von aw. (jaos drafsö (y. 10, 14J durch
*ein Tropfen Milch* (Metrik, S. 153) ist schwerlich richtig (s. Ausgabe).
^) dramna (Bund), syr. LW. ^^O")*!-
— 124 —
aw. droatäl- 'Geisundlieit' ') ; plilv. drüt (Men. ; AV.),
drütik courtoous' (West II, 280).
556. durüclen 'crndtcn\ Praes. diretv-em diretvldeiij durüd
'Erndto', JN^ni ^Erndte' (Is. 9, 2).
aw. vergl. dereta-, adereta- {t/ava-) ^geschnittenes,
gemähtes (sc. Korn)'; päz. drüdan erndten (PPGl.,
Men.).
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
drdw-am.
Das 3 in jüd.-pers. )x5l*n zwingt direivem zu lesen
und mit Spiegel, Arische Periode, 70 gr. Ooftko
'pflücken* zu vergleichen.
557. iliiröy, deröy 'Lüge; unwahr.
ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
n. dröy (49).
558. dnrüne 'Regenbogen'.
skr. drum- 'Bogen' (spät und selten).
bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
drün,
bei. drin beweist, dass die ebenfalls überlieferte
np. Aussprache dnrüne falsch ist, vergl. Hübsch-
mann, ZDMG. 44, 555.
559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
Vers 8), deryös, deryöz, deryöze.
aw. vergl. driyu- 'arm*, fem. driwt- {*driyvJ-),
driwika- {?); phlv. daryöä, daryösih.
Die neupersisehen Formen sind im Einzelnen schwer
zu erklären. Auch derey 'Jammer, Elend', Grund-
bedeutung 'Mangel, Beraubtsein*, dereyä gehören nach
Nöldeke (mündliche Mitteilung) hierher.
560. derre 'Thal, Schlucht'.
aw. darenä- 'Thal, Schlucht'; Adovu, Ptolem. 6, 1
(Spiegel, ZDMG. 32, 721).
») Vergl. Fr. Müllor, WZKM. 5, 352.
```


## [2026-09-05T20:05:05.167Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"dāštan\" \"dastan\" \"dārūg\" \"dlwk\" \"darmān\" \"drmʾn\" \"andarz\" \"handarz\" \"darz\" \"pahikārdan\" \"pendāštan\" \"pd-yn\" \"zēnhār\"; do echo \"--- $w\"; grep -n -- \"$w\" PHD_mackenzie.txt | head -5; done",
 "description": "Grep MacKenzie for relevant Pahlavi words"
}
```


## [2026-09-05T20:05:06.469Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT dar ===\"; grep -n \"dar-\\|Dārayavauš\\|darayamiy\\|Darayava\" KNT.txt | head -20",
 "description": "Grep Kent for Old Persian dar"
}
```


### [2026-09-05T20:05:06.943Z] TOOL RESULT

```
--- dāštan
--- dastan
732: ..... dastan: withhold, restrain, prevent.
1653: ,.., dastan: dwell, settle.
1881:dar-, --lsn, v. dastan.
1924:dastan [dIt'n l I N --] menstruation; menstruous.
1931:  pad ..• dastan: hold by, to; take for.
--- dārūg
--- dlwk
--- darmān
--- drmʾn
--- andarz
555:       handarz .,. add M 'ndrz.
1892:dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
2741:ham&tlr                         41                handarz~nidan
2789:handarz [hndlc i N andarz] advice, injunction, testament.
2790:handarzenidan, handarzen- [hndlc,,,,-ytn ] advise.
--- handarz
555:       handarz .,. add M 'ndrz.
1892:dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
2741:ham&tlr                         41                handarz~nidan
2789:handarz [hndlc i N andarz] advice, injunction, testament.
2790:handarzenidan, handarzen- [hndlc,,,,-ytn ] advise.
--- darz
555:       handarz .,. add M 'ndrz.
1848:dahillin                        24                           darzill
1892:dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
1904:darz [dIe I N --] seam.
1905:  ",ill [_yk l I N darzi] tailor.
--- pahikārdan
--- pendāštan
--- pd-yn
--- zēnhār
```


### [2026-09-05T20:05:07.001Z] TOOL RESULT

```
=== KNT dar ===
418:Darayavaus : rsdyagiya : vazrala :
724:Darayavahaus nom. XPf 25, Dérayavaus gen. XPf 28: the original copy had -vu in both places, and the corrector, finding the error in 28, made the insertion in the word where it stood in 25.
1462:Nom. Dàrayava^u&, gen. Darayavahaus. Nom. Hara*uvati&, Skt. sdrasvati.
1808:Expressing adjectival actor, as personal name: Vi- dar-na-; name of month, Vi-yaz-na-.
1814:V. For the dubious neuter abstract dar-tana-, see §238.
1820:1. Primary, in the following: dar-ma- in per- sonal name Upa-darma-, gar-ma- in month name Garma-pada-, fem. tau-mà-, ad]. taz-ma- in per- sonal names (see Lex.), hau-ma- in hauma-varga-. On dubious атат, see Lex.
1822:$150. Noun AND ADJECTIVE STEMS WITH SUF- FIX -ya- are a miscellaneous group. They include ai-va- ‘one’; adjective duru-va-, to verbal root dar-; adj. par-uva-; ethnic Par@a-va-, cf. Parsa-; yd-va-, to relative ya-; har-uva-; visa- and (Med.) vispa-, from pIE *yik-yo-; ji-va- ‘living’, unless the v is somehow radical (cf. §216). On Gau- baruva-, see Lex.:s.v.; on fem. aruva- as abstract, see Lex. s.v.
1940:a. Names of the Achaemenian dynasty: Ari- ? ydramna-, Árlaxíaga-, Aríüma-, Uvarstra- (M), Kabüjiya-, Küru-, XSayarSan-, Gaubaruva-, Cifpi-, Darayavau-, Bardiya-, Vistüspa- (M).
1956:IV. Still other names are appellatives indicat- ing the qualities of the persons, like the redupli- cated Dé-dar- ‘Bold’. Possibly *U-vazstra-, Vi- darna-, Vi-vàna- (given under П) also belong here. Or names may denote occupations, as per- haps in the adjectival derivative, possibly pa- tronymie, Mardun-iya- ‘Vintner’s son’.
2528:I. The Sigmatic Aorist is seen in niy-aparsam ‘I inscribed’ (or -apiSam?)}, to root pai8-, pIE *peik-; in mid. adarSiy ‘I held’, to root dar-, pIE *dher-; perhaps in pass. -asahya in frasah[ya]. The aorist endings 3d sg. -s-t, pl. -s-nf, may also be respon- sible for the endings of @1$ -diSa" to root ay- (8208); akunaus akunavasa to kar-; adurujiyasa to durujiya-; abaraha to bar-.
2534:With the vocalism of the present-tense stem: addriya, to dar-, pres. dāraya- ($215); and the uncertain [ар 0 уа] (see Lex. s.v. paté-). Formed on the present-tense stem: 3d pl. akunavaya"td, to kar-, pres. kunav-a- (§210.1); and the uncertain [айуа|вї]уа, for *atiyayastya ($215), to yam-, pres. yasa- (5212). Dubious forms on the sigmatic aorist stem, früsah[ya] to root sã- ($218.1), and on the per- fect stem, cazr|zyatd] or |clizr|iyatà], to kar-.
2593:V. The ending -i seems to be original in non- thematic imperfects and aorists in Aryan; cf. Skt. dnest ‘I led’ to root ni-. There is one example in OP, the sigmatic aorist adarsiy ‘I held’ to root dar- (normalization adarSaty, with -aty like all other OP 1st sg. middles, is also possible).
3133:Агатай... Dāraywaušahyā X Shyà puça Daraya- vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű XSayarcahya XShyà puça Xšayäreahyä Dāraya- vaušahyā XŠhyā puça D{éralyavausahya Vš- láspahya puça Haxamán?siya! In this the first phrase of parentage is grammatically correct; in the second, the gen. DarayavauSahyd is repeated аз a basis for clarity, and the appositive puça is in the nom. (see above), with proper depending
3137:II. The inscriptions A’Sb, A’Sd, A?Hb, AsH, А?Ра have a different scheme, in which the nomi- native of the royal name replaces the genitive. Only А?Ра is truly cogent, for the others have only these slightly varying versions of ‘son of Darius the King’: A'Sb Ddrayavaus Хбуй puça, A'Sd Darayavaus XSühyà риса, АЎНЬ Darayavaus X Š puçã; and ‘son of Ariaramnes the King’, in AsH Ariyüramna xsdyatiyahya риса. But A*Pa has a full lineage from Artaxerxes ITI back to Arsames, and uses the nominative for all royal names except for Hystaspes, also replacing the genitive of ‘king’ by nom. хёауабйуа, like X. S in АНЬ. Apparently OP had by this time become virtually а dead language employed only in writing ceremonial official records, its spoken form having suffered a wearing down of the endings (seen very clearly in Pahlavi). With the loss of the genitive ending it was natural to employ the nominative as a gen- eral case, as it had already been thus used in appositions. The gen. V*Slaspahyà probably per- sisted beeause in the earlier inscriptions available to the scribes of Artaxerxes I and later the name of Hystaspes occurred much more frequently in the genitive than in the nominative, and the scribes therefore used the familiar form in the in- seriptions whieh they composed.
3463:4 Darayavaus : xSayafflya : manā : pita : Vistàspa : Vistaspahyd : pità : Ars
3468:9 апу: Darayavaus : xSdyaéiya : ҮШ : mana : taumayd : tyoty : paruvam
3472:13 айту : Dārayavauš : xSayafiya : ima : dahyava : {уа : mand : paliyaisa : vain
3480:24 ya :avafà :akunavayatà : Oatiy : Darayavaus : xšňyaðiya : Auramazdü
3492:44 : Darayavaus : xSayafiya : айа : xSacam : tya : Gaumáta : һуа : magus : adin
3534:: Gitiy : Darayavaus : xSiyadiya : pasiva : adam : Ва
```


## [2026-09-05T20:05:16.819Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD_mackenzie 1876-1935 ===\"; sed -n '1876,1935p' PHD_mackenzie.txt; echo \"=== darug ===\"; grep -n \"darug\\|darng\\|dlwk\\|d..ug.*medicine\\|medicine\" PHD_mackenzie.txt | head -10",
 "description": "Read MacKenzie dar- section"
}
```


### [2026-09-05T20:05:16.896Z] TOOL RESULT

```
=== PHD_mackenzie 1876-1935 ===
    N --] know.
 --isn: knowledge.
 ,...,lsnOmand [-sn'wmnd] knowing.
dar [BBA < A bb'; dll M dr, N,...,] door; palace; chapter, subject.
dar [d'll M d'r-, N ,...,] tree, gallows; wood.
dar-, --lsn, v. dastan.
-dar [-d'll M -d'r, N --] suffix, -holder, -keeper.
P daray [dl'g I J --, N daray] bell.
·darak [dlk l ] section, paragraph.
darband [BBAbnd IN",] gate.
darbas [dIp's] palace.
dard [dW I M drd, N ,...,] pain.
 --omand [-'wmnd I M -wmnd, N ""'mand] ill, suffering.
daren [d'lyn l 1M d'rwyn] wooden.
dargah [dIg's I N --] doorway.
dargardih [d'lkrtyh I M d'rgyrdyh] crucifixion.
dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
darigbed [dlykpt ] palace superintendent.
                          '
• darmag [d'lmk ] fine, delicate.
                        '
darmin [dlm'n I M drm'n, N --] remedy, medicine.
                      '
darridan, darr- [SDKWN-tn < A"'; sdq; dl-ytn IN",] split, tear.
                                     '              '
darfig [d'lwk ' I M d'rwg, N daru] drug, medicament.
dar-wazig [d'lw'eyk I N dlir-baz] (pole-)acrobat.
                            '
darz [dIe I N --] seam.
  ",ill [_yk l I N darzi] tailor.
das                                25                         dazidan
das [d's I N --] sickle.
dasBr [d'sl = Av. dii8ra-] gift, reward.
 dast [YDE < A yd-h; dstl I = M, N --] hand.
dasta~ [dstk 1 I N --a] bunch, bundle, group.
dast(a)~ird [YDE-, dst-krt l I M dstygyrd, N dastgird] estate.
dast-l1ir [dst OHDWN, (v. griftan) I N --] I. helper; 2. captive.
dast-~raw [dstglwb ' ] captivity.
dast-karih [YDEk'lyh I N --i] handiwork.
dast-Aoy [dstfwd] = ~omez.
dastwar [dstwbll M dstwr, N dastilr] authority, priest, minister.
   --ih: custom; authority.
dastyar [dstyd'll (P dstd'r), N --] helper.
  --ih: help, assistance.
daAn [dIn' I = M] right hand.
diAn [d'fn' I M d'f(y)n] gift.
daAna~ [dInk I I N --a] I. right hand; 2. dagger.
daAt [dft' I = M, N --] plain, open ground.
dastan [dIt'n l I N --] menstruation; menstruous.
  --estan [-st'n l ] secluded place for menstruous women.
  ---mah [-m'h] menstrual cycle.
  -omand [-'wmnd] menstruous.
daAtan, dar- [YHSNN-tn < A"'; b-sn; d'Itn ' , d'l-I M d'ftn, d'r-, N-]
                                '
      have, hold, keep, preserve.
  pad ..• dastan: hold by, to; take for.
  pad ed da§tan [cf. N pindiiItan] consider.
  -iAn: preservation, maintenance.
dastar [d'ft'l] keeper, preserver.
daw-, v. dawidan, dawistan.
=== darug ===
1897:darmin [dlm'n I M drm'n, N --] remedy, medicine.
7040:  zag, hangosidag, ristag, san, son,       medicine darman.
7089:medicament darug.                          millstone iisyag.
10922:dadar, gadar                     ~l'eJU         darug
```


## [2026-09-05T20:05:17.890Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT lexicon dar ===\"; grep -n \"'hold'\\|to hold\" KNT.txt | head -20",
 "description": "Grep Kent for hold"
}
```


### [2026-09-05T20:05:17.941Z] TOOL RESULT

```
=== KNT lexicon dar ===
4225:2179 The list of provinces is restored by retranslation from the АКК. version; whether both Putayé and Kūšiyā stood in 29-30 depends upon whether the gap at the end of line 21 of the АКК. is adequate to hold both names. 35 vind] Kent, JAOS 58.116-7; ci(£a] Sen 134. *** The restorations are quite uncertain; but cf. Hinz, ZDMG 95.229-32.
4853:nobleman, Otanes son of Pharnaspes, suspecting his identity, managed by a ruse to prove it to himself (67-9), and secured the help of five other trusted noblemen, to whom there was added Darius, who had come to Susa from his father Hystaspes, governor of Persia (70; see App. IIT). Darius insisted on immediate action against the two Magi (71-3). Helped by the confusion follow- ing the public confession of Prexaspes that he had murdered the true Smerdis, and by his suicide, the seven men burst into the presence of the two Magi and slew them (74-9). They then agreed upon a method of selecting one of their number to hold the throne, and Darius, aided by the trickery of his groom Oebares, was the winner (80-8).
```


## [2026-09-05T20:05:30.652Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT lex dar ===\"; grep -n \"^dar-\\|dar- .*hold\\|adarsiy\\|dāraya\" KNT.txt | head; echo \"=== KNT Darayavau lexicon ===\"; grep -n \"Dārayava.*hold\\|holding good\\|holding firm\" KNT.txt | head",
 "description": "Grep Kent lexicon for dar"
}
```


### [2026-09-05T20:05:30.754Z] TOOL RESULT

```
=== KNT lex dar ===
2534:With the vocalism of the present-tense stem: addriya, to dar-, pres. dāraya- ($215); and the uncertain [ар 0 уа] (see Lex. s.v. paté-). Formed on the present-tense stem: 3d pl. akunavaya"td, to kar-, pres. kunav-a- (§210.1); and the uncertain [айуа|вї]уа, for *atiyayastya ($215), to yam-, pres. yasa- (5212). Dubious forms on the sigmatic aorist stem, früsah[ya] to root sã- ($218.1), and on the per- fect stem, cazr|zyatd] or |clizr|iyatà], to kar-.
2593:V. The ending -i seems to be original in non- thematic imperfects and aorists in Aryan; cf. Skt. dnest ‘I led’ to root ni-. There is one example in OP, the sigmatic aorist adarsiy ‘I held’ to root dar- (normalization adarSaty, with -aty like all other OP 1st sg. middles, is also possible).
3707:23 : Yautiyd : nama : dahyáus : Pársaiy : avadà : adāraya : ha
5517:ldar- vb. ‘hold; (intrans.) dwell’: Av. dar-, Skt. dhr-, Lt. fir-mus ‘firm’, Lith. daryti ‘to make’, pIE *dher- ($76.11, $122). See also Upadarma-, Dérayavau-, duruva-, Vidarna-. Present stem dàraya- and conj. 58215. dárayümiy Ist sg. (226.1) AmH 5f; AsH 11, 14; DB 1.26; DPh 4f;
5519:DNb 14; DH 4. dárayatty DNd 2 (reading cer- tain, acc. to Wb.’s marginal note to AbkSGW 29.- 142). dàáraya"liy 3d pl. (82321) XPh 23f, 24f. adāraya imf. ($2281) DB 1.85;2.9,3.23; DNa 41; DSe 20Ї°; XPh 19; adáraiya DNa 22 ($48; Wb. AbkSGW 29.33, cf. Kent, JAOS 35.947n; wrongly Hz. ApI 132, as passive). adaá[rayat]à imf. mid. with passive meaning DB 4.90f ($235.II; JAOS 62.268). adaršiy Ist sg. aor. mid. (8218 T, 8233. V) DPe 8. adáüriya imf. pass. ($220, $228JT) DB 2.15, 90.
5520:ham- + dar- ‘get hold of, obtain’: hamadárayaiy Ist sg. imf. (5233. TIT) DB 1.26.
5524:Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
=== KNT Darayavau lexicon ===
```


## [2026-09-05T20:05:31.574Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB bahadur ===\"; grep -n -i \"bahaudur\\|bahadur\\|BAHAUDUR\" HJB.txt | head -10",
 "description": "Grep Hobson-Jobson for bahadur"
}
```


### [2026-09-05T20:05:31.650Z] TOOL RESULT

```
=== HJB bahadur ===
2489:BAHAUDUR
2504:BAHAUDUR,  s.  H.  Bahadur,  'a hero,  or  champion.'  It  is  a  title  affixed commonly  to  the  names  of  European officers  in  Indian  documents,  or  when spoken  of  ceremoniously  by  natives {e.g.  "Jones  Sahib  Bahddur"\  in  which use  it  may  *be  compared  with  "the gallant  officer"  of  Parliamentary courtesy,  or  the  lUtutrissimo  Signare  of the  Italians.  It  was  conferr^  as  a title  of  honour  by  the  Great  Mogul and  by  other  native  princes  [while in  Persia  it  was  often  applied  to  slaves (Burton,  Ar.  Nights,  iii.  114)].  Thus it  was  particularly  a^ffected  to  the  end of  his  life  by  Hyder  Ali,  to  whom  it had  been  given  by  the  Raja  of  Mysore (see  quotation  from  John  Lind«iy below  [and  Wilks,  Mygoor,  Madras reprint,  i.  2801).  Bahddur  and  Sirddr Bahddur  are  also  the  official  titles  of members  of  the  2nd  and  1st  classes respectively  of  the  Order  of  British Inaia,  established  for  native  officers of  the  army  in  1837.  [The  title  of Rdi  Bahddur  is  also  conferred  upon Hindu  civil  officers.]
2507:BAHAUDUR.
2508:BAHAUDUR,
2510:Bahddur  is  one  of  the  tenas  which the  hosts  of  Chlngiz  Khan  brought with  them  from  the  Mon^l  Steppes. In  the  Monffol  cenealpgies  we  hnd Yesugai  Bahadur^  Uie  father  of  Chineiz, and  many  more.  Subutai  BahMur, one  of  the  great  soldiers  of  the  Mongol host,  twice  led  it  to  the  conquest  of Southern  Russia,  twice  to  that  of Northern  China.  In  Sanang  Setzen's ]X)etical  annals  of  the  MoiLgols,  as rendered  by  I.  J.  Schmidt,  the  word is  written  BaghaJtuTy  whence  in  Russian Boffoiir  still  survives  as  a  memento probably  of  the  Tartar  domination, meaning  *^  hero  or  champion.'  It occurs  often  in  the  old  Russian  epic fiallads  in  this  sense ;  and  is  also  ap- plied to  Samson  of  the  Bible.  It occurs  in  a  Russian  chronicler  as  early as  1240,  but  in  application  to  Mongol leaders.  In  Polish  it  is  found  as  Bo- hatyr^  and  in  Hungarian  as  Bdtor, — this last  beinjg  in  fact  the  popular  Mongol pronunciation  of  Baghaiur.  In  Turki also  this  elision  of  the  guttural  extends to  the  spelling,  and  the  word  becomes Bdtur,  as  we  find  it  in  the  Diets,  of VamWry  and  Pavet  de  Courteille. In  Manchu  also  the  word  takes  the form  of  BatuTUy  expressed  in  Chinese characters  as  Pa-tu-lu ;  f  the  Kirghiz has  it  as  Baiyr;  the  Altai-Tataric  as PcuUtyTy  and  the  other  dialects  even as  Magaihyr.  But  the  singular  history of  the  word  is  not  vet  entirely  told. Benfey  has  suggestecl  that  the  word originated  in  Skt.  bhaga-dhara  (*  happi- ness-possessing'). J  But  the  late lamented  Prof.  A.  Schiefner,  who favoured  us  with  a  note  on  the subject,  was  strongly  of  opinion  that the  word  was  rather  a  corruption ^Hhrough  dissimulation  of  the  conso- nant," of  the  Zend  bagha-puthra  *  Son of  GJod,'  and  thus  but  another  form of  the  famous  term  Fagbfor,  by  which the  old  Persians  rendered  the  Chinese Tien-tsz  (*Son  of  Heaven  *),  applying  it to  the  Emperor  of  China.
2521:1404.— "E  elles  le  dixeron  q  aquel  era uno  de  los  valiStes  e  Bahadures  q'en  e) linage  del  Sefior  am&"—Clavij0f  §  Ixxxix.
2523:1407.— "The  Prince  mounted,  escorted  by a  troop  of  Bahadurs,  who  were  always about  his  peTaon."—Abdurrazak't  Hist,  in Not.  et  Ext.  xiv.  126.
2528:We  have  said  that  the  title  Behauder {Bahadur)  was  one  by  which  Hyder Ali  of  Mysore  was  commonly  known in  his  day.  Thus  in  the  two  next quotations :
2537:1872.—".  .  .  the  word  'BahAdnr'  .  .  . (at  the  Mogul's  Court)  .  .  .  was  only  used as  an  epithet.  Ahmed  Shah  used  it  as  a title  and  ordered  his  name  to  be  read  in  the Friday  prayer  as  'Mujahid  ud  dfn  Mu- hammad AbtE  na^r  Ahmad  Sh^  Bahddur. Hence  also  *  Kamjaani  Bahadur,'  the  name by  which  the  £.  1.  Com^ny  is  still  known in  India.  The  modem  *  Khan  Bahddur '  is, in  Bengal,  by  permission  assumed  by  Mu- hammedan  Deputy  Magistrates,  whilst  Hindu Deputy  Magistrates  assume  *  R^  BalULdur ' ; it  stands,  of  course^  for  ^  KhjCn-i-Bahddur, ' 'the  courageous  Kh^n.'  The  compound, however,  is  a  modem  abnormal  one;  for *Khin'  was  conferred  by  the  Dihli  Em- perors, and  so  also  *  Bah^ur '  and  *  Bah^ur KMn,'  but  not  *Kh^  Bah^ur.'"— Pro/. Blochmann,  in  Ind,  AfUifptary,  i.  261.
3229:*  The  "  Bahadur"  ooold  hardly  have  read  Don Quixote  I  But  what  a  cuiiooa  parallel  presentH itself!  When  Sancho  Is  bracing  of  his  aau^ter to  the  "  Squire  of  the  Wood,  and  takes  umbrage at  the  ftee  epithet  which  the  said  8qnira  spiles to  her  (s  IsMmUkA  and  more) ;  the  latter  reminds him  of  the  like  term  of  apparent  abuse  (hardly reprodnoeable  here)  with  which  the  mob  were .wont  to  greet  a  champion  in  the  bull-ring  after  a deft  spear>thiust,  meaning  only  ths  highest  fbnd* nass  and  applause  I— Ffert  ii.  eh.  IIL
```


## [2026-09-05T20:05:46.496Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('HJB.txt',encoding='utf-8',errors='replace').read()\n# find line number 2504 offset\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:2503])\nprint(\"formfeeds before:\", t[:off].count('\\f'))\nEOF",
 "description": "Find HJB leaf for bahadur"
}
```


## [2026-09-05T20:05:47.417Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN bahadur ===\"; grep -n -i \"bahadur\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== SOD d'r ===\"; grep -n \"to hold, have\\|hold, have\" SOD_pages.txt | head -10",
 "description": "Grep Klein and Sogdian"
}
```


### [2026-09-05T20:05:48.361Z] TOOL RESULT

```
formfeeds before: 100
```


### [2026-09-05T20:05:48.440Z] TOOL RESULT

```
=== KLN bahadur ===
KLN_1971.txt:24865:bahadur, n., a title given to European officers in 
KLN_1971.txt:24866:India. — Hind, bahadur , ‘hero’, which accord- 
KLN_1971.txt:25005:ment in Bhagavadgita, and in bahadur. 
KLN_1971.txt:180045:element in esophagus. Cp. also bahadur, bak- 
KLN_1966.txt:4285:baguette,  n.,  a  small  molding.  —  F.,  prop,  ‘a small  rod’,  fr.  It.  bacchetta,  dimin.  of  bacchio, ‘rod’,  fr.  L.  baculum.  See  bacillus, bahadur’n.,  a  title  given  to  European  officers  in India.  —  Hind,  bahddur,  ‘hero’,  which  accord¬ ing  to  Benfey  (in  Orient  und  Occident  1  137, quoted  in  Hobson-Jobson  49a)  derives  fr.  OI. bhaga-dhara-,  ‘happiness-possessing’.  The  first
KLN_1966.txt:4302:baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
KLN_1966.txt:28431:-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning
=== SOD d'r ===
```


## [2026-09-05T20:05:58.084Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4285,4292p' KLN_1966.txt; echo \"=== SOD ===\"; grep -n \"δʾr\\|d'r\\b\" SOD_pages.txt | head -20; echo \"=== SOD 135 ===\"; grep -n \"\\[pdf page 20[0-5]\\]\" SOD_pages.txt | head",
 "description": "Read Klein bahadur and locate Sogdian"
}
```


### [2026-09-05T20:05:58.162Z] TOOL RESULT

```
baguette,  n.,  a  small  molding.  —  F.,  prop,  ‘a small  rod’,  fr.  It.  bacchetta,  dimin.  of  bacchio, ‘rod’,  fr.  L.  baculum.  See  bacillus, bahadur’n.,  a  title  given  to  European  officers  in India.  —  Hind,  bahddur,  ‘hero’,  which  accord¬ ing  to  Benfey  (in  Orient  und  Occident  1  137, quoted  in  Hobson-Jobson  49a)  derives  fr.  OI. bhaga-dhara-,  ‘happiness-possessing’.  The  first
element  is  cogn.  with  Gk.  tpaystv,  ‘to  eat’;  see -phagous  and  cp.  baksheesh.  For  the  second  ele¬ ment  see  aumildar  and  cp.  words  there  referred  to. Bahaism,  n.,  the  teaching  of  the  religious  sect  of the  Bahaists.  —  Formed  with  suff.  -ism  fr.  Pers. baha,  ‘splendor’,  fr.  Arab,  bahd' ,  of  s.m. bahar,  n.,  a  weight.  - —  Arab,  hahdr,  a  weight  used in  India,  ultim.  fr.  OI.  bhdrah,  ‘load,  weight’, which  is  rel.  to  bhdrati,  bharate,  ‘carries’,  and cogn.  with  Gk.  qilpeiv,  L.  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,  and  cp.  words  there referred  to.
bahur,  n.,  young  man,  youth,  unmarried  man.  — Hebrew  bah  dr,  ‘young  man’,  rel.  to  Akkad. bahulati,  ‘warriors’.
bahuvrihi,  n.,  name  of  a  class  of  compounds (Old  Indian  gram.)  —  OI.  bahuvrihih,  ‘having much  rice’,  compounded  of  bahuh,  ‘much, numerous,  abundant’,  and  vriltih,  ‘rice’.  The first  element  is  rel.  to  Avestic  bazah-,  ‘height, depth’,  and  cogn.  with  Gk.  -ay;)?,  ‘thick’;  see pachy-.  For  the  second  element  see  rice, baignoire,  n.,  box  at  a  theatre.  —  F.,  ‘bath,  bath¬ tub;  box  at  a  theatre’,  fr.  baigner,  ‘to  bathe’,  fr. bain,  ‘bath’,  fr.  L.  balneum.  See  balneal  and  cp. bagnio.
baikalite,  n.,  a  dark-green  variety  of  hedenbergite (mineral.)  —  Named  after  Lake  Baikal  in  Si¬ beria,  near  which  it  was  first  discovered.  For  the ending  see  subst.  suff.  -ite. bail,  n.,  security.  —  OF.  bail,  ‘custody’  (whence F.  bail,  ‘lease’),  fr.  haillier,  ‘to  seize,  carry,  give’, fr.  L.  bajulare,  ‘to  bear  a  burden’,  fr.  bdjulits, ‘porter’,  which  is  of  uncertain  origin.  Cp.  bail, ‘to  dip  water’,  and  bailiff.
Derivatives:  bail,  tr.  v.,  bail-ee,  n.,  bail-er,  n. (law),  bail-ie,  n.,  baili-er-y  (also  haili-ar-y)  n., bail-ment,  n.
bail,  n.,  fortification;  crossbar.  —  ME.,  fr.  OF. bail,  ‘stake;  palisade’,  which  prob.  derives  fr. L.  baculum,  ‘rod,  staff’.  See  bacillus  and  cp. bailey.
bail,  also  bale,  n.,  a  bucket  used  to  dip  water  out of  a  boat;  tr.  v.,  to  dip  water  out  of;  intr.  v.,  to dip  out  water.  —  F.  bailie,  ‘bucket’,  fr.  ML. *bajula  (aquae)  lit.  ‘porter  (of  water)’,  used  in the  sense  of  ‘water  jar’;  *bdjula  is  the  fern,  of bdjulits.  See  bail,  ‘security’, bailey,  n.,  walls,  resp.  courts  of  a  feudal  castle.  — ME.  variant  of  bail.  See  bail,  ‘fortification’, bailiff,  n.  —  ME.  baillif,  fr.  OF.  baillif  ‘custodian, magistrate’,  fr.  ML.  bdjulivus,  fr.  L.  bajutus, ‘porter’.  See  bail,  ‘security’,  and  -ive. Derivative:  bailiff-ry,  n.
=== SOD ===
4084:86 "y^-             (J>> j<*& jj) j-bjUT t&J'&ji                *yst-\ ^sd'r-
4110:90 »y5>w B                                jAjh'sxJ             'yd'r-
4337:    anlt ©pt. st. ^nyd'r-, 'n'y-                                       farewell
4846:372 "yScw S                                         j^j»<j*>?      382 "ytwS'r- =» 'yd'r-
5352:555 >ptmyk B, S, M                               ^              (s)Pyapt (py'pt-) ©pt. st. ^by'pd'r-
5829:    (a)xsawan5ar, oxsonSar       Oxswnd'r)
5878:      ayast ©pcrf. st. }rst/0}r-; pt. st. ^'yst-1, 'ysd'r-
6412:928 toptot1 B                    C-ip-0 <L^          iA^i <OJp      939 *>nPYt- => 'npYtd'r-
7175:         341; Sogd. Cpds. 146                                            anay- ^'nyt-, 'nyd'r-, 'n'y-
7306:1222 'nyd'r-      C                  O^O^^l^'j                       Sogdica. 64.5, 65.28; GMS     1100
7328:        anzut, anzot Oz'wd'r-) ©pt. st. ^'z'w-, zw-
9101:                                                                  1863 Svcn-d'r-     C            jj/ulkilo^/o^
9438:                                                                  6st(5)ar OwstS'r-, ^styS/d'r-) ®<mwsi-6yr
9484:1978 'wsty8/d'r-           B, C =» 'wst'r-, >wst}yt                     1993 Hvswxt-  =» 'ws'wyt-
9686:       880.14; C2, 51V3, 77R14; AVS 132                            C2, 87R10, 51V24, trans, pret. 'wyzd'r, Vyz/V,
9990:       C2 gloss, ob. -y, C2, 51R13                                 2156 >yd'r- C                                        ^/
10718:                                                                  OjZ**   2414 'ytS'r- '-» 'yd'r-
11016:     2509 b'wd'r- C                                                          VJ 820; GMS 434 n 2, fiion
11626:2735 brd'r-    C => Prt-                                          frayna (prynh, Prynh) =*fryn()), P'ryn               <
11683:     Par(a)kya =*8b}rqy\ bznbrqy*                                      Pn, pa/art (brd'r-) ©<*brta **Pr-, Pwrt-
=== SOD 135 ===
```


## [2026-09-05T20:05:58.761Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5; echo ...; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5",
 "description": "Check BQT page tags"
}
```


### [2026-09-05T20:05:58.847Z] TOOL RESULT

```
...
```


## [2026-09-05T20:06:05.618Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -40 SOD_pages.txt; echo \"=== entry 135x ===\"; grep -n \"^\\s*135[0-9]\\? \\|1350\\|  135 \" SOD_pages.txt | head -20",
 "description": "Inspect SOD file"
}
```


### [2026-09-05T20:06:05.673Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English




      B.Gharib




   FARHANGAN   PUBLICATIONS
Sogdian Dictionary (Sogdian-Persian-English)
by B. Gharib
editorial supervisor: A. Mansouri
editor: S. Fotouhi
© 1995, Farhangan Publications
2/52. Shahid-e Said Street, Tehran 15916, Iran.
Tel: 6460069. Fax: 670230

ISBN: 964-5558-06-9
4f*Jj*l{^ 0"J-^8 'Jy^**-             ^J>*4^ tfW : j' a>„J^ <f jljX-U^ -LUi^-L ^JjJ'j^ L» e jlf ijj-
                                                                • l^> o-^ jl ^^<o (j ^jb^b             j uij^- ^C*"
                  ;l_^0 jL-u jlS' 4$" (.5*^-*^' "^^   (H^- fJ




                                                                                                                   L?JJ J'
                                                                             ^            jS.          Ji          *




                                                                             JU-ib^y* jl^ *^Up ^j^>» 4^—*a j -U>_#

O      i j^tbj^> j^Ui   ^O ^ p-iU- jl ^                  ~J*A*         u^T J ('.»-) ^.^ MJ-^ ^                         jl

iJUj
=== entry 135x ===
4200:135 »kJcyy        M -> »k>c(h)                                 (ro)hang, (ro)suspend
7617:                                                                     1353 'psys'r S                             o~r"a~i
7623:                                                                     1354 'psyyk M                                     6xy^ <*juil
7631:                                                                     1355 >pt- B, M                                           o^/
7642:                                                                     1357 'pt'yn'kCw) S                                      ^/
7679:1350 >psty- B,S              d^cd^'dijTjjfh
7686:1351 >Psy  B =* psy                                                      GMS 969
7687:1352 }psyk => 'psyyk                                                1365 >pw J,stnyh     B                                  ^MW
9772:       135 n8                                                       2080 »xsVn       M, S
31697:                                                                 EGSii 113f; GMS 1350, 1393; VJ pl20; TSP
36728:    11350 znq'n      C ^ znk'n                                        zand-wac msryCa) ^zntw'cCh)
37564:above   1542, 3301,8806,8808                    accustomed       10966                        OcOadmonish 1350, 651 1, 7527
38169:eloquent      10348                            OcOentrust     1350                     everyday     5604
```


## [2026-09-05T20:06:07.298Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -20 BQT_v2_pages.txt; echo \"======\"; grep -c \"\" BQT_v2_pages.txt; grep -n \"^\\s*۸۱۰\\|^\\s*810\\s*$\" BQT_v2_pages.txt | head",
 "description": "Inspect BQT v2 format"
}
```


### [2026-09-05T20:06:09.269Z] TOOL RESULT

```
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
======
41071
```


## [2026-09-05T20:06:16.091Z] TOOL CALL #30: Bash

```json
{
 "command": "sed -n '1,50p' tools/ref_page.py",
 "description": "Inspect ref_page.py"
}
```


### [2026-09-05T20:06:16.133Z] TOOL RESULT

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
```


## [2026-09-05T20:06:18.211Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD delta-ar ===\"; grep -n \"hold, have\\|to have, hold\\|(to) hold\" SOD_pages.txt | head -20; echo \"=== 8'r- entries ===\"; grep -n \"^\\s*[0-9]\\{3,4\\} \\(8\\|5\\|δ\\)'r-\" SOD_pages.txt | head",
 "description": "Search Sogdian dar"
}
```


### [2026-09-05T20:06:19.745Z] TOOL RESULT

```
=== SOD delta-ar ===
=== 8'r- entries ===
13504:3412 8'r- B, M, S             (J>> ^<** jj)jzi.L^i <jiib          3425 S'rwkp'Sy B                               ^^      Jj£
```


## [2026-09-05T20:06:26.333Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13500,13512p' SOD_pages.txt; echo \"=== formfeed leaf ===\"; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:13503])\nff=t[:off].count('\\f')\nprint(\"leaf(0-based):\",ff, \"printed approx:\", ff-66)\nEOF",
 "description": "Read Sogdian dar entry and its page"
}
```


### [2026-09-05T20:06:27.939Z] TOOL RESULT

```
     5apat-sir ?                                                       SCE 133; TSP; BSTBL, Padm. 41; GMS 978; BBB
     Dapat-wishcr                                                        463; STii 1.49, 53; Syrwq% BBB 498; STii 1.15,
     Sogdica. 7.1                                                        80, 13.10

3412 8'r- B, M, S             (J>> ^<** jj)jzi.L^i <jiib          3425 S'rwkp'Sy B                               ^^      Jj£
     6ar (d'r1) ©OP ddraya- ©inf. -}y; trans, prct.                    5aruk-pa5c
       aux. =»5ryt-                                                    wooden shoes
     (/cOhavc, (/cOpossess, (ro)hold, 0o)kccp, (/o)wcar                SCE 152
       GMS 285, 877-880, 855
                                                                  3426 8'rwkync     M                          ^J^S ^^3^
3413 dV     C =» 8>r-                                                  5arukc(n)c   (5'rwqync) ©f. adj,
3414 dV     C                                          r t a— J
                                                                       (o/)pIant, herbal
=== formfeed leaf ===
leaf(0-based): 200 printed approx: 134
```


## [2026-09-05T20:06:34.084Z] TOOL CALL #33: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:06:34.131Z] TOOL RESULT

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


## [2026-09-05T20:06:40.380Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0er-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B1%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D9%85%D8%A7%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 128, root Dher 1: verifying dher- root and Persian dastan/pendastan/daru/darman\" ; done",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-05T20:06:45.303Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ac0bd876cb6e2258.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab429ac3eed845de.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/858b489c7d4b6adb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66b649f839865ec2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/263f48b21acf26ff.txt
```


## [2026-09-05T20:06:48.595Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in ac0bd876cb6e2258 ab429ac3eed845de 858b489c7d4b6adb 66b649f839865ec2 263f48b21acf26ff; do echo \"###### $f\"; sed -n '1,400p' $f.txt | grep -n -A6 -i \"Etymology\\|Reconstruction\" | head -60; done",
 "description": "Read archived Wiktionary text"
}
```


### [2026-09-05T20:06:50.288Z] TOOL RESULT

```
###### ac0bd876cb6e2258
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0er-
2-FETCHED: 2026-09-05T20:06:42Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/dʰer- - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/dʰer- - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
11-
12- Main menu
--
78: Reconstruction:Proto-Indo-European/ dʰer- 
79-
80- Add languages 
81-
82: Reconstruction 
83-
84- Discussion 
85-
86- English 
87-
88- Read 
--
263: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/dʰer-&oldid=92171357 "
264-
265- Categories : Proto-Indo-European lemmas 
266- Proto-Indo-European roots 
267- Proto-Indo-European CeR-shaped roots 
268- Proto-Indo-European perfective roots 
269-
--
304: Reconstruction:Proto-Indo-European/ dʰer- 
305-
306- Add languages 
307-
308- Add topic
###### ab429ac3eed845de
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
--
159: Etymology
160- [ edit ] 
161-
162- From Middle Persian [Book Pahlavi needed] ( dʾštn' /⁠dāštan⁠/ , “ to hold, to have ” ) , [Book Pahlavi needed] ( YHSNN-tn' /⁠dāštan⁠/ ) , 𐫅𐫀𐫢𐫤𐫗 ( dʾštn /⁠dāštan⁠/ ) , from Old Persian 𐎭𐎠𐎼𐎹𐎫𐎡𐎹 ( d-a-r-y-t-i-y /⁠dārayatiy⁠/ , “ to hold, have ” ) , from Proto-Iranian *dāráyati , [ 1 ] from Proto-Indo-Iranian *dʰāráyati ( “ to hold, carry; to bear, support ” ) , from Proto-Indo-European *dʰer- ( “ to hold ” ) .
163-
164- Pronunciation
165- [ edit ] 
###### 858b489c7d4b6adb
62: Etymology 
63-
64- 1.2 
65- Verb 
66-
67- 1.2.1 
68- Conjugation 
--
141: Etymology
142- [ edit ] 
143-
144- From Middle Persian pd ( pad , “ to, at ” ) + ẔNE ( ēn , “ this ” ) + dʾštn' ( dāštan , “ to hold/have ” ) . Compare Middle Persian pd HNA dʾštn' ( pad ēd dāštan , “ to consider ” , literally “ to this to hold/have ” ) .
145-
146- Verb
147- [ edit ] 
###### 66b649f839865ec2
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
--
99: Etymology 
100-
101- 3.2 
102- Pronunciation 
103-
104- 3.3 
105- Noun 
--
125: Etymology 1 
126-
127- 4.1.1 
128- Pronunciation 
129-
130- 4.1.2 
131- Noun 
--
134: Etymology 2 
135-
136- 4.2.1 
137- Pronunciation 
138-
139- 4.2.2 
140- Noun 
--
224: Etymology
225- [ edit ] 
226-
227- Borrowed from Classical Persian دارو ( dâru , “ medicine, drug, gunpowder ” ) , itself derived from Middle Persian dʾlwkˈ ( dārūg , “ drug, medicament ” ) .
228-
229- Noun
230- [ edit ] 
###### 263f48b21acf26ff
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
--
82: Etymology 
83-
84- 2.2 
85- Noun 
86-
87- 2.2.1 
88- Derived terms 
--
102: Etymology 
103-
104- 3.2 
105- Pronunciation 
106-
107- 3.3 
108- Noun 
--
194: Etymology
195- [ edit ] 
196-
197- Borrowed from Classical Persian درمان ( darmân , “ remedy, cure ” ) 
198-
199- Noun
200- [ edit ] 
--
245: Etymology
246- [ edit ] 
247-
248- Inherited from Old Anatolian Turkish درمان ( dermān ) , from Classical Persian درمان ( darmān , “ remedy, cure ” ) .
249-
250- Noun
251- [ edit ] 
--
308: Etymology
309- [ edit ] 
310-
311- Inherited from Middle Persian 𐫅𐫡𐫖𐫀𐫗 ( drmʾn /⁠darmān⁠/ , “ remedy, medicine ” ) , Northern Luri دںرمۆ ( dərmø ) from Proto-Indo-Iranian , ultimately from Proto-Indo-European *dʰér-mn̥ . Compare Sanskrit धर्मन् ( dharman , “ support, supporter ” ) , धर्म ( dharma , “ morality, virtue ” ) , [ 1 ] and the Iranian loanwords: Old Armenian դարման ( darman ) , Classical Syriac ܕܪܡܢܐ ( darmānā ) .
312-
313- Pronunciation
314- [ edit ]
```


## [2026-09-05T20:06:59.838Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### PIE dher-\"; sed -n '95,180p' ac0bd876cb6e2258.txt; echo; echo \"##### daru Persian\"; grep -n -B3 -A12 \"Persian\\b\" 66b649f839865ec2.txt | sed -n '1,120p'",
 "description": "Read PIE dher- and Persian daru"
}
```


### [2026-09-05T20:06:59.937Z] TOOL RESULT

```
##### PIE dher-

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

 *dʰer- ( perfective ) [ 1 ] [ 2 ] 

 to support 

 to hold 

 Extensions
 [ edit ] 

 *dʰer-ǵʰ- ( “ strong, robust ” ) 

 *dʰer-s- ( “ to be bold ” ) 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *dʰer- (68 c, 0 e) 

 *dʰr̥-tó ~ dʰr-n̥tó ( root medio-passive aorist ) [ 2 ] [ 3 ] 
 Proto-Indo-Iranian: *Hádʰr̥ta 
 Proto-Indo-Aryan: *Hádʰr̥ta 
 Sanskrit: अधृत ( ádhṛta ) , धृथास् ( dhṛthā́s , 2sg.inj.med. ) 

 Proto-Iranian: *Hádr̥ta 
 Avestan: 𐬛𐬆𐬭𐬆𐬙𐬁 ( dər ə tā , 3sg.inj.med. ) , 𐬛𐬭𐬍𐬙𐬁 ( drītā , 3sg.opt.med. ) 

 *dʰér-e-ti ( thematic present ) [ 2 ] [ 4 ] 
 Proto-Balto-Slavic: 
 Latvian: derêt 

 Lithuanian: derė́ti 

 *dʰí-dʰer-ti ( reduplicated present ) [ 2 ] [ 3 ] 
 Proto-Indo-Iranian: *dʰidʰarti 
 Proto-Indo-Aryan: *didʰarti 
 Sanskrit: दिधृतम् ( didhṛtám ) 

 Proto-Iranian: *didarti 
 ( perhaps ) Avestan: 𐬬𐬌𐬛𐬌𐬜𐬁𐬭𐬆𐬨𐬥𐬀- ( vidiδār ə mna- ) 

 *dʰe-dʰór-e ~ *dʰe-dʰr̥-ḗr ( reduplicated perfect ) [ 2 ] [ 3 ] 

##### daru Persian
91- Synonyms 
92-
93- 3 
94: Persian 
95-
96: Toggle Persian subsection 
97-
98- 3.1 
99- Etymology 
100-
101- 3.2 
102- Pronunciation 
103-
104- 3.3 
105- Noun 
106-
107- 3.3.1 
108- Derived terms 
--
224- Etymology
225- [ edit ] 
226-
227: Borrowed from Classical Persian دارو ( dâru , “ medicine, drug, gunpowder ” ) , itself derived from Middle Persian dʾlwkˈ ( dārūg , “ drug, medicament ” ) .
228-
229- Noun
230- [ edit ] 
231-
232- دارو • ( dārū ) ( plural دارولار ) 
233-
234- medicine , drug 
235-
236- spice 
237-
238- Declension
239- [ edit ] 
--
705- Etymology
706- [ edit ] 
707-
708: Borrowed from Classical Persian دَارُو ( dārū , “ medicine, drug, gunpowder ” ) , itself derived from Middle Persian dʾlwkˈ ( dārūg , “ drug, medicament ” ) . The sense of "alcohol" is semantically influenced by Hindustani .
709-
710- Pronunciation
711- [ edit ] 
712-
713- IPA ( key ) : /dɑˈru/ 
714-
715- Noun
716- [ edit ] 
717-
718- دارو • ( dârû )  m 
719-
720- ( slang ) alcohol 
--
753-
754- درمل ( darmal ) 
755-
756: Persian
757- [ edit ] 
758-
759- Etymology
760- [ edit ] 
761-
762: Inherited from Middle Persian [script needed] ( dʾlwkˈ /⁠dārūg⁠/ , “ drug, medicament ” ) , perhaps from Proto-Iranian *dā́rukah ( “ tree, wood ” ) . Compare Parthian 𐫅𐫀𐫓𐫇𐫃 ( dʾlwg /⁠dālūg⁠/ , “ plant, tree ” ) . Unrelated to English drug . [ 1 ] 
763-
764- Pronunciation
765- [ edit ] 
766-
767: ( Classical Persian ) IPA ( key ) : /daː.ˈruː/ 
768-
769- ( Dari, formal ) IPA ( key ) : [d̪ɑː.ɾúː] 
770-
771- ( Dari, formal ) IPA ( key ) : [d̪ɑː.ɾúː] 
772- ( Kabuli ) IPA ( key ) : [d̪ɑː.ɾúː] 
773-
774- ( Hazaragi ) IPA ( key ) : [d̪ɔː.ɾú] 
775-
776- ( Iran, formal ) IPA ( key ) : [d̪ɒː.ɹúː] 
777-
778- ( Tajik, formal ) IPA ( key ) : [d̪ɔ.ɾú] 
779-
--
858- Further reading
859- [ edit ] 
860-
861: Dehkhoda, Ali-Akbar ( 1931– ), “ دارو ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
862-
863- Urdu
864- [ edit ] 
865-
866- Etymology 1
867- [ edit ] 
868-
869- Etymology tree
870-
871- Proto-Indo-European *dóru 
872- Proto-Indo-Iranian *dā́ru 
873- Proto-Iranian *dā́ru 
--
875- Proto-Iranian *-kah 
876-
877- Proto-Iranian *dā́rukah ? 
878: Classical Persian دَارُو ( dārū ) bor. 
879- Urdu دارو 
880-
881: Borrowed from Classical Persian دَارُو ( dārū , “ medicine, drug, gunpowder ” ) , itself derived from Middle Persian dʾlwkˈ ( dārūg , “ drug, medicament ” ) .
882-
883- Pronunciation
884- [ edit ] 
885-
886- ( Standard Urdu ) IPA ( key ) : /d̪ɑː.ɾuː/ 
887-
888- Noun
889- [ edit ] 
890-
891- دارو • ( dārū )  f ( Hindi spelling दारू ) 
892-
893- ( health ) medicine , drug , medication 
--
903- Etymology 2
904- [ edit ]
```


## [2026-09-05T20:07:12.777Z] TOOL CALL #37: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D9%86%D9%87%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B1%DB%8C%D9%88%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\" \\\n \"https://www.etymonline.com/word/throne\" \\\n \"https://www.etymonline.com/word/farm\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 128, root Dher 1: zenhar, andarz, darz, Dariush, bahador, throne, farm\" ; done",
 "description": "Archive more sources"
}
```


### [2026-09-05T20:07:18.620Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/922c57c923cddcea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7af55838b31c7bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/334ce303b96994ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae29fa1402eaa3ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b893df06703e275.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/860b3a03aca4ef89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d18c30a263f37233.txt
```


## [2026-09-05T20:07:22.379Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 922c57c923cddcea d7af55838b31c7bb 334ce303b96994ee ae29fa1402eaa3ca 6b893df06703e275; do echo \"###### $f\"; awk '/^ Etymology$/{p=NR} {a[NR]=$0} END{}' $f.txt >/dev/null; grep -n -A4 \"^ Etymology\" $f.txt | grep -v \"^\\s*--$\" | head -40; echo; done",
 "description": "Read etymologies from archived pages"
}
```


### [2026-09-05T20:07:24.101Z] TOOL RESULT

```
###### 922c57c923cddcea
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
154: Etymology
155- [ edit ] 
156-
157- From Middle Persian [script needed] ( zynhʾl /⁠zēnhār⁠/ ) , originally an imperative command of 𐭬𐭭 ( MN /⁠az⁠/ , “ from, of ” , modern از ) + 𐭦𐭭𐭤 ( ZNH /⁠ēn⁠/ , “ this ” , modern این ) + Proto-Iranian *hār- ( “ to guard; to observe ” , from Proto-Indo-European *ser- ( “ to warn ” ) ) : "guard against this; beware of this", but used as a noun already in Middle Persian with the current meanings.
158-

###### d7af55838b31c7bb

###### 334ce303b96994ee
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
105: Etymology 
106-
107- 3.2 
108- Pronunciation 
109-
201: Etymology
202- [ edit ] 
203-
204: Etymology tree
205-
206- Proto-Indo-European *dʰer- ? 
207- Proto-Indo-European *dʰerǵʰ- 
208- Proto-Indo-Iranian *dʰarȷ́ʰ- 
983: Etymology
984- [ edit ] 
985-
986: Etymology tree
987-
988- Proto-Indo-European *dʰer- ? 
989- Proto-Indo-European *dʰerǵʰ- 
990- Proto-Indo-Iranian *dʰarȷ́ʰ- 

###### ae29fa1402eaa3ca
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
144: Etymology
145- [ edit ] 
146-
147- Learned borrowing from Old Persian 𐎭𐎠𐎼𐎹𐎺𐎢𐏁 ( d-a-r-y-v-u-š /⁠Dārayavaʰuš⁠/ ) , through an older transcription. Probably first used by Mirza Aqa Khan Kermani in 1909, who first transliterated Henry Rawlinson 's 1848 transcriptions of Old Persian into Arabic script rather than the Greek forms current in nineteenth-century Iran. [ 1 ] Rawlinson transliterates 𐎭𐎠𐎼𐎹𐎺𐎢𐏁 ( d-a-r-y-v-u-š /⁠Dārayavaʰuš⁠/ ) as Dáryawush . Doublet of داراب ( dârâb ) and دارا ( dârâ ) 
148-

###### 6b893df06703e275
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
152: Etymology
153- [ edit ] 
154-
155- Borrowed from Middle Mongol ᠪᠠᠭ᠋ᠠᠲᠤᠷ ( baɣatur ) , attested after the Mongol conquest in the 1200s.
156-
```


## [2026-09-05T20:07:45.194Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### andarz\"; grep -n -i \"andarz\\|Middle Persian\\|Etymology\" d7af55838b31c7bb.txt | head -30; echo; echo \"### darz tree\"; sed -n '201,240p' 334ce303b96994ee.txt; echo \"### darz 983\"; sed -n '983,1030p' 334ce303b96994ee.txt",
 "description": "Read andarz and darz pages"
}
```


### [2026-09-05T20:07:45.255Z] TOOL RESULT

```
### andarz

### darz tree
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *dʰer- ? 
 Proto-Indo-European *dʰerǵʰ- 
 Proto-Indo-Iranian *dʰarȷ́ʰ- 
 Proto-Iranian *darj- 
 Proto-Iranian *darjakah, *dārjakah 
 Middle Persian [script needed] ( dlc /⁠darz⁠/ ) 
 Classical Persian دَرْز ( darz ) bor. 
 Arabic درز 

 Borrowed from Classical Persian دَرْز ( darz ) . Borrowed earlier already as طَرْز ( ṭarz ) .

 Noun
 [ edit ] 

 دَرْز • ( darz )  m ( plural دُرُوز ( durūz ) ) 

 seam , suture 

 ( anatomy ) suture , a joining in the skull etc.

 Declension
 [ edit ] 

 Declension of noun دَرْز ( darz )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

### darz 983
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *dʰer- ? 
 Proto-Indo-European *dʰerǵʰ- 
 Proto-Indo-Iranian *dʰarȷ́ʰ- 
 Proto-Iranian *darj- 
 Proto-Iranian *darjakah, *dārjakah 
 Middle Persian [script needed] ( dlc /⁠darz⁠/ ) 
 Persian درز 

 Inherited from Middle Persian [script needed] ( dlc /⁠darz⁠/ ) , [ 1 ] from Proto-Iranian *darjakah, *dārjakah , from *darj- , from Proto-Indo-Iranian *dʰarȷ́ʰ- , from Proto-Indo-European *dʰerǵʰ- ( “ to bind fast ” ) , possibly from *dʰer- . [ 2 ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈdarz/ 

 ( Dari, formal ) IPA ( key ) : [d̪äɹz] 

 ( Dari, formal ) IPA ( key ) : [d̪äɹz] 
 ( Kabuli ) IPA ( key ) : [d̪äɹz] 

 ( Hazaragi ) IPA ( key ) : [d̪äɹz] 

 ( Iran, formal ) IPA ( key ) : [d̪æɹz] 

 ( Tajik, formal ) IPA ( key ) : [d̪äɹz] 

 Rhymes: -arz 

 Readings

 Classical reading ? 

 darz

 Dari reading ? 

 darz

 Iranian reading ? 

 darz

 Tajik reading ?
```


## [2026-09-05T20:07:46.694Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### throne\"; grep -n -i \"thronos\\|throne\" 860b3a03aca4ef89.txt | head -20; echo; echo \"### farm\"; grep -n -i \"firmus\\|firma\\|farm (n\" d18c30a263f37233.txt | head -20",
 "description": "Read etymonline throne and farm"
}
```


### [2026-09-05T20:07:46.756Z] TOOL RESULT

```
### throne
1:URL: https://www.etymonline.com/word/throne
4:TITLE: Throne - Etymology, Origin & Meaning
6:Throne - Etymology, Origin & Meaning 
21: Origin and history of throne 
23: throne (n.) 
25: c. 1200, trone , "the seat of God or a saint in heaven;" c. 1300, "seat occupied by a sovereign, potentate, or dignity on earth," from Old French trone (12c., Modern French trône ), from Latin thronus (Medieval Latin tronus ), from Greek thronos "elevated seat, chair, throne," according to Watkins from suffixed form of PIE root *dher- "to hold firmly, support" (source also of Latin firmus "firm, steadfast, strong, stable," Sanskrit dharma "statute, law").
27: Attested from late 14c. figuratively as a symbol of royal power. The colloquial meaning "toilet" is by 1960; comparison of the toilet to a throne is by 1922. The classical -h- begins to appear in English from late 14c. Related: Thronal .
30: Entries linking to throne 
32: dethrone (v.) 
34: c. 1600, "remove or drive from a throne, depose;" see de- (privative) + throne . Figurative sense "divest of power or authority" is from 1640s. Related: Dethroned ; dethroning .
36: enthrone (v.) 
38: "to place on a throne, exalt to the seat of royalty," c. 1600, from en- (1) + throne (n.). Replacing enthronize (late 14c.), from Old French introniser (13c.), from Late Latin inthronizare , from Greek enthronizein . Also simply throne (v.), late 14c., from the noun in English. Related: Enthroned ; enthroning .
62: c. 1300, "throne of a bishop, archbishop, or pope," also "throne of a monarch, a goddess, the Antichrist, etc.," from Old...French sie "seat, throne; town, capital; episcopal see," from Latin sedem (nominative sedes) "seat, throne, abode, temple...
66: "a seat with a back, intended for one person," early 13c., chaere, from Old French chaiere "chair, seat, throne" (12c.; Modern...French chaire "pulpit, throne;" the humbler sense having gone since 16c. with the variant form chaise), from Latin cathedra...
70: (source also of Old Frisian stol, Old Norse stoll, Old High German stuol, German Stuhl "seat," Gothic stols "high seat, throne...The English word was originally used of thrones (as in cynestol "royal seat, throne") and in early Middle English still of...
74: From 1640s as "act of coming to a position or into possession," especially in reference to a throne....
88: Share throne 
92: https://www.etymonline.com/word/throne Copy 
95: <a href="https://www.etymonline.com/word/throne">Etymology of throne by etymonline</a> Copy 
98: Harper, D. (n.d.). Etymology of throne. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/throne Copy 

### farm
23: farm (n.) 
25: c. 1300, "fixed payment (usually in exchange for taxes collected, etc.), fixed rent," from Old French ferme "a rent, lease" (13c.), from Medieval Latin firma "fixed payment," from Latin firmare "to fix, settle, confirm, strengthen," from firmus "strong; stable," figuratively "constant, trusty" (from suffixed form of PIE root *dher- "to hold firmly, support").
29: Phrase buy the farm "die in battle," is from at least World War II, perhaps a cynical reference to the draftee's dream of getting out of the war and going home, in many cases to a peaceful farmstead. The simple term buy it as slang for "suffer a mishap," especially "to die" is attested by 1825, and seems to have been picked up in airmen's jargon. Meanwhile fetch the farm is prisoner slang from at least 1879 for "get sent to the infirmary," with reference to the better diet and lighter duties there.
34: mid-15c., "to rent (land)," from Anglo-French fermer , from ferme "a rent, lease" (see farm (n.)). The agricultural sense is from 1719. Original sense is retained in to farm out .
50: late 14c., "one who collects taxes, etc.," from Anglo-French fermer , Old French fermier "lease-holder," from Medieval Latin firmarius , from firma "fixed payment" (see farm (n.)). In the agricultural sense, 1590s, replacing native churl and husbandman .
```


## [2026-09-05T20:07:52.439Z] TOOL CALL #41: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/128.jpg"
}
```


### [2026-09-05T20:07:52.456Z] TOOL RESULT

```

```


## [2026-09-05T20:08:05.580Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(sorted(d.keys()))\n\" ; echo \"=== CEL search in repo ===\"; grep -rn \"\\\"CEL\" data/extracted/*.json 2>/dev/null | head -3; ls data/extracted/ | head -20",
 "description": "List ref abbreviations"
}
```


### [2026-09-05T20:08:07.461Z] TOOL RESULT

```
['AEF', 'AFA', 'AFM', 'AHD', 'AHM', 'AID', 'AIN', 'AKD', 'AKM', 'AMD', 'ARB', 'ARK', 'ARM', 'ARP', 'ARY', 'AVG', 'AWH', 'BLY', 'BQT', 'BRT', 'BST', 'CEL', 'DEV', 'DMO', 'DOZ', 'DRM', 'DVS', 'DZA', 'EAV', 'ETM', 'FAF', 'FFD', 'FIB', 'FNI', 'FRS', 'FSD', 'FSF', 'FVA', 'FVF', 'FVQ', 'FVS', 'FWE', 'GPL', 'HID', 'HJB', 'HRN', 'HUB', 'IEC', 'IRN', 'IRT', 'ISS', 'KAS', 'KFL', 'KGW', 'KLN', 'KNT', 'LAM', 'LAT', 'LEW', 'LKT', 'LST', 'MAG', 'MFL', 'MMF', 'MON', 'MPP', 'MZF', 'NAT', 'NFI', 'NYB', 'OEW', 'OXF', 'PEI', 'PHD', 'PHN', 'PLA', 'POK', 'PRT', 'RCH', 'ROE', 'SAP', 'SBK', 'SDQ', 'SHP', 'SIN', 'SKT', 'SLW', 'SNB', 'SNS', 'SOD', 'SOG', 'SOR', 'SPG', 'SYN', 'TAD', 'TLM', 'TTS', 'TYL', 'TZF', 'UNV', 'VDQ', 'VGH', 'VIE', 'VOP', 'VSF', 'WEB', 'WLD', 'ZAP', 'ZAW', 'ZFS', 'ZMA']
=== CEL search in repo ===
(eval):5: no matches found: data/extracted/*.json
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-05T20:08:10.121Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['CEL','MON','ETM']:\n    print(k, json.dumps(d[k],ensure_ascii=False)[:900]); print()\n\"",
 "description": "Check CEL entry"
}
```


### [2026-09-05T20:08:11.885Z] TOOL RESULT

```
CEL {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Haus printing is not digitised anywhere found. HathiTrust full-text search (search-only volumes) can confirm whether a word occurs, via a browser."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
```


## [2026-09-05T20:08:18.218Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"\\[pdf page\" FFD_pages.txt | head -3; echo \"===\"; grep -n \"داشتن\\|پنداشتن\" FFD_pages.txt | head -20",
 "description": "Grep FFD for dashtan"
}
```


### [2026-09-05T20:08:18.281Z] TOOL RESULT

```
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
===
359:1۳ 5 : داشتن
424:فعل آرزویی فعلی است که برداشتن آرزوی انجام‌دادن یاگرفتن کاری دلالت می‌کند.
1218:پنداشتن
1219:«پنداشتن» بازماندةٌ ۳هاققل 27 024 فارسی میانه است. 020: به» 5 اين» 43318:
1220:داشتن» روی هم به معنی «به چیزی شمردل).
1352:«هیجان‌داشتن» و 2۵۵414۵8 به معنی «لرزیدنْ» است.
1380:پیشوند فعلی است. ۳370 صورت بالاندةٌ ريشهٌ 77870 است و 77870(«گامبرداشتن» معنی
1440:داشتن
1445:ريشهٌ 487 است. 447 به معنی «داشتن» است.
2313:2 (ريشةٌ ضعیف + ۳72[7) ۳۶ 7 : (ريشه < داشتن) ۱۲ ۰۱۵ ۵۲
2329:40 : (ريشه - هیجان‌داشتن) ۴۹
2667:۷۲:1۵ 0 (ريشه - گام‌برداشتن) ۵۰
```


## [2026-09-05T20:08:24.194Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'NR<=1440 && /^\\[pdf page/{p=$0} END{}' FFD_pages.txt; for L in 1218 1440; do echo -n \"line $L -> \"; awk -v L=$L 'NR<=L && /^\\[pdf page/{p=$0} NR==L{print p}' FFD_pages.txt; done; echo \"=== context 1215-1225 ===\"; sed -n '1214,1226p' FFD_pages.txt; echo \"=== context 1438-1450 ===\"; sed -n '1436,1452p' FFD_pages.txt",
 "description": "Locate FFD pages for pendashtan and dashtan"
}
```


### [2026-09-05T20:08:26.036Z] TOOL RESULT

```
line 1218 -> [pdf page 1]
line 1440 -> [pdf page 1]
=== context 1215-1225 ===
پسندید < فارسی میانه 02820676. 02820670 ماد ماضی جعلی است و از ماده
مضارع ساخته شده است.
پسند + فارسی میانه 028300 < ایرانی باستان 0211-8200-8*. برای 2 آرای. 030
پیشوند فعلی است. ريشةٌ ۶224 به معنی «به نظرآمدن» است.
پنداشتن
«پنداشتن» بازماندةٌ ۳هاققل 27 024 فارسی میانه است. 020: به» 5 اين» 43318:
داشتن» روی هم به معنی «به چیزی شمردل).
پوزیدن
«پوزید» مادهٌ ماضی جعلی است و از مادهٌ مضارع ساخته شده است.
پوز < فارسی میانه 062 < ایرانی باستان 2-[0۵0*. برای 2 + آرای. 8 صورت
اصلی [۳۵ است» [به جای 8 آمده است. مادهٌ ماضی 052 در فارسی میانه :00 بوده
[pdf page 49]
با فعلهای فارسی دری
=== context 1438-1450 ===
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی باستان.
7 صورت ضعیف ريشةٌ 447 است. برای 1۵ -> آراست. 4351 به قیاس با 137 1351
به‌وجود آمده است.
دار < فارسی میانه 437 < ایرانی باستان 437-۵*. برای 2 -> آرای. 437 صورت بالانده
ريشهٌ 487 است. 447 به معنی «داشتن» است.
[pdf page 58]
ماده‌های ماضی و مضارع فارسی دری ۳ تا ۵۳
دانستن
دانست < فارسی میانه 420191. 432181 در فارسی میانه مادهٌ ماضی جعلی است.
دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
دراییدن
درایید ج فارسی میانه 473[14. در فارسی میانه 47316 مادءٌ ماضی جعلی است که از
```


## [2026-09-05T20:08:41.732Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nlines=open('FFD_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.match(r'\\s*\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if i in (359,1218,1440,1445):\n        print(i, cur, l[:60])\nEOF",
 "description": "Map FFD lines to pdf pages"
}
```


### [2026-09-05T20:08:43.728Z] TOOL RESULT

```
359 17 1۳ 5 : داشتن
1218 48 پنداشتن
1440 57 داشتن
1445 57 ريشهٌ 487 است. 447 به معنی «داشتن» است.
```


## [2026-09-05T20:09:01.166Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f,'formfeeds:',t.count('\\f'),'lines:',t.count('\\n'))\nEOF\nls ocr/ 2>/dev/null; ls ocr/BQT 2>/dev/null | head",
 "description": "Check BQT text file page structure"
}
```


### [2026-09-05T20:09:03.277Z] TOOL RESULT

```
BQT_v1_pages.txt formfeeds: 776 lines: 32485
BQT_v2_pages.txt formfeeds: 683 lines: 41070
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
```


## [2026-09-05T20:09:05.906Z] TOOL CALL #48: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT/ | tr '\\n' ' '; echo; ls data/verification/sources/refs/ocr/BOOK/ | tr '\\n' ' '",
 "description": "List cached BQT OCR pages"
}
```


### [2026-09-05T20:09:05.981Z] TOOL RESULT

```
0001.png 0001.txt 0049.png 0049.txt 103.vision.txt 1225.png 1225.txt 1225.vision.txt 1275.png 1275.txt 1339.png 1339.txt 1357.png 1357.txt 1382.png 1382.txt 1385.png 1385.txt 1385.vision.txt 1445.png 1445.txt 1445.vision.txt 1452.png 1452.txt 1455.png 1455.txt 1488.png 1488.txt 1803.png 1803.txt 180.png 180.vision.txt 181.png 181.vision.txt 1878.png 1878.txt 1900.png 1900.txt 1908.png 1908.txt 2143.png 2143.txt 220.vision.txt 2222.png 2222.txt 2246.png 2246.txt 2246.vision.txt 2407.png 2407.txt 31.vision.txt 58.vision.txt 70.vision.txt 72.vision.txt 733.png 733.vision.txt 
100.png 101.png 102.png 103.png 104.png 105.png 106.png 108.png 109.png 110.png 111.png 112.png 114.png 117.png 118.png 120.png 121.png 123.png 124.png 125.png 126.png 311.png 33.png 39.png 46.png 54.png 69.png 71.png 72.png 73.png 74.png 75_greek_latin_arrow.png 75.png 76.png 77.png 78.png 79.png 80.png 81.png 82.png 83.png 85.png 86.png 87.png 88.png 89.png 90.png 91.png 92_pahlavi_box.png 92.png 94.png 95.png 96.png 99.png
```


## [2026-09-05T20:09:15.842Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1055 --image 2>&1 | head -60",
 "description": "Fetch BQT page 1055"
}
```


### [2026-09-05T20:09:17.461Z] TOOL RESULT

```
no scan of BQT covers printed page 1055 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:09:20.256Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "Check BQT scans config"
}
```


### [2026-09-05T20:09:22.062Z] TOOL RESULT

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
```


## [2026-09-05T20:09:26.644Z] TOOL CALL #51: Bash

```json
{
 "command": "grep -o '\"src\": \"BQT\"[^}]*' data/verification/page-12[0-9].json | head -8; echo \"-----\"; grep -o '\"ref\": \"BQT:[0-9]*\"[^}]*' data/verification/page-12[0-9].json | head -10",
 "description": "See how prior pages cited BQT"
}
```


### [2026-09-05T20:09:26.702Z] TOOL RESULT

```
data/verification/page-120.json:"src": "BQT",
data/verification/page-124.json:"src": "BQT",
data/verification/page-124.json:"src": "BQT",
data/verification/page-127.json:"src": "BQT",
data/verification/page-127.json:"src": "BQT",
data/verification/page-125.json:"src": "BQT",
data/verification/page-125.json:"src": "BQT",
data/verification/page-121.json:"src": "BQT",
-----
data/verification/page-121.json:"ref": "BQT:869",
data/verification/page-121.json:"ref": "BQT:854",
data/verification/page-123.json:"ref": "BQT:837",
data/verification/page-123.json:"ref": "BQT:822",
data/verification/page-123.json:"ref": "BQT:820",
data/verification/page-124.json:"ref": "BQT:169",
data/verification/page-124.json:"ref": "BQT:418",
data/verification/page-124.json:"ref": "BQT:2211",
data/verification/page-124.json:"ref": "BQT:2214",
data/verification/page-124.json:"ref": "BQT:818",
```


## [2026-09-05T20:09:29.944Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 -c \"\nimport json\nfor p in [121,123,124]:\n    d=json.load(open(f'data/verification/page-{p}.json'))\n    for e in d['entries']:\n        for n in e['nodes']:\n            for r in n.get('ref_check',[]):\n                if r['ref'].startswith('BQT:'):\n                    print(p, r['ref'], r['status'], r['note'][:400]); print()\n\" | head -60",
 "description": "Read prior BQT ref_check notes"
}
```


### [2026-09-05T20:09:31.705Z] TOOL RESULT

```
121 BQT:809,843 supports BQT_v2_pages.txt leaf 269 (≈ printed 809, start of the دار entries): Mo'in's footnote 9 'پهلوی dār «تاوادیا ۹۱۲»، اوستا dāuru- (چوب)، قس: ارمنی ... هندی باستان dāru- (چوب)، کردی و بلوچی dār ... و رک: هوبشمان ۲۲۵'. Leaf 300 (≈ 843): 'درگر = باکاف فارسی بروزن دختر، درودگر را گویند' + footnote 'مخفف «درودگر»'. Both pages say what the arrow says.

121 BQT:869 partial BQT_v2_pages.txt leaf 329 (its foot carries 'بقیه در صفحهٔ ۸۷۰', so this is printed p.869) opens the بیان دهم 'در دال بی نقطه با فا' and has دف with 'دف زدن', 'دفتین'. The page does have the word Nourai wants, but its footnote derives Arabic دف from Hebrew/Sumerian, not from Persian داریه.

121 BQT:840,842,843 supports BQT_v2_pages.txt leaf 302 (≈ printed 842) 'درو ۳ = بروزن سرود، بمعنی صلوات است' with Mo'in's footnote 'پهلوی drūt (صحت، آرامش) ... drōd (آرزوی خیر و برکت) از ریشهٔ *drvatāt (ارمنی drut) و از اوستا drvatāt- «بارتولمه ۷۸۹»'; leaf 296 (≈ 836–840) carries درست with the Pahlavi/Old-Persian forms; leaf 300 (≈ 843) has درگر/درودگر.

121 BQT:854 partial the درونه entry with Mo'in's footnote 'drūna (کمان، قوس) بلوچی drīn' is at BQT_v2_pages.txt leaf 305, i.e. printed p.845±3 (its foot reads 'بقیه در صفحهٔ ۸۴۸'), not p.854; p.854 falls in the دژ section. The content Nourai wants is in Borhan, but the page number is off by about nine.

123 BQT:837 partial BQT_v2_pages.txt leaf 297 (printed 837), Mo'in's footnote to درشت: '... (جرأت، جسارت، کوشش) و اوستا darši ... و هوبشمان از ریشهٔ ایرانی *družt- می‌داند'; i.e. Mo'in cites Skt dhṛṣṇu- next to Hübschmann's competing *družta-, so the page supports Nourai's family but records the rival derivation as well.

123 BQT:822 partial BQT_v2_pages.txt leaf 282 (printed 822), Mo'in's footnote: 'دایه — ... اوستا daēnu (مادّه [از جانوران])، پهلوی dāyag (دایه)، هندی باستان ریشهٔ dhā- (شیر دادن)، ارمنی dayeak (دایه، مربّی)، کردی dāyik و dāyā (مادر) ... معرّب آن دایة (ماماه، قابله)'. Supports دایه fully; the page has no entry for دایی 'mother's brother'.

123 BQT:820 supports BQT_v2_pages.txt leaf 280 (printed 820), Mo'in's two footnotes: 'دانگ — ... پهلوی dāng، پارسی باستان (بنقل یونانی) δανάκη ... ارمنی dang، عربی معرّب دانق ... اصلاً همریشهٔ دانه (ه.م) است' and 'دانه — ... پهلوی dān(ag)، اوستا dānō-karša- (دانه‌کش)، هندی باستان dhānā- (دانهٔ گندم)، بلوچی dān(ag)، گیلکی dāna ...'. Exactly Nourai's two words, on exactly the page he cites.

124 BQT:169 supports Borhān-e Qāte‘ vol.1, leaf 387 of BQT_v1_pages.txt (running head '۱۶۹') carries the headword «اندام - بروزن انجام، معروف است که بدن و عضو آدمی باشد»; Mo'in's etymological footnote on that page is not legible in this OCR.

124 BQT:418 supports vol.1 leaf 644 = p.418, the «پنام» entry; Mo'in's long footnote there reads «در اوستا paiti-dāna ... در وندیداد بند ۹ پنام جزو اسلحه و لوازم یک مرد جنگی بشمار آمده ... دو قطعه پارچهٔ سفید که بروی دهان آویخته», and it prints the Avestan with -n-, contradicting Nourai's 'paiti-dâma'. Same page carries the Shahīd Balkhī couplet the chart quotes.

124 BQT:2211 supports Borhān vol.4, pdf page 294 = printed 2211 (offset printed = pdf+1917): headword «نهاد ... ماضی نهادن است که بمعنی گذاشتن باشد» with Mo'in's footnote «پهلوی nihātan ... ایرانی باستان *ni-dā- ... اوستا dāح بارتولمه ... هرن».

124 BQT:2214 supports Borhān vol.4, pdf 297 = printed 2214: the نهان block (نهان‌پیکران، نهان‌خانه، نهان‌دره); the simple headword نهان falls in the same two-column spread.

124 BQT:818 supports Borhān vol.2, leaf 278 of BQT_v2_pages.txt = printed p.818 (running-head calibration leaf+540, checked against داد=807 and داور=821): headword «دان بر وزن نان، مطلق دانه را گویند ... و چون در آخر کلمه آید معنی ظرفیت بخشد، همچو قلمدان و کیفدان و قهوه‌دان», with footnote 7 'اوستا dāna-، هندی باستان dhāna-، ... پهلوی dān'.

124 BQT:807 supports vol.2 leaf 267 = p.807 (running head داد): the داد entry 'وبمعنی راستی و عدل و عدالت', footnote 8 'پهلوی dāt (قانون) ... پارسی باستان dāta- ... قس: هندی باستان dhāta- ... بارتولمه', and the neighbouring headword 'داتوبر ... بمعنی داور و دادری' with the note 'پهلوی است، رک: داور'.

124 BQT:814 not_found vol.2 leaf 274 = p.814 by the same calibration is the داس‌/داستان page (داسار، داستاره، داستان، داسخاله); it contains nothing on داد or داور. Its Mo'in footnote (deriving داستان from Pahlavi dātastān 'حق، قانون') belongs to node #14, not here.

124 BQT:821 supports vol.2 leaf 281 = p.821 (running head داوردان): 'داور - بر وزن خاور، نام خدای عزوجل است - و پادشاه عادل ... و دراصل دادور بروزن دادگر بوده', with the Latin-script footnote giving Pahl. dātōbar/dātbar/dātwar, Av. dātō-bara, Arm. datavor.

124 BQT:862 supports vol.2 leaf 322 = printed p.862 by the leaf+540 calibration (verified against داد=807, دان=818, داور=821): the page carries the دست‌/دستوار block ('دستوار ... دستوانه') immediately preceding the دستور headword; دستان stands a few pages earlier in the same دست‐ run.
```


## [2026-09-05T20:09:37.863Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 270 273; do echo \"######## v2 leaf $L (printed $((L+540)))\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -70; done",
 "description": "Read BQT pages 810, 813"
}
```


### [2026-09-05T20:09:39.405Z] TOOL RESULT

```
######## v2 leaf 270 (printed 810)
   ‫وت‬                                                                                                         ‫دارا‬
‫داادرار کردن" » با دال ابجد ‪,‬‬                                 ‫است در هندوستان ‪ -‬و داامروبی که آنرا‬
‫کنابه ازدیر باسدن وشات داشتن‪ -‬ومدارا کردن‪-‬‬                    ‫‪ -‬و بممنی داشتن و امر‬           ‫وزبند‬
                                                                                                  ‫ی دگرا‬
                                                                                                       ‫ظمفل‬
                                   ‫باشد‬   ‫ویسار ماندن‬         ‫بداشتن‌هم هت ‪ -‬وبمعنی داورهم آمده است که‬
                                                              ‫خانه‬      ‫بی‬
                                                                         ‫رو‬‫ع‪-‬‬
                                                                            ‫یشد‬
                                                                              ‫مکی از نامهای خدایتمالی با‬
‫ممدوده‬       ‫قریں ‪ - ۸‬با همزه‬              ‫دار‬
                                                                                         ‫ومحله رگاونند ‪.‬‬
‫ومتصوره هردوآمده است وسکون‌فا‪ .‬هرچیز که‬
                                                               ‫دارا = بروزن خارا ‪ ,‬نام بادشاه مشپور‬

‫وینچره‬       ‫وامثال آن‬     ‫وخواه سنوای‬     ‫آن مححری‬
                                                               ‫است که دارای! کبر‪,‬اشد واورا داراب نیز گوبند‪.‬‬
                                                               ‫ولو درزمان سکندر کشته شد ودارای اصفر پس‬
‫را نز گربند که دریش خاله مابن دو‬                ‫ومحجری‬
                                                               ‫اوست ‪١‬‏ ‪ -‬ویمعنی داأرنده هم‌هست ‪ _ ۴‬واشاره‬
‫وهد‌وصفةٌ درخاله راز گود‪,‬‬
                        ‫باژو ی درساژ لد‪ -‬ک‬                      ‫مذات بارتمالی ‪ -‬و کنابه از بادشاهان باشد ‪-‬‬
                                                               ‫که در ته خم‬        ‫ویبزند‬
                                                                                       ‫و دردی رکان‬            ‫وای‬
                                                                                                                ‫ل‬
         ‫‪۰‬‬   ‫است ات و نام داروبی هی‌هست‬          ‫هم ‪۹‬‬                                                     ‫‪/‬‬   ‫‪۹۳۹ ۳1‬‬




‫دادای ‏* بر وزن بارای » بمعنی‬                                  ‫دار اب = بر وزن فاراب » بمعنی رب‬
‫پرورد کار است حل و حلاله ‪ ۳۳‬و کنانه از بادشاه‬
                                                               ‫آب است که پرورنده و رب‌النوع خوانند ‪- ۴‬‬
‫ویرورنده راهم کفته‌اند کهآ نرارب‌النوع‬          ‫مر هت‬
                                                               ‫و دلرای اکیر را نیز گویند م‪ ۳‬ونام دخترزادء‬
                                            ‫خوانند؟ ‪.‬‬
                                                               ‫مههمینن‌هم‌هست‪ -‬وبمعنی کروفروشان‌ودو کت‬
‫دارای گو نه ‪١‬‏ باکان فارسی بواو‬                                               ‫وخودنمامی هم بنظر آمده امت ® ‪.‬‬

                                                                ‫دار ات ‪ -‬بانای‌فرشت ‪ ,‬شأن ووشکت‬
                                   ‫رب‌النوع خوانند ‪.‬‬                                        ‫وکر و فر ‪ ۷‬باشد ‪.‬‬
    ‫بای اه امال شد را اروق تا‬                                        ‫ها وذازات تفاس ی‬
                                                 ‫‪ - ۴‬پپلوی ‪( ۷2720‬دارنده) «متای ‪. ۱۷۲۰‬‬
                    ‫ظ » از برساخته‌های فرقةٌ آذ رکیوان ‪ .‬رك‪ :‬دارای گونه > دارای ‪.‬‬                ‫‪۴‬‬
                                   ‫‪ - ۴‬پهلوی ‪ « 2720‬تربکه ‪ » ۸4‬رك ‪ :‬داراء دارنوش ‪.‬‬
 ‫(نسابوری)‬      ‫‪ .‬معر‌ ی‬    ‫نزن ویکوب‬     ‫‪۹ ۹‬‬            ‫«رارات» (ه‪.‬م‪۰ ).‬‬     ‫® ‪ -‬بان هعتی ممحف‬

 ‫حاشة تاربخ بهقی) ‪ ۰‬رك‪ :‬تاربخبیهقی‬               ‫کومد‪ :‬دارات‌نمودی چوعلی درصف‌صفن» (ادب لثابوری‬

                           ‫رك‪ :‬داردار کردن ‪.‬‬         ‫‪۲‬‬               ‫چاپ د کتر فیاش ص ‪۷۰٩‬‏ متن وحاشیه ‪.‬‬
 ‫آمده‪« :‬دارا‪.‬‬      ‫«رارافز ین» (درابز بن) ) ھ‪.‬م‪ ( .‬درفرهنث رشدی‬               ‫‏‪ - A‬تمعتی اول مصحف‬

 ‫قزین وداروزین » وداربزین بممنی تکیه گاه و محجرتخت وصفه و بام وتکیه گاهمطلق ‪ .‬ابوالفرج‬
                                                                                              ‫(رونی) کوید ‪:‬‬


                                                                        ‫تکیه بربالش اقبالش دار‬
 ‫دردبوان ابوالفرح رولی چاپ ارمغان ص ‪ < ۷۲‬دارافرین » در بیت فوقآمده و درتاریخ‬
 ‫هقی چاپ ادیب ص ‪:۱۵۵‬دارآ فرین‌ها» ثبت شده ولی در چاپد کتر فباض « دارافزین‌ها ‪٩‬‏ و در‬
 ‫رکه ‪ :‬درایزین؛‬      ‫ی مشبك» آمده وبازاوصحیح است‬               ‫دارافز‬     ‫برلن‌صی‪۹۷‬‬   ‫سقرنامةٌ ناسرخسرو اپ‬

‫از برساخته های فرقةٌ‬          ‫ظ‪,‬‬    ‫‪۹‬‬            ‫‪.‬‬   ‫داربوش‬   ‫رکه‪ :‬دارا ‪ ,‬داراب »‬      ‫‪٩‬‏‬            ‫‪.‬‬   ‫داریزین‬

                                                                 ‫رکه ‪ :‬داراب ‪e‬‏ دارای ‪۰‬‬     ‫است ‪۰‬‬    ‫آذرکیوان‬

######## v2 leaf 273 (printed 813)
 ‫دای‬                                                                                              ‫سور‬
‫چوب بندند کتباوتران ودمگر پرندکان برآن‬                 ‫دار و برد بادال ابجد درآخربروزن‬
            ‫‪.‬‬      ‫بنشینند ‪ -‬وترجمة لفظ هم‌هست‬       ‫ساز وبرگك » بمعنی طاق وترتب گویرودارو کر‬
‫بر وزن طاس » افزاری است‬       ‫داس‬                                             ‫وفر وتبخترباشد ‪.‬‬
‫که بدان‌غله درو کنند وبعربی‌منجل خوانند‪- ۴‬‬            ‫داره = بروزن چاره ‪ ۰‬وطیفه وراب را‬
                                                      ‫وشفف دایره است ‪ -‬وهاله ماهر اثبز‬
                                                                                     ‫م‬  ‫کن‬
‫ده برسردانه‌های کندم‬
                   ‫وخهای‌سر تیزرانیزکوبن ک‬
                                                                                            ‫کفته‌اند ‪١‬‏ ‪#.‬٭‪#‬‬
‫وجوی است که درخوشه میباشد ‪ - ۴‬ونوعی از‬
‫اک ار با کت و تسیر (‪]۱‬‬                                ‫داره س با زای نقطه دار بروزن تازه »‬
 ‫ری‬     ‫رها‬
          ‫نک‬‫آایی‬
               ‫است دو‬             ‫هی‬
                                   ‫‪-‬و‬‫یتا‬
                                       ‫گ‌هس‬
                                          ‫هم‬         ‫آن است که دو چوب بلند را پر زمین فروبر ند‬
‫سداب خوائشدت ودهره رانز کفتمانه وآتسلاحی‬               ‫ماندڭك فاصله وجوب ‪re‬‏ عر ص بربالای آن دو‬


                                                                         ‫‪.‬‬    ‫)‪ (۱‬چش‪ :‬لخحر‬


  ‫« وازء»‬       ‫باین معنی مصحف‬     ‫‪۴‬‬          ‫‪۱‬ع‪-‬بنابینعربی است ‪ .‬رك ‪ :‬داظم لاطبا ‪.‬‬
                                                                                  ‫م‬
  ‫‪۴‬پ‪-‬لوی ‪ . 58‬هندی باستان ‪ ( 210۵1 -‬دای » کردی‬
                                             ‫پ‬                                 ‫‪۰‬‬   ‫( است‬   ‫و «واژه» ) ‪.‬م‬

                            ‫‪.‬‬   ‫ر که‪ :‬داسه‬    ‫‪۴‬‬        ‫‪.‬‬    ‫» گیلکی عق‬       ‫‪ 3‬بلوچی ‪« 551‬اسشق ‘‪aa‬‏‬

  ‫(‪fitanimon‬‏‬   ‫کولشمه ابت اپزارسی باستان ‪ .‬که در حالت فاعلی (‬
                                                             ‫‪-‬ری‬
                                                               ‫* دا‬
 ‫‏‪ raya‬مود مر کب از‪( 192۲84:‬دارا) ‪ ( ۷۵2۷ +‬یکی ) ؛ جمماً داردے‬
  ‫‪ .‬ابن نام دریهلوی دارای و داراب خوانده شدمو حرادبیات‬           ‫نیکی «بارتولمه ‪« ۸۳۲‬اشپیگل ‪۵‬‬
  ‫اسلامی دارا و داراب دواربوشآعدء ‪ .‬رکه ‪ :‬شاهان کیانی وهخامنشی آدثاررالباقیه بقلم نکارنده ‪.‬‬
                                        ‫مجلهٌ آموزش سال ‪ ۵۱‬شمار؛ ‪٩‬‏ ‪۳ ۰۱ -‬‬
 ‫ص‪ ۱1 - ۹‬و‪- ۷8۰‬دهرتسنلسلهٌ هخامتشی بدن عم‬
                                                                                   ‫خوانده شده‌اند‪:‬دارنوش‬
                                                                                    ‫اول باداربوش پزر کي‬
                                                                                     ‫سروشناسپ (‪-۱۲۵‬‬
                                                                                     ‫‏‪ ٩‬قم)؛ داریوش‬
                                                                                     ‫دوم پر اردشیر اول‬
                                                                                     ‫‏(‪(e. J ٩۰4 -4۲۶‬‬
                                                                                     ‫و داربوش سوم پر‬
                                                                                     ‫آرسان ونو داربوش‬
                                                                                      ‫دوم(‪۹۳۳-۰۳۳‬قی‪.‬م)‬
                    ‫نقش برجتةٌ داربوش بز رک در ابوان جنوبی‬                            ‫و اوست که مغلوب‬
                         ‫حیاط خزانه ‪ .‬تخت حمشید‪.‬‬                                            ‫اسکندر شد ‪.‬‬

                                                                                      ‫بقه از صفحه ‪۲۱۸‬‬
  ‫گوش ‪« .‬حافظط شیراژی‪. *۲۹۱‬‬            ‫وز خط رچشم یدش دار‬
                    ‫=‪( 76020‬فر) «لك ‪۲‬ص ‪۵۷٩‬‏ ۔‬
                                            ‫‪ 5108 = ۱‬درزی ج ‪ ۱‬ص ‪1 ۰۲1۰‬‬
   ‫» کردی و افغالی و بلرچی ‪078‬‬               ‫( وا ) « منای ‪¥‬‬         ‫‪ #‬دارو ‪ -‬پهلوی ‪1‬‬
   ‫«اسشق‪ »۳۲۵‬اصل آن مشکوك است ‪« .‬حویشمان ‪ ۳۲۵۲‬؛ دوا ‪ -‬آنجه بزشك برای معالجةٌ مار‬
                                                                                           ‫بخورد او دهد ‪.‬‬
```


## [2026-09-05T20:10:06.363Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 298 299 300; do echo \"######## v2 leaf $L (≈printed $((L+540)))\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"درمان\\|درز\\|درگر\\|درم \" | head -20; done",
 "description": "Locate darman in BQT"
}
```


### [2026-09-05T20:10:08.002Z] TOOL RESULT

```
######## v2 leaf 298 (≈printed 838)
######## v2 leaf 299 (≈printed 839)
######## v2 leaf 300 (≈printed 840)
10:‫عمش کنن را منخص سازند ‪ -‬ویمعئی درشادی‌غم‬                  ‫‪ ۰‬و عصی یخی را گوند که درزیر‌ناودان‬           ‫گوند‬
36:       ‫‪ - ۸‬از درماندن؟‪.‬‬        ‫بر منیع ‪ 027۲721‬نیب ک‪ »:۹‬ورك‪ :‬اسثق مهوبشمان‪4۵‬ه ‪.‬‬                          ‫‪1‬‬
43:  ‫‪ #‬درم ‪ -‬بکراول وفتح دوم پهلوی ‪ « 772۳1‬منای ‪ ۱۷۲:۲۰‬و ‪ < 0۳5201‬تاوادیا‬
```


## [2026-09-05T20:10:10.794Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==301' BQT_v2_pages.txt | sed -n '25,60p'",
 "description": "Read BQT leaf 300 footnotes"
}
```


### [2026-09-05T20:10:12.654Z] TOOL RESULT

```
                                           ‫گومنت ‪:‬‬        ‫در لاله = بفح اول و صکون ثالی‬
 ‫»ج دووا‬
       ‫لا‬‫عمان‬
            ‫دروزن فر‬
                   ‫درهان ب‬                                 ‫وضم کاف فارسی ولام الف ولام مفتوح » بمعنی‬
‫ودار‌باشد ‪ - ۷‬ویمعتی درمالده ‪ -‬واهر باینمعنی‬               ‫کدارله است که بخ زبرناردان‌باشد وآن درهوای‬
                                ‫همت ‪. ۸‬‬   ‫ه‬                                ‫سرد ث کل مخروطی بسته مشود ‪.‬‬

   ‫‪3‬‬    ‫رك‪:‬دراہك‬     ‫‪۴‬‬         ‫مخفف «در و کر » = درو دگر‪.‬‬       ‫‪۴‬‬            ‫‪ ۱‬رك ‪ :‬در کلاله ‪.‬‬
              ‫در لك ‪۰‬‬    ‫رك‪:‬‬    ‫‪1‬‬          ‫‪.‬‬   ‫رل‪ :‬مادةٌ قل‬    ‫‪_ ۵‬‬           ‫‪.‬‬    ‫‪ - ۴‬رك‪ :‬هاده نمف‬
   ‫« بارتولمه ‪٩ ۴۹۹‬‏ ‪ ۰‬قس‬           ‫‪ - ۲‬بهلوی ‪ « 03۳۳۳1‬منای ‪۱۷۲٩‬‏ از ربت ‪۲2 -‬‬
       ‫‪ - ۸‬از درماندن؟‪.‬‬        ‫بر منیع ‪ 027۲721‬نیب ک‪ »:۹‬ورك‪ :‬اسثق مهوبشمان‪4۵‬ه ‪.‬‬                          ‫‪1‬‬
       ‫‪ #‬درگاه ‪ -‬بفتح اول » از ‪ :‬در ‪ -‬گاه (پوند مکان ) » پهلوی ‪( 8487310‬دائرة لمعارف‬
  ‫اسلام ‪ :‬در) ‪hãûgrid ۰‬‏ «تاواد‪:‬ا‪ » ۹۵۱‬معرب آن درقاعة « دزی ح‪۱‬صی ‪۵۳٤‬‏ » ودر گاه « ابا‬
  ‫ص ‪۲۹: ۷۳4‬؛ بار گاه ‪ .‬در‪,‬ار» سرای وادشاهی » دبوان ملطاتی ‪ « :‬یکی ازملوك عجم شنیدم که‬
   ‫مته‌لقان را همی کفت که مرسوم‌فلان راچندانکه هست مضاعف کد که ملازم دگراه است ومترصد‬
                             ‫د‪-‬ر » درواژه ‪-‬آستانهٌ در» حشرت ‪.‬‬
                                                            ‫*تان ‪* ۷4‬‬   ‫فرمان ‪.‬‏ گل‬
  ‫‪ #‬درم ‪ -‬بکراول وفتح دوم پهلوی ‪ « 772۳1‬منای ‪ ۱۷۲:۲۰‬و ‪ < 0۳5201‬تاوادیا‬
  ‫ازیونانی ‪« 8×۵۲‬نبرک ‪۸‬ه“ معرب آن درهم (بک راول وفتح سوم )؛‬       ‫‪ ۰۶‬و ‪.‬‬
   ‫واحد سک قره (وزن و ‪:‬بای آن درعصرهای مختلف» متفاوت بوده است) ‪ .‬رك ‪ :‬دار المعارف‬
  ‫اسلام ‪ :‬درهم ‪١‬‏ ورك‪ :‬دزیح اص ‪ ۸۳‬واحدوزن ‪ :‬معادل شش‌دانگه(هر دانگ معادل درفراط)‬
                                          ‫«ناطم الاطبا» ورك‪ :‬دائرة لمعارف اسللام‪ :‬درهم ‪. ۲‬‬
```


## [2026-09-05T20:10:28.530Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"######## v2 leaf 515 (≈printed 1055)\"; awk 'BEGIN{RS=\"\\f\"} NR==516' BQT_v2_pages.txt | grep -n \"زنهار\\|زینهار\\|زین\" | head -20",
 "description": "Read BQT page 1055 zenhar"
}
```


### [2026-09-05T20:10:30.511Z] TOOL RESULT

```
######## v2 leaf 515 (≈printed 1055)
17: ‫دوبال اوسرخ است وآواز او بفایت خوش‌وحزین‬                                          ‫عربی زر قلب نا سره باشد ©‬
```


## [2026-09-05T20:10:34.549Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'زنهار' in p or 'زینهار' in p:\n        print(\"leaf\",i,\"printed≈\",i+540, p.count('زنهار'), p.count('زینهار'))\nEOF",
 "description": "Find zenhar leaf in BQT v2"
}
```


### [2026-09-05T20:10:36.369Z] TOOL RESULT

```
leaf 135 printed≈ 675 0 1
leaf 503 printed≈ 1043 1 0
leaf 517 printed≈ 1057 1 0
```


## [2026-09-05T20:10:39.069Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==518' BQT_v2_pages.txt | grep -n -B3 -A12 \"زنهار\"",
 "description": "Read BQT leaf 517"
}
```


### [2026-09-05T20:10:40.943Z] TOOL RESULT

```
3-                                                                                                      ‫ا‬
4-
5-
6:                             ‫بر روی خمیر نان پاشند‪.‬‬      ‫زنهار ‪ ۴‬است که بناه‬         ‫ربنهار ‪۳‬‬
7-‫رلو ار » با نالی مجهولبروزن دیوار ‪.‬‬                         ‫ویمان‬
8-                                                                ‫جستن و امان خواستن باشد ‪ -‬و عهد پ‬
9-       ‫معنی سوبت وماوی بودن وبرابری باشد‪.‬‬                   ‫‪ -‬و تری‌وبيم ‪ -‬و شکایت را لکیوزیند ‪-‬وبمعنی‬
10- ‫هه‬              ‫بگر‬     ‫ی‬         ‫‪۷‬‬        ‫ی‬                 ‫هآی‬ ‫او‬‫گعجل‬
11-                                                                       ‫افوس و حسرت ‪ -‬وامات ‪ -‬وت‬
12-‫بمعنی(ژ شت‬            ‫' = بروزن ده‬     ‫لو‬
13-                                        ‫زر‬
14-                                                                                          ‫لیزآمده است ؟ ‪.‬‬
15-‫و آرایش باشد ‪ -‬و آنچه بدان زبنت و آرایش‬
16-                                                            ‫ر بنهاری = یناه آورنده ‪ -‬ویناه داده‬
17-
18-‫لرین = بفتح اول بورزن زمین ؛ بلغت‬                           ‫‪-‬در عوهادمان کی در‬
```


## [2026-09-05T20:10:45.787Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==518' BQT_v2_pages.txt | tail -25",
 "description": "Read BQT leaf 517 footnotes"
}
```


### [2026-09-05T20:10:47.390Z] TOOL RESULT

```
                                                                        ‫(‪ )۱‬چك ‪ :‬ژند وپاژند ‪.‬‬
 ‫‪۳1,‬‬       ‫‪ - ۱‬بهلوى ‪( 41112‬امن‪.‬امان)» ‪-‬قدی ‪( 11/2‬بناه‪.‬امان) رك‪ :‬مقالهةٌ ‪6/7۲۳‬‬
      ‫ص‪.۵ ۵۸‬‬     ‫‪ 2‬شمارء ‏‬       ‫چاپ ماساچوست‌ح ‪۷‬‬       ‫درمعر فی تارمخ عرب تالف هتی ‪»,mulucepS‬‏‬

      ‫‪ 590‬آرامر کب‌از‪0128 ۲201 :‬میداند‪ .‬بعنی‌ازین پر هرز ‪ ۲۳. ۲611(1)۷۱.‬آنراعاوستابی‬
      ‫(سلاح‌حامی )میداند هوبشمان گوی که وجه‌اخیر بنظرمن بهتراست «هویشمان‬                   ‫‪60622 .3‬‬
  ‫‪ - ۴‬در بت ذبل لختن بمعنی‬                        ‫‪.‬‬   ‫ار‬
                                                       ‫ه‪:‬‬‫زنرك‬
                                                            ‫‪۳‬‬                    ‫‪ :‬احق ‪. ۷۲۰‬‬       ‫‪ ۷‬ور‬
                                                ‫و دوم‌یمعنی ”یناه ‪ ۰‬حمایت؟ است ‪:‬‬      ‫‪ ۵‬بپرهیز ‪ ۰‬حذرکن؟‬

                ‫حان مرا «دین فلك ز هار خوار‪.‬‬                    ‫مگذار ز‪:.‬هار چو در زهار تت‬
  ‫‪.‬‬     ‫‪ °‬ھچ‬    ‫سعد‬   ‫معود‬   ‫‪۶‬‬

               ‫® _ از‪ :‬زبنهار‪-۳‬ی (حاصل مصدر) ‪.‬‬                 ‫نزه‪:‬ار(‪-‬ی ( ست ) ‪.‬‬
                                                                                ‫زی ا‬
                                                                                   ‫‪۴‬‬
                                   ‫_ سفدی ‪. ۲۷۷72‬‬       ‫‪۲‬‬           ‫‪.‬‬   ‫‪٠‬‏ زان‬    ‫رك ‪ :‬زان‬     ‫‪۹‬‬

             ‫‪Henning, Sogdian loan - words..., 505,2۰۰‬‬
           ‫زه ‪ , 22/8100 ۰ 2298280 ۰‬ىولېپ ‪ » 01200‬دنلپ ‪‎‬ركىوب« ‪. ۰ ۱۰۸‬‬                         ‫‪۸‬‬
```


## [2026-09-05T20:11:01.901Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==389' BQT_v1_pages.txt | grep -n -B2 -A8 \"اندرز\"; echo \"=== tail footnotes ===\"; awk 'BEGIN{RS=\"\\f\"} NR==389' BQT_v1_pages.txt | tail -18",
 "description": "Read BQT page 170 andarz"
}
```


### [2026-09-05T20:11:03.499Z] TOOL RESULT

```
19-با شیردان او متکون حبشود ۰ و آنرا عربی
20-حجرالبق رکویند . ۱
21:انفد وا با واه بروزن اندرزاابمعنی
22-سر گشته‌وحیران‌باشد - وبمعنیآرزوو حاجتمندی
23-هم هست - و سرنگون آریخته و واژ گونرا نیز
24-کوش .
25-3 شش :- واحتیاج ۰
26-و۷ -
27-| ندر و از - با زای فارسی بر وزن
28-چنبر باز , بمعنی آندرواست که سر کشته وحیران
29-و آرزو و حلجتمندی - و سرنگون آویشته
=== tail footnotes ===
وسرنگون آوبخته باشد . .
| ندد و ای" بروزن‌سندل‌سای,یمعنی
اندرواه است که صر گشته وحیران و احتیاج (۱)
وسرتگون آویخثه باشد .
| نددوالی " - بروزنک پروایی: بمحنی
ب کشتگی وحیرانی - و آرزو و حلجتمندی -
وسر‌دگونی باشف .
ندر وب س بفتح اول وضم ثالث‌پروزن
کند کرب . نام نوعی از جوشش باشد که پوست
بعربی قوبا کوبند .
اندروخون ه بن خای شله دار
رسممی سطیر ار تال باشد .
| ندروسص - بر وزن سندروی ؛ تلم
مردی بود واو مطلویی داشت «هارو»نلم وهارو در
نا اندروی فروغ آش نا کنان آمدی و پیش
7 یر که ۰۱۰۰ < منای ۲۷۹ ۲.
۳ ‌- ۴ 1 اندرو ای.
.ِ‌ ۲۶٩ :۱ فاب‎ ۰
```


## [2026-09-05T20:11:08.261Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'اندرز' in p:\n        print(\"leaf\",i,\"printed≈\",i-218, p.count('اندرز'))\nEOF",
 "description": "Find andarz leaf in BQT v1"
}
```


### [2026-09-05T20:11:10.333Z] TOOL RESULT

```
leaf 19 printed≈ -199 4
leaf 39 printed≈ -179 2
leaf 388 printed≈ 170 1
```


## [2026-09-05T20:11:20.824Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==388' BQT_v1_pages.txt | tail -22",
 "description": "Read BQT leaf 387 tail"
}
```


### [2026-09-05T20:11:22.460Z] TOOL RESULT

```
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
```


## [2026-09-05T20:11:39.012Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT dar- 'halten'\"; grep -n \"halten, festhalten\\|'halten'\\|dar-.*halten\" BRT.txt | head -10; echo; echo \"### BRT zaeno\"; grep -n -i \"zaeno\\|zaenO\\|zaena\" BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:11:39.069Z] TOOL RESULT

```
### BRT dar- 'halten'
12844:•  j,,  g,,  p.  3dar-  V.  'halten;  fassen'. Praes.  i  ä3n-,  dr-,  2  dam-  (?),  4  dara-, 5  däiär-'^,  16  (Des.)  dtdar^Ia-''^,  20  'dru-3\ 24  daraya-(?),  30  (Iter.)  däraya-,  30  +  27 (Pass.)  *'d3rya-''^;  PrP.  adariy;  Perf.  i da^är- :  dadr-,  dalr-,  1  dädr-\  J-Aor,  i dänr- :  dars:  ~  PPfP,  d^r^ta-;  Inf.  dar»- dyai,   dar?hräi,  därayS;  Absol.  dtnigm.
13478:Zum  V.  idar-,  —  ai.  dAära^a-  n.  'Halten ; Zurückhalten'.
29235:•  g.  hap-  V.  'halten',     Praes.  i  Aap: 'halten':  Ayai  ta  xastä  yä  ia  Aaßt (iS.)

### BRT zaeno
4338:•  j.  an-ava'Dhabdamna-  Adj.  'nicht  ein- schlafend': -d^mnS'  zaenauha  Y.57.16".
27470:zaenay-
27499:•  j.  zaena-  m.  'Waffe':  vasrfm  . .  ama- vastpmfm  -nam  (GP.)  Yt.  70.  96  ";  96;  — hqm  *'tta  (AP.)"  stmbayalwtm  (sd.)  Yt  i. 27;  —  *tta  (IS.)  haHtma  hutniia  Yt. 10. 141.
27501:•  j.  zaenaDh'an-  Adj,  'wachend,  wach- sam': sraes?m..yd  anavanhabdsmra  'aha (NS.)  nipaili  tnazää  däman  Y.57.  16;  16, F.  20;  —  'K>ha  (NS.)  niJspBj^aJna  (sd.) ya&a  västryS  fsuyqs  V.  13. 46.
27503:•  j.  zaenay-  Adj.  "reg,  eifrig':  yas^a  hi .  .  väam    paifi    'nil   anhat    (näroL  sp£)
27509:•  j.  zaenav-  f.  'Wehrgehänge'*':  yailqm zayanqm  raisWi  .  .  puxaa  'nätti  mat aiana  mat  "irisas  ayj.arfräil  ". .  das  Wehr- gehänge mit  dem  Köcher  sammt  30  eisen- spilzigen  Pfeilen"  V.  14. 9.
27513:•  j.  zaenah'vant- Adj.  'wachsam,  regsam': mCir?m  . .  •narthuntim  Yt  /o.  61 ;  — *'na>3uhant>m     . .    yaka     taxmS    urvpa
30515:•  j.  hu-zaena-  Adj,  'mit  schönen,  guten Waffen';  mihnm . .  'n^m  . .  vn-Hsravastittum
```


## [2026-09-05T20:11:40.545Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB dastan/handarz\"; grep -n \"handarz\\|dāštan\\|dastan\\|dārūk\\|darmān\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Nyberg"
}
```


### [2026-09-05T20:11:40.590Z] TOOL RESULT

```
### NYB dastan/handarz
407:ümurZitan [’mwleytn'] to forgive, to absolve, with be 3114. 35%. 67°; to pity 76°; Gi hac 61... bē āmuržīt this (bull) shielded him 49°, with the gl. kū-š gāvān haciš apāc dašt. — Ps. pt. ’mwicyt; Paz. dmuržidan, NP ämurzidan; MPrth subst. ’mwjd ‘compassion’ (A-H III), "mwždyft ‘mercy’ (S); MPrs ’mwrzydn (S), pres. >muw(r)[2- (Sogd. 45); Verbum 168 sq. Av. (1175) moroždā- pres. ‘to forgive’, marazdika- "mercy'.— V. also an-āmuržišn. āmušt [Pmwšt'] crushed 2622-24, — < *a-murst < *d-mrsta- < à + Av. (1150) marod- ‘to destroy’, cf MPrth >mStn, pt. ’mst ‘to crush, to destroy’ (A-H III), which seem to go back, quite irregularly, to *āmdrsta-; as to -rst > -št cf dāštan, vaštan, vitaštan; the explanation given in Verbum 218 is not satisfactory. Ghi- lain 99.
1191:dar [BB”] door 75"; gate, pl. ~ -ihā 8713.18, 11472; hac an ~ in another way 813; har ~ every category 111”; — a royal person's court P1:4. P2:9. 39. 55, 131, 1710, 208-9. 617. 705. 1077. 1097. 1123. — SW form of Av. (766) dvar-, OP duvara-: MPrs dr, Paz. NP dar- as against NW: MPrth br, NP bar. — V. darak, dar-band and dar-handarz-pat.
1196:dar-handarz-pat v. handarz-pat. *darik [*dlyk] courtier, court dignitary
1198:dārišn [YHSNN-šn'] v.n. of dāštan: 1. used as pred. (is) to be held 907°. 12118. — 2. [d'lšn'] maintenance (of the body) 682, 7615-17, [YHSNN-Sn] 117%; x%arišn u ~ 2204
1199:dārišnēh [d?linyh] det. v.n. of dāštan: (pus) pat tušn ~ in order to keep (his son) quiet 41°.
1220:dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
1222:' dāštan
1424:who is the messenger from this being [the Creator just mentioned] is good 5711; etc. passim; — anticipates a clause with kū ‘that’ 521.7132, 5320; ~ ku the fact is that 52"; a rel. clause: ~ +-t... pursit 7614; ~ ce that which 11214; — forms a rel. attribute: ~ i vas kayak u karap 5525; — forms possessives of the pers. pronouns: ~ % man zan my wife 3215; ~ i tō pus thy son 5213-15; ~ 4 tē separated by other parts of the sentence from its headw. 60°; — pat ~ dāštan 5012, v. dāštan; pat ~ šātēhē for joy over this 412°; pat ~ ku... adak-ic although ... yet 5525-26; ~~ rād for that reason 795 ete.; — cigon ~ i den göbet as the pertinent passage of the Scripture says 5323 etc.; čvak — i paitäk ku one (event) is that which is revealed, namely that 385-17, — 2 HWHw-yt! (ideogr. for the 2nd p. pl. of h- ‘to be’) wrongly for ēt: pat ~ dästan 25°. — 3. ē: ēvak ~ (i) paitäk 36% and passim 41-54; ~ rād ce because 9422. — Av. (12 sqq.) aéta-, OP aita-; MPrth ‘yd; MPrs ?yd. The form é in BP is confirmed by the wrong ideogr. HWHw-yt', but it is note- worthy that this pron., wherever it is phonetically written in BP, has the form é (also in FrP 25). In Paz. there is no trace of & (ed), since the only form occurring there is ē with the pl. ēšgn, which is also used as the pl. of õi, ētšān having totally disappeared; NP has only 6, pl. ēšān. This esqn can neither be derived from ët nor from öisän; it must reflect the Olr. gen. pl. *atšām (Av. aēšam) of *ayam (Av. ayem, aēm) whence in Milr "aš enlarged with the Milr pl. ending -än. The most probable expla- nation of BP ē is, therefore, that it is not a mutilation of é& but the gen. sg. of *ayam: ahya. This being so, it would seem to be most advisable simply to give č as the normal equivalent of HN’, which would best explain the widely spread use of HN’ as the ideogr. for homonyms, v. below.
1701:g08 [gwš] ear, with the indef. art. ~-é [gwš +1], 24". 301. 31". 671. 9525; ~ dastan hac to take care of 148; ~ apar dästan to care about 463-4, — = Paz. NP; Av. (486) gaoša-, OP gauša-.
1872:adverbs and conjunctions: hac hàm | handarzčnitan [—-ynytn'] to give direc-
1880:handarz [hndlc'] counsel, advice 41%. 62 (heading). — Ps. hndley ‘command, law’; MPrs ?ndrz (S); NP andarz.
1881:tions, warnings, to instruct: apt-m züpihä „.. handarzenit he 7615-16,
1882:handarz-pat [hndlept'] chancellor, chief judge, head of the treasury of a province or a corporation, administrator of pro- perty: Sakistin ~ P 1:6; dar-~ 7 vàs- puhrakän the court administrator of the (royal) properties 1118-19, v. 2vdspuhrakdan and Périkhanian, REA V, 1968, 20-21 (cf s.v. väspuhr); [yztpt MLKTH-n hndrzpty KZSPrth 1. 27 = yztpt ZY b’ny(!)kn hndicpt Prs 1. 33 = Gr. v. InodtBad Bactrrcodyv avčapčaBIŠ (enumer- ated among the lower ranks of court officials). — Arm lw. handerjapet ‘the Master of the Royal household’, already in the Bible (e.g. 1 Kings 16:9 = Gr oixovéuoc), then often ‘director, manager” in different functions; when speaking of Persian officials the authors use the form anderjapet: Sakstan a. P‘aust. Buz. 4,45, mogac a. ‘the chancellor of the Magi? ibd. 4,47, or in the idiomatic Persian form Movan a. EliSe (5th c.), Hist. of the Vardans (Venedig 1838), 138. 142 (thus the MSS; the ed. han-).
2705:nihan [nyh’n'] secrecy; a secret place, a hiding-place: pat ~ secretly 5? etc.; hac ~ from an ambush 259; ~ kartan to hide 10?3; õi ~ be dätan to put aside in safe custody 4219; pat ~ dāštan to con- ceal 165-24-25 (hac from); ~ ravisn, -nēh v. these ws. — Cf Av. (1082) ničate-. Paz. niha, NP nihan.
2719:nikah [nk’s] look, glance, observation; custody, care: ~ kartan to look on, to watch 152. 259.24, 2726. 2817; ~~ daštan to notice, to observe, to pay attention to 108%. 12114; apar ~ dāštan to keep in safe custody 4112. — MPrth ng’h ‘look, attention’, n. kyrdn ‘to notice’ (A-H ITT); Paz. nagäh, NP nigäh; < Olr "ni-kada- from kà-, v. ākāh. Another derivative was "niš-ka0a- > Milr *niškāh ‘contempt’, preserved in Arm nškah-em ‘to reject, to condemn’. Cf also Arm nkat linel or nkat-em ‘to see, to consider, to contem- plate’ from MIr *nikät < Olr *nikātā, nom. sg. of the nomen actoris *nikätar- ‘contemplator’. The pt. pass. *nekāta- is found in the name of the 15th nask (q. v.) of the Sas. Avesta: N?kütom [nyk”- twm] = Av. *nikätem ‘that which is observed (in medical matters)’.
3007:doubt and its antonyms (gumdn, apé- gumän, apēgumānēh pat), reliance (upon); — to look on, at (nikéritan); to consider, regard as (dāštan pat); to make a p. such and such (kas kartan pat + subst., often in the cas. obl. sg. ending in -čh); to entrust (gumürtan pat kas); to get married (v. zančh) ; etc. ete., v. the individual ws. — 9. forming adverbial expressions: from adjectives, with or without the ending -éh: pat buland aloud, pat sihsčilak, pat näm- cist; pat bavandakeh, pat perözeh, pat sagréh, pat tuxsakéh; from a subst.: pat frazam, pat dēkān; pat hamäzakeh, pat sihsaleh, pat bundahisnéh, pat paitiyära- kēh; pat ax"arišneh without food; from adverbs: pat uléh, pat niküneh, pat apākēh. — 10. compound expressions: pat
4017:2vaspuhrakan adj. of väspuhr: belonging to, or characteristic of, a member of the elan or family entitled to share the patrimony (chiefly people of the upper or highest classes of the society): 1. subst. the patrimony itself: dar-handarzpat + ~ 11, v. handarzpat. [- 2. distinguished, prominent, comp. ~-tar, sup. ~-tom DkM 2921-17; adv. ~-tha especially, par- ticularly, e. g. DkM 413?!.] — Correspond- ing to Arm sephakan, v.s. v. vispuhr. vāspuhrakānīk adj. = ®väspuhrakän 2, comp. ~-tar 1068.
5778:’ndrz: handarz
5907:d’n’g: dänäk d’nystn, d’n-: dänistan @nysn: dānišn @r-gyrdyyh: dar d’rwg: därök d’Stn, d’r-: dastan
6990:andarz: handarz
```


## [2026-09-05T20:11:53.120Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT darza\"; grep -n \"d3r3za\\|dsrsza\\|dar\\?za-\\|'Fessel'\\|Naht\" BRT.txt | head -15; echo; echo \"### BRT han-darez\"; grep -n \"hqm-d\\|ham-d3r\\|handar\\|hqmdar\" BRT.txt | head -15",
 "description": "Grep Bartholomae for darza and handarza"
}
```


### [2026-09-05T20:11:53.201Z] TOOL RESULT

```
### BRT darza
12956:mit  3  'fesseln':  HltryB  .  .  avqm  pairi- kam  adafTtayäti  bibdailla  . .  vUpabäailla .  .  ya^a  hataanm  narqm  Bim  narvm adarstaySit  Yt.  Ä  55.  Undeutlich  ;/ii«r- yqm  htm  vanm  *ad3r3zaySii  hg .  .  N.j". joit/ra  und  nT  'festmachen  sva.  unschäd- lich machen' :  aitahmaiat  nidanzaym  (sd.) fra  kimcil  nidamaym  ".  .  (so)  sollen  sie ihn  (den  Hund)  unschä<9ich  machen"  V. 13'  31-
17399:•  j,  bdti'  m.  'Fessel'.

### BRT han-darez
8647:Pü.:    hanibasf->.     —    J>  Zu  streichen;    s.  die Var.  —  ')  Wie  für  das  folgende  handar/iia.
12959:mit  Äqm  i)  'aneinander  befestigen, zusammenbindend  vereinigen':  yS  barisma .  .  hqm^risaiti  kam  va  damayäti (Konj.)  N.  <)9;  —  yezi  aat  nöit  HirB larÖMmand  handar^zanti  (Konj.)^^  aratu- /risH.  101.  a)  'fesseln':  zasta  hepaoinm kandarnayanta  V.  g.  49.  a)  mit  hatt-
29362:j.  handaramana  N.  Jji  lie*  ktmdram'.
29365:•  j.  handarszan-  Adj.  'zusammenfassend, fassend,  greifend':  yd%a  (Sp,  1 248  m.)  lata paoirjm  'ta  (NS.)  z>ml  aSaipaiti  nidaC^ita avavat  haÜa  shrat  nasvpakä^  . .  "soviel er  dabei  beim  ersten  Mal  fassen  kann,  das soll  er  auf  dem  Erdboden  ntederiegen, so  weit  von  . ."  V.  8.  76.
```


## [2026-09-05T20:11:59.767Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12950,12960p' BRT.txt; echo \"=== zaeno compounds ===\"; sed -n '27495,27520p' BRT.txt",
 "description": "Read Bartholomae darez root and zaena entries"
}
```


### [2026-09-05T20:11:59.844Z] TOOL RESULT

```
•  g.  darasät  Inf.  'zu  erblicken,  zu  er- schauen': mq^mtiB  ..  yS  is  pai  d'  alahyä ". .  des  Propheten,  der  es  ihnen  wehren  wird das  A.  zu  erschauen"  y.j2, 13''.
Zum  V.  dani:  —  VgL  Jar^ia-.  ~-  PÜ. :  Aa! mirüht,  Npü.-.  dl  diäatt.  —  ')  Vgl.  iSt.  Bthl. KZ.  38.  33  und  V.  28.  5.
•  j,,  g.dflr3z-V.'stabilire;vincire'.  Praes. 1  ^r?«-'*,  i6(Des.)tfWwvi3-'>,  z^dtrnaya-, 30  (Iter.)  damaya—,  J-Aor.  1  dar»z-*^.
1)  'festbinden,  fesseln':  apq^  (sd.)  gavs dam^äti  Ytro.48.  a)  Des.  '(Satzungen) aofirecht  erhalten,  (daran)  festhalten  wollen' ; aväU  urvamis  (sd.)  ya  tu  dldsrdö  (aS.)'' maa£i  Y- 4^.15,         S.  noch  dimanB.'.
mit  aipi  fesseln'  (?) :  aipi  dtrfzvamm d^ratayahi'ftH  "in  Fesseln  legt  (ihn)  den Fesseln  tragenden"  Yt/.  a;  (?)♦'.
mit  autark  —  ?  — :  yesi  *tmtar».dfr)za- yaiti^''  .  .  yezi  *'ilai  itBif  atiianJ?nzayaiti ti.94.
mit  3  'fesseln':  HltryB  .  .  avqm  pairi- kam  adafTtayäti  bibdailla  . .  vUpabäailla .  .  ya^a  hataanm  narqm  Bim  narvm adarstaySit  Yt.  Ä  55.  Undeutlich  ;/ii«r- yqm  htm  vanm  *ad3r3zaySii  hg .  .  N.j". joit/ra  und  nT  'festmachen  sva.  unschäd- lich machen' :  aitahmaiat  nidanzaym  (sd.) fra  kimcil  nidamaym  ".  .  (so)  sollen  sie ihn  (den  Hund)  unschä<9ich  machen"  V. 13'  31-
mit  nl  'festmachen,  befestigen':  altala .  .  mazdayasna  altern  irist>m  nidarjsaytn Aavtttibya  pataäbya  *x°a^ai^ytua  (sd.) varsa  .  .  yai  nöit .  .  astam  avi  apqmla  . . barmtsm  (sd.)  frajasqn  ".  .  sollen  den Toten  festmachen  mittelst . ."  V.  6.46;  — yezi  nsit  *nidarvzayäitW>  (nämL  iristfm) V.6'.47.  a)  'an-'  (Abi.):  aaahmätat
nidanzayen  "an  ihm  (dem  Maul)  sollen sie  es  (das  Stück  Holz,  Sp.  367  o.)  fest- machen" V.  y.  31.  b)  mit  Dat  'fest- machen gegen  —  hin  sva.  davon  ab- sperren'; paoiryäi  (näml.  sBni)  nidan- taysn  apirmayükim  ava%a  atrftn  "von dem  ersten  (Hund)  soll  man  die  Kinder absperren,  de^Ieichen  das  Feuer"  V. 0--48'".
mit  Äqm  i)  'aneinander  befestigen, zusammenbindend  vereinigen':  yS  barisma .  .  hqm^risaiti  kam  va  damayäti (Konj.)  N.  <)9;  —  yezi  aat  nöit  HirB larÖMmand  handar^zanti  (Konj.)^^  aratu- /risH.  101.  a)  'fesseln':  zasta  hepaoinm kandarnayanta  V.  g.  49.  a)  mit  hatt-
danza  "Fesseln  anlegen':  fiandar3zaal{sA.) Aandar^zaym  V.5.  49.
=== zaeno compounds ===
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
```


## [2026-09-05T20:12:28.802Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### TTS bagatur\"; grep -n -i \"bagatur\\|baghatur\\|batur\\|bahadir\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10; echo; echo \"### LKT bagatur\"; grep -n -i \"bahadur\\|bagatur\\|bogatyr\" LKT.txt | head -10; echo; echo \"### AID bahadur\"; grep -n -i \"bahadur\" AID.txt | head -5",
 "description": "Grep Turkic sources for bahadur"
}
```


### [2026-09-05T20:12:28.909Z] TOOL RESULT

```
### TTS bagatur

### LKT bagatur
615:'Held'  [nach  Schiefner  durch  Dissimi- lation der  Konsonanten  aus  fagfür  hier Nr.  569  oder  aus  dessen  Grundwort bagha-piithfa  entstanden;  vgl.  mongol. bagatur,  batur,  woraus  ung.  bdtor  'kühn' wurde];  ebenso  tk.  bahadyr  'Held';  hier- aus russ.  bogatyr'  'Held,  Riese,  Vor- kämpfer' z.  B.  im  AT  in  Bezug  auf Simson  gebraucht;  klruss.  bohaiyr  'Held', bahatyr  'reicher  Mann';  poln.  bohatyr 'Held'.  Über  bind,  bahädur  'Held,  Vor- kämpfer' entstand  angloind.  bahaudur, bahawder,  behadoor,  frz.  bihadour:  ein Titel,  der  gewöhnlich  dem  Namen  euro- päischer Offiziere  in  indischen  Schrift- stücken angefügt  wird,  z.  B.  Jones  ^dhih Bahädur.  Auch  sind  Bahaivdur  und Sirdar  Bahaivdur  die  offiziellen  Titel der  Inhaber  der  2.  und  1.  Klasse  des Order  of  British  India,  der  1837  für eingeborene  Offiziere  der  Armee  gestif- tet wurde.  Im  gewöhnlichen  Leben  be- zeichnet angloind.  behawdur  'eine  hoch- mütige, wichtigtuende  Persönlichkeit'.  — [Benfey,  Orient  und  Occident  I,  1H7

### AID bahadur
5758:RAm  RAA.  The  denomination  of  Sikhs who  adhered  to  RAm  RAi,  the  son  of Har  RAi  the  seventh  guru,  when  the succession  passed,  not  to  him,  but  to his  great-uncle  Tegh  BahAdur.
```


## [2026-09-05T20:12:30.121Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB daru p325\"; grep -n \"dārū\\|daru\\b\\|därü\" HUB.txt | head -15",
 "description": "Grep Hübschmann"
}
```


### [2026-09-05T20:12:30.173Z] TOOL RESULT

```
### HUB daru p325
```


## [2026-09-05T20:12:41.235Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '610,620p' LKT.txt; echo \"=== HUB format ===\"; head -c 400 HUB.txt; echo; grep -n -i \"arznei\\|dāru\\|därü\\|dárü\" HUB.txt | head -10",
 "description": "Read Lokotsch entry and check HUB"
}
```


### [2026-09-05T20:12:41.299Z] TOOL RESULT

```
173.  Tk.  baglania:
'Das  Binden'  Inf.  des  Vbs.  baglamak 'binden';  hieraus  rum.  balaiiia,  balamale 'Türangel,  Scharnier'.
174.  Tk.  ba^yr:
'Eingeweide';  hieraus  runi.  hairi,  baere 'dass.'.
175.  Pers.  bähädur:
'Held'  [nach  Schiefner  durch  Dissimi- lation der  Konsonanten  aus  fagfür  hier Nr.  569  oder  aus  dessen  Grundwort bagha-piithfa  entstanden;  vgl.  mongol. bagatur,  batur,  woraus  ung.  bdtor  'kühn' wurde];  ebenso  tk.  bahadyr  'Held';  hier- aus russ.  bogatyr'  'Held,  Riese,  Vor- kämpfer' z.  B.  im  AT  in  Bezug  auf Simson  gebraucht;  klruss.  bohaiyr  'Held', bahatyr  'reicher  Mann';  poln.  bohatyr 'Held'.  Über  bind,  bahädur  'Held,  Vor- kämpfer' entstand  angloind.  bahaudur, bahawder,  behadoor,  frz.  bihadour:  ein Titel,  der  gewöhnlich  dem  Namen  euro- päischer Offiziere  in  indischen  Schrift- stücken angefügt  wird,  z.  B.  Jones  ^dhih Bahädur.  Auch  sind  Bahaivdur  und Sirdar  Bahaivdur  die  offiziellen  Titel der  Inhaber  der  2.  und  1.  Klasse  des Order  of  British  India,  der  1837  für eingeborene  Offiziere  der  Armee  gestif- tet wurde.  Im  gewöhnlichen  Leben  be- zeichnet angloind.  behawdur  'eine  hoch- mütige, wichtigtuende  Persönlichkeit'.  — [Benfey,  Orient  und  Occident  I,  1H7
Pers.  bähmän.]
16
führt  das  Wort  auf  sskr.  bhagordhara "glückbringend'  zurück.]  —  Über  tk. hahadyr  wurde  rum.  hahardlrcä  'alte Kokelte,  ydieinspröde'.  [Hobson-Jobson 48/Ö0.    Gorjajew  !2-2.   Bern  SlEtWb  Ü6.
176.  Pers.  bähuiäu:
Eine  Pflanze,  die  verschieden  bestimmt wird,  wahrscheinlich  Centaurea  beben, aber  ar.  bahman  'eine  Art  Rettich". Hieraus  frz.  hiJien,  sp.  behen,  dtsch. Behenuurzel;  die  Wurzel  wird  in  der Arzneikunde  benutzt.  —  Das  sog.  Behen- öl  wird  dagegen  durch  Pressen  der  Be- hennüsse  gewonnen,  d.  h.  aus  den  Sa- men der  Pflanzen  Moringa  oleifera  Lani. und  M.  aptera  Gaertn.,  die  wie  die  be- kanntere unsere  Kapern  [s.  hier  Nr.  978] liefernde  Capparis  der  Familie  der  Cap- paridaceen  (unseren  Cruciferen  verwandt) angehören.    [Devic  DEt  63/C4.
=== HUB format ===
Google
This is a digital copy of a book that was preserved for generations on Hbrary shelves before it was carefully scanned by Google as part of a project
to make the world's books discoverable online.
It has survived long enough for the copyright to expire and the book to enter the public domain. A public domain book is one that was never subject
to copyright or whose legal copyright term has ex
```


## [2026-09-05T20:12:50.371Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB darz\"; grep -n \"darz\\|derz\" HUB.txt | head -10; echo \"### HUB dar hold\"; grep -n \"dāštan\\|dastan\\|halten\" HUB.txt | head -10; echo \"### HUB zinhar\"; grep -n -i \"zinhar\\|zīnhār\\|zenhar\" HUB.txt | head",
 "description": "Grep Hübschmann more"
}
```


### [2026-09-05T20:12:50.450Z] TOOL RESULT

```
### HUB darz
4407:muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
4550:havar *Glaube ; derjak 'Schneider, np. darzT ; kerp 'Form' =
7714:'Testament' — np. andarz *Rath, Testament', dazu wohl
7908:zd. vareza- *Thun', verezyeiti *thut', darz *Naht' {g^h), zd.
7923:sisch); andarj Testament' = np. andarz 'Rath, Testament',
7924:anderjapet oder handerjapet = phi. andarzpat BB. 4, 62;
7934:vgl. np. dars^T 'Schneider, darzan *Nader, darz *Naht*, darz-
9128:*Glied* = np. andam; andarj 'Testament* = np. andarz
### HUB dar hold
86:Das Wort wird das Thema dpi- ^Wasser enthalten 2),
114:aus avarad *bringt* halten), wenn das Wort nicht are
529:zu skr. bhaj *Antheil geben, Antheil erhalten' (vgl.
553:= ap. *ha(n)basta' kann auch ich nicht fiir richtig halten.
615:lieferten Lesart festzuhalten, das Wort durch *Stand-
622:'Standhalten' (skr. avasihd- *Bestand') ableitet.
643:paJ- und pa-y vgl. Nr. 345), das im Neup. erhalten
647:p = np. p) im Neup. in bad^ ba uberzugehen. Erhalten
961:217. Np. bisydr Viel' -= ap. ^vasi-dara- Viel haltend'
1264:und machte apuxt, ihn fiir einen Fisch haltend.
### HUB zinhar
4960:zinhdr *Schutz, Sicherheit, gieb Acht! hiite dichf = zinhar
```


## [2026-09-05T20:12:51.898Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY latin index dar\"; grep -n -i \"^DHER\\|DHER\\b\\|DAR-\\|DARZ\" incoming/ARY/ARY_latin_index_pages.txt | head -15",
 "description": "Grep Aryanpur index"
}
```


### [2026-09-05T20:12:51.967Z] TOOL RESULT

```
### ARY latin index dar
7813:DARH- SANSKRIT) Gy Sikes DARZ PAHLAVD 65 hy,
7828:seal gt IG chlo 9% 4 DARZIG Gsr5ly hy Obj 22-1
```


## [2026-09-05T20:12:57.298Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4955,4975p' HUB.txt; echo \"=== 7930-7940 ===\"; sed -n '7930,7940p' HUB.txt",
 "description": "Read Hübschmann zinhar and darz"
}
```


### [2026-09-05T20:12:57.349Z] TOOL RESULT

```
>) Aber Sirln Frao Choaru's II (Tab. 283) - arm. Sirin
(Sebeos p. 45), np. Sirln 'siiiis' (auB *Sfrin)? Suffix -fi/ = zd. a^na-
(np. zarrtn *golden', zd. zaranafna-) b. bei Yullers, Gram. p. 255,
Der Name wird erst im 7. Jhd. den Armeniern bekannt geworden sein.— 142 -
= firSsta, arm. hrestaJc; xism (xasm^) Zorn' = zd. aesma-;
zinhdr *Schutz, Sicherheit, gieb Acht! hiite dichf = zinhar
[ztnehar); istadan stehn' ^= np. paz. estddan. Vgl. § 12 und
27 und Sal. Shuk. Gram. p. 15, Dazu hirun = herUn
aussen, heraus* (s. oben p. 33), pindastan 'dafiir halten' ^^
mp. pa in daStan; si *diei' = paz. se (s^) = zd. d^rayqm;
ki Ver, alter k\ paz. he = ap. *kai/a?
Dagegen wird ap. ai im Anlaut zu paz. np. ya- in:
yax *Eis, osset. yex, ix^ zd. a^a;a-; yoA: 'ein*, paz. yak, phi.
evai aus aiva -\~ ka (neben -e ein* = paz. ew-, ev- in Zu-
sammensetzungen Shk. 243 = ap. aiva-).
Kapitel 6: ap. au.
§ 31. Ap. au {^' idg. aw, ew, ou) wird im Mp. und
Np. zu 0: roz Tag = ap. raudah- u. s. w.
§ 32. Ap. au = phi. 6 wird vor w, m im Paz. und
Np. zu U: gun^) *Farbe, Art und Weise' — p^z. jrim, gUna^
arm. goin^ zd. gaona- ; paz. driew 'a consecrated cake' Min.
=== 7930-7940 ===
auch aspal (in Klammern) an, das = ap. ^sparda-lw&TQ, Aber in echt
kad. WSrtern ist z nicht in rf, also auch rz nioht in rd = I iiber-
gegangen. Woher aber stammt espul oder^wie^^erklftrt es sich?
') Vgl. np. histan : hilam 'lasse' zu^zd. harez.— 228 --
vgl. np. dars^T 'Schneider, darzan *Nader, darz *Naht*, darz-
man *Faden ; varj Xohn, Sold' (entlehnt?), np. varza *Gewinn\
Also liegt iran. z \m Persischen als z und d im An-
laut, sowie inlautend nach Vokalen und r vor und zwar
stimmt, soweit sich urtheilen lasst, das Mp. und Np. in der
Scheidung von z und d mit dem Ap. ganz iiberein. In
denselben oder von gleicher Wurzei stammenden WOrtem
```


## [2026-09-05T20:13:19.849Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### LEW firmus\"; grep -n \"firmus\" LEW_1910.txt | head -5; echo \"### LAT firmus\"; grep -n \"firmus\" LAT.txt | head -5; echo \"### SKT throne\"; grep -n \"^throne\\|throne,\" SKT.txt | head -5; echo \"### SKT farm/firm\"; grep -n \"farm (1)\\|firm (1)\\|^firm\" SKT.txt | head -5; echo \"### KLN thronos\"; grep -n \"thronos\\|θρόνος\\|Opovo\" KLN_1966.txt | head -5",
 "description": "Grep Latin/English sources"
}
```


### [2026-09-05T20:13:19.954Z] TOOL RESULT

```
### LEW firmus
### LAT firmus
21573:prochenent avec firmus, fretus n'est pas inpossible, nais il est
21945:fretus, firmus (et /ere?). Chacun des representants lartins suppos 4 s
22638:firmusV -a, -um (firmis Ital. d'aprfes fortis, ou d'aprbs infir¬
22642:et 5330 eat contredit par lea 1. romanea qui attestent firmus (it.
22669:infirmus: faible (sens physique et moral) et, tardif, infirmis, cf.
### SKT throne
3121:choir.  (F.  -  L.  -  Gk.)  M.  E.  ckaitt, chsure.^O.  F.  chaiere,  cluiett.  —  Low  L. cathedra^  a  throne,  raised  seat*  chair ;  see al.ove.
### SKT farm/firm
### KLN thronos
39149:throne,  n.  —  ME.,  fr.  earlier  trone,  fr.  OF.  trone (F.  trone),  fr.  L.  thronus,  fr.  Gk.  Opovoc,  ’seat, chair,  throne’,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold, support’,  whence  also  Gk.  Dpavo?,  ‘bench’, ftpijvup,  ‘footstool’,  Ol.  dhdrdyati,  ‘he  holds, supports’,  dhdrmah,  ‘custom,  law’,  L.  firmus.
```


## [2026-09-05T20:13:22.175Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC dher\"; grep -n \"dher-\\|dherō\\|dhereghō\" IEC.txt | head -10; echo \"### SYN hold\"; grep -n \"dhar-\\|dhṛ\\|dhr-\" SYN.txt | head -8; echo \"### WLD dher halten\"; grep -n \"halten, festhalten\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5",
 "description": "Grep Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-05T20:13:22.261Z] TOOL RESULT

```
### IEC dher
285:aidher-, aidhros, à “burning, bright; bright- ness’. WP I, 5. Cf. aidho Gk. aithér; aithros; aithra; cf. aithérios, adj.; Sequanian aidrini, adj. ‘bright: Gk. aithrinós “of early morning’; Alem. eter, adj. ‘clever, bright; Li. jedrà ‘measles’. Cf. aidhlos
2701:nature’; Finn. LW tapa, id.; Li. cf. dabnùs, dabinti “elegant; to adorn’ dhābh- ‘limp, flaccid’. Cf. dhabros D Skt. (ambig.) -dābhyah (‘frivolous’, in a- ° *serious); Alb. i dobë, í dobët ‘weak’; Sw. dof (‘sultry, blunt, stupid". Infl. of LG? & NG döf ‘stupid’. See dhoubh-); Go. cf. af- dobnan ‘grow dumb’ dhabhló, dhabhró, ið (?) ‘surge’. Cf. dabh- Skt. dabhráh (ocean; EMDu. daveren ‘tremble’; ON dafla ‘dabble, splash? dhadhló, dhadhró, ið (?) ‘waver, tremble’. Cf. dhedher- MHG tatern ‘chatter’; G tattern ‘shake, dod- der, twaddle’; Icel. daðra ‘flirt; Sw. darra ‘tremble’; cf. E dial. daddle ‘stagger, dawdle’. (A form *dhadh- seems to be present in EME to dade ‘to toddle’ and Li. dadu, eti “cackle') dhagh- ‘beautiful, fine, abundant, good, harmonious’ Gaul. dago-; OBr. da; W da ‘good’; MHG tagen, tegen ‘confer, arbitrate’; Du. dagen ‘summon’; G cf. Reichs-tag; Du. Rijks-dag; EME days-man ‘arbitrator’; EMDu. cf. dege- lijk ‘honest’; LG cf. d&g, m & f ‘good man- ners’; Li. dažyti ‘to eeh daZalas “orna- ei: ; dažnas ‘many 3... * Latv daZs, id. dhaloros, is ‘verdant, lush". WP I, 825. Cf. dhalió Arm. dalar (i-st. *green"); Gk. thalerós, id. dhalgho “hold, squeeze'
2725:dhåros, à “firm: firmness'. Cf. dher-, dherm-, dhor- Skt. (ambig.) dharab (adj. holding"); Li. dóras ‘honest’; dorà, f. ‘virtue’; Per. där 'posses- sing’, in cpds.
2791:dheémn- — dher-
2807:dher- (dhor-) (1) ‘strike’. Cf. WP I, 858 & 867 Li. deru, eti (1) “bump, hit; (o-gde in) OE derian, MHG teren, Du. deren “harm. Cf. perhaps Skt. dhàrà (2) “edge, blade’; Av. dara ‘cutting-edge’ and (?) ON där ‘mockery’, dára ‘scoff, fr. *dher-. Cf. WP I, 643
2808:dher- (2) “hard, fast, firm'. Cf. dhermos, dhern-, dhor- & dháros Skt. cf. dharayami “hold, bear, wear, prevail, agree’; Hind. dharna ‘grasp; pledge’; Av. dar- ‘hold, get’; Ober dar-, id.; Per. (ambig.) dā- ram ‘have’; Arm. (o- or zero-gde) darem ‘stay’; Gk. cf. thérsos, Aeolic: ‘courage’; Lat. cf. fer-tim ‘thickly, closely’; W der ‘stubborn’; deru, derio ‘jib, be stubborn’; Li. derüs ‘thriving’; deriù, éti ‘bargain’; derù, éti ‘serve; suit’; Latv. depu, et ‘befit; pledge; suffice’.
2812:dher-dhlom, -dhrom, -trom ‘holder’. Cf. dher- (2), etc. Skt. dhartrám ‘stay, prop’; Gk. térthron “sail- yard?
2816:dheri (dheri-met) (dhor-) ‘up to, near; nearly’. Cf. WP I, 858 Arm. der “still, yet’; OAlb. dere, cj. ‘while’; — për 'until'; Alb. deri, djer&, cj. ‘until’, adv. ‘nearly’; Lat. fere, ferme; Blg. (o-gde) dori do ‘up to; Li. dar ‘still, yet’. (A relation- ship w. root dher- “firm”, etc. is possible on the analogy of G fast “almost? and E fast: Du. vast “firm? beside Du. al-vast ‘already’)
2817:dhermos, à, io (dhermn-, dherom-) “firm, fixed; fixture, pact, order'. See dher- (2) and cf. WP I, 856 Skt. dhármah, dhárman; Tokh. (?) sarm ‘reason’; Arm. cf. darum (fend, term’, fr. *dherom-); Lat. firmus; LLat. firma “fixed payment; farm’; Umb. cf. ferime ‘firmly’; Ir. darmna (‘price-fixing or sim.); MHG térme,
2823:5 dhern- “holding, firm; hold, hardwood'. Cf. dher- (2), dhor-, dhermos Cz. dřeň ‘pith, core; dřín *'cornel-cherry'": OHG tirn-paum, -pauma (“cornel', cognate accdg. to J. Schmidt, LW accdg. to O. Schade);
### SYN hold
6040:Skt. girodhara-, lit. ‘head-supporter’, epd. of giras- ‘head’ and dhr- ‘hold’.
6434:4.42 UDDER (Of Animals) ee otap Goth. Lith. te3muo a Haarépt, Buel ON jugr Lett. tesminis ae uber Dan. yver ChSlteer Ir mammella, poppa Sw. juver SCr. wvime Sp. ee OE tider Boh.  vujmé Rum, siger ME udere Pol. wymie in i ne udder Russ. vymja Nive u. uier Skt.  udhar- WV. Be OHG  atar(o) Av. it ran (cader) MHG iter (inter) Words NHG  euter Ords for i
7447:Skt. vadh- ‘smite, kill’ (mostly in tenses supplementing jhan-), beside vadha- ‘killing, murder’, vadhar- ‘Indra’s weapon’, Av. vadar- ‘weapon, club’ (20.22) : Grk. §é ‘thrust, push’. Walde-P. 1.254 f.
7598:Lat. fortis (more commonly of mental strength, ‘brave’, but also and orig. used of physical strength and in this sense > It. forte, Fr. fort, Sp. fuerte), fr. forctis (Festus), prob.: Av. dragaite ‘holds’, ChSI. driiZati ‘hold’, guttural ex- tensions of IE *dher- in Skt. dhr- ‘hold, support’, ete. Walde-P. 1.859. Ernout- M. 382f. Otherwise (fr. *bhergh- in Skt. brhant- ‘great, mighty, high’, Ay. barazant- ‘high’, etc.) Walde-H. 1.535 ff.
7664:Lat. infirmus, neg. of firmus ‘fast, solid, firm, strong’ : Skt. dhr-, Av. dar- ‘hold, support’, etc. (cf. Lat. fortis ‘strong’, 4.81). Walde-P. 1.859. Er- nout-M, 364.
12102:‘footstool’, fr. the root *dher- in Skt. dhr- ‘hold, support’, etc. (11.15). Walde- P. 1.857. Boisacq 349.
18918:11.15 HOLD Grk.  &w Goth. haban Lith.  laikyti NG par, Baord ON halda (hafa) Lett. turét Lat. _tenére Dan. holde ChSl.  driiZati It. tenere Sw. hdlla SCr.  drzati Fr. lenir OE healdan (habban) Boh. — drieli Sp. tener ME sholde Pol. — trzymaé Rum. fine ; NE hold Russ. erat’ Tr. congaibim Du. houden Skt. — dhr- NIr.  congbhaim OHG _habén (haltan) Av. dar-, drag-, hap- WwW. dal MHG haben, halten Br. derc’hel NHG _halten
18943:7. Skt. dhr-, Av. dar-, drag-, above, 6.
### WLD dher halten
21781:cymr. gafael „das Halten, Festhalten", wovon gafaelu „halten, festhalten", 
53991:2. dher- ( dhere -) „halten, festhalten, stiitzen“. 
54006:halten", av. dar- „halten, festhalten, zuriickhalten ; woran festhalten, es be- 
54116:dlieregh- „halten, festhalten; fest", aksl. drzzq, drbzati „halten, inne-
```


## [2026-09-05T20:13:39.418Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '53991,53996p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== dheregh npers darz ===\"; grep -n \"darzman\\|darzan\\|npers. darz\\|darz „Naht\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"=== WLD pages calibration ===\"; python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'halten, festhalten, stiitzen' in pg or 'halten, festhalten, stützen' in pg:\n        print('leaf',i, pg[:120].replace('\\n',' '))\nEOF",
 "description": "Read Walde-Pokorny dher"
}
```


### [2026-09-05T20:13:41.479Z] TOOL RESULT

```
2. dher- ( dhere -) „halten, festhalten, stiitzen“. 

Ai. dhar- „halten, tragen, stutzen, erhalten, aufrecht halten“, vratam 

„ein Gesetz beobachten“ (Praes. meist dhardyati ; Pf. dadhdra , dadhre; 

=== dheregh npers darz ===
54412:Npers. darz, darza „Naht“, darzman, d irznan „Faden“, dnrzan „Nadel“, 
=== WLD pages calibration ===
leaf 864                            :     856                                                   dher-         Lat. fraces „Olhefe
```


## [2026-09-05T20:13:48.457Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'Naht' in pg and 'darz' in pg:\n        m=re.search(r'\\b(8\\d\\d)\\b',pg[:300])\n        print('leaf',i,'hdr:',pg[:100].replace('\\n',' '))\nEOF",
 "description": "Find WLD page for darz"
}
```


### [2026-09-05T20:13:50.439Z] TOOL RESULT

```
leaf 867 hdr:                                                   dher-                                             
leaf 871 hdr:                                  dhergh-, dhregh           dberbh-                              863
```


## [2026-09-05T20:13:50.798Z] TOOL CALL #77: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%B2%D9%85%D8%A7%D9%86/\" \"https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 128: Mo'in entries for darzman / bahador\"; done",
 "description": "Fetch Moin entries"
}
```


### [2026-09-05T20:13:54.788Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/35f5f03c9e361843.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd38d7677df2c130.txt
```


## [2026-09-05T20:13:57.795Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### darzman\"; grep -n -A6 \"معین\" 35f5f03c9e361843.txt | head -30; echo; echo \"### bahador\"; grep -n -A8 \"معین\" bd38d7677df2c130.txt | head -30",
 "description": "Read Moin entries from abadis"
}
```


### [2026-09-05T20:13:57.864Z] TOOL RESULT

```
### darzman
77:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
78-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
79-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
80-
81- به روزگار حضرت عمر . . . . . . . . . . . . . . .
82-
83- در ایامِ . . . . . . . . . . . . . . . . .
--
96: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
97-
98- لینک ها 
99-
100- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
101-
102- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 

### bahador
35: فرهنگ معین
36-
37- (بَ دُ ) [ تر. ] (ص . ) دلیر، دلاور، شجاع . 
38-
39- فرهنگ عمید
40-
41- ۱. شجاع، دلیر، دلاور.
42-۲. پهلوان. 
43-
--
87:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
88-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
89-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
90-
91- منابع • https://archive.org/details/1_20221023_20221023_1515 
92- منبع. عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی
93-لینک کتاب فرهنگ واژه های اوستا
94-قرار می می دهم چون واژه درش دوستان می تواند بررسی کنید و ببینید
95-زبان های ترکی�در چند مرحله بر�زبان فارسی�تأثیر گذاشته است. نخستین تأثیر زبان ترکی بر پارسی، در زمان حضور سربازان تُرک در ارتش�سامانیان�روی داد. پس از آن، در زمان فرمان روایی�غزنویان، �سلجوقیان�و پس از�حملهٔ مغول، تعداد بیشتری�وام واژهٔ�ترکی به زبان فارسی راه یافت؛ اما بیشترین راه یابی واژه های ترکی به زبان فارسی در زمان فرمانروایی�صفویان، که ترکمانان�قزلباش�در تأسیس آن نقش اساسی داشتند، و�قاجاریان�بر ایران بود. 
--
100:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
101-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
102-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
103-
104- منابع • https://archive.org/details/1_20221023_20221023_1515 
105- دوستان این شخص هزار حساب کاربری دارد موقعی که کم می آورد اینقدر آدم ضعیفی هست به توهین رجوع می کند با حساب مهدی یا حساب دیگرش
106-استاد هزار چهره آبادیس قدیمی ترین حساب بش جدیری عضو از�٥ سال پیش هست 
107-حرف استاد عزیز پاین 
108- ... [مشاهده متن کامل] 
--
```


## [2026-09-05T20:14:13.621Z] TOOL CALL #79: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%B2/\" \"https://abadis.ir/fatofa/%D8%B2%D9%86%D9%87%D8%A7%D8%B1/\" \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2/\" \"https://abadis.ir/fatofa/%D8%AF%D8%A7%D8%B1%D9%88/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 128: Mo'in entries darz/zenhar/andarz/daru\"; done; cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in $(python3 - <<'EOF'\nimport hashlib\nfor u in [\"https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%B2/\",\"https://abadis.ir/fatofa/%D8%B2%D9%86%D9%87%D8%A7%D8%B1/\",\"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2/\",\"https://abadis.ir/fatofa/%D8%AF%D8%A7%D8%B1%D9%88/\"]:\n    print(hashlib.sha1(u.encode()).hexdigest()[:16])\nEOF\n); do echo \"##### $f\"; grep -n -A4 \"فرهنگ معین\" $f.txt | head -12; done",
 "description": "Fetch and read Moin entries"
}
```


### [2026-09-05T20:14:21.181Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b810663320d98c9c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c19eb33366ba12a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/48cc30a90b2eec90.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27e058e966d1e0b0.txt
##### b810663320d98c9c
43: فرهنگ معین
44-
45- (دَ رْ زْ ) (اِ. ) ۱ - شکاف باریک . ۲ - واحد مساحت تقریباً معادل ۲۱ متر. 
46-
47- فرهنگ عمید
--
211: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
212-
213- لینک ها 
214-
215- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
##### c19eb33366ba12a5
62: فرهنگ معین
63-
64- (زِ ) نک زینهار. 
65-
66- فرهنگ عمید
--
201: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
202-
203- لینک ها 
204-
205- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
##### 48cc30a90b2eec90
66: فرهنگ معین
67-
68- (اَ دَ ) [ په . ] (اِ. ) ۱ - پند، نصیحت . ۲ - وصیت . 
69-
70- فرهنگ عمید
--
144: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
145-
146- لینک ها 
147-
148- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
##### 27e058e966d1e0b0
45: فرهنگ معین
46-
47- [ په . ] (اِ. ) ۱ - آن چه پزشک برای درمان بیمار تجویز می کند. ۲ - درمان . 
48-
49- فرهنگ عمید
--
266: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
267-
268- لینک ها 
269-
270- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد.
```


## [2026-09-05T20:14:28.353Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '7810,7832p' ARY_latin_index_pages.txt; echo \"=== pdf page ===\"; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\nfor i,l in enumerate(lines,1):\n    m=re.match(r'\\s*\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if i in (7813,7828): print(i,cur,l[:80])\nEOF",
 "description": "Read Aryanpur index around DARZ"
}
```


### [2026-09-05T20:14:30.027Z] TOOL RESULT

```
.
|
CARKA ——_:(TOKHARIAN B) B ins DEREZA, DAREZ- (AVESTAN) gw
DARH- SANSKRIT) Gy Sikes DARZ PAHLAVD 65 hy,
DEJAK, DERJAN (ARMENIAN) gu) DARES MOSSETIC) ual
DRETH ALBANIAN) | gisT DEZI (RURDISH) «52,5
‘TARNAHL HITTITE) <a (TORHARIAN A) A. 5 jis
TARNA, TARK, CARK .
[pdf page 271]
a]
MACKENZIE: (SEAM) 131 REFERENCES beth
are «eb iy poKomy SStS~*~S~«S
oi teetlool
03S pSme rey Sale y gles! 205 cal pe
: Days LS st 22 aly gal pe
wake gesl 2 Sls cal
wala cody cQ ale aflel 16 J89 elak5 22 oly gil ee
Day 152532 05s cal
seal gt IG chlo 9% 4 DARZIG Gsr5ly hy Obj 22-1
GETROUW (DUTCH) sake DRVA- AVESTAN) gl
DRUTAS LITHUANIAN) gp: (OLD PERSIAN) kal .go3\,
DRUWIS (OLD PRUSSIAN) S53. DRU-DRSHTI, DRUVA-DRSHTI
DERB HOLD IRISH) AS 54) 2! DURUST, DRUST (PAHLAVI) 5},
=== pdf page ===
7813 270 DARH- SANSKRIT) Gy Sikes DARZ PAHLAVD 65 hy,
7828 271 seal gt IG chlo 9% 4 DARZIG Gsr5ly hy Obj 22-1
```


## [2026-09-05T20:14:37.320Z] TOOL CALL #81: Bash

```json
{
 "command": "pdftoppm -f 128 -l 128 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/128 && ls -la data/verification/sources/refs/ocr/BOOK/128.png",
 "description": "Render page 128 PNG for audit"
}
```


### [2026-09-05T20:14:39.601Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 83553 Sep  5 16:14 data/verification/sources/refs/ocr/BOOK/128.png
```


## [2026-09-05T20:16:14.909Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG dar\"; grep -n \"\\*dar\\b\\|\\*dar \\|to hold, keep\" CHEUNG.txt | head -8; echo \"### KLN farm/confirm\"; grep -n \"^farm,\\|farm,  n\\.\\|confirm,  tr\" KLN_1966.txt | head -5; echo \"### SKT firm\"; grep -n \"firm\\. (F\\|firm, adj\\|farm, sb\" SKT.txt | head -5",
 "description": "Final source greps"
}
```


### [2026-09-05T20:16:14.992Z] TOOL RESULT

```
### CHEUNG dar
1865:Orm. ur-uk ‘to hold, keep’ || (+ 4-) Par. ar-/awur ‘to bring’ || (+ *ni-) Orm. 
4775:*dar! *to hold, keep; [intr.] to dwell 
4777:*AVESTAN: dar- ‘to hold, keep’ || (+ *aua-) caus. ‘to hold to, apply to’ || (+ *ui-) ‘to 
4805:MIDDLE PERSIAN: MMP d'r-, BMP d’I- (YHSNN-) /ааг-/ ‘to hold, keep’ || (+ 
4815:*PARTHIAN: d'r- ‘to hold, keep’ = Ghilain: 74 | DMMPP: 135a f. 
4869:*SANSKRIT: dhar ‘to hold, keep, preserve’ (RV+) = EWAia I: 778 
4888:*dar? ‘to tear, split’ 
5011:© The Ir. forms above are probably etymologically related to the forms of *dar?: 
### KLN farm/confirm
8671:confirm,  tr.  v.  —  OF.  confermer  (F.  confirmer),  fr. L.  confirmare,  ‘to  make  firm’,  fr.  con-  and  fir- mare,  ‘to  make  firm  or  steady’,  fr.  firmus.  See firm,  adj.,  and  cp.  affirm,  infirm.
14393:farm,  n.  —  ME.  ferme,  ‘rent,  lease’,  fr.  MF. (=  F.)  ferme,  ‘lease’,  fr.  ML .firma,  ‘fixed  pay¬ ment’,  fr.  L  .firmare,  ‘to  strengthen,  fix,  establish’, fr.  firmus,  ‘strong,  fixed,  firm’.  See  firm,  adj. Derivatives:  farmer  (q.v.),  farm-ing,  n.
### SKT firm
```


## [2026-09-05T20:16:17.842Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4775,4790p' CHEUNG.txt; echo \"...\"; sed -n '4885,4900p' CHEUNG.txt",
 "description": "Read Cheung dar entry"
}
```


### [2026-09-05T20:16:17.902Z] TOOL RESULT

```
*dar! *to hold, keep; [intr.] to dwell 

*AVESTAN: dar- ‘to hold, keep’ || (+ *aua-) caus. ‘to hold to, apply to’ || (+ *ui-) ‘to 
support’ = Liste: 27f. 

Aor. athem.: INJ. med. 3sg. OAv. dorotä (Y 44.4), OPT. med. 3sg. OAv. dritä (Y 46.5); Aor. {2} s-: INJ. 
3sg. OAv. darast (Y 43.13), ? dorast (Y 49.2); Perf.: IND. 3sg. YAv. dadara (Yt 13.67), med. 3sg. OAv. 
dadré (Y 51.8); Partic.: pres. caus. YAv. "viöäraiiamna- (H 2.7), perf. med. YAv. daöräna- (Vr 2.5), pass. 
Y Av. dorata- (Y 10.17); Inf.: aor. OAv. deroidiiai (Y 43.1); Caus.: pres. IND. 2sg. YAv. däraiichi (Y 
11.3), 3sg. Y Av. vióaraiieiti (Yt 10.28, Yt 10.48, Yt 14.36, etc.), med. 35р. YAv. "paiti daraiiete (FrW 
4.3), 3р1. Y Av. daraiieinti (Yt 7.3, Ny 3.5), INJ. 1sg. vidaraém (Yt 13.2, etc.), 2sg. OAv. daraiio (Y 32.1), 
3sg. däraiiat (Y 31.7, etc.), 3pl. YAv. viöäraiion (Y 23.1, Y 67.1, Yt 13.22), SUBJ. med. 3sg. ҮАУ. 
*däraiiäite (FrW 4.3), ОРТ. 2sg. Y Av. vióaraiiois (Yt 14.44), 3sg. Y Av. “fra.daraiidit (N 67), IMPV. med. 
2р1. YAv. ашпа ... daraiiaópom (Vr 15.1, Vr 15.4 £); Desid.: pres. INJ. med. 3sg. OAv. didarosata (Y 
46.7) 

...
2002: 121, 123, 125 (passim); Kiefer 2003: 195; ESIJa II: 332 ff.; Korn 2005: 320, 372 


*dar? ‘to tear, split’ 
*AVESTAN: YAv. dar- ‘to tear’ || (+ *aua-) ‘to tear down’ || (+ *pari-) ‘to tear off by 
twisting’ (or rather ‘to let (the ears) burst’, Praust 2000: 438, fn. 40) || (+ *nis-) ‘to 


tear, take ош” = Liste: 28 

Pres. na-: IND. 3pl. YAv. dorononti (V 19.28); Partic.: pres. Y Av. auua.doronant- (V 18.19, V 18.22), 
perf. pass. YAv. dorota- (Yt 10.125, V 7.35); Caus.: pres. IND. 3pl. YAv. pairi.daraiieinti (Yt 14.56); 
Intens.: pres. OPT. 350. YAv. niZdaro.dairiiat (V 18.38, rep.). © According to Praust, l.c: 438, the nasal 
pres. formation may have analogically arisen after the (unattested) Ir. correspondence of Skt. smati 
‘breaks, shatters’ (Ir. *sarH°). This nasal formation must be of Pir. origin as it is widely attested in many 
Ir. languages. Moreover, it is most likely to be Рг. already, cf. opt. 3sg. drniyat (SB).
```


## [2026-09-05T20:16:23.206Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*darz\\|\\*darj\" CHEUNG.txt | head -6; echo \"---\"; grep -n \"PIE \\*d.er\" CHEUNG.txt | head -5; sed -n '4870,4884p' CHEUNG.txt",
 "description": "Cheung darz and PIE note"
}
```


### [2026-09-05T20:16:23.298Z] TOOL RESULT

```
4871:9 In many Ir. languages the suppletive past stem has been imported from *darz. 
5107:*darz ‘to attach, fasten; to load; to sew’ 
5112:*darz, being INJ. 3sg. of an athem. aor. — Liste: 28 
5117:*darz 63 
5940:command’ (*ham- + *darz). = Ghilain: 51 | DMMPP: 141a, 96, 252b, 46a f. 
55305:*band (s.v.), *čap, *darz, 
---
4873:«PIE *d'er- ‘to hold’ > LIV: 145 f. | Pok.: 252 ff. 
5078:«PIE *d'ers- ‘to attack, venture, dare, be bold, audacious’ > LIV: 147 | Pok.: 259 
5172:“PIE *d'erg"- (*d'reg^-) ‘to hold, fasten’ ? > LIV: 126 | Pok.: 213, 254 

9 In many Ir. languages the suppletive past stem has been imported from *darz. 

«PIE *d'er- ‘to hold’ > LIV: 145 f. | Pok.: 252 ff. 

*IE COGNATES: Hitt. /dar-/ ‘to hold, to say (?)’, Lat. firmus ‘firm, steady’, Lith. derü 


‘I am good for’ 

*REFERENCES: KPF I: 80b f., 138b f., 206b, 245b; KPF II: 182; Ivanow 1926: 420; EVP: 38; IIFL I: 250b, 
393a; Christensen, Contributions I: 64, 160 f., 258; Christensen, Contributions II: 54 £., 114, 158; IIFL II: 
223b f., 548; Abrahamian 1936: 112, 129, 133; Lambton 1938: 42a; Andreev — PeSéereva: 248b; Abaev, 
Slovar’ I: 345 f., 195 f., 470; Abaev, Slovar’ II: 18; Yarshater 1969: 183; EVS: 31b, 58a, 89a, 55a; Lecoq 
1974: 62; WIM I: 67; Werba 1997: 200; Steblin-Kamenskij 1999: 167, 402; Cheung 2002: 165; Lecoq
```


## [2026-09-05T20:16:26.180Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5107,5125p' CHEUNG.txt; echo \"...\"; sed -n '5168,5178p' CHEUNG.txt",
 "description": "Read Cheung darz entry"
}
```


### [2026-09-05T20:16:26.244Z] TOOL RESULT

```
*darz ‘to attach, fasten; to load; to sew’ 
*AVESTAN: daraz- ‘to attach’ || (+ *ni-) ‘to fasten’ || (+ *ham-) ‘to bind together’. > 
According to Pirart, Kellens — Pirart I: 232, OAv. dorost (Y 49.2) might belong to 


*darz, being INJ. 3sg. of an athem. aor. — Liste: 28 
Pres. -aja-: IND. 35р. YAv. (4-)darazaiieiti (Yt 10.48, Yt 14.63, N 99, Yt 8.55), 3pl. YAv. han.daroZanti 
(? "han.darozaiieinti) (N 101), SUBJ. 3sg. YAv. -doraziiaiti ("-dorozaiiaiti) (N 94), 3pl. ? ҮАУ. 


*darz 63 


*nidarozaiianti (У 6.47), med. Y Av. nidarozaiiánte (V 6.47), OPT. 3sg. YAv. àdarozaiioit (Yt 8.55), 3р1. 
Y Av. nidarozaiion (V 6.46), YAv. handarozaiion (V 9.49), med. Y Av. nidarozaiianta (V 6.47), IMPV. 
2р1. med. Y Av. nidarozaiiaóom (Yt 1.27); Desid.: pres. INJ. 2sg. OAv. didoroZo (Y 44.15) 


*MIDDLE PERSIAN: (+ *ham-) BMP hndlcyn- /handarzén-/ ‘to advise’, "ndrz ‘order, 
...
Orm. palast ‘to wring, fold’ 

*SANSKRIT: darh ‘to fix, make firm, make strong’ (RV+) = EWAia I: 706 f. 

“PIE *d'erg"- (*d'reg^-) ‘to hold, fasten’ ? > LIV: 126 | Pok.: 213, 254 


64 *das] ? 


*IE COGNATES: Gr. ёро ссоцол ‘I grasp’, OCS dreZati ‘hold, possess’, Russ. derzat’,
```


## [2026-09-05T20:29:35.658Z] TOOL CALL #86: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build128.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan / Old Persian\", words=\"dâr 2, dr\",\n  verdict=\"confirmed\",\n  derivation=(\"Avestan dar- and Old Persian dar- are the regular Iranian continuations of PIE *dʰer- \"\n    \"'to hold, support': the causative-shaped present *dʰér-eye- > Proto-Iranian *dāraya- gives Av. dāraiieiti \"\n    \"'he holds' and OP dārayatiy / dārayāmiy 'I hold' (Behistun I 26, DNb 14). Nourai's second form 'dr' is \"\n    \"the zero grade *dṛ- seen in the athematic aorist OAv. dərətā (Y 44.4), the optative drītā (Y 46.5) and the \"\n    \"participle dərəta-; the alternation dār-/dərə- is exactly the full-grade/zero-grade pair the root predicts. \"\n    \"The gloss 'to hold' is right; Bartholomae's own definition is 'halten; fassen'. Semantically Avestan already \"\n    \"has the extended senses 'to keep to (a law), to keep in mind', which is what feeds the Persian branch below.\"),\n  derivation_fa=(\"ریشهٔ ایرانی باستان *dar- «داشتن، نگاه داشتن» دنبالهٔ راستین ریشهٔ هندواروپایی آغازین *dʰer- است. \"\n    \"ستاک مضارع در اوستایی dāraiieiti و در پارسی باستان dārayatiy/dārayāmiy است که در سنگ‌نوشتهٔ بیستون آمده است؛ \"\n    \"صورت dr که نورایی آورده، همان گونهٔ ضعیف (صفر‌پایه) *dṛ- است که در dərətā و dərəta- دیده می‌شود. \"\n    \"بارتولومه معنی را «halten; fassen» می‌دهد و کنت در واژه‌نامهٔ پارسی باستان همین را به *dʰer- می‌رساند. ادعای نورایی درست است.\"),\n  sources=[W+\"Reconstruction:Proto-Indo-European/d%CA%B0er-\", W+\"%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\"],\n  ref_check=[{\"ref\":\"POK:252\",\"status\":\"supports\",\"note\":\"POK_01.txt line 3592 ff. (IEW p.252, '2. dher-, dherə- „halten, festhalten, stützen“'): 'av. dar- „halten, festhalten, zurückhalten; woran festhalten, es beobachten (ein Gesetz); fest im Gedächtnis halten“ (dārayeiti usw., Partiz. darəta-), ap. dārayāmiy „halte“, npers. Inf. dāstan [dāštan]'. The Avestan/Old-Persian box is copied straight out of this page.\"}],\n  consulted=[\n   {\"src\":\"BRT\",\"where\":\"col. 686 ff. (BRT.txt line 12844)\",\"stance\":\"supports\",\"note\":\"'j., g., p. 1dar- V. „halten; fassen“. Praes. … 30 (Iter.) dāraya-… PPfP. dərəta-; Inf. darədyai…' — both the full grade dār- and the zero grade dərə- Nourai writes as 'dr'.\"},\n   {\"src\":\"KNT\",\"where\":\"Lexicon s.v. dar- (KNT.txt line 5517)\",\"stance\":\"supports\",\"note\":\"'1dar- vb. „hold; (intrans.) dwell”: Av. dar-, Skt. dhr-, Lt. fir-mus “firm”, Lith. daryti “to make”, pIE *dher- … Present stem dāraya- … dārayāmiy 1st sg. … adārayā imf.'\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *dar¹ (CHEUNG.txt line 4775 ff.)\",\"stance\":\"supports\",\"note\":\"'*dar¹ “to hold, keep; [intr.] to dwell” — AVESTAN: dar- “to hold, keep” … «PIE *dʰer- “to hold” > LIV: 145 f. | Pok.: 252 ff.»'\"}])\n\nN(id=2, lang=\"Pahlavi\", words=\"dâštan; pad-en-dâštan\",\n  verdict=\"confirmed\",\n  derivation=(\"Middle Persian dāštan, present stem dār- (Book Pahlavi ideogram YHSNN-tn', phonetic d'štn'/d'l-; Manichaean \"\n    \"dʾštn), continues OP dārayatiy. The past stem is analogical: Old Iranian *dṛ-ta- should have given MP *dird/*dart, \"\n    \"so dāšt was rebuilt on the -št past of verbs like hāšt/āšt (Abolghasemi, FFD p.52, says exactly this). \"\n    \"'pad-en-dāštan' is the phrasal idiom pad ēn/ēd dāštan 'to hold by this = to take (something) for, to consider', \"\n    \"with pad 'to, at' + ēn/ēd 'this'; MacKenzie prints 'pad ēd dāštan [cf. N pindāštan] consider' and Nyberg \"\n    \"'pat ē ~ kū to be of the opinion that, to think, imagine that… cf NP pindāštan < *pa(t) ēn daštan'. \"\n    \"Nourai's node is right down to the hyphenation.\"),\n  derivation_fa=(\"در فارسی میانه (پهلوی) مصدر dāštan با ستاک مضارع dār- به کار می‌رفته است؛ مادهٔ ماضی dāšt قیاسی است، \"\n    \"زیرا از *dṛ-ta- ایرانی باستان باید *dird می‌آمد (ابوالقاسمی، فعل‌های فارسی دری، ص ۵۲ همین را می‌گوید). \"\n    \"ترکیب pad ēn/ēd dāštan یعنی «به این داشتن، چیزی را چیزی شمردن» است؛ مکنزی و نیبرگ هر دو آن را سرچشمهٔ «پنداشتن» فارسی می‌دانند. \"\n    \"ادعای نورایی درست است.\"),\n  sources=[W+\"%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\", W+\"%D9%BE%D9%86%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\"],\n  ref_check=[\n   {\"ref\":\"FFD:52\",\"status\":\"supports\",\"note\":\"FFD_pages.txt pdf page 57 (= printed 52, offset printed = pdf−5, calibrated on the running head of pdf 58): 'داشتن — داشت < فارسی میانه dāšt. به جای dāšt باید dṛta می‌آمد از *dṛ-ta ایرانی باستان … دار < فارسی میانه dār < ایرانی باستان *dāra-… dar به معنی «داشتن» است'.\"},\n   {\"ref\":\"FFD:43\",\"status\":\"supports\",\"note\":\"FFD_pages.txt pdf page 48 (= printed 43): 'پنداشتن — «پنداشتن» بازماندهٔ pad ēn dāštan فارسی میانه است. pad «به»، ēn «این»، dāštan «داشتن» روی هم به معنی «به چیزی شمردن»'. Exactly the form Nourai prints.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p.25 s.v. dāštan (PHD_mackenzie.txt line 1930 f.)\",\"stance\":\"supports\",\"note\":\"'dāštan, dār- [YHSNN-tn < A…; dʾltnʼ, dʾl- | M dʾštn, dʾr-, N —] have, hold, keep, preserve. pad … dāštan: hold by, to; take for. pad ēd dāštan [cf. N pindāštan] consider.'\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. dāštan (NYB_vol2_glossary.txt line 1220)\",\"stance\":\"supports\",\"note\":\"'pat ē ~ kū to be of the opinion that, to think, imagine that 25²⁵… cf NP pindāštan < *pa(t) ēn daštan'.\"}])\n\nN(id=3, lang=\"Persian\", words=\"-dâr 3 «ـدار ۳»; dâštan «داشتن»; pendâštan «پنداشتن» (extra: پندار)\",\n  verdict=\"confirmed\",\n  derivation=(\"All three continue the Pahlavi node without complication. (1) The agentive suffix -dār (\"\n    \"خزانه‌دار، سردار، جانبدار) is the bare present stem dār- used as the second member of a compound, already MP \"\n    \"'-dār [-dʾl | M -dʾr] suffix, -holder, -keeper' (MacKenzie); it is the -dar of English sirdar, zamindar. \"\n    \"(2) NP dāštan/dār- is MP dāštan/dār- unchanged. (3) pendāštan is the univerbation of MP pad ēn dāštan: \"\n    \"pad > pa- > pe(n)-, with the n of ēn absorbed into the prefix, giving pindāštan/pendāštan 'to suppose, imagine'; \"\n    \"the deverbal pendār 'پندار, notion, conceit' is built on the present stem in the usual Persian way. \"\n    \"Hübschmann already printed 'pindāštan „dafür halten“ = mp. pa īn daštan' (Pers. Stud. p.142).\"),\n  derivation_fa=(\"هر سه واژه بی‌واسطه از فارسی میانه به فارسی نو رسیده‌اند. پسوند «ـدار» (خزانه‌دار، سردار) همان ستاک مضارع dār- است که در \"\n    \"پهلوی نیز همین کارکرد را داشته است. «داشتن» دنبالهٔ بی‌دگرگونی dāštan پهلوی است، و «پنداشتن» فشردهٔ ترکیب pad ēn dāštan: \"\n    \"pad به pe- بدل شده و نون «این» در پیشوند جذب شده است؛ «پندار» نیز از ستاک مضارع همین فعل ساخته شده. هوبشمان (ص ۱۴۲) همین تحلیل را آورده است. ادعای نورایی درست است.\"),\n  sources=[W+\"%D9%BE%D9%86%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\", W+\"%D8%AF%D8%A7%D8%B4%D8%AA%D9%86\"],\n  ref_check=[\n   {\"ref\":\"BQT:810\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaf 270 (printed ≈810, the دارا/داراب spread that follows the دار headwords of p.809): the دار column reads 'و بمعنی داشتن و امر بداشتن هم هست', i.e. Borhān does gloss dār as the stem/imperative of dāštan, which is Nourai's suffix; but پنداشتن stands in the پ section (≈p.400), not here.\"},\n   {\"ref\":\"FFD:43\",\"status\":\"supports\",\"note\":\"same passage as node 2: FFD printed p.43 derives پنداشتن from MP pad ēn dāštan.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p.24 s.v. -dār (PHD_mackenzie.txt line 1882)\",\"stance\":\"supports\",\"note\":\"'-dār [-dʾl | M -dʾr, N —] suffix, -holder, -keeper.' — the suffix is already Middle Persian.\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.142 (HUB.txt line 4960 ff.)\",\"stance\":\"supports\",\"note\":\"'pindāštan „dafür halten“ = mp. pa īn daštan'.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann s.v. dhāros (IEC.txt line 2725)\",\"stance\":\"supports\",\"note\":\"'dhāros, ā “firm; firmness”. Cf. dher- … Per. dār “possessing”, in cpds.' — Mann lists the Persian -dār suffix under the same root.\"}])\n\nN(id=4, lang=\"Persian\", words=\"darmân «درمان»; dârŭ «دارو»\",\n  verdict=\"disputed\",\n  derivation=(\"Two words with different fates. (a) darmān 'cure' is secure: MP darmān [dlmʾin] 'remedy, medicine' \"\n    \"(MacKenzie p.24), from Old Iranian *dar-man- 'a holding, maintaining' → 'restoration', i.e. PIE *dʰér-mn̥, \"\n    \"the exact formation of Sanskrit dhárman- 'support, prop, statute' and of Latin firmus (*dʰer-mo-). \"\n    \"Horn no.554 (p.123) gives 'dermān „Arzenei“ … √dʰar- „halten“ … phlv. darmān', and the same word was lent to \"\n    \"Armenian darman and Syriac darmānā. (b) dārū 'medicine' is where Nourai's chart is contradicted. \"\n    \"Horn no.523 (p.116) did put dārū under √dʰar-, and Nourai follows him, but he prints his own reservation \"\n    \"(ETM:65 → Deru 1); modern scholarship agrees with the reservation. NP دارو < MP dārūg [dʾlwkʼ] < \"\n    \"Proto-Iranian *dāru-ka- 'of wood, herbal', a -ka- derivative of *dāru 'wood, tree' (PIE *dóru), cf. Parthian \"\n    \"dālūg 'plant, tree', Avestan dauru-, Sanskrit dāru 'wood'; the sense went 'plant matter' → 'herbal remedy' → \"\n    \"'drug, gunpowder'. Mo'in's own footnote in Borhān (the دارو note carried on p.813) ends 'اصل آن مشکوک است' \"\n    \"citing Hübschmann. Verdict for the node = disputed, driven by dārū; darmān alone would be confirmed.\"),\n  derivation_fa=(\"این گره دو واژه دارد که سرنوشتشان یکی نیست. «درمان» از فارسی میانه darmān و آن از *dar-man- ایرانی باستان است، \"\n    \"همان ساخت *dʰér-mn̥ که در سنسکریت dhárman- و در لاتین firmus دیده می‌شود؛ هرن (شمارهٔ ۵۵۴) و حاشیهٔ معین بر برهان قاطع (ص ۸۴۰) هر دو این را تأیید می‌کنند. \"\n    \"امّا «دارو» را پژوهش امروزی از این ریشه نمی‌گیرد: فارسی نو «دارو» < پهلوی dārūg < ایرانی باستان *dāru-ka- «چوبی، گیاهی» \"\n    \"از *dāru «چوب، درخت» (قس: پارتی dālūg، اوستایی dauru-، سنسکریت dāru)، یعنی از ریشهٔ Deru که خود نورایی هم در یادداشت به آن اشاره کرده است. پس این پاره از ادعای نورایی رد می‌شود.\"),\n  sources=[W+\"%D8%AF%D8%B1%D9%85%D8%A7%D9%86\", W+\"%D8%AF%D8%A7%D8%B1%D9%88\", \"https://abadis.ir/fatofa/%D8%AF%D8%A7%D8%B1%D9%88/\"],\n  ref_check=[\n   {\"ref\":\"BQT:840\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 300 (printed 840): headword 'درمان — بروزن فرمان … و دارو باشد', with Mo'in's footnote 7 'پهلوی darmān «معین ۱۷۲۹» از ریشهٔ *dar- «بارتولمه»'. Supports darmān on exactly the cited page.\"},\n   {\"ref\":\"HRN:123\",\"status\":\"supports\",\"note\":\"Horn, Grundriss no.554 (leaf 145 = p.123): 'dermān „Arzenei“, vergl. dārū (No. 523) … √dʰar- „halten“, vergl. aw. drva- „gesund“; phlv. darmān „Arzenei“.'\"},\n   {\"ref\":\"HRN:116\",\"status\":\"partial\",\"note\":\"Horn no.523 (leaf 138 = p.116): 'dārū, dārūt „Arznei; Schiesspulver“, vergl. dermān (No. 554). √dʰar- „halten“ … phlv. dārūk „Arznei“.' Horn does say what Nourai's arrow says, but the immediately preceding entry (no.522 dār „Baumstamm, Holz“, aw. dauru-) is the derivation the field has since adopted.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p.24 (PHD_mackenzie.txt lines 1897, 1902)\",\"stance\":\"partial\",\"note\":\"'darmān [dlmʾin | M drmʾn, N —] remedy, medicine' and 'dārūg [dʾlwkʼ | M dʾrwg, N dārū] drug, medicament' — both MP forms confirmed, but MacKenzie gives no root.\"},\n   {\"src\":\"BQT\",\"where\":\"vol.2 leaf 273 (printed ≈813), the دارو footnote\",\"stance\":\"contradicts\",\"note\":\"Mo'in: 'دارو — پهلوی dārūk … کردی و افغانی و بلوچی dārū … اصل آن مشکوک است «هوبشمان ۳۲۵»' — 'its origin is uncertain', i.e. Mo'in does not endorse the dher- derivation.\"},\n   {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi s.v. دارو (via abadis.ir)\",\"stance\":\"partial\",\"note\":\"'[ په . ] (اِ. ) ۱- آن چه پزشک برای درمان بیمار تجویز می کند' — Mo'in tags it Pahlavi only, no IE root.\"}])\n\nN(id=5, lang=\"Avestan\", words=\"zaenô-hara\",\n  verdict=\"disputed\",\n  derivation=(\"The word Nourai prints is not an attested Avestan compound. Bartholomae's Altiranisches Wörterbuch has \"\n    \"zaena- m. 'Waffe' (col. 1651) and a separate zaenah- n. 'Wachsein', zaenaŋhan- 'wachend, wachsam', \"\n    \"zaeni-buδra- 'wachsam', but no *zaenō-hara-. The form is a modern reconstruction: Hübschmann's reading of \"\n    \"NP زینهار as *zaena-hāra- 'weapon-guarding, guarding one's arms', which Mo'in reproduces in his footnote to \"\n    \"زینهار in Borhān. Even on that reading the second member is Old Iranian hār-/har- 'to guard, watch over', \"\n    \"which goes back to PIE *ser- 'to protect, watch over' (Skt. sar-, Lat. servāre) — not to *dʰer-; Avestan d- \"\n    \"never becomes h-. So the arrow drawn from node 1 (Av./OP dār-) cannot stand phonetically. Horn (no.527, \"\n    \"p.117) does hang zīnhār tentatively on dāštan ('halte dich von diesem zurück'), but he immediately objects \"\n    \"that Ferdowsi scans zīnhār as an amphimacer and that he cannot then explain the quantity. The reading now \"\n    \"usually printed (Nöldeke, Henning, MacKenzie, Wiktionary) is az + ēn + hār 'guard against this'.\"),\n  derivation_fa=(\"صورت zaenō-hara در متون اوستایی گواهی نشده است؛ بارتولومه تنها zaena- «سلاح» و جداگانه zaenah- «بیداری» را ثبت کرده است. \"\n    \"این ترکیب بازساختهٔ هوبشمان است که معین در حاشیهٔ «زینهار» برهان قاطع نقل کرده است. حتی بر همان خوانش نیز جزء دوم از ریشهٔ hār-/har- \"\n    \"«پاس داشتن» است که به هندواروپایی *ser- می‌رسد، نه به *dʰer-؛ دال اوستایی هرگز به هـ بدل نمی‌شود. بنابراین پیوند این گره به «دار» درست نیست و پژوهش امروزی \"\n    \"(نولدکه، هنینگ، مکنزی) تحلیل az ـ ēn ـ hār «از این بپرهیز» را می‌پذیرد.\"),\n  sources=[W+\"%D8%B2%D9%86%D9%87%D8%A7%D8%B1\"],\n  ref_check=[\n   {\"ref\":\"BQT:1055\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 517 (printed ≈1055–1057; the headword is زینهار/زنهار 'که پناه جستن و امان خواستن باشد'). Mo'in's footnote: 'پهلوی zēnhār (امن، امان)، سغدی zʾynhʾr (پناه، امان)، رک: مقالهٔ Henning … آن را مرکّب از az ēn hār می‌داند، یعنی از این پرهیز؛ … آن را zaenō-hāra اوستایی (سلاح‌حامی) می‌داند؛ هوبشمان گوید که وجه اخیر به‌نظر من بهتر است'. The page really does carry Nourai's form — as one of two competing analyses.\"},\n   {\"ref\":\"HRN:117\",\"status\":\"partial\",\"note\":\"Horn leaf 139 = p.117, appended to no.527 dāšten: 'Gehört hierher vielleicht auch zīnhār, zinhār „Schutz, Sicherheit etc.“, ursprünglich „hüte dich vor diesem, halte dich von diesem zurück“? Allerdings wüsste ich dann nicht die Messung von zīnhār als Amphimacrus bei Firdūsī zu erklären…'. Horn hangs it on dāštan only tentatively and with an explicit metrical objection; and his analysis is not Nourai's zaenō-hara.\"}],\n  consulted=[\n   {\"src\":\"BRT\",\"where\":\"col. 1651 (BRT.txt lines 27499–27513)\",\"stance\":\"contradicts\",\"note\":\"'j. zaena- m. „Waffe“ … j. zaenaŋhan- Adj. „wachend, wachsam“ … j. zaenah- n.: sva. zaeman- … j. zaenahʷvant- Adj. „wachsam, regsam“' — no compound *zaenō-hara- anywhere in the dictionary.\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.142 (HUB.txt line 4960)\",\"stance\":\"partial\",\"note\":\"'zinhār „Schutz, Sicherheit, gieb Acht! hüte dich!“ = zinhar (zīnehar)' — Hübschmann lists the word among ap. ai > NP i cases but gives it no verbal root here.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"Etym. Dict. of the Iranian Verb (no *dar entry covers hār-)\",\"stance\":\"silent\",\"note\":\"Cheung's *dar¹ 'to hold' article (CHEUNG.txt 4775 ff.) has no zīnhār material; the guarding verb belongs to his *har-/*sar- family, i.e. PIE *ser-.\"}])\n\nN(id=6, lang=\"Persian\", words=\"zenhâr «زنهار» (extra: زینهار)\",\n  verdict=\"plausible\",\n  derivation=(\"The Persian word itself is beyond doubt: زنهار/زینهار continues MP zēnhār [zynhʾl] 'safety, quarter, \"\n    \"protection', with a Sogdian counterpart zʾynhʾr discussed by Henning ('Sogdian loan-words in New Persian'). \"\n    \"It began life as an imperative phrase 'beware! guard against this!' and was already lexicalised as a noun \"\n    \"'quarter, amnesty, safe-conduct' in Middle Persian, whence the classical Persian idioms زنهار خواستن, \"\n    \"زنهار دادن and the adverbial زنهار! 'on no account!'. The parent drawn here — Avestan *zaenō-hara- — is \"\n    \"Hübschmann's conjecture, one of two live readings; the other (Nöldeke–Henning–Wiktionary) is MP az + ēn + \"\n    \"hār-. Under either the first element is 'weapon' or 'this' and the second is hār- 'to guard' (PIE *ser-), so \"\n    \"the word's presence under Dher 1 is what is wrong, not the word. Plausible, with the parent link unproven.\"),\n  derivation_fa=(\"خود واژهٔ «زنهار/زینهار» بازماندهٔ zēnhār فارسی میانه به معنی «امان، پناه» است که همتای سغدی zʾynhʾr نیز دارد \"\n    \"(رک: مقالهٔ هنینگ دربارهٔ وام‌واژه‌های سغدی). نخست جمله‌واره‌ای امری به معنی «بپرهیز، پاس دار» بوده و سپس در همان دورهٔ میانه به اسم بدل شده است. \"\n    \"پدری که نورایی رسم کرده (zaenō-hara اوستایی) تنها یکی از دو تحلیل رایج است؛ پس واژه درست است ولی جای آن زیر ریشهٔ Dher پذیرفتنی نیست: با احتیاط.\"),\n  sources=[W+\"%D8%B2%D9%86%D9%87%D8%A7%D8%B1\", \"https://abadis.ir/fatofa/%D8%B2%D9%86%D9%87%D8%A7%D8%B1/\"],\n  ref_check=[\n   {\"ref\":\"BQT:1055\",\"status\":\"supports\",\"note\":\"Same page as node 5 (BQT_v2 leaf 517): the headword block 'زینهار … زنهار است که پناه جستن و امان خواستن باشد — و عهد و پیمان … و ترس و بیم' plus 'زنهاری = پناه آورنده' — word and glosses exactly as charted.\"}],\n  consulted=[\n   {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi s.v. زنهار (abadis.ir)\",\"stance\":\"partial\",\"note\":\"'(زِ ) نک زینهار.' — Mo'in makes زنهار a variant of زینهار and gives no root in the online text.\"},\n   {\"src\":\"HRN\",\"where\":\"no.527 note, p.117\",\"stance\":\"partial\",\"note\":\"Horn's tentative attachment to dāštan, with his own metrical caveat (quoted at node 5).\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.142\",\"stance\":\"supports\",\"note\":\"'zinhār „Schutz, Sicherheit, gieb Acht! hüte dich!“' — confirms both the form and the imperative origin of the sense.\"}])\n\nN(id=7, lang=\"Avestan\", words=\"dereza\",\n  verdict=\"confirmed\",\n  derivation=(\"Nourai's 'dereza' is Avestan darəz-/dərəz- 'to fasten, bind', with the noun darəza- m. 'the fastening, \"\n    \"binding, seizing' and dərəz- f. 'bond, fetter'. Bartholomae heads it 'darəz- V. „stabilire; vincire“' with \"\n    \"present darəzaiieiti 'binds fast, fetters', so the gloss 'to hold together, close, tighten' is a fair \"\n    \"rendering. Formally it is the velar extension *dʰer-ǵʰ- of *dʰer-, which is why Pokorny files it as one of the \"\n    \"'Gutturalerweiterungen' of dher-2 (IEW p.254, 'dheregh- „festhalten, fest“') and again at p.258 \"\n    \"('dheregh- (dʱr̥gh-nā-) „drehen, winden, wenden“, auch „spinnen, nähen“'). Cheung reconstructs *darz \"\n    \"'to attach, fasten; to load; to sew' < PIE *dʰergʰ- and files Pok. 213, 254 rather than 258.\"),\n  derivation_fa=(\"صورت اوستایی darəz-/dərəz- «بستن، محکم کردن» است با اسم darəza- «بستن، گرفتن» و dərəz- «بند، پابند»؛ \"\n    \"بارتولومه معنی «stabilire; vincire» داده است. این ریشه گسترش‌یافتهٔ کامی *dʰer-ǵʰ- از همان *dʰer- است و پوکورنی آن را در بخش \"\n    \"«گسترش‌های کامی» ذیل dher-2 آورده است (ص ۲۵۴ و باز ص ۲۵۸). ادعای نورایی درست است.\"),\n  sources=[W+\"%D8%AF%D8%B1%D8%B2\"],\n  ref_check=[\n   {\"ref\":\"POK:252\",\"status\":\"supports\",\"note\":\"IEW p.252 is the dher-2 headword itself (POK_01.txt line 3592); the guttural extensions that carry darəz- follow at p.254.\"},\n   {\"ref\":\"POK:258\",\"status\":\"supports\",\"note\":\"POK_01.txt line 3704 (IEW p.258): 'dheregh- (dʱr̥gh-nā-) „drehen, winden, wenden“ (auch „spinnen, nähen“). Npers. darz, darza „Naht“, darzmān, darznān „Faden“, darzan „Nadel“; pehl. darzīk „Schneider“'. The Avestan verb itself is on p.254: 'dheregh- „festhalten, fest“ … av. darəzayeiti „bindet fest, fesselt“, darəza- m. „das Befestigen, Binden, Fassen, Greifen“, dərəz- f. „Bande, Fessel“ … wohl auch npers. darz „Naht“'.\"}],\n  consulted=[\n   {\"src\":\"BRT\",\"where\":\"col. 687 (BRT.txt line 12952)\",\"stance\":\"supports\",\"note\":\"'j., g. darəz- V. „stabilire; vincire“. Praes. … 1) „festbinden, fesseln“ …'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 856 ff. / 863 (WLD_Bd1 djvu lines 53991, 54412)\",\"stance\":\"supports\",\"note\":\"'2. dher- (dherē-) „halten, festhalten, stützen“' and, under the guttural extension, 'Npers. darz, darza „Naht“, darzman, darznan „Faden“, darzan „Nadel“'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *darz (CHEUNG.txt line 5107 ff.)\",\"stance\":\"supports\",\"note\":\"'*darz “to attach, fasten; to load; to sew” — AVESTAN: darəz- “to attach” || (+ *ni-) “to fasten” || (+ *ham-) “to bind together” … «PIE *dʰergʰ- (*dʰregʰ-) “to hold, fasten” ? > LIV: 126 | Pok.: 213, 254»'.\"}])\n\nN(id=8, lang=\"Persian\", words=\"darz «درز»; darzî «درزی»; darzmân «درزمان»; darzan «درزن» (extra: درزه)\",\n  verdict=\"confirmed\",\n  derivation=(\"This is one of the best-attested nodes on the page: Pokorny's IEW p.258 prints Nourai's four words in a \"\n    \"row. NP darz 'seam, crack' continues MP darz [dlc] 'seam' (MacKenzie p.24) < Proto-Iranian *darjaka-/*dārjaka-, \"\n    \"from the verbal root *darz- 'to fasten, sew' < PIE *dʰerǵʰ-; the intervocalic *-j-/-ǵʰ- surfaces as Persian z \"\n    \"(Hübschmann p.228 uses exactly this family to show that Iranian ǵʰ gives NP z after r). darzī 'tailor' is \"\n    \"darz + the relational -ī, and is already MP darzīg 'tailor' (MacKenzie), Pahl. darzīk in Pokorny; darzan \"\n    \"'needle' is darz + the instrument suffix -an (cf. سوزن, خرمن); darzmān 'thread' has the -mān suffix of \"\n    \"زایمان/سامان. The Armenian loans derjak 'tailor', derjan 'thread', handerj 'garment' show the same \"\n    \"set was already Middle Iranian. Persian darz was later borrowed into Arabic as darz/طرز.\"),\n  derivation_fa=(\"این خانواده در خود کتاب پوکورنی (ص ۲۵۸) یکجا آمده است. «درز» از فارسی میانه darz و آن از ایرانی باستان *darjaka- \"\n    \"از ریشهٔ *darz- «بستن، دوختن» است؛ جیم/ǵʰ ایرانی پس از «ر» در فارسی به «ز» بدل می‌شود (هوبشمان، ص ۲۲۸). \"\n    \"«درزی» از darz ـ یای نسبت (پهلوی darzīg)، «درزن» با پسوند ابزارساز «ـن» (قس: سوزن) و «درزمان» با پسوند «ـمان» ساخته شده است. \"\n    \"وام‌واژه‌های ارمنی derjak «درزی» و derjan «نخ» گواهی می‌دهند که این مجموعه در دورهٔ میانه موجود بوده است. ادعای نورایی درست است.\"),\n  sources=[W+\"%D8%AF%D8%B1%D8%B2\", \"https://abadis.ir/fatofa/%D8%AF%D8%B1%D8%B2/\"],\n  ref_check=[\n   {\"ref\":\"HRN:122\",\"status\":\"supports\",\"note\":\"Horn leaf 144 = p.122, no.549: 'derz, derze „Naht“, derzmān, derzen, derzī (syr. LW.), … darzīn „Nadel“ … aw. dereza- „Fessel“, √darez- „festmachen“; ai. √darh-, dr̥ṁhati „befestigen“, arm. derjak „Schneider“, derjan „Faden“, handerj „Kleid“'. All four of Nourai's words, on the cited page.\"},\n   {\"ref\":\"MON:1510\",\"status\":\"not_checked\",\"note\":\"Mo'in's Farhang-e Fārsi is online only as entry text (vajehyab/abadis) without print pagination, and the local scans are the 2-vol Adena abridgement with different pages; the volume/page 1510 could not be located. The abadis text of درز ('(دَ رْ زْ ) (اِ. ) ۱ - شکاف باریک') carries no etymology.\"},\n   {\"ref\":\"CEL3:254\",\"status\":\"not_checked\",\"note\":\"S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words — refs_online.json records it as catalogue-only, no digitised copy anywhere permitted.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p.24 (PHD_mackenzie.txt line 1904 f.)\",\"stance\":\"supports\",\"note\":\"'darz [dlc | N —] seam.' followed by 'darzīg [-yk | N darzī] tailor.'\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien p.228 (HUB.txt line 7934)\",\"stance\":\"supports\",\"note\":\"'vgl. np. darzī „Schneider“, darzan „Nadel“, darz „Naht“, darzman „Faden“' — used by Hübschmann as his example of Iranian z > NP z after r.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt pdf 270–271 (printed ≈269–270)\",\"stance\":\"supports\",\"note\":\"Aryanpur's index groups 'DEREZA, DAREZ- (AVESTAN) … DARH- (SANSKRIT) … DARZ (PAHLAVI) … DARZIG … DERJAK, DERJAN (ARMENIAN) … MACKENZIE: (SEAM) 131 … POKORNY' — the same family, same authorities.\"},\n   {\"src\":\"POK\",\"where\":\"IEW p.258\",\"stance\":\"supports\",\"note\":\"quoted in ref_check above: darz, darza, darzmān, darznān, darzan, pehl. darzīk.\"}])\n\nN(id=9, lang=\"Avestan\", words=\"han-dareza\",\n  verdict=\"confirmed\",\n  derivation=(\"Avestan hąm-/han- (the prefix from PIE *sem- 'one, together', Nourai's ☞ Sem 1) prefixed to darəz-. \"\n    \"Bartholomae lists it under the root: 'mit hąm 1) „aneinander befestigen, zusammenbinden, vereinigen“ … \"\n    \"2) „fesseln“', citing handarəzanti (N. 101) and handarəzaiiən (V. 9.49); there is also the adjective \"\n    \"handarəzan- 'grasping, holding together'. Nourai's gloss 'pull together, unite, fortify' is exactly this. \"\n    \"Cheung files the same compound as *ham- + *darz and traces the Middle Persian continuation \"\n    \"handarzēn- 'to advise' straight from it. Before a dental the nasal appears as -n-, hence han-darəza-.\"),\n  derivation_fa=(\"پیشوند اوستایی hąm-/han- (از *sem- هندواروپایی به معنی «با هم، یک») بر سر ریشهٔ darəz- می‌آید. \"\n    \"بارتولومه ذیل همین ریشه می‌نویسد: «mit hąm ۱) aneinander befestigen, zusammenbinden, vereinigen»، و صورت‌های handarəzanti و handarəzaiiən را گواه می‌آورد. \"\n    \"چونگ نیز همین ترکیب را *ham- ـ *darz می‌نویسد و دنبالهٔ پهلوی آن (handarzēn- «پند دادن») را برمی‌شمارد. ادعای نورایی درست است.\"),\n  sources=[W+\"%D8%AF%D8%B1%D8%B2\"],\n  ref_check=[\n   {\"ref\":\"HRN:122\",\"status\":\"supports\",\"note\":\"Horn no.549 end (p.122): 'Wahrscheinlich gehört np. enderz „Rat, Ermahnung“ (phlv. andarj bezw. andarz) zu derselben Wurzel (mit Praefix ham).'\"},\n   {\"ref\":\"BQT:170\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 388 is printed p.170 by the calibration printed = leaf − 218 (checked on leaf 387 = p.169, headwords اندر، اندرآب، اندربای). The اندرز headword falls exactly here — the same leaf still shows the cross-reference 'اندروا … بروزن اندرز' — but the tesseract OCR of this leaf drops the headword and Mo'in's footnote, so the etymological note could not be read.\"}],\n  consulted=[\n   {\"src\":\"BRT\",\"where\":\"col. 687 f. (BRT.txt line 12959)\",\"stance\":\"supports\",\"note\":\"'mit hąm 1) „aneinander befestigen, zusammenbinden, vereinigen“: … handarəzanti (Konj.) … 2) „fesseln“: zasta … handarəzaiianta V. 9.49.'; also col. 1802 'j. handarəzan- Adj. „zusammenfassend, fassend, greifend“'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *darz, Middle Persian section (CHEUNG.txt line 5117 ff.)\",\"stance\":\"supports\",\"note\":\"'*MIDDLE PERSIAN: (+ *ham-) BMP hndlcyn- /handarzēn-/ “to advise”, ʾndrz “order”' — the Avestan hąm-darəz- and the Pahlavi handarz are the same compound.\"}])\n\nN(id=10, lang=\"Persian\", words=\"andarz «اندرز»\",\n  verdict=\"confirmed\",\n  derivation=(\"MP handarz [hndlcʼ] 'counsel, advice, injunction, testament' (MacKenzie p.41, Nyberg II p.90) is the \"\n    \"direct continuation of Avestan hąm-darəza-, the semantic bridge being 'that which binds' → 'binding \"\n    \"injunction' → 'counsel, testament' — which is why the Sasanian wisdom genre is called andarz. In New \"\n    \"Persian the initial h- is lost, as regularly (MP handām > اندام, MP hēnثīšn > اندیشه); Nyberg's own entry \"\n    \"ends 'MPrs ʾny̱drz (S); NP andarz'. Armenian borrowed the Middle Persian form as handerj / anderjapet \"\n    \"'chancellor', which fixes the shape of the word before the New Persian loss of h-. Mo'in tags اندرز \"\n    \"[په.] = Pahlavi.\"),\n  derivation_fa=(\"فارسی میانه handarz «پند، وصیت» دنبالهٔ مستقیم hąm-darəza- اوستایی است؛ تحول معنایی از «آنچه می‌بندد» به «حکم الزام‌آور» و سپس «پند و وصیت» رفته است \"\n    \"(از همین روست که ادبیات پندنامه‌ای ساسانی را «اندرز» می‌نامند). در فارسی نو هـ آغازین افتاده است، همان‌گونه که در «اندام» و «اندیشه»؛ \"\n    \"وام‌واژهٔ ارمنی handerj/anderjapet شکل پیشین را نگاه داشته است. معین نیز آن را [په.] می‌نامد. ادعای نورایی درست است.\"),\n  sources=[\"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2/\"],\n  ref_check=[\n   {\"ref\":\"BQT:170\",\"status\":\"partial\",\"note\":\"Same leaf as node 9 (BQT_v1 leaf 388 = printed 170): the page is the right one — it still shows 'اندروا … بروزن اندرز' — but this OCR does not render the اندرز headword or Mo'in's footnote legibly.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p.41 s.v. handarz (PHD_mackenzie.txt line 2789)\",\"stance\":\"supports\",\"note\":\"'handarz [hndlc | N andarz] advice, injunction, testament.' plus 'handarzēnidan, handarzēn- [hndlc-ytn] advise.'\"},\n   {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II, glossary s.v. handarz (line 1880)\",\"stance\":\"supports\",\"note\":\"'handarz [hndlcʼ] counsel, advice 41⁵… — Ps. hndlcy “command, law”; MPrs ʾny̱drz (S); NP andarz.'; the next entry gives Arm. lw. handerjapet.\"},\n   {\"src\":\"HUB\",\"where\":\"Persische Studien (HUB.txt lines 7714, 7923, 9128)\",\"stance\":\"supports\",\"note\":\"'andarj „Testament“ = np. andarz „Rath, Testament“' and 'anderjapet oder handerjapet = phi. andarzpat'.\"},\n   {\"src\":\"MON\",\"where\":\"Farhang-e Fārsi s.v. اندرز (abadis.ir)\",\"stance\":\"supports\",\"note\":\"'(اَ دَ ) [ په . ] (اِ. ) ۱ - پند، نصیحت . ۲ - وصیت .' — tagged Pahlavi.\"}])\n\nN(id=11, lang=\"Old Persian\", words=\"dâr; dârayat-vahu\",\n  verdict=\"confirmed\",\n  derivation=(\"Old Persian dar- 'to hold' (present dāraya-, 1sg. dārayāmiy, imperfect adāraya, sigmatic aorist adaršiy \"\n    \"'I held', DPe 8) is the direct Iranian reflex of *dʰer-. 'dārayat-vahu' is the royal name Dārayava(h)uš, \"\n    \"which Kent analyses exactly as Nourai does: 'From pAr. *dhārayat-, ptc. to root in OP dar-, + pAr. *vasu \"\n    \"“the good” … “He who holds firm the good”'. The second element vahu- 'good' is Nourai's ☞ Su 1 \"\n    \"(PIE *h₁su- / *wesu-), the same word as Avestan vohu- in Vohu Manah. Elamite da-ri-a-ma-u-iš and Akkadian \"\n    \"da-ri-ia-muš render the same name.\"),\n  derivation_fa=(\"پارسی باستان dar- «داشتن» با ستاک مضارع dāraya- (dārayāmiy «می‌دارم») بازتاب مستقیم *dʰer- است. \"\n    \"«dārayat-vahu» همان نام شاهانهٔ Dārayava(h)uš است که کنت آن را از اسم فاعل *dʰārayat- به‌علاوهٔ *vasu «نیکی» می‌داند: \"\n    \"«دارندهٔ نیکی»؛ جزء دوم همان vohu- اوستایی در «وهومن» است. ادعای نورایی درست است.\"),\n  sources=[W+\"%D8%AF%D8%A7%D8%B1%DB%8C%D9%88%D8%B4\"],\n  ref_check=[\n   {\"ref\":\"AHD:335\",\"status\":\"partial\",\"note\":\"Watkins' appendix entry dher-² (AHD_watkins1985.txt line 379) reads 'dher-2. To hold firmly, support. … 5. Old Persian dar-, to hold (whence Persian -dār, “-holder”): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.]' — exactly Nourai's Old-Persian box. The page number 335 cannot be the appendix (New College Edition pp.1505–1550), so it must point to the main A–Z of the 1975 edition, which is not to hand; the substance is confirmed.\"}],\n  consulted=[\n   {\"src\":\"KNT\",\"where\":\"Old Persian, Lexicon s.vv. dar-, Dārayavaʰu- (KNT.txt lines 5517, 5524)\",\"stance\":\"supports\",\"note\":\"'1dar- vb. “hold…” … pIE *dher-' and 'Dārayavaʰu- sb. “Darius” … From pAr. *dhārayat-, ptc. to root in OP dar- … + pAr. *vasu asn. “the good” …: “He who holds firm the good”'.\"},\n   {\"src\":\"BRT\",\"where\":\"col. 686 (1dar-)\",\"stance\":\"supports\",\"note\":\"Bartholomae's 1dar- article includes 'ap. dārayāmiy „halte“' among the forms.\"},\n   {\"src\":\"POK\",\"where\":\"IEW p.252\",\"stance\":\"supports\",\"note\":\"'ap. dārayāmiy „halte“' cited under 2. dher-.\"}])\n\nN(id=12, lang=\"Persian\", words=\"Dârîuš «داریوش»; dârâbgard «دارابگرد» (extra: دارا ، داراب)\",\n  verdict=\"plausible\",\n  derivation=(\"The content of the arrow is right, the transmission needs one caveat. OP Dārayavaʰuš gave Greek Dareios \"\n    \"and, in Iran itself, Middle Persian Dārāy / Dārā, which is why the Shāhnāma has دارا and داراب (Nourai's own \"\n    \"'extra' forms) as the inherited descendants — Mo'in's footnote in Borhān says precisely 'این نام در پهلوی \"\n    \"دارای و داراب خوانده شد'. The spelling داریوش, by contrast, is not an unbroken inheritance: it is a modern \"\n    \"learned re-borrowing of the cuneiform name, coined from Rawlinson's 1848 transcription and put into Persian \"\n    \"script in the early 20th century (Wiktionary credits Mirza Aqa Khan Kermani, 1909), replacing the Greek-based \"\n    \"داریوش/داریوس forms then current. Dārābgerd (mod. Dārāb, Fārs) is Dārāb + -gerd < MP -kart/-gird \"\n    \"'made, built' (PIE *kʷer- 'to make', Nourai's ☞ Kwer), i.e. 'the city Dārāb made'.\"),\n  derivation_fa=(\"محتوای پیوند درست است امّا یک نکته را باید افزود. Dārayavaʰuš پارسی باستان در فارسی میانه به دارای/دارا رسیده \"\n    \"و همین «دارا» و «داراب» است که در شاهنامه می‌بینیم (حاشیهٔ معین بر برهان قاطع، ص ۸۱۳، همین را می‌گوید)؛ \"\n    \"امّا صورت «داریوش» وام‌گیری دانشمندانهٔ دورهٔ معاصر است که از روی حرف‌نویسی راولینسن ساخته شده و نه میراث پیوستهٔ زبانی. \"\n    \"«دارابگرد» نیز از داراب ـ گرد (فارسی میانه -kart/-gird «ساخته‌شده») است. پس: با احتیاط پذیرفتنی است.\"),\n  sources=[W+\"%D8%AF%D8%A7%D8%B1%DB%8C%D9%88%D8%B4\"],\n  ref_check=[\n   {\"ref\":\"BQT:813\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 273 (printed 813), the داریوش footnote: 'داریوش کلمه‌ای است از پارسی باستان که در حالت فاعلی (nominativus) Dārayavauš بود، مرکب از Dāraya (دارا) ـ vau (نیکی)؛ جمعاً دارندهٔ نیکی «بارتولمه ۸۳۲»، این نام در پهلوی دارای و داراب خوانده شد' — both Nourai's Old-Persian gloss and his 'extra' forms دارا/داراب, on the cited page.\"},\n   {\"ref\":\"TZF:13\",\"status\":\"not_checked\",\"note\":\"Abolghasemi, Tārikh-e Mokhtasar-e Zabān-e Fārsi — refs_online.json records no downloadable copy (ketabnak login only).\"}],\n  consulted=[\n   {\"src\":\"KNT\",\"where\":\"Lexicon s.v. Dārayavaʰu-\",\"stance\":\"supports\",\"note\":\"'“He who holds firm the good” … Elam da-ri-a-ma-u-iš, Akk. da-ri-ja-muš, Gk. Δαρεῖος (by haplology for *Δαρειαῖος)'.\"},\n   {\"src\":\"MON\",\"where\":\"Wiktionary s.v. داریوش (learned-borrowing note)\",\"stance\":\"partial\",\"note\":\"'Learned borrowing from Old Persian Dārayavaʰuš, through an older transcription. Probably first used by Mirza Aqa Khan Kermani in 1909 … Doublet of داراب (dârâb) and دارا (dârâ)' — so the modern spelling is a revival, and دارا/داراب are the inherited forms.\"}])\n\nN(id=13, lang=\"Sogdian\", words=\"d`r\",\n  verdict=\"confirmed\",\n  derivation=(\"Sogdian δʾyr-/δār- (Nourai's 'd`r' = δʼr-), written δʾyr- in the Buddhist, Manichaean and Christian corpora, \"\n    \"is the same present stem *dāraya- as Old Persian dāraya-: Gharib's entry no.3412 glosses it '(to) have, \"\n    \"(to) possess, (to) hold, (to) keep, (to) wear' and explicitly equates it with OP dāraya-. In Sogdian the \"\n    \"Old Iranian intervocalic/initial *d- is spirantised to δ-, which the transliteration writes with a \"\n    \"δ/ḏ; the Persian and Sogdian forms are cognate, not borrowed from each other.\"),\n  derivation_fa=(\"سغدی δār- (در حرف‌نویسی نورایی d`r) همان ستاک *dāraya- ایرانی باستان است. غریب در فرهنگ سغدی \"\n    \"(مدخل ۳۴۱۲، ص ۱۳۴–۱۳۵) آن را «داشتن، دارا بودن، نگاه داشتن» معنی کرده و صریحاً با dāraya- پارسی باستان برابر نهاده است. \"\n    \"دال ایرانی باستان در سغدی به سایشی δ بدل می‌شود. ادعای نورایی درست است.\"),\n  sources=[],\n  ref_check=[\n   {\"ref\":\"SOD:135\",\"status\":\"supports\",\"note\":\"SOD_pages.txt line 13504, leaf 200 (printed ≈134–135 by the calibration printed ≈ leaf − 66): entry '3412 δʾr- B, M, S — δar (dʾr) ©OP dāraya- ©inf. -ʾy; trans. pret. aux. ⇒δryt- — (to) have, (to) possess, (to) hold, (to) keep, (to) wear. GMS 285, 877–880, 855'. Exactly the node.\"}],\n  consulted=[\n   {\"src\":\"SOD\",\"where\":\"Gharib no.3412 (printed p.134–135)\",\"stance\":\"supports\",\"note\":\"quoted above; Gharib is the only dictionary the SOURCE_MATRIX lists for Sogdian.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *dar¹, Sogdian section\",\"stance\":\"supports\",\"note\":\"Cheung's *dar¹ 'to hold, keep' article lists the Middle Iranian continuations (MMP dʾr-, BMP dʾl-, Parthian dʾr-) alongside the Sogdian δʾr-, all under PIE *dʰer-.\"}])\n\nN(id=14, lang=\"Sanskrit\", words=\"dhar; bhaga-dhara\",\n  verdict=\"plausible\",\n  derivation=(\"'dhar' is the Sanskrit root dhṛ-/dhar- 'to hold, bear, support, maintain' (pres. dhāráyati, ppp. dhṛtá-), \"\n    \"the eponymous member of PIE *dʰer- and the source of dhárma- 'law, statute' — which Pokorny equates directly \"\n    \"with Latin firmus. That half is beyond dispute. 'bhaga-dhara “holder of happiness”' is a different matter: \"\n    \"it is not a classical Sanskrit lexeme but Theodor Benfey's conjecture (Orient und Occident I 137) about the \"\n    \"origin of bahādur, reported second-hand by Hobson-Jobson 49a, by Klein s.v. bahadur and by Lokotsch no.175. \"\n    \"bhaga- 'good fortune, lot' (☞ Bhag, PIE *bʰeh₂g-) is of course real, and the compound is well-formed, but \"\n    \"no text attests it. Hence plausible rather than confirmed.\"),\n  derivation_fa=(\"«dhar» همان ریشهٔ سنسکریت dhṛ-/dhar- «داشتن، نگاه داشتن، برداشتن» است که dhárma- از آن ساخته شده و پوکورنی آن را \"\n    \"برابر firmus لاتین می‌گذارد؛ تا اینجا مطلب قطعی است. امّا bhaga-dhara «دارندهٔ بخت» واژه‌ای گواهی‌شده در متون سنسکریت نیست؛ \"\n    \"فرضیهٔ بنفی است دربارهٔ خاستگاه «بهادر» که هابسن‌جابسن، کلاین و لوکوچ از او نقل کرده‌اند. پس با احتیاط پذیرفتنی است.\"),\n  sources=[],\n  ref_check=[\n   {\"ref\":\"POK:252\",\"status\":\"supports\",\"note\":\"IEW p.252: 'Ai. dhar- „halten, tragen, stützen, erhalten, aufrecht halten“ (Präs. meist dhāráyati; … dhṛ-tá-)' and, p.253, 'ai. dhárma- (= lat. firmus) m. „Satzung, Sitte, Recht, Gesetz“'.\"}],\n  consulted=[\n   {\"src\":\"SYN\",\"where\":\"Buck 11.15 HOLD (SYN.txt line 18918, 18943)\",\"stance\":\"supports\",\"note\":\"'Skt. dhṛ-, Av. dar-, drag-, hap-' listed as the Indo-Iranian words for 'hold'.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann s.v. dher- (2) (IEC.txt line 2808)\",\"stance\":\"supports\",\"note\":\"'dher- (2) “hard, fast, firm” … Skt. cf. dharayami “hold, bear, wear…”; Av. dar- “hold, get”; OPer dar-, id.'\"},\n   {\"src\":\"HJB\",\"where\":\"s.v. BAHAUDUR, p.49 (HJB.txt line 2510)\",\"stance\":\"partial\",\"note\":\"'Benfey has suggested that the word originated in Skt. bhaga-dhara (“happiness-possessing”).' — i.e. a suggestion, not an attested word, and Hobson-Jobson goes on to report Schiefner's rival derivation.\"}])\n\nN(id=15, lang=\"Hindustani\", words=\"bahaudur\",\n  verdict=\"disputed\",\n  derivation=(\"The direction of this arrow is the reverse of what the sources say. Hindi/Urdu बहादुर / بہادر bahādur \"\n    \"is a Turco-Mongol loanword that entered India with the Delhi Sultanate and the Mughals, and 'bahaudur' \"\n    \"(bahawder, behadoor) is merely the 18th–19th-c. Anglo-Indian spelling of it. Lokotsch no.175 states the \"\n    \"route explicitly: 'Über hind. bahādur „Held, Vorkämpfer“ entstand angloind. bahaudur, bahawder, behadoor, \"\n    \"frz. béhadour'. Hobson-Jobson, on the page Nourai cites, opens 'Bahādur is one of the terms which the \"\n    \"hosts of Chingiz Khan brought with them from the Mongol Steppes'. Benfey's Sanskrit bhaga-dhara etymology \"\n    \"is reported by both, but neither adopts it, and it fails phonetically anyway (Skt. bh- would not give \"\n    \"Mongol/Turkic b-γ-, and the -γ- of baγatur has no Sanskrit source). A Sanskrit → Hindustani arrow is \"\n    \"therefore rejected by modern scholarship.\"),\n  derivation_fa=(\"جهت این پیکان وارونه است. واژهٔ هندی/اردوی bahādur وام‌واژه‌ای ترکی–مغولی است که با حکومت‌های ترک و مغول به هند رفته، \"\n    \"و صورت bahaudur فقط املای انگلوهندی همان است. لوکوچ (شمارهٔ ۱۷۵) می‌نویسد که صورت انگلوهندی از هندی پدید آمده، و هابسن‌جابسن \"\n    \"می‌گوید که این واژه را لشکریان چنگیزخان از دشت مغولستان آوردند. فرضیهٔ سنسکریتی بنفی را هیچ‌کدام نپذیرفته‌اند. پژوهش امروزی این پیوند را رد می‌کند.\"),\n  sources=[W+\"%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\"],\n  ref_check=[\n   {\"ref\":\"HJB:49\",\"status\":\"partial\",\"note\":\"HJB.txt line 2504 ff. (leaf 100; Klein cites the same passage as 'Hobson-Jobson 49a'): 'BAHAUDUR, s. H. Bahādur, “a hero, or champion” … Bahādur is one of the terms which the hosts of Chingiz Khan brought with them from the Mongol Steppes … Benfey has suggested that the word originated in Skt. bhaga-dhara … But the late lamented Prof. A. Schiefner … was strongly of opinion that the word was rather a corruption … of the Zend bagha-puthra “Son of God”.' The page carries Benfey's idea but frames the word as a Mongol import.\"},\n   {\"ref\":\"KLN:140\",\"status\":\"partial\",\"note\":\"KLN_1966.txt line 4285 (p.140): 'bahadur, n., a title given to European officers in India. — Hind. bahādur, “hero”, which according to Benfey (in Orient und Occident 1 137, quoted in Hobson-Jobson 49a) derives fr. OI. bhaga-dhara-, “happiness-possessing”.' Klein reports the derivation as Benfey's, with attribution, and does not endorse it.\"}],\n  consulted=[\n   {\"src\":\"LKT\",\"where\":\"Lokotsch no.175 'Pers. bāhādur' (LKT.txt line 615)\",\"stance\":\"contradicts\",\"note\":\"'vgl. mongol. bagatur, batur, woraus ung. bátor „kühn“ wurde; ebenso tk. bahadyr „Held“; hieraus russ. bogatyr’ … Über hind. bahādur „Held, Vorkämpfer“ entstand angloind. bahaudur, bahawder, behadoor, frz. béhadour … [Benfey … führt das Wort auf sskr. bhaga-dhara „glückbringend“ zurück.]' — Lokotsch files the word as Persian/Mongol and derives the Anglo-Indian form FROM Hindi, not Hindi from Sanskrit.\"},\n   {\"src\":\"AID\",\"where\":\"Whitworth, An Anglo-Indian Dictionary (AID.txt)\",\"stance\":\"silent\",\"note\":\"grep 'bahadur' returns only the personal name 'Tegh Bahādur' s.v. Rām Rāi; Whitworth has no headword for the title.\"},\n   {\"src\":\"HJB\",\"where\":\"p.49\",\"stance\":\"contradicts\",\"note\":\"the Mongol-Steppes sentence quoted above, plus the list of cognates (Manchu baturu, Kirghiz batyr, Turki bâtur, Russian bogatyr) — an Inner-Asian, not an Indic, word.\"}])\n\nN(id=16, lang=\"Mongolian\", words=\"bahâdŭr\",\n  verdict=\"disputed\",\n  derivation=(\"Mongolian baγatur (modern baatar, as in Ulaanbaatar) is the source of the whole family, not a borrowing \"\n    \"from Hindustani. It is attested in the Secret History of the Mongols and in 12th–13th-c. names such as \"\n    \"Yesugei Baγatur, Chinggis Khan's father, and Subötei Baγatur; the older Turkic baγatur is attested \"\n    \"centuries earlier still (Danube-Bulgar and Old Turkic inscriptions). From it come Russian богатырь, \"\n    \"Polish bohatyr, Hungarian bátor, Manchu baturu (Chinese pa-tu-lu), Turkish bahadır, Persian بهادر and \"\n    \"Hindi/Urdu bahādur. Nourai's arrow Hindustani → Mongolian inverts the attested chronology by roughly a \"\n    \"millennium; his form 'bahādūr' is itself the Persianised spelling, not the Mongol one.\"),\n  derivation_fa=(\"مغولی baγatur (امروز baatar، در «اولان‌باتار») سرچشمهٔ همهٔ صورت‌هاست و وام‌گرفته از هندی نیست؛ \"\n    \"در تاریخ سرّی مغولان و در نام‌هایی مانند یسوگای بهادر و سوبتای بهادر گواهی شده است، و صورت ترکی باستان آن قدیمی‌تر هم هست. \"\n    \"از همین ریشه روسی بوگاتیر، مجاری bátor، مانچوری baturu و فارسی «بهادر» آمده است. پس پیکان «هندی ← مغولی» در نمودار وارونه است و رد می‌شود.\"),\n  sources=[W+\"%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\"],\n  ref_check=[\n   {\"ref\":\"HJB\",\"status\":\"contradicts\",\"note\":\"HJB p.49 (HJB.txt line 2510): 'Bahādur is one of the terms which the hosts of Chingiz Khan brought with them from the Mongol Steppes. In the Mongol genealogies we find Yesugai Bahadur, the father of Chingiz, and many more. Subutai Bahādur … In Sanang Setzen's poetical annals of the Mongols … the word is written Baghatur, whence in Russian Bogatyr still survives … In Turki also this elision of the guttural extends to the spelling, and the word becomes Bâtur.' Nourai cites this very page, which says the opposite of his arrow.\"}],\n  consulted=[\n   {\"src\":\"LKT\",\"where\":\"Lokotsch no.175\",\"stance\":\"contradicts\",\"note\":\"'vgl. mongol. bagatur, batur, woraus ung. bátor „kühn“ wurde' — Mongol is the donor throughout.\"},\n   {\"src\":\"TTS\",\"where\":\"Vámbéry, Etym. Wb. der turko-tatarischen Sprachen (TTS_vambery1878_uoft_djvu.txt)\",\"stance\":\"silent\",\"note\":\"grep for bagatur / baghatur / batur / bahadir in the OCR returns nothing usable; the scan is too poor to confirm Vámbéry's entry, which Hobson-Jobson cites for Turki Bâtur.\"}])\n\nN(id=17, lang=\"Persian\", words=\"bahâdor «بهادر»\",\n  verdict=\"confirmed\",\n  derivation=(\"Persian بهادر 'brave, champion' is a Middle Mongol loan taken during and after the Ilkhanid conquest \"\n    \"(attested in Persian historiography from the 13th c. — Juvayni, Rashid al-Din — exactly when Wiktionary \"\n    \"dates it, 'attested after the Mongol conquest in the 1200s'). Mongol baγatur lost its intervocalic velar in \"\n    \"Persian pronunciation, and the Persian spelling writes the resulting hiatus with هـ: baγatur → bahādur; the \"\n    \"same word was later exported from Persian/Turkish to Russian and to India. Mo'in's Farhang-e Fārsi tags the \"\n    \"entry [تر.] i.e. Turkish. So the arrow Mongolian → Persian is correct, even though its parent nodes (15–16) \"\n    \"are not.\"),\n  derivation_fa=(\"«بهادر» وام‌واژه‌ای مغولی است که در دورهٔ ایلخانان (سدهٔ هفتم قمری) وارد فارسی شده و در جهان‌گشای جوینی و جامع التواریخ دیده می‌شود. \"\n    \"گاف میانی baγatur در تلفّظ فارسی افتاده و خلأ حاصل را با «ه» نوشته‌اند: baγatur ← bahādur. معین نیز آن را [تر.] می‌نامد. \"\n    \"پس این پیکان (مغولی ← فارسی) درست است، هرچند دو گرهٔ پیش از آن نادرست‌اند.\"),\n  sources=[W+\"%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\", \"https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/\"],\n  ref_check=[\n   {\"ref\":\"HJB:49\",\"status\":\"supports\",\"note\":\"the same Hobson-Jobson page gives the Persian use ('while in Persia it was often applied to slaves (Burton, Ar. Nights, iii.114)') and traces the word from the Mongol steppes into Persian and Indian usage — which is the arrow drawn here.\"},\n   {\"ref\":\"BQT\",\"status\":\"not_checked\",\"note\":\"Nourai gives no page for BQT here; بهادر falls in Borhān vol.1 (ب section) and could not be located without a page number in this OCR.\"},\n   {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Fārsi s.v. بهادر (abadis.ir): '(بَ دُ ) [ تر . ] (ص . ) دلیر، دلاور، شجاع .' — Mo'in marks it a Turkic loan, i.e. not a Persian inheritance and not from Sanskrit.\"}],\n  consulted=[\n   {\"src\":\"MON\",\"where\":\"s.v. بهادر (abadis.ir)\",\"stance\":\"supports\",\"note\":\"'[ تر . ] (ص . ) دلیر، دلاور، شجاع' — tagged Turkic.\"},\n   {\"src\":\"LKT\",\"where\":\"Lokotsch no.175, headword 'Pers. bāhādur'\",\"stance\":\"supports\",\"note\":\"Lokotsch enters the word under Persian and derives it from Mongol bagatur, with Turkish bahadyr beside it.\"},\n   {\"src\":\"HJB\",\"where\":\"p.49\",\"stance\":\"supports\",\"note\":\"the Chingizid transmission narrative quoted at node 16 covers the Persian branch as well.\"}])\n\nN(id=18, lang=\"Latin\", words=\"firmus\",\n  verdict=\"confirmed\",\n  derivation=(\"Latin firmus 'firm, strong, steadfast' is the classic *dʰer-mo- formation: Italic *f- is the regular \"\n    \"outcome of PIE word-initial *dʰ-, and Pokorny states the equation outright on p.253, 'ai. dhárma- \"\n    \"(= lat. firmus) m. „Satzung, Sitte, Recht, Gesetz“' — the Latin adjective and the Sanskrit noun are the same \"\n    \"stem with different vowel treatment (Lat. i < *e before r + labial). Watkins likewise: 'Suffixed form \"\n    \"*dher-mo- in Latin firmus'. Note that Latin fortis 'strong' is NOT securely from this root: Watkins and \"\n    \"Pokorny both leave it hanging between *dhergh- and *bhergh-, so Nourai is right to keep it off the chart.\"),\n  derivation_fa=(\"لاتین firmus «استوار، محکم» همان ساخت *dʰer-mo- است؛ دال دمیدهٔ هندواروپایی در آغاز واژه در ایتالیایی به f بدل می‌شود. \"\n    \"پوکورنی در ص ۲۵۳ صریحاً می‌نویسد «ai. dhárma- (= lat. firmus)»، یعنی همان ستاک سنسکریت است. واتکینز نیز همین را می‌گوید. ادعای نورایی درست است.\"),\n  sources=[\"https://www.etymonline.com/word/farm\"],\n  ref_check=[\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 379: 'dher-2. To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIRMARY).'\"}],\n  consulted=[\n   {\"src\":\"POK\",\"where\":\"IEW p.253\",\"stance\":\"supports\",\"note\":\"'ai. dhárma- (= lat. firmus) m. „Satzung, Sitte, Recht, Gesetz“'.\"},\n   {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. firmus (LAT.txt line 22638)\",\"stance\":\"supports\",\"note\":\"the firmus article ('firmus, -a, -um …') stands in the dictionary with the -firm- family (infirmus, firmare); the OCR of the etymological paragraph is broken but the headword and family are there.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck (SYN.txt line 7664)\",\"stance\":\"supports\",\"note\":\"'Lat. infirmus, neg. of firmus “fast, solid, firm, strong” : Skt. dhr-, Av. dar- “hold, support”, etc. Walde-P. 1.859.'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 856 ff.\",\"stance\":\"supports\",\"note\":\"the dher-2 article, on which Buck's reference 'Walde-P. 1.859' rests.\"}])\n\nN(id=19, lang=\"English\", words=\"firm, farm, confirm\",\n  verdict=\"confirmed\",\n  derivation=(\"All three reach English from Latin firmus through French. firm (adj.), late 14c. ferme, from Old French \"\n    \"ferme < L. firmus. confirm, c.1300, from OF confermer < L. confirmāre 'to make firm' (con- + firmāre). \"\n    \"farm is the semantically interesting one: c.1300 'fixed payment, fixed rent', from OF ferme 'a rent, lease' \"\n    \"< Medieval Latin firma 'fixed payment' < L. firmāre 'to fix, settle'; the sense 'to rent land' is mid-15c. \"\n    \"and the agricultural sense only 1719 — so 'farm' is a legal-fiscal word that became agrarian, not a word for \"\n    \"cultivation that acquired a rent sense. Nourai's grouping of the three is exactly Watkins' list under \"\n    \"dher-².\"),\n  derivation_fa=(\"هر سه واژه از راه فرانسه از لاتین firmus به انگلیسی رسیده‌اند: firm از فرانسهٔ کهن ferme، confirm از لاتین confirmāre. \"\n    \"نکتهٔ جالب farm است که در حدود ۱۳۰۰ میلادی به معنی «اجارهٔ مقطوع» بوده (از لاتین میانه firma «پرداخت ثابت») و معنی کشاورزی آن تازه در ۱۷۱۹ پدید آمده است. \"\n    \"ادعای نورایی درست است.\"),\n  sources=[\"https://www.etymonline.com/word/farm\"],\n  ref_check=[\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins dher-² lists FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM under *dher-mo- > Latin firmus (AHD_watkins1985.txt line 379); the index entries 'FARM dher-2', 'FIRM dher-2', 'CONFIRM dher-2' repeat it.\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein s.vv. farm, confirm (KLN_1966.txt lines 14393, 8671)\",\"stance\":\"supports\",\"note\":\"'farm, n. — ME. ferme, “rent, lease”, fr. MF. ferme, “lease”, fr. ML. firma, “fixed payment”, fr. L. firmare … fr. firmus'; 'confirm, tr. v. — OF. confermer … fr. L. confirmare, “to make firm” … fr. firmus'.\"},\n   {\"src\":\"Etymonline\",\"where\":\"etymonline.com/word/farm\",\"stance\":\"supports\",\"note\":\"'farm (n.) c.1300, “fixed payment … fixed rent”, from Old French ferme “a rent, lease” (13c.), from Medieval Latin firma “fixed payment”, from Latin firmare … from firmus “strong; stable” … (from suffixed form of PIE root *dher- “to hold firmly, support”). … The agricultural sense is from 1719.'\"}])\n\nN(id=20, lang=\"Greek\", words=\"thornus\",\n  verdict=\"transcription_suspect\",\n  error_in=\"book\",\n  book_prints=\"thornus\",\n  correct_form=\"thronos (Gk. θρόνος; Latin thronus)\",\n  derivation=(\"There is no Greek word *thornus. The word meant is θρόνος thrónos 'elevated seat, chair, throne' \"\n    \"(Homeric, Odyssey passim), whose Latin borrowing thronus is what gives English throne; the gloss 'support, \"\n    \"seat' Nourai prints is right for thrónos. The printed page (book p.98, PDF 128 — the PNG is filed at \"\n    \"data/verification/sources/refs/ocr/BOOK/128.png) really does read 'thornus : support, seat', so this is \"\n    \"Nourai's own misprint — a metathesis of -ron- to -orn- crossed with the Latin ending -us — and the \"\n    \"extraction is faithful. On the etymology itself: Watkins, Klein and Etymonline derive thrónos from a \"\n    \"suffixed zero grade *dʰr̥-ono- of *dʰer- ('a support'), with Gk. thrânos 'bench' and thrênūs 'footstool' \"\n    \"beside it; Beekes treats the group as of uncertain, possibly Pre-Greek origin, so the root link is \"\n    \"traditional rather than universally accepted.\"),\n  derivation_fa=(\"واژه‌ای به صورت *thornus در یونانی وجود ندارد؛ مقصود همان θρόνος (thrónos) «تخت، کرسی بلند» است که از هومر به بعد گواهی شده \"\n    \"و صورت لاتینی آن (thronus) سرچشمهٔ throne انگلیسی است. در صفحهٔ چاپی کتاب (ص ۹۸) هم همین «thornus» آمده؛ پس خطای چاپی خود کتاب است \"\n    \"(قلب -ron- به -orn-) و خوانش اسکن درست بوده است. دربارهٔ خود ریشه، واتکینز و کلاین thrónos را از *dʰr̥-ono- می‌گیرند، ولی بیکس آن را احتمالاً پیشایونانی می‌داند.\"),\n  sources=[\"https://www.etymonline.com/word/throne\"],\n  ref_check=[\n   {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 379, dher-²: '3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE.' — Watkins gives the word Nourai meant, spelled correctly.\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein s.v. throne (KLN_1966.txt line 39149)\",\"stance\":\"supports\",\"note\":\"'throne, n. — ME., fr. earlier trone, fr. OF. trone, fr. L. thronus, fr. Gk. θρόνος, “seat, chair, throne”, fr. I.-E. base *dher(e)-, “to hold, support”, whence also Gk. θρᾶνος, “bench”, θρῆνυς, “footstool”, OI. dhāráyati … L. firmus.' No form 'thornus' in Klein.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck (SYN.txt line 12102)\",\"stance\":\"supports\",\"note\":\"'“footstool”, fr. the root *dher- in Skt. dhr- “hold, support”, etc. (11.15). Walde-P. 1.857.'\"},\n   {\"src\":\"BOOK\",\"where\":\"printed page 98 = PDF 128 (image at data/verification/sources/refs/ocr/BOOK/128.png)\",\"stance\":\"supports\",\"note\":\"the Greek box on the page reads 'thornus : support, seat' — confirming the JSON is a faithful extraction and the error is the author's.\"}])\n\nN(id=21, lang=\"English\", words=\"throne\",\n  verdict=\"confirmed\",\n  derivation=(\"English throne is a straight Greek→Latin→French→English chain: Gk. thrónos → L. thronus (Medieval \"\n    \"Latin tronus) → Old French trone (12c.) → Middle English trone, c.1200 'the seat of God or a saint in \"\n    \"heaven', c.1300 'seat occupied by a sovereign'; the classical -h- was restored in the English spelling from \"\n    \"the late 14c. under Latin influence. The figurative sense 'royal power' is late 14c. The node's link to its \"\n    \"Greek parent is therefore sound even though the parent's form is misprinted.\"),\n  derivation_fa=(\"throne انگلیسی از یونانی thrónos از راه لاتین thronus و فرانسهٔ کهن trone به انگلیسی میانه (حدود ۱۲۰۰ م.) رسیده \"\n    \"و نخست به معنی «تخت خداوند یا قدیسان در آسمان» بوده است؛ حـ کلاسیک در املای انگلیسی از اواخر سدهٔ چهاردهم بازگردانده شده است. ادعای نورایی درست است.\"),\n  sources=[\"https://www.etymonline.com/word/throne\"],\n  ref_check=[\n   {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives this node no reference at all (the box is empty in the printed chart); it inherits the AHD citation of its Greek parent, which does list THRONE under dher-².\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"Klein s.v. throne\",\"stance\":\"supports\",\"note\":\"'throne, n. — ME., fr. earlier trone, fr. OF. trone (F. trône), fr. L. thronus, fr. Gk. θρόνος…'\"},\n   {\"src\":\"Etymonline\",\"where\":\"etymonline.com/word/throne\",\"stance\":\"supports\",\"note\":\"'c.1200, trone, “the seat of God or a saint in heaven;” c.1300, “seat occupied by a sovereign…” from Old French trone (12c.…), from Latin thronus (Medieval Latin tronus), from Greek thronos “elevated seat, chair, throne” … The classical -h- begins to appear in English from late 14c.'\"}])\n\nentry = {\n \"entry\": 0,\n \"root\": \"Dher 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰer- 'to hold firmly, support' (Pokorny IEW 252 '2. dher-, dherə-'; Watkins/AHD dher-²)\",\n \"note\": (\"Pokorny's IEW p.252 heads the entry '2. dher-, dherə- „halten, festhalten, stützen“' and Watkins prints \"\n  \"'dher-2. To hold firmly, support', so the root box — name, language label and gloss — is exactly right, and \"\n  \"the numbering 'Dher 1' is Nourai's own (he separates it from the other dher- homophones, which is what Pokorny \"\n  \"does too). The chart is unusually well sourced: Pokorny's own page 258 prints Nourai's four darz words verbatim, \"\n  \"Kent's lexicon prints his analysis of Dārayavaʰuš verbatim, MacKenzie and Nyberg print his pad-ēn-dāštan > \"\n  \"pindāštan verbatim, and Gharib's Sogdian entry is on the page he cites. Three weak spots: (a) dārū 'medicine' \"\n  \"(node 4) belongs to *dóru 'wood', as Nourai's own NOTE concedes; (b) the Avestan zaenō-hara of node 5 is an \"\n  \"unattested reconstruction whose second element goes back to *ser-, not *dʰer-; (c) the bahādur chain \"\n  \"(nodes 14–17) is drawn backwards — the word is Mongol/Turkic and travelled INTO Persian and Hindustani, and \"\n  \"the Sanskrit bhaga-dhara etymology is only Benfey's conjecture, which Nourai's own sources report but do not \"\n  \"adopt. One printing error: the Greek box (node 20) reads 'thornus' for thrónos.\"),\n \"note_fa\": (\"جعبهٔ ریشه درست است: هندواروپایی آغازین *dʰer- «نگاه داشتن، پشتیبانی کردن» که پوکورنی در صفحهٔ ۲۵۲ با معنی آلمانی \"\n  \"«halten, festhalten, stützen» آورده و واتکینز نیز همین را ثبت کرده است. مستندات این نمودار به‌طور غیرمعمول دقیق است: \"\n  \"چهار واژهٔ درز/درزی/درزمان/درزن عیناً در صفحهٔ ۲۵۸ پوکورنی، تحلیل «دارندهٔ نیکی» برای داریوش در واژه‌نامهٔ کنت، \"\n  \"و pad ēn dāštan > پنداشتن در مکنزی و نیبرگ آمده است. سه نقطهٔ سست دارد: یکم «دارو» که از ریشهٔ *dóru «چوب» است نه از این ریشه \"\n  \"(خود نورایی هم در یادداشت اشاره کرده)؛ دوم صورت اوستایی zaenō-hara که گواهی نشده و جزء دوم آن به *ser- می‌رسد؛ سوم زنجیرهٔ «بهادر» \"\n  \"که وارونه رسم شده است: این واژه مغولی–ترکی است و از آنجا به فارسی و هندی رفته، نه برعکس. همچنین یک خطای چاپی: جعبهٔ یونانی \"\n  \"«thornus» دارد که باید thrónos باشد.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0er-\"],\n \"ref_check\": [\n   {\"ref\":\"POK:252\",\"status\":\"supports\",\"note\":\"POK_01.txt line 3592 (IEW p.252, the page marker '253' follows a few lines later): '2. dher-, dherə- „halten, festhalten, stützen“. Ai. dhar- „halten, tragen, stützen…“, av. dar- „halten, festhalten, zurückhalten…“ (dārayeiti usw., Partiz. darəta-), ap. dārayāmiy „halte“, npers. Inf. dāštan, osset. Inf. darun…'. Root, language and gloss all as charted.\"}],\n \"consulted\": [\n   {\"src\":\"WLD\",\"where\":\"Walde-Pokorny Bd. I 856 ff. (WLD_Bd1 djvu line 53991; page header '856' at leaf 864)\",\"stance\":\"supports\",\"note\":\"'2. dher- (dherē-) „halten, festhalten, stützen“. Ai. dhar- „halten, tragen, stutzen, erhalten, aufrecht halten“…' — the article Pokorny 252 abridges.\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985, dher-² (AHD_watkins1985.txt line 379)\",\"stance\":\"supports\",\"note\":\"'dher-2. To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus… 3. Suffixed zero-grade form *dhr-ono- in Greek thronos… 4. Suffixed form *dher-mn in Sanskrit dharma… 5. Old Persian dar-, to hold (whence Persian -dār, “-holder”)… [Pok. 2. dher- 252.]' — four of Nourai's branches in one paragraph.\"},\n   {\"src\":\"IEC\",\"where\":\"Mann, dher- (2) (IEC.txt line 2808)\",\"stance\":\"supports\",\"note\":\"'dher- (2) “hard, fast, firm”… Skt. cf. dharayami; Av. dar- “hold, get”; OPer dar-, id.; Per. (ambig.) dāram “have”… Lat. cf. fer-tim'.\"},\n   {\"src\":\"SYN\",\"where\":\"Buck 11.15 HOLD (SYN.txt line 18918)\",\"stance\":\"supports\",\"note\":\"the comparative table for 'hold' gives 'Skt. dhṛ-, Av. dar-, drag-, hap-', with Walde-P. 1.857/859 as the reference — i.e. the same root.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"s.v. *dar¹ (CHEUNG.txt line 4873)\",\"stance\":\"supports\",\"note\":\"'«PIE *dʰer- “to hold” > LIV: 145 f. | Pok.: 252 ff.» — IE COGNATES: Hitt. /dar-/, Lat. firmus “firm, steady”, Lith. derū'.\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 128,\n \"book_page\": 98,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-128.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build128.py",
 "description": "Build page-128.json"
}
```


### [2026-09-05T20:29:38.331Z] TOOL RESULT

```
written 21 nodes
```


## [2026-09-05T20:29:43.769Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-128.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 128",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:29:45.852Z] TOOL RESULT

```
JSON OK
nodes verified: 21/21
node verdicts: {'confirmed': 13, 'disputed': 4, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 20, 'partial': 8, 'not_checked': 5, 'contradicts': 1}
books consulted: {'supports': 44, 'partial': 7, 'contradicts': 5, 'silent': 3} | by book: {'BRT': 5, 'CHEUNG': 5, 'PHD': 5, 'HUB': 5, 'MON': 5, 'KNT': 3, 'POK': 3, 'SYN': 3, 'HJB': 3, 'LKT': 3, 'KLN': 3, 'NYB': 2, 'IEC': 2, 'WLD': 2, 'Etymonline': 2, 'BQT': 1, 'HRN': 1, 'ARY': 1, 'SOD': 1, 'AID': 1, 'TTS': 1, 'LAT': 1, 'BOOK': 1}
```


## [2026-09-05T20:29:48.940Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "Check archived sources"
}
```


### [2026-09-05T20:29:51.450Z] TOOL RESULT

```
1198 cited URLs, 5 not yet archived
archived 5, failed 0
```


## [2026-09-05T20:29:54.388Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 tools/verify_check.py 128 2>&1 | grep -i problem; echo \"exit=$?\"; git -C /home/sfmqrb/git/rishe status --short | head -20",
 "description": "Confirm no problems and show changed files"
}
```


### [2026-09-05T20:29:56.092Z] TOOL RESULT

```
exit=1
 M data/verification/sources/web/index.jsonl
?? data/verification/page-128.json
?? data/verification/page-140.json
?? data/verification/page-142.json
?? data/verification/sources/web/5a036997824f6860.txt
?? data/verification/sources/web/755d52e7e3ce9ed8.txt
```


## [2026-09-05T20:30:03.308Z] TOOL CALL #90: Bash

```json
{
 "command": "cat .gitignore 2>/dev/null | head -20; echo \"---\"; git check-ignore -v data/verification/sources/web/ac0bd876cb6e2258.txt data/verification/sources/refs/ocr/BOOK/128.png 2>&1 | head",
 "description": "Check gitignore status"
}
```


### [2026-09-05T20:30:05.113Z] TOOL RESULT

```
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
---
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/128.png
```


## [2026-09-05T20:30:10.291Z] TOOL CALL #91: Bash

```json
{
 "command": "git -C /home/sfmqrb/git/rishe status --short data/verification/sources/web | head -30; echo \"---count untracked---\"; git -C /home/sfmqrb/git/rishe status --short data/verification/sources/web | wc -l; ls -la data/verification/sources/web/ac0bd876cb6e2258.txt data/verification/sources/refs/ocr/BOOK/128.png",
 "description": "Check web archive git status"
}
```


### [2026-09-05T20:30:12.005Z] TOOL RESULT

```
---count untracked---
0
-rw-rw-r-- 1 sfmqrb sfmqrb 83553 Sep  5 16:14 data/verification/sources/refs/ocr/BOOK/128.png
-rw-rw-r-- 1 sfmqrb sfmqrb  7451 Sep  5 16:06 data/verification/sources/web/ac0bd876cb6e2258.txt
```


## [2026-09-05T20:30:18.145Z] TOOL CALL #92: Bash

```json
{
 "command": "git status --short | head; echo \"--- ignore check ---\"; git check-ignore -v data/verification/sources/web/ac0bd876cb6e2258.txt; ls data/verification/sources/web/.gitignore 2>/dev/null && cat data/verification/sources/web/.gitignore",
 "description": "Recheck git status"
}
```


### [2026-09-05T20:30:19.867Z] TOOL RESULT

```
Exit code 2
?? data/verification/page-143.json
--- ignore check ---
```


## [2026-09-05T20:30:24.440Z] TOOL CALL #93: Bash

```json
{
 "command": "ls -la data/verification/page-128.json; git log --oneline -5; git log --oneline -3 -- data/verification/page-128.json",
 "description": "Check file and recent commits"
}
```


### [2026-09-05T20:30:24.539Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72640 Sep  5 16:29 data/verification/page-128.json
c9f1149 Verify page 136 (Dhus/fusus, Dhwer/dar, thyroid)
1b394e1 Verify pages 139 (Do 2/dadan, hushyar; Dolmak/dolmeh) and 141 (Dipi/dabir, divan, adab)
72ab166 Verify pages 135 (Dhragh/dorushkeh, Dhreugh/dorugh) and 144 (D.v.r/arsenal, Dwei/bish)
42db6b4 Verify page 131 (Dheu 3/andudan, Dheugh/dukhtar, dushizeh)
3368203 Verify pages 130 (Dheu 2/dud, anduh, tufan) and 133 (Dhis/deh)
c9f1149 Verify page 136 (Dhus/fusus, Dhwer/dar, thyroid)
```


## [2026-09-05T20:30:31.218Z] TOOL CALL #94: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-128.json'))\ne=d['entries'][0]\nprint(d['pdf_page'], d['book_page'], e['root'], len(e['nodes']))\nprint(e['nodes'][19]['verdict'], e['nodes'][19].get('book_prints'))\n\"; python3 tools/verify_check.py 128",
 "description": "Final sanity check"
}
```


### [2026-09-05T20:30:33.011Z] TOOL RESULT

```
128 98 Dher 1 21
transcription_suspect thornus
nodes verified: 21/21
node verdicts: {'confirmed': 13, 'disputed': 4, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 20, 'partial': 8, 'not_checked': 5, 'contradicts': 1}
books consulted: {'supports': 44, 'partial': 7, 'contradicts': 5, 'silent': 3} | by book: {'BRT': 5, 'CHEUNG': 5, 'PHD': 5, 'HUB': 5, 'MON': 5, 'KNT': 3, 'POK': 3, 'SYN': 3, 'HJB': 3, 'LKT': 3, 'KLN': 3, 'NYB': 2, 'IEC': 2, 'WLD': 2, 'Etymonline': 2, 'BQT': 1, 'HRN': 1, 'ARY': 1, 'SOD': 1, 'AID': 1, 'TTS': 1, 'LAT': 1, 'BOOK': 1}
```


## [2026-09-05T20:30:52.455Z] AGENT

Page 128 (book p. 98), one entry: **Dher 1** = PIE \*dʰer- "to hold firmly, support" — root **confirmed** (Pokorny IEW 252, Watkins dher-²).

**Verdicts:** 21/21 nodes — confirmed 13, disputed 4, plausible 3, transcription_suspect 1. `verify_check.py 128` reports 0 PROBLEM lines. File: `/home/sfmqrb/git/rishe/data/verification/page-128.json`.

**Disputed**
- #4 Persian دارو *dārū* "medicine" — belongs to PIE \*dóru "wood" (MP dārūg < PIr \*dāru-ka-, cf. Parth. dālūg, Skt dāru), not \*dʰer-; Nourai's own NOTE (ETM:65 → Deru 1) concedes it, and Mo'in's Borhān footnote says "اصل آن مشکوک است". (darmān alone would be confirmed.)
- #5 Avestan *zaenô-hara* — not attested in Bartholomae; it is Hübschmann's reconstruction quoted by Mo'in. Second element is hār- "to guard" < PIE \*ser-, so the arrow from Av./OP dār- fails phonetically. Horn (p.117) attaches zīnhār to dāštan only tentatively, with his own metrical objection.
- #15 Hindustani *bahaudur* ← Sanskrit — reversed: Hindi bahādur is a Turco-Mongol loan; "bahaudur" is the Anglo-Indian spelling (Lokotsch 175 states it explicitly). Benfey's Skt bhaga-dhara is reported by HJB/Klein but adopted by neither.
- #16 Mongolian ← Hindustani — inverted by ~a millennium; Mongol baγatur is the source (Secret History, Yesügei Baγatur), whence Russian богатырь, Hung. bátor, Pers. بهادر.

**Transcription suspect**
- #20 Greek "thornus" — `error_in: book`. The printed page really reads *thornus*; Nourai's misprint for θρόνος *thrónos* (Latin thronus). Extraction is faithful. Page PNG filed at `data/verification/sources/refs/ocr/BOOK/128.png`.

**No extraction errors found** — the JSON matches the printed chart throughout (checked against `site/pages/128.jpg`).

Notable positive findings: Pokorny p.258 prints Nourai's four darz words verbatim ("Npers. darz, darza 'Naht', darzmān, darznān 'Faden', darzan 'Nadel'; pehl. darzīk 'Schneider'"); Kent's lexicon gives Dārayavaʰu- as "He who holds firm the good", exactly node 11/12; MacKenzie and Nyberg both print *pad ēn dāštan* > NP *pindāštan*; FFD pp. 43 and 52 are precisely the پنداشتن and داشتن entries Nourai cites; Gharib no. 3412 δʾr- sits on the cited p. 135. Not checkable: CEL3:254, ETM:65, TZF:13, MON:1510 (no digitised copy / no print pagination online).
