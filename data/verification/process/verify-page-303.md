# Verification process log — verify-page-303


## [2026-09-06T22:52:13.660Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 303 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-303.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-303.json. Write /home/sfmqrb/git/rishe/data/verification/page-303.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 303` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:52:15.419Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:52:16.025Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:52:16.040Z] TOOL RESULT

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


## [2026-09-06T22:52:16.174Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-303.txt"
}
```


### [2026-09-06T22:52:16.186Z] TOOL RESULT

```
1	=== PDF page 303 (book page 273) ===
2	--- entry 0 ---
3	ROOT [Semitic / Syriac] Layh, A.l.h : Layh: to be high; A.l.h: to worship  (refs KLN:505; FVQ:66; VDQ:125)  PART 1
4	#1 (parent #0) [Hebrew] refs=KLN:505,510 | Eloh, Elohim, Ěl : God
5	  #2 (parent #1) [English] refs=KLN:505,510 | Elohim, El : God
6	  #3 (parent #1) [Hebrew] refs=KLN:138,505; AHD:94 | Bâbh-ěl : "gate to God", Babel, Babylonia ☞N.b.b ; Gebher-ěl : "man of God", Gabriel ☞J.b.r ; Yîšmâ-ěl : "God hears", Ishmael ☞S.m.`a ; Mîxâ-ěl : "who is like God ?", Michael ; Yisrâ-ěl : "soldier of God", Israel ; Azra`-ěl : "God has helped", Azrael
7	    #4 (parent #3) [Arabic] refs=FVQ | - el, ěl : a suffix meaning "pertaining to God"
8	      #5 (parent #4) [Persian] refs=FVQ; MON |  «بابل ، جبرئیل» ;  «اسماعیل ، میکائیل» ;  «اسرائیل ، عزرائیل»
9	    #6 (parent #3) [Latin] refs=None | 
10	      #7 (parent #6) [French] refs=None | 
11	        #8 (parent #7) [Persian] refs=MON | Gâbrîel «گابریل»
12	      #9 (parent #6) [English] refs=KLN; AHD | Babel, Babylonia, Gabriel, Ishmael, Michael, Israel, Azrael
13	  #10 (parent #1) [Hebrew] refs=KLN:1682 | Urî-ěl : "flame of God" or "my light is God"
14	    #11 (parent #10) [Persian] refs=AKM:64 | Ureîl «اوریئل» : name of an angel
15	    #12 (parent #10) [English] refs=KLN:1682 | Uriel
16	  #13 (parent #1) [Hebrew] refs=KLN | Dânî-ěl : "God is my judge", Daniel ☞Dînu ; Ěl-iyyâh : "Lord is God", Elijah ; Immânŭ-ěl : "God is with us", Immanuel ; Rephâ-ěl : "God has healed", Raphael ☞R.f.a' ; Ěli-šebha : "God is an oath", Elizabeth ; Šěmu-ěl : "name of God", Samuel
17	    #14 (parent #13) [Arabic] refs=FVQ | 
18	      #15 (parent #14) [Persian] refs=FVA; MON | Dânyâl «دانیال» : a prophet ; Elyâs «الیاس» : a prophet
19	    #16 (parent #13) [Latin] refs=None | 
20	      #17 (parent #16) [French] refs=None | 
21	        #18 (parent #17) [Persian] refs=MON |  «الیزه ، شانزه لیزه ، آمانوئل» ;  «دانیل ، رافائل ، الیزابت ، ساموئل»
22	      #19 (parent #16) [English] refs=KLN; AHD | Elijah, Immanuel, Daniel, Raphael, Elizabeth, Samuel
23	  #20 (parent #1) [Hebrew] refs=KLN; AHD | Beth-ěl : 'house of God', Bethel ☞B.y.t ; Yô-ěl : 'Lord is God',Joel ; Ěl-îša : God is salvation ; Nethan-ěl : God has given, God given
24	    #21 (parent #20) [Latin] refs=None | 
25	      #22 (parent #21) [English] refs=KLN; AHD | Bethel ; Joel ; Elisha ; Nathaniel
26	
```


## [2026-09-06T22:52:20.644Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-303.json",
 "description": "Read source JSON for page 303"
}
```


### [2026-09-06T22:52:20.680Z] TOOL RESULT

```
{
  "pdf_page": 303,
  "book_page": 273,
  "entries": [
    {
      "root": {
        "name": "Layh, A.l.h",
        "lang": "Semitic / Syriac",
        "refs": "KLN:505; FVQ:66; VDQ:125",
        "gloss": "Layh: to be high; A.l.h: to worship"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:505,510",
          "words": [
            {"translit": "Eloh, Elohim, Ěl", "gloss": "God", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:505,510",
          "words": [
            {"translit": "Elohim, El", "gloss": "God", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN:138,505; AHD:94",
          "words": [
            {"translit": "Bâbh-ěl", "gloss": "\"gate to God\", Babel, Babylonia", "script": null, "see": ["N.b.b"]},
            {"translit": "Gebher-ěl", "gloss": "\"man of God\", Gabriel", "script": null, "see": ["J.b.r"]},
            {"translit": "Yîšmâ-ěl", "gloss": "\"God hears\", Ishmael", "script": null, "see": ["S.m.`a"]},
            {"translit": "Mîxâ-ěl", "gloss": "\"who is like God ?\", Michael", "script": null},
            {"translit": "Yisrâ-ěl", "gloss": "\"soldier of God\", Israel", "script": null},
            {"translit": "Azra`-ěl", "gloss": "\"God has helped\", Azrael", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVQ",
          "words": [
            {"translit": "- el, ěl", "gloss": "a suffix meaning \"pertaining to God\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "FVQ; MON",
          "words": [
            {"translit": null, "gloss": null, "script": "بابل ، جبرئیل"},
            {"translit": null, "gloss": null, "script": "اسماعیل ، میکائیل"},
            {"translit": null, "gloss": null, "script": "اسرائیل ، عزرائیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Gâbrîel", "gloss": null, "script": "گابریل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 6,
          "lang": "English",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "Babel, Babylonia, Gabriel, Ishmael, Michael, Israel, Azrael", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN:1682",
          "words": [
            {"translit": "Urî-ěl", "gloss": "\"flame of God\" or \"my light is God\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "AKM:64",
          "words": [
            {"translit": "Ureîl", "gloss": "name of an angel", "script": "اوریئل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": "KLN:1682",
          "words": [
            {"translit": "Uriel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN",
          "words": [
            {"translit": "Dânî-ěl", "gloss": "\"God is my judge\", Daniel", "script": null, "see": ["Dînu"]},
            {"translit": "Ěl-iyyâh", "gloss": "\"Lord is God\", Elijah", "script": null},
            {"translit": "Immânŭ-ěl", "gloss": "\"God is with us\", Immanuel", "script": null},
            {"translit": "Rephâ-ěl", "gloss": "\"God has healed\", Raphael", "script": null, "see": ["R.f.a'"]},
            {"translit": "Ěli-šebha", "gloss": "\"God is an oath\", Elizabeth", "script": null},
            {"translit": "Šěmu-ěl", "gloss": "\"name of God\", Samuel", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Arabic",
          "refs": "FVQ",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "FVA; MON",
          "words": [
            {"translit": "Dânyâl", "gloss": "a prophet", "script": "دانیال"},
            {"translit": "Elyâs", "gloss": "a prophet", "script": "الیاس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سکندر جست لیکن یافت بهره - ز آب زندگانی خضر و الیاس",
            "poet": "Sanâî"
          }
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "Latin",
          "refs": null,
          "words": [],
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
          "words": [
            {"translit": null, "gloss": null, "script": "الیزه ، شانزه لیزه ، آمانوئل"},
            {"translit": null, "gloss": null, "script": "دانیل ، رافائل ، الیزابت ، ساموئل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 16,
          "lang": "English",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "Elijah, Immanuel, Daniel, Raphael, Elizabeth, Samuel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 1,
          "lang": "Hebrew",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "Beth-ěl", "gloss": "'house of God', Bethel", "script": null, "see": ["B.y.t"]},
            {"translit": "Yô-ěl", "gloss": "'Lord is God',Joel", "script": null},
            {"translit": "Ěl-îša", "gloss": "God is salvation", "script": null},
            {"translit": "Nethan-ěl", "gloss": "God has given, God given", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "English",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "Bethel", "gloss": null, "script": null},
            {"translit": "Joel", "gloss": null, "script": null},
            {"translit": "Elisha", "gloss": null, "script": null},
            {"translit": "Nathaniel", "gloss": null, "script": null}
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


## [2026-09-06T22:52:20.838Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:52:20.877Z] TOOL RESULT

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


## [2026-09-06T22:52:24.815Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVQ','VDQ','AKM','AHD','MON','FVA']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n    print()\n\""
}
```


## [2026-09-06T22:52:25.202Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-06T22:52:26.731Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.", "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (19

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.", "cites": "page number of the Persian translation of Jeffery's Foreign Vocabulary of the Qurʾān"}

AKM {"title": "Amir J. A'lam, Farhang-e A'lam-e Ketab-e Moqaddas (Dictionary of Proper Names in the Bible, English–Persian), Iran University Press 1988", "kind": "purchase", "url": "in print (Niloofar 1388); gisoom/iketab", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
```


### [2026-09-06T22:52:26.764Z] TOOL RESULT

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


## [2026-09-06T22:52:36.796Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60 && echo \"---sizes---\" && ls -la KLN_1966.txt KLN_1971.txt FVQ_pages.txt 2>/dev/null"
}
```


### [2026-09-06T22:52:36.863Z] TOOL RESULT

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
---sizes---
-rw-rw-r-- 1 sfmqrb sfmqrb   628003 Sep  4 14:06 FVQ_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 10837854 Sep  4 14:06 KLN_1966.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 10278576 Sep  4 14:06 KLN_1971.txt
```


## [2026-09-06T22:52:37.618Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Elohim\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T22:52:37.669Z] TOOL RESULT

```
2240:Allah,  n.,  Mohammedan  name  of  the  Supreme Being.  —  Arab.  Alldhu,  contraction  of  al-lldhu, fr.  al-,  ‘the’,  and  lldh.  ‘God’.  See  Elohim.
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
12865:Elohim,  n.,  one  of  the  names  of  God  in  the  Bible.
12866:—  Heb.  Elohim,  pi.  of  El6ah,  ‘God’,  of  un¬ certain  etymology;  possibly  enlarged  fr.  El.  w
```


## [2026-09-06T22:52:52.665Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"nleaves\",len(leaves))\nfor i,l in enumerate(leaves):\n    if 'Elohim,  n.,' in l or 'El,  n.,  Hebrew' in l:\n        print(\"leaf\",i,\"-> approx page\", i*2-24, i*2-23)\nEOF"
}
```


### [2026-09-06T22:52:54.476Z] TOOL RESULT

```
nleaves 903
leaf 275 -> approx page 526 527
leaf 278 -> approx page 532 533
```


## [2026-09-06T22:52:55.175Z] TOOL CALL #10: Bash

```json
{
 "command": "pdftoppm -f 303 -l 303 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg303 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:52:57.665Z] TOOL RESULT

```
total 125504
drwx------ 7 sfmqrb sfmqrb    12288 Sep  6 18:52 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      958 Sep  6 18:52 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332775 Sep  6 18:33 bqtv2_289_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9689 Sep  6 18:33 bqtv2_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   726576 Sep  6 18:33 bqtv2_n289.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63778 Sep  6 18:33 build290b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68833 Sep  6 18:30 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2612 Sep  6 18:28 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13418 Sep  6 18:28 c_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8430 Sep  6 18:28 c_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11245 Sep  6 18:28 c_katrang.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6717 Sep  6 18:28 c_katvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28872 Sep  6 18:28 c_katvar_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18514 Sep  6 18:52 crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    51742 Sep  6 18:33 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    50446 Sep  6 18:33 mk292b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41011 Sep  6 18:29 mk294.py
-rw-rw-r-- 1 sfmqrb sfmqrb    45170 Sep  6 18:47 mk297.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67312 Sep  6 18:51 mk298.py
-rw-rw-r-- 1 sfmqrb sfmqrb    44967 Sep  6 18:51 mk299.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:33 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:43 p295
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:49 p296
-rw-rw-r-- 1 sfmqrb sfmqrb     9447 Sep  6 18:41 p297_av2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8787 Sep  6 18:41 p297_cav.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2803 Sep  6 18:41 p297_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8189 Sep  6 18:41 p297_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   125960 Sep  6 18:28 pg295hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56184 Sep  6 18:39 pg296.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130247 Sep  6 18:41 pg297hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66500 Sep  6 18:33 pg297.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60960 Sep  6 18:39 pg298.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99543 Sep  6 18:52 pg299hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52844 Sep  6 18:38 pg300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89589 Sep  6 18:52 pg303.png
-rw-rw-r-- 1 sfmqrb sfmqrb   132637 Sep  6 18:38 sns_n155.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129771 Sep  6 18:38 sns_n156.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   130970 Sep  6 18:38 sns_n90.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   531356 Sep  6 18:38 sns_n90_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   124445 Sep  6 18:38 sns_n92.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   522585 Sep  6 18:38 sns_n92_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   495290 Sep  6 18:38 sns_n92_right.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   351684 Sep  6 18:35 tad_n59.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   342929 Sep  6 18:35 tad_n59_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   242025 Sep  6 18:34 tad_n60_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   282364 Sep  6 18:34 tad_n60.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   335678 Sep  6 18:34 tad_n60_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   276093 Sep  6 18:34 tad_n61.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   332662 Sep  6 18:34 tad_n62.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   334767 Sep  6 18:35 tad_n65.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   265879 Sep  6 18:35 tad_n65_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:53:06.148Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(273,281):\n    l=leaves[i]\n    print('=== leaf',i,'first 200:',repr(l[:200]))\nEOF"
}
```


### [2026-09-06T22:53:07.844Z] TOOL RESULT

```
=== leaf 273 first 200: 'he  ending  see  subst.  suff.  -ite.\nEdentata,  n.  pi.,  a  group  of  placental  mammals including  the  armadillo,  sloth,  anteater,  etc. (zoo!.)  —  ModL.,  neut.  pi.  of  L.  edentatus, ‘toot'
=== leaf 274 first 200: '?,  ‘an  absolute  master  or  ruler’.  See\nauthentic.\nefferent,  adj.,  conveying  outward  (physiol.) —  L. efferens,  gen.  -entis,  pres.  part,  of  efferre,  ‘to carry  out  or  away;  to  sprea'
=== leaf 275 first 200: 'h. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ),  Gk.  oxtoj, Alb.  tets  (for  *okto-t),  L.  odd,  OSlav.  osmi  (re¬ fashioned  after  the  ordinal  number  osmu,  ‘the eighth’),  Lith.  astuoni, '
=== leaf 276 first 200: '��uplifted,  ex¬ alted’  (used  as  pp.  of  efferre,  ‘to  bring  out,  carry out;  to  raise,  lift  up’),  fr.  e-  and  latus  (used  as pp.  of  ferre,  ‘to  bear,  carry’),  which  stands  for\ne'
=== leaf 277 first 200: 'h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis.\nelephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font'
=== leaf 278 first 200: '  El.  Heb.  qandh,  ‘he  created or  acquired’,  from  which  derive  qinydn,  ‘thing acquired,  acquisition’,  and  miqneh,  ‘cattle’,  is rel.  to  Aram.-Syr.  q(na,  ‘he  acquired’,  Arab. qdnd,  '
=== leaf 279 first 200: ' ])  the  letter  m;  2)  anything  shaped  like an  m;  3)  unit  of  measure  of  printed  matter; orig.  space  occupied  by  the  printed  letter  m. em-,  assimilated  form  of  en-  before  b,  '
=== leaf 280 first 200: ' A  blend  of  em¬ broil  and  brangle.\nembrasure,  n.,  window  opening,  splay  (archil.)  — F.,  fr.  embraser,  ‘to  splay’,  prop,  the  same  word as  embraser,  ‘to  fire,  set  on  fire’;  see'
```


## [2026-09-06T22:53:23.972Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor w in ['Uriel','Babel,','Bethel','Gabriel,','Ishmael','Michael,','Israel,','Azrael','Daniel,','Elijah,','Immanuel','Emmanuel','Raphael','Elizabeth','Samuel,','Joel,','Elisha','Nathaniel','Nathanael']:\n    hits=[i for i,l in enumerate(leaves) if w in l]\n    print(w, [(i,(i-12)*2) for i in hits][:6])\nEOF"
}
```


### [2026-09-06T22:53:26.096Z] TOOL RESULT

```
Uriel [(891, 1758)]
Babel, [(84, 144), (275, 526)]
Bethel []
Gabriel, [(275, 526), (342, 660), (354, 684)]
Ishmael [(275, 526), (442, 860), (453, 882), (549, 1074), (761, 1498), (767, 1510)]
Michael, [(275, 526), (523, 1022)]
Israel, [(275, 526), (443, 862), (446, 868), (737, 1450), (781, 1538)]
Azrael []
Daniel, [(220, 416), (221, 418), (275, 526), (757, 1490)]
Elijah, [(275, 526), (277, 530), (448, 872)]
Immanuel [(37, 50), (280, 536), (415, 806), (452, 880), (499, 974)]
Emmanuel [(44, 64), (275, 526), (280, 536), (287, 550), (502, 980)]
Raphael [(275, 526), (350, 676), (627, 1230), (660, 1296), (692, 1360)]
Elizabeth [(2, -20), (92, 160), (99, 174), (107, 190), (275, 526), (277, 530)]
Samuel, [(733, 1442)]
Joel, [(275, 526), (448, 872)]
Elisha [(275, 526), (277, 530), (401, 778), (549, 1074)]
Nathaniel [(275, 526), (551, 1078)]
Nathanael [(551, 1078)]
```


## [2026-09-06T22:53:43.766Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ndef show(i,pat,before=0,after=1400):\n    l=leaves[i]\n    for m in re.finditer(pat,l):\n        print(f'--- leaf {i} @{m.start()} ---')\n        print(l[max(0,m.start()-before):m.start()+after].replace('\\n',' '))\n        print()\nshow(275, r'\\bEloah|Elohim,  n\\.')\nshow(275, r'Eliezer|Elizabeth,  fem')\nshow(84, r'Babel,  n')\nshow(891, r'Uriel')\nEOF"
}
```


### [2026-09-06T22:53:45.383Z] TOOL RESULT

```
--- leaf 275 @6131 ---
Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel. -el,  suff.,  as  in  hovel.  —  OE.  -el,  -eta,  -ele.  Cp. -le,  suff.  representing  OE.  -el,  -ela,  -ele. -el,  dimin.  suff.  of  French  origin.  —  1)  OF.  -el (F.  - eau ),  fr.  L.  -el/us  (as  in  tunnel)’,  OF.  -ele, -elle  (F.  -eile),  fr.  L.  -ella  (as  in  chapel).  See  -le, suff.  of  French  origin. -el,  suff.  representing  OF.,  F.  -el,  fr.  L.  -alis,  as in  vowel  (fr.  L.  vocalis).  Cp.  adj.  suff.  -al. elaborate,  adj.,  worked  out  in  detail.  —  L.  ela- boratus,  pp.  of  elaborare,  ‘to  exert  oneself’,  lit. ‘to  work  out’,  fr.  e-  and  laborare,  ‘to  work’.  See labor,  v.,  and  adj.  suff.  -ate. Derivatives:  elaborate-ly,  ndv  ..elaborate- ness, n. elaborate,  tr.  v.,  to  work  out  in  detail.  —  L.  ela- boratus,  pp.  of  elaborare.  See  elaborate,  adj. Derivatives:  elaborat-ive,  adj.,  elaborat-or,  n. elaboration,  n.  —  L.  elaboratio,  gen.  -onis,  ‘per¬ severing  labor’,  fr.  elaboratus,  pp.  of  elaborare. See  elaborate,  adj.,  and  -ion. Elaeagnaceae,  n.  pi.,  the  oleaster  family  (hot.)  — ModL.,  formed  fr.  Eleagnus  with  suff.  -aceae. elaeagnaceous.adj. —  See  

--- leaf 84 @4138 ---
Babel,  n.,  name  of  the  capital  of  Babylonia.  — Heb.  Babhel,  fr.  Akkad.  Bab-ilu,  lit.  ‘the  gate  of God’,  prop,  a  literal  translation  of  Sumerian Ka-dingir.  Akkad.  Bab-ilu  is  compounded  of bdb,  ‘gate’,  and  ilu,  ‘god’.  The  first  element  is rel.  to  Aram,  babh,  babhd,  ‘door,  gate’ ;  see  Bab. For  the  second  element  see  El.  Cp.  the  second element  in  Zerubbabel.  Cp.  also  Babylon, babiroussa,  babirussa,  n.,  a  species  of  wild  swine. —  Malay,  compounded  of  babi,  ‘hog’,  and rasa,  ‘deer’. baboo,  n.,  Master,  Mr.  —  Hind.  babu. baboon,  n.  —  ME.  baboin,  fr.  OF.  babuin,  ba- bouin  (F.  babouiti),  a  blend  of  babine,  ‘the  pen¬ dulous  lip  of  certain  animals,  esp.  monkeys’  (the baboon  has  prominent  lips),  and  baboue,  ‘wry, ugly  face’ ;  both  babine  and  baboue  are  of  imi¬ tative  origin.  See  Bloch-Wartburg,  DELF.,  p.49 s.v.  babouin.  MDu.  baubijn  (whence  Du.  baviaan) is  an  OF.  loan  word.  G.  Pavian  is  borrowed  fr. Du.  baviaan. Derivative:  baboon-ery,  n. babouche,  n.,  a  heelless  Oriental  slipper.  —  F., fr.  Arab,  babiish,  fr.  Pers.  papush,  lit.  ‘foot- covering’,  fr.  pa,  ‘foot’,  and  the  verb  pushiden, ‘to  cover’.  Pers.  pa  is  rel.  to  Avestic pad-,  ‘foot’ ; see  foot.  The  change  of  p  to  b  proves  that  the word  came  into  Europe  through  t

--- leaf 891 @3579 ---
Uriel,  for  the  second  see  Eljiah  and  cp.  words there  referred  to. uric,  adj.,  pertaining  to  urine.  —  Formed  with adj.  suff.  -ic  fr.  Gk.  ohpov.  See  urine. Uriel,  masc.  PN.  —  Heb.  Uri’el,  lit.  ‘flame  of God’  or  ‘my  light  is  God’.  See  next  word  and El. Urim,  n.  pi.,  one  of  the  two  objects  attached  to the  breastplate  of  the  high  priest  (Bible).  —  Heb. urim,  of  uncertain  origin.  It  is  perh.  identical with  the  pi.  of  Sr,  ‘fire,  flame’,  fr.  dr,  v.,  ‘it  be¬ came  light’  (whence  also  or,  n.,  ‘light’),  which  is rel.  to  Aram.  Sr,  ‘to  give  light,  shine’,  Akkad. urru,  ‘light,  day’,  Arab,  awwara,  ‘he  kindled’, uwar,  ’heat,  glow’.  Cp.  Uriah,  prec.  word  and the  second  element  in  Melchior.  Cp.  also  the Septuagint  which  renders  urim  by  SrjXcoon;, ‘manifestation’  (fr.  StjXoGv,  ‘to  make  visible’), and  Symmachus,  who  translates  it  with  the word  ooTioiioi,  pi.  of  cpomapLo?,  ‘illumina¬ tion’  (fr.  90k.  gen.  cpUTo?,  ‘light’).  Cp.  Thum- mim. urin-,  form  of  urino-  before  a  vowel, urinal,  n.  —  ME.  urynale,  fr.  OF.  (=  F.)  urinal, fr.  Late  L.  urinal,  fr.  L.  adj.  urinalis,  ‘relating  to urine’,  fr.  urina.  See  urine  and  adj.  suff.  -al. urinary,  adj.  —  Medical  L.  urindrius,  correspond¬ ing  in  sense  to  L.  urinalis,  ‘relating  to  ur

--- leaf 891 @3757 ---
Uriel,  masc.  PN.  —  Heb.  Uri’el,  lit.  ‘flame  of God’  or  ‘my  light  is  God’.  See  next  word  and El. Urim,  n.  pi.,  one  of  the  two  objects  attached  to the  breastplate  of  the  high  priest  (Bible).  —  Heb. urim,  of  uncertain  origin.  It  is  perh.  identical with  the  pi.  of  Sr,  ‘fire,  flame’,  fr.  dr,  v.,  ‘it  be¬ came  light’  (whence  also  or,  n.,  ‘light’),  which  is rel.  to  Aram.  Sr,  ‘to  give  light,  shine’,  Akkad. urru,  ‘light,  day’,  Arab,  awwara,  ‘he  kindled’, uwar,  ’heat,  glow’.  Cp.  Uriah,  prec.  word  and the  second  element  in  Melchior.  Cp.  also  the Septuagint  which  renders  urim  by  SrjXcoon;, ‘manifestation’  (fr.  StjXoGv,  ‘to  make  visible’), and  Symmachus,  who  translates  it  with  the word  ooTioiioi,  pi.  of  cpomapLo?,  ‘illumina¬ tion’  (fr.  90k.  gen.  cpUTo?,  ‘light’).  Cp.  Thum- mim. urin-,  form  of  urino-  before  a  vowel, urinal,  n.  —  ME.  urynale,  fr.  OF.  (=  F.)  urinal, fr.  Late  L.  urinal,  fr.  L.  adj.  urinalis,  ‘relating  to urine’,  fr.  urina.  See  urine  and  adj.  suff.  -al. urinary,  adj.  —  Medical  L.  urindrius,  correspond¬ ing  in  sense  to  L.  urinalis,  ‘relating  to  urine’,  fr. urina.  See  urine  and  adj.  suff.  -ary. urinate,  intr.  v.  —  ML.  urinatus,  pp.  of  urinare, ‘to  pass  urine’,  fr.  L.  urina,  ‘urine’.  (L.  urindri means
```


## [2026-09-06T22:54:12.030Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\npats={275:[r'El,  n\\.,  Hebrew'],277:[r'Elijah,',r'Elisha,',r'Elizabeth,  fem'],\n      280:[r'Emmanuel|Immanuel'],342:[r'Gabriel,'],453:[r'Ishmael'],443:[r'Israel,'],\n      523:[r'Michael,'],551:[r'Nathaniel'],660:[r'Raphael'],733:[r'Samuel,'],448:[r'Joel,'],\n      220:[r'Daniel,']}\nfor i,ps in pats.items():\n    l=leaves[i]\n    for p in ps:\n        for m in list(re.finditer(p,l))[:2]:\n            print(f'### leaf {i} /{p}/')\n            print(l[m.start():m.start()+700].replace('\\n',' '))\n            print()\nEOF"
}
```


### [2026-09-06T22:54:14.146Z] TOOL RESULT

```
### leaf 275 /El,  n\.,  Hebrew/
El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel. -el,  suff.,  as  in  hovel.  —  OE.  -el,  -eta,  -ele.  Cp. -le,  suff.  representing  OE.  -el,  -ela,  -ele. -el,  dimin.  suff.  of  French  origin.  —  1)  OF.  -el (F.  - eau ),  fr.  L.  -el/us  (as  i

### leaf 277 /Elijah,/
Elijah,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  the great  prophet  also  known  as  the  Tishbite.  — Heb.  Eliyydh,  lit.  ‘The  Lord  is  God’.  For  the first  element  see  El  and  words  there  referred  to and  cp.  esp.  Joel.  For  the  second  element  in Elijah  cp.  the  second  element  in  hallelujah, Hezekiab,  Isaiah,  Jeremiah,  Matthew,  Matthias, Nehemiah,  Obadiah,  Zachariah,  Zephaniah.  Cp. also  Elias,  a  shortened  form  of  Elijah. eliminable,  adj.  —  See  eliminate  and  -able, eliminant,  adj.,  promoting  elimination  ( med .)  — L.  eliminans,  gen.  -antis,  pres.  part,  of  eliminare. See  next  word  and  -ant. eliminate,  tr.  v.,  1)  to  rem

### leaf 280 /Emmanuel|Immanuel/
Emmanuel,  masc.  PN.  —  Gk.  ’Efj.[zavour]A,  fr. Heb.  'Immanuel,  lit.  ‘God  is  with  us’.  See  Im¬ manuel. emmenic,  adj.,  capable  of  menstruation  (med.) Formed  with  suff.  -ic  fr.  Gk.  iiLiirya,  ‘the  men¬ ses’,  fr.  ev  (see  2nd  en-),  and  p.r)v,  gen.  wrybe, ‘month’.  See  meno-,  and  cp.  catamenia, emmenology,  n.,  that  part  of  medicine  which treats  of  menstruation.  —  Compounded  of  Gk. spipnrjva,  ‘the  menses’,  and  -Xoyia,  fr.  -Aoyop, one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  emmenic  and -logy. Emmentaler  cheese,  often  shortened  to  emmen- taler,  n.  —  G.  Emmentaler  Kdse,  ‘Emmentaler ch

### leaf 280 /Emmanuel|Immanuel/
Immanuel,  lit.  ‘God  is  with  us’.  See  Im¬ manuel. emmenic,  adj.,  capable  of  menstruation  (med.) Formed  with  suff.  -ic  fr.  Gk.  iiLiirya,  ‘the  men¬ ses’,  fr.  ev  (see  2nd  en-),  and  p.r)v,  gen.  wrybe, ‘month’.  See  meno-,  and  cp.  catamenia, emmenology,  n.,  that  part  of  medicine  which treats  of  menstruation.  —  Compounded  of  Gk. spipnrjva,  ‘the  menses’,  and  -Xoyia,  fr.  -Aoyop, one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  emmenic  and -logy. Emmentaler  cheese,  often  shortened  to  emmen- taler,  n.  —  G.  Emmentaler  Kdse,  ‘Emmentaler cheese’,  prop,  ‘cheese  of  the  valley  of  the  Great Emm

### leaf 342 /Gabriel,/
Gabriel,  1)  masc.  PN. ;  2)  in  the  Bible,  name  of  an angel.  —  Heb.  GabhrVil,  lit.  ‘man  of  God’,  fr. gebher,  ‘man’,  and  El,  ‘God’.  Heb.  gebher derives  from  the  base  of  the  verb  gdbhar,  ‘was strong’,  whence  also  gibbdr,  ‘strong,  mighty; hero’,  glbhtr,  ‘lord’,  g(bhirdh,  gebhereth,  ‘lady, queen’,  gebhurdn,  ‘strength,  might’.  Cp.  the related  words:  Aram. -Syr. glbhar, ‘was  mighty’, gebhar,  gabhrd,  ‘man’,  Syr.  gabbdr,  ‘hero’, Arab,  jabr,  ‘a  strong,  young  man’,  jabbdr, ‘tyrant’,  Akkad,  gapru,  ‘strong’,  Ethiop.  gabara, ‘he  acted’.  For  the  first  element  cp.  gibbar,  for the  second  see  El. gaby,  n.,  a  foolish  person.  —  Pr

### leaf 453 /Ishmael/
Ishmael  (see  Gen. 25:3,  IChr.  1:29),  rel.  to  qadhar,  ‘was  black, dark,  swarthy’,  whence  also  qadhruth,  ‘dark¬ ness,  gloom’,  qedhorannlth,  ‘gloomily,’  QidhrSn, name  of  a  wady  and  valley  east  of  Jerusalem, Mishnaic  Heb.  qldherdh,  ‘pot’,  qadddr,  ‘potter’, and  to  Aram,  qidhrd,  qedherd,  Syr.  qedhrd,  ‘pot’, Arab,  qddhura,  qadhira,  ‘was  dirty’. Derivative:  Kedar-ite ,  adj.  and  n. keddah,  n.,  an  enclosure  for  entrapping  ele¬ phants  (India).  —  Hind,  khedd,  rel.  to  khedna ‘to  chase,  hunt’,  fr.  OI.  akhetah,  khetah,  ‘hun¬ ting’,  which  is  of  uncertain  origin, kedge,  tr.  v.,  to  warp  (a  ship);  intr.  v.,  to  move a  ship  by  ke

### leaf 443 /Israel,/
Israel,  n.  —  L.  Israel,  fr.  Gk.  ’IopaajX,  fr.  Heb. Yisra’el,  lit.  ‘he  contends  with  God’,  fr.  sardh, ‘he  fought,  contended’,  and  El,  ‘God’.  The  first element  is  rel.  to  Arab,  shard,  ‘he  was  angry’, in  the  III  conj.  ‘he  contended’.  For  the  second element  see  El. Israelite,  n.  —  L.  Israelita,  fr.  Gk.  ’Iopa7)Xfx7)4, ‘Israelite’,  fr.  ’IopaTjX.  See  prec.  word  and  subst. suff.  -ite. Derivatives:  Israelit-ic,  adj.,  Israelit-ish,  adj., Israelit-ism,  n. Issachar,  n.,  son  of  Jacob  by  Leah;  a  tribe  of Israel  (Bible).  —  Gk.  Taad/xp,  fr.  Heb.  Yissd- khdr,  which  prob.  stands  for  yesh  sakhdr,  ‘there is  a  reward’.  See  Ge

### leaf 443 /Israel,/
Israel,  fr.  Gk.  ’IopaajX,  fr.  Heb. Yisra’el,  lit.  ‘he  contends  with  God’,  fr.  sardh, ‘he  fought,  contended’,  and  El,  ‘God’.  The  first element  is  rel.  to  Arab,  shard,  ‘he  was  angry’, in  the  III  conj.  ‘he  contended’.  For  the  second element  see  El. Israelite,  n.  —  L.  Israelita,  fr.  Gk.  ’Iopa7)Xfx7)4, ‘Israelite’,  fr.  ’IopaTjX.  See  prec.  word  and  subst. suff.  -ite. Derivatives:  Israelit-ic,  adj.,  Israelit-ish,  adj., Israelit-ism,  n. Issachar,  n.,  son  of  Jacob  by  Leah;  a  tribe  of Israel  (Bible).  —  Gk.  Taad/xp,  fr.  Heb.  Yissd- khdr,  which  prob.  stands  for  yesh  sakhdr,  ‘there is  a  reward’.  See  Gen.  30: 18. issue,  

### leaf 523 /Michael,/
Michael,  1)  masc.  PN.;  2)  in  the  Bible,  an  arch¬ angel.  —  Late  L.,  fr.  Gk.  Mty.afps  fr.  Heb. Mikha  el,  lit.  ‘Who  is  like  God?’  See  El  and  cp. Micah. Michaelmas,  n.,  festival  ofthe  archangel  Michael, celebrated  by  the  Christian  church  on  Septem¬ ber  29th.  —  Compounded  of  Michael  and  -mas, ‘mass’.  See  Mass. mick,  n.,  an  Irishman  (slang).  —  Corruption  of the  PN.  Michael. mickle,  adj.,  great,  much  ( archaic  or  dial.)  —  ME. mikel,  muchel,  fr.  OE.  micel,  mycei,  ‘great,  big, many’,  rel.  to  OS.  mikil,  ON.  mikill,  OHG. mihhil,  Goth,  mikils,  fr.  I.-E.  base  *meg(h)-, *m*g-,  ‘great,  large’,  whence  also  OI.  mah-, ma

### leaf 523 /Michael,/
Michael, celebrated  by  the  Christian  church  on  Septem¬ ber  29th.  —  Compounded  of  Michael  and  -mas, ‘mass’.  See  Mass. mick,  n.,  an  Irishman  (slang).  —  Corruption  of the  PN.  Michael. mickle,  adj.,  great,  much  ( archaic  or  dial.)  —  ME. mikel,  muchel,  fr.  OE.  micel,  mycei,  ‘great,  big, many’,  rel.  to  OS.  mikil,  ON.  mikill,  OHG. mihhil,  Goth,  mikils,  fr.  I.-E.  base  *meg(h)-, *m*g-,  ‘great,  large’,  whence  also  OI.  mah-, mahd-,  mahat-,  ‘great’,  mahas-,  ‘greatness’, Avestic  maz -,  mazant-,  ‘great’,  mazah-,  ‘great¬ ness’,  Toch.  A  mak,  B.  maka-,  ‘great,  much’, Hitt,  mekkish,  ‘great,  large’.  Arm.  mec  (instru¬ mental  case  

### leaf 551 /Nathaniel/
Nathaniel, Jonathan,  Nethinim.  Cp.  also  Matthew,  Mat¬ thias. Nathaniel,  Nathanael,  masc.  PN.  —  Late  L.  Na¬ thanael,  fr.  Gk.  Naffxva 7)X,  fr.  Heb.  Nathan' el, lit.  ‘God  has  given’.  See  Nathan  and  El. natheless,  nathless,  adv.,  nevertheless  (archaic). —  ME)  natheles,  fr.  OE.  nd  pe  lies,  'not  the  less’. See  no,  adv.,  and  nevertheless. Natica,  n.,  a  genus  of  marine  snails  (zool.)  — ModL.,  fr.  ML.  natica,  ‘buttock’,  dimin.  of  L. natis.  See  nates. nation,  n.  —  ME.  nacioun,  fr.  OF.  (=  F.)  nation, fr.  L.  nationem,  acc.  of  natio,  ‘breed,  race,  peo¬ ple,  nation’,  lit.  ‘birth’,  fr.  natus,  pp.  of  nasci,  'to be  born’, 

### leaf 551 /Nathaniel/
Nathaniel,  Nathanael,  masc.  PN.  —  Late  L.  Na¬ thanael,  fr.  Gk.  Naffxva 7)X,  fr.  Heb.  Nathan' el, lit.  ‘God  has  given’.  See  Nathan  and  El. natheless,  nathless,  adv.,  nevertheless  (archaic). —  ME)  natheles,  fr.  OE.  nd  pe  lies,  'not  the  less’. See  no,  adv.,  and  nevertheless. Natica,  n.,  a  genus  of  marine  snails  (zool.)  — ModL.,  fr.  ML.  natica,  ‘buttock’,  dimin.  of  L. natis.  See  nates. nation,  n.  —  ME.  nacioun,  fr.  OF.  (=  F.)  nation, fr.  L.  nationem,  acc.  of  natio,  ‘breed,  race,  peo¬ ple,  nation’,  lit.  ‘birth’,  fr.  natus,  pp.  of  nasci,  'to be  born’,  which  stands  for  *gnasci,  fr.  I.-E.  *gn-, zero  degree  of 

### leaf 660 /Raphael/
Raphaelite,  n.,  a  member  of  the  society  of painters  called  the  Pre-Raphaelite  Brotherhood ; adj.,  pertaining  to  Pre-Raphaelitism.  —  See  next word. Pre-Raphaelitism,  n.,  the  style  of  the  Pre-Raphae¬ lites.  —  Formed  with  suff'.  -ism  from  the  fore¬ name  of  Raphael  Sanzio  (1483-1520)  and  the suffixes  -ite  and  -ism.  The  members  of  the  Pre- Raphaelite  Brotherhood,  founded  in  England  in 1847,  called  themselves  Pre-Raphaelites,  to  inti¬ mate  that  their  style  resembled  that  of  the  Italian painters  before  Raphael, prerequisite,  n.  —  Formed  fr.  pre-  and  requisite, prerogative,  n.,  a  special  privilege.  —  ME.,  fr. OF.  (=  F.)

### leaf 660 /Raphael/
Raphaelite  Brotherhood ; adj.,  pertaining  to  Pre-Raphaelitism.  —  See  next word. Pre-Raphaelitism,  n.,  the  style  of  the  Pre-Raphae¬ lites.  —  Formed  with  suff'.  -ism  from  the  fore¬ name  of  Raphael  Sanzio  (1483-1520)  and  the suffixes  -ite  and  -ism.  The  members  of  the  Pre- Raphaelite  Brotherhood,  founded  in  England  in 1847,  called  themselves  Pre-Raphaelites,  to  inti¬ mate  that  their  style  resembled  that  of  the  Italian painters  before  Raphael, prerequisite,  n.  —  Formed  fr.  pre-  and  requisite, prerogative,  n.,  a  special  privilege.  —  ME.,  fr. OF.  (=  F.)  prerogative,  fr.  L.  praerogativa,  ‘a previous  choice  or  election’,  

### leaf 733 /Samuel,/
Samuel,  masc.  PN. ;  a  celebrated  judge  and  proph¬ et  (Bible).  —  Late  L.,  fr.  Gk.  Sau,ouY)X,  fr.  Heb. Shlmu'el,  lit.  ‘name  of  God’,  fr.  shem,  ‘name’, and  El,  God’.  The  first  element  is  rel.  to  Aram. shem,  sh?ma,  also  shum,  Ugar.  sh-m,  Arab,  sim, sum,  ism,  Ethiop.  sem,  Akkad,  shumu,  ‘name’. For  the  second  element  see  El. samurai,  n.  (sing,  and  pi.),  1)  a  member  of  the military  retainers  of  the  daimios  (new  extinct) ; 2)  gentry;  3)  an  army  officer.  —  Jap.,  ‘guard’, san,  n.,  name  of  the  ancient  Greek  letter  — Fr.  Heb.  shin,  name  of  the  latter  sh,  for  shen, ‘tooth’.  See  sin,  shin. sanable,  adj.,  curable

