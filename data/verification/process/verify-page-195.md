# Verification process log — verify-page-195


## [2026-09-06T02:14:36.636Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 195 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-195.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-195.json. Write /home/sfmqrb/git/rishe/data/verification/page-195.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 195` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:38.222Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:38.884Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:38.897Z] TOOL RESULT

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


## [2026-09-06T02:14:39.388Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-195.txt"
}
```


### [2026-09-06T02:14:39.399Z] TOOL RESULT

```
1	=== PDF page 195 (book page 165) ===
2	--- entry 0 ---
3	ROOT [Arabic] Gh.r.f : to draw water  (refs KLN:237; SAP:1152)
4	#1 (parent #0) [Arabic] refs=KLN:237 | gharrâf : drinking jug
5	  #2 (parent #1) [Persian] refs=FVA:296; MON:308 | eğterâf «اغتراف» : to draw water by hands
6	  #3 (parent #1) [Spanish] refs=AHD:201 | 
7	    #4 (parent #3) [French] refs=AHD:201 | 
8	      #5 (parent #4) [English] refs=KLN:237 | carafe : a glass bottle
9	--- entry 1 ---
10	ROOT [Indo-European] Ghu 1, Ghau, Gheue, Gheu 2 : to call for help, appeal  (refs POK:413)
11	#1 (parent #0) [Indo-European] refs=AHD | Ghu-to : God, one who is called upon for help
12	  #2 (parent #1) [Avestan] refs=WLD:599; KLN:413 | zavaiti : invoked, God
13	    #3 (parent #2) [Pahlavi] refs=HUB:54 | xvatây : God | NOTE: See root "Aiw" for a different derivation.
14	      #4 (parent #3) [Persian] refs=BQT:718; HRN:104; FSF:159 | Xodâ «خدا» : God (who is called upon for help) ; xadieve «خدیو» : governor, king ; xâjeh «خواجه» : master | NOTE: See above references for more details.
15	  #5 (parent #1) [Germanic] refs=AHD | Gudam : God
16	    #6 (parent #5) [English] refs=AHD | God, good-bye, good-night
17	#7 (parent #0) [Indo-European] refs=KNT:182 | Gheu-bh : to speak
18	  #8 (parent #7) [Old Persian] refs=BQT:1821; FFD:75; KNT:182 | gaub, gub : to speak
19	    #9 (parent #8) [Pahlavi] refs=FFD:75; MON:3333 | guftan : to tell
20	      #10 (parent #9) [Persian] refs=FFD:75; HRN:206; BQT:1775,1821; MON:3195 | goftan «گفتن (گو ، گفتار ، گویش)» : to tell ; goptan «گپتن» : to tell, say ; gap «گپ (گب)» : gossip
21	--- entry 2 ---
22	ROOT Ghu 2 -> redirect to Dinghw
23	--- entry 3 ---
24	ROOT Ghuâ -> redirect to Dinghw
25	
```


## [2026-09-06T02:14:42.566Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-195.json",
 "description": "Read source JSON for page 195"
}
```


### [2026-09-06T02:14:42.616Z] TOOL RESULT

```
{
  "pdf_page": 195,
  "book_page": 165,
  "entries": [
    {
      "root": {
        "name": "Gh.r.f",
        "lang": "Arabic",
        "refs": "KLN:237; SAP:1152",
        "gloss": "to draw water"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:237",
          "words": [
            {"translit": "gharrâf", "gloss": "drinking jug", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:296; MON:308",
          "words": [
            {"translit": "eğterâf", "gloss": "to draw water by hands", "script": "اغتراف"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Spanish",
          "refs": "AHD:201",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD:201",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:237",
          "words": [
            {"translit": "carafe", "gloss": "a glass bottle", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghu 1, Ghau, Gheue, Gheu 2",
        "lang": "Indo-European",
        "refs": "POK:413",
        "gloss": "to call for help, appeal"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "AHD",
          "words": [
            {"translit": "Ghu-to", "gloss": "God, one who is called upon for help", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "WLD:599; KLN:413",
          "words": [
            {"translit": "zavaiti", "gloss": "invoked, God", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "HUB:54",
          "words": [
            {"translit": "xvatây", "gloss": "God", "script": null}
          ],
          "note": "See root \"Aiw\" for a different derivation.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:718; HRN:104; FSF:159",
          "words": [
            {"translit": "Xodâ", "gloss": "God (who is called upon for help)", "script": "خدا"},
            {"translit": "xadieve", "gloss": "governor, king", "script": "خدیو"},
            {"translit": "xâjeh", "gloss": "master", "script": "خواجه"}
          ],
          "note": "See above references for more details.",
          "quote": {
            "text": "سیامک به دست خزروان دیو - تبه گشت و ماند انجمن بی خدیو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "Gudam", "gloss": "God", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "God, good-bye, good-night", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "KNT:182",
          "words": [
            {"translit": "Gheu-bh", "gloss": "to speak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Old Persian",
          "refs": "BQT:1821; FFD:75; KNT:182",
          "words": [
            {"translit": "gaub, gub", "gloss": "to speak", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "FFD:75; MON:3333",
          "words": [
            {"translit": "guftan", "gloss": "to tell", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "FFD:75; HRN:206; BQT:1775,1821; MON:3195",
          "words": [
            {"translit": "goftan", "gloss": "to tell", "script": "گفتن (گو ، گفتار ، گویش)"},
            {"translit": "goptan", "gloss": "to tell, say", "script": "گپتن"},
            {"translit": "gap", "gloss": "gossip", "script": "گپ (گب)"}
          ],
          "note": null,
          "quote": {
            "text": "که ز هر ناشسته رویی گپ زنی - شرم داری، وز خدای خویش نی",
            "poet": "Molavî"
          }
        }
      ]
    },
    {"root": {"name": "Ghu 2", "redirect": "Dinghw"}, "nodes": []},
    {"root": {"name": "Ghuâ", "redirect": "Dinghw"}, "nodes": []}
  ]
}
```


## [2026-09-06T02:14:42.919Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T02:14:42.960Z] TOOL RESULT

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


## [2026-09-06T02:15:16.037Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','SAP','FVA','MON','AHD','POK','WLD','HUB','BQT','HRN','FSF','KNT','FFD','SKT','LKT','DEV','PHN','CHEUNG','BRT','PHD','NYB']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


## [2026-09-06T02:15:17.257Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-124.json'));print(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\""
}
```


### [2026-09-06T02:15:17.788Z] TOOL RESULT

```
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
=== SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only. Google Books no-view records 4y
=== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
=== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
=== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
=== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
=== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
=== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
=== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
=== CHEUNG MISSING
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
```


### [2026-09-06T02:15:19.348Z] TOOL RESULT

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
{"entry": 0, "root": "Dhě 2", "verdict": "confirmed", "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)", "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.", "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"], "ref_check": [{"ref": "AHD:1512", "status": "supports", "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the
```


## [2026-09-06T02:15:35.954Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN1966 carafe ===\"; grep -n -i \"carafe\" KLN_1966.txt | head -20\necho \"=== KLN1971 carafe ===\"; grep -n -i \"carafe\" KLN_1971.txt | head -20\necho \"=== LKT carafe ===\"; grep -n -i \"carafe\\|karaffe\\|ġarrāf\\|garrāf\" LKT.txt | head -20\necho \"=== DEV carafe ===\"; grep -n -i \"carafe\" DEV.txt | head -20\necho \"=== PHN carafe ===\"; grep -n -i \"carafe\" PHN.txt | head -20\necho \"=== SKT carafe ===\"; grep -n -i \"carafe\" SKT.txt | head"
}
```


### [2026-09-06T02:15:36.147Z] TOOL RESULT

```
=== KLN1966 carafe ===
6490:caracara,  n.,  a  kind  of  large  South  American bird.  —  A  Tupi  word  of  imitative  origin, carack,  n.  —  See  carrack. caracole,  n.,  half-turn  in  riding.  —  F.,  fr.  Sp. caracol,  lit.  ‘snail’,  which  is  prob.  a  blend  of L.  scarabaeus,  ‘a  beetle’,  and  conchylium  (fr.  Gk. xoyxuXiov),  ‘a  shell  fish’.  See  scarab  and  cockle, caracole,  intr.  v.,  to  make  a  caracole.  —  F.  cara- coler,  fr.  caracole.  See  caracole,  n. carafe,  n.,  a  glass  bottle.  —  F.,  fr.  Sp.  garrafa,  fr. Arab,  gharrdf  ‘drinking  jug’,  fr.  gharafa,  ‘he drew  water’.
=== KLN1971 carafe ===
39386:carafe, n., a glass bottle. — F., fr. Sp. garrafa , fr. 
=== LKT carafe ===
1699:689.  Ar.  garräfa: 'Weitbauchige  Flasche'  [vom  Vb.  garafa 'schöpfen';  das  Subst.  ist  nicht  klassisch- ar.,  sondern  scheint  nur  vulgär  imMagrib, s.  hier  Nr.  674,  gebräuchlich  zu  sein] ; hieraus  sp.  pg.  garrafa,  frz.  caraffe, carafe,  it.  caraffa,  siz.  carrabba  'Wasser- flasche, Flasche  für  Wein  od.  ähnl.'; dtsch.  Karaffe,  Karaffine,  ndl.  karaf, engl,  caraffe;  russ.  grafin,  poln.  karafka, ßech.  karafina,  bulg.  karafa.  —  [Ab- leitung aus  ar.  kar'a  'Kürbis,  Kürbis- flasche' geht  für  kat.  carbassa,  sp.  cala- baza,  pg.  cabaga  'Flasche'  ebensowenig wie  die  Gruppe  caraffe  aus  angeblichem ar.  karä'a  ML  4676  u.  6900].  —  [DE 274.  Dozy  Oost  48/50.  Hobson-Jobson 160.    Gorjajew  78.
5789:1068 A'ar«i*('  1004 Karaffe  689 Karakal  1081 ifa>-rt<  1182 Karawane  1075 Karatvanserai  1075 Karbatsche  1279
=== DEV carafe ===
941:Galtoun.  Pipe  persane.  M.  de  Gobineau  écrit  kalian.  ^  De beaux  kalians,  à  la  carafe  de  cristal  et  à  la  tête  d'or  simple ou  d'or  ëmaiHé\?5  G'est  le  persan  (jyXi  qalioûn  ou  ij^'i qahân.
963:Carafe.  Esp.  et  portug.  ^wrr^^/fl,  ital.  caraj^fa,  envient  cer- tainement de  la  racine  arabe  C^^à  gliaraf  qui  signifie  pm- ser??,  dit  M.  Dozy  (G/oss.  p.  27/1).  Et  le  savant  professeur en  donne  d'excellentes  et  solides  raisons.  Nous  renvoyons il  son  article.  M.  Littré  [Addit.)  cite  l'opinion  de  M.  MohI qui  rapproche  carafe  du  persan  ^joiyi  qarâbah,  bouteille  de verre  à  gros  ventre,  destinée  à  laisser  reposer  le'vin  pen- dant quarante  jours.
3191:Carafe.
3192:Caraffa,  ital.  voy.  Carafe.
3526:Garrafa ,  hisp.  voy.  Carafe.
4972:»^lc  voy.  Algarade. iô;lc  voy.  Razzia. ^L£  voy.  Alchimie,  5. wj«ijs^  vov.  Gamache. cj!j£  voy.  Astronomie,  7. Jb^  voy.  Grabeler. <j.r£  voy.  Garbin. A^sLcjC  y>er,s.  voy.  (jourgaiidinc. ci^  voy.  Carafe. J\y£  voy.  Gazelle. J-..C  voy.  Ghazel. 8^>^  voy.  Razzia. Ixa-^  voy.  Astronomie,  (i. Jyc  voy.  Algol,  Goule. L^".^^  voy.  Grèbe.
5004:3<^\Jipers.  voy.  Carafe.
=== PHN carafe ===
3202:CARAFE, s. f. (a.oup.)
3204:— Le mot carafe, qui se dit d'un vase en verre, plus large par
3207:Peut-être carafe vient-il plutôt du persan ajI^ [^arâ&eA] grand
10365:Carafe, s. f. (a. ou p.) — Carafoii, s. m 97
=== SKT carafe ===
23861:ITyexpWned  u  being  'of  wonted/  I      Carafe, a gUnwiter-bottle.     (F.  — Spi
```


## [2026-09-06T02:15:37.333Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ghau ===\"; grep -n \"ĝhau\\|ghau-\\|ĝhau-\\|ghu-tó\\|ĝhu-\" POK_full.txt | head -30\necho \"=== AHD gheu ===\"; grep -n -i \"^gheu\\|ghau\\|ghu-to\\|gudam\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-06T02:15:37.427Z] TOOL RESULT

```
=== POK ghau ===
34420:belong to *ghau-^zd\\, shout, cry', as also e.g. Old Norse gaud^ bark '); 
36023:Root / lemma: ghau- ghaua- 
36027:Alb. shows that Root/ lemma: ghuen-: "to sound' derived from Root/ lemma: ghau-, 
36056:gr. KQuxaopai " praise, oneself, boast, brag' ( *ghaughau-, compare Avestan zaozaomi), 
36059:maybe gemination alb. {*ghaughau-) ^e^e "northern alb. people. 
37664:Root / lemma: gheu- : ghd(u)- : ghau- 
38145:Note: extension from ghau-, s. Persson Beitr. 191 
38157:Alb. shows that Root/ lemma: ghuen-\ "to sound' derived from Root/ lemma: ghau-, 
39846:Root/ lemma: gh^ena^ woman, wife, *goddess' could be a truncated Root/ lemma: ghau- 
=== AHD gheu ===
523:gheu-
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
```


## [2026-09-06T02:15:47.969Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36015,36075p' POK_full.txt"
}
```


### [2026-09-06T02:15:48.032Z] TOOL RESULT

```
Meaning: hand, arm 

See also: s. more properly under ghesto-2. 

Page(s):413 



Root / lemma: ghau- ghaua- 

Meaning: to call, *priestess, *goddess 

Alb. shows that Root/ lemma: ghuen-: "to sound' derived from Root/ lemma: ghau-, 

ghaua-: "to call' 

Material: Old Indie havate^ call, shout, send for, call out to, summon ' (other phrase 

formations in hvayati, huve, homa, juhumasi). Pass. hOyate, participle hOta- " loaded, 

charged, filled with emotion, called', havftave \ni\n., havlman-n. "appeal, request, plea; 

prayer', hava-vn. n., havas-, havana-n. 6s., homann. " caller of the price ', hvatar-^ caller 



Avestan zavaitr calls, shouts, curses' (besides the present zbayeiti, zaozaomi), 
participle zuta- " call ', zavana-u. "shout, call, appeal, request, plea; prayer', zavan^shovX, 
call', zbafar-m. " shouter, caller'; [common alb. Romanian Iranian -v- > -b-]. 

Maybe Albanian zana^ nymph ', alb. geg {*gha-) za, zan/\o\ce, call' 

Lithuanian Z5i/e//" conjure, perform magic', Latvian zavetds., actually " somebody to 
curse something ' (compare Avestan zava/t/" enchanted, spellbound, bewitched '); 

Old Church Slavic zovg, zbvaf/^caW, shout, cry', Serbo-Croatian zovem, zvat/'caW, 
shout, cry'. Old Czech zovu, zvati, russ. zovu, zvatb ds.; in addition sloven, zovm. "shout, 
call (whether not noun post-verbal, = Old Indie hava-h, m. "shout, call'). 

Am\er\\an Jaunem ' consecrate, sanctify, bless; ordain', n-zovk" curse '; 

gr. KQuxaopai " praise, oneself, boast, brag' ( *ghaughau-, compare Avestan zaozaomi), 
from which back formation Kauxn f. " boastfulness '; 

maybe gemination alb. {*ghaughau-) ^e^e "northern alb. people. 

Old Irish guth m. "voice' ( *gutu-s); in addition gall, gutuatername a class of priests, 
probably from *ghufu-pdter lather (that is to say master) of calls (a god)'. Loth, RC 15, 224 
ff., 28, 1 1 9 ff.. Rev. Archeol. 1 925, 221 ; 



Here probably (as *ghu-t6-m "angerufenes creature '): 

Germanic *guda-n. "god' (compare Old Indie yC»^m-/7j/a-/7 "loud call', ved. epithet of 
Indras) in Gothic guf^m. "god' (the originally neutral form still in PI. ^^o'aand in galiuga- 
gul=>^ idol '), Old Icelandic god, gudu. " heathenish god'; gudm. "( Christian) god', Old 
English engl. Old Frisian asachs . godds., Old High German gotds.; 

therefrom derived Old High German gutin{na), mnl. godinne. Old English gyden 
"goddess'; Gothic ^^q^am. "(originally heathenish) priest'. Old Icelandic ^od/m. "
```


## [2026-09-06T02:15:48.924Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"zav\\b\\|zavaiti\\|zbayemi\\|zaozaomi\\|zbā\" POK_full.txt | head -20; echo \"=== page 413 in POK_02 ===\"; grep -n \"413\" POK_02.txt | head -5"
}
```


### [2026-09-06T02:15:48.996Z] TOOL RESULT

```
36041:Avestan zavaitr calls, shouts, curses' (besides the present zbayeiti, zaozaomi), 
36056:gr. KQuxaopai " praise, oneself, boast, brag' ( *ghaughau-, compare Avestan zaozaomi), 
=== page 413 in POK_02 ===
1008:413
1055:gT.  eleisch  asg-ög'  x^k  Hes.  (aus  *xt£S,  idg.  ghies?);  gr.  x^k  {*9hdes), h^k  (nach  iytsLvog  :  y,eTvog,  selbständige  Partikel  oder  Vorschlagsvokal, s.  oben  S.  283  und  Schwyzer  Gr.  Gr.  I  413,  Lejeune  Traite  182);  x^i-^dg, adverb.  x^t^a  , gestrig',  nach  Schwyzer  Gr.  Gr.  I  351  aus  X-^k-{-*dtd zu  ai.  a-dyä  ,heute'  (Instrum.  von  idg.  *dios  ,Tag';  fehlt  oben  S.  183),  mit vortoniger  Schwächung  des  e  zu  i,  nach  Specht  KZ.  68,  205  aus  *ghdis >  ghis  mit  Adverbialsuffix  (wie  in  gr.  xQvß-da) ;  Xi9-£0't)'0g  , gestrig' ;
1068:WP.  I  664,  Trautmann  373,  Schwyzer  Gr.  Gr.  I  325,  413;  zum  idg.  d ycr\,  zuletzt  Lejeune  Traite  de  Phonetique  grecque  S.  31  f.
1448:WP.  I  606,  WH.  I  413  f.
1539:'    Vgl.  im  allg.  Fick  P  219,  435,  IP  107,   IIP  130  (und   Falk-Torp  u. gjers    m.    Lit.    über    den    Fischnamen    norw.    gjers    ,lucioperca,    Sander^ schwed.  gers  ,acerina,  Kaulbarsch',   prakrit.  jhasa-  ,ein  gewisser  Fisch*). WP.  1  610,  WH.  I  413  f.,  650,  659.
```


## [2026-09-06T02:15:53.732Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '36075,36110p' POK_full.txt"
}
```


### [2026-09-06T02:15:53.823Z] TOOL RESULT

```
"goddess'; Gothic ^^q^am. "(originally heathenish) priest'. Old Icelandic ^od/m. " 
heathenish priest' (Proto Norse gudija), gydjai. "priestess'; Middle High German gating 
"priest'; 

previous Christian formations are Old High German *gotfater, gotmuoter. Old English 
godfaeder. Old Norse gudfader, gudmoder' godfather, godmother ', in addition of the 
name indicating fondness also Swedish gubbe^ graybeard', gumma^ hag ', Old High 
German *goto, gota. Middle High German gd1{t)e, goi{t)e^ godfather, godmother'. 

References: WP. I 529 f., Trautmann 367; ausfiJhrl. Lithuanian by Feist 227 f. 
Page(s): 413-414 

Root / lemma: ghag^'h- 

Meaning: young of an animal or bird 

Material: Npers. zac/ "young animal, esp. young chicken ' (c/ Arabic spelling for fj\ 

[Armenian ya^ "the young of an animal, esp. a bird, nestling, chick' is pers. loanword]; 

alb. zok, zogu'bkd, young bird, the young of the donkey'. 

References: WP. I 531. 
Page(s): 409 

Root / lemma: g(h)egh- 

Meaning: ferret 

Material: Old lndicya/7a/ra "polecat' (or "hedgehog'?), Lithuanian ses/ras "polecat' 

(originated through double assimilation iroxr\*zezkas)\ compare Lithuanian os/ra "goaf 

compared with Old Indie ajika ds. 

References: WP. I 570, W. Schuize Kl. Schr. 630; different Miihlenbach-Endzelin III 820.
```


## [2026-09-06T02:15:55.166Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"zavaiti\\|ghau-\\|ĝhau\" WLD_Bd1_pages.txt | head -20; echo \"=== find page 599 tag ===\"; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | sed -n '600,615p'"
}
```


### [2026-09-06T02:15:55.256Z] TOOL RESULT

```
31422:     u. ghau-
49973:ghaua-, daneben ghau- „rufen, anrufen 44                                        .
49987:hvatar „Anrufer“; av. zavaiti „ruft, ruft an, verruft, verwiinscht 44 (daneben die
50015:zavet ds., eigtl. ,,jemandem etwas anfluchen , vgl. av. zavaiti jjVerwiinscht
60466:      Zweifelhaft bleibt, ob *ghouros zu ghau- „rufen ,schreien“ zu stellen ist.
=== find page 599 tag ===
```


## [2026-09-06T02:16:04.149Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nhead -3 WLD_Bd1_pages.txt; grep -c \"\" WLD_Bd1_pages.txt; grep -n \"pdf page\" WLD_Bd1_pages.txt | head -3\necho \"=== context of ghaua ===\"; sed -n '49965,50000p' WLD_Bd1_pages.txt"
}
```


### [2026-09-06T02:16:04.254Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

81975
=== context of ghaua ===



(trotz Pedersen KZ. 38, 199; s. u ghou-).                        .




ghaua-, daneben ghau- „rufen, anrufen 44                                        .



  Ai. hdvate „ruft, ruft an, . .                herbei44 (andere Praesensbildungen in livdyat i,
                                                         .




huve, homa, juhumasi ),                  pass, huyate, hfitd „geladen“, Inf. haiitavc, havmian
„Anrufung“, liava m. n., hdvas, hdvana n. ds., homan n. „Rufen des Preises 44                                                             ,


hvatar „Anrufer“; av. zavaiti „ruft, ruft an, verruft, verwiinscht 44 (daneben die
Praesentia zbayeiti. zaozaomi), zavana n. „Ruf, Anrufung 44 zavan ,.Ruf‘ zbatar                        ,
                                                                                                                       4
                                                                                                                           ,


m. „Rufer, Anrufer 44 arm. jaunem „weihe“ (hierher nach Osthoff BB. 24,
                                 ;


182 und Persson Beitr. 118; sonst meist zu gheu- „gie6en 44 gestellt, s. d.),
               44                                         44
n-zovR „Fluch    ;
                   gr. xav/doyai „riihme mich, prahle        (< *ghaughau vgl. av.
```


## [2026-09-06T02:16:05.996Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN zavaiti/god ===\"; grep -n \"zavaiti\\|zbayeiti\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN god entry ===\"; grep -n \"gudam\\|guth-\\|god, n\\.,\" KLN_1966.txt | head -5"
}
```


### [2026-09-06T02:16:06.082Z] TOOL RESULT

```
=== KLN zavaiti/god ===
KLN_1971.txt:104230:to Avestic zavaiti , of s.m., Gk. xau/aouai, ‘I 
KLN_1966.txt:16388:God;  god,  n.  —  ME.,  fr.  OE.  god,  rel.  to  OS., Du.  god,  OHG.,  MHG.  got,  G.  Gott,  ON.  gud, Dan.,  Swed.  gud,  Goth,  gup,  for  Teut.  *guda-, which  is  prob.  a  participial  formation  (cp.  cold, loud,  old)  meaning  ‘the  invoked  being’,  and corresponds  to  I.-E.  ghu-tb-m,  fr.  base  *ghu-, ‘to  invoke’,  whence  OI.  hu-ta-,  ‘invoked’  (epithet of  Indra),  pp.  of  havate,  ‘invokes’,  which  is  rel. to  Avestic  zavaiti,  of  s.m.,  Gk.  xxu'/ao;jiat,  ‘I boast’,  OSlav.  zovq,  zuvati,  ‘to  call’.  Cp.  bigot, giddy,  good-by,  gossip.
=== KLN god entry ===
```


## [2026-09-06T02:16:14.187Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','WLD','HUB','HRN','BQT','MON','FSF','KNT','FFD','AHD','POK']:\n  v=d[k]; print('==',k); print(' offset:',v.get('page_offset')); print(' hint:',str(v.get('lookup_hint'))[:400]); print(' local:',v.get('local_file'))\n\""
}
```


### [2026-09-06T02:16:15.944Z] TOOL RESULT

```
== KLN
 offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
== WLD
 offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
 hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
== HUB
 offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
== HRN
 offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
== BQT
 offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== MON
 offset: None
 hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
== FSF
 offset: 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
 hint: grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt']
== KNT
 offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
== FFD
 offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
 hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt']
== AHD
 offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
== POK
 offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-d
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
```


## [2026-09-06T02:16:24.521Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ncat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py <<'EOF'\nimport sys\nf=sys.argv[1]; targets=[int(x) for x in sys.argv[2:]]\ndata=open(f,encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0; res={}\nti=0\nfor i,l in enumerate(data,1):\n    if '\\f' in l: leaf+=l.count('\\f')\n    if i in targets: res[i]=leaf\nfor t in targets: print(t, '-> leaf(0based)', res.get(t))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py KLN_1966.txt 16388 6490\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py incoming/WLD/WLD_Bd1_pages.txt 49973"
}
```


### [2026-09-06T02:16:26.357Z] TOOL RESULT

```
16388 -> leaf(0based) 360
6490 -> leaf(0based) 136
49973 -> leaf(0based) 537
```


## [2026-09-06T02:16:33.219Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^cherub\\|cherub,  n\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T02:16:33.271Z] TOOL RESULT

```
7347:cherub,  n.  —  Heb.  klrubh ,  ‘winged  angel’,  prob. rel.  to  Akkad,  karabu,  ‘to  bless’,  karibu,  ‘one who  blesses’,  epithet  of  the  bull-colossus,  and  to Heb.  bertikh,  ‘he  blessed’,  berakhdh,  ‘blessing’. See  berakah  and  cp.  griffin.
```


## [2026-09-06T02:16:34.158Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==137' KLN_1966.txt | head -5; echo \"....\"; awk 'BEGIN{RS=\"\\f\"} NR==137' KLN_1966.txt | tail -3"
}
```


### [2026-09-06T02:16:35.853Z] TOOL RESULT

```
  ‘cart,  waggon’,  Bret,  karr,  ‘chariot’,  L. carrus,  of  the  same  origin  and  meaning,  gave birth  to  ONF.  car,  F.  char.  L.  currus,  ‘chariot’, is  independent  of  the  above  Celtic  words,  but cognate  with  them.  See  course  and  cp.  career, cargo,  caricature,  cariole,  cark,  caroche,  car-
roccio,  carry,  carriage,  charabanc,  charge,  chariot. Derivative:  car,  tr.  and  intr.  v. carabao,  n.,  water  buffalo.  —  Sp.,  from  Philip¬ pine  native  name.
Carabidae,  n.  pi.,  a  family  of  beetles  ( entomol .)  — ModL.,  formed  with  suff.  -idae  fr.  Gk.  vAcyfio-, ‘homed  beetle’.  See  scarab  and  cp.  Caridea. carabineer,  n.,  a  mounted  soldier  armed  with  a carbine.  —  F.  carabinier,  fr.  carabine,  ‘carbine’. See  carbine.
carabinieri,  n.  pi.,  the  Italian  police.  —  It.,  pi.  of carabiniere,  fr.  F.  carabinier.  See  carabineer, caracal,  n.,  a  kind  of  lynx.  —  F.,  fr.  Turk,  qarah qulak,  ‘black  ear’.
caracara,  n.,  a  kind  of  large  South  American bird.  —  A  Tupi  word  of  imitative  origin, carack,  n.  —  See  carrack. caracole,  n.,  half-turn  in  riding.  —  F.,  fr.  Sp. caracol,  lit.  ‘snail’,  which  is  prob.  a  blend  of L.  scarabaeus,  ‘a  beetle’,  and  conchylium  (fr.  Gk. xoyxuXiov),  ‘a  shell  fish’.  See  scarab  and  cockle, caracole,  intr.  v.,  to  make  a  caracole.  —  F.  cara- coler,  fr.  caracole.  See  caracole,  n. carafe,  n.,  a  glass  bottle.  —  F.,  fr.  Sp.  garrafa,  fr. Arab,  gharrdf  ‘drinking  jug’,  fr.  gharafa,  ‘he drew  water’.
....
card,  n.,  a  machine  for  combing  hair,  wool,  etc.  — F.  carde,  ‘chard,  teasel,  card",  fr.  OProveng.  ear- do,  back  formation  fr.  cardar,  ‘to  card’,  fr.  L. carduus,  ‘thistle’,  which  is  related  to  carro,  car- rere,  ‘to  card  (wool)’,  from  a  basic  form  *carri- dus,  ‘that  which  scrapes’,  fr.  I.-E.  base  *qars-, 'to  scrape,  scratch,  rub’.  See  harsh  and  cp.  car- doncillo,  cardoon,  Carduus,  Carex,  carline  thistle, carminative,  carrizo,  chard, card,  tr.  v.,  to  comb  with  a  card.  —  F.  carder, fr.  carde.  See  prec.  word.
Derivatives:  eard-ed,  adj.,  card-er,  n. card,  n.,  a  piece  of  pasteboard  for  playing.  —  F. carte,  fr.  Late  L.  carta,  ‘a  leaf  of  paper;  paper’, fr.  L.  charta,  ‘a  leaf  of  the  Egyptian  papyrus; papyrus;  paper',  fr.  Gk.  yip rqp,  of  s.m.,  a foreign  word,  possibly  of  Egypt,  origin.  Cp. carte  blanche,  carte  de  visite,  cartel,  cartoon, cartouche,  cartridge,  cartulary,  chart,  charter, ecartc,  skat.
Cardamine,  n.,  a  genus  of  plants  of  the  mustard family  (hot.)  —  ModL.,  fr.  L.  cardamina,  fr.  Gk. xxpSxaivr,,  ‘a  kind  of  cress',  a  word  formed  by Dioseorides  fr.  xxpSxpov,  ‘cress",  which  is  of  un¬ certain  origin.  Cp.  next  word, cardamom,  cardamum,  n.,  an  aromatic  fruit.  — F.  c
```


## [2026-09-06T02:16:41.287Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py KLN_1966.txt 7347"
}
```


### [2026-09-06T02:16:42.906Z] TOOL RESULT

```
7347 -> leaf(0based) 155
```


## [2026-09-06T02:17:13.812Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 printed 599 (leaf 608 1-based) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==608' incoming/WLD/WLD_Bd1_pages.txt | head -25\necho \"=== check leaf 538 (printed 529) head ===\"; awk 'BEGIN{RS=\"\\f\"} NR==538' incoming/WLD/WLD_Bd1_pages.txt | head -8"
}
```


### [2026-09-06T02:17:15.430Z] TOOL RESULT

```
=== WLD Bd1 printed 599 (leaf 608 1-based) ===
                                     ger-, gere-                                 599

                                                    2
   gr. eyecgco „wecke“ (e- ist nach Brugmann II       3, 38 das Adv. *r, vgl. 0
oder o in av. d-garayeiti ), aor. k'ygezo, eygsadat, pf. i-ygrj-yoga (fur e-yt]-
yoga      vgl. ai. ja-gara — mit dem g von eygeo&ai Thurneysen IF. 19,
           —
