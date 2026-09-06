# Verification process log — verify-page-239


## [2026-09-06T15:43:17.342Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 239 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-239.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-239.json. Write /home/sfmqrb/git/rishe/data/verification/page-239.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 239` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:43:18.471Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:43:19.235Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:43:19.251Z] TOOL RESULT

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


## [2026-09-06T15:43:19.775Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-239.txt"
}
```


### [2026-09-06T15:43:19.805Z] TOOL RESULT

```
1	=== PDF page 239 (book page 209) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kand 1, Qand : to shine, to be white  (refs POK:526)
4	#1 (parent #0) [Sanskrit] refs=POK:526 | kandrak : shining ; kandana, kundruka : sandalwood
5	  #2 (parent #1) [Pahlavi] refs=SIN:585 | kundurŭk : sandalwood
6	    #3 (parent #2) [Persian] refs=SIN:552,585; BQT:664,1174,1705; MON:1930 | kondor «کُندر» : incense ; sandal «سندل» : sandalwood, sandal shoe ; sandalî «صندلی» : chair (originally made of sandalwood) | extra: چُندل ، چُندن
7	      #4 (parent #3) [Greek] refs=KLN:1380; SKT:462 | santalon : sandal tree ; santalion : sandal shoe
8	        #5 (parent #4) [Latin] refs=None | 
9	          #6 (parent #5) [French] refs=None | 
10	            #7 (parent #6) [English] refs=None | sandal
11	#8 (parent #0) [Sanskrit] refs=AHD:1149 | candrah-râga : bright red (resin from tree)
12	  #9 (parent #8) [Greek] refs=AHD:1149 | sandarak, sandaraxĕ : a red resin from trees
13	    #10 (parent #9) [Arabic] refs=TAD:37 | sendarŭs : a resinous tree
14	      #11 (parent #10) [Persian] refs=MON:1929 | sandarŭs «سَنْدَروس» : a resinous tree and its red resin | extra: سَندَره
15	    #12 (parent #9) [Latin] refs=AHD | sandraca : red pigment, red resin
16	      #13 (parent #12) [English] refs=AHD:1149 | sandarac
17	#14 (parent #0) [Latin] refs=AHD; KLN:231 | candidus : glowing white ; candidâre : to make white or bright ; candidâtus : candidate (due to their white toga)
18	  #15 (parent #14) [French] refs=None | candidat
19	    #16 (parent #15) [Persian] refs=MON:2874 | kândîd «کاندید ، کائندیدا» : candidate
20	  #17 (parent #14) [English] refs=None | candid, candidate, candle, chandelier, incandescent
21	#18 (parent #0) [Greek] refs=AHD | kandhĕla : light, lamp, candle
22	  #19 (parent #18) [Arabic] refs=TAD:59; BQT:1545 | qandîl : light, lamp
23	    #20 (parent #19) [Persian] refs=MON:2734; ARK:235 | qandîl «قندیل» : lamp
24	--- entry 1 ---
25	ROOT Kand 2 -> redirect to Skand
26	--- entry 2 ---
27	ROOT Kank -> redirect to Kâk 2
28	
```


## [2026-09-06T15:43:22.524Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-239.json | head -200",
 "description": "Read source JSON page 239"
}
```


### [2026-09-06T15:43:22.560Z] TOOL RESULT

```
{
  "pdf_page": 239,
  "book_page": 209,
  "entries": [
    {
      "root": {
        "name": "Kand 1, Qand",
        "lang": "Indo-European",
        "refs": "POK:526",
        "gloss": "to shine, to be white"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:526",
          "words": [
            {"translit": "kandrak", "gloss": "shining", "script": null},
            {"translit": "kandana, kundruka", "gloss": "sandalwood", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SIN:585",
          "words": [
            {"translit": "kundurŭk", "gloss": "sandalwood", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SIN:552,585; BQT:664,1174,1705; MON:1930",
          "words": [
            {"translit": "kondor", "gloss": "incense", "script": "کُندر"},
            {"translit": "sandal", "gloss": "sandalwood, sandal shoe", "script": "سندل"},
            {"translit": "sandalî", "gloss": "chair (originally made of sandalwood)", "script": "صندلی"}
          ],
          "script_extra": "چُندل ، چُندن",
          "note": null,
          "quote": {
            "text": "بفروز و بسوز پیش خویش امشب - چندان که توان ز عود و از چُندن",
            "poet": "Asjadî Marvazî"
          }
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": "KLN:1380; SKT:462",
          "words": [
            {"translit": "santalon", "gloss": "sandal tree", "script": null},
            {"translit": "santalion", "gloss": "sandal shoe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sandal", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:1149",
          "words": [
            {"translit": "candrah-râga", "gloss": "bright red (resin from tree)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Greek",
          "refs": "AHD:1149",
          "words": [
            {"translit": "sandarak, sandaraxĕ", "gloss": "a red resin from trees", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "TAD:37",
          "words": [
            {"translit": "sendarŭs", "gloss": "a resinous tree", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON:1929",
          "words": [
            {"translit": "sandarŭs", "gloss": "a resinous tree and its red resin", "script": "سَنْدَروس"}
          ],
          "script_extra": "سَندَره",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sandraca", "gloss": "red pigment, red resin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD:1149",
          "words": [
            {"translit": "sandarac", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:231",
          "words": [
            {"translit": "candidus", "gloss": "glowing white", "script": null},
            {"translit": "candidâre", "gloss": "to make white or bright", "script": null},
            {"translit": "candidâtus", "gloss": "candidate (due to their white toga)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "candidat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
```


## [2026-09-06T15:43:23.206Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:43:23.242Z] TOOL RESULT

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


## [2026-09-06T15:43:26.873Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '200,300p' data/extracted/batch/page-239.json && echo ---- && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','SKT','SIN','BQT','MON','TAD','ARK','WLD']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-06T15:43:28.881Z] TOOL RESULT

```
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:2874",
          "words": [
            {"translit": "kândîd", "gloss": "candidate", "script": "کاندید ، کائندیدا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "candid, candidate, candle, chandelier, incandescent", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kandhĕla", "gloss": "light, lamp, candle", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Arabic",
          "refs": "TAD:59; BQT:1545",
          "words": [
            {"translit": "qandîl", "gloss": "light, lamp", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Persian",
          "refs": "MON:2734; ARK:235",
          "words": [
            {"translit": "qandîl", "gloss": "lamp", "script": "قندیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چو از زلف شب باز شد تابها - فرو مُرد قندیل محرابها",
            "poet": "Manŭchehrî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Kand 2",
        "redirect": "Skand"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kank",
        "redirect": "Kâk 2"
      },
      "nodes": []
    }
  ]
}
----
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


## [2026-09-06T15:44:03.783Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==534' POK_01.txt | head -60",
 "description": "Print Pokorny page 526"
}
```


## [2026-09-06T15:44:05.197Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kand-\" POK_full.txt | head -30; echo ===; grep -n \"candeo\\|candela\\|candidus\" POK_full.txt | head -20",
 "description": "Grep Pokorny for kand"
}
```


### [2026-09-06T15:44:05.324Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:44:05.377Z] TOOL RESULT

```
Exit code 1
43488:Root/ lemma: kand-, skand- and (Old Indie) (s)kend- 
43495:Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 
75017:Root / lemma: (s)kand- (s)kend- 
(eval):2: == not found
```


## [2026-09-06T15:44:08.228Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43480,43560p' POK_full.txt",
 "description": "Read Pokorny kand entry"
}
```


### [2026-09-06T15:44:08.274Z] TOOL RESULT

```
nasalized equal meaning family of Old Indie capa-vn. n. "bow', capala-' resWess, 
fluctuating ', npers. cap "left', i.e. "*crooked'; Endzelin KZ. 44, 63 reminds of *capala-a\so 
in Latvian kaparuoties' wriggle ', k'eparaV wriggle, move with difficulty ', Lithuanian 
kapanotis " liegend sich aufzuhelfen suchen ' or " go laboringly '. 

References: WP. I 346, 350 f., WH. I 148 f., Trautmann 116. 
Page(s): 525 

Root/ lemma: kand-, skand- and (Old Indie) (s)kend- 
Meaning: to glow; bright, *moon 



Note: 

Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 

from Root/ lemma: sen(o)-{*heno)\ 'old, *old moon' 

Material: Old Indie ^3/70(3// 'shines', Intens. participle cani-scadaV exceedingly gleaming' 

[*sknd-), candra- {scandra-, EN Hari-scandra-) 'luminous, gleaming, burning; m. moon', 

candana-m. n. ' sandalwood (incense '); 

gr. KQvSapoc; avGpa^ Hes.; 

alb. Geg hane, Tosc hene^moon' {*skandna) : Urdu chand'moon' 

PN Candavia : Maybe lllyrian PN Sca(n)din-avia 

(Kav5aouia), Candavii Montes. The mountains separating lllyricum from Macedonia, 
across which the Via Egnatia ran. 

Latin candeo, -e/ie 'gleam, shimmer, bright glow', transitive *candd, -ere\x\ accendo, 
incendo^ set on fire, ignite, inflame ', ca/7o'/b'i/s 'blinding, dazzling white, gleaming', candor 
' A dazzling, glossy whiteness, a clear lustre, clearness, radiance, brightness, brilliancy, 
splendor, glitter ', candela, candelabrum ' cand\est\ck, flambeaux' (out of it cymr. etc. 
cannwyll ds. {common Celtic -ns-, -nt- > -nn-}), cicindela^ little luminous beetle, oil lamp ', 
cicendula^ lamps ' (redupl. *ce-cand-)\ 

cymr. C5/7/7 'white, bright'. Middle Breton cann^ full moon ', abret. cant^ canus '; 
borrowing from cand/dus takes Pedersen KG. I 190 (compare Latin splendidus> bret. 
splann), but cymr. c5/7/7a/o'' luminous; sun, moon' and numerous derivatives leave perhaps 
a genuine Celtic *kando- seem possible, whereas the FIN Kander {Badeu, Switzerland) 
does not belong to Indo Germanic gand- ' waste, desolate reclining land', Bertoldi BSL 30, 
111 and Anm. 2. 

References: WP. I 352, WH. I 151 f. 
Page(s): 526 

Root / lemma: kan-tho- 

Meaning: angle, curve 

Note: probably from kam-tho-io kam-p-'bend' 

Material: Gr. kqvOoc; ' corner of the eye'; in the meaning ' wheel rim' meaning-loanword 

from Latin cantus, 

Latin cantus"\ron wheel rim' is again loanword from: 



gall, (also gallo-rom.) *cantos "\ron ring, edge, point, edge', cymr. cant {hence ceiniog' 
penny, coin ') ds., bret. kant^ circle ', Old Irish cetad^ {round) seat' from * kanto-sedo-. 
Middle Irish ce/'round stone pillar'; derivatives: gall, cantalon, probably " pillar', cantena, 
KavTsva dss.?; also gall, cando-soccus^ Rebsenker ', lies canto-soccus {io gall, succo-^ 
pig's snout, plowshare '; compare Jud Arch. Rom. VI 210 f.); 

abret. //7/cc»^ca/7/ "complete'; mcymr. yn geuganf6s. (actually "very skillful ' from *kouo- 
kantos, Latin caved); to kant^ circle ' > " perfect ' compare acymr. Iloerganf full moon'; 

cymr. ca/7/"troop, multitude, crowd', in addition Middle Irish cete {*kantia) "congregation, 
meeting', probably as *" a division of 100' identical with cymr. c5/7/"100' above S. 92; 

Slavic *kgt-b m. " angle ' in russ.-Church Slavic kut-b etc. 

Maybe alb. /re/7o' "angle' a Slavic loanword?.
```


## [2026-09-06T15:44:09.245Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 532 533 534 535; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt | head -20; done",
 "description": "Print Pokorny leaves around 534"
}
```


### [2026-09-06T15:44:11.454Z] TOOL RESULT

```
=== leaf 532 ===
=== leaf 533 ===
=== leaf 534 ===
=== leaf 535 ===
```


## [2026-09-06T15:44:19.797Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"$f: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) leaves\"; done\necho ===; grep -n \"kand-\" POK_0*.txt | head; echo ===; grep -n \"candela\" POK_0*.txt | head",
 "description": "Check POK volume coverage"
}
```


