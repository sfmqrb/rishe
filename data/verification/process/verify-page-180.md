# Verification process log — verify-page-180


## [2026-09-05T20:52:08.053Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 180 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-180.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-180.json. Write /home/sfmqrb/git/rishe/data/verification/page-180.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 180` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:52:10.611Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:52:11.288Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:52:11.304Z] TOOL RESULT

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


## [2026-09-05T20:52:11.589Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-180.txt"
}
```


### [2026-09-05T20:52:11.600Z] TOOL RESULT

```
1	=== PDF page 180 (book page 150) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ghdhem, Dhehem : earth  (refs POK:414; SYN:16; AHD:1513)
4	#1 (parent #0) [Avestan / Old Persian] refs=AHD; BQT:1032; KNT:177 | zam : earth
5	  #2 (parent #1) [Persian] refs=None | zamîn «زمین» : earth
6	  #3 (parent #1) [Avestan / Old Persian] refs=KNT:177 | u-vâra-zmi : good ... land ☞Su 1 | NOTE: The meaning of "vâra" is not clear
7	    #4 (parent #3) [Avestan / Old Persian] refs=BQT:22(Introduction),781; MON5:488 | huvârazmîš, xvarazmîš, xvârizem : An ancient city believed to be one of the original residences of the Aryan people (Airyanemwaejô). Now it is known as "Khiva" in central Asia between Uzbekistan and Turkmenistan, along the Amu Darya
8	      #5 (parent #4) [Persian] refs=BQT:781,805; MON5:488,491; KLN:49 | Xârazm, Khârazm «خوارزم» : a city in central Asia, modern Khiva ; Xârazmî «خوارزمی» : from Khârazm ; Xîveh, Xîvaq «خیوه ۱، خیوق» : Khârazm | NOTE: Khârazmî is surname of Abŭ Ja`far Mohammad ebn Musâ, the great mathematician of the ninth century. His great work "Al-Jabr wal Moqâbeleh" introduced the Arabic numerals and Algebra in Europe.
9	        #6 (parent #5) [Arabic] refs=None | Al-Xwârazmî : the ninth century mathematician
10	          #7 (parent #6) [Middle Latin] refs=AHD:33; KLN:49 | algorismus : the Arabic system of numerals
11	            #8 (parent #7) [French] refs=AHD:33 | algorisme, algorithme
12	              #9 (parent #8) [Persian] refs=VOP:17 | âlgoritm «آلگوریتم» : a type of computational procedure
13	              #10 (parent #8) [English] refs=KLN:49 | algorism, algorithm
14	#11 (parent #0) [Old Persian] refs=KNT:177 | ud-zma, uzma : grown up from ground ☞Ud 1
15	  #12 (parent #11) [None] refs=None | 
16	#13 (parent #0) [Latin] refs=AHD | humus : earth ; homo : man ; humanus : kind
17	  #14 (parent #13) [English] refs=None | humble, humility ; human, homicide ; humane
18	#15 (parent #0) [Greek] refs=AHD | gumon : man
19	  #16 (parent #15) [English] refs=None | bridegroom
20	
```


## [2026-09-05T20:52:15.069Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-180.json",
 "description": "Read source JSON page 180"
}
```


### [2026-09-05T20:52:15.122Z] TOOL RESULT

```
{
  "pdf_page": 180,
  "book_page": 150,
  "entries": [
    {
      "root": {
        "name": "Ghdhem, Dhehem",
        "lang": "Indo-European",
        "refs": "POK:414; SYN:16; AHD:1513",
        "gloss": "earth"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "AHD; BQT:1032; KNT:177",
          "words": [
            {"translit": "zam", "gloss": "earth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "zamîn", "gloss": "earth", "script": "زمین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "KNT:177",
          "words": [
            {"translit": "u-vâra-zmi", "gloss": "good ... land", "script": null, "see": ["Su 1"]}
          ],
          "script_extra": null,
          "note": "The meaning of \"vâra\" is not clear",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:22(Introduction),781; MON5:488",
          "words": [
            {
              "translit": "huvârazmîš, xvarazmîš, xvârizem",
              "gloss": "An ancient city believed to be one of the original residences of the Aryan people (Airyanemwaejô). Now it is known as \"Khiva\" in central Asia between Uzbekistan and Turkmenistan, along the Amu Darya",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:781,805; MON5:488,491; KLN:49",
          "words": [
            {"translit": "Xârazm, Khârazm", "gloss": "a city in central Asia, modern Khiva", "script": "خوارزم"},
            {"translit": "Xârazmî", "gloss": "from Khârazm", "script": "خوارزمی"},
            {"translit": "Xîveh, Xîvaq", "gloss": "Khârazm", "script": "خیوه ۱، خیوق"}
          ],
          "script_extra": null,
          "note": "Khârazmî is surname of Abŭ Ja`far Mohammad ebn Musâ, the great mathematician of the ninth century. His great work \"Al-Jabr wal Moqâbeleh\" introduced the Arabic numerals and Algebra in Europe.",
          "quote": {
            "text": "حافظ تو ترک غمزهٔ خوبان نمی‌کنی - دانی کجاست جای تو خوارزم یا خجند",
            "poet": "Hâfez"
          }
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "Al-Xwârazmî", "gloss": "the ninth century mathematician", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Middle Latin",
          "refs": "AHD:33; KLN:49",
          "words": [
            {"translit": "algorismus", "gloss": "the Arabic system of numerals", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": "AHD:33",
          "words": [
            {"translit": "algorisme, algorithme", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "VOP:17",
          "words": [
            {"translit": "âlgoritm", "gloss": "a type of computational procedure", "script": "آلگوریتم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:49",
          "words": [
            {"translit": "algorism, algorithm", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:177",
          "words": [
            {"translit": "ud-zma, uzma", "gloss": "grown up from ground", "script": null, "see": ["Ud 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "humus", "gloss": "earth", "script": null},
            {"translit": "homo", "gloss": "man", "script": null},
            {"translit": "humanus", "gloss": "kind", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "humble, humility", "gloss": null, "script": null},
            {"translit": "human, homicide", "gloss": null, "script": null},
            {"translit": "humane", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "gumon", "gloss": "man", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bridegroom", "gloss": null, "script": null}
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


## [2026-09-05T20:52:15.780Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:52:15.822Z] TOOL RESULT

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


## [2026-09-05T20:52:40.845Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','AHD','KNT','BQT','MON','KLN','VOP']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900])\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T20:52:41.587Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' data/verification/page-127.json",
 "description": "Look at an existing verification file format"
}
```


### [2026-09-05T20:52:42.637Z] TOOL RESULT

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
----
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
```


### [2026-09-05T20:52:42.673Z] TOOL RESULT

```
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
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
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
```


## [2026-09-05T20:52:49.639Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hðem\\|ghdem\\|ĝhðem\\|ghðem\" POK_01.txt | head -20",
 "description": "Grep Pokorny for ghdhem root"
}
```


### [2026-09-05T20:52:49.693Z] TOOL RESULT

```
3732:air.  duine  (*dliu-n-io-),  PI.  döini  (*dheuen-{o-),  cymr.  dyn,  corn.  bret. den  , Mensch*  (.Sterblicher*,  Brugmann  ZfceltPh.  3,  595 ff.);  s.  auch  unter ghdem-]
```


## [2026-09-05T20:52:49.917Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"dhghem\\|dhghom\\|dhgh\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for dhghem"
}
```


### [2026-09-05T20:52:49.967Z] TOOL RESULT

```
137:A word for the earth can be reconstructed as dhghem- (*dheghom). Other terms of lesser distribution designated forest or uncul- tivated land, like kaito- and welt- (wILD). Swampy or boggy terrain was apparently also familiar, from the evidence of the roots sel-es-, pele-', and *mdno-. But since none of these runs through the whole family, it would not be justifiable to infer anything from them regarding the terrain of a hypo- thetical original homeland of the Indo- Europeans.
145:A generic term for “fish” existed, dhghi- (also peisk- in Europe). The salmon (laks-) and the eel (ang”hi-) were known, the latter also in the meaning “snake.” Several birds were known, including the crane (gere-?), the eagle (or-), the THRUSH (trozdo-), the STAR-
150:Man and Society. For man himself, a number of terms were employed, with differ- ent nuances of meaning. The general terms for “man” and “woman” are wi-ro- (VIRILE) and *g”end- from g’en- (GYNECOLOGY). For man as a human being, the oldest word was apparently *manu- (man-'), as preserved in English MAN and in Slavic and Sanskrit. In other dialects we find interesting metaphori- cal expressions, which attest a set of religious concepts opposing the gods as immortal and celestial to mankind as mortal and terres- trial. Man is either *mortos, “mortal” (mer-2, “to die’), or *dhghomyo-, ‘“‘earthling”’ (dhghem-, “earth”).
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1638:HOMAGE dhghem- HOMBRE dhghem- HOME tkei-
1639:HOMEO- sem-! HOMICIDE dhghem- HOMILY sem-1 HOMINID dhghem- HOMO! dhghem- HOMO- sem-1 HOMOIOUSIAN eS- HOMOLOGOUS leg-1 HOMOLOGRAPHIC sem-1 HOMOLOSINE PROJECTION HOMONYMOUS nO-men- HOMUNCULUS dhghem- HONE! k6-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1662:ICEBERG bhergh-2 IcH dhgWher- ICHTHYO- dhghi- ICHTHYORNIS  or- ICICLE eis-2, yeg- ICON weik-3
1678:INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
1970:OLLA aukw- 2 OLLA PODRIDA pU-2 OMBRE dhghem-
2255:SIDE sé-2 SIDEREAL sweid-1 SIEGE sed-1 SIEGFRIED pri-, segh- SIEROZEM dhghem- SIEVE seib-
2401:TRANSHUMANCE dhghem-
```


## [2026-09-05T20:52:58.546Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==423' POK_01.txt | head -80",
 "description": "Print Pokorny page 414"
}
```


### [2026-09-05T20:53:00.451Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:53:03.559Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) pages\"; done; grep -n \"ghdem-\\|ghdem\\b\\|dhghem\" POK_full.txt | head -20",
 "description": "Count Pokorny pages and grep full"
}
```


### [2026-09-05T20:53:42.075Z] TOOL RESULT

```
== POK_01.txt: 363 pages
== POK_02.txt: 433 pages
== POK_03.txt: 429 pages
== POK_full.txt: 1 pages
21456:("mortal, human being', Brugmann ZfceltPh. 3, 595 ff.); s. also under ghdem-, 
34981:derived from Root/ lemma: ghdem-, ghdom-. Gen.- ablative gh(d)m-es lAeaw\wQ\ " earth, 
37728:Root / lemma: ghdem-, ghdom-, Gen.- ablative gh(d)m-es 
37740:Root/ lemma: gerrt^-, gixt"^-: to bite; tooth ' derived from Root/ lemma: ghdem-, ghdom- 
47231:common Old Indie gh- > ks- : Hittite gh- > tk- : gr. tk- > kt- see Root / lemma: ghdem-, 
51221:common Old Indie gh- > ks- : Hittite gh- > tk- : gr. tk- > kt- (see Root / lemma: ghdem-, 
63645:lemma: ghdem-, ghdom-. Gen.- ablative gh(d)m-es\ earth' 
85056:Tocharian - Greek -g"h- > -kt-: -tk- see Root / lemma: ghdem-, ghdom-. Gen.- ablative
```


## [2026-09-05T20:53:44.361Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37720,37820p' POK_full.txt",
 "description": "Print Pokorny ghdem entry"
}
```


### [2026-09-05T20:53:44.437Z] TOOL RESULT

```
References: WP. I 465 f., WH. I 470, Trautmann 77. 
Page(s): 449 



Root / lemma: ghdem-, ghdom-, Gen.- ablative gh(d)m-es 

Meaning: earth, man, dragon 

Note: It was developed from the zero grade, from where the simple aniaut gh- a\so in 

lengthened grade spread forms (about Old Indie aniauts y/r?-, ^/77- besides /rs/r?- compare 

Johansson Xenia Lideniana 1912, S. 116-126) 

Comments: 

Root/ lemma: gerrt^-, gixt"^-: to bite; tooth ' derived from Root/ lemma: ghdem-, ghdom- 

, Gen.- ablative ^^(^d[^/77-es Meaning: ' earth, man, dragon ' because the ancients believed 

that their ancestors killed the dragon, planted his teeth in the ground and fierce men were 

born from the ground, snake peeled its skin and was reborn again, that is why warriors 

venerated the snake as the source of immortality in battle. 

Material: compare to aniaut still Wackernagel Old Indie Gr. I 129, 241, pp. 109, 209bY, III 

241 ff., SchwyzerGr. Gr. I 326, 631, 10, Benveniste BSL 38, 139 ff., Specht Dekl. 241. 

Old Indie stem ksam-, Nom. Sg. ksah{= Avestan za) f. 'earth, ground; face of the earth, 
earth's surface' [common Old Indie gh- > As-], (Akk. ksam = Avestan z^nr, Lok. ksam/an6 
*ksam, if ksamanirom this form with postposition *e/7'in' to define is, compare Old Indie 
pari-Jman^ all around on the earth'; Instr. y/775; Gen. Jmah, secondary gmah, ksmah); 
ksamya-h^p\ace6 on earth, earthly '; 

Avestan za, Akk. z^m, Lok. zeme. Gen. za/77o"earth, ground, earth; face of the earth, 
earth's surface'; 

Note: 

the -/77- suffix similar to alb. delme' sheep ', zjarm " fire '. Illyrian Nominative is the same 
as Indo Iranian and in general Indo European Locative. 

gr. x6wv f. "ground, earth; face of the earth, earth's surface' (*x0wm; thereafter with v 
also Gen. x0ov6(;, x06vio(; "subterraneous, underground' etc.), xciMCi' originally ' on the 
ground, to earth ', (in addition to the other vowel gradation = Old Prussian 55/77/775/ "low' 
and presumably also = Latin humfio bottom'), xai-ia^s to the ground, on the ground ', 
XajjriAoc; "low', xQaMoAoq " near the ground, on the ground, low ' (: Latin humilis), perhaps 
v£o-xij6(; ' new, always of things, drastic, egregious, rude, flagrant, discourteous, impolite 
(*low)'; 



Phrygian ^spsAw (thrak. IspsAri) 'mother earth' (?), also Phrygian ^spsAsv pappapov 
C(v5paTTo5ov Hes. (compare russ. de/oi/e/r 'person' and 'servant') ; fSav Ma 'XGcbv Ma' 
can be genuine Phrygian (Indo Germanic e> Phrygian a), gd- : z- as Old Indie ksah: 
Avestan za; common Old Indie gh- > ks- 

alb. (y/7e 'earth' (= xQwv) ; 

Note: 

Albanian oT?© 'earth' : Phrygian ^spsAoj */hi/forthe non -colouring laryngeal. 

[common Old Indie gh- > ks- : Avestan gh- > gz-] 

Note: 

[common Old Indie gh- > ks- : Avestan gh- > gz-] 

Avestan gz- > Greek x0- > Baltic dz- > lllyrian d- : Baltic dz- > Slavic z-] 

compare gr. AriMHTrip, Doric Aaparrip, Thessalian AaiJijarrip, Aeolic Acjo^jarrip; lllyrian Aw-, 
Aap- (Pisani IF. 53, 30, 38) from Indo Germanic *gdhd, respectively Vokat. *gdhom, about 
Aapia, epithet of Demeter, s. WH. I 321 ; 

Note: 

Clearly AriMHTrip 'mother earth' was shaped according to lllyrian and alb. phonetic laws 
[common alb. gh- > d-, dh-] Anpn-Trip common venetic lllyrian suffix -ter,-tre . Therefore 
AriMHTrip is an lllyrian goddess of earth. 

Note: 

gr. AnMHTiP 'mother earth' : Old Irish duine, cymr. dyn, corn. bret. den: lllyrian AriMnTiP. 
alb. oT?© cognates evolved according to lllyrian and alb. phonetic laws [common alb. gh- > 
d-, dh-] suggesting a shared origin of those lang. 

Latin humus {irom * homos) 'earth, ground, earth; face of the earth, earth's surface', 
probably reshaping of an old consonant -stem *ghom-\ hence also f. as xQwv; humilis 'low' 
(: x0C(piaA6(;); in Oscan-Umbrian *homi-teros, -temos as Kompar. Superl. of Lok. *hom/ 
'under' (: Old Indie ksami) : Oscan hL{n]truis^ below, beneath, underneath, lower ', huntrus 
' below, beneath, underneath, lower'; Umbrian hutra, hontra^ on the underside, below, 
underneath ', Abl. hondomu^ the lowest '; Umbrian hondu^ pessumdato ' from * hon(d)-tdd, 
about Latin humanussee below;
```


## [2026-09-05T20:53:48.042Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37820,37940p' POK_full.txt",
 "description": "Continue Pokorny ghdem entry"
}
```


### [2026-09-05T20:53:48.086Z] TOOL RESULT

```
Old Irish du, Gen. o'lo/7'place' (Pedersen KG. I 89, s. also under to duine; the 
development from ghdio d- similar to /from -kt^-\v\ art'bear' from efkf^os, /? instead of -/77- 
as in xQovoq extended from the full grade *ddn- from *ddm - from du); 

Note: 

Old Irish du/ne, cymr. dyn, corn. bret. den: lllyrian AnMHTrip, alb. oT?© cognates evolved 
according to lllyrian and alb. phonetic laws [common alb. gh- > d-, dh^ suggesting a 
shared origin of those lang. 

Lithuanian zeme, Latvian zeme. Old Prussian same, semme'eadW, semma/'base, low' 
(: xci|JC('. see above), Latvian zem 'under' (probably VerkiJrzung of Lok. zenn§)\ Lithuanian 
zemas, Latvian zemslow'; 

Old Church Slavic ze/77^5 'earth'; in addition also Old Church Slavic zmtja'snake' 
("creeping on the earth'), zmbjb 'dragon' : gr. x0C(|jaA6(; ' near the ground, on the ground, 
low '. 



layoe aiD. {~dnemie) dnemje eartni^^^^^MfTmponanOe^j^ffi 

In addition words for "person' as " earthly,of the earth ': 

Latin homo, -//7/s "person'. Old Latin hemo {a\so in nemo^ nobody, no person, no one ' 
from *ne-hemd), Akk. hemonem, to /7^/77^s probably humanus^ human, of human beings, 
of people; humane ', with unclear vocalism {*ho/m-\Nur6e to o/of Old Irish PI. do/n/ 
"people', whether here lay before an older diphthong, but for Indo Germanic *gdhoim- 
lacks every probability; s. also under); Oscan-Umbrian 770/770/7- (ablaut grade *ghom- as 
humus, compared with Latin /7e/770/7- or dialectic umlaut from *hemdn-), Oscan humuns^ a 
human being, man, person ', Umbrian homonus^ a human being, man, person '; 

Gothic guma. Old Icelandic gumi. Old English guma. Old High German ^0/770 "person, 
man, husband'. Modern High German in Braut/'-gam {\ndo Germanic *ghemon- or *ghomon- 

); 

Lithuanian (old) z/77i/d'(Dauksa m. Akk. zmun/) "person', nowadays zmogus, zmdgus{g- 
forms as in Old Church Slavic mg-zb) "person'. Old Prussian smoy{\eQ. smoal), other 
formations Old Prussian smunentsm. "person', smonenaw/ns6s., and smun/'t "person', 
Lithuanian zmonai. "wife, woman', zmdnesP\. m. "people' (Akk. PI. z/77d/7/sdial. from Indo 
Germanic ghmoPens). 



Pedersen (KG. I 69, 89, 116, 173) places here also Old Irish duine, cymr. dyn, corn, 
bret. o'e/? 'person', Proto Celtic *don/o- irom *ghdomJo-= x66viO(;, Old Indie ksamya-lj, 
however, this would be the only evidence for Celtic /7/from mj, it could be considered the 
transference of /7fronn the paradigm *o'o/7 'place' (see above). However, then the PI. Old 
Irish dofni, nir. o'ao//?© 'humans, people' (typical diphthong) would have to be separated 
from duine; far likely it is connected dofni as *^^euenJo-ox *^^ouenJo-dx\^ duine eic. as 
strong grade *d'^un/o- with Gothic diwans' perishable, mortal ' connected (see '^^uen- 
under d^e^z-'die'); incredible Borgstrom NTS. 12, 83 f.; 

Note: 

common lllyrian-celtic gh- > d- 

Tocharian A so/n'lad, young boy, youngling ', B saumo, PI. S5/77/7a 'person' (: Latin 
fiemonem); s. Pedersen Tochar. 107 f.; 

Hittite te-e-kan{tegan). Gen. tagnas'ear\h' and Tocharian A tkam, Gen. tkanis, B kem 
ds. 

Luvian: tiyamm(i)- 

Meaning: earth' 

Attestations: [NSg] ti-ya-am-mi-is: 54 ii 41.42.43*.51.iii 28 .35; 56,2*; KBo XXIX 40,5e. 

ti-ya-am-me-is: 107 ii 4*. 

[ASg] ti-ya-am-mi-in: 103 iii 13; 139 i 4(?).iv 10e(?). 

ti-ya-am-me-in: 107 ii 11. 

[D-LSg] ti-ya-am-mi: 94, lie; VII 53 + XII 58 i 59e; KBo XXII 254 Vo 7*. 

[ErgSg] ti-ya-am-ma-an-ti-is: 39 ii 15. 

[GenAdj] 

[NSgC] ti-ya-am-ma-as-si-is: 45 ii 26; 107 ii 12*. 

[NPIC] ti-ya-am-ma-as-si-in-zi: KBo XXII 254 Vo 1 1*. 

Commentary: Delocatival formation, as per Kimball, Hittite Plene Writing 42720, NOT 
direct formal match of Hittite tekaii. 



Hittite: tekan n., gen. taknas ' earth ', dagan, tagan ' down, to the ground '; HLuw takamia ' 
earth ', Luvian tiyammi- id. (Friedrich 204, 220) 

common Old Indie gh- > ks- 

Note: 

Common Hittite Tochanrian gh- > tk- : common Old Indie gh- > ks- : lllyrian Albanian gh- > 
dh- : Celtic gh- > d-. 

They derived through metathesis from * g(e)dhom-, *gh{e)dhom {Pe6ersen Group. 41 f.), 
these explained from Indo Germanic '^'^{ejghom (Kretschmer Gl. 20, 66 f.); against it with 
substantial reasons Beuveniste Mel. Van Ginneken 193 ff.; a root in *d^egh-p\aces also 
Specht Dekl. 241; I with Benveniste would rather keep away the Hittite and Tocharian 
forms. 

References: WP. I 662 ff., WH. I 654 f., 663 ff., 869, Trautmann 369. 
Page(s): 414-416 

Root / lemma: ghd/es {zero grade ghdi^), vereinfacht (?) to ghdes, ghies, ghes 

Meaning: yesterday 

Material: Old Indie hyah^ yesterday ' {ghies), hyastana-h^ yesterday'; 

Latin hen, here^ yesterday ', hesternus^ yesterday' (from * hestr/nos \N'\t\r\ -tro-as in 
Germanic *gestra-); Common Old Indie : Latin gh-> h-.
```


## [2026-09-05T20:53:57.146Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | head -60",
 "description": "Print Kent page 177"
}
```


## [2026-09-05T20:53:58.166Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Uvārazm\\|Uvarazm\\|uvarazm\\|Huvarazm\\|hUvarazm\" KNT.txt | head -20",
 "description": "Grep Kent for Uvarazmi"
}
```


### [2026-09-05T20:53:58.780Z] TOOL RESULT

```
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
Ariya- adj. ‘Aryan’ (perhaps Ariya-, §126): Ау. atrya-, Skt. drya- ‘noble’, cf. NPers. ёгт ‘Iran, Persia’, Irish Eire ‘Ireland’, to pIE root *er-, OP ar- (585.1, §144.1). See also Ariyacica-, Artydramna-. Ariya паш. DNa 14; DSe 13; XPh 18. ariyd isn. as sb. ‘in Aryan (language) DB 4.89.
Ariyacica- adj. ‘of Aryan lincage’ (5161.18): Ariya- + ciga-. Artyacica пет. XPh 13; Ariya cica (written as two words, $44) DNa 14f, DSe 18f.
Ariydramna- sb. ‘Ariaramnes’, great-grand- father of Darius: Elam. har-ri-ia-ra-wm-na, АКК. ar-ja-ra-am-na-', Gk. 'Ариараштѕ. From ariya- + pass. pte. of d-ram- (8131; Av. Skt. ram- ‘to be at peace, to pacify’): ‘Having the Aryans at peace’ (8161.]1c). Hardly Ariyà pl. + ramna- (Foy, KZ 35.9), or Ariya- + aramna- pres. pte. mid. to ar- (Hz. Ар! 287). Anydramna nsm. AmH 1, 4, 9; DB 1.5; DBa 7; as gsm. AsH 3 ($313.1). Ariydramnahyé gsm. DB 1.5; DBa 7.
aruvü- sb. ‘action’ (JNES 444, 52; 53511, $150; so also Bv. TPS 1945.42-3): fem. to adj. arwa-, Av. aurva- ‘schnell, tapfer’ (Bthl. AiW 200), doublet to Av. aurvant- (q.v., under aru- vasta-).  aruváyà \sf. DNb 38 (inscribed afuvayá, $55.11; not anwasa with Wb. Grab 28, KIA 94;
OLD PERSIAN
not to be emended with Hz. Ар] 293-6 to aruvāðā ‘love’, cf. Av. urvafa- ‘amicus, befreundet’, ВЕЦ, AiW 1537; dfusdyd acc. nt. pl. ‘measures to be taken’, from *épy-dia-, acc. to Pisani, Riv. Stud. Or. 19.82-5, to root *&p- ‘get’, of. Av. afonte ‘they obtain’, Bthl. AiW 70 and 72, note 1 to ap-).
aruvasta- sb. ‘activity’ (INES 4.50-2, 232), ‘physical prowess’ (Bv. TPS 1945.40-1): -ta- ab- stract (5145) to arvani- ‘moving’, Av. aurvant- ‘schnell, tapfer, Held’ (ВЫ. AiW 200), Skt. ar- vant- ‘running, hasting, horse’, from Ar. ar- ‘move’ + suffix -vani- (535.11, §85, §126, §157), ef. Lt. orior ‘arise’; cf. АКК. translation '2t-ba-ru-tum ‘ac- tivity’, to abdru ‘be strong’ (Schaeder, OLZ 43.280-03). See also aruvi- Not with Hz. RHRel. 113.29-31, ApI 80-6, ‘Gut-sein’, to Ау, urvafa- ‘amicus’, with it-ba-ru-tum as ‘companion- ship’ to ibru ‘friend’ (cf. JNES 4.51); no valid evidence for meaning in Arm. loanword arwest ‘wonders’, cited by Nyberg, Rel. 351, from St. John 448. arwastam nsn. DNb 31, 33; asn. DNb 4.
Arza- sb. ‘Arkha’, an Armenian rebel (531, $164.V): Elam. ha-rak-ga, АКК. a-ra-hu. Атта nsm. DB 3.78, 91°; 4.28f; DBil. Arzam asm. DB 3.82, 89.
arjana- sb. ‘ornamentation’, as shown by АКК. : si-im-ma-nu-u ‘decoration’ (§84, §126, 8147.1): for meaning, see JAOS 51.208, 53.13, 53.19, Schaeder, Arch. Anz. 47.272-4, against Hz.’s ‘lime- stone’ (AMI 3.52-3) and ‘building material’ (ApI 88-93). Cf. Av. pres. arga- ‘be worth’, Skt. árhati, and Ars. РЫ, arzün, NPers. arzün, Av. arojah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSI 41f; arjanam-Sary DSf 23°.
arta- sb. ‘Law, Justice’, an archangel attend- ing Ahuramazda: pte. to ar- as sb., Av. aša- and arata-, Skt. rid- ‘cosmic order’, Lt. ortus -‘risen, originated’, pIE *rto- ($30, $66, 5242.1). See also Artaxsaca-, arlavan-, Artavardiya-. ^ arid-cà isn. (8252.1, Lg. 21.223-9) XPh 41, 50f, 531 (not with Hartmann, OLZ 40.145-60; nor with Nyberg, Rel. 367, 478; Bailey ap. Nyberg, Rel. 478; Henning, TPS 1944.108; hardly, with Sen 155, artäcã braz- maniy apn. ‘and the divine fulfillments’; nor with Pisani, Riv. Stud. Or. 19.85-8, as elliptic dual ‘Arta and Brazman’, the -cé connecting with the preceding Auramazdém, and Brazman being the OP for the Av. vohü man ‘Good Though
```


### [2026-09-05T20:53:58.825Z] TOOL RESULT

```
2132:Nom. Sg.: Uvárazmiy Uvārazmiš, Baztriš; Harau- valiá (Skt. sárasvati), Sikalyaluvatis; apis (in айт = dpif-&m), BU ‘earth’ (ideogram only).
2143:I. The -- stems and the -i- stems fell together in OP into one declensional paradigm, having nom. sg. -1&, acc. -tm, gen. -ais, abl. -cya* (= Skt. -уӣз), loc. -îy (= Skt. -yà-m), nom. pl. -iya*. The only survival of separate declensional forms is nom. Uvarazmiy, with original -7, replaced in later inscriptions by Uvdrazmis. There is the possibil- ity that when nom. -i of -i- stems took the ending -8, the length of the vowel remained to distin- guish the -i- stems from the -i- stems; and simi- larly the long vowel in асе. -im may have re- mained. The OP system of writing leaves this am- biguous. But 1 is more likely that the new ending -i§ and the old ending -im became 2 and -їт in imitation of the corresponding forms of -{- stems.
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4576:21 : Haraiva : Baxtn$ : Sugda : Uvarazmi
4719:8 iyam : Uvarazmiya 9 iyam : така
5212:Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
```


## [2026-09-05T20:54:08.474Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if 'Uvárazmi- sb.' in p or 'Uvarazmi- sb.' in p:\n        print('leaf idx',i,'-> printed', i-15, i-13)\n        print(p[:200])\nEOF",
 "description": "Locate Kent leaf for Uvarazmi"
}
```


## [2026-09-05T20:54:09.437Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^zam-\\|zam- sb\\|uzma\\|ud- \\|uzmá\\|Ud-\" KNT.txt | head -30",
 "description": "Grep Kent for zam and uzma"
}
```


### [2026-09-05T20:54:10.249Z] TOOL RESULT

```
leaf idx 200 -> printed 185 187
B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.
Uvárazmi-
```


### [2026-09-05T20:54:10.299Z] TOOL RESULT

```
211:BSOS - Bulletin of the Sehool of Oriental Stud- ies, London. ;
1128:Final -d disappeared after 1, as in the enel. OP -cly, Skt. cid, pIE q*id; OP лаш ‘not’, Av. лб, from *ne + id. After и the final t seems to be retained as § in OP akunaus ‘he made’, adarsnaus ‘he dared’, Skt. ákrnot ddhysnot; but this § is better taken as an extension of the s of the aorist, after which -t would be lost. The prefix ud ‘up’, which appears unchanged before a vowel in ud- apatatā ‘he rose up (in rebellion)’, suffers com- plete assimilation of the d in uzma- ‘stake’ (from *ud-zma-), and became us- in us-taSand- ‘stair- case’ in the dental cluster (585).
1608:This shortening took place in most languages before and after consonants; OP example: uzma- ‘stake’ from *ud-zma-, §84.
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2599:II. The secondary ending was pIE -io, as in Gk. ёферєто, Skt. dbharata; this is seen in OP ud- араай (Gk. &érero, Skt. épatata), anayatà (Skt. dnayaia), amariyata, früámáyalà, agarbüyatà, agau- bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, [ат]аоаій, passive akunavayatd, perhaps aor. (h)amarmalà and perf. pass. cazr[zyala] or [claxr|iyata]; non-thematie remade to thematic, avarnavaté and aisiata; non-thematic aor. akula (Skt. dkria) and imf. patiy-ajatd (Skt. dhata).
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2705:B. Expressing place to which, with prep. уйй ‘as far as’, in DSf 32 abara yata Bābiraw ‘carried as far as Babylon’, 34 у010 Сй {уа ‘as far as Susa’; perhaps also, because of the idea of motion which seems to be in the verbs, in gátavà avástáyam (DB 1.62f), güfavü niyaSadayam (РМа 36), maškđuvā avükanam (DB 1.86), uzmayà-patiy (DB 2.76, etc.).
2864:(DB 2.16°, 3.26), ‘оп’ with locative in uzmayá-
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
3634:9] uzmayapatiy :akunavam p :8tly : Daravavaus : xšāyaðiya : ma : tya : ma
3646:Rl. has the following correct readings, in whieh he records as visible certain characters, here indicated by roman type, which were not visible to KT: * Naditabai- fram; *бай]у : Dárayavaus; *aham : i[mà; * Auri; з rhiyal6iya; * nama : var[danam; ” avais;  Dárayavaus : xéáya[frya; ? haeáma; * hya; * mahya : VI : ralucabes (VI is corrected to VIII by КІ. on page 218); * parazta : pat(is; 9 Armaniyaiy (RI. misread the third character); * vasiy; * ham[igrya; *! Uvaz[Stra]hyá; *! uzmayapat]iy.
3730:90 ауайуа : pasiva : adam : ava : Vahyazd&tam : uta : martiya : 51 tyaisaiy : fratamā : anuSyáà : Shata : Uvidaicaya : пата : var 92 danam : Parsaty : avadasiS : uzmayápatiy : akunavam : 64
3767:92 uXiyà : &hatà : Babirawv : uzmayāpatiy : akartyata
4956:Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
4995:and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
5177:ud prep. and prefix ‘up’, becoming Iran. us- uz- before dentals ($85): Av. us- uz-, Skt. ud, pIE *ud (and *üd in NEng. out, NHG aus): ud with verbal root раф, us- in ustaxand-, u(z)- in uzma- (S84).
5226:uzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5372:gud- vb., see gaud-.
5624:ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
5807:yaud- vb. ‘be in commotion’, present stem yauda-: Av. yaoz- ‘boil up’ (§88), pres. yaoza- (Hz. AMI 8.67, ApI 362-5); not to Av. yaod- ‘fight’, Skt. yudh-, because of the difference in the present stem (Av. yüióyeiti, Skt. yüdhyati; JAOS 58.116).  ayauda imf. (5213) XPh 31f (not dyauda пзш. ‘rebellion’, as taken by Henning, BSOS 10.505, which is refuted by Akk. version). ayauda" 3d pl. imf. (5232.П) DSe 33°. yau[da*- tim] asf. pres. pte. act. ($190.1, $240) DNa 32.
```


## [2026-09-05T20:54:18.573Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    for key in ['uzma- adj','Uvárazmi- sb','ud prep','zam- sb','zam- ']:\n        if key in p:\n            print('leaf',i,'printed~',i-15,'key',key)\nEOF\ngrep -n \"zam- sb\\|Ζam\\|'earth'\" KNT.txt | grep -n \"zam-\" | head",
 "description": "Map Kent leaves"
}
```


### [2026-09-05T20:54:20.315Z] TOOL RESULT

```
leaf 20 printed~ 5 key zam- 
leaf 65 printed~ 50 key zam- 
leaf 198 printed~ 183 key ud prep
leaf 200 printed~ 185 key uzma- adj
leaf 200 printed~ 185 key Uvárazmi- sb
leaf 200 printed~ 185 key zam-
```


## [2026-09-05T20:54:28.746Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nprint(len(pages))\np=pages[200]\nprint(repr(p[:300]))\nprint('---- zam context ----')\ni=p.find('zam-')\nwhile i!=-1 and i<len(p):\n    print(repr(p[max(0,i-300):i+300]))\n    print('======')\n    i=p.find('zam-',i+1)\n    if i>20000: break\nEOF",
 "description": "Inspect Kent leaf 200"
}
```


### [2026-09-05T20:54:30.756Z] TOOL RESULT

```
232
'B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.\nUvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk'
---- zam context ----
"d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.\nUvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.\nUvürazmiya- adj. ‘Chorasmian’: deriv. to pre- ceding ($144.11). (Uvarajzm*ya (822) nsm. APP 8. |\nwar Stika- sb. ‘good spearman’: u- ‘good’ +"
======
'sk, Skt. $ügka-, Sisyatt ‘dries’, Lith. saüsa-s ‘dry’, NEng. sere, sear ($146.1). uškahyā gsn. DPe 13.\nushamaranakara- sb. ‘good warrior’: u- ‘good’ + hamaranakara- ‘warrior’ (§140.VI). ushamara- nakara nsm. DNb 34.\nuzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.\nka- interrog.-indef. pron. ‘who’: Av. Skt. ka-, Gk. то-, Lt. quo-, NEng. wha-t, pIE *q*o- ($201). See also Ка, -katy, ci- (§132.'
======
```


## [2026-09-05T20:54:42.476Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages):\n    if 'LEXICON' in p.upper()[:400]:\n        print('leaf',i, repr(p[:120]))\nfor i,p in enumerate(pages):\n    if p.strip().startswith('zam-') or '\\nzam-' in p:\n        print('ZAM leaf',i, repr(p[:100]))\nEOF",
 "description": "Find lexicon start and zam entry"
}
```


### [2026-09-05T20:54:44.187Z] TOOL RESULT

```
leaf 2 '� i\nтег. E\nEAD Мут\nOLD PERSIAN\nGRAMMAR TEXTS LEXICON\nBY ROLAND G. KENT\nProfessor Emeritus of Indo-European Linguistics\nU'
leaf 4 'y whose courtesy tt appears here\nFOREWORD\nThis volume has been prepared to meet the need for a comprehensive treatment o'
leaf 20 'gs and uses; fuller discussion will be found in the phonology and in the Lexicon, s.vv.:\nI. Place-Names:\nAsagarla ‘Sagar'
leaf 34 'ch problems must be settled by etymological comparison or by comparison with borrowings in other languages; but these ar'
leaf 193 't’).\n-\nLEXICON\nч.\nАтах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. i'
leaf 227 'ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. '
```


## [2026-09-05T20:55:01.544Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages[193:],start=193):\n    if 'zam' in p and ('‘earth’' in p or 'earth' in p):\n        for line in p.split('\\n'):\n            if line.strip().startswith('zam') or 'zam- sb' in line or 'BU ' in line:\n                print(i,'|',line[:400])\nEOF",
 "description": "Find Kent zam entry"
}
```


### [2026-09-05T20:55:03.280Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:55:07.306Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bümi\\|būmi- sb\\|bumi- sb\" KNT.txt | head -5; echo ===; python3 - <<'EOF'\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=data.split('\\f')\nfor i,p in enumerate(pages[220:],start=220):\n    idx=p.find('zam')\n    if idx>=0:\n        print('leaf',i, repr(p[max(0,idx-200):idx+300]))\n        print('---')\nEOF",
 "description": "Search late Kent leaves for zam"
}
```


### [2026-09-05T20:55:08.990Z] TOOL RESULT

```
Exit code 1
641:$2. Tue InEoGRAMS are five in number, stand- ing respectively for s8dyabiya ‘king’, dahydus ‘province’, bümi$ ‘earth’, Auramazdá ‘Ahura- mazda’, and baga ‘god’; they are transcribed by Хо, DH, BU, AM, BG. In DSk 4 there is what seems to be a ligature for AM-ha,
652:DSf has both bümim and BU Вуй; otherwise XS and DH, but, Auramazdà and baga in full.
653:DSm, as restored by Brandenstein, WZKM 39.55-8, has XŠ and тїйуабтуат, DHnàüm and dahydva, bümiyà, AMhà and AMmaiy; it is probable that all the words should be written
656:pSt, as restored, has XS and х&йуабиат (both entirely restored), and bümim Auramazdà ba- gaibis; this should not be, but I fail to see any alternative. j
658:Ае agrees with DSf; it has bümim and Вуй, otherwise XŠ and DH , but Auramazdà and baga.
(eval):1: == not found
```


## [2026-09-05T20:55:14.483Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zam- \\[f\\]\\|zam-, f\\|zam- f\\.\\|^zam-\\|zǝm\\|zam-\" BRT.txt | head -30",
 "description": "Grep Bartholomae for zam"
}
```


### [2026-09-05T20:55:14.527Z] TOOL RESULT

```
7114:KompE.  —  Et.?  Vgl.  äxSiay—  ')  So  J  lo,  ba0mm{%^)  vTbaraitl ahmät'..hazam-ayna Ei;  na.  mit  Fi  "//.  paiH-jasaiti  ätar^{m.  A)  VrA'.So;  Vyt 5i;
19219:AbleiL  aus  'm-vaza.  m.  'attraclioii'");   ai.  ni-       Ableit.  aus  *»i-zam-  Adj.  'in  die  Erde  hinein väha-  m.  'Abnahme  (der  Tage)',  vgl.  iihaiä-       gehend'.  —  Vü.:  fa  nÜBnih.  ~  1)  Wörtl.  'duos Adj.  -herheiführend  .  —   O  Anders  Gdn.  KZ.  .      digjtos  altitudinis'  im  Sinn  von  'in  altiludinem 25-  401  {'geschnürt')  und  Dst.  ZA.  3.  395,  der       duorum  digitotum'. np.  tiavSk  'schmeichclod'  vergleicht  (s.  auch
27690:•  j-t  g-  (.  P-)  zam-  f.'>  'Erde';  i)  als  die Stätte  alles  MaterieUcn*>,  'Erde,  Erdober- fläche, Erdboden,  Erdreich";  zam  (AS.) pirtk'WJm  .  .  ya  bar?%ri  paraos  srTrahe yü  vtsp^m  ahum  astvantim  baraiii  Yt  13, 9;  Y.io.\,  3S.1,  i^.i;  —  ai^Ai  z?mS (GS.)  yal  pa%anayä  skannayh   dOra^a-
28099:j.,  g.   iiiH',    Kasusf.:    %,    unter   zam-    and zyam-,
28102:Ableit.    aus    zam-.    —    Pü, ;  zaniiken,  an  i  za- mii.  —   I)  Hds.  'Hiitya.
30550:•  j.  huSkö.zam-  1)  f.  'trockene  Erde'; I  istyehe  v3  sarstvahe  va  'amanam ''  vä \pqsnam    "Staub    von  . ,  trockenen    Etd-
```


## [2026-09-05T20:55:20.599Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# find leaf index of line 27690\nimport re\nn=0\nfor i,l in enumerate(lines[:27700]):\n    n+=l.count('\\f')\nprint('formfeeds before line 27690:',n)\nprint('\\n'.join(lines[27680:27700]))\nEOF",
 "description": "Locate Bartholomae zam column"
}
```


### [2026-09-05T20:55:22.439Z] TOOL RESULT

```
formfeeds before line 27690: 906
•  j.  zantu.irik-  Adj.  'den  Gau  im  Stich lassend,  dera  Verderben  preisgebend':  ma buyama  ist^rö.irics  ma  nmanSiricö  .  . vTsSiricö  ..  "iricj  Yl  10.  j  $.
•  j.  zantu-san-  Adj.  'der  sich  den  Gau verdient,  erworben  hat':  paoiryqn  tkalli ■  .  nmänanqmia  .  .  zantunqmca  . .  nmsna- tahand  .  ,  'säfiö  (AP.)  Yt  13. 151,
Komp.;  ''iaii/av-\-'Aait:
•  '].  zanda-  m.  Name  gewisser  Häretiker*': ya'ha  'da{^V.) yatumsnia  m^rmcita gai%a as'ahe  V.7ÄSS; +F.20";  —  'dqmca  (GP.) yätumatqmca  Y.  61.  3.
•)  So  wird  Adalii  genannt  {saiidit);  Mx.  36. 16  «teht  zandBäh  neben  yäluhih.  Nach  PüEtl. ist  sand:  paylämiar  i  yätStän  u  pa  zand  yätükih Säyet  iarlan.  Vgl.  dazu  BARTHELEF4y  Gab.  39, DsT.  ZA.  /.  384.
Et  und  Bed.?     —    Pü.;   sand;     vgl.  *).     —
I)  Ilds.  zinda.
•  j.  *zainyävara*"  m.,  mit  GS.  il'äahe eine  Ortsbezeichnung:  ya%a  azani  ptlana *asta.aurvants  . ,  °rai  pasca  s^i^aht  "dass ich  dem  A.  eine  (siegreiche)  Schlacht  liefere .  .  hinter  ZJC"  Ytp.  30.
Wohl  *jfl»tt' (vgl.  saim.gav-i)+*i\'!,ara' teiV3> 'Wall,  Wehr',  lum  V.  ^var-)'1;  s.  No.  I  f.  — ')  So  die  beste  Lesung  in  F  i,  J  lO;  NA. Jainy.  —  I)  Wertlos  Gdn.  sYt  117,  DST. ZA.  2.  439- j.  tanva  Yt.  /,  37 :  lies  zalna.
•  j-t  g-  (.  P-)  zam-  f.'>  'Erde';  i)  als  die Stätte  alles  MaterieUcn*>,  'Erde,  Erdober- fläche, Erdboden,  Erdreich";  zam  (AS.) pirtk'WJm  .  .  ya  bar?%ri  paraos  srTrahe yü  vtsp^m  ahum  astvantim  baraiii  Yt  13, 9;  Y.io.\,  3S.1,  i^.i;  —  ai^Ai  z?mS (GS.)  yal  pa%anayä  skannayh   dOra^a-
dby  Google
i663  «un-  I
rayä  Yt  70.95;  —  »va  pa'tri  zgmS  ka- rana  Yt /p.  ag;  J2.  ao;  —  vJspqmüa  aipi imqm  sqm  Y. 57.33;  —  asticajm  ta (ND.)  avaid  bqtS  yavaiti  frahasclt  Y.ig. 7;  F.20,  ti.6y;  —  avavaitya  .  .  ya'ha  Tm zä  Y.ig.j;  ziL  *F.  4  a;  —  aoi  kafts.- karsvairlm  tarn  Y.  57.  23,  G.  5.  S;  —  ma- \}me  %rihe  *aähh  t»mS  "im  mittlern Drittel  der  Erde  hier"  Y.  jj.  7;  —  vimai- üTm  aiüka  S3ms  Yt.  Jo.  104,  12.21;  — ti/a  karatDm  ai^ha  simS  Yt. /a.  20;  — zqm  ahurahatqm  Yt5.  63,  85,  6.  1,2,  7,3, 75.48,  V.y.49,  75.21,26,35.  2^-4%  8, Y.fj.  29;  —  kS  paoirtm  imqm  zqm  ma- tilia  xmaoma  xsnJvayeiti  V._y.  la;  — fiSil  iJ  Tm  xä  sä  (sd.)  yj  danya  akaräa saita  V.J.  34;  — yS  imqm  zqm  aiwL- vir^zyeiti  ..  äaj  aoxta    Tm  zä  V.J.  25  f.;
—  pfrj'hwe  (sd.)  aiiiAs  z^mS  V.p.  2;  — kva  . ,  air>hä  ztmff  V.J.  i,  7;  YL 12.  aa, Y-  2J.  3,  F.  26;  —  aitala  .  .  airiAä  s?mU V.J.  18,  ö.  7,  Ä8,  16.  \2-,-~itaomi  z3mö ..  larärum  Y.  70.  4;  —  zsmS  *karsuyä (sd.)  F.5;  —  SÄva  vyarTitahva  zpmS  V. 77,3';  —  hankaine  paiti  aiäha  simS Yt.  5. 4 1 ;  V.  J.^.  6 ;  — p^rtne  Xm  ta  hangata patvqmla  .,  V. 2.9;  8;  —  yimS  imqm sqm  vJsävayaJ  .  .  V.2.11;  10;  —  naram . .  ySi  h»iiH  airihh  s»m5  maziütaca  . ,  V. 2.87;  27,  28',  j.  15,  40  PüZ,,  70.18;  — ys  .  .  /raxftaite  paiii  äya  sfma'^  mi^rS Yt.  70. 98;  7j.  97,  sg.  I,  y.g.  ao';  —  daiva ,  .  yBi  .  .  apatay?n  *paili  äya  z3mä*^  Y. 5.  15;  —  apa.ävarat  anrS  mainyus  kala z)mat  Yt  77. 19,  20;  — pasvas^a  . .  upairi zqm  vllarmta  masyäla   Yt.5.89;  75.34;
—  apB  yä  s^mä'''  paiti  frata^nti  Y.6ß. 3;  —  ap5..ya  tima''>  armaHta  ..  Y.6S. 6;  FrG.;  —  maiiyaäbyS  . .  yäi/  apairl *aya  s>mS'^  gaohls  *^yeintT  Y.72.  3;  — ,.  zjmäia^'*  uzuxfyänti  urvarä  Yt.  7j. 10,  14;  7,4;  —  nasunqm  yä  paiti  äya zgma**  irlri^arj  V.5.4;  —  daxmaSsva yBi  paiti  äya  z^mä'''  bavainti  V.  7.  54; — yat..U5  vats zqm  hagcayäiV.  5. 12;  ■ — sairi  .  .  z»m!  (LS.)"'  nioäite  .  .  z>ml'^ nikante  "ein  Kadaver  . .,  der  auf  den  Erd- boden hingelegt  . .  in  das  Erdreich  ein- gegraben ist"  V.  7. 45  und  47;  J.40FÜZ.; — mä  tl  «7"«(Sp.  1085)  *'z>me*>  paiti  Y.io. 17;  —  z?me'*  paiti  nidai^ita  Y.ö.^i;  A'. 76;  — yat  aiMk  i?mU  (alsLS,)*'  nikante spänasia  .  .  V.J.  36;  34,  Ä37;  —  ztmö
-3b
1664
(als  LS.)*>  nidaihyqn  V.  6.43;  7.39,  S. 10;  —  ufträvhs  .  .  *uzayantB  (sd.)  tfmat Yx.ij.iy,  —  yB  . .  var>s3m  t^mäta^^ sayarum  (sd.)  vafnaiti  .  .  Yt  14.  3 1 ;  — vans?m  ztmäp'^  avaoirihffttfm  Yt.  16. 10;
—  yB  hakat  astJica  ..  zimä^a'-^  kam.- rai%wayäti  (sd.)  Yt.  70. 72.  Daher  a)  oft im  Gegensatz  zu  a)  Himmel  und  Luft- raum: atitary  zqm  asmaiumca  Y.68.1^, Yt.<y.8,  io.95,  /J.13',  43,  44,  Y.Ol.i, H.7.16;  Yt  79.43;  —  vispqmca  zqm  .. vTspimca  asmamm  Y.  77,  9;  —  imqmla zqm  .  .  aomla  asmatam  "die  Erde  hier ..  der  Himmel  dort"  Yt7j.i53;  2,  77. 57,60; —  aiähäsia  ztmB  avai^htia  asnS Y.  7. 16;  —  kasna  djritä  zqmcä  ads  na- bäsiä  avapastöÜ {%A)  Y.44.  4;  —  s.  noch A.  ß)  den  Leuchten  des  Himmels: yetihe  växi  ,  ,  us  ava  raocä  asnaoiH  ava pairi  tmqm  sqm  jasaiti  Vt  70.85;  89, H.  7,  21;  —  ka^a  avatbyS  sitnbyB  aoi zqm  Yt5.85.  a)  Im  Gegensatz  lu Wasser  'Erde,  Land,  Festland':  aSavat apal  haca  nilbäraym  huskei^'A^  z?me''' nidaiiiyqn  V.(7. 29;  31;  —  zugleich  im Gegensatz  zu  Pflanzen:  zqm  akuraläiqm äptm  ,.  urvarqm  y.ig.$$;  5.33,  4a,  77. I,  a,  5,  9,  H,  7. 3;  —  Aa^a  apaj ..  z^mat •  ■  S^H  ,  .  urvarayät  V.  77.  10;  —  nava 3fs  .  .  tä  ..  urvarä  V.27.3;  —  ta^a fanti  sartta  äps  .  .  s»mB  . .  urvarayä V.  7. 3 ;  —  auch  Flur. :  imat  vS  äpS  Jaii- yemi  . .  z}mB  (VP.)  . .  urvarä  Y.  Ö3. 1  a;
—  apasca  z»mai(W,)/a  urvaräsca  yaza- maiiüVT.iG.s;  Y.  2. 16,  G.  2.6;  —  apqmca ztmqmca  urvaranqmla  Y,  7.  16;  V.  6. 3.  a)  mit  Wasser  zusammen  im  Gegen- satzzuHimmel:  asmamm..  äptm  ..sqm  .. gqm  Y.  2J.  I ,  Yt  7j.  2  8 ;  Y.  75,  z ;  —  avattht *ava^hela  altiB.. apasca  ztmasca  Yt/j.aS; 86,Y.79.8;  — a/näa/Za  apäafSa  zsmäaih''^ Vr.7. 4.  3)  ein  Stück derErdoberfläche von  bestimmter  Abgrenzung;  a)  'Land'  in politischem  Sinn:  *iqm  tamsi  (sd.)  zqm kuhrä  rumsi  ayint  Y.  46.  i .  b)  'Grund- stück': zqm  karsyim  *rasS>yqm  "ein urbar zumachendes  Ackergrundstück"  V.  14. 13; 13.  'S.  6;  —  lvant)m  dräjB  zrvängm  aiäkh z3mB  anaitya  yat  ahmt  spänas^a  narasca paradri%inti  "wie  lange  ruht  der  Bann auf  einem  Grundstück,  wo  . ."  V.ö'.  i;  i, a*,  3;  —  '^hixiäm  nanm  aSavatwm  . . drvatqm  . .  zqm  . .  nipärayanta  . .  anyam
```


## [2026-09-05T20:55:31.793Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; echo ===; grep -n \"خوارزم\" BQT_v2_pages.txt | head -20",
 "description": "Grep Borhan v2 for Khwarazm"
}
```