176; med. i-yrj-yeg-juar, vom pf. gin gen auB eygrjyogzt „im Wachen", eygt)-
yogaig), eyggcoa) „wache" [*eygyaMa> nach Meillet, s. Boisacq 212);
   alb. ngre „ich hebe auf, wecke auf (Gr. Meyer Alb. Wb. 306, Pedersen
                                            ‘


KZ. 33,545);
       experglscor -i „erwachen“ (diss. aus ex -prr-gr>-scor, J. Schmidt KZ.
    lat.            ,


37, 155,  bzw. noch alterem *ex-pro-grt-scor, Yf. LEWb. 2 s. v , das in der
Praep. mit av. fru-yrd- sich deckt; trotz Persson Beitr. 828 f. nicht aus *ex-
per-r(e\gi-scor   von einer zu pergo, rego gehorigen Wzf. *regei-, wenngleich
die Romer das Wort als mit letzterem zusammengesetzt empfanden,                 woher
das ptc. experrectus);
  aus dem Germ, vermutlich anord. larskr, kerskr „frisch, lebhaft“, mhd.,
nhd. mdartl. karsch „frisch, munter' (Prellwitz 82, Zupitza Gutt. 144).
=== check leaf 538 (printed 529) head ===
                                                              gau-   — ghaua-                                                       529

gau- ,,sich freuen, sich freudig briisten 44                                .



  Gr. yrj&eco „freue mich 44 (aus *ydf€'&em, trotz der von Jacobsohn KZ. 43.
44 beanstandeten, bei Homer bereits iiberall durchgefiihrten Kontraktion
```


## [2026-09-06T02:17:16.512Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB xvatay/xuda ===\"; grep -n -i \"xvatâi\\|xvatāi\\|hvatâi\\|xudâ\\|xudā\\|hudâ\\|χvatāi\\|hvatay\" HUB.txt | head -20\necho \"=== HRN xuda ===\"; grep -n -i \"χudā\\|xudā\\|chudā\\|hudā\\|χudâ\" HRN.txt | head -20"
}
```


### [2026-09-06T02:17:16.594Z] TOOL RESULT

```
=== HUB xvatay/xuda ===
=== HRN xuda ===
```


## [2026-09-06T02:17:23.669Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN printed 104 (leaf 125) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==126' HRN.txt\necho \"=== HUB printed 54 (leaf 64) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==65' HUB.txt"
}
```


### [2026-09-06T02:17:25.657Z] TOOL RESULT

```
=== HRN printed 104 (leaf 125) ===
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
=== HUB printed 54 (leaf 64) ===
— 54 —
Z. 2 stimmen, auch wenn es vorhanden ware, was
aber nicht der Fall ist: xcLvar-xudai = der Xavar-
herr Fird. I, 154, 465.
469. In den Nachtragen wird saxudan zerkratzen' (afgh.
LW. st^xudq 'scratched with the nails') hierher gestellt.
Aber 'kauen ist nicht zerkratzen' und xdyam nicht
Saxayam.
ill, NSldeke bezweifelt die Richtigkeit von Horn's
Etymologie: np. xuddi *Gott' = zd. *x^adaya- mit
voUem Recht, da ocudai = phi. x^atai (61. and. Ind.
p. 47, Bdh. Gl. 126, ZDMG. 31, p. 596, Nr. 34, etc.)
ein zd. *xwataya- oder auch *xwataia-^) voraussetzt,
die sich zur Not durch skr. svatas 4- ayu- Von selbst
lebend' oder skr. svatas + adi- Von selbst anfangend,
uranfanglich' (vgl. skr. svayambhu-) deuten liessen. Doch
sind diese Deutungen so unsicher wie die iibrigen. Vgl.
Fr. Muller, WZKM. 5, 65. Als Curiosum sei er-
wahnt, dass de Lagarde, Agathang. p. 159—160
deutsch Gott wieder (nach Burnouf) aus dem Per-
sischen {xodd = xudai) entlehnt sein lasst wie deutsch
gund (in Kunigunde etc.) aus pers. "^gund.
474. Vgl. ZDMG. 46, 234. Dazu arm. xarbzak 'Melone' (nur
bei Caxcax,)
475. Np. xarSang *Krebs' aus phi. karcang mit volksety-
mologischer Anlehnung an die Composita mit xar Esel
(vgl. Vullers s. v. xar 2), so dass nun das Wort
aus xar 'Esel' und cang *Kralle' zusammengesetzt er-
scheint.
476. Lies arm. xrat (fur xart),
477. Dazu kurd. vird, Mrs, hire 'Bar ZDMG. 38, 93.
478. Auf Grund der Pazendlesungen des Min. und Shk
setze ich x^arsand als Pehleviform an und lehne
die so wie so unsichere Etymologie Darmesteters
(= hu-rasant' gut-kommend' ab.)
*) Arsao. phi. *x^ataS, sp&ter phi. x^atai, paz. x^adai.
```


## [2026-09-06T02:17:50.432Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD xwadāy ===\"; grep -n -i \"xwadāy\\|xwatāy\\|xwad'y\\|xwadāy\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD xwaja ===\"; grep -n -i \"xwāǰag\\|xwacag\\|xwāja\" PHD.txt PHD_mackenzie.txt | head\necho \"=== NYB xvatay ===\"; grep -n -i \"xvatāy\\|xvatay\\|xvadāy\\|hvatāy\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T02:17:50.523Z] TOOL RESULT

```
=== PHD xwadāy ===
PHD.txt:124:~išn : [М tandis] ... add ёахгар |c hlk' | M cxr, № čarx] wheel, circle. čimīg ... add caused, justified, reasonable. dagrand-xwadāy ... delete eternal. dast-gir [dstgyl | N x]... delete: dst OHDWN, ...
PHD.txt:703:absolute kāmag-xwadāy, kāmgār.
PHD.txt:1677:dominion šahryārīh; of long ~ dagrand-xwadāy.
PHD.txt:2330:householder kadagxwadāy.
PHD.txt:2415:independent kāmag-widār / -xwadāy kām-zīwišn.
PHD.txt:2667:lord аху, bay, šahryār, xwadāy; ~ of the land dahibed.
PHD.txt:2668:lordly xwadāywār.
PHD.txt:2745:master awestād, rad, salar; ~ of the house kadagxwadāy, mānbed.
PHD.txt:2825:misrule dušxwadāyīh; v. evil rule.
PHD.txt:4984:kadagxwadāy kadagbünüg kadagig
PHD.txt:5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
PHD.txt:5415:duSoxig dušox dušxwaršt dušhumat gūšūsrūd dušxwadāyīh dušāgāh dušāgāhīh dūšāram dušarz dušīh dujdānāg yojdahr yójdahrih yojdahrgar yējdahrgarīh dujdén dušgēwišn dujgand dujgandīh dujdēysšrīh dūšīzagīh dēšīzag dujdatt
PHD.txt:5488:dagrand-xwadāy t pay KÉ
=== PHD xwaja ===
=== NYB xvatay ===
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
3899:Vadagān [wtk?n'] patron. or pl. cas. obl.: adak-it 1000 sāl xvatāyēh i gehän dahom cigon 6 ~ dahyupat Dahāk dāt then I will
4376:xYatayéh domination, dominion, reign 620, 727, 1311.19.21 ete. passim; v. also zēšt-xvatāyēh, duš-xuatayeh, ēv-xYatāyēh, ēvak-x".; KZŠPrth hwtwypy, Gr. v. šeo-
```


## [2026-09-06T02:17:51.771Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT gaub printed182 (leaf 197) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==198' KNT.txt | head -40\necho \"=== KNT grep gaub ===\"; grep -n \"gaub\" KNT.txt | head -20"
}
```


### [2026-09-06T02:17:53.663Z] TOOL RESULT

```
=== KNT gaub printed182 (leaf 197) ===
�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.
ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bis, 26, 68; 444; DNb If; DSf 10; DS} 2°, 5°; ХРе 10f; XPd 16; XSa 1; Х8е 3°; XV 20; А:Ра 19°; D'Sb3?, 4°. imá apn. DB 432. imaibiš ipn. DNb 48.
Imaniš- sb. ‘Imanish’, name assumed by the Elamite rebel Martiya (§163.V): Elam. um-man- nu-$, АКК. tm-nia-ni-e-Su. — Imani$ пә. (8185.11) DB 2.10; 4.16f; DBF 4.
уат demonst. adj. and pron. ‘this’ ($11, $260.I1I, $265): from * nsf. (perhaps also from *? suffixless пзш.) -+ pronominal -am (q.v.). Decl., $199. Seealso?dà,/ma-. тат pron. пет. DBb 1; DBe 1; DBd 1; DBe 1; РЫ 1; DBg 1; DBh 1; DBi 1; рву 1; DBk1; DN i-v, xv, xvi", xvii, xxix; А?Р 1-4, 8°, 9-21, 22 (written imy*, $51), 23-8, 29°, 30. туат adj. nsf. AmH 5,8 (as Isf., §56.V);
DPd 6; DZe 10; iya (§52.V) DB 4.90; т |
DB 4.91 (written тё, $52. VI).
isuvd- sb. ‘battle-ax’ (Junge, Klio 33.223; Kent, JNES 4.233): etymology unknown (stem- formation $143.IV). Not ‘bowcase’, for ?$uvd-, to Av. ifu- ‘arrow’, Skt. fsu- (ef. for variant views Wb. Grab 41-8). _ iswām asf. DNd 2.
LEXICON
as- vb., see atš-,
isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König, Burgbau 51-2; Wb. AfOF 7.41; Hz. AMI 3.57-8; W. N. Brown, Lg. 8.13). 2328 nsf. DSf 29.
ета or lismar\uy asn., of uncertain mean- ing, possibly ‘(gold) inlay’ (Cameron, Persepolis Treasury Tablets 129-30), DSf 51; supplied by Hz. AMI 3.74-5, as a borrowing from Elam. 25- ma-lu (@%ma-lu ‘wood’ Hinz, Orientalia 1950, shortly to appear), or from the lost Akk. original of both; сЁ JAOS 53.21, 56.220. But read rather Idàr|uv with Hinz, see Lex. s.v.
Izalàü- sb. 'Izala', a district in Assyria (86, $107): Elam.?5-$1-la.  Tizaljä nsf. DB 2.58, as re- stored by Wb ZDMG 61.726 (zara Tm. Lex. 74), after the Elam.; but Cameron found all the char- acters visible: 124.
^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
ukdra- adj. ‘having good people or army’: from u- ‘good’ + kāra- ‘people, army’.  uküram asn. for asf. AsH 9 ($52.11).
ucsnav- adj. ‘well satisfied’ ($142): from u- ‘good’ + zšnav- ‘satisfy’ (*wohlgeneigt", Hz. ApI 199-200; ихти ‘well-informed’, Sen 233). u[zina]us nsm. ($188.11, §190.1) DNb 27.
."ucüra- adj. ‘well done, successful’, as sb. nt.
‘good deed’: from u- + cãra-, to root kar- ‘do’ / (809, §122, §123.3), cf. LAv. dard- Hilfsmittel" NPers. батё (Ву. BSLP 30.1.65-6, Gr. $292; cf. Bthl. AiW 584); but Wb. AfOF 7.39-40, Hz. ApI 193-8, take from Ar. car- ‘move’ (Av. éaraitt, Skt. cárati; but Skt. has only sucürá as a woman's name!) ucüramnsn. DS} 4^; DSI 5. ucüram asn. DB 4.76; ucdramaiy DSf 20° (= ucéram-maty, $138.T).
uca$ma, incorrect reading for ст? = саат; see casa-.
^Uja- ^Uvja (83.1) sb. ‘Elam, Susiana’, a province of the Persian Empire ($166.П); also as
175
ethnic, ‘Elamite, Susian’: Elam. hal-tam-ti, Akk. e-lam-mat, ef. MPers. Ни? (Uja distinct from Uvja, wrongly Konig, Burgbau 9-11, and Hz. AMI 3.69-73). See also Ujiya-. (1) ‘Elam’: Ọja пзш. DSe 21°, DSm 7°; XPh 20. Uvja DB 1.14, 2.7, 5.4; DPe 10; DNa 22. Uvjam asm. DB 1.82; 2.12; 4.12, 17; 5.7, 10. {Лау lsm. DSf 46. Uvjaiy DB 1.74f, 75, 77; 2.10, 10f; 4.11, 17; DBe 9f; DBE 5. (2)'Elamite': Uvja nsm. DN iii; A?P 3.
^Ujya- *Uvjiya- (144.11) adj. 'Elamite, Susian’: deriv. of preceding. Uvjiya пет. DB 4.10, 5.5f. Unjiya npm. DB 1.75, 2.12, 5.15. Unjiyd apm. DB 5.11°. Uvjiyaibis ipm. DB 5.10,
ula (for шй, $36.I) conj. ‘and’ (52911-00): Av. ula, Skt. ш, Gk. Hom. -úre ‘like’, pIE *ute (hardly both -@ and - in Aryan, despite Mt. MSLP 19.57-8, MB Gr. 5151). Correlative with preceding -сӣ, DB 1.66f (cf. Gk. тё xai); ша... шб ‘both ... and’ 
=== KNT grep gaub ===
800:II. The stroke is in excess: agaubatà DB 3.55, inscribed ag*urf"a, acc. to KT. abara DB 3.67, inscribed arr’, acc. to KT. akariyatà DB 3.92, inscribed as't- acc. to КТ. vikanāhy DB 4.71, 73, inscribed viis- acc. to KT. yikandh°dis DB 4.77, inscribed v%s*- acc. to KT. pasüva : hada : Қата DB 5.21, correction from
2468:Also, with strong-grade roots: OP kana- m imf. avakanam; gauba- in mid. gaubalaty, imf. agau- бий, pl. адамба'{@; tazša- m mid. ha”tarSatary, imf. hamataxsaiy hamataxíatà hamatazsa"td, yauda- (Av. yaozai), in imf. ayauda! ayauda’, pte. yau[da"tim]; apparently vaja- in avajam, татда- in imv. razbatuv; perhaps máva- in 3d pl. imf. mid. [am]ávatà.
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2598:I. The primary ending was pIE -taz, as in Gk. perar, Skt. bhdrate; this is seen in ОР yadatary (= Skt. ydjate), gaubataty, ha”-taxSatary, vaina- lary, varnavatary, and in the subjunctives yaddtary, gaubdtary, etc. (§222).
2602:П. The secondary ending was pIE -nto, as in OP abara"íà, Skt. dbharanta, Gk. ёфрорто; agauba"td, pass. akariya"td; non-thematic remade to thematic, akunava"ta ‘made’, dha*td ‘were’, йуа"{@ ‘went’,
2763:I. The pronouns haw, ava-, -fim, -dim, and their forms are often used to refer back to a pre- ceding phrase or relative clause; a preceding phrase is usually in the nominative, as in DB 2.30f Ката kya hamiçiya тапа nary gaubatary avam jadiy ‘the rebel army which does not call itself mine—that do thou smite’, but sometimes in its own proper case, as in DB 2.84 kdram hamiciyam hya mand naty gaubdtaiy атат jatà ‘the rebel army which may not call itself mine—that do ye smite’.
2770:In DB 2.921 Раша uta Varkana hami- туй арала" hacdma Fravartaiš agauba"tà ‘Parthia and Hyrcania became rebellious from me, they called themselves Fravartis’s’, the plural verbs in- dicate that the predicate adjective hamiçiyä is plural rather than dual, although it is predicate to two singular nouns,
2819:ПІ. A descriptive adjective is likewise incor- porated within the clause, in DB 2.30f (and 2.50f) kāra hya hamiçiya mana лашу gaubataiy ‘the hos- tile army which does not call itself mine’; but such adjectives usually stand outside, as in DB 2.84 küram hamiciyam hya тапа naiy gaubdtaiy, cf. also DB 2.21, 3.86.
2877:(a) The middie meaning is clear in such ex- amples as the following: DB 1.41f xSacam аш agarbiyata ‘he seized the kingship for himself’; DB 147 wãipašiyam акиіа ће made (the prov- inces) his own possession’; DB 1.55 patiydvahyaty ‘I asked aid for myself’; DB 1.93 hya Nabuk dra- cara agaubalà ‘who called himself Nebuchadrez- заг”; DB 4.38 patipayawa ‘protect thyself’.
2921:(c) Ina defining relative clause, not differing from one with the present indicative, the main clause being a command: gaubätaiy DB 2.84, 3.86; cf. ind. gaubatarzy DB 2.21, 31, 51, 3.15, 59 in the same meaning.
3067:VIII. Subordinate clauses may stand either be- fore or after the main clause; the order of the ele- ments in them is the same as the order in main clauses, though the verb is more likely to stand in final position. Occasionally a word belonging to the clause stands before the relative or conjunc- tion which introduces it: DB 4.37 tuvam Ка xSaya- iya hya aparam ühy ‘thou who shalt be king hereafter’, 4.67f, 4.87, cf. especially ОМ 21f, 24f. In one phrase an adjective belonging to the ante- cedent is incorporated within the relative clause: DB 2.31, 2.51 kära hya hamiciya manā nary gauba- іаїу ‘the rebel army which does not call itself mine’, ef. DB 2.84 kdram hamigiyam hya mand nau gaubülauy.
3535:84 birum : asiyavam : abiy : avam : Naditabairam : hya : Nabuk'dracara : agaubatà 85 : kara : пуа : Naditabairahya : Tigrám : adàraya : avada : aistatà : uta : i abiš : nāviyā : dha : pasiva : adam : küram : maškāuvā : avakanum : aniyam : usa : 87 bürim : akunavam : aniyahyà : asam : frinayam : Auramazdàmaiy : upastim 88 : abara : vaSnà : Auramazdaha : Tigrām : viyatarayama : avadà : avam : kàram : 80 tyam : Naditabairahyà : adam : ajanam : vasiy : ыз MR E rau
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3594:51 hya : hamiciya : mana : naiy : gaubataiy : avam : jadiy : pasiva : Vaumisa : a
3610:67 gaubatà : ài$ : hadā : kara : patiš : mim : hamaranam : cartanaiy,: pasáva : hamarana
3627:84 dram : hamigiyam : һуа : mana : naiy : gaubataly : avam : jatà : pas
3636:93 kana : hamiciya : abava : hacáma : Fravartazf : agaubatà : Vistaspa : mand : pita : ha
3647:WB, from Wb.'s reading of Ri.’s squeezes, add the following, also in roman, which were not visible to KT, nor to RI.: © zXiyat[tya]; 4 Fravajrii$;  Arminiyaily; 9! ova [mna ; 25 Fravartaié [:] agaubala; °° anustya; # nam.
3701:15 m : кагат : jadiy : hya : mana : пазу : gaubataiy : pasáva : DadarSis : hada : К 16 Ārā : a’iyava : hamaranam : akunaus : hadá : Márgavaibi$ : Auramazd
3717:35 vadā : hauv : Vahyazdáta : һуа : Bardiya : agaubatà : ài :
```


## [2026-09-06T02:18:01.091Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^gaub\\|gaub- vb\\|gauba- vb\\|‘call, say’\\|gaub-\" KNT.txt | grep -i \"vb\\|lexicon\\|say\" | head\necho \"---- search lexicon entry ----\"\ngrep -n \"Av. gaob\\|Skt. gup\\|gaub- vb\" KNT.txt | head\ngrep -n \"gaub\" KNT.txt | awk -F: '$1>3900' | head"
}
```


### [2026-09-06T02:18:04.392Z] TOOL RESULT

```
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5373:gub- vb., see gaub-.
---- search lexicon entry ----
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5341:gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
5373:gub- vb., see gaub-.
```


## [2026-09-06T02:18:22.603Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py KNT.txt 5341 5373\necho \"=== POK gaoša ===\"; grep -n \"gaoša\\|ghous-\\|gheus-\" POK_full.txt | head -10"
}
```


## [2026-09-06T02:18:22.646Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG gaub ===\"; grep -n \"gaub\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T02:18:24.380Z] TOOL RESULT

```
5341 -> leaf(0based) 205
5373 -> leaf(0based) 206
=== POK gaoša ===
23374:The key link between Root/ lemma: dous- {* gheus-): "arm' derived from an archaic root 
23376:*gheus'[^ar\d, arm' and Root /lemma: ghesor-1, ghesr- {* gheus-): hand' and Root/ 
23378:lemma: ghesto-2 {* gheus-): "hand, arm' are Baltic : Latvian pa-duse {zero grade) " armpit ' 
33523:Root / lemma: ghous- 
37328:gheus-: 
64521:Root / lemma: dus2. aus- : us- : ear', derived from zero grade of Root / lemma: ghous- : 
64994:The key link between Root / lemma: c/ous- {* gheus-): 'arm' derived from an archaic root 
64995:*gheus'hand, arm' and Root /lemma: ghesor-1, ghesr- {* gheus-): hand' and Root/ 
64996:lemma: ghesto-2 {* gheus-): "hand, arm' are Baltic : Latvian pa-duse {zero grade) " armpit '
```


### [2026-09-06T02:18:24.429Z] TOOL RESULT

```
=== CHEUNG gaub ===
575:etc.). Examples are *caxs ‘to drip, sip, eat’, *fšar! ‘to shame, be ashamed’, *gaub ‘to 
8188:*gaub 113 
8221:*gaub ‘to say (positively/negatively)’ 
8223:*OLD PERSIAN: gaub- (med.) ‘to call oneself" = Kent: 182b 
8225:MED.; Pres. them.: IND. 3sg. gaubataiy <g-u-b-t-i-y> (БВ 2.21 |, DB 2.31, DB 2.51, etc.), impf. 35р. 
8226:agaubatä <a-g-[u]-[b]-[t]-a> (DB 1.84), <a-g-u-b-t-a> (DB 1.93, DB 3.35, DB 3.55), <a-g-u-b-t-a> (DB 
8227:2.66), <a-g-u-b-t-[a]> (DB 3.89), 3pl. agauba”tä <[a]-[g]-u-[b]-t-a> (DB 2.93), SUBJ. 3sg. gaubätaiy 
18197:by the other roots for ‘to speak’, *џаќ and *gaub respectively, in the other Iranian 
34051:gaub-, 113 
55340:*gaub (s.v.), *ndz (s.v.), 
55471:*gaub (s.v.), *Hraz (s.v.), 
55503:*gaub (s.v.), *Hraz (s.v.), 
57677:*gaub, *HaH(a)d, *Hauj,
```


## [2026-09-06T02:18:28.858Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8188,8300p' CHEUNG.txt"
}
```


### [2026-09-06T02:18:28.912Z] TOOL RESULT

```
*gaub 113 


SUBJ. 15р. ? "ngw'n, ’ngw’’n; Partic.: perf. pass. пема; Caus.: pres. SUBJ. 15р. ’ng’w’n, IMPV. 2р1. 
"ng"wyd, partic. П ’ng’w’’d 

*KHOTANESE: gvana- ‘growth; at all’, guäna ‘at all’ 

*SOGDIAN: CSogd. ywn- ‘to increase’ || (+ *abi-) BSogd. Gw BSogd. ’Bz’’w, 
CSogd. bZ’w, MSogd. Ву? ‘to increase’ || (+ *fra- or *pari-) SSogd. pry^w (m.), 
BSogd. pry’w ‘wealth, riches’ 

Partic.: pres. CSogd. ywnnc (f.) ‘increasing’ || (+ *abi-) Pres.: IND. 3sg. BSogd. Bz’wt, BSogd. *Bz’’wt, 
OPT. 3sg. BSogd. ’Bz’w’y, IMPV. 25р. CSogd. bZ’w, MSogd. Bin 

*CHORESMIAN: (+ *fra-) Sy’weyk (m.) ‘profit’ 

*BACTRIAN: (+ *abi-) оВбоо- ‘to increase, prosper’ || (+ *fra-) Ypoyaoayo, 
Mpoyavo, Ppoyaoo ‘profit? = S-W, Bact.: 173b, 230b 

*NWIR: (+ *abi-) NP afzudan/afzäy- ‘to increase’ 

*NEIR: (+ *fra-) Oss. I. regaw, D. argaw ‘herd, cattle’ 

*MISC: (+ *fra-) Toch. (LW) A pärko, B pärkäu ‘benefit, advantage, profit’ 

© An IE provenance for this root cannot be established convincingly. 

*PIE — = LIV: 188 | Pok.: 403 f. 

*REFERENCES: Abaev, Slovar’ II: 368 f.; Nyberg II: 26b; DKS: 96a 


*gaub ‘to say (positively/negatively)’ 

*OLD PERSIAN: gaub- (med.) ‘to call oneself" = Kent: 182b 

MED.; Pres. them.: IND. 3sg. gaubataiy <g-u-b-t-i-y> (БВ 2.21 |, DB 2.31, DB 2.51, etc.), impf. 35р. 
agaubatä <a-g-[u]-[b]-[t]-a> (DB 1.84), <a-g-u-b-t-a> (DB 1.93, DB 3.35, DB 3.55), <a-g-u-b-t-a> (DB 
2.66), <a-g-u-b-t-[a]> (DB 3.89), 3pl. agauba”tä <[a]-[g]-u-[b]-t-a> (DB 2.93), SUBJ. 3sg. gaubätaiy 
<g-u-b-a-t-i-y> (DB 2.84), <[g]-u-b-a-t-i-y> DB 3.86) 

*MIDDLE PERSIAN: MMP gw-, ВМР gwb- /gö(w)-/ ‘to say, speak” = DMMPP: 
166af. 

Pres.: IND. 15р. MMP gwym, 3sg. MMP gwyd, BMP gwbyt /gowéd/, 3р1. MMP gwynd, SUBJ. 1sg. 
MMP gw’n, gww’n, 3sg. MMP gw’d, 1pl. MMP *gw'm, 3р1. MMP gw’nd, ІМРУ. 2sg. MMP gw-’m ‘say 
to me’, MMP gw; Partic.: pres. MMP gw’g’n pl., MMP gw’n, perf. pass. MMP gwpt, gwpt, gwft, gwft, 
sec. MMP *gwpyhyst, Inf.: MMP gwptn, MMP gwftn 

*KHOTANESE: LKh. gguph- ‘to dispraise, abuse’ — SGS: 29 

*SOGDIAN: BSogd. ywf-, CSogd. ywb-, MSogd. ywß- ‘to praise’ || (+ *pati-) 
MSogd. pcywf- ‘to praise’ 

Pres.: OPT. 3р1. BSogd. ywß’ynt; Impf.: IND. 3sg. CSogd. ywb; Partic.: pres. MSogd. ywBnyt, perf. pass. 
CSogd. ywbt‘, CSogd. ywbc (f.); Inf.: BSogd. ywB’y, pret. BSogd. ywß’t, Pass.: perf. intr. IND. 35р. 
MSogd. ywftyy хсу || (+ *pati-) Pass.: pres. SUBJ. 3sg. MSogd. pcywptyh B’t 

*CHORESMIAN: ywß(Yy)- ‘to praise oneself, boast, be proud’ = Samadi: 82 
*BACTRIAN: YoB- ‘to make a (legal) statement, invoke (the law)’ = S-W, Bact.: 189a 
*NWIR: NP guftan/göy-, Kurd. (Kurm.) gotin, guhtin (supplet.) beZ-, (Sor.) gutin, 
kutin (supplet.) 7e-, Shamerz. -get-/gün- ‘to speak’ 


114 *gaud 


*NEIR: (+ *uz-) Wa. zgiv-/zgivd ‘to howl (of dogs)’, Sariq. zsıgiw- ‘to bark? (< 
Wa.?) 

*MISC: Arm. (LW) govem ‘I praise’ 

No IE etymology. 


“PIE LIV: — | Pok.: 
*REFERENCES: Horn 1893: 206; Christensen, Contributions II: 162; Nyberg II: 85; DKS: 86b; 
Steblin-Kamenskij 1999: 436; Cabolov 2001: 396 


*gaud ‘to cover’ 

*PARTHIAN: (+ *apa-) 'bgwnd ‘to uncover, reveal’ || (+ *fra-) “fr’gwnd- ‘to cover, 
muffle’ || (+ *ni-) ngwnd- ‘to cover, veil, cothe, hide? => Ghilain: 83 | DMMPP: 10a, 
153b, 241a 

(+ *ара-) Pres.: IND. 25р. ’bgwndyy, 3sg. 'bgwndyd, 'bgwndyyd, 3р1. 'bgwndynd, IMPV. 2sg. 'bgwnd, 
’bywnd,; Partic.: perf. pass. ’bgwst, *’bgwstg || (+ *fra-) Pres.: IND. 3р]. "fr'gwndynd || (+ *ni-) Pres.: 
SUBJ. 1sg. ngwnd’n, IMPV. 2sg. ngwnd; Partic.: perf. pass. nywst, ngwst, ngwstg 

*KHOTANESE: (+ *uz-) uysgun- (uysg(a)us-) ‘to uncover, open’ || (+ *pati-) OKh. 
pajud- (pajut-) || (+ *ham-) LKh. hamgun- ‘to cover up’ = SGS: 15, 65, 137 
*SOGDIAN: MSogd. ryt-ywwó ‘face cover’ (Sogdica: 25, 39) || (+ *apa-) BSogd. 
py wnt ‘to discover’, MSogd. p'ywyó ‘to be revealed’ || (+ *a-) BSogd. "ywnt, 
CSogd. "ywnt, MSogd. ’’ywnd/’’ywst ‘to cover, dress’ || (+ *pati-) BSogd. ptyws- 
‘to cover’, CSogd. ptywnt ‘to cover, hide’, MSogd. ptywó ‘to conceal’ || (+ *ni-) 


BSogd. ny’wnt, (caus.) CSogd. nywynt ‘to dress, put on (clothes)’ 

(+ *apa-) Impf.: IND. 35р. MSogd. p'ywyó || (+ *4-) Pres.: PREC. 15р. MSogd. "ywndytww ‘may I 
cover/anoint’, IMPV. 2sg. BSogd. "ywnt; Impf.: IND. 3sg. CSogd. m’ywnt || (+ *pati-) Impf.: IND. 3sg. 
CSogd. ptyywnt; Perf.: tr. IND. 3sg. BSogd. ptywstk ö’rt, Partic.: pres. MSogd. ptywóyy (ВВВ: 36), (pl.) 
MSogd. ptywöyt ‘concealing’, perf. pass. BSogd. ptywstk, CSogd. ptywst-, CSogd. ptywc’ (Ё) ‘hidden’; 
Pass.: perf. intr. IND. 3sg. MSogd. ptywstyy xcyy ‘is hidden’ || (+ *ni-) Pres.: IND. 3sg. BSogd. ny’wnt, 
3р1. BSogd. ny’wnt’nt, Impf.: IND. 3sg. BSogd. nyywntw; Caus.: impf. IND. 3pl. CSogd. nyywynt 


*CHORESMIAN: ? mxsy- ‘[according to Arab. transl.] to crawl, creep ?; [according to 
NP transl.] to disappear ?' || (+ *apa-) bxsy- (inch./intr.) ‘to appear, become clear; 
[hapax, euphemism ?, different pref. ?] to defecate’, bywnd- (caus.) ‘to uncover, 
reveal, make clear; to acknowledge’ || (+ *a-) ’ywo ‘cover(ing)’ || (+ *pati-) pjyd- ‘to
```


## [2026-09-06T02:18:41.801Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN printed 206 (leaf 227) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==228' HRN.txt | head -45"
}
```


### [2026-09-06T02:18:43.507Z] TOOL RESULT

```
=== HRN printed 206 (leaf 227) ===
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


## [2026-09-06T02:18:43.894Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB guftan ===\"; grep -n \"guftan\\|gōvēt\\|gowēt\\|gövét\\|göftan\" NYB_vol2_glossary.txt | head -10\necho \"=== PHD gowistan/guftan ===\"; grep -n \"guftan\\|gōwišn\\|gōw-\" PHD.txt | head -10"
}
```


### [2026-09-06T02:18:43.963Z] TOOL RESULT

```
=== NYB guftan ===
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
1015:božišn [bwešn'] salvation 7615-18; excuse: ~ guftan to beg to be forgiven 415, cf SGV XI, 216.
1427:46 Py; HN?], old ev [yw], particle de- noting the opt. 1. ev: ~ HNHTWN. HajB:13 (v. nihätan); ču ŠDYTN ibd. 14 (v. vistan); ev ‘BYDWN F:5 (v. kartan); év göbet 128? (v. guftan). — 2. € Dy]: frāc & yazēt 539; ē nikecet 60%; han ē bavēt 1095. — 3. HN’: bē ē raset 604. — 4. encl. and written HWHw-yd = (h)e 61: āyēnd ~ they would cover (a distance of ...), ef the yäy-i Sart and the yày-i tamannā in early NP. — Av. (22) aēvā; Paz. č (SGV).
1677:guftan.
1705:g0(v)-vieär [gwwe’l] explicit, lucid 8021-25, — gov- from guftan, vicar from vtcārtan (g. v.): "word-explaining'. Paz. gaoguzdr, góguzür, gövazär ete., Skr. v. vibhakta (Mx), suvyakta (ŠGV).
1720:guftan [gwptn'] gēb- [YMLLWN-,YMR- RWN-; 3d p. sg. gwbyt 128%, gwbyt' 9923, 1021, gwpyt' 2315 göbet], opt. 2nd p. sg. gobeš [YMRRWN-yš] 6012, pt. always gwpt' = guft: to say, to tell, to utter, to pronounce, to recite, passim; with 6 ‘to’, apar, rād (53) ‘concerning, of’ (patiš 6614); followed by direct speech introduced by ku, passim; with a
1723:MPrs guftn gwy-; Paz. guftan, pres. 3d p. góéd, góid, gčend, gčind; NP guftan guy; the typical SW vb. for saying, as against NW vac-, v. vdeišneh.
2046:hu-gobišn [hwgwbšn'] of good speech, well-speaking 73°. 744, — Paz. hugavešn; v. guftan.
2993:passax" [pshw], püsax" [p'shw] answer, reply, reponse: 53?" (6 to) 5624. 1059-22; ~ guftan, pat ~ guftan, ~ kartan to answer, to reply, passim; ~ datan 26*;
4426:yütango(k) [y’tngwk] solicitor 70%, — Paz. jädangö; < *ydtana- = *ydta- (v.s. v. yāt) + go < gov from guftan (-k is spurious, ef. s. v. z"étodàt). Commonly yätak-göb from yātak = yät; Arm. lw. jatagov (Hbschm.).
=== PHD gowistan/guftan ===
3523:say guftan, P wāxtan.
3760:speak dranjidan, guftan, P wāxtan; (daevic) dawidan, drayidan.
5342:damidan mir-! murdant uštar! gow-t guftan™ gow-! guftant zamestān damišn. yask dastyār dastyārīh
5417:dostih dëst l*?dawistan dūpāy gubrāg gubrās- guftār guftārīh guftan
```


## [2026-09-06T02:19:01.965Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf ~175 (p.718) خدا ===\"; awk 'BEGIN{RS=\"\\f\"} NR==176' BQT_v2_pages.txt | head -40"
}
```


## [2026-09-06T02:19:03.852Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== grep خدا in BQT v2 ===\"; grep -n \"خداي\\|خدای\\b\" BQT_v2_pages.txt | head -5\necho \"=== BQT v3 گپ ===\"; grep -n \"گپ\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== BQT v3 گفتن ===\"; grep -n \"گفتن\" incoming/BQT/BQT_v3_pages.txt | head -5"
}
```


### [2026-09-06T02:19:04.315Z] TOOL RESULT