## [2026-09-06T15:44:21.004Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sandarac\\|Sandarac\" KLN_1966.txt | head -10; echo \"=== KLN sandal ===\"; grep -n \"^sandal\\|sandal, n\\|sandalwood\" KLN_1966.txt | head -20",
 "description": "Grep Klein for sandarac/sandal"
}
```


### [2026-09-06T15:44:21.623Z] TOOL RESULT

```
Exit code 1
POK_01.txt: 363 leaves
POK_02.txt: 433 leaves
POK_03.txt: 429 leaves
(eval):3: == not found
```


### [2026-09-06T15:44:21.694Z] TOOL RESULT

```
2151:Derivative:  alepidote,  n.,  a  fish  without  scales, alerce,  alerze,  n.,  the  sandarac  tree.  —  Sp.,  ‘the larch  tree’,  fr.  Arab,  al-arz,  in  vulgar  pronun¬ ciation  al-erz,  fr.  al-,  ‘the’,  and  arz,  resp.  erz, ‘coniferous  tree,  pine  tree,  cedar’,  borrowed  fr. Heb.  erez,  ‘cedar’.
6339:upright',  fr.  candere,  ‘to  shine,  glow,  be  white  , which  is  cogn.  with  Gk.  xavSapo;,  ‘glowing coal’,  OI.  candrah,  ‘shining  glowing’,  candana ‘sandalwood’  (lit.  ‘wood  for  burning  incense’). Alb.  Gheg  hqne,  Tosk  hene,  ‘moon’  (lit.  ‘the white  one’).  All  these  words  derive  fr.  I.-E.  base *(s)qand-,  *(s)qend-,  ‘to  shine,  glow’.  Cp.  W. cann,  ‘white,  bright’,  OBret.  cant,  ‘white’, MBret.  cann,  ‘full  moon’,  which,  according  to Pedersen,  are  not  cognate  with  L.  candidus,  but loan  words  fr.  VL.  *candus,  contraction  of  can¬ didus  (see  haplology).  Cp.  candle,  candelabrum, candidate,  chandelier,  chandler,  Cicindelidae, incandescent,  incense,  sandalwood,  sandarac, sanders,  santal.
33668:rub,  rub  away;  to  crumble  away'.  See  psilo- and  cp.  ammo,  psammite,  psephism,  sabulous, saburra  and  the  second  element  in  palimpsest. Derivatives:  sand,  tr.  v.,  sand-ing,  n. sandal,  n.  —  L.  sandalium,  fr.  Gk.  oavSaXtov, dimin.  of  oavSaXov,  a  word  from  Asia  Minor (whence  also  Pers.  sandal),  orig.  meaning  ‘shoe of  the  Lydian  god  Sandal'.  See  Kretschmer, Indogermanische  Forschungen,  45,  270  (1927). sandalwood,  n.  —  ML.  sandalum  (whence  also OF.  sandal),  fr.  Arab,  sandal,  fr.  OI.  candanah, ‘sandalwood’  (lit.  ‘wood  for  burning  incense’), which  is  rel.  to  candrah,  ‘shining,  glowing’,  and cogn.  with  Gk.  zavSapoc,  ‘glowing,  coal’,  L. candere,  ‘to  shine,  glow,  be  white’.  See  candid and  cp.  sanders  and  santal.  Cp.  also  next  word, sandarac,  n.,  1)  the  sandarac  tree;  2)  resin  ob¬ tained  from  this  tree;  3)  realgar.  —  L.  sanda- raca,  fr.  Gk.  aavSapax.T),  which  is  of  Oriental origin.  Cp.  OI.  candra-raga-,  ‘having  the  bright-
39189:thyine,  adj.,  pertaining  to  the  sandarac  tree.  — Late  L.  thyinus,  fr.  Gk.  ffu'ivo?,  fr.  fku5,  an African  tree.  See  thyme  and  adj.  suff.  -ine.
=== KLN sandal ===
2326:Bible,  prob.  the  sandalwood  (the  first  form  oc¬ curs  I  Kings  10:11-12,  the  second  11  Chron. 2:7  and  9:10-11).  —  Heb.  almuggtm,  resp.  al- gummfm  (pi.).  The  singular  of  these  words  must be  almdgh,  resp.  algdm,  so  that  the  forms almug  and  algum  are  incorrect.  They  should  be replaced  by  almog,  resp.  algom. alnage,  n.,  measurement  by  the  ell.  —  OF.  aul- nage  (F.  aunage),  fr.  aulne,  ‘ell’,  fr.  Frankish *alina,  prop,  ‘forearm’,  which  is  rel.  to  OHG. elina,  OE.  eln,  ‘ell’.  See  ell  and  -age.
6339:upright',  fr.  candere,  ‘to  shine,  glow,  be  white  , which  is  cogn.  with  Gk.  xavSapo;,  ‘glowing coal’,  OI.  candrah,  ‘shining  glowing’,  candana ‘sandalwood’  (lit.  ‘wood  for  burning  incense’). Alb.  Gheg  hqne,  Tosk  hene,  ‘moon’  (lit.  ‘the white  one’).  All  these  words  derive  fr.  I.-E.  base *(s)qand-,  *(s)qend-,  ‘to  shine,  glow’.  Cp.  W. cann,  ‘white,  bright’,  OBret.  cant,  ‘white’, MBret.  cann,  ‘full  moon’,  which,  according  to Pedersen,  are  not  cognate  with  L.  candidus,  but loan  words  fr.  VL.  *candus,  contraction  of  can¬ didus  (see  haplology).  Cp.  candle,  candelabrum, candidate,  chandelier,  chandler,  Cicindelidae, incandescent,  incense,  sandalwood,  sandarac, sanders,  santal.
33668:rub,  rub  away;  to  crumble  away'.  See  psilo- and  cp.  ammo,  psammite,  psephism,  sabulous, saburra  and  the  second  element  in  palimpsest. Derivatives:  sand,  tr.  v.,  sand-ing,  n. sandal,  n.  —  L.  sandalium,  fr.  Gk.  oavSaXtov, dimin.  of  oavSaXov,  a  word  from  Asia  Minor (whence  also  Pers.  sandal),  orig.  meaning  ‘shoe of  the  Lydian  god  Sandal'.  See  Kretschmer, Indogermanische  Forschungen,  45,  270  (1927). sandalwood,  n.  —  ML.  sandalum  (whence  also OF.  sandal),  fr.  Arab,  sandal,  fr.  OI.  candanah, ‘sandalwood’  (lit.  ‘wood  for  burning  incense’), which  is  rel.  to  candrah,  ‘shining,  glowing’,  and cogn.  with  Gk.  zavSapoc,  ‘glowing,  coal’,  L. candere,  ‘to  shine,  glow,  be  white’.  See  candid and  cp.  sanders  and  santal.  Cp.  also  next  word, sandarac,  n.,  1)  the  sandarac  tree;  2)  resin  ob¬ tained  from  this  tree;  3)  realgar.  —  L.  sanda- raca,  fr.  Gk.  aavSapax.T),  which  is  of  Oriental origin.  Cp.  OI.  candra-raga-,  ‘having  the  bright-
33670:ness  of  the  moon’.  The  first  element  of  this  com¬ pound  means  ‘shining,  bright’ ;  see  sandalwood, sandblind.  adj.,  purblind.  —  ME.,  prob.  fr.  OE. *sdm-blind,  ‘half  blind’,  fr.  sdm-,  ‘half’  (see semi-),  and  blind,  adj.  The  alteration  of  the  first element  to  sand  is  due  to  folk  etymology. Derivative:  sandblind-ness,  n. sanderling,  n.,  a  wading  bird  (Crocethia  alba).  — Formed  fr.  sand  with  the  dimin.  suff.  -ling, sanders,  saunders,  n.,  sandalwood  {archaic).  — OF.  sandre,  a  var.  of  sandal.  See  sandalwood, sandia,  n.,  a  watermelon.  —  Sp.,  fr.  Arab,  (bat- tlhd')  sindfyah,  lit.  ‘(the  melon  coming)  from Sind  (India)’.  See  India.
33703:Santa  Claus,  —  American  alteration  of  dial.  Du. Sante  Klaus,  ‘Saint  Nicholas’, santal,  n.,  sandalwood.  —  F.  sanlal,  fr.  Gk. cavvaXov,  fr.  OI.  candanah.  See  sandalwood. Santalaceae,  n.  pi.,  the  sandalwood  family  (bot.) —  ModL.,  formed  with  suff.  -aceae  fr.  ML.  san- talum,  ‘sandalwood’.  See  sandalwood, santalaceous,  adj.  —  See  prec.  word  and  -aceous. santalin,  n.,  a  crystalline  compound  containing  a red  coloring  matter,  C15H1405  ( chem .)  —  F.  san- taline,  fr.  santal.  See  santal  and  -in. santir,  n.,  a  kind  of  dulcimer.  —  Arab,  santir,  fr. Gk.  •jiaA-rrjp'.ov,  ‘stringed  instrument,  psaltery, harp’,  whence  also  Aram.  pesanterin,  pesanterin, ‘a  (triangular)  stringed  instrument’.  See  Psalter. Santolina,  n.,  a  genus  of  plants  of  the  thistle  fam¬ ily  (bot.)  —  ModL.,  fr.  L.  herba  santonica.  See santonica  and  -ina  (representing  L.  -ina). santon,  n.,  a  saint  in  Mohammedan  countries.  — Sp.  santon,  augment,  formed  fr.  santo,  fr.  L. sdnctus ,  ‘holy’.  See  saint, santonica,  n.,  the  European  wormwood.  —  Mod- L.,  fr.  L.  herba  santonica,  'the  herb  of  the  San- toni',  a  people  of  Aquitania.  Cp.  Santolina,  san¬ tonin.
```


## [2026-09-06T15:44:36.731Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN leaf 413 (p.585) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==413' SIN.txt | head -60",
 "description": "Sino-Iranica p.585"
}
```


## [2026-09-06T15:44:37.885Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kundur\\|kunduru\\|Kundur\" SIN.txt | head -20; echo \"=== 552 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==380' SIN.txt | head -50",
 "description": "Grep Sino-Iranica kundur"
}
```


### [2026-09-06T15:44:38.744Z] TOOL RESULT

```
=== SIN leaf 413 (p.585) ===
e  com- mentary (p.  245),  Achundow  cites  also  a  Persian  bih-i  hindl  ("Indian quince"),  and  adds  that  Schlimmer  mentions  merely  a  Cydonia  vulgaris. What  this  Cydonia  indica  is  supposed  to  be  is  a  mystery:  neither  Rox- burgh nor  Watt  knows  such  an  Indian  species.  A.  de  Candolle  already knew  that  there  is  no  Sanskrit  name  for  the  quince.  The  Persian  quince is  mentioned  by  Abu  Mansur  (No.  309)  as  sajarjal  (P.  bih  or  beh,  and  abi).
37(368).  sandal  (Arabic),  Zandan,  Zandal  (Persian),  sandal- wood (Lignum  santalinum).  Red  (from  Pterocarpus  santalinus)  and  white (from  Santalum  album)  are  distinguished.  Skr.  candana.
38(386).  tdlisfar,  alleged  to  be  Myristica  moschata;  on  p.  247,  how- ever, Achundow  withdraws  this  interpretation.  According  to  Daud,  it is  the  bark  of  the  mulberry  coming  from  the  Dekkan.  The  word,  at  all events,  appears  to  be  Indian:  cf.  Skr.  tdlicapattra,  "leaf  of  Flacourtia cataphracta."
39(422).  fulful,  alsofilfil,  black  pepper  (Piper  nigrum).  Skr.  pippall, marica.
40(434).  fufal,  P.  pupal,  areca-nut  palm  (Areca  catechu).  Skr. pugaphala;  Singhalese  puvak.
41(450).  qust,  P.  kust,  Costus  amarus  or  speciosus  (cf.  also  p.  254). Skr.  kustha,  idem  and  Saussurea  lappa.
42(456).  qdqula,  P.  hll4  buzurg,  grains  of  paradise  seeds,  greater  seeds of  cardamom  (Amomum  granum  paradisi,  or  melegueta).
43(457).  qaranful,  P.  mexak,  cloves  (Caryophyllus  aromaticus).  Skr. lavanga.
Indian  Elements  in  Persian  Pharmacology  585
44(459).  quldni,  a  kind  of  barley  brought  from  India.  Jolly  (p.  196) , without  giving  an  Indian  name,  regards  this  as  Glycine  labialis  (Rox- burgh, Flora  Indica,  p.  565) ;  Watt  does  not  give  this  species  for  India. Cf.  No.  572,  where  it  is  described  under  the  name  hdl.
45(480).  kundur,  incense  (Boswellia  thurifera).  Skr.  kunduru, kundura,  kundu,  kunduruka.  Achundow  does  not  mention  a  Persian form  kunduru,  as  asserted  by  Hubschmann  (Armen.  Gram.,  p.  172). Pahlavi  *kunduruk  and  Armenian  kndruk  are  directly  traceable  to  Skr. kunduruka.
46(483).  kafur  (Arabic  and  Persian),  camphor  (Laurus  camphor  a). The  same  word  appears  already  in  Middle  Persian.   Skr.  karpura.
47(512).  Idk,  rdngldk,  lac  (Gummi  laccae).   Cf.  above,  p.  476.
48(517).  mdl,  mungo  bean  (Phaseolus  mungo).  Skr.  mdsa  (Phaseolus radiatus).  This  Indian  word  is  widely  diffused  over  Asia:  Tibetan ma-Sa,  Mongol  mala,  Turki  mas'  ("a  small  kind  of  bean"),  Taranei mat  ("bean"),  Sart  wai  ("lentil"),  Osmanli  mat
49(525).  mulktirdmullr ',  muSktirdmli,  Origanum  dictamnu
```


### [2026-09-06T15:44:40.384Z] TOOL RESULT

```
175:others  of  this  genus,  they  call  salad  (terak  or  tdrak,  Persian  tar  ah). Whatever  is  like  spinning  cotton,  and  others  of  this  genus,  they  call clothing  plants  (jdmak).  Whatever  lentil  (mafag)  is  greasy,  as  sesame, dutedh,  hemp,  vandak  (perhaps  for  zeto,  'olive,'  as  Anquetil  supposes, and  Justi  assumes),  and  others  of  this  genus,  they  call  an  oil-seed (rokano).  Whatever  one  can  dye  clothing  with,  as  saffron,  sapan-wood, zalava,  vaha,  and  others  of  this  genus,  they  call  a  dye-plant  (rag). Whatever  root,  or  gum  (tuf),  or  wood  is  scented,  as  frankincense (Pazand  kendri  for  Pahlavi  kundur),  vardst  (Persian  barghast),  kust, sandalwood,  cardamom  (Pazand  kdkura,  Persian  qaqulah,  'cardamoms, or  kakul,  kdkul,  'marjoram')?  camphor,  orange-scented  mint,  and others  of  this  genus,  they  call  a  scent  (bod).  Whatever  stickiness comes  out  from  plants  they  call  gummy  (vadak).  The  timber which  proceeds  from  the  trees,  when  it  is  either  dry  or  wet,  they call  wood  (Zihd).  Every  one  of  all  these  plants  which  is  so,  they  call medicinal  (ddruk).
740:In  the  Yuan  period  the  Chinese  also  made  the  acquaintance  of mastic,  the  resinous  product  of  Pistacia  lentiscus*  It  is  mentioned  in the  Yin  ia«  leh  yao,  written  in  133 1,  under  its  Arabic  name  mastaki, in  the  transcription  $1  JS  %£  l=f  ma-se-ta-ki.7  Li  Si-cen  knew  only  the medical  properties  of  the  product,  but  confessed  his  ignorance  regarding the  nature  of  the  plant;  hence  he  placed  his  notice  of  it  as  an  appendix to  cummin  {M-lo).  The  Wu  tsa  tolll,  written  in  1610,  says  that mastaki  is  produced  in  Turkistan  and  resembles  the  tsiao  W>  (Zanth- oxylum,  the  fruit  yielding  a  pepper-like  condiment) ;  its  odor  is  very strong;  it  takes  the  place  there  of  a  condiment  like  pepper,  and  is beneficial  to  digestion.8  The  Persian  word  for  "mastic"  is  kundurak (from  kundur,  "incense"),  besides  the  Arabic  loan-word  mastaki  or
1250:Among  the  vegetables  of  India,  Huan  Tsan5  mentions  W  K5  hun-Vo (*hun-da)  ts'ai.  Julien  left  this  term  untranslated;  Beal  did  not  know, either,  what  to  make  of  it,  and  added  in  parentheses  kandu  with  an interrogation-mark.  Waiters6  explained  it  as  "kunda  (properly  the olibanum-tree)."  This  is  absurd,  as  the  question  is  of  a  vegetable  culti- vated for  food,  while  the  olibanum  is  a  wild  tree  offering  no  food.  More- over, hun  cannot  answer  to  kun;  and  the  Sanskrit  word  is  not  kunda, but  kundu  or  kunduru.  The  mode  of  writing,  hun,  possibly  is  intended to  allude  to  a  species  of  Allium.  Huan  Tsan  certainly  transcribed  a Sanskrit  word,  but  a  Sanskrit  plant-name  of  the  form  kunda  or  gunda is  not  known.  Perhaps  his  prototype  is  related  to  the  Iranian  word previously  discussed.
4067:45(480).  kundur,  incense  (Boswellia  thurifera).  Skr.  kunduru, kundura,  kundu,  kunduruka.  Achundow  does  not  mention  a  Persian form  kunduru,  as  asserted  by  Hubschmann  (Armen.  Gram.,  p.  172). Pahlavi  *kunduruk  and  Armenian  kndruk  are  directly  traceable  to  Skr. kunduruka.
5878:kafar  585,  591 kahruba  521 kammun  383 karnab  380 keblr  590 kibrlt  575 kirbas  574 kundur  585 kurkum  321
5937:kunkuma  321         \ kunduru  585 kunkuma  309 kufici,  kuncika  215 kupllu  449 kuberaksl  583 kulafija  545 kustha  463,  464,  584 kusumbha  327 kustumburu  298,  299 ksatrapa  529
6000:kahrupai 521 kaplk  581 kundur  193 kvindurok  585 *kurman  (*gunnan)  385 kulkera  321
=== 552 ===
s  originally  a  secret  Chinese  remedy  formed  with  amlaj (Sanskrit  dmalaka,  Phyllanthus  emblica,  the  emblic  myrobalan).4  It is  the  3$tMWi  an-mo-lo,  *an-mwa-lak,  of  the  Chinese.5  In  Persian  it is  amala  or  amula.
12.  Persian  guli  xaird  (xairu)  is  explained  as  Chinese  and  Persian hollyhock  (Althcea  rosed).6  This  is  the  iw  k'wei  16  l£  ("mallow  of  Se- 6'wan")  of  the  Chinese,  also  called  Zuh  kxwei  ("mallow  of  the  Zun"). It  is  the  common  hollyhock,  which  Stuart7  thinks  may  have  been originally  introduced  into  China  from  some  western  country.
13.  Ibn  al-Baitar8  speaks  of  a  "rose  of  China"  {ward  sini),  usually called  nisrln.  According  to  Leclerc,  this  is  a  malvaceous  plant.  In Persian  we  find  gul-lml  ("rose  of  China"),  the  identification  of  which,
1  The  Herball  or  Generall  Historie  of  Plantes,  p.  317  (London,  1597).
2  Dictionary,  Vol.  VI,  p.  486.
%  Achundow,  Abu  Mansur,  p.  74. 4  E.  Seidel,  Mechithar,  p.  215.
6  Pen  ts'ao  kan  mu,  Ch.  30,  p.  5  b;  Fan  yi  min  yi  tsi,  Ch.  8,  p.  I.  Stuart  (Chinese Materia  Medica,  p.  421)  wrongly  identifies  the  name  with  Spondias  amara.
6  Steingass,  Persian  Dictionary,  p.  1092.
7  Chinese  Materia  Medica,  p.  33.
8  Leclerc,  Traite"  des  simples,  Vol.  Ill,  pp.  369,  409.
552  Sino-Iranica
judging  from  what  Steingass  says,  is  not  exactly  known.  The  Arabic author,  further,  has  a  $ah-slm  ("Chinese  king"),  described  as  a  drug in  the  shape  of  small,  thin,  and  black  tabloids  prepared  from  the  sap of  a  plant.  It  is  useful  as  a  refrigerant  for  feverish  headache  and  in- flamed tumors.  It  is  reduced  to  a  powder  and  applied  to  the  diseased spot.1  Leclerc  annotates  that,  according  to  the  Persian  treatises,  this plant  originating  from  China,  as  indicated  by  its  name,  is  serviceable for  headache  in  general.  DimaSkI,  who  wrote  about  1325,  ascribes lah-llnl  to  the  island  of  Cankhay  in  the  Malayan  Archipelago,  saying that  its  leaves  are  known  under  the  name  "betel."2  Steingass,  in his  Persian  Dictionary,  explains  the  term  as  "the  expressed  juice  of a  plant  brought  from  China,  good  for  headaches."  I  do  not  know  what plant  is  understood  here.
14.  According  to  Ibn  al-Baitar,  the  mango  (Arabic  anba)  is found  only  in  India  and  China.3  This  is  Mangifera  indica  (family Anacardiaceae) ,  a  native  of  India,  and  the  queen  of  the  Indian  fruits, counting  several  hundreds  of  varieties.  Its  Sanskrit  name  is  antra, known  to  the  Chinese  in  the  transcription  ^  M  an-lo,  *am-la(ra). Persian  amba  and  Arabic  anba  are  derived  from  the  same  word.  During the  T'ang  period  the  fruit  was  grown  in  Fergana.4  Malayan  manga (like  our  mango)  is  based  on  Tamil  mangas,  and  is  the  foundation
```


## [2026-09-06T15:44:54.869Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Zandal\\|candana\\|santalinum\\|sandal-\\|sandalwood\" SIN.txt | head -20",
 "description": "Grep SIN for sandal"
}
```


### [2026-09-06T15:44:54.911Z] TOOL RESULT

```
175:others  of  this  genus,  they  call  salad  (terak  or  tdrak,  Persian  tar  ah). Whatever  is  like  spinning  cotton,  and  others  of  this  genus,  they  call clothing  plants  (jdmak).  Whatever  lentil  (mafag)  is  greasy,  as  sesame, dutedh,  hemp,  vandak  (perhaps  for  zeto,  'olive,'  as  Anquetil  supposes, and  Justi  assumes),  and  others  of  this  genus,  they  call  an  oil-seed (rokano).  Whatever  one  can  dye  clothing  with,  as  saffron,  sapan-wood, zalava,  vaha,  and  others  of  this  genus,  they  call  a  dye-plant  (rag). Whatever  root,  or  gum  (tuf),  or  wood  is  scented,  as  frankincense (Pazand  kendri  for  Pahlavi  kundur),  vardst  (Persian  barghast),  kust, sandalwood,  cardamom  (Pazand  kdkura,  Persian  qaqulah,  'cardamoms, or  kakul,  kdkul,  'marjoram')?  camphor,  orange-scented  mint,  and others  of  this  genus,  they  call  a  scent  (bod).  Whatever  stickiness comes  out  from  plants  they  call  gummy  (vadak).  The  timber which  proceeds  from  the  trees,  when  it  is  either  dry  or  wet,  they call  wood  (Zihd).  Every  one  of  all  these  plants  which  is  so,  they  call medicinal  (ddruk).
1368:The  last  clause  means  that  the  plant  i,s  propagated  from bulbs.  There  is  a  much  earlier  tribute-gift  of  saffron  on  record.  In a.d.  519,  King  Jayavarman  of  Fu-nan  (Camboja)  offered  saffron  with storax  and  other  aromatics  to  the  Chinese  Court.1  Accordingly  we  have to  assume  that  in  the  sixth  century  saffron  was  traded  from  India  to Camboja.  In  fact  we  know  from  the  T'ang  Annals  that  India,  in  her trade  with  Camboja  and  the  anterior  Orient,  exported  to  these  coun- tries diamonds,  sandal-wood,  and  saffron.2  The  T'ang  Annals,  further, mention  saffron  as  a  product  of  India,  Kashmir,  Uddiyana,  Jagucja, and  Baltistan.3  In  a.d.  719  the  king  of  Nan  (Bukhara)  presented thirty  pounds  of  saffron  to  the  Chinese  Emperor.4
2719:1  Cen  lei  pen  ts'ao,  I.  c.  This  tree  is  mentioned  in  the  Ku  kin  lu  (Ch.  c,  p.  I  b, as  a  product  of  Fu-nan,  and  by  Cao  Zu-kwa  as  a  variety  of  sandal-wood  (Hirth) Chao  Ju-kua,  p.  208).  Li  Si-6en  (Pen  ts'ao  kan  mu,  Ch.  34,  p.  12)  says  that  the people  of  Yun-nan  call  tse  Van  by  a  peculiar  word,  $f£  Sen;  this  is  pronounced  sen in  Yun-nan,  and  accordingly  traceable  to  a  dialectic  variation  of  landan,  sandan, sandal.   The  Japanese  term  is  Ulan  (Matsumura,  No.  2605).
3676:15.  Isak  Ibn  Amran  says,  "Sandal  is  a  wood  that  comes  to  us  from China."6  Santalum  album  is  grown  in  Kwan-tun  to  some  extent,  but  it is  more  probable  that  the  sandal-wood  used  in  western  Asia  came  from India  (cf.  Persian  Zandan,  Zandal,  Armenian  candan,  Arabic  sandal, from  Sanskrit  candana).
4058:37(368).  sandal  (Arabic),  Zandan,  Zandal  (Persian),  sandal- wood (Lignum  santalinum).  Red  (from  Pterocarpus  santalinus)  and  white (from  Santalum  album)  are  distinguished.  Skr.  candana.
5941:candana  552,  584 camara  565 clnaka  595 cinanl  540 cinarajaputra  540 cobaclnl  556
```


## [2026-09-06T15:44:56.737Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kand-\\|(s)kand\\|kend-\" AHD_watkins1985.txt | head -20; echo \"=== sandarac AHD ===\"; grep -n \"sandarac\\|candela\\|candidus\" AHD_watkins1985.txt | head",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-06T15:44:56.804Z] TOOL RESULT

```
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
934:*sua-yo-, contracted to *si-yo- in Greek huein, to rain, and huetos, rain: ISOHYET. II. Possible extended zero-grade form *sib-. 1.Germanic *sip- in: a. Old English sipan, sipian, to drink, sip: suP!; b. Old French soup(e), soup: SOUP, (SUP2). 2. Germanic “supp- in: a. Old English sopp, bread dipped in liquid: sop; b. possibly Low German sippen, to sip, probably akin to the source of Middle English sippen, to sip: stp. III. Possible ex- tended zero-grade form “sig-. 1. Germanic *sik- in Old English sican, to suck: sucK. 2. Germanic shortened form *sukdn in Old English socian, to steep: SOAK. 3. Latin siigere, to suck: SUCTION, SUCTORIAL. 4, Variant form *sik- in Latin siicus, succus, juice: SUCCULENT. [Pok. 1. seu- 912.] seut-. To seethe, boil. 1. Germanic *seuthan in Old English séothan, to boil: SEETHE, (SODDEN). 2. Germanic *suth- in: a. Middle Dutch sudde, sudse, marsh, swamp: sups; b. suffixed form *suth-l- in Middle High German sudelen, to soil, do sloppy work, akin to Middle Dutch soetler, sutler: SUTLER. [Pok. 4. seu- 914.] si-lo-. Silent. Suffixed (stative) form *si/-é- in Latin silére, to be silent: SILENT. [In Pok. 2. sé(i)- 889.] skabh-. To prop up, support. Suffixed form *skabh-no- in Latin scamnum, a bench (> Old English sceamel, table, stool): SHAMBLES. [Pok. skabh- 916.] skai-. Also kai-. Bright, shining. 1. Extended form *kaid- in Germanic *haiduz, “bright appearance,” manner, quality, in Old English -hdd, quality, condition: -Hoop. 2. Suffixed form *ki-t-ro- in Sanskrit citra-, variegated, many-colored: CHEETAH, CHINTZ. [Pok. (s)kdi- 916.] [skalkaz. Servant, slave. Germanic noun of unknown origin. 1. Old High German compound marahscalc, “horse-servant” (see marko-). 2. Germanic compound *sini-skalkaz, “old servant” (see sen-'). [In Pok. (s)kel- 929.]] skamb-. Also kamb-. To curve, bend. Suffixed form *kamb-o- in Celtic *kambo-, crooked, and denominative verb *k(a)mb-yo-, to turn, exchange, whence Gallo-Latin cambidre, to exchange: CAMBIST, CAMBIUM, CHANGE. [Pok. (s)kamb- 918.] skand-. Also skend-. To leap, climb. 1. Latin scandere, to climb: SCAN, SCANDENT, SCANSION, SCANSORIAL; AS- CEND, (CONDESCEND), DESCEND, TRANSCEND. 2. Suffixed form *skand-alo- in Greek skandalon, a snare, trap, stumbling block: SCANDAL. 3. Suffixed form *skand-sld- in Latin scdlae, steps, ladder: ECHELON, ESCALADE, SCALE?. sked-. To split, scatter. Extension of sek-. 1. O-grade form *skod- in Germanic *skaé- in Old English *sc(e)ater- ian, to scatter: SHATTER. 2. Variant nasalized form *ska-n-d- in Latin scandula, a shingle for roofing (< “split piece”): SHINGLE}. [Pok. (s)k(hjed- 918.] skeei-. To gleam. 1. Suffixed form “ske(ji-no- in Ger- manic *skinan, to gleam, shine, in: a. Old English scinan, to shine: SHINE; b. Old High German scinan, to shine: GEGENSCHEIN. 2. Germanic extended form *ski-m- in Old English scimerian, scymrian, to shine brightly: SHIM- MER. 3. Possibly suffixed form *ski-nto-, shining, in Latin scintilla, a spark: SCINTILLA, SCINTILLATE, STEN- CIL, (TINSEL). 4. Suffixed zero-grade form *skia-G-, *skiy-d- in Greek skia, shadow: SKIAGRAM, SKIASCOPE, SQUIRREL. [Pok. skai- 917.] skei-. To cut, split. Extension of sek-. 1. Germanic suffixed form *ski-nd- in: a. Old English scinu, shin, shinbone (< “piece cut off’): SHIN!-; b. Old French eschine, backbone, piece of meat with part of the back- bone: CHINE, 2, Latin scire, to know (< “to separate one thing from another,” “discern”): SCIENCE, SCILICET, SCIOLISM, SCIRE FACIAS; ADSCITITIOUS, CONSCIENCE, CONSCIOUS, NESCIENCE, (NICE), OMNISCIENT, PLEBI- SCITE, PRESCIENT. 3. Suffixed zero-grade form *skiy-end in Old Irish scian, knife: SKEAN. 4. Extended root *skeid- in: a. Germanic *skitan, to separate, defecate, in Old English *scitan, to defecate: SHIT; b. suffixed zero-grade
1262:ART? er-1 ARTEL ar- ARTERIO- wer-2 ARTERIOLE wer-2 ARTERY wer-2 ARTHRO- ar- ARTHUR rtko- ARTICLE ar- ARTIFACT dhé-1 ARTIFICE dhé-1 ARTIODACTYL ar- ARTISAN ar- ARTIST ar- ARYAN aryo- ASBESTOS gWes- ASCEND skand- ASCRIBE skribh- ASH! as-
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1674:IN-2 en INAMORATA amma INAUGURATE aug-! INCANDESCE kand- INCANTATION kan- INCARCERATE cGarcer INCARNATE sker-1 INCENDIARY kand- INCENSE kand- INCENTIVE kan- INCEPTION kap- INCERTITUDE krei- INCEST kes-2 INCH! i-no- INCHOATE kagh-
2222:SCAB skep- SCABBARD sker-1 SCABBLE skep- SCABIES skep- SCABROUS_ skep- SCAGLIOLA skel-1 SCALD! kele-1 SCALE! skel-1 SCALE? skand- SCALE’ skel-1 SCALENE skel-! SCALL_ skel-!
2223:SCALP skel-1 SCALPEL skel-1 SCAN skand- SCANDAL skand- SCANDENT skand- SCANSION skand- SCANSORIAL skand- SCANT kem-1 SCAPHOID skep- SCAPULA skep-, sker-1 SCAR? sker-1 SCARCE kerp- SCARIFY!  skribh- SCARP_ sker-! SCATHE skét(o)- SCATO- sker-4 SCAVENGER keu-! SCENT sent- SCHADENFREUDE preu-, skét(e)- SCHEME segh- SCHERZO sker-2 SCHILLER skel-3 SCHIPPERKE skipam
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
=== sandarac AHD ===
```


## [2026-09-06T15:45:12.269Z] TOOL CALL #16: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:45:12.274Z] TOOL RESULT

```


```


## [2026-09-06T15:45:13.946Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT sandal ===\"; grep -n \"sandal\" SKT.txt | head -5",
 "description": "Grep Skeat sandal"
}
```


### [2026-09-06T15:45:14.008Z] TOOL RESULT

```
=== SKT sandal ===
16466:Sandal,  shoe.  (,F.-L.-Gk.)  F.  $an dale.  ^  L.  jandalium.  *  Gk.  awbaXiov, dimin.  of  aavioKov,  a  wooden  sole  bound on  to  the  feet  with  straps.  Cf.  Fers.  sandal, a  saiidal.
17740:60II  (t),  ground,  country.  (F  —  L.) M.  E.  W/r.— O.  F.  j«/,  sue/,  Uter  /NriV. threshold  of  a  door.— Late  L..  io//a  soil, ground  i^by  confusion  with  L.  tofum, ground) ;  L.  soUa,  a  sandal,  sole,  timbei  on which  wattled  walls  are  built.  Allied  to L.  solum^  ground ;  whence  F.  sol,  soil, ground  1  from  whidi.  however,  the  £.  word cannot  be  directly  derived).
23648:French  from   Persian  from lake  (a^,  sandal  (wood).
```


## [2026-09-06T15:45:21.507Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /Sandal,  shoe/{print NR}' SKT.txt\necho \"=== KLN leaf of sandalwood/sandarac line 33668 ===\"\nawk 'BEGIN{RS=\"\\f\"} /sandalwood,  n\\./{print NR}' KLN_1966.txt\nawk 'BEGIN{RS=\"\\f\"} /candidate,  n\\.|fr.  candere,  ‘to  shine,  glow,  be  white/{print NR}' KLN_1966.txt | head",
 "description": "Find leaf numbers in SKT and KLN"
}
```


## [2026-09-06T15:45:23.267Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['KLN','SKT','TAD','ARK','SIN']:\n    v=d[k]; print(k, '|', v.get('page_offset'), '|', v.get('lookup_hint'))\n\"",
 "description": "Page offsets for KLN SKT TAD"
}
```


### [2026-09-06T15:45:24.137Z] TOOL RESULT

```
440
=== KLN leaf of sandalwood/sandarac line 33668 ===
734
133
```


### [2026-09-06T15:45:26.389Z] TOOL RESULT

```
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
TAD | 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
ARK | None | Not found.
SIN | leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.
```


## [2026-09-06T15:45:34.554Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT leaf 440 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==440' SKT.txt | head -8\necho \"=== SKT leaf 439/441 first lines ===\"; awk 'BEGIN{RS=\"\\f\"} NR==439||NR==441{print NR\": \"substr($0,1,200)}' SKT.txt",
 "description": "Inspect SKT leaf 440"
}
```


## [2026-09-06T15:45:36.087Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN leaf 734 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==734' KLN_1966.txt | head -5\necho \"=== KLN leaf 133 head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==133' KLN_1966.txt | head -5",
 "description": "Inspect KLN leaves"
}
```


### [2026-09-06T15:45:36.356Z] TOOL RESULT

```
=== SKT leaf 440 head ===
r  $aitjelar,  where  telar  is  an for  'sall-hohkr;'  so  that  the be  saii  is  superfluous.  O.  F.  saliere, tp.Il->ellrr  ; '  Cot.  •>  L.  salarium,  salt- Ir  (to  late  L.) ;  from  L.  salarius.  adj.. ^ng  lo  salt*L.jay,salL  See  salary fw). t-petro,  nitre.  (E.;  am/ F.  —  L.  aku/ Fnt  for  OF.  sal/tstrr,  «It.petre •  L,  taJ  f^ir^,  salt  of  the  rock. tai,  aalli   Gk.  Wr^,    a  rock;    sec
(F.  M  L.)     F.  id«£/.  »  L.  salsa, ttlted}    fem.  of  Misus,  salted.
See  Batt.  Der.  satu-er,  orig.  a  ves«el for  sauce  ;  sauc-y,  full  of  sauce,  pu'  genl.
sausage.  (F.  — L.)  F.  jawtnj^.  — Low L.  sakitia.  L.  salsuium,  a  sausnge,  of salted  or  seasoned  meat.  — L.  sahus,  salted.
—  L.  sal,  salt.
Sonne,  pickle.  (F.  —  L.)  Merely  an other  spelling  of  itauoe  (above).  Hence sousi,  vo.f  to  immerse,  orig.  to  plunge  in brine.
Saltation.  8altlre ;  see  Salient.
Salubrious,  Salutary.  Saluto,  Sal- va^ ;  see  Salvation.
=== SKT leaf 439/441 first lines ===
439: lient.  (L.)  From  prcs.  pt.  of  L. fa/ire,  to  leap,  spring  forward.  Allied  to Skt.  srit  to  6ow,  sari,  waterfall,  Gk.  &AAo- >«K.  Heap.     (V'SAK.)
assail.  (F.  -  L.)  O.  F.  assa
441: nguintus^  adj.,  from  san^tM;  stem  of jangttis,  blood.
ooiisang:uineou8.  (L.)  L.  (msam- guineus,  related  by  blood.  — L.  <wt-  (cum), together;  san^in-,  stem  oi san^is,  blood.
Sanhed
```


### [2026-09-06T15:45:37.976Z] TOOL RESULT

```
=== KLN leaf 734 head ===
s’,  fr.  Samnium,  which  prob.  stands for  *Sabniom  and  is  rel.  to  Sabinus,  ‘Sabine’. See  Sabine  and  subst.  suff.  -ite.
Samoan,  adj.,  pertaining  to  Samoa;  n.,  an  inhabi¬ tant  of  Samoa.  —  Formed  with  suff.  -an  fr. Samoa,  name  of  a  group  of  islands  in  Polynesia. Derivative :  Samoan,  n.,  an  inhabitant  of  Samoa. Samolus,  n.,  a  genus  of  plants,  the  brookweed (bot.)  —  L.  samolus,  ‘brookweed’,  prop,  ‘a  sum¬ mer  plant’,  fr.  Gaul.  *samos,  ‘summer’,  whence also  L.  samauca,  name  of  a  fish.  Cp.  samara, samovar,  n.,  a  Russian  tea  urn.  —  Fr.  Tatar  sana- bar,  ‘tea  urn’,  altered  by  folk  etymology  into Russ,  samovar,  ‘self-boiler’,  fr.  samo,  ‘self’,  and varit',  ‘to  boil’.
Samoyed,  Samoyede,  n.  and  adj.,  name  of  a  Si¬ berian  people.  —  Russ.  Samoyed,  lit.  ‘self¬ eaters’,  used  in  the  sense  of  cannibals,  a  name given  them  by  the  Russians  (the  native  name  of the  people  is  Nenets).  For  the  first  element  in Samoyed  see  same.  The  second  element  is  cogn. with  Gk.  28siv,  L.  edere,  Goth,  itan,  OE.  elan, ‘to  eat’ ;  see  eat.
sampan,  n.,  a  light  Chinese  boat.  —  Fr.  Chin,  san pan,  ‘three  boards’.
samphire,  n.,  1)  the  plant  Crithmum  maritimunv, 2)  the  glasswort.  —  Fr.  earlier  sampere,  sampire, fr.  F.  (herbe  de)  Saint  Pierre,  ‘St.  Peter’s  herb’. The  actual  French  names  of  the  plant  are  perce- pierre,  passe-pierre,  christe-marine. sample,  n.  —  ME.  sample,  aphetic  for  asaumple, fr.  OF.  essample ,  fr.  L.  exemplum.  See  example and  cp.  cnsample.
=== KLN leaf 133 head ===
n or  index  (of  the  sundial)’,  OL.  gnoscere,  L.  nds- cere,  ‘to  know’,  Alb.  heh,  ‘you  know’  (sing.), hoh,  ‘I  know’,  OSlav.  znajq,  znati,  Lith.  iinaii, zinoti,  ‘to  know’,  OPruss.  po-sinna,  ‘I  confess’, OIr.  ad-gninim,  T  know,  recognize  ,  gndth, ‘known,  accustomed’,  W.  gnawd,  ‘custom’.  See know  and  cp.  canny,  con,  ‘to  peruse’,  could, cunning,  keen,  ken,  ‘to  know’,  ken,  ‘range  of sight’,  kith,  kithe,  uncouth.  Cp.  also  acquaint, agnoiology,  cognition, diagnosis, gnome, ‘maxim  , gnomic,  gnomon,  gnosis,  gnostic,  ignoble,  ignore, incognito,  jnana,  narrate,  noble,  normal,  note, notice,  notion,  notorious,  quaint,  recognize, reconnoitre.
can,  n.,  vessel.  —  ME.  canne,  fr.  OE.  canne,  rel. to  OS.,  ON.,  Swed.  kanna ,  MDu.  kanne.  Du. kun,  OHG.  channa,  MHG.,  G.  kanne,  ‘can’, borrowed  fr.  L.  canna,  ‘reed,  cane;  small  vessel, tube’,  which  is  of  Sem.  origin.  See  cane  and cp.  canal.
Derivatives:  can,  tr.  vM  to  put  into  a  can,  cann¬ ed,  adj.,  cann-er ,  n.,  cann-er\\  n.,  cann-ing,  n. Canaan,  n.,  the  Promised  Land  of  the  Israelites. —  L.  Chanaan ,  fr.  Gk.  Xavadtv,  fr.  Heb.  Kf-
canaba
na'an,  which  is  of  unknown  origin.
```


## [2026-09-06T15:46:01.516Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 700 703 706 710 720 730 733; do echo \"--- leaf $n: $(awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | head -2 | tr '\\n' ' ' | cut -c1-110)\"; done",
 "description": "Check KLN leaf alphabetical positions"
}
```


### [2026-09-06T15:46:03.605Z] TOOL RESULT

```
--- leaf 700: ler  (F.  reconcilier),  fr.  L.  reconciliare,  ‘to  bring together  again,  reconcile',  fr.  re-  and  co
--- leaf 703: tablishment  of  Protestantism  in  the  1 6th cent.  —  See  prec.  word. re-formation,  n.,  a  new  forma
--- leaf 706: ’,  fr. rilevare,  'to  raise’,  fr.  L.  relevare.  See  next  word and  cp.  prec.  word  and  relievo, 
--- leaf 710: uisitus,  pp.  of  requirere.  See  require  and  -ion. Derivatives:  requisition,  tr.  v.,  requisition-ary,
--- leaf 720: y’.  See  retard, rite,  n.,  a  ceremonial  act.  —  ME.,  fr.  L.  ritus, ‘religious  custom,  usage, 
--- leaf 730: onsecration.  —  ME.,  verbal  noun  of sacren,  ‘to  consecrate’.  See  sacred  and  -tag,  suff. formi
--- leaf 733:   fr.  OF.  saluta- cion  (F.  salutation),  fr.  L.  salutationem,  acc. of  saliitatio,  fr.  salutatus,  pp
```