### leaf 448 /Joel,/
Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to. Joanna,  fem.  PN.  —  ML.  Johanna,  Joanna,  fem. form  of  ML.  Johannes,  Joannes.  See  John  and cp.  Jean,  fem.  PN.,  Johanna, job,  n.,  piece  of  work.  —  Of  uncertain  origin. Derivatives:  job,  intr.  v.,  to  do  odd  jobs, etc; tr.  v.,  to  hire  or  to  let  out  for  hire  (a  horse  or carriage),  jobb-er,  n.,  jobb-ery,  n.,  jobb-ing,  adj. job,  tr.  v.,  to  stab,  to  prod.  —  ME.  jobben,  ap¬ parently  of  imitative  origin.  Cp.  jab. Job,  1)  masc.  PN. ;  2)  in  the  Bible:  a)  a  man  who endured  much  suffering  with  faith  and  patience; b)  the  Book

### leaf 448 /Joel,/
Joel,  1)  masc.  PN.;  2)  a)  the  second  in  the  order of  the  Twelve  Prophets;  b)  the  Book  of  Joel (Bible).  —  Late  L.  Joel,  fr.  Gk.  ’ J cofjX,  fr.  Heb. Yo’el,  lit.  ‘the  Lord  is  God’.  See  Elijah,  in  which the  same  two  elements  are  contained,  but  in  an inverted  order. Joe  Miller,  1)  a  jestbook;  2)  a  stale  joke.  — From  Joseph  Miller,  name  of  a  comedian  (1684- 1738),  whose  name  was  connected  with  a  jest- book  published  in  1739. Joey,  n.,  masc.  PN.  —  Dimin.  of  Joe. joey,  n.,  a  young  kangaroo.  —  Fr.  native  Aus¬ tralian  joe. jog,  tr.  v.,  to  push  or  shake  slightly;  to  nudge; intr.  v.,  to  move  slowly.  —  O

### leaf 220 /Daniel,/
Daniel,  Dinah. Cp.  also  Danaiis. Dan,  n.,  a  title  of  honor  equivalent  to  Master.  — OF.  dan,  fr.  L.  dominus,  ‘lord,  master’.  F.  dom (an  ecclesiastic  title)  also  derives  fr.  L.  dominus (through  the  medium  of  It.  don,  short  form  of donno).  See  dominus,  dome,  ‘building’,  and  cp. Dom,  domine,  dominie,  domino,  donna. Danae,  n.,  daughter  of  Acrisius  and  mother  of Perseus  ( Greek  mythol.)  —  L.,  fr.  Gk.  Aavdfo;, lit.  prob.  meaning  ‘she  who  judges’,  and  rel.  to Aavai?.  See  Danaiis. Danaid,  n.,  one  of  the  Danaides.  —  See  Danaides. Danaidean,  adj.,  pertaining  to  the  Danaides.  — Formed  fr.  Danaides  with  suff.  -an. Dan
```


## [2026-09-06T22:54:29.700Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"nleaves\",len(leaves))\nfor n in (83,84):\n    print(\"==== leaf\",n,\"(printed p.\",n-17,\")\")\n    print(leaves[n][:2600])\nEOF"
}
```


### [2026-09-06T22:54:31.543Z] TOOL RESULT

```
nleaves 335
==== leaf 83 (printed p. 66 )
66 FOREIGN VOCABULARY OF THE QUR ? AN
'4J| (Alldh).
Of very frequent occurrence.
God.
One gathers from ar-Razi, Mafdfih, i, 84 (so Abu Hayyan, Bcihr,
i, 15), that certain early Muslim authorities hold that the word was of
Syriac or Hebrew origin. The majority, however, claimed that it was
pure Arabic, though they sot forth various theories as to its derivation. 1
Some held that it has no derivation, being A^ - : the Kufans in
- * *
general derived it from o X * I, while the Basrans derived it from
I , taking d 2/ as a verbal noun from O to be high or to be veiled.
The suggested origins for a 2(] were even more varied, some taking
-/* ^ *
it from 43 1 to worship, some from <) I to be perplexed, some from
(jl A) I to turn to for protection, and others from <)j to be perplexed.
Western scholars are fairly unanimous that the source of the
word must be found in one of the older religions. In the Semitic area
JlvK was a widely used word for deity, cf. Heb. H^K ; Aram. H7K ;
Syr. loi!k ; Sab. V1h and s <> Ar. 4) I is doubtless a genuine old
2
Semitic form. The form 4,\J|, however, is different, and there can be
little doubt that this, like the Mandaean N!"INvX and the Pahlavi
ideogram, 2 goos back to the Syr. loii^ (cf. Griinbaum, ZDMG,
xxxix, 571; Sprenger, Lebcn, i, 287-9; Ahrens, Muhammad, 15;
Rudolph, Abhangigkeit, 26 ; Bell, Origin, 54 ; Cheikho, Nasrdniya,
159 ; Mingana, Syriac Influence, 86). The word, however, came into
use in Arabian heathenism long before Muhammad's time (Wellhausen,
Reste, 217 ; Nielsen in HAA, i, 218 ff.). It occurs frequently in the
N. Arabian inscriptions, 3 and also in those from S. Arabia, as, e.g.,
1 They are discussed in detail by ar-Razi on pp. 81-4, of the first volume of his
Tafsir.
2 Herzfeld, Paikuli, Glossary, 135.
3 Cf. Littmann, Entzifferung der thamudenischen Inschriften, p. 63 IF. ; Sem. Inscr,
p. 113 ff. ; and Ryckmans, Noms propres, i, 2 ; RES, iii, 441.
==== leaf 84 (printed p. 67 )
FOREIGN VOCABULARY OF THE QUR*AN 67
3X1 Mn 1rf h3 " with all the Gods " (in Glaser, Abessinien, 50), 1
as well as in the pie-Islamic oath foims, such as that of Qais b. Khatim
given by Horovitz, KU, 140, and many in ash-Shanqiti's intioduction
to the Mu'allaqat. It is possible that the expression (JW 4\J1 is of
S. Arabian origin, as the name i iX occurs in a Qatabanian
inscription. 2
-/"*
1,^)1 (Allahumma).
iii, 25 ; v, 114 ; viii, 32 ; x, 10 ; xxxix, 47.
An invocatory name for God.
The form of the word was a great puzzle to the early grammarians 3 :
the orthodox explanation being that it is a vocative form where the
final A takes the place of an initial u. The Kufans took it as a con-
\
traction of ^J^ U*l 4\]l u (Bai<J. on iii, 25), but their theory is
ridiculed by Ibn Ya'ish, i, 181. As a vocative it is said to be of the same
f >
class as 1& come along. al-Khafaji, 20, however, recognizes it as a
foreign word.
It is possible, as Margoliouth notes (ERE, vi, 248), that it is the
Heb. DTI /K which had become known to the Arabs through their
contacts with Jewish tribes. 4
vi, 85 ; xxxvii, 123, 130.
Elijah.
1 Derenbourg in JA, viii e ser., xx, 157 if., wants to find the word in the \ T in
of a Minacan inscription, but this is usually taken as a reference to a tribal god ^l^II,
Me Halcvy, ibid, p. 325, 326.
2 Rhodokanakis, " Die Inschriften an der Mauer von Kohilan Tirana*," in SBAW,
Wien, 1924. 8 Margoliouth, ERE, vi, 248.
4 There is to be considered, however, the Phon. Q^3X = godhead (see references
in Harris' Glossary, p. 77), which is evidence of a Semitic form with final m. Cf.
Nielsen in HAA, i, 221, n. 2.
```


## [2026-09-06T22:54:50.923Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"Jibril|Mika|Israil|Isma'il|Ismail|Ilyas|Elijah|Daniel|Azrael|Israel\" FVQ_pages.txt | head -40"
}
```


### [2026-09-06T22:54:50.973Z] TOOL RESULT

```
240:Margoliouth, D. S. Schweich Lectures on Relations between Arabs and Israelites.
414:religionum, Hebraicae, Christianae, et Israeliticae, additis paucis
1361:old Israelitish tradition.26 INTRODUCTION
2319:2 Oeschichte Israels, i, 483.
2407:Children of Israel. In vii, 160, it is used normally of the Twelve Tribes,
2517:(Israil).
2526:Usually it stands for the Children of Israel, but in iii, 87, and xix,
2618:(Ismail).
2757:Elijah.
2831:2 Zimmern, Akkad. Fremdw, 46 ; Pedcrsen, Israel, 505.
3221:The word occurs in the Elijah story and as a proper name un-
4460:1 Daniel, 62 n.
4797:In the QurYin he is mentioned both as King of Israel and also as
5891:calf for the Children of Israel.
5895:deceive the Israelites. This, however, is rather remote, and there can
6410:late/period. In ii, 249, it refers to the sign whereby the Israelites
6529:and quails sent as provision for the Children of Israel in their desert
6562:name of Israel's king, and as a personal name, 3 so it would have been
7497:with the experiences of the Israelites at Sinai. 4
8465:contest between Elijah and the priests of Baal, and the latter to the
9762:to the Children of Israel (LA, xvii, 306).
9883:of Israel.
```


## [2026-09-06T22:54:54.374Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2510,2560p;2610,2660p;2750,2790p' FVQ_pages.txt"
}
```


### [2026-09-06T22:54:54.432Z] TOOL RESULT

```
and pH2T would seem to point to a Christian origin, 2 cf. Gk. 'IcraaK,
Syr. t-QiAttLilor Q**CDl, 3 though it is true that in the Talmud we come
across a pO^K *12 "HO (Baba Mezi'a, 39 b ), showing a form with
initial vowel among the Babylonian Jews of the fourth century A.n. 4
The name >z*\ must have been known before the Qur'an, but no
pre-Islamic instances of it seem to occur, for those quoted by Cheikho,
Nasrdniya, 229, 230, are rightly rejected by Horovitz, K U, 91.
(Israil).
Occurs some 43 times. Cf. ii, 38.
1 West, Glossary, 13.
2 Spronger, Leben, ii, p. 336; Fraenkel, ZA, xv, 394; Horovit/., JPA T , 155, and
Mingana's note, Syriar Influence, 83. Torrey, Foundation, 49, however, takes this
to be a characteristic of his assumed Judaeo-Arabic dialect.
3 This is the Christian Palestinian form, cf. Schulthess, Le.r, 14.
4 Derenbourg in REJ, xviii, 127, suggests that p!"I2P may have been pronounced
among the Arabian Jews asFOREIGN VOCABULARY OF THE QUR'AN 61
Usually it stands for the Children of Israel, but in iii, 87, and xix,
59, it is the name of the Patriarch otherwise called *
Some of the exegetes endeavoured to derive it from^ " to travel
by night ", because when Jacob fled from Esau he travelled by night
(cf. at-Tabari, Annales, i, 359, and Ibn al-Athir). It was very generally
recognized as a foreign name, however (cf. al- Jawaliqi, 9 ; al-KhafajI,
II), 1 and is given as such by the Commentators Zam. and Bai(J. on
ii, 38.
Here also the absence of the initial ** stands against a direct deriva-
tion from the Heb. ^^HC??, and points to a Christian origin, cf. Gk.
'Ioy>a??A, Syr. ^5u;au] ' Ett . hfl/,./bA The probabilities are in
favour of a Syriac origin 2 especially in view of the Christian Palestinian
forms ^Vrflol ; ^VrO^l (Schulthess, Lex, 16). The name was doubt-
less well enough known to the people of Muhammad's day and though
no pre-Tslainic example of its use in N. Arabia seems to have survived 3
1ih)&? occurs in S. Arabian inscriptions, cf. CIS, iv, 543, 1. 1.
ff * I / / T v
| (USSIS).
^ ^
ix, 109.
Founded .
- * \
The verbal form .y* I occurs in ix, 110. The verb is denominative
.
from -, I , a foundation, which Fraenkel, Fremdw, 11, noted was an
Aramaic borrowing, cf. Aram. $$*}# foundation, and in the Christian
Palestinian dialect the verb **! = e'^/zeA/oxre ; %A)LD
re0e/x6A/a>TO, and )*ol OentXiov (Schwally, Idioticon, 7),
so classical Syr. l*o) (and see Noldeke, Hand. Gramm, 98, n. 2 ;
Zimmern, AJcJcad. Fremdw, 31 ; Henning, BSOS, ix, 80).
1 al-Khafaji notes the uncertainty as to the spelling of the word, Jl . I and
J^l^l being known besides J-TI^I.
2 Mingana, Syriac Influence, 81 ; Horovitz, KU, 91. The Qamus, as a matter of
fact, says that all forms ending in JJ are jl^-, though Tab. on ii, 38, claims that
J.J is Heb.
in Syriac that we find j^] used precisely as in the Qur'an, e.g.
" he devoted himself to God and His
Church ", or -ooim2U OlL^ oVnV^. 2 and one feels confident in
looking here for the origin of the Arabic word.
J
*, of course, is a formation from this, 3 and was in use in
pre-Islamic Arabia. *y<**\ however, would seem to have been
formed by Muhammad himself after he began to use the word.
(Ismail).
ii, 119-134 ; iii, 78 ; iv, 161 ; vi, 86 ; xiv, 41 ; xix, 55 ; xxi, 85 ;
xxxviii, 48.
Ishmael.
The Muslim philologers early recognized that it was non- Arabic,
as is clear from Zam. on xix, 55, and from its being treated as non-
Arabic by al-Jawaliqi, Mu'arrab, 9 ; al-KhafajT, 10; as-SuyutT, Muzhir,
1 Robertson Smith, Religion of the Semites, 79 ff.
2 The example given by Horovitz, viz. OO1
is curiously like <jrdUl L>
3 Sura, li, 36 ; xxii, 77 ; and note Bagh, vii, 192, and Ya'qubl, 7/tVrf, i, 259, and
its use in Safaito (RvckmaiiK, Nmns propres, i, 239).64 FOREIGN VOCABULARY OF THE QUR'AN
i, 138. Various forms of the name are given J^*^ I ; +*" \ ; A
and Ju^U^l, the ^ in this last form, quoted from Sibawaih in Muzhir,
i, 132, being significant.
A Christian origin for the word is evident from a comparison
of the Gk. 'I(j/ia^A ; Syr. Vu^iQ*] ; Kth. ftfr'VJt.A, with the Heb.
7X17Q2T. A form derived from Heb. occurs in the inscriptions of
both the S. and N. of the Peninsula. 1 In S. Arabia we* find in a
Himyaritic inscription 1h3 A? 2 - ^NJJQO'' (cf. Eth.
and in the Safaite inscriptions of N. Arabia we find a form
It is thus clear that the form with initial * was well enough known
in Arabia before Muhammad's day, but on the other hand, there seems
to be no evidence that the form used in the Qur'an was in use as a
personal name among the Arabs in pre-Islamic times. 4 The fact
that in the Qur'an we find cJu-j^for ^JOV and CJJ.AA> for DplT,but
J for ^infiP and J-uH for ^KSTKOf], just as in Syr. we find
and >OQ^, but JfiCU and '^j.LSQ*] makes it
reasonably certain that the Qur'anic form came from a Syr. source, 6
and the form ^ A S V)fln) in the Christian Palestinian dialect removes
any difficulty which might have been felt of ^ for
1 I). H. Miiller suggests that the name is an independent formation in S. Arabian
(WZKM, iii, 225, being followed in this by Horovitz, .IPS, 155, 15C), but this is a
little difficult.
2 Hal, 193, 1 ; cf. CIS, iv, i, 55, with other references in Filter's " Index of H.
Arabian Proper Names ", PttBA* 1917, p. 110, and Hartmann, Arahische, Frage, 182.
226, 252-4. Derenbourg in his note on this inscription, C'/S', iv, i, 56, takes it as a
composite name in imitation of the Heb., but see Miiller, \VZKM, iii, 225 ; ZDMG,
xxxvii, 13 ff. ; Ryekmans, A'OOTA propres, i, 239, and RES, i, No. 219.
3 Dussaud, Mission, 221 ; Littmann, Semitic Inscriptions, 116, 117, 123 ; En,'-
zifferumj der Naffi-lnsehriften, 58 ; Lidzbarski, Ephemeris, ii, 44.
4 The examples collected by Cheikho, Xa*riiniya 9 230, cannot, as Horovitz, K(J,
92, shows, be taken as evidence for the pre-lslamic use of the name. The form 'EapayXos
f >
class as 1& come along. al-Khafaji, 20, however, recognizes it as a
foreign word.
It is possible, as Margoliouth notes (ERE, vi, 248), that it is the
Heb. DTI /K which had become known to the Arabs through their
contacts with Jewish tribes. 4
vi, 85 ; xxxvii, 123, 130.
Elijah.
1 Derenbourg in JA, viii e ser., xx, 157 if., wants to find the word in the \ T in
of a Minacan inscription, but this is usually taken as a reference to a tribal god ^l^II,
Me Halcvy, ibid, p. 325, 326.
2 Rhodokanakis, " Die Inschriften an der Mauer von Kohilan Tirana*," in SBAW,
Wien, 1924. 8 Margoliouth, ERE, vi, 248.
4 There is to be considered, however, the Phon. Q^3X = godhead (see references
in Harris' Glossary, p. 77), which is evidence of a Semitic form with final m. Cf.
Nielsen in HAA, i, 221, n. 2.68 FOREIGN VOCABULARY OF THE QUR ? AN
In xxxvii, 130, for the sake of rhyme, the form is ^
From al-Jawallql, Mu'arrab, 8, we learn that the philologers early
recognized it as foreign, and it is given as such by as-Suyuti, Muzhir,
i, 138 ; as-Sijistanl, 51 ; LA, vii, 303. The Heb. forms are PP^K and
'irpbN, so it is obvious that the Arabic form must have been derived
from a Christian source, as even Hirschfeldi Beitrage, 56, recognizes. 2
The Gk. 'HA*W or 'HAe/ay gives us the final s, but this afso appears
in Syr. j]l!& beside the more usual ]1^ (P/Sw, 203), and in the
Eth. J^A^fl.
The name was no uncommon one among Oriental Christians before
Islam, and 'HA/a? occurs not infrequently in the Inscriptions. 3 We
also find an ^Ul in the genealogy of the poet 'Adi b. Zaid given in
Aghdril, ii, 18. 4 The likelihood is thus that it entered Arabic through
the Syriac.
**
(Al-Yasa 6 ).
vi, 86 ; xxxviii, 48.
Elisha.
The word is usually treated as though it were **-^ arid the J)
the definite article, 5 and then derived from ^^ or x**J. Tab., on
vi, 86, argues against this view, and in the Lexicons (e.g. al-Jawharl,
sub roc., LA, x, 296), and in al-Jawallql, 134 (cf. al-Khafaji, 215), it is
given as a foreign borrowing, a fact which is also indicated by the
variant spelling *~Jb (LA, x, 296).
1 Gciger, 190 ; Mingana, Ryriac Influence, 83. Grimme, ZA, xxvi, 167, would
```


