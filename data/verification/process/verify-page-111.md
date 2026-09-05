# Verification process log — verify-page-111


## [2026-09-05T17:31:16.756Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 111 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-111.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-111.json. Write /home/sfmqrb/git/rishe/data/verification/page-111.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 111` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:31:18.221Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:31:18.931Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:31:18.949Z] TOOL RESULT

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


## [2026-09-05T17:31:19.132Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-111.txt"
}
```


### [2026-09-05T17:31:19.159Z] TOOL RESULT

```
1	=== PDF page 111 (book page 81) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dei, Deiw, Dyeu, Dyě : to shine, used to describe bright days and heavenly spirits  (refs POK:183; AHD)
4	#1 (parent #0) [Avestan] refs=POK:185; AHD:1511; BQT:917; SNB:126 | daěv, daěvoh : the meaning, originally, was God but later, when Zoroaster introduced Ahuramazda, old gods were considered as demons.
5	  #2 (parent #1) [Persian] refs=HRN:133 | dîv «دیو» : demon ; dîvâneh «دیوانه» : mad
6	#3 (parent #0) [Sanskrit] refs=POK:183; AHD | dî, dîp : to shine
7	  #4 (parent #3) [Pahlavi] refs=BQT:908; SNS:313 | děpâk, děbâg : a colorful type of cloth | NOTE: BQT is not certain about this derivation.
8	    #5 (parent #4) [Persian] refs=BQT:908 | dîbâ «دیبا» : a colorful cloth | extra: دیبه ، دیباج | NOTE: See root "Zay" for another possible derivation.
9	#6 (parent #0) [Latin] refs=AHD | deus : God ; diěs : day ; jovis, jŭlius : from Jupiter
10	  #7 (parent #6) [French] refs=AHD:707 | journal : daily paper
11	    #8 (parent #7) [Persian] refs=MON:1778 | žornâl «ژورنال»
12	    #9 (parent #7) [English] refs=AHD:707 | journal
13	  #10 (parent #6) [English] refs=AHD | deity, divine, dial, diary, journey, Jupiter, July, Julian, Julius
14	#11 (parent #0) [Germanic] refs=AHD | tiwaz : god of sky
15	  #12 (parent #11) [English] refs=None | Tuesday
16	#13 (parent #0) [Greek] refs=AHD | Zeus : ruler of the heavens
17	  #14 (parent #13) [English] refs=AHD | Zeus
18	
```


## [2026-09-05T17:31:22.617Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-111.json | head -200",
 "description": "Read page-111 source JSON"
}
```


## [2026-09-05T17:31:23.194Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T17:31:24.370Z] TOOL RESULT

```
{
    "pdf_page": 111,
    "book_page": 81,
    "entries": [
        {
            "root": {
                "name": "Dei, Deiw, Dyeu, Dy\u011b",
                "lang": "Indo-European",
                "refs": "POK:183; AHD",
                "gloss": "to shine, used to describe bright days and heavenly spirits"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:185; AHD:1511; BQT:917; SNB:126",
                    "words": [
                        {
                            "translit": "da\u011bv, da\u011bvoh",
                            "gloss": "the meaning, originally, was God but later, when Zoroaster introduced Ahuramazda, old gods were considered as demons.",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "HRN:133",
                    "words": [
                        {
                            "translit": "d\u00eev",
                            "gloss": "demon",
                            "script": "\u062f\u06cc\u0648"
                        },
                        {
                            "translit": "d\u00eev\u00e2neh",
                            "gloss": "mad",
                            "script": "\u062f\u06cc\u0648\u0627\u0646\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0645\u0627 \u0628\u0647 \u0633\u0644\u06cc\u0645\u0627\u0646 \u062e\u0648\u0634\u06cc\u0645 \u060c \u062f\u06cc\u0648 \u0648 \u067e\u0631\u06cc \u06a9\u0648 \u0645\u0628\u0627\u0634 - \u062d\u0633\u0646 \u062a\u0648 \u0627\u0632 \u062d\u062f \u06af\u0630\u0634\u062a\u060c \u0634\u06cc\u0648\u0647 \u06af\u0631\u06cc \u06a9\u0648 \u0645\u0628\u0627\u0634",
                        "poet": "Molav\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "POK:183; AHD",
                    "words": [
                        {
                            "translit": "d\u00ee, d\u00eep",
                            "gloss": "to shine",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Pahlavi",
                    "refs": "BQT:908; SNS:313",
                    "words": [
                        {
                            "translit": "d\u011bp\u00e2k, d\u011bb\u00e2g",
                            "gloss": "a colorful type of cloth",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "BQT is not certain about this derivation.",
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "BQT:908",
                    "words": [
                        {
                            "translit": "d\u00eeb\u00e2",
                            "gloss": "a colorful cloth",
                            "script": "\u062f\u06cc\u0628\u0627"
                        }
                    ],
                    "script_extra": "\u062f\u06cc\u0628\u0647 \u060c \u062f\u06cc\u0628\u0627\u062c",
                    "note": "See root \"Zay\" for another possible derivation.",
                    "quote": {
                        "text": "\u062f\u0631 \u06af\u0646\u062c \u062f\u06cc\u0646\u0627\u0631 \u0648 \u067e\u0631\u0645\u0627\u06cc\u0647 \u062a\u0627\u062c - \u0647\u0645\u0627\u0646 \u06af\u0648\u0647\u0631 \u0648 \u062f\u06cc\u0628\u0647 \u0648 \u062a\u062e\u062a \u0648 \u062a\u0627\u062c",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "deus",
                            "gloss": "God",
                            "script": null
                        },
                        {
                            "translit": "di\u011bs",
                            "gloss": "day",
                            "script": null
                        },
                        {
                            "translit": "jovis, j\u016dlius",
                            "gloss": "from Jupiter",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "French",
                    "refs": "AHD:707",
                    "words": [
                        {
                            "translit": "journal",
                            "gloss": "daily paper",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "Persian",
                    "refs": "MON:1778",
                    "words": [
                        {
                            "translit": "\u017eorn\u00e2l",
                            "gloss": null,
                            "script": "\u0698\u0648\u0631\u0646\u0627\u0644"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 7,
                    "lang": "English",
                    "refs": "AHD:707",
                    "words": [
                        {
                            "translit": "journal",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 6,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "deity, divine, dial, diary, journey, Jupiter, July, Julian, Julius",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
```


### [2026-09-05T17:31:24.398Z] TOOL RESULT

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


## [2026-09-05T17:31:28.266Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-111.json | tail -70; echo ---; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','SNB','SNS','HRN','MON']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:900])\n\""
}
```


## [2026-09-05T17:31:29.003Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -40; echo ---; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-05T17:31:30.111Z] TOOL RESULT

```
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "tiwaz",
                            "gloss": "god of sky",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "Tuesday",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Zeus",
                            "gloss": "ruler of the heavens",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 13,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Zeus",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
---
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
SNB {"title": "H. Kowsar, Sang-nebeshteh-ha Sokhan Miguyand, Iranian Military Press (1960s)", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
```


### [2026-09-05T17:31:30.149Z] TOOL RESULT

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
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
page-56.json
page-57.json
page-58.json
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
```


## [2026-09-05T17:31:36.678Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==192' POK_01.txt | head -60",
 "description": "Print Pokorny p.183"
}
```


## [2026-09-05T17:31:36.948Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==194' POK_01.txt | head -70",
 "description": "Print Pokorny p.185"
}
```


### [2026-09-05T17:31:38.254Z] TOOL RESULT

```
  ,als  wie*  =  osk.  paUj umbr.  pane  ,quam',  ebenso  osk.  pwn,  umbr.  pon(n)e  ,quom*  {^qiiom-de), lat.  in-de  ,von  da*  {*im-de),  un-de  ,woher*;  gr.  6s  ,aber*;  gr.  örj  ,eben,  nun, gerade,  gewiß',  }j-dr]  ,schon*,  ifrsi-ö^  ,quoniam';  dal  hinter  Fragewörtern ,(was)  denn?';
idg.  *de  steckt  auch  im  air.  Artikel  in-d  (*sijid-os^  idg.  *8em-de)',
ital.  -*dam  in  lat.  qui-dam,  quon-damj  umbr.  ne-rsa  ,donec'  (wohl  er- starrter Akk.  f.  *ne-däm  , nicht  die  Weile*;  daneben  m.  oder  n.  in:);
lat.  dum  (*dom)  ,noch*,  als  Konj.  , während,  indes,  indem',  ursprgl.  de- monstratives ,dann',  vgl.  etiam-dum,  interdum,  nöndum,  agedum  (:  gr.  äye 6rj),  manedum,  quidum  ,wie  so?'  u.  dgl.,  dann  in  relativ-konjunktioneller Bed.,  wie  auch  in  diimmodo,  dumne,  dumtaxat)  osk.  isidum  ,ldem*  ist aber  in  is-id-um  zu  zerlegen,  wie  auch  in  lat.  idemj  quidem,  tandem^ tantusdem,  totidem  kein  mit  dum  aus  *dom  ablautendes  -dem  anzuerkennen ist;  id-em  aus  *id-em  =  ai.  id-dm  ,eben  dieses',  vgl.  osk.  is-id-um,  wie quid-em  aus  *quid-om  =  osk.  pid-um,  und  infolge  der  Silbentrennung i-dem  wurde  -dem  als  Identitätspartikel  gefühlt  und  wucherte  weiter);
aber  die  Grundbedeutung  von  dum  ist  ,ein  Weilchen*,  weshalb  das  u vielleicht  alt  ist  (vgl.  düdum)  und  dum  zur  Wz.  deud-  gehört  (EiVP  288  f.).
idg.  *dö  ursprgl.  , herzu*  in  lat.  dö-ni-cum  (altertümlich),  dönec  (^dö-ne-que), seit  Lukrez  auch  dönique  ,so  lange  als,  bis  daß,  bis  endlich',  aber  auch ,dann*  {dö-  gleichbed.  mit  ad-,  ar-  in  umbr.  ar-ni-po  ,quoad*  aus  *ad-ne- qvom)  und  in  quandö  ,wann*  =  umbr.  panupel  ,quandoque';  air.  do,  du, acymr.    di    (=  di)^    corn.    de    ,zu*    aus    *dü   (in   gall.    du-ci   .und'),    Thur-
182
neysen  Grammar  506;    ags.    tö,   as.    to   (te,    ti),    ahd.  zuo   (za,    ze,   zi-^  ^j^
■    kürzeren  Formen  sind  trotz  Solmsen  KZ.  35,  471  nicht  als  bereits  uri{Jr
Ablautvarianten  aufzufassen),  nhd.  zu  (got.  du  ,zu'  mit  Dat.  und  Präver}
z.  B.  in   du-ginnan  , beginnen',    scheint  proklitische  Entw.  aus  *2^ö(?),   y^
Brugmann  11^  2,   812   als   unaufgeklärt   bezeichnet);    alit.    do   Präp.   ^^^
Präf.    ,zu';    aksl.   da    ,so,    und,  aber;    daß'  (Bed.-Entw.  ,*dazu'   —   ,no(
und^,  woraus  dann  die  unterordnende  Anknüpfung);  anders  Pedersen  Tech.
Daneben  idg.  *(iö  in  aksl.  do  ,bis,  zu'.
Lit.   da-,  perfektivierendes  Verbalpräfix,  und  lett.  da  ,bis  —  zu',  aucj
Verbalpräf.  z.  B.  in  da-iet  »hinzugehen*,  stammen  aus  dem  Slavischen.  |
en-do  :  alat.   endo,  indu  jin*",   lat.  nur  mehr   als  Kompositionsglied,  z. indi-gena,  ind-oles,  weitergebildet  in  hom.  rä  Ev-d-lva  (richtig  evöXva)  ,(Üp Eingew
```


### [2026-09-05T17:31:40.023Z] TOOL RESULT

```
en^;  Partiz.  Pass.  do-tö-s]  de-mn  ,T3and^
Ai.  dy-dti  (mit  ä-,  ni-,  sam-)  ^bindet'    (dy-  TieFstufe  von  *dei-,  von  der
•  3^  PI.  dydnti  aus^  vgl.  av.  nl-dyä-tqm  3.  Sg.  Med.  in  pass.  ßed.  ,es  soll Einhalt  getan  werden^,  -ä-  Erweiterung  von  der  Tiefstufe  di-,  Bartholomae Airan.  Wb.  761),  ai.  Partiz.  ditd-  ,gebunden'^  (==  gr.  SeTÖg),  däman-  n. Band'  (==  gr.  -drjfxci),  ni-dätär-  , Binder';
gr.  (hom.  att.)  öeco  (*ösja))  , binde';  SsTÖg  ^gebunden';  öez]^  ^zusammen- gehundeue  Späne  als  Fackel'  (öe-  für  idg.  *d9-  wie  d-srög  :  TLSrjfiL),  dua?^Xo- dsvrjQ  , Garbenbinder',  Siaig  ,das  Binden,  Bindung',  ösoy,6q  ,Band',  x^ij- ds-^vov  , Kopfbinde',  dsixvia  PL  , Bettgestell';  hom.  Präs.  öiörj^i  ,binde'  ist zu  drjau)  nach  TL-d^rji.iL  :  &rjaa)  ,neugebildet';  vuö-örj^a  (vgl.  ai.  däman-) , Sandale',  diddriixa.  , umgeschlungenes  Band,  Turban,  Diadem';
alb.   dual  , Garbe'    (über    *dön-    aus    idg.  *<ie-7i-),    del    ,(*Band),    Sehne,
•  Flechse,  Ader'  (idg.  *dö-lo-).
WP.  I  771  f.,  Schwyzer  Gr.  Gr.  I  340  f.,  676,  688.
dSg-  ,packen'?
Got.  tekan  ,berühren',  mit  Ablaut  anord.  taka,  (engl,  take)  ,uehmen'; toch.  B  tek-j  tak-  ,berühren',  B  teteka  ,sobald'..
WP.  I  786,  WH.  I  351,  Van  Windekens  Lexique  138,  139  (vergleicht auch  lat.  tango)^  Pedersen  Toch.  207  L
I.  dei-,  deiQ'f  di-,  diä-  ,hell  glänzen,  schimmern,  scheinen'  (älter  ,*Strahlen
werfen'?).
Ai.  di-de-ti  ,scheint,  leuchtet',  3.  PL  dldyati,  Impf.  3.  Sg.  ädldet,  Iraper.
2.  Sg.  didlhij  su-dl-ti-h  ,schönen  Glanz  habend',  Kaus.  dlpdyati  ,entzündet,
erhellt',    dipyate  ,flammt,    strahlt,    scheint'   (über    dlvyati   s.  unten),    didi-
■  ,scheinend'  (auf   Grund  von   di-de-ti);  ähnliches  *doi-d-o-  (gebrochene  Re-
•  dupL)  in  anord.  teitr  ,heiter,  froh'  (eigentl.  , strahlend'),  ags.  t^tdn  , lieb- kosen', tat-  (in  Namen)  ,froh',  ahd.  zeiz  ,zart,  anmutig'  (vgl.  heiter  sowohl ,klar'  als  ,froh';  Uhlenbeck  Ai.  Wb.  126);  vielleicht  hierher  auch  lit,  didis ,groß'  als  ,ansehnlich';
184  '
gT.  hom.  diaro  ,videbatur',    öedfirjV    idoyiqta^oVj   idöSaLOv    Res.,    arkac Konj.   dsdvoij    hom.   Aor.    öoaaaaro    ,erschien^,    Konj.    dodaaerai,  gegei über   arkad.  Aor.  d6d[as]T0L  mit  o  nach  edo^s,  Schwyzer  Gr.  Gr.  I  68l3 hom.  dhXog  ,sichtbar^   {*dei€log',    mit  metr.  Dehnung  evSsUXog),  drjXog  dgl (aus  *66icclogj  woraus  auch  Hesychs  öiaXog',  hom.  dQl^r]kog  ,sehr  deutlicl klar''  (aus  ^dirj-Xög)]
*doilo-  vermutlich  in  ags.  sweo-tol  (aus  *täl)  ^offenbar,  deutlich,  klar"^ und  in  mir.  döel  , Käfer'  (^glänzend  schwarzes  Insekt')  sowie  im  ir.  Fluß, namen  Daol  (*doila)  als  ,die  glänzende'.  Hierher  wohl  auch  lit.  dailii^, ,zierlich,  hübsch',  ddüinti  ,glätten,  schmücken'.
Mit  Formans  -tlo-  vermutlich  hierher  das  nur  im  Kompositum  vorJ kommende  germ.  H
```


## [2026-09-05T17:31:48.922Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 195 196; do echo \"=== NR=$n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -50; done",
 "description": "Print Pokorny leaves 195-196"
}
```


## [2026-09-05T17:31:50.284Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'deiuo\\|deiwo\\|daeva\\|dae-va\\|dyeu' POK_01.txt | sed -n '1,40p'",
 "description": "grep deiwos in Pokorny"
}
```


### [2026-09-05T17:31:50.639Z] TOOL RESULT

```
=== NR=195 ===
ipla-:  zldal-,  nhd.  Zeidel-,  nd.  til-  ,Honig'  (,KlarheitJ Glanz  —  klarer  Honig').
Gegen  Pedersens  Heranziehung  von  hett.  te-es-ha-  , träumen'  (Mur§i^ lis  69)  s.  Couvreur  H  53  und  oben  S.  178.
u-Erweiterung:  deieu-  (:  dieu-,  diu-,  diu-)  leuchtender,  göttlich] verehrter  Himmel  und  leuchtender  Tag:
Diphth.  St.  Nom.  dieus  (diieus),  Akk.  die[u]m,  Vok.  dieu,  Lok.  cf/^u^ und  dieu,  Dat.  diuei.  Gen.  diu'6s,  -ös;  dieus-poter  ,Himmelvater'.
ai.  dyduh  (diyäuh)  , Himmel',  Akk.  dyäm,  Lok.  dydvi,  divi,  Dat.  divi^S Gen.  divdh  (und  dyöh),  Instr.  PI.  dyu-bhih;
gr.    Zsvg    (=  dyäü-li)j    Akk.  Zf^v    (=  dyäm),    Vok.   Zbu    {^dviu),    Gen.l Ji{<f)ög,  Dat.  (Lok.)  Ji(J^)l  (Zrjv  zog  Zrjra,  Zr]v6gy  ZrjvL  nach  sich;  über  Zd^g' bei  Pherekydes  von  Syros  s.  Schwyzer  Gr.  Gr.  1577*);    der  Gen.  *diue8 in  thess.    zJieg-y.ovgiddscjj  prien.  Ji£g-Y,ovQidov   (Schwyzer   Gr.  Gr.  I   547);
im  Lat.  hat  sich  das  alte  Paradigma  in  zwei  gespalten,  die  den  Namen des  obersten  Gottes  und  den  ^Tag'  bezeichnen;  ähnlich  im  Osk.  und  Umbr.:
lat.  luppiter  aus  lü-piter,  umbr.  Jupater  Vok.  =  Zev  ndrsQ,  zum  Nom. ai.  dyäuspitä  ,Vater  Himmel',  Zavg  TrazrjQj  Dat.  umbr.  luvepatre,  illyr. (Hes.)  j€L-7idrvQog',  lat.  Gen.  louis  (altlat.  auch  Dlovis,  auch  als  Nom.), osk.  Dill V ei  ,Tovl',  iuvilam,  älter  diuvilam  ,*iovilam',  iuvilas  ,*iovilae' usw.,  vgl.  GentilN  lat.  lülius  {*Iovilios)]  \a.t.  Diespiter  (wovon  flamen  Dia- lis)  mit  nach  dem  Akk.  d{i)iem  geneuertem  Nom.  dies,  der  in  der  Bed. ,Tag'  sonst  herrschend  wurde,  während  zur  Bezeichnung  des  ,Himmels- gottes'  die  Ablautstufe  *diou-  aus  *dieu-  unter  dem  Drucke  des  Vok. *dieu-  durchgeführt  wurde  (bis  auf  Diespiter,  auch  umbr.  Di,  Dei  ,divom, dive',  kontrahiert  aus  die-,  so  daß  Di{m)  =  *diem);  der  alte  Nom.  *diüs aus  *dieus  noch  in  dem  neben  Vediovis,  Vsiovis  stehenden  Ve-di^  ,alt- röm.  Unter weltsgott' ;
-
185
der  Bed.  /Pag^  lat.  dies  s.  oben  (m,;  als  f.  in  der  Bed.  ,Terrain, •  t  Zeit'  vermutlich  nach  nox)^  doch  daneben  der  ältere  Nom.  dieus h  in  nii-dväs  tertius  ,\\\m  ist  der  3.  Tag',  ferner  diu  ,bei  Tage'  (Lok. '^  tl"u  oder  *diöu),  ,den  Tag  lang',  daraus  ,lange'.  Deminutiv  lat.  diecula *    eine  kurze  Frist',  osk.  [d]i{külüs  ,Tage',  zicolo  ra.  ,Tag';
*  ir  (^^6  proklitisch  dla  ,Tag'  (aus  nach  dem  Akk.  *diiem  geneuerten g  »••^,^  cymr.  dydd,  corn.  c^eiÄ,  (^y^Ä,  bret.  deiz^  ;Tag'  (ebenso);  air.  m-c?iw heute'  cymr.  usw.  he-ddyw  ,heute'  (zunächst  aus  *-diiü,  das  wohl  =
=== NR=196 ===
  lat.  diu).
*  You  der  Ablautstufe  diu-  in  der  Bed.  ,Tag';
ai.  divd  ,am  Tage',  divBdive  ,Tag  für  Tag'  {divdm  Nom.  sonst  ,Himmel'),. naktdmdivam  , Nacht  und  Tag',  audivdm  /ein  schöner  Tag',  sudivd-h  ,einen gcbönen  Tag  habend',  arm.  tiv  ,Tag',  gr.  eydlog  ,mitten  am  Tage  (er- geheinend)' (auf  Grund  von  *iv  diJ^ij  vgl.  ^wvxioq)]  lat.  dius,  interdius  ,tags^ untertao's'  (mit  lat.  Synkope  aus  dem  Gen.  *diuös)]  hi-j  tri-duum  (*diiiom Zeitraum  von  zwei,  drei  Tagen';
es-St.  dities'  vorausgesetzt  von  ai.  divasd-h  ,Tag',  formell  zu  dak. <J<ficr€fia  , Königskerze,  Fackelkrau t^,  wohl  aus  *diuesjr)iä  ,Leuchtpflanze^ (Detschev,  Dak.  Pflanzenn.  14 ff.);  aber  gr.  sVötog  (*8i)-SiSog)  , heiter',  älter sidia  ,heiteres  Wetter',  zu  ai.  su-divdm  (oben);  vgl.  Sommer  Nominal- komp.  73  ff.
*diuios  in  ai.  divyd-,  divid-  ,himmlisch',  divyäni  ,die  himmlischen Räume',  gr.  öTog  (aus  *(5f/(og,  Schwyzer  Gr.  Gr.  I  472a)  ,göttlich',  lat. dius  ,göttlich'  (verschieden  von  dlvusl),  dium  ,Himmelsraum^,  suh  dlo] Diana  aus  ^Diviänay  die  zur  Mondgöttin  *Diviä  Gehörige  (?);  vgl.  etr.  Tiv ,luna',  tlves  ,Monate',  nach  Kretschmer  Gl.  13,  Ulf.  aus  ital.  *diviä^  und orph.  FLavöla  ,Selene'  aus  *7rav-diJ^iä  ,Allerleuchterin'.
Ablautstufe  diu-  in  ai.  dyu-mndm  , Himmelsherrlichkeit',  dyu-mdnt-  ,hell, licht',  verbal  dyut-  ,leuchten'  in  dyötate,  i^Lor.  ved.  ddyaut  ,leuchtet^  (mit  t wohl  nach  ^vit-  ,hell  sein');  vgl.  auch  aksl.  d^zdh  , Regen',  russ.  dozd\  acech. deUj  usw.,  aus  *dus-diu-  , schlechtes  Wetter',  Trubetzkoj  Z.  sl.  Ph.  4,  62  ff.
o-St.  deiuo-s  ,Gott,  Himmlischer':
ai.  devd-h.  ,Gott'  {devi  , Göttin'),  av.  daeva-  ,Dämon^;
lat.  deus  und  divus,  beides  aus  dem  Paradigma  *deiuos  (>  deos),  Gen. *deiui  (>  dlvi);  osk.  deivai  ,divae'  (osk.  deivinais  =  lat.  divinis]  umbr. deueia  ,divinam';  osk.  deiuatud  ,iurato'  =  lett.  dievdties  ,schwören';  lat. dives  ,reich',  eigentl.  ,der  unter  dem  Schutz  der  Götter  Stehende',  wie slav.  bogai^,  s.  Schulze  KZ.  45,  190);
gall.  GN  Devona,  PN  Devo-gnäta,  air.  dia,  Gen.  de  ,Gott',  acymr.  duiu-{tit) ,Gott(heit)',   mcymr.  ncymr.  duxo,  acorn.  duy,  bret.  doue  ,Gott';
anord.  tlvar  PL  , Götter'  (*deiuös)  sowie  anord.  Tyr  (agerm.  teiwaz) ,der  Kriegsgott',  ags.  Tlg,  Gen.   Tiwes  ,Mars',  ahd.  Zio,  Zio]
186
apreuß.  deiw{a)s,  lit.  dieuas  ,Goit'  (deive  , Göttin^  Gespenst^  aus  *c?eiw2ci1 dievo  süneliai  ,Himraelssöhne^,  finn.  Lw.  taiwas  , Himmel^);  lett.  d\e\3^ (verbale  Ableitung  liegt  vor  in  lit.  deivötis  , Adieu  sagen',  lett.  dievätiiii s.  oben),  vgl.  Trautmann  50,  Mühlenbach-Endzelin  I  484,  485  f.  Dagegeal sind  aksl.  d^v^  m.  ,Wunder',  divo,  -ese  n.  ds.  (-es-St.  wohl  erst  nach  ^w^^ol -ese  ds.),  divhm  , wunderbar^,  nicht  vom  Begr
```


