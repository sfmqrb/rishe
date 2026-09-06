# Verification process log — verify-page-198


## [2026-09-06T02:16:13.253Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 198 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-198.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-198.json. Write /home/sfmqrb/git/rishe/data/verification/page-198.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 198` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:16:14.881Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T02:16:15.591Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:16:15.608Z] TOOL RESULT

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


## [2026-09-06T02:16:16.021Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-198.txt"
}
```


### [2026-09-06T02:16:16.034Z] TOOL RESULT

```
1	=== PDF page 198 (book page 168) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gnô, Gen, Gene 2 : to know  (refs POK:376)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:376; BQT:1298 | zan 2, zânâ 2 : to know ; dan, dânâ : to know
5	  #2 (parent #1) [Persian] refs=BQT; FFD:53 | Zand «زند» : interpretation of the Avesta book ; zandîq «زندیق» : familiar with the Zand book (non-Moslem) ; dânestan «دانستن» : to know ; dân «ـدان» : with knowledge in | extra: دانا ، دانش ؛ سخندان ، کاردان
6	#3 (parent #0) [Old Persian] refs=POK:376; BQT:1298 | xšnâ : to know
7	  #4 (parent #3) [Persian] refs=SPG:216 | šenâxtan «شناختن» : to recognize | extra: آشنا ، شناس
8	#5 (parent #0) [Sanskrit] refs=POK:377 | pra-jan : one who knows in advance, one who has perception, wise ☞Per 1
9	  #6 (parent #5) [Pahlavi] refs=BQT:1459; HRN:181 | farzânak : wise
10	    #7 (parent #6) [Persian] refs=None | Farzâneh «فرزانه» | extra: فرزین
11	#8 (parent #0) [Germanic] refs=AHD | know ; kunnan
12	  #9 (parent #8) [English] refs=None | know ; can
13	#10 (parent #0) [Latin] refs=AHD | gnôcere, nôcere 1 : get to know ; î-gnôrâre : not to know, ignore ☞Ne 1 ; nôbilis : well known ; norma : rule, pattern
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=MON:4704 | normâl «نُرمال» : normal ; not «نُت ، نوت» : a tone ; nobel «نوبل» : noble
16	  #13 (parent #10) [English] refs=None | note ; notify ; notorious ; acquaint ; recognize ; ignore ; noble ; norm ; normal ; abnormal ; enormous
17	#14 (parent #0) [Greek] refs=AHD | gignôskein : to know
18	  #15 (parent #14) [English] refs=AHD:563 | gnosis : intuitive apprehension of spiritual truths ; diagnosis
19	--- entry 1 ---
20	ROOT [Indo-European] Gogel, Gogelos : knob, tapering object  (refs IEC:287)
21	#1 (parent #0) [Persian] refs=IEC:287; MON:3306 | gazar «گَزَر» : carrot
22	#2 (parent #0) [Armenian] refs=IEC:287 | kakği : lime tree (from the fruit shape)
23	--- entry 2 ---
24	ROOT Gogelos -> redirect to Gogel
25	
```


## [2026-09-06T02:16:19.017Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-198.json",
 "description": "Read source JSON page 198"
}
```


### [2026-09-06T02:16:19.090Z] TOOL RESULT

```
{
  "pdf_page": 198,
  "book_page": 168,
  "entries": [
    {
      "root": {
        "name": "Gnô, Gen, Gene 2",
        "lang": "Indo-European",
        "refs": "POK:376",
        "gloss": "to know"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:376; BQT:1298",
          "words": [
            {"translit": "zan 2, zânâ 2", "gloss": "to know", "script": null},
            {"translit": "dan, dânâ", "gloss": "to know", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT; FFD:53",
          "words": [
            {"translit": "Zand", "gloss": "interpretation of the Avesta book", "script": "زند"},
            {"translit": "zandîq", "gloss": "familiar with the Zand book (non-Moslem)", "script": "زندیق"},
            {"translit": "dânestan", "gloss": "to know", "script": "دانستن"},
            {"translit": "dân", "gloss": "with knowledge in", "script": "ـدان"}
          ],
          "script_extra": "دانا ، دانش ؛ سخندان ، کاردان",
          "note": null,
          "quote": {"text": "یکی زردشت وارم آرزویست - که پیشت زند را برخوانم از بر", "poet": "Daqîqî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:376; BQT:1298",
          "words": [
            {"translit": "xšnâ", "gloss": "to know", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "SPG:216",
          "words": [
            {"translit": "šenâxtan", "gloss": "to recognize", "script": "شناختن"}
          ],
          "script_extra": "آشنا ، شناس",
          "note": null,
          "quote": {"text": "یارب بقدر قدر تو نشناختم تو را - درحدّ فکر کوته خود ساختم تو را", "poet": "Vajdî"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:377",
          "words": [
            {"translit": "pra-jan", "gloss": "one who knows in advance, one who has perception, wise", "script": null, "see": ["Per 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "BQT:1459; HRN:181",
          "words": [
            {"translit": "farzânak", "gloss": "wise", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Farzâneh", "gloss": null, "script": "فرزانه"}
          ],
          "script_extra": "فرزین",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "know", "gloss": null, "script": null},
            {"translit": "kunnan", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "know", "gloss": null, "script": null},
            {"translit": "can", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "gnôcere, nôcere 1", "gloss": "get to know", "script": null},
            {"translit": "î-gnôrâre", "gloss": "not to know, ignore", "script": null, "see": ["Ne 1"]},
            {"translit": "nôbilis", "gloss": "well known", "script": null},
            {"translit": "norma", "gloss": "rule, pattern", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:4704",
          "words": [
            {"translit": "normâl", "gloss": "normal", "script": "نُرمال"},
            {"translit": "not", "gloss": "a tone", "script": "نُت ، نوت"},
            {"translit": "nobel", "gloss": "noble", "script": "نوبل"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "note", "gloss": null, "script": null},
            {"translit": "notify", "gloss": null, "script": null},
            {"translit": "notorious", "gloss": null, "script": null},
            {"translit": "acquaint", "gloss": null, "script": null},
            {"translit": "recognize", "gloss": null, "script": null},
            {"translit": "ignore", "gloss": null, "script": null},
            {"translit": "noble", "gloss": null, "script": null},
            {"translit": "norm", "gloss": null, "script": null},
            {"translit": "normal", "gloss": null, "script": null},
            {"translit": "abnormal", "gloss": null, "script": null},
            {"translit": "enormous", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "gignôskein", "gloss": "to know", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD:563",
          "words": [
            {"translit": "gnosis", "gloss": "intuitive apprehension of spiritual truths", "script": null},
            {"translit": "diagnosis", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gogel, Gogelos",
        "lang": "Indo-European",
        "refs": "IEC:287",
        "gloss": "knob, tapering object"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:287; MON:3306",
          "words": [
            {"translit": "gazar", "gloss": "carrot", "script": "گَزَر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Armenian",
          "refs": "IEC:287",
          "words": [
            {"translit": "kakği", "gloss": "lime tree (from the fruit shape)", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gogelos",
        "redirect": "Gogel"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:16:19.362Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:16:19.465Z] TOOL RESULT

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


## [2026-09-06T02:16:24.049Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','FFD','SPG','HRN','AHD','MON','IEC']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:800]); print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T02:16:24.567Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat tools/verify_check.py | head -80",
 "description": "List verification dir and check script"
}
```


### [2026-09-06T02:16:25.839Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/F

SPG {"title": "F. Spiegel - title lost in the bibliography OCR (Table IV no. 93 is missing); Table III lists Spiegel with SPG and ARP. Best guesses: Die altpersischen Keilinschriften (2nd ed. 1881) or Eranische Alterthumskunde (1871-78)", "edition_found": "Die altpersischen Keilinschriften, 2. Aufl. 1881 (downloaded as a guess)", "kind": "archive_djvu", "url": "https://archive.org/details/diealtpersische00spiegoog", "identifier": "diealtpersische00spiegoog (Eranische Alterthumskunde: in.gov.ignca.11987 vol.1, in.ernet.dli.2015.529286 vol.2, in.ernet.dli.2015.103474 vol.3)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SPG_keilinschriften1881.txt", "page_offset": "Keilinschriften 1881: leaf = printed + 11 for the texts, leaf = printed - 29 for the Glossar (e.g. leaf 182 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries ar

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IE
```


### [2026-09-06T02:16:25.888Z] TOOL RESULT

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


## [2026-09-06T02:16:28.123Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 80,200p tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T02:16:28.190Z] TOOL RESULT

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


## [2026-09-06T02:16:29.278Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\n\"",
 "description": "Sample recent verification file"
}
```


### [2026-09-06T02:16:30.898Z] TOOL RESULT

```
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
   "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam'
```


## [2026-09-06T02:17:15.335Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep ĝen- know ===\"\ngrep -n \"erkennen, kennen\" POK_full.txt POK_01.txt POK_02.txt 2>/dev/null | head -20\necho \"=== IEC gogel ===\"\ngrep -n -i \"gogel\" IEC.txt | head -20\necho \"=== IEC gazar ===\"\ngrep -n -i \"gazar\" IEC.txt | head -20",
 "description": "Grep Pokorny and Mann"
}
```


### [2026-09-06T02:17:15.447Z] TOOL RESULT

```
=== POK grep ĝen- know ===
=== IEC gogel ===
6138:&hugh-, &hughno ‘stir, shake, tremble, agi- tate' MHG gugen "rock sway’; gogen ‘rampage’; G cf. Gug, Güge ‘prank’; Gmc. LW in Fr. gogue ‘revelry’ beside gogaille, id. (MHG gogel, gol, adj. ‘wanton; lewd joke’, hence E a-gog :Fr. en gogue; Fris. apparently also gol, gul folly’, but OFr. joli ‘gay’, mod. ‘pretty’ is of doubt- ful association in view of Lat. iovialis and gaudiālis as possible though ambig. back- grounds for this wd.). For type ghughnó, cf. ON gugna ‘tremble’; Blg. zázna, id.
=== IEC gazar ===
4216:gogolos, ios (gog9l-) ‘knob, tapering object Per. gazar ‘carrot; Arm. kakyi (“lime-tree”, fr. the fruit); OS kakeli ‘icicle’?
```


## [2026-09-06T02:17:16.266Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG zan/dan ===\"\ngrep -n \"\\*zanH\\|\\*danH\\|\\*dan\\b\\|to know\" CHEUNG.txt | head -40",
 "description": "Grep Cheung for know verbs"
}
```


### [2026-09-06T02:17:16.353Z] TOOL RESULT

```
=== CHEUNG zan/dan ===
2168:*SOGDIAN: (+ *pati-) BSogd. ptByó-, CSogd. ptbyd- ‘to know, recognize, 
4450:dis-/dist ‘to know, understand, to be able’ 
9762:much’ || (+ *pati-) Oss. D. fzesmarun/£esmard ‘to know, be known; to find out; to 
16985:traverse’ || (+ *pari-) NP parmäsidan ‘to know’ || (+ *fra-) NP farmudan/farmay- ‘to 
26507:*uaid! ‘to know? 
26509:*AVESTAN: vid- (vió-, vaed-, va&ö-) ‘to know’ || (+ *abi-) ‘to proffer’ || (+ *a-) ‘to 
26548:*pati-) SSogd. ptwyó ‘to know’, MSogd. ptwyó ‘to offer, show’ || (+ *ni-) BSogd. 
26558:hear, listen, get to know’ 
26568:«PIE (perf. stem) *uoid- ‘to know’ = LIV: 686 ff. | Pok.: 1125 ff. 
26573:védé, Goth. wait, witum, ON vita, OE witan ‘to know’, Engl. wit, etc. 
26678:[perf.] to know’, Ir. *yaid', *uaid?, as often assumed. 
27678:*PARTHIAN: (+ *fra-) frwd- ‘to be informed; to know, understand’ || (+ *ui-) wywd- 
29768:*us.zazonti by Bartholomae, AIW: 1658 and interpreted as 3р1. SUBJ. ‘they breed’ (*zanH!), but Kellens 
29770:3pl. IND. (*zanH’). 
30019:*zanH! ‘to give birth; (pass.) to be born’ 
30026:*zanHl 465 
30081:466 *zanH2 
30113:*zanHË ‘to know’ 
30115:*AVESTAN: zan- ‘to know’ || (+ *aua-) ‘to perceive, recognize’ || (+ *pati-) ‘to 
30116:recognize’ || (+ *fra-) ‘to learn, get to know’ = Liste: 67 
30123:*OLD PERSIAN: Х$па- (inch.) ‘to know’ = Kent: 182 
30128:*MIDDLE PERSIAN: MMP ‘sn’s-, BMP sn’s- /Snas-/ (inch.) ‘to recognize, get to know, 
30129:(re)connaitre’, MMP d’n-, BMP d’n- (YD'YTN-) /аап-/ ‘to know, savoir’ || (+ *a-) 
30140:*PARTHIAN: ‘Sn’s- (inch.) ‘to recognize, get to know, (re)connaitre’, z’n- ‘to know, 
30145:*zanH2 467 
30156:*SOGDIAN: BSogd. zn’kh ‘knowledge, уйапа' || (+ *a-) SSogd. "ein ‘to know, 
30179:nas-, Zaz. паѕ-, Awrom. aznasay/aznas- ‘to know, recognize’, Gil. (Rsht.) -snast-/ 
30181:Snàs- (inch.) ‘to get to know, recognize’, NP danistan/dan-, Bal. zan-/zant, Kurd. 
30186:zonaj-/zon-, Qohr. zünada/zün-, Semn. -zün- ‘to know’, Sang. -zunäj-/zun-, Soi 
30187:zünà-/zün-, Sorkh. (1sg.) me-zon-cem, (neg.) nä-zoen, Lasg. (1sg.) zæjn ‘to know; to 
30190:*NEIR: Oss. I. zonyn/zynd, D. zonun/zund ‘to know, be able’, (intr./pass. *-ja-) I. 
30192:vazan-/vazed- ‘to know’ || (+ *aua-) Sh. wiztin-/wizént, Rosh. wizön-/wizint, Sariq. 
30193:wazon-/wazond, Yzgh. vozan- ‘to know, recognize’ || (+ “*pati-) Pash. 
30202:*MISC: (+ *pati-) Orm. pazän-, pazen- ‘to know, recognize’ = pazan-/pazanok ‘to 
30203:understand’, pazan- ‘to know’ 
30205:*SANSKRIT: jfid ‘to know, recognize, understand’ (RV+) = EWAia I: 601 
30212:know’, Arm. canea- / cani- ‘to recognize’, Goth. kunnan, OHG kunnan ‘to know, to 
30215:be able’, Engl. to know, etc. 
55324:*grabH (s.v.), *uat, *zanH? 
55337:(s.v.), Som (s.v.), *zanH?
```


## [2026-09-06T02:17:23.095Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30110,30235p' CHEUNG.txt",
 "description": "Read Cheung zanH2 entry"
}
```


### [2026-09-06T02:17:23.147Z] TOOL RESULT

```
210; Lecoq 2002: 125; Shahbakhsh: s.v. za(h)-Korn 2005: 109 f., 379 (passim) 


*zanHË ‘to know’ 

*AVESTAN: zan- ‘to know’ || (+ *aua-) ‘to perceive, recognize’ || (+ *pati-) ‘to 
recognize’ || (+ *fra-) ‘to learn, get to know’ = Liste: 67 

Pres. {1} na-: IND. 3pl. YAv. paiti.zanonti (Yt 13.46), ІМРУ. 2р1. OAV. paiti.zanata (Y 29.11); Pres. {2} 
them. па-: IND. 3sg. YAv. frazänaiti (F 278, FrK 18 ff.), SUBJ. 3sg. YAv. paiti.zanat (Yt 13.50), 3pl. 
YAv. auuazanan (У 6.45); Partic.: pres. desid. YAv. zixsnanhomna- (Yt 13.49, Yt 13.73), perf. pass. 
Y Av. paiti.zanta- (Y 57.14, Y 57.34, Yt 8.34, etc.) 

*OLD PERSIAN: Х$па- (inch.) ‘to know’ = Kent: 182 

Pres. {1} inch.: SUBJ. 2sg. xsnäsähy <x-S-n-a-s-a-h-y> (DNa 42), 3sg. xsnasatiy <x-S-n-a-s-a-t-i-y> (DB 
1.52); Pres. {2} na-: impf. IND. 3sg. adana <a-d-a-n-a> (DB 1.51), <[a]-d-a-n-a> DSq 3) 

*MIDDLE PERSIAN: MMP ‘sn’s-, BMP sn’s- /Snas-/ (inch.) ‘to recognize, get to know, 
(re)connaitre’, MMP d’n-, BMP d’n- (YD'YTN-) /аап-/ ‘to know, savoir’ || (+ *a-) 
MMP "zynd, ’’znd ‘story’ (LW) = DMMPP: 93b, 134b f., 85b 

Well attested: Inch.: pres. IND. 1sg. BMP ёп em /Snasam/, šn’sym /Snasém/, 3sg. MMP ‘sn’syd, BMP 
Sn’syt /Snaséd/, 3р1. MMP *'sn'synd, BMP sn'synd /snäsönd/, SUBJ. 3р1. MMP ‘sn’s’nd, etc.; Pres.: IND. 
1sg. MMP d’nym, 25р. BMP d’nyh /danéh/, 3sg. MMP d’nyd, 3р1. MMP d’nynd, etc. 


сх? 


*PARTHIAN: ‘Sn’s- (inch.) ‘to recognize, get to know, (re)connaitre’, z’n- ‘to know, 
savoir || (+ *а-) "zynd, "znd ‘story’ || (+ *fra-) frz’ng ‘wise’ = Ghilain: 82, 84 | 
DMMPP: 93b, 379b f., 85b, 161a 


*zanH2 467 


Well attested: Inch.: pres. IND. 3sg. “Sn’syd, 3р1. ‘Sn’synd, SUBJ. 3sg. ‘Sn’s’h, IMPV. 2pl. ‘sn’syd; Pres.: 
IND. 1sg. z’n’m, 2sg. z’nyh, 3sg. z’nyd, etc. 

*KHOTANESE: ysän- ‘to shine’ || (+ *aua-) OKh. уауѕап- ‘to recognize’ || (+ *pati-) 
paysän- ‘to recognize’ || (+ *fra-) OKh. haysan- ‘to be aware’ || (+ *ui-) OKh. 
biysen- (biyan-) ‘to wake up’, OKh. biysañ- (caus.) ‘to waken? = SGS: 112, 119, 
71, 148 

*SOGDIAN: BSogd. zn’kh ‘knowledge, уйапа' || (+ *a-) SSogd. "ein ‘to know, 
recognize’, SSogd. "z'nt, BSogd. "z'nt, CSogd. "zynt, MSogd. '(")z(y)nd, MSogd. 
"z'nt ‘tale, parable’ || (+ *pati-) SSogd. ptz’n, BSogd. ptz’(’)n, CSogd. ptz’n, 
MSogd. ptz’n ‘to recognize’ || (+ *fra-) MSogd. ”fn’s ‘to recognize’ || (+ *ham-) 
SSogd. nz’n ‘to declare’, BSogd. ’nz’n, CSogd. ’z’n ‘to acknowledge, confess, give 
thanks’, CSogd. ’z’n ‘confession, acknowledgement, thanksgiving’ 

(+ *а-) Pres.: IMPV. 25р. SSogd. "z'n || (+ *pati-) Pres.: IND. 2sg. MSogd. ptz’n’y, 3sg. BSogd. ptz’’nt, 
Impf.: IND. 159. CSogd. ptyz’nw, MSogd. ptyz’nww, 3sg. BSogd. pt’yz’n, 3р1. BSogd. pt’yz’n’nt, 
BSogd. pt’yzn’nt; Fut.: IND. 3pl. BSogd. ptz’nt k’m, SUBJ. 3pl. SSogd. ptz’nt k'm || (+ *fra-) Impf.: 
IND. 3sg. MSogd. "f’sn’s || (+ *ham-) Pres.: SUBJ. 3sg. BSogd. ’nz’n’t, POT.-SUBJ. 3sg. BSogd. ’nz’n’t 
wn’’t, Impf.: IND. 15р. SSogd. mnz’nw, MSogd. mnz’nw (BBB: 36), 3sg. CSogd. mz’n; Fut.: IND. 15р. 
CSogd. ’z’nnq’, 3sg. CSogd. ’z’ntq’; Partic.: pres. CSogd. ’zn’nyt (pl.) ‘confessors’; Inf.: BSogd. ’nz’n’y, 
BSogd. ’nz’’n’y 

*CHORESMIAN: m/n’s- ‘to become acquainted, accustomed’, (caus.) m/n’sy- ‘to 
acquaint’ (n = [nn] < *zn- ?, rather than *xsn-, MacKenzie IV: 532) || (+ *apa-) 
bn’sy- ‘to wean’ (< *‘to disaccustom’, MacKenzie I: 532) || (+ *ham-) m/nc’n- ‘to 
acknowledge, admit’ > Samadi: 115, 22, 35, 119 

*BACTRIAN: Cav- ‘to acknowledge, (bear) witness" = S-W, Bact.: 191b 

*NWIR: Widely attested: NP Sinaxtan/Sinas- ‘to recognize, distinguish’, Kurd. näsin/ 
nas-, Zaz. паѕ-, Awrom. aznasay/aznas- ‘to know, recognize’, Gil. (Rsht.) -snast-/ 
Senas-, Khuns. iSnäs-, esnas-/isnayt, i$nasa, Mah. -isnas-, Qohr. esnasada/esnas-, Siv. 
Snàs- (inch.) ‘to get to know, recognize’, NP danistan/dan-, Bal. zan-/zant, Kurd. 
zanin/zan-, Zaz. zanayis/zan-, Tt. (Esh.) zun/zund, Anar. -izono/ezon-, Awrom. 
zanay/-zan-, Fariz. zonást-/zon-, Yar. zönäj-/zön-, Gz. zün-/zünast, (LW) Gil. (Rsht.) 
dänestzn/dän-, Gur. (Kand) zäna-/-zän-, Ham. zunayän/zun-, Isfah. zunän/zun-, 
Khuns. zün-/zünä, Mah. zön-, Meim. zu:näj-/a-zun-, Nn. zuna/zön-/zun-, Natan. 
zonaj-/zon-, Qohr. zünada/zün-, Semn. -zün- ‘to know’, Sang. -zunäj-/zun-, Soi 
zünà-/zün-, Sorkh. (1sg.) me-zon-cem, (neg.) nä-zoen, Lasg. (1sg.) zæjn ‘to know; to 
be able’ 

*NEIR: Oss. I. zonyn/zynd, D. zonun/zund ‘to know, be able’, (intr./pass. *-ja-) I. 
zynyn/zynd, D. zinnun/zind ‘to be seen, appear’ || (+ *abi- ?) Yi. vozan-/vozad-, M. 
vazan-/vazed- ‘to know’ || (+ *aua-) Sh. wiztin-/wizént, Rosh. wizön-/wizint, Sariq. 
wazon-/wazond, Yzgh. vozan- ‘to know, recognize’ || (+ “*pati-) Pash. 


468 *zanj 


peZan-/p&Zand-, (?) Yghn. bizön-, bézón-, bizon-/bizonta (diff. prev. ?), Sariq. 
pajan-/pajand, Wa. pazdan- ‘to recognize’ 

*MISC: (+ *pati-) Orm. pazän-, pazen- ‘to know, recognize’ = pazan-/pazanok ‘to 
understand’, pazan- ‘to know’ 

*SANSKRIT: jfid ‘to know, recognize, understand’ (RV+) = EWAia I: 601 

© This root has an impeccable IE etymology. 

«PIE *éneH;- ‘to recognize, know’ = LIV: 168 ff. | Pok.: 376 ff. 

*IE COGNATES: Gr. yıyvookoa ‘I recognize’, Lat. noscere, OCS znati, Lith. Zinöti ‘to 
know’, Arm. canea- / cani- ‘to recognize’, Goth. kunnan, OHG kunnan ‘to know, to 


be able’, Engl. to know, etc. 

*REFERENCES: КРЕ I: 82b, 81a, 139a f., 206b, 245b; Ivanow 1926: 420; EVP: 63, 105; IIFL I: 405b; 
Christensen, Contributions I: 69, 64, 161, 259; Christensen, Contributions II: 52, 55, 114; KPF II: 197 f.; 
IIFL П: 260b; Abrahamian 1936: 125, 135; Lambton 1938: 42a; Andreev — Реёќегеуа: 232a; MacKenzie 
1966: 89, 114; Yarshater 1969: 183; EVS: 96a, 55b; WIM I: 69, 74; DKS: 214; WIM II/1: 86; Blau 1980: 
281; WIM III: 117; Omar 1992: 702a; Abaev, Slovar' IV: 315, 323; Cabolov 1997: 73; Werba 1997: 403 
f; Paul 1998: 306b, 320a; Steblin-Kamenskij 1999: 458; Cheung 2002: 255; Lecoq 2002: 121, etc.; 
NEVP: 68; Kiefer 2003: 205; Shahbakhsh: s.v. zan-; Korn 2005: 37, 88, 379 (passim) 


*Zanj ‘to seize’ 

*KHOTANESE: (+ ш-) LKh. biysamj- ‘to take hold of = SGS: 97 

*NEIR: Sangl. zenz-, zenj-/zuyd, Ishk. zänz-/zöyd ‘to seize, catch, lift up, take on 
one's back’ 

9 The root may not be Plr., considering its limited distribution.
```


## [2026-09-06T02:17:25.282Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=data.split('\\n')\n# find leaf index of line 4216\nidx=sum(len(l)+1 for l in lines[:4215])\nleaf=data[:idx].count('\\f')\nprint('leaf(0-based)',leaf, 'approx printed page', (leaf-15)*2)\nprint(data.split('\\f')[leaf][:1500])\nEOF",
 "description": "Locate IEC gogolos page"
}
```


### [2026-09-06T02:17:27.054Z] TOOL RESULT

```
leaf(0-based) 171 approx printed page 312
(dump of Dr, fr. *gogio); Sw. koka ‘clod’; Li. gáoga *trunch- eon’, guogas ‘Mariampol Lithuanian; yokel'; guoge ‘knob; head; duffer'; Blg. cf. proper n. Gago
gogolos, ios (gog9l-) ‘knob, tapering object Per. gazar ‘carrot; Arm. kakyi (“lime-tree”, fr. the fruit); OS kakeli ‘icicle’?
goig- (1) bend, twist Gaelic gaog ‘knot in yarn’; ON keikja “bend back’; Li. gieZiü, ^ti, v. (2) “plot. (Isophonic: Icel. keikur 'erect)
goiĝ- (2) ‘mordant, piercing; stab, bite’. Cf.
giĝ- Arm. kajcu, gs kajcvi ‘thistle’ beside z-gde kic ‘sting’, kcu ‘sour, sharp’; Pol. giez ‘botfly’; Li. gaiZüs ‘sour; irascible’; geän, ^ti (1) *tch?
golios, see goios
goios, goiios “lock, keep, lock-up, depository, hold’. Cf. WP I, 527, 677 Skt. gayah “house, family; OE cég, cége ‘key’; OFris. ka kei, id., beside keia, v. *pro- tect’; OCS goj ‘peace’ beside (*-0-) gaj ‘grove, copse’, Pol. gaj, Cz. háj, cf. Cz. hájit “protect and OR iz-gój (fey, outlawed’ or sim.); LW in Li. gojus ‘grove’. (Du. kooj ‘cage’ is a LW fr. Lat. cavea)
golətis (golt-) “chill, cold, frost’. cf. gel-, geldios, golos MHG kelte, id.; OCS goloti “ice”
(golg-, see gelg-. O-gde in OCS *glazü “eye” in glaz-atü ‘eyed’; R glaz, pl. glazà, id. The sense of Cypriot Gólgoi ‘temple of Cupid and Venus’ is not clear. Isophonic: Sw. kälke “iron shoe, glide")
golos, à, is, io ‘neck, throat, gullet’. Cf. WP I, 621 & 682 Skt. galah; Arm. cf. koy-koyit ‘epiglottis’, koykoyim ‘groan’; Lat. gola, gula; MIr. & Ir. goile; (e-gde in) MHG kel kéle; WG cf. Kall 'ro
```


## [2026-09-06T02:17:37.522Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(166,177):\n    t=leaves[i]\n    nums=re.findall(r'\\b\\d{2,4}\\b', t[:200]+' || '+t[-200:])\n    print(i, repr(t[:80]), '...', repr(t[-80:]))\nEOF",
 "description": "Inspect IEC leaves near gogolos"
}
```


### [2026-09-06T02:17:39.273Z] TOOL RESULT

```
166 '� ‘stick; be sticky, adhere’. WP I, 619. Sce next Olr. glenaim, Ir. gleanaim; W ' ... '’; G kleimen and (fr LG) klehmen, LG kleemen “stick, lime, glue, daub’; Kiem ‘da'
167 'ub, mud’; OE clæman ‘to smear’; clam ‘daub’; ON kleima,\ngliu- (glou-) ]— glomor-' ... 'ud- ‘compact; ball, lump, huddle’. WP I, 618 MHG kloz “lump, stump, gag; OFris. '
168 'klāt ‘Jump’; Du. kloot ‘ball, testis; Blg. glužd (“not in wood, fr. *eloudio); (' ... 'džioju ‘loaf, idle\nglunk- ‘group, cluster’ Norw. klynge, id.; G cf. Klüngel ‘gan'
169 'g, group; ball of (bread: Cz. s-hluk, dim. hloucek ‘group, gang’\nglüt- (1) ‘guip' ... '. knipa, id.; Fris. cf. knyp-taünge ‘pincers’; (*i- in) LG knippen, s. id.; Du. '
170 'cf. knippen ‘snip’; Li. gnýbu, -ti, v. ‘pinch’; gnjbis, m. id. beside *gnib- in ' ... 'lb. Gogë, mf. Albanian of Rumania’; OHG kuocho ‘cake’; Du. koek, id.; EME keech '
171 '(dump of Dr, fr. *gogio); Sw. koka ‘clod’; Li. gáoga *trunch- eon’, guogas ‘Mari' ... 'ho?) in Skt. garhami; MHG\n289\nkargen, etc. See gargh-. Isophonic w. Li. gargu, e'
172 'ti ‘get grimy’. (Skt. garha ‘abuse’: MHG karc, -ges)\ngorgo, io (1) ‘seize, snatc' ... '. grāquos, gragəl- and next. Lat. graculus ‘jackdaw, chough, jay’; Br. grakal ‘c'
173 "roak; chatter, scrape’ beside gragal'a ‘chatter, as jay or magpie’; OHG kragil, " ... 'g dock); G krauen, Du. krauwen ‘scrape, scratch, graze’ here, or: Hom. grápho, i'
174 'd. qua *graguho?)\ngreg- ‘erode; erosion’ (?) W grai, pl. greioedd ‘blight’; R gr' ... ' cf. grebeni, gs. grebene: Cz. hřeben, where the vowel is Sei\ngrido (grid-, groi'
175 "d-) “cry, scream’. See next Lat. (ambig.) rideo (laugh', prob. < *righid-); Gall" ... 'm (“chattels?, but MHG kram “tent, shop, goods’ of uncertain origin); OCS cf. gr'
176 'omada ‘pile’, grominica ‘shop’\ngrom- (2) ‘waste, rubbish, triviality, decline’ O' ... ': shaft of cart\ngrou?- “crush, grind; ground, gravel, grit? W cf. grual (gruel, '
```


## [2026-09-06T02:17:49.477Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(168,175):\n    t=leaves[i]\n    print(i, re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', t))\nEOF",
 "description": "Find printed page markers in IEC leaves"
}
```


### [2026-09-06T02:17:51.098Z] TOOL RESULT

```
168 ['10', '20', '25', '30', '35', '40', '45', '282', '283']
169 ['20', '25', '30', '35', '40', '45', '284', '285']
170 ['15', '20', '25', '30', '35', '40', '45', '286', '287']
171 ['20', '25', '30', '35', '40', '45', '288', '289']
172 ['15', '20', '25', '30', '35', '40', '45', '290']
173 ['291', '10', '20', '25', '30', '35', '40', '292']
174 ['293', '15', '20', '25', '30', '35', '40', '45', '294']
```


## [2026-09-06T02:17:57.422Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('IEC.txt',encoding='utf-8',errors='replace').read()\nt=data.split('\\f')[171]\ni288=t.find('\\n288\\n'); ig=t.find('gogolos'); i289=t.find('\\n289\\n')\nprint('288 at',i288,'gogolos at',ig,'289 at',i289,'len',len(t))\nprint(t[max(0,i288-300):i288+200])\nEOF",
 "description": "Position of page markers vs gogolos"
}
```


### [2026-09-06T02:17:59.233Z] TOOL RESULT

```
288 at 1593 gogolos at 158 289 at 3446 len 3501
glide")
golos, à, is, io ‘neck, throat, gullet’. Cf. WP I, 621 & 682 Skt. galah; Arm. cf. koy-koyit ‘epiglottis’, koykoyim ‘groan’; Lat. gola, gula; MIr. & Ir. goile; (e-gde in) MHG kel kéle; WG cf. Kall 'roof-gutter. (Per. galü, gulü is fr. a type
gógos, à, iə — gorgho (gargho?)
20
25
30
35
40
45
 
288
gurgot-, q. v.)
(golos (2), -es- ‘congealed mass; ice, snow” in OE cealer ‘curd cheese’. Cf. gel-, geldios, golotis. Verbal type: OE calan, ON kala “chill? Cf. also ON kal, n. *frostbite?)
gong-
```


## [2026-09-06T02:18:07.829Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kennen\\b\" POK_01.txt | head -30\necho \"=== leaf for p376: POK_01 leaf = p+8 => 384 ===\"\npython3 - <<'EOF'\ndata=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint(len(leaves))\nfor i in (383,384,385):\n    print('---LEAF',i,'---')\n    print(leaves[i][:2500])\nEOF",
 "description": "Read Pokorny p.376 area"
}
```


### [2026-09-06T02:18:09.735Z] TOOL RESULT