### [2026-09-05T20:55:31.849Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T20:55:35.061Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BQT_v2_pages.txt BQT_v1_pages.txt 2>&1; head -c 400 BQT_v2_pages.txt; echo; echo \"-----\"; grep -c \"pdf page\" BQT_v2_pages.txt",
 "description": "Inspect Borhan v2 file"
}
```


### [2026-09-05T20:55:35.119Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان�
-----
0
```


## [2026-09-05T20:55:39.040Z] TOOL CALL #26: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null; echo ===; sed -n '1,40p' tools/ref_page.py",
 "description": "Check ref_page tool and ocr cache"
}
```


### [2026-09-05T20:55:39.076Z] TOOL RESULT

```
Exit code 1
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
(eval):1: == not found
```


## [2026-09-05T20:55:41.620Z] TOOL CALL #27: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/BQT | head -40; echo ---; ls data/verification/sources/refs/ocr/BOOK | head",
 "description": "List cached BQT ocr pages"
}
```


### [2026-09-05T20:55:41.685Z] TOOL RESULT

```
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
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1624.png
1624.txt
172.vision.txt
1776.png
---
100.png
101.png
102.png
103.png
104.png
105.png
106.png
108.png
109.png
110.png
```


## [2026-09-05T20:55:45.884Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:781 --image 2>&1 | tail -40",
 "description": "Fetch Borhan page 781"
}
```


### [2026-09-05T20:55:47.498Z] TOOL RESULT

```
no scan of BQT covers printed page 781 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:55:50.759Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\"",
 "description": "Show BQT refs entry"
}
```


### [2026-09-05T20:55:52.510Z] TOOL RESULT

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


## [2026-09-05T20:55:56.976Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 241 265; do echo \"=== leaf $n (printed $((n+540))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -60; done",
 "description": "Print Borhan v2 leaves 241 and 265"
}
```


### [2026-09-05T20:55:58.780Z] TOOL RESULT

```
=== leaf 241 (printed 781) ===
‫خوان پابه‬                                                                                                      ‫یز پا‬
                                                      ‫خوالگر ‪ - ۱ )۱‬باانی معدوله بر باشد ‪.‬‬
‫حوان ه با نانی ممدوله بر وزن نان »‬                               ‫وزن شالگر (‪ .)۷‬مطبخی و طباخ و طعام پز را‬
‫کنابه ازخوردنی وماده باشد ‪ ۵‬و‪-‬طبق بزرگی‬                          ‫گویند ‪ - ۴‬و بمعنی سفره چی هم بنظر آمده‬
                                                                                                                    ‫است‬
          ‫را یز گوبند که از چوب ساخته باش‬
     ‫طندبچه‬
     ‫ق‬
‫کوچك راخوانجه گویند ‪ -‬وخاروخلاشه وگیاه‬                           ‫خو‌الی‪ -‬باانی ممدوله بروزن عالی»‬
‫خودرو را نگیفزته اند که از ميان زراعت قوت‬                         ‫وزبند ‪ - ۴‬ورود‬‫زیبا ومهنا باشد ‪ -‬وطعام رگای‬
‫برهسماند ‪ - ۷‬وبمعنی چیزی خواندن وطلیسن‬                           ‫خانهٌآب را همگفته‌اند ‪ -‬و بمعنی مطبخی نیز‬
‫هم هت ‪ - ۷‬و امرباین دومعنی آیمزده است‬                            ‫؛بکراول بروزن نهالی هم‬
                                                                                      ‫بنظرآمده است ‪ ۴‬و‬
                                 ‫بعنی بخوان وبطلب ‪. ۷‬‬                                                  ‫‪۰‬‬       ‫ات‬   ‫درست‬



‫خوان پایه ‪ -‬با انی معدوله و بای‬                                   ‫خوالیگر ‪ - ۴‬بنانی ممدوله بروزن‬
‫فارسی بالف کشیده وفتح نحتانی‪ .‬دستار خوالرا‬                        ‫بازیگرطباخ‌ومطبخی‌وخوالالار وسفره چی‌باشد؛‬
                                                ‫‪.‬‬     ‫فمف‬
                                                                   ‫و بکر اول نیزگفته اندکه بر ونزانلیگر‬
                                                       ‫‪:‬الك‪.‬‬
                                                           ‫(‪ )۲‬خم ش‬                 ‫(‪ )۱‬خ‪٠‬‏ ‪ :‬خوالك ‪.‬‬

        ‫‪۰‬ص‪.‬‬
          ‫‪۲ :۹!۱‬‬
               ‫‪ - ۱‬از ‪ :‬خوال (= خوار) ‪ +‬کر ( یوند فاعلی وشفلی ) رکه‪ :‬اسفا‬
                                         ‫‪ -‬ابن آفروشه‌است‪ ,‬دوزاغ است خوالگرش‬
                ‫هر دو قرین بکدیگر وليك در خورند‪.‬‬
     ‫‪ ۶‬ناصرخسرر بلخی ‪.*۸۱۱‬‬
‫‪-‬اوزا‪:‬لی ‪ -۳‬کر( پوند فاعلی‬
                         ‫خ‬                                   ‫‪.‬ك‪ :‬اسفا!‪۲ :‬ص ‪. ۰۹۱‬‬
                                                                               ‫‪ = ۴‬خوال ر‬
                                                ‫‪0‬‬                                              ‫وشفل) = خوالگر‬
            ‫بدیبا وخوالیگران خواستند ‪.‬‬                                  ‫یکی خانه او را بباراستند‬
     ‫فردوسی طوسی‪ *.‬لغت فرس> ‪۳۱۰‬‬
     ‫» کردی ع ‪nãx‬‏ »افغانی ‪naVX‬‏‬                ‫‪ 9‬تاوادیا ‪۹۱۷‬‬       ‫س‬    ‫(طبق‬       ‫بهلوی ‪nãvx‬‏‬   ‫حه‬       ‫‪۵‬‬

     ‫اشتفافی که حهرن‌در موضع فوق برای کلمه آ ورده‪,‬‬           ‫وجه‬    ‫(سینی» بثقاب) «اسشق ‪A4‬‏‬            ‫بلوچی ‪02۷‬‬

                         ‫هوشمان مردود مداند « هوبشمان ‪. ۸‬معرب آن خوان (ضم اول) «نفس»‬
 ‫کرده ‪:‬‬              ‫کک‬                    ‫کاکک‬              ‫ا‬      ‫ا‬    ‫ی‬           ‫ا‬    ‫کا‬      ‫‪ ۹‬ا‬

                ‫و خار خوانا ‪۰‬‬       ‫مك‬    ‫خار‬       ‫مانندة‬         ‫سنداخت‬    ‫خوار‬   ‫از بمح نکند او ورا‬


     ‫«لفت فرس ‪.»۹۸۳‬‬
  ‫الف خوانا دربن بيت » الف اطلاق است وخوان جمم خو (علف حرزه) (ه‪.‬م‪ ).‬است که‬
 ‫‪.‬‬     ‫خواندن‬   ‫‪:‬‬   ‫رك‬   ‫‪-‬‬   ‫‪۷‬‬           ‫اسدی خود درص ‪ ۷۱۶‬متذ کر شده ) از افادات استاد دد«شدا) ‪.‬‬


                                                                                               ‫بقبه از صفحه ‪۸۷ ۲‬‬

  ‫‪ #‬خواستی ‪ -‬بروزن‌ک ستن » هندی باستان ‪( 1208۷۹ , * 02۷5‬چشدن‪.‬مزیدن‪.‬‬
 ‫‪.‬ردی ‪ . 0115۵۷5‬عنا‪« 502‬اسشق )‪۷٩4‬‏ «اسفا‪۱:۲‬ص ‪۰ ۸۳۱‬‬  ‫پسند کردن)» پهلوی ‪ 0252۷2‬ک‬
 ‫‪« ۹۷۳ ۳۳۰‬مسینا ‪»۲ :۹۳۱‬؛ خواهش کردن ‪ -‬اراده کردن ت طلبیدن» درخواست کردن؛‬   ‫‪۰‬‬
                ‫آرزو داشتن ؛ مشتاق مودن ‪ -‬حکم کردن ؛ فرمودن = طلب عروسی وازدواج کردن‬

=== leaf 265 (printed 805) ===
                                                                                     ‫‪=A‬‬‫و‪‎‬‬




‫خیناگر = باکاف فارسی‌بروزن تیرآور‪.‬‬                ‫کردن وباد دربوق انداختن باشد‪ .‬که آنهم کنابه‬
                  ‫و‬    ‫ساز نده ومغنی را گومند ‪۳‬‬
                                                    ‫از برخاستن و برپایشدن آلت تناسل است ‪-‬‬
‫= بفتح واو بروزن بی‌خبر »‬        ‫حینو ر‬            ‫کونابه از فرودآمدن ومقیم شدن ولزول کردن‪.‬‬
                           ‫پل صراط رگاویند ‪.‬‬                           ‫ولشکر کشیدن و نوت نا‬
‫حو ‪ = ۴‬بسراول وسکون‌ثانی وواو‪,‬‬                      ‫خیم نزگادی ‪ -‬کنابه از آسمان‬
‫آب‌دهن راگوبند؛ وبفتح اول وضم ثانی‌هم‌درست‬
                                                                                         ‫است ‪.‬‬
                                        ‫اكت ‪::‬‬      ‫خیمه کبوه = بعنی خيمة زنکاری‬
                                                                           ‫است که آسمان باشد ‪.‬‬
‫حیوق * ‪ -‬بکراولبروزن زببق ‪.‬نام‬
          ‫ولاسی جک ازاولعای )‪ (۱‬خوارزم ‪¥.‬‬         ‫ن ینا سرودونغه هرا کومند ‪١.‬‏‬
                                                                               ‫خینا ‪ 5‬روز‬




                                                                  ‫)‪ ۱‬چك چش‪:‬الکای ‪.‬‬

   ‫(ھ‪ .‬م‪(0‬‬   ‫«چینود»‬    ‫_ مصحف‬   ‫‪۴‬‬         ‫خنبا کر‪.«(.‬م‪).‬‬   ‫سس‬          ‫رك‪ :‬خنبا ‪۵‬‬   ‫‪۱‬‬

   ‫= یوخ » یولهب ‪ ‹ 120016‬نامشیوه ‏‪٩۵۱۷‬و ‪12101‬‬                   ‫‏‪= X۷. e0 _ ۴‬ودخ‬
   ‫‪ - ۵‬کدثرب‌اسلامی‬                  ‫|تال‪ « 6708‬اسشق ‪۷۱‬ه»› رك‪ :‬خدو‪.‬‬
                                                                  ‫و‪. 25‬اوسا _ ‪ ۵۷۵2‬ن‬
                             ‫‪« xiwaq‬دائرة المعارف اسلام‪ .‬فراشه ج ‪ ۲‬ص ‪۳٩٩‬‏ ستون ‪.*۱‬‬
                                                                                   ‫خیوق ‏‬
                                                                  ‫‪ #‬خيوه ‏ رك‪ :‬خیوق ‪.‬‬
```