## [2026-09-06T22:55:04.304Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"^Gabriel|Gabriel\\.|Michael\\.|^Michael\" FVQ_pages.txt | head -20"
}
```


### [2026-09-06T22:55:04.356Z] TOOL RESULT

```
3846:Gabriel.
9878:Michael.
```


## [2026-09-06T22:55:06.850Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3838,3900p' FVQ_pages.txt && echo \"=========\" && sed -n '9870,9925p' FVQ_pages.txt"
}
```


### [2026-09-06T22:55:06.910Z] TOOL RESULT

```
says it is from yvi/ios.
3 Jawhari's clinching argument is that r and o do not occur as the first and
last radicals of any genuine Arabic word.100 FOREIGN VOCABULARY OF THE QITR^AN
This has been recognized by Dvorak, Fmndw, 50, and by
Noldeke, New Beitrage, 48, who shows that JtJP'Ah *7*fl1" #609
7rpoar(f)aTo$, and in ^*fl-|* we have the form we need.
(Jibnl).
ii, 91, 92 ; Ixvi, 4.
Gabriel.
Always as the Angel of Revelation, and by name only in Madinan
passages. (There is possibly a reference to his name ^X'HSS -
" mighty one of God ", in liii, 5, kk one mighty in power.")
There was considerable uncertainty among the early authorities
as to the spelling of the name, for we find
> % >
Ox-
and even ^^>- and ^^^J". 1 as-Suyuti, Minhir, i, 140.
notes that these variants point to its non-Arabic origin, 2 and this
was admitted by some of the philologers, cf. Tab. on ii, 91 ;
al-Jawallqi, 144, and al-Khafaji, GO.
The ultimate origin, of course, is the Heb. /N'HSS, and in
Dan. viii, 16 ; ix, 21, Gabriel is one of the high angels and the agent
of Kevelation, just as he is in the Qur'an. There is, however, the
possibility that the Gabriel of the QurVin is of Christian rather than
Jewish origin, and the form ^y-i^Xy which is found in the Christian
Palestinian dialect, 3 gives us the closest approximation to the usual
Arabic form.
There is some question how well the name was known in Arabia
before Muhammad's time. Gabriel was known and honoured among
the Mandaeans, 4 and this may have been a pre-Islamic element in
their faith. The name occurs also in verses of poets contemporary
with Islam, but seems there to have been influenced by Qur'anic
1 Vide al-Jawaliqi, Alu'arrab, /50, and Haiti, and Zain. on ii, 91.
* Sec also Ibn Qutaiba, Affab nl-Kiitib t 78.
3 Schulthoss, Lex, 34.
4 Brandt, Mandaer, 17, 25 ; JVdzharski, Johannefilmch, xxvi. Tt is interesting
to note that (Inbrall occurs in a Persian Manichaean fragment from Tnrfan ; cf. V.
Midler, MlAW, Berlin, 1904, ]>. 351, Salcnmnn, Manirhafi*c,he Mwtirn, i, 03.FOREKJN VOCABULARY OF THE QUR^AN 101
usage. Cheikho, Nasrdniya, 235, gives an instance of a personal name
containing the word, but Horovitz, KU, 107, rightly insists on the
incorrectness of this. 1 Muhammad seems to have been able to assume
in his Madinan audience some familiarity with the name, and the
probabilities are that it came to him in its Syr. form.
xxxvii, 103,
The temple, or side of forehead.
The sole occurrence of the Avord is in the story of Abraham pre-
paring to sacrifice his son, when he laid him down on his forehead. The
exegetes got the meaning right, but neither they nor the Lexicons
have any satisfactory explanation of the origin of the word from
a root
Barth has suggested an Aramaic origin. WSJ moans brow or
eyebrow, and is fairly common in the Rabbinic writings. Similarly
jla.CLt is eyebrow and a commonly used word. From either of these
it may have been an early borrowing into Arabic.
ix, 29.
Tribute.
The word is used ii, a technical sense in this passage which is late
Madinan, and looks very much like an interpolation in the Qur'iiu
reflecting later usage.
In later Islam < j>- was the technical term for the poll-tax imposed
on the Dhimmis, i.e. members of protected communities (cf. as-Sijistanl,
101). It is usually derived from (j>-, and said to be so called because
it is a compensation in place of the shedding of their blood (so llaghib,
=========
came to the Arabs through the Syr. ]ioLo 3 or the Bth.
especially rfs it was from the Syr. that the Pazend Mushde, Phlv.
and Arm. \* ni -l!r were borrowed.
There appears to be no well-attested example of the use of the
word earlier than the Qur'an, 4 so that it may have been an importation
of Muhammad himself, though doubtless well enough known to his
audience from their contacts with Jews and Christians.
ii, 92.
Michael.
As an angel he is mentioned with Gabriel in a passage where the
Commentators claim that the two are contrasted, Gabriel as the
opponent of the Jews and Michael as their protector. He thus occupies
in the Qur'an the place given him in Dan. x, 13, 21, etc., as the Patron
of Israel.
The early authorities were a little uncertain as to the spelling
of the word, and al-Jawallqi, 143, notes the forms
\ |L ; JuX-w* ; and A^A.-^. This would suggest that it was a
foreign word, and it is given as such by Ibn Qutaiba, Adah al-Katib, '
78> and al-Jawaliqi, op. cit.
The word may have come directly from /JO'VS, or more likely
or ^iuio, as it was from Syriac that the form
1 Raghib gives the form as
2 So Tub. on ii, 48 ; ath-Tha'labi, Qisas, 118, who tell us that in Coptic mu means
water and sha means trees. This obviously rests on the Jewish theory given in Josephus,
Antiq, ii, ix, 6 : TO yap vbcop n& ol Aiyvirrioi KaXovaiv* vcrys 8 rouj ef vSaros
awOevras, which fairly well represents the Coptic JMOOTF water and OV2 rescued.
3 Cf. the form XD1D on a Christian incantation bowl from Nippur (Montgomery,
Aramaic Incantation Texts, p. 231).
So Horovitz, KU, 143 ; JPN, 156.276 FOREIGN VOCABULARY OF THE QUR^AN
in the Persian Manichaean fragments from Turfan was derived. 1 It
is difficult to say how well the name was known in pre-Islamic times. 2
(NaKy).
Of very frequent occurrence, e.g. ii, 247 ; iii, 61 ; viii, 65.
Prophet. * x
Usually the word is taken to be from LJ to bring news (as-Sijistanl,
312), though some thought it was from a meaning of that root to be
high? . .
Fraenkel, Vocab, 20, pointed out that the phi. Jj , beside the
*.
more usual *Lo I, would suggest that the word was a foreign borrowing.
and that it was taken from the older religions has been generally ac-
cepted by modern scholarship. 4 Sprenger, Lebcn, ii, 251, would derive
it from the Heb. *T?3, and this view has commended itself to many
scholars. 5 There are serious objections to it, however, on the ground of
form, and as Wright has pointed out, 6 it is the Aram. K*5?, which
by the dropping of the sign for emphatic state, gives us the form we
need. Thus there can be little doubt that ^ , like Eth. Vd, (Noldeke,
Neue Beitrage, 34), is from the Aram., 7 and probably from Jewish
Aram, rather than from Syr. U^- It was seemingly known to the
Arabs long before Muhammad's day, 8 and occurs, probably of Mani
himself, in the Manichaean fragments (Salemann, Manichaeische
Studien, i, 97).
1 Muller in SBAW, Berlin, 1904, p. 351 ; Salemann, Manichaeische Studien, i, 95.
2 Cf. Horovitz, KU, 143, and Khodokanakis, WZKM, xvii, 282.
3 Ibn Duraid, Ishtiqdq, 273 ; and sec Fraenkel, Fremdw, 232, n.
Margoliouth, Schweich Lectures, 22, however, thinks that the Hebrew is to be
```


## [2026-09-06T22:55:23.939Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg303.png"
}
```


### [2026-09-06T22:55:24.406Z] TOOL RESULT

```

```


## [2026-09-06T22:55:24.404Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:55:40.397Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 303 -l 303 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg303hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg303hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.55),int(h*0.53),int(w*0.80),int(h*0.60))).save('p303_n18.png')\nim.crop((int(w*0.55),int(h*0.21),int(w*0.80),int(h*0.30))).save('p303_n5.png')\n\""
}
```


### [2026-09-06T22:55:43.623Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T22:55:45.786Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p303_n18.png"
}
```


### [2026-09-06T22:55:45.800Z] TOOL RESULT

```

```


## [2026-09-06T22:55:48.811Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg303hi.png'); w,h=im.size\nim.crop((int(w*0.52),int(h*0.58),int(w*0.82),int(h*0.635))).save('p303_n18b.png')\n\""
}
```


### [2026-09-06T22:55:51.382Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:55:53.777Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p303_n18b.png"
}
```


### [2026-09-06T22:55:53.790Z] TOOL RESULT

```

```


## [2026-09-06T22:56:14.502Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"جبرئیل\" \"میکائیل\" \"اسرافیل\" \"عزرائیل\" \"اسماعیل\" \"دانیال\" \"الیاس\" \"بابل\" \"گابریل\" \"اوریئل\" \"الیزه\" \"شانزه\" \"آمانوئل\" \"رافائل\" \"الیزابت\" \"ساموئل\" \"دانیل\"; do echo \"== $w\"; grep -c -- \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


### [2026-09-06T22:56:16.557Z] TOOL RESULT

```
Exit code 1
== جبرئیل
MON_part1.txt:4
MON_part2.txt:1
== میکائیل
MON_part2.txt:0
MON_part1.txt:0
== اسرافیل
MON_part1.txt:2
MON_part2.txt:5
== عزرائیل
MON_part1.txt:3
MON_part2.txt:0
== اسماعیل
MON_part1.txt:9
MON_part2.txt:9
== دانیال
MON_part1.txt:0
MON_part2.txt:0
== الیاس
MON_part2.txt:0
MON_part1.txt:0
== بابل
MON_part2.txt:5
MON_part1.txt:2
== گابریل
MON_part1.txt:0
MON_part2.txt:0
== اوریئل
MON_part1.txt:0
MON_part2.txt:0
== الیزه
MON_part1.txt:0
MON_part2.txt:2
== شانزه
MON_part1.txt:0
MON_part2.txt:0
== آمانوئل
MON_part1.txt:0
MON_part2.txt:0
== رافائل
MON_part1.txt:0
MON_part2.txt:0
== الیزابت
MON_part2.txt:0
MON_part1.txt:0
== ساموئل
MON_part1.txt:0
MON_part2.txt:0
== دانیل
MON_part2.txt:0
MON_part1.txt:0
```


## [2026-09-06T22:56:21.236Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -- \".\\{140\\}جبرئیل.\\{140\\}\" MON_part1.txt | head -5; echo \"---عزرائیل\"; grep -n -o -- \".\\{140\\}عزرائیل.\\{140\\}\" MON_part1.txt | head -4; echo \"---الیزه\"; grep -n -o -- \".\\{100\\}الیزه.\\{100\\}\" MON_part2.txt | head -3"
}
```


### [2026-09-06T22:56:21.334Z] TOOL RESULT

```
---عزرائیل
---الیزه
```


## [2026-09-06T22:56:26.892Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\ndef norm(s):\n    return s.replace('ي','ی').replace('ى','ی').replace('ك','ک').replace('‌','')\nfor f in ['MON_part1.txt','MON_part2.txt']:\n    t=norm(open(f,encoding='utf-8',errors='replace').read())\n    for w in ['جبرئیل','عزرائیل','اسرافیل','بابل','الیزه','اسماعیل']:\n        hits=[m.start() for m in re.finditer(norm(w),t)]\n        print(f,w,len(hits))\n        for h in hits[:2]:\n            print('   ...',t[max(0,h-160):h+160].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T22:56:28.668Z] TOOL RESULT

```
MON_part1.txt جبرئیل 4
   ... ان) روحانی» موبد» راهنما. به پیر!  سوگند به مرشد (اصطلاحات صوفیه که  وارد کلام عامه شده.) پیر چهل ساله: (کد.)  عقل» قوت عاقله که در چهل سالگی کامل  شسود. (اخ.) جبرئیل. (اخ.) آدم(ص).  فبروزه» فبر وز ۳ پبروره. ببر خانقاه: (تص.)  شیح خانقاه» مر شد. پیر خدای: ( کذ.) عثمان  بن عفان. پبر خرابات: بیری که در میکدهها  شراب فروش
   ...  به حرکت و سکون وا دارد.  جیران: م9 [ع.] (مص ع.) تلافی کردن.  (امص.) تلافی.   چسسروت. 202 [ع.] (.) قدرت»  عظمت. عالم قدرت و عظمت الهی» جهان  برین؛ مق. ناسوت.   جبرئیل: :1007 |- جبرائیل - جبریل]  (اخ.) یکی از فرشتگان مقرب. (ا.) دل که به  زعم صوفیان مهبط انوار الهی و محل وحی  و الهام او است.   جیسین: 10 (- جیسین» معر.(.)
MON_part1.txt عزرائیل 3
   ...  بسک الهی: ( کد.) جرثیل. بیکث  چرخ: (کذ.) ماه» قمر. پیک درگاه: (ک.)  جبرگیل. بیکث رایگانی: (کذ.) ماه؛ قمر.  (کد.) سوداگر. راهگذر. ( کد.) باد صبا. یک  رب: (کد.) عزرائیل. پیک سپید و سیاه: شب  و روز. بیک فلکک: (کد.) ماه» قمر. بیکک  مرتب: پیکک باراتبه دایم نه موقت» برید  مرتب. بیک هوابی: ( کذ.) ابر. سحاب.  پیک: »3 (ا.) ورق
   ... ) جان دهنده فدائی.   جان سیر دن: (.9:۳0۲0206662-.(مصل.)  مر دن» موات.   یس نستان: 6057:-.1 [- جسانستاننده)  (رصفا.) حان ستاننده» روج ستاننده» کشنده»  قاتل. صفت عزرائیل» فرشتهای که جان  زندگان را میگیرد.   جانشکر: ۲ما(ع)ه-.]. [- جانشکر نده ]  (صفا.) شکار کننده جان» جانستان.  معشوق دلبر. (اخ.) عزرائیل.  جانشناس: 5 (- جان
MON_part1.txt اسرافیل 2
   ...  و منعکس با یکدیگر به  گوس میرسد و سبب تقویت صوت (و به  اصطلاح پیجیدن صدا) میگر دد؛ صدا.  صور: ۰:0۷ [ع.] (.) شاخ و جز آن که در  آن دمند تا اواز براید» بوق. صور اسرافیل:  شیپور اسرافیل که روز قیامت وی در آن  دمد و مردگان زنده شو ند.   صورت: ادتلاه (ع. صورة] (.) شکل» قیافه.  رخسار» چهره. نقش» تصویر. ظاهرء دید.  (رض.) هر 
   ... گر به  گوس میرسد و سبب تقویت صوت (و به  اصطلاح پیجیدن صدا) میگر دد؛ صدا.  صور: ۰:0۷ [ع.] (.) شاخ و جز آن که در  آن دمند تا اواز براید» بوق. صور اسرافیل:  شیپور اسرافیل که روز قیامت وی در آن  دمد و مردگان زنده شو ند.   صورت: ادتلاه (ع. صورة] (.) شکل» قیافه.  رخسار» چهره. نقش» تصویر. ظاهرء دید.  (رض.) هر کسر مرکب است از 
MON_part1.txt بابل 2
   ...  درخور. از بات در حصوص؛ در  عوض. به حساب. همطراز» همسر » نظیر .  بایزن: ۱0 )۱( سیخ کباب خواه آهت  باشد یا چوبی.   بابک: ۱2۳-۴ [مصف. باب] (.) پدر (به  تحبیب).   بابل: ۵1 (.) مغرب؛ مق. خراسان به  معنی مشر ق.   بابو: 205 رقس. باب] (.) پدر بابا. بزرگ  قلندران و درویشان. به معنی بابا که در اوایل  اسماء برای شفقت با مجرد تلق
   ... ن» آرزو داشتن. (.) آرزو)  ج. تمنیات.  تموج: لجوصها [ع.] (مصل.) موج زدن»  خیزاب براآوردن» موجدار شدن. (امسص.)  موجزنی؛ ج. تموجات.  تمور: ۱20012 ,۱2012 [معر. سر. بابلی ]  گرمای سخت. نام ماه اول تاستان و ماه دهم  از سال رومیان. تابستان» فصل گرما.  تموک: ۱۵۳16 )٩(‏ قسمی تیر که دارای  پیکان بهن است. نشانةٌ تبر هدف.  تمول: ۱
MON_part1.txt الیزه 0
MON_part1.txt اسماعیل 9
   ...   سوش و ریشة آن بوی معطر دارد و در طب  به عنوان مسهل و مقیی مصرف میگردد.  اساس: 5 [ع.] (.) پی؛ پابه» بنباد»  شالده» بن» ننبان» پیکره» اصل. اصطلاحی  است در مذهب اسماعیلیه و آن عنوان کسی  است که در زامن هر سلسله از سلسلههای  «صامت» (امام) قرار دارد.   اساسا: «-«292 [ع.] (ق.) از بسن از پای  ست, از یابه» از اصل؛ از ننیاد. 
   ... ) نزد شیعهٌ اثناعشری هر یک از دوازده  پیشوا که نخستین آنان علی بن ابیطالب و  آخرین آنان مهدی(ع) است (یازده تن اخیر  از سل علی(ع) و فاطمه دختر  محمد(ص)اند.) نزد اسماعیلیه» هر یک از  هفت پیشوا که شش تن نخستین همان شش  امام اول شیعه اثناعشری هستند و هفتمین  اسماعیل این جعفر صادق(ع) باشد. (تص.)  تطب» شیخ؟ ج. ایمه (ائمه). ا
MON_part2.txt جبرئیل 1
   ...   ناکث: ۱2۳ [ع.] (افا.) برهم رننده»  گسلنده. عهدشکن» پیمانشکن؛ ج. ناکثین  ناک حااباد: 72012-20240 (امر.)  شهابالدین سهروردی در حکمة الاشراق  در رسالةٌ «آواز پر جبرئیل» این اصطلاح را    نا کح فرهنگ فارسی معین ۱۹۰۳    در برایر (لامکان) آورده. (روابط حکمت  اشراق و فلسفة ایران باستان. کرین قسمت  فرانسوی. ص 1 ح. ۵ ۵).  ناکح
MON_part2.txt عزرائیل 0
MON_part2.txt اسرافیل 6
   ... 2۷6 [ع.] (.) فر شته» ج. ملائکک  (ملایک)» ملاثکه (ملایکه). ملکک مقرب:  فرشتهای که نزدیکک به آستان حضرت حق  است. عدد این گونه فرشتگان در اسلام جها  راست: جراثیل» اسرافیل» مبکائیل»  عزراشل و در دین زردشت هفت و در دین  بهود نیز هفت است. (فد.) صدرالدین    شیرازی عقل اول را ملک مقرب و عقول  طویله را ملائکةٌ مقربین نامیده به 
   ... قیام  به حق (فر ع. سبح .) نفخ معده: (امر.) (بزر.)  تجمع گاز در معده» و جود دمش در معده.  نفخه: (0-)226۵ (ع. نخفة] (مصم.) یک  بار دمیدن با دهان» دم و غبره. نفخه اسرافیل  (اسرافیلی): دمیدن اسرافیل در صور نفخة  صور. یک بار باد کردن. (مصل.) پر شدن  شکم از باد. (ا.) (پز.) ورم بادی سخت؛ ورم  ریحیء آماس شکم. نفخ روح: دمی که  
MON_part2.txt بابل 5
   ... صی که  همه روز زیر درخت امرود بلمد و کاری  کاهل. 261 [ع.] (.) میان دو شانه» بشت  گردن؛ ج. کواهل.   کاهن: ۲2۰۰ (ع.| (ص.) فا لگیر» غی بگو.  روحانی مصریان باستان» بابلیان و یهودیان)  ج. کهنه.   کاهو: تت (- کوک] (.) (گیا.) گیاهی  است از تیره مرکبان که یکساله است ولی  دارای برخی انواع دو ساله و بایا نیز میباشد.  در ساقه و ب
   ... و گوشههای لب فرو ریزد و یرون  | بد.   لیر : ۱ (از بو.] (.) (مس.) سازی است دارای  سیمهای آزاد که سابقةٌ آن به یونان باستان  میرسد و نمونههایی از آن نیز در نقوش  بابل و اشور موجود است. صورت ابتدایی  این ساز به شکل مثلث بوده است با چهار  سیم که به موازات قاعده به دو ضلع مثلث  متصل است.   لیرت: (قد.-108 ,100 ۱- لیرد] (.) خ
MON_part2.txt الیزه 2
   ... فحص کننده؛  تجسس کننده. کننده» حفار. بحث کننده.    ستیز ه کننده.   کاونه: (۵-)2۷۵۲۸ (۱.) (جان.) جانورکی  است سرخ و زهردار و بر او خالهای سیاه  باشد و بیشتر در فالیزها بهم رسد و خریزه را  کاوی: ۲۵ (ع.](.) (پز.) دارویی که سب  سوختن و ضمناً تصلب دهانةٌ عروق و محل  بریدگی و زخم در انساج بشود و بالنتیجه  مجاری عروق را بهم آ
   ...  نایژه  باشد.    لولو: تات! (.) صورت مهیبی که برای    ترسانیدن کودکان سازند. وجودی وهمی که  کودکان را بدان ترسانند؛ لولو خرخره.  لولو(ی) سر خرمن: مترسکی که در جالیزها  و مزارع نصب کنند تا پرندگان و جانوران  بترسند و به مزرعه آسیب نرسانند. (کد.)  شخص ییفواره و مهیب.   لولو: تلا (- لوالو - لوالوا] (ص.) سبکت»  بیو قار.   
MON_part2.txt اسماعیل 9
   ... اتق  )1( (اسماعنلید) سسن هر دو تن از ناطقان هفت  صامت و اسطه هستند که ات هر یک از  تسار اش عد د ۳ را «فاتق» تًِ «راساس»  بانتت: فا تقان عار 7 ۳ از : شنت ) سام: اسماعیل   (پسر هاجر). هارون؛ بطرس (حواری).  علی(ع) و بجای هفتمین یکی از موٌسسان  فرق سعیه را نام پرند مانند عبدالله ببن    سمون.   فاتک: ۱۳۸ (ع.| (ص   فتا کک.  
   ... (امص.) پیدایی؛ برداشتگی پرده از  روی چیزی. (تص.) ظهور عوالم معنوی و  حقایق جهان باطن بر سالکک. (عر.) نوعی  زحاف که عبارت است از اسقاط تاء  «مفعولات». دور کشف: (اسماعیلیه) عهدی  که در آن حقایق آشکار شود؛ مق. دور ستر.  کشفت: ۲5۸۱ (ص.) پراکنده؛ پر بشان.  (فع.) سوم شخص مفرد ماضی از « کشفتن».  کشفتن: ۲:۱۵ (- شگفتن - شکافتن
```


## [2026-09-06T22:56:44.211Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-06T22:56:44.255Z] TOOL RESULT

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


## [2026-09-06T22:56:53.089Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔil-\" \\\n \"https://en.wiktionary.org/wiki/אל\" \\\n \"https://en.wiktionary.org/wiki/אלהים\" \\\n \"https://en.wiktionary.org/wiki/إله\" \\\n \"https://www.etymonline.com/word/Elysium\" \\\n \"https://www.etymonline.com/word/Israel\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 303, root Layh/A.l.h (Semitic *ʔil-), checking El/Elohim/ilāh and Elysium/Israel\" ; done"
}
```


### [2026-09-06T22:56:58.627Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bf360eda76657501.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce9a071129e4f623.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bfd73104faff0f10.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ece87052a052772b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30f80976f4bc95e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d3ef7c82760eb268.txt
```


## [2026-09-06T22:57:00.863Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in bf360eda76657501 30f80976f4bc95e2 d3ef7c82760eb268; do echo \"########## $f\"; head -c 3000 $f.txt; echo; done"
}
```


### [2026-09-06T22:57:02.686Z] TOOL RESULT

```
########## bf360eda76657501
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔil-
FETCHED: 2026-09-06T22:56:55Z
STATUS: 200
TITLE: Reconstruction:Proto-Semitic/ʔil- - Wiktionary, the free dictionary

Reconstruction:Proto-Semitic/ʔil- - Wiktionary, the free dictionary 

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
 Proto-Semitic 

 Toggle Proto-Semitic subsection 

 1.1 
 Noun 

 1.1.1 
 Inflection 

 1.1.2 
 Coordinate terms 

 1.1.3 
 Descendants 

 Toggle the table of contents 

 Reconstruction:Proto-Semitic/ ʔil- 

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

 This Proto-Semitic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Semitic
 [ edit ] 

 English Wikipedia has an article on: El (deity) 

 Wikipedia 

 English Wikipedia has an article on: Ilah 

 Wikipedia 

 Noun
 [ edit ] 

 *ʔil-   m 

 deity , god 

 Inflection
 [ edit ] 

 Declension of *ʔil- 

 case

 singular

 dual

 plural

 nominative 

 *ʔilum

 *ʔilāna

 plural stem + *-ūna

 accusative 

 *ʔilam

 *ʔilayna

 plural stem + *-īna

 genitive 

 *ʔilim

 possessive forms

 1 st person

 *ʔilī / *ʔilVya

 —

 *ʔilVni

 2 nd person m 

 *ʔilVka

 *ʔilVkumā / *ʔilVkumay

 *ʔilVkum(ū)

 2 nd person f 

 *ʔilVki

 *ʔilVkin(ā)

 3 rd person m 

 *ʔilVšu

 *ʔilVšumā / *ʔilVšumay

 *ʔilVšum(ū)

 3 rd person f 

 *ʔilVša

 *ʔilVšin(ā)

 the endings - m and - na are dropped in the bound form , which may also undergo syncopation of an unstressed final vowel where possible.