```
=== BQT v2 leaf ~175 (p.718) خدا ===
                                                    ‫بیان بنحم‬
                           ‫لفت‬   ‫خای نقطه دار باجیم مشتمل بر ده‬                           ‫در‬


‫باشد ‪ -‬ونام کلی حم هست (‪ )۲‬زردرنگه ومیان‬                      ‫خحا ره = سم‌اول بروزن‌شماره‪ .‬بمعنی‬
‫تب میکویند؟ ‪۰‬‬                        ‫مشود‬                     ‫ول باشد ‪ - ۱‬و بمعنی تسخر‬
                                                                                     ‫لی‬‫اند وقکم‬
                                                           ‫و مسخرکی هم آمده است ؛ و بفتح اول ایز‬
                                                    ‫ا‬                                                        ‫گفته‌اند ‪.‬‬

‫بفتح اول بر وزن کفش »‬                ‫ححشس‬

‫عردم‬        ‫وکاوی‬   ‫گردن‬   ‫آماسی و گرهی‌باشد که در‬
                                                                   ‫وبواو زده * آواز وصدای هرچیز رگاویند ‪.‬‬
‫نماند بزر گك تر‬        ‫نکند وهرچند‬      ‫بهم رسد و درد‬         ‫بفتح اول و سکون ثالی‬                 ‫خحچ؟ =‬
                                                ‫‪.‬‬   ‫شود‬       ‫در گلو‬                  ‫رجیم فارسی ‪٠‬‏ ورم ا‬


‫ححاك = بفتح‌اول‌بروزن کجك» بمعنی‬                              ‫؛ وباینمعنی‬        ‫بهم رسد ؛ وعم ارل حمامده ‪۱‬ست‬

                                                                   ‫(‪. )۱‬‬     ‫ت هم هت‬      ‫محای جم فارسی ا‬
‫قطه باشد ‪ -‬وشالیرا یز گوبند که با سرچوب‬
‫و نقطه وخال‬         ‫‪ 5‬باالگشت دست درزمدن گذارند ‪-‬‬             ‫خحته ‪ = ۲‬ض‌اول وفتح‌ثانی‌وسکون‬
               ‫سقدیرا یز گوبند که درچشم افتد ‪.‬‬                 ‫سین بی‌نقطه وفوقانی‌مفتوح» بمعنی‌مبارك ومیمون‬
                                   ‫(‪ )۲‬چس ‪ :‬کلی است‬                      ‫آمده است‪.‬‬      ‫)‪ ۱‬چكڭ» چش‪:‬‬



  ‫درق را بپانزده هزار دینار [ک] بنتدلد درمدتی خجاره»‬                       ‫‪* - ۱‬رباز فروختن او یمی‬
 ‫= هو = خوب )‬              ‫از‪ :‬خ ( بشو‬      ‫‪۴‬‬             ‫خجش(ھ‪.(.6. .‬‬       ‫‪۳‬‬    ‫‪۳‬‬            ‫«ئارىخ سستان‪۹۸۳‬؟‪.‬‬

      ‫جته؛ اوستا ‪uh - [2052‬‏ « اسفاا ‪ :‬ص ‪۷٩.‬‏ از ربشه اوستابی‪ ( )[028(02‬خواهش‪.‬‬
                                                                             ‫‪+‬‬
  ‫‪.‬‬    ‫ابر لندی ‪uidiug‬‏ (خواهس میکنم)» در ترحجمه و تفسس بهلوی ‪natsahZ‬‏‬                      ‫کردن ‪ ۰‬درخواستن)‪.‬‬

      ‫ه« بارتولمه ‪ .»۷۸4‬خجته لفة بمعتی تك‌خواسته ‪ .‬متبرك » مبارك؛ ضد «گسسته»‬                                    ‫‪0‬‬
                                                                       ‫رك‪ :‬همیثه بهار‪:‬‬         ‫‪۴‬‬             ‫(ملعون)‪.‬‬

                      ‫بر ربخت فرابةً می حدری‬                           ‫بربرك سپید باسمین تر‬
                     ‫بر گردن کوتشز پرعطری‪.‬‬                             ‫جنبید سر خجته تتوالد‬
```


### [2026-09-06T02:19:04.403Z] TOOL RESULT

```
=== grep خدا in BQT v2 ===
4413:     ‫(رمتن ‪ :‬الحکم) بود» وجادوی عظیم داشت» مقنمی بر روی بسته داشتیو دعوی‌خدایی کردی‪....‬‬
9517:             ‫که چون مانفخام بردست‌ویای‪.‬‬                             ‫بجاآورای خام شکر خدای‬
10270:  ‫شکكرده » چون خدای فارسی و خواتای بهلوی بکلمةٌ ‪_ayÃtaWX‬‏ ‪ °‬با ‪o 2002802۷01‬‏‬
10295:          ‫گفته‌اند ؛ وبفتح اول همآمده اش‬                         ‫وآنها راخدای فروشان هم میگوبند با دوتحتانی‬
10325:  ‫کشادیم» ‪« .‬دکلتان ‪ - ۰ ۸۲‬ان ‪ 9:‬هر که خدای را عزوجل بمازارد تادل مخلوقی بدست آرد ‪۰‬‬
=== BQT v3 گپ ===
6100:‏چون سک مزاست جایگپت شله.
16689:‎Ka ۴‏ بخشد کف تو در وگپر
18050:‏5 .«که. ۰۰۱۹۹۲ گپلکی 137186 : روزآباده - روز ی که پی از امروزخواهدآمد.
19664:‎chy‏ را ‎Eye‏ خود ‎ly‏ نگپداری آن‌آفریده
21921:گپی بگرید و کاهی بررش برفوزد ©
25641:‏۱ - مخفف‌آن «کارآ که»: خبرشد ازابشان‌بکارا گپان به‌پیرانبگفتنديك‌بك مهان..
27411:‏که داند که چه بات زر وگپر.
32766:بعنی سوراخ ‎BET‏ کوشك . ‎OT)‏ نوعی ازآلات قلمه کشابی بوده است که بدان سنگپای کلان
41872:‏گپ- بقتح اول و سکون ‎tae” «ut‏ - بن‌اول. بروژن ومعن ی ‎BS‏
49207:۸ - براساسی لیست. ‎٩‏ ا زگپر(گوهر )
=== BQT v3 گفتن ===
287:عهد ار شهید شدراورا شایور ذوالا کتاف ی گفتند
4817:سم گفتند دووجه بیان کرده‌ادد : ‎Kul‏ تعمان درزبان عرب بمعنی خون
5383:و حرف بی صرفه و محل گفتن- وبی‌عزت کردن
9507:کوبان‌است ,نی مردماییکه بصیاح الخیرگفتن
11991:کوید که «ابران شهر» را عمرب کرده ءراق گفتند . صدیقی ‎OU)‏ دخیل فارسی درعربی قدییم »
```


## [2026-09-06T02:20:20.847Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py BQT_v2_pages.txt 10270 10295\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py incoming/BQT/BQT_v3_pages.txt 41872"
}
```


### [2026-09-06T02:20:22.593Z] TOOL RESULT

```
10270 -> leaf(0based) 176
10295 -> leaf(0based) 177
41872 -> leaf(0based) 571
```


## [2026-09-06T02:20:28.257Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==577' BQT_v2_pages.txt | sed -n '1,60p'"
}
```


## [2026-09-06T02:20:29.222Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"==== BQT v2 leaf 176 full ====\"; awk 'BEGIN{RS=\"\\f\"} NR==177' BQT_v2_pages.txt"
}
```


### [2026-09-06T02:20:30.118Z] TOOL RESULT

```
  ‫»<<‬                                                                                            ‫سرافوج‬
 ‫سارفكرر = بر وزن در انداز » مقنعه‬                ‫‪ = ۱‬ضم یننقطه د اروسکون‬               ‫سراعوج‬

 ‫و رکویپ‌اباشد که زنان برسر انداز ندکوسیکه‬        ‫واو وجیم فارسی ‪ ۰‬بمعنی سراغج است که کیسو‬
 ‫از روی ناز وتخوت ومستی سرخود را بهر جالب‬                                                ‫پوش زتان باشد ‪.‬‬
 ‫حر کت دهد وخرامان خرامان براه رودسویمنی‬
                                                  ‫سراغوش ‪ = ۴‬با غین نقطه‌داربروزن‬
  ‫سارفکندکی هم آمده است ‪ -‬و شخص چت‬
 ‫وچالاك ویی‌پروا وبی‌باك ودزد وخونی ومردمکش‬       ‫زان باشد » و بعضی گوبند دامی است که زنان‬
‫نت کنند بعنی رویا کی است که و نایاك را نگیوزیند و‪-‬ستولیرا نکفیتزه‌اند که‬
                                                                       ‫بدان ززبیو‬
‫مین ابوان عمارت‌اندازندکه سر‌چوب‌های دیگر‬
 ‫بر بالای آن باشدسو قالی‌وپلای کوچکیرا گویند‬       ‫سرا گوش ‪ ۴‬د بکااف فارسی‪,‬بروزن‬
 ‫که بر سر جقت قالی و پلای بزر که بر عرض‬                 ‫و ممنی سراغوش است و کفته شد‪.‬‬
 ‫از حمله‬   ‫خاله اندازند ‪ -‬و نام اصولی حم هت‬
                                                      ‫سرا کوفت ‪ = ۴‬باخف س‬
                                                   ‫وکون‬
 ‫حفده بحر اصول موسقی وآنرا صوفیانه خوانند‬
                                                   ‫واو و فا و تای قرشت » بمعنی سرزش وطعنه‬
  ‫و‪-‬یممنی جلد وچايك هم بنظرآمده است ‪٩‬‏ ‪.‬‬
                                                                                                     ‫باشد ‪.‬‬
 ‫سر اندر ردن ک=نابه ازیتهان شدن‬
                                                   ‫سرا گون ‪ = °‬با کاف بروزن‌فلاطون»‬
 ‫باشد از تری و بیم ‪ -‬و کنابه از سر در‬
                                                           ‫بمعنی سرلگون باشد که سرازیر است‪.‬‬
 ‫کریبان فرو بردن و متفکر و متحیر بودن‬
                              ‫ههمست ‪.‬‬             ‫گال‪.‬‬   ‫ا همز ممدوده‌بروزن‌یر‬          ‫=‬   ‫سر آل‬

                                                  ‫گونند که مانند فلك‬            ‫را و چیزبرا‬             ‫کی‬
‫سرا ند پب‪ ۲‬نام کوهی‌است مذهور که‬
                                                  ‫و آسیا و گردون سر کردان وهمیشه در گردیدن‬
 ‫آدم صفی‌علهالسلام از بپشت بدانجا فرود آمد‬
                                                                                                     ‫باشد ‪.‬‬
 ‫«وقام کردولقش قدم او درآنجا هت» و بعضی‬
‫گویند نام شهرست بزر گے برلب دربا وان کوه‬          ‫بالف‬   ‫هيم هر دو‬   ‫با الی و‬       ‫»‬    ‫سر اماج‬



 ‫منوب بشآهنراست ‪ .‬و گوبند قبر ابوالبشر‬             ‫کشیده و بجیم زده ‪ ۰‬نوع را گونند‪,‬رآن چوبی‬
                                ‫در آ نحا اس ‪:‬‬            ‫باشد که بر کردن کاونهند وهچونب‌کراو‬
                                                    ‫اآبدان‬
  ‫لند" با لام * بر وزن و معنی‬
                            ‫سیرا‬                  ‫سته زمین را شیار کنند ‏ و بعضی باجیم فارسی‬
 ‫سراندیب است که کوهی باشد مشهور بقدمگاه‬            ‫است که کاوآهن رار‬     ‫جو «ی‬          ‫أ ورده‌اند و گفته‌اند‬


                                                                ‫بند وبعربی عم گوبند‪.‬‬
                                                                                   ‫آن کصن‬
                                   ‫ادم صفی ‪.‬‬
  ‫سرانگشتی ‪ -‬بطم کاف فارسی‌و‪-‬کون‬                   ‫و آخرکار باشد ‪-‬‬    ‫عاقت‬      ‫=‬       ‫سر انحام‬

                                                                         ‫وسامان کار را فر گومتف ‪۰‬‬
 ‫شین نقطفدار و فوفالی بتحتالی کشیده » نوعی از‬
   ‫آش‌آرد کروایند ‪ -‬وبحنرایسیرهکهای‌انگشت‬
                             ‫ويا مف لد ‪۰‬‬   ‫دست‬              ‫ملایکه کورویبان وحاملان عرش باشد‪.‬‬


    ‫نظامی کنجوی‪« .‬کنجینه ‪۵۸‬؟‪.‬‬                                      ‫سرآغوشی برآموده بگوهر‬
   ‫‪ = ۴‬از ‪:‬سر‪( | ۳‬واسطه) ‪ +‬کوفت (کوفتن) ‪.‬‬                 ‫‪ = ۴‬سراغوش = سراغوج ‪.‬‬
      ‫اس‬   ‫بیشترباین معبی ]ند‬   ‫‪ ۹‬مولف‬         ‫® ‪ -‬فس ‪:‬سرنگون ‪.‬‬         ‫درزبان کنونی«سر گوفت» ‏‬
```


### [2026-09-06T02:20:31.575Z] TOOL RESULT

```
==== BQT v2 leaf 176 full ====
 ‫ضا‬
  ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬
                                                              ‫نون ودال ابجد ‪ 0‬نام قصبه‌ایت درماوراءالنهر که‬
                                         ‫‪.‬‬   ‫بهم رسد‬
                                                          ‫‪۲‬‬                              ‫مولد کمال است ‪٩‬‏ ‪:‬‬
‫اول و انی بتحتانی‬
  ‫»|‬    ‫=‬    ‫‪۷۳1‬‬
                            ‫حجیر "‪۰‬یکر‬
                                  ‫‪۴‬‬          ‫‪2‬‬


                                                               ‫_ بن اول و ثالی» در نذه است‬        ‫خجی؟‬

                                                              ‫گویند‪.‬‬   ‫که لآرا چکاو کے خوانند و بعربی قبره‬
‫وجمیل وخوش صورت وصاحب حسن راگویند ؛‬
                          ‫ویضم اول هم آمده است ‪1‬‬              ‫خجو له بکر اول و فتح ثانی و لام‬
                                                              ‫وسکون واو »آبله گروانندکه ببب کارکردن‬


                                                   ‫بیان ششم‬
            ‫درخای نقطه دار ‪ ۳‬دال بی نقطه مشممل بر شانزده لغت و کنات‬

 ‫‪-‬دوای؟ جم اول ‪ ۰‬نام ذات | وصاحب ومالك را نگیوزبند ؛ وبا ذال نقطه‌دار‬
                                                                    ‫خداً خ‬
                                      ‫بارتمالی است همچو الهواله ‪ -‬و مخقف خود؟" | هم خوانده‌اند ‪.‬‬
                                                                                              ‫‪1‬‬




                                                   ‫(‪ )۷‬چك‪ .‬چش‪ :‬جوئی‪.‬‬               ‫(‪ )۱‬خم‪ -: ۱‬و‪.‬‬
  ‫روزه راه‬         ‫ده‬   ‫‪ ۰‬من آن و ‪-‬مرقند‬         ‫‪ - ۱‬شهری مشپور بماوراء النهر بر ساحل سبحون‬
  ‫در ‪ ۱4‬درجه و ‪ ۳۲‬دققهة‬               ‫ت‬
                                      ‫س)‬‫اوس‬
                                          ‫است « ممجم‌البلدان ‪ :‬خجندة » و اکنون در ترکستان (ر‬
      ‫‪ - ۴‬ظ‪ .‬مصحف«چفو»‬          ‫عرض شمالی و ‪۸٩‬‏ درجه و‪ ۲4‬دققة طول‌شرفیه ضمیمهةٌ معجم البلدان»‪.‬‬
  ‫بهلوی ‪rhic‬‏ ‪( uh -‬از ‪ :‬هو (خوب ) ‪٣‬‏ چهر(اصل نژاد ) ‪.‬‬                            ‫هرژ=ر‬
                                                                                      ‫هج‬          ‫(«‪.‬م ) ‪= ۴‬‬
   ‫اوستا_‪-»3601)1‬ل‪0‬ا«بارتولمه ‪۱۲۸۱٩‬‏ نبیر گے ‪»۹۰۱‬طبری ‪( ۲1[06‬خوش» خوب‪ .‬زیدا) «واژه‌نامه‬
  ‫‪ .‬دامفالی نیز ×‪٣[0‬‏ ‪ ,‬شهمیرزادی ‪7[1205‬؛ لفة نيك نژاد ‪ .‬خوب اصل و مجازاً بمعانی‬                            ‫‪۳‬‬
  ‫‪ ۴‬ب۔هلوی متأخر ‪: . ۷2۸۵۷۲‬هلوی اشکانی‬                                    ‫مکقور در متن آمده ‪ .‬رك‪ :‬هزیر ‪.‬‬
  ‫بازند ‪« 102۷‬هوبشمانس ‪4۵‬ج » « مسینا ‪. » ۲ : ۹۳۱‬بعضی ابن کلمه را از‬                                 ‫‪007‬‬
   ‫اوستابی_‪ )# 212210(, 6 ۵۷5 3/2010-‬مشتق دانسته اند ونولد که بحق دراين وجه اشتقاق‬
  ‫شکكرده » چون خدای فارسی و خواتای بهلوی بکلمةٌ ‪_ayÃtaWX‬‏ ‪ °‬با ‪o 2002802۷01‬‏‬
   ‫‪+ 142‬‬      ‫رت‬    ‫کبا‬
                      ‫سده )‬
                          ‫اد زن‬
                              ‫مزخو‬‫اقرب است و آنهم بسادسکریت_‪( 5802۷5 + 1018‬ا‬
  ‫‪ ( 52‬ازخود آغاز کرده) رابطه دارد ‪ .‬برای اطلاع از عقابد مختلف رك ‪ :‬بارتولمه ‪۰ ۲۹۸۱‬‬
      ‫استق ‪ , ۱۲۷‬هوشمان ‪.۱۷4‬تبعات ادرالی‪ .‬دارمستتر ‪ ۱‬ص‪ ۷۰‬بشتها ‪ ۲6۰ : ۱‬خرده اوستاه‪.۵۲‬‬
  ‫‪.‬‬          ‫* گربرسن ‪۶‬‬      ‫‪ ۰‬زبا کی ‪127‬‬           ‫‪2‬‬    ‫» اشکاشمی‬      ‫‪۵۰۹‬‬   ‫ص‬    ‫ا«اسفا ‪۱‬‬        ‫‪6‬‬     ‫کردی‬

       ‫گیلکی ‪830‬ا‪ .‬در بهلوی و پازند خواتای بمعنی شاه آمده و « خوانای نامك» بعنی «شاهنامه»‪.‬‬
      ‫اشتقاق عامداله است‬       ‫جه‬
                                ‫و‪-‬‬‫‪9‬‬                ‫فارسی بمعتی اله گرفته‌شده ورك ‪ :‬خداوند ‪.‬‬           ‫ارن‬
                                                                                                        ‫زا د‬
                                                                                                           ‫خد‬
                                                                                                  ‫برای‌معنی‌اول‪.‬‬
                                                    ‫‪ ۵‬خحچکول ‪ -‬رك ‪:‬ملتغافترقةٌ بابان کتاب ‪.‬‬
            ‫ب(رهان فاطع مه)‬
```


## [2026-09-06T02:20:46.092Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v3 leaf 571 (گپ) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==572' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T02:20:47.605Z] TOOL RESULT

```
=== BQT v3 leaf 571 (گپ) ===
[pdf page 572]
بیان سیم

درکاف فارسی بای فارسی مقتمل بر دو ‎<A‏
‏گپ- بقتح اول و سکون ‎tae” «ut‏ - بن‌اول. بروژن ومعن ی ‎BS‏

سفن پاش ‎٩‏ - ونان ‎BUSS Eos‏ | است که سخن کردن و حرف زدن وییان نمودن
کونند ۴ ج ‎aS gas‏ و سطبر و بز رکه چم باق

آمده است ۴

tole ‏بیان‎

در ‎GE‏ فارسی با تای قرشت مشتمل بر سه لغت
گت بنم اول و سکون ‎Ql‏ : بسعنی | قلزم » بسمنی ‎GY‏ کراف است ‎gin‏ سخن که
بز رک باشد و یمربی عظیم ‏ وکبی سکوبند ۵ - از حد واندازء کوبنده متجاوز باشد ‎٩‏ ۰
وبتر کی بمعتی کون باشد که عربان دیرخوانند. گقه ۷ - بن اول و فتح ثالی » بمعنی
‎pe OP‏ اول ورای قرشت بر وزن | کت است که بز رکه وعظیم و کبیرباشد .

‎ol‏ پنجم

‏در کف فارسی با ‎et‏ اد مشتمل بر دو ‎cal‏

‏گج + بفتح اول وسکون ثالی» لوعی وخاله سفید کنند؛ ‎only‏ معنی با جیم فارسی‌هم
از خاله ‎"Soa‏ ۳ پزند ‎oles‏ عمارت سازند | آمده است .

‏۱ - در خراسان وزبان لری بمعنی سخن است «فرهنگه انم" کردی 800 ( سخن +
کنتکو) «ژابا صس ۰۳۵۷ , اشکاشمی ‎Bap‏ (مکالمه) , زباکی 88۳ ( کلمه ؛ سخن) ؛ سنگلیچی
‎gap dah sy 0‏ ( مکالمه کردن ) « گربرسن ص۸۰-۷۹) ‎BAP 266۳0 LS.‏ ( کپ
زدن » سخ نکفتن) ۰ تهرانی 82۳ (سخن ‎Ay (SITs‏ : گفتن .

‏۴ - چون زن صوفی توخائن بوده‌ای دام مکر اندر ‎oy Les‏ ای
که ز هر ا شته روبی کپ زلی شرم داری. وز خدای خوش نی-

‏مولوی . مثئوی . چاپ میرزا محمود ص۳۲۸ وچاپ نیکلسن دفترچهارم ص۲۹۰: کپ.
۴ - هر دیدهای اطراف بروجرد و میلاخوری ‎BAP‏ (بز رکه) > شهندی ۰۲ کلپایگانی
‎eS) 8‏ بز رکه) «قاسمی» . ۴ - رك :گفتن + * - طبری ‎gat‏ ( بز رکه )
۰ «واژه نامه ‎ATA‏ . در مازندرانی ‎Endy oT‏ مردم فاری ‎Bat‏ (بز رکه) ورك :کته .
-رك : جپانگیری . ۷ - ره :کت . ۸ ‎ph‏
```


## [2026-09-06T02:21:00.313Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 613 614 615 616; do echo \"----- pdf page $n -----\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' incoming/BQT/BQT_v3_pages.txt | head -30; done"
}
```


### [2026-09-06T02:21:01.919Z] TOOL RESULT

```
----- pdf page 613 -----
[pdf page 613]
‎Clea”‏ ۱ » بنم اول ؛ بروزن وممنی
بستاج است که ‎ge‏ ادب و دلی و تند باشد ۴ .

‏گستاخ دست «کنابه از چابدست
وجلد و تندکار کننده باشد ۴ .

‏گستر ۴ = ‎ee‏ اول‌بروزن دختی؛بمعنی
پهن‌کننده و افرازنده باشد ‎٩‏ - و امرباین‌معنی
هم‌هت عنی پهن کن و بیفراز و ‎Merged‏
‏میاه وخار سفید را نیز گوبند .

‎Vo pal?‏ © فتح دال و سکون‌تون,
بععني پهن ‎OS‏ و فرو چیدن و فراز کردن
باشد .

‏گسترش ۷ ۰ بنم ارل و سکون آخر

‏که شین نقطه‌دار باشد , هرچیز راکه توان فرو

‎NAN

‏چید ‎oS uy‏ از دام وباط و فرش ۸ وامثال
آن

‏کته ‎٩‏ » بفتح اول‌بروزن ‎austen‏
‏مر کین باشد که فلا اسب و استر و خر وکاو
است .

‎Cire ‏نم اول و قتج‌ها‎ 5 re
----- pdf page 614 -----
[pdf page 614]
VAY

باشد و عربان خلیماامذا رگویند .

‎seal?‏ لور ‎eee‏ اول و دون, کتابة
از ‎ole‏ نواست که هلال باشد - و پیاله‌ای را لیز
کوند که از ‎Wh‏ و نقره باندام کشتی ساخته

‏باشند . این دو ‎cad‏ را ‎Wu Gays‏ باکاف‌تازی
نوشتداند .

‎cn eS Sa”‏ اول وکرتانی وسکون
لام ۰ پممنی گیختن باشد - و امر ب رکسیختن
هم هست ‎ce Sy NG ge‏ شو ۴

‏گسله ۴ - ین اول وکر تا
۷ ۰ بممنی گسيخته شده باشد .#۶

‏گصن ۴ - بنم اول و سکون ‎BU‏
‏ولون » ‎an Tyan‏ باشد که در مقابلسیری
است

‏اسب .

‏ی و فتح

‎. ‏-رك :کلیدن .گستن‎ ۱
gat on: ayo

----- pdf page 615 -----
[pdf page 615]
‎Ol‏ سیز دهم

‏در کف فارسی با شین نقطه دار مشتمل بربیست و پنج لفت و کنایت

‏گشی » بنتح اول وسکون ‎gb‏ » بمعتی
خوب و خوشی رفتار با ناز و تکیر و ‎Pk‏
‏باشد ‎٩‏ - و بمعتی کفتی ملاح هم بت آمده
است ۴ - و وسوسه و مزاحمت را لیز کفته‌انس
‎gale ids! gas‏ را کوین که ازجمله اخلاط آریع
است که ‎OT‏ خون و صفرا و سودا وبلغم‌باشد۴ -
‎Jods! Gs‏ را کویند و بعربی‌قللب‌خوانند؟

‎ga - * OL‏ اول بروزن مراد بمعنی
قراخ است که در برابر ‎a‏ باشد - و مىاضی
کشادن همهت که در مقابل بستن است‌سوبمفتی
فتح و ظفر هم آمده است ‎٩‏ - و خوش وخوشی

‎say‏ کویند ۷ - و ‎by‏ کردن لیر باشد از
‎Het‏

‏گشاأث نامه ‎ob ye‏ پادشاهانر! ‎aa S‏
‎Ty‏ بعربی منشور خوانند ۸ - و بمعنی عنوان
کتابت و فرمان هم هست یعنی آلچه بر سر
کتابتها نوسند ؛ ‎aly‏ لغت ‎GEL‏ تازی‌هم آمده
است .
‎ool’‏ دل ‌ بکر دال ابجد. ‎aS‏
‏ا زکرم و بخشنده باشد - و خوشحالی با فرح‌را
ی زکوند ‎٩‏ .
گشاده ‎OLS‏ - بنتم زای نقتطمدار ,
----- pdf page 616 -----
[pdf page 616]
aes ۱۸۱۹

استممال میکنند چنانکه کوبند: « عستمد گفت»
‎sins‏ مهیا شد وآماده گردید - و سیر وگفت را
یز گوبند ۷ - و بمعنی حك کردنمحوساختن
هم کفته‌اند ۸ - و خریزه را هم میگویند ‎٩‏
‎yews‏ حنظل لزآمده است ‎٩‏ - ویمعتی دیدن
ونظاره کردن هم بنظر رسیده است.
‎GAP‏ *۱- منم اول و فوقالی ‎BL,‏
‏کشیده . بهشت ‎SaaS‏ بمربی‌جنت‌خوانند.
گشتاسب ۱ م‌اول بروزن‌لهراسبء
دام برزخی است که ‎ole‏ خلق و خالق باشدبرای
رسیدن فیض حق ‎MT‏ و نام پادشاهی‌است‌ممروف
و او پدر اسفندیار رویین ‎of‏ بود . گوشد یکسد
و شصت ‎JL‏ پادشاهی کرد ودین زردشت ‎pty‏
‏و چون زردشت کته کردید بجای او مثصوب‌شد
وآیین زردشت را بریای داشت .

کنایه از مردم ضیح و بلیغ باشد ۱

گشاده هنگامان ۲ )1( = ‎ats‏
‏از فصول اریعه است که بهار و تابستان و ‎Sok‏
‏و زمستان باشد .

گشاسب " ه بسکون سین بی قله
و بای ابجد . همان کشتاسب مشپور است: که
پادشاهی بود پدر اسفندیار رویین تن و بکسد
وشصت ‎plesk JL‏ کرد .
```


## [2026-09-06T02:21:09.414Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 618 619; do echo \"----- pdf $n -----\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' incoming/BQT/BQT_v3_pages.txt; done"
}
```


### [2026-09-06T02:21:10.800Z] TOOL RESULT

```
----- pdf 618 -----
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

‏۵ مت - رك : ‎old‏ متفرقة پابان کتاب .

‎O‏ گنتن - ‎en‏ اول و فتح سوم » از :کف (۳ کو ) تن ( پسوند مصدری ) ؛ پپلوی
‎oye , 8‏ اول از ‎Lea,‏ پارسی باستان ‎BaUb_‏ « بارتولمه 4۸۲ > ‎yy‏ : لیب گس ۸4-
‎tho‏ کردی «نااع » وخی ‎xdy - 880 JS. . joy am‏ « استق ‎٩۷5‏ » ورلك:هوبشمان

‎tbogoftan . bogotan . botan CLS. « va ‏کنتن)«واژه‌نامه‎ ( baoten ‏ایضاٌ. طبری‎ ۰

‏سضن راندن . تکلم , صحبت کردن © بیان کردن » حرف زدن ».تقربرکردن - بنظم درآوردن .

----- pdf 619 -----
[pdf page 619]
‎oli‏ چهاردهم
در ‎GE‏ فارسی با لام مشتمل بر یکصد و سه لفت و کنایت

‎Sopris ‏اول وسکون‎ ac ۱ JF
PT ‏است و بعریی ورد خوانند - و بمعتی‌اخگ‎
‏هم‌هست - و را سرخ‌را یز کوبند - وطریق‎
‏معنی‌دولت هم میکندچنانکه گویند‎ Salil ‏کنایه‎
‏را می‌شنويم » یمتی بدولت‎ lel ‏د از کل تو‎
*. ۴ ‏توب وبکسراول,خاله بآ بآمیخنه را کوبند‎

‎pe = ۴ cur‏ اول ‎tty‏ بالف کشیده
و بجیم زده ۰ ‎gl‏ حلوائی است پاکیزه و عربان
قطابف میگوبند ؛ و بعضی گوبند نالیست بسیار
بازك و تنك مانندکاغن حربر و ‎MAT‏ شاسته
وتخم مرغ پزند ودرشربت قند ولبات ریز هکنند
و با قاشق و چمچه بخورد +

‏گل‌ار به = ‎pe‏ اول و کرثانی‌وهمزة
عضوم برای فرشت زده وفتح بای ابجد » ‎Sly‏
‏است که ‎LST‏ ازشامآورند و عنبر بید یزخوانشد.
‎aX‏ جانوران ‎GUL‏ است و بعربی جمده
گونشد .

‎Ge gel‏ اول و انی؛ کلی

‎ath *‏ سرخ رنگه بیاهی ‎ees bb‏ طین‌ارمنی

‏خوانند.. تبی راکه در ‎Ub‏ وبا و طاعون بهم‌رسد
‎cal gill‏ . گوبند وقتی در ارمن وبا و طاعون
عظیمی بهم رسید چنانکه معدودی چند مانده
بودنه چون آزابشان تفص کرددد در ‎IIT‏

‏می‌خوردلد +

‏گل‌اقر یطس ۴ - بکس ‎Sst‏ و تع
‎cll‏ و سکون قاف و رای فرشت بتحتالی‌رسیده
و طای حطی مضبوم بسین ‎Made‏ زده ۰ لوعی از
کل باشد و آبرا از جزایر ‎by‏ آورند. گوبند
اکر زن آبستن بر خود بندد بچة او را آسیبی
ارسد تا برسد .

‎WP‏ گو ه ‎٩‏ - بنم اول وکاف فارسی
بواو رسیده و فتح نون » بمعنی غازه و کلگونه
است و آن چیزی ‎th‏ سرخ که زنان بر روی
مالند .

‏گل ] گین کردن - کنابه از برز
کردن یمنی پرساختن ‎dha‏ و صراحی باشد از
شراب لملی .

‏له © پروزن نخاله ؛ بمعنی پیراهن