```
Exit code 1
1046:Falk-Torp  1407  reiht  auch  an:  ahd.  öcZi,  as.  öthlj  ags.  Adj.  lepe,  Adv. eape  ,leicht,  bequem',  ahd.  ödmuotij  as.  öthmödi  ,demütig',  ags.  eapmöd ,demütig',  anord.  audmjükr  ,leicht  zu  bewegen,  willig,  demütig',  audkendr ,leicht  zu  erkennen';  Gdbed.  sei  ,willig',  woraus  ,leicht  zu  machen'; formell  germ.  ^o-Partizip-Bildung  zu  aivi-  (Vorbild  germ.  aupia-  ,öde'?). Recht  unsicher.
1873:Neben  der  sehr  fruchtbaren  Wzf.  bbereu-  (s.  dort)  ist  wohl  auch bh{e)rei-,  bh(e)ri-  anzuerkennen.  Auf  diese  kann  bezogen  werden  ai. jar-bhurl-ti,  gr.  *q)VQi-(x),  *7tOQ(pvQi-(o  (s.  oben);  mit  xn -Formantien  vermut- lich gr.  (pQL^dcj,  q)Qi^daao(xat  , bewege  mich  unruhig,  springe,  schnaube*; aisl.  brimi  ,Feuer';  mengl.  brlm  ,Glut*,  wahrscheinlich  auch  aisl.  biim  n. , Brandung',  ags.  hnm  n.  ,Meer,  See*;  die  in  brühen,  Brodem,  braten  yot- liegende  Bedeutungsfärbung  kehrt  wieder  in  norw.  prim  ,eine  Art  aus saurem  Molken  unter  starkem  Kochen  bereiteter  Käse*  (auch  nhd.  Brimsen- käse), mdartl.  auch  bi'lm  ,ds.;  auch  Kruste,  Bodensatz  einer  eingekochten Flüssigkeit*  (nbd.  bair.  Brimsen,  Brinzen  ,was  sich  beim  Mus  angebräunt an  der  Pfanne  festsetzt');  daneben  mit  formantischem  -uo-  sehr  wahr- scheinlich abd.  brio,  mbd.  brl(e),  ags.  briw  ,Brei'  (als  ,*Sud,  Gekochtes'), briwan  , kochen*;  hierzu  auch  mir.  breo  ,Flamme*  (*bhri-uo-).
2128:bheudh-,    nasal,    bhu-n-dh-    ,wach    sein,    wecken,    beobachten;    geweckt, geistig   rege,   aufmerksam   sein,  erkennen,   oder  andere   dazu    veran- lassen (aufpassen  machen,  kundtun,  gebieten;  darbieten)'. Themat.  Präs.  in  ai.  bödhati,  bödhate  , erwacht,  erweckt,  ist  wach,  merkt, wird    gewahr',    av.    baodaiti    ,nimmt   wahr',    mit  paiti-  ,sein   Augenmerk worauf  richten'  (=  gr.  7tsvd^o(.iaij  germ.  *biudan,    abg.    bljudg);    Aor.    ai. bhuddnta  (=  invd-ovTo),  Perf.  bubödlia,  bubndhimd  (:  germ.  *baud,  *budurn), Partiz.  buddhd-  , er  wacht,  verständig;  erkannt'  (=  gr.  ä-nvarog  ,unkundig; unbekannt'),    buddhi-    f.    , Einsicht,  Verstand,    Meinung,    Absicht'    (=  av. paiti-busti-    f.    ,das    Bemerken',    gr.  nvotig    ,das    Nachforschen,    Fragen; Kunde,  Nachricht');  Kausativ  in  ai.  5öc^M7/a<i  , er  weckt;  belehrt,  teilt  mit', av.    baodayeiti   ,bemerkt,    fühlt'  (=  abg.    buzdg,    buditi,   lit.  pasibaudyti)] Zustandsverb  in  ai.  budhydte  ,erwacht,  wird  gewahr;  erkennt',  av.  buiöyeiti
2138:got.  anabiudan  , befehlen,  anordnen',  faurbiudan  , verbieten',  aisl.  bjöda , bieten,  anbieten,  zu  erkennen  geben',  ags.  beodauj  as.  biodan^  ahd.  biotan , bieten,  darbieten',  nhd.  bieten,  gebieterij  verbieten,  Gebiet,  eigentl.  , Befehls- bereich'; aisl.  bod  n.,  ags.  gebod  n.,  mhd.  bot  n.  , Gebot',  ahd.  usw.  boto ,Bote',  ahd.  butil  (nhd.  Büttel),  ags.  bydel  ,Bote, .  Gerichtsdiener';  got. biups,  -dis  jTisch',  aisl.  bjödr,  ags.  beod,  ahd.  beot,  piot  ,Tisch;  Schüssel', eig.  , worauf  angeboten  wird,  Servierbrett'  (dazu  auch  ahd.  biutta,  nhd. Beute  , Backtrog,  Bienenkorb').
2620:lat.  dum  (*dom)  ,noch*,  als  Konj.  , während,  indes,  indem',  ursprgl.  de- monstratives ,dann',  vgl.  etiam-dum,  interdum,  nöndum,  agedum  (:  gr.  äye 6rj),  manedum,  quidum  ,wie  so?'  u.  dgl.,  dann  in  relativ-konjunktioneller Bed.,  wie  auch  in  diimmodo,  dumne,  dumtaxat)  osk.  isidum  ,ldem*  ist aber  in  is-id-um  zu  zerlegen,  wie  auch  in  lat.  idemj  quidem,  tandem^ tantusdem,  totidem  kein  mit  dum  aus  *dom  ablautendes  -dem  anzuerkennen ist;  id-em  aus  *id-em  =  ai.  id-dm  ,eben  dieses',  vgl.  osk.  is-id-um,  wie quid-em  aus  *quid-om  =  osk.  pid-um,  und  infolge  der  Silbentrennung i-dem  wurde  -dem  als  Identitätspartikel  gefühlt  und  wucherte  weiter);
4975:Inwieweit  die  von  Persson  Beitr.  666,  773,  839  f.  als  Erweiterungen unseres  *er(9)-  betrachteten  Wurzeln  re-d-  ,scharren',  rei-,  reu-  ,auf reißen' ihr  wirklich  entstammen,  ist  fraglich;  die  bei  *er(a)-  besonders  ausgeprägte Bedeutung  des  lockern,  undichten,  auseinanderstehenden  lassen  sie  ganz vermissen  oder  wenigstens  nicht  als  herrschende  Bedeutung  erkennen.
=== leaf for p376: POK_01 leaf = p+8 => 384 ===
364
---LEAF 383 ---
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
IndexError: list index out of range
```