Note: the ending - V before the possessive endings responds to case: *ʔiluya for nom. case, *ʔiliya for gen. case, *ʔilaya for acc. case, etc.

 Coordinate terms
 [ edit ] 

 *ʔilāhat- 

 Descendants
 [ edit ] 

 East Semitic:
 Akkadian: 𒀭 ( ilum ) 

 West Semitic:
 Central Semitic:
 Arabic: إِلّ ( ʔill ) 

 Northwest Semitic:
 Aramaic: אֵיל ( ʾēl ) 
 Samaritan Aramaic: ࠀࠢࠋ ( ʾĕl ) , ࠀࠜࠋࠠࠄ ( ēla ) , ࠀࠝࠋࠦࠄࠉ࠙ࠝࠌࠬ ( ʾelūwem ) 

 Canaanite:
 Ammonite: 𐤀𐤋𐤌 ( ʾlm ) 

 Hebrew: אֵל ( el, ʾēl ) 

 Phoenician: 𐤀𐤋 ( ʾl ) , 𐤀𐤋𐤕 ( ʾl
########## 30f80976f4bc95e2
URL: https://www.etymonline.com/word/Elysium
FETCHED: 2026-09-06T22:56:58Z
STATUS: 200
TITLE: Elysium - Etymology, Origin & Meaning

Elysium - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of Elysium 

 Elysium (n.) 

 1590s, from Latin Elysium , from Greek Ēlysion (pedion) "Elysian field," abode of the blessed after death, where heroes and the virtuous dwell, which is of unknown origin, perhaps from Pre-Greek (a non-IE substrate Mediterranean language). Also used figuratively of a situation of complete happiness.
 also from 1590s 

 Entries linking to Elysium 

 Elysian (adj.) 

 1570s, "pertaining to Elysium (q.v.), the abode of the blessed after death." Hence, "exquisitely happy, full of the highest bliss."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 heaven 

 Old English heofon "home of God," earlier "the visible sky, firmament," probably from Proto-Germanic *hibin-, a dissimilation of *himin- (source also of Low German heben, Old Norse himinn, Gothic himins, Old Frisian himul, Dutch hemel, German Himmel "heaven, sky"), which is of un

 counsel 

 c. 1200, "advice or instruction given;" c. 1300, "mutual advising or interchange of opinions, consultation," from Old French counseil "advice, counsel; deliberation, thought" (10c.), from Latin consilium "plan, opinion," from assimilated form of com "with, together" (see con-) + 

 method 

 early 15c., "regular, systematic treatment of disease," from Latin methodus "way of teaching or going," from Greek methodos "scientific inquiry, method of inquiry, investigation," originally "pursuit, a following after," from meta "in pursuit or quest of" (see meta-) + hodos "a m

 Jehovah 

 1530, Tyndale's transliteration of Hebrew Tetragrammaton YHWH using vowel points of Adhonai "my lord" (see Yahweh). Used for YHWH (the full name being too sacred for utterance) in four places in the Old Testament in the KJV where the usual translation the lord would have been inc

 prism 

 1560s, in geometry, "a solid whose bases or ends are any similar, equal, and parallel plane polygons, and whose sides are parallelograms" (not always triangular), from Late Latin prisma, from Greek prisma "a geometrical prism, trilateral column," (Euclid), literally "something sa

 Nicholas 

 masc. proper name, from French Nicolas, from Latin Nicholaus, Nicolaus, from Greek Nikolaos, literally "victory-people," from nikē "victory" (see Nike) + laos "people" (see lay (adj.)). The saint associated with Christmas (died 326 C.E.) was a bishop of Myra in Lycia, patron of s

 fret 

 Old English fretan "devour, feed upon, consume," from Proto-Germanic compound *fra-etan "to eat up," from *fra- "completely" (from PIE root *per- (1) "forward," hence "through") + *etan "to e
########## d3ef7c82760eb268
URL: https://www.etymonline.com/word/Israel
FETCHED: 2026-09-06T22:56:58Z
STATUS: 200
TITLE: Israel - Etymology, Origin & Meaning of the Name

Israel - Etymology, Origin & Meaning of the Name 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of Israel 

 Israel 

 Old English Israel , "the Jewish people, the Hebrew nation," from Latin Israel , from Greek, from Hebrew yisra'el "he that striveth with God" (Genesis xxxii.28), symbolic proper name conferred on Jacob and extended to his descendants, from sara "he fought, contended" + El "God." As the name of an independent Jewish state in the Middle East, it is attested from 1948. Compare Israeli , Israelite .

 Entries linking to Israel 

 Israeli (n.) 

 "citizen of the state of Israel," 1948, from Israel + Hebrew national designation suffix -i . Also used in English as the adjective (1948). It distinguishes the citizens of the modern state from the ancient people who had been known in English since 14c. as Israelites (see Israelite ).

 Israelite (n.) 

 mid-14c., "a Jew; one of the people of ancient Israel, a descendant of Israel or Jacob," from Latin israelita , from Greek Israelites , from Israel (see Israel ). The Middle English adjective was Israelish (Old English Israelisc ), sometimes Israelitish (Coverdale, 1530s); Israelitic (c. 1600, from Late Latin Israeliticus ).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 manna 

 tree," but used in Greek and Latin specifically with reference to the substance miraculously supplied to the Children of Israel...

 theocracy 

 which God is recognized as supreme ruler and his laws form the statute book," originally of the sacerdotal government of Israel...

 shamus 

 The word is said to be probably from Yiddish shames, literally "sexton of a synagogue" (according to Israel Zangwill "a potent...

 Solomon 

 masc. proper name, Biblical name of David's son and successor as king of Judah and Israel and wisest of all men, from Greek...

 Seven Seas 

 or sometimes in reference to seven seas forming part of the Hindu cosmology or to the Talmudists' supposed seven seas of Israel...

 philistine 

 German Philister "enemy of God's word," literally "Philistine," inhabitants of a Biblical land, neighbors (and enemies) of Israel...

 Arcturus 

 In Israel and Arabia, the seven stars of the Great Bear seem to have been a bier (the "bowl") followed by three mourners....

 race 

 [act of running] late Old English, also rase, "a narrative, an account;" c. 1300, "an act of swift running, a hurried attack," also "a course of life or conduct, a swift current;" from Old Norse rās "a running, a rush (of water)," cognate with Old English ræs "a running, a rush, 

 acre 

 Old English æcer "tilled field, open land," from Proto-Germani
```


## [2026-09-06T22:57:09.198Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f in ['ce9a071129e4f623','bfd73104faff0f10','ece87052a052772b']:\n    t=open(f+'.txt',encoding='utf-8').read()\n    i=t.find('From Wiktionary')\n    print('#########',f, t.split('\\n')[0])\n    print(re.sub(r'\\n{2,}','\\n',t[i:i+3500]))\nEOF"
}
```


### [2026-09-06T22:57:12.241Z] TOOL RESULT

```
######### ce9a071129e4f623 URL: https://en.wiktionary.org/wiki/אל
From Wiktionary, the free dictionary
 See also: אל־ and ﭏ 
 Arabic
 [ edit ] 
 Noun
 [ edit ] 
 אל • ( ʔāl )  m 
 Judeo-Arabic spelling of آل ( ʔāl , “ family ” ) ‎‎
 c. 10th century , Saadia Gaon , Tafsir ‎ [1] , Exodus 1:1: הדׄה אסמא בני אסראיל אלדאכׄלין אלי מצר מע יעקוב רגׄל ואלה דכׄלו׃ hāḏihi ʔasmāʔu banī ʔisrāʔīla d-dāḵilīna ʔilā miṣra maʕa yaʕqūba rajulun wa-ʔāluhu daḵalū. These are the names of the sons of Israel entering Egypt. With Jacob, man and his kin entered: 
 Hebrew
 [ edit ] 
 Etymology 1
 [ edit ] 
 Root 
 א־ל ( ʾ-l ) 
 7 terms 
 From Proto-Semitic *ʔil- . Cognate with Akkadian 𒀭 ( ilum ) , Arabic إِل ( ʔil ) , إِلَٰه ( ʔilāh ) , Aramaic אלה ( aláh ) .
 Pronunciation
 [ edit ] 
 ( reconstructed Biblical ) IPA ( key ) : /ʔil/ 
 ( Tiberian ) IPA ( key ) : /ˈʔeːl/ , [ˈʔeː.el] 
 ( Yemenite ) IPA ( key ) : /ˈʔel/ , [ˈʔeːl] 
 ( Persian ) IPA ( key ) : /(ʔ)el/ 
 ( Ashkenazi ) IPA ( key ) : /ejl/ 
 ( Modern Israeli ) IPA ( key ) : /(ʔ)el/ 
 Noun
 [ edit ] 
 אֵל • ( el )  m ( plural indefinite אֵלִים , singular construct אֵל־ , plural construct אֵלֵי־ , feminine counterpart אֵלָה ) 
 god ( a deity or supreme being ; a supernatural , typically immortal , being with superior powers , to which personhood is attributed ) 
 Declension
 [ edit ] 
 Declension of אֵל 
 isolated forms
 with possessive pronouns
 Number: 
 State: 
 form
 Person: 
 singular 
 plural
 m 
 f 
 m 
 f 
 singular 
 indefinite
 אֵל 
 first
 אֵלִי 
 אֵלֵנוּ 
 definite
 הָאֵל 
 second
 אֵלְךָ 
 אֵלֵךְ 
 אֵלְכֶם 
 אֵלְכֶן 
 construct
 אֵל־ 
 third
 אֵלוֹ 
 אֵלָהּ 
 אֵלָם 
 אֵלָן 
 plural 
 indefinite
 אֵלִים 
 first
 אליי / אֵלַי 
 אֵלֵינוּ 
 definite
 הָאֵלִים 
 second
 אֵלֶיךָ 
 אלייך / אֵלַיִךְ 
 אֵלֵיכֶם 
 אֵלֵיכֶן 
 construct
 אֵלֵי־ 
 third
 אֵלָיו 
 אֵלֶיהָ 
 אֵלֵיהֶם 
 אֵלֵיהֶן 
 Proper noun
 [ edit ] 
 אֵל • ( el )  m 
 God , the God of Israel .
 El , the chief deity in Canaanite religion
 Derived terms
 [ edit ] 
 אֶלְעָד ( el'ad ) 
 אֶלְעָזָר ( el'azár ) 
 אֲרִיאֵל ( ari'él ) 
 גַּבְרִיאֵל ( gavri'él ) 
 מִיכָאֵל ( mikha'él ) 
 See also
 [ edit ] 
 אלוה 
 אל שדי 
 אלישבע 
 Etymology 2
 [ edit ] 
 From Proto-Semitic *ʾila ( “ towards, nigh ” ) , cognate with Akkadian 𒀀𒈾 ( ana ) , Arabic إِلَى ( ʔilā ) .
 Pronunciation
 [ edit ] 
 ( Tiberian ) IPA ( key ) : /ʔɛl/ , [ʔɛl] 
 ( Yemenite ) IPA ( key ) : /ʔal/ , [ʔæl] 
 ( Persian ) IPA ( key ) : /(ʔ)el/ 
 ( Ashkenazi ) IPA ( key ) : /ɛl/ 
 ( Modern Israeli ) IPA ( key ) : /(ʔ)el/ 
 Preposition
 [ edit ] 
 אֶל • ( el ) 
 to , towards , into 
 at , by 
 Inflection
 [ edit ] 
 Inflection table
 base form
 אֶל ( el ) 
 Personal-pronoun-
including forms
 singular
 plural
 m 
 f 
 m 
 f 
 1 st person
 אליי / אֵלַי ( elái ) 
 אֵלֵינוּ ( eléinu ) 
 2 nd person
 אֵלֶיךָ ( elékha ) 
 אלייך / אֵלַיִךְ ( eláyikh ) 
 אֲלֵיכֶם ( aleikhém ) 1 
 אֲלֵיכֶן ( aleikhén ) 1 
 3 rd person
 אֵלָיו ( eláv ) 
 אֵלֶיהָ ( eléha ) 
 אֲלֵיהֶם ( aleihém ) 1 
 אֲלֵיהֶן ( aleihén ) 1 
 In Modern Hebrew, the second- and third-person plural forms are usually pronounced with leading /e/ rather than /a/.
 See also
 [ edit ] 
 אל נכון 
 El Al on Wikipedia. Wikipedia 
 Etymology 3
 [ edit ] 
 Cognate with Phoenician 𐤀𐤋 ( ʾl ) , Ugaritic 𐎀𐎍 ( ảl ) , Akkadian 𒌑𒌌 ( ul ) .
 Pronunciation
 [ edit ] 
 ( Tiberian ) IPA ( key ) : /ʔal/ , [ʔal] 
 ( Yemenite ) IPA ( key ) : /ʔal/ , [ʔæl] 
 ( Persian ) IPA ( key ) : /(ʔ)æl/ 
 ( Ashkenazi ) IPA (
######### bfd73104faff0f10 URL: https://en.wiktionary.org/wiki/אלהים
From Wiktionary, the free dictionary
 Hebrew
 [ edit ] 
 Pronunciation
 [ edit ] 
 Audio : ( file ) 
 Proper noun
 [ edit ] 
 אֱלֹהִים • ( elohím )  m   pl ( singular construct אֱלֹהֵי־ ) 
 defective spelling of אלוהים .
 Tanach , Psalms 82:1 , with translation of the Jewish Publication Society The value tsrc=JPS is ambiguous and deprecated. After checking the translation, please replace it with JPS1917 , JPS1985 , or JPS2023 . See the documentation . : אֱֽלֹהִ֗ים נִצָּ֥ב בַּעֲדַת־אֵ֑ל בְּקֶ֖רֶב אֱלֹהִ֣ים יִשְׁפֹּֽט׃ ’ĕlōhîm niṣāḇ ba‘ăḏaṯ-’êl; bəqereḇ ’ĕlōhîm yišpōṭ God stands in the divine assembly; among the divine beings He pronounces judgment. 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=אלהים&oldid=85464886 "
 Categories : Hebrew terms with audio pronunciation 
 Hebrew lemmas 
 Hebrew nouns 
 Hebrew pluralia tantum 
 Hebrew masculine nouns 
 Hebrew defective spellings 
 Hebrew terms with quotations 
 Hidden categories: Hebrew noun entries missing plural forms 
 Hebrew noun entries missing plural construct forms 
 Pages with entries 
 Pages with 1 entry 
 Hebrew links with redundant alt parameters 
 This page was last edited on 5 July 2025, at 14:48.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct 
 Developers 
 Statistics 
 Cookie statement 
 Mobile view 
 Search 
 Search 
 Toggle the table of contents 
 אלהים 
 15 languages 
 Add topic
######### ece87052a052772b URL: https://en.wiktionary.org/wiki/إله
From Wiktionary, the free dictionary
 See also: أله , اله , آله , and آلة 
 Arabic
 [ edit ] 
 Root 
 ء ل ه ( ʔ l h ) 
 10 terms 
 Alternative forms
 [ edit ] 
 إِلَاه ( ʔilāh ) 
 Etymology
 [ edit ] 
 From Proto-Semitic *ʔil- with a vocative suffix ـَاه ( -āh ) which is else only sporadically attested in Arabic but has left its trace in the -ā vocatives of أَب ( ʔab , “ father ” ) , أَخ ( ʔaḵ , “ brother ” ) , حَم ( ḥam , “ father-in-law ” ) . 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ʔi.laːh/ 
 Egypt: IPA ( key ) : [ʔeˈlæːh] 
 Levant: IPA ( key ) : [ʔɪˈlaːh] 
 Central Arabia: IPA ( key ) : [ʔɪˈlæːh] 
 Hijazi: IPA ( key ) : [ʔɪˈlaːh] 
 Persian Gulf: IPA ( key ) : [ʔɪˈlɑːh] 
 Tunisia: IPA ( key ) : [ʔiˈle̞ːh] 
 Algeria: IPA ( key ) : [ʔiˈlæːh] 
 Morocco: IPA ( key ) : [ʔiˈlæːh] 
 Noun
 [ edit ] 
 إِلٰه • ( ʔilāh )  m ( plural آلِهَة ( ʔāliha ) , feminine إِلٰهَة ( ʔilāha ) ) ( countable ) 
 a god , a deity , a divinity 
 Synonym: رَبّ ( rabb , “ lord; master ” ) 
 609–632 CE , Qur'an , 28:88 : وَلَا تَدْعُ مَعَ اللَّٰهِ إِلَٰهًا آخَرَ ۘ لَا إِلَٰهَ إِلَّا هُوَ walā tadʕu maʕa llāhi ʔilāhan ʔāḵara lā ʔilāha ʔillā huwa And do not call upon another god beside Allah: there is no god but He. 
 Declension
 [ edit ] 
 Declension of noun إِلٰه ( ʔilāh )
 singular
 basic singular triptote 
 indefinite
 definite
 construct
 informal
 إِلٰه 
 ʔilāh 
 الْإِلٰه 
 al-ʔilāh 
 إِلٰه 
 ʔilāh 
 nominative
 إِلٰهٌ 
 ʔilāhun 
 الْإِلٰهُ 
 al-ʔilāhu 
 إِلٰهُ 
 ʔilāhu 
 accusative
 إِلٰهًا 
 ʔilāhan 
 الْإِلٰهَ 
 al-ʔilāha 
 إِلٰهَ 
 ʔilāha 
 genitive
 إِلٰهٍ 
 ʔilāhin 
 الْإِلٰهِ 
 al-ʔilāhi 
 إِلٰهِ 
 ʔilāhi 
 dual
 indefinite
 definite
 construct
 informal
 إِلٰهَيْن ‎; إلَاهَيْن 
 ʔilāhayn ‎; ʔilāhayn 
 الْإِلٰهَيْن ‎; الْإلَاهَيْن 
 al-ʔilāhayn ‎; al-ʔilāhayn 
 إِلٰهَيْ ‎; إلَاهَيْ 
 ʔilāhay ‎; ʔilāhay 
 nominative
 إِلٰهَانِ ‎; إلَاهَانِ 
 ʔilāhāni ‎; ʔilāhāni 
 الْإِلٰهَانِ ‎; الْإلَاهَانِ 
 al-ʔilāhāni ‎; al-ʔilāhāni 
 إِلٰهَا ‎; إلَاهَا 
 ʔilāhā ‎; ʔilāhā 
 accusative
 إِلٰهَيْنِ ‎; إلَاهَيْنِ 
 ʔilāhayni ‎; ʔilāhayni 
 الْإِلٰهَيْنِ ‎; الْإلَاهَيْنِ 
 al-ʔilāhayni ‎; al-ʔilāhayni 
 إِلٰهَيْ ‎; إلَاهَيْ 
 ʔilāhay ‎; ʔilāhay 
 genitive
 إِلٰهَيْنِ ‎; إلَاهَيْنِ 
 ʔilāhayni ‎; ʔilāhayni 
 الْإِلٰهَيْنِ ‎; الْإلَاهَيْنِ 
 al-ʔilāhayni ‎; al-ʔilāhayni 
 إِلٰهَيْ ‎; إلَاهَيْ 
 ʔilāhay ‎; ʔilāhay 
 plural
 broken plural triptote in ـَة ( -a ) 
 indefinite
 definite
 construct
 informal
 آلِهَة 
 ʔāliha 
 الْآلِهَة 
 al-ʔāliha 
 آلِهَة 
 ʔālihat 
 nominative
 آلِهَةٌ 
 ʔālihatun 
 الْآلِهَةُ 
 al-ʔālihatu 
 آلِهَةُ 
 ʔālihatu 
 accusative
 آلِهَةً 
 ʔālihatan 
 الْآلِهَةَ 
 al-ʔālihata 
 آلِهَةَ 
 ʔālihata 
 genitive
 آلِهَةٍ 
 ʔālihatin 
 الْآلِهَةِ 
 al-ʔālihati 
 آلِهَةِ 
 ʔālihati 
 Related terms
 [ edit ] 
 أُلُوهِيَّة ( ʔulūhiyya , “ godhood , divinity ” ) 
 إِلَٰهِيَّات ( ʔilāhiyyāt , “ theology ” ) 
 إِلَٰهِيّ ( ʔilāhiyy , “ divine ” ) 
 إِلٰهَة ( ʔilāha ) 
 اللَّات ( al-lāt , “ Allat ” ) 
 ٱللَّٰه ( allāh , “ God ” ) 
 Descendants
 [ edit ] 
 → Azerbaijani: ilah 
 → Bashkir: илаһ ( ilah ) 
 → Northern Kurdish: îlah 
 → Malay: ilah 
 → Indonesian: ilah 
 → Persian: اله ( elâh ) 
 → Ottoman Turkish: الاه ( ilâh ) 
 > Turkish: ilah ( inherited ) 
 → Uyghur: ئىلاھ ( ilah ) 
 → Uzbek: iloh 
 References
 [ edit ] 
 Bauer, Hans ( 1915 ), “Semitische Sprachprobleme. 5. Die Verwandtschaftsnamen und ilāh „Gott“ im Semitischen. 6. Die Entstehung des semitischen
```


## [2026-09-06T22:57:22.979Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ndef find(pat,maxn=2,ln=560):\n    for i,l in enumerate(leaves):\n        for m in list(re.finditer(pat,l))[:1]:\n            print(f'### leaf {i} /{pat}/')\n            print(l[m.start():m.start()+ln].replace('\\n',' '));print()\n            maxn-=1\n            if maxn<=0: return\nfind(r'Elizabeth,  fem\\.')\nfind(r'Elisha,')\nfind(r'bethel,  n|Bethel,  n')\nfind(r'Daniel,  masc|Daniel,  1\\)')\nfind(r'Raphael,  masc|Raphael,  1\\)')\nfind(r'Elohim,  n\\.')\nfind(r'Azrael')\nfind(r'Ishmael,  masc|Ishmael,  1\\)')\nfind(r'Babylonia')\nEOF"
}
```


### [2026-09-06T22:57:24.957Z] TOOL RESULT

```
### leaf 99 /bethel,  n|Bethel,  n/
bethel,  n.,  a  house  of  worship.  —  Heb.  beth  El, ‘the  house  of  God’.  Beth  is  the  state  construct of  bdyith,  ‘house’,  and  rel.  to  Aram,  baythd, bethd,  Ugar.  bt,  Arab,  bayt,  Akkad,  bitu, ‘house’;  cp.  beth,  beta.  Cp.  also  Basque  baita, ‘house’.  For  the  second  element  see  El.  Cp. baetulus,  baetyl. Bethesda,  n.,  a  pool  at  Jerusalem;  a  chapel.  — Gk.  Bij&eaSd,  fr.  Aram,  beth  hesdd,  ‘house  of mercy’.  See  bethel  and  Hasidim  and  cp.  beth, beta. bethink,  reflex,  v.  —  ME.  bethenehen,  fr.  OE. be

### leaf 221 /Daniel,  masc|Daniel,  1\)/
Daniel,  masc.  PN.,  the  hero  of  the  Book  of  Da- 401 niel  (Bible).  —  Heb.  Ddni'il,  lit.  ‘God  is  my judge’,  rel.  to  Akkad.  Ddnilu.  For  the  first  ele¬ ment  see  Dan,  PN.,  for  the  second  see  El. dank,  adj.,  moist,  damp.  —  ME.  danke,  of  Scand. origin;  cp.  Swed.  dank,  ‘moist  place’,  ddnka, ‘to  moisten’,  which  are  rel.  to  OS.  dunkar, OFris.  diunk,  ‘dark’,  ON.  dokkr,  Du.  donker, OHG.  tunkal ,  dunkal,  MHG.  tunkel,  G.  dunkel, of  s.m.,  and  to  OHG.,  MHG.  damph,  MDu., Du.  damp,  ‘vapbr’.  See  da

### leaf 692 /Raphael,  masc|Raphael,  1\)/
Raphael,  1)  masc.  PN.  2)  an  archangel  mention¬ ed  in  the  Apocrypha.  —  Late  L.,  fr.  Gk.  'Piora- y{k,  fr.  Heb.  R^pha’el,  lit.  ‘God  has  healed’.  Heb. raphd,  ‘he  healed’  (whence  riphu'ah,  ‘medicine, remedy’,  marpe,  ‘healing,  cure’),  the  first  ele¬ ment  of  this  compound  word,  is  rel.  to  Syr. repha,  ‘he  healed’,  Arab,  rafa'a,  ‘he  darned, mended,  repaired’,  Ethiop.  rafaa,  ‘he  stitched together,  mended’.  For  the  second  element  in Raphael  see  El. Raphalesque,  Raffaelesque,  adj.,  in  the  style  of t

### leaf 278 /Elohim,  n\./
Elohim,  n.,  one  of  the  names  of  God  in  the  Bible. —  Heb.  Elohim,  pi.  of  El6ah,  ‘God’,  of  un¬ certain  etymology;  possibly  enlarged  fr.  El.  w See  El.  Cp.  Aram.  Eldh,  in  the  emphatic  state Elahd,  Syr.  Allahd;  Arab,  lldh,  with  the  article, A  llihu  (see  Allah). eloign,  eloin,  tr.  v.,  to  remove  to  a  distance.  —  F. eloigner,  fr.  OF.  esloignier,  fr.  Late  L.  exlongdre, elongare,  ‘to  remove,  keep  aloof’,  which  is formed  fr.  L.  ex,  e,  ‘out  of’  (see  e-),  and  longe, ‘far  off’,  adv.  of  long

### leaf 9 /Babylonia/
Babylonian Deut. Deuteronomy bacteriol. bacteriology dial. dialect,  dialectal B.C.E. 

### leaf 34 /Babylonia/
Babylonia, al-,  assimilated  form  of  ad-  before  /. -al,  suff.  forming  adjectives,  as  in  royal,  or  sub¬ stantives  of  adjectival  origin,  as  in  rival.  — Either  fr.  F.  -al,  -el,  or  directly  fr.  L.  adj.  suff. -alis.  In  many  cases  the  suff.  -alls  was  used  al¬ ready  in  Latin  both  adjectivally  and  substanti¬ ally  (cp.  L.  rival  is,  ‘pertaining  to  a  brook ;  one who  uses  the  same  brook;  neighbor;  competi¬ tor,  rival’,  and  see  rival).  Cp.  the  suffixes  -ial and  -ar. -al,  suff.  forming  verbal  nou
```


## [2026-09-06T22:57:34.948Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,pat in [(277,r'Elisha'),(277,r'Elizabeth'),(442,r'Ishmael'),(453,r'Ishmael'),(34,r'Babylon,'),(84,r'Babylon')]:\n    l=leaves[i]\n    for m in list(re.finditer(pat,l))[:2]:\n        print(f'### leaf {i} /{pat}/ @{m.start()}')\n        print(l[m.start():m.start()+520].replace('\\n',' '));print()\nEOF"
}
```


### [2026-09-06T22:57:36.989Z] TOOL RESULT