### [2026-09-05T17:31:50.681Z] TOOL RESULT

```
2080:ai.  blititi-h,  bhüti-h  f.  ,Sein,  Wohlsein,  guter  Zustand,  Gedeihen^  (av. bäti-  m.  ,Name  eines  daeva'7  =  aksl.  za-,  'po-^  pre-byth,  russ.  byth,  Inf. aksl.  bytl,  lit.  öw^i;  mit  ü  gr.  cpvGig).
2681:o-St.  deiuo-s  ,Gott,  Himmlischer':
2682:ai.  devd-h.  ,Gott'  {devi  , Göttin'),  av.  daeva-  ,Dämon^;
2683:lat.  deus  und  divus,  beides  aus  dem  Paradigma  *deiuos  (>  deos),  Gen. *deiui  (>  dlvi);  osk.  deivai  ,divae'  (osk.  deivinais  =  lat.  divinis]  umbr. deueia  ,divinam';  osk.  deiuatud  ,iurato'  =  lett.  dievdties  ,schwören';  lat. dives  ,reich',  eigentl.  ,der  unter  dem  Schutz  der  Götter  Stehende',  wie slav.  bogai^,  s.  Schulze  KZ.  45,  190);
```


## [2026-09-05T17:32:12.199Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf p133 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==155' HRN.txt | head -40",
 "description": "Horn p.133"
}
```


## [2026-09-05T17:32:12.601Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'deiw\\|dyeu' AHD_watkins1985.txt | head -30",
 "description": "grep AHD deiw"
}
```


### [2026-09-05T17:32:13.858Z] TOOL RESULT

```
=== HRN leaf p133 ===
— 138 —
596. dltn i^dem) ') *Geöiclit, Waiigun , dliue,
aw. daeman- ; plilv. andemän\kar 'empfangend,
führend', päz. andlmdnl 'entgegen, vor; arm. LW.
dem, det, y-andman (Hübschmann, No. 88).
kurd. LW. djm\ bei. LW. dem (80); afy. leina
'Pupille.
597. dtn 'Glaube, Religion*.
aw. dafwö-; phlv. diu bezw. den, paz. diu, dlmk,
arm. LW. den.
Allgemein entlehnt*'^).
598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
29, 26.) 3).
aw. daeva- 'Dämon'; phlv. dev; ai. devd- 'Gott'.
599. dlvär 'Mauer, Wand'.
ap. ^deghavära- (vergl. gr. th/o^-, osk. felhuss).
Nöldeke (mündliche Mitteilung), unter der Voraus-
setzung, dass die np. Grundform '^devür lautete, was
die Zusammenstellung mit dev (8ähn. I, 24 Vers 86)
wahrscheinlich macht.
kurd. LW. dwär; wa;^. LW. dival^ sar. delvül 'Mauer,
Wand, Umwallung.
*) Der Majhül vokal ist nicht mehr in der Aussprache erhalten.
') College Jensen hat din sogar im Verdachte, babylonisch zu
sein. Er äussert sich in folgender WeiBe über diese Ansicht:
y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
dattira ibid. = framätaram, beides in der Inschr. von Naqs-i-Rustani.
iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
welches in der babyl. Version der Achämonideninschriften vorkommt.
iHiiii = 'Gesetz, Recht* könnte sehr wohl persisches daina übersetzen,
das im Altpersischen nicht vorhanden. Ich halte es daher für möglich
(falls nichts Entscheidendes dagegen einzuwenden), dass daina durcli
elamitischcs den- mit assyr.-babyl. dlmi zu verknüpfen ist."
Vergl. Geldner's Etymologie von aw. dapiä- unter No. 413.
Jensen nimmt als Grundbedeutung *Recht, Gesetz' an, Geldner da-
gegen *Glaube, Religion*, wie im Neup.
^) Ursprünglich natürlich 'teuflisch , dämonisch*, vergl. Sahn. 1,
)5? Vers 408, 413.
```


### [2026-09-05T17:32:13.896Z] TOOL RESULT

```
111:Consider the case of religion. To form an idea of the religion of a people, archaeologists proceed by inference, examining temples, sanctuaries, idols, votive objects, funerary offerings, and other material remains. But these may not be forthcoming; archaeology is, for example, of little or no utility in under- standing the religion of the ancient Hebrews. Yet of the Indo-European-speaking society we can reconstruct with certainty the word for “god,” *deiw-os, and the two-word name of the chief deity of the pantheon, *dyeu-pa- ter- (Latin Jupiter, Greek Zeus patér, San- skrit Dyaus pitar, and Luvian Tatis Tiwaz). The forms *dyeu- and *deiw-os are both de- rivatives of a root deiw-, meaning “to shine,” and appearing in the word for “day” in nu- merous languages (Latin diés; but English DAY is not related). The notion of deity was therefore linked to the notion of the bright sky.
112:The second element of the name of the chief god, *dyeu-pater-, is the general Indo- European word for FATHER, used not in the sense of father as parent, but with the mean- ing of the adult male who is head of the household, the sense of Latin pater familias. For the Indo-Europeans, the society of the gods was conceived in the image of their own society as patriarchal. The reconstructed words *deiw-os and *dyeu-pater- alone tell us more about the conceptual world of the Indo- Europeans than a roomful of graven images.
136:Conceptions of the sky, heaven, were var- ied in the different dialects. As we have seen, the root deiw- occurs widely as the divinized bright sky. On the other hand, certain lan- guages viewed the heavens as basically cloudy; nebh- is “sky” in Balto-Slavic and Iranian, but “cloud” elsewhere. Another div- inized natural phenomenon is illustrated by the root (s)tene-, “thunder,” and the name of the Germanic god THOR.
178:The notion of government and sovereignty was well represented. The presence of the old word for tribal king, *reg- (reg-'), only in the extreme east (RAJAH) and the extreme west (Latin réx, Celtic -rix) virtually guarantees its presence in the earliest Indo-European society. (Here is an example of the phenom- enon of marginal or peripheral conservation of a form lost in the central innovating area). Roman tradition well attests the sacral char- acter of kingship among the Indo-Europeans. The functions of king and priest were differ- ent aspects of a single function of sover- eignty. It is this which is symbolized by the divine name *dyeu-poter- (deiw-), the chief of the gods.
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1706:goss deiw- JOURNAL deiw- JOURNEY deiw- JOUST yeug- JovE deiw- JOVIAL deiw- JOWL! gep(h)- JOWL2 gwel-3
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
2139:PROVE per! PROVENANCE gWa- PROVENDER ghabh- PROVENIENCE gWa- PROVERB wer-& PROVIDE weid- PROVOKE wekw- PROVOST apo- PROW per! PROXIMATE per! PROXY cira PRUINOSE preus- PRUNE? ret- PRURIENT preus- PRURIGO preus- PRURITUS preus- PRY? ghend- PSALM pdl- PSALTERY pol- PSEPHOLOGY bhes-1 PSEUDEPIGRAPHA gerbh- PSEUDOMONAD _men-4 PSEUDONYM n0-men- PSILOMELANE bhes-!, mel-2 PSYCHE bhes-2 PSYCHEDELIC deiw- PSYCHIC bhes-2 PSYCHO- bhes-2 PSYLLA plou- -PTER pet- PTERIDOLOGY pet- PTEROCERCOID pet- PTERYGOID pet- PTISAN pelis-1 PTOMAINE pet- PTOSIS pet- PTYALIN spyeu- PUBERTY pubés PUBERULENT piibés PUBESCENT pubés PUBIC plibés PUBIS plbés PUBLIC populus PUCE plou- PUCKER beu-! PUDENCY (s)peud- PUDENDUM (s)peud- PUEBLO populus PUERILE pau- PUERPERAL pau- PUFF beu-!
2158:QUOTH gwet-2 QUOTIDIAN deiw-, k¥o- QUOTIENT kWo-
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2392:Tiu deiw- TMESIS tem-
2414:TUBER teue- TUBIFEX dhé-1 TUCK3 (s)teu- TUESDAY deiw- TUFT tap-
2422:TUSK dent- TUSSAH tens- Tussis (s)teu- TUTOR teu- TUTTI teuta- TWAIN dwo- TWEAK twik- TWELFTH dwo- TWELVE dwo- TWENTY dwo- TWIBIL dwo- TWICE dwo- TWIG! dwo- Twic2 euk- TWILIGHT dwo- TWILL dwo- TWIN dwo- TWINE dwo- TWINGE twengh- TwIsT dwo- Twit weid- TWITCH twik- TWIxT dwo- Two dwo- TYKE digh- TYMPANUM (s)teu- TYPE (s)teu- TYPHLOSOLE dheu-! TYPHUS dheu-! Tyr deiw- TYROSINE teue-
```


## [2026-09-05T17:32:34.619Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN NR=150 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==150' HRN.txt | head -20; echo; echo \"=== HRN NR=151 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==151' HRN.txt | head -6",
 "description": "Horn printed p.133 check"
}
```


## [2026-09-05T17:32:35.892Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'دیبا' BQT_v2_pages.txt | head -20; echo \"=== دیو ===\"; grep -n 'دیو ' BQT_v2_pages.txt | head -10; echo \"=== pages tags near ===\"; grep -c 'pdf page' BQT_v2_pages.txt",
 "description": "grep BQT v2 for diba"
}
```


### [2026-09-05T17:32:36.320Z] TOOL RESULT

```
=== HRN NR=150 ===
— 128 —
vergl. oss. d. dumun, t. dimin Vauchcn; wehen,
blasen (115)0.
Entlehnt kurd. dem, bei. dam (69).
57P». dum, dumb^), diimbe'^) 'Schwanz', dumhal).
aw. duma- 'Schwanz'; phlv. dutn^ dumb, dumhak,
arm. LW. dmak (= "^dumak).
kurd. düw, dunk; Sify. lam; oss. d. dumaij, t. diniag
(107); bei. (LW. ?) dunhag, n. di^/nJ, de^wfc (87), daneben
sicher echt d%m (briefl. Mitteilung von Dam es an
Geiger); sar. öihn, dümba, wsl/. diimbd (LW.).
Die arische Grundform muss ^dhumblmia- gelautet
haben (Bartholomae, Studien II, 101).
574. dendün 'Zahn*^), dendäne 'Mauerzinne'.
aw. vTmitö.lidanfa7i'; phlv. dandän (AV., Bund.);
ai. ddnta-,
kurd. didän *Zähne'; oss. t. dänddg 'Zahn* (104);
l)el. dantän, n. dafän^ d'anfän (70); minj. land, si/n.
dendäHj sar. dandän, wa/. dundäk.
Nach Joh. Schmidt' (zuletzt KZ. 32, 329) 'die

=== HRN NR=151 ===
- 129 -
af/. dvalas; oss. d. duades, t. duädäs.
Die neupersische Form (eine Analogiebildung) ist
entlehnt in kurd. duänzdih (hier findet sich noch
ausserdem das n von np. sänzdeh), hol. duäzdeh,
oll. (\)dö%ten *anheften, durchbohren, nähen', Praes.
```


### [2026-09-05T17:32:36.386Z] TOOL RESULT

```
300:                                         ‫‪ -۲‬رجوع بدیباچة همین مجلد شود ‪.‬‬
739:    ‫بود ‪ .‬د»ا«شنامه ‪۸٩‬‏ و مط » در ادیبات فارسی متر ادف روان ر‬           ‫لنی‬ ‫اآ‬‫هشت‬
813:                                                         ‫بال ‪۸٩۸‬‏ در هرات اتفاق افتاد « تاریخ‌ادیبات‬
8859:         ‫‪ ::‬یو همان دیباچه ) وگاه به *ء » وبا«غ» (رك‪ :‬ص ‪ :‬بح دیباچةٌ مزبور) ‪.‬‬‫(رك ص‬
14245:     ‫>‪٤‬‬‫شهیدبلخی‪« .‬تاریخ‌ادیبات ‪ .‬ش‪.‬فق‬
14283:            ‫بدیبا وخوالیگران خواستند ‪.‬‬                                  ‫یکی خانه او را بباراستند‬
15691: ‫ص بح دیباچة مولف)‪ .‬برای اطلاع از دال نمیر ‪ ,‬رك ؛ ص که ‪ -‬کو از دیباچة مولف ‪ ,‬و برای‬
15959:‫سایرنج (‪-)۱‬کنایه ازدیباوعالسفلی‬
16762:      ‫‪ )۰ 91‬ره لفت‌های دببر * دییرستان» دیبا * دیباچه و دبوان همین کمه است ‪ « .‬فاب‪۱‬ص‪۸۸۰+‬‬
21750:‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
21789:‫دییاجی ‪ = ۱‬بروزن تیماجی» دیبایاف‬                            ‫اقطه بالف‬    ‫دال ‪۳‬‬    ‫و‬       ‫کشیده و قاف بواو زسده‬
21791:‫راگوند بعتی هرچه آزدیبا بافته شده باشد ‪#.‬‬                   ‫را گونند‬    ‫خشخاش‬     ‫‪ ۰‬بلغت عودانی شرت‬             ‫کشده‬
21794:‫دیبادین ‪ = ۳‬بفتح اول ودال دیگر بر‬
21805:‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬
21811:   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
21815:   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
21818:                                                                                      ‫دیباح است ج‬
21820:                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
21823:      ‫‪ #‬ویاچه = بکس اول وینجم (درلهجة مر کزی) » از ‪ :‬دیبا( ه‪.‬م‪ +) .‬چە ( توب‬
21830:   ‫«دی بآنر» و روز پاتردهم را «دی بمهر» و روز بیت وسوم را «دی بدین» با « دیبا دين » گوشد‬
=== دیو ===
2622:               ‫بای ابجد ؛ دو کودك ربا کو‬              ‫عرمی معروف است که پری و دیو باشد ‪-‬‬     ‫در‬
2980:      ‫کېلکی ‪ [04۷3‬فربز ندیو بر ئى ‪ [011۷5‬ن›طنز ی‪ 24.۱ [18۷3‬ص‪:٩۳۹۲‬‏ سمنالی ‪15۷5‬ل ‪.‬سنگری‬
3839:‫چار دیو ار صمرذات؟ ‪ -‬وکنابه‬                                                                        ‫‪١‬‏ ‪.‬‬       ‫هم هت‬
10357:‫جدیو * ‪ -‬بکر اول و الیوسکون‬
10365:‫یمعتی خدیو است که‬          ‫و سکون رای فرشت ‪۰‬‬                                              ‫نیز گفته‌اند ‪۲‬‬
10394:   ‫® ‪ -‬خدیو از ‪ .۵ ۷6/۵۳‬از ‪ ( 2۷۳212070-‬ق ‪« ) 121۵۷‬یبرك ‪ ۷۵۲‬درمادء‬
10395:   ‫‪ 2‬رك ‪ :‬خدا ‪« .‬خدیو» خداوند بود ‪ .‬گویندکشور خدیو و گهان خدیو ‪ .‬فردوسی‬                             ‫‪0۱‬‬
10404:                            ‫خدیو ‪.‬‬    ‫‪:‬‬   ‫رك‬    ‫_‬    ‫‪۱‬‬      ‫رزیر آمده «نفن» ورك ‪ :‬دائرةالمعارف احلام ‪.‬‬
14675:     ‫بخورد ودناابونددگمراتند زنگه‌ودیو کودغاتغر ابا‬                          ‫(یوند نبت واتصاف) هرچیزی که ‪0‬‬
21533:   ‫و از آن مخلوفی اهریمنی دیو سرت اراده شد» وغالبا باآژی ‪ 2‬مکجاآمده «شت ص‪4۸۱‬‬
=== pages tags near ===
0
```


## [2026-09-05T17:32:48.016Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BQT_v2* BQT_v1*; echo \"--- formfeeds v2:\"; python3 -c \"\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('len',len(s),'ff',s.count('\\f'))\nprint(repr(s[:600]))\n\"",
 "description": "Inspect BQT v2 file structure"
}
```


## [2026-09-05T17:32:49.341Z] TOOL CALL #16: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nb=d['BQT']\nfor k,v in b.items(): print(k,':',str(v)[:1200])\n\"",
 "description": "BQT ref info full"
}
```


### [2026-09-05T17:32:49.520Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r-- 1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
--- formfeeds v2:
len 2900526 ff 683
'\x0c                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bلض\u200cبال \u202a ۰ ۲۶\u202cرک\u202c\n\u202b\u202a۱\u202c\u202c       \u202bاسا تعدولیدیارتم و\u202c\n                                     \u202b\u202a7\u202c\u202c\n\u202b\u202a ۰\u202cو زل رسوا »وا روون لات سا روصا مواقم\u202c      \u202bوتان\u202c\n\n                      \u202b\u202a۴2 ۱\u202c\u202c\n\n                  \u202bرک یمن\u202c\n                  \u202bم سارو کی و ررك\u202c\n\n\n                 \u202bجلررومدا\u202c\n             \u202bچاپ دوم فروردین \u202a۳۴۳۱\u202c\u202c\n                 \u202bبا تجدید نظر کامل\u202c\n          \u202bبسرمایه کتابفروشی ابن سیتناپران\u202c\n\n\n\n\n                   \u202bچاپ افست رشدبه\u202c\n\x0c                   \u202bم\u202c \u202bو\u202c\n\u202bنآکو سخنیم بیاموز'
```


### [2026-09-05T17:32:51.176Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
kind : archive_djvu+local_scan_ocr
url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
covers_etymology : True
notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated
scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. 
cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-05T17:32:56.590Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nimport sys\n# find leaf containing 'دیباذر'\nfor i,p in enumerate(pages):\n    if 'دیبادین' in p or 'دیباذر' in p:\n        print('leaf',i,'printed approx',i+543)\n\"",
 "description": "Locate diba leaf in BQT v2"
}
```


### [2026-09-05T17:32:58.332Z] TOOL RESULT

```
leaf 367 printed approx 910
leaf 368 printed approx 911
```


## [2026-09-05T17:33:01.866Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i in (365,366,367):\n    print('=== leaf',i,'===')\n    print(pages[i][:2600])\n\"",
 "description": "Print BQT v2 leaves 365-367"
}
```


### [2026-09-05T17:33:03.789Z] TOOL RESULT

```
=== leaf 365 ===
                                                                                           ‫‪6‬‬   ‫= ‪۵‬‬




‫دهگانی س بنتح اول بروزن ارزالی‬                        ‫نکر اول وثالی وسکون‬       ‫‪e ۱‬‏‬   ‫ذهشی‬

‫و‌درقديم رایج‌بوده ‪ -‬ویکس‬
                        ‫نوعی‌از زرباشد آن‬             ‫شبن فرشت ‪ ۰‬بمعنی دادن وهمت وبخشش و عطا‬
                   ‫اول دهقانی وزراعت کردن ‪. ۵‬‬                                     ‫وکرم باشد ‪.‬‬
                                                      ‫ذهشت ‏ بفتح اول وانی وسکون شین‬
                                          ‫باشد ‪.‬‬      ‫وتای‌قرشت» بمعنی‪,‬بکجهتی وبکرنگی وبگانگی‬
‫دهله = بفتح اول بروزن بهله ‪ ۰‬نوعی‬                                                          ‫باشد ‪۶# .‬‬

  ‫صل‬
   ‫تهن‬
     ‫م وپ‬
        ‫ورکه‬
           ‫از خار است که بوتهٌ آن بز‬
‫زمین میباشد واآرا گرن بروزن چمن‌می‌کومند‬
                                                                  ‫‪۰‬‬                            ‫‪۱‬‬    ‫است‬




‫و تشه‬    ‫وه‌طلق بل را نز گفه‌اند خواه از جوب‬          ‫دهقان خلك ح کنامه ازرضوان‌باعد‬
‫فتطره‬   ‫خواه ازسنگه و آ هك ساز ند ‪ +‬ومعری‬      ‫و‬                          ‫که خازن بهشت ات ‪.‬‬
                                     ‫خوانند ‪۶.‬‬
‫‪.‬نابه‬
    ‫دهلیزی ه بر وزن شبخیزی ک‬                          ‫است که زراعت کننده ومز آرع باشد‬   ‫وععنی‌دهقان‬

                                                      ‫و دهقان معرب آنست ‪ -‬ومردم تاربخی و تاریخ‬
‫ثالی و هیم»‬    ‫بفتح اول وسکرن‬   ‫‪-‬‬   ‫دهم‬                                        ‫ویند ‪. ۴‬‬
                                                                                      ‫گز‬‫دان را ن‬

 ‫‪۰:۷۰‬‬         ‫«معئی آفر سن «منای‪‎‬‬   ‫که‬         ‫‪ - ٩۱‬اسم صدز از دادن (ه‪.‬م‪ .).‬بهلوی ‪0‬‬

   ‫وحرنوشت*«تاوادبا ‪»4۵۱‬نز آهده‪ .‬‏ ‪- ۴‬گازا‪:‬نده(ی‪+‬سونداصاف‌ودارند کی )‪.‬پهلوی ‪78۲80‬‬
  ‫«اوادبا ‪ ۶۹۱۲‬زباکی ‪( 08290160‬زارع)« کربرسن ‪. ۷۷2‬کیلکی ‪ ,2801/61‬معرب آن‌دهقان‬
 ‫ومصدر جملی آن دهقنت است ‪ -‬وچون ماکان ابرالی دهگان لامیده منشدما ند در اسلام من باب‬
                                                   ‫اطلاق جزء بکل هامبهرایان را دهقان تامیدند ‪:‬‬
              ‫آبد ادر مبان‬   ‫نژادی یدید‬                    ‫از ابران و از ترك و از تازبان‬
               ‫سخنها بکردار بازی بود ‪.‬‬                      ‫لدههقان نه‌ترك و نتهازی بود‬
  ‫فردوسی طوسی ‪.‬‬
  ‫‪ - ۴‬چون‌لاقل اخبار وسنن وروایات ابرانی‌در آغلز اسلام دهقانانابران بودنده‌بدین هعنی‬
   ‫‪- ۴‬قن‪:‬بستگانی‪-8 .‬پهلوی‪« 0102080‬تاوادیا ‪۶5۹‬‬                         ‫آمده‌است‪.‬ر‪ :‬مزدیسنا ص ‪۶۹۳.‬‏‬
  ‫‪ #‬دهلی‪ -‬بکر‬                ‫‪ #‬دهقان ‪ -‬بک
=== leaf 366 ===
 ‫=‬    ‫‪6 ۵‬‬   ‫‪۱‬‬
                                                                                            ‫ده مر ده گوی‬


‫و بطعم شدرین بتلخی مابل است ‪۰‬‬                   ‫همیمباشد‬     ‫درخت و بوتهٌ غار است و آنرا معریی شجرتالفار‬
‫‪.‬وبند اگر کسی را‬
               ‫و معرب آن دهنج باشد گ‬                          ‫کوبند ‪ .۱‬وآن چوبی است که چون بوزسش‬
‫زهر ددهباشند بخورد دفع هرکدواگرزهی‬                                              ‫بوی خوش از آن آید ‪: ۴‬‬

‫لخورده باشد بخورد هلاك شود ‪ -‬ودهنه و لجام‬                    ‫ذه مرده گوی = یمعنی پر حرف‬
                              ‫اس را ندزگفته‌اند ‪۱‬‬
                                                                                          ‫وسیار گوی باشد ‪.‬‬
‫ده له ‪ -‬بفتح اول و ضمثالث و ظهور‬                             ‫ده هست ‪ ۲‬د بامیمبروزن بکدست‪.‬‬
‫انی ورابع > زیور وآرایش راکوبند وآنرا هر‬                     ‫فامدرختی‌است که بعربی‌غار گوبند‪ .‬چون‌بسوزانند‬
‫هفت تزخوانند ‪ -‬وبمعتی لتصان کردن هم‌هست‪.‬‬                      ‫بوی خوش دهد ودر بہار وزمستان سبز میباشد‪.‬‬
‫وهر دوچیز را نز گوبند که در کیفیت و کمیت‬                     ‫اکر شاخی ازآن دراراخی وباغ دفن کنند آفتی‬
‫تزديك بهم‌باشند‪ .‬وعدد نود هم هت که دعر بی‬
                                                             ‫که از ارضی وسماوی بپم رها آن شاخ رسد‬
                                         ‫تمعن خوالند ‪.‬‬       ‫وآن باغ و اراضی محفوظ باشد » وبعضی گویند‬
‫ده ودار = بکر اول و دال ابجد‬                                 ‫پاردرختی است کهآ ترا زغار ‪ ۴‬می‌گومندت ومعنی‬
 ‫بالف کشیده بروزن سه و چار » بمعنی دگاریور‬                   ‫ترکی آن ده نفراهسمت‪ .‬باد وعربان مسکران‬

                             ‫و کروفرباشد ‪.‬‬                                                         ‫خوانند ‪.‬‬