‎٩‏ - در اوراق مالوی (یپارنی) ‎WE‏ (کل‌سرخ ) » اوستا - ۷۵۵128 , ارمنی۷2۲۵
‎(Henning, A list of Middle Persian... , 2505 , IX, 1, p ۰ 88(‏ , پهلوی
‎gul‏ . ۷۵۲۸۵ ۰ ۷2۲۵2 , ممرب «ورد» ( بفتح اول ) 6 قس: ارمنی ‎vardges‏ «اسشق ‎tary‏
‏کردی 801 (کل سرخ ) ‎gal.‏ ( خار ) « ژاباس ۳۹۵» زازا ۷116 » ژابا س ‎ES tro‏

‎. gil

‏خوشنوبان فطایف با قلمپای شکر

‏جمله عاجز کشته‌اند ازخط ‎CUS gat‏
بسحاق العمه «رشیدی» .
‎yet‏ اقربعطی . ° ح کلگونه ‎(pn)‏ = کلغونه .
‎aro‏ بطم اول, درختی است ‎(pirus COMMUNIS)‏
از ‎o>‏ سیبی‌ها ‎GIT IS? (Pomactes)‏ س ۷۲۲۷ » دارای
ب رکه ‎TK,‏

‏میوء مخروطی شکل ولذید .

‏؟ - پپلوی ‎Bil‏ «منای ۷۲۷6 : 6۲ , رك : اسشق- هوبتمان ‎BIS ٩۷۷‏ .
۴ - مخفف «کولالج»(ه.م.) = کولاج(«.م.)ورك : کولانج:
```


## [2026-09-06T02:21:54.525Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON اغتراف ===\"; grep -n \"اغتراف\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5\necho \"=== MON گپ ===\"; grep -n \"گپ\" MON_part2.txt | head -5\necho \"=== MON گفتن ===\"; grep -n \"گفتن\" MON_part2.txt | head -3\necho \"=== FSF خدیو ===\"; grep -n \"خدیو\" FSF_pages.txt | head -5\necho \"=== FSF خواجه ===\"; grep -n \"خواجه\" FSF_pages.txt | head -3"
}
```


### [2026-09-06T02:21:54.641Z] TOOL RESULT

```
=== MON اغتراف ===
MON_part1.txt:14647:اغتراف: 6 [ع.] (مسصم.) آب یه 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:14647:اغتراف: 6 [ع.] (مسصم.) آب یه 
=== MON گپ ===
9095:اجرای آن به سرعت باید انجام گپرد. (ق.) 
20012:کیر: ۲ (- گیر - گپر] (.) خفتان. 
20526:کپی: 1-(0۴)0: [- کبی - گپی] )٩(‏ میمون 
29947:گپ: ««ع (- گب] (.) سخنء کلام. سخن 
=== MON گفتن ===
260:می‌گفتند و از مس سکه زده می‌شد و ده غاز 
1144:(عم.) آهسته سخن گفتن از روی خشم» 
1636:غزل: اه2مر [ع.] (مص‌ل.) سخن گفتن بت 
=== FSF خدیو ===
6627:     ‫خردباید و گوهر نامدار‬                   ‫بریده دل از ترس گیهان خدیو‬
10066:                                             ‫ببرد از رخت شرم گیهان خدیو‬
10343:‫شاهد برای واژة خدیو همین بیت را از‬
20118:‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬
20129:                              ‫گیهان خدیو‬                  ‫توگفتی نهشببودپیدانه روز‬
=== FSF خواجه ===
1299:                        ‫دیگر ت‬                         ‫باچنین کم‌دشمنی خواجه نیاغارد به جنگ‬
1315:       ‫تو لشکر بر آغال بر لشکرش‬                          ‫باچنین کم دشمنان کیخواجه آغارد بجهنگ‬
15630: ‫کی‌رهد ای خواجه گل ز تنگدلی؟!‬                                            ‫(تاریخ سیستان ‪:)۲۲‬‬
```


## [2026-09-06T02:21:55.518Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD page 75 (pdf 80) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==80' incoming/FFD/FFD_pages.txt\necho \"=== FFD grep gaub ===\"; grep -n \"gaub\\|گفتن\" incoming/FFD/FFD_pages.txt | head -10"
}
```


### [2026-09-06T02:22:00.589Z] TOOL RESULT

```
=== FFD page 75 (pdf 80) ===
[pdf page 80]
ماده‌های ماضی و مضارع فارسی دری وی

گفت < فارسی میانه +801 < ایرانی باستان 80-42 *. برای 12 -> آراست. 6۵0 صورت
اصلی ۶باع است» ۳ پیش از 1 به ؟ بدل شده است. 90ع صورت ضعیف ريشهٌ 8200 به
معنی «گفتن» است.

گوی + فارسی میانه 83۷ < ایرانی باستان 8200-2*. برای ۵ > آرای.

گماردن. گماشتن

گمارد < فارسی میانه ۰8070370 (گماشت) در فارسی دری به قیاس با «کاشت».
«کار» به وجود آمده است.

گمار + فارسی میانه ۰801037

گواردن

گوار + فارسی میانه 6۳837 < ایرانی باستان ۷1-127-۵*. برای 2-> آرای. 137 صورت
بالاندةٌ ريشهٌ ۴۵۲ به معنی «کردنْ» است. ۷۷1 پیشوند فُعلی است.

مادهٌ ماضی در فارسی میانه 8083770 بوده که جعلی است. «گوارد» فارسی دری
بازماندة ۹1-137-1۵* ایرانی باستان است. برای 1۵ -> آراست.

گوالیدن (:بالیدن)

گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.

=== FFD grep gaub ===
372:3 ۵ :گفتن
455:بوده است. به جای 2880021 می‌گفتند:
590:و 0810 ريشه است به معنی «گفتن».
1456:«گفتن». ۳۷ وازژه‌ای اهریمنی بوده» یعنی برای اهریمن و دیو به کار می‌رفته است.
1803:صورت ضعیف ۷۷۵و آن به معنی «گفتن» است. ۱
2032:معنی «گفتن» است.
2149:شده است. ريشهٌ ۷8۴ به معنی «گفتن» است.
2345:7 (ريشه - گفتن اهریمنی) ۵۳ 42 :۷۴
2347:7۷ (ريشةٌ بالانده + 472#) ۵۳ 0 : (ريشه -گفتن) ۰۱۶ ۷۵
2623:42 ۴۶ ۳ (ريشه < گفتن) ۱۳ ۰۶۶ ۷۹
```


## [2026-09-06T02:22:15.346Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON اغتراف ctx ===\"; sed -n '14644,14650p' MON_part1.txt\necho \"=== MON گپ ctx ===\"; sed -n '29944,29952p' MON_part2.txt\necho \"=== MON گفتن headword ===\"; grep -n \"^گفتن\\|گفتن:\" MON_part2.txt | head -5"
}
```


### [2026-09-06T02:22:15.437Z] TOOL RESULT

```
=== MON اغتراف ctx ===
فریب خوردن» سمغرور شدن. (امسص.) 
فریفتگی. 

اغتراف: 6 [ع.] (مسصم.) آب یه 
مشت برگرفتن» با کف دست آب نوشیدن. 
ات (ععابه [ع.] (مص م.) سر و تن 
شست‌و شو, 
=== MON گپ ctx ===
ححامت کند) شاج ححامت. 
کبه: (6-)2002ع (.) نوعی قالی که یودهای 
دراز دارد؛ خر سکث. 
گپ: ««ع (- گب] (.) سخنء کلام. سخن 
لاف و گزاف؛ سخن بهوده و دراز. 
کت 0 اطراف بروجرد و سیلاخور و 
ملایر؛ بزرگ» گلپایگانی؛ گنده. بز رگ ] 
(ص ) گنده و ستبر» بزرگ و ضخیمء کلان. 
کت ۲ (.) اندرون رخ داخل چهر ه. 
=== MON گفتن headword ===
14593:گفتن. 
31672:گفتن. ( 9ص تفر نکاه کرد 
32982:گفت. 01۱ (مص خم. امسص.) گفتن: 
32991:گفتار: 007۲: (امص.) گفتن: گفت. (.) 
33002:گفتن: 20- مهن اکتا رن
```


## [2026-09-06T02:22:16.574Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF خدیو entry ctx ===\"; sed -n '10335,10360p' FSF_pages.txt\necho \"=== FSF page tags near ===\"; grep -n \"pdf page\" FSF_pages.txt | awk -F: '$1>10200 && $1<10500' | head"
}
```


### [2026-09-06T02:22:18.223Z] TOOL RESULT

```
=== FSF خدیو entry ctx ===
                                                            ‫آرخو‬
                                                               ‫ازینسو طب‬
 ‫دکتر عبدالعلی‬      ‫شسته‬
                       ‫ذ فر‬
                          ‫گلغت‬
                             ‫از‬
 ‫طاعتی مصحح صحاح الفرس نیز به عنوان‬          ‫ردتاجای گردان کجاست‬
                                                               ‫نکگه‬
‫شاهد برای واژة خدیو همین بیت را از‬
 ‫فرهنگ وفایی به همان شکل نادرست‬           ‫(‪)۲-۲۲-۶۸۳‬‬

‫«سیامک بدست خود و رای دیو» در‬                                  ‫(رودکی ‪-‬نفیسی ‪۰۸‬‬

                 ‫پاورقی نقلکردهاست‪.‬‬         ‫سپر به پیش کشیدم خدنگ قهر تو را‬
‫همچنین دکتر محمد معین مصحح برهان‬          ‫ر چه سود کند؟‬ ‫سرپاید‬
                                                             ‫چو تیربرجگ‬
                                                                                                    ‫خرام‬
                                              ‫‪۸۰۳‬‬




         ‫شدی تنگدل چون نیامد خرام‬               ‫قطعات شکل نادرست این مصراع را از‬

‫نجستم همی زین سخن کامو نام‬                                             ‫لغت فرس نقل کرده است‪.‬‬

=== FSF page tags near ===
```


## [2026-09-06T02:22:30.720Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/leaf.py FSF_pages.txt 10343\necho \"=== leaf content ===\"; awk 'BEGIN{RS=\"\\f\"} NR==224' FSF_pages.txt | head -60"
}
```


### [2026-09-06T02:22:34.154Z] TOOL RESULT

```
10343 -> leaf(0based) 210
=== leaf content ===
                                           ‫‪۳۳۰‬‬


‫دلاقشت‌های گات‌ها ‪:)۹۷‬‬
                     ‫ا»د خ‬
                         ‫س(ریشت‬                            ‫سپهبد بکهژی نگیرد فروغ‬
‫بدنهاد‪.‬‬    ‫جزء دوم واه مرکب دژخیم‬                ‫زبان خیره پرتاب و دل پردروغ‬
‫از همین ریشه است‪ .‬فر دوسی‬      ‫بدسرشت‬            ‫(‪)۵-۸۲۳-۲۶۵۱‬‬

  ‫خود در بیت زیر «خیم» را معنی می‌کند‪:‬‬                                               ‫خی ‪4‬ش‬
           ‫گذشته سخن ياد دارد خرد‬                ‫ابزاری که باآنزمین را شیارکنند و خیش‬
                                                                 ‫کار ‪-‬کشاورز‪ .‬دهگان‪:‬‬
          ‫دگر خوی را انک خوانیم خیم‬                        ‫به شخی ککهرگس برو نگذرد‬
‫که بااو ندارد دل از دیو بیم‬                      ‫بدو گور و نخچیر پی نسپرد‬
 ‫(‪۸‬نرشیروان ‪)۵۶۴۲‬‬                                          ‫کنم چاه اآنبدرو صدهزار‬
 ‫در بیت زیر نسخه قاهره به جای بدخواه‬             ‫توانگر کنممردم خیش کار‬
                       ‫‪:‬‬‫تبط‬
                          ‫س ض‬
                            ‫اخیم»‬
                                ‫(بد‬               ‫(‪)۶-۲۵۱-۰۹۲‬‬
           ‫گرزم آن بداندیش بدخواه مرد‬                            ‫اندرز اسکندر به مادرش‪:‬‬

‫دفلرمنززند خود تیره کرد‬                                     ‫مرامرده در خاک مصر آگنید‬
 ‫(‪)۶-۷۵۱-۰۴۳‬‬                                      ‫گزفتار من هیچ مپراگنید‬
                             ‫)‬
                             ‫وزن‬
                               ‫دبر و‬
                                   ‫کو (‬
                                      ‫خی‬                    ‫به سالی ز دینار من صدهزار‬
                               ‫آب دهن‪:‬‬            ‫ببخشید بر مردم خیش‌کار‬
  ‫دزیدار [گیسوی شیرین ] پیران فرو ماندند‬          ‫(‪)۷-۴۰۱-۵۷۷۱‬‬
                                                                          ‫خیم (بروزن بیم)‬
‫‪٩(‎‬شیرویه ‪)۵۳۷‬‬                                    ‫خو طبع» طبیعت (صحاح‪ ,‬جهانگیری؛‬
                                                 ‫رشیدی» برهان) اوستا هثم ‪ 06۵‬نهاد‪.‬‬
```


## [2026-09-06T02:22:50.230Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n++} END{print \"leaves:\",n}' FSF_pages.txt\nfor n in 100 150 200 224 300; do echo \"-- NR=$n --\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' FSF_pages.txt | head -3; done"
}
```


### [2026-09-06T02:22:51.967Z] TOOL RESULT

```
leaves: 484
-- NR=100 --
                                                                                   ‫برع‬


-- NR=150 --
                                                ‫‪۱۳۹‬‬                                       ‫پرهیزیدن‬


-- NR=200 --
                                              ‫‪1۹۹‬‬                                                  ‫جرده‬


-- NR=224 --
                                           ‫‪۳۳۰‬‬


-- NR=300 --
                                           ‫‪۳۹۹‬‬                                      ‫ستودان‬
```


## [2026-09-06T02:23:02.368Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 213 214 215 216 217; do echo \"== NR=$n ==\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' FSF_pages.txt | head -50; done 2>/dev/null | grep -n \"خدیو\\|خدای\\|== NR\" "
}
```


### [2026-09-06T02:23:03.933Z] TOOL RESULT

```
1:== NR=213 ==
50:== NR=214 ==
101:== NR=215 ==
152:== NR=216 ==
202:== NR=217 ==
```


## [2026-09-06T02:23:08.588Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /خدیو/ {print \"LEAF(1based)=\"NR}' FSF_pages.txt\necho \"--- first lines of those leaves ---\"\nawk 'BEGIN{RS=\"\\f\"} /خدیو/ {print \"=== NR=\"NR\" ===\"; print substr($0,1,200)}' FSF_pages.txt | head -40"
}
```


### [2026-09-06T02:23:10.407Z] TOOL RESULT

```
LEAF(1based)=139
LEAF(1based)=205
LEAF(1based)=211
LEAF(1based)=411
--- first lines of those leaves ---
=== NR=139 ===
                                                                                     ‫پایمرد‬
                                                           ‫دستیار دستگیر یاری
=== NR=205 ===
              ‫همی تا آز باشد بر جهان چیر‬               ‫نبینی باغبان چون گل بکارد‬
 ‫نگردد جان مردم از گنه سیر‬              
=== NR=211 ===
                      ‫(اسدی ‪:)۷۹۳-۷۳‬‬                  ‫سپاهی بدین رزمگاه آمدیم‬
        ‫رنگ رنگ‬   ‫ز خرگاه و ازخیمۀ‬        �
=== NR=411 ===
‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬


              ‫پآسگاهی آمد سوی نیمروز‬              ‫فروختن عافروختن ]‪ :‬ف�
```


## [2026-09-06T02:23:19.760Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==411' FSF_pages.txt | head -60\necho \"###### p.159 area (NR=163) ######\"\nawk 'BEGIN{RS=\"\\f\"} NR==163' FSF_pages.txt | head -12"
}
```


### [2026-09-06T02:23:21.668Z] TOOL RESULT

```
‫کیهان خدیو‬                                  ‫‪۳۰۷‬‬


              ‫پآسگاهی آمد سوی نیمروز‬              ‫فروختن عافروختن ]‪ :‬فروزندة گیتی‪.‬‬
‫به نزدیک سالار گیتی فروز‬                          ‫ک‌نایه از خورشید و صفت برای‬
‫‏)‪(F-1۱۷۰7‬‬                                                            ‫خورشید‪:‬‬
                                     ‫گیلی‬                  ‫چو ازکوه بفروخت گیتی فروز‬
                         ‫منسوب بگهیلان‪:‬‬           ‫دو زلف شب تیره بگرفت روز‬
       ‫سیاوش سپر خواست گیلی چهار‬                  ‫(‪)۴-۸۸۱-۲۶۱۱‬‬
‫دو چسوبین و دو زاهن ابدار‬                                  ‫از آن چادر قير بیرون کشید‬
‫(‪)۳-۰۲۱-۴۵۸۱‬‬                                      ‫به‌دندان لب ماه در خون کشید‬
                              ‫گیهان خدیو‬                  ‫توگفتی نهشببودپیدانه روز‬
‫از گیهان ‪ +‬حدیو ]‪ :‬خداوند سرور]‪:‬‬                  ‫نهان گشت خورشید گیتی‌فروز‬
                          ‫ایزد‪:‬‬   ‫جهاندار‬         ‫(‪)۳-۲۸۱-۲۹۷۲‬‬


             ‫ناپاک دیو‬    ‫رگرمکاهن‬
                                 ‫فدی‬
                                   ‫و‬              ‫فردوسی گیتی‌فروز را صفت برای‬
‫ببرد دل از ترس گیهان خدیو‬                                          ‫پهلوانان هممی‌آورد‪:‬‬
‫(‪)۱-۲۱۱-۵۲۵‬‬

###### p.159 area (NR=163) ######
 ‫پیمودن‬                                    ‫‪1۵۹‬‬


           ‫تو ای میگسار ابزامبیلی‬                                         ‫(ویس ‪:۱۴-۴۳‬‬
 ‫بپیمای تاسر یکی بلبلی‬                                     ‫چو مادر دید روی دخترش را‬
            ‫بپیمود می ساقی و داد زود‬             ‫سهی بالاو نیکو پیکرش را‬
 ‫تهمتن شد از دادنش شاد زود‬                                                            ‫پیلوار‬
‫(‪)۶ ۵۲۵-۱۶۱-۲‬‬                                    ‫صفت مرکب از پیل ‪ +‬وار [‪ :‬مانند]‪ :‬مانند‬
 ‫(سیاست‌نامه ‪ :)۴۵۱‬دیگر روز بنده رابر‬                            ‫سل به رگن پل یلآ‬
 ‫لب دریا بردو در کشتی نشستیم و مطربان‬                      ‫تنش پیلوار و به رخ چون بهار‪...‬‬
  ‫سماع بسرکشیدند‪ ...‬و ساقیان شراب‬                 ‫(‪)۱-۵۴۱-۴۴۱‬‬
                                                                               ‫پیمان پ=یمانه‬
```


## [2026-09-06T02:23:30.234Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==205' FSF_pages.txt"
}
```


### [2026-09-06T02:23:31.913Z] TOOL RESULT

```
              ‫همی تا آز باشد بر جهان چیر‬               ‫نبینی باغبان چون گل بکارد‬
 ‫نگردد جان مردم از گنه سیر‬                   ‫چه مايه غم خورد تاگل برآرد؟‬

                     ‫چیره زبان و چیره سخن‬                                 ‫چیرگی‬
 ‫هردو به معنی‪ :‬سخنور» خوش‌سخن»‬               ‫(مرکب از چیره ‪ +‬ی مصدری‪ :‬های آخر‬
                             ‫خوش بیان‪:‬‬       ‫چیره در پیوند به «ی» به کاف پارسی بدل‬
          ‫بجستند از آن انجمن هر دوان‬                ‫می‌شود)‪ :‬پیروزی» برتری» تسلط‪:‬‬
‫یکی پاکدل مرد چیره زبان‬                                  ‫همه چیرگی با منوچهر بود‬
‫(‪)۵۱۸-۱۱۱-۱‬‬
                                             ‫کزو مگغیزتی پر از مهر بود‬
              ‫ولیکن توای پور چیره سخن‬        ‫‪۱-۲۲۱۰۸۲۷6‬‬

‫شبارده مکن‬
         ‫زبان برنگیا‬                                                         ‫ر‬
                                                                             ‫ي=‬‫جره‬
                                                                                 ‫چی‬
‫(ه‪)۸۰۱۲-۸۸۳‬‬
                                                            ‫پیروز» مستولی» مسلط ‪:‬‬
                                       ‫چیز‬          ‫جرابر دلت چیره شد رای دیو؟‬
                         ‫خواسته دارایی‪:‬‬
                                             ‫ببرد از رخت شرم گیهان خدیو‬
         ‫ندارد جز او گیو فرزند نیز‬           ‫(‪)۳-۷۵۱۰-۵۱۲۲‬‬
‫زنج و ز چیز‬
          ‫گرامی‌ترستش گ‬                           ‫چو چیره شدی‪ ,‬بی‌گنه خون مریز‪...‬‬
‫(‪)۴۰۶۲۱۰۸‬‬                                    ‫(‪)۲-۵۹۱-۰۸۹۲‬‬
                       ‫(اسدی ‪:)۰۰۱-۳۷‬‬                             ‫(اسدی ‪:)۰۷۲-۱۳‬‬
          ‫پذیرفتمش دخت و بسیار چیز‬                    ‫نشسته بر آهو عقاب دلیر‬

‫ونج و دینار نیز‬‫همان کشور گ‬                   ‫چو براسب گردی به ناورد چیر‬
                                                                 ‫(ویس ‪:)۸۲۴-۱۶۲‬‬
```


## [2026-09-06T02:23:38.007Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T02:23:38.015Z] TOOL RESULT

```


```


## [2026-09-06T02:23:40.850Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/carafe",
 "prompt": "Give the full etymology text for carafe, including the Italian/French/Spanish route and the Arabic gharrafa vs Persian qarabah alternatives."
}
```


## [2026-09-06T02:23:43.178Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7",
 "prompt": "Give the Persian خدا etymology section in full: Middle Persian form, Proto-Iranian reconstruction, what it is composed of, and any cited scholars (Hasandust, MacKenzie, Nyberg). Also any mention of خدیو or خواجه."
}
```


### [2026-09-06T02:23:45.504Z] TOOL RESULT

```
# Etymology of Carafe

The word "carafe" entered English in 1786, derived from French *carafe* (17th century). The French term came from either Italian *caraffa* or Spanish *garrafa*.

These Romance language versions trace back to Arabic origins, with two proposed sources: Arabic *gharraf* meaning "drinking cup," or Persian *qarabah* meaning "a large flagon."

As the source states: *"probably from Arabic gharraf 'drinking cup,' or Persian qarabah 'a large flagon.'"* This uncertain attribution reflects the etymological ambiguity regarding whether the ultimate source is Arabic or Persian, with both languages offering plausible candidates for the word's ancestor.
```


### [2026-09-06T02:23:51.936Z] TOOL RESULT

```
# Persian Etymology of خدا

## Middle Persian Form
The Middle Persian form is **hwtʾy** (pronounced /xwadāy/), rendered in Book Pahlavi as an Aramaic ideogram **MRA** (meaning "lord").

## Proto-Iranian Reconstruction
The ultimate source is **\*hwatā́wHā** ("lord, god") from Proto-Iranian.

## Composition & Cognates
The entry notes this word has "religious and secular connotations." Related cognates include:
- Avestan **xᵛaδata** ("self-determined")
- Bactrian **χοαδηο** (khoadēo, "lord")
- Northern Kurdish **xwedê** and Central Kurdish **خوا** (xwa)
- Sanskrit **स्वधा** (svadhā́)

## Related Terms
The etymology section explicitly mentions **خود** (xod, "self"), **خدیو** (xadiv, "lord, master"), and **خاتون** (xâtun, "lady, noblewoman") as related words.

## Cited Scholar
**D. N. MacKenzie** is referenced in the References section for his 1971 *Concise Pahlavi Dictionary* entry on "xwadāy."

No mention of Hasandust or Nyberg appears in this entry.
```


## [2026-09-06T02:23:57.237Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87",
 "prompt": "Give the Persian خواجه etymology in full — Middle Persian form, proposed origins, any connection to خدا/xwadāy, and cited sources."
}
```


## [2026-09-06T02:23:58.419Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%BE",
 "prompt": "Give the Persian گپ etymology in full — is it related to گفتن, is it a loan, what sources are cited?"
}
```


### [2026-09-06T02:24:03.727Z] TOOL RESULT

```
# Persian Etymology of خواجه

Based on the Wiktionary article, the Persian خواجه etymology is:

**Ultimate Origin:** The word derives from a Middle Indo-Aryan reflex of Sanskrit उपाध्याय (upādhyāya, "teacher; preceptor; spiritual adviser"), transmitted "via Central Asian intermediaries."

**Proposed Form:** The Central Asian loaning source most closely resembles an unattested *vājjhāa, matching Sindhi واجهو (vājho).

**Cited Parallels:** The article notes comparison to Tamil வாத்தியார் (vāttiyār, "teacher; instructor; family priest").

**Sources:** The etymology cites two academic references by Garnik Asatrian (2011, 2012) published in *Iran and the Caucasus*.

**Regarding خدا (xwadāy):** The article makes no connection between خواجه and خدا/xwadāy. These appear to be etymologically unrelated words with different Sanskrit sources—خواجه from upādhyāya and خدا from a different origin.
```


### [2026-09-06T02:24:04.313Z] TOOL RESULT

```
# Persian گپ Etymology

Based on the Wiktionary entry, the Persian etymology is limited in detail:

**Etymology 1** states: "Compare the verb _[گپتن](/w/index.php?title=%DA%AF%D9%BE%D8%AA%D9%86&action=edit&redlink=1 "گپتن (page does not exist)")_ (gaptan, goptan)." This suggests a relationship to the verb form, though the connection isn't explicitly defined as derivation.

**Etymology 2** notes the term comes "From [Old Persian](https://en.wikipedia.org/wiki/Old_Persian "w:Old Persian") \[Term?\]." However, the specific Old Persian source is marked as unknown.

The entry emphasizes cognate relationships across multiple languages (Mazanderani, Gilaki, Talysh, Kurdish) rather than providing a detailed internal Persian etymology. No scholarly sources are cited for the etymological origin. The entry indicates gaps in documentation by marking the Old Persian source as missing and noting various terms require transliteration or native script additions.
```


## [2026-09-06T02:24:10.418Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88",
 "prompt": "Give the Persian خدیو etymology in full — Middle Persian form, relation to خدا/xwadāy, meaning, and cited sources."
}
```


## [2026-09-06T02:24:11.539Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/good-bye",
 "prompt": "Give the full etymology of good-bye, including the \"God be with ye\" origin and the influence of good day/good night. Also say what etymonline says about the word good itself if mentioned."
}
```


### [2026-09-06T02:24:17.012Z] TOOL RESULT

```
# Persian Etymology of خدیو

**Middle Persian Form:** 𐭤𐭲𐭩𐭥 (htyw /⁠xadēw⁠/)

**Origin:** The word derives from Bactrian χοαδηο (khoadēo), meaning "lord."

**Meaning:** In Persian, خدیو historically denoted "lord, master, mighty ruler, or king" in archaic usage, and later referred specifically to the khedive (Ottoman viceroy of Egypt).

**Related to خدا/xwadāy:** The entry lists خدا (xodâ) under "Related terms" but does not explain a direct etymological connection between the two words. The sources do not establish that خدیو derives from خدا.

**Cited Sources:** The etymology cites Nicholas Sims-Williams' work on Bactrian language in Encyclopædia Iranica (1988) and a 2012 article by Jafari Dehaghi and Emadaldin Sadri on "Bactrian Loanwords in New-Persian," both tracing the ultimate origin to Bactrian rather than to internal Persian word formation.
```


### [2026-09-06T02:24:18.176Z] TOOL RESULT

```
# Etymology of Good-bye

**Origin and Development:**
The word "good-bye" emerged in the 1590s as a contraction of "godbwye" (1570s), which itself derived from "God be with ye," a phrase dating back to the late 14th century. The term was "influenced by good-day, good evening, etc." Various intermediate forms appeared in the 16th century, including "God be wy you," "God b'uy," and "God buoye."

**Spelling Variants:**
The word has been written as "goodbye," "good bye," and "good-by," reflecting its evolution from a full phrase into a unified word over several centuries.

**Related Parting Salutations:**
The term parallels "adieu," which similarly expresses kind wishes upon departure. Both serve as general parting salutations in English, though they originated from different linguistic traditions—English versus French/Latin respectively.

**Note on "Good" Etymology:**
The source briefly mentions that "good" comes from Old English "gōd" meaning "excellent, fine; valuable; desirable," but does not provide extensive etymological detail about the word itself in this particular entry.
```


## [2026-09-06T02:24:28.571Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hwat%C4%81wH%C4%81",
 "prompt": "Give the full reconstruction entry: composition (*hwa- + *tāwH-), meaning, and all descendants (Avestan, Bactrian, Middle Persian, Sogdian, Khotanese, New Persian, Kurdish)."
}
```


## [2026-09-06T02:24:30.897Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-",
 "prompt": "Give the full entry: meaning of the root, derived terms including *ǵʰu-tó-, and descendants in Indo-Iranian (Sanskrit havate, Avestan zauuaiti) and Germanic (*gudą)."
}
```


### [2026-09-06T02:24:31.344Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:24:37.265Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵʰewH-

## Meaning
The root means "to call on, invoke."

## Derived Terms
Key formations include:
- *ǵʰéwH-e-ti (thematic root present)
- *ǵʰuH-éye-ti (éye-present)
- *ǵʰuH-e-ti (zero-grade root present)
- *ǵʰuH-eh₂
- *ǵʰuH-tus

## Indo-Iranian Descendants

**Sanskrit:** The page shows हवते (hávate) from Proto-Indo-Aryan *źʰáwHati, though the entry does not list *ǵʰu-tó- specifically.

**Avestan:** 𐬰𐬀𐬎𐬎𐬀𐬌𐬙𐬌 (zauuaiti) appears as a Proto-Iranian form meaning "to call on, invoke."

## Note on Germanic
The webpage provided does not contain information about Germanic descendants like *gudą. The document focuses on Indo-Iranian, Celtic, Balto-Slavic, Tocharian, and other language families, but Germanic cognates are not discussed in this particular entry.
```


## [2026-09-06T02:24:42.696Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gud%C4%85",
 "prompt": "Give the full etymology of Proto-Germanic *gudą: which PIE root(s) it is derived from (ǵʰewH- 'invoke' vs ǵʰew- 'pour'), and the descendants (Gothic guþ, Old English god)."
}
```


## [2026-09-06T02:24:42.920Z] TOOL CALL #59: WebSearch

```json
{
 "query": "Persian خواجه etymology xwāja Middle Persian xwāgāy Asatrian upādhyāya"
}
```


### [2026-09-06T02:24:48.844Z] TOOL RESULT

```
# Etymology of Proto-Germanic *gudą

## PIE Derivation

The etymology is debated. Two main hypotheses exist:

1. **From ǵʰewH- ("to call, invoke")**: Would yield meaning "(that which is) invoked," though this derivation has phonological issues—"the derivation from *ǵʰewH- would normally result in long ū."

2. **From ǵʰew- ("to pour")**: Would mean "libated, poured as part of a liquid offering," possibly via earlier sense of "idol" or "spirit in burial mound." However, this root appears in Germanic only in extended form *ǵʰewd-.

An alternative hypothesis connects it to Proto-Indo-European *gʷʰew- via Old Church Slavonic gověti ("to revere").

## Key Descendants

- **Gothic**: guþ
- **Old English**: god (ancestor of Modern English "god/God")
- **Old Norse**: guð/goð
- **Old High German**: got
- **Old Dutch**: got

The word originally had neuter gender but "eventually became masculine when referring to the Christian god" as Christianity spread.
```


### [2026-09-06T02:24:52.916Z] TOOL RESULT

```
Web search results for query: "Persian خواجه etymology xwāja Middle Persian xwāgāy Asatrian upādhyāya"

Links: [{"title":"خواجه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87"},{"title":"xoʻja - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/xo%CA%BBja"},{"title":"hodja - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/hodja"},{"title":"Khoja - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Khoja"},{"title":"خواجہ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%DB%81"},{"title":"Khawaja - Wikipedia","url":"https://en.wikipedia.org/wiki/Khojas"},{"title":"Hajji Firuz","url":"https://en.wikipedia.org/wiki/Hajji_Firuz"},{"title":"Kashmiri Khwaja","url":"https://en.wikipedia.org/wiki/Kashmiri_Khwaja"},{"title":"Khwaju Kermani","url":"https://en.wikipedia.org/wiki/Khwaju_Kermani"},{"title":"Akhshunwar","url":"https://en.wikipedia.org/wiki/Akhshunwar"}]

Based on the search results, I can provide information about the etymology of Persian خواجه (xwāja):

The Persian word خواجه (xwāja) is ultimately derived from Sanskrit उपाध्याय (upādhyāya). The word ultimately derives from a Middle Indo-Aryan reflex of Sanskrit उपाध्याय (upādhyāya, "teacher; preceptor; spiritual adviser"), via Central Asian intermediaries.

Various Middle Indo-Aryan reflexes are attested from all stages, including Maharastri Prakrit forms, but the Central Asian loaning source most closely resembles an unattested form matching Sindhi واجهو (vājho, "Hindu schoolteacher").

The word has been widely adopted across multiple languages and regions. Khawaja (Persian: خواجه, romanized: khwāja) is an honorific title used across the Middle East, South Asia, Southeast Asia and Central Asia, particularly towards Sufi teachers. In Persian, the title roughly translates to 'Lord' or 'Master'.