## [2026-09-06T15:46:13.256Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt)\"\nawk 'BEGIN{RS=\"\\f\"} NR==900{print substr($0,1,120)}' KLN_1966.txt\ngrep -on \"[0-9]\\{3,4\\}  *SANDAL\\|^1380\\|1380\" KLN_1966.txt | head -5",
 "description": "KLN total leaves"
}
```


### [2026-09-06T15:46:14.995Z] TOOL RESULT

```
leaves: 903
  F.)  veine,  fr.  L. vena,  ‘blood  vessel,  watercourse,  vein;  natural inclination',  which  is  of  uncertain  o
33669:1380
```


## [2026-09-06T15:46:20.353Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33660,33675p' KLN_1966.txt | cut -c1-300\necho \"=== candid area ===\"; sed -n '6330,6345p' KLN_1966.txt | cut -c1-300",
 "description": "Show KLN page markers"
}
```


### [2026-09-06T15:46:20.437Z] TOOL RESULT

```
make  holy’,  fr.  L.  sdnctus ,  ‘holy’,  and  -ficdre,  fr. facere,  ‘to  make,  do’;  see  saint  and  -fy.  E. sanctify  was  influenced  in  form  by  Late  L. sanctificare.
sanctimony,  n.,  hypocritical  devoutness.  —  MF. sanctimonie,  fr.  L.  sanctimonia,  ‘sacredness, sanctity,  piety’,  fr.  sdnctus,  ‘holy,  sacred’.  See saint.  For  the  ending  see  suflf.  -mony  and  cp. words  there  referred  to.
Derivatives:  sanctimonious-ly,  adv.,  sanctimo- nious-ness,  n.
sanction,  n.  —  L.  sanctio,  gen.  -onis,  ‘the  decree¬ ing  of  something  as  sacred,  decree,  sanction’ (prob.  through  the  medium  of  F.  sanction), fr.  sdnctus,  pp.  of  sancire.  See  saint  and  -ion. Derivatives:  sanction,  tr.  v.,  sanction-ary,  adj., sanction-er,  n.
sanctitudc,  n.,  saintliness  {rare).  —  ME.  sanctitud, fr.  L.  sanctitiidd  fr.  sdnctus,  ‘holy,  sacred’.  See
saint  and  -tude.
sanctity,  n.,  sacredness.  —  ME.  sauncite,  fr.  MF. saintete,  sainctete  (F.  saintete),  fr.  L.  sanctita- tem,  acc.  of  sanctitas,  ‘holiness,  sacredness’,  fr. sdnctus,  ‘holy,  sacred’.  See  saint  and  -ity. sanctuary,  n.  —  ME.  sanctuarie,  fr.  MF.  sainc- tuarie,  s
Sanctus,  n.,  the  hymn  beginning  with  the  word Sanctus.  —  L.  sdnctus,  ‘holy’,  the  rendering  of Heb.  qadhosh  (in  Is.  6 : 3).  See  saint. sand,n. —  ME.  sond,  sand,  fr.  OE.,  rel.  to  OS.  sand, ON.  sandr,  Dan.,  Swed.  sand,  OFris.  sond,  MDu. sant,  ‘sand’,  Du
rub,  rub  away;  to  crumble  away'.  See  psilo- and  cp.  ammo,  psammite,  psephism,  sabulous, saburra  and  the  second  element  in  palimpsest. Derivatives:  sand,  tr.  v.,  sand-ing,  n. sandal,  n.  —  L.  sandalium,  fr.  Gk.  oavSaXtov, dimin.  of  oavSaXov,  a  word  from  Asia  Mino
1380'
ness  of  the  moon’.  The  first  element  of  this  com¬ pound  means  ‘shining,  bright’ ;  see  sandalwood, sandblind.  adj.,  purblind.  —  ME.,  prob.  fr.  OE. *sdm-blind,  ‘half  blind’,  fr.  sdm-,  ‘half’  (see semi-),  and  blind,  adj.  The  alteration  of  the  first el
sandiver,  n.,  glass  gall.  —  ME.  saundiver,  popular alteration  of  F.  suin  (now  spelled  suint)  de  verre, ‘sandiver’,  lit.  ‘sweating  of  glass”.  F.  suin  is  a derivative  of  suer,  ‘to  sweat,  perspire’,  fr.  L. siiddre;  see  sudation.  F.  de,  ‘of,  from’,  
Derivatives:  sand-i-ness,  n.,  sand-y-ish,  adj. Sandy,  n.,  nickname  for  a  Scotsman.  —  From Sandy,  Scott,  abbreviation  of  Alexander.  Cp. Sawney.
sane,  adj.  —  L.  sdnus,  ‘sound,  whole,  healthy’, rel.  to  Umbr.  sanes  {=  L.  sanis,  abl.  pi.);  of uncertain  etymology.  Cp.  sanative,  sanatorium, sanicle,  sanitary,  and  the  second  element  in tutsan  and  in  vesania.
Derivatives:  sane-ly,  adv.,  sane- ness,  n. sanforize,  tr.  v.,  to  preshrink  (a  cotton  or  linen fabric)  permanently.  —  Named  after  the  Amer¬ ican  Sanford  Lockwood  Cluett  (born  in  1874), inventor  of  this  process.  For  the  ending  see  suff. -ize.
sang,  past  tense  of  sing.  —  ME.,  fr.  OE.  sang. See  sing.
=== candid area ===
cancellate,  adj.,  marked  with  crosslines.  —  L. cancellatus,  pp.  of  cancellare.  See  prec.  word and  adj.  suff.  -ate.
Derivatives:  cancellat-ed,  adj.,  cancellat-ion,  n. cancellous,  adj.,  having  a  spongelike  structure (said  of  the  spongy  part  of  bones).  —  Formed with  suff.  -ous  fr.  L.  cancelli  (pi.),  ‘lattice’.  See
cancel.
cancer,  n.,  a  malignant  growth.  —  L.,  ‘crab,  ul¬ cer,  cancer’,  dissimilated  fr.  *carcro-  and  cogn. with  Gk.  xxpxlvos,  ‘crab’,  lit.  ‘the  animal  with the  hard  shell’,  fr.  I.-E.  base  *qarq-,  *qraq-,  ‘to be  hard’,  whence  also  OI.  karkatakt,  karkah, �
Derivatives ;  cancer-ous ,  adj.,  cancer-ous-ly ,  adv., cancer-ous-ness,  n.
cancriform,  adj.,  crablike.  —  Compounded  of L.  cancer,  gen.  cancri,  ‘crab’,  and  forma,  ‘form, shape'.  See  cancer  and  form,  n. cancroid,  adj.,  like  a  crab;  like  a  cancer.  —  A hybrid  coined  fr.  L.  cancer,  gen.  cancri,  ‘crab’, and  Gk.  -ostS^g,  ’like�
candelabrum,  also  candelabra,  n.,  a  branched candlestick.  —  L.  candelabrum,  ‘candlestick’, fr.  candela.  See  candle  and  cp.  chandelier, candent,  adj.,  glowing,  white.  —  L.  candens,  gen.
-entis,  pres.  part,  of  candere.  See  candescent, candescence,  n.  —  Formed  fr.  next  word  with  suff. -ce.
candescent,  adj.,  glowing.  —  L.  candescens,  gen. -entis,  pres.  part,  of  candescere,  ‘to  begin  to glow’,  inchoative  of  candere,  ‘to  shine,  glow’, whence  also  candidus,  ‘glowing,  white’.  See  next word  and  -escent,  and  cp.  incandesce. Derivative r  candescent
upright',  fr.  candere,  ‘to  shine,  glow,  be  white  , which  is  cogn.  with  Gk.  xavSapo;,  ‘glowing coal’,  OI.  candrah,  ‘shining  glowing’,  candana ‘sandalwood’  (lit.  ‘wood  for  burning  incense’). Alb.  Gheg  hqne,  Tosk  hene,  ‘moon’  (lit.  ‘the white  one�
Derivatives:  candid-ly,  adv.,  candid-ness,  n. candidate,  n.,  one  who  seeks  an  office,  etc.  —  L. candidatus,  ‘one  aspiring  to  office’,  prop.  pp.  of candidare,  ‘to  make  bright  or  white’,  fr.  can¬ didus,  ‘glowing,  white’ ;  so  called  because  a  can¬ didat
Derivative:  candidat-ure,  n. candle,  n.  —  ME.  candel,  fr.  OE.  candel,  fr.  L. candela,  ‘candle  made  of  wax  or  tallow’,  fr. candere,  ‘to  shine,  glow,  burn’.  See  candid  and cp.  candelabrum,  chandelier,  chandler. Candlemas,  n.  —  ME.  candelmasse,  fr.  OE.  can
candy,  n.,  crystallized  sugar.  —  Shortened  fr. sugar  candy,  fr.  F.  (sucre)  candi,  fr.  It.  (zucchero) candi(to),  ‘sugar  candy’,  fr.  Arab,  qandi,  ’crys¬ tallized,  candied’,  adj.  formed  fr.  qand,  ‘cane sugar',  which,  like  OI.  khandakah ,  ‘candy  ,  is prob.
cane,  n.  —  ME.  cane,  canne,  fr.  OF.  cane,  canne (F.  canne),  fr.  OProveng.  carta,  fr.  L.  canna, ’reed,  cane,  small  vessel,  tube',  fr.  Gk.  xxvva, ’reed’,  which  is  of  Sem.  origin.  Cp.  Akkad. qanu,  Heb.  qaneh,  Aram.-Syr.  qanyO,  Arab. qanAh  (whence  Pers.  qana
nikin,  canon,  ‘rule’,  canonical,  canyon,  and  the first  element  in  canephorus,  caramel.
Derivatives:  cane,  tr.  v.,  can-er,  n.,  can-ing,  n. caneila,  n.,  cinnamon.  —  ML.,  dimin.  of  L.  can¬ na,  ‘reed,  cane’.  See  cane  and  -ella. canephorus,  n.,  a  basket  bearer  (Greek  antiq.)  — L.,  fr.  Gk.  xav7)96poc,  ‘basket  bearing’,  com¬ pounded  of  xxveov
```


## [2026-09-06T15:46:32.724Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=6300 && NR<=6345 && /^[0-9]{2,4}[^A-Za-z]*$/{print NR\": \"$0}' KLN_1966.txt\necho \"=== TAD sandarus ===\"; grep -n \"سندروس\\|صندروس\\|سنداروس\" TAD_pages.txt | head\necho \"=== TAD qandil ===\"; grep -n \"قنديل\\|قندیل\" TAD_pages.txt | head",
 "description": "KLN page number and TAD greps"
}
```


### [2026-09-06T15:46:34.578Z] TOOL RESULT

```
6325: 230
=== TAD sandarus ===
1459:‫وهو صمخ ير ينضح ووش أشهار‬              ‫مسندروس ‪ -‬ووناني ‪121‬‬
=== TAD qandil ===
2271:   ‫عمعناه شمعة يستضاء مهامرادفه مصصباح وسراج‬            ‫قنديل ‪ -‬لانيى ‪84‬‬
```


## [2026-09-06T15:46:44.396Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1459 && /\\[pdf page/{p=$0; n=NR} END{}' TAD_pages.txt\nawk 'NR<=1459 && /pdf page/{p=$0} END{print \"before 1459: \"p}' TAD_pages.txt\nawk 'NR<=2271 && /pdf page/{p=$0} END{print \"before 2271: \"p}' TAD_pages.txt\necho \"--- context 1455-1465 ---\"; sed -n '1450,1465p' TAD_pages.txt\necho \"--- context 2265-2275 ---\"; sed -n '2265,2276p' TAD_pages.txt",
 "description": "TAD page tags and context"
}
```


### [2026-09-06T15:46:46.289Z] TOOL RESULT

```
before 1459: 
before 2271: 
--- context 1455-1465 ---
‫اللاتينية طتصدة مأخوذ من « سنبك » الفارسي الذي معناه طرف الحافر وقد‬
                     ‫يطلق على سفينة صخيرة سميت به لصغرها مرادفه _سبارة‬
                           ‫سئحة ‏ فارسي « سنجه ‪ 4‬معناه عبار المعزان‬

‫منجاب ‪ -‬في الفارسية _سنجاب وفي اليونانية ‪507‬ناهأ!ة وتميه العامة‬
                                                                 ‫قرقدون‬
 ‫منجق ‪ -‬فالينارسية سنجاق وافليتركية سنجاق وفي اليوثانية ‪0016765‬‬
                                        ‫معثاه سمه رمأدفه أواء وعدم ورابة‬
            ‫سندان ‪ -‬في الفارسية ‪ 2‬سندان »© وفي الارامية ‪ 9‬سدانا »‬
‫وهو صمخ ير ينضح ووش أشهار‬              ‫مسندروس ‪ -‬ووناني ‪121‬‬
                       ‫افريقية ويطلق أيضا على رب من المعدن أحمر الاون‬
 ‫لنهما‬
     ‫ينعنلاتنعكا‬
               ‫ولانيني تسطن‪1‬لهاصذة وهو ال‬   ‫ابو ناني ‪0-2‬‬        ‫دل‬

                                      ‫الاقدمون قبل اختراع الحف والحذاء‬
--- context 2265-2275 ---
                                                                   ‫بنيان القناطر‬
                                      ‫د‬    ‫سابةاجم‬




   ‫عمعناه شمعة يستضاء مهامرادفه مصصباح وسراج‬            ‫قنديل ‪ -‬لانيى ‪84‬‬
                                                                              ‫‪1‬‬     ‫‪01‬‬

‫قعل ‪ 5‬ب لاتيبى امه معثاه مشتكاد وراد به فى زماننا تمثل الدولة‬

              ‫«الالنةرعاتون معناه مئوي من «اتاأهعء مائة‬            ‫قنطار لاتينى‬
```


## [2026-09-06T15:46:58.055Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\nt=open('TAD_pages.txt',encoding='utf-8').read()\nlines=t.split('\\n')\n# find leaf index by counting formfeeds before each target line\nimport re\nfor target in ['مسندروس','قنديل ‪ -‬لانيى']:\n    idx=t.find(target)\n    print(target, 'leaf(0-based)=', t[:idx].count('\\f'))\nprint('total leaves', t.count('\\f')+1)\nprint(re.findall(r'\\[pdf page \\d+\\]', t)[:5])\nEOF",
 "description": "Find TAD leaf positions"
}
```


### [2026-09-06T15:47:00.193Z] TOOL RESULT

```
مسندروس leaf(0-based)= 40
قنديل ‪ -‬لانيى leaf(0-based)= 62
total leaves 87
[]
```


## [2026-09-06T15:47:14.176Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v2 sandal/چندن ===\"; grep -n \"چندن\\|چندل\" BQT_v2_pages.txt | head -5\necho \"=== v2 سندل ===\"; grep -n \"سندل\" BQT_v2_pages.txt | head -5\necho \"=== v3 قندیل/کندر ===\"; grep -n \"قندیل\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5\necho \"=== v4 کندر ===\"; grep -n \"کندر\" incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head -5",
 "description": "Grep BQT for target words"
}
```


### [2026-09-06T15:47:14.289Z] TOOL RESULT

```
=== v2 sandal/چندن ===
7103:      ‫‪ - ۹‬رك ‪ :‬چندن ‪.‬‬                 ‫هماتکتاب ص ‪. ۹۳۳‬‬           ‫کلمه ‪ « 218004‬زاخائو‬
7142: ‫‪ = ۴‬چندل‪ ,‬ازقدیم از‬                ‫‪ _ ۴‬رك‪ :‬چندن ‪.‬‬         ‫‪ - ۱‬رکه‪ :‬چنندر‪ .‬چگندر ‪.‬‬
7145:  ‫مصفله» « وبلیامز ‪٩۸۳‬‏ ‪ .»۳:‬چندل (صندل) بیشتر محتمل امت که در آسیای غربی از هند‬
7146:   ‫واردشده باشد(فارسی چندان » چندل » ارمنی ‪ 1200126‬؛عربی صندل از سان کرب‪6‬ت‪28۳3002‬‬
7147: ‫‪ ۴‬چندن » صندل بود » ءمجدی(مروزی) گوید ‪:‬‬                         ‫» ‪ ۲. 255.‬و ‪oniS( - 26182۳1‬‏‬
=== v2 سندل ===
3763:              ‫که زرین کی سندل و چاچله ‪.‬‬                ‫‪ ۱‬گ‪-‬رفتم که جابی رسیدی زمال‪‎‬‬
7144:                              ‫هندی وارد فارسی‌شده و معرب آن‌سندل است « اسفا ‪ ۱‬ص‬
38327:    ‫سندل‬                                                                                   ‫‪۳۷-‬ات‬
38382:      ‫‪,25 1200‬ممربآن مندل«تفس» «لاروس‌بز رکه درزبان کنونی لیز‪ 200189‬کوبند ورك‪:‬سندلك‪.‬‬
38383:                           ‫« ندل کفش باشد و سندلك بیز کوبندش‪ .‬عنصری (بلخی) کوید ‪:‬‬
=== v3 قندیل/کندر ===
incoming/BQT/BQT_v4_pages.txt:9062:ای ماهی زرین و بمه بر زده شپیل دبرست بباغ آدر برزرین قندیل. >
incoming/BQT/BQT_v3_pages.txt:24569:قندیل. ۵و سر » کنابه از آسمان
incoming/BQT/BQT_v3_pages.txt:24574:قندیل ‎geet‏ کنابه از آتاب
=== v4 کندر ===
3627:وآن صمفی است که بفارسی کندررومی وب بانی نون » سنگی باشد سبز رنگك که کارد بدان یز
4024:پایشخت آن قاهرء و شهرهای عمدة‌آن اسکندربه» پرت سعید » سوئز میباشد . مصربان در نهشت
4243:ابراهیم علیه‌اللام درآنجا نما زگزارده بود - شعریت که دارالملك فیلفوی 8 پدر اسکندر
4261:لیدل و اسکات» «مرچنت» » ناحیه‌ای‌بود در شمال ونان » که در زمان فیلیپس واسکندر مقدونی
7869:- و نام مادر اسکندر ذوالفرئین هم هست ۷ . خدا , چه نالّب درعربی قائم مقام و تنکری در
```


## [2026-09-06T15:47:25.788Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f,targets in [('BQT_v2_pages.txt',[7144,38327,38382]),]:\n    lines=open(f,encoding='utf-8').read().split('\\n')\n    for t in targets:\n        # search backwards for a pdf page tag\n        for i in range(t-1,max(0,t-400),-1):\n            m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n            if m: print(f,t,'-> pdf page',m.group(1)); break\n        else: print(f,t,'-> no tag')\nEOF\ngrep -c \"pdf page\" BQT_v2_pages.txt",
 "description": "Find BQT v2 pdf page tags"
}
```


### [2026-09-06T15:47:28.219Z] TOOL RESULT

```
BQT_v2_pages.txt 7144 -> no tag
BQT_v2_pages.txt 38327 -> no tag
BQT_v2_pages.txt 38382 -> no tag
0
```


## [2026-09-06T15:47:31.402Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nprint('leaves',t.count('\\f')+1)\nlines=t.split('\\n')\nfor tgt in [7144,38327,38382]:\n    pre='\\n'.join(lines[:tgt])\n    print(tgt,'leaf',pre.count('\\f'))\nEOF",
 "description": "BQT v2 leaf positions"
}
```


### [2026-09-06T15:47:33.734Z] TOOL RESULT

```
leaves 684
7144 leaf 122
38327 leaf 637
38382 leaf 637
```


## [2026-09-06T15:47:42.516Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v3_pages.txt','BQT_v4_pages.txt']:\n    t=open(f,encoding='utf-8').read()\n    print(f,'leaves',t.count('\\f')+1, 'pdfpagetags', len(re.findall(r'\\[pdf page',t)))\nlines=open('BQT_v3_pages.txt',encoding='utf-8').read().split('\\n')\nt3='\\n'.join(lines[:24569])\nprint('qandil leaf', t3.count('\\f'))\nEOF\necho \"=== kondor v4 ===\"; grep -n \"کندر\\b\" BQT_v4_pages.txt | head -20",
 "description": "BQT v3/v4 structure"
}
```


### [2026-09-06T15:47:44.582Z] TOOL RESULT

```
BQT_v3_pages.txt leaves 721 pdfpagetags 721
BQT_v4_pages.txt leaves 553 pdfpagetags 553
qandil leaf 337
=== kondor v4 ===
3627:وآن صمفی است که بفارسی کندررومی وب بانی نون » سنگی باشد سبز رنگك که کارد بدان یز
4024:پایشخت آن قاهرء و شهرهای عمدة‌آن اسکندربه» پرت سعید » سوئز میباشد . مصربان در نهشت
4243:ابراهیم علیه‌اللام درآنجا نما زگزارده بود - شعریت که دارالملك فیلفوی 8 پدر اسکندر
4261:لیدل و اسکات» «مرچنت» » ناحیه‌ای‌بود در شمال ونان » که در زمان فیلیپس واسکندر مقدونی
7869:- و نام مادر اسکندر ذوالفرئین هم هست ۷ . خدا , چه نالّب درعربی قائم مقام و تنکری در
7890:۷ - در شاهنامه هم مادر اسکندر و هم اسم دیگن «کتایون > - زن کشناسب و مادر
10336:باستناد این بیت نظامی دربارة اسکندر :
10340:که بای (جد) اسکندر فرزند عیم‌ین‌امحوین ابراهیم بود . اگر ممنی نوا زاده را نوم بگیریم
10341:غلط تاریشی‌میشو د که اسکندر سیصد وکری سال پیش ازمیلاد بوده ومبان او وعیص بیش ازهزار
10600:زمان سکندرسه‌لوبت بوده بمدازآن چها رکرادند» فوبتی * - بر وزن نکبتی, نقاره‌چی‌را
10662:[اسکندر]پبلغآمد و آتش زردهشت بطوفان شمشیر چون‌آب کشت
10760:نودر منش سکندرئانی که در جهان چون او نزاد مادر ایام نودره » درشنگ»
16557:درخدمت اسکندر ۴ - و بعضی دیگر کوبند نام | و جمعی(۱) کویند سه خکیم‌اند که هرسه‌هرمس
16587:۴ - این اشتیاه از نظامی کنجوی است که هفت داشمند مختلف‌اامهد را درزمان‌اسکندر
16589:ازآن فیلوفان کزین کرد (اسکندر) هفت که برخاطر کس خطایی نرفت :
16593:نظامی کنجوی . اقبال نامه : « خلوت ماختن اسکندر با هفت حکیم > چاپ ارمقان س ۰۱۲۰
17632:۲ - رك : هف ت کوهر . خان آرزو در شغرح اسکندر نامه نوشته که رسم ملاطین ایران
18282:۱ - بیهوده مجوی آب حیوان در ظلمت خوش چون سکندر
19875:بیاورد وبنهاد پیشش ( پیش اسکندر که بصورت رسول آهده بود) خریر
19877:که کرهیچ جنیش بدی درنگار نبودی جز اسکندر شهربار.
```


## [2026-09-06T15:47:53.251Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nlines=open('BQT_v3_pages.txt',encoding='utf-8').read().split('\\n')\nfor i,l in enumerate(lines):\n    if 'کندر' in l and 'اسکندر' not in l and 'سکندر' not in l:\n        print(i, l[:160])\nEOF",
 "description": "Grep kondor in BQT v3"
}
```


### [2026-09-06T15:47:55.254Z] TOOL RESULT

```
12328 ‏مانتد کندر بسوزانندو,عربی میمةسابله خوالند.
35591 از کندر باشد ‎Ty‏ صمغ یمن ی کویند .
36577 ‏4 کندراله (هم).
36590 ‎—\veo—‏ کندرو
36598 ‏کندردوهی ‎gine ag’‏ است که
36615 کندر است که کندر لوبان باشت ؛ و بسنی دیگر
36616 کوبند کندر درختی است شبیه‌بدرخت پسته‌لیکن
36618 ‏۱ - بیابان بی‌آب و کوه شکسته دو صد ره قزوست از شهر ‏ وکندر .
36620 ۴ کندر ( منم اول و سوم ) نام دو موضع است ‎cass‏ قربه‌ای از ‎aly‏ تیشابوراز
36621 اعمال ترشیز و عمیدالملك ابوصر کندری بدان منسوبست - ‎sland Sar‏ ترديك بقزوین‌وابوغانم
36622 حین و ابوالهن علی پران عیی‌بن‌حسین کندری بدالجا منشوبند « ممیم‌البلدان ‎.٩‏
36627 ‎UI‏ مابرهوف کوید : دو تام کندر و لبان مشتق ازیوبانی 1100۵ 2۵80۲05 ( ‎grumeaux‏
36628 ‎Me» atl. ) 5‏ ۸۸ ف *. کندر ؛ توعی از صمغ » وآن لبان نربنه است .سمخ
36639 ‎٩‏ - ره : کندر .
36642 ‎Ly‏ « کندرو» خواندندی ‎Ay‏ بکندی زدی پیش‌بیدادکام.
36645 است . در مجمل‌التواریخ و القصص ص ‎۸٩‏ «کندروق» آمده . اما در اوستا ‎Gandareva‏ ( با
36646 کاف پارسی ) ‎ok,‏ شده (آبان بشت بند ۲۷ ) و در کتب متأخر پپلوی « کندرب زره پاشنه»آمده.
36649 ‏۸ _ بعلمطبقات طبق زنان سرای ‎HL‏ مازو و کندرو و کلاب
36650 > خافانی شروالی ‎۵٩‏ © . در مهذب الاسماء نز در معنی علك « کندرو» ‎otal‏ .
38010 کوداب ۴ » بروزن و معنی دوشاب» طبع و ‎alee‏ را گویند - و اسب پی رکندرو
38934 ‏و کندرو را نیز کوبند ۳ - و نام ‎SVS Sedans‏ ۲ با ثالی مجهول بوزن
50514 آنراکندر میگویند ۷
```


## [2026-09-06T15:48:02.479Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '36570,36640p' BQT_v3_pages.txt\necho \"=== page tags near ===\"; awk 'NR>=36400 && NR<=36700 && /pdf page/{print NR\": \"$0}' BQT_v3_pages.txt",
 "description": "Read BQT kondor entry"
}
```


### [2026-09-06T15:48:04.327Z] TOOL RESULT

```
‏مصدر بقلم نگارنده ۱۱۹-۱۱۸ .

‏۲ + از : کندا (.م.) ۲ کر (پسرند شفل ومبالفه).

‎A‏ - ممرب‌آن ‎TUS?‏ ( بضم اول و کسر پنجم ) : « الشجاع » الجصور » فارسیةنقلها

‎.) ۵ ‏اقرب‌الموارد : 2 ان د‎ ( (OMS ‏عن‌بعض‎ GS

‏4 کندراله (هم).

‎N°‏ این ‎cal‏ در فرهنگها بصورت «کندآور* آمده است . بسض فنلای مماصر صورت

‏اخیر را سحیح داسته‌اند. بولد که وهرن وهوبشمان « اسشق

‏- هوبشمان ‎CANA‏ آلرا با کاف‌تازی

‏از ‎dey‏ «کند » ‎gine‏ شجاع هل کردماند , ولف نیز در فهرست شاهنامه « کندآور © و « کند
آوری » را ‎GEL‏ تازی آورده است . بتابراین کندآور باید مر کب از :کندا ( شجاعت ) + ور
‎sigs (‏ اصاف ) باشد » به از : کند (شجاع) + آور (آورنده) چه آور در ‎ALT‏ فرکبه ازاسم
آید : رزم‌آور » تناور » دلاور ‎Ay)‏ : لف‌نامه : آور ) - و رك :کندآور.
[pdf page 498]
‎—\veo—‏ کندرو