## [2026-09-05T20:56:10.247Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 236 237 238 239 240; do echo \"=== leaf $n (printed ~$((n+540))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -25; done",
 "description": "Print Borhan v2 leaves 236-240"
}
```


### [2026-09-05T20:56:12.141Z] TOOL RESULT

```
=== leaf 236 (printed ~776) ===
 ‫¬ ‪~A‬‬


   ‫ن‬
   ‫ز بر‬
      ‫وول‬
        ‫حنبور ‏‪ ١‬با تحتانی مجپ‬                        ‫وسکون‬     ‫انی‬   ‫نم اول وکر‬      ‫‪-‬‬   ‫حضاف‬


‫حلی کر » قامت و پل صراط رگانویبزند ‪-‬‬                  ‫باشف‬    ‫وخشن‬    ‫تستالی وکاف ‪ ۰‬لوعی آزلبای درشت‬

 ‫ومزارع‌و زراعت کنندهرا گنفیتزه‌اند؟ و؛یمعنی‬                             ‫که درویثان وفقیران بوشند ‪.‬‬
    ‫اول بتقدیم بای حطی بر نون هم آمده ات‬




                                       ‫بیان هیجد هم (‪)۱‬‬
          ‫ن و ن (‪)۳‬‬         ‫و‬          ‫یکی‬                      ‫در خای باه‬

                                            ‫و کنات‬      ‫لف‬


‫ىك مشت آ بوبك مشت کاه‌وامثال آن ‪ -‬وبمعنی کفل‬           ‫خو » بفتح اول و سکون انی ‪ ۰‬جرب‬
‫وساغری اسبان هم هست ‪ -‬وقالبی را نیز گویند‬              ‫بتابی (‪ )4‬باشد که بنابان و کتابه نوسان‬
=== leaf 237 (printed ~777) ===
 ‫خواجه‬                                                                             ‫ها‬
                                       ‫آنچه بدان روز (‪ )۱‬بگذرانند‪ .‬یمنی قوت | است‬
‫خواب نادیده س کنابه‌ازطفل دابافغ‬                                       ‫لابموت ‏‪# . ٩‬‬
                                   ‫خواب جاو ید باانی ممدوله ‪ | ۰‬باشد ‪. ۴‬‬
                           ‫بونا‬
 ‫یده ه با ثانی معدوله بر وزن‬  ‫خ‬                ‫کنابه ازهرکے است که بیدار شدن در قیامت‬
          ‫والمیده » مخفف خواباننده ® باشد ‪.‬‬                                        ‫باشد ‪, .‬‬

 ‫خو اجه" ‪ -‬بائانىممدولەبووزن راجه‪,‬‬              ‫خو اب خرگوش د کنابه از غافل‬
 ‫کدخدا ورئیی خانه گروایند‪-‬ویمعتی معظم‌باشد‬                     ‫بودن وغفلت و تفافل باشد ‪. ۴‬‬
 ‫خو) بستان ‪ - ۴‬باانی مسوله بروزن | وشیخ ویر ‪ -‬ومالدار‪ -‬و حاکم وساحب جمعیت‬
                                                     ‫امعا‬
                                                  ‫یندن‬   ‫وو‬  ‫‪ .‬تاستان ‪ ,‬کنانه از حای خو‬
                                                           ‫خاب‬
 ‫را نیز کفته‌اند ‪ -‬ویمعنی دل وروح هم هت ‪-‬‬
                       ‫و خدمتکاری که آلت‬                               ‫‪۱‬‬            ‫باشد ‪.‬‬
 ‫تناسل او را بریده‬


                                                     ‫(‪ )۱‬چك » چش ‪ :‬روز بدان ‪.‬‬

                                                            ‫رك ‪ :‬خواجه بار ‪.‬‬   ‫ِ‬
       ‫دهد شرافکنان راخواب خر کوش‪.‬‬               ‫‪ - ۴‬بچشم آهوان چآشنمهةٌ نوش‬
   ‫نظامی کنجوی ‪« .‬کنجنه >‪٤۵‬‏ ‪.‬‬
                                          ‫‪:‬واب ‪-۲‬ستان (یموند مکان ) ‪.‬‬
=== leaf 238 (printed ~778) ===
   ‫کوپ‬                                                                             ‫خواجة اختران‬
‫خلیفة خواجه مودود وخواجه محمد ریکه‌روان‬            ‫اخة آن » کناب از تاره‬           ‫اوجه‬
                                                                                      ‫ح‬
‫خلیفة خواجه خان‌سعید درآن موضم باهم‌صحیت‬                      ‫عتری ماش ۔ وآفتاب را نیز گونند ‪۱‬‬
                                   ‫داشته اند ‪.‬‬
                                                   ‫خواجه بار ۔ با باابیمد بروزن‬
‫خواحة فلك ‪ -‬کنابه ازآتاب ‪-‬‬
                                                    ‫آشدنکرها بعربی‬
                                                                 ‫لاله زار؛ طعام بقدر حاجت با‬
                         ‫وستارة مشتری باشف ‪.‬‬

‫خواخة ماح ‪ -‬اشارءبحضرترساك‬
‫صلوات‌افعلیه است ‪ .‬مجسهاح بمعنی کثیر الخیر‬              ‫خواجه اش ؟ ‪ -‬باناوئین‌فرشت‬
                                                    ‫‪-‬‬     ‫ند؟‬
                                                            ‫یرا‬
                                                              ‫وقا‬
                                                                ‫کكآ‬
                                                                  ‫ران ب‬
                                                                      ‫علامان بصكاحب وكنو‬
                                    ‫باشد ‪. ۴‬‬
                                                         ‫وسصی خداو ند وصاحب خانه هم امه اس‬
‫خو ار = با انی ممدوله بورزن چار ‪,‬‬
‫در آخر کلمات گفته‬        ‫ب‬
                         ‫کنیتر‬
                             ‫بابنمعنی بدو‬          ‫خواچه چرخ اردق‪ -‬کناب از‬
=== leaf 239 (printed ~779) ===
 ‫خوازه‬                                                                                                                     ‫‪۷‬‬           ‫‪-‬‬


‫بمعنی خوردنی ورزق وروزی باشد ‪ -‬و جضم اول‬                    ‫‪ -‬ونام ولاسی‌است درحوالی ری‪٩‬‏ ‪ -‬وعم‬                                        ‫هت‬
‫بروژن شماره » بمعتی دستورباشد که رسم وقاعده‬                 ‫اول و ثانی بالف کشیده بر وزن شمار " بمعنی‬
‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬


 ‫بدن شود ق‪-‬اولبی بائد کهبنایان طاق کونبد‬                    ‫خو ار بار » بائانی معدوله وبای ابجد‬
‫بربالای آن سازند‪٩‬‏ ‪ -‬و بمعنی چوب بندی هم‬                    ‫است که قوت‬                 ‫کارزار» یمعی خوراك ادك‬                        ‫روزن‬
                                       ‫‪9‬‬       ‫فەا‬           ‫باشد ‪ - ۲‬و مره ولذت را نز گوند ‪-‬‬                                       ‫لانموت‬
‫خواری خوار » بائانی معدوله بر‬                               ‫ازديك‬           ‫وخطه‌ای‬           ‫و تومئی است از توه‌نات ضارا‬

     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
 ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬

                 ‫دادن ‪ -‬وزبان‌کاری کردن باشد ‪.‬‬                                                            ‫ازتر کتان ‪۶. ۴‬‬

 ‫بفتح اول بر وزن بماز »‬          ‫خوار ‪-‬‬
 ‫چوبدستی که خر کواو وسایر ستوران را بدان‬                          ‫کارزار ‪ ۰‬ستمکار وخواری کننده راکوبند ® ‪.‬‬
                                               ‫رانند ‪5‬‬
                                                             ‫جو ار کاره = با انی معدوله بر وزن‬
 ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬


=== leaf 240 (printed ~780) ===
 ‫‪“VAY‬‬                                                                                                      ‫خوای‬
‫هر گاه‬    ‫چنانکه‬   ‫ارادی باشد‬     ‫راستی » بمعنی‬         ‫سازند ‪ ۱‬؛ وبایتمعنی بقتح اول بروزن ملازه هم‬
‫کوبند «حر کت خواسی » ازآن حر کت ارادی‬                                                                ‫آمده است ‪.‬‬
                                        ‫خواهدد ‪.‬‬
                                                         ‫خو اس س بانانی معدوله بروزن طای‪.‬‬
‫حو اسه = بفتح اول بر وزن نواسه ‪۰‬‬                        ‫بمعنی خواستگار و طلبکار باشد ‪ -‬و بفتح اول‬
 ‫نند‬ ‫صورتی باشد که در فالیزها و زراعتهپا نکصب‬             ‫بروزن‌پلای» بمعنی تریس و بیم وهرای باشد ‪.‬‬
‫تا وحوش وطبور ازآن رمیده خان بکشت زار‬
                                        ‫فسرانند ‪.‬‬
                                                        ‫وجزیر؛ مبان دربا باشد؟ ہے‬            ‫فته شده ‪- ۴‬‬        ‫راه‬

 ‫اه بائانی معدوله وسکون کاف‬   ‫خو‬                         ‫و طلب چیزی از کی کردن را نیز گوبند ‪- ۴‬‬
‫فارسی * مرغ خانگی رگوابند ‪ -‬وتخم هرغ را‬                  ‫وبمعنی زر ومال وسامان هم‌هست_ و گاهی یمعتی‬
 ‫نکیفزته اند کوخیوناه (‪ )۱‬تخم مرغ بروغن‬                  ‫اراده گفته مشود چنالکه گویند « خواست خدا‬
                                ‫«ربان کرده باشد ‪.‬‬                         ‫‪.‬‬       ‫‪۵‬‬   ‫اراد خدا‬   ‫شی‬    ‫نود ‪٩‬‏‬   ‫رین‬

 ‫خو ال ‪ -‬با انی معدوله بروزن مال »‬                       ‫‏‪ me‬بائانی‌معدو له باس‌داز ‪۰‬‬       ‫خواستار"‬
 ‫دوده‌ای که بحهت ساختن سداهی ومر کب از دود‬
                                                         ‫لر وکواکار ور خواهتده و طلت هه را‬
‫چراغ کیرند؛ و صم اول بروزن جوال همأ مده‬                                              ‫کوند ‪#*.‬‬
           ‫است ‪ -‬وخوردئی را نگیوزبند *‪.۹‬‬
                                                         ‫خو استه ‪ = ۷‬بائانیمعدو له بروزن راسته»‬

                                                          ‫لءاه‬
                                                             ‫زر ومال واسباب وجمعدت ومامان وملك وا‬
```


## [2026-09-05T20:56:23.822Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==240' BQT_v2_pages.txt | tail -40",
 "description": "Print full Borhan leaf 239 footnotes"
}
```


### [2026-09-05T20:56:45.282Z] TOOL RESULT

```
 ‫بمفعنریی|ن ‪ -‬وخواهش باشد‪-۱٩‬‏ ومطلق چوب‬                      ‫خوار کادی ‪ -‬بانانی مسوله بروزن‬
 ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬

 ‫بابنایی ونقاشی کردن عمارت یابجهت تاك انگور‬                                                       ‫‪۱‬‬   ‫را نز گوند ‪۸‬‬                    ‫دهنده‬
 ‫وامثال آن بندند کوشکی وقبه‌ای را گنفزتهاند‬
 ‫که بجهت عروسی وآبین بندی ازکل ورباحین‬                       ‫خوا ده = بانانی ممدوله بروزن چاره»‬

   ‫‪ .‬معرب آن‬      ‫‪۳۸‬‬    ‫و حدود المالم ص‬         ‫‪۵۵۳‬‬   ‫کیپان ص‬      ‫‪.‬‬     ‫رك ‪ :‬حفرافیای سیاسی‬                   ‫‪-‬‬           ‫‪۱‬‬

    ‫البارها پر کرد ‪...‬‬    ‫چون بوسف‬     ‫«‬   ‫_‬    ‫‪۳‬‬          ‫«خوار» سم اول وفتح دوم ‪ :‬رلك‪ :‬معدم البلدان ‪۰‬‬


 ‫بوسف و زلیتا ‪ .‬خڅ‬
                 ‫خابنربار های مصر بجهان بیفتاد ‪ .‬خلق روی بمصر نهادند بطلب خواربار ‪.«٩‬‏‬
   ‫"‪ 7‬همان خوار (ھ‪.‬م‪ (.‬است ‪.‬‬       ‫‪۴‬‬                       ‫ص‪ ۹۳‬‏‪ - ٩‬آمروز یزاین کاحه معنتی ارراق بکار رود‪.‬‬

               ‫مقلده‪.‬‬   ‫رکف‪:‬ص؛ ست‌ و دو‬         ‫حدودالمالم رمعم السلدان و‬                 ‫‪ 5 ۳۴‬رکف ‪ :‬فہرست‬


         ‫زشت است خوارکاری»خوبت بردباری ‪.‬‬                          ‫‪ . 6‬توخوارکارتر کی «من بردبار عاشق‬
    ‫«منوچپری د؛مفالی ‪.*۸۸‬‬
    ‫‪ - ۷‬از‪ :‬خوارکار ی ( مصدری ) رك‪ :‬خوارکار ‪.‬‬                                           ‫‪ :‬خوارکار ‪.‬‬     ‫رک‬         ‫۔‬       ‫‪1‬‬


    ‫_؛ مصحف «خوازه» (هم‪).‬‬  ‫‏‪ ٩‬ظ‬                           ‫‪ - ۸‬باين معنی *خوارکار »>صحیح است‬
    ‫‏‪27287۷۲ .1١‬‬     ‫»ور که ‪ :‬کواز ‪۰‬‬                ‫‪۶‬ت ظ ‪ ,‬مصحف «حوازه (ھ‪.‬م‪(.‬‬                                          ‫‪.‬‬       ‫‪ :‬خو‬     ‫ورك‬



    ‫خواستن آرزو کردن)‪ .‬کردی ‪( 01122۷1‬من‌میخواهم) ‪ ۰‬مازندرانی ‪( 22۷722011‬کین‌خواء)‬                                                        ‫‏(‬
                                                                             ‫‪۰‬‬       ‫«واژه امەس ‪۹۳۲‬‬           ‫«اسفا‪۲ :۱‬ص ‪۱۹‬‬
           ‫‪۰‬‬   ‫ودومقدمه‬   ‫بست‬    ‫" ر کت ‪ :‬ص‬         ‫زبان خوارزم‬        ‫بخوارزم‬         ‫خوارز می ‪ ۳‬منسوب‬                    ‫‪۶‬‬

   ‫‪ #‬خوار ی ‪ -‬بروزن کاری » در بهلوی ‪ +012‬بمعنی آسالی است (رکه‪ :‬خوار ) آما‬

                                 ‫در فارسی بمعنی پستی وزبولی وتوهین گرفته‌اند «بشت هااس ‪۳۲۳٩‬‏ ‪.‬‬
```


## [2026-09-05T20:56:53.800Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 489 490 491 492; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -30; done",
 "description": "Print Borhan v2 leaves near 1032"
}
```


### [2026-09-05T20:56:55.417Z] TOOL RESULT

```
=== leaf 489 ===
                                    ‫بیان سیزدهم‬
             ‫درزای نقطه دار بالام مشتمل برباتزده لفت و کنایت‬


                    ‫تنکه و تلريك را گویند ‪.‬‬       ‫رلال ‪ -‬صم اول بروزن جوال » کرمی‬
‫رلقیی ‪ - ۱‬نم اول ‪ .‬بر وزن و معنی‬                 ‫را کوبند که درميان برف هم میرسد » و او‬
                                                  ‫پرنده‌ابت پر از آب صاف و آن آب را آب‬
              ‫نند ‪۰‬‬
                  ‫اکسب‬      ‫رخچوابنه‬
                                   ‫دار‬
                                     ‫وچ‬          ‫زلال خوانند و آن کرمرا اندك حیائی وح رکت‬
 ‫زلو ‪ - ۴‬تح اول ثوائی بکوشایوده‪.‬‬                  ‫مذیوحی‌هت ‪ -‬وزلال بمعنی صاف عربیاست ‪.‬‬
‫کرمی باشد سیاه رنگه ‪ .‬چون بر اصنای آدمی‬           ‫بلسفتی د کنابه از نمودن مطلوب‬
                                                                              ‫ز‬
               ‫مجیانند خون ازآ جا بمکد ‪.‬‬          ‫(‪ )۱‬است خودرا حاشق و دل او را بکمند خود‬
‫ز لو ك ‪ -‬تح اول و انی بو اوکشیده‬                                                        ‫آوردن ‪.‬‬

   ‫زات رھ رل باه که کے ا‬                          ‫زلف خطا ‪ -‬بک الت ‪ .‬بمعنی‌خطا‬
                              ‫معروف است ‪.‬‬                                  ‫و گناء و تتصیر باشد ‪.‬‬

‫رله ‪ = ۴‬بفتح اول‌وثانی‌مشدده جائوری‬              ‫زلف رهی = بکس ثالت ‪ ۰‬کنابه از‬
‫باشد شبیه بملخ که پیوسته در میان غله زارها‬       ‫شب است که جربی لیل خوالند ‪ -‬و کنابه از‬
                                                  ‫خاکی هم حت که جوهر آدمی از آست‪ -‬و‬
 ‫وهوای کرم فرباد طولانی کندوآنرا جزد بروزن‬
                                                                        ‫بلةٌ ارضی را نز گویند ‪.‬‬
 ‫بزد هم خوانند؛ وباین معنی بکسراول آیمزده‬
‫ست؛ وبعضی کویند جانوریست سیامرنکک وپر او‬          ‫وال‪ -‬ممروف است ‪ -‬کونابه‬
                                                                        ‫رلف خ‬
 ‫در زیرکاسة يشت او می‌باشد ‪ ,‬وآن لوعی‌ازجمل‬       ‫است اطزلا لواجورد که بر‬       ‫یشنوتی‬
                                                                                     ‫زرای‬
=== leaf 490 ===
 ‫‪٩‬‏ ‪۱ ۵‬سه‬   ‫سز‬                                                                               ‫زلبا‬



‫ز لیف ‪ - ۴‬بفتح اول بروزن حربف ‪۰‬‬                     ‫و شبها فرباد نند و تیز وطولالی میکند و او را‬
                   ‫بمعنی ترس وبیم باشد‪.‬‬              ‫چرخ رمه نیز میگویند ‪ -‬و در عربی طمامي‬
‫ر لیفی * = بفتح اول بروزن طبیدن »‬      ‫‪۱‬‬             ‫باشد که مردم فرومایه از جایی بردارند وبرند ‪.‬‬
 ‫بمعنی ترسیدن و بیم بردن ‪ -‬و تهدید کردن‬              ‫لیا ‪ = ۱‬بباای ابچد بروزن‌کسیاه‬
  ‫قهاوم‬
      ‫تین‬
        ‫ن ک‬
          ‫اعنی‬
             ‫تورسالیدن باشد ‪ - ۷‬و بم‬                 ‫و عربان زلابه‬         ‫نام حلوابی است مشهور‬
‫هم آمده است‪ -‬وچرخی را نیزگویند که بدان‬
                                                                                         ‫گونند ؟ ‪.‬‬
‫نه دانه را از پنبه جدا کنند ؛ و بکسر اول‬
                                     ‫همکفته‌اند ‪.‬‬   ‫وای شطه دار‬
                                                              ‫زلیخا ‪ -‬بانول خ‬
  ‫ای‬
   ‫دو‬‫صاز‬
       ‫رلیل ‪ -‬بر وزن خلیل " آو‬                      ‫بالف کذیده بروزن سویدا » نامزن عزیز مس‬
                                    ‫ند‪.‬‬
                                      ‫ویرا‬
                                         ‫ککلو‬                                     ‫باشد ‪. ۴‬‬


                                          ‫بیان جهار دهم‬

                 ‫در زای نقطه دار بامیم مشتمل بر سی و وو لقت و کنات‬

=== leaf 491 ===
  ‫رمج‬                                                                                         ‫‪-۱۰۷4-‬‬
 ‫رمام = بکر اول بورزن لظام 'مپار‬                      ‫هم هت » وبضی چشمهٌ زمزم را کوبند ‪٩‬‏ ‪-‬‬
                 ‫شتو باشد ‪ .‬گوبند عربی است ‪٩‬‏ ‪.‬‬      ‫و بممتی آهسته هم هست و زمزم بمنی آحسته‬

 ‫رمان = بفتح اول‌بروزن رمان» بمعنی‬                    ‫آهته ‪ - ۴‬و طفلی که در هنگام حرف زدن‬
‫ورمکه باشد‪ -‬و در عربی مقدار‬             ‫متووت‬
                                            ‫فو‬       ‫آب از دهنش بیرون آید ‪ -‬و شخصی که بوقت‬
                           ‫ح ركت فلك اعظم ‪. ۷‬‬        ‫لب او‬        ‫گوشت‬      ‫زدن‬      ‫و حرف‬        ‫خندیدن‬

  ‫رمقر ] ‪ -‬با تا و رای فرشت بورزن‬                   ‫بیرون ابد و گوشت دهان او تمام یبدا و ‪.‬‬
 ‫فلکاء بلفت زند و پازند ( ‪ ) ۲‬بمعنی تمسخر‬             ‫تمابان شود‪ - ۴‬و فتیله را بیز کوبند مطلقا‬
                                ‫ویشخند باشد ‪.‬‬
                                            ‫ر‬
                                                      ‫خواه فتیلة داغ و خواءه چراغ باشد و خواه‬
‫رهج ‪ -‬بفتح اول و سکون الی و جیم‬                          ‫د‬ ‫دنی‬
                                                             ‫شاثا‬
                                                                ‫می ب‬
                                                                   ‫فتبله نفنگگ و زخم ‪ -‬و در عرب‬
‫ابجد » مطلق صمغ را کوبند خواء صمخ عربی‬                ‫بمعنی مهار کردن شتر باشد‪ -‬و بمعنی تکبر و‬
 ‫باشد و خواه غیر عربی ‪ -‬مطلق زاج را لیز‬              ‫نخوت هم هت ‪ -‬و بلند بدراشتن سر را یز‬
                                                       ‫‌ماست ‪.‬‬ ‫هه‬‫دتن‬‫وی پآیشمرف‬  ‫‪-‬ن‬ ‫مدع‬
                                                                                     ‫بین‬
                                                                                       ‫گو‬
 ‫کویند ‪ - ۷‬اعم اززاج سفید وسرخ وسیاء وزرد‬
‫و سبز؛ وبعضی کویند ابن لغتبفتح اول و ثالی‬             ‫زماروغ ‪ - ۴‬بفتح اول و انی بالف‬
 ‫است ومعرب زمه است و زمه زاج سفید باشد له‬             ‫کشیده ورای‌بی نقطه بواو رسیده و بغین شطه‌دار‬
‫مطلق زاج ‪ -‬و بضم اول وفتح الیمشدد بعربی‬               ‫زده" رستنیی باشد که اززمینهای نمناك ومتعفن‌و‬
‫مرغی اتسرتاذکوهبآرادران‌میگونند ‪ ۸‬؛وبنی‬               ‫دبوار های حمام وزبرهای خم آب (‪ )۱‬و امثال‬
‫کویند مرغی است شکاری و خوش منظر از‬                    ‫آن روبد باندام چتر و عوام آنرا کلاء قاضی‬
  ‫جنس سیاء چم یمئی از جنس چرخ‌وشاهین ‪.‬‬                      ‫و چترمار کوبند؛ وضم اول‌هم آمدماست ‪.‬‬
=== leaf 492 ===
 ‫‏—‪ opo‬اسه‬




‫طعم‬       ‫مانئد‬   ‫قطه‌دار و فوقانی » طعمی راگوشد‬
                                                     ‫هچ ‪ -‬بفتح اول و سکون ثالیو جیم‬
‫عفص خوانندب‬          ‫حنرویی‬
                          ‫حلیله و مازو و امثال آ‬
‫و بنعنی نیشکر هم آمده است ‪ -‬و گرهی رایز‬                ‫را" زمج بلور میگوبند ‪ -‬و نام موضمی هم‌هست‬
‫گفته‌اند که بغامت مخت بته باشند ‪ -‬و کنابه‬              ‫در خراسان و احمد زمچی بآن موضع موسوم‬
‫ازمردم گرفته ومقبوض ‪ -‬و بخیل ‪ -‬و درشت و‬                ‫است ‪ . ۴‬وبکسر اول مرغی باشد سرخ ردکه‬
           ‫‪ :‬ورشتح اول‌هم آمده‌است ‪۰‬‬   ‫تانق باشد‪6‬‬
                                                      ‫و بزرکه شبیه بعقاب ویسیکوبند شکره امت‬
‫‪ « ۱‬باکاف ‪ ۰‬بروزن و ععنی‬               ‫هك‬              ‫و آن پردده‌ای باشد شکاری کوچکتوازباشه ‪. ۴‬‬
‫ومرد‬       ‫ه سخت‪.‬‬      ‫زمخت است که طعم عفص‪ -‬و‬
                                                         ‫زسیا»ج‬
                                                              ‫زهج بلور ‪ -‬بکر جیم فار‬
                              ‫بخیل وناکس باشد ‪.‬‬        ‫سفید را گوبند ‪ -‬و بعریی شب بمانی خوانند‬
 ‫وای قرشت‬
        ‫زمر و نتن ‪ ۰ ۲‬بانون ت‬                                                        ‫بتشدید بای ابد ‪.‬‬
‫(‪ )۱‬بروزن پهلو شکن » بلغت زند و یلزند(»)‬               ‫زهمچاك؟ » بفتح اول و جیمفارسی و‬
 ‫بمعتی‌سراییدن وخوانند گی کردن باشد ‪,‬وزمروب‬            ‫واف ‪" ۰‬تامپرنده ایست غير‬
                                                                              ‫سکون انی ک‬
‫نمی بعنی برایم و خوانند کیکتم “ و زمرویه‬                                                        ‫فظوم‬
                    ‫یعنی برایید وخوانن دک یکنید ‪.‬‬       ‫زمچیکور۔ بفاجایرمسی کواف‪.‬این‬
 ‫آهسته‬      ‫بمعتی‬   ‫بروزن همدم ‪۰‬‬   ‫ی‬   ‫رمز م‬
                                                       ‫خود از موّید النسّلا‬   ‫لفت را سروری در فرهنك‬