The search results reference Asatrian in the Wiktionary sources but do not provide detailed information about Asatrian's specific work on this etymology or about the Middle Persian form xwāgāy that you mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:25:02.642Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON خدیو ===\"; grep -n \"خدیو\" MON_part1.txt | head -5\necho \"=== MON خواجه ===\"; grep -n \"^خواجه\\|خواجه:\" MON_part1.txt | head -5\necho \"=== MON گپتن ===\"; grep -n \"گپتن\\|گپیدن\" MON_part1.txt MON_part2.txt | head -5\necho \"=== BQT v2 خواجه ===\"; awk 'BEGIN{RS=\"\\f\"} /خواجه/ && /پهلوی|هوبشمان|اوستا/ {print \"NR=\"NR}' BQT_v2_pages.txt | head -8"
}
```


### [2026-09-06T02:25:04.642Z] TOOL RESULT

```
=== MON خدیو ===
=== MON خواجه ===
11218:خواجه‌سرا» خصی» خادم؛ آغا. . (عسم.) 
57715:خواجه: (قد. -6(005-)2812 (ص.) بز رگ 
88436:خواجه. عنوانی که در ممالک اطراف ایران 
=== MON گپتن ===
=== BQT v2 خواجه ===
NR=238
NR=239
NR=279
NR=307
NR=312
NR=393
NR=404
NR=409
```


## [2026-09-06T02:25:09.318Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 57715 ctx ===\"; sed -n '57710,57725p' MON_part2.txt 2>/dev/null || sed -n '57710,57725p' MON_part1.txt\necho \"=== which file ===\"; grep -c \"\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-06T02:25:09.402Z] TOOL RESULT

```
=== MON 57715 ctx ===
انگلیسی دانند و شاید در ساختن این صیغه به 
سیاق اسم مفعول عربی» نظری به مفهول 
کلمه آنکلت, مذ کور هم داشته‌اند. مشرو طه 
مشروعه: (سیا.) حکومت مبتنی بر مشروطه و 
منطبق با احکام اسلام. ضح.- این اصطلاح را 
شیح فضل‌الله نوری و طرفداران او بکار 
بر ده‌انك. 

مشروطه‌خواه: ۱۰-0 [- مشر و طه 
خواهنده] (ص‌فا.) (سیا.) آنکه طرفدار 
مشر و طه است؟ مشر و طه طلب. 
مشروطیت: ۹ [ع.] (مص جه.) 
مشروط بودن. (سیا.) حکومت مشروطه. 
مشروع: تتگد [ع.] (امف.) انجه موافق 
شرع باشدء چیزی که طبق شرع جایز باشد. 
مسر وعه.: (۸)۵- ۱۵۹۲۱۲ (ع. مش وعه | 
=== which file ===
MON_part2.txt:94500
MON_part1.txt:99339
```


## [2026-09-06T02:25:12.005Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57710,57722p' MON_part1.txt\necho \"=== MON خدیو any ===\"; grep -n \"خدیو\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T02:25:12.087Z] TOOL RESULT

```
و مانند آن). 

خواتسيم: سآنهد [ع ۲ () ج. خاتام. 
انگشتری‌ها. مهر ها. 

خواجه: (قد. -6(005-)2812 (ص.) بز رگ 


صاحبت؛ سر و ر» خداوند. مالدار» دولنمند. 


فرهنگ فارسی معین 

=== MON خدیو any ===
```


## [2026-09-06T02:25:17.585Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 238 239; do echo \"=== NR=$n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | tail -25; done"
}
```


### [2026-09-06T02:25:19.597Z] TOOL RESULT

```
=== NR=238 ===
                      ‫‪8‬اجیکی‬
                           ‫‪0‬جة ت‬   ‫‪-۱‬‬
                               ‫‪1‬درله‬                  ‫رك ‪ :‬اسقا ‪۲: ۱‬ص ‪۰۲‬‬       ‫‪۵‬‬
   ‫» درهندوتر کیه ‪( 805 -‬درهندوستان ‪ -‬اصطلاحاً خوجه بییروان اسمعیلیه‬       ‫شمارة ‪ ۸‬ص ‪۹۱۱‬‬
 ‫اطلاق شود ) ‪ ,‬معرب آخنواجا « تفس» « دزی ج‪ ۱‬ص‪٤٠٩‬‏ ‪ ۰‬آفای پورداود این‌کمه رامر کب‬
  ‫از ‪ ۵۷2 = 2۷27 :‬اوستابی بمعنی خود ‪ 16) +‬که درآخرکلمات اوستابی درآبد بمعنی لل و‬
  ‫همچنین‪.‬جمعاًبمنی کسکه دارای‌خودییوشخصیت مستقل‌است‪,‬دانته‌اد‪ «.‬حافظ شبرین سخن ‪, ۲ ۳۷‬‬
  ‫صفیر = چه)دانسته‌اند تیه‌ای‌در‬   ‫وند‬
                                     ‫س‪+‬‬‫یای)‬
                                          ‫((خد‬
                                             ‫كلوی‬
                                                ‫چی به‬
                                                    ‫بعضی اصل] نرا«خواتای‌چث» از خواتا‬
  ‫نزدیکی درباچة زره (هامون ) سیستانست ‪.‬انرا هم « کوه خدا» گویند وهم «کوء خواجه » (اين‬
           ‫درباچه و کوه ترد زرتشتبان جنبةٌ تقدس دارد ) واين امرشاید موند فرضةٌ اخیرباشد ‪.‬‬
   ‫‪ - ۷‬بین این دومعنی خواجه درحقیقت هیچگونه اختلان طفظ ومعنی نست و خواخه‬
   ‫درهردو مورد بمعنی بزر که وسرور وصاحب است بااين تفاوت که درمورددوم درقدیم «خواجمسرا»‬
   ‫میگفتند یعنی بزر كك و سرور اندرون» و چون مردم نامحرم لمیتوانته است درحرم راه بايد در‬
  ‫دستگاههای استبدادی قدیم مردالی را که بابد برای خدحت تریدت شوند خصی مکردلد ‪.‬کم کم‬
   ‫مردم ‪,‬در استعمال » لفت « سرا » را از دبال خواجه انداخته و بهمان لفظ خواجه افتصار‬
   ‫کرده‌اند‪ .‬وزراصطلاح عامه خواجه بمعنی‌خصی شده «وآغا » همکه بخواجه سرابان خضی اطلاق‬
  ‫کرده‌اند درحقیفت ترجمةٌ ترکی همین خواجه است وهآغاباشی» معننی بز رکه خواجه سرابان وا‬
                ‫دارد « باد کارسال ‪ ۳‬شمارة ‪٩-۷‬‏ ص ‪ > ۰۳۱-۱۳۱‬ورك ‪ :‬دائرتالمعارف اسلام ‪.‬‬
         ‫هصهفدرحة ‪۰۸‬‬

=== NR=239 ===
              ‫سلطانيم‬     ‫بنندده بارگاه‬                    ‫‪ - ۴‬من وتو هردو خواجه تاشالیم‬
   ‫«لتان ‪.۰۹‬‬
           ‫ک‬
                                          ‫‪ - ۴‬ویسی گوبند بمناسبت پیمودن آسمانها ‪:‬‬
            ‫آت شیرءاینت مبشرنلام ‪.‬‬                           ‫خواجة مساح ومسیحش غلام‬
    ‫نظامی گنجوی‪ 2 .‬گنجنه >‬

  ‫® _ یهلوی ‪( ۲۷3‬بيهودە‪ .‬تاچیز)‬                  ‫خوار (خوارنده) از مصدر خواردن ‪.‬‬      ‫‪۴‬‬
                                                                               ‫‪:‬‬     ‫‪ ۰‬او بوال ‪۵‬‬

        ‫که بنده درنظر خویش خوار میدارد ؛‬                  ‫چه جرم دید خداوند سابق الاسم‬
   ‫«کلتان ‪.۰4‬‬
  ‫هلوی ‪. 52۷5‬‬           ‫‪ - ۱‬اوستا ‪ ( 2۳01۵۷2‬رفاه‪ ,‬آسایش ) هخرده اوستا ‪ ۲۹۱‬ح ‪۱‬‬
   ‫کردی ‪ . 725‬اففانی ‪ ۰ ۲2۷1‬بلوچی ‪« 72۷‬اسنق ‪.٩٤۹٩‬طیر‏ ی‪( ×4 ۲‬خوب) «صاب‌طبری‪.*۱۱۳‬‬

                                                                                ‫بقه ازصفحهٌ ‪۹۷۷‬‬
  ‫‪ #‬خواب ‪-‬بروزن تاب ‪ .‬پهلوی ‪ 08۷1‬درنیکبه ‪» ۵۳۱2‬سانسکربت ‪ › 8۳۷5‬اوستا‬
  ‫‪: 2062‬س ‪٩۵‬‏ ‪ ۵۷ ۰ ۸۹,‬و ‪ ۸۹۲‬کردی ‪ , 81۷6۲ ۰ 0۷61‬اففانی ع ‪۰ ۵۲‬‬
   ‫بلوچی ‪« ۵۷‬استق‪ .»۵۹4‬گیلکی ‪ 0۵5۰‬فریزتدی ‪ ۷۷21‬برنی ‪W۷4‬‏ نطنزی ‪« 7101‬که‪۱ .‬ص‬
   ‫‪ , ۹‬سمنالی ‪ . 02113‬سنگری ‪» ۷05‬سرخه‌یی ‪ , ۷۷0‬لاسکردی ‪ ۰ ۷5۷‬شپم‌رزادی ‪05‬‬
   ‫د کت ‪۲ .‬ص ‪ ۷۸۱‬طبری ‪« 05‬صاب طبری ‪ ۰ ۲۲۳۰‬درارا که ولرستان نیز ‪ ( ۷01‬مکی‌تژاد)؛‬
  ‫حالتی که برائر ازکار باز ماندن حوای ظاهر درانان وحیوان یدید آمد و اعنای تن را راحت و‬
                                 ‫‪.‬ر زجامه مانند مخمل‪.‬‬
                                                    ‫آسایش بشند؛ لوم ‪ ۰‬ضد‪ :‬بیداری ‪ .‬غفلت پ‬
```


## [2026-09-06T02:25:40.089Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 134 135 136 137; do echo \"--- NR=$n first/last ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -2; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | tail -2; done | cut -c1-200"
}
```


### [2026-09-06T02:25:41.531Z] TOOL RESULT

```
--- NR=134 first/last ---
  days.  —  L.  caniculdris,  fr. eanicula.  See  prec.  word  and  -ar.
Canidae,  n.  pi.,  the  family  of  dogs,  wolves,  foxes and  jackals  (zool.)  —  ModL.,  formed  with  suff. -idae,  fr.  L.  canis,  ‘dog'.  See  next  woid. canine,  adj.,  pertaining  to  t
Derivative :  cantilever,  tr.  v. cantillate,  tr.  v.,  to  chant.  —  L.  cantillatus,  pp.  of cantillare,  ‘to  sing  low’,  dimin.  of  cantare,  ‘to sing’.  See  cant,  ‘slang  of  
Derivative:  cantillat-ion,  n. cantle,  n.,  the  hinder  part  of  a  saddle.  —  ONF. cantel,  corresponding  to  OF.  chantel,  ‘corner, piece’  (whence  F.  chanteau,  ‘hunch  of  bread�
--- NR=135 first/last ---
  chant),  ‘corner’.  See  cant,  ‘slope’, cantlet,  n.,  a  small  cantle.  — -  Formed  fr.  prec.
word  with  dimin.  suff.  -et. canto,  n.,  chief  division  of  a  long  poem.  —  It., ‘song’,  fr.  L.  cantus,  ‘song',  fr.  cant-(um),  pp. stem  of  canere,  ‘to  sing’.  See  cant
capitulate,  intr.  v.,  to  surrender  on  terms.  —  ML. capitulatus,  pp.  of  capituldre,  ‘to  draw  up  the heads  of  an  agreement’,  fr.  L.  caput,  gen.  capitis.
‘head’.  See  capital,  adj.,  and  verbal  suff.  -ate. Derivative:  capitulat-ion,  n. capon,  n.,  a  castrated  cock.  —  ME.,  fr.  OE.  capun, fr.  L.  caponem,  acc.  of  capo,  ‘castra
--- NR=136 first/last ---
 Gk.  xojrrsiv,  ‘to  strike,  cut,  cut  off’,  xorrog, ‘a  striking;  toil,  suffering,  pain’,x6p.[j.a,  ‘a  piece cut  off ;  a  short  clause’,  xotuc,  ‘chopper,  cleaver, billhook
Derivatives :  capon,  tr.  v.,  caponier  (q.v.),  capon- ize,  tr.  v.,  capon-iz-er,  n.
capybara,  n.,  a  South  American  rodent  (Hydro- choerus  capybara).  —  A  Tupi  word.  Cp.  Cavia, cavv.
car,  n.  —  ME.  carre,  fr.  ONF.  carre,  fr.  VL. carra,  a  word  of  Celtic  origin;  cp.  OIr.,  MW. carr,
--- NR=137 first/last ---
  ‘cart,  waggon’,  Bret,  karr,  ‘chariot’,  L. carrus,  of  the  same  origin  and  meaning,  gave birth  to  ONF.  car,  F.  char.  L.  currus,  ‘chariot’, is  independent  of  the  abo
roccio,  carry,  carriage,  charabanc,  charge,  chariot. Derivative:  car,  tr.  and  intr.  v. carabao,  n.,  water  buffalo.  —  Sp.,  from  Philip¬ pine  native  name.
Derivatives:  eard-ed,  adj.,  card-er,  n. card,  n.,  a  piece  of  pasteboard  for  playing.  —  F. carte,  fr.  Late  L.  carta,  ‘a  leaf  of  paper;  paper’, fr.  L.  charta,  ‘a  leaf  
Cardamine,  n.,  a  genus  of  plants  of  the  mustard family  (hot.)  —  ModL.,  fr.  L.  cardamina,  fr.  Gk. xxpSxaivr,,  ‘a  kind  of  cress',  a  word  formed  by Dioseorides  fr.  xxpSxpov,
```


## [2026-09-06T02:26:04.578Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==219' KLN_1966.txt | head -3 | cut -c1-300\necho \"=== also leaf for carafe check: what is at leaf 130 (p~236) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==131' KLN_1966.txt | head -2 | cut -c1-200"
}
```


### [2026-09-06T02:26:06.292Z] TOOL RESULT

```
 See  -cyte.
cytology,  n.,  study  of  the  structure,  functions  and life  history  of  cells  (biol.)  —  Lit.  ‘study  of  cells’, compounded  of  cyto-  and  -Xoyta,  fr.  -Xoyop, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy. Derivatives:  
cytoplasm,  n.,  the  protoplasm  of  the  cells  (biol.
=== also leaf for carafe check: what is at leaf 130 (p~236) ===
lo-  and  melancholy. Calonyction,  n.,  a  genus  of  plants  of  the  morning- glory  family  (bot.)  —  ModL.,  compounded  of calo-  and  Gk.  vuxtio;,  ‘nightly’,  fr.  gen. vuxtop,  ‘nig
calori-,  combining  form  meaning  ‘heat’.  —  L. calori-,  fr.  color,  ‘heat’,  fr.  calere,  ‘to  be  hot’.
```


## [2026-09-06T02:26:36.924Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zav ===\"; grep -n \"zavaiti\\|zbayemi\\|zav-\\|zbā\" BRT.txt | head -10\necho \"=== BRT gaub/gub 482 ===\"; grep -n \"gaub\\|1gub\\|gub-\" BRT.txt | head -10"
}
```


### [2026-09-06T02:26:36.998Z] TOOL RESULT

```
=== BRT zav ===
5211:—  Hat    ^wä    .  .   m^rrta  .  .   vibaryn  *°oi iiiata..*°oi*y.io.ii;\ti0.iz6{'7'i); — «J tat  3p»n  iincaiti  H'i  yavS/ariltamV.$.^; 16;  —  Oft  um  spay3jlsd.)  I>m9  äia  va?ls.. vupata  'vi  ti/ra  *iumata(sd.)  ^.^^.35; —   ' cataarB  pirsnä  (sA)  v^ärayBis  'vi  pahqm  ' Yt/^44;    —    nanm    «J  (sd.)  'vi    ava.-  '• ginplsm  V. /Äio;  —  aai  ti  ifps  */rasil- vqyää  . .  'vi  hapid.karsvairTi  (IP.  als  AP.) YLÄ9;  —  mit  Gen.  part  statt  Akk.:  yai  , nsit  sünS  . .  aSanham  astqm  'vi  apqmca  \ urvaranqmca    barmtun  (sd.)  frajasqn  V.   ■ 6.  46.  p)    sonst:    un'ä^qmcit  zbayemi '7-i    imat   vard   Yt/2.3;  3J;  —    ahumat raüttnat  (sd.)  vaÄi/fym  vaoiaia  k>mcit  art- h3ui  .  .  °oi  P.  jj;    —    asmamm  .  .  yS  . rtulakiitö   'oi   *5«Vi'a  (sd.)    Yty.  a;    — ya^numca  'vi  sqm^a  V.2J.4;4.  f)  bei  1 Ellipse  des  Verbums :   cim  'oi  yamd  "an  ; wen    (richtet   sich)    das   Gebet?" 2".         b)  'gegen,  contra',  in  feindlichem Sinn:  daiAhupatayS ..  ai'ajasmts  'oi  Aas- nayS  xrvlfyätl/  Yt  10.8;  8;  —  ya^a  yat  < AaOtam    ava^t  .  .  'vi   vTsö  V.  18.  i nSit  .  .  *tyanJm  (sd.)  . .  xit3  mäidayasnls  ).
5388:auniäa.bäzav-
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6427:•  j.  asiä.hak-  Adj.  'der  Asay  anhängend, ergeben':  tDttß . .  'JiSgit  (NSn.)  Srmaili/.- hägtt  Y.  $8- 1-  a)  NSn.  'kägst  als  Adv. 'in  Ergebenheit  gegen  A':  vTspaica  alte 'hsgst  ärmaitii.hägft  (zbayemify  yazama- daEca  "und  all  diese  (rufe  ich  an)  in  Er- gebenheit gegen  A.  und  Ä.,  und  wir  beten sie  an"  Y.  -]!.  ii.
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
7662:■»«zav-
7692:•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
7697:"arazav-
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
=== BRT gaub/gub 482 ===
4968:■finu  tiaiy  gaubataiy  'vam  jatä  Bh.2.1 4, aü<^  ty<r  kartam  °v<^  visam  vasha  i^ur^-
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
9802:•  p.  gaub-  V.  'düir^.    Praes,  z  gauba-. Med.    i)  'sich  nennen,    erklären,   aus- geben für  — ',  mit  Nom.:  vakyazdätj'  Ayt^ bardiye^  a^nM^d/jBh.j.Ö;  9,  ^.  18,  r.18,19;
9804:au  Gunsten  von  — ',  mit  Gen.  (statt  Dat): käram  hyJ^  däraya'vahaus  gaubalaiy  Bh. 3.  9;  —  hatnih^iyä  abava"  uiä  fravar- lais*agaubc^ta  Bh.2. 16".  a)m!tNeg, sva.  'den  Gehorsam  verweigern',  von Truppen;  käram  .  .  Ayi^  manä  naiy  gau- bataiy'&h.2.6,3.3,i4;2.T,\o;  —  käram .  .  hy^  manä  naiy  gaubätaiy^^  Bh.  2.  14. ntp.  gmoel  'er  sagt'  (vgl.j-ii/j*  g'"')''  np.  ^ly'ija^. —  'I  Text  unsicher.  —  'i  Konjunktiv?
10847:yam  D.6. 1;  X.i.  r,  6.  i,  Ao./.  1,  D.  <f- 4;  —  a^ura^mazdä  ..  kaieu  darayt^v^um yam  adadi^  .  .  vaina  J'urJ'mazdahJ' därayt^va/'ui'  yJ"  D.  4. 1 ;  Bh,  /.  5,  6,  13, D.  ff.  4;  —  k^bajiyj'  .  .  paruvam  ida ya^  aAa*  Bh. /.  loj  15;  —  tyaiy  paruvä ya  Bh.  4,  9;  —  Aauv  '_>'«*  aöavir  *uva- Jaiy  Bh. /.  16;  10,  12,  2.5,  ^.  5,  i3i  4-2; —  adam  'yer  amiy  asagartaiy  Bh.  2.14, 4.2;  /.  16,  2,3,  4.2J,  Bh.b-j9,  D.ö".4;  — fravartis  hyJ'  madaty  yj'  agaubata  Bh. 2.  12;  —  Uevam  kä  yt^  Aya^  aparatn *aby  Bh.  4.  5, 14, 19;  —  S  mana  taumaya tyaiy paranam  yi  aAa''Bh,t.4; — ^dui'ita- faranam'sd.)  vayam  ya  amahy  Bh,7,4;  — 9  -yl  (AP.)  agarbiyam  Bh.4.3;  3;  — dlrayJ'vahaus  yahya  Bh,  J.  9,  D.  j,  4.  j, 8,  g,  sj.  I,  X./.  2,  3.  3,  5;  Am.  /',  2;  — arlaxid^^'a  y^  (statt  GS.)  puh'^^  Ao.  /.
15963:•  p.  pätiä''uvaray-  Adj.  'aus  Patis''uvara stammend, /'arfjf^örer'"':  ^gaubruvc^  'ris darayc^vahaus  .  .  arstibarj^  D.  8.
17802:•  p.  fravartay-  m.  EN.  eines  Meders,  der sid)  gegen  Darius  I.  empörte,  Phraories: 1  martiyj^  'tis  nätnt^  hauv  udapatatä madaiy  Bh.  2.  5;  13",  4.  2,  Bh.  e;  —  Aauv •iis  Aya*  mädaiy  xsäyäitiyJ'  agaubatä  ~' 2.  12;  —  iära*  msd(r  .  .  hatniViyJ' abava'  abiy  avain  'lim  aHyavc^  Bh.  2,  5; —  par%ava''  utä  variäna^ . .  °lais  *agau- ba'tä  Bh.2. 16;  —  karam  fyam  'tats  Bh.
19040:ioatard  N.  2/;  2/,  68;  —  es  ist  das  Prae-  draujani^  akam  rt'  zara*iara*  sham  n' dikatsnomen  des  vorhergehenden  positiven  aJam  naimaiy  taumä  Bh.^.  13;  I.  ig;  — Satzes  zu  ergänzen:  -viiarS ,  .  ratu/ris  n'  yadiy  imäm  dipim  vainshy  .  .  naiyäii *avrJari>  H.  gS;  gg,  104,  57—59^',  —  vikanähy  Bh.  4.16;  11,  17;  —  mafyo'  .. Aa  he  asti  Spsrstis  aipi.pänmnäi  ioa  avakyä  paruv  *%aäayi^  (sd.)  /yir*  mana asaone  «°  atiaipiparTmnai  V.Ä107;  —  kartam  naisim  vamavätaiy  Bh.4.8;  — paoirJm  ..iyao^manqm  vinzimmm  «=  bi-  mit  Ellipse  von  asäy:  yäha  im<^  haiiyam timN.4.^0.  b)  das  Verbum  hat  modale  n'  äurvxtamßh.4~T-  zu  2):  karam  ., Fonn  oder  Bedeutung:  n°  dtm  .  .  bitlm  Ayc^  mattä  n*  gaubaiaiy  Bh.  2. 6,  7,  10,  14, väUrn  paiiip>rfi?mta  bva  (Sp.  919  u.)''  J.  3,  14;  —  yaä^ä  gaumätJ'  .  .  vt&am  .  . V.J&29;  —  n°  akmäi  *ä  *tyanTm  {sA.)' n' paräbari^  Bii.1.1/^.  3)  in  ungewöhn- «*  vTvJpsm  xitü'^  .  .  aoi  vTse  n'  astö  n° ,  lieber  Stellung":  tya^  adam  n°  bardiy«^ ultänahl  HnmüHl  (sd.)  Y,  12, y,  —  «"  h!  amiy  Bh. /.  13;  — yanaiy  dipim  n°  nipiltäm apastaväne'^  .  .  äamam  V.ig.  j;  —  a'  zJ  akunaus  X.  7.  3.  b)  im  gAw.;  zu  I):
19394:—  manS  J'ur<^tnasds  upasiam  baratuv . .  Uta  imam  dahySum  . .  pätuv  D.  4. 3 ;  — vas^i  (^urJ'mazdäkJ'  manacS  däray<^- vaAaui"D.4.2;  —  iya*  mana  kartam  utä fyc^maiy  /iS'ö*  kartam  X.7.4;  —  avam käram  .  .  hyj*  mana  naiy  gaubataiy*^ Eh.2. 6,  j,3,  14;  2.14.  zu  1  b):  J'urt^- masda  ya'ha  avaina*  imäm  bümim  *yau- d<rHm  (sd.)  pasüvt^dim  martä  fräbart^ mam  (s.  i  i  b)  . .  D.  61 4 ;  — pasavo^  dahyUui mana  abavJ'  Bh.j.  a,  4,  iz.  zu  3): kari^  hy<^  hamüi'iyc^  mana  naiy  gau- &ataiy*'>  Eh.  2.  7,  10.  b  n)  im  jAw.; zu  I  a):  Hat . ,  mana  asti  vjjaymift^m  . . attivam  asti  vJmamiiftim  Yt  /.  a;  — s.  noch  bei  a.  zu  1  b):  mana  raya  .  . pawasla  staorüta  upairi  tarn  vTcarmta Yt  5.  89;  /.  a6  (?).  zu  a):  ya%a  .  . Os  zaofff  mana  yat  ahurakt  matda  Yt ig.  8a;  V.  ig.  14;  —  ar»hu^  y3  mana yai  ahurahe  mazdä  P.  40;  —  zugleich zu  1  a):  manada  yatmm  yat  ahurahe mazda  a^rasca  P.Jp.  11)  schwach- tonige  Formen  stehen  a)  enklitisch i)  hinter  dem  ersten  Wort  des  Satz-  oder Versteils,  von  dem  sie  aber  a)  durch  ein andres  enklitisches  Wort  getrennt  sein können;  a)  hinter  einem  Praenomen; 3)  selten  in  anderer  Stellung;  b)  pro- klitisch5>;  das  hochbetonte  Wort,  an  das sie  sich  anschliessen,  hat  keine  bestimmte Stellung.  I)  Akk,;  a)  im  Ap.;  zu  a  1): avada  mam  cita  amanayJ"  Eh.  2. 6;  — y^a  mam  kame^  Bh.4.4;  D. ö. 4, 17-3)
20066:•  p.  marduniya-  m.  EN.  eines  Persers, Mardonius:  *gaubrtan^  nämt^  °yahyä pu%'^J'  parst^  Bh.4. 18.
```


## [2026-09-06T02:26:52.220Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9780,9810p' BRT.txt | grep -o \"^[0-9]\\{3,4\\}\\|  [0-9]\\{3,4\\}  \" | head -20\necho \"--- raw around ---\"\nsed -n '9795,9803p' BRT.txt | cut -c1-160"
}
```


### [2026-09-06T02:26:54.058Z] TOOL RESULT

```
--- raw around ---
ai.  i,',yhäyai-  Adj.  —  Pü. ;  gJs/andän  daiisa, Sfi.:  gflsj-zläj/avasäj/T.
•  j.  *gao'iÄya-'>  Adj.  'das  Rind  hegend und  pflegend':  vaslreiiratahda  gave  hii- tiäohe  'hyeAeät ''  «ar/  asaonS  Vr.  /.  9.
BAinouiiiAi,  Altinn.  Wb.
■gaona-  48a
*dya-  Adj.,  zum  V.  'dä^y)- ;  vgL  goodäya»-.  — Pü. !  gÖsfandSti  dätrir.  —  D  So  K  7  B;  NA. •dy.  —  »)  Fälschlich  gäidy  N.  /o
•  j.  gao'pivanhav-  m.  EN.  eines  Gläu- bigen :  °»ÄJu/  asaonB  Yt,  13.111.
Eig.  'Rinder  fett  machend,  mästend';  "fhan- hau-  Adj.,  PPA.  (5209.4).  zum  den.  Praes.  3t 'fivah'ya-  [S  26S.  38,  30)  'siaiyiri'.
•  p.  gaub-  V.  'düir^.    Praes,  z  gauba-. Med.    i)  'sich  nennen,    erklären,   aus- geben für  — ',  mit  Nom.:  vakyazdätj'  Ayt^ bardiye^  
I  — /ravarti^ Aya"  mildaty  xsäyakiye^  agau- '  batä  Bh.2.iz.  a)  'sich  erklären  für —,
```


## [2026-09-06T02:26:59.950Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"•  *[jgp]\\.  *.\\?zav-\\|zbayemi\\|•  *j\\.  *zav\" BRT.txt | head -10\necho \"--- search zav- V ---\"\ngrep -n \"zav-  *V\\.\\|zbā-  *V\\.\\|zav-  V\" BRT.txt | head"
}
```


### [2026-09-06T02:27:00.041Z] TOOL RESULT

```
5211:—  Hat    ^wä    .  .   m^rrta  .  .   vibaryn  *°oi iiiata..*°oi*y.io.ii;\ti0.iz6{'7'i); — «J tat  3p»n  iincaiti  H'i  yavS/ariltamV.$.^; 16;  —  Oft  um  spay3jlsd.)  I>m9  äia  va?ls.. vupata  'vi  ti/ra  *iumata(sd.)  ^.^^.35; —   ' cataarB  pirsnä  (sA)  v^ärayBis  'vi  pahqm  ' Yt/^44;    —    nanm    «J  (sd.)  'vi    ava.-  '• ginplsm  V. /Äio;  —  aai  ti  ifps  */rasil- vqyää  . .  'vi  hapid.karsvairTi  (IP.  als  AP.) YLÄ9;  —  mit  Gen.  part  statt  Akk.:  yai  , nsit  sünS  . .  aSanham  astqm  'vi  apqmca  \ urvaranqmca    barmtun  (sd.)  frajasqn  V.   ■ 6.  46.  p)    sonst:    un'ä^qmcit  zbayemi '7-i    imat   vard   Yt/2.3;  3J;  —    ahumat raüttnat  (sd.)  vaÄi/fym  vaoiaia  k>mcit  art- h3ui  .  .  °oi  P.  jj;    —    asmamm  .  .  yS  . rtulakiitö   'oi   *5«Vi'a  (sd.)    Yty.  a;    — ya^numca  'vi  sqm^a  V.2J.4;4.  f)  bei  1 Ellipse  des  Verbums :   cim  'oi  yamd  "an  ; wen    (richtet   sich)    das   Gebet?" 2".         b)  'gegen,  contra',  in  feindlichem Sinn:  daiAhupatayS ..  ai'ajasmts  'oi  Aas- nayS  xrvlfyätl/  Yt  10.8;  8;  —  ya^a  yat  < AaOtam    ava^t  .  .  'vi   vTsö  V.  18.  i nSit  .  .  *tyanJm  (sd.)  . .  xit3  mäidayasnls  ).
6427:•  j.  asiä.hak-  Adj.  'der  Asay  anhängend, ergeben':  tDttß . .  'JiSgit  (NSn.)  Srmaili/.- hägtt  Y.  $8- 1-  a)  NSn.  'kägst  als  Adv. 'in  Ergebenheit  gegen  A':  vTspaica  alte 'hsgst  ärmaitii.hägft  (zbayemify  yazama- daEca  "und  all  diese  (rufe  ich  an)  in  Er- gebenheit gegen  A.  und  Ä.,  und  wir  beten sie  an"  Y.  -]!.  ii.
8472:brauchten Pflanze :  *h<ata  nS  rnhma  bans- mana  ratu/risi  ^ris.uri'ara  (sd.)  cyävaitis aäaya  'rayti  (NP.)  anhsnl  ".  .  wie  gross sollen  die  Pflanzenstengel  sein?"  N.i^o;  — yezi  *paitila  (sd.)  °varh  upa-doo^litt  ratu- /ri/H.ioi.  S.  auch  3.  a)  oft  neben Feuer,  Wasser,  Rind,  Himmel,  Erde  usw. : xshiivayeiti  ätrmt  .  .  ap^m  .  .  gqm  .  .  °rqin V.f).4Z;  33,  i/.  I,  2,  6,  9;  —  haca  a^rat .  .  Opal  .  .  z^mat  .  .  gaot  .  .  "rayiJf  V. ;/. 10;  —  aHiS  .  ,  apas^a  ttmasca  'rayhsca Ytij.jS;  aS.  86,  Y.ytj.a,  8;  —  asnäalca apäatca  z»mäatca  'rayüatca  Vr.  7. 4;  — hs  äp?m  staoiti  .  ,  zqm  .  .  gqm  .  .  'rqm H.  7.3;  —  ys  gqmcä  ahmcä  dät  apascä 'räsctl  vat^kli  y.  3-^.1 ;  —  yS  gqm  tasö (sd.)  apaslS  °rasca  Y.si-T,  —  vlspä  bal- iazä  apqmca  gavqmea  'ranqmca  Y,52.  a; J2. 7 ;  —  nasuspaim  .  .  äsirysnie  .  ,  apasca Zimasca  'rayäsca  V.  6.y,  /.j,  2/.3,  Y.  j.  16, 2.16,  Vr./Ö.3,  G.2.6;  —  ntzbayemi  zqm .  .  äppm  .  .  'rqm  asaonim  V,  ;p.35;-  — imat  vö  sps  jaiüyemi  . .  tfmO  . .  'rä  Y.
9548:arjnm  mainyüm  /ramiUm  aspahe  'pa (IS.)  Yt;p.29;i¥.i8,zi,r4.9;  —  ahmli . . üjasat  vaztmnö  i'sri^raynS  uftrahe  'fa ■  Yt. /4- n;  P-J-i  —  nizbayemi  iistrtni  .  . \gius  'pa  Y.if}.3T,  Yt&i6,  74.7;  —  he I  'pa  varäzaie  Yt  ;^  1 5 ;  —  maiiahe  'pa  Yt |j4.23;  —  bUzahe  'pa  Yt  74.25;  —  yat dim  us;a  usdi'qnayat  .  .  '^raltaonS  m^?- yahe  -pa  kahrkäsahe  Yt.  J.  6 1 ;  —  m»rrjahe 'pa  vär^iiahe  Yt/4. 19,  /9.35;  —  zaf- nimnpitt  .  .  :^ar^n3  m^rjyahe  'pa  fra^usap Vt/'>.34.  Undeutlich:  ratufris  *n.liri- A-ayi  'pa  näij  payauhs  nSit  sun5  'pa payai?h5  ratufris  v>hrkaya  'pa'a  paya- uha^a  N.j()*',  [V,  7.  a:  lies  maxHJ!'^
13221:w?)  Vr,  //.  1 9;  —  numawiä  asiii  uzdälä (näml.  z/ie^ri)  paiil  avat  stuyi  Y.  72. 3  3".  3)  'ansetzen,  anstellen,  veranstal- ten': urva'i:qmHi  zbayemi  avi  tmat  varo uzdätsm  YtJ2. 3,
20399:j.  'iD'Srazav-  in.,  Du.  Bezeichnung iner  a frischen  Schöpfung,  vll.  eines Sternbilds:  nizbayemi  'zu  ^pourvs  *:^a%/ltd yüßis/ff  mairtivä  *d3mqn  'ich  rufe  an  die beiden  M.  im  Süden,  die  ewigen,  die  am besten  kämpfen  von  der  Schöpfung  der beiden  Geister"  V.  ig.  42.
22442:'besingen,  einen  Sang  dichten  auf  — ' (Akk.):  *yavat3  %ivä  matda  *ilaomT ujyäcä  (iSPA,)  "(immer)  so  lang  ich  dich, Q  M.,  lobe  und  besinge"  Y.4:_J,  8;  — yS  va  asä  ufyäni  manaüS  vohQ  apaourvlm (sd.)  Y.  2Ä  3 ;  —  asäunqm  va>3uhJl . . fravalayS  staomi  zbayemi  ufyemi  Y,  ly.  18; —  k3  nB  stavat  .  .  yazäite  .  .  ufyät  .  . */rinät  .  .  paiti^sanät  Yt  /_J.  50.
22814:•  j.  ^varah-  Adj.  (auch  fem.)  'beim  Ordal verwendet,Ordal-';  urva%qmäti.%d^ zbayemi avi  imatvarS{%A.^uzd3t>m.. avi  raoynyqm 'ranhim  (AS£)  ". .  zu  der  Ordalbutter" Yt  12.  z*\
27448:•  j.  srü-,  srvä-'>  f.  i)  'Nagel'  der  Finger und  Zehen:  paiti  te  m>rrfa  aiS^su/la  (sd.) ima  'va  (AP.)  va^ayant  V./7.9;  9;  — imsn  ts  'vh  minya  aisxt/fa  kyär»  arlta- yaslä  . .  "diese  Nägel  sollen  dir,  0 Vogel  A.,  als  Speere  dienen  . ,"  V.  17. 9; 10.  a)  Du.  '(beiderlei  Nägel  sva.)  die Nägel  der  Hände  und  FÜsse">:  yat  tarn ..varasasla  *hqm.räsayaj3ha ..  'vaf{AD.)ca *upa.%W3nsanAa  "wenn  du  dir.. und  die Nägel  zuschneidest"  V.  ij.  4;  —  ir  (Sp. 6a I  o.)  aisqm  paiti  *srvi  (AD.)'*  a^a äruxf  . .  upa.dvqtaiti  "auf  deren  Nägel kommt  ,.  herzugeflogen"  V.  7.  a4,  37,  g, 41;^.  14  (vio  sruye)**;  —  srvabya  marfim ava.kanSi/  "du  sollst  für  die  (abgeschnitte- nen) Nägel  ein  Loch  graben"  V.  ly. 7.  a)  'Hom'  der  Tiere  (und  tierähn- lichen Wesen,  s.  Komp.):  gSu/  .  .  yim upairi  sntye  (AD.)*'  sanal  (Sp.  1590  o.) amö  Yt,  14.  7.  a)  Piur.  mit  Aafia  Name eines  Sternbilds  (?) :  nitbayemi  m^ntuiSp. iiT4  0.)..nizbayemi  kapta  sraps  {AP.)i^ b.imya  V. /p.  4a,  3)  'Hom'  als  Stoff, 'Homstück'  (nur  Komp.  und  Ableit).
27763:•  j.  zavanö.sästa-  Adj.  (fem.  Uä-)  'durch den  Ruf  belehrt,  angewiesen':  ana  buyä fsd.)  'ta  "so  mögest  du  dich  durch  den Ruf  weisen  lassen"  Yt,  5,  9.
--- search zav- V ---
```


## [2026-09-06T02:27:04.917Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '27735,27775p' BRT.txt | cut -c1-240"
}
```