‏باری ومیوه‌ای و تخمی ندارد صمغ آن را بنام
‎oT‏ درخت خوانند و صمغ‌البطم همان است ‎OT,‏
‏شبیه است بمصطکی . وطبیت آنکرم باشد -
و نام پادشاه سقللاب هم بوده و اوییاری افراسیاب
آمده بود ۵ .

‏کندردوهی ‎gine ag’‏ است که
آ را علك رومی میگوبند و مصطکی‌همان است.

‎» ‏اول بر وزن ستبلك‎ pe - Sa

‏کنداکر است که حکیم و دانا - ومبارزوپهلوان
‎ath‏ - و بممنی سیهسالار هم بتظرآمده است -
‎can >‏ پهلوان و ‎eee‏ با کاف فارسی هم
‎a”‏ اند .

‏کندد - بفتح اول و ثالث و سکون‌ثالی
و رای قرشت » مطلق شهر و مدیته را گوبند
عموماً | - و شهری بوده از شهرهای خراسان
خصوماً ۴ - وبفتح اول و ضم ‎elt‏ » ظرفی‌باشد
که از گل سازند و کندم ونان درآن‌کنند ۴ -
و ضم اول و ثالث صمغی است که آنرا مصطکی
خوانند ۴ - و بستی کوبند مصطکی‌هم نوعی از
کندر است که کندر لوبان باشت ؛ و بسنی دیگر
کوبند کندر درختی است شبیه‌بدرخت پسته‌لیکن

‏۱ - بیابان بی‌آب و کوه شکسته دو صد ره قزوست از شهر ‏ وکندر .
« اصرخرو بلخی ص۱۹۹ *.
۴ کندر ( منم اول و سوم ) نام دو موضع است ‎cass‏ قربه‌ای از ‎aly‏ تیشابوراز
اعمال ترشیز و عمیدالملك ابوصر کندری بدان منسوبست - ‎sland Sar‏ ترديك بقزوین‌وابوغانم
حین و ابوالهن علی پران عیی‌بن‌حسین کندری بدالجا منشوبند « ممیم‌البلدان ‎.٩‏
‏۴ - «کندو» (ه.م.) باین معنی است ودرمتن صحیف شده (سراج‌اللقات بنقل فرهنگه
نظام ‎Oe‏ ص م) . ۴ - لوفر کوید . ‎kundur‏ . بشور ( ‎(Boswellia thurifera‏
ساتسکریت ‎kunduruka .kundu .kundura .kundury‏ . شکل‌پهلوی۵00۲۵1ناعاه
‎kundurukaj\ vii. kndruk,..,\,‏ سانسکررت میباشند(1۳2۵68,۴۰585 ‎(Sino.‏
‎UI‏ مابرهوف کوید : دو تام کندر و لبان مشتق ازیوبانی 1100۵ 2۵80۲05 ( ‎grumeaux‏
‎Me» atl. ) 5‏ ۸۸ ف *. کندر ؛ توعی از صمغ » وآن لبان نربنه است .سمخ
درختی است قریب بدو ذراع و ‎ULE‏ . ب رک ‎OT‏ شبیه بب کهآس است وآن در کوههای‌یمن

‏صمتی باشد که آنرا بجاوند وآن راعلك‌خآییدی

‏هم میگوبند و گوبند مصطکی همان است.
کنددف = بروزن ‎SF‏ . نام وزیر

‎- ۵۸ ‏بوده ۷ - و مسطکی را بي زکوبند‎ tne

‏یافته شود وییونانی خندروی کوبند. « اقرب‌الموارد ». ۵ رك : فهرست ولف .
‎٩‏ - ره : کندر .
=== page tags near ===
36402: [pdf page 496]
36494: [pdf page 497]
36590: [pdf page 498]
36652: [pdf page 499]
```


## [2026-09-06T15:48:19.350Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '24555,24600p' BQT_v3_pages.txt\necho \"=== tags ===\"; awk 'NR>=24400 && NR<=24700 && /pdf page/{print NR\": \"$0}' BQT_v3_pages.txt\necho \"=== search qandil footnote ===\"; grep -n \"قندیل\" BQT_v3_pages.txt | head -20",
 "description": "BQT qandil entry"
}
```


### [2026-09-06T15:48:21.344Z] TOOL RESULT

```
قندهار = با ها بروزن شرمار » نام
شهری ‎col‏ معروف . بعضی گویند از ترکتان
است وبستی دیگر ‎a‏ ازهندوستان ۷ .*

‎٩‏ رك : رئیدی . ؟ ‏ رك

‏بناحیت غور ) قس : سگ غوری « دبوان خاقانی ص ‎٩۵۰‏ س4 > .

‎Vda - le i pad‏ گونند که
پیوسته ‎IS‏ که مد ترسابان است‌آوبنته
باشد ۸ .

‏قند یل چرخ = ‎ALS‏ ازآتاب و ماه
ات٩‏ .
قندیل. ۵و سر » کنابه از آسمان
است .

‎pad‏ شب ‎ow‏ کنابه از سیاهی شب
است .
قندیل ‎geet‏ کنابه از آتاب
عالمتاب است

‎Und‏ - بکر اول و طای حطی بالف
کشیده » بلفت رومی*۱ دوائیست که نرابفارسی
خون سیاوشان و بعربی دم‌آلاخوین خوانند ‎.۷٩‏

‏قنظاد » با ‎cb‏ حطی بروزن دلدار .
‎cal‏ رومی بمعنی ساداوران‌است» وآن‌چیزی‌است
‎ale‏ صمغ ودر درون ‎Ge‏ درخت کردکان‌میباشد.

‏۴ ظ . قندز غوری ‎ve)‏
‏۴ 2 کندس ‎dw?‏

‏حکیم ممن » « فهرست مخزن‌الادوبه * ‎(ye)‏ « کندی ‎RAAT‏ . بیخ نباتیست درون‌آن زرد وبرون
آن ‎ule‏ مفیئی است مسهل, دافعبهق: وچون سفوف آنرا سعوط کنند عطه‌آورد و کندی‌بینایی

‏وشبکوری را نافع . » «منتهی الارب» .
۵ ه ‎Cea)‏
‏« دزی ‎EV HIE‏ . رل + واوشیشمان .

‎calycotome intermedia . (5) aspalathe= ۱

‎Y‏ شهری باففاستان که نام آن بابللت شامل

‏وی نیز اطلاق شده » ‎OT,‏ در۳۱ درجه ‎Liaw,‏ عرض شمالی ‎Vey‏ درجه و4۳ ‎Liss‏ طول‌شرقی»
بارتفاع ۳4۹۲ قدم ۰ ‎on‏ رودهای ترىك و ارغنتاب واقم شده و دارای ۳۱۰۶۶ سکنه‌است. ره :
=== tags ===
24415: [pdf page 336]
24468: [pdf page 337]
24534: [pdf page 338]
24618: [pdf page 339]
=== search qandil footnote ===
24569:قندیل. ۵و سر » کنابه از آسمان
24574:قندیل ‎geet‏ کنابه از آتاب
```


## [2026-09-06T15:48:36.236Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"== $f: $(wc -l < $f) lines\"; done\ngrep -n \"سندروس\" MON_part1.txt MON_part2.txt | head -5\necho \"=== kandid ===\"; grep -n \"کاندیدا\\|کاندید\" MON_part1.txt MON_part2.txt | head -5\necho \"=== sandali ===\"; grep -n \"صندلی\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in local files"
}
```


### [2026-09-06T15:48:38.627Z] TOOL RESULT

```
== MON_part1.txt: 99339 lines
== MON_part2.txt: 94500 lines
MON_part1.txt:80055:سسندروس: 2026 (.) (گیا.) سرو . 
MON_part1.txt:80062:از مخلوط سندروس و روغن بزرگ روغنی 
MON_part1.txt:80065:حجر السندروس. (گیا.) تبریزی. (گی.) 
=== kandid ===
=== sandali ===
MON_part2.txt:21948:سخن خود را تحمیل کردن. صندلی؛ ج 
MON_part2.txt:40325:بالش يا مخده یا صندلی راحتی و غیره برای 
MON_part2.txt:45115:مبل: 0۱0۱۱ (۱.) لوازم خانه مانند صندلی» 
MON_part2.txt:81670:اطاق‌ها و ساختن برخی لوازم از قبیل صندلی 
MON_part1.txt:6969:اطاق دراز و صندلی‌های متعدد که ها
```


## [2026-09-06T15:48:42.076Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '80045,80070p' MON_part1.txt\necho \"=== صندل headword ===\"; grep -n \"^صندل\\|صندل:\" MON_part1.txt MON_part2.txt | head -10\necho \"=== کندر headword ===\"; grep -n \"^کندر\\|کندر:\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Mo'in sandarus context"
}
```


### [2026-09-06T15:48:42.175Z] TOOL RESULT

```
از وانلای فرهنگ فارسی معین ۱۳ 


بر آن اهل خانه را خبردار کنند. سندان 
گوش: (پز.) یکی از سه استخوان کوچکك 
داخل صندوق کوش میانی؛ استخوان 
سندانی» سندانی. 


سسندروس: 2026 (.) (گیا.) سرو . 


کوهی. (گیا.) صمفی که از گونه‌ای سرو 
کوهی استخراج می‌شود و در طب قدیم 
مورد استعمال بوده ما از آن در ساختن 
دانة تسبیح با گر دن‌ند استفاده می کر ده‌اند» 
از مخلوط سندروس و روغن بزرگ روغنی 
بنام روغن کمان حاصل می‌کر ده‌اند که از آن 
جهت چرب کردن کمان‌ها استفاده می‌شد؛ 
حجر السندروس. (گیا.) تبریزی. (گی.) 
نارون. 

سسند زره (6-)۹6002۲2 [- سنداره] (اص.) 
حرامزاده. 

=== صندل headword ===
MON_part2.txt:58922:صندل؛ خوشوی شده با صندل. 
MON_part1.txt:29255:صندلی و مانند آن» پایه نخت» بای میزه 
MON_part1.txt:35174:صندلیی که در بیش تخت (سلطان با امیری) 
MON_part1.txt:90271:صندل؛: اوه (.) نوعی کفش که با نند به 
MON_part1.txt:90273:صندلی: آ-20021: (ص‌نسه. امر.) صندلی 
=== کندر headword ===
MON_part1.txt:26434:کندر هندی. 
MON_part1.txt:44069:کندرو. بی‌با کك» بی پر و ا. 
MON_part1.txt:91910:کندرسته» الطالع من الکند. 
MON_part1.txt:92209:سکندر: طبل منسوب به اسکند مقدونی 
MON_part2.txt:2012:کندرین در آن حل شده است؛ بافت 
MON_part2.txt:27042:کندر: ۲0۳۵0۲ (.) (گیا.) 
MON_part2.txt:93008:کندرو و دارای سم‌های پهن و قوی و کمر
```


## [2026-09-06T15:48:55.528Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON صندل / صندلی ===\"; sed -n '90255,90300p' MON_part1.txt\necho \"=== MON کندر ===\"; sed -n '27035,27060p' MON_part2.txt",
 "description": "Read Mo'in sandal and kondor entries"
}
```


### [2026-09-06T15:48:55.601Z] TOOL RESULT

```
=== MON صندل / صندلی ===
صنعت. . صنایع ند بعی. صنعت‌هایی که در 
علم بدیم بحث می‌شود» مانند تجنیس» 
مراعاة النظیر» لف و نشر و غیره. صنایع 
دستی: صنعت‌هایی که دست در آنها دخیل 


است» مانند: بارچه‌بافی» قالی‌افی. صنایع 
ظر یفه: صنعت‌هایی که در آنها ظرافت بکار 
رود از قبل خطاطی» نقاشی» مجسمه‌سازی» 
رقص؛ هنرهای زیسبا. صنایع بسدی: 
دست‌ورزی (فره.) 
صنج؛ : 571 [معر. . سنج» قس. . چنگ] (.) 
چنکگ. در فد ۶ فلزی که به وسبلهة 
بندی به انگشتان پیوندد. مج ۱ س از بند 
کردن به انگشتان» به 7 تا آوازی 
از آن بر آید. 
صندل؛: اوه (.) نوعی کفش که با نند به 
پا بندند. 
صندلی: آ-20021: (ص‌نسه. امر.) صندلی 
بیدسته: صندلیی که دسته ندارد؛ مق. صندلی 
دسته‌دار. صندلی دسته‌دار: صندلیی که دارای 
دسته است؛ مق. صندلی بیدسته. صندلی 
راحتی: صندلیی که به راحتی توان در آن 
نشست و باها را دراز کرد. 
صندوق: ههد [ع.] () جع بزرگک 
فلزی یا چوبی ج. صنادیق. ضح.- در عربی به 

ضم اول گویند ولی در فارسی عموماً به فتح 
و تلفظ شود. صندوق نسوز: صندوقی 
فلز ی که در حریق دوام آورد. تالوت مرده. 
(ادا. سانک.) شعبه‌ای در بانک پا ادارات 
دولتی و موّسسات ملی که اخد و پرداخت 
وجه رابه عهده دارد. 
صدوقدار: ۶-۲ [ع. ف. < 
صندوق‌دارنده] (ص‌فا.) خرانه‌دار. (فره.) 
کسی که در حسانداری‌ها متصدی کار 
صندوق است. 
صند ید: ۰۰0۵14 [ع.] (ص.۱.) مرد بزرگك» 
مهتر» سرور. دلاور. سرمای شد ید (غم.)؛ 
۳ صناد بد. 

نم: 502 [ع.] (مص‌م.) ساختن» آفریدن. 
نیکویی کردن؛ نیکی کردن؛ احسان کردن. 
(امص.) احسان» نیکویی. آفرینش. کلکک 


=== MON کندر ===
۰۳ 


حکمت و دانایی استعمال کر ده‌اند. 
کنددذهن: ۵۱0 آف. ۳۵ (ص‌مر.) 
کودن» کم هوش. 

کندر: ۲0۳۵0۲ (.) (گیا.) 
خوشو که از درخت کندر هندی بدست 
آورند و جهت استفاده از رایحهٌ مطبوعش 
آن را در ۳ ریزند. کندر را از درختان 
دیگر از جمله درختان تیرٌ کاج و صنوبر 
می‌توان بدست آورد ولی نوع مرغوب آن 
همان کندر هندی است که سرخ رنگ است 
و انواغ دیگر کندرها سفید رنگند. کندر 
حبشی: (گیا.) گونه‌ای کندر سفید رنگ که 
از انواغ سرو کوهی و عرعر حاصل می‌شود 
ولی به مرغویب کندر هندی نیست. کندر 
رومی: (گیا.) مصطکی. کندر هندی: ( گیا.) 
درختی است از رده دو لیهبی‌های جدا 
کل که زر و نارس رآسته که نوش 
هندوستان است و آن را از صمغی خوشوی 
بنام کندر استخراج می‌کنند؛ لبان» لیبانون 
شجرة اللبان» درخت کندر» عسلنند. 

تال ر: 0-2 [- کهن‌دز (دزکهن) -
```


## [2026-09-06T15:49:07.608Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD",
 "prompt": "Give the full etymology of Ancient Greek σάνδαλον (sandal, shoe) and of σάνταλον (sandalwood) if mentioned, including proposed Persian/Lydian/Oriental origins and any cited scholars (Beekes, Kretschmer)."
}
```


## [2026-09-06T15:49:08.769Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sandalwood",
 "prompt": "Give the full etymology text for sandalwood, sandal (shoe), and sandarac if present, verbatim as far as possible."
}
```


### [2026-09-06T15:49:14.052Z] TOOL RESULT

```
# Etymology of σάνδαλον

Based on the Wiktionary entry provided, here is the documented etymology:

## Origin
The word is described as "Likely from Pre-Greek or some other foreign source, in view of the alternation 'νδ/μβ'." The entry cites Robert S. P. Beekes's *Etymological Dictionary of Greek* (2010) as the source for this analysis.

## Comparative Evidence
The entry notes a comparison with Middle Persian *čandal* (meaning "sandalwood"), which itself derives from Sanskrit *candana* ("sandalwood").

## Note on σάνταλον
The provided content does not discuss σάνταλον (sandalwood) separately or offer distinct etymological information for that term. The entry focuses exclusively on σάνδαλον as it refers to sandals/footwear and a type of fish, with the Persian/Sanskrit connection mentioned only as a comparative point rather than as the direct source of the Greek word.

No scholars beyond Beekes are cited in this particular entry.
```


### [2026-09-06T15:49:15.810Z] TOOL RESULT

```
# Etymology Information

## Sandalwood

The full etymology provided states:

"1510s, earlier simply _sandell_ (late 14c.), _saundres_ (early 14c.), 'the wood of the heart and roots of certain species of trees native to Asia,' from Old French _sandale_, from Medieval Latin _sandalum_, from Late Greek _santalon_, which is ultimately from Sanskrit _čandana-m_ 'the sandalwood tree,' perhaps literally 'wood for burning incense,' related to _candrah_ 'shining, glowing,' and cognate with Latin _candere_ 'to shine, glow.'"

The entry also notes that in China, sandalwood "was burnt extensively as incense in temples and homes," and that sandalwood oil is "strongly aromatic and used in perfumes and cosmetics."

## Sandal (shoe) and Sandarac

The page content provided does not include etymological entries for sandal (shoe) or sandarac. While "sandal" appears in the alphabetical index of nearby dictionary entries, its full etymology is not displayed in the extracted content.
```


## [2026-09-06T15:49:19.474Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sandal",
 "prompt": "Give the full etymology text for \"sandal\" (footwear), verbatim."
}
```


## [2026-09-06T15:49:21.601Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AF%D9%84%DB%8C",
 "prompt": "Give the Persian entry صندلی: etymology, meaning, and any stated Arabic/Greek origin. Also mention any Arabic صندلي entry."
}
```


### [2026-09-06T15:49:24.339Z] TOOL RESULT

```
# Etymology of Sandal

The full etymology text from the source is:

"type of shoe consisting of a sole fastened to the foot by thongs, the common footwear of ancient Greece and Rome, late 14c., from Old French *sandale* and directly from Medieval Latin *sandalum*, from Latin *sandalium* "a slipper, sandal," from Greek *sandalion*, diminutive of *sandalon* "a sandal," also "a flatfish," a word of unknown origin, probably foreign, perhaps from Persian."

In summary: The term entered English in the late 14th century through Old French and Medieval Latin, ultimately deriving from Greek *sandalion*. The Greek root's exact origin remains unclear, though scholars suspect it may have foreign (possibly Persian) roots.
```


### [2026-09-06T15:49:28.175Z] TOOL RESULT

```
# Persian Entry: صندلی

## Etymology
The word صندلی (sandalī) derives from صندل (sandal) plus the Persian suffix ـی (-i). The root traces back through Arabic صَنْدَل (ṣandal) to Middle Persian, ultimately originating from Sanskrit चन्दन (candana).

## Meaning
صندلی has two primary definitions:
1. **Chair** (in Iranian Persian and Classical Persian)
2. **Bench**

The Dari dialect uses the synonym چَوْکِی (čawkī) for chair instead.

## Arabic Connection
The etymology tree shows Arabic صَنْدَل (ṣandal) as a borrowing stage in the word's development. Additionally, the entry notes that Persian صندلی descended into Arabic as صَنْدَلِيَّة (ṣandaliyya), demonstrating bidirectional linguistic influence.

No separate Arabic صندلي entry details appear in this Wiktionary page content.
```


## [2026-09-06T15:49:36.397Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF%D9%8A%D9%84",
 "prompt": "Give the Arabic قنديل entry: etymology (Greek/Latin/Syriac route), meaning. Also any Persian قندیل entry."
}
```


## [2026-09-06T15:49:37.812Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%AF%D8%B1",
 "prompt": "Give the Arabic كندر entry (frankincense) etymology, and any Persian کندر entry etymology. Mention Sanskrit kunduru / Middle Persian kundur if stated."
}
```


### [2026-09-06T15:49:42.915Z] TOOL RESULT

```
# Etymology of كندر (Frankincense)

**Arabic كندر (kundur):** According to the Wiktionary entry, this term was "Borrowed from Classical Persian _کندر_ (kundur)."

**Persian کندر:** The page does not provide a separate etymology section for the Persian entry, only noting it as the source language for the Arabic borrowing.

The entry does not mention Sanskrit kunduru or Middle Persian kundur specifically, though the Persian origin is confirmed as the etymological source for the Arabic word meaning frankincense (the resin of _Boswellia thurifera_).
```


### [2026-09-06T15:49:43.496Z] TOOL RESULT

```
# Arabic قنديل Entry

**Etymology Route:**
The word traces back through "Classical Syriac ܩܢܕܠܐ (qandēlā), borrowed from Ancient Greek κανδήλη (kandḗlē)," which itself derives from Latin *candēla* (candle), rooted in Proto-Indo-European *(s)kend-*.

**Primary Meanings:**
1. Lamp
2. Candlestick or candelabrum
3. Thorny broom (*Calicotome*)

**Persian قندیل Entry:**
The page indicates Persian received this word from Arabic. In Persian, it functions as "قندیل (qandil)" and spawned numerous descendant terms across South Asian languages including Hindi, Urdu, Punjabi, Gujarati, Kannada, and Marathi—all referring to lamps or light sources.

The word dispersed widely through Ottoman Turkish to Spanish, Portuguese, and other Romance languages, demonstrating extensive historical trade and cultural contact across Mediterranean and Asian regions.
```


## [2026-09-06T15:49:48.931Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kend-",
 "prompt": "Give the reconstructed root, its meaning, and the list of descendants (Latin candeo, Sanskrit, Welsh, Albanian). Also note references (Pokorny page)."
}
```


## [2026-09-06T15:49:50.475Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/candana",
 "prompt": "Give the Sanskrit चन्दन (candana) etymology and meaning, and whether it is connected to candra- / PIE *(s)kend- or considered a non-Indo-European/Dravidian loan."
}
```


### [2026-09-06T15:49:52.760Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:49:55.193Z] TOOL RESULT

```
# Proto-Indo-European Root *(s)kend-

**Reconstructed Root:** *(s)kend-

**Meaning:** "to shine, appear"

**Key Descendants:**
- Latin: *candeō* (to shine)
- Sanskrit: *chandas* (meter/verse), *candrá* (moon)
- Albanian: *hënë* (moon)
- Welsh and other Indo-European languages show related formations

**Alternative Reconstructions:** *(s)kand-, *(s)ḱend-

**Primary References:**
- Pokorny (1959): "Indogermanisches etymologisches Wörterbuch," page 526
- Rix (2001): "Lexikon der indogermanischen Verben," page 554
- De Vaan (2008): Etymological Dictionary of Latin and the other Italic Languages, pages 106-107

The root demonstrates the characteristic Proto-Indo-European s-mobile feature and appears across multiple language families with consistent semantic connections to luminosity and celestial phenomena.
```


## [2026-09-06T15:49:59.402Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A8",
 "prompt": "Give the Sanskrit चन्दन (candana) etymology and meaning, whether it derives from the root cand- 'to shine' or is regarded as a non-Indo-Aryan / Dravidian / Austroasiatic loanword. List descendants (Middle Persian, Arabic, Greek)."
}
```


## [2026-09-06T15:50:00.775Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%86%D8%AF%D8%B1%D9%88%D8%B3",
 "prompt": "Any entry for سندروس (sandarus) in Arabic or Persian: etymology and meaning."
}
```


### [2026-09-06T15:50:07.639Z] TOOL RESULT

```
# Etymology and Meaning of سندروس (Sandarus)

## Arabic

**Meaning:** The term refers to sandarac—both the tree *Tetraclinis articulata* and the resin extracted from it.

**Etymology:** The word derives from Ancient Greek σανδαράκινος (sandarákinos, meaning "orange-coloured, sandarac-like") or related Greek masculine formations. The entry notes that "the Arabic term can well be considered an Aramaic loan," given that related terms appear in Classical Syriac, Jewish Babylonian Aramaic, and Mishnaic Hebrew.

## Persian

**Meaning:** In Persian, سندروس functions both as a noun describing the *Tetraclinis articulata* tree and the resin product, and as an adjective meaning "sandarac-coloured" or "yellow" (archaic/literary usage). Figuratively and in literary contexts, it describes someone as "extremely scared."

**Etymology:** The Persian term was "borrowed from Arabic," representing a direct linguistic transmission from the Arabic form already discussed above.
```


### [2026-09-06T15:50:08.520Z] TOOL RESULT

```
# Sanskrit चन्दन (candana) — Etymology and Meaning

## Etymology

The word has two proposed origins:

**Traditional View:** Derived from the Sanskrit root चन्द् (cand-), meaning "to shine."

**Modern Linguistic View:** "Probably a Dravidian borrowing" rather than Indo-Aryan. Cognates include Tamil சாந்து (cāntu, "Santalum tree") and Malayalam ചാന്ത് (cāntŭ, "sandal paste").

## Meaning

The Sanskrit noun refers to **sandalwood** (the aromatic tree and wood).

## Selected Descendants

The term spread across multiple language families:

- **Middle Persian:** cndl (/čandal/)
- **Greek:** σάνδανον (sándanon) — via Gandhari intermediary
- **Romance/European:** Lokotsch (1927) documents orientalisms in European languages
- **Asian languages:** Hindi चन्दन (candan), Malayalam ചന്ദനം (candanaṁ), Thai จันทน์ (jan), Chinese 栴檀 (zhāntán)
- **Classical Tibetan:** ཙན་དན (tsan dan)

The wide geographic dispersal suggests the term traveled ancient trade routes, particularly the Silk Road.
```


## [2026-09-06T15:50:15.961Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%B1%CE%BD%CE%B4%CE%B1%CF%81%CE%AC%CE%BA%CE%B7",
 "prompt": "Give the Ancient Greek σανδαράκη etymology and meaning; does it mention Sanskrit candra-rāga, Iranian, or Beekes's view that it is a Pre-Greek/Oriental loan?"
}
```


## [2026-09-06T15:50:16.280Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sandarac",
 "prompt": "Give the full etymology text for sandarac, verbatim."
}
```


### [2026-09-06T15:50:21.105Z] TOOL RESULT

```
I don't see any etymology text for "sandarac" in the web page content provided. The content shows the header, navigation, and footer of the Etymonline website, but it doesn't include the actual dictionary entry or etymology for that word. To find the full etymology text for sandarac, you would need to visit the Etymonline website directly and search for that term.
```


### [2026-09-06T15:50:22.025Z] TOOL RESULT

```
# σανδαράκη Etymology and Meaning

## Meaning
The Ancient Greek word refers to: (1) sandarac or realgar; (2) red orpiment; (3) beebread (bee pollen mixed with honey and bee secretions).

## Etymology
The document does **not** mention Sanskrit candra-rāga or Iranian origins.

Regarding the etymology itself, the text notes: "Long taken to be an Oriental loanword from an unknown source." It then proposes a possible Akkadian origin combining words for "pigment/paint" and "yellow," creating "yellow paint" (orpiment).

On Pre-Greek origin, Beekes's view is: "does not dismiss a Pre-Greek origin, in view of the variation 'κ/χ'."

The etymology also connects it to Middle Armenian ջնարակ (ǰnarak) as a synonym, suggesting possible linguistic relationships across language families.
```


## [2026-09-06T15:50:53.875Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kundur/sandal ===\"; grep -n -i \"kundur\\|kondor\\|çandal\\|candal\" HRN.txt | head -10\necho \"=== HUB ===\"; grep -n -i \"kundur\\|kndruk\\|candana\" HUB.txt | head -10\necho \"=== LKT ===\"; grep -n -i \"sandel\\|sandal\\|sandarak\\|kandil\\|candela\" LKT.txt | head -15",
 "description": "Grep Horn, Hübschmann, Lokotsch"
}
```


### [2026-09-06T15:50:53.963Z] TOOL RESULT

