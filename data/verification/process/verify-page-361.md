# Verification process log — verify-page-361


## [2026-09-07T19:29:04.408Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 361 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-361.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-361.json. Write /home/sfmqrb/git/rishe/data/verification/page-361.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 361` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:06.565Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:07.275Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:07.287Z] TOOL RESULT

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


## [2026-09-07T19:29:07.729Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-361.txt"
}
```


### [2026-09-07T19:29:07.751Z] TOOL RESULT

```
1	=== PDF page 361 (book page 331) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ner 1 : vital energy, man  (refs POK:765)
4	#1 (parent #0) [Avestan] refs=POK:765; SYN:81; HRN:238 | nar, nairya : man, male ; naire-manâw : manly mannered ☞Men 1 ; nairyava : manliness, strength
5	  #2 (parent #1) [Persian] refs=BQT:1796,2126,2132,2225 | nar «نر» : male ; Narîmân «نریمان» : "like a man", a male name ; nîrŭ «نیرو» : strength
6	#3 (parent #0) [Avestan] refs=POK:765 | nâirî : female, lady, woman
7	  #4 (parent #3) [Pahlavi] refs=SNS:264 | nâyrig : (pious) woman
8	#5 (parent #0) [Avestan] refs=POK:765 | hu-nara : good virtue, skill ☞Su 1
9	  #6 (parent #5) [Persian] refs=BQT:2381 | honar «هنر» : skill, virtue, art
10	#7 (parent #0) [Greek] refs=AHD; KLN:47 | a-ner, andros : man ; alex-andros : protector of men ☞Alek ; philo-anthrôpos : fond of people ☞Bhili
11	  #8 (parent #7) [English] refs=AHD | android ; Alexander, Andrew ; philanthropy
12	  #9 (parent #7) [Syriac] refs=VDQ:108 | 
13	    #10 (parent #9) [Arabic] refs=VDQ:108 | Edrîs : name of a prophet
14	      #11 (parent #10) [Persian] refs=MON5:109 | Edrîs «إدریس» : a prophet
15	  #12 (parent #7) [Arabic] refs=None | Eskander : Alexander
16	    #13 (parent #12) [Persian] refs=MON5:144 | Eskandar «اسکندر»
17	
```


## [2026-09-07T19:29:11.389Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-361.json",
 "description": "Read source JSON"
}
```


### [2026-09-07T19:29:11.486Z] TOOL RESULT

```
{
  "pdf_page": 361,
  "book_page": 331,
  "entries": [
    {
      "root": {
        "name": "Ner 1",
        "lang": "Indo-European",
        "refs": "POK:765",
        "gloss": "vital energy, man"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:765; SYN:81; HRN:238",
          "words": [
            {"translit": "nar, nairya", "gloss": "man, male", "script": null},
            {"translit": "naire-manâw", "gloss": "manly mannered", "script": null, "see": ["Men 1"]},
            {"translit": "nairyava", "gloss": "manliness, strength", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1796,2126,2132,2225",
          "words": [
            {"translit": "nar", "gloss": "male", "script": "نر"},
            {"translit": "Narîmân", "gloss": "\"like a man\", a male name", "script": "نریمان"},
            {"translit": "nîrŭ", "gloss": "strength", "script": "نیرو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:765",
          "words": [
            {"translit": "nâirî", "gloss": "female, lady, woman", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "SNS:264",
          "words": [
            {"translit": "nâyrig", "gloss": "(pious) woman", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:765",
          "words": [
            {"translit": "hu-nara", "gloss": "good virtue, skill", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:2381",
          "words": [
            {"translit": "honar", "gloss": "skill, virtue, art", "script": "هنر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; KLN:47",
          "words": [
            {"translit": "a-ner, andros", "gloss": "man", "script": null},
            {"translit": "alex-andros", "gloss": "protector of men", "script": null, "see": ["Alek"]},
            {"translit": "philo-anthrôpos", "gloss": "fond of people", "script": null, "see": ["Bhili"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "android", "gloss": null, "script": null},
            {"translit": "Alexander, Andrew", "gloss": null, "script": null},
            {"translit": "philanthropy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Syriac",
          "refs": "VDQ:108",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Arabic",
          "refs": "VDQ:108",
          "words": [
            {"translit": "Edrîs", "gloss": "name of a prophet", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON5:109",
          "words": [
            {"translit": "Edrîs", "gloss": "a prophet", "script": "إدریس"}
          ],
          "note": null,
          "quote": {"text": "عیسی و ادریس بر گردون شدند - با ملایک چون که هم جنس آمدند", "poet": "Molavî"}
        },
        {
          "id": 12,
          "parent": 7,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "Eskander", "gloss": "Alexander", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON5:144",
          "words": [
            {"translit": "Eskandar", "gloss": null, "script": "اسکندر"}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T19:29:13.472Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','HRN','BQT','SNS','AHD','KLN','VDQ','MON','WLD','BRT','PHD','NYB','IEC','ARY','FVQ','AFM','PLA','SKT','WEB','FSD','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-07T19:29:14.717Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
```


## [2026-09-07T19:29:38.530Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80 && echo \"---POK offsets---\" && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['POK']['page_offset']);print(d['POK'].get('lookup_hint'))\n\""
}
```


## [2026-09-07T19:29:39.604Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ner-1\\|ner-(1)\\|ner- 1\" POK_full.txt 2>/dev/null | head -20; ls POK*"
}
```


### [2026-09-07T19:29:39.836Z] TOOL RESULT

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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
---POK offsets---
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


### [2026-09-07T19:29:39.907Z] TOOL RESULT

```
62647:Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
```


## [2026-09-07T19:29:42.367Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62640,62760p' POK_full.txt"
}
```


### [2026-09-07T19:29:42.448Z] TOOL RESULT

```
'. (Greek Occidental Romance vowel prefix) 

Probably as " the under-age, dependent ' to ne- and pot/s. 

References: WP. II 329 f., WH. II 161 f., Trautmann 196. 
Page(s): 764 

Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 

Meaning: vital energy; man 

Material: 

Maybe Hittite: innarawatar 'life power', innarawant= 'strong', Luvian annar-ummi- 'strong' 

(Tischler 358ff) (under the influence of common Celtic -ns-, -nt- > -nn-)\ 

Armenian air. Gen. a/77'man, person' (z. Lautlichen s. Meillet Esquisse^ 83), ar^ "virile', 
whereof arvest, arhesV art '; New Phrygian avap "man'; Luvian annar6s. (under the 
influence of common Celtic -ns-, -nt- > -nn-); 

gr. vwpsT EvspysT Hes. (: Lithuanian noras, see below), avrip, -spa, av5p6c; "man', 
nvopsp) " manfulness ' (Hom.; p- metr. lengthening), avbpeioq " manly, gamy', £u-r|vu)p "rich 
an vitality ', ay-nvajp "gamy', Sp-cbijj av9pu)no(; (*vp-(ji)i|j ' Mannesantlitz habend '); about 
av9pu)no(; "person' (*av5p-u)no(; with secondary Aspiration [?]) s. Kretschmer Gl. 28, 246, 
Schwyzer Gr. Gr. 1 , 426^; 

Old Indie nar-{na) "man, person', Avestan nar-{na) ds. (Old Indie nara-h, Avestan nara- 
after Akk. naram, /75/'a/77 neologism); Old Indie nan, Avestan nairfmie, woman' (previously 
Aryan feminine formation); Old Indie narya-, Avestan nairya-^ manly, virile ': probably also 
Old Indie sunara-^\\y\\ of vitality, juvenile ', Avestan hunara-vn. " miracle power'. Old Indie 
nrtu-m. ' hero ', sOnrta 'vitality ' (5^- offers also Celtic: Old Irish so-nirt, cymr. hy-nerth 
"valiant, strong'); osset.-kaukas VN Nart- (\ran. *nar-^ra-); 

alb. /7/e/'"man, person'; (common alb. Serbian -e- > -Je-). 



Note: 

Probably alb. njeriu^rmvi derived from sabin. Afe/7^s because of solidified alb. PI. njerez 
'men, people', /T/eAez//?? "humanity' where -os, -^sending has been solidified. 

^^^nWar^rnuilive^inaur 



Latin neriosus ' resistens, fortis ', Nerio, -ienis " eine mit Mars in Kultverbindung 
stehende Gottin ' ('*the strong '), Nero, Sabine = ' fortis ac strenuus ' (Schuize Eigenn. 
315, 363, 485; sabin. Nerius ai^rees with Old Indie narya-), Oscan Gen. PI. nerum^ man; 
husband, great man| nobleman, hero ', Umbrian nerfAkk. PI. ' proceres, principes '; 

cymr. ner' hero ', Old Irish ner'boar' (also PN), gall. GN Nerios, Old Irish nert{*ner-to-), 
cymr. corn, nerth^ manfulness, army ', bret. nerz^ power ', gall. Nerto-briga, Esu-nertus 
etc.. Old Irish nertaim^\ strengthen', cymr. nerthu^ strengthen, support ', bret. nerza^ 
strengthen '; Old Irish nar{ *ndro-) "noble, bighearted ', gall. GN Nariai.; about Old Irish nar 
"blushful' s. S. 754; 

Old Germanic Nerthus^a goddess'. Old Icelandic Njgrdrvn. god's name; Lithuanian 
norasm. " volition ', nor/u, noref/'want, desire, will'. Old Prussian PN Nor-mans, ablaut. 
Ner-man\ Lithuanian nerteti, ablaut, nart/nt/'be angry with', /-n/rtgs^ becomes angry ', 
nartsasm. {*nar-sa-s) "boldness, rage, fury', /75/'Si>s "fierce, grim'; Old Prussian nertien 
Akk. "rage, fury', er-nertimai^ we enrage '; Slavic *non/b m. in Old Church Slavic nravb 
"custom', etc.; 

gr. hom. vwponj xciAk6(; after Kretschmer Gl. 32, 3 ff. "ore from Noricum', also not here; 
after Kuiper "full of vitality '. 

Proto-Altaic: *hjari 

Meaning: man, young man 

Turkic: *jerne 

Mongolian: *3er-me- 

Tungus-Manchu: *h(i)ari 

Korean: *nar-na- 

Japanese: *mi(n)tu 

Comments: AnnnJlJl 291. 



Uralic: hore 

Kartvelian: (Georg. nar- 'male camel' < Iran.) 

References: WP. II 332 f., WH. II 164 f., Trautmann 197 f., Kuiper Meded. Koninkl. Nederl. 
Akad. van Wetensch., Nieuwe Reeks, Deel 14, No. 5. 
Page(s): 765 

Root / lemma: ner-2{*he- ner-2) 
Meaning: under 

Material: Gr. vsprspoq ' unterer, tieferer, unterirdischer ' (through hybridization with svspoi 
"the subterraneous, underground', s. S. 312 *en^\x\\ also £V£pT£po(;); V£p9£(v) (and again 
£V£p9£(v), Doric Aeolic £V£p9a) "from under'; V£ip6(; "the Unterste' ( *nerio-)\ Oscan nertrak 
" left hand ', Umbrian nertru^ left ' (= v£pT£po(;); zero grade Old Icelandic nordru. "north'. Old 
English norderra'more northern'. Old High German /70/r//'d/7/" northern' (The north is to the 
direction of the prayer to the east = on the left); 

possible kinship from n-er-wWh *n-ei- "low, base' (see 312). 

Maybe alb. Geg ner, alb. /7o'e/'" under' [common alb. n >/7o' shift] 

References: WP. II 333 f. 
Page(s): 765-766 

Root / lemma: ner-3{*he- ner-3) 

Meaning: to conceal, cover, hiding place, hollow 

Material: established only for the Balto-Slavic: Lithuanian neriu, nert/" immerse, swim through, 

flee, einschlijpfen ', nerisxw. "beaver', narasm. ' Taucherente ', nan/a' cell of the queen bee 

', Latvian n/'rt, n/rdaf submerge '; Old Church Slavic ntrg, n ret/" penetrate' , sloven, po-
```


## [2026-09-07T19:29:52.745Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls WLD* 2>/dev/null; ls incoming/ 2>/dev/null | head -40; echo ---; grep -n \"ner-\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T19:29:52.803Z] TOOL RESULT

```
WLD_band3.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
---
781:nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepdt- 764.] ner-1, Under, also on the left; hence, with an eastward orientation, north. Suffixed zero-grade form *nr-t(r)o- in Germanic *north-, north, in: a. Old English north, north: NORDIC, NORTH; NORMAN; b. Old English northerne, northern: NORTHERN; c. Middle Dutch nort, north: NorsE. Compare deks-. [Pok. 2. ner- 765.] ner-2, Also aner-. Man; basic sense ‘vigorous, vital, strong.” 1. Oldest root form *aner- (with prothetic vowel) in Greek anér (stem andr-, from zero-grade “anr-), man: ANDRO-, -ANDROUS, -ANDRY; PHILANDER. 2. Extended zero-grade form *(9)nrt- in Sanskrit nrtyati, he dances (“moves vigorously”): NAUTCH. 3. Referred by some to this root (as if “having human eyes”; dps, eye; see ok’-) but more likely of unknown origin is Greek anthropos, man (earliest Greek form anthrék”os): ANTHROPIC, AN- THROPO-; LYCANTHROPE, MISANTHROPE, PHILANTHROPY, THEANTHROPIC. [Pok. 1. ner-(t)- 765.]
803:oner-. Dream. Suffixed form *oner-yo- in Greek oneiros, dream: ONEIROMANCY. [Pok. oner- 779.]
1244:AND en ANDRO- ner-2 ANDROECIUM welk-1 -ANDROUS _ner-2
1245:-ANDRY ner-2 ANECDOTE d6- ANELE elaia ANEMO- ane- ANEROID newo- ANESTHESIA au-5 ANEURYSM were-! ANFRACTUOUS bhreg- ANGARY angelos ANGEL angelos ANGELIC angelos ANGELICA angelos ANGELUS angelos ANGER angh- ANGINA angh- ANGLE! = ank- ANGLE? §ank- ANGLE ank- ANGST angh- ANGUILLIFORM ang¥hi- ANGUINE ang¥hi- ANGUISH angh- ANHYDROUS wed-! ANIL nei-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1782:LYASE leu-1 LYCANTHROPE ner-2, wlkwo- LYCHNIS leuk- LYCOPODIUM ped-!, wikwo- LYE leu(9)- LYMPHADENITIS eng¥- LYNX leuk-
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1902:NATAL gene- NATANT sna- NATATION sna- NATATORIAL sna- NATATORIUM sna- NATES not- NATHELEsS to- NATION gene- NATIVE gene- NATURE gene- NAUGHT ne, wektl- NAUGHTY ne NAUSEA nau-2 NAUTCH ner-2 NAUTICAL nau-2 NAUTILUS nau-2 NAVAL nau-2 NAVE? nobh- NAVEL nobh-, nau-2 NAVIGATE ag-, nau-2 NAVY nau-2
1935:Norpic_ ner-1 NORM gné- NoRMA gno- NORMAL gno- NORMAN man-1, ner-1 NORN_ sner- NorsE_ ner-! NORTH ner-1 NORTHERN ner-1 NOSE nas-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2368:THE? to- THEANTHROPIC ner-2 THECA dhé-1
```


## [2026-09-07T19:29:53.263Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==105' SYN.txt | head -60"
}
```


### [2026-09-07T19:29:54.469Z] TOOL RESULT

```
. ZeSti, #ega, SCr. deci (Boh. Zeci, Pol. gec for- merly the usual words for ‘burn’, now mostly ‘scorch, singe’), Russ. ge¢’; NIr. doigim (denom., ef. MIr. daig ‘fire’, NIr. doigh ‘pain’); Alb. djégé ‘burn’; Toch. tsdk- ‘burn’; cf. Lat. fovére ‘warm’.
2. IH *eus-. Walde-P. 1.111. Er nout-M. 1137 £, eee us-, Lat. arere ‘burn’, Grk. ew
3. Grk, Kalw, A
tt. xéw, fr, *xé i : zy aor. Hom. gna (# ’ aF-Lw,
Peay exnfa), Att. 2
ia Gr nt ee,
Withers with numerous derivatives.
Walde-p a clear outside connections.
Te 76. Kato &, Kaiouar b (or mer also ‘light for themselves’).
kal 4 + a,b (ch xale ‘it burns’), dis-
tinguished in aor. éaya (éavoa) a, éxanka b.
Grk. civrpnue : rpnfw ‘blow up, in- flate’, Russ. pret’ ‘stew, sweat’, ChSI. para ‘steam, vapor’, ete. Walde-P. 2.27. Prob. first intrans. ‘burn’ from the no- tion of ‘spurting out’.
Grk. aiéw (poet.) ‘light up, kindle’, aifouat ‘burn’ b, ‘blaze’: Skt. idh- ‘kindle’, edhas- ‘fuel’, iddha- ‘blazing, bright’ (cf. Grk. atéwy ‘blazing’, atOpws ‘bright, clear’), Lat. aestus ‘heat’, etc. Walde-P. 1.4 ff. Walde-H. 1.15f. In this group the underlying notion is ‘blaze’ rather than ‘burn’ in the sense of consume by fire.
Grk. ¢déyw, déyouar ‘blaze, burn’ b, gdéyw also ‘kindle’, or ‘burn’ a : dddé ‘flame’, Lat. flamma ‘flame’, flagrare ‘blaze’, etc. (1.82). Walde-P. 2.214.
4. Lat. ardére : Gridus ‘dry’, drére ‘be dry’, Grk. afw ‘be dry’, Skt. dsa- ‘ashes, dust’, Goth azgd, OE asce ‘ashes’, etc. Ernout-M. 75. Walde-H. 1.65.
Hence Rum. arde, the common word for ‘burn’, both a and b, while It. ardere and Sp. arder are mostly used in figura- tive sense.
Lat. cremdare, fr. *krem- prob. : *ker- in Lat. carbo, Goth. hauri ‘coal’, Lith. kurts ‘light a fire’, ete. Walde-P. 1.418 ff. Ernout-M. 229. Walde-H. 1.287.
Lat. adolére (‘burn’, a sacrificial term), Umbr. ufetu ‘adoleto’, root connection dub. Ernout-M. 14. Walde-H. 1.13.
It. bruciare (cf. abbrustiare ‘singe’), Fr. braler (OFr. brusler), of much dis- puted orig. Perh. fr. Lat. ustulare ‘singe’, with init. br by a blend with Gme. words like OHG brennan, brunst. REW 9097.
Sp. quemar, Port. guiemar, prob. fr. a late Grk. xayua ‘burning, heat’ (caima gl.) formed fr. éayv aor. of xalw, like NG xanyés ‘sharp pain, grief’, REW 2309.
SS In Public Domain. Gurukul Kangri Collection, Haridwar
Moraitzed by Arya Samaj Foundation Chennai and eGangotri
76 SELECTED INDO-EUROPEAN SYNONYMS
5. Ir. loscim, NIr. loiscim, W. Ulosgi, Br. leski, etym. dub. (fr. *lop-sk- : OPruss. lopis ‘flame’, Grk. Aduw ‘shine’,
etc.?). Stokes 256. Walde-P. 2.383. Pedersen 1.76 (fr. *luks-: Lat. lax ight’).
Ir. breoaim, deriv. of breo ‘flame’ (1.82).
Br. devi : W. dezfio ‘singe’, Ir. 3 sg. attai ‘kindles’ (cpd. with ad-), Skt. du- ‘burn’, Grk. dalw (*dar-1w) ‘kindle’, etc. Walde-P. 1.768. Thurneysen, Z. celt. Ph. 8.64f. Pedersen 2.507 f. (but here and 1.108 preferring to derive the Br. and W. words fr. *deg”h-, above, 1).
6. Goth. brinnan, caus. brannjan, etc., all the Gmc. words, with uses b and a ex- pressed by simple verb or causative re- spectively in the earlier periods, but later merged in a single form. Here the in- transitive meaning of the simple verb is, of course, the more original (in contrast to the opposite relation in Grk. xalw,
xalouat, and others), and this, analyzed as *b
```


## [2026-09-07T19:30:06.921Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 109 110 111 112; do echo \"=== rec $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -c 1500; done"
}
```


### [2026-09-07T19:30:08.095Z] TOOL RESULT

```
=== rec 109 ===
UGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
The more general
| |
| notion of ‘man’ as a homme, etc.; or they may be differen- ) and the more spe- | tiated (1) by related forms, as NHG aan as an adult male mensch vs. mann, (2) by unrelated ote a int may be combined | words, as Lat. homo vs. vir, ete. An old
» 88 in NE man, Fr. differentiation may be lost, as in VLatin, 79
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
80 SELECTED INDO-EUROPEAN SYNONYMS
where the use of homé was extended at the expense of vir; or it may be re- sumed, as in Rumanian, where bdrbat is frequently preferred to om when the meaning is ‘man’. There is not only extension but sometimes complete shift of application from ‘man’ to ‘man’, and of the latter again to ‘husband’.
The principal source of words for ‘man’, so far as their etymology is clear, is the notion of ‘earthly’ or ‘mortal’, thus di=== rec 110 ===
 man, OHG man, NHG mann, ete. (the most widespread Gme. word, with extension fr. ‘man’! to ‘man’); ChSl. madi (fr. *magjo- with a guttural suffix, as in Lith. Zmogus), SCr., Boh., Russ. muZ, Pol. maz (general Slay- ic word, with shift from ‘man’! to ‘man”); Skt. manu-, manus-, manusa-, manusa-. These point to an IE word for ‘man”!, but its root connection and so its ultimate semantic source are whol- ly uncertain. It has been derived from IE *men- ‘think’, or, since the designa-
tion ‘thinker’ seems too sophisticated, from *men- in an assumed earlier mean- ing ‘breath’ or the like; or by some con- nected with Lat. manus ‘hand’ (cf. NE all hands). Walde-P. 2.266. Falk-Torp 693. Feist 344 f.
In Germanic the prevailing meaning in the earlier period is ‘man’ (so Goth. manna reg. = avOpwros, only a few times = avyp). After the extension of use to include ‘man”, its place in the sense of ‘man’! was taken, except in English, by forms going back to a deriv. adj. like Goth. mannisks = avOphmivos. Hence OHG mannisco, mennisco, MHG, NHG, Du. mensch, Dan. menneske, Sw. men- niska. Falk-Torp 714. Weigand-H. 2.168.
In Slavic there was a complete shift from ‘man’! to ‘man’? and ‘husband’, and in part a later restriction to ‘hus- band’ with new derivatives in the sense of ‘man’, as SCr. muskarac, Russ. muzcina, ete.
3. Grk. aOpwros, etym. much dis- puted. But the old analysis av§p-wzos ‘man-faced, man-like’, fr. the ste=== rec 111 ===
�die’ in Skt. mr-, Lat. morz, etc. Walde- P, 2.276. Barth. 1148 ff.
2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
Many of the words for ‘man’, namely most of the Romance and Germanic and all the Slavic, were originally words for ‘man’!, or derivatives of these and have been included in the discussion 2.1.
Many of the words for ‘man’? were also used for ‘husband’, and some of them are quotable only in the latter sense, so that they do not appear in this list (so ON verr).
1. TE *wiro-, that is, *wt-ro- : Lat. vis, Skt. vayas, ete. ‘strength’. Walde- ot ff. Ernout-M. 1112 f.
at. vir, Umbr. uiro (ace. pl.): Ir. Jer, Nir. fear, W. gur, Nie nas Ge ae with neg. for ‘no one’); Goth. wair Gat Chee OE wer, ete. (old : ) Dut now obs. except in epds.,
as NE Werewolf, N. ? Weitere ae HG wergeld; also NE
» Ay, vira-,
2. TE *ner-, nert ‘strength, tion of ‘stren
Lith. vyras, Lett. virs;
Various cognates, as Ir. might’, show that the no- gth’ is dominant, as in IE
*wiro-, but the ultimate root connection is uncertain. Walde-P. 2.332f=== rec 112 ===
 burg 1.254 f. (best account of the com- plicated history). REW 962. Gamill- scheg 83. NED s.v. baron.
Rum. bdrbat, fr. Lat. barbatus ‘beard- ed’ through Byz. BapBaros used for one who was not aeunuch. Cf. NG BapBaros used of an animal that is not castrated, as adoyo BapBaro ‘stallion’.
4. Br. gwaz, fr. OBr. guas, MBr. goas
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
82 SELECTED INDO-EUROPEAN SYNONYMS
‘servant’ = W. gwas, Ir. foss ‘servant’, etc. (19.438).
5. ON karl and karlmadr, OF ceorl, OHG karl, all meaning ‘man’, esp. the ‘man without rank, freeman’, in the earlier period a term of esteem (as in the proper name Karl), later one of dis- paragement or contempt, asin NE churl,
OE wep(en)-man, wepned-man ‘man, male’, cpds. of w&pen ‘weapon, penis’ (4.492), wepned ‘male’.
OHG gomman, cpd. of gomo (2.1) and man.
6. Skt., Av. vtra-, nar-, above 1, 2. Skt. pumazis-, pums- ‘man, male’ (ys,
NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE wo
```


## [2026-09-07T19:30:14.819Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 259 260 261; do echo \"=== rec $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -c 2000; done"
}
```


### [2026-09-07T19:30:16.095Z] TOOL RESULT

```
=== rec 259 ===
— 237 —
*m + V^göp- "behüten, verwahren*, vergl. ai. X^göp- ;
plilv. n(i)huflan 'verbergen*.
kurd. nixiftifi *sich verbergen*, nix^ftin Causat.
^verbergen.
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.
=== rec 260 ===
— 288 —
1062. niyä 'Grossvater, Ahne (Plur. myagän),
ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
Ahne'; phlv. nyok.
af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
(250).
1063. niymn 'Scheide*.
ap. *nigama', vergl. skr. w^ + l^f/am-, mgamd-
'Einfügung (aber nur als ritueller t. t.), vorgl. np.
peyam (de Lagarde, Ges. Abb. 79).
Unsicher ^).
1064. nirö {*n^rö) 'Kraft, Macht'.
aw, '^nairyava- 'Mannhaftigkeit', vergl. nrnrya-
mannhaft'; ai. ndrya-; phlv. nerök,
1065. ni» auch', hemz (Sahn. I, 167 Vers 691), ?:x (Is.
1, 15).
ap. *anyadadi^) 'irgend wie anders' (Säle mann,
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.
=== rec 261 ===
- 239 —
ap. fiaiha- \schön, gut* ; phlv. neicah, nSwakih, new
(PPÖl.) 0.
1069. nem 'Hälfte, halb*.
aw. naema- *halb* in naemo asm, na^me /saf^ti,
vd. 4, 45, Geld n er, Studien I, 100 [na^mqm im
ZPGl. bedeutet nicht *halb*); skr. nvma- halb*; phlv.
mm, nSmak.
kurd. nTw *Hälfte, vergl. nlwrfiz 'Mittag*; afy. mmai;
bei. vergl. nl^röt^, nSnnöc, n. nermös 'Mittag', mmsap,
n. nSmSaf 'Mitternacht* (269) ; sar. L W. naim.
Vergl. D''i13X (Talmud) 'halb (sc. gar), nur zur
Hälfte (sc. gebraten)*, de Lagarde, Semitica I, 39.
1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
aw. *n? — \/gaos-, vergl. apa gaosay^iti; phlv.
n(i)yösJtany n(i)yö/sltan bezw. n(i)gösltan'') 'hören'; ai.
[/"ghöS'^ ghösati mit d 'hören, horchen auf.
bei. mgösag, niyösay (262).
>) Vergl. Fr. Müller, WZKM. 5, 265.
Die jüngere phlv. Form tiek liest Justi fZDMG. 46, 288) zwoi
Mal auf Gemmen (die letztere derselben, JRAS. XIII No. 45, die ich
ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
ZDMG. 11, 320 als semitisch (!) entziffert, worauf mich Herr Cler-
mont-Ganneau aufmerksam macht).
*) de Lagarde^s CBeitr. zur altb. Lex. 76) von Darmesteter
f6t. ir. I, 85 Note 2) wiederholte Erklärung aus aw. yao^nti' ist ver-
fehlt ; phlv. ftffJyö/Sitan^ das auch gelegentlich n(i)ybHltan geschrieben
sein kann (aber wo?), beruht auf einer im Pchlevl häufigen graphischen
Eigentümlichkeit.
Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
l/kar8', kasiian u. s. w.), vergl. auch bereits aw. pä^no" gegen ai.
pärsni: Der Übergang von rs in /S ist dem gegenüber nur ein schein-
barer in äia^s aus ätars und Syäva^^ aus Si/ävarsati-; )^h soll hier bloss
eine scharfe oder wahrscheinlich etwas modificirte Aussprache des s
bezeichnen, wie sie in ^^ar^set (vergl. Hörn, Mitteiluiigen, Heft IV,
S. 34) berechtigt war. Diese Aussprache wurde dann weiter über-
tragen, z. B. phlv. Zartux^t (aw. Zara^usfra-), daraus Zerduhest etc. des
SähnSme, vielleicht kÜ^sU
```


## [2026-09-07T19:30:25.575Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i bqt; echo ---; ls incoming/BQT | head; echo ---; ls ocr/ ; echo ---; ls ocr/BQT 2>/dev/null | head -50"
}
```


### [2026-09-07T19:30:25.636Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
---
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
---
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
---
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1296.png
1296.txt
1296.vision.txt
1297.png
1297.txt
1298.png
1298.txt
1299.png
```


## [2026-09-07T19:30:26.201Z] TOOL CALL #13: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-07T19:30:26.249Z] TOOL RESULT

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


## [2026-09-07T19:30:30.848Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for f in BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"=== $f\"; wc -l $f; grep -c \"pdf page\" $f; head -5 $f; done"
}
```


### [2026-09-07T19:30:32.084Z] TOOL RESULT

```
=== BQT_v3_pages.txt
51425 BQT_v3_pages.txt
721
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
=== BQT_v4_pages.txt
22553 BQT_v4_pages.txt
553
[pdf page 1]
[pdf page 2]
ه
و سم
۰ و
=== BQT_v5_pages.txt
10090 BQT_v5_pages.txt
293
[pdf page 1]
5
[pdf page 2]
,۶ +مه
مان ها
```


## [2026-09-07T19:30:36.807Z] TOOL CALL #15: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'), ensure_ascii=False, indent=1))\nprint(json.dumps(d['MON'].get('scans'), ensure_ascii=False, indent=1))\nprint(d['MON'].get('local_file'), d['MON'].get('page_offset'))\n\""
}
```


### [2026-09-07T19:30:38.030Z] TOOL RESULT

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
null
['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None
```


## [2026-09-07T19:30:46.299Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))['map']\nfor p in ['1796','1795','1797']: print(p, m.get(p))\n\""
}
```


### [2026-09-07T19:30:47.647Z] TOOL RESULT

```
1796 None
1795 None
1797 592
```


## [2026-09-07T19:30:48.529Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ndef getpage(f,n):\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    parts=re.split(r'\\[pdf page (\\d+)\\]',txt)\n    # parts: [pre, num, text, num, text...]\n    for i in range(1,len(parts),2):\n        if int(parts[i])==n: return parts[i+1]\n    return None\nfor n in (209,215,308,464):\n    print('===== v4 pdf page',n,'printed',n+1917)\n    t=getpage('BQT_v4_pages.txt',n)\n    print((t or 'MISSING')[:1200])\nEOF"
}
```


### [2026-09-07T19:30:49.879Z] TOOL RESULT

```
===== v4 pdf page 209 printed 2126

ر3 -۱۷۹-
وامق خوانند۱ » و چون برهفده رسد‌آترا دست | عربی سه معنی دارد : اول شرط و کرو قمارک »
خون گوبند » واگر از دست خون بگذرد حکم دوم اشان وجای زخم وجراحت ۴ » سیم تهلکه
اول‌پید! میکند چه داو بر هژده نمی‌باشد -ودر | واضطراب .

بیان هشتم
در نون با رای بی نقطه مشتمل برسی ودش لغت وکنایت