### [2026-09-06T02:27:04.991Z] TOOL RESULT

```
•  j-,  g.  zav-,  zbä-'*  V.  'rufen'.  Praes. 2  sava-,  5  sBm>;  ^  zaosav,  5  +  7  zao- tftv-'>,  24  tiaya';S' AOT.  x  zävii'-.  —  PPfP. 'tbata-;  PFP.  'saoya-.
1)  'Jemanden,  etwas  (Akk.)  lufen,  an- rufen, aufrufen':  t!ng  sbayä  vanhiu^ uxhäis manankö  "die  will  ich  rufen  mit  den SpTÜchen  des  guten  Smns"  Y.4&.  14;  — thsla  mZ  nqma  sbaya^a  ¥1,75.49;  4.2 {^baySit);  —  
(Akk.):  at  ta  mdi  däiS  (Sp.  671  u.)  as»m hyat  mä  zaozaomi  Y .  43. 10.  3)  'ver- :
rufen, verwünschen'^':  %räyd ..afrivalanhs tavairtti  . .  gäus  zagtärpm  savaiH  "drei  . . sprechen  fluchend  Verwünschungen  aus., das  Rind  verwünscht  den  Priester"  Y.  //. i;   2,  3.  a)  Med.  'sich  verwünschen,
'zavan-  1668
verfluchen':  cahwärB  :^aiS  (sd.)  tavanU V.1S.11.
mit  aiwi  'au&ufen,  auffordern':  yasea.. matdayasnanqm  .  .  aiwi.tBzuyanqm'°^-. imq  vals  nBit*visaiteframrOite(sA)  "wer von    den  (dazu)   aufgeforderten   M.    .  ."
Y.Ä4.
mit  a  (sca)  'heranrufen',  Gottheiten: amt^  sptntS  vatihüS  srjrüH  nSman  atbaya (iS.)  Y.  75.  I,  Vr.  6.  I.  a)'mit  Inf.:
3ca  %itiä  (nämL  miirTm)  zbayäi  (iS.) avaiMe  Yt  /o.  77,  78.
mit  upa  'anrufen',  Gottheiten:  ta  hasHt upajsbayälg'"^  .  ,  fravasayB  Yt  13.  69;  — upa  usaahm  upa.tbaya^  andvlm  Vt.5. 62.  Wertlos:  upa.tbaya  Vyt  43;  — upa.zbayata  Yyt.  3S,  3g.
mit  US  'herausrufen,  excitarc',  Gottheiten : yä  {namL /ravasays)  uzbaiä"^  ..  fra- lasmte  Yty.42.
mit  ftJ  'herabrufen',  Gottheiten:  nizba- ymi  mi'krfm  V.  iq.  15;  lst^  35-39**. 4!^;  —  nizbayaauha  ..  vatauhjm  daOiqm V.  ig.  13;  yf.*,  34.  Wertlos:  *nisia' \yaila  Vyt.  24;  —  nitbaya  Vd.20.
ai.  hävate,  jukSmäii,  }6kaväi,  ki/äyali;  mp.  vgl- äiiäj^n.  —  Pü. :  Landau,  Sü. ;  {satn^hväna- yiium,  äkärayiluvi;  frätliayilum;  a,  noch No.  5,  g.  —  >)  D.  i.  ä-'Erweitemng;'  au  an--; ■.  Bthl.  Stud
—  S)  FQ.:  val  burlär  im  ha!  indaann,  erl.: SnSsem  at;  asi  ki  itän  gmeii  iu :  nyäiänH  i lä  ö  yajl  im  vam  tüH  ö  yai.    —    *)  S.  No.  a.
—  7)  VgL  indram  . .  ävase  k(rsimahe  RV. 3.  16.  I,  USW.  —  B)  NA.  taia.ib';  s,  Sp. 400  o.  S.  die  Var.  yäva  si',  Mf3  u.a.  — 9)  Pü.:  rp  if,  ind  (aoch  in  V.  iS.n;  s.  Sp. PahlVend.  705.  10),  s.  daiu
—  10)  Statt  •EttPun*  geschr.,  S  i^S.  1 1  d,  Pii. : apar  giifiSr,  —  ■■)  So  NA.,  aber  korr.  aus •yanle.  —  "i  %  304  H.  3^-
•  g.  'zavan-  n,  'Ruf;  ä  ttiBi  ra/ir^rSi 'v'iiig  (15,)'*  jasatä  "kommt  her  zu  meiner Unterstützung,  wenn  ich  rufe"  Y.  2Ä  3 ;  — yahmäi  ''z'5«tf  (LS.) "  jimä  ktnäuiä  (sd.) Y.  29.  3.
Zum  V.  =«.-.  —  VgL  ■•tavan-  EN.  —  ai.  vgl.
höman-  n.,  woiu  sich  savan-  siellt  wie  j.  asaa.
lu  asmait-;    i.  srayan-  No.    —    Pü.:   /a  i»j.
aby  Google
'zavan-
1669
»'in.  —  ')  Einen  AP,  aui  'zava-  (ai.  hdva-  \ m.)  halle  ich  Iroti  RV.  /.  183.  5  Rr  weniger ' wahrscheinlich,  weil  in  Y.  29.  3  das  Ziel  schon duTcb  den  Dativ  zum  Ausdruck  kommt  (Sp. 495  n»-)-
•  j.  'zavan-  m.  EN.  eines  Gläubigen: gaomatB  'vanS  . .  asaanif  "des  G.,  Sohns des  Z  .."  Yty.  125.
Wohl  KuTzname;  vgl.  'zaj/an-.
•  ').  tavana-  n.  'Ruf;  Anrufimg". KorapA.  —  Zum  V.  tor-,  —  ai.  Aävaiia-  n.
•  j.  zavanö.sästa-  Adj.  (fem.  Uä-)  'durch den  Ruf  belehrt,  angewiesen':  ana  buyä fsd.)  'ta  "so  mögest  du  dich  durch  den Ruf  weisen  lassen"  Yt,  5,  9.
Npü. :  an  bid  ba  ^ähis  mirä  pand.
•  j.  zavanö.sii-  Adj.  'der  auf  Anruf,  wenn gerufen,  hilft';  apqm  napättm  .  .  aHätam 'sunt  Yt/p.  52;  —  cihra  vB  buyänl  ma- sänä  n^ra  vS  *sav3  (VP.)"'  "offenbar sollen  eure  Grosstaten  werden,  offenbar di
Vgi.  j-ii^<jwjt.fln-.  — t)  D.L  'sm,S,  \268.\3.
s.  Mf3. ■    j.  zavanö.svan-   Adj.  sva.  'su-.    mm (näml.  Mihra)  ..  'sva  (NS.)  aki  sürB  Yt. 10.  76.
an-Part.  zum  V.  sav-;  s.  Bthl.  IF.  10.  195.
•  j.  zavano.srüt- ''  Adj.  'auf  den  Anruf hörend':  satavaisS  ..  'srtUS  (NSm.)"'  Yt i3'  44J  —  satavals?m  . .  •srBt>m  Yt  i^. 43  j  —  mihnm  .  .  •srBhm  Yt.  io.  61.
ai.  havanairüt-  Adj.  —  ')  F  l  hat  zweimal  11.  —
•  j.  '"utyeiti  zavavaf  hyatiia  mazäyascil
voku"-  Vyt  ?o  '*.
Pü.:/fl  ;^äiiiht.  —  0  Wo.  will  avaval;  vgl. noch  Sp.  1 164  No.  3.
j.  ia-^a>->/a:  s.  nnler  :ävat:
•  g.  zavah-  n.  'Kraft,  Stärke':  äaiva  . . spSniStä  mainya  maida  vanhuyü  'vS  iida (Sp.  3210.)  Y..??.ia.
```


## [2026-09-06T02:27:15.580Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"xwadāy\\b\" PHD_mackenzie.txt | head -10\necho \"---\"; grep -n \"xwadāy \\[\\|xwadāy(īh)\\|MRA\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== PHD gōwišn/guftan main ===\"; grep -n \"gōwēd\\|gōw- \\[\\|guftan \\[\" PHD.txt PHD_mackenzie.txt | head -5"
}
```


### [2026-09-06T02:27:15.705Z] TOOL RESULT

```
---
PHD.txt:601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD_mackenzie.txt:5083:ustar [GMRA < A gmZ>; 'wltll N uftur] camel.
PHD_mackenzie.txt:5540:xar [HMRA < A lJ,mr); hll N.......,] donkey, ass.
=== PHD gōwišn/guftan main ===
```


## [2026-09-06T02:27:21.596Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"xwad[āa]y[^]]\\{0,80\\}\" PHD.txt | head -8\necho \"---mackenzie---\"; grep -o \"xwad[āa]y[^]]\\{0,80\\}\" PHD_mackenzie.txt | head -8\necho \"--- gowisn ---\"; grep -o \"g[oō]wišn[^]]\\{0,60\\}\\|guftan, g[oō]w[^]]\\{0,60\\}\" PHD.txt PHD_mackenzie.txt | head -6"
}
```


### [2026-09-06T02:27:23.448Z] TOOL RESULT

```
xwadāy ... delete eternal. dast-gir [dstgyl | N x
xwaday ... read N xuday.
xwaday [-hwt’y
xwaday [-hwty | P gdyxwd?y, N kadxudā
xwaday [-Awt^y
xwaday [лору | M xwd'y, N ~
xwadāy, kāmgār.
xwadāy.
---mackenzie---
xwaday [-hwt)y I P qdyxwd)y, N kadxudii
xwaday [hwt>y I M xwd'y, N .......
xwaday, kamgar.               ebgat, petyiirag.
xwaday.
xwaday, hameig,                    experienced kiiragah, nibardag.
xwaday.
xwaday; '" of   manager kiirframan.
xwadayih.                       Ma7lichaean zandik.
--- gowisn ---
```


## [2026-09-06T02:27:36.213Z] TOOL CALL #72: Bash

```json
{
 "command": "ls site/pages/195.jpg 2>/dev/null; pdftoppm -f 195 -l 195 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg195 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg195.png"
}
```


### [2026-09-06T02:27:38.797Z] TOOL RESULT

```
site/pages/195.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 75938 Sep  5 22:27 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg195.png
```


## [2026-09-06T02:27:40.933Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg195.png"
}
```


### [2026-09-06T02:27:41.321Z] TOOL RESULT

```

```


## [2026-09-06T02:27:41.318Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T02:28:04.678Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/good",
 "prompt": "Give the etymology of the adjective \"good\": Old English god, Proto-Germanic *godaz, and the PIE root it is traced to (ghedh- 'to unite, join, fit'). Is it related to \"God\"?"
}
```


## [2026-09-06T02:28:07.320Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D9%81",
 "prompt": "Give the Arabic root غ ر ف: the verb غَرَفَ (ḡarafa) and its meaning, and any derived nouns such as غَرَّاف (ḡarrāf), غُرْفَة, and the form VIII اِغْتَرَفَ (iḡtarafa). What does each mean?"
}
```


### [2026-09-06T02:28:10.572Z] TOOL RESULT

```
# Etymology of "Good"

**Old English Origin:**
The adjective "good" comes from Old English *gōd*, derived from Proto-Germanic *\*gōda-*, meaning "fitting, suitable."

**Proto-Germanic and PIE Root:**
The word traces back to the Indo-European root *\*ghedh-*, which means "to unite, be associated, suitable." This root also appears in Sanskrit *gadh-* ("seize"), Old Church Slavonic *godu* ("favorable time"), and Lithuanian *goda* ("honor").

**Relationship to "God":**
The etymology page indicates that "good" and "God" have **different origins**. While both come from Proto-Germanic roots, the entry for "god" notes it derives from Proto-Germanic *\*guthan*, which has "uncertain origin"—distinctly separate from the *\*gōda-* root of "good." Though they share Germanic linguistic heritage, they are not etymologically related despite their phonetic similarity in modern English.
```


### [2026-09-06T02:28:13.437Z] TOOL RESULT

```
# Arabic Root غ ر ف (Ḡ R F)

Based on the Wiktionary entry, here's what's documented:

## Verb Form I
**غَرَفَ (ḡarafa)** means **"to lade out, to scoop."** The entry provides extensive conjugation tables for active and passive voices across various tenses and persons.

## Derived Nouns
The entry shows two noun forms from this root:

1. **غَرْف (ḡarf)** - Listed as the "verbal noun of غَرَفَ" (the gerund/infinitive form)

2. **غُرَف (ḡuraf)** - Identified as "plural of غُرْفَة (ḡurfa)" (rooms/chambers)

## Note on Other Forms
The webpage does not provide information about **غَرَّاف (ḡarrāf)** or the Form VIII verb **اِغْتَرَفَ (iḡtarafa)**. Only the Form I verb and its basic derivatives are documented in this dictionary entry. To find those related forms, you'd need to consult additional Arabic lexical resources.
```


## [2026-09-06T02:28:21.732Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/carafe\" \\\n \"https://www.etymonline.com/word/good-bye\" \\\n \"https://www.etymonline.com/word/good\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%BE\" \\\n \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D9%81\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gud%C4%85\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 195: roots Gh.r.f (carafe) and Ghu 1 (God/xoda/goftan)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T02:28:26.318Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9e6b847831eb3d55.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/21529a15a77b4a1f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab985ace6dc76799.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a2b71d06c5962d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8453aab80c6e0de9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5489c0b5dc2b3564.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74ad421639582390.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9b9b92d799a00f6a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bc421e117bbda2b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dd5054786100887.txt
```


## [2026-09-06T02:28:34.030Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT carafe ===\"; sed -n '23861p' SKT.txt | cut -c1-400\necho \"=== SYN god ===\"; grep -n \"guþ\\|Goth. gup\\|gudam\\|hu-tá\\|ghu-to\" SYN.txt | head -6\necho \"=== IEC ghuto ===\"; grep -n \"ghutos\\|ghu-to\\|ĝhutos\" IEC.txt | head -6\necho \"=== FSD carafe ===\"; grep -n -i \"carafe\" FSD_vol1.txt | head -3 | cut -c1-300"
}
```


### [2026-09-06T02:28:34.148Z] TOOL RESULT

```
=== SKT carafe ===
ITyexpWned  u  being  'of  wonted/  I      Carafe, a gUnwiter-bottle.     (F.  — Spi
=== SYN god ===
=== IEC ghuto ===
=== FSD carafe ===
60551:-carafe
```


## [2026-09-06T02:28:37.658Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23861,23864p' SKT.txt | cut -c1-600\necho \"=== SYN 22.12 god ===\"; grep -n \"22\\. 12\\|22\\.12\\|'GOD'\\|Goth\\. gu\" SYN.txt | head -8\necho \"=== IEC hu- ===\"; grep -n \"ghau-\\|ghau\\b\" IEC.txt | head -5"
}
```


### [2026-09-06T02:28:37.752Z] TOOL RESULT

```
ITyexpWned  u  being  'of  wonted/  I      Carafe, a gUnwiter-bottle.     (F.  — Spi
|ppo«c  it  was  orig.  of  coftisc  silk.*F. }4orte^  *  the  coursest  part  of  silke,  whereof Bare  is  made  ; '  Cot.  Span,  cadarzo,  coane, paoglcd  ailk,  that  cannot  b<r  spun  on  a Poft.  eedarco,  a  coarse  silk.     Origin
lown ;  pro&aoiy  Eastern.  Der.  caiiUij- pnpf ,  from  tbe  cnddis-Uke  shape  of  the  case [ibc  Urra.
badl,ajndge.  (Arab.)  At9h.  qMi,gds{, cadi  or  cari,  a  judge.  Hence  Span,  ai- \idt^  the  jttdge;  wbere  ai  is  the  Axab. rt".  article.
=== SYN 22.12 god ===
2265:1. Lat. homé (> It. womo, Fr. homme, etc.), OLat. hemo, Osc. humuns ‘homi- nes’; Ir. duine, W. dyn, Br. den; OLith. zmuo, OPruss. smoy, Lith. Zmogus, pl. zmonés; Goth. guma (but translates dynp), ON gumi, OE guma, OHG gomo (old Gme. word, now surviving only in cepds., as NHG brdutigam, NE bride- groom fr. OE brydguma) ; Toch. B sawmo, pl. Samna : Lat. humus, Grk. x8év, Lith. zemé, etc. ‘earth’ (1.21). Cf. Hom. emtxBovioc avOpwrot, in contrast to emoupavio. Geol, and even ‘mxGdvior alone (Il. 24.220). Walde-P. 1.663. Ernout-M. 457f. Walde-H. 1.654 f. Pedersen 1.89. Vendryes, RC 40.487 ff.
2337:Grk. aponv, appnv CN NG apoevixds OnduKébs Lat. mds (masculus, masculinus) fémina It. maschio Semmina Fr. mile Semelle Sp. macho hembra Rum. bdrbdtesc Semetesc Tr. Ser-, firend ban- NIr. fireann baineann W. guryw benyw Br. gwaz maouez Goth. gumeins, gumakunds gineins ON karl- (karlligr) kvenn- Dan. mandlig kvindelig Sw. manlig kvinlig OE wéepned, wepman wif, wifman ME male female NE male female Du. mannelijle vrouwelijk OHG gomman wib MHG man wip NHG ménnlich weiblich Lith. vyriskas moteriskas Lett. virisks sieveskigs, sievielisks ChSl. maqziskit Zeniskit SCr. mu3ki Zenskt Boh. muzky zensky Pol. meski zenski Russ. muzkoj, muzeskij zenskij Skt. vrsan-, pums-, nara- stri-
4528:some unexplained phonetic features and taken as an Illyr. loanword by Kretsch- mer, Glotta 22.120); Lat. equus (with fem. equa ‘mare’); Ir. ech, Gall. *epo- in names Eporedia, etc. (W. ebol, Br. ebeul ‘colt?); ON jor (poet.), OK eoh ‘war- horse’ (Goth. aihwa-tundi ‘bramble bush’, lit. ‘horse-tooth’); Lith. (obs.) esva, asva ‘mare’; Skt. agva-, Av., OPers.
15392:Grk. aoe Goth. gulp Lith. auksas NG re Xpvoadt, ON gull Lett. zelts
15395:Goth. gulb, OE gold, etc., general Gmc.; Lett. zelts, ChSI. zlato, etc., gen- eral Slavic; Skt. hiranya-, Av. zaranya-, OPers. daranya- (Dar. Sus. f. 35), all neuters.
=== IEC hu- ===
4556:ghaiios (ghaios) (?) *vigorous, lively, solid, firm. (The evidence is ambig.,, cf. WP I, 528 & 670). Cf. guoiio Gk. khaios ‘staunch, genuine’ (but a-gaios is *elegant); Br. gaé, adj. (gay. LW in Fr. gai); OCz. hojiti sé, v. *multiply', cf. Cz. hojný 'abundant'; Li. gajüs ‘sprightly’. (LG gau ‘dashing, gay’ is from a type *ghau-, cf. Norw. göy ‘fun’. Li. gaivüs ‘lively’ repre- sents *guoiu- apparently, but is entirely ambig. Gaulish gaeso- fstalwart may equate w. Br. gaé ‘gay’) |
4604:ghau$os ‘cuckoo; fool, simpleton’. See next, and cf. ghaughor- Ir. guag ‘folly; foo; OHG gouh ‘cuckoo’; G Gauch ‘cuckoo; simpleton; tree-bug'; OE gēac ‘cuckoo’; ON goukr; (LW in Scots gowk ‘cuckoo; Tool" fr. ON); (ambig.) Latv. gauZu, gauzt ‘twaddle’; cf. also MHG goukeln ‘play tricks? beside gougeln (see next)
4856:ghouió (1) “shout, rave’. Cf. ghau- Gk. khóomai ‘rave, be angry’; G dial. gauwen (shout'. FH); Fris. geije, id.; ON geyja ‘hurl abuse; bark
5952:(8hauo, ið ‘bark’. A possible variant of type ghau-, q. v. Cf. WP I, 565)
```