## [2026-09-06T02:18:14.384Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('nleaves',len(leaves))\nfor i in (31,32,33,34):\n    print('=== LEAF',i,'===')\n    print(leaves[i][:3000])\nEOF",
 "description": "Read POK_02 leaves for p.376"
}
```


### [2026-09-06T02:18:15.943Z] TOOL RESULT

```
nleaves 434
=== LEAF 31 ===
ruti filiuSj  ogom  Gen.  Coimagnij  ir.  Coim-än;  gall.  Ate-gnia]  gr.  dfiöyvLog  ,von gleicher  Abstammung';  über  kypr.  Ivig  ,Kind'  (kaum  *ev-yvig)  vgl.  Schwyzer Gr.  Gr.  I  4503;
*gn-io-  (wozu  obiges  -gnio-  weitere  Schwächung)  in  lat.  genius  ,der Schutzgeist  (des  Mannes)',  ursprüngl.  die  personifizierte  Zeugungskraft (allenfalls  hochstufiges  *gen-ios),  got.  kuni  {^gn-io-m),  ahd.  (usw.)  chunni , Geschlecht',  vgl.  got.  sama-kunjans  Akk.  PI.  , desselben  Geschlechtes'  :  gr. ^f.iö-yvLog]  Isit.  progenies  ,Nachkommenschaft',  air.  gein  {^genen  <i*gen-n) ,Geburt',  ags.  cyne-  in  Kompos.  ,königlich',  anord.  konr  ,Sohn,  edelge- borener  Mann'  (germ.  "^kuninga-z  in  ahd.  usw.  kuning  ,König',  d.  i.  ,einem edlen  Geschlechte  angehörig,  ihm  entsprossen').
gn-  in  ai.  jä-s  ,Nachkomme',  pra-jä  , Nachkommenschaft',  jäs-patis ,Familienvater'  (Meillet  MSL.  10,  139);
über  lat.  ingenuus  ,freibürtig',  genulnus  ,echt'  s.  WH.  I  593  f.
WP.  I  576  ff.,  WH.  I  590 £f.,  597  ff.,  868,  Trautmann  370,  Meillet  Cin- quantenaire  172  ff.
376  t
2.  ien-,  genQ-,  gne-,  gno-  .erkennen,  kennen^;  Nominalbildungen:  geziQ^tlQ^ ..Kennzeichen^  gnö-mn   ds..  gno-ter-  .Kenner',  gnö-ti-  .Erkenntnia' gnö'to-s  (?)  .bekannt',  g^-tö-s  ds.;  zur  Vermeidung  der  Homonyi^i^ mit  1.  gen-  werden  vielfach  Verbalformen  mit  gnö-  verwendet.
Ai.  jänämi  .ich  weiß',  anu-jüä-  .zugestehen,  gewähren',  av.  paiti-zändnn
..sie  nehmen  sich  jemandes  an'  (themat.  2.  PL  paiti-zänatä  .ihr  erkennt  aiL
nehmt  auf),  apers.  3.  Sg.  Impf,  a-dänä  .er  wußte'  (idg.  *gn-nä-mi,  daneben
enklit.    *§n-nämi  in:)    av.   zanä-t,   zanqn,    afghan.  pe-zanl    .unterscheidet,
erkennt';  w
arm.  Aor.  caneay  .ich  erkannte'  (an-can  .unbekannt')  unsicherer  Grund-  ' form  (zum  Präs.  *gn-nä-'mi?  oder  aus  *^eW-?  wie:)  canaut''  .bekannt';
air.  itar-gninim,  asa-gninaim  .sapio'  (Fut.  -gena  aus  *ge-gnä-,  Perf, ad-gen-sa  .cognovi.  cognosco'  aus  "^ge-gn-;  am  Präsensstamm  gnin-  ist  der Vok.  noch  ungeklärt;  vgl.  Pokorny  IF.  35.  338 f..  Marstrander  Pros, nas.  23);
got.  kunnan  .kennen,  wissen'  {kann,  Prät.  kunpa-,  Ausgangspunkt  die schwundstuf.  Pluralformen  kunnum,  kunnun  aus  *gn-nd-mes) ;  daneben schwaches  Verb  ana-kunnan  .erkennen'  usw.  =  ahd.  kunnen  ,noscere, temptare'  (schon  urgerm..  Wissmann  Nom.  postverb.  146 f.);  daneben hochstufiges  ön-Verb  anord.  kanna  .untersuchen';
ahd.  (usw.)  starkes  Verb,  kunnan  (kann)  .wissen,  können'  (in  den  älteren Sprachzeiten  nur  von  geistigem  können  =  kennen.  Gegensatz  zu  mögen)] dazu  das  Kaus.  got.  kannjan  (*gon-)  .bekanntmachen,  kundtun',  ags.  cennan .benachrichtigen,  erklären,  zuschreiben',  ahd.  ar-kennen  .erken
=== LEAF 32 ===
nen',  hi- kennen  .bekennen',  nhd.  kennen.
lit.  Hnau,  Hnöti,  lett.  zindt  .wissen'  (zino  =  *^«w-.  danach  PL  Binome, Inf.  zinöti,  Partiz.  zinötas)  =  apr.  posinna  .ich  bekenne'  (Inf.  posinnatj Partiz.  posinnäts),  ersinnat  .erkennen';
s^o-Präs.  apers.  (Konj.)  xsnäsätiy  .er  soll  erkennen';  gr.  yiyvwayco),  epir. yv(b(Ty.(ü  .erkenne',  lat.  nösco  (gndsco)  .erkenne',  ignösco  .habe  ein  Ein- sehen, verzeihe'  (vgl.  ai.  anu-jnä-)-^  alb.  njoh  .ich  kenne'  {*gne-skö] 2.  3.  Sg.  njeh  durch  Umlaut) ;  s.  auch  unten  lit.  pa^stu ;
Perf  .3ii.  jajnäu,  lat.  növi,  ags.  cneoio  (cnäwan)  .erkannte';  gr.  Aor.  e-yvioVy ai.  Opt.  jnä-yät]  gr.  yeycjva  >bin  vernehmlich,  sage'  (auch  formell  zum Präs.  geworden  yeycjvsü}  ds..  ysyumaxü))',
dazu  das  lo-Präs.  ai.  jüäydte  (Pass.  zu  jänäti),  ahd.  knäu  (ir-,  hi-,  int-) .erkenne'   {^gne-io),   ags.  cnäwan   (engl,  know)    ds.    (zum  w   vgl.  lat.  növl, ai.  jajnäu),  mit  ahd.  urknät  .Erkenntnis',  und   aksl.  znajq,  znati  .kennen, •     wissen'  (*^nö-iö);
Desid.  ai.  jijnäsatij  av.  zixsnäidhdmnä  .die  erkundigen  Wollenden';   lit.
377
pazfstu,  -^inaü,  Bnti  ^kennen'';  nach  Leumann  IF.  58,  118  aus  *gn-skö herzuleiten;  anders  Persson  Beitr.  341;
Kaus.  ai.  jnäpayati  (die  p-Fovm  wäre  alt,  wenn  Charpentier  IF.  25,  243 mit  Recht  arm.  canaut"^  , bekannt',  i-St.  =  ai.  jnapti-h  ^Erkenntnis, Kunde'  setzt) ;  aber  jfiapta-  vielmehr  retograd  aus  kausat.  jnäpita-,  IF. 57,  226  f.
to-Partiz.  gnö-tö-s  (hat  vielleicht  das  ö  sekundär  von  den  Verbalformen bezogen):  ai.  jnätd-h  ,bekannt',  gr.  yvwrög  (jünger  yywöTOc;)  ds.  (dyvcbg, -wTog  ,unbekannt'),  lat.  nötus,  air.  gnäth  ,o-ewohnt,  bekannt'  (cymr. gnawd  , Gewohnheit' ;  dazu  cymr.  gnaws,  naws  ,Natur',  bret.  neuz  ,Aus- sehen',  als  brit.  Lw.  air.  nös  ,Sitte*),  gall.  KaTov-yvärog,  Epo-so-gnätus , ai.  ajnäta-j  äyvwTog,  ignötus  ,unbekannt',  air.  ingnad  ,fremd';  daneben *gnÖ-tö-s  (Umfärbung  von  *gnd-tös  nach  gnö-?)  in  lat.  nota  ,Kennzeichen, Merkmal,  Fleck,  Mal'  (substantiviertes  Fem.  des  Partiz.),  Denom.  notö, -äre  ,kennzeichnen,  beobachten ;  tadeln,  rügen',  daher  wohl  auch  in  cognitus^ agiiitus,  vgl.  mit  derselben  Yokalstufe  gr.  "^li-yvo-fog  in  äyvoao)  ,weiß  nicht', dyvoLßj  Icyvota  ,Ünwissenheit' ;  besser  über  äyvöew  (steht  für  *dv6£(ü)  und lat.  nota  (zu  Uvoa&aL  , tadeln')  jetzt  Leumann  Homer.  Wörter  228 ^2; toch.  A  ä-knats,  B  a-knätsa  s.  unten.
gn9-to-s  in  mcjmr.  yngnad,  ynad  ,Richter'  (^en-gnd-to-s),  dirnad  ,Urteils- kraft'  {*de-pro-gn9-to-),  Loth  RC  47,  174  f.
gn-tö'S  in  lit.  pazmtas  ,bekannt',  got.  kunps,  ags.  cüp^  ahd.  kund  ,kund, bekannt',  got.  unkun^s  ,unbekannt';  mit  Hochstufe  der  1.  Silbe  av.  paiti- zanta-  ,anerkannt'  (wie  ä-zainti-  ,Kunde').
gnö'ti-  in  ai.  pra-jiiäti-h  f.  ,Er
=== LEAF 33 ===
kenntnis',  gr.  yvwGig  f.  ,Erkenntnis',  lat. nöti-ö  f.,  aksl.  Inf.  znatiy  russ.  znath  f.  ,die  Bekannten';  vgl.  ahd.  urchnät f.  ,agnitio'  (*gne-ti-s) ;
gn-ti'S  in  ahd.  kunst  (sti-  für  -ti-)  ,Kunst,  Kenntnis,  Weisheit'  (got. kunpi  ,Kunde,  Erkenntnis'  aus  *kunpia-  n.),  lit.  pazinüs  f.  ,Erkenntnis';
gnö-ter-  in  ai.  jnätdr-j  av.  inätar-  ,Kenner',  vgl.  gr.  yvaxJzrjQy  lat.  nötor ,Kenner,  Bürge';  vgl.  ai.  jnäna-m  (*gnö-no-m)  ,Kunde,  Erkenntnis'.
gno-mn  in  gr.  yvwiia  ,Erkennungszeichen ;  Winkelmaß'  (daraus  lat.  gröma ,Meßinstrument  der  Feldmesser'  und,  vom  Akk.  yv(bfj,ova  aus,  auch  norma ,Winkelmaß,  Richtschnur,  Vorschrift,  Regel');  aruss.  znamja  (aksl.  znamenije, znak^)  , Zeichen'  (von  einem  entsprechenden  lat.  *gnömen  ist  *cognömen, agnömen  beeinflußt);  gr.  yvtb^r]  ,Meinung'  (wohl  für  *gnö-m[n']a),  vgl.  lit. zyml  ,Merkzeichen'  (*fjw2);  yvw^tjv  , Richtmaß'.
gnö-tel-  in  sloven.  znätelj  ,Kenner',  russ.  zndteh  ,Mitwisser';  auch  ai. jüätdr-  könnte  statt  zu  gnö-ter-  hierher  gehören.
gens-tlo-  :  gno-tlo-  ,Erkennungszeichen'  in  lit.  Unklas  ,Zeichen' ;  apr. ebsentliuns  ,bezeichnet' :  ai.  jflätra-  n.  ,Fähigkeit  des  Erkennens';
378  f
o-erm.  *knöpla-  in  ahd.  heknuodilen  .vernelimbar  werden^  einknuadi ,insignis';  vgl.  lat.  {g)nöUlis  ^kennbar,  bekannt;  vornehm,  edel'  (Adjekt^ vierung  eines  *gnö-dhlom  ^Kennzeichen') ;
gno-rO'  in  gr.  yv6}Qiy.og  ^kenntlich,  bekannt,  angesehen',  yvco^/fw  ,niacli|
-  bekannt'  (zu  *yvwqov),  wozu  mit  Ablaut  ^gn-rö- :  lat.  gnärus  ,einer  Sache kundig',  ignärus    ,unkundig'  (ignöro   eher    aus    Hgnäro  nach    nösco  umge färbt   als   mit   der   Ablautstufe   von    yvojQLixog),    gnaruris    Gloss.    ,gnärus<||_ ignärures  ,äyvoovvTsq' ,  närräre  ,zu  Wissen  machen,  künden'  =  umbr.  naratn  "^
-  ,narrätö',  naraklum  ,nüntiätiö';   als   Endglied   von  Kompositis   ai.  -jnö,-^
-  av.  uxöa-sna-  ,die  Rede  kennend'.
Hierher  vermutlich  idg.  gne-uos  ,kundig,  wer  es  weiß,  wie  man  es  zu machen  hat,  tatkräftig'  in  anord.  knär  ,tüchtig,  kräftig'  (ags.  gecnceive ,eingestanden,  bekannt'  ist  dagegen  junge  Bildung  von  cnäwan  aus);  vgl. (aus  *^n-ifo-s?)  lat.  nävus  (alt  gnävus)  ,regsam,  tatkräftig',  ignävus  ,ohne  Tat- kraft', woneben  mit  *-9w-  mcjmr.  go-gnaw  ,vertraut  mit'  (*upo-uks-gn9uo-?)^ mbret.  gnou  ,manifeste,  evident',  abret.  inschr.  Bodo-cnous  (d.  i.  -gnous, Loth  RC  18,  93),  mir.  gnö  ,ausgezeichnet',  nir.  gnö  ,business,  affairs'. Eine  ähnliche  Bed.-Entw.  in  der  germ.  Sippe  aisl.  kenn  ,einsichtsvoll,  klug, tüchtig',  ags.  cene  ,kühn,  dreist',  ahd.  kuoni  ,kühn,  kampflustig'  (DehnstuEe wie  ysycDva), 
=== LEAF 34 ===
 vgl.  mit  Tief  stufe  lit.  zyne  ,Hexe'  (,die  Kluge'),  zynis  m. ,Hexenmeister' ;
toch.   AB  knä-  ,wissen,   erkennen',  A  ä-knats,  B  a-knätsa  ,unwissend'.
Über  hitt.   ha-an-na-i  ,urteili'   s.  Pedersen  Hitt.  201  (wenig  glaubhaft).
WP.  I   578ff.,  WH.  I  613f.,  II  176ff.,   Trautmann  370f.,  Feist   316  f.,: Meillet  Cinquantenaire  172  ff.
genebh-,  genobh-  ,Pflock,  Stock,  abgeschnittenes  Holzstück' V? Nur  germanisch,  daher  wohl  kaum  idg.  Herkunft. Es  handelt  sich  wohl  um  zwei  verschiedene  Wortgruppen :
1.  Germ,  kamh-,  kumh-  ,Klotz,  Klumpen,  abgeschnittenes  Holzstück'. Ahd.  kembil  ,Fesselblock',    kamp    ,compes',    anord.    kumhr    ,Holzklotz'
mit  germ.  -p-:  mhd.  kumpf  ,gestutzt,  stumpf,  engl,  chump  ,Holzklotz^ (Anlaut  von  cÄop),  norw.  dial.  kump  ,Klumpen',  norw.  dän.  kamp  ,Berg- kuppe',  anord.  kqppusteinn,  dän.  kampe-sten  ,Rollstein'  usw.  Vgl.  auch unter  gern-,
2.  Germ,  knah-^  knahh-,  knap-,  knapp-  (expressive  Geminationen)  ,Pflock, Stock,  Penis,  Knabe'.
Mit  -h- :  nhd.  dial.  knabe  ,Stift,  Bolzen',  ahd.  knaho,  nhd.  Knabe  ,puer', ags.  cnafa  ds.,  woraus  engl,  cnave  , Schurke';  anord.  knefill  ,Stange,  Pfahl, Stock',  ahd.  knebil,  mhd.  knebel  ,Knebel,  Knöchel'   (auch  ,Schlingel',   wie
379
auch  norw.  knehel),  mnd.  knevel  ,kurzes^  dickes  Querholz,  Knebel^  und o-edrehte  Schnurrbartspitze'^  (nhd.  ,Knebelbart^\  schwed.  dial.  knavel ^dünne  Stange^;
mit  -hh-:  schwed.  dial,  knabbe  ^Knollen,  Klumpen^,  auch  ^untersetzter Bursche,  Rind,  Stier^;  knabb  ,Pflock^  (norw.  ,Bergkuppe^) ;
mit  -p-:  ags.  cnapo,  as.  knapo  ,junger  Mann,  Diener^,  schwed.  dial. knape  , Pflock^  und  ,Knoten^;
mit  -pp- :  nhd.  dial.  Knappe  ,Fuß,  Stütze  einer  Bank',  ahd.  knappo ^Jüngling,  Knabe^,  nhd.  Knappe^  schwed.  dial.  knappe  ,Pflock,  Holzklotz^;
manchmal  sind  obige  Formen  von  den  Ableitungen  von  gn-ebh-  ,zu- sammendrücken*'  (oben  S,  370)  kaum  zu  unterscheiden;  vgl.  oben  (S.  370) anord.  knappr  usw.;
ags.  cenep,  afries.  kenep,  anord.  kanpr  ^Schnurrbart^  (germ.  *kanipa-)j wozu  wohl  rand.  kenneve  ,Halsblock^,  mnl.  kanef-been  , Kinnlade^  sind  wohl irgendwie  mit  genu-  ,Kinn^  (unten  S.  381  f.)  kontaminiert.
WP.  I  585  f.,  Martinet  Gemination  117  f.,  196.
geng-,  gong-  , Klumpen,  klumpig';  gongu-s  ,Ball'.
Gr.  yoyyoog  , Auswuchs  am  Stamm  von  Ölbäumen;  Meeraal'  (daraus  lat. gonger,  conger  ds.),  yoyyocovr]  ^angeschwollene  Halsdrüse',  vielleicht  yoyywv* {.LCüQÖg  Hes.  (,feist  und  dumm'?),  yoyyvXog  ,rund'  (-vlog  Suffix  wie  in OTQoyyvXog,  dyy,vlog]
```


## [2026-09-06T02:18:48.664Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins gnō ===\"\ngrep -n \"gn[oō]-\" AHD_watkins1985.txt | head -20\necho; echo \"=== KNT xšnā ===\"\ngrep -n \"xsna\\|xšnā\\|xsnasatiy\\|adana\" KNT.txt | head -20\necho; echo \"=== BRT zan- know ===\"\ngrep -n \"zan-\\|paiti.zan\\|azainti\\|ā-zainti\" BRT.txt | head -20",
 "description": "Grep AHD, Kent, Bartholomae"
}
```


### [2026-09-06T02:18:48.799Z] TOOL RESULT

```
=== AHD watkins gnō ===
527:gno-
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1332:CAM gembh- CAMARILLA kamer- CAMBIST skamb- CAMBIUM skamb- CAMERA kamer- CAMPYLOTROPOUS kamp- CAN! gno- CANAILLE kwon- CANARY kwon- CANCEL carcer CANCER kar-1
1563:GLOWER ghel-2 GLUCAGON ag- GLUCOSE dlk-u- GLUE gel-1 GLUME gleubh- GLUT gWel-3 GLUTEN gel-! GLUTEUS gel-1 GLUTINOUS  gel-1 GLUTTON gWel-3 GLYCERIN dik-u- GLYPH gleubh- GLYPTIC gleubh- GNAT ghen- GNATHIC genu-2 -GNATHOUS genu-2 GNAW ghen- GNOCCHI gen- GNOME? gno- GNOMON gno- GNOSIS gnd-
1672:IGNORE gno- ILEUS wel-3 ILK i-
1711:KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
1722:KNOT! gen- KNOUT gen- KNOW gno- KNUCKLE gen- KNUR gen- KOBOLD ku- KOHLRABI kaul-, rap- KoINE kom KOPECK skep- KRISHNA = kers-*- Kriss KRINGLE gene- KRYPTON krau- KSHATRIYA tké- KUCHEN kak-2 KuDOs_ keue-!
1929:NOBLE gno- NOCENT nek-! Nock ken-5 NOCTI- nekw-t- NOCTILUCA leuk- NOCTUID nekw-t- NOCTULE nekw-t- NOCTURN nekw-t- NOCTURNAL nekw-t- Nocuous_nek-! NOD ken-2
1935:Norpic_ ner-1 NORM gné- NoRMA gno- NORMAL gno- NORMAN man-1, ner-1 NORN_ sner- NorsE_ ner-! NORTH ner-1 NORTHERN ner-1 NOSE nas-
1937:NOTE gno- NOTHING ne NOTICE gno- NOTIFY dhé-1, gnd- NOTION gndé- NOTOCHORD ndot- NOTORIOUS gn6- NOTORNIS of- NOTTURNO nekw-t- NOUGAT ken-5 NOUMENON nous NOUN no-men- NOURISH (s)nau- NOUS nous

=== KNT xšnā ===
1182:ardastina-, Ardumants, avahar|da], uradana-, dan-
2166:For forms of tanūš, dahydusS, uxsnaus, naus, see
2544:navinaiy, 3d sg. kunavatazy. var-, pres. varnay(a)-: varnavátauy. xsnav-, pres. zinav(a)-: ü-z5navàhy. kan-, pres. kan(a)-: vi-kandhy (and -àh*-di$). jan-, pres. jan(a)-: perhaps (restored) 3d pl. vi-
2899:DNb 26 z£nula amiy, cf. the adj. in the parallel clause uxsnaus атту, in line 27.
4913:(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
5039:dyadana- sb. ‘sanctuary’: deriv. ($1471) of prefix à + vb. yad- ‘worship’. dyadand apn. DB 1.63f.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5197:uradana- adj. ‘of good regulation’: u- ‘good’
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
5829:yad- vb. ‘reverence, worship’, usually middle: Av. yazaite, Skt. ydjati, Gk. aterat, pIE *raój- (888, §113). See also Agiyadiya-, dyadana-, Bagayadi-, zyadā. yadataiy mid. ($213, §235.1) XPh 53. ayadaty lst sg. imf. mid. ($288.Ш) DB 5.16, 32; DSf 18°; DSk 5; XPh 40f. ayadiya imf. pass. ($220) DB 5.16°, 32.  ayadiya^ 3d pl. imf. pass. (8220, $282.11) XPh 36, 40. yadàátaiy subj. mid. (6999 11, 8235.1) DB 5.19, 34f. yadaišä 2d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
5855:?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.

=== BRT zan- know ===
3529:•  j.  a-paiti.zanta-  Adj.  "nicht  gut  auf- genommen, nicht  willkommen  geheissen': ya>a  grantS  ttpa.tbuts  "ts  mi^naiti  mi^rä Vt  10. 39.
5903:Ableit.  aus  azan-,  %  33.  1.  —  Pü.  (lu  A): Iransskr.,  Sü. ;  ahahpuaya;urai-a\\  (lu  V. /J: hal  naz,rJi  (Verwechslung  mit  asna-).
5924:•  j.  *asrü.azan- '*  Adj.  'Tränen  (treibend sva.)  vergiessend' :  'z3nS  (NP.)  hilt>nte anuxajand  (sd.)  takahe  Yt.  JO.38.
5925:'asrai<-  n.  'Träne';  at.  äirav-  r.,  np.  ars.  — "azan-,  an-  Part,  lum  V.  U3-;  s.Bthl.  1F.  jO. 195.  —  ')  NA.  trennt;  s.  ebd.
5982:i)  'treiben,  wegtreiben,  wegschleppen' (Vieh   und  Gefangene   als   Kriegsbeute): jvU  gqm  *vani(rm  (sd.)  aznUe'W.  S-Zl ', —   ' ya  {gäu^  varÄa  (sd.)  azimna  (Pass.)  Yt.  . ;o.86;    —    kaoa    nS  fraourvaesayälti  . drujö  vaismmda  a z;/ mn a m  (APm.)  "wann wird  er  uns,   die  zur  Wohnung  der  Dr.  ,  j.^  g,  azan-  :  asn-'^  n.  'Tag',  im  Gegens. hinweggetriebenen  (Rinder)  . ."  Yt/o.86;,2ur  Nacht:  pat/i  'sai paiti  xsa/ne  Yt./.g,
5988:Abkit.  —  ai.  ähnäm  usw.  (NS.  ihar).  —  Pü. : rS^.  —  ''S  3S.  1.  Doch  beruht  dei  Ansati azan-  lediglich  auf  dem  au  ähan-.  — ")  Thcm.
7444:•  j.  ärStyö.barazan-  Adj.  'von  Klafter- höhe': yim  upairi  *vis*rao(iat  -««(NSn.)'' "auf  dem  das  Gift  klafterhoch  floss"  Y. 9.11.
8047:•  j-.  g-  tätay-''  f.  i)  'Vermögen,  Können, Imslandsein,  Kiaff,  mit  Inf.:  Aat  vf  xsa- :^r^m  kn  'trfi'SS.)  iyao>amli  masda ya>ä *vä  ^kaxmi  (sd.)  asä  vokü  manatikä ^mydidyni  (sd.)  "habt  ihr  die  Herrsch- gewalt, habt  ihr  die  Kraft  lu  tun,  o  M., . .,  o  Asa,  o  VM. . .?"  Y. ^4.5.  2)  'Ver- mögen sva.  Habe,  Besitz,  Gut,  Reichtum'; auch  mit  obj.  und  subj.  Gen.:  mä  yave imat  timiliifm  .  ,  /ratahlt  .  .  x^iiiravatti °ti/  mä  j^ä'hravaiti  äsna  frazaintii  Y. 60.7;  —  äps  °tjm  vS  jaidyämi  pauru.- sars'iqm  . .  *frazaintimla  Y.  (fj.  1 1 ;  —  °tlm pourus.x^a'irqm  .  .  ''frazaintim  Y.  68. 1 1 ; —  kahmäi  °tim  .  .  kahmäi  ainistim  .  . baxsiJni  Yt  10.  108— 110;  —  '/Im  jaio- yanla  . .  molu  pas^aSta  . .  'tlm  baon  sivÜla Yt.5.98;  —  dazdi  ahmJk3tn  . .  'lfm  anum v)r?^r(qmnua  Yt.  ici.33;  —  ydi^a  , .  uz-
8496:•  j.,  g.  'U3,  US',  UZ",  p.  us°,  ud"  i)  Adv. (nur  Komp.  und  Ableit);  —  2)  Praev, (mit  'ai'-,  '^■warps-,  pat-,  'bar-,  'stä-,  'zan- usw.);  Iiinauf;  hinaus'.         IYLÄ32:   hes
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
10924:fl-'Eiweiterung^'t  lus  dem  V.  'zan-;  ^zS.m, S6.  —  M.  jijiiäsati,  jnälah ;  np.  Haäsad  'er erkennt''),  lat.  ^näjfo.  —  i)'Vgl.  Hirt  Abi  au  i 93.  —  ')  mp.  inätan,  np.  sunSdan  "höien' (Hbu.  FSt  8z)  scheint  auf  einer  Kontamina- tion von  air.  xsnä-  und  sru-  lu  beruhen;  vgl. auch  die  PD..werter  SWienAW.  jhS.  880, GIrPb.  /  b.  306.  Undeuüich  Ut  mir  ClrPb. I-  303.  34 1
13227:mit  /rä  i)  'Jemandem  (DaL)  N.  N. (Akk.)  als  Namen  (Akk.)  beilegen':  äat hl  nama  fradai^ya  ätr».dätim  (sd.)  v3  . . V.  A  52.  2)  'etwas  (Akt.)  schaffend verleihen',  von  AhM. ;  a)  mit  Dat  der  Person : tisirtm  .  .  yahiiiäi  hazavrsm  yaoxstinam frada'iap^  ahurö'^t.S.^S  (s- b).  b)  mit Gen.  der  Person:  miinm  . .  yeähe  hazan- r?in  yaoxstinqm  frada^at^'^  ahurd  Yt  70. 82  (s.  a).  3) 'hervorbringen, schaffen',  von AhM.  und  den  AmSf.:  yal  mür^m  .  . /rädaöqm  az»n  (näml.  AhM.)  äat  dim dalqm '. .  Yt.  70.  i ;  —  ana  vaca  . .  da'iat sppnts  mainyui ../rada'kitt^^  (jäm\.väcitti) avusa  sp3ida  V.  ig.  9;  —  apqm  .  .ya  para ahmät  histmta  fra^Utä  a/ratatjiusis  (sd.) ". ,  nachdem  sie  geschaffen  waten"  Yt  79. 53)  55-  ä)  mi'  praed.  Akk.  '(schaffend) bestimmen,  machen  zu  — *:  t»m  . .  i-Tspanqm sravanhqm  uparö.iairim  frada^qm  yim airyamanim  Ulm  FrW.  4.  i ;  Yt /^.  35; —  tiStrim  . .  yim  ratUm  .  .  stärqm  frada- :j<r/5>  ahurB  YtA'.44;  70.  ro3;  —  dazu ^Mi^:  fradai'i^Tla  Vt.j.i ;  — frad^htsi})  Vt 4)  '(schaffend)  bestimmen  für  — ',
14896:—  tqm  yazata  vistaurus  .  .  jniuxhat  °ti vacanhat  (sd.)  Yt5.76.  III)  Praev.  (mit 'als-,  ay,  gan-,  gam-,  'bar-,  'zan-,  'Aaei- usw.)
15063:•  j.  paiti.zantay-  f'gute  Aufnahme,Bewill- kommnung,  Willkomm enheissen':  iä  ahmt nmäne  jamyaris  ya  asaonqm  xittUtaua asayas^a  .  .  'tayasca  Y.  60.  2 ;  - — ■  narsca aidonS  xinäillmca  . .  'zaintyasca  (AP.)  7.3Q.
15542:'vor—',  neben  parö:  aoa  ..  nS  ..  ntpaya .  .  'ri  dniatat  mahrkai  'ri^  . .  aistnake pars  draomSbyS  Y.  57.  25;  JÄ'.  2  ">,  SrB.j; —  th  (Täxüi.frtrvasay^)  .  .paritasca  pairi- värascä  vUfnte  'ri  mainyaoyät  drujat  Yt. ^J-7ij  71;  —  ya'ka  ..  dadränS  m  'ri iri>yqstätal(sd.)  Aaraite  Y.ip.io.  d)  wie lat  ab  zur  Bezeichnung  des  Anlasses, neben  parff:  viian.qzahyehei^A^ca  paiti  . . 'ri"^  *halnyäsca  vöiynäuyU  aurva- byasla  parö  Y.6S.i$.  e)  'ohne' aufTalliger  Verwendung:  yim  antan  äkitim ramm  frajasäi  (Sp.  goo  o.)  afranhansäl (Sp.ioi  o.)  'ri  xi'udrätV.i6.i6"\  4)  mit Instr.;  i)  'ex  — ',  beim  V.  'zan-  mit  /r 'cognoscere':  yS  aSa  (Sp.  11  u.)  -n'' ariira  frasänaiti    F.5.  2)  pairi  SiS
16741:•  j-,  g.,  p.  bav-  V.  'werden'.  Fraes.  1  \hm  V.  7.  52  PiiZ.;  —  iJ»«*'  gag'^ia  ''amar- bu;  bv-'\  2  bava-,  3  bva-'\  17  (Fat.)  ] säntis  Yt  ig.  12;  —  iä  srva  ..  bun^  .. büiya-,  22  bJ-'^,  [25  'vlli/\'>,  27  buya-(^)i']  dagvattam  karstayasia  . .  "die  Nägel  wer- Perf.  I  bväv*',  2  babv'^;  J-Aor.  i  bUs-*''.  \  den  zu  Messern  der  Z>.  und  . ."  V.  ly.  10; —  PPfP.  bsta-]  Inf.  buy^,  'bata,  bOzdyäi.  —  vXsp^m  a  ahmat  yat  kan5  .  .  bavaj I)  'werden  sva,  ins  Dasein  treten,  ent- ,  "usque  eo  donec  senex  . .  fuerit"  Y.j.ig; stehen;  erfolgen,  geschehen':  vupim  a/a-'j,  32,  5.38,  5.31,  Y.  65.  9,  FrW.4.3;  — vamm  hsntiinca  bavanlimcai'^  bßsyan-'  itala  dai/iAävS  AuyäiiyS  baväitti  Yt  S.  36; titnca  ",  .  der  (jetzt)  da  ist  und  (jetzt)  FrW.^.jj — yat  baväni /rya  fri^a  paiti.- ins  Dasein  tritt  und  künftig  ins  Dasein  irdn/tf  (s.5)  Yt./J.sö;  —  siviÜS  bavski ya'ka treten  wird"  Y.2/.4,  Vr,/Ä2;  — vispam  ,mazdi  Az.2.  2-7"^  Vyt4*;  —  *ya%a*ra aSaetüS  sttm  haitimca  bavaintJmca^''  bäs-  ,buyäl  (statt  Plur.)  Aväyaonänhs  pantätüS yeintxmia  Y.  rp,  9;  —  vTspayS  afaonö  Yl/ö.  3;  —  yesnyS  ahi  .  .  yesnyö  buyi stuii Aai'ätyaica  bavqi%yäi^a^  bB^yqi%-\Y.62.i;  —  Uta  buyä  afrazaintis  Y.ii.i; yäi^a  Y,52,i;  68.22;  —  ala  Aau  apa-\  —  ta  tiS  buyqn  kumiid^Y.^^.2;  —  «ä«i ylärB  bvat'''  "da  entstand  jener  Abfluss" ,  e?  buyarps  masänä  Ny. _j-ii;  —  alsiJca Yt  ig.  56;  —  yat  kvan  uzuxsyäti  bvat'>  ■  ^wä  Smavantasca  buyamä  "wirksam  möch- zqm  , .  yacsdäi^rjm  "wenn  die  Sonne  auf-  i  ten  wir  durch  dich  werden  und  mächtig" geht,   erfolgt  eine  Purifizirung  der  Erde"  |y.  47. 4;   —   buyama  ahurahe  . .  frya  ..
17017:•  j.  bar^zan-  m.  'Höhe':  kukatrlm  (sd.) banzS . .  yahmat . .  haca  fi-azgmaite  andvl . .  AazavrHi  (statt  GS.)  'nsha  (IS.)  vTranqm YL5.  g6";  —  xiva/paya  (sd.)  vaOtaya 'nSna  Y.  5. 1 1  PüZ.,  Yt  ig.  40.
17022:'Zum  V.  tarn-.  —  VgL  barizan-  and  Bthl. IF.  p  65.  —  Ptt.  (dRn.);  bäUitä»  bälist,  bälist Aac  bäliilän,
17185:rmt  . .  'zantitn  Yt.  10.  a  5 ;  7 ;  —  rainui •ts  (NS.)  Yt  10. 1 00, 12. 6,  ly.  16;  —  'zan- tmt  ahursm*^  ..  apqm  fiafät»m  Y.  2, 5; /.  5;  —  'za  (VS.)S>  akara<>  .  .  apqm  napS Y.  6'5.  j  a ;  —  haomasca  zairis  'zs  V.  ig. 19;  Y.  70.  a  1 ;  —  sraohm  ..yS  'zS  Y.  57. 30;  —  tiitrJm  . .  "zantim  Yt  8.  a,  4';  — (Ml/  var^uhiya  'zaiti  Yt/o.  68,  17.17,  21, *Si  26,  34,  57.  58,  59.  8.^8,  iS.  4,17. 15; 17.1,  1S.3,  Y,2. 14,  57.3;  —  andvlm sürqm  anähitqm  .  .  'zat'iTm  Yt.5.  15;  — 'za  (als  NS.)  n'qma  ahmt  (näml.  AHM.)  Yt /.  15;  —  ratüm  'zantim  .  .  yim  ahunm mazäqm  Y.57. 4;  — ■  ra%waica  'xaite  Y. 4.2;  yi.ia.i;  —  ra%uiS  'zaiB yu  asahe Y. /.  17,  22.4;  Vr.  5. 6,  N.  ^;  —  raivB *za  (VS.)  "  Vr.  21.  a;  —  fravasayS  .  .  yä 'zaitU  Yl  IJ.  29; —  ahura  mi^ra  °zanta (ND.)  Y.2.11,  YtiO.113,  145;  —  ahu- raäbya  mikragibya  'zanbya  (DD.)^  Y. /. II.  y)  uilrS  .  .   "zu  amava  Yt.l4-i2;
17969:•  j.  ■'■fra-zan-  'Nachkommenschaft,  Kin- der': am  ^afifanha  ao/aauhaiti  ast»m tamia  . .  am  *'sqm  (GP.)  '•  Aog.  48.
```


## [2026-09-06T02:18:50.786Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD dan/snas/frazanag ===\"\ngrep -n \"dānistan\\|dān-\\|šnāxtan\\|šnās\\|frazānag\\|frazān\" PHD.txt PHD_mackenzie.txt | head -30\necho; echo \"=== NYB ===\"\ngrep -n \"frazānak\\|frazān\\|dānistan\\|šnāxtan\\|zand\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-06T02:18:50.882Z] TOOL RESULT

```
=== PHD dan/snas/frazanag ===
PHD.txt:135:šnāxtan ... read M... šn's-.
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:354:frazānaģ [plc”nk! | P frzng, N farzána] wise, intelligent.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
PHD.txt:1072:brave čēr, dilēr, marčābuk, mardān- ag, nēw.
PHD.txt:2140:grateful burdešnēhr, huspās, spās- dār, spāsešnās, spāsūmand.
PHD.txt:2459:intelligent frazānag.
PHD.txt:2538:know danistan, šnāxtan, uzwārdan,
PHD.txt:2539:knowing āgāh, dānāg, dānišnēmand, šnāsag.
PHD.txt:2540:knowledge āgāhīh, danagih, dānišn, frahang, šnāsagīh.
PHD.txt:3118:physics čihr-šnāsīh.
PHD.txt:3579:sense böy, sēhišn, šnāsag.
PHD.txt:4323:wisdom danagih, frazānagīh, xrad; innate ~ àsn-xrad.
PHD.txt:4324:wise dānāg, frazānag, xradēmand, zīrak.
PHD.txt:4548:šnāsagīh šnāsag šnāyišn šnāyīdan šnāz šnāz- šnāzīdan šaw- šawāg Soy, Suy šanēn šūymand -išn
PHD.txt:4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
PHD.txt:4592:беһ- čēh-widarag čēhag 1-2čihr čihrēn- čihrēnīdan čihrīg cihrag čihr-šnāsīh čēhišnīg čēhišn ет! &yónih
PHD.txt:4661:frazānagīh ^3» > O° frazanag 13 d o frazām $ à o frazám- -S à оу
PHD.txt:4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
PHD.txt:5348:gnftar griftàárómand griftan darz garz- darzig garzidan garzag garzišnīg garzián gard- gardān- gardānāg gardānīdan dardūmand girdīh gardīdan dard, gard, gird gardan girdag gardisn dam- zamanig zaman
PHD.txt:5564:gāwars dānistan appar-! appurdan! dānišnūmand dānišn jahūd yākand yākand

=== NYB ===
22:Special attention has been paid, however, to ii indigenous Zoroastrian tradition, the linguistic one as laid down in the neglected but authentic Pazand, as well as the interpretative one manifest in the Sanskrit versions. The value of the information to be acquired through these sources'should not be underrated.
23:I gladly appoint myself à champion of the rehabilitation of Pazand, too often regarded with diffidence and disdain. It became obsolete on many points and requires a great amount of time-consuming critical research before it can be fully utilized. I sincerely hope that this branch of philology will find a careful and scholarly devotee, who does not shrink from the preliminary critical work. -
30:Mrs. Josephson and her husband, Assistant Professor Folke Josephson, Upp- sala, have composed the word lists of the Index (except in the case of Pazand) and ‘have both assisted me in proof-reading for which I owe them great thanks. My pupil, Bo Utas, now at the Scandinavian Institute of Asian Studies in Copen- hagen, has examined the manuscript and part of the proofs with special regard to the New Persian vocabulary. While reading some texts of Volume I together with him I had the opportunity to discuss the linguistic problems and have profited a great deal from his criticism and subtle observations. My sincere thanks to him and best wishes for his future.
120:HYB: uncertain, v. s. v. *mār (could it be HAYY AB ‘debtor’, an adequate designation of a merchant's account-book? BQ (and Steingass) quotes a w. héb as ''Zand and Pazand" in the sense of "agibat i kar ‘the end of any business’)
417:heard as such a ''modesty pronoun" = I. — This pron. is, however, obsolete in BP, and the cas. obl. man (q. v.) is regu- larly used as the cas. rect. The Pazandists had lost all tradition regarding the equi- valent of the ideogr., which they trans- literate mechanically aomen (Mx, SGV), when occurring in the texts. It was omitted in most MSS of the FrP (want- ing in Junker’s text), but exists in Codd. P and S, though with misunderstood Ir. equivalents.
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
1161:Dahöstän [dhyst’n'] n. pr. a town in Gurgan 114"; "' Dihistän in the extremity of Mazandaran near Khwarizm and Jur- jan" Yagut 2, 632
1256:én apčcak ~ i mäzdesn 244; veh ~ 4 apčcak 5914; (En) apécak veh ~ 4 maz- desnān 819. 844; ~ i Ohurmazd 60%; ~ stayitan, ~ yastan: v. these ws; — in particular: the authoritative canonical texts of this religion: én ~, cigon hamäk apastak u zand namely, the whole Avesta and commentary 1078; the quotations from these texts are introduced by the following formula: cigén ~ göbet followed by ku 3613-14, 421-13, 4520, 4615, 484-18, 491-16. 5224, 53%. 541-17; followed by hat (q. v.) 387-8. 4375-26, 4414-15, 503-5; without following particle 41196; (7) cigon et i ~ gobet ku 5323-24, 563. 581. 608. 617-8; cigon pat ~ 7718, pat hàn i ~ göbet kū 4345; andar ~ guft estet 8011; an-ic ~ gobet ku 3819; hac ~ (čičn) paitäk kü 341. 8612-115; cigón hac apécak veh- ~ i mäzdesnän paitäk 819-9; v. further paitäk and paitakéh; v. also s.v. dipivareh. — Av. (662 sqq.) daenä-; Arm. lw. den; MPrthPrs dyn religion, religious community, church; Paz. din. — Cf ak-dénéh, dén-burtàr, denik, dušden, huden.
1421:rad (v. below). 1. HN’: ~ nāmaky this inscription (here above) P 2:3; ~ vizand hac yātūkēh i ~ kanik 373: ~-ic évak hac avdéh the following is one of the miracles 4474; kē hac ~ aštak, veh he
1426:3.8 [the figure l; -’y, -y, -yh] the enel. indef. art.: tigr-é [-1] 339; duxt-ē [BRTH- ^y] 14%; gad-ē [gt'-”y] one stroke with the mace 312°, 4 ēvak-ē [HD-wk!-y] one fourth 998; vāt-ē [-1] 4 hubod 73°; hec ctš-ē [-l] nö 16%; har kas-ē PYS-1] 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [al -ē's spelt -1] zāyēt every forthieth year a child is born of a woman and a man (= of one couple) 8622-23; 6 artestäreh for 6 artēštār-ē 4517. — Identical with ?e; MPrs ‘yw placed after its subst.; Paz. -é, NP -é. — The spelling [-1] is sometimes erroneously used for other suffixes -é: mēd4-1 = mode cas. obl. 72??; har marg- arzanik+-1 = -aržānīkē for the abstr. -arzanikéh 10199.
1502:fradand [prdnd], fradandéh [prdndyh], v. frazand.
1576:frazand [prznd; inser. plend], fradand [prdnd] child: 1. frazand 6522-25, 661"; with the indef. art. —-e [~ + 1] 86%; ~ varzitan to produce children 67%; pl. cas. rect. ~ 963, 9726, 10514; pl. cas. obl. ~-dn 6913, ~-in [plendyn] F:5. — 2. fra- dand 16, 1013-18, 1119.11.24, 123.12.21.25. 1526 (after numeral). 1676; pl. cas. obl. —-ān 210, 37186 99, 12% 1423-5, [51% 2217, = Av. (1004 sq.) frazanti- ; MPrthPrs frzynd, MPrs also przynd; Ps. plendy; Paz. far- zand frazand; NP farzand. — fradand is the authentic SW form, preserved as an orthographical archaism, and listed in FrP ll with the gl. frazand ; the first -d- of fradand is not a dwarfed z, which only occurs in ideograms, and in the inscript- ions has a form wholly different from d.
1577:(frazandéh abstr.) fradandéh the state of being a child: pat ~ as his own child 2?5,
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3198:2räd [l’d; inser. and Ps. Pdy] postpos. l. for the sake of, because of, for, on behalf of, in favour of (7220-21), con- cerning (37?. 2919 etc. passim); ham cim ~ for that very reason 512-13, 671-2; han cim ~ 342, & ~ 795. 9626, 982° for that reason; ēt ~ cé because (conj.) 773-5; ce ~ why? 3511. 795; õi ke ~ for whom 183; — preceded by an inf. or a v. n.: in order to, for the purpose of, because: ditan i Zartuxšt ~ (in order) to see Z. 4777, 5218-19; ves avis matārēh i xrat ~ because more wisdom had been allotted to him 9041-12; — forms together with hac or pat a frame preposition: hac bim i Artaxšēr ~ for fear of A. 1525; 3719. 4612-19; hac hin cim ~ 118%; kirpak i pat dat ~ kart for the sake of Law 6419; pat omet +... ~ in hope of 1211917; pat hän cim ~ cé because (conj.) 10421-22, — 2. used as in NP: a) ‘to, for’: cahārpādān ~ ap hamë dat 1419; Papak ~ héc fradand ne būt P. had no child 19; 32-4, 422;  ménam to ~ nevakeh 4771, v.s. v. méni- tan; 427; frazand i zu&s m kar u kirpak bē- dimoxtan 652-23; — b) denoting the dir. obj. of the pres. tense: hakar né han ~ <apdc> dārēt if you do not abjure that (religion) 191; 2520-21; 453; — c) denoting
3373:not grieve! 359; hakar šmah bagän sahet if it please Your Majesty 19-27, passim; - governing a clause with ki: apt-mān eton sahist ku it seemed to us that 86-7; 3812-13, 569-9. 7834, — Av. (1559) Isand-, pres. sadaya-; OP pres. 0adaya-; MPrs pt. shyd, Verbum 171; the Pazandists (Mx, SGV) give for MDMHn- the equivalent Sthastan ših- (of obscure etymology).
3654:šnas [Sn’s] pres. st. of šnāxtan, in com- pounds: spās-šnāsān (pl. cas. obl.) those understanding service = having service as their profession 71!, v. späs.
3656:šnāxtan [šn'htn'] šnas-, Ist p. sg. šnāsom [Sn’swm] 5777, to understand, to know, to recognize 615; bē ~ 715, 907. 10018; 5722 + hakar ‘whether’. — Av. (559) xénà-, pres. ašnas- = OP (Skr. jää-); MPrthPrs *$n?xin “Snäs-; Paz. Snàxtan $näs-, NP Sinäxlan šinās-.
```


## [2026-09-06T02:19:05.834Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('n',len(leaves))\nfor i in (201,202,203):\n    print('=== leaf',i,'(printed p.',i-21,')===')\n    print(leaves[i][:2200])\nEOF",
 "description": "Read Horn p.181"
}
```


### [2026-09-06T02:19:07.424Z] TOOL RESULT

```
n 412
=== leaf 201 (printed p. 180 )===
— 180 —
ap. ^\^, fra\ plilv. fra bezw. /ar, arm. LW. ]ira-\
ai. ]prd,
kurd. AiZ-, hol-,
808. /<9ri* 'Glanz, Majestät*, ferre^ yurve % vergl. /eveme
(arab. /avarnaq).
ap. N. pr. Vi(fi)da]fa7'na' ; aw. /^'arenah- *61anz';
phlv. N. pr, Farn[hag^ N(a)pl\farnai (Gemme, Hörn,
Mitteilungen, Heft IV, 24), arm. LW. par[lc, päz.
yj'areh,
np. ferrux 'glücklieh', phlv. farraxü, farraxülh
('Glück*) sind durch «(-Epenthese entstanden; vergl.
auch ferytinde.
Vergl. 0f()o/di'7]g' ro d^oroitia rrjv tov uaylaXQov
aii'av rfi QUif.iaYy,ri ivariJ,ialvBvai yXidrrrj (Theoph. Simoc.
IV, 2), Ferru/än, Ferruhän (Nöldeke, Tab.-Übs. 292,
Anm. 2). Hohe Würdenträger führen auf Gemmen
den Beinamen farra/ß (Hörn, a. a. O., 39).
809. ferä, Praefix, 'auf, zu, in' z. B. in fera/m\ auch
selbständig, z. B. ferä restden, yiriften,
aw. frä' in fra\keresta', frä[cidra' etc., ai. prü-
z. B. in präkära-,
810. feräji weit, breit', feräxh \S'r>X-lS (Is. 15, 3).
aw. fradah' Breite'; phlv. /räA bezw. /röA[e] 2),
fräh[(f\T.h^ fräh[e\Jmtan^ frah[e\kart (aw. Vourukasa-),
fr äh[e]raftar (Himd.), fr{ä)hgöyöt {av^woiiru.gaoi/aoUi');
ai. präthas'.
kurd. LW. (?) fereh 'weit'; bei. LW. präh^ präh
weit, breit' (303).
*) Nicht *Teil, Provinz' in Ardeslr ^urre (wie bei Vullers s. v.
xurre)^ vergl. Nöldeke, Tab.-Übs. 11. — Bezzenberger^s Ver-
wendung des päz. ^^'arehy -^'^arehmand bei Fick *, Seite 341 ist falsch.
2) Oft ein Strich zu viel, z. B. vd. 14 (23) Gl.; ich halte die
Form /m/i, frähih etc. aUein für richtig, vergl. /räfi[varst (vd. 18
(128)). Man könnte natürlich auch schon im Pehlevl ffäx lesen, doch
sclM'iiit OS besser, «lor Päzondausspraclie, welche h hat, zu folgen.
=== leaf 202 (printed p. 181 )===
— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a-); phlv. fräd- (päz. fräz^ frfl^); ai. pränc-
(schw. St. präC') ^vorwärts*.
oss. räzäi Von vorn* etc. (210).
812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
muSt^ fer(a)mösiden (Vis und RämTn, S. 50 V. 13).
ai. pra + |/';/?«rs-, ////ifya^c Vergessen' ; y\\]w , framös
bezw. farmös^ framöst^).
bei. samusag, samDsay, n. samusay^ Samösay Ver-
gessen (361), mit anderem Pracfix.
813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
pih (No. 365).
aw. frapi^wa- 'Voizug, first-rate' (Geldner, Ve-
dische Studien 11, 17iJ)'^); phlv. frapili hi^zw. farpfh;
ai. prapitüd' (vergl. Geldner a. a. (). 155 folg.).
LW. wa;^. farhl^ sar. farhe,
Jüd.-pers. HO*!^ (Is. 17, 4) geht auf ein ap. *//(/-
2)itU' zurück.
814. ferjätn *Ende\
ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
jung in Kolophonen. Siehe No. 113).
815. ferxane V^eise, gelehrt*, ferzanegl.
ai. pra + [/^./aw- , jafiäti- 'erkennen , verstehen' ;
phlv. frazänak bezw. farzänak,
Vergl. dänisten (ar. l/iaw-), No. 534.
816. ferzend 'Spross'. sowohl *Sohn* als auch 'Tochter (N'is
und Kämln, S. 22 V. 4, 5 v. u.).
aw. frazainti' 'Nachkonimenschalt*; phlv. farc^attd
bezw. frazand.
*) Vergl. Dar mestcter, Et. ir. IT, 112 foli^g.
*J Nach den arm. LW. hraman^ hrasak, hrahany zu sclilicsson,
scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
Das Päzend lässt beide Möglichkeiten offen.
'j Justi' Thema /raj9J/M- *Füllc' rauss also fallen.
=== leaf 203 (printed p. 182 )===
- 182 -
817. fiv'i stallen 'schicken*.
ap. *fra + [^sta-, vergl. a.i. pra -\- l^stho- (Causat.)
'entsenden, entlassen'.
vergl. Sit'/, (ififcwul 'senden'; bei. sastay ^ n. sastay
(363).
818. ferseng 'Parasange', arab. LW. farsax»
ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
Bund.).
819. firisfe 'Bote.
phlv. firisfak (Dat. d. 3, 15); chald. LVV. vXpnonp
(das de Lagarde fälschlich = np. pereste setzt) und
NOPIDI.?« (Ezra 4, 9), Hoffmann, Zeitschr. f. Assy-
riologie II, 55 (danach Ezra 5, 6 und 7, 6 zu emen-
diren).
Zu np. ßristäden (No. 817), vergl. skr. prasthita-
aufgebrochen, der sich aufgemacht hat'. Ein aw.
^frcfsfa- (aus ar. *prasth'td', vergl. KZ. 25, 56) ist
etwa als Grundform anzunehmen ^).
^[()bi. ffriste, firzste (AM., d. l ßreste) 'Bote; Engel*.
skr. presita- {pra + |/es-, Causat.) 'gesandt', vergl.
ap. fräisayam, fräisaya ; arm. LW. hresfak 'Engel'.
bei. LW. piristay (202).
Die Etymologie stammt von de Lagarde, zuletzt
Semitica I, 67.
820. fermän 'Befehl'.
ap. framana- 'Befehl'; phlv. farman bezw. framm,
arm. LW. hramcm (davon hramanem), talm. }0*)n.
Allgemein entlehnt.
821. f ermüden 'befehlen', Praes. fermäy-em^ fermayis,
fra -f [/^ma-y vergl. ap. framätar- 'Gebieter ; phlv.
farmütan bezw. framiitan^ framät, framäy(i)sn,
822. fernüs 'töricht, nachlässig, verschlafen; Thorheit'.
ai. pra -f [/^nag- 'verloren gehen, verschwinden'.
*) Justi (Glossay 8. v. asta-) hat die Etymologie fra -|- astO' auf-
gestellt, doch giebt es ein aw. asta- 'Gesandter' nicht, und l/^as- (ai.
ag-, agnöti) heisst nicht 'senden*.
```


## [2026-09-06T02:19:08.010Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT xšnā ===\"\ngrep -n \"Snasatiy\\|snasahy\\|xSna\\|jña\\|jna-\" KNT.txt | head -20\necho \"=== KNT dan ===\"\ngrep -n \"adānā\\|adana\\|'know'\" KNT.txt | head -20",
 "description": "Grep Kent again"
}
```


### [2026-09-06T02:19:08.088Z] TOOL RESULT

```
=== KNT xšnā ===
1538:*jnó- in zénüsüliy; *Gna-u- in d-xSnaulty, cf. *ôn-u- in zénuta (S208).
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5339:à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
=== KNT dan ===
1182:ardastina-, Ardumants, avahar|da], uradana-, dan-
2570:II. The secondary ending is -t, which is not written in OP final after & (840); before - the thematic vowel is -e-: pIK *ebheuet, Skt. dbhavat, OP abava; pIE *ebheret, Gk. &фєре, Skt. dbharat, OP abara; Skt. ddruhyat, OP adurujiya; Skt. ddhd- rayat, OP adáraya; viyamarda; unaugmented ava- harida]; etc. Injunctive @adaya. Remodeled non- thematic, dha‘ ‘was’. Passive, abariya, adariya, etc. (§220). Non-thematic: adānā' to z5nà-, adada to 'dá-, айта to *di-, viy-aka" to kan-, avàja" to ava-jan-; in the last two, radical n as well as end- ing é is not represented in the OP orthography. Strong aorist: pIE *edhél, Skt. ddhat, OP ada. Optatives: Skt. gamydi, OP a-jamiya; OP avā- janiyà, Муй, pert. caxriyd.
4913:(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
5039:dyadana- sb. ‘sanctuary’: deriv. ($1471) of prefix à + vb. yad- ‘worship’. dyadand apn. DB 1.63f.
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5197:uradana- adj. ‘of good regulation’: u- ‘good’
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
5829:yad- vb. ‘reverence, worship’, usually middle: Av. yazaite, Skt. ydjati, Gk. aterat, pIE *raój- (888, §113). See also Agiyadiya-, dyadana-, Bagayadi-, zyadā. yadataiy mid. ($213, §235.1) XPh 53. ayadaty lst sg. imf. mid. ($288.Ш) DB 5.16, 32; DSf 18°; DSk 5; XPh 40f. ayadiya imf. pass. ($220) DB 5.16°, 32.  ayadiya^ 3d pl. imf. pass. (8220, $282.11) XPh 36, 40. yadàátaiy subj. mid. (6999 11, 8235.1) DB 5.19, 34f. yadaišä 2d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
5855:?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
```


## [2026-09-06T02:19:23.202Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT lexicon zna/xsna ===\"\ngrep -n \"z5nà-\\|z5na-\\|zZnä\\|xšnā-\\|xsna-\\|xsnasatiy\\|adànà\\|adana'\" KNT.txt | head\ngrep -n \"‘know\" KNT.txt | head -20\necho \"=== HRN 534 danisten ===\"\npython3 - <<'EOF'\ndata=open('HRN.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=data.find('534.')\nwhile i!=-1 and 'dan' not in data[i:i+120].lower():\n    i=data.find('534.',i+1)\nprint(data[i-200:i+1400])\nEOF",
 "description": "Kent lexicon and Horn 534"
}
```


### [2026-09-06T02:19:24.954Z] TOOL RESULT

```
=== KNT lexicon zna/xsna ===
2570:II. The secondary ending is -t, which is not written in OP final after & (840); before - the thematic vowel is -e-: pIK *ebheuet, Skt. dbhavat, OP abava; pIE *ebheret, Gk. &фєре, Skt. dbharat, OP abara; Skt. ddruhyat, OP adurujiya; Skt. ddhd- rayat, OP adáraya; viyamarda; unaugmented ava- harida]; etc. Injunctive @adaya. Remodeled non- thematic, dha‘ ‘was’. Passive, abariya, adariya, etc. (§220). Non-thematic: adānā' to z5nà-, adada to 'dá-, айта to *di-, viy-aka" to kan-, avàja" to ava-jan-; in the last two, radical n as well as end- ing é is not represented in the OP orthography. Strong aorist: pIE *edhél, Skt. ddhat, OP ada. Optatives: Skt. gamydi, OP a-jamiya; OP avā- janiyà, Муй, pert. caxriyd.
4361:2... : DérayavauS: XŠ: ...:с%фат:... DE : adànà : .... ... hasta ...
1143:-dzdh- by -tst-. ada adv. ‘known’, Skt. addhá ‘thus, truly’, from
1228:jiid- ‘know’; the ў is clearly shown in the z-
2202:but Haxümamiiahyà stands in the much miswrilten Ariaramnes inscription, and may replace a gen. in *ananait аз Dárayavaus-ahyà (in inscriptions of Ar- taxerxes I and IT) replaces the old gen. Dérayavahaut. However, the derivative Hazümanis-iya ‘Achaemenian’ seems to justify us in regarding the -5- as belonging to the stem. ? This -n- may come from the perf. ptc. nom. Skt. vidvin, pIE -uós as in Gk. ds(e)ós ‘knowing’; and in the perf. pte. of Skt. it seems to have come from the -nt- of the pres. ptc. * Cf. similar phenomena in the de- clension of Xšayäršan-, 8187. Pisani, Riv. Stud. Or. 19.81-2, argues that Auramazdá is by origin a root-noun in -à-, with analogical gen. to avoid identity of nom. and gen., but this is very improbable. * The divine name ia always declined in both parts in the Avesta; in the Gathàs other words commonly intervene between its two parts, and in the Later Avesta mazda ahuró is more fre- quent than aAuró тагай. * This rather indicates that -h was lost in OP after à, and remained only after d; $40.
5865:vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
=== HRN 534 danisten ===
awä; af/. zäm, zümgai; bei. zämcLS^, n. Jan-
wa^ (420).- 118 —
533. ~dän 'Behälter , vergl. äbdän, nemekdän etc.
aw. awz\da?ia- ; ai. -dhäna- *Behälter\
oss. d. 'döne, t. do7i (110); wa/. sar. -dän,
534. daniHteti 'wissen*, Praes. dän-em, dünä, danls^ ferzam
(No. 815).
g. znnädmün^ ta e-züni (2. Sing.); taJ. züne, hezin
(Impt.) ; gel. dänisten; mäz. dänussin, ddn^ dün (Inipt.);
Kä§. züneden^ zönö^imün^ ziinün, zönäti, zön6n (Aor.).
ap. adänä er wusste' (ap. V^ dan- — arisch I/^ian-);
aw. [/^zaU' 'wissen', paiti].2änatä; phlv. dän(i)stan,
dünak, dänakihj dän(i)sn ; ai. jfändti {l/^Jan- ')) ; arm.
canatif 'bekannt*, ancan 'unbekannt*, cmiäcem 'kennen'
(H. No. 134).
kurd. zänin 'wissen* ; af/. pezanam {ijuti-) ; oss.
d. zönum^ zönun, t. zönin^ zönin (134); bei. zdnag,
n. zänay (422); sar. pad-züti-am, va-zün-am, v/a/. paz-
dan-am,
Friedrich MüUer's Aufstellung, WZKM. IV, 309
scheint mir im Wesentlichen verfehlt.
535. däne 'Korn , arab. dänaj (auch säli]dänaj, sah\danag,
pers. säh]dane)^ dänöe 'Linse*.
aw. düiiiö.^karsa' 'körnerschleppend'; phlv. dänak;
ai. dhänd' 'Getreidekörner*.
kurd. däni (LW.), daneki; bei. (LVV. ?) dän, däniu/,
n. dän, danay 'Korn' (74); af/. LW. däne; sar. pinj]-
dand 'Fünfkorn* d. i. 'Hirse*.
536. dang, däneg 'eine Münze bezw. ein Maass*.
ap. öavay.r} (Herakleides im Etyni. magn.); phlv. dang
(PPGl.), arm. LW. dang, arab. LW. danaq , mand.
LW. Np3xn 'Obolus*, syr. talmüd. LW. pr\ (de
Lagarde, Ges. Abh. 32).
Ursprünglich mit däne (No. 535) identisch.
537. däwer 'Richter*, däwen,
aw. *dätö,bara'; phlv. dätwar, däthar (bezw. dätebar),
dawar, arm. LW. data
```


## [2026-09-06T02:19:32.559Z] TOOL CALL #23: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py",
 "description": "Inspect ref_page.py"
}
```


### [2026-09-06T02:19:32.599Z] TOOL RESULT

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


## [2026-09-06T02:19:34.972Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1298 2>&1 | head -60",
 "description": "Fetch BQT page 1298"
}
```


### [2026-09-06T02:19:42.510Z] TOOL RESULT

```
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 89  OCR-lang: fas

شمفاد -۱۹-
شمخاد ه بکراول‌بروزن بهزادءممروف وبعربی آذان‌الفار کوبند .
است. وآن درختی باشد که چوب آن در غات شمشک * - بکر اوز و فتح نانی
سختی و ملائی بود و از آن چیزها سازند ۱ - | واسکون ثالك‌وکاف , بلفت زند وپازند(۱) کاجد
و مرزنگوش را نی ز گوبند » وآن نوعی ازریحان | راکوبند و آن دانه‌ای باشد معروف که(؟)ازآن
باشد در غایت سبزی و خوشبویی ؛ و بفاح اول | روغن کیرند.
م آمده است - و کنایه از فامت خوبان هم شمذور * بنم اول بروزن پرزورء بلفت
هت , کیلانی رستنیی باشد که برکه آن ببر کهسمتر
شمخار - بکراول‌برون یار شاخهای ماند و در آشپای ترش «داخل کنند و روغن‌آن
تازه را گوبند که از درخت شمعاد برآید وب رکه درد گوش را تافعم است.
آن درمایت سبزی و لطافت وطاراوت و نزاکت شمشیر ۹ « بفتح اول بروزن نخجیر .
باشد و ازغایت با ز کی میل بجانب زمین کندلهذا معروفت و وجه تمه آن شم شیر است که‌دم
شعر!آ ترا پزلف خوبان تشبیه کرده‌اند ۲ ,وبعضی
کوبند درختی است مانند شمشاد وآاهم پیوسته
سبز وخرم میباشد وازچوب آلهم چیزهامیتراشند ی موی
وی دیگر کوبند شمشاد و شمشار هر دو یکی | ۳
است اختلاف در دال ورا شده است ۳ ۰
شمشدر ۴ « با رال و رای بی شله شمشیر
بروزن ستمگر , بلفت زند وپازند (۱)سیر براور | شیر وناخن شیر باشد چه شم بممنی دم و ؛اخن
از راکویند . هردوآمده است ۷ - وروشنایی صبح‌وآفتاب‌رانیز
شمشُر ! - با رای بی‌قطه پروزن غمزداء گوبند . ۹ 9
رستنیی باشد دوابی و آنرا مرزاگوش خوانند شمشی ر گوشتین « بممنی تبغ کوشتین
() چك: ژند ویاژند . (۷) چش: و .
‎٩‏ - پیاوی 5132108118۲ * بندهش ۱۱۹ و ۱۰۳ طبری 51305172۲ » مازندرانی
کنونی 5131512۲ و 512۲ ر510812۳ د«واژه‌نامه1۸۷ س 561۳06۲۷1۲65 3025 . شمعاد
( درتهران) - شعماد رسمی * 12000102 1۷۵۲۵2۲۷5 «نابتی ۱۹4 ورك: کل تلاب۲۰۹.
۴ - فدای آن قد وزلاش که کوبی «رو هشته است از شم‌شاد شمغار .
زسشی. «لغخت فری 6
۴ درد ح ۰.۱ ۴ - وز , 5030)8(910)2(4127۲ ( ونظایرآن) » پهلوی
6 » پیاز «,ونکر ۰۸۹ 8 - مصحف هز . ‎٩)1(771)8۱8‏ و 510280 ۰
پهلوی 60ز۳۷8 . کنجد :۰ ونر ۰.۹۸4 ‎٩‏ - بهاوی 51215۳6۲ «دب رکه ۲۱۳ >
هر اوراق مانوی (بمهاوی) ‎٩12709101۲‏ و 82۲912۲ :
.8505 ۳۲۹120 6ا1:00 ۶ اهنا ه هدند
۷ - و<ه آشته‌اق عامانه ۰
(برهان قاطع ۱۱۷)
```


## [2026-09-06T02:19:51.446Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "BQT scans metadata"
}
```