‫ذهون ‪ -‬بنتح‌ارل بروزن زبون» بمعنی‬                            ‫ده هسکی ادر یس ‪ -‬بکسر اول‬
 ‫حفظ وباد ودر حفظ داشتن وچیزیرا ابزرخواندن‬                      ‫است ‪۰9‬‬     ‫نپبشترسرشت‬
                                                                                    ‫وثانی ک»نابه اعز ب‬

                                                             ‫* = بائون‌بروزن بفداد؛ بمعنی‬      ‫دهناد‬
                                                   ‫ناگ ‪.‬‬

 ‫ده هز ار = بازی‌چهارم استاجملة‬                                                            ‫نظامواسق باشد ‪.‬‬
        ‫ز ااشرتهار دارد ‪۸‬‬‫نرد که نداو هز‬         ‫بازی‬   ‫هفت‬
                                                             ‫=فتح اول و الی و دال‬
                                                                                ‫دهن ذده ب‬
 ‫ده هر ار آن د بمعنی 
=== leaf 367 ===
‫دي‬                                                                                     ‫=‬

‫‪ » ۱‬بروزن افزوده » بمعنی‬      ‫دوه‬
                                ‫ده ب‬             ‫و تحتانی بواو مجپول رسیده و بای فارسی‬
                   ‫عشر باشد که ده بك است ‪.‬‬                          ‫مفتوح مدال ابجد زده ا‬
                                                ‫»مر‌معروف واهی‌منکررا‬




                                     ‫بیان بیست ویکم‬


‫ماه دهم باشد از سال شمسی ‪ ,‬وآن مدت بودن‬
                                                 ‫دی = بقتح اول وسکون انی‪ .‬نام‌ملکی‬
                                                 ‫است که تقددس امور و مصالح دیماه و روز دی‬
‫وتام روزنهم ‪ ۴‬ازهرماه فارسی » ودرین روز ازماه‬
‫بمهر ودیبادین و دیباتر بدوتلق است ‪ -‬د ‏ | وی فارسیان جشن ‪-‬ازند ومد کنند؟ ‪ -‬وبکس‬
  ‫ظ‪ ,‬ممحف « دهوبه »‪ .‬این‌کله درعصر ساسانبان ویز در قرنهای اول اسلام معمول‬         ‫‪۱‬‬
 ‫بود ‪ .‬درالفهرست ابن‌الندیم(چاپ مصري ‪ )۸۳۳‬در موضوع اقل‌دبوان عرب ازفارسی بعربیآمدد‪:‬‬
  ‫صالح‌بن عبدالرحمن مولی‌بنی تمیم که" زیر دست مردایشام بر للفيخ صاحب دیوان حجاج بود‬
  ‫‪ :‬کیفتصنع بدهویه وششوبه؟‬           ‫قیول کرد که آنرا از فارسی بعربی بگرداند ‪ .‬رونام‬
     ‫قال ‪ :‬اکتب عثراً و نصف عشراً » در اینجا ظاهراً ششوبه مصحف « پنجوبه » است »ببااازب‬
  ‫مضیقه در اصطلاح عربی » تاگزیر شده صف عثر را بجای « شثوبه » بشنهاد کند ‪ .‬مب لمات ‪.‬‬
  ‫‪ - ۴‬دراوستا _تاکناا‪ 21‬با ‪ 2۷01021-‬بمعنیآ فربنندہ‪.‬‬    ‫‪ ۴‬هشتم صحیح‌است‪.‬‬
  ‫دادار و آفریدکار است و غالبا صفت اهورمزداست و آن ازمصدر ‪ 21‬بمعنی‌دادن وآفربدن است‪.‬‬
  ‫دی) برای تعین دهه‌ین ماه استممال شده ‪ .‬درمیان سی روز مامه‬      ‫در خود اوستا صفت دئوش [‪-‬‬

  ‫روزهای هشتم و پاتزدهم وبیست وسوم به دی( د=ئوش) موسوم است بنا بر تسمیه بنام ختا‪ .‬برای‬
  ‫بقیه درصفحةٌ ‪۸۰٩‬‏‬
                                                                          ‫‪4۰٩‬‏‬    ‫حة‬
                                                                                   ‫صبهفاز‬
                                                                                        ‫بق‬
       ‫رك ‪ :‬خاله گیر ء ده هزاران ‪.‬‬     ‫‪۸‬‬         ‫‪۲٩‬‏ ‪.‬‬   ‫‪:۸۹‬‬   ‫معرب آن دهنج‪ « .‬دزی ح ‪ ۱‬ص‬
        ‫عبارآن‌هفت دهم (طلامانقره) بوده‪.‬‬   ‫نی‬            ‫‏‪ ٩‬رك‪ :‬ده هزار خانه گیر‪.‬‬
  ‫‪ 0‬و بکشید ‪ « :‬و حن ( سلیمان ) گفت ‪ :‬دهید و حشمتی بزرکه افکتید بکشتن‬
      ‫بیار که کنید ‪ .‬تا یس از این دتدانها کند شود از ری» «تاریخ بیهقی ص‪ ۳4‬متن وحاشیه» ‪.‬‬
     ‫=ه بسعنی ناحیه وکشور ) [ رك ‪:‬ده ]‪= +‬‬
                                        ‫(ي‬
                                         ‫از ‪ :‬دهیو د‬             ‫=یت‬
```


## [2026-09-05T17:33:13.651Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nprint(pages[368])\n\"",
 "description": "Print BQT v2 leaf 368"
}
```


### [2026-09-05T17:33:16.311Z] TOOL RESULT

```
   ‫سره‬                                                                                                         ‫دبافودا‬

‫دابا * = بروزن زببا ‪,‬قماشی باشد از‬                                               ‫اول رو ز گذشته را گوند ‪. ۱‬‬

‫ونابه از دیدارخوبان همهت ‪.‬‬
                         ‫حربرالوان ‪ -‬ک‬                      ‫دیاقود‪ - ۴ )۵‬بنتح اول و انیبالف‬
‫دییاجی ‪ = ۱‬بروزن تیماجی» دیبایاف‬                            ‫اقطه بالف‬    ‫دال ‪۳‬‬    ‫و‬       ‫کشیده و قاف بواو زسده‬

‫راگوند بعتی هرچه آزدیبا بافته شده باشد ‪#.‬‬                   ‫را گونند‬    ‫خشخاش‬     ‫‪ ۰‬بلغت عودانی شرت‬             ‫کشده‬

                                                             ‫که ازیوست خشخاش بخته باشند نهازشم آن‪:‬‬
‫دیبادین ‪ = ۳‬بفتح اول ودال دیگر بر‬
‫وزن شرم کین » نام فرشته است ‪ -‬و مکی از‬                      ‫دیا وش س با نون بر وزن قبایوش »‬
‫نامهای‌الهی هم هت ‪ -‬ونام روز بیست وسیم(‪)۱‬‬
‫از دیماه مغان‬    ‫روز‬       ‫در ین‬   ‫‪۰‬‬   ‫باشد ازهر ماه شمسی‬    ‫خشکی ودربا دزدی وراهزنی میکردند ‪ ۰‬وبصنی‬
‫روز‬     ‫بتن‬
          ‫دكراس‬
              ‫جشن سازند و عید کنند و لي‬                         ‫کگوبند دام شخصی است که عذرا را بفروخت ‪.‬‬
‫دعا کردن بجهت دفم شر شیاطین واز حق تمالی‬                     ‫دیب = پکسراول بروزن‪ :‬سیب » بندری‬
                                       ‫فرزند درخواستن ‪.‬‬
                       ‫‪۱‬‬                    ‫‪۰‬‬                      ‫باشد ازبنادر هند ‪ -‬ودر ترکی‌بیخ وین ه‬
                                                                ‫چریز‬
‫دیباذر ‪ = ۲‬بفتح اول دوال قطه دار‬                                                                     ‫رگاونند ‪. ۴‬‬

                                                                          ‫(‪ )۱‬چك‪ :‬ببست وسوم ‪.‬‬
  ‫]‪id‬‏ ‪evécs‬‬      ‫ع‬         ‫‪ ,‬کردی‬       ‫‪kîd‬‏‬   ‫یهلوی‬   ‫( دیروز ‪۹5‬‬     ‫هندی ‏ باستان ‪séyh‬‏‬             ‫‪۱‬‬
  ‫د(یروز عصر ) ‪ ۰‬استی ‪ 2002 , 8012 , 6022‬و ‪ ( 00012‬دیروز ) " بلوچی ‪۵2 , 612‬‬
       ‫‪4:۲۰ ۶۸‬‬   ‫‪ .‬ورك‪ :‬دزی حاص‬             ‫‪۱۸۱‬‬    ‫(فر) «لك‪۲‬ص‬    ‫‪60062‬‬       ‫‪Ff‬‏ —‬              ‫‪.‬‬    ‫داسشق ‪۰۹۵۰‬‬
   ‫‪ - ۴‬سانسکریت ‪« 301۷‬فهرست ماللهند بیرونی ص ‪« :»۲4۳‬الدیبات » وحی‌الجزاثره‬
  ‫‪ - ۴‬درترکی ‪ :‬شایستگی‪ ,‬خوشبختی؛ ته " پ »ا پابه «جفتابی‬                               ‫م«اللهند ص ‪ ۰۸‬ی ‪٩‬‏ > ‪.‬‬
      ‫* ‪ -‬بهلوی ‪ « 081‬تاوادیا ‪ ۰ ۰۹۱‬از هندی باستان ‪802۷010 . 01 -‬‬                                          ‫‪.‬‬         ‫‪۳‬‬
   ‫‪ .‬رجه اشتقاق آن قطعی ليست‬                        ‫( زبانه کشیدن » پرتو افکندن » درخشیدن) ‪٠‬‏ ارمنی ع‬
   ‫د اسشق ‪۱٩٥۰‬‏ در فارسی = دبباه د‪۳‬یبه؛ و دیباچه و دیوان نیز ازهمین ریشه است معرب آن‬
  ‫‪ 06.‬است «اسفا ‪ ۲: ۱‬ص ‪ > ۵۷۱ ۰ ۱۷۱‬وآلرا از ربشة‬                            ‫‪06‬‬
                                                                             ‫‪.‬زو اول آن‬
                                                                                      ‫دیباح است ج‬
      ‫‪ ۷001۱ ,‬اکدی گرفته‌اند < فاب ‪۱‬ص ‪> ۲۱۱‬رك‪:‬‬                     ‫تالا سومری (لوحه ‪ .‬خط ) و ا‪00‬‬
                  ‫دستان» دییر ‪ * ۰۰ ۰‬از ‪ :‬دیباج ( معرب دبا = ديپاکه ) ی (سبت)‪.‬‬
                                                                                      ‫‪.‬‬    ‫رك ‪ :‬دی‬   ‫‪ ۷‬س‬

      ‫‪ #‬ویاچه = بکس اول وینجم (درلهجة مر کزی) » از ‪ :‬دیبا( ه‪.‬م‪ +) .‬چە ( توب‬
  ‫آبنباجة « دزی ج ‪ ۱‬ص ‪۱۲٤:۲‬‏ »‪ .‬آنجه کهدرآغاز کتاب‬
                                                 ‫تصغیر ) « اسشق ‪» ۱۰‬؛ معرب د‬
                                                                         ‫برای تفهیم موضوع کتاب نویسند ‪.‬‬
                                                                                               ‫یه از صفحهٌ ‪۷۰٩‬‏‬

  ‫اینکه سه روز موسوم به«دی» باهم اشتباء نشوندنام‌هريك رابنام روز بعد بپیوندند مثلاروز هشتم‌را‬
   ‫«دی بآنر» و روز پاتردهم را «دی بمهر» و روز بیت وسوم را «دی بدین» با « دیبا دين » گوشد‬
   ‫وکاهی نیز دئوش ( دی) را درفارسی «دین» کفته‌اند و دین‌بآنر ودیبا دين ازشروست ولی‌ترجمة‬
   ‫صحیح دئوش«دی» است ‪ .‬ابورحان بیرونی درفهرست روزهای ابرانی هشتمن روز را « دی‌بآذر »‬
   ‫مشتهااص‪ « »4 ۲‬خرده اوستا‬                ‫ورده‪ ۶ .‬روزشماری ‪۵۲-۹۲‬‬       ‫و درسفدی «ادست؟ و درخوارزمی«دنو»‬
                                                                                ‫ص ‪ « ۳۱۲‬فاب ‪۱‬ص ‪۷۲‬؟‪.‬‬
```


## [2026-09-05T17:33:36.488Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ns=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i in (377,378):\n    print('======= leaf',i,'=======')\n    print(pages[i])\n\"",
 "description": "Print BQT v2 leaves 377-378"
}
```


### [2026-09-05T17:33:38.191Z] TOOL RESULT

```
======= leaf 377 =======
                                                                                                            ‫‪۱۷‬‬


 ‫دی ره ‪ -‬بضم باوزای‌فارسی وسکون‬                                  ‫است چه باز بسیار بزرکه راباونشبت دهند وباز‬
‫که نام روز بانزدهم‬
                 ‫ها مخفف دين پژوه است ‪۴‬‬                          ‫دبتار گویند ‪ .‬و بعضی کویند دبذار نوعی از باز‬
                      ‫باشد ازهرماه ملکی ‪.‬‬
                                                                  ‫است وآن بیاراصیل کومیاب‌میباشد وبرخلاف‬
 ‫دینسافوس ‏‪ - ٩‬بکس اول و اك‬                                      ‫بازهای دیگر بردورمردمك چشم اوتحربرسیاهی‬
 ‫وسین بی‌نقطه (‪ )۳‬بالف کے ده وفای بواو رستده‬                     ‫هت درغایت تراکت ‪ -‬ونخم کشوث را بسریانی‬
‫وسین بینقطة (‪)e‬‏ زده ‪ ۰‬بلغت بونانی نوعی از‬                                                                ‫دثار گوبند ‪.‬‬
 ‫خار باشد وبر گے آن بککر‌کاهو میماند و نآرا‬
 ‫وون ازهم بشکافند‬
                ‫شبرازی طوسك خوانند ‪ .‬چ‬
                                                                 ‫دینار اشمر (‪-‬ر دینار شمر سراف‬
                                                                                                                ‫کوت‬
                                                                                                                  ‫وا‬
‫کرمهای کوچك از مان ساق وبرکه‌آن برآ ند‬
 ‫وآنرابتازی خس‌الکلب کوبند ومشطالراعی همان‬                       ‫دبنارو له = با رای بی‌نقطه (‪ )۱‬بواو‬
‫است ‪ .‬اکر کل وشکوفة آنرا بکوبند و برشیر‬                          ‫کشیده و فتح بای حطی (‪ ۰ )۲‬بسریانی گیاهی‬
 ‫خواهند‬        ‫که‬‫عبر‬‫ضدو‬
                      ‫وبیند‬
                          ‫مال‬
                            ‫گوسفند بمالند درح‬                    ‫است دوابی ‪ ۴‬وب رکه آن بکرفی ماند و آنرا‬
                   ‫بتر نف ضماد کنند بحس گرداند ‪:‬‬
                                                                                        ‫بشبرازی آهو دوستك خوانند‪.‬‬
 ‫دیو ‪ = ۲‬بااول بثالی مجهول رسیده‬                                 ‫دبنادی ‪ -‬بر وزن بماری » جشی از‬
‫وبواو زده ‪ ۰‬معروف است وآن نوعی از شباطین‬
                                                                      ‫جامةٌ اپرشمی ‪ -‬ونوعی از شراب لعلی باشد‪.‬‬
 ‫باشد ‪ -‬و کمراه و کج اندیش و کج طبع را نیز‬
 ‫کوبند ‪ -‬کونابه ازمردم پهلوان ودلیر وشجاع‬                        ‫دین پژوه ‪ * ۲‬بکر بای فارسی‬
 ‫باشد ‪ -‬وفوعی ازجامةٌ پشمینه است بمیاردرشت‬                       ‫وزای‌فارسی بواوکشیده وبها زده‪ ,‬نام روزپاتردهم‬
‫بوه از‬  ‫ا‪-‬‬‫ن‪۷‬‬  ‫کشند‬
                 ‫ز های جنگه پو‬    ‫رهودر‬‫ک‬                         ‫است ازهرماه ملکی ؛ وحم بای‌فارسی همآمده‬
 ‫اسب هم‌هست که بعربی‌فرس خوانندھ ک‪-‬نوایه‬

               ‫‪.‬‬   ‫بی‌لقطه‬   ‫‪- :‬‬   ‫چك‬       ‫(‪)۳‬‬          ‫‪ :‬وفتح با‪.‬‬    ‫چك‬   ‫(‪)۲‬‬            ‫)‪ (۱‬چك‪ :‬با را‪.‬‬

                                        ‫شمرندء ) ‪.‬‬       ‫شمر ( ائمرنده ‏‬          ‫از‪ :‬دینار ‪ +‬اشمر‬         ‫‪۱‬‬

                                   ‫ص ‪. ۰ ۱۶۱‬‬         ‫‪ < .۳۵۷ Asclepium Dios.‬كل‬                        ‫‏‪— ۴‬‬
      ‫دضافوی‬       ‫مصحف‬      ‫‏‪e‬‬         ‫دنن يروه‬   ‫رك‪:‬‬   ‫ت‬   ‫‪۴‬‬   ‫از ‪ :‬دین ‪ +۳‬روه (یژوهنده) ‪۰‬‬               ‫‪۴‬‬
   ‫‪ - ۱‬پهلوی ‪« ۷64‬منای ‪ ۲*۰ :۱۷۲۷‬اوسا ‪8۷63‬‬               ‫= ‪] 51102501‬لك ‪ ۷‬ص ‪. ۰۸۱۰‬‬
  ‫(دبو)‪.‬هندی باستان ‪( 8۷80‬خدا) «اسشق ‪ .۸۹4۰‬این‌کلمه درقد‪:‬م بگروهی از پرورد کاران‌آربایی‬
  ‫اطلاق میشده ولی پس از ظهور زرتشت و معرفی *اهسوره‌زدا» برورد گاران عهد قدیم با دیوان »‬
    ‫کمراه کنند گان و شباطین خوانده شدند ولی کلم «دبو» نزد همه افوام هند و ارویایی‪ -‬باستثتای‬
   ‫ابرانیان‪ -‬معنی اصلی‌خودرا محفوظ داشته است ‪ 2۷61 :‬ترد هندوان عنوز‪ :‬هم بمعنی خداست ‪.‬‬
      ‫نام پرورد کاربزرک بونالي ٍ ‪ 81100‬پرورد کارلانینی ونای‪ ]12‬درفرانوء‪ .‬از همن‌رشه‬                                ‫‪5‬‬
                                        ‫‪.‬‬    ‫‪ ۱‬ص ‪ ۹۲‬ورك‪ :‬دائرةالمعارف اسلام وفهرست مزدسنا‬                      ‫است ‪ ۶‬وش‬

  ‫‪:‬‬      ‫صیوف‬
            ‫متوبجا‬
                 ‫_ه‌به ( اسب چابك قوی)‪ .‬سف‬
                                         ‫م‪۸‬شب‬                                       ‫‪.‬‬   ‫‪ :‬دنو حامه‬   ‫رك‬    ‫‪۷‬‬


          ‫نشستم از مر دنو حېنده همجوشهاب ن‬                               ‫اعت‬   ‫«دان فیا جو رضا دادم اندرآن‬


   ‫‪ °‬ممزی یشابرری ده * ‪.‬‬

======= leaf 378 =======
      ‫اه‬                                                                      ‫دبوار خانه روزن شدن‬

‫آرا‬
  ‫وسکون دوسین و فوقانی ‪ ۰‬دوابی است که ن‬                            ‫از قپر وغضب هم نوشته‌اند ‪.# ۷‬‬
‫انده قوقو گونند وبرکلف وبهق مالند تبافاعشد »‬         ‫ررنو‌شدن‪ ».‬کناه‬               ‫نه‬
                                                                                    ‫خواار‬
                                                                                        ‫ذی‬
‫واگرطفلی دبر بحر کت بد چون برومالند زود‬                                  ‫از خراب دن خانه باشد ‪.‬‬
                                                     ‫ديو ار گر = دبوارساز ‏ وگل‌کار وینارا‬