```
=== HRN kundur/sandal ===
=== HUB ===
=== LKT ===
743:243.  Ar.  barga: 'Haifa-Sandale,  Hausschuh'  [das  Wort ist  selbst  durch  romanische  Vermittelung aus  dem  Baskischen  zu  den  Arabern gekommen  ZDMG  LI,  311;  vgl.  sp. aharca,  mlat.  abärca  'Bauernschuli'] ; hieraus  mit  dem  ar.  Art.  pg.  alparca, murcianisch  alborga,  albolya  ;  aus  dem ar.  plr.  al-bargät  wurde  sp.  pg.  alpar- gata  'Spartoschuh'.  [ZfromPh  XXXII, 43.    ML  904.
787:'Sandale,  Schuh'  [Kelekian  Kämüs  240  a]; hieraus  russ.  klr.  basmak  'Schuh',  bas- niacnik  'Schuhmacher',  bulg.  basmak, serb.  2^^smag,  poln.  baczmag  'Schuh'. [Gorjajew  14.  Mikl  SlEtWb  8.  Bern SlEtWb  45.
2505:1053.  Ar.  kandil:
2506:'Leuchte,  Laterne'  [aus  lat.  candela,  gr. KttvbriXn  ZDMG  LI,  316];  hieraus  sp. candil  'dass.',  mit  ar.  Art.  alcandora 'Signalfeuer'  [DE  84  u.  247].
4135:[Ar.  sandal.
4137:182.5.  Ar.  saudal: 'Indisches  Farbholz'  [aus  pers.  cändäl <^  sskr.  candana];  hieraus  gr.  öavbd\iov 'Holz  von  Pterocarpus  sanlalina  L.'. It.  sändalo,  frz.  sandale,  bois  de  sandal, sp.  pg.  sändalo;  russ.  sandal;  engl,  san- dal, sandle,  sanders,  dtsch.  Sandel(holz) . [DE  339.    Hobson-Jobson  789/790.
5285:A;«^«?'«  1002 ka'fihn  1002 ÄrrtÄA-rt/ur  1003 kahwa  1005 k'i^  1006 A;«*/*  1007.  1173 kail  1 174  a kä^iininnkäm  1010 katsänia  1011 kaitus  273 Ä-«)i;ö(i  lol3 käkang  1016 ter«  1021 kala'a  1036 kalaba  1376 kalada  1505 fcatofa  1022 Ä-aZ«w  1023 Ä:ffZ6  1025 A-a/ö  1026 teZ»  1029 k^/ö  1030 Ä;fl?«»iffl  1032 A;a?tö'  1036 A-aWfli  1037 A;rt>Hä  1157 käma  1010.  1999 if«H!7  1044 kammün  1046 kand(l)  10.52 kandara  1051 kandil  1053 kantara  1057.  1506 kanz(lja)  1059 Ä;ar«  1181.  1507 A;ßm  1071.  1072 A-ar'^a  689 kaya'a  1250 karam  1083 karawän  1086 karawijä'  1087 kafija  1094 karlwija  1095 A;ar>«  1096 Ä-flrA-rti  1096  b Ä:a»-n  1098 karräza  1101 karsana  1 103 A-a;YSs  1104 karuba  1252 Ära's  1105 A-äsa  1174 kas^a  1106 iW&ff  1108.  1118 Ä-asa/'a  1109 kasama  1187 kasara  1575 Ä;as(i  1110 kasdlr  1111 Ä-ßs/r  1575 A-as/s  1114 fcasr  1117
5874:Saccharin  1855 ÄicÄ;  1781 SäcAreZ  1781 Sacker  falk  1799 Sackmann  1781 &'a/^«n  1752 Äa/"«/-«  1879 Ärt/'/jaw  1769 SaA/-«w  2178 Sa^o  1761 Sahara  1766 Sniga(antilope)  1774 Salangan  1844 Äa^pft  2001 Sa/t;p  2001 Äa/i««-  1567 Salniter  1567 salomonisch  1881 Sambuk  1824 sambaztac  ahd.  1742 sameztag  nihd.  1742 Samatag  1742 Samum  1819 Sandel(holz)  1825 Sapeke  1835 Sarafan  1845 Sarazene  1856  c Sarsche  1878 Sarong  1862 Safa«'  1867 Äa<m  2188 S(,/rt  1869 Schabbes  j.  1742 Schabbesgoj  j.  728 Schabracke  395 Schach  1762 Schacherjude  1763 schachern  j.  1763 schachtnott  1443 schachzabel  mhd.  1762 Schachzngel  1762 Schäfzngel  1762 si-haqgün  mhd.  434 Sc-Äa/i  1762 Schakal  1929
6160:sabhalh  1742 sacÄ;  1781 sacre  1799 sa/f/-OM  2178 sa(/o  1761 saÄJÖ  2122 saÄ;er  1799 saZep  2001 sa/op  2001 sambook  1824 samp  m  1834 sandal  1825 Sanders  1825 sandle  1825
7426:cabacius  993 cabacus  993 caJaZZa  974 caballus  653 cabassmm  993 cadus  988 caladium  1153 calamina  1149 camelinum  653 camelotum  653 camelus  653 camphora  1100 candela  1053 cannabis  1248 capparis  978 capsa  993 capulum  766 carabe  1004 carcannum  1096  b careum  1087 carratus  1182 carthamus  1262
```


## [2026-09-06T15:51:05.667Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB sandal ===\"; grep -n \"SANDAL\\|Sandal-wood\\|candana\" HJB.txt | head -10\necho \"=== AFM ===\"; grep -n \"صندل\\|سندروس\\|قنديل\\|كندر\" AFM_pages.txt | head -10",
 "description": "Grep Hobson-Jobson and Addi Shir"
}
```


### [2026-09-06T15:51:05.757Z] TOOL RESULT

```
=== HJB sandal ===
4675:1759.— "These  Vakeels  .  .  .  stated  that the  Rani  (of  Bednore)  would  pay  a  jrearly sum  of  100,000  Hoons  or  Pagooas,  besides  a tribute  of  other  valuable  articles,  such  as Foful  (betel),  Dates,  Sandal-wood,  XaJcnl .  .  .  black  pepper,  &c." — Hitt.  of  Mydur Naik,  183.
12187:o.  1500. — "In  the  town  of  Pursotem  on the  baiiJcs  of  the  sea  stands  the  temple  of Jagnant,  near  to  which  are  the  images  of Eishen,  his  brother^  and  their  sister,  made of  Sandal-wood,  which  are  said  to  be  4,000 years  old.  .  .  .  The  Brahmins  ...  at  cer- tain times  carry  the  image  in  procession upon  a  carriage  of  sixteen  wheels^  which  in the  Hindooee  language  (is  called  Rahth  (see BUT) ;  and  they  believe  that  whoever  assists in  drawing  it  along  obtains  remission  of  all his  maa."—Olad»in*t  Ayeen,  ii.  18-15 ;  [ed. JarMU,  ii.  127].
19186:789    SANDAL,  SANDLE,  SANDERS.
19212:SANDAL,  SANDLE,  SANDEBS, SANDAL-WOOD,  s.  From  Low Latin  santalum,  in  Greek  <rdrra\oy, and  in  later  Greek  adydofoir  ;  coming from  the  Arab,  sandal,  and  that  from Skt.  chandana.  The  name  properly beloncs  to  the  fragrant  wood  of  the Santalum  album,  L.  Three  woods bearing  the  name  santalum,  white, yellow,  and  red,  were  in  officinal  use in  the  Middle  Ages.  But  the  name Red    Sandalwood,    or    Red    Sanders,
19213:SANDAL,  8ANDLE,  SANDERS.  790
=== AFM ===
571:» ( ܐܢܝܟ ) الكندر معرب بِسْتَك وهو الككندر الابيض وقيل صمغ سجر
1531:رتككى وجن اثاجى ' وفي بعض الاماكن « قنديل اغاحى 809 اغاجى وقره
2780:بالاتكاارة والفرنسمة ܙ 5020810 بالارطا 1 ܕ ܧ$83110@11101 ® وصندل
```


## [2026-09-06T15:51:07.652Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD sandarac ===\"; grep -n \"sandarac\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -5\necho \"=== WEB ===\"; grep -n \"sandarac\\|san-da-rac\" WEB_vol1.txt | head -5\necho \"=== PLA ===\"; grep -n -i \"sandal\\|kundur\\|qandil\" incoming/PLA/PLA_pages.txt | head -10",
 "description": "Grep FSD, Webster, Asbaghi"
}
```


### [2026-09-06T15:51:07.754Z] TOOL RESULT

```
=== FSD sandarac ===
FSD_vol4.txt:1996:North-African  tree  (CaHffrfs ffMOrfrfca/pfj),  yielding sandarac .       o   ..  t
FSD_vol4.txt:2002:ous  compound  contained  In  sandarac  that  remains  when  *   period  that  precedes  a   ^^uga
FSD_vol4.txt:34924:Thj"a-tl'ra,  1   fhal  a-tQl'ra  2   th^'a-tl'ra  n   [Grl  1   Same as  AKHissAR  2.  Bib  Per  1,  11 Thy-cs'tcs,  1   fhQi-cs'tIz  2thy-€s'te5  n   Cr  Myth  A   brother of  Atreus,  who,  being  banished  for  the  seduction  of  Aerope wife  of  Atreus,  «ent  Plcisthenes  to  kill  Atreus  See  Atreus and  Pi  eisthenes  —   Thj-es'te-an,  a   —   Thj  cstean  ban- quet, a   cannibal  feast  —   Thyesfean  revenge,  a   blood-feud Thy-i'a-dcs,  1   fhi-ai’e-diz,  2   thy-!'a-de|,  n   pi  (Gr] Class  Antiq  A   group  of  Attic  and  Delphian  women  who ■w  ent  j   early  to  Parnassus  to  celebrate  the  orgiastic  wor- ship of  Dionysos -'Thy '1-ad,  n   One  of  the  Thy  lades thy 'Inc  wood,  1   thoi'tn  2   thy  in  wood  mentioned  In Rev  11!,  12,  supposed  to  be  tbit  of  the  sandarac-tree  See 8ANDVRAC  (<  Gr  thy\non,  <   thylnoSt  ot  tha  tree  thyta] thy"la-cl-i'tis,  1   fliai'lo-si-oi'tis  or  -I'tis,  2   th\  *Ia-?i-I - tis  or  -i'tis,  n   Pathol  Inflammation  of  the  oil-glands of  the  skin,  commonly’  of  some  part  of  the  face,  often due  to  intemperate  use  of  strong  drink  [   <   Gr  tkylak- ion,  dim  oi  thulakos,  sack  ]   thj"la-ci'tist. thy'ia-cln(c®,  1   flioi'le-sm  or  -amn,  2   thS  'la-^Tn  or  -^tn,  n A   thylacminc  marsupial  (.Tkylacinus  cynocephalus)  See Tasm  nm  vn  w   olf,  under  Tasu  nvi  v   ( <   Thi  l.ncin  os  1
FSD_vol1.txt:11488:al  e-gar,  1   al  l-gdr  or  6   h-gSr;  2   fil  e-grtr  or  S   le-gar,  n.  (Dial.,  0f  sandarac-trec  (Caltltris  quadrlcalvls) ,   also  of  the  pine
FSD_vol1.txt:22987:Lytton,  and  of  a   poem  by  Thomas  Hood.  "   ar'ar,  1   Oriar;  2   firiiir.  n.  fMor.l  The  sandarac-tree.  ar'ari  ^x'  ?■.
=== WEB ===
5422:2. the wood of the sandaractree of Morocco. Al-ex-an/dri-in, n. a citizen of Alexandria. a. (Fr. alerte; It. all’ eria, on the watch; Al-ex-an/drine, 7. in prosody. an iambic line
7453:1. in anatomy, the elbow, 2. in architecture, a bracketlike projection supporting a cornice; a console. ; Ancon sheep; a breed of sheep, now extinct, which originated in Massachusetts in 1791: called also otter sheep. ar añ’cõ-năl, afi-cd/ne-al, a. pertaining to the elbow. afi/cOne, n, same as ancon. afi-co-né/us, n.; pl. añ-çõnë’i, [L. ancon, elbow.] a muscle at the back of the elbow joint, used in extending the forearm. afi’cO-noid, a. elbowlike. afi/co-ny, n. [prob. from Gr. ankn, elbow, on account of its shape.] a piece of half- wrought iron, in the shape of a bar in the middle, but rude and unwrought at the ends. {Rare.] 7 an’co-ra, n.; pl. afi/cG-rae, in zoology an anchor. -an/cy, see -ance, an-cyl’/6-st6me, n. any of a genus of hook- Wenn parasitic in man and some other mam- mals. an’cy-los’t6-mi‘a-sis, n. [Mod. L., from An- cylostoma, hookworm genus, from Gr. ankylos crooked, and stoma, the mouth; and ~iasis.| an infestation by hookworms. ; an-cy/roid, a. (Gr. ankyra, anchor, and eidos, shape.] in anatomy, anchor-shaped. $ and, conj. {ME. and, an; AS. and, ond; akin to G. und, O.H.G. unti, OS. endi, ON. enn; the original meaning was “thereupon, then, next. 1. also; in addition; moreover; as well as. Za plus; added to; as, six and two makes eight. 3. as a consequence or result; as, he told her and she wept. 4. if. [Obs.] 5. to; in order to; as, try and come tomor- row. [Colloq.} and so forth; and the rest; and such things; et cetera. an-dab/a:tism, z. blind struggling; uncer- tainty. [Obs.] An-da-lu’sian, a. of Andalusia, its An-da-lu/sian, n. Andalusia. 2. the Spanish dialect of Andalusia. 3. a Mediterranean variety of chicken like the leghorn. an-da-li/site, n. a mineral of different colors, occurring usually in thick lamellar forms and sometimes in rhombic prisms, composed chiefly of silica and alumina. Its name is derived from Andalusia, in Spain, where it was first discovered. än-dän’tẹe (or an-dan’té), a. and adv. [It., ppr. of andare, to walk.] in music, moderately slow; faster than larghetto and slower than alle- gretto. än-dän’te (or an-dan’té), n. a musical passage or composition in andante time. än-dän-ti’nō, a. and adv. [It., dim. of andante.] in music, a little faster than andante. an-dan-ti’n6, n. any composition or passage in andantino time. an/da-rac, n. same as sandarac. An-dé/An, n. pertaining to the Andes Moun- tains or their inhabitants. an’dés-ine, n. a triclinic feldspar containing both lime and soda. It was first discovered in the Andes. an’dés-ite, n. [from the Andes Mountains, in which it occurs.] a volcanic rock, the ground- mass of which is usually composed of feldspar microliths, containing crystals of plagioclase feldspar. 3 An’dine, a. pertaining to the Andes Moun- tains; Andean. z An-di/ra, n. [LL., from the native name.) a genus of tropical American trees, including the Andira inermis of the West Indies, a showy flowering tree yielding building timber and a medicinal bark: called also the cabbage tiree.
26602:valvis, the sandarac tree.
34120:cit’rén wood, 1. the wood of the Barbary pine or sandarac tree, Callitris quadrivalvis.
85446:gummi; Gr. kommi, gum.] f 1. a sticky substance given off by certain trees and plants, which dries into an uncrys- tallized, brittle mass soluble in water. | 2. any similar plant secretion, as resin. | 3. any plant gum processed for use in in- dustry, art, etc. 4. an adhesive, especially on the back of a postage stamp; glue; mucilage. 5. gum elastic; rubber. 6. any gum tree; also, its wood. 7. a part of a hollow gum log used as a beehive, trough, etc. [Dial.] 8. [pl.] overshoes or rubbers. 9, chewing gum. , acaroid gum or gum acaroides; a gum given off by certain species of Xanthorrhæa. gum ammoniac; ammoniac, a natural gum resin. ' gum anime or animi; same as anime. gum arabic or gum acacia; a gum usually de- rived from Acacia arabica and Acacia vera, used in medicine, in the manufacture of candy, etc. The East Indian variety is from Feronia elephantum. gum butea; a gum derived from Butea fron- dosa, used in medicine and the arts. gum dragon; gum tragacanth. gum elastic; same as caoulchouc. gum elemi; same as elemi. gum juniper; same as sandarac (resin). gum ladanum; the gum or resin of the Cistus ladaniferus. gum resin; a mixture of resin and gum. The gum resins do not flow naturally from plants, but are mostly extracted by incision, in the form of white, yellow, or red emulsive fluids, which dry and solidify. The most important species are olibanum, galbanum, scammony, gamboge, euphorbium, asafetida, aloes, myrrh, and ammoniac. gum sandarac; same as sandarac (resin). gum senegal; a gum resembling gum arabic, brought from Senegal, in Africa. gum tragacanth; a gum obtained from vari- ous Asiatic or east European shrubs and trees of the pea family: also tragacanth. gum, v.t.; gummed, pt., pp.; gumming, p$r. to coat,-unite, or stiffen with gum. gum, v.i. 1. to secrete or form gum. 2. to become sticky or clogged. gum an/i-m4l, the galago of Senegal, a lemur which feeds upon gums. gum/bd, n. [prob. of Indian or Negro origin.] 1. the okra plant. 2. the edible, sticky pods of this plant. 3. a soup thickened with unripe okra pods. 4. a fine, silty soil of the Western prairies, which becomes sticky and nonporous when wet: also gumbo soil. 5. a French patois spoken by Creoles and
=== PLA ===
8062:Ip,    -       zarbül:               "Sandalen"         8,        wahrscheinlich            aus     dem    pers.         FL      sarpäyi
8082:Jr          - zarbil:                "Sandalen"                  = zarbül           q. v.
10014:ders» - Sarbil:                "Sandalen!              4     wahrscheinlich             aus    pers.     gt,. sarpäyi.
10578:dl. - sanädil:                     Pl.       v.     sandal           ag. v.
10590:Sanär                                                                             188                                            sandaldand
10613:Jr - sandal:                     "Sandelholz"                    <        pers.)yo Sandal                I mp.)sı9 tandal          12     syr.
10616:       Sandale:              aind.            candanah                     Sandale           "leichte       Fußbekleidung"               pers.>
10619:        Sandale             lat.                  sandalia Fe griech.                         sandalion;          zu neupers.      sändäl            .
10622:al            - sandaläni:                        "Apotheker"               = saidaläni              q. v.
10625:eis           -    sandaldanaf:                        "Sandelsamen"                    <Tpers.         &ly).,,    sandaldäne      16,
```


## [2026-09-06T15:51:19.600Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 kand ===\"; grep -n \"kand-\\|candeo\\|candela\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== ARY kand ===\"; grep -n -i \"KAND\\|candere\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Walde-Pokorny and Aryanpur"
}
```


### [2026-09-06T15:51:19.662Z] TOOL RESULT

```
=== WLD Bd1 kand ===
33120:glanzend", candor ,.blendend weifie Farbe, Lichtglanz", candela, candelabrum
33126:  Ygl. Curtius 5 522, Yanicek LEWb. 2 309, Yf. LEWb. 2 u. candeo cicindela,      ,
33136:u. candeo; nach Petersson LUA. 1915, 6 als *kun-ti- zu *ku-en-, *keu-
72700:Gdf. etwa * kom-dau'o -; niclit zu lat. candeo usw., Wz. (s)qand -, nach Fick
=== ARY kand ===
1834:AKANDAN, AKANDE, AKANESH (u61~ 81 dist oaisl ais) — (PERSIAN) qui
1837:GONEJETE, GANA-, GONETI, ‘AGANDAN,AKANDAN.(PAHLAVI) 5 sy,
6739:KANDU (LITHUANIAN) gle}
7061:CHICHTAC POLISH) ling) KHANUEL.KANDA
7606:KANDE, KAN DANISH) Sheil HOSSETIC) guy)
11076:SCITAN :(OLD ENGLISH) A Sl SHIKANDIN _ (KURDISH) 53,5
11971:| KANDAN, KANTAN | :(PAHLAVD) 514
11973:TOKORN St=CS~S*~S~Sa KENAN, CHIKANDIN:(KURDISH) 52,5
11975:AMINDAROV: (DIG) 212 KANDAL, KINDEL
```


## [2026-09-06T15:51:20.532Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== DEV santal ===\"; grep -n -i \"santal\\|sandarac\\|candi\" DEV.txt | head -10\necho \"=== PHN ===\"; grep -n -i \"santal\\|sandarac\" PHN.txt | head -8",
 "description": "Grep Devic and Pihan"
}
```


### [2026-09-06T15:51:20.592Z] TOOL RESULT

```
=== DEV santal ===
474:Alpuémc.  Ancien  terme  de  pharmacie  :  sucre  candi, sucre  d'orge,  pâte  faite  d'amandes  et  de  sucre,  etc.  Esp. alfenique ,  port.  aJfenim.  De  l'arabe  *>sylÀ]i  al-fânid,  qui vient  du  persan  ù^ii  fânid  ou  ^x^jU  pâmdli,  sucre  purifié, sacchavum  pcnidium,  dit  Meninski.  11  y  a  un  verbe  persan fj>y^\à  jûmden  qui  signifie  rajjfiner  le  sucre.
475:L'ancienne  pharmaceutique  disait  pénide  pour  sucre tors.  C'est  le  même  mot  persan.  On  a  r np^woché  peiiidium du  grec  tsvviov,  réseau  de  fils ,  trame ,  parce  que  la cristallisation  du  sucre  candi  s'obtient  au  moyen  de  fds tendus  dans  la  dissolution  sucrée.
956:Candi  (Sucre).  Esp.  cande,  candi,  portug.  candil  et  ital. candito  (dans  un  texte  de  i3io^).  De  l'adjectif  (^*XJL»  ^mi- dï  formé  sur  l'arabe-persan  ùsXiqand,  sucre  de  canne,  mot d'origine  hindoue.
1005:'  Voij.  (h  Coniitanlinnpla  à  Sniyrnc  H  (ïnns  Vth'do.  Candie,  dans  la  (X)lloc- lion  Smilli,  f.  XI ,  p.  .S()0,  noie  y.  Cel  impôt,  dit  le  même  voyagenr,  est  d'en- viron 10  piastres  turques  (nioins  de  10  l'rancs).  Les  femmes  et  les  enfants au-dessous  de  dix  ans  n'y  sont  poini  assujellis  {U)id.  j>.  371,  noie  2  ).
1021:'■'  l'oy.  de  Constantinople  à  Smyrne  et  dans  l'île  de  Candie,  dans  la  collec- tion Smith,  t.  XI,  p.  890,  note  2.  Cet  impôt,  dit  le  même  voyageur,  est  d'en- viron 10  piastres  turques  (moins  de  10  francs).  Les  femmes  et  les  enfants au-dessous  de  dix  ans  n'y  sont  point  assujettis  {Ihid.  p.  871,  note  2  ).
1564:•'  '<  A  Trapsano  (Candiiî),  il  y  a  une   .'ji'andc   fabrique  de  marmiles  de
1954:'^  Vo]/ag(>  de  Constanlinople  à  Smyrne  et  dans  Vile  de  Candie ,  dans  la  collecl. Smilli,  t.  XI,  p.  390,  noli3  9.
2064:Sandal  ou  Santal.  Esp.  portug.  ital.  sandalo.  Malgré  le grec  (jolvtôXov^  il  paraît  probable  que  sandal  et  sandalo qui  ont  un  d  et  non  un  t  sont  venus  par  l'arabe  J^K^uo sandal,  ou  du  moins  ont  subi  son  influence.  Le  mol  est d'origine  indienne.
3182:Candi.
3183:Candil,/>^.  voy.  Candi. Candito,  itaL  voy.  Candi. Caufora,  ital.  voy.  Camphre. Cangiar,  voy.  Alfange. Canna ,  h.  lat.  voy.  Cuine. Canque,  voy.  Cainocan. Capacho ,  esf.  voy.  Cabas. Capaza,  esp.  voy.  Cabas. Capazo,  esp.  voy.  Cabas. Caphar. Caphura,  h.  lat.  voy.  Camplire.
=== PHN ===
8912:SANDAL et SANTAL, s. m. (a.)
10852:Sandai et Santal, s. m. (a.) ^ 395
```


## [2026-09-06T15:51:28.233Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=32900 && NR<=33130 && /pdf page/{p=$0} END{print \"WLD Bd1 tag before 33120: \"p}' incoming/WLD/WLD_Bd1_pages.txt\nsed -n '33112,33130p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "WLD kand entry context"
}
```


### [2026-09-06T15:51:30.617Z] TOOL RESULT

```
WLD Bd1 tag before 33120: 
&qcl£ Ides.  alb. geg. hqne, tosk. hens „Mond“ ( *sqandna
               ;
                                                                G. Meyer Alb.
                                                                         ,


Wb. 151, Alb. St. Ill 59); lat. candco, -ere „glanzen, schimmern, hell glfihen",
trans. *cando, -ere in accendo , incendo „zfinde an", candidus „blendend weili,
glanzend", candor ,.blendend weifie Farbe, Lichtglanz", candela, candelabrum
„Leuchter“ (daraus cymr. usw. cannwyll ds.), cicindela „Leuchtkaferchen,
Ollampe", cicendula „Lampchen“ (redupl. *ce-cand -); cymr. cann „wei£i,
hell", mbret. cann „Vollmond“, abret. cant „canus“ (Fick II 4 90, Prellwitz 2
207; Entlehnung aus candidus nimmt Pedersen KG. I 199 an, kaum alien
Anwendungen genfigend).
  Ygl. Curtius 5 522, Yanicek LEWb. 2 309, Yf. LEWb. 2 u. candeo cicindela,      ,


Reichelt KZ. 46, 311. Lat. kelt. alb. gr. -an- mfissen gleichen Ursprungs
                                                             2
```


## [2026-09-06T15:51:31.247Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/239.jpg 2>/dev/null; pdftoppm -f 239 -l 239 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg239 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 239"
}
```


### [2026-09-06T15:51:33.759Z] TOOL RESULT

```
site/pages/239.jpg
total 7068
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:51 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     902 Sep  6 11:50 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:49 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:51:37.917Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg239.png"
}
```


### [2026-09-06T15:51:38.308Z] TOOL RESULT

```

```


## [2026-09-06T15:51:38.304Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:52:09.984Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 239 -l 239 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg239hi\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg239hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.53),int(h*0.44),int(w*0.80),int(h*0.50))).save('c239_kandid.png')\nim.crop((int(w*0.38),int(h*0.16),int(w*0.78),int(h*0.26))).save('c239_persian.png')\nim.crop((int(w*0.50),int(h*0.36),int(w*0.80),int(h*0.42))).save('c239_sandarus.png')\n\"\nls -la c239_*.png",
 "description": "Crop page regions at high res"
}
```


### [2026-09-06T15:52:15.010Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb  4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb  4087 Sep  6 11:52 c239_sandarus.png
```


## [2026-09-06T15:52:17.433Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c239_kandid.png"
}
```


### [2026-09-06T15:52:17.445Z] TOOL RESULT

```

```


## [2026-09-06T15:52:20.921Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg239hi.png'); w,h=im.size\nim.crop((int(w*0.52),int(h*0.49),int(w*0.80),int(h*0.545))).save('c239_kandid2.png')\n\"",
 "description": "Crop kandid box"
}
```


### [2026-09-06T15:52:23.356Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:52:25.635Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c239_kandid2.png"
}
```


### [2026-09-06T15:52:25.654Z] TOOL RESULT

```

```


## [2026-09-06T15:52:32.339Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c239_persian.png"
}
```


### [2026-09-06T15:52:32.527Z] TOOL RESULT

```

```


## [2026-09-06T15:52:32.525Z] INPUT

[Image: original 2040x660, displayed at 2000x647. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-06T15:52:37.383Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c239_sandarus.png"
}
```


### [2026-09-06T15:52:37.396Z] TOOL RESULT

```

```


## [2026-09-06T15:52:52.198Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg239.png data/verification/sources/refs/ocr/BOOK/239.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page PNG for audit"
}
```


## [2026-09-06T15:52:54.022Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"کاندید\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== qandil in MON ===\"; grep -n \"قندیل\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in for kandid and qandil"
}
```


### [2026-09-06T15:52:54.516Z] TOOL RESULT

```
total 9964
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:52 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