‫آهته‌است چهزمآهسته را گویند ‪ ۸‬وخوالند گی‬               ‫سمعنی زمج بلور‬     ‫بروزن کردی دور آورده ات‬
```


## [2026-09-05T20:57:06.485Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 492 493 494; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | tail -32; done",
 "description": "Search Borhan leaves for zamin"
}
```


### [2026-09-05T20:57:08.299Z] TOOL RESULT

```
=== leaf 492 ===
          ‫پیتما‬
              ‫پرستان درمحل ستایش بار‬                                          ‫خوانی کردماند » افداعلم ‪:‬‬
 ‫ونگام بدن شتن و چیزی خوردن بر زبان‬
                                  ‫ه‬                     ‫رمحت = بضماول و ثالی و سکون‌خای‬

                                        ‫)‪ (۱‬چك ‪ :‬رند وباژند ‪.‬‬         ‫‪.‬‬       ‫ت‬‫ش‪-‬‬
                                                                                ‫رك ‪:‬‬
                                                                                   ‫ق) چ‬
                                                                                      ‫(‪۱‬‬

      ‫‪ - ۴‬زمج وزمج در حدودالعالم ومسجم‌البلدان‌نيامده ولی‬                 ‫“رهج (ھ‪.‬م‪۹ (.‬‬    ‫‪۱‬‬


      ‫« زمیج؟درتاریخ بیهق نام یکی از بخش‌های جنومی سبزواراست تاریخ بیپقمصححبهمنیارس ‪۹۳۳٩‬‏‬
      ‫(بضم اول وتشد‪:‬د دوم مقتوح وخاء» خره‌ایست ازبیهق از اعمال لشابور‬           ‫و درمعجم‌البلدان*زمیخ»‬

                                   ‫برای اطلاع بیشتر از « احمد زمجی » رك ‪ :‬لفت نامه ‪ :‬احمد زمجی ‪.‬‬

                                                          ‫‪۴‬‬           ‫‪ ۴‬رك‪ :‬زمج * زمنج ‪.‬‬
                      ‫‪ ٩‬امروزه نز ‪ 18100102‬بهر چیز طبر ودرشت اطلاق شود‪. ‎‬‬
      ‫‏‪ Zmlalênitan . zamr(a)rênitan «ja _ Y‬یولپی‪,‬‬            ‫‪ ۱‬رك‪ :‬زمخت‪.‬‬
      ‫‪ ۸‬زم باين معنی در ماخذ معتبر بافته نشد ‪ .‬رك ‪:‬‬               ‫‪.‬‬   ‫«بونکر ‪4°‬‬      ‫‏‪ ۰ srûtan‬سر ودن‬


                                                                                ‫‪ ۸۵۷‬جح ‪-‬‬       ‫ص‬‫ادب‬
                                                                                                  ‫مز‬

              ‫محفل بوز مجمرء عود‪.‬‬       ‫خادم‬                ‫‏‪ - ٩‬مطرب مجلس باز زمزمة عود‬
      ‫‪۰‬‬    ‫سعدی شیرازی‬

   ‫( برهای اطع ‪) ۴۳۱‬‬

=== leaf 493 ===
                                                                                ‫هم آ مده‌است ج‬

‫رمودن ‪ .‬بفتح اول بر وزن بودن »‬
             ‫بمعنی نقش ونگار کردن باشد ‪.‬‬        ‫رمنج! یکی اول وانی مضموم‌بنون‬
                                               ‫‪ 5‬جيم زده » مرغی باشد از جنس عقاب ورنگش‬
 ‫رموده = بفتح اولیروزن لبوده »هش‬
                                               ‫بسرخی مابل بود؛ بوعضی کوبند مرغی است‬
                      ‫ونگار کرده را کویند ‪.‬‬
                                               ‫سیاه و از غلیواج بزرکتر و آنرا دو برادران‬
                                               ‫خوانند ؛ و بعضی گویند جالوریست‪ .‬شکاری بغایت‬
  ‫‪ - ۱‬وآن مترادف «باژ» است ‪ .‬درکتاب الناج منوب بجاحظ آمده ‪« :‬پادشاهان‌ساسافی‪-‬‬
  ‫هنگامیکه طعام ابشان حاضر ميشد ‪ -‬برآن زمزمه میکردند‪ .‬وکسی بحرفیمخن‌نمیگفت تابلند‬
  ‫شود واگر بخن گفتن ناچار میشد » بجای آن‌باشاره » غرض ومتصود خودرا میفپماند ‪» .‬فردوسی‬
                                          ‫در داستان پذبرابی خرو پرویز ازسفیر روم گوید ‪:‬‬
      ‫بزمزم همی رای زد‪.‬درنهان ‪.‬‬                     ‫چپاندار بگرفت باژ مهان‬
  ‫‪ ۴‬ممودی در‬              ‫رك ‪ :‬مزدینا ص ‪ ۳۵۲‬۔ ‪ ۷۵۷‬؛ خرده اوستا ‪. ۶۸ - ۲۸‬‬
   ‫مروح الذهب (چاپ قاهره ص ‪ )۸۱‬گوبد ‪ :‬وهو ( زردشت ) بی الم‌جوس الذی اناهم بالکتاب‬
  ‫المعروف بالزمزمه عتد حوام الناس واسمه عندالمجوی بتاه ا(و=ستا)‪ ».‬ظاهراً لظر باینکه اوستا‬
   ‫‪ ۴‬برك‪:‬زمزم‪.‬‬     ‫‪_ ۳‬رك‪:‬موجم الملدان ‪.‬‬         ‫را مپزهم‌زمیخواندند این نام بدان‌اطلاق‌شده ‪.‬‬
                       ‫‪,‬مچ ‪.‬‬
                           ‫‪-‬ك‪ :‬زمج ز‬
                                   ‫‪ 1‬ر‬                ‫مسحف «رمکان» (ه‪.‬م‪. ).‬‬        ‫‪۵9‬‬
                                                             ‫رك ‪ :‬رمج » زمه ‪.‬‬      ‫‪۷‬‬

  ‫‪ #‬زمتان ‪ -‬بکر اول ودوم ‪ :‬از ‪ :‬زم (سرما) ‪ +‬ستان ( یوند زمان ) ‪ .‬بهلوی‬
    ‫‪05700۳‬‬
         ‫کے ‪ . ۳۵۲۲‬دراوراق مانوی ‪( 680012‬سرما‪ .‬زمستان)‪ ,‬پارسی ماله ‪2‬‬            ‫‪0«1‬نیبر‬
           ‫‪Henning, A list of Middle‬‬                ‫‪Persian..., BSOS, 126, 1, p.‬‬            ‫‏‪۰‬‬
  ‫کیلکی ‪.08056201622‬فر بز دی ‪, 0115580۳1622‬برنی ‪«ılij 1115580۳162‬‏ ‪82 0821560۳16 J‬‬
   ‫ەك ‪ .‬س ‪ ۵۸۲‬سمنایی ‪ . 1153052‬سنگری ‪ » 005807162‬سرخه‌یی و لاسکردی‬
   ‫‪ ۰. 0‬شپمیرزادی ‪« 01560022‬ل ‪ ۷ .‬ص ‪ , ۹۷۱۱‬استی ‪‹ 8620112‬ك‪ .‬است‪۸۱6 ۲‬‬

=== leaf 494 ===

      ‫زمهر بر‬        ‫شیر خواره‌سرهای‬        ‫در دست‬               ‫ناخن شده کمود‬            ‫جون‌ین‬   ‫برکه شفثه»‬   ‫‪۳‬‬    ‫‪۱‬‬



    ‫‪ +‬منوچهری دامفانی ‪۳۳۰‬‬
  ‫از ‪ :‬زمن ‪٣‬‏ بیمای(ییماینده)‪.‬‬              ‫‪۴‬‬                  ‫رك‪ :‬زامیاد‬       ‫‪۴‬‬                   ‫ن‬
                                                                                                    ‫م‪:‬‬‫زرك‬‫‪۴‬‬
                                                                   ‫® ‪ -‬از ‪ :‬زمين ‪ +‬کوب ( کوبنده) ‪.‬‬
  ‫‪۶‬بارتولمه‪۹۹۱ ۲‬‬           ‫اوستا‪0۳]22‬‬   ‫‪10۳22‬‬           ‫بپلو‬     ‫آن‪:‬زمی)؛‬     ‫بفتح اول» (‪.‬خفف‬           ‫‪2‬‬   ‫د مین‬

 ‫ایو لد «بك»‪ .‬ره ‪:‬‬            ‫بایسو ندو«وین» وزميك بهلوی قنز ازه«مان ریثهاست‬
                                                                                                   ‫ورمبن از همین زم است‬
 ‫(وی زمی ) » افغانی ‪( [2120۳‬زمین) ‪ ۰‬استی‬
                                       ‫تبرگه ‪ ۳۵ - ۲۵۲‬؛ هندی باستان ‪ [80-۳‬ر‬
 ‫‪ . 72 ,‬سریکلی ‪ . 57762‬شفنی ‪ . 627162‬بلوچیع ‪( ۴10122‬مزارع‪.‬بذرها) «اسشق‬  ‫‪8‬‬
 ‫)‪°' ۸۷۲۶‬‬    ‫‪»a‬‏ ‪ ۰.‬ص‬            ‫> مرنی واطنزی ‪0‬‬                   ‫دی‬
                                                                    ‫لهز‬
                                                                      ‫ایس ؛ کیلکی ‪ .‬فر‬              ‫ورك ‪ :‬هوشمان‬          ‫‪۷‬‬

  ‫سمنانی‪.‬سنگری ‪ » 010۳182‬س‪2‬ر‪8‬خ‪.‬هلیایس‪1‬گ‪7‬ردیوشهمیرزادی‪ 94.۲ 01/0۳832‬ص‪٩۸۱٩‬‏ ؛کر‬
  ‫خاك ‪ .‬ارض » تراب‪ .‬خاك ‪« :‬استاد از زمینش (شاکردرا) بالای سزبرد وفروکوفت»« گلتان‪۰‬ه»‪-‬‬
  ‫منظومة شمی است که درمدت ‪4۲‬‬                          ‫ایرات‬
                                                          ‫ییک‬
                                                            ‫سین‬
                                                              ‫ارززم‬
                                                                  ‫سطح کر؛ خاکی ‪ -‬ملك و کشور ‪ .‬ک‬
 ‫ساعت بکبار دورخود میچرخد (حرکت وضمی ) و درمدت ‪ ۵۹۳‬روز وشش ساعت و چند دقیقه‬
 ‫بکبار دورخورشید میگرده (حرکت اتقالی ) رة زمن دار ای ينجقار ‪ :‬آسا ‪ ۰‬ارویا » امریکاء‬

                                                                                                   ‫آفربقا‪ .‬واقیانوسیه است‬
```


## [2026-09-05T20:57:26.975Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- PHD ---\"; grep -n \"zamīg\\|zamīk\\|zamig\\|zmyk\" PHD.txt PHD_mackenzie.txt | head -10; echo \"--- HRN ---\"; grep -n \"zamīn\\|zamin\\|zemīn\" HRN.txt | head -10; echo \"--- HUB ---\"; grep -n \"zamīn\\|zamin\" HUB.txt | head -10",
 "description": "Grep Pahlavi and Persian sources for zamin"
}
```


### [2026-09-05T20:57:27.063Z] TOOL RESULT

```
--- PHD ---
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:1724:earth büm, xàk, zamig.
PHD.txt:1725:earthly zamigig.
PHD.txt:2097:geometry zamig-paymanih.
PHD.txt:3953:terrestrial zamīgīg.
PHD.txt:5064:zardčūbug zam zamīg zamān zastan zafar zadar zadan zadüg
PHD.txt:5337:хоп! daménag zamigig
PHD.txt:5338:zamig
PHD.txt:5341:zamigpaymünih AU росу gn?
PHD_mackenzie.txt:5751:zamig [z-, ?myk I M zmyg, N zami] earth.
--- HRN ---
5883:wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
--- HUB ---
```


## [2026-09-05T20:57:32.986Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zami\\b\\|zamin\\|zamīn\\|zamik\\|zamīk\\|zmyk\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n \"zami\\|zam\\b\\|Erde\" HUB.txt | head -20",
 "description": "Grep Horn and Hübschmann for zamin"
}
```


### [2026-09-05T20:57:33.052Z] TOOL RESULT

```
5883:wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
=== HUB ===
171:51. Wenn die Flexion dmextan mischen, pr. amBzam
185:5, 351 angezogene np. mezldan, pr. mBzam 'harnen*.
221:56. Np. dvextem 'hangen, hangen' (pr. avezam)^ altes ptc.
464:von afrozam : afroxtan u. s. w.) neu gebildete Infinitiv.
676:Analogiebildung nach afrdzam : afrdxtan etc. aufgefasst
2213:eine iran. Wzl. duk, dud (also np. ddzam — phi. docem)— 64 —
2406:ment = phi. "^zarrik aus "^zamik = zd. ^zarenya- (fiir
2447:666. Np. zamistdn 'Winter : »am *Kalte* = tobistan *Sommer*
2451:667. Np. zami aus phi. zamlk = bal. zamih, Ap. uzmaya-
2868:pe-zam) vereinigen, was mir bedenklicher scheint.
3397:*listanaiy = np. listan, das Praesens Haizamiy = np.
3398:*lezam, das nach dem Muster von nivistan : niv^am zu
4422:ptixtan *koehen fiir *paxtan zum pras. pazam gebildet
4779:239, phi. cim Gl. and Ind. 128; zam *Kalte*, zd. zimo (gen.
4914:np. dur *fern = ap. zd. skr. dura; bum *Erde' = ap.
6387:badan 'sein' H. 233 ; bor Tuchs (Pferd) H, 234 ; bUm *Erde
7887:mit g^, siehe oben p. 70; zam 'Kalte* (g^h) H. 666; zamt,
7888:zamln *Erde (g^) H. 667; zanax 'Kinn {g^h) H. 669; zud
7905:damiy = zd. marezami^'); burz *Hohe, hoch* (g^h), phi. 6wr^,
7963:np. zam *Kalte* (oben p. 70).
```


## [2026-09-05T20:57:35.591Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2447,2462p' HUB.txt",
 "description": "Read Hübschmann 667 on zami/zamin"
}
```


### [2026-09-05T20:57:35.636Z] TOOL RESULT

```
666. Np. zamistdn 'Winter : »am *Kalte* = tobistan *Sommer*
: tdb *Hitze'. Mit paz. damistan, das auch ich fiir falsch
halte, vergleicbt N old eke np. datna = arab. LW.
damaq *Wind und Schnee vereint*.
667. Np. zami aus phi. zamlk = bal. zamih, Ap. uzmaya-
patiy kar *kreuzigen (Bang: pfahlen') gehOrt schwerlich
hierher.
670. Zu streichen.
671. Dazu osset. ztndon Ev. Matth. XI, 23 *6efangnis\ vgl.
meine Etym. und Lautl. p. 124. Die Pehleviform mit
„plene geschriebenem i bezw. e" auch Ganjeshayagan
Gloss, p. 10. Danach ist mit Riicksicht auf Darme-
steter's richtige Etymologic^) im phi. zenddn zu
lesen. Freilich setzt arm. zndan, zendan 'Gefangnis'
(EliSe) ein mp. zenddn (nicht zendan) voraus, ist
aber vielleicht erst im 5. Jhd. ins Armeniscbe ge-
```


## [2026-09-05T20:57:44.752Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"667\\.\" HRN.txt | head -10; echo ===; sed -n '7880,7895p' HRN.txt",
 "description": "Find Horn entry 667"
}
```


### [2026-09-05T20:57:44.819Z] TOOL RESULT

```
Exit code 1
5892:667. ;s;emi: (Öähn. I, 134 Anm. 4, 178 Vers 877)'), zemm
14077:I <?<»;/;/- 667.
14078:i zennn 667.
14726:zÖÖ, «MrtS 667.
17251:zamth 667.
17692:jmi 667.
19687:zamlk 667.
20127:I zmaka 667.
21370:t. 2f<y;f 667.
21372:d. zdnxä 667.
(eval):1: == not found
```


## [2026-09-05T20:57:47.453Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5876,5905p' HRN.txt",
 "description": "Read Horn 666-667"
}
```


### [2026-09-05T20:57:47.528Z] TOOL RESULT

```
mann, ZDMG. 38, 424).
666. xeni 'Kälte', zemistan 'Winter.
aw. zyao- 'Winter', Gen. ziniö; phlv. zam 'Winter'
(vd. 2 (20)), zam(i)stan; ai. himä- 'Winter ; arm. vergl.
jiun 'Schnee', jmern 'Winter', jmerem 'überwintern
(H. No. 178).
oss. d. zumägy t. zimag 'Winter' (135); af/. zimai;
wa;^. zam, zamin (Adj.), sar. zainän, zamämn (Adj.),
si/n. zimjy zinj 'Schnee'.
) vt. 19, 42 ]int die neuo AuRfj^abe harözuiiem.
10*— 148 —
Daneben auch allgemein entlehnt, kurd. afy. zamistän,
bei. zamisiän, :^imisfän, zavistän (414), sar. zümistän,
yidg. zemistän.
Die Pazendlesung damistan ist belanglos und falsch
wie päz. damik statt zamtk (np. zemin).
667. ;s;emi: (Öähn. I, 134 Anm. 4, 178 Vers 877)'), zemm
*Erde.
ap. uzmaya[patiy ; aw. ^^äo 'Erde', Gen. zemö; phlv.
zamlk; ai. //wtt- auf der Erde'.
af/. zmaka 'Erde*; oss. d. zän/ä, t. zä/ (127); sar.
zems, siyn. zemc,
LW. bei. zamtk 'Felder, Saaten' (415); ausserdem
ist np. zemm^) allgemein entlehnt (vergl. bei. No. 298).
668. ^en *Weib'; zenber 'Sänfte''-).
g. Jen (Vullers sen, Asteräbäd); Käs. K. zen, Jen,
Jin, Z. mn,
aw. Jeni- (y. 53, 6), Jaini- (y. 10, 17) *Weib'; phlv.
zan; ai. Jäni-, Jäm- 'Weib, Gattin'; arm. kiu 'Frau'
(H. No. 144).
```


## [2026-09-05T20:58:00.686Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"algorism\\|Algorism\\|Khowarazmi\\|Khwarizmi\\|Khowarizmi\\|al-Khuwarizmi\" KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Grep Klein for algorism"
}
```


### [2026-09-05T20:58:00.742Z] TOOL RESULT

```
KLN_1971.txt:11007:by Mohammed ibn Musa al-Khowarizmi, 
KLN_1971.txt:11013:bound together, united’. Cp. algorism. 
KLN_1971.txt:11100:algorism, n., the Arabic system of numerals. — 
KLN_1971.txt:11104:ME. algorisme , fr. OF. algorisme (F. algorith - 
KLN_1971.txt:11105:me), fr. ML. algorismus , from the inexact trans- 
KLN_1971.txt:11106:literation of Arab. al-Khowarizmi, ‘the man of 
KLN_1966.txt:2173:of  equations,  which  was  the  original  scope  of algebra.  Al-jabr  is  formed  fr.  al-,  ‘the’,  and  jahr, ‘reunion’,  which  is  rel.  to  the  s/crbja'bara,  ‘he bound  together,  united’.  Cp.  algorism.
KLN_1966.txt:2189:algology,  n.,  the  study  of  algae.  —  A  hybrid  coin¬ ed  fr.  L.  alga  and  Gk.  -Xoyla,  fr.  -Xoyo;,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  alga  and  -logy. Derivatives:  algolog-ical,  adj.,  algolog-ist,  n. algor,  n.,  cold;  chill.  —  L.,  fr.  algere,  ‘to  be  cold’. See  algid  and  -or.  For  the  mode  of  formation cp.  terror,  ‘fright’,  fr.  terrere,  ‘to  frighten’,  albor, ‘white  color’,  fr.  albere,  ‘to  be  white’, algorism,  n.,  the  Arabic  system  of  numerals.  — ME.  algorisme,  fr.  OF.  algorisme  (F.  algorith- me),  fr.  ML.  algorismus ,  from  the  inexact  trans¬ literation  of  Arab.  al-Khowarizmi,  ‘the  man  of Khowarizm  (the  modern  Khiva),  surname  of Abu  Jafar  Mohammed  ibn  Musa,  great  mathe¬ matician  of  the  9th  cent.  His  famous  work  Al- jabr  w’al  muqdbalab  (‘Reunion  and  compar¬ ison’),  introduced  the  use  of  Arabic  numerals  in Europe,  which  denoted  a  turning  point  in  the history  of  mathematics.  Cp.  algebra, algous,  adj.,  pertaining  to  algae.  —  L.  algosus, fr.  alga,  ‘seaweed’.  See  Alga  and  -ous. alguazil,  n.,  peace  officer  in  Spain.  —  Sp.  alguacil, fr.  earlier  alguazil,  fr.  Arab,  al-wazfr,  fr.  al-, ‘the’,  and  waztr,  ‘vizier’.  See  vizier, algum,  n.  —  See  almug.
```


## [2026-09-05T20:58:09.751Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nn=sum(l.count('\\f') for l in lines[:2190])\nprint('leaf idx',n,'-> printed approx',(n-12)*2, (n-12)*2+1)\nEOF",
 "description": "Compute Klein page for algorism"
}
```


### [2026-09-05T20:58:11.747Z] TOOL RESULT

```
leaf idx 37 -> printed approx 50 51
```


## [2026-09-05T20:58:22.791Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 1.21 ===\"; grep -n \"1\\.21 EARTH\\|1\\.21\" SYN.txt | head -5; echo \"=== IEC ghdem ===\"; grep -n \"ghdem\\|ghðem\\|ghdom\\|gh(d)m\" IEC.txt | head -10; echo \"=== WLD ===\"; grep -n \"ghðem\\|ghdem\\|ghdom\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Buck, Mann, Walde-Pokorny"
}
```


### [2026-09-05T20:58:22.879Z] TOOL RESULT

```
=== SYN 1.21 ===
781:1.21 EARTH, LAND
800:b. The solid surface of the earth, viewed either simply as a surface (one lies on the earth or more commonly on the ground), or as the source of vegeta- tion, (good) earth, land, soil, or ground. For other words used in these senses, see 1.212.
829:1.212 EARTH = GROUND, SOIL
831:that a list would be mainly a repetition of that in 1.21. But there are also other words, some less common, others (like NE ground, soil, NHG boden) now more common in these senses.
845:1.213 DUST Grk. — xévts Goth. mulda, stubjus Lith. dulkés (pl.) NG oxéyn ON dupt, dust Lett. pisli (pl.), putelklz (pl.) Lat. pulvis Dan. stg ChSl.  prachii It. polvere Sw. stoft SCr. oprah Fr. poussitre OE dist Boh. prach Sp. polvo ME dust Pol. proch Rum. opraf, pulbere NE dust Russ. pyl Ir. luaithred Du. stof Skt.  renu-, pansu-, dhiali- Nir. luaithreadh OHG _ stuppi, stoub (melm) Av. pasnu- W. Ulwch, pylor MHG stoup Br. poulir NHG _ staub
=== IEC ghdem ===
=== WLD ===
41697:glogh- : glegli- — gkdem-, ghdom-, ghilmi 
41788:DaB ghdem- „Erde <£ als „die tragende“ benannt und mit ai. kiama-h 
41793:wachsend" (n „in £ ‘) und andern Worten eine Kurzform von ghdem („* zyhtm 
41819:cymr. dyn , corn. bret. den „Mensch ££ , urk. *don{o- aus *ghdomlo- = y&ovios, 
49834:Anknfipfung an ghdem- „Erde“ bei G. Meyer und Pedersen KZ. 36, 335
```


## [2026-09-05T20:58:25.720Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41690,41700p;41780,41835p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read Walde-Pokorny ghdem entry"
}
```


### [2026-09-05T20:58:25.777Z] TOOL RESULT

```
43 * 



662 


glogh- : glegli- — gkdem-, ghdom-, ghilmi 


glogli- : glagh- „Stachel, Spitze". 
lett. zcms „niedrig ;£ ; 

aksl. zemlja „Erde ££ (zemi nicht nach Hirt IF. 37, 225 = gr. yauat, sondern 
Lok. *zemjrd von *zernja; daraus russ. ozemu „zu Bod err", nazenib „auf die 
Erde“ gekiirzt, nicht nach Hirt einen alten Kons. Acc. *?jliem-m enthaltend) ; 
dazu auch (Liden AfslPh. 28, 38), aksl zmbja „Schlange“ („auf der Erde 
kriechend, yda/uai.6g“), znibjb „Drache ££ . 

DaB ghdem- „Erde <£ als „die tragende“ benannt und mit ai. kiama-h 
„ertragend, geduldig", ksamatc „duldet, ertragt" verwandt sei (Prelhvitz 
u. ydcov, Uhlenbeck Ai. Wb. u. ksdff), ist nicht glaublich (auch lat. tillus 
gehort nicht zu gr. Te/.aooai, lat folio, s. u. *iel- „flach“). — Nicht iiber- 
zeugend sucht Prellwitz KZ. 46, 172 in d-oyiov „Triiffel ££ als „in der Erde 
wachsend" (n „in £ ‘) und andern Worten eine Kurzform von ghdem („* zyhtm 