```
### leaf 277 /Elisha/ @9172
Elishah,  1)  masc.  PN.;  2)  in  the  Bible,  an  Israelite prophet,  disciple  and  successor  of  Elijah.  — Heb.  Elishd‘,  lit.  ‘God  is  salvation’,  fr.  El,  ‘God’, and  yesha',  ‘salvation’.  For  the  first  element  see El  and  cp.  words  there  referred  to.  The  second element  is  rel.  to  yishu‘dh,  ‘salvation,  deliver¬ ance,  welfare,  prosperity’,  hoshfa',  ‘he  saved’. See  hosanna  and  cp.  the  first  element  in  Isaiah and  the  second  element  in  Joshua, elision,  n.  —  L.  elisio

### leaf 277 /Elizabeth/ @10504
Elizabeth,  1)  fern.  PN.;  2)  in  the  Bible,  the  name of  the  wife  of  Aaron.  —  Late  L.  Elisabeth,  fr. Gk.  ’EXELaotJUeft,  ’EXtaafte-r,  fr.  Heb.  Elishebha', lit.  ‘God  is  an  oath’.  For  the  first  element  see  El. The  second  element  is  rel.  to  shivfdh,  fem.  sheva‘, ‘seven’,  and  to  nishbd‘,  ‘he  swore’,  orig.  ‘he bound  himself  by  the  sacred  number  seven’.  See Shabuoth  and  cp.  the  second  element  in  Bath- sheba.  Cp.  also  Elsa. Elizabethan,  adj.,  pertaining  to  t

### leaf 277 /Elizabeth/ @10986
Elizabethan,  adj.,  pertaining  to  the  age  of  Queen Elizabeth  I.  —  First  used  by  Carlyle,  instead  of Elizabethian,  which  was  coined  by  Coleridge. See  prec.  word  and  -ian,  resp.  -an. elk,  n.,  the  largest  existing  deer.  —  ON.  elgr, rel.  to  OE.  eolh,  OHG.  elaho,  MHG.  elhe,  G. Elch;  Gk.  itXxT)  and  L.  alces,  ‘elk’,  are  Teut. loan  words.  The  above  Teut.  words  are  cogn. with  OI.  fsah,  fsyah,  ‘buck  of  the  antelope’, Russ,  losu,  Czech  los,  etc.,  ‘elk’.  Thes

### leaf 442 /Ishmael/ @2136
Ishmael,  n.,  son  of  Abraham  and  Hagar  (Bible); used  in  a  figurative  sense  to  denote  an  outcast (see  Gen.  16:12)  —  Heb.  Yishmafl,  lit.  ‘God hears’.  Heb.  yishmd',  ‘he  will  hear’,  is  imperf. of  shdmd,  ‘he  heard’.  See  Sbema  and  cp.  Simeon, Simon.  For  the  second  element  in  the  name Ishmael  see  El  and  cp.  words  there  referred  to. Derivative:  Ishmael-ite,  n. Ishtar,  n.,  the  chief  goddess  of  the  Assyrians  and Babylonians,  the  counterpart  of  the  Phoenician A

### leaf 442 /Ishmael/ @2458
Ishmael  see  El  and  cp.  words  there  referred  to. Derivative:  Ishmael-ite,  n. Ishtar,  n.,  the  chief  goddess  of  the  Assyrians  and Babylonians,  the  counterpart  of  the  Phoenician Astarte.  —  Akkad.  Ishtar.  See  Ashtoreth. Ishvara,  Isvara,  n.,  a  title  given  to  Siva  (Hindu mythol.)  —  OI.  isvarafi,  ‘ruler,  lord’,  fr.  isafi, ‘owner,  lord’,  fr.  is-,  ‘to  have,  possess’,  which is  rel.  to  Avestic  is-,  ‘riches,  fortune’,  isvan, ‘well  off,  rich’,  fr.  I.-E.  base  *aik-,  

### leaf 453 /Ishmael/ @5171
Ishmael  (see  Gen. 25:3,  IChr.  1:29),  rel.  to  qadhar,  ‘was  black, dark,  swarthy’,  whence  also  qadhruth,  ‘dark¬ ness,  gloom’,  qedhorannlth,  ‘gloomily,’  QidhrSn, name  of  a  wady  and  valley  east  of  Jerusalem, Mishnaic  Heb.  qldherdh,  ‘pot’,  qadddr,  ‘potter’, and  to  Aram,  qidhrd,  qedherd,  Syr.  qedhrd,  ‘pot’, Arab,  qddhura,  qadhira,  ‘was  dirty’. Derivative:  Kedar-ite ,  adj.  and  n. keddah,  n.,  an  enclosure  for  entrapping  ele¬ phants  (India).  —  Hind,  khedd,  rel.  to  k

### leaf 84 /Babylon/ @4179
Babylonia.  — Heb.  Babhel,  fr.  Akkad.  Bab-ilu,  lit.  ‘the  gate  of God’,  prop,  a  literal  translation  of  Sumerian Ka-dingir.  Akkad.  Bab-ilu  is  compounded  of bdb,  ‘gate’,  and  ilu,  ‘god’.  The  first  element  is rel.  to  Aram,  babh,  babhd,  ‘door,  gate’ ;  see  Bab. For  the  second  element  see  El.  Cp.  the  second element  in  Zerubbabel.  Cp.  also  Babylon, babiroussa,  babirussa,  n.,  a  species  of  wild  swine. —  Malay,  compounded  of  babi,  ‘hog’,  and rasa,  ‘deer’. baboo,  n.

### leaf 84 /Babylon/ @4560
Babylon, babiroussa,  babirussa,  n.,  a  species  of  wild  swine. —  Malay,  compounded  of  babi,  ‘hog’,  and rasa,  ‘deer’. baboo,  n.,  Master,  Mr.  —  Hind.  babu. baboon,  n.  —  ME.  baboin,  fr.  OF.  babuin,  ba- bouin  (F.  babouiti),  a  blend  of  babine,  ‘the  pen¬ dulous  lip  of  certain  animals,  esp.  monkeys’  (the baboon  has  prominent  lips),  and  baboue,  ‘wry, ugly  face’ ;  both  babine  and  baboue  are  of  imi¬ tative  origin.  See  Bloch-Wartburg,  DELF.,  p.49 s.v.  babouin.  MDu.
```


## [2026-09-06T22:57:59.108Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt WEB_vol1.txt SKT.txt LKT.txt; do echo \"== $f\"; grep -n -i -o \".\\{0,80\\}Azrael.\\{0,220\\}\" $f | head -3; done"
}
```


## [2026-09-06T22:58:01.295Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/Azrael\" \\\n \"https://en.wiktionary.org/wiki/عزرائیل\" \\\n \"https://en.wiktionary.org/wiki/جبرئیل\" \\\n \"https://en.wiktionary.org/wiki/الیاس\" \\\n \"https://en.wiktionary.org/wiki/دانیال\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 303, Layh/A.l.h: Persian and Arabic reflexes of Hebrew -el names (Azrael, Gabriel, Elyas, Daniyal)\"; done"
}
```


### [2026-09-06T22:58:08.011Z] TOOL RESULT

```
== FSD_vol1.txt
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,220}
                        \___exceeds complexity limits


== WEB_vol1.txt
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,220}
                        \___exceeds complexity limits


== SKT.txt
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,220}
                        \___exceeds complexity limits


== LKT.txt
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,220}
                        \___exceeds complexity limits
```


### [2026-09-06T22:58:18.833Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/91a450e8d30ba04b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35a3376bfdfb47ef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e56f7a11e69f5ce9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7424b540cf34722e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d505d2ba684b173c.txt
```


## [2026-09-06T22:58:21.934Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in FSD_vol1.txt WEB_vol1.txt LKT.txt PHN.txt DEV.txt; do echo \"== $f\"; grep -n -i \"Azrael\" $f | head -3; done"
}
```


### [2026-09-06T22:58:23.850Z] TOOL RESULT

```
== FSD_vol1.txt
32993:It  is  the  Ansel  men  call  Azrael,
32995:Longfellow  Wayside  Inn,  Azrael  in  pt.  iii,  st.  2
32996:[<  Heb.  Azrael,  help  of  God.]  Az'ra-ilJ.
== WEB_vol1.txt
14451:2. the universal remedy of Paracelsus. — 4-zot/ic, a. pertaining to azote; formed or con- sisting of azote; nitric. [Rare.} A z az’ö-tīite, n. {Gr. a priv., and zdein, to live.) a salt of nitrous acid; a nitrite. = az/6-tize, v.t.; azotized, pl., Pp.: azotizing, Ppr. to impregnate with nitrogen or azote; to nitrogenize. az-6-tom/e-tér, n. [azo-, and Gr. metron, a f measure.] an instrument for measuring the or. ° proportion of nitrogen in a substance; a ni- trometer, s å-zō' tous, a. same as nilrous. i S az-o-ti/ri-a, n. [azo-, and L. urina, urine.) a pathological condition characterized by an excess of nitrogenous matter in the urine. Azrael, n. [Heb. Azsraél, help of God] the angel of death, who, in ancient Jewish and Moslem helicf, parts the soul from the body. Aztec, a. {a native name.] 1. of or pertaining to the Aztecs, a people with an advanced civilization living in Mexico at the time of the Spanish invasion under Cortes in 1519, 2. their language. Az/tec, n. a member of the Aztec people. Az/tec-an, a. 1. Aztec. 2. Nahautlan. aztle’jo (i-thi-la’ho), n. [Sp.] a kind of richly decorated tile. _ A-zam/bre (4-thim/bra), n. [Sp.] a Spanish liquid measure of between two and three quarts. az/are (or a/zure), a. (ME. azure; OFr. azur; LL. azura; Ar. lazivard; Per. lazhward, azure; the initial / lost through confusion with the definite article, Fr. l’, le, etc.] 1. sky-blue; resembling the color of the clear blue sky. 2. cloudless; like the clear sky. azare o ī’zūre), n. 1. the clear blue color of the sky. Her eyes a bashful azure. —Tennyson. 2. any of various blue pigments, as that made of lapis lazuli. 3. the clear sky. [Poet.] 4. the lapis lazuli. (Obs.] 5. in heraldry, blue: in engraving it is rep- resented by parallel horizontal lines, az/are, v.t. to color blue. a-zZu/ré-ous, a. of a clear blue color. az/uare stone, lazulite or azurite. az/a-rine, a. azure. az/i-rine, n. 1. the blue roach, a fish common in Europe. 2. the blue wren of Australia. az/i-rite, n. 1. a blue ore of copper, basic copper carbonate, 2CuCO:Cu(OH)z. 2. a semiprecious gem made from this ore. az/iirn (or a/ziirn), a. of a blue color. [Obs.} az-y-gom/a-tous, a. [Gr. a priv., and sygoun, to yoke.] without zygomatic arches. az/y-g0s, n. in anatomy, an azygous part. a:zy’g0-spore, n. [Gr. a priy., and zygon, a yoke, and sporos, a sowing.] in botany, a par- thenogenetic spore resembling a zygospore. az/y-gous, a. (Gr. azygos, unmatched; a priv., È and zygoun, to yoke.| in anatomy, a term ap- 7 plied to certain parts or organs which have no mates or are not found in pairs, as certain muscles, veins, bones, etc. az/yme, az'ym, n. [Gr. azymos, unleavened; a priv., and symé, leaven. unleavened bread. a-zym/ic, a. pertaining to unleavened bread. Bry me n. in church history, one of a sect ` of Christians who administered the Eucharist with unleavened bread; also, a term applied by the Greeks in the eleventh century to the a, atins. g az/y-mous, a. (Gr. azymos, unleavened; a priv. and symeé, leaven.] unleavened; PELRA
== LKT.txt
== PHN.txt
== DEV.txt
```


## [2026-09-06T22:58:24.042Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f in ['91a450e8d30ba04b','35a3376bfdfb47ef','e56f7a11e69f5ce9','7424b540cf34722e','d505d2ba684b173c']:\n    t=open(f+'.txt',encoding='utf-8').read()\n    i=t.find('From Wiktionary')\n    if i<0: i=t.find('Origin and history')\n    print('#########',t.split('\\n')[0])\n    print(re.sub(r'\\n{2,}','\\n',t[i:i+1600]))\nEOF"
}
```


### [2026-09-06T22:58:25.976Z] TOOL RESULT

```
######### URL: https://www.etymonline.com/word/Azrael
x
######### URL: https://en.wiktionary.org/wiki/عزرائیل
d
######### URL: https://en.wiktionary.org/wiki/جبرئیل
d
######### URL: https://en.wiktionary.org/wiki/الیاس
From Wiktionary, the free dictionary
 See also: إلياس and الياس 
 Ottoman Turkish
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Biblical Hebrew אֵלִיָּהוּ ( ʔeliyyɔhū ) der. 
 Ancient Greek Ἠλίας ( Ēlías ) der. 
 Arabic إِلْيَاس ( ʔilyās ) bor. 
 Ottoman Turkish الیاس 
 Borrowed from Arabic إِلْيَاس ( ʔilyās ) , from Ancient Greek Ἠλίας ( Ēlías ) , from Biblical Hebrew אֵלִיָּהוּ ( ʔeliyyɔhū ) .
 Proper noun
 [ edit ] 
 الیاس • ( ilyâs ) 
 ( biblical , Islam ) Elijah , Prophet Ilyas 
 a male given name from Arabic, equivalent to English Elias or Elijah 
 Coordinate terms
 [ edit ] 
 Islamic prophets edit 
 آدم ( âdem ) 
 ادریس ( idrîs ) 
 نوح ( nûh ) 
 هود ( hûd ) 
 صالح ( sâlih ) 
 ابراهیم ( ibrâhîm ) 
 لوط ( lût ) 
 اسماعیل ( ismâʿîl ) 
 اسحاق ( ishâk ) 
 یعقوب ( yaʿkûb ) 
 یوسف ( yûsuf ) 
 ایوب ( eyyûb ) 
 ذو الكفل ( zülkifl ) 
 شعیب ( şuʿayb ) 
 موسی ( mûsâ ) 
 هارون ( hârûn ) 
 داوود ( dâvûd ) 
 سلیمان ( süleymân ) 
 یونس ( yûnüs ) 
 الیاس ( ilyâs ) 
 الیسع ( elyesaʿ ) 
 زكریا ( zekeriyyâ ) 
 یحیی ( yahyâ ) 
 عیسی ( ʿîsâ ) 
 محمد ( muhammed ) 
 Descendants
 [ edit ] 
 Turkish: İlyas 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Arabic إِلْيَاس ( ʔilyās ) , from Hebrew אליהו .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʔil.ˈjaːs/ 
 ( Dari, formal ) IPA ( key ) : [ʔɪl.jɑ́ːs] 
 ( Dari, formal ) IPA ( key ) : [ʔɪl.jɑ́ːs] 
 ( Kabuli ) IPA ( key ) : [ʔɪl.jɑ́ːs] 
 ( Hazaragi ) IPA ( key ) : [ʔil.jɔ́ːs] 
 ( Iran, formal ) IPA ( key ) : [ʔel.jɒ́ːs] 
 ( Tajik, formal ) IPA ( key ) : [ʔil.jɔ́s] 
 Rhymes: -aːs 
 Readin
######### URL: https://en.wiktionary.org/wiki/دانیال
From Wiktionary, the free dictionary
 See also: دانيال 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: دانیال 
 Wikipedia fa 
 Alternative forms
 [ edit ] 
 دنیل ( daniyel ) 
 Etymology
 [ edit ] 
 Borrowed from Arabic دَانِيَال ( dāniyāl ) , from Biblical Hebrew דָּנִיֵּאל ( Dāniyyêl ) . Northern Luri دۆنیار ( dønyar ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /daː.ni.ˈjaːl/ 
 ( Dari, formal ) IPA ( key ) : [d̪ɑː.ni.jɑ́ːl] 
 ( Dari, formal ) IPA ( key ) : [d̪ɑː.ni.jɑ́ːl] 
 ( Kabuli ) IPA ( key ) : [d̪ɑː.ni.jɑ́ːl] 
 ( Hazaragi ) IPA ( key ) : [d̪ɔː.ni.jɔ́ːl̥] 
 ( Iran, formal ) IPA ( key ) : [d̪æ.ni.jɒ́ːl̥] 
 ( Tajik, formal ) IPA ( key ) : [d̪ɔ.ni.jɔ́l] 
 Rhymes: -aːl 
 Readings
 Classical reading ? 
 dāniyāl
 Dari reading ? 
 dāniyāl
 Iranian reading ? 
 daniyâl
 Tajik reading ? 
 doniyol
 Proper noun
 [ edit ] 
 دانیال • ( dāniyāl  / dâniyâl ) ( Tajik spelling Дониёл ) 
 Daniel ( the prophet ) 
 a male given name , Danial , Daniyal , and Danyal 
 Ushojo
 [ edit ] 
 Noun
 [ edit ] 
 دانیال ( dānyāl ) 
 coriander 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=دانیال&oldid=88669019 "
 Categories : Persian terms borrowed from Arabic 
 Persian terms derived from Arabic 
 Persian terms derived from Biblical Hebrew 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/aːl 
 Rhymes:Persian/aːl/3 syllables 
 Persian lemmas 
 Persian proper nouns 
 Persian given names 
 Persian male given names 
 Ushojo lemmas 
 Ushojo nouns 
 Hidden categories: Persian undefined derivations 
 Persian terms in
```


## [2026-09-06T22:58:36.043Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 91a450e8d30ba04b.txt 35a3376bfdfb47ef.txt e56f7a11e69f5ce9.txt | head -30"
}
```


### [2026-09-06T22:58:36.082Z] TOOL RESULT

```
==> 91a450e8d30ba04b.txt <==
URL: https://www.etymonline.com/word/Azrael
FETCHED: 2026-09-06T22:58:15Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary


==> 35a3376bfdfb47ef.txt <==
URL: https://en.wiktionary.org/wiki/عزرائیل
FETCHED: 2026-09-06T22:58:15Z
STATUS: -1
TITLE: 


==> e56f7a11e69f5ce9.txt <==
URL: https://en.wiktionary.org/wiki/جبرئیل
FETCHED: 2026-09-06T22:58:16Z
STATUS: -1
TITLE:
```


## [2026-09-06T22:58:44.577Z] TOOL CALL #39: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/جبريل\" \\\n \"https://en.wiktionary.org/wiki/إسرائيل\" \\\n \"https://en.wiktionary.org/wiki/عزرائيل\" \\\n \"https://fa.wikipedia.org/wiki/اوریل\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 303, Layh/A.l.h: Arabic Jibril/Israil/Azrail and Persian Uriel\"; done; cd data/verification/sources/web && for f in $(python3 - <<'EOF'\nimport hashlib\nfor u in [\"https://en.wiktionary.org/wiki/جبريل\",\"https://en.wiktionary.org/wiki/إسرائيل\",\"https://en.wiktionary.org/wiki/عزرائيل\",\"https://fa.wikipedia.org/wiki/اوریل\"]:\n    print(hashlib.sha1(u.encode()).hexdigest()[:16])\nEOF\n); do echo \"##### $f\"; sed -n '1,4p' $f.txt; done"
}
```


### [2026-09-06T22:58:48.761Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3a7c110fe45cbd19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/20aa2df229a876e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73565166680a7ce7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d83246cf20ee16e.txt
##### 3a7c110fe45cbd19
URL: https://en.wiktionary.org/wiki/جبريل
FETCHED: 2026-09-06T22:58:47Z
STATUS: 200
TITLE: جبريل - Wiktionary, the free dictionary
##### 20aa2df229a876e2
URL: https://en.wiktionary.org/wiki/إسرائيل
FETCHED: 2026-09-06T22:58:47Z
STATUS: 200
TITLE: إسرائيل - Wiktionary, the free dictionary
##### 73565166680a7ce7
URL: https://en.wiktionary.org/wiki/عزرائيل
FETCHED: 2026-09-06T22:58:48Z
STATUS: 200
TITLE: عزرائيل - Wiktionary, the free dictionary
##### 2d83246cf20ee16e
URL: https://fa.wikipedia.org/wiki/اوریل
FETCHED: 2026-09-06T22:58:48Z
STATUS: 200
TITLE: آوریل - ویکی‌پدیا، دانشنامهٔ آزاد
```


## [2026-09-06T22:58:52.003Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nfor f in ['3a7c110fe45cbd19','20aa2df229a876e2','73565166680a7ce7']:\n    t=open(f+'.txt',encoding='utf-8').read()\n    i=t.find('From Wiktionary')\n    print('#########',t.split('\\n')[0])\n    print(re.sub(r'\\n{2,}','\\n',t[i:i+1400]))\nEOF"
}
```


### [2026-09-06T22:58:53.804Z] TOOL RESULT

```
######### URL: https://en.wiktionary.org/wiki/جبريل
From Wiktionary, the free dictionary
 Arabic
 [ edit ] 
 Alternative forms
 [ edit ] 
 جَبْرَئِل ( jabraʔil ) , جَبْرَئِيل ( jabraʔīl ) , جَبْرَائِيل ( jabrāʔīl ) 
 Etymology
 [ edit ] 
 Alteration of جَبْرَائِيل ( jabrāʔīl ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /d͡ʒib.riːl/ , /d͡ʒab.riːl/ 
 Rhymes: -iːl 
 Proper noun
 [ edit ] 
 جِبْرِيل or جَبْرِيل • ( jibrīl or jabrīl )  m 
 ( Islam ) The archangel Gabriel 
 a male given name , Jibril , equivalent to English Gabriel 
 Usage notes
 [ edit ] 
 جِبْرِيل ( jibrīl ) is the form used in the Quran in Ḥafṣ 's reading and is usually used in Islamic contexts. Arabic-speaking Christians refer to Gabriel as جِبْرَائِيل ( jibrāʔīl ) .
 Declension
 [ edit ] 
 Declension of noun جِبْرِيل ( jibrīl )
 singular
 basic singular diptote 
 indefinite
 definite
 construct
 informal
 —
 جِبْرِيل 
 jibrīl 
 —
 nominative
 —
 جِبْرِيلُ 
 jibrīlu 
 —
 accusative
 —
 جِبْرِيلَ 
 jibrīla 
 —
 genitive
 —
 جِبْرِيلَ 
 jibrīla 
 —
 Retrieved from " https://en.wiktionary.org/w/index.php?title=جبريل&oldid=88965531 "
 Categories : Arabic 2-syllable words 
 Arabic terms with IPA pronunciation 
 Rhymes:Arabic/iːl 
 Rhymes:Arabic/iːl/2 syllables 
 Arabic lemmas 
 Arabic proper nouns 
 Arabic masculine nouns 
 ar:Islam 
 Arabic given names 
 Arabic male given names 
 Arabic nouns with basic diptote singular 
 Arabic 
######### URL: https://en.wiktionary.org/wiki/إسرائيل
From Wiktionary, the free dictionary
 See also: اسراییل and اسرائیل 
 Arabic
 [ edit ] 
 Arabic Wikipedia has an article on: إسرائيل 
 Wikipedia ar 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /ʔis.raː.ʔiːl/ 
 Rhymes: -iːl 
 Etymology 1
 [ edit ] 
 Borrowed from Biblical Hebrew יִשְׂרָאֵל ( yiśrāʾēl ) .
 Proper noun
 [ edit ] 
 إِسْرَائِيل • ( ʔisrāʔīl )  m 
 Israel ( the Hebrew patriarch Jacob ) 
 Synonym: يَعْقُوب ( yaʕqūb ) 
 609–632 CE , Qur'an , 3:93 : كُلُّ الطَّعَامِ كَانَ حِلًّا لِّبَنِي إِسْرَائِيلَ إِلَّا مَا حَرَّمَ إِسْرَائِيلُ عَلَىٰ نَفْسِهِ مِن قَبْلِ أَن تُنَزَّلَ التَّوْرَاةُ kullu ṭ-ṭaʕāmi kāna ḥillan li-banī ʔisrāʔīla ʔillā mā ḥarrama ʔisrāʔīlu ʕalā nafsi-hī min qabli ʔan tunazzala t-tawrātu All food was lawful unto the Children of Israel , save that which Israel forbade himself, (in days) before the Torah was revealed. 
 Declension
 [ edit ] 
 Declension of noun إِسْرَائِيل ( ʔisrāʔīl )
 singular
 basic singular diptote 
 indefinite
 definite
 construct
 informal
 —
 إِسْرَائِيل 
 ʔisrāʔīl 
 —
 nominative
 —
 إِسْرَائِيلُ 
 ʔisrāʔīlu 
 —
 accusative
 —
 إِسْرَائِيلَ 
 ʔisrāʔīla 
 —
 genitive
 —
 إِسْرَائِيلَ 
 ʔisrāʔīla 
 —
 Derived terms
 [ edit ] 
 إِسْرَائِيلِيّ ( ʔisrāʔīliyy ) 
 بَنُو إسْرَائِيلَ ( banū ʔisrāʔīla ) 
 Etymology 2
 [ edit ] 
 Borrowed from Israeli Hebrew יִשְׂרָאֵל ( yisra'él ) .
 Proper noun
 [ edit ] 
######### URL: https://en.wiktionary.org/wiki/عزرائيل
From Wiktionary, the free dictionary
 Arabic
 [ edit ] 
 Arabic Wikipedia has an article on: عزرائيل 
 Wikipedia ar 
 Proper noun
 [ edit ] 
 عَزْرَائِيل or عِزْرَائِيل • ( ʕazrāʔīl or ʕizrāʔīl )  m 
 Azrael , angel of death 
 Declension
 [ edit ] 
 Declension of noun عَزْرَائِيل ( ʕazrāʔīl )‎; عِزْرَائِيل ( ʕizrāʔīl )
 singular
 basic singular diptote 
 indefinite
 definite
 construct
 informal
 —
 عَزْرَائِيل ‎; عِزْرَائِيل 
 ʕazrāʔīl ‎; ʕizrāʔīl 
 —
 nominative
 —
 عَزْرَائِيلُ ‎; عِزْرَائِيلُ 
 ʕazrāʔīlu ‎; ʕizrāʔīlu 
 —
 accusative
 —
 عَزْرَائِيلَ ‎; عِزْرَائِيلَ 
 ʕazrāʔīla ‎; ʕizrāʔīla 
 —
 genitive
 —
 عَزْرَائِيلَ ‎; عِزْرَائِيلَ 
 ʕazrāʔīla ‎; ʕizrāʔīla 
 —
 Synonyms
 [ edit ] 
 مَلَك المَوْتِ ( malak al-mawti , literally “ angel of death ” ) 
 Descendants
 [ edit ] 
 → Bashkir: Ғазраил ( Ğazrail ) 
 → English: Azrail , Azrael 
 → French: Azraël 
 → German: Azrael 
 → Kazakh: Әзірейіл ( Äzireyil ) 
 → Russian: Азраи́ль ( Azraílʹ ) 
 → Swahili: Izraili 
 → Turkish: Azrail 
 → Ukrainian: Азраї́ль ( Azrajílʹ ) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=عزرائيل&oldid=91481442 "
 Categories : Arabic lemmas 
 Arabic proper nouns 
 Arabic masculine nouns 
 Arabic nouns with basic diptote singular 
 Arabic definite nouns 
 ar:Death 
 ar:Islam 
 ar:Personifications 
 Hidden categories: Pages with entries 
 Pages
```