### [2026-09-06T02:19:52.914Z] TOOL RESULT

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


## [2026-09-06T02:20:00.561Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))['map']\nks=sorted(m,key=int)\nprint(ks[0],m[ks[0]],ks[-1],m[ks[-1]])\nfor p in ['1208','1290','1298','1300','1459','1460','1500']:\n    print(p, m.get(p))\n\"",
 "description": "BQT v3 page map lookups"
}
```


### [2026-09-06T02:20:03.398Z] TOOL RESULT

```
1210 1 1924 721
1208 None
1290 81
1298 89
1300 91
1459 252
1460 253
1500 293
```


## [2026-09-06T02:20:17.691Z] TOOL CALL #27: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | head -20",
 "description": "List cached BQT OCR pages"
}
```


### [2026-09-06T02:20:17.730Z] TOOL RESULT

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
1298.png
1298.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
```


## [2026-09-06T02:20:19.212Z] TOOL CALL #28: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1298.png"
}
```


### [2026-09-06T02:20:19.855Z] TOOL RESULT

```

```


## [2026-09-06T02:20:19.852Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T02:20:29.019Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1298 --pdf-page 93 --image 2>&1 | tail -40",
 "description": "Fetch BQT printed page 1298"
}
```


### [2026-09-06T02:20:30.902Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1298.png
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 89  OCR-lang: fas

شمفاد -۱۹-
شمخاد ه بکراول‌بروزن بهزادءممروف وبعربی آذان‌الفار کوبند .
است. وآن درختی باشد که چوب آن در غات شمشک * - بکر اوز و فتح نانی
سختی و ملائی بود و از آن چیزها سازند ۱ - | واسکون ثالك‌وکاف , بلفت زند وپازند(۱) کاجد
و مرزنگوش را نی ز گوبند » وآن نوعی ازریحان | راکوبند و آن دانه‌ای باشد معروف که(؟)ازآن
باشد در غایت سبزی و خوشبویی ؛ و بفاح اول | روغن کیرند.
م آمده است - و کنایه از فامت خوبان هم شمذور * بنم اول بروزن پرزورء بلفت
هت , کیلانی رستنیی باشد که برکه آن ببر کهسمتر
شمخار - بکراول‌برون یار شاخهای ماند و در آشپای ترش «داخل کنند و روغن‌آن
تازه را گوبند که از درخت شمعاد برآید وب رکه درد گوش را تافعم است.
آن درمایت سبزی و لطافت وطاراوت و نزاکت شمشیر ۹ « بفتح اول بروزن نخجیر .
باشد و ازغایت با ز کی میل بجانب زمین کندلهذا معروفت و وجه تمه آن شم شیر است که‌دم
شعر!آ ترا پزلف خوبان تشبیه کرده‌اند ۲ ,وبعضی
کوبند درختی است مانند شمشاد وآاهم پیوسته
سبز وخرم میباشد وازچوب آلهم چیزهامیتراشند ی موی
وی دیگر کوبند شمشاد و شمشار هر دو یکی | ۳
است اختلاف در دال ورا شده است ۳ ۰
شمشدر ۴ « با رال و رای بی شله شمشیر
بروزن ستمگر , بلفت زند وپازند (۱)سیر براور | شیر وناخن شیر باشد چه شم بممنی دم و ؛اخن
از راکویند . هردوآمده است ۷ - وروشنایی صبح‌وآفتاب‌رانیز
شمشُر ! - با رای بی‌قطه پروزن غمزداء گوبند . ۹ 9
رستنیی باشد دوابی و آنرا مرزاگوش خوانند شمشی ر گوشتین « بممنی تبغ کوشتین
() چك: ژند ویاژند . (۷) چش: و .
‎٩‏ - پیاوی 5132108118۲ * بندهش ۱۱۹ و ۱۰۳ طبری 51305172۲ » مازندرانی
کنونی 5131512۲ و 512۲ ر510812۳ د«واژه‌نامه1۸۷ س 561۳06۲۷1۲65 3025 . شمعاد
( درتهران) - شعماد رسمی * 12000102 1۷۵۲۵2۲۷5 «نابتی ۱۹4 ورك: کل تلاب۲۰۹.
۴ - فدای آن قد وزلاش که کوبی «رو هشته است از شم‌شاد شمغار .
زسشی. «لغخت فری 6
۴ درد ح ۰.۱ ۴ - وز , 5030)8(910)2(4127۲ ( ونظایرآن) » پهلوی
6 » پیاز «,ونکر ۰۸۹ 8 - مصحف هز . ‎٩)1(771)8۱8‏ و 510280 ۰
پهلوی 60ز۳۷8 . کنجد :۰ ونر ۰.۹۸4 ‎٩‏ - بهاوی 51215۳6۲ «دب رکه ۲۱۳ >
هر اوراق مانوی (بمهاوی) ‎٩12709101۲‏ و 82۲912۲ :
.8505 ۳۲۹120 6ا1:00 ۶ اهنا ه هدند
۷ - و<ه آشته‌اق عامانه ۰
(برهان قاطع ۱۱۷)
```


## [2026-09-06T02:20:37.009Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\nmv 1298.png 1294.png; mv 1298.txt 1294.txt\ncd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:1298 --pdf-page 93 --image 2>&1 | head -50",
 "description": "Re-render BQT 1298 from pdf page 93"
}
```


### [2026-09-06T02:20:44.639Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1298.png
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 93  OCR-lang: fas

ششگار -۱۳۰۲-
شنگاد - بروزن زنگار »گیاهی‌است ‎٩‏ | است ۷ که بمدد افراسیاب رفته بود وافراسیاب
که بیخشسطبر و برکش سیاه میباشد وبسرخی | اورا بیاری‌پیران ورسه فرستاد وقتی که‌پنران‌رسه
مایل است و اکر بیخ آنرا زهان بخود برکیرند | بجنگه طویین نوذر میرفت - و بمعنی اول
و درآ ب گرم شینند حیض‌را بگهاید ومعرب‌آن | شنگه هم هست ۸ که شوخ و اظریف - و دزد
شنجار است و بمربی شجرة الدم خوانند. و راه زن - وخرطوم فیل باشد - وضم‌کاف‌فارسی
شنگان - بکر اول بر وزن زدان , و سکون رای بی لقطه و کاف » بادريسهٌ دو4 را
نام ولایتی است ۲ - وجمع شنگه هم هست. گوبند وآن چوب با چرمی باشد مدور که در
شی پر کلری دوه محکم سازند ۸ .
نیز" <- بکس پای‌ایچدیروزن شنگ زن ۱*۶ با زای قطه دار و نود
رنگه ریز شرابی باش د که از درخت خرماحاصل با زای دار و نون
شود - و بزبان پهلوی زنجبیل را کوبند ۴ .| بمعنی دویم شنگرف باشد و آن کرمی است که
شنگر ف‌ - باکاف فارسی » بروزن‌ومعئی 0 سا پا ّ نایم کند حرکت
شنجرف باشد * و آن چیزیست که از سیماب
و گوکرد سازند و نقاشان و مصوران بکار برند شنگل - بنتح اول و ضم ثالك بر وزن
و معرب آن شنجرف است و بیونانی سربقون | فرکل . دزد و راهزن و عیار باشد ۱۱- و دام
خوانند 9 - ونام کرمی هم هست دراز و کندم | پادشاه‌هند که بمدد افراسیاب‌آمده بود ۱۴-ویفتج
خوار که در کشت زارها بهمرسد و غله را خراب | اول و ال جنی از غله را گوبند - و بمعنی
کند ۹ . دزد و راه زن هم‌آمده است ۰.۱۴
شنگر ك - بفتح اول وسکون ثانی‌وئالت شنگله < بفتح اول و ثالث ولام » مطلق
بر وزن پنج‌لك » نام بکی از رایان هتدوستان | خوشه را کوبند اعم از خوشهٌ خرما ۱۴ وانگور
۹ - معرب آن شنجار شنکار < 1100010712 ۸8612۷۶2 < 0۲020۵1]6(فر )دزی
چ ۱ص ۲:۷۹۰ و ۷۹۲ :۰۹۲ ۴ - درممجم البلء ان وحدودالعالم و نخبة‌الدهر نیامده»
ظ . مصحف «سمنگان» (و.م.) است . انا شنگویز (وم.) .
۴ - تصحرفی درقرائت پهلوی 52881۷۷61 ( زنجبیل)«اونوالا6۱۱۱ « که سنگه پیر»هم
خوانده شود . ۵ * زنجرف :
بنفشه‌وار(زار. دهغدا) بپوشیدرو زگارببرف چنا رگشت دوتا وزریرشد شنگرف.
کسایی دروزی «لغت فری ۰۲۸۶
‎٩‏ - رد: هنگه زن (۱). ۷ - درفهرست ولف نیامده . رك : شنگل .
۸ رك4 : شنگه ۰ ۹ - شهنگور (و.م.) «رشیدی؟ < سنگراه (ه.م.) * سنگور
(هم) . ۴ ر4: شنگرف (بیکی مصحف دیگریست). ۱۱ * شنگول «رشیدی» -
شنگوله ر4: لغت فری ص ۲۹۳ ورك: شنگه . ۴ درفهرست واف [ا511288 . نام
«شنكريك» درهاد متداول است «فرهنگه اظام» . ۴۳ ره : دک .شنگراه ۰
۴ درخت‌خرها صد خارزشت داردوخءاف اگردوشنگله خرمای خوب وتردارد.
تاصر خرو بلخی ۰-۱۱4
( برهان‌قاطع ۱۹۸)
```


## [2026-09-06T02:20:56.490Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\nmv 1298.png 1302.png; mv 1298.txt 1302.txt\ncd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:1298 --pdf-page 91 --image 2>&1 | head -45",
 "description": "Fetch BQT pdf page 91"
}
```


### [2026-09-06T02:21:05.280Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1298.png
REF: BQT:1298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 91  OCR-lang: fas

شتن امن ‎٩‏ شا
که نام روز اول هفته باشد ‎٩‏ . از صدف باشد که آنرا تولیای اکبر خوانند
شنت ؟ - بنتح اول و ثالی و سکون و شبرازبان قسبك گویند - وتراجید کی و درهم
- 2 شکتگی را نیز کفته اند 9 .
فوقانی » باغت زند ووازند (۱) بمعنی سال است
و بعربی سئه گوبند. شنجار - با جم بروزن زنگار»ه معرب
۱ شتا شنگار ‎٩‏ است که (۲) لوعی از سرخ هرد باشد
۰ -< بر وزن سرطان » بلغت‌زاد | او آبرا بعربی شجرةالدم و حناء الفوله وعاقرشمما
و پازند (۱) جمع سال باشد که سالهاست‌وبعربی | وعودالفالوذج کویند.
سنین خوانند. شند « بفتح ارل بر وزن قند » منقار
شنج < بفتح اول و سکون ای وَجیم. | مرغانرا ۷ خوانند (۳).
پینی کوه باشد - وزمبنی را دز کوبند که‌بقایت, شندف - بفتح اول بر وزن اشرف»
سخت بودو شکتگی و ناهمواری وسنگه‌بیار | طبل ودمامه ودهل ونقارء بزرکه‌را کویند ۸.
داعته باشد - و بکر اول و سکون ثانی,"کنق شند له - یسم اول و سکون ثالی و کسر
و سرین مردم و حبوانات دبگر را کویند ؛ . وال ابجد وفتح لام » دوایی است کف آراتودری
وباین معنی‌بفتح اول هم گفته‌اند و بافنج‌مرادف خوانند و درکرمان مادر دخت کوبند وتخم‌آنرا
ساخته‌اند۴ - و چم‌اول وسکون‌لون.:رعربی‌لوعی | بعربی بذرالپوه خواشد .

(۱) چك : ژند ویاژند . (۷) چش : و . (۳) چش : کوبند . 8

۱ -< عنبد (ه.م.) * شبرازی 51302060 »گیلکی 520202 لفتی است سامی .
در آرامی :۰5200211 سربانی 5112018 .عبری 52080۵ » اکدی 5112۳2110 . شبانو در
نزد اکدیان بروز پانزدهم ماه - روزیکه دائرة ماء پردود - اطلاق میشد . این کلمه مشتق از
افعال ذبل است : عبری 021 ۰5112(ازکاز کنر رفت, استراحت کرد) » سربانی 512021 (استراحت
کرد ) ۰ اکدی 51128021۷ (استراحت کرد » عاطل گذاشت) » عربی سبت ( استرا<ت کرد ) و
سبت‌الشیء (قطع کردآنرا) وآن از «سب» است بمعنی قطم واستراحت متوقف برانقطاع از شفل
«ولد تمب . همین کلمه است که در عربی سبت « شنبه > و در فرانسوی 527716011 و در آلمانی
8 تشنده.

7 ۱917 هداما ۳۳۵۵۵۲۵۲۵۲۰ هط وان ۸ مصعصسصن2 .3
ورك :بشنها . پورداود ج ۲ ص ۷۹ ؛ معجمیات عربیه - سامیه ص ۰۱۷۵

۲ -هز, ۰50881 580011 ۰ آرامی 51128218 » بپلوی 541 ؛سال « دهارله۲۹۹ »
ان پبونگر ۷۹ ری سنة ای - هرز 0 (جمع ۰ شنت؟(ه.م.) باق پهلوی).
بهلوی 52138 سالها . رك: بونکل ۸۲.

۴ - پبری ودرازی وخشعك شنجی کوبی بگه آلوده لتره غنجی .

منجيك ترمذی.«لغت فرص *۴۷ .۰

8 - (عر) «شنج محر که شتر رو ترنجید کی‌پوست ودر کشید کی آن*«منتهی‌الارب»
```


## [2026-09-06T02:21:22.211Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\nmv 1298.png 1298b.png; mv 1298.txt 1298b.txt\ncd /home/sfmqrb/git/rishe\npdftoppm -f 90 -l 90 -r 200 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt90\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt90.png",
 "description": "Render BQT v3 pdf page 90"
}
```


### [2026-09-06T02:21:24.457Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 91088 Sep  5 22:21 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt90.png
```


## [2026-09-06T02:21:26.502Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt90.png"
}
```


### [2026-09-06T02:21:26.539Z] TOOL RESULT

```

```


## [2026-09-06T02:21:52.021Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json;m=json.load(open('BQT_v3_pagemap.json'))['map']\nfor p in range(1290,1310): print(p, m.get(str(p)))\n\"",
 "description": "Page map 1290-1310"
}
```


### [2026-09-06T02:21:53.402Z] TOOL RESULT

```
1290 81
1291 82
1292 83
1293 84
1294 85
1295 86
1296 87
1297 88
1298 89
1299 90
1300 91
1301 92
1302 93
1303 94
1304 95
1305 96
1306 97
1307 98
1308 99
1309 100
```


## [2026-09-06T02:22:10.938Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nfor p in 88 89; do pdftoppm -f $p -l $p -r 300 -png -singlefile -x 0 -y 0 -W 1700 -H 400 data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/hdr$p; done\nls $S/hdr*.png",
 "description": "Render header strips of pdf pages 88,89"
}
```


### [2026-09-06T02:22:13.007Z] TOOL RESULT

```
/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/hdr88.png
/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/hdr89.png
```


## [2026-09-06T02:22:15.281Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/hdr89.png"
}
```


### [2026-09-06T02:22:15.298Z] TOOL RESULT

```

```


## [2026-09-06T02:22:24.479Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"شناختن\\|شناسیدن\\|شناس \" BQT_v3_pages.txt | head -20\necho \"--- pdf page tags near 88-92 ---\"\ngrep -n \"\\[pdf page 8[5-9]\\]\\|\\[pdf page 9[0-3]\\]\" BQT_v3_pages.txt | head",
 "description": "Search BQT v3 OCR for šenāxtan"
}
```


### [2026-09-06T02:22:24.544Z] TOOL RESULT

```
6468:4 بارنوامه 6004 از- 04[ «بب رکه ۰۲۲۱۷ پارسی‌بادتان ‎xshndsatiy‏ (شناختن) «
6469:کردی 28510 ( شناختن ) ‎evar gol‏ ورك : هوبشمان ‎vay‏ ؛کیلکی ‎Shanaxtan‏ +
10584:‏طبیعت شناس کنابهازطیب وسالج
18182:( شناختن , فهمیدن ) , قس : دانستن ( ارمنی - 080[ ) « اسشق ۸۱۵ » ورك : فاب \ ص۸۵
25695:آنکه در کارها خبیر باشد « دارستتر. تبمات ج۱ ص‌۳۱۵» فرهنگتان «کار شناس » را بجای
30768:جز این چاره‌ای نیز نشناختند
30901:کردن . اطاعت کردن » برباست شناختن ) « جفتابی ص 4۸ ؛ تعظیم کردن و سرفرود آوردن
--- pdf page tags near 88-92 ---
6414:[pdf page 85]
6471:[pdf page 86]
6527:[pdf page 87]
6593:[pdf page 88]
6683:[pdf page 89]
6759:[pdf page 90]
6848:[pdf page 91]
6924:[pdf page 92]
7010:[pdf page 93]
```


## [2026-09-06T02:22:29.918Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '6414,6475p' BQT_v3_pages.txt",
 "description": "Print BQT v3 pdf page 85 OCR"
}
```


### [2026-09-06T02:22:30.061Z] TOOL RESULT

```
[pdf page 85]
NTS ke

شذاوری وآب ورزی باشد 9 - وبه‌منی ‎Asad‏
‏وشوم وهی ‎٩‏ وانگه وعار هم ‎Vali‏ -
و ولابت خرابی را نیز کویند که کی در آن
توطن نکند و خالی از ءردمان باشد - و شاخ

پوست ‎OT‏ رسمان پتاپند ‎٩‏ - و در عربی دام
قبیله است - وخيك کهنه - وپاشیدن آبرا نیز
کوند ۴ .

شنا ‎oh‏ یک راولبروزن‌منا . معروف
است که شناوری وآب ورزی باشد .

شناب ۴ = ‎ING‏ بروزن‌ساب ۰
بمملی شناست که آب ورزی باشد . *

شنار © پکسر اول بروزن‌چنار » بمعنی

لوبرا گونند که ازه از درخت پر آبد - ودر
عربی ۷ - ‎yee‏ دشمنی کردن‌باشدودشن‌داشتن
یعلی با کی وچیزی بدبودن .

شنان @ ‎ge‏ اول , ‎dite‏ آشنان امت

۱ - پهلوی ‎shan‏ ) & شاهدانه , کنف) « ناوادیا ‎٩۱۹۵‏ - شن‌در نورو کچور وزبارت

= شونگ = ‎Lonicera‏ > ثابتی ۰۱۹4 . ۴ شن پکس اول » ریگهای یار ریزه که
درکتار ‎bys‏ و رود بسیار است ؛ ماسه . ۴ _ هه شناء -- آشنا « لفت 48 = شنار

شناب ‏ شناو )¢0(=

شیتاب (ه.م ‎dan‏ اوستابی-
‎Any (ysl, os ( 8‏
هندی‌باستان - 508(اسحمام
کردن).استی 0218 (استحمام)
و ‎axsoun‏ ر ‎axsoin‏
‏(شتن) «اسشق ‎VAY‏ ورك :
هوبتمان ۷۹۲ ۰ ‎SS‏
‏۷ طبری 02500
ماد رالی ‎send eS‏ و
0 « واژه‌نامه ۰۳۰۸ ۰

۴ رل : شنا . انوا اع‌شنا

۵ _ رل : شدا :

بدر گفت مردی وی رود بار برود اندرون شوهمی بی شنار .
برشکور بلخی . «لفت فرس ‎NE‏
‎٩‏ - (عر) « شنار (بقتح اول ) عیب بدتر و عار و امر مشهور ببدی © ‎HOM ged‏
5 آیکه با شکری ‎oy‏ شوم وشنار میبرد نا شکر را تا قصی ار..
مواوی. « فرهنک نظام ‎A‏
‏# شناخفی-بکسراول وفنح‌پنجم ‎pings)‏ کزی). پرلوی 5102:1020 ؛ابرانی‌باستان-
4 بارنوامه 6004 از- 04[ «بب رکه ۰۲۲۱۷ پارسی‌بادتان ‎xshndsatiy‏ (شناختن) «
کردی 28510 ( شناختن ) ‎evar gol‏ ورك : هوبشمان ‎vay‏ ؛کیلکی ‎Shanaxtan‏ +
دالستن » ممرفت یافتن » وفوف یافتن - افرار کردن - دوستی داشتن .
[pdf page 86]
‎oly‏ نوزدهم

‏در شین نقطه‌دار با میم مشتمل بر پنجاه وشش لفت و کنامت
کونند ۵ .*
```


## [2026-09-06T02:22:51.491Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk '/^\\[pdf page /{tag=$0} /شمشاد/{print tag\": \"NR}' BQT_v3_pages.txt | head\necho \"---farzaneh---\"\nawk '/^\\[pdf page /{tag=$0} /فرزانه/{print tag\": \"NR}' BQT_v3_pages.txt | head\necho \"--- v4? ---\"\ngrep -c . BQT_v4_pages.txt",
 "description": "Locate šamšād and farzāneh pages in BQT OCR"
}
```


### [2026-09-06T02:22:54.183Z] TOOL RESULT

```
[pdf page 1]: 6692
[pdf page 1]: 6696
[pdf page 1]: 6698
[pdf page 1]: 6736
[pdf page 1]: 40350
[pdf page 1]: 40400
---farzaneh---
[pdf page 1]: 776
[pdf page 1]: 811
[pdf page 1]: 18148
[pdf page 1]: 18183
[pdf page 1]: 18186
[pdf page 1]: 18205
[pdf page 1]: 36303
[pdf page 1]: 42620
--- v4? ---
20153
```


## [2026-09-06T02:23:00.301Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]', txt)\n# blocks[0] preamble, then pairs\npages={}\nfor i in range(1,len(blocks),2):\n    pages[int(blocks[i])]=blocks[i+1]\nprint('npages',len(pages), min(pages), max(pages))\nfor w in ['شمشاد','فرزانه','فرزین','گزر']:\n    hits=[p for p,t in pages.items() if w in t]\n    print(w, hits[:12])\nEOF",
 "description": "Map BQT v3 OCR pages containing keywords"
}
```


### [2026-09-06T02:23:02.082Z] TOOL RESULT

```
npages 721 1 721
شمشاد [89, 552]
فرزانه [16, 252, 494, 582]
فرزین [249, 252, 253]
گزر [284, 331, 429, 590, 591, 608]
```


## [2026-09-06T02:23:21.225Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]', txt)\npages={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\nprint(pages[252][:3500])\nEOF",
 "description": "Read BQT p.1459 (farzāneh)"
}
```


### [2026-09-06T02:23:23.094Z] TOOL RESULT

```
سنننه
علم وحکمت وداش و استواری باشد ۱ وبکر
اول فرزین شطریج را گوبند » وآن‌مهره‌ای‌باشد
از ‎tLe‏ مهره‌های شطرنج و ‎Vea OT‏ وزس
انت ۳ ۶
قرا ‎GES‏ ۴ = بازای‌قطمدار(۱)بروزن(۷)
پروانه . بمعنی حکیم و دانشمند و عالم و عاقل
باشد ؛ و ترد محققین آنکه مجرد ومطلو‌المنان
‎ask‏ .
قرز بو۵ ۴ - بنتح اول و بای ابمد
بروزنگرم‌سود » پمعنی حکمت باشد که آن در
یافتن افضل معلومات است بافنل علم .
قردد ‎٩‏ - بضم اول و ثالی و سکون
الث و دال ابجد . سبزمایت در نپات سبزی
و تازکی و تری ‎Ts‏ فریز نیز گوبند ؛وبعضی
گوشد سبزم‌ای باشدکه در روی آبهای ابستادء
(۷) چك: پا زا .

۱ فرزانه (هم) :
مخالفان‌تو ‎og‏ فره‌اند 2 ‎Kas‏

۴ فرزین » ورك : فرز .

فرزدد شاد

بهم میرسد و در تابستان و زستان سبز و خرم
عیباشد ‎He‏

فرز ‎wT‏ - بکردال ‎deel‏ .کنابه
از حیوانات آبی باشد - و حباب را ‎ja‏ گویند
وآن ‎ats‏ ماندی است که بوقت باربدن باران
بر روی آب بهم میرسد +

فرر ند ‎LST‏ » بکردال .کنایهاز
لمل و ‎ol‏ و جواهر کانی باشد .

فرز ند خاود » کنابه از ‎wT‏
‏جهانتاب است .

فررند شا ۷ - بنتح اول و ‎AU‏
‏و سکون ثانی ورابع و شین نقطم‌دار بالف کشیده
و بدال بی ‎Me‏ زده » بمعنی مراقبه است که‌سر
جیب فرود بردن ‎Yay»‏ صاحب حال باشد.

. Ody : ‏چك‎ (0

| معادیان تو تافرخند و تافرزان .
بهرامی‌سرخی« لغت فرس ۳۷۹ *.

۴ - فرزان («.م.) . پپلوی 1822026 «مناس

۳ : ۲ > « اونوالا ‎٩۱۲‏ * هندی ‎OL‏ ۳۳2 ( پیشوند بمعنی پیش ) + ‎JAndti . jan‏
( شناختن , فهمیدن ) , قس : دانستن ( ارمنی - 080[ ) « اسشق ۸۱۵ » ورك : فاب \ ص۸۵
ورك : فرزانگی ی « فرزان حکمت ‎ol‏ و حکیم فرزانه »« لفت فرس ۰۳۷۹« فرزانسزاوار
بود ‎Kee (ipa)‏ حکیم راکونند ‎GLO.‏ (مروزی) گوید :

نباشد میل‌فرزانه بفرزند وبزن ‎Sp‏

» ‏این هردو تبرد دل قرزانه.‎ JH oye
. ٩ ۸٩۳ ‏«لت فری‎

۴ - برساختة ‎sho‏ > فرهنگه دماتیر ‎۷0٩‏ » « فاب ۱ : 4۷ .
5 - فربز < فرز < فرس * پریز. «قرزد » سبزم‌ای باشد درآب‌ومدام سب باشد.درتازی

آنرا ثیل(ه.م.) خوانند . بوشکور ( بلخی) گوبد :

فروتر زکیوان ترا ‎spol‏

برخشانی لاله اندر فرزد. »

0 ‏فری‎ cal?

۱ = فرزشاد ‎dsl,‏ دساتیر « فرهنگ دساتیر ۲۵۷ ۰.

‎POU ©‏ -بفتح ‎pind wees pads!‏ کزی بکرپنجم). پهلوی1722808161
«منای ‎٩۲۷6‏ از: فرزانك )= فرزانه) ‎(ge)‏ + یه( سای ببت) ؛ علم. داتابی» حکت. فشل .

‏۵ فرز ند - بقتح‌اولوسوم ؛ پهلوی ‎frazand‏ . ایرانی باستان - 4 ۲82210]دبارتولمه
۶ « یی رکه ۷۵ * اسشق ‎۸۱٩‏ ۲ ؛ ولد . زاده ‎WE.‏ پسر وگاء بدختراطلاق شده«اسشق

‎۰ ‏ورامین‎ we 0G ANN
```


## [2026-09-06T02:23:38.660Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n 1,40p /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T02:23:38.708Z] TOOL RESULT

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


## [2026-09-06T02:23:40.618Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 198 -l 198 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg198 && echo ok",
 "description": "Render dictionary page 198"
}
```


### [2026-09-06T02:23:42.947Z] TOOL RESULT

```
ok
```


## [2026-09-06T02:23:45.010Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg198.png"
}
```


### [2026-09-06T02:23:45.544Z] TOOL RESULT

```

```


## [2026-09-06T02:23:45.541Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:24:02.630Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 198 -l 198 -r 450 -png -singlefile -x 780 -y 1870 -W 900 -H 300 EtymologicalDictionary-persian-english.pdf $S/latin198\npdftoppm -f 198 -l 198 -r 450 -png -singlefile -x 760 -y 3070 -W 900 -H 200 EtymologicalDictionary-persian-english.pdf $S/arm198\necho ok",
 "description": "Crop Latin and Armenian boxes"
}
```


### [2026-09-06T02:24:04.629Z] TOOL RESULT

```
ok
```


## [2026-09-06T02:24:07.047Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/latin198.png"
}
```


### [2026-09-06T02:24:07.064Z] TOOL RESULT

```

```


## [2026-09-06T02:24:10.997Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 198 -l 198 -r 450 -png -singlefile -x 780 -y 2080 -W 950 -H 260 EtymologicalDictionary-persian-english.pdf $S/latin198b\npdftoppm -f 198 -l 198 -r 450 -png -singlefile -x 760 -y 3120 -W 950 -H 180 EtymologicalDictionary-persian-english.pdf $S/arm198b\necho ok",
 "description": "Crop again"
}
```


### [2026-09-06T02:24:13.352Z] TOOL RESULT

```
ok
```


## [2026-09-06T02:24:16.155Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/latin198b.png"
}
```


### [2026-09-06T02:24:16.187Z] TOOL RESULT

```

```


## [2026-09-06T02:24:23.288Z] TOOL CALL #49: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/arm198b.png"
}
```


### [2026-09-06T02:24:23.368Z] TOOL RESULT

```

```


## [2026-09-06T02:24:27.510Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 198 -l 198 -r 450 -png -singlefile -x 780 -y 3450 -W 950 -H 200 EtymologicalDictionary-persian-english.pdf $S/arm198c\necho ok",
 "description": "Crop Armenian node"
}
```


### [2026-09-06T02:24:29.199Z] TOOL RESULT

```
ok
```


## [2026-09-06T02:24:31.805Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/arm198c.png"
}
```


### [2026-09-06T02:24:31.819Z] TOOL RESULT

```

```


## [2026-09-06T02:24:44.394Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵneh₃-\" \\\n \"https://en.wiktionary.org/wiki/دانستن\" \\\n \"https://en.wiktionary.org/wiki/شناختن\" \\\n \"https://en.wiktionary.org/wiki/فرزانه\" \\\n \"https://en.wiktionary.org/wiki/زندیق\" \\\n \"https://en.wiktionary.org/wiki/گزر\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 198, root Gnô/Gogel: verify node forms and routes\" 2>&1 | tail -2\ndone",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-06T02:24:50.011Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b6181410e6c595f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce2e9a5348261e24.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2f16c785afa9c705.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c2f0f96a4904e74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7bd92bc7dd5944e5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5bb45ab691242ed7.txt
```


## [2026-09-06T02:26:01.670Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in b6181410e6c595f7 ce2e9a5348261e24 2f16c785afa9c705; do echo \"########## $f\"; grep -n -A12 -i \"Etymology\" $f.txt | head -60; done",
 "description": "Read fetched Wiktionary etymologies part 1"
}
```


### [2026-09-06T02:26:03.113Z] TOOL RESULT

```
########## b6181410e6c595f7
########## ce2e9a5348261e24
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Usage notes 
75-
76- 1.4.2 
77- Conjugation 
--
171: Etymology
172- [ edit ] 
173-
174- From Middle Persian YDOYTWN-stn' ( dānistan ) , from Proto-Indo-Iranian *ȷ́ānáHti , from Proto-Indo-European *ǵn̥néh₃ti .
175-
176- Related to شناختن ( šenâxtan , “ recognize ” ) , Northern Kurdish zanîn , Baluchi زانگ ( zánag ) , Sanskrit जानाति ( jānāti ) , English know .
177-
178- Pronunciation
179- [ edit ] 
180-
181- ( Classical Persian ) IPA ( key ) : /daː.nis.ˈtan/ 
182-
183- ( Dari, formal ) IPA ( key ) : [d̪ɑː.nɪs.t̪ʰán] 
########## 2f16c785afa9c705
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Usage notes 
72-
73- 1.3.2 
74- Conjugation 
--
154: Etymology
155- [ edit ] 
156-
157- From Middle Persian 𐭱𐭭𐭠𐭧𐭲𐭭 ( šnāxtan , “ to recognize, to know ” ) , from Old Persian 𐎧𐏁𐎴𐎠𐎿𐎠𐏃𐎹 ( xšnāsāhiy ) , from Proto-Iranian *jnaHŝáti , from Proto-Indo-Iranian *ȷ́naHsćáti , from Proto-Indo-European *ǵn̥h₃sḱéti . [ 1 ] 
158-
159- Related to دانستن ( dânestan , “ know ” ) , Northern Kurdish zanîn , Avestan 𐬰𐬀𐬥𐬄𐬥 ( zanąn , “ to recognize ” ) , Baluchi زانگ ( zánag ) , English know .
160-
161- Pronunciation
162- [ edit ] 
163-
164- ( Classical Persian ) IPA ( key ) : /ʃi.naːx.ˈtan/ 
165-
166- ( Dari, formal ) IPA ( key ) : [ʃɪ.nɑːx.t̪ʰán]
```