فر « بفتح اول و سکون ثانی » معروف | آن برميآید ‎٩‏ - و بمعنی خنثی‌هم هت و آن
است که قیض ماده باشد ۴ - و زشت و کربه | شخصی باشد که آلت مردان و زان هردو داشته
وداهموار را نیز گوبند همچو ثرکد! پمنی کدای | باشد (۱)
باهموار و درشت ‎٩‏ - ونام پدر سام است و او را فرا *۱- پروزن سرا » دیوارکوچکی را
نریم و نربمان هم میگوبند٩‏ - وآلت رجولیت | کوبند که در برابر چیزهاکشند تا شماید.
را دی ز کفته اند ۷ - و کوعه و موجه آب ۸ - راك < بفتح اول بروزن هلاك » بمعنی
و غاخ میالین درخت که شاخهای دیگراز اطراف | همیعه و دایم وبر دوام باشد ۰۱۱

)0( خم۱: هردو دارد .

۱ ر4: وامق. ۴ - (عر) «دب محركة. تیراندازی وآنچه درمیان کنند چون
در چیزی کرد بندند.» « منتهی‌الارب > - ۲ - (عر) « ندية بالفتح, شان جراحت که بر
پوست باقی‌باشد » ندب محر كة , وانداب ولاوب جمع . » « هنتهی الارب >

۴ - بتخفیف و تشدید راء » ابرانی باستان - 327 « بارتولمه ۱۰4۷ ۰ پهلوی 287
« نیب رکه س ۱۵۵ ۰۶ اوستا - 82۳ (هرد) . هندی باستان - 34۳ » افغانی32۳ ۰ استی2216,
1 (
===== v4 pdf page 215 printed 2132

فرةآب ۱ -۱۳-
نره دیو ۱ - وآلت تثاسل راهم گفته آند ۲ - فرق ۸ - بروزن خری » آلت رجولیت
و بممتی موجه وكوعهةٌ آب هم آمده است ۳ - | را کوبند مطلقاً واه از اسان و خواء از ()
و ساق درخت را هم میگویند۳ - و دندانهکلید | حیوان دیگر باشد ‎٩‏ .
را یز کوبند 8 - و بمعنی خنتی «م‌هست بعثی ریم < بروزن کریم . تام پدرسام است
شخصی (۱) که آلت مردان و زنان هردو دارد - |[ که جد رستم باشد *۱.
وگدا و کدایی کننده را نیز کفته‌اند ‎٩‏ . نریمان ندیه بروزن کربمان ۰ بدمنی
نرة‌آب -کنایه از موج آب و کوعهة نریم است که جد رستم زال باشد .
آب باشد ۷ .
ی سم
() چش : - یمتی شخصی - () خم ۱ : - از - :
۱ - بتخفیف وتشدید راء ( هردو ) : ولره غول ولره خر :
گر بود تره خر اندر وی رود آن رحم وأن روده‌ها وبران شود .
مولوی بلخی رومی « فرهنگه نظام *.
۴ - من‌گفتم این حدیت ومیان دو رن من امانند ترب غا#فری سخت شد اره +
۰ سوزنی سمرقندی « فرهنگه نظام >
۴ - ازدر ماده بین که چون سینةٌ تیخ روی او تیغ صفت شکافته کنید آب را نره .
سیدلویکی * جهانگیری ۰ < فرهنکه نظام *
در رشیدی مصراع دوم باین صورت آمده : تبیغ صفت شکافته کنید آب راه نر » و محشی رشیدی
کوید : « در سخهٌ جهانگیری وسروری «کنید آب را نره » و همان صحیح است *
۴ - ر4 : جهانگیری . 8 مسحف « تره » ( رك : لفت فری ص 4۶۲ ۱۸۹۰
ح )هه (هم.) ۹ جمع‌آن برکان (ه.م.) ۷ رل تجح ۳
۸ از : بر (همم.) ی (نب
===== v4 pdf page 308 printed 2225

وود نیرز
یراج است که سحروساحری وافون‌وافونگر: ی یر 8 « بکراول بروزن لیکو., بمعنی
وطلسم ومکر و حیله وقون باشد ۱ - وهیولای ‏ زور وقوت وتوالایی باشد ۴ - و پمعتی تقدیر هم
هرچیز را نی زکوبند - وآنچه مرتبدّاول نقاغان ‏ بنظرآمده‌است چنانکه کوبند « برهرلیزو» یعنی
بانگشت و زغال نفش وطرح کنند وبکهند ۲ ؛ | برهرتقدیر 8 -
وبفتح اول هم آمده است. نیرومند ۱ - بسمنی توانا و خداوند
نیرنود؟۴ - بکسر اول و سکون ثانی | زور وقوت وقدرت باشد .
وثالك ونون بوا و کشیده و بدال زده , بمعنی‌فکر نیریز - بکر اول وسکون‌آخر که‌زاي
ونظر است واندیشه ونگریستن باشد بعنی پافتن | نقطه‌دار باشد . نام شهری است هشهو رکه درآن
حقیقت چیزها بفکر وخیال. آهنگران بهار میباشند ۷ - و نام شعبه ای هم
۱ - زهیچگونه بدو جادوان حیلت‌ساز ‏ بکار برد نداشد حیلت و لیرنگه .
فرخی سیستانی « لغت فری ص ۲۸۸*.
۴ -« برنکه دیگر , رنگه باشد که نکارگران زنند . فرخی (سیستانی ) کفت :
همه عالم ز فتوح توانگاری گشته است همچوآ کنده صد رنگه نوآیین نیرنگه»
لغت فری ص ۲۸۸ *.
واین بیت دردیوان فرخی‌چاپ عبدالرسولی(س۲۰۷) نیز بهمین صورت‌آمده ؛ منتهی بجای نوآریین
«نگارین»ثبت شده . علامه دهخدادربارةاین‌پبت نوشته اند : «سپرنگه است بممتی‌سیمرغ ولیرنگه
غلطاست». رك: سیرنگه . بیت ذبل هم ازخاقانی شروانی درفرهنگه نظام شاهد معنی‌متن آهده ::
در غمزهٌ جادوی او تیرنگه رنگارنگه بین
===== v4 pdf page 464 printed 2381

نها هنکه
باشد ۱ - و کنایه از تیغ و شمشیر هندی «م ْ وکاف فارسی » چند معتی دارد : ۱ - سنگینی
هت؟ . 4 وتمکین ووقارباشد۴ . ۲- قصد واراده وآهنگه
هنگ؟ - بنتح اول و سکون ثانی | طرفی وجائیه ۰ ۳- غار وشکاف کوه باشد۹ +
۱- نیز هندی < هندوستانی را بزبان مردم هندوستان که زبانی است مرکب از
سانکریت و لهجه‌های هندی و فارسی وعربی» اطلاق کنند. ۰
۴ - ۶ وآن (عمعیر) چهارده گونه است : یکی بمانی » دوم هندی ... » * نوروژنامه
س ۳۹ > وهندی شمشیرست که آخن آنرا از هندوستان آورده و یا در هندوستان ساخته
باشندء, وآن را هندوانی ومپند وهند کی ( مأخون ازهندوك فارسی [پهلوی] ) نیز خوانده اند .
«تملیقات نوروز نامه ص۳۱۵*. ۴ - دریپلوی 8888 (قهم » معرفت) «اولوالا ۶۲۳۹ ۰ در
اوراق مانوی بپارتی 11888 [ء و۲۲ ( بممنی * بیزاری » تنفر ) (۲ ) ر4 :
.۳ و1 (176 ,8905 ...صهزوعهط ۸۸:41 ‎٩۶‏ اعنا ۸ ,116025128 آقای پورداود
نوشته‌اند: «هنکه درفارسی‌بممنی قصد ولیت گرفته شده.آهنکه با پیشاوند «1» درزمان ما رایج‌تر
است . ناگزیر هنگه ( ۳ آهنکه ) از پارسی باستان بما رسیده . اگر از زبان آن روز کلران
این‌واژه بجا مانده‌بود بایستی نپنکه 18888 باشد. اینکه حرف « تم > ازپارسی باستان واوستایی
درفارسی به «۸» تبدیل میکردد . نظایر بسیار دارد چون میتهر 82111272 ۳ مپر؛ چیتهر61110۳8
چهر و ماند اینها . دراوستا فعل تهنگه 10288 بمعنی کشیدن بسیار بکار رفته و
```


## [2026-09-07T19:31:12.119Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\nd={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nprint('==== 308 full ===='); print(d[308])\nfor n in (461,462,463):\n    print('==== ',n,'printed',n+1917,'====')\n    print(d.get(n,'MISSING')[:1400])\nEOF"
}
```


### [2026-09-07T19:31:13.559Z] TOOL RESULT

```
==== 308 full ====

وود نیرز
یراج است که سحروساحری وافون‌وافونگر: ی یر 8 « بکراول بروزن لیکو., بمعنی
وطلسم ومکر و حیله وقون باشد ۱ - وهیولای ‏ زور وقوت وتوالایی باشد ۴ - و پمعتی تقدیر هم
هرچیز را نی زکوبند - وآنچه مرتبدّاول نقاغان ‏ بنظرآمده‌است چنانکه کوبند « برهرلیزو» یعنی
بانگشت و زغال نفش وطرح کنند وبکهند ۲ ؛ | برهرتقدیر 8 -
وبفتح اول هم آمده است. نیرومند ۱ - بسمنی توانا و خداوند
نیرنود؟۴ - بکسر اول و سکون ثانی | زور وقوت وقدرت باشد .
وثالك ونون بوا و کشیده و بدال زده , بمعنی‌فکر نیریز - بکر اول وسکون‌آخر که‌زاي
ونظر است واندیشه ونگریستن باشد بعنی پافتن | نقطه‌دار باشد . نام شهری است هشهو رکه درآن
حقیقت چیزها بفکر وخیال. آهنگران بهار میباشند ۷ - و نام شعبه ای هم
۱ - زهیچگونه بدو جادوان حیلت‌ساز ‏ بکار برد نداشد حیلت و لیرنگه .
فرخی سیستانی « لغت فری ص ۲۸۸*.
۴ -« برنکه دیگر , رنگه باشد که نکارگران زنند . فرخی (سیستانی ) کفت :
همه عالم ز فتوح توانگاری گشته است همچوآ کنده صد رنگه نوآیین نیرنگه»
لغت فری ص ۲۸۸ *.
واین بیت دردیوان فرخی‌چاپ عبدالرسولی(س۲۰۷) نیز بهمین صورت‌آمده ؛ منتهی بجای نوآریین
«نگارین»ثبت شده . علامه دهخدادربارةاین‌پبت نوشته اند : «سپرنگه است بممتی‌سیمرغ ولیرنگه
غلطاست». رك: سیرنگه . بیت ذبل هم ازخاقانی شروانی درفرهنگه نظام شاهد معنی‌متن آهده ::
در غمزهٌ جادوی او تیرنگه رنگارنگه بین در طبم خاقانی کنون سودای کوا کون نگر.
۴ - از دساتیر ۶« فرهنگه دسانیر ص ۲۷۲ > « فاب ۱ : ۸۷ ۰
۴ - 217۵ (08676) ( زور . قوت ). اوستا 0881712۷8 (رجولیت » مردانگی)»
قی -88179۷8 (مردانه ) ؛ هندی باستان -84۸7[8 » پهلوی 28۲۵1 « اسشق ۱*۹4 و رل :
هوبشمان ۰.۱۶۹4 * نیرو » زور وقوت باشد.» رك : لغت فری ص 2۱۹
مرا پادشاهی آباد هت «ما ن کنج ومردی ولبروی دست.
فردوسی طوسی ۶ شاهنامة بخ ج اص ۰*۹۷
8 - رك : فرهنگه دساتیر ص ۲۷۲ ۰ ‎٩‏ از : یرو (هم.) ۲ مند ( پوند *
اصاف ) :+
کور اگر چند بود لیرومند با پدستش گرفت با بکمند .
امیرخرو دعلوی « اشراج ».
۷ - « ریز در جنوب غربی کرمان و شمال ولایت هفتگاه و مشرق درباچهٌ بختگان
واقع شده و راء عمدء اتصال فاری به یزد وکرمان از آن میگذرد . لیربز را میتوان بدو قسمت
تیم کرد : اول لیربز (خاس) » دوم اصطپبانات . رك : کیهان . جغرافیای سیاسی‌س ۰۲۸۱
بقیه از حاشيةٌ صفحهٌ قبل
بیرنگه ازجملةٌ کلمات دینی زرتعی است که پس از رواج اسلام در ایران و بیگانه غدن ابرایان
بتدریج از مصطلحات پیشینیان , از معنی اصلی وقدیمی خود منحرف کردیده, ازآن محر وطلمم
وشیده وافون وحیله اراده کرده‌اند. شاید تأثیرات‌خارق‌الماده‌ای که درقدیم برای ليرنگهاینداشته
میشده » سیب بروز معانی نو شده باشد: ۸ پورداود . خرده اوستا ص ۵۹-۵۸

====  461 printed 2378 ====

اس اند
درقدیم هندرهندوستان‌پشبه قاره‌ای که‌اخیرآً بدو 1 :
مملکت هندوپا کستان‌تضیم کردیدماطلاق‌میشده, 78 3 ۹
امروژه اسطلاحاً هندوستان شبه قارة مزبور را ( سا 5 ن ل در
کویند وهندبمملکتی که‌از یم هندوستان‌پدید ۵ اج بومران ان
آمده . مقابل پاکتان (وکاه هر دو را نی ۹ ۵ ۹
یکدبگر بکاربرند) . هند دره ماه آوت۱۹4۲ 0 رو
م. ازاستممار انگلستان درآمد وستقل گردید. 1 ۱ ۱
در٩؟‏ ژانوبه *۱۹۵م. جمهوریت اعلام گردید. 1
قانون اسامی هند (غامل ۳۹۵ اصل و۸ضمیمه) ۸ پا
تا 9 ار
از ژانوبه ۱۹۵۰رسماً بموقع اجراگذاشته شد. ز چم روم
ت کل هند بنا پر سر شماری ۱۹۵۱ رااوک صحا 5۸8
جممیت هند بنابر سر شماری ۰۱۹۵۱ ۱ 7:1 5 ل
۵ تن (باستثنای استان جامو و ی وس لد
کشمیرولواحی‌قبیله شین اسام) میباشد . مردم ۹ : ۵
هند دارای مذاهب ذَبل هتند : هندو (۸4/۹۹ ۸ 5 را
کل جسیت) , صلمان (۹/۹۳ کل جمسیت) ۰ لت
بقیه دزحاشیه صذْحهٌ بعد شان‌هند
هند 1 /
سود بو نم ۸ یف "ور ۹
رطع یا ۳ و ی زو
یک هط 7
1 بی نم 9 هی ت۲۲
مب ۳ ‌ِ : 0 ً هد
۰ ۳ ججایت ی بو 0۳
سحسدم رب چا رسمه
1 اس ۳ امیش وف َ
ّ قرن (ل و تمو اي ۳ ره
4 زیر تیه ی 8
۹ 1 7 3 ایالات بکزی یرل 7 ِ ن
اه با هیا
شاد رگم ۹ مدا ۸ ب
هار ۹
۳1 4 راگره
۱ هگ
شیر :۳
اسستا ۱ اه
۳
۲
(برهان قاطع ۴۰۰)

====  462 printed 2379 ====

مفنها هل
هم بوده است۹ (۱) + زده » بمعنی هندیا باشد که‌کاسنی است۴ .
هندبا؟ « بکر اول و مکون نانی هندسان؟ باسین بی لقطه بر وزن
وثالت وبای ابجد بالف کشیده . گیاهی است تلخ | هندوان » مخفف هندستان و هندستان مخفف
که آنرا بفارسی‌کاستی میگویند وبیخ آ نراعربان هندوستان .9
اصل‌الهندیا خواند . هندسه* « بکراوزوناك۹ وفتح-ین
هندبید.- بکراول‌وسکون نانی‌ونالث | بی‌نقطه . بمعتی اندازه وشکل باشد - وارقامی
وبای ابجد بتختانی مجهول کشیده وبدال بی‌نقطه | را نیز کوین د که در زیر حروف کلمات توسند
() چش: ۳ هنام... اندام است (1). جای این اغت در صفحةٌ ۲۳۷۵ است .
۹ - هند چگرخوارء زوجم ابو-فیان ومادر مماوبه. که چجگر حمزه عم پیفمبرس را که
درجنگه احد شهید شده بود جوید واورا عرب آكلة الاکباد خوانند . ۴ - ژاباکوید :
پهلوی «هندوپا» ازیونانی 601]0101 (کلمةٌ مسری) است. رل : 116 3۲ .26118007 ,8016
1 ,۷11 .۸10۲8601 5عل ۳۵۵6 «ژابا س۲ 4۵ . لوفر گوبد : هندبا شکل «عرب از
سریانی 8841 وآن ماأخون ازیونانی 81(008] و نام انواع بسیار از18100۳80665» است
ودر عقار مراد 6841۷6 (فر) است س 6501۷012 ۳10807100 و سپس 4۱۷2۳1621080 6۰
ودیگر 520۷286 66 07عزجا» (0۵]1116108[6 12۳352600) «عقار ۱۱4ف» «هندباء هی -
باليوتانية ااطویپا ... بقال له بالبربرية تبقاف و بمجمية الانداس شرالیه واسمه: بالعربية ید ,
وهوالشرقین > «عقار4 ۰*۱۱ ایتالیائی 1801۷18«تفی». کردیع 681000608 ۵ ژابا س۲ 10 .
۴ - ر4: هندیا. ۴ «هندوستان (ه.م.) - معرب « اندازه » «ژاباص
7 بیرون ی گوید : ««ندسه چیست؟ داستن اندازء ها وچندی يك از دیگر وخاسیت صورتها
وشکلها که اندر جسم موجود
====  463 printed 2380 ====

هندوان نها

همچو ابچد هوز < لی .4 هندوی پر - بسسنی هندوی پاررك
هندوان - نتم اول وثاك و واو بر بین است که کنایه از کوکب زحل باشد .

وزن همزبان , نام قلعهٌ بل است۹ #۰ هندوی چرخ - بسنی هندوی پیر

۹ ۳" است که کوکب زحل باشد .

هندو بار؟ » بکر اول و بای بالف سم 1
5 هندوی دریانشین - کنابه از
دشیده بروزن کیسودار » بمعنی هندوستان باشد قلم (۱) نوسندگی پاش .۱
- و کنایه‌از دوات سیاهی هم هست 3 ۹
هندویاژ دها نان ۰ هندوی سپهر « بسنی‌هندوی‌چرخ
وی‌از 3ها - کنایه از شمشیر | است که‌کنایه از کوکب زحل باشد .
تیغ هندی امت . ۰ ۰
دتیع هندوی گکنید گردان - من
هندوی باريك بن- کناب از | . ی بد گردان ۹
ی ۰ 7 هندوی سپهر است که کنایه ازستارة زحل‌باشد.
ک وکب زحل است . هندی؟۲ « معروق‌است که هندوستانی

(۳) چك. چش:- قلم ۰ سس

۹ - هندوان ( یکسر اول و ضم نوم ) جمع هندو (م ) - در پعلوی 1800568
« تاوادیا۹7 بهعنی هندوستان آمده: و درفارسی نیز بهمین معنی بکار رفته . رك : مجمل‌التواریخ
والقصص , مقدمه ص‌بط. ۴ - از: هندو ۳ بار ( پوند مکان ) لغة بممتی کشور هندوان,
هندوستان «دارمتشر . تتبعات چ۱ ۰۲۸۹ ۳ - از: هند (ه م.ای (نبت) ۰

2 هندوی - بکر ارل وم سوم بهلوی 1310001 (هندی) «اونوالا ۲۱۲», اهل هند
(مخصوصاً بمردم هندوستا ن که بان قدیم باقی‌هستند). جمع هندوان : «فضیلت علم دریوتان‌باقی
بود یا با ابرانیان وهندوان‌بود؛ ازبهرآنك بایست که بمسلمانان آید.» «کشف المحجوب‌سجستالی
م۹۵ - مجازاً زلف سیاه معشوق :
گر زدست زلف مه مشکینت خطائی رفت رفت ور ز هندوی شما بر ماجفائی رفت رفت .

حافظ شیرازی ص۰۵۷

‎٩‏ هندوانه - بکراولوض‌سوم وفتح ششم (
```


## [2026-09-07T19:31:37.808Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\nd={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nprint('==== 464 full ===='); print(d[464])\nprint('==== 465 ===='); print(d.get(465,'')[:900])\nEOF"
}
```


### [2026-09-07T19:31:39.017Z] TOOL RESULT

```
==== 464 full ====

نها هنکه
باشد ۱ - و کنایه از تیغ و شمشیر هندی «م ْ وکاف فارسی » چند معتی دارد : ۱ - سنگینی
هت؟ . 4 وتمکین ووقارباشد۴ . ۲- قصد واراده وآهنگه
هنگ؟ - بنتح اول و سکون ثانی | طرفی وجائیه ۰ ۳- غار وشکاف کوه باشد۹ +
۱- نیز هندی < هندوستانی را بزبان مردم هندوستان که زبانی است مرکب از
سانکریت و لهجه‌های هندی و فارسی وعربی» اطلاق کنند. ۰
۴ - ۶ وآن (عمعیر) چهارده گونه است : یکی بمانی » دوم هندی ... » * نوروژنامه
س ۳۹ > وهندی شمشیرست که آخن آنرا از هندوستان آورده و یا در هندوستان ساخته
باشندء, وآن را هندوانی ومپند وهند کی ( مأخون ازهندوك فارسی [پهلوی] ) نیز خوانده اند .
«تملیقات نوروز نامه ص۳۱۵*. ۴ - دریپلوی 8888 (قهم » معرفت) «اولوالا ۶۲۳۹ ۰ در
اوراق مانوی بپارتی 11888 [ء و۲۲ ( بممنی * بیزاری » تنفر ) (۲ ) ر4 :
.۳ و1 (176 ,8905 ...صهزوعهط ۸۸:41 ‎٩۶‏ اعنا ۸ ,116025128 آقای پورداود
نوشته‌اند: «هنکه درفارسی‌بممنی قصد ولیت گرفته شده.آهنکه با پیشاوند «1» درزمان ما رایج‌تر
است . ناگزیر هنگه ( ۳ آهنکه ) از پارسی باستان بما رسیده . اگر از زبان آن روز کلران
این‌واژه بجا مانده‌بود بایستی نپنکه 18888 باشد. اینکه حرف « تم > ازپارسی باستان واوستایی
درفارسی به «۸» تبدیل میکردد . نظایر بسیار دارد چون میتهر 82111272 ۳ مپر؛ چیتهر61110۳8
چهر و ماند اینها . دراوستا فعل تهنگه 10288 بمعنی کشیدن بسیار بکار رفته وازین مصدر
(ریشه) چندین واژه درفارسی‌یجا مانده» ازآنهاست: هنگه ( ۳ آهنکه), هنجیدن, با پیشاوند7۸»
آهنجیدن وهیأت دیگرآن هختن( ۳ «یختن)» با پیشاوند «۲» آهختن ( ۳ آهیختن)؛ با پیشاوند
«فر» فرهختن» باییشاوند * بر» برهیشتن . باپیشاوند «فرو» فروهخشن وجز ابنها . ازهمین پنیاد *
آختن با پیشاوند «1» بیار معمول است». «فاب ۰۴۸۹-۸۵۱ ۴ - ر4: ح۱ و صفحهبعد:
ای همه سبرت نو هنکه وثبات چکنم بی ثبات و بی هنگم.
آنوری آبیوردی.
8 - «هنگه... آهنگه بچیزی کردن» لفت فری ص۲۸۲ :
دلتانی را لفظ نو همی سازد ساز جان ربایی را تیخ توهمی‌داردهنکه.
: مختاری «فرهنگه فظام».
ر4 : ح۳. ‎٩‏ - این ممتی را از « هنگه افراسیاب » (ه.م.) استتباط کرده‌اند» ورك : دژ
آهنگه افراسیاب .
2 هنر - بشم اول‌وفتح دومء اوستا - 1101278 عظمت. استعداد, فابلیت, هندی‌باستان
- 508478 , ساسکربت 8080878 ( زیبا , قشنکه ) . پهلوی 3002۳ ۰ ارمق ع 888۳ ۰
اففانی وبلوچی 1311187۴ «اسشق ۱۱*۸ ورك : نیب رکه س*۱۱؛ کردی 1067 (فن» معرقت)
«ژابا س4۵۳ ؛ صنمت, معرفت امری توأُم با ظرافت و ریزه کاری : « آورده‌اند که ظرافت بمیار
کردن هنرندیمان است وعیب‌حکیمان» «کلتان ص۳۸ » - هنرهای زیبا , صنایم مستظرفه -
هنرمند - بشم اول وفتح دوم وچهارم» از: هنر(۸.م.) + مند (پسوند اتصاف)؛ پارسی
میاه 1۵۵۲2۷800 . رک : ۷فط۰»۸7 368۷۵۵۵ 31806 067 , ف۲عانظ ۷۷۰)
2710 «1954 ,]167 ,05:62 ؛ آنکه دارای هنراست : «کفت محال است اگر
هنرمندان بمیرند که بیهنران جای ایشان بگیرند .» «کل‌ان ص۲۰ .

==== 465 ====

هنگار نها
4 - وزن ومقدار هرچیز۱ . ه- زور وقدرت را ۱ صمغ درخت اشترغاراست که بزبان عربی حلثیت
کوبند؟۲ - بمعنی‌بسیار ووافر وفراوان باشد. | میگویند٩‏ .
پیا نگاهداختن و غمخواری کردن؟ . ۸- زبرك هتگار(۱)- بنتح اول بر وزن زنگار »
وعاقل۴ ودانایی وهثیاری‌باشد9 ۰ ‎-٩‏ قوم‌وقبیله بمعنی تندی وتیزی باشد*۹.
ولشکر وسپاه راکوبند" . *۱- ضرب و صدمه ۹۱۱۵
وآسیب وآزارباشد. ۱۱- دم آیی کهخور۷ - هنگارد۲(۱۱) - بکون را و دال
وبمعنی زکام وهوا زدکی‌هم بنظرآمده است ۸ | بی‌نقطه, بممثی هنگار(۱) امت که قندی وتیزی
وبکسراول, زحیر وپیچش شکم باشد- وبهندی | باشد » و بفتح را یمنی تندی وتیز ی کند. 8
(۱) چك, چش: هنکلر. (۲) چك. چش: هنکارد . :
۱ ظ*<سنکه (هم.) . ۲ -ظ #سنکه: « هنکه . زوربود. » «لفت فرص
۸۱
آزهنگه سپهدار وچنگه سوار امد دوال کمن پایدار
کست وبغاك اندرآمد سرش سواران گرفتند کرد اندرش.
فردوسی طوسی «فرهنکه نظام».

۴ - سروری بنقل از تحفه بمعنی نگهداشتن وتیمار بردن آورده و بیت منجيك ترمذی
(منقول درحاشيةٌ ۵) را بنام منوچهری
```


## [2026-09-07T19:31:51.992Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re,json\ntxt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',txt)\nd={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}\nm=json.load(open('BQT_v3_pagemap.json'))['map']\ninv={v:k for k,v in m.items()}\nfor n in (590,591,592):\n    print('==== pdf',n,'printed',inv.get(n,'?'),'====')\n    print((d.get(n) or 'MISSING')[:900])\nEOF"
}
```


### [2026-09-07T19:31:53.333Z] TOOL RESULT

```
==== pdf 590 printed 1793 ====

۱۷۹۳ گرزن
گرد ۷ - نم اول و سکون ‎gl‏ وزای کویند ۴ ؛ و ‎GEL‏ نازی هم بنظر آمده است.
نقطه دار , عمود گرم - بت اول وفتح ثالی و سکون

آحنین راکو ‎moe‏ ]| الت ومیم . برادراعانیاسفندیاراست واوبدکوبی
اسفندبار پیش کشتاسب کرد و کشتاسب اسفندبار
و چماق چوب را گرز

را بند فرنمود 6 .
‎Vols J‏ پفتح اول ‎hs‏ و رایع
بالف کشیده بروزن فلك‌سان » آسمان را گویند؛
وبفتح اول وسکون ثانی هم آمده است - وعرش
اعظم را نیز گفته اند که فلك الافلاك باشد ۷ .
گردن بر وزن ارزن ۰ تاج مرصعی
بوده کیاترا بیار بز رک وسنگین وآترا پربالای
تخت محاذی سر ابشان‌با زنجیرطلامیآ وبخته‌اند .
کویند درآن صد دانه مروارید ‎oy‏ هربك بقدر
با کنجشگی وآن بانوشیروان رسیده و عربان
‎LT‏ قنقل بروزن منقل کنتندی و قنفل کیله

° کمته‌اند - و ‎dns‏ هاون را نیز کوبند -
‎esl als’,‏ هت که آلت تناسل باشد.
گرردمن ۴ ‎gi‏ اول والی‌وسکون
زای نقطه‌دار ‎Goby‏ دال بی‌نقطه و کسر میم ونون
‎woah OL‏ وپازند بمعتی‌دشمن وغنیم‌باشد.
گرزدن ۷ پم اول وفتح انی‌ورابع
وسکون ‎
==== pdf 591 printed ? ====

گرزه
و پیمانه بز رکه را گونند ۱

‎OIF‏ © بنتح اول بروزن هرزه »لوعی
ازمار استء وبعض یکوبند ماری باشد سر بز رکه
و پر خط وخال وزهر او ‎asks‏ از مارهای ‎Kee‏
‏است وهیج ترباقی برزهر او مقاومت نکند ۴ -
ودر بعضی از ولایت دارالمرز ۴ موش راکرزء ۴
‎any‏ - و بضم اول. هم یمعنی اولوهم‌بمعنی
کرز باشدکه عربان‌عمود کویند ۵ .

‏گرد گاو پیکر ۷ » ‎oma‏
‏راگوبند چه آنرا بپیأت سر کاومیش از فولاد
ساخته ‎Woy‏ .

‏گر او چهر ۱ -بس یکره
‎Kash‏ است که کرز فربدون باشد .

‏گرز ق گاف سار ۷ - بممنیکرز: کاو
چهراست که عمود فربدون باشد.

‏گرد ة گاوسر ۱ - ‎WSS gn‏

‎. ‏چش : - وآنرا ... بودند‎ (A)

‎1۷۹4 -

‏سار است ‎IFT‏ فربدون باشد .

‏گرذخ او میش ۱ - بسن ی کرزه
کاوسراست که گرز فربدون باشد ‎a LT,‏
سر کاومیش از فولاد ساخته بودند ‎AN)‏

‏گرزیدن ۷ - بن اول و فتح ‎BE‏
‏بروزن ستجیدن » بعمتی گرزدن باشد که چاره
وعلاح کردن ‎col‏ ۰

‏گردلن ‎a‏ بکراول بروزن‌مسکین:
تاج کیانیرا گوبند و آنرا مرصع ساخته از بالای
تخت محازی‌سرایشان باز
==== pdf 592 printed 1797 ====

۱۷۹7

گرست « بفتح اول و ابی و سکون
ثالث و ‎sigh‏ بمعنی سیاه همست باشد وبعریی
طافع گویند ۱ - و بزبان علمی هند فرو بردن
لقمه و امثال ‎OT‏ باشد و عربان ‎ab‏ خوانند.

گرسقن ۴ - بکر اول وانی :مخف
کربستن است که کربه کردن باشد .

گر ستودن ۴ بفتح‌اول وئالی‌بروزن
تیغرودن » بمعنی ‎OS‏ است وآن ترازو مانندی
است که بستها و تنگهای ‎gh‏ را بدان سنجند .

گرستون ۴ © بفتح اول وئالی بروزن
شف ق کون + بمعت ی گرستودن است که ‎methods‏
‏وبه‌عنی کیل ‎Ulan‏ بزر که همآمده است‌ومعرب

گرسنه چشم - بت ول تا ناه
از ‎Ste‏ و ممسك ‎ath‏ - و مردم ‎ad‏ وکدا را
‎e‏ میگویند ۵ - وکنابه از مردمی‌هم هست که
از قحط وغلا برآمده پاشتد .

گرسنه چشمان کنعان - کنایه
از برادران ‎Gey‏ علیه‌اللام است .

گرسیان - با بای ونون وحرکت
غیرمملوم « نوعی‌ازسنگه باشد ‎OT;‏ درهتدوستان
‎re‏ میرسد ودر صثمت کیمیا ‎ale‏ 1

‎Sg F‏ = بتادرستا مود
بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
کاف تازی هم بنظ رآمده است .

‏آن قرسطون ‎Fath‏

‏گر شاسب ۲ = با
```


## [2026-09-07T19:32:22.211Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS nayrig ===\"; grep -n -i \"nayrig\\|nāyrig\\|nairig\\|nāirig\\|nayrīg\" SNS_pages.txt SNS.txt | head -20; echo \"=== PHD ===\"; grep -n -i \"nērōg\\|nerog\\|nārīg\\|narig\\|hunar\\|nāyrīg\" PHD.txt | head -30"
}
```


### [2026-09-07T19:32:22.278Z] TOOL RESULT

```
=== SNS nayrig ===
=== PHD ===
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
500:narig [n(y)lyk'] woman, lady, wife.
692:ability čāraggarīb, hunar, šāyendag- ih, tuwānīgih; extent of ones — tuwān-sāmān.
3682:skill abzar, hunar, hunarāwandīh, kārāgāhih, kirrēgih, nēzūmānīh.
3683:skilled ` abzarómand, frahixtag, hunarāwand, hunarómand, kār- āgāh, kirrēg.
4229:virtue hunar, hunarāwandīh, hu- waršt, kirbag, nék-góhrih.
4230:virtuous даһа, hunarāwand, kir- bagig, nék-gohr.
4310:width pahnāy, wéhmih. wife narig, zan; Cagar. wild kófig.
4334:woman nārīg, тап; married ~ šūy- mand; young ~ ziyanag.
5212:wigrad wigridan nerang n��rógómand nerog nilopal nirmadomand nirmad ncm, wem wūmār wēmārīh nēmasp wimand wimandómand wimandig wimustan nemag ncmroz ncmtan niság wisbed
5268:wārānīg 445 aA V waran ' У» ` narig `
5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
```


## [2026-09-07T19:32:22.846Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ idris ===\"; grep -n -i \"idrīs\\|idris\" FVQ_pages.txt | head -20; echo \"=== FVQ iskandar ===\"; grep -n -i \"iskandar\\|Alexander\" FVQ_pages.txt | head -10"
}
```


### [2026-09-07T19:32:22.906Z] TOOL RESULT

```
=== FVQ idris ===
2223:5 Ho seems to base this on the occurrence of the name Abu Idris, but see Horovitz,
7108:Abraham, and Idris are called ^ *X^ } and the Virgin Mary <a^*X^ in
=== FVQ iskandar ===
2257:ZA, xxiv, 315, however, recognized this Andreas as the famous cook of Alexander
10353:Both passages are reflections of Syriac legends concerning Alexander
10371:the Syriac Alexander legend ..0,1 is generally spelled yt^vjlL 2 which is
```


## [2026-09-07T19:32:31.709Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2190,2275p' FVQ_pages.txt"
}
```


### [2026-09-07T19:32:31.755Z] TOOL RESULT

```
was a tradition that the word came from Syriac. 2 The name occurs
in the Safaite inscriptions (Horovitz, KU, 85), and was known to
the poet 'Adi b. Zaid, so it was doubtless familiar, along with the
creation story, to Muhammad's contemporaries.
^, ol (tdritt)
Ls-Z *
xix, 57 ; xxi, 85.
Idrls,
He is one of the Prophets casually mentioned in the QurVtn,
where all the information we have about him is (i) that he was a man
of truth (xix, 57) ; (ii) that God raised him to a kt place on high '*
ULjp l>Lx^ aLi*3 j (xix, 58) ; and (iii) that being steadfast and
* " *
patient he entered God's mercy (xxi, 85).
The Muslim authorities are agreed that he is *7-j\>-\, i.e. ^130,
the Biblical Knoch, 3 a theory derived not only from the facts
enumerated above, but from the idea that his nanio <j*^ j^ I is derived
from <^J^ to study both Jewish and Christian legend attributing
to Enoch the mastery of occult wisdom. 4 The fallacy of this derivation
was, however, pointed out by some of the philologers, as Zam. on
xix, 57, shows, and that the name was of foreign origin was recognized
by al-Jawallqi, Mu'armb, 8 ; Qdtnus, i, 215 ; which makes it the more
strange that some Western scholars such as Sprenger, Lvben, ii, 33G, 5
and Eickmann, Awgdologie, 26, have considered it to be a pure Arabic
word.
1 Ibn Qutaiba, Ma'arif, 180 (Kg. cd.) notes a variant reading ^|Jb| which may
represent a Jewish pronunciation.
2 Sycz, Eigennamen, 18.
<l Tha'labI, Qisa*, 34.
4 "[3H of course means to instruct, to initiate (of. viL-) and may have suggested
the connection with ^jj. For the derivation see Tha'labI, loo. cit. ; Ibn Qutaiba,
Ma'arif, 8. Finkel, MW f xxii, 181, derives it from i5So>peaxo?, the 7th antediluvian
King of Berossus, but this is very far-fetched.
5 Ho seems to base this on the occurrence of the name Abu Idris, but see Horovitz,
KU 9 88.52 FOREIGN VOCABULARY OF THE QUR'AN
Noldeke has pointed out, ZA, xvii, 83, that we have no evidence
that Jews or Christians ever called Enoch by any name derived from
or **ij, and though Geiger, 105, 106, thinks the equivalence of
IxU I'lSL* *li*ijj of xix, 58, with the n.triQr)Ktv avrov o Qeoy
of Heb. xi, 5, from the Midrash, sufficient to justify the identification,
we may well doubt it. Casanova, JA, 1924, vol. ccv, p. 358 (so Torrey,
Foundation, 72) suggested that the reference was to *E<r5/>a9 which
through a form *Epay became ^j^'. Albright 1 imagines that
it refers to Hermes-Poemandres, the name being derived from the
final element in the Greek name Yloi/jidv8pr)$ } while Montgomery,
JQR, xxv, 261, would derive it from Atrahasis, the Babylonian Noah,
None of these suggestions, however, comes as near as that put forward
by Noldeke in ZA, xvii, 84, that it is the Arabic form of 'AyS/>eW
filtered through a Syriac medium. 2 In Syriac we find various forms of
the name *fio11>,jl : ^cooli^l : -CD^yl and tf&j&rJl, this latter
being the form in Christian-Palestinian, and from this by the coalescing
of the n and d we get the Ar. ^^ '. Grirame, ZA, xxvi, 164, suggested
a S. Arabian origin but there is no trace of the name in the inscriptions
and the Eth. htf'Cftl has nothing in its favour.
! (Arffik)
xviii, 30 ; xxxvi, 56 ; Ixxvi, 13 ; Ixxxiii, 23, 35.
A-^ 1
** ^^ I
Couches. Plu. of 4.Ajjl.
We find the word only in passages descriptive of Paradise. The
Muslim authorities as a rule take it as an Arabic word derived from
^j 1 but their theories of its derivation are not very helpful, as may be
seen from Raghib, Mufradat, 14, or the Lexicons LA, xii, 269 ; TA, vii,
1 Journal oj Palestine, Oriental Society, ii, 197-8, and in AJSL. 1927, p. 235 n.
* Noldeke's earlier suggestion in ZDMG, xii, 706, was that it might stand for
8cd$o>poff, but in ZA, xvii, he refers it to the Upd^ts 'AvSpcov and thinks the lifting
him " to a place on high " may refer to the saint's crucifixion. R. Hartmann, in
ZA, xxiv, 315, however, recognized this Andreas as the famous cook of Alexander
the Great.FOREIGN VOCABULARY OF THE QUR/AN 03
100. Some early philologers concluded thatit was foreign, andas-Suyuti,
Itq, 318, says that Ibn al-Jawzi gave it as an Abyssinian loan-word, and
on p. 310 has the interesting statement " Abu 'Ubaid related that
Al-Hasan said We used not to know the meaning of <~lHj j( 1 until
we met a man from Yemen who told us that among them an jjyjl was
a pavilioh containing a bed/'
Addai Sher, 9, says that it is the Pers. ^Uijjl, by which he
probably means <_XJj^i throne the colloquial form for AJjjl (Vullers,
Lex, i, 141), but there does not seem to be anything in this. There is
nothing in Eth. with which we can relate it, and the probabilities are
that it is of Iranian origin, especially as we find it used in the verses of
the old poets, e.g. al-A'sha, who were in contact with Iranian culture
(cf. Horovitz, Parodies, 15).
Ajl (Irani)
Ixxxix, 6.
Iram : the city of the people of 'Ad.
The number of variant readings for this *j] in 2\<Jl C>b *jl
```


## [2026-09-07T19:32:59.208Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT nairyava ===\"; grep -n \"nairyava\\|nairyav\" BRT.txt | head; echo \"=== BRT nairyo.manah ===\"; grep -n -i \"nairyō\\.manah\\|nairyo\\.manah\\|nairimanah\\|Nairimanah\" BRT.txt | head; echo \"=== BRT hunara ===\"; grep -n \"hunara\" BRT.txt | head; echo \"=== BRT nāirī ===\"; grep -n \"nāirī\\|nairika\\|nāirika\" BRT.txt | head"
}
```


### [2026-09-07T19:32:59.296Z] TOOL RESULT

```
=== BRT nairyava ===
=== BRT nairyo.manah ===
=== BRT hunara ===
6346:•  ].  aäahunara-  Adj,  'des  Können  (usw.) gross  ist,  vielvermögend':  ««'är?* Yt  10.  25.
7035:yeü,  ß)  vorausgehendem  yen  'Svenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyastis  hala *nmä>tat  . .  a°  yat  he  aoxte  .  .  dka  *hä *x!ayae  .  .  haxtöit{%A.)  N.A'f.;  V.7.3 äat  (s.  ?•)  yg  .  .  upairi  hunarain  (sd.)  maiiü barst  .  .  J'  yaj  .  .  faiti  barät  aat  (s.  z) yat  .  .  ava  baraite  "wer  .  .  aber  wenn  er .  .    und    wenn    er    .  ."    P.^jjf.;    —  yezi
14059:•  j.  draxtö.hunara-  Adj.  'der  gelernte Fertigkeiten  besitzt,  Kunststücke  kann' vom  Luxushund'*:  iünqm  .  .  'narattam V.  IJ.&;  —  *ui  *täät  Spina  patfnti  pasus.- Aaurvam äi  (sd.)  ..  "naranamia  V.  jy.  42.
16818:hinzubringen  zu  — ,  an  —  hin'  (Akk,)i haoma  .  ,  ya  nasäum  ava.b?r»ta  Y.6. 42 '"'.  5)  'wegtragen,  wegbringen':  ava aS?m  iristfm  baraym  V.8.2;  3.  Un- deutlich P.jA';  s.  unter  hunara-.
18454:•  j.,  g.  nae-kay-  neg.  Pron.  interrog.  'non quisquam',  nur  substantivisch  'nemo;  nihil': %waAy3  xratsus  ylm  'Si  dabayäti  (sd.) y.43i>\  —  y3m  vä  '''üs  dänst  iil  (sd.) Y.  43-  13;  —  *frasafntlmca  .  .  yeäha pourBsta  htyjayan  'cisca  aiii/ia  yäsaili zyänäi  (sd.)  Y.  05.  1 1 ;  —  yahmat  haca °eii  bunjayai  .  .  nSit  ^usyqs  i^A^  tacö  .  . Aog.jSB.;  —  yaf  mqm  'a/  taurvaySi nsil  dafuö  nai^a  .  .  Yt  /.  6.  a)  mit Gen.  pari.:  'iil  a^arftiiam  tva  rait  .  . asayqm  (sd.)  nsit  .  .  V.^.iy,  —  yS  'Sm isaiti  hunaranqm  V.  jj.  19;  —  a^qm alnauhqm  'clt  vJdvh  aojöi  (sd.)  Y.  32. 7.  na^im,  naiHs  als  Neg.  sbes.;  vgl. auch  na^üxit  mit  No.
20876:35ra.)  ..cikayatö'F.^c;  —  mitGen.part.: yasca  altailqm  viazdayasnanqm  .  .  nötl *vTsaile  framrüite  aitqm  a  .  .  jasatti  Y. <y.4;N.6j; — *pouru.nar?m  tum  ktnnBsi . .  yas?  tl  . .  iaxsaite  ", .  (eum)  facis qui  . ."  Y.  10. 13;  —  n^armS  .  .  yat  upa- nhacaiii  yS  avatä^  fraxsayeite  ".  .  quod sequitur  (eum)  qui  . ."  Yt/9. 66; —  Cßw ..  nmän^m  da^äM  b>rnimit?m  yas?  %wä .  .  yazaite  ".  .  domum  (eius)  qui  .  ."  Yt. 70,30;  —  Aa  yaoidä  yS  Avqm  anhvqm yaozdäite  ".  .  puriücatio  (eius)  qui  .  .**  V, Y,  ö's.  10;  —  paoiflm  aitassqm ^adknanqm  . .  yS  narym  afavantm  .  . \  kasyanhe  (sd.)  satthäi  da%aiH  "die  erste dieser  Taten  . .  ist  (die  dessen,  der . .  sva.) wenn  man  . ."  V.  75.  a;  3,  5,  7,  8; —  kva i  asti  spa  vohunazgs  (sd.)  däityB^ätuli  . . \yj  naicim  isaiü  hunaranqm  "ubi  est  canis ',  .  aptus?  . .  (apud  cum)  qui  .  .  "  V,  7_j. !  19;  17,  18;  —  aheca  ank^uf  .  .  yasta asti  manahyS  "et  huius  vitae  et  (illius) quae  est . ."  Y. 57.  25;  —  cvathya  *nä  nitt- malibya  hävanailbya  (sd.)  *ratufrisl  *yä (NDm.) . .  '^hÜj^istö  (sd.)  N.  io8\  —  ^a- rata  ..  *ysi.dim  hauhäna  (sd.)  ,  .  "editc  . . (is)  qui  (vestrum)  . .  meritus  est . ."  Y.  8. 2;  —  ya  (NDm.)  ffä^a  ..  *sravayalS  Ma 'ratu/rya  N.  2^;  24; — *kaya  h?nH  mas- yanhs  ai'ja  (sd.)?  *yifi3'*  *aparaya  paiti mastrr^naya  ".  .  (ü)  qui  (sunt)  .  ."  F._jc; *ja3'>;  —  vtspe  mainyava  dama  yai- (NPm.ya  varpnya  ".  .  invisibiles  . .  et  (ii) qui  (sunt)  .  ."  Yt.  70.68;  FrW.  1.2;  — vlspe  kaoma  yatcit  (sd.)  ..yaectt  qzahu dfrttAnAs  .  .  *upa  *d»rfzähu  (sd.)  Y,  70. 17;  —  kä  an-a  as'if.staiti/ (sd.)  ^,!(NSf:) dasa  anyaSsqm  asS.stBitinqm  .  .  an/aiti "quae  sola  ..  precatio  (ea  est)  quae  ,  .?" H.2. 6;  —  AvuHtS  vä  ySUlS  (vä)  yim (ASm.)  vä  ainim  ..layqn  "maximus  (natu) seu    (is)    quem    alium   .  .
26822:paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa  va  na  va  iri^yai  V.Ä  4; '>  5-  39;  —  y^  asiim  upanhanzaiii  sBnS va  para.irittahe  maryehe  vä  y.6.  10;  12, 7.23; —  *näirikayä  hhrpa  ..sunü  kihrpa N.jp;  —  pasvamca  slaoranqmca  masya- nqmca  saiiamla  vayqmca  V.  2.  8; — pasca . .  nasäum  ava.kar>i>nti  spstum  vä  raoz»m va  v>hrk3m  va  V,  5.  5;  6.50;  —  yahöit dim  . .  avaxanan  süns  (NP.)  va  hnß.- ifardvayB  va  V.ö.^s;  46,7.29,  30;  — j/J vä..vay5vä  hn/sji^aroFr'W.li.  A)  mit Bezeichnung  der  besonderen  Art:  spä pasusJtaurvS^''  .  .  spä  vU.kaurvS''''  .  .  spa vohuna^B^^ ..spa  taurunö'''^..spa  sukurmd*''> . .  spa  jaiui^^ . .  spa  aiwinu/'''' . .  spa  vltus''^ ..spa  urupis"'^'  V.  5,  29-33;  —  späntm slidnm  urvUarsm  yim  vat»hapar>m^^  V. 13.3;  —  ys  aSa^qm  sünam  Jainti  yim pa^us.kaurvqmca  viLhaurvqmca  vohuna- sgqtnea  draxtS.hunaranqmia^^  V.  13. 8,  42 ;
29136:Pü.;  apäk  Kkt{ai). j.  haia.ztm%rd.iaräi  Yt.  5.  I9:  lies  haia  t'. ■  j,  haSa.hunara-  Adj.  'geschickt':  narfm ..  mqzdnm  'rtm  lanu.mqhr^m  V.  it?.  51; —  mazdrö  'rS  ianu.makrS  Yt.  j.  91.
30379:den"  Vr.  16.  o;  —  akunavaitlm  gä^am  . .  |  .  g.  hunaratät-  f.  'Inbegriff  des  Könnens,
30399:•  j-,  g.  hunara-  m.  i)  -Können,  Kunst':'     «"""°>'  «""  »"dstda;  s.  No.  i. kyal     da     ^yaohana     mlidavqn    (sd.)    .  .  •  j.  huovana-  Adj.,  PPM.:  s.  'Aai-. %wä   'ra   ".  .  durch   dein   Können"   Y.  ,  j.  hunvant-  Adj.  (fem.  'vaintt-),  PPA.: 4^.5".         a)  'Kunstfertigkeit,  Geschick- js,  'hav.
=== BRT nāirī ===
3391:^parayät  nairika  v3  nmänO.paitiS  vä  N.j;
3665:—  y!^  anyake  nairika  . .  yS  anyahe  *°ha (IS.)^  ..  a'^aurutum  *pararikacaiii  (sd.) N.  7;  77;  —  yat  he  aoxte  aisa  yeiihe  'ks hacatsuha  ms  *ana  "ka  (VS.)  N.5;  7,  *y, *io,  10 ;  —  'ktm  iiahmB.kßrpl)m  *syaokn3m.- v>r}Nm  (sd.)  V.7J.23;  ¥.2^.27.
8383:yai  . .  nairika  -rim  jasäl  "wenn  eine  Frau in  die  Schwangerschaft  kommt"  V.  5. 45.
8983:•  ].,  g.  ka'tära-  Adj.  'wer,  welcher  von beiden?',  nur  substantivisch;!)  als  eigent- liches Fragewort,  an  der  Spitze  des Satzes  'uter':  'rS  2/(sd.)  aya  v^krkaya (Gen.  part.)  ja^ivöJarö  ai//un  . .  ya^a sp.t  v>hrkahe  k-'r^naotti  yaia  yat  v)hrkö spä  V.  75,41  ■>;  —  sonst  mit  folg.  vä  .  . vä:  -riJ  a'iaurunpm  *  parayät  nairika  jvi nniilnS.pai/is  vä  "wer  (von  den  beiden) soll  auf  Priesterdienst  aus(dera  Haus)gehen, die  Frau  oder  der  Hausherr?"  N.  5;  — 'rim    ä   angrö  (sd.)  vä  hrS  vä  angrö   Y.
11948:—  yaiia  hl  hqm  ta/nS  Jasat  avi  'nuye zsi^uyt  \.y.^a■,  —  vohu  manö  paiti.- ral%waya/i  haifa  avaahat  'nvatyat  daivö.- jatayä  V.ig.io;  — yS  nairikayi  ä^ra- vaiiya  ..  'nüm  iri^yat  'W.i6.ii\;  —  iata MH  (sd.)  *paitisama  frya  paüi  -nvi-  Yt ij.  10;  —  fra  'nvo  rmjayeiti  (näml. pannäi)  Vr.7.3;  —  Mihr^m  ..ya'ha  'nüm raocayäti  ya%a  mJwÄö  Yt.ro.  14a; — paity- aoggt  (sd.)  ta  ahmai  jassit  .  .  'nv>m  ä Y.46.B;  —  ya//ij  'nüm  apayäti  (näml. ariUs)  Yt.  /0. 2 1 ;  —  ahunam  vatrlm  'nüm paiti  sva.  ". '.  gewährt  persönlichen  Schutz" Y.ii.y,  —  yS  ..  'nuye  isaite  'hra%nm ". .  Schutz  lUr  seine  Person.."  V. y.19;
18689:—  yal  ba  paiti  nars  asaonS  ..  nairika^a apirmäyUkasca  varaihim(ßd.)pantqm  asBil V.J.  11;  —  ^rigaim  haca  ninbyS  asa- vaby}  V.  l6'.4;  3. 16,  17,  77.4;  —  frava- sayB(id.)  jvanq/n  narqm  aiaonqm  aojyehlt .  ,  ya%a  iristanqm  YX.13.1T;  Y.4.5;  — avanhe  narqm    asaonqm  Yi.g.2,  13.10,
21228:jAw.:  i)  mit  Ind.:  ^°  aiAlA  amS  mkanie spanasia  irista  . .  ka  hl  asti  aha  V.3.  36; iX  36,  37,  12.  i;  —  y  .  .  caratd  dva  mS apajw>tayaaa  V.y.49;  —  hs para  mintS daSvS  .  ■  y  maiys  maitm  xhtdra  avi franhirftaiti  y  vä  mafys  .  .  xsudranqm *pairi,gmrvayäti  V.  Ä32;  —  hs  ba  .  . arhtqm  MtyS  y  na  paurva  frabda  (Sp. 984  o) /rabdsJrajB  framalxaiti  V.  j8.  40; 34,  46,  54;  —  y  aoxte  aiia  . .  a%a  *ha *x/ayete..  haxäsit (sd.)  ü.g;  7;  — y  hakat *amrute  . .  aliü  *ratu/rii y5 . .  N.24;  — ta^a  y  paiti.barvnti  yä  .  .  äjayaurra N,54;  —  yl>  sSne  piÜr^m  jainti  . . yas»*'^ tat . .  täyus  . .  para.baraiti  dasa  (sd.)  oSj/ päili  afsl  aiayai(sd.)  Y.  13. 10;  —  aät y  bavaiti  avijpastS  sasta  .  .  ta  hascit upajbayäte  Yl  13.  69;  46;  —  yO  nars snaHmt  usihiltaiti  a^at  hl  ag^r^ptam  (sd.) y  frasusaiti  altai  hl  avaoirist»m  {sd.)  y . . Y.4.1T,  —  al^  zr  narS  paityeinti  (sd.) *aslS.vitotus  pgsanaiti  yasla'>''  isui..p»ia- naiti yasca^..Y .4.^^^^; — h^m  ita  (s.Ntr.) tltao^ra  bavairiti  (Sp.  939  O.)  yasj*^  tava frabannte  drvantö  . .  ".  .  dann  .  .  wenn (sie)  dir  darbringen  . ."  Yt.5. 94,  2)  mit Konj.  (oder  Inj.);  y  .  .  masdayasna  .  . nassum  frajasqn  ku%a  . .  v^myqn  "ange- nommen den  Fall:  die  M.  stossen  aul einen  Leichnam  .  .,  wie  .  .?"  V.  6. 36: 5.45,  Äi,  4,  J&i;  —  y  •■  spä  avaca va  bavat , ,  kuha  . .  vjrxyqn  . .  masdqyasna V.  13.  39;  35;  — y  . .  masdayasna  bal^atai (sd.)  fravasänte  katärö  paurvB  ämayänie (sd.)  V.  7. 36;  —  y  iavani  (sd.)  aiwi.- sasls  . .  eis  aiAhe  asti  balfazd  Yt  J4.34; —  y  afvS  zaata  (sd.)  frayatäiti .,  zaoiars gatava  N,  tf/;  70;  —  y  ahmt  nmlne  . . nairika  daxstavaiti  arthal  y  vä  ..  *aipi.- irytS.gatus  isd.)  altala  .  .  V.5.  59;  — y pouruiaist^a  hanjasänte . .  t^m  i^ra  ha*- Jasante  V,  7,44;  YL//.6;  —  yas/a^>  .  . väcim  paiti  taBtii' {sd.)  ar?hat  nsil.. täyus .  .  para.baraiti  Y.J3.40;  —  y  ma^äia frayazantt  .  .  rüsit  t^ra  airyä  daiähävS /ras  hyätYt.i4.^&;  — y paoirim . . itryntäl .  .y ' . ,  ktrmtät'  ava  hö  miryaite  anämStS ZT  ais6  Y.y.^T,  —  nthenyesi:  yeti/a  alte asti  . .  gar>mBkva  (sd.)  vjiänte  y  vä  aiU gar^ma  (sd.)  i^ars^a  stamaruM  .  .  apa.- daiai  .  .  aiühai   haca  .  .  bavainti  p»sB.-
21784:fratara  (sd.)  hala  nmäna  vsnzyan  yat  vä nalmim  ..y°n'  nairika  ätnm  aiwi.vatnät (sd.)  W.lö.a;  a;  —  ailala  .  .  irishm  ni- dartsayift ..  y  n°  sunt!  . .  aetanham  astam avi  apqmca  .  .  barp7ti»m  (Sp.  944  o.)  fra-
22391:mit  upa  'zuführen,  zur  Ehe  geben';  upa va  nairikam  vaöayaSa  "(so)  möge  man (ihnen)  eine  Frau  zur  Ehe  geben"  V.4.44; —  jfanAa  vä  duyöa  vä  , ,  *näiri^watiai
23013:viratyst  YL  75.  40;  — -  pu^nm  anyakmat arsänai  varst?m  YL77.S8.  3)  'Jeman- dem (Dat)  etwas  erwirken,  durch  seme Tätigkeit  verschaffen';  tai  tts  nülXi  van^äni "ihn  (den  Anteil)  will  ich  jetzt  uns  ver- schaffen" Y.  57,  i">.  Undeutlich:  ya nairika  nmanspaiti  v>r>tyanti  N.  6;  — nSii  hi  alt  *^adinanqm  vfr»tySit  N.  16.
```


## [2026-09-07T19:32:59.820Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10340,10380p' FVQ_pages.txt"
}
```


### [2026-09-07T19:32:59.862Z] TOOL RESULT

```
came to mean judge or magistrate. 1 This word, of course, is good Iranian,
being from the Av. .ujj^j/? vicira meaning deciding,* which was
borrowed into Arm. as *t&bn-? and is related to the form behind the
Mod. Pers. j>-$ or ^>-J judge*', J^J or prefect* and jjjj, which is
generally regarded as a loan-word from Arabic but which Bartholomae,
AIW, 1438, rightly takes as a genuine derivative from the older
Iranian word.
The borrowing was doubtless direct from the Middle Persian, for the
Syr. }^1O seems to be late and a borrowing from Arabic (PSm, 1061).
> > i ^ ^ > > i .-
tr J>\-A } r j>\-s (Ycijuj wa Mdjuj).
xviii, 93 ; xxi, 96.
Gog and Magog.
Both passages are reflections of Syriac legends concerning Alexander
the Great.
< It was recognized very commonly that the names were non- Arabic
(cf. ai-Jawaliqi, Mtfarrab, 140, 156 ; al-KhafajI, 215 ; LA, iii, 28), and
* there was some doubt as to whether they should be read with Hamza
or without.
The names were apparently well known in pre-Islamic Arabia,
and we find references to them in the early poetry, where the statements
about them would indicate that knowledge of them came to Arabia
1 West, Glossary, 237. It was a fairly common word, and enters into a number
of compounds ; cf. Nyberg, Qlossar, 242.
2 Bartholomae, AIW, 1438 ; Reichelt, Awestisches Elementarbuch, 490.
3 Hiibschmann, Arm. Gramm, i, 248 ; Spiegel, Huzvaresh Grammatik, Wien, 1856,
p. 188.
* Vullers,Zes,ii, 1411.
6 Vullers, Lex, ii, 1000 ; Horn, Qrundriss, 242 ; Hubschmann, Pers. Studien, 94.FOREIGN VOCABULARY OP THE QTJR S AN 289
from Christian eschatological writings. 1 The names, of course, were
originally Heb. 313 and 3130, which in Syr. are ..CU and yt ^^ - I n
the Syriac Alexander legend ..0,1 is generally spelled yt^vjlL 2 which is
a variant reading of the word in the Qur'an (Noldeke, Qorans, 270).
The Mandaean demons Hag and Mag, which Horovitz, 7P2V,163, quotes,
are more likely to be derived from the Qur'an than the Qur'anic
names from them. 3
(Ydqul).
Iv, 58.
Ruby.
It was very generally recognized as a loan-word from Persian. 4
Some Western scholars such as Freytag 5 have accepted this at face
```


## [2026-09-07T19:33:09.192Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"g\\.  nar-\\|g\\. nar-\\|nairya-\\|näirI-\\|nāirī-\\|nairi-\" BRT.txt | head -20; echo \"=== search Mann/nairya ===\"; grep -n \"nairya\" BRT.txt | head"
}
```


### [2026-09-07T19:33:09.255Z] TOOL RESULT

```
4472:ASm.  (n.)  aus  ainya-.  —  Vgl.  zu  mairi«,.  - Pü,:  an.  —  »  Die  von  DsT.  ZA.  a,  Z4[  ge- billigte Fassung  des  Dk.  S.  44-  6S  "st  mit  dem Wortlaut  {urvatqm  aimm !)  nicht  zu  vereinigen ; s.  •nairya-  No.  3.
16384:•  j.  pipivah-  Adj.,  nur  fem.  pipyßst-  'die Milch  in  der  Brust  hat,  säugt':  yS  nairi- kam  yqm  apu^rqm  °pyBsim  va  apipyästm va  anasaxtqm  (sd.)  para  xludra  avi fra^hiTszaiti  ". .  eine  Frau  . .  gleichviel  ob
18671:•  '};  g.  nar-  :  lur-  m.  'Mann';  1)"  'Mann' als  der  erwachsene  (,  geschlechtsreife) männliche  Mensch;  i)  im  Gegensatz  zu Weib  und  Kind;  uzw.  zu  a)  g3n3-:  yJ  vs mäi  nS  giita  vä  .  .  ääjiäj . .  yä  .  .  Y.  4^. 10.  b)  jSnay:  i^ä  T  Aai^yJ  (sd.) «  a  rö(  VP.)  a%a  jSnayS  Y.5J.  6.  c)  natrT- : ^rtäJ  . .  uia  na  Vä  nain  va  vaedä  hat- %-lm  H.3S-  6;  Yt.  II.  i,;— huxla%ras{^A.)ta nS  na   vä  nain  vä  xsaitä  Y.41.2;
18717:Slfttl  *nairya-m'  geschr.;  S  2ÖÄ  3*.  —  Vgl. ai.  H^mänas-  Adj.  —  Pü. :  mart  minisn,  erL : tus  dl!  pa  gas  däsl.
18729:•  j.  nairya-  Adj.  (fem.  'ryä-)  'virilis'; i)  'männlichen  Geschlechts';  a)  von  Men- schen; dva  nara  us.eayeirtie  mHwana (sd.)  strica  'ryasca  V.  2.  41 ;  —  yezi  °ryS afihat  ..yezi  strJ  atshat  V.S.  $S;  —  däya ml  .  .  'ryqm  3snqm  */razaintlm  \.6S.$;
22162:•  '].  vaesa-  m.  'Knecht',  der  im  Herrenhof seine  feste,  dauernde  Wohnung  hat'*:  a%ra- varam..nman5.pailTm..nmanspaitTm  nairi- kqm..  'sJs/a  ^pairyaarSusca yaozda%d gSuI
24593:•  j.  viä-  n.  'Gift,  Giftsafi':  asTm  .  .  yim upairi  *vii'^  *raohat  är!!tyl.bam»m  nairi- hm  ". .  auf  dem  das  grünliche  Gift  klafler- hoch  floss"  Y.o.  11;  Yt/p.40.
30001:I  •  j.  ham.varatay-,  ham-varetay-**  f, •Wehrhaftigkeit,  Tapfeikeit",  stets  mit nairya-    Adj.    verbunden:     däyä    mt  .  .
=== search Mann/nairya ===
4472:ASm.  (n.)  aus  ainya-.  —  Vgl.  zu  mairi«,.  - Pü,:  an.  —  »  Die  von  DsT.  ZA.  a,  Z4[  ge- billigte Fassung  des  Dk.  S.  44-  6S  "st  mit  dem Wortlaut  {urvatqm  aimm !)  nicht  zu  vereinigen ; s.  •nairya-  No.  3.
7206:•  j.  ax'afnya-  Adj.  (fem.  yä-)  'schlaflos, immer  wach':  nairyam  ham-ianitlm  . . °yqm  \.(>J.$.
7501:•  j.  'ä-sna-  Adj.  (fem.  °»<i-)  'erfolgreich, wirksam,  tüchtig':  'naca  (APn.)  viana asäunam  'nafa  manä  sae^antqm  Vr.  J/.3; —  °K.7  (APn.)  . .  mata  Yt  13. 74.  a)  bes. von  frasanfay-  f.'*:  ifä%ravaiH  'na  fra- ttitntifY.tio.-j; — nairyam  '»am  *frazain- am  Y.öS.s;  62.S,  GS.'i-i,  Yt./o.3,  108, 110,    ;Ä5;    —    'naySs^a  paili    vanhuya
7679:•  j.aradwö.zvnga-,  *«radvö.zflnga-'*  Adj. (fem.  'gä-)  'mit  aufgerichtetem  Knöchel' sva.  '(immer)  auf  den  Füssen,  Beinen'": mi'ir»m  ..  'g^m  2amaahunt9m  Yt/o.6i; —  nairyam  kqm.varjÜJm  'gqm  a:^afnyqm Y.  62.  5 ; '  —  any3  *'g3  V.  5.9  PüZ.
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
10043:(Dat):  anairyanqm  tat  dahyutiqm  v?r3- "i'fäi  uzjasaiii  H.^S.
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai  (sd.)  V.  2. 24;  —  hixrsm  .  .  ast^m  .  .'P.4j;  — asavamm  . .  ajyei^yai  mraomt..; aaÄai^Tm  .  .;  ta  (APa)  hdhra  frafrS-^  tat  zl  vatiks  Y.7/-13;  —  dazdi  m!  ydka vayaAi  y.S.16;  —  hixr?m  .  .  aslim  ....  mjanani  ..  dahat  ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti  (statt  NPn.)  kiitmti  yzary.-  \ . .  failySnte  . ,;  tarn  tä  (AP.)  aiibys  .  . yiarmtts..  V.5,i8£;  —  a%ra  ml  urvarä'.msirinavahi  Yt5.87;  —  yB  dim  *fra- raöhnü  vTspä  ,.;  ta  (statt  APf.)  ha%ra  hinan  {sA.)..,  anairyanqtn  tai  dahytmqm vJvärayemi^ . 5.  \^i.;  —  vTspanqm  narqm\vfrihrai  uzjasaiti  N.ffff;  —  agtmanqmat ..  vispanqm  gSus  sar^anqm  . .;  //(ADf.)'*'.  .  vazyail {sA.)  . .  ratSui  nmStum  fi-anäia- larpnava  müwaireisd.)  ..  V,2.27f.;  — 'yatayezi  tajyayata  naväj  tatyayata(sd.) mit  Numeniswechsel:  jahi  . .;  tisca  t^A-j.s;  s\  s',  4';  —  ym  i^  (tiDxi.)  yaf- mraomi  jq%wS.lara  ..  V.i&öa— 65;  — '  tatary  {sd.) 'S.  4  g;  —  ASn.  in  kollektivem "mi^rS.ao/anAs  ..  yatcit  vlmaiiim  (sd.)  Smo:  umarä  baiiazyä ..,- tat  vlsp^m /rTttä- ai^ha  s3mS,   t»mSt  tnihrS  hangrp/simnS  mahi,  tat'  vuppm'  . .  V,  20.  4£  a)  in
13113:yahmat  haca  Jräkwirisal  näfs  airyanqm °Hyunqm  ^r^m  airyanqm  'hyunqm  Yt. '^■^7)  —  ifar^Rö  .  .  yat  asti  airyanqm 'Ayunqm  Ytip.  56;  V. /^.  39;  —  iava/ftn :^arpnd  'hrähr^m  airyanqm  "AyunamYl-ig. 69;/?.  10; —  avavat  kavaSm  3^ar>ns yaha yat  iöa  anairym  °Ahus  hakat  usäi  us.frs- vayöit  (sd.)  Yl.  ip.  6  8 ;  —  taurvayeiti  anairya *'/iAävS(3isA'P.)Yt.iS.2;  —  airaityanqm tat  °Ayunqm  Vf/y^rai  uzjasaiH  N.(iS;  — aiioitaradyJ  haca  'nhubyö  Yt  i'j.  14;  — mi>r)m  .  .  yim  yazmte  daiAkupatayS  .  . aniar»  -iiihu  (AD.)  papr^täne  Yt.  10.  8; r_5.  49;  —  hasaaräis  (näml.  asH  mihrS) aiitary  °Ryu  (AD.)  Yt.  /o.  117;  —  yd  .  . karafanö  urapayeintl  (sd.)  yacä  xrata *Ju£>sc/a'irä  "Ayunqm  Y.4^'.io;  —  säsia 'rthSui  äaähupailii  *äxsta  isimnS  'lihave amtm  is^mnS  tanuye  YtJÖ^.  19;  —  sSsta 'itißaus  hams^ia%rö  Yt  13.  r8,  69,  75.  50; — fraiimatcltl!  'Xyunqm  Yt  13.  95;  *lo.  18; —  nöit  me..  ährava  . .  'iiifiava  (LS,)  earät Y.p,  34;  —  Siihqm  'hyunqm  yä  anyä rajSit  Y.ig.  18;  —  bawrSil paiti  'tJihaove Yti.ag.  a)  GS.  mit  GS.  des  Landes- namens  zur  Bezeichnung  der  Gebürtigkeit bei  EN.:  parlatgava  dazgrS^ava  apa- jTjVavi  (sd.)  'iähfus'  Ytrj.i2j;  127;  — ^rüJ  atv5jar3(^  fyultahe  tanyehe  tanyayä •tViÄÄ/ Yl  jy.  125;  125';  —  s,  noch tnzavant-  daitiksus  EN.  a)  bes.  im Gegensatz  zu  Haus,  Gemeine  und  Gau***; a)  im  gAiw.:  *S  sl  dimSnsm  vTs)m  v3 söihnrrt  vä 'Ayäm  vä  adaj  du^iäcd(sd.) .. Y.jt.  18;  —  yP  Auäänus  d^manahyä  xla- %r?m  iiSi^rahyS  vä  'AySus  vä  .  .fi-ada'iiäi (sd.)  asppmaia  Y.Jl.  16;  —  ga  JrSnKis' (sd.)  /tfiiraAyä  vä  'AySus  vä  Y.4ß.^; —  ähnlich:  patri  jfaSSuf  airyamanascä dadaiii  (sd.)  tiSil  ma  xsnäus  yä  v^rvsSnä (sd.)  ..  naida  'hy3u!  ..  sästärB  (sd.)  Y.46. 1.  b)    im  jAw.:    */ratainitm   .  .  yä
15470:(s.  ebenj.  3)  'von  —  her,  von  Seiten', mit  Abi.:  yat  bavaiti  avi.spaslB {sA.)  sssta . .  aurvd^aiibyB  tb  tbisyanbyB  Yt.  13, 69;  — neben/(7r><  i';  vUarf.qzahyehe{sd.^ca  patli . . pairi  *Aalnyäs!a  vBiynäuyB  aurva%aäbyasca •rB  pifyanbyö  Y.  68. 1 3.  4)  'mittelst;  mit Hilfe  von  — '  (Abi.):  yim  yazata  haomB .  .  anähimt  'rB  barismm  Yt  iO.  88;  88'; —  yüsmaoyB  'rB  karsnazB  hvira  baon  Yt. '.?■  38;  —  y<ii  3s  masyanqm  . .  aoji^B  ,  . nairyayät  'rB  hqm.vtrttBil  yat  dim  uparfha- cat    hqm.variilil  Yt  J(J.  jSf.  5)    'um
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
```


## [2026-09-07T19:33:19.854Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18700,18740p' BRT.txt; echo \"=====nairi headword=====\"; grep -n \"näirI\\|nāirī\\|'Frau'\\|näiri\" BRT.txt | head -20"
}
```


### [2026-09-07T19:33:19.914Z] TOOL RESULT

```
hanfa  .  .  afym  staoiti  "wenn  man  , ,"  H, J.  7 ;  —  hyat  n  a  /ryli  vasiamnö  isvä  (sd.) daidlt  Y.  43.  14;  — yat  nä  paurva  frahda (sd)  .  .  fi-amaaaiti  V.  18.  40J  34,  37,  46, 49i  54  (Sp-  Sao  u.);  —  ya%a  na  snaüi/ . .  nifmatfm  (Sp.  500  m.)  paiH.valnoit  P. 21;  YL13.JO,  71,  aa)  In  gleichem  Sinn erscheint  auch  NP.:  äai  mqm  narB  . . yazmte..  darrfB.yast»m(sd.)/a  .  .  H.2.  14; Vd.iS;  —  ^aj  ta  (Sp.  6ia)  nara  yaos- dayqn  aahm  .  .  ya  nasaum  avahistät "können  die  Männer  (sva.  kaim  man)  puxi- fizirt  werden  .  .,  wenn  man  . ."  V.  5*.  33; 35.  97.  7-"3.  "5-
Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
Komj>A.,  E. ;  AbleiL  —  ai.  nä,  nirah,  n/iliyah ;
dby  Google
"nara
nairyö.sanha-
1054
np.  nur.  —  Pü.:  mar/;  s.  noch  No.  10,  16-31.  — ■}  Die  einielnen  Bedeutungen  sind  nicht  immer streng  auseinanderzuhalten.  —  >)  Them.  Vgl. ai.  nara^  NS.,  usw.  —  3>  VgL  lu  nars  gAw. Bwj  und  Abis,  mnl;  Bthl.  IF.  5.  J63.  — 1)  Hds.  mrtgä  raydii.  —  S)  Vgl.  va  sava:  —
—  *>  S.  datu  nurobr.  nerf  'principes'.  — 7)  Pronominal  flcktirt?  —  8)  5  a6^_  54.  _ 9)  Vg).  Dbr.  VgJS.  /.  421.  —  ■")  Pü.!  lässt das  Wort  aus.  —  ")  Hds.  n<üri.  —  n)  Also GS.  an  Stelle  des  AR!  —  >J)  Hds.  nairi.  — M)  S  268.  41.  —  "s)  S.  daiu  Gdn.  BB.  14- 14.  —  16)  Pü.  hat  fiit  tasnä  nur  ki,  wie  Tür ii  allein;  ».  No.  ZO.  —  '7)  Pu.:  1  oniä^,  SU.: asmäiant.  —  18)  Hds.  Aaonä;  Pü.;  ön  mar/. — '9)  Die  beiden  Worte  fehlen  in  der  Ausg.; aber  T  hat  srao%rana  undPü. :  mart..gäiäri sräyiSn.  —  lo)  Pü.  nur  ii;  s.  No.  16.  —  "•)  Hds. vtt,  aber  Pü.  mart.  —  ")  Hds.  iä,  aber  Pü. marl.  —  'S)  Wohl  vetstümmeltes  Zitat;  s. P.  2J.
•  j.  ^vasia  /laoa  nara  /aca  mara  ^aSo näjanasus"  Yti2.8.
•  j.  "naratö  ifr^^m"  N.  46,  gj  (wo Jtarai^in),
Anscheinend  verderbtes  Zitat.
•  g.  naräm  nar^m  Adj.  'MannfiirMann, mlinniglich' :  sraota..n'  n°  i^ahyäi  lanuyi .  .  ahniäi  nS  sasdyäi  (sd.)  baodantd  paiij Y.30.3.
Ein  ämreißam;  AS.  aus  »flr-.  —  Pü.i  ki  marl
•  j.  narava-  patr.  Adj.  'von  Narav  stam- mend, dessen  Nachkomme' " :  ayraira^ahe °vahe  Yt  13.  131 ;  g.  18.
Ableit  aus  "tiarav-  m.  EN.  —  0  Anders  DsT. ZA.  3.  433.
•  j.  naircmanah-  Adj,  'mannhaften  Sinns' : °ni  ktnsäsps  Y.  g.  11,  Yt.  j.  37,  1$.  aj, ip-3^,  44*-
Slfttl  *nairya-m'  geschr.;  S  2ÖÄ  3*.  —  Vgl. ai.  H^mänas-  Adj.  —  Pü. :  mart  minisn,  erL : tus  dl!  pa  gas  däsl.
].  fiaili.naröiS  N.  Ö5:  lies  fnlli-barSis.
•  j.  *narö.vaeipya-  *'  Adj.  'päderasterisch': a'/a  anap?r3^a  fyaoiina  yS  °ya  V.  /.  1 1.
Ableit.  aus  *narv.i'ii^-  m.  'Päderastie';  zum V.  vacft-,  —  Pü.!  mart  vefili,   eri.:  tun  marz.
—  ')  So  Jp  I.     NA,  'vaifaya.
"  j.,  g.  narap-  V.  'abnehmen',  vom  Mond. Praes.  14  mrifia-.
is  yä  mä  ttxfyei/l  mnfsaitt  %'wal  (sd.) Y.44.%; —  k(ü  mh  mrifsmtii  . .  paiica.- dasa  tnä  n^n/saiti  Ytj.  2;  —  tunfsatä- (nur  Ableit.).
Pü. :  nir/sitan,  mit  der  np.  Glosse :  Um  hidan;
NpÜ.:  täsla«;  Sü.j  «imWiim,  (luVt.)i  kinyali
3S.  (statt  »liyatij.
•  g.  narapis-  n.  '(Verminderung  sva.) HcTabwürdigung,  Herabsetzung'  *\  mit  Akk. verb.:  iöi  'pis  (AS.)  *ar»jU  akasä  (sd.) (isjlt.anlä  Y.  53.  9.
Zum  V.  nartp:  —  Pü, :  :*/  m  i  15  dastawar nirfsenend  ('sie  vermindern')  vai  ..  .  —  •)  Vgl. lAusdr,  nnter  kasyah-  a.
•  j.  nairya-  Adj.  (fem.  'ryä-)  'virilis'; i)  'männlichen  Geschlechts';  a)  von  Men- schen; dva  nara  us.eayeirtie  mHwana (sd.)  strica  'ryasca  V.  2.  41 ;  —  yezi  °ryS afihat  ..yezi  strJ  atshat  V.S.  $S;  —  däya ml  .  .  'ryqm  3snqm  */razaintlm  \.6S.$;
—  'rySraiu!..  N.5(?).  b)von Tieren: m^rsya  .  .  mi^wana  strica  'ryasca  "V,  iS. *8;  iJ-Si  (von  Hunden).  2)  'mann- haft', von  hqm.vaniay-  f.  (sd.,  auch  fdSL): -re  (NSf.)  hqm.vanitis  \t.io.b()  usw.;  — 'ryqm  Aqm.vaniim  Yl  ig.  39  usw.;  — °ryayä  Aqtn.varytsis  S.1.32;  —  ha'hra °rya  (ISf.)  kqnt.vania  Yt  io.  71; — 'rya- yälparB  /tqm.v»rytoii  Yt  ig.  38.  S.  noch unter  nairyS-saaAa-  mit  No.  i.
KompA.  —  Ableit.  aus  nar-.  —  ai.  nörya- Adj.  —  Pü.:  nar,  (lu  Y.  68):  i  martä»,  (lu N.):  fehlt.
•  j.  nairyö.näman-Adj.  '(mit  männlichem
Namen  sva.)  männlichen  Geschlechts',  von Tieren;  hazanräis  jJ!nr/(sd.)  strl.nämanS ..  -manaitiP.)  V. 13.51,  l4-iG\.  Wert- los; ani>iaHbyS  .  ,  yS  asti  yazatanam  . . *'manh'^Yt4.Z. FB.  (lu  V.):  iiar  näm ;  s.  noch  No.  i.  —  >)  So F  1 ;  NA.  ray5.it',  vgl.  Npü. :  xälis  n.inii.
•  j.  nairy5,saoha-'>  m.  Name  einer  Gott- heit {Yazata),  die  des  Götterbotenamts waltet;  *'hs'^  ..  astö  mazdä  ahurahe  "J^., der  Bote  des  AhM^  V.  ;p.  34;  34;  — nairyS.sarjAs  (statt  Dat )  aocayata  yS  dmva ahurS  masdh:  nairya  sartha  '*  vyHxana  . . imal  saiihsil  airyamanai  V.  22.  7;  13;  — sraosasca  ,  .  °hasca  yd  mayu^{sA.)  Yt  10. 5a;  —  apqm  naptärsm  . .  nairim  sanfum  '> Y.  77.  23;  —  sraohm  ..  nairimca  saa/ifin'^ huraohm  Y.  57.  3,  Vyt^o;  Vr.  7.  i;  — sraolake  ,  .  nairyeheca  sat?haAe'^  Vr.  is. 16;  — yqmca  (räml.  Jrava/lm)  srao/aAe ..yqmca  nairyeAe  saaAaAe'^  Yty.Sj;  — Xfa%r»n.nafolrfm  "Atm  yazattm  Y.  77. 1 1 ;
—  xl<£ä:rd.naf^r5  'kaAe  yazatahe  üy.^.S. •)  Wie  der  indische  ^^nü.    In  der  Tat  steht
n'  in  y.  7/  unter  den  Namen  für  Feuer.  Vgl. ai.  HÖräJämia-  und  Gray  AfB.  j.  45,  OLDEM- RBKO  ZDMG.  S4-  49-  5.  noch  die  GrBd.-Stelle bei  DsT.  ZA.  S.  319-
dby  Google
I055     naiiyam-ham-värativant-
Eig.Bed.?i),
056
=====nairi headword=====
2531:y.  I ;  —  cayö  'te  raola  at»A)n  . .  yö  ava^a  '  vayrjanake  .  .  yat  °&o  kanjasante  paouru Sraoiayeite'^.2.^<j\  —  "taFsva  daxtnaih'a .gaonaAec'a  IsA.)  . .  ti.6^\  yi(7);  —  taotarf yöi  faiti  äya  z^mä  iavainti  "V.y.^^;  — ^.gstava  ..  ■""'oa'*  ..  N-tVi;  —  yetiAe  'oa "U  malsma  .  .  yaHbyö  .  .  framayattte  V. .  mazdayasnanqm  näirika  . .  *ham.raf^wa- (S'.ii;  —  'taisam  syao^nafiam  yöi  v»r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, sjbA'  masy.lka  V.  J5.2;  —  "tiitbyff  zao-  11;  —  ava'ia  ''QrtV.4.50;  —  taica  "'jaca >rabyö  ..  yämham  ..  N.  71;  —  ku^a  -tat  pü^nm    baraili    Y.iy^^if).  a)    mit
2559:;j.  I ;  —  cayö  'tt  raocii  atjhin  . .  yö  avaha  '  v(rf'ianahe  .  .  yat  '6a  han)asSnte  paouru Sraoeayeite\.2.y);  —  'tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazdayasnanam  näirika  . .  *hqm.raEä:wa- J'.ii;  —  'taiiam  syao^naiiqm  yöi  V3r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, ziiiti  masyjka  V. /j.  2;  —  "täibyö  zao-  11;  —  avaoa  °oa  'V.4-50;  —  taica  °üaca 'irJbyß  ..yäakqm..  N.  7/;  —  iu>a 'tat  pu>nm    baraiti    V.  15. 49(?).  a)    mit
2713:•  j.  aevö.mahya-  Adj.  'einen  Monat '  ständnis  bringen,  so  gut  wir  können" dauernd':   yat  näirika  upas.puirlm  jas3l\  Y._J5. 7;    —    tat    nö    diyata   yaiim    ya-
2801:Irrlehrer,  der  . ."  \.g,$i{.;  —  yavat  °fa *gaintii  upankacaili  (sd.)  V.  7.  56;  — yavat  'sa  ilß  bySrixfi  (sd.)  .  ,  frabavai \.i4.\y,  — yavat  -lö  spä  anya{sA.) )asö V./5.48,  a)mitrelativischemAnschIuss: "jS  zT  asti  baslazyö.t3mö  .  .yal  *mahnm.- sppni»m.baei'azyd  (sd.)  V.  7.44;  —  '/a  bi~ paitisiana  (sd.)  y3  kaine  V.  75. 19;  19;  — vXsp»m  ä  ahmst.,  yat  -ia  yö  apsntinyBkB uxjasnf  (sd.)  "bis  es,  das  Kind  . ,"  V.  75. 15;  —  'sa  yS  *ar?mBiidd'a.W3.  2)  auf ein  Relativum  als  dessen  Korrelat,  sub- stantivisch: ci'at  dra)ö  avaMUlüt  '^a  yö näirikaya  . .  !^ar>^3tn  frabamt  V.  /J.  4 1 ; —  °sö  .  .  aitayä  vihrkayh  (sd.)  Jq'^-wS.' tarö  *at3kat  . .  ya^a  spä  vtkrkake  k»r?- naoiti  V.  y .  4 1 ;  — "/?  ratufris  *yö  jayara N.if};  24,  60;  —  'sa  yetjhe  apirinSyükö ^•9i  7;  —  °^'''  zaoiranqm  tnaziltaca  . . yiJ  *naire  asaone  *daste  N.^4.  III)  In
3222:—  spätatn  da^im  . .  "oa  azsm  .  .  spän?m nida^^m  V.  y,  39; —  a^arät  .  .  °äa  agsa näirika  *zastö.mitim{%A)  äp>m  fraauAaräl "sie  soll  trinken  .  .  und  (zwai)  soll  .  ." V.  7.71.  a)  wiederholt  'et  ,  .  et';  'oa *zpmahe  matoim  'oa  ^t^maie  z^r^a^rnfsd.) V,  !.$.  a)  das  zweite  Ma!  mit  '/it  'cum ..  tum':  °oa  Äftiti  yotumashma  -oa  taiat usjasmti  V, /,  14GI.  3)  auffordernd 'so  .  .  dann',  vor  Opt:  °ba  nö  tum  . . dayi  "so  mögest  du  uns  denn  . ,  verleihen" Y. 37.26;  Yt.JO.94;  —  °la  .  .  UV  nipaya YL/0.93,  Y.57.2Si>;  —  °äa  mq%r»m  'tat matryHt  V._^.33;  —  hurayäsnt  "oa*'  .  . daidyat  A.J,4.          [Vr.22.2:    lies  mäoa;
3392:— yö  anyahe  näirika  anahaxtB  'fum  *pa-
3664:—  ym  'k3  frashavat  (sd.)  satta  ki  paoi- rfm  frasnäoay^n  aitahe  yat  'kahe  V.  16.  ^ ; /J.44.4S;  —  näirika  'kasiaV.3.\\;y, — nitrHatüt  •iahecil  N..40;  —  näirikqm w  *'ibm  (va)  N.  105;  —  nairinqmca 'ioMOMca  kainikanamca  Y.6S.12;  —  ttai- riie  'keQ)  kainike  Y.'2?.5;  —  nairikqm ..  mbmtmiit  (sd.)    "Awi^V. 5.38;  75.48;
4354:•  j.  ana-saxta-  Adj.  (fem.  °/ii-)  'der  den Ablauf  der  (bestimmten)  Zeit  noch  nicht erreicht  hat' "' :  yö  näirikam  yqm  a/^'irqm ..'tarn para  xludrä  ai'i frau/wrjzaiti  "wer eine  Kindbetterin,  die  ihre  Zeit  noch  nicht abgewartet  hat,  vordem  beschläft"  V.  i^.  8.
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5554:mnbyascä  näiribyasca  xara>ustrahe  za-  »j.  aurva- Adj, 'schnell;tapfer">:  ^«rffli^^iT tshsus  raßoräi  manaahS  "het  komme  Ae^  aiWü  'vS  \X.4.q;  —  Iqm  yazjitta  'va liebe  X  zur  Unterstützung  zu  den  Männern  hunavSvalsakaya\\..$.t,T,i^;—iS>:riv!Ht und  Frauen  des  Z,  zur  Unterstützung  des  "'^"p«  Yt/0.109;  14;  —  'itwam  yazfmU guten  Sinns"  V.54,1.  "i-ätihs  ahuränhs  VL5.85;  —  yat  bäun
6259:—  antar)  i^ädamaü  'iiionis"  (IP.)  Vr.  21. 3.  'P-S^i  —  °Ai<JW  (VS.)  pu%ra  kava vJstaspa  ^y\-53',  45  (wo  'säum);  —  ratui 'iava  V.ö.ii;  Vr.5.6;  —  'laonB  aiahe raiwü  rafufritlm  Y.  22.3,  71. 3;  — yqmca bipaitistänqm  '/aonim  Y.  13,1;  —  °/at»ti- nqm  ärmaiti.paoiryanqmY .21.2; — Jiaisa- nqm  . ,  sasnSgüsqm  . .  'iaonqm  '/aoninqmca ..  nabänazdistanqm  ..  -saonqm  'iaoninamia .  .  af&rapaitinqm  'iaonqm  .  .  ai'i:ryanqm 'iaonqm  .  .  naram  'iaonqm  .  .  näirinqm 'saoninqm  Y.  26. 4— 8;  gf.^,  Vr, /.  3';  — ä'irai'antm  'iavamm  ,.  rdialitär^m  °iara- mm  .  .  västrXm  fiuyant^m  'iavanjm  .  . nmänS.paitlm  °!avan»m  .  .  nmänB.pa'inUn 'iavanjm  (statt  fem.)*>  aiaAe  raiüm  Q.4 7  f.;  7—9";  —  zaotanm  'savamm  ,- sraoiävar3zim  'iavafum  G.  J.  5;  5*;  — Aai^yavarxsqm  'iaonqm  haOiyavamtnqm -saoninqm  V.17.14;  14*,  G.J.7';  —  saoi- yantqm  'iaonqm  Y.  ;4-i.  *i~-li  Vr-5-i. 22,1,  Ytii,i7;  —  äsna?a  mana  'iaonqm äsna/a  mana  saoiyantqm  Vr.  /i.  3 ;  — fravasays  .  .  yamca  staoyB  (sd.)  'iävaoyj {DP.)YU3.88(f);~ädaAyunqm/a  'iaonqm .  ,  uzdaAyunqmca  'saonqm  Vr.  16.  z;  — irtrüuiqm  'iaonqm  .  .  Jvantqm  'saonqtn Y,  24. 5 ;  —  vup>m  'Savamm  h3iit»mca bavantimia  bü^anipmca  Y.  2^4,  Vr, /Äs;
6271:—  '/äum  spitama  Yt.5.89,  91,  72.2,  77. 21.  aa)  auch  kät'  i^.  (ohne  Nennung des  Namens,  s.  i  a  a):  paiti  dim  psr»sat 'hva  asäum  afiura  masda  .  .  äat  mraot ahurS  mazdä  axtm  bä  tl  tat  fratnraväni ,  .  asäum  spitama  Yt  72.  i  f.  ß)  Sing. koU.  sva.  die  gläubige  Gemeinde  im  Gegen- satz zum  amtirenden  Zaotar^^:  ya^ä  ahU vairyS  saota  (sd.)  fra  ml  mrüti  .  .  a^ä ratus  .  .  fra  °lava  vütva  mraotu  Y.j. 25.  f)  GP-  mit  fravasay-  (sd.,  auch fdSt):  'laonqm  {'launqm)  JravalayS  Y. 2.6,  Yt  7^.1,  usw.  0)  insbes.  mit  nar-'>> m.  und  näirl-'^^,  näirikä-'>'>  t  'der,  die Gläubige',  von  den  erwachsenen  Mitglie- dern der  zara^ustnscAitn  Religionsgemein- schaft; Sing,  und  Plur.:  narsm  'savatum ys  anhat .  .  mqhr^m  p}r>sS  'sava  V.5.2;
6272:—  yS  nanm  'savamm  anyS.var^näi  vä anyS.tka^äi  vä  kasyatihe  (sd.)  sarjAäi daiäiti  V.  75. 2  ;  —  ya^ra  narB  'savanS ahm  hittii  zrasdättma  .  .  yahraca  atbUtS 'sava  Yt.  7^,25;  —  nanm  'savamm  .. näirikqm  'saomtn  V.5. 33,  42;  —  narqm 'sagnqm  .  .  nilirinqm  'saoninqm  Yt  7_j. 143—145*)  —  niruyS  'savaoyS  (DP.)  Yt >y.  1 1 ;  usw.  2)  von  Göttern  und  von göttlich  gedachten  Wesen  und  Dingen (s.  auch  3),  auch  sva,  'heilig';  im  jAw. (unvolbtändig);  am>sanqm  ip^laiiqm  .  , yöi  ai^yajanhs  'lavanS  Y.sÖ.y,  —  vls- p?mca  'Savamm  . .  yazat?m  Y.  16.  i ;  2, 25.8';  —  vjspe  '^avanö  (als  AP.)  yazata üyeseY.  2.i8i  77.5,  76.9,  6'5.i2,  G.2.6, FrW.  7. 2 ; —  tat  nö  dayata .  .yazata  'savana (VP,)  Y.  65. 14;  —  yazatanqm  *'iäunqm  ■ Y.J.4;  22.27  (*"  'saonqm);  —  mai  vis- pSbyiS  'laonibyS  fravalibyS  Y.  2_y.  2;  2,  2^. S;  —  fravasayS  .  .  'saonTs  Yt 7,^.40,  57;
6731:•  j.  B-haxta-  Ad),  'der  berechtigt  (geeigen- schaftet  und  ermächtigt)  ist  (etwas  zu  tun)' : yS  anyahe  näirika    anahaxtd  aiaurun^m
6944:•  j.,  g.  ahmät  Adv.  I)  'inde';  i)  räumlich; nHt  käu  as  vaote  (sd.)  .  .  nBit  a'  vaiata ". ,  oon  inde  procedit"  P.  4^.  2)  zeit- lich, a)  'von  nun  an,  nunmehr':  ys . .  kayä (sd.)  a°  . .  7'ästryä  Y._jy.6;  — yä  a°  staota yasnya  irävayeni  "indem  ich  nunmehr  die StY.  aufsage"  Ny.4-S-  b)  mit  folgen-' dem  ya^a  und  fiiL  Konj.  'doncc,  bis  dass': aU'it  a'  yaha  ap?mgm  maniva  an  Aat mz'Ji/is  (sd.)  Y. 10.16.  U)  beim  Kompar., wörtL  'als  das',  was  i)  vorausgeht  oder 1)  folgt;  meist  unübersetzbar,  i)  zurück- weisend auf  zuvor  Genanntes  oder  Ge- sagtes: imaj  vS  jatöyemi  .  .  yalca  a°  asH miirya  ".  .  quodque  hoc  est  maius"  Y. 'jj.  14;  14'i  —  saisisca  .  .  oAqxitäiscä *ß-äyjblscal(sA.)ca  a-  Vr.  Ä  i.  a)  in Verbindung  mit  eil :  ayaaAaUtäis  kan- täis  paiti  azdibis  avaJitriäiyilt  {%^)  masyd vü  'mii-'i/V. 4. 50;  51,52.  2)  voraus- weisend auf  einen  Nebensatz  mit  &)yd:ia: yifnö  zqm  visävayat  afvit  irii'va  a'  mas- yefäm  ydia  fara  ahmai  Y.  2. 1 1 ;  —  nüit il  a-  *drajyS  *yätltn  framraemi  (sd.)  .  . äfrOIm  .  .  ya>a  .  .  V.33;  Yt.  I3. 64^;  — xraesyöJaraia  (sd.)  ri5  a'  ya>a  vikrkS raiÄfsd.)  Ißi/eV.  IJ.8;  —  näirivai/e.  .  «• pÖurum  '>  frantraomi  . .  ya%a  mayavö  (sd.) /ratäxsffit'V.4.^T,  47J.  h)  yäha  yat: itsit  vaakö  a'  fyao>amm  v»r^yeiti  ya'^a yai..karMt^.4S;^.iS.\o.  c)  yattsit: nSit  vanhs  a'  syao%tum   vtnsyeiti  yaüöil
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
8623:•  j.  uz-uätSna- ■>  Adj.  'leblos':  yat  .. nliriia  .  .  apuhrTm  (sd.)  nijassi  'na  V, 5.45; — ym  näirika  . .  apuirim  *Vw»w'' nijasäUi  Vd.  ig;  —  *«i  (ÄPn.)  .  .  uäana- ?'(kW  vTspä  frasumaitJs  (sd.)  P.  5Ä
8898:1)  'etwas  bedenken,  überdenken,  über- legen': yö  näirikam  a^ra^aitim  .  .  baoLo VlOT'-i  iiii'^wn'''  bao-iai^uhiiiljm  -.■i'iuiim avi.iii'i'i'usim''"'  Xiudr.l  a-.-i  frankar." taiti  .  .  kiU  aäahe  palti  varsta  syaoina HH>w<i^'>  ataaa  (sd.)  "<jui  in  muhereni menstiuam     sentiens     sciens     meditatus
9639:•  g.  kudö.zäta-  Adj.  'beliebig  wo  ge- boren': urunJ  ..  'tanqmcU  narqmcä  näiri- nqmiäY.3g.i\  zit  Yt  7j.  154,  wo  kmSjs'.
9651:I  •  j.  kü-näiri-'t  f.  'Hurenweib,  Hure',  ital.
```


## [2026-09-07T19:33:42.751Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"nērōg\\|nērōk\\|nerok\\|nērō\\|hunar\\|nārīg\\|nāyrīg\\|nayrig\" NYB_vol2_glossary.txt | head -20; echo \"=== PHD nerog ===\"; grep -n \"nēr\\|nerō\" PHD.txt | head -10"
}
```


### [2026-09-07T19:33:42.824Z] TOOL RESULT

```
=== NYB ===
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
2057:hunar [hwnl] skill 3?5, 158-9-20, 694, 845, — Av. (1831) hunara-; MPrth hwnr ‘manli- ness, ability’; Paz. xunar; NP hunar. *hūnēh: read *höneh q. v.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4039:vat-hunar [wthwnl] of bad skill, unskil- ful, comp. ~-tar 15$.
5197:haxay-: *hamāxakēh (vi-)häy-: višatan haya-, hya-: xóm hazanra-: hazar hazanré.zyam-: hazan- grö-zim hšm, ham: hamak hindu-, hondu-: Hind hixra-: hihréh hizü, hizva: uzvàn hudah-: hu-dahak, véh-dak hü-: ?xuar hu frāšmē.dāti-: frašm hüxta-: hüxt humata-: humat humäyä-: Hamak hunara-: hunar hunivixta-: *hu-vaxm hunu-: hunusk h(u)vira-: dür-huviréh hurà: hur huska-: husk Hutaosā-: Hutös hutāšta-: hu-taštak hvaro-darosa-: xUar-cašm hvaro-xšačta-: xUar-xščt hvaršta-: huvaršt hyaona-: xičn
5638:hwnr: hunar
6943:xūnāhin: xYan-asén xunar: hunar xurahe: xYarrah xüram: huram xurdak: xtartak xurséd: xLarxšēt xusrüb: husrav xusrubi: husravčh
=== PHD nerog ===
211:anērān 10 a-pursisnig
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
927:barbarity anērih.
1012:blameless anērang.
2359:ignobility anērīh.
2930:non- Aryan anēr.
3194:power abzār, amāwandīh, nērēg, 07, stahm, tuwān, zor.
```


## [2026-09-07T19:33:44.689Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n -i \"nairyava\\|nērōk\\|niru\\|nīrū\\|hunar\" HUB.txt | head -20; echo \"=== IEC ===\"; grep -n \"aner-\\|ǝner\\|nṛ-\\|nert\" IEC.txt | head -10"
}
```


### [2026-09-07T19:33:44.777Z] TOOL RESULT

```
=== HUB ===
1948:'Wissen' und hunarmandi 'Tiichtigkeit'), liesse ein np.
7611:*zusammen, derselbe* H. 1102; hunar *Tugend' H. 1108 u.s.w.;
7649:'skiir Min. Gl. 157, das neben np. hunar und paz. hunar
7659:Wege, Ranke' --^ np. hunar; hzaur machtig (aus Viti-zaur),
7677:xurtak 'klein , aber h in hunar^ Humdk^ humanak^ hudihr und
=== IEC ===
11529:narK- (?) ‘seizure, grip, torpor. Cf. WP II, 701 Gk. nárkë, f. ‘torpor’; Alb. cf. narth, v. “feel cold’; i nerthté, adj. ‘freezing cold’; Sw. cf.
11655:ner- (1) ‘man; male’. WP II, 332. Cf. ne- rios, nertos Skt. nárah ‘man, husband, hero’; Av. nar, id. beside naro, id. and cons. stem nā, acc. narom, id.; Ober -nara-, in cpds.; Per. nar, adj. ‘male’; cf. nare ‘penis’; nari (id. & 'virility); narian ‘stallion’; Oss. nàl, adj. ‘male’; Scyth. cf. ená- rees, enáries (/hermaphrodites'. Compn. un-
11667:ner- (2) “into, in, under”. Variant: nor-. Cf. ener-, nerfteros, en-. Arm. (ambig.) cf. ner-Ko, adv. & prep. (under; Ko = "eidel: (Arm. nerban, Get ‘sole of foot? is a folk-etym. based on Tk. nalband or its Pers. form na'lband); Tokh. B cf. fior, adv. & postp. ‘below’; Gk. cf. nerthe(n), énerthe “under, below’; (e)nérteros, adj. “lower”; Li. neng, ti, v. ‘dive, plunge’; OCS cf. (o-gde) noriti, inf. id.; cf. Li. náras, m. ‘diver’. Cf. also Li. neris, gs: iés, m. ‘beaver’ & Cz. nofec ‘mink’, LW in G Nerz ‘polecat; marsh otter; Cz. norek ‘otter. (*-e-: *-o-)
11669:nerteros ‘lower, down; nether’. Cf. ner- (2). WP II, 333
11671:Arm. cf. ner- in nerkin, gs: -kno, o-st. “lower, interior; Gk. nérteros, adj. ‘lower; Umb. nertru, ds. ‘left-hand’; cf. MHG norder, adj. adv. ‘northern; northerly’; OE norperra, id.; ON norór, id. in Z-gde
11672:nertos ‘manly; manliness, virtue, strength’. Cf. ner- (1) and nerios Olr. nert, n., Ir. neart, m. ‘strength’; OBr. nerth-, v. ‘fortify’; W. Cor. nerth, m. ‘power, strength’; OE (hapax) neorp, adj. 'content- ed'?; ON cf. Njorór, gs: Njarðar, ds: Nirði (name of a god); geir-njgrór, m. tspearbearing warrior"; cf. Oss. nart, m. ‘hero’
11851:nor- (1) “penetration; inside; interior; depth’. Cf. nið, enor-, ner- (2), nerteros. WP IT, 333 OCS norü, m. “den, hole, cave, nest’; nora, norja, f. id.; R norà, f. ‘burrow’; Ukr. norà, f. “hole; source, spring’; Li. náras *diver-bird', cf. naroms, adv. “under water; narüs, adj. “Table to sink”
14645:rmtos, is ‘restful, resting, quiet; rest’. Cf. rot- (1) (rát-). Skt. ambig. Skt. ratáh, adj. ('cgratified'. To root ram-. Monier-Wms. Cf. rameio); rátih, f. ‘rest, plea- sure’; cf. ratvá, -ratya, pts. of root ram-; Li. rimtas and rimtas, adj. 'serious'; rimtis, f. ‘rest, quiet, inertia’; Latv. rimts, adj. ‘quiet’; cf. Li. Latv. rimstu, rimti, rimt, v. ‘subside’
16587:snork- (snerK-, snrK-) ‘grip, cramp, torpor’. WP II, 701 Gk. (z-gde) nárke, f. ‘cramp, torpor’; Alb. cf. narth, nerth, v. (“feel a chill’, fr. *snork-); OHG snaraha, OE snëarh, snëare, ON snara, f. *snare, noose' (o-gde in view of e-gde MHG snérhan, sv. 3. ‘constrict, tie’, as against ON snara, v. ‘twist, wring’)
17495:Lat. cf. stagnum, n. (“pond”). Phonol. ambig.); stagno, are, v. ‘stagnate; overflow’. In sense of ‘fortify’, see *sthak-); W sai, m. ‘inertia’; Sw. stackig ('short'. Cf. E stocky); Du. staken, v. *stop'
```


## [2026-09-07T19:33:59.827Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"andro-\\|ἀνήρ\\|aner\\b\" KLN_1966.txt | head -10; echo \"=== find page 47 ===\"; grep -n \"^47$\\|Alexander\" KLN_1966.txt | head -10"
}
```


### [2026-09-07T19:34:01.034Z] TOOL RESULT

```
1820:fr  -may0?,  ‘eating  .  See  -phagy. aerophore,  n„  an  apparatus  carrying  air  for breathing  as  used  for  miners.  —  Compounded of  aero-  and  Gk.  -ipipoc,  ‘bearing’.  See  -phore aerophyte,  n.,  an  air  plant.  —  Compounded  of aero-  and  cp’-ixov,  ‘plant’.  See  -phyte. aeroplane,  n„  an  airplane.  —  F.  aeroplane  com¬ pounded  of  L.  der ,  ‘air’,  and F .planer,  ‘to hover, soar’,  fr.  L.  planus,  ‘level,  flat;  plain’.  See  aero- and  plane,  ‘a  flat  surface’,  and  cp.  airplane, aerostat,  n.  —  F.  aerostat,  compounded  of  Gk. irp,  ‘air’,  and  axxx'1;,  ‘placed;  standing’.  See aero-  and  static  and  cp.  gyrostat,  hcliostat,  hy- drostat,  pyrostat,  rheostat,  thermostat, aerostatic,  adj.  —  F.  aerostat ique,  compounded of  Gk.  dr, p,  ‘air’,  and  oxa xtxoc,  ‘causing  to stand’.  See  aero-  and  static, aerostatics,  n.,  that  science  which  deals  with  the equilibrium  of  gaseous  fluids.  —  See  prec.  word
1892:Afrikander,  n.,  a  South  African  native  of  Dutch descent.  —  Formed  fr.  Du.  Afrikaner,  ‘African’, with  d  inserted  on  analogy  of  Du.  Hollander, Englander,  etc.
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
2709:andr-,  form  of  andro-  before  a  vowel.
2710:Andrew,  masc.  PN.  —  OF.  Andreu,  Andrieu  (F. Andre),  fr.  L.  Andreas,  fr.  Gk.  ’  AvSpsac,  which is  rel.  to  AvSpeToi;,  ‘manly’,  fr.  avljp,  gen.  avSpoi;, ‘man’.  See  andro-  and  cp.  dandy.
2712:Andrias,  n.,  a  genus  of  fossil  salamanders  (zool.) — •  ModL.,  fr.  Gr.  dvSpidi;,  ‘image  of  a  man’, diminutive  formed  fr.  dvfjp,  gen.  avSpoc,  ‘man’; see  andro-.  For  the  diminutive  character  of  the -nf-formative  element  see  Kretschmer  in  Glotta, 14,  84L
2713:andro-,  before  a  vowel  andr-,  combining  form meaning  ‘man’.  —  Gk.  avSpo-,  avSp-,  fr.  avfjp, gen.  avSpfS?,  ‘man’,  which  is  cogn.  with  OI. ndram  (acc.),  ‘man’,  naryah,  ‘virile’,  Arm.  ayr, gen.-dat.  arn,  ‘man’,  Alb.  n'er,  ‘man’,  Umbr. nerus  (pi.  acc.),  ‘men’,  Sabine-L.  Nerd,  PN.,  lit. ‘strong’,  W.  ner,  ‘hero’,  OIr.  nert,  W.,  Co.  nerth, ‘virility’.  Cp.  Andrew,  Andrias,  andron,  dandy, ‘a  fop’,  and  the  second  element  in  Alexander, Ardhanari,  Dianira,  Leander,  philander,  sundari. Cp.  also  the  first  element  in  anthropo-. androcracy,  n.,  rule  or  supremacy  of  men.  — Compounded  of  andro-  and  -xpaxla,  fr.  xpdxoc;, ‘strength,  power,  rule’.  See  -cracy. androecium,  n.,  the  stamens  of  a  flower  taken collectively  (hot.)  ■ —  ModL.,  compounded  of andro-  and  Gk.  oExtov,  dimin.  of  olxog,  ‘house’. See  economy.
2714:androgen,  n.,  a  male  sex  hormone  ( biochem .)  — Coined  fr.  andro-  and  -gen. androgynous,  adj.,  hermaphrodite.  —  Gk.  avSpo- Y uvop,  ‘man-woman,  hermaphrodite’,  fr.  avfjp, gen.  avSpop,  ‘man’,  and  y uvrj,  ‘woman’.  See andro-  and  gynaeco-,  and  cp.  gynandrous.  For E.  -ous,  as  equivalent  to  Gk.  -op,  see  suff. -ous.
2715:Andromache,  n.,  the  wife  of  Hector  ( Greek  my- thol.)  —  L.,  fr.  Gk.  ’  AvSpopaxr],  lit.  ‘whose  hus¬ band  excells  in  the  fight’,  fr.  dvr,p,  gen.  dcvSpop, ‘man’,  husband’,  and  ‘fight’.  See  andro-
2717:Andromeda,  n.,  1)  the  daughter  of  Cepheus  and Cassiopeia  (Greek  mythol.)  —  Gk.  ’AvSpopcSa, Ion.  ’AvSpopeSr;,  lit.  ‘mindful  of  her  husband’, compounded  of  ivpp,  gen.  avSpop,  ‘man’  (see andro-),  and  p£8soi>ai,  ‘to  be  mindful  of,  give heed  to,  think  on’,  which  is  rel.  to  pe8<ov,  pcSs- cov,  ‘guardian,  ruler’  (prop.  pres.  part,  of  the ancient  verb  peSeiv,  ‘to  protect,  rule  over’), pf,8ea&ai,  ‘to  devise,  resolve,  advise’,  prjSea  (pi. neut.),  ‘counsels,  plans,  device, cunning’,  p£8ip- voc,  ‘amea5ure’,  fr.I.-E.base *mld-, ‘to measure, limit,  consider’,  which  is  a  -d-enlargement  of base  *me-,  ‘to  measure’.  See  meditate  and  cp. Medea,  Medusa  and  the  second  element  in  auto- medon,  Diomedes,  Ganymede.  Cp.  also  medical. Andromeda,  n.,  1)  name  of  a  constellation  in  the northern  hemisphere;  2)  name  of  a  genus  of plants  of  the  heath  family  (bot.)  —  From  prec. word.
=== find page 47 ===
73:athetosis,  n.,  affection  of  the  nervous  system  marked  by  involuntary  movements  of  the  fingers  and  toes (med.)  —  Medical  L.,  coined  by  the  American  nerve  specialist  William  Alexander  Hammond  (1828- 1900)  in  1871  fr.  Gk.  affcTO?,  ‘not  fixed’,  and  suff.  -osis.  See  prec.  word, aureomycin,  n.,  an  antibiotic  drug  resembling  penicillin  (med.)  —  A  hybrid  coined  fr.  L.  aureus,  ‘golden’ (so  called  from  its  color),  Gk.  puxr)<;,  ‘fungus’,  and  chem.  suff.  -in;  see  aureate  and  myco-.  The  correct form  would  be  chrysomycin,  in  which  both  elements  are  of  Greek  origin  (see  chryso-  and  cp.  Aureo- basidium).
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
2136:Alcmene,  n.,  the  mother  of  Hercules  ( Greek mythol.)  —  L„  fr.  Gk.  ’AXxp.f)VTr),  lit.  ’the  strong one’,  fr.  aXxf),  ’strength,  power’.  See  Alexander, alcohol,  n.  —  ML.,  fr.  Arab,  al-kohl ,  vulgar  pro¬ nunciation  of  al-kuhl,  fr.  a/-,  the  ,  and  kohl, resp.  kuhl,  ‘antimony  (used  for  painting  the  eye¬ lids)’,  which  is  rel.  to  Heb.  kahal  (Ezek.  23.40), ‘he  painted  the  eyelids  with  antimony’,  Aram.- Syr.  kfhal,  Ethiop.  kahala,  of  s.m.,  Aram. kuhld,  Ethiop.  kuhel,  ‘antimony’.  (Akkad,  guhlu, ‘antimony’,  is  prob.  a  WSem.  loan  word.)Its  mod¬ em  sense  (‘highly  rectified  spirits’)  is  due  to  the analogy  of  the  fineness  of  this  powder.  Cp.  kohl. Derivatives:  alcohol-ic,  adj.,  alcohol-ic-ally , adv.,  alcohol-ism ,  n.,  alcohol-ize ,  tr.  v. alcoholometer,  n.,  an  instrument  for  measuring the  alcoholic  strength  of  liquids.  —  A  hybrid coined  fr.  alcohol  and  Gk.  pixpov,  ‘measure’. See  meter,  ‘poetical  rhythm  .
2147:fight’.  The  first  element  lit.  means  ‘warder  off, fighter’,  and  is  rel.  to  diX^etv,  ‘to  ward,  drive or  keep  off’,  4X4v)TY)p,  ‘fighter’,  4Xxxf)p,  of s.m.  See  Alexander  and  cp.  the  first  element  in next  word  and  the  second  element  in  hippalec- tryon.  For  the  second  element  in  alectryomachy see  -machy.
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
2161:See  Alexander  and  pyretic.
2164:ward  off,  keep  off,  protect’.  See  Alexander  and
2628:Derivatives:  anagrarnmat-ic,  anagrammat-ic-al , adjs.,  anagrammat-i-cal-ly ,  SLdv.,anagrammatism (q.v.),  anagrammat-ist, n.,  anagrammatize  (q.v.) anagrammatism,  n.,  the  making  of  anagrams.  — ModL.  anagrammatismus,  fr.  Gk.  avaypappa- xiop. 6?.  See  anagram  and  -ism. anagrammatize,  tr.  v.,  to  make  an  anagram  of; intr.  v„  to  make  anagrams.  —  Gk.  dvaypaupia- TtyEtv.  See  anagram  and  -ize. anal,  adj.,  pertaining  to,  or  connected  with,  the anus.  See  anus  and  adj.  suff.  -al. analcite,  n.,  a  white  zeolite  (mineral.)  —  Formed with  subst.  suff.  -ite  fr.  Gk.  dvaXx-fc,  ‘weak, feeble’,  fr.  dv-  (see  priv.  pref.  an-)  and  dXxr), ‘protection,  help,  strength’;  so  called  in  allusion to  the  weak  electricity  it  acquires  when  rubbed. Gk.  dXxfj  is  rel.  to  dXsxE'.v,  ‘to  ward  off’, whence  the  desiderative  verb  dXl'Eiv,  ‘to  ward off,  keep  off,  turn  away,  defend,  protect’.  See Alexander.
2713:andro-,  before  a  vowel  andr-,  combining  form meaning  ‘man’.  —  Gk.  avSpo-,  avSp-,  fr.  avfjp, gen.  avSpfS?,  ‘man’,  which  is  cogn.  with  OI. ndram  (acc.),  ‘man’,  naryah,  ‘virile’,  Arm.  ayr, gen.-dat.  arn,  ‘man’,  Alb.  n'er,  ‘man’,  Umbr. nerus  (pi.  acc.),  ‘men’,  Sabine-L.  Nerd,  PN.,  lit. ‘strong’,  W.  ner,  ‘hero’,  OIr.  nert,  W.,  Co.  nerth, ‘virility’.  Cp.  Andrew,  Andrias,  andron,  dandy, ‘a  fop’,  and  the  second  element  in  Alexander, Ardhanari,  Dianira,  Leander,  philander,  sundari. Cp.  also  the  first  element  in  anthropo-. androcracy,  n.,  rule  or  supremacy  of  men.  — Compounded  of  andro-  and  -xpaxla,  fr.  xpdxoc;, ‘strength,  power,  rule’.  See  -cracy. androecium,  n.,  the  stamens  of  a  flower  taken collectively  (hot.)  ■ —  ModL.,  compounded  of andro-  and  Gk.  oExtov,  dimin.  of  olxog,  ‘house’. See  economy.
2970:anticlerical,  adj.  —  Formed  fr.  anti-  and  clerical Derivative:  anticlerical-ism,  n. anticlimax,  n.,  the  opposite  of  climax  (rhet.)  — Coined  by  Alexander  Pope  (1688-1744)  fr.  anti- and  climax.
```


## [2026-09-07T19:34:17.130Z] TOOL CALL #31: Bash

```json
{
 "command": "grep -rn \"KLN:4[0-9]\\\"\" data/verification/page-*.json | head -5; echo ===; grep -rn \"Klein p\\.\" data/verification/page-3*.json | head -5"
}
```


### [2026-09-07T19:34:17.215Z] TOOL RESULT

```
Exit code 1
data/verification/page-166.json:213:       "ref": "KLN:46",
data/verification/page-166.json:251:       "ref": "KLN:46",
data/verification/page-166.json:283:       "ref": "KLN:46",
data/verification/page-180.json:277:       "ref": "KLN:49",
data/verification/page-180.json:359:       "ref": "KLN:49",
(eval):1: == not found
```


## [2026-09-07T19:34:17.253Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2700,2712p' KLN_1966.txt | cut -c1-300"
}
```


### [2026-09-07T19:34:17.316Z] TOOL RESULT

```
73
anemo-
ande,  OFris.  and(a),  ande,  MDu.  ende,  enn,  Du. en,  OHG.  enti,  anti,  later  unfa,  unti ,  MHG.  unde, und,  G.  und,  ‘and’,  ON.  enn,  en,  ‘and,  but’,  prob. fr.  I.-E.  *i}thd-,  whence  also  OI.  athS,  ‘then, and’.  Cp.  an,  ‘if’,  and  ampersand, anadabata,  n., 
Andalusia,  n.,  a  former  province  of  southern Spain.  —  Andalusia  (=  Sp.  Andalucia),  fr.  Arab. Andalus,  a  name  denoting  the  whole  peninsula, fr.  Late  L.  *  Vandalicia,  prop,  ‘the  country occupied  by  the  Vandals’.  See  Vandal, andalusite,  n.,  a  hard  silicate  of  
andesine,  n.,  a  mineral  of  the  group  of  feldspars.
—  Coined  by  the  German  geologist  Wilhelm Hermann  Abich  (1806-86)  from  the  name  of  the Andes  Mountains.  For  the  ending  see  chem. suff.  -ine.
andesite,  n.,  name  of  a  family  of  rocks  ( petrogr .)
—  Coined  by  the  German  geologist  Baton  Chris¬ tian  Leopold  von  Buch  (1774-1853)  from  the name  of  the  Andes  Mountains.  For  the  ending see  subst.  suff.  -ite.
Derivative:  andesit-ic,  adj. andiron,  n.,  either  of  a  pair  of  metal  supports  for logs  in  a  fireplace.  —  ME.  anderne,  aundirne, aundiren,  fr.  OF.  andier  (F.  landier),  fr.  Gaul. *andero-,  ‘a  young  bull’  (cp.  Ir.  ainder,  ‘a  young woman’,  W.  anner,  ‘heifer
andr-,  form  of  andro-  before  a  vowel.
Andrew,  masc.  PN.  —  OF.  Andreu,  Andrieu  (F. Andre),  fr.  L.  Andreas,  fr.  Gk.  ’  AvSpsac,  which is  rel.  to  AvSpeToi;,  ‘manly’,  fr.  avljp,  gen.  avSpoi;, ‘man’.  See  andro-  and  cp.  dandy.
andrewsite,  n.,  a  hydrous  phosphate  (mineral.)  — Named  after  the  Irish  physicist  and  chemist Thomas  Andrew  (1813-58).  For  the  ending  see subst.  suff.  -ite.
Andrias,  n.,  a  genus  of  fossil  salamanders  (zool.) — •  ModL.,  fr.  Gr.  dvSpidi;,  ‘image  of  a  man’, diminutive  formed  fr.  dvfjp,  gen.  avSpoc,  ‘man’; see  andro-.  For  the  diminutive  character  of  the -nf-formative  element  see  Kretschmer  in  Glotta, 14,  84L
```


## [2026-09-07T19:34:24.734Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=2100 && NR<=2730 && /^[0-9]{1,4}$/ {print NR\": \"$0}' KLN_1966.txt | head -40"
}
```


### [2026-09-07T19:34:25.896Z] TOOL RESULT

```
2100: 44
2114: 45
2142: 46
2186: 49
2216: 50
2217: 51
2255: 52
2256: 53
2313: 54
2318: 55
2385: 58
2394: 59
2430: 60
2440: 61
2458: 62
2459: 63
2499: 64
2500: 65
2550: 66
2565: 67
2613: 68
2626: 69
2645: 70
2646: 71
2699: 72
2700: 73
```


## [2026-09-07T19:34:40.199Z] TOOL CALL #34: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo ===; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"ادریس\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -c \"اسکندر\" MON_part1.txt MON_part2.txt 2>/dev/null"
}
```


### [2026-09-07T19:34:40.254Z] TOOL RESULT

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
(eval):1: == not found
```


## [2026-09-07T19:34:52.289Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82n%E1%B8%97r\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B1%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%86%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%CE%B1%CE%BD%CE%AE%CF%81\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 361, root Ner 1: PIE *h2ner, Persian nar/niru/honar, Greek aner\" ; done 2>&1 | tail -20"
}
```


### [2026-09-07T19:34:58.407Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b61ecf755fcb60cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8871a4caa67d39cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aad6b3a3de9d9887.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e97d90088de80132.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/38ee3bd41360fb32.txt
```


## [2026-09-07T19:35:01.876Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"########## PIE h2ner\"; grep -n -A4 -i \"Proto-Indo-European.*h₂nḗr\\|man, hero\\|Descendants\" b61ecf755fcb60cf.txt | head -60"
}
```


### [2026-09-07T19:35:01.926Z] TOOL RESULT

```
########## PIE h2ner
4:TITLE: Reconstruction:Proto-Indo-European/h₂nḗr - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/h₂nḗr - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
10- Main menu 
--
71: Descendants 
72-
73- 1.2 
74- References 
75-
--
78: Reconstruction:Proto-Indo-European/ h₂nḗr 
79-
80- 2 languages 
81-
82- Ελληνικά 
--
241: Proto-Celtic: *nertom ( “ strength ” ) ( see there for further descendants )
242-
243: Descendants
244- [ edit ] 
245-
246: Terms derived from the Proto-Indo-European word *h₂nḗr 
247-
248: Proto-Albanian: *nera ( see there for further descendants )
249-
250- Anatolian:
251- Hittite: 𒅔𒈾𒊏𒉿𒀭𒋫 ( innarawant- ) 
252-
--
267: Proto-Slavic: *norvъ ( “ custom, manner ” ) ( see there for further descendants )
268-
269- Proto-Celtic: *neros , with thematicized full-grade leveled from *h₂nérm̥ ( accusative singular ) 
270-
271- Proto-Hellenic: *anḗr 
--
273: Proto-Indo-Iranian: *Hnā́ ( see there for further descendants )
274-
275: Proto-Italic: *nēr ( see there for further descendants )
276-
277- Phrygian: αναρ ( anar ) 
278-
279- References
--
286: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/h₂nḗr&oldid=92151440 "
287-
288- Categories : Proto-Indo-European lemmas 
289- Proto-Indo-European nouns 
290- Proto-Indo-European masculine nouns 
--
329: Reconstruction:Proto-Indo-European/ h₂nḗr 
330-
331- 2 languages 
332-
333- Add topic
```


## [2026-09-07T19:35:04.989Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '190,245p' b61ecf755fcb60cf.txt"
}
```


### [2026-09-07T19:35:05.028Z] TOOL RESULT

```
 *h₂nérh₁(e) 

 *h₂nérm̥s 

 genitive

 *h₂n̥rés 

 *? 

 *h₂n̥róHom 

 ablative

 *h₂n̥rés 

 *? 

 *h₂nr̥mós , *h₂nr̥bʰós 

 dative

 *h₂n̥réy 

 *? 

 *h₂nr̥mós , *h₂nr̥bʰós 

 locative

 *h₂nér , *h₂néri 

 *? 

 *h₂nr̥sú 

 instrumental

 *h₂n̥réh₁ 

 *? 

 *h₂nr̥mís , *h₂nr̥bʰís 

 Note: an alternative form, *éh₂nōr , and feminine derivation, *h₂nerih₂ , are seen in many Ancient Greek compounds (i.e. -ήνωρ and -άνειρα ), probably reanalysed from archaic compounds.

 Derived terms
 [ edit ] 

 *h₂ner-to- ( “ virile, strong ” ) 
 Proto-Celtic: *nertom ( “ strength ” ) ( see there for further descendants )

 Descendants
 [ edit ]
```


## [2026-09-07T19:35:08.931Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '96,140p' b61ecf755fcb60cf.txt; echo \"#### refs\"; sed -n '279,286p' b61ecf755fcb60cf.txt"
}
```


### [2026-09-07T19:35:08.990Z] TOOL RESULT

```
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

 Noun
#### refs
 References
 [ edit ] 

 ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [1] , 1st edition, Oxford: University Press, →ISBN 

 Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 366 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/h₂nḗr&oldid=92151440 "
```


## [2026-09-07T19:35:11.703Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,160p' b61ecf755fcb60cf.txt"
}
```


### [2026-09-07T19:35:11.753Z] TOOL RESULT

```
 Noun
 [ edit ] 

 *h₂nḗr   m [ 1 ] 

 man 
 Synonym: *wiHrós 

 power , force , vital energy

 Inflection
 [ edit ] 

 Athematic, amphikinetic

 singular

 nominative

 *h₂nḗr
```


## [2026-09-07T19:35:18.040Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 8871a4caa67d39cb aad6b3a3de9d9887 e97d90088de80132; do echo \"######## $f\"; grep -n -i \"Etymology\\|Middle Persian\\|Proto-Iranian\\|Proto-Indo-Iranian\\|Avestan\\|Hasandust\\|inherited\\|borrowed\" $f.txt | head -30; done"
}
```


### [2026-09-07T19:35:19.286Z] TOOL RESULT

```
######## 8871a4caa67d39cb
62: Etymology 1 
68: Etymology 2 
79: Etymology 
96: Etymology 
136: Etymology 1 
145: Etymology 2 
156: Etymology 
236: Etymology 1
248: Etymology 2
263: Etymology
292: Etymology
295: From Middle Persian 𐭦𐭪𐭫 ( ZKL ) , 𐭭𐭫 ( nl /⁠nar⁠/ , “ male ” ) , from Proto-Indo-Iranian *Hnā́ , from Proto-Indo-European *h₂nḗr .
297: Cognate with Pashto نر ( nar, nër ) , Ossetian нӕл ( næl ) , Avestan 𐬥𐬀𐬭 ( nar ) , and Sanskrit नर ( nara ) .
415: Etymology 1
454: Etymology 2
469: Etymology
485: Ottoman Turkish terms borrowed from Persian 
492: Persian terms inherited from Middle Persian 
493: Persian terms derived from Middle Persian 
494: Persian terms inherited from Proto-Indo-Iranian 
495: Persian terms derived from Proto-Indo-Iranian 
496: Persian terms inherited from Proto-Indo-European 
518: Ushojo terms borrowed from Urdu 
525: Middle Persian terms with non-redundant manual transliterations 
526: Middle Persian terms with redundant script codes 
527: Middle Persian terms with redundant transliterations 
######## aad6b3a3de9d9887
62: Etymology 
82: Etymology 
160: Etymology
163: From Middle Persian [script needed] ( nērōg /⁠nylwk’, nyrwg⁠/ ) , from Proto-Iranian *naryawa-ka- ( “ valor, strength ” ) , from Proto-Indo-Iranian *Hnā́ ( “ man ” ) . [ 1 ] 
230: Etymology
252: Categories : Persian terms derived from Middle Persian 
253: Persian terms inherited from Proto-Iranian 
254: Persian terms derived from Proto-Iranian 
255: Persian terms derived from Proto-Indo-Iranian 
271: Hidden categories: Requests for native script for Middle Persian terms 
######## e97d90088de80132
62: Etymology 
82: Etymology 
179: Etymology
182: Borrowed from Classical Persian هُنَر ( hunar , “ art; craft, ability ” ) , from Middle Persian 𐫍𐫇𐫗𐫡 ( hwnr /⁠hunar⁠/ , “ virtue, ability, skill ” ) , ultimately from Old Persian 𐎢𐎺𐎴𐎼 ( ʰuvnara , “ talent, capability ” ) .
242: Etymology
245: Inherited from Middle Persian [Book Pahlavi needed] ( hwnl ) , 𐫍𐫇𐫗𐫡 ( hwnr /⁠hunar⁠/ , “ virtue, ability, skill ” ) , from Old Persian 𐎢𐎺𐎴𐎼 ( ʰuvnara , “ talent, capability ” ) , from Proto-Iranian *hu-nara , from Proto-Indo-European *h₁su- ( “ good ” ) + *h₂nḗr ( “ man; power, force, vital energy ” ) . Cognate with Old Armenian հնար ( hnar , “ means, way ” ) (from Iranian), Avestan 𐬵𐬎𐬥𐬀𐬭𐬀   m ( hunara , “ skill, strength ” ) , Sanskrit सूनर ( sū-nára , “ possessing vital strength, mighty, prosperous, beautiful ” ) and सुन्दर ( sundara , “ beautiful, charming ” ) .
378: Boyce, Mary ( 1977 ), “hwnr”, in A word-list of Manichaean Middle Persian and Parthian (Acta Iranica 9a, Série 3 – “Textes et mémoires”, vol. 2-supplément)‎ [6] , with a reverse index by Ronald Zwanziger, Leiden, Tehran-Liège: E.J. Brill, Bibliothèque Pahlavi, page 49 
398: Categories : Ottoman Turkish terms borrowed from Classical Persian 
400: Ottoman Turkish terms derived from Middle Persian 
405: Persian terms inherited from Middle Persian 
406: Persian terms derived from Middle Persian 
407: Persian terms inherited from Old Persian 
409: Persian terms inherited from Proto-Iranian 
410: Persian terms derived from Proto-Iranian 
424: Requests for Book Pahlavi script for Middle Persian terms 
425: Middle Persian terms with redundant script codes
```


## [2026-09-07T19:35:38.413Z] TOOL CALL #41: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D8%AF%D8%B1%D9%8A%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%83%D9%86%D8%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%CE%91%CE%BB%CE%AD%CE%BE%CE%B1%CE%BD%CE%B4%CF%81%CE%BF%CF%82\" \\\n \"https://www.etymonline.com/word/android\" \\\n \"https://www.etymonline.com/word/philanthropy\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 361, root Ner 1: Idris, Iskandar, Alexandros, android, philanthropy\"; done 2>&1 | tail"
}
```


## [2026-09-07T19:35:39.209Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nayrig\\|nārīg\\|narig\\|nāyrīg\\|nāirika\\|nairika\" SNS_pages.txt SNS.txt | head -20; echo \"@@@ pdf tags near\"; grep -n \"pdf page 26[0-9]\" SNS_pages.txt | head"
}
```


### [2026-09-07T19:35:43.577Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f30a184bd0c11af5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0a42af8d21e886d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4d47d121fbe02174.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/549a9bab1d916dae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/895a998323496a30.txt
```


### [2026-09-07T19:35:43.642Z] TOOL RESULT

```
@@@ pdf tags near
```


## [2026-09-07T19:35:46.669Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c SNS_pages.txt SNS.txt; head -30 SNS_pages.txt; echo \"@@@\"; grep -c \"\" SNS.txt"
}
```


### [2026-09-07T19:35:46.730Z] TOOL RESULT

```
1292394 SNS_pages.txt
 325929 SNS.txt
1618323 total
    A
>l»>'i




 O^t'

        /
« *>&
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -




       and Six indexes

         '




@@@
34173
```


## [2026-09-07T19:35:54.118Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'nayr|nāyr|nayr|yrīg|yrig|nārig|nārīg', p, re.I):\n        print('---- leaf',i)\n        print(p[:600])\nEOF"
}
```


### [2026-09-07T19:35:55.622Z] TOOL RESULT

```
pages 243
---- leaf 56
                                                                                                                                                                                                       j                                       v



                                                              US *~*U *.ii *A                                                                                                     ^-^bj ^i—^L: 4, L a       \
                                                                                                                                                      
---- leaf 150
                                                                                                                                                                     bfc.U.;!,                                            T^r
                               c-jAic— fc**fc*3'3.


                                                                                               ~v w-^— w j-***-**^ j'jS ^ f'j o**^ j^'o*' r'^*"' ***&cw j j,jj
                                                                                                                                                       1




         
---- leaf 229
25                                               Li;^Li*.L y>   ^At tfl**;'* ^-vr»
mahraanih 239/14             mazdist 241/17                     raiySnag 237/12           naxun 258/3
Mahraspand/Maraspand         raazdistan 241/20                  raizag 253/6              nSyrlg 264/19
  240/8                      raazg     243/18                   ra5g   248/1              nayrlg zan 264/24
ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
man 221/1                    mShan 252/17                       ra&r   3sy3nag 248/8      namad 282
---- leaf 239
                                                   U^bo'j   i$}kl <***•& e-j^
 "

                                                            ahravtar/ahlavtar 5/12   an-ahOg 56/8
,i   <\   I.   Tm 25/2          afganSd 228/13
                                                            ahriman/ahrraan 4/17     anar 59/3
 i.a-dld          18/16-20/12   afganend 228/11
                                                            ahrraog 4/9              an-asanlh 58/11
nhft-rjumfln           20/12    afganisn 228/15
                                                            ahunvad/ahuved gah 8/
```


## [2026-09-07T19:36:05.267Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'yrlg|yr1g|nSyr', p):\n        print('---- leaf',i, 'len',len(p))\n        for ln in p.split('\\n'):\n            if re.search(r'yrlg|nSyr|264', ln): print('   >',ln.strip()[:200])\nEOF"
}
```


### [2026-09-07T19:36:06.635Z] TOOL RESULT

```
---- leaf 150 len 8677
   > •       4i^*     cLjI^j^d) :n ayrlg:
   > 6/YT^                 c^LjL     j : nayrlg,              it:
   > •                  •                *   ***** oj           :n3yrlg zan:                      ^feu** aij-«i
---- leaf 229 len 3026
   > Mahraspand/Maraspand         raazdistan 241/20                  raizag 253/6              nSyrlg 264/19
   > 240/8                      raazg     243/18                   ra5g   248/1              nayrlg zan 264/24
   > margarzan vinSh 246/11       mih 243/21                         nam 201/18                naxSzIg 264/7
```


## [2026-09-07T19:36:10.522Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[150]\nls=p.split('\\n')\nfor j,ln in enumerate(ls):\n    if 'ayrlg' in ln:\n        print('\\n'.join(x.strip() for x in ls[max(0,j-4):j+4]))\n        print('=====')\nEOF"
}
```


### [2026-09-07T19:36:11.946Z] TOOL RESULT

```
.A-Y-Y/UJ (Jt-^^e^fHtf^G^JT)

^IrSds     ..-vyd:         *>w"
vt/tJ   -ta/tO                                                                                                                                                                             *&*»*
•       4i^*     cLjI^j^d) :n ayrlg:
nairlk :^                       {AiWb. 1065) nart-:                           ^^
6/TY^ .X»-6/»a^ .fl/'T^ .(ijttsr-.)
nairl-        :      &„
=====
.^:kard:
c gYDWI,t       :>*:       V*«^
0UW>. 444-7)        ttarx^.,— /kari                   ^A ^      ar     :

6/YT^                 c^LjL     j : nayrlg,              it:
(Mrr .Man. 11,57) kyrd: j3ll
•                     .
if_i^3>»**
=====
```


## [2026-09-07T19:36:26.577Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in f30a184bd0c11af5 a0a42af8d21e886d 4d47d121fbe02174; do echo \"######## $f\"; grep -n -i -B2 -A6 \"Etymology\" $f.txt | sed -n '1,70p'; done"
}
```


### [2026-09-07T19:36:27.769Z] TOOL RESULT

```
######## f30a184bd0c11af5
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
156- [ edit ] 
157-
158: Etymology
159- [ edit ] 
160-
161- Uncertain, formally a borrowing, candidates suggested include:
162-
163- Koine Greek Ἀνδρέας ( Andréas ) 
164- one of the apostles of Jesus [ 1 ] [ 2 ] 
######## a0a42af8d21e886d
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Descendants 
--
141- Իսքէնտէր ( İskender ) — Armeno-Turkish 
142-
143: Etymology
144- [ edit ] 
145-
146- Borrowed from Arabic إسْكَنْدَر ( ʔiskandar ) , from Ancient Greek Ἀλέξανδρος ( Aléxandros ) .
147-
148- Proper noun
149- [ edit ] 
######## 4d47d121fbe02174
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
155- [ edit ] 
156-
157: Etymology
158- [ edit ] 
159-
160- Inherited from Ancient Greek Ἀλέξανδρος ( Aléxandros ) .
161-
162- Pronunciation
163- [ edit ]
```


## [2026-09-07T19:36:31.117Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### IDRIS full etym\"; sed -n '158,200p' f30a184bd0c11af5.txt; echo \"#### ISKANDAR (which lang?)\"; sed -n '100,160p' a0a42af8d21e886d.txt"
}
```


### [2026-09-07T19:36:31.192Z] TOOL RESULT

```
#### IDRIS full etym
 Etymology
 [ edit ] 

 Uncertain, formally a borrowing, candidates suggested include:

 Koine Greek Ἀνδρέας ( Andréas ) 
 one of the apostles of Jesus [ 1 ] [ 2 ] 

 and also the immortalized cook of Alexander the Great (the latter being called ذُو الْقَرْنَيْن ( ḏū l-qarnayn ) ) [ 3 ] 

 Ancient Greek Ποιμάνδρης ( Poimándrēs ) , one of the figures in the Corpus Hermeticum [ 4 ] 

 the Koine Greek form Ἔσδρας ( Ésdras ) of Biblical Hebrew עֶזְרָא ( ʿezrā , “ Ezra ” ) , which would make it a doublet of عَازِر ( ʕāzir , “ Ezra ” ) , عُزَيْر ( ʕuzayr , “ Ezra ” ) , and آزَر ( ʔāzar , “ Terah, Abraham’s father ” ) [ 5 ] [ 6 ] 

 Biblical Hebrew דּוֹרֵשׁ ( dōrēš , “ teacher of the Torah ” ) [ 7 ] 

 Islamic theologists took the name as from أَدْرَسَ ( ʔadrasa , “ to teach ” ) from the root د ر س ( d r s ) , in spite of the pattern إِفْعِيل ( ʔifʕīl ) having been unproductive even by the time of Islam, leading to the equation with the biblical Enoch , whose name derives from Biblical Hebrew חינוך ( “ education ” ) . Enoch is generally depicted as a man of science, and is sometimes credited for inventing the art of writing and astronomy.

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʔid.riːs/ 
 ( Morocco ) IPA ( key ) : /ʔid.riːs/ , /driːs/ 

 This entry needs an audio pronunciation . If you are a native speaker with a microphone, please record this word . The recorded pronunciation will appear here when it's ready.

 Proper noun
 [ edit ] 

 إِدْرِيس • ( ʔidrīs )  m 

 ( Islam ) Idris , Idrees , a figure in the Islamic narrative.
 609–632 CE , Qur'an , 19:56 : وَٱذۡكُرۡ فِی ٱلۡكِتَـٰبِ إِدۡرِیسَۚ إِنَّهُۥ كَانَ صِدِّیقࣰا نَّبِیࣰّا wa-ḏkur fī l-kitābi ʾidrīsa ʾinnahū kāna ṣiddīqan nabiyyan And mention in the Book, Idrees . Indeed, he was a man of truth and a prophet. 

 a male given name 

 Declension
 [ edit ] 

 Declension of noun إِدْرِيس ( ʔidrīs )

 singular

#### ISKANDAR (which lang?)
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

 Ottoman Turkish
 [ edit ] 

 Alternative forms
 [ edit ] 

 Իսքէնտէր ( İskender ) — Armeno-Turkish 

 Etymology
 [ edit ] 

 Borrowed from Arabic إسْكَنْدَر ( ʔiskandar ) , from Ancient Greek Ἀλέξανδρος ( Aléxandros ) .

 Proper noun
 [ edit ] 

 اسكندر • ( İskender ) 

 Alexander the great
 Synonyms: اسكندر ماكدونی ( İskender-i Makedoni ) , اسكندر ابن فیلقوس ( İskender ibni Filikos ) 

 a male given name from Arabic, equivalent to English Alexander 
 Synonyms: علكساندر , آلكساندر 

 Descendants
 [ edit ]
```


## [2026-09-07T19:36:39.434Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%AF%D8%B1\" --note \"page 361: Persian Eskandar\" ; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1\" --note \"page 361: Arabic al-Iskandar\""
}
```


## [2026-09-07T19:36:40.808Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### android\"; grep -n -A12 \"^ android\" 549a9bab1d916dae.txt | head -30; echo \"#### philanthropy\"; grep -n -A12 \"philanthropy (n\" 895a998323496a30.txt | head -30"
}
```


### [2026-09-07T19:36:42.815Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cb5838a3a392505b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5b346f8ead13c05.txt
```


### [2026-09-07T19:36:42.881Z] TOOL RESULT

```
#### android
23: android (n.) 
24-
25- "automaton resembling a human being in form and movement," 1837, in early use often in reference to automated chess players, from Modern Latin androides (itself attested as a Latin word in English from 1727), from Greek andro- "man" (from PIE root *ner- (2) "man") + -eides "form, shape" (see -oid ). Greek androdes meant "like a man, manly;" compare also Greek andrias "image of a man, statue." Listed as "rare" in OED 1st edition (1879), popularized from c. 1950 by science fiction writers.
26- also from 1837 
27-
28- Entries linking to android 
29-
30- droid (n.) 
31-
32- popularized from 1977, short for android . It is attested in a science fiction story from 1952.
33-
34- *ner- (2) 
35-
--
122: android 
123- Andromache 
124- Andromeda 
125- andron 
126- androphagous 
127- androphobia 
128-
129- Advertisement Close 
130- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
131-
132- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
133-
134- Close 
#### philanthropy
23: philanthropy (n.) 
24-
25- "love of humankind, especially as evinced in deeds of practical beneficence and work for the good of others," c. 1600, from Late Latin philanthropia , from Greek philanthrōpia "kindliness, humanity, benevolence, love to mankind" (from gods, men, or things), from philanthrōpos (adj.) "loving mankind, useful to man," from phil- "loving" (see philo- ) + anthrōpos "mankind" (see anthropo- ). Originally in English in the Late Latin form; the modern spelling in English is attested from 1620s.
26- also from c. 1600 
27-
28- Entries linking to philanthropy 
29-
30- philanthrope (n.) 
31-
32- "a philanthropist," 1734, from Latin philanthropos , from Greek philanthrōpos "loving mankind, humane" (see philanthropy ).
33-
34- philanthropic (adj.) 
35-
```


## [2026-09-07T19:37:04.034Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### Persian اسکندر\"; grep -n -i -A8 \"Etymology\" cb5838a3a392505b.txt | sed -n '1,60p'; echo \"#### Arabic الإسكندر\"; grep -n -i -A8 \"Etymology\" d5b346f8ead13c05.txt | sed -n '1,40p'"
}
```


### [2026-09-07T19:37:04.115Z] TOOL RESULT

```
#### Persian اسکندر
73: Etymology 
74-
75- 2.3 
76- Pronunciation 
77-
78- 2.4 
79- Proper noun 
80-
81- 2.4.1 
--
178: Etymology
179- [ edit ] 
180-
181- Inherited from Middle Persian [script needed] ( swkndl /⁠Skandar ~ Sokandar⁠/ ) , [ 1 ] [ 2 ] from Arabic إِسْكَنْدَر ( ʔiskandar ) , from Ancient Greek Ἀλέξανδρος ( Aléxandros ) .
182-
183- Pronunciation
184- [ edit ] 
185-
186- ( Classical Persian ) IPA ( key ) : /ʔis.kan.ˈdar/ 
#### Arabic الإسكندر
62: Etymology 
63-
64- 1.2 
65- Proper noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
--
138: Etymology
139- [ edit ] 
140-
141: Etymology tree
142-
143- Proto-Indo-European *h₂lek- 
144-
145- Proto-Indo-European *-seti 
146-
147- Proto-Indo-European *h₂lékseti 
148- Proto-Hellenic *aléksō der. 
149- Ancient Greek ᾰ̓λέξω ( ăléxō ) 
--
245: Pages with etymology trees 
246: Arabic entries with etymology trees 
247: Arabic entries with etymology texts 
248- Pages using etymon with no ID 
249- Arabic terms with redundant transliterations 
250- Pages with entries 
251- Pages with 1 entry 
252-
253- This page was last edited on 24 June 2026, at 06:49.
254-
255- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy.
```


## [2026-09-07T19:37:07.934Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '143,185p' d5b346f8ead13c05.txt; echo \"@@@ MP refs for eskandar\"; grep -n -A3 \"MacKenzie\\|Hasandust\\|Nyberg\\|references\" cb5838a3a392505b.txt | sed -n '1,40p'"
}
```


### [2026-09-07T19:37:07.992Z] TOOL RESULT

```
 Proto-Indo-European *h₂lek- 

 Proto-Indo-European *-seti 

 Proto-Indo-European *h₂lékseti 
 Proto-Hellenic *aléksō der. 
 Ancient Greek ᾰ̓λέξω ( ăléxō ) 

 Proto-Indo-European *h₂nḗr 
 Proto-Hellenic *anḗr 
 Ancient Greek ᾰ̓νδρ- ( ăndr- ) 

 Proto-Indo-European *-os 
 Proto-Hellenic *-os 
 Ancient Greek -ος ( -os ) 

 Ancient Greek Ἀλέξανδρος ( Aléxandros ) bor. 
 Arabic الإسكندر 

 Borrowed from Ancient Greek Ἀλέξανδρος ( Aléxandros ) . The initial Ἀλ- was reanalyzed by Arabic speakers as the Arabic definite article ال ( al- ) .

 Proper noun
 [ edit ] 

 الْإِسْكَنْدَر • ( al-ʔiskandar )  m 

 Alexander 
 الْإِسْكَنْدَر الْأَكْبَر ― al-ʔiskandar al-ʔakbar ― Alexander the Great 

 Declension
 [ edit ] 

 Declension of noun الْإِسْكَنْدَر ( al-ʔiskandar )

 singular

 basic singular triptote 

 indefinite

 definite

 construct
@@@ MP refs for eskandar
282: ^ Nyberg, H. S. ( 1974 ), “Sokandar”, in A Manual of Pahlavi, Part II: Glossary , Wiesbaden: Otto Harrassowitz, page 177 , 
283-
284: ^ MacKenzie, D. N. ( 1971 ), “*Skandar”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 75 
285-
286- Retrieved from " https://en.wiktionary.org/w/index.php?title=اسکندر&oldid=88094914 "
287-
```


## [2026-09-07T19:37:24.212Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### PHD Skandar\"; grep -n \"Skandar\\|skandar\" PHD.txt | head -5; echo \"#### PHD nerog entry\"; grep -on \"n.r.g \\[n(y)lwk\\|nylwk\\|nyrwk\" PHD.txt | head; grep -n \"nērōg\\|nērōg\\|nyrwg\" PHD.txt | head -5; echo \"#### NYB Sokandar\"; grep -n \"Sokandar\\|sokandar\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-07T19:37:24.303Z] TOOL RESULT

```
#### PHD Skandar
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
5509:snóy déwók sanwar dēnūdag 1-356g sūgand Skandar sūfistā Sūšyans sor, sür sūrāx stirigomand sūrāg sūragīg
#### PHD nerog entry
510:nylwk
538:nylwk
510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
#### NYB Sokandar
3461:Sokandar [swkndl] = Alaksandar, 113}. 1145. — Probably the Arab. Iskandar with elision of %- and inserting of an auxiliary vowel between s and k, cf Sikandar < Iskandar.
```


## [2026-09-07T19:37:33.835Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,80p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T19:37:33.908Z] TOOL RESULT

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
```


## [2026-09-07T19:37:39.481Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"ner-\\|nert\" WLD_Bd2_pages.txt | grep -n -i \"mann\\|kraft\" | head -10"
}
```


### [2026-09-07T19:37:39.531Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
14:11128:85 m.          Lit.   (gegen anl, *w r-    2     s.    auch      u.    7ner-   ^flimmem'^),       Trautmann
30:21972:1. ner-,  aner- (aner-?) Mann.
32:22005:   air. nert i^ner-to-m), cymr. corn, nertli ,jMannhaftigkeit'*, bret. ^r^„Kraft“,
```


## [2026-09-07T19:37:40.329Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"ادریس\" MON_part1.txt MON_part2.txt; grep -c \"اسکندر\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-07T19:37:40.409Z] TOOL RESULT

```
MON_part2.txt:1
MON_part1.txt:0
MON_part2.txt:2
MON_part1.txt:6
```


## [2026-09-07T19:37:44.276Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '21965,22015p' WLD_Bd2_pages.txt; echo \"@@@ page tag\"; awk 'NR<=21972 && /\\[pdf page/ {l=$0; n=NR} END{}' WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<21972' | tail -2"
}
```


### [2026-09-07T19:37:45.658Z] TOOL RESULT

```
,,W6lbung“ hieher, 8ondern nach Duvau Rc. 22, 82f., Pederaen KG. I 255,
387 mit schon air. y iiiv f = abg. mbo.
   S. Pick I* 97, II^ 192, III* 294 und bes. Curtius 313f., Johansson IP. 2,
54 ff. mit Lit., der aber nicht iiberzeugend auch ai. ndka- m. „Himmels-
w61bung“, gr. vdnrj, vdnog „Tal, Waldschlucht“ heranzieht.


1. ner-,  aner- (aner-?) Mann.
   Ai. ndr- {nd) „Mann, Mensch“, av. nar- {na) ds. (ai. nara-h, av. nara-
nach dem Acc. naram, nardm neugebildet) ai. wdn, av. ncdri „Frau“ (erst
                                                    ;



ar. Pemininbildung); ai. narya-, av. nairya- „mannhaft, maniilich“; wohl
auch ai. sunara- (dial, jiinger sundara-) ..freigebig, freundlich, wonnig, sch6n“
(wenn eigentlich „ein guter Mann“, s. Oldenberg ZdiuG. 50, 442; bezweifelt
von Bartholomae Altiran. Wb. 1831), av. Tivnara- m. „Konneii, Kunst, Kunst-
fertigkeit, Tiichtigkeit*' (ware ursprgl. „virtus“, dann „virtuosite“, vgl. unten
arm. arvest), ai. sunrta „Freigebigkeit, Freundlichkeit, Wonne“ (eine Zs.
mit sii- bietet auch das kelt.: air. so-nirt, cymr. hy^nerth „tapfer, stark“);
   arm. a/r, gen. arn „Mann, Mensch'^ (z. Lautlichen s. Pedersen KZ. 39,
353, 407), aril „mannlich'‘ {-ii aus -opa nach Pedersen aaO. 389? gr. dg-coiy,
8. u., ist aber darum doch nicht mit idg. p anzusetzen), wo von arvtst, arhest

 ,Kimst“ (z. Bed. s. o.);
   gr. dvYiQ, “fpa, dvdgog „Mann‘^, proger] „Mannhaftigkeit“ (Horn.  ?)- metr.
                                                                           ;


Dehnung), avdgeiog „mannhaft, mutig“, dyi]v(jdg „mutig“ dg-d)ip* av^gcojiog
(*vg-o)ip ..Mannesantlitz habend“); alb, n'er „Mann, Mensch“ (G. Meyer
        8,   190, Alb. Wb. 313);
     lat.          „resistens, fortis“, Nerio, -ienis „eine mit Mars in Kult-
             neriostis
verbindung stehende Gottin^^ (*die Starke^), Nero^ sabinisch = „forti8 ac
sbenuus'* (s. v. Planta II 593, Ernout EL dial. lat. 201 fF., und iiber andere
Namen von diesem Stamme Schulze Eigenn. 315, 363, 485; sabin. Nerms
stimmte zu ai. narya-), osk. niir g. pi. nerum, „vir, procer“, umbr. nerus
d. pi., nerf a. pi. ,,proceres, principes‘‘;
   air. nert i^ner-to-m), cymr. corn, nertli ,jMannhaftigkeit'*, bret. ^r^„Kraft“,
gall. Nerto-briga, Esu^iertus usw., air. nertaim „ich starke‘^, cymr. nerihu
 „starken, unterstiitzen^, bret.    nerm „festigen“.
     Z. B. Curtius^ 306 f., Pick I^ 98, 275, 502, II ^ 193.        — Ai. Jndra-h aus
 HnrosV. (Jacobi KZ. 31, 3 16 If., anders, doch auch kaum glaublich, Liden
 S. 58). Gegen Heranziehung von germ. Nerthus, anord. Njordr (Pick)
                                               ner-                                     333


8. Noreen Ltl. 209 (: vigregog ^unterirdisch^^.
                                                            —
@@@ page tag
```


## [2026-09-07T19:37:56.110Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \".\\{80\\}ادریس.\\{120\\}\" MON_part2.txt | head -3; echo \"@@@\"; grep -n -o \".\\{60\\}اسکندر.\\{100\\}\" MON_part1.txt | head -6"
}
```


### [2026-09-07T19:37:56.205Z] TOOL RESULT

```
@@@
```


## [2026-09-07T19:38:00.172Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ('ادریس','اسکندر'):\n        for m in re.finditer(w,t):\n            print(f,w,repr(t[max(0,m.start()-120):m.start()+150]))\n            print('---')\nEOF"
}
```


### [2026-09-07T19:38:01.455Z] TOOL RESULT

```
MON_part1.txt اسکندر 'از» انکار \nکننده. \n\nابیات: ی سبت. خانه\u200cها. \nفردها از شعر \n\nبیاری: 1 ۸1571 (ص\u200cنسب.) منسوب به ابیار \n(دیهی است میان مصر و اسکندریه). دیبایی \nمخطط و راه راه» لطبف و نازک بافته و \nبهترین آن ایباری کافوری بوده است. نوعی \nکبوتر. نوعی پرستو. \n\nاییب: «آده [معر.] (ا.) نامی است ک'
---
MON_part1.txt اسکندر '(گیا.) درختجه\u200cای \nاز سیرة ترشک\u200cها (هصفت\u200cندها) که در \nسواحل آفریقا و آسیای مرکزی و غربی \nمی\u200cروید» بتوء رسوء ارطی» ارته. \nاسکندروس: کتتالنصايه اظ. محر.] 0( \n(کٌیا.) سیر. \n\nاسکنه: (م-2جع۲ب [- اسکنک ] (.) (نج.) \nآلتی که نجاران چوب را به وسیلة آن \nسوراخ کنند؛ بیرم. \n\nاسکنه: '
---
MON_part1.txt اسکندر ' جایی که متهمان و \nمحکومان را در آن نگاه دار ند؛ بندی خانه» \nمحس» قیدخانه. زندان خاموشان: (کن.) \nگور؛ قبر. زندان سکندر (اسکندر): شهر \n( بر د). ( کد.) طلمات. \n\nزندانبان: 2۰-0 (رص مر .) آنکه در محس \nمأمور نگاهانی محوسان است» نگهبان \nزندان. \n\nزندانی: آ-761037 (ص\u200cنسه.) کسی '
---
MON_part1.txt اسکندر 'امک و \nمحتوی چند دانه است. میوه و برگک مختلف \nسنا دوای تلخ مسهلی است که بصورت دم \nکرده يا پودر بکار می\u200cرود» عشرق. سنای \nاسکندری: (گیا.) گونه\u200cای سنا که در مصر و \nسودان و اطراف نیل (در نواحی کوهستانی \nشمال و مغرب خرطوم) به حد وفور \nمی\u200cرو ید و و یکی از انواغ سناهای دارویی '
---
MON_part1.txt اسکندر 'ای مختلف است. \nسنای مکی» سنای حجازی» مهار» سنای \nمکی آغاجی؛ سنه مکی. سنای بری: (گیا.) \nقدقدک. سنای حجازی: (گنیاء) سنای \nاسکندربه. سنای مکی: (گیا.) سنای \nاسکندر به. سنای هندی: (گیا.) گونه\u200cای سنا \nکه بحد وفور در عربستان و آفریقا و سواحل \nسومالی تا موزامبیکك می\u200cروید ولی ام'
---
MON_part1.txt اسکندر 'زی» مهار» سنای \nمکی آغاجی؛ سنه مکی. سنای بری: (گیا.) \nقدقدک. سنای حجازی: (گنیاء) سنای \nاسکندربه. سنای مکی: (گیا.) سنای \nاسکندر به. سنای هندی: (گیا.) گونه\u200cای سنا \nکه بحد وفور در عربستان و آفریقا و سواحل \nسومالی تا موزامبیکك می\u200cروید ولی امروز \nبیشتر در جنوب هندوستان کشت م'
---
MON_part2.txt ادریس 'لب: ۱۱۵2 [ع. .( انگبین. \nمحلب: حادا ۵ [ع.] .۲ (گیا.) تین از \nگونه\u200cهای آلبالو است که آن را آلبالوی تلخ: \nپیوند مریم» شجر ادریس نیز گویند. \nمحلب: 3( [ع. ۰ | (1.) ظرفی که در 1 \nشبر دو شند؟ ۳ محالت. \nمحلت: ۲( ك . محله ] ( ۰) جای فر و د \nام رمان فر ود آمدن. 1 مقام؛ جای \nباش.'
---
MON_part2.txt اسکندر 'لید و بی\u200cشرم. \n\nهستاکی: ۲:5 (ع. ف.] (حامص.) \nپرده\u200cدری. بی\u200cشرمی» بی\u200cحیایی. \n\nهتر:. ۲ ([دو ست] (.) بخشی از سیاهیان \n\n\nره \nاسکندر مقدونی که افراد آن از صنف \nسواره نظام و از حیث قوت جسمانی و \nقدرت جنگی و فنون آ نف نان وگن \nصنوف ممتاز بو دند. \nهتف: ۷ (ع.] (سصل.) بانگ کردن. \n'
---
MON_part2.txt اسکندر 'نه» چینی کهنه). \n\nهفت\u200cگنجینه: (۵-)32] ۱۰-۵201 (امر.) ( کد.) \nطلاء نقره» قلعی» سرب» آهن» مس» بر نج. \nضح. خان آرزو در شرح اسکندرنامه نوشته \nکه رسم سلاطین ايران بود که هفت جا خزانه \nمی\u200cداشتند یا آنکه هفت گنجینه مراد از هفت \nکونه بخشش بادشاهان باشد و آن هفت این \nاست: اول نق'
---
```


## [2026-09-07T19:38:10.669Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://vajehyab.com/moein/%D8%A7%D8%AF%D8%B1%DB%8C%D8%B3\" --note \"page 361: Mo'in on Edris (MON5:109 check)\" ; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%D8%B3%DA%A9%D9%86%D8%AF%D8%B1/\" --note \"page 361: Mo'in on Eskandar (MON5:144 check)\""
}
```


### [2026-09-07T19:38:14.022Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0d1c9bfd5067b3a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7583dfea2c3f70a9.txt
```


## [2026-09-07T19:38:17.391Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### vajehyab edris\"; grep -n \"ادریس\\|معین\" 0d1c9bfd5067b3a5.txt | head -20; echo \"#### abadis eskandar\"; grep -n \"معین\" 7583dfea2c3f70a9.txt | head -10"
}
```


### [2026-09-07T19:38:17.451Z] TOOL RESULT

```
#### vajehyab edris
#### abadis eskandar
168: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-07T19:38:27.107Z] TOOL CALL #62: Bash

```json
{
 "command": "ls site/pages/361.jpg 2>/dev/null; pdftoppm -f 361 -l 361 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg361 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:38:28.744Z] TOOL RESULT

```
site/pages/361.jpg
total 31916
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:38 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:38:34.418Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg361.png"
}
```


### [2026-09-07T19:38:34.850Z] TOOL RESULT

```

```


## [2026-09-07T19:38:34.849Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:38:57.949Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg361.png')\nprint(im.size)\n# crop region of the empty box: x ~ 940..1310, y ~ 440..520 in displayed 1545x2000 -> scale\nw,h=im.size\nsx=w/1545.0; sy=h/2000.0\nbox=(int(900*sx),int(430*sy),int(1330*sx),int(530*sy))\nim.crop(box).resize((int((box[2]-box[0])*2.5),int((box[3]-box[1])*2.5))).save('p361_empty2.png')\n\"; ls -la p361_empty2.png"
}
```


### [2026-09-07T19:38:59.381Z] TOOL RESULT

```
(1700, 2200)
-rw-rw-r-- 1 sfmqrb sfmqrb 4789 Sep  7 15:38 p361_empty2.png
```


## [2026-09-07T19:39:02.712Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p361_empty2.png"
}
```


### [2026-09-07T19:39:02.727Z] TOOL RESULT

```

```


## [2026-09-07T19:39:31.100Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### KNT\"; grep -n -i \"huvnara\\|hunara\" KNT.txt | head -5; echo \"#### LKT\"; grep -n -i \"iskandar\\|idris\\|alexand\" LKT.txt | head -8; echo \"#### AFM\"; grep -n \"الإسكندر\\|إسكندر\\|إدريس\" AFM_pages.txt | head -5; echo \"#### KLN Idris/Enoch\"; grep -n -i \"Enoch\\|Idris\" KLN_1966.txt | head -5"
}
```


### [2026-09-07T19:39:31.183Z] TOOL RESULT

```
#### KNT
5218:twnara- sb. ‘skill, accomplishment’: ad}. form- ation to pAr. *su- ‘good’ + *nar- ‘man’ (§142, 5148.1, V), = ‘having the good quality of a man’, Av. hunara- ‘ability, skill’, Skt. sümára- ‘glad, joyous, merry’, with vriddhi of the first vowel in OP and Skt. to show the derivative nature (523.11, $126: Lg. 15.173, JNES 4.51-2: cf. Hz. RHRel. 113.30, ApI 200-6, who aecepts this meaning but seeks another etymology, as does also Pisani, Riv. Stud. Or. 19.93-4). düvnarü npn. DNb 45, 51. üwnaraibis ipn. DNb 48.
#### LKT
41:Die  weitaus  bedeutsamste  Verbindung  des  Morgen-  und  Abendlandes im  Altertum  wurde,  wenn  von  einer  Besprechung  der  Wirkung  der  Perser- kriege in  sprachlicher  Hinsicht  abgesehen  werden  darf,  durch  den  Zug Alexanders  des  Großen  hervorgerufen.  Bis  auf  diese  Zeiten  läßt  sich  der erste  reichlichere  Abfluß  orientalischer  Begriffe  und  Wörter  in  die  griechische Sprache  und  in  den  darauf  folgenden  Jahrhunderten  ins  Latemische  zurück- führen; seitdem  erstreckt  sich  die  Wirkung  in  ununterbrochenem  Flusse bis  auf  die  heutigen  modernen  Sprachen  und  Dialekte  Europas.  Das  folgende hellenistische  Zeitalter  begünstigte  aus  hier  nicht  zu  erörternden  Gründen die  Entlehnung  orientalischen  Sprachgutes  in  hervorragendem  Maße:  die Verbreitung  des  Judentums  und  die  Entstehung  des  Christentums  gaben Anlaß  zur  Übernahme  vieler  hebräischer  und  aramäischer  Wörter  ins Griechische  und  Lateinische  [besonders  in  die  als  Kichenlatein  bezeichnete Färbung].  Mit  dem  Mittelalter  beginnt  der  Einfluß  des  Arabischen.  Nach- dem sich  der  Islam  von  den  malayisclien  Inseln  bis  zu  den  Gestaden  des Atlantischen  Ozeans  verbreitet  hatte,  war  eine  riesige  Berührungslinie  des arabischen  Sprachgebiets  mit  dem  Abendlande  geschaffen.  Der  Wortschatz der  Sprachen  der  Pyrenäenhalbinsel,  des  Spanischen,  Portugiesischen  und Katalanischen,  und  in  geringerem  Umfange  anch  der  des  ProvenzaHschen, Französischen  und  Italienischen  werden   mit  arabischen   Wörtern  derart
892:Auch  berün  'außen,  heraus'  [Horn NpEt  S.  58,  Nr.  252] ;  hieraus  ein  Adj. mit  ar.  Endung  blrünl  'draußen  woh- nend', mit  ar.  Art.  al-blrünl  'der  Vor- städter'. Diesen  Beinamen  erhielt,  weil in  einer  Vorstadt  von  Huärizm  [s.  hier Nr.  890]  geboren,  der  berühmte  Poly- histor und  fruchtbare  Schriftsteller  Aba Raihän  Muhammad  ihn  Ahmad  al-Bi- runi,  ein  Zeitgenosse  Avicennas  [973  bis 1048,  vgl.  C.  Brockelmann,  Geschichte der  ar.  Literatur.  Leipzig  1901.  S.  166  u. 167,  wo  allerdings  die  überragende  Be- deutung des  Mannes  m.  E.  nicht  genü- gend gewürdigt  ist;  Alexander  Baum- gartner, Geschichte  der  Weltliteratur. Freiburg  1901.  I,  384].  Nach  der  an- sprechenden Vermutung  DEVICS  ist hieraus  frz.  alihoron  zur  Bezeichnung eines  fast  wunderbaren  Gelehrten  und Propheten,  einer  ganz  hervorragenden Persönlichkeit  geworden;  schließlich  er- hielt frz.  aliboron  die  Bedeutung  'Esel'. [Devic  DEt  20/22.  Lammens  Rem  273/4.
1109:'Tee';  cha-ye  'Teeblätter'  [so  ist  die Aussprache  im  Kuan-hoa,  s.  hier  Nr.  1400, und  im  Kantondialekt];  hieraus  pg.  chä, sp.  (selten)  cha,  russ.  cai,  bulg.  caj,  serb. iaj,  sej,  öech.  caj,  poln.  czajnik  ('Tee- kanne'), czaj.  —  Im  Dialekt  von  Amoy, von  wo  aus  vermutlich  die  ersten  Tee- ladungen ausgegangen  sind,  wird  etwa te  gesprochen,  daher  frz.  the,  sp.  te,  it. U  [seltener  ciä],  ndl.  thee,  dtsch.  Tee, engl,  tea  [früher  wie  im  Deutschen  aus- gesprochen, vgl.  die  beweisenden  Reime in  dem  1712  geschriebenen  Rape  of  the Lock  von  Alexander  Pope,  Canto  I,  61 u.  62;  III,  7/8;  etwa  in  der  Ausgabe Pandora  Nr.  11  (Inselverlag  Leipzig), S.  10  u.  2.3].  Übrigens  hat  das  Neu- griechische beide  Aussprachen  über- nommen :  TOai  und  Teiov.  [Nichts  mit engl,  tea  zu  tun  hat  erigl.  tee-totaller 'Abstinenzler';  dies  ist  vielmehr  die Aussprache  der  Abkürzung  T.  total, d.  h.  temperance  total.]  [Gorjajew  407. Bern  SlEtWb  134.   Hirth  ChinFW  201.
1306:Lateinische  Form  des  hebr.  dawid;  N. pr.,  Name  eines  berühmten  Königs  von Israel  [das  Wort  bedeutet  eigenthch 'Liebhng'i  BAUER  in  ZDMG  LXXI, 411];  hieraus  afrz.  davit,  nfrz.  davie, davier  'Zahnzange'  [Romania  XXXIII, 344],  frz.  david  Name  des  'Schippen- königs' im  Kartenspiel.  —  Zu  engl. taffg  verderbt,  die  Bezeichnung  für  den Waliser  [wie  Paddy  für  den  Iren,  Saw- neij  für  den  Schotten;  ersteres  aus Pafrick,  letzteres  aus  Alexander].  [ML 2487.
4182:'Haupt  des  Heeres'  [eigentlich  mit  pers. Genitivverbindung  i :  sär-i-üskär  aus  sä»- 'Haupt,  Kopf  und  ar.  'askar  'Heer, Soldat'  <^  lat.  exercitus  mit  vorgeschla- genem 'ain  und  Metathesis  von  k  und  s wie  in  ar.  Iskandar  <^  Alexander],  tk. seraakjer  alter  Titel  des  'Generalissimus der  osmanischen  Streitmacht';  hieraus in  gleicher  Bedeutung  rum.  serascher, seraschier,  frz.  sirasker,  sSrasquier; dtsch.  Seraskier,  engl,  seraskier  'Kriegs- minister'.
#### AFM
#### KLN Idris/Enoch
4075:Gk.  x'jcrj'.y.o?,  fr.  a’j'r,Tcic,  ‘that  may  be  in¬ creased',  verbal  adj.  of  a’j'xvsiv.  See  auxano-. Derivative:  auxetical-ly,  adv. auxiliary,  adj.  —  L.  auxilidris ,  helpful ,  fr.  auxi- lium,  ‘help,  aid,  assistance,  support’,  which  is rel.  to  augere.  pp.  auetus ,  ‘to  increase  .  See  auc¬ tion  and  adj.  suff.  -ary.
6841:caulescent,  adj.,  having  a  visible  stem.  —  Formed fr.  L.  caulis,  ‘stalk,  stem’,  with  the  inchoative suff.  -escent,  on  analogy  of  arborescent.  See cole  and  cp.  next  word.  Cp.  also  acaulescent. cauliflower,  n.  —  Refashioned  after  L.  caulis, ‘stem’,  and  E.  flower  fr.  earlier  colyflory,  fr.  F. chou-fleuri,  chou-fleur,  which  is  formed  on  ana¬ logy  of  It.  cavolo  fiore,  ‘cauliflower’,  fr.  L.  caulis, ‘stem,  stalk’,  and  flos,  gen.  /Idris,  ‘flower’.  See cole.
13216:Enoch,  masc.  PN.;  1)  the  eldest  son  of  Cain; 2)  the  father  of  Methuselah  (Bible).  —  Late  L. Enoch,  fr.  Gk.  ’Evciy,  fr.  Heb.  HanSkh,  lit.  ‘de¬ dicated,  consecrated’,  fr.  hanakh,  ‘he  dedicated, consecrated’,  whence  also  hanukkdh,  ‘dedicat¬ ion’,  consecration’.  See  Hanukkah. enorm,  adj.,  1)  abnormal  (obsol.)-,  2)  enormous; outrageous  (archaic).  —  F.  enorme,  fr.  L.  endr- mis,  ‘irregular,  unusual,  enormous,  immense’,  fr. e  norma ,  ‘out  of  rule’,  fr.  e,  ‘out  of’  (see  e-),  and norma,  abl.  of  norma,  ‘rule,  pattern’.  See  norm, enormity,  n.  —  F.  enormite,  fr.  L.  enormitatem, acc.  of  enormitas,  ‘hugeness,  vastness',  fr.  endr- mis.  See  prec.  word  and  -ity. enormous,  adj.  —  Formed  with  suff.  -ous  fr.  L. enormis.  See  enorm.
13221:Derivatives :  enormous-ly,  adv, ,  enormous-ness ,  n. Enos,  masc.  PN. ;  in  the  Bible,  son  of  Seth.  — Gk.’Evco?,  fr.  Heb.  EnSsh ,  lit.  ‘man’,  rel.  to  Heb. nashtm,  ‘women’,  ish  (for  insh),  ‘man’,  Arab. ins  (coll.),  ‘men,  people’,  and  prob.  also  to Arab,  anisa,  ‘he  joined,  was  friendly’,  Akkad. eneshu,  to  unite,  join  (intr.) enough,  adj.  —  ME.  inogh,  enogh,  enouh,  fr.  OE. genoh,  rel.  to  OS.  ginog,  ON.  gnogr,  Swed.  nog, Dan.  nok,  OFris.  enoch,  Du.  genoeg,  OHG.  ginu- og(i ),  MHG.  genuoc,  G.  genug,  Goth,  ganohs, ‘enough’,  OE.  geneah,  OHG.  ginah,  Goth .ganah, ‘it  suffices’,  fr.  I.-E.  base  *enek-,  *nek-,  *nk-,  ‘to reach,  attain,  carry’,  whence  also  OI.  asndti, Avestic  ashnaoiti,  ‘reaches,  arrives  at’,  OI.  na- sati,  Avestic  nasaiti,  ‘reaches’,  OI.  drpsah, ‘portion,  part’,  Avestic  qsa-,  ‘party’,  Hitt,  nakish, ‘heavy’,  nikzi,  ‘rises’,  ninikzi,  ‘lifts,  raises’,  Gk. Jv-eyxeiv,  ‘to  bear,  carry’,  Srqvejo)?,  Att.  Siocve- y.ric,  ‘continuous,  unbroken’  (which  are  prob.  a contraction  of  *§ta-Tr)vexir)q  and  lit.  mean  ‘capa¬ ble  of  being  carried  through’,  fr.  8ia,  ‘through’, and  4veyxstv,  ‘to  carry’),  Syxo?,  ‘bulk,  size,  mass, body’,  L.  nancisci  (for  na-n-c-isci),  perf.  nactus sum,  ‘to  reach,  obtain’,  OSlav.  nesg,  nesti,  Lith. nesu,  nHsti,  Lett,  nesu,  nest,  ‘to  bear,  carry’, Lith.  nastd,  ‘burden’,  and  perh.  also  Toch.  A ents-,  B  enk-,  ‘to  seize,  take’.  Cp,  onco-,  ‘bulk, size’.
14347:Derivatives:  fame,  tr.  v.,  fam-ed,  adj. familiar,  adj.  —  OF.  (=  F.)  familier,  fr.  E.fami- lidris,  ‘pertaining  to  a  household,  domestic', dissimilated  fr.  *familia-lis,  fr.  familia,  ‘house¬ hold’.  See  family  and  adj.  suff.  -ary. Derivatives:  familiar,  n.,  familiar-ism,  n.,  fami¬ liarity  (q.v.),  familiar-ize,  tr.  v.,  familiar-iz- ation,  n.,  familiar-iz-er,  n.,  familiar-ly,  adv. familiarity,  n.  —  F.  familiarite,  fr.  L.  familidri-
```


## [2026-09-07T19:39:31.819Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%86%D8%B1%DB%8C%D9%85%D8%A7%D9%86\" --note \"page 361: Persian Nariman < Av. nairemanah-\""
}
```


### [2026-09-07T19:39:33.293Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c766023574d8d307.txt
```


## [2026-09-07T19:39:42.926Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A8 -i \"etymology\" c766023574d8d307.txt | sed -n '1,40p'"
}
```


### [2026-09-07T19:39:42.976Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
--
149: Etymology
150- [ edit ] 
151-
152- From Middle Persian (compare Manichaean Middle Persian nrymʾn ( narēmān ) ), from Avestan 𐬥𐬀𐬌𐬭𐬈⸱𐬨𐬀𐬥𐬀𐬢𐬵 ( na i re.manaŋh , “ manly-hearted ” ) , compound of 𐬥𐬀𐬌𐬭𐬌𐬌𐬀 ( na i riia , “ brave, manly ” ) and 𐬨𐬀𐬥𐬀𐬢𐬵 ( manaŋh , “ thought, mind ” ) .
153-
154- Pronunciation
155- [ edit ] 
156-
157- ( Classical Persian ) IPA ( key ) : /na.riː.ˈmaːn/
```


## [2026-09-07T19:40:04.796Z] TOOL CALL #69: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T19:40:04.838Z] TOOL RESULT

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


## [2026-09-07T19:40:24.226Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -8 38ee3bd41360fb32.txt; grep -n -i \"Ancient Greek\\|Etymology\" 38ee3bd41360fb32.txt | head"
}
```


### [2026-09-07T19:40:24.280Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%CE%B1%CE%BD%CE%AE%CF%81
FETCHED: 2026-09-07T19:34:58Z
STATUS: 200
TITLE: ανήρ - Wiktionary, the free dictionary

ανήρ - Wiktionary, the free dictionary 

 Jump to content 
139: ( archaic ) the Ancient Greek ἀνήρ ( anḗr , “ man ” ) typed in monotonic script in modern texts
```


## [2026-09-07T19:40:28.976Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AE%CF%81\" --note \"page 361: Ancient Greek aner, andros\" && cd data/verification/sources/web && f=$(python3 - <<'EOF'\nimport json\nfor l in open('index.jsonl'):\n    d=json.loads(l)\n    if d['url'].endswith('%E1%BC%80%CE%BD%CE%AE%CF%81'): print(d['file'])\nEOF\n) && echo $f && grep -n -A6 \"Etymology\" $(basename $f) | head -30"
}
```


### [2026-09-07T19:40:31.366Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/915d38f527665766.txt
data/verification/sources/web/915d38f527665766.txt
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
182: Etymology
183- [ edit ] 
184-
185- From Proto-Hellenic *anḗr , from Proto-Indo-European *h₂nḗr . [ 1 ] Cognates include Sanskrit नृ ( nṛ́ ) , नर॑ ( nára ) , Latin neriosus and Old Irish nert .
186-
187- Pronunciation
188- [ edit ]
```


## [2026-09-07T19:42:13.490Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### NYB narig\"; grep -n \"nyryk\\|nārīg\\|narig\\|nāyrīg\" NYB_vol2_glossary.txt | head -5; echo \"#### SKT\"; grep -n -i \"philanthropy\\|andrew\\|android\" SKT.txt | head -5; echo \"#### ARY\"; python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nfor i in range(1,len(parts),2):\n    body=parts[i+1]\n    for w in ('نیرو','هنر','نریمان'):\n        if re.search(r'(^|\\n)\\s*'+w+r'\\b', body):\n            print('pdf page',parts[i], w)\nEOF"
}
```


### [2026-09-07T19:42:14.813Z] TOOL RESULT

```
#### NYB narig
#### SKT
16416:sal  tire,  in  heraldry,  a  St.  Andirw'sj (F.  — L.)     Across  in  this  position F.saul/oir^  St.  Andrew's  cross  (Cot.),^ O.  F,  sauioir,  ori^;.  a  stirrtJp  of  a 5hni>e  A ;  the  cro^s  being  named position  of  the  stirrup's  sidea,  « saltatorium,  a  sttrrup.  •>  L..  sattmi^Hw^ longing  to  leaping  or  Springing; for  mounting  anorie.  —  L.  ral/atvr,  t\cA\
#### ARY
```


## [2026-09-07T19:42:21.849Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### FSD android\"; grep -c \"android\" FSD_vol1.txt; grep -o -m1 \".\\{0,80\\}android.\\{0,200\\}\" FSD_vol1.txt | head -2; echo \"#### FSD philanthropy\"; grep -o -m1 \".\\{0,60\\}philanthropy.\\{0,150\\}\" FSD_vol3.txt | head -2; echo \"#### ARY grep\"; grep -c \"نیرو\" incoming/ARY/ARY_pages.txt; grep -c \"هنر\" incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T19:42:28.894Z] TOOL RESULT

```
#### FSD android
4
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits


#### FSD philanthropy
ugrep: error: error at position 89
x80-\xbf][\x80-\xbf]*){0,150}
exceeds complexity limits___/


#### ARY grep
7
3
```


## [2026-09-07T19:42:34.677Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('android',t))[:3]:\n    print(repr(t[m.start()-100:m.start()+260])); print('---')\nt3=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('philanthrop',t3))[:2]:\n    print(repr(t3[m.start()-120:m.start()+300])); print('---')\na=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',a)\nfor i in range(1,len(parts),2):\n    for w in ('نیرو','هنر'):\n        if w in parts[i+1]:\n            j=parts[i+1].find(w)\n            print('ARY pdf',parts[i],w,repr(parts[i+1][max(0,j-150):j+250]))\n            print('---')\nEOF"
}
```


### [2026-09-07T19:42:36.092Z] TOOL RESULT

```
'2.  la-)  A   salamander  of  this genus.—  Am"phl-u\'ml-dtc,  n. pi.  Herp.  A   family  of  aala- mandroid  amphibians  with  per- sistent gills  and  without  eye- lids, Including  the  Congo-snake  j of  the  southern  United  States.\n—   anR\'phi-u\'mld,  n.—  am"-  I phl-u\'mold,  a.—  Am"pbl-u\'- rl-dm,  n.  pi.  Echin.  A   family of  brittle-stars  with '
---
'as  certain  flowers.—  an-drog\'j-ny,  n.  Her- maphroditism. an"dro-gy-ne\'I-tyJ;  an"dro-gyn\'l-af.\nandroid  Key  l:  ortlstlc,  art;  fat,  fare;  fast;  get,  prey;  hit,  police;  obey,  gO;  not,  Cr;  full,  rflle;  but,  bOrn;  »   =   final;  i   =   habit,  renew;\nangelique  Eey  2:  art,  upo,  fat,  fare,  fast,  what,  all;  mG,  get,  prey,  fern'
---
')  =sing;  so;  Ship;  fhin,  this;  ajure;  F.  bon,  dune;  h   =   loch. +,  obsolete  variant.  android\nKey  2:  book,  bdbt;  full,  rule,  cure,  but,  bOrn;  oil,  boy;  •€  =   k;  r   =   s;  go,  gem;\x0c  ink;  s   =   z;  thin,  this;  F.  bon,  dune;  h   =   loch.  angeliQUe\nan"e-refc\'Ic»  \\   1   an\'i-ret\'ik;  2   Sn\'e-r5t\'ic,  n.  Med .   Any an'
---
'd or\nmould, a mortal — man of motley t, a iester; fool — Man\nof Boss, John Kyrle of Ross, Herefordshire, a 17th-oentury\nphilanthropist, ImtnorUllaed by Pope — Man of Beditlon*\nJoan Claude, an eloquent l*rotestant pastor, twice silenced\nfor cufitrovemles with Rossuet and others over the edict of\nNantes: so oallod by Madame de Matntenon.— man of sin,\na New Testament designation (0 These 11, 3) applied to Anti-\nchrist —'
---
'tesman. Heerotary of Htate. Chief .Icstlco of the Hupreroe\nCourt. 4. tiOUls (iVi4l8riG->/nl029), an American lawyer\nand philanthropist fi. Thomas SIley <■ i«lK/i4>Vil92A).\nAmerican lawyer, Vloe-Presldent of the United Htaten 1913>\n1921 fi. A eoiiniy iuN E Alsimnia ritHisfj m .county-seat\nGuiitersville 7 A county in N central IIHiioIh 39b sq. m ;\ncount y-seat, I.ucr>ii H. A county In N liiilluna 440 sij m\ntounty-seat,'
---
ARY pdf 14 هنر 'ترش این زبان غیر هند و اروپایی به تدریج\nکم شده است. در شمال و مرکز ایتالیا «اتروسکان\u200cهاء (177741780۸1758) تمدن درخشانی را به وجود\nآورده بودند که آثار هنری آن در بسْیاری از موزه\u200cها دیده می\u200cشود. ورود هند و اروپائیان از شمال.\nباعث شد که این زبان و فرهنگك غیر هند و اروپایی نابود گردد. مدارکك موجود نشان می\u200cدهد که در\nآسپای صغیر نیز اقوام غیر هند و اروپایی ("هوریان\u200cها" 131771۸18 و "هتیک\u200cها" ۳7108 ۸)\nتوسط'
---
ARY pdf 190 هنر '۲۳-۶۴\n2 (308۸00178) ,84\nبادداشت,\n۱ چم این واژه در زبان\u200cهای رمانس (ناشی از لاتین) و اسلاوی: نساجی؛ بافندگی.\n۰ چم این واژه در زبان\u200cهای دیگر: با فنوری و هنرمندی ساختن (به ویژه از چرب).\nاوستایی (/4887۸): 7۸0۸۰ 3 ۱\nپارسی باستان (401/ق۲87 00 ت7۸\nپهلوی (۲1اللمه): پسگشت\u200cها رد رد۳۹۱\n6 بلل707 ,704 ,784 8 و20\nکردی (0(3/7): 707131 ,70۷ ,73 2 (5580) 1\nافغانی (پشتو) (۸01721): 70۸ 6 (85852) ی\nسانسکریت (5۸(88077)'
---
ARY pdf 203 نیرو '1شا5 77637ل) صام). :57\n۰ ال ران ن ۷ 9 (78310) ,647 (010151\nلهستانی (3آ]۳0): اد ی برهان قاطع : ۵۱۹\nروسی (/5314): 7637\nپادداشت:\nچم این واژه در اوستایی: نیرومند\nچم این واژه در تخاری 2,۸ جلوگیری.\nاوستایی (۸۷887۸/۷): انگلیسی کهن (8701/8/7 010):\n۸ 7۸1۸۸ راغ 3 080۸0 ,051۸\nپهلوی (۲1هاتلمم): 7۸ لیترانی (الفاللهلاتز تم 1۸0۸8 ,۳۳۲۶\nسانسکریت (54(/97777):\n۸5۰ «ها122 ,7۸611 ,لق1۸ پسگشت\u200cها 5\nیرنانی 028810): ۰ 1۸'
---
ARY pdf 290 هنر 'نی کهن ((087244 777077 010)(شاید) 7 (05) 547\n۹ ت70 010 :043 ۸ 07لا\n.ار آلمانی (0880/40)(شاید) 7۸7 برهان قاطع + .۹\nاست بادداشت.\nچم این واژه در زبان\u200cمالهنر و اروپایی کهن: دویدن» جاری شدن. :\nچم اين واژه در زبان\u200cهای ژرمنی نوین: ژاله,\nاوستایی (/4(8974): ۰ 0۸3181 ,0۸301 پارسی باستان (۶37807 0ا0):\n\x0c'
---
ARY pdf 494 نیرو '028\nگالی (/5/): ,05 7 (۲۸۷۷) ,396 (۸۸۷5) 57\nولزی (/5ا76): 08 121 ملتهلا\nبرتونی (87570۸): 10 برهان قاطع : ۳1۰\nیادداشت:\nچم این واژه در انگلیسی: ناوگان» نیروی دریایی,\n۱\nپارسی باستان ((۲8۸۶4 ۰:00 ۹3۸۵۸ لونی (لتی) (4777400): ۸۸۹۲.۲ ,2۸۵733\nپپلوی (71ماتل۸ :۰ ۸۷۸ \u200e٩2013,\u200f ,۸۸\nکردی (0870154): لا پسگشت\u200cها ارسی اد تردن\nافقانی (پشتو) (///4۴0۸): . هع۸2 ۳ را\nسانکریت (54(75877): م۸۸۵۸ ,۸۸۵۶ 58 (۸۷۳) ,8850) :02/'
---
ARY pdf 495 نیرو 'نیکد (007/110): 4۸ | برهان قاطع + ۳۱۳۶\nاسلاوی کهن (ع۷1اما؟ [ع18بل» 01.0):\nبادداشت:\n۱ چم این واژه در زبان لاتین(به ویژه به عنران اسم خاص يا ویژه نام): نیرومند.\nچم این واژه در زبان\u200cهای ولزی و برترنی: قهرمان.\nچم این واژه در زبان پروسی کهن: خشم.\nچم این واژه در زبان گوتیکه: (اسم خاص) نام خدا.\nچم این واژه در ایرلندی کهن: شریف» بزرگوار.\n۲ بازگشت به: نیروء ثیر,\nاوستایی (/41287۸2): ۸82۸ ,2۸20۷0 ۸۵0۸۰ 2۸201'
---
ARY pdf 524 نیرو '\nویر» بیر (به چم *"هوش* "حافظه"» "نیرو(مند)") / ۵۲۵\nاوستایی (/4۳287۸): 0 بش۷1 پروسی کهن رپرمرووتج۲۳ ۰:۵۵ ۷1385\nپهلری (۳۸۶۲7): ۷۷1۳۵۸۸۸۷۵1۲ ,]۱۷۶ ایرلندی کهن (4کلقا 0ا0): 3 داد\nکردی (20/877ن6): ۸1\nبلوچی (/677/ا.ل8): دا پسگشت\u200cها ارت ات تس\nتخاری ۸ ( 4(۷ل70104۸7): 3 ۲0/05/0\nسانسکریت (5۸4'
---
ARY pdf 536 نیرو '\nوش ۵۳۷۲\nپسگشت\u200cها 5 4 (2۸3ن31) :۸1۸0620/28\nبادداشت.\nبازگشت به: تر» نیرو\nاوستایی (4۳587۸/1): 3\nپپلوی (۸4۷7ا3ل2۸): پسگشت\u200cها ۰ 23۳8۵۸۵۶ | .\nبررعت ,858 ,38 ,وتات و ۶000۸\nکردی (8.0/57): 1115 ات / 0\nانغانی (پشتو) (/۸۳07): ۱1 مدز 0۷۳۳2۲63۲۵\nارمنی (ل۸/0452/14): ان برهان قاطع : ۳۳۹۳\nیادداشت:\nبازگشت به:گرش,\nاوستایی رورم 2885۱'
---
```


## [2026-09-07T19:42:52.317Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\na=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',a)\nd={parts[i]:parts[i+1] for i in range(1,len(parts),2)}\nprint('=== pdf 495 ==='); print(d['495'][:1500])\nEOF"
}
```


### [2026-09-07T19:42:53.541Z] TOOL RESULT

```
=== pdf 495 ===

۶ | نره نره- (مثلاً در"نره خر)» نرینه
| جماکلسی سوالی فش سس 94۵
اوستایی (40897۸0۷: ,۸۸/۲۵ 2۷۸۵ ۵
۸ لیتوانی (42/14(۷(ا 2 7/./): ,۱۷0577 ,تآ۴03
پارسی باستان (4(4ا۶828 صا0): 8 ,م708۸
21۸871۸ پروسی کهن (/۳3۲-55 ۰:۵2 21837180۲
پهلری (1/1اتلمم). 3 ایرلندی کهن (لا5لقا صا0): 17 ۸8
اوستی (0558776: ق۸٩‏ ,۸۸5 ,3۸۲۰ ولزی (514ل5ل): ۱5۸
کردی (78.015/1)): 8 ۲۴ برتونی (/87570): دال!
بلوچی (6711/آملم8): ۸ آلبانی (۸2۷ا۷مقام): انا
افقانی (پشتی) (/۸۳0//۸۷): ۷330۸ ,۸
سانسکریت (54(/58/7): بللش۷۸ ,3۸۵ پسگشت‌ها رده ید دید
1۸ زر ۳0
آرمنی (۵1ا/7452)): 0 بالاتغ 2 تهج ند ات ی
برنانی 8540ظ0): 5 ,2085 9 ما8 ,85 0
لاتین (47/00): ,3۷88108108 ,۸۷8 1 تهج ۸/1/00
10 لغت‌نامه دهخدا: ۲۱۳۳۰۶
گرنیکد (007/110): 4۸ | برهان قاطع + ۳۱۳۶
اسلاوی کهن (ع۷1اما؟ [ع18بل» 01.0):
بادداشت:
۱ چم این واژه در زبان لاتین(به ویژه به عنران اسم خاص يا ویژه نام): نیرومند.
چم این واژه در زبان‌های ولزی و برترنی: قهرمان.
چم این واژه در زبان پروسی کهن: خشم.
چم این واژه در زبان گوتیکه: (اسم خاص) نام خدا.
چم این واژه در ایرلندی کهن: شریف» بزرگوار.
۲ بازگشت به: نیروء ثیر,
اوستایی (/41287۸2): ۸82۸ ,2۸20۷0 ۸۵0۸۰ 2۸2018131۸
```


## [2026-09-07T19:43:01.847Z] AGENT

Now I'll write the verification file.


## [2026-09-07T19:49:09.150Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk361.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = {\n \"pie\":  \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82n%E1%B8%97r\",\n \"nar\":  \"https://en.wiktionary.org/wiki/%D9%86%D8%B1\",\n \"niru\": \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B1%D9%88\",\n \"honar\":\"https://en.wiktionary.org/wiki/%D9%87%D9%86%D8%B1\",\n \"nariman\":\"https://en.wiktionary.org/wiki/%D9%86%D8%B1%DB%8C%D9%85%D8%A7%D9%86\",\n \"aner\": \"https://en.wiktionary.org/wiki/%E1%BC%80%CE%BD%CE%AE%CF%81\",\n \"idris\":\"https://en.wiktionary.org/wiki/%D8%A5%D8%AF%D8%B1%D9%8A%D8%B3\",\n \"alex\": \"https://en.wiktionary.org/wiki/%CE%91%CE%BB%CE%AD%CE%BE%CE%B1%CE%BD%CE%B4%CF%81%CE%BF%CF%82\",\n \"aliskandar\":\"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1\",\n \"eskandar\":\"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%AF%D8%B1\",\n \"eskandar_ot\":\"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D9%83%D9%86%D8%AF%D8%B1\",\n \"android\":\"https://www.etymonline.com/word/android\",\n \"philan\":\"https://www.etymonline.com/word/philanthropy\",\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"nar, nairya; naire-manâw; nairyava\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Av. nar- m. 'man' (nom. sg. nā, acc. narəm, oblique stem nar-/nr̥-) is the regular Iranian reflex of \"\n  \"PIE *h₂nḗr; Bartholomae AiW col. 1049ff. gives 'nar- : nr̥- m. ‚Mann‘' explicitly opposed to the \"\n  \"feminine nāirī- and to gənā-/jani- 'wife'. The adjective nairya- 'virilis, manly, of male sex' (AiW: \"\n  \"'nairya- Adj. (fem. °ryā-) ‚virilis‘') is *nar-ya- with the normal Avestan i-epenthesis before y \"\n  \"(nar-ya > nairya). naire-manah- (Bartholomae's nairemanah- 'mannhaften Sinns', epithet of Kərəsāspa, \"\n  \"Y.9.11, Yt.5.37, 15.27, 19.38f., Pahlavi gloss mart-mēnišn, Skt. nr̥mānas-) is nairya- + manah- 'mind'; \"\n  \"Nourai's 'naire-manâw' is his transliteration of the nominative singular nairemanā̊ of that -manah- stem, \"\n  \"not a different word. The third word is the weak link: nairyava- 'manliness, strength' is NOT attested in \"\n  \"the extant Avesta — Horn (Grundriss no. 1064, p. 238) cites it as aw. *nairyava- with an asterisk, and \"\n  \"current reconstruction is Proto-Iranian *naryawa-(ka)-; printing it as plain 'Avestan' overstates the \"\n  \"evidence, hence the verdict 'plausible' for the box as a whole.\"),\n \"derivation_fa\": (\n  \"اوستایی nar- «مرد» (نهادی nā، رایی narəm) بازماندهٔ منظم *h₂nḗr هندواروپایی آغازین است و بارتولومه در \"\n  \"«فرهنگ ایرانی باستان» (ستون ۱۰۴۹ به بعد) آن را در برابر مادهٔ مادینهٔ nāirī- آورده است. صفت nairya- \"\n  \"«مردانه» از nar-ya- ساخته شده و «ای» آن حاصل هم‌گونی/میان‌جی i پیش از y در اوستایی است. naire-manah- \"\n  \"«مردانه‌منش» (لقب کرساسپ، با برگردان پهلوی mart-mēnišn و همتای سنسکریت nr̥mānas-) از nairya- + manah- \"\n  \"«اندیشه» است؛ آنچه نورایی «naire-manâw» نوشته همان صورت نهادی nairemanā̊ همین ستاک است، نه واژه‌ای دیگر. \"\n  \"ولی nairyava- «مردانگی، نیرو» در متون اوستایی موجود گواه ندارد: هرن (بند ۱۰۶۴، ص ۲۳۸) آن را با ستاره \"\n  \"*nairyava- می‌آورد و بازسازی امروزی ایرانی آغازین *naryawa- است؛ پس نامیدن آن «اوستایی» بی‌احتیاطی است و \"\n  \"ادعای این جعبه «با احتیاط پذیرفتنی» است.\"),\n \"sources\": [W[\"pie\"], W[\"nariman\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:765\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt line 62647 'Root / lemma: ner-1(t)-, aner-' … 'Old Indic nar-(na) \\\"man, person\\\", Avestan nar-(na) ds. … Old Indic narya-, Avestan nairya- \\\"manly, virile\\\"'; Page(s): 765 — exactly the arrow's Avestan words.\"},\n  {\"ref\": \"SYN:81\", \"status\": \"supports\",\n   \"note\": \"Buck 2.21 'MAN² (vs. Woman)' begins on printed p. 81 (SYN.txt record 111): the language list has 'Skt. nar-, nara-, vīra-…  Av. nar-, vīra-, OPers. martiya-', and section '2. IE *ner-, nert- ‚strength, might‘ … Walde-P. 2.332f.'\"},\n  {\"ref\": \"HRN:238\", \"status\": \"supports\",\n   \"note\": \"Horn no. 1064 on printed p. 238 (HRN.txt record 260): 'nīrō (*nērō) ‚Kraft, Macht‘. aw. *nairyava- ‚Mannhaftigkeit‘, vergl. nairya- ‚mannhaft‘; ai. narya-; phlv. nērōk.' — supports the derivation but writes *nairyava- with an asterisk.\"}],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1049ff. s.v. nar-; col. 1053f. nairemanah-; nairya-\", \"stance\": \"supports\",\n   \"note\": \"'j; g. nar- : nr̥- m. ‚Mann‘' with sub-sense (c) opposed to nāirī-; 'j. nairemanah- Adj. ‚mannhaften Sinns‘: … kərəsāspa Y.9.11, Yt.5.37 … Vgl. ai. nr̥mānas- … Pü.: mart mēnišn'; 'j. nairya- Adj. (fem. °ryā-) ‚virilis‘'. No entry nairyava- anywhere in BRT.txt (grep 'nairyava' → 0 hits).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 332f. s.v. '1. ner-, aner-'\", \"stance\": \"supports\",\n   \"note\": \"'Ai. nár- (nā) ‚Mann, Mensch‘, av. nar- (nā) ds. … ai. nárī, av. nāirī ‚Frau‘ … ai. narya-, av. nairya- ‚mannhaft, männlich‘' (WLD_Bd2_pages.txt line 21972ff.).\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. ner- (1) 'man; male'\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'ner- (1) ‚man; male‘. WP II, 332. … Av. nar, id. beside naro, id. and cons. stem nā, acc. narom … Per. nar, adj. ‚male‘' (IEC.txt line 11655).\"}]})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"nar «نر»; Narîmân «نریمان»; nîrŭ «نیرو»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"All three are genuine, but they reach New Persian through Middle Persian, not out of Avestan (Avestan is \"\n  \"a sister dialect of the ancestor, not the ancestor). (1) NP nar 'male' < MP nar (Book Pahlavi nl, with the \"\n  \"Aramaic ideogram ZKL) < Old Iranian *nar-, cognate with Av. nar-, Skt. nara-, Pashto nar, Ossetic næl. \"\n  \"(2) Narīmān < MP Narēmān (Manichaean MP nrymʾn narēmān) < Av. nairemanā̊/nairyō.manah- 'of manly mind', \"\n  \"with ē > ī in New Persian; in the Šāhnāme he is the father of Sām and great-grandfather of Rostam, which \"\n  \"is exactly what Borhān-e Qāṭeʿ p. 2132 says. Nourai's gloss \\\"like a man\\\" is loose — the compound means \"\n  \"'manly-minded'. (3) nīrū 'strength' < MP nērōg [nylwk'] 'strength, power' (MacKenzie; Manichaean MP nyrwg) \"\n  \"< Old Iranian *naryawa-ka-; the final -g/-k is lost after the long vowel and ō > ū: nērōg > nērō > nīrū, \"\n  \"the very chain Horn no. 1064 prints (nīrō < *nērō, phlv. nērōk) and Moʿin's footnote in Borhān p. 2225 \"\n  \"repeats with Hübschmann.\"),\n \"derivation_fa\": (\n  \"هر سه واژه اصیل‌اند، اما راهشان به فارسی نو از فارسی میانه است نه از اوستایی (اوستایی گونهٔ خواهرِ نیای \"\n  \"فارسی است، نه نیای آن). ۱) «نر» از فارسی میانهٔ nar (پهلوی کتابی nl و نویسهٔ آرامی ZKL)، از ایرانی باستان \"\n  \"*nar-، هم‌ریشه با اوستایی nar- و سنسکریت nara-. ۲) «نریمان» از فارسی میانهٔ Narēmān (مانوی nrymʾn)، از \"\n  \"اوستایی naire.manaŋh- «مردانه‌منش»؛ ē فارسی میانه در فارسی نو به ī بدل شده است. در شاهنامه نریمان پدر سام \"\n  \"و نیای رستم است و برهان قاطع (ص ۲۱۳۲) نیز همین را می‌گوید؛ معنای دقیق ترکیب «مردمنش» است نه «مانند مرد». \"\n  \"۳) «نیرو» از فارسی میانهٔ nērōg «زور، توان» (مکنزی؛ مانوی nyrwg)، از ایرانی باستان *naryawa-ka-؛ کافِ پایانی \"\n  \"پس از واکهٔ بلند افتاده و ō به ū بدل شده: nērōg > nērō > nīrū — همان زنجیره‌ای که هرن (بند ۱۰۶۴) و حاشیهٔ \"\n  \"معین بر برهان قاطع (ص ۲۲۲۵، با استناد به هوبشمان) می‌آورند. ادعای نورایی درست است.\"),\n \"sources\": [W[\"nar\"], W[\"niru\"], W[\"nariman\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:2126\", \"status\": \"supports\",\n   \"note\": \"Borhān vol. 4, printed p. 2126 (pdf 209 of BQT_v4): headword «نر … معروف است که نقیض ماده باشد» plus Moʿin's etymological footnote 'بتخفیف و تشدید راء، ایرانی باستان -nar «بارتولمه ۱۰۴۷»، پهلوی … «نیبرگ ۱۵۵»، اوستا nar- (هرد)، هندی باستان nara-, افغانی nar, استی…' — exactly Nourai's arrow.\"},\n  {\"ref\": \"BQT:2132\", \"status\": \"supports\",\n   \"note\": \"printed p. 2132 (pdf 215): «نریم … نام پدر سام است که جد رستم باشد» and «نریمان … بمعنی نریم است که جد رستم زال باشد» — confirms Narīmān as the male name.\"},\n  {\"ref\": \"BQT:2225\", \"status\": \"supports\",\n   \"note\": \"printed p. 2225 (pdf 308): «نیرو … بمعنی زور و قوت و توانایی باشد» with footnote 4: 'nērōk (زور، قوت). اوستا nairyava (رجولیت، مردانگی)، cf. nairya- (مردانه)؛ هندی باستان nārya-, پهلوی nērōk … و رك: هوبشمان' — the whole chain Av. nairyava- > Pahl. nērōk > NP nīrū.\"},\n  {\"ref\": \"BQT:1796\", \"status\": \"not_found\",\n   \"note\": \"printed p. 1796 of the Moʿin/Amir Kabir continuous pagination is in vol. 3 in the گرز… section (pdf 591; p. 1793 = «گرد/گرزن», p. 1797 = «گرست»); there is nothing about نر/نیرو there. Either a typo in the book or a citation belonging to another chart.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p. 57 s.v. nērōg; nar (in narig etc.)\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie: 'nērōg [nylwk' | M nyrwg, N nērō] strength, power. ~ōmand: strong, powerful' (PHD.txt line 510).\"},\n  {\"src\": \"HRN\", \"where\": \"no. 1064, p. 238\", \"stance\": \"supports\",\n   \"note\": \"'nīrō (*nērō) ‚Kraft, Macht‘ … phlv. nērōk.'\"},\n  {\"src\": \"ARY\", \"where\": \"printed p. 496 (ARY_pages pdf 495) s.v. نر، نره، نرینه\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's independent entry lists Av. NAR-/NAIRYA-, OP, Pahlavi, Ossetic, Kurdish, Balochi, Pashto, Skt., Arm., Gk., Lat. and cross-refers «بازگشت به: نیرو، نر»; his note 'چم این واژه در زبان لاتین … نیرومند / در ولزی و برتونی: قهرمان' reproduces Pokorny 765's cognate set.\"},\n  {\"src\": \"MON\", \"where\": \"vajehyab/abadis (فرهنگ معین) for نیرو/نر\", \"stance\": \"silent\",\n   \"note\": \"the online Moʿin viewers are JavaScript-rendered; the archived fetches returned only site chrome, so nothing usable.\"}]})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"nâirî\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Av. nāirī- f. 'woman, wife, lady' is the Indo-Iranian feminine built to nar- with vr̥ddhi of the first \"\n  \"syllable (*nār-ī-), matching Skt. nārī 'woman'; Walde-Pokorny II 332 states it plainly ('ai. nárī, av. \"\n  \"nāirī ‚Frau‘ (erst ar. Femininbildung)'), i.e. the formation is Indo-Iranian, not PIE. Bartholomae has \"\n  \"nāirī- and its -ka- derivative nāirikā- 'woman, wife' throughout the Vīdēvdād and Nērangestān (e.g. \"\n  \"'yat nāirika ərəθrim jasāt ‚wenn eine Frau in die Schwangerschaft kommt‘' V.5.45), and notes that nar- \"\n  \"and nāirī-/nāirikā- specifically designate 'der, die Gläubige', the adult male and female members of the \"\n  \"Zoroastrian community (nāirinąm aṣ̌aoninąm 'of the pious women', Yt.13.143-145) — which is where the \"\n  \"'(pious) woman' of the next box comes from.\"),\n \"derivation_fa\": (\n  \"اوستایی nāirī- «زن، بانو» صورت مادینهٔ nar- در دورهٔ هندوایرانی است که با کشش (وریدی) هجای نخست ساخته شده \"\n  \"(*nār-ī-) و همتای سنسکریت nārī است؛ والده-پوکورنی (ج۲ ص۳۳۲) صریحاً می‌گوید این ساخت مادینه «تازه و \"\n  \"هندوایرانی» است، نه هندواروپایی. بارتولومه هم nāirī- و مشتق آن nāirikā- «زن، همسر» را در وندیداد و \"\n  \"نیرنگستان می‌آورد و یادآور می‌شود که nar- و nāirī- در متن‌های دینی به‌ویژه بر «مرد و زن مؤمن» جامعهٔ \"\n  \"زردشتی دلالت دارند (nāirinąm aṣ̌aoninąm «زنان پارسا»)؛ همین نکته سرچشمهٔ معنای «زن پارسا» در جعبهٔ بعدی \"\n  \"است. ادعای نورایی درست است.\"),\n \"sources\": [W[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:765\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p. 765: 'Old Indic narī, Avestan nāirī ‚woman‘ (previously Aryan feminine formation)' (OCR 'Avestan nairfmie, woman').\"}],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1065 nāirī-, nāirikā- (cited from SNS); V.5.45, N.5, Yt.13.143\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt has 'yat … nairika ərəθrim jasāt ‚wenn eine Frau in die Schwangerschaft kommt‘ V.5.45' (line 8383) and 'insbes. mit nar- m. und nāirī-, nāirikā- f. ‚der, die Gläubige‘' (line 6271); also 'kū-nāiri- f. ‚Hurenweib‘' (line 9651).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 332\", \"stance\": \"supports\",\n   \"note\": \"'ai. nárī, av. nāirī ‚Frau‘ (erst ar. Femininbildung)'.\"},\n  {\"src\": \"SYN\", \"where\": \"2.22 WOMAN, p. 82\", \"stance\": \"silent\",\n   \"note\": \"Buck's 'woman' list gives Av. only nāirikā- indirectly; the printed list on p. 82 does not cite nāirī- for Avestan, so no independent statement there.\"}]})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Pahlavi\",\n \"words\": \"nâyrig\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"MP nāyrīg / nārīg [n(y)lyk'] 'woman, lady, wife' (MacKenzie, Concise Pahlavi Dictionary: 'nārīg … woman, \"\n  \"lady, wife'; English-Pahlavi index 'wife nārīg, zan', 'woman nārīg, zan') continues not the bare Av. \"\n  \"nāirī- but its -ka- derivative nāirikā-, Old Iranian *-ikā- giving the regular MP suffix -īg; the written \"\n  \"-y- of nāyrīg still shows the Avestan diphthong ai. In Šāyest nē Šāyest, the text Tavoosi's glossary \"\n  \"indexes, nāyrīg is the (married, ritually observant) woman of the community and the phrase nāyrīg zan \"\n  \"also occurs — hence Nourai's '(pious) woman'. The step Av. nāirī(kā)- > MP nāyrīg is therefore right, \"\n  \"with the small correction that the immediate base carries the -ka- suffix.\"),\n \"derivation_fa\": (\n  \"فارسی میانهٔ nāyrīg/nārīg «زن، بانو، همسر» (مکنزی: nārīg … woman, lady, wife) دنبالهٔ خودِ nāirī- اوستایی \"\n  \"نیست، بلکه دنبالهٔ مشتق آن nāirikā- است؛ پسوند ایرانی باستان *-ikā- در فارسی میانه به -īg بدل می‌شود و \"\n  \"«ی» در nāyrīg هنوز نشانهٔ دوگانه‌واکهٔ ai اوستایی است. در متن «شایست نه شایست» — که واژه‌نامهٔ طاوسی برای \"\n  \"آن فراهم شده — nāyrīg زنِ (شوهردار و دین‌دارِ) جامعه است و ترکیب nāyrīg zan نیز به‌کار رفته؛ از این‌رو \"\n  \"معنای «زن پارسا» در کتاب نورایی بی‌جا نیست. ادعا درست است، با این تصحیح کوچک که پایهٔ بی‌واسطه، صورت \"\n  \"پسوندی nāirikā- است.\"),\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"SNS:264\", \"status\": \"supports\",\n   \"note\": \"Tavoosi's own index (SNS_pages.txt leaf 229) lists 'nāyrīg 264/19' and 'nāyrīg zan 264/24', i.e. exactly the cited page; the glossary entry itself (leaf 150) reads ':nāyrīg:' with the cross-references 'nairīk' and '(AiWb. 1065) nairī-', so Tavoosi derives it from Avestan nāirī-/nairikā- as Nourai's arrow does.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p. 57 s.v. nārīg; index s.v. wife, woman\", \"stance\": \"supports\",\n   \"note\": \"'narig [n(y)lyk'] woman, lady, wife' (PHD.txt line 500); 'woman nārīg, zan' (line 4334).\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary\", \"stance\": \"silent\",\n   \"note\": \"grep of NYB_vol2_glossary.txt for nārīg/nāyrīg/nyryk gives no hit — the word does not occur in the texts Nyberg glosses.\"},\n  {\"src\": \"BRT\", \"where\": \"col. 1065 nāirikā-\", \"stance\": \"supports\",\n   \"note\": \"the Avestan -kā- form on which MP nāyrīg is built is amply attested in BRT.txt (V.4.44 'upa vā nairikam vādayaδa ‚so möge man (ihnen) eine Frau zur Ehe geben‘', line 22391).\"}]})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Avestan\",\n \"words\": \"hu-nara\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Av. hunara- m./n. 'ability, art, skill' (Bartholomae: 'g. hunara- m. 1) ‚Können, Kunst‘', with the \"\n  \"abstract hunaratāt- 'the sum of ability' and the compounds aṣ̌a-hunara- 'whose ability is great', \"\n  \"haθa-hunara- 'skilful', draxtō.hunara- 'that knows learnt tricks' of the luxury dog V.13.8) is hu- \"\n  \"'good' (PIE *h₁su-, Nourai's cross-reference Su 1) + nara-, i.e. 'having the good quality of a man'. \"\n  \"The Old Persian cognate is actually attested: huvnara- 'skill, accomplishment' in Darius' Naqš-e Rostam \"\n  \"inscription DNb 45, 48, 51, which Kent analyses as 'adj. formation to pAr. *su- ‚good‘ + *nar- ‚man‘ \"\n  \"= having the good quality of a man'. Walde-Pokorny II 332 lists av. hunara- 'Können, Kunst, \"\n  \"Kunstfertigkeit, Tüchtigkeit' under ner- with the remark that it would originally be 'virtus', then \"\n  \"'virtuosité' — precisely Nourai's gloss 'good virtue, skill'.\"),\n \"derivation_fa\": (\n  \"اوستایی hunara- «توانایی، هنر، مهارت» (بارتولومه: hunara- m. «Können, Kunst»، با مشتق hunaratāt- و \"\n  \"ترکیب‌هایی چون aṣ̌a-hunara- و draxtō.hunara- «سگِ آموخته‌کار» در وندیداد ۱۳/۸) از hu- «نیک» (هندواروپایی \"\n  \"*h₁su-، همان ارجاع Su 1 نورایی) + nara- ساخته شده، یعنی «دارندهٔ خویِ نیکِ مردانه». همتای پارسی باستان آن \"\n  \"گواه دارد: huvnara- «هنر، توانایی» در سنگ‌نوشتهٔ داریوش در نقش رستم (DNb بندهای ۴۵، ۴۸، ۵۱) که کنت آن را \"\n  \"«*su- نیک + *nar- مرد» تحلیل می‌کند. والده-پوکورنی نیز آن را زیر ner- می‌آورد و معنای نخستینش را «virtus» \"\n  \"و سپس «چیره‌دستی» می‌داند — دقیقاً همان «فضیلت نیک، مهارت» نورایی. ادعا درست است.\"),\n \"sources\": [W[\"honar\"], W[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:765\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt p. 765: 'probably also Old Indic sunara- ‚full of vitality, juvenile‘, Avestan hunara- ‚miracle power‘' (i.e. Wunderkraft) under ner-1(t)-.\"}],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1831 hunara-; also aṣ̌ahunara-, haθa.hunara-, draxtō.hunara-\", \"stance\": \"supports\",\n   \"note\": \"BRT.txt line 30399 'j-, g. hunara- m. 1) ‚Können, Kunst‘ … a) ‚Kunstfertigkeit, Geschick…‘'; line 6346 'aṣ̌ahunara- Adj. ‚des Können (usw.) gross ist‘ Yt.10.25'; line 14059 'draxtō.hunara- Adj. ‚der gelernte Fertigkeiten besitzt, Kunststücke kann‘ vom Luxushund'.\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. huvnara- (DNb 45, 48, 51)\", \"stance\": \"supports\",\n   \"note\": \"Kent: 'huvnara- sb. ‚skill, accomplishment‘: adj. formation to pAr. *su- ‚good‘ + *nar- ‚man‘ …, = ‚having the good quality of a man‘, Av. hunara- ‚ability, skill‘, Skt. sūnára-' (KNT.txt line 5218).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 332\", \"stance\": \"supports\",\n   \"note\": \"'av. hunara- m. ‚Können, Kunst, Kunstfertigkeit, Tüchtigkeit‘ (wäre ursprgl. ‚virtus‘, dann ‚virtuosité‘)', with the caution that Bartholomae AiW 1831 doubted the link with Skt. sunara-.\"}]})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"honar «هنر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"NP honar < MP hunar [hwnl], Manichaean MP and Parthian hwnr 'virtue, ability, skill' (MacKenzie: 'hunar \"\n  \"… virtue, ability, skill', with hunarāwand, hunarōmand > NP hunarmand), continuing OP huvnara-/Av. \"\n  \"hunara-: u is kept, the thematic -a falls, and the New Persian pronunciation shifts to honar. Nyberg's \"\n  \"glossary gives the whole line in one place: 'hunar [hwnl] skill … Av. (1831) hunara-; MPrth hwnr \"\n  \"‚manliness, ability‘; Paz. xunar; NP hunar'. The semantic path is 'manly quality' > 'ability, craft, \"\n  \"accomplishment' (so in Kalīla and Golestān: هنر ندیمان) > modern 'art' (هنرهای زیبا, a 20th-century \"\n  \"calque of beaux-arts); Armenian hunar 'means, way' is an Iranian loan from the same word.\"),\n \"derivation_fa\": (\n  \"«هنر» از فارسی میانهٔ hunar (پهلوی hwnl؛ مانوی و پارتی hwnr) «فضیلت، توانایی، مهارت» است (مکنزی: hunar … \"\n  \"virtue, ability, skill، با hunarāwand و hunarōmand که به «هنرمند» رسیده)، و آن دنبالهٔ huvnara- پارسی \"\n  \"باستان و hunara- اوستایی است: u بر جای مانده، -a پایانی افتاده و تلفظ فارسی نو به honar گراییده. نیبرگ \"\n  \"همهٔ این زنجیره را یک‌جا آورده است: «hunar … اوستایی (۱۸۳۱) hunara-؛ پارتی/مانوی hwnr «مردانگی، توانایی»؛ \"\n  \"پازند xunar؛ فارسی نو hunar». تحول معنایی: «خویِ مردانه» > «توانایی، پیشه، فضیلت» (چنان‌که در گلستان: \"\n  \"«هنر ندیمان») > «آرت/هنرهای زیبا» در دوران معاصر. «هنر» ارمنی (hunar) وام‌واژهٔ ایرانی از همین واژه است. \"\n  \"ادعای نورایی درست است.\"),\n \"sources\": [W[\"honar\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:2381\", \"status\": \"supports\",\n   \"note\": \"Borhān vol. 4, printed p. 2381 (pdf 464): 'هنر - بضم اول و فتح دوم، اوستا hunara- عظمت، استعداد، قابلیت، هندی باستان sunara-، سانسکریت sundara (زیبا، قشنگ)، پهلوی hunar، ارمنی hunar، افغانی و بلوچی hunar «… ۱۱۸» و رك: نیبرگ ص ۱۱۱؛ کردی hunar (فن، معرفت) «ژابا ص ۴۵۳»' — the exact arrow Av. hunara- > NP هنر.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p. 45 s.v. hunar\", \"stance\": \"supports\",\n   \"note\": \"'hunar [hwnr | M hwnr, N ~] virtue, ability, skill. hunarāwand … hunarōmand [… | N hunarmand]' (PHD.txt line 398); index 'skill … hunar', 'virtue hunar'.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary p. ~85 s.v. hunar\", \"stance\": \"supports\",\n   \"note\": \"'hunar [hwnl] skill 3?5, 158-9-20, 694, 845, — Av. (1831) hunara-; MPrth hwnr ‚manliness, ability‘; Paz. xunar; NP hunar' (NYB_vol2_glossary.txt line 2057); Avestan index 'hunara-: hunar' (line 5197).\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. huvnara-\", \"stance\": \"supports\",\n   \"note\": \"gives the attested Old Persian ancestor huvnara- 'skill, accomplishment' (DNb 45, 48, 51), which Wiktionary also puts in the direct line to NP honar.\"}]})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Greek\",\n \"words\": \"a-ner, andros; alex-andros; philo-anthrôpos\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Gk. ἀνήρ, gen. ἀνδρός 'man' < Proto-Hellenic *anḗr < PIE *h₂nḗr: the word-initial a- is the vocalised \"\n  \"laryngeal *h₂ (which is why Pokorny and Watkins set up the variant 'aner-' and why Nourai writes \"\n  \"'a-ner'), and the genitive comes from the zero grade *h₂n̥r-ós with the regular Greek epenthetic -d- in \"\n  \"*-nr- > -ndr-. Ἀλέξανδρος is ἀλέξω 'ward off, defend' + ἀνδρ- = 'defender of men' (Klein, p. 47, s.v. \"\n  \"Alexander: 'lit. ‚defender of men‘, fr. ἀλέξειν … and ἀνήρ, gen. ἀνδρός'); the name is already \"\n  \"Mycenaean (a-re-ka-sa-da-ra). φιλάνθρωπος 'loving mankind' is where the box weakens: its second element \"\n  \"ἄνθρωπος belongs here only on the old analysis *ἀνδρ-ωπός 'man-faced' (Walde-Pokorny II 332 cite the \"\n  \"gloss ἀρ-ώψ = ἄνθρωπος, i.e. *n̥r-ōkʷ- 'having a man's face'), which Buck calls 'much disputed' and \"\n  \"Watkins refers to the root only with the warning 'referred by some to this root … but more likely of \"\n  \"unknown origin'; Beekes treats ἄνθρωπος as Pre-Greek. Hence 'plausible' for the box: two of the three \"\n  \"words are certain, the third is a contested analysis.\"),\n \"derivation_fa\": (\n  \"یونانی ἀνήρ (اضافی ἀνδρός) «مرد» از هلنی آغازین *anḗr و آن از *h₂nḗr هندواروپایی است؛ «آ»ی آغازین بازماندهٔ \"\n  \"حنجری *h₂ است (به همین سبب پوکورنی و واتکینز گونهٔ aner- را نیز می‌آورند و نورایی «a-ner» می‌نویسد)، و صورت \"\n  \"اضافی از پایهٔ تهی *h₂n̥r-ós با میان‌جی معمولِ یونانی -d- در خوشهٔ nr > ndr پدید آمده است. Ἀλέξανδρος از \"\n  \"ἀλέξω «دور کردن، پاسداشتن» + ἀνδρ- یعنی «پاسدارِ مردان» است (کلاین، ص ۴۷). اما دربارهٔ φιλάνθρωπος جای \"\n  \"احتیاط است: پیوند ἄνθρωπος با ἀνήρ تنها بر پایهٔ تحلیل کهنِ *ἀνδρ-ωπός «مرد-روی» برجاست (والده-پوکورنی ج۲ \"\n  \"ص۳۳۲ با گواهِ ἀρ-ώψ = ἄνθρωπος)، و باک آن را «سخت مورد اختلاف» می‌خواند و واتکینز تنها با قید «برخی آن را \"\n  \"به این ریشه می‌برند، اما به احتمال بیشتر خاستگاهش ناشناخته است» می‌آورد؛ بیکس ἄνθρωπος را پیش‌یونانی \"\n  \"می‌داند. پس دو واژهٔ نخست قطعی و واژهٔ سوم پذیرفتنی-با-احتیاط است.\"),\n \"sources\": [W[\"aner\"], W[\"alex\"], W[\"philan\"]],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 781): 'ner-2, Also aner-. Man; basic sense ‚vigorous, vital, strong‘. 1. Oldest root form *aner- (with prothetic vowel) in Greek anḗr (stem andr-, from zero-grade *anr-), man: ANDRO-, -ANDROUS, -ANDRY; PHILANDER. … 3. Referred by some to this root (as if ‚having human eyes‘) but more likely of unknown origin is Greek anthrōpos… PHILANTHROPY. [Pok. 1. ner-(t)- 765.]' — supports the box but flags anthrōpos.\"},\n  {\"ref\": \"KLN:47\", \"status\": \"supports\",\n   \"note\": \"Klein's 'Alexander' falls on printed p. 47 (KLN_1966.txt: page markers 46 at line 2142, 49 at line 2186, Alexander at line 2158): 'Alexander, masc. PN. — L. Alexander, fr. Gk. Ἀλέξανδρος, lit. ‚defender of men‘, fr. ἀλέξειν … and ἀνήρ, gen. ἀνδρός, ‚man‘. … For the 2nd element in Alexander see andro-.'\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p. 73 s.v. andro-\", \"stance\": \"supports\",\n   \"note\": \"'andro-, before a vowel andr-, combining form meaning ‚man‘. — Gk. ἀνδρο-, ἀνδρ-, fr. ἀνήρ, gen. ἀνδρός … cogn. with OI. náram, náryaḥ ‚virile‘, Arm. ayr, Alb. njer, Umbr. nerus, Sabine-L. Nero, W. ner ‚hero‘, OIr. nert … Cp. also the first element in anthropo-.'\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II 332\", \"stance\": \"partial\",\n   \"note\": \"'gr. ἀνήρ, ἄνδρα, ἀνδρός ‚Mann‘, ἠνορέη ‚Mannhaftigkeit‘, ἀνδρεῖος ‚mannhaft‘ … ἀρ-ώψ· ἄνθρωπος (*n̥r-ōkʷ- ‚Mannesantlitz habend‘)' — the anthrōpos link only as a hesitant gloss-based inference.\"},\n  {\"src\": \"SYN\", \"where\": \"2.1 MAN¹, p. 80 (record 110)\", \"stance\": \"partial\",\n   \"note\": \"Buck: '3. Grk. ἄνθρωπος, etym. much disputed. But the old analysis ἀνδρ-ωπος ‚man-faced, man-like‘, fr. the stem…' — i.e. the derivation is possible but contested.\"}]})\n\nnodes.append({\n \"id\": 8, \"lang\": \"English\",\n \"words\": \"android; Alexander, Andrew; philanthropy\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"All four are Greek loans, as drawn. android: Modern Latin androides (in English 1727, then 1837 in the \"\n  \"sense 'automaton resembling a human being', first of automated chess players), from Greek andro- 'man' + \"\n  \"-eidēs 'having the form of'; popularised from c. 1950 by science-fiction writers (Etymonline). Alexander: \"\n  \"Latin Alexander < Gk. Ἀλέξανδρος, in English through Latin and the Alexander romances. Andrew: Old French \"\n  \"Andreu/Andrieu < Latin Andreas < Gk. Ἀνδρέας, a short form of a compound in ἀνδρ-, related to ἀνδρεῖος \"\n  \"'manly' (Klein s.v. Andrew). philanthropy: c. 1600, from Late Latin philanthropia < Gk. φιλανθρωπία \"\n  \"'kindliness, benevolence, love to mankind', from φιλάνθρωπος (Etymonline) — so the Greek > English step \"\n  \"the arrow asserts is beyond doubt; only the further link of ἄνθρωπος to *h₂nḗr (see node 7) is contested.\"),\n \"derivation_fa\": (\n  \"هر چهار واژه — چنان‌که در نمودار آمده — وام‌واژهٔ یونانی‌اند. android از لاتین نو androides (در انگلیسی \"\n  \"۱۷۲۷، و از ۱۸۳۷ به معنی «آدم‌واره/ماشین آدم‌نما»، نخست دربارهٔ شطرنج‌بازهای خودکار)، از andro- «مرد» + \"\n  \"-eidēs «به شکلِ»؛ Alexander از لاتین Alexander و آن از Ἀλέξανδρος؛ Andrew از فرانسهٔ کهن Andreu و لاتین \"\n  \"Andreas و آن از Ἀνδρέας (کوتاه‌شدهٔ ترکیبی با ἀνδρ-، هم‌ریشه با ἀνδρεῖος «مردانه»، کلاین)؛ philanthropy از \"\n  \"حدود ۱۶۰۰، از لاتین متأخر philanthropia و یونانی φιλανθρωπία. پس گامِ «یونانی > انگلیسی» بی‌گمان درست است؛ \"\n  \"تنها پیوند ἄνθρωπος با ریشهٔ *h₂nḗr (بنگرید به جعبهٔ یونانی) محل اختلاف است.\"),\n \"sources\": [W[\"android\"], W[\"philan\"]],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 index lists all of them under this root: 'ANDRO- ner-2', 'ANDROID' (via andro-), 'PHILANTHROPY ner-2', 'MISANTHROPE ner-2', 'LYCANTHROPE ner-2' (AHD_watkins1985.txt lines 1244-1247, 2084) — with the caveat on anthrōpos quoted at node 7.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p. 73 s.v. Andrew, Andrias, andro-\", \"stance\": \"supports\",\n   \"note\": \"'Andrew, masc. PN. — OF. Andreu, Andrieu (F. André), fr. L. Andreas, fr. Gk. Ἀνδρέας, which is rel. to ἀνδρεῖος ‚manly‘, fr. ἀνήρ, gen. ἀνδρός, ‚man‘' (KLN_1966.txt line 2710).\"},\n  {\"src\": \"FSD\", \"where\": \"vol. 1, s.v. android (running head 'android'), and vol. 3 s.v. philanthropist\", \"stance\": \"supports\",\n   \"note\": \"Funk & Wagnalls has android as a headword in the andro- family (FSD_vol1.txt, running heads 'android … angelique' around the andro-gyny entries) and philanthropist in vol. 3; both are treated as Greek compounds of andr-/anthrōpos.\"},\n  {\"src\": \"SKT\", \"where\": \"Concise Skeat\", \"stance\": \"silent\",\n   \"note\": \"Skeat's concise dictionary has no entries for android, philanthropy, Andrew or Alexander (grep of SKT.txt: only an unrelated 'St. Andrew's cross' under saltire).\"}]})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Syriac\",\n \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"The box is printed empty (no language-internal word given): it simply asserts that the Greek name reached \"\n  \"Arabic through a Syriac/Aramaic intermediary. That is Nöldeke's proposal (ZA xvii, 84), reported by \"\n  \"Jeffery, Foreign Vocabulary of the Qur'ān, pp. 51-52: 'None of these suggestions, however, comes as near \"\n  \"as that put forward by Nöldeke … that it is the Arabic form of Ἀνδρέας filtered through a Syriac medium. \"\n  \"In Syriac we find various forms of the name … this latter being the form in Christian-Palestinian, and \"\n  \"from this by the coalescing of the n and d we get the Ar. إدريس.' So the intermediary is Syriac \"\n  \"ʾAndrēʾā / ʾAndrēwos and above all the Christian-Palestinian Aramaic form ʾdrys. The step is a \"\n  \"reconstruction of a transmission route rather than a documented equation, hence 'plausible'.\"),\n \"derivation_fa\": (\n  \"این جعبه در چاپ کتاب تهی است و هیچ صورت سریانی نمی‌آورد؛ تنها می‌گوید که نام یونانی از راه سریانی/آرامی به \"\n  \"عربی رسیده است. این همان فرضیهٔ نولدکه (ZA ج۱۷ ص۸۴) است که جفری در «واژه‌های دخیل در قرآن» (ص ۵۱-۵۲) نقل \"\n  \"می‌کند: هیچ‌یک از پیشنهادهای دیگر به‌اندازهٔ رأی نولدکه پذیرفتنی نیست که «إدريس» صورت عربیِ Ἀνδρέας است که \"\n  \"از میانجی سریانی گذشته، و از صورت آرامیِ فلسطینی-مسیحی ʾdrys با درآمیختن n و d به «إدريس» رسیده است. پس \"\n  \"میانجی، سریانی ʾAndrēʾā/ʾAndrēwos و بالاتر از همه صورت فلسطینی-مسیحی است. چون این بازسازیِ راهِ وام‌گیری \"\n  \"است نه برابری مستند، حکم «با احتیاط پذیرفتنی» است.\"),\n \"sources\": [W[\"idris\"]],\n \"ref_check\": [\n  {\"ref\": \"VDQ:108\", \"status\": \"supports\",\n   \"note\": \"VDQ (Badre'i's Persian translation of Jeffery) is only on noorlib, whose viewer is JavaScript-rendered, so the substance was checked in the original, FVQ pp. 51-52 (FVQ_pages.txt lines 2190-2260): Nöldeke's Ἀνδρέας-through-Syriac derivation, with the Syriac and Christian-Palestinian forms listed — exactly what the Syriac box asserts.\"}],\n \"consulted\": [\n  {\"src\": \"FVQ\", \"where\": \"pp. 51-52 s.v. Idrīs\", \"stance\": \"supports\",\n   \"note\": \"'that it is the Arabic form of Ἀνδρέας filtered through a Syriac medium. In Syriac we find various forms of the name … this latter being the form in Christian-Palestinian, and from this by the coalescing of the n and d we get the Ar. إدريس' (Jeffery, note 2 there refers to Nöldeke ZDMG xii, 706 and ZA xvii).\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. Enoch, Andrew\", \"stance\": \"silent\",\n   \"note\": \"Klein has 'Enoch … fr. Heb. Ḥanōkh' (line 13216) and 'Andrew … fr. Gk. Ἀνδρέας' but says nothing about Idrīs or a Syriac mediation, so no independent support there.\"}]})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Arabic\",\n \"words\": \"Edrîs\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Arabic إدريس Idrīs is the Qur'ānic prophet (19:56-57; 21:85). Muslim tradition identifies him with Enoch \"\n  \"and takes the name from the root د ر س 'to study' — an etymology already rejected by the philologists \"\n  \"(Jeffery: 'The fallacy of this derivation was … pointed out by some of the philologers, as Zam. on xix, \"\n  \"57, shows, and that the name was of foreign origin was recognized by al-Jawālīqī, Muʿarrab, 8; Qāmūs, i, \"\n  \"215'), and impossible in form because the pattern ʾifʿīl was no longer productive. Nöldeke's derivation \"\n  \"from Greek Ἀνδρέας through Syriac/Christian-Palestinian ʾdrys (loss of -n- by coalescence with d) is the \"\n  \"one Jeffery prefers, and it is Nourai's. But it is not the only candidate: Ἔσδρας/Ezra (Casanova, \"\n  \"Torrey), Ποιμάνδρης (Albright), Atrahasis (Montgomery) and Hebrew dōrēš are all still in the field, and \"\n  \"Wiktionary heads the entry 'Uncertain, formally a borrowing'. So the arrow is the best-supported \"\n  \"hypothesis but not established: 'plausible'.\"),\n \"derivation_fa\": (\n  \"«إدريس» نام پیامبری در قرآن است (مریم ۵۶-۵۷؛ انبیاء ۸۵). سنت اسلامی او را همان «اخنوخ» می‌داند و نام را از \"\n  \"ریشهٔ «درس» می‌گیرد؛ اما همین ریشه‌شناسی عامیانه را زبان‌شناسان کهن رد کرده‌اند (زمخشری در تفسیر مریم ۵۷؛ \"\n  \"جوالیقی، المعرّب ص۸؛ قاموس ج۱ ص۲۱۵ آن را واژهٔ بیگانه می‌شمارند) و از نظر ساخت هم وزن «إفعیل» در آن دوره \"\n  \"زاینده نبوده است. رأی نولدکه — که جفری نیز آن را بهترین می‌داند و نورایی همان را آورده — این است که \"\n  \"إدريس از Ἀνδρέας یونانی از راه سریانی/آرامی فلسطینی (ʾdrys، با افتادن n در برخورد با d) آمده است. با این \"\n  \"همه پیشنهادهای دیگری هم زنده‌اند: Ἔσδρας (عزرا)، Ποιμάνδρης، اترحسیس، و عبری dōrēš؛ ویکی‌واژه نیز سرآغاز \"\n  \"مقاله را «نامعلوم، صورتاً وام‌واژه» گذاشته است. پس ادعای نورایی محتمل‌ترین فرض است، نه قطعی.\"),\n \"sources\": [W[\"idris\"]],\n \"ref_check\": [\n  {\"ref\": \"VDQ:108\", \"status\": \"supports\",\n   \"note\": \"checked in the original FVQ pp. 51-52 (noorlib's VDQ viewer is JS-only): Jeffery's entry Idrīs sets out exactly the Greek Ἀνδρέας > Syriac > Arabic إدريس route as the best proposal, while listing the rivals.\"}],\n \"consulted\": [\n  {\"src\": \"FVQ\", \"where\": \"pp. 51-52 s.v. Idrīs\", \"stance\": \"supports\",\n   \"note\": \"'Nöldeke has pointed out, ZA, xvii, 83, that we have no evidence that Jews or Christians ever called Enoch by any name derived from … Casanova … suggested that the reference was to Ἔσδρας … None of these suggestions, however, comes as near as that put forward by Nöldeke in ZA, xvii, 84, that it is the Arabic form of Ἀνδρέας filtered through a Syriac medium.'\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. Enoch\", \"stance\": \"silent\",\n   \"note\": \"no Idrīs entry in Klein; his Enoch is derived from Hebrew Ḥanōkh, which bears on the identification but not on the name's form.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\",\n   \"note\": \"grep of AFM_pages.txt for إدريس gives no hit — Addi Shir treats Persian loans in Arabic, and does not discuss this name.\"}]})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Persian\",\n \"words\": \"Edrîs «إدریس»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"The Persian word is a straightforward Arabic loan of Islamic religious vocabulary: Arabic إدريس > Persian \"\n  \"Edrīs, kept in its Arabic spelling with hamza (the printed page shows إِدریس, so the JSON's «إدریس» is \"\n  \"faithful), used both of the Qur'ānic prophet and as a man's name. The Molavī couplet the book quotes \"\n  \"— «عیسی و ادریس بر گردون شدند / با ملایک چون که هم جنس آمدند» — alludes to Q 19:57, 'we raised him to a \"\n  \"high place', the very verse that made Idrīs a figure of ascent in Persian poetry. The Arabic > Persian \"\n  \"direction is certain; only the ultimate Greek origin upstream (nodes 9-10) is a hypothesis.\"),\n \"derivation_fa\": (\n  \"«ادریس» فارسی وام‌واژه‌ای عربی از گنجینهٔ واژگان دینی اسلامی است: عربی إدريس > فارسی Edrīs، که با همان \"\n  \"املای عربی (با همزه) به کار می‌رود — صفحهٔ چاپی نیز «إِدریس» دارد، پس خوانش داده‌ها درست است — هم برای \"\n  \"پیامبر قرآنی و هم به‌عنوان نام مردانه. بیت مولوی که کتاب می‌آورد («عیسی و ادریس بر گردون شدند...») اشاره به \"\n  \"آیهٔ ۵۷ سورهٔ مریم («و رفعناه مکاناً علیّاً») دارد؛ همان آیه‌ای که ادریس را در شعر فارسی نمادِ فرارَوی کرده \"\n  \"است. گامِ «عربی > فارسی» قطعی است و تنها خاستگاه یونانی در بالادست (جعبه‌های سریانی و عربی) فرضی است.\"),\n \"sources\": [W[\"idris\"]],\n \"ref_check\": [\n  {\"ref\": \"MON5:109\", \"status\": \"not_checked\",\n   \"note\": \"Moʿin's vol. 5 (اعلام) has no scan in the local library (refs_online.json lists no BQT-style scan for MON vols 5-6) and the online Moʿin at vajehyab/abadis serves only the lexicon volumes and is JavaScript-rendered — both archived fetches returned site chrome only. The page number is at least internally consistent: ادریس (a-d-r) at 109 precedes اسکندر (a-s-k) at 144.\"}],\n \"consulted\": [\n  {\"src\": \"FVQ\", \"where\": \"pp. 51-52\", \"stance\": \"supports\",\n   \"note\": \"confirms the name's Qur'ānic status and Arabic form (Q 19:57 'God raised him to a high place'), which is what the Persian word continues.\"},\n  {\"src\": \"MON\", \"where\": \"MON_part1/part2 (lexicon volumes)\", \"stance\": \"silent\",\n   \"note\": \"grep of the two local Moʿin text files for ادریس finds only the plant name شجر ادریس (s.v. محلب); the proper-name entry is in vol. 5, which is not on disk.\"}]})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Arabic\",\n \"words\": \"Eskander\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Arabic (al-)Iskandar 'Alexander' is a borrowing of Greek Ἀλέξανδρος in which the initial Ἀλ- was \"\n  \"reanalysed as the Arabic definite article al-, leaving a stem Iskandar with prothetic i- before the \"\n  \"cluster sk- (Wiktionary s.v. الإسكندر: 'Borrowed from Ancient Greek Ἀλέξανδρος. The initial Ἀλ- was \"\n  \"reanalyzed by Arabic speakers as the Arabic definite article ال (al-)'); Lokotsch (no. 4182, s.v. \"\n  \"serasker) notes the same thing as 'Metathesis von k und s wie in ar. Iskandar < Alexander'. The name was \"\n  \"familiar in Arabia before Islam through the Syriac Alexander romance — Jeffery, FVQ 288-289 (s.v. Yājūj \"\n  \"wa Mājūj): 'Both passages are reflections of Syriac legends concerning Alexander the Great' — so the \"\n  \"Greek > (Syriac) > Arabic path Nourai draws is right. Nourai gives this box no reference of his own.\"),\n \"derivation_fa\": (\n  \"«(الـ)إسكندر» عربی وام‌گیریِ Ἀλέξανδρος یونانی است، با این ویژگی که «Ἀλ» آغازین را عرب‌زبانان حرف تعریف \"\n  \"«ال» پنداشته‌اند و ستاکِ «إسكندر» با همزهٔ آغازین پیش از خوشهٔ «سک» بر جای مانده (ویکی‌واژه، ذیل الإسكندر). \"\n  \"لوکوچ نیز (شمارهٔ ۴۱۸۲) از «قلبِ ک و س، چنان‌که در عربیِ Iskandar < Alexander» یاد می‌کند. این نام پیش از \"\n  \"اسلام از راه «داستان اسکندر» سریانی در عربستان شناخته بود — جفری (ص ۲۸۸-۲۸۹، ذیل یأجوج و مأجوج): «هر دو \"\n  \"آیه بازتاب افسانه‌های سریانی دربارهٔ اسکندر است». پس راهِ «یونانی > (سریانی) > عربی» که نورایی کشیده درست \"\n  \"است. نورایی برای این جعبه هیچ مرجعی نداده است.\"),\n \"sources\": [W[\"aliskandar\"], W[\"alex\"]],\n \"ref_check\": [\n  {\"ref\": \"(none)\", \"status\": \"not_checked\",\n   \"note\": \"the printed box carries no reference (the JSON's refs field is null), so there is nothing of Nourai's own to check; the claim was verified against Wiktionary, Lokotsch and Jeffery instead.\"}],\n \"consulted\": [\n  {\"src\": \"LKT\", \"where\": \"no. 4182 s.v. serasker\", \"stance\": \"supports\",\n   \"note\": \"Lokotsch: '… mit vorgeschlagenem ʿain und Metathesis von k und s wie in ar. Iskandar < Alexander'.\"},\n  {\"src\": \"FVQ\", \"where\": \"pp. 288-289 s.v. Yājūj wa Mājūj\", \"stance\": \"partial\",\n   \"note\": \"'Both passages are reflections of Syriac legends concerning Alexander the Great' — documents the Syriac-mediated route by which the Alexander material (and name) reached pre-Islamic Arabia, though Jeffery does not treat the name Iskandar itself.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir\", \"stance\": \"silent\",\n   \"note\": \"no إسكندر entry (grep of AFM_pages.txt) — expected, since the name is a Greek and not a Persian loan in Arabic.\"}]})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\",\n \"words\": \"Eskandar «اسکندر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"NP Eskandar/Sekandar «اسکندر» is the Arabic-shaped form of the name, as the arrow says: Wiktionary \"\n  \"(s.v. اسکندر) has 'Inherited from Middle Persian (swkndl /Skandar ~ Sokandar/), from Arabic إِسْكَنْدَر, \"\n  \"from Ancient Greek Ἀλέξανδρος', citing Nyberg and MacKenzie; Nyberg's glossary is explicit: 'Sokandar \"\n  \"[swkndl] = Alaksandar … Probably the Arab. Iskandar with elision of ʾI- and inserting of an auxiliary \"\n  \"vowel between s and k, cf. Sikandar < Iskandar'. The older, direct Greek loan also existed in Pahlavi \"\n  \"(MacKenzie: 'Aleksandar [ʾlksndl | M ʾlxsyndr, N Iskandar] Alexander (of Macedon)', with '*Skandar \"\n  \"[swkndl | N sikandar] = Aleksandar'), so Persian has both layers; the form with initial e-/i- that \"\n  \"Nourai prints is the Arabic one, and the poetic doublet سکندر shows the aphaeresis of that vowel.\"),\n \"derivation_fa\": (\n  \"«اسکندر» فارسی همان صورتِ عربی‌شدهٔ نام است، چنان‌که نمودار می‌گوید: ویکی‌واژه (ذیل اسکندر) می‌نویسد از \"\n  \"فارسی میانهٔ swkndl (Skandar/Sokandar)، از عربی إسْكَنْدَر، از یونانی Ἀλέξανδρος، و به نیبرگ و مکنزی استناد \"\n  \"می‌کند. نیبرگ صریح است: «Sokandar [swkndl] = Alaksandar … احتمالاً همان Iskandar عربی است با افتادن ʾI- و \"\n  \"افزودن واکهٔ میانجی میان s و k، مانند Sikandar < Iskandar». وام‌واژهٔ کهن‌تر و بی‌واسطهٔ یونانی نیز در پهلوی \"\n  \"بود (مکنزی: Aleksandar «اسکندر مقدونی»، و *Skandar = Aleksandar)، پس فارسی هر دو لایه را دارد؛ صورتی که \"\n  \"نورایی آورده همان صورت عربی است و گونهٔ شعری «سکندر» نشان افتادن واکهٔ آغازین است. ادعا درست است.\"),\n \"sources\": [W[\"eskandar\"], W[\"eskandar_ot\"], W[\"aliskandar\"]],\n \"ref_check\": [\n  {\"ref\": \"MON5:144\", \"status\": \"not_checked\",\n   \"note\": \"same reason as MON5:109: Moʿin's vol. 5 (اعلام) is not in the local library and the online Moʿin (vajehyab/abadis, archived) is JS-rendered and lexicon-only. The local Moʿin lexicon files mention اسکندر only in compounds (سنای اسکندری، زندان سکندر، هتر «سواران اسکندر مقدونی»), not as a headword.\"}],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Glossary p. 177 s.v. Sokandar\", \"stance\": \"supports\",\n   \"note\": \"'Sokandar [swkndl] = Alaksandar, 113ʹ, 114ʹ. — Probably the Arab. Iskandar with elision of ʾI- and inserting of an auxiliary vowel between s and k, cf. Sikandar < Iskandar' (NYB_vol2_glossary.txt line 3461).\"},\n  {\"src\": \"PHD\", \"where\": \"pp. 8 and 75\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie: 'Aleksandar [ʾlksndl | M ʾlxsyndr, N Iskandar] Alexander (of Macedon)' and '*Skandar [swkndl | N sikandar] = Aleksandar'.\"}]})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ner 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₂nḗr 'man; power, force, vital energy' (Pokorny ner-1(t)-/aner-, p. 765; Watkins ner-2)\",\n \"note\": (\n  \"Root, language label and gloss are all right: Pokorny 765 heads the entry 'ner-1(t)-, aner-' with the \"\n  \"meaning 'vital energy; man' — word for word Nourai's 'vital energy, man' — and Watkins/AHD gives \"\n  \"'ner-2, Also aner-. Man; basic sense ‚vigorous, vital, strong‘ [Pok. 1. ner-(t)- 765]'. Modern \"\n  \"reconstruction writes *h₂nḗr, the initial laryngeal being what surfaces as the a- of Greek ἀνήρ (and of \"\n  \"Nourai's variant spelling 'a-ner'). Nourai's numbering 'Ner 1' matches Pokorny's, who has three \"\n  \"homophonous roots ner- (1 'man', 2 'under/north', 3 'to conceal'). Two things to flag for the data \"\n  \"owner rather than for scholarship: (a) the reference BQT:1796 in the Persian nar/Narīmān/nīrū box does \"\n  \"not exist as cited — printed p. 1796 of the Moʿin edition is in the گرز… stretch of vol. 3; the other \"\n  \"three page numbers (2126, 2132, 2225) are exactly right. (b) The printed page has a FOURTH box in the \"\n  \"nāirī row — an entirely blank box, no language header and no words, joined by a line to the Pahlavi \"\n  \"nâyrig box — which the extraction dropped; it carries no information, but the JSON has no node for it, \"\n  \"so the chart in the repository is one (empty) box short of the page. Everything else on the page \"\n  \"(words, glosses, scripts, refs, the Molavī quotation) matches the print.\"),\n \"note_fa\": (\n  \"ریشه، برچسب زبان و معنا هر سه درست است: پوکورنی در ص ۷۶۵ سرواژهٔ «ner-1(t)-, aner-» را با معنای «نیروی \"\n  \"زندگی؛ مرد» آورده — همان «vital energy, man» نورایی — و واتکینز نیز «ner-2 … مرد؛ معنای پایه: پرتوان، \"\n  \"زنده، نیرومند» می‌نویسد. بازسازی امروزی *h₂nḗr است و همان حنجریِ آغازین است که در یونانی ἀνήρ به «آ» بدل \"\n  \"شده (و نورایی هم آن را «a-ner» نوشته است). شمارهٔ «Ner 1» با شمارگذاری پوکورنی می‌خواند، که سه ریشهٔ \"\n  \"هم‌آوای ner- دارد. دو نکته برای صاحب داده، نه برای بحث علمی: نخست، ارجاع BQT:1796 در جعبهٔ «نر/نریمان/نیرو» \"\n  \"نادرست است — صفحهٔ ۱۷۹۶ چاپ معین در بخش «گرز…» جلد سوم است — حال آنکه سه شمارهٔ دیگر (۲۱۲۶، ۲۱۳۲، ۲۲۲۵) \"\n  \"دقیقاً درست‌اند. دوم، در صفحهٔ چاپی در ردیفِ nāirī جعبهٔ چهارمی هست که کاملاً تهی است (بی نام زبان و بی \"\n  \"واژه) و با خطی به جعبهٔ «nâyrig» پهلوی پیوسته است؛ این جعبه در استخراج نیامده است. باقی صفحه (واژه‌ها، \"\n  \"معناها، خط فارسی، ارجاع‌ها و بیت مولوی) با چاپ مطابق است.\"),\n \"sources\": [W[\"pie\"], W[\"aner\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:765\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt line 62647: 'Root / lemma: ner-1(t)-, aner- … Meaning: vital energy; man … References: WP. II 332 f., WH. II 164 f., Trautmann 197 f. … Page(s): 765'. The page also carries ner-2 'under' (765-766), so 765 is the right page for Nourai's Ner 1.\"}],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. II 332-333\", \"stance\": \"supports\",\n   \"note\": \"'1. ner-, aner- (aner-?) Mann' with the full Indo-Iranian, Greek, Italic, Celtic, Germanic and Baltic material — the source Pokorny himself cites as WP. II 332 f.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ner-2\", \"stance\": \"supports\",\n   \"note\": \"'ner-2, Also aner-. Man; basic sense ‚vigorous, vital, strong‘ … [Pok. 1. ner-(t)- 765.]'\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. ner- (1), nertos\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'ner- (1) ‚man; male‘. WP II, 332' and 'nertos ‚manly; manliness, virtue, strength‘ … Oss. nart ‚hero‘' — the 'vital energy' half of the gloss is carried by these -to- derivatives.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 2.21 'MAN²', p. 81\", \"stance\": \"supports\",\n   \"note\": \"'2. IE *ner-, nert- ‚strength, might‘ … Various cognates, as Ir. nert ‚strength, might‘, show that the notion of ‚strength‘ is dominant … Walde-P. 2.332f.'\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 361,\n \"book_page\": 331,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-361.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk361.py"
}
```


### [2026-09-07T19:49:10.710Z] TOOL RESULT

```
written
```


## [2026-09-07T19:49:14.041Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-361.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 361"
}
```


### [2026-09-07T19:49:15.470Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 4, 'confirmed': 9}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 15, 'not_found': 1, 'not_checked': 3}
books consulted: {'supports': 25, 'silent': 9, 'partial': 3} | by book: {'BRT': 4, 'WLD': 4, 'PHD': 4, 'KLN': 4, 'FVQ': 4, 'NYB': 3, 'MON': 2, 'SYN': 2, 'KNT': 2, 'AFM': 2, 'IEC': 1, 'HRN': 1, 'ARY': 1, 'FSD': 1, 'SKT': 1, 'LKT': 1}
```


## [2026-09-07T19:49:23.637Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg361.png data/verification/sources/refs/ocr/BOOK/361.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head -5 && git status --short | head"
}
```


### [2026-09-07T19:49:23.744Z] TOOL RESULT

```
total 16968
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  7 15:49 .
drwxrwxr-x 13 sfmqrb sfmqrb   4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
?? data/verification/page-361.json
```


## [2026-09-07T19:49:47.715Z] AGENT

Done. `verify_check.py 361` reports 13/13 nodes, 0 PROBLEM lines.

**Page 361 (book p. 331) — root "Ner 1" (PIE *h₂nḗr), 1 entry, 13 nodes**

- Verdicts: root **confirmed**; nodes **9 confirmed, 4 plausible**, 0 disputed, 0 transcription_suspect.
- Ref checks: 15 supports, 1 not_found, 3 not_checked. Books consulted: 25 supports, 3 partial, 9 silent (BRT, WLD, POK, AHD, IEC, SYN, KNT, PHD, NYB, HRN, HUB, SNS, BQT, ARY, KLN, FSD, SKT, FVQ, LKT, MON).
- Root confirmed verbatim: Pokorny 765 "ner-1(t)-, aner-: vital energy; man"; Watkins ner-2; Wiktionary *h₂nḗr "man / power, force, vital energy".
- `plausible` items (why): **#1 Avestan** — nar/nairya/naire-manā̊ all attested (BRT), but *nairyava-* is **not attested in the Avesta*; Horn 238 cites it with an asterisk (PIr. *naryawa-). **#7 Greek** — anēr/andros and Alexandros certain (KLN:47), but *philo-anthrôpos* rests on the contested *ἀνδρ-ωπός analysis (Watkins: "more likely of unknown origin"; Buck "much disputed"). **#9 Syriac / #10 Arabic Edrîs** — Nöldeke's Ἀνδρέας-via-Syriac route is the best-founded proposal (Jeffery FVQ 51-52, = Nourai's VDQ:108) but competes with Ἔσδρας/Ποιμάνδρης/Atrahasis; Wiktionary heads it "uncertain".
- Fully confirmed chains: nar < MP nar; Narīmān < MP Narēmān < Av. naire.manaŋh-; nīrū < MP nērōg (< *naryawa-ka-) — Moʿin's own footnote at BQT 2225 gives exactly Av. nairyava- > nērōk > nīrū; nāirī- > MP nāyrīg (SNS index: nāyrīg 264/19, nāyrīg zan 264/24); hu-nara > honar with the attested OP huvnara- (Kent, DNb 45/48/51); Arabic (al-)Iskandar with Ἀλ- reanalysed as the article (Lokotsch 4182) > NP اسکندر (Nyberg "Sokandar", MacKenzie *Skandar).

**Owner action items**
- **Bad citation in the book (not extraction):** `BQT:1796` in the Persian nar/Narīmān/nīrū box points to the گرز… stretch of vol. 3 (p. 1793 گرد/گرزن, p. 1797 گرست) — nothing about نر. The other three (2126, 2132, 2225) are exact.
- **Extraction gap:** the printed page has a **fourth, completely blank box** in the nāirī row (no language header, no words, joined by a line to the Pahlavi *nâyrig* box) that `data/extracted/batch/page-361.json` omits entirely, so there is no node id for it. Carries no content, but the chart is one box short of the print. Page image kept at `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/361.png`.
- `MON5:109` / `MON5:144` unverifiable: Moʿin vol. 5 (اعلام) has no scan on disk and vajehyab/abadis are JS-rendered (both fetches archived, returned chrome only). Page numbers are at least internally consistent (ادریس 109 < اسکندر 144).
- All web sources archived via `fetch_source.py` (14 URLs); file written to `/home/sfmqrb/git/rishe/data/verification/page-361.json` (untracked, not committed).