Dazu Worte fiir ^Mensch" als „Irdischer“ (s. z. B. Bgm. IF. 17, 166ff. ; 
anders, nicht iiberzeugend Wiedemann BB. 27, 203): lat. homo, -inis „Mensch“ 
umgelautet aus alat. hemo (auch in nemo „niemand ££ aus *ne-hemo), acc. 
hemonem; dazu humdnus „menschlich“ (Lit. zum noch klarungsbediirftigen 
ii bei Bgm. aaO., Yf. LEWb. 2 s. v.; Brugmanns Erklarung aus einem *hoi-mo- 
„hiesig, diesseitig‘ £ ist ebenso unglaublich, wie Pedersens KG. I 69, 89, 166, 
173 Konstruktion eines * ghdoim - neben angeblichem *ghdiom- und seine 
Berufung auf ir. dunti, s. auch unten; verfehlt Fay Min. 1907, 37 : ai. 
ksont u. a. „Erde, Land", und IF. 26, 34 A. 2 : ai. iima-h „amicissimus, 
comes, (pgarcoo^); osk. -umbr. *homon- (entweder mit der Ablautstufe *ghom- 
wie humus, gegeniiber lat. hemdn-, s. v. Planta I 242 f., oder einzeldialek- 
tischer Umlaut aus *hemdn-, Solmsen IA. 19,30): 

o. humans „homines“, u. ho monies „hominibus ££ . 

got. gutna, aisl. gumi, ags. guma, ahd. gomo ,.Mensch, Mann", nhd. in 
Briiuti-gam (idg. *gh e mon- oder *gh 0 mon-), lit. (alt) zmud (DaukSa m. Acc. 
zniunf) „Mensch“, heute zmogiis , zmogus (^-Formans wie in aksl. mq-zb ) 
„Menscli £ ‘, pr. smog (zum Ausgang s. Trautmann Apr. 432), weitergebildet 
pr. smunents „Mensch“. smonemnvins ds und smuni „Person ££ , lit. zmond 
„Frau <£ , zmones pi. „Menschen ££ (acc. pi. znwnis dial, aus idg. ghmonns ; Traut- 
mann BslWb. 369 f.). 

Pedersen a. o. gen. 0. (gegen KZ. 36, 105) stellt hierher auch air. duine, 
cymr. dyn , corn. bret. den „Mensch ££ , urk. *don{o- aus *ghdomlo- = y&ovios, 
ai. ksamya-h ; da dies der einzige Beleg fiir kolt. ni aus mi ware, miiBte 
allenfalls Ubertragung des n aus dem Paradigma *ddn „Ort, Stelle", s. o., 



664 


ghd — gh[di]es, ghjes 


erwogen werden. Doch ware dann der pi. air. doini , nir. daoine ,.Menschen, 
Leute" (echter Diphthong) von duine zu trennen (denn Pedersens Konstruk- 
tion eines *ghdoim- neben seinem *gkdjoni- ist unannehmbar, s. o. zu hn- 
manus). Weit wahrscheinlicher wird doini ais *dheuenio- oder *dhoiicnio- 
und duine usw. als tiefstufiges *d1mnio- mit got. diwans „sterblich“ ver-
```


## [2026-09-05T20:58:26.699Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '781,830p' SYN.txt",
 "description": "Read Buck 1.21 EARTH LAND"
}
```


### [2026-09-05T20:58:26.761Z] TOOL RESULT

```
1.21 EARTH, LAND
NG = airpa, land Lith. Zeme
ie a ON jord, land Lett.  zeme
val i tellus, humus Dan. jord, land ChSl. zemlja
Tr. eee Sw. — jord, land SCr. zemlja
Sp. tierra OE eorpe, land Boh. zemé
Rum. pamint, tard ME  erthe, land Pol, _ziemia, lad
Ir. talan ee NE earth, land Russ. zemlja
Nir. talamh, tay Du. aarde, land Skt. bhi, bhimi-, ksam-
W. capi OHG erda, lant prthivi-, mahi, ete.
Br, douar MHG erde, lant Av. zam-, biimi, OPers. NHG erde, land biimi-
‘
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
—
; Digitized by Arya Samaj Foundation Chennai and eGangotri
16 SELECTED INDO-EUROPEAN SYNONYMS
The various ideas expressed by NE earth and land are frequently covered by the same word, and where different words are employed their uses overlap. We may distinguish here:
a. The whole earth, as distinguished from sun, moon, etc. Commonly ex- pressed by the same words that are used in the following senses, and representing a relatively later conception. Special terms may be introduced to distinguish this sense, as (from the present state of knowledge) words meaning ‘globe, sphere’, or compounds like NHG erd- Kreis, erdreich. But these do not dis- place the common words and are not considered further here.
Since the earth is felt as the known world, words for ‘earth’ in this sense and ‘world’ may overlap in use (the high- est mountain in the world = on earth), and some of the words discussed under ‘world’ belong here not only in origin but also in actual use. So regularly ON midgarér, OS middilgard, and fre- quently OF middangeard, OHG miitil- gart.
b. The solid surface of the earth, viewed either simply as a surface (one lies on the earth or more commonly on the ground), or as the source of vegeta- tion, (good) earth, land, soil, or ground. For other words used in these senses, see 1.212.
ce. The solid surface of the earth in contrast with that which is covered with water, now regularly land. This sense is in some languages commonly ex- pressed more specifically as ‘dry (land)’, as Byz., NG émpa, Rum. uscat (fr. adj. uscat ‘dry’), Lith. sauszemis (sausas ‘dry’ and Zeme).
d. The earth as material in general. This may be expressed by the common words for ‘earth’ (cf. NE earthenware), but more often by special words for a
particular kind of earth, like NE clay, NHG ton, Fr. argile, etc. (9.73).
e. A definite portion of the earth’s surface, from the land of an individual to a whole country (19.11).
The association between these various senses is such that any one of them may be the starting-point of an extension to some or all of the others.
Of the two Gmc. words represented by NE earth and land, the latter started with sense e, as indicated by the ety- mology and the use in Gothic, but was at an early period extended to sense c, eventually displacing earth, etc., which were once freely used in this sense. In English, on the other hand, land in a part of its earlier uses is mostly displaced by country.
1. IE *Ghem- and *§h®em-, represent- ing the most widespread cognate group, though the precise character of the IE variant form involves a difficult rob- lem. Walde-P. 1.662 f. Ernout-M. 464. Walde-H. 1.664f. The inclusion in this group of Hitt. tekan, Toch. A tkam ‘earth’, and the resulting assumption of IE *dheghom-, *dhghom- (Kretschmer, Glotta 20.66 f.), is rejected by Ben- veniste, Mélanges Ginneken 193 ff. But some ultimate connection is probable.
Grk. x#av (mostly poet. and in sense b), beside xayuai ‘on the ground’, xPapadds, xaundds ‘on the ground, low lying’; Lat. humus (mostly in sense b) beside humt ‘on the ground’, humilis ‘low’; Ir. diz, gen., ace. don ‘place’, early ‘earth’ (Pedersen 1.89, Vendryes, RC 40.437 ff.); Lith. Zemé, Lett. zeme, OPruss. semmin (acc. sg.), ChSl. zemlja, etc., general Balto-Slavic for ‘earth’ and ‘land’; Skt. ksam- (gen. usually jmas), Vedic and in sense b, esp. ‘earth’ vs. ‘sky’; Av. zam- (gen. zemo = Skt. jmas) ‘earth’ in all senses (Barth. 1662 ff.); Alb. dhe ‘earth’.
CC-0. In, Public Domain. Gurukul Kangri Collection, Haridwar
| | | | | |
‘floor, pavement’.
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 17
While there is no clear root connec- tion for this group, its primary sense seems to have been that of ‘earth’s sur- face, ground’.
2. Grk. yf, Hom. yata, etym. un- known, perh. of pre-Greek origin. The poetical afa is also of dub. etym., but possibly ‘the mother (earth)’. Brug- mann, IF 15.93 ff. e
3. Lat. terra (Osc. teertim, tertim ‘ter- ritory’), prob. fr. “tersa- : torrére ‘dry up, parch’, Grk. répcoua ‘dry up’, Skt. irs- ‘be thirsty’, Goth. ga-Jairsan ‘dry up, wither’, NE thirst, etc., in which case its orig. meaning was ‘dry land’ vs. ‘sea’ as in the frequent terra marique. Here belong also, though of somewhat different formation, Ir. fir (‘Iand’ mainly in sense e), W. tir, and the now obs. Br. tzr. Walde-P. 1.737 ff. Ernout-M. 1034 f.
The descendants of Lat. terra remain the Usual words in all the Romance lan- guages except Rumanian, where {ara is now mostly ‘land’ = ‘country’ (also ‘country’ vs. ‘city’), otherwise displaced by the following.
Rum. pamint, fr. Lat. pavimentum Used first of the ‘ground’ (sense b), it became the com- mon word for ‘earth, land’ in most of the other senses. REW 6312.
4. Ir. talam, NIr. talamh, Lat. tellus (mostly poet.) : Skt. tala- ‘surface, bot-
tom, plain’, ChSl. télo, SCr. ilo ‘ground’, etc. Here also the starting-point was senseb. Walde-P. 1.740. Pedersen 1.132.
W. daear, Br. dowar, Corn. doar, etym.? Pedersen 1.66. Henry 104.
5. Goth. airpa, ON jord, OE eorpe, OHG erda, etc., general Gmc. : Ir. ert ‘land’ occurring only in epds., OHG ero ‘earth’, Grk. épa attested by épas’ vis Hesych. and épafe ‘to the ground’. Any further root connection is uncertain, so that the semantic starting-point remains obscure, though prob. b. Walde-P. 1.142. Feist 25f.
Goth. land, etc., general Gme. : Ir. wh-land ‘threshing floor’ (epd. of ith ‘grain’), W. llan ‘inclosure, yard’, etc. Its earliest use was sense e, and in Goth- ic it is only so used, namely for ‘piece of land’ or ‘country’, airpa being used in all other senses, including ‘land’ in con- trast tosea. Walde-P. 2.438. Feist 321 f.
6. Balto-Slavic words, above, 1.
Pol. lad fr. NHG land.
7. Skt. ksam- (Vedic), Av. zam-, above, 1.
Skt. bhi-, bhiimi-, OPers. biimi-, Av. bumz- (less common than zam-), fr. bhi- ‘be’, hence first used of the earth as the known world. ;
Other common Skt. words for ‘earth’ are prthivi- fem. of prthu- ‘wide’, mahi- fem. of mah- ‘great’, ksiti- properly ‘abode’, vasu-dha- lit. ‘yielding good’, etc.
1.212 EARTH = GROUND, SOIL
As already remarked, the words for earth’, among their various applica- tions, are used for the earth’s solid sur- face (‘falls to earth, the ground’) or its soft surface for cultivation (‘good earth land, ground, soil’). They are, in fact, the usual expressions of these senses, %
```


## [2026-09-05T20:58:38.022Z] TOOL CALL #45: Bash

```json
{
 "command": "pdftoppm -f 180 -l 180 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg180 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 180"
}
```


## [2026-09-05T20:58:39.657Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"ghdem\\|ghdom\\|ghom-\\|ghmon\\|guma\" IEC.txt | head -10; echo \"=== SKT bridegroom ===\"; grep -n -i \"bridegroom\" SKT.txt | head -5; echo \"=== LAT humus ===\"; grep -n \"^humus\\|humus,\" LAT.txt LEW_1910.txt | head -10",
 "description": "Grep Mann, Skeat, Latin dicts"
}
```


### [2026-09-05T20:58:41.096Z] TOOL RESULT

```
total 23336
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:58 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:58:41.191Z] TOOL RESULT

```
=== IEC ===
5987:&hem- (ghom-, 8hm- with u-basis) “ground, earth; on the ground, on (to, in) the ground, down". WP I, 662 Av. zom, f.; Per. cf. zamin, id.; Hitt. cf. gimras *countryside; campaign'; Thrac. cf. zémele- “low fellow, captive, slave’; Cypro-Myc. (que- ried) kham-, cons. decl. ‘land’; Gk. cf. khamaí “on the ground’; Siculian hemitom (queried: “of clay); Lat. humus, gs -1, f. (u-basis); Umbr. cf. hun-tru ('down', fr. *&hm-tero-, compara- tive); OCS zemlja, f.; Cz. země “land, ground”, na zem ‘to the ground’; na zemi (on the. . .); R nà-zemí *down, on the ground"; Li. Zéme, beside Zémas, adj. lowlying'; Zemýn *down- ward’; Zemai “on the ground’; Zemiaü *down- ward'; Latv. zeme, beside zem, prp. “under”; zemē ‘below’; zemi, zemu, adv. lowlying'
6080:pl. ‘men’; Umb. homonus, dp ‘to men’; Go. guma, gs gumins, pl. gumans; OE guma; OHG gomo, gs -en; MHG gome, gume; ON cf. gumi, coll. gumnar; OLi. Zmuð, pl. Zmónes (mod. žmónēs) ‘man; husband’; cf. žmona ‘wife’; e-gde in Ir. geamán-ach ‘servant’; Cz. zeman ‘farmer’. (Note: Li. sg. Zmogüs “man, human being’ contains the element of Li. guvùs, root *guu- ‘lively, alive’, cf. Gk. prés-bus, -gus “old man’; prés-ba *venerable")
=== SKT bridegroom ===
8036:Groom.  (E.)  Prob.  for  goom.  We  fit indeed,  O.  Du.  grom,  Icel  gromr,  a  b( lail ;  but  these  have  no  obvious  etymolo: and  may  be  the  same  as  O.  Du  gem^  Ici giimi,  a  man.  If  the  r  crm  thuj  be  d posed  of.  the  etym  is  from  A.  S.  guifza man,  allied  to  Icel.  gnmi^  Goth,  gnma, homo,  a  man.  In  the  comp.  bridegroom it  is  quite  certain  that  the  r  it  iotiusir I  SIC  Bridegroom. j    Groove ;  see  Grave  (i).
=== LAT humus ===
LAT.txt:28352:en latin, ou l'on a, d'une part humus, de 1 'autre, hemo, homB, la
LAT.txt:28701:humus, -i £. (comme les autres noms de la terre, tellUs, terra',
LAT.txt:28728:L'autre, y 6 <t)v, X a t J ' txl, > a P 01ir correspondant le mot derive humus, qui,
LAT.txt:49383:due k un rapprocbement fait avec humus, humare. Le suffixe est 1 e
LAT.txt:69565:laire, en rapprochant umor de humus, a dot£ ces mots d'un h adventice;
LAT.txt:70794:populaire avec humus, les emplois de ces formes sont rares, et presque
```


## [2026-09-05T20:58:46.009Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg180.png"
}
```


### [2026-09-05T20:58:46.543Z] TOOL RESULT

```

```


## [2026-09-05T20:58:46.540Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:59:12.120Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:59:12.168Z] TOOL RESULT

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


## [2026-09-05T20:59:34.491Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:59:34.496Z] TOOL RESULT

```


```


## [2026-09-05T20:59:38.864Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Khwarazm",
 "prompt": "What does the article say about the etymology of the name Khwarazm / Chorasmia (Old Persian Uvārazmiš, Avestan)? List all proposed etymologies with their proponents. Also what does it say about the relation to Airyanem Vaejah?"
}
```


## [2026-09-05T20:59:39.463Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/algorithm",
 "prompt": "Give the full etymology entry for algorithm and algorism, including dates, French, Medieval Latin, Arabic al-Khwarizmi."
}
```


### [2026-09-05T20:59:46.267Z] TOOL RESULT

```
# Etymology of Khwarazm/Chorasmia

The article presents multiple proposed etymologies:

## Proposed Etymologies

**Yaqut al-Hamawi's theory:** A Persian compound of *xwār* (food/cooked) and *razm* (battle), referring to "the abundance of cooked fish as a main diet."

**C.E. Bosworth's theory:** Derived from *xwar* (sun) and *zam* (earth/land), designating "the land from which the sun rises."

**Alternative Iranian view:** Represents "lowland" from *xwār* (low) and *zam* (land), reflecting Khwarazm's status as Central Asia's lowest region.

**Geographic interpretation:** Various forms of *xwar/xar/xor* commonly denote "tidal flats, marshland, or tidal bays" in Persian Gulf regions.

## Connection to Airyanem Vaejah

The article notes that some early scholars identified Khwarazm with *Airyanem Vaejah*, the legendary Aryan homeland in Avestan texts. However, scholarly opinions diverge:

- **Supporters:** Elton L. Daniel considers Khwarazm "the most likely locale" for the original Avestan homeland; Dehkhoda calls it "the cradle of the Aryan tribe."

- **Skeptics:** Michael Witzel argues *Airyanem Vaejah* was in Afghanistan instead.
```


### [2026-09-05T20:59:46.303Z] TOOL RESULT

```
# Etymology of Algorithm and Algorism

**Algorithm (1690s)**
The term originates from French *algorithme*, which was "refashioned (under mistaken connection with Greek *arithmos* 'number') from Old French *algorisme*" referring to the Arabic numeral system. The Medieval Latin *algorismus* traces back to Arabic *al-Khwarizmi*, meaning "native of Khwarazm" (modern Khiva, Uzbekistan). This was the surname of a mathematician whose works introduced sophisticated mathematics to Western Europe.

**Algorism (early 13c.)**
The earlier Middle English form *algorism* came directly from Old French, deriving from the same Medieval Latin *algorismus* and Arabic source as algorithm.

**Semantic Evolution**
Originally designating the Arabic computational system, the word's meaning broadened to encompass any computational method. From the mid-twentieth century onward, it became particularly associated with computing processes.

Both terms represent European linguistic adaptation of an Arabic scholar's name, demonstrating how mathematical innovations traveled westward through translation and linguistic transformation.
```


## [2026-09-05T20:59:52.900Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0%C7%B5%CA%B0%C3%A9m-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Latin humus/homo, Greek khthon, Germanic *gumô, Proto-Iranian *dzam- / Avestan zam-, Old Persian). Also any note on Pokorny page number."
}
```


## [2026-09-05T20:59:54.290Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%85%DB%8C%D9%86",
 "prompt": "Give the Persian etymology of زمین: Middle Persian form, Proto-Iranian, Old Persian, Avestan, PIE, and cognates."
}
```


### [2026-09-05T20:59:54.895Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:59:59.983Z] TOOL RESULT

```
# Persian Etymology of زمین

**Middle Persian:** zmyk' (zamīg, "earth")

**Proto-Iranian:** *jā́h

**Proto-Indo-Iranian:** *ȷ́ʰžʰā́s

**Proto-Indo-European:** *dʰéǵʰōm

**Cognates include:**
- Northern Kurdish: zevî
- Northern Luri: زمی (zemi)
- Avestan: 𐬰𐬃 (zā̊)
- Sanskrit: क्ष (kṣa)

The word evolved from earlier زمی (zamī) in Persian, tracing back through these ancient language families to ultimately derive from the Proto-Indo-European root.
```


## [2026-09-05T21:00:03.578Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0%C7%B5%CA%B0%C3%B3m",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Latin humus/homo, Greek khthon, Germanic *gumo, Proto-Iranian, Avestan zam-, Old Persian). Also any note on Pokorny page."
}
```


## [2026-09-05T21:00:05.411Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gum%C3%B4",
 "prompt": "Give the reconstruction *gumô, its meaning, etymology (from PIE dhghom-on-), and descendants including Old English guma and the compound bridegroom."
}
```


### [2026-09-05T21:00:05.641Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T21:00:11.832Z] TOOL RESULT

```
# Proto-Germanic *gumô

**Reconstruction:** *gumô (masculine an-stem noun)

**Meaning:** "man"

**Etymology:** The term derives from Proto-Indo-European *ǵʰmṓ ("human"), which is "Cognate with Latin homō ('human being')."

**Key Descendants:**

- **Old English:** guma, which evolved through Middle English forms (gome, gom, gomme, gone, goom, goome, gume) into Modern English gome
- **Old Norse:** gumi, preserved in Icelandic gumi and Danish gom
- **Old High German:** gomo
- **Gothic:** 𐌲𐌿𐌼𐌰 (guma)
- **Compound:** *brūdigumô, which survives in Swedish brudgum ("bridegroom")

The term appears in an "an-stem" declension pattern typical of Proto-Germanic masculine nouns, with distinct forms for nominative, accusative, genitive, and other cases across singular and plural.
```


## [2026-09-05T21:00:20.997Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰéǵʰōm",
 "prompt": "Give the reconstruction, meaning, Pokorny reference, and descendants: Latin humus, Proto-Hellenic/Greek khthon, Proto-Indo-Iranian, Avestan zam-, Old Persian, and the derived term *dʰǵʰmṓ 'earthling, human'."
}
```


## [2026-09-05T21:00:23.186Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/chorasmia-i",
 "prompt": "What does Encyclopaedia Iranica say about the name Chorasmia / Khwarazm: Old Persian Uvārazmiš, Avestan form, and proposed etymologies (huvāra 'good land', 'lowland', 'sun land')? Also anything about identification with Airyanem Vaejah."
}
```


### [2026-09-05T21:00:25.244Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T21:00:28.037Z] TOOL RESULT

```
# Proto-Indo-European *dʰéǵʰōm

**Reconstruction:** *dʰéǵʰōm (feminine noun)

**Meaning:** "earth"

**Key Descendants:**
- Latin: *humus* (via Proto-Italic *homos)
- Ancient Greek: *khthṓn* (via Proto-Hellenic *kʰtʰṓn)
- Proto-Indo-Iranian: *ȷ́ʰžʰā́s* (Avestan *zəmar*)
- Old Persian: attested through Proto-Indo-Iranian branch

**Derived Term:**
The page notes that *dʰǵʰmṓ* ("earthling, human") derives from this root.

**Pokorny Reference:** Not explicitly stated in this Wiktionary entry, though the article provides extensive etymological discussion citing scholars like Kloekhorst and Ringe.

**Additional Note:** The etymology involves "From *dʰeǵʰ- +‎ *-ōm," with scholarly debate about whether the root is *dʰeǵʰ-* or *dʰeǵ-* based on Sanskrit and Anatolian evidence.
```


## [2026-09-05T21:00:31.094Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bridegroom",
 "prompt": "Full etymology of bridegroom: Old English brydguma, guma 'man', PIE root, and how the -r- got in."
}
```


## [2026-09-05T21:00:32.337Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Khiva",
 "prompt": "What does the article say about the etymology and origin of the name Khiva (Khivaq, Xiva)? Is the name derived from Khwarazm? Any legends about the well Kheyvak?"
}
```


### [2026-09-05T21:00:37.956Z] TOOL RESULT

```
# Etymology of Bridegroom

The word "bridegroom" originates from Old English *brydguma*, combining *bryd* (bride) with *guma* meaning "man." The *guma* element traces back to Proto-Germanic *\*gumon-*, literally meaning "earthling, earthly being," derived from the PIE root *\*dhghem-* meaning "earth."

**The "-room" Mystery**

A significant linguistic shift occurred in the 16th century. The original ending underwent "folk etymology after groom (n.) 'groom, boy, lad.'" This means speakers reinterpreted the unfamiliar final syllable, reshaping it to match the more recognizable word "groom," transforming *brydguma* into *bridegroom*.

**Comparative Evidence**

This pattern appears across Germanic languages—Old Saxon *brudigumo*, Old Norse *bruðgumi*, and German *Bräutigam* all share similar structures. Interestingly, Gothic diverged entirely, using *bruþsfaþs*, literally "bride's lord," instead of adopting the compound form used by other Germanic peoples.

The shift demonstrates how folk etymology can alter word forms when their original components become obscure to speakers.
```


### [2026-09-05T21:00:40.091Z] TOOL RESULT

```
# Etymology and Origin of Khiva

According to the article, the origin of Khiva's name is **unknown**, though several theories exist.

## Proposed Derivations

One theory suggests the name comes from Persian Khwarezm: "the name comes from the Persian word Khwarezm, altered by borrowing into Turkic as Khivarezem, then shortened to Khiva."

## Legend of the Well Kheyvak

A traditional story attributes the name to Shem (Noah's son). According to this account, Shem dreamed of 300 burning torches in the desert and founded the city with its outline mapped according to these torch placements. The legend states: "Then Shem dug the Kheyvak well, the water from which had a surprising taste. It is possible to see this well in Ichan-Kala (an internal town of Khiva City) even today."

The article notes that these origin stories are "contradictory" and that the true etymology remains unclear, though the Khwarezm connection appears plausible given linguistic parallels.
```


## [2026-09-05T21:00:50.119Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا entries for خوارزم — especially any etymology (خوار + زم) and the identification with خیوه."
}
```


## [2026-09-05T21:00:51.285Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=algorithm",
 "prompt": "Give the American Heritage Dictionary etymology for algorithm (and algorism if shown), including Medieval Latin algorismus and al-Khwarizmi."
}
```


### [2026-09-05T21:00:57.036Z] TOOL RESULT

```
# خوارزم (Khwarezm)

## Etymology & Meaning

According to the Dehkhoda Dictionary and Mo'in Dictionary entries presented:

**Dehkhoda identifies the region as:** "a territory in the lower Oxus River area, historically home to the Aryan people" with alternate names خوراسمیه and خوراسمیا.

**Etymology via compound formation:** The entries suggest خوارزم derives from خوار (meaning "lowly/defeated") + رزم (meaning "battle/war"), yielding a sense of "the land of difficult warfare."

## Geographic & Historical Context

This ancient Iranian territory in Central Asia corresponds to modern Khiva and encompasses areas now split between **Uzbekistan and Turkmenistan**. Major historical cities included Gorganj (Urgench), Kath, and Khiva.

The region was:
- Part of the Achaemenid Empire
- An important Sasanid province (242-350 CE)
- A major center of Persian culture until the devastating Mongol invasions (early 13th century)
- Subsequently ruled by various dynasties including the Khwarazmshah dynasty

The territory was formally separated from Iran through the **Akhal Treaty of 1881**.
```


### [2026-09-05T21:00:57.508Z] TOOL RESULT

```
# Algorithm Etymology from American Heritage Dictionary

According to the dictionary entry, **algorithm** originated as a variant of **algorism**, likely influenced by the word "arithmetic" or its Greek source *arithmos* ("number").

The term traces back to **al-Khwarizmi**, a ninth-century mathematician from Khwarizm (a region near the Aral Sea in south-central Asia). His full name was Muhammad ibn-Musa al-Khwarizmi (780?-850?).

The dictionary explains: "Algorism, the English word for computation with Arabic numerals, is derived from Al-Khwarizmi's name." Al-Khwarizmi wrote treatises on using Arabic numerals for mathematical computation, which Europeans learned through Arabic mathematical texts.

The entry notes that with 20th-century computing developments, "algorithm" was adopted "as a convenient word for a recursive mathematical procedure, the computer's stock-in-trade."

The dictionary does not provide a separate entry for Medieval Latin *algorismus* beyond its connection to the Arabic mathematician's name.
```


## [2026-09-05T21:01:05.842Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"zamīk\\|zamīg\\|zamik\\|zmyk\" NYB_vol2_glossary.txt | head -5; echo \"=== LKT algorism ===\"; grep -n -i \"algorism\\|Chwarizmi\\|Khwarizmi\\|Chwarezm\" LKT.txt | head -10; echo \"=== FSD bridegroom ===\"; grep -n -i \"bridegroom\" FSD_vol1.txt | head -3; echo \"=== WEB humus ===\"; grep -n \"humus\" WEB_vol1.txt | head -3",
 "description": "Grep Nyberg, Lokotsch, FSD, Webster"
}
```


### [2026-09-05T21:01:05.937Z] TOOL RESULT

```
=== NYB ===
1175:damik [dmyk] earth: 1. as opposed to the firmament 3377. 37, 526, 83-93 passim. — 2. the terrestrial world, 515. 5211, 6710, 8913, 99-104 passim. — 3. ground, soil 926, 21-29 passim. 3316-21, 3916, 606. 89-95 passim, etc. — 4. in a geographical sense 719. 86, 1134. 11517-18, 1173; pl. ~ tha 109%. — SW form of zamik (Ps. zmyk), which occurs just as often in MSS and editions. MPrth Prs zmyg, NP zami, archaic form for modern zamin; Av. (1662 sqq.) zam-.
3201:. raftan to keep company with, to communicate with 702-8; — apar én zamik ravét he moves on this earth 3333; apar zanišn raft hend they went to slay (him) 4515-16. — hac from 62. 569.809; — 6 to 3726, 385-9 etc. passim ; — pat gehän *hamāi raft hom I roamed the world all about 318-9 (kame would not suit the context; cf 952° s, v. hamäk); — with prev.: andar ~ : ka srav ... 0$ (prep.) mart (+...) andar rajt ēstāt when the report had reached that man (who ...) 4424-26; došar"% ... andar 6 [KN] ravét will move, roam freely in Hell 347-8; — apar ~ : 6 õi ket apar raft hénd they went off to the sooth- sayer 379; 3811-15, 415, ete. — be ~ : fra- tom 6 änöd apar raft, avdom be raft (he was the first to step in there) and the last to step out 496-?-20; 5714-15; pas patvand hac oisan be raft then offspring proceeded from them 941°; very often bē only indicates the aspect: ētēn sart bē raft i-š ... went ahead so vehemently that 3315; bē rav! 6019; adak ēišān bē raft hend 5712; — frac ~ : frac raft Pourusäsp
=== LKT algorism ===
2144:"NTpr.,  eine  Landschaft  in  Mittelasien  [dem heutigen  Chanate  Ghiva-HIwa  entspre- chend]; davon  das  ar.  Adj.  hnärizmi  od. härizmi  'aus  Hwarizm  stammend,  der Gharizmier',  Beiname  des  Mathematikers ABÜ  GA'FAR  MUHAMMAD  IHN  MÜSÄ [s.  hier  Nr.  631];  durch  sein  Werk  über Algebra  kam  das  dekadische  Zahlensystem und  das  Rechnen  mit  ar.  Zahlen  um  das Jahr  1200  nach  Europa;  daher  wurde  lat. algorithmus,  algorismus  [mit  Anlehnung an  gr.  öpi&|ui6<;]  die  Bezeichnung  für  das Rechnen  mit  ar.  Ziffern  u.  schließlich  für Rechnungsverfahren  überhaupt.  Hieraus afrz.  algofisme,frz.  algorithme,it.alguaris- nio  'Rechenart,  Arithmetik',  sp.  alguaris- nio,  guarismo  'Ziffer',  engl,  algorism, algorithm  'Rechenart'.  [DE  130/131. WOEPGKE  in  JAs  (1863)  I,  519.  Devic DEt  18.  Lammens  Rem  13.  Schirmer WortschdMath  4/5.
5918:algorism  890
7423:Aegidius  951 aegyptus  1222 alambicum  79 alchanna  867 algorismus  890 algorithmus  890 alleluia  793 ahnageshim  1348 almutium  1520 amaracum  1411 amen  68
=== FSD bridegroom ===
22653:pasaueflower.  which  ccncrally  blossoms  about  Easter.—  a"pro-so'pl-a.  1   o'pro-sfi'pt-a;  2   Spro-sO'pt-a,  n.  Teral. A.  gentleman!,  a   bridegroom.—  A"pnl«esque  ,   o.  Like  Absence  of  the  greater  part  of  the  face.  [   <   Gr.  aprosdpos, ^   „   -   „   .   ~   rT. ,   <   a-  priv.  +   prosdpon.  face.]  —   a"pro-so'pous,  a.
25525:Parthia  and  Armenia,  dating  from  about  250  B.  C.  to  bridegroom  to  the  bride's  father.  [<  Sans,  arsna.]
29055:—   auld  lang  syne,  days  gone  by,  especially  happy  days. —   A.  Llcht  ( Eccl .   Hist.),  one  of  the  supporters  of  the  old, or  conservative,  party  of  the  Scottish  Church  in  the  latter half  of  the  18th  century.  Compare  burgher,  2.  A. UghtJ.— A.  Reekie,  Old  Smoky:  a   sobriquet  of  Edin- burgh.— A.  Robin  Gray,  a   Scotch  ballad  written  by  Lady Anne  Barnard,  In  1772,  to  the  Scotch  air  The  Bridegroom Grat  When  the  Sun  Went  Down.
=== WEB humus ===
68705:ex-hi-ma’tion, n. [LL. exhumatio (-onis), from exhumare, to dig up. exhume; L. ex, out, and humus, the EE act of exhuming; aa isnt eens PEN ahi AET.
68706:ex-hime’, v.t.; exhumed, pt., pp.; exhuming, ieee ger, (LL, exhumare, to dig out of the paar: ex, out, and humus, the ground.]
92761:humanus; to homo, a man, humus, soil.) 1. of or characteristic of a person or persons; sac as people have.
```


## [2026-09-05T21:01:09.567Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wikipedia.org/wiki/Khwarazm' --note 'page 180, root Ghdhem, node 4/5: etymologies of Khwarazm (Bosworth xwar+zam, lowland) and Airyanem Vaejah identification' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/algorithm' --note 'page 180, nodes 7-10: algorism/algorithm chain ML algorismus < Arabic al-Khwarizmi, Fr algorithme' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B2%D9%85%DB%8C%D9%86' --note 'page 180, node 2: Persian zamin < MP zamig < PIE dheghom' 2>&1 | tail -3",
 "description": "Archive web sources part 1"
}
```


### [2026-09-05T21:01:12.226Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/665ecff8e7934338.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4d7501a1c70bce5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ccc250ac8ab7a4e.txt
```


## [2026-09-05T21:01:28.664Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gum%C3%B4' --note 'page 180, node 15/16: *gumo is Proto-Germanic (OE guma), not Greek; bridegroom' 2>&1|tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/bridegroom' --note 'page 180, node 16: OE brydguma, guma < PGmc *gumon- earthling, PIE dhghem-' 2>&1|tail -2; python3 tools/fetch_source.py 'https://en.wikipedia.org/wiki/Khiva' --note 'page 180, node 5: origin of the name Khiva unknown; one theory via Turkic Khivarezem < Khwarazm' 2>&1|tail -2; python3 tools/fetch_source.py 'https://ahdictionary.com/word/search.html?q=algorithm' --note 'page 180, nodes 7-10: AHD entry algorithm/algorism < al-Khwarizmi' 2>&1|tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85/' --note 'page 180, node 5: Dehkhoda/Moin on خوارزم, modern Khiva' 2>&1|tail -2",
 "description": "Archive remaining web sources"
}
```


## [2026-09-05T21:01:30.401Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"زمین\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY latin ===\"; grep -n -i \"GHDHEM\\|DHGHEM\\|GHDEM\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Grep Aryanpur for zamin"
}
```


### [2026-09-05T21:01:33.821Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b18263a6af2d5324.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/432b44b13cdb674c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/409368c96b91e96c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2626dfa3c071458.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce6f67d990ec1fc5.txt
```


### [2026-09-05T21:01:33.874Z] TOOL RESULT

```
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
90:نژادهای «پست‌تر» بیشتر شد. بهمین دلیل در سرزمین‌های دور از آلمان درصد مردم چشم آبی و
108:سرزمین آغازین هند و اروپائیان
111:کردستان و سرزمین‌های اطراف آن است چون در اين نواحی بود که در حدود ده هزار سال پیش
114:سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا
=== ARY latin ===
```


## [2026-09-05T21:01:37.825Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^زمین\\|زمین (\\|زمین:\\|dhghem\\|ĝhem\\|ghem-\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== latin index sample ===\"; grep -n -i \"HUMUS\\|HOMO\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Grep Aryanpur more"
}
```