## [2026-09-06T02:28:44.694Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"invoked being\\|‘the invoked\\|hu-tá-\\|hutá-\" SYN.txt IEC.txt | head -5\ngrep -n \"22\\.12\" SYN.txt | head -3\ngrep -n -i \"^22\\. *12\\|GOD$\" SYN.txt | head -5"
}
```


### [2026-09-06T02:28:46.343Z] TOOL RESULT

```
4528:some unexplained phonetic features and taken as an Illyr. loanword by Kretsch- mer, Glotta 22.120); Lat. equus (with fem. equa ‘mare’); Ir. ech, Gall. *epo- in names Eporedia, etc. (W. ebol, Br. ebeul ‘colt?); ON jor (poet.), OK eoh ‘war- horse’ (Goth. aihwa-tundi ‘bramble bush’, lit. ‘horse-tooth’); Lith. (obs.) esva, asva ‘mare’; Skt. agva-, Av., OPers.
14954:ORE ) Lith. grezli (skverbtt) ; Lett. urbt : CHS Fane SCr. buSitt, urtjelt Boh.  »rtatt . Pol.  swidrowaé, wierci¢ Russ. buravit', sverlit! Skt.  vidh-, gnath- Av. God
```


## [2026-09-06T02:28:49.146Z] TOOL CALL #80: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T02:28:49.197Z] TOOL RESULT

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


## [2026-09-06T02:29:45.396Z] AGENT

Now let me write the verification file.


## [2026-09-06T02:37:51.638Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-195.json <<'JSONEOF'\n{\n  \"pdf_page\": 195,\n  \"book_page\": 165,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Gh.r.f\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Arabic root غ-ر-ف, verb غَرَفَ (ḡarafa) 'to scoop, lade out (water)'\",\n      \"note\": \"The root box is right on all three counts: غ-ر-ف is a real Arabic triliteral root, the language label is correct, and the gloss 'to draw water' is exactly what the verb غَرَفَ means (Wiktionary: 'to lade out, to scoop'; from it غُرْفَة 'handful of water; chamber', غَرْف verbal noun). The whole of entry 0 is in fact a transcription of one entry in Klein: 'carafe, n., a glass bottle. — F., fr. Sp. garrafa, fr. Arab. gharraf, drinking jug, fr. gharafa, he drew water' — the root gloss, the gloss of node #1 and the gloss of node #5 are Klein's own words. Two caveats that belong at root level rather than to any single box. (1) The Arabic noun behind the Romance words is the FEMININE غَرَّافة garrāfa, not the masculine غرّاف; Lokotsch no. 689 states it is 'nicht klassisch-arabisch, sondern scheint nur vulgär im Magrib gebräuchlich zu sein', i.e. a Maghrebi colloquial formation, which is why it travelled through Spanish/Italian and not through the classical language. (2) The Arabic etymon is not the only candidate: Etymonline and Littré (after Mohl) offer Persian قرابه qarāba 'large glass flagon' instead, and Pihan prefers exactly that. Nourai gives only the Arabic side, which is Klein's, Dozy's and Lokotsch's line, so the chart follows the majority view but suppresses a live alternative.\",\n      \"note_fa\": \"ریشهٔ سه‌حرفی عربی «غ ر ف» و فعل غَرَفَ به معنای «آب برداشتن، آب کشیدن با کف دست» واقعی است و برچسب زبانی و معنای نورایی هر دو درست‌اند. تمام این نمودار در واقع بازنویسی یک مدخل از فرهنگ ریشه‌شناسی کلاین (ذیل carafe) است. دو نکته: نخست آنکه واژه‌ای که به زبان‌های اروپایی رفته صورت مؤنث «غرّافه» است و لوکوچ (شمارهٔ ۶۸۹) تصریح می‌کند که این اسم عربی فصیح نیست و ظاهراً فقط در گویش عامیانهٔ مغرب به کار می‌رفته است؛ دوم آنکه ریشهٔ عربی تنها گزینه نیست و اتیمانلاین و پیهان و لیتره واژهٔ فرانسوی را از «قرابه»ی فارسی می‌گیرند. پس ادعای نورایی دربارهٔ خودِ ریشه درست است، اما وجه دیگر را نیاورده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D9%81\",\n        \"https://www.etymonline.com/word/carafe\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:237\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. carafe (local KLN_1966.txt line 6490): 'carafe, n., a glass bottle. — F., fr. Sp. garrafa, fr. Arab. gharraf, drinking jug, fr. gharafa, he drew water.' This one entry supplies the root gloss and every box of entry 0. Page: in the two-pages-per-leaf 1966 scan the entry sits on leaf 136, i.e. printed p. ~248 (leaf 130 = the calo-/calori- page ~p.236), so Nourai's '237' is about eleven pages early for this printing; the wording is nevertheless unmistakably Klein's.\"},\n        {\"ref\": \"SAP:1152\", \"status\": \"not_checked\", \"note\": \"SAP = Ahmad Sayyah, Farhang-e Sayyah (Persian translation of al-Munjid), 3 vols; refs_online.json records it as purchase-only (fidibo), no copy on disk or on any permitted platform, so p. 1152 could not be opened.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"LKT\", \"where\": \"no. 689 (LKT.txt line 1699)\", \"stance\": \"supports\", \"note\": \"'Ar. garrāfa: Weitbauchige Flasche [vom Vb. garafa schöpfen; das Subst. ist nicht klassisch-ar., sondern scheint nur vulgär im Magrib ... gebräuchlich zu sein]; hieraus sp. pg. garrafa, frz. caraffe, carafe, it. caraffa ... dtsch. Karaffe' — same derivation as Nourai, with the important rider that the Arabic noun is Maghrebi colloquial and feminine.\"},\n        {\"src\": \"DEV\", \"where\": \"s.v. Carafe (DEV.txt line 963)\", \"stance\": \"supports\", \"note\": \"'Esp. et portug. garrafa, ital. caraffa, viennent certainement de la racine arabe غرف gharaf qui signifie puiser, dit M. Dozy (Gloss. p. 274)' — Dozy's derivation from the root غرف, exactly Nourai's root box; Devic adds Mohl's rival Persian قرابه qarâbah.\"},\n        {\"src\": \"PHN\", \"where\": \"s.v. CARAFE (PHN.txt lines 3202-3207), printed p. 97\", \"stance\": \"partial\", \"note\": \"Pihan heads the entry 'CARAFE, s. f. (a. ou p.)' — Arabic OR Persian — and then writes 'Peut-etre carafe vient-il plutot du persan قرابه [qarâbeh]', i.e. he prefers the Persian etymon over the Arabic root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"gharrâf\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"غَرَّاف ḡarrāf is the fa''āl intensive/instrument pattern built on the root غ-ر-ف, so 'the (thing) that scoops much' > 'drinking jug' is a normal Arabic formation and Klein prints exactly this form and gloss. The reservation is one of form and register: the word that actually underlies the European words is the feminine غَرَّافة ḡarrāfa, which is what Lokotsch (no. 689), Dozy and Devic cite, and Lokotsch adds that it is not Classical Arabic at all but a Maghrebi colloquial noun — which explains why it entered Europe through Iberian/Italian trade rather than through the learned Arabic vocabulary. Standard Arabic lexica give غُرْفَة ḡurfa 'a handful/scoop of water' and the Form VIII اِغْتَرَفَ, but no classical غرّاف, so Nourai's box reproduces Klein faithfully while the better-attested etymon is garrāfa.\",\n          \"derivation_fa\": \"«غرّاف» بر وزن فَعّال از ریشهٔ غ ر ف ساخته شده و ساختِ صرفیِ آن در عربی کاملاً قاعده‌مند است: «بسیارآب‌برگیرنده» و از آنجا «کوزهٔ آب». اما آنچه به زبان‌های اروپایی راه یافته صورت مؤنث «غرّافه» است، همان‌گونه که لوکوچ و دزی و دویک آورده‌اند، و لوکوچ می‌افزاید که این اسم در عربی فصیح نیست و گویا تنها در عربی عامیانهٔ مغرب رواج داشته است؛ به همین سبب هم از راه بازرگانی اندلس و ایتالیا به اروپا رفته نه از راه واژگان فصیح. پس ادعای نورایی (که برگرفته از کلاین است) با احتیاط پذیرفتنی است و صورت درست‌تر «غرّافه» است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D9%81\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:237\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6490: '... fr. Arab. gharraf, drinking jug, fr. gharafa, he drew water' — Nourai's transliteration and gloss are Klein's verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 689\", \"stance\": \"partial\", \"note\": \"gives the etymon as 'Ar. garrāfa' (feminine) and marks it non-classical, vulgar Maghrebi — same root, slightly different form and register from Nourai's gharrâf.\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Carafe\", \"stance\": \"partial\", \"note\": \"Devic works from 'la racine arabe غرف gharaf ... puiser' via Dozy and cites Spanish/Portuguese garrafa, not a masculine gharrāf.\"},\n            {\"src\": \"AFM\", \"where\": \"grep 'غراف' and 'غرف' in AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words arabised has no entry for this word, which is consistent with it being an Arabic formation rather than a Persian loan.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"eğterâf\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"اغتراف eḡterāf is the maṣdar of the Arabic Form VIII verb اِغْتَرَفَ iḡtarafa 'to scoop up (water) for oneself', built with the infix -t- directly on the root غ-ر-ف; it entered Persian as an Arabic loanword of the learned register. Mo'in's Farhang (the very reference Nourai cites) has 'اغتراف: [ع.] (مص م.) آب به مشت برگرفتن، با کف دست آب نوشیدن' — Arabic-marked, and glossed exactly as Nourai's 'to draw water by hands'. What is not right is the arrow: اغتراف is not derived FROM غرّاف. Arabic morphology is root-and-pattern, so غرّاف (fa''āl) and اِغْتَرَفَ (Form VIII) are sister formations from the same consonantal root, and the chart should have hung eḡterāf directly on the root box, as it does the Spanish branch's ancestor.\",\n          \"derivation_fa\": \"«اغتراف» مصدر باب افتعال از ریشهٔ عربی غ ر ف است (اِغْتَرَفَ: آب به کف برگرفتن) و به عنوان وام‌واژهٔ عربیِ ادبی وارد فارسی شده است. معین در فرهنگ فارسی — همان مأخذی که نورایی آورده — می‌نویسد: «اغتراف: [ع.] (مص م.) آب به مشت برگرفتن، با کف دست آب نوشیدن»، که دقیقاً همان معنای نمودار است. اما جهت پیکان نادرست است: در صرف عربی، «غرّاف» بر وزن فَعّال و «اغتراف» بر وزن افتعال هر دو مستقیماً از ریشه ساخته می‌شوند و یکی از دیگری مشتق نیست؛ پس این خانه می‌بایست به‌جای «غرّاف» به خودِ ریشه وصل می‌شد. ادعای نورایی با این اصلاح پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D9%81\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:308\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi (local MON_part1.txt line 14647): 'اغتراف: [ع.] (مص م.) آب به مشت برگرفتن، با کف دست آب نوشیدن' — Arabic tag and Nourai's gloss. Mo'in's printed page numbers cannot be mapped in the available scan, so p. 308 itself is unverifiable, but the entry is there and says what the chart says.\"},\n            {\"ref\": \"FVA:296\", \"status\": \"not_checked\", \"note\": \"FVA = Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989); refs_online.json records a catalogue entry only (OpenLibrary OL2012991M), no digital copy on archive.org, ketabnak or noorlib.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. اغتراف\", \"stance\": \"supports\", \"note\": \"quoted above; marks the word [ع.] i.e. Arabic loan, not a Persian formation.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'اغتراف' in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry, as expected for a Semitic loan.\"},\n            {\"src\": \"PLA\", \"where\": \"grep 'garraf' / 'gurfa' in PLA_pages.txt (Asbaghi, Persische Lehnwoerter im Arabischen)\", \"stance\": \"silent\", \"note\": \"no entry — Asbaghi lists Persian words borrowed INTO Arabic, and this word runs the other way, so his silence is the expected result.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Spanish\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box stands for Spanish garrafa 'carafe, decanter' (also Portuguese garrafa), the Iberian reflex of Maghrebi Arabic ḡarrāfa taken over during or just after the Andalusi period; Arabic ḡ- is regularly rendered by Ibero-Romance g-, and the Arabic geminate -rr- is kept. Klein routes the French word through this Spanish form, and Lokotsch and Devic list sp. pg. garrafa in the same position.\",\n          \"derivation_fa\": \"این خانهٔ بی‌واژه نمایندهٔ اسپانیایی garrafa (و پرتغالی garrafa) به معنای «تنگ، صراحی» است که در دورهٔ اندلس یا اندکی پس از آن از عربیِ مغربی «غرّافه» وام گرفته شده؛ «غ» عربی در زبان‌های ایبریایی به g بدل می‌شود و «رّ» مشدد نیز حفظ شده است. کلاین، لوکوچ و دویک همگی همین صورت اسپانیایی را در همین جایگاه می‌آورند، پس ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carafe\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:201\", \"status\": \"not_checked\", \"note\": \"AHD:201 is a page of the main American Heritage Dictionary (New College Edition, 1975/76), not of the Indo-European appendix; only Watkins's appendix (AHD_watkins1985.txt) is on disk, and the New College scans on archive.org are lending-only. The Spanish garrafa link is however covered by KLN and LKT.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 689\", \"stance\": \"supports\", \"note\": \"'hieraus sp. pg. garrafa, frz. caraffe, carafe, it. caraffa' — Spanish garrafa taken straight from Arabic garrāfa.\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Carafe; index 'Garrafa, hisp. voy. Carafe' (DEV.txt line 3526)\", \"stance\": \"supports\", \"note\": \"Devic files Spanish garrafa under carafe as the Iberian intermediary.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. carafe\", \"stance\": \"supports\", \"note\": \"'F., fr. Sp. garrafa' — the Spanish stage is Klein's own.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The empty box stands for French carafe (17th c.), the immediate source of the English word. Klein and Lokotsch route it from Spanish garrafa, as the chart does; but Etymonline and most modern accounts derive French carafe from Italian caraffa (Naples/Sicily, siz. carrabba) rather than from Spanish, since the vessel and its name reached France through Italy. Both Romance forms go back to the same Maghrebi Arabic ḡarrāfa, so the difference is only which Romance language handed the word on; Spanish garrafa would in any case be expected to give French *garrafe, whereas the initial c- of carafe matches Italian caraffa.\",\n          \"derivation_fa\": \"این خانه نمایندهٔ فرانسوی carafe (سدهٔ هفدهم) است که واژهٔ انگلیسی از آن گرفته شده. کلاین و لوکوچ آن را از اسپانیاییِ garrafa می‌گیرند، همان‌گونه که نمودار نشان می‌دهد؛ اما اتیمانلاین و بیشتر پژوهش‌های امروزی آن را از ایتالیاییِ caraffa (و صورت سیسیلی carrabba) می‌دانند، چون این ظرف و نامش از راه ایتالیا به فرانسه رسیده است. هر دو صورت رومی سرانجام به «غرّافه»ی عربیِ مغربی می‌رسند، پس اختلاف تنها بر سر واسطه است. نکتهٔ آوایی به سود ایتالیایی است: از garrafa اسپانیایی در فرانسوی *garrafe انتظار می‌رفت، حال آنکه «ک» آغازیِ carafe با caraffa ایتالیایی می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carafe\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:201\", \"status\": \"not_checked\", \"note\": \"same as node #3: the cited page belongs to the main AHD dictionary text, which is not open online; only the Watkins IE appendix is on disk.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"s.v. CARAFE, printed p. 97 (PHN.txt line 3202 ff.)\", \"stance\": \"partial\", \"note\": \"Pihan marks the word '(a. ou p.)' and inclines to Persian قرابه qarâbeh rather than to the Arabic root, so he neither confirms nor uses the Spanish stage.\"},\n            {\"src\": \"DEV\", \"where\": \"s.v. Carafe\", \"stance\": \"partial\", \"note\": \"gives 'Esp. et portug. garrafa, ital. caraffa' side by side without deciding which fed French, and reports Mohl's Persian qarâbah as a rival.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 689\", \"stance\": \"supports\", \"note\": \"lists 'sp. pg. garrafa, frz. caraffe, carafe, it. caraffa' in one series from Arabic garrāfa, i.e. Nourai's chain.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"carafe\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English carafe 'glass water-bottle, decanter' is a straight 18th-century borrowing of French carafe (first recorded in English 1786), unchanged in form and meaning; the gloss 'a glass bottle' is Klein's own wording. Skeat likewise files it as 'Carafe, a glass water-bottle. (F. — Sp. ...)'. Only the far end of the chain (Arabic ḡarrāfa vs Persian qarāba, Spanish vs Italian mediation) is contested; the French-to-English step is not.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی carafe به معنای «تنگ شیشه‌ای» وام‌گیریِ مستقیم از فرانسوی carafe در سدهٔ هجدهم است (نخستین کاربرد ثبت‌شده ۱۷۸۶) و در صورت و معنا تغییری نکرده است؛ معنای «a glass bottle» عیناً از کلاین گرفته شده و اسکیت هم آن را «تنگ آبِ شیشه‌ای، از فرانسوی» می‌داند. تنها سرِ دیگرِ زنجیره (عربی «غرّافه» در برابر فارسی «قرابه»، و واسطهٔ اسپانیایی در برابر ایتالیایی) محل بحث است و این گام فرانسوی‌به‌انگلیسی بی‌چون‌وچرا درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/carafe\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:237\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6490 s.v. carafe: 'a glass bottle. — F., fr. Sp. garrafa ...' — Nourai's gloss is Klein's. (Page in the 1966 scan is ~248, see the root-level ref_check.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 23861\", \"stance\": \"supports\", \"note\": \"Skeat: 'Carafe, a glass water-bottle. (F. — Sp...)' — same definition and same French-from-Spanish route.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 689\", \"stance\": \"supports\", \"note\": \"lists 'engl. caraffe' among the European reflexes of Arabic garrāfa, alongside dtsch. Karaffe, ndl. karaf, russ. grafin.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 60551 (headword '-carafe')\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls has the headword but the OCR of the etymology bracket is unreadable, so nothing can be quoted from it.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ghu 1, Ghau, Gheue, Gheu 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ǵʰewH- 'to call (on), invoke' (Pokorny 413-414 ĝhau-, ĝhau̯ə-; Watkins/AHD gheu(e)-)\",\n      \"note\": \"The root box is correct and its four alternant spellings are simply the citation forms of the two standard handbooks: Pokorny's lemma reads 'Root/lemma: ghau-, ghaua-, Meaning: to call ... Page(s): 413-414', and Watkins in the AHD appendix has 'gheu(e)-. To call, invoke. ... [Pok. ghau- 413.]'. So 'Ghu 1 / Ghau / Gheue / Gheu 2 : to call for help, appeal' with POK:413 reproduces both. Wiktionary reconstructs it as *ǵʰewH- 'to call on, invoke', with Sanskrit हवते hávate and Avestan zauuaiti as the Indo-Iranian reflexes — a palatal *ǵʰ, which matters below. The chart's real problem is not the root but the fact that it hangs TWO branches on it that cannot both belong there. The left branch (*ǵʰu-tó- > Gmc *gudam > God; Av. zav-) is textbook. The right branch (Gheu-bh > Old Persian gaub- > Pahlavi guftan > Persian goftan/gap) cannot be: PIE palatal *ǵʰ gives Indo-Iranian h/z (Skt. hávate, Av. zav-), so an Iranian verb beginning in g- cannot descend from *ǵʰewH-, and Cheung 2007 s.v. *gaub leaves the PIE and LIV/Pokorny fields empty with the flat verdict 'No IE etymology'. Kent p. 182, which Nourai cites, says only 'perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gausa-' — that is the sound/hearing root behind gausa- 'ear', not the invoking root of p. 413. Separately, the Iranian left branch is wrong at its own second step: Pahlavi xwadāy and its Persian descendants do not come from Av. zav- at all (see nodes #3 and #4), as Hübschmann p. 54 and Mo'in's own footnote on the Borhan page Nourai cites both state, and as Nourai half-concedes in his note 'See root Aiw for a different derivation'.\",\n      \"note_fa\": \"خودِ ریشه درست است و چهار صورتِ نوشتاری آن چیزی جز صورت‌های استنادیِ دو فرهنگ معیار نیست: پوکورنی در صفحات ۴۱۳–۴۱۴ مادهٔ ghau-, ghaua- «خواندن، فراخواندن» را آورده و واتکینز در پیوستِ فرهنگ American Heritage می‌نویسد «gheu(e)-. To call, invoke. [Pok. ghau- 413]». ویکی‌واژه آن را *ǵʰewH- «خواندن، نیایش کردن» بازسازی می‌کند با بازتاب‌های سنسکریت hávate و اوستایی zauuaiti. اما نمودار دو شاخه را به یک ریشه بسته که هر دو نمی‌توانند از آنِ آن باشند: *ǵʰ کامی در هندوایرانی به h/z بدل می‌شود، پس فعلی ایرانی که با g آغاز می‌شود نمی‌تواند از این ریشه باشد؛ چونگ (۲۰۰۷) ذیل *gaub می‌نویسد «هیچ ریشه‌شناسی هندواروپایی ندارد» و خانه‌های LIV و پوکورنی را خالی می‌گذارد، و کنت هم فقط با «شاید» از گسترشِ -bh سخن گفته و آن هم از ریشهٔ *gheu- ی «آوا/شنیدن» (همان که در gauša- «گوش» است) نه از ریشهٔ ۴۱۳. افزون بر این، شاخهٔ چپ در گام دوم خود خطاست: «خواتای» پهلوی و فرزندان فارسی‌اش هیچ پیوندی با zav- اوستایی ندارند؛ هوبشمان در ص ۵۴ و حاشیهٔ معین بر همان صفحهٔ برهان قاطع که نورایی ارجاع داده، هر دو این را می‌گویند و خودِ نورایی هم با یادداشت «رک ریشهٔ Aiw» نیمه‌اعتراف کرده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:413\", \"status\": \"supports\", \"note\": \"Pokorny's own entry (local POK_full.txt lines 36023-36076): 'Root / lemma: ghau- ghaua- ... Meaning: to call ... Avestan zavaiti calls, shouts ... Here probably (as *ghu-to-m angerufenes creature): Germanic *guda- god ... References: WP. I 529 f. Page(s): 413-414.' Both branches Nourai draws on the left side of the chart are literally in Pokorny at the cited page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix, AHD_watkins1985.txt line 526\", \"stance\": \"supports\", \"note\": \"'gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, the invoked, god, in Germanic *gudam, god, in: a. Old English god, god: GOD ... [Pok. ghau- 413.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I p. 529 (WLD_Bd1_pages.txt leaf 538, running head 'gau- — ghaua- 529')\", \"stance\": \"supports\", \"note\": \"'ghaua-, daneben ghau- rufen, anrufen. Ai. havate ruft, ruft an ... av. zavaiti ruft, ruft an, verruft, verwuenscht (daneben die Praesentia zbayeiti, zaozaomi)' — the source Pokorny abbreviates as WP. I 529.\"},\n        {\"src\": \"IEC\", \"where\": \"grep 'ghau-', 'ghuto' in IEC.txt\", \"stance\": \"silent\", \"note\": \"Mann's comparative dictionary has ghauos/ghausos/ghouio entries of quite different meaning ('vigorous', 'cuckoo', 'shout, rave') but no *ghu-to- 'god' lemma; nothing usable either way.\"},\n        {\"src\": \"SYN\", \"where\": \"grep 'guth', 'gudam', 'invoked being' in SYN.txt\", \"stance\": \"silent\", \"note\": \"Buck's chapter 22.12 'god' is not recoverable from this OCR (the Gothic and Germanic forms in that section come out garbled), so no quotation can be taken.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Ghu-to\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"*ǵʰu-tó- is the regular zero-grade verbal adjective (the -to- participle) of *ǵʰewH-, hence literally 'the (one) invoked, the called-upon' — Pokorny writes it 'as *ghu-to-m angerufenes Wesen' and Watkins 'Suffixed zero-grade form *ghu-to-, the invoked, god'. The Indo-Aryan witness for the same participle is Vedic hu-tá- 'invoked', an epithet of Indra (Klein cites it under god), so the formation is not an ad hoc reconstruction. Nourai's gloss 'God, one who is called upon for help' is Watkins's gloss expanded. The only reservation worth recording is that Wiktionary notes the laryngeal in *ǵʰewH- ought to give a long vowel (*ǵʰuH-tó- > *gūda-), which is one of the reasons the Germanic word is still argued about (see node #5); the reconstruction itself, as the -to- adjective of this root, is standard.\",\n          \"derivation_fa\": \"*ǵʰu-tó- صفتِ فعلیِ درجهٔ صفر (اسم مفعولِ ساخته‌شده با پسوند -to-) از ریشهٔ *ǵʰewH- است، یعنی «خوانده‌شده، آنکه او را می‌خوانند». پوکورنی خود می‌نویسد «*ghu-to-m یعنی موجودِ فراخوانده‌شده» و واتکینز «صورت درجه‌صفرِ پسونددار *ghu-to-، خوانده‌شده، خدا». گواهِ هندوآریاییِ همین ساخت، hu-tá- در وداهاست که صفتِ ایندره است، پس این بازسازی ساختگی نیست و معنایی که نورایی داده همان معنای واتکینز است. تنها نکتهٔ باقی‌مانده آن است که به‌سبب حنجرهٔ ریشه انتظار می‌رفت واکهٔ کشیده پدید آید (*ǵʰuH-tó-)، و همین یکی از دلایل ادامهٔ بحث دربارهٔ واژهٔ ژرمنی است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gud%C4%85\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 526: 'Suffixed zero-grade form *ghu-to-, the invoked, god, in Germanic *gudam' — Nourai's box word for word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 413-414\", \"stance\": \"supports\", \"note\": \"'Here probably (as *ghu-to-m angerufenes creature): Germanic *guda- n. god (compare Old Indic hu-ta- loud call, ved. epithet of Indras)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. God; god (KLN_1966.txt line 16388, printed p. ~696)\", \"stance\": \"supports\", \"note\": \"'for Teut. *guda-, which is prob. a participial formation ... meaning the invoked being, and corresponds to I.-E. ghu-to-m, fr. base *ghu-, to invoke, whence OI. hu-ta-, invoked (epithet of Indra), pp. of havate, invokes'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 529\", \"stance\": \"supports\", \"note\": \"the same root article, with the Germanic god-word attached to it.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"zavaiti\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan zavaiti is real and belongs to this root: Bartholomae's Altiranisches Woerterbuch has 'j-, g. zav-, zbā- V. rufen' with the senses (1) 'jemanden, etwas rufen, anrufen, aufrufen' and (3) 'verrufen, verwuenschen', comparing Skt. hávate; Pokorny cites 'Avestan zavaiti calls, shouts, curses (besides the presents zbayeiti, zaozaomi)'. Two things in the box are nevertheless off. (a) The gloss: zavaiti is a 3rd sg. present, 'he calls, he invokes' — not 'invoked' and certainly not 'God'; the passive participle of the root is Av. zūta- 'called', and the noun is zavana- 'call, invocation, prayer'. Avestan has no *zavaiti 'god'. (b) The position: the box is drawn under *ǵʰu-tó- 'the invoked one', but a finite present cannot descend from a verbal adjective; zavaiti is a sister of *ǵʰu-tó-, both formed from the root, and it belongs one level up. This matters because the whole Iranian branch of the chart hangs off zavaiti — and, as node #3 shows, it should not hang off zav- at all.\",\n          \"derivation_fa\": \"صورت اوستایی zavaiti واقعی است و به همین ریشه تعلق دارد: بارتولمه در فرهنگ ایرانی باستان مدخل «zav-، zbā- فعل: خواندن» را با معناهای «کسی یا چیزی را خواندن، فراخواندن، نیایش کردن» و نیز «نفرین کردن» آورده و آن را با hávate سنسکریت سنجیده است؛ پوکورنی نیز همین را می‌گوید. اما دو نکته درست نیست: نخست معنا — zavaiti فعل سوم‌شخص مفردِ مضارع است یعنی «می‌خوانَد»، نه «خوانده‌شده» و به‌هیچ‌روی «خدا»؛ اسم مفعولِ این ریشه در اوستایی zūta- و نام‌واژهٔ آن zavana- «خواندن، نیایش» است. دوم جایگاه — این خانه زیر *ǵʰu-tó- «خوانده‌شده» نشانده شده، حال آنکه فعلی صرف‌شده نمی‌تواند از یک صفت فعلی مشتق شود؛ zavaiti و *ǵʰu-tó- هر دو مستقیماً از ریشه ساخته شده‌اند و این خانه باید یک پله بالاتر می‌بود. پس ادعای نورایی با احتیاط و با این دو اصلاح پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-\"],\n          \"ref_check\": [\n            {\"ref\": \"WLD:599\", \"status\": \"not_found\", \"note\": \"Wrong page. In Walde-Pokorny Bd. I the article is on p. 529 (WLD_Bd1_pages.txt leaf 538, running head 'gau- — ghaua- 529': 'av. zavaiti ruft, ruft an, verruft, verwuenscht'), which is also the page Pokorny himself cites ('WP. I 529 f.'). Printed p. 599 of the same volume (leaf 608) carries the root 'ger-, gere-' (Gk. egeiro 'wecke'), nothing to do with invoking — so 599 looks like a digit slip for 529.\"},\n            {\"ref\": \"KLN:413\", \"status\": \"not_found\", \"note\": \"Klein p. 413 is in the cyto- range of the alphabet (KLN_1966.txt leaf 218/219: cytology, cytoplasm), so it cannot be the source of an Avestan form. Klein does cite zavaiti, but s.v. 'God; god' at printed p. ~696 ('which is rel. to Avestic zavaiti, of s.m.'). The number 413 is exactly Pokorny's page for this root, so this looks like a slip for POK:413.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch s.v. zav-, zbā- (BRT.txt line 27735, cols. ~1666-1668)\", \"stance\": \"partial\", \"note\": \"'j-, g. zav-, zbā- V. rufen. Praes. ... 1) Jemanden, etwas (Akk.) rufen, anrufen, aufrufen ... 3) verrufen, verwuenschen ... ai. hávate' — confirms the verb and the root but glosses it as 'to call', never 'God'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 413\", \"stance\": \"partial\", \"note\": \"'Avestan zavaiti calls, shouts, curses (besides the present zbayeiti, zaozaomi), participle zuta- called, zavana- shout, call, appeal, request, plea; prayer' — same correction to the gloss.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheu(e)-\", \"stance\": \"silent\", \"note\": \"Watkins lists no Iranian material under this root at all, only the Germanic god-words.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"xvatây\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Pahlavi word is real — MacKenzie's Concise Pahlavi Dictionary has 'xwadāy [hwt'y | M xwd'y, N ~] lord, master, god' (Book Pahlavi also writes it with the Aramaic ideogram MRA 'lord'), and Nyberg's glossary has the abstract xwatāyēh 'dominion, reign' throughout the Kārnāmag — but its derivation from Avestan zav- 'to invoke' is rejected by every source consulted, including the one Nourai cites. Modern scholarship reconstructs Proto-Iranian *hwa-tāwHā 'self-powerful, self-ruling' > MP xwadāy: *hwa- 'own, self' (Av. xva-, cf. NP خود xod) plus the root *tauH- 'to be able, be powerful' (Av. tav-, MP tuwān), with intervocalic -t- voiced to -d- in Middle Persian and the -āy ending of the nominative stem. Hübschmann, Persische Studien p. 54 — Nourai's own HUB:54 — writes: 'Noeldeke bezweifelt die Richtigkeit von Horn's Etymologie: np. xudāi Gott = zd. *xvadaya- mit vollem Recht, da xudāi = phl. xvatāi ... ein zd. *xvataya- oder auch *xvataia- voraussetzt', comparing Skt. svatas + āyu- 'living of itself'. Nourai's own note 'See root Aiw for a different derivation' points at precisely that svatas+āyu- account, so he knew of the rival and drew both. Nothing in this word has anything to do with calling or invoking.\",\n          \"derivation_fa\": \"واژهٔ پهلوی خودش واقعی است: مکنزی در فرهنگ کوچک پهلوی می‌آورد «xwadāy [hwt'y] سرور، خداوند، خدا» و نیبرگ نیز xwatāyēh «فرمانروایی» را در کارنامه فراوان ثبت کرده است؛ اما اشتقاق آن از zav- اوستایی به معنای «خواندن» را هیچ‌یک از منابع تأیید نمی‌کند، از جمله همان مأخذی که نورایی به آن ارجاع داده. ریشه‌شناسی امروزی چنین است: ایرانی باستان *hwa-tāwHā «خودتوان، خودفرمان» از *hwa- «خود» (اوستایی xva-، فارسی «خود») + ریشهٔ *tauH- «توانستن» (اوستایی tav-، پهلوی tuwān)؛ «ت» میان دو واکه در فارسی میانه به «د» نرم شده و پسوند -āy از ستاک فاعلی مانده است. هوبشمان در ص ۵۴ — همان HUB:54 نورایی — می‌نویسد که نولدکه به‌حق ریشه‌شناسی هرن را رد کرده و xudāi فارسی = xvatāi پهلوی صورت اوستاییِ *xvataya- را می‌طلبد، و آن را با svatas + āyu- سنسکریت («از خود زنده») می‌سنجد. یادداشت خودِ نورایی («رک ریشهٔ Aiw») دقیقاً به همین وجه اشاره دارد. پس پژوهش امروزی ادعای این خانه را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HUB:54\", \"status\": \"contradicts\", \"note\": \"Huebschmann, Persische Studien p. 54 (HUB.txt leaf 64, note to Horn's no. 471): 'Noeldeke bezweifelt die Richtigkeit von Horn's Etymologie: np. xudāi Gott = zd. *xvadaya- mit vollem Recht, da xudāi = phl. xvatāi ... ein zd. *xvataya- oder auch *xvataia- voraussetzt, die sich zur Not durch skr. svatas + āyu- von selbst lebend oder skr. svatas + adi- von selbst anfangend ... deuten liessen', with the footnote 'Arsac. phl. *xvataš, spaeter phl. xvatāi, paz. xvadāi'. Huebschmann derives the word from xva- 'self', never from zav- 'invoke'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. xwadāy (PHD.txt: 'xwaday [hwt'y | M xwd'y, N ~]')\", \"stance\": \"partial\", \"note\": \"confirms the Pahlavi form and its ideogram but gives no etymology; also lists the compounds kadag-xwadāy 'householder', kāmag-xwadāy 'absolute', dagrand-xwadāy 'of long dominion' — all with the sense 'lord, ruler', not 'invoked one'.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. xvatāyēh (NYB_vol2_glossary.txt line 4376)\", \"stance\": \"partial\", \"note\": \"'x-vatāyēh domination, dominion, reign ... KZ/Prth hwtwypy, Gr. v. theo-' — the Parthian and Greek equivalents of the Sasanian inscriptions, i.e. a word of rulership, again with no link to invoking.\"},\n            {\"src\": \"BQT\", \"where\": \"Mo'in's footnote 3 on خدا, vol. 2 leaf 176 (printed p. 718/719)\", \"stance\": \"contradicts\", \"note\": \"'پهلوی متأخر xwatāy ... پازند xwadāy «هوبشمان ۵۴» ... بعضی این کلمه را از اوستایی xva-dāta- (خودآفریده) مشتق دانسته‌اند و نولدکه بحق در این وجه اشتقاق شک کرده، چون خدای فارسی و خواتای پهلوی به کلمهٔ xwatāya- اقرب است و آن هم به سانسکریت svatas + āyu ... رابطه دارد' — Mo'in canvasses xva-dāta- and xva-tāya- and rejects neither in favour of a 'call' root.\"},\n            {\"src\": \"BRT\", \"where\": \"grep 'xvatāy', 'hvatāy' in BRT.txt\", \"stance\": \"silent\", \"note\": \"Bartholomae has no Avestan *xvataya- headword (the form is a reconstruction), so his dictionary neither supports nor refutes directly; his zav- article, by contrast, contains no MP derivative.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"Xodâ; xadieve; xâjeh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three words, three different verdicts, and none of them supports the arrow from Avestan zav-. (1) خدا xodā is the regular New Persian outcome of Middle Persian xwadāy (xwadāy > xudāy > xudā/xodā, with loss of the final -y and the usual reduction of the labialised onset xw- to x- before a back vowel) — the descent is certain, but its ultimate source is Proto-Iranian *hwa-tāwHā 'self-powerful' (Wiktionary, following MacKenzie), not *ǵʰewH- 'invoke'. Horn's Grundriss no. 471 on the very page Nourai cites (p. 104) sets up 'als Grundform ist etwa *xva-dāta- / aw. xvadāta- (oder *xvatāya-) anzusetzen', i.e. 'self-created' or 'self-powerful'. So the gloss 'God (who is called upon for help)' is Nourai's etymological gloss, not a meaning of the word. (2) خدیو xadiv 'lord, ruler, king' (in the modern period 'khedive') is not a Persian development of xwadāy at all: Wiktionary, citing Sims-Williams and Jafari Dehaghi-Sadri on Bactrian loanwords, derives it from Bactrian χοαδηο khoadēo 'lord' (Middle Persian htyw /xadēw/), which is the Bactrian reflex of the same *hwa-tāw- word — a sideways loan, not a vertical descent. Nourai's transliteration 'xadieve' is the printed book's own (checked on the page image); the sources know xadēw/xadīv. (3) خواجه xʷāja 'master' is the weakest link: Wiktionary, following Asatrian (Iran and the Caucasus 2011, 2012), derives it from a Middle Indo-Aryan reflex of Sanskrit उपाध्याय upādhyāya 'teacher, preceptor' (an unattested *vājjhāa, cf. Sindhi واجهو vājho), transmitted through Central Asia — no relation to xwadāy. Mo'in's footnote on Borhān records the older guesses (Purdavud's Av. xva- + -če 'one who has a self of his own', and 'خواتای‌چه from Pahlavi xwatāy + diminutive -če'), so Nourai's arrow reproduces a nineteenth/twentieth-century Iranian view now superseded.\",\n          \"derivation_fa\": \"سه واژه در یک خانه و هر سه با داوری جداگانه، و هیچ‌یک پیکانِ آمده از zav- اوستایی را تأیید نمی‌کند. ۱) «خدا» بازماندهٔ قاعده‌مندِ فارسی میانهٔ xwadāy است (xwadāy > xudāy > خدا، با افتادن «ی» پایانی و سادگیِ خوشهٔ xw-)، اما خاستگاه نهایی آن ایرانی باستانِ *hwa-tāwHā «خودتوان» است نه ریشهٔ «خواندن». هرن در شمارهٔ ۴۷۱ همان صفحهٔ ۱۰۴ که نورایی ارجاع داده، صورت اصلی را *xva-dāta- «خودآفریده» (یا *xvatāya-) می‌نهد. پس معنای «خدایی که او را به یاری می‌خوانند» تفسیر ریشه‌شناختیِ نورایی است نه معنای واژه. ۲) «خدیو» تحولِ فارسیِ خواتای نیست: ویکی‌واژه به پیروی از سیمز-ویلیامز آن را وام‌واژه‌ای از بلخیِ χοαδηο «سرور» می‌داند (فارسی میانه xadēw)، یعنی همان واژهٔ *hwa-tāw- اما از راه وام‌گیری افقی از بلخی، نه توارث عمودی. آوانگاشتِ «xadieve» از خودِ کتاب است (با دیدنِ تصویر صفحه بررسی شد) و صورت شناخته‌شده xadēw/xadīv است. ۳) «خواجه» سست‌ترین حلقه است: ویکی‌واژه به پیروی از آساتریان آن را از بازتابی هندوآریاییِ میانه از upādhyāya سنسکریت («آموزگار، مربی») از راه آسیای میانه می‌داند و پیوندی با «خواتای» نمی‌بیند. حاشیهٔ معین بر برهان قاطع حدس‌های کهن‌تر را ثبت کرده است (پورداود: xva- + -če؛ و دیگران: «خواتای‌چه» از خواتای + یای تصغیر). پس پژوهش امروزی این خانه را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:718\", \"status\": \"contradicts\", \"note\": \"Borhān-e Qāte', vol. 2 leaf 176 = printed p. 718/719 (offset printed ~ leaf + 543): the headword خدا with Mo'in's etymological footnote 3, quoted under node #3. It derives خدا from Pahlavi/Pazand xwatāy/xwadāy and canvasses xva-dāta-/xva-tāya- with Skt. svatas + āyu-; it also notes 'در پهلوی و پازند خواتای بمعنی شاه آمده و «خواتای‌نامک» یعنی «شاهنامه»'. The page is the right one, but it contradicts the arrow from zav-.\"},\n            {\"ref\": \"HRN:104\", \"status\": \"contradicts\", \"note\": \"Horn, Grundriss no. 471 (HRN.txt leaf 125 = printed p. 104): the entry for xudā, ending 'Die Durchsichtigkeit des Zusammenhanges mit xva(d)- hat wohl das d geschuetzt: als Grundform ist etwa *xva-dāta- / aw. xvadāta- (oder *xvatāya-) anzusetzen. Noeldeke ... bezweifelt die Richtigkeit dieser Etymologie'. Right page, right word — but Horn's source is xva- 'self', not the invoking root.\"},\n            {\"ref\": \"FSF:159\", \"status\": \"not_found\", \"note\": \"Noushin's Vazhe-namak: in the scan on disk (FSF_pages.txt, 484 leaves) printed p. 159 is the پیمودن/پیلوار page (leaf 163), with no خدیو. The book does treat the word, under the headword گیهان خدیو at printed p. ~407 (leaf 411), and discusses the very Ferdowsi line Nourai quotes ('سیامک به دست خزروان دیو / تبه گشت و ماند انجمن بی خدیو') at leaf 205, noting that some copies corrupt the hemistich to 'سیامک بدست خود و رای دیو'. The refs_online entry warns that this scan's printing is unidentified, so the discrepancy is most likely a different edition rather than a bad citation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. خواجه (MON_part1.txt line 57715)\", \"stance\": \"partial\", \"note\": \"'خواجه: (قد. ...) (ص.) بزرگ، صاحب، سرور، خداوند. مالدار، دولتمند' — Mo'in's Latin-script origin tag is unreadable in this OCR, but he treats the word as an old inherited term meaning 'lord', not as a form of خدا. He has no entry for خدیو in the scanned lexicon volumes.\"},\n            {\"src\": \"BQT\", \"where\": \"Mo'in's footnote on خواجه, vol. 2 leaf 238\", \"stance\": \"partial\", \"note\": \"'آقای پورداود این کلمه را مرکب از xva- اوستایی بمعنی خود + -če ... دانسته‌اند «حافظ شیرین‌سخن ۲: ۳۷»؛ بعضی اصل آن را «خواتای‌چه» از خواتای (خدای) پهلوی + چه (یای تصغیر) دانسته‌اند' — records exactly the xwatāy derivation Nourai draws, as one of several competing guesses, alongside 'معرب آخنواجا ... دزی ج۱ ص ۴۰۹'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 54\", \"stance\": \"contradicts\", \"note\": \"as under node #3: 'np. xudāi Gott = phl. xvatāi ... setzt ein zd. *xvataya- voraus', with Skt. svatas 'from oneself' — an internal Iranian compound, not a reflex of *ǵʰewH-.\"},\n            {\"src\": \"FSF\", \"where\": \"s.v. گیهان خدیو, leaf 411 (printed ~407)\", \"stance\": \"partial\", \"note\": \"'گیهان خدیو: از گیهان + خدیو [= خداوند، سرور]: جهاندار، ایزد' with the Ferdowsi citations — confirms the Persian sense 'lord, sovereign' that Nourai glosses 'governor, king', without an etymology.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"Gudam\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Proto-Germanic *gudan (neuter) 'god' > Gothic guþ, Old Norse guð/goð, Old English god, Old High German got. Watkins's appendix, which Nourai cites, states the derivation from *ǵʰu-tó- outright ('Germanic *gudam, god, in: a. Old English god, god: GOD; b. Germanic *gud-igaz, possessed by a god, in Old English gydig ... GIDDY'), and Klein and Pokorny say the same, Pokorny noting that the noun is originally neuter (the old neuter plural survives in Gothic guda and in galiuga-guþ 'idol'), which fits a -to- adjective substantivised as 'the invoked (thing)'. It is 'plausible' rather than 'confirmed' only because the reconstruction is still contested: Wiktionary observes that *ǵʰewH- with its laryngeal should have produced a long *ū, and sets against it a derivation from *ǵʰew- 'to pour' ('that which is libated', i.e. the object of a poured offering), plus a minority link to *gʷʰew- (OCS goveti 'to revere'). Nourai reproduces the majority handbook view.\",\n          \"derivation_fa\": \"ژرمنی آغازین *gudan (خنثی) «خدا» که در گوتی guþ، نورس کهن guð/goð، انگلیسی کهن god و آلمانی علیای کهن got بازتاب یافته است. واتکینز در پیوست فرهنگ American Heritage — همان مأخذ نورایی — همین اشتقاق از *ǵʰu-tó- را صریح می‌آورد و کلاین و پوکورنی نیز همین را می‌گویند؛ پوکورنی می‌افزاید که این نام در اصل خنثی بوده (جمعِ خنثای کهنِ guda در گوتی هنوز مانده است) و این با صفتِ فعلیِ اسم‌شده به معنای «آنچه خوانده می‌شود» می‌خواند. اینکه داوری «با احتیاط پذیرفتنی» است نه «درست»، از آن روست که بحث هنوز باز است: ویکی‌واژه یادآور می‌شود که حنجرهٔ ریشه می‌بایست واکهٔ کشیدهٔ *ū پدید می‌آورد و در برابر، اشتقاق از *ǵʰew- «ریختن» (یعنی «آنچه برایش شراب می‌ریزند») و نیز پیوند اقلیتی با *gʷʰew- را می‌آورد. نورایی همان دیدگاه اکثریتِ فرهنگ‌های معیار را بازگو کرده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gud%C4%85\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 526, s.v. gheu(e)-: 'Suffixed zero-grade form *ghu-to-, the invoked, god, in Germanic *gudam, god' — Nourai's box verbatim, spelling included.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 413-414\", \"stance\": \"supports\", \"note\": \"'Germanic *guda- n. god ... in Gothic gup m. god (the originally neutral form still in Pl. guda and in galiuga-gup idol), Old Icelandic god, gud ... Old English, Old Frisian, Old Saxon god, Old High German got'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. God; god, printed p. ~696\", \"stance\": \"supports\", \"note\": \"'for Teut. *guda-, which is prob. a participial formation ... meaning the invoked being, and corresponds to I.-E. ghu-to-m'.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'guda', 'guth' in SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's concise entry for God is not recoverable from this OCR; nothing quotable.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"God, good-bye, good-night\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three belong here, the third does not. GOD is the direct Old English continuation of Gmc *gudan and is listed under this root by Watkins and Klein. GOOD-BYE does belong etymologically: it is a contraction of godbwye (1570s) < 'God be with ye' (late 14th c.), so its first element really is God, though Etymonline notes that its modern spelling with good- is secondary, 'influenced by good-day, good evening, etc.'; Klein files it under God ('Cp. bigot, giddy, good-by, gossip'). GOOD-NIGHT, however, contains no god element at all: the adjective good is Old English gōd, Proto-Germanic *gōda- 'fitting, suitable', from a different PIE root *ghedh- 'to unite, be associated, suitable' (cf. OCS godu 'favourable time', Lith. goda), and Etymonline states explicitly that good and God are of different origins. Nourai has been misled by the same surface resemblance that reshaped good-bye. Watkins's own entry, which the box cites, lists only GOD and GIDDY.\",\n          \"derivation_fa\": \"از سه واژهٔ این خانه دو تا به این ریشه تعلق دارند و سومی نه. God ادامهٔ مستقیمِ *gudan ژرمنی در انگلیسی کهن است و واتکینز و کلاین آن را ذیل همین ریشه آورده‌اند. good-bye نیز از نظر ریشه‌شناسی به‌جاست: کوتاه‌شدهٔ godbwye (دههٔ ۱۵۷۰) از عبارت God be with ye (اواخر سدهٔ چهاردهم) است، هرچند املای امروزیِ آن با good- ثانوی و به قیاسِ good-day و good evening پدید آمده؛ کلاین هم آن را ذیل God ارجاع داده است. اما good-night هیچ عنصر «خدا» ندارد: صفت good از انگلیسی کهن gōd و ژرمنی آغازین *gōda- «مناسب، درخور» و از ریشهٔ هندواروپاییِ دیگری یعنی *ghedh- «پیوستن، درخور بودن» است، و اتیمانلاین تصریح می‌کند که good و God خاستگاه یکسان ندارند. نورایی فریبِ همان شباهت ظاهری را خورده که املای good-bye را هم دگرگون کرده است؛ خودِ واتکینز در همان مدخل تنها GOD و GIDDY را برشمرده است. پس این خانه در بخشی نادرست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/good-bye\",\n            \"https://www.etymonline.com/word/good\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 526 gives, as the English derivatives of *ghu-to- via Germanic *gudam, only 'Old English god, god: GOD' and 'Old English gydig ... GIDDY'. Neither good-bye nor good-night appears, so the reference supports one of Nourai's three words and is silent on the other two.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. God; god, printed p. ~696\", \"stance\": \"partial\", \"note\": \"'Cp. bigot, giddy, good-by, gossip' — Klein does attach good-by to God (gossip < godsibb 'god-relative'), but never good-night.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'good-bye', 'good bye' in SKT.txt\", \"stance\": \"silent\", \"note\": \"not recoverable from this OCR.\"},\n            {\"src\": \"POK\", \"where\": \"p. 413-414\", \"stance\": \"silent\", \"note\": \"Pokorny lists the Germanic god-words and their Christian compounds (godfather, godmother) but no salutation formulas.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Gheu-bh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"This box cannot hang under *ǵʰewH- 'to invoke'. The decisive point is phonological: the root of node #0 has a PALATAL *ǵʰ, as the Indo-Iranian reflexes prove (Skt. hávate, Av. zav-/zbā-, where *ǵʰ > h/z). An Iranian verb beginning in plain g-, such as Old Persian gaub-, cannot descend from it — it would have to appear as *zaub-. Cheung's Etymological Dictionary of the Iranian Verb (2007) s.v. *gaub 'to say (positively/negatively)' therefore leaves the reconstruction blank and writes flatly 'No IE etymology', with the fields '*PIE — LIV: — | Pok.: —' empty. Kent p. 182, the page Nourai cites, is the source of the label 'Gheu-bh': 'gaub- vb. say ... perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gausa- (q.v.)'. But Kent's *gheu- there is the sound/hearing root that yields Av. gaosa- 'ear', not Pokorny's invoking root of p. 413, and Kent himself only says 'perhaps'. So the box records a real (if tentative) suggestion of Kent's, misfiled under the wrong root.\",\n          \"derivation_fa\": \"این خانه نمی‌تواند زیر ریشهٔ *ǵʰewH- «خواندن، نیایش کردن» بنشیند و دلیل آن آوایی و قاطع است: همخوان آغازین آن ریشه *ǵʰ کامی است، چنان‌که بازتاب‌های هندوایرانی نشان می‌دهند (سنسکریت hávate، اوستایی zav-/zbā-، یعنی *ǵʰ > h/z). پس فعلی ایرانی که با g ساده آغاز می‌شود — مانند gaub- پارسی باستان — نمی‌تواند از آن آمده باشد؛ می‌بایست *zaub- می‌شد. از همین رو چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷) ذیل *gaub «گفتن» خانهٔ بازسازی هندواروپایی و ارجاع به LIV و پوکورنی را خالی می‌گذارد و می‌نویسد «هیچ ریشه‌شناسی هندواروپایی ندارد». کنت در ص ۱۸۲ — همان مأخذ نورایی — سرچشمهٔ برچسبِ Gheu-bh است: «gaub- فعل: گفتن ... شاید گسترشی با -bh از ریشهٔ *gheu- که با گسترش -s در gauša- دیده می‌شود»؛ اما آن *gheu- ریشهٔ «آوا/شنیدن» است که gaoša- «گوش» از آن است، نه ریشهٔ ۴۱۳ پوکورنی، و کنت هم فقط «شاید» گفته است. پس این خانه حدسی واقعی از کنت را زیر ریشهٔ نادرست نشانده و پژوهش امروزی آن را نمی‌پذیرد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0ewH-\"],\n          \"ref_check\": [\n            {\"ref\": \"KNT:182\", \"status\": \"partial\", \"note\": \"Kent, Old Persian, Lexicon s.v. gaub- (KNT.txt line 5341, leaf 205 = printed p. 182-183; Cheung cites the same place as 'Kent: 182b'): 'gaub- vb. say, mid. call one's self: Sas. Phl. gowet he says, NPers. goyad, inf. guftan: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gausa- (q.v.).' The -bh- extension is Kent's, so the label is sourced; but the parent root he means is the one behind gausa- 'ear', not Pokorny 413, and he hedges with 'perhaps'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *gaub, p. 113-114 (CHEUNG.txt lines 8221-8280)\", \"stance\": \"contradicts\", \"note\": \"'*gaub to say (positively/negatively) ... No IE etymology. *PIE — LIV: — | Pok.: — . REFERENCES: Horn 1893: 206; Christensen, Contributions II: 162; Nyberg II: 85; DKS: 86b'. Cheung declines any PIE reconstruction whatsoever.\"},\n            {\"src\": \"POK\", \"where\": \"p. 413-414 and index\", \"stance\": \"silent\", \"note\": \"Pokorny's ghau- article contains no Iranian g-initial verb and no -bh- extension; there is no lemma *gheu-bh- in the dictionary.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gheu(e)-, gheu-, gheu-\", \"stance\": \"silent\", \"note\": \"Watkins has gheu- 'to pour', gheu- 'to yawn, gape' and gheu(e)- 'to call, invoke', but no *gheu-bh- and no Iranian material under any of them.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 529 and Bd. II index\", \"stance\": \"silent\", \"note\": \"Walde-Pokorny's ghaua-/ghau- article likewise lists no g-initial Iranian verb of speaking.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Old Persian\",\n          \"words\": \"gaub, gub\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Persian gaub- 'to say', middle 'to call oneself', is one of the best-attested verbs of the Bisotun inscription: DB 2.21, 2.31, 2.51, 3.15, 3.59 gaubataiy, DB 1.84, 1.93, 3.35 agaubatā, in the recurring formula kāra hya hamiçiya manā naiy gaubataiy 'the rebel army which does not call itself mine'. Kent's lexicon gives the present stem gauba- and cross-refers 'gub- vb., see gaub-', which is exactly Nourai's pair gaub/gub: gub- is the zero-grade (weak) stem, with au reduced to u before the following consonant cluster, and it is the stem that yields the past participle. Bartholomae's Altiranisches Woerterbuch col. 482 has 'p. gaub- V. dicere. Praes. gauba-. Med. sich nennen, erklaeren ... np. gōvēd er sagt, np. guftan' — the same forms and the same Persian continuation. Abolghasemi (FFD p. 75) writes the reconstruction as Old Iranian *gaub- with 'gub the weak form of the root gaub, meaning to speak'.\",\n          \"derivation_fa\": \"فعل پارسی باستان gaub- «گفتن» و در وجه میانه «خود را خواندن/نامیدن» از پربسامدترین فعل‌های کتیبهٔ بیستون است: gaubataiy در DB 2.21، 2.31، 2.51، 3.15، 3.59 و agaubatā در DB 1.84، 1.93، 3.35، در قالبِ تکرارشوندهٔ kāra hya hamiçiya manā naiy gaubataiy «سپاهِ شورشی که خود را از آنِ من نمی‌خوانَد». کنت در واژه‌نامهٔ خود ستاک مضارع gauba- را می‌آورد و ارجاع می‌دهد «gub- فعل: رک gaub-»، و این دقیقاً همان جفتِ gaub/gub نورایی است: gub صورت درجه‌صفر (ضعیف) ستاک است که پیش از خوشهٔ همخوانی پدید می‌آید و ستاکِ صفت مفعولی از آن ساخته می‌شود. بارتولمه در ستون ۴۸۲ می‌نویسد «gaub- فعل: گفتن. مضارع gauba-... فارسی نو gōvēd «می‌گوید»، گفتن». ابوالقاسمی نیز در ص ۷۵ همین را با تصریح می‌آورد که gub صورت ضعیفِ ریشهٔ gaub به معنای «گفتن» است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:182\", \"status\": \"supports\", \"note\": \"KNT.txt line 5341 (leaf 205, printed p. 182-183): 'gaub- vb. say, mid. call one's self ... gaubataiy mid. DB 2.21, 31, 51; 3.15, 59. agaubatā imf. mid. DB 1.84, 93 ...' and line 5373 'gub- vb., see gaub-.' Both of Nourai's citation forms are Kent's.\"},\n            {\"ref\": \"FFD:75\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 75 (FFD_pages.txt pdf page 80, printed = pdf − 5): 'گفت < فارسی میانه guft < ایرانی باستان *gaub-ta ... gub صورت ضعیف ریشهٔ gaub به معنی «گفتن» است' and 'گوی < فارسی میانه gōw < ایرانی باستان *gauba-'. Exactly the gaub/gub pair and the Middle Persian outcome.\"},\n            {\"ref\": \"BQT:1821\", \"status\": \"supports\", \"note\": \"Borhān vol. 3, pdf page 618 = printed p. 1821 (running heads on pdf 616 read ۱۸۱۹, so printed = pdf + 1203): Mo'in's footnote on گفتن, 'گفتن ... از: گف (؟ گو) + تن (پسوند مصدری)؛ پهلوی ...، پارسی باستان gaub- «بارتولمه ۴۸۲»' — Mo'in derives the Persian verb from Old Persian gaub-, citing Bartholomae col. 482, which the local BRT text confirms (running head 'gaona- 482' on the leaf carrying the gaub- entry).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. 482 (BRT.txt line 9802)\", \"stance\": \"supports\", \"note\": \"'p. gaub- V. dicere. Praes. gauba-. Med. 1) sich nennen, erklaeren, ausgeben fuer, mit Nom.: vahyazdāta hya bardiya agaubatā Bh. 1.6 ... np. gōvēd er sagt ... np. guftan.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gaub, p. 113\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: gaub- (med.) to call oneself = Kent: 182b', with the full paradigm of attested forms — Cheung accepts the Old Persian verb (he denies only its Indo-European ancestry).\"},\n            {\"src\": \"TLM\", \"where\": \"grep 'gaub' in TLM.txt (Tolman, Ancient Persian Lexicon)\", \"stance\": \"silent\", \"note\": \"the relevant lexicon page is not recoverable from this OCR.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"guftan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian guftan, present stem gōw- (written <gwptn'> with the ideogram YMLLWN-), 'to say, tell'. The two stems come from the two grades of the Old Iranian verb: the present gōw- < *gauba- (intervocalic -b- > -w- in Middle Persian), the infinitive/past guft < *gub-ta (the weak grade gub- plus the -ta- participle suffix, with regular devoicing b + t > ft). Nyberg's glossary has 'guftan [gwptn'] gōb- ... to say, to tell, to utter, to pronounce, to recite, passim ... MPrs guftn gwy-; Paz. guftan, pres. 3d p. gōēd ... NP guftan gūy; the typical SW vb. for saying, as against NW vac-'. Cheung's Middle Persian section gives 'MMP gw-, BMP gwb- /gō(w)-/ to say, speak', with the past participle gwpt/gwft and the infinitive gwptn/gwftn. Abolghasemi (FFD p. 75), the reference Nourai cites, sets out the same two-stem derivation.\",\n          \"derivation_fa\": \"فارسی میانه guftan با ستاک مضارع gōw- (به خط پهلوی <gwptn'> و با هزوارشِ YMLLWN-) به معنای «گفتن». دو ستاک از دو درجهٔ آوایی فعلِ ایرانی باستان می‌آیند: ستاک مضارع gōw- از *gauba- (بِ میان دو واکه در فارسی میانه به «و» بدل شده) و ستاک ماضی guft از *gub-ta (درجهٔ ضعیفِ gub- به‌علاوهٔ پسوند صفت مفعولی -ta-، با بی‌واک‌شدنِ قاعده‌مندِ b + t > ft). نیبرگ در واژه‌نامهٔ خود می‌آورد: «guftan [gwptn'] gōb-: گفتن، بیان کردن... فارسی نو guftan gūy؛ فعل نمونهٔ جنوب‌غربی برای «گفتن» در برابر vac- شمال‌غربی». چونگ نیز صورت‌های فارسی میانهٔ مانوی و کتابی را با همین ستاک‌ها می‌آورد و ابوالقاسمی در ص ۷۵ — همان مأخذ نورایی — همین دو ستاک را به‌روشنی توضیح داده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FFD:75\", \"status\": \"supports\", \"note\": \"FFD p. 75 (pdf page 80): 'گفت < فارسی میانه guft < ایرانی باستان *gaub-ta ... گوی < فارسی میانه gōw < ایرانی باستان *gauba-' — precisely the Old Persian to Middle Persian step of this node.\"},\n            {\"ref\": \"MON:3333\", \"status\": \"not_checked\", \"note\": \"Mo'in's printed pagination cannot be mapped in the scans available (refs_online.json: 'Page numbers cannot be mapped online'), and the local MON OCR is unpaginated, so p. 3333 could not be located. Mo'in does treat گفتن (MON_part2.txt line 33002) and گفت/گفتار (lines 32982, 32991).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p. 85 s.v. guftan (NYB_vol2_glossary.txt line 1720-1723)\", \"stance\": \"supports\", \"note\": \"'guftan [gwptn'] gōb- [YMLLWN-, YMRRWN-; 3d p. sg. gwbyt ... gōbēt], opt. 2nd p. sg. gōbēš, pt. always gwpt' = guft: to say, to tell ... MPrs guftn gwy-; Paz. guftan ... NP guftan gūy; the typical SW vb. for saying, as against NW vac-'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, English-Pahlavi index (PHD.txt lines 3523, 3760)\", \"stance\": \"supports\", \"note\": \"'say guftan, P wāxtan' and 'speak dranjidan, guftan, P wāxtan' — MacKenzie's guftan is the SW Middle Persian verb, with Parthian wāxtan as its NW counterpart.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gaub, Middle Persian section\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: MMP gw-, BMP gwb- /gō(w)-/ to say, speak = DMMPP: 166af.', with perf. pass. gwpt/gwft and Inf. gwptn/gwftn.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"goftan; goptan; gap\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"goftan گفتن (present stem گو gū-, with the derivatives گفتار goftār 'speech' and گویش guyeš 'dialect' that Nourai puts in the box) is the direct and uncontroversial New Persian continuation of Middle Persian guftan/gōw-, itself from Old Persian gaub-: this is Horn's entry no. 926 on the page Nourai cites and Mo'in's footnote in Borhān p. 1821, which derives گفتن from Old Persian gaub- after Bartholomae col. 482. The other two words are less secure. گپ gap 'chat, talk, gossip' is joined to گفتن by both of Nourai's Persian authorities — Horn prints 'guften sprechen ... guftar Rede, gep Witz' in the same entry, and Mo'in ends his footnote on گپ (Borhān p. 1775) with 'ورک: گفتن' — but the -p- is the difficulty: inherited *-b-t- gives -ft- in South-West Persian, so a form with -p- is not the regular Persian outcome and gap is normally treated as an eastern/dialectal word (Mo'in's own comparanda in that footnote are Khorasani and Lori 'سخن', Kurdish gap, Ishkashmi gap 'conversation', Zebaki gap 'word', Sanglechi gap dah- 'to converse', Tehrani gap), i.e. a regional cognate rather than a descendant of literary گفتن. Wiktionary's Persian گپ entry gives no derivation at all beyond 'From Old Persian [Term?]' and 'Compare the verb گپتن (gaptan, goptan)' — which is Nourai's third word, گپتن, a rare variant infinitive built on the same unshifted stem; it is not in Mo'in or Borhān and was checked against the printed page image (the book does print گپتن, so the extraction is faithful). The Molavi couplet Nourai quotes (که ز هر ناشسته رویی گپ زنی / شرم داری وز خدای خویش نی) is the same verse Mo'in cites on Borhān p. 1775, from Masnavi book IV.\",\n          \"derivation_fa\": \"«گفتن» (ستاک مضارع «گو»، با مشتق‌های «گفتار» و «گویش» که نورایی در همین خانه آورده) ادامهٔ مستقیم و بی‌مناقشهٔ فارسی میانهٔ guftan/gōw- و آن هم از gaub- پارسی باستان است؛ همین را هرن در شمارهٔ ۹۲۶ صفحهٔ ۲۰۶ و معین در حاشیهٔ برهان قاطع ص ۱۸۲۱ (به استناد بارتولمه ۴۸۲) گفته‌اند. دو واژهٔ دیگر استوارتر نیستند. «گپ» را هر دو مرجعِ فارسیِ نورایی به «گفتن» می‌پیوندند — هرن در همان مدخل «gep: لطیفه» را می‌آورد و معین حاشیهٔ خود بر «گپ» (ص ۱۷۷۵) را با «ورک: گفتن» به پایان می‌برد — اما «پ» مشکل‌ساز است: خوشهٔ *-b-t- در فارسیِ جنوب‌غربی به -ft- بدل می‌شود، پس صورتی با «پ» بازتاب قاعده‌مندِ فارسی نیست و «گپ» را معمولاً واژه‌ای گویشی/خاوری می‌دانند؛ شاهدهای خودِ معین هم گویشی‌اند: خراسانی و لری «سخن»، کردی gap، اشکاشمی gap «مکالمه»، زباکی gap «کلمه، سخن»، سنگلیچی gap dah- «مکالمه کردن» و تهرانی gap. ویکی‌واژه نیز برای «گپ» هیچ اشتقاقی نمی‌دهد جز «از پارسی باستان [؟]» و «قس. فعل گپتن (gaptan, goptan)». «گپتن» همان واژهٔ سوم نورایی است، مصدری کم‌کاربرد بر همان ستاکِ دگرگون‌نشده که در معین و برهان نیامده؛ تصویر صفحهٔ چاپی بررسی شد و کتاب واقعاً «گپتن» چاپ کرده است، پس خطای خوانشِ اسکن در کار نیست. بیت مولوی («که ز هر ناشسته رویی گپ زنی / شرم داری وز خدای خویش نی») همان بیتی است که معین در ص ۱۷۷۵ برهان از دفتر چهارم مثنوی آورده است. در مجموع: «گفتن» درست، «گپ/گپتن» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%DA%AF%D9%BE\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:206\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 926 (HRN.txt leaf 227 = printed p. 206, running head '— 206 —'): 'guften sprechen, Praes. gōy-em, guftar Rede, gep Witz. ... ap. sqrt gaub-, gaubataiy sprechen, sagen; phlv. guftan, guftar, guv(i)šn (geschrieben gub-) ... kurd. gutin'. Horn gives the whole OP > Pahlavi > NP chain and puts gep in the same entry — both of Nourai's main claims.\"},\n            {\"ref\": \"BQT:1775\", \"status\": \"supports\", \"note\": \"Borhān vol. 3, pdf page 572 = printed p. 1775: the headword گپ with Mo'in's footnote 1, 'در خراسان و زبان لری بمعنی سخن است «فرهنگ انجمن‌آرا»؛ کردی gap (سخن + گفتگو) «ژابا ص ۳۵۷»، اشکاشمی gap (مکالمه)، زباکی gap (کلمه، سخن)؛ سنگلیچی gap dah- ... تهرانی gap (سخن)؛ رک: گفتن', and footnote 2 quoting the same Molavi couplet Nourai prints, referenced to Masnavi daftar 4 p. 290 (Nicholson).\"},\n            {\"ref\": \"BQT:1821\", \"status\": \"supports\", \"note\": \"Borhān vol. 3, pdf page 618 = printed p. 1821, Mo'in's footnote on گفتن deriving it from Old Persian gaub- (Bartholomae 482) and listing the dialect forms Tabari baoten, Gilaki bogoftan/bogotan/botan.\"},\n            {\"ref\": \"FFD:75\", \"status\": \"supports\", \"note\": \"as under nodes #8 and #9: Abolghasemi's derivation گفت < MP guft < OIr *gaub-ta, گوی < MP gōw < OIr *gauba-.\"},\n            {\"ref\": \"MON:3195\", \"status\": \"not_checked\", \"note\": \"Mo'in's page numbers cannot be mapped in the available scan; the entries themselves are present (گپ at MON_part2.txt line 29947: 'گپ: [- گب] (اِ.) سخن، کلام. سخن لاف و گزاف؛ سخن بیهوده و دراز' — which also confirms Nourai's variant spelling گب and his gloss 'gossip').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. گپ (MON_part2.txt line 29947)\", \"stance\": \"supports\", \"note\": \"'گپ: [- گب] (اِ.) سخن، کلام. سخن لاف و گزاف؛ سخن بیهوده و دراز' — the variant گب and the pejorative 'idle talk' sense that Nourai renders 'gossip'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *gaub, NWIR section, p. 113\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP guftan/gōy-, Kurd. (Kurm.) gotin, guhtin (supplet.) bēž-, (Sor.) gutin, kutin (supplet.) ḷē-, Shamerz. -get-/gūn- to speak' — the New Persian verb is the direct continuant of the Iranian root; Cheung's references list Horn 1893: 206, the page Nourai cites.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 926, p. 206\", \"stance\": \"supports\", \"note\": \"quoted above; the only handbook consulted that prints gep next to guftan.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'گپ' and 'گفتن' in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"Aryanpur's root dictionary yields no usable entry in this OCR for either word.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-195.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-06T02:37:53.974Z] TOOL RESULT

```
JSON OK
```


## [2026-09-06T02:38:00.029Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 tools/verify_check.py 195"
}
```