### [2026-09-06T15:52:54.589Z] TOOL RESULT

```
=== qandil in MON ===
MON_part1.txt:26219:ریز و خوشبو است؛ زهرة القندیل» علف 
MON_part1.txt:51088:نوعی جار یا قندیل بزرگ که شمع‌ها یا 
MON_part1.txt:80548:دیگر محرمات. سنگ بر قندیل زدن: با 
MON_part1.txt:80549:سنگ قندیل را شکستن. (کد.) تاریکك 
MON_part2.txt:15141:باشد)؛ قنادیل. قندیل ترسا: قندیلی که
```


## [2026-09-06T15:52:57.151Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15130,15150p' MON_part2.txt",
 "description": "Read Mo'in qandil entry"
}
```


### [2026-09-06T15:52:57.198Z] TOOL RESULT

```
هر شیرابةٌ دیگر گیاهی که در برابر هوا 
انجماد بابد؛ ذ کر شده است. 

قند ز: ۲۵۱-62 آمعر وت (امر.) کهن دژ؛ 
قلعه قد یم و 

ندشکن: 7-10 [معر. ف. 
قندشکننده] (ص‌فا. .) چکشی که ۳ 
کلوخه‌های قند را به اجزاء تقسیم کنند. 
تندیل: [معر.] (.) چراغ. چراغدان» 
شمعدن (مخصوصاً که از سقف آویزان 
باشد)؛ قنادیل. قندیل ترسا: قندیلی که 
پیوسته در کلیسا آویخته باشند. قندیل چرخ: 
( کد.) آفتاب و ماه. قندیل دوسر: ( کد.) 
آسمان. قندیل شب: سیاهی شب. قندیل 


فرهنک فارسی معین 


قنداق
```


## [2026-09-06T15:53:08.285Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%CF%83%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CE%B1%CE%BD%CE%B4%CE%B1%CF%81%CE%AC%CE%BA%CE%B7\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AF%D9%84%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF%D9%8A%D9%84\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%86%D8%AF%D8%B1%D9%88%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kend-\" \\\n \"https://www.etymonline.com/word/sandalwood\" \\\n \"https://www.etymonline.com/word/sandal\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 239, root Kand 1/Qand: sandal/sandalwood/sandarac/qandil/candidus verification\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:53:13.599Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4256f2f8a52fa443.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/666de69580abbea4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/420cc69c9eaf66dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5fcf45d4670eb33f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49dcd2888b925912.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0ece6af7cb91914.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ebede1367d168394.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9ed69110b561d5bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2016d6d7b3cefca2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f8bbae5259a49c2.txt
```


## [2026-09-06T15:53:16.588Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-06T15:53:16.631Z] TOOL RESULT

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


## [2026-09-06T15:54:29.251Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD kundur ===\"; grep -n -i \"kundur\\|kwndl\\|candal\" PHD.txt PHD_mackenzie.txt | head\necho \"=== NYB ===\"; grep -n -i \"kundur\\|kwndlwk\" NYB_vol2_glossary.txt | head\necho \"=== SKT candid/candle ===\"; grep -n \"^Candid\\|^Candle\\|^Chandelier\\|Candidate\" SKT.txt | head",
 "description": "Grep MacKenzie, Nyberg, Skeat"
}
```


### [2026-09-06T15:54:29.329Z] TOOL RESULT

```
=== PHD kundur ===
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD.txt:2036:frankincense kundur.
PHD.txt:5022:kundur kün künmarz kunjid kunjid kunišngar kunišn karak, kūk kūr
PHD_mackenzie.txt:3356:kundur [kwndll N ,...,] frankincense.
PHD_mackenzie.txt:6618:   xwarisn; ......, and drink xwiir-bar.     frankincense kundur.
PHD_mackenzie.txt:8470:casmarcskih    AU~-E:U~               candal                      '\..,,~
PHD_mackenzie.txt:9553:                          ~'V,~                 kundur                          ~,,~
=== NYB ===
=== SKT candid/candle ===
```


## [2026-09-06T15:54:36.216Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"candal\" PHD.txt PHD_mackenzie.txt | head -5\necho \"=== SKT candle ===\"; grep -n -i \"Candle\\|Candid\" SKT.txt | head -5",
 "description": "Grep candal and Skeat candle"
}
```


### [2026-09-06T15:54:36.276Z] TOOL RESULT

```
PHD_mackenzie.txt:8470:casmarcskih    AU~-E:U~               candal                      '\..,,~
=== SKT candle ===
275:sconce  {^^,  a  candlestick.  (F.  «  L.) M.  E  s<ance,  scimi,  a  covered  light,  lantcin. «0.  F.  t^(0»s/,  a.  dark  bintcni  (kot|ucfort). wt..  aJfsumsa,  a  dark  Inntem  ^ia  late  L.) ; from  L.  tUncortJUi,  hidden.
2792:Cannel-ooal ;  see  Candid.
3225:Ceneer;  see  Candid.
8891:hustings.  (Scand.)  The  ntod.  nse  is incorrect ;  k  is  properly  Mui/mg;  sing., and  means  a  council,  an  assembly  for  the choice  of  a  candidate.  M.  £.  ktistin^. A  S.  hthtittg.^\cc\.  kiis]ttng,  a  council, meeting.  —Ice!.  hUs,  a  house ;  |»/*^,  a  thing. aUo  un  assembly ;  see  Thing.  Cf.  Swed. and  Dan.  tittff,  the  same  as  Icel.  )finj^\  and the  Swed.  form  better  accounts  for  the  £. form. huswife.  (E.)    I.e.  keusewife.
9134:Inoandesoent ;  see  Candid.
```


## [2026-09-06T15:54:48.953Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Candid\\.\" SKT.txt | head -3\nawk 'BEGIN{RS=\"\\f\"} /Candid,/{print NR; print substr($0,1,900)}' SKT.txt | head -20",
 "description": "Skeat candid entry"
}
```


### [2026-09-06T15:54:50.656Z] TOOL RESULT

```
2792:Cannel-ooal ;  see  Candid.
3225:Ceneer;  see  Candid.
9134:Inoandesoent ;  see  Candid.
```


## [2026-09-06T15:54:54.578Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"candere, to glow\\|candidus\\|candela\" SKT.txt | head -5\necho \"=== FSD sandarac entry ===\"; grep -n \"san'da-rac\\|sandarac,\\|SANDARAC\" FSD_vol4.txt | head -5",
 "description": "Skeat candid text and FSD sandarac"
}
```


### [2026-09-06T15:54:54.644Z] TOOL RESULT

```
2737:CANDELABRUM.
=== FSD sandarac entry ===
1992:Baii"da-na',  1   eiin  da-na',  2   6aa'da-na',  «   (P  II  A   diptero-  poor  possesses  so  many  good  qualities  that  ho  Is  held  up  as  a carpaceoostre”  tAnisopma  oMongd)  yielding  a   fragrant  gum  pattern  to  the  wealthy  but  111  behaved  Tommy  ^   [gland san'dang,  1   sQn'daq,  2   san'dang,  7»  [P  1   ]   A   marine  mile  Sand'gate,  1   sand'gCt,  2   sand'£fit  n   A   town  In  Kent,  En- san'da-rac,  1   san'do-rak,  2   sXn'da-r&c.  n   1.  A   pale-jel- Saiid'ham,  ti  Same  as  SandowaN  ,
1995:pan'da-racbf,— san'da-rac-tree",  n   1   A   medium-sized  San'dh!*,  n   [Sans  I   The  last  sixth  of  a   Yuga  or  of  a   Man-
```


