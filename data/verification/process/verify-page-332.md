# Verification process log — verify-page-332


## [2026-09-07T16:11:40.791Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 332 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-332.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-332.json. Write /home/sfmqrb/git/rishe/data/verification/page-332.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 332` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:11:42.596Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T16:11:43.171Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:11:43.186Z] TOOL RESULT

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


## [2026-09-07T16:11:44.139Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-332.txt"
}
```


### [2026-09-07T16:11:44.163Z] TOOL RESULT

```
1	=== PDF page 332 (book page 302) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Men 1 : to think  (refs POK:726)  PART 2
4	#1 (parent #0) [Greek] refs=KLN:947; AHD:864 | mousa : protector of arts ; matos : mind, will ; autos-matos : has mind of itself ☞Autos
5	  #2 (parent #1) [Latin] refs=None | 
6	    #3 (parent #2) [French] refs=None | musique
7	      #4 (parent #3) [Persian] refs=MON:4063, 4433 |  | extra: موزیک ، مزقان ، مزغان
8	      #5 (parent #3) [Persian] refs=BQT:2052; MON:4432 |  | extra: موزه ۱ ، موزائیک ، اتوماتیک
9	    #6 (parent #2) [English] refs=AHD | music, museum, mosaic, amnesty, maniac, automatic
10	#7 (parent #0) [Latin] refs=AHD | ment, měns : mind
11	  #8 (parent #7) [English] refs=AHD | mental, mention, monitor, monster ; monument, comment, demonstrate
12	--- entry 1 ---
13	ROOT [Indo-European] Manu, Manus : one who thinks, man  (refs KLN:930; POK:700)
14	#1 (parent #0) [Avestan] refs=POK:700; KLN:930; BQT:2047; SNS:241 | manu, manuš, mainyuš : man(ly) ; manuš-čitra : with manly face, or of "Manush" race ☞Skai
15	  #2 (parent #1) [Persian] refs=BQT:2047 | Manŭčehr «منوچهر» : from Manush family | NOTE: a male name
16	#3 (parent #0) [Germanic] refs=AHD | manna : man
17	  #4 (parent #3) [French] refs=None | mannequin : manikin
18	    #5 (parent #4) [Persian] refs=MON:3721 | mânkan «مانکن» : manikin
19	  #6 (parent #3) [English] refs=KLN:930 | man, Norman, Herman, manikin
20	--- entry 2 ---
21	ROOT [Indo-European] Men-dh : to learn  (refs POK:730)
22	#1 (parent #0) [Avestan] refs=AHD; KLN:1095 | ma[n]dz-dha, mazdha : learned, wise ☞Dhě 2 ; ahura-mazdha : wise spirit ☞An 1 ; mazda-yasna : God worshipper ☞Yag
23	  #2 (parent #1) [Persian] refs=BQT:109 | Mazdâ «مزدا» : wise ; Ahŭrâmazdâ «اهورامزدا ( هرمز )» : wise spirit ; mazdîsnâ «مزدیسنا» : God worshipper
24	#3 (parent #0) [Greek] refs=AHD | manthanein : to learn
25	  #4 (parent #3) [English] refs=None | mathematics
26	
```


## [2026-09-07T16:11:48.301Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-332.json",
 "description": "Read source JSON page 332"
}
```


### [2026-09-07T16:11:48.342Z] TOOL RESULT

```
{
  "pdf_page": 332,
  "book_page": 302,
  "entries": [
    {
      "part": 2,
      "root": {
        "name": "Men 1",
        "lang": "Indo-European",
        "refs": "POK:726",
        "gloss": "to think"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:947; AHD:864",
          "words": [
            {"translit": "mousa", "gloss": "protector of arts", "script": null},
            {"translit": "matos", "gloss": "mind, will", "script": null},
            {"translit": "autos-matos", "gloss": "has mind of itself", "script": null, "see": ["Autos"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "musique", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:4063, 4433",
          "words": [],
          "script_extra": "موزیک ، مزقان ، مزغان",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:2052; MON:4432",
          "words": [],
          "script_extra": "موزه ۱ ، موزائیک ، اتوماتیک",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "music, museum, mosaic, amnesty, maniac, automatic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ment, měns", "gloss": "mind", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "mental, mention, monitor, monster", "gloss": null, "script": null},
            {"translit": "monument, comment, demonstrate", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Manu, Manus",
        "lang": "Indo-European",
        "refs": "KLN:930; POK:700",
        "gloss": "one who thinks, man"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:700; KLN:930; BQT:2047; SNS:241",
          "words": [
            {"translit": "manu, manuš, mainyuš", "gloss": "man(ly)", "script": null},
            {"translit": "manuš-čitra", "gloss": "with manly face, or of \"Manush\" race", "script": null, "see": ["Skai"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2047",
          "words": [
            {"translit": "Manŭčehr", "gloss": "from Manush family", "script": "منوچهر"}
          ],
          "script_extra": null,
          "note": "a male name",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "manna", "gloss": "man", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "mannequin", "gloss": "manikin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3721",
          "words": [
            {"translit": "mânkan", "gloss": "manikin", "script": "مانکن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:930",
          "words": [
            {"translit": "man, Norman, Herman, manikin", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Men-dh",
        "lang": "Indo-European",
        "refs": "POK:730",
        "gloss": "to learn"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AHD; KLN:1095",
          "words": [
            {"translit": "ma[n]dz-dha, mazdha", "gloss": "learned, wise", "script": null, "see": ["Dhě 2"]},
            {"translit": "ahura-mazdha", "gloss": "wise spirit", "script": null, "see": ["An 1"]},
            {"translit": "mazda-yasna", "gloss": "God worshipper", "script": null, "see": ["Yag"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:109",
          "words": [
            {"translit": "Mazdâ", "gloss": "wise", "script": "مزدا"},
            {"translit": "Ahŭrâmazdâ", "gloss": "wise spirit", "script": "اهورامزدا ( هرمز )"},
            {"translit": "mazdîsnâ", "gloss": "God worshipper", "script": "مزدیسنا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "manthanein", "gloss": "to learn", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mathematics", "gloss": null, "script": null}
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


## [2026-09-07T16:11:48.530Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:11:48.572Z] TOOL RESULT

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


## [2026-09-07T16:11:55.582Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T16:11:55.619Z] TOOL RESULT

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


## [2026-09-07T16:11:57.585Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','BQT','MON','SNS','WLD','IEC','SYN','BRT','HRN','HUB','PHD','NYB','ARY','SKT','LKT','LEW','LAT','FSD','WEB']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:700])\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T16:11:58.872Z] TOOL RESULT

```
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
=== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
=== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
=== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
=== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
=== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
=== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
```


## [2026-09-07T16:12:47.930Z] AGENT

Now let me check the references. Starting with Pokorny.


## [2026-09-07T16:12:48.618Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"=== $f leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\"; done",
 "description": "Count leaves in POK files"
}
```


### [2026-09-07T16:12:49.879Z] TOOL RESULT

```
=== POK_01.txt leaves: 363
=== POK_02.txt leaves: 433
=== POK_03.txt leaves: 429
```


## [2026-09-07T16:12:50.528Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mendh-\" POK_full.txt | head -20; echo \"---manu\"; grep -n \"^manu-s\\|manu-s, monu-s\\|monu-s\" POK_full.txt | head -20; echo \"---men-3\"; grep -n \"^men- 3\\|men-3\\|men- 3\\.\" POK_full.txt | head",
 "description": "Grep Pokorny full for roots"
}
```


### [2026-09-07T16:12:50.604Z] TOOL RESULT

```
---manu
---men-3
```


## [2026-09-07T16:12:53.924Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK_full.txt; head -c 600 POK_full.txt; echo; echo \"=== grep mendh\"; grep -c \"mendh\" POK_full.txt",
 "description": "Inspect POK_full.txt"
}
```


### [2026-09-07T16:12:53.986Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 



=== grep mendh
0
```


## [2026-09-07T16:12:57.296Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"mendh\\|men-dh\" POK_full.txt | head -20; echo \"=== POK_02 mendh\"; grep -n -i \"mendh\" POK_02.txt | head -20",
 "description": "Grep POK for mendh case-insensitively"
}
```


### [2026-09-07T16:12:57.359Z] TOOL RESULT

```
=== POK_02 mendh
5825:(.uaw  mit  Red.-Stufe  der  Wz.  wie  SaL-ddXXo)  usw.),  Infin.  iiwod-ai  ,strebeii^, partiz.  ^(bfisvog;  (AaJraL  (Epich.)  *  Kt^tsl,  'i;sxvü'C,ei:ai  Hes.  (und  andere  Glossen), aus  dem  o-stufigen  Perf.  erwachsen;  Movaa  ,Muse^  hierher  oder  zu  mendh-?
6210:mendh-  , seinen  Sinn  worauf  richten,  lebhaft  sein';    m(o)ndh-ro-  _,munter'
```


## [2026-09-07T16:13:03.395Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nfor target in (5825,6210):\n    off=sum(len(l)+1 for l in lines[:target-1])\n    leaf=d[:off].count('\\f')\n    print('line',target,'-> leaf',leaf,'printed p.',leaf+344)\nEOF",
 "description": "Map POK_02 lines to leaves"
}
```


### [2026-09-07T16:13:04.780Z] TOOL RESULT

```
line 5825 -> leaf 365 printed p. 709
line 6210 -> leaf 391 printed p. 735
```


## [2026-09-07T16:13:10.023Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==392' POK_02.txt | head -60",
 "description": "Print POK_02 leaf 391 (0-based)"
}
```


### [2026-09-07T16:13:11.301Z] TOOL RESULT

```
bret.  menn  ,junges  Tier',  menn gavr  , Zicklein' ;  gall.  ON  Epo-manduo-durum,  brit.  ON  Mandu-essedum (illyr.  Lw.?);  wohl  auch  der  bair.  FIN  Mindel;  ahd.  manzon  m.  PL  , Zitze, Euter';  illyr.  gall.  mand-  könnten  auch  idg.  Ablaut  mnd-  enthalten.
WP.  II  232,  WH.  II  29  f.,  Marstrander  ZceltPh.  7,  384 f.,  Krähe,  Würz- burg. Jb.  1,  189,  202.
mend(ä,  -om)  , Fehler,  Körperfehler,  Gebrechen'  (auch  ,Makel,  Fleck'?). Ai.  mindä  , Körperfehler'  {im- *mandä  nach  nindä  »Tadel'); lat.  mendum,  menda  »Fehler,  Gebrechen'»  e-mendäre  »ausbessern;  heilen', wovon  mendlcus  »Bettler'  und  mendäx,  -äcis  ,lügnerisch'  (* fehlerhaft);
730
vielleicht  air.  mennar  ,n3acula*,  schwundstufig  air.  mind  , Zeichen,  Merk mal*  (*mndu  n.;  auch  in  der  Bed.  ,diadema'  =  .insigne'  dass.  Wort),  cymr mann  , Platz,  Stelle',  mann  geni  , Muttermal'.
WP.  II  270,  WH.  II  69,  J.  Loth  RC.  44,  362  f.
mendh-  , seinen  Sinn  worauf  richten,  lebhaft  sein';    m(o)ndh-ro-  _,munter'
Ai.  medhä  , Weisheit,  Einsicht,  Verstand',  av.  mazdä,  mazdäh-  n.  Ge- dächtnis, Erinnerung',  mazdäh-  m.  Name  des  höchsten  Gottes  (*mazdha aus    ^mndh-ta) ;
gr.  fiavd-dvw  (sekundäres  Präs.  zu)  fj,adrjGOf,taL,  ^a&etv  , lernen',  dor.-äol. ixadtj,  ion.  iia&og  n.,  ion.-att.  (.iddr/aig  , Lernen,  Unterricht';  (^ev-d^rjQT]  , Stirn- (pQOVTLq' ;  vielleicht  Movoa  {*^iov-d-ia)  ,Muse' ;
alb.  mund  ,kann,  siege' ;
cjmr.  mynnu  , wollen',  com.  mennaf  ,ich  will',  mynnes,  mynnas  ,wollen Wille',  cymr.  go-fin(n)  ^verlangen,  bitten,  fragen',  corn.  govyn  ds. ;
got.  mundön  , sehen  auf,  mundrei  ,Ziel',  aisl.  munda  ,zielen,  streben*, ahd.  muntar  , eifrig,  munter^,  muntari  , Eifer';  ahd.  mendl  ,Freude',  menden, as.  mendian  ,sich  freuen';
lit.  mafidras,  mandrüs  , munter,  übermütig' ;  lett.  muodrs  und  muö^s  ds. (*mandus),  mudsties  , aufwachen';  abg.  mgdr^  , weise'.
Idg.  men-dh-  durch  Zusammenrückung  aus  *men-dhe-  ,den  Sinn  worauf setzen',  vgl.  ai.  man[*z]-dhätdr-  ,der  Sinnende,  Andächtige',  av.  mqz-dä- ,dem  Gedächtnis  einprägen'  (davon  mqzdra-  , verständig,  weise').  —  Von gr.  TiQO-fxrj-difjg  ^vorsorglich'  (dor.  -ä-)  auf  ein  idg.  *mä-dh-  neben  ^men-dh- (wie  g'^ä- :  g^em-)  zu  schließen,  scheint  möglich.
WP.  II  270  f.,  Trautmann  168  f.
xnen{e)gh-,  nion{e)gh-,  mngh-  , reichlich,  viel;  reichlich  geben*.
Ai.  maghd-  n.  ,Gabe,  Geschenk',  maghdvan{t)-  , gabenreich,  freigebig'; m.  , Spender',  mamhate  , schenkt,  spendet',  mamhistha-  ,im  höchsten  Maße freigebig,  überaus  reichlich',  mamhdnä  ,g
```


## [2026-09-07T16:13:21.442Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 357 365 383; do echo \"########## NR==$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | head -50; done",
 "description": "Print POK_02 leaves 356,364,382"
}
```


### [2026-09-07T16:13:22.784Z] TOOL RESULT

```
########## NR==357

ahd.  mast  ,Futter,  Mästung,  Eichelmast',  nhd.  Mast,  Mästung,  ags.  mcBst
,Buchecker';  got.  mats  ,Speise',  aisl.  matr  m.,  ags.  mete  m.,  ahd.  maz  n.
ds.  (nhd.  noch   in  Messer  aus   ahd.  mezzi-rahs),  sowie   got.  matjan  , essen,
fressen',  aisl.  metja  , schlürfen',  ags.  mettan  , füttern',  mnd.  mat(e)   ,Kame-
rad,  bes.   in   der   Seemannssprache'  (Maat),  ahd.  gamazzo  ,Kamerad',  eig.
;.!   ,*Essensgenosse';    dazu   auch   mnd.    met   ,Schweinefleisch',   nnd.  mett  ,ge-
•     hacktes  Fleisch'  als  ,*saftiges,  breiiges  Fleisch',  ahd.  (eig.  ndd.)  Mettivurst
:     (aus  andd.  *matja-)-  ablautend  ags.  as.  mos  , Brei,  Speise',  ahd..  wwo5  ,ge-
kochte,  bes.  breiige  Speise,  Essen  überhaupt',  nhd.  Mus,  Gemüse  (*mädso-).
WP.  II  231  f.,  WH.  II  6f. ;    Kuiper  Nasalpräs.  140.
magh- :  znägh-  ,können,  vermögen,  helfen';  magh-ti-  , Macht'.
Ai.  maghd-  , Macht,  Kraft,  Reichtum,  Gabe',  maghdvan-,  maghdvat- ,kräftig',  iran.  magu-,  apers.  magus  , Magier,  Zauberer'  (daraus  gr.  (.layog, lat.  magus);
arm.  marthankh  ,Hilfsmittel'  (*mag-thra-)]
gr.  (.ifjxog  n.  (dor.  iiä^og),  poet.  (.ifjxaQ  , Hilfsmittel',  (.irjxavrj^  dor.  iiG^avä (>  lat.  machina)  ,Hilf smittel,  Werkzeug,  List' ;
got.  ags.  magan,  aisl.  mega,  maga,  muga,  afries.  muga,  mnd.  mögen,  ahd. magan^  mugan  ,mögen','  1.  Sg.  Präs.  got.  as.  ahd.  mag,  aisl.  mä,  ags.  mseg, afries.  mei;  aisl.  magn,  meg{i)n  n.  , Macht,  Hauptsache',  ags.  masgen,  ahd., as.  magan,  megin  ds.;  got.  mahts  f.  , Macht,  Kraft',  ahd.  as.  mäht,  ags. meaht,  might,  aisl.  mättr  ds. ;
lit.  mägulas  , zahlreich,  viel*;
aksl.  mogg,  mosti  ,können,  vermögen',  jpo-moHi,  Iterat.  po-magati , helfen' usw.,  aksl.  mosth,  russ.  moch  usw.  ,Macht,  Stärke'  (=  got.  mahts).
WP.  II  227,  Trautmann  164 f.,  H.  Güntert,  Weltkönig  108 f.;  falls E.  Fraenkel  (Lexis  1,  169  f.)  richtig  gr.  ^ifjxog  mit  lit.  moJceti  ,können, verstehen'  auf  eine  Wz.  mäkh-  zurückführt,  könnten  die  anderen  Wörter auch  auf  megh- :  mogh-  zurückgehen ;  vgl.  toch.  A  mokats  ,mächtig'.
696
maghos,  -ä  jung^,  maghu-  ^^Knabe,  JüDgliDg,  unverheiratet^  und  zugehörige  # Fem. -Bildungen,  wie  magho-ti-  j'unge  Weiblichkeit^  #
Av.   mayava-  _,unverheiratet' ;  ?f
alb.  makth  junger    Hase^;
kelt.  *magus  in  gall.  PN  Magu-rlx,  urir.  (Ogam)  Maguno-,  air.  mang,  rriug ^Sklave^;  corn.  maw,  bret.  mao  ^Jüngling,  Diener^,  cymr.  meu-dwy  ^Ej^. Siedler*  (
########## NR==365
iti'  ,Maß,  Gewicht,  Wert' ;
gr.  (.lexQOv  ,Maß'  (nach  Brugmann  Grundr.  IP  1,  342  wie  ai.  d-d-tra-m ,Gabe'  zu  *(iö-) ;  (.irjTig  ,Plan,  List',  ^ui^ricrw  , beschließe',  (j,r]TLdo/j.aL  ,ersinne' ;
alb.  mat,  mas  (*matiö)  ,messe',  mate  ,Maß',  möt  [*meto-)  ,Jahr,  Wetter', matein  , erhebe  die  Hand  zum  Schlage,  werfe'  (,abmessen  =  zielen');
ir.  to-math'  (z.  B.  3.  Sg.  do-mathi)  ^drohen' ;
lat.  metior,  -Iri,  mensus  sum  (Reimbildung  zu  pensus)  , messen,  abmessen', wovon  wohl  mensa  , Tisch,  Eßtisch ;  die  Speisen  selbst'  =  umbr.  mefe ,mensae',  mefa  ,libum'  als  subst.  Fem.  des  Partiz.  Perf.  Pass. ;
mcymr.  medru  ,ein  Ziel  treffen,  können',  zu  medr  .,Geschicklichkeit' ( :  gr.  fxhgov  ?)  ;  gall.  mataris  , Wurfspieß' ;  vielleicht  hierher  acymr.  maut, mbret.  meut  (*mö-tä),  ncymr.  bawd  , Daumen'  (als  Maß?);
ags.  mced  f.  ,Maß';  got.  mela  m., Scheffel';  aisl.  mcklir  m.  ds.,  ags.  male, mele  ,Napf';  aisl.  mcela  ,messen' ;    got.  mel  n.  ,Zeit',   aisl.  mal  ,Maß,  Zeit-
704
punkt,  Mahlzeit^;  ags.  wM  ds.^  ahd.  mal  ,Zeitpunkt^  Mahlzeit',  nhd.  mal
lit.  metas  ,^dJav,  Zeit,  Maß',  apr.  mettan  ,Jahr',  lett.  mfts  , Zeitraum' (vokalisch  wie  gr.  (.istqov  zu  beurteilen) ;  dazu  (^abmessen.  >  *zielen  S. werfen)  lit.  metüj  mesti,  lett.  metu,  mest  ^werfen',  Iterat.  lit.  metyt^  l^u metät  ,hin  und  her  werfen';  apr.  metis  =  iit.  metis  m.  ,Wurf';  mästas  m ,Maß',  mätas  m.  ds.,  matuoti  ^messen',  pämatas  , Grundlage'  usw.;
aksl.  metg,  mesti  ^werfen',  slov.  motdti  , aufwinden',  russ.-ksl.  Iterat v^mätati  , werfen',  slov.  mei  ,Wurf',  usw. ;  aksl.  m^ra  ,Maß',  meriti , messen'* öech.  alt  m^n  ,Maß'  (:  ai.  mäna-),  russ.  mä'tith  ,zielen;  trachten',  usw.«
toch.  A  me-,  B  mai-  ,messen'.
WP.  II  237 f.,  WH.  II  70f.,  81  f.,  Trautmann  179,  183;  verwandt  mit 1.  med-.
4.  me-,  mö-  ,groß,  ansehnlich'.
Positiv  me-ro-s,  mö-ro-s:  gr. -ficogog  in  ^yx^ct-^w^og  ,groß(?)  im  Speer- werfen' u.  dg'l.,  air.  mör  (das  ö  aus  dem  Komparativ),  mär  ,g"roß',  cymr. mawr  ,groß',  bret.  meur  ds.,  gall.  -märos  in  Eigennamen  wie  Nerto-märot (,groß  an  Kraft') ;  mit  e  ahd.  -Tnär  in  Namen  wie  Volk-mär  usw.,  ferner das  Denominativ  germ.  *merjan  ,*als  groß  darstellen,  rühmen',  woraus ,künden':  got.  merjan^  as.  märian,  ahd.  mären,  anord.  mcera  ,verkünden', wozu  nhd.  Mär^  Märchen  u.  dgl.,  sowie  das  postverbale  Adj.  ahd.  as. märi  ,berühmt,  glänzend',  ags.  möere,  anord.  mcerr  ds.,  got.  waila-mereis ,von  gutem  Ruf;
slav.  -merz,  in  Namen  wie  Vladi-mSrbj
mö-lo-  in  cymr.  mawl  ,Lob',  moli  ,loben'  (daraus  air.  molur  ,lobe'), bret.  meuliff  ds. ;
Komparativ  *rae-ies,  -is,  bzw.  (mit  der  Tiefstufe  des  Superlativs)  ms-iesj zn9-is:  ai
########## NR==383
*melsO'  :  (.leXog  ==  lit. tamsid:a,i.  tdmas  n.);  toch.  AB  mälk-  , zusammenfügen'.
WP.  II  292.
6.  mel-,  mela-  in  Farbbezeichnungen,  bes.  von  dunklen,  unreinen,  schmut-
zigen   Farbentönen ;    Schmutz,    beschmutzen' ;    melo-no-   ,schmutzigS Ai.  malind-  , schmutzig,  schwarz',  mlä-na-  , schwarz,  dunkelfarbig',  mala-
m.  n.  , Schmutz,  Unrat,  Sünde';
gr.   ueXäg,    -aiva,    -äv    ,schwarz'    (wohl    für  *[.isXavog    nach    dem    Fem.
(xsXaLva    =   ai.    malini),    ^iXiog    , Rötel',    fxoXvvco    , besudle'    (vielleicht    aus
721
*uaUvix)),  ^vllog  , Rotbarbe'  (Ablaut  wie  lat.  mulleus,  lit.  mulvas),  mit ^Stufe  ixü)Xwip  , Striemen,  blutunterlaufene  Stelle';
alb.  mel-ene  (KoUekt.  *mel-imo-)  ,Ulme'  (von  der  Farbe  des  Holzes), .jjiel-eze  ds.,  mjere  »unglücklich'  (*mel-ro-  ,schwarz'),  usw.  ;
vorrom.   *melix,  -ice  (frz.  meleze)  , Lärche^;
lat.  mulleus  , rötlich,  purpurfarben'  (*mHneios) ;  vgl.  ahd.  mol  S.  717 ;
got.  mela  Nom.  PL  , Schriftzeichen',  meljan  »schreiben',  ahd.  ana-mali ^Fleck,  Narbe',  mhd.  mal  n.  ,Fleck',  ahd.  mälön,  -en  .malen,  zeichnen', anorw.   mmla   , färben,   malen'   (ursprüngl.   ,mit   schwarzer  Farbe   malen');
halt.  *melna-  (*meh-no-)  in  lett.  m^lns  , schwarz',  apr.  meine  , blauer Fleck',  lit.  melsvas  , bläulich'  (auch  lit.  meletä,  -ata  »Grünspecht;  Hasel-, Waldhuhn',  apr.  melato  ,Grünspecht'?);  lit.  m^las,  melynas  ,blau',  melyne , blauer  Fleck  infolge  eines  Schlages',  lett.  me}s  , dunkelblau'  {*melias);  apr. milinan  Akk.  fem.  , Fleck';  lit.  mölis,  lett.  mdls  ,Lehm';
mit  i/-farbiger  Red.-Stufe:  lit.  mulvas  , rötlich,  gelblich',  mulv-yti,  -inti , beschmieren',  mulve  , Schlamm,  Sumpf;
russ.  malina  , Himbeere,  Brombeere'.
WP.  II  293 f.,  WH.  II  122  f.,  Trautmann  177  f.,  188.
7.  mel-  , Wolle,  Wollgewand'?
Gr.  iiallog  (*ml-nö-)  , Zotte,  Flocke';  lit.  rnilas  ,Tuch',  lett.  mil(n)a jgrobes  Tuch',  apr.  milan  ds.  (skr.  mälje.  Gen.  mäljä  PL  f.  , Flaum,  Milch- haar' ist  Lw.  aus  ngr.  jimAAtd  PL).
WP.  II  294.
B.  mel-j  xnelQ-  :  mlö-  »hervorkommen,  erscheinen,  hochkommen;  Erhöhung, Wölbung';  molä  ,Ufer^
Vielleicht  ai.  mani-  ,Perle',  manika-  m.  »(runder)  Wassertopf';  gr.  (xoXetv , gehen,  kommen'  (Aor.),  Präs.  ßlojaxu),  Perf.  (xs^ßXü}v,a]  eßXo)'  i(pdvr]' aüT6-(.ioXoq  , Überläufer',  TtQO-fioXrj  , Auslauf  eines  Berges,  Flusses',  ^oXsvo) »beschneide  die  Pflanzenschößlinge' ;
venet.  FIN  Mal-ont-ina  »Maltein'  (Kärnten),  südillyr.  ON  Malontum, usw.  (Krabe,  Würzburger  Jahrb.  1,  214);
alb.  waZ  ,Berg'  {*mol-no-)',  tosk.  maje  , Spitze,  Gipfel'  (*mol{a)',  alb.  mol jWald'  (, Bergwald)  aus  *melo-'^  geg.  moje  , hochgelegener  Ort'  (*meZ-iä); vorrom.  malga  ,  Alpen  wirtschaff  (*mal-ika)]
air.  Akk.  PL  mailgea  (*mal-ik-),  mir.  Nom,  Sg.  mala  ,Augenwimper' ; mell  , Klumpen,  Hügel'  (*mel-no-)  =  bret.  mell  »großer  Ball';  mir.  mul , Kugel,  Klumpen'  {*molu-),  mul-lach  , Gipf
```


## [2026-09-07T16:13:30.041Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"manu-s\\|monu-s\\|Manu-s\\|mänu\\|3.  men-\\|men-  ,denken\\|Sinn,  denken\" POK_02.txt | head -20",
 "description": "Grep POK_02 for manus and men roots"
}
```


### [2026-09-07T16:13:30.093Z] TOOL RESULT

```
405:ai.  jdniman-  (und  jdnman-)  n.  ,Geburt,  Geschlecht,  Abkunft',  lat.  germen Keim,    Sproß,    Zweig',   germinare  , hervorsprossen',  germänus,  -a  (-m-  aus .trin-)  ,leiblicher  Bruder,  l.  Schwester'  (*gen-men).
1042:lat.  humus  (aus  *homos)  ,Erde,  Erdboden',  wahrscheinlich  Umformung' eines  alten  Kons. -St.  *§hom-]  daher  auch  f.  wie  xdthv]  humilis  , niedrig' ( -vd-af^ccXög)  ]  im  Osk.-Umbr.  * homi-teros,  -temos  als  Kompar.  Superl.  vom Lok.  *homi  ,unten'  (:  ai.  ksdmi)  :  osk.  hu[n]truis  ,inferis',  huntrus  ,inferös'; umbr.  hutra,  kontra  ,lnfrä^  Abi.  hondomu  ,infimö';  umbr.  hondu  ,pessum- datö'  aus  *hon(d)-töd]  über  lat.  hümänus  s.  unten;
1046:Dazu  Worte  für  ,Mensch'  als  , Irdischer': -  lat.  homö,  -inis  ,Mensch',  alat.  hemö  (auch  in  nemo  , niemand'  aus  *ne- Äemö),  Akk.  hemönem]  zu  humus  wohl  hümänus  , menschlich',  mit  unklarem Vokalismus  (*hoim-  würde  zum  oi  des  air.  PI.  doini  , Menschen'  stimmen, falls  hier  alter  Diphthong  vorläge,  aber  für  ein  idg.  *gdhoim-  fehlt  jede Wahrscheinlichkeit;  s.  auch  unten);  osk. -umbr.  *homön-  (Ablautstufe  *ghom- wie  humus,  gegenüber  lat.  hemön-  oder  einzeldialektischer  Umlaut  aus *hemün-),  osk.   kumuns  ,homines',  umbr.   homonus  ,hominibus';
5637:Mit  Formans  -no-  alat.  mänus  ,gut',  immänis  ,schrecklich',  adverbial mäne,  mänl  ,früh';  hierher  auch  mänes  f.  ,die  abgeschiedenen  Seelen', später  , Unterwelt,  Tod';  vielleicht  phryg.  (j,rjv  ,abgeschiedene  Seele',  ^avla „*xaAiJ";  oder  gehört  lat.  mänes  zu  gr.  (^rjvig,  dor.  (,iävig  , Groll'?  vgl.  S.  727.
5746:manu-s  oder  monu-s  ,Mann,  Menscht
5748:WP.  II  266,  Trautmann  169;  vielleicht  zu  3.  men-  ^denken^
6176:3.  men-  , denken,  geistig  erregt  sein' ;   erweitert  meng-  :  mnä-  und  mne-,
6241:Mena  ist  gr.  Lw.),  seme(n)stris  , sechsmonatig,  halbjährig',  umbr.  memn^' ,mense';  air.  ml  (*mens),  Gen.  mls  (*7nmsos),  cymr.  acorn.  mis,  bret.  7^12 , Monat';  got.  mena,  aisl.  mäni,  ags.  möna,  as.  ahd.  mäno  ,Mond'  (-en-St.)- got.  menöps,  aisl.  mänadr,  ags.  mönad,  as.  mänuth,  ahd.  mänöt,  nhd.  Monat (*me7iöt-),  lit.  miinuo  (*menöt),  m^nesis  m.  ,Mond,  Monat',  lett.  menes(i)g ,Mond,  Monat'  (dial.  lit.  minas  aus  einem  neutr.  *menos),  apr.  menins ,Mond';  abg.  m§s§ch  m.  ,Mond,  Monat'  (*mes-n-ko-) ;
6377:Auf  dem  *zn9-n-  der  Kasus  obliqui  beruhen:  lat.  manus,  -üs  f.  ,Hand' (der  w-St.),  umbr.  mänuv-e  ,in  manu',  Abi.  mani,  osk.  Akk.  manim,  Kons.-St. noch  in  umbr.  matif  Akk.  PL ;  lat.  mancus  ,verstümmelt'  (ursprüngl. ;an  der  Hand^) ;  hierher  lat.  mandö,  -äre  , anvertrauen,  befehlen',  osk.  aama- naffed  ,mandävit',  manafum  ,mandavi*?  aus  manus  und  -dere  (Wz.  dhe-), wörtl.  ,in  die  Hand  legen';  mir.  montar,  muinter  , rechtmäßige  Gattin';
```


## [2026-09-07T16:13:33.461Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5744,5752p' POK_02.txt; echo \"=====MEN3=====\"; sed -n '6176,6215p' POK_02.txt",
 "description": "Print POK manus and men-3 entries"
}
```


### [2026-09-07T16:13:33.514Z] TOOL RESULT

```
700
möin   f.    ^Moos,   Sumpf,    Torf^;    vielleicht    dazu    ablaut.    asächs.    -mannia -mennia  in  FIN  und  ON,  wie  Throtmennia  ,Dortmund^,  usw. WP.  11  224,  WH.  II  30f.,  J.  Loth  RC  42,  91  f.
manu-s  oder  monu-s  ,Mann,  Menscht
Ai.  manu-,  mdnus-  , Mensch,  Mann^  (auch  , Ahnherr  der  Menschen'),  av im  PN  Manus-cid-ra-,  urgerm.  *manuaz  im  PN  Mannus  (Tacitus),  Stamm- vater der  Deutschen,  got.  manna  (Gen.  mans),  aisl.  madr,  mannr,  a^ afries.  ahd.  mann  ,Mann',  got.  mannisJcs,  aisl.  mennskr,  ags.  ahd.  mennUc ,menschlich^;  ahd.  mannisho  usw.  ,Mensch^;  aksl.  moh,  russ.  muz  ,Mann* (*mangia-y  Suffix  ähnlich  wie  in  lit.  zmo-g-üs  ,Mensch^).
WP.  II  266,  Trautmann  169;  vielleicht  zu  3.  men-  ^denken^
marko-  _,Pferd^;  nur  kelt.  und  g-erm.
Ir.  marc,  cymr.  usw.  march  ,Pferd^,  gall.  y.aQY.av  Akk.  Sg.,  Marco- durum  ON;
ahd.  marali,  ags.  mearTi,  aisl.  marr  ,Pferd'  (nhd.  in  Marschall,  -stalV)^ fem.  ahd.  meriha,  ags.  miere,  aisl.  merr,  nhd.  Mähre.
WP.  II  235.
=====MEN3=====
3.  men-  , denken,  geistig  erregt  sein' ;   erweitert  meng-  :  mnä-  und  mne-,
nienei-  :  nieni-]  Nominalbildungen:  men-raen-  n.,  znenos-  n.,  men-ti-^ men-tu-,  nioni-,  znn-ti-,  mn-to-  ,Sinn,  Gedanke',  men-ter-  , Denker'. Ai.  mdnyate  , denkt',  av.  mainyeite  ds.,  ap.  mainyähay  (idg.  *men-i-0', =  gr.  {.laivofxai  ,rase',  air.  -muiniur,  slav.  mhnjq  , meine,'  s.  unten),  ai.  Perf. ma-mne,  mene^  manäy-ati  ,ist  eifrig',  manä-yu-  , eifrig,  fromm',  manl-sä ,Weisheit,  Verstand ;  Andacht,  Gebet'  (*m^nei-  :  m^ni-) ;  ai.  mannte  , denkt'; mdnati  , erwähnt'  (=  lit.  menü,  poln.  -mione,  öech.  -menu);  0.1.  mandyati  ,ehrt , ( :  lit.  is-monis  , Verstand'),  av.  manaydn  ,man  könnte  glauben' ;  Supin.  ai.
727
„idntum,   Partiz.  Perf.  matd-  ,gedacht'  (=  gr.  aiTÖ-^arog,   lat.  commentus, lit.  mifitas,  air.  dermat)]
von  der  ä-Basis  (=  gr.  uva-):  ai.  mnätd-  ,erwähnt';  mnäydte  ,wird  er- wähnt* ;
ai.  mdnas-,  av.  manah-  n.  ,Sinii'  (=  gr.  (.isvog);  ai.  durmands  {=  öva^e- vrjg)]  3,p.  Haxä-manU  'Ayaiuivr^g  ,von  Freundessinn  beseelt';  ai.  mdnman- ,Sinn,  Gedanke'  (=  air.  menme);  mantdr-  ,Denker'  (=  gr.  Msvtwq,  lat. commentor);  müni-  ra.  begeisterter,  Seher  (vgl.  nccvrig),  Asket';  mdntra- m.  , religiöse  Formel',  av.  mq-d-rö  ds.;
ai.  su-mnd-  n.  , Wohlwollen' ;  äi.  ma^z-,  maa*-,  av.  -maiti-  ,Sinn,  Gedanke, Meinung'  (=  lit.  mintis,  abg.  pa-mgit,  got.  ga-munds,  lat.  wem),  woneben auch  ai.  manti-  , denken'  (=  got.  ana-minds) •  mdntu-  ds.;  abhi-mäti-  f. ^Nachstellung'  (*-'»ini-i-) ;
arm.  i-manam  , verstehe'  {*menä-mi,  vgl.  unten  ahd.  manön)] gr.  (xsfxova  {ix6f.iai.isv]  f^sfiäcbg,  mit  metr.  Dehnung  (xe^iäcog)  ,gedenke, habe  Lust,  verlange'  (Präteritopräs.  wie  lat.  meviini,  unredupl.  got.  man), Imper.  Perf.  !.ie(.i(XTü)  (=  lat.  mementö) ;  avTÖ-(.iaTog  ,aus  sich  selber  heraus- denkend und  handelnd' ;  fi(xivo(.Lai  ,bin  verzückt,  rase'  (=  mänyate  usw.), 1  Aor.  if.i7]vcc(j.r]v,  ifiavrjv,  Perf.  (j,6{.ir]va]  vgl.  fiavla  ,Raserei',  (lavTig  , Seher', fiaivdgj  -ddog  ,die  Verzückte',  (.laivölTjg,  -oXig  , rasend' ;
von  der  Basis  auf  ä-:  Perf.  (.i6(j,vrjfiaL  (dor.  -ä-)  ,bin  eingedenk',  Präs. jiL(Xvfj(Ty.ü}  (äol.  y,LfivaioY,(jü)  , erinnere',  Med.  , erinnere  mich',  Fut.  i.ivr^oo}] ^vdofiai  ,erinnere  mich'  in  hom.  (xvcoöfisvog,  (.nwovro ;  fxvrjaig  f.  , Erinnerung', fivrjfj,a)v  , eingedenk',  fi^rjua,  dor.  (xväfia  , Erinnerungszeichen,  Grabmal'; (ih'og  n.  (=  ai.  mdnas-)  ,Mut,  Zorn';  (xsvoLvda)  ,habe  im  Sinn,  habe  vor', pLSvoLvrj  , Wunsch',  auf  Grund  eines  Subst.  *{.i6rd)(i)  (vgl.  den  Frauen- namen MsvcüL,  Msvü)  und  die  Ableitung  Mevolrrjg,  MevoixLog) ;  ^fjvLg,  dor. fxävig  , Groll'  (*uvävLg?)]  vgl.  oben  S.  693: alb.  mund,  mend  ,kann'  (*mn-dh-)',
lat.  meminl  , erinnere  mich,  bin  eingedenk'  (:  gr.  ixe^iova]  vgl.  osk.  mem- nim  ,monumentum,  memoriam') ;  von  der  Basis  auf  -l  ( :  -ei)  minlscitur  ds., comminlscor  , erinnere  mich';  mens, -tis  , Sinnesart,  Gemüt,  Denkvermögen, Vernunft'  (aus  *mnti-,  s.  oben  ai.  mati-  usw.),  mentiö  , Erwähnung'  (=  air. air-mitiu),  Denom.  mentior,  -Iri  , lügen'  (vgl.  apr.  mentimai  ,wir  lügen', d.  i.  ,Ersonnenes  vorbringen',  vgl.  z.  Bed.  noch  commentum  , Erdichtung, Plan',  zum  Partiz.  commentus  , ersonnen',  und  lit.  pra-manytas  , erdichtet, falsch');  Kaus.  moneö  , mahne'  (=  lit.  is-manyti,  dehnstufig  ai.  mändyati), monitor  m.  , Mahner',  monumentum  , Erinnerungszeichen',  mönstrum  , Mahn- zeichen, Ungeheuer'  (*mone-strom),  mön-sträre  .anzeigen',  usw.;
air.  do-moiniur  ,glaube,  meine'  (=  fxaivouat,  ai.  mdnyate,  mit  -mo-  aus •ma-)  und  viele  andere  Komposita ;  Simplex  in  ro-menair  ,er  hat  überlegt',
728  *
dia-ru-muinedar  ,für  die  er  bestimmt  hat';  mit  o-Stufe  (vgl.  moneo)  ab guo-monim  gl.  ,polliceri' ;    air.   cuman,   cuimne  (=  mcymr.  covein)  ,Erin    ^ rung',    cjmr.    co-f  {*Jcom-men)    ds. ;    air.    menrae   (=  ai.    manman-)     Geist^ Sinn';  air.  dermat  , Vergessen'  (*- 17113,(0-),  airmitiu  (*are-mentiö)  ,honor'  usw  •
got.  *man,  munum  (Inf.  munan,  Prät.  mundo)  , meinen,  glauben'  (Prät* Präs.  wie  ^efxova^  memim,  j.is(j,vr]uaL),  ga-munan  ,sich  einer  Sache  erinnern*^ aisl.  muna  , gedenken,  sich  erinnern',  munu,  mono  , beabsichtigen,  werden**^ ags.  mon,  man  ,(ge) denke',  3.5.  far-munan  (Fvsit.  -munsta)  »nicht  gedenken  ■■■ verleugnen';  got.  schw.  V.  munan  (3.  Sg.  munaip,  Prät.  munaida)  »gedenken (zu  tun),  (xsXXsLv^  (munaip  aus  ^m^nei-eti  =  ai.  manay-ati,  vgl.  m^ne-  [xiA ahd.  ßrmonen  , verachten'  (und  slav.  monäti,  lit.  minUi,  sowie  —  wenn  all —  gr.  ij,av7jvai) ;  o-stuf.  ahd.  as.  manön,  ags.  manian  , mahnen'  (ahd.  maiun 3.  Sg.  =  lit.  mäno  ,versteht',  vgl.  reduktionsstufig  arm.  i-manam  »verstehe' aus  *m^nämi)\  got.  muns  m.  , Gedanke,  Meinung',  aisl.  munr  ,Sinn,  Ver- langen, Lust',  ags.  myne  , Erinnerung,  Verlangen,  Liebe',  as.  muni-lik , lieblich'  (=  ai.  müni');  got.  ana-minds  , Verdacht'  (=  ai.  manti-),  ga-minU n.  , Andenken',  aisl.  minne  , Erinnerung',  ahd.  as.  minn{e)a  , Liebe,  Minne* (*minpjä,  *mindjä)]  got.  ga-munds,  Si^s.  ge-mynd,  ahd.  gi-munt  , Andenken Gedächtnis'  (=  ai.  mati-  usw.);
lit.  menü  (==  wslav.  *-meng,  ai.  mdnati),  miüti  , gedenken',  red.-stuf. miniü,  mineti  (:  ahd.  ßrmonet  usw.)  ,ds.,  erwähnen',  lett.  minet  ds.,  ablaut, Yit.manyti  , verstehen*;  dehnstufig  U-moms  , Verstand';  lit.  wzn^zs  , Gedanke' (=  ai.  mati-  usw.);  menas  m.  , Kunst' ;  prä-mintas  , benannt' ;  apr.  mentimai ,wir  lügen^;
aksl.  mhnjo  (mtniSi),  mtn^ti  , meinen',  po-mbniti  .gedenken,  sich  erinnern', pam^tb  , Gedenken';   toch.  A  mnu  , Denken'^,  B  manu  ,Verlangen^;
hitt.  me-im-ma-i  (memmai)  ,sagt',  falls  aus  *memn-  oder  *men-?  Vgl. Benveniste  BSL.  33,  140,  Pedersen  Hitt.  116,  Bonfante  Lg.  17,  205ff.
WP.  II  264ff.,  WH.  II  65ff.,  68ff.,  107,  109f.,  Trautmann   ISOf.
4.  inen-,  teils  mit  u-,  uo-,  teils  mit  k-Formantien  ,klein,  verkleinern ;  ver- einzelt'. u-,  uo-St. :  arm.  manr,  Gen.  manu  , klein,  dünn,  fein',  manuk  ,Kind, Knabe,  Diener';  gr.  (.idw-^a'  iiovo%e(paXov  a-KÖQodov  Hes.,  ixdw  fj-r/tgöv (Hs.  niTigöv)  ^Ad-afxavsg  Hes.,  ^ävög,  att.  f.iccvög  (*^avJ^6g)  ,dünn,  locker, spärlich',  diss.  ßavöv  (=  ixavöv)  •  Xbtvxöv  Hes. ;  dazu  als  , isoliert  sich'  nach Brugmann  RhMus.  62,  634 f.  (Lit.)  ^avavstai'  nageXy-eTau  Hes.;  d.  i. , drückt  sich,  schleicht  sich  weg^  und  mit  Diss.  eventuell  att.  ßccvavaog ,(*wer  sich  abseits,  von  andern  fernhält'  =)  ,der  kleine  Mann  mit  be- schränktem Gesichtskreis' ;  o-stufig  ion.  f^ovvog,  dor.  ^wvog,  att.  i.iövog  (*^6v- Sog)  ,allein,   vereinzelt';   air.  min  (^meni-)   .glatt,   sanft';   menb   , klein',  alt
729
}fenueh  Gen.,  cjmr.  di-fanw  »unbedeutend',  di-fenwi  (*mnu-)   »verkleinern, schmähen'.
Mit  ir-Formans:  ai.  manäk  ,ein  wenig';  ahd.  mengen  {*mangjan)  und „langolön  , entbehren',  nhd.  mangeln,  mhd.  manc  (-g-)  »Mangel,  Gebrechen* ; lit.  menkas  »gering,  unbedeutend',  menke  , Dorsch,  Aalquappe',  usw.;
toch.  B  menki  , minder' :  hitt.  ma-ni-in-ku-wa-an-te-es  Nom.  PI.  ,kurz'.
WP.  II  266  f.,  WH.  II  93.
c.  aien-  , bleiben,  (sinnend)  stillstehen'  (=  men  »denken'?).
Ai.  man-  {parimamandhi,  dmaman)  »zögern,  stillstehen',  av.  ap.  man- , bleiben,  warten',  av.  fra-man-  ,ausharren';  arm.  mnam  , bleibe,  erwarte' {*menä-)\  gr.  i.isv(ü,  ixluvü)  {(.isfisvrj-Ka)  »bleibe'»  liovt^  f.  ,das  Bleiben',  (x6vL(.iog ^ausharrend',  ^i^vwv  ,Esel'  (,ausdauernd') ;  \a.t.  maneö,  -ere  (vgl.  [xsfxevTj-yta) , bleiben'  (*m^neiö),  Denomin.  mantäre  ,saepe  manere';  air.  ainmne,  cymr. amynedd,  mcymr.  anmynedd  , Geduld'  {*an-meniä) ;
toch.  AB  mäsk-  »sein';  hitt.  mi-im-ma-i  , verweigern'.
WP.  II  267,  WH.  II  26,  Pedersen  Hitt.  121.
mend-,  znond-  (mnd-?)  , säugen»  saugen;  Brust';  auch  »junge,  saugende Tiere'. Alb.  ment  , säuge,  sauge',  mezej  , säuge' ;  mes,  m.ezi  m.  , Füllen',  mezat ,junger  Stier,  Tierjunges',  mezore  »junge  Kuh'  (*mondiO')-  illyr.  PN  Menda f.  , Stute',  ablaut.  P^  3Iandeta'^  mandos  »kleines  Pferd',  daraus  diaX.  mannns : lat.  , kleines  gall.  Pferd';  messap.  Juppiter  Menzana  {*mendio-no-)  »Gott, dem  Pferde  geopfert  wurden' ;  aus  dem  lUyr.  stammt  rom.  mandius  »Füllen, Rind'  (rum.  minz  , Füllen',  manzat  »junge  Kuh',  nhd.  Tirol  Manz,  Menz ,unfruchtbare  Kuh',  rheinländ.  Minzekalb,  bask.  mando  .mulus',  usw.); mir.  menn  (*mendo-),  menndn  »junges  Tier,  Kalb,  Füllen',  sekundär  benndn , Kälbchen,  Böcklein,  Hirschlein',  nir.  binnseach,  gael.  minnseach  , Zicklein', cymr.  mynnan  ,kid',  corn.  min  ,haedus',  bret.  menn  ,junges  Tier',  menn gavr  , Zicklein' ;  gall.  ON  Epo-manduo-durum,  brit.  ON  Mandu-essedum (illyr.  Lw.?);  wohl  auch  der  bair.  FIN  Mindel;  ahd.  manzon  m.  PL  , Zitze, Euter';  illyr.  gall.  mand-  könnten  auch  idg.  Ablaut  mnd-  enthalten.
WP.  II  232,  WH.  II  29  f.,  Marstrander  ZceltPh.  7,  384 f.,  Krähe,  Würz- burg. Jb.  1,  189,  202.
mend(ä,  -om)  , Fehler,  Körperfehler,  Gebrechen'  (auch  ,Makel,  Fleck'?). Ai.  mindä  , Körperfehler'  {im- *mandä  nach  nindä  »Tadel'); lat.  mendum,  menda  »Fehler,  Gebrechen'»  e-mendäre  »ausbessern;  heilen', wovon  mendlcus  »Bettler'  und  mendäx,  -äcis  ,lügnerisch'  (* fehlerhaft);
730
vielleicht  air.  mennar  ,n3acula*,  schwundstufig  air.  mind  , Zeichen,  Merk mal*  (*mndu  n.;  auch  in  der  Bed.  ,diadema'  =  .insigne'  dass.  Wort),  cymr mann  , Platz,  Stelle',  mann  geni  , Muttermal'.
WP.  II  270,  WH.  II  69,  J.  Loth  RC.  44,  362  f.
mendh-  , seinen  Sinn  worauf  richten,  lebhaft  sein';    m(o)ndh-ro-  _,munter'
Ai.  medhä  , Weisheit,  Einsicht,  Verstand',  av.  mazdä,  mazdäh-  n.  Ge- dächtnis, Erinnerung',  mazdäh-  m.  Name  des  höchsten  Gottes  (*mazdha aus    ^mndh-ta) ;
gr.  fiavd-dvw  (sekundäres  Präs.  zu)  fj,adrjGOf,taL,  ^a&etv  , lernen',  dor.-äol. ixadtj,  ion.  iia&og  n.,  ion.-att.  (.iddr/aig  , Lernen,  Unterricht';  (^ev-d^rjQT]  , Stirn- (pQOVTLq' ;  vielleicht  Movoa  {*^iov-d-ia)  ,Muse' ;
alb.  mund  ,kann,  siege' ;
cjmr.  mynnu  , wollen',  com.  mennaf  ,ich  will',  mynnes,  mynnas  ,wollen Wille',  cymr.  go-fin(n)  ^verlangen,  bitten,  fragen',  corn.  govyn  ds. ;
got.  mundön  , sehen  auf,  mundrei  ,Ziel',  aisl.  munda  ,zielen,  streben*, ahd.  muntar  , eifrig,  munter^,  muntari  , Eifer';  ahd.  mendl  ,Freude',  menden, as.  mendian  ,sich  freuen';
```


## [2026-09-07T16:13:52.814Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5815,5830p' POK_02.txt",
 "description": "Context of Mousa mention line 5825"
}
```


### [2026-09-07T16:13:52.861Z] TOOL RESULT

```
WP.  II  237 f.,  WH.  II  70f.,  81  f.,  Trautmann  179,  183;  verwandt  mit 1.  med-.
4.  me-,  mö-  ,groß,  ansehnlich'.
Positiv  me-ro-s,  mö-ro-s:  gr. -ficogog  in  ^yx^ct-^w^og  ,groß(?)  im  Speer- werfen' u.  dg'l.,  air.  mör  (das  ö  aus  dem  Komparativ),  mär  ,g"roß',  cymr. mawr  ,groß',  bret.  meur  ds.,  gall.  -märos  in  Eigennamen  wie  Nerto-märot (,groß  an  Kraft') ;  mit  e  ahd.  -Tnär  in  Namen  wie  Volk-mär  usw.,  ferner das  Denominativ  germ.  *merjan  ,*als  groß  darstellen,  rühmen',  woraus ,künden':  got.  merjan^  as.  märian,  ahd.  mären,  anord.  mcera  ,verkünden', wozu  nhd.  Mär^  Märchen  u.  dgl.,  sowie  das  postverbale  Adj.  ahd.  as. märi  ,berühmt,  glänzend',  ags.  möere,  anord.  mcerr  ds.,  got.  waila-mereis ,von  gutem  Ruf;
slav.  -merz,  in  Namen  wie  Vladi-mSrbj
mö-lo-  in  cymr.  mawl  ,Lob',  moli  ,loben'  (daraus  air.  molur  ,lobe'), bret.  meuliff  ds. ;
Komparativ  *rae-ies,  -is,  bzw.  (mit  der  Tiefstufe  des  Superlativs)  ms-iesj zn9-is:  air.  mäu,  daraus  möu,  mö  (aus  *md-{ös)]  cymr.  mwy,  corn.  may, bret.  mui  ,mehr'  aus  *7nezs;  eine  Abstraktbildung  auf  urkelt.  -anti  (*mantl aus  ma-antl)  in  air.  meit  , Größe',  acymr.  pamint  gl.  ,quam'^  ncymr.  maint ,Größe',  corn.  myns,  mbret.  nbret.  ment]  vielleicht  osk.  mais  (*md-i8-)  Adv. ,mehr',  maimas  ,maximae'  (wohl  aus  *mais[e']mo.),  GN  Maesius  , Mains', umbr.  mestru  f.  ,maior'  (aus  *maisterä) ;  got.  mais  ,raagis',  maiza  ,maior', maists  ,maximus',  aisl.  meir{i)  ,mehr',  ags.  mä,  mära,  mcestj  as.  mer, mero,  mest,  ahd.  mer,  mero^  meist]  apr.  muisieson  Adv.  ,mehr'  (muis  aus *ma-is-)'j  toch.  A  mdnt  ,wie',  B  mantd  ,so'  (=  air.  meit?).
WP.  II  238,  292,  WH.  II  14.
5.  me-,  mö-,  mo-  ,heftigen  und  kräftigen  Willens  sein,  heftig  streben'.
Gr.  ^aio^ai  (äol.  iiao^ai)  ,strebe,  trachte',  wozu  die  Namen  E^fxaiog, Olvöfiaoi;,  Malcjv  (*m?-to-) ;   mit  Intensivredupi.    (j,aL^dü)   ,verlange   heftig'    .
■  705
(.uaw  mit  Red.-Stufe  der  Wz.  wie  SaL-ddXXo)  usw.),  Infin.  iiwod-ai  ,strebeii^, partiz.  ^(bfisvog;  (AaJraL  (Epich.)  *  Kt^tsl,  'i;sxvü'C,ei:ai  Hes.  (und  andere  Glossen), aus  dem  o-stufigen  Perf.  erwachsen;  Movaa  ,Muse^  hierher  oder  zu  mendh-?
auf  einem  Partiz.  *^mrdg  beruht  ^arsvco  ^suche,  suche  auf;  strebe^; partiz.  *f.iaGTÖg  ,wo  nach  auch  y.aOTevo)  =  ixaTsvoj ;  (xarel '  ^rizsT  Hes. ;
lat.  mos,  möris  ,die  jedem  eigene  Art;  Sitte;  durch  Gewohnheit  fest- ere wordener  Brauch',  mörösus  , eigensinnig';
got.  mops  (-d-)  ,Mut,  Zorn'  (mödags  , zornig'),  ahd.  mhd.  muot  ,Kraft des  Empfindens;  Geist,  Mut,  Zorn,  Begehren,  Entschluß',  nhd.  Mut,  Gemüt, ags.  möd  ds.,  aisl.  mödr  ,Zorn';
baltoslav.  *matö  ,nehme  wahr'  in  lett.  matu,  mast  , wahrnehmen,  fühlen', ursprüngl.  Iterativ  lit.  mataü,  matyti  ,sehen',  lett.  matu,  matit  ,empfinden', lit.  matrüs  ,vorsichtig';  auf  einem  Subst.  *motro-  beruht  ksl.  mostrjq, motriti  ,spectare',  usw.;  dazu  wohl  abg.  s^-m^jo,  -mHi  , wagen'.
kWP.  II  238  f.,  WH.  II  114  f.,  Trautmann  171;    wohl  zu  mö-,  mö-lo-. .  med-  ,messen,  ermessen';  medos-  ,Ermessen';  mwd-  ,Arzt'. A.  Ai.  masti-  f.  ,das  Messen,  Wägen'  (^med-tis,  mit  im  isolierten  Wort nicht  rückgängig  gemachtem  Wandel  von  d-t  zu  s-t-?);
```


## [2026-09-07T16:14:01.041Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"men-1\\|men- 1\\|^men\" AHD_watkins1985.txt | head -40",
 "description": "Grep AHD Watkins for men roots"
}
```


### [2026-09-07T16:14:01.087Z] TOOL RESULT

```
217:men-1, I. Zero-grade form *mn-...
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
745:men-!, To think; with derivatives referring to various qualities and states of mind and thought. I. Zero-grade form *mn-. 1. Suffixed form *mmy-ti- in: a. Germanic “ga-mundi- (*ga-, intensive prefix; see kom), in Old English gemynd, memory, mind: MIND; b. Latin méns (stem ment-), mind: MENTAL; AMENT?, DEMENT; c. Latin mentid, remembrance, mention: MENTION. 2. Suffixed form *mn-to- in Greek -matos, “willing”: AUTOMATIC. 3. Suffixed form *mn-yo- in: a. Greek mainesthai, to be
747:meng-
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
1027:ste-men-. Denoting various body parts and orifices. Greek stoma, mouth: STOMA, STOMACH, STOMATO-, (STO- MATOUS), -STOMY; ANASTOMOSIS, ANCYLOSTOMIASIS, PROSTOMIUM, SCYPHISTOMA. [Pok. stomen- 1035.] storo-. Starling. Germanic *staraz in Old English ster, starling: STARLING}. [Pok. storos 1036.]
1219:AGIO al-1 AGITATE ag- AGLET ak- AGMINATE ag- AGNAIL angh- AGNATE gene- AGNI egni- _ AGNOMEN no-men- AGNOSIA gnd- AGO ghé- -AGOGUE ag- AGONY ag- AGORA! ger-1 AGORAPHOBIA ger-! AGRAFFE ger-2 AGRAPHA gerbh- AGRAPHIA gerbh- AGRARIAN agro- AGREE gWere-3 AGRESTAL agro- AGRIA agro- AGRICULTURE agfo- AGRIOECOLOGY agro- AGRIOLOGY agro- AGROSTOLOGY agro- AHIMSA ghei-i, ne AHRIMAN men-1
1220:AnuRA MazpDa_ansu-, men-1
1237:AMBLYOPIA mel-1 AMBROSIA mer-2 AMBSACE ambho AMBULATE al-2 AMBUSCADE busk- AMBUSH busk- AMELIORATE mel-4 AMENABLE men-2 AMEND mend- AMENORRHEA mé-2 AMENT! = ap-1 AMENT2 men-1 AMETHYST medhu- AMIANTHUS mai-2 AMICABLE amma AMICE yé-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1419:DEMENT men-1 DEMETER mater- DEMILUNE leuk- DEMIT (s)meit(a)- DEMIURGE da-, werg- DEMOCRACY da- DEMOLISH mé6- DEMON da- DEMONSTRATE men-! DEMOPHOBIA da- DEMOS da- DEMOTIC da- DEMUR mere- DEN dan- DENARIUS dekm DENARY dekm DENDRO- deru DENDRON deru DENIER? dekm DENIGRATE negW-ro- DENOMINATE no-men- DENOUEMENT ned- DENOUNCE neu-! DENSE dens-2 DENTAL dent- DENTATE dent- DENTI- dent- DENTICLE dent- DENTIFRICE bhréi- DENUDE nogw- DENY ne
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1811:MANACLE man-2 MANAGE man-2 MANANA ma-1 -MANCY men-! MANDAMUS man-2 MANDARIN men-1 MANDATE man-2 MANDIBLE mendh-2 MANDOLIN pandoura MANE mon-
1812:MANEGE man-2 MANES ma-1 MANEUVER man-2, op-1 MANGE mendh-2 MANGELWURZEL_ wrad- MANGER mendh-2 MANGLE! = mai-1 MANGONEL meng- MANIA men-1
1813:MANIAC men-! MANICOTTI man-2 MANICURE cilra, man-2 MANIFEST dhers-, man-2 MANIKIN man-1 MANIPLE man-2 MANIPULATION man-2 MANNEQUIN man-! MANNER man-2 MANOMETER men-4 MANOR men-3 MANQUE man-2 MANSE men-3 MANSION men-3 MANSUETUDE man-?, s(w)e- MANTIC men-1 MANTICORE mer-2 MANTIS men-1 MANTRA men-1 MANUAL man-2 MANUBRIUM man-2 MANUFACTURE dhé-1, man-2 MANUMIT man-2 MANURE man-?, op-1 MANUS man-2 MANUSCRIPT man-2, skribh- MANY menegh-
1846:MELON mélion MELT mel-1 MEMBER méms- MEMBRANE méms- MEMENTO men-! MEMORABLE (S)mer-1 MEMORANDUM (s)mer-1! MEMORY (s)mer-1 MENACE men-2 MENAGE men-3 MENARCHE = arkhein, mé-2 MEND mend- MENDACIOUS mend- MENDICANT mend- MENHIR s6-2 MENINX méms- MENISCUS mé-2 MENOPAUSE mé-2 MENSCH man-! MENSES mé6-2 MENSHEVIK mei-2 MENSTRUAL mé-2 MENSTRUATE mé-2 MENSURAL mé-2 MENTAL men-1 MENTION men-1 MENTOR men-1 MENU mei-2 MERCENARY merk-2 MERCER merk-2 MERCHANT merk-2 MERCURY merk-2 MERCY merk-2 MERE! mer-1 MERE? mori-
1874:MINE? me-1 MINERVA men-! MINESTRONE mei-2 MINGLE mag- MINIKIN men-1 MINIMUM mei-2 MINISTER mei-2 MINISTRY mei-2 MINIVER wer-! MINNESINGER men-!, sengWh- MINNOW men-4 MINOR mei-2 MINT! men-1 MINUEND mei-2 MINUS mei-2 MINUSCULE mei-2 MINUTE? mei-2 MIOCENE mei-2 MIOSIS mul-
1879:MITOCHONDRION ghrendh-, mei-4 MITOSIS mei-4 MITTEN medhyo- MITTIMUS (s)meit(a)- MIX meik- MIXTURE meik- MIZZEN medhyo- MIZZLE meigh- MNEMONIC men-! MNEMOSYNE men-1 MOAN mei-no- MOB meue- MOBILE meue- MODAL med- MODE med- MODEL med- MODERATE med- MODERN med- MODEST med- MODICUM med- MODIFY dhé-1, med- MODIOLUS med- MODULATE med- MODULE med- MODULUS med- MOGUL! miik- MOIETY medhyo- MOIL mel-1
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
1892:MORTUARY mer-2 MORT! mer-2 MORULA moro- MOSAIC men-1 MOSQUITO = mu-2 MOss meu- MOssO meue- MOST mé-3
1897:MUNIFICENT mei-1 MUNITION mei-3 MURAL mel-3 MURAMIC ACID mei-3 MURDER mer-2 MURE mei-3 MURINE mis- MURK mer-1 MURMUR mormor- MURRAIN mer-2 MURREY moro- Musca mu-2 MUSCARINE mu-2 MUSCLE miis- MUSE misum Muse men-1 MUSEUM men-! MUSH2 mu-2 MUSIC men-1! MUSKET mu-2 MusT! med- MUSTS ~=meu- MUSTACHE mendh-2
1997:ORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- ORGASM wrdg- ORGEAT ghers- ORGY werg- ORIENT er-1 ORIFICE 6s- ORIFLAMME aurum ORIGIN er-1 ORIGINAL er-! ORINASAL 6S- ORIOLE aurum ORLOP klou-, uper OrMaAzD ansu-, men-1 ORMER mori-, ous- ORMOLU aurum, mele- ORNAMENT ar- ORNATE ar- ORNITHO- oF OROIDE aurum OROTUND 6s- ORPHAN orbh- ORPHREY aurum ORPIMENT aurum ORT ed-, ud- ORTHO- wrddh- ORTHODOX dek-1 ORTHOGONAL genu-1 ORTHOPEDICS pau- ORTHOSTICHOUS _steigh- ORTHOTICS wrddh- ORTOLAN gher-! os! Os-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
```


## [2026-09-07T16:14:09.100Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '745,748p' AHD_watkins1985.txt | fold -w 200 | head -60",
 "description": "Read AHD men-1 entry"
}
```


### [2026-09-07T16:14:09.158Z] TOOL RESULT

```
men-!, To think; with derivatives referring to various qualities and states of mind and thought. I. Zero-grade form *mn-. 1. Suffixed form *mmy-ti- in: a. Germanic “ga-mundi- (*ga-, intensive prefix
; see kom), in Old English gemynd, memory, mind: MIND; b. Latin méns (stem ment-), mind: MENTAL; AMENT?, DEMENT; c. Latin mentid, remembrance, mention: MENTION. 2. Suffixed form *mn-to- in Greek -mat
os, “willing”: AUTOMATIC. 3. Suffixed form *mn-yo- in: a. Greek mainesthai, to be
41
meng-
mad: MAENAD; b. Avestan mainyu, spirit: AHRIMAN. II. Full-grade form *men-. 1. Suffixed form *men-ti- in Germanic *minthj6 in: a. Old High German minna, love: MINNESINGER; b. Middle Dutch minne, love:
 MINIKIN. 2. a. Reduplicated form in Latin meminisse, to remem- ber: MEMENTO; b. Latin comminisci (¢com-, intensive prefix; see kom), to contrive by thought: COMMENT; c. Latin reminisci (re-, again, 
back; see re-), to recall, recollect: REMINISCENT; d. possibly Latin Minerva, name of the goddess of wisdom: MINERVA. 3. a. Greek menos, spirit: EUMENIDES; b. Greek Mentér, man’s name (probably mea
ning “adviser”): MENTOR; c. Greek mania, madness: MANIA, MANIAC; d. Greek mantis, seer (< “he who is mad”): -MANCY, MANTIC, MANTIS. 4, San- skrit mantrah, counsel, prayer, hymn: MANDARIN, MAN-
 TRA. III. O-grade form *mon-. 1. Suffixed (causative) form *mon-eyo- in Latin monére, to remind, warn, advise (with probable derivative monéta, an epithet of Juno): (MINT!), MONEY, MONISH, MONITION
, MONITOR, MON- STER, MONUMENT, MUSTER; ADMONISH, DEMONSTRATE, PREMONITION, SUMMON. 2. Suffixed o-grade form *mon- twa in Greek mousa, a muse: MOSAIC, MUSE, MUSEUM, music. IV. Extended form mnd-. 1. R
eduplicated form in Greek mimnéskein, to remember (> amnésia, forgetful- ness, and amnéstos, forgotten): MNEMOSYNE; AMNESIA, AMNESTY, ANAMNESIS. 2. Greek mném6n, mindful: MNE- MONIC. V. Indo-Europ
ean verb phrase *mens dhé-, “to set mind” (see dhé-'), underlying compound *mns-dhé- in Avestan mazdd-, wise: AHURA MazpDA, ORMaAzD. [Pok. 3. men- 726, mendh- 730.]
```


## [2026-09-07T16:14:21.479Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"man-1\\|man-!\\|^man-\" AHD_watkins1985.txt | head; echo \"===\"; grep -n \"MANIKIN\\|mannequin\\|manneken\" AHD_watkins1985.txt | head",
 "description": "Grep AHD for man-1"
}
```


### [2026-09-07T16:14:21.538Z] TOOL RESULT

```
722:man-'. Also mon-. Man. 1. Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz), in: a. Old English man(n) (plural menn), man: MAN; Nor- MAN; b. Old High German man (> Middle High German man > German Mann), man: FUGLEMAN, LANDSMAN?; c. Middle Dutch man, man: MANIKIN, (MANNEQUIN); d. Old Norse madhr, mannr, man: NORMAN, OMBUDS- MAN. 2. Germanic adjective *manniska-, human, in Old High German mennisco, human: MENSCH. 3. Slavic suf- fixed form *mon-gyo- in Russian muzh, man: MUZHIK. [Pok. manu-s 700.]
723:man-?, Hand. 1. Latin manus, hand: MANACLE, MANAGE, (MANEGE), MANNER, MANUAL, MANUBRIUM, MANUS; AMANUENSIS, MAINTAIN, MANEUVER, MANICOTTI, MANI- CURE, MANIFEST, MANIPLE, MANIPULATION, MANSUE- TUDE, MANUFACTURE, MANUMIT, MANURE, MANUSCRIPT, MASTIFF, MORTMAIN, QUADRUMANOUS. 2. Suffixed form *man-ko-, maimed in the hand, in Latin mancus, maimed, defective: MANQUE. 3. Latin compound man- ceps, “he who takes by the hand” (-ceps, agential suffix, “taker”; see kap-), purchaser: EMANCIPATE. 4. Latin compound manddre, “to give into someone’s hand” (dare, to give; see d6-), entrust, order: MANDAMUS, MANDATE; COMMAND, (COMMANDO), COMMEND, COUN- TERMAND, DEMAND, RECOMMEND, REMAND. [Pok. ma-r- 740.]
1544:FROLIC fik-, preu- FROM per? FRONTISPIECE spek- FROST preus- FROTTAGE bhréi- FROWARD per! FRUCTIFY bhrig- FRUGAL bhriig- FRUGIVOROUS bhrig- FRUIT bhriig- FRUITION bhriig- FRUMENTACEOUS _ bhrig- FRUMENTY bhriig- FRUSTULE bhreus-2 FRUSTUM bhreus-2 FRY! bher-4 FUGACIOUS bheug-1 -FUGE bheug-! FUGITIVE bheug-1 FUGLEMAN man-1, pleu- FUGUE bheug-! FUHRER per-2 FULCRUM bhelg- FULGENT bhel-1 FULGURATE bhel-1 FULIGINOUS dheu-1 FULL! pele-1 FULMAR pu-2 FULMINATE bhel-1 FUMARIC ACID dheu-1 FUMAROLE dheu-1 FUMATORIUM dheu-! FUMATORY dheu-1 FUME dheu-! FUMIGATE ag-, dheu-! FUMITORY dheu-1, ters- FUNAMBULIST al-2 FUNCTION bheug-2 FUND bhudh- FUNDAMENT bhudh- FUNDUS_ bhudh- FUNGIBLE bheug-2 FUNNEL gheu-
1729:LAMIA lem-2 LAMMERGEIER ghai- LAMP |ap- LAMPOON lab- LANATE wele-1 LAND lendh-2 LANDSCAPE lendh-2, skep- LANDSMAN2 lendh-2, man-1 LANGLAUF del-1, klou- LANGUAGE dnghi LANGUET dnghi LANGUISH slég- LANIFEROUS wele-1 LANK kleng- LANOLIN wele-! LANTERN [ap- LANTHANUM [|adh- LANUGO wele-1 LAP! {eb-1
1810:MAN man-1
1813:MANIAC men-! MANICOTTI man-2 MANICURE cilra, man-2 MANIFEST dhers-, man-2 MANIKIN man-1 MANIPLE man-2 MANIPULATION man-2 MANNEQUIN man-! MANNER man-2 MANOMETER men-4 MANOR men-3 MANQUE man-2 MANSE men-3 MANSION men-3 MANSUETUDE man-?, s(w)e- MANTIC men-1 MANTICORE mer-2 MANTIS men-1 MANTRA men-1 MANUAL man-2 MANUBRIUM man-2 MANUFACTURE dhé-1, man-2 MANUMIT man-2 MANURE man-?, op-1 MANUS man-2 MANUSCRIPT man-2, skribh- MANY menegh-
1846:MELON mélion MELT mel-1 MEMBER méms- MEMBRANE méms- MEMENTO men-! MEMORABLE (S)mer-1 MEMORANDUM (s)mer-1! MEMORY (s)mer-1 MENACE men-2 MENAGE men-3 MENARCHE = arkhein, mé-2 MEND mend- MENDACIOUS mend- MENDICANT mend- MENHIR s6-2 MENINX méms- MENISCUS mé-2 MENOPAUSE mé-2 MENSCH man-! MENSES mé6-2 MENSHEVIK mei-2 MENSTRUAL mé-2 MENSTRUATE mé-2 MENSURAL mé-2 MENTAL men-1 MENTION men-1 MENTOR men-1 MENU mei-2 MERCENARY merk-2 MERCER merk-2 MERCHANT merk-2 MERCURY merk-2 MERCY merk-2 MERE! mer-1 MERE? mori-
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
1935:Norpic_ ner-1 NORM gné- NoRMA gno- NORMAL gno- NORMAN man-1, ner-1 NORN_ sner- NorsE_ ner-! NORTH ner-1 NORTHERN ner-1 NOSE nas-
1971:OMBUDSMAN ambhi, bheudh-, man-1
===
722:man-'. Also mon-. Man. 1. Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz), in: a. Old English man(n) (plural menn), man: MAN; Nor- MAN; b. Old High German man (> Middle High German man > German Mann), man: FUGLEMAN, LANDSMAN?; c. Middle Dutch man, man: MANIKIN, (MANNEQUIN); d. Old Norse madhr, mannr, man: NORMAN, OMBUDS- MAN. 2. Germanic adjective *manniska-, human, in Old High German mennisco, human: MENSCH. 3. Slavic suf- fixed form *mon-gyo- in Russian muzh, man: MUZHIK. [Pok. manu-s 700.]
1813:MANIAC men-! MANICOTTI man-2 MANICURE cilra, man-2 MANIFEST dhers-, man-2 MANIKIN man-1 MANIPLE man-2 MANIPULATION man-2 MANNEQUIN man-! MANNER man-2 MANOMETER men-4 MANOR men-3 MANQUE man-2 MANSE men-3 MANSION men-3 MANSUETUDE man-?, s(w)e- MANTIC men-1 MANTICORE mer-2 MANTIS men-1 MANTRA men-1 MANUAL man-2 MANUBRIUM man-2 MANUFACTURE dhé-1, man-2 MANUMIT man-2 MANURE man-?, op-1 MANUS man-2 MANUSCRIPT man-2, skribh- MANY menegh-
```


## [2026-09-07T16:14:30.062Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('../refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\"",
 "description": "KLN offsets"
}
```


### [2026-09-07T16:14:31.353Z] TOOL RESULT

```
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-07T16:14:36.590Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^man, n\\.\\|^Muse, n\\.\\|^muse\\|^mannequin\\|^manikin\\|^Norman, n\\|^Ormazd\\|^Ormuzd\\|^Ahriman\\|^mosaic\\|^museum, n\\|^music, n\\|^amnesty\\|^maniac\\|^automatic\\|^mental, adj\\|^mention\\|^monitor\\|^monster\\|^monument\\|^comment\\|^demonstrate\\|^mathematics\" KLN_1966.txt | head -40",
 "description": "Grep Klein 1966 headwords"
}
```


### [2026-09-07T16:14:36.656Z] TOOL RESULT

```
720:mathematics
8363:comment,  n.  —  ME.,  fr.  OF.  comment,  fr.  L.  com- mentum ,  ‘invention,  fabrication,  fiction’,  prop, neut.  of  pp.  commentus,  used  as  a  noun,  fr. comminiscor,  ‘I  devise,  invent,  contrive,  fabri¬ cate’,  which  stands  for  *com-mcn-iscor  and  lit. means  '1  ponder’,  fr.  com-  and  mens,  gen.  men¬ tis,  ‘mind’.  Sec  mental,  'pertaining  to  the  mind', comment,  intr.  v.  F.  commenter,  fr.  L.  com- mentdrl,  ‘to  consider  thoroughly,  meditate  upon, explain’,  freq.  formed  fr.  comminiscor.  See prcc.  word.  Derivative:  comment-or,  n. commentary,  n.  —  L.  commentdrium,  ‘notebook, sketch,  commentary’  (short  for  volumen  eom- mentdrium,  ‘a  commenting  book’),  neut.  of  the
8365:commentation,  n.  —  L.  commentdtio,  gen.  -onis, ‘meditation  upon  something,  treatise,  disser¬ tation’,  fr.  commentatus,  pp.  of  commentari.  See
8366:comment,  v.,  and  -ation.
8367:commentator,  n.  —  L.,  ‘inventor,  contriver,  inter¬ preter’,  fr.  commentatus,  pp.  of  commentari.  See comment,  v.,  and  -ator.
22804:maniac,  adj.,  pertaining  to  mania;  insane;  n., madman.  —  ML.  maniacus  (whence  also  F. maniaque),  fr.  L.  mania,  fr.  Gk.  uavt a.  See
22820:manikin,  n.,  1)  a  little  man;  a  dwarf;  2)  a  model of  the  human  body;  3)  a  mannequin.  —  Du. manneken,  ‘little  man’,  dimin.  of  man,  ‘man’.
22829:mannequin,  n.,  1)  a  model  of  the  human  body ,  2) a  woman  employed  to  display  clothes  by wearing  them.  —  F.,  fr.  Du.  manneken,  little man’.  See  manikin.
23500:mention,  n.  —  ME.  mencioun,  fr.  OF  (-  r.) mention,  fr.  L.  mentidnem,  acc.  of  mentio,  a speaking  of,  a  calling  to  mind’,  fr.  mens,  gem mentis.  See  mental,  ‘pertaining  to  the  mind’,  and
23502:mention,  tr.  v.  —  F.  mentionner,  fr.  mention.  See
23503:mention,  n.
24257:monitor,  n.,  one  who  reminds.  —  L.,  fr.  monitus.
24260:monitory,  adj.,  warning.  —  L.  monitorius,  fr.  mo¬ nitus,  pp.  of  monere.  See  monition  and  adj.  suff. -ory.
24346:monster,  n.  —  ME.  monstre,  fr.  OF.  (=  F.) monstre,  fr.  L.  monstrum,  ‘an  evil  omen,  por¬ tent,  monster’,  for  *mone-strom,  lit.  ‘that  which serves  as  a  warning’,  fr.  monere,  ‘to  remind, warn,  advise,  instruct’.  L.  monstrare,  ‘to  show, point  out,  indicate’,  is  a  derivative  of  monstrum. See  monition  and  cp.  monstrance,  monstrous, demonstrate,  premonstrate,  remonstrate.  Cp.  also muster.
24359:monument,  n.  —  ME.  moniment,  fr.  L.  monumen- tum,  monimentum ,  ‘monument",  lit.  ‘that  which reminds",  fr.  monere,  ‘to  call  to  mind,  remind, advise,  warn’.  See  monition  and  -ment. monumental,  adj.  —  L.  monumentalis,  ‘pertaining to  a  monument',  fr.  monttmentum;  first  used  by Shakespeare.  See  monument  and  adj.  suff.  -al. Derivatives:  monumental-ize,  tr.  v.,  monumen- tal-iz-ation,  n.,  monumental-ly,  adv.
24733:muse,  intr.  v.,  to  reflect.  —  ME.  musen,  fr.  OF. (=  F.)  muser,  ‘to  loiter,  dream,  ponder  deeply’, prop,  ‘to  snuff  about’  (said  of  a  dog),  fr.  ML. musum,  ‘muzzle’,  whence  also  It.  muso,  OProv¬ eng.  mus,  and  the  OF.  dimin.  museKF.  museau), whence  E.  muzzle  (q.v.)  Cp.  amuse  and  musette. Derivatives :  muse,  n.,  meditation,  muse-ful,  adj., muse-ful-ly,  adv.,  muse-less,  adj.,  muse-less-ly, adv.,  mus-ing,  n.  and  adj.,  mus-ing-ly,  adv. Muse,  n.,  one  of  the  nine  goddessess,  daughters of  Zeus  and  Mnemosyne,  protectors  of  the  arts ( Greek  mythol.)  —  ME.,  fr.  OF.  (=  F.),  fr.  L. Musa,  fr.  Gk.  Molina,  pouaa,  ‘Muse;  music, song’,  which  stands  peril,  for  *M6vlha  and  is rel.  to  pavOavciv,  ‘to  learn’.  See  mathematical and  cp.  amusia,  mosaic,  museum,  music, musette,  n.,  1)  a  small  bagpipe;  2)  a  composition for  this  instrument.  —  F.,  fr.  MF.,  fr.  OF.,  fr. muser,  ‘to  play  the  bagpipe’,  fr.  OF.  mor, ‘mouth, muzzle’,  fr.  ML.  musum,  of  s.m.  See  muzzle  and -ette  and  cp.  muse.  Cp.  also  cornmuse. museum,  n.  —  L.  museum,  ‘library,  academy, study,  museum’,  fr.  Gk.  pouaeiov,  lit.  ‘seat  of the  Muses’,  fr.  MoOera,  ‘Muse’.  See  Muse, mush,  n.,  1)  a  thick  soft  mass;  2)  a  porridge  (U.S.)
```


## [2026-09-07T16:14:46.480Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport sys\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\ndef leaf_of(n):\n    off=sum(len(l)+1 for l in lines[:n-1])\n    return d[:off].count('\\f')\nfor n in (720,22804,22820,22829,23500,24257,24346,24359,24733,8363):\n    print(n, 'leaf', leaf_of(n), 'est p', (leaf_of(n)-12)*2)\nEOF",
 "description": "Map Klein lines to leaves"
}
```


### [2026-09-07T16:14:48.057Z] TOOL RESULT

```
720 leaf 10 est p -4
22804 leaf 501 est p 978
22820 leaf 501 est p 978
22829 leaf 502 est p 980
23500 leaf 517 est p 1010
24257 leaf 534 est p 1044
24346 leaf 536 est p 1048
24359 leaf 537 est p 1050
24733 leaf 545 est p 1066
8363 leaf 179 est p 334
```


## [2026-09-07T16:14:54.987Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==546' KLN_1966.txt | grep -nE '^[0-9]{3,4}$|^ *[0-9]{3,4} *$' ; echo \"--- head/tail leaf 546\"; awk 'BEGIN{RS=\"\\f\"} NR==546' KLN_1966.txt | head -3; echo \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==546' KLN_1966.txt | tail -3",
 "description": "Find page numbers in Klein leaf 545"
}
```


### [2026-09-07T16:14:56.419Z] TOOL RESULT

```
--- head/tail leaf 546
urrain’,  which  also  derive  fr. VL.  *morire.  Cp.  murrina. murre,  n.,  1)  guillemot  of  the  genus  Uria;  2)  the razorbill  —  Related  to  dial.  E.  marrot,  morrot, ‘guillemot’;  of  uncertain  origin.  Cp.  next  word, murrelet,  n.,  any  of  various  birds  of  the  auk family.  —  Formed  fr.  murre  with  dimin.  suff. -let.
murrey,  adj.,  mulberry  red;  dark  purplish  red;  n., murrey  color.  —  ME.,  fr.  MF.  moree,  fr.  ML. moratus,  ‘mulberry  colored’,  fr.  L.  morum, ‘mulberry’.  See  mulberry, murrhine,  adj.,  made  of,  or  resembling,  murra;  n., a  murrhine  vase  ( Roman  antiq.).  —  L.  murr(h)i- nus,  ‘of,  or  made  of,  murra’,  fr.  murra,  less  cor¬ rectly  murrha,  ‘fluorspar;  agate;  a  glass  imita¬ tion’,  which  is  of  Iranian  origin.  Cp.  Pers.  mori, muri,  ‘globule  of  glass'.  Cp.  also  Gk.  pippta, fj.ouppi.va  (pi.),  which  are  of  the  same  origin  and meaning  as  L.  murra.
murrina,  n.,  a  disease  of  horses  (vet er.)  —  Sp. morriha,  ‘murrain’.  See  murrain.
...
mussel,  n.,  any  of  several  bivalve  mollusks.  — ME.  muscle,  fr.  OE.  muscelle,  muscle,  fr.  VL. *muscula  [whence  also  OF.  musle  (F.  moule), OS.,  OHG.  muscula  (MHG.,  G.  muschel), ‘mussel’],  corresponding  to  L.  musculus,  ‘little mouse,  muscle;  sea  mussel’.  See  muscle. Derivatives:  mussel-ed ,  adj.,  mussel-er,  n. mussuck,  mussuk,  n.,  a  leathern  skin  for  water (India)  —  Hind,  masak,  fr.  OI.  masakah. Mussulman,  n.,  a  Moslem.  —  Turk,  musulman, fr.  Pers.  musulman,  which  is  formed  with  the adj.  suff.  -an  fr.  Arab,  muslim,  ‘Moslem’.  See Moslem.
must,  aux.  v.,  am  (or  is,  are)  obliged  to.  —  ME. moste,  fr.  OE.  moste,  pret.  of  motan,  ‘to  be allowed  to,  be  able  to,  have  opportunity  to, have  to’,  rel.  to  OS.  motan,  ‘to  be  obliged  to, have  to’,  OFris.  mdta,  MLG.  moten,  MDu.,  Du. moeten,  ‘to  be  obliged  to’, OHG.  muo^an,  MHG. mue^en,  ‘to  be  allowed  to,  have  to’,  G.  miissen,
‘to  be  obliged  to’,  Goth,  gamotan,  ‘to  have room  to,  be  able  to’,  fr.  Teut.  base  *  motan,  ‘to fix,  allot,
```


## [2026-09-07T16:15:09.648Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^man,  n\\.\\|^man,  n\\|manniz\\|^Norman,\\|manniska\" KLN_1966.txt | head -10",
 "description": "Find Klein man entry"
}
```


### [2026-09-07T16:15:09.704Z] TOOL RESULT

```
17305:Hausmannize,  tr.  and  intr.  v.,  to  reconstruct  a city  by  straightening  and  widening  its  streets.  — Prop,  ‘to  follow  the  example  of  Baron  Georges- Eugene  Haussmann  (1809-91),  who  was  prefect of  Paris  belween  1853  and  1870  and  during  this period  much  contributed  to  its  beautification. For  the  ending  see  suff.  -ize. hausse-col,  n.(  a  piece  of  armor.  —  F.,  ‘neck
22737:man,  G.  Mann,  ON.  madr  (for  *mannr),  Dan. mand,  Goth,  manna,  ‘man’  (cp.  Mannas,  a  tribal deity,  in  Tacitus’  Germania,  chapt.  2),  OS.  men- nisco,  OFris.  manniska,  MDu.  mensche,  Du. mens,  OHG.  mannisco,  mennisco,  MHG.  men¬ sche,  mensch,  G.  Mensch,  ‘man’  (orig.  adj. meaning  ‘human’),  and  cogn.  with  OI.  manuh, ‘man;  progenitor  of  mankind’,  Avestic  manu-, ‘man’,  OSlav.  mgSi,  ‘man’.  All  these  words  prob. meant  orig.  ‘one  who  thinks’,  fr.  I.-E.  base *men-,  ‘to  think’,  whence  also  OI.  matih,  matih, ‘thought’,  L.  mens,  gen.  mentis,  ‘mind’,  Goth. muns,  ‘thought’,  munan ,  ‘to  think',  ON.  minni, ‘mind’,  OE.  gemynd,  ‘memory’.  See  mind  and cp.  Manu,  muzhik,  and  the  second  element  in Marcomanni.  Cp.  also  minx.
25614:Norman,  n.,  1)  one  of  the  Northmen  who  occu¬ pied  Normandy  in  the  10th  cent.;  2)  one  of  the Norman  French  who  conquered  England  in 1066;  3)  a  native  of  Normandy.  —  OF.  Nor- mant,  F.  Normand,  lit.  ‘Northman’.  See  North¬ man.
```


## [2026-09-07T16:15:19.992Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n=NR; if (match($0,/(^|\\n)[ ]*[0-9]{3,4}[ ]*(\\n|$)/)) {s=substr($0,RSTART,RLENGTH); gsub(/[^0-9]/,\"\",s); print n, s}}' KLN_1966.txt | sed -n '1,5p;100,120p;240,260p'\necho \"=== total leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt",
 "description": "Extract page numbers from Klein OCR leaves"
}
```


### [2026-09-07T16:15:21.202Z] TOOL RESULT

```
65 100
66 102
67 104
68 106
69 108
190 340
191 341
193 340
194 348
195 350
196 351
198 357
199 358
200 360
202 362
203 364
207 373
208 374
209 376
210 378
211 380
212 382
213 385
214 386
215 386
216 389
368 681
369 682
371 686
372 688
373 690
374 693
375 694
376 696
377 698
378 700
379 702
380 704
381 706
382 707
383 709
384 711
385 713
386 715
387 716
388 718
389 720
=== total leaves
903
```


## [2026-09-07T16:15:31.756Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 506 507 508; do echo \"##### NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -4; done",
 "description": "Inspect Klein leaves near p.947"
}
```


### [2026-09-07T16:15:33.043Z] TOOL RESULT

```
##### NR=506
—  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’, which  is  of  uncertain  etymology.  It  possibly stands  for  *mari-tos  and  lit.  means  ‘provided with  a  young  wife’,  and  is  cogn.  with  OI. mdryah,  ‘young  man,  lover,  wooer’,  Gk.  p.eipaE, ‘boy,  girl’,  Lith.  marti,  ‘bride’,  Opruss.  martin (acc.),  ‘bride’,  Lith.  rnerga,  OPruss.  mergo,  ‘girl, maid,  servant’,  W.  merch,  Co.  myrgh,  ‘daughter; wife’,  W.  morwyn,  ‘virgin,  girl’.  Cp  marry. Derivatives:  marital-ity,  n.,  marital-ly,  adv. maritime,  adj.,  of,  or  pertaining  to,  the  sea.  —  F., fr.  L.  marilimus,  ‘of  the  sea,  near  the  sea’,  fr. mare,  sea'.  See  mare,  ‘sea’.  Suff.  -timus  in  mari- timus  (also  -tnmus)  is  prop,  a  superl.  suff.,  and occurs  also  in  L.  in-timus,  ‘inmost ,  ul-timus, ‘last’,  pos-tumus,  ‘last’  (see  intimate,  ultimate, posthumous).
Marius,  masc.  PN.  —  L.,  fr.  Marius,  name  of  a Roman  gens.
marjoram,  n.,  name  of  a  plant.  —  ME.  majoran, fr.  OF.  majorane  (F.  marjolaine),  tr.  ML.  majo- rana,  fr.  L.  amaracus,  fr.  Gk.  apapaxo;,  ‘mar¬ joram’,  which,  together  with  Macedonian  Gk. afixpu,  ’marjoram',  prob.  derives  from  a  lan¬ guage  of  India.  Cp.  OI.  maruvah,  maruvakah, ‘marjoram’. ML.  majorana  (fr.  L.  amaracus)  owes its  form  to  a  confusion  with  L.  major,  contpar. of  magmis,  ‘great,  large’  (see  major,  adj.) Marjorie,  Marjory,  fern.  PN.  —  Collateral  forms of  Margery  (q.v.)
mark,  n.,  1)  boundary  (archaic);  2)  sign.  —  ME. merke,  marke,  fr.  OE.  mearc,  ‘boundary, bound¬ ary  sign,  sign,  mark’,  rel.  to  ON.  merki,  mark, 'boundary  sign’,  mork,  ‘forest’  (forests  often served  as  frontiers),  OFris.  merke,  OS.,  Goth. marka,  ‘boundary,  frontier’,  Du.  merk,  ‘mark, brand’,  mark,  ‘borderland;  mark,  sign’,  OHG. marcha,  MHG.  marke,  G.  Mark,  ‘boundary, boundary  land',G.  Marke,  ‘sign,  token ;  stamp  , and  cogn.  with  Avestic  marlza,  ‘border’,  L. margo,  gen.  marginis,  ‘edge,  brink,  border  ,  OIr. mruig,  h.  bruig,  ‘boundary;  district’,  W„  Co., Bret,  bro,  ‘district’.  Cp.  mark,  ‘to  put  a  mark on’,  mark,  a  weight.  Cp.  also  march,  ‘bounda¬ ry’,  Marcomauni,  margrave,  marque,  marquetry, marquis,  marquise,  countermark,  demarcation, remark.  Cp.  also  margin.  Cp.  also  Cymric, mark,  tr.  v.,  to  put  a  mark  on.  —  ME.  merken, ntnrken.  fr.  OE.  mearcian ,  ‘to  make  a  mark,  to
##### NR=507
 See  marital  and  marriage.
Derivatives:  marri-ed,  adj.,  marri-er,  n.
Mars,  n.,  the  Roman  god  of  war.  —  L.  Mars,  of unknown  etymology.  Cp.  March,  Marcia, Marcus,  Mark,  Martin,  martin,  martite.  Gk., (xApvotiiai,  '1  fight’,  is  not  cognate  with  L. Mars  (see  marasmus).
Marsala,  n.,  a  kind  of  wine  produced  in  Sicily.  — So  called  from  Marsala,  a  seaport  in  Sicily,  fr. Arab,  Mirsa-llahi,  lit.  'the  Port  of  God’. Marseillaise,  n.,  name  of  the  French  national Republican  song,  composed  by  Rouget  de  Lisle in  1792.  —  F.,  fern,  of  the  adj.  Marseillais,  ‘of Marseilles’.  Rouget  de  Lisle  composed  this song  for  the  Strassburg  volunteers,  yet  it  was named  Marseillaise  because  it  was  the  volun¬ teers  from  Marseilles  who  sang  it  in  Paris  for the  first  time.
##### NR=508
—  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.  maschera,  fr.  Arab.  maskharah,  ‘mockery; buffoon’,  fr.  sdkhira,  ‘he  mocked,  ridiculed’. Cp.  masque,  masquerade.
Derivatives :  mask,  tr.  and  intr.  v.,  musk-ed,  adj., mask-er,  n.,  mask-ette,  n.
maskery,  masquery,  n.  —  F.  masquerie,  fr.  mas¬ quer,  ‘to  mask’,  fr.  masque.  See  mask  and  -ery. maskelynite,  n.,  a  feldspar  mineral  (mineral.)  — Named  after  the  English  mineralogist  Nevil Slory -Maskelyne  (1823-1911).  For  the  ending see  subst.  suff.  -ite. maskinonge,  n.  —  See  muskellunge. maslin,  n.,  a  kind  of  brass  (obsol.)  —  ME.,  fr. OE.  meestling,  m  testing,  mseslin,  rel.  to  MDu., M  HG.  messinc,  missinc,  Du.  messing,  G.  Mes¬ sing,  ‘brass’.  These  Teut.  words,  as  well  as Czech  mosaz,  Slovak  mosadz,  Pol.  mosiqdz, ‘brass’,  ult.  derive  fr.  Gk.  Moaouvoixoi;  yeOutiq, ‘brass  made  by  the  Mossynoikoi’,  a  people  liv¬ ing  south  of  the  Euxine,  lit.  ‘those  dwelling  in (zoaouvec  (i.e.  wooden  houses)’.  Brass  is  said to  have  been  first  manufactured  by  the  Mossy¬ noikoi,  whence  the  name  Moaouvotxo?  yotXxoq. maslin,  n.,  a  mixture  of  different  kinds  of  grain. —  ME.  mastlyoun,  mestlyon,  fr.  OF.  mesteillon, mestillon,  fr.  mestueil,  mesteil  (F.  mdteil),  fr. VL.  *mistilium,  which  was  formed  from  the adjective  *mistilis,  fr.  *mistus,  a  collateral  form of  L.  mixtus,  pp.  of  miscere,  ’to  mix’.  See  mix. masochism,  n.,  a  form  of  sexual  perversion  in which  one  finds  pleasure  in  being  hurt  ( med.); the  opposite  of  sadism.  —  Named  after  the Austrian  novelist  Leopold  Sacher  Masoch (1836-95),  who  describes  it  in  one  of  his  works. For  the  ending  see  suff.  -ism. masochist,  n.  —  See  prec.  word  and  -ist.
Derivative:  masocHTst-ic,  adj. mason,  n.  —  ME.,  fr.  OF.  (=  F.)  mafon,  fr. Frankish  *makjo,  Latinized  into  machid,  from the  verb  *makan ,  ‘to  make’.  See  make  and  cp. freemason.
```


## [2026-09-07T16:15:42.543Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=485 && NR<=560 {n=NR; if (match($0,/(^|\\n)[ ]*[0-9]{3,4}[ ]*(\\n|$)/)) {s=substr($0,RSTART,RLENGTH); gsub(/[^0-9]/,\"\",s); print n, s}}' KLN_1966.txt",
 "description": "Calibrate Klein page numbers near leaf 500"
}
```


### [2026-09-07T16:15:43.757Z] TOOL RESULT

```
485 900
486 902
487 904
488 905
489 907
490 909
491 910
492 912
493 914
494 919
496 921
497 923
498 925
499 927
500 929
501 930
502 932
503 935
504 937
506 940
507 942
508 946
510 948
511 950
512 953
514 957
515 958
519 966
520 968
521 970
522 972
523 974
524 976
525 977
526 979
530 986
531 988
532 990
533 992
534 994
536 998
```


## [2026-09-07T16:15:59.342Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 509 510; do echo \"##### NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | tr '\\f' '\\n' | head -80; done",
 "description": "Print Klein leaves 509-510"
}
```


### [2026-09-07T16:16:00.598Z] TOOL RESULT

```
##### NR=509
nis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of masticare.  See  masticate  and  -ion. mastiff,  n.  —  ME.  mastif,  fr.  OF.  muslin  (whence F.  matin),  fr.  VL.  *md(n)suetinus,  ‘tamed’,  fr. L.  mansuetus,  of  s.m.,  pp.  of  mansuescere,  ‘to tame’ ;  see  mansuete.  The  ending  of  E.  mastiff  is due  to  a  confusion  with  OF.  mestif,  ‘mongrel’, mastitis,  n.,  inflammation  of  a  breast  ( med .)  — Medical  L.,  coined  by  Konig  fr.  Gk.  aaoxo;, "breast’,  and  suff.  -tTiq.  See  masto-  and  -itis. masto-,  before  a  vowel  mast-,  combining  form meaning  ‘breast’.  — -  Gk.  p.a paaT-,  fr. [x'/.n-ric,  ‘breast’,  which  prob.  stands  for  *trccS- toi;  and  derives  from  the  stem  of  paSav,  ‘to  be wet,  to  flow’,  fr.  I.-E.  base  *mad-,  ‘wet,  moist, dripping’.  See  mast,  ‘fruit  of  the  beech’,  and  cp. prec.  word,  mastoid,  mazo-,  ‘breast’,  amastia, bimastism.
mastodon,  n.,  an  extinct  elephantlike  mammal.  — ModL.,  compounded  of  mast-  and  Gk  68c ov, gen.  oSovtoc,  ‘tooth’  (see  odonto-);  so  called from  the  nipple-shaped  projections  on  the  mo¬ lar  teeth.
mastodontic,  adj.,  pertaining  to,  or  resembling,  a mastodon.  —  See  prec.  word  and  -ic. mastoid,  adj.,  resembling  a  breast  or  nipple.  — Gk.  paaTOEiS-r)!;,  compounded  of  paaro;, ‘breast’,  and  -oeiSt)!;,  ‘like’,  fr.  eT8oc,  ‘form, shape’ .  See  masto-  and  -oid.
Derivative:  mastoid,  n.,  the  mastoid  process  or bone.
masturbate,  intr.  v.,  to  practice  onanism.  —  L. masturbdtus,  pp.  of  masturbdri,  ‘to  masturbate’, prob.  from  *man-stuprdre,  for  manu  stuprare, ‘to  defile  oneself  with  the  hand’,  fr.  manu,  abl. of  manus,  ‘hand’,  and  stuprare,  ‘to  defile  one¬ self’,  fr.  stuprum,  ‘defilement,  dishonor,  dis¬ grace'.  See  manual,  stuprum,  and  verbal  suff. -ate.  The  ending  of  L.  mdsturbdri  is  due  to  a popular  connection  of  the  word  with  L.  turbare, ’to  disturb,  agitate,  confuse’.  See  Walde-Hof- mann,  LEW.,  II,  48  s.v.  mdsturbor.
Derivatives',  masturbat-ic,  adj.,  masturbat-ion, n.,  masturbat-ion-al,  adj.,  masturbat-or,  n,, masturbat-ory,  adj.
masurium,  n.,  name  of  a  chemical  element;  now called  technetium  ( chem .)  —  ModL.,  named  by its  discoverers,  the  German  chemists  Walter Noddack,  Ida  Tacke  and  Otto  Berg,  after  Masu¬ ria,  a  district  in  East  Prussia;  so  called  by  them, because  the  platinum  ore,  from  which  it  was first  extracted,  occurs  frequently  in  this  district.
mat,  n.,  a  coarse  fabric  made  of  straw,  hemp, rushes,  etc.  —  ME.  matte,  fr.  OE.  matt,  fr.  Late L.  matta,  ‘mat  made  of  rushes’  (whence  also OHG.  matta,  MHG.,  G.  matte),  fr.  Phoem- Punic  matta,  corresponding  to  Heb.  mitta  , ‘bed’,  which  is  formed  from  the  stem  of  natd  , ‘he  bent’  (for  sense  development  cp.  Gk.  xXfvr„ ‘bed’,  fr.  xXtvEtv,  ‘to  bend’).  From  Late  L. natta,  a  secondary  form  of  Late  L.  matta,  which occurs  in  the  writings  of  Gregoire  de  Tours,  de¬ rives  F.  natte,  ‘mat,  matting’.  For  the  change of  Heb.-Punic  initial  m  to  n  cp.  F.  nappe, ‘tablecloth’,  fr.  L.  nappa,  which  derives  fr.  Heb.- Punic  mappdh  (see  napery,  napkin).
Derivatives:  mat,  tr.  v.,  to  cover  with  a  mat  or mats,  matt-ed,  adj.,  matt-ed-ly,  adv.,  matt-ed- ness,  n.,  matting  (q.v.)
mat,  adj.,  dull  (said  of  color  or  a  surface).  —  F., ‘dull,  lusterless,  unpolished’,  fr.  OF.  mat,  ‘de¬ feated,  afflicted,  depressed,  dejected;  dull’,  fr. Arab,  mat  in  the  sentence  mat  ash-shah,  ‘the king  has  died’.  The  word  mat,  orig.  used  only as  a  term  of  chess,  gradually  developed  also  the meanings  ‘faint,  feeble,  dull-colored .  See checkmate  and  cp.  matador,  mate,  adj. matador,  n.,  1)  the  man  who  kills  the  bull  in  the bullfight ;  2)  one  of  the  three  chief  cards  in  the game  of  ombre  and  quadrille.  —  Sp,,  ‘killer, murderer’,  fr.  matar,  ‘to  kill,  murder’,  fr.  Arab. mdta,  ‘he  died’.  Cp.  checkmate.  Cp.  also  mat, ‘dull’.
matamata,  n.,  a  freshwater  turtle,  Chelys  fim- briata.  —  Port,  matamata,  fr.  Tupi  matamatd. match,  n.,  an  equal. — ME  .macche,  fr.  OE.  nuecca, ge-mtecca,  ‘one  suited  to  another,  one  of  a  pair, mate’,  fr.  mac-ian,  ‘to  make’.  Cp.  OHG.  gi- mah  (n.),  ‘comfort,  advantage',  MHG.  ge- mach,  ‘comfort,  ease’,  OHG.  gi-mah  (adj.), ‘suitable,  comfortable’,  MHG.  ge-mach,  ‘com¬ fortable,  quiet’,  G.  ge-mach,  ‘easy,  leisurely’, and  see  make,  v.  For  formation  cp.  batch,  fr. bake.
Derivatives:  match,  tr.  and  intr.  v.,  match-less, adj.,  match-less-ly,  adv.,  match-less-ness,  n. match,  n.,  1)  wick  or  cord  for  firing  a  gun;  2)  a slender  piece  of  wood  tipped  with  a  substance that  catches  fire  by  friction.  —  ME.  macche,  fr. OF.  mesche  (F.  meche),  ‘wick’  (of  a  candle,  lamp, etc.),  match,  fuse’,  fr.  VL.  *micca,  which  is  a blend  of  L.  myxa  (fr.  Gk.  (zu£a),  ‘wick  of  a lamp’,  and  L.  mucus ,  ‘slime  from  the  nose  . See  myco-,  mucus.
Derivative:  match,  tr.  v. matchet,  n.  —  A  var.  of  machete, mate,  tr.  v.,  to  checkmate;  to  overcome.  —  ME. maten,  fr.  OF.  mater,  ‘to  checkmate;  to  defeat, overcome’,  fr.  mat,  ‘checkmated ;  defeated,  over¬ come’.  See  cp.  mat,  ‘dull’.
mate,  n.,  checkmate.  —  ME.  mat,  fr.  MF.,  fr.  OF. See  prec.  word.
mate,  n.,  a  companion.  —  ME.,  fr.  MLG.  mate, mat,  ‘companion’,  orig.  ‘a  messmate’,  whence
also  Du.  maat;  cp.  Dan.,  Swed.  mat,  OHG. gimazzo,  MHG.  gema33e,  ‘messmate’,  G.  Maat, ‘mate’;  fr.  Teut.  base  *mati-,  ‘food’,  whence also  E.  meat  (q.v.)  See  also  matelote.
Derivatives:  mate,  tr.  and  intr.  v.,  mate-less,  adj. mate,  n„  1)  Paraguay  tea;  2)  the  plant  from  which it  is  made.  —  Sp.  mate,  fr.  Quichua  mati,  prop, ‘calabash,  a  vessel  made  of  calabash’,  hence also  ‘a  vessel  in  which  mate  is  made’, matelasse,  adi.,  woven  in  a  manner  suggestive  of quilting.  —  F.,  pp.  of  matelasser,  ‘to  stuff,  pad, cushion’,  fr.  matelas,  ‘mattress,  pad,  cushion’. See  mattress.
matelasse,  n.,  a  matelasse  fabric.  —  Fr.  prec. word.
matelote,  n.,  a  dish  of  fish.  —  F.,  fr.  matelot. ‘sailor’,  fr.  MF.  matenot,  a  loan  word  fr.  MDu, mattenoot,  which  is  rel.  to  ON.  motunautr, MHG.  masgenoje,  lit.  ‘messmate’.  For  the  first element  in  these  words  see  mate,  ‘companion’. The  second  element  is  rel.  to  ON.  nautr,  OE. geneat,  OS.  ginot,  OFris.  nat,  OHG.  gino3, gind30,  MHG.  gend3,  G.  Genosse,  ‘mate,  com¬ panion’.  These  words  orig.  meant  ‘one  who shares  cattle  with  others’.  They  are  rel.  to  ON.
/ mm,  OE.  neat,  ‘ox,  cattle’;  see  neat,  n.  Cp. matross.
mater,  n.  1)  mother  ( colloq .);  2)  either  of  the  two membranes  of  the  brain  ( pia  mater  and  dura mater).  — -  L.  mater,  ‘mother’.  See  mother, materfamilias,  n„  the  mother  of  a  family.  —  L. mater  familias,  compounded  of  mater,  ‘mother’, and  familias,  ancient  gen.  of  familia,  ‘family’. See  mater  and  family  and  cp.  paterfamilias, material,  adj.  —  ME.,  fr.  Late  L.  mdterialis,  ‘of matter’,  fr.  L.  materia,  ‘wood,  timber,  stuff, matter’.  See  matter  and  cp.  materiel. Derivatives:  material,  n.,  material-ism,  n.,  ma- terial-ist,  n.,  material-ist-ic,  adj.,  material-ist-ic- al-Iy,  adv.,  material-ity,  n.,  material-ize,  tr.  and intr.  v.,  material-iz-ation,  n.,  material-ly,  adv., material-ness,  n.
materia  medica,  1)  substances  used  in  medicine; 2)  that  branch  of  medicine  which  deals  with  the properties  of  drugs  and  with  their  application in  the  cure  of  diseases.  - —  Med.  L.,  lit.  ‘medical matter’.  See  matter  and  medical, materiel,  n.,  material  equipment.  —  F.,  from  the adj.  materiel,  ‘material,  physical',  fr.  Late  L. mdterialis.  See  material.
maternal,  adj.  —  ME.,  fr.  MF.  (=  F.)  maternel, fr.  L,  mdternus,  ‘of  a  mother’,  fr.  mater.  See mother  and  adj.  suff.  -al.
Derivatives:  maternal-ity,  n.,  maternal-ly,  adv., maternal-ness,  n.
maternity,  n.,  motherhood.  —  F.  maternite,  fr. MF.,  fr.  L.  maternitatem,  acc.  of  mdternitas, ‘motherhood’,  fr.  mdternus.  See  prec.  word  and -ity.
matey,  adj.,  friendly  ( British  colloq.)  —  Formed with  suff.  -y  fr.  mate,  ‘companion’, math,  n.,  a  mowing.  —  ME.  *math,  fr.  OE.  map.
‘harvest,  crop',  rel.  to  OFris.  meth,  OHG.  mad, MHG.  mat ,  G.  Mahd,  ‘a  mowing’,  fr.  Teut. *mapa-,  lit.  ‘that  which  is  wown’,  pp.  form  of I.-E.  base  *me-,  *mi-,  ‘to  mow’.  See  mow,  ‘to cut  (grass)’,  and  cp.  aftermath.  Cp.  also  meadow, mathematic,  adj.,  mathematical  (now  rare).  — See  next  word.
mathematical,  adj.  —  Formed  with  adj.  suff.  -al fr.  F.mathematique,  fr.  Gk.  'J.y.dTyiy.ziy.yi.  ‘scien¬ tific,  mathematical’,  fr.  ‘that  which  is
learned,  learning,  science’,  from  the  aorist p,a&£tv  (whence  the  pres,  [iavffaveiv ),  ‘to  learn’, fr.  *mndh-,  reduced  form  of  I.-E.  base  *men-dh-, ‘to  have  one’s  mind  aroused,  apply  oneself to’.  From  the  same  base  (resp.  its  reduced  form) prob.  derive  Gk.  p.Ev(H)p7],  ‘care’,  Lith.  man- dr  as,  mandrils,  ‘wide-awake’,  OSlav.  mqdru, ‘wise,  sage’,  Goth,  mundon  sis,  ‘to  look  at’,  ON. munda,  ‘to  aim’,  OHG.  mendan,  ‘to  rejoice , OHG.  muntar,  MHG.  munter,  munder,  ‘eager, agile,  nimble",  G.  munter,  ‘awake,  lively,  gay, merry,  vigorous’,  W.  mynnu ,  ‘to  want,  wish  , Alb.  mund,  ‘I  can,  I  am,  victorious’,  and  pos¬ sibly  also  Ol.  medha,  ‘wisdom,  intelligence',  Gk. Mouaot  (if  fr.  *M6vffia),  ‘Muse’.  Base  *men-dh- is  an  enlargement  of  base  *men-,  ‘to  think’. See  mind  and  cp.  Muse,  Epimetheus,  Prome¬ theus.  Cp.  also  the  second  element  in  chresto- mathy,  opsimath,  polymath.  Cp.  also  the  second element  in  Ormazd.
Derivative:  mathematical-ly,  adv. mathematician,  n.  —  F.  mathematicien,  fr.  mathe- matique.  See  prec.  word  and  -ian. mathematico-,  combining  form  meaning  ‘mathe¬ matical  and’.  —  See  next  word, mathematics, n.  —  F.mathematique,  fr.  L.  mathe- matica,  fr.  Gk.  (scil.  te'/v/]),
‘mathematical  art’,  fern,  of  p.aff'rjp.a-n.xoi;, ‘scientific,  mathematical’.  See  mathematical  and -ics.
mathematize,  tr.  and  intr.  v.  —  See  prec.  word and  -ize.
Mathilda,  fern.  PN.  —  See  Matilda, matico,  n.,  1)  a  Peruvian  shrub ;  2)  a  styptic  made from  its  leaves.  —  Sp.,  fr.  Matico,  dimin.  of Mateo,  ‘Matthew’.  See  Matthew.
Matilda,  Mathilda,  fern.  PN.  —  F.  Mathilde,  of Teut.  origin  and  lit.  meaning  ‘mighty  in  battle’. Cp.  OHG.  Mahthilda,  compounded  of  mahti, ‘might,  power',  and  hildi,  ‘battle’.  For  the  first element  see  might,  for  the  second  cp.  Hilda  and words  there  referred  to.  Cp.  Maud, matildite,  n.,  a  silver  bismuth  sulfide  (mineral.)  — Named  after  Matilda  mine,  near  Morococha, Peru.  For  the  ending  see  subst.  suff.  -ite. matin,  n.,  1)  morning  song  esp.  of  birds;  2)  (pi.) the  first  of  the  seven  canonical  hours;  3)  (pi.) morning  service  of  the  Church  of  England.  — F.,  ‘morning’,  fr.  L.  matutlnum  (short  for  md- tutinum  tempos,  ‘morning  time'),  neut.  of  mdtii- tinus,  ‘of  the  morning’  See  matutinal  and  cp. matinee.
matinee
maund
Derivatives:  matin,  adj.,  matin-al,  adj. matinee,  n.,  afternoon  performance.  —  F.  mati¬ nee,  fr.  matin.  See  matin, matiockite,  n.,  lead  oxychloride  {mineral.)  — Named  after  Matlock  in  Derbyshire,  England. For  the  ending  see  subst.  suff.  -ite. matra,  n.,  an  Indian  unit  of  measure.  OI. mdtram  (neut.),  matra  (fern.),  measure ,  fr. mati  (fr.  I.-E.  *me-ti),  ‘measures’,  fr.  I.-E.  base *me-,  ‘t
##### NR=510
o  measure’.  See  meter,  ‘poetical  rhythm’, and  cp.  words  there  referred  to. matranee,  n.,  a  female  sweeper;  a  female  servant (India).  —  Flind.  mehtardnd,  mehtrani,  fr.  Pers. mihtarani,  ‘female  sweeper’,  fem.  of  mihtar, ‘sweeper’.  See  mehtar.
matrass,  n.,  a  glass  vessel  with  a  long  neck.  —  F. matras,  prob.  fr.  Arab.  mdtarah,  ‘leathern  bottle, skin,  vase’.
matri-,  combining  form  meaning  ‘mother  .  L. main-,  from  the  stem  of  mater,  gen.  mdtris, ‘mother’.  See  mater.
matriarch,  n.,  a  mother  who  rules  her  family  or tribe.  —  Formed  fr.  matri-  on  analogy  of  patri¬ arch  (q.v.)
Derivatives:  matriarch-al,  adj.,  matriarch-ate, n.,  matriarch-ic,  adj.,  matriarch-y,  n.
Matricaria,  n.,  a  genus  of  plants,  the  wild  camo¬ mile  (hot.)  —  ModL.,  fr.  L.  matrix,  ‘womb’  (see matrix) ;  so  called  for  the  reputed  medicinal  val¬ ue.  For  the  ending  see  suff.  -ia. matricidal,  adj.  —  See  next  word  and  adj.  suff.  -al. matricide,  n.,  one  who  kills  his  mother.  L.  ma- tricida,  compounded  of  matri-  and  - clda ,  killer  , fr.  caedere,  ‘to  kill’.  See  -cide,  ‘killer  . matricide,  n.,  the  act  of  killing  one’s  own  mother. —  L.  matricidium,  compounded  of  matri-  and -cidium,  ‘killing-,  fr.  caedere,  ‘to  kill’.  See  -cide, ‘killing’.
matricular,  adj.  - —  Formed  with  adj.  suff.  -ar  fr.
Late  L.  matricula.  See  matriculate, matriculate,  tr.  and  intr.  v.  —  Late  L.  matriculd- tus,  pp.  of  matriculdre,  ‘to  register',  fr.  L. matricula,  ‘register’,  dimin.  of  L.  matrix ,  gen. matricis.  See  matrix,  and  -ule  and  verbal  suff,-ate. Derivatives:  matriculat-ion,  n.,  matriculat-or ,  n., matriculat-ory,  adj.
matrilineal,  adj.,  pertaining  to,  or  descended from,  the  maternal  line.  —  Compounded  of  L. mater,  gen.  matris,  ‘mother’,  and  tinea,  ‘line’. See  mother,  line  and  adj.  suff.  -al.
Derivative:  matrilineal-ly,  adv. matrimonial,  adj.  —  MF.  (=  F.),  fr.  Late  L.  md- trimonidlis,  fr.  L.  matrimonium.  See  next  word and  adj.  suff.  -al.
Derivative:  matrimonial-ly,  adv. matrimony,  n.,  1)  wedlock;  2)  a  card  game. ME.  matrimoine,  matrimony,  fr.  OF.  matre- moine,  matrimoine,  ft.  L.  matrimonium,  mar¬ riage,  matrimony’,  formed  fr.  mater,  gen.  mdtris, ‘mother’,  with  suff.  - mdnium .  See  mother  and -mony.
matrix,  n.,  womb.  —  L.  matrix,  ‘womb,  matrix.
948
source,  origin’,  formed  fr.  mater,  gen.  mdtris, ‘mother',  on  analogy  of  nutrix,  ‘wet-nurse, nurse'.  See  mother.  For  the  sense  development of  L.  matrix  (fr.  mater,  ‘mother’)  cp.  Gk.  p.r)tpa, ‘uterus,  womb’,  which  derives  fr.  moth-
er’,  and  OHG.  muodar,  ‘belly’  (whence  G. Mieder,  ‘bodice’),  which  is  rel.  to  OHG.  muoter, ‘mother’  (cp.  metralgia).
matron,  n.,  a  married  woman.  —  ME.  matrone, fr.  MF.  (=  F.)  matrone,  fr.  L.  matrdna,
‘a  married  woman,  wife,  matron’,  fr.  mater, ‘mother’ ;  see  mother.  For  the  formation  of  the word  cp.  L.  patronus,  ‘protector,  patron’,  fr. pater,  ‘father’  (see  patron)  and  Belldna,  ‘the goddess  of  war’,  fr.  bellum,  ‘war’  (see  Bellona). Derivatives:  matron-age,  n.,  matronal  (q.v.), matron-hood,  n.,  matron-ize,  tr.  v.,  matron-like, adj.  matron-ly,  adj.,  matron-li-ness,  n. matronal,  adj.  —  L.  matronalis,  ‘of,  or  belonging to,  a  married  woman’,  fr.  matrona .  See  matron and  adj.  suff.  -al.
matross,  n.,  soldier  in  a  train  of  artillery  (hist.) Du.  matrons,  corruption  of  F.  matelots,  pi.  of matelot,  fr.  MF.  matenot,  which  itself  is  borrow¬ ed  fr.  MDu.  mattenoot,  lit.,  ‘messmate’.  See
matelote.
mattamore,  n.,  a  subterranean  dwelling  or  store¬ house.  —  F.  matamore,  fr.  Arab,  matmura  , ‘something  hidden’,  prop.  fem.  pass.  part,  of tdmara,  ‘he  hid,  concealed’,  fr.  Aram,  fmar,  of s.m.  See  Siegmund  Fraenkel,  Die  aramaischen Fremdworter  im  Arabischen,  p.  137.  Aram. tlmar  is  rel.  to  Heb.  taman,  ‘he  hid,  concealed’ (whence  matmon,  ‘treasure’,  lit.  ‘something  hid¬ den’),  Akkad,  tamaru,  ‘to  cover  with  earth’, matter,  n.  • —  ME.  matere,  fr.  OF.  matere  (F.  ma- tiere),  fr.  L.  materia,  ‘wood,  timber,  stuff,  mat¬ ter’,  formed  fr.  L.  mater,  ‘mother’,  as  transla¬ tion  of  Gk.  uXt),  ‘wood,  forest,  timber,  stuff, matter’.  See  mother  and  cp.  Madeira,  madrier. L.  materia  is  not  cogn.  with  Arm.  mair,  ‘pine, cedar’,  mairi,  ‘forest’.
Derivative:  matter,  intr.  v. matter  of  fact.  —  Loan  translation  of  L.  resfacti. Cp.  G.  Tatsache,  which  is  the  loan  translation of  E.  matter  of  fact.
Derivative:  matter-of-fact,  adj.
Matthew,  masc.  PN.  —  F.  Mathieu,  fr.  Late  L. Matthaeus,  fr.  Gk.  MxTOafoc,  fr.  Maxffia;, contraction  of  MxxTaffla;,  fr.  Heb.  Mattiyyah, shortened  form  of  Mattithyah,  Mattithyahu,  lit. ‘gift  of  the  Lord’.  For  the  first  element  cp.  Heb. mattdth,  ‘gift’,  and  see  Nathan,  for  the  second see  Elijah  and  cp.  words  there  referred  to.  The form  Max-Halo?  is  due  to  change  of  suff.  Cp. Matthias.  Cp.  also  matico.
Matthias,  n.  - —  Late  L.,  fr.  Gk.  MaxlIia?,  fr.
Heb.  Mattiyyah.  See  Matthew, mattock,  n.  —  ME.  mattok,  fr.  OE.  mattuc,  fr. VL.  * matteuca ,  which  is  rel.  to  L.  mateola, ‘mallet’.  See  mace,  ‘a  staff’,  and  cp.  words  there referred  to.
949
Derivative:  mattock,  tr.  v. mattoid,  n.,  a  person  of  abnormal  mind  verging on  insanity.  —  It.  mattoide,  a  hybrid  coined  fr. It.  matto,  ‘mad’,  and  Gk.  -octS-i)?,  ‘like’,  fr. elSo?,  ‘shape,  form’.  The  first  element  derives fr.  L.  mattus,  intoxicated’,  fr.  mad(i)dus,  ‘moist, wet;  drunk,  intoxicated’,  fr.  madere,  ‘to  be  wet; to  be  drunk  or  intoxicated’,  fr.  I.-E.  base  mad-, ‘wet,  moist,  dripping;  to  drip’.  See  meat  and  cp. mast,  ‘fruit  of  beech’.  For  the  second  element  in mattoid  see  -oid.
mattress,  n.  —  ME.  materas,  fr.  OF.  materas  (F. matelas),  fr.  It.  materasso,  borrowed  in  Sicily  fr. Arab,  mdtrah,  ‘place  where  something  is  thrown or  laid’,  used  also  in  the  sense  of ‘mattress’  (see Dozy-Engelmann,  Glossaire  des  mots  espagnols et  portugais  derives  de  l’arabe,  p.  151);  fr. taralja,  ‘he  threw’.  Cp.  Sp.  ulmadraque,  ‘mat¬ tress’,  which  is  formed  fr.  Arab,  al-,  ‘the’  and mdtrah,  ‘mattress’  (see  above).  Cp.  also  mate- lasse.  Cp.  also  E.  tare,  ‘allowance  in  weight’, maturate,  tr.  v.,  to  make  mature  or  ripe;  to  cause to  suppurate;  intr.  v.,  to  ripen;  to  suppurate.  — L.  maturdtus,  pp.  of  maturare,  ‘to  ripen’,  fr.  md- tiirus.  See  mature,  adj.,  and  verbal  suff.  -ate. maturation,  n.  —  F.,  fr.  L.  mdturdtionem,  acc.  of maturatio,  ‘a  ripening’,  fr.  maturdtus,  pp.  of  ma¬ turate.  See  prec.  word  and  -ion. maturative,  adj.,  promoting  ripeness;  promoting suppuration.  —  F.  maturatif  (fem.  maturative), fr.  L.  mdturativus,  ‘tending  to  ripen’,  fr.  matura- tus,  pp.  of  maturare.  See  maturate, mature,  adj.,  ripe.  —  L.  mdturus,  ‘ripe’,  which  is rel.  to  manus,  ‘good’  (whence  immanis,  ‘mon¬ strous’),  manes,  ‘ghosts,  the  gods  of  the  Lower World’,  lit.  ‘the  good  gods’,  mane,  ‘early  in  the morning’,  Matuta,  ‘the  goddess  of  dawn’,  md- tutinus,  ‘of,  or  pertaining  to,  the  morning’.  All these  words  derive  from  base  *md-,  ‘good; early’,  whence  possibly  also  Olr.  maith,  ‘good’, W.  mad,  Co.  mas,  of  s.m.  See  manes  and  cp. demure,  immanity,  manana,  matinee,  Matuta, matutinal.
Derivatives:  maturate  (q.v.),  maturation  (q.v.), maturative  (q.v.),  mature-ly,  adv.,  mature-ness, n.,  mature,  v,  (q.v.),  matur-er,  n.,  maturescent (q.v.),  matur-ing,  n.,  maturity  (q.v.) mature,  tr.  v.,  to  cause  to  ripen;  intr.  v.,  to  ripen. —  OF.  maturer,  fr.  L.  maturare,  ‘to  ripen’,  fr. mdturus.  See  mature,  adj. maturescence,  n.  —  Formed  from  next  word  with suff.  -ce.
maturescent,  adj.,  becoming  ripe.  —  L.  mature- scens,  gen.  -entis,  pres.  part,  of  maturescere,  ‘to become  ripe,  to  ripen’,  formed  with  inchoative suff.  -escere,  fr.  mdturus,  ‘ripe’.  See  mature,  adj., and  -escent.
maturity,  n.,  ripeness.  —  ME.  maturite,  fr.  L. mdturitas,  ‘ripeness,  maturity’  [prob.  through the  medium  of  Late  MF.  (=  F.)  maturity],  fr. mdturus.  See  mature,  adj.,  and  -ity.
Matuta,  n.,  name  of  the  goddess  of  dawn  in  Ro¬
man  Religion.  —  L.  Mdtiita  (whence  matutinus, ‘of,  or  pertainig  to,  the  morning’),  rel.  to  md¬ turus.  See  mature,  adj.,  and  cp.  next  word, matutinal,  adj.,  pertaining  to,  or  happening,  in the  morning.  —  L.  matutinalis,  fr.  matutinus,  ‘of, or  pertaining  to,  the  morning’.  See  prec.  word, adj.  suff.  -ine  (representing  L.  -inus)  and  adj. suff.  -al.
Derivative:  matutinal-ly,  adv. matutine,  adj.,  matutinal.  —  L.  matutinus.  See prec.  word.
Derivative:  matutine-ly,  adv. matzah,  also  matza,  matzoh,  matzo,  n.  (pi.  mat- zoth,  also  matzos),  a  flat  piece  of  unleavened bread  eaten  by  Jews  during  the  Passover.  — Heb.  matztzah  (pi.  matztzdth),  ‘unleavened bread’,  lit.  ‘that  which  is  sucked  out’,  hence ‘sapless,  juiceless’,  from  the  stem  of  matzatz,  ‘he sucked  out,  drained  out’,  which  is  rel.  to  Aram.- Syr.  matzatz,  matz,  ‘he  sucked  out’,  Arab,  mas  fa, ‘he  sucked  out’,  and  to  Heb.  mdtzah,  ‘he  drained out’.
maucherite,  n.,  a  nickel  arsenide  (mineral.)  — Named  after  the  German  mineral  dealer  Wil¬ helm  Maucher  (1879-1930).  For  the  ending  see subst.  suff.  -ite.
Maud,  fem.  PN.  —  OF.  Mahaut,  of  Teut.  origin. Cp.  OHG.  Mahthilda  and  see  Matilda, maud,  n.,  a  woolen  plaid  worn  by  shepherds  in Scotland.  —  Prob.  from  the  PN.  Maud. maudlin,  adj.,  tearfully  sentimental.  —  ME. Maudlin,  ‘Mary  Magdalene’  (see  Luke  8:2),  fr. OF.  (=  F.)  Madelaine,  fr.  L.  Magdalena,  in allusion  to  the  fact  that  painters  used  to  rep¬ resent  Mary  Magdalene  weeping;  maudlin orig.  meant  ‘shedding  tears  of  penitence  like Magdalene’.  See  Magdalene, mauger,  maugre,  prep.,  in  spite  of  (archaic).  — ME.  maugrie,  fr.  OF.  malgre,  maugre  (F.  mal¬ gre),  lit.  ‘ill  will’,  fr.  mal,  ‘ill,  badly’,  and  gre (F.  gre),  ‘will,  pleasure’.  For  the  first  element see  mal-.  The  second  element  comes  fr.  L.  gra- tum,  neut.  of  gratus,  ‘acceptable,  pleasing, agreeable,  grateful’,  used  as  a  noun.  See  grace, n.,  and  cp.  malgre.
maul,  mall,  n.,  a  heavy  hammer.  —  ME.  made, fr.  OF.  (=  F.)  mail,  ‘hammer’,  fr.  L.  malleus. See  malleus  and  cp.  the  second  element  in  pall- mall.
Derivatives :  maul,  mall,  tr.  v.,  maul-er,  n. maulstick,  also  mahlstick,  n.,  a  long  rod  used  by painters.  —  Du.  maalstok,  lit.  ‘painting  stick’, compounded  of  malen,  ‘to  paint’,  and  stok, ‘stick’.  The  first  element  is  rel.  to  ON.  maria, OHG.  maldn,  malen,  MHG.  mdten,  G.  malen, ‘to  paint’,  OE.  mal,  ‘m
```


## [2026-09-07T16:16:16.725Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Ormazd\\|Ahura\\|Ormuzd\\|mazdao\\|Mazda\" KLN_1966.txt | head -10",
 "description": "Grep Klein for Ormazd"
}
```


### [2026-09-07T16:16:16.782Z] TOOL RESULT

```
2036:ahura,  n.,  a  benevolent  deity  (Persian  mythology). —  Avestic  ahura-,  ‘a  god,  a  good  spirit',  rel.  to OL  dsurah,  of  same  meaning.  Sec  asura  and  cp. the  first  element  in  Ormazd.
2037:Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
11938:‘I  place’,  aor.  ed,  ‘he  placed’,  Gk.  riDivoa,  ‘to put,  place,  set’,  f )eai;,  ‘a  placing,  setting’,  fHjxr], ‘case  in  which  to  put  something’,  flejxa,  ‘that which  is  placed’,  Difxi?,  Tight,  decree’,  Ssajxo;, Taw,  rule,  precept’,  lit.  ‘that  which  is  laid  down’, fb)(xtov,  Htop.61;,  ‘heap’,  flcueOXa  (pi.),  Homeric (pi.),  ‘foundation’,  L.  facere,  ‘to  make, do’,  -dere  in  ab-dere,  ‘to  hide,  conceal’,  con-dere, ‘to  found,  establish’,  per-dere,  ‘to  lose,  throw away,  ruin’,  OSIav.  dejp,  deti,  ‘to  place,  lay’, Lith.  deti,  Lett,  del,  ‘to  place,  put’,  OSIav. o-denu,  ‘clothed,  dressed’,  Gael,  deck,  ‘placed’. Cp.  ado,  deed,  deem,  doff,  -dom,  don,  v.,  doom, dout,  dup.  Cp.  also  theme  and  words  there referred  to.  Cp.  also  fact  and  words  there  re¬ ferred  to.  Cp.  also  abdomen,  abscond,  condiment, Consus,  dagoba,  dam,  ‘an  earthbank’,  family, fetial,  hoard,  perdition,  recondite,  sacerdotal, samadh,  samadhi,  sconce,  ‘a  metal  bracket’, stridhana.  Cp.  also  the  second  element  in  creed and  in  jubilate,  and  the  third  element  in  divide and  in  Ormazd.
23122:learned,  learning,  science’,  from  the  aorist p,a&£tv  (whence  the  pres,  [iavffaveiv ),  ‘to  learn’, fr.  *mndh-,  reduced  form  of  I.-E.  base  *men-dh-, ‘to  have  one’s  mind  aroused,  apply  oneself to’.  From  the  same  base  (resp.  its  reduced  form) prob.  derive  Gk.  p.Ev(H)p7],  ‘care’,  Lith.  man- dr  as,  mandrils,  ‘wide-awake’,  OSlav.  mqdru, ‘wise,  sage’,  Goth,  mundon  sis,  ‘to  look  at’,  ON. munda,  ‘to  aim’,  OHG.  mendan,  ‘to  rejoice , OHG.  muntar,  MHG.  munter,  munder,  ‘eager, agile,  nimble",  G.  munter,  ‘awake,  lively,  gay, merry,  vigorous’,  W.  mynnu ,  ‘to  want,  wish  , Alb.  mund,  ‘I  can,  I  am,  victorious’,  and  pos¬ sibly  also  Ol.  medha,  ‘wisdom,  intelligence',  Gk. Mouaot  (if  fr.  *M6vffia),  ‘Muse’.  Base  *men-dh- is  an  enlargement  of  base  *men-,  ‘to  think’. See  mind  and  cp.  Muse,  Epimetheus,  Prome¬ theus.  Cp.  also  the  second  element  in  chresto- mathy,  opsimath,  polymath.  Cp.  also  the  second element  in  Ormazd.
23215:Mazdaism,  also  Mazdeism,  n.,  Zoroastrianism.
23216:—  See  Ormazd  and  -ism.
26581:Orleans,  n.,  1)  a  kind  of  purple  plum) ;  2)  worsted- and-cotton  fabric.  —  In  both  senses  named  after the  city  of  Orleans,  south  of  Paris, orlop,  n.,  the  lowest  deck  of  a  ship.  —  Du.  over¬ loop,  ‘deck  of  a  ship’,  lit.  ‘that  which  runs  over", fr.  overlopen,  ‘to  run  over’;  (see  over  and  leap); so  called  because  it  covers  the  ship’s  hold. Ormazd,  n.,  the  principle  of  good  in  the  Zoro- astrian  religion.  —  Pers.,  fr.  OPers.  Auramazda, fr.  Avestic  Ahuramazda,  lit.  ‘wise  lord',  a  com¬ pound  of  ahura-,  ‘a  god,  a  good  spirit’  (see ahura),  and  ma(n)dzdha-,  ‘wise’,  which  is  a  com¬ pound  formed  from  the  I.-E.  bases  *men-dh~,  ‘to apply  oneself  to’,  and  *dhe-,  ‘to  put,  place’. From  base  * men-dh -  derives  also  OI.  medha, ‘wisdom,  intelligence’.  For  other  derivatives  of this  base  see  mathematical.  For  base  *dhe-  see do  and  cp.  theme,  fact.
```


## [2026-09-07T16:16:26.814Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\ndef leaf_of(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return d[:off].count('\\f')+1\nfor n in (2036,23122,26581,22737,24733):\n    print(n,'NR',leaf_of(n))\nEOF\necho \"=== page nums nr 580-600\"\nawk 'BEGIN{RS=\"\\f\"} NR>=575 && NR<=600 {n=NR; if (match($0,/(^|\\n)[ ]*[0-9]{3,4}[ ]*(\\n|$)/)) {s=substr($0,RSTART,RLENGTH); gsub(/[^0-9]/,\"\",s); print n, s}}' KLN_1966.txt",
 "description": "Locate Klein Ormazd leaf and page numbers"
}
```


### [2026-09-07T16:16:28.275Z] TOOL RESULT

```
2036 NR 34
23122 NR 509
26581 NR 587
22737 NR 501
24733 NR 546
=== page nums nr 580-600
```


## [2026-09-07T16:16:32.007Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=560 && NR<=620 {n=NR; if (match($0,/(^|\\n)[ ]*[0-9]{3,4}[ ]*(\\n|$)/)) {s=substr($0,RSTART,RLENGTH); gsub(/[^0-9]/,\"\",s); print n, s}}' KLN_1966.txt",
 "description": "Klein page numbers leaves 560-620"
}
```


### [2026-09-07T16:16:33.205Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:16:51.835Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\n\"",
 "description": "BQT/MON/SNS details"
}
```


### [2026-09-07T16:16:53.076Z] TOOL RESULT

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
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-07T16:17:00.396Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 130\\]|\\[pdf page 131\\]/' BQT_v4_pages.txt | head -80",
 "description": "BQT vol4 pdf page 130 (printed 2047)"
}
```


### [2026-09-07T16:17:01.598Z] TOOL RESULT

```
[pdf page 130]
ند ها ملیوش
و بممتی علوی هم‌آمده است که در برایر سقلی منوشان - بروزن خموشان, ام حاکم
است ۱ ؛ وباین معنی بفتح اول هم کفته‌اند. فاری‌است که ازجانب کیخروحکومت و پادشاهی
منوچهر ؟ - بکر جیم فارسی . فاری میکرد9 - وعنع ازنوشانیدن هم‌هست؟۹ .
یی بهشت روی » چه مئو مخغف مینواست که مه - بفتح اول و ثالی وظهور ها » فك
بهشت باشد وچهره بمعنی روی » و بمعنی علوی | اسفل‌را کوبند که چانه ومرتبهٌ پایین دهان باس
ذأات هم‌هت چه متو بمعنی علوی وچهر بمعنی | و بکسراول و اضم آخر » در عربی بمعتی از او
ذات باشد - و نام پرابرج است وبعتی کفته‌اند | باشد -
نبیرة ابرج است ازجالب دختر » اسّاعلم. کوبند منهیان ۷ ر بع مسکون - کنایه
چون سلم وتور ابرج را کشتند تیغ بر اولاد او از هفت ک و کب است که زحل و مشتری و مرخ
نپادند وا کثرمخدرات اورا هلاكساختند, یکی‌از | وآفتاب و زهره وعطارد و ماه باشد +
سنورات خر کیرجر سابل کرت | منهیان سبع طباق ۶۸- بسنی
کی کل وا مانوی هر کرد ۴ منهیان ربم مسکون است که سبعهٌ سیاره باشد.
کوه متولد شده بود اورا مانوش چهر‌فام کرد
وبمرور ایام وتغییر السته منوچهر شد » و بعتی منیژه ‎٩‏ - با تحتانی مجهول و زای
کوبند که مادر اورا نام نکرد تا بز رکه شد واو | فارسی » بروزن ومعنی منیجه است که نام دختر
بفایت خوش‌سورت بوداورا منوچهرخواندند بمنی | افراسیاب باشد و بیژن پسرکیو یاو عاشق بود.
بپشت صورت چه‌هرچیزخوب راببهشت سبت کنند منیوش *۱- منم از غنیدن و کوش
ویتغییر النه منوچهرشد - ونیزنام مبارزی بوده | کردن باشد بمنی‌مشنو وکوش مکن‌چه‌لیوشیدن
ایرانی پسرآرش ۰ . شنیدن ‏ وکوش کردنراکویند .

۹ <مینو (هم.) ۴ - دراوستا ۳8ظ11) 8180080 [ر4 : بوستی . نام نامه
۳-۱۹۱ ] جزو دوم چیثره همربشه « چهن > فارسی است که در اصل بمعتی نژاد بوده » این
کلم مر کب بمعنی * ازنژاد وپشت منوش » است . متوش محقفاً یکی از ناموران قدیم بود که
آمروزه دراوستا اسمی ازو نیست. ولی درکتب دیگر نام چند نامور پسورت « مانوش > باد شده از
جمله در فصل۳۱ بندهشن‌بند ۲۸مانوش درسللةٌ نسب لهراسب جزواجداد آن پادشاه کیانی‌شمرده
شده است . نیزدرفرهنگها مانوش یا مانوشان نام کوهی‌است که منوچهر دربالای آن تولد بافته »
لابد این کوه بناموری که مانوش نام داشته منسوب است ( رك: مانوشی ). اسم خاندان منوچهر در
اوستا 8۷2لک ۸ آمده بمعمنی باری کنندة ایرالیان. اسم منوچهر وخاندان وی (ایرج ۳ اثیرباوه)
فقط بکبار در اوستا بند ۱۳۱ فروردین بشت پاد شده است . رك : بشتها اس *0 - ۰0۲

۴ - رك : مانوش . ۴ - ققه‌اللشهٌ عامیانه . * - 312209835 : ۱)نم
پادشاه کرمان ‏ تابع کیخرو. ‏ ۲) متحفظ فراموشخانه درزمان هرمز 0۳72217 چهارم(تئوفانی
۳ ) ۸« پوستی . فام نامه ۱۹۱ ۰ ‎٩‏ - هی از « نوشانیدن >.

۷ - جمع « هنهی > بنم اول اسم فاعل از آنهاء (عر) بمعنی خبن دهنده -

۸ داهفت طبقه . ماٌخوذ ازآیِهٌ ۳ سورة ‎٩۷‏ ( الملك ) وآ یه ۱۶ سورة ۷۱ (نوح)-

۰۱۹۰ ‏ط2ط۸1۵282 ( طع‌طاعژه3/6 ) موت‌نام 812080 «یوستی. نام‌نامه.‎ - ٩

ایزگ نهی از ۶ نبوشیدن؟ .

[pdf page 131]
بیان بیست و ششم
درمیم با واو مشتّمل برهفتاد و دو لغفت و کنایت
مو - بنتح اول و سکون نانی , آواز | وآنرا موالید ثلائه هم میگویند.
وصدای کربه‌باشد وعربان کر به را ستورخواشد ۱ موبد ‎٩‏ ۴ جم اول و کنر بای ابجد
- و بلفت پودانی ۴ نام بیخ دوائی است که هم | وسکون ثانی و دال بی نقطه » حکیم و دانشمند
پیودای‌میون خواشند وآن برنگه ووزن غاربقون | وعالم‌ودانا وحا کم وصاحب دیرآتش پرستان باشد؛
باشد لیکن اند کی بزردی مابل است.بولوحیضش | و بفتح اول وبای ایجد هم گفته‌اند.؛ و پم اول
براند. کوبند کزروزردك صحرائی است۴ - وجضم | وفتح بای ایجد هم‌آمده است - ونام شوهرونه
اول» معروف است و بعربی شمر میگوبندگ ‏ است که رامین برادر او عاشق او بود ۷ ۰
موالید ؟ سه گانه - بر بته وبر موجان ۸ - با جیم بروزن خوبان ,
رسته وجنبنده راکویند پمنی‌جماه ولبات‌وحیوان | چشم خوب پر كرشمهٌ خواب‌آلود را گویند.
۱ موم * میومیو ( اسم صوت ).
۲ - مو ۳30 کلمهٌ عربی اس ت که از بودانی 22808 ۸
بحروف عربی نقل شده و آن 520۷286 28610 ام
(0ع 20 سقطاه ۳۵ع11) است . «عقار۲۳۱ ف» 3 مو, /
هوالمران و بعجمية الاندلی مرانه . > «عقار 2۷۳۱+ ۹ مث
۴ - مویفتح اولقزوینی 338/۷ (مو) ۰ 128[/۷888 ان ۱
( شاخه‌های مو ) » کرماشاهی کَقْل - 1338۲۷ (درخت مو ) ؛ ۳ ۹
خواداری 338 , «زفولی 3380 « سالنامة کلپایگان ‎4٩‏ > 4
سا ۲6۲۵نط۷1 ۷:5 « ثابتی ۲۱۰ درخت انگور است . مو
۴ «موی (م.) ب جمع مولود (عر). زاییده. ۹ پهلوی ۰13881281
ارمنی 30861 ۰ 1320۷281 « اسشق ۰۰۹۸۶ از : 0811 - 073281 جزء اول همان مخ
(هم.) است وجزه دوم پوند « بد > (در: سپهید . هیرید) * اوستایی 02 است « دارمتر .
تتبمات جچ ۱ص ۹۲۸۹ . در اوراق مانوی (پارتی) 1380/8 (هنینگه . فپرست‌کلمات پارسی میانه ‏
858 , 17 .1۱.ص ۸۵ ). ؛ این عنوان بروحانیان زرتشتی اطلاق شود .
۷ - چنان‌آمد که روزی شاه شاهان که خواندننش همی موبد منیکان
بدید آن سیمتن مرو روان را بت خندان و ماه بانوان را ۰ : ۰
« ویس ورامین ص ۳۳ -
۸ - «موجان, در کس‌شکنته وچشم نیکوان‌راخوانند.» «لغت فری‌چاپ‌هرن‌س۹۸* «موژان,
چشم نیکورا کوبند که اندااند4 متحرا‌شود بنظر وحالی‌دارد ازلطافت. فرخی (سیستانی) کوید :
خوی کرفته لاله سیرابش از اتف لبید
خیره گشته درکس موژانی ( موجاش ) از خواب خمار .»
« لت فری چاپ اقبال ص ۳۵۹ *.
```


## [2026-09-07T16:17:17.542Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 135\\]/' BQT_v4_pages.txt | head -60",
 "description": "BQT vol4 pdf page 135 (printed 2052)"
}
```


### [2026-09-07T16:17:19.228Z] TOOL RESULT

```
[pdf page 135]
موژّه ومد
است و آنرا پثر کی چکمه(۱) میگوبند و نام | زنبور باشد وآن پرنده‌ایست کزنده ؛ و بفتح اول
حلوائی هم هست؛ وبحتی باین هم‌آمده است ۴ .
معتی بفتح اول کفته‌اند . موسیچه - با اول بنانی رسیده واسین
۰ 2

موزه - با زای‌فارسی بی‌نقطه بتحتانی کشیده وفتح جیم فارسی » پرنده
و ثالی معروف بر وزن روژه » است شبیه بفاخته۴ راوبیشتردرمیان طبق وکاسه
غم واندوه ومصییت باشد ۱ - موزه وکنار طاقچةٌ خان‌ها تخم (۳) میکند وبچه می
و با انی مجهول . استخر و آبگیر و تالاب را | آورد؛ وبختی‌سموه را مومیجه میگویند! وبستی
کوبند ‎٩‏ . ابابیل را ۰

موزه در گل‌ماندن » کدبه از موسیقار ۴ - با قان بروزن بوتیمار:
درماندء شدن وپای بندگشتن و دشواری کشیدن سازی است معروف که آنرا از نیهای: بز رکه
باشد. ‏ , ۱ و كوچك باندام مثلث بهم وصل کرده‌اند ؛ وبحنی

موده لهادن - کنایه از ت رکه سفر | کوبند سازی است که درویشان دارند ؛ و بسشی
کردن است که اقامت نمودن باشد. دیگر گوبند سازست که غبانان‌مینوازند!وجممی

موسخ - با سی‌بی نقطهپروزن‌دوزخ(۷). ۱ کوبند نام پرنده ایست که در منقار او سوراج
بممتی‌زنارباشد وآن رشته اشت که کفار بر کردن | بسیاری هت وازآن سوراخهاآوازهای گوا کون
اندازند وبرمیان هم بندند . برمپاید وموسیقی ازآن مخوذ است 8 .۸

موسه - بنم اول بروزن"بوسه » بدمنی موش - با تانی‌ممروف. جانورست که

(۱) چك » چش : چزمه . (۷) چش : دوزن - (۳) چش : خانه بیضه .

۹ - ر3: موژ . ۴ - رك : جهانگیری » رشیدی .

۴ - « موسیچه » مرغکی سییدگون بود مانند قمری . خسرو ی کوید :

موسیچه و قمری چو مقربانند از سرو بنان هریکی تبی خوان .>

« لغت فری ی 4۹۸ ۴ .۰

۴ - عریی ازبونانی 1330181166 ( موسیقی ) [ ر: موسیقی ] دزی (ج ۲ ص۹۲8 )
* موسیقار » را بممنی موسیقی‌دان ( 1318160168 [فر]] ) آورده است .

* این قول اضانه است :

تا چکاوك بست موسیقار برمنقار خوش ارغنون زن کشت بلبل پردرخت ارغوان.
خوش بود آواز موسیقار وصوت‌ارغنون ساخته با یک گر درمجلس شاه جهان.
«* معزی تیشایوری ص ۰۲۵۷۸
از اینجا واستعمالات دیگر پبداست که «* موسیقار > را بمعنی ساز معینی بکار میبرده‌اند.

۰1321381016 ‏موسیقی -جنم اول, از یونانی183201181166(موسیقی).لانینی 13208108 (قس : ف‎ ٩
‏انگه 13۷96 , آلم 3108۴ ) مأخون از182 ( بسنی 73186 (فر) هريك از فه ربقاللوع‎
‏اساطیری‌یونان که‌حامیان هنرهای‌زیبا بودند) ؛ فن‌تر کیب اصوات بنحوی که بگوش خونایند بوده‎
۴ ‏معرفت احوال‌الحان وآنچه التیام‌الحان بدان بود وبدان‌کامل شود « نفایی‌الفنون چص۷۷‎
```


## [2026-09-07T16:17:45.834Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 332 -l 332 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg332 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 332"
}
```


## [2026-09-07T16:17:47.344Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"اهورامزدا\\|اهورا مزدا\\|مزدیسنا\\|Ahuramazd\\|Ahura\" BQT_v1_pages.txt | head -10",
 "description": "Grep BQT vol1 for Ahuramazda"
}
```


### [2026-09-07T16:17:47.551Z] TOOL RESULT

```
total 2672
drwx------ 2 sfmqrb sfmqrb   4096 Sep  7 12:17 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb 101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    449 Sep  7 12:17 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb  85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb   7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb  19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb  40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb  33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb  46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb  51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb  37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb  58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb  97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb 146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb 163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb 128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb      4 Sep  7 12:17 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb  35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33685 Sep  7 12:01 z_mezna.png
```


### [2026-09-07T16:17:47.597Z] TOOL RESULT

```
262:۱ داجم باین موضوع نگاه کنید به «مزدیسناو تأثیر آن‌درادییات فارسی »
534:نفسیر اوستا مقلم استاد بود داود ۰ مزدیسنا و تأثر آن در ادبیات بادسی مقلم
4497:مزدیسناو تأثیر آن‌در ادیات بادسی .محمدهمن. از انتشارات .
4498:دانشگاه :پر ان شمارة؟. جابشا نة دانشگام۱۳۲ شمسی. . (عمزدیسنا).
4815:مزدیسنا اه
6538:دمزدیسنا ۱۷۷ ۰۴ درکیلکی قفا . فریزندی و بیریی. و طنزی طفقناة « . اس 4د۷»
6572:فردوسی « مزدیسنا ۱۸4 - 6۱۸۷
6663:فردوسی« مزدیسنا ۱۸۷بعد *
6961:۵ آذران با آدران معععفق. معابد و آتشکده ها یکوچك زرشتیان. «مزدیسنا ۰۷۳۳-۲۳۲] تربلدگان وت
7078:فرنبغ‌است . « مزدیسنا ۲۳۱ » و ره
```


## [2026-09-07T16:17:54.392Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg332.png"
}
```


### [2026-09-07T16:17:54.762Z] TOOL RESULT

```

```


## [2026-09-07T16:17:54.759Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T16:18:13.988Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg332.png data/verification/sources/refs/ocr/BOOK/332.png 2>/dev/null || (mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg332.png data/verification/sources/refs/ocr/BOOK/332.png); ls data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG to audit dir"
}
```


### [2026-09-07T16:18:15.259Z] TOOL RESULT

```
95.png
96.png
99.png
```


## [2026-09-07T16:18:15.557Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=315 && NR<=335 {print \"#### leaf\", NR-1; print substr($0,1,400)}' BQT_v1_pages.txt",
 "description": "Inspect BQT vol1 leaves 314-334"
}
```


### [2026-09-07T16:18:16.771Z] TOOL RESULT

```
#### leaf 314
آردو ت
برابر نا
سس ۳ص اس ای دیس ۳۳
سذ الفبای ار دو
۳ کیت لا
2 غ ۹ | کیت عرلا
ف ف‌ ِ؛
ت | نا 98
ات 42
ات 4و
ك 7 ار
۳ ‌ ۰ ۷ ی
ی ژا خر سر
و ۱ ول و ۷ ا(زم ؛ ساح خزطعرر
۸ ۳ اج باه | ارف افن‌را)
۱ ] ح شُرر
۵ ۵ 9
7 مر عب | #وع لا یکرجنت)
رل ۵ 92۳۱ از ء ک ز�
#### leaf 315
شراب است - و حبایی را نیز کوبند که بردوی
شراب بهم رسد - و کو کب و ستاره - و شرارةٌ
آش را نز کفته اند .
ارژ نگ ۱ »با زای فارسی بر وزن
و معتی ارشگه امت که نکار خانةٌ حانی نفاش
باشد . گریند اصل این لت باين همتی ارننگه
با ثای مثلثه مود
#### leaf 316
لرسانیفون
ارسانقون » با اك بالف کشیده
و نون تحتانی رسیده و فاف مضموم بواو و نون
زده » بلفت‌بونانی زرنبخ زردباشد وآن‌جوهرست
کومتشد یامر ند هر هتکتی که از ان شخورد
یمیید »
ارس بز آن - بکر الث و ضم بای
ابجد , چرك کنج چشم بز کوه�
#### leaf 317
وا ۱ ارغاب
جمیم گزندکان بگرایزند و آرا ازطاعاسیا
وار طمسا دز خوانئد محذف نحتانی .
ارطی - بنتح او و طایحطی وسکون
انی و محتانی ۰ بلفت رومی‌درخت وزاه را گوشد
که پده است و بمربی غرب خوانند » و بکس
ثالث ليز همین معنی کفته اند ۵ .
ا
#### leaf 318
ارغامونی
ار غامو نی پامیم بر وزن افلاطونی؛
بلغت بونانی تباتی است
صحرایی و برنگ
تردنك(۱) شقایق‌صمان
بائد و آنرا بشیرازی /
ماعیثای سرخ کوند .
ب رکه آن رابرچشم‌ورم
کرده خباو کننه نامم باشد ِ
ارغاو ه بفتح اول وسکون ثانی والث
ب�
#### leaf 319
سس سا
مشهور که افلاطون وضع (۱) کرده است ؛» و
ی گونند .ارغنون
ترجبة مزامیر است
بعنی جمیم ساز های
»؛ وبسنی دیگر
کرنند چرن هزار
آدمی از پبر و جوان ارغنون باریری ۷
همه پیکبار بآراز های مخالفبکدیگر چیزی
بخواد هد آن حات را
ارعنون خ
#### leaf 320
ار که
واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛
و باین معنی نم اول و انی مشهور است
ار کال -بکر اول و سکون ثانی با
کاف بالف کشیده وبکاف دیگر زده » قطرباران
(۲) کوچك‌را کویند که نرم باران باشد .#۶
ار گنج - بنم اود و سکون ثانی
و 
#### leaf 321
سب ۱۰۵ تت
ضحاك می فرمود بکشند و مغز سرایشالرا بجهت
مارالی که از کتف او برآهده بودند حاضر
سازند ء يك‌فررا آزاد میکرهد و میگریزانیدد
و بجای مفز سر او مفز سر کوسفند داخل می
لمودند . و گوبند کردان صحرا نثین از دل
آلجمات اند .
ار�
#### leaf 322
ارمند
زلایتی‌است از کوهستان آنربابجان و مولدشیرین
مشهور آبجا بوده و ابریشم ارمنی منسوب بدانجا
است - و مخثف اگر من باشد در محاورات ؛
وبنعنی اول بکسر اول هم .کفتهاند .
از من « بروزن‌فرزند , مخففآرمیده
مند است یسی صاحب آرام و 
#### leaf 323
از یا
وجیم. , بمعنی آرنج است ت که بندگاه ساعد
وبازو باشد وبحربی مرفق خوانند .
ار ندان بر وزن‌قلمدان 4 يو
و حاشاً باشد .
ار نوار بنثح وأو بر وزن سی فراز »
نام خواهر جمشید است که با خواهر دبگرشهر
از در حبالهٌ ضحاك بودند و عاقبت ب�
#### leaf 324
ارء جان
اره‌جان با ثاتی‌هشدد و جیم بروزن
پهلوان » نام شهری است که ما ین آن شهر
وش رازشصت فرسنکه واه است وا ترا هوام‌ارمغان
خوانند باغین نقطه دار .
ار هفت- باها بروزن زریفت ۰ یکی از
پیغمبران‌است باعتقاد کفرء هند؟ . وایشان ش
#### leaf 325
<<
۶+ )راد - یک اول بر وزن خبار » بن
و تك آب را خوانند - و دستار را یز گویند -
و هی چیز که بر پا یکشند مانند شلوار وتتبان
و در عربی بممنی‌زن باشد که درمقابل هرداست-
و بسمتي لنگی و لنگ فوطه هم حست .
ار ار با یکسر اول و رابم و بای
قرسی 
#### leaf 326
از ذست ب رکرفتن
یت و بود گردانیدن باشد .
هوز بالف کشده , نان فطیر را گویند یمن بعنی نافی
که خمیر آن نرسیده باشد .
از دست دهرجستن - بستی از
خر افتادن است که مردن و از عالم رفتن باشد .
از دست رقتن - کناید از بخودی
و بی اختیاری و اضط�
#### leaf 327
ما
ارم » جح اول و سکون.تانی و میم »
بنتی فد باشد ‏
ارمل س بر وژن جدول » بمنی بسیار
وکثیرباشد. وصدا وآوازرا یز گومند - وبمعنی
همه و مجبوغ هم آمده است
از ناو با نون و واو بی وزن غرفاو .
نم ناحیه‌ایست از نواحی حمدان .
از ناوه ت شتح 
#### leaf 328
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی�
#### leaf 329
۱ <<
رومی است . 1 2 بکویتد و باشیر تازه
بیامیز ند وبرزیر خصه‌بمالند نموظ عجبآورد۱
اساسه بفتح نی رو اس :
بمعتی نگرستن بگوشة چشم ووایس دیدن‌باشد ۴
وبکی اول نیز گفته اند .
اسا لیطوس یکی لام و سکون
تحنالی وضم طای حطلید واو وسین می�
#### leaf 330
اسپخحول بکسر اول و سکون‌انی
و بای فارسی مکور و خای نقطه دار حضموم‌بواو
ولام زده » بععتی‌پیخال است که فضله وافکند گی
اسیر ۱ س با بای فارسی بر وزن مهتر»
سپررا گونند و بعریی جثه خوانند .
اسپر اثین )0 بابای فارسی» بروزن
وممنی ا
#### leaf 331
فآ فا برگه زرد چوبه است -
ودرخت خربزه را نیز گوبند .
اسیر لو س « بالام وسین بی‌نقطه ووار
مجپول بروزن کشورسوز » خانه وسرای پادشاحان
و سلاطین و حکام را کوبند .
اسیر 8 - بکسر اول و فتح ثالث ورابم
و سکون ثانی و میم » بمعنی اول اسپرغ
#### leaf 332
قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱
است ۰ چه غول بدمنی کوش هم آعده است ؛
وجط یکونند چون ب رکه آن بگوش اسب‌شبه
و معنی اسفناج است »
و آن سبزی باش د که در
آش و هله کنند , سرفه
است‌بنابرین اسب‌غول خوانند و بضی بشپش‌تشبیه | �
#### leaf 333
26 ٩
ح ی 9 من - ۳۲6 وک در ۳
براء
ء ‏
صعحه
رر 9
اسفهان
#### leaf 334
تست سس ات سس سوت سس منت سس
اصنهان
ترایز صقعةٌ ۱۲۳-
```


## [2026-09-07T16:18:37.217Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"اهورا\\|اورمزد\\|هرمزد\\|Ahura\\|Auramazd\\|mazdāh\\|Mazdāh\" BQT_v1_pages.txt | head -20",
 "description": "Grep BQT vol1 for Ahura/Ohrmazd"
}
```


### [2026-09-07T16:18:37.273Z] TOOL RESULT

```
1533:عنصری واسدی که این کلمه‌را درست نیاورده‌اند اورمزدی» شاعرفزن‌چپارم
1772:وادنامزد شدند» نامپای‌خرد وروان وتن هرمزد یابرجیس(مشتری) نجم‌داد
10641:یا کی ونقدس وفالون اهورامزداست ودرجهان خاکی نگیبانی آتش بدو سپرده است ( وبهمین‌جهت
11036:0 :, در فلرسی هرمزد (ختح میم) . هرمزد (بضم میم) » اورمزد » هورمزد , هرمزهم
11045:< هرمزد » ودر فپرست روزهای سغدی * خرمژد » ودر فهرست روزهای خوارزمی « ربمژد > باد
11668:روز ماه بدو سپرده شده » پنجمین امشاسینداست واو نمانده بردباری و شکییابی و سازش اهورا
14692:اوهرمز د,خداست و چون اورمزد در فارسی بمشتری اطلاق شده . بفعتی آخیر در من آمده ات .
15389:ن اهوراهز دا _ بفتح اول و ششم , ره : ارمز . .ابا
24891:(آفرنش) هرمزد خدای» کنامات جمت امنت ( جسته است ) .» وست ۷۷656 ؛ پر کست را دد
25294:۱ . نام نواده انوشیروان بر هرمزد چهارم ( ۵4۰ - ٩۷۷‏ مُ 3
28590:اورمزدی , «لفت فرس ٩۳۲۱‏ .
```


## [2026-09-07T16:18:44.080Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\ndef leaf_of(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return d[:off].count('\\f')\nfor n in (11036,11045,14692,15389,10641):\n    print(n,'leaf',leaf_of(n))\nEOF",
 "description": "Locate BQT vol1 leaves for Ahuramazda"
}
```


### [2026-09-07T16:18:45.405Z] TOOL RESULT

```
11036 leaf 321
11045 leaf 321
14692 leaf 397
15389 leaf 411
10641 leaf 312
```


## [2026-09-07T16:18:55.365Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==322' BQT_v1_pages.txt",
 "description": "Print BQT vol1 leaf 321 in full"
}
```


### [2026-09-07T16:18:56.619Z] TOOL RESULT

```
سب ۱۰۵ تت
ضحاك می فرمود بکشند و مغز سرایشالرا بجهت
مارالی که از کتف او برآهده بودند حاضر
سازند ء يك‌فررا آزاد میکرهد و میگریزانیدد
و بجای مفز سر او مفز سر کوسفند داخل می
لمودند . و گوبند کردان صحرا نثین از دل
آلجمات اند .
ارمز پشم أول بروزن هرمز . نام
روز اول است از هرماه‌شمسی - و نام فرشته‌است
که امور و مصالح روز ارمز بدو تعلق دارد- و
نام سثار؛ مشتری است - و نام پسر اسفندیار
ین
ارمن
که ادرس بیغمیر باشد و اورا هرمی هرامه
ليز کویند . ۱
ار هغان « باغین شقطمدار بروزن‌پپلوان,
نحفه و سوغانی را کورند ۴ که چون از جابی
یایند بجهت دوستان بطریق ره آورد (۷)یاور ند
و آن را ارعفاتی بر وزن لن ترانی هم گویند ,
و ضم ثالث بر وزن مردمان هم اشتقت اد
وآنرا بعربی‌عراشه خوانند - ودرم و دیتار رالیز
کته
ار مك بشم اول‌بروزن‌اروك» پشمینه‌ای
باشد پوشیدلی .
ارمز است که نام ستار مشتری - و نام روز اول
حر ماه - و لام یس اسفتد بار (۱)- و نام فرشته‌ای
باشد .
آرمس - بر وژن و حعنی هرهس است
(۱ چش : اسیندبار . )۱( خ ۳ ؛ راه‌آورد .
۱- اوستا ۸12208۷ ۸۷۲2 . پارسی باستان ۸۲2۳8280 . پهلوی
0 :, در فلرسی هرمزد (ختح میم) . هرمزد (بضم میم) » اورمزد » هورمزد , هرمزهم
آمده . نام خدای مزدیسنا , مر کب از اهوره در اوستا و ۸511۳۵ در ساسکریت از ريش 250
ساتسکریت و لا20 اوستا بمعنی سرور و مولی « دارستتر . زند اوستا . ج ۱ ص ۲۱-۲۰ > ؛
مزدا در اوستا « بسنا 4۰ : ۱ بمعی حافظه آمده . در کانها ( بسنا 4۵ : ۱) یمعنی بخاطر
سپردن وبیاد داشتن است . این کلمه در سانسکریت صورت 126025 بمنی داش و هوش است »
بنابراین چون‌با اهوره استعمال شود ازآن معنی حوشیار ودانا وا گاه اراده کنند «بارتولمه۱۱۹۲»؛
در پهلوی نیز آنرا 80 ترجمه کردمانن « زند اوستا ج ۱ ص ۲۱-۲۰ ۰ بتابر آنچه کته
شد اهورمزدا بمعنی سرور داناست . ابرانیان باسثان بمنوان تبسن و تبرك نتین روز ماه را نام
خدای بزر که نامزد کردند . ابوربحان در آ ثلر الباقبه نام این روز را در فپرست روز های امرائی
< هرمزد » ودر فپرست روزهای سغدی * خرمژد » ودر فهرست روزهای خوارزمی « ربمژد > باد
کرده « آثارالبابه ص ۳: ۰ 4٩‏ ۰ ۹۸ » رك : روز شماری ۱۳ - ۱۹ . بعد ها این نام را بتارة
مشتری‌اطلاق کردند . ۴ - باین معنی در لفت غزی وارد
شده وبعضی برمقان گفته‌اند دکاتفری ج۱ ص‌۱۲۵*.
۴ - این نلم در کتيبةٌ ستون ( شتان ) ۸۲۳۱۵2
است.| کنون‌آن تاحیت‌را ارمشثان کویندوقوم‌ارمن‌را ارمنی
( در استی6 ۸۲۲۳۱002 ) «2 . است ٩۱*۷‏ ».هلوی]9 3۳۳2
« خسرو کواتان بند۵۲ » «اونوالا ۲۹۳ ارامنه خودرا ۲1218
و کشور ارمنتان را 118765020 کوبند .
ار مگان- بان فرسی بروزن اسنهان,
تریت کننده و مربی را کویند - و بمعنی سعد
وسعادت‌یز نج ات ۰
ادهی ۴ « بفتح اول بی وزن ارزن .
```


## [2026-09-07T16:19:25.882Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=320 && NR<=345 {split($0,a,\"\\n\"); print NR-1\": \"a[1]\" || \"a[2]}' BQT_v1_pages.txt",
 "description": "First lines of BQT vol1 leaves 319-344"
}
```


### [2026-09-07T16:19:27.204Z] TOOL RESULT

```
319: سس سا || مشهور که افلاطون وضع (۱) کرده است ؛» و
320: ار که || واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛
321: سب ۱۰۵ تت || ضحاك می فرمود بکشند و مغز سرایشالرا بجهت
322: ارمند || زلایتی‌است از کوهستان آنربابجان و مولدشیرین
323: از یا || وجیم. , بمعنی آرنج است ت که بندگاه ساعد
324: ارء جان || اره‌جان با ثاتی‌هشدد و جیم بروزن
325: << || ۶+ )راد - یک اول بر وزن خبار » بن
326: از ذست ب رکرفتن || یت و بود گردانیدن باشد .
327: ما || ارم » جح اول و سکون.تانی و میم »
328: اراد || باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
329: ۱ << || رومی است . 1 2 بکویتد و باشیر تازه
330: اسپخحول بکسر اول و سکون‌انی || و بای فارسی مکور و خای نقطه دار حضموم‌بواو
331: فآ فا برگه زرد چوبه است - || ودرخت خربزه را نیز گوبند .
332: قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱ || است ۰ چه غول بدمنی کوش هم آعده است ؛
333: 26 ٩ || ح ی 9 من - ۳۲6 وک در ۳
334: تست سس ات سس سوت سس منت سس || اصنهان
335: اسیندار هف ۱ - بش میم وسکون || ذال نقطه دار. بروزن ومعنی اسفندارمن است که
336: ابجد و ظهور های هوز ؛ مخفف اسباه است که || لشکر و سپاه باشد - و سگه را ليز کوشد که
337: ۱ ۷۲۳ || ظروف می را سفید کند و اورا قلعی کر وسفید
338: یعتی باز داشت و منم دفتن کرد . || استای بکر اول وسکون بای‌حملی,
339: علم است بی حیوانات و نباتات » بر خلاف‌استه که اسقر » بروزن || متخصوص بانات لتعرتی کانه از مردم اصیل اف
340: استرش -ایم اول و لت و قحرابم || و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را
341: وت ۱ تیم || استوی بش اول والث بر وزت بر
342: استینه ۱ || وورم وآمای کرده باشده وی سرعابی‌را گویشد
343: راک ِ || ۰
344: اعاء کلي اسطرلاب هفت‌عدد است : ۱ ام ۲۰ - عضاده , ۳ صفایح» نگ رن || ۵ - فری » ٩‏ - فلس , ۷ - قطب .۰ ۶ التفهدم بیروئی مصحه جلال همایی ص و۲۸ - ۳۱۵ »
```


## [2026-09-07T16:19:47.908Z] TOOL CALL #44: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-07T16:19:47.949Z] TOOL RESULT

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


## [2026-09-07T16:19:55.927Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n=NR-1; if (match($0,/[۰-۹]{3}/)) {s=substr($0,RSTART,RLENGTH); print n, s}}' BQT_v1_pages.txt | awk 'NR%1==0' | sed -n '1,60p'",
 "description": "Find Persian 3-digit numerals per BQT vol1 leaf"
}
```


### [2026-09-07T16:19:57.249Z] TOOL RESULT

```
1 ط�
2 ر�
3 ش�
4 ۱�
5 ض�
6 ر�
7 ر�
8 ص�
9 س�
10 ر�
11 س�
12 پ�
13 پ�
14 س�
15 ر�
16 ع�
17 ز�
18 ش�
19 ز�
20 ز�
21 س�
22 ع�
23 ز�
24 ش�
25 ز�
26 ع�
27 ز�
28 ز�
29 س�
30 ۳�
31 پ�
32 پ�
33 س�
34 س�
35 س�
36 س�
37 س�
38 س�
39 س�
40 س�
41 س�
42 پ�
43 س�
44 س�
45 ر�
46 غ�
47 س�
48 پ�
49 پ�
50 س�
51 پ�
52 پ�
53 ذ�
54 ر�
55 پ�
56 پ�
57 ص�
58 پ�
59 پ�
60 پ�
```


## [2026-09-07T16:20:03.123Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef fa2int(s): return int(s.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')))\nfor i,leaf in enumerate(d):\n    if not (300<=i<=360): continue\n    head='\\n'.join(leaf.split('\\n')[:2])\n    nums=[fa2int(m) for m in re.findall(r'[۰-۹]{2,3}',head)]\n    nums=[n for n in nums if 60<n<200]\n    if nums: print(i, nums, repr(head[:60]))\nEOF",
 "description": "Extract page numerals from BQT vol1 leaf headers"
}
```


### [2026-09-07T16:20:04.542Z] TOOL RESULT

```
321 [105] 'سب ۱۰۵ تت\nضحاك می فرمود بکشند و مغز سرایشالرا بجهت'
```


## [2026-09-07T16:20:10.162Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef fa2int(s): return int(s.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')))\nout=[]\nfor i,leaf in enumerate(d):\n    head='\\n'.join(leaf.split('\\n')[:3])\n    for m in re.findall(r'[۰-۹]{2,3}',head):\n        n=fa2int(m)\n        if 1<=n<=600 and abs(i-n-215)<12:\n            out.append((i,n,i-n)); break\nfor t in out: print(t)\nEOF",
 "description": "Fit BQT vol1 leaf-to-page offset"
}
```


### [2026-09-07T16:20:11.441Z] TOOL RESULT

```
(321, 105, 216)
(334, 123, 211)
(344, 131, 213)
(437, 217, 220)
(595, 378, 217)
(607, 383, 224)
```


## [2026-09-07T16:20:40.338Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"manuš\\|manusc\\|mānūč\\|Manūčihr\\|mēnōy\\|mainyu\" SNS_pages.txt | head -20; echo \"=== leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt",
 "description": "Grep SNS for manus"
}
```


### [2026-09-07T16:20:41.638Z] TOOL RESULT

```
584:                                                                     TD Manuscript No. 2, Bombay 1908.
15384:aoramainyu- 339/1                                  ar^zara- 42/20                axs 3/9
=== leaves
242
```


## [2026-09-07T16:20:46.663Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nfor i in (233,234,235,236,237,238,239,240,241):\n    print('#### leaf',i)\n    print(d[i][:900])\nEOF",
 "description": "Print SNS last leaves"
}
```


### [2026-09-07T16:20:48.051Z] TOOL RESULT

```
243
#### leaf 233
                                         r
                                             tw oaf!* tab <jlj   tj>V« j^j'j «^-^-j
11
                          g5h3nlg 298/11                         getlCgD 177/14           gost I bristag 103/2
fravahr 131/8
                         gam 300/9                               getofrld 179/18          gosurvan 333/7
fravar5n5 133/2
                                                                 getog xrid 180/8         gosurvan amahraspanc
fravardlgSn 133/8-141/16 gan 302/20
                         ganag 210/9                             geto xrid 179/7          gosvar 334/1
fravardln 133/14
                          gSusda 302/8                           girad 182/16-265/5       gov 325/12
fravastag 132/20
                          gac 310/18                             girand 182/20            goved 325/19
fravas 133/1
                       
#### leaf 234
                                                        tf*V* tf**^ *-jrf
15                                            U-U.j'i

                                                        evar 93/10                   fraz barisn 136/14
dvarfid 307/15-327/20     £ r3y 224/20
                                                        evbar 91/2                   fraz burd 136/13
dvSrist 308/13-327/21     erbad 88/5
                                                        evenag 94/7-10               fraz guft 136/16
dvarisnlh 327/18          erbadan 88/9
                                                        evgad/ebgad 85/22            fraz rasisnlh 136/18
dvazdah 292/7-326/16      erbadistan 88/14
                                                        evirist 94/5                 fraz ravfid 136/11
                          erbad-z3d 88/10
                                                     
#### leaf 235
 13                                        Uu^ teub.fy
                                                         i5p« i5^*»3^ ,Sm *-*
dandan frisn 340/1-3        debSg 313/9                  dil 225/6                  drust 339/9
dandSn fris post 339/19     deh/dih 242/10               dist 313/11                drustih 339/12
dar 100/2-9                 d§n 192/18                   do 149/13-307/9            druvasp 336/15
dard 320/7                  den 188/17                   doan 327/6                 druvand 324/15
dar 1 dusax v 100/8         den5g5h 189/23               do hazar 307/20            druvandan 324/18
darg5h 321/14               d§n ahramogth 193/7          dol 328/9-335/15           druvandth 324/19
dar I s3hg5h 100/6          dSn bandag 190/9             dolraanagC?)      336/10   druj/druz 323/2
dar   I   iahr 100/7        denbarSn 190/5               dopaykar 329/12
#### leaf 236
 i   I                                            V'J   tfi^tfwj'j ^-^t-*

 caanlg 157/4              cegOn/ciyOn 161/12           dSdistSn 189/6-295/18     darisnlh 299/20
 casnlg kardan 157/6       cS gOved 247/15              dSdistan Bmandlh 295/20   d3sr/d5sar 298/12
 cast 156/19               ce-h3d 247/9                 dSdvar 296/2              dasran 298/16
 cSstag 156/13-157/1       ce-h«t 87/1                  dadvaran 296/7            dast 298/17
cahflr40/5-48/10-155/11    c5-m3n 247/13                dadvar I drozan 296/5     daltan 299/1
cahardah 304/12           c6-man handaxt 247/13         dadvar tar 296/8          daltartar 298/23
cahardahum 156/4          ce-I 247/10                   dam 300/6                 dast ested 298/22
cahar payan 155/13        cihr 62/19rl60/l3             dam dad 301/10            dayag 306/1
caharura 156/1            cihrab 160/17          
#### leaf 237
                                                                        ^

                                             Ln-L.jlj   ^^Jy^^UajljO—


bazay 97/4               bavandaglh 110/16              boxtan 106/5              bulandtar 109/6
bahr 96/9                bavandagtar 110/14             b5xted 106/8              bun 109/20
ba$ /bag/bay 101/7       bavSd 303/22                   boxtisn 106/2             bun-is 110/9-195/9
ba^an 101/6              bavSh 303/20                   b6y 111/1-6               bun kardag 110/7
baj baxt 101/16          bavSnd 303/18                  b5y   I   p3k 111/5       burd 185/14
                         bavisn 304/1                   bSzSh 107/13              burdan 108/16
ba^   yasn 99/18
band 110/18              baxsiln 97/19                  b5zisn 107/18             burdar 108/13
banded 33/6              baxt 97/10-11                  boz
#### leaf 238
                                              U-Uft                    ^-^J
                                                      is*1*-* \s\**&

 anoh/anocf 149/15        arsisvang 43/2
 anosag 75/16                                          astar 35/17             ayab/aya 91/4
                          arsisvang I hucihr 43/6
                                                       astar burdan 35/19      ayadenisn 84/20
 a-padixsS 13/2           artestar 41/14
 a-padixs5-tar 13/4                                    a-tarsagah 27/14        a-yosdahr/a-y5zdahr
                          artSstaran 41/18
                                                       a-tavanlg 27/17         a-ySsdahrlh 91/17
 a-pSdyab 13/11           arz 277/18
                                                       avara 14/8
 apflr/appar 14/2         arz 42/1                                             aySxsust 93/5
#### leaf 239
                                                   U^bo'j   i$}kl <***•& e-j^
 "

                                                            ahravtar/ahlavtar 5/12   an-ahOg 56/8
,i   <\   I.   Tm 25/2          afganSd 228/13
                                                            ahriman/ahrraan 4/17     anar 59/3
 i.a-dld          18/16-20/12   afganend 228/11
                                                            ahrraog 4/9              an-asanlh 58/11
nhft-rjumfln           20/12    afganisn 228/15
                                                            ahunvad/ahuved gah 8/6   an-afsudag 56/20
abfi-mOzag 25/18                afroxtan 21/21
                                                            ahuvar/ahunavar 7/18     anayran 80/11
abfir          25/12            afrBzend 22/9
                                                            ahyas 9/10               an
#### leaf 240
                                                     ,U 4.1**11,
                                                                   tf>V< *s^*J i ^J+*
                                                                               l




agShlh 38/13                apus 24/2                               atas I vahraro 27/6      abayisnig 16/2
agSh-tar 38/10              5pus bavSd 24/5                         ataxl/atas 26/16         abaz 223/20
Sgrift 88/16                apustan 24/7                            Svar3d 305/16            abaz axezend 220/11
agust 39/9                  5n-iz 63/22                             Svardan 305/7            abaz axezenend 9/8
Sgust ested 39/14           arSyfid 40/1                            Svared 225/13-305/2-13   abaz ayend 296/21
3han/ahSn 7/13-34/17        3rd 210/1                               avarfira   305/10        abaz banded 33/10
ahan
#### leaf 241
                     (   tf>M^U\s-jli ^l**j|j c**j*i




5   83/8                             abustanih 20/9
3b 12/9-251/8-252/22                 ab zSh 155/9
3bad 12/19                           ab zShr 251/21
abadanlh 12/22                      adur/atur 27/19
abadag 13/9                         adurbad I raarispand 28/7
abfld-tar 13/6                      adurbad 1 marispandSa
abad-xlrih/herlh 13/7                  28/4
ab3n (1) 14/14                      adurbad I zardustan 28/9
       (2)
ab3n         14/19                  3dur fambajf 28/15
abgGnag 20/11                       adur farnba^ narse 28/11
3b 1 cah 251/18-19                  adur I burz 108/9
3b 1 fistadag 251/23                aduristar 28/13
ab I vSh 251/20                     adur Ohrraazd 28/2
abistan 20/6                        afrln 23/8-24/17
ab ud gOmSz 251/16                  afrln kunSh 23/12
abus/apus 24/2
```


## [2026-09-07T16:20:59.912Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\noff=sum(len(l)+1 for l in lines[:15383])\nprint('leaf', d[:off].count('\\f'))\nEOF\necho \"---\"\npython3 - <<'EOF'\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (229,230,231,232):\n    print('#### leaf',i); print(d[i][:1200])\nEOF",
 "description": "Find SNS Avestan index leaf"
}
```


### [2026-09-07T16:21:01.228Z] TOOL RESULT

```
leaf 215
---
#### leaf 229
25                                               Li;^Li*.L y>   ^At tfl**;'* ^-vr»
mahraanih 239/14             mazdist 241/17                     raiySnag 237/12           naxun 258/3
Mahraspand/Maraspand         raazdistan 241/20                  raizag 253/6              nSyrlg 264/19
  240/8                      raazg     243/18                   ra5g   248/1              nayrlg zan 264/24
ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
man 221/1                    mShan 252/17                       ra&r   3sy3nag 248/8      namad 282/5
raang 248/2                  raSnisn 254/17                     raSrcag 248/10            naraak 282/7
man-iz 233/4                 raSniinlg 254/24                   mSristan 248/18           narab   282/2
raanuyscihr 240/20           mSniinlha 254/22                   raBy 249/22-24            nar 164/10
ma Bzan 39/21                raSnCg 255/1                       mOyfin 250/22             NarsSh Burzmihr 283
raar    244/23               mfinCgan 255/9                     mCylh 250/21              nasay/nasa 272/20
raard 308/2                  ra6nCg I     3b 255/7              mGzag 2
#### leaf 230
23                                    .—_*L>; d—^U a.L«;I3
                                                             tf^dkgye-tj**
kaned 22/11-14-16        kS-s3n 249/18                        kun&n 266/5            mahm3n 237/1
kanend 22/11-14          k5-t 249/13                          kun§nd 219/14-266/9    mahraantar 237/5
kaplg 210/15             kih 211/15                           kunlhfid 266/6         raahraspand 240/17
karcang 214/6            kihSn 211/17                         kunisn 219/1-266/7    m3h yast 236/10
kard 217/4-265/23        kihist 219/17                        kunisnan 219/7        maiisn 239/11
kardartar 213/18          kira 220/8                         kunisnlh 219/9          -man 230/16-20
kardag 213/19-22-217/1- 2 kimist 220/9
                                                             kust 217/19            raanad 211/4
kardag kardag 213/24      kirfag 216/11                      kustag 217/22          mSnbad 240/4
kardan 217/16            kirfag handOzIh 81/19-              kustlg 218/1           manbadan 240/7
kard baved 266/2           216/14                            ku-I 87/17-195/6       raandag 241/3
kard Isted 266/3         kirfaglh 
#### leaf 231
                                                               >s*K* ts^j'j c-.^j
 21                                       L-*.   b c L jj j
                                                         l




hilisn 206/1                                                   jSvSd3n 304/8             k3hSd     208/1
                        husangd 65/14
hist 205/18                                                    jagar 317/6               kahisn 208/5
                        husparam 65/18
histan 205/8                                                   jahud/yahud 302/4         k3m 209/18
                        husravlh 66/18
histan abayed 205/14                                           jast 314/1                karaad 209/21
                       hus/us-bara 67/2
hixr 84/7                                                      javisn 341/15             karaag 210/3
                       hu-xfimS 60/6-89/12
horn   72/9                                                    jiv 188/23                kara akaraay
                       hQxt 56/22                                                                       39/1
horaast 72/16                                                  jOrdag 335
#### leaf 232
                                     li;   c—rfU **U *3'j   isA* i5U»;'j c-«J
11
                     hat 2/5                                hamSsag 54/1            har bar 98/6
gugan 335/7
                     havandlh 8/4                           hara-giyag 54/20        har evak 92/2
gugard 335/5
                     havand/havind 7/21                     hara-gOnag 54/15        harven 45/15
gugard ested 335/6
                     havist 7/7                             ham-gum5zisnlh 54/13    harvisp 45/2
guman 337/6
                     hflvistan 7/9                          ham-kar 51/10           harvisp 3gSh 45/7
gumanig 337/8
                     haft 16/7-84/14-197/9                  ham-karzag 51/11        harvist 45/10
gumSrSnd 337/3
                     haftad ud s5(h) 315/8                  hara-karzaglh 51/13     hast 74/3
gumast 337/4
                     haft amsaspand 16/11                   hararais   210/11       hast 84/17-152/9
gumbad 337/9
                     haft kisvar 16/13                      haraogen/hamoyen 90/6   havasSnd 60/16
guraSxt 338/1
                     haftOyrang 17/3                        hara-pursaglh 50/1      havSsIdag 60/15
gumSzag dad
```


## [2026-09-07T16:21:11.670Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"nuysc\\|nuscihr\\|uyscihr\\|manuys\\|Manuys\" SNS_pages.txt | head; echo \"=== manu\"; grep -n \"^manu\\|  manu\\| manu \" SNS_pages.txt | head -20",
 "description": "Grep SNS for Manuscihr"
}
```


### [2026-09-07T16:21:11.728Z] TOOL RESULT

```
16020:raanuyscihr 240/20           mSniinlha 254/22                   raBy 249/22-24            nar 164/10
=== manu
```


## [2026-09-07T16:21:25.325Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"منوچهر\\|منوش\\|مینو\" SNS_pages.txt | head -10; echo \"=== Avestan index leaf 215\"; python3 -c \"\nd=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(d[215][:800])\nprint('#### leaf 214'); print(d[214][:500])\"",
 "description": "Grep SNS for Manuchehr in Persian"
}
```


### [2026-09-07T16:21:26.666Z] TOOL RESULT

```
=== Avestan index leaf 215
                                                   &b*j* *st**3'j

                                                   anaSsaijh 75/18               arraa§-sta- 44/14
                                                   an-ajra- 80/13                aritat 35/15
                                                   aniya- 94/1                   asan- 193/16-313/15
                                                   an-us2ivant- 191/4            a-saya- 174/21
                                                   angusta- 82/2                 ast- 31/4
                                                   antara- 80/17                 astvat-/astvant 31/1
                    ^U-jltfl*^^-**                 antara 188/7                  aspa- 192/1
                                                   afitar
#### leaf 214
                                         U; c-»l: *-b *jl 3   j^^-j ijU.jl^c-^J
                                                                   1




55
                                                              kusaiti 218/6            x v a5tvada0a 78/12
atar/atars 26/19        us- 66/22
                                                              khan- 7/11               xv aini 59/22
5tar/50r 27/19          usah- 67/3
```


## [2026-09-07T16:21:50.147Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/WLD/; echo \"=== grep WLD Bd2 for men- denken\"; grep -n \"denken, geistig\\|men- 'denken'\\|men-  ,denken\\|manu-s\\|monu-s\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Grep Walde-Pokorny Bd2"
}
```


### [2026-09-07T16:21:50.201Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== grep WLD Bd2 for men- denken
```


## [2026-09-07T16:21:55.363Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mendh\\|men-dh\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== manus\"; grep -n \"manu-s\\|mánus\\|manu- ,Mensch\\|Manus-cithra\\|Manus-ci\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== 264\"; grep -n \"denken.*geistig\\|geistig erregt\" incoming/WLD/WLD_Bd2_pages.txt | head",
 "description": "Grep WLD Bd2 for mendh / manus"
}
```


### [2026-09-07T16:21:55.437Z] TOOL RESULT

```
16402:8. u.  mendh- „einen Sinn worauf richten"') nach Medermann JA. 18, 81.
17229:    s. u. ^mendh- „seinen Sian worauf richten*'); desgleichen alb.       „Spitze,
17744:270                                       menth-   — mendh-
17832:mendh- „seinen Sinn worauf richten, angeregt, lebhaft sein‘‘.
17860:   Idg. men-dh- ist Erw. von men- „denken“, genauer wohl Zsrlickung
17861:men-dhe- „den Sinn worauf setzen'S vgl. ai. man[*3~\-dhatdr- „der sinnende,
17865:^ma-dh neben "^men-dh (wie g'^a g'^e^n) zu schlieBen (Boisacq s. v.), ist vor-
17942: Wz. *mendh- „seinen Sinn worauf richten“, zu stelleui.
=== manus
=== 264
17322:3.     men- ^d^nken, geistig erregt sein“;
17847: ahd. mendl, mendan zu "^menth- ^schiitteln, quirlen''— „geistig erregt sein“);
```


## [2026-09-07T16:22:00.049Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17832,17870p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=====MEN3 WLD\"; sed -n '17322,17345p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== MOUSA in WLD\"; grep -n \"Mo?joa\\|Movoa\\|Mouoa\\|Muse\" incoming/WLD/WLD_Bd2_pages.txt | head",
 "description": "Read WLD mendh- and men-3"
}
```


### [2026-09-07T16:22:00.144Z] TOOL RESULT

```
mendh- „seinen Sinn worauf richten, angeregt, lebhaft sein‘‘.
                                                       av. mazda, mazdtih-
    Ai. niedhd „Wei8heit, Einsicht, Yerstand, Gedanke‘',
n. „Gedachtnis,Erinnerung*^ mazdah- m. Name des hochsten Gottes i^maz-
dha aus ^nnidh-ta, Lit. z. B. bei Scheftelowitz IP. 33, 163); gr. jnav&dvoj
                                            menes-                                          ^71

 (nachgeborenes Praes. zu)       /na'&'tjoojuai^   fia&sTy „lerneix'*, dor.-aol. jud&r], jon.
 jLid^og, n., jon.-att. jud^oig   „Lernen, Unterricht'',                  „Stim;      (pQovTig^^;
 YieWeicht Movoa {*jLiovd'ia; von Pick KZ. 46, 82 nach Platons Kratylos als Ptc.
 von /iio^G&at   —s. me- „lieftigen Willeiis sein^'    —
                                                    gedenkt, „der siniiende Geist'^
 ursprgL die Schutzgottin der pierischen Sangergilde am Olymp, doch be-
 deutet            „streben'', nicht „sinnen''; Wackernagel KZ. 33, 571 erklarte
 es als ,^'^montia Bergnympbe''; nicht nach Ehrlich KZ. 41, 2S8 samt jnevd}]Qrj,
 ahd. mendl, mendan zu "^menth- ^schiitteln, quirlen''— „geistig erregt sein“);
   alb. (G. Meyer Wb. 291, Jokl SBAk. Wien 168,158 mimd „kann, siege“);
   got. niundon sis „einen besehen, sehen auf', mundrei „Ziel“ (liber das
 vonOsthofflA. 15, 104 angereihte germ,                „Schutz“ s, u. mdr „Hand“)-
 aisl. mimda „zielea (Waffe), einem Ziele zusteuern“, ahd. muntar „eifrig,

 behende, munter^ muntari „Eifer, FleiB“; ahd. mendi ,,Freude“, menden, as.
 mendian „sich freuen“ (stammt lit. mandagus „anmutig, anstandig'" aus
 einem germ. *mandaga 0 „erfreulich‘' ? Mit lat. rnundus und (?) ai. manda-
 yati „schmuckt'‘ hat es kaum etwas zu tun, s. u. men- „feucht“); lett.
 mudu, mujchu^ must „erwecken'‘, lit. mundriis^ mandriis „munter, iiber-
 mutig“; abg. mad)^ „weise“.          Curtins 31 If., Meillet      De indoeur. rad.
 41 f. (Lit.), Fick III^ 308.
   Idg. men-dh- ist Erw. von men- „denken“, genauer wohl Zsrlickung
men-dhe- „den Sinn worauf setzen'S vgl. ai. man[*3~\-dhatdr- „der sinnende,
andachtige'S ao. mqz-da- „dem Gedachtnis einpragen'^ (davon mqzdra- ver-
standig, weise“j.      —
                      Yon gr. TtQojurj&i^g „vorsorglich'' (dor. -d-) auf ein idg.
^ma-dh neben "^men-dh (wie g'^a g'^e^n) zu schlieBen (Boisacq s. v.), ist vor-
                                        :



eilig und eine innergriech. Erklarung abzuwarten (""Ttgoiid^rjg mit Dehnung
=====MEN3 WLD
3.     men- ^d^nken, geistig erregt sein“;
            Basen men-, mend-, mene{i)-                                 (s.    dazu J. Schmidt KZ. 39, 40, Persson
            Beitr. 648, 731).
      Ai. mdnyate „denkt“,                         av. mainyeite ds.,                         ap.     mainyahay        (idg.
= gr. ixaivo}xai, air. -muminr, slav. m%Y q ^menl- *m^ne-^ s. u.), ai. Pf.                ;                 :



ma-mne, mme (aus letzterm das Praes. mind, menati „meint'‘ aus ^menyat%
s. u. moln- „meinen‘‘); manmj-ati ,,ist eifrig^', mana-yu- „eifrig, fromm‘%
wmwo-sa „Weisheit, Yerstand; Andacht, Gebet“                m^ni-) ai. mamitt                                     \
                                                                                                                         \

„denkt'' mcinati „erwahnt'‘ (= lit. menu, poln. -mione, cech. -menu^ Zubaty
                  ;


AfslPh. 15, 497 Anm. 1, Meillet De rad. 7nen- 15, Jensen KZ. 39, 590 f.,
Persson Beitr. 731); ai. mandyati ,,ehrt, erw^eist Ehre'^ (in der Bed. beein-
fluBt von 7nana- m. n. „hohe Meinung'' s. Brugmann II ^ 1150; o-Stufe wie
in     lit.    isz-monis            „Yerstand‘',           Brugmann II ^ 3,                         246), av. mcinaym „man
konnte glauben“; Sup.                       Si\,   mdntum, ppp.                                   „gedacht‘' (=gr. amo-fjiaxogy
lat.        conmieyitus,          lit.   mintas,        air.    der met)       \

=== MOUSA in WLD
9405:bei Kern Museum 10, 18f.), bhujissa- „freigelassen (von friiheren Sklaven)"
17841: YieWeicht Movoa {*jLiovd'ia; von Pick KZ. 46, 82 nach Platons Kratylos als Ptc.
```


## [2026-09-07T16:22:21.006Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 manu-s 'Mann'\"; grep -n \"manu-s\\|manu- „Mann\\|Mannus\\|manwaz\\|manu-, monu-\" incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== WLD lat mens\"; grep -n \"mens, -tis\\|mens,-tis\\|mens, gen. mentis\" incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== IEC men\"; grep -n \"^men- \\|^mendh\\|^manus\\|^manu-\" IEC.txt | head -20\necho \"=== SYN mind\"; grep -n \"17.11\\|MIND\" SYN.txt | head -10",
 "description": "More greps: WLD, IEC, SYN"
}
```


### [2026-09-07T16:22:21.090Z] TOOL RESULT

```
=== WLD Bd2 manu-s 'Mann'
=== WLD lat mens
=== IEC men
10322:manus (man-, manustios) *man, human be- ing, husband’. (Prob. distinct from type monus ‘thoughtful’, q.v, and from type monuos “single, individual’, q.v. The Breton forms indicate *-a-). WP II, 266 Skt. mánuh ‘man’; Av. cf. Manus-CiOró (a name); Oss. moi, pl: måitta; Dig. moiná (“man, husband'. Loss of *-n- as in mäi *month"); Arm. cf. manc, gs manu, ab. s. manéov (boy': cf. Skt. manusyáh; Romani manus, m. man); Tokh. A māññe, B mafiiye, mafiye ‘servant, slave’; Phryg, mánes, id.; Gaul. cf. -mannus (in names: Catu-, etc.); Br. màn, m. (person,
=== SYN mind
2551:Delbriick, Die indogermanischen Ver- wandschaftsworter. Schrader, IF 17.11 ff. and Reallex., S.v- Familie. Tappolet, Die romanischen Verwandtschaftswé6r- ter. Wiedermann, BB 27.205 ff. Her- mann, Gétt. Nachr. 1918.204 ff.
19067:tagtnoee Mt. 17.11, daoxatioré Mk. 9.12), also ‘prepare, bring into order’, epd. of strojiti ‘prepare, arrange’.
27536:For Grk. ¢pjv, poet. word for both the seat of emotion and ‘mind’, with nu- merous derivs., partly of emotional but more commonly of intellectual charac- ter, see under ‘mind’ (17.11).
27546:Goth. ahma (= zvedua) : aha ‘mind’, etc. (17.11). Feist 16 f.
27737:SCr. éudenje, fr. vb. Guditi se ‘wonder’ = ChSI. éuditi se id., fr. ChSl. éudo, etc. general Slavic for the obj. ‘wonder’ (rare or dial. for the feeling), this : éuti ‘per- ceive’ (17.11). Berneker 161.
27845:ON hugna, fr. hugr ‘mind, mood, de- sire’ : Goth. hugs ‘mind, understanding’, etc. (17.11).
28455:Grk. db0-¢pwv, cpd. of dve- ‘ill’ and ~$pay AS IN o-ppwy ‘wise’, etc. (: dpfy as seat of thought and feeling, 17.11), hence ‘ill-disposed’ and also ‘sad’.
29452:Lat. vb. mentiri ‘lie’ : méns, mentis ‘mind, intelligence, thought’ (17.11), with semantic development perh. through ‘say something thought up, invented’ (cf. also the cognate OPruss. meéntimart ‘we lie’). Walde-P. 2.270. Ernout-M. 606. Hence the sbs., Sp. mentira (fr. vb. mentir) and, through VLat. derivs. (*mentionia, *mentio), It.
30146:CHAPTER 17 MIND, THOUGHT
30152:17.11 MIND Grk. vols Goth. aha, frapi, hugs Lith. _protas NG vods ON hugr, munr Lett. gars, prats Lat. méns, animus Dan. aand, sind ChSl. um It. mente Sw. sinne SCr. um Fr. esprit OE mod, hyge, gewit(t) Boh.  mysl Sp. mente ME ~~ mode, mynde, (i) wit Pol. umyst Rum. ‘minte NE mind Russ. wm I. menme, intinn Du. geest, zin Skt.  manas-, citta- Nir. aigne, intinn OHG muot, sin, hugu Av. manah- W. meddwl MHG muol, sin, huge Br. spered NHG - sinn, geist
```


## [2026-09-07T16:22:28.214Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30152,30190p' SYN.txt | fold -w 170 | head -50",
 "description": "Read Buck 17.11 MIND"
}
```


### [2026-09-07T16:22:28.263Z] TOOL RESULT

```
17.11 MIND Grk. vols Goth. aha, frapi, hugs Lith. _protas NG vods ON hugr, munr Lett. gars, prats Lat. méns, animus Dan. aand, sind ChSl. um It. mente Sw. sinne SCr. um 
Fr. esprit OE mod, hyge, gewit(t) Boh.  mysl Sp. mente ME ~~ mode, mynde, (i) wit Pol. umyst Rum. ‘minte NE mind Russ. wm I. menme, intinn Du. geest, zin Skt.  manas-, 
citta- Nir. aigne, intinn OHG muot, sin, hugu Av. manah- W. meddwl MHG muol, sin, huge Br. spered NHG - sinn, geist
‘Mind’ is intended here as the seat of intelligence, parallel to ‘soul, spirit’ (16.11) as the seat of emotions. But, as already remarked in 16.11, the two groups
 overlap. Several of the words there listed may cover also the ‘mind’, and conversely many of those in this list cover mental states in the widest sense, that is, may
 be used with reference to feelings as well as thoughts, as Lat. méns, Skt. manas-, Grk. vois (rarely), OE mod, hyge, NE mind, etc.
Apart from those discussed under ‘soul, spirit’, most of the words for ‘mind’ are connected with verbs for ‘think, understand, know’, or the like, and many of
 them are used also for the mind’s activity, ‘intelligence, reason, thought’, etc.
The actual physical seat of the mind in the brain, though recognized by some of the Greek philosophers (Plato, but not Aristotle, who favored the heart), was not generall
y enough known to have any effect on linguistic usage, except in mod- ern phrases like NE has brains, has a good head = has a good mind, NG éxeu pvadd ‘has good sense�
��, éxace 7a pvadé Tov ‘lost his head’. It was rather the vague dpe ves (cf. below) that affected the ter- minology.
1. Derivs. of IE *men- in Skt. man- ‘think’, Lat. memini ‘remember’, etc. Walde-P. 2.264 ff. Ernout-M. 606. Walde-H. 2.69 f.
Lat. méns, mentis (> It., Sp. mente Rum. minte); Ir. menme (NIr. meanma, but not the usual word for ‘mind’); ON munr (also ‘longing, love’, OF myne ‘de- sire, 
love’, rarely ‘mind’, Goth. muns ‘thought, intention’, etc.), ME mynde, NE mind (OE gemynd ‘memory’); Skt. manas-, Av. manah-.
2. Grk. voos, Att. vods, whence voew ‘perceive, notice, think’, etc., vénpa ‘thought, purpose, understanding’, etym. dub. Walde-P. 2.324. Boisacq 672. Schwyzer, 
Festschrift Kretschmer 247 ff. For the technical uses, Schottlaender, Hermes 64.228 ff.
Grk. ¢pnv, esp. pl. dpéves, in Homer when used in lit. sense (with reference to wounds) hardly ‘diaphragm’ in the strict sense, but rather as if membranes inclosing
 the vital organs (heart, liver, etc.); hence a vague general term for the vital organs and most frequently in fig. sense ‘heart, mind’ as the seat of both emotion an
d thought—in this sense mostly poetic, but important for the large group of derivs., in some of which the thought element is dominant, i gpove ‘think’, gpovris ‘t
hought, ane ot-@pwv ‘of sound mind, wise, pruden (but also ‘of restrained senses’), 10 a the emotional, as «b-ppwv ‘cheertu’s
Eee yas baa dden’. Etym. merry’, eippaivw ‘cheer, glad 37 dub. Walde-P. 1.699. Boisacg 109/™
oi Jso 3. Lat. animus ‘spirit’ (16.11) 4
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pind Fr. esprit ‘spirit’? (16.11) also
(pin? ove, l.
4, Ir. i ‘spirit, desire, inten-
Cea fr. aigneadh, Ir. atcned ‘na- tion » ; ye epd. of ad- and the root in he make’, Lat. gignere ‘beget’, ig | aren ‘be born, become’. Walde- Gur y16, Peders
en 2.54, 534 ‘Jr, intinn ‘intention, purpose.» but also in certain phrases ‘mind’, fr. Lat. intentiO. Pedersen 1.234. Vendryes, De hib. voc. 147.
W. meddwl, orig. ‘thought’, vbl. n. to meddwl ‘think’ (17.13).
Br. spered ‘spirit’ (16.11), also ‘mind’.
5. Goth. aha (reg. for vois), beside akjan ‘think’ : ahma ‘spirit’, OHG ahta Gntention, consideration, notice’, OE eaht ‘deliberation, council’, OHG, OS ahi
on ‘consider, take notice of, estimate’, ON @tla ‘think, intend’, outside connec- tinsdub. Walde-P. 1.169. Feist 15.
Goth. frabi (sometimes for vods, but mostly ‘thought, understanding’) : frap- jan ‘understand, think’ (17.16).
Goth. hugs (vots Eph. 4.17), ON hugr (Dan. hu, Sw. hég more nearly ‘mood’, except in certain phrases), OE hyge, OHG hugu, beside Goth. hugjan, ete. think’ (17,18),
 deriv. Goth. gahugds (reg. for dtavora, also vods Rom. 7.25, and ovveldnos 1 Cor. 8.12, etc. : OE aehygd ‘thought’, OHG gihugt ‘memory, Palen ctym. dub. Walde-P, 1
.378.
Ome 2k E. Feist 272, fy mod, ME mode, OHG, MHG i edad mind’ in intellectual sense,
te often with emotional value (cf.
m
MIND, THOUGHT.
Digitized by Arya Samaj Foundation Chennai and eGangotri
1199
NE mood ‘state of feeling’, NHG mut ‘courage’) : Goth. mops, ON moor ‘an- ger’ (16.42). ;
OE gewit(t), ME (i)wit, also ‘intelli- gence’ (NE wit), and in the latter sense ON vit, OHG wizzi, MHG witze (NHG witz) : OF witan, OHG wizzan, Goth. witan ‘know’
 (17.17).
OHG, MHG sin, NHG sinn, Du. zin, MLG sin (> Dan. sind, Sw. sinne), also and more orig. ‘sense’ (15.11).
Dan. aand ‘spirit’ (16.11), also ‘mind’.
Du. geest, NHG geist, orig. ‘spirit’ (16.11).
6. Lith. protas, usual word for ‘mind’ and ‘reason’, Lett. préts mostly ‘intelli- gence, understanding, reason’ (OPruss. pratin acc. sg. ‘counsel’) : Lit
h. sw- prasti, Lett. sa-prast, Goth. frapjan ‘understand’, etc. (17.16).
```


## [2026-09-07T16:22:39.013Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 2.21 MAN\"; grep -n \"2.21 MAN\\|^2.21\" SYN.txt | head -5\necho \"=== LEW mens\"; grep -n \"^mens\\|mens,  *-tis\\|^moneo\\|^monstrum\\|^Musa\" LEW_1910.txt | head -10\necho \"=== LAT mens\"; grep -n \"^mens\\|^moneo\\|^monstrum\\|^Musa\\|^musica\" LAT.txt | head -10\necho \"=== BRT mazda\"; grep -n \"mazdā-\\|mazdāh\\|mazda-\\|Manuš\\|manuš\" BRT.txt | head -20",
 "description": "Greps for Buck MAN, LEW, LAT, BRT"
}
```


### [2026-09-07T16:22:39.114Z] TOOL RESULT

```
=== SYN 2.21 MAN
2281:2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
=== LEW mens
=== LAT mens
3938:menstrua mouqjat", cf. Isid. 17,7,7 et Sofer 117 et 176; ex-animus; ex¬
4794:mensura continetur, finitur secundum antiquam obseruationem fluminibus,
6434:mensibus | Prius olfecissem quam ille quicquam coeperet. De la, a basse
7827:menstruus (-is codd .) uenit; compos£ inbubino dans Lucilius.
12512:moneo. M.L.7i33a. De IA reclinatorium: dossier, reposoir (Vnlg.).
21229:mense sacra fiebant, eiusque feriae erant Lupercalia, quo die mulieres
37334:mens, cf. skr. matih "pensee", 1'autre, de type italo-celtique, mentio ,
37404:mens, je ne dis pas la vdritd", par une litote analogue. De meme les
37522:mensis, -ls m.(ancien theme consonantique, muni d'un nominatif
37531:mensa spatia conficiunt, menses nominantur. Le pl. menses designe
=== BRT mazda
3627:•  j.  apa-stütay-  f.  'das  Sichabgeloben, Abschwören':  yä  haca  damayat  mazda- yasnSii  'Biiis  "das  Abschwören  dei  mazd. Religion"  N.41.
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
5904:•  j.  asnvant-  m.  Name  eines  Bergs  oder Gebiigs":  ahmat  haca garays  fraoxsyqn.. 'väsca  Yt.  //).  5;  —  "vanlitn  gairJm  masda- <iSt)m  S.2.9;  —  'vaniahe'^  garSts  mazda- oätahe  Ny.5.5.
7939:chen (ausgesprochenen)  Gegensatz;  i)  ad- jektivisch; öfters  sva,  'dieser  mein,  dieser unser*:  ^  ya'iä  avatnc^  °mäm  bümim  .. D.  ().4;  —  VTspqmäi  aipi  °mqm  zqm  Y. 37-P3;  V.2.io,*ii,  >i2,  j^;  5.25;  — -ma  apasca  z>masca  urvarasia  .  .  'mä asasla  sßiiräsäi  ..Y.  2.16;  S.l.aS',  2.28'; —  D  'mäm  dahyäum  a*ur^mazda  pätuv  . . abiy  'mam  dahyaum  ma  äjamiyi/'  .  .  D. 4-3',  Ao.j;  —  mäm  c^ur^mazda  pätuv , .  utamaiy  vtiam  Uta  'mam  dahyäum  D. tf.  S;  —  Äauciy . .  nirasätiy  (sd.)  abiy  'mam !'/5  am  D.  5. 3 ;  II  —  ma  yave  'ma^  nmantm .  .  ifanns  /rasa Alt  Y.  60.  7;  Vyt  (?;  — II  'mam  duvariim  .  .  adam  akunafam  X. 7.3;  —  °Mi<i*  Aadis  X.^.3,  4-3,  Am._5  (wo 'mam);  ^-j  —  '■mam  lacaram  D,  i;  — ^'mam  ustasanam"  {sd.)Ao.  1.2; — "'mam apadana*'^  (sd.)  Am.  i,  4;  —  'ma*  stäiiam (sd.)  Aauv  niyaitayt^  ka'lanaiy'X^y.y, — adam  niyaslayam  °mäm yuiiyäm  keCtanaiy D. /7;  —  tuvam  ka  hy^  aparam  'mam dipim  vainsAy  .  .  'maiva  patikani  Bh.  4. 'S;  ^6"i  17',  6.  8;  —  'mam  Aa'dugäm Bh.^.io,  11;  5.3(?);ll  —  yat  'mam  daz- nqm  astaotaYt,iQ.%w — A3  damqm  mazda- yasttim  fravaza  vazaite  AS  'mqm  datnqm
8147:Undeutlich:  hauanröpam  (sd.)    mazdai 'oqm    F.  24.         [FrW.  g.  i :    lies    mazda-
9643:•  j.  ku'*a  Adv.  1)  'wie?':  k-'  nanm  asa- vatum  yaozdaküni  V.ig.12;  12*,  70.1, It.i'*,  J2,  a',  Yt.^.4',  SO.121;  —  k°  /iTs awm  Jijffnav<lni\.ig.\2,Yti~.^T.  a)mit li  (sd.)"';  i°  tg  v>rttyqn  alte  yBi  mazda- yasna  V.5.  10,  39,  45,  6.6,  36,  28,  tV,  i, 4,  73.  y-29.  35.  36.  J546.  Jö-i;  —  aal yimS  mqsta  k'  ti  as?m  vanm  k}r>naväne V.  2. 31;  22.6'.  A)  frageeinleitend,  mit Z^':  k*  ti  aae  masdayasna  aihm  ätnm aiii  baran  ava  . .  'Svie?  sollen  die  M.  das Feuer  (wieder)  hinbringen  zu  .  .?"  V.  5. 41.  z)  'wohin?*:  i°  actqm  baoiö  (sd.) jamiti  V. /j.  50;  —  i'  altdöa  , .  masyäka hqm.valnantei  . .  nanm  a^avatum  "Wohin (sva.  an  wen) . .  sollen  sich  die  Menschen wenden?  ..  An  einen  Gläubigen"  V.fj.  i.
9772:•  j.  gaeiSya-,  gae*ya-'>  Adj.  (fem.  ya-)  sehen  Baums*>:  ma  attmyöahurs  masäa 'stofflich  lebendig,  materiell'«:  vlspqm  ^urvarA  baSsasyä  uz^artm  paoirls  . .  dyum asaom  stm  ..  mainynnmca  '>yamc<i  Y.  '■„im  pairiyi.20.i,;  —  'mm  sünm  mazda- J5.1;  —  asmawm  ..  '■'ihm  ''i^yayn  r^jfy^  Yt.j.30,  S.a.  7;  —  'noAe  sarahe si5is'  Vr.  7.  4;    —    zaraiuitnm  .  .  -är«  I  mazdmätahe  Yt.  i.  30,  S.  /.  7.
11461:•  j.  £istä-  t.  'Erkenntnis,  Einsicht'  (nur Komp.).  A)  mit  razi'tä-  ('die  richtigste Eindchf )  Name  einer  Gottheit,  an  die  Yt.  jä' gerichtet  ist:  Hat  hE  hävSya  anoe  j^azaite rasiftam  °tqm  (statt  NS.)  asaonim  Yt  io. 126;  —  kaxaya  razistayi  'tayä  Yt.  11.  16; V.J^.  39;  —  sonst  mit  mazäalatä-  und asaoni-:  yat  kl  dahat  razista  'la  mazda-
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
18908:'Hausfrau',  uzw.  der  a-4«rischenSchöpfung'': yat  ahtTti  nmane  yat  tnäzäayasnBts  °ka a^ravaiti  .  .  nisAihaj  V,  16.  i;  8;  —  yö 'kayä  ei^ravaihyä  .  .  x^an%>m  frabarät . .  hat  :far>%?m  frabaräli  dva  danar>  . . yesi  nSii  'ka  muruioyat  (sd.)  Y.16.5—7; a'i  13,  14,5.50;  —  yff  'kam  cdravaittm .  .  xhidrä  avi  franhartzaiti  V.  18.  67 ; y  ■  7 ;  —  anySJkaisa  (sd.)  -ka  pairi  xsudrh Jra»^artzaiti  tiik.  2;r;  — yaiAe . .  mazda- yasnanqm  °ka  avaya{%A^  xsudrä  *Aqm.- rai^wayeiti  .  .  ti.li;  —  y3  'kam  yqm apu%rqm  .  ,  xjudrä  avi  fratahrszaiti  V. i^.  8;  —yat  ahmt  nmäne  yal  mäzdayasnöis 'ka  upas.pükirlm  (sd.)  jasat . .  aSdla  alia °ka  la^a  apu%rJm  (sd.)  mjasai  uzuUana V.  5.  45;  59.  7-  70,  7I1  Vd.  igi;  —  yai fiairi.cinaivÄä  jasqn  upa  va  'kam  vä^ayaäa V.  4. 44;  —  'ka  (\AS.)  'kayä  (GD.)  'kanam (GP.)  F.2f.;  —  ratufris  -*'kaya'^  kihrpa N.  sg;  —  a^rS  .  .  av<^a  (sd.)  'kayäi  V. ■'5-4S;  —  naram..  °  rikqm  (GP.?)  Az.i, VytJ;  Vdy;   —   nar^m   va   *'iqm   va
20195:•  j.  mazda-JIata-'l  Adj.  (fem.  'ia-)  'von Maadäh  geschaffen':  vTspa  voha  Ha  (APn.) asacihra  (StvKz.)  Y.  ig.  3  usw. ;  —  vtspäca ääma  Ha  a/at>rir/  Y.jl.6;  —  sav^  °i?m Y.2.14;  /.14,  Ny.^.j,  S,/.9,  2.9;  —  yatäi laoka  ..  Ha  (als  VS£)  V.22.3;  Yti.  21, S. /.  3,  2.3;  —  A<&ra  saoke  -lätle  {\SU) Yt.  1-2. 4;  —  raiaia  vamthi  Ha  (NSf.)  V. /ß.  1 9 ;  S,  I.  5,  2. 5,  VyL j(*;  — ■  sl'arinaTihaca Ha  (IS.)  Ytro.67;  V.J.  i4i,  Ny.5.s',  6, S./.a5-, -'.9',  Yli?.6s,  134,  14.3',  19.9, 13';  —  airyanam  x^ama  'tätanqm  (statt A5n,)  Ny.5.  5,  YtJÄo;  —  v^n^raryrom *t3m  V./5.  37';  —  rumH  urvaire  . .  'laile (VSf.)  V.  jg.  18;  Y.  1. 12,  2. 12,  Ny.  4-  o, N.  7/,  p7,  VyL22;  —  aptmca  HqmH.2.%\ I-  S.  I a.  .?■  3'.  '^-  4.  65. 7,  ffÄ  7,'Yt  y.  53, V.  /p.  35,  Ny.  4.  o',  S.  2. 10,  FrW.  7.  i;  — S/y  V(7  (ASf.)  alaonll  Y.2.  la';  —  ^ii«»- k»r>nahe  ..  °take  Vt.  /.  30;  30,  S.  /.  7,  2.  7;
20201:•  j.  'mazda-yasna-  Adj.  'der  den  Matdäh verehrt,  anbetet;  Anhänger  der  MatJäh- religion';  ya^. .  balsazäi  (sd.)  fratiazsnte.. (taet'ayasnaö&yS  paurvö  ämayayania  ya%a '•naiifyasätV.j.$6i;z6;-^yaiAe..°»atiqm näiriia  avaya  xhtärä  hqm.ras%wayeüi 'nanqtnca  //agvayasnartqm/aH.ii; — naisml daWoS  fravaranS  'nS  tara%usfril  vJäalv5 V.  12.  1;  ö,  8,  Yt  13.  89;  —  fi-ä  gave vtrindyäi  -na  zara'hustrayS  Vr.  4.  2 ;  15.1;
20328:•  j.  *niäzdayasiia-''  Adj.  (fem.  'nä-)  'den MdzdaÄxabeteia  zugehörig  (usw.),  mazda- _)'öj«isch':  'nanqm  vlsqm  Y.  J2.  a.
20330:•  ').  mäzdayaanay-  Adj.  (auch  fem.)  'den .it/aidä^anbetem  zugehörig  (usw.),  mazda- ^arnisch';  i)  von  viir-  f.:  ..Aafnqm  avazSit •nis  avi  vUS  V.  iS.ia;Y.J2.  y,  —  / *avaAia/  vlsai  yat   'nöit   W.ig.iz;
22628:als  Gottheit  verehrten  Fixsterns*':  'nant»m stär»n  mazdahätf/n  Vt.2/.i;  r,Äi3,  /2,»6, Ny.  /.  8,  S.  2.  13;  —  'nantS  stSrS  mazda- oataAe  Yt  21.  o,  2,  S.  /.  13,  Vd.  10 (•nmtS).
23831:Stützung    gewährt' :     ahurahe    matda 'nanhs    Y.  i.  i ;     —     dainqmca     mazda- yamfm  .  .  'nahxm  Vyt  14. Ableit.         —       ■-      ■
```


## [2026-09-07T16:22:48.744Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"manui\\.ci\\|manui\\.\\|Manui\\|manuš\\.\\|manus\\.ci\\|Mänu\\|manu-\\b\" BRT.txt | head -10\necho \"=== mazdah headword\"; grep -n \"mazdäh-\\|mazdah- \\|masdah\\|mazdä-  \\|Mazdäh\" BRT.txt | head -10\necho \"=== 1192\"; grep -n \"^1192\\|1192\" BRT.txt | head -5",
 "description": "Grep Bartholomae for manuš and mazdāh"
}
```


### [2026-09-07T16:22:48.829Z] TOOL RESULT

```
=== mazdah headword
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
6090:rMtlsbTs!  dansaia  urväzä  Y.30,  i;  —  jyS  tr' päl  darfsat  (sd.)  'sa^a  Y.  J2.  13;  —  at m  mit  äais  (sd.)  -Am  Y.  4y.  i  o  ;  —  Hyalins möi  tnraos  's?m  JasB  fräxihml  (sA)  Y. 43.^2;  —  alilye  mos  -sä  (als  Subj.)^ syazäuj (sd.)  Y,_y4.9j  a)  neben  AAtira- Mazdäh:  frS  va  fratsyS  ptazää  'Ifmcä mrsiu (sd.)  Y.4i}.6;  —  iä  uxoa  *mamySus mahyä  niasds  'Säicä  yüstnaibyä  gfntl  Y. ^2.9 ;  —  at  tBi  myatdim  ahurä  .  .  'säila dämä  (sd.)  Y.J^.3;  —  %wa/i»tT  vS  masdä xsa^rSi  °iäicä  sSnghS  viäqnt  (sd.)  Y.  ja. 6;  —  at  räiam  (sd.)  zarakustrB..  daäaitf .  .matdsi.  .°/3i\.J J.  14;  —  ahurS..°sä hazaosS  tnasda  Y.sg.j;  —  .  yim  'üt  vahiitS hasaoltm    ahur^m  yäsä   (sd.)  .  .  Y..  28.  8 ;
6111:als    die    dem  AkaraMazdäh    lanächst    stehende
6848:YLio.69; —  s.nochIIIl3A.       U)  voni  J/flSi/i/^,   MazdähÄhura';    i)  II  im  Ap.:
6871:Am?l'a  (^tvm.,va.ttx A. R-a.)  Sp^nta:  rumas» ts  'ra  mazda  ,  .  rumS  vS  amiiä  spsntä  . . allal  *jih<tt  'r)m  mazdqm  astat  am»si spjnts  Ny.  1. 1;  Y.  68.22;  usw.  b)  im Gegensatz  zu  A/jra(sd.)Mainyav:  xihae- ^ra  "rahe  mazdh  laröidtti  anrahe  main- ySus  Yt./.o;  —  sna>ai  attrahe  maittySuL. /rada%äi  'rahe  mazdiY.2-j.\(.  2  K)aAu- rahe  ma-id?!  (näml.  ayarg)  heisst  der  i. Monatstag:  'rahe  mazda  raivatS..  S,/,i, Y.j.  ii;vgL/6:i,S.2. 1.  3)inGHapt.; 'ra-  ist  einmal  Ci-3S-l)  von  mazdäh-  ge- trennt, sonst  steht  es  unmittelbar  davor oder  dahinter:  huxsa'irS.timüi  ..  xla'hnm .  .  *hvqnmahicii  kyat  mazdäi  'rat  Y.J5. S;  s.  A,_j.  6;  —  mazdil  'rä  . .  kätqm  hu- dsslfmä  \.4i.  2, 4;  —  'rä  mazda.. vaahuda YjA'.4;—  vohü  xsa'hr»m  tsi  mazdä  'rä apaSmä  Y.^/.  a;  —  sralstqm  at  tSi  k»hr- pSm  .  .  ävaSdayamahJ  masdä  'rä  . .  avat yät  hvar!  aväcl  V.j6.6;  — yäsctJ  tsi gmä  *'ra.mazdä^''>  Y.  j8.  i;  ^5.  3,  9;  — hyat  mizdjm  *mafai^im  (sd.)  Jradadfiä .  .  masdä  'rä  V.40.  i;  i,  4;  —  läa  äl yazamaide  'rtm  mazdqm  y}  gqmlä  ahmiä dat..  Y.3-J.  i;  —  BitJ  yä  v3  ..  '1^  mazdh *nämqm  dadät  ..  Y.  ^JÄ  4;  —  dätdl  a/.. mazdä  'rä  . .  västryJng .  .  akmaj-afonat>hs (sd.)  Y,  4a.  3;  —  ya^ä  tu  l  *'ra.mazdä^^ minghäcä  .  .yä  vohü  diä  tSi  dadunahi . . a^ä  iiSidyämahl  ^wä  mazdä  'rä  Y.yp.4; j6.  5,  I ;  —  'rakyä  :l  at  vi  mazda  yas- n»mcä  .  .  amSAmaidt  . .  Y.J5. 7;  —  ^wDi staotarascä  ..  ^''ra.mazdä"'^  aggitnadailä  .. Y. 41.%;  —  ätari  vSi (sd.)  mazdä  'rahyä ahi  Y.J6.3; — äiar^  mazdä  akurahyäY. 36.1,  3.  a)  in  Verbindung  mit  n)  Asa (sd,,  unter  A  1  a)  und  ß)  Asa  (sd.,  unter A  1  0,  VohuManah  ua.:  a)  *'ra.mazdä"'^ d/ä  srTrä  Y.  J^.  $;  — stets  garS  vahmSrtg 'rät  mazdäi  asäicä  vahiääi  dadtmahicä Y.  41.  I ;  _95.  s;  —  mazdä  'rä  .  .  iava/ä sar)iit  asaliyäcä  Y.  41. 5  f. ;  40.  i  f.  ß)  yaza- maide 'rillt  mazdqm  . .  ahm  ..  vahislmt  .. 7ighucä  inanö  . .  vohttcä  xiäi^rim  . .  Y.  ^-j. I— 5-  4)  im  gAw.  (ausser  GHapt,), Es  sind  hier  die  Strophen  herangezogen, die  ^ahura-  und  'mazdäh-  im  gleichen Kasus  enthalten;  s.  dagegen  I  z.  Die Stellung  der  Wörter  ist:  ah'..m',  m'..ah' (in  beiden  Fällen  ist  die  Trennung  oft erheblich);  m°  ah",  ah' m'  (im  letzten  Fall trifft  stets  die  Zäsur  dazwischen:  Y.  2^.  9,
6903:•  p.    a'\ira''mazdäh- "    m.     Name    des
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
10915:—  nsitiä  Im  •näus  vaf/y0(sd.)Y.^i.  13;  — f0i/  mä  -näui  yä  v>mSna  (sd.)  ,  ,  Y. 4B.\.  2)  £  'ZufriedcnstcUung;  Pflicht- erfüllung gegenüber  -'  (Gen.):  atca  hii scantä  manamAa  ux<iais  fyao'ianäisca  'näm matda  vaAmäi  ä  fraorii  yasnascä  . .  "und es  sollen  sich  in  Gedanken,  Worten  und Taten  gern  um  seine  Zufriedenstellung bemühen  —  (ihm)  dem  Mazdäh  zum  Preis
13427:•  g.  'dämay-,  g.  d^nay-  Adj.  (auch fem.)  'schaffend,  Schöpfer',  a)  absolut  oder b)  mit  t)  Gen.  obj.,  ß)  Akk.;  von  (lUttem, uzw.  i)  von  Mazdäh:  b  a)  at  ^wä  minghl
14330:hyä  i^uri^masdaha'  framana,  hauvtaiy gasta  ma  %adayi^  "0.6.6; — c^urc^matda- taiy  (Gen.  obj.)  jti'ta  biyi^  Bh.^  17,  11 (wo  'tay).  b)  im  Aw.;  uzw.  Bio)  im gAw.  (mit  Ausschluss  des  YHapt);  zu  i): at  isi  atrim  aAura.. usJmahl^^yoa  deinem Feuer,  o  AA.,  . ."  Y.  34. 4 ;  1 1,  33. 9,  48. 1 ;
=== 1192
```


## [2026-09-07T16:22:58.224Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^•.*mazd\\|^• .*mazd\" BRT.txt | cut -c1-260 | head -30",
 "description": "Bartholomae entries containing mazd"
}
```


### [2026-09-07T16:22:58.292Z] TOOL RESULT

```
2954:•  j.  aoman-"  Adj.  'helfend,  beistehend': tä  nS  . .  %räy?nle  .  .  'mtta  (IS.)  ahura mazda  sraoiaea  .  ,  ".  .  una  cum  juvante AhM.  et  Sr."  Ytij.146.
3058:•  j.  *a-gar»mo.varah- ''  Adj.  'der  keine (Zulassung  zur)  Hilzeprobe  hat,  vom  Hitze- ordal  ausgeschlossen  isf:  myazdavä  ratus atnyaadavamm  ratunaim  "ratflum  daste antan  mazdayasiiilts  ". .  macht  (erklärt) der  Ji.  . .  den  Laien
3121:•  j.  "^a-yzö.nvamna- ''  Adj.  'sich  nicht mindernd,  verkleinernd*;  mazdqmcä  ahu- rsm  yaa'byü  xsa^r»mca  "tum  varidaitl ärmaitis    "und    den  MAA.  und    (all)   die,
3432:•  j.,  g.  a'^Tä  Adv,  1)  räumlich  'hier;  da- hin' :  °ra  pasiaHa  vazaile  vats  . .  värsmca ..  avi  asä  Yt.Ägs;  /p.69;  —  «a/  °ra vicarmti  .  .  yty.49;  V.  J7,s; — yai  °ra para.jasaiti  ..  ya^ra  .  .  Ytio.ioi;  — *'fa
3530:•  j.  x^d/vnoWa ..  apaitisjc^ara^ä  bavätii te  mazda  Yyt.jS:  -?-.
3619:•  g.  a-paourvim  Adv.  'in  noch  nicht  da- gewesener Weise,  wie  nie  zuvor":  yS  va aia  ufySnl  tnanaüa  vohü  ap'  mazdqmcä.. "der  ich  euch,  o  A.,  besingen  will  wie nie  zuvor,   und   den    VM.   und   . ,"    Y.
3627:•  j.  apa-stütay-  f.  'das  Sichabgeloben, Abschwören':  yä  haca  damayat  mazda- yasnSii  'Biiis  "das  Abschwören  dei  mazd. Religion"  N.41.
3694:•  j.  '''aipi.karata'^  Inf.,  mit  asii  'er  ist eingedenk,  hat  Acht  auf  — '  (Gen.):  vis- paz'a  vilcS  mazds.fraoxta  .  .  ySi  huiti  "la dusmatahe  ".  .  die  Acht  haben  auf  das, was  übel  gedacht  ist"  Y.  71.7;  7*.
4231:•  g.  an-aeäa-  Adj.  'der  nichts  (auszu- richten) vermag,  unvermögend,  unwirk- sam, einflusslos':  vaeda  tat yo.  ahmt  mazdn, °sS  "ich  weiss  das,  weshalb  ich,  o  M., nichts  (auszurichten)  vermag"  Y.46.2;  — y?  'um  x/qnm3ng(sd.)  
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  D
4446:•  j.  an-ä'st^rstam  Absol."  'mit  Nicht- sichversündigen,  ohne  sich  zu  versündigen': %<asS  pascaiia  mazdayama  ake  nmünahe myazdim  dati^yani .  .  \yaoidayqfi\ ''  an" hama^a  ya'ia  paracil  "nach  Gefallen können  alsdann  die  M.  die
4661:•  g.  anyäd-ä  Adv.  'anders,  sonst  ausser  — ' (AbL)'';  yi  mit  na  mar?xiaiti  a"  ahmät (sd.)  mazda  hvS  dämSis  drsp  huiius  (sd.) "wer  sonst  noch  auf  mein  Verderben  aus- geht ausser  Ihm,  o  M.,  . ."  Y.5/.10.
4958:•  j-i  g-i  P-  'ava-  Pron.  dem.  (fem.  'rJ-)";  einem  erläuternden  oder  ergänzenden  Re- 'jener';  I)  in  starkdeiktischer  Verwendung :  lativ,  i)  adjektivisch:  aom  stänm  yiiii 'jener,  der  dort,  dann',  von  dem  gebraucht, ! //ÄrJ
5005:•  j.  ava-lcana-  in.  i)  'Graben,  fossa':  ys atttm  'tum  avalianta\.lyz^-  a)'Gnibe': aSa'iii  .  .  mazdayasna  ai-^hä  s»mS  'mm aiaJianayin  V. i'.8".
5172:•  p.  avahya-rädiy  adv.-artige  Verb. 'aus diesem  Grund,  deshalb':  äspiU pit-ii  haxä- manil  .  .  av  haxamanisiyä  'itahyümahy Bh.  /.  3;  —  tyt^  manä  kartam  avaiii (sd.)  *aiava^  av  mä  apagaudaya'^  Bh. 4-10.  a)  mit  folg.  y
5188:•  g.  *av5in''  Inf.  'zu  sorgen  für  -,  zu wachen  über  — ':  tatca  mazdi  %wahml  ä
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö
5680:•  j.  arsya-  m.  EN.  eines  Gläubigen: vatihsui  '^ehe  asaonS . .  'syehe  vyilxanake yJsi)rJsi)maAe  mazdayasnanqm  "des  V., Sohns  des  A. . .,  des  beredten  Ä. . ."  Yt. ij.  loS.
5765:•  g.  a-siStay-"  f.  1) 'Verheissung  auf-' (Akk.):  iä^ä  mSt  yqm  yaoi  damam  yaoz- däm  yqm  *Aud3naos  paiüh  saüyat  xsa- %raAya  xnlvä  xsaira  %wSvqs  °tls  (AP.) mazda  "ob  mir  wohl  für  das  Ich  des  ein- sichtigen, das  ich  ve
5794:•  ].,  g.  'astay-  m.  'Geselle,  Genosse'' aarahe  mainySus  'ti^(ä\  P.j2'*;  —  y} atsm  drygvaile  .  .  varilaitJ  vaahäu  vä tSi>ain  (sd)  'nm*>  \-33.2;  —  drüjö (bmitni  Aaüya  auA^n  'tayd  "im  Haus  der Drug  werden  sie  sicher
5828:•  j,  astvat^rsta-  m.  EN.  des  dritten  der drei  Söhne  Zara^ustras,  die  aus  dessen; im  See  Kasaoya  aufbewahrten  Samen hervorgehen  sollen '' " :  uxsyatjtylahe  .  . uxsyai.mmanhs . .  'Iahe  aiaota  Yt  13. 1 28; HO,  117;  —  yttt  'l�
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm
5904:•  j.  asnvant-  m.  Name  eines  Bergs  oder Gebiigs":  ahmat  haca garays  fraoxsyqn.. 'väsca  Yt.  //).  5;  —  "vanlitn  gairJm  masda- <iSt)m  S.2.9;  —  'vaniahe'^  garSts  mazda- oätahe  Ny.5.5.
6007:•  j.  az«m,  g.  azSm,  p.  adam  NS.  Fron. 1.  Pers.  'ich'.  Es  wird  gesetzt  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegt)  a)  bei  Gegenüberstellung:  1  naiy 'iam  fuümaiy  taumä  Bh.  >^.  1 1 ;  —  11  ima' ttsuam  (s
6045:•  g.,  p-  azdi  Adv.  'kund,  gewiss' :  Ikärahya naiy  a'  abavaf'  tya'' . .  ". .  wurde  es  dem Volk  nicht  kund,  dass  .  ."  Bh.  1. 10;  — \adataiy  a°  bavätiy  D.  Ö.4';  —  k!  mSi pasSus  k!  mS  nä  ^ratd  vis/3  anyS  asät "^
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  
6165:•  j.  aSa-ä^ra-,  aäö.ÜdTa-'*  Adj.  'der seinen  Ursprung  im  Asa  hat':  vispanam vohunqm  vispanam  'ranam  H.  1. 1 ;  —  vis- palsu  var»hufu  vUpagsuca  -ra^iu  YL  1/.3'*; P.  27'';  -^  äps  ..  urvara  .  .  vitpa  voka 'ra  y.8.^.  a
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (
6879:•)  {Vgl.  unter  J'arJ'mazdäh.)  Ah.  Ut  maiiUö yasalanqmtit,  ma%Ul</'  bagänäm  Und  alE  solcher der  Schöpfer  aller  guten  Wesen  und  Dinge, auch  der  AmisaSpata  (sd.*)  und  vj-l.  Y.  /p.  8). Sein  ewiger  Gegner  und  Zw illingsb rü
6898:•  j.  ahura.tkaeäa- '',  TÖ.tkaeäa- '>  Adj. (fem.  'Sä-)  i)  'j4/iurashehie  enthaltend': väät/i ..vidsyum  's?m  Yt./^.go'.  2) 'Ahuras Lehre  zugetan,  anhangend':  mazdayasnö zara^us^tri/  vTdagZ'3  's3  Y. /2.1,  Yt  iS-Zq; Y-5-i3>  —  a
```


## [2026-09-07T16:23:09.685Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mazdäh-  m\\.\\|mazdäh-  n\\.\\|Gedächtnis'.*mazd\\|mazd.*Gedächtnis\" BRT.txt | cut -c1-300 | head -10\necho \"=== manuscithra region\"; grep -n \"cJ%ra\\|ci%ra\\|ciOra\\|cifira\\|ci\\^ra\" BRT.txt | cut -c1-150 | head -10",
 "description": "Grep BRT for mazdāh entry and čiθra"
}
```


### [2026-09-07T16:23:09.755Z] TOOL RESULT

```
20214:•  j.  '^mazdltae-ir'i)  '>  Inf.  'dem  Gei^chtnis einzuprägen,  im  Gedächtnis  zu  behalten': yasnaheüa  kaftanhätsis . .  m'  *trazäätaica Vr.  1$.  2.
20216:•  g.  mazdä&a-  □,  'res  commemorabilis, was  man  dem  Gedächtnis  einprägen  soll, sich  merken  muss':  at  ta  vaxlya  iimts yä  "äJ  hya^äi  (Sp.  593  u.)  viäu^i  stao- täcA  akurai  yetnyatä  vaaÄSUl  manatffie humqsdra  (sd.)  a/a  yeäl  .  .  "nun  will  ich davon  r
20220:•  g.  'mazdäh-'*  n.  'memoria,  Gedächtnis', nur  AS.  'äqm''^  mit  ^kar-  (Sp.  445  m.): 'dqmcä  hUiricS  ktnhä  räiti  tsi  xrapaiti (sA)  ahmat  Aya£  aiii  Y,4o.  i.
20222:•  j-,  g'i  P-  'mazdäh-  m.  Name  des  höchsten Gottes;  I)  ohne  ahura-;  i)  im  gAw.: urvätä  . .  yS  °ää  (Nom.)  äadat  Y.  jo.  11; 34- i;  —  'da  (Gen.)  data  . . gayehyä  (sd.) lyao%atai!  vahyS  Y.jJ.  19;  —  urvat>m (sd.)  .  .  tat  nS  'da  (Vok.)  vidvanSi  
26149:•  g,  sax^ar-  n.  'Anschlag,  Plan':  mazdä •x'ärJiAF.)  niairisiJyä  sT  7'äv>r)iSi  pairT.- ählj  daSvaUcä  maiyäUul  ylcä  variSaitS aipLciUU  "M.  hat  die  Anschläge  am besten  im  Gedächtnis,  die  früher  schon von  G.  und  Menschen  ausgeführt  worden sind  und  auc
30443:•  g,  hu-mazdar-  m.  'der  (etwas)  gut,  recht im  Gedächtnis  behält,  (es)  gut  merkt': °zdrä  aiä  yaä'^  yä  raocibl!  dansatä urvätä  "und  von  der  Wonne,  die  von dem,  der  es"  sich  gut  merkt,  (zugleich) mit  dem  ..^rä^',  die  (zugleich)  mit  dem  Licht- raum 
=== manuscithra region
6599:Kopula  hat  keinen  festen  Platz,  bevor- zugt aber  entschieden  die  Stelle  hinter dem  ersten  Hochton  ihres  Satzes,  und zwar  auch  im 
7153:feuer***':  yqm  xsnBtftn  ränsibyä  (sd.)  da "^wä  ''ira  suxrä  mazdä  ayanhä  xiustä Y.5/.9;  31.3;  —  (a  da  spmta  mainyü ,  �
7255:aoxta  aAurö  mazdä  N.  2. 3ti.; —  äat(s.Z) frasüsat  andvl  . .  ä°  aoxta  arsdvl  Yt5. V.  22,i  iSt.;  —  aat  (s.  8)  mi paoiry
7536:•  j.  'i-zäta-  Adj.  (fem.  Ha-)  'adeHg,  edel, vornehm':  °ta  F.  7;  —  kainins  . .  "tayi raevasci^raya  H.  2.9;  —  kainlnö  .
9778:.  .  mainyaom  .  .  *'ihim  yazafym  Y.  25.  8,  •  j.  gao-ciOra-  Adj.  'den  Ursprung  des 16.1  f.; —  vispaSca  ,  ,  mamyai^a^a  yas
13762:•  j.  duS-ciOra-  Adj.  (fem.  'ra-)  'des .\nblick  übel  ist,  hässlich  anzusehen': drujim  yam  °rqm  timanhainJm  YL  /^.gs;
17191:•  '].  barazavant-  m.  EN.  eines''  Gläu- bigen, BapCasynjg:'  uxsänS  vfhtsravaahB dQralsrüia/ie  {sA.)  'vatd  YtJj.  119;  -— fräc
21260:•  j.  yat  vä"  partikelhafte  Verbindung; J)  zur  Trennung  von  Satzteilen  im  Sinn des  lat.  vel.  Sie  tritt  1)  zum  letzten  von z
23870:•  j.  vohuna'vant-'*  Adj.,  nur  fem.  'vaifi- 'die  ihre  Blutung  hat"';  nsirika  ci%ra-\ vaiti  äaxstavaiti  'vaiti  V.  16.  i ;  — 
24581:•  j.  vi-zuS-'*  m.  (auch  mit  ^span-  m.) Name  einer  Art  desHundegeschlechts;  hau 'zaui^GS-yK .  hau  vispanam . .  spaci%ra»am V.y.
```


## [2026-09-07T16:23:24.937Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'•[^\\n]{0,40}m[aä]nu[^\\n]{0,200}', d):\n    print(repr(m.group(0)[:200]))\nEOF",
 "description": "Find Bartholomae manu- entries"
}
```


### [2026-09-07T16:23:26.315Z] TOOL RESULT

```
'•  j.  manu/-  m.  ES.  eines  alten,  vorsag- lidien  Helden.'
"•  j.  manuSa-  m.  Name  eines  Bergs '>: afr^atB{sA^  gairi/ pärmtar^m  ar^d  °lahe Ytiff.i."
'•  j.  manuä.£i3-ra-  in.  EN.  eines  Gläubigen: *%raie  airyävafu  asoönö  "des  M.,  Sohns des  A.  .:•  Yty.  131.'
'•manu  asaene  Yt.  13. 128,  121.'
```


## [2026-09-07T16:23:35.969Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'•[^\\n]{0,30}mainyu[^\\n]{0,250}', r'•[^\\n]{0,30}mai[nñ]y[aou][^\\n]{0,180}']:\n    for m in list(re.finditer(pat,d))[:6]:\n        print(repr(m.group(0)[:250])); print('--')\n    print('=====')\nEOF",
 "description": "Bartholomae mainyu entry"
}
```


### [2026-09-07T16:23:37.269Z] TOOL RESULT

```
'•  j.  mainyu.tääta-\'\'  Adj.  \'von  Geistern" gefertigt":  väüm . . stfArpalsa?»\x0ch?m  \'tsm  Yt 10.  143;  —  aiwyäahanam  stthrpaisam^fm \'ttmY  .g.36;Yt.l3.i,Y±20; — hat>ma{sA.) . .  stikrpaEsanha  Ua  (als  APm.)  Yt  10.  90.'
--
"•  j.'''mainyu.stäta- Adj.'voii(den)  Geistern hingestellt':  asman»m  .  .  ys  histaile  'tS Yty.a."
--
'•  j.  mainyu.äüta-  Adj.  (fem.  *ta-)  Vom Geist  angetrieben\':  frava^ayB ■ .  ya  utisti \'tä  fraiüsinte  bansnvS  avaAht  alnS  "die Fr.,  die,  wenn  gerufen,  vom  Geist  getrieben, herankommen  von  . ."  Yty.43.'
--
"•  j.  mainyuä.x'ar«&a-  Adj.  (fem.  •%a^ i)  'die  Nahnmg  des  Geistes  bildend':  yh nS  htnti  gdhä  Aarfhravaitls^a . .  '^äsca  yä nö  hsnti  urune  tvaim  i^an'äfmld  vastr^mSi Y.55.  a;  2.  2)  'die  Nahrung  der  Geister geniessend':   aur"
--
"•  j.  mainyu.h^n.ääta-  Adj.  'von  Geistern gefertigt,  gebaut':  mikr3m.,ys  vala'ta.. fravataite  Yt  lO.  67."
--
"•savÄim  mainyu.- täst»n  Yt.  10. 143;  —  nm lrum..*°sanhm'^ '> niitara.nalmlt  Y.  57.  21;  —  haomq  .  . 'sanha  (APm.)  mainyu.täsia  Yt  10.  90."
--
=====
"•  j.  aBr5.mainyav-  Adj,  'dem  bösen Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig' :  iaAe  vaca  vanai  . .  kana zaya  mana  dqma  'yus  (IP,  als  APn.) ''  V. /»).8;  —  -ffl"
--
'•ris  mainya- i-asa  yim  aahat  >r?xsS  (sd.)  Yl  S.  6.'
--
"•  j.   däSmainya-  Adj.  'sich   aufblasend,"
--
"•  j.  dus-mainyav-''  Adj.  'übel,  feindlich gesinnf ;  (als  mask.  Subst)  'Feind':  vUär?m"
--
"•  j.  fra-mainya-  n.  'Praevalcnz,  Vonnacht über  — '  (Gen.):  nöii  nmänS.baxffm  . .  nöit 'manim  brä'iranqm  aglius/e (sd.)  P.43i  — *a^a  *nä  äxsta  (sd.)  htyqn  *ya'^a  *«3 buyill  . ."
--
"•  j.  mainyaoya-  Adj.  sva,  mainyava-x ahurahe  mazdh  . .  mainyJus  'yatyehe  Y.^7."
--
=====
```


## [2026-09-07T16:23:45.261Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD\"; grep -n \"Ohrmazd\\|ōhrmazd\\|Mānūščihr\\|Manuscihr\\|māzdēsn\\|mazdēsn\\|mēnōy\" PHD.txt PHD_mackenzie.txt | cut -c1-220 | head -20\necho \"=== NYB\"; grep -n \"Ohrmazd\\|ōhrmazd\\|Mānūščihr\\|māzdēsn\\|mazdēsn\" NYB_vol2_glossary.txt | cut -c1-220 | head -15",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-07T16:23:45.337Z] TOOL RESULT

```
=== PHD
PHD.txt:472:māzdēsn [m”3d(y)sn' | М m”zdys] Mazda-worshipping, Mazdean. ^h: Mazda-worship, Mazdaism.
PHD.txt:518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, b�
PHD.txt:760:Ahuramazda Ohrmazd.
PHD.txt:2514:Jupiter (astr.) Ohrmazd. Justice dad, dadestan.
PHD.txt:2753:Mazdean māzdēsn, scriptures abestag.
PHD.txt:4383:Ohrmazd
PHD.txt:4390:r Ohrmazd
PHD.txt:4883:māzdēsn mahist, māst māzandar māš, maxš roynt
PHD.txt:4891:jām mānsīr māns*rbar mānsšrspand māraspand mānbān mānbed mānišn māzanīg māzandar māzdēsnīh māzdēsn fradagt mar
PHD.txt:4893:māzdēsnīh
PHD.txt:4896:mah māhīgān māhīg mayān mayanag mayānjīgīh mayānjīg mehmānīh mehmān māzdēsn māyišn zan-!
PHD_mackenzie.txt:3846:Ohrmazd [)whrm:;:d I M )whrm(y)zd, N H6rmuzd] Ahura Mazda: astr.
PHD_mackenzie.txt:5922:Ahuramazda Ohrmazd.                       anybody kas-iz.
PHD_mackenzie.txt:6905: interpreter targumiin; ....., of dreams   Jupiter (astr.) Ohrmazd.
PHD_mackenzie.txt:8014:Ohrmazd                      Ard (Ahriswang)
PHD_mackenzie.txt:8039: I  Ohrmazd                  12 Miih
=== NYB
2522:māzdēsnēh [m?zdysnyh] the state of be- ing a Mazdayasnian 63H.
4343:x"arrah [GDH] a divine essence, a special form of the Eternal Light, a splendour, a glory I. manifested in the gods: one swears by (pat) ~ % Ohurmazd bag u den imāzdēsnān 2117-22-28 (without bag). 2321-22 ; zor 
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-man
```


## [2026-09-07T16:23:58.013Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD manus\"; grep -n \"Mānūš\\|Manūš\\|Manuš\\|mānūščihr\\|Mānušcihr\\|Manuscihr\\|nūščihr\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | cut -c1-200 | head\necho \"=== HRN music/mousa\"; grep -n -i \"musik\\|musiqi\\|mûsîqî\\|mazgân\\|mazqân\" HRN.txt HUB.txt | cut -c1-200 | head\necho \"=== HRN manucehr\"; grep -n -i \"manûčihr\\|Manutschihr\\|Minocher\\|manuc\" HRN.txt HUB.txt | cut -c1-200 | head",
 "description": "Grep PHD/NYB/HRN/HUB"
}
```


### [2026-09-07T16:23:58.100Z] TOOL RESULT

```
=== PHD manus
NYB_vol2_glossary.txt:1172:dahyupat [dhywpt'] ruler, king: Fran ~ of Vistasp-sah 1917. 6017-2. 1118; of Manušcihr 47°; of the Great King killed by Alexander 107’; Vadagān (g. v.) ~ of Dahäk 902;
NYB_vol2_glossary.txt:2237:ikartan [krtn'; klty; ‘BYDWN-t'] kun- [ BYDWN-;forms v. I, 179; pres. 3d p.sg. kwnd: read kund] to make, to do, to per- form, to exercise, to commit, to cause, to bring ab
NYB_vol2_glossary.txt:2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz
NYB_vol2_glossary.txt:2428:Manūcihr [mnweyhl]113!1%, and Manuš- cihr [m’nweyhl] 472. 1165, the son of Eréc and the successor of Frétón. — Av. (1135) Manuš.cidra-; NP Manücihr.
NYB_vol2_glossary.txt:2430:Manuš-x"arnar [m’nwShwlnl] the son of the preceding and the father of Manus- cihr 472. — BdJ 781° Paz. Mandsx“arnar.
NYB_vol2_glossary.txt:3208:Rag [l'k']the name of a district and a town: né ka étar har 2 6 ham rasénd ~ u Notar not (even) when the two, Rag and Notar, come together here (i.e., never) 4316-17, 501
NYB_vol2_glossary.txt:5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčni
=== HRN music/mousa
HUB.txt:2640:bal. sarDd musik' (Dames p. 87), afgh. sardd a song,
HRN.txt:4516:'Musik, /unyäyer,
HRN.txt:9183:ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
HRN.txt:23307:Schwa (g) ist vorläufig noch Zukunftsmusik, in deren
=== HRN manucehr
```


## [2026-09-07T16:24:08.238Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in موزیک مزقان مزغان موزائیک اتوماتیک مانکن موزه منوچهر مزدیسنا; do echo \"=== $w\"; grep -o -n \".\\{0,120\\}$w.\\{0,160\\}\" MON_part1.txt MON_part2.txt | head -3; done",
 "description": "Grep Mo'in 2-vol for the Persian words"
}
```


### [2026-09-07T16:24:32.344Z] TOOL RESULT

```
=== موزیک
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


=== مزقان
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


=== مزغان
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


=== موزائیک
ugrep: error: error at position 92
\n\x80-\xbf][\x80-\xbf]*){0,160}
   exceeds complexity limits___/


=== اتوماتیک
ugrep: error: error at position 94
[^\n\x80-\xbf][\x80-\xbf]*){0,160}
     exceeds complexity limits___/


=== مانکن
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


=== موزه
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,160}
                          \___exceeds complexity limits


=== منوچهر
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,160}
 exceeds complexity limits___/


=== مزدیسنا
ugrep: error: error at position 92
\n\x80-\xbf][\x80-\xbf]*){0,160}
   exceeds complexity limits___/
```


## [2026-09-07T16:24:37.279Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntexts={}\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    texts[f]=open(f,encoding='utf-8',errors='replace').read()\nfor w in ['موزیک','مزقان','مزغان','موزائیک','موزاییک','اتوماتیک','مانکن','منوچهر','مزدیسنا']:\n    print('====',w)\n    for f,t in texts.items():\n        for m in list(re.finditer(re.escape(w),t))[:2]:\n            print(' ',f,repr(t[max(0,m.start()-90):m.end()+150]))\nEOF",
 "description": "Python grep Mo'in 2-vol"
}
```


### [2026-09-07T16:24:38.659Z] TOOL RESULT

```
==== موزیک
  MON_part1.txt 'ای \nترکیبی و آن تجسم و نمایش یکك موضوع \nاست به وسیلة نوعی رقص علمی و حرکات \nمشکل همراه با موزیکث. \n\nبالرین: ۱2 (.) (نم.) رقاصةٌ حرفه\u200cیی. \nبالش: ۳2۱-64 (.مص. بالیدن) نمو؛ بالیدن. \nبالش: 02-5 (.) آنجه به هنگام خواب ز بر \nسرگذارند» فتوا تن \n\nبالش: '
  MON_part1.txt 'نجم فوقانی رفته باشیم؛ \nسس عشاق شنیده می\u200cشود و راست پنجگاه \nتبدیل به نوا می\u200cگردد. (خالقی. موزیکك.) \n\n\nبت ج توبت: (۲.20200۷ آف. ۳۵8 \n(افز) تویت بویت که بر دن بادضاهان \n\n\nپنجه فرهنگ فارسی معین \n\n\n۳۹۹ \n\n\nزنند و این از عهد سلطان سنحر مقرر شده \nاست و'
  MON_part2.txt ' که از ماهور به دلکش می\u200cرویم \nتغییر مقام است زیرا مقام ماهور تبدیل به \nشور می\u200cشود (خالقی. موزیکك ۰۸:۱۰ \n۱-۳ مایه\u200cشناسی ماهور طبق قواعد \nمایه\u200cشناسی گام\u200cهای تور کت است یعنی \nآخرین دیزه نوت محسوس و به ماقبل از \nآخر تنیک است. کیفیت آواز - ماهور \nآوا'
  MON_part2.txt 'مامتان (رص. .) \nمسوستی\u200cدان» نوازنده. هصسح.- احتراز از \nاستعمال این کلمة بیگانه اولی است. \nموزیک: ۲ (.) موسیقی. \nمسوزیکال: 722 (ص.) مروط به \nموسیقی. \n\nموز: : 712 [قس. موی؛ مو ب | ( ی \nموز: : (2)0۳62تا (۱.) تالات؛ ۳ \nموژیک: ۶ روسی: دهقان \nروسی (یی'
==== مزقان
==== مزغان
  MON_part2.txt ') \nمسکر: ۱1۱۲ اع. (افا.) جیزری که \nنوشیدنش مستی آورد مانند شراب عرق و \nبر و \nمسکل: ۱7۵۵۸ [مزغان. موسبقی | (.) \nسازی که 1 را با دهن نوازند. \nمسکن: 0( [ع. (.) محل که ات \nجای\u200cباش؛ منزل» مقام؛ ج. میت \nمسکن: ۱0 اع. (افا.) \nدهند هه مطی امس ی موچبت \nشو'
==== موزائیک
==== موزاییک
==== اتوماتیک
  MON_part1.txt 'را می\u200cشو یند. \n\nاتوکار: 00-۲ (امر.) اتوسیل بزرگ که \nبرای حمل مسافران دسته جمعی بکار رود. \nاتوماتیک: (ص.) دستگاهی که \nخود به خود کار می\u200cکند و نیازی به بودن \nکارگر بر سر آن نیست؛ خودکار (فره.) \nاتومبیل: (1مهم۱ه (.) (فز . فک دستگاه \nخودرو که به وسیلةٌ'
==== مانکن
  MON_part2.txt ' \nعدم ازم نباد به داته, مایت فتافرت که مانع \nروزه گرفتن و تمامیت نداز است (فر عم. \nسج.) \n\nمانکن: ۵۸ (۱.) پیکر دای به شکان \nانسان که از جوب؛ مقوا و غبره سازند و بر \nآن لاس پوشانند و در خیاطخانه\u200cها و \nمغازه\u200cهای لباس\u200cفروشی به معرض تماشا \n2 دختر زیب'
==== منوچهر
  MON_part1.txt 'لجوقی و خوارزمشاهی تعقیب \nمی\u200cکردند. از جملةٌ نمایندگان این سبکك \nودک فتهت خاکو) عتضری ری \nمنوچهری و انوری را باید نام برد. سبکث \nعراقی: سبکی که شاعران عراق عجم از قرن \nششم به بعد تعقیب کردند از جملة نمایندگان \nاسن سک جمال\u200cالدیسن اصفاهانی و \nکمال\u200c'
  MON_part2.txt 'ب رگك\u200cهای آن به رنگ خون و \nوسط آن سیاه باشد بنام لاله و شقایق نامیده \nمی\u200cشود (کازیمیرسکی. منوچهری ۳۱۲). \nت رکیبات اسمی: لاله احمر: (گیاء) لاله سر خ» \nلاله حمرا. ( کد.) اشکك خونین. لاله حافظ: \n(گیا.) گونه\u200cای لاله که در باغ\u200cهای شیراز \nرک و داخل کلی'
==== مزدیسنا
  MON_part1.txt 'ب \nگردید. پس از به بایان رسانیدن دورة دکتری» جلسة دفاع از پایان\u200cنامةٌ دکتری وی \nبا عنوان «مزدیسنا و تأثیر آن در ادبیات پارسی» در روز سه\u200cشنبة ۱۷ شهریور \n۱ تشکیل و پایان\u200cنامةٌ او با قید ربسیار خوب؛ قبول گردید» و او نخستین \nدکتر ادبیات فارسی در ايران'
  MON_part1.txt '(ترحمه احوال و آثار) (جزو یادنامهٌ بورداود محلد اول و نیز \nجدا گانه منتشر شده) ۰۱۳۲۵ \n\n۰ -مزدیسنا و تأثیر آن در ادبیات پارسی (با مقدمهٌ مشرح به زبان فرانسه به \nقلم هنری کربن) شماره ٩\u200f از انتشارات دانشگاه تهران ۱۳۲ \n\n۱ - شماره هفت و هفت پیکر نظامی '
  MON_part2.txt '. (که اعیاد دینی \nسال باشند.) کستی را را باید ۳ بار دور کمر \nپیچید و اين نیز به عدد ۲ اصل مزدیسنا \n(منش نیکك» گوش نیک و کنش نیک) \n\n\n9 \nموظف است که کستی رابه دور کمر نندد. \nکشتی» مصارعت. \n\nکس ده: ۱05-001 [- کس\u200cدهنده] (رص\u200cفا.) \nزنی که از راه نامشروع'
```


## [2026-09-07T16:24:59.414Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfiles={'ARY':'incoming/ARY/ARY_pages.txt','ARYL':'incoming/ARY/ARY_latin_index_pages.txt','FSF':'FSF_pages.txt','FRS':'FRS_pages.txt'}\nfor k,f in files.items():\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(k,e); continue\n    for w in ['منوچهر','مزدا','موسیقی','مینو','MANU','MEN-','MENS']:\n        for m in list(re.finditer(re.escape(w),t))[:2]:\n            print(k,w,'|',repr(t[max(0,m.start()-120):m.end()+180]))\n    print('-----')\nEOF",
 "description": "Grep ARY and FSF"
}
```


### [2026-09-07T16:25:00.764Z] TOOL RESULT

```
ARY منوچهر | '\u200cها و به طورکلی همه مطالب این کتاب را\nبمهده می\u200cگیرم.\nامیدوارم که این کتاب دوست\u200cداران زبان پارسی و زبانشناسی را خوش آید.\nمنوچهر آریان\u200cپورکاشانی\n\x0c[pdf page 3]\nسا\nباسپاس از ۴۰۱ دب\nدکتر ایرج آزیان\u200cپور کاشانی (بازخوانی متن)\nمهندس حسین فلاح (بازخوانی متن پرینت دوم)\n\x0c[pdf page 4]\nا نا :7\nدیباچه / ۵.\nدیباچه\n«هند '
ARY مزدا | 'ای او تحت عنوان «برگزیده\u200cای از زبان\u200cهای آریایی»\nدر مقدهه\u200cی فرهنگك نوین پیوسته فارسی -انگلیسی و انگلیسی -فارسی. انتشارات مزداء لوس آنجلس»\n۹) چاپ شده است. هدف ایشان بیشتر نشان دادن خویشی فارسی با زبان\u200cهای اروپایی بود و\nرابطه\u200cی واژه\u200cهای فارسی با هند و اروپایی نخستین را شامل نمی\u200cشد. :\n\nدر چند دهه\u200cی اخیر راب'
ARY مزدا | 'م اين واژه در زبان\u200cهای ژرمنی: ننگی؛ تنگه» باریکك.\nچم این واژه در زبان انگلیسی نوین: خشم.\n\x0c[pdf page 98]\nاهورا هرمز اهورامزدا / ۹۹\nچم این واژه در زبان ابلندی کهن: اندوه» غم.\nریشه\u200cی اوستایی این واژه دارای دو بخش است» بخش نخست آن در این ,فهرست پیگیری شده است» برای\nشناخت بخش دوم آن به آمنش " بازگشت شود.\nِ\nا'
ARY مینو | ' ,6 713006113) :۸۸۸۲0297212\nلانین (7/۷): ۰ ,۲0۱۸۸18۹۲۲0۴ ,۸45824 0 118۲110۲ :\n8 برهان قاطع + ۲:۴۲\nبادداشت.\n۱ بازگشت به: مینو.\n۲ راژه\u200cی انگلیسی ,31328۲7۸3 هم از همین واجریشه است.\n\x0c[pdf page 480]\nاوستایی (/۸۷887۸2): -1۸0181 سودی (817501374): ه1۹7\nپپلری (۲1مابنهه: 31080۸6 ب1۸0 نروژی (08۷/6/۸۸/+\nاوستی 0۶370'
-----
ARYL MANU | 'e\nBecta ieee y satay golStl BladL5 32 Sly cal\n2 AF ia piles BOdUs 2205 oul oe\nns\npan anton | A\nMAN HOLD SAXON) AS iy Se MANUS. HAVESTAN) glory!\nMONN HOLD FRISIAN) oS 53.3 “MAN (ZAR-MAN) (PAHLAVI) 5 ly\nMAN (OLD HIGH GERMAN) pf lal MANU, MANUS (SANSKRIT) ey Sails\nMANN (GERMAN) gist MANNA GOTHIC) Sa F\nHOLD'
ARYL MANU | ' AS iy Se MANUS. HAVESTAN) glory!\nMONN HOLD FRISIAN) oS 53.3 “MAN (ZAR-MAN) (PAHLAVI) 5 ly\nMAN (OLD HIGH GERMAN) pf lal MANU, MANUS (SANSKRIT) ey Sails\nMANN (GERMAN) gist MANNA GOTHIC) Sa F\nHOLD ENGLISH) oS pul) (OLD SCANDINAVIAN) 35 (g-thu\\\nMANN, MON, MANNA MATHA, MANNR\n\x0c[pdf page 461]\n| oul | FFT\nMUZE'
ARYL MEN- | "3-904 HAMA, HAMUK, HAMAK\nMACKENZIE: SANSKRIT) ey Sail\n(ALL) 102, (TOTALITY) 137 SAMA, SAHA, SADHRI\nrrvr tab obey AMEN, AMEN-AIN (GREEK) (gly\nAeetlaak\npth\nHNAR ARMENIAN) «gs! HUNARA AVESTAN) pls!\nEU-ENOR GREEK) gy HUNAR (PAHLAVI) 5 shay\nfl SO-NIRT (OLD IRISH) opS' 54 p\\ HONER (KURDISH) 52,\n| HY-NERTH (WE"
ARYL MENS | ') Sx ASMAN AAFGHAND (24) glii)\nKAMEN (BULGARIAN) ¢5 ji, ASHMAN, (SANSKRIT) 2, Suite\nAKMUO, LITHUANIAN) gi g.3 TASMAN\nASHMENS AKMON A(GREEK) 3b y\nHIMINS GOTHIC) &3\n‘REFERENCES bch (OLD SCANDINAVIAN) 3486!\nPOKORNY SSS~*~*~«wD HAMMARR\nBARNHART: (EDEG) 315, HAMUR — (OLD SAXON) oS gyS\n(HAMMER) 463 HOMER — (O'
ARYL MENS | 'A (SANSKRIT) 2 Site\ns(LITHUANIAN) vigd AMIS (ARMENIAN) 0)\nMENESIS, MENUO MEN, MES (GREER) gli\nMENESIS (LATVIAN) (3) six MENSIS H(LATIN)\nMENINS (OLD PRUSSIAN) (9S 3.4 MOIS :(FRENCH) «i135\nMI HOLD IRISH) 3S $43) MES (SPANISH) plied!\nMIS s(WELSH) $39 MESE ITALIAN) gle)\nMIZ ADRETON) «33. més PORTUGUESE) J\nM'
-----
FSF منوچهر | '                                                  \u202bوخ\u202c\u202bخنزد\u202c\n                                                          \u202bمنوچهر را\u202c\n                                                \u202b(\u202a)۱-۴۱۱-۶۶۵\u202c\u202c\n                                    \u202bگوید]\u202c          \u202b\u202a-۵\u202cستأییدن» تعریف و توصیف کردن\u202a:\u202c\u202c\n           \u202bبیارای تا'
FSF منوچهر | '                       \u202b(برانگسیختن» می\u200cنویسد و بیتی از\u202c\n     \u202b(لخت فرس) «کسی را بر جنگ یکاار\u202c                         \u202bمنوچهری باین شکل شاهد می\u200cآورد\u202a:\u202c\u202c\n       \u202bاحهد)\u202c\n           \u202bشحا\u202c\n             \u202b\u200c (ص\u202c\n                \u202bین»\u202c\n                  \u202b\u202a-\u202cیزبکرد\u202c\n                        \u202bدیگر ت\u202c                '
FSF مزدا | 'زد» هرمز\u202c       \u202bانوشه کسی کو بمیرد به زهر\u202c\n\u202bهمه این\u200cها شکل\u200cهای دیگری از «اهورا\u202c                     \u202b(\u202a)۳-۵۰۲-۶۲۱۳\u202c\u202c\n \u202bمزدا»\u200cی اوستایی است که نام ایزد است\u202a:\u202c\u202c                               \u202bکیخسرو از رستم می\u200cپرسد\u202a:\u202c\u202c\n\u202bاز دو واژه است\u202a :\u202cا\u202c         \u202bمرکب\u202c   \u202bاهورامزدا\u202c\n                                   '
FSF مزدا | 'نام ایزد است\u202a:\u202c\u202c                               \u202bکیخسرو از رستم می\u200cپرسد\u202a:\u202c\u202c\n\u202bاز دو واژه است\u202a :\u202cا\u202c         \u202bمرکب\u202c   \u202bاهورامزدا\u202c\n                                                                \u202bزواره فرامرز و دستان سام\u202c\n                                                       \u202bدرستند؟ ازیشان چه داری پیام؟\u202c\n\u202b'
FSF موسیقی | '                                   \u202bابریشم\u202c               \u202bابر دست کیخسرو افراسیاب\u202c\n                     \u202bسیم و تار الت موسیقی\u202a:\u202c\u202c             \u202bشود کشته» این دیده\u200cام من به خواب\u202c\n         \u202bوانگ نای\u202c\n                \u202bز اواز ابریشم ب\u202c                        \u202b(\u202a)۲-۲۳۲-۵۵۳\u202c\u202c\n\u202bسمن عارضان پیش خسرو بهپای\u202c        '
FSF موسیقی | '                          \u202bبربط\u202c        \u202bبیت به معنی\u202a :\u202cپروراندن\u202a ,\u202cبزرگ کردن\u202a:\u202c\u202c\n                          \u202bنوعی ابزار موسیقی\u202a:\u202c\u202c                              \u202bسیمرغ به زال گوید\u202a:\u202c\u202c\n      \u202bبهربط چو بایست بر ساخت رود\u202c                                     \u202bکه در زیر رت بپرودهام\u202c\n \u202bسرود\u202c        \u202bمازندرانی\u202c  '
FSF مینو | '۳۲۳-۳۳\u202c\u202c\n              \u202bبرهان) «زیبایی» (لغت فرس)\u202a:\u202c\u202c               \u202bدو صد گونه گل بد میان فرزد\u202c\n      \u202bگر ایدونک آید ز مینو سروش\u202c                    \u202bفروزان چو در شب ز چرخ اورمزد\u202c\n \u202bنباشد بدان فر و اورنگ و هوش\u202c                                          \u202bاورند (بروزن سوگند)\u202c\n \u202b(\u202a)۳-۶۱۱-۵۸۷۱\u202c\u202c            '
FSF مینو | '              \u202bبدین رنج و بدین گفتار نیکو\u202c\n                      \u202b(دقبقی \u202a:)۶-۳۸-۸۶۲\u202c\u202c         \u202bتو را داشن دهاد ایزد به مینو\u202c\n              \u202bسپهبدش را گفت فردا پگاه\u202c                                       \u202b(مسعود \u202a:)۵۲۶\u202c\u202c\n \u202bبخوان از همه پادشاهی سپاه\u202c                                    \u202bبحر و ابرست روز پا'
-----
FRS منوچهر | 'را مواف حاشیهٌ تنچنانکه بباید در باب الهاء برای لغت دنه مثال آورده و\u202c\n           \u202bآنرا از پرویز خانون نامی مداند \u202a .\u202cدر منوچهری چایی ان پیت نیست \u202a.\u202c\u202c\n\x0c                                \u202b\u202a۲۰۳\u202c\u202c\n   \u202bقاشکی برد پیش آن تاشك\u202c              \u202bبادنان\u200cپرزماست ماست\u200cفروش\u202c\n                          \u202bو لاش\u202c\n            \u202bک'
FRS منوچهر | 'نخواهم سیر گ\u202c\n\u202bوزین رخهای چون دیبا وعارضهای چون حله\u202a۲\u202c\u202c\n                                                               \u202bمنوچهری کوید \u202a:\u202c\u202c\n                             \u202bنو آبین مطربان داریم و بر بطهای گوینده\u202c\n\u202bمساعد ساقیان داریم و ساعد های چون ذله\u202a]۳\u202c\u202c\n                                  \u202b\u202a1\u202c\u202c             \u202b\u200c'
FRS مینو | '                                                                   \u202b\u202a:\u202c\u202c   \u202bآفرخی گفت\u202c\n\n\n\u202bچ وگرد بادهمی \u202a2\u202cش\u202a5\u202cت\u200cبر \u202a,\u202cهمینو بسار |\u202c                    \u202bهمی کرفت ببر؛ وهی\u200cفگند ببوز\u202c\n                                   \u202b\u202a۶\u202c\u202c   \u202b\u202a۱\u202c\u202c       \u202b\u202a۰\u202c\u202c        \u202b»\u202c\n\n                                   \u202bاد\u202c          '
FRS مینو | 'ممئوبا\u202c\n         \u202bنامبادیه ایبروزکارضحاك ازخوشی کهبود » اسدی گوید \u202a:\u202c\u202c\n  \u202bچوبگذشت ازوپهلوان شادکام\u202c           \u202bزوشی بود مینو آباد نام\u202c\n                                                          \u202bخ\u202c\n                               \u202bوت\u202c\n                 \u202bند باشد کهبتازی مر\u200cجان خوانند » اسد گیوید \u202a:\u202c\u202c\n\u202bوسد و'
-----
```


## [2026-09-07T16:25:10.338Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('اهورا هرمز اهورامزدا')\nprint(t[i-3500:i+1500])\nEOF",
 "description": "Read Aryanpur Ahura Mazda entry"
}
```


### [2026-09-07T16:25:11.797Z] TOOL RESULT

```
 در سانسکریت: اندام» عضو پدن. : ۱

معنی اين واژه در زبان‌های ارمنی و یرنانی و رومانس؛ گوشه) خمی. ۱ ۱ وی
اوستایی (4587400): ۸7 ۸۷۸۶ اسلاوی کهن (ع4۷1آ5 2711001 2ا0):

پارسی باستان (/۶8۸۹14۸ 11۸17۷:)012 ,۸۷۸ ۸ 0۷3
پهلوی (2۸(1۲1): 09,30 08 ب۸۷۳ لهستانی (۳0.187): 0۸ ,0
ارستی (0897/6): 1 چکک ((220). ۸ ,00
کردی (00157): اند صربی (/55814): 0۵۷۸7
افغانی (پشتر) (/7ل۸لا0 ۸7): 2 ,1۸ اسلواکی 5]07۸0): ۸ ,(0
تخاری 4 (۸ [(۸ل7ل707)+ 01

تخاری 8 (8 [(۸ل7077۸): 1 پسگشت‌ها 5
سانسکریت (8۸(/88207): ۸۸ 4 ۶005

ارمنی (۸/۵(/82/744): 1 7 (85) :1۸020/218
یرنانی 01828/0)+ | برهان قاطع : ۸۰
گرتبک (0077/0): 08 ,نا

اوستایی (1ل۸8874): 108۸۰ ایسلند یکهن (/5(/070/۸/۸ 2ا0): 07

پهلری (۲1اللمه): 10۴ نورس کهن (208۶82 صاه): 07
سانسکریت (54۸/58777): 108۸13 ,کف10 آلمانی کهن ((02791۸ 1/0 صا0):

برنانی ۰:08 130808 ,130805 0۸

لاتین (77ا): 11۸ آلمانی (08804۸۷): 07

فرانسه (4ل/۳822): 1017 انگلیسی کهن (للولا80/0 ۵ا۵: 0708
اسپانیایی (8۸(7/3): اد ان انگلیسی (باکلنا8(/0): 3
پرتغالی (۳0/7081882): ه1077 دانمارکی (0۸/150): 000 ۱
[pdf page 96]
0 میا
اوزار‌افزان ابزار / ‎٩۷‏
‏سوئدی (ل/550[3): 1۳
نروژی (/۵/08/8014(۷: 0 پسگشت‌ها 5
هلندی (ط07): 0 زر را
اسلاوی کهن (۲7۲بها5 864( 010): 0 (07788) 7
۸ ۷۷0۸ 7 (۵۷۲38) :للم ۳۲25
روسی (#551۸4۸): ۷100۸ 24 2/3
لیعرانی (711۸219۷/): 1208۸ 35 (07783) +00/700/3
لثرنی (لتی) (7۵ها): 105 7 (07788) :547
ایرلندی کهن (18757 صا0): ۰ 0001808
یادداشت+
این واژه را در هیچ فرهنگ فارسی نیافتم ولی واژه‌های اوستایی 11101۸۰ و پهلری 1101۸0 بنابه روایتی هنوز در
برخی از روستاهای مازندران و گیلان به کار می‌رود. شاید علت از مان رفتن این واژه در دیگر نواحی فلات ایران
این باشد که در اثر خشکه شدن آب و هواء اين جانور معدوم شده و لذا نام آن هم از ییاد رفته است. واژه‌ی
آدارموک" هم ممکن است از همین ربشه باشد گواینکه امروزه معنی آن عوض شده است.
اوستایی (47257407): ۸07۳۸ لترنی (لتی) ((7۷4مل): ۸7
پهلری (۲1ها7ل۸ه): م۸۲2۸ ایرلندی کهن (تلدلقا ا0): 7/۸
,۸3728 ولزی (1لک )+ 0
افغانی (پشتو) (۸7۳042/1): ۸ هیت (1777172): 1۳۷۸1 ,10۲۲-۲۵
ارمنی (۵//547/۸۷): ال
یه لین ووتمم: 006 رقن شاناه‌تآرهنای پسگشت‌ها 333
اسلاوی که (0ملاً نات صم: 6 ق۶030
071 :00 ,121117 رتا[ن12 0 (13872728) مد هام
لهستانی (5ا۳0): و زرد ۱2 9 (8[105) 802
روسی (8514(4نا): تا[نا12 ,لل1نا029 0 (0۲) #مقلو
ینوا نی ما71 5ل): 0 ,۸۷1 برهان قاطع : ۱۳۸
۸171 فرهنگ معین : ۳۵
[pdf page 97]
۸ اهریمن ‏ :
یادداشت.
۱ چون هیچکدام از پسگشت‌ها به رابطه‌ی واژه‌های فارسی و پهلری وکردی این فهرست با واژه‌ی اوستایی و دیگر
واژه‌های آن اشاره‌ای نکرده‌اند» در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام را
۲ واژه‌های لاتین 13۷0-0771۸88 (به چم "لاس" و آپوشاکه) و 8807۷1۸8 (به چم "پرست منار و یروا هن
آلباس") نیز از همین ربش‌اند. ۹
۳ چم اکثر واژه‌های غیرایرانی اين فهرست: پوشا کد» پوشیدن» کفش. :
اوستایی (488740): ,۸00 آلمانی کهن (0274۸00 107 صان):
۸ ۸۷63۸ ,11۸18۲55 61 ,۸۸6
پهلری (1/ماللمه): آلمانی (0874/۸00): نداد
۸13۸1 ,۸13813۸۵ انگلیسی کین (5#لا2۷0 صا): 8۲05
۱ سانسکریت (54(/872077): 1 انگلیسی (۸/01/870): ۸
(۵(18-813801) -ناتتان۸ بشاانا ۸/28 هلدی (ل0770): 16
17 ,ک۸ا۸2 ایرلندی کهن (574ل18 010):
ارمنی (/(4/8714): ۸ 06 00005
برنانی 088/0): ۸076173181 ,۸1071181 سلتی (کلتی) (۴8776): ۸16 ,6تآه۸ت[8
لاتین ((7ضا):
5 ,۸008 ,۸1087115 دا6ن۸ پسگشت‌ها گر
فراسه (۳۸/04): 1555 60 0و2
ایتالیایی (/(۸لمله): ۸0501۸ 4 (۸(08) +17
پرتغالی (۳0717010295): ۸015۸ 7 (۸111۸) ۸/21
گرتیک (00771/6): ۸۳۷0۷۷5 ,۸001۷108 :010/5
ایسلندی کهن (0107۸74۸(ه52 0ا0): 7 (1اقاآناع اند م1658ه۸)
7 ب۸۷0 برهان قاطع : ۸۹
ساکسونی کهن ((54340 ا0): 6
یادداشت:
۱ چم این واژه در زبان‌های رومانس: تنگی‌خاطر» تشویش.
چم اين واژه در زبان‌های ژرمنی: ننگی؛ تنگه» باریکك.
چم این واژه در زبان انگلیسی نوین: خشم.
[pdf page 98]
اهورا هرمز اهورامزدا / ۹۹
چم این واژه در زبان ابلندی کهن: اندوه» غم.
ریشه‌ی اوستایی این واژه دارای دو بخش است» بخش نخست آن در این ,فهرست پیگیری شده است» برای
شناخت بخش دوم آن به آمنش " بازگشت شود.
ِ
اوستایی (//472374): ۰ برشقاناتل۸ ,دلاقل۸ 055
۸ نررس کهن (۸/078 010): وق
پارسی باستان (/(۳8۵]۸ 010): ۰ بشااتا۸ انگلیسی کهن (تلولسا8۸0 010): 08
۸۸3/۸70۸3
پهلوی (1اتلمم): 0۸0 پسگشت‌ها شرت دی
00 2000
سانسکریت (54(79807): ,8ناقم وتاق۸ 31 بطل2/ 2/۸02
۸ + ۶۲۵۶ ال ب‌لقطلله ۱
پرنانی 076220): 5 41 (ت51ه) ۱
گوتیکه (007[7/0): 8 ,۸۷855 برهان قاطع + ۹ ۱
ایسلند ی‌کهن (070۸1۸7/(م5 0ا0): 0
اوستایی (4/:37۸4): 10۸ پرتغالی (۳0/71701888): آتا۸0
پارسی پاستان (۷(ای۳8 ۰۰:۵۵ ۸۲۸ ابرندی کهن (تتکلها صا۵): 10
۲ پهلری (۸(1ات۸): ۰ 8۸۷-۰ ,50۸3 ,3:۸3 گالی (5لله0): 0
۹ "کرد (68[/8: ,۷1۸ ,160۸ بشا1[13
ا سانسکریت (5/580007): ۰۰ ب8ل1 با17۸738[ پسگشت‌ها 5
۸ 9 ت20
یرنانی 076870): 17۸[ 7 (161) :ما05
لاتین (7100مل): از 30 :۱25
فرانسه (۳88(07): 1 5 (118۳) ۸/700
اسپانیایی (۸/18[3ط6): ۸01 برهان قاطع : 1۹۳
ایتالیایی (۷(فله)): 011
[pdf page 99]
۰ / ایرمان (به چم "مهمان"» "دوست")
اوستایی (/۵۲57): ۸۵180 رال۸۱/۸ ۸18۷ پسگشت‌ها 5
پارمی باستان (۷(فا2878 صا0): 28/۸ 7 ۶۸005200
پهلری (۲7ماتنهم): 83۸1۸0۲ ,۸۳58۸۸201 5 (۲81310) . :۸/۸215
اوستی (0558716): ۸ ,1110 برهان قاطع + 1۹۶
سانسکریت (7ل6۸(۶82): ۸27۷۸۵۸ فرهنگ معین : ۴۵
ایرلندی کهن (3نق1 صا0): ۸138611 ب8ل۸ لفت‌نامه دهخدا: ۳۷۷
: یادداشت: ‏ "
۱ ۱- چم این واژه در ایرلندی کهن: اشرافی» رادمرد. (جالب اینکه در پهلوی نیز واژه‌ی 58 به چم "رادمرد" و
آقهرمان" بود).
چم این واژه در زبان اوستایی؛
```


## [2026-09-07T16:25:23.734Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('MANUS. HAVESTAN')\nprint(t[i-1800:i+900])\nEOF",
 "description": "ARY latin index MANUS context"
}
```


### [2026-09-07T16:25:24.952Z] TOOL RESULT

```
LATVIAN) (3) giz
ONIONS: (MAMMA) 549 OLD IRISH) pS 54) p',
SKEAT: (MAMMA) 358 MAMA, MAM
MALLORY & ADAMS: M-AM MAM (WELSH) $3
14FA sei oby MAM H(BRETON) «gi
seth
as” ing “al” Y AT tll 9 25) apr alt 9 He SHdL (l La Sel ge
Ggghs ages ya oT ghb ele ab Gp MATER) "al guts iy OT stats gis St st
ced tS aay oly cpl SASh ool lt AS
has LE ig LST 5 Sli 2 05a cal eae oT
dy IES 3h 4 ody 2 MOMMY s0jly wor
ARMENIAN) .g,! MANA, DaMANA :(AVESTAN) gles!
‘TANU., (TANU-TER) MANIYA — (OLD PERSIAN) dul gos),
DOM6s, DOMA (GREEK) gb» (PAHLAVI) 5 34
DOMUS, DOMO LATIN) oo) MAN, MANISHN, MAND
DOME (FRENCH) 4313 MAL (KURDISH) 53,
DOMO (SPANISH) glibee! TTAM., TAM: :(TOKHARIAN A) A 5 55
DoMo PORTUGUESE) U5 A(TOKHARIAN B) B 5 j\53
(OLD SCANDINAVIAN) 6S 541! TEM, TAM., TSAM-
TIMBR Damp, SANSKRIT) oy Site
TIMBAR — (OLD SAXON) nS -S (DAMU-NAS), MANAH, DAMAS
[pdf page 460]
TEN | (lens colaga clap ya— ated yo 3 a" 9 ay) OLE
DUM BOHEMIAN) | aa y TIMBER — (OLD FRISIAN) oS 5.3
DOM, DOMA (SLOVAK) gsi HOLD HIGH GERMAN) oy lst
NAMAS LITHUANIAN) «y:3 ZIMBER
NAMS LATVIAN) (3) gh ZIMMER HAGERMAN) galt
DAMNAE — (OLD IRISH) 24553 p\ TIMBER (OLD ENGLISH) 4S S61
DEFNYDD WELSH) 5) TIMBER ENGLISH) JSi1
DEFFNEZ (BRETON) 5 4 TOMMER s(DANISH) Sjlsl>
TIMMER (SWEDISH) (5. yo
‘REFERENCES beth TOMMER (NORWEGIAN) (539 ;
POKORNY SSSS~SC«.I99 TIMMER (DUTCH) «gala
BARNHART: (DOME) 294-295 (OLD CHURCH SLAVIC) 46,5 sh
DELAMARRE: (MAISON) 59 DoMU
‘MACKENZIE: (HOUSE) 118 DOM (POLISH) leg)
BUCK: (HOUSE) 457.459 DOMA, DOM ARUSSIAN) yoy
rVIA fog Kas DOM, DOMAcf CZECH) Se
rer ieboby DoM SERBIAN) 93 po
lethal
29 g-ASHOUSE AND HOME (A Coley “ls ) XAN UD MAN 5 ly obj 52-1
SE AS 33 SOIL; 22 Sy cel oY |
Ud GST Ob 5 42 aly, le
Becta ieee y satay golStl BladL5 32 Sly cal
2 AF ia piles BOdUs 2205 oul oe
ns
pan anton | A
MAN HOLD SAXON) AS iy Se MANUS. HAVESTAN) glory!
MONN HOLD FRISIAN) oS 53.3 “MAN (ZAR-MAN) (PAHLAVI) 5 ly
MAN (OLD HIGH GERMAN) pf lal MANU, MANUS (SANSKRIT) ey Sails
MANN (GERMAN) gist MANNA GOTHIC) Sa F
HOLD ENGLISH) oS pul) (OLD SCANDINAVIAN) 35 (g-thu\
MANN, MON, MANNA MATHA, MANNR
[pdf page 461]
| oul | FFT
MUZE (BOHEMIAN) gua y MAN HENGLISH) .5J6it
MAND (DANISH) Sails
REFERENCES y pie ‘ beth MAN (SWEDISH) 54h yo
k POKORNY:* 700 MAND. NORWEGIAN) «5595
BARNHART: (MAN) 627 MAN (DUTCH) sha
‘DELAMARRE: (HOMME) 51, 74 (OLD CHURCH SLAVIC) ot 6!
MACKENZIE: (MAN) 122 MOZHI
| | ontons: (MAN) $50 MAZH HPOLISH) gling)
SKEAT: (MAN) 358 MUZH RUSSIAN) 3
MUZH H(SERBIAN) 9 pe
RIMANERE “ITALIAN) gills! MAN, MANAYA —:(AVESTAN) ogi
RAMINERA (RUMANIAN) seg (OLD PERSIAN) kos go 34
AINMNE HOLD IRISH) <5 3p! MAN-, MANAYA
MB-IMNA, MEIMMAL (HITTITE) <2 PAHLAVI) 534,
MAN., MANDAN, MANISTAN
"REFERENCES eat MAIN, MANDU (KURDISH) 62,
```


## [2026-09-07T16:25:36.576Z] TOOL CALL #71: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T16:25:36.584Z] TOOL RESULT

```


```


## [2026-09-07T16:25:41.455Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%9C%CE%BF%E1%BF%A6%CF%83%CE%B1",
 "prompt": "Give the full etymology section for Ancient Greek Μοῦσα (Moûsa): all proposed derivations, which are accepted/rejected, and cited scholars (Beekes, Pokorny, etc.)."
}
```


## [2026-09-07T16:25:42.867Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%86%D9%88%DA%86%D9%87%D8%B1",
 "prompt": "Give the full etymology of Persian منوچهر (Manuchehr): Middle Persian and Avestan forms, meaning of each element, and any cited sources."
}
```


### [2026-09-07T16:25:48.642Z] TOOL RESULT

```
# Etymology of منوچهر (Manuchehr)

Based on the Wiktionary entry provided, here is the etymological information available:

## Origin
The word derives from **Avestan** _manušciθra_. The entry notes it is "akin to" Old Armenian _Մանաճիհր_ (Manačihr), which itself represents an Iranian borrowing.

## Meaning of Elements
Unfortunately, the source document does not provide a detailed breakdown of the individual morpheme meanings within the Avestan or Middle Persian forms. It only identifies the Avestan etymon without semantic component analysis.

## Limited Documentation
The entry does not cite specific academic sources for the etymology, nor does it provide intermediate Middle Persian forms. The connection to Old Armenian is noted but marked as a related borrowing rather than a direct descendant in the main entry (though descendants do include Middle and Modern Armenian forms).

For more comprehensive etymological details about individual elements and scholarly sources, consulting specialized Persian etymological dictionaries or academic works on Iranian languages would be necessary.
```


### [2026-09-07T16:25:49.343Z] TOOL RESULT

```
# Etymology of Ancient Greek Μοῦσα (Moûsa)

The origin of this word remains disputed, with multiple competing theories:

**Proto-Indo-European Derivations:**

1. **From *Μόνθια (*Mónthia)**: Scholars propose this derives from PIE *men- ("to think") + *dʰeh₁-, connecting to μανθάνω (manthánō). "Among theories supposing an Indo-European origin, this is considered most appealing by Beekes."

2. **From *Μόντια (*Móntia)**: Another PIE theory links *men- ("to tower; mountain") to the Muses' mountain cult centers. However, Beekes rejects this, noting the root *men- ("mountain") lacks other Greek attestations.

3. **Pokorny's Theory**: This scholar derives the word from PIE *moh₁-/*meh₁- ("endeavour, will, temper"), comparing related Greek terms (μῶμαι, μαίομαι, μαιμάω) and cognates in Latin (mōs), English (mood), and Proto-Slavic.

**Alternative Theories:**

4. **Pre-Greek Substrate**: Beekes suggests possible borrowing from Pre-Greek with proto-form *mont͏̌a, "though there is no evidence for or against substrate origin."

5. **Egyptian Origin**: Swerdlow traces it to Bohairic Coptic Egyptian mōw, cognate with Hebrew משה (moshé, "Moses"), citing medieval sources connecting music to water.
```


## [2026-09-07T16:25:54.139Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mannequin",
 "prompt": "Give the full etymology entry for mannequin, and also for manikin if shown on the page."
}
```


## [2026-09-07T16:25:56.006Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9n-mn%CC%A5",
 "prompt": "What does this page say? If it is the PIE root *men- 'to think', list the root, its meaning, and derived terms in Latin, Greek, Avestan."
}
```


### [2026-09-07T16:25:57.372Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:25:59.696Z] TOOL RESULT

```
# Etymology Entries

## Mannequin

The word "mannequin" dates to 1898, meaning "model to display clothes." It derives from French *mannequin* (15c.), which comes from Dutch *manneken*, literally "little man." Originally referring to people serving as models, the term later shifted to describe artificial human figures for displaying clothing around 1853 in French translations, though it didn't become common in English until circa 1930. An earlier English term for such artificial models was "tailor's dummy" (1889).

## Manikin

"Manikin" appears from the 1560s, denoting "jointed model of the human figure used by artists." It originates from Dutch *manneken*, meaning "little man"—a diminutive of Middle Dutch *man*, which traces back to Proto-Germanic *\*manwaz* and the Proto-Indo-European root *\*man-* meaning "man." The entry notes that "sense and spelling often blended" with mannequin.
```


## [2026-09-07T16:26:03.867Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-",
 "prompt": "List the PIE roots *men- given on this page with their meanings, and for the one meaning 'to think' list the derived terms in Latin, Ancient Greek, Avestan, Proto-Germanic."
}
```


## [2026-09-07T16:26:04.827Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Ahura_Mazda",
 "prompt": "Give the full etymology of Ahura Mazda: Avestan form, analysis of mazdā-, the PIE reconstruction, Middle Persian forms, and cited sources."
}
```


### [2026-09-07T16:26:08.477Z] TOOL RESULT

```
# Proto-Indo-European *men- Roots

The page lists four distinct PIE roots with *men-:

1. **to think, mind** (perfective) - "spiritual activity"
2. **to stay, remain**
3. **to stand out, tower**
4. **small, isolated**

## Derived Terms for "to think" Root

**Latin:** memor ("mindful")

**Ancient Greek:** μνήμων (mnḗmōn, "mindful"); μνημοσύνη (mnēmosúnē, "memory")

**Avestan:** 𐬨𐬀𐬧𐬙𐬁 (maṇtā, "minded one")

**Proto-Germanic:** *minþijō, leading to English minion via Old French mignon
```


### [2026-09-07T16:26:10.689Z] TOOL RESULT

```
# Etymology of Ahura Mazda

Based on the Wiktionary content provided, here's what can be established:

## Avestan Form
The term derives from Avestan **𐬀𐬵𐬎𐬭𐬀 𐬨𐬀𐬰𐬛𐬁** (ahura mazdā), which is described as a "transliteration" of this ancient Iranian language.

## Limited Etymological Detail
Unfortunately, the source material does not provide:
- A detailed analysis of the *mazdā-* component or its semantic breakdown
- Proto-Indo-European (PIE) reconstruction
- Middle Persian cognate forms beyond modern Persian variants
- Scholarly citations or sources discussing the etymology

## What Is Documented
The page only notes that Ahura Mazda is a "doublet" of related terms like *Aramazd* and *Hormuz*, suggesting linguistic variations across different language families and historical periods that borrowed this term.

For comprehensive etymological analysis including PIE roots and Middle Persian attestations, you would need to consult specialized historical linguistics sources or more detailed academic references beyond this dictionary entry.
```


## [2026-09-07T16:26:16.571Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B2%D9%82%D8%A7%D9%86",
 "prompt": "Give the full entry for Persian مزقان: meaning and etymology (is it from موسیقی or from French/Russian musique/music?)."
}
```


## [2026-09-07T16:26:17.984Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/music",
 "prompt": "Give the etymology of music, and any linked entries visible for museum, mosaic, amnesty, maniac, automatic — the Greek/Latin/French chain for each."
}
```


### [2026-09-07T16:26:18.158Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T16:26:23.243Z] TOOL RESULT

```
# Etymology Response

## Music
**Origin chain:** Greek *mousikē* (art of the Muses) → Latin *musica* → Old French *musique* → English *music* (mid-13c.)

The term derives from "the Muses," daughters of Zeus in classical mythology who protected the arts.

---

## Linked Entries from the Page

The provided content only includes **Muse** and **folk-music** as linked entries with full information:

**Muse:** Greek *Mousa* → Latin *Musa* → Old French *Muse* → English (late 14c.). Traces to PIE root *\*men-* meaning "to think."

**Folk-music:** English compound combining *folk* + *music* (1852), modeled on German *Volksmusik*.

---

## Unavailable Entries

Museum, mosaic, amnesty, and maniac do not appear on this etymology page for "music." To provide their etymological chains, I would need access to their respective dictionary entries, which this source document does not contain.
```


## [2026-09-07T16:26:29.374Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mosaic",
 "prompt": "Give the etymology of mosaic (Medieval Latin, Greek, French chain) and how it relates to the Muses."
}
```


## [2026-09-07T16:26:30.098Z] TOOL CALL #81: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/amnesty",
 "prompt": "Give the etymology of amnesty: Greek amnestia, Latin, French chain, and the PIE root."
}
```


### [2026-09-07T16:26:34.537Z] TOOL RESULT

```
# Etymology of Mosaic

The word "mosaic" traces back through Medieval Latin to Italian and Old French origins. According to etymonline, the term comes "from Old French _mosaicq_ 'mosaic work,' from Italian _mosaico_, from Medieval Latin _musaicum_."

## Connection to the Muses

The Medieval Latin form reveals the artistic connection: "_musaicum_ 'mosaic work, work of the Muses,' noun use of neuter of _musaicus_ 'of the Muses,' from Latin _Musa_." The entry notes that "Medieval mosaics often were dedicated to the Muses," establishing a cultural link between these intricate artworks and the classical goddesses of inspiration.

Interestingly, while Medieval scholars created this term as though deriving it from Greek, the actual Greek word for mosaic work was _mouseion_. The etymology suggests that "this sense in Greek was borrowed from Latin," making the pathway somewhat circular—the Latin term referencing the Muses was later adopted back into Greek rather than originating there.
```


### [2026-09-07T16:26:35.747Z] TOOL RESULT

```
# Etymology of Amnesty

**PIE Root:** The word traces back to "*men-" meaning "to think," which underlies numerous English words related to thought and memory.

**Greek Origin:** The Greek term "amnestia" meant "forgetfulness (especially of wrong); an amnesty," derived from "amnestos" (forgotten; forgetful). This combined the prefix "a-" (not) with "mnestis" (remembrance).

**Latin and French Chain:** The Greek "amnestia" became Latin "amnestia," which then passed into French as "amnistie" (intentional overlooking) in the 16th century.

**English Adoption:** The word entered English around the 1570s as "a ruling authority's pardon of past offenses," borrowing directly from the French form. It was first used as a verb in 1809.

**Modern Usage:** The organization Amnesty International, founded in 1961 as an "Appeal for Amnesty," popularized the term in contemporary contexts focused on prisoners of conscience.
```


## [2026-09-07T16:26:41.661Z] TOOL CALL #82: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B2%D9%82%D8%A7%D9%86/",
 "prompt": "What do the dictionaries (Dehkhoda, Mo'in, Amid) say about مزقان — its meaning and origin? Quote the entries."
}
```


## [2026-09-07T16:26:42.884Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/monster",
 "prompt": "Give the etymology of monster: Latin monstrum, its relation to monere, and the PIE root. Also any note on monstrare/demonstrate."
}
```


### [2026-09-07T16:26:47.021Z] TOOL RESULT

```
# Dictionary Entries for مزقان

**Dehkhoda Lexicon:**
"مزقان. [ م ِ ] ( اِ ) مزغان. رجوع به مزغان شود" — directs readers to the entry for مزغان.

**Farsi Dictionary:**
The term is listed as a noun with three meanings: musicians, a group of various musical instruments played together in an ensemble, and music itself.

**Amid Dictionary:**
Lists three definitions: (1) colloquial usage for music, (2) colloquial usage for a musical instrument, and (3) a military term (now obsolete) referring to "a group of different musical instruments that were played together in formation."

All three sources connect the word fundamentally to music and musical performance.
```


### [2026-09-07T16:26:49.268Z] TOOL RESULT

```
# Etymology of Monster

**Latin Origin & Monere Connection:**
The word "monster" comes from Latin *monstrum*, which meant "divine omen (especially one indicating misfortune), portent, sign; abnormal shape; monster." This derives from *monere*, meaning "to remind, bring to (one's) recollection, tell (of); admonish, advise, warn, instruct, teach."

**PIE Root:**
Both *monere* and *monstrum* trace back to the Proto-Indo-European root *\*moneie-*, described as "to make think of, remind"—a causative form of *\*men-* meaning "to think."

**Monstrare & Demonstrate:**
The Latin verb *monstrare* ("to point out, show") shares the same *monstrum* root. This verb underlies English "demonstrate," which entered the language around 1550. The prefix *de-* combines with *monstrare* to create the sense of pointing something out entirely or establishing truth through evidence.

**Historical Shift:**
Initially, abnormal animals were interpreted as signs of impending evil. By the late 14th century, the meaning expanded to include fabulous composite creatures, and by the 1550s, it came to describe morally deformed or cruel persons.
```


## [2026-09-07T16:26:54.361Z] TOOL CALL #84: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B2%D8%BA%D8%A7%D9%86/",
 "prompt": "What do Dehkhoda, Mo'in and Amid say about مزغان — meaning and origin (is it derived from موسیقی or from موزیک / French musique)? Quote the entries."
}
```


## [2026-09-07T16:26:55.697Z] TOOL CALL #85: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%80%F0%90%AC%B0%F0%90%AC%9B%F0%90%AC%81",
 "prompt": "Give the entry for Avestan mazdā: meaning, etymology (PIE reconstruction), and descendants."
}
```


### [2026-09-07T16:27:00.846Z] TOOL RESULT

```
# Origins of مزغان According to Persian Dictionaries

**Dehkhoda Dictionary** traces it to French:
> "این لفظ محرف موزیک فرانسوی است که با الف و نون فارسی جمع بسته شده"

This indicates the word is a corruption of French "musique" (موزیک), which received Persian plural suffixes (-ان).

**Mo'in Dictionary** provides minimal information, listing only:
> "(مِ ) [ فر - فا. ] (اِ. )۱ - ساز. ۲ - آلت موسیقی"

It classifies the term simply as a musical instrument or music device, without discussing etymology.

**Amid's Dictionary** (Farhang-e Farsi) offers:
> "( اسم ) ۱ - موسیقی دانان . ۲- دسته ای از سازهای مختلف موسیقی که در نظام با هم نوازند"

It defines مزغان as musicians or orchestral instruments but similarly omits etymological detail.

**Conclusion:** Only Dehkhoda explicitly addresses origin, attributing it to French musique rather than deriving it from Persian موسیقی.
```


### [2026-09-07T16:27:01.147Z] TOOL RESULT

```
# Avestan mazdā Entry

**Meanings:**
The term denotes "(Zoroastrianism) Mazda" and also means "wisdom."

**Etymology:**
The word traces back through multiple proto-languages. It derives from Proto-Iranian *mazdáH, which came from Proto-Indo-Iranian *mazdʰáH. The ultimate source is Proto-Indo-European *mn̥s-dʰéh₂, stemming from *men(s)dʰh₁- meaning "to pay attention, wisdom."

**PIE Reconstruction:**
The relevant reconstruction is *men(s)dʰh₁-, denoting concepts of attention and wisdom.

**Notable Cognate:**
Sanskrit medhā́ (मेधा) shares the same etymological root, demonstrating the word's distribution across Indo-European language families.
```


## [2026-09-07T16:27:11.553Z] TOOL CALL #86: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%88%D8%B2%D9%87/",
 "prompt": "List the separate senses/entries for موزه in Mo'in and Dehkhoda: which one is the boot (چکمه) and which one is the museum, what origin tag each carries (e.g. [فر. musée]), and whether Mo'in numbers them موزه (۱) and موزه (۲)."
}
```


## [2026-09-07T16:27:12.525Z] TOOL CALL #87: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87",
 "prompt": "List all Persian entries for موزه with their etymologies — the boot sense and the museum sense (from French musée?)."
}
```


### [2026-09-07T16:27:17.544Z] TOOL RESULT

```
# موزه: Separate Senses in Mo'in and Dehkhoda

## Mo'in (معین)

Mo'in lists **two distinct entries**:

1. **موزه (۱)** – "چکمه" (boot)
   - Origin tag: [په.] (Pashto) and [اِ.] (Arabic)

2. **موزه (۲)** – Museum sense
   - Origin tag: [فر.] (French)
   - Definitions: "مجموعه آثار باستانی" (collection of antiquities) and "محلی که آثار باستانی را در آن نگه داری کنند" (place where antiquities are kept)

## Dehkhoda

Dehkhoda presents **multiple historical entries** under موزه without formal numbering:

- **Boot sense**: "به ترکی چکمه گویند" (called boot in Turkish) – origin from Turkic
- **Museum/treasury sense**: Multiple citations from classical Persian texts, including references to "گنجینه" (treasure house)

The boot sense is etymologically Turkic; the museum sense reflects broader meanings of collection and preservation in classical usage.
```


### [2026-09-07T16:27:18.654Z] TOOL RESULT

```
# موزه (Moze) - Persian Dictionary Entry

The Persian word **موزه** has two distinct meanings:

## Etymology 1: Boot
Derived from Middle Persian *mōzag* ("shoe"), tracing back to Proto-Iranian *hmáwčati* ("to clothe"). This sense appears in historical texts, such as an 11th-century work by Abulfazl-i Bayhaqī describing "a new Michaelic boot on the foot."

## Etymology 2: Museum
"Borrowed from French *musée*." This modern usage refers to a museum and is specifically used in Iranian Persian, with alternate forms in Dari and Tajik.

Both meanings are documented as Persian nouns with their respective plural forms (موزه‌ها in Persian dialects). The word demonstrates how a single term can retain an ancient footwear meaning while simultaneously adopting a contemporary European loanword sense.
```


## [2026-09-07T16:27:41.308Z] TOOL CALL #88: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mathematics",
 "prompt": "Give the etymology of mathematics: Greek mathematike/mathema, manthanein, the PIE root, and the Latin/French/English chain."
}
```


## [2026-09-07T16:27:42.381Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mens",
 "prompt": "Give the Latin entry for mens: meaning, declension (mens, mentis), vowel length, and etymology (PIE reconstruction), plus descendants."
}
```


### [2026-09-07T16:27:46.101Z] TOOL RESULT

```
# Etymology of Mathematics

**Greek Origins:**
The word traces to Greek *mathēmatike tekhnē* ("mathematical science"), derived from *mathēma* meaning "that which is learnt." This stems from *manthanein*, "to learn."

**Proto-Indo-European Root:**
The ultimate source is the PIE root *\*mendh-*, meaning "to learn."

**Romance Language Transmission:**
From Latin *mathematica* (plural), the term passed through Old French *mathematique* before entering Middle English as *mathematik* around the late 14c.

**English Development:**
The modern form *mathematics* emerged in the 1580s, combining the noun form with the suffix *-ics*. The older singular *mathematic* was eventually replaced, though shortened forms like *math* (American English, 1890) and *maths* (British English, 1911) later developed.

**Historical Context:**
Originally, mathematics was one of three branches of Aristotelian theoretical science, alongside metaphysics and natural philosophy.
```


### [2026-09-07T16:27:48.873Z] TOOL RESULT

```
# Latin Entry for Mens

**Meaning:** Mind, intellect, reason, thought, plan, purpose, intention, heart, conscience, and disposition.

**Declension:** Third-declension i-stem feminine noun. Nominative singular: *mēns*; genitive singular: *mentis*; accusative: *mentem*; ablative: *mente*. Plural forms include nominative *mentēs* and genitive *mentium*.

**Vowel Length:** The initial vowel is long (*mēns*), pronounced as a long vowel in Classical Latin.

**Etymology:** Derived from Proto-Italic *mentis*, ultimately from Proto-Indo-European *méntis* meaning "thought." The entry notes that this root is "cognate with Sanskrit मति (matí), Ancient Greek μάντις (mántis), Russian мнить (mnitʹ, 'to think'), Old English ġemynd (whence English mind), and Lithuanian mintis ('thought')."

**Major Descendants:** The word produced numerous Romance language descendants including Italian *mente*, Spanish *mente*, French *-ment* (adverbial suffix), Portuguese *mente*, Romanian *minte*, and Catalan *ment*. It also influenced adverbial constructions across Romance languages through the *-mente* suffix pattern.
```


## [2026-09-07T16:28:04.606Z] TOOL CALL #90: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mannaz",
 "prompt": "Give the etymology of Proto-Germanic *mannaz: PIE reconstruction, whether it is linked to *men- 'to think', Sanskrit/Avestan cognates, and descendants (Gothic manna, Middle Dutch man)."
}
```


## [2026-09-07T16:28:05.557Z] TOOL CALL #91: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/maniac",
 "prompt": "Give the etymology of maniac and mania: the Greek, Late/Medieval Latin and French chain, and the PIE root."
}
```


### [2026-09-07T16:28:10.248Z] TOOL RESULT

```
# Etymology of Proto-Germanic *mann-

## PIE Origins

The word derives from Proto-Indo-European **\*mon-** ("man") or **\*men-** ("to mind; to stay"). An alternative theory, favored by Kroonen following Berneker, proposes derivation from PIE **\*(dʰ)ǵʰmō, \*(dʰ)ǵʰmon-** ("human"), with the initial consonant cluster reduced in Germanic to produce \*(-)man-.

## Cognates

The page does not explicitly list Sanskrit or Avestan cognates, though it references comparative Indo-European evidence supporting the etymology.

## Documented Descendants

**Gothic:** 𐌼𐌰𐌽𐌽𐌰 (manna)

**Middle Dutch:** man

**Old English:** mann, man, manna (consonant stem forms)

**Old Norse:** maðr

The widespread Germanic reflexes across Gothic, West Germanic, and North Germanic branches attest to the word's antiquity in the proto-language, demonstrating the robust nature of this etymological reconstruction.
```


### [2026-09-07T16:28:10.792Z] TOOL RESULT

```
# Etymology of Maniac and Mania

**Maniac** (adj., c. 1600) derives from French *maniaque* (14c.), which came from Late Latin *maniacus*, ultimately from Greek *maniakos*—all stemming from the noun *mania*.

**Mania** (n., late 14c.) comes from Late Latin *mania* "insanity, madness," borrowed from Greek *mania* meaning "madness, frenzy; enthusiasm." The Greek term relates to *mainesthai* "to rage, go mad" and *mantis* "seer."

**PIE Root**: The word traces back to the Proto-Indo-European root *\*men-* (1), "to think," which produced "derivatives referring to qualities and states of mind or thought."

The noun form of *maniac* ("one affected with mania, a madman") is attested by 1763, derived from the earlier adjective.
```


## [2026-09-07T16:28:28.612Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/Μοῦσα|page 332 entry 0 node 1: Greek Mousa origin (Beekes, Pokorny, Pre-Greek)' \\\n 'https://en.wiktionary.org/wiki/منوچهر|page 332 entry 1 node 2: Persian Manuchehr from Av. manuščiθra' \\\n 'https://www.etymonline.com/word/mannequin|page 332 entry 1 nodes 4/6: French mannequin < Dutch manneken; manikin' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-|page 332 entry 0 root: PIE men- to think' \\\n 'https://en.wiktionary.org/wiki/Ahura_Mazda|page 332 entry 2 node 2: Ahura Mazda doublets Hormuz' \\\n 'https://www.etymonline.com/word/music|page 332 entry 0 nodes 3/6: Gk mousike > L musica > OFr musique > E music' \\\n 'https://www.etymonline.com/word/mosaic|page 332 entry 0 nodes 5/6: ML musaicum work of the Muses' \\\n 'https://www.etymonline.com/word/amnesty|page 332 entry 0 node 6: Gk amnestia < men-' \\\n 'https://abadis.ir/fatofa/مزقان/|page 332 entry 0 node 4: Persian mazqān = mazghān, music' \\\n 'https://abadis.ir/fatofa/مزغان/|page 332 entry 0 node 4: Dehkhoda mazghān = corrupted French muzik + Persian plural -an' \\\n 'https://en.wiktionary.org/wiki/𐬨𐬀𐬰𐬛𐬁|page 332 entry 2 node 1: Avestan mazda < PIE *mns-dheh2' \\\n 'https://www.etymonline.com/word/monster|page 332 entry 0 node 8: L monstrum < monere, causative of men-' \\\n 'https://abadis.ir/fatofa/موزه/|page 332 entry 0 node 5: Moin numbers muze(1)=boot [Pahlavi], muze(2)=museum [French]' \\\n 'https://en.wiktionary.org/wiki/موزه|page 332 entry 0 node 5: Persian muze boot < MP mozag vs museum < Fr musee' \\\n 'https://www.etymonline.com/word/mathematics|page 332 entry 2 node 4: mathematics < Gk manthanein, PIE mendh-' \\\n 'https://en.wiktionary.org/wiki/mens|page 332 entry 0 node 7: Latin mens, mentis long e, PIE *mentis' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mannaz|page 332 entry 1 node 3: PGmc *mannaz, Kroonen dhghmon- alternative' \\\n 'https://www.etymonline.com/word/maniac|page 332 entry 0 node 6: maniac < Gk mania < men-' \\\n ; do\n url=\"${u%%|*}\"; note=\"${u##*|}\"\n python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone",
 "description": "Archive all web sources"
}
```


### [2026-09-07T16:28:38.967Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/404eb01191149d95.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82bf74180715df36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/deec2d64efdf6143.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f249e87bde5d28c8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c93d75a030a9b8ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cfd5c6b90c7d1da3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8855d96039b7b93a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/652ae1b36e744850.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa54f8258803318e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14fadf232f929e51.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92b78456fe38dc0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96961c138bd7fbbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8776bd6f4bd42344.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b41117e19100a38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/639c653028cf6a4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/78a7467fc2d43895.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cf40d4c21f28bce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e501413a3fa4a851.txt
```


## [2026-09-07T16:28:50.118Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef show(f, pats, n=1, w=(90,220)):\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,e); return\n    for p in pats:\n        for m in list(re.finditer(p,t))[:n]:\n            print(f.split('/')[-1],'|',p,'>>',repr(t[max(0,m.start()-w[0]):m.end()+w[1]]))\n        else: pass\nshow('SKT.txt',[r'\\nMan, ', r'\\nMusic, ', r'\\nMuse, ', r'\\nMosaic', r'\\nMathematic', r'\\nMental', r'\\nMonster', r'\\nManikin'])\nprint('==== LEW')\nshow('LEW_1910.txt',[r'\\nmens, ', r'\\nmoneo', r'\\nmonstrum', r'\\nMusa'])\nprint('==== LAT')\nshow('LAT.txt',[r'mens, mentis', r'\\nmens\\b', r'moneo,'])\nEOF",
 "description": "Grep Skeat, LEW, LAT"
}
```


### [2026-09-07T16:28:51.422Z] TOOL RESULT

```
SKT.txt | \nMosaic >> "f  an  arrow),  very  tenacious  ^s&id  ol'  a roiserV\nMortmain,  Mortuary ;  see  Mortal.\nMosaic ;  see  Muse  (}).\nMoslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  pro"
SKT.txt | \nMental >> 'nnection  of  its action  with  the  phase&  of  the  nu>on.\nMenffuration:  see  Meaiiure.\nMental.  (F.«>L.  1  F.  mrn/o/.  —  Low  L. mcntaiu,  mental.  *L.  nun/-,  stem  oC  ttuns^ mind.     (V-MAN."*\ncomment.  (F.«»L.)  ¥.  eommeHter.^ L.  commenfari,  to  consider,  make  a  note  on. — L.  commeatus,  pp.  of'
SKT.txt | \nMonster >> 'oon,  year.  — Arab. mawsim,  a  time,  season.  —  Arab,  -uxum (root  wasamd)^  marking.\nMonster;  see  Monition.\nMonth ;  sec  Moon.\nMonument ;  see  Monition.\nMood  (i),  dlspoiilion  of  mind.  (E.) Prob.  sometimes  confused  with  mood  (a), but  properly  di«tincl.  M,  £.  mood,  miiKl. also  temper,  anger,'
==== LEW
==== LAT
LAT.txt | \nmens\b >> 'Sndyati, av. ntpnayeiti.\nIl y a deux formes de thbme en ~ti~, l\'une relativement ancienne,\nmens, cf. skr. matih "pensee", 1\'autre, de type italo-celtique, mentio ,\ncf. iri. air-nitiu "respect". La forme mens a ^te detachee, comme la\nforme mors , des formes composees; cf. got. ga-munds, lit. at-nintis ,\nv.sl.pa-mft'
LAT.txt | moneo, >> "nstance de -e- dans les formes latines exclut\n1'hypothese d'un ancien causatif du type de moneo, monui, monitus. -\nLes formes latines, alimentum , etc., indiqueraient une racine dissylla-\nbique; mais altus ne concorde pas.\naloglo, -as, -are: a rationis tramite deuiare (Aug.Ep.36). Emprunt\nt ardif au gr. aXoyew.\nalo"
```


## [2026-09-07T16:29:04.170Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndef show(f, pats, n=2, w=(60,260)):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for p in pats:\n        ms=list(re.finditer(p,t))[:n]\n        if not ms: print(f.split('/')[-1],'|',p,'>> NOT FOUND')\n        for m in ms:\n            print(f.split('/')[-1],'|',p,'>>',repr(t[max(0,m.start()-w[0]):m.end()+w[1]]))\nshow('SKT.txt',[r'Muse\\s*\\(2\\)', r'Muse\\s*\\(1\\)', r'Mathematic', r'Man,\\s*a  human', r'Manikin', r'Mannequin', r'Music'])\nprint('==== LAT')\nshow('LAT.txt',[r'Musa,', r'monstrum,', r'moneo, -es'])\nprint('==== LEW loose')\nshow('LEW_1910.txt',[r'mens,\\s*-tis', r'moneo,\\s*-ere', r'monstrum'],n=1)\nEOF",
 "description": "More greps Skeat/LAT/LEW"
}
```


### [2026-09-07T16:29:05.556Z] TOOL RESULT

```
SKT.txt | Muse\s*\(2\) >> NOT FOUND
SKT.txt | Muse\s*\(1\) >> NOT FOUND
SKT.txt | Mathematic >> NOT FOUND
SKT.txt | Man,\s*a  human >> NOT FOUND
SKT.txt | Manikin >> NOT FOUND
SKT.txt | Mannequin >> NOT FOUND
SKT.txt | Music >> NOT FOUND
==== LAT
LAT.txt | Musa, >> NOT FOUND
LAT.txt | monstrum, >> 'raitre monumentalis, monumentarius, A moneO se ratta-\nchent monstrum, Moneta , q.u.\nMoneo est conserve dans 1 ’esp.ra uflir "inviter", M.L.565O; un fre-\nquentatif atteste tardivernent monitare (Fortun.) s\'est maintenu en\nsicilien, M.L.5661,\nAutres derives et composes: monela (Tert.); monitio, -tor,-torius\n(Sen.), - tum,-tus,-us'
LAT.txt | monstrum, >> '. sg.), le sens de "pointe" d\'une hauteur. V. aussi\nmentum.\nmonstrum, -In.: — ut Aelius Stilo interpretatur, a monendo dictum\nest, uelut monestrum. Item Sinnius Capito, quod monstret futurum,\net moneat uoluntaten deorum, Fest. 133,8. Terme du vocabulaire religieux,\n"prodige qui avertit de la volonte des dieux"; par suite "objet'
LAT.txt | moneo, -es >> NOT FOUND
==== LEW loose
LEW_1910.txt | mens,\s*-tis >> NOT FOUND
LEW_1910.txt | moneo,\s*-ere >> NOT FOUND
LEW_1910.txt | monstrum >> NOT FOUND
```


## [2026-09-07T16:29:13.259Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'Muse',r'M[uo]sic',r'Mathemat',r'Manikin|Mannikin|Manakin',r'\\bMan\\b[^\\n]{0,60}human']:\n    ms=list(re.finditer(p,t))\n    print('###',p,len(ms))\n    for m in ms[:3]:\n        print(' ',repr(t[max(0,m.start()-70):m.end()+320]))\nEOF",
 "description": "Loose grep Skeat"
}
```


### [2026-09-07T16:29:14.579Z] TOOL RESULT

```
### Muse 2
  "id  ol'  a roiserV\nMortmain,  Mortuary ;  see  Mortal.\nMosaic ;  see  Muse  (}).\nMoslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  professes  ii/dm, i.  e.  submission  to  the  will  of  God  and  to the  orthodox  faith. —  Arab,  sa/ama,  to  s"
  'rives  all  j mntilus,  maimed-\nMutual ;  see  Mntable.\nMuzale;  see  Muse  (i).\nMy;  «c  Me\nMyriad.  (Gk.)    Gk.  mv/uc ^vpitit,  the  number  of  to,ooo.— < numberless.\nMyrmidon.    (L.  -  Gk.)    G«b. Afyrmulans.  —  L,    AfyrmiJoftes, KvpfttiCvfv,  pi.  a  wirlikc  people formerly  in  >Fginri  ^Monicr).\nMyrrh.  ;!• .  -  L.  -  Gk  -  Aral mirre.  ••  O.  F.    mirre    (lllh myrrhe.'
### M[uo]sic 0
### Mathemat 0
### Manikin|Mannikin|Manakin 0
### \bMan\b[^\n]{0,60}human 0
```


## [2026-09-07T16:29:22.672Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ('FSD_vol3.txt','WEB_vol1.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for p in [r'mu[·\\-]?sic,?\\s*n', r'Mu[·\\-]?sa', r'man[·\\-]?ne[·\\-]?quin', r'mo[·\\-]?sa[·\\-]?ic', r'math[·\\-]?e[·\\-]?mat']:\n        ms=list(re.finditer(p,t,re.I))\n        print('###',f,p,len(ms))\n        for m in ms[:1]:\n            print('  ',repr(t[max(0,m.start()-60):m.end()+330]))\nEOF",
 "description": "Grep Funk&Wagnalls and Webster"
}
```


### [2026-09-07T16:29:25.226Z] TOOL RESULT

```
### FSD_vol3.txt mu[·\-]?sic,?\s*n 2
   'spci tally\nndupted to the pianoforte, os iimst sonaian, (r) music not\nIntended specially for any particular mmlo of performum o.\nIncluding most daiico-inusic, (2) v<»ral, goner.iUv with lii-\nstrumeiuol aceompaiilmont including (a) eerlesInstlraU\nas tho mays requiem, and an/hi m. ih) clramAtlc. us t he opera,\noratorio. uml cantata. (c> lyrie.as the hymn. song, nn I glee\njn form, musle that nmslH'
### FSD_vol3.txt Mu[·\-]?sa 11
   ' names of consignees, 2. The fiber of a tall perenmal herb (Musa toxtilU) of\nn list of passengers and their baggage, and other items, the same genus as the banana. Mamla hemp. Whnn\nthe human body for exhibiting anatomical structure and\nthe position of the various organs and members, or for\npractical instruction in certain obstetrical operations,\ntho application of bandages, etc. 2. A model o'
### FSD_vol3.txt man[·\-]?ne[·\-]?quin 1
   "splaved and advertised. 4. A lillle\nman, pignw; dwarf [< F. mannequin, < MD. monne-\nken, dim* of man, man )\niw-na\n(Or J Or < . .\n‘ nn^nR'fRB* a. Samoss Manhwoaqan\nB.l Bhnp\nma-nip'u-la-ryt [< L manipularlt, < manipulus, sue\nMANiPLr 1— ma-iilp'u-1a*rMy» otfp\nmR-iilp'u-lBte» 1 ms-nip'yu-Ifit, 2 ma-nlp'yv-lAt, v.\n[-LAT'En: -lat'xno.] 1. t. 1. To operate on or work\nwith the hands; especially, to handl"
### FSD_vol3.txt mo[·\-]?sa[·\-]?ic 18
   ", 2 mu-g I'lc. it. (Hare 1 1. 'I'oorimment\nor doooratu with mosaics. 2. To form us If into a moaulc.\nmo-sa'lc*>, a Of, rierlaining to, or n’scMahliiig tho stylo\nof inlaid work culled iiiosuic; tesselluied; inlaid.\nAfoiate plotuniB nm a very iniportant bnuioh of ancient art.\nJulia II Dn Immirnt iShorl\niltat Art p KM Ir * ii ISHl 1\nI < LL mostticua, < fir. moM- 1\naeioa, < mousa, musoj iiiu«j\nsa'"
### FSD_vol3.txt math[·\-]?e[·\-]?mat 61
   "ckish\nbands, and\nBllvory beneath\nMackerel.\n1746). A BeottWh mathematician, who developed the In-\nfinitesimal calculus.— Maclanrin «mnslon, same as\nMACLAuatN's TBBOBBM.— Madanrln^s series (JtfaiA), a\n■ertes derived from Taylor's sartai by putting x » o.\nnacTo, 1 makT. 8 mien. n. 1. Mineral. (1) A twto crystal.\n(2) ChlastoUte. 8. SameaaMACKLB. 8. BameasMAscLa.\n(Fj, < L. macula, spot j\nMo>Lean', X "
### WEB_vol1.txt mu[·\-]?sic,?\s*n 1
   'bsidiary.\n3. additional; supplementary.\nauxiliary notes; in music, notes representin tones subsidiary to harmony but inserted for variety.\nauxiliary quantity; in mathematics, a quan- tity employed to elucidate an equation or trigonometrical problem.\nauxiliary scales; in music, the six keys or scales, consisting of any key major, with its relative minor, and the attendant keys of each.\nauxiliary '
### WEB_vol1.txt Mu[·\-]?sa 3
   'panan/a, n. [Sp.] a large tropical perennial plant or tree, Musa sapientum, akin to the plantain; also, its fruit, which is narrow and somewhat turved, and has a sweet, creamy flesh covered by a yellowish or reddish skin. The plant grows fifteen to twenty feet high and has a soft stalk and leaves that are six feet long and a foot broad. Bananas grow in large bunches, which weigh as much as 8'
### WEB_vol1.txt man[·\-]?ne[·\-]?quin 1
   'le and detachable parts, used in medical schools, etc. 3. a mannequin. P : Also spelled manakin, mannikin. : Ma-nil’a, ma-nil’a, n. 1. Manila hemp. 2. Manila paper. 3. Manila rope. 3 ESRA 4. a kind of cigar made in Manila, the ital of the Philippine Islands. ed Manilla.\nstalk of a Philippi\nnana; abac4: it is used for m\npaper, etc. à AA z\nanila paper; a strong, brownish wrap\npaper, originally made'
### WEB_vol1.txt mo[·\-]?sa[·\-]?ic 12
   '-cis/cus, n. in ancient architecture, a tile\nor square in a mosaic pavement. eee ab/a-cist, n. [L. abacus, a counting board.] one >\npee casts accounts with an abacus; a calcu- ator. ciate A-back’, adv. [AS. on bec, at, on, or toward the back.] toward the back; on the back part; backward. Now archaic except in nautical usage, where it signifies the situation of the sails when pressed back again'
### WEB_vol1.txt math[·\-]?e[·\-]?mat 256
   'PROPER NAMES, FOREIGN WORDS AND\nPHRASES, PRACTICAL BUSINESS MATHEMATICS, ABBREVIATIONS, TABLES OF WEIGHTS AND MEASURES, SIGNS AND SYMBOLS, AND FORMS OF ADDRESS\nILLUSTRATED THROUGHOUT\nTHE WORLD PUBLISHING COMPANY\x0c\nCLEVELAND AND NEW YORK\n1962\nPUBLISHED BY\nThe World Publishing Company\nCopyright under the Universal Copyright Convention; the International Copyright Union; Pan-American Conventions of '
```


## [2026-09-07T16:29:34.951Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'mousike|mousikE|musike', r'F\\. musique', r'< AS\\. mann|AS\\. man,|mann, man', r'maniac', r'am-nes|amnesty', r'au-to-mat|automatic']:\n    ms=list(re.finditer(p,t,re.I))\n    print('###',p,len(ms))\n    for m in ms[:2]: print('  ',repr(t[max(0,m.start()-200):m.end()+200]))\nEOF",
 "description": "FSD music/man/maniac etymologies"
}
```


### [2026-09-07T16:29:37.454Z] TOOL RESULT

```
### mousike|mousikE|musike 0
### F\. musique 0
### < AS\. mann|AS\. man,|mann, man 1
   'LinffuUtic Studies aaoon<i§erleB,p 274 [a 1874.]\nCapital M is from Lat. Or. M < Early Greek ^ <\nPhemcian T < Egyptian hieratio $ < nierogl^n\nThe hierogl^h represented an owl. The runK^H “ M\nIs called mann, man. It is the twentieth letter of the\nfuthorc. For the lower-case, black letter, and dates\nand the like, see A.\nThe history of the oharaeter Is represented as below:\nEgsrptlan Phenl-\n*Owl* HloraUc. clan'
### maniac 4
   "uoiVkal. 2 ma-nra-cal. a. plating ||i||Q^.fold, 1 mauVfdld, 2 m&n'i-f6ld, vL To make\nto, roaembling, or affected by manta, eharartenstic of a more than one copy of at once, as in a typewriter: aa, to\nmaniac. Syn.: see insanb.— ma-nra-eal*lyt eds manifold a letter, to multiply; as, he manifclatd his\nla'nM^. 1 me'ni-e-si, e mg'm-a^y, ^ successes the following yeai.\n[a'^nl-bM'tao, 1 mfl'ni-bffs'o. 2 mft'nl"
   "at'hookf,— niat^tock, w A ef\nMat'ioiCilroH^so, 1 nui'to-grfiH'u 2 niu'io-urPH'o. » A min-\ning state In Brazil, 532,683 sq m . capital, Cuyabg Ma'to\nGros'sof,\nmat 'told, 1 maroid; 2 mftt'OliI. n A monomaniac charao-\ntcrlzed by stupidity ( <* LL mattua, dull, + -oiii |\nTliorc IN H « Ihmr ttf , ongi'titittl iianuiitiaiMi ooiunoin in 1 inly, whom\nLniitlirtMu dtMiignatoa m maUouta\nLtierary Digeat Juno 11. 18"
### am-nes|amnesty 6
   "Not of sound mind or discretion, mental-\nly unbalanced often abbreviated non compos.\niion''*eom-pound'er,fi. Eng HUt One of the Jaoobltes who\nfavored the restoration of James II without condltloua of\namnesty or guaranties of liberty Hee goiipounobb, 8\nnon con., abbr Nuu-ountent, i e., dissentient, nou-oon-\nformlst\nBon^aeon-due'Car, n. A substanoo or medium that offers\nmuoh resistuiiee to the passage of a"
   "proofs has agreed to\naccept his opponent's oath on the afTalr In question — o. of\nalleglanre. a declaration under oath by which a person\npromises to boor allegiance to a government or sover^n\n— o. of amnesty, in United Btates history, the oath of\nloyalty to the CousUiutlon prescribed In President l.ln-\neoln's proclamation of amnesty and reconstruction lasu^\nDto. 8. 18A3* derisively called the damnaaty o."
### au-to-mat|automatic 35
   "gnmt* silicate (lli< 'nAU.MbOnt). ciysuillAiiig lu the moiiocllnlc sy t-\nmpr'e-O-graptat 1 mar'i-o-grof, 2 niir'e-o-£rkf, n. An tom 2. Petrol A curved Hue of globulites looking like a\ninstrument that automatically aud continuously records string of pearls 2. (/r C/i Hamc as makoakita 4t. A\nthe tidal changes in the level of the sea, a recording tide- pearl [F ,< 1. margartta, iiewl, ' Or waryarlP*. v. marga"
   "'ryeen, 1 mel'rln. 2 mdl'rOn. n. fir.) Bee Maihe*.\nMan'ser, 1 roau'ser, 2 mou'sAr. Feter Paul (Virl8a8*^/ii\n1017) A German meehanlolan and legislator. Inventor of\na magaxlne rifle — Mauser pistol, an automatic pistol\nIn which tho force of recoil ejeott the exploded shell and\nauppllee a cartridge from the magasine chamber.— M.\nride, see kivlk*, n\nnum^so-le'um, 1 me'so-lFum; 2 in6''so-l5'fim, n. [-uua or\n-A,"
```


## [2026-09-07T16:31:57.055Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nfor p in [r'Auramazd[āa]', r'mazd[āa]h', r'manu']:\n    ms=list(re.finditer(p,t))\n    print('###',p,len(ms))\n    for m in ms[:2]: print('  ',repr(t[max(0,m.start()-160):m.end()+240]))\nEOF",
 "description": "Grep Kent Old Persian for Auramazda"
}
```


### [2026-09-07T16:31:58.830Z] TOOL RESULT

```
### Auramazd[āa] 99
   '8 Ideograms and Ligature 37 XS ‘König M-G 02 8 DH Ча L 45 39 BU ‘Erde’ L 45 40 AM ‘Ahuramazda’ Op 74, E 90 4| BG бода ‘god’ Sc 1929 42  AMha Auramazdé Sc 1929, Auramazda- ha Br 1932 (cf. Hz 1931) Word-divider 43: Ty 1798\n$18. Tue Orp-PERstiAN SviLABARY. The in- scriptions composed in the Old Persian language are inscribed on various hard materials in a syllabary, each character having the value of a vowel '
   ' not accurately written. ;\nАе agrees with DSf; it has bümim and Вуй, otherwise XŠ and DH , but Auramazdà and baga.\nАзРа has zšāyaðiya, DH, būmām (sc) and BUyé, Auramazdā, baga; a state of variation which is attributable to the inaccuracy of OP writing at this period. $3. NumeRars: The cardinals are not written\nin full (except aiwa- ‘one’ in a formulaic phrase),\nbut are indicated by signs: 1, a single long '
### mazd[āa]h 49
   'en expressed that À was lost\nbetween two a-vowels which then contracted to\nd; but this is true only if the sequence is -ahah-;\nnote fraharavam, avahar[da], Auramazdaha -daha\n-daha, naham, атуйћа bagaha, dvahanam, Giira-\nvühara-, Gham and other forms of the tense,\nataham a6aha etc., maniyühaty, fraha"jam. The examples of ahah > äh are the following:\n*ahahy > аһу ‘thou mayst be’, cf. ahaliy ‘he may be’.\n*'
   'uence #0 there are some wrong writings in XPh: ahame = йМїт for ah*m* = Gham ‘I was’, атой = ahanty for *ah*an*iy = *ahüniy ‘may I be’, (gen.) амттг% а = Aura- mazdaha (4 occurrences; also twice in XPf) for -d"ah* = -dàha or -d\'ahea = -dähã; but these miswritings, some of them probably explainable (852, 558, $222.1), do not controvert the views expressed above.\n$132. CONSONANTAL VARIATION occurs in OP w'
### manu 4
   ' American Oriental Series, and to the Soci- ety’s Editor, Dr. Murray B. Emeneau, and its Secretary-Treasurer, Dr. Ferris B. Stephens, for their labors upon the manusenpt and the busi- ness management of the volume. To Mr. A. Eric Parkinson, of the University Museum in Philadelphia, I am indebted for the skillful drawing of the cuneiform characters which are\nreproduced on pages 12 and 215. My grateful '
   'sty. It is represented in some bilingual in- scriptions alongside the Sasanian Pahlavi, where it is often called Chaldaeo-Pahlavi or Parthian; by the parchment manuscripts of Auroman; and by certain Manichaean texts from Turfan (IV). It is also called Northwest Pahlavi, and appar- ently was developed from a dialect which was almost or quite identical with that of Media.\nII. The Sasanian or Southwest P'
```


## [2026-09-07T16:32:05.599Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Auramazd[āaà][^\\n]{0,60}(the great god|great god|god\\b)', t):\n    print(repr(t[max(0,m.start()-250):m.end()+200])); print('---')\n    break\ni=t.find('Auramazdā-')\nprint(repr(t[i-300:i+500]) if i>0 else 'no hyphen form')\nEOF",
 "description": "Kent lexicon Auramazda entry"
}
```


### [2026-09-07T16:32:06.954Z] TOOL RESULT

```
no hyphen form
```


## [2026-09-07T16:32:11.970Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:42:06.954Z] TOOL CALL #100: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk332.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MOUSA = \"https://en.wiktionary.org/wiki/%CE%9C%CE%BF%E1%BF%A6%CF%83%CE%B1\"\nW_MEN = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/men-\"\nW_MENS = \"https://en.wiktionary.org/wiki/mens\"\nW_MANNAZ = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/mannaz\"\nW_MANU = \"https://en.wiktionary.org/wiki/%D9%85%D9%86%D9%88%DA%86%D9%87%D8%B1\"\nW_MAZDA = \"https://en.wiktionary.org/wiki/%F0%90%AC%A8%F0%90%AC%80%F0%90%AC%B0%F0%90%AC%9B%F0%90%AC%81\"\nW_AHURA = \"https://en.wiktionary.org/wiki/Ahura_Mazda\"\nW_MUZE = \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87\"\nE_MUSIC = \"https://www.etymonline.com/word/music\"\nE_MOSAIC = \"https://www.etymonline.com/word/mosaic\"\nE_AMNESTY = \"https://www.etymonline.com/word/amnesty\"\nE_MANIAC = \"https://www.etymonline.com/word/maniac\"\nE_MONSTER = \"https://www.etymonline.com/word/monster\"\nE_MANNEQ = \"https://www.etymonline.com/word/mannequin\"\nE_MATH = \"https://www.etymonline.com/word/mathematics\"\nA_MAZQAN = \"https://abadis.ir/fatofa/%D9%85%D8%B2%D9%82%D8%A7%D9%86/\"\nA_MAZGHAN = \"https://abadis.ir/fatofa/%D9%85%D8%B2%D8%BA%D8%A7%D9%86/\"\nA_MUZE = \"https://abadis.ir/fatofa/%D9%85%D9%88%D8%B2%D9%87/\"\n\nPOK726 = (\"POK_02.txt leaf whose running head reads 727, entry head: \\\"3. men- ,denken, geistig erregt sein'; \"\n          \"erweitert meng- : mna- und mne-, menei- : meni-; Nominalbildungen: men-men- n., menos- n., men-ti-, \"\n          \"men-tu-, moni-, mn-ti-, mn-to- ,Sinn, Gedanke', men-ter- ,Denker'\\\" — the article opens on p.726 and runs to 728.\")\n\ndata = {\n \"pdf_page\": 332,\n \"book_page\": 302,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Men 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *men- 'to think, have in mind' (Pokorny 3. men- 726; Watkins/AHD men-1)\",\n \"note\": (\"The root, the language label and the gloss are all right: Pokorny p.726 heads the article \"\n          \"\\\"3. men- 'denken, geistig erregt sein'\\\" and Watkins glosses men-1 \\\"To think; with derivatives \"\n          \"referring to various qualities and states of mind and thought\\\", citing [Pok. 3. men- 726]. This is \"\n          \"PART 2 of the chart; the page's own cross-cutting problem is that Nourai hangs several nodes on the \"\n          \"wrong intermediate: Greek mousa is not derived from the bare root in any of his own sources \"\n          \"(Pokorny puts it under 5. me-/mo- p.705 or under mendh- p.730, Klein under *men-dh-), and in node #8 \"\n          \"monitor/monster/monument/demonstrate come from the causative monere (o-grade *mon-eye-), a sibling of \"\n          \"mens, not from mens itself. Nourai's superscript-breve notation (mens, Dhe 2) stands for the long \"\n          \"vowel of classical mens and of *dheh1-, so it is house style, not a misprint.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *men- «اندیشیدن، در ذهن داشتن» درست است؛ پوکورنی در صفحهٔ ۷۲۶ همین ریشه را با \"\n             \"عنوان «men- ۳: اندیشیدن، برانگیخته‌شدن ذهن» آورده و واتکینز (AHD) نیز men-1 را «to think» معنی کرده و به \"\n             \"همان صفحهٔ ۷۲۶ پوکورنی ارجاع داده است. برچسب زبانی «هندواروپایی» و معنای «to think» هر دو پذیرفتنی است. \"\n             \"اشکال کلی این نمودار در جای‌گذاری چند گره است: mousa یونانی در هیچ‌یک از منابع خودِ نورایی مستقیماً از این \"\n             \"ریشه گرفته نشده (پوکورنی آن را ذیل mē-/mō- ص ۷۰۵ یا mendh- ص ۷۳۰ می‌آورد و کلاین ذیل *men-dh-)، و در گرهٔ ۸ \"\n             \"واژه‌های monitor/monster/monument/demonstrate از فعل سببیِ monere (درجهٔ o یعنی *mon-eye-) می‌آیند، نه از mēns. \"\n             \"نشانهٔ «ě» در نگارش نورایی (مانند měns و Dhě) همان واکهٔ کشیدهٔ ē است و شیوهٔ خودِ کتاب است، نه غلط چاپی.\"),\n \"sources\": [W_MEN, E_MUSIC],\n \"ref_check\": [\n   {\"ref\": \"POK:726\", \"status\": \"supports\", \"note\": POK726}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I pp. 726-728 (POK_02.txt, grep '3.  men-')\", \"stance\": \"supports\",\n    \"note\": \"\\\"3. men- ,denken, geistig erregt sein'\\\"; the article lists ai. manyate, av. mainyeite, gr. mainomai, lat. memini / mens, got. munan, etc.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 264 ff. (incoming/WLD/WLD_Bd2_pages.txt line 17322)\", \"stance\": \"supports\",\n    \"note\": \"\\\"3. men- ,denken, geistig erregt sein'; Basen men-, mend-, mene(i)-\\\" — the same article Pokorny 1959 reprints.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. men-1 (AHD_watkins1985.txt line 745)\", \"stance\": \"supports\",\n    \"note\": \"\\\"men-1. To think; with derivatives referring to various qualities and states of mind and thought ... [Pok. 3. men- 726, mendh- 730.]\\\"\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 17.11 MIND, pp. 1198-1199 (SYN.txt line 30152 ff.)\", \"stance\": \"supports\",\n    \"note\": \"\\\"1. Derivs. of IE *men- in Skt. man- 'think', Lat. memini 'remember', etc. Walde-P. 2.264 ff. ... Lat. mens, mentis ...; Skt. manas-, Av. manah-.\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. manus (IEC.txt line 10322)\", \"stance\": \"partial\",\n    \"note\": \"Mann keeps a type *monus 'thoughtful' distinct from *manus 'man', i.e. he recognises the *men- 'think' family but not the equation with 'man' that Nourai's second root box makes.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Greek\", \"words\": \"mousa; matos; autos-matos\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Three separate items. (a) Gk. Mousa 'Muse, patroness of the arts' (Ion. Mousa, Dor. Mosa, Aeol. \"\n   \"Moisa): Watkins does put it here (men-1 III.2 'Suffixed o-grade form *mon-twa in Greek mousa, a muse: MOSAIC, \"\n   \"MUSE, MUSEUM, MUSIC'), but that is the minority view. Pokorny does NOT list it on p.726: he mentions it twice \"\n   \"elsewhere - p.705 under '5. me-, mo- heftigen und kraeftigen Willens sein' (\\\"Mousa ,Muse' hierher oder zu \"\n   \"mendh-?\\\") and p.730 under mendh- (\\\"vielleicht Mousa (*mon-dh-ia) ,Muse'\\\"). Klein p.947, the very page Nourai \"\n   \"cites, derives it from *men-dh- ('possibly also ... Gk. Mousa (if fr. *Monthia)'), i.e. from the enlarged root of \"\n   \"entry 2, not from bare *men-. Beekes finds *Monthia (*men- + *dheh1-) the most appealing IE option, rejects \"\n   \"*Montia 'mountain (nymph)', and allows a Pre-Greek *montia. So the arrow is defensible only through the \"\n   \"*men-dh- enlargement. (b) 'matos: mind, will' is not a free Greek word: it is the bound second member -matos of \"\n   \"automatos, from the verbal adjective *mn-to- 'thought' (= Skt. mata-, Lat. commentus); Watkins prints it as \"\n   \"'Greek -matos, \\\"willing\\\"'. (c) autos-matos = Gk. automatos 'acting of itself, self-willed' (autos 'self' + \"\n   \"-matos), confirmed by Pokorny p.727 (\\\"auto-matos ,aus sich selber heraus denkend und handelnd'\\\"); it is the \"\n   \"source of English automatic and Persian اتوماتیک.\"),\n \"derivation_fa\": (\"سه چیزِ جداگانه در یک گره. الف) Mousa یونانی «موز، ربّةالنوع هنرها»: واتکینز آن را از درجهٔ o \"\n   \"یعنی *mon-twa و زیر همین ریشه می‌آورد، ولی این دیدگاه اقلیت است. پوکورنی در صفحهٔ ۷۲۶ نامی از آن نمی‌برد و آن را دو \"\n   \"جا دیگر می‌آورد: ص ۷۰۵ ذیل mē-/mō- «سخت خواستن» («Mousa اینجا یا به mendh-؟») و ص ۷۳۰ ذیل mendh- («شاید Mousa از \"\n   \"*mon-dh-ia»). کلاین در همان صفحهٔ ۹۴۷ که نورایی ارجاع داده، آن را از *men-dh- می‌گیرد، یعنی از ریشهٔ گسترش‌یافته‌ای که \"\n   \"مدخل سوم همین صفحه است، نه از *men- ساده. بیکس هم *Monthia (از *men- + *dʰeh₁-) را پذیرفتنی‌ترین گزینهٔ هندواروپایی \"\n   \"می‌داند و احتمال وام‌واژهٔ پیش‌یونانی را نیز باز می‌گذارد. پس این پیکان تنها از راه گسترشِ *men-dh- توجیه‌پذیر است. \"\n   \"ب) «matos: mind, will» واژهٔ آزاد یونانی نیست؛ جزء دومِ بستهٔ automatos است از صفتِ فعلیِ *mn̥-to- «اندیشیده» (هم‌ریشه \"\n   \"با matá- سنسکریت و commentus لاتین)؛ واتکینز آن را به‌صورت «-matos, willing» می‌نویسد. پ) autos-matos همان \"\n   \"automatos «خودکار، از خود برانگیخته» است که پوکورنی در ص ۷۲۷ آن را «از خود اندیشنده و کننده» معنی کرده و سرچشمهٔ \"\n   \"automatic انگلیسی و «اتوماتیک» فارسی است. حکم: با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_MOUSA, E_MUSIC],\n \"ref_check\": [\n   {\"ref\": \"KLN:947\", \"status\": \"partial\",\n    \"note\": \"KLN_1966.txt leaf NR=509 (= printed pp.947-948, fitted from the numerals on leaves 508=946 and 510=948), s.v. 'mathematical': \\\"fr. *mndh-, reduced form of I.-E. base *men-dh-, 'to have one's mind aroused, apply oneself to' ... and possibly also OI. medha 'wisdom, intelligence', Gk. Mousa (if fr. *Monthia), 'Muse'. Base *men-dh- is an enlargement of base *men-, 'to think'.\\\" Klein therefore supports the ultimate link to *men- but routes Mousa through *men-dh-, and says nothing about matos / autos-matos.\"},\n   {\"ref\": \"AHD:864\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD page numbers are pages of the 1975/76 New College Edition body text, which is not on disk (only Watkins 1985, the standalone IE-roots appendix). The corresponding root article, Watkins men-1, does list Greek mousa (*mon-twa) and Greek -matos (*mn-to-).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 705 and p. 730 (POK_02.txt lines 5825, 17841-equivalent)\", \"stance\": \"partial\",\n    \"note\": \"p.705: \\\"Mousa ,Muse' hierher oder zu mendh-?\\\" (under 5. me-, mo-); p.730 under mendh-: \\\"vielleicht Mousa (*mon-dh-ia) ,Muse'\\\". Nowhere under men- p.726.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 271 (WLD_Bd2_pages.txt line 17841)\", \"stance\": \"partial\",\n    \"note\": \"\\\"vielleicht Mousa (*mondhia; von Fick KZ. 46, 82 ... ) ... Wackernagel KZ. 33, 571 erklaerte es als *montia 'Bergnymphe'\\\" - three rival derivations, none of them the bare root men-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins men-1 III.2 and I.2 (AHD_watkins1985.txt line 745)\", \"stance\": \"supports\",\n    \"note\": \"\\\"2. Suffixed o-grade form *mon-twa in Greek mousa, a muse: MOSAIC, MUSE, MUSEUM, MUSIC\\\"; \\\"2. Suffixed form *mn-to- in Greek -matos, 'willing': AUTOMATIC\\\".\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~1017, s.v. 'Muse' (KLN_1966.txt leaf NR=546)\", \"stance\": \"partial\",\n    \"note\": \"\\\"Muse ... fr. L. Musa, fr. Gk. Mousa, 'Muse; music, song', which stands perh. for *Monthia and is rel. to manthanein, 'to learn'. See mathematical and cp. amusia, mosaic, museum, music.\\\"\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"An empty pass-through box standing for the Latin borrowings of the Greek Muse-words: Musa (Ennius, \"\n   \"Plautus, 3rd-2nd c. BCE), musica (< Gk. mousike techne 'art of the Muses'), museum/musaeum (< Gk. mouseion \"\n   \"'seat of the Muses', the Alexandrian Mouseion), musivum/musaicum opus 'mosaic work'; Late Latin also amnestia \"\n   \"(< Gk. amnestia) and maniacus (< Gk. maniakos). Greek ou was regularly rendered by Latin u, and the Greek \"\n   \"feminine adjective in -ike by -ica. All of these are simple literary borrowings, not inherited Latin words.\"),\n \"derivation_fa\": (\"این جعبهٔ خالی نمایندهٔ وام‌واژه‌های لاتین از خانوادهٔ «موز» یونانی است: Musa (از سدهٔ سوم-دوم پیش از \"\n   \"میلاد در انیوس و پلاوتوس)، musica از mousikē technē «هنر موزها»، museum/musaeum از mouseion «جایگاه موزها» \"\n   \"(موزهٔ اسکندریه)، و musivum/musaicum opus «کار موزاییک»؛ در لاتینِ پسین نیز amnestia و maniacus از یونانی. \"\n   \"دوواکهٔ ou یونانی در لاتین به u و پسوند مؤنثِ -ikē به -ica بدل شده است. همهٔ اینها وام‌گیریِ ادبی‌اند نه واژهٔ \"\n   \"موروثی لاتین. ادعای نورایی درست است.\"),\n \"sources\": [E_MUSIC, E_MOSAIC],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this pass-through box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~1017 s.v. Muse, museum (KLN_1966.txt leaf NR=546)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Muse ... fr. L. Musa, fr. Gk. Mousa\\\"; \\\"museum, n. - L. museum, 'library, academy, study, museum', fr. Gk. mouseion, lit. 'seat of the Muses', fr. Mousa, 'Muse'.\\\"\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. III s.v. mosaic (FSD_vol3.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"[< LL. mosaicus, < Gr. mos-aeios(?), < mousa, muse]\\\" - the Latin stage is explicit.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt), grep 'Musa,'\", \"stance\": \"silent\",\n    \"note\": \"No entry for Musa/musica: Ernout-Meillet treat only inherited Latin vocabulary, so the Greek loans are absent.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"French\", \"words\": \"musique\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Latin musica > Old French musique (attested c.1150-1200, first as musike/musique), a learned \"\n   \"borrowing rather than a popular development (a popular outcome would have lost the medial -s- and shifted the \"\n   \"stress). Old French musique gave Middle English musik (mid-13c.) and, in the 19th century, the Persian and \"\n   \"Turkish forms. Mo'in states the chain himself in his footnote to Borhan-e Qate' p.2052: Gk. mousike > Lat. \"\n   \"musica (cf. Fr. musique, Eng. music, Ger. Musik), all from Mousa.\"),\n \"derivation_fa\": (\"musica لاتین در فرانسهٔ کهن به musique بدل شده (نخستین گواه‌ها حدود ۱۱۵۰-۱۲۰۰ م، به‌صورت \"\n   \"musike/musique) و این وام‌گیری از راه زبان عالمانه است نه تحولِ عامیانه (در تحول عامیانه -s- میانی می‌افتاد و \"\n   \"جای تکیه جابه‌جا می‌شد). از همین صورتِ فرانسهٔ کهن، musik انگلیسی میانه (میانهٔ سدهٔ سیزدهم) و در سدهٔ نوزدهم \"\n   \"صورت‌های فارسی و ترکی گرفته شده است. خودِ معین در حاشیهٔ برهان قاطع ص ۲۰۵۲ همین زنجیره را آورده: از یونانی \"\n   \"mousikē به لاتینی musica (قس فرانسه musique، انگلیسی music، آلمانی Musik) و همه مأخوذ از Mousa. ادعای نورایی درست است.\"),\n \"sources\": [E_MUSIC],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given for the French box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote 9 on Borhan-e Qate' p.2052 (= BQT_v4_pages.txt [pdf page 135], printed = pdf+1917)\", \"stance\": \"supports\",\n    \"note\": \"«موسیقی - بضم اول، از یونانی mousikē (موسیقی). لاتینی musica (قس: ف. musique، انگ. music، آلم. Musik) مأخوذ از Mousa (بمعنی Muse (فر) هریک از نه ربةالنوع اساطیری یونان که حامیان هنرهای زیبا بودند)».\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~1017 s.v. Muse / music (KLN_1966.txt leaf NR=546)\", \"stance\": \"supports\",\n    \"note\": \"Klein's Muse article cross-refers to 'music' and gives the Latin > Old French route for the whole group.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"موزیک ، مزقان ، مزغان\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All three are one and the same French loan. (a) موزیک mūzīk < Fr. musique, taken in during the \"\n   \"Qajar period with the European military band and the Dar al-Fonun (1851): Mo'in tags it «موزیک: [فر.] (اِ.) \"\n   \"موسیقی». French [myzik] was heard as Persian mūzīk, the front rounded ü being replaced by the nearest Persian \"\n   \"ū. (b) مزغان mazghān and (c) its variant مزقان mazqān 'military band; band music; the players' are the popular \"\n   \"reshaping of the same word: Dehkhoda says so in as many words - «این لفظ محرف موزیک فرانسوی است که با الف و \"\n   \"نون فارسی جمع بسته شده» ('this word is a distortion of French mūzīk pluralised with the Persian -ān'). \"\n   \"Phonetically mūzīk > *mūzīk-ān > mazghān/mazqān, with the unstressed first syllable reduced and the -k- voiced \"\n   \"to gh (and then, in the spelling مزقان, backed to q). Dehkhoda cross-refers مزقان to مزغان, i.e. treats them as \"\n   \"one word. Note that the immediate donor is French musique, exactly as the chart draws it - not Persian موسیقی, \"\n   \"which is the older Arabic-mediated borrowing of Greek mousike.\"),\n \"derivation_fa\": (\"هر سه صورت، یک وام‌واژهٔ فرانسوی‌اند. الف) «موزیک» از musique فرانسوی، که در دورهٔ قاجار همراه با \"\n   \"دستهٔ موزیکِ نظامی و دارالفنون (۱۲۳۰ ش/۱۸۵۱ م) به فارسی آمد؛ معین آن را «[فر.] (اِ.) موسیقی» ثبت کرده است. واکهٔ \"\n   \"گردِ پیشینِ فرانسوی (ü) در فارسی به نزدیک‌ترین واکه یعنی «او» بدل شده. ب و پ) «مزغان» و گونهٔ آن «مزقان» به معنای \"\n   \"«دستهٔ سازهای نظامی، نوازندگان، موسیقی» دگرگون‌شدهٔ همان واژه‌اند؛ دهخدا صریحاً می‌نویسد: «این لفظ محرف موزیک \"\n   \"فرانسوی است که با الف و نون فارسی جمع بسته شده». از نظر آوایی: mūzīk ← *mūzīkān ← mazghān/mazqān، با کاهش هجای \"\n   \"بی‌تکیهٔ آغازی و واک‌دار شدنِ k به «غ» و سپس ابدال آن به «ق» در املای «مزقان». دهخدا «مزقان» را به «مزغان» ارجاع \"\n   \"می‌دهد، یعنی آن دو را یک واژه می‌شمارد. نکته آنکه وام‌دهِ بی‌واسطه همان musique فرانسوی است - چنان‌که نمودار \"\n   \"رسم کرده - نه «موسیقی» فارسی که وام‌گیریِ کهن‌ترِ mousikē یونانی از راه عربی است. ادعای نورایی درست است.\"),\n \"sources\": [A_MAZGHAN, A_MAZQAN],\n \"ref_check\": [\n   {\"ref\": \"MON:4063\", \"status\": \"not_checked\",\n    \"note\": \"The 6-volume Amir Kabir Farhang-e Farsi is not available in any digitised form (see refs_online.json: only the 2-volume Adena condensation exists). In that condensation the entry reads «موزیک: [فر.] (اِ.) موسیقی» and «موزیکال: [فر.] (ص.) مربوط به موسیقی» (MON_part2.txt), which is what p.4063 would carry.\"},\n   {\"ref\": \"MON:4433\", \"status\": \"not_checked\",\n    \"note\": \"Same reason. The condensation has the مزغان entry as «[فر - فا.] (اِ.) ۱- ساز. ۲- آلت موسیقی» (i.e. Mo'in himself tags it French + Persian, exactly Dehkhoda's analysis).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. موزیک and s.v. مزغان (2-vol Adena condensation)\", \"stance\": \"supports\",\n    \"note\": \"«موزیک: [فر.] (اِ.) موسیقی»; the مزغان gloss carries the tag [فر - فا.] 'French + Persian', i.e. a French stem with a Persian suffix.\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote 9 to Borhan-e Qate' p.2052 (BQT_v4_pages.txt [pdf page 135])\", \"stance\": \"supports\",\n    \"note\": \"Gives the Greek > Latin > French chain and names French musique as the modern European form.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye Hend-o-Orupayi (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur only treats inherited Persian vocabulary; no entry for موزیک/مزغان.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie (HRN.txt), grep 'musik', 'mazgan'\", \"stance\": \"silent\",\n    \"note\": \"Horn (1893) and Huebschmann (1895) do not register these 19th-century Europeanisms; only the German word 'Musik' occurs, in Horn's own prose.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"موزه ۱ ، موزائیک ، اتوماتیک\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Three French loans of the late Qajar / early Pahlavi period, but none of them comes from French \"\n   \"musique: the arrow from node #3 is a chart shorthand for 'French'. (a) موزه mūze 'museum' < Fr. musée < Lat. \"\n   \"museum < Gk. mouseion 'seat of the Muses'; French -ée was rendered by Persian -ه. The superscript ۱ is \"\n   \"off: in Mo'in's Farhang the numbered homographs are موزه (۱) = 'boot' (tagged [په.], i.e. Pahlavi, from MP \"\n   \"mozag 'shoe', Proto-Iranian *hmaw-, which has nothing to do with *men-) and موزه (۲) = the museum word, tagged \"\n   \"[فر.]; the word the chart wants is موزه ۲. (b) موزائیک mūzā'īk < Fr. mosaïque < It. mosaico < Med.Lat. \"\n   \"musaicum (opus) 'work of the Muses'. (c) اتوماتیک otomātīk < Fr. automatique < Gk. automatos + -ikos; Mo'in \"\n   \"glosses it «دستگاهی که خود به خود کار می‌کند ... خودکار» with a French tag. So the words and the \"\n   \"ultimate root are right; the intermediate (musique) and the homograph number are not.\"),\n \"derivation_fa\": (\"هر سه وام‌واژهٔ فرانسوی پایان دورهٔ قاجار و آغاز پهلوی‌اند، ولی هیچ‌یک از musique نیامده‌اند؛ پیکانی \"\n   \"که از گرهٔ ۳ کشیده شده در واقع کوتاه‌نوشتِ «از فرانسه» است. الف) «موزه» به معنای عتیقه‌خانه از musée فرانسوی، خود از \"\n   \"museum لاتین و mouseion یونانی «جایگاه موزها»؛ پایانهٔ -ée فرانسوی در فارسی به «ه» بدل شده. شمارهٔ «۱» جابه‌جا \"\n   \"افتاده است: در فرهنگ معین «موزه (۱)» همان چکمه است با برچسب [په.] از mōzag فارسی میانه (ایرانی آغازین *hmaw-) که \"\n   \"هیچ پیوندی با *men- ندارد، و «موزه (۲)» واژهٔ فرانسویِ عتیقه‌خانه است؛ آنچه نمودار می‌خواهد «موزهٔ ۲» است. ب) \"\n   \"«موزائیک» از mosaïque فرانسوی، از mosaico ایتالیایی، از musaicum لاتینِ میانه «کارِ موزها». پ) «اتوماتیک» از \"\n   \"automatique فرانسوی، از automatos یونانی با پسوند -ikos؛ معین آن را «دستگاهی که خود به خود کار می‌کند... خودکار» \"\n   \"معنی کرده و فرانسوی دانسته است. پس واژه‌ها و ریشهٔ نهایی درست است، ولی واسطه (musique) و شمارهٔ همنگاره نادرست است؛ \"\n   \"با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_MUZE, A_MUZE, E_MOSAIC],\n \"ref_check\": [\n   {\"ref\": \"BQT:2052\", \"status\": \"supports\",\n    \"note\": \"BQT_v4_pages.txt [pdf page 135] = printed p.2052 (printed = pdf + 1917). The page carries Mo'in's footnote 9: «موسیقی ... از یونانی mousikē ... لاتینی musica ... مأخوذ از Mousa (بمعنی Muse ... هریک از نه ربةالنوع اساطیری یونان که حامیان هنرهای زیبا بودند)» - i.e. the page really is the etymological anchor for the whole Muse group. It does NOT contain موزه 'museum' (the Borhan's موزه there is the boot, and 'grief' and 'pool'), so the page supports the root claim, not the homograph number.\"},\n   {\"ref\": \"MON:4432\", \"status\": \"not_checked\",\n    \"note\": \"6-vol Mo'in not digitised; the 2-vol condensation has «اتوماتیک: (ص.) دستگاهی که خود به خود کار می‌کند و نیازی به بودن کارگر بر سر آن نیست؛ خودکار [فر.]» (MON_part1.txt) and, per abadis' rendering of Mo'in, موزه (۱) = چکمه [په.] vs موزه (۲) = museum [فر.].\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. اتوماتیک; abadis rendering of Mo'in s.v. موزه\", \"stance\": \"partial\",\n    \"note\": \"Confirms the French origin of اتوماتیک and of the museum sense of موزه, but numbers the museum word موزه (۲), the boot موزه (۱).\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. mozag (PHD.txt)\", \"stance\": \"contradicts\",\n    \"note\": \"The homograph موزه ۱ is MP mozag 'shoe, boot', an inherited Iranian word - not a member of the *men- family; hence the number in the chart cannot be right.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. III s.v. mosaic (FSD_vol3.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"[< LL. mosaicus, < Gr. ..., < mousa, muse]\\\" - the source of Fr. mosaïque > Pers. موزائیک.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"music, museum, mosaic, amnesty, maniac, automatic\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Every one of the six is a descendant of PIE *men-, and Watkins lists all six under men-1, so the \"\n   \"root is right; but only the first three descend through Mousa/Musa, so the Latin box #2 is not the parent of \"\n   \"the last three. (a) music: Gk. mousike (techne) > Lat. musica > OFr. musique > ME musik, mid-13c. (b) museum: \"\n   \"Lat. museum < Gk. mouseion, in English 1610s of a building for scholarly collections. (c) mosaic: Med.Lat. \"\n   \"musaicum 'work of the Muses' > It. mosaico > OFr. mosaicq > E. 1580s (Etymonline notes medieval mosaics were \"\n   \"dedicated to the Muses, and that Gk. mouseion in this sense is itself a loan back from Latin). (d) amnesty: Gk. \"\n   \"amnestia 'forgetfulness (of wrong)' (a- privative + mnestis 'remembrance') > Lat. amnestia > Fr. amnistie > E. \"\n   \"1570s - from the extended base *mna-/*mne- (Watkins men-1 IV), not from mousa. (e) maniac: Gk. mania 'madness' \"\n   \"(: mainesthai < *mn-yo-) > Late Lat. maniacus > Fr. maniaque > E. c.1600 (Watkins men-1 II.3.c). (f) automatic: \"\n   \"Gk. automatos > automatikos, E. 1740s, from *mn-to- (Watkins men-1 I.2).\"),\n \"derivation_fa\": (\"هر شش واژه بازماندهٔ *men- هندواروپایی‌اند و واتکینز همه را ذیل men-1 آورده است، پس ریشه درست است؛ \"\n   \"اما تنها سه واژهٔ نخست از راه Mousa/Musa آمده‌اند و بنابراین جعبهٔ لاتینِ شمارهٔ ۲ پدرِ سه واژهٔ آخر نیست. الف) \"\n   \"music: از mousikē technē یونانی به musica لاتین، musique فرانسهٔ کهن و musik انگلیسی میانه (میانهٔ سدهٔ سیزدهم). \"\n   \"ب) museum: از museum لاتین و mouseion یونانی، در انگلیسی از دههٔ ۱۶۱۰. پ) mosaic: از musaicum لاتینِ میانه «کار \"\n   \"موزها»، mosaico ایتالیایی، mosaicq فرانسهٔ کهن، انگلیسی دههٔ ۱۵۸۰. ت) amnesty: از amnestia یونانی «فراموشی (گناه)» \"\n   \"(پیشوند نفیِ a- + mnestis «یادآوری») به amnestia لاتین، amnistie فرانسوی و انگلیسیِ دههٔ ۱۵۷۰ - از ستاکِ \"\n   \"گسترش‌یافتهٔ *mnā-/*mnē-، نه از mousa. ث) maniac: از mania یونانی «دیوانگی» (هم‌ریشه با mainesthai از *mn̥-yo-) به \"\n   \"maniacus لاتینِ پسین، maniaque فرانسوی و انگلیسیِ حدود ۱۶۰۰. ج) automatic: از automatos و automatikos یونانی، در \"\n   \"انگلیسی دههٔ ۱۷۴۰، از *mn̥-to-. حکم: با احتیاط پذیرفتنی است، زیرا سه واژهٔ آخر خواهرِ گروهِ «موز»اند نه فرزندِ آن.\"),\n \"sources\": [E_MUSIC, E_MOSAIC, E_AMNESTY, E_MANIAC],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 men-1 lists all six: 'MOSAIC, MUSE, MUSEUM, MUSIC' (III.2, *mon-twa), 'AMNESIA, AMNESTY, ANAMNESIS' (IV.1, mna-), 'MANIA, MANIAC' (II.3.c), 'AUTOMATIC' (I.2, *mn-to-). The index confirms MUSIC men-1, MOSAIC men-1, AMNESTY men-1, MANIAC men-1, AUTOMATIC men-1.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~1017 (Muse, museum), p. ~978 (maniac) (KLN_1966.txt leaves 546, 501)\", \"stance\": \"supports\",\n    \"note\": \"\\\"museum, n. - L. museum ... fr. Gk. mouseion, lit. 'seat of the Muses'\\\"; \\\"maniac, adj. ... ML. maniacus (whence also F. maniaque), fr. L. mania, fr. Gk. mania\\\" - i.e. maniac comes through mania, not through Musa.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mosaic (SKT.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Mosaic; see Muse (2).\\\" - Skeat too groups mosaic with the Muse, and separately treats mental/monition.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. III s.v. mosaic (FSD_vol3.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"[< LL. mosaicus, < Gr. ..., < mousa, muse]\\\".\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Latin\", \"words\": \"ment, měns\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Lat. mens, gen. mentis, f. 'mind, intellect, disposition' goes back to the *-ti- abstract \"\n   \"*mn-ti- / *men-ti- 'thought' from *men-, the same formation as Skt. mati-, Av. -maiti-, Goth. ga-munds, OE \"\n   \"gemynd (> English mind), Lith. mintis, OCS pa-metь. Pokorny p.727: \\\"lat. mens, -tis 'Sinnesart, Gemuet, \"\n   \"Denkvermoegen, Vernunft' (aus *mnti-)\\\"; Ernout-Meillet add that mens, like mors, was extracted from the \"\n   \"compounds (cf. Goth. ga-munds). The oblique stem ment- (whence Nourai's first form 'ment') is what all the \"\n   \"derivatives are built on. Nourai prints měns with a breve; classical Latin has a long vowel, mens (< *ments \"\n   \"< *mentis), but the breve is Nourai's own notation for that vowel (he writes Dhě 2 for *dheh1- likewise), so \"\n   \"this is house style rather than an error, and the extraction is faithful to the printed page.\"),\n \"derivation_fa\": (\"mēns لاتین با حالت اضافیِ mentis «ذهن، خرد، منش» از نامِ مجردِ پسوندی *mn̥-ti-/*men-ti- «اندیشه» از \"\n   \"ریشهٔ *men- می‌آید؛ همان ساختی که در mati- سنسکریت، -maiti- اوستایی، ga-munds گوتی، gemynd انگلیسی کهن (که mind \"\n   \"امروزی از آن است)، mintis لیتوانیایی و pa-mętь اسلاوی کهن دیده می‌شود. پوکورنی در ص ۷۲۷ می‌نویسد: «lat. mens, -tis \"\n   \"«منش، ذهن، خرد» از *mn̥ti-»؛ ارنو-میه نیز می‌افزایند که mens مانند mors از ترکیب‌ها جدا شده است. ستاکِ مایلِ ment- \"\n   \"(همان صورت نخستِ نورایی) پایهٔ همهٔ مشتق‌هاست. نورایی «měns» با نشانهٔ کوتاه می‌نویسد، در حالی که واکهٔ لاتینِ کلاسیک \"\n   \"کشیده است؛ ولی «ě» در این کتاب همان واکهٔ کشیده را می‌رساند (چنان‌که «Dhě ۲» را برای *dʰeh₁- به کار می‌برد)، پس \"\n   \"شیوهٔ نگارشِ خودِ نویسنده است نه خطای چاپی و خوانشِ اسکن هم درست است. ادعای نورایی درست است.\"),\n \"sources\": [W_MENS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins men-1 I.1.b: \\\"Suffixed form *mn-ti- in ... b. Latin mens (stem ment-), mind: MENTAL; AMENT, DEMENT; c. Latin mentio, remembrance, mention: MENTION.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 727 (POK_02.txt, men- 3 article)\", \"stance\": \"supports\",\n    \"note\": \"\\\"lat. meminī ,erinnere mich' ... mens, -tis ,Sinnesart, Gemuet, Denkvermoegen, Vernunft' (aus *mnti-, s. oben ai. mati- usw.), mentiō ,Erwaehnung'\\\".\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. mens (LAT.txt line 37334)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Il y a deux formes de theme en -ti-, l'une relativement ancienne, mens, cf. skr. matih 'pensee', l'autre, de type italo-celtique, mentio ... La forme mens a ete detachee, comme la forme mors, des formes composees; cf. got. ga-munds, lit. at-mintis, v.sl. pa-metь.\\\"\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 17.11 MIND (SYN.txt line 30152 ff.)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Lat. mens, mentis (> It., Sp. mente, Rum. minte) ... Skt. manas-, Av. manah-\\\" under 'Derivs. of IE *men-'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"English\",\n \"words\": \"mental, mention, monitor, monster; monument, comment, demonstrate\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All seven belong to *men-, but only two of them actually descend from mens (node #7); the rest \"\n   \"come from two sibling Latin stems, so the single arrow is too coarse. From mens/ment-: mental (< Late Lat. \"\n   \"mentalis, ME/OFr.) and mention (< Lat. mentio, -onis 'a calling to mind' > OFr. mention > ME mencioun). From \"\n   \"the verb comminisci 'to devise by thought' (*com-men-iscor): comment (< Lat. commentum 'invention, fiction', \"\n   \"neut. pp. of commentus) - Klein spells out \\\"which stands for *com-men-iscor and lit. means 'I ponder', fr. \"\n   \"com- and mens, gen. mentis\\\". From the causative o-grade *mon-eye- > Lat. monere 'to remind, warn': monitor \"\n   \"'one who reminds', monumentum 'that which reminds', and monstrum 'divine portent, monster' (< *mone-strom), \"\n   \"whence monstrare 'to point out' and de-monstrare > demonstrate (1550s). Skeat files monster and monument under \"\n   \"'Monition' (i.e. monere) and only mental under mens; Ernout-Meillet: \\\"A moneo se rattachent monstrum, \"\n   \"Moneta\\\". So the words are right and the root is right, but four of the seven are cousins of mens, not its \"\n   \"children.\"),\n \"derivation_fa\": (\"همهٔ این هفت واژه به ریشهٔ *men- می‌رسند، ولی تنها دو تای آنها به‌راستی از mēns (گرهٔ ۷) گرفته \"\n   \"شده‌اند و بقیه از دو ستاکِ خواهرِ لاتین می‌آیند؛ پس یک پیکان برای همه بسیار کلی است. از mēns/ment-: mental (از \"\n   \"mentalis لاتینِ پسین) و mention (از mentiō «به یاد آوردن» ← mention فرانسهٔ کهن ← mencioun انگلیسی میانه). از فعل \"\n   \"comminisci «با اندیشه پدید آوردن» (*com-men-iscor): comment از commentum «ساخته، پرداخته»؛ کلاین صریحاً \"\n   \"می‌نویسد که این صورت *com-men-iscor است و «می‌اندیشم» معنی می‌دهد. از درجهٔ o و ساختِ سببیِ *mon-eye- ← monēre \"\n   \"«یادآوری کردن، هشدار دادن»: monitor «یادآورنده»، monumentum «آنچه یاد را زنده می‌کند» و monstrum «نشانهٔ الهی، \"\n   \"هیولا» (از *mone-strom) که monstrāre و de-monstrāre ← demonstrate از آن است. اسکیت هم monster و monument را ذیل \"\n   \"«Monition» (یعنی monēre) آورده و تنها mental را ذیل mēns؛ ارنو-میه نیز می‌نویسد: «monstrum و Monēta به monēo \"\n   \"بازمی‌گردند». پس واژه‌ها و ریشه درست است، اما چهار واژه از هفت واژه عموزادهٔ mēns‌اند نه فرزند آن؛ با احتیاط \"\n   \"پذیرفتنی است.\"),\n \"sources\": [E_MONSTER, W_MENS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins men-1: I.1.b-c gives MENTAL and MENTION from Latin mens/mentio; II.2.b gives COMMENT from comminisci; III.1 gives \\\"Suffixed (causative) form *mon-eyo- in Latin monere ... MONISH, MONITION, MONITOR, MONSTER, MONUMENT, MUSTER; ADMONISH, DEMONSTRATE, PREMONITION, SUMMON\\\" - which is exactly the split described above.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~334 s.v. comment, p. ~1048-1050 s.v. monster, monument (KLN_1966.txt leaves 179, 536-537)\", \"stance\": \"supports\",\n    \"note\": \"\\\"comment ... fr. L. commentum ... fr. comminiscor ... which stands for *com-men-iscor and lit. means 'I ponder', fr. com- and mens, gen. mentis\\\"; \\\"monster ... fr. L. monstrum ... for *mone-strom, lit. 'that which serves as a warning', fr. monere\\\"; \\\"monument ... fr. L. monumentum ... lit. 'that which reminds', fr. monere\\\".\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mental, Monster, Monument (SKT.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Mental. (F.-L.) F. mental. - Low L. mentalis ... - L. ment-, stem of mens, mind\\\"; \\\"Monster; see Monition.\\\"; \\\"Monument; see Monition.\\\" - the same two-stem split.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. moneo / monstrum (LAT.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"A moneo se rattachent monstrum, Moneta, q.u.\\\"; \\\"monstrum, -i n.: ... a monendo dictum est, uelut monestrum\\\" (Aelius Stilo, Fest. 133,8).\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 727 (POK_02.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Kaus. moneo ,mahne' ..., monitor m. ,Mahner', monumentum ,Erinnerungszeichen', monstrum ,Mahnzeichen, Ungeheuer' (*mone-strom), mon-strare ,anzeigen'\\\".\"}\n ]\n})\ndata[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Manu, Manus\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *manu-s / *monu-s 'man, human being' (Pokorny 700); the connection with *men- 'to think' is only a possibility\",\n \"note\": (\"Both of Nourai's references really do say what he writes, but they are the older layer of scholarship. \"\n          \"Pokorny p.700 heads the entry \\\"manu-s oder monu-s 'Mann, Mensch'\\\" and closes \\\"WP. II 266, Trautmann \"\n          \"169; vielleicht zu 3. men- 'denken'\\\" - 'perhaps'. Klein p.930 s.v. man is more confident: 'All these \"\n          \"words prob. meant orig. \\\"one who thinks\\\", fr. I.-E. base *men-, \\\"to think\\\"', which is verbatim \"\n          \"Nourai's gloss 'one who thinks, man'. Current handbooks are more reserved: Mann (IEC) keeps *manus 'man' \"\n          \"expressly distinct from the type *monus 'thoughtful'; Watkins gives man-1 the bare gloss 'Man' and does \"\n          \"not cross-refer it to men-1; and Kroonen (after Berneker) prefers to derive Germanic *mann- from \"\n          \"*(dh)ghmon- 'human, earthling'. Hence 'plausible': the root and its gloss 'man' are real, the added \"\n          \"'one who thinks' is a 19th/20th-century etymology no longer standard.\"),\n \"note_fa\": (\"هر دو ارجاعِ نورایی به‌راستی همان را می‌گویند که او نوشته، اما هر دو لایهٔ کهن‌ترِ پژوهش‌اند. پوکورنی در \"\n             \"ص ۷۰۰ مدخل را «manu-s یا monu-s: مرد، انسان» می‌نامد و در پایان می‌نویسد «شاید به men- ۳ «اندیشیدن» \"\n             \"[مربوط باشد]» - یعنی با تردید. کلاین در ص ۹۳۰ ذیل man قاطع‌تر است: «این واژه‌ها احتمالاً در اصل «آن که \"\n             \"می‌اندیشد» معنی می‌داده‌اند، از ستاک هندواروپایی *men- «اندیشیدن»» - که همان معنایی است که نورایی آورده. \"\n             \"پژوهش امروزی محتاط‌تر است: مان (IEC) *manus «مرد» را از گونهٔ *monus «اندیشمند» جدا می‌داند؛ واتکینز man-1 \"\n             \"را تنها «Man» معنی می‌کند و آن را به men-1 ارجاع نمی‌دهد؛ و کرونن (به پیروی از برنکر) ترجیح می‌دهد *mann- \"\n             \"ژرمنی را از *(dʰ)ǵʰmon- «انسان، خاکی» بگیرد. پس: ریشه و معنای «مرد» درست است، ولی افزودهٔ «آن که \"\n             \"می‌اندیشد» ریشه‌شناسی سدهٔ نوزدهم و بیستم است و امروز معیار نیست؛ با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_MANNAZ],\n \"ref_check\": [\n   {\"ref\": \"KLN:930\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf NR=501, whose running head the OCR reads ۹۳۰/930, s.v. 'man': \\\"... and cogn. with OI. manuh, 'man; progenitor of mankind', Avestic manu-, 'man', OSlav. mozi, 'man'. All these words prob. meant orig. 'one who thinks', fr. I.-E. base *men-, 'to think', whence also OI. matih, 'thought', L. mens, gen. mentis, 'mind' ... See mind and cp. Manu, muzhik ...\\\" - word for word Nourai's root gloss.\"},\n   {\"ref\": \"POK:700\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt, leaf whose running head reads 700: \\\"manu-s oder monu-s ,Mann, Mensch'. Ai. manu-, manus- ,Mensch, Mann' (auch ,Ahnherr der Menschen'), av. im PN Manus-cithra-, urgerm. *manwaz im PN Mannus (Tacitus), Stammvater der Deutschen, got. manna (Gen. mans) ... WP. II 266, Trautmann 169; vielleicht zu 3. men- ,denken'.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. man-1 (AHD_watkins1985.txt line 722)\", \"stance\": \"partial\",\n    \"note\": \"\\\"man-1. Also mon-. Man. 1. Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz) ... [Pok. manu-s 700.]\\\" - the root is there, but Watkins gives no 'one who thinks' gloss and no cross-reference to men-1.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. manus (IEC.txt line 10322)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"manus (man-, manustios) 'man, human being, husband'. (Prob. distinct from type monus 'thoughtful', q.v., and from type monuos 'single, individual'.) WP II, 266 Skt. manuh 'man'; Av. cf. Manus-Cithro (a name) ...\\\" - Mann explicitly separates 'man' from 'thoughtful'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 266 (cited by Pokorny p.700; grep in WLD_Bd2_pages.txt found no separate headword)\", \"stance\": \"silent\",\n    \"note\": \"The OCR of Walde-Pokorny Bd. II does not yield the manu-s headword (Pokorny's own reference is WP. II 266).\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index (incoming/ARY/ARY_latin_index_pages.txt, pdf pp. 460-461)\", \"stance\": \"supports\",\n    \"note\": \"The entry grouping MANUS (Avestan), MANU/MANUS (Sanskrit), MANNA (Gothic), MAN (Old English), MUZH (Russian) gives 'REFERENCES: POKORNY 700; BARNHART (MAN) 627; MACKENZIE (MAN) 122; ONIONS (MAN) 550; SKEAT (MAN) 358' - i.e. an independent modern Persian handbook that anchors the group at Pokorny 700.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 2.21 MAN (SYN.txt line 2281)\", \"stance\": \"partial\",\n    \"note\": \"Buck's word-list for 'man' has Goth. wair, guma, manna; OE wer, ceorl, man; Skt. nar-, nara-, vira-, pumams-; Av. nar-, virad-, OPers. martiya- - note that the Iranian entries are nar-/martiya-, NOT manu-.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"manu, manuš, mainyuš; manuš-čitra\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The compound is right, the glosses of the simple words are not. (a) There is no Avestan common \"\n   \"noun manu-/manus- 'man': Bartholomae's Altiranisches Woerterbuch has only \\\"manus- m. EN. eines alten, \"\n   \"vorzeitlichen Helden\\\" (proper name of an ancient hero) and \\\"manusa- m. Name eines Bergs\\\" (a mountain). \"\n   \"Pokorny p.700 is careful for exactly this reason - he cites Avestan only 'im PN Manus-cithra-'. The Avestan \"\n   \"words for 'man' are nar- and mas(y)a-/masya-. Klein p.930 does assert 'Avestic manu-, \\\"man\\\"', which is what \"\n   \"Nourai followed, but that is an inference from Sanskrit manu-, not an attestation. (b) mainyus is the nom. sg. \"\n   \"of Av. mainyu- 'spirit, mind' (< *mn-yo-, Watkins men-1 I.3.b 'Avestan mainyu, spirit: AHRIMAN'); every \"\n   \"compound in Bartholomae glosses it 'Geist' (mainyu.tasta- 'von Geistern gefertigt', mainyu.suta- 'vom Geist \"\n   \"angetrieben'). It therefore belongs to *men- 'think' but means 'spirit', not 'man(ly)', and it does not belong \"\n   \"under this root box at all. (c) manus-cithra- is genuine: Bartholomae \\\"manus.cithra- m. EN. eines Glaeubigen \"\n   \"... Yt. 13.131\\\", i.e. 'having the seed/lineage of Manus' (cithra- 'seed, lineage, appearance' > MP cihr > NP \"\n   \"چهر). The book's spelling manus-citra is Nourai's simplified transcription of cithra-. Nourai's first gloss \"\n   \"'with manly face' is the folk etymology (the Borhan's 'behesht-ruy' story) that Mo'in flags as \"\n   \"قصةاللغة عامیانه; his alternative 'of \\\"Manush\\\" race' is the correct one.\"),\n \"derivation_fa\": (\"ترکیب درست است، ولی معنای واژه‌های ساده نه. الف) در اوستایی نامِ عامِ manu-/manuš- به معنای «مرد» \"\n   \"وجود ندارد؛ فرهنگ ایرانی باستانِ بارتولومه تنها «manuš- (مذکر) نام خاصِ پهلوانی کهن و پیش‌تاریخی» و «manuša- نام \"\n   \"کوهی» را دارد. پوکورنی نیز از همین رو در ص ۷۰۰ تنها می‌نویسد «اوستایی: در نام خاصِ Manuš.čiθra-». واژهٔ اوستایی \"\n   \"«مرد» nar- و maš(y)a- است. کلاین در ص ۹۳۰ «اوستایی manu- «مرد»» را می‌آورد و نورایی همان را پی گرفته، ولی این \"\n   \"استنتاج از manu- سنسکریت است نه گواهِ متنی. ب) mainyuš حالت فاعلیِ مفردِ mainyu- اوستایی است به معنای «مینو، روان، \"\n   \"گوهر مینوی» (از *mn̥-yo-؛ واتکینز ذیل men-1 می‌نویسد «اوستایی mainyu، spirit») و بارتولومه در همهٔ ترکیب‌ها آن را \"\n   \"«Geist» معنی می‌کند. پس این واژه به ریشهٔ *men- «اندیشیدن» می‌رسد ولی معنای آن «مینو/روان» است نه «مردانه»، و \"\n   \"جای آن در این جعبه نیست. پ) manuš.čiθra- درست است: بارتولومه «manuš.čiθra- نام خاصِ یکی از پیروان دین، فروردین \"\n   \"یشت بند ۱۳۱». معنای آن «از تخمه و نژادِ منوش» است (čiθra- «تخمه، نژاد، چهره» ← čihr پهلوی ← «چهر» فارسی). \"\n   \"املای «manuš-citra» در کتاب همان čiθra- است با نگارشِ ساده‌شدهٔ نورایی. معنای نخستِ او «با چهرهٔ مردانه» همان \"\n   \"ریشه‌شناسی عامیانه‌ای است که معین آن را «قصةاللغة عامیانه» می‌نامد؛ معنای دومِ او «از نژادِ منوش» درست است. \"\n   \"پژوهش امروزی گلوسِ «manu/manuš/mainyuš = مردانه» را رد می‌کند.\"),\n \"sources\": [W_MANU],\n \"ref_check\": [\n   {\"ref\": \"POK:700\", \"status\": \"partial\",\n    \"note\": \"Pokorny p.700 supports only the compound: \\\"av. im PN Manus-cithra-\\\". He gives no Avestan simplex and nothing about mainyus.\"},\n   {\"ref\": \"KLN:930\", \"status\": \"supports\",\n    \"note\": \"Klein p.930 s.v. man does write \\\"Avestic manu-, 'man'\\\", so Nourai's gloss is faithfully taken from his source - but the form is unattested (see consulted: BRT).\"},\n   {\"ref\": \"BQT:2047\", \"status\": \"supports\",\n    \"note\": \"BQT_v4_pages.txt [pdf page 130] = printed p.2047 (printed = pdf + 1917), Mo'in's footnote to منوچهر: «دراوستا Manuš.čiθra ... جزو دوم چیثره هم‌ریشهٔ «چهر» فارسی است که در اصل بمعنی نژاد بوده، این کلمهٔ مرکب بمعنی «از نژاد و پشت منوش» است. منوش محققاً یکی از ناموران قدیم بود که امروزه در اوستا اسمی ازو نیست ... اسم منوچهر و خاندان وی فقط یکبار در اوستا بند ۱۳۱ فروردین یشت یاد شده است.» Mo'in also marks the Borhan's 'behesht-ruy' explanation as folk etymology (قصةاللغة عامیانه).\"},\n   {\"ref\": \"SNS:241\", \"status\": \"partial\",\n    \"note\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the Pahlavi word-index (SNS_pages.txt leaf 229, index page ٢٥) lists \\\"manuyscihr 240/20\\\", i.e. Manuščihr occurs at p.240 line 20 of the glossary - adjacent to Nourai's p.241. The Persian OCR of the glossary pages themselves is unusable (refs_online.json flags it 'POOR'), and no page offset is established for this scan, so the exact page could not be read.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Woerterbuch s.vv. manus-, manusa-, manus.cithra-, mainyu- (BRT.txt)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"manus- m. EN. eines alten, vor[zeit]lichen Helden\\\"; \\\"manusa- m. Name eines Bergs\\\"; \\\"manus.cithra- m. EN. eines Glaeubigen: ...thraie airyavahu asaono 'des M., Sohns des A.' Yt. 13.131\\\". mainyu- is glossed 'Geist' throughout (mainyu.tasta- 'von Geistern gefertigt'). So Av. manus- is a hero's name, not 'man', and mainyus is 'spirit', not 'man(ly)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins men-1 I.3.b (AHD_watkins1985.txt line 745)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"Suffixed form *mn-yo- in ... b. Avestan mainyu, spirit: AHRIMAN\\\" - mainyu is filed under men-1 'to think' with the meaning 'spirit', not under man-1 'man'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.v. Manucihr (NYB_vol2_glossary.txt line 2428)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Manucihr [mnwcyhl] 1131-18, and Manus-cihr [m'nwcyhl] 47-2, 1165, the son of Erec and the successor of Fredon. - Av. (1135) Manus.cithra-; NP Manucihr.\\\" Confirms the compound and its Avestan source.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt), grep 'manu'\", \"stance\": \"silent\",\n    \"note\": \"Old Persian has no manu-; the only 'manu' hits in Kent are the English word 'manuscript'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"Manŭčehr «منوچهر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Av. Manus.cithra- (Yasht 13.131) 'of the lineage of Manus' > Middle Persian Manuscihr / Manucihr \"\n   \"(Pahlavi mnwcyhl and m'nwcyhl; the Bundahishn makes him the son of Manus-khwarnar and grandson of Erec/Iraj) > \"\n   \"New Persian منوچهر Manučehr, the Kayanid king of the Shahnama. The sound history is regular: the Avestan \"\n   \"cluster -sc- is simplified to -c- in Middle Persian, intervocalic Avestan -thr- gives MP -hr- (cithra- > cihr), \"\n   \"and MP cihr becomes NP چهر/چهره 'face, appearance'. Because cihr had shifted from 'seed, lineage' to 'face', \"\n   \"the name was re-etymologised in Persian as 'of the face of paradise' (mēnō 'paradise' + čehr 'face') - the \"\n   \"explanation given in Borhan-e Qate' and rejected by Mo'in as folk etymology. Nourai's gloss 'from Manush \"\n   \"family' is Mo'in's own («از نژاد و پشت منوش»), and his NOTE 'a male name' is correct.\"),\n \"derivation_fa\": (\"«منوچهر» از اوستایی Manuš.čiθra- (فروردین یشت، بند ۱۳۱) به معنای «از نژادِ منوش»؛ در فارسی میانه \"\n   \"Manuščihr / Manūčihr (به خطِ پهلوی mnwcyhl و m'nwcyhl؛ در بندهشن پسرِ منوش‌خورنر و از تبارِ ایرج) و در فارسی نو \"\n   \"«منوچهر»، شاهِ کیانیِ شاهنامه. دگرگونی آوایی قاعده‌مند است: خوشهٔ -šč- اوستایی در فارسی میانه به -č- ساده شده، \"\n   \"-θr- میان‌واکه‌ای اوستایی به -hr- بدل گشته (čiθra- ← čihr) و čihrِ پهلوی در فارسی نو «چهر/چهره» شده است. چون معنای \"\n   \"«چهر» از «تخمه و نژاد» به «رخ» گرایید، این نام در فارسی از نو ریشه‌شناسی عامیانه شد به «چهرهٔ مینو» (مینو + چهر) - \"\n   \"همان توضیحی که در برهان قاطع آمده و معین آن را ریشه‌شناسی عامیانه دانسته است. معنای «از خاندان منوش» که نورایی \"\n   \"داده، عیناً گفتهٔ معین است («از نژاد و پشت منوش») و یادداشت او «نام مردانه» نیز درست است. ادعای نورایی درست است.\"),\n \"sources\": [W_MANU],\n \"ref_check\": [\n   {\"ref\": \"BQT:2047\", \"status\": \"supports\",\n    \"note\": \"Printed p.2047 = BQT_v4_pages.txt [pdf page 130]: Mo'in's footnote «دراوستا Manuš.čiθra ... این کلمهٔ مرکب بمعنی «از نژاد و پشت منوش» است» and «اسم منوچهر و خاندان وی ... فقط یکبار در اوستا بند ۱۳۱ فروردین یشت یاد شده است»; the Borhan's own 'بهشت روی' derivation on the same page is footnoted قصةاللغة عامیانه (folk etymology).\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary (NYB_vol2_glossary.txt lines 2428-2430)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Manucihr ... and Manus-cihr ..., the son of Erec and the successor of Fredon. - Av. (1135) Manus.cithra-; NP Manucihr.\\\" and \\\"Manus-khwarnar ... the son of the preceding and the father of Manus-cihr\\\" (BdJ).\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae s.v. manus.cithra- (BRT.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"manus.cithra- m. EN. eines Glaeubigen ... Yt. 13.131\\\" - the Avestan attestation Mo'in and Nyberg refer to.\"},\n   {\"src\": \"FSF\", \"where\": \"Noushin, Vazhenamak (Farhang-e Shahnameh) (FSF_pages.txt)\", \"stance\": \"partial\",\n    \"note\": \"Noushin discusses منوچهر/منوچهری only as Shahnama vocabulary and does not give the Avestan etymology; his اهورامزدا entry (see entry 2) is the etymological one.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt), grep 'Manuscihr'\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie's dictionary excludes proper names, so Manuscihr is absent; the Pahlavi form comes from Nyberg.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Germanic\", \"words\": \"manna\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Nourai's 'manna' is the Gothic form used to label Proto-Germanic *mann-/*mannaz (n-stem, gen. \"\n   \"mans, pl. *manniz): Gothic manna, Old Norse maðr/mannr, Old English mann/man (pl. menn), Old Frisian monn, \"\n   \"Old High German man > German Mann, Middle Dutch man. Pokorny p.700 derives it from *manu-s with the u/w-stem \"\n   \"still visible in \\\"urgerm. *manwaz im PN Mannus (Tacitus, Germania 2), Stammvater der Deutschen\\\", and Watkins \"\n   \"man-1 has \\\"Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz)\\\". Modern Germanic etymology is \"\n   \"divided: Kroonen, following Berneker, prefers to trace *mann- to PIE *(dh)ghmon- 'human, earthling' (the \"\n   \"*dhghem- 'earth' family, cf. Lat. homo), with the initial cluster reduced in Germanic - which would sever it \"\n   \"both from Skt. manu- and from *men- 'to think'.\"),\n \"derivation_fa\": (\"«manna» در نمودار صورتِ گوتی است که نورایی برای نامیدنِ *mann-/*mannaz ژرمنیِ آغازین (ستاکِ n با \"\n   \"حالت اضافیِ mans و جمعِ *manniz) به کار برده است: manna گوتی، maðr/mannr نورسِ کهن، mann/man انگلیسی کهن (جمع \"\n   \"menn)، monn فریزی کهن، man آلمانی علیای کهن ← Mann آلمانی، man هلندی میانه. پوکورنی در ص ۷۰۰ آن را از *manu-s \"\n   \"می‌گیرد و ستاکِ u/w را در «*manwaz ژرمنیِ آغازین در نام خاصِ Mannus (تاسیت، ژرمانیا ۲)، نیای آلمانیان» نشان \"\n   \"می‌دهد، و واتکینز نیز می‌نویسد «صورت‌های گسترش‌یافتهٔ *manu-, *manw- در *manna- ژرمنی (جمع *manniz)». ریشه‌شناسیِ \"\n   \"امروزیِ ژرمنی دو دسته است: کرونن به پیروی از برنکر ترجیح می‌دهد *mann- را از *(dʰ)ǵʰmon- «انسان، خاکی» بگیرد \"\n   \"(از خانوادهٔ *dʰǵʰem- «زمین»، قس homo لاتین) با ساده‌شدنِ خوشهٔ آغازی در ژرمنی، که در آن صورت پیوندِ آن با manu- \"\n   \"سنسکریت و با *men- «اندیشیدن» بریده می‌شود. صورت و معنای گره درست است.\"),\n \"sources\": [W_MANNAZ],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins man-1: \\\"1. Extended forms *manu-, *manw- in Germanic *manna- (plural *manniz), in: a. Old English man(n) (plural menn), man: MAN; NORMAN; b. Old High German man ...; c. Middle Dutch man, man: MANIKIN, (MANNEQUIN); d. Old Norse madhr, mannr, man: NORMAN, OMBUDSMAN.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 700 (POK_02.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"urgerm. *manwaz im PN Mannus (Tacitus), Stammvater der Deutschen, got. manna (Gen. mans), aisl. madr, mannr, a[gs.] afries. ahd. mann ,Mann', got. manniskis ... 'menschlich'\\\".\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. 930 s.v. man (KLN_1966.txt leaf NR=501)\", \"stance\": \"supports\",\n    \"note\": \"\\\"... G. Mann, ON. madr (for *mannr), Dan. mand, Goth. manna, 'man' (cp. Mannus, a tribal deity, in Tacitus' Germania, chapt. 2), OS. mennisco, OFris. manniska, MDu. mensche, Du. mens, OHG. mannisco ...\\\"\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt), grep 'Man,'\", \"stance\": \"silent\",\n    \"note\": \"The OCR of Skeat's M pages is defective around this entry (neither 'Man' nor 'Music' can be retrieved); no reading obtained.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"mannequin\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"French mannequin (15th c.) is a borrowing from Middle Dutch/Dutch manneken 'little man', the \"\n   \"diminutive of man - so the arrow from the Germanic box is right, but the immediate donor is Dutch, not Gothic, \"\n   \"and the -quin spelling is the French adaptation of the Dutch diminutive suffix -ken. In French the word first \"\n   \"meant a jointed artist's figure, then (from 1853, in translations) an artificial figure for displaying \"\n   \"clothes, then a live fashion model; the last sense went back into English in 1898. English manikin (1560s) is \"\n   \"a separate, earlier borrowing of the same Dutch word, which is why Nourai can list manikin in node #6 and \"\n   \"mannequin here.\"),\n \"derivation_fa\": (\"mannequin فرانسوی (سدهٔ پانزدهم) وام‌واژه‌ای است از manneken هلندی/هلندیِ میانه به معنای «مردِ \"\n   \"کوچک»، مصغّرِ man؛ پس پیکانِ آمده از جعبهٔ ژرمنی درست است، ولی وام‌دهِ بی‌واسطه هلندی است نه گوتی، و املای -quin \"\n   \"برگردانِ فرانسویِ پسوندِ تصغیرِ هلندیِ -ken است. در فرانسه نخست به «پیکرکِ مفصل‌دارِ نقاشان»، سپس از ۱۸۵۳ م به \"\n   \"«پیکرِ بدلی برای نمایشِ لباس» و آنگاه به «مانکنِ زنده» گفته شد؛ معنای آخر در ۱۸۹۸ م به انگلیسی بازگشت. manikin \"\n   \"انگلیسی (دههٔ ۱۵۶۰) وام‌گیریِ جداگانه و کهن‌ترِ همان واژهٔ هلندی است، و از این‌رو نورایی manikin را در گرهٔ ۶ و \"\n   \"mannequin را اینجا آورده است. ادعای نورایی درست است.\"),\n \"sources\": [E_MANNEQ],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given for the French box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. ~980 s.v. mannequin, manikin (KLN_1966.txt leaves 501-502)\", \"stance\": \"supports\",\n    \"note\": \"\\\"manikin, n., 1) a little man; a dwarf; 2) a model of the human body; 3) a mannequin. - Du. manneken, 'little man', dimin. of man, 'man'.\\\"; \\\"mannequin, n., ... - F., fr. Du. manneken, 'little man'. See manikin.\\\"\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. III s.v. mannequin (FSD_vol3.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"4. A little man, pigmy; dwarf. [< F. mannequin, < MD. manneken, dim. of man, man]\\\"\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins man-1 1.c (AHD_watkins1985.txt line 722)\", \"stance\": \"supports\",\n    \"note\": \"\\\"c. Middle Dutch man, man: MANIKIN, (MANNEQUIN)\\\" - the Dutch stage is explicit.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"mânkan «مانکن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"French mannequin > Persian مانکن mânken/mânkan, a 20th-century loan that came in with European \"\n   \"tailoring and the ready-made clothing trade. French [manəkɛ̃] was adapted by replacing the nasal vowel of the \"\n   \"final syllable with -kan/-ken (Persian has no nasal vowels), and the geminate -nn- was simplified. Mo'in's \"\n   \"Farhang defines it «پیکر بدلی به شکل انسان که از چوب، مقوا و غیره سازند و بر آن لباس پوشانند و در خیاطخانه‌ها \"\n   \"و مغازه‌های لباس‌فروشی به معرض تماشا [گذارند]» with a French origin tag, i.e. exactly Nourai's 'manikin'. The \"\n   \"word is thus, at the far end of the chart, a Germanic word (Dutch manneken) that reached Persian through \"\n   \"French - a route Nourai draws correctly.\"),\n \"derivation_fa\": (\"«مانکن» از mannequin فرانسوی، وام‌واژه‌ای از سدهٔ بیستم که همراه با خیاطیِ اروپایی و بازارِ \"\n   \"لباسِ آماده به فارسی آمد. واکهٔ خیشومیِ هجای پایانیِ فرانسوی، چون فارسی واکهٔ خیشومی ندارد، به -کن/-کان بدل شده و \"\n   \"همخوانِ مشدّدِ -nn- ساده گشته است. معین آن را «پیکر بدلی به شکل انسان که از چوب، مقوا و غیره سازند و بر آن لباس \"\n   \"پوشانند و در خیاطخانه‌ها و مغازه‌های لباس‌فروشی به معرض تماشا [گذارند]» معنی کرده و برچسبِ [فر.] بر آن نهاده - \"\n   \"همان «manikin» نورایی. پس این واژه در انتهای نمودار، واژه‌ای ژرمنی (manneken هلندی) است که از راه فرانسه به \"\n   \"فارسی رسیده و نورایی این مسیر را درست کشیده است. ادعای نورایی درست است.\"),\n \"sources\": [E_MANNEQ],\n \"ref_check\": [\n   {\"ref\": \"MON:3721\", \"status\": \"not_checked\",\n    \"note\": \"The 6-volume Farhang-e Farsi is not digitised (refs_online.json: only the 2-volume Adena condensation). That condensation carries the entry: «مانکن: [فر.] (اِ.) پیکر بدلی به شکل انسان که از چوب، مقوا و غیره سازند و بر آن لباس پوشانند و در خیاطخانه‌ها و مغازه‌های لباس‌فروشی به معرض تماشا ...» (MON_part2.txt), which is what p.3721 would carry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. مانکن (2-vol Adena condensation)\", \"stance\": \"supports\",\n    \"note\": \"«مانکن: [فر.] (اِ.) پیکر بدلی به شکل انسان که از چوب، مقوا و غیره سازند و بر آن لباس پوشانند ...» - French tag plus Nourai's meaning.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt), grep 'مانکن'\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian covers only inherited vocabulary; no entry.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. mannequin (KLN_1966.txt leaf NR=502)\", \"stance\": \"supports\",\n    \"note\": \"Gives the French > Dutch source of the word that Persian borrowed.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"man, Norman, Herman, manikin\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All four contain Germanic *mann-. man < OE mann/man (pl. menn) < PGmc *mannaz. Norman < Old \"\n   \"French Normant (mod. Normand), literally 'North-man', i.e. Old Norse Nordhmadhr (nordhr + madhr < *mannaz), \"\n   \"the name the Franks gave the Vikings who settled Normandy in the 10th c.; Klein s.v. Norman: \\\"OF. Normant, F. \"\n   \"Normand, lit. 'Northman'. See Northman.\\\" Herman < Germanic *Hari-man 'army-man' (OHG Hariman/Heriman, hari \"\n   \"'army' + man), an ordinary Germanic dithematic name, borrowed into English through Dutch/German. manikin \"\n   \"(1560s) < Dutch manneken 'little man'. Nourai's page reference is right: Klein's article 'man', with the whole \"\n   \"Germanic list, stands on p.930 of the 1966 edition, and the Norman and manikin entries cross-refer to it.\"),\n \"derivation_fa\": (\"هر چهار واژه *mann- ژرمنی را در خود دارند. man از mann/man انگلیسی کهن (جمع menn) از *mannaz \"\n   \"ژرمنیِ آغازین. Norman از Normant فرانسهٔ کهن (Normand امروزی) به معنای تحت‌اللفظیِ «مردِ شمال»، یعنی Norðmaðr \"\n   \"نورسِ کهن (norðr «شمال» + maðr از *mannaz)، نامی که فرانکان به وایکینگ‌های ساکنِ نورماندی در سدهٔ دهم دادند؛ \"\n   \"کلاین ذیل Norman می‌نویسد: «فرانسهٔ کهن Normant، فرانسهٔ نو Normand، تحت‌اللفظی «مردِ شمال»». Herman از \"\n   \"*Hari-man ژرمنی «مردِ سپاه» (Hariman/Heriman آلمانی علیای کهن، از hari «سپاه» + man)، نامی دوجزئیِ معمولِ \"\n   \"ژرمنی که از راه هلندی/آلمانی به انگلیسی رسیده. manikin (دههٔ ۱۵۶۰) از manneken هلندی «مردِ کوچک». ارجاعِ \"\n   \"صفحهٔ نورایی درست است: مقالهٔ «man» کلاین با همین فهرستِ ژرمنی در ص ۹۳۰ چاپ ۱۹۶۶ آمده و مدخل‌های Norman و \"\n   \"manikin به آن ارجاع می‌دهند. ادعای نورایی درست است.\"),\n \"sources\": [E_MANNEQ, W_MANNAZ],\n \"ref_check\": [\n   {\"ref\": \"KLN:930\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf NR=501 = printed p.930 (running head read by the OCR as 930; leaves 500=929, 502=932 bracket it), s.v. 'man': the full Germanic cognate list plus 'All these words prob. meant orig. \\\"one who thinks\\\"'. Klein's 'Norman' (leaf 587 region: \\\"OF. Normant, F. Normand, lit. 'Northman'\\\") and 'manikin' (leaf 501: \\\"Du. manneken, 'little man'\\\") entries cross-refer to it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins man-1 and index (AHD_watkins1985.txt lines 722, 1810, 1813, 1935)\", \"stance\": \"supports\",\n    \"note\": \"Index: 'MAN man-1', 'NORMAN man-1, ner-1', 'MANIKIN man-1', 'MANNEQUIN man-1' - all four of Nourai's items except Herman, which Watkins does not list.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. Norman, manikin (KLN_1966.txt leaves 587, 501)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Norman, n., 1) one of the Northmen who occupied Normandy in the 10th cent. ... - OF. Normant, F. Normand, lit. 'Northman'.\\\"; \\\"manikin ... Du. manneken, 'little man', dimin. of man\\\".\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. III s.v. mannequin/manikin (FSD_vol3.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"[< F. mannequin, < MD. manneken, dim. of man, man]\\\" for the manikin/mannequin pair.\"}\n ]\n})\ndata[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Men-dh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *mendh- (*men-dheh1-) 'to direct one's mind to, learn' (Pokorny 730; Watkins mendh-1 'To learn')\",\n \"note\": (\"Correct in every respect, and Nourai's hyphenated spelling 'Men-dh' is Pokorny's own analysis. Pokorny \"\n          \"p.730: \\\"mendh- ,seinen Sinn worauf richten, lebhaft sein'\\\" and, at the end of the article, \\\"Idg. \"\n          \"men-dh- durch Zusammenrueckung aus *men-dhe- ,den Sinn worauf setzen'\\\" - i.e. the root is a compound of \"\n          \"*men- 'mind' with *dheh1- 'to put', which is exactly why Nourai cross-refers the Avestan node to his \"\n          \"root Dhě 2. Watkins glosses mendh-1 simply 'To learn' [Pok. mendh- 730], which is Nourai's gloss verbatim. \"\n          \"The one thing to keep in mind is that the same page of Pokorny also assigns Greek Mousa here - which is \"\n          \"where entry 0 node #1 should have been hung.\"),\n \"note_fa\": (\"این مدخل از هر نظر درست است و نگارشِ خط‌فاصله‌دارِ «Men-dh» همان تحلیلِ خودِ پوکورنی است. پوکورنی در ص \"\n             \"۷۳۰ می‌نویسد: «mendh-: ذهن را به چیزی گرداندن، سرزنده بودن» و در پایانِ مقاله: «men-dh هندواروپایی از \"\n             \"به‌هم‌پیوستنِ *men-dhe- «ذهن را بر چیزی نهادن» پدید آمده است» - یعنی این ریشه ترکیبی است از *men- «ذهن» \"\n             \"با *dʰeh₁- «نهادن»، و همین است که نورایی گرهٔ اوستایی را به ریشهٔ «Dhě ۲» ارجاع داده. واتکینز نیز mendh-1 \"\n             \"را تنها «to learn» معنی کرده و به همان ص ۷۳۰ پوکورنی ارجاع داده است، که عیناً معنای نورایی است. تنها \"\n             \"نکته آنکه همان صفحهٔ پوکورنی Mousa یونانی را نیز به همین ریشه نسبت می‌دهد - جایی که در واقع گرهٔ ۱ از \"\n             \"مدخل نخست باید آویخته می‌شد. ادعای نورایی درست است.\"),\n \"sources\": [E_MATH],\n \"ref_check\": [\n   {\"ref\": \"POK:730\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt, the leaf whose running head reads 730: \\\"mendh- ,seinen Sinn worauf richten, lebhaft sein'; m(o)ndh-ro- ,munter'. Ai. medha ,Weisheit, Einsicht, Verstand', av. mazda, mazdah- n. ,Gedaechtnis, Erinnerung', mazdah- m. Name des hoechsten Gottes (*mazdha aus *mndh-ta); gr. manthano ... ,lernen' ... vielleicht Mousa (*mon-dh-ia) ,Muse' ... Idg. men-dh- durch Zusammenrueckung aus *men-dhe- ,den Sinn worauf setzen' ... WP. II 270 f.\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 270-271 (WLD_Bd2_pages.txt lines 17832-17865)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mendh- ,seinen Sinn worauf richten, angeregt, lebhaft sein'. Ai. medha ,Weisheit ...', av. mazda, mazdah- n. ,Gedaechtnis, Erinnerung', mazdah- m. Name des hoechsten Gottes (*mazdha aus *mndh-ta) ... Idg. men-dh- ist Erw. von men- ,denken', genauer wohl Zsrueckung men-dhe- ,den Sinn worauf setzen'\\\".\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mendh-1 (AHD_watkins1985.txt line 749)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mendh-1. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMATICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.]\\\"\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. 947 s.v. mathematical (KLN_1966.txt leaf NR=509)\", \"stance\": \"supports\",\n    \"note\": \"\\\"fr. *mndh-, reduced form of I.-E. base *men-dh-, 'to have one's mind aroused, apply oneself to' ... Base *men-dh- is an enlargement of base *men-, 'to think'.\\\"\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 730 (POK_02.txt)\", \"stance\": \"supports\", \"note\": \"See ref_check above.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"ma[n]dz-dha, mazdha : learned, wise; ahura-mazdha; mazda-yasna\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"The odd-looking first form is not a misprint: it is copied straight from Klein p.1095 s.v. Ormazd, \"\n   \"who writes 'Avestic ma(n)dzdha-, \\\"wise\\\"'. The standard transcription is Av. mazda- (stem mazdah-), from \"\n   \"*mns-dheh1-/*mns-dheh2 'having set (one's) mind', i.e. the acc. *mns of manah- 'mind' compounded with *dheh1- \"\n   \"'to put' - which is precisely Nourai's cross-reference to Dhě 2, and which Watkins states as an \"\n   \"'Indo-European verb phrase *mens dhe-, \\\"to set mind\\\"'. Bartholomae's own glosses are worth keeping: \"\n   \"mazdah- n. is 'memoria, Gedaechtnis' (memory) and mazdah- m. is 'Name des hoechsten Gottes'; the sense 'wise' \"\n   \"is the one the word carries in the compound (Mo'in, summarising Bartholomae col. 1192: «چون با اهوره استعمال \"\n   \"شود ازآن معنی هوشیار و دانا و آگاه اراده کنند»). ahura-mazda- is thus 'the Lord Wisdom / the wise Lord' (Old \"\n   \"Persian Auramazda, attested about a hundred times in Kent's lexicon and abbreviated by the ideogram AM). \"\n   \"mazda-yasna- / mazdayasna- is 'Mazda-worshipper', Bartholomae \\\"'der den Mazdah verehrt, anbetet; Anhaenger \"\n   \"der Mazdah-religion'\\\". The extra -h- in Nourai's mazdha/ahura-mazdha is again Klein's notation of the \"\n   \"aspirate *dh.\"),\n \"derivation_fa\": (\"صورتِ عجیبِ نخست غلط چاپی نیست: عیناً از کلاین ص ۱۰۹۵ ذیل Ormazd گرفته شده که می‌نویسد «اوستایی \"\n   \"ma(n)dzdha- «دانا»». نگارشِ معیار mazdā- اوستایی (ستاکِ mazdāh-) است، از *mn̥s-dʰeh₁-/*mn̥s-dʰéh₂ «آن که ذهن \"\n   \"[خود را بر چیزی] نهاده»، یعنی حالتِ مفعولیِ *mn̥s از manah- «منش، ذهن» در ترکیب با *dʰeh₁- «نهادن» - و همین \"\n   \"است ارجاعِ نورایی به ریشهٔ «Dhě ۲»؛ واتکینز نیز آن را «عبارتِ فعلیِ هندواروپاییِ *mens dhē- «ذهن نهادن»» می‌نامد. \"\n   \"گلوسِ خودِ بارتولومه را باید در نظر داشت: mazdāh- در حالتِ خنثی «memoria، حافظه، یاد» و در حالتِ مذکر «نامِ \"\n   \"خدای برین» است؛ معنای «دانا» معنایی است که واژه در ترکیب می‌گیرد (معین در خلاصهٔ سخنِ بارتولومه، ستون ۱۱۹۲: «چون \"\n   \"با اهوره استعمال شود ازآن معنی هوشیار و دانا و آگاه اراده کنند»). پس ahura-mazdā- «سرورِ دانا / خداوندِ خرد» \"\n   \"است (در پارسی باستان Auramazdā، با نزدیک به صد گواه در واژه‌نامهٔ کنت و نشانهٔ اختصاریِ AM). mazda-yasna- نیز \"\n   \"«مزداپرست» است؛ بارتولومه: «آن که مزداه را می‌ستاید و می‌پرستد؛ پیروِ دینِ مزداه». افزودگیِ -h- در mazdha و \"\n   \"ahura-mazdha نیز شیوهٔ نگارشِ کلاین برای واکِ دمیدهٔ *dʰ است. ادعای نورایی درست است.\"),\n \"sources\": [W_MAZDA, W_AHURA],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins men-1 V: \\\"Indo-European verb phrase *mens dhe-, 'to set mind' (see dhe-1), underlying compound *mns-dhe- in Avestan mazda-, wise: AHURA MAZDA, ORMAZD. [Pok. 3. men- 726, mendh- 730.]\\\" - both the compound analysis and Nourai's Dhe cross-reference. The index has 'AHURA MAZDA ansu-, men-1' and 'ORMAZD ansu-, men-1'.\"},\n   {\"ref\": \"KLN:1095\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf NR=587, which the leaf/page fit puts at printed p.1095 (leaf 536 = p.998 at ~1.915 pages per leaf), s.v. Ormazd: \\\"Pers., fr. OPers. Auramazda, fr. Avestic Ahuramazda, lit. 'wise lord', a compound of ahura-, 'a god, a good spirit' (see ahura), and ma(n)dzdha-, 'wise', which is a compound formed from the I.-E. bases *men-dh-, 'to apply oneself to', and *dhe-, 'to put, place'. From base *men-dh- derives also OI. medha, 'wisdom, intelligence'. For other derivatives of this base see mathematical. For base *dhe- see do ...\\\" This is verbatim the source of Nourai's 'ma[n]dz-dha' and of the Dhe cross-reference.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.vv. mazdah- (n. and m.), mazdatae-, mazdatha-, a(h)ura-mazdah-, mazda-yasna- (BRT.txt lines 20214-20222, 6879-6903, 20201)\", \"stance\": \"partial\",\n    \"note\": \"\\\"mazdah- n. 'memoria, Gedaechtnis', nur AS. mazdam mit kar-\\\"; \\\"mazdah- m. Name des hoechsten Gottes\\\"; \\\"mazdatae(-ca) Inf. 'dem Gedaechtnis einzupraegen, im Gedaechtnis zu behalten'\\\"; \\\"a(h)ura-mazdah- m. Name des hoechsten Gottes\\\" (also as Old Persian); \\\"mazda-yasna- Adj. 'der den Mazdah verehrt, anbetet; Anhaenger der Mazdah-religion'\\\". Bartholomae's primary gloss is 'memory', not 'wise' - hence 'partial'.\"},\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 730 (POK_02.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"av. mazda, mazdah- n. ,Gedaechtnis, Erinnerung', mazdah- m. Name des hoechsten Gottes (*mazdha aus *mndh-ta)\\\" - note that Pokorny's *mazdha is the very spelling Nourai and Klein use.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian (KNT.txt), grep 'Auramazda'\", \"stance\": \"supports\",\n    \"note\": \"About 99 occurrences of Auramazda / Auramazdaha in the texts and in Kent's paradigms, plus the ideogram list §18: \\\"40 AM 'Ahuramazda'\\\" - the Old Persian form of the compound.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 270 (WLD_Bd2_pages.txt line 17832 ff.)\", \"stance\": \"supports\",\n    \"note\": \"Same data as Pokorny plus \\\"ao. maz-da- ,dem Gedaechtnis einpraegen' (davon mazdra- ,verstaendig, weise')\\\".\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"Mazdâ «مزدا»; Ahŭrâmazdâ «اهورامزدا ( هرمز )»; mazdîsnâ «مزدیسنا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Three modern Persian forms of the same Avestan material. (a) مزدا and (b) اهورامزدا are learned \"\n   \"re-borrowings of the Avestan name, made in the 19th-20th c. by Iranian scholars of Zoroastrianism (Purdavud \"\n   \"and after) directly from the Avesta. (c) The inherited line, which Nourai gives in the parenthesis, runs Av. \"\n   \"ahura- mazda- > Old Persian Auramazda > Middle Persian Ohrmazd/Ohrmizd (MacKenzie: \\\"Ohrmazd ['whrmzd | M \"\n   \"'whrm(y)zd, N Hormuzd] Ahura Mazda: astr. Jupiter\\\") > New Persian هرمز/هرمزد/اورمزد/هورمزد - the loss of the \"\n   \"medial -a-, the contraction ahura- > ohr-, and the shift of the final -d are all regular; Mo'in sets them out \"\n   \"in his note to Borhan-e Qate' s.v. ارمز, and adds that Hormozd is also the name of the first day of each \"\n   \"solar month and, later, of the planet Jupiter (Biruni, al-Athar al-baqiya: Persian هرمزد, Sogdian خرمژد, \"\n   \"Khwarezmian ریمژد). (d) مزدیسنا continues Av. mazdayasna- through MP mazdesn (MacKenzie: \\\"mazdesn ... \"\n   \"Mazda-worshipping, Mazdean; -ih: Mazda-worship, Mazdaism\\\"; Nyberg: \\\"mazdesneh ... the state of being a \"\n   \"Mazdayasnian\\\"), the modern Persian shape being a learned restitution of the Avestan -yasna-.\"),\n \"derivation_fa\": (\"سه صورتِ فارسیِ نو از یک مادهٔ اوستایی. الف و ب) «مزدا» و «اهورامزدا» وام‌گیریِ عالمانه و \"\n   \"دوباره‌ای است که ایران‌شناسان و اوستاپژوهانِ سدهٔ سیزدهم و چهاردهمِ خورشیدی (پورداود و پس از او) مستقیماً از \"\n   \"اوستا کرده‌اند. پ) رشتهٔ موروثی که نورایی درونِ کمانک آورده چنین است: ahura- mazdā- اوستایی ← Auramazdā پارسی \"\n   \"باستان ← Ōhrmazd/Ōhrmizd فارسی میانه (مکنزی: «Ōhrmazd [ʼwhrmzd، مانوی ʼwhrm(y)zd، فارسی نو Hōrmuzd]، اهورامزدا؛ \"\n   \"در نجوم: مشتری») ← «هرمز، هرمزد، اورمزد، هورمزد» در فارسی نو؛ افتادنِ -a- میانی، فشرده‌شدنِ ahura- به ōhr- و \"\n   \"دگرگونیِ -d پایانی همه قاعده‌مندند. معین در حاشیهٔ برهان قاطع ذیل «ارمز» همین را می‌آورد و می‌افزاید که هرمزد نامِ \"\n   \"روزِ نخستِ هر ماهِ شمسی و سپس نامِ اخترِ مشتری است (بیرونی در آثارالباقیه: در فهرست روزهای ایرانی «هرمزد»، سغدی \"\n   \"«خرمژد»، خوارزمی «ریمژد»). ت) «مزدیسنا» ادامهٔ māzdayasna- اوستایی است از راهِ māzdēsn فارسی میانه (مکنزی: \"\n   \"«māzdēsn: مزداپرست، مزدیسنی؛ māzdēsnīh: مزداپرستی»؛ نیبرگ: «māzdēsnēh: مزدیسنی‌بودن») و صورتِ فارسیِ امروزی \"\n   \"بازسازیِ عالمانهٔ -yasna- اوستایی است. ادعای نورایی درست است.\"),\n \"sources\": [W_AHURA, W_MAZDA],\n \"ref_check\": [\n   {\"ref\": \"BQT:109\", \"status\": \"supports\",\n    \"note\": \"The page is BQT_v1_pages.txt leaf 321, s.v. ارمز, whose running head the OCR reads as ۱۰۵; the leaf-to-page offset of this scan drifts between about 210 and 220 across the volume (refs_online.json), so leaf 321 sits within the 105-111 band and this is the page Nourai means - it is the only place in Borhan-e Qate' with the Ahura Mazda etymology. Mo'in's footnote: «اوستا Ahura Mazdā، پارسی باستان Auramazdā، پهلوی [Ōhrmazd]، در فارسی هرمزد (بفتح میم)، هرمزد (بضم میم)، اورمزد، هورمزد، هرمز هم آمده. نام خدای مزدیسنا، مرکب از اهوره در اوستا و Asura در سانسکریت از ریشهٔ asu سانسکریت و ahu اوستا بمعنی سرور و مولی ... مزدا در اوستا (یسنا ۴۰:۱) بمعنی حافظه آمده. در گاثاها (یسنا ۴۵:۱) بمعنی بخاطر سپردن و بیاد داشتن است. این کلمه در سانسکریت صورت medhas بمعنی دانش و هوش است، بنابراین چون با اهوره استعمال شود ازآن معنی هوشیار و دانا و آگاه اراده کنند «بارتولمه ۱۱۹۲» ... بنابر آنچه گفته شد اهورامزدا بمعنی سرور داناست.»\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.vv. Ohrmazd, mazdesn (PHD_mackenzie.txt line 3846; PHD.txt line 472)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Ohrmazd ['whrmzd | M 'whrm(y)zd, N Hormuzd] Ahura Mazda: astr. Jupiter\\\"; \\\"mazdesn [m'zd(y)sn' | M m'zdys] Mazda-worshipping, Mazdean. -ih: Mazda-worship, Mazdaism.\\\" Also the English-Pahlavi index: \\\"Ahuramazda Ohrmazd\\\", \\\"Mazdean mazdesn\\\", \\\"Jupiter (astr.) Ohrmazd\\\".\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary (NYB_vol2_glossary.txt lines 2522, 4343)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mazdesneh [m'zdysnyh] the state of being a Mazdayasnian 63H\\\"; and s.v. khwarrah: one swears 'pat khwarrah i Ohrmazd bag u den i mazdesnan'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. اهورا هرمز اهورامزدا (incoming/ARY/ARY_pages.txt, pdf p. 98 = printed p. 99)\", \"stance\": \"supports\",\n    \"note\": \"The entry lists Avestan Ahura/Ahurō, Old Persian Auramazdā, Pahlavi Ōhrmazd and Sanskrit asura/asu, and notes «ریشهٔ اوستایی این واژه دارای دو بخش است، بخش نخست آن در این فهرست پیگیری شده است، برای شناخت بخش دوم آن به «[آ]منش» بازگشت شود» - i.e. Aryanpur too analyses the name as ahura + a 'mind' element, citing Borhan-e Qate' and Farhang-e Mo'in.\"},\n   {\"src\": \"FSF\", \"where\": \"Noushin, Vazhenamak / Farhang-e Shahnameh s.v. اورمزد، هرمز (FSF_pages.txt)\", \"stance\": \"supports\",\n    \"note\": \"«همه اینها شکل‌های دیگری از «اهورامزدا»ی اوستایی است که نام ایزد است: اهورامزدا مرکب از دو واژه است ...» - the Shahnama forms اورمزد/هرمز are identified as the same Avestan name.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', Mo'in's ed., s.v. اهورامزدا (BQT_v1_pages.txt leaf 411, printed p. ~191-194)\", \"stance\": \"supports\",\n    \"note\": \"«اهورامزدا - بفتح اول و ششم، رك: ارمز» - the Borhan itself cross-refers اهورامزدا to the ارمز entry where the etymological footnote stands.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"manthanein\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. manthano (inf. manthanein) 'to learn' is built on the zero grade *mndh- of *mendh- with the \"\n   \"nasal-infix/-an- present formation, beside the aorist stem math- (emathon, inf. mathein) and the future \"\n   \"mathesomai; Pokorny p.730 notes that the present is secondary to the aorist (\\\"gr. manthano (sekundaeres \"\n   \"Praes. zu) mathesomai, mathein ,lernen'\\\") and adds the derivatives mathos n. and mathesis 'learning, \"\n   \"instruction'. Watkins mendh-1: \\\"Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn\\\". \"\n   \"The gloss 'to learn' is exactly right.\"),\n \"derivation_fa\": (\"manthánō یونانی (مصدرِ manthánein) «آموختن» بر پایهٔ درجهٔ صفرِ *mn̥dh- از *mendh- و با ساختِ \"\n   \"حالِ میان‌افزودهٔ خیشومی/-an- ساخته شده، در برابرِ ستاکِ گذشتهٔ سادهٔ math- (émathon، مصدرِ mathein) و آیندهٔ \"\n   \"mathḗsomai. پوکورنی در ص ۷۳۰ یادآور می‌شود که ستاکِ حال ثانوی و برساختهٔ از ستاکِ ماضی است («manthánō یونانی، \"\n   \"حالِ ثانوی برای mathḗsomai، mathein «آموختن»») و مشتق‌های máthos و máthēsis «آموزش» را می‌افزاید. واتکینز نیز \"\n   \"ذیل mendh-1 می‌نویسد: «درجهٔ صفرِ *mn̥dh- در manthánein یونانی (ستاکِ ماضیِ math-)، «آموختن»». معنایی که نورایی \"\n   \"داده کاملاً درست است.\"),\n \"sources\": [E_MATH],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins mendh-1: \\\"To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMATICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.]\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I p. 730 (POK_02.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"gr. manthano (sekundaeres Praes. zu) mathesomai, mathein ,lernen', dor.-aeol. mathe, ion. mathos n., ion.-att. mathesis ,Lernen, Unterricht'\\\".\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 270 (WLD_Bd2_pages.txt line 17836 ff.)\", \"stance\": \"supports\",\n    \"note\": \"Same wording, with the added reference to Curtius 311 f. and Meillet, De indoeur. rad. 41 f.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p. 947 s.v. mathematical (KLN_1966.txt leaf NR=509)\", \"stance\": \"supports\",\n    \"note\": \"\\\"from the aorist mathein (whence the pres. manthanein), 'to learn', fr. *mndh-, reduced form of I.-E. base *men-dh-\\\".\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"mathematics\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. mathema (gen. mathematos) 'that which is learnt, lesson, science', from the aorist stem math- \"\n   \"of manthanein, gave the adjective mathematikos 'fond of learning, scientific, mathematical' and the \"\n   \"substantivised feminine mathematike (techne) 'the mathematical art'; this became Lat. mathematica (pl. \"\n   \"mathematica/mathematicae), Old French mathematique, Middle English mathematik (late 14th c.), and was \"\n   \"remodelled with the plural -ics in the 1580s to give mathematics (whence math 1890 AmE, maths 1911 BrE). \"\n   \"Klein's entry on p.947-948 covers the whole chain, and Watkins files MATHEMATICAL/MATHEMATICS under mendh-1.\"),\n \"derivation_fa\": (\"máthēma یونانی (اضافی mathḗmatos) «آنچه آموخته می‌شود، درس، دانش» از ستاکِ ماضیِ math- در \"\n   \"manthánein، صفتِ mathēmatikós «دانش‌دوست، علمی، ریاضی» و مؤنثِ اسم‌شدهٔ mathēmatikḗ (tékhnē) «هنرِ ریاضی» را \"\n   \"پدید آورد؛ این صورت به mathematica لاتین، mathematique فرانسهٔ کهن و mathematik انگلیسیِ میانه (پایانِ سدهٔ \"\n   \"چهاردهم) بدل شد و در دههٔ ۱۵۸۰ با پسوندِ جمعِ -ics به mathematics درآمد (و از آن math در انگلیسیِ آمریکایی \"\n   \"۱۸۹۰ و maths در انگلیسیِ بریتانیایی ۱۹۱۱). کلاین در ص ۹۴۷-۹۴۸ همین زنجیره را می‌آورد و واتکینز نیز \"\n   \"MATHEMATICAL و MATHEMATICS را ذیل mendh-1 ثبت کرده است. ادعای نورایی درست است.\"),\n \"sources\": [E_MATH],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for the English box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. pp. 947-948 s.vv. mathematical, mathematics (KLN_1966.txt leaf NR=509)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mathematical, adj. - Formed with adj. suff. -al fr. F. mathematique, fr. Gk. mathematikos, 'scientific, mathematical', fr. mathema, 'that which is learned, learning, science', from the aorist mathein ... 'to learn'\\\"; \\\"mathematics, n. - F. mathematique, fr. L. mathematica, fr. Gk. mathematike (scil. techne), 'mathematical art'\\\".\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins mendh-1 and index (AHD_watkins1985.txt line 749)\", \"stance\": \"supports\",\n    \"note\": \"\\\"MATHEMATICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH\\\" listed under mendh-1.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat (SKT.txt), grep 'Mathemat'\", \"stance\": \"silent\",\n    \"note\": \"Not retrievable: the OCR of Skeat's M pages is defective in this stretch.\"}\n ]\n})\ndata[\"entries\"].append(e2)\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-332.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk332.py",
 "description": "Write page-332.json"
}
```


### [2026-09-07T16:42:08.898Z] TOOL RESULT

```
written
```


## [2026-09-07T16:42:12.878Z] TOOL CALL #101: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-332.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 332",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-07T16:42:14.267Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 4, 'confirmed': 13, 'disputed': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 3, 'not_checked': 9, 'supports': 13}
books consulted: {'partial': 6, 'supports': 44, 'silent': 8, 'contradicts': 3} | by book: {'KLN': 11, 'POK': 6, 'AHD': 5, 'FSD': 5, 'SKT': 4, 'WLD': 3, 'LAT': 3, 'BQT': 3, 'MON': 3, 'ARY': 3, 'PHD': 3, 'BRT': 3, 'NYB': 3, 'KNT': 2, 'FSF': 2, 'HRN': 1, 'SYN': 1}
```


## [2026-09-07T16:42:38.973Z] AGENT

Done. `verify_check.py 332` reports **0 PROBLEM lines**, 18/18 nodes.

**Page 332 (book p. 302) — 3 entries, 18 nodes**
- Node verdicts: 13 confirmed, 4 plausible, 1 disputed. Root verdicts: 2 confirmed (Men 1, Men-dh), 1 plausible (Manu, Manus).
- Ref checks: 13 supports, 3 partial, 9 not_checked (all 4 MON citations — the 6-vol Farhang is not digitised — plus 5 boxes Nourai leaves unreferenced). 44 supporting `consulted` readings across 17 books.

**disputed**
- *Manu, Manus* #1 Avestan `manu, manuš, mainyuš : man(ly)` — Bartholomae has only "manuš- m. EN. eines alten, vorzeitlichen Helden" (a hero's name) and "manuša- Name eines Bergs"; there is no Avestan noun manu- "man" (that is nar-/maš(y)a-), and mainyuš is mainyu- "spirit" (Watkins men-1: "Avestan mainyu, spirit: AHRIMAN"). Pokorny p.700 himself cites Avestan only "im PN Manuš-ciθra-". The compound manuš-čiθra- and Nourai's second gloss "of Manush race" are correct.

**plausible (with reasons)**
- *Men 1* #1 Greek: Mousa is not derived from bare *men-* by his own sources — Pokorny puts it on p.705 or p.730, Klein p.947 under *men-dh-, Beekes prefers *Mónthia or Pre-Greek; and "matos" is only the bound -matos of automatos.
- *Men 1* #5 Persian: موزه/موزائیک/اتوماتیک come from Fr. musée / mosaïque / automatique, not from musique; and Mo'in's موزه (۱) is the native boot (MP mōzag) — the museum word is موزه (۲), so the superscript is off by one.
- *Men 1* #6 and #8 English: correct root, wrong intermediate — amnesty/maniac/automatic are siblings of the Muse group, and monitor/monster/monument/demonstrate come from monēre (*mon-eye-), not from mēns.
- Root *Manu, Manus*: KLN:930 and POK:700 do say what Nourai writes ("prob. meant orig. 'one who thinks'" / "vielleicht zu men-"), but Mann (IEC) separates *manus "man" from *monus "thoughtful" and Kroonen prefers *(dʰ)ǵʰmon-.

**Extraction errors: none.** I rendered PDF p. 332 and the JSON is faithful throughout (copy at `data/verification/sources/refs/ocr/BOOK/332.png`). Two apparent oddities are the book's own notation, not misreads: `měns` (his breve marks the long vowel, cf. his `Dhě 2` for *dʰeh₁-) and `ma[n]dz-dha` (copied verbatim from Klein p.1095 s.v. Ormazd).

Notable positive finds: BQT:2047 and BQT:2052 land exactly (Mo'in's منوچهر and موسیقی footnotes); KLN:930, 947, 1095 all verified by leaf→page fitting; Dehkhoda states outright that مزغان is "محرف موزیک فرانسوی" with Persian -ān, confirming node #4; Nyberg gives "Av. Manuš.ciθra- ; NP Manūcihr" for node #2. BQT:109 is the ارمز page whose OCR running head reads ۱۰۵ (this scan's leaf→page offset drifts 210–220), the only place in Borhan with the Ahura Mazdā etymology. 18 web pages archived via `fetch_source.py`.