‫دیوال ‪ ۴‬سبا لام" بروزن ومعنی دیوار‬                                                            ‫گونشد ‪.‬‏‬
‫است» چه درفارسی راولام بهم تبدیل مییایند ‪#.‬‬
‫‪۰‬‬    ‫فرشت‬     ‫رای‬   ‫بفتح‬   ‫دیواله رو‬
‫شخصی‌را کوبند کهمدابنوندانهاسلوك کند وبراه‬                                ‫عاجز وزبون هدن باشد ‪.‬‬
                                            ‫رود ‪.‬‬    ‫همز هو بای‌فارسی‬   ‫د یو اسست ‪ ۴‬یک‬


    ‫‪ - ۱‬نظر بتصور مهيب و هولناك بودن دبوان‪ « .‬هرچیز را که از افراد خودفوی جثه‌تر‬
     ‫و بزرکترباشد بدیو اضافت نمابند (با بفول که آنهم دو موهوم است) مثلاکمان بز رکه راکمان‬
     ‫دیو خوانندیسنی دبورامیدابد‪ .‬نوعی ازاسیست‌را که ‪-‬اق وبرگهآن ازامتال بزرکنراست دیوامیت‬
    ‫گوبند ‪ .‬کلوخ کلانرا دیو کلوخ » عنکبوت برزکه را دیوپا» زبراکه بابپای بزرکه و بلند‬
     ‫دارده و گردناد را که بلند شود ديو باد گوشد»‪ 9‬انجمن آرا» ولىز ‪ :‬دیوحان › دیوچه‪ ,‬دیوخاره‬
                       ‫دبودار » دیودل» دیوزای» دیوسار » دیوگ » دیو گندم‪ .‬ورك‪ :‬فاب ‪ ۱‬ص ‪٩۹۱.‬‏‬
    ‫‪ 2‬وجنگه کرد‬      ‫دبوار («‪.‬م‪).‬‬   ‫‪-‬‬   ‫‪۴‬‬           ‫امست («‪.‬م‪).‬‬    ‫از ‪ :‬دنو (ھ‪.‬م‪4 (.‬‬          ‫‪۳‬‬

    ‫بسیار بدرارك » و کشتن کرد فراوانی بدر شارستان » در گرکوی عاقبت بستد » و ارك را و قلمة‬
                             ‫زورین راء بعد ازان دبوالآ قرا ببرید ‪« »...‬تاریخ سیستان ‪4۸۳٩‬‏ ‪.‬‬
     ‫‪#‬د یوار بکراول د=بوال د=ی=فال(عامیانه)‪ ,‬بېلوی ‪« 4۷8‬تاوادبا‪ *۹۱‬وجهاشتقاق‬
      ‫کنومله است‪ .‬رك‪ :‬اسشق‌ءهوبشمان ‪ ۹۹‬؛کردی‌ع «‪rãvîd‬‏ وخیع‪ .13۷114‬سربکلی‪1۷164‬‬           ‫آ‬
     ‫اسشق ‪ , ۹۹۵۰‬افقانیع ‪ 14۷1‬هوبمان ‪ 4۹۵‬جداری که دراطراف خانه‌بنا کنند بجهت‌مصور‬
             ‫کردن و حفاظت آن » هرچیزی که ای را محصور کند خواه ازمصالح بنابی با حزآن‪.‬‬
    ‫د‪#‬یوان بکر اول » ازکامة مفروض ایرانی ‪ 0261‬همریثة «دبیر ‪٩‬‏ ( نوسنده )‬
    ‫وبقول اندرآی مرتبط بکامة آسوری ‪« ۳21‬دائردالمعارف املام» وکلمة أن پارسی باستان که از‬
     ‫کدی و نال سومری ( لوحه‪ ,‬خط ) مأخون است « مجلة ابراشهر سال ‪ ۱‬شمارء ‪۸‬‬       ‫‪۷‬‬
     ‫ص ‪«٩ ۷۹۱ - ۵۹۱‬ف‏اب‪ ۱‬ص‪ . ۲۱۱‬معرب آن هم «دبوان» «دزی ح ‪۱‬ص ‪۹۷4 -۸۷4‬؛ دفاتر‬
     ‫عمومی محاسبات ‪ -‬موضع حساب‪ -‬مرکز ندوبن کتاب ها کتابی که نام لکربان واهل عطیه در‬
    ‫آن مکتوب باشد ‪ -‬ادار دولتی ‪ -‬وزارت خانه ‪ -‬سفن شامل اشمار گوبندگان ‪.‬رك ‪ :‬دائرة‬
                                                                                      ‫الممارف اسلام ‪.‬‬
     ‫‪ -‬کر اول وینجم( در لهس مر کزی) م از ‪ :‬ديو ‪٣‬‏ ان (جمع) ‪(۳-۰‬نسبت)‬               ‫‪ #‬ویوانه‬
     ‫[رك ‪ :‬اسشق ‪ ۸۹۵‬ویشتم! ‪٩۲ :۱‬‏ | ؛گیلکی ‪ 20۵۷1‬فنریدزی‪ .20۷64‬برنی ‪. 800۷14‬‬
     ‫‪ . 6488۷10‬سرخه‌بی‬         ‫نطری ‪ < 8012۷1‬ك ‪ .‬اص ‪۳٩۲‬‏ ‪ .‬سمنانی ‪ . 803۷10‬سنگری‬
     ‫» مجنون « وشبانگاه آوردند بش وی (عیسی)‬         ‫بی عفل* بخیرد‬       ‫‪۶۹۱‬‬   ‫ص‬       ‫رد( ‪۰‬‬       ‫‪6‬‬
     ‫احمق‪.‬‬   ‫دیوانگان ب‌بار» و دیورا ازامشان بدر کرد بخن خود وشفا داد ‪« »...‬انجیل فارسی ‪۸۸4‬‬
                                                                                  ‫ابله‪ .‬ادان» بي علم ‪۲‬‬
       ‫هباری فاطع‪)۰۳۱‬‬
                    ‫(‬
```


## [2026-09-05T17:34:00.132Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SNS grep dyp/deb/dib ==\"; grep -n -i 'dēbāg\\|debag\\|dyp\\|dībā\\|diba' SNS.txt SNS_pages.txt | head -20; echo \"== PHD dew ==\"; grep -n -i \"^dēw\\|dēw \\|dēb\\|dēpak\\|dyw'\\|dyp'k\" PHD_mackenzie.txt PHD.txt | head -30",
 "description": "grep SNS and PHD"
}
```


### [2026-09-05T17:34:00.206Z] TOOL RESULT

```
== SNS grep dyp/deb/dib ==
SNS.txt:8040:UKotval.p'dypr'hzsl* LGNPE. 36)? paitifrasa- :L- 
SNS_pages.txt:5188:                                                                                          UKotval.p'dypr'hzsl* LGNPE. 36)?
== PHD dew ==
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:1099:brocade dēbāg.
PHD.txt:4565:dēwī dew: |! dēwēsnīhī déwézagiht šahbalüt šāy- šāhdānag šāyendagīh
PHD.txt:4779:spāh ALY Q335 dēbahr, spihr, Nay LAKE spaxr spahbed VP OR 0335 spas ts” суз? spāsdār Nee es. spāsdārīh uA a soda) spāsešnās TO Put 0335 debàg VW ett spāsūmand ? v€ Pus” q335 spāš AV суз?
PHD.txt:5527:dēwānag
PHD_mackenzie.txt:1982:dewanag [dyw'nk I N --a] demonic, mad.
PHD_mackenzie.txt:1984:dewar [dyw'll M dyw'r, N -] wall.
PHD_mackenzie.txt:1985:dewl-esnih [SDYAysnyh I (M dyw'snyh)] idolatry, devil-worship.
```


## [2026-09-05T17:34:02.049Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT daeva ==\"; grep -n 'daēva\\|daeva-' BRT.txt | head -20; echo \"== NYB dew ==\"; grep -n -i 'dēw\\|dyw' NYB_vol2_glossary.txt | head -20",
 "description": "grep BRT and NYB"
}
```


### [2026-09-05T17:34:02.105Z] TOOL RESULT

```
== BRT daeva ==
12448:'daeva- n
12459:•  j-,  g,  'daeva-  m.,  j.  'daevi-''  f.  I)  im gAw.*'  Bezeichnung  f��r  die  Gottheiten der  vor  Zard^ustra  in  Iran  geltenden Religion:  cüma  .  .  Auxs'd^rä  (sd.)  °vä änkarS  .  .  aiibyS  kam  y.lis  gam  karapa usixt^ä  (sd.)  aehmtli  dstä  Y.  44-  *o;  — af  yaf  'vä  (VP.)  vtspitshö  akat  (sd.)  ma- nanha  sta  H^rsm  Y.^2. 3;  i;  —  aya (naml.  mainiva)  nSit  »ris  vSsyilta  °väcinä hyal  Jf  a-d^baoma  (sd.)  , .  upa.jasal  Y.  30. 6;  —  hya^  vi  .  -y^ns  °vSng  akaslä  main- yus  . .  syao%aiiim  ..fracinas  . .  x/ay^(sd.) Y.  J2.  5;  —  sas^ärS  (sd.)  .  .yä  zl  väv>rs- z5i  . .  °väUiä  masylisca  Y.  2p.  4;  —  hyat '"qsasutä  (sd.)  yii  daibitanä  (sd.)  fraoxti, 'iäilla  masySiicä  Y.  4^1;  —  par}  *v3 . . vacxsma  "väisca  xra/strais{sA.)  masyäiscä Y-^4.  5;  verwendet  Y.  75.  a;  —  yastä °ving  apars  masyqscä  tarS.mqsta  Y.  4^. II.  a)  GP.  mit  dam-  m.  sva.  drüjs dam-:  tsi  'VMg  (GP.)  dqn  \3  dngvais dama  (sd.)  Y.  4r).  4,  11)  'im  jAwr.* 'Dämon,  Unhold,  Teufel':  t&m  z^margüti
12466:'daeva-  11
12473:*)  Im  gAw.  gehört  der  BegritT  daeva-  in  die gleiche  Gnippe  wie  usif-,  'imiay- mhA  karafian- ; sd.  Die  Priester  und  Anhöiiger  des  alten  Glau- ben«, der  den  Goltesbegriff  mit  dania-  beieicii- nete,  setzten  begreiflicher  Weise  der  Einfühning
12476:Bedeutung  von  daeva-  vi
12480:•  j.  'daeva-  Adj.  (fem.  'dapvj-)  'den Dapva  zugehörig,  von  ihnen  herrührend (usw.),  rfa?iisch':  kB  asti  'vö  ks  da^aySzB "wer  gehört  zu  den  Z>.,  wer  ist  ein  Z>.- Anbeter?"  V.Ä31;  32';  —  kva  asti  'vB kva  datvaydzB  Y.y.sz'y  54'.  yt77.6;  — yat  nürsm  vyämbura  (sd.)  'va  maSyäka da^vayäsB  vohuntm  vä  täc^änti  YL  7^.  54; — -  ga%Bittsca  'vJsüa  *handramana  (sd.) N.  5j;  Yt.  77, 6.  et)  sonst  von  drug-: aiXm  dahaktm  ..  'vTm  *dru/im  V.5. 8;  — Hat  ki  ha,  paiti.davata  ya.  'vi  druxl  V. 18.  $1;  —  nase  °vJ  druxs  SrB.j;  — sraosim  ..yd  janta  °vaya  drujB  Y.57. 15.
12483:•  j.  daeva-yasna-  Adj.  'der  die  Dalva verehrt,  anbetet';  überhaupt  'ungläubig"*: ye^he  .  .  näirika  avayi  xfudrä  Aqm.- rafktoayeiti  mazdayasnanqm  'nanqmca N.  77'';  ~  kalärö  paurvB  ämayante  (sd.) maidayasna/ibyB  va  'nalibyB  vä  V.  7.  36; 37;  —  drvafäB  'naahdYt.  5.  94;  —  huma- yak»m  'n>m  drvanttmca  ..Y\..^.\\y,  109, 5.37;  —  drvatam  'nanqm  Y.ig.  26,41, Yt5.68,  ;;.  4,6;'  —  dusmainys .'. 'n^iAP.) A.  7,  11;  —  daffnqm  'nanam  Y,  72. 1 1 ;  —
12506:•  j.  daeva-yaz-  Adj.  'der  zu  den  Da!va betet,  Z>tfA'iianbetei':  nyancs  'yä^  (NF.) V.J5.4Ö,  Ylj/.  6;  —  mafyaka  'yasS  Yt 14.SM —  Aäu  asti  daivff  Aäu 'yOtS  iHS.)'i V.-.54;  53.  <?-3i.  Sa-
13285:—  maisrake  sp3ntahi  .  .  'tahe  vidaivahe Y.  /.  13,  Yt.  11.  17,  b)  mit  zardiustray- Adj.  'das  von  Z.  gegebene  Gesetz':  dättm vTdSyüm  .  .  't?m  zara^usiri  Y.  2.  13;  — dälahe  vJdaivahe  .  .  'tahe  zara'kuitrsis  Y. i.  13;  —  kat  'tahe  zard^uärSiS  ^/i.  2;  Yt. //.  3.  c)  mit  vJdaeva-  und  sara'^ustray-: aufm  "hm  yim  vTdöyüm  zara'iustri  upatri anyäi^  sravSil .  .  yd^a  zrayö  vouruAasfM sipairi  anyä  apö  V.5.  23;  22,  24,  25;  — nisbayemi  vafiuhJm  dalHqm  mazdayasnim 'tim  vldöyam  *eara>ustri  V.  ig.  r6;  — 'l,U  Aala.dätäi  vTdaH-äi  "zara'iuüräi  Extr. ';  2,  _yj  —  'ta  (VS.)  haha.däta  vldaiva sara^u/iri  Extr.  4.  c)  I  im  Ap,:  'tarn tyJ*  mana  aitJ*  *aditriy  D.6.3;  —  imä dahyäva*  *tya  manä  'ta  (AP.)  ^apariyäy^ (sd.)  Bh.7.8.  ni)  'Regel,  Norm'  (nur Ableit).
14853:i)  'fliegen,  sich  im  Flug  stürzen  auf-'  v.j.  11.  2)  in  -/arischer  Art 'einher- {Jaiü  mit  Lok.):  kazanrim  iiunqm  .  .  gehen'<>:  yat  nä  \Jahika\  pasca  panca- mainyavasä  patinti  katiurile  patH  daeva-  1  jasTm  sarn^m  frapalaitii''  anaiwyästa (ad.) t1qmYt.10.119.  2) 'fallen,  hinabstUrzenlj,^  anabdäts  vä  "wenn  ein  Mann  [ein (s.  auch  4):  pairikä  .  .  yü  starö  hnma  Weib]  nach  (vollendetem)  fünfzehnten  Jahr (sd.)  patmOi  aniar»  tarn  asmammca   Yt  !  ^\^Yia  geht  ohne  .  ."  V.  18.  54.  3)  in
23629:KompA. ;  Ableit.  —  Vgl.  auch  via-käna~  und *hattmizsariar.  —  ai.  vika-  di.()  ;  inp.  (Pü.)  vurk, np.  gurg,  sbaL  gvark.  —  >)  Streng  lautgeseti- liel»  wäre  virikjmta;  %  sSg.  4  No.,  2^4  No. —  >)  Das  ist  jedenfalls  der  Sinn  der  Stelle, aber  der  Wortlaut  stimmt  nicht  dazu;  s.Hbm. ZDMG.  28.  84.-3)  Umgekelut  af?.  levf •Wolf  -  jAw.  daeva-.  —  4)  Aber  fem,  vflA-.
24022:•  j.  vl-daeva-,  -dSiva-  (fem.  °va-)  'gegen die  Daiva  gerichtet,  ihnen  feind':  Jra-\ varänl  mazdayasnS  zara'hu^tri^'vS  aAura.- '. tka^sS  Y.  12. 1 ;  Vr. 5. 3,  Yt  13. 89,  Y. p.  1 3;  j —  andvTtn  süram  anShitam  .  .  °vqm  | ahura.tkaisqm  Y.65,  i ;  —  väHm . .  'dsyum  "  l ahurs.ikalssm  Yt.  13.  90';  —  mq%ra!a  \ spsnia  .  .yS  °vö  'vahe  astä  mazdä  ahuraht\ "und  (mit  Unterstützung)  des  heüigen Worts,  des  Z).-feindlichen,  des  Boten  des ' Z>.-feindlichen  AhAf."  Yt  13. 146.  a)  bes. , von    'data-  n.  (Stverz.):    dstam    'dSyBm'K
27816:(zu)  hoheitsvoll'.  2ar.  wurde  . .  gewahr: 'Die  .  .  Dafva  verabreden  sich  über mein  Verderben'.  Es  erhob  sich  Zar.^ es  machte  sich  auf  Zar.  ungebeugt  .  . Steine  in  der  Hand  haltend , .  (vom  Schöpfer AhM.  sie  bekommend)  ...  Zu  wissen tat  Ärr.  dem/(j1/,:  'Ich  werde  die  daeva- geschaffene  Schöpüing  schlagen  .  .,  bis dass  der  Heiland  geboren  wird  .  .'■  Ihm antwortete -4 J/".:  'Zerstöre  meine  Schöpfung nicht,  o  heiliger  Zar.  Du  bist  der  Sohn I'ourui'aspas.  Von  deiner  Mutter  ward ich  angerufen.  Schwör  ab  die  . .  mazd. Religion,  um  die  Gunst  zu  erlangen,  die erlangte  Vat.  . .'.  Ihm  erwiderte  der  Spit. Zar.:  'Ich  werde  die  .  .  mazd.  Religion nicht  abschwören  .  .'"  V.  jp.  iff.;  -  - Vok.  sehr  häufig,  oft  nur  zeilenflillend: Y. 51.13,  14,  15,  65.10,  71.1,  14,  IS,  Vr. 21.2,  Yt/.9,  10,  34,  35^,  2.11,  13',  4.9, 5.7,  88,  102,  II.  \,  4,  6, 13.3,  9,  ao,  11^46, V.2.3',  43,  j.4a, 4.46,5- 17,  »1,3s,  (J. 37', 7.53,  5.13,14,  lO.iZ,  11.2,  JJ.39,  /7.4, $,  iS.e^t*,  J().i3£*,  21,  34,  H./.2,  4,  7, P.  27,  2S,  2(j,  43,  46,  4$,  FrW.  I.  3,  S.  3, 10.40,   F.  4e;    s.  noch  unten  bei  a  und
== NYB dew ==
655:Art-vahišt [?rtwhšt'] 402; Urt-vahiSt Pwrtwhst'] 39%,  A&a-vahist [?šwhšt'] 394-5, 401-4, 589. 593, 9727 one of the Amahraspands (g.v.). — art, urt < OlrSkr rta- ‘the right cosmic order, the divine law’, Av. (192) arata-, (349) orota-, (229 sqq.) aša- + vahista- (v. vahišt) 'the best, the heavenly law'. Asa-vahist is directly borrowed from Av. (233 sgg.); also the name of the 2nd month of the year and the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. Cf ahlav, ahläi, artči; Arta-xšahr "he whose dominion is (de- termined) by the divine law’.
845:*āyiyān [’dyw’n'], *āyiyānak [Pdyw'nk'] a bird’s nest 409-16-25, — Reading hypo- thetical; I identify the w. with MPrth ’hy’ng = ähiyänag ‘nest’ (A-H III) < "a0iyan-, borrowed in SW and subjected there to the usual alternation -h- : -y-. The genuine SW form is found in NP 4é- yanah < "čdOyčna-, with -0y- in contact- ual position > -sy-. As to the spelling -yw- for -iy- cf apiyuat, giyäk, niyandar.
1300:divan [dyw'n'] the government office 11124. 11227-13, — NP divän, Arab. lw. diwän; Arm. lw. diwan already in the Bible. Possibly < *dipi-vahana- 'docu- ment house', v. dépivar.
1301:divar [dyw?l] a wall 39%, — NP divar. V. Hübsehmann, PSt 65, no. 599, whose etymology is quite satisfactory: *dida- vüra-, v. the next w.
1412:dütak [dwtk'] family 212. 1322, 3726, 386, — Talm. lw. dywig’ ‘family’; NP didah.
1524:framätan [inscr.], framütan [plmwt'n] framäy-, imp. sg. framäi 10% ete. and framäye [plm’dyd 923,plm? dh 272, plm’ - dyw 5725]; pres. 2d p. sg. framdyé [plm’yh 64, plm’dyh 244]; 3d p. sg. = 2nd p. pl. framäyet 141°, 261° [plm’dt!, ef Ps. hwéty and ywdty 1289, v.s. v. hošitan and yöd-]; Ist p. sg. and pl. framdyém [plm’dym]; pt. = pret. pass. 3d p. sg. inser. framät [prm*t, plm?t; plm’ty P2:4], in the books framüt: to order, to issue an order, to command, to bid, with 6 of the p. to whom (3725-27), and rād of the p. concern- ing whom(219?)the order is issued; with a dir. obj. of the ordered th. 38. 64. 199%; apt-t pasēh framayém karkäs and we shall order the vulture (after thee —) to pursue thee 604; mā man 6 pasčh framdi do not bid me to turn my back 5774-75; — to please to, to deign to, with inf. 1122-26, 149; — kar framutan = kar kartan 27, v. kar; — the order itself is expressed 1. in dir. speech by an imp. introduced by ku: framut kū "nikēr” 45; 1213. 33%; consequently, in 216 (framut ku ...) ‘BYDWN-x, and in 109? YDLWN.x; should be taken as the imperatives kuné and baré; — 2. by a subordinate clause a) with kū + pres. ind. 313-5; b) with tāi + pres. ind. 129-19; c) after the pret. framut, with ku tài + opt. pass.: 217-18; d) introduced by the rel. pron.: amah framatké ... cit” we ordered someone (an
1982:hép (Prth) [hyp] particle denoting the opt., placed immediately before the vb.: hip HQ’YMW-d (v. avistätan) — hēp SDYW (v. vistan) HajA:12.13. - MPrth hyb (BBB); < *aiva-pi, Av. (22) aēvā + pi, V.S. V. -p; v. also ēv.
2946:pardaxtan [pldhtn'] pardac- [plde-] to run after, or to run to an end: 1. to strive for (6): avis névak pardac strive well for it! 7616 (Paz. friz = frēc [plyc], g. v., Skr v. sadrsam sädhu vardhaya; however, Cod. K has explicitly pidc with a marked d ; this reading pardac, accepted already by West, suits the context bet- ter). — 2. to be accomplished, finished, cf MPrs w "z ’wd dyw'n zd "wd prdxt mnd
4210:vistan [SDYTN-stn'; Prth. SDY-] *vind- (v.s. v. vindak) to shoot; pt. — pret. pass. 3d p.'sg. vist, written SDY-t HajA: 5.6, SDYTN HajB:5.6; opt. 3d p. sg. hyp SDYW HajA:13, ?yw ŠDYTN HajB:14, both probably = vindé (v. also kep and ev); — ~ ne dānam I do not know how to shoot 2819-20. — Av. (1318 sqq.) *vaēd-, cf vindätan; cf Av. (1320) *vaēda- 'arrow-shot', the name of a weapon of attack. The pres.-stem is however not given in FrP 14 where the ideogr. is listed; nor is the Prth equi- valent of SDY- explicity established.
5797:’rdywh(ySt): Art-vahist
```


## [2026-09-05T17:34:18.681Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN diba ==\"; grep -n -i 'dībā\\|dibā\\|diba\\b\\|dëbà\\|debä' HRN.txt | head -20; echo \"== HUB ==\"; grep -n -i 'diba\\|dība' HUB.txt | head -20",
 "description": "grep Horn/Hübschmann for diba"
}
```


### [2026-09-05T17:34:18.741Z] TOOL RESULT

```
== HRN diba ==
5299:591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
13204:' pädebän 267.
== HUB ==
```


## [2026-09-05T17:34:20.336Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PLA dibag ==\"; grep -n -i 'dībāǧ\\|dibag\\|dībāj\\|diba' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20; echo \"== AFM ==\"; grep -n 'ديباج\\|ديبا' AFM.txt | head -10",
 "description": "grep Asbaghi and Addi Shir"
}
```


### [2026-09-05T17:34:20.399Z] TOOL RESULT

```
== PLA dibag ==
9178:&” dabaf: "mit Figuren bemalen, sticken" s. dibag. 
9904:< Mp. „ro, depäk ap. dipi 2 Syrı 32 3 3, mand. diba& (p. eb> ) a 
9907:do» - di dibäf = diba Ss. diba. 
9909:El» - dibag? : "Vorrede" dim. v. diba 5, 
9910:Sl» - dibagi: "Brokathändler". 
== AFM ==
389:( )ܠ ܚܡܕ الديياج الغليظ وقيل ديباج يعمّل بالذهب او ثاب + ܨ صفاق 
2497:( الدياج) معرب ديباً وهو الثوب الذي سداه ܙܥ :4 حرير. وقيل ان ديا
```


## [2026-09-05T17:34:26.616Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA context ===\"; sed -n '9895,9915p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt; echo; echo \"=== HRN context ===\"; sed -n '5290,5320p' HRN.txt",
 "description": "Context in Asbaghi and Horn"
}
```


### [2026-09-05T17:34:26.672Z] TOOL RESULT

```
=== PLA context ===
dayäwin 129 


«sl,» - dayäwin: Pl. v. ©l,, diwän s. diwän. 


IL») - dibä:; "Brokat, gestickter Goldstoff" pers, I aus pers. Lı> dibä 


< Mp. „ro, depäk ap. dipi 2 Syrı 32 3 3, mand. diba& (p. eb> ) a 


do» - di dibäf = diba Ss. diba. 

El» - dibag? : "Vorrede" dim. v. diba 5, 
Sl» - dibagi: "Brokathändler". 

Ole, -divag = ding s. dinag °. 

2>> - dibüg = dübüd s. dibu 7, 


=== HRN context ===
Das eze etc. der Dialekte von Kasan ist sehr in-
teressant.
*) Firdüsi reimt aber das Wort auf est (Sahn. I, 205 Anm. S
Calc).
') Firdüslfliat aus metrischen Gründen bisweilen auch däh.
«) Yergl. siiukoYski s. v. dehne (S. 129).
*) Bei Fi*k findet man im Wörterbuch* mehrmals ein aw. zyö
'gestern' ohne Stern und — leider auch ohne Belog.
9*- 132 —
591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
phlv. depäk {S«äy. näsäy. 4, i), arm. LW. dipak, syr.
LW. :i2n.
Die Etymologie ist nicht sicher, da im Sanskrit nur
Formen mit T, nie solche mit e vorkommen.
592. dlden 'sehen, dld 'Anblick; sehend', didär,
ap. i^dai-, didiy sehen'; aw. l/'rföi-, a]di^aifi:
phlv. dUan; ai. V^dhäi-, didhye.
kurd. dUin *sehen' ; af/. Udal ; bei. dU, diMr (LW.),
dtdö:^ ^Augapfel'; wa/. didig-am.
593. "des, -dis, -des gleichend, ähnlich*.
aw. dareS' 'Blick* (yt. 19, 94); ai. dfc- *das Sehen;
sehend*, -dfga- '-Aussehen; -sehend*.
Der r- Vokal ist hier durch e vertreten, wie in heSe
(No. 256). Aw. daesa- (yt. 13, 104), das Darmeste-
ter als *Traum' nimmt, ist zu unsicher, um ver-
glichen werden zu können.
594. deg *Topf*, vergl. dez, deze,
phlv. deg 'Topf; lat. figulus^) Töpfer*; mhd. tigel^
tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*.
LW. kurd. dizik; af/. deg^ decka; bei. deg, dez, dPd,
```


## [2026-09-05T17:34:57.857Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SNS depak ==\"; grep -n -i 'depak\\|dēpāk\\|dep[aā]k\\|dyp' SNS_pages.txt | head; echo \"== SNS 'brocade/dibā' ==\"; grep -n 'دیبا' SNS_pages.txt | head; echo \"== MON zhornal ==\"; grep -n 'ژورنال' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head",
 "description": "grep SNS and MON"
}
```


### [2026-09-05T17:34:57.942Z] TOOL RESULT

```
== SNS depak ==
5188:                                                                                          UKotval.p'dypr'hzsl* LGNPE. 36)?
== SNS 'brocade/dibā' ==
== MON zhornal ==
```


## [2026-09-05T17:34:59.667Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN journal ==\"; grep -n -i 'journal,' KLN_1966.txt KLN_1971.txt | head -5; echo \"== WLD deiuo ==\"; grep -n -i 'deiuo\\|deiwo' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "grep Klein and Walde-Pokorny"
}
```


### [2026-09-05T17:34:59.735Z] TOOL RESULT

```
== KLN journal ==
KLN_1971.txt:7519:diurnal and cp. journal, sojourn. The insertion 
KLN_1971.txt:71038:nal, diuturnal, journal, and the second element 
KLN_1971.txt:74208:next word. Cp. also journal, which is a doublet 
KLN_1971.txt:129452:journal, adj., daily (archaic). — ME., fr. OF. 
KLN_1971.txt:129458:journal, n. — F„ lit, ‘a daily paper’, fr. OF. jor- 
== WLD deiuo ==
48705:w-Erweiterung *deieu(o)- ( :deiuo -, diuo- und dieu -, dill-, 
48766:o-St. deiuo- „Gott, Himmlischer" : ai. dcva-h „Gott“ (dvvt „Gottin“), av. 
48767:daeva- „Damon“; lat. deus und divas (beides aus dem Paradigma *deiuos,
```


## [2026-09-05T17:35:08.667Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T17:35:08.675Z] TOOL RESULT

```


```


## [2026-09-05T17:35:09.704Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '129445,129475p' KLN_1971.txt; echo \"=== WLD page tag ===\"; grep -n 'deiuo-' incoming/WLD/WLD_Bd1_pages.txt | head -3",
 "description": "Klein journal entry, WLD page"
}
```


### [2026-09-05T17:35:09.779Z] TOOL RESULT

```
joule, n., unit of electrical energy (physics). — 
Named after the English physicist James Prescott 
Joule (1818-89). 

jounce, tr. and intr. v., to jolt; n., a jolt. — Prob. 

a blend of jump and bounce, 
journal, adj., daily (archaic). — ME., fr. OF. 
jornal, jurnal, journal (F. journal ), ‘daily’, fr. 
L. diurnalis, ‘diurnal’, fr. diurnus, ‘daily’. See 
diurnal, which is a doublet of journal and cp. 
journey. 

journal, n. — F„ lit, ‘a daily paper’, fr. OF. jor- 
tjal, jurnal, journal, ‘daily’. See journal, adj. 
Derivatives : journal-ese , n., journal-ism , n., 
journal-ist, n., journal-ist-ic, adj., journal-ize, 
tr. and intr. v. 

journey, n. — OF Jor nee, jurnee, jour nee (¥. jour- 
nee), ‘day; day’s work, day’s journey’, fr. VL. 
* diurnata , ‘day, day’s work’, fr. L. diurnus, 
‘daily’. Cp. It. giornata, OProveng. jornada and 
see diurnal, adj. Cp. also journal, adj. and n., 
adjourn, sojourn. The ending -ata in diurnata is 
prop. fern. pp. suff. See adj. suff. -ate. 
Derivatives: journey, intr. v., journey-er, n., 
journey-ing, n. 

joust, just, intr. v., to tilt. — ME. justen, jousten, 
fr. OF. joster,juster, jouster (F.jouter), ‘to joust, 
=== WLD page tag ===
73167:  o-St. deiuo- „Gott, Himmlischer" ai. dcva-h „Gott“ (dvvt „Gottin“), av.
```


## [2026-09-05T17:35:15.934Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=73167 && /pdf page/{p=$0} END{}' incoming/WLD/WLD_Bd1_pages.txt; python3 - <<'EOF'\nimport re\np=None\nfor i,l in enumerate(open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace'),1):\n    if 'pdf page' in l: p=(i,l.strip())\n    if i==73167: print('line 73167 preceded by',p); break\nEOF",
 "description": "Find WLD page tag"
}
```


### [2026-09-05T17:35:17.560Z] TOOL RESULT

```
line 73167 preceded by None
```


## [2026-09-05T17:35:17.878Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-",
 "prompt": "Give the reconstructed root, its meaning, and the derived terms/descendants listed (especially *deywós, Avestan daēva, Latin deus/dies/Iuppiter, Greek Zeus, Proto-Germanic *Tīwaz). Quote key lines."
}
```


### [2026-09-05T17:35:23.819Z] TOOL RESULT

```
# Proto-Indo-European Root *dyew-

## Reconstructed Root and Meaning

The root **\*dyew-** has two primary meanings:
1. "to be bright, to shine"
2. "sky, heaven"

## Key Derived Terms and Descendants

The entry lists extensive descendants across Indo-European language families:

**Major descendants include:**
- **\*deywós** - a significant derivative form
- **Latin**: *dies* (day) and *deus* (god), plus *Iuppiter* (Jupiter)
- **Greek**: Zeus (from \*dyḗws)
- **Proto-Germanic**: \*tīnaz, leading to Germanic day-related terms
- **Sanskrit**: द्यु (dyú, sky/heaven) and दिन (diná, day)
- **Anatolian languages**: Hittite šiwatt- (day)

The source notes that "some derivations have undergone metathesis of the root, giving *deyw-*." This explains variant forms across different language branches, particularly how the root produced both celestial/divine terms and temporal (day-related) vocabulary throughout Indo-European languages.
```


## [2026-09-05T17:35:32.736Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7",
 "prompt": "What is the Persian entry دیبا? Give its meaning and full etymology as stated (Middle Persian form, any Old Persian / Sanskrit / Aramaic antecedents), and any descendants (Arabic ديباج etc.). Quote the etymology verbatim."
}
```


## [2026-09-05T17:35:34.682Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88",
 "prompt": "For the Persian entry دیو (div): give the meaning and the full etymology (Middle Persian, Avestan daēva, Proto-Iranian, Proto-Indo-Iranian, PIE *deywós). Quote verbatim. Also note anything about دیوانه (divāne)."
}
```


### [2026-09-05T17:35:40.407Z] TOOL RESULT

```
# Persian Entry: دیبا (dêbâ)

## Meaning
**Brocade** — a rich fabric with raised designs, often incorporating gold and silver threads.

## Etymology
The word derives from Middle Persian *dēbāg* ("brocade"), likely stemming from Proto-Iranian *\*diHp-* meaning "to shine, light up." This etymology references the lustrous quality imparted by precious metals in traditional brocades. The Sanskrit cognate दीप् (*dīp*, "to blaze, to glow") shares this root.

**Verbatim etymology quote:**
"From Middle Persian [dēbāg], probably a derivative of Proto-Iranian *\*diHp-* ('to shine, light up'), due to the sheen imparted by the gold and silver in traditional brocades."

## Notable Descendants
- Arabic: ديباج (*dībāj*)
- Georgian: დიბა (*diba*)
- Ottoman Turkish: دیبا (*diba*)
  - Modern Turkish: *diba*
  - Serbo-Croatian: *díba*

The Persian term is a doublet of دواج (*dawāj*), meaning "bed-quilt."
```


### [2026-09-05T17:35:41.406Z] TOOL RESULT

```
# Persian دیو (div)

## Meaning
In Persian, دیو means "demon, devil, goblin; evil supernatural creature." It can also refer to a wicked jinn (in Islamic contexts) or a daeva—a spirit of evil in Zoroastrianism.

## Etymology
The word traces back through multiple language stages:

**Quoted from the source:** "Inherited from Middle Persian 𐫅𐫏𐫇 (dyw /⁠dēw⁠/)."

The etymological chain continues upward: Middle Persian derives from Old Persian 𐎭𐎡𐎺 (d-i-v), which came from Proto-Iranian *daywáh, then Proto-Indo-Iranian *daywás, and ultimately Proto-Indo-European *deywós (meaning "god").

## Related Term: دیوانه (divāne)
This appears as a derived term from دیو, listed under "Derived terms" in the Persian section, though the source provides no additional definition or context for it.
```


## [2026-09-05T17:35:54.624Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/journal",
 "prompt": "Give the full etymology of \"journal\" verbatim, including Old French jornel, Latin diurnalis/diurnus, dies, and PIE root. Also mention what it says for the root dyeu-."
}
```


## [2026-09-05T17:35:56.802Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%D9%88%D8%B1%D9%86%D8%A7%D9%84/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for ژورنال? Give the entry verbatim including any origin tag such as [فر.] (French). Also any Dehkhoda entry text."
}
```


### [2026-09-05T17:36:00.312Z] TOOL RESULT

```
# Etymology of "Journal"