## [2026-09-06T15:54:59.897Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sanmda-rac\\|san'da-rac\\|sandarac, n\\|sandarac\\b\" WEB_vol1.txt | head -8\ngrep -n -o \"sandarac[^.]\\{0,200\\}\" WEB_vol1.txt | sed -n '1,6p'",
 "description": "Webster sandarac"
}
```


### [2026-09-06T15:55:02.145Z] TOOL RESULT

```
7453:1. in anatomy, the elbow, 2. in architecture, a bracketlike projection supporting a cornice; a console. ; Ancon sheep; a breed of sheep, now extinct, which originated in Massachusetts in 1791: called also otter sheep. ar añ’cõ-năl, afi-cd/ne-al, a. pertaining to the elbow. afi/cOne, n, same as ancon. afi-co-né/us, n.; pl. añ-çõnë’i, [L. ancon, elbow.] a muscle at the back of the elbow joint, used in extending the forearm. afi’cO-noid, a. elbowlike. afi/co-ny, n. [prob. from Gr. ankn, elbow, on account of its shape.] a piece of half- wrought iron, in the shape of a bar in the middle, but rude and unwrought at the ends. {Rare.] 7 an’co-ra, n.; pl. afi/cG-rae, in zoology an anchor. -an/cy, see -ance, an-cyl’/6-st6me, n. any of a genus of hook- Wenn parasitic in man and some other mam- mals. an’cy-los’t6-mi‘a-sis, n. [Mod. L., from An- cylostoma, hookworm genus, from Gr. ankylos crooked, and stoma, the mouth; and ~iasis.| an infestation by hookworms. ; an-cy/roid, a. (Gr. ankyra, anchor, and eidos, shape.] in anatomy, anchor-shaped. $ and, conj. {ME. and, an; AS. and, ond; akin to G. und, O.H.G. unti, OS. endi, ON. enn; the original meaning was “thereupon, then, next. 1. also; in addition; moreover; as well as. Za plus; added to; as, six and two makes eight. 3. as a consequence or result; as, he told her and she wept. 4. if. [Obs.] 5. to; in order to; as, try and come tomor- row. [Colloq.} and so forth; and the rest; and such things; et cetera. an-dab/a:tism, z. blind struggling; uncer- tainty. [Obs.] An-da-lu’sian, a. of Andalusia, its An-da-lu/sian, n. Andalusia. 2. the Spanish dialect of Andalusia. 3. a Mediterranean variety of chicken like the leghorn. an-da-li/site, n. a mineral of different colors, occurring usually in thick lamellar forms and sometimes in rhombic prisms, composed chiefly of silica and alumina. Its name is derived from Andalusia, in Spain, where it was first discovered. än-dän’tẹe (or an-dan’té), a. and adv. [It., ppr. of andare, to walk.] in music, moderately slow; faster than larghetto and slower than alle- gretto. än-dän’te (or an-dan’té), n. a musical passage or composition in andante time. än-dän-ti’nō, a. and adv. [It., dim. of andante.] in music, a little faster than andante. an-dan-ti’n6, n. any composition or passage in andantino time. an/da-rac, n. same as sandarac. An-dé/An, n. pertaining to the Andes Moun- tains or their inhabitants. an’dés-ine, n. a triclinic feldspar containing both lime and soda. It was first discovered in the Andes. an’dés-ite, n. [from the Andes Mountains, in which it occurs.] a volcanic rock, the ground- mass of which is usually composed of feldspar microliths, containing crystals of plagioclase feldspar. 3 An’dine, a. pertaining to the Andes Moun- tains; Andean. z An-di/ra, n. [LL., from the native name.) a genus of tropical American trees, including the Andira inermis of the West Indies, a showy flowering tree yielding building timber and a medicinal bark: called also the cabbage tiree.
26602:valvis, the sandarac tree.
34120:cit’rén wood, 1. the wood of the Barbary pine or sandarac tree, Callitris quadrivalvis.
85446:gummi; Gr. kommi, gum.] f 1. a sticky substance given off by certain trees and plants, which dries into an uncrys- tallized, brittle mass soluble in water. | 2. any similar plant secretion, as resin. | 3. any plant gum processed for use in in- dustry, art, etc. 4. an adhesive, especially on the back of a postage stamp; glue; mucilage. 5. gum elastic; rubber. 6. any gum tree; also, its wood. 7. a part of a hollow gum log used as a beehive, trough, etc. [Dial.] 8. [pl.] overshoes or rubbers. 9, chewing gum. , acaroid gum or gum acaroides; a gum given off by certain species of Xanthorrhæa. gum ammoniac; ammoniac, a natural gum resin. ' gum anime or animi; same as anime. gum arabic or gum acacia; a gum usually de- rived from Acacia arabica and Acacia vera, used in medicine, in the manufacture of candy, etc. The East Indian variety is from Feronia elephantum. gum butea; a gum derived from Butea fron- dosa, used in medicine and the arts. gum dragon; gum tragacanth. gum elastic; same as caoulchouc. gum elemi; same as elemi. gum juniper; same as sandarac (resin). gum ladanum; the gum or resin of the Cistus ladaniferus. gum resin; a mixture of resin and gum. The gum resins do not flow naturally from plants, but are mostly extracted by incision, in the form of white, yellow, or red emulsive fluids, which dry and solidify. The most important species are olibanum, galbanum, scammony, gamboge, euphorbium, asafetida, aloes, myrrh, and ammoniac. gum sandarac; same as sandarac (resin). gum senegal; a gum resembling gum arabic, brought from Senegal, in Africa. gum tragacanth; a gum obtained from vari- ous Asiatic or east European shrubs and trees of the pea family: also tragacanth. gum, v.t.; gummed, pt., pp.; gumming, p$r. to coat,-unite, or stiffen with gum. gum, v.i. 1. to secrete or form gum. 2. to become sticky or clogged. gum an/i-m4l, the galago of Senegal, a lemur which feeds upon gums. gum/bd, n. [prob. of Indian or Negro origin.] 1. the okra plant. 2. the edible, sticky pods of this plant. 3. a soup thickened with unripe okra pods. 4. a fine, silty soil of the Western prairies, which becomes sticky and nonporous when wet: also gumbo soil. 5. a French patois spoken by Creoles and
5422:sandaractree of Morocco
7453:sandarac
26602:sandarac tree
34120:sandarac tree, Callitris quadrivalvis
85446:sandarac (resin)
85446:sandarac; same as sandarac (resin)
```


## [2026-09-06T15:55:13.758Z] AGENT

Now writing the verification file.


## [2026-09-06T16:02:07.917Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nA=\"https://en.wiktionary.org/wiki/%CF%83%CE%AC%CE%BD%CE%B4%CE%B1%CE%BB%CE%BF%CE%BD\"\nB=\"https://en.wiktionary.org/wiki/%CF%83%CE%B1%CE%BD%CE%B4%CE%B1%CF%81%CE%AC%CE%BA%CE%B7\"\nC=\"https://en.wiktionary.org/wiki/%E0%A4%9A%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%A8\"\nD=\"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AF%D9%84%DB%8C\"\nE=\"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%AF%D9%8A%D9%84\"\nF=\"https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%AF%D8%B1\"\nG=\"https://en.wiktionary.org/wiki/%D8%B3%D9%86%D8%AF%D8%B1%D9%88%D8%B3\"\nH=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/(s)kend-\"\nI=\"https://www.etymonline.com/word/sandalwood\"\nJ=\"https://www.etymonline.com/word/sandal\"\n\nnodes=[]\n\nnodes.append({\n \"id\":1,\"lang\":\"Sanskrit\",\"words\":\"kandrak : shining; kandana, kundruka : sandalwood\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Three different words are packed into one box. (1) 'kandrak' = Skt candra- (candraka-) 'shining, gleaming; moon' < *skand-ro-, the regular zero/full-grade -ro- adjective of the root; Pokorny 526 lists exactly 'candra- (scandra-, EN Hari-scandra-) leuchtend, glaenzend, brennend; m. Mond' — confirmed. (2) 'kandana' = Skt candana- 'sandalwood'; Pokorny and Klein attach it to candra- ('wood for burning incense'), but Wiktionary/modern Indology treats it as probably a Dravidian loan (Tamil caantu 'Santalum tree', Malayalam caantu 'sandal paste'), so its membership in the IE root is only traditional. (3) 'kundruka' = Skt kunduru/kunduruka 'olibanum, frankincense (Boswellia)' — this is NOT a member of the *kand- family at all and does not mean 'sandalwood': it is a South-Asian/Near-Eastern culture word (Laufer, Sino-Iranica 585; Meyerhof even derives kondor/luban from Greek chondros). Nourai has fused the frankincense word (kunduru) with the sandalwood word (candana) and glossed both 'sandalwood', which is the error that propagates down the whole left branch.\",\n \"derivation_fa\":\"در این خانه سه واژهٔ جداگانه در هم آمیخته است. نخست candra- سنسکریت «درخشان، ماه» که ساخت -ro- از ریشهٔ *(s)kend- است و پوکورنی (ص ۵۲۶) آن را زیر همین ریشه آورده؛ این بخش درست است. دوم candana- «صندل، چوب صندل» که پوکورنی و کلاین آن را به candra- («چوبی که برای بخور می‌سوزانند») بسته‌اند، ولی ریشه‌شناسی امروزی آن را احتمالاً وام‌واژه‌ای دراویدی می‌داند (تامیلی cāntu). سوم kunduru/kunduruka «کندر، لبان» که اصلاً از این ریشه نیست و معنایش «صندل» هم نیست بلکه صمغ درخت بوسولیا (کندر) است؛ لوفر آن را واژه‌ای فرهنگی هندی می‌داند. بنابراین نورایی «کندر» و «صندل» را یکی گرفته و همین خطا در سراسر شاخهٔ چپ نمودار تکرار شده است.\",\n \"sources\":[C,H],\n \"ref_check\":[{\"ref\":\"POK:526\",\"status\":\"partial\",\"note\":\"POK_full.txt line 43488ff, 'Root/lemma: kand-, skand- and (Old Indic) (s)kend-, Meaning: to glow; bright, *moon ... Page(s): 526' lists 'candra- ... luminous, gleaming, burning; m. moon' and 'candana- m.n. sandalwood (incense)' — supports words 1 and 2, but Pokorny has NO kunduru/kunduruka anywhere: word 3 is not in the cited page.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231 s.v. candid\",\"stance\":\"partial\",\"note\":\"'fr. candere ... which is cogn. with Gk. kandaros, glowing coal, OI. candrah, shining glowing, candana sandalwood (lit. wood for burning incense)' — Klein backs candra-/candana- but never mentions kunduru.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kand-\",\"stance\":\"partial\",\"note\":\"'kand-. To shine. 1. Suffixed (stative) form *kand-e- in Latin candere ... [Pok. kand- 526.]' — Watkins gives only the Latin family; no Sanskrit sandalwood/frankincense reflexes.\"},\n  {\"src\":\"SIN\",\"where\":\"SIN.txt leaf 413 = printed p.585, no. 45(480)\",\"stance\":\"contradicts\",\"note\":\"'kundur, incense (Boswellia thurifera). Skr. kunduru, kundura, kundu, kunduruka' — the meaning is incense/olibanum, not sandalwood; and Laufer's no. 37(368) keeps 'sandal ... Skr. candana' as a separate item.\"}]\n})\n\nnodes.append({\n \"id\":2,\"lang\":\"Pahlavi\",\"words\":\"kundurŭk : sandalwood\",\n \"verdict\":\"plausible\",\n \"derivation\":\"The FORM is Laufer's: Skt kunduruka- was taken into Middle Persian as *kundurūk (starred, i.e. reconstructed from Armenian kndruk, which Hübschmann derived from Iranian), the Skt -ka- suffix appearing as the ordinary MP -ūk/-ōk ending; the actually attested Book-Pahlavi word is kundur [kwndl] (MacKenzie 1971 p.51). The arrow Skt kunduruka- > Pahl. kundurūk is therefore sound. What is wrong is the GLOSS: kundur/kundurūk is frankincense/olibanum (Boswellia thurifera resin), never sandalwood — the Pahlavi word for sandalwood is candal (< Skt candana). And since kunduru- is not an inherited *kand- word, this node does not really belong under the root at all.\",\n \"derivation_fa\":\"صورت واژه از لوفر گرفته شده است: kunduruka سنسکریت در فارسی میانه به *kundurūk (با ستاره، یعنی بازسازی‌شده از ارمنی kndruk) درآمده و پسوند -ka سنسکریت به پسوند رایج -ūk فارسی میانه بدل شده است. صورت واقعاً گواهی‌شده در پهلوی کتابی kundur (مکنزی، ص ۵۱) است. پس پیکان «کنداروکَ سنسکریت ← کندروک پهلوی» پذیرفتنی است، اما معنی نادرست است: کندر همان لبان و صمغ درخت بوسولیاست نه چوب صندل؛ واژهٔ پهلوی برای صندل candal است. افزون بر این چون kunduru- واژه‌ای ارثی از ریشهٔ *kand- نیست، جای این خانه زیر این ریشه نیست.\",\n \"sources\":[F],\n \"ref_check\":[{\"ref\":\"SIN:585\",\"status\":\"partial\",\"note\":\"SIN.txt leaf 413 (printed p.585): 'Pahlavi *kunduruk and Armenian kndruk are directly traceable to Skr. kunduruka' — supports the form and the arrow exactly, but the same paragraph glosses kundur as 'incense (Boswellia thurifera)', contradicting Nourai's 'sandalwood'.\"}],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 430 / PHD_mackenzie.txt line 3356\",\"stance\":\"contradicts\",\"note\":\"'kundur [kwndl | N ~] frankincense.' — MacKenzie has kundur (no -ūk) and glosses it frankincense; his English-Pahlavi index gives 'sandalwood: candal' as a different word.\"},\n  {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt, grep 'kundur'\",\"stance\":\"silent\",\"note\":\"Nyberg's Pahlavi glossary has no kundur/kundurūk entry (grep returns nothing).\"},\n  {\"src\":\"BQT\",\"where\":\"BQT vol.3 printed p.1705, Mo'in's footnote 4 s.v. کندر\",\"stance\":\"supports\",\"note\":\"'لوفر گوید: kundur ... سانسکریت kunduru, kundura, kundu, kunduruka. شکل پهلوی kundurūk ... ارمنی kndruk ... از سانسکریت kunduruka می‌باشد (Sino-Iranica p.585)' — Mo'in reproduces exactly the Laufer passage Nourai cites.\"}]\n})\n\nnodes.append({\n \"id\":3,\"lang\":\"Persian\",\"words\":\"kondor «کُندر» : incense; sandal «سندل» : sandalwood, sandal shoe; sandalî «صندلی» : chair (originally made of sandalwood)\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Only the first word descends from the parent. (1) کُندر kondor 'frankincense, olibanum' < MP kundur (< Skt kunduru-), the ordinary Book-Pahlavi > New Persian continuation with no change beyond the loss of the MP -ūk suffix; Borhan-e Qate' p.1705 defines it as 'صمغ ... لبان' and Mo'in as 'خوشبو که از درخت کندر هندی به دست آورند ... لبان'; Arabic كندر kundur was borrowed FROM Persian (Wiktionary). The parenthetical variants the book prints beside it, چُندل / چُندن, are NOT variants of kondor: they are the Persian reflexes of Skt candana 'sandalwood' (MP čandal), a different tree and a different resin — Mo'in's own footnote in BQT p.664 says 'چندل (صندل) بیشتر محتمل است که در آسیای غربی از هند وارد شده باشد ... عربی صندل از سانسکریت candana'. (2) سندل sandal: in Persian lexicography سندل is the SHOE (BQT p.1174 'سندل کفش باشد'), while the sandalwood word is صندل, the Arabised form of چندل; neither can come from kundurūk. (3) صندلی sandalī 'chair' = Arabic صندل ṣandal 'sandalwood' + Persian -ī, i.e. 'of sandalwood', an old Persian-Arabic round trip (Persian čandal > Arabic ṣandal > Persian صندل/صندلی, and back into Arabic as ṣandaliyya). So the box mixes the frankincense line (from the parent) with the sandalwood line (from Skt candana, not from the parent).\",\n \"derivation_fa\":\"تنها واژهٔ نخست از خانهٔ مادر می‌آید. «کُندر» از فارسی میانهٔ kundur (از kunduru سنسکریت) است و در برهان قاطع (ص ۱۷۰۵) «صمغ ... لبان» و در فرهنگ معین «خوشبویی که از درخت کندر هندی به دست آورند» تعریف شده؛ عربی «كندر» خود وام‌گرفته از فارسی است. اما «چُندل، چُندن» که کتاب در کنار کُندر آورده، گونهٔ کندر نیستند بلکه بازماندهٔ candana سنسکریت (چندل فارسی میانه) یعنی چوب صندل‌اند؛ خودِ معین در حاشیهٔ برهان (ص ۶۶۴) می‌نویسد «چندل (صندل) بیشتر محتمل است که در آسیای غربی از هند وارد شده باشد ... عربی صندل از سانسکریت candana». «سندل» در فرهنگ‌های فارسی به معنی کفش است (برهان ص ۱۱۷۴: «سندل کفش باشد»)، و صورت مُعرَّبِ چندل «صندل» است. «صندلی» نیز از «صندل» عربی + یای نسبت فارسی ساخته شده، یعنی «صندلی‌جنس، ساخته از چوب صندل»، و دوباره به عربی به صورت صندلیّة رفته است. پس این خانه دو خانوادهٔ جدا (کندر و صندل) را به هم آمیخته است.\",\n \"sources\":[D,F,I],\n \"ref_check\":[\n  {\"ref\":\"SIN:585\",\"status\":\"supports\",\"note\":\"SIN.txt leaf 413: 'kundur, incense'; and no. 37(368) 'sandal (Arabic), čandan, čandal (Persian), sandalwood ... Skr. candana' — Laufer himself keeps the two words apart.\"},\n  {\"ref\":\"SIN:552\",\"status\":\"not_found\",\"note\":\"SIN.txt leaf 380 (printed p.552) is about Chinese/Persian hollyhock, mango and 'rose of China' — nothing about sandal or kondor. Laufer's index does list 'candana 552, 584', so p.552 mentions candana in passing, but the OCR of that leaf does not contain it.\"},\n  {\"ref\":\"BQT:664\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 122 (printed ≈664), Mo'in's footnote to چندن/چندل: 'هندی وارد فارسی شده و معرب آن صندل است' and 'چندل (صندل) ... فارسی چندان، چندل، ارمنی ..., عربی صندل از سانسکریت candana' — supports the Skt origin of the sandal words.\"},\n  {\"ref\":\"BQT:1174\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 637 (printed ≈1174): 'سندل کفش باشد و سندلک نیز گویندش. عنصری (بلخی) گوید ...' with Mo'in's note 'معرب آن صندل ... در زبان کنونی نیز sandale گویند' — the سندل entry is the SHOE.\"},\n  {\"ref\":\"BQT:1705\",\"status\":\"supports\",\"note\":\"BQT_v3_pages.txt pdf page 498, printed ۱۷۰۵: کندر entry, 'صمغی است که آن را مصطکی خوانند ... کندر لوبان باشد', with Mo'in's Laufer and Meyerhof footnotes.\"},\n  {\"ref\":\"MON:1930\",\"status\":\"partial\",\"note\":\"Mo'in's lexicon has صندل 'نوعی کفش که با بند به پا بندند' and صندلی immediately after (MON_part1.txt lines 90271-90273) — the س/ص region matches p.1929-1930, but the OCR lost the bracketed origin tag.\"}],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"MON_part2.txt line 27042 s.v. کندر\",\"stance\":\"supports\",\"note\":\"'کندر: kondor (ا.) (گیا.) خوشبو که از درخت کندر هندی بدست آورند ... لبان، لیبانون، شجرة اللبان' — frankincense, matching Nourai's gloss 'incense'.\"},\n  {\"src\":\"PLA\",\"where\":\"Asbaghi, Persische Lehnwoerter im Arabischen p.188 (PLA_pages.txt lines 10613-10619)\",\"stance\":\"supports\",\"note\":\"'sandal: \\\"Sandelholz\\\" < pers. sandal / mp. čandal ... aind. candanah' and separately 'Sandale \\\"leichte Fussbekleidung\\\" ... lat. sandalia, griech. sandalion' — Asbaghi keeps sandalwood and sandal-shoe apart, and routes the wood Skt > MP > Persian > Arabic.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1825 (LKT.txt line 4137)\",\"stance\":\"supports\",\"note\":\"'Ar. sandal: Indisches Farbholz [aus pers. čandal < sskr. candana]; hieraus gr. sandalion ... engl. sandal, sanders, dtsch. Sandel(holz)'.\"},\n  {\"src\":\"HRN\",\"where\":\"HRN.txt, grep kundur/kondor/čandal\",\"stance\":\"silent\",\"note\":\"Horn's Grundriss has no entry for these words (grep returns nothing).\"},\n  {\"src\":\"HUB\",\"where\":\"HUB.txt, grep kundur/candana\",\"stance\":\"silent\",\"note\":\"Huebschmann's Persische Studien is silent (grep returns nothing).\"}]\n})\n\nnodes.append({\n \"id\":4,\"lang\":\"Greek\",\"words\":\"santalon : sandal tree; santalion : sandal shoe\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Late/Byzantine Greek σάνταλον 'sandalwood' is real and does come from the Indian word — Hobson-Jobson p.789: 'From Low Latin santalum, in Greek santalon, and in later Greek sandanon; coming from the Arab. sandal, and that from Skt. chandana'; Wiktionary gives Greek σάνδανον through Gandhari. The mediation is therefore Indian/Prakrit and then Arabic (Lokotsch, Devic: 'Malgre le grec santalon, il parait probable que sandal et sandalo qui ont un d et non un t sont venus par l'arabe sandal'), not the Persian>Greek arrow drawn here. The second word is a different lemma altogether: Greek σανδάλιον is the diminutive of σάνδαλον 'sandal, shoe', which Beekes (EDG 2010) calls 'likely Pre-Greek or some other foreign source, in view of the alternation nd/mb' and Klein (p.1380) 'a word from Asia Minor (whence also Pers. sandal), orig. meaning shoe of the Lydian god Sandal (Kretschmer, IF 45, 270)'. It has delta, not tau, and no connection with sandalwood; the printed page's spelling 'santalion' is Nourai's own misprint/harmonisation.\",\n \"derivation_fa\":\"σάνταλον یونانی متأخر «چوب صندل» واژه‌ای واقعی است و از هند آمده؛ هابسن-جابسن (ص ۷۸۹) می‌نویسد از لاتینی پست santalum، در یونانی σάνταλον و در یونانی متأخر σάνδανον، برگرفته از «صندل» عربی و آن از candana سنسکریت. یعنی میانجی، هندی/پراکریت و سپس عربی است، نه فارسی چنان‌که پیکان کتاب نشان می‌دهد؛ دُویک نیز می‌گوید صورت‌های اروپایی چون «د» دارند نه «ت»، از راه عربی آمده‌اند. واژهٔ دوم اصلاً واژهٔ دیگری است: σανδάλιον مصغّر σάνδαλον «کفش، صندل» است که بیکس آن را پیش‌یونانی یا وام‌واژه‌ای بیگانه می‌داند و کلاین (ص ۱۳۸۰) آن را واژه‌ای از آسیای صغیر و در اصل «کفش خدای لیدیایی Sandal» می‌خواند. این واژه با «دال» است نه «تاء» و هیچ پیوندی با چوب صندل ندارد؛ املای «santalion» در متن چاپی خطای خود نورایی است.\",\n \"sources\":[A,J,I],\n \"ref_check\":[\n  {\"ref\":\"KLN:1380\",\"status\":\"contradicts\",\"note\":\"KLN_1966.txt line 33668, page marker '1380' on the next line: 'sandal, n. — L. sandalium, fr. Gk. sandalion, dimin. of sandalon, a word from Asia Minor (whence also Pers. sandal), orig. meaning shoe of the Lydian god Sandal' vs. 'sandalwood, n. — ML. sandalum ... fr. Arab. sandal, fr. OI. candanah'. Klein's page 1380 is exactly the page Nourai cites, and it separates the two words instead of deriving the shoe from the wood.\"},\n  {\"ref\":\"SKT:462\",\"status\":\"contradicts\",\"note\":\"SKT.txt leaf 440: 'Sandal, shoe. (F.-L.-Gk.) F. sandale. L. sandalium. Gk. sandalion, dimin. of sandalon, a wooden sole bound on to the feet with straps. Cf. Pers. sandal, a sandal.' — Skeat likewise keeps the shoe word separate and spells it with delta.\"}],\n \"consulted\":[\n  {\"src\":\"HJB\",\"where\":\"Hobson-Jobson p.789 (HJB.txt line 19212)\",\"stance\":\"partial\",\"note\":\"'SANDAL, SANDLE, SANDERS, SANDAL-WOOD, s. From Low Latin santalum, in Greek santalon, and in later Greek sandanon; coming from the Arab. sandal, and that from Skt. chandana.' — Greek santalon confirmed, but routed through Arabic, not Persian.\"},\n  {\"src\":\"DEV\",\"where\":\"Devic, Dictionnaire etymologique des mots francais d'origine orientale (DEV.txt line 2064)\",\"stance\":\"contradicts\",\"note\":\"'Sandal ou Santal ... Malgre le grec santalon, il parait probable que sandal et sandalo qui ont un d et non un t sont venus par l'arabe sandal, ou du moins ont subi son influence. Le mot est d'origine indienne.'\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1825\",\"stance\":\"partial\",\"note\":\"derives Gk sandalion (in the WOOD sense) from Arabic sandal, i.e. Greek is downstream of Arabic, not of Persian.\"}],\n \"error_in\":\"book\",\"book_prints\":\"santalion\",\"correct_form\":\"sandalion (Gk. σανδάλιον)\"\n})\n\nnodes.append({\n \"id\":5,\"lang\":\"Latin\",\"words\":\"\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Empty pass-through box. Two Latin forms actually fill it, and they belong to the two different words of node #4: Medieval Latin sandalum/santalum 'sandalwood' (Etymonline s.v. sandalwood: 'from Medieval Latin sandalum, from Late Greek santalon'), and Latin sandalium 'a slipper, sandal' from Gk sandalion (Klein, Skeat). Nourai's silent box is therefore right for the wood but conflates the shoe; and the Latin is Medieval/Late, not Classical.\",\n \"derivation_fa\":\"این خانه در کتاب تهی است. در واقع دو صورت لاتینی جای آن را می‌گیرد و هر یک به یکی از دو واژهٔ خانهٔ پیشین بازمی‌گردد: لاتینی میانه sandalum / santalum «چوب صندل» (اتیمانلاین: از یونانی متأخر santalon) و لاتینی sandalium «کفش سبک، صندل» از σανδάλιον یونانی. پس خانهٔ تهی برای «چوب صندل» درست است ولی کفش را نیز با آن یکی گرفته است؛ ضمناً این لاتینی، لاتینیِ میانه است نه کلاسیک.\",\n \"sources\":[I,J],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference in the book.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380\",\"stance\":\"supports\",\"note\":\"'sandalwood, n. — ML. sandalum (whence also OF. sandal)' and 'sandal, n. — L. sandalium'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 440\",\"stance\":\"supports\",\"note\":\"'F. sandale. L. sandalium.'\"}]\n})\n\nnodes.append({\n \"id\":6,\"lang\":\"French\",\"words\":\"\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Empty pass-through box = Old French sandal / sandale. Etymonline s.v. sandalwood: English sandell (late 14c.) 'from Old French sandale, from Medieval Latin sandalum'; Klein s.v. sanders: 'OF. sandre, a var. of sandal'. For the shoe the same French sandale (< L sandalium) is the vehicle. Both are well attested Old French forms of the 12th-14th c.\",\n \"derivation_fa\":\"خانهٔ تهی همان فرانسهٔ کهن sandal / sandale است. اتیمانلاین ذیل sandalwood می‌نویسد صورت انگلیسی sandell (اواخر سدهٔ ۱۴م) از فرانسهٔ کهن sandale و آن از لاتینی میانه sandalum آمده است؛ کلاین نیز sandre را گونه‌ای از sandal می‌داند. برای معنی «کفش» نیز همان sandale فرانسوی (از sandalium لاتینی) واسطه است. هر دو صورت در فرانسهٔ کهن سده‌های ۱۲ تا ۱۴ گواهی شده‌اند.\",\n \"sources\":[I,J],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference in the book.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380 s.v. sanders\",\"stance\":\"supports\",\"note\":\"'OF. sandre, a var. of sandal. See sandalwood.'\"},\n  {\"src\":\"DEV\",\"where\":\"DEV.txt line 2064\",\"stance\":\"supports\",\"note\":\"'Sandal ou Santal. Esp. portug. ital. sandalo.'\"}]\n})\n\nnodes.append({\n \"id\":7,\"lang\":\"English\",\"words\":\"sandal\",\n \"verdict\":\"plausible\",\n \"derivation\":\"English has two homophonous 'sandal' words and the chart's chain is right for only one of them. 'Sandal' = sandalwood: ME sandell (late 14c.), saundres (early 14c.) < OF sandale < ML sandalum < Late Gk santalon < Skt candana — exactly the drawn Greek>Latin>French>English chain (Etymonline s.v. sandalwood). 'Sandal' = the shoe (late 14c.) < OF sandale / ML sandalum < L sandalium < Gk sandalion, 'a word of unknown origin, probably foreign, perhaps from Persian' (Etymonline s.v. sandal) — same surface chain but a different etymon that has nothing to do with the Indian tree. Since Nourai's box gives no gloss, the node is right for the wood and wrong for the shoe.\",\n \"derivation_fa\":\"در انگلیسی دو واژهٔ هم‌آوای sandal هست و زنجیرهٔ نمودار تنها برای یکی از آن دو درست است. sandal به معنی «چوب صندل»: انگلیسی میانه sandell (اواخر سدهٔ ۱۴م) از فرانسهٔ کهن sandale، از لاتینی میانه sandalum، از یونانی متأخر santalon، از candana سنسکریت — دقیقاً همان زنجیرهٔ یونانی ← لاتینی ← فرانسوی ← انگلیسی که کتاب کشیده است. اما sandal به معنی «کفش» از sandalium لاتینی و σανδάλιον یونانی می‌آید که به گفتهٔ اتیمانلاین «واژه‌ای با خاستگاه نامعلوم، احتمالاً بیگانه، شاید فارسی» است و هیچ پیوندی با درخت هندی ندارد. چون خانهٔ کتاب معنی نداده، این گره برای «چوب صندل» درست و برای «کفش» نادرست است.\",\n \"sources\":[I,J],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference in the book.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380\",\"stance\":\"partial\",\"note\":\"two separate headwords 'sandal, n.' and 'sandalwood, n.'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 440\",\"stance\":\"partial\",\"note\":\"'Sandal, shoe. (F.-L.-Gk.)' — only the shoe word is entered, with a Greek, not Indian, source.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1825\",\"stance\":\"supports\",\"note\":\"'engl. sandal, sandle, sanders' listed among the descendants of the sandalwood word.\"}]\n})\n\nnodes.append({\n \"id\":8,\"lang\":\"Sanskrit\",\"words\":\"candrah-râga : bright red (resin from tree)\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Skt candra-rāga- is a transparent compound candra- 'moon, shining' + rāga- 'colour, redness' = 'having the brightness/redness of the moon'; the first member is the same *(s)kend- derivative as in node #1, so as a Sanskrit word it is legitimate and Nourai's root attachment for it is fine. It is, however, cited in the etymological literature only as a COMPARISON for Greek sandarake, not as a documented name of a resin: Klein p.1380 writes 'Cp. OI. candra-raga-, having the brightness of the moon. The first element of this compound means shining, bright', which is the wording behind Nourai's 'bright red (resin from tree)'. AHD's 1975 appendix does not list the word at all.\",\n \"derivation_fa\":\"candra-rāga- سنسکریت ترکیبی روشن است: candra- «ماه، درخشان» + rāga- «رنگ، سرخی»، یعنی «دارای درخشندگی/سرخی ماه». جزء نخست همان مشتق ریشهٔ *(s)kend- است که در گرهٔ نخست دیدیم، پس نسبت‌دادن آن به این ریشه درست است. اما این واژه در ادبیات ریشه‌شناسی تنها به عنوان «مقایسه» برای σανδαράκη یونانی آورده شده، نه به عنوان نام گواهی‌شدهٔ یک صمغ: کلاین (ص ۱۳۸۰) می‌نویسد «قس. سنسکریت candra-rāga- به معنی دارای درخشندگی ماه»، و همین جمله سرچشمهٔ معنی‌ای است که نورایی داده است. پیوست ریشه‌های هندواروپایی AHD اصلاً این واژه را ندارد.\",\n \"sources\":[B],\n \"ref_check\":[{\"ref\":\"AHD:1149\",\"status\":\"not_checked\",\"note\":\"AHD:1149 is a page of the 1975 New College main dictionary (the 'sandarac' entry), not of the IE appendix; the local AHD file is Watkins 1985 (appendix only) and it has no 'sandarac' and no candra-raga- (grep 'sandarac' in AHD_watkins1985.txt returns nothing). Not accessible.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380 s.v. sandarac\",\"stance\":\"supports\",\"note\":\"'Cp. OI. candra-raga-, having the brightness of the moon. The first element of this compound means shining, bright; see sandalwood.'\"},\n  {\"src\":\"POK\",\"where\":\"POK_full.txt, kand- p.526\",\"stance\":\"silent\",\"note\":\"Pokorny lists candra- but no compound candra-raga-.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kand-\",\"stance\":\"silent\",\"note\":\"no Sanskrit reflex given under kand- at all.\"}]\n})\n\nnodes.append({\n \"id\":9,\"lang\":\"Greek\",\"words\":\"sandarak, sandaraxĕ : a red resin from trees\",\n \"verdict\":\"disputed\",\n \"derivation\":\"The Greek words are genuine: σανδαράκη (with the by-form σανδαράχη, which is Nourai's 'sandaraxĕ') means 'realgar, red arsenic sulphide; red orpiment; sandarac resin' — the κ/χ alternation is itself the classic sign of a loanword. But the arrow from Sanskrit is not what modern scholarship holds. Klein only writes 'L. sandaraca, fr. Gk. sandarake, which is of Oriental origin. Cp. OI. candra-raga-' — a comparison, not a derivation. Beekes (EDG 2010), followed by Wiktionary, calls it 'long taken to be an Oriental loanword from an unknown source', floats an Akkadian compound 'yellow paint' (orpiment), and 'does not dismiss a Pre-Greek origin, in view of the variation k/kh'. A Sanskrit source is not accepted: the word denotes a MINERAL pigment in Greek from Aristotle onward, and only later the North-African conifer resin.\",\n \"derivation_fa\":\"واژه‌های یونانی واقعی‌اند: σανδαράκη (با گونهٔ σανδαράχη که همان «sandaraxĕ» نورایی است) به معنی «زرنیخ سرخ، رِئالگار» و سپس «صمغ سندروس» است؛ خودِ جابه‌جایی κ/χ نشانهٔ آشکار وام‌واژه بودن است. اما پیکانی که از سنسکریت کشیده شده، دیدگاه امروزی نیست. کلاین تنها می‌نویسد «از یونانی sandarakē که خاستگاه شرقی دارد؛ قس. سنسکریت candra-rāga-» یعنی مقایسه، نه اشتقاق. بیکس (فرهنگ ریشه‌شناختی یونانی، ۲۰۱۰) و به پیروی او ویکی‌واژه آن را «وام‌واژه‌ای شرقی از سرچشمه‌ای ناشناخته» می‌خوانند، احتمال ساختی اکدی به معنی «رنگ زرد» را پیش می‌کشند و خاستگاه پیش‌یونانی را نیز رد نمی‌کنند. پس ادعای نورایی را پژوهش امروزی نمی‌پذیرد.\",\n \"sources\":[B],\n \"ref_check\":[{\"ref\":\"AHD:1149\",\"status\":\"not_checked\",\"note\":\"page of the 1975 New College main dictionary; the local AHD file is the Watkins appendix only and has no sandarac entry.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380 s.v. sandarac\",\"stance\":\"partial\",\"note\":\"'L. sandaraca, fr. Gk. sandarake, which is of Oriental origin' — Oriental, source unspecified; the Sanskrit word is only 'Cp.'-ed.\"},\n  {\"src\":\"FSD\",\"where\":\"FSD_vol4.txt line 1992 s.v. san'da-rac\",\"stance\":\"silent\",\"note\":\"Funk & Wagnalls gives the substance ('a pale-yellow ... sandarac-tree, Callitris quadrivalvis') but the OCR of the etymology bracket is unreadable.\"},\n  {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt\",\"stance\":\"silent\",\"note\":\"volume 1 (A-L) only; sandarac occurs merely in cross-references ('an'da-rac, n. same as sandarac').\"}]\n})\n\nnodes.append({\n \"id\":10,\"lang\":\"Arabic\",\"words\":\"sendarŭs : a resinous tree\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Arabic سندروس sandarūs 'sandarac; the tree Tetraclinis articulata and its resin' is a Greek loan, as Nourai's own source states: Tobia al-Unaysi's Tafsir al-alfaz al-dakhila, printed p.37, has 'سندروس - يوناني' followed by 'وهو صمغ يترشح من أشجار افريقية' ('a gum exuding from African trees'). Wiktionary derives it more precisely from the Greek adjective σανδαράκινος 'orange-coloured, sandarac-like' rather than the bare noun, and notes that 'the Arabic term can well be considered an Aramaic loan', since the word is also in Classical Syriac, Jewish Babylonian Aramaic and Mishnaic Hebrew — i.e. the usual Hellenistic Greek > Aramaic/Syriac > Arabic road for materia medica.\",\n \"derivation_fa\":\"«سندروس» عربی، نام درخت Tetraclinis articulata و صمغ آن، وام‌واژه‌ای یونانی است و خودِ مأخذ نورایی همین را می‌گوید: طوبیا العنیسی در «تفسیر الألفاظ الدخیلة» (ص ۳۷) می‌نویسد «سندروس ـ یونانی» و سپس «وهو صمغ یترشح من أشجار افریقیة». ویکی‌واژه دقیق‌تر آن را از صفت یونانی σανδαράκινος «نارنجی‌رنگ» می‌گیرد و می‌افزاید که با توجه به وجود همین واژه در سریانی و آرامی بابلی و عبری میشنایی، عربی آن را به احتمال زیاد از راه آرامی گرفته است — همان مسیر همیشگی داروشناسی یونانی ← سریانی ← عربی.\",\n \"sources\":[G],\n \"ref_check\":[{\"ref\":\"TAD:37\",\"status\":\"supports\",\"note\":\"TAD_pages.txt leaf 40 (printed ≈37): 'سندروس - يوناني ... وهو صمغ يترشح من أشجار افريقية' — al-Unaysi marks the word Greek, exactly as the arrow says.\"}],\n \"consulted\":[\n  {\"src\":\"AFM\",\"where\":\"AFM_pages.txt, grep سندروس\",\"stance\":\"silent\",\"note\":\"Addi Shir's list of Persian Arabisms has no سندروس (grep returns nothing) — consistent with a Greek/Aramaic, not Persian, source.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380\",\"stance\":\"partial\",\"note\":\"Klein traces the European word through Latin only and does not treat the Arabic form.\"},\n  {\"src\":\"PLA\",\"where\":\"PLA_pages.txt, grep sandarus\",\"stance\":\"silent\",\"note\":\"Asbaghi does not list sandarūs among Persian loanwords in Arabic.\"}]\n})\n\nnodes.append({\n \"id\":11,\"lang\":\"Persian\",\"words\":\"sandarŭs «سَنْدَروس» : a resinous tree and its red resin\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Persian سندروس sandarūs is borrowed straight from Arabic سندروس, with no phonetic change (the Arabic ū is kept; Persian also uses it adjectivally for 'sandarac-coloured, yellow'). Mo'in's lexicon, the reference Nourai cites, has 'سندروس (ا.) (گیا.) سرو کوهی؛ صمغی که از گونه‌ای سرو کوهی استخراج می‌شود و در طب قدیم مورد استعمال بوده ... از مخلوط سندروس و روغن ... روغن کمان حاصل می‌کرده‌اند' — the mountain-cypress resin, matching the gloss. One caution: the variant the book prints in brackets, «سَندَره», is not a variant of sandarūs in Mo'in; the word سندره standing next to سندروس in the same column of Mo'in is glossed [= سنداره] حرامزاده 'bastard' and is an unrelated lemma, so the bracketed form looks like a column-neighbour picked up by mistake.\",\n \"derivation_fa\":\"«سندروس» فارسی مستقیماً از «سندروس» عربی وام گرفته شده و هیچ دگرگونی آوایی نیافته است (واو کشیدهٔ عربی نگه داشته شده)؛ در فارسی صفت‌وار هم به معنی «به رنگ سندروس، زرد» به کار رفته است. فرهنگ معین، همان مأخذی که نورایی یاد می‌کند، می‌نویسد: «سندروس (ا.) (گیا.) سرو کوهی؛ صمغی که از گونه‌ای سرو کوهی استخراج می‌شود و در طب قدیم مورد استعمال بوده ...» که با معنی نمودار می‌خواند. یک نکته: صورت «سَندَره» که کتاب در کمانک آورده، در معین گونهٔ «سندروس» نیست؛ «سندره» در همان ستون معین «[= سنداره] حرامزاده» معنی شده و واژه‌ای بی‌ربط است، پس به نظر می‌رسد از سرِ همسایگی ستونی به اشتباه به این خانه راه یافته باشد.\",\n \"sources\":[G],\n \"ref_check\":[{\"ref\":\"MON:1929\",\"status\":\"supports\",\"note\":\"MON_part1.txt line 80055: 'سندروس ... (ا.) (گیا.) سرو کوهی. (گیا.) صمغی که از گونه‌ای سرو کوهی استخراج می‌شود و در طب قدیم مورد استعمال بوده ...'; two lines further 'سندره [= سنداره] (اص.) حرامزاده'.\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"Borhan-e Qate', grep سندروس in BQT_v2_pages.txt\",\"stance\":\"silent\",\"note\":\"no سندروس headword found in the س volume OCR.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt / ARY_latin_index_pages.txt, grep سندروس\",\"stance\":\"silent\",\"note\":\"Aryanpur's IE-roots dictionary has no entry (the word is a Semitic-mediated Greek loan, outside its scope).\"},\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt line 80055\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}]\n})\n\nnodes.append({\n \"id\":12,\"lang\":\"Latin\",\"words\":\"sandraca : red pigment, red resin\",\n \"verdict\":\"transcription_suspect\",\n \"derivation\":\"The Latin word is sandaraca (four syllables), a straight transliteration of Gk σανδαράκη, used by Pliny for realgar/red arsenic and later for the resin; Klein: 'sandarac ... L. sandaraca, fr. Gk. sandarake'. The form 'sandraca' with the second -a- lost is not a Latin word the dictionaries know. I rendered pdf page 239 at 600 dpi and read the box: the printed page itself shows 'sandraca', so the extraction is faithful and the haplology is Nourai's own misprint. (Late/Vulgar Latin does show a syncopated sandraca in a few mediaeval alchemical spellings, but no standard dictionary heads the entry that way.)\",\n \"derivation_fa\":\"صورت لاتینی این واژه sandaraca است، برگردان مستقیم σανδαράκη یونانی، که پلینی آن را برای زرنیخ سرخ و سپس برای صمغ به کار برده است؛ کلاین می‌نویسد «sandarac ... از لاتینی sandaraca، از یونانی sandarakē». صورت «sandraca» با افتادن الف دوم واژه‌ای نیست که فرهنگ‌ها بشناسند. صفحهٔ ۲۳۹ نسخهٔ پی‌دی‌اف را با تفکیک ۶۰۰ نقطه بازنمایی و خواندم: خودِ متن چاپی «sandraca» دارد؛ پس خطای خوانش اسکن نیست بلکه خطای چاپی کتاب است (حذف هجای میانی).\",\n \"sources\":[B],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"not_checked\",\"note\":\"the reference is given without a page; the local AHD file (Watkins 1985 appendix) has no sandarac/sandaraca entry.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380 s.v. sandarac\",\"stance\":\"contradicts\",\"note\":\"'L. sandaraca, fr. Gk. sandarake' — with the medial -a-.\"},\n  {\"src\":\"LEW\",\"where\":\"LEW_1910.txt, grep sandaraca\",\"stance\":\"silent\",\"note\":\"Walde's Lateinisches etymologisches Woerterbuch does not treat this Greek loanword.\"},\n  {\"src\":\"FSD\",\"where\":\"FSD_vol4.txt s.v. sandarac\",\"stance\":\"silent\",\"note\":\"etymology bracket unreadable in the OCR.\"}],\n \"error_in\":\"book\",\"book_prints\":\"sandraca\",\"correct_form\":\"sandaraca\"\n})\n\nnodes.append({\n \"id\":13,\"lang\":\"English\",\"words\":\"sandarac\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"English sandarac (in Middle English sandaracha, 14th c., in alchemical and medical texts, first of realgar, then from the 16th c. of the North-African conifer resin) is a learned borrowing of Latin sandaraca, itself Gk σανδαράκη. The word has never been naturalised in form: it keeps the Latin stem intact with only the loss of the ending. Klein p.1380 gives precisely 'sandarac, n., 1) the sandarac tree; 2) resin obtained from this tree; 3) realgar. — L. sandaraca, fr. Gk. sandarake'. Only the ultimate Sanskrit link at node #8/#9 is doubtful; this last step is not.\",\n \"derivation_fa\":\"واژهٔ انگلیسی sandarac (در انگلیسی میانه sandaracha، سدهٔ ۱۴م، نخست به معنی زرنیخ سرخ و از سدهٔ ۱۶م به معنی صمغ درخت مخروطی شمال افریقا) وام‌گیری کتابی از لاتینی sandaraca و آن از σανδαράκη یونانی است. این واژه هرگز صورت بومی نیافته و ستاک لاتینی را دست‌نخورده نگه داشته و تنها پایانه را از دست داده است. کلاین (ص ۱۳۸۰) دقیقاً می‌نویسد «sandarac ... از لاتینی sandaraca، از یونانی sandarakē». تنها حلقهٔ سنسکریتیِ آغاز زنجیره (گره‌های ۸ و ۹) تردیدآمیز است، نه این گام پایانی.\",\n \"sources\":[B],\n \"ref_check\":[{\"ref\":\"AHD:1149\",\"status\":\"not_checked\",\"note\":\"1975 New College main-dictionary page; local AHD file is the Watkins appendix only, which has no sandarac.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.1380\",\"stance\":\"supports\",\"note\":\"'sandarac, n. ... L. sandaraca, fr. Gk. sandarake, which is of Oriental origin.'\"},\n  {\"src\":\"FSD\",\"where\":\"FSD_vol4.txt line 1992\",\"stance\":\"supports\",\"note\":\"'san'da-rac ... 1. a pale-yel[low resin]' with the sandarac-tree (Callitris quadrivalvis) — same word and sense in Funk & Wagnalls.\"},\n  {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt lines 26602, 34120\",\"stance\":\"partial\",\"note\":\"Webster vol.1 has only cross-references ('the wood of the Barbary pine or sandarac tree, Callitris quadrivalvis'); the headword is in the unavailable vol.2.\"}]\n})\n\nnodes.append({\n \"id\":14,\"lang\":\"Latin\",\"words\":\"candidus : glowing white; candidâre : to make white or bright; candidâtus : candidate (due to their white toga)\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Latin candeō, -ēre 'to glow, shine, be white' is the stative *kand-ē- of the root; from its participle stem comes the -idus adjective candidus 'dazzling white, gleaming', thence the denominative candidāre 'to make white' and its participle candidātus, used substantivally at Rome of an office-seeker because he canvassed in an artificially whitened toga (toga candida) — the semantic development Nourai gives is the standard one, already in Cicero. Pokorny p.526 lists 'Latin candeo, -ere gleam, shimmer, bright glow ... candidus blinding, dazzling white ... candela, candelabrum'; Walde-Pokorny I 352 has the same set.\",\n \"derivation_fa\":\"candeō, -ēre لاتینی «درخشیدن، سفید و تابان بودن» صورت حالتیِ *kand-ē- از ریشه است؛ از ستاک آن صفت candidus «سفید خیره‌کننده، درخشان» با پسوند -idus ساخته شده و از آن فعل candidāre «سفید کردن» و اسم مفعول candidātus. این واژهٔ اخیر در رم به داوطلب مقام گفته می‌شد، زیرا نامزدان هنگام رأی‌جویی جامهٔ سفیدشدهٔ ویژه (toga candida) می‌پوشیدند؛ همان تحول معنایی که نورایی آورده و از زمان سیسرون گواهی شده است. پوکورنی (ص ۵۲۶) و والده-پوکورنی (ج ۱ ص ۳۵۲) همین مجموعه را زیر ریشه آورده‌اند.\",\n \"sources\":[H],\n \"ref_check\":[\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt s.v. kand-: 'kand-. To shine. 1. Suffixed (stative) form *kand-e- in Latin candere, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. [Pok. kand- 526.]'\"},\n  {\"ref\":\"KLN:231\",\"status\":\"supports\",\"note\":\"KLN_1966.txt, page marker '230' at line 6325 and the entries immediately after (so p.231): 'candidate, n., one who seeks an office, etc. — L. candidatus, one aspiring to office, prop. pp. of candidare, to make bright or white, fr. candidus, glowing, white; so called because a candidat[e wore a white toga]'.\"}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"POK_full.txt kand- p.526\",\"stance\":\"supports\",\"note\":\"'Latin candeo, -ere gleam, shimmer, bright glow ... candidus blinding, dazzling white, gleaming, candor ... candela, candelabrum'.\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny Bd. I 352 (WLD_Bd1_pages.txt line 33120)\",\"stance\":\"supports\",\"note\":\"'lat. candeo, -ere glaenzen, schimmern, hell gluehen, trans. *cando, -ere in accendo, incendo zuende an, candidus blendend weiss, glaenzend, candor ..., candela, candelabrum Leuchter'.\"},\n  {\"src\":\"LEW\",\"where\":\"LEW_1910.txt s.v. candeo\",\"stance\":\"silent\",\"note\":\"OCR search for candeo/candidus in the local Walde 1910 file returns no usable entry.\"}]\n})\n\nnodes.append({\n \"id\":15,\"lang\":\"French\",\"words\":\"candidat\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"French candidat (attested 1467 in the Roman sense, current political sense from the 16th c.) is a learned borrowing straight from Latin candidātus, not an inherited popular form — the intact -did- and the final -at (rather than the *chandié one would expect from regular Old French sound change) mark it as a latinisme of the humanist period. Klein p.231 explicitly notes candidate as a direct Latin loan into the modern languages.\",\n \"derivation_fa\":\"واژهٔ فرانسوی candidat (نخستین گواهی ۱۴۶۷م در معنی رومی، و از سدهٔ ۱۶م در معنی سیاسی امروزی) وام‌گیری کتابی و مستقیم از candidātus لاتینی است، نه بازماندهٔ عامیانه؛ حفظ خوشهٔ -did- و پایانهٔ -at (به‌جای صورتی چون *chandié که تحول آوایی منظم فرانسهٔ کهن ایجاب می‌کرد) نشان می‌دهد که واژه‌ای «لاتینی‌مآب» از دورهٔ اومانیسم است. کلاین (ص ۲۳۱) نیز candidate را وام مستقیم لاتینی در زبان‌های نو می‌داند.\",\n \"sources\":[H],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference in the book.\"}],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231\",\"stance\":\"supports\",\"note\":\"'candidate, n. ... — L. candidatus'; Klein marks no intermediate popular form.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kand-\",\"stance\":\"supports\",\"note\":\"CANDIDATE listed among the Latin candere derivatives.\"}]\n})\n\nnodes.append({\n \"id\":16,\"lang\":\"Persian\",\"words\":\"kândîd «کاندید ، کائندیدا» : candidate\",\n \"verdict\":\"transcription_suspect\",\n \"derivation\":\"The word itself is right: Persian کاندیدا / کاندید 'candidate' is a 20th-century French loan taken during and after the Constitutional period, from French candidat(e) — the -ā of کاندیدا reflects the French feminine/Latinate candidata rather than the masculine candidat, and the shorter کاندید is the back-formed everyday form; Mo'in's volume of foreign compounds is exactly where such words are entered. The JSON, however, misreads the second form: at 600 dpi the printed page clearly shows «کاندید ، کاندیدا», with no hamza; the extracted string «کائندیدا» has a spurious ئ. This is an extraction error, not the book's.\",\n \"derivation_fa\":\"خودِ واژه درست است: «کاندیدا / کاندید» وام‌واژه‌ای فرانسوی از سدهٔ بیستم است که در دورهٔ مشروطه و پس از آن وارد فارسی شده، از candidat(e) فرانسوی؛ الف پایانی «کاندیدا» بازتاب صورت مؤنث/لاتینی‌وار candidata است و «کاندید» صورت کوتاه‌شدهٔ گفتاری. مجلد واژه‌های بیگانهٔ فرهنگ معین جای طبیعی چنین مدخلی است. اما در فایل استخراج‌شده صورت دوم نادرست خوانده شده: در بازنمایی ۶۰۰ نقطه‌ای صفحهٔ چاپی به‌روشنی «کاندید ، کاندیدا» آمده و همزه‌ای در کار نیست، حال آنکه در JSON «کائندیدا» ثبت شده است. این خطای خوانش اسکن است، نه خطای کتاب.\",\n \"sources\":[H],\n \"ref_check\":[{\"ref\":\"MON:2874\",\"status\":\"not_checked\",\"note\":\"grep for کاندید/کاندیدا in MON_part1.txt, MON_part2.txt and the two Adena djvu texts returns nothing; the page falls in Mo'in's vol. 4 (foreign compounds), which is not in the local OCR. The ک-region numbering (کندر at MON_part2 line 27042) is consistent with p.2874.\"}],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"MON_part1/part2, grep کاندید\",\"stance\":\"silent\",\"note\":\"not in the local OCR (vol. 4 missing).\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep کاندید\",\"stance\":\"silent\",\"note\":\"Aryanpur's IE-roots dictionary does not carry modern French loans.\"},\n  {\"src\":\"BQT\",\"where\":\"Borhan-e Qate'\",\"stance\":\"silent\",\"note\":\"a 17th-century dictionary; a 20th-century Europeanism cannot be in it.\"}],\n \"error_in\":\"extraction\",\"book_prints\":\"کاندید ، کاندیدا\",\"correct_form\":\"کاندید ، کاندیدا\"\n})\n\nnodes.append({\n \"id\":17,\"lang\":\"English\",\"words\":\"candid, candidate, candle, chandelier, incandescent\",\n \"verdict\":\"plausible\",\n \"derivation\":\"All five are ultimately from Latin candēre, but only two of them hang from the box's own words. candid (1620s) < L candidus 'white, pure', and candidate (1610s) < L candidātus — these do descend from node #14. candle, however, is Old English candel, borrowed from Latin candēla (a sister formation, candē-lā, directly on candēre, not on candidus) already in the Anglo-Saxon church vocabulary; chandelier < Old French chandelier < Medieval Latin candēlārius, again from candēla; and incandescent < L incandēscere, the inchoative of candēre. Watkins (AHD s.v. kand-) puts all of them under candēre, not under candidus, so the arrow is right about the root but wrong about the immediate parent for three of the five words.\",\n \"derivation_fa\":\"هر پنج واژه سرانجام از candēre لاتینی‌اند، اما تنها دو تای آن‌ها از واژه‌های همین خانه می‌آیند. candid (۱۶۲۰م) از candidus و candidate (۱۶۱۰م) از candidātus — این دو براستی از گرهٔ ۱۴ گرفته شده‌اند. اما candle همان candel انگلیسی کهن است که در واژگان کلیسایی دورهٔ آنگلوساکسون از candēla لاتینی (ساختی خواهر، مستقیماً از candēre نه از candidus) وام گرفته شده؛ chandelier از فرانسهٔ کهن chandelier و آن از candēlārius لاتینی میانه، باز هم از candēla؛ و incandescent از incandēscere، فعل آغازیِ candēre. واتکینز در پیوست AHD همهٔ این‌ها را زیر candēre می‌آورد نه زیر candidus. پس پیکان در بارهٔ ریشه درست است ولی برای سه واژه از پنج واژه، خانهٔ مادرِ بی‌واسطه را نادرست نشان می‌دهد.\",\n \"sources\":[H],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference in the book.\"}],\n \"consulted\":[\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kand-\",\"stance\":\"partial\",\"note\":\"'*kand-e- in Latin candere, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE' — all under candere, none under candidus; CHANDELIER is not even listed there.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231\",\"stance\":\"partial\",\"note\":\"'candle, n. — ME. candel, fr. OE. candel, fr. L. candela ... fr. candere' and 'candelabrum ... fr. candela. See candle and cp. chandelier'.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt, cross-references at lines 2792, 3225, 9134\",\"stance\":\"supports\",\"note\":\"Skeat groups 'Cannel-coal; see Candid', 'Censer; see Candid', 'Incandescent; see Candid' — the same family, headed at Candid.\"}]\n})\n\nnodes.append({\n \"id\":18,\"lang\":\"Greek\",\"words\":\"kandhĕla : light, lamp, candle\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Greek κανδήλα / κανδήλη 'lamp, candle' is real but it is NOT an inherited Greek reflex of the root: it is a Koine/Byzantine borrowing of Latin candēla, which spread with Roman church lighting from about the 2nd-4th c. CE (whence also Byzantine κανδηλάπτης 'lamp-lighter'). Wiktionary's chain for the Arabic word runs 'Classical Syriac qandēlā, borrowed from Ancient Greek kandḗlē, which itself derives from Latin candēla, rooted in PIE *(s)kend-'; Lokotsch no. 1053 says the same ('aus lat. candela, gr. kandele'). So the arrow root>Greek should be root>Latin>Greek. The spelling 'kandhĕla' with an -h- is also not a form the sources know (Greek has no aspirate here); the printed page does read kandhĕla, so it is the book's own transliteration slip, not the extraction's.\",\n \"derivation_fa\":\"κανδήλα / κανδήλη یونانی «چراغ، شمع» واژه‌ای واقعی است اما بازماندهٔ ارثی این ریشه در یونانی نیست: وام‌واژه‌ای است از candēla لاتینی که در یونانی کوینه و بیزانسی همراه با چراغ‌افروزی کلیسای رومی از سدهٔ دوم تا چهارم میلادی رواج یافت (از همین‌جا κανδηλάπτης «چراغ‌افروز»). ویکی‌واژه زنجیرهٔ واژهٔ عربی را چنین می‌آورد: «سریانی qandēlā، وام‌گرفته از یونانی kandḗlē، و آن از candēla لاتینی، از ریشهٔ هندواروپایی *(s)kend-»؛ لوکوچ (شمارهٔ ۱۰۵۳) نیز همین را می‌گوید. پس پیکان باید «ریشه ← لاتینی ← یونانی» باشد نه «ریشه ← یونانی». املای kandhĕla با «ه» هم صورتی نیست که مأخذی بشناسد (یونانی در اینجا واک دمیده ندارد)؛ صفحهٔ چاپی نیز همین را دارد، پس خطای آوانگاری خود کتاب است نه خطای خوانش اسکن.\",\n \"sources\":[E,H],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt s.v. kand- lists 'CANDLE' under Latin candere/candela and gives no Greek reflex at all; the reference does not support an independent Greek branch.\"}],\n \"consulted\":[\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1053 (LKT.txt line 2505)\",\"stance\":\"contradicts\",\"note\":\"'Ar. kandil: Leuchte, Laterne [aus lat. candela, gr. kandele ZDMG LI, 316]' — Latin is named first as the source.\"},\n  {\"src\":\"POK\",\"where\":\"POK_full.txt kand- p.526\",\"stance\":\"partial\",\"note\":\"Pokorny's Greek material under kand- is only 'gr. kandaros: anthrax (Hes.)'; no kandela.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231 s.v. candle\",\"stance\":\"contradicts\",\"note\":\"'fr. L. candela' with no Greek intermediary; Klein's Greek cognate of the root is kandaros 'glowing coal'.\"}],\n \"error_in\":\"book\",\"book_prints\":\"kandhĕla\",\"correct_form\":\"kandēla (Gk. κανδήλα / κανδήλη, itself < Lat. candēla)\"\n})\n\nnodes.append({\n \"id\":19,\"lang\":\"Arabic\",\"words\":\"qandîl : light, lamp\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Arabic قنديل qindīl/qandīl 'lamp, hanging church-lamp' is indeed the Greek word, but the accepted route inserts Syriac: Latin candēla > Greek κανδήλη > Classical Syriac ܩܢܕܝܠܐ qandēlā > Arabic qindīl (Wiktionary), the Syriac stage explaining both the q- (Aramaic regularly renders foreign k- before back vowels with q) and the Arabic pattern qiCCīC. Nourai's own reference in fact names Latin, not Greek: al-Unaysi, printed p.59, has 'قنديل - لاتيني' glossed 'معناه شمعة يستضاء بها، مرادفه مصباح وسراج'. Borhan-e Qate' p.1545 has the Persian entry but gives no etymology. So the node is right in substance (Graeco-Latin loan) but the single Greek>Arabic arrow skips both the Latin origin and the Syriac transmitter.\",\n \"derivation_fa\":\"«قندیل» عربی به معنی چراغ و چراغِ آویختهٔ کلیسا براستی همان واژهٔ یونانی است، اما مسیر پذیرفته‌شده یک حلقهٔ سریانی هم دارد: candēla لاتینی ← κανδήλη یونانی ← qandēlā سریانی ← qindīl عربی (ویکی‌واژه). مرحلهٔ سریانی هم «ق» آغازین را توضیح می‌دهد (آرامی «ک» بیگانه را پیش از واکه‌های پسین به قاف بدل می‌کند) و هم وزن قِنْدیل را. جالب آنکه خودِ مأخذ نورایی لاتینی را نام می‌برد نه یونانی را: العنیسی (ص ۵۹) می‌نویسد «قندیل ـ لاتینی» با معنی «شمعة یستضاء بها، مرادفه مصباح وسراج». برهان قاطع (ص ۱۵۴۵) نیز مدخل فارسی را دارد ولی ریشه‌شناسی نمی‌دهد. پس جانِ ادعا درست است ولی پیکانِ یک‌مرحله‌ای «یونانی ← عربی» هم خاستگاه لاتینی و هم واسطهٔ سریانی را نادیده می‌گیرد.\",\n \"sources\":[E],\n \"ref_check\":[\n  {\"ref\":\"TAD:59\",\"status\":\"partial\",\"note\":\"TAD_pages.txt leaf 62 (printed ≈59): 'قنديل - لاتيني ... معناه شمعة يستضاء بها مرادفه مصباح وسراج' — al-Unaysi marks the word LATIN, not Greek.\"},\n  {\"ref\":\"BQT:1545\",\"status\":\"partial\",\"note\":\"BQT_v3_pages.txt pdf page 338 (= printed 1545, calibrated against pdf page 498 = printed ۱۷۰۵): the قندیل entry, 'گویند که پیوسته [در] معبد ترسایان آویخته باشد', plus قندیل چرخ / قندیل دوسر etc. — the word is there, with no etymological footnote.\"}],\n \"consulted\":[\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1053\",\"stance\":\"supports\",\"note\":\"'Ar. kandil: Leuchte, Laterne [aus lat. candela, gr. kandele]; hieraus sp. candil, mit ar. Art. alcandora Signalfeuer'.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231\",\"stance\":\"silent\",\"note\":\"Klein treats candela only on its way into English; no Arabic offshoot.\"},\n  {\"src\":\"AFM\",\"where\":\"AFM_pages.txt, grep قنديل\",\"stance\":\"silent\",\"note\":\"Addi Shir does not list قنديل among Persian words Arabised — consistent with a Graeco-Syriac, not Persian, origin.\"}]\n})\n\nnodes.append({\n \"id\":20,\"lang\":\"Persian\",\"words\":\"qandîl «قندیل» : lamp\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Persian قندیل qandīl 'lamp, chandelier, hanging lamp' is taken from Arabic with no change; Mo'in marks it [معر.] (mu'arrab, i.e. an Arabicised foreign word passed on to Persian) and defines it 'چراغ، چراغدان، شمعدان (مخصوصاً که از سقف آویزان باشد)؛ قنادیل' — even the broken plural قنادیل is carried over. Nourai's Manuchehri line ('چو از زلف شب باز شد تابها / فرو مرد قندیل محرابها') dates the word in Persian poetry to the first half of the 11th c., which fits an early Islamic-period borrowing of a church/mosque lamp term.\",\n \"derivation_fa\":\"«قندیل» فارسی به معنی چراغ و چراغدان آویخته، بی هیچ دگرگونی از عربی گرفته شده است؛ معین آن را با نشان [معر.] (معرَّب، یعنی واژهٔ بیگانه‌ای که از راه عربی به فارسی رسیده) آورده و چنین تعریف می‌کند: «چراغ، چراغدان، شمعدان (مخصوصاً که از سقف آویزان باشد)؛ قنادیل» — حتی جمع مکسر «قنادیل» نیز به فارسی راه یافته است. بیت منوچهری که نورایی آورده («چو از زلف شب باز شد تابها / فرو مُرد قندیل محرابها») کاربرد واژه را در شعر فارسی به نیمهٔ نخست سدهٔ پنجم هجری می‌رساند، که با وام‌گیری زودهنگام یک اصطلاح چراغِ عبادتگاه در دورهٔ اسلامی می‌خواند.\",\n \"sources\":[E],\n \"ref_check\":[\n  {\"ref\":\"MON:2734\",\"status\":\"supports\",\"note\":\"MON_part2.txt line 15141: 'قندیل: [معر.] (ا.) چراغ. چراغدان، شمعدان (مخصوصاً که از سقف آویزان باشد)؛ قنادیل. قندیل ترسا: قندیلی که پیوسته در کلیسا آویخته باشند. قندیل چرخ: (کن.) آفتاب و ماه. قندیل دوسر: (کن.) آسمان. قندیل شب: سیاهی شب.' — the [معر.] tag is exactly Nourai's Arabic-mediated claim, and the sub-entries match the ones Borhan lists.\"},\n  {\"ref\":\"ARK:235\",\"status\":\"not_checked\",\"note\":\"Rokn-zadeh Adamiyyat, Arkan-e Sokhan: refs_online.json records 'Not found ... nothing digitised on any permitted platform'.\"}],\n \"consulted\":[\n  {\"src\":\"BQT\",\"where\":\"BQT_v3_pages.txt pdf page 338 = printed 1545\",\"stance\":\"supports\",\"note\":\"the قندیل entry and the same idioms (قندیل چرخ، قندیل دوسر، قندیل شب) that Mo'in repeats.\"},\n  {\"src\":\"MON\",\"where\":\"MON_part2.txt line 15141\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1053\",\"stance\":\"supports\",\"note\":\"traces the same Arabic word onward into Spanish candil, confirming its currency as an Arabic loan-noun.\"}]\n})\n\nentry={\n \"entry\":0,\n \"root\":\"Kand 1, Qand\",\n \"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *(s)kend- / *kand- 'to shine, glow; bright, white'\",\n \"note\":\"The root box is right. Pokorny's headword on the cited page 526 is 'kand-, skand- and (Old Indic) (s)kend-, Meaning: to glow; bright, *moon', with Skt candra-/candana-, Alb. hene, Lat. candeo/candidus/candela, W cann; Watkins (AHD) has 'kand-. To shine ... [Pok. kand- 526]'; Wiktionary reconstructs *(s)kend- 'to shine, appear' citing Pokorny 526, LIV 554 and de Vaan 106-107. The language label 'Indo-European' and the gloss 'to shine, to be white' are both accurate. The second headword 'Qand' is not a separate root: it is Nourai's way of covering the q- spellings of the Arabic-mediated branch (qandil), where q renders a foreign k. The weakness of the chart is not the root but the left branch: Nourai has merged two unrelated tree products, frankincense (Skt kunduru- > MP kundur > NP kondor) and sandalwood (Skt candana- > MP candal > NP candal/sandal, Arab. sandal), and has attached the shoe word (Gk sandalion, Pre-Greek per Beekes) to the sandalwood chain. The Greek kandela branch (node 18) is also mis-drawn: Greek borrowed it from Latin. The Latin branch (nodes 14-17) is impeccable.\",\n \"note_fa\":\"خانهٔ ریشه درست است. سرمدخل پوکورنی در همان صفحهٔ ۵۲۶ که نورایی یاد کرده چنین است: «kand-, skand- و (در هندی باستان) (s)kend-، به معنی درخشیدن؛ روشن، ماه»، با نمونه‌های candra-/candana- سنسکریت، hënë آلبانیایی، candeō/candidus/candēla لاتینی و cann ولزی؛ واتکینز نیز در پیوست AHD «kand-. To shine ... [Pok. kand- 526]» دارد و ویکی‌واژه ریشه را *(s)kend- «درخشیدن، پدیدار شدن» بازسازی می‌کند و به پوکورنی ۵۲۶، LIV ۵۵۴ و دِ وان ۱۰۶-۱۰۷ ارجاع می‌دهد. برچسب زبانی «هندواروپایی» و معنی «درخشیدن، سفید بودن» هر دو درست‌اند. سرواژهٔ دوم «Qand» ریشهٔ جداگانه‌ای نیست، بلکه شیوهٔ نورایی برای پوشش‌دادن صورت‌های قاف‌دار شاخهٔ عربی‌میانجی (قندیل) است. ضعف نمودار در ریشه نیست، در شاخهٔ چپ است: نورایی دو فرآوردهٔ درختیِ بی‌ربط، یعنی کندر (kunduru سنسکریت ← kundur پهلوی ← کُندر فارسی) و چوب صندل (candana سنسکریت ← čandal پهلوی ← چندل/صندل)، را یکی گرفته و افزون بر آن واژهٔ «کفش» (σανδάλιον یونانی که به گفتهٔ بیکس پیش‌یونانی است) را نیز به همین زنجیره چسبانده است. شاخهٔ κανδήλα یونانی (گرهٔ ۱۸) هم نادرست رسم شده، زیرا یونانی آن را از لاتینی وام گرفته است. شاخهٔ لاتینی (گره‌های ۱۴ تا ۱۷) بی‌عیب است.\",\n \"sources\":[H,C,A,B,D,E,F,G,I,J],\n \"ref_check\":[{\"ref\":\"POK:526\",\"status\":\"supports\",\"note\":\"POK_full.txt lines 43488-43520: 'Root/lemma: kand-, skand- and (Old Indic) (s)kend- / Meaning: to glow; bright, *moon ... Old Indic candati shines ... candra- luminous, gleaming, burning; m. moon, candana- m.n. sandalwood (incense); gr. kandaros: anthrax Hes.; alb. Geg hane, Tosk hene moon; Latin candeo, -ere gleam ... References: WP. I 352, WH. I 151 f. Page(s): 526'.\"}],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny Bd. I 352 (WLD_Bd1_pages.txt line 33112ff)\",\"stance\":\"supports\",\"note\":\"'alb. geg. hane, tosk. hene Mond (*sqandna) ...; lat. candeo, -ere glaenzen, schimmern, hell gluehen ... candela, candelabrum Leuchter ...; cymr. cann weiss, hell, mbret. cann Vollmond' — the same root, the same material, and the page Pokorny cites.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kand-\",\"stance\":\"supports\",\"note\":\"'kand-. To shine. ... [Pok. kand- 526.]' — same root, same gloss, same Pokorny page.\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC.txt\",\"stance\":\"silent\",\"note\":\"no separate kand- article surfaced by grep.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt p.231 s.v. candid\",\"stance\":\"supports\",\"note\":\"'All these words derive fr. I.-E. base *(s)qand-, *(s)qend-, to shine, glow.'\"}],\n \"nodes\":nodes}\n\nout={\"pdf_page\":239,\"book_page\":209,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\"entries\":[entry]}\nopen(\"data/verification/page-239.json\",\"w\",encoding=\"utf-8\").write(json.dumps(out,ensure_ascii=False,indent=2)+\"\\n\")\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-239.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 239",
 "description": "Write and validate page-239.json"
}
```


### [2026-09-06T16:02:11.192Z] TOOL RESULT

```
written 20 nodes
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 5, 'plausible': 6, 'confirmed': 7, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'supports': 9, 'not_found': 1, 'contradicts': 2, 'not_checked': 11}
books consulted: {'partial': 12, 'contradicts': 6, 'silent': 19, 'supports': 22} | by book: {'KLN': 13, 'LKT': 6, 'AHD': 4, 'BQT': 4, 'MON': 4, 'SKT': 3, 'POK': 3, 'FSD': 3, 'PLA': 2, 'DEV': 2, 'WEB': 2, 'AFM': 2, 'ARY': 2, 'LEW': 2, 'SIN': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'HJB': 1, 'WLD': 1}
```


## [2026-09-06T16:02:34.131Z] AGENT

Done. `python3 tools/verify_check.py 239` reports **0 PROBLEM lines** (20/20 nodes).

**Page 239 (book p. 209) — root `Kand 1, Qand` (PIE *(s)kend- "to shine")**

Verdicts: root **confirmed**; nodes — confirmed 7, plausible 6, disputed 5, transcription_suspect 2.
Ref checks: supports 9, partial 6, contradicts 2, not_found 1, not_checked 11. 21 different books consulted.

Disputed / flagged:
- **#1 Sanskrit `kandana, kundruka` "sandalwood"** — Nourai fuses two unrelated words: candana- (sandalwood, probably a Dravidian loan) and kunduru/kunduruka- (frankincense, Boswellia, not an IE word). Pokorny 526 has candana- but no kunduru.
- **#3 Persian `kondor / sandal / sandalî`** — only کندر descends from the parent; سندل/صندلی belong to the candana → MP čandal → Ar. ṣandal line, not to kundurūk. (BQT 664, 1174, 1705 and Mo'in all keep them apart.)
- **#4 Greek `santalon; santalion`** — σανδάλιον "shoe" is a different lemma (Pre-Greek per Beekes; Klein p.1380 "shoe of the Lydian god Sandal"); also σάνταλον came via Arabic, not Persian (Hobson-Jobson 789, Devic, Lokotsch 1825). Book prints "santalion" — Nourai's misprint for *sandalion*.
- **#9 Greek `sandarak, sandaraxē`** — Beekes/Wiktionary: Oriental loan of unknown source (possibly Akkadian), not from Skt candra-rāga-; Klein only "Cp."
- **#18 Greek `kandhĕla`** — Gk κανδήλη is itself borrowed from Latin candēla (Wiktionary, Lokotsch 1053), so the root→Greek arrow is wrong; spelling with -h- is the book's slip.
- **#12 Latin `sandraca`** (transcription_suspect, error_in = **book**) — correct form *sandaraca*; verified on the 600-dpi page render, extraction is faithful.

**Extraction error the owner must fix (JSON ≠ printed page):**
- node **#16**, Persian script: JSON has `کاندید ، کائندیدا`; the page prints `کاندید ، کاندیدا` (spurious ئ in the second form).

Also worth noting: node #11's bracketed variant «سَندَره» looks like a column-neighbour of Mo'in's سندروس (Mo'in glosses سندره "حرامزاده", unrelated); and node #2's Pahlavi gloss "sandalwood" contradicts both Laufer SIN:585 and MacKenzie ("kundur … frankincense").

Page PNG saved to `data/verification/sources/refs/ocr/BOOK/239.png`; 10 web pages archived via `tools/fetch_source.py`. Output at `/home/sfmqrb/git/rishe/data/verification/page-239.json`.