## [2026-09-06T02:26:10.195Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nwc -c b6181410e6c595f7.txt; head -20 b6181410e6c595f7.txt\nfor f in 0c2f0f96a4904e74 7bd92bc7dd5944e5 5bb45ab691242ed7; do echo \"########## $f\"; grep -n -m3 -A8 \"^ Etymology$\" $f.txt | head -40; done",
 "description": "Check PIE page and other etymologies"
}
```


### [2026-09-06T02:26:11.889Z] TOOL RESULT

```
7433 b6181410e6c595f7.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ǵneh₃-
FETCHED: 2026-09-06T02:24:46Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/ǵneh₃- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/ǵneh₃- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
########## 0c2f0f96a4904e74
156: Etymology
157- [ edit ] 
158-
159- From Middle Persian [script needed] ( plcʾnk' /⁠frazānag⁠/ , “ wise, intelligent ” ) , which is cognate with Parthian 𐫜𐫡𐫉𐫀𐫗𐫃 ( frzʾng /⁠frazānag⁠/ , “ wise, clever ” ) . Equivalent to فرزان ( farzân ) +‎ ـه ( e ) .
160-Perhaps related to Sanskrit प्रज्ञान।Prajnaana (knowledgeful)
161-
162- Pronunciation
163- [ edit ] 
164-
########## 7bd92bc7dd5944e5
164: Etymology
165- [ edit ] 
166-
167- Borrowed from Arabic زِنْدِيق ( zindīq , “ heretic, atheist ” ) , from Middle Persian .
168-
169- Noun
170- [ edit ] 
171-
172- زندیق • ( zındık ) ( definite accusative زندیغی ( zındığı ) , plural زنادیق ( zenâdık ) ) 
--
222: Etymology
223- [ edit ] 
224-
225- Borrowed from Arabic زِنْدِيق ( zindīq ) , from Middle Persian [script needed] ( zndyk' /⁠zandīk⁠/ , “ heretic, Manichaean ” ) .
226-
227- Pronunciation
228- [ edit ] 
229-
230- ( Classical Persian ) IPA ( key ) : /zin.ˈdiːq/ 
########## 5bb45ab691242ed7
326: Etymology
327- [ edit ] 
328-
329- Borrowed from Classical Persian گزر ( gazar ) . Doublet of گاجر ( gājar ) .
330-
331- Noun
332- [ edit ] 
333-
334- گزر • ( gazar )  m ( Hindi spelling गज़र )
```


## [2026-09-06T02:26:20.716Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== PIE gneh3 ===\"; sed -n '40,140p' b6181410e6c595f7.txt\necho \"=== gazar persian ===\"; grep -n -B4 -A10 \"Middle Persian\\|Proto-Iranian\\|uncertain\\|Old Armenian\" 5bb45ab691242ed7.txt | head -60",
 "description": "Read PIE page and gazar Persian etymology"
}
```


### [2026-09-06T02:26:20.784Z] TOOL RESULT

```
=== PIE gneh3 ===

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.1.2 
 Descendants 

 1.2 
 References 

 1.3 
 Further reading 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ ǵneh₃- 

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

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *ǵneh₃- ( perfective ) [ 1 ] [ 2 ] [ 3 ] [ 4 ] 
=== gazar persian ===
231-
232- Etymology 1
233- [ edit ] 
234-
235: Inherited from Middle Persian *gazar . Compare Sanskrit गार्जर ( gārjara ) , Classical Syriac ܓܙܪܐ ( gezzārāʾ ) , Hebrew גֶּזֶר ( gézer ) , Pashto ګازره ( gāzara ) , Alviri-Vidari گزر ( gazer ) , Baluchi گزرک ( gizirk, gazirk ) , Kurdish gêzer , گێزەر ( gêzer ) , Northern Luri گزر ( gezer ) . Compare also the Turkic borrowings: Bashkir кишер ( kişer ) , Tatar кишер ( kişer ) , Turkmen käşir .
236-
237- Pronunciation
238- [ edit ] 
239-
240- ( Classical Persian ) IPA ( key ) : /ɡa.ˈzar/ 
241-
242- ( Dari, formal ) IPA ( key ) : [ɡä.záɾ] 
243-
244- ( Dari, formal ) IPA ( key ) : [ɡä.záɾ] 
245- ( Kabuli ) IPA ( key ) : [ɡä.záɾ] 
--
349- Mazanderani terms with IPA pronunciation 
350- Mazanderani lemmas 
351- Mazanderani nouns 
352- mzn:Vegetables 
353: Persian terms derived from Middle Persian 
354: Persian terms inherited from Middle Persian 
355- Persian terms with IPA pronunciation 
356- Rhymes:Persian/ar 
357- Rhymes:Persian/ar/2 syllables 
358- Persian lemmas 
359- Persian nouns 
360- Persian terms with archaic senses 
361- fa:Vegetables 
362- Urdu terms borrowed from Classical Persian 
363- Urdu terms derived from Classical Persian 
364- Urdu doublets
```


## [2026-09-06T02:26:34.807Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK gog ===\"; grep -n \"gogel\\|gog-\\|gogo\" POK_01.txt POK_02.txt POK_03.txt POK_full.txt 2>/dev/null | head\necho \"=== WLD gog ===\"; grep -rn \"gogel\\|kakgi\\|kakyi\" incoming/WLD/*.txt WLD_band3.txt 2>/dev/null | head\necho \"=== AHD gno full ===\"; python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('gno-. To know.')\nprint(t[i:i+2600])\nEOF",
 "description": "Check Pokorny/WLD for gogel and AHD gno-"
}
```


### [2026-09-06T02:26:36.504Z] TOOL RESULT

```
=== POK gog ===
POK_01.txt:4888:gr.  ogvV(j,i  .errege,  bewege'  (:  ai.  T'^öti]  vgl.  Schwyzer  Gr.  Gr.  I  696/?; das  0  nach  dgso^ac?),  Aor.  (hgoa,  ^gogov,  h'gGo),  Med.  })gwf.iai^  d)gTO  .erhob sich'.  Fut.  dgov{.iai,  them.  Aor.  djgsTO,  Partiz.  bg^evog^  Perf.  Ugwga  .bin erregt';  mit  og-  als  Iterativvokalismus  ögs-oi-iai,  -ovro  .aufbrechen',  mit er-  noch  egero '  wgurjd^T]  Hes..  egoeo '  ÖLsyslgov  Hes..  sgffr] '  ögfirjcr]  (die  dann durch  öjgsro,  b'gaeo  verdrängten  Formen);  ein  Präs.  *l'QWfiL  (wie  xLgvrji.iL) folgt  aus  dem  kret.  Zevg  "'EnigvvTLog  (Schwyzer  Gr.  Gr.  I  695);  -ogvog in  vsogTÖg  .neugeboren'. d-eogrog  .himmlisch',  usw.;  Kvv-,  ^vY,-6gTag, ^ä-igrrjg] hom.  o-ögog  .günstiger  Fahrwind'  {*ögJ^og,  .das  Schiff  treibend'),  ^gog  m. ;Antrieb';
POK_02.txt:152:alb.  gogele  , Kugel,  Ball;  Gallapfel'  (*gel-gal-na)]
POK_02.txt:918:russ.  gogotdth  _,gackern,  schnattern;  laut  lachen^  mdartl.  ,wiehern^,  öech. alt  Jiohtati  ,heulen^,  poln.  gogotac  ,glucken^,  osorb.  gagotac,  gigotac  (wegen g  statt  h  jüngere  Lautnachahmung)  ,schnattern^ ;  russ.  gdgatb  ,schnattern, von  Gänsen^,  9dgci  ^Eidergans^,  gagdra  ,Taucher^  usw.
POK_02.txt:922:russ.  gögolh  ,Quäk-,  Schellente,  anas  clangula^,  poln.  gogol,  gagol  ,clangula glaucion^,  alt  gogoUca  ,fulica^  (Berneker  318).
POK_02.txt:3888:cymr.  gogof  ^Höhle^  (Ableitung  mcjmr.  guocobauc),  bret.  Jcougon  ^sj (*upo-lcuba) ;
POK_full.txt:29594:Root / lemma: gag- gog- 
POK_full.txt:32394:russ. gogotatb " gaggle, cackle, chitchat, talk, snicker, chatter; laugh loudly ', Dialectal " 
POK_full.txt:32406:russ. gogolb " common goldeneye. Golden Eye ', poln. gogoi, g^goF European 
POK_full.txt:32407:goldeneye ', old gogolica^ a coot, a water-fowl ' (Berneker 318). 
POK_full.txt:46854:cymr. gogorcave' (derivative mcymr. guocobauc), bret. kougoh^s. {*upo-kubS)\ 
=== WLD gog ===
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:35663:gogd „ausgelassener Scherz, Possen", gogelen „sich ausgelassen gebarden", 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:38550:gunika ), alb. gogel’e ,,Kugel, Ball; Gallapfel" ( *gal-galnu , Jokl SBWienAk. 
incoming/WLD/WLD_Bd1_pages.txt:53810: gogd „ausgelassener Scherz, Possen", gogelen „sich ausgelassen gebarden",
incoming/WLD/WLD_Bd1_pages.txt:58132: gunika ), alb. gogel’e ,,Kugel, Ball; Gallapfel" ( *gal-galnu Jokl SBWienAk.                       ,
=== AHD gno full ===
gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
gras-
*kunnan in Old English cunnan, to know, know how to, be able to (Old English first and third singular can from Germanic *kann from o-grade *gona-): CAN}, CON2, CUN- NING; b. Germanic causative verb *kannjan, to make known, in Old English cennan, to declare, and Old Norse kenna, to name (in a formal poetic metaphor): KEN, KENNING; c. Germanic *kunthaz in Old English cath, known, well-known, usual, excellent, familiar: (COUTH); UNCOUTH; d. Germanic *kunthithd in Old English cyth(the), cyththu, knowledge, acquaintance, friendship, kinfolk: KrTH. 3. Suffixed form *gné-sko- in Latin (g)n6- Scere, cognéscere, to get to know, get acquainted with: NOTICE, NOTIFY, NOTION, NOTORIOUS; (ACQUAINT), COG- NITION, (COGNIZANCE), (CONNOISSEUR), (QUAINT), REC- OGNIZE. 4. Suffixed form *gné-ro- in Latin igndrdre, not to know, to disregard (i- for in-, not; see ne): IGNORANT, IGNORE. 5. Suffixed form *gn6-dhli- in Latin nobilis, knowable, known, famous, noble: NOBLE. 6. Redupli- cated and suffixed form *gi-gn6é-sko- in Greek gignd- skein, to know, think, judge (and *gnd- in gndm6n, a judge, interpreter): GNOME2, GNOMON, GNOSIS; AGNOSIA, DIAGNOSIS, PATHOGNOMIC, PHYSIOGNOMY, PROGNOSIS. 7. Suffixed zero-grade form “gna-ro- in Latin gndrus, knowing, expert, whence narrdre (< *gnarrare), to tell, relate: NARRATE. (8. Traditionally but improbably re- ferred here are: a. Latin nota, a mark, note, sign, cipher, shorthand character: NOTE; ANNOTATE, CONNOTE, PRO- THONOTARY; b. Latin norma, carpenter’s square, rule, pattern, precept: NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.) [Pok. 2. gen- 376.]
gras-. To devour. 1. Germanic *krasjon-, fodder, in Old English cresse, czrse, cress: CRESS. 2. Suffixed form *gras-men in Latin gradmen, “fodder,” grass: GRAMA, GRAMINEOUS. 3. Suffixed form *gras-ter-, ‘the de- vourer,” dissimilated in Greek gastér, stomach, belly: (GASTRIC), GASTRO-, GASTRULA; EPIGASTRIUM. 4. Redu- plicated form “*gar-gr- dissimilated in Greek gangraina, gangrene: GANGRENE. [Pok. gras- 404.]
[grat-. Also krat-. To scratch. Germanic root. 1. Ger- manic *krattén in Middle Dutch cratsen, to scrape: SCRATCH. 2. Germanic *grat- in Old French grater, to scrape: GRATE}; REGRATE. [Pok. gred- 405.]]
[gravo-. Also grafo-. A designation of rank, later corre- sponding with the feudal title of count. West Germanic noun. Middle Dutch grave, count: MARGRAVE, PALS- GRAVE.]
greut-. To compress, push. 1. Germanic *kridan in Old En
```


## [2026-09-06T02:26:53.168Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON gazar ===\"; grep -n \"گزر\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== MON normal/not/nobel ===\"; grep -n \"نرمال\\|نُرمال\\|نوبل\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5\necho \"=== FFD pages check ===\"; ls -la incoming/FFD/ ; grep -n \"دانستن\" incoming/FFD/FFD_pages.txt | head -5\necho \"=== SPG ===\"; ls -la SPG*; grep -n -i \"xsna\\|khsna\\|kennen\" SPG_keilinschriften1881.txt | head -10",
 "description": "Grep Mo'in, FFD, Spiegel"
}
```


### [2026-09-06T02:26:53.291Z] TOOL RESULT

```
=== MON gazar ===
MON_part1.txt:35780:13 زدن بر» آزمودن که تاب گزر خوردن 
MON_part1.txt:47695:چزر: »12 [معر. گزر] (.) (گیا.) گزر 
MON_part1.txt:54529:طبخ» حوایج ج آشپزخانه. (گیا.) گزر» زردکك. 
MON_part2.txt:32456:گزر 
MON_part2.txt:32469:شامل دو فندقه و بیضوی است. ريشة گزر به 
=== MON normal/not/nobel ===
MON_part2.txt:75244:نرمال: ۱ (ص.) معمولی؛ عادی 
=== FFD pages check ===
total 1452
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 1301330 Sep  4 14:06 FFD_asmaneketab.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  170624 Sep  4 14:06 FFD_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    4096 Sep  4 13:19 FFD_pages.txt.pages
369:اش 2 : دانستن
1448:دانستن
1450:دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
2648:7 (اسم < باران) ۳۴ 1 (ريشه < دانستن) ۱۳
=== SPG ===
-rw-rw-r-- 1 sfmqrb sfmqrb 466443 Sep  4 14:06 SPG_keilinschriften1881.txt
330:dem Steine erkennen, nur der Schlussbuchstabe voft agata (1. 21) ist etwas
591:genau zu erkennen. Auch der Anfangsbuchstabe von yathä ist undeutlich,
1904:erkennen. Cf. NR, 53 — 55.
2586:die wir von Kyrus kennen, von Kambyses ist noch gar keine gefundeii,
2849:schon kennen, hat seinen Namen Kur {S) bis heute beibehalten. —
3400:Sicherheit auf dem Steine zu erkennen (cf. die krit Bem.), ieh wollte
3576:kennen, so mag das Eine wie das Andere möglich sein. Die übrigen
3833:glaubt Oppert in äthafigaina das neupersische iiSJji^\ zu erkennen, das
3908:Herodots (5, 49. 52) erkennen, die im Osten von Armenien wohnen,
4188:den letzten Jahrzehnten, kennen gelernt haben, man wusste aber
```


## [2026-09-06T02:27:01.540Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\npython3 - <<'EOF'\nimport re\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor i,l in enumerate(lines):\n    if 'دانستن' in l and i>1400 and i<1460:\n        print(i,l)\n# find page tag before line 1448\nfor i in range(1448,1300,-1):\n    if 'pdf page' in lines[i] or re.match(r'^\\s*\\[',lines[i]):\n        print('TAG',i,lines[i]); break\nprint('---context---')\nprint('\\n'.join(lines[1435:1465]))\nEOF",
 "description": "Read FFD dānestan entry"
}
```


### [2026-09-06T02:27:03.333Z] TOOL RESULT

```
1447 دانستن
1449 دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
TAG 1445 [pdf page 58]
---context---
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
7[ ماده مضارع و 14 ساخته شده است.
درای + فارسی میانه 473 « ایرانی باستان 472۳-۵7۵*. 278 برای ساختن مادهٌ
مضارع از ربشه به کار می‌رفته است. 41739 صورت بالاندهُ ريشهٌ 7۷ است و آن به معنی
«گفتن». ۳۷ وازژه‌ای اهریمنی بوده» یعنی برای اهریمن و دیو به کار می‌رفته است.
همین‌طور 4۲371120 واژه‌ای اهریمنی بوده است. در فارسی دری» که در آن واژه‌ها به
اهریمنی و اهورایی تقسیم نشده» «دراییدن» به معنی «یاوه گویی» به کار رفته است.
درودن
درود < فارسی میانه 4۳04 < ایرانی باستان 4۲8-۵*. برای 1۵ > آراست. 475
صورت ضعیف ريشةٌ 478۷ است. 4729 به معنی «درو کردن» است.
درو < فارسی میانه 47۵۷* < ایرانی باستان 45۵۳-۵* برای 2 > آرای. در
فارسی میانهٌ مانوی 47 به جای 4۲3* ایرانی باستان آمده» ۶ و لاجایه‌جا
شده‌اند.
دمیدن
```


## [2026-09-06T02:27:14.084Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"khsnâ\\|khšnâ\\|xšnâ\\|chshnâ\\|khsnasâtiy\\|snâsâtiy\\|snâsahy\" SPG_keilinschriften1881.txt | head -20\necho \"--- try 'erkennen' near glossary ---\"\npython3 - <<'EOF'\nt=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\n# glossar: leaf = printed - 29 => printed 216 -> leaf 187\nfor i in (186,187,188):\n    print('=== leaf',i,'===')\n    print(leaves[i][:1800])\nEOF",
 "description": "Find Spiegel glossary page 216"
}
```


### [2026-09-06T02:27:15.765Z] TOOL RESULT

```
--- try 'erkennen' near glossary ---
nleaves 224
=== leaf 186 ===
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
y^ von khs'athra oder 
=== leaf 187 ===
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
doch ist dies nicht ganz sic
=== leaf 188 ===
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
Gäthu (^TT"^ fff y^y ^7?
```


## [2026-09-06T02:27:25.489Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"khshnä\\|khshnâ\\|khshna\\|shnä\\|shnasa\\|snäsä\" SPG_keilinschriften1881.txt | head -20\necho \"--- leaf 187 tail ---\"\npython3 -c \"\nt=open('SPG_keilinschriften1881.txt',encoding='utf-8',errors='replace').read()\nprint(t.split('\\f')[187][1700:3600])\"",
 "description": "Search Spiegel for xšnā"
}
```


### [2026-09-06T02:27:27.170Z] TOOL RESULT

```
260:11. yä. amahy V. . Thätiy. Därayavaush. khshäyathiya. vashnä, Auramazd
274:vashnä* Au
288:26. adkvj. vashnä. Auramazdäha. ima. khshatfam. därayäm'iy X. . Thä
289:11. 12. Die resliluirlen Worte vashnä Auramazdäha und mana fräbara sind nichl
429:60. shnä. Auramazdäha. adam. khshäyathiya. abavam. Auramazdä.
443:68. m. patiyäbaram. vashnä. Auramazdäha. ima. adam. ak'unavam. adam.
485:70. avathä. adam. hamatakhshaiy. vashnä. Auramazdäha. yathä.
520:88. . abara. vashnä. Auramazdäha. Tigräm. viyatarayäma. [pasäva],
571:2J?ara. vashnä. AuramSk
579:3. va. pasäva. adam. Bäbirum. SLShiyavam. vashnä. Auramazdäha,.
675:25. pastäm. abara. vashnä. Auramazdäha. kära. hya. V'idamahyä.
693:35. bara. vashnä. Auramazdäha. kära. hya. mdjiä. avam. käram. tyam.
702:40. uramazdämaiy. upastäm. abara. vashnä. Auramazdäha. kära. Aya.
749:45. vadä. hamaranam. ak'unava, Auramazdä/WÄey. upastäm. abara. t^ashnä.
767:yashnä. Au
776:60. Auramazdämaiy. upastäm. abara. vashnä.Auramazdäha. kära. hya. ma
827:68. m. ak'umä. Auramazdkmsiiy. upastäm. abara. vashnä. Juramazdäba.
900:86. ä. Gitran/^khmä. Anrsimsizddmaiy. upastäm. abara. yashnä. Auramazd
969:6. ish. Auramazdämaiy. upastäm. abara. yashnä. Auramaz
1045:38. shnä. Auramazdäha. kära. hya. manä. avam. käram. tyam. Yahya
--- leaf 187 tail ---
etzte
Theil mag arshan Auge (wie in Qyävarshan) oder arshan» Mann sein,
doch ist dies nicht ganz sicher.
Khshi («ff << TT) herrschen. Im Aw. khs'i, skr. xi.
+ pati: beherrschen. 1. sg. imperf. med. patiyakhshaiy ich be-
herrschte. NRa) 19. Cf. oben die Bemerkungen zu d. St.
Kkshnäs («ff ^ E:^ fTl ^) kennen, praes. coiy. 2. p. sg. sq.
d'ish: khshnäsähad'ish NRa, 42. 3. ps. khshnäsätiy Bh. I, 52. Cf. ^jJCSLu
im Neupersischen und den anderen neuöränischen Dialekten.
6^Äi/Ä4 (^ff" TT W TTl) Besitzthum, Heerde acc. gaUhäm,
Bh. I, 65. So schwierig die Stelle auch ist, so glaube ich doch sicher
dass man das Wort mit aw. gaetha zusammenstellen darf. Cf. oben di
Noten zu der St.
Gaubar'uva «ff^ <7| ^f -« <'n "^Vr) n. pr. Gobryas noi
Bh. IV, 84. V, 7. 9. NRc, 1. Mit Recht hat man den bei Häuptling
von Taberistän vorkommenden Namen Ssü^u od. Sjb^lT hierher gezog«
```


## [2026-09-06T02:27:36.360Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON gazar ctx ===\"; sed -n '32450,32475p' MON_part2.txt\necho \"=== MON normal ctx ===\"; sed -n '75238,75252p' MON_part2.txt",
 "description": "Read Mo'in contexts"
}
```


### [2026-09-06T02:27:36.438Z] TOOL RESULT

```
=== MON gazar ctx ===
۱۴۳ ۲ 


فر هنک فارسی معین 


گزر 


سره ساسحا خخر یسح 


چتریان که دارای ريشة ضسخیم محتوی 
اندوخته‌های گباهی یت این کٌیاه را به 
سب استفادة غذابی از ر شه‌اش در غالب 
نقاط جهان می‌کارند. برگ‌هایش متناوب و 
بدون گوشوارک و دارای بریدگی بسیار 
است. گل آذینش چتر مرکب است و 
گل‌هایش کو چکث به رنگ سفید و میوه‌اش 
شامل دو فندقه و بیضوی است. ريشة گزر به 
علت ما کول بودن مورد مصرف روزانه 
است» حویج» کر کر اکتا 
کگکیاهی است دو ساله و خودر و از تسرة 
چتریان به ارتفاع ۳۰ تا ٩۰‏ سانتیمتر با ساقة 
پره‌دار فرو رفته و برگک‌های ۰ بر یده که 
در صحاری می‌روید و در حقیفت سوعی 
=== MON normal ctx ===
(پرج ها) و هم عضو مولد سلول‌های ماده 
را (ماد کی) و تعداد گیاهانی که گل‌های ماده 
از گل‌های نر جدا باشند به مراتب کمتر از 
دستةٌ قبلی است و در گیاهان بی‌گل هم بطور 
عام دستگاه تولیدمئلی نر و ماده بر روی 
یکث کیاه است.)؛ دو جنسین» هر مافرودیت. 
نرمال: ۱ (ص.) معمولی؛ عادی 
ضح.- احتراز از استعمال این کلم بیگانه 
اولی است. 

نرم‌بیز: ۸۰-7 [ هت سبط (ص فا. ۱.) 
غربالی که دارای سوراخ‌های تنکگ باشد. 
نرم (خوی): (۰50.(ص‌مر.) دارای 
خلق ملایم. دارای خلق پسندیده. 
نرمش: ۱۵۲-4 (امسص.) نو.) قالت
```


## [2026-09-06T02:27:47.998Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN gnosis ===\"; grep -n \"gnosis, n\\.\\|gno-sis\\|gnosis,\" KLN_1966.txt KLN_1971.txt 2>/dev/null | head -5\necho \"=== KLN norm ===\"; grep -n \"^norm,\\|norm, n\\.\\|L\\. norma\" KLN_1966.txt KLN_1971.txt 2>/dev/null | head -8\necho \"=== LAT norma ===\"; grep -n \"norma\" LAT.txt | head -10\necho \"=== LEW norma ===\"; grep -n \"norma\" LEW_1910.txt | head -10",
 "description": "Grep Klein and Latin dictionaries for norma/gnosis"
}
```


### [2026-09-06T02:27:48.119Z] TOOL RESULT

```
=== KLN gnosis ===
KLN_1971.txt:38218:agnoiology, cognition, diagnosis, gnome, ‘maxim’, 
KLN_1971.txt:38219:gnomic, gnomon, gnosis, gnostic, ignoble, ignore, 
KLN_1971.txt:51134:man, tele-, telegnosis, telegraph, teleology, tele- 
KLN_1971.txt:70185:diagnose, tr. v. — Back formation fr. diagnosis, 
KLN_1971.txt:70186:diagnosis, n., determination of the nature of a 
=== KLN norm ===
KLN_1966.txt:25780:nun,  n.,  1)  a  woman  devoted  to  religious  life,  esp. one  living  in  a  convent  under  vows  of  chastity, poverty  and  obedience;  2)  any  of  various  birds. —  ME.  nunne,  nun,  fr.  OE.  nunne,  fr.  Late  L. norma,  ‘an  old  woman,  a  nun’,  fern,  of  nonnus, ‘an  old  man,  a  monk’,  orig.  a  child’s  lip  word. Cp.  OI.  nana,  ModPers.  nana,  ‘mother’,  Gk. vavva,  vcvva,  ‘aunt’,  Alb.  none,  ‘mother,  nurse', Bulg.  neni,  ‘the  older  one’,  Serbo-Croatian  nana, nena,  ‘mother’,  W.  nain,  ‘grandmother’,  which all  were  orig.  child's  lip  words.  Olt.  nonno, ‘grandfather’,  nonna,  ‘grandmother’,  are  loan words  fr.  Late  L.  nonnus,  resp.  nonna.  Cp. nunnery.  Cp.  also  nanism.
KLN_1971.txt:162770:norm, n., standard, pattern, model. — L. norma , 
KLN_1971.txt:162781:lation (astron.) — L. norma , ‘carpenter’s square ; 
KLN_1971.txt:162784:Norma, fern. PN. — Prob. fr. L. norma , ‘rule, 
=== LAT norma ===
353:europdenne et par les formes normales du latin de Rome.
1116:gr. papue, etc.; le o de lat. ocior represente un degri plein, normal au
1197:La d6clinaison de acer, acris est le produit d'nne normalisation;
2040:ger" (question unde). Peregri est la forme normale de locatif; peregre
3018:dissimilation normale de l.
3183:Amb- est la forme normale devant voyelle: ambactus, ambages, ambar-
5447:normaax axis, texo, etc. Tontefois le rapprochement de lat. uiscus et
6587:indo-europ^en normal. Tous les b initiaux resultent donc de phenomenes
7569:k bos , cf.Thes. II 3135,59sqq., pour normaliser la flexion; le g 4 n.pl.
8518:Issu de *caelo-lo-s avec dissimilation normale du premier I; cf.
=== LEW norma ===
```


## [2026-09-06T02:27:52.177Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '162765,162800p' KLN_1971.txt\necho \"=== KLN gnosis entry ===\"\ngrep -n -A8 \"^gnosis, n\" KLN_1971.txt | head -20\necho \"=== KLN know ===\"\ngrep -n -A6 \"^know, tr\" KLN_1971.txt | head -14",
 "description": "Read Klein norm/gnosis/know"
}
```


### [2026-09-06T02:27:52.278Z] TOOL RESULT

```
worter im Arabischen, p. 134), a derivative of 
the verb n e 'ar, ‘he poured out’, which is ‘rel. to 
Heb. na“dr, of s.m. ; cp. Arab, na'ara , ‘it spurted, 
gushed forth’ (said of the blood of a wound), 
na'ara* 1 , ‘earthen jug, pot’, 
norm, n., standard, pattern, model. — L. norma , 
‘carpenter’s square, rule, pattern’, borrowed — 
prob. through the medium of the Etruscans — 
fr. Gk. yvwfxova, acc. of yvckfxtov, ‘carpenter’s 
square’, Jit. ‘one who, that which, knows, 
judge, indicator’, which is rel. to yvtofjnr), ‘mind, 
judgment, maxim, opinion’. See gnome, ‘maxim’, 
and cp. gnomon. Cp. also next word, Norma, 
normal, enormous. 

norma, n., 1) a norm; 2) (cap.) a southern constel- 
lation (astron.) — L. norma , ‘carpenter’s square ; 
rule’. See prec. word. 

Norma, fern. PN. — Prob. fr. L. norma , ‘rule, 
pattern’. See norm. 

normal, adj., 1) agreeing with the standard type; 
2) regular, usual; 3) ( geom .) perpendicular. — 
L. normdlis , ‘made according to a carpenter’s 
square’, fr. norma. See norm and adj. suff. -al 
and cp. abnormal. Cp. also nor-. 

Derivatives: normal , n., normalcy (q.v.), normal- 
ity, n., normal-ly , adv., normal - ness, n. f and the 
hybrids normal-ize, tr. v., norma l-iz-er , n., 
normal-iz-ation , n. 

normalcy, n., normality. — A hybrid coined by 
Warren Gamaliel Harding (1865-1923), presi- 
dent of the U.S.A. (1921-23), fr. normal with 
=== KLN gnosis entry ===
104055:gnosis, n., knowledge, especially that claimed by 
104056-the Gnostics. — ModL. gnosis , fr. Gk. yv&ctk;, 
104057-‘knowledge’, from the base seen also in yvco(jo), 
104058-‘mind, judgment; maxim, opinion*. See gnome, 
104059-‘maxim’, and cp. diagnosis, prognosis, 
104060-gnostic, adj., pertaining to knowledge. — Gk. 
104061-yvoioTtxoq, ‘of knowing’, fr. yvMCTxoq, 'known, 
104062-perceived, understood’, a later collateral form 
104063-of yvcot6c, verbal adj. of yiyvcoo-xsiv, ‘to know’. 
=== KLN know ===
131974:know, tr. and intr. v. — ME. knawen, knowen, 
131975-fr. OE. cnawan, rel. to OHG. bi-chndan, ir- 
131976-chndan , ‘to know’, Goth, kannjan, ‘to make 
131977-known’, OE. cunnan, ‘to know’, cennan , ‘to 
131978-make known, declare, attest’, fr. I.-E. base 
131979-*gene *gend ‘to know’. See can, aux. v., and 
131980-words there referred to and cp. esp. keen, adj.,
```


## [2026-09-06T02:28:05.429Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"zand \\[znd[^.]*\\.\\|zandīk[^.]*\\.\\|zand[ī]*g[^.]*\\.\" PHD.txt | head -10\necho \"---\"\ngrep -n \"zandīk\\|zandik\\|zand,\" PHD.txt PHD_mackenzie.txt | head -6\necho \"=== NYB zand ===\"\ngrep -n -o \"zand \\[[^]]*\\][^.]\\{0,200\\}\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep MacKenzie/Nyberg for zand"
}
```


### [2026-09-06T02:28:07.119Z] TOOL RESULT

```
677:zand [znd | N ~] commentary, explanation, Zend.
---
PHD.txt:677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
PHD.txt:1223:child aburnüy(ag), frazand, waččag, zadag, zahag.
PHD.txt:2272:heresy ahlomoyih, dušwurrēyišnīh, judristagih, zandikih; v. hetero- doxy.
PHD.txt:2273:heretic ahlomoy, judristag, zandik.
PHD.txt:2718:Manichaean zandik.
PHD.txt:2967:offspring frazand, paywand, zahag; (daevic) hunušak,
=== NYB zand ===
1576:zand [prznd; inser. plend], fradand [prdnd] child: 1
4280:zand [wznd] injury, damage 214
4490:zand [znd] knowledge, religious doctrines 6522; esp
```


## [2026-09-06T02:28:24.001Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('\\n'.join(t[4487:4494]))\"",
 "description": "Read Nyberg zand entry"
}
```


## [2026-09-06T02:28:25.286Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/فرزین\" \"https://www.etymonline.com/word/norm\" ; do\npython3 tools/fetch_source.py \"$u\" --note \"page 198: farzin (chess queen) and Latin norma > norm\" 2>&1|tail -1; done",
 "description": "Fetch farzin and etymonline norm"
}
```


### [2026-09-06T02:28:25.648Z] TOOL RESULT

```
izanak [znk'] jaw 50%. - MPrth zne (S); NP zanas.
2zanak (Prth) [znk] kind, sort; hō [LH- w] — ... kü in such a way ... that HajA: 8 = Prs ēgēn... kū. — Olr "zana- — Skr jana- 'race, man, tribe': OP vispa- zana -‘containing all kinds of men’, paru- zana- ‘having many kinds of men’; Av. (1650) srvo.zana- ‘of the horned species’; MPrth zng (MHC); Arm. lw. zanazan ‘different’.
zand [znd] knowledge, religious doctrines 6522; esp. the commentary and explica- tion of the Avesta text (in Phl) 107°. 10815-18, 11020, 1124. — Av. (1660) zanti-, cf s. v. dänistan.
"zandi(k) [zndy] 1179? according to Cat. 110-112 “the Heretic” = Mazdak. — The correct form lis zandik (v. next w.), derived from zand (v. above), and corres- ponding exactly to Gr yvworıxöc. The spelling here is, however, very strange, and it would seem that the seribe has purposely distorted the w. so as to
229
Zarr
resemble ZNB” (for GNB?) = duzd ‘thief’, FrP 13 ult.
```


### [2026-09-06T02:28:29.692Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a04e8ca83f7dd127.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27a5147bc1ebcc44.txt
```


## [2026-09-06T02:28:34.730Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== farzin ===\"; grep -n -m2 -A8 \"^ Etymology\" a04e8ca83f7dd127.txt | head -25\necho \"=== etymonline norm ===\"; grep -n -m1 -A12 \"norm (n\" 27a5147bc1ebcc44.txt | head -20",
 "description": "Read farzin and norm etymologies"
}
```


### [2026-09-06T02:28:34.808Z] TOOL RESULT

```
=== farzin ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.4 
--
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Adjective 
92-
93- 2.5 
=== etymonline norm ===
23: norm (n.) 
24-
25- "a standard, pattern, or model," 1821 (Coleridge), from French norme , from Latin norma "carpenter's square, rule, pattern," a word of unknown origin. Klein suggests a borrowing (via Etruscan) of Greek gnōmōn "carpenter's square." The Latin form of the word, norma , was used in English in the sense of "carpenter's square" from 1670s, also as the name of a small, faint southern constellation introduced 18c. by La Caille.
26- also from 1821 
27-
28- Entries linking to norm 
29-
30- abnormal (adj.) 
31-
32- "not conformed or conforming to rule, deviating from a type or standard, contrary to system or law, irregular, unnatural," 1835, a refashioning of anormal (q.v.) under influence of Latin abnormalis "deviating from a fixed rule, irregular," from ab "off, away from" (see ab- ) + norma "rule" (see norm ).
33-
34- The older form was from French anormal (13c.), from Medieval Latin anormalus , an altered (by association with norma ) borrowing of Greek anomalos "uneven, irregular," from an- "not" (see an- (1)) + homalos "even," from homos "same" (from PIE root *sem- (1) "one; as one, together with"). Compare anomaly . "Few words show such a series of pseudo-etymological perversions" [Weekley]. Another adjective was abnormous (1742) "irregular, misshapen," from Latin abnormis . Related: Abnormally .
35-
```


## [2026-09-06T02:28:39.305Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n \"Middle Persian\\|frazēn\\|Etymology 1\\|Etymology 2\\|queen\" a04e8ca83f7dd127.txt | head -20",
 "description": "Farzin etymology details"
}
```


### [2026-09-06T02:28:39.356Z] TOOL RESULT

```
173: From Middle Persian [Book Pahlavi needed] ( plcyn' /⁠frazēn⁠/ , “ guard, (chess) queen ” ) .
216: ( archaic , chess ) queen , fers 
219:waz safar yābīd yūsuf sad murād Through travel the pawn becomes a noble queen ,
280: ( chess ) fers or queen 
317: Categories : Persian terms inherited from Middle Persian 
318: Persian terms derived from Middle Persian 
338: Hidden categories: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-09-06T02:29:07.171Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 gen- erkennen ===\"\ngrep -n \"erkennen, kennen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5\necho \"=== SYN know ===\"\ngrep -n -i \"17.17 KNOW\\|KNOW (VB\" SYN.txt | head -5\necho \"=== IEC gnos ===\"\ngrep -n \"^gnó\\|gnosko\\|gnoskō\\|gnō-\" IEC.txt | head -8",
 "description": "Grep Walde-Pokorny, Buck, Mann for the know root"
}
```


### [2026-09-06T02:29:07.257Z] TOOL RESULT

```
=== WLD Bd1 gen- erkennen ===
36400:2. (gen-), gene-, geno- „erkennen, kennen". 
36413:338 f. : got. kiinnan ..erkennen, kennen, wissem 1 ( kann , praet. kunpa\ Aus- 
=== SYN know ===
30387:17.17 KNOW Grk. ola, érlorapat, Goth. witan, kunnan Lith.  Zinoli, patinti yuyvaokw ON vita, kunna, kenna Lett.  zinat, pazit i NG nkebpw (tEpw), yrwplfw Dan. vide, kende ChSl. védéti, razumélt, analt Lat. scire, mdscere, cog- Sw. velta, kinna SCr. znati, poznavalt moscere OE witan, gecndéwan, Boh. védéti, endir_— It. sapere, conoscere cunnan Pol.  wiedziéd, znac Fr. savoir, connaitre ' ME wite, (1)knowe, kunne, Russ. nat! % Sp. saber, conocer kenne Skt. _—_—vid-, yna- Rum. sli, cunoaste NE know Ay. vid-, zan- Ir. rofelar, adgén, asa- Du. weten, kennen gninaim OHG wizzan, cunnan, li-, Nir. {aa fhios agam, aith- tr-cnaan, -chennan nigim MHG wissen, kiinnen, be-, W. gwybod, adnabod er-kennen Br. gouzout, anaout NHG wissen, kennen : nt The two main notions which are cov- | were originally expressed by differe
=== IEC gnos ===
```