## [2026-09-06T22:59:13.299Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD/WEB/SKT ===\"; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt SKT.txt; do echo \"-- $f\"; grep -c -E \"Elohim\" $f; done\necho \"=== AFA (Fraenkel) ilah/Gabriel ===\"; grep -n -i -E \"ilâh|ilah|Gabriel|Elohim\" AFA.txt | head -8\necho \"=== TAD ===\"; grep -n -o -E \"جبرائيل|جبريل|اسرائيل|عزرائيل|الله\" TAD.txt | head -8\necho \"=== ARY latin index ===\"; grep -n -i -E \"gabriel|israel|daniel|elohim\" incoming/ARY/ARY_latin_index_pages.txt | head -8\necho \"=== HRN/HUB ===\"; grep -n -i -E \"Gabriel|Daniel|Elias\" HRN.txt HUB.txt | head -8\necho \"=== LKT ===\"; grep -n -i -E \"Gabriel|Elias|Israel\" LKT.txt | head -8"
}
```


### [2026-09-06T22:59:14.915Z] TOOL RESULT

```
=== FSD/WEB/SKT ===
-- FSD_vol1.txt
2
-- FSD_vol2.txt
1
-- FSD_vol3.txt
0
-- FSD_vol4.txt
3
-- WEB_vol1.txt
2
-- SKT.txt
0
=== AFA (Fraenkel) ilah/Gabriel ===
617:Elohim-El Sep. Abdr. IG Auni. 2; ül^^io^ » DurclibrucU"? zur
2650:l^JSLs (Nöldeke, Elohim-£l. Sitzungsber. der Akademie zu
7234:den. Vgl. Noldeke Elohim , JH p. 5 (Sep. Abdr.). Im Ara-
=== TAD ===
83:الله
751:الله
2088:الله
2822:الله
2911:الله
3146:الله
3148:الله
3186:الله
=== ARY latin index ===
=== HRN/HUB ===
HUB.txt:6786:fiir *patgam i), arm. patgam, aram. pi^gam (Daniel, Esra),
HUB.txt:6859:de&mvar (Daniel 3, 2 — 3), arm. daiavor, 2i^,^databara- (§ 60).
HUB.txt:7713:metrie', aram. haddam 'Stuck' (Daniel), syr. DIH; andarj
HRN.txt:1930:Danielsson- Johansson, BB. 18, 11).
=== LKT ===
1306:Lateinische  Form  des  hebr.  dawid;  N. pr.,  Name  eines  berühmten  Königs  von Israel  [das  Wort  bedeutet  eigenthch 'Liebhng'i  BAUER  in  ZDMG  LXXI, 411];  hieraus  afrz.  davit,  nfrz.  davie, davier  'Zahnzange'  [Romania  XXXIII, 344],  frz.  david  Name  des  'Schippen- königs' im  Kartenspiel.  —  Zu  engl. taffg  verderbt,  die  Bezeichnung  für  den Waliser  [wie  Paddy  für  den  Iren,  Saw- neij  für  den  Schotten;  ersteres  aus Pafrick,  letzteres  aus  Alexander].  [ML 2487.
4263:i"eich  geführt  haben,  h)  Aus  Schlim- massel mit  Anlehnung  an  Gabriel  oder ähnhtlie  Namen,  c)  Hebr.  selümVel  soll als  Ausruf  'Heil  Gottes!  =  Gott  behüte!' auf  die  Person  übertragen  sein.  Die oben  angegebene  Etymologie  scheint  die wahrscheinlichste  zu  sein.]  (MDWiD 39/40.
```


## [2026-09-06T22:59:22.001Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WEB Elohim\"; grep -n -o \"Elohim.\\{0,400\\}\" WEB_vol1.txt | head -2; echo; echo \"### FSD1 Elohim\"; grep -n -o \"Elohim.\\{0,400\\}\" FSD_vol1.txt | head -2; echo; echo \"### WEB Elysian\"; grep -n -o \"Elysian.\\{0,350\\}\" WEB_vol1.txt | head -2; echo; echo \"### FSD Bethel\"; grep -n -o \"Bethel.\\{0,300\\}\" FSD_vol1.txt | head -2"
}
```


### [2026-09-06T22:59:23.805Z] TOOL RESULT

```
### WEB Elohim
63074:Elohim is used instead of Yahweh as the name for. God.
63076:Elohim is used instead of

### FSD1 Elohim
7919:Elohim. Hebrew  being  written  without  vowels,  and  the  Jews never  pronouncing  JHVH  when  they  met  it  in  the Scriptures,  but  substituting  for  it  either  Adonai  or  Elo- him, the  true  vowels  were  forgotten,  say  the  Adonists. a-do'nltc,  1   o-do'nait;  2   a-do'nlt,  n.  Chem.  A   white crystalline  pentatomic  form  of  alcohol  (CsH7(OH)s) obtained  from  Adonis  vernalis.  [as
65630:Elohim:  Wo  hung  with  The©  the  curtains  of  the  heavens, And  choired  the  morning  atars.

### WEB Elysian
63170:Elysian fi
63172:Elysian plain, the plain of the departed. from elysis, a variant of eleusis, from eleusesthai, fut. of elthein, to go or come.

### FSD Bethel
22189:Bethel  of Vermont*,  Bledsoe  Favorite1,  Blenheim  Pippin4,  Bowen Favorite1,  Broad  we  II  Sweet*,  Carolina  June**,  Chenango Strawberry*.  Delaware  Red  Winter*1,  Derby  Seck-no- further9.  Duchess  of  Oldenburg*4,  Esopus  Spltzenburg11, Funtllng”,  Gabriel  of  Indlanai',  Golden  Pippin13,  
40809:Bethel  I’ll  raise.  Beth"»tap'pu-ah,l  -tap'u-a;  2   -tfip'q-a,  n.  Bib.  Josh.  XV,  23.
```


## [2026-09-06T22:59:36.440Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,os\ndef norm(s): return s.replace('ي','ی').replace('ى','ی').replace('ك','ک').replace('‌','')\nfiles=['BQT_v1_pages.txt','BQT_v2_pages.txt','incoming/BQT/BQT_v3_pages.txt','incoming/BQT/BQT_v4_pages.txt','incoming/BQT/BQT_v5_pages.txt','AFM.txt','incoming/ARY/ARY_pages.txt','TAD.txt']\nwords=['جبرئیل','جبرائیل','عزرائیل','میکائیل','اسرائیل','بابل','دانیال','الیاس','اوریئل']\nfor f in files:\n    if not os.path.exists(f): print('missing',f); continue\n    t=norm(open(f,encoding='utf-8',errors='replace').read())\n    out=[]\n    for w in words:\n        n=len(re.findall(norm(w),t))\n        if n: out.append(f'{w}={n}')\n    print(f, ' '.join(out) or 'NONE')\nEOF"
}
```


### [2026-09-06T22:59:38.112Z] TOOL RESULT

```
BQT_v1_pages.txt جبرئیل=2 عزرائیل=3 میکائیل=6 اسرائیل=8 بابل=41 دانیال=1 الیاس=6
BQT_v2_pages.txt جبرئیل=2 جبرائیل=1 عزرائیل=2 اسرائیل=3 بابل=5 الیاس=5
incoming/BQT/BQT_v3_pages.txt جبرئیل=2 عزرائیل=1 میکائیل=1 اسرائیل=5 بابل=17 الیاس=4
incoming/BQT/BQT_v4_pages.txt جبرئیل=4 جبرائیل=1 میکائیل=2 اسرائیل=2 بابل=12 دانیال=1 الیاس=5
incoming/BQT/BQT_v5_pages.txt جبرئیل=1 میکائیل=1 بابل=1 الیاس=1
AFM.txt بابل=4 الیاس=1
incoming/ARY/ARY_pages.txt بابل=6
TAD.txt بابل=2 دانیال=1
```


## [2026-09-06T22:59:42.525Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef norm(s): return s.replace('ي','ی').replace('ى','ی').replace('ك','ک').replace('‌','')\nt=norm(open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read())\n# find headword-ish contexts\nfor w in ['بابل','الیاس','دانیال']:\n    print('=====',w)\n    for m in list(re.finditer(norm(w),t))[:4]:\n        s=t[max(0,m.start()-200):m.start()+260].replace('\\n',' ')\n        print('   ...',s)\n        print()\nEOF"
}
```


### [2026-09-06T22:59:44.502Z] TOOL RESULT

```
===== بابل
   ... وشوش ( درعیلام ) وبنستان ( - بیستون ) وهمدان والوند ( در ماد) و وانمقد مه دو ( در ارمشتان) وسوئز ( درمصر ) . نوشتة بفستان ازداریوش بزرگ کهمانند بیشتر این نوشتها بسه خط میخی و بسه زبان پارسی باستان و بابلی و عیلامی کنده گری شده » از بزر گتر ینسنگنبشتهای جپان بشمار است این کوهایزدی ( بفستان ) که گر انبهاترین سند زبان ملی مارا در بردارد » دردوهز ار وبا نصد سال بیش از این بغرمان داریوش ۰ سومین شاهنشاه هخامنشی ( ۵۲۲ - ۸ پیش از مسیح ) نوشته شده است . دراین نوشت

   ... ست . دراین نوشته که ازپیش آمدهای چپار و بنج سال نخستین از شهریاری داریوش سخن رفته و نامپای هریک از هماوردان وسر ککانیا تاریخ شکست و کهجه شدنشانباد گر دیده؛ دار ای 6۱۵ رده(سطر ) پارسی باستان و ۱۶۱ رده بابلی و ۹۵۰ رده عیلامی است . شاهنشاهانهخا منشی که نو شتهای از خودبباد گار گذاشتهاند اینا نند: کورش بز رگ(۵۵۹ - ۵۲٩‏ پیش ازمسیح)» داریوش بز رگ» خشابار شا(410-4۸7) اردشیر اول ( 6 . ۶۲۲6۵ ) »دار بوش دوم ) ۶ - ۶۰۵ اک اردشیر دوم (۰6 ۳۵۹ )۰ اردشیر سوم ( ۳۵۹ ۳۳۸ ). ا

   ... حان بیش نیز ۲نجارا بهمین نام یاد کردهاند. نوترین نمو نهای که ازبارسی باستان بما رسیده از اردشیر سوم هخامنشی است در نختجمشید . چون خطوط میخی درهر جا که رواح داشت پیش از آغاز تاریخمیلادی از میان رفت ودربابل زمین هم گویا بیشاز یکفرن پیش از میلاد پایدار نیا ند و درهمهجاخط آرامی جای آنهارا گرفت .از آنتاریخ ببعد نه کسی ازذبانهایی زب ند با این خطها نو شته شده بو گاهی داشت و ه چیزی ازمندرجات آئپا میدانست » خط میعی هضامنشیهم درجزه آنها از نقوش اسرار آمیزوشگفت انگیز

   ... شیان؛ دیرین [نها را نمودارمیسازد مثلا داوری در سر کلمةٌ «دین> که یا آن آربایی است یاسامی است ؛ بگواهی گواهان سه هزاررسالهٌ اوستا آریاییاست » چنانکه دین درزبان تازیبگواهی گواهان چندین هزارسالهً | کدی وبابلی » سامی است . درمفپوم قدیمی و اصلی ربطی باهمدیگر نداشتند . گذشته از پیوستگی لمجه پارسی باستان با لهجة نا گزیر چنین زبانی چون زبان ستایش و نیایش و نهاز روزانهةً دین داران است» آثاری درزبان بیروان خود میگذارد ؛ دست کم برغی اژواژههایدینی ژبان زد آنان میگردد 

===== الیاس
   ... تی است که آنرابعر یی سلسالبول گویند...» درصورتی که صحیح آنکلمه دیا ییطساست ۱ وثانیامرض سلسالبول نیستبلکهمرض قنداست وازریشة یونانی دیابتیس 10۵64۵8 گرفته شده . مثال ۳- «بپترک. باناءقرشت برو زناسیرک نامسالیاستسیزدهماهه که فارسیان یش از ظپوراسلام از کبسةٌ ۱۲۰ سال اعتبار میکردند.» در صورتیکه کلمه بپیزک با وهیزک است ۴ مثال؟- «ریونیز» بروزن پیشخیز... نامپسر کیکاوس وداماد طوس ناغفه زای کت پشن بردست. بر ادران بان ویسه کشته شد» وحضی گویند بردست فرود پسر سیأوخش .> ظا

   ...  - چکه . چش: مدخلی. ۲ - خم ۱ : اضافه. ۳ چگ , چش :+ مرد. )۱ عنی بهنگام کتابت. (۲) رل : المعجم ص ۰.۱۸ (۳) موصی وعسی نقاعده اسبت درعرمی» سوه و وخ گر واز: )( رک :المعجم ص ۰۱۸۸ (۵) ۶ حرف میرو رابطه - وآن بالیاس ت که دراواخر افعال ضمیرهخاطب باشد چنانک «رفتی» و « می روی * ودر اءاخر صفات حرف رابطه باشد چنانک « نو عالهی * ۰« نو نوانگری» » «المعجم ص۱۸۷ . انواع یبای حطیدیباجذ مو اف صالنیاب و دیگری بای لیافت است همجوه«خوردنی» و «برداشتنی» وازدنی» و « کشتنی * بعنی لاب

   ... س وزن آستن » بارچةٌ جامه را گوین که بدن مرده را بصد از غل دادن بدان خشک سازند ۴ . آب حیات - بفتح حای بی قطه مشهور است . کونند چشمه است در ظلمات » ه رکه آب از آن چشمه بخورد هر گز لمیرد ؛ وآن صیب خضر و الیاس پیغمبرشد - وباصطلاح شعرا کنایه از سخن کلام صای ویاک - و دحان معشوق و تکلم او باشد - و باءنقاد سالعان اشاره بمشق ومحبت است که ه رکه ازآن بچشد معدوم و فالی نگردد . آب حیو ان - بممن ی آب حیات است که آب زه کی (۱) باشد . آب خر ابات - کناب از شراب اگرری باشد -

   ... ت لغت و کنایت ات یم اول ؛ بمعتی اوباش د که ضصر الاحی . باجیم فارسی مَحتانی زسیلدهه» غایپ است ویعربی ه وکوند - ویکسر اولبزبان | یل را گویند ویعربیِقَاقلةٌ صفار خوانند » وبزبان سربالی بکیازنامهای خدایتعالیاست جلجلاله - | هندی نیز هیل دا لاچی کویند ۴ . 3 دی وولابت هم هست - ودرعربیعهدوییمان الاسافددا* < با سین بی نقطه بالف خواننثد , ار ۱ ۱ را خوا کشیده وسکوننون وفتح دال ابجد و رایقرشث الا س بفتح اول و ثانی بالف کشیدم . | بالف کشیده» نام اسکندرذوالقرنناست واسکت

===== دانیال
   ... سلسلهٌ هخامنشی خطآرامی که در آنروز کار هممجا رخنه بافبهبود همچنان راء خودرا پیمود تابجابی رید که چندی پساز آن بنام خط پهلویخوانده شده است. ۱ آار عمدث آرامی- دوبخش ازتوراة بزبانآرامی است: بخشی از کتاب دانیال که درژمان ااقیوخساییفانوی ۳۵/0205 ۸۱۷۵11:05 (۱۷۵-۱۹ ق.م. ) توشتهشده وبداتیال تسبت دادهشده» دیگر بخثیا ز کتاب عزرا که درحدود فرن سوم ق.م. نوشته شدم همچنین تر گوم 0 (ترجوم - ترجمه) نضبری که بتوراة نوشتهشده واز فرندوم ق.م. آغا زگردیده است؛ بزمان آرامی است
```


## [2026-09-06T22:59:54.733Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef norm(s): return s.replace('ي','ی').replace('ى','ی').replace('ك','ک').replace('‌','')\nfor f in ['BQT_v1_pages.txt','BQT_v2_pages.txt']:\n    t=norm(open(f,encoding='utf-8',errors='replace').read())\n    print('=====',f)\n    for m in list(re.finditer('جبرئیل',t))[:3]:\n        print('   ...',t[max(0,m.start()-180):m.start()+200].replace('\\n',' '),'\\n')\nEOF"
}
```


### [2026-09-06T22:59:56.653Z] TOOL RESULT

```
===== BQT_v1_pages.txt
   ...  و و2 نو یس ۰ میر نوراله ۳9 در ۳ ۳ پمعئی رها کردن وترکگ کردنکه دزمردم بذال معجمه مشهور شده غلط است . بزاء حصجمه صحیح باشد.» واین قول خطاست ۰ وموّ لف مجبل التواریخ و القصص رد : چون جبرئیل علیه السلام کیش بیاورد وابراهیم قر بان کرد...» موّلف «موّ بدا لفضلاء > گوید ۷ :«استوده» بالضم با واو فارسی استه؛ نیک آوردن و نیک آمده.وماندگی گر فته. > وجای دیگی گویها : < استوه» مانده شدهو افس 

   ... الحیل وا کردن. پر نیان ۲ - بر ون سختبان » حر سر گووتد وسضی با بای ابجد آوردهاند و گفتهاند پوششی بوده که پادشاهان قدم آترا بفال نک داشتندی ودر روژهای حجشن بوشدندیو گفتندی که این را جبرئیل از بهشت آورده است؛ وبعضی گوبند جامه رزم رستم زال بوده که از پوست پانگه دوخته .وده اف وگل ح و اک آن مرفوم شده بوده است۸ . بر نیان خوی « کنامه از خوشدل ونرم دل وخوشحال - و خوشخوی ؛ و نرمخوی- و صا 

===== BQT_v2_pages.txt
   ... ‬      ‫ودرعربی لفظی امت که نرا درمقام انکار استعمال‬                        ‫‪E‬‏‬                                                           ‫کنند ؟ ‪# .‬‬ ‫حامل وحی ‪ -‬کنابه از جبرئیل‬                              ‫علهاللام است ‪.‬‬                                           ‫‪۳‬‬                                                  ‫حالوما ‪ - ۴‬بالام بواو رسیده و میم‬           

   ...                                                             ‫روح هکرم ‪ -‬بکر حایحطی(‪:)۱‬‬   ‫رودا به = بر وزن دوشابه ‪ ۰‬نام دختر‬                                      ‫کنابه از جبرئیل عایهاللام است ‪.‬‬   ‫وستم‬‫مپراب کابلی است که زال او را خواست ر‬                                                               ‫روخ ‪ = ۴‬بضم اول وسکوننانی وخای‬  ‫ازو تولد یافت ‪ -‬و نام قلعه