According to the Online Etymology Dictionary, the word "journal" originates from mid-14th century Anglo-French *jurnal*, derived from Old French *jornel*, meaning "a day; time; a day's travel or work."

The entry traces it further back: "properly 'that which takes place daily,' noun use of adjective meaning 'daily, of the day,' from Late Latin *diurnalis* 'daily,' from Latin *dies* 'day.'"

Classical Latin also used *diurnus* for "of the day, by day," and as a noun meaning "account-book, day-book."

Regarding the Proto-Indo-European root, the source states: "from PIE root *dyeu- 'to shine.'" The page also notes that this root appears "in derivatives 'sky, heaven, god'" when applied to related terms.

The etymology explains a phonetic transformation: when Latin's initial *-d-* is "followed by an *-iu-*, the *-i-* becomes consonantized as a *-j-* 'and eventually ejects the d.'"
```


### [2026-09-05T17:36:03.510Z] TOOL RESULT

```
# Farhangi Mo'in Entry for ژورنال

According to the Farhangi Mo'in section, the entry reads:

"(ژُ ) \[ فر. \] (اِ. ) ۱ - روزنامه . ۲ - مجلة مخصوصِ مُ د لباس ."

This translates to: newspaper; or a magazine specifically devoted to fashion/clothing.

The Dehkhoda entry states: "ژورنال. ( فرانسوی ، اِ ) روزنامه و در زبان فارسی غالباً به مجلاتی که در آن صور متنوع و اشکال مختلف البسه رسم شده و در خیاطی بکار است اطلاق می شود."

This indicates the word originates from French and in Persian typically refers to magazines featuring diverse illustrations and clothing designs used in tailoring.
```


## [2026-09-05T17:36:13.066Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# look for column numbers near line 12459\nfor i in range(12420,12470):\n    l=lines[i-1]\n    if re.search(r'\\b6\\d\\d\\b|\\b\\d{3,4}\\b', l[:60]):\n        pass\nprint('\\n'.join(lines[12440:12462])[:1500])\nEOF",
 "description": "BRT daeva context"
}
```


## [2026-09-05T17:36:14.482Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT daiva ==\"; grep -n -i 'daiva' KNT.txt | head -10; echo \"== SKT Tuesday ==\"; grep -n -i 'tuesday' SKT.txt | head -5; echo \"== SYN god ==\"; grep -n -i 'deiwos\\|deivos' SYN.txt IEC.txt | head -10",
 "description": "grep Kent, Skeat, Buck, Mann"
}
```


### [2026-09-05T17:36:15.000Z] TOOL RESULT

```
asahya  axäyai  (sd.)  ggnedim  Y.  37, 17;  — aiäunqm  . .  uruns  .  .  kudüJiatanqmAt  .  . yailqm  vahehl^  'na  vanainti  va  vSnghm va  vaonarS  va  H.  3g.  z;  —  karapanS kavayasca  .  .  ySng  ^S  urva  ::^a!^a  xrao- dat  (sd.)  'na  Y.46.11;  —  Ö  dngvats *tnandaHg  *9r?tael  (sd.)  haihim  yehya urvü  xraodaiti , .  Y.  ji,  13;  —  tsm  *vä ahsm  dtTgvantS  .  .  'na  nailal  (sd.)  Y.^y/. so;  zT.  verwendet  V.f.  fia;  s.  a;  —  ySi .  .  aiäm>m  vandtn  (sd.)  . .  töi  daoiStig dqn  yS  drsgvats  °na  ",.  die  —  in  AnDaiva Haus  fUr  das  Ich  des  ^rv^enossen!"  Y. 4^.  4*>.  a)  im  jAiv.:  alaonqm ..  ahümla 'nam/ai*  iaooasäi  urvänsmca  fravaiSmia yagamaide  Y.  a6.  4;  —  asni  iyazamaide\ manä  . .  °nä  [yazamaidi]  saoryantqm  yaaa- vtaide  Yt  13.  7^;  —  aisS  zT  växs . .  a  va^S ahunB  vaityS . .  uruna^a  'tiaca  (IS.)  span- vanti  (sd.)  H.  J.  4;  —  'nqm  .  .  yaoldai- är/a  dha  zl  aifihä  asH  yaosdaitis  kahmai- Ht  ..  havaya  tnsvS  'naya  yl  hvqm  'nqm yaozdaite  humataisla  ..  V.  10.  19*';  —  um vä  ahOm  drvaniö  *^a  *'na  msirtnttyJJ [a/isiäi  a/fuhe]  V.  5. 6a;  —  aiiihä  dim vütaya  fr-Jmita  (sd.)  salayeiti  ya  hava 'naT>  kaininS  k>hrpa  srlrayh  .  .  aat  Alm aoxta  ..yS  nars  asaonü  urva  alca  Karditis ahi  ..?  äat  hl paiH.aoxta  ya  hava  'na  .. az?m  ba  U  ahmt  .  .  yä  hava  'na  *:^ai- paihejanvö  {sd.Y'  H.2.9— 11; — arahvam 'nqm  V.^.ai  PüZ.s),  io.  19  PüZ.
*)  Ein  tlieologiscb-philo
```


### [2026-09-05T17:36:15.068Z] TOOL RESULT

```
== KNT daiva ==
122:І The Inscription and Sculptures of Darius the Great at Behistan.............. II The Gold Tablet of Hamadan ПІ The Daiva Inscription of Xerxes
1060:IIT. OP d from pIE d: pIE *deiyo- ‘deity’, OP daiva- (evil) god’, Av.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
3368:XPh = Xerxes, PERsEPOUIS н: The Daiva Inscription: Trilingual, on stone tablets, found in the building on the southeast corner of the ter- race; 2 OP copies, one complete in 60 lines, the other stopping in the middle of line 51; 1 Elam. сору in 50 lines, 1 АКК. copy in 50 lines. New York Times, Feb. 9, 1936; Univ. of Chicago Mag. 28.4.23-5 (Feb. 1936); EFSehmidt, Ill. London News, Feb. 22, 1936, page 328; Kent, JAOS 56.212-5 (1936); AfOF 11.91 (1936); Hz. AMI 8.56-77 (1936), RHRel. 113.21-41 (Jan.-Feb. 1936); HHartmann, OLZ 40.145-60 (1937) ; Kent, Lg. 13.292-305 (1937); Hz. Арі 27-35 No. 14 and Plates 10-3 (1938); Wb. Symbolae Koschaker 189-98 (1938; on the Elamite version); ILevy, Revue historique 185.105-22 (1939); EFSchmidt, 'The Treasury of Persepolis 12-5 (1939); Sen, OPI 148-56 (1941); VIAbayev, Hranskie Yazyki 1.134-40 (Izd. Ak. Nauk, Ҥашса vol. 3; Moscow- Leningrad, 1945).
4592:37 šnă : Auramazdahà : adam: avam : daivadina
4610:59 yàvam : aita : adam : Auramazdam : jadiy 60 àmiy : aitamaiy : Auramazda : dadàtuv Notes To XPh: " The h* of abaraha has become л by failure to engrave the prior angle. ? tye for уу = tyaty. ? The p? of upariy lacks the two small verticals in copy a. * The daivaddna- of copy a is daivadáva- in copy b; the engraver was misled by the v* ending the previous line (Hz. AMI 8.62). ® ydeiysis for yid'iysife = yadiyaiša. 4 For the normalization brazmaniya here and in 51 and 54, see Lex. s.v, 4° antya$c for «cnp = -ciy. 5 The me of -maiy lacks the small middle vertical in copy b. 6 The a of kā, in both copies, has the horizontal over а single vertical only. “ арага is perhaps an error for aparam, which elsewhere stands in this idiom. " Copy b ends midway in this line, with the left-hand part lacking; the engraver was accustomed to Aramaic writ- ing, which went from right to left, Hz. AMI 8.62. 50 pariyail = -iye = -tiy. % In the prior uid the space for the first character is left blank; probably the char- acter in the model copy was illegible to the engraver.
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
== SKT Tuesday ==
== SYN god ==
```


## [2026-09-05T17:36:42.681Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT Tues ==\"; grep -n -i 'Tues\\|Tiw' SKT.txt | head -8; echo \"== KLN Tuesday/deity/Zeus ==\"; grep -n -i '^Tuesday\\|Tuesday, n\\|^deity\\|deity, n\\|^Zeus\\|Zeus, n' KLN_1971.txt | head -10",
 "description": "grep Skeat and Klein"
}
```


### [2026-09-05T17:36:42.780Z] TOOL RESULT

```
== SKT Tues ==
942:Aristocracy.  (Gk.)  Modified  from  Gk. upicTiwparta,  govenunent  by  the  nobles  or •  bt-sl'  men.  — Gk.dpiiJTo-,  for  d/«ffTot,  best; and  Hparuv,  to  be  strong,  govern,  from mftiTin,  strong.  The  form  op-taroi  is  a  su- perlative from  the  base  d/i-  seen  in  np-rtof, hi.  (ip-iT^.  excellence.  (V  AK.  to  fit.) Per.  aristacmiic ;  whence  aristocrait  pot for  '  aiistocratic  perMjn.'
1523:bastinado.  (Span.)  From  Span,  bos- tiwada,^  bcAling.  — Span.  &aj/on,  a  stick~ lx>w  L.  bas/ijnem  (above).
3189:incessant,  ceaseleu.  (L.)  L.  itues- lanf;  stem  of  ittcfssaMt,  unceasing.— L.  wi-, not ;  cessans,  ceasing,  pros.  pt.  of  ressart, to  cease ;  see  oeaae  (above).
3534:Claw.  (£.)  M.  E.  dau,  eUe.  A.  S. dawu  ;  also  dd^di^,  a  claw.'f-Du.  klaatiw, led.  j(/J.  Dan.  Jth,  Sw.  kio.  G.  klaue. Allied  to  Clow ;  from  a  Teut.  base  KLU -Aryan  GLU.     CI  glue.
3548:glair,  the  white  of  an  egg.  (F.-L.> M.  E.  gleyre.^O,  F.giain.  —  L.  (lam.  fern. of  clartts,  bright;  Low  U  clara  oui,  the while  of  an  egg. Cleave  (i).  to  split.  (E.)  Strong  yerb. A.  S.  cMfan,  pt.  t.  c/r^i/.  pp.  €lofm  (-» E.fA«'/n).  +  Du.  klevtn.  Ice!.  *^V/a  (pt.  t. klauf).  Swcrl.  klyfva,  'Dvi.kicve,  G.  khtbm. (Teut.  bnsc  KLUB;  cC  Ck.  7^£^«k,  to holltiw  out.)
5541:duchy  (F.-L.)  F.  ^itt-M-Low  L. dmaium,  ace.  of  JucaiHS,  a  dukedom.  *L. tiw-.  ktem  ol  '/mjt,  a  duke.
5651:Eaves,  the  clipped  edge  of  a  thatc^ roof.  \E.^  M.  E  eutu\  pi  tuesu  ( eaveses).  AS.  efese^  a  clipped  edge  J thatch ;  whence  e/etian,  to  sorar.  ^  li N/Ui  Swed.  dial,  uffs,  Goth.  M^itiMi,  a  poi from  (he  prcjectioa  of  the  eaves ;  O.  Hj e/asa.  Urig.  sense  'that  which  profi or  is  over ; '  allied  to  Over.  Dar.  Ml dropper^  one  who  stands  under  droppi from  the  eaves,  a  secret  lisicncr.
5712:Egg  (1),  the  oval  body  whence  chickens, Ac  are  hatched.  (S.and  >  M.  E  #x'.  I'l* <Si''''J  -  Icel.  <gg,  Dnn.  ag,  tiwcd.  z^^. + A.  S.  ay  (-M.  £.  ty") ;  Du.  ii.  G.  ei.  Irish ugh,  GaeL  ^h,  W.  jt-}-,  L.  ouum,  Gk.  tWi'. Allied  to  L.  auit,  a  biid.
== KLN Tuesday/deity/Zeus ==
7430:deity. 
66658:deity, n. — ME. deite, fr. OF. deite (F. deite), 
68079:deity and date, ‘point of time’. For the use of 
69826:deity. 
71037:deity and cp. dial, diary, diet, ‘assembly’, diur- 
71803:Zeus’, fr. Aio?, gen. of Zeu?, ‘Zeus’, and ptTjSo?, 
71823:Zeus and cp. prec. word and the first element in 
136149:deity. Accordingly OE. lengten , etc., prop, 
141775:Zeus a dish of human flesh, in order to test his 
142573:Zeus at Athens, lit. ‘stormy, boisterous, impetu-
```


## [2026-09-05T17:36:44.878Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LAT deus ==\"; grep -n 'deus\\b' LAT.txt | head -8; echo \"== LAT dies ==\"; grep -n 'diēs\\|dies,' LAT.txt | head -8; echo \"== IEC dei ==\"; grep -n -i 'deiuos\\|deiwos\\|dīpaya' IEC.txt WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "grep Ernout-Meillet, Mann, WLD"
}
```


### [2026-09-05T17:36:44.968Z] TOOL RESULT

```
== LAT deus ==
920:abaddlr ind.: 6 paixoTuoC; "abaddir deus dicitur, quo nemine lapis uocatw
1172:pond A notre "de fil en aiguille". De deus derivent acuc; - is: aiguiser
2478:lois: itus deus appellatus araque ei statuta est, quae est <in > infima
4746:Derivas: arculus: putabatur esse deus qui tutelam gereret arcarum,
8341:^trusque, comme aesar "deus". Si le nom se rapporte A caesus, il
10487:Derives: caudeus ; cf.P.F.40,19, caudeae cistellae ex iunco, e simili¬
11519:mus ipse deus arcens et continens ceteros-, toutefois semble plus
13584:sons terre, cf. Serv., Ae .8,636, Consus autem deus est consiliorum (etyn.
== LAT dies ==
8275:dies, et d'autre part le type v. latin aruorsum en face de aduersus.
8458:au pl., caelites - oupav uovec. Pour la fornation cf. dies, -it is de ala.
16753:dies, -ei (-Si,-e) ». et f.: jour; espace d'une journ^e. Le genre,
16793:dans les 1 .roaanes: Lunae, Martis dies, etc., cf. M.L.5164,5383,5519,
16847:satif diem qu*a 4 t 4 fait le paradigae de dies, et ce aot a 4 t 4 reserre
17145:cf. dies, ou l'adj. aubstantiy 4 et diyinis 4 . - Fomes, rares et archai-
17822:spiritum-, d. somnos, d. pocula', d. aetatem (c. agere), dies, noctem; d.
18863:ire (= exire, ou^eoOcxi,), Lucr.3,536; it dies, Pl.Ps.340*. D'usage fre-
== IEC dei ==
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:48767:daeva- „Damon“; lat. deus und divas (beides aus dem Paradigma *deiuos, 
IEC.txt:2112:deiuaið (denom. of deiuos, q.v.) ‘swear; admire, adore? Osc. deiuast (3s fut. *will swear); deiuatu-
IEC.txt:2122:deiuinos 'god-like, inspired'. See deiuos, dieus Lat. divinus; Osc. deiuin-; OCS divinü "won. derful'; Li. dievinis (*divine'. Lalis)
IEC.txt:2124:deiuos, ios ‘divine, inspired’. See dieus Skt. deváh, adj., dévah, s., Av. daevo ‘demon’; Hes. deós 'god'; Lat. divus, adj. & s.; Osc. deivo, gp; Sequanian devo-, deivo- ‘day’; OCS divij ‘wild’; Li. diévas; Latv. dievs ‘god’; Finn. loanword taivas ‘heaven, sky’
IEC.txt:2322:dieus, obl. diu- (cons. stem) ‘god, sky”. Cf. diu-, etc. WP I, 772. Also: deiuos, à (variant) ‘god, goddess; demon, demoness' Skt. dyáuh; deváb; Per. div ‘demon’; Oss. cf. äv-dīw, -dew (*demon'. Cf. G “Ab-gott'); Thess. cf. dagüs “ritual wax image”; Arm. tiwr, tir ‘god, idol; tiv ‘day’; Av. cf. paiti-dayus *very-deceitful' beside daevo ‘demon’; Myc. cf. diwijewe ds.; Gk. Zeüs; Gk-Albanian Die, gs Diesé ‘God’; EMAlIb. zevé ‘goddess’; OLat. deiuos, L deus; Osc. deivo gp; deívaí fs. dat.; Gaul. divo; W duw; Br. dué; Mir dia, déa, i.s. diu; Runic Go. tyz; OE Tiw ‘Mars’; ON Tyr, pl. tívar; OHG cf. Zios-tac ‘Tuesday’: OE Tiwes-dag, id.; OCS divü ‘portent, wonder’; divo, -ese, id.; dijevü ‘divine’; Li. diévas, voc. Die; Latv. dievs; OPr. deiws; Finn. LW taivas ‘sky’
```


## [2026-09-05T17:36:53.125Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN deity ==\"; sed -n '66655,66665p' KLN_1971.txt; echo \"== KLN Tuesday ==\"; grep -n 'Tuesday, n' KLN_1971.txt | head; grep -n 'Tiu, n\\|Tiw, ' KLN_1971.txt | head -5; echo \"== KLN Zeus ==\"; grep -n 'Zeus, n' KLN_1971.txt | head -3",
 "description": "Klein entries"
}
```


### [2026-09-05T17:36:53.227Z] TOOL RESULT

```
== KLN deity ==
Derivatives: deist-ic , deist-ic-al, adjs., deist-ic- 
al-ly, adv. 

deity, n. — ME. deite, fr. OF. deite (F. deite), 
fr. Late L. deitdtem , acc. of deitds , ‘divine na- 
ture’, which was coined by Augustine on ana- 
logy of Gk. t>e6nrj<;, ‘divine nature’, fr. L. deus, 
‘god’, fr. OL. deivos (whence also L. divus, 
‘divine’), which is cogn. with OI. devah, ‘god’, 
devt, ‘goddess’, Avestic daeva -, ‘demon’, Lith. 
dievas, Lett, die vs, OPruss. deiwas, deiws, OIr. 
== KLN Tuesday ==
221243:Shrove Tuesday, n. — See Shrovetide; so called 
254936:Tuesday, n. — ME. Tiwesdai , Twisdai, Tuesdai, 
66668:OE. Tiw, name of the Teutonic war god, Gk. 
== KLN Zeus ==
270572:Zeus, n., the supreme god of the ancient Greeks.
```


## [2026-09-05T17:36:54.395Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16753,16760p' LAT.txt; echo \"=== deus entry ===\"; grep -n '^deus\\|deus, -i\\|diuus' LAT.txt | head -8",
 "description": "Ernout-Meillet dies/deus"
}
```


### [2026-09-05T17:36:54.458Z] TOOL RESULT

```
dies, -ei (-Si,-e) ». et f.: jour; espace d'une journ^e. Le genre,
est aasculin ou feainin indiff^reaaent au singulier, e.g. Lex Repet.,
CIL I 3 583,63, ubi ea. dies uenerit quodle iusei erunt adesse, et Cic.,
Dos.45; au pl. presque exclusiveaent aasculin: dies festi, nefasti
(exceptions rarissiaes, cf.Thes. s.u. V i°33,70sqq.). Meae au singulier,
le aasc. est plus fr^quent, et seable aussi plus ancien, coaae on le
voit dans Dies-piter, et dans 1 'ancien locatif fix£ dans les expres-
sions postridie, meridie, die quinti, cottldie, etc. Le feainin est
=== deus entry ===
8196:cadiuus (£poq.imp. ): qui toabe de soi-aeme; ^pileptique. Le simple
8197:est peu uaite, maia recidiuus est un peu plus frequent; v. plus loin.
8243:dimus, etc.), d'ou recidiuus-, comme cadiuus , ce mot appartenait d'abord
8248:etiam messes ferant. - Recidiuus a pris de IA le sens de "qui renait"
14784:criiditS,-ds; -tdiio, -tio, crudiuus opp. a coctxuus); "vert, non nur"
16405:deus, -I n. (ancien deiuos atteste epigraphiqaement), dea (deiua
16412:deus
16418:le fi».diua et les cas obliques dlui, diuo, diue, le nominatif diuus
```


## [2026-09-05T17:37:01.466Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '254936,254945p' KLN_1971.txt; echo \"=== Zeus ===\"; sed -n '270572,270582p' KLN_1971.txt; echo \"=== KLN 66666-66675 ===\"; sed -n '66665,66675p' KLN_1971.txt",
 "description": "Klein Tuesday/Zeus/Tiw"
}
```


### [2026-09-05T17:37:01.593Z] TOOL RESULT

```
Tuesday, n. — ME. Tiwesdai , Twisdai, Tuesdai, 
fr. OE. Tiwesdxg (‘day of Tiw'). Tiw is an an- 
cient Teutonic war god, identified with the Ro- 
man Mars. The name Tiw is etymologically con- 
nected with Gk. Z e 6 c, gen. the first ele- 

ment in L. Dies-piter , Ju(p)-piter and with L. deus , 
‘god’. ON. Tyrsdagr, Tysdagr (Dan. Tirsdag ), 
OFris. ties-dei, OHG. Ziostag (MHG. Ziestac ), 
lit. ‘the day of Tyr\ resp. ‘the day of Ziu\ are the 
=== Zeus ===
Zeus, n., the supreme god of the ancient Greeks. 

— Gk. Zeu q [gen. *Ai cogn. with the 

first element in L. Diespiter , Jupiter , ‘Jupiter’. 
See deity and cp. words there referred to. Cp. 
also the first element in Diomedes, Dione, Dios- 
curi, Diospyros, Zenobia. 

zeuxite, n., a kind of brown tourmaline. — Form- 
ed with subst suff. -ite fr. Gk. ‘a join- 
=== KLN 66666-66675 ===
dievas, Lett, die vs, OPruss. deiwas, deiws, OIr. 
dia (gen. de), OW. duiu, MW. duw, OCo. duy, 
MCo. dew, ‘God’, OHG, Zio, Zio, ON. Tyr, 
OE. Tiw, name of the Teutonic war god, Gk. 
8105, ‘divine’, Zsug, gen. Atfos, Aid?, ‘Zeus’, OI. 
dyduh, ‘heaven, god of Heaven’, Dyduspitd , 
‘heavenly father’, L. Diespiter, Jupiter . ‘Jupiter’., 
All these words come fr. *deyew(o)-, ‘shining’, 
which derives fr. I.-E. base *dei~, *deyd-, *di-, 
dyd-, ‘to shine’, whence also OI. df-de-ti, ‘shines, 
diva, ‘by day’, di-vasah , ‘heaven; day’, Arm. tiv,
```


## [2026-09-05T17:37:02.843Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'daiva-' KNT.txt | sed -n '1,20p'; echo \"=== lexicon line ===\"; grep -n \"daiva-,\\|daiva- ‘\" KNT.txt | head",
 "description": "Kent lexicon daiva"
}
```


### [2026-09-05T17:37:02.904Z] TOOL RESULT

```
1060:IIT. OP d from pIE d: pIE *deiyo- ‘deity’, OP daiva- (evil) god’, Av.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
=== lexicon line ===
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
```


## [2026-09-05T17:37:18.267Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SNS size ==\"; wc -l SNS_pages.txt; python3 -c \"\ns=open('SNS_pages.txt',encoding='utf-8',errors='replace').read(); print('ff',s.count('\\f'))\n\"; echo \"== SNS greps ==\"; grep -n -i \"dep\\|dyb\\|dib\" SNS_pages.txt | head -15",
 "description": "SNS structure and greps"
}
```