### [2026-09-06T02:38:01.828Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 6, 'confirmed': 5, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'not_checked': 5, 'not_found': 3, 'contradicts': 3, 'partial': 2}
books consulted: {'partial': 12, 'silent': 14, 'supports': 20, 'contradicts': 3} | by book: {'POK': 5, 'LKT': 4, 'KLN': 4, 'CHEUNG': 4, 'DEV': 3, 'MON': 3, 'SKT': 3, 'BRT': 3, 'ARY': 2, 'WLD': 2, 'AHD': 2, 'PHD': 2, 'NYB': 2, 'BQT': 2, 'AFM': 1, 'PLA': 1, 'PHN': 1, 'FSD': 1, 'HUB': 1, 'FSF': 1, 'TLM': 1, 'HRN': 1}
```


## [2026-09-06T02:38:11.798Z] TOOL CALL #83: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg195.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/195.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/195.png; git status --short"
}
```


### [2026-09-06T02:38:11.913Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75938 Sep  5 22:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/195.png
```


## [2026-09-06T02:38:14.514Z] TOOL CALL #84: Bash

```json
{
 "command": "git status --short | head -20"
}
```


### [2026-09-06T02:38:14.567Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:38:17.122Z] TOOL CALL #85: Bash

```json
{
 "command": "git status --short | head -20 && git check-ignore -v data/verification/page-195.json data/verification/sources/refs/ocr/BOOK/195.png"
}
```


### [2026-09-06T02:38:18.815Z] TOOL RESULT

```
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/195.png
```


## [2026-09-06T02:38:23.467Z] TOOL CALL #86: Bash

```json
{
 "command": "git status --short -- data/verification/ ; echo \"---branch---\"; git rev-parse --abbrev-ref HEAD; ls -la data/verification/page-195.json"
}
```


### [2026-09-06T02:38:23.529Z] TOOL RESULT

```
---branch---
verified
-rw-rw-r-- 1 sfmqrb sfmqrb 73071 Sep  5 22:37 data/verification/page-195.json
```


## [2026-09-06T02:38:25.590Z] TOOL CALL #87: Bash

```json
{
 "command": "cat .gitignore | head -20; echo \"---\"; git check-ignore -v data/verification/page-195.json; echo \"exit=$?\""
}
```


### [2026-09-06T02:38:27.495Z] TOOL RESULT

```
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
---
exit=1
```


## [2026-09-06T02:38:32.177Z] TOOL CALL #88: Bash

```json
{
 "command": "git config --get status.showUntrackedFiles; cat .git/info/exclude 2>/dev/null | tail -5; git status --short --untracked-files=all -- data/verification/ | head"
}
```


### [2026-09-06T02:38:32.257Z] TOOL RESULT

```
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```


## [2026-09-06T02:38:36.888Z] TOOL CALL #89: Bash

```json
{
 "command": "git ls-files data/verification/page-195.json; echo \"tracked? $?\"; git log --oneline -1 -- data/verification/page-195.json; git diff --stat HEAD -- data/verification/ | tail -3; git ls-files -o --exclude-standard data/verification/ | head"
}
```


### [2026-09-06T02:38:38.787Z] TOOL RESULT

```
data/verification/page-195.json
tracked? 0
96e431e Verify pages 192 (Gheu 1/zawr, kimiyâ, fuse) and 200 (Gŭrb/jurâb, Gurdos/gord, gul); data fix: page 192 missing blank box
```


## [2026-09-06T02:38:44.859Z] TOOL CALL #90: Bash

```json
{
 "command": "git show HEAD:data/verification/page-195.json | wc -c; git show HEAD:data/verification/page-195.json | md5sum; md5sum data/verification/page-195.json; git log --oneline --all -- data/verification/page-195.json | head"
}
```


### [2026-09-06T02:38:44.988Z] TOOL RESULT

```
73071
ca64afae83df4b5a65e914e10c45615b  -
ca64afae83df4b5a65e914e10c45615b  data/verification/page-195.json
96e431e Verify pages 192 (Gheu 1/zawr, kimiyâ, fuse) and 200 (Gŭrb/jurâb, Gurdos/gord, gul); data fix: page 192 missing blank box
```


## [2026-09-06T02:38:55.424Z] TOOL CALL #91: Bash

```json
{
 "command": "grep -c \"Maghrebi colloquial\" data/verification/page-195.json; git show 96e431e --stat | head -20; git log --oneline -3"
}
```


### [2026-09-06T02:38:55.560Z] TOOL RESULT

```
3
commit 96e431e1a43716ac3865537f635f5e4f95d680cf
Author: Sajad F. Maghrebi <sajad.faghfoor@gmail.com>
Date:   Sat Sep 5 22:37:59 2026 -0400

    Verify pages 192 (Gheu 1/zawr, kimiyâ, fuse) and 200 (Gŭrb/jurâb, Gurdos/gord, gul); data fix: page 192 missing blank box
    
    Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01Rzw2E62LY2codqSrh552Pi

 data/extracted/batch/page-192.json              |   10 +
 data/verification/page-192.json                 |  799 +++++
 data/verification/page-195.json                 |  332 ++
 data/verification/page-200.json                 |  723 +++++
 data/verification/process/verify-page-192.jsonl |  248 ++
 data/verification/process/verify-page-192.md    | 3940 +++++++++++++++++++++++
 data/verification/process/verify-page-200.jsonl |  251 ++
 data/verification/process/verify-page-200.md    | 3506 ++++++++++++++++++++
 8 files changed, 9809 insertions(+)
96e431e Verify pages 192 (Gheu 1/zawr, kimiyâ, fuse) and 200 (Gŭrb/jurâb, Gurdos/gord, gul); data fix: page 192 missing blank box
f7c9b92 Verify page 199 (Gôtra/gohar, Gras/gangrene, Gredh/grade); data fix: page 199 غانغرایا
629fe88 Verify page 188 (Gher 2/âzâr, qarn, chronos, garden)
```


## [2026-09-06T02:39:16.102Z] AGENT

Done. `verify_check.py 195` → **0 PROBLEM lines**, 15/15 nodes.

**Page 195 (book p. 165) — verdicts:** roots 2 confirmed; nodes 5 confirmed, 6 plausible, 4 disputed. Ref checks: 13 supports, 3 contradicts, 2 partial, 3 not_found, 5 not_checked.

**Disputed**
- Ghu 1 #3 `xvatây` (Pahlavi) — not from Av. *zav-* 'invoke'; MP xwadāy < PIr *hwa-tāwHā 'self-powerful'. Hübschmann p. 54 — the page Nourai cites — explicitly rejects it, as does Mo'in's footnote on Borhān p. 718.
- Ghu 1 #4 `خدا / خدیو / خواجه` — خدا descends from xwadāy but not from this root; خدیو is a Bactrian loan (χοαδηο, Sims-Williams); خواجه is from Skt. *upādhyāya* via Central Asia (Asatrian), unrelated.
- Ghu 1 #6 `God, good-bye, good-night` — God ✓, good-bye ✓ (< "God be with ye"), but *good-night* has no God element (good < PIE \*ghedh-); Watkins lists only GOD and GIDDY.
- Ghu 1 #7 `Gheu-bh` — PIE palatal \*ǵʰ gives Iranian z-, so OP *gaub-* cannot belong here; Cheung 2007 s.v. \*gaub: "No IE etymology". Kent p. 182's "perhaps a -bh- extension of \*gheu-" refers to the *gaoša-* 'ear' root, not Pokorny 413.

**Citation problems (book-side, not extraction)**
- `WLD:599` (node #2) → should be **WP I 529** (running head confirms; p. 599 is root *ger-*).
- `KLN:413` (node #2) → Klein p. 413 is the *cyto-* range; the zavaiti citation is s.v. "God" (~p. 696). 413 is exactly Pokorny's page, so it looks like a slip for POK:413.
- `KLN:237` → the carafe entry is at ~p. 248 in the 1966 two-volume scan (text matches verbatim).
- `FSF:159` → not in the available printing (p. 159 there is پیمودن); Vazhe-namak treats the word s.v. گیهان خدیو, ~p. 407.

**No transcription_suspect, no extraction errors.** Checked against the rendered page (copied to `data/verification/sources/refs/ocr/BOOK/195.png`): the book really does print "xadieve" and «گپتن», so the JSON is faithful. 10 web sources archived via `fetch_source.py`.