```


## [2026-09-06T23:00:43.715Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:07:11.744Z] TOOL CALL #46: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk303.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPS  = W + \"Reconstruction:Proto-Semitic/ʔil-\"\nHEL = W + \"אל\"\nHELM= W + \"אלהים\"\nAIL = W + \"إله\"\nAJB = W + \"جبريل\"\nAIS = W + \"إسرائيل\"\nAAZ = W + \"عزرائيل\"\nPIL = W + \"الیاس\"\nPDA = W + \"دانیال\"\nELY = \"https://www.etymonline.com/word/Elysium\"\nISR = \"https://www.etymonline.com/word/Israel\"\nFAU = \"https://fa.wikipedia.org/wiki/اوریل\"\n\nKLN_EL = (\"Klein, KLN_1966.txt leaf 275 (s.v. 'El'): \\\"El, n., Hebrew name for God. — Heb. El, 'God', \"\n          \"of uncertain etymology; possibly related to el, 'strong' … Cp. also the first element in the PN.s \"\n          \"Eleazar, Eliezer, Elihu, Elijah, Elishah, Elizabeth, and the second element in Babel, bethel and in \"\n          \"the PN.s Daniel, Emmanuel, Ezekiel, Gabriel, Gamaliel, Ishmael, Israel, Joel, Michael, Nathaniel, \"\n          \"Raphael, Samuel.\\\"\")\nKLN_ELOHIM = (\"Klein, KLN_1966.txt leaf 278 (s.v. 'Elohim'): \\\"Heb. Elohim, pl. of Elōah, 'God', of uncertain \"\n              \"etymology; possibly enlarged fr. El … Cp. Aram. Elāh, in the emphatic state Elāhā, Syr. Allāhā; \"\n              \"Arab. ilāh, with the article, Allāhu (see Allah).\\\"\")\n\nnodes = []\n\ndef N(i, lang, words, verdict, derivation, derivation_fa, sources, ref_check, consulted):\n    nodes.append({\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n                  \"derivation\": derivation, \"derivation_fa\": derivation_fa,\n                  \"sources\": sources, \"ref_check\": ref_check, \"consulted\": consulted})\n\n# ---------------- node 1 ----------------\nN(1, \"Hebrew\", \"Eloh, Elohim, Ěl\", \"confirmed\",\n  \"Hebrew אֵל ʾēl 'god, God' continues Proto-Semitic *ʔil- 'god' (Akkadian ilum, Ugaritic ʾil, Phoenician ʾl, \"\n  \"Aramaic ʾēl, Sabaic ʾl); אֱלוֹהַּ ʾĕlōah is the expanded singular and אֱלֹהִים ʾĕlōhīm its plural, used as the \"\n  \"ordinary Biblical name of God (plural of majesty). Klein s.v. 'Elohim' derives ʾĕlōhīm as 'pl. of Elōah, of \"\n  \"uncertain etymology; possibly enlarged fr. El' and explicitly lines it up with Aramaic ʾĕlāh / emphatic ʾĕlāhā, \"\n  \"Syriac ʾalāhā and Arabic ʾilāh / al-lāhu — i.e. exactly the Semitic-Syriac frame Nourai's root box draws. The \"\n  \"arrow root→Hebrew is therefore right in substance, though the direction is 'both go back to Proto-Semitic *ʔil-' \"\n  \"rather than 'Hebrew ʾēl was formed from a verb lāha/ʾalaha'.\",\n  \"«اِل» (אֵל) و «اِلوهیم» (אֱלֹהִים) در عبری بازماندهٔ سامی آغازین *ʔil- «خدا» است؛ هم‌ریشه با اَکَدی ilum، اوگاریتی ʾil، \"\n  \"آرامی ʾēlāh و عربی إله. اِلوهیم جمعِ اِلوه است و در کتاب مقدس به‌عنوان نام خداوند (جمعِ تعظیم) به کار می‌رود. کلاین نیز \"\n  \"همین را می‌گوید و آن را با آرامی/سریانی alāhā و عربی إله/الله می‌سنجد. پس این پیوند در نمودار نورایی درست است، جز آنکه \"\n  \"نسبت میان ریشه و واژه «هم‌ریشگی» است نه اشتقاق از فعل.\",\n  [PS, HEL, HELM],\n  [{\"ref\": \"KLN:505\", \"status\": \"supports\", \"note\": KLN_ELOHIM},\n   {\"ref\": \"KLN:510\", \"status\": \"supports\", \"note\": KLN_EL + \" (the two cited pages are Klein's 'El' and 'Elohim' entries; the OCR file has no printed page markers, so only the entries, not the page numbers, could be checked)\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 275, 278 s.v. El / Elohim\", \"stance\": \"supports\", \"note\": KLN_EL},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 83 = p.66 s.v. Allāh\", \"stance\": \"supports\",\n    \"note\": \"\\\"In the Semitic area [ʾl] was a widely used word for deity, cf. Heb. אל; Aram. אלה; Syr. alāhā; Sab. ʾlh … Ar. إله is doubtless a genuine old Semitic form.\\\"\"},\n   {\"src\": \"AFA\", \"where\": \"AFA.txt lines 617, 2650, 7234\", \"stance\": \"supports\",\n    \"note\": \"Fraenkel repeatedly cites Nöldeke's monograph 'Elohim-El' (Sitzungsber. der Akademie) when discussing the Aramaic/Syriac word for God, i.e. the same Hebrew–Aramaic–Syriac equation.\"}])\n\n# ---------------- node 2 ----------------\nN(2, \"English\", \"Elohim, El\", \"confirmed\",\n  \"English 'Elohim' and 'El' are learned biblical borrowings taken straight from the Hebrew text (through the \"\n  \"Vulgate/Authorized-Version tradition, not through a spoken chain): Elohim is first used in English theological \"\n  \"writing in the 17th c., El chiefly as the divine name in Semitic scholarship. Klein enters both as Hebrew words \"\n  \"('El, n., Hebrew name for God. — Heb. El, God'; 'Elohim, n., one of the names of God in the Bible. — Heb. \"\n  \"Elohim'), which is precisely the arrow Hebrew → English drawn here.\",\n  \"واژه‌های انگلیسی Elohim و El وام‌واژه‌های کتابی‌اند که مستقیم از متن عبری (از راه ترجمه‌های لاتینی و انگلیسی کتاب مقدس) \"\n  \"گرفته شده‌اند، نه از راه گفتاری. کلاین هر دو را ذیل «از عبری» می‌آورد. ادعای نورایی در این گره درست است.\",\n  [HEL, HELM],\n  [{\"ref\": \"KLN:505\", \"status\": \"supports\", \"note\": KLN_ELOHIM},\n   {\"ref\": \"KLN:510\", \"status\": \"supports\", \"note\": KLN_EL}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 275, 278\", \"stance\": \"supports\", \"note\": \"Both English headwords are given as直 borrowings: 'El, n., Hebrew name for God. — Heb. El'; 'Elohim, n., one of the names of God in the Bible. — Heb. Elohim'.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 7919 (s.v. Adonai) and vol.4\", \"stance\": \"supports\",\n    \"note\": \"Funk & Wagnalls uses Elohim as an English headword/technical term: 'the Jews never pronouncing JHVH … but substituting for it either Adonai or Elohim'.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 63074\", \"stance\": \"supports\",\n    \"note\": \"Webster: 'Elohim is used instead of Yahweh as the name for God' — an established English entry.\"},\n   {\"src\": \"SKT\", \"where\": \"grep 'Elohim' in SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's concise dictionary has no proper-name entries; 0 hits.\"}])\n\n# ---------------- node 3 ----------------\nN(3, \"Hebrew\", \"Bâbh-ěl; Gebher-ěl; Yîšmâ-ěl; Mîxâ-ěl; Yisrâ-ěl; Azra`-ěl\", \"plausible\",\n  \"Four of the six are exactly Klein's: Gabhrīʾēl 'man of God' (gebher 'man' + ʾēl), Yishmāʿēl 'God hears' \"\n  \"(yishmaʿ, imperf. of shāmaʿ + ʾēl), Mīkhāʾēl 'Who is like God?' — Klein's wording verbatim. Two need \"\n  \"qualification. (a) Bābhel: the very page Nourai cites (KLN:138) says the opposite of a Hebrew ʾēl-compound — \"\n  \"'Heb. Bābhel, fr. Akkad. Bāb-ilu, lit. the gate of God, prop. a literal translation of Sumerian Ka-dingir … \"\n  \"compounded of bāb gate and ilu god'; Hebrew borrowed the city name from Akkadian, and Akkadian ilum is a \"\n  \"cognate of ʾēl, not a Hebrew ʾēl (Genesis 11:9 further re-etymologises it from bālal 'to confuse'). \"\n  \"(b) Yisrāʾēl is not 'soldier of God': Klein gives 'lit. he contends with God, fr. sārāh he fought, contended, \"\n  \"and El', and Etymonline 'he that striveth with God (Genesis xxxii.28)'. ʿAzarʾēl 'God has helped' is a real but \"\n  \"rare biblical name (1 Chr 12:6 etc.); the angel of death Azrael is not biblical but Islamic Arabic ʿAzrāʾīl.\",\n  \"از شش نام، «جبرئیل» (gebher «مرد» + ʾēl)، «اسماعیل» (yishmaʿ «می‌شنود» + ʾēl) و «میکائیل» («کیست مانند خدا؟») دقیقاً همان است \"\n  \"که کلاین می‌آورد. اما «بابل» بنا بر همان صفحه‌ای که نورایی ارجاع داده (کلاین ۱۳۸) وام‌واژه‌ای اکدی است: Bāb-ilu «دروازهٔ خدا»، \"\n  \"ترجمهٔ تحت‌اللفظی سومری Ka-dingir؛ یعنی جزء دومش ilu اکدی است که با ʾēl عبری هم‌ریشه است نه برگرفته از آن (و در سِفر پیدایش به \"\n  \"ریشه‌شناسی عامیانه از bālal «آشفتن» بازبسته شده). معنای «اسرائیل» نیز «سرباز خدا» نیست؛ کلاین و اتیمآنلاین «با خدا کشتی گرفت/ \"\n  \"ستیزید» می‌دهند. «عزرائیل» هم به‌عنوان نام کتاب‌مقدسی نادر (ʿAzarʾēl «خدا یاری کرد») درست است، ولی فرشتهٔ مرگ به این نام اسلامی-عربی است.\",\n  [HEL, ISR, AAZ],\n  [{\"ref\": \"KLN:138\", \"status\": \"contradicts\",\n    \"note\": \"Klein leaf 84 s.v. 'Babel': 'Heb. Bābhel, fr. Akkad. Bāb-ilu, lit. the gate of God … compounded of bāb, gate, and ilu, god … For the second element see El.' — a loan from Akkadian, not a Hebrew ʾēl-compound.\"},\n   {\"ref\": \"KLN:505\", \"status\": \"supports\", \"note\": KLN_EL + \" Klein's own list of ʾēl-names includes Babel, Gabriel, Ishmael, Israel, Michael.\"},\n   {\"ref\": \"AHD:94\", \"status\": \"not_checked\",\n    \"note\": \"AHD:94 is a page of the main 1975 New College Edition dictionary (the Ba- pages); only the Watkins Indo-European appendix (AHD_watkins1985.txt) is on disk, and it has no Semitic material.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 84, 275, 342, 442, 443, 523\", \"stance\": \"partial\",\n    \"note\": \"Gabriel 'Heb. Gabhrīʾēl, lit. man of God, fr. gebher, man, and El'; Ishmael 'Heb. Yishmāʿēl, lit. God hears'; Michael 'Heb. Mīkhāʾēl, lit. Who is like God?'; but Israel 'lit. he contends with God, fr. sārāh he fought, contended'.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaves ~78, 100, 276\", \"stance\": \"supports\",\n    \"note\": \"Jeffery on Jibrīl: 'The ultimate origin, of course, is the Heb. גבריאל'; on Mīkāl: 'may have come directly from מיכאל'; on Ismāʿīl: 'A Christian origin for the word is evident from a comparison of the Gk. Ἰσμαήλ; Syr.; Eth., with the Heb. ישמעאל'.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line ~14451\", \"stance\": \"partial\",\n    \"note\": \"Webster: 'Azrael, n. [Heb. Azraél, help of God] the angel of death, who, in ancient Jewish and Moslem belief, parts the soul from the body' — the gloss agrees, the angel is Jewish-Islamic rather than biblical.\"}])\n\n# ---------------- node 4 ----------------\nN(4, \"Arabic\", \"- el, ěl\", \"plausible\",\n  \"Arabic has no living suffix -īl: the element is the frozen Hebrew ʾēl of names that Arabic took over whole \"\n  \"(Jibrīl/Jibrāʾīl, Mīkāl/Mīkāʾīl, Ismāʿīl, Isrāʾīl, ʿAzrāʾīl), overwhelmingly through Syriac Christian and \"\n  \"Jewish channels rather than straight from Hebrew — Jeffery notes for Isrāʾīl that 'the absence of the initial \"\n  \"ʿayin stands against a direct derivation from the Heb. ישראל, and points to a Christian origin … The \"\n  \"probabilities are in favour of a Syriac origin'. Arabic philologists themselves treated the ending as a mark of \"\n  \"foreignness: Jeffery quotes the Qāmūs to the effect that 'all forms ending in -īl are ʿajamī'. So Nourai's \"\n  \"'suffix meaning pertaining to God' is a descriptive, not a morphological, statement, and the arrow should pass \"\n  \"through Syriac/Greek.\",\n  \"در عربی پسوند زندهٔ ‑ئیل وجود ندارد؛ این جزء همان «اِل» عبری است که در نام‌های وام‌گرفته (جبرئیل، میکائیل، اسماعیل، اسرائیل، \"\n  \"عزرائیل) به‌صورت متحجر مانده است، و راه ورود آن‌ها بیشتر سریانیِ مسیحی بوده تا عبریِ مستقیم؛ جفری دربارهٔ «اسرائیل» می‌گوید نبودِ \"\n  \"«ع» آغازی مانع اشتقاق مستقیم از עברی است و منشأ سریانی محتمل‌تر است. خودِ لغویان عرب نیز پایانهٔ ‑یل را نشانهٔ اعجمی‌بودن می‌دانستند \"\n  \"(نقل جفری از قاموس). پس تعبیر نورایی توصیفی است نه صرفی، و در مسیر باید سریانی/یونانی افزوده شود.\",\n  [AJB, AIS, AAZ],\n  [{\"ref\": \"FVQ\", \"status\": \"partial\",\n    \"note\": \"FVQ_pages.txt leaf 78 (p.61) s.v. Isrāʾīl: 'the absence of the initial ʿayin stands against a direct derivation from the Heb. ישראל, and points to a Christian origin … The probabilities are in favour of a Syriac origin'; footnote 2: 'The Qamus, as a matter of fact, says that all forms ending in -īl are ʿajamī.' Jeffery supports the Hebrew source but inserts Syriac.\"}],\n  [{\"src\": \"FVQ\", \"where\": \"leaves 78 (Isrāʾīl), 80 (Ismāʿīl), 100 (Jibrīl), 276 (Mīkāl)\", \"stance\": \"partial\",\n    \"note\": \"All four names traced to Hebrew originals but 'through the Syriac' — Jibrīl: 'the probabilities are that it came to him in its Syr. form'.\"},\n   {\"src\": \"KLN\", \"where\": \"leaf 275 s.v. El\", \"stance\": \"supports\",\n    \"note\": \"Klein treats -el as the second element of the theophoric names, the same analysis Nourai's box states.\"},\n   {\"src\": \"AFM\", \"where\": \"grep جبرئیل/عزرائیل in AFM.txt\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir's list of Persian words arabised has nothing on these names (0 hits) — expected, since they are Hebrew/Syriac, not Persian, loans.\"}])\n\n# ---------------- node 5 ----------------\nN(5, \"Persian\", \"بابل ، جبرئیل; اسماعیل ، میکائیل; اسرائیل ، عزرائیل\", \"confirmed\",\n  \"All six reached Persian as Arabic (largely Qurʾānic) names after the Islamic conquest: Bābil (بابل), Jibraʾīl/\"\n  \"Jibrīl (جبرئیل, Qurʾān 2:97), Ismāʿīl (اسماعیل, Q 2:125), Mīkāʾīl (میکائیل, Q 2:98), Isrāʾīl (اسرائیل, Q 3:93) \"\n  \"and ʿAzrāʾīl (عزرائیل, post-Qurʾānic, the malak al-mawt). Persian keeps the Arabic consonant skeleton unchanged \"\n  \"and only re-writes the hamza (جبرائیل ~ جبرئیل ~ جبریل). Moʿin's entry جبرئیل reads '[= جبرائیل ـ جبریل] (اخ.) \"\n  \"یکی از فرشتگان مقرب', and s.v. ملک مقرب he lists the four archangels of Islam as 'جبرائیل، اسرافیل، میکائیل، \"\n  \"عزرائیل' — precisely the set of this node.\",\n  \"هر شش نام از راه عربی (و بیشتر از قرآن) وارد فارسی شده‌اند: بابل، جبرئیل (قرآن ۲:۹۷)، اسماعیل، میکائیل (۲:۹۸)، اسرائیل (۳:۹۳) و \"\n  \"عزرائیل (پس از قرآن، همان ملک‌الموت). فارسی ساختار صامتی عربی را دست‌نخورده نگاه داشته و تنها در نگارش همزه نوسان دارد \"\n  \"(جبرائیل/جبرئیل/جبریل). معین ذیل «جبرئیل» می‌نویسد: «[= جبرائیل ـ جبریل] (اخ.) یکی از فرشتگان مقرب»، و ذیل «ملک مقرب» \"\n  \"چهار فرشتهٔ مقرب اسلام را «جبرائیل، اسرافیل، میکائیل، عزرائیل» می‌شمارد. ادعای نورایی در این گره درست است.\",\n  [AJB, AIS, AAZ],\n  [{\"ref\": \"FVQ\", \"status\": \"supports\",\n    \"note\": \"Jeffery's entries for Jibrīl, Mīkāl, Ismāʿīl and Isrāʾīl establish the Arabic forms that Persian took over; on Mīkāl he even notes 'it was from the Syr. that the Pazend Mušdē, Phlv. and Arm. forms were borrowed', i.e. the same names circulated in Iran.\"},\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"MON_part1.txt: 'جبرئیل: [= جبرائیل ـ جبریل] (اخ.) یکی از فرشتگان مقرب'; MON_part2.txt s.v. ملک: 'عدد این گونه فرشتگان در اسلام چهار است: جبرائیل، اسرافیل، میکائیل، عزرائیل'. (Moʿin's aʿlām volumes 5–6 are not on disk, so page numbers could not be given.)\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. جبرئیل; MON_part2.txt s.v. ملک\", \"stance\": \"supports\",\n    \"note\": \"'جبرئیل: [= جبرائیل ـ جبریل] (اخ.) یکی از فرشتگان مقرب'; 'عدد این گونه فرشتگان در اسلام چهار است: جبرائیل، اسرافیل، میکائیل، عزرائیل'.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt and BQT_v2_pages.txt (grep جبرئیل, بابل, اسرائیل)\", \"stance\": \"supports\",\n    \"note\": \"Borhān uses the names as ordinary Persian vocabulary: v2 'حامل وحی ـ کنایه از جبرئیل علیه‌السلام است' and 'روح مکرم ـ کنایه از جبرئیل علیه‌السلام است'; بابل occurs 41× in vol. 1.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary of the Indo-European roots of Persian has no entry for any of these names — correct, since they are Semitic loans.\"}])\n\n# ---------------- node 6 ----------------\nN(6, \"Latin\", \"(no words)\", \"plausible\",\n  \"Pass-through box for the Latin transmission of the biblical names: Vulgate Latin Babel, Babylonia, Gabriel, \"\n  \"Ismahel, Michael, Israhel. The step is real but incomplete as drawn — the Latin forms come through the Greek \"\n  \"Septuagint and New Testament, and Klein spells this out for the names of this group (Michael: 'Late L., fr. Gk. \"\n  \"Μιχαήλ, fr. Heb. Mīkhāʾēl'; Israel: 'L. Israel, fr. Gk. Ἰσραήλ, fr. Heb. Yisrāʾel'). Nourai's chart omits the \"\n  \"Greek stage.\",\n  \"این جعبه گذرگاه لاتینی نام‌های کتاب مقدس است: صورت‌های ولگات Babel، Gabriel، Michael، Israhel. خودِ مرحله درست است اما ناقص \"\n  \"رسم شده؛ لاتینی این نام‌ها را از یونانیِ سبعینه و عهد جدید گرفته است (کلاین: Michael از Late L. ← یونانی Μιχαήλ ← عبری؛ \"\n  \"Israel از لاتینی ← یونانی Ἰσραήλ ← عبری). نورایی مرحلهٔ یونانی را نیاورده است.\",\n  [ISR],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 443, 523\", \"stance\": \"partial\",\n    \"note\": \"'Israel, n. — L. Israel, fr. Gk. Ἰσραήλ, fr. Heb. Yisra'el'; 'Michael … — Late L., fr. Gk. Μιχαήλ, fr. Heb. Mīkhāʾēl' — Latin yes, but via Greek.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1/vol4 (grep Elohim, Bethel)\", \"stance\": \"silent\",\n    \"note\": \"Funk & Wagnalls gives the biblical names as Bible entries without a Latin etymology, so it neither confirms nor denies the Latin step.\"}])\n\n# ---------------- node 7 ----------------\nN(7, \"French\", \"(no words)\", \"plausible\",\n  \"Pass-through box for French: Old/Modern French Babel, Gabriel, Michel/Michaël, Israël, Ismaël, Azraël — the \"\n  \"learned church forms taken over from Latin with French stress and orthography (the tréma marking the \"\n  \"non-diphthongal -aë-). The step Latin → French is uncontroversial for the names that Persian later borrowed in \"\n  \"their European shape (node 8).\",\n  \"این جعبه گذرگاه فرانسوی است: صورت‌های کلیسایی Gabriel، Michaël، Israël، Ismaël، Azraël که از لاتینی به فرانسوی رفته‌اند و \"\n  \"تنها آهنگ و املای فرانسوی (از جمله دو نقطهٔ tréma) بر آن‌ها افزوده شده است. این مرحله برای نام‌هایی که بعدها فارسی به شکل \"\n  \"اروپایی وام گرفت (گرهٔ ۸) لازم و پذیرفتنی است.\",\n  [AAZ],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaf 275 and the individual PN entries\", \"stance\": \"partial\",\n    \"note\": \"Klein routes the English names through Late Latin/French church usage but does not spell out a separate French stage for each name.\"},\n   {\"src\": \"DEV\", \"where\": \"DEV.txt (grep Azrael, Gabriel)\", \"stance\": \"silent\",\n    \"note\": \"Devic's dictionary of French words of Oriental origin has no entry for these names (0 hits); it covers common nouns, not biblical PNs.\"}])\n\n# ---------------- node 8 ----------------\nN(8, \"Persian\", \"Gâbrîel «گابریل»\", \"plausible\",\n  \"گابریل is the modern Persian rendering of the European (French/English) name Gabriel — with initial gā- and a \"\n  \"stressed -el, exactly the French [ɡabʁijɛl] — and it is kept apart in Persian from the Islamic form جبرئیل, \"\n  \"which came through Arabic (node 5). Persian thus has a doublet from one Hebrew source by two routes: \"\n  \"Heb. Gabhrīʾēl → Syriac/Arabic Jibrāʾīl → NP جبرئیل, and Heb. → Gk. Γαβριήλ → Lat. Gabriel → Fr. Gabriel → \"\n  \"NP گابریل (19th–20th c., with the wave of European names and translated literature). The route itself is sound; \"\n  \"it could not be checked in Moʿin, because the cited reference is the aʿlām part of Farhang-e Fārsi (vols 5–6), \"\n  \"which is not among the local files.\",\n  \"«گابریل» صورت فارسیِ نام اروپایی (فرانسوی) Gabriel است ـ با «گا»ی آغازی و «ـِل» پایانی، درست مانند تلفظ فرانسوی ـ و در فارسی \"\n  \"از «جبرئیل» که از راه عربی آمده جداست. بنابراین فارسی از یک اصل عبری دو صورت دوگانه (doublet) دارد: عبری Gabhrīʾēl ← سریانی/عربی \"\n  \"جبرائیل ← جبرئیل، و عبری ← یونانی Γαβριήλ ← لاتینی ← فرانسوی ← گابریل (سدهٔ سیزدهم/چهاردهم خورشیدی، همراه موج نام‌ها و ترجمه‌های \"\n  \"اروپایی). مسیر پذیرفتنی است، ولی چون ارجاع به جلدهای اعلامِ فرهنگ معین (۵ و ۶) است و آن جلدها در کتابخانهٔ محلی نیست، تأیید مستقیم نشد.\",\n  [AJB],\n  [{\"ref\": \"MON\", \"status\": \"not_checked\",\n    \"note\": \"گابریل would stand in Moʿin's aʿlām volumes (5–6); the local MON_part1/part2 files cover only the lexicon volumes and return 0 hits for گابریل. vajehyab/abadis also carry only the lexicon.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep گابریل\", \"stance\": \"silent\",\n    \"note\": \"0 hits — the lexicon volumes on disk do not contain European proper names.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v1–v5_pages.txt, grep گابریل\", \"stance\": \"silent\",\n    \"note\": \"0 hits; Borhān-e Qāteʿ (17th c.) predates the European borrowing, as expected if the form is modern.\"}])\n\n# ---------------- node 9 ----------------\nN(9, \"English\", \"Babel, Babylonia, Gabriel, Ishmael, Michael, Israel, Azrael\", \"plausible\",\n  \"Michael and Israel do run Hebrew → Greek → Latin → English (Klein: 'Michael … Late L., fr. Gk. Μιχαήλ, fr. Heb. \"\n  \"Mīkhāʾēl'; 'Israel — L. Israel, fr. Gk. Ἰσραήλ, fr. Heb. Yisra'el'), and Babylonia is Greek Βαβυλωνία from \"\n  \"Βαβυλών. But two words break the drawn route: Klein takes English Babel and Ishmael directly from Hebrew \"\n  \"(Bābhel < Akkad. Bāb-ilu; Yishmāʿēl), and Azrael is not a Latin word at all — it entered English (and French \"\n  \"Azraël, German Azrael, Turkish Azrail) from Arabic ʿAzrāʾīl, the Islamic angel of death, as Wiktionary's \"\n  \"descendant list and Webster ('the angel of death, who, in ancient Jewish and Moslem belief, parts the soul from \"\n  \"the body') show. Gabriel is Late Latin Gabriel from Greek Γαβριήλ.\",\n  \"«Michael» و «Israel» به‌راستی از عبری ← یونانی ← لاتینی ← انگلیسی آمده‌اند (کلاین) و Babylonia از یونانی Βαβυλωνία است. اما دو واژه \"\n  \"با مسیر رسم‌شده نمی‌خواند: کلاین «Babel» و «Ishmael» انگلیسی را یکسره از عبری می‌گیرد، و «Azrael» اصلاً از لاتینی نیامده بلکه از \"\n  \"عربیِ «عزرائیل» (فرشتهٔ مرگ در اسلام) وارد انگلیسی و فرانسوی و آلمانی و ترکی شده است (ویکی‌واژه و وبستر). حکم: با احتیاط پذیرفتنی، \"\n  \"با اصلاح مسیرِ Babel و Ishmael و به‌ویژه Azrael.\",\n  [AAZ, ISR],\n  [{\"ref\": \"KLN\", \"status\": \"partial\",\n    \"note\": \"Klein leaf 84 'Babel, n. … — Heb. Bābhel, fr. Akkad. Bāb-ilu' and leaf 442 'Ishmael, n. … — Heb. Yishmāʿēl' give no Latin intermediary; leaves 443/523 do give L. ← Gk. for Israel and Michael. Klein has no entry for Azrael at all.\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"Only the Watkins Indo-European appendix of AHD is on disk; the main dictionary's proper-name entries could not be consulted.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 84, 342, 442, 443, 523\", \"stance\": \"partial\", \"note\": \"See ref_check: Latin stage present for Michael/Israel/Gabriel, absent for Babel/Ishmael, and no Azrael entry.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line ~14451\", \"stance\": \"partial\",\n    \"note\": \"'Azrael, n. [Heb. Azraél, help of God] the angel of death, who, in ancient Jewish and Moslem belief, parts the soul from the body' — Hebrew source acknowledged, but the currency is Jewish-Islamic, not Latin.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 32993–32996\", \"stance\": \"partial\",\n    \"note\": \"Funk & Wagnalls, s.v. Azrael: '[< Heb. Azrael, help of God.] Az'ra-il' — the same double form Azrael/Azrail that betrays the Arabic route.\"}])\n\n# ---------------- node 10 ----------------\nN(10, \"Hebrew\", \"Urî-ěl\", \"confirmed\",\n  \"Klein's entry is Nourai's sentence word for word: 'Uriel, masc. PN. — Heb. Uri'el, lit. flame of God or my \"\n  \"light is God. See next word and El.' The first element is ʾūr 'fire, flame' / ʾōr 'light' (verb ʾōr 'it became \"\n  \"light'), which Klein connects with Aramaic ʾōr 'to give light', Akkadian urru 'light, day', Arabic awwara 'he \"\n  \"kindled'; ʾŪrīʾēl is a name of an archangel in 1 Enoch and 4 Ezra rather than in the Hebrew Bible proper.\",\n  \"کلاین دقیقاً همان را می‌گوید که نورایی آورده است: «Uriel، اسم خاص مذکر ـ عبری Uri'el، تحت‌اللفظ «شعلهٔ خدا» یا «نور من خداست».» \"\n  \"جزء نخست ʾūr «آتش، شعله»/ʾōr «نور» است (هم‌ریشه با آرامی ʾōr، اکدی urru «روز، روشنایی» و عربی أوّر «برافروخت») و جزء دوم همان \"\n  \"«اِل». این نام در کتاب مقدس عبری نیامده و از فرشتگان کتاب اول خنوخ و عزرای چهارم است. ادعای نورایی درست است.\",\n  [HEL],\n  [{\"ref\": \"KLN:1682\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 891: \\\"Uriel, masc. PN. — Heb. Uri'el, lit. 'flame of God' or 'my light is God'. See next word and El.\\\" — verbatim Nourai's gloss. (No printed page numbers in the OCR; only the entry could be located.)\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaf 891 s.v. Uriel / Urim\", \"stance\": \"supports\",\n    \"note\": \"Uriel as above; the neighbouring 'Urim' entry gives the ʾūr 'fire, flame' family Klein refers to.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol4 (grep Uriel)\", \"stance\": \"silent\",\n    \"note\": \"No usable Funk & Wagnalls entry surfaced for Uriel; the name is apocryphal rather than biblical.\"}])\n\n# ---------------- node 11 ----------------\nN(11, \"Persian\", \"Ureîl «اوریئل»\", \"unverified\",\n  \"The form اوریئل is a straightforward Persian transcription of Hebrew ʾŪrīʾēl (ū-rī-ʾēl), with hamza on yeh \"\n  \"writing the glottal stop before the -el element, exactly as in جبرئیل and میکائیل; it belongs to the Persian \"\n  \"Bible/apocrypha and angelology vocabulary rather than to the Qurʾānic set. I could not confirm it in any \"\n  \"independent source available here: Nourai's reference AKM (A'lam-e Ketab-e Moqaddas) is purchase-only, Moʿin's \"\n  \"aʿlām volumes are not on disk (0 hits for اوریئل in MON_part1/2 and in BQT vols 1–5), and fa.wikipedia.org/wiki/\"\n  \"اوریل redirects to آوریل, the month of April, not the angel.\",\n  \"«اوریئل» آوانگاری فارسیِ ʾŪrīʾēl عبری است؛ همزه روی «ی» همان انسداد چاکنایی پیش از جزء «ـئیل» را می‌نویسد، درست مانند جبرئیل و \"\n  \"میکائیل. این نام به واژگان کتاب‌مقدسی/فرشته‌شناسی فارسی تعلق دارد نه به مجموعهٔ قرآنی. با منابع در دسترس تأیید مستقل نشد: مرجع \"\n  \"نورایی (فرهنگ اعلام کتاب مقدس) نسخهٔ رقمی ندارد، جلدهای اعلام معین در کتابخانهٔ محلی نیست (در معین و برهان قاطع هیچ نمونه‌ای نیافتم) و \"\n  \"«اوریل» در ویکی‌پدیای فارسی به «آوریل» (ماه) می‌رسد. بنابراین: تأییدنشده، نه ردشده.\",\n  [FAU],\n  [{\"ref\": \"AKM:64\", \"status\": \"not_checked\",\n    \"note\": \"refs_online.json: AKM (A'lam-e Ketab-e Moqaddas, Iran University Press 1988) is 'purchase only', no digital copy on any permitted platform.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep اوریئل\", \"stance\": \"silent\", \"note\": \"0 hits; the aʿlām volumes that would carry it are not on disk.\"},\n   {\"src\": \"BQT\", \"where\": \"BQT_v1–v5_pages.txt, grep اوریئل\", \"stance\": \"silent\", \"note\": \"0 hits in any of the five volumes.\"}])\n\n# ---------------- node 12 ----------------\nN(12, \"English\", \"Uriel\", \"confirmed\",\n  \"English Uriel is the apocryphal archangel's name (1 Enoch; Milton, Paradise Lost III), taken over unchanged \"\n  \"from the Hebrew form through the Greek/Latin apocrypha. Klein's entry, on the page Nourai cites, gives the \"\n  \"English headword straight from Hebrew: 'Uriel, masc. PN. — Heb. Uri'el, lit. flame of God or my light is God'.\",\n  \"«Uriel» انگلیسی همان نام فرشتهٔ مقرب در ادبیات اپوکریفایی است (کتاب خنوخ؛ و در بهشت گمشدهٔ میلتون) که بی‌تغییر از صورت عبری، از راه \"\n  \"متن‌های یونانی و لاتینی، به انگلیسی رسیده است. کلاین در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد: «Uriel ـ عبری Uri'el «شعلهٔ خدا» یا \"\n  \"«نور من خداست».» ادعای نورایی درست است.\",\n  [HEL],\n  [{\"ref\": \"KLN:1682\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 891, s.v. Uriel (quoted in full at node 10).\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaf 891\", \"stance\": \"supports\", \"note\": \"English entry given directly from Hebrew Uri'el.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt (grep Uriel)\", \"stance\": \"silent\", \"note\": \"Skeat carries no proper names.\"}])\n\n# ---------------- node 13 ----------------\nN(13, \"Hebrew\", \"Dânî-ěl; Ěl-iyyâh; Immânŭ-ěl; Rephâ-ěl; Ěli-šebha; Šěmu-ěl\", \"confirmed\",\n  \"Every one of the six is Klein's, essentially word for word: Dāniʾēl 'God is my judge' (Dan 'judge' + ʾēl, \"\n  \"'rel. to Akkad. Dāni-ilu'); ʾĒliyyāh 'The Lord is God' (ʾēl + Yāh, the short Tetragrammaton); ʿImmānūʾēl 'God \"\n  \"is with us' (ʿimmānū 'with us' + ʾēl, Isaiah 7:14); Rephāʾēl 'God has healed' (rāphā 'he healed', rel. to Syr. \"\n  \"rephā, Arab. rafaʾa); ʾĔlīshebhaʿ 'God is an oath' (ʾēl + shevaʿ 'seven/oath', 'orig. he bound himself by the \"\n  \"sacred number seven'); Shĕmūʾēl 'name of God' (shem 'name' + ʾēl). Note that Elijah and Joel (node 20) are the \"\n  \"same two elements in inverted order, as Klein observes.\",\n  \"هر شش نام دقیقاً همان است که کلاین می‌آورد: دانیال «خدا داور من است» (Dan + ʾēl، هم‌سنگ اکدی Dāni-ilu)؛ ایلیّا «یهوه خداست» \"\n  \"(ʾēl + یاه، کوتاه‌شدهٔ نام چهارحرفی)؛ عمّانوئیل «خدا با ماست» (اشعیا ۷:۱۴)؛ رفائیل «خدا شفا داد» (rāphā، هم‌ریشه با سریانی rephā و \"\n  \"عربی رَفَأَ)؛ الیشبع «خدا سوگند است» (ʾēl + shevaʿ «هفت/سوگند»)؛ و سموئیل «نام خدا» (shem + ʾēl). چنان‌که کلاین یادآور می‌شود، \"\n  \"ایلیّا و یوئیل (گرهٔ ۲۰) همان دو جزءاند با ترتیب وارونه. ادعای نورایی در این گره درست است.\",\n  [HEL],\n  [{\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 221 'Daniel … Heb. Dāni'il, lit. God is my judge'; leaf 277 'Elijah … Heb. Eliyyāh, lit. The Lord is God' and 'Elizabeth … fr. Heb. Elishebha', lit. God is an oath'; leaf 280 'Emmanuel … fr. Heb. ʿImmanuel, lit. God is with us'; leaf 692 'Raphael … fr. Heb. Rephā'el, lit. God has healed'; leaf 733 'Samuel … fr. Heb. Shĕmu'el, lit. name of God'.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 221, 277, 280, 692, 733\", \"stance\": \"supports\", \"note\": \"See ref_check — all six glosses match verbatim.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 84 (p.67-68) s.v. Ilyās\", \"stance\": \"supports\",\n    \"note\": \"'The Heb. forms are אליה and אליהו, so it is obvious that the Arabic form must have been derived from a Christian source' — confirms the Hebrew ʾĒliyyāh(ū) base of Elijah.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (grep Elohim, Daniel)\", \"stance\": \"supports\",\n    \"note\": \"Webster carries the same biblical names with Hebrew glosses; nothing contradicts Klein.\"}])\n\n# ---------------- node 14 ----------------\nN(14, \"Arabic\", \"(no words)\", \"plausible\",\n  \"The Arabic pass-through box for this group: Dāniyāl (دانيال), Ilyās (إلياس, Qurʾān 6:85, 37:123), and further \"\n  \"Ilyasaʿ, Ismāʿīl. Jeffery shows the route is Hebrew → Greek/Syriac → Arabic rather than Hebrew → Arabic direct: \"\n  \"for Ilyās, 'The Heb. forms are אליה and אליהו, so it is obvious that the Arabic form must have been derived from \"\n  \"a Christian source … The Gk. Ἠλίας gives us the final s, but this also appears in Syr. … The likelihood is thus \"\n  \"that it entered Arabic through the Syriac.' The final -s of إلياس is the decisive proof: it is Greek, not Hebrew.\",\n  \"این جعبه گذرگاه عربی این دسته است: دانيال و إلياس (قرآن ۶:۸۵ و ۳۷:۱۲۳). جفری نشان می‌دهد راه انتقال عبری ← یونانی/سریانی ← عربی است \"\n  \"نه عبری ← عربی مستقیم: «صورت‌های عبری אליה و אליהו است، پس آشکار است که صورت عربی باید از منبعی مسیحی گرفته شده باشد… یونانی Ἠλίας \"\n  \"همان «س» پایانی را به ما می‌دهد… احتمالاً از راه سریانی به عربی رسیده است.» همان «س» پایانیِ «الیاس» گواه یونانی‌بودن مسیر است. \"\n  \"پس ادعا با افزودن مرحلهٔ یونانی/سریانی پذیرفتنی است.\",\n  [PIL, PDA],\n  [{\"ref\": \"FVQ\", \"status\": \"partial\",\n    \"note\": \"FVQ_pages.txt leaf 85 (p.68) s.v. Ilyās: 'the Arabic form must have been derived from a Christian source … The Gk. Ἠλίας or Ἠλείας gives us the final s … The likelihood is thus that it entered Arabic through the Syriac.' Hebrew origin yes, direct Hebrew→Arabic arrow no.\"}],\n  [{\"src\": \"FVQ\", \"where\": \"leaf 85 (p.68) s.v. Ilyās; leaf 85 s.v. al-Yasaʿ\", \"stance\": \"partial\",\n    \"note\": \"As quoted; al-Yasaʿ (Elisha) is likewise 'given as a foreign borrowing' by al-Jawālīqī.\"},\n   {\"src\": \"KLN\", \"where\": \"leaf 277 s.v. Elijah\", \"stance\": \"supports\",\n    \"note\": \"'Cp. also Elias, a shortened form of Elijah' — Klein registers the Greek-mediated form Elias that underlies Arabic Ilyās.\"}])\n\n# ---------------- node 15 ----------------\nN(15, \"Persian\", \"Dânyâl «دانیال»; Elyâs «الیاس»\", \"confirmed\",\n  \"Persian دانیال and الیاس are Arabic loans of Hebrew names, and Wiktionary spells out both chains: دانیال \"\n  \"'borrowed from Arabic دَانِيَال (dāniyāl), from Biblical Hebrew דָּנִיֵּאל (Dāniyyêl)'; الیاس 'borrowed from \"\n  \"Arabic إِلْيَاس (ʔilyās), from Ancient Greek Ἠλίας (Ēlías), from Biblical Hebrew אֵלִיָּהוּ (ʔeliyyɔhū)'. Both are \"\n  \"old in Persian: Borhān-e Qāteʿ s.v. آب حیات has 'وآن نصیب خضر و الیاس پیغمبر شد', the same Khiżr-and-Elias \"\n  \"topos as Sanāʾī's couplet quoted in this box ('سکندر جست لیکن یافت بهره / ز آب زندگانی خضر و الیاس'). The only \"\n  \"correction to the chart is the Greek stage inside the Arabic step (whence the -s of الیاس).\",\n  \"«دانیال» و «الیاس» وام‌واژه‌های عربیِ نام‌های عبری‌اند و ویکی‌واژه هر دو زنجیره را می‌آورد: دانیال از عربی دانيال از عبری کتاب مقدس \"\n  \"דָּנִיֵּאל؛ الیاس از عربی إلياس از یونانی Ἠλίας از عبری אֵלִיָּהוּ. هر دو در فارسی کهن‌اند: برهان قاطع ذیل «آب حیات» می‌نویسد «و آن \"\n  \"نصیب خضر و الیاس پیغمبر شد» ـ همان مضمونی که در بیت سنایی نقل‌شده در همین جعبه آمده است. تنها اصلاح لازم، افزودن مرحلهٔ یونانی درون \"\n  \"گام عربی است که «س» پایانیِ «الیاس» را توضیح می‌دهد. ادعای نورایی درست است.\",\n  [PIL, PDA],\n  [{\"ref\": \"FVA\", \"status\": \"not_checked\",\n    \"note\": \"FVA (Nahvi, Farhang-e Vāzheh-hā-ye ʿArabi dar Fārsi, 1368) has no digital copy on any permitted platform (refs_online.json: 'catalogue record only').\"},\n   {\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Moʿin's aʿlām volumes (5–6), where دانیال and الیاس would stand, are not on disk; MON_part1/2 (lexicon) return 0 hits for either name.\"}],\n  [{\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt s.v. آب حیات\", \"stance\": \"supports\",\n    \"note\": \"'کویند چشمه است در ظلمات … وآن نصیب خضر و الیاس پیغمبر شد' — الیاس current as the prophet's Persian name, matching the Sanāʾī verse in the box.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part1/part2 (grep دانیال, الیاس)\", \"stance\": \"silent\",\n    \"note\": \"0 hits in the lexicon volumes on disk.\"},\n   {\"src\": \"FVQ\", \"where\": \"leaf 85 (p.68)\", \"stance\": \"supports\",\n    \"note\": \"Establishes the Arabic إلياس that Persian borrowed, and its Hebrew ultimate origin.\"}])\n\n# ---------------- node 16 ----------------\nN(16, \"Latin\", \"(no words)\", \"plausible\",\n  \"Pass-through box for the Latin forms Daniel, Elias, Emmanuel, Raphael, Elisabeth, Samuel. Klein documents the \"\n  \"step for four of the six but always with Greek in front of Latin: 'Emmanuel … Gk. Ἐμμανουήλ, fr. Heb. \"\n  \"ʿImmanuel'; 'Raphael … Late L., fr. Gk. Ῥαφαήλ, fr. Heb. Rephāʾel'; 'Elizabeth … Late L. Elisabeth, fr. Gk. \"\n  \"Ἐλισάβετ'; 'Samuel … Late L., fr. Gk. Σαμουήλ'. Daniel he gives straight from Hebrew. So the Latin box is real \"\n  \"but, as at node 6, the Greek link is missing.\",\n  \"این جعبه گذرگاه لاتینی صورت‌های Daniel، Elias، Emmanuel، Raphael، Elisabeth و Samuel است. کلاین این گام را برای چهار نام گواهی \"\n  \"می‌کند، اما همیشه با یونانی پیش از لاتینی: Emmanuel از یونانی Ἐμμανουήλ، Raphael از Late L. ← یونانی Ῥαφαήλ، Elizabeth از Late L. \"\n  \"Elisabeth ← یونانی Ἐλισάβετ، Samuel از Late L. ← یونانی Σαμουήλ؛ و «دانیال» را یکسره از عبری می‌گیرد. پس جعبهٔ لاتینی درست است ولی \"\n  \"مانند گرهٔ ۶ حلقهٔ یونانی افتاده است.\",\n  [],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 221, 277, 280, 692, 733\", \"stance\": \"partial\",\n    \"note\": \"Late Latin forms attested for Emmanuel, Raphael, Elisabeth, Samuel — but each 'fr. Gk.'; Daniel is given directly from Hebrew.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1–4 (grep Bethel, Elohim)\", \"stance\": \"silent\",\n    \"note\": \"Funk & Wagnalls lists the names as Bible entries with no Latin etymology.\"}])\n\n# ---------------- node 17 ----------------\nN(17, \"French\", \"(no words)\", \"plausible\",\n  \"Pass-through box for French Daniel, Élie, Emmanuel, Raphaël, Élisabeth, Samuel — the forms Persian actually \"\n  \"borrowed at node 18 (دانیل, رافائل, الیزابت, ساموئل, آمانوئل reproduce French [danjɛl], [ʁafaɛl], [elizabɛt], \"\n  \"[samɥɛl], [emanɥɛl] rather than the English or Arabic shapes). The step Latin → French for church names is not \"\n  \"in doubt.\",\n  \"این جعبه گذرگاه فرانسوی نام‌های Daniel، Élie، Emmanuel، Raphaël، Élisabeth و Samuel است ـ همان صورت‌هایی که فارسی در گرهٔ ۱۸ وام گرفته \"\n  \"است؛ «دانیل»، «رافائل»، «الیزابت»، «ساموئل» و «آمانوئل» تلفظ فرانسوی را بازمی‌تابانند، نه انگلیسی و نه عربی را. گام لاتینی ← فرانسوی \"\n  \"برای نام‌های کلیسایی تردیدبردار نیست.\",\n  [],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 277, 692, 733\", \"stance\": \"partial\",\n    \"note\": \"Klein gives the Late Latin/Greek ancestry of these names; the French stage is implicit in his 'F.' forms but not itemised.\"},\n   {\"src\": \"PHN\", \"where\": \"PHN.txt (grep Gabriel, Azrael, Raphael)\", \"stance\": \"silent\",\n    \"note\": \"Pihan's dictionary of French words from Arabic/Persian/Turkish has no entry for these biblical names (0 hits) — consistent with a Latin, not an Oriental, route into French.\"}])\n\n# ---------------- node 18 ----------------\nN(18, \"Persian\", \"الیزه ، شانزه لیزه ، آمانوئل; دانیل ، رافائل ، الیزابت ، ساموئل\", \"disputed\",\n  \"Five of the seven are right: آمانوئل, دانیل, رافائل, الیزابت and ساموئل are 20th-c. Persian renderings of French \"\n  \"Emmanuel, Daniel, Raphaël, Élisabeth, Samuel, and so do go back through French and Latin to the Hebrew ʾēl-names \"\n  \"of node 13. The first two do not belong here at all: الیزه is French Élysée and شانزه لیزه is Champs-Élysées, \"\n  \"from Latin Elysium, Greek Ēlýsion (pedíon) 'the Elysian field, abode of the blessed after death', 'of unknown \"\n  \"origin, perhaps from Pre-Greek' (Etymonline) — a Greek mythological word with no Semitic ʾēl in it. (Webster's \"\n  \"19th-c. guess connects it with Greek elysis/eleusesthai 'to come', also purely Greek.) The resemblance between \"\n  \"Élysée and Élisabeth/Élisée is accidental homophony; Nourai appears to have been misled by the Persian \"\n  \"spelling الیزه ~ الیسع. Verdict: disputed for those two words, confirmed for the other five.\",\n  \"پنج واژه از هفت درست است: «آمانوئل»، «دانیل»، «رافائل»، «الیزابت» و «ساموئل» آوانگاری فارسیِ صورت‌های فرانسوی Emmanuel، Daniel، \"\n  \"Raphaël، Élisabeth و Samuel‌اند و از راه فرانسوی و لاتینی به همان نام‌های عبریِ گرهٔ ۱۳ می‌رسند. اما دو واژهٔ نخست به‌کلی بیرون از این \"\n  \"شجره‌اند: «الیزه» همان Élysée فرانسوی و «شانزه لیزه» همان Champs-Élysées است، از لاتینی Elysium و یونانی Ēlýsion (pedíon) «دشت \"\n  \"خجستگان، جایگاه نیک‌بختان پس از مرگ» که خاستگاهش ناشناخته و احتمالاً پیش‌یونانی است (اتیمآنلاین). هیچ «اِل» سامی در آن نیست و شباهت \"\n  \"«الیزه» با «الیسع/الیزابت» تنها هم‌آوایی تصادفی است؛ ظاهراً همین املای فارسی نورایی را به خطا انداخته. حکم: برای این دو واژه پژوهش \"\n  \"امروزی ادعا را رد می‌کند، برای پنج واژهٔ دیگر درست است.\",\n  [ELY],\n  [{\"ref\": \"MON\", \"status\": \"not_checked\",\n    \"note\": \"These are European personal names and a Paris place name; they would stand (if at all) in Moʿin's aʿlām volumes 5–6, which are not on disk — MON_part1/part2 give 0 hits for الیزه, شانزه, آمانوئل, رافائل, الیزابت, ساموئل, دانیل.\"}],\n  [{\"src\": \"MON\", \"where\": \"MON_part1/part2, grep of all seven words\", \"stance\": \"silent\", \"note\": \"0 hits for each; the lexicon volumes contain no European proper names.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line ~63170 s.v. Elysian\", \"stance\": \"contradicts\",\n    \"note\": \"'Elysian plain, the plain of the departed. from elysis, a variant of eleusis, from eleusesthai, fut. of elthein, to go or come' — a Greek etymology (now superseded by 'pre-Greek'), in any case not Semitic.\"},\n   {\"src\": \"KLN\", \"where\": \"leaves 275/277 (El, Elizabeth) vs. the Elysium entry\", \"stance\": \"contradicts\",\n    \"note\": \"Klein's ʾēl-name list (Eleazar, Eliezer, Elihu, Elijah, Elishah, Elizabeth …) does not include Elysium/Élysée.\"}])\n\n# ---------------- node 19 ----------------\nN(19, \"English\", \"Elijah, Immanuel, Daniel, Raphael, Elizabeth, Samuel\", \"plausible\",\n  \"All six are English biblical names of the Hebrew ʾēl-type, and Klein confirms each gloss; the qualification is \"\n  \"again the route. Klein routes Emmanuel, Raphael, Elizabeth and Samuel through Greek into Late Latin and only \"\n  \"then into English, while Elijah and Daniel he takes straight from the Hebrew forms ('Elijah … — Heb. Eliyyāh'; \"\n  \"'Daniel, masc. PN. … — Heb. Dāni'il'). So Nourai's single Latin box is right for four of the six and skips the \"\n  \"Greek stage throughout.\",\n  \"هر شش نام از نام‌های کتاب‌مقدسیِ انگلیسی‌اند و کلاین همهٔ معناها را تأیید می‌کند؛ آنچه نیاز به اصلاح دارد باز مسیر است: کلاین Emmanuel، \"\n  \"Raphael، Elizabeth و Samuel را از یونانی به لاتینی متأخر و سپس به انگلیسی می‌برد، ولی Elijah و Daniel را یکسره از صورت عبری می‌گیرد. \"\n  \"پس جعبهٔ لاتینیِ نورایی برای چهار نام درست است و در همهٔ موارد حلقهٔ یونانی افتاده است. حکم: با احتیاط پذیرفتنی.\",\n  [HEL],\n  [{\"ref\": \"KLN\", \"status\": \"partial\",\n    \"note\": \"Klein leaves 221 (Daniel, direct from Hebrew), 277 (Elijah, direct from Hebrew; Elizabeth 'Late L. Elisabeth, fr. Gk.'), 280 (Emmanuel 'Gk. Ἐμμανουήλ'), 692 (Raphael 'Late L., fr. Gk.'), 733 (Samuel 'Late L., fr. Gk.').\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Only the Watkins IE-roots appendix is on disk; the main AHD entries for these names could not be checked.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 221, 277, 280, 692, 733\", \"stance\": \"partial\", \"note\": \"See ref_check.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt (grep Elohim, Daniel, Samuel)\", \"stance\": \"supports\",\n    \"note\": \"Funk & Wagnalls carries the same names as English biblical entries with Hebrew glosses; nothing contradicts Klein.\"}])\n\n# ---------------- node 20 ----------------\nN(20, \"Hebrew\", \"Beth-ěl; Yô-ěl; Ěl-îša; Nethan-ěl\", \"confirmed\",\n  \"All four are Klein's, with his glosses: bethel 'Heb. bēth El, the house of God' (bēth, construct of bayith \"\n  \"'house', rel. to Aram. baythā, Arab. bayt, Akkad. bītu); Joel 'Heb. Yōʾel, lit. the Lord is God' — 'See Elijah, \"\n  \"in which the same two elements are contained, but in an inverted order'; Elishah 'Heb. Elīshāʿ, lit. God is \"\n  \"salvation, fr. El and yeshaʿ salvation'; Nathaniel 'Heb. Nathanʾel, lit. God has given'. Nourai's second gloss \"\n  \"'God given' for Nethan-ēl is a stylistic variant of the same analysis.\",\n  \"هر چهار نام همان است که کلاین می‌آورد: «بیت‌ئیل» یعنی bēth El «خانهٔ خدا» (bēth حالت مضافِ bayith، هم‌ریشه با آرامی baythā، عربی بیت و \"\n  \"اکدی bītu)؛ «یوئیل» yōʾēl «یهوه خداست» ـ به گفتهٔ کلاین همان دو جزءِ «ایلیّا» با ترتیب وارونه؛ «الیشع» ʾĔlīshāʿ «خدا نجات است» \"\n  \"(ʾēl + yeshaʿ)؛ و «نتنئیل» Nathanʾēl «خدا داد». افزودهٔ نورایی («God given») تنها تعبیر دیگری از همان تحلیل است. ادعای نورایی درست است.\",\n  [HEL],\n  [{\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 99 'bethel, n., a house of worship. — Heb. beth El, the house of God'; leaf 448 'Joel … — Late L. Joel, fr. Gk. Ἰωήλ, fr. Heb. Yo'el, lit. the Lord is God'; leaf 277 'Elishah … Heb. Elishā', lit. God is salvation, fr. El, God, and yesha', salvation'; leaf 551 'Nathaniel, Nathanael … fr. Heb. Nathan'el, lit. God has given'.\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Main-dictionary AHD entries are not on disk (only the Watkins IE appendix).\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 99, 277, 448, 551\", \"stance\": \"supports\", \"note\": \"See ref_check — all four glosses verbatim.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 85 (p.68) s.v. al-Yasaʿ\", \"stance\": \"supports\",\n    \"note\": \"Jeffery's entry for Qurʾānic al-Yasaʿ 'Elisha' treats it as a foreign borrowing of the same Hebrew name, corroborating Ěl-îša.\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (grep Bethel)\", \"stance\": \"supports\",\n    \"note\": \"Webster's 'Bethel' entry likewise glosses it as 'house of God'.\"}])\n\n# ---------------- node 21 ----------------\nN(21, \"Latin\", \"(no words)\", \"plausible\",\n  \"Pass-through box: Vulgate Latin Bethel, Iohel/Joel, Eliseus, Nathanael. Klein's own entries again put Greek \"\n  \"before Latin ('Joel … Late L. Joel, fr. Gk. Ἰωήλ'; 'Nathaniel … Late L. Nathanael, fr. Gk. Ναθαναήλ') and take \"\n  \"'bethel' straight from Hebrew as a common noun ('a house of worship'). So the Latin step holds for the personal \"\n  \"names but not for bethel, and the Greek link is omitted.\",\n  \"این جعبه گذرگاه لاتینی صورت‌های ولگاتیِ Bethel، Joel، Eliseus و Nathanael است. کلاین باز هم یونانی را پیش از لاتینی می‌نشاند \"\n  \"(Joel از Late L. ← یونانی Ἰωήλ؛ Nathaniel از Late L. Nathanael ← یونانی Ναθαναήλ) و «bethel» را به‌عنوان اسم عام یکسره از عبری \"\n  \"می‌گیرد. پس گام لاتینی برای نام‌های خاص درست است اما برای «bethel» نه، و حلقهٔ یونانی افتاده است.\",\n  [],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 99, 448, 551\", \"stance\": \"partial\",\n    \"note\": \"'Joel … Late L. Joel, fr. Gk. Ἰωήλ, fr. Heb. Yo'el'; 'Nathaniel, Nathanael … Late L. Nathanael, fr. Gk. Ναθαναήλ'; but 'bethel … — Heb. beth El' with no Latin.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 40809 (Beth-tappuah etc.)\", \"stance\": \"silent\",\n    \"note\": \"Funk & Wagnalls lists the Beth- names as Bible entries without an etymological route.\"}])\n\n# ---------------- node 22 ----------------\nN(22, \"English\", \"Bethel; Joel; Elisha; Nathaniel\", \"confirmed\",\n  \"All four are established English words/names with exactly this ancestry in Klein: bethel 'a house of worship. — \"\n  \"Heb. bēth El, the house of God' (in English since the 17th c., and in 19th-c. Wales/America the ordinary word \"\n  \"for a nonconformist chapel); Joel 'Late L. Joel, fr. Gk. Ἰωήλ, fr. Heb. Yōʾel'; Elishah/Elisha 'Heb. Elīshāʿ, \"\n  \"lit. God is salvation'; Nathaniel/Nathanael 'Late L. Nathanael, fr. Gk. Ναθαναήλ, fr. Heb. Nathanʾel'. The only \"\n  \"refinement is that Klein interposes Greek between Hebrew and Latin, and takes bethel directly from Hebrew.\",\n  \"هر چهار واژه در انگلیسی جا افتاده‌اند و کلاین همین تبار را برایشان می‌آورد: bethel «نیایشگاه» از عبری bēth El «خانهٔ خدا» (در انگلیسی از \"\n  \"سدهٔ هفدهم، و در ولز و آمریکای سدهٔ نوزدهم واژهٔ معمول برای کلیسای غیررسمی)؛ Joel از لاتینی متأخر ← یونانی Ἰωήλ ← عبری Yōʾēl؛ Elisha \"\n  \"از عبری ʾĔlīshāʿ «خدا نجات است»؛ Nathaniel از لاتینی متأخر Nathanael ← یونانی Ναθαναήλ ← عبری Nathanʾēl. تنها نکتهٔ اصلاحی آن است \"\n  \"که کلاین یونانی را میان عبری و لاتینی می‌نشاند و «bethel» را بی‌واسطه از عبری می‌گیرد. ادعای نورایی درست است.\",\n  [HEL],\n  [{\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaves 99 (bethel), 448 (Joel), 277 (Elishah), 551 (Nathaniel, Nathanael) — quoted at node 20.\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Main-dictionary AHD entries are not on disk.\"}],\n  [{\"src\": \"KLN\", \"where\": \"leaves 99, 277, 448, 551\", \"stance\": \"supports\", \"note\": \"See node 20's ref_check for the verbatim entries.\"},\n   {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 22189, 40809\", \"stance\": \"supports\",\n    \"note\": \"Funk & Wagnalls has Bethel both as a Bible place name and as an ordinary English word (and even as an apple variety, showing how naturalised it is).\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt (grep Bethel, Joel)\", \"stance\": \"silent\", \"note\": \"Skeat's concise dictionary omits proper names.\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Layh, A.l.h\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Proto-Semitic *ʔil- 'god' (Hebrew ʾēl, ʾĕlōah/ʾĕlōhīm; Aramaic ʾĕlāh, Syriac ʾalāhā; Arabic ʾilāh, al-lāh); the verbal roots l-y-h 'to be high/veiled' and ʾ-l-h 'to worship' are the medieval Arab grammarians' back-formations\",\n  \"note\": (\"The two 'roots' in the box are real Arabic verbal roots and Nourai reproduces them faithfully from the page \"\n           \"he cites — Jeffery, FVQ p.66 s.v. Allāh: 'the Kufans in general derived it from [ilāh], while the Basrans \"\n           \"derived it from [lāh], taking [lāh] as a verbal noun from [lāha] to be high or to be veiled. The suggested \"\n           \"origins for [ilāh] were even more varied, some taking it from [ʾalaha] to worship…'. But Jeffery gives these \"\n           \"as the early Muslim philologers' theories and then rejects them: 'Western scholars are fairly unanimous that \"\n           \"the source of the word must be found in one of the older religions. In the Semitic area [ʾl] was a widely \"\n           \"used word for deity, cf. Heb. אל; Aram. אלה; Syr. alāhā; Sab. ʾlh … Ar. إله is doubtless a genuine old \"\n           \"Semitic form', with al-lāh itself going back to Syriac ʾalāhā. Klein agrees: 'El … of uncertain etymology; \"\n           \"possibly related to el, strong' and 'Elohim, pl. of Elōah, of uncertain etymology; possibly enlarged fr. El. \"\n           \"Cp. Aram. Elāh … Syr. Allāhā; Arab. ilāh'. Modern reconstruction: Proto-Semitic *ʔil- 'god', with Arabic \"\n           \"ʾilāh = *ʔil- + a vocative suffix -āh (Wiktionary), and the verb ʾalaha 'to worship' denominal from it. So \"\n           \"the language label (Semitic, with Syriac as the immediate donor of Allāh) and the consonantal frame are \"\n           \"right, and every Hebrew name in the chart really does contain this element; what is not right is the \"\n           \"direction — ʾēl is not derived from a verb 'to be high' or 'to worship'. Verdict: plausible.\"),\n  \"note_fa\": (\"دو «ریشه»‌ای که نورایی در جعبهٔ ریشه آورده، ریشه‌های فعلی واقعیِ عربی‌اند و او آن‌ها را درست از همان صفحه‌ای که ارجاع \"\n              \"داده (جفری، ص ۶۶ ذیل «الله») برداشته است: کوفیان «الله» را از «إله» و بصریان از «لاه» می‌گرفتند و «لاه» را مصدرِ \"\n              \"«لاهَ» به معنی «برتر شد / پوشیده شد» می‌دانستند، و برای «إله» نیز برخی «أَلِهَ» به معنی «پرستید» را پیشنهاد کرده بودند. \"\n              \"اما جفری این‌ها را آرای لغویان کهن مسلمان می‌شمارد و می‌پذیرد که پژوهشگران غربی تقریباً هم‌داستان‌اند که واژه از ادیان \"\n              \"کهن‌تر آمده: «إله عربی بی‌گمان صورتی کهن و اصیل سامی است» و «الله» به سریانیِ alāhā بازمی‌گردد. کلاین نیز «اِل» و \"\n              \"«اِلوهیم» را «با ریشه‌شناسی نامعلوم» می‌داند و آن‌ها را با آرامی ʾĕlāh، سریانی alāhā و عربی إله/الله می‌سنجد. \"\n              \"بازسازی امروزی: سامی آغازین *ʔil- «خدا»، و «إله» = *ʔil- به‌علاوهٔ پسوند ندایی ‑اه؛ فعل «أَلِهَ» نیز اشتقاق ثانوی از \"\n              \"همان اسم است (ریشه‌شناسی عامیانه). پس برچسب زبانی (سامی/سریانی) و ساختار صامتی درست است و همهٔ نام‌های عبریِ نمودار \"\n              \"به‌راستی همین جزء را دارند؛ آنچه نادرست است جهتِ اشتقاق است. حکم: با احتیاط پذیرفتنی.\"),\n  \"sources\": [PS, HEL, HELM, AIL],\n  \"ref_check\": [\n    {\"ref\": \"KLN:505\", \"status\": \"supports\", \"note\": KLN_ELOHIM + \" — this is the Semitic/Syriac equation the root box rests on.\"},\n    {\"ref\": \"FVQ:66\", \"status\": \"partial\",\n     \"note\": \"FVQ_pages.txt leaf 83 = printed p.66, s.v. Allāh. The page does contain both of Nourai's glosses ('taking lāh as a verbal noun from lāha to be high or to be veiled'; 'some taking it from ʾalaha to worship') but attributes them to the Kufan/Basran grammarians and rejects them in favour of a genuine old Semitic *ʾil- and a Syriac source for Allāh.\"},\n    {\"ref\": \"VDQ:125\", \"status\": \"not_checked\",\n     \"note\": \"Badreh'i's Persian translation of Jeffery is only on noorlib (JavaScript viewer, not fetchable); refs_online.json advises verifying the substance via FVQ, the same entry — which was done.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaves 275, 278, and 'Allah' (leaf ~9/2240)\", \"stance\": \"partial\",\n     \"note\": \"s.v. Allah: 'Arab. Allāhu, contraction of al-lāhu, fr. al-, the, and lāh, God. See Elohim.' Klein has the same al- + lāh analysis but no verb 'to be high'.\"},\n    {\"src\": \"FVQ\", \"where\": \"leaf 83 = p.66\", \"stance\": \"partial\", \"note\": \"See ref_check: reports the two derivations, then rejects them.\"},\n    {\"src\": \"AFA\", \"where\": \"AFA.txt lines 617, 2650, 7234\", \"stance\": \"supports\",\n     \"note\": \"Fraenkel cites Nöldeke's 'Elohim-El' for the Aramaic/Syriac word for God, i.e. the Semitic family Nourai's box presupposes.\"},\n    {\"src\": \"TAD\", \"where\": \"TAD.txt (grep الله)\", \"stance\": \"silent\",\n     \"note\": \"Tobia al-Unaysi lists الله only in formulaic phrases, with no etymological discussion.\"}],\n  \"nodes\": nodes,\n}\n\nout = {\"pdf_page\": 303, \"book_page\": 273, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-06\", \"entries\": [entry]}\n\np = \"/home/sfmqrb/git/rishe/data/verification/page-303.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"wrote\", p, len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk303.py"
}
```


### [2026-09-06T23:07:14.360Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-303.json 22 nodes
```