### [2026-09-05T17:37:20.006Z] TOOL RESULT

```
== SNS size ==
16583 SNS_pages.txt
ff 242
== SNS greps ==
16329:day 193/4                   diblr 308/21                 drOg/drOy 220/3            duzdldag 330/16
```


## [2026-09-05T17:37:20.054Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY دیو ==\"; grep -n 'دیو$\\|دیو ' incoming/ARY/ARY_pages.txt | head -8; echo \"== ARY دیبا ==\"; grep -n 'دیبا' incoming/ARY/ARY_pages.txt | head -8; echo \"== ARY latin index DEV ==\"; grep -n -i 'deiwos\\|DAEVA\\|DIV ' incoming/ARY/ARY_latin_index_pages.txt | head -8",
 "description": "Aryanpur greps"
}
```


### [2026-09-05T17:37:22.421Z] TOOL RESULT

```
== ARY دیو ==
1118:[. البته ارج اجتماعی آنها با مقام والای لبیدهای باستانی قابل مقایسه نیست. متاسفانه اختراع رادیو و
== ARY دیبا ==
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
45:دیباچه / ۵.
46:دیباچه
101:دیباچه / ۷
156:دیباچه / ‎٩‏ ۱
214:دیباچه / ۱۱
276:دیباچه / ۱۳
337:۱ دیباچه / ۱۵
== ARY latin index DEV ==
```


## [2026-09-05T17:37:28.312Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16315,16350p' SNS_pages.txt",
 "description": "SNS index context"
}
```


### [2026-09-05T17:37:28.352Z] TOOL RESULT

```
dastOr 314/5                denlh 193/14                 dost 331/14                dubSzag 328/18
dastoran 314/8              den radan 193/11             sos 332/13                 Dufdav 329/22-335/1
dastorlh 314/10             dSr 182/13                   dosend 334/18              ducmDbag 328/7
dastOrlha 314/14            derang 185/9                 doxt 334/19                dusrav 331/18
dast soy 187/19             der-zaraan 183/13            drayan javisnih 319/16     -dus 332/16
dast sabtg 187/16           dSr zlvad 183/15             drayid 320/4               dus agah 332/19
dast sustan 187/18          dfirzlvisnlh 183/17          drahra 341/19              dusax v 331/1
dasn 316/17                 dev 196/1-205/5              drahnag 319/11-12          dusraan 333/15
dast 315/10                 devan 196/5                  drahna(y) 319/9            dus xv arlh 333/4
dastan 316/3                devar 190/2                  drang 324/6                duvasrujld 327/11
dastanistan 316/9           devart?) 233/17              dranjed 323/7              duxt 107/4
datus 309/19                dSv yazaglh 196/7            draxt 318/21               duz 330/7
daxraag 29/8                did 31/18-177/10             driyosan 324/12            duzd 330/10-15
daxsag 299/3                didan 181/1                  drod 203/8-322/15          duzdld 331/2
day 193/4                   diblr 308/21                 drOg/drOy 220/3            duzdldag 330/16
3ay-ba-mihr 193/9           did 153/4                    drOn 323/16                duzdlh 330/11
3ay dadar Ohrraazd 193/12   didlgar 310/13               drOn I siganag 324/2       duzdlh kardan 330/1
2az6d 312/3                 dihbad 242/14                drOzan 323/11              duzvar 330/13
iazisn 311/22               dihbadfln 242/16             drozanlh 323/15            dvanCuDs 327/8
 i   I                                            V'J   tfi^tfwj'j ^-^t-*

 caanlg 157/4              cegOn/ciyOn 161/12           dSdistSn 189/6-295/18     darisnlh 299/20
 casnlg kardan 157/6       cS gOved 247/15              dSdistan Bmandlh 295/20   d3sr/d5sar 298/12
 cast 156/19               ce-h3d 247/9                 dSdvar 296/2              dasran 298/16
 cSstag 156/13-157/1       ce-h«t 87/1                  dadvaran 296/7            dast 298/17
cahflr40/5-48/10-155/11    c5-m3n 247/13                dadvar I drozan 296/5     daltan 299/1
cahardah 304/12           c6-man handaxt 247/13         dadvar tar 296/8          daltartar 298/23
cahardahum 156/4          ce-I 247/10                   dam 300/6                 dast ested 298/22
cahar payan 155/13        cihr 62/19rl60/l3             dam dad 301/10            dayag 306/1
caharura 156/1            cihrab 160/17                 -dan 301/17               dah 292/4
cakarczanD 158/13         cihragC?) 160/20              danag 301/19-302/9        dah 293/20
cambar 159/17             cikam-c6 _ 161/8              danagan 301/21            dahad 293/21
camisn 159/19             cim 161/11                    danagtar 301/22           dahan 140/12
cand 160/1                cimlgtar 161/13               dane 78/21                dahed 294/10
candfinGd 160/12          clnisn. «161/14               daned 78/22               dahem 294/9
Sand-is 195/11            cisan 158/3                   danem 78/19               dahend 294/13
```


## [2026-09-05T17:37:34.924Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '31[0-9]/' SNS_pages.txt | head -20; echo \"=== search dep ===\"; grep -n -iE '\\bd[eēĕ][bp][aā]?[kg]' SNS_pages.txt | head -10",
 "description": "SNS page 313 index entries"
}
```


### [2026-09-05T17:37:34.985Z] TOOL RESULT

```
14859:                                                                   sasti 313/6
14860: yajfia- 315/4                vinakti f -vivekti 272/18
14862: yakrt 317/7                  vina?a-282/13
14866: yasati, yasyatU?)      314/2 visati 221/6
14891:tamisra- 146/11         distay- 313/13
14893:tapati 153/20           dlpyate, 313/10
14952:                                                     upari 253/21                      giray- 318/20
14954:                                                     ursnay- 334/5                     gurav- 319/3
15093:vicica- 310/19           sava- 190/17                      srva-/srfl 183/8-185/8   haro-   6/3-46/15
15109:vls.paiti- 273/17-286/19 spanta- 175/18                    ha-ydfanham- 315/1       hu-ci^ra- 64/2
15120: baralnQra- 104/5           raaraka-/nahrka- 246/16                yasna- 315/4                 raiti- 222/1
15131:bural- 109/9               malya-/marata- 68/20                    yesi. yaeais 313/2           vaghar- 257/8
15132:buray- 110/12              raS    39/16                            yakar- 317/      7           vayu- 263/22
15182:draxta-C?) 318/20         nCit 221/8
15188:drajah- 319/10
15234:                      zantu- 169/11                       tisarO sata 154/14             dasina 316/18
15251:                      zim, ziraa-,   zyarn    325/10      eritya- 148/15-181/16          dastvam 314/6
15253:                      zufay 168/1                         Qrisat- 227/21                 disti- 313/13
15272:                      tara- 226/11                        daxsta- 299/4-316/4            duz-50ra- 336/14
15304:i9yajah-, i0yejah 314/19 kataraa- 211/2                                                G
=== search dep ===
```


## [2026-09-05T17:37:42.213Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'pyate\\|dTpyate\\|dipyat' SNS_pages.txt | head; echo \"=== ff leaf containing ===\"; python3 - <<'EOF'\ns=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt',encoding='utf-8',errors='replace').read()\npg=s.split('\\f')\nfor i,p in enumerate(pg):\n    if 'pyate' in p:\n        print('leaf',i)\n        print(p[:1800])\nEOF",
 "description": "Find SNS glossary page with dipyate"
}
```


### [2026-09-05T17:37:43.753Z] TOOL RESULT

```
14893:tapati 153/20           dlpyate, 313/10
=== ff leaf containing ===
leaf 206
                                         l£J ffwrfU 4*L ajlj   u^jt-i-, tf U*;lj iz-.jtJ
71
                                                               pratidhana- 123/7            N
tamisra- 146/11         distay- 313/13
                                                               pratimana 120/17             nakh£- 258/4
tapati 153/20           dlpyate, 313/10
                                                               prayah 126/7                 nambh-nabh- 282/3
tapti 145/9             dlrgha- 182/14
                                                               prstay 139/7                 navati-33/11-182/5
taruna- 149/8           dughda- 330/1                           • • *

                                                               piavayati 131/17             navaraS- 262/20
tokman- 150/19          durat-dure- 335/18
                                                                                            naraan- 201/19
tisrah/trayah- 10/5     durraanas 333/17
                                                               B                           nava 11/3-284/4
tuaksas- 150/14         dus 332/17
                                                               bandh- 110/19               nlbh- 258/14
tuccha- 151/6           dudha- 330/8
                                                               bandha, bcdhAti 100/15      nava 148/2
tucchya- 151/4          durah-/dvarau 100/3
                                                               barhis 98/11                nar 164/11
tubh, tuph 147/14       dva- 149/14-307/10
                                                               b3hav 96/14                 narl- 264/20
 turya- 156/2           dvadasa- 292/7-326/17
                                                               bOdha- 111/2
```


## [2026-09-05T17:38:05.632Z] TOOL CALL #49: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/site/pages/111.jpg 2>/dev/null || echo \"no jpg\"",
 "description": "Check page image"
}
```


### [2026-09-05T17:38:05.673Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61141 Aug 22 01:02 /home/sfmqrb/git/rishe/site/pages/111.jpg
```


## [2026-09-05T17:38:07.607Z] TOOL CALL #50: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/111.jpg"
}
```


### [2026-09-05T17:38:07.640Z] TOOL RESULT

```

```


## [2026-09-05T17:38:19.868Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 111 -l 111 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg111 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg111.png'); print(im.size)\n# Latin box approx: in the 1100x1400-ish preview it was x 260-430, y 490-560 out of 1100x1400\nw,h=im.size\nbox=(int(0.22*w),int(0.345*h),int(0.42*w),int(0.41*h))\nim.crop(box).resize((int((box[2]-box[0])*2),int((box[3]-box[1])*2))).save('latin.png')\nprint('ok')\n\"",
 "description": "Render and crop Latin box"
}
```


### [2026-09-05T17:38:22.439Z] TOOL RESULT

```
(2550, 3300)
ok
```


## [2026-09-05T17:38:25.123Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/latin.png"
}
```


### [2026-09-05T17:38:25.142Z] TOOL RESULT

```

```


## [2026-09-05T17:38:38.820Z] TOOL CALL #53: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg111.png data/verification/sources/refs/ocr/BOOK/111.png && for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\" \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\" \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88\" \"https://www.etymonline.com/word/journal\" \"https://abadis.ir/fatofa/%DA%98%D9%88%D8%B1%D9%86%D8%A7%D9%84/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 111, root Dei/Deiw/Dyeu: PIE *dyew-/*deiwos, Persian div, diba, French/English journal, Persian zhornal\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T17:38:42.664Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/05ec9b0ba7f6e67d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68f02d9af94fe136.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/756d24855a3bb355.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff229b9e7713bf5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/34706ae3c7c2a804.txt
```


## [2026-09-05T17:39:52.270Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '60,200p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-05T17:39:52.307Z] TOOL RESULT