### [2026-09-05T21:01:37.886Z] TOOL RESULT

```
=== latin index sample ===
9426:4, oe? pHE ALBANIAN) gldT HUMUS LATIN) 3
13908:THOMO STIFVE Mics dab (OLD SCANDINAVIAN) 5;scle\
15619:(ALSO) 102, (SAME) 131 HOMOS, HOMO. GREEK) gli
```


## [2026-09-05T21:01:42.880Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor ln in (9426,15619):\n    print('--- line',ln,'---')\n    print('\\n'.join(d[ln-4:ln+3]))\n    # find nearest pdf page tag above\n    for j in range(ln,0,-1):\n        if '[pdf page' in d[j]:\n            print('PAGE TAG:',d[j]); break\nEOF",
 "description": "Inspect Aryanpur index lines"
}
```


### [2026-09-05T21:01:44.614Z] TOOL RESULT

```
--- line 9426 ---
SEMMIN, :(OLD PRUSSIAN) Ot 8 KEM :(TOKHARIAN B)B (5 os
| SAME Co KSAM, JMA (SANSKRIT) cy Sail
i DU, DON» (i RIsH) AG y! KHTHON AGREER) lip,
4, oe? pHE ALBANIAN) gldT HUMUS LATIN) 3
TEKAN HITTITE) ca OLD CHURCH SLAVIC) x5 53%\
' : ZEMLJA
‘REFERENCES cutKay ZIEMIA POLISH) gong)
PAGE TAG: [pdf page 325]
--- line 15619 ---

(MEME) 234, (AVEC) 301 | SOMA s(TOKHARIAN A) A ri ,
MACKENZIE: SAM, SAAB": oansKre es Sc
(ALSO) 102, (SAME) 131 HOMOS, HOMO. GREEK) gli
BUCK: om SIMILIS, SIMUL LATIN) gs
ONIONS: (SAME) 785 SAMA- GOTHIC) $3 $F
SKEAT: (SAME) 533 (OLD SCANDINAVIAN) 4S 54th!
PAGE TAG: [pdf page 534]
```


## [2026-09-05T21:01:50.201Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(d):\n    if 'KHTHON' in p:\n        print('block',i)\n        print(p[:1400])\nEOF",
 "description": "Print Aryanpur page with KHTHON"
}
```


### [2026-09-05T21:01:52.008Z] TOOL RESULT

```
block 324
[pdf page 325]
| te
|
SEMMIN, :(OLD PRUSSIAN) Ot 8 KEM :(TOKHARIAN B)B (5 os
| SAME Co KSAM, JMA (SANSKRIT) cy Sail
i DU, DON» (i RIsH) AG y! KHTHON AGREER) lip,
4, oe? pHE ALBANIAN) gldT HUMUS LATIN) 3
TEKAN HITTITE) ca OLD CHURCH SLAVIC) x5 53%\
' : ZEMLJA
‘REFERENCES cutKay ZIEMIA POLISH) gong)
POKORNY, SO*~*~*~S*~*«SdNS SEMLYA (RUSSIAN) yoy
DELAMARRE: (LA TERRE) 181 ZEME (CZECH) Sy
MACKENZIE: (EARTH) 112 ZEMLJA (SERBIAN) 9 po
z BUCK: 16-17 ZEME (BOHEMIAN) gus y
SKEAT: + (GHEL-, GHEM) 757 ZEM SLOVAK) Suh
rrr sebuoby ZHEME LITHUANIAN) gi)
, ZEME LATVIAN) (3) 95
ea PERL el |
Pwo ester |
KONA, KVAN JANI, GENA, JAIN] (AVESTAN) glu!
QVENA, — (OLD SAXON) oS gp-S ZAN (PAHLAVI) 5 3h
QVAN . JIN (KURDISH) 63,5
(OLD HIGH GERMAN) oS gl JAN S(BALUCHI) gx sh
QUENA, GUENA JINAL AFGHAN) ( =), 3lsi!
CWENE, (OLD ENGLISH) oS ssi SAM -(TOKHARIAN A) A 5,65
CWEN SANA -(TOKHARIAN B) B ys 63
QUEAN, QUEEN (ENGLISH) AS! JANIS (SANSKRIT) 24 Sie
KVINDE, KONE —«(DANISH) S\ail2 KIN ARMENIAN) «gi 5)
KVINNA, KONA (SWEDISH) 3» GYNE (GREEK) ii.
KVINNE (NORWEGIAN) (5335 QUING, GENS, GOTHIC) S36
QUENE (DUTCH) sachs KWENS
(OLD CHURCH SLAVIC) ot Gel (OLD SCANDINAVIAN) 45$4h—11
a
```


## [2026-09-05T21:02:00.776Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LAT humus ===\"; sed -n '28695,28740p' LAT.txt; echo \"=== AFM khwarazm ===\"; grep -n \"خوارزم\" AFM.txt TAD.txt 2>/dev/null | head -5",
 "description": "Read Ernout-Meillet humus and grep Arabic sources"
}
```


### [2026-09-05T21:02:00.844Z] TOOL RESULT

```
=== LAT humus ===
hDc: v. hic.
hui: exclamation d' 4 tonnement ou d'admiration. Langue familibre.
humfinus: v. hom~ 6 .
humeS: v. ume S.
humerus: v. umerus.
(h)umor, (h) umidus : v.umor.
humus, -i £. (comme les autres noms de la terre, tellUs, terra',
par r 4 action du genre sur la forme, abi. humu dans Varron cite par
Non. 4O8, 5sqq., gen. humGs dans les inscriptions ; inversement quelques
traces du genre masculin dans Laevius et T. Gracchus): terre, sol;
Xoc.huml "par terre, sur le sol"; cf. Varr. L.L. 5,33, terra, ut putant,
eadem et humus; ideo Ennius (Sc. 411 V.) in terram cadentis dicere
"cubitis pinsibant humum", et quod terra sit humus ideo is humatus
mortuus, qui terra obrutus... et dicitur humilior qu.i ad terram de-
missior, infimus humillimus, quod in mundo infima humus. Souvent mis
en rapport par l' 4 tymologie populaire avec (h)umidus. Pas de pluriel.
D 4 riv 4 s et composes: humilis : "qui reste a terre, qui ne s' 41 bve
pas de terre", et au sens moral "humble, bas", etc.; humiliter,-tas,
-tatula,-tudo (Gloss.); perhumilis, thelohumilis (trbs tardifs );
et a basse 4 poque humilis (humilo , cf. leudrej leuis , etc.), humiliatio,
et humi lito,-ds = Tcmetvoa) ( cf. nobi lis, nobilita), hiinilitdtio (Gloss.);
hum-ilifico (Tert.); humo,-as "enterrer" (les morts), d'ou humStiO,
-tor (rare), - tus,-us m.; inhumdtus "non enterre", sens classique:
ce n 1 est qu'a partir de Pline qu'on voit apparaitre inhumare avec
in- local, "mettre en terre, inhumer" d'ou inhumator; pollinctor
(Gloss.): circum-, ob-humo. II est k noter que les Latins n'ont jamais
eu terrdre, interrSre dans ce sens. Cf. aussi homS.
Humus se rencontre k toutes les epoques. Mais le mot courant est
terra qui l'a supplante dans les 1. romanes; les repr 4 sentants de hu¬
milis sont de la langue savante; cf.M.L.4335. Le celt. a: iri .uim,
humal', le britt. ufyll, ufylldod.
Des deux noms indo-europ 4 ens de la "terre" qui figurent en grec,
le latin n'a pas conserv 4 celui qui r 4 pond a gr. epa et k all.erde.
L'autre, y 6 <t)v, X a t J ' txl, > a P 01ir correspondant le mot derive humus, qui,
des la date la plus ancienne, tend en italo-celtique a etre remplace
par le groupe de terra. - Ce nom avait a 1 'initiale une forme alter¬
nante, a groupe de consonnes dans v 4 d. k§dh, loc .ksdmi, g 4 n .jmdh (et
gmdh), gr.yQoJv, v.iri. dii (gen. don), v. Rev. celt., 40,437 , k consonne
simple dans gr. x a (J- a l' e t sans doute dans a y.za, g&n.zamG, loc.zemi.
Le hittite a tskan (g 4 n .taknds) ou dagan issu de *g(h)edhom~, le
tokh. A tkam (D han) "terre", dont la dentale rappelle celle de gr.
X 0 wv; cf.Pedersen, Groupement 41 et s., et aussi Kretschmer, Glotta
«0,65. Au lien du nom racine, il jr a des derives, en -a-: gr. x°H^C e539
hyoscyamos
et ya^aC (avec le compose veo—'/j x~OC, "nouveau, etrange"), en -y- suivi
de voyelle longue dans v.sX.zemlja et Xit.Seve, en -o- dans 1 at. humus .
=== AFM khwarazm ===
```


## [2026-09-05T21:02:07.521Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"bridegroom, n\\..\\{0,600\\}\" KLN_1971.txt | head -2; echo \"=== humble ===\"; grep -n -o \"humble, adj\\..\\{0,400\\}\" KLN_1971.txt | head -2",
 "description": "Grep Klein for bridegroom and humble"
}
```


### [2026-09-05T21:02:09.257Z] TOOL RESULT

```
33727:bridegroom, n. — ME. brudgume, bridegome , fr. 
=== humble ===
116662:humble, adj. — ME. humble , umble , fr. OF.(= F.)
```


## [2026-09-05T21:02:11.901Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33727,33750p' KLN_1971.txt; echo \"====\"; sed -n '116662,116680p' KLN_1971.txt",
 "description": "Read Klein bridegroom and humble"
}
```


### [2026-09-05T21:02:12.013Z] TOOL RESULT

```
bridegroom, n. — ME. brudgume, bridegome , fr. 
OE. brydguma, rel. to OS. brudigumo, ON. brud- 
gumi, OHG. brutigomo, MHG. briutegome, G. 
Brautigam , ‘bridegroom’. For the first element 
in bridegroom see bride. The second element 
arose through the substitution of groom (q.v.) 
for OE. guma, ‘man’, which is rel. to OS. gumo. 




95 



BROADLOOM 



gomo, ON. gumi, OFris. goma , OHG. go mo, 
Goth. guma y ‘man’, and cogn. with L. homo , 
‘man’. See human. 

bridewell, n. P house of correction, prison. — 
====
humble, adj. — ME. humble , umble , fr. OF.(= F.) 
humble , fr. L. humilem , acc. of humilis, ‘low, 
base, humble’, lit. ‘on the ground’, fr. humus , 
‘earth, ground, soil’. See humus and words there 
referred to and cp. esp. humiliate, humility. 
Derivatives: humble , tr. v., humble-ness , n., 
humbl-er, n., humbl-ing, n., humbl-y , adv. 
humblebee, n., a bumblebee. — ME. humbyl-bee, 
a compound whose first element is rel. to Dan. 
humle , humlebi , Swed., Norw. humla, MDu. 
hummel, homel, hommel, Du. hommel , OHG. 
humbal, MHG. humbel, hummel , G. Hummel, 
‘humblebee’, prop, ‘the humming bee’. See hum, 
‘to utter an inarticulate sound’, and freq. suff, 
-le, and cp. Czech 6mel , Pol. czmiel, OPruss. 
camus, Lith. kamane, ‘humblebee’, which are 
also of imitative origin. For the second dement 
in ME. humbyl-bee see bee. 
humble pie, pie made of the umbles of a deer. —
```


## [2026-09-05T21:02:26.135Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -l \"transcription_suspect\" page-1*.json | head -5; echo ---; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('/home/sfmqrb/git/rishe/data/verification/page-1*.json')):\n    d=json.load(open(f))\n    for e in d['entries']:\n        if e.get('verdict')=='transcription_suspect':\n            print(f, 'ROOT', e['root'], '|', e.get('note','')[:200], '| error_in=',e.get('error_in'))\nEOF",
 "description": "Check precedent for root-level transcription_suspect"
}
```


### [2026-09-05T21:02:28.018Z] TOOL RESULT

```
page-100.json
page-103.json
page-101.json
page-121.json
page-110.json
---
/home/sfmqrb/git/rishe/data/verification/page-106.json ROOT Čîxâ, Čixâ, Čĕxara | Two separate problems. (1) The form: there is no Sanskrit *čikhā or *čekhara. The words Nourai means are śikhā- (शिखा) 'tuft of hair, crest, point, tip, flame-point' and śekhara- (शेखर) 'crest, peak'. | error_in= book
/home/sfmqrb/git/rishe/data/verification/page-140.json ROOT Drassoman | There is no Greek word 'Drassoman'. The printed page (pdf p.140, image kept at data/verification/sources/refs/ocr/BOOK/140.png) really does read 'Drassoman', so this is Nourai's own misprint/mis-trans | error_in= book
```


## [2026-09-05T21:04:02.849Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"airizem\\|xvairizem\\|äirizom\\|airizom\\|arizem\" BRT.txt | head -10",
 "description": "Grep Bartholomae for Avestan Chorasmia"
}
```


### [2026-09-05T21:04:02.888Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:04:05.125Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg180.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/180.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/180.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T21:04:05.189Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81598 Sep  5 17:04 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/180.png
```