## [2026-09-06T23:07:21.832Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-303.json'\nd=json.load(open(p,encoding='utf-8'))\ns=json.dumps(d,ensure_ascii=False,indent=2)\ns=s.replace('given as直 borrowings','given as direct borrowings')\nopen(p,'w',encoding='utf-8').write(s)\nimport re\nbad=re.findall(r'[一-鿿]',s)\nprint('CJK left:',bad)\nEOF\npython3 -m json.tool data/verification/page-303.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 303"
}
```


### [2026-09-06T23:07:23.616Z] TOOL RESULT

```
CJK left: []
JSON OK
nodes verified: 22/22
node verdicts: {'confirmed': 9, 'plausible': 11, 'unverified': 1, 'disputed': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 12, 'contradicts': 1, 'not_checked': 14, 'partial': 5}
books consulted: {'supports': 24, 'silent': 17, 'partial': 13, 'contradicts': 2} | by book: {'KLN': 18, 'FSD': 8, 'FVQ': 7, 'WEB': 6, 'MON': 5, 'BQT': 4, 'SKT': 3, 'AFA': 1, 'AFM': 1, 'ARY': 1, 'DEV': 1, 'PHN': 1}
```


## [2026-09-06T23:07:44.073Z] AGENT

Done. `python3 tools/verify_check.py 303` reports **0 PROBLEM lines**.

**Page 303 (book p. 273), single entry — ROOT "Layh, A.l.h" [Semitic/Syriac], 22 nodes**

- Root verdict: **plausible** (1)
- Node verdicts: **confirmed 9, plausible 11, unverified 1, disputed 1**
- Ref checks: supports 12, partial 5, contradicts 1, not_checked 14 (AHD main-dictionary pages, AKM, FVA, VDQ and the five empty Latin/French boxes are not accessible/carry no refs)

Flagged items:
- **ROOT (plausible)** — FVQ p.66, the very page cited, *does* print both glosses ("lāha to be high or to be veiled", "ʾalaha to worship") but as the Kufan/Basran grammarians' theories, which Jeffery then rejects: Arabic ʾilāh is "a genuine old Semitic form" and Allāh goes back to Syriac ʾalāhā. Modern: PS \*ʔil- "god"; the verb ʾ-l-h is denominal. Frame right, direction wrong.
- **#18 «الیزه ، شانزه لیزه» — disputed.** Élysée / Champs-Élysées are from Latin *Elysium* < Greek *Ēlýsion (pedíon)*, of unknown (pre-Greek) origin — no Semitic ʾēl. The other five words of the node (آمانوئل، دانیل، رافائل، الیزابت، ساموئل) are correct French→Persian.
- **#11 «اوریئل» — unverified.** AKM:64 is purchase-only; 0 hits in MON (aʿlām vols. missing) and BQT 1–5; fa.wikipedia «اوریل» redirects to آوریل (April).
- **#3 (plausible)** — two words off: Klein p.138 (Nourai's own citation) makes *Bābhel* a loan from Akkadian *Bāb-ilu*, not a Hebrew ʾēl-compound; and *Yisrāʾēl* is "he contends with God" (Klein, Etymonline), not "soldier of God".
- **#9 (plausible)** — English *Azrael* comes from Arabic ʿAzrāʾīl (Wiktionary descendants; Webster), not through Latin; Klein takes *Babel* and *Ishmael* straight from Hebrew.
- **#4/#14 (plausible)** — Arabic -īl is not a suffix but the frozen Hebrew element, and Jeffery shows the route runs through Syriac/Greek (the -s of إلياس is Greek), not Hebrew→Arabic direct. Nodes #6/#7/#16/#17/#21 are plausible for the same reason: the chart omits the Greek (Septuagint/NT) stage before Latin.

**Extraction errors: none.** I compared the JSON against the printed page at 400 dpi (including zoomed crops of the Persian boxes #5, #15, #18) — every word, script form and gloss in `data/extracted/batch/page-303.json` matches the book.

Output: `/home/sfmqrb/git/rishe/data/verification/page-303.json`. New archived web sources (11) are in `data/verification/sources/web/` with `index.jsonl` updated.