```
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


## [2026-09-05T17:46:00.438Z] TOOL CALL #55: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-111.json <<'JSONEOF'\n{\n  \"pdf_page\": 111,\n  \"book_page\": 81,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Dei, Deiw, Dyeu, Dyě\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *dei- / *dei̯H- 'to shine', with the u-extension *dyew- 'bright sky, daylight' and the o-stem *deiwos 'god, celestial one'\",\n      \"note\": \"Pokorny I 183–187 heads the entry '1. dei-, deiə-, dī-, diā- \\\"hell glänzen, schimmern, scheinen\\\"' and puts under it the u-extension 'deieu- (: dieu-, diu-, diu-) leuchtender, göttlich verehrter Himmel und leuchtender Tag' and the 'o-St. deiuo-s Gott, Himmlischer'. Nourai's four-way heading Dei / Deiw / Dyeu / Dyě is exactly this ablaut series (dei- / deiw-o- / dyeu- / dyē-), the language label 'Indo-European' is right and the gloss 'to shine' is the standard one (Watkins: 'deiw-. To shine (and in many derivatives, \\\"sky, heaven, god\\\")'). Only a nuance separates him from current work: Wiktionary and Beekes make *dyew- 'sky, to be bright' primary and *deiwós a metathesised derivative of it, whereas Pokorny/Watkins (Nourai's sources) make the verbal *dei- primary. Both accounts unite exactly the material of this chart, so the chart's shape stands. The whole page is one entry with fourteen nodes; the extraction is faithful to the printed page (checked on the 300 dpi render, copy at data/verification/sources/refs/ocr/BOOK/111.png), including the author's own breve marks in 'diěs' and 'jŭlius'.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *dei- / *dei̯H- به معنی «درخشیدن، تابیدن» با گسترش وَاوی *dyew- «آسمانِ روشن، روز» و ستاک اسمی *deiwos «ایزد، آسمانی». پوکورنی (ص ۱۸۳–۱۸۷) و واتکینز در پیوستِ ریشه‌های هندواروپایی فرهنگ American Heritage همین صورت‌ها را زیر یک ریشه گرد آورده‌اند، پس عنوان چهارگانهٔ نورایی (Dei / Deiw / Dyeu / Dyě) چیزی جز همان زنجیرهٔ ابدال‌های پوکورنی نیست و برچسب زبانی و معنای «درخشیدن» هر دو درست است. تنها تفاوت با پژوهش امروزی این است که ویکی‌واژه و بیکس *dyew- «آسمان» را اصل می‌گیرند و *deiwós را با قلبِ آواها از آن مشتق می‌دانند، حال آنکه پوکورنی فعل *dei- را اصل می‌شمارد؛ دامنهٔ واژه‌ها در هر دو تحلیل یکی است. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:183\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 194 (printed p.183/184, awk RS=\\\\f NR==194): '1. dei-, deiQ-, di-, diä- ,hell glänzen, schimmern, scheinen' (älter ,*Strahlen werfen'?)' — the root, the page and the gloss are exactly Nourai's.\"},\n        {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v.: 'deiw-. To shine (and in many derivatives, \\\"sky, heaven, god\\\"). I. Noun *deiwos, god … [Pok. 1. dei- 183.]' — Watkins gives the same root, the same gloss and the same Pokorny page Nourai cites.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I (WLD_Bd1_1930_djvu.txt ll. 48705, 48766) s.v. dei-\", \"stance\": \"supports\", \"note\": \"'w-Erweiterung *deieu(o)- (:deiuo-, diuo- und dieu-, diu-)' and 'o-St. deiuo- „Gott, Himmlischer\\\": ai. deva-h „Gott\\\" (devi „Göttin\\\"), av. daeva- „Dämon\\\"' — Walde-Pokorny I 772ff. is the source Pokorny himself abridges.\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. dieus / deiuos (IEC.txt l. 2322)\", \"stance\": \"supports\", \"note\": \"Mann: 'dieus, obl. diu- (cons. stem) \\\"god, sky\\\". … Also: deiuos … Skt. dyáuh; deváh; Per. div \\\"demon\\\" … Av. … daevo \\\"demon\\\"; Gk. Zeüs; OLat. deiuos, L deus; … OE Tiw \\\"Mars\\\"; ON Tyr … OHG cf. Zios-tac \\\"Tuesday\\\": OE Tiwes-dæg' — one entry covering nearly every node of this chart.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. deity (KLN_1971.txt ll. 66658-66675)\", \"stance\": \"supports\", \"note\": \"'All these words come fr. *deyew(o)-, \\\"shining\\\", which derives fr. I.-E. base *dei-, *deyō-, *di-, dyō-, \\\"to shine\\\", whence also OI. dí-de-ti, \\\"shines\\\"' — Klein's base list is Nourai's heading.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"daěv, daěvoh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *deiwós 'god, celestial one' > Proto-Indo-Iranian *daivás (Skt. devá- 'god') > Proto-Iranian *daivah > Avestan daēva-, nom. sg. daēvō — Nourai's 'daěv, daěvoh' is his own transcription (ě = ē/ae) of the stem and the nominative. The semantic history the chart states is the standard one and is exactly Bartholomae's: in the Gathas daēva- still designates 'the gods of the religion current in Iran before Zaraθuštra', while in the Younger Avesta it means 'Dämon, Unhold, Teufel'; the Zoroastrian reform, which set Ahura Mazdā above all, demoted the old *daiva- gods to demons, and the same demotion is public policy in Old Persian, where Xerxes' daiva-inscription (XPh) boasts of destroying the daivadāna 'house of the daivas'. Iranian is the only IE branch in which the word turned negative — Indic devá-, Latin deus, Lith. diẽvas all stayed 'god'.\",\n          \"derivation_fa\": \"از هندواروپایی آغازین *deiwós «ایزد، آسمانی» به هندوایرانی آغازین *daivás و ایرانی باستان *daivah و از آنجا به اوستایی daēva- (نهادی daēvō) رسیده است؛ نگارشِ «daěv, daěvoh» شیوهٔ خودِ نورایی برای نمایش ā/ē است. آنچه در کادر آمده همان تحلیل بارتولومه است: در گاهان daēva- هنوز نامِ خدایانِ دین پیش از زرتشت است و در اوستای متأخر معنای «دیو، اهریمن» می‌یابد؛ با اصلاح دینی زرتشت و برنشاندن اهورامزدا، خدایان کهن به دیوان فروکاسته شدند و همین سیاست در سنگ‌نبشتهٔ دیوِ خشایارشا (پارسی باستان daiva-، daivadāna «دیوکده») نیز دیده می‌شود. در هیچ شاخهٔ دیگر هندواروپایی این معنای منفی پدید نیامد: سنسکریت devá-، لاتین deus و لیتوانیایی diẽvas همچنان «خدا» مانده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\",\n            \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:185\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 196 (printed 185/186): 'o-St. deiuo-s ,Gott, Himmlischer': ai. devá-h ,Gott' (devī ,Göttin'), av. daeva- ,Dämon'' — the arrow root → Avestan daēva- is on precisely the page cited.\"},\n            {\"ref\": \"AHD:1511\", \"status\": \"partial\", \"note\": \"The New College Edition p.1511 is not on disk; the 1985 Watkins standalone edition of the same appendix (AHD_watkins1985.txt s.v. deiw-) has 'Noun *deiwos, god … 6. Sanskrit devah, god' but does NOT cite Avestan daēva-. Watkins therefore supports the root and the Indo-Iranian noun, not the Avestan form specifically.\"},\n            {\"ref\": \"BQT:917\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 377 (= printed p.917; the leaf/page offset is fixed by the 'بقیه در صفحهٔ ۹۰۸' catch-lines), footnote 1 to the headword دیو: 'پهلوی dēv … اوستا daēva (دیو). هندی باستان devá (خدا) «اشتقاق ۵۹۸». این کلمه در قدیم به گروهی از پروردگاران آریایی اطلاق می‌شده ولی پس از ظهور زرتشت و معرفی «اهورامزدا» پروردگاران عهد قدیم با دیوان، گمراه‌کنندگان و شیاطین خوانده شدند، ولی کلمهٔ «دیو» نزد همهٔ اقوام هند و اروپایی — باستثنای ایرانیان — معنی اصلی خود را محفوظ داشته است' — Mo'in's footnote is word for word the sentence Nourai puts in the box.\"},\n            {\"ref\": \"SNB:126\", \"status\": \"not_checked\", \"note\": \"SNB = H. Kowsar, سنگ‌نبشته‌ها سخن می‌گویند; refs_online.json records kind 'none' — not digitised on any accessible platform, so p.126 could not be seen.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. ¹daēva- m. (BRT.txt l. 12459)\", \"stance\": \"supports\", \"note\": \"Bartholomae: '¹daēva- m., j. ¹daēvī- f. 1) im gAw. Bezeichnung f. die Gottheiten der vor Zaraθuštra in Iran geltenden Religion … 2) im jAw. \\\"Dämon, Unhold, Teufel\\\"', with the footnote (l. 12473) that the priests and adherents of the old belief, which used daēva- for 'god', naturally opposed the reform.\"},\n            {\"src\": \"KNT\", \"where\": \"§ on OP d < PIE d (KNT.txt l. 1060) and XPh (l. 3368, 4592)\", \"stance\": \"supports\", \"note\": \"Kent: 'pIE *deiwo- \\\"deity\\\", OP daiva- \\\"(evil) god\\\", Av. …'; the Daiva Inscription of Xerxes (XPh) line 37 'adam avam daivadāna(m)' shows the demoted sense already in Achaemenid Old Persian.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dieus (IEC.txt l. 2322)\", \"stance\": \"supports\", \"note\": \"Mann lists 'Av. … daevo \\\"demon\\\"' beside 'Skt. deváh' under the same lemma.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"dîv «دیو»; dîvâneh «دیوانه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan daēva- 'demon' > Middle Persian dēw (written with the Aramaic ideogram ŠDYA, from Aramaic šēdā 'demon', pl. šydy') > New Persian dīv «دیو»; the Middle Persian majhūl ē regularly yields the NP majhūl ē/ī written with ی, hence dēv ~ dīv. From it MP dēwānag [dyw'nk] 'demonic, mad' > NP dīvāna «دیوانه» — dīv + the adjectival suffix -āna(g) 'of the kind of', i.e. 'possessed by a dīv' > 'mad'; Mo'in's footnote analyses the ending as -ān + -a, but the MP form dēwānag shows the single suffix -ānag. The Molavī couplet the book quotes ('ما به سلیمان خوشیم، دیو و پری کو مباش') attests the word in the classical language. Both words are inherited, not borrowed.\",\n          \"derivation_fa\": \"اوستایی daēva- «دیو» در فارسی میانه به صورت dēw درآمد (در کتابت پهلوی با هُزوارشِ آرامی ŠDYA از šēdā «دیو» نوشته می‌شد) و ē مجهولِ فارسی میانه در فارسی نو با «ی» نوشته شد: «دیو». «دیوانه» دنبالهٔ فارسی میانهٔ dēwānag «دیوزده، دیوانه» است، یعنی «دیو» + پسوند نسبی ‑ānag «از گونهٔ ...»؛ معین در حاشیهٔ برهان آن را «دیو + ان (جمع) + هٔ نسبت» تحلیل کرده، اما صورتِ پهلوی dēwānag نشان می‌دهد که پسوند یکی است. تحول معنایی «دیوزده» به «مجنون» همان است که در متون کهن (بیت مولوی در همین کادر) دیده می‌شود. هر دو واژه ارثی‌اند نه وام‌واژه؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:133\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 155 = printed p.133 (the OCR misreads the running head '133' as '138'; the offset leaf = printed + 22 is fixed by leaf 150 = p.128, leaf 151 = p.129), entry '598. dēv \\\"Dämon, Teufel\\\", dēvāne \\\"verrückt\\\" … aw. daēva- \\\"Dämon\\\"; phlv. dēv; ai. devá- \\\"Gott\\\"' — both of Nourai's words, with the same parent, on exactly the page cited.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.26 s.v. dēw, dēwānag (PHD.txt l. 312)\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'dēw [ŠDYA < A šyd', pl. šydy' | N ~] demon, devil' and 'dēwānag [dyw'nk | N ~a] demonic, mad' — the Middle Persian link and the NP outcome are explicit.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 378 = printed p.918, footnote to دیوانه\", \"stance\": \"partial\", \"note\": \"Mo'in: 'دیوانه … از: دیو + ان (جمع) + ه (نسبت) [رک: اشتقاق ۵۹۸ …]؛ گیلکی dīvōna … «مجنون»، «بی‌عقل»' — same parentage, but a segmentation of the suffix that MP dēwānag does not bear out.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'dēv'/'diva'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien has no separate entry for dēv/dīvāne under any spelling I searched (dev, div, diva); he cites Horn's numbers instead.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"dî, dîp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Sanskrit reflexes of the bare verbal root: dī- 'to shine' (3 sg. dí-dē-ti 'scheint, leuchtet', 3 pl. dídyati, part. dīdi- 'shining') and its labial extension dīp- (dīpyate 'flames, radiates, shines', caus. dīpáyati 'kindles, lights up'), from *deiH-/*diH- with the -p- enlargement *diH-p-. Both are listed by Pokorny on the very page Nourai cites, under the head-root dei-, so the arrow root → Sanskrit dī, dīp is drawn correctly; dīp- is a derivative of dī-, not an independent root, and it is dīp- (not dī-) that matters for node #4.\",\n          \"derivation_fa\": \"این گره بازتاب‌های سنسکریتِ خودِ ریشه است: dī- «درخشیدن» (dí-dē-ti «می‌تابد»، dídyati) و گسترشِ لبی آن dīp- (dīpyate «شعله می‌کشد، می‌درخشد»، سببی dīpáyati «برمی‌افروزد»)، از *deiH-/*diH- با افزودهٔ ‑p-. هر دو صورت در همان صفحهٔ ۱۸۳–۱۸۴ پوکورنی زیر ریشهٔ dei- آمده‌اند، پس پیکانِ «ریشه ← سنسکریت» درست کشیده شده است. تنها نکته آنکه dīp- ریشه‌ای مستقل نیست بلکه مشتقِ dī- است، و همین dīp- است که در گرهِ بعدی (دیبا) به کار می‌آید. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:183\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 194 (printed 183/184): 'Ai. dí-dē-ti ,scheint, leuchtet', 3. Pl. dīdyati … su-dī-ti-h ,schönen Glanz habend', Kaus. dīpáyati ,entzündet, erhellt', dīpyate ,flammt, strahlt, scheint' … didi- ,scheinend'' — both of Nourai's Sanskrit forms with the gloss 'to shine'.\"},\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. deiw- cites Sanskrit only for devah/deva- (DEVI, DEODAR, DEVANAGARI); the verbal dī-/dīp- is not in Watkins' appendix, which lists only the English-relevant descendants. It supports the gloss 'to shine' but not this particular Sanskrit pair.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I s.v. dei- (WLD_Bd1_1930_djvu.txt around l. 48700)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny I 772f. has the same Sanskrit material (dídēti, dīpyate) under the head 'dei-, deiə-, dī-, diā- hell glänzen'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dei- / deiuos (IEC.txt ll. 2112-2124, 2322)\", \"stance\": \"partial\", \"note\": \"Mann builds his lemmas on the nominal *deiuos/*dieus and cites 'Skt. deváh', not the verb dī-/dīp-; he neither supports nor contradicts the verbal node.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"děpâk, děbâg\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"MP dēbāg [dyp'k] 'brocade' is well attested (MacKenzie p.26 'dēbāg [dyp'k | N dēbā] brocade'; it occurs at Šāyast nē-šāyast 4,1, the very text whose glossary Nourai cites as SNS). Its derivation from the 'shine' root is Horn's (no. 591): 'ai. √dīp-, dīpyate \\\"flammen, strahlen, glänzen\\\"; phlv. dēpāk … Die Etymologie ist nicht sicher, da im Sanskrit nur Formen mit ī, nie solche mit ē vorkommen' — i.e. the Sanskrit comparandum has ī where Pahlavi has ē, which is exactly why the chart's own NOTE says BQT is not certain. Two further corrections to the arrow as drawn: (a) MP dēbāg is not descended from Sanskrit but is an inherited Iranian formation from the same root, Proto-Iranian *diHp- 'to shine' (so Wiktionary: 'probably a derivative of Proto-Iranian *diHp- \\\"to shine, light up\\\", due to the sheen imparted by the gold and silver'), so the parent–child arrow really marks a cognate relation; (b) a rival etymology, preferred by Asbaghi and reported by Mo'in himself, takes dēpāk to the OP dipi- 'writing, inscription' family (ultimately Sumerian dub / Akkadian ṭuppu), whence 'figured, embroidered stuff' — cf. Arabic dabbaǧa 'to paint with figures, embroider' and MP dibīr 'scribe', dēwān. The Pahlavi form and gloss are right; the parentage is 'accepted by some, doubted by others', hence plausible.\",\n          \"derivation_fa\": \"صورتِ فارسی میانهٔ dēbāg (نگارش pahlavi: dyp'k) به معنی «پارچهٔ زربفت، دیبا» به‌خوبی گواهی شده است (مکنزی، ص ۲۶؛ و در متنِ شایست نه‌شایست ۴/۱ به کار رفته که واژه‌نامه‌اش همان SNS مورد استنادِ نورایی است). پیوند آن با ریشهٔ «درخشیدن» از آنِ هرن است (شمارهٔ ۵۹۱): «سنسکریت √dīp-، dīpyate «شعله کشیدن، درخشیدن»؛ پهلوی dēpāk … این اشتقاق قطعی نیست، زیرا در سنسکریت تنها صورت‌های با ī هست و هرگز با ē» — و همین نکته است که یادداشتِ خودِ نمودار («برهان قاطع در این اشتقاق مطمئن نیست») بدان اشاره دارد. دو تصحیح بر پیکان: نخست آنکه dēbāg وام‌واژه‌ای از سنسکریت نیست بلکه ساختی ارثی از ایرانی آغازین *diHp- است، پس رابطهٔ این دو هم‌ریشگی است نه فرزندی؛ دوم آنکه اصباغی و نیز حاشیهٔ معین اشتقاقِ رقیبی را می‌آورند که dēpāk را به خانوادهٔ dipi- «نوشته» در پارسی باستان (و سرانجام dub سومری و ṭuppu اکدی) می‌برد، یعنی «پارچهٔ نقش‌دار»؛ مقایسه کنید با عربی دبّج «نقش زدن» و پهلوی dibīr «دبیر» و dēwān. صورت و معنای پهلوی درست است اما نسبِ آن با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:908\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 368 = printed p.908 (fixed by the catch-lines 'بقیه در صفحهٔ ۹۰۸' on leaf 367 and 'بقیه از صفحهٔ ۹۰۷' on leaf 368), footnote to دیبا: 'پهلوی dēpāk «تاوادیا ۹۱۰»، از هندی باستان dīp-, dīpayati (زبانه کشیدن، پرتو افکندن، درخشیدن) … «اشتقاق ۵۹۱» … اگرچه اشتقاق آن قطعی نیست' and, in the same note, the rival route 'وآن را از ریشهٔ … سومری (لوحه، خط) و اکدی … گرفته‌اند «فاب ۱ ص ۲۱۱»، رک: دستان، دبیر' — Mo'in gives Nourai's chain AND the uncertainty the chart's NOTE reports.\"},\n            {\"ref\": \"SNS:313\", \"status\": \"supports\", \"note\": \"SNS_pages.txt, the Sanskrit index of Tavoosi's glossary (l. 14893) has 'dīpyate, 313/10' (beside 'distay- 313/13'), i.e. glossary page 313 line 10 adduces Skt dīpyate — the comparandum for dēpāk, which occurs at Šāyast nē-šāyast 4,1 (Horn no. 591). The body of p.313 itself is not legible in the OCR (the Persian layer of this scan is largely noise), so the index entry is the evidence.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p.26 s.v. dēbāg (PHD.txt l. 312; English side l. 1099 'brocade dēbāg')\", \"stance\": \"supports\", \"note\": \"'dēbāg [dyp'k | N dēbā] brocade' — MacKenzie confirms both Pahlavi spellings Nourai prints (dēpāk = the transliteration dyp'k, dēbāg = the transcription) and the NP outcome, without committing to an etymology.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 591, printed p.132 (HRN.txt leaf 154)\", \"stance\": \"partial\", \"note\": \"Horn supplies the etymology Nourai draws but flags it: 'Die Etymologie ist nicht sicher, da im Sanskrit nur Formen mit ī, nie solche mit ē vorkommen'; he also gives 'phlv. dēpāk (Šāy. nē-šāy. 4,1), arm. LW. dipak, syr. LW.'\"},\n            {\"src\": \"PLA\", \"where\": \"p.129 s.v. dībāǧ (PLA_asbaghi_1988_ia_djvu.txt l. 9904)\", \"stance\": \"contradicts\", \"note\": \"Asbaghi: 'dībāǧ … aus pers. dībā < Mp. dēpāk, ap. dipi …, syr. …, mand. dibag' — he refers the Middle Persian word to Old Persian dipi- 'inscription, writing', not to the 'shine' root.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II glossary s.v. dīvān (NYB_vol2_glossary.txt l. 1300)\", \"stance\": \"partial\", \"note\": \"Nyberg: 'dīvān [dyw'n'] the government office … Possibly < *dipi-vahana- \\\"document house\\\", v. dēpivar' — independent evidence that a dip(i)- 'writing' family was alive in Middle Persian, which is what makes Asbaghi's rival etymology of dēpāk possible.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"dîbâ «دیبا» (extra: دیبه ، دیباج)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP dēbāg > NP dībā «دیبا» 'figured silk, brocade': the Middle Persian final -g of the suffix -āg was lost in New Persian (as in MP xānag > NP xāna, MP asprēs > …), and MP ē is written ی, so dēbāg > dēbā/dībā; the variant دیبه (dība/dībe) preserves the same stem with the -a ending, and دیباچه 'preface' is dībā + the diminutive -če, literally 'little brocade' = the ornamented opening of a book. دیباج is the Arabicised form travelling back into Persian: Arabic dībāǧ is an early loan from Persian dībā (Addi Shir: '(الديباج) معرب ديبا وهو الثوب الذي سداه … حرير'; Asbaghi p.129 'dībāǧ … pers., aus pers. dībā'), so the printed دیباج in the box is a Persian→Arabic→Persian round trip, not a separate word. The chart's cross-reference 'See root \\\"Zay\\\" for another possible derivation' is Nourai's own acknowledgement of the rival etymology discussed at node #4. The Ferdowsī hemistich in the box ('همان گوهر و دیبه و تخت و تاج') attests دیبه in the Šāhnāma. The step Pahlavi → Persian itself is beyond doubt; only the step above it (node #4) is uncertain.\",\n          \"derivation_fa\": \"«دیبا» دنبالهٔ مستقیم فارسی میانهٔ dēbāg است: گافِ پایانیِ پسوند ‑āg در فارسی نو افتاده (مانند xānag > خانه) و ē مجهول با «ی» نوشته شده، پس dēbāg > دیبا. گونهٔ «دیبه» همان ستاک با پایانهٔ ‑ه است و «دیباچه» از دیبا + ‑چه (تصغیر) یعنی «دیبای کوچک»، کنایه از آغازِ آراستهٔ کتاب. «دیباج» معرّبِ همین «دیبا» است که دوباره از عربی به فارسی بازگشته است (ادّی‌شیر: «الدیباج معرّب دیبا»؛ اصباغی ص ۱۲۹)، پس در کادر با یک وام‌گیریِ رفت‌وبرگشتی فارسی ← عربی ← فارسی روبه‌روییم. بیتِ فردوسی («همان گوهر و دیبه و تخت و تاج») کاربردِ کهنِ «دیبه» را گواهی می‌کند. خودِ گامِ پهلوی ← فارسی تردیدناپذیر است و تنها گامِ بالاتر (گرهٔ ۴) جای بحث دارد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:908\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 368 = printed p.908: headword 'دیبا * = بروزن زیبا، قماشی باشد از حریر الوان' with Mo'in's footnote 'پهلوی dēpāk … در فارسی = دیباه، دیبه؛ و دیباچه و دیوان نیز از همین ریشه است، معرب آن دیباج است' — the headword, the gloss 'a colorful cloth', and the extras دیبه/دیباج are all on the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 591, printed p.132\", \"stance\": \"supports\", \"note\": \"'591. dēbā, dēbah \\\"Brokat\\\", arab. dībāǧ; dēbāče \\\"Vorrede\\\"' — Horn has the NP word, the variant دیبه, the Arabic loan and دیباچه in one line.\"},\n            {\"src\": \"PHD\", \"where\": \"p.26 s.v. dēbāg\", \"stance\": \"supports\", \"note\": \"MacKenzie's bracket '| N dēbā' states the Middle → New Persian descent that this arrow draws.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, s.v. الديباج (AFM.txt l. 2497)\", \"stance\": \"supports\", \"note\": \"'(الديباج) معرب ديبا وهو الثوب الذي سداه … حرير' — Arabic dībāj is Arabicised Persian dībā, confirming the direction of the loan behind the printed extra دیباج.\"},\n            {\"src\": \"PLA\", \"where\": \"p.129 s.v. dībā / dībāǧ\", \"stance\": \"partial\", \"note\": \"Asbaghi confirms 'aus pers. dībā < Mp. dēpāk' for the Persian → Arabic loan, but refers dēpāk itself to OP dipi- rather than to the 'shine' root.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"deus; diěs; jovis, jŭlius\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three Latin items belong to the same paradigm-split described by Pokorny p.185: Old Latin deiuos (epigraphically attested) yields both deus 'god' (< *deiuos > *deos) and dīvus 'divine' (< gen. *deiuī); the diphthong stem *dyeu-/*dyew- gives the name of the sky god — voc. *dyeu-pəter = Iuppiter (Umbrian Iupater, Greek Zeû páter, Skt. dyáuṣ pitā́), gen. Iovis, whence the gentilicium Iūlius < *Iouilios 'descended from Jupiter'; and the ē-grade *dyē- gives diēs 'day' (nom. dies remade after acc. diem). Two notes on the printed forms: Nourai's breves are his own vowel marks — Latin has diēs and Iūlius with long vowels (the extraction is faithful; the printed page really shows 'diěs' and 'jŭlius') — and 'jovis' is the genitive of Iuppiter, not a nominative, so the gloss 'from Jupiter' fits Iūlius but describes Iovis loosely.\",\n          \"derivation_fa\": \"هر سه واژهٔ لاتینی از یک ساختِ صرفیِ دوپاره‌شده‌اند که پوکورنی در ص ۱۸۵ شرح داده است: لاتینِ کهن deiuos هم deus «خدا» می‌دهد و هم dīvus «ایزدی»؛ ستاکِ دوواکه‌ای *dyew- نامِ ایزدِ آسمان را می‌سازد — ندایی *dyeu-pəter یعنی Iuppiter (اومبریایی Iupater، یونانی Zeû páter، سنسکریت dyáuṣ pitā́)، اضافیِ Iovis، و از آنجا نامِ خاندانِ Iūlius از *Iouilios «از تبار ژوپیتر»؛ و درجهٔ ē یعنی *dyē- واژهٔ diēs «روز» را می‌دهد. دو نکته دربارهٔ صورت‌های چاپی: علامت‌های کوتاهِ روی مصوت از آنِ خودِ نورایی است و در لاتین diēs و Iūlius با مصوتِ بلند درست است (خطای خوانشِ اسکن نیست؛ در صفحهٔ چاپی نیز «diěs» و «jŭlius» آمده)، و jovis صورتِ اضافیِ Iuppiter است نه نهادی، پس توضیحِ «from Jupiter» بیشتر برازندهٔ Iūlius است. در کل ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/journal\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deiw-: 'I.2. Latin deus, god … 3. Latin divus … II. Variant *dyeu-, Jove … 1. Latin Jovis, Jupiter … 2. Derivative *jou-il- in Latin Jūlius, \\\"descended from Jupiter\\\" (name of a Roman gens): JULY. 3. Vocative compound *dyeu-poter- … Juppiter … III. Variant *dyē- (< *dyeə-) in Latin diēs, day' — every Latin word in the box, with the same relations.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. deus (LAT.txt l. 16405) and s.v. dies (l. 16753)\", \"stance\": \"supports\", \"note\": \"'deus, -ī m. (ancien deiuos attesté épigraphiquement), dea (deiua…)' and 'dies, -ei … jour; espace d'une journée … comme on le voit dans Dies-piter' — the Old Latin deiuos and the Diespiter/Iuppiter connection are explicit.\"},\n            {\"src\": \"POK\", \"where\": \"printed p.185 (POK_01.txt leaf 195)\", \"stance\": \"supports\", \"note\": \"'lat. Iuppiter aus Iū-piter, umbr. Iupater Vok. = Zeῦ πάτερ … lat. Gen. Iouis … vgl. GentilN lat. Iūlius (*Iouilios); lat. Diespiter … dies … in der Bed. \\\"Tag\\\" sonst herrschend wurde'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. deity (KLN_1971.txt l. 66658ff.)\", \"stance\": \"supports\", \"note\": \"'fr. L. deus, \\\"god\\\", fr. OL. deivos (whence also L. divus) … L. Diespiter, Jupiter'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"journal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin diēs > adj. diurnus 'of the day' > Late Latin diurnālis 'daily'; with the regular Gallo-Romance loss of intervocalic material and the treatment di- > /dʒ/ > /ʒ/, diurnālis gave Old French jornal, jurnal 'daily' (and diurnum > OF jorn, jour 'day'). The adjective was substantivised, first as 'a day's work / a day's measure of land', then in the 17th century as 'daily register, day-book' and 'daily paper' — the modern French journal (Théophraste Renaudot's Gazette, 1631, and the Journal des sçavans, 1665, fix the press sense). Etymonline states the chain: 'noun use of adjective meaning \\\"daily, of the day\\\", from Late Latin diurnalis \\\"daily\\\", from Latin dies \\\"day\\\" … from PIE root *dyeu- \\\"to shine\\\"'.\",\n          \"derivation_fa\": \"لاتین diēs صفتِ diurnus «روزانه» را ساخت و از آن لاتینِ متأخر diurnālis پدید آمد؛ در گذر به فرانسویِ کهن، ‑di‑ آغازین نخست به /dʒ/ و سپس به /ʒ/ بدل شد و diurnālis صورتِ jornal / jurnal «روزانه» را داد (چنان‌که diurnum به jorn و jour «روز» رسید). این صفت اسم شد: نخست «کارِ یک روز، مساحتِ یک‌روزه»، سپس در سدهٔ هفدهم «دفترِ روزانه» و «روزنامه» (گازتِ رنودو ۱۶۳۱ و Journal des sçavans ۱۶۶۵ این معنا را تثبیت کردند). زنجیرهٔ لاتین ← فرانسه در اتیمانلاین و کلاین بی‌هیچ اختلافی آمده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/journal\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:707\", \"status\": \"partial\", \"note\": \"Only the Watkins appendix is on disk, not the New College main dictionary where p.707 (the 'journal' entry) stands; the appendix s.v. deiw- III does list '(JOURNAL)' among the descendants of Latin diēs > Late Latin diurnum, which is the claim of this arrow, but the cited page itself could not be read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. journal adj./n. (KLN_1971.txt l. 129452ff.)\", \"stance\": \"supports\", \"note\": \"'journal, adj., daily (archaic). — ME., fr. OF. jornal, jurnal, journal (F. journal), \\\"daily\\\", fr. L. diurnalis, \\\"diurnal\\\", fr. diurnus, \\\"daily\\\"' and 'journal, n. — F., lit. \\\"a daily paper\\\", fr. OF. jornal'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'journal'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise edition on disk gives no separate journal entry in the OCR; nothing for or against.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"žornâl «ژورنال»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A modern French loan, taken into Persian in the Qajar period along with the European press vocabulary (گازت، تلگراف، ژورنال). French journal /ʒuʁnal/ is rendered with Persian ژ for /ʒ/ — the letter Persian reserves for this foreign sound — and the French nasal-free -al is kept, giving ژورنال žornāl. Mo'in tags it '[فر.]' (= فرانسه) and glosses it '۱ - روزنامه. ۲ - مجلهٔ مخصوص مد لباس'; Dehkhoda likewise 'ژورنال. (فرانسوی، اِ) روزنامه' and notes the Persian narrowing to fashion magazines used by tailors. The arrow French → Persian is correct and direct (not via Turkish or Russian, for which the form would be žurnal).\",\n          \"derivation_fa\": \"وام‌واژه‌ای نو از فرانسه است که در دورهٔ قاجار همراه با واژگانِ مطبوعات (گازت، تلگراف، ژورنال) به فارسی درآمد. آوای /ʒ/ فرانسوی با حرفِ «ژ» نوشته شده — همان حرفی که فارسی برای این آوا نگاه داشته است — و پایانهٔ ‑al دست‌نخورده مانده: journal > ژورنال. معین آن را با نشانِ «[فر.]» می‌آورد و چنین معنی می‌کند: «۱ ‑ روزنامه. ۲ ‑ مجلهٔ مخصوص مد لباس»؛ دهخدا نیز «ژورنال. (فرانسوی، اِ) روزنامه» و تخصیصِ فارسیِ آن به مجله‌های مدِ لباس را یاد می‌کند. پس پیکانِ فرانسه ← فارسی درست و بی‌واسطه است (نه از راه ترکی یا روسی که در آن صورت žurnal می‌شد).\",\n          \"sources\": [\"https://abadis.ir/fatofa/%DA%98%D9%88%D8%B1%D9%86%D8%A7%D9%84/\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1778\", \"status\": \"supports\", \"note\": \"Mo'in's entry, read through abadis.ir (the print volumes' page numbers cannot be mapped online, so the page 1778 itself is unverified): 'ژورنال (ژُ) [فر.] (اِ.) ۱ - روزنامه. ۲ - مجلهٔ مخصوصِ مُد لباس' — the French origin Nourai's arrow claims is Mo'in's own bracketed tag.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab/abadis, s.v. ژورنال\", \"stance\": \"supports\", \"note\": \"'[فر.]' = French; gloss 'روزنامه'.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2/v3 (ژ section)\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (1062/1652) predates the loan by two centuries and has no such entry; silence here is expected and not evidence against.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt, grep ژورنال\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian does not treat modern European loanwords; no entry found.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"journal\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English journal is borrowed from French, in two layers: the adjective first (Middle English, mid-14th c., from Anglo-French jurnal / Old French jornal 'daily', e.g. 'journal hours'), then the noun 'day's record, diary' (15th c.) and finally 'daily newspaper, periodical' (17th c.) on the model of French journal. So the chart's French → English arrow is right; Klein makes journal a doublet of diurnal, both from Latin diurnus.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی journal وام‌گرفته از فرانسه است، در دو لایه: نخست صفت (انگلیسیِ میانه، میانهٔ سدهٔ چهاردهم، از آنگلونورمنِ jurnal و فرانسویِ کهن jornal «روزانه»)، سپس اسمِ «دفترِ روزانه، یادداشتِ روزانه» در سدهٔ پانزدهم و سرانجام «روزنامه، نشریهٔ ادواری» در سدهٔ هفدهم به پیرویِ فرانسه. پس پیکانِ فرانسه ← انگلیسی درست کشیده شده است. کلاین journal را دوگانهٔ (doublet) diurnal می‌شمارد که هر دو از diurnus لاتین‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/journal\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:707\", \"status\": \"partial\", \"note\": \"Same as node #7: the New College page 707 is not on disk; the Watkins appendix s.v. deiw- III lists '(JOURNAL)' under Latin diēs, supporting the ancestry but not the cited page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. journal, adj. and n. (KLN_1971.txt l. 129452ff.)\", \"stance\": \"supports\", \"note\": \"'journal, adj. … — ME., fr. OF. jornal … See diurnal, which is a doublet of journal'; 'journal, n. — F., lit. \\\"a daily paper\\\"'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dieus (IEC.txt l. 2322)\", \"stance\": \"silent\", \"note\": \"Mann's comparative entry stops at the ancient languages and lists no Romance or English derivatives.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"deity, divine, dial, diary, journey, Jupiter, July, Julian, Julius\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All nine are Latin-derived and all nine are listed by Watkins under deiw-. deity < OF deité < Late Latin deitās (coined by Augustine after Greek theótēs) < deus; divine < OF divin < Latin dīvīnus < dīvus; dial < Medieval Latin diālis 'daily' (rota diālis, the sun-dial's daily wheel) < diēs; diary < Latin diārium 'daily allowance, journal' < diēs; journey < OF jornee < Vulgar Latin *diurnāta 'a day's work / a day's travel' < diurnus; Jupiter < Latin Iuppiter < voc. *dyeu-pəter; Julius / Julian < the gens name Iūlius (< *Iouilios) and its adjective Iūliānus; July < Latin (mēnsis) Iūlius, the month renamed in 44 BCE for Gaius Iulius Caesar, through OF julie/juil into ME. Each word is a learned or Old-French-mediated Latinism, not a native English form, so the chart's Latin → English arrow is right.\",\n          \"derivation_fa\": \"هر نُه واژه لاتینی‌تبارند و همگی در پیوستِ واتکینز زیر deiw- آمده‌اند. deity از فرانسویِ کهن deité از لاتینِ متأخر deitās (ساختهٔ آگوستین به قیاسِ theótēs یونانی) از deus؛ divine از dīvīnus لاتین از dīvus؛ dial از لاتینِ میانه diālis «روزانه» (rota diālis، چرخِ روزانهٔ ساعتِ آفتابی) از diēs؛ diary از diārium «جیرهٔ روزانه، روزنگار»؛ journey از فرانسویِ کهن jornee از لاتینِ عامیانه *diurnāta «کارِ یک روز، سفرِ یک‌روزه»؛ Jupiter از Iuppiter؛ Julius و Julian از نامِ خاندانِ Iūlius (از *Iouilios) و صفتِ Iūliānus؛ و July از (mēnsis) Iūlius، ماهی که در سال ۴۴ پیش از میلاد به نامِ ژولیوس سزار نامیده شد و از راهِ فرانسویِ کهن به انگلیسی رسید. همهٔ این‌ها وام‌واژه‌های عالمانه یا فرانسوی‌واسطه‌اند نه صورت‌های بومیِ ژرمنی؛ پس پیکانِ لاتین ← انگلیسی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/journal\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deiw- lists, in order, DEISM/DEITY (Latin deus), DIVINE (Latin divus), JUPITER, JULY (*jou-il- > Jūlius), and under III 'Latin diēs … DIAL, DIARY … DIURNAL; ADJOURN, … (JOURNAL), (JOURNEY)'. The reverse index confirms it word by word: 'DEITY deiw-', 'DIAL deiw-', 'DIARY deiw-', 'JOURNEY deiw-', 'JUPITER deiw-', 'JULY deiw-'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. deity, journey (KLN_1971.txt ll. 66658, 129465ff.)\", \"stance\": \"supports\", \"note\": \"'deity, n. — ME. deite, fr. OF. deite … fr. Late L. deitatem … which was coined by Augustine on analogy of Gk. θεότης … fr. L. deus'; 'journey, n. — OF. jornee … fr. VL. *diurnata, \\\"day, day's work\\\", fr. L. diurnus'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. deiuinos, dieus (IEC.txt ll. 2122, 2322)\", \"stance\": \"supports\", \"note\": \"Mann: 'deiuinos \\\"god-like, inspired\\\" … Lat. divinus' — the base of English divine.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Germanic\",\n          \"words\": \"tiwaz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *Tīwaz < PIE *deiwós, with the regular Grimm shift *d > *t and *ei > *ī; the plural of the same noun survives as ON tívar 'gods' (< *deiwōs). The singular became the name of the individual god: ON Týr, OE Tīw (gen. Tīwes), OHG Zio/Ziu. Pokorny p.186 gives 'anord. tívar Pl. \\\"Götter\\\" (*deiuōs) sowie anord. Týr (agerm. teiwaz) \\\"der Kriegsgott\\\", ags. Tīg, Gen. Tiwes \\\"Mars\\\", ahd. Zio, Zio'. One nuance on Nourai's gloss 'god of sky': by the time the Germanic god is attested he is the war god equated with Mars (whence the interpretatio Romana behind Tuesday = dies Martis); 'sky god' is his reconstructed prehistoric role, not his attested one — Watkins hedges it as 'god of war and sky'.\",\n          \"derivation_fa\": \"ژرمنی آغازین *Tīwaz از هندواروپایی *deiwós است، با دو دگرگونیِ منظم: *d ژرمنی بر پایهٔ قانون گریم به *t بدل شده و *ei به *ī کشیده تک‌واکه شده است. جمعِ همان اسم در نورسِ کهن به صورت tívar «خدایان» (از *deiwōs) مانده و مفردِ آن نامِ خاصِ ایزد شده است: نورسِ کهن Týr، انگلیسیِ کهن Tīw (اضافی Tīwes)، آلمانیِ علیای کهن Zio/Ziu. پوکورنی در ص ۱۸۶ همین صورت‌ها را می‌آورد. تنها نکته دربارهٔ معنایی که نورایی داده («ایزدِ آسمان») این است که در دورهٔ گواهی‌شده، این ایزد خدای جنگ و همتای مارس رومی است و «ایزدِ آسمان» نقشِ بازسازی‌شدهٔ پیشاتاریخی اوست؛ واتکینز نیز محتاطانه «خدای جنگ و آسمان» می‌نویسد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deiw-: 'I. Noun *deiwos, god. 1. Germanic *Tīwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: TIU, (TUESDAY); b. Old Norse Tyr, sky god: TYR.' — Nourai's node, spelling and gloss come straight from here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"printed p.186 (POK_01.txt leaf 196)\", \"stance\": \"supports\", \"note\": \"'anord. tívar Pl. „Götter\\\" (*deiuōs) sowie anord. Týr (agerm. teiwaz) „der Kriegsgott\\\", ags. Tīg, Gen. Tiwes „Mars\\\", ahd. Zio, Zio'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dieus (IEC.txt l. 2322)\", \"stance\": \"supports\", \"note\": \"Mann: 'Runic Go. tyz; OE Tiw \\\"Mars\\\"; ON Tyr, pl. tívar; OHG cf. Zios-tac \\\"Tuesday\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. deity / Tuesday\", \"stance\": \"supports\", \"note\": \"Klein: 'OHG. Zio, Ziu, ON. Tyr, OE. Tiw, name of the Teutonic war god' in the same cognate list as L. deus and Gk. Zeús.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"Tuesday\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English Tīwesdæg 'day of Tīw', gen. sg. Tīwes + dæg — a calque of Latin diēs Martis made when the Roman week was adopted in the Germanic world (the interpretatio germanica of the 3rd–4th c.), Tīw being equated with Mars. ME Tiwesdai / Twisdai / Tuesdai > Tuesday; the modern spelling with -ue- reflects the Middle English rounding of /iu/ and the influence of French orthography. The parallel calques ON týsdagr, OFris. tiesdei, OHG Ziostag confirm the pattern. The node carries no reference in the book, but the derivation is standard.\",\n          \"derivation_fa\": \"از انگلیسیِ کهن Tīwesdæg «روزِ تیو»، یعنی اضافیِ Tīwes به‌علاوهٔ dæg «روز» — گرته‌برداری از diēs Martis لاتین، از زمانی که هفتهٔ رومی در جهان ژرمنی پذیرفته شد (سدهٔ سوم و چهارم میلادی) و تیو با مارس برابر نهاده شد. صورتِ انگلیسیِ میانه Tiwesdai / Twisdai بود و املای امروزی با ‑ue‑ بازتابِ گردشدنِ /iu/ در انگلیسیِ میانه و تأثیرِ املای فرانسوی است. همین گرته‌برداری در نورسِ کهن týsdagr، فریزیِ کهن tiesdei و آلمانیِ علیای کهن Ziostag دیده می‌شود. این گره در کتاب بی‌ارجاع است، اما اشتقاق آن استاندارد و پذیرفته است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (the printed box has no reference icon), so there is nothing of Nourai's to check; the parent node #11 cites AHD, which does list TUESDAY under deiw-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Tuesday (KLN_1971.txt l. 254936)\", \"stance\": \"supports\", \"note\": \"'Tuesday, n. — ME. Tiwesdai, Twisdai, Tuesdai, fr. OE. Tiwesdæg (\\\"day of Tiw\\\"). Tiw is an ancient Teutonic war god, identified with the Roman Mars … ON. Tyrsdagr, Tysdagr (Dan. Tirsdag), OFris. ties-dei, OHG. Ziostag … lit. \\\"the day of Tyr\\\", resp. \\\"the day of Ziu\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deiw- and reverse index 'TUESDAY deiw-'\", \"stance\": \"supports\", \"note\": \"Watkins puts TUESDAY under Germanic *Tīwaz > Old English Tiw.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dieus (IEC.txt l. 2322)\", \"stance\": \"supports\", \"note\": \"'OHG cf. Zios-tac \\\"Tuesday\\\": OE Tiwes-dæg, id.'\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Greek\",\n          \"words\": \"Zeus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek Ζεύς continues the PIE diphthong-stem nominative *dyēus exactly (*dy- > Gk. Z-, as in Skt. dyáuḥ = Ζεύς), with the old paradigm still visible in the oblique cases: acc. Ζῆν < *dyēm, voc. Ζεῦ < *dyeu, gen. Δι(ϝ)ός, dat. Δι(ϝ)ί from the zero-grade *diw-. The vocative compound Ζεῦ πάτερ = Latin Iuppiter = Vedic dyáuṣ pitā́ 'O father Sky' is one of the securest reconstructed IE phrases and shows that the 'ruler of the heavens' gloss Nourai gives is the inherited meaning, not a Greek innovation.\",\n          \"derivation_fa\": \"یونانی Ζεύς دقیقاً دنبالهٔ نهادیِ ستاکِ دوواکه‌ایِ هندواروپایی *dyēus است (خوشهٔ *dy- در یونانی به Z بدل شده، چنان‌که سنسکریت dyáuḥ برابرِ Ζεύς است)، و ساختِ کهنِ صرفی هنوز در حالت‌های دیگر پیداست: رایی Ζῆν از *dyēm، ندایی Ζεῦ از *dyeu، و اضافی Δι(ϝ)ός و برایی Δι(ϝ)ί از درجهٔ صفرِ *diw-. ترکیبِ ندایی Ζεῦ πάτερ برابر با Iuppiter لاتین و dyáuṣ pitā́ ودایی («ای پدرْ آسمان») از استوارترین عبارت‌های بازسازی‌شدهٔ هندواروپایی است و نشان می‌دهد معنای «فرمانروای آسمان‌ها» که نورایی آورده همان معنای ارثی است نه نوآوریِ یونانی. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deiw- II.4: 'Greek Zeus, Zeus: ZEUS; (Dioscuri)' under 'Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pantheon'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"printed p.185 (POK_01.txt leaf 195)\", \"stance\": \"supports\", \"note\": \"'gr. Ζεύς (= dyāú-h), Akk. Ζῆν (= dyām), Vok. Ζεῦ (*dyeu), Gen. Δι(ϝ)ός, Dat. (Lok.) Δι(ϝ)ί' — the full paradigm equation with Sanskrit.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Zeus (KLN_1971.txt l. 270572)\", \"stance\": \"supports\", \"note\": \"'Zeus, n., the supreme god of the ancient Greeks. — Gk. Ζεύς [gen. Διός], cogn. with the first element in L. Diespiter, Jupiter. See deity'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. dieus (IEC.txt l. 2322)\", \"stance\": \"supports\", \"note\": \"'Gk. Zeüs' listed beside 'Skt. dyáuh' under dieus.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"Zeus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Zeus is a learned borrowing of Greek Ζεύς, taken over unchanged (through Latin Zeus) in the Renaissance revival of classical mythology; it is a proper name, not an inherited word, and English's own inherited reflex of the same PIE noun is Tiw/Tuesday (node #12). The chart's Greek → English arrow therefore marks a straightforward literary borrowing.\",\n          \"derivation_fa\": \"«Zeus» در انگلیسی وام‌واژه‌ای عالمانه از یونانی Ζεύς است که در دورهٔ رنسانس و با احیای اساطیر کلاسیک، از راهِ لاتین و بی‌هیچ دگرگونی وارد شده است؛ نامی خاص است و نه واژه‌ای ارثی. بازتابِ ارثیِ همین اسمِ هندواروپایی در خودِ انگلیسی Tiw و Tuesday است (گرهٔ ۱۲). پس پیکانِ یونانی ← انگلیسی در این کادر صرفاً یک وام‌گیریِ ادبی را نشان می‌دهد و درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dyew-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. deiw- II.4 gives the English headword ZEUS directly from Greek Zeus; the reverse index has no separate entry because the borrowing is unaltered.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Zeus (KLN_1971.txt l. 270572)\", \"stance\": \"supports\", \"note\": \"Klein enters English Zeus and derives it from 'Gk. Ζεύς', cross-referring to deity for the IE background.\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (Webster's New Twentieth Century), grep 'Zeus'\", \"stance\": \"silent\", \"note\": \"Only volume 1 (A–…) of Webster's is on disk, so the Z entries could not be consulted.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-111.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 111",
 "description": "Write and validate page-111.json"
}
```