## [2026-09-05T21:12:49.471Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build180.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ghdhem, Dhehem\",\n \"verdict\": \"transcription_suspect\",\n \"modern_form\": \"PIE *dʰéǵʰōm 'earth' (Pokorny's ĝhðem-, ĝhðom-, gen.-abl. ĝh(d)m-es; Watkins/AHD dhghem-)\",\n \"note\": \"The root itself is real and correctly labelled and glossed: Pokorny IEW 414-416 heads the entry 'ghdem-, ghdom-, Gen.-ablative gh(d)m-es' with the meaning 'earth, man, dragon', and Nourai's first spelling 'Ghdhem' is simply his own rendering of Pokorny's ĝhðem- (he writes the interdental ð as dh). The gloss 'earth' and the language label 'Indo-European' are right, and every branch drawn on the page (Av./OP zam-, Latin humus/homo/humanus, Greek khthon, Germanic *gumon-) is in Pokorny's and Watkins' own material. The flag is only for the SECOND form in the box. The printed page (pdf p.180, image kept at data/verification/sources/refs/ocr/BOOK/180.png) really does read 'Ghdhem, Dhehem', so the extraction is faithful; but 'Dhehem' is an impossible reconstruction — no source knows it. It is Nourai's misprint for Watkins/AHD's metathesised variant 'dhghem- (*dheghom)' (AHD Appendix, quoted verbatim under 'A word for the earth can be reconstructed as dhghem- (*dheghom)'), i.e. it should read 'Dhghem' or 'Dheghom'. Note also that the two forms are not two roots but the two conventional orderings of the same cluster (ĝhð- vs dhgh-), which Pokorny explains as a metathesis of *g(e)dhom-, *gh(e)dhom-. Two substantive weak spots further down the chart: node 4's gloss (Khwarazm as a 'city' and as the Airyanem Vaejo) and node 15, which the book labels Greek although its own source AHD says Germanic.\",\n \"note_fa\": \"جعبهٔ ریشه در بنیاد درست است: پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صفحهٔ ۴۱۴ تا ۴۱۶ سرواژهٔ «ghdem-, ghdom-» را با معنای «زمین، آدمی، اژدها» آورده است و صورت نخستِ نورایی یعنی Ghdhem همان ĝhðem- پوکورنی است (او دندانی‌میان‌دندانیِ ð را dh می‌نویسد). برچسبِ زبان (هندواروپایی) و معنای «زمین» نیز درست است و همهٔ شاخه‌های نمودار — zam- اوستایی و پارسی باستان، humus و homo لاتینی، khthōn یونانی و *gumōn- ژرمنی — در مادهٔ خودِ پوکورنی و واتکینز هست. اما صورت دومِ جعبه، یعنی «Dhehem»، در هیچ مأخذی نیست و صورتی ناممکن است؛ تصویر صفحهٔ چاپی نشان می‌دهد که خطای خوانشِ اسکن نیست بلکه خطای چاپی خودِ کتاب است و باید «Dhghem» (یا Dheghom) می‌بود، یعنی صورتِ قلب‌شدهٔ همان ریشه که فرهنگ American Heritage به کار می‌برد. این دو، دو ریشهٔ جدا نیستند بلکه دو ترتیبِ متعارفِ همان خوشهٔ همخوانی‌اند و پوکورنی خود آن را قلب (metathesis) از *g(e)dhom- می‌داند.\",\n \"error_in\": \"book\",\n \"book_prints\": \"Ghdhem, Dhehem : earth\",\n \"correct_form\": \"Ghdhem (= Pokorny ĝhðem-) / Dhghem (= AHD dhghem-, *dheghom)\",\n \"sources\": [\n   W + \"Reconstruction:Proto-Indo-European/d%CA%B0%C3%A9%C7%B5%CA%B0%C5%8Dm\",\n ],\n \"ref_check\": [\n  {\"ref\": \"POK:414\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt line 37728 ff.: 'Root / lemma: ghdem-, ghdom-, Gen.- ablative gh(d)m-es | Meaning: earth, man, dragon', ending 'References: WP. I 662 ff., WH. I 654 f., 663 ff., 869, Trautmann 369. Page(s): 414-416'. The material contains Av. za, Akk. zam, Gen. zamo 'earth'; gr. khthon; Lat. humus, homo, humanus; Goth. guma, OE guma, OHG gomo, NHG Brauti-gam — i.e. every branch Nourai draws. Exactly the root box, except for the spelling 'Dhehem'.\"},\n  {\"ref\": \"SYN:16\", \"status\": \"supports\",\n   \"note\": \"Buck, Selected Synonyms, section '1.21 EARTH, LAND', pp.16-17 (SYN.txt lines 781-828): '1. IE *ĝhem- and *ĝh(d)em-, representing the most widespread cognate group... Walde-P. 1.662 f.... Grk. khthon..., Lat. humus... beside humi 'on the ground', humilis 'low'... Av. zam- (gen. zemo = Skt. jmas) 'earth' in all senses (Barth. 1662 ff.)'. Nourai's page number is right to the page.\"},\n  {\"ref\": \"AHD:1513\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 382 carries the appendix entry verbatim: 'dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, \\\"earthling,\\\" in Germanic *gumon- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth... 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth... 5. ... a. Latin homo... b. (in part) Latin humanus, human, kind, humane... 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.]' The IE appendix of the AHD New College Edition runs pp.1505-1550, so p.1513 falls in the dh- range. This is the page Nourai's 'Dhehem' and his humus/homo/humanus/gumon/zamin branches all come from.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 662-664 (WLD_Bd1 djvu lines 41697-41830)\", \"stance\": \"supports\",\n   \"note\": \"Running head 'ghdem-, ghdom-, ghðmi'; the article gives 'lat. homo, -inis \\\"Mensch\\\" umgelautet aus alat. hemo (auch in nemo \\\"niemand\\\" aus *ne-hemo), acc. hemonem; dazu humanus \\\"menschlich\\\"' and 'got. guma, aisl. gumi, ags. guma, ahd. gomo \\\"Mensch, Mann\\\", nhd. in Brauti-gam (idg. *gh(e)mon- oder *gh(o)mon-)'. This is Pokorny's own source ('WP. I 662 ff.').\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. ĝhem- (IEC.txt line 5987) and ĝhom-on- (line 6080)\", \"stance\": \"supports\",\n   \"note\": \"'ĝhem- (ghom-, ghm- with u-basis) \\\"ground, earth; on the ground...\\\". WP I, 662  Av. zom, f.; Per. cf. zamin, id.; ... Gk. cf. khamai \\\"on the ground\\\"; Lat. humus...' and, in the 'man' entry, 'Umb. homonus, dp \\\"to men\\\"; Go. guma, gs gumins... OE guma; OHG gomo'. Mann too puts guma in Germanic and lists Persian zamin under the root.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. humus (LAT.txt lines 28701-28745)\", \"stance\": \"supports\",\n   \"note\": \"'Des deux noms indo-europeens de la \\\"terre\\\" qui figurent en grec, le latin n'a pas conserve celui qui repond a gr. era et a all. erde. L'autre, khthon, khamai, a pour correspondant le mot derive humus'; the alternation is spelled out 'ved. ksah, loc. ksami, gen. jmah ... gr. khthon, v.irl. du (gen. don) ... et sans doute dans av. za, gen. zamo, loc. zemi'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, entry for زمین, pdf p.325 = printed p.326 (ARY_latin_index_pages.txt block 324)\", \"stance\": \"supports\",\n   \"note\": \"The Persian headword's cognate list is exactly this root — 'KSAM, JMA (SANSKRIT) / KHTHON (GREEK) / DHE (ALBANIAN) / HUMUS (LATIN) / TEKAN (HITTITE) / KEM (TOKHARIAN B) / SEMMIN (OLD PRUSSIAN) / ZEMLJA (OLD CHURCH SLAVIC) ...' — with 'REFERENCES: POKORNY ... BUCK: 16-17 ... SKEAT: (GHEL-, GHEM) 757'. Aryanpur independently cites the same Buck pages 16-17 that Nourai cites as SYN:16.\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"zam\", \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Iranian *dzam- (< PIE *dʰéǵʰōm, with the regular Indo-Iranian palatalisation and the Iranian *ǰʰ > z) is directly attested as Avestan zam- f. 'earth': Bartholomae, Altiranisches Wörterbuch cols. 1662-1664, gives the paradigm 'zam- f. \\\"Erde\\\"; zam (AS.) ... zəmō (GS.) ... zəmi (LS.)' with the two chief senses 'earth as opposed to sky' and 'earth/land as opposed to water'. Sanskrit kṣam- (gen. jmaḥ) and Greek khthōn are the exact cognates. In Old Persian the free word for 'earth' is būmi- (usually written with the ideogram BU); zam- survives only as a bound second member, precisely in the two compounds Nourai draws below it — uzma- < *ud-zma- and Uvārazmi- — so the double label 'Avestan / Old Persian' is defensible for the stem but the OP is compound-only. Nourai's gloss 'earth' is exact.\",\n \"derivation_fa\": \"ستاکِ ایرانیِ باستانِ *dzam- (از هندواروپاییِ آغازینِ *dʰéǵʰōm، با کامی‌شدنِ هندوایرانی و سپس تبدیلِ *ǰʰ به z در ایرانی) در اوستا به‌صورتِ zam- (مؤنث) «زمین» به‌جا مانده است؛ بارتولومه در ستون‌های ۱۶۶۲ تا ۱۶۶۴ صورت‌های صرفیِ zam (رایی)، zəmō (اضافی) و zəmi (دری) را با دو معنای اصلی «زمین در برابر آسمان» و «خشکی در برابر آب» می‌آورد. هم‌ریشه‌های دقیقِ آن سنسکریت kṣam- (اضافی jmaḥ) و یونانی khthōn است. در پارسیِ باستان واژهٔ آزادِ «زمین» būmi- است و zam- تنها در ترکیب می‌آید، همان دو ترکیبی که نورایی زیرِ همین گره کشیده است: uzma- و Uvārazmi-. پس معنا و برچسبِ گره درست است، جز آنکه صورتِ پارسیِ باستان تنها در ترکیب گواهی شده است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/d%CA%B0%C3%A9%C7%B5%CA%B0%C5%8Dm\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 382, s.v. dhghem-: '7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR.' Watkins puts the Iranian zam-/zamin branch under this root, as the arrow requires.\"},\n  {\"ref\": \"BQT:1032\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' ed. Mo'in, the زمین article (BQT_v2_pages.txt leaf 494; the volume's leaf→page offset is +540..+542, so leaf 494 = printed 1032-1034). Mo'in's etymological footnote reads '(مخفف آن: زمی)؛ پهلوی zamīk، اوستا zam- ... بارتولمه [۱۶۶۲] ... و زمین از همین زم است ... با پسوندِ «ین»' — i.e. Avestan zam- > Pahlavi zamīk > NP zamī / zamīn, exactly the arrow #1 → #2.\"},\n  {\"ref\": \"KNT:177\", \"status\": \"supports\",\n   \"note\": \"Kent, Old Persian, Lexicon (KNT.txt \\\\f-leaf 200 of the archive.org 'oldpers' scan, the page that carries Uvārazmi- and uzma-): 'uzma- adj. as sb. \\\"that which is up from the earth, stake\\\": from ud- \\\"up\\\" + zma- to zam- \\\"earth\\\"' and 'Uvārazmi- ... + zmi- ... to zam- \\\"land\\\"'. Kent has no independent zam- headword because OP zam- is attested only in these compounds — which is why one page carries all three of Nourai's KNT:177 citations.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 1662-1664 (BRT.txt line 27690 ff.)\", \"stance\": \"supports\",\n   \"note\": \"'zam- f. \\\"Erde\\\"; 1) als die Stätte alles Materiellen, \\\"Erde, Erdoberfläche, Erdboden, Erdreich\\\"; zam (AS.) ... zəmō (GS.) ... Daher a) oft im Gegensatz zu Himmel und Luftraum ... 2) Im Gegensatz zu Wasser \\\"Erde, Land, Festland\\\"'. Both Buck ('Barth. 1662 ff.') and Nyberg ('Av. (1662 sqq.) zam-') cite the same columns.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §85 and §84 (KNT.txt lines 1128, 1608)\", \"stance\": \"supports\",\n   \"note\": \"'The prefix ud \\\"up\\\" ... suffers complete assimilation of the d in uzma- \\\"stake\\\" (from *ud-zma-)' — the OP stem zma-/zam- is thereby explicitly recognised, although OP writes 'earth' itself as būmiš (§2: the ideogram BU).\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1.21, p.16\", \"stance\": \"supports\",\n   \"note\": \"'Av. zam- (gen. zemo = Skt. jmas) \\\"earth\\\" in all senses (Barth. 1662 ff.)' and, in the word table, 'Av. zam-, būmi-, OPers. būmi-' — Buck lists būmi- and not zam- for Old Persian, which is why the node's OP half is compound-only.\"}\n ]})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"zamîn «زمین»\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian زمین continues Middle Persian zamīg [zmyk'] 'earth' (MacKenzie, Concise Pahlavi Dictionary p.96: 'zamīg [z-, zmyk' | M zmyg, N zamī] earth'; Manichaean MP zmyg), itself from Proto-Iranian *dzam- + the MP -īg suffix. Regular MP → NP loss of final -g gives زمی zamī, still the normal word in Ferdowsi and in Horn's citations (Šāhnāma I.134, I.178 v.877); the current form زمین is that stem enlarged by the adjectival/nominal suffix -īn, exactly as Mo'in states in his footnote to Borhan-e Qate' ('و زمین از همین زم است ... با پسوند ین'), and it had already displaced zamī by the classical period. Nyberg calls zamī 'archaic form for modern zamīn'. The gloss 'earth' is right; the node's only omission is that the immediate ancestor is the Middle Persian form, not Avestan zam- directly.\",\n \"derivation_fa\": \"«زمین» دنبالهٔ فارسیِ میانهٔ zamīg (نوشتهٔ zmyk'، در متونِ مانوی zmyg) است — مکنزی در «فرهنگ کوچکِ پهلوی» ص ۹۶ می‌آورد: «zamīg ... زمین» — و آن خود از ایرانیِ باستانِ *dzam- با پسوندِ -īg ساخته شده است. بنا بر قاعدهٔ آواییِ گذر از فارسیِ میانه به فارسیِ نو، گافِ پایانی می‌افتد و «زمی» به دست می‌آید که هنوز در شاهنامه به کار می‌رود (هرن، شمارهٔ ۶۶۷، با شاهدِ شاهنامه)؛ صورتِ امروزیِ «زمین» همان ستاک با پسوندِ «ـین» است، چنان‌که معین در حاشیهٔ برهان قاطع می‌نویسد: «و زمین از همین زم است ... با پسوندِ ین». نیبرگ نیز «زمی» را صورتِ کهنِ «زمین» می‌خواند. پس ادعای نورایی درست است؛ تنها نکته آنکه واسطهٔ فارسیِ میانه در نمودار نیامده است.\",\n \"sources\": [W + \"%D8%B2%D9%85%DB%8C%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no references of its own; the parent node's BQT:1032 (Mo'in's footnote to زمین) is in fact the reference that covers this arrow, and it supports it.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p.96 s.v. zamīg (PHD.txt line 677; PHD_mackenzie.txt line 5751)\", \"stance\": \"supports\",\n   \"note\": \"'zamīg [z-, zmyk' | M zmyg, N zamī] earth. ~ig [-yk'] terrestrial, earthly. --paymānīh [-pym'nyh] geometry.' The English-Pahlavi half of the book gives 'earth būm, xāk, zamīg'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. damīk (NYB_vol2_glossary.txt line 1175)\", \"stance\": \"supports\",\n   \"note\": \"'damīk [dmyk] earth ... SW form of zamīk (Ps. zmyk), which occurs just as often in MSS and editions. MPrth Prs zmyg, NP zamī, archaic form for modern zamīn; Av. (1662 sqq.) zam-.' Nyberg spells out the whole chain Av. zam- > MP zamīk/zamīg > NP zamī > zamīn.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 667, pp. 148-149 (HRN.txt line 5892)\", \"stance\": \"supports\",\n   \"note\": \"'667. zemī (Šāhn. I, 134 Anm. 4, 178 Vers 877), zemīn \\\"Erde\\\". ap. uzmaya[patiy]; aw. zå \\\"Erde\\\", Gen. zemō; phlv. zamīk; ai. jmā \\\"auf der Erde\\\". ... LW. bal. zamīk \\\"Felder, Saaten\\\"'. Horn groups zamīn with Avestan zam- and with the Old Persian compound of node 11.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 667 (HUB.txt line 2451)\", \"stance\": \"partial\",\n   \"note\": \"'667. Np. zamī aus phl. zamīk = bal. zamīh. Ap. uzmayā-patiy kar \\\"kreuzigen (Bang: pfählen)\\\" gehört schwerlich hierher.' Hübschmann confirms zamī < Pahlavi zamīk but strikes out Horn's Old Persian comparison — see node 11.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, زمین (BQT_v2_pages.txt leaf 494 ≈ printed p.1032-1034)\", \"stance\": \"supports\",\n   \"note\": \"Mo'in's footnote: '... (مخفف آن: زمی)؛ پهلوی zamīk، اوستا zam- ... بارتولمه ... کردی zevî ... افغانی [zmaka] (زمین) ... رك: هوبشمان' — Pahlavi zamīk, Avestan zam-, with Bartholomae and Hübschmann cited by name.\"}\n ]})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"u-vâra-zmi\", \"verdict\": \"plausible\",\n \"derivation\": \"This is Kent's analysis reproduced letter for letter. Kent, Old Persian, Lexicon s.v.: 'Uvārazmi- sb. \\\"Chorasmia\\\", a province of the Persian Empire: Elam. ma-ra-iš-mi-iš, Akk. hu-ma-ri-iz-ma-\\\\', Gk. Khōrasmiē, Av. asf. x'āirizəm. From u- \\\"good\\\" + vāra- \\\"?\\\" (§126, §148.III), + zmi- (§95, §120, §152) to zam- \\\"land\\\".' Nourai's segmentation u-vāra-zmi, his gloss 'good ... land' with the ellipsis, and even his NOTE 'the meaning of \\\"vāra\\\" is not clear' are Kent's question mark rendered into words — so as a report of the cited source the node is exact. It is marked plausible rather than confirmed because Kent's is only one of several current analyses of the name and not the favoured one: the first element is more usually taken as *hwar-/xwar- either 'sun' (Bosworth: 'the land from which the sun rises') or *xwār- 'low' ('the lowland', Khwarazm being the lowest part of Central Asia), and Yaqut already offered a folk etymology xwār 'food' + razm. What is not in doubt is the second element -zmi- < zam- 'earth, land', which is the only part the arrow from the root actually needs. One label correction: Uvārazmi- is Old Persian (DB 1.16, DPe, DNa, DSe, DSm, XPh); the Avestan counterpart is a different form, x'āirizəm.\",\n \"derivation_fa\": \"این گره واژه‌به‌واژه تحلیلِ کنت است. کنت در واژه‌نامهٔ «پارسی باستان» ذیلِ Uvārazmi- «خوارزم، ساتراپی‌ای از شاهنشاهی هخامنشی» می‌نویسد: «از u- (خوب) + vāra- (؟) + zmi- که به zam- «زمین» بازمی‌گردد»، و صورت‌های ایلامی، اکدی، یونانی (Khōrasmiē) و اوستایی (x'āirizəm) را نیز می‌آورد. بخش‌بندیِ نورایی، معنای «سرزمینِ خوب…» با نقطه‌چین، و حتی یادداشتِ «معنای vāra روشن نیست» همان علامتِ پرسشِ کنت است که به جمله درآمده؛ پس گره در گزارشِ مأخذ کاملاً امین است. اما «با احتیاط پذیرفتنی» است، زیرا تحلیلِ کنت تنها یکی از تحلیل‌های موجود است و امروز رایج‌تر آن است که جزءِ نخست را *xwar- «خورشید» (بازورث: «سرزمینی که خورشید از آن برمی‌آید») یا *xwār- «پست، فرود» («سرزمینِ پست») بگیرند؛ یاقوت نیز ریشه‌شناسیِ عامیانهٔ «خوار (خوراک) + رزم» را آورده است. آنچه مورد اختلاف نیست جزءِ دومِ -zmi- از zam- «زمین» است و همین برای درستیِ پیکانِ نمودار بس است. یک نکتهٔ برچسبی: Uvārazmi- پارسیِ باستان است نه اوستایی؛ برابرِ اوستایی‌اش x'āirizəm است.\",\n \"sources\": [\"https://en.wikipedia.org/wiki/Khwarazm\"],\n \"ref_check\": [\n  {\"ref\": \"KNT:177\", \"status\": \"supports\",\n   \"note\": \"Kent, Lexicon, the page carrying Uvāmarsiyuš / Uvārazmi- / Uvārazmiya- / uvarštika- / uškahyā / ušhamaranakara- / uzma- (KNT.txt \\\\f-leaf 200 of archive.org 'oldpers'; the Lexicon opens at leaf 193 = printed p.164, so this leaf is printed p.177, and the same page carries all three of Nourai's KNT:177 citations — nodes 1, 3 and 11). Quote: 'From u- \\\"good\\\" + vāra- \\\"?\\\" ... + zmi- ... to zam- \\\"land\\\".' The '?' is exactly Nourai's NOTE.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW (BRT.txt, greps for 'airizem', 'xvairizem', 'arizem')\", \"stance\": \"silent\",\n   \"note\": \"The Avestan Chorasmia name could not be located in the OCR of the Altiranisches Wörterbuch (the diacritic-heavy x'āirizəm defeats the scan); the AiW is however the source Kent quotes for the Avestan accusative form.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, §179.1, DNa 23, DSe 22, DSm 9, XPh 21f, DB 1.16, DPe 16f (KNT.txt lines 2132, 2143, 4214, 4576, 4719)\", \"stance\": \"supports\",\n   \"note\": \"'The only survival of separate declensional forms is nom. Uvarazmiy, with original -ī, replaced in later inscriptions by Uvārazmiš' — the name is solidly Old Persian and inscriptionally attested, e.g. DSe 22 'Suguda : Uvarazmiš'.\"},\n  {\"src\": \"web\", \"where\": \"Wikipedia, Khwarazm, section Etymology\", \"stance\": \"partial\",\n   \"note\": \"Lists Bosworth's *xwar 'sun' + *zam 'land' ('the land from which the sun rises'), the 'lowland' analysis (*xwār 'low' + zam), and Yaqut's xwār 'food' + razm — i.e. the second element zam- is common ground, the first is disputed and Kent's u- 'good' is not the modern favourite.\"}\n ]})\n\nN.append({\n \"id\": 4, \"lang\": \"Avestan / Old Persian\", \"words\": \"huvârazmîš, xvarazmîš, xvârizem\", \"verdict\": \"plausible\",\n \"derivation\": \"The three forms are real and are Kent's: 'huvârazmîš' is the Old Persian nominative Uvārazmiš (DNa 23, DSe 22, DSm 9, XPh 21f; the earlier nominative Uvārazmiy stands at DB 1.16 and DPe 16f), Nourai writing the initial u- as hu- because he takes it as the prefix hu- 'good'; 'xvarazmîš' is the same name with the later Iranian xʷ- development that yields MP/NP Xwārazm; 'xvârizem' is Kent's Avestan accusative x'āirizəm. The forms are therefore sound. What is not sound is the gloss. (a) Uvārazmiš in the inscriptions is a dahyu-, a province/country in the satrapy lists (Bactria, Sogdia, Chorasmia, Drangiana...), not 'an ancient city'. (b) The identification with Airyanəm Vaēǰah, the Avestan homeland of Vd. 1.1, is a nineteenth/twentieth-century hypothesis (Markwart; in Persian scholarship Dehkhoda, who calls Khwarazm 'the cradle of the Aryan tribe'; Elton Daniel still calls it 'the most likely locale'), and it is contested — Witzel places Airyanəm Vaēǰah in the Afghan highlands. (c) 'Now it is known as Khiva' repeats Klein's and Lokotsch's nineteenth-century shorthand, in which the whole region was named after the Khanate of Khiva; the historical Khwarazm oasis is much larger than the town of Khiva, and its old capitals were Kāth and Gurgānj (Urgench).\",\n \"derivation_fa\": \"هر سه صورت واقعی‌اند و از کنت گرفته شده‌اند: «huvârazmîš» همان صورتِ فاعلیِ پارسیِ باستان Uvārazmiš است (کتیبه‌های DNa ۲۳، DSe ۲۲، DSm ۹، XPh ۲۱؛ صورتِ کهن‌ترِ Uvārazmiy در DB ۱٫۱۶ و DPe)، و نورایی «u» آغازین را «hu» می‌نویسد چون آن را پیشوندِ hu- «خوب» می‌گیرد؛ «xvarazmîš» همان نام با تحولِ xʷ- ایرانی است که در فارسیِ میانه و نو «خوارزم» می‌شود؛ «xvârizem» صورتِ اوستاییِ x'āirizəm است که کنت آورده. اما معنایی که در جعبه آمده سه اشکال دارد: نخست آنکه Uvārazmiš در کتیبه‌ها نامِ یک «دهیو» (ساتراپی/سرزمین) در فهرستِ کشورهاست، نه نامِ یک شهر؛ دوم آنکه یکی‌گرفتنِ آن با «ائیریانَه‌وَئِجَه» فرضیه‌ای است (مارکوارت، و در ایران دهخدا که خوارزم را «مهدِ نژادِ آریایی» می‌خواند) که همگانی نیست و ویتسل آن را در افغانستان می‌نهد؛ سوم آنکه «امروز خیوه خوانده می‌شود» بازگفتِ تعبیرِ سدهٔ نوزدهمیِ کلاین و لوکوچ است که سراسرِ سرزمین را به نامِ خانِ‌نشینِ خیوه می‌خواندند، حال آنکه واحهٔ تاریخیِ خوارزم بسیار بزرگ‌تر از شهرِ خیوه بوده و پایتخت‌های کهنش کاث و گرگانج (اورگنج) بوده است.\",\n \"sources\": [\"https://en.wikipedia.org/wiki/Khwarazm\", \"https://abadis.ir/fatofa/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85/\"],\n \"ref_check\": [\n  {\"ref\": \"BQT:22(Introduction)\", \"status\": \"supports\",\n   \"note\": \"The pointer is real and is Mo'in's own: at the foot of the خوارزم article (BQT_v2_pages.txt leaf 239) footnote 6 reads 'خوارزمی: منسوب به خوارزم؛ بزبان خوارزم رك: ص بست و دو مقدمه' — 'Khwarazmi: belonging to Khwarazm; on the language of Khwarazm see p. twenty-two of the Introduction'. Nourai's odd citation form 'BQT:22(Introduction),781' is simply this footnote copied out.\"},\n  {\"ref\": \"BQT:781\", \"status\": \"partial\",\n   \"note\": \"The خوارزم article stands on that page (BQT_v2_pages.txt leaf 239, printed 781 by the footnote-6 cross-reference): 'خوارزم: نام شهری است معروف و مشهور از ترکستان' — 'the name of a famous city of Turkestan'. So Borhan does call it a city, which is where Nourai's 'city' comes from; but Borhan says nothing about Airyanem Vaejo or about Khiva at this entry, and calls it Turkestan, not the Aryan homeland.\"},\n  {\"ref\": \"MON5:488\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in's Farhang-e Farsi vols 5-6 are the a'lam (proper-name) volumes; they are not on archive.org and vajehyab/abadis serve only the lexicon volumes, so p.488 of vol. 5 could not be read. abadis.ir's Dehkhoda entry for خوارزم gives compatible content (Khwarazm on the lower Oxus, 'historically home to the Aryan people', modern Khiva, split between Uzbekistan and Turkmenistan) — i.e. Nourai's gloss reproduces the standard Persian encyclopaedic article.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. Uvārazmi- and text DSe 22 (KNT.txt leaf 200, line 4214)\", \"stance\": \"partial\",\n   \"note\": \"'Uvārazmi- sb. \\\"Chorasmia\\\", a province of the Persian Empire ... Gk. Khōrasmiē, Av. asf. x'āirizəm.' Kent's 'province' contradicts Nourai's 'city'; the DSe satrapy list runs 'Baxtriš : Suguda : Uvarazmiš : Zranka : Haraiva...', which is a list of countries.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890 (LKT.txt line 2144)\", \"stance\": \"supports\",\n   \"note\": \"'Hwārizm, Npr., eine Landschaft in Mittelasien [dem heutigen Chanate Chiva-Hīwa entsprechend]' — 'a region in Central Asia, corresponding to the present khanate of Khiva'. Lokotsch is a 'Landschaft' (region), and shows exactly where the 'now Khiva' equation comes from.\"},\n  {\"src\": \"web\", \"where\": \"Wikipedia, Khwarazm, Airyanem Vaejah section\", \"stance\": \"partial\",\n   \"note\": \"'Supporters: Elton L. Daniel considers Khwarazm the most likely locale for the original Avestan homeland; Dehkhoda calls it the cradle of the Aryan tribe. Skeptics: Michael Witzel argues Airyanem Vaejah was in Afghanistan instead.' A live scholarly dispute, not a settled fact as the box implies.\"}\n ]})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"Xârazm, Khârazm «خوارزم»; Xârazmî «خوارزمی»; Xîveh, Xîvaq «خیوه ۱، خیوق»\", \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three are straightforward. خوارزم is the regular New Persian continuant of Old Persian Uvārazmiš / Middle Persian Xwārazm: OP initial u- of the compound, once it was no longer felt as hu- 'good', was refashioned as the labialised xʷ- that Persian writes خو-, and the -iš nominative ending was lost with the collapse of OP nominal inflection; the modern spelling خوارزم has the silent wāw of xʷ- (as in خواهر, خواندن). خوارزمی is the Persian nisba in -ī 'of Khwarazm', used both of the language (Mo'in's footnote 6 in Borhan sends the reader to p.22 of his Introduction 'on the language of Khwarazm') and as the surname of Abū Jaʿfar Muḥammad b. Mūsā, whose Kitāb al-jabr wa'l-muqābala is correctly described in the node's NOTE. The third word is the weak link: خیوه / خیوق (Khiva, Khīvaq) is a distinct toponym of unknown origin — one theory does take it from Khwārazm through a Turkic intermediate Khīvarezem, and the local legend derives it from the well Kheyvak dug by Shem — and Borhan itself keeps them apart, treating خیوق as a place within the Khwarazm territory ('خیوق: نام ولایتی ... اولکای خوارزم') with a cross-reference 'خیوه: رك: خیوق'. Drawing خیوه as simply equal to خوارزم repeats Klein's and Lokotsch's nineteenth-century shorthand (Khwarazm = the khanate of Khiva) rather than an etymological derivation, hence plausible, not confirmed. The Hāfez line quoted in the box ('دانی کجاست جای تو خوارزم یا خجند') is genuine and merely illustrates the name.\",\n \"derivation_fa\": \"دو واژه از سه واژهٔ این گره بی‌اشکال است. «خوارزم» دنبالهٔ منظمِ Uvārazmiš پارسیِ باستان و Xwārazm فارسیِ میانه است: چون u- آغازین دیگر پیشوندِ hu- «خوب» احساس نمی‌شد، به همان xʷ- لبی‌شده بدل شد که در فارسی «خوـ» نوشته می‌شود (مانندِ خواهر و خواندن با واوِ معدوله)، و پایانهٔ فاعلیِ -iš با از میان رفتنِ صرفِ اسم در فارسیِ میانه افتاد. «خوارزمی» صفتِ نسبیِ فارسی است، هم برای زبانِ خوارزمی و هم لقبِ ابوجعفر محمد بن موسی که یادداشتِ جعبه دربارهٔ «الجبر و المقابله»اش درست است؛ معین نیز در حاشیهٔ برهان (پانوشتِ ۶ ذیلِ خوارزم) خواننده را برای زبانِ خوارزمی به صفحهٔ «بیست و دو»ی مقدمه ارجاع می‌دهد. اما «خیوه / خیوق» جای‌نامی جداگانه با خاستگاهِ نامعلوم است؛ یک نظر آن را از راهِ ترکیِ Khīvarezem به خوارزم می‌رساند و افسانهٔ محلی آن را به چاهِ «خیوک» بازمی‌گرداند. خودِ برهان قاطع این دو را یکی نمی‌گیرد و خیوق را «نام ولایتی ... [از] اولکای خوارزم» می‌خواند و می‌نویسد «خیوه: رك: خیوق». پس یکی‌گرفتنِ خیوه با خوارزم بازگفتِ تعبیرِ کلاین و لوکوچ (خوارزم = خانِ‌نشینِ خیوه) است نه اشتقاقِ زبانی؛ از این رو داوری «با احتیاط پذیرفتنی» است.\",\n \"sources\": [\"https://en.wikipedia.org/wiki/Khiva\", \"https://abadis.ir/fatofa/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85/\"],\n \"ref_check\": [\n  {\"ref\": \"BQT:781\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 239 (printed 781): 'خوارزم: نام شهری است معروف و مشهور از ترکستان' with Mo'in's footnote 6 'خوارزمی: منسوب به خوارزم؛ بزبان خوارزم رك: ص بست و دو مقدمه'. Covers both خوارزم and خوارزمی.\"},\n  {\"ref\": \"BQT:805\", \"status\": \"partial\",\n   \"note\": \"BQT_v2_pages.txt leaf 265 (printed 805): 'خیوق: بکسر اول بروزن زیبق. نام ولایتی ... اولکای خوارزم' followed by 'خیوه: رك: خیوق', with Mo'in's footnote 'xiwaq «دائرة المعارف اسلام، ج ۲ ص ۳۹۹ ستون ۱»'. Borhan therefore places Khīvaq inside the Khwarazm territory and gives a separate Encyclopaedia-of-Islam reference for it — it does not say that Khiva IS Khwarazm or that the name derives from it.\"},\n  {\"ref\": \"MON5:488,491\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in vols 5-6 (a'lam) are not online; pp.488 and 491 could not be read. The parallel abadis/Dehkhoda article for خوارزم is compatible with the box.\"},\n  {\"ref\": \"KLN:49\", \"status\": \"supports\",\n   \"note\": \"Klein, s.v. algorism (KLN_1966.txt line 2189, \\\\f-leaf 37, i.e. printed pp.50-51 by the two-pages-per-leaf offset, within ±2 of Nourai's 49): '... from the inexact transliteration of Arab. al-Khowarizmi, \\\"the man of Khowarizm (the modern Khiva)\\\", surname of Abu Jafar Mohammed ibn Musa, great mathematician of the 9th cent. His famous work Al-jabr w'al muqabalah (\\\"Reunion and comparison\\\") introduced the use of Arabic numerals in Europe...' — Nourai's NOTE is a paraphrase of this sentence, and 'the modern Khiva' is where his Xiveh equation comes from.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890 (LKT.txt line 2144)\", \"stance\": \"supports\",\n   \"note\": \"'davon das ar. Adj. hwārizmī od. hārizmī \\\"aus Hwārizm stammend, der Chwarizmier\\\", Beiname des Mathematikers ABŪ ĞAʿFAR MUHAMMAD IBN MŪSĀ' — the Persian toponym, the Arabic nisba and the mathematician, in Nourai's order.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, خیوق / خیوه (leaf 265, printed p.805)\", \"stance\": \"partial\",\n   \"note\": \"See ref_check: خیوه is only a cross-reference to خیوق, and خیوق is a district, with its own Encyclopaedia of Islam citation.\"},\n  {\"src\": \"web\", \"where\": \"Wikipedia, Khiva, Etymology\", \"stance\": \"partial\",\n   \"note\": \"'the origin of Khiva's name is unknown', though 'one theory suggests the name comes from the Persian word Khwarezm, altered by borrowing into Turkic as Khivarezem, then shortened to Khiva'; the rival account is the legend of the well Kheyvak dug by Shem.\"}\n ]})\n\nN.append({\n \"id\": 6, \"lang\": \"Arabic\", \"words\": \"Al-Xwârazmî\", \"verdict\": \"confirmed\",\n \"derivation\": \"الخوارزمي is the ordinary Arabic nisba: the Persian toponym خوارزم with the Arabic relative-adjective suffix -ī and the article al-, 'the man from Khwarazm'. It is the by-name of Abū Jaʿfar Muḥammad ibn Mūsā (fl. c.820), an astronomer and mathematician of the Bayt al-Ḥikma in Baghdad under al-Maʾmūn, whose Kitāb al-jabr wa'l-muqābala gave Europe the word algebra and whose arithmetic (surviving only in the Latin Liber Algorismi de numero Indorum) gave it the decimal place-value system and, from his name, algorism. The node is a personal name, not a common noun, so the 'Arabic' label means only that the nisba is formed by Arabic morphology on a Persian base — the derivation from node 5 is exact.\",\n \"derivation_fa\": \"«الخوارزمی» نسبتِ عربیِ معمول است: جای‌نامِ فارسیِ «خوارزم» با یایِ نسبتِ عربی و حرفِ تعریفِ «ال»، یعنی «مردِ خوارزمی». این لقبِ ابوجعفر محمد بن موسی (شکوفاییِ حدودِ ۲۰۵ هجری / ۸۲۰ میلادی) است، ریاضی‌دان و اخترشناسِ بیت‌الحکمهٔ بغداد در روزگارِ مأمون، که «کتاب الجبر و المقابله»اش واژهٔ algebra را به اروپا داد و حسابِ هندیِ او — که تنها در ترجمهٔ لاتینِ Liber Algorismi de numero Indorum مانده است — دستگاهِ ارقامِ اعشاری و، از نامِ خودِ او، واژهٔ algorism را. این گره نامِ خاص است نه اسمِ عام، و برچسبِ «عربی» تنها به معنای آن است که ساختِ نسبت عربی است بر پایه‌ای فارسی؛ پیکانِ آن از گرهٔ ۵ کاملاً درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/algorithm\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no reference of its own; the KLN:49 cited on the flanking nodes covers it — Klein explicitly writes 'Arab. al-Khowarizmi, \\\"the man of Khowarizm\\\"'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. algorism (KLN_1966.txt line 2189 ≈ printed p.49-51)\", \"stance\": \"supports\",\n   \"note\": \"'from the inexact transliteration of Arab. al-Khowarizmi, \\\"the man of Khowarizm (the modern Khiva)\\\", surname of Abu Jafar Mohammed ibn Musa, great mathematician of the 9th cent.'\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890\", \"stance\": \"supports\",\n   \"note\": \"'davon das ar. Adj. hwārizmī ... \\\"aus Hwārizm stammend\\\", Beiname des Mathematikers ABŪ ĞAʿFAR MUHAMMAD IBN MŪSĀ [s. hier Nr. 631]' — Lokotsch's no. 631 is algebra, the companion loan.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Muʿarraba (grep 'خوارزم' in AFM.txt and TAD.txt)\", \"stance\": \"silent\",\n   \"note\": \"Neither Addi Shir nor al-Unaysi lists خوارزم — expected, since they collect Persian common nouns arabicised, not proper names.\"}\n ]})\n\nN.append({\n \"id\": 7, \"lang\": \"Middle Latin\", \"words\": \"algorismus\", \"verdict\": \"confirmed\",\n \"derivation\": \"Medieval Latin algorismus arose in the twelfth-century Toledo translation movement: the Latin version of al-Khwārizmī's lost arithmetic circulates as Liber Algorismi de numero Indorum / Dixit Algorizmi, where the author's nisba is transliterated as the book's name and then taken as the name of the method. Klein calls it 'the inexact transliteration of Arab. al-Khowarizmi'; the -ismus ending was helped along by the familiar Latin/Greek noun suffix, and the variant algorithmus appears beside it under the pull of Greek arithmos 'number' (Lokotsch 890 states this explicitly: 'daher wurde lat. algorithmus, algorismus [mit Anlehnung an gr. ἀριθμός] die Bezeichnung für das Rechnen mit ar. Ziffern'). The gloss 'the Arabic system of numerals' is Klein's own wording.\",\n \"derivation_fa\": \"«algorismus» در لاتینِ میانه زادهٔ نهضتِ ترجمهٔ سدهٔ دوازدهم در تولدو است: ترجمهٔ لاتینِ حسابِ گم‌شدهٔ خوارزمی با نامِ Liber Algorismi de numero Indorum («کتابِ الخوارزمی دربارهٔ شمارِ هندیان») و آغازهٔ Dixit Algorizmi می‌گشت، و نسبتِ نویسنده نخست نامِ کتاب و سپس نامِ خودِ روشِ محاسبه شد. کلاین آن را «آوانگاریِ نادقیقِ al-Khowarizmi عربی» می‌خواند؛ پایانهٔ -ismus به قیاسِ پسوندِ آشنای لاتینی‌ـ‌یونانی نشست و گونهٔ algorithmus نیز به کششِ واژهٔ یونانیِ arithmos «شمار» در کنارِ آن پدید آمد — لوکوچ (شمارهٔ ۸۹۰) این را صریح می‌گوید: «از این رو algorithmus و algorismus لاتینی، با تکیه بر ἀριθμός یونانی، نامِ حساب کردن با ارقامِ عربی شد». معنایی هم که در جعبه آمده («دستگاهِ ارقامِ عربی») عینِ عبارتِ کلاین است.\",\n \"sources\": [\"https://www.etymonline.com/word/algorithm\", \"https://ahdictionary.com/word/search.html?q=algorithm\"],\n \"ref_check\": [\n  {\"ref\": \"AHD:33\", \"status\": \"supports\",\n   \"note\": \"Not checkable in the local file (only Watkins' roots appendix is on disk), but the AHD entry itself, read online at ahdictionary.com/word/search.html?q=algorithm, gives 'algorithm: variant of algorism, probably influenced by arithmetic or Greek arithmos \\\"number\\\"', with the note 'Algorism, the English word for computation with Arabic numerals, is derived from Al-Khwarizmi's name'. p.33 is where 'algorism/algorithm' falls in the A-section of the New College Edition.\"},\n  {\"ref\": \"KLN:49\", \"status\": \"supports\",\n   \"note\": \"'algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus, from the inexact transliteration of Arab. al-Khowarizmi' (KLN_1966.txt line 2189). Klein's gloss is verbatim Nourai's gloss.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890 (LKT.txt line 2144)\", \"stance\": \"supports\",\n   \"note\": \"'durch sein Werk über Algebra kam das dekadische Zahlensystem und das Rechnen mit ar. Zahlen um das Jahr 1200 nach Europa; daher wurde lat. algorithmus, algorismus [mit Anlehnung an gr. ἀριθμός] die Bezeichnung für das Rechnen mit ar. Ziffern'; the index lists 'algorismus 890, algorithmus 890'.\"},\n  {\"src\": \"web\", \"where\": \"Etymonline s.v. algorithm/algorism\", \"stance\": \"supports\",\n   \"note\": \"'The Medieval Latin algorismus traces back to Arabic al-Khwarizmi, meaning \\\"native of Khwarazm\\\"'; algorism in English 'early 13c. ... came directly from Old French, deriving from the same Medieval Latin algorismus'.\"}\n ]})\n\nN.append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"algorisme, algorithme\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old French algorisme is attested from the thirteenth century (Alexandre de Villedieu's verse Carmen de algorismo and Sacrobosco's Algorismus made it a school word), taken straight from Medieval Latin algorismus. The modern French algorithme is a learned refashioning of that older algorisme under a false association with Greek arithmos 'number' — the -th- has no Arabic or Latin warrant at all, which is why Klein sets it in parentheses beside the older form ('OF. algorisme (F. algorithme)') and why Lokotsch says 'afrz. algorisme, frz. algorithme'. Both French forms are therefore correctly placed, and both feed the English node below.\",\n \"derivation_fa\": \"صورتِ فرانسویِ کهنِ algorisme از سدهٔ سیزدهم میلادی گواهی شده است (منظومهٔ Carmen de algorismo از الکساندر دو ویل‌دیو و Algorismus ساکروبوسکو آن را واژه‌ای مدرسی کردند) و یکراست از algorismus لاتینِ میانه گرفته شده. صورتِ امروزیِ algorithme بازساختی عالمانه از همان algorisme است بر پایهٔ پیوندی نادرست با arithmos یونانی «شمار»؛ آن «th» نه پشتوانهٔ عربی دارد نه لاتینی. به همین سبب کلاین صورتِ نو را در کمانک کنارِ صورتِ کهن می‌گذارد («OF. algorisme (F. algorithme)») و لوکوچ می‌نویسد «afrz. algorisme, frz. algorithme». پس هر دو صورتِ فرانسوی در جای درستِ خود نشسته‌اند.\",\n \"sources\": [\"https://www.etymonline.com/word/algorithm\"],\n \"ref_check\": [\n  {\"ref\": \"AHD:33\", \"status\": \"supports\",\n   \"note\": \"The AHD entry read online derives algorithm as 'variant of algorism, probably influenced by arithmetic or Greek arithmos', which is the same refashioning; the French link is spelled out by Etymonline ('from French algorithme, refashioned ... from Old French algorisme') and by Klein and Lokotsch. AHD p.33 itself could not be read (local copy = Watkins appendix only).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. algorism (printed p.49-51)\", \"stance\": \"supports\",\n   \"note\": \"'ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus'.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890\", \"stance\": \"supports\",\n   \"note\": \"'Hieraus afrz. algorisme, frz. algorithme, it. alguarismo \\\"Rechenart, Arithmetik\\\", sp. alguarismo, guarismo \\\"Ziffer\\\", engl. algorism, algorithm \\\"Rechenart\\\".'\"},\n  {\"src\": \"web\", \"where\": \"Etymonline s.v. algorithm\", \"stance\": \"supports\",\n   \"note\": \"'from French algorithme, refashioned (under mistaken connection with Greek arithmos \\\"number\\\") from Old French algorisme \\\"the Arabic numeral system\\\" (13c.)'.\"}\n ]})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"âlgoritm «آلگوریتم»\", \"verdict\": \"confirmed\",\n \"derivation\": \"A twentieth-century European loan back into Persian, and thus the closing of a full circle: a Khwarazmian toponym → an Arabic nisba → Medieval Latin → French → modern Persian. The donor is French algorithme (Persian technical vocabulary of the Reza Shah and post-war period came overwhelmingly through French), which explains the final -tm cluster of آلگوریتم rather than an English -thm pronounced /ðəm/. Nourai's spelling with alef-madda, آلگوریتم, renders the French [al-] with a long ā; the spelling now standard in Persian mathematics and computing is الگوریتم (and the Academy's Persian equivalent is خوارزمی or خوارزمیک — a deliberate restoration of the original name). The gloss 'a type of computational procedure' is right for the modern sense. Verdict confirmed for the fact and route of the borrowing; the only unverifiable point is Nourai's source, Moshiri's Farhang-e vazheha-ye Orupayi dar Farsi p.17, of which no copy could be found.\",\n \"derivation_fa\": \"این گره وام‌واژه‌ای اروپایی در فارسیِ سدهٔ چهاردهمِ خورشیدی است و دایره را می‌بندد: جای‌نامی خوارزمی ← نسبتِ عربی ← لاتینِ میانه ← فرانسه ← بازگشت به فارسی. وام‌دهنده به احتمالِ بسیار algorithme فرانسوی است، زیرا واژگانِ فنّیِ فارسی در آن دوره عمدتاً از راهِ فرانسه آمده‌اند و خوشهٔ پایانیِ «ـتم» نیز همان را نشان می‌دهد نه تلفظِ انگلیسیِ /ðəm/ را. املای نورایی با الفِ ممدود («آلگوریتم») برابرنهادِ [al-] فرانسوی با آی کشیده است؛ املای رایجِ امروز در ریاضی و رایانه «الگوریتم» است و فرهنگستان برابرِ فارسیِ «خوارزمی/خوارزمیک» را نهاده که در حقیقت بازگرداندنِ همان نامِ اصلی است. معنای «روشِ محاسبه» درست است. تنها نکتهٔ بررسی‌ناپذیر مأخذِ نورایی است: «فرهنگ واژه‌های اروپایی در فارسی» مهشید مشیری، ص ۱۷، که هیچ نسخه‌ای از آن یافت نشد.\",\n \"sources\": [\"https://www.etymonline.com/word/algorithm\"],\n \"ref_check\": [\n  {\"ref\": \"VOP:17\", \"status\": \"not_checked\",\n   \"note\": \"VOP = Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371/1992). refs_online.json records kind 'none': re-searched archive.org, ketabnak, noorlib and the open web — no scan and no catalogue record with a copy; the near-title hits (Zomorrodian, ketabnak 132354) are a different book. Not accessible.\"}\n ],\n \"consulted\": [\n  {\"src\": \"web\", \"where\": \"Etymonline s.v. algorithm\", \"stance\": \"supports\",\n   \"note\": \"'From the mid-twentieth century onward, it became particularly associated with computing processes' — the sense in which modern Persian borrowed it; the French form algorithme is the one whose shape matches آلگوریتم/الگوریتم.\"},\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi vol. 4 (foreign compounds), searched via vajehyab/abadis\", \"stance\": \"silent\",\n   \"note\": \"Mo'in's dictionary was compiled before the word entered general Persian use; no entry الگوریتم / آلگوریتم is served by vajehyab or abadis.\"}\n ]})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"algorism, algorithm\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle English algorisme appears early in the thirteenth century, borrowed from Old French algorisme and denoting reckoning with the nine Arabic figures and the zero (as against reckoning on the abacus, 'augrim' in Chaucer). Modern algorithm is a separate, later entry, 1690s, from the refashioned French algorithme, and only in the mid twentieth century did it settle on its present sense 'a finite, effective computational procedure' under the influence of computing and of Church-Turing style definitions. Both English words therefore descend from the French node exactly as drawn; Klein sets them out in one line and Lokotsch's list ends 'engl. algorism, algorithm \\\"Rechenart\\\"'.\",\n \"derivation_fa\": \"«algorisme» در انگلیسیِ میانه از آغازِ سدهٔ سیزدهم دیده می‌شود، وام‌گرفته از algorisme فرانسویِ کهن، به معنای حساب کردن با نُه رقمِ عربی و صفر، در برابرِ حسابِ چرتکه‌ای (که چاسر آن را augrim می‌نامد). صورتِ امروزیِ algorithm ورودی‌ای جداگانه و دیرتر است — از دههٔ ۱۶۹۰ میلادی — از algorithme فرانسویِ بازساخته، و تنها از میانهٔ سدهٔ بیستم است که معنای امروزینِ «رَویّهٔ محاسباتیِ متناهی و کارآمد» را زیرِ تأثیرِ رایانه و تعریف‌های چرچ و تورینگ یافت. پس هر دو واژهٔ انگلیسی درست از گرهٔ فرانسوی می‌آیند؛ کلاین هر دو را در یک سطر می‌آورد و فهرستِ لوکوچ نیز با «engl. algorism, algorithm» پایان می‌گیرد.\",\n \"sources\": [\"https://www.etymonline.com/word/algorithm\"],\n \"ref_check\": [\n  {\"ref\": \"KLN:49\", \"status\": \"supports\",\n   \"note\": \"'algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus...' (KLN_1966.txt line 2189, \\\\f-leaf 37 ≈ printed pp.50-51, within the ±2 tolerance of the leaf formula for Nourai's p.49).\"}\n ],\n \"consulted\": [\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary (grep 'algorism')\", \"stance\": \"silent\",\n   \"note\": \"The concise Skeat on disk has no algorism/algorithm headword.\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890\", \"stance\": \"supports\",\n   \"note\": \"'engl. algorism, algorithm \\\"Rechenart\\\"', at the end of the Romance/Germanic descendant list.\"},\n  {\"src\": \"web\", \"where\": \"Etymonline s.v. algorithm and algorism\", \"stance\": \"supports\",\n   \"note\": \"'Algorithm (1690s) ... from French algorithme'; 'Algorism (early 13c.) The earlier Middle English form algorism came directly from Old French.'\"}\n ]})\n\nN.append({\n \"id\": 11, \"lang\": \"Old Persian\", \"words\": \"ud-zma, uzma\", \"verdict\": \"plausible\",\n \"derivation\": \"Kent's lexicon has exactly this: 'uzma- adj. as sb. \\\"that which is up from the earth, stake\\\": from ud- \\\"up\\\" + zma- to zam- \\\"earth\\\"', with the phonology stated at §84-85 — the prefix ud 'up' (Av. us-/uz-, Skt. ud, PIE *ud) assimilates its d completely before the following z, giving uz-, and the resulting long cluster is shortened. The word is attested only in the locative compound uzmayā-patiy, in Darius' formula for impaling rebels: DB 2.76 'pasāva-šim Hagmatānaiy uzmayāpatiy akunavam' — 'afterwards I put him on the stake at Ecbatana' (also DB 2.91, 3.52, 3.92). Nourai's gloss 'grown up from ground' is Kent's 'that which is up from the earth' with the actual referent — the impaling stake — silently dropped, which makes the box read as though it were a word for a plant. The verdict is plausible rather than confirmed because the etymology is not unanimous: Hübschmann, Persische Studien no. 667, expressly rejects it ('Ap. uzmayā-patiy kar \\\"kreuzigen (Bang: pfählen)\\\" gehört schwerlich hierher'), against Horn who had put it under zamīn, and Kent himself flags dissent ('otherwise Wackernagel KZ 61.208; Lommel OLZ 37.180 n.2; König RuID 72'). Kent's *ud-zma- is nevertheless the standard analysis today.\",\n \"derivation_fa\": \"واژه‌نامهٔ کنت درست همین را می‌آورد: «uzma-، صفتِ اسم‌شده، «آنچه از زمین برآمده، چوبهٔ دار»: از ud- «بالا» + zma- که به zam- «زمین» بازمی‌گردد»، و قاعدهٔ آوایی را نیز در بندهای ۸۴ و ۸۵ می‌گوید: پیشوندِ ud «بالا» (اوستایی us-/uz-، سنسکریت ud، هندواروپایی *ud) دالِ خود را پیشِ z یکسره همگون می‌کند و uz- می‌شود و خوشهٔ کشیدهٔ حاصل کوتاه می‌گردد. این واژه تنها در ترکیبِ درِ حالتِ دری uzmayā-patiy گواهی شده است، در فرمولِ داریوش برای بر دار کردنِ شورشیان: بیستون ۲٫۷۶ «pasāva-šim Hagmatānaiy uzmayāpatiy akunavam» یعنی «سپس او را در هگمتانه بر دار کردم» (و نیز ۲٫۹۱، ۳٫۵۲، ۳٫۹۲). معنایی که نورایی داده («برآمده از زمین») همان عبارتِ کنت است اما مرجعِ واقعیِ آن، یعنی «چوبهٔ دار»، افتاده است و جعبه چنان خوانده می‌شود که گویی نامِ گیاهی است. داوری «با احتیاط پذیرفتنی» است چون این ریشه‌شناسی همگانی نیست: هوبشمان در «پژوهش‌های فارسی» شمارهٔ ۶۶۷ آن را صریح رد می‌کند و می‌نویسد این ترکیب «به‌سختی به اینجا تعلق دارد»، در برابرِ هرن که آن را ذیلِ «زمین» آورده بود؛ کنت نیز نظرهای مخالف (واکرناگل، لومل، کونیگ) را یاد می‌کند. با این همه تحلیلِ کنت امروز تحلیلِ متعارف است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"KNT:177\", \"status\": \"supports\",\n   \"note\": \"KNT.txt \\\\f-leaf 200 (= printed p.177, the same page as Uvārazmi-): 'uzma- adj. as sb. \\\"that which is up from the earth, stake\\\": from ud- \\\"up\\\" + zma- to zam- \\\"earth\\\" (§84, §95, §120, §130, §142, §148.II, VI): otherwise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent §85 (KNT.txt line 1128) and §84 (line 1608)\", \"stance\": \"supports\",\n   \"note\": \"'The prefix ud \\\"up\\\", which appears unchanged before a vowel in ud-apatatā \\\"he rose up (in rebellion)\\\", suffers complete assimilation of the d in uzma- \\\"stake\\\" (from *ud-zma-), and became us- in us-taxāna- \\\"staircase\\\"'; §84 'OP example: uzma- \\\"stake\\\" from *ud-zma-'. Nourai's two forms ud-zma and uzma are Kent's pre-form and attested form.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no. 667 (HUB.txt line 2451)\", \"stance\": \"contradicts\",\n   \"note\": \"'Ap. uzmayā-patiy kar \\\"kreuzigen (Bang: pfählen)\\\" gehört schwerlich hierher' — Hübschmann denies the connection with zam-/zamīn that this arrow asserts.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 667 (HRN.txt line 5892)\", \"stance\": \"supports\",\n   \"note\": \"Horn lists 'ap. uzmaya[patiy]' as the first comparandum of NP zamī/zamīn — i.e. he does derive it from the 'earth' word, which is the position Hübschmann was arguing against and Kent later restored.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie (grep uzm-, zm-)\", \"stance\": \"silent\",\n   \"note\": \"The word has no Middle Persian continuation, so the Pahlavi dictionary has nothing; the chart correctly draws no descendant from it (see node 12).\"}\n ]})\n\nN.append({\n \"id\": 12, \"lang\": \"None\", \"words\": \"\", \"verdict\": \"unverified\",\n \"derivation\": \"A blank box. The printed page (pdf p.180, kept at data/verification/sources/refs/ocr/BOOK/180.png) shows a genuinely empty double-ruled rectangle to the right of the 'Old Persian ud-zma, uzma' box, with no language label, no word, no gloss and no references, so the extraction is faithful and there is nothing to verify. Substantively the emptiness is correct: OP uzma- 'stake' has no Middle or New Persian continuation (it is absent from MacKenzie and Nyberg), so the slot that in every parallel row of this chart holds the Persian reflex has nothing to hold. The box is best read as a layout artefact of Nourai's drawing program rather than as a claim.\",\n \"derivation_fa\": \"جعبه‌ای تهی است. تصویرِ صفحهٔ چاپی (صفحهٔ ۱۸۰ پی‌دی‌اف، نگه‌داشته در مسیرِ ocr/BOOK/180.png) نشان می‌دهد که در کنارِ جعبهٔ «پارسی باستان: ud-zma، uzma» مستطیلی دوخطّه و کاملاً خالی چاپ شده است، بی هیچ نامِ زبان و واژه و معنا و مأخذی؛ پس خطای خوانشِ اسکن نیست و چیزی برای سنجیدن نمانده. از دیدِ محتوایی هم این تهی بودن درست است: uzma- پارسیِ باستان در فارسیِ میانه و نو دنباله‌ای ندارد (نه در مکنزی هست نه در نیبرگ)، و جایگاهی که در دیگر ردیف‌های همین نمودار بازتابِ فارسیِ واژه را در خود دارد، اینجا چیزی برای نشاندن ندارد. بهتر است آن را بازماندهٔ برنامهٔ نمودارکشیِ نویسنده دانست نه ادعایی ریشه‌شناختی.\",\n \"error_in\": \"book\",\n \"book_prints\": \"(an empty double-ruled box, no text at all)\",\n \"correct_form\": \"(nothing — OP uzma- has no Persian continuation)\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no references and no words.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (grep uzm-)\", \"stance\": \"silent\",\n   \"note\": \"No Middle Persian reflex of uzma-; the Pahlavi z-section runs zamān, zamānag, zamestān, zamīg, zāmyād, zan... with nothing from *ud-zma-.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\",\n   \"note\": \"Likewise nothing; the glossary's only relevant entry is damīk/zamīk 'earth'.\"}\n ]})\n\nN.append({\n \"id\": 13, \"lang\": \"Latin\", \"words\": \"humus; homo; humanus\", \"verdict\": \"confirmed\",\n \"derivation\": \"All three are the standard Latin reflexes of this root and all three stand in Nourai's cited source. humus f. 'ground, soil' is the suffixed o-grade *(dʰ)ǵʰom-o-, a thematised remake of an older consonant stem *ǵʰom-, which kept the feminine gender of the old *dʰéǵʰōm (Ernout-Meillet: 'comme les autres noms de la terre, tellūs, terra, par réaction du genre sur la forme'); the locative humī 'on the ground' preserves the old case form, and humilis 'low' (: Gk. khthamalós) is built on it. homō, -inis 'human being' is the suffixed o-grade *(dʰ)ǵʰom-on- 'earthling', with Old Latin hemō still visible in the accusative hemōnem and in nemō 'nobody' < *ne-hemō; the Oscan-Umbrian cognates humuns / homonus show the same stem. hūmānus 'human, humane' belongs here too, though with an unexplained long ū (Walde-Pokorny: 'mit unklarem Vokalismus'); Watkins guards it with '(in part)'. Nourai's gloss 'kind' for humanus is copied straight from Watkins' 'Latin hūmānus, human, kind, humane'. The one thing the box does not show is that homo/hūmānus and humus are two different derivatives of the root rather than a chain.\",\n \"derivation_fa\": \"هر سه واژه بازتاب‌های متعارفِ لاتینیِ همین ریشه‌اند و هر سه در همان مأخذی هستند که نورایی یاد کرده است. humus (مؤنث) «خاک، زمین» صورتِ درجهٔ o با پسوند، یعنی *(dʰ)ǵʰom-o-، بازساختی مصوّت‌دار از ستاکِ همخوانیِ کهنِ *ǵʰom- است و جنسِ مؤنثِ *dʰéǵʰōm هندواروپایی را نگاه داشته (ارنو و مه‌یه: «مانندِ دیگر نام‌های زمین، tellūs و terra»)؛ صورتِ دریِ humī «بر زمین» همان حالتِ کهن است و humilis «پست» (هم‌ارزِ khthamalós یونانی) بر آن ساخته شده. homō با اضافیِ hominis «آدمی» درجهٔ o با پسوندِ -on-، یعنی *(dʰ)ǵʰom-on- «زمینی، خاکی»، است و صورتِ کهنِ لاتینیِ hemō هنوز در رایِ hemōnem و در nemō «هیچ‌کس» از *ne-hemō پیداست؛ هم‌ریشه‌های اسکی و اومبریایی (humuns، homonus) همان ستاک را نشان می‌دهند. hūmānus «انسانی، مهربان» نیز از همین جاست، هرچند کشیدگیِ ū آن ناروشن مانده است (والده‌ـ‌پوکورنی: «با آواشناسیِ نامعلوم») و واتکینز آن را با قیدِ «تا اندازه‌ای» می‌آورد. معنای «kind» که نورایی برای humanus داده، عینِ عبارتِ واتکینز است. تنها نکته‌ای که جعبه نشان نمی‌دهد این است که humus از یک سو و homo/hūmānus از سوی دیگر دو مشتقِ جداگانهٔ ریشه‌اند نه یک زنجیره.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 382, s.v. dhghem-: '4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, \\\"earthling\\\", in: a. Latin homo, human being, man: HOMAGE, ... HOMICIDE; b. (in part) Latin humanus, human, kind, humane: HUMAN, (HUMANE).' Nourai's three words, their glosses and their English derivatives are all lifted from this one sentence.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. humus (LAT.txt lines 28701-28745)\", \"stance\": \"supports\",\n   \"note\": \"'humus, -ī f. ... terre, sol; loc. humī \\\"par terre, sur le sol\\\" ... Dérivés et composés: humilis \\\"qui reste à terre\\\" ... humō, -ās \\\"enterrer\\\" ... Cf. aussi homō.' And, on the root: 'ce nom avait à l'initiale une forme alternante, à groupe de consonnes dans véd. kṣāḥ ... gr. khthōn, v.irl. dú (gen. don), à consonne simple dans gr. khamaí et sans doute dans av. zā, gén. zamō, loc. zemi.'\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 663 (WLD_Bd1 djvu line 41788 ff.)\", \"stance\": \"supports\",\n   \"note\": \"'lat. homo, -inis \\\"Mensch\\\" umgelautet aus alat. hemo (auch in nemo \\\"niemand\\\" aus *ne-hemo), acc. hemonem; dazu humānus \\\"menschlich\\\" (Lit. zum noch klärungsbedürftigen ū ...)' and 'osk.-umbr. *homon- ... o. humuns \\\"homines\\\", u. homonus \\\"hominibus\\\"'.\"},\n  {\"src\": \"POK\", \"where\": \"Pokorny IEW 414-415\", \"stance\": \"supports\",\n   \"note\": \"'Latin humus (from *homos) \\\"earth, ground\\\" ... probably reshaping of an old consonant-stem *ghom-; hence also f. as khthōn; humilis \\\"low\\\" (: khthamalós)'.\"},\n  {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.v. human, exhume (WEB_vol1.txt lines 68705, 92761)\", \"stance\": \"supports\",\n   \"note\": \"'humanus; to homo, a man, humus, soil'; 'exhumare, to dig up ... L. ex, out, and humus, the ground'.\"}\n ]})\n\nN.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"humble, humility; human, homicide; humane\", \"verdict\": \"confirmed\",\n \"derivation\": \"Each of the five English words takes the Latin route drawn in the box, and all five appear in the AHD entry that the parent node cites. humble is ME humble/umble from Old French humble, from Latin humilem, acc. of humilis 'low, lit. on the ground', a derivative of humus (Klein s.v. humble: 'fr. L. humilem ... lit. \\\"on the ground\\\", fr. humus'); humility is Old French humilite from Latin humilitātem. human comes through Old French humain from Latin hūmānus, and humane is the same word: the two were a single English word into the seventeenth century, and only then did spelling and stress split them into 'of mankind' and 'kindly' — hence Watkins' bracketing '(HUMANE)'. homicide is Old French homicide from Latin homicīdium 'manslaughter' and homicīda 'man-slayer', i.e. homo + -cīda (caedere 'to cut, kill'), and so belongs to the homo branch, not the humus branch. The box's grouping in three lines in fact tracks that distinction correctly: humble/humility from humus, human/humane from hūmānus, homicide from homo.\",\n \"derivation_fa\": \"هر پنج واژهٔ انگلیسی همان راهی را می‌روند که در جعبه کشیده شده و هر پنج در همان مادهٔ فرهنگِ American Heritage هست که گرهٔ بالادست به آن ارجاع می‌دهد. humble در انگلیسیِ میانه humble/umble است از humble فرانسویِ کهن، از humilem لاتینی (رایِ humilis «پست، به‌لفظ: بر زمین») که خود مشتقِ humus است — کلاین می‌نویسد: «از humilem لاتینی … به‌لفظ «بر زمین»، از humus»؛ humility از humilite فرانسویِ کهن و humilitātem لاتینی. human از راهِ humain فرانسویِ کهن از hūmānus می‌آید و humane همان واژه است: این دو تا سدهٔ هفدهم یک واژه بودند و سپس املا و جای تکیه آن‌ها را به «انسانی» و «مهربان» بخش کرد؛ به همین سبب واتکینز HUMANE را در کمانک می‌گذارد. homicide از homicide فرانسویِ کهن و homicīdium/homicīda لاتینی است، یعنی homo به‌علاوهٔ -cīda از caedere «کشتن»، و پس به شاخهٔ homo تعلق دارد نه به شاخهٔ humus. سه‌سطری بودنِ جعبه در واقع همین تفکیک را درست نشان می‌دهد.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no references; the parent's AHD citation covers it and supports it word for word ('HUMBLE, (HUMILIATE), (HUMILITY), HUMUS' under humus; 'HOMAGE ... HOMICIDE' under homo; 'HUMAN, (HUMANE)' under humanus).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. humble (KLN_1971.txt line 116662)\", \"stance\": \"supports\",\n   \"note\": \"'humble, adj. — ME. humble, umble, fr. OF.(= F.) humble, fr. L. humilem, acc. of humilis, \\\"low, base, humble\\\", lit. \\\"on the ground\\\", fr. humus, \\\"earth, ground, soil\\\". See humus and words there referred to and cp. esp. humiliate, humility.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt lines 1638-1639, 1658)\", \"stance\": \"supports\",\n   \"note\": \"The reverse index lists 'HOMICIDE dhghem-', 'HUMAN dhghem-', 'HUMANE dhghem-', 'HUMBLE dhghem-', 'HUMILITY dhghem-' — every word of this node, under this root.\"},\n  {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary s.v. human\", \"stance\": \"supports\",\n   \"note\": \"'humanus; to homo, a man, humus, soil' — the same two-branch analysis.\"}\n ]})\n\nN.append({\n \"id\": 15, \"lang\": \"Greek\", \"words\": \"gumon\", \"verdict\": \"disputed\",\n \"derivation\": \"The word is real but the language is wrong, and Nourai's own cited source says so. AHD (Watkins) reads: 'dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, \\\"earthling,\\\" in GERMANIC *gumon- in Old English guma, man: BRIDEGROOM.' Nourai has copied the reconstruction *gumon- but labelled the box Greek. There is no Greek word gumon and none could be: PIE *dʰǵʰ- gives Greek khth-, so this root's Greek reflexes are khthṓn 'earth', khamaí 'on the ground', khthamalós 'low' — all with initial khth-/kh-, and all listed a line above in the same AHD entry. The form *gumōn- is Proto-Germanic, whence Gothic guma, Old Norse gumi, Old English guma, Old High German gomo 'man', and the compound *brūdi-gumô that gives German Bräutigam and, via node 16, English bridegroom. Walde-Pokorny I 663 and Mann both put guma in Germanic; Klein s.v. bridegroom writes 'OE. guma, \\\"man\\\", which is rel. to OS. gumo, ON. gumi, OFris. goma, OHG. gomo, Goth. guma, \\\"man\\\", and cogn. with L. homo'. The printed page (image at data/verification/sources/refs/ocr/BOOK/180.png) really does read 'Greek', so the extraction is faithful and the mislabelling is the book's own; the label should be Germanic (or Old English guma).\",\n \"derivation_fa\": \"واژه واقعی است اما برچسبِ زبان نادرست است، و خودِ مأخذی که نورایی یاد کرده همین را می‌گوید. واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگِ American Heritage می‌نویسد: «dhghem- «زمین». ۱. صورتِ درجهٔ صفر با پسوند، *(dh)ghm-on- «زمینی»، در ژرمنیِ *gumon- که در انگلیسیِ کهن guma «مرد» شده است: BRIDEGROOM». نورایی بازساختِ *gumon- را برداشته اما جعبه را «یونانی» برچسب زده است. واژه‌ای یونانی به‌صورتِ gumon نه هست و نه می‌تواند باشد: *dʰǵʰ- هندواروپایی در یونانی khth- می‌دهد، و بازتاب‌های یونانیِ این ریشه khthōn «زمین»، khamaí «بر زمین» و khthamalós «پست» است — که همگی یک سطر بالاتر در همان مادهٔ AHD آمده‌اند. صورتِ *gumōn- ژرمنیِ آغازین است و از آن گوتیِ guma، نورسِ کهنِ gumi، انگلیسیِ کهنِ guma و آلمانیِ علیای کهنِ gomo «مرد» و ترکیبِ *brūdi-gumô آمده که Bräutigam آلمانی و — از راهِ گرهٔ ۱۶ — bridegroom انگلیسی از آن است. والده‌ـ‌پوکورنی (جلد یکم ص ۶۶۳) و مان نیز guma را ژرمنی می‌دانند و کلاین ذیلِ bridegroom می‌نویسد که OE guma هم‌ریشهٔ گوتیِ guma و هم‌ارزِ homo لاتینی است. تصویرِ صفحهٔ چاپی نشان می‌دهد که در کتاب هم «Greek» چاپ شده است؛ پس خطای خوانشِ اسکن نیست، خطای خودِ کتاب است و برچسب باید «ژرمنی» (یا «انگلیسی کهن: guma») می‌بود.\",\n \"error_in\": \"book\",\n \"book_prints\": \"Greek [AHD] | gumon : man\",\n \"correct_form\": \"Germanic *gumōn- (Old English guma) 'man'\",\n \"sources\": [W + \"Reconstruction:Proto-Germanic/gum%C3%B4\", \"https://www.etymonline.com/word/bridegroom\"],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"contradicts\",\n   \"note\": \"AHD_watkins1985.txt line 382: '1. Suffixed zero-grade form *(dh)ghm-on-, \\\"earthling,\\\" in Germanic *gumon- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCHTHON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground.' The reference Nourai cites assigns *gumon- to Germanic and gives Greek quite different reflexes.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 663 (WLD_Bd1 djvu line ~41810)\", \"stance\": \"contradicts\",\n   \"note\": \"'got. guma, aisl. gumi, ags. guma, ahd. gomo \\\"Mensch, Mann\\\", nhd. in Bräuti-gam (idg. *gh(e)mon- oder *gh(o)mon-)' — a Germanic list, with no Greek member.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. bridegroom (KLN_1971.txt line 33727)\", \"stance\": \"contradicts\",\n   \"note\": \"'The second element arose through the substitution of groom for OE. guma, \\\"man\\\", which is rel. to OS. gumo, ON. gumi, OFris. goma, OHG. gomo, Goth. guma, \\\"man\\\", and cogn. with L. homo, \\\"man\\\". See human.'\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 6080\", \"stance\": \"contradicts\",\n   \"note\": \"'Go. guma, gs gumins, pl. gumans; OE guma; OHG gomo, gs -en; MHG gome, gume; ON cf. gumi, coll. gumnar' — again Germanic only; the Greek member of Mann's entry is khamaí.\"},\n  {\"src\": \"POK\", \"where\": \"Pokorny IEW 415\", \"stance\": \"contradicts\",\n   \"note\": \"'Gothic guma, Old Icelandic gumi, Old English guma, Old High German gomo \\\"person, man, husband\\\", Modern High German in Brauti-gam (Indo Germanic *ghemon- or *ghomon-)'; Pokorny's Greek entries for the root are khthōn, khamaí, khthamalós.\"}\n ]})\n\nN.append({\n \"id\": 16, \"lang\": \"English\", \"words\": \"bridegroom\", \"verdict\": \"confirmed\",\n \"derivation\": \"The English word does descend from *gumōn-, so the arrow's substance is right even though its parent box is mislabelled (node 15). Old English brȳdguma = brȳd 'bride' + guma 'man', i.e. 'the bride's man', matching Old Saxon brūdigomo, Old Norse brúðgumi, Old High German brūtigomo, German Bräutigam (Gothic went its own way with brūþsfaþs 'bride's lord'). In Middle English the word is still brudgume, bridegome; guma then died out of the language, and in the sixteenth century the now-meaningless second element was replaced by folk etymology with the familiar groom 'lad, serving-man' — the sole source of the -r-, which has no etymological standing. The word is thus, through guma < Germanic *gumōn- < PIE *(dʰ)ǵʰm-on- 'earthling', a cousin of Latin homo and, through the root, of Persian zamīn: the bridegroom is literally 'the bride's earthling'.\",\n \"derivation_fa\": \"واژهٔ انگلیسی به‌راستی از *gumōn- می‌آید، پس مضمونِ پیکان درست است هرچند جعبهٔ بالادستش (گرهٔ ۱۵) برچسبِ نادرست دارد. در انگلیسیِ کهن brȳdguma است، یعنی brȳd «عروس» + guma «مرد»، «مردِ عروس»، برابر با brūdigomo ساکسونِ کهن، brúðgumi نورسِ کهن، brūtigomo آلمانیِ علیای کهن و Bräutigam آلمانی (گوتی راهِ دیگری رفته و brūþsfaþs «خداوندِ عروس» دارد). در انگلیسیِ میانه هنوز brudgume و bridegome است؛ سپس واژهٔ guma از زبان افتاد و در سدهٔ شانزدهم جزءِ دومِ بی‌معنا شده را به ریشه‌شناسیِ عامیانه با groom «پسر، نوکر» جانشین کردند — و «ر» این واژه یکسره از همین‌جاست و هیچ پشتوانهٔ ریشه‌شناختی ندارد. بدین‌سان bridegroom از راهِ guma و ژرمنیِ *gumōn- و هندواروپاییِ *(dʰ)ǵʰm-on- «زمینی» پسرعمویِ homo لاتینی و، از راهِ ریشه، هم‌ریشهٔ «زمین» فارسی است: داماد به‌لفظ «خاکیِ عروس» است.\",\n \"sources\": [\"https://www.etymonline.com/word/bridegroom\", W + \"Reconstruction:Proto-Germanic/gum%C3%B4\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"No references on the node; the parent's AHD citation ends its first sense with 'Old English guma, man: BRIDEGROOM', which supports this arrow (while contradicting the parent's 'Greek' label).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. bridegroom (KLN_1971.txt line 33727)\", \"stance\": \"supports\",\n   \"note\": \"'bridegroom, n. — ME. brudgume, bridegome, fr. OE. brydguma, rel. to OS. brudigumo, ON. brudgumi, OHG. brutigomo, MHG. briutegome, G. Bräutigam ... The second element arose through the substitution of groom for OE. guma, \\\"man\\\".'\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Groom (SKT.txt line 8036)\", \"stance\": \"supports\",\n   \"note\": \"'In the comp. bridegroom it is quite certain that the r is intrusive ... the etym. is from A.S. guma, man, allied to Icel. gumi, Goth. guma, homo, a man.'\"},\n  {\"src\": \"web\", \"where\": \"Etymonline s.v. bridegroom\", \"stance\": \"supports\",\n   \"note\": \"'from Old English brydguma ... the guma element traces back to Proto-Germanic *gumon-, literally \\\"earthling, earthly being,\\\" derived from the PIE root *dhghem- \\\"earth\\\"'; the -room ending arose in the 16th c. by 'folk etymology after groom (n.)'.\"}\n ]})\n\nout = {\n \"pdf_page\": 180,\n \"book_page\": 150,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry],\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-180.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('ok', len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build180.py",
 "description": "Build page-180.json"
}
```


### [2026-09-05T21:12:56.660Z] TOOL RESULT

```
ok 16
```


## [2026-09-05T21:12:57.266Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