## [2026-09-06T02:30:15.409Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\nfor w in ['دانستن','شناختن','فرزانه','گزر','زند ']:\n    hits=[p for p,x in pages.items() if w in x]\n    print(w, hits[:8])\nEOF",
 "description": "Grep Aryanpur for the Persian headwords"
}
```


### [2026-09-06T02:30:17.116Z] TOOL RESULT

```
دانستن [17, 110, 186, 263]
شناختن [264]
فرزانه []
گزر []
زند  [54, 168, 331, 403]
```


## [2026-09-06T02:30:21.177Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\[pdf page (\\d+)\\]', t)\npages={int(blocks[i]):blocks[i+1] for i in range(1,len(blocks),2)}\nfor p in (110,264):\n    x=pages[p]\n    for w in ('دانستن','شناختن'):\n        i=x.find(w)\n        if i>=0: print('PAGE',p, repr(x[max(0,i-400):i+400])[:1200]); print()\nEOF",
 "description": "Read Aryanpur entries"
}
```


### [2026-09-06T02:30:22.855Z] TOOL RESULT

```
PAGE 110 '07): 1 با[۷ 37 (73 ۲ همه\nاسلاری کهن (72/ما5 7(#تاتز» 2ا0): :6 /( 021\n0 ,۷۵111 2 (3101813) :]ت0۲\nلهستانی ([۳01/3): ۲0۵۲۸ 4 (851387) +۸۸25\nچک ((ع۲25): ۸ ,۷۵۲ ما۸\nاسلواکی (51.0(4): ۵7 ب3۸ظ۷0۵۲ 1 (ت۲۲۳3\nلیترانی (۸/1۸04لا727/): :00/7075\n1 ۷۴17 9 (5) ,1006-1007 ۳30\nولزی (87ا8/): 8 دورن 6 (۲]۳) و\nبرتونی (/87570): سلطناه هان قاطم + ۳۰\nیادداشت: 8\nچم این واژه در زبان\u200cهای غیرایرانی: خواستن» ترجیح دادن» بهتر دانستن» گزیدن.\nاوستایی (۸8742): 8۸2 سوئدی (982157): ۸ ,880\nسانسکریت (5(/507): 121311 بالآ87 هلندی (07۳(3): 26\nایسلندی کهن (/۵۸ یی صاه): اسلاوی کهن (۴//ما5 7ل#6لاتل صضاه):\n82601۸ ,ت88 نارای ۱۵\nنورس کهن (۸086 2ا0): 81 روسی (۸۷ا595(]#): ندید ۱۱\nساکسرنی کهن (543000 012): 8۸601۸ صربی (/(522814): ۸۸\n۹ فریزی کین (زنلعلم ضام: 880001۸ گالی (ب3لتلا0۸): ۸۸\nآلمانی کهن ۶۷1028720 صاه): پسگشت\u200cها 3335 ۱\n۸ با06ل 8'

PAGE 264 '\nدانه / ۲۶۵\nبادداشت:\n۱- واژه\u200cی "دانا" نیز از همین واجريشه است.\n۲ بازگدت به: شناختن.\nاوستایی (/4۲87۸): ۸ ,0۸۷0 لنونی (لتی) (771420ا): 0۸\nپهلری (۷1الل۳۸):\n6 020 ,020۸ پسگشت\u200cها 5\nکردی (9(0اطن0): ۰ 02080 ,0208 زر\nبلوچی (/61/ال8۸): 6 وال0۸ 2 (8880) :4۸5/215\nافغانی (پشتو) (017۸1/م: ۳ 515 ناط\nسانسکریت (5۸۸/56277): 57 0107 :۸0۸5 بل ۸4۸07\n,013201۸3 ,03۸۸۸8 برهان قاطع : ۸۳۰\nلیترانی ((71۸هلالل7/): 00۸\nِْ\nپارسی باستان (۳2781 010): ابسلندی کهن (/804۸01044 010)(شاید)\n2 2006\nتخاری ۸ (۸ '
```


## [2026-09-06T02:31:24.613Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB ===\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('792')\nleaves=t.split('\\f'); print('nleaves',len(leaves))\n\"\ngrep -n \"sinâchtan\\|šinâchtan\\|snachtan\\|khšnâ\\|chšnâ\" HUB.txt | head -5\necho \"=== BQT v2 zandiq ===\"; grep -n \"زندیق\\|زندیک\" BQT_v2_pages.txt BQT_v1_pages.txt 2>/dev/null | head -5",
 "description": "Grep Hübschmann and Borhan for zandiq"
}
```


### [2026-09-06T02:31:26.342Z] TOOL RESULT

```
=== HUB ===
nleaves 300
=== BQT v2 zandiq ===
BQT_v2_pages.txt:29757: ‫وقلندران‌بندند ‪ ۴‬و بمعنی تند وتیزوسوزندهحم‬                   ‫ومعرب‌آن زندیق است ‪.‬‬               ‫ءد‬
BQT_v2_pages.txt:29794:   ‫نده ‪ ) 20222‬خوانده شد و مد ها ترد عرب زبانان كمه زندیق‬
BQT_v2_pages.txt:29799:  ‫و نیز آلنی فلزی و مجوف که از درون آن‌مبله‌ایآویخته‬               ‫‪۴‬‬            ‫المعارف املام ‪ :‬زندیق ‪.‬‬
```


## [2026-09-06T02:31:30.079Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find page tag before 29757\ntag=None\nfor i in range(29757,29600,-1):\n    if 'pdf page' in lines[i]: tag=lines[i]; break\nprint('TAG',tag)\nprint('\\n'.join(lines[29750:29805]))\nEOF",
 "description": "Read Borhan zandiq context"
}
```


### [2026-09-06T02:31:31.780Z] TOOL RESULT

```
TAG None

‫ر نگ = بفتح اول بروزنرنگ ‪ ۰‬سبزی‬                        ‫وسکون زای نقطه‌دار (‪ )۲‬ومیم‪ .‬نام پهلوانی‌است‬
 ‫وزنگار وچرکی باشد که برروی آبنه وشمشیر‬                ‫تورالی وزور سهراب بن رستم که رستم بيككمشت‬
 ‫وامتال آن دشنند ومعرب آن زاج است_وولات‬                                         ‫کار او را ساخت ‪۹.‬‬
‫زنگبار را پز کوبند ‪ -‬وپرتو آفتاب وماء را حم‬            ‫ر نديك ‪ - ۴‬بفتح اول بروزن نزديك‬
 ‫کفته‌اند ‪ -‬وزنگلة بزر کی را گونن دکه شاطران‬
 ‫وقلندران‌بندند ‪ ۴‬و بمعنی تند وتیزوسوزندهحم‬                   ‫ومعرب‌آن زندیق است ‪.‬‬               ‫ءد‬
                                                                                                  ‫امل‬
                                                                                                    ‫مد ع‬
                                                                                                       ‫تازن‬
                                                                                                          ‫وی‬
 ‫آهنه است ‪ -‬وآب وثراب‌را گهفمته‌اندوحسین‬
 ‫وفائی میکوبد که از اشمار چنین مملوم میشود‬             ‫والی بر وزن‬
                                                                 ‫بکر اول ث‬                       ‫ر تشت‬
 ‫کزهنگ آب صاف باشد و شرابرا بآن تشبیه‬                  ‫روت‬       ‫صروبی‬
                                                                     ‫سشد‬
                                                                       ‫بهنت » بمعنی دیدن با‬
‫کهودشرهای چشمبهم‬      ‫کوی ک‬   ‫ر‪-‬‬‫چ‌اند‬
                                    ‫کرده‬                                                               ‫خوانند ‪.‬‬

                                  ‫نقمله دار‪.‬‬   ‫‪۳‬‬   ‫)(«( جك‪:‬‬            ‫‪۰‬‬   ‫بیلقطه‬   ‫=‬   ‫‪:‬‬   ‫چك‬   ‫(‪)۱‬‬



                                               ‫‪ ۱‬بېلوىی ‪ «11۳6120022‬بونکر ‪: › ۷۰۱‬‬
           ‫بزیر اندر آورده بد پهلوان ‪.‬‬                        ‫مکی زنده پیلی چو کوحی روان‬
  ‫شهید بلخی «لفت فری‪. ۸۸4‬‬                                          ‫‪ - ۴‬رك ‪ :‬زنده ‪ ,‬ژنده‪.‬‬
   ‫(مالوی) « ناوادیا ‪۲٩ : ۷۹۱‬‏ این کلمه‌محتملنا بار اول درفرن‌سوم‬           ‫‪ - ۳‬دپلوی ‪12‬‬

  ‫میلادی در کتيبة ‪ 711121‬موبدان موبد شاهان‌ساسانی هرمزد اول وبهرام اول وبهرام دوم د رکعبة‬
   ‫ز'رنشت درلفش رستم نزديك تخت جمشید آمده وصریحاً بمعنی «مالوی » فاسد المقیده» استعمال‬
                                                                                                 ‫‪ .‬رك ‪:‬‬    ‫شده‬

  ‫‏‪M. Sprengler,‘Kartîr...” , Journal of Near Eastern Studies,‬‬
   ‫‪۷,۱] (0491) , 791 -822 .‬‬
   ‫‪۴F.‬‏‬ ‫‪6۷N‬‬‫ورك‪ :‬مناس ‪۳٤۲‬‏ ‪.۲٤٤ -‬ارمنبان‏ فیزاین‌کلمه رابمانوبان‌اطلاق کرده‌اند ‪ .‬رکه‪ :‬م‪R‬نا‪.‬ل ‪۲‬‬
   ‫‪6‬ی‪1‬د‪1‬ر‪ 00111‬طبع ماساچوست ج ‪ ××۷1‬شمارة ‪ 4‬ص‬           ‫دمعررفی تاربخ عرب تأ‪5‬لی‪۳‬ف‪6‬هت‬
  ‫‪ . 4‬ظاهراً ابن لفت از ‪ 20282‬اوستابی مشتق میباشد که دوبار (سنا‪٩۱‬‏ بند‪ » ۳‬وفدیداد‬
  ‫مذ کور‬   ‫اما در دو موضع‬     ‫‪ ۸۱‬بند ‪ )۵۵ - ۳۵‬در اوستا آمده » هرچند ربثةٌ آن مملوم لست‬

   ‫در ردیف کناهکارانی چون راهزن و دزد و جادوگر و پیمان شکن و دروغزن آورده شده‬
   ‫وبثابرین «زند» بزهگر و فربفتاری است دشمن دین مزدبسنا و زنديك منسوب بزنداست ( با ا‬
   ‫علامت دبت) ‪ .‬مالی کهبعقيد زردشتبان بجادوبی و دروغ وفریب خود را پیغمبر خوانده ومدعی‬
   ‫نده ‪ ) 20222‬خوانده شد و مد ها ترد عرب زبانان كمه زندیق‬
                                                        ‫ز=‬‫‪,‬نديك (‬
                                                                ‫مزدسنا گردید ز‬
   ‫(معرب زنديك) بپیرومانی وبکیکه مرتد و ملحد و دهری و بیدین ومخالف املام می‌بنداشتند‪,‬‬
  ‫اطلاق گردید ‪ ۳‬بورداود ‪ .‬ژندیق ‪ .‬سالنامةٌ دیا ‪ .‬سال ‪ )۷۲۳۱( ۳‬ص ‪ )۷۱۱-۹۱۱‬ورك ‪ :‬داگرة‬
  ‫و نیز آلنی فلزی و مجوف که از درون آن‌مبله‌ایآویخته‬               ‫‪۴‬‬            ‫المعارف املام ‪ :‬زندیق ‪.‬‬

   ‫و بواسطة تمای آن باجدار درونیآوازی برمیآبد ‪ ,‬درپهلوی ‪( 8082‬آلنی‌موسیقی) «اونوالا‪.*۲۸‬‬
                                           ‫يك ‪.‬‬    ‫د‪:‬‬ ‫لدریق ‪ -‬بكر اول »زرك‬   ‫‪#‬‬
   ‫‪ ۵‬اس‬   ‫و‬
```


## [2026-09-06T02:31:49.782Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nlines=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(29757,29000,-1):\n    if 'pdf page' in lines[i]:\n        print('TAG at',i,lines[i]); break\nfor i in range(29757,30200):\n    if 'pdf page' in lines[i]:\n        print('NEXT TAG at',i,lines[i]); break\nEOF",
 "description": "Find pdf page tag for Borhan zandik"
}
```


### [2026-09-06T02:31:51.551Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:31:54.639Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\ngrep -c \"pdf page\" BQT_v2_pages.txt\nawk 'NR>=29600 && NR<=29760 && /[0-9]{3,4}/' BQT_v2_pages.txt | head -5",
 "description": "Check page tags in BQT v2"
}
```


### [2026-09-06T02:31:56.357Z] TOOL RESULT

```
0
      ‫‪4‬دراوستا ‪( 126022‬شناساندن»‬
      ‫معرفت) «بارتولمه ‪ .۹۹۱‬کلم اخیر از مصدر ‪ 022‬اوستابی (‪ 0121‬پارسی‌باستان) بمعنی‌داد‪-‬تن‬
                         ‫وشناختن است که یا پیشود ‪ 2‬در اوستابی صورت ‪ 11022‬در آمده د‬
      ‫( اوستا ‪ )- 40122 -‬بمعنی س(رود» سرودن ) است و"‪ 0106۷002 8۲۵2۰‬بمعنی‬                            ‫‪10‬‬
              ‫‪Henning,‬‬        ‫‪Sogdian‬‬     ‫‏‪loan — words..., BSOS, X.1, p. 104_105.‬‬
```


## [2026-09-06T02:32:05.301Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"زند‬\\|‫زند\" BQT_v2_pages.txt | head -8\necho ---\nsed -n '29580,29620p' BQT_v2_pages.txt",
 "description": "Find Borhan zand entry"
}
```


### [2026-09-06T02:32:05.386Z] TOOL RESULT

```
370:‫بر وزن باك سیر » ام شهری است در‬                                                              ‫زند پوازند (‪۰ )۱‬‬
873:                  ‫زنده ) « منای ‪ ۷۷۲2‬؛ حیوان (جاورگویا » حیوان اطق «دانشنامه ص ‪ ۵‬س ‪: ) > ۵‬‬
1099:                                                          ‫و تای قرشت بر وزن پهلو شکن ‪ ,‬بلغت زند‬
1587:‫واقع شدبنابر آن فارسیان درین روز جشن سازند‬            ‫جشی» تح اول و انی وسکون نون »‬
1643:                                                       ‫ماه کنند ‪ ,‬و در آن روز آش بیار افروزند‬
1743:  ‫ولیکن عامیان لو در آوردند ‪ .‬این روز برکاغذ ها نوبند و بدرر خانه آویزند تا اندرو کزند‬
2588:                                   ‫زندکی است ‪.‬‬
2947:                                                            ‫زند و پازند (‪ )۱‬بمعنی روز است که بعربی يوم‬
---
  ‫وند دونك اند اصزحف‬
                   ‫دوگ رگوبند زبنداز‬                                                              ‫‪۷‬‬   ‫انه خا‬
‫دو قسم از اقام آن ‪ - ۵‬ونام‬                  ‫عمن»ی‬
                                                ‫یاهی‬
                                                   ‫ابر‬                               ‫رت‬               ‫‏‪EE‬‬
       ‫‪۱‬‬          ‫‪۱‬‬              ‫‪9‬‬      ‫‪1‬‬             ‫‪۱‬‬        ‫ر نخ بر حون ردن = کابه از‬
‫هرراب بن رستمبود‬
               ‫پپلوالی بوده‌تورالی که وسزی‬                         ‫‪۹‬‬