### [2026-09-05T17:46:03.080Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 13, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 4, 'not_checked': 2}
books consulted: {'supports': 27, 'partial': 5, 'silent': 6, 'contradicts': 1} | by book: {'KLN': 8, 'IEC': 7, 'PHD': 3, 'POK': 3, 'BQT': 2, 'HRN': 2, 'PLA': 2, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'WLD': 1, 'NYB': 1, 'AFM': 1, 'LAT': 1, 'SKT': 1, 'MON': 1, 'ARY': 1, 'AHD': 1, 'WEB': 1}
```


## [2026-09-05T17:46:12.623Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB dev/div ==\"; grep -n -iE '\\bd[eiē]v[aāe]?\\b|dīv' HUB.txt | head -5; echo \"== SKT journal ==\"; grep -n -i 'journal' SKT.txt | head -3; echo \"== WEB Zeus ==\"; grep -c -i 'Zeus' WEB_vol1.txt; echo \"== BQT ژورنال ==\"; grep -c 'ژورنال' BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null; echo \"== ARY ژورنال ==\"; grep -c 'ژورنال' incoming/ARY/ARY_pages.txt",
 "description": "Verify silent claims"
}
```


### [2026-09-05T17:46:12.742Z] TOOL RESULT

```
== HUB dev/div ==
7033:V. u. = zd. astdvUdtU' *der Dev des Todes, ap. ^astaviSatu- ;
10408:diVa/l 61.
== SKT journal ==
9534:Journal.  Journey ;  see  Diary,
== WEB Zeus ==
33
== BQT ژورنال ==
incoming/BQT/BQT_v3_pages.txt:1
BQT_v2_pages.txt:0
== ARY ژورنال ==
0
```


## [2026-09-05T17:46:23.442Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT Diary ==\"; grep -n -i '^Diary\\|Diary\\.' SKT.txt | head -5; sed -n '9530,9540p' SKT.txt; echo \"== WEB Zeus lines ==\"; grep -n -i 'Zeus' WEB_vol1.txt | head -5; echo \"== BQT v3 zhornal ==\"; grep -n 'ژورنال' incoming/BQT/BQT_v3_pages.txt; echo \"== HUB 10405-10412 ==\"; sed -n '10405,10412p' HUB.txt",
 "description": "Check Skeat, Webster, BQT v3, Hübschmann"
}
```


### [2026-09-05T17:46:23.562Z] TOOL RESULT

```
== SKT Diary ==
367:Adjourn :  see  Diary.
5220:Dium&l ;  see  Diary.
17705:m :  sec  Diary.
Jonquil,  kind  of  narcissiu  ;  see  Junk  ( a).
JordLan,  a  pot.  (L.  -  Gk.  —  Hcb.  ?) M.  £.  iordan  {Jordcm),  Chancer,  C  T. 1 1  i^g.  Short  tot  Jordan^bottU  ;  it  was customary  for  pilgrims  to  bring  home  water from  tlie  river  Jordan,  and  a  Jordan  was orig.  a  bottle,  not  a  pot  (.lUidsley,  Halli- well).  —  I«  lordams.  —  Gk,  *Iopiavi/t.» Ucb.   Variti'n,  i.e.  'llowmg  duwn.*
Jostle ;  see  Joust.
Jot ;  see  Iota.
Journal.  Journey ;  see  Diary,
Jotiflt,  Juat.  to  till.  (F.  — L.^  O.  F. fcujter.  to  UlL  —  Low  L.  iuxfane,  to approach  (hence  to  approach  with  hostile intent,  as  in  tilling). » I..  jMjr/a,  close  to, hard  by  (whence  O.  F.  jomjU,  dose  to). p.  The  form  iuxta  is  short  for  iug-ii'td,  fem. abl.  of  the  superlative  form  of  L.  iu^Ut continual.  From  the  base  tug'  of  iun^ert, toioin.    (VYUG.)
Joetle,  jufitle,  to  push  acainst  (F.  — L.; wi/h  E.  si//fix.)  A  frequent,  form,  with  suffix •/<,  from  M.E^jous/<ri,  to  tilt,  push  against.
Jovial :  see  Deity.
Jowl,  Jole,  the  jaw  or  cbok.  (E) M.  )i.  jolie\  all  the  foims  are  corruptions of  M.  E.  <hei,  chauK  which  is  a  contraction of  M.  E.  thaHcl  y{kavtl\  the  jowl.  — A.  S. ceaft,  the  jaw;  pi.  ctafias,  the  jaws,  chaps. Allied  to  Chaps,  q.  v.  %  The  successive ipellings  are  A.  S.  fra/7,  chafie  (Ijiyamon), MomtJ,  r4«W.  cAoii  joit,  Jorui  ^all  found).
I
JUICE.
== WEB Zeus lines ==
6217:3. at all times; on all occasions; invariably: Am-Al-thaé/a, Am-ăl-thē’å, n. [L.; Gr. Amal- opposed to sometimes; as, he is alwayskindto theia.] in Greek and Roman mythology, the poat that nursed Zeus (Jupiter): one of its
6727:2. in ancient Egypt, a name for Zeus or Jupiter.
6878:Am-phi/én, n. [L.; Gr. Amphion.] in Greek mythology, the son of Zeus and Antiope: with a lyre that Hermes gave him he built a wall around Thebes by charming the stones into place.
6911:Am-phit’ry-6n, n. [L., from Gr. Amphitry6n.]} in Greek mythology, a king of ebes: his wife, Alcmene, became the mother of Her- cules by Zeus, who seduced her by appearing in the likeness of Amphitryon.
14554:Bac’chus, 7. [L.; Gr. Bakchos.] in Greek and Roman mythology, the god of wine and revelry, son of Zeus (Jupiter) and Semele: earlier called Dio- nysus by the Greeks. He is said first to have taught the cultivation of the grape, and the prepara- tion of wine and other in- toxicating liquors.
== BQT v3 zhornal ==
28213:تلم دیگرش را ‎as‏ کفته اند و فردوسی و مژلف مجمل التواريخ ( ژورنال آزباتيك ‎TID‏ ]1 ,
== HUB 10405-10412 ==
dBz 65.
rfiftfr 60.
dih 64, 129.
diVa/l 61.
dirBy 62.
(fivan 60.
(fivar 65.
diz 62.
```


## [2026-09-05T17:46:42.347Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-111.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\n# node 2 HUB\nfor c in nodes[2]['consulted']:\n    if c['src']=='HUB':\n        c['where']=\"HUB.txt, index of Persian words (ll. 10405-10412)\"\n        c['note']=\"Hübschmann's Persische Studien index has dīvān 60, dīvāl 61, dīvār 65, dīz 65 but no entry for dīv or dīvāne; he treats the compound words, not the simplex, and cites Horn's numbers for the rest — silent on this arrow.\"\n\n# node 7 SKT\nfor c in nodes[7]['consulted']:\n    if c['src']=='SKT':\n        c['stance']='supports'\n        c['where']=\"s.v. Journal (SKT.txt l. 9534), cross-referring to Diary\"\n        c['note']=\"Skeat: 'Journal. Journey; see Diary.' — he files both under Diary (< L. diarium < dies), i.e. the same Latin diēs ancestry; cf. 'Diurnal; see Diary' (l. 5220) and 'Adjourn: see Diary' (l. 367).\"\n\n# node 10: add SKT\nnodes[10]['consulted'].append({\n  \"src\":\"SKT\",\"where\":\"s.v. Jovial (SKT.txt l. 9536) and the Diary cross-references (ll. 367, 5220, 9534)\",\n  \"stance\":\"supports\",\n  \"note\":\"Skeat: 'Jovial: see Deity.' and 'Journal. Journey; see Diary.' — he groups exactly Nourai's two families, the deus words under Deity and the diēs words under Diary.\"})\n\n# node 8 BQT note refine\nfor c in nodes[8]['consulted']:\n    if c['src']=='BQT':\n        c['where']=\"BQT_v2_pages.txt and incoming/BQT/BQT_v3_pages.txt (ژ section), grep ژورنال\"\n        c['note']=\"No headword ژورنال in Borhan-e Qate' (compiled 1062/1652, two centuries before the loan). The single occurrence of the string in vol. 3 (l. 28213) is inside a modern editorial footnote citing the periodical «ژورنال آزیاتیک» (Journal Asiatique), not a dictionary entry; silence here is expected and is not evidence against the arrow.\"\n\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nprint('written')\nEOF\npython3 -m json.tool data/verification/page-111.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 111",
 "description": "Patch consulted notes and re-validate"
}
```


### [2026-09-05T17:46:44.496Z] TOOL RESULT

```
written
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 13, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 4, 'not_checked': 2}
books consulted: {'supports': 29, 'partial': 5, 'silent': 5, 'contradicts': 1} | by book: {'KLN': 8, 'IEC': 7, 'PHD': 3, 'POK': 3, 'BQT': 2, 'HRN': 2, 'PLA': 2, 'SKT': 2, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'WLD': 1, 'NYB': 1, 'AFM': 1, 'LAT': 1, 'MON': 1, 'ARY': 1, 'AHD': 1, 'WEB': 1}
```


## [2026-09-05T17:47:01.785Z] AGENT

Page 111 (book p. 81) verified — one entry, root "Dei, Deiw, Dyeu, Dyě", 14 nodes. `verify_check.py 111`: 14/14 nodes, 0 PROBLEM lines.

**Verdicts:** root confirmed; nodes 13 confirmed, 1 plausible, 0 disputed / transcription_suspect.
**Ref checks:** 13 supports, 4 partial, 2 not_checked. **Consulted:** 29 supports, 5 partial, 5 silent, 1 contradicts (18 books).

Notable findings:
- **#4 Pahlavi dēpāk/dēbāg — plausible** (only non-confirmed node). The form and gloss are solid (MacKenzie p.26 "dēbāg [dyp'k | N dēbā] brocade"), but (a) MP dēbāg is not *descended from* Sanskrit — it is an inherited Iranian formation from the same root (PIr *diHp-), so the arrow really marks cognacy; (b) Horn no. 591, whom both Mo'in and Nourai follow, himself warns "die Etymologie ist nicht sicher, da im Sanskrit nur Formen mit ī, nie solche mit ē vorkommen"; (c) Asbaghi (PLA p.129) *contradicts*, taking dēpāk to OP dipi- "writing" (Sumerian dub / Akkadian ṭuppu). The chart's own NOTE and its "see root Zay" cross-reference already flag this.
- Nourai's refs check out unusually well here: BQT:908 and BQT:917 are exactly right pages (I fixed the vol-2 leaf→page offset to leaf+540 using the "بقیه در صفحهٔ ۹۰۸" catch-lines, not the +543 recorded in refs_online.json), HRN:133 = Horn no. 598 (the OCR running head "138" is a misread "133"), SNS:313 is confirmed via the glossary's Sanskrit index entry "dīpyate 313/10".
- Not checkable: SNB:126 (Kowsar, not digitised); AHD:707 and AHD:1511 are New College Edition pages — only the 1985 Watkins appendix is on disk, so both marked partial; MON:1778 content confirmed via abadis (Mo'in "[فر.]"), page number unmappable online.
- **No extraction errors.** I rendered pdf p.111 at 300 dpi and read the Latin box: the book itself prints "diěs" and "jŭlius" with breves (Nourai's own marks; correct Latin is diēs, Iūlius), so the JSON is faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/111.png`.
- 5 web pages archived via fetch_source.py (Wiktionary *dyew-, دیبا, دیو; Etymonline journal; abadis ژورنال) — these plus the PNG are the only untracked files added.