‫خجل‌شدنوخجالت کشیدن وشرمند کیباشد ‪ | ۰‬ورستم او را ييك مشت کشت و او را زندههم‬

                                                                             ‫هم ‪.‬‬         ‫)‪ (۱‬چش ‪++‬‬

      ‫حندی باستان ‪( 1102 -‬زنخ) ‏ اوستا ‪" 2۷082 -‬ارمنی ‪( 608۳6‬فك‪ ,‬کونه)‪.‬‬                               ‫‪۱‬‬
  ‫افنانی ع ‪anaZ‬‏ ‪ « 618122‬بلوچی ‪ 6082 , 10022‬و‪( 8082‬ع) » وخی ‪( 80722‬ع)»‬
           ‫‪ ۴‬رك ‪ :‬رخ زدن ‪.‬‬      ‫‪. 4۹۹1‬‬  ‫تق‬‫اس «‬   ‫شفنی ‪ » 080012‬سریکلی ‪00‬‬
                                                           ‫‪ -‬چون رنگ خخجلت زده سرخ گردد ‪:‬‬             ‫‪۴‬‬

              ‫زنخ برخون زد اراج بعداد ‪.‬‬                               ‫تراج غبغبم را کر کنی باد‬
      ‫نظامی کنجوی‪ «.‬کنجینه ‪. ۰۸۰‬‬
                                                                      ‫‪ - ۴‬و بمعنی طمنه وتسخر ‪:‬‬
                      ‫‪.‬‬    ‫شد‬
                            ‫بخازدن‬
                                 ‫ریشخند و زا‬                          ‫آینجنن بخشش وصله لنود‬
      ‫کمال اسمعیل «گنجینه ‪*A.‬‏‬

      ‫‪4‬دراوستا ‪( 126022‬شناساندن»‬
                               ‫‪ - ۵‬زند در پهلوی ‪( 04۳82‬شرح ‪+‬تقسیر)«اونوالا ‪./44‬‬
      ‫معرفت) «بارتولمه ‪ .۹۹۱‬کلم اخیر از مصدر ‪ 022‬اوستابی (‪ 0121‬پارسی‌باستان) بمعنی‌داد‪-‬تن‬
      ‫ور تفر بهلوی بهازدن»‬
                         ‫وشناختن است که یا پیشود ‪ 2‬در اوستابی صورت ‪ 11022‬در آمده د‬
      ‫گردانیده شده ( پور داود ‪ .‬زلدیق ‪ ,‬سالنامةٌ دنا ‪ ۷۲۳۱‬ص ‪ )۸۱۱‬بابددالست که در ازمنة‌سیار‬

      ‫کهن تفیری برای اوستا بزبان اوستایی نوشته بودلد و ده‌ونه‌ای ازین تفیر درخوداوسنای کمولی‬
      ‫بافیمانده و بامتن مخلوط شده است ‪ .‬بعد هسااین تفیر را از زبان اوستابی بزبان پپلوی ترجمه‬
  ‫(اهراً بلاش‌اول اشکالی ‪). ۸۷ - ۱۵‬‬  ‫کردند ‪ .‬طبق سنت پس از تدوین اوستا در زمان ولخش ظ‬
   ‫تفر اوستا بعنی زلد » بزبان پپلوی شروع شد و ندوین این تفیرتا اواخر عهد ساسانیمخصوصاً‬
  ‫کوشید ( چه نام مزدك بامدادان دربند ‪٩4‬‏ از‬  ‫لط‬
                                              ‫تا زمان مزدگ مماصر فباد ( ‪۱۳۵ - ۰44‬م‪) .‬‬
      ‫فصل ‪ 4‬ولدندادآمده ) ‪ .‬زلد با تفیری که امروژه در دست داریم »ت>فسیرست اآزعهد ساسایان‪.‬‬
      ‫روبهم رفته از تفیر پهلوی اوستایمنی اززند ‪ ۰۰۰۱۶۱‬کلمه یما رسیده ‪ .‬در بار مفهوم و استعمال‬
  ‫کلمةٌ «زند» ازقدیم تاکنون دوبسند گان‌شرق وغرب‌دچار اشتباه شدء‌اند از جمله قولمژلف برهالست‬
```


## [2026-09-06T02:32:15.718Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg198.png data/verification/sources/refs/ocr/BOOK/198.png\nls -la data/verification/sources/refs/ocr/BOOK/198.png",
 "description": "Copy page 198 PNG for audit"
}
```


### [2026-09-06T02:32:15.790Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 85794 Sep  5 22:32 data/verification/sources/refs/ocr/BOOK/198.png
```


## [2026-09-06T02:32:42.959Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nmv 1298b.png 1300.png 2>/dev/null; mv 1298b.txt 1300.txt 2>/dev/null\ncp $S/bqt90.png 1299.png\ncat > 1294.vision.txt <<'EOF'\n[read from the PNG by a vision model, 2026-09-05, verification of dictionary page 198]\nBQT vol. 3 (BQT_v3_picofile.pdf) PDF page 89. Printed page number in the header reads \"-۱۲۹٤-\" (= 1294).\nRunning head: شمشاد. Entries on the page: شمشاد ، شمشار ، شمشدر ، شمشرا ، شمشک ، شمشور ، شمشیر ، شمشیر گوشتین.\nMo'in's footnotes: \"۱ - پهلوی shamshâr «بندهش ۱۱۹ و ۱۰۳» طبری shûshâr ... Boxus sempervirens ...\";\n\"۶ - پهلوی shamshêr «دبیرک ۲۱۳» ... Henning, A list of Middle Persian..., BSOS., IX,1,p.82.\"\nNOTE ON OFFSET: pdf 90 of the same file carries the header \"-۱۲۹۹-\" and pdf 93 \"-۱۳۰۲-\", i.e. the scan\njumps 1294 -> 1299 between pdf pages 89 and 90; the pagemap (BQT_v3_pagemap.json) is a plain linear\noffset (printed = pdf + 1209) and is therefore WRONG for pdf pages <= 89 in this region.\nPrinted page 1298 (the entry شناختن) is NOT among the rendered images; its text IS present in the OCR\nfile BQT_v3_pages.txt, in the block tagged \"[pdf page 85]\" (line ~6414 ff.).\nEOF\ncat > 1299.vision.txt <<'EOF'\n[read from the PNG by a vision model, 2026-09-05, verification of dictionary page 198]\nBQT vol. 3 (BQT_v3_picofile.pdf) PDF page 90. Printed page number in the header reads \"-۱۲۹۹-\" (= 1299).\nRunning head: شنبه. Entries: (continuation of شنان) ، شناو ، شناه ، شنب ، شنبد ، شنبلیت ، شنبلید ،\nشنبلیله ، شنبه. So the page immediately preceding it (printed 1298) is the one carrying شنا / شناختن /\nشناس — which is the page Nourai cites as BQT:1298, and whose text is in BQT_v3_pages.txt \"[pdf page 85]\".\nEOF\ncat > 1300.vision.txt <<'EOF'\n[read from the PNG by a vision model, 2026-09-05] BQT vol. 3 PDF page 91 = printed 1300 (entries\nشنبد؟ ، شنت ، شنتا ، شنج ، شنجار ، شند ، شندف ، شندله). Rendered only to fix the printed-page offset.\nEOF\ncat > 1302.vision.txt <<'EOF'\n[read from the PNG by a vision model, 2026-09-05] BQT vol. 3 PDF page 93 = printed 1302 (header\n\"-۱۳۰۲-\"; entries شنگار ، شنگان ، شنگبین؟ ، شنگرف ، شنگرک ، شنگل ، شنگله). Rendered only to fix the\nprinted-page offset; see 1294.vision.txt.\nEOF\nls",
 "description": "Save vision transcriptions for BQT pages read as images"
}
```


### [2026-09-06T02:32:44.733Z] TOOL RESULT

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
1294.png
1294.txt
1294.vision.txt
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
1465.png
1465.txt
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
1759.png
1759.txt
1776.png
1776.txt
1783.png
1783.txt
1786.png
1786.txt
1786.vision.txt
1803.png
1803.vision.txt
180.png
180.vision.txt
1819.png
1819.txt
181.png
181.vision.txt
1848.png
1848.txt
1861.png
1861.txt
1862.png
1862.txt
1864.png
1864.txt
1865.png
1865.txt
1870.png
1870.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
2080.png
2080.txt
2083.png
2083.txt
2099.png
2099.txt
2143.png
2143.txt
220.vision.txt
2222.png
2222.txt
2224.png
2224.txt
2246.png
2246.txt
2246.vision.txt
2293.png
2293.txt
2331.png
2331.txt
2396.png
2396.txt
2406.png
2406.txt
2407.png
2407.txt
2427.png
2427.txt
2427.vision.txt
31.vision.txt
333.png
333.vision.txt
58.vision.txt
70.vision.txt
72.vision.txt
733.png
733.vision.txt
902.png
902.vision.txt
```


## [2026-09-06T02:35:13.849Z] TOOL CALL #79: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198a.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5neh%E2%82%83-\"\n\ne0_nodes = []\n\ne0_nodes.append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"zan 2, zânâ 2; dan, dânâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both halves of the box are attested, and Pokorny puts them side by side on the very page Nourai cites. Avestan has the root zan- 'to know' (YAv. paiti.zanənti 'they recognise', frazānaiti 'he learns', auuazanən), Iranian z- being the regular outcome of PIE palatal *ǵ; the nasal present *ǵn̥-né-h₃-ti gives the stem zanā-/zānā- (Pok. 376 'av. zanā-t, zanąn'), which is Nourai's 'zânâ'. Old Persian has the same nasal present with an unexplained d- for expected z-: DB 1.51 a-dānā 'he knew' (Kent: 'Non-thematic: adānā to zānā-'), which is why Horn no. 534 writes 'ap. adānā \\\"er wusste\\\" (ap. √dan- = arisch √źan-)' — exactly Nourai's pairing of dan/dānā with zan/zānā. The d- is still debated (dialect mixture, or contamination with dā- 'to put/give'); Wiktionary and Cheung nevertheless set NP dānistan and Av. zan- under one root, PIIr. *ȷ́ānáHti < PIE *ǵn̥néh₃ti. The only inaccuracy is one of labelling: zan/zānā are Avestan and dan/dānā Old Persian, not both in both languages.\",\n \"derivation_fa\": \"هر دو ستاکِ این جعبه به‌راستی گواهی‌شده‌اند. در اوستایی ریشهٔ zan- «دانستن، شناختن» هست (paiti.zanənti، frazānaiti، auuazanən)؛ «ز» در ایرانی دنبالهٔ منظمِ *ǵ کامیِ هندواروپایی آغازین است، و ستاکِ حالِ بانونی *ǵn̥-né-h₃-ti در اوستایی zanā-/zānā- شده که همان «zânâ»ی نمودار است. در پارسی باستان همین ستاک با «د» به‌جای «ز» می‌آید: a-dānā «دانست» در بیستون ۱٫۵۱ (کنت). هرن در بند ۵۳۴ همین را می‌نویسد: «پارسی باستان adānā، یعنی ریشهٔ dan- = ریشهٔ آریاییِ źan-» — درست همان جفت‌سازیِ نورایی. «د» آغازینِ پارسی باستان هنوز توضیحِ قطعی ندارد (آمیختگیِ گویشی یا اثرپذیری از dā- «نهادن/دادن»)، ولی چونگ و ویکی‌واژه هر دو صورت را زیرِ یک ریشه (*ǵneh₃-) می‌گذارند. تنها خردهٔ کار برچسبِ زبان است: zan/zānā اوستایی است و dan/dānā پارسی باستان، نه هر دو در هر دو زبان.\",\n \"sources\": [PIE, W + \"%D8%AF%D8%A7%D9%86%D8%B3%D8%AA%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"POK:376\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 31 (IEW p.376): '2. ǵen-, ǵenə-, ǵnē-, ǵnō- \\\"erkennen, kennen\\\" … av. paiti-zānən … apers. 3. Sg. Impf. a-dānā \\\"er wußte\\\" (idg. *ǵn̥-nā-mi), daneben enklit. *ǵn̥-nāmi in: av. zanā-t, zanąn'. Both the Avestan zanā- and the Old Persian a-dānā stand on the cited page.\"},\n  {\"ref\": \"BQT:1298\", \"status\": \"partial\", \"note\": \"Printed p.1298 is Borhan's شناختن entry; its text is in BQT_v3_pages.txt block '[pdf page 85]' (the picofile scan jumps 1294→1299, see data/verification/sources/refs/ocr/BQT/1294.vision.txt). Mo'in's footnote there reads 'شناختن … پهلوی shnâxtan؛ … پارسی باستان xshnâsatiy (شناختن)، کردی zanîn (شناختن) … ورک: هوبشمان ۷۹۲'. It documents the root but gives xšnās-/zanîn, not the forms zānā/dānā, which Mo'in instead pairs in his footnote to زند (see consulted BQT below).\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW s.v. zan-; cf. paiti.zantay- f. 'gute Aufnahme' (BRT.txt line 15063) and the xšnā- footnote at line 10924\", \"stance\": \"supports\", \"note\": \"Bartholomae's note under xšnā- says the stem is 'ein s-Erweiterung aus dem V. zan-; … ai. jijñāsati, jñātaḥ; np. šinâsad \\\"er erkennt\\\", lat. gnōscō' — Avestan zan- 'to know' is the base.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §on non-thematic imperfects (KNT.txt line 2570) and lexicon\", \"stance\": \"supports\", \"note\": \"'Non-thematic: adānā to zānā-, adadā to dā-' — Kent files OP adānā under a stem zānā-, i.e. the same present as Avestan zanā-.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH² 'to know' (CHEUNG.txt line 30113 ff.)\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: zan- \\\"to know\\\" … *OLD PERSIAN: xšnā- (inch.) \\\"to know\\\" = Kent: 182 … impf. IND. 3sg. adāna <a-d-a-n-a> (DB 1.51)'; and '«PIE *ǵneH₃- \\\"to recognize, know\\\" = LIV: 168 ff. | Pok.: 376 ff.»'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 534, p.118 (dānisten)\", \"stance\": \"supports\", \"note\": \"'ap. adānā \\\"er wusste\\\" (ap. √dan- = arisch √źan-); aw. √zan- \\\"wissen\\\", paiti-zānatā; phlv. dān(i)stan, dānāk, dānakīh, dān(i)šn; ai. jñānāti (√jan-)'.\"},\n  {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 264] = printed p.265, s.v. دانستن/دانه\", \"stance\": \"supports\", \"note\": \"Aryanpur lists under one root: اوستایی zan-, پارسی باستان, پهلوی dān-/dānāk, کردی zanîn, بلوچی, سانسکریت jñā/jānāti, لیتوانی žinoti, with the note 'واژهٔ «دانا» نیز از همین واج‌ریشه است. بازگشت به: شناختن.'\"}\n ]\n})\n\ne0_nodes.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"Zand «زند»; zandîq «زندیق»; dânestan «دانستن»; dân «ـدان» (+ دانا ، دانش ؛ سخندان ، کاردان)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three of the four words are straightforward, the fourth is not. زند is Middle Persian zand [znd] 'commentary, explanation, Zend' (MacKenzie 1971), from Old Iranian *zanti- 'knowledge': Nyberg glosses 'zand [znd] knowledge, religious doctrines … esp. the commentary and explication of the Avesta text' and derives it 'Av. (1660) zanti-, cf. s.v. dānistan', and Mo'in's footnote to زند in Borhan says the same ('زند در پهلوی zand (شرح + تفسیر)؛ در اوستا āzanti (شناساندن، معرفت) «بارتولمه ۱۹۹»؛ کلمهٔ اخیر از مصدر zan اوستایی (dan پارسی باستان) بمعنی دانستن و شناختن'). دانستن continues MP dānistan, dān- (MacKenzie s.v.; Abolghasemi FFD p.53: 'دانست < فارسی میانه dānist … دان < فارسی میانه dān < فارسی باستان *dāna-'), the direct heir of OP adānā; دانا, دانش and the suffix ‑دان of سخندان/کاردان are all built on that present stem dān- (MP dānāg 'knowing, wise', dānišn 'knowledge'). زندیق, however, is not a native continuation: MP zandīk 'heretic, Manichaean' (MacKenzie; Nyberg: 'derived from zand … corresponding exactly to Gr. γνωστικός') was taken into Arabic as zindīq (pl. zanādiqa) in the first Islamic centuries as the label for Manichaeans and freethinkers, and re-entered New Persian in that Arabic dress — a Persian→Arabic→Persian round trip the chart does not mark. Worse for the arrow, Mo'in's own footnote in Borhan s.v. زندیک rejects the link with zand 'commentary' altogether: 'ظاهراً این لغت از zanda اوستایی مشتق می‌باشد … هرچند ریشهٔ آن معلوم نیست … و زندیک منسوب به زند است', pointing to Avestan zanda- (a term of abuse, Y. 61.3, Vd. 18.55) whose root is unknown, and citing Kartīr's 3rd-c. inscription at the Kaʿba-ye Zardošt. Hence 'plausible', not 'confirmed'.\",\n \"derivation_fa\": \"از چهار واژهٔ این جعبه سه‌تا روشن است و یکی نه. «زند» همان zand فارسی میانه است، «شرح و تفسیر» (مکنزی؛ نیبرگ: «دانش، آموزه‌های دینی؛ به‌ویژه تفسیر متن اوستا»)، از ایرانی باستان *zanti- «دانش»؛ حاشیهٔ معین بر برهان قاطع نیز همین را می‌گوید: «زند در پهلوی zand (شرح + تفسیر)؛ در اوستا āzanti (شناساندن، معرفت)؛ … از مصدر zan اوستایی (dan پارسی باستان) بمعنی دانستن و شناختن». «دانستن» دنبالهٔ dānistan/dān- فارسی میانه است (ابوالقاسمی، فعل‌های فارسی دری ص ۵۳)، و «دانا، دانش» و پسوندِ «ـدان» در «سخندان، کاردان» همه بر همان ستاکِ حالِ dān- ساخته شده‌اند. اما «زندیق» وام‌واژهٔ برگشتی است: zandīk فارسی میانه («مانوی، بددین») به عربی رفت و zindīq (جمع: زنادقه) شد و از راه عربی دوباره به فارسی نو بازگشت — رفت‌وبرگشتی که نمودار آن را نشان نمی‌دهد. افزون بر این، خودِ معین در حاشیهٔ «زندیک» پیوند آن را با «زندِ» تفسیر رد می‌کند و آن را از zanda اوستایی (دشنامی در یسنا ۶۱٫۳ و وندیداد ۱۸٫۵۵ که ریشه‌اش نامعلوم است) می‌داند و به سنگ‌نبشتهٔ کرتیر در کعبهٔ زردشت ارجاع می‌دهد. پس ادعای نورایی برای سه واژه درست است و برای «زندیق» با احتیاط پذیرفتنی.\",\n \"sources\": [W + \"%D8%B2%D9%86%D8%AF%DB%8C%D9%82\", W + \"%D8%AF%D8%A7%D9%86%D8%B3%D8%AA%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Nourai gives no page. Borhan vol. 2, s.v. زند, Mo'in's footnote 5 (BQT_v2_pages.txt, lines ~29606-29615): 'زند در پهلوی zand (شرح + تفسیر) «اونوالا ۴۴»؛ در اوستا āzanti (شناساندن، معرفت) «بارتولمه ۱۹۹»؛ کلمهٔ اخیر از مصدر zan اوستایی (dan پارسی باستان) بمعنی دانستن و شناختن است که با پیشوند ā در اوستایی صورت āzanti در آمده' — precisely the chart's Avestan/Old Persian → Zand line.\"},\n  {\"ref\": \"FFD:53\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p.53 (FFD_pages.txt after the tag '[pdf page 58]', page head 'ماده‌های ماضی و مضارع فارسی دری … ۵۳'): 'دانستن — دانست < فارسی میانه dānist … دان < فارسی میانه dān < فارسی باستان *dāna- < ایرانی باستان: دانستن'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p.94 (z-) and p.77 (d-)\", \"stance\": \"supports\", \"note\": \"'zand [znd | N ~] commentary, explanation, Zend'; 'zandīk [zndyk' | N ~] heretic, Manichaean. ~īh: heresy'; 'dānistan, dān- [YDʿYTWN-stn'; d'n-stn' | M d'n-ystn, N ~] know. ~išn: knowledge'; 'dānāg [d'n'k' | M d'n'g, N dānā] knowing, wise'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.vv. zand, zandi(k)\", \"stance\": \"partial\", \"note\": \"'zand [znd] knowledge, religious doctrines … Av. (1660) zanti-, cf s.v. dānistan' (supports Zand); but on zandīk: 'The correct form is zandīk … derived from zand (v. above), and corresponding exactly to Gr γνωστικός' — Nyberg makes zandīk a Middle Persian derivative, so the New Persian word must have come back through Arabic, which the chart does not show.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 2, s.v. زندیک, Mo'in's footnote 3 (BQT_v2_pages.txt lines ~29780-29800)\", \"stance\": \"contradicts\", \"note\": \"'ظاهراً این لغت از zanda اوستایی مشتق می‌باشد که دوبار (یسنا ۶۱ بند ۳ و وندیداد ۱۸ بند ۵۵) در اوستا آمده، هرچند ریشهٔ آن معلوم نیست … و زندیک منسوب به زند است … نزد عرب‌زبانان که زندیق (معرب زندیک) … اطلاق گردید' — Mo'in derives zandīk from Av. zanda-, a word of unknown root, not from zan- 'to know'.\"},\n  {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 264] = printed p.265, s.v. دانستن\", \"stance\": \"supports\", \"note\": \"'پهلوی dān-, dānāg … بازگشت به: شناختن' — دانا and دانستن on the same present stem.\"}\n ]\n})\n\ne0_nodes.append({\n \"id\": 3,\n \"lang\": \"Old Persian\",\n \"words\": \"xšnâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian xšnā- 'to know, recognise' is genuinely attested, in the s-inchoative present: DB 1.52 xšnāsātiy 'he shall know' and DNa 42 vadā xšnāsāhy 'thou shalt know thereby'. It reflects PIE *ǵn̥h₃-sḱé-ti, the very *sḱe/o- present Pokorny prints on the cited page ('sḱo-Präs. apers. (Konj.) xšnāsātiy \\\"er soll erkennen\\\"'), Iranian resolving the initial cluster *ǵn- as xšn- (the same treatment gives Avestan xšnā-, ptc. xšnas-). So the box is a legitimate sister of node 1: the same root *ǵneh₃-, but with the inchoative -s- rather than the nasal present.\",\n \"derivation_fa\": \"xšnā- پارسی باستان «شناختن، دانستن» به‌راستی گواهی‌شده است: xšnāsātiy در بیستون ۱٫۵۲ و xšnāsāhy در نقش رستم (DNa ۴۲). این صورت بازتابِ *ǵn̥h₃-sḱé-ti هندواروپایی است، یعنی همان ستاکِ حالِ ـسک که پوکورنی در همان صفحهٔ ۳۷۶/۳۷۷ می‌آورد؛ خوشهٔ آغازینِ *ǵn- در ایرانی به xšn- بدل شده (همین دگرگونی در اوستاییِ xšnā- هم دیده می‌شود). پس این جعبه خواهرِ درستِ گرهٔ ۱ است: یک ریشه، اما با پسوندِ آغازیِ ـس به‌جای ستاکِ بانونی. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%D9%86\", PIE],\n \"ref_check\": [\n  {\"ref\": \"POK:376\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 32 (IEW p.376/377): 'sḱo-Präs. apers. (Konj.) xšnāsātiy \\\"er soll erkennen\\\"; gr. γιγνώσκω … lat. nōscō (gnōscō)' — the Old Persian form is printed on the page Nourai cites.\"},\n  {\"ref\": \"BQT:1298\", \"status\": \"supports\", \"note\": \"Borhan, printed p.1298 s.v. شناختن (BQT_v3_pages.txt block '[pdf page 85]'), Mo'in's footnote: 'شناختن … پهلوی shnâxtan؛ … پارسی باستان xshnâsatiy (شناختن)، کردی zanîn (شناختن) … ورک: هوبشمان ۷۹۲' — the Old Persian form, with exactly Nourai's transcription.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, text of DNa l.42 (KNT.txt line 4105) and lexicon p.182\", \"stance\": \"supports\", \"note\": \"DNa 42 reads 'patikarā : dīdiy : tyaiy : gāθum : baratiy : vadā : xšnāsāhy' — '(then) thou shalt know'; Cheung cites the same lexicon page: 'OLD PERSIAN: xšnā- (inch.) \\\"to know\\\" = Kent: 182'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH² (CHEUNG.txt line 30123)\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: xšnā- (inch.) \\\"to know\\\" = Kent: 182. Pres. {1} inch.: SUBJ. 2sg. xšnāsāhy (DNa 42), 3sg. xšnāsātiy (DB 1.52)'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.v. šnāxtan\", \"stance\": \"supports\", \"note\": \"'Av. (559) xšnā-, pres. xšnas- = OP (Skr. jñā-)' — Nyberg equates the Old Persian and Avestan inchoative stems and the Sanskrit root.\"},\n  {\"src\": \"BRT\", \"where\": \"AiW, footnote under xšnā- (BRT.txt line 10924)\", \"stance\": \"supports\", \"note\": \"'ein s-Erweiterung aus dem V. zan- … ai. jijñāsati, jñātaḥ; np. šinâsad \\\"er erkennt\\\", lat. gnōscō' — the s-stem is built on zan-.\"}\n ]\n})\n\ne0_nodes.append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"šenâxtan «شناختن» (+ آشنا ، شناس)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian شناختن / شناس- is the regular continuation of Middle Persian šnāxtan, šnās- 'to know, recognise' (MacKenzie 1971 s.v.; Nyberg II s.v.), itself from Old Persian xšnā-/xšnās- with the ordinary Middle Iranian loss of the initial x- of the cluster xšn- > šn-, and with the new past stem in -xt- built on the present šnās- (šnās- + -t- > šnāxt-). Persian then prothesises a vowel before the initial cluster: ši-nāxtan. آشنا is the same stem with the prefix ā- (MP āšnāg 'acquainted'), and شناس is the bare present stem used as an agent noun (شناسنده, کارشناس). Nourai's SPG:216 is exactly on target: Spiegel's glossary prints the Old Persian verb and refers the reader to the New Persian word.\",\n \"derivation_fa\": \"«شناختن / شناس-» دنبالهٔ منظمِ šnāxtan، šnās- فارسی میانه است (مکنزی، نیبرگ)، و آن خود از xšnā-/xšnās- پارسی باستان با افتادنِ x در خوشهٔ آغازینِ xšn- (> šn-)؛ ستاکِ گذشتهٔ ـخت از ستاکِ حالِ šnās- + ـت ساخته شده (šnās-t > šnāxt). در فارسی نو پیشِ خوشهٔ آغازین واکه‌ای افزوده شده: شِناختن. «آشنا» همان ستاک با پیشوندِ ā- است (فارسی میانه āšnāg «آشنا») و «شناس» ستاکِ حال در نقشِ اسمِ فاعل (کارشناس، شناسنده). ارجاعِ نورایی به اشپیگل ص ۲۱۶ دقیقاً درست است: اشپیگل در واژه‌نامهٔ خود همین فعل پارسی باستان را می‌آورد و خواننده را به «شناختن» فارسی ارجاع می‌دهد.\",\n \"sources\": [W + \"%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"SPG:216\", \"status\": \"supports\", \"note\": \"Spiegel, Die altpersischen Keilinschriften (2. Aufl. 1881), Glossar p.216 (SPG_keilinschriften1881.txt leaf 187): 'Khshnās … kennen, praes. conj. 2. p. sg. … khshnāsāhadʼish NRa,42. 3. ps. khshnāsātiy Bh. I,52. Cf. شناختن im Neupersischen und den anderen neueranischen Dialekten.' Exactly the arrow drawn.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p.80 s.v. šnāxtan\", \"stance\": \"supports\", \"note\": \"'šnāxtan, šnās- [šnʾhtn', šnʾs- | M xšn-, ʾšnʾs-, N šin-] know, recognize'; also 'šnāsag … knowing, knower; sense'.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.v. šnāxtan (line 3656)\", \"stance\": \"supports\", \"note\": \"'šnāxtan [šnʾhtn'] šnās-, 1st p. sg. šnāsom … to understand, to know, to recognize. — Av. (559) xšnā-, pres. xšnas- = OP (Skr. jñā-); MPrthPrs *šnʾxtn šnāš-; Paz. šnāxtan šnās-, NP šināxtan šinās-.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH² (CHEUNG.txt lines 30128, 30179)\", \"stance\": \"supports\", \"note\": \"'MIDDLE PERSIAN: MMP ʾsnʾs-, BMP šnʾs- /šnās-/ (inch.) \\\"to recognize, get to know\\\"'; '*NWIR: NP šinaxtan/šinās- \\\"to recognize, distinguish\\\", Kurd. nāsin/nās-, … NP dānistan/dān-'.\"},\n  {\"src\": \"BQT\", \"where\": \"printed p.1298 s.v. شناختن (BQT_v3_pages.txt '[pdf page 85]')\", \"stance\": \"supports\", \"note\": \"'شناختن — بکسر اول و فتح پنجم (شناسیدن، گذری). پهلوی shnâxtan؛ … پارسی باستان xshnâsatiy (شناختن)، کردی zanîn … گیلکی shanaxtan … دانستن، معرفت یافتن، وقوف یافتن'.\"}\n ]\n})\n\njson.dump(e0_nodes, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_a.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e0_nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198a.py",
 "description": "Build nodes 1-4"
}
```


### [2026-09-06T02:35:15.928Z] TOOL RESULT

```
ok 4
```


## [2026-09-06T02:37:05.611Z] TOOL CALL #80: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5neh%E2%82%83-\"\nn = []\n\nn.append({\n \"id\": 5,\n \"lang\": \"Sanskrit\",\n \"words\": \"pra-jan\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The meaning given ('one who knows in advance, one who has perception, wise') belongs to Sanskrit prajña- 'wise, knowing' / prajñā- f. 'wisdom, discernment', from pra- 'forth, in advance' + the root jñā- 'to know' (RV+), i.e. PIE *pro- + *ǵneh₃-; Pokorny prints the noun on the page Nourai cites ('gnō-ti- in ai. pra-jñāti-ḥ f. \\\"Erkenntnis\\\"', IEW 377). The printed page, however, shows 'pra-jan' (confirmed on the page image, data/verification/sources/refs/ocr/BOOK/198.png), and pra-jan is not that word: Sanskrit prajan- belongs to the homonymous root jan- 'to be born, beget' (Pokorny's 1. ǵen-, IEW 373-375; 'ai. jā-s \\\"Nachkomme\\\", pra-jā \\\"Nachkommenschaft\\\"'), the root this very entry's '2' is meant to distinguish itself from. Both of Nourai's own sources write the word correctly: Horn no. 815 has 'ai. pra + √jñā-, jñāti- \\\"erkennen, verstehen\\\"' and Mo'in's footnote in Borhan p.1459 has 'هندی باستان pra (پیشوند بمعنی پیش) + jñā, jānāti (شناختن، فهمیدن)'. The extraction is faithful; the misprint is Nourai's own, evidently his habit of rendering the Indic cognate of Iranian zan- as jan-.\",\n \"derivation_fa\": \"معنایی که در جعبه آمده («آنکه از پیش می‌داند، دریابنده، خردمند») از آنِ prajña- سنسکریت است، «دانا، خردمند»، و prajñā- «خرد، بصیرت»؛ ساختِ آن pra- «پیش» + ریشهٔ jñā- «دانستن» است، یعنی *pro- + *ǵneh₃- هندواروپایی. پوکورنی همین اسم را در صفحهٔ ۳۷۷ می‌آورد: «gnō-ti- در سنسکریت pra-jñāti-ḥ \\\"شناخت\\\"». اما آنچه در کتاب چاپ شده «pra-jan» است (بر روی تصویرِ صفحه بررسی شد) و pra-jan واژهٔ دیگری است: از ریشهٔ همنامِ jan- «زادن، زاییدن» (ریشهٔ ۱ نزد پوکورنی، ص ۳۷۳–۳۷۵)، یعنی همان ریشه‌ای که عددِ «۲» در نامِ این مدخل قرار بود آن را جدا کند. هر دو مأخذِ خودِ نورایی صورتِ درست را دارند: هرن بند ۸۱۵ «pra + √jñā-» و حاشیهٔ معین بر برهان قاطع ص ۱۴۵۹ «pra + jñā, jānāti». پس خطا از چاپِ کتاب است، نه از خوانشِ اسکن؛ گویا نورایی همتای هندیِ zan- ایرانی را عادتاً jan- می‌نویسد.\",\n \"error_in\": \"book\",\n \"book_prints\": \"pra-jan\",\n \"correct_form\": \"prajña- / pra-jñā- (root jñā-)\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"POK:377\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 32/33 (IEW p.377): 'gnō-ti- in ai. pra-jñāti-ḥ f. \\\"Erkenntnis\\\", gr. γνῶσις f. \\\"Erkenntnis\\\", lat. nōti-ō f.' — Pokorny's page does carry the pra-jñā- compound, so the reference is right even though the form printed in the chart is not.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"no. 815, p.181 (ferzāne)\", \"stance\": \"partial\", \"note\": \"'ai. pra + √jñā-, jñāti- \\\"erkennen, verstehen\\\"; phlv. frazānak bezw. farzānak' — the correct Sanskrit form, but Horn presents it as a comparison, not a source of the Pahlavi word.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 17.17 KNOW\", \"stance\": \"supports\", \"note\": \"Buck's table for 'know' lists 'Skt. vid-, jñā-' and 'Av. vid-, zan-' — the Indic member of this root is jñā-, not jan-.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō-\", \"stance\": \"silent\", \"note\": \"Watkins gives only the European reflexes of *gnō- (know, can, nōscere, gignōskein …) and no Sanskrit, so it neither supports nor contradicts the Sanskrit form.\"},\n  {\"src\": \"BQT\", \"where\": \"printed p.1459, Mo'in's footnote 2 to فرزان (BQT_v3_pages.txt '[pdf page 252]')\", \"stance\": \"partial\", \"note\": \"'هندی باستان pra (پیشوند بمعنی پیش) + jñā, jānāti (شناختن، فهمیدن)' — this is plainly the source of Nourai's gloss 'one who knows in advance', and it spells the root jñā.\"}\n ]\n})\n\nn.append({\n \"id\": 6,\n \"lang\": \"Pahlavi\",\n \"words\": \"farzânak\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Middle Persian word is real: MacKenzie 1971 p.34 'frazānag [plcʾnk' | P frzng, N farzāna] wise, intelligent' — Nourai's 'farzânak' is Horn's older transcription of the same word ('phlv. frazānak bezw. farzānak', Grundriss no. 815), with -k for the late -g and the New Persian vocalisation far- for fra-. What is wrong is the direction of the arrow. MP frazānag is not borrowed from Sanskrit: it is a native Iranian formation, *fra- 'forth, in advance' + the stem zān- of zan- 'to know' + the adjective suffix -ag, and it is matched by Parthian frzʾng /frazānag/ 'wise, clever' (Cheung, s.v. *zanH², '(+ *fra-) frzʾng \\\"wise\\\"'; DMMPP 161a) — a Parthian word cannot come from Sanskrit. Sanskrit prajña- is therefore a parallel compound of the same two morphemes, a cognate and not an ancestor; that is exactly how Nourai's own two sources put it (Horn 'vergl.', Mo'in 'قس' = 'compare'). Wiktionary states it plainly: 'From Middle Persian frazānag … cognate with Parthian frazānag … Perhaps related to Sanskrit prajñāna'.\",\n \"derivation_fa\": \"خودِ واژهٔ فارسی میانه درست است: مکنزی frazānag «خردمند، دانا» را ثبت کرده و صورتِ «farzânak» نزد نورایی همان خوانشِ کهنِ هرن است (بند ۸۱۵: «پهلوی frazānak یا farzānak»). آنچه نادرست است جهتِ پیکان است. frazānag وام‌واژهٔ سنسکریت نیست، بلکه ساختی ایرانی است: پیشوند *fra- «پیش» + ستاکِ zān- از ریشهٔ zan- «دانستن» + پسوندِ صفت‌سازِ ‑ag؛ و همتای دقیقِ آن در پارتی هست: frazānag «دانا» (چونگ، ذیل *zanH²) — و واژهٔ پارتی نمی‌تواند از سنسکریت آمده باشد. پس prajña- سنسکریت ترکیبِ هم‌ساختِ همان دو تکواژ است، یعنی هم‌ریشه (cognate) نه نیا؛ و هر دو مأخذِ خودِ نورایی هم آن را همین‌گونه آورده‌اند (هرن: «vergl.»؛ معین: «قس»). بنابراین ادعا با احتیاط پذیرفتنی است، به شرط آنکه پیکان را خطِ هم‌ریشگی بخوانیم.\",\n \"sources\": [W + \"%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87\"],\n \"ref_check\": [\n  {\"ref\": \"BQT:1459\", \"status\": \"partial\", \"note\": \"Borhan printed p.1459 (BQT_v3_pages.txt '[pdf page 252]'), Mo'in's footnote 2 to فرزان: 'فرزان (ه.م.). پهلوی frazānak «اونوالا ۹۱۲»؛ هندی باستان pra (پیشوند بمعنی پیش) + jñā, jānāti (شناختن، فهمیدن)، قس: دانستن … «اسشق ۸۱۵»'. The page supports the Pahlavi form and the pra- + jñā- analysis, but 'قس' ('compare') makes the Sanskrit a comparandum, not the source.\"},\n  {\"ref\": \"HRN:181\", \"status\": \"partial\", \"note\": \"Horn, Grundriss no. 815, p.181: 'ferzāne \\\"weise, gelehrt\\\", ferzanegī. ai. pra + √jñā-, jñāti- \\\"erkennen, verstehen\\\"; phlv. frazānak bezw. farzānak. Vergl. dānisten (ar. √zan-), No. 534.' The page is exactly where Nourai points and gives his form farzānak, but Horn's 'vergl.' is a comparison of cognates, not a derivation from Sanskrit.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.34 (PHD.txt line 354)\", \"stance\": \"supports\", \"note\": \"'frazānag [plcʾnk' | P frzng, N farzāna] wise, intelligent'; the index also gives 'intelligent frazānag', 'wise dānāg, frazānag, xradēmand, zīrak'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH², Parthian section (CHEUNG.txt line 27678/30140)\", \"stance\": \"contradicts\", \"note\": \"'*PARTHIAN: ʾšnʾs- … zʾn- \\\"to know\\\" || (+ *ā-) ʾzynd, ʾznd \\\"story\\\" || (+ *fra-) frzʾng \\\"wise\\\" = Ghilain: 82, 84 | DMMPP: … 161a' — the compound is inherited Iranian (fra- + zan-), not a Sanskrit loan.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II glossary (frazand, frazām, fradand entries)\", \"stance\": \"silent\", \"note\": \"Nyberg's King Husrav glossary has frazand 'child' and frazām 'end' but no frazānag, so it says nothing about this word.\"}\n ]\n})\n\nn.append({\n \"id\": 7,\n \"lang\": \"Persian\",\n \"words\": \"Farzâneh «فرزانه» (+ فرزین)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"فرزانه is the regular New Persian outcome of MP frazānag: intervocalic -g of the suffix -ag is lost and the word ends in -a/-eh (frazānag > farzāna), while unstressed fra- becomes far- as in فرمان < framān, فرزند < frazand; the abstract فرزانگی preserves the old -g. Wiktionary analyses the modern word as فرزان (farzân) + ـه (e), i.e. the same stem. The second word in the box, فرزین 'the queen (originally the vizier) at chess', is a different Middle Persian word, frazēn 'guard, (chess) queen' (Wiktionary s.v.; Mo'in's footnote in Borhan p.1459 refers فرزین to فرز, not to فرزان), and its connection with frazānag is a popular association rather than a demonstrated derivation. Hence the box is right for Farzâneh and doubtful for the extra form.\",\n \"derivation_fa\": \"«فرزانه» برآیندِ منظمِ frazānag فارسی میانه است: ‑g پایانیِ پسوندِ ‑ag می‌افتد و واژه به ‑ه ختم می‌شود، و fra- بی‌تکیه به far- بدل می‌گردد، درست مانندِ فرمان < framān و فرزند < frazand؛ «فرزانگی» هنوز آن ‑گ کهن را نگه داشته است. ویکی‌واژه صورتِ امروزی را «فرزان + ـه» تحلیل می‌کند. اما واژهٔ دومِ جعبه، «فرزین» (مهرهٔ شطرنج، در اصل «وزیر»)، واژهٔ دیگری از فارسی میانه است: frazēn «نگهبان، فرزینِ شطرنج»؛ معین هم در حاشیهٔ برهان ص ۱۴۵۹ «فرزین» را به «فرز» ارجاع می‌دهد نه به «فرزان». پیوندِ «فرزین» با «فرزانه» بیشتر ریشه‌شناسیِ عامیانه است. پس ادعای نورایی برای «فرزانه» درست و برای «فرزین» مشکوک است.\",\n \"sources\": [W + \"%D9%81%D8%B1%D8%B2%D8%A7%D9%86%D9%87\", W + \"%D9%81%D8%B1%D8%B2%DB%8C%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own; the parent node's BQT:1459 and HRN:181 were checked there and both give the New Persian outcome (Horn: 'ferzāne \\\"weise, gelehrt\\\", ferzanegī').\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.34\", \"stance\": \"supports\", \"note\": \"'frazānag … N farzāna' — MacKenzie himself gives the New Persian continuant.\"},\n  {\"src\": \"BQT\", \"where\": \"printed p.1459 (BQT_v3_pages.txt '[pdf page 252]')\", \"stance\": \"partial\", \"note\": \"Borhan's headword فرزانه is glossed 'حکیم و دانشمند و عالم و عاقل'; but footnote 3 on the same page reads simply 'فرزین، ورک: فرز' — Mo'in keeps فرزین apart from فرزان/فرزانه.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 815, p.181\", \"stance\": \"supports\", \"note\": \"'ferzāne \\\"weise, gelehrt\\\", ferzanegī … phlv. frazānak bezw. farzānak' — the New Persian word and its abstract.\"}\n ]\n})\n\nn.append({\n \"id\": 8,\n \"lang\": \"Germanic\",\n \"words\": \"know; kunnan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Of the two forms in the Germanic box only kunnan is Germanic. Gothic kunnan 'to know', OHG kunnan 'to know, be able' continue the zero grade *ǵn̥-né-h₃- through the plural forms kunnum/kunnun (Pokorny 376: 'got. kunnan \\\"kennen, wissen\\\" (kann, Prät. kunþa-, Ausgangspunkt die schwundstufigen Pluralformen kunnum, kunnun aus *ǵn̥-nə-mes)'). The other Germanic branch is the *-ye/o- present *knē-a- : OE cnāwan, OHG (ir-, bi-, int-)knāu 'erkenne' (Pok. 377: 'ahd. knāu (*ǵnē-i̯ō), ags. cnāwan (engl. know)'), and Watkins likewise puts 'Germanic *knē(w)- in Old English cnāwan' under gnō-. 'know' as printed is the Modern English shape of that stem, not a Germanic form; the expected entries would be *knēaną / OE cnāwan. The derivation is right, the label is loose.\",\n \"derivation_fa\": \"از دو صورتِ این جعبه تنها kunnan ژرمنی است. kunnan گوتی «دانستن» و kunnan آلمانیِ باستان «دانستن، توانستن» دنبالهٔ درجهٔ صفرِ *ǵn̥-né-h₃- اند، از راهِ صیغه‌های جمعِ kunnum/kunnun (پوکورنی ص ۳۷۶). شاخهٔ دیگرِ ژرمنی ستاکِ *knē-a- است: cnāwan انگلیسیِ کهن و knāu آلمانیِ باستان (پوکورنی ص ۳۷۷: «ahd. knāu، ags. cnāwan (engl. know)»)، و واتکینز نیز «ژرمنیِ *knē(w)- در انگلیسیِ کهنِ cnāwan» را ذیلِ gnō- می‌آورد. اما «know» آن‌گونه که چاپ شده صورتِ انگلیسیِ امروزی است، نه ژرمنی؛ در جای آن باید *knēaną یا cnāwan می‌آمد. پس ریشه‌شناسی درست است و تنها برچسبِ زبان دقیق نیست.\",\n \"sources\": [\"https://www.etymonline.com/word/norm\", PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gnō- 'To know. Contracted from *gnoo-. 1. Variant form *gnē- in Germanic *knē(w)- in Old English cnāwan, to know: KNOW. 2. Zero-grade form *gnō- in: a. Germanic *kunnan in Old English cunnan, to know, know how to, be able to … CAN¹, CON², CUNNING'. Nourai cites AHD without a page; this is the entry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 376-377 (POK_02.txt leaves 31-32)\", \"stance\": \"supports\", \"note\": \"'got. kunnan \\\"kennen, wissen\\\" … ahd. (usw.) starkes Verb kunnan (kann) \\\"wissen, können\\\"'; and 'ahd. knāu (ir-, bi-, int-) \\\"erkenne\\\" (*ǵnē-i̯ō), ags. cnāwan (engl. know) ds.'\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. know (KLN_1971.txt line 131974)\", \"stance\": \"supports\", \"note\": \"'know … fr. OE. cnāwan, rel. to OHG. bi-chnāan, ir-chnāan \\\"to know\\\", Goth. kannjan \\\"to make known\\\", OE. cunnan \\\"to know\\\" … fr. I.-E. base *ǵenə-, *ǵnō- \\\"to know\\\"'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 17.17 KNOW\", \"stance\": \"supports\", \"note\": \"Buck's row for Germanic: 'Goth. witan, kunnan; OE witan, gecnāwan, cunnan; OHG wizzan, cunnan, bi-, ir-cnāan; NE know'.\"}\n ]\n})\n\njson.dump(n, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_b.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(n))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198b.py",
 "description": "Build nodes 5-8"
}
```


### [2026-09-06T02:37:07.543Z] TOOL RESULT

```
ok 4
```


## [2026-09-06T02:39:39.268Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198c.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5neh%E2%82%83-\"\nNORM = \"https://www.etymonline.com/word/norm\"\nn = []\n\nn.append({\n \"id\": 9,\n \"lang\": \"English\",\n \"words\": \"know; can\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English know is OE cnāwan (ME knawen, knowen), from Germanic *knē(w)- < PIE *ǵnē-/*ǵneh₃-; the initial kn- was still pronounced in Middle English and went silent in the 17th c. English can is OE cunnan, 1st/3rd sg. can(n), from Germanic *kunnan, o-grade *ǵon- in the singular, zero grade in the plural cunnon — semantically 'to know how to' > 'to be able to'. Both are Watkins's items 1 and 2a under gnō-, and Klein derives them from the same base. Straight, uncontroversial descent from the Germanic node above.\",\n \"derivation_fa\": \"know انگلیسی همان cnāwan انگلیسیِ کهن است (میانه: knawen, knowen)، از ژرمنیِ *knē(w)- و در نهایت از *ǵneh₃- هندواروپایی؛ خوشهٔ kn- تا انگلیسیِ میانه تلفظ می‌شد و در سدهٔ هفدهم خاموش شد. can نیز cunnan انگلیسیِ کهن است (اول‌شخص و سوم‌شخصِ مفرد can)، از ژرمنیِ *kunnan؛ معنایش از «دانستنِ چگونگی» به «توانستن» رفته است. واتکینز هر دو را ذیلِ gnō- می‌آورد و کلاین نیز آن‌ها را از همین ریشه می‌گیرد. زنجیره روشن و بی‌مناقشه است و ادعای نورایی درست.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own; the parent's AHD citation covers it (Watkins s.v. gnō-, items 1 and 2a: '… Old English cnāwan, to know: KNOW'; '… Old English cunnan … CAN¹').\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.vv. know, can (KLN_1971.txt lines 131974 ff.)\", \"stance\": \"supports\", \"note\": \"'know … fr. OE. cnāwan … fr. I.-E. base *ǵenə-, *ǵnō- \\\"to know\\\". See can, aux. v.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō-\", \"stance\": \"supports\", \"note\": \"'1. … Old English cnāwan, to know: KNOW. 2. Zero-grade form *ǵnō- in: a. Germanic *kunnan in Old English cunnan … (Old English first and third singular can from Germanic *kann from o-grade *ǵon-): CAN¹, CON², CUNNING'.\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. know\", \"stance\": \"supports\", \"note\": \"Skeat likewise takes know from AS. cnáwan and compares Lat. (g)noscere, Gk. gignōskein, Skt. jñā-.\"}\n ]\n})\n\nn.append({\n \"id\": 10,\n \"lang\": \"Latin\",\n \"words\": \"gnôcere, nôcere 1; î-gnôrâre; nôbilis; norma\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Three of the four are sound, one form is misprinted and one etymology is bracketed even by the source Nourai cites. (a) The first entry should read gnōscere, nōscere 'to get to know' (< *ǵnē-sḱ-, Pokorny 376 'lat. nōscō (gnōscō) \\\"erkenne\\\"'); the book prints 'gnôcere, nôcere' with no -s-, verified on the page image (data/verification/sources/refs/ocr/BOOK/198.png) — the extraction is faithful, the error is the book's. (b) î-gnôrâre is Nourai's morpheme-split spelling of ignōrāre 'not to know' (in- negative, whence his cross-reference to root 'Ne 1'), from *ǵn̥-ro- gnārus 'knowing'; correct. (c) nōbilis 'well known, noble' < *gnō-dhli- (Watkins item 5; Pokorny 378 'lat. (g)nōbilis \\\"kennbar, bekannt; vornehm, edel\\\"'); correct. (d) norma 'carpenter's square, rule' is the doubtful one: Pokorny p.378 himself derives it not from Latin but from the accusative of Greek γνώμων ('vom Akk. γνώμονα aus, auch norma'), Klein makes it a borrowing 'prob. through the medium of the Etruscans' of Greek gnōmōn, Etymonline calls it 'a word of unknown origin', and Watkins — Nourai's own reference for this box — parenthesises it: '(8. Traditionally but improbably referred here are: a. Latin nota … b. Latin norma …)'. So norma belongs under the Greek node at best, not directly under Latin.\",\n \"derivation_fa\": \"از چهار واژه سه‌تا استوارند، یکی غلطِ چاپی است و یکی حتی نزدِ مأخذِ خودِ نورایی مشکوک. (الف) صورتِ نخست باید gnōscere, nōscere «شناختن، دانستن» باشد (< *ǵnē-sḱ-؛ پوکورنی ص ۳۷۶: «lat. nōscō (gnōscō)»)؛ کتاب «gnôcere, nôcere» بدونِ ـس چاپ کرده است — بر تصویرِ صفحه بررسی شد: خطای چاپِ کتاب است نه خطای خوانشِ اسکن. (ب) «î-gnôrâre» همان ignōrāre است که نورایی تکواژها را از هم جدا نوشته (پیشوندِ نفیِ in-، و از همین رو ارجاع به ریشهٔ Ne 1)؛ درست است. (ج) nōbilis «شناخته، نامدار، شریف» از *gnō-dhli- (پوکورنی ص ۳۷۸)؛ درست است. (د) اما norma «گونیا، قاعده» مسئله‌دار است: خودِ پوکورنی در ص ۳۷۸ آن را نه لاتینیِ ارثی، بلکه گرفته‌شده از حالتِ مفعولیِ γνώμονα یونانی می‌داند؛ کلاین آن را وام‌واژه‌ای «احتمالاً به میانجیِ اتروسکی» از gnōmōn یونانی می‌خواند؛ اتیمانلاین «ریشه‌اش نامعلوم» می‌نویسد؛ و واتکینز — یعنی همان مأخذی که نورایی برای این جعبه آورده — آن را در کمانک می‌گذارد: «به‌طورِ سنتی اما نادرست به این ریشه بازبرده شده‌اند: nota و norma». پس norma دستِ‌بالا زیرِ گرهِ یونانی جای دارد، نه مستقیماً زیرِ لاتین.\",\n \"error_in\": \"book\",\n \"book_prints\": \"gnôcere, nôcere 1\",\n \"correct_form\": \"gnōscere, nōscere\",\n \"sources\": [NORM, PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. gnō- supports items 3-5 exactly ('3. Suffixed form *ǵnē-sko- in Latin (g)nōscere, cognōscere … 4. Suffixed form *ǵnē-ro- in Latin ignōrāre, not to know … 5. Suffixed form *ǵnō-dhli- in Latin nōbilis … NOBLE'), but explicitly brackets norma: '(8. Traditionally but improbably referred here are: a. Latin nota … b. Latin norma, carpenter's square, rule, pattern, precept: NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.)'\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 376 and 378 (POK_02.txt leaves 32-33)\", \"stance\": \"partial\", \"note\": \"'lat. nōscō (gnōscō) \\\"erkenne\\\", ignōscō'; 'lat. gnārus \\\"einer Sache kundig\\\", ignārus \\\"unkundig\\\" … ignōrō'; 'lat. (g)nōbilis \\\"kennbar, bekannt; vornehm, edel\\\" (Adjektivierung eines *ǵnō-dhlom)'. But for norma: 'gr. γνῶμα \\\"Erkennungszeichen; Winkelmaß\\\" (daraus lat. grōma … und, vom Akk. γνώμονα aus, auch norma \\\"Winkelmaß, Richtschnur, Vorschrift, Regel\\\")' — a Greek loan.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. norm (KLN_1971.txt line 162770)\", \"stance\": \"partial\", \"note\": \"'norm … L. norma, \\\"carpenter's square, rule, pattern\\\", borrowed — prob. through the medium of the Etruscans — fr. Gk. γνώμονα, acc. of γνώμων \\\"carpenter's square\\\", lit. \\\"one who, that which, knows\\\"' — same root, but through Greek and Etruscan.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt), searched for 'norma'\", \"stance\": \"silent\", \"note\": \"grep of the OCR text for 'norma' returns only French occurrences of 'normal(e)' in the running prose; the dictionary entry itself is not recoverable from this scan.\"}\n ]\n})\n\nn.append({\n \"id\": 11,\n \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box: the Latin words reached Persian through French, which is historically correct for the three loanwords in the next node. French inherited/borrowed norme and normal from Latin norma/normālis, note from Latin nota, and noble from Latin nōbilis (Old French noble, 11th c.); it is these French shapes — with French final stress and the vowel of note — that were taken into Persian in the 19th-20th centuries, not the Latin ones.\",\n \"derivation_fa\": \"این جعبه تهی و تنها گذرگاه است: واژه‌های لاتینی از راهِ فرانسه به فارسی رسیده‌اند و این از نظرِ تاریخی درست است. فرانسه norme و normal را از norma/normālis لاتین، note را از nota، و noble را از nōbilis لاتین (فرانسهٔ کهن noble، سدهٔ یازدهم) گرفته است؛ و همین صورت‌های فرانسوی — با تکیهٔ پایانی و واکهٔ note — بودند که در سدهٔ نوزدهم و بیستم به فارسی وام داده شدند، نه صورت‌های لاتینی.\",\n \"sources\": [NORM],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Pass-through node with no reference of its own.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.vv. norm, normal, noble\", \"stance\": \"supports\", \"note\": \"'normal … L. normālis, \\\"made according to a carpenter's square\\\", fr. norma'; norm is given as entering English from Latin via French usage; noble is derived from OF. noble < L. nōbilis.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō-\", \"stance\": \"supports\", \"note\": \"The English words NOTE, NORM, NORMAL, NOBLE are all routed through Old French in Watkins's lists, which is the same French stage the chart draws.\"}\n ]\n})\n\nn.append({\n \"id\": 12,\n \"lang\": \"Persian\",\n \"words\": \"normâl «نُرمال»; not «نُت ، نوت»; nobel «نوبل»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three are modern European loans that entered Persian in the Qajar-Pahlavi period, mostly through French-medium schooling (Dār al-Fonun) and translation. نرمال is French normal 'normal, standard' — Mo'in's dictionary carries it and even flags it as an unwanted foreign word ('نرمال: (ص.) معمولی؛ عادی … احتراز از استعمال این کلمهٔ بیگانه اولی است'); نت (also نوت) is French note in its musical sense; نوبل is French noble. The chain French < Latin < *ǵneh₃- is right for نرمال and نوبل; for نت it inherits the doubt attached to Latin nota (Watkins brackets it as 'traditionally but improbably referred here'). The spelling نوبل is also the Persian rendering of the surname Nobel (جایزهٔ نوبل), so the box can be misread. Nourai's page reference could not be verified: MON:4704 is in Mo'in's vol. 4 (foreign words), and neither the online Mo'in nor the 2-volume abridgement on disk carries the print pagination.\",\n \"derivation_fa\": \"هر سه وام‌واژهٔ اروپاییِ نو هستند که در دورهٔ قاجار و پهلوی، بیشتر از راهِ فرانسه (دارالفنون و ترجمه)، وارد فارسی شده‌اند. «نرمال» از normal فرانسوی است؛ معین آن را ثبت کرده و حتی هشدار داده است: «نرمال: معمولی؛ عادی … احتراز از استعمال این کلمهٔ بیگانه اولی است». «نت» (و «نوت») از note فرانسوی در معنای موسیقایی، و «نوبل» از noble فرانسوی. زنجیرهٔ فرانسه < لاتین < *ǵneh₃- برای «نرمال» و «نوبل» درست است؛ اما «نت» همان تردیدی را به ارث می‌برد که بر nota لاتین هست (واتکینز آن را «به‌طور سنتی اما نادرست» به این ریشه بازبرده می‌داند). ضمناً «نوبل» در فارسی بیشتر نامِ خانوادگیِ آلفرد نوبل (جایزهٔ نوبل) را به یاد می‌آورد. ارجاعِ نورایی به معین ج ۴ ص ۴۷۰۴ را نتوانستم بسنجم، چون شماره‌صفحهٔ چاپیِ فرهنگِ معین نه در نسخهٔ برخط و نه در تلخیصِ دوجلدیِ موجود قابلِ ردیابی نیست.\",\n \"sources\": [NORM],\n \"ref_check\": [\n  {\"ref\": \"MON:4704\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 4 (foreign words/compounds) is not paginated in any copy on disk; the 2-vol abridgement (MON_part2.txt line 75244) does carry 'نرمال: ۱ (ص.) معمولی؛ عادی — ضح. احتراز از استعمال این کلمهٔ بیگانه اولی است', so the word is in Mo'in, but the page number 4704 could not be checked.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi, s.v. نرمال (MON_part2.txt line 75244)\", \"stance\": \"supports\", \"note\": \"'نرمال: ۱ (ص.) معمولی؛ عادی. ضح. - احتراز از استعمال این کلمهٔ بیگانه اولی است.' — Mo'in registers it as a foreign (European) word.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.vv. normal, noble, note\", \"stance\": \"supports\", \"note\": \"'normal … L. normālis … fr. norma'; note < OF. note < L. nota — the French links the chart draws are the standard ones.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō- item 8\", \"stance\": \"partial\", \"note\": \"'(8. Traditionally but improbably referred here are: a. Latin nota … NOTE; b. Latin norma … NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.)' — the ultimate root of نرمال and نت is doubted by Nourai's own source.\"}\n ]\n})\n\nn.append({\n \"id\": 13,\n \"lang\": \"English\",\n \"words\": \"note; notify; notorious; acquaint; recognize; ignore; noble; norm; normal; abnormal; enormous\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Watkins's entry gnō- yields most of this list verbatim: item 3 (*ǵnē-sḱo- > Latin (g)nōscere, cognōscere) gives NOTICE, NOTIFY, NOTION, NOTORIOUS, ACQUAINT, COGNITION, RECOGNIZE; item 4 (ignōrāre) gives IGNORANT, IGNORE; item 5 (nōbilis) gives NOBLE. But the same entry brackets the rest: '(8. Traditionally but improbably referred here are: a. Latin nota, a mark, note …: NOTE; ANNOTATE, CONNOTE …; b. Latin norma …: NORM, NORMA, NORMAL; ABNORMAL, ENORMOUS.)' — so four of the eleven words (note, norm, normal, abnormal, enormous) are exactly the ones Watkins declines to attach to the root. Klein and Pokorny take the milder line that norma is a Greek loan from γνώμων, hence still ultimately of this root but not by direct Latin descent; note/nota is the weaker case. The list is therefore right in the main and over-inclusive at the edges.\",\n \"derivation_fa\": \"مدخلِ gnō- نزد واتکینز بیشترِ این فهرست را واژه‌به‌واژه می‌دهد: بندِ ۳ (*ǵnē-sḱo- > لاتینِ nōscere, cognōscere) واژه‌های NOTICE، NOTIFY، NOTION، NOTORIOUS، ACQUAINT، RECOGNIZE را؛ بندِ ۴ (ignōrāre) واژهٔ IGNORE را؛ و بندِ ۵ (nōbilis) واژهٔ NOBLE را. اما همان مدخل بقیه را در کمانک می‌گذارد: «به‌طور سنتی اما نادرست به این ریشه بازبرده شده‌اند: nota لاتین > NOTE و norma لاتین > NORM, NORMAL, ABNORMAL, ENORMOUS». پس چهار واژه از یازده واژهٔ این جعبه دقیقاً همان‌هایی هستند که واتکینز از ریشه جدا می‌کند. کلاین و پوکورنی نرم‌تر می‌گویند: norma وام‌واژه‌ای از γνώμων یونانی است، پس در نهایت از همین ریشه اما نه با وراثتِ مستقیمِ لاتینی. بنابراین فهرست در کلیت درست و در حاشیه‌ها فراخ‌تر از حد است.\",\n \"sources\": [NORM],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; the parent Latin box's AHD citation was checked there and is quoted above.\"}],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō- (AHD_watkins1985.txt line 527 ff.)\", \"stance\": \"partial\", \"note\": \"Items 3-5 list NOTICE, NOTIFY, NOTION, NOTORIOUS, (ACQUAINT), COGNITION, RECOGNIZE, IGNORANT, IGNORE, NOBLE; item 8 brackets NOTE, NORM, NORMA, NORMAL, ABNORMAL, ENORMOUS as 'traditionally but improbably referred here'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.vv. norm, normal, note\", \"stance\": \"partial\", \"note\": \"'norm … L. norma … borrowed — prob. through the medium of the Etruscans — fr. Gk. γνώμονα' — for Klein the norm-family does reach the root, but through Greek.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 378\", \"stance\": \"partial\", \"note\": \"'gr. γνῶμα … (daraus lat. grōma … und, vom Akk. γνώμονα aus, auch norma …)' and, on nota, 'besser über ἀγνοέω … und lat. nota (zu ὄνοσθαι \\\"tadeln\\\") jetzt Leumann, Homer. Wörter 228' — Pokorny too questions nota.\"}\n ]\n})\n\nn.append({\n \"id\": 14,\n \"lang\": \"Greek\",\n \"words\": \"gignôskein\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek γιγνώσκειν 'to know, perceive, judge' is the reduplicated *sḱe/o- present *ǵi-ǵnh₃-sḱe/o-, the exact Greek counterpart of Latin (g)nōscere and of Old Persian xšnāsātiy in node 3 — Pokorny prints the three together on p.376 ('gr. γιγνώσκω, epir. γνώσκω \\\"erkenne\\\", lat. nōscō (gnōscō) \\\"erkenne\\\"'), and Watkins gives 'Reduplicated and suffixed form *gi-gnō-sko- in Greek gignōskein, to know, think, judge'. Aorist ἔγνων, perfect ἔγνωκα, verbal adj. γνωτός.\",\n \"derivation_fa\": \"γιγνώσκειν یونانی «شناختن، دریافتن، داوری کردن» همان ستاکِ حالِ دوگان‌شده با پسوندِ ـسک است: *ǵi-ǵnh₃-sḱe/o-، یعنی برابرِ دقیقِ nōscere لاتین و xšnāsātiy پارسی باستان در گرهِ ۳. پوکورنی هر سه را در صفحهٔ ۳۷۶ کنارِ هم می‌آورد و واتکینز می‌نویسد: «صورتِ دوگان‌شده و پسونددارِ *gi-gnō-sko- در یونانیِ gignōskein». گذشتهٔ ساده ἔγνων، ماضیِ نقلی ἔγνωκα و صفتِ مفعولی γνωτός. ادعای نورایی درست است.\",\n \"sources\": [PIE],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. gnō- item 6: 'Reduplicated and suffixed form *gi-gnō-sko- in Greek gignōskein, to know, think, judge (and *gnō- in gnōmōn, a judge, interpreter): GNOME², GNOMON, GNOSIS; AGNOSIA, DIAGNOSIS, PATHOGNOMIC, PHYSIOGNOMY, PROGNOSIS.'\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW 376 (POK_02.txt leaf 32)\", \"stance\": \"supports\", \"note\": \"'sḱo-Präs. apers. (Konj.) xšnāsātiy \\\"er soll erkennen\\\"; gr. γιγνώσκω, epir. γνώσκω \\\"erkenne\\\", lat. nōscō (gnōscō) \\\"erkenne\\\"'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 17.17 KNOW\", \"stance\": \"supports\", \"note\": \"Buck's Greek row: 'Grk. οἶδα, ἐπίσταμαι, γιγνώσκω'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein s.v. gnostic (KLN_1971.txt line 104060)\", \"stance\": \"supports\", \"note\": \"'Gk. γνωστικός \\\"of knowing\\\", fr. γνωστός \\\"known, perceived, understood\\\", a later collateral form of γνωτός, verbal adj. of γιγνώσκειν, \\\"to know\\\"'.\"}\n ]\n})\n\nn.append({\n \"id\": 15,\n \"lang\": \"English\",\n \"words\": \"gnosis; diagnosis\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"gnosis is Modern Latin gnosis from Greek γνῶσις 'knowledge, enquiry', the ti-abstract *ǵnō-ti- of the same root (Pokorny 377 lists it beside Sanskrit pra-jñāti-ḥ and Latin nōtiō); in English it is a 17th-19th c. learned borrowing used of the esoteric knowledge of the Gnostics (γνωστικοί). diagnosis is Modern Latin from Greek διάγνωσις 'discernment, distinguishing', dia- 'apart, through' + gnōsis, medicalised in English from 1680s. The AHD:563 that Nourai cites is a page of the main dictionary (the g- pages), not of the Indo-European appendix, and the New College edition is not on disk; the appendix entry gnō- nevertheless lists GNOSIS and DIAGNOSIS explicitly.\",\n \"derivation_fa\": \"gnosis از لاتینِ نو gnosis و آن از γνῶσις یونانی «شناخت، پژوهش» است، یعنی اسمِ معنایِ *ǵnō-ti- از همین ریشه (پوکورنی ص ۳۷۷ آن را کنارِ pra-jñāti-ḥ سنسکریت و nōtiō لاتین می‌آورد)؛ در انگلیسی وام‌واژه‌ای دانشورانه است که برای دانشِ رازآمیزِ گنوسیان (γνωστικοί) به کار می‌رود. diagnosis نیز از διάγνωσις یونانی «تمییز، بازشناسی» است: dia- «از میان، جدا» + gnōsis، که از دههٔ ۱۶۸۰ در انگلیسی معنای پزشکی گرفت. ارجاعِ نورایی «AHD:563» به صفحهٔ خودِ فرهنگِ امریکن هریتیج (بخشِ g) است نه به پیوستِ ریشه‌های هندواروپایی، و آن چاپ روی دیسک نیست؛ ولی مدخلِ gnō- در پیوست هر دو واژه را صریحاً نام می‌برد.\",\n \"sources\": [PIE],\n \"ref_check\": [\n  {\"ref\": \"AHD:563\", \"status\": \"not_checked\", \"note\": \"p.563 belongs to the body of the American Heritage Dictionary, New College Edition (the g- pages), which is only available as a lending scan on archive.org; not checked. The Watkins appendix on disk does list 'GNOSIS' and 'DIAGNOSIS' under gnō- item 6, which is the substance of the claim.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein s.vv. gnosis, diagnosis (KLN_1971.txt lines 104055, 70186)\", \"stance\": \"supports\", \"note\": \"'gnosis, n., knowledge, especially that claimed by the Gnostics. — ModL. gnosis, fr. Gk. γνῶσις, \\\"knowledge\\\" … cp. diagnosis, prognosis'.\"},\n  {\"src\": \"POK\", \"where\": \"IEW 377\", \"stance\": \"supports\", \"note\": \"'gnō-ti- in ai. pra-jñāti-ḥ f. \\\"Erkenntnis\\\", gr. γνῶσις f. \\\"Erkenntnis\\\", lat. nōti-ō f.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gnō- item 6\", \"stance\": \"supports\", \"note\": \"'… Greek gignōskein … GNOME², GNOMON, GNOSIS; AGNOSIA, DIAGNOSIS …'\"}\n ]\n})\n\njson.dump(n, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_c.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(n))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198c.py",
 "description": "Build nodes 9-15"
}
```


### [2026-09-06T02:39:41.286Z] TOOL RESULT

```
ok 7
```


## [2026-09-06T02:41:51.753Z] TOOL CALL #82: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198final.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nS = '/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5neh%E2%82%83-\"\nGAZAR = W + \"%DA%AF%D8%B2%D8%B1\"\n\nnodes0 = json.load(open(S+'part_a.json')) + json.load(open(S+'part_b.json')) + json.load(open(S+'part_c.json'))\n# fix node 8 sources\nfor nd in nodes0:\n    if nd[\"id\"] == 8:\n        nd[\"sources\"] = [PIE]\nassert [nd[\"id\"] for nd in nodes0] == list(range(1,16)), [nd[\"id\"] for nd in nodes0]\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Gnô, Gen, Gene 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ǵneh₃- 'to know, recognize' (Pokorny: 2. ǵen-, ǵenə-, ǵnē-, ǵnō-; LIV 168 f.)\",\n \"note\": \"Pokorny IEW 376-378 heads the entry '2. ǵen-, ǵenə-, ǵnē-, ǵnō- \\\"erkennen, kennen\\\"', so Nourai's three-part root name, the language label and the gloss 'to know' are all accurate, and his '2' is Pokorny's own numeral, which keeps this root apart from 1. ǵen- 'beget' (IEW 373-375). Watkins/AHD gives the same root as 'gnō-. To know. [Pok. 2. gen- 376]', Walde-Pokorny I 578 as '2. (ǵen-), ǵenē-, ǵenō- \\\"erkennen, kennen\\\"', Cheung as '«PIE *ǵneH₃- \\\"to recognize, know\\\" = LIV: 168 ff. | Pok.: 376 ff.»'. The Iranian side of the chart is unusually well documented: Pokorny's own page 376 prints both Avestan zanā- and Old Persian a-dānā, and page 376/377 the inchoative xšnāsātiy, so nodes 1, 3 and 4 are exactly what the cited page says. Two weaknesses run through the rest: the Sanskrit box (node 5) is misprinted and is drawn as the ancestor of the Pahlavi word although both Horn and Mo'in present it as a mere cognate (node 6); and the Latin/English boxes carry the norma/nota family, which Nourai's own reference, Watkins, brackets as 'traditionally but improbably referred here'.\",\n \"note_fa\": \"پوکورنی در صفحهٔ ۳۷۶ فرهنگِ خود مدخل را چنین می‌آورد: «۲. ǵen-, ǵenə-, ǵnē-, ǵnō- \\\"شناختن، دانستن\\\"»؛ پس نامِ سه‌بخشیِ ریشه نزد نورایی، برچسبِ زبان و معنای «to know» هر سه درست است، و عددِ «۲» نیز از خودِ پوکورنی است و این ریشه را از ریشهٔ ۱ (ǵen- «زادن») جدا می‌کند. واتکینز همین را «gnō-، دانستن [پوکورنی ۳۷۶]» می‌نویسد، والده‑پوکورنی جلد ۱ ص ۵۷۸ همان‌گونه، و چونگ نیز «*ǵneH₃- = LIV ۱۶۸ | پوکورنی ۳۷۶». بخشِ ایرانیِ نمودار به‌ویژه مستند است: در همان صفحهٔ ۳۷۶ هم zanā- اوستایی و هم a-dānā پارسی باستان و هم xšnāsātiy آمده است، پس گره‌های ۱ و ۳ و ۴ دقیقاً همان‌اند که مأخذ می‌گوید. دو نقطهٔ سست هست: جعبهٔ سنسکریت (گرهٔ ۵) هم غلطِ چاپی دارد و هم نیایِ واژهٔ پهلوی نمایانده شده، حال آنکه هرن و معین آن را تنها هم‌ریشه می‌دانند؛ و جعبه‌های لاتین و انگلیسی خانوادهٔ norma/nota را در خود دارند که خودِ واتکینز — مأخذِ نورایی — آن را «به‌طور سنتی اما نادرست به این ریشه بازبرده» می‌شمارد.\",\n \"sources\": [PIE, W + \"%D8%AF%D8%A7%D9%86%D8%B3%D8%AA%D9%86\", W + \"%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n  {\"ref\": \"POK:376\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 31 (IEW p.376, printed page marker '376' on that leaf): '2. ǵen-, ǵenə-, ǵnē-, ǵnō- \\\"erkennen, kennen\\\"; Nominalbildungen: ǵnō-mn̥ \\\"Kennzeichen\\\", ǵnō-ter- \\\"Kenner\\\", ǵnō-ti- \\\"Erkenntnis\\\", ǵnō-to-s \\\"bekannt\\\" … zur Vermeidung der Homonymie mit 1. ǵen- werden vielfach Verbalformen mit ǵnō- verwendet.' Exactly the root box as drawn, numeral included.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 578 (WLD_Bd1_1930_djvu.txt line 36400)\", \"stance\": \"supports\", \"note\": \"'2. (ǵen-), ǵenē-, ǵenō- \\\"erkennen, kennen\\\"' — the older edition Pokorny abridges (he cites 'WP. I 578ff.' at the end of the entry).\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 527)\", \"stance\": \"supports\", \"note\": \"'gnō-. To know. Contracted from *gnoo-. … [Pok. 2. gen- 376.]' — same root, same Pokorny page.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *zanH² (CHEUNG.txt line 30205 ff.)\", \"stance\": \"supports\", \"note\": \"'This root has an impeccable IE etymology. «PIE *ǵneH₃- \\\"to recognize, know\\\" = LIV: 168 ff. | Pok.: 376 ff.» IE COGNATES: Gr. γιγνώσκω, Lat. noscere, OCS znati, Lith. žinoti, Arm. canea-, Goth. kunnan, Engl. to know.'\"},\n  {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms 17.17 KNOW (SYN.txt line 30387)\", \"stance\": \"supports\", \"note\": \"Buck's table for 'know' aligns Grk. γιγνώσκω, Lat. nōscere/cognōscere, Goth. kunnan, NE know, Skt. jñā-, Av. zan-, Lith. žinoti — the same set the chart draws.\"}\n ],\n \"nodes\": nodes0\n}\n\nentry1 = {\n \"entry\": 1,\n \"root\": \"Gogel, Gogelos\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"no such Indo-European root is generally recognised; Mann's private reconstruction *gogolos, -ios (gogəl-) 'knob, tapering object'\",\n \"note\": \"The root box is a faithful copy of one line of Stuart Mann's Indo-European Comparative Dictionary — 'gogolos, -ios (gogəl-) \\\"knob, tapering object\\\": Per. gazar \\\"carrot\\\"; Arm. kakγi (\\\"lime-tree\\\", fr. the fruit); OS kakeli \\\"icicle\\\"?' — which is why Nourai's root name pairs 'Gogel' (Mann's variant gogəl-) with 'Gogelos'. But Mann's dictionary is a one-man work whose reconstructions are frequently not accepted, and this one is nowhere else: Pokorny's IEW has no such entry (his nearest g-o-g items are gag-/gog- 'to cackle' and the Albanian gogelë 'ball, gall-apple' under gel-), Walde-Pokorny has nothing, Watkins/AHD has nothing, and Mann himself flags the Old Saxon comparandum with a question mark. Since the whole root rests on two words, one of which (Persian gazar) is now derived quite differently and the other (the Armenian) I could not confirm at all, the root as such must be called disputed. Note also that the entry stands on p.288 of the Mann scan (the leaf carrying pp. 288-289), one page after Nourai's 'IEC:287'.\",\n \"note_fa\": \"این جعبهٔ ریشه رونوشتِ وفادارِ یک سطر از فرهنگِ تطبیقیِ هندواروپاییِ استوارت مان است: «gogolos, -ios (gogəl-) \\\"برآمدگی، چیزِ باریک‌شونده\\\": فارسی gazar \\\"هویج\\\"؛ ارمنی kakγi (\\\"درختِ زیرفون\\\"، از شکلِ میوه)؛ ساکسونیِ کهن kakeli \\\"قندیل\\\"؟» — و از همین‌رو نامِ ریشه نزد نورایی «Gogel» (همان گونهٔ gogəl- مان) در کنارِ «Gogelos» آمده است. اما فرهنگِ مان کارِ یک‌تنه‌ای است که بازسازی‌هایش را غالباً نپذیرفته‌اند، و این یکی در هیچ جای دیگر نیست: پوکورنی چنین مدخلی ندارد، والده‑پوکورنی ندارد، واتکینز ندارد، و خودِ مان همتای ساکسونیِ کهن را با علامتِ پرسش آورده است. چون کلِ ریشه بر دو واژه استوار است که یکی (gazar فارسی) امروز به‌گونهٔ دیگری ریشه‌یابی می‌شود و دیگری (واژهٔ ارمنی) اصلاً تأیید نشد، باید این ریشه را «ردشده/مورد مناقشه» شمرد. یادآوری: مدخلِ مان در اسکنِ موجود در صفحهٔ ۲۸۸ است (برگی که صفحه‌های ۲۸۸ و ۲۸۹ را دارد)، یک صفحه پس از «IEC:287» که نورایی داده است.\",\n \"sources\": [GAZAR],\n \"ref_check\": [\n  {\"ref\": \"IEC:287\", \"status\": \"supports\", \"note\": \"Mann, IEC, printed p.288 (IEC.txt leaf 171, line 4216; the leaf carries the page markers 288 and 289, the entry standing before the '288' marker): 'gogolos, ios (gogəl-) \\\"knob, tapering object\\\" Per. gazar \\\"carrot\\\"; Arm. kakγi (\\\"lime-tree\\\", fr. the fruit); OS kakeli \\\"icicle\\\"?'. The chart reproduces the line exactly; the page is 288, one off Nourai's 287.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW, g-section (grep 'gogel', 'gog-' in POK_01/02/03/full)\", \"stance\": \"silent\", \"note\": \"No root *gogel-/*gogolos anywhere. The only hits are 'Root/lemma: gag- gog-' (onomatopoeic 'cackle', with russ. gogotátʼ, gógolʼ) and, under gel- 'ball, lump', 'alb. gogelë \\\"Kugel, Ball; Gallapfel\\\" (*gel-gal-na)' at IEW 357 — a different formation, and not connected with carrots.\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I (WLD_Bd1 djvu, grep 'gogel')\", \"stance\": \"silent\", \"note\": \"Only 'MHG gogel …' under the Germanic 'wanton, prank' words and the same Albanian gogelë 'Kugel, Ball; Gallapfel (*gal-galnu)' — no 'knob, tapering object' root.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list\", \"stance\": \"silent\", \"note\": \"The list runs gleubh-, glōgh-, gnō-, gras-, grat-, gravo-, greut-… — no gog-/gogel- root at all.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1,\n   \"lang\": \"Persian\",\n   \"words\": \"gazar «گَزَر»\",\n   \"verdict\": \"disputed\",\n   \"derivation\": \"گزر 'carrot' is a real Persian word (Borhan, Mo'in s.v. گزر = Daucus carota; still the ordinary word in Gilaki, Kurdish gêzer, Balochi gizirk, Pashto gāzara, and the source of Arabic جزر jazar), but its origin is not a PIE *gogolos. Wiktionary reconstructs it as inherited from Middle Persian *gazar and sets it beside a striking Near-Eastern cluster: Sanskrit गार्जर gārjara, Classical Syriac ܓܙܪܐ gezzārāʾ, Hebrew גֶּזֶר gézer, all 'carrot', plus the Turkic borrowings kişer/käşir. A word shared in that shape by Iranian, Indic, Aramaic and Hebrew is a cultivated-plant Wanderwort of the Near East, not an inherited Indo-European noun; the carrot itself is a domesticate of the Iranian plateau spread in historical times. Mann's *gogolos 'knob, tapering object', built on the shape of the root, is a private etymology with no support outside his own dictionary, and 'g-z-r' beside Semitic gzr also invites (though it does not prove) a link with the root 'to cut'. Modern scholarship therefore prefers a different origin.\",\n   \"derivation_fa\": \"«گزر» واژه‌ای اصیل و زنده در فارسی است (برهان و معین آن را همان هویج، Daucus carota، می‌دانند؛ در گیلکی هنوز رایج است، کردی gêzer، بلوچی gizirk، پشتو gāzara، و خاستگاهِ «جزر» عربی)، اما خاستگاهِ آن ریشهٔ هندواروپاییِ *gogolos نیست. ویکی‌واژه آن را از *gazar فارسی میانه به ارث‌رسیده می‌داند و در کنارِ خوشه‌ای خاورِنزدیکی می‌گذارد: گارجَرَ (gārjara) سنسکریت، گِزّارا (gezzārāʾ) سریانی، گِزِر (gézer) عبری — همه به معنای «هویج» — و وام‌های ترکیِ kişer/käşir. واژه‌ای که با همین صورت میانِ ایرانی و هندی و آرامی و عبری مشترک باشد، «واژهٔ گردندهٔ» (Wanderwort) گیاهِ کِشتی است، نه اسمِ ارثیِ هندواروپایی؛ خودِ هویج گیاهی اهلی‌شده در فلاتِ ایران است که در دورانِ تاریخی پراکنده شده. بازسازیِ مان («برآمدگی، چیزِ باریک‌شونده»، بر پایهٔ شکلِ ریشهٔ گیاه) ریشه‌شناسیِ شخصیِ اوست و بیرون از فرهنگِ خودش پشتوانه‌ای ندارد. پس پژوهشِ امروزی این ادعا را نمی‌پذیرد.\",\n   \"sources\": [GAZAR],\n   \"ref_check\": [\n    {\"ref\": \"IEC:287\", \"status\": \"supports\", \"note\": \"Mann, printed p.288 (IEC.txt line 4216) does list 'Per. gazar \\\"carrot\\\"' under gogolos — the citation is accurate as a citation; it is Mann's claim that is doubtful.\"},\n    {\"ref\": \"MON:3306\", \"status\": \"not_checked\", \"note\": \"Mo'in's 6-vol pagination cannot be checked in the copies on disk. The word is certainly in Mo'in: MON_part2.txt line 32456 s.v. گزر gives the botanical entry '… چتریان که دارای ریشهٔ ضخیم … ریشهٔ گزر به علت ماکول بودن مورد مصرف روزانه است؛ هویج، گجر' with no etymology attached.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi s.v. گزر (MON_part2.txt line 32456 ff.)\", \"stance\": \"silent\", \"note\": \"A purely botanical description of Daucus carota ('گیاهی است دو ساله و خودرو از تیرهٔ چتریان … هویج، گجر'); Mo'in gives no origin tag here, so he neither supports nor contradicts an IE root.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', searched for گزر in BQT_v3_pages.txt (hits on pdf pages 284, 331, 429, 590, 591, 608)\", \"stance\": \"silent\", \"note\": \"The hits are the ordinary lexical uses; no etymological footnote of Mo'in attaches گزر to an Indo-European root.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (grep 'gazar', 'gezer')\", \"stance\": \"silent\", \"note\": \"Horn has no entry for gazar; the word is absent from his New Persian etymological list.\"}\n   ]\n  },\n  {\n   \"id\": 2,\n   \"lang\": \"Armenian\",\n   \"words\": \"kakği\",\n   \"verdict\": \"unverified\",\n   \"derivation\": \"The form is faithfully copied from the book (checked on the page image: the chart prints 'kakği', data/verification/sources/refs/ocr/BOOK/198.png) and the book in turn copies Mann, whose text the OCR renders 'Arm. kakγi (\\\"lime-tree\\\", fr. the fruit)'. I could not confirm the word from any independent source: no Armenian etymological dictionary (Ačaṙyan) is in the local library, the standard Armenian words for the linden/lime are լորենի loreni and for the poplar կաղամախի kaġamaxi, and searching the on-disk references (IEC, POK, WLD, AHD) turns up the form only in Mann's own line. Neither the existence of an Armenian kakġi/kakγi 'lime tree' nor its supposed derivation from a shape word can be verified either way; Mann's semantic bridge ('from the fruit') is in any case his own conjecture.\",\n   \"derivation_fa\": \"این صورت درست از کتاب برداشته شده است (روی تصویرِ صفحه بررسی شد: نمودار «kakği» چاپ کرده)، و کتاب نیز آن را از مان گرفته که متنش در نویسه‌خوانی «Arm. kakγi (\\\"درختِ زیرفون\\\"، از شکلِ میوه)» خوانده می‌شود. اما نتوانستم این واژه را از هیچ منبعِ مستقلی تأیید کنم: فرهنگِ ریشه‌شناسیِ ارمنیِ آچاریان در کتابخانهٔ محلی نیست، واژهٔ رایجِ ارمنی برای زیرفون լորենի (loreni) و برای سپیدار կաղամախի (kaġamaxi) است، و جست‌وجو در منابعِ روی دیسک (مان، پوکورنی، والده‑پوکورنی، واتکینز) این صورت را تنها در همان یک سطرِ مان می‌یابد. پس نه هستیِ چنین واژه‌ای در ارمنی و نه ریشه‌یابیِ آن اثبات یا رد شد؛ به‌هرحال پُلِ معناییِ مان («از شکلِ میوه») حدسِ خودِ اوست.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\"ref\": \"IEC:287\", \"status\": \"supports\", \"note\": \"Mann, printed p.288 (IEC.txt line 4216): 'Arm. kakγi (\\\"lime-tree\\\", fr. the fruit)' — the citation reproduces Mann accurately; the OCR gives kakγi/kakyi where the chart prints kakği, so the exact diacritic in Mann's print could not be settled.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW, grep 'kakgi', 'kaky', 'kakeli'\", \"stance\": \"silent\", \"note\": \"No such Armenian word anywhere in Pokorny.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I-III, grep 'kakgi', 'kakyi'\", \"stance\": \"silent\", \"note\": \"Nothing; Walde-Pokorny's Armenian material does not include it.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, printed p.288 (leaf 171)\", \"stance\": \"supports\", \"note\": \"The single source for the word, together with the doubtful 'OS kakeli \\\"icicle\\\"?'.\"}\n   ]\n  }\n ]\n}\n\nout = {\n \"pdf_page\": 198,\n \"book_page\": 168,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry0, entry1]\n}\np = \"/home/sfmqrb/git/rishe/data/verification/page-198.json\"\nwith open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", p, os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build198final.py\npython3 -m json.tool data/verification/page-198.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 198",
 "description": "Assemble and validate page-198.json"
}
```


### [2026-09-06T02:41:54.097Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-198.json 77381
JSON OK
nodes verified: 17/17
node verdicts: {'confirmed': 7, 'plausible': 6, 'transcription_suspect': 2, 'disputed': 1, 'unverified': 1}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 11, 'partial': 4, 'not_checked': 7}
books consulted: {'supports': 36, 'partial': 10, 'contradicts': 2, 'silent': 8} | by book: {'KLN': 8, 'AHD': 6, 'POK': 6, 'BQT': 5, 'CHEUNG': 4, 'HRN': 4, 'PHD': 4, 'NYB': 4, 'SYN': 3, 'BRT': 2, 'KNT': 2, 'ARY': 2, 'MON': 2, 'SKT': 1, 'LAT': 1, 'WLD': 1, 'IEC': 1}
```


## [2026-09-06T02:42:15.780Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-198.json` written; `verify_check.py 198` reports **17/17 nodes, 0 PROBLEM lines**.

**Page 198 (book p. 168) — verdict counts**
- Roots: 1 confirmed (Gnô/Gen/Gene 2), 1 disputed (Gogel/Gogelos)
- Nodes: 7 confirmed · 6 plausible · 2 transcription_suspect · 1 disputed · 1 unverified
- Ref checks: 11 supports · 4 partial · 7 not_checked. Books consulted: POK, WLD, AHD/Watkins, IEC, SYN, CHEUNG, BRT, KNT, PHD, NYB, HRN, BQT (v2+v3), MON, ARY, FFD, SPG, KLN, SKT, LAT.

**Flagged items**
- `transcription_suspect` #5 Sanskrit `pra-jan` — book misprint (error_in: book, page image checked). The word meant is *prajña-/pra-jñā-* (pra- + √jñā-); `pra-jan` belongs to the *other* root jan- 'to beget' (Pok. 1. ǵen-). Both of Nourai's own sources (Horn 815, Mo'in BQT 1459) write `pra + jñā`.
- `transcription_suspect` #10 Latin `gnôcere, nôcere` — book misprint for *gnōscere, nōscere* (verified on the page image). Same node: `norma` is bracketed by Watkins himself ("traditionally but improbably referred here") and is a Greek loan (γνώμονα) per Pokorny 378 and Klein.
- `disputed` root Gogel/Gogelos and node #1 Persian `gazar` — Mann's private reconstruction, absent from Pokorny, Walde-Pokorny and Watkins; گزر is an inherited MP *gazar / Near-Eastern culture word (Skt gārjara, Syriac gezzārā, Heb. gezer, Ar. جزر).
- `unverified` #2 Armenian `kakği` — attested only in Mann's own line; no Armenian etymological dictionary on disk, no independent confirmation.
- Notable `plausible` calls: #6 Pahlavi *frazānag* is a native Iranian *fra-+zan-* formation (Parthian frzʾng), a cognate of Skt prajña-, not a descendant — Horn and Mo'in both say "vergl."/"قس"; #2 Persian زندیق came back via Arabic *zindīq* (round trip unmarked), and Mo'in's own footnote in Borhan derives it from Av. *zanda-*, not from *zand*; #7 فرزین is a separate MP word *frazēn*.

**No extraction errors** — the JSON matches the printed page in every case (both odd forms are the book's).

Notes for the owner: `BQT_v3_pagemap.json` is a plain linear offset and is wrong around pdf pp. 85–89 (the picofile scan jumps printed 1294 → 1299); the real BQT:1298 (شناختن) text is only in `BQT_v3_pages.txt` block `[pdf page 85]`. I saved `.vision.txt` notes for BQT 1294/1299/1300/1302 and the page PNG to `data/verification/sources/refs/ocr/BOOK/198.png`. Also, Mann's *gogolos* entry sits on p. **288**, not 287.
