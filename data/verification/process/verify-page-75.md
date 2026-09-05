# Verification process log — verify-page-75


## [2026-09-05T05:46:12.088Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 75 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-75.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-75.json. Write /home/sfmqrb/git/rishe/data/verification/page-75.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 75` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:46:13.171Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:46:13.979Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:46:13.996Z] TOOL RESULT

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


## [2026-09-05T05:46:14.431Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-75.txt"
}
```


### [2026-09-05T05:46:14.457Z] TOOL RESULT

```
1	=== PDF page 75 (book page 45) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Baba, Barbarah, Balbarah : Baba: baby words for relatives, imitative of indistinct speech. Barbarah, Balbarah: people who speak a non-Aryan language.  (refs OEW:22; AHD:1507)
4	#1 (parent #0) [Greek] refs=OEW:22 | barbitos, barbaros : non-Greek, foreign people or things.
5	  #2 (parent #1) [Pahlavi] refs=BQT:249; MON:497 | barbut : a stringed musical instrument
6	    #3 (parent #2) [Persian] refs=MON:497 | barbat «بربط» : a musical instrument
7	#4 (parent #0) [Latin] refs=AHD | barbaria : foreign country ; barbarus : foreign, rude, wild ; rheu-barbarum : foreign rhubarb ☞Eres 1
8	  #5 (parent #4) [English] refs=OEW:22 | barbarian, barbarous, Barbara, rhubarb
9	#6 (parent #0) [Russian] refs=AHD:100 | balalayka : a musical instrument
10	  #7 (parent #6) [Persian] refs=VOP:84 | bâlâlâykâ «بالالایکا» : a Russian stringed musical instrument
11	  #8 (parent #6) [English] refs=AHD:100 | balalaika
12	#9 (parent #0) [Old French] refs=OEW:22 | babine : hanging lip (not talking properly)
13	  #10 (parent #9) [English] refs=OEW:22 | baboon
14	#11 (parent #0) [Italian] refs=OEW:22 | bambino : originally meant a wild and savage man; later changed to a brave and courageous man.
15	  #12 (parent #11) [French] refs=None | bravo : an expression of approval (for bravery).
16	    #13 (parent #12) [Persian] refs=VOP:87 | brâvo «براوو»
17	  #14 (parent #11) [English] refs=AHD; OEW | brave, bravo
18	#15 (parent #0) [Hindustani] refs=OEW:22 | bâbŭ : old man (baby talk)
19	  #16 (parent #15) [Persian] refs=MON:430 | bâb 3 «باب ۳ ( بابو )» : an old respectful man | extra: بابوالخیر | NOTE: Compare with the Persian word "bâbâ:father". See root "Pa"
20	#17 (parent #0) [Germanic] refs=AHD | 
21	  #18 (parent #17) [English] refs=AHD | baby, babe, babble
22	
```


## [2026-09-05T05:46:17.610Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-75.json",
 "description": "Read source JSON page 75"
}
```


### [2026-09-05T05:46:17.653Z] TOOL RESULT

```
{
  "pdf_page": 75,
  "book_page": 45,
  "entries": [
    {
      "root": {
        "name": "Baba, Barbarah, Balbarah",
        "lang": "Indo-European",
        "refs": "OEW:22; AHD:1507",
        "gloss": "Baba: baby words for relatives, imitative of indistinct speech. Barbarah, Balbarah: people who speak a non-Aryan language.",
        "note": "These words may be related to the root \"Pa: to protect, feed\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "OEW:22",
          "words": [
            {"translit": "barbitos, barbaros", "gloss": "non-Greek, foreign people or things.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:249; MON:497",
          "words": [
            {"translit": "barbut", "gloss": "a stringed musical instrument", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:497",
          "words": [
            {"translit": "barbat", "gloss": "a musical instrument", "script": "بربط"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بدانسان سوخت چون شمعم که بر من - صُراحی گریه و بربط فغان کرد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "barbaria", "gloss": "foreign country", "script": null},
            {"translit": "barbarus", "gloss": "foreign, rude, wild", "script": null},
            {"translit": "rheu-barbarum", "gloss": "foreign rhubarb", "script": null, "see": ["Eres 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "OEW:22",
          "words": [
            {"translit": "barbarian, barbarous, Barbara, rhubarb", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Russian",
          "refs": "AHD:100",
          "words": [
            {"translit": "balalayka", "gloss": "a musical instrument", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:84",
          "words": [
            {"translit": "bâlâlâykâ", "gloss": "a Russian stringed musical instrument", "script": "بالالایکا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:100",
          "words": [
            {"translit": "balalaika", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old French",
          "refs": "OEW:22",
          "words": [
            {"translit": "babine", "gloss": "hanging lip (not talking properly)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "OEW:22",
          "words": [
            {"translit": "baboon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Italian",
          "refs": "OEW:22",
          "words": [
            {"translit": "bambino", "gloss": "originally meant a wild and savage man; later changed to a brave and courageous man.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "bravo", "gloss": "an expression of approval (for bravery).", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "VOP:87",
          "words": [
            {"translit": "brâvo", "gloss": null, "script": "براوو"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": "AHD; OEW",
          "words": [
            {"translit": "brave, bravo", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Hindustani",
          "refs": "OEW:22",
          "words": [
            {"translit": "bâbŭ", "gloss": "old man (baby talk)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:430",
          "words": [
            {"translit": "bâb 3", "gloss": "an old respectful man", "script": "باب ۳ ( بابو )"}
          ],
          "script_extra": "بابوالخیر",
          "note": "Compare with the Persian word \"bâbâ:father\". See root \"Pa\"",
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "baby, babe, babble", "gloss": null, "script": null}
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


## [2026-09-05T05:46:19.471Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['OEW','AHD','BQT','MON','VOP','POK','KLN','WLD','IEC','SYN','HRN','HUB','PHD','NYB','ARY','SKT','FSD','WEB','LKT','TTS','HJB','AID']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-05T05:46:21.030Z] TOOL RESULT

```
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo
```


## [2026-09-05T05:46:51.254Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-05T05:46:51.293Z] TOOL RESULT

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


## [2026-09-05T05:46:51.835Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/*.json | head -40 && python3 -c \"\nimport json;d=json.load(open('data/verification/page-66.json'));print(json.dumps(d,ensure_ascii=False)[:3000])\""
}
```


### [2026-09-05T05:46:53.885Z] TOOL RESULT

```
data/verification/page-101.json
data/verification/page-126.json
data/verification/page-311.json
data/verification/page-31.json
data/verification/page-32.json
data/verification/page-33.json
data/verification/page-345.json
data/verification/page-34.json
data/verification/page-35.json
data/verification/page-36.json
data/verification/page-37.json
data/verification/page-38.json
data/verification/page-39.json
data/verification/page-40.json
data/verification/page-41.json
data/verification/page-42.json
data/verification/page-43.json
data/verification/page-44.json
data/verification/page-45.json
data/verification/page-46.json
data/verification/page-47.json
data/verification/page-48.json
data/verification/page-49.json
data/verification/page-50.json
data/verification/page-51.json
data/verification/page-52.json
data/verification/page-53.json
data/verification/page-54.json
data/verification/page-55.json
data/verification/page-56.json
data/verification/page-57.json
data/verification/page-58.json
data/verification/page-59.json
data/verification/page-60.json
data/verification/page-61.json
data/verification/page-62.json
data/verification/page-63.json
data/verification/page-64.json
data/verification/page-65.json
data/verification/page-66.json
{"pdf_page": 66, "book_page": 36, "verified_by": "claude-fable-5-1", "verified_on": "2026-09-04", "entries": [{"entry": 0, "root": "A`.s.r", "verdict": "confirmed", "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'", "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.", "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.", "sources": ["https://www.ahdictionary.com/word/semitic.html", "https://www.ahdictionary.com/word/search.html?q=alizarin", "https://en.wiktionary.org/wiki/عصارة"], "ref_check": [{"ref": "KLN:50", "status": "supports", "note": "KLN_1966.txt, form-feed leaf 38 (two printed pages per leaf ⇒ printed pp. ~52-53, i.e. Nourai's p.50 ±2): 'alizari, n., madder root. — F., fr. Sp. alizari, fr. Arab. al-'aṣārah, \"the juice\", fr. al-, \"the\", and aṣara, \"he squeezed, pressed\", which is rel. to Heb. ʿātzar, Aram.-Syr. ʿătzār, \"he retained\".' Exactly the root, the gloss and the Romance chain Nourai draws."}, {"ref": "FVA:273", "status": "not_checked", "note": "FVA = S.M. Nahvi, Farhang-e vāžehā-ye ʿarabi dar fārsi (1368/1989). refs_online.json records no digital copy on archive.org, ketabnak, noorlib or the open web; catalogue record only (OpenLibrary OL2012991M)."
```


## [2026-09-05T05:46:59.506Z] TOOL CALL #7: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -60; echo ---; sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T05:46:59.604Z] TOOL RESULT

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
---
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
```


## [2026-09-05T05:47:00.291Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt; do echo \"== $f\"; grep -n -i -E 'baba|barbar|balbal' $f | head -20; done"
}
```


### [2026-09-05T05:47:01.809Z] TOOL RESULT

```
== POK_01.txt
1218:tausend!^    (daraus    lat.    babae,    papae   ds.,   wie    babaecalus    etwa   , Gigerl,
1221:babiger  (gloss.)  ,dumm^;   ital.  babbo  ,yater^   (cjmr.  baban  ,Kind^   ist   engl.
1225:aksl.  baba  ,altes  Weib^;  serb.-ksl.  bhbVu,  bhbati  ,stammeln^,  serb.  bbbocem,
1229:balbal-  (babal-,  bambal-,  woraus  bam-b-,  bal-b-  u.  dgl.):
1230:Ai.    balbalä-haröti    ,stammelt^;    bulg.    blabölh,    b^lböV^    ,schwatze'',    lit.
1237:Mit  -r-:  ai.  harlara-h  ^stammelnd^,  PI.  Bezeichnung  nichtarischer  Völkej (sofern  hier  r  auf  idg.  r  und  ai.  l  in  halhalä  auf  idg.  l  zurückgeht),  gl ßdoßaoog  ,nicht  griechisch,  von  unverständlicher  Sprache^  (woraus  lat harharus)  ,ßaQßaQ6cpo)vog  ,von  unverständlicher  Sprache^  (kaum  nacl Weidner  Gl.  4,  303 f.  aus  einem  babylon.  barbaru  ,Fremder^),  serb.  brboljüi] brbljati  ,plappern^  (s.  auch  unter  bJier-  , brummen^),  lat.  baburrus  ,stuitus| ineptus^,  gr.  ßaßvQTag'  ö  ftaqd^wQog  Hes.  (über  lat.  burrae  s.  WH.  I  124)j
1259:bal-,  balbal'  _,wirbeln,  sich  drehend
1260:Ai.  balballti  ^wirbelt',   balvd-   ^schief;    gr.  (in   Sizilien)  ßalliLo)  ^tanze^, daraus  entlehnt  lat.  balläre  ^tanzen^ WP.  II  109,  WH.  1,  95,  Wackernagel  Ai.-Gr.  I  181.
1261:bal-bal'  s.  unter  baba-.
1263:Gr.  ßöfxßog  m.  (daraus  lat.  bombus)  ,dumpfer  Ton^,  ßöf^ißv^,  -vxog  ,Flöhe^, ßo^ßvMa  ,summende  Insekten^,  ßo^ßvXr]  ,enghalsiges  Gefaßt  (als  ,gluck- send'^),  ßo^ßvliöq  oder  -vXiog  ,Hummel^  (und  ,enghalsiges  GefäßQ;  über ßa(.ißaivco  ,klappere  mit  den  Zähnen;  stammle,  lisple^  s.  unter  baba-]
1372:Vgl.   mit   z.  T.    ähnlicher    Bed.    hhltd-    , aufsprudeln,    schwatzen',    bhel- , schallen'    und   bal-,  bal-bal-  unter  baba-   (z.  B.  lit.  blebenti   mit  dem  nhd.^ plappern  ähnlicher  Bildung).
1419:gr.  (priiil^  dor.  ^ä/a  ,sage',  (prjuT],  dor.  q)df.iC(  , Kunde,  Ruf,  Offenbarung' (=  lat. /äwa;  dcprjfioreg'  äogr/coi,  ovy,  övoi,La^6{A,€voi  Hes.  und  das  erst  bei Apuleius  begegnende  affämen  , Ansprache'  braucht  keine  alte  Gleichung zu  sein);  (pdoY.ü)  ,sage,  sage  ja,  glaube'  (auch  ßdaY.avog^  lat.  fascimimj  s. unter  *baba  Schalhvort),  q)dvig  f.  , Gerücht',  cpdaig  , Sprache,  Rede,  Behaup- tung, Anzeige';  mit  Ablaut  cpwvi^  , Stimme' ;
1913:Hierher  wenigstens  z.  T.  (mit  gebrochener  Red.)  auch  die  bsl.  Grupp^ von   lit.   barbeti   ^klirren'^,    birbiü,    -iaü,    birbti   ,summen^,    burbiü,    Uivhe^ ^brummen,  brodeln^  u.  dgl.;  klr.  borborösy  PL  _,mürrische  Reden"^,  skr.  bf'blati. ^schwatzen'  u.  dgl.^   in  denen  freilich  die  Bedeutungen   ^undeutlich   reden! stammeln^  auf  die  Gruppe  von    ai.  barbaräh  usw.  (s.  Haba)  zurückgehen werden.
== POK_02.txt
```


## [2026-09-05T05:47:09.903Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 1218\nimport re\nidx=sum(1 for l in lines[:1218] if '\\f' in l)\nprint('formfeeds before line1218:',idx)\npos=t.find('babiger')\nleaf=t[:pos].count('\\f')\nprint('leaf(0-based)',leaf,'-> printed page approx',leaf-8, leaf+1-8)\nprint(t[pos-2500:pos+2500])\nEOF"
}
```


### [2026-09-05T05:47:11.347Z] TOOL RESULT

```
formfeeds before line1218: 95
leaf(0-based) 100 -> printed page approx 92 93
fügt  ist;  Liden  IF. 19,  321).
90
aus-  ^schöpfen^  ^i
Gr.  i^avco  ^schöpfe^  entnelime'^  (Simplex  a^/w),  i^avaviJQ  *  ycgsdyQa,  aiazr^^'^^ ^srQOv  UvofXCCj  yiaravaai'  i^avvXi^aaL,  xaradvaaLj  ytad-avaca'  äcpaviaai  (Aspej^ nach  dem  einstigen  Präsens  *«{;a>  aus  "^al'acj,  Sommer  Gr.  Lautst.  2f; n.  dgl.,  mit  Tiefstufe  *us-  dcp-vco,  äcp-vacü)  (letzteres  aus  dem  Aor.  di(p% vaaai)  ^schöpfe*^,  äcpvauög'  dTtavTlrjcng  Suidas  und  doißcj  ^schöpfe^_,  ursprüngl| */ff^  (:  ai.  vär  , Wasser^)  *^'[ö']w  ^schöpfe  Wasser^^  (^^ror?;^  ^Schöpfgefäß^
Anord.  ausa  ^schöpfen^,   austr  ^das   Schöpfen^  Kielwasser^,  ndd.  ütoeser^' ,ausschöpfen^_,  schwäb.  Ose  ^Schöpfgefäß^.
Lat.  hauriö,  -Ire,  haust,  haustum  ^schöpfe^,  dann  auch  ^schlürfe,  schlinge* erdulde'^,  poet.  ^verwunde'',  mit  sekundärem  h  wie  gelegentlich  in  humerusJl
AVP.  I  27  f.,  WH.  I  637,  869,   W.  Schulze  KL  Sehr.  190  f.,   Schwjzer^ Gr.  Gr.  I  644  ^
B.')
.    x^j-    bba^bh-,  pa^p-  ^scliwellen^  (wie  ha^mh-,  s.  d.).
Ai-  pipp^^^-b  ;Beere_,  Paradiesfeigenbaum^^  pippalaka-h  ^Brustwarzen piplic-h  ^Mal  am  Körper^  (wohl  eig.  ^Blatter^  Bläschen^);  lat.  papula Blatter^  Bläschen^^  papilla  ds.  ;,Brustwarze^;  lit.  päpas  ^Brustwarze^  Zitze^^ popä  ^Geschwür^^  pupuolo  ;,dicke  Knospe^  (u  kann  Redukt.-St.  zu  a,  oder Assimii.  ans  folgende  uo  sein,  aber  auch  der  Wzf.  pup-  entstammen).
Un verschoben  oder  Neuschöpfung  schwed.-norw.  mdartl.  pappe  ^Frauen- brust^;  mengl.  pappe,  engl,  pap  ^jBrustwarze'^;  daneben  w-Formen  s.  unter p(h)^-  ^auf blasen,  schwellend
Auch  neben  den  unter  haba-  vereinigten  Lall-  und  Kinderworten,  wie en<rl.  haby,  stehen  rahd.  huoben  PI.  ^weibliche  Brast^,  westfläm.  habhe ,Geschwulst^  (idg.  hli  oder  im  Schallwort  unverschobenes  h),  die  von  der Vorstellung  der  aufgeblasenen  Backen  aus  in  unseren  Kreis  gehören  werden.
WP.  II  107.
bäba-  Schall  wort,  Lall  wort   für  unartikuliertes  undeutliches  Reden;   ebenso
bal-bal-,  bar-bar-  mit  vielfachen  Dissimilationen.
Ai.  bahabä-karöti   vom   Knistern   des   Feuers;    gr.  ßaßaX,   TcaTcai    ,potz-
tausend!^    (daraus    lat.    babae,    papae   ds.,   wie    babaecalus    etwa   , Gigerl,
Stutzer^    aus   *ßaßaly,alog),    ßaßaCoi    ,schwatze,    rede    undeutlich^   (anders
ist   die   Lautvorstellung   von   ßa��q&Lo)  ,zirpe^);    lat.  babit  (gloss.)   ,yavqia^,
babiger  (gloss.)  ,dumm^;   ital.  babbo  ,yater^   (cjmr.  baban  ,Kind^   ist   engl.
Lw.);   alb.  bebe  ,neugeborenes   Kind^;    engl,    baby  ,Kind^,  schwed.  mdartl.
babbe  ,Kind,  kleiner  Juuge^  (s.  auch  unter  bä^mb-  ,schwellen^),  mhd.  bäbe,
böbe  ,Alte,  Mutter^  (über  buobe  ,Knabe^  s.  unter  bhräter  ,Bruder^);  lit.  böba,
aksl.  baba  ,altes  Weib^;  serb.-ksl.  bhbVu,  bhbati  ,stammeln^,  serb.  bbbocem,
bohhtati  ,mit  den  Zähnen  klappern^  usw.;  lett.  bibinät  ,plappern,  murmeln^,
apr.  bebbint  ,spottenn
♦  ,
balbal-  (babal-,  bambal-,  woraus  bam-b-,  bal-b-  u.  dgl.):
Ai.    balbalä-haröti    ,stammelt^;    bulg.    blabölh,    b^lböV^    ,schwatze'',    lit.
6aZ&as?/^i , plappern^,  serbokr.  öZa5os^7^, stammeln^,  russ.  bolob6lit^  ,schwatzen,
faseln^,    öech.   beblati   ,stammeln^;    lat.  babulus  ,Schwätzer%'    nhd.   babbeln,
päppeln,  engl,  babble,  norw.  bable,  schwed.  babbla,  aisl.  babba  ,schwatzen^;
^)  Fast  nur  Schallworte;  vgl.  Johansson  KZ  36,  342 ff.,  Hirt  Idg.  Gr.  I  214f.,  Schwyzer Gr.  Gr.  I,  291.
92  #
lat.  halbus  ^stammeln d^  lallend^;  halhütiö  ^stammle^^   ai.  halhüthd-h  Nam^j (eigentlich  ^Stammler^),  cech.  hlh  ^Tölpel^,  hlhlati,  6Zep^a^^, stammeln^  stottern^ serb.  llehetati,  lit.  Uebenti  ^plappern^;  gr.  ßaixßaXv^o)  (daraus  lat.  hambalc^ ßa!.ißay,v^cü  ^habe  Zähneklappernd,  ßa^ßaiva)  ^»stammle^
Mit  -r-:  ai.  harlara-h  ^stammelnd^,  PI.  Bezeichnung  nichtarischer  Völkej (sofern  hier  r  auf  idg.  r  und  ai.  l  in  halhalä  auf  idg.  l  zurückgeht),  gl ßdoßaoog  ,nicht  griechisch,  von  unverständlicher  Sprache^  (woraus  lat harharus)  ,ßaQßaQ6cpo)vog  ,von  unverständlicher  Sprache^  (kaum  nacl Weidner  Gl.  4,  303 f.  aus  einem  babylon.  barbaru  ,Fremder^),  serb.  brboljüi] brbljati  ,plappern^  (s.  auch  unter  bJier-  , brummen^),  lat.  baburrus  ,stuitus| ineptus^,  gr.  ßaßvQTag'  ö  ftaqd^wQog  Hes.  (über  lat.  burrae  s.  WH.  I  124)j
Hierher  vielleicht  auch  ai.  bäla-h  ,jung,  kindlich,  einfältig^,  möglicher« weise  auch  die  slav.  Sippe  von  russ.  baldkath  ,schwätzen^,  balamüt% ,Schwätzer,  Kopfverdreher^  —  Unredupl.  vermutlich  auch  gr.  ßd^cj  ,rede] schwatze'^,  ßd^ig  ,Rede^,  ßdaycsiv  XkyBiv,  -/.a'^oXoystv  Hes.;
aber  gr.  ßdazavog  ,beschreiend,  behexend;  Übles  nachredend,  verleum- derisch; neidisch^,  ßaazaivco  ,behexe,  beneide^  sind  als  Zauberwort  durchl Entlehnung  aus  ei
```


## [2026-09-05T05:47:20.949Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins baba\"; grep -n -i -E '^\\s*b(a|ā)ba|baba-' AHD_watkins1985.txt | head -20\necho \"=== AHD barbarian/babble/baboon\"; grep -n -i -E 'barbar|babble|baboon|balalaika' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T05:47:21.024Z] TOOL RESULT

```
=== AHD watkins baba
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
=== AHD barbarian/babble/baboon
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
```


## [2026-09-05T05:47:22.303Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in barbarous barbarian rhubarb baboon balalaika 'babble' 'brave' 'bravo' 'bambino'; do echo \"===KLN $w\"; grep -n -i \"$w\" KLN_1966.txt | head -6; done"
}
```


### [2026-09-05T05:47:24.160Z] TOOL RESULT

```
===KLN barbarous
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4426:Barbara,  fern.  PN.  —  L.,  prop.  fern,  of  barbarus, ‘strange,  foreign,  barbarous’,  fr.  Gk.  (3ap(3apop. See  barbaric.
4427:Barbarea,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  named  after  St.  Barbara. barbarian,  n.  and  adj.  —  Formed  with  suff.  -ian fr.  Gk.  fSapPapop.  See  barbaric, barbaric,  adj.  —  OF.  barbarique,  fr.  L.  barbari- cus,  ‘foreign,  strange,  outlandish’,  fr.  G.  pap- fJocpixop,  fr.  pippapop,  ‘non-Greek,  foreign, barbarous’,  which  is  cogn.  with  OI.  barbarah, ‘stammering  (designation  of  the  non-Aryan nations),  from  the  I.-E.  imitative  base  *barb-, ‘to  stammer,  stutter;  unintelligible’.  Cp.  brave. Cp.  also  Berber  and  the  second  element  in  rhu¬ barb.  For  *balb-,  a  collateral  base  of  *barh-,  see balbuties,  booby.  For  the  imitative  base  *bab- see  babble.
4429:Derivative;  barbariz-ation,  n. barbarous,  adj.  —  L.  barbarus,  fr.  Gk.  pxpp-xpop. See  barbaric.  For  E.  -ous,  as  equivalent  to  Gk. -op,  see  -ous.
4430:Derivatives:  barbarous-ly,  adv.,  barbarous¬ ness,  n.
4431:Barbary,  n.,  the  countries  in  North  Africa  west of  Egypt.  —  OF.  Barbarie,  fr.  L.  barbaria ,  ‘a foreign  country’,  fr.  barbarus,  ‘strange,  foreign, barbarous’.  See  barbaric  and  -y  (representing OF.  -ie).
===KLN barbarian
2226:aljamia,  n.,  Moorish  name  of  the  Spanish  lan¬ guage.  —  Sp.  aljamia,  fr.  Arab.  al-‘ajamtyah, ‘the  non-Arabic,  barbarian  (language)’,  fr.  al-, ‘the’,  and  fern.  oVajamt,  ‘non-Arabic,  barbarian’, aljofaina,  n.,  wash  basin.  —  Sp.,  fr.  Arab,  al- jufaynah,  dimin.  of  al-jdfnah  (whence  Sp,  alja- fana),  fr.  al-,  ‘the’,  and  jafnah,  ‘dish’, alkahest,  n.,  the  universal  solvent  of  the  alche¬ mists.  —  F.  alcahest,  fr.  ML.  alcahest,  a  pseudo- Arabic  word  prob.  coined  by  Paracelsus, alkali,  n.  —  F.  alcalli  (now  spelled  alcali),  fr. Arab,  al-qilt,  fr.  al-,  ‘the’,  and  qilt,  ‘charred ashes  of  the  saltwort’,  fr.  qala,  ‘he  fried,  roast¬ ed’,  which  is  rel.  to  Heb.  qaldh,  ‘he  roasted, parched’,  Aram.  qeld,  ‘burned’,  Akkad,  qalu.
4427:Barbarea,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  named  after  St.  Barbara. barbarian,  n.  and  adj.  —  Formed  with  suff.  -ian fr.  Gk.  fSapPapop.  See  barbaric, barbaric,  adj.  —  OF.  barbarique,  fr.  L.  barbari- cus,  ‘foreign,  strange,  outlandish’,  fr.  G.  pap- fJocpixop,  fr.  pippapop,  ‘non-Greek,  foreign, barbarous’,  which  is  cogn.  with  OI.  barbarah, ‘stammering  (designation  of  the  non-Aryan nations),  from  the  I.-E.  imitative  base  *barb-, ‘to  stammer,  stutter;  unintelligible’.  Cp.  brave. Cp.  also  Berber  and  the  second  element  in  rhu¬ barb.  For  *balb-,  a  collateral  base  of  *barh-,  see balbuties,  booby.  For  the  imitative  base  *bab- see  babble.
4428:Derivative:  barbaric-al-ly,  adv. barbarism,  n.  —  F.  barbarisms,  fr.  L.  barbarismus, fr.  Gk.  pappapiopLop,  ‘unintelligible  speech’,  fr. PdcpPapop.  See  prec.  word  and  -ism. barbarity,  n.  —  See  barbaric  and  -ity. barbarize,  tr.  and  intr.  v.  —  Gk.  pappxpt^Etv, ‘to  speak  like  a  barbarian’,  fr.  pdtppocpop.  See barbaric  and  -ize.
5561:Derivative:  bravado,  intr.  v. brave,  adj.  —  F.,  fr.  It.  bravo,  orig.  meaning ‘wild,  savage’,  fr.  L.  barbarus,  ‘foreigner’ (through  the  intermediate  forms  *brabarus, *brabus)\  with  change  of  meaning  from  ‘wild’ to  ‘courageous’.  See  barbarian  and  cp.  brab. Derivatives:  brave,  n.,  brave,  v.  (q.v.),  brave¬ ry,  n.
10364:dasi,  n.,  a  female  slave;  a  concubine  (Hinduism). —  Hind.,  fr.  OI.  ddsi-,  ‘female  slave’,  which  is rel.  to  dasah,  ‘demon,  enemy,  barbarian,  slave, servant’,  and  prob.  also  to  dasyuh,  ‘demon, enemy  of  the  gods,  barbarian’,  dasyah,  ‘bon¬ dage,  servitude’.  Cp.  the  second  element  in devadasi.
===KLN rhubarb
12986:Derivative:  emmetrop-ic,  adj. emodin,  n.,  a  compound  obtained  from  rhubarb (chem.)  —  Formed  with  chem.  suff.  -in  fr.  ModL. (Rheum)  emodl,  ‘Turkey  rhubarb’,  lit.  ‘rhubarb of  the  Himalaya’,  fr.  Gk.  'HpuoSAi;,  ‘the  Hima¬ laya’.
32758:rhapontic,  n„  a  species  of  rhubarb.  —  ModL.  rha-
32759:ponticum,  fr.  MedL.  rha  Ponticum,  lit.  ‘Pontic rhubarb’.  The  first  element  stands  for  orig. rheum,  ‘rhubarb’,  fr.  Gk.  pijov,  fr.  Pers.  rewend, of  s.m. ;  the  alteration  of  rheum  into  rha  is  due to  a  confusion  with  Rha,  the  ancient  name  of the  river  Volga.  See  Rheum,  rhubarb.  For  the second  element  see  Pontic.
32780:Rheum,  n.,  a  genus  of  herbs  (bot.)  —  L.,  ‘rhubarb’, fr.  Gk.  prjov,  fr.  Pers.  rewend,  of  s.m.  See  rhu¬ barb  and  cp.  rhapontic.
32823:rhombus,  n.,  an  oblique-angled  equilateral  paral¬ lelogram.  —  L.  See  rhomb, rhoncial,  also  rhonchal,  adj.,  pertaining  to  arhon- chus.  See  next  word  and  adj.  suff.  -al. rhonchus,  n.,  a  whistling  sound  heard  on  the auscultation  of  the  chest.  —  L.,  ‘a  snoring’,  fr. Gk.  poy-/_o;,  which  is  rel.  to  (56yxo;,  friyyoq, ply xo;,  of  s.m.  plyysiv,  peyxEtv,  ‘to  snore’; prob.  of  imitative  origin, rhotacism,  n.,  mispronunciation  of  the  letter  r.  — ModL.  rhotacismus,  fr.  Gk.  ptoTaxiopoc,  fr. pwraxlqEiv.  See  next  word  and  -ism. rhotacize,  intr.  v.,  to  mispronounce  the  letter  r. — Gk.  ptoTaxi^Eiv,  ‘to  use  the  letter  r  excessive¬ ly’,  fr.  p<7>,  name  of  the  letter  r.  See  rho  and  -ize. rhubarb,  n.,  a  garden  plant  with  large  leaves  and edible  leaf  stalks.  —  ME.  rubarbe,  fr.  MF.  reu- barbe,  rubarbe  (F.  rhubarbe),  fr.  ML.  rheubar- barum.  The  first  element  in  ML.  rheubarbarum derives  fr.  L.  rheum,  fr.  Gk.  ptjov,  ultimately  fr. Pers.  rewend,  ‘rhubarb’  (whence  also  Russ. reven).  Cp.  the  ML.  form  rhabarbarum,  which comes  fr.  Gk.  pec  fSxppapov,  lit. ‘foreign  rhubarb’ ; px,  ‘rhubarb’,  is  a  blend  of  pvjov,  ‘rhubarb’,  with 'Pa,  the  Scythian  name  of  the  Volga;  see  roric. The  second  word  in  pa  |3xp!3xpov  refers  to  the foreign  origin  of  the  plant.  It.  rabarbaro  (whence G.  Rhabarber)  derives  fr.  Gk.  pa  |3dpj3xpov.  Cp. rhapontic,  rheum.
33106:roric,  adj.,  pertaining  to  dew.  —  Formed  with suff.  -ic  fr.  L.  ros,  gen.  roris,  ‘dew’,  which  is  cogn. with  Lith.  rasa,  OSlav.  rosa,  ‘dew’,  Ol.  rasah, ‘sap,  juice,  fluid,  essence’,  rasa,  ‘moisture’,  Rasa, name  of  a  mythic  river  (=  Avestic  Rahha), aryati,  ‘flows',  rsabhdh,  ‘bull,  steer’,  Avestic  and OPers.  arshan,  ‘man’,  Hitt,  arszi,  ‘flows’,  Gk. Sp  ary,  jipp  tjv.  ‘male,  masculine’,  prob.  also  'Pa, Scythian  name  of  the  Volga,  fr.  I.-E.  base  *ras-, *eras-,  *eres-,  *ers-,  ‘to  flow,  wet,  moisten’.  Cp. rasa,  romerillo,  rosemary,  rosolio,  rouse,  ‘to pickle'.  Cp.  also  the  first  element  in  rhubarb  and the  second  element  in  Ahasuerus  and  in  Xerxes, rorqual,  n.,  any  whale  of  the  genus  of  large  whales, the  Balaenoptera.  —  F.,  fr.  Norw.  reyrhval,  fr. ON.  reydarhvalr,  fr.  reydr,  ‘rorqual’  (fr.  raudr, ‘red"),  and  hvalr,  ‘whale’.  See  red  and  whale. Rosa,  1)  fern.  PN.;  2)  a  genus  of  plants,  the  rose (bot.)  —  L.  rosa,  ‘rose’.  See  rose.
===KLN baboon
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4225:baboo,  n.,  Master,  Mr.  —  Hind.  babu. baboon,  n.  —  ME.  baboin,  fr.  OF.  babuin,  ba- bouin  (F.  babouiti),  a  blend  of  babine,  ‘the  pen¬ dulous  lip  of  certain  animals,  esp.  monkeys’  (the baboon  has  prominent  lips),  and  baboue,  ‘wry, ugly  face’ ;  both  babine  and  baboue  are  of  imi¬ tative  origin.  See  Bloch-Wartburg,  DELF.,  p.49 s.v.  babouin.  MDu.  baubijn  (whence  Du.  baviaan) is  an  OF.  loan  word.  G.  Pavian  is  borrowed  fr. Du.  baviaan.
4226:Derivative:  baboon-ery,  n. babouche,  n.,  a  heelless  Oriental  slipper.  —  F., fr.  Arab,  babiish,  fr.  Pers.  papush,  lit.  ‘foot- covering’,  fr.  pa,  ‘foot’,  and  the  verb  pushiden, ‘to  cover’.  Pers.  pa  is  rel.  to  Avestic pad-,  ‘foot’ ; see  foot.  The  change  of  p  to  b  proves  that  the word  came  into  Europe  through  the  medium  of the  Arabic,  which  having  no  p,  regularly  chan¬ ges  the  p  of  foreign  words  into  b. baby,  n.  - —  Dimin.  of  babe.
7101:chabot,  n.,  the  fish  called  miller’s  thumb  (her.)  — F.,  ‘miller’s  thumb’,  also  ‘bullhead’,  fr.  earlier cahot,  fr.  OProven?.  cabotz,  ‘a  large-headed (fish)’,  fr.  VL.  *capoceus,  fr.  L.  caput,  ‘head’.  See capital,  adj.,  and  cp.  Capito. chabouk,  chabuk,  n.,  a  long  whip.  —  Pers.  chdbug, ‘a  whip’.  Cp.  chawbuck,  sjambok, cha-cha,  also  cha-cha-cha,  n.,  a  dance  in  3-beat rhythm.  —  Amer.  Sp.  cha-cha-cha. chacma,  n.,  a  South  African  baboon.  —  Hot¬ tentot.
12270:drill,  n.,  a  baboon  of  Western  Africa.  —  Native name.  Cp.  mandrill.
22773:mandrake,  n.  —  ME.  mandrake,  altered  by  folk etymology  (as  if  it  were  a  compound  of  man  and drake),  fr.  ME.  mandragge,  fr.  OE.  mandragora, fr.  L.  mandragoras.  See  prec.  word, mandrel,  mandril,  n.,  a  metal  bar.  —  Fr.  earlier manderil,  corrupted  fr.  F.  mandrin,  ‘mandrel’, which  is  rel.  to  ModProven?.  mandre,  ‘axle, winch,  crank’ ;  of  uncertain  origin mandrill,  n.,  a  kind  of  large  baboon,  Papio  mai- mon.  —  Compounded  of  man  and  drill,  ‘ba¬ boon’.
===KLN balalaika
4255:balalaika
4303:Balaena,  n.,  a  genus  of  whales,  the  Greenland whale.  —  L.  ballaena,  balaena.  See  baleen, balaghat,  balaghaut,  n.,  tableland  above  the  pas¬ ses  (Anglo-Ind.)  —  Formed  fr.  Pers.  bald, ‘above’,  and  Hind,  ghat,  ‘a  pass’, balalaika,  n.,  a  Russian  stringed  instrument  with a  triangular  body.  —  Russ,  balalaika,  which, according  to  Erich  Berneker,  Etymologisches
5340:booby,  n.,  an  awkward  fellow;  name  of  various seabirds.  —  Sp.  hobo.  fr.  L.  balbus,  ‘stammering’, from  the  I.-E.  imitative  base  *balb-,  whence  also OI.  Balbuthdh ,  a  name  (lit.  ‘the  stammerer’), Czech  bib,  ‘booby’,  blblati,  ‘to  stammer’,  Ser¬ bian  blebdtati,  ‘to  blabble’,  OI.  balbala-karoti, ‘he  stammers’,  Russ,  balabdliti,  ‘to  chatter, babble’,  Bulg.  blabdl’u,  ‘I  chatter,  babble’. *Barb-,  a  collateral  base  of  base  *balb-,  ap¬ pears  in  OI.  barbarah,  ‘stammering’  (desig¬ nation  of  the  non-Aryan  nations),  Gk.  pSap(3a- poq,  ‘non-Greek,  foreign,  barbarous’,  Slovenic brbrati,  brbljati,  Serbian  brboljiti,  ‘to  mumble, mutter’,  Lith.  birbti,  ‘to  buzz,  hum’.  Cp.  babble, babe,  baby,  balalaika,  balbuties,  barbaric,  bauble. Derivative:  booby-ish,  adj. boodle,  n.,  money  {slang).  —  Prob.  fr.  Du.  boe- del,  ‘estate,  possession’.  Cp.  caboodle, boohoo,  intr.  v.  and  n.  —  Of  imitative  origin. Cp.  boo.
===KLN babble
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4222:Derivatives:  babble,  n.,  babbl-er,  n.,  babbl-ing, n.  and  adj.,  babbl-ing-ly,  adv.,  babbl-ish,  adj., babbl-ish-ly,  adv.,  babbl-ish-ness,  n.,  babb!-y,ad}. babe,  n.  —  ME.,  of  imitative  origin.  See  prec. word  and  cp.  baby.  Cp.  also  boy.
4306:Worterbuch  der  russischen  Sprache,  I,  p.40, Heidelberg,  1908-13,  is  rel.  to  Russ,  balabolit’, ‘to  chatter,  babble',  from  the  I.-E.  imitative  base *balb-,  whence  also  L.  balbus,  ‘stammering’.  See booby  and  cp.  words  there  referred  to. balan-,  form  of  balano-  before  a  vowel, balance,  n.  —  OF.  (=  F.)  balance,  fr.  L.  bi-, ‘two,  twice’,  and  VL.  *lancia,  fr.  L.  lanx,  gen. lands,  ‘plate,  dish;  scale  of  weighing  machine’, which  prob.  stands  for  *llnk-s,  fr.  I.-E.  base *iliq~,  ‘to  bend’,  whence  prob.  also  Gk.  k&aoq, Xexovt),  ‘dish’,  lt/pwc„  ‘slanting,  crosswise’, Xo E,6<;,  ‘slanting,  crooked,  bent’;  see  Walde- Hofmann,  LEW.,  I,  p.761  s.v.  lanx.  See  bi-  and loxo-  and  cp.  the  second  element  in  auncel.  Cp. also  Lecanium,  Lecidea,  lekane.  The  first  a  in balance  is  prob.  due  to  an  association  of  this word  with  F.  bailer,  ‘to  dance’,  fr.  Gk.  paXXeiv, ‘to  throw’  (see  ballistic).
4309:balatron,  n.,  jester,  buffoon.  —  L.  balatro,  gen. -onis,  of  Etruscan  origin;  not  related  to  L. blaterd,  ‘babbler’.
4427:Barbarea,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  named  after  St.  Barbara. barbarian,  n.  and  adj.  —  Formed  with  suff.  -ian fr.  Gk.  fSapPapop.  See  barbaric, barbaric,  adj.  —  OF.  barbarique,  fr.  L.  barbari- cus,  ‘foreign,  strange,  outlandish’,  fr.  G.  pap- fJocpixop,  fr.  pippapop,  ‘non-Greek,  foreign, barbarous’,  which  is  cogn.  with  OI.  barbarah, ‘stammering  (designation  of  the  non-Aryan nations),  from  the  I.-E.  imitative  base  *barb-, ‘to  stammer,  stutter;  unintelligible’.  Cp.  brave. Cp.  also  Berber  and  the  second  element  in  rhu¬ barb.  For  *balb-,  a  collateral  base  of  *barh-,  see balbuties,  booby.  For  the  imitative  base  *bab- see  babble.
4571:bausond,  adj.,  having  white  spots  or  stripes  {dial. E.)  —  OF.  baufant.  See  prec.  word, bauxite,  n.,  a  claylike  hydrate  of  aluminum  (min¬ eral.)  —  F.,  fr.  Les  Baux,  near  Soles  in  France, where  this  compound  was  first  found.  The  name Les  Baux,  fr.  Proven?.  Li  Baus,  lit.  means  ‘the precipices’.  Proven?,  baus  derives  fr.  L.  balteus, ‘girdle’,  whence  also  Rum.  bal\,  ‘girdle’.  It.  bal- zo,  ‘shelf’,  balzare,  ‘to  spring,  jump’.  See  belt and  subst.  suff.  -ite  and  cp.  bauson, bavenite,  n.,  a  calcium  aluminum  silicate  (min¬ eral.)  —  Named  after  Baveno  in  Italy.  For  the ending  see  subst.  suff.  -ite. bavette,  n.,  a  child’s  bib.  —  F.,  dimin.  formed  fr. have,  ‘drivel,  slaver’,  fr.  baver,  ‘to  drivel,  slob¬ ber’  (whence  bavarder,  ‘to  babble,  prattle’);  of imitative  origin.  Bavette  lit.  means  ‘slobbering bib’.  For  the  ending  see  suff.  -ette. bawbee,  n.,  1)  sixpence;  2)  halfpenny.  —  Named after  the  Laird  of  Sill ebawby,  a  mintmaster  of Scotland  in  the  1 6th  cent, bawd,  n.,  procurer,  procuress.  — -  ME.  bawde, ‘joyous,  merry’,  prob.  fr.  OF.  baude,  baud,  ‘bold’, which  is  of  Teut.  origin.  Cp.  OE.  bald,  beald, ‘bold’,  and  see  bold.
===KLN brave
1431:Achilles,  n.,  son  of  Thetis  and  Peleus,  the  bravest hero  in  the  Trojan  war.  —  L.  Achilles,  fr.  Gk. ’AxtXXeu?,  a  name  of  prob.  pre-Greek  origin. Achilles’  tendon.  —  So  called  from  the  myth  of Achilles  being  held  by  the  heel  when  his  mother Thetis  dipped  him  into  the  river  Styx  to  render him  invulnerable;  first  used  by  the  Dutch  ana¬ tomist  Verheyden  in  1693  when  dissecting  his own  amputated  leg.  See  Achilles  and  tendon, achlamydate,  adj.,  having  no  mantle  (zool.)  — Lit.  ‘not  chlamydate’,  fr.  priv.  pref.  a-  and chlamydate.
2135:—  L.  Alcmaed(n),  fr.  Gk.  ’AXxpucicov,  prob. meaning  lit.  ‘valiant,  brave’.  Cp.  Gk.  aXxp.oaos (Hesychius),  ‘young  man’,  &Xxp.ap£s  (neut.) (ibidem),  ‘strong,  powerful’.
3368:arditi,  n.  pi.,  Italian  volunteers  serving  in  storm troops  in  World  War  I.  —  It.,  pi.  of  ardito, ‘brave,  audacious’,  fr.  F.  hard/,  prop.  pp.  of  OF. *hardir,  ‘to  render  courageous’,  lit.  ‘to  make hard’,  fr.  Frankish  *hardjan,  fr.  *hart,  ‘hard’, which  is  rel.  to  OHG.  harti.  OE.  heard,  ‘hard’. See  hard.
4221:babble,  intr.  and  tr.  v.  —  ME.  babelen,  from  the I.-E.  imitative  base  *bab-,  whence  also  ON. babba ,  Swed.  babbla ,  Norw.  babble,  LG.  bab- beln,  Du.  babbelen,  G.  babbeln,  ‘to  prattle',  L. babulus ,  ‘babbler’,  F.  babilter,  ‘to  stutter,  stam¬ mer’  ;  cp.  babe,  baboon,  bauble.  Cp.  the  related imitative  base  *balb-,  whence  L.  balbus,  ‘stam¬ merer’  ;  see  balbuties,  booby.  Cp.  also  the  related imitative  base  *barb-,  ‘to  stammer’,  whence  Gk. ^ap^apoi ;,  ‘foreign,  barbarous’;  see  barbaric, brave.
4427:Barbarea,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  named  after  St.  Barbara. barbarian,  n.  and  adj.  —  Formed  with  suff.  -ian fr.  Gk.  fSapPapop.  See  barbaric, barbaric,  adj.  —  OF.  barbarique,  fr.  L.  barbari- cus,  ‘foreign,  strange,  outlandish’,  fr.  G.  pap- fJocpixop,  fr.  pippapop,  ‘non-Greek,  foreign, barbarous’,  which  is  cogn.  with  OI.  barbarah, ‘stammering  (designation  of  the  non-Aryan nations),  from  the  I.-E.  imitative  base  *barb-, ‘to  stammer,  stutter;  unintelligible’.  Cp.  brave. Cp.  also  Berber  and  the  second  element  in  rhu¬ barb.  For  *balb-,  a  collateral  base  of  *barh-,  see balbuties,  booby.  For  the  imitative  base  *bab- see  babble.
5093:Derivative:  bivouac,  intr.  v. bixbyite,  n.,  an  iron  mangenese  oxide  (mineral.) —  Named  after  Maynard  Bixby  of  Utah,  its discoverer.  For  the  ending  see  subst.  suff.  -itc. bizarre,  adj.,  strange.  —  F.,  fr.  It.  bizzarro,  ‘ca¬ pricious’,  fr.  Sp.  bizarro,  ‘gallant,  brave’,  fr. Basque  bizar,  ‘beard’.  The  sense  development of  the  word  is  due  to  the  strange  impression made  by  the  bearded  Spanish  soldiers  upon the  French.
===KLN bravo
5486:brab,  n.,  the  Palmyra  tree.  —  Corruption  of  Port. brava  (which  is  short  for  palmeira  brava ,  ‘wild palm"),  fern,  of  bravo,  ‘wild’,  fr.  L.  barbarus. See  brave.
5561:Derivative:  bravado,  intr.  v. brave,  adj.  —  F.,  fr.  It.  bravo,  orig.  meaning ‘wild,  savage’,  fr.  L.  barbarus,  ‘foreigner’ (through  the  intermediate  forms  *brabarus, *brabus)\  with  change  of  meaning  from  ‘wild’ to  ‘courageous’.  See  barbarian  and  cp.  brab. Derivatives:  brave,  n.,  brave,  v.  (q.v.),  brave¬ ry,  n.
5562:brave,  tr.  v.,  to  defy;  intr.  v.,  to  boast.  —  F. braver,  ‘to  dare,  defy’,  fr.  brave.  See  brave,  adj. Derivatives:  braver,  n.,  brav-ing,  n. bravo,  n.,  brigand.  —  It.  bravo,  fr.  L.  barbarus. See  brave,  adj.
5563:bravo,  interj.,  well  done! ;  n.,  the  shout  ‘bravo’.  — ■ It.  bravo,  ‘the  brave  man’,  used  in  applauding actors,  etc. ;  the  fern,  form  brava  is  used  in  ap¬ plauding  a  woman,  the  pi.  bravi  in  applauding several  people.  See  brave,  adj. bravoite,  n.,  an  iron  sulfide  containing  nickel (mineral.)  —  Named  after  Jose  J.  Bravo,  of Lima,  Peru.  For  the  ending  see  subst.  suff.  -ite. bravura,  n.,  I)  boldness,  spirit;  2)  in  music,  a brilliant  passage.  —  It.,  ‘bravery,  spirit’,  formed
5565:fr.  bravo,  ‘courageous,  brave’,  with  suff.  -lira. See  brave,  adj.,  and  -ure. brawl,  intr.  v.  —  ME.  braulen,  ‘to  scold,  quarrel’, fr.  braule,  ‘scold,  quarrel’,  rel.  to  Du.  and  LG. brallen,  ‘to  brag’.
36043:Derivatives:  spacious-ly,  adv.,  spacious-ness,  n. spadassin,  n.,  a  swordsman,  bravo.  —  F.,  fr.  It. spadaccino,  ‘swordsman’,  fr.  spada,  ‘sword’,  fr. L.  spatha,  fr.  Gk.  oTtafir).  See  next  word, spade,  n.,  a  tool  for  digging.  —  ME.,  fr.  OE. spadu,  rel.  to  OS.  spado,  OFris.  spada,  Dan., Swed.,  MDu.,  Du.  spade,  ‘spade’,  MHG.  spat(e), G.  Spaten,  and  cogn.  with  Gk.  an dtUv),  ‘a  flat wooden  instrument;  a  broad,  two-edged  sword’ (whence  L.  spada,  ‘a  broad  wooden  instrument, a  broad,  two-edged  sword’).  These  words  are formed — with  rfA-formative  element — fr.  I.-E. base  *spe(i)-,  *spi-,  ‘to  draw,  stretch,  span, spread,  extend’,  whence  also  L.  spatium,  ‘space, room,  extent’.  See  space  and  cp.  spadassin, spade  on  cards,  spadilla,  spadix,  spado,  spathe. Cp.  also  epaulet  and  words  there  referred  to. Derivatives:  spade,  tr.  v.,  to  dig  with  a  spade. spade-ful,  adj.
===KLN bambino
4345:bambino,  n.,  a  little  child ;  an  image  of  the  infant Jesus.  —  It.,  ‘baby’,  dimin.  of  bambo,  ‘simple’, w  hich  is  of  imitative  origin, bamboo,  n.  —  Malay  bambu.  Cp.  Bambusa.
```


## [2026-09-05T05:47:53.855Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD\"; grep -n -i -E 'barbu|barbat|wlbwt|barbi' PHD.txt PHD_mackenzie.txt | head -10\necho \"=== NYB\"; grep -n -i -E 'barbu|barbat' NYB_vol2_glossary.txt | head -10\necho \"=== HRN\"; grep -n -i -E 'barbat|barbut|barbit' HRN.txt | head -10\necho \"=== HUB\"; grep -n -i -E 'barbat|barbut|barbit' HUB.txt | head -10\necho \"=== LKT\"; grep -n -i -E 'balalaika|barbat|babu|baboo' LKT.txt | head -10\necho \"=== HJB\"; grep -n -i -E 'BABOO' HJB.txt | head -8\necho \"=== AID\"; grep -n -i -E 'babu|baboo' AID.txt | head -8"
}
```


### [2026-09-05T05:47:54.004Z] TOOL RESULT

```
=== PHD
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:2691:lyre barbut, kennàr; v. harp.
PHD_mackenzie.txt:1500:barbut [blbwt I N -] lyre.
PHD_mackenzie.txt:7001:link band.                               lyre barbut, kennar; v. harp.
=== NYB
=== HRN
=== HUB
=== LKT
669:'Laute' ;  hieraus  russ.  halalaika,  klr. balabaika,  serb.  balalajka,  öech.  bala- lajka  'russische  Zither  oder  Laute  mit zwei  oder  drei  Saiten' ;  frz.  la  balale'ika, dtsch.  Balalaika.    [Gorjajew  10.
3166:13fi5.  Ar.  luaimuu: 'Affe'  [eigentlich  'glücklich,  glückbrin- gend' genau  wie  das  andere  Wort  für Affe:  ar.  su'dän,  si'dän;  Euphemismus, da  der  Alle  als  Teufel  gilt.  Vgl.  Nöldeke, Neue  Beiträge  zur  semitischen  Sprach- wissenschaft. S.  89.  Zusammenhang mit  gl',  m^d»  ist  also  abzulehnen];  hier- aus it.  mammone  'Meerkatze',  maimone [Oriente  I,  195],  afrz.  prov.  maimon, kat.  maymon  'heuchlerisch,  faul',  sp.  pg. mono,  mona,  frz.  maimon,  mona,  Ablei- tung mimonet,  momine,  rum.  malmu^ä, momi^ä  [mit  Sulfixwechsel];  ferner  [mit Wechsel  von  m  zu  b]  it.  babuino;  engl. haboon  'Affe';  bulg.  majmima,  serb. majmun,  poln.  munia.  [ML  5242.  Devic DEt  155  (auf  pers.  m.  zurückgeführt). Mikl  SiElWb  ISO.
3716:1625.  Pers.  päpüs: 'Fußbekleidung'  [aus  pers.  p&  'Fuß' Horn  NpEt  S.  63,  Nr.  281  und  püs  Prä- sensstamm von  püsldän  'bedecken'], ebenso  tk.  papus,  ar.  bäbüs;  hieraus  it. babbuccia,  frz.  babouche,  sp.  babuche, Tum.papuci,  papuc  'leichter  Hausschuh', siz.  babbaluci  'verschiedene  Arten Schnecken' ;  serb.  papusa,  poln,  babusza, öech.  papuö,  russ.  babiisi  'Pantoffeln ohne  Hackenleder';  dtsch.  Babusche, (dial.  Schlesien)  Paputschen.  [DE  231, Eguilaz  328.  ML  858  und  6216  (gehören natürlich  zusammen).    GrSVociSic  227.
4794:'Moos,  Flechte';  hieraus  im  Latein  der Bolaniker  usnea  'eine  Flechte  der  Familie der  Ascolichenes,  z.  B.  Usnea  barbata 'Bartflechte'  und  frz.  usnde  'eine  Flechte', usn^e  humaine  'Flechte,  die  auf  den  der Luft  ausgesetzten  Schädeln  der  Toten sprießt' ;  man  schrieb  ihr  früher  außer- ordentliche Heilkräfte  zu.  [Devic  DEl  224;
5713:Babusche  16^5
5718:Balalaika  198
5991:baboon  1365
6904:babuino  1365
7639:babusza  1625 bachmat(y)  128 bachor  180 bachur  180 baczmag  265 badawja  164 öarfja  159 badjan  162 ftöi-aZie  189 balaban  1607 balagula  145  d bafamucic  199 balamut  199 baldachin  170 balkon  197 balsani  293 Z»af<a  207
8668:arababura  52
=== HJB
132:Of  words  that  seem  to  have  been  admitted  to  full  franchise,  we  may  give examples  in  curry^  toddy^  veranda,  cheroot,  loot,  nahob,  teapoy,  sepoy,  cowry ;  and of  others  familiar  enough  to  the  English  ear,  though  hardly  yet  received into  citizenship,  compound,  batta,  pucka,  chowry,  baboo,  mahout,  aya,  nauU^,* first-chop,  competition-toa/^,  griffin,  &c.  But  beyond  these  two  classes  of words,  received  within  the  last  century  or  so,  and  gradually,  into  half  or whole  recognition,  there  are  a  good  many  others,  long  since  fully  assimilated, which  really  originated  in  the  adoption  of  an  Indian  word,  or  the  modifica- tion of  an  Indian  proper  name.  Such  words  are  the  three  quoted  at  the beginning  of  these  remarks,  chintz,  calico,  gingham,  also  shawl,  bamboo,  pagoda^ typhoon,  m/msoon,  mandarin,  palanquin,f  &c.,  and  I  may  mention  among further  examples  which  may  perhaps  surprise  my  readers,  the  names  of  three of  the  boats  of  a  man-of-war,  viz.  the  cutter,  the  jolly-boat,  and  the  dijigy,  as all  (probably)  of  Indian  origin.!  Even  phrases  of  a  different  character — slang  indeed,  but  slang  generally  supposed  to  be  vernacular  as  well  as  vulgar — e.g,  'that  is  the  cheese* ;%  or  supposed  to  be  vernacular  and  profane — e,g, *I  don't  care  a  dam^X — are  in  reality,  however  vulgar  they  may  be,  neither vernacular  nor  profane,  but  phrases  turning  upon  innocent  Hindustani vocables.
314:Baboo  and  other  Tales,  descriptive  of Society  in  India.  Smith  k  Elder. London,  1834.  (By  Augustus  Prinsep, B.C.S.,  a  brother  of  James  and  H. Thoby  Prinsep.)
2383:BABOO.
2385:BABOOL.
2390:BABOO,  s.  Beng.  and  H.  BcOm [Skt.  wipra^  *a  father'].  Properly  a term  of  respect  attached  to  a  name, like  Mader  or  Mr,^  and  formerly  in some  parts  of  Hindustan  applied  to certain  persons  of  distinction.  Its application  as  a  term  of  respect  is now  almost  or  altogether  confined  to Lower  Ben^l  (though  C.  P.  Broni'n states  that  it  is  also  used  in  S.t  India for  *Sir,  My  lord,  your  Honour  \  In Bengal  ana  elsewhere,  among  Anglo- Indians,  it  is  often  used  with  a  slight savour  of  disparaffement,  as  characteriz- ing a  superncialiy  cultivated,  buti  too often  effeminate,  Bengali.  And the  extensive  employment  oj class,  to  which  the  term  was  a] as  a  title,  in  the  capacity  of  clei English  offices,  the  word  has often  to  signify  *a  native  clerk'  who writes  EngBsh.^
2392:1782,—** CwiUoo  Baboo"  appears  as  a subscriber  to  a  famine  fund  at  Madras  for 200  Sicca  Rupees.— /n<£ta  Gazettey  Oct.  12.
2397:1803.— *<.  .  .  Calling  on  Mr.  Neave  I found  there  Baboo  Dheep  Nanain,  brother to  Oodit  Narrain,  Rajah  at  Benares.'* — Lard ValaUia*8  Travels,  i.  112.
2398:1824. — **.  .  .  the  immense  oonvent-liko mansion  of  some  of  the  more  wealthy BaboOB.  .  ."-i7«5er,  i.  31,  ed.  1844.
=== AID
688:Baboo.  [Bengali,  bdbu,  perhaps  from the  Sanskrit  pitri ,   a   father.]  A term  of  respect  formerly  applied  in upper  India  to  the  younger  sons of  a   riji ;   in  a   Bengal  village  it  is the  usual  title  of  the  zaminddr ;   it is  also  appended  to  a   proper  name as  an  equivalent  to  ‘   mister ;   *   but among  the  English  it  is  chiefly  used to  denote  a   native  clerk  or  manager.
6010:SamAr.  [GujarAti.]  An  implement for  smoothing  soil ;   it  is  a   flat  piece of  wood,  usually  raen  or  bAbul, drawn  breadthwise  by  bullocks,  the driver  standing  on  it  to  increase  the weight.
```


## [2026-09-05T05:47:55.065Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 barbat\"; grep -n 'بربط' BQT_v1_pages.txt | head -10\necho \"=== MON part1 بربط\"; grep -n 'بربط' MON_part1.txt MON_part2.txt | head -10\necho \"=== MON بابو\"; grep -n 'بابو' MON_part1.txt | head -10"
}
```


### [2026-09-05T05:47:55.166Z] TOOL RESULT

```
=== BQT v1 barbat
16544:و درفن بربط لوازی ر موسیقی دأني عدیل ونظیر
18241:کوند بربط ساز عود است » وآن طنبور ماشدی
28830:تو نبوراکی بدست ومن عکی‌بربط بچنگه.
=== MON part1 بربط
MON_part2.txt:53709:مرغ سغدی: (منسوب به سغد). ( کد.) بربط. 
MON_part2.txt:55110:به معنی عود و بربط را اشتباه فرهنگ‌نویسان 
MON_part2.txt:61242:سودن - مص (ع.) + بربط - عود. مس + 
MON_part1.txt:73808:مانند چنگ» تاره بربط» قانون» ویولن. 
MON_part1.txt:93172:و بربط. رف شرت وتا 
MON_part1.txt:99032:اصل شبیه بربط بوده. در دورة اسلامی این 
=== MON بابو
2513:آتشین. ( گیا.) قسمی از گُل بابونه اقحوان. 
2515:بابونٌ کاو چشم. 
19574:باب: ۵80 ببا - بابو] (.) پدر بااء اب. 
19591:بابا: 0505 [- باب - بابو] (ا.) پدر؛ باب اب. 
19647:بابو: 205 رقس. باب] (.) پدر بابا. بزرگ 
19652:بابونه: (۵-)02ا0ق0 | بایونج؛ معر.] (.) 
26236:دارای رایبحه» بابوی. (امر.) سگ شکاری» 
29236:۳۸ فرهنگ فارسی ۵ بابور 
43107:(مضرنل:) ست شون بابود کفی دی کنده 
69136:بابو نه: روغنی که از «یایو نه» اهر او شود.
```


## [2026-09-05T05:48:04.212Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بابو context\"; sed -n '19570,19600p;19640,19660p' MON_part1.txt\necho \"=== LKT balalaika entry\"; sed -n '660,675p' LKT.txt\necho \"=== MON part1 head lines for page markers\"; grep -n '\\[pdf page' MON_part1.txt | head -3"
}
```


### [2026-09-05T05:48:04.299Z] TOOL RESULT

```
=== MON بابو context
گلگون. زیباه قشنگ 
بائت: ۰ .| اصا آنچه شبی بر 9 
گذشته شته باشد (از گوشت و نان و غیره)» شب 
مانده» بیات؟ مّ. تازه. 
باب: ۵80 ببا - بابو] (.) پدر بااء اب. 
بات: (ص.) درخور لایق» شایسته: 
باب فلانی است. مر سوم؛ معمول» مد: بات 
۰-به این دو 
معنی بصورت اضافه آید. طبقة دستة: 
توکربات.: باب دندان: غذای مطابق سسلیقه» 
هر چیز موافق با ذوق. باب طبع: مطابق طبع. 
بات مسحلی بودن: در آزیجا بازار رواج و 
مشتری بسیار داشتن 
ش 0 (ا.) ۳ معادل اک 
باب: (ع.] (.) در و دروازه. بخشی از 
کتاب که به فصل‌هاتءة یم شود. باره؛ 
خصوص. قسم؛» گونه. بارگاه سلاطین. 
(جف.) تنکه میان دو خشکی. تمام» به تمام) 
وا (شرع.) دعوت کننده دینی» داعی. 
(شیعه اثنی عشری): هر یکث از وکلای امام 
دوازدهمم در عغعست. (سعبه): علی سن 
بابا: 0505 [- باب - بابو] (ا.) پدر؛ باب اب. 
پدربزرگ. آدم ابوالبشر. امروز به پیرمردان 
نیز «بابا, اطلاق کنند. شخص: کس. . ضح.- 
در تخاطب به هر کسی (اعم از مرد و زن و 
کوچک و بزرکت) «بابا؛ گو بند. پدر فرزند 
را گاه به لفظ ریاباء خواند. عنوان عارفان و 


روره مد رور؟ مف. تابات. 


بابک: ۱2۳-۴ [مصف. باب] (.) پدر (به 
تحبیب). 

بابل: ۵1 (.) مغرب؛ مق. خراسان به 
معنی مشر ق. 

بابو: 205 رقس. باب] (.) پدر بابا. بزرگ 
قلندران و درویشان. به معنی بابا که در اوایل 
اسماء برای شفقت با مجرد تلقیب افزایند و 
گویند. 

بابونه: (۵-)02ا0ق0 | بایونج؛ معر.] (.) 


۳۳۴ 


فرهنگ فارسی معین بایی 


=== LKT balalaika entry
195.  Mal.  baläcau:
^Vorspeise  aus  gesalzenen  und  dann  ge- stampften und  getrockneten  Fischchen oder  dergl.'  [Pijn  38  a];  hieraus  anglo- ind. balachong,  blachong,  die  charakte- ristische Speise  der  indochinesischen  und malayischen  Völker.  [Dass.  wie  hier Nr.  286.]    [Hobson-Jobson  51.
196.  Ar.  balad:
'Land',  Adj.  dazu  baladl  'ländlich,  ein- heimisch'; hieraus  mit  leicht  verständ- lichem Bedeutungswechsel  sp.  baladi 'wertlos,  gering'.    [DE  202/3.
197.  Pers.  bälähäuä:
[Aus  pers.  bälä  'hoch'  Horn  NpEt  S.  39, Nr.  171  und  pers.  hänä  'Haus'  ebenda S.  103,  Nr.  465;  also  eigentlich  'Hoch- haus'] 'ein  oberes  Zimmer,  hervorstehen- der Teil  des  Hauses,  Erker,  Balkon'; hieraus  mit  vielfachen  Kontaminationen ähnlich  bedeutender  Wörter  und  unter volksetymologischen  Einflüssen  it.  bar- ■bucane  'Brustwehr  mit  Schießscharten, Stützmauer',  prov.  barbacana,  frz.  bar- bacane  'Schießscharte',  kat.  barbacana ''Fensterdach,  Dachvorsprung',  sp.  bar- bacana und  pg.  barbacäa  'Außen werk
Lolcotsch,  Etymolog.  Wörterbuch.
einer  Feslunii'.  Wenn  Löbel  EITAP  11 diese  Ableitung  mit  mehr  als  einem Schein  von  Recht  elimologia  indoiosä nennt,  so  sind  die  folgenden  Wörter aus  semantischen  Gründen  unzweifel- haft aus  dem  angegebenen  Grundwort abzuleiten  und  Annahme  eines  ahd. palco  'Balken'  als  Grundwort  abzuleh- nen: it.  balcotie,  frz.  balcon,  rum.  halcon, sp.  balcÖH,  pg.  balcäo;  dtsch.  Balkon, engl,  balconi/;  russ.  bulg.  serb.  poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890.
198.  Tat.  balaliiika:
'Laute' ;  hieraus  russ.  halalaika,  klr. balabaika,  serb.  balalajka,  öech.  bala- lajka  'russische  Zither  oder  Laute  mit zwei  oder  drei  Saiten' ;  frz.  la  balale'ika, dtsch.  Balalaika.    [Gorjajew  10.
199.  Mongrol.  balamnt:
Hieraus  russ.  balamut,  öech.  balanmt, poln.  balamut  'Schwätzer,  Klatsch  er' ; Tum.  balamut  'dumm'.  Dazu  auch  Verba: russ.  balamutit' ,  Cech.  balamutiti,  poln. balamucic  und  mit  Abstoßung  der ersten  Silben:  bulg.  mUja,  serb.  mutiti 'verwirren,  trüben'.    [Gorjajew  10.
200.  Ar.  balät: Einheitsnomen  baläta  'glattes  Pflaster, breiter  Stein  zum  Pflastern,  Quader'; hieraus  siz.  balata  'die  lastra,  d.  h.  ein harter,  viereckiger  Stein  zum  Einram- men der  Pflastersteine'.
201.  Tk.  balbaäy:
Aus  tk.  hal  'Honig'  und  bas  'Kopf, eigentlich  'Honigkopf',  hieraus  rum. balba^,  baba§  'Honigwasser'.  —  Aus  tk. balgy  'Honigverkäufer'  wird  rum.  balgiü 'dass.'.  —  Tk.  bal-jemez  'der  nicht  Honig ißt  oder  frißt'  ist  Bezeichnung  für  ein Geschütz  großen  Kalibers,  vgl.  v.  Moltke, Briefe  über  Zustände  und  Begebenheiten in  der  Türkei.^  1876.  S.  260  im  Briefe vom  12.  Mai  08.  Hieraus  rum.  balimez, baliemez  'großkalibriges  Geschütz'.  Hier- von kommt  sicherlich  auch  der  luia. Ausdruck  a  face  talme§  bahiief  'krumm und  lahm  schlagen'.
202.  Tat.  balda:
=== MON part1 head lines for page markers
```


## [2026-09-05T05:48:04.575Z] TOOL CALL #15: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T05:48:04.582Z] TOOL RESULT

```


```


## [2026-09-05T05:48:11.844Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%A8%D8%B7",
 "prompt": "Give the full etymology sections for Persian بربط (barbat) and Arabic بربط: what is the origin (Middle Persian barbut? Greek barbitos? bar+bat 'duck-breast'?), and any cited scholars."
}
```


## [2026-09-05T05:48:14.474Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B2%CE%AC%CF%81%CE%B2%CE%B9%CF%84%CE%BF%CF%82",
 "prompt": "Full etymology of Ancient Greek βάρβιτος: is it of foreign/Pre-Greek origin, linked to Persian barbat, or to barbaros? Quote what is said and any scholars cited (Beekes, Chantraine)."
}
```


### [2026-09-05T05:48:17.452Z] TOOL RESULT

```
# Etymology of بربط (Barbat)

## Persian بربط

Based on the Wiktionary article provided, the Persian term has a clear documented origin:

**Etymology:** The word is "inherited from Middle Persian [barbut] ('lyre'), from Ancient Greek _bárbitos_."

The article cites D. N. MacKenzie's 1971 *Concise Pahlavi Dictionary* (Oxford University Press, page 17) as a reference for the Middle Persian form "barbut."

The etymological chain is: Ancient Greek βάρβιτος (bárbitos) → Middle Persian barbut → Persian بربط (barbat)

## Arabic بربط

The webpage provided contains **only** the Persian entry. There is no Arabic etymology section included in this content, so I cannot provide cited information about an Arabic origin based on the source material given.

To obtain Arabic etymology information, you would need to consult a separate Arabic Wiktionary entry or Arabic lexicographical sources.
```


### [2026-09-05T05:48:20.196Z] TOOL RESULT

```
# Etymology of Ancient Greek βάρβιτος

Based on the Wiktionary entry, the origin is described as follows:

**Etymology Statement:** "Uncertain, probably from Phrygian."

The article provides no detailed discussion of competing etymological theories, nor does it cite specific scholars like Beekes or Chantraine discussing connections to Persian *barbat* or Greek *barbaros*. 

However, the **Descendants section** indicates a possible later connection to Persian languages: "→ Middle Persian: [script needed] (blbwt' /⁠barbut, barbat⁠/, 'barbat, lute') (possibly)" — suggesting the Persian form may derive from the Greek word rather than the reverse.

The References section cites Beekes's *Etymological Dictionary of Greek* (2010, page 201), but the content of that citation is not reproduced in this excerpt. The entry thus acknowledges Phrygian origin as most probable while leaving the question ultimately unresolved.
```


## [2026-09-05T05:48:25.853Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/barbat-an-old-persian-musical-instrument",
 "prompt": "Summarize what the Encyclopaedia Iranica says about the etymology and history of barbaṭ: Middle Persian barbut, relation to Greek barbitos, the 'bar-bat / duck-breast' folk etymology, and any scholars cited."
}
```


## [2026-09-05T05:48:26.790Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/baboon",
 "prompt": "Full etymology of baboon; also quote what it says about Old French babine / baboue and any alternative (Arabic maimun) theory."
}
```


### [2026-09-05T05:48:27.809Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T05:48:32.967Z] TOOL RESULT

```
# Etymology of Baboon

The word "baboon" entered English around 1400 from French *babouin*, which derives from Old French *baboin* meaning "ape" but earlier referring to "simpleton, dimwit, fool" and "gaping figure (such as a gargoyle)."

**Possible origins:**

The etymology suggests two theories. First, it may stem from Old French *baboue* meaning "grimacing." Second, scholars propose it could be "imitative of an ape's babbling speech-like cries."

**Alternative theory:**

The dictionary notes that "Arabic *maimun* probably is from the European words," suggesting the Arabic term may have actually derived from European languages rather than the reverse.

The word's path through European languages is also documented: German *Pavian* came via Dutch *baviaan*, from Middle Dutch *baubijn*, which borrowed the Old French term.
```


## [2026-09-05T05:48:37.888Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/brave",
 "prompt": "Full etymology of brave and of bravo (interjection): Italian bravo, Latin barbarus vs pravus, and what Etymonline prefers."
}
```


## [2026-09-05T05:48:39.047Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/balalaika",
 "prompt": "Etymology of balalaika: Russian origin, relation to balabolit'/balakat', any Turkic/Tatar theory."
}
```


### [2026-09-05T05:48:43.961Z] TOOL RESULT

```
# Etymology of "Brave" and "Bravo"

## Brave (Adjective)
The word "brave" entered English in the late 15th century from French *brave*, meaning "splendid, valiant," which derived from Italian *bravo* meaning "brave, bold" (originally "wild, savage"). The origin remains uncertain, though scholars have proposed several theories:

- **Latin connection**: Possibly from Medieval Latin *bravus* ("cutthroat, villain"), connected to Latin *pravus* ("crooked, depraved")
- **Alternative theory**: Less likely connection to Latin *barbarus* (meaning "foreign")
- **Celtic possibility**: Irish *breagh* and Cornish *bray* have been suggested

The entry notes that "a confusion of two or more words" may have occurred during transmission.

## Bravo (Interjection)
The exclamation "bravo!" emerged around 1761 from Italian *bravo*, literally meaning "brave." Interestingly, the noun form appeared earlier (1590s) to denote "desperado, hired killer."

## Key Distinction
Etymonline doesn't strongly endorse any single origin theory, presenting multiple possibilities without declaring one definitively correct, acknowledging the word's uncertain etymology and potential linguistic contamination.
```


### [2026-09-05T05:48:44.431Z] TOOL RESULT

```
# Balalaika: Etymology and Origins

Based on the Wiktionary entry, the balalaika's etymology is straightforward:

**Russian Origin**: The word derives directly from Russian. The English entry states: "From Russian _балала́йка_ (balalájka)."

**No Turkic/Tatar Theory Mentioned**: The provided content does not discuss any Turkic or Tatar etymological theories for the instrument's name. The article only confirms Russian as the source language for the term used across multiple languages.

**Instrument Description**: The balalaika is defined as "a plucked stringed instrument with a triangular body, short neck and three strings, of Russian origin."

The Wiktionary entry focuses on documenting the term's current usage across 29 languages rather than exploring disputed historical origins of the word itself.
```


## [2026-09-05T05:48:54.271Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT ctx 16544\"; sed -n '16500,16560p' BQT_v1_pages.txt | grep -n '' | tail -50\necho \"=== nearest pdf page tag before 16544\"; awk 'NR<=16544 && /\\[pdf page/ {p=$0; n=NR} END{print n, p}' BQT_v1_pages.txt\necho \"=== ctx 18241\"; awk 'NR<=18241 && /\\[pdf page/ {p=$0; n=NR} END{print n,p}' BQT_v1_pages.txt; sed -n '18225,18260p' BQT_v1_pages.txt"
}
```


## [2026-09-05T05:48:55.797Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D0%B1%D0%B0%D0%BB%D0%B0%D0%BB%D0%B0%D0%B9%D0%BA%D0%B0",
 "prompt": "Etymology of Russian балалайка: what is it derived from (балакать, балаболить, imitative)? Quote and note cited sources such as Vasmer."
}
```


### [2026-09-05T05:48:56.066Z] TOOL RESULT

```
=== BQT ctx 16544
12:غم و اندوه و کناه بسیار باشد همچو: با رگیری
13:محتس بفال و نان‌با و قصاب و امثال آنهاراودزد
14:بابارگرفته . ۱٩‏ - اباری راگویند که بجپت
15:قوت زراعت بی زمین کم زور ربزند ۰ ۱۷ - ساز
16:هابی که طربان نوازند همجو : فانون و طتبور
17:و ماد آن ۰ ۱۸ - آرد بواج وارژن (۲) باشد
18:که بجهت بوزه مهیا ساخته باشند و.هئوز آنرا
19:صاف نکرده باشند ۰ ۱٩‏ - نام دهی‌است ازولابت
20:طوی*۱ . ۲۰ آنچه‌یا زر ونقره در کدازنهند .
21:۱ آنچه نوسن دکان‌وسند . ۲۲ - هرچیر
22:که آنرا خورند . ۲۳ - شاخ را گونند . ۲۶ -
23:پار اب ه بر وزن و معتی راب پاشد »
24:و آن تاحیه‌ایت مشهور و وسیم‌در ماورلعالهر-
25:و زراعتی را یز کویند کماز آب رودخانه وکارز
26:حاصل شده باشد . *
27:(۱) چب ۰۱ چش : چافشر . (۲) چك : لران:
28:0۶ نز : رك : شمار؛ هفت و حضت پبکر لظامی ص ۲۳ . ۴ ور پپلوی‎ - ٩
29:«مناس ۲۲۹8 از مصبر 087 اوستایی بممنی بردن ؛ در سمتالی و سشکسری و سرخة و لاسگردی‎
30:: و شهمیرزادی 02 . ۲ ص ۱۹۱» کیلکی حمچنن . ۴ رك: بارخدا‎
31:۲ زبات خمش نگشت از فول دهد بار اطق ایزدبار . . اثیرآلدین .
32:۴ - در پهلوی یز ۵8 چنانکه 6۷2۲ بممنی‌یکبار «منای ۲۷۳و ۵1025 بمعنی دو باراست
33:«منای ۰۲۷۲ «تیبر که ۰۳۲ طبری ۷2۲ «واژه‌نامه ۰۰۷۷۲ کیلکی ۷8۴ . بهلوی
34:نیز ۵۲ (ساحل) [رك : نب که ۳۷ 0۵۲۰ دوم] ورك : صء لد از دیباچة مولف  .‏ ۱ - از
35:مصدر باربدن. . .۰ ۷ کیلکی۲۸۷8 (بیار).
36:٩‏ - که بارت‌شده براوج عیغ کنگر؛ ضرت‌زده پراوج تبغ . امیرخسرو دهلوی .
37:مصحف با ( ۵ . م) . شه درصفحه ۲۱۵
38:۵ رك : بر .مج وا
39:باران بر س رگذارند - ۶ حر چیزی راکه تجهت
40:مانع باران پوشند پیز کویشف - و نم قبیلهایست
41:از ترکان .
42:پار ید ۱ د بت بای ابید رسکون‌دال
43:بی نقطه , نام مطرب خسروپرویز است : گویند
44:اصل او از جهرم بوده که از توابم شیراز است
45:و درفن بربط لوازی ر موسیقی دأني عدیل ونظیر
46:نداشته و سرود مسجع از مخترعات اوست وان
47:سرود را خسروالی فلم هاده بود ۰ و بفتح بای
48:ایچد هم آمذه ات .
49:انگور باشد و آفرا بتازی عنب‌التعلبکوند .
50:پاار جا « پروزن پارسا. بمعنی‌بار گاه
51:است که محل بار ملوك و سلاطی باشد .
52:بار جامه» پروزن کاردامه » جوالی را
53:کوب د که ههن آن از پهلو باشد و بربالای‌چارزا
54:اندازند و حرچیز خواهند درآ ن کنند .
55:پار خدا - حمعالیاکوینجل‌جلاله
56:- ویادشاهان‌پز رکه واولی‌الامر- وصاحب‌وخداوند
57:ممنی‌بارخدا خوانند؛ و آن‌لفظی‌است م کب بممنی
58:(۱) چش : خورجی .
59:بارطاربون
60:خدای بز رکه ۱
61:بار دان- بروزن کاردل ۰ خرجن (۱)
=== nearest pdf page tag before 16544
 
=== ctx 18241
 
نیز گوبند - و بعرمی نلم ولابتی است در عغرب
که مردم آنجا سبزچهره میباشنه ۷ .
بر پروشان ۴ با بای فارسی بروزن
پرده پوشان . مطلق امت راکوندازهر بیفمبری
که باشد .
بر لست " با سین بی تفمله بروزن‌سر مست»
بمعنی طرز و روش و قاعده و قانون باشد ۳ .
بر بستگان - بروزن‌سربتکان » جمع
بر لسته - بروزن‌برجته » تقیض‌بررسته
است و آن چیزیرا گوین که روح نبانی در وی
اثر نکند و نشو و نما تتواند کرد وژداوه از ا نسعه
مت تواند شد , مانند بعضی از جمادات که
برجورب
سنگه و کلوخ و امثال آن باشد . ۱
بر ابص  *‏ بتح ال و سکون تن یکه
طای حعلی باشد ۰ نام سازست مهور » و بستی
کوند بربط ساز عود است » وآن طنبور ماشدی
باشد کاسه بز رکه و دسته کویاه .
ر لگ ع بروزن سربند » سینه‌ندطفلان
و پستان بند زنان باشد, چه بر بمعنی پستان هم
بر ود ۲« با بای‌فارسی‌بروزن‌زردوزه
برامون دهان چرندکان ومنقار پرند گان‌باشد .
بر یوس ۱ - با بای فارسی بر وزن
پریدکان باشد .
و ۱ دقیفةٌ عرض شمالی وطول ۳۳ درجه و ۵٩‏ دقیقةٌ شرقی کربنویج » و این‌شهر کلیدسودان بشمار
آبد - قوم بربر امروز هم مانند فرون اوگ اسلام دارای وحدت متجاس نیستند . عنصر الب
آنان همواره در افربقای شمالی مسکن داشتند ولی با عرب مضلوط شدند واغلب تمیز آنان‌مشکل
است : کروه های بسیار از ابشان در کوهها و صحراها زست کنند و مراکز آنان طرابلی و برقه
و توص و الجزایر و مرا کش است . رك : داثرةالمعارف اسللام . بونالیان و رومیان 82708785
را بهمهٌ ملل غبر ازملت خوش اطلاق میکردند. ۴ - این‌کلمهتصحیف <بر روشنان*دقیفی
است. اسدنی درلعت فرس (ص۳۵۸) کوید : ۱برروشنان امت بود . دقیقی .کومد:
شفیم باش برشه مرا بدین زلت چو مسطفی بر دادار بر روشنانرا .»
این کلمه در پهلوی ۷2۵۲۳/150/620 بمعنی مزّمنان ‏ وکروند کان است. بردوی سکه‌ای که در
دارابگرد فاری بنلم عدامهین زیر - آادگاه که بغلافت برخاسنه بود - بال ٩۵‏ حجری نرب
شده اين جملةٌ پهلوی ثبت شدء :
لري پ زید چم برس توس
```


### [2026-09-05T05:49:01.763Z] TOOL RESULT

```
# Etymology of Russian балалайка

According to the Wiktionary entry, the Russian word **балалайка** derives from dialectal **балабайка**, which comes from an onomatopoetic root **балабай-** plus the diminutive suffix **-ка**.

The entry states: "From dialectal _балабайка_ (balabájka), from onomatopoetic _балабай-_ (balabaj-) +‎ _-ка_ (-ka)."

The source also notes related Russian words for comparison, including **балаболить** (balabónitʹ), **балагурить** (balagúritʹ), and **балакать** (balákatʹ), suggesting a broader family of imitative terms.

However, the provided Wiktionary page does **not cite Vasmer's etymological dictionary** or other specific scholarly sources beyond noting the onomatopoetic origin and dialectal variants. For detailed etymological analysis with academic citations, consulting Vasmer's dictionary directly would be necessary.
```


## [2026-09-05T05:49:11.750Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c $'\\f' BQT_v1_pages.txt; grep -n 'pdf page' BQT_v1_pages.txt | head -3\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\np=t.find('نام سازست')\nprint('leaf', t[:p].count('\\f'))\npg=t.split('\\f')\ni=t[:p].count('\\f')\nprint(repr(pg[i][:200]))\nprint('---END---')\nprint(repr(pg[i][-300:]))\nEOF"
}
```


### [2026-09-05T05:49:13.310Z] TOOL RESULT

```
766
leaf 469
'تب ۷46 سه\nنیز گوبند - و بعرمی نلم ولابتی است در عغرب\nکه مردم آنجا سبزچهره میباشنه ۷ .\nبر پروشان ۴ با بای فارسی بروزن\nپرده پوشان . مطلق امت راکوندازهر بیفمبری\nکه باشد .\nبر لست " با سین بی تفمله بروزن\u200cس'
---END---
'ن جملةٌ پهلوی ثبت شدء :\nلري پ زید چم برس توس\n۲۳۷۸۵۸۷ ۷۷- [ ۸۱۷۲1 اب۸0\nیمنی عبداةٌ امیرالمومنین . رث : ۱ ۱\n0 صیمین )۸ طعنات۲ عظ؛ جوز فوامی ممفصوصدهات ۱۲ عط ۵۲ منو\u200cداهای) ۸\n6۵۷ )۳۵۵۵۵ ده کادء\u200cمهم : 33. ۵ , 1941 م۵0عما۱ . ۷۷2۱۴۵۲ صداهز\n,5 . ۵ ,1872 1۵0008 , ۲۳۵۴8۵8 ۰ 4 زرد , کامتعطم۵(]\nبقبه درصفحهٌ ۲۵۰'
```


## [2026-09-05T05:49:19.979Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npg=t.split('\\f')\nprint(pg[469])\nEOF"
}
```


### [2026-09-05T05:49:21.818Z] TOOL RESULT

```
تب ۷46 سه
نیز گوبند - و بعرمی نلم ولابتی است در عغرب
که مردم آنجا سبزچهره میباشنه ۷ .
بر پروشان ۴ با بای فارسی بروزن
پرده پوشان . مطلق امت راکوندازهر بیفمبری
که باشد .
بر لست " با سین بی تفمله بروزن‌سر مست»
بمعنی طرز و روش و قاعده و قانون باشد ۳ .
بر بستگان - بروزن‌سربتکان » جمع
بر لسته - بروزن‌برجته » تقیض‌بررسته
است و آن چیزیرا گوین که روح نبانی در وی
اثر نکند و نشو و نما تتواند کرد وژداوه از ا نسعه
مت تواند شد , مانند بعضی از جمادات که
برجورب
سنگه و کلوخ و امثال آن باشد . ۱
بر ابص  *‏ بتح ال و سکون تن یکه
طای حعلی باشد ۰ نام سازست مهور » و بستی
کوند بربط ساز عود است » وآن طنبور ماشدی
باشد کاسه بز رکه و دسته کویاه .
ر لگ ع بروزن سربند » سینه‌ندطفلان
و پستان بند زنان باشد, چه بر بمعنی پستان هم
بر ود ۲« با بای‌فارسی‌بروزن‌زردوزه
برامون دهان چرندکان ومنقار پرند گان‌باشد .
بر یوس ۱ - با بای فارسی بر وزن
پریدکان باشد .
و ۱ دقیفةٌ عرض شمالی وطول ۳۳ درجه و ۵٩‏ دقیقةٌ شرقی کربنویج » و این‌شهر کلیدسودان بشمار
آبد - قوم بربر امروز هم مانند فرون اوگ اسلام دارای وحدت متجاس نیستند . عنصر الب
آنان همواره در افربقای شمالی مسکن داشتند ولی با عرب مضلوط شدند واغلب تمیز آنان‌مشکل
است : کروه های بسیار از ابشان در کوهها و صحراها زست کنند و مراکز آنان طرابلی و برقه
و توص و الجزایر و مرا کش است . رك : داثرةالمعارف اسللام . بونالیان و رومیان 82708785
را بهمهٌ ملل غبر ازملت خوش اطلاق میکردند. ۴ - این‌کلمهتصحیف <بر روشنان*دقیفی
است. اسدنی درلعت فرس (ص۳۵۸) کوید : ۱برروشنان امت بود . دقیقی .کومد:
شفیم باش برشه مرا بدین زلت چو مسطفی بر دادار بر روشنانرا .»
این کلمه در پهلوی ۷2۵۲۳/150/620 بمعنی مزّمنان ‏ وکروند کان است. بردوی سکه‌ای که در
دارابگرد فاری بنلم عدامهین زیر - آادگاه که بغلافت برخاسنه بود - بال ٩۵‏ حجری نرب
شده اين جملةٌ پهلوی ثبت شدء :
لري پ زید چم برس توس
۲۳۷۸۵۸۷ ۷۷- [ ۸۱۷۲1 اب۸0
یمنی عبداةٌ امیرالمومنین . رث : ۱ ۱
0 صیمین )۸ طعنات۲ عظ؛ جوز فوامی ممفصوصدهات ۱۲ عط ۵۲ منو‌داهای) ۸
6۵۷ )۳۵۵۵۵ ده کادء‌مهم : 33. ۵ , 1941 م۵0عما۱ . ۷۷2۱۴۵۲ صداهز
,5 . ۵ ,1872 1۵0008 , ۲۳۵۴8۵8 ۰ 4 زرد , کامتعطم۵(]
بقبه درصفحهٌ ۲۵۰
```


## [2026-09-05T05:49:30.124Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:249 --image 2>&1 | tail -40"
}
```


### [2026-09-05T05:49:31.892Z] TOOL RESULT

```
no scan of BQT covers printed page 249 (see 'scans' in refs_online.json)
```


## [2026-09-05T05:49:38.398Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npg=t.split('\\f')\nprint(pg[470][-1800:])\nEOF"
}
```


### [2026-09-05T05:49:40.225Z] TOOL RESULT

```
ن سرتراشك » بممنی برناشك أست .
بر لنگه - بروزن خرچنگهه . تشگهدوم
باشد از زین اسب - و نوار ماتتدیرا نز گونه
که از کربای و غیرمدوزند و بر ؟پوار؛ًاطفال نصب
۳9 و طفل را بدان در کهواره ند ند - ونوعی
از بارچهُ کم عرض هم هت .
بر ننی ۴ بروزن کردنی » غروروتکبر
و تجمر باشد .
بر نه بروزن شرطه » نام بر نوابه(۱)
است که مبارزی بوده ازابراتبان .
۱ پر یبا - با فوفانی بتحتانی رسیده و بای
ابجد با فکشیده » بزبان زند وپازند (۲)پرمتوله
رااگویتد و آن پرنده‌ایست معروف .
بر ج < بفتع اول و انی وسکون جیم »
رستلی باش دکه آنرااگر ثرکی خوانند ۴ .
بر چاس - بنم‌اول و سکون ثالی‌وجيم
ثیر را گویند و عرب آنرا .که در هوا نشانهٌ تبر
۳ تاشك - مین معجمه و کاف بروژن
قردائب , گیاهی که آترا بوی مادران گویند
ویعربی شوبلا خوانند. :
(۱) چك : توابه . (۲) چك : ژند و باژند .
برطاسی بدیشان سبت دارد ؛ و آنان پیومته و ترديك بخزران باشند. وبین آندو قوم امتی دمگر
نیست. و ايشان در وادی انل باشند. برطای امن ناحیه و شهری است ودردم آن مسلمانند ومسجد
جامم دارند و نزديك بدان شهری‌است ینام «سوار» و اهل برطای را زبانی مشخص است که تر کی :
و خزری و للغاری بت . «ممج‌البلدان» رك : برطاس. 4 - بازند 2۷2۲۵۵ ارحنی
280۲ * اسفا!: ۸۰۲ *. ۴ - برح ( م‌اول ) از تازی» از بونانی ۳۷۲805
بمعنی حصار و قلمه « تفس» -
بقیه ازصمحهُ ۲٩‏
دراسناد پهلوی نورفان‌اسم مصدرا۷/۵۳۱۷/۱511 (< کروش) آمده. ویرویشینکان جمع وبروشنيك
(-<* کروشی < موّمن ) است و فاعدة در فارسی باید کروشیان و با (بقاعدءت,دیل کاف‌بیاء)بروشیان
شود ولی این‌کلمه را دفیقی «بررو‌شنان» و دیگران بصور برپروشان » پرپروشان: و غیرهآورده‌اند.
اینکه در حائيةٌ لفت فری چاپ اخیر (س ۳۵۸) کلمه را به < بد روشن » صحیح کرده‌اند صحیح
تست . ره : مجلهٌ موسیةی سال ۳ شمارة ۸ مقالةً س . هدایت و رل : مزدیستا۳۲۱ ح .
۳ ۴ رگ :.فرهنگه دسانیر ص ۷۳۵ . ۵ - پپلوی )تا02۲0 از بونانی
۵5 «اونوالا 4۰۵»کمةٌ بونانی بعدها در زبانهای فرتگی 092801008 کردیده (رك :مجله
موسیقی]] ی ۷ ص ۲ ح ۱). ۱- مسحف «بدپوز» . رث : بدپوز » بتفوز » پتفوز .
```


## [2026-09-05T05:50:06.331Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 MON_part1.txt; echo ...; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (19647,93172):\n    print('=== around line',ln)\n    print('\\n'.join(lines[ln-14:ln+12]))\nEOF"
}
```


### [2026-09-05T05:50:08.066Z] TOOL RESULT

```
0 
2 


چم 
...
=== around line 19647
برای کودکان آرد؛ نظیر پاپا نوئل مسیحیان. 
بابت: ۱1 اغ. بابة ] (.) شایسته» سزاواره 
از در» درخور. از بات در حصوص؛ در 
عوض. به حساب. همطراز» همسر » نظیر . 
بایزن: ۱0 )۱( سیخ کباب خواه آهت 
باشد یا چوبی. 

بابک: ۱2۳-۴ [مصف. باب] (.) پدر (به 
تحبیب). 

بابل: ۵1 (.) مغرب؛ مق. خراسان به 
معنی مشر ق. 

بابو: 205 رقس. باب] (.) پدر بابا. بزرگ 
قلندران و درویشان. به معنی بابا که در اوایل 
اسماء برای شفقت با مجرد تلقیب افزایند و 
گویند. 

بابونه: (۵-)02ا0ق0 | بایونج؛ معر.] (.) 


۳۳۴ 


فرهنگ فارسی معین بایی 

=== around line 93172


اپوانی که توی ایوان بزرگتر باشد. تالار. 
اطاقی وسیع و مجلل نظیر شاه‌نشین. 

طنز: معا [ع. )] (مصم.) افسوس کردن» 
مسخره کردن. طعنه زدن» سرزنش کردن. 
(امص.) مسخره. طعنه» سرزنش. (.) ناز. 
طنزکنان: «قمه.۱ [ع. ف.] (ص‌فا. حا.) 
در حال از و کرشمه کردن. 

طنطنه: : (ع-)02هاه۱ [ع. . طنطنه ] (عص م.) به 
آواز آوردن طشت و جز و (.) بانگ رود 
و بربط. رف شرت وتا 
طنفسه: (م)معهتهها [ع. طنفسه ] (مص‌ل.) 


زشت خوی گردید پس از نیکخویی (عم.) 
پوشیدن جامه‌های بسیار (غم.) 

طنفسه: (می‌معدنمها [ع. طنفسة» معر.] (.) 
بوریا مانندی از شاخة خرما بر پهنای یکك 
گزء زیلوء فرش. نهالی» توشکک. جامه؛ ج. 
طنافس. 

طنین: «لهها (ع. ۰ (مسص‌ل.) آواز کردن
```


## [2026-09-05T05:50:25.464Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'بربط\\|بربت\\|بربص\\|بریط' MON_part1.txt | head -20; echo \"--- search 'برب' headword-ish\"; grep -n '^بر' MON_part1.txt | sed -n '1,60p'"
}
```


### [2026-09-05T05:50:25.556Z] TOOL RESULT

```
47236:بسیگانگی. ممتاز بودن؛ استباز. غبربت» 
73808:مانند چنگ» تاره بربط» قانون» ویولن. 
93172:و بربط. رف شرت وتا 
99032:اصل شبیه بربط بوده. در دورة اسلامی این 
--- search 'برب' headword-ish
423:بر ی ی 
889:بر (به روی) سر ریختن: (عم.) توبه کردن. 
1031:برند و به فشار آب در آن کنند؛ آب‌دزدکک. 
1267:برای سخت کردن آهن و آن فرو بردن فلز 
1271:بر کان دهد. خادمی که وی تهب 
1277:بر نده» تیز. صاحب سامان و مالدار» صاحبت 
1342:برنج که با آب کار کند؛ دنگی که به نیروی 
1352:برای اندودن دیوارها بکار می‌رود؛ دوغاب. 
1451:بر ومنك. 
1521:برای زراعت. 
1674:برآوردن آب از چاه و مانند آن با دلو. حمل 
1753:بر که. مرداب. حوض. دریا: بحر. (زم.) تمام 
1868:بروانه‌واران که در هند و مادا گاسکار و 
1912:بردارند؛ مق. دیم» دیمی. مثلث زراعت: 
2107:بر روی آتش در مواقع ایجاد حریق» بکار 
2154:بر آید» آروع. آرغ. 
2204:بردارند» شاه کیش می‌شود. 
2229:برافراشتن» بالا بردن: سر تاجشان بر سپهر 
2233:بررآورده» کشیده, رون کشده» تیغ آخته. 
2236:برافراشته» بالا برده» مرفوع. بر دوخته به 
2363:برفی: مجسمه و هیکل انسانی که از برف 
2560:برگ‌های زبادی درخت «بیراستن». نطم 
2710:برای نسواخستن آلات زهسی (ویولون» 
2896:برآمدگی کوچکد. گوشتین به رنگ 
3044:بر هم نهاده و سنگ زیرین در میان میلی 
3769:برای شکار حشرات دارد و دمش بر خلاف 
3920:برادر پدر» عم» عمو عفق: هرس بر کف 
3969:برای تهيةٌ مقاطع گیاهی در آزماشگاه‌ها 
4017:برند» برای نشان دادن نقاط مشترکی که 
4039:بر» مملو؛» ممتلی. حشو در نهاده, آکند نهاده. 
4148:برجستگی کو چکك در سافه با ريشة کیاه 
4270:برهم نهادة متقاطع که دو کس بر دو سر 
4414:برقوق. 
4543:برای روبت و ان‌برای اندازه فیری زوابا 
4893:برخاست. مباشرت» آرمش» نزدیکی کردن 
4935:بر سر ۰ نودن. بر 1 بودن. 
4978:بر زمان: علاوه بر هام به «- آن)» جمع بسته 
4988:برای اشخاص دوره اشان؛ مق. اینان. 
5017:برای تقو بت دستگاه‌های فر ستندة امواج 
5163:برافتاده. (ا.) هرج و مرج» بی‌نطمی» فساد. 
5208:براستی. 
5250:برنجن. خلخال» پای آور نجن. 
5261:بر اهه. 
5388:براق شو ده شوی» ؛ بت» آش جامه. 
5428:بردباری. 
5591:برافراشتن. راست کردن ستیخ کردن. 
5621:برهان. هر عبارت قرآن که بدان وقف کنند. 
6061:برآوردن» نو چیزی آوردن, نو آوردن؛ نو 
6099:برای دفع شقل و سنگینی. یکی از اقسام 
6130:بر آید. ابر بهار» ابر بهاری: ابری که در فصل 
6166:برآوردن. سخت تافتن ریسمان و جامه را 
6220:بر ابرو افکندن یا انداختن» چین آوردن 
6255:بروانه‌واران که کونه‌ای ار ان در جنل‌های 
6572:برگ‌هایش پایه متقابل» فشرده بهم در چهار 
6575:برگ‌هایش و حتی دستگاه‌های تولید مثلش 
6765:برگرفتن» فرا گرفتن. اتخاذ سند: استناد به 
6825:بر وجهی که ممکن باشد فرض اجزاء 
6923:بردن یا معیوب ساختن مال غیر بطور مستقیم 
6927:برنگرفتن. 
6996:برای حمل مسافران دسته جمعی بکار رود.
```


## [2026-09-05T05:50:27.036Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%B1%D8%A8%D8%B7/",
 "prompt": "Quote the فرهنگ معین entry for بربط (including any bracketed origin tag such as [په.] or [يو.]), and the دهخدا entry's etymology if present."
}
```


### [2026-09-05T05:50:34.308Z] TOOL RESULT

```
# Barbat Entry Summary

**From Farhang-e Moein:**
"(بَ بَ) [معر.] (اِ.) عود، از آلات موسیقی شبیه تار که کاسه اش بزرگتر و دسته اش کوتاه تر است"

This defines barbat as a musical instrument resembling a lute, with a larger resonance chamber and shorter neck than comparable instruments.

**Etymology from Dehkhoda:**
The Dehkhoda dictionary traces the word's origins to "بربت" (barbat), stating it derives from a compound: "بر" (breast) + "بت" (duck), because the instrument's shape resembles a waterfowl's chest. The entry notes this is an Arabicized Persian term, with the instrument comprising four strings: the thickest called "bam," followed by "moslls," "mosanna," and the thinnest called "zir." It notes the Arabs called this instrument "oud."
```


## [2026-09-05T05:50:48.908Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 baba\"; grep -n -i -E 'baba-|balbal|barbar' incoming/WLD/WLD_Bd2_pages.txt | head -15\necho \"=== IEC\"; grep -n -i -E '^ *baba|barbaros|barbaro|bambino' IEC.txt | head -10\necho \"=== SYN\"; grep -n -i -E 'barbaros|barbarus|foreign' SYN.txt | head -8"
}
```


### [2026-09-05T05:50:49.010Z] TOOL RESULT

```
=== WLD Bd2 baba
6893:   "^balbal- {babal-; bambal-, woraus bam-b-, bal-b- u. dgl.):
6912:   Mit -r-:      barbara-h „stammelnd, pi. Bezeichnung nichtarischer Yolker,
6916:barbartis), ^ag^agopcovog „von unverstandlicher Sprache" (kaum nach Weid-
6917:ner GL 4, 303 f. aus einem babylon. barbaru „Fremder, womit die Griechen
7082:                                    bal-,   balbal    bend-                                   109
7089:bal-, balbal- „wirbeln, sich drehen".
=== IEC
908:baba (2) ‘mess, slobber’ It. bava ‘drivel, dross, waste’; Fr. bave, id.; Du. poep (2) ‘excrement’; E dial. poop, id.; Cz. bába ‘bread-pudding, brown beer
=== SYN
103:ranslation words”. A special use of a familiar foreign
180:For most of the other modern languages covered, various students or citi- zens of foreign birth have supplied or been consulted on the words of their respective mother-tongues.
9216:ended sense of NE mill in saw- BF eel etc., which is foreign to the other words for ‘mill’ and is = pressed rather by words for ‘factory’, ‘workshop’, or the like.
10649:The Greeks knew the trousers worn by oriental peoples, which they called iyatupiies, & foreign word, or @édakor Sacks); and the Romans became ac- quainted with the brdcae worn by the peoples of north Europe, which they aad despite even legal opposi- " ae barbarian garment, adopted. hie Crm (68. Brak), OF bree. (sg. ft? ME brech, NE breeches © pl.), Du. broek OHG bruoh MHG bruoch« ? TUON, ; ch; prob. fr. Gme. Gallo-Lat racae, braccag (> G ik ; ‘ Broxl, cf, also zy TK. Bpaxa, NG bathe Sp. bragae on, crawers’; It. " /agas, Fr. braies; Br. bra-
13343:2. Grk. onutda (Theophr. HP 3.14.4, 5.7.7), formerly taken as ‘birch’ (but identification uncertain) and hence NG use to render the (foreign) birch; prob. a loanword of unknown source.
17624:inherited group are In or A Bs of ‘go (come) after, cos bined 4 ‘go (come) with, accom- pend fl with dominance of the lat- pany vrranian and generally in de- feria NCP the notion of ‘follow ag- rvative™ ue’ was originally foreign
29010:sense > It. bravo > Fr. prav), fr. Lat. barbarus orig. ‘foreign, a foreigner’, id. REW 945. Gamill-
31207:Words that are used mainly with ref- erence to the interpretation of foreign languages or learned exposition, like Grk. épunvebw, NE interpret, expound, Russ, istolkovat’, etc., are not included. But the Goth. and ChSl. renderings of épunvebw are given as the only available words and probably used for ‘explain’ in general. For the group ON pyda partly ‘explain, interpret’, MHG (be)diuten ‘explain, point out’, see under ‘meaning’ (17.33).
```


## [2026-09-05T05:50:50.892Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT\"; grep -n -i -E 'baboon|barbarous|rhubarb|brave|babble' SKT.txt | head -8\necho \"=== FSD vol1 baboon/barbarian\"; grep -n -i -E 'baboon|barbarian|balalaika' FSD_vol1.txt | head -6\necho \"=== WEB\"; ls WEB*; grep -n -i -E 'baboon|balalaika|bambino' WEB*.txt | head -6"
}
```


### [2026-09-05T05:50:51.000Z] TOOL RESULT

```
=== SKT
1266:Baboon.  (F.  or  Low  L.)  F.  hahou we  ftl&o  find  M,  E.  babion,  hafnan,  btt^' wine. ^  Law  L.  habfwynus.  a  baboon  (a.o. 1205).     Origin  uncert.iin.
1281:Badinage,  jesting  talk.  (F.-Prov.— L.) F.  ftaa'ifiij^.  —  F,  badintr,  to  jest.  ■■  F. baiitn,  an; ,  jesting.  —  Prov.  badtr  ( =  F. bayerX  lit.  to  gni>e;  hence,  to  be  silly.— Lale  L.  baiiare.  to  gape ;  prob.  of  imitative origin,  from  ba.  exjjrcssive  of  opening  the mouth.     Cf.  Babble.
1402:barrifiter.  (lx>w  L.  —  C.)  A  barbarous word ;  formed  with  suffix  -isferi  =  Low  L. 'ii/ariuj')  from  the  sb.  Air.  Spelinan  gives the  Low  L.  form  as  l>annrferiuj.
1542:Bauble   (a),  a  plaything     (P.  «  Ql^ Corr.  from  F.  bstbioU,  a  child's  loy.-«iv' babboia,  a  toy.— Ital.  fhibbeo,  a  stiupAsttf cf.  Low  L.  f'dhu.'ui.  a  simpleton      Frov uttering  ot  indistinct  sounds.  d[.  Gk-fc Cctf,  10  chatter ;  sec  Babble,  BarbaWtt.
1856:Blab,  (0  tell  tales.  (Scand  >   M.  £. a  telltale;    blabetm,   to   babble.  - bfabbrtfXo  Iwbble  ;  cf.  Swed.  dial. Q.  plapfirn,  to  bflbhle.  prate.     <>f| live  origin ;   cf.  Gael.  pUb,  a  soft Plabair,  a  babbler ;   blaihirun^  a  stamt blabhdoih,  babbling,  garnilous.
2226:Bravado.  (Span.)     See  Brave.
2227:Bravo.  (F.)  F.  brave.  *  brave,  gay, line,  proud,  brdggard,  valiant ;'  Cot.  The same  as  Ital.,  Span  ,  and  Port,  bravo.  Elym. miknowu ;  none  of  the  explanations  nre satisfactory  ;  the  Bret,  brav,  O.  Swcd.  A/ii/l appear  Co  be  borrowe<l  from  F.  Cf.  Bret. bru^,  to  itrnt  about,  Gael,  brragh,  fme; see  Brag.
2228:bravado.  (Span.)  Altered  from  Span. bmvaJa.  'a  bravarlo ;'  Minsfaeu's  Span. Diet-— Span.  ^mtw.  brave.
=== FSD vol1 baboon/barbarian
6698:Ac'lis,  1   ak'lis;  2   fic'IIs,  n.  IL.J  1.  Conch.  A   genus  typical of  Aclidx.  2.  [a-!  [ac'li-des,  1   ak'h-dlz;  2   fic'll-dSg,  pl.\ A   club  studded  with  spikes,  thrown  from  the  hand  and drawn  back  by  a   leather  thong:  used  only  by  barbarians, but  mentioned  by  Roman  writers.
8409:drove  the  barbarians  across  the  T>annbc  in  253. yE-mil'l-us,  1   I-mll'i-us;  2   G-miri-fls,  n.  1.  Mamcrcus, a   Roman  dictator  who  died  In  437  B.  C.  2.  Paul  us,  a Roman  consul  and  general  who  died  In  210  B.  C.  3.  A Christian  martyr,  A.  D.  4S4.  4,  A   noble  Roman  In  Shake- speare’s Titus  Andronicus.  5.  A   masculino  personal  name. See  Emile.
9612:—   canonical  age  (Eccl.),  the  age  required  by  the  canons for  ordination  or  for  the  performance  of  any  particular  act. ^-copper  age  ( Archcol .),  an  age  Intermediate  between  the stone  age  and  the  bronze  age.— dark  ages,  the  period  in European  history  beginning  with  the  Irruption  of  barbarian hordes  before  the  fall  of  the  Western  Roman  Empire  (A.  D. 476),  extending  to  the  Italian  Renaissance  (13th  century), and  characterized  by  the  decay  of  civilization.—  flint  age, same  as  stone  age.  See  age1,  2,  (4).— full  age,  the  age when  one  reaches  the  period  of  independent  action  and responsibility  In  personal  affairs;  majority:  generally  21 years  —   golden  age.  1.  A   mythical  period  when  perfect Innocence,  peace,  and  happiness  reigned.  2.  Rom.  Lit.  The period  (31  B.  C.  to  A.  D.  14)  of  the  finest  classical  writers; hence,  in  any  country,  the  periods  of  literature  most  nearly corresponding  to  this.
11619:al-for'ja,  1   al-fer'ja  or  (Sp.)  al-fOr'ha;  2   51-for'ja  or  (Sp.) al-f6r'ha,  n.  [Sp.]  [Archaic.]  A   wallet;  saddle-bag;  hence, cheek-pouch,  as  of  a   baboon;  humorously,  the  stomach, al-ror'get;  aU-for'chet.
22871:A-ra'bl-an,  1   a-re'bi-an;  2   a-ra'bi-an,  a.  Of  or  pertain- ing to  Arabia  or  Its  Inhabitants.—  Arabian  architecture,  a branch  of  the  Saracenic,  esp.  as  illustrated  in  Egypt  and Syria,  distinguished  by  buildings  generally  square  or  polyg- onal in  form,  with  fiat  roofs  supported  by  arches,  pointed or  of  horseshoe  form,  resting  on  columns  generally  in  paral- lel lines,  frequently  domed,  the  domes  often  being  pointed, and  with  walls  covered  with  ornament  in  Intricate  diaper patterns  brilliantly  colored.  See  plate  of  architecture. fig.  8,  and  Saracenic  architecture,  fig.  8.— A.  baboon, the  sacred  b^n-vm.  or  hamadryad. —   A.  bird,  the  pbenix. — A.  coffee,  coffee  from  Mocha,  A^bla. — A.  Desert,  that section  of  the  desert  between  the  Nile  and  the  Gulf  of  Suez. — A.  Gulf,  anciently,  the  Red  Sea. — A.  horse,  see  Arab*.  2. — A.  Nights*  Entertainment,  a   famous  and  ancient  col- lection of  Eastern  stories,  supposed  to  have  been  related  to the  sultan  Shahriyar  by  his  wife  Scheherezade,  who  by  that means  saved  herself  from  death  as  inflicted  by  the  sultan
33144:cation  of  Babbitt  metal  or  the  like,  as  to  bearings.—  bah'-  ba'bl-anf,  n.  A   baboon,  ba'bl-onf.
=== WEB
WEB_vol1.txt
14471:PAE T ; ee Ba’bi, a. Babist. Baal Bt, Alite, n. 1. one who worships pā/bi-An, bā’bi-ðn, n. a baboon. [Obs.] ba’bies’-breath” (bret), n. 1. a fairly tall plant of the pink family, with small, fragrant, white or pink flowers.
14475:trine and principles of a religious se in Persia in 1843: it forbids besging arnnaed alcoholic liquors, buying and selling ah ing ne more than gae wife, ete. aves, äb’ist, n. one who believes in Babis Bäb’ist, a. of Babism. bipm Bäb’īte, a. and 2. Babist. bab/lah, 7. {Hind.] a pod of several species Acacia, which comes from the East undec ie name of neb-neb. It contains gallic acid a A tannin and is used in dyeing and tanning n bä’bọọ, n. 1.a Hindu title equivalent to M Si, or Esq. wi i A . a native clerk in India who ca rite English. can Nests 3. a native of India who has a little English education: derogatory term. ba-bool’, n. same as bablah. bab-oon’, n. [ME. babewyne; OFr, babuin baboon, origin of name unknown,] the dog. faced ape of various genera, including the Cynocephalus and Mandrilla. They have an elongated abrupt muzzle like that of a dog strong tusks or canine teeth, a short tail, checkpouches, small, deep eyes with huge eyebrows, and naked callosities on the but- tocks.
14476:BABOON (Cynocephalus maimon)
14477:bab:ọọn’ēr-y, n. 1. baboons collectively. 2. baboonish behavior. bab-ọọn’ish, a. like a baboon; stupid; un- couth. bå-bouche’, ba-bogsh’ (-bọọsh/), n. [Fr. ba- bouche; Ar. babush; Per. paposh, a slipper from pa, foot, and posh, covering.] a heelless slipper, consisting of a vamp and sole, worn in Eastern countries. ba-bu’, n. same as baboo. ba-bul’, n. same as bablah. x bà-bush’kå, n. [Russ., grandmother.] a ker- chief or scarf worn on the head by a woman or girl. bā’by, 7.; pl. bā’bieş, [dim. of babe.] 1. an infant or young child of either si babe. A 2. a person who behaves like an 1n helpless or cowardly person. 3. the youngest or smallest in a grouk; a 4. a girl È young woman, especially pretty one, [Slang. k zi baby buniing; an l ar sleeping bag with an attached hood. ‘dist ba’by, a. 1. babyish; infantile or childish. 2. small of its kind. 3. of or for an infant. à to bā’by, v.l.; babied, pl., pp-; babying: ppr- treat like a baby; pamper; coddle. teer bā’by beef, meat from a prime heifer Or stee fattened for butchering when on years old. ba/by blue, light blue. ba/by blue-eyes, a California plan spotted blue flowers. ba/by bug/gy, a light carriage for W baby about; perambulator. dren can ba/by farm, a place where young childr
15151:BALALAIKA
16839:ba/vi-in, 2. (OE. babewin, baboon.] a baboon.
```


## [2026-09-05T05:51:00.941Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6875,6920p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-05T05:51:00.991Z] TOOL RESULT

```
baby ,,Kind‘‘, schwed. mdartl. babbe „Kind, kleiner Junge“ (s. auch u. ba*b
„schwellen“, mhd. babe, bohe „Alte, 3iutter‘, biiobe ,,Knabe, Diener^', ahd.
                                                                                           ;




f06                                           baba


JBuobo, agB, Bofa          Mannsname:     lit Ibba, aksl.        „altes           serb.-ksl.
IhbVu, bhbati ^stammeln'^, bulg. h^bV^ (hihrh) „bruinme, schelte; schwatze,
stottere^', sloven. Idbam, hdhdti „unverstan(ilich reden“, bdhljdfi „lallen“,
bulg.      habdfz,      bohdf^ „larme,   mache ein Gerauscli“, serb. hbbocem, bobbtati
„niit den Zahnen klappern“, bobbniti „schwatzen, murmeln“; lett. bibinat
„plappern, murmeln^, apr. bebhint „spotten'* (s. Berneker 105, auch 36 f.
•fiber russ.     zabobony „abgeschmackte, aberglaubische Eeden‘* u. dgl.).

   "^balbal- {babal-; bambal-, woraus bam-b-, bal-b- u. dgl.):
   Ai. balhala Tear- „stammeln'‘; bulg. blaboF^, bolboVz „schwatze“, russ. boh-
boliih „8chwatzen, faseln“, cech. beblati „stammeln“ (usw. s. Berneker 69)
lat. babulus „Scliwatzer“ mir. babloir „Sclivratzer“ TLehnwort: vgl. Fick II
                                 ;


161, Vendryes De bib. voc. 115)      nhd. babbehi, pa'p'peln, engl. babble, norw.
                                          ;


bable, schwed. babbla, aisl. babba „scliwatzen‘’; cech. blblati, bleptaii „stam-
meln, stottern“ (ahnlich breptati „stammeln, schvratzen“), poln. beblac, beblac
„schnell und unverstandlich reden; verbotenes reden"'; lat. balhus „stani-
melnd, lallend", balbiitio „stamnile", ai. balbfithd-h Name feigentlich ,,Stamm-
ler"), cech. bib ,,Tolpel", serb. bJebetati, lit. blebenti „plappern“; gr. ^aa-
PaXvl^cOy ^aju^a^vxco „habe Zahneklappern"", ^aju^alvoj ,,stammle” (daraus
lat. bamhalo, s. Lit. bei Yt LEWb.^ 80 j.

   Mit -r-:      barbara-h „stammelnd, pi. Bezeichnung nichtarischer Yolker,
                  ai.

gr. pdQ^aQog „nicht griechisch,      von unverstandlicher Sprache", woraus (lat.
barbartis), ^ag^agopcovog „von unverstandlicher Sprache" (kaum nach Weid-
ner GL 4, 303 f. aus einem babylon. barbaru „Fremder, womit die Griechen
sich doch selbst benannt gehort hatten), sloven, brbrati brbljaii ,,plappern“,
Serb, brholjiti, brbljati ds. (s. auch u. bher „brummen“), lat. babitrrus ,,stultus,
ineptus", gr. ^a^vQjag' 6 naQayojQo^ Hes. (iiber lat. biirrae s. Yf. LEAYb.^;
```


## [2026-09-05T05:51:02.658Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A4%BE%E0%A4%AC%E0%A5%82",
 "prompt": "Etymology of Hindi बाबू (bābū): origin (nursery word? Persian? Sanskrit?), meaning, and descendants/borrowings."
}
```


### [2026-09-05T05:51:08.756Z] TOOL RESULT

```
# Etymology of बाबू (bābū)

## Origin

According to the Wiktionary entry, बाबू is "Inherited from Proto-New Indo-Aryan *बाब्ब (bābba) + Middle Indo-Aryan -𑀉𑀓- (-uka-), imitative of baby talk." This indicates the word derives from baby talk rather than Persian or Sanskrit sources.

## Meaning

The Hindi noun has four primary definitions:

1. "papa" or "father"
2. A government clerk or administrative official
3. A polite form of address meaning "sir" or "mister"
4. A term addressing a young boy or one's son

## Descendants

The word has entered English through borrowing, appearing as:
- **babu** (modern English)
- **baboo** (archaic English)

It was also borrowed into Jarawa, where it means "(government) official," reflecting the administrative sense of the Hindi term.

The word's journey from nursery language to terms denoting both familial relationships and bureaucratic positions demonstrates semantic expansion typical of words entering official administrative vocabularies during colonial periods.
```


## [2026-09-05T05:51:18.446Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 75 -l 75 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg75 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T05:51:20.715Z] TOOL RESULT

```
total 7248
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:51 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
```


## [2026-09-05T05:51:23.607Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg75.png"
}
```


### [2026-09-05T05:51:24.066Z] TOOL RESULT

```

```


## [2026-09-05T05:51:24.058Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T05:51:37.741Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 75 -l 75 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg75_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg75_400.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.18*w),int(0.22*h),int(0.60*w),int(0.40*h))).save('pg75_greeklatin.png')\n\""
}
```


### [2026-09-05T05:51:41.208Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T05:51:43.444Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg75_greeklatin.png"
}
```


### [2026-09-05T05:51:43.467Z] TOOL RESULT

```

```


## [2026-09-05T05:51:58.246Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rhubarb",
 "prompt": "Full etymology of rhubarb: Medieval Latin rheubarbarum, Greek rha barbaron, the river Rha / Persian rewend question."
}
```


## [2026-09-05T05:51:58.667Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/barbarian",
 "prompt": "Full etymology of barbarian and barbarous: Greek barbaros, PIE imitative root, Latin barbarus, Sanskrit barbara-."
}
```


### [2026-09-05T05:52:03.394Z] TOOL RESULT

```
# Rhubarb Etymology

The word "rhubarb" entered English in the late 14th century, originating from Medieval Latin *reubarbarum*, which derived from Greek *rha barbaron* meaning "foreign rhubarb."

The term combines two elements:
- **Rha**: "rhubarb," possibly connected to Persian *rewend* ("rhubarb")
- **Barbaron**: "foreign," from *barbaros* (see: barbarian)

The plant itself was native to China and Tibet, and "was long imported into Europe by way of Russia and became associated with that land." The modern spelling with an *h* wasn't standardized until the late 18th century.

Interestingly, the word gained a secondary meaning in baseball slang around 1938, referring to a "loud squabble on the field," possibly derived from stage actors repeating "rhubarb" to create crowd noise effects.
```


### [2026-09-05T05:52:05.905Z] TOOL RESULT

```
# Etymology of "Barbarian"

The word "barbarian" traces back through multiple languages to an ancient imitative root. According to the Online Etymology Dictionary, the term originates from "Greek _barbaros_ 'foreign, strange; ignorant,' from PIE root _\*barbar-_ echoic of unintelligible speech of foreigners."

**Key etymological path:**
- **Greek**: _barbaros_ (foreign, strange)
- **Latin**: _barbarus_ (strange, foreign, barbarous)
- **Medieval Latin**: _barbarinus_
- **English**: Used from the early 15c. onward

**Original meaning**: The Greeks employed this word to describe "all that are not Greek," particularly the Medes and Persians. Initially not entirely derogatory, the term became increasingly negative following the Persian wars. Romans subsequently applied it to tribes lacking Greek or Roman cultural accomplishments.

**Semantic shift**: The adjective form emerged in the mid-14c. as "foreign, of another nation," but by the 1590s it acquired the sense of "rude, uncivilized." The noun developed meanings ranging from historical references (non-Roman/Greek persons) to broader applications describing uncultured individuals.

The root itself is onomatopoetic, mimicking the incomprehensible sounds of foreign languages to ancient Mediterranean ears.
```


## [2026-09-05T05:52:17.231Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/بربط' --note 'page 75, root Baba, node #3: Persian barbat < MP barbut < Gk barbitos' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/βάρβιτος' --note 'page 75, node #1: Gk barbitos origin (probably Phrygian), descendant MP barbut' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/baboon' --note 'page 75, nodes #9-#10: OF babine/baboue > baboon' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/brave' --note 'page 75, nodes #11-#14: brave/bravo < It. bravo, L. pravus vs barbarus' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/balalaika' --note 'page 75, node #8: English balalaika < Russian' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/балалайка' --note 'page 75, node #6: Russian balalaika < dial. balabajka, onomatopoetic balabaj-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/بربط/' --note 'page 75, node #3: Moin and Dehkhoda entries for بربط (MON:497 check)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/बाबू' --note 'page 75, nodes #15-#16: Hindi babu, nursery word, not from Persian' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/rhubarb' --note 'page 75, nodes #4-#5: rheubarbarum, rha barbaron' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/barbarian' --note 'page 75, nodes #1,#4,#5: Gk barbaros, PIE echoic *barbar-' 2>&1 | tail -2"
}
```


### [2026-09-05T05:52:23.111Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1fe3ed61f0355afe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/763ef50487e36078.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/590bb166588f0473.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7276822cf2670d2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cea9cdba9c5e1f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/790d38a569ad2e0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c595bb339a474517.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/22247f636f7947b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/213ab01d606324b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5f779d0f0be6ad1.txt
```


## [2026-09-05T05:52:47.008Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY بربط/بابا\"; grep -n 'بربط\\|بابا\\|بالالایکا' incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY latin index\"; grep -n -i 'BARBAT\\|BABA\\|BALALA' incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== FSD bravo\"; grep -n -i 'bravo, ' FSD_vol1.txt | head -3\necho \"=== DEV/DOZ baboon\"; grep -n -i 'babouin\\|babine' DEV.txt DOZ.txt LAM.txt 2>/dev/null | head -6"
}
```


### [2026-09-05T05:52:47.107Z] TOOL RESULT

```
=== ARY بربط/بابا
2920:۲ / بابا (واژه‌ی کودکانه به چم"پدر")
5318:۱ ایسلند ی کیره (۸0 ۲ باباایی 5 صا۵): 998999 ۶080800
=== ARY latin index
3181:BABINAT (LATVIAN) (3) gis) BABABA- (SANSKRIT) cy Soile
3182:BEBINT — :(OLD PRUSSIAN) oS gos 9 BABAI (GREEK) 3h y
3183:BABAN CELTIC) (1S) gle BABAE, PAPAE LATIN) 3
3184:BABAN WELSH) 5) BEBE (FRENCH) W313
3185:BABAN AGABLIC) SSE NENE, BEBE (SPANISH) gly
3194:Lisa dasens dala BABA, BOBOCEM — (SERBIAN) ig po
3382:BABBELN BABAI (GREEK) gy
3402:; BRBOLJITI, (SERBIAN) «9 po BALBALA, BABALAKR
=== FSD bravo
48963:3.  [Archaic.]  Excellent.  [F.,  <   It.  or  Sp.,  bravo,  brave, wild;  prob.  <   L.  barbarus;  6ee  barbarous.]
48974:Green  Short  Hist.  Eng.  People  p.  531.  Ur.  1875,1 2.  A   shout  of  applause.  See  bravo,  interj. bra'vo,  1   bra'vo;  2   bra'vo  (xm),  interj.  [It.]  Good; well  done;  excellent:  used  in  applause,  also  as  a   noun. The  Italian  cries  bravo  only  to  a   male  performer;  to  a   fe- male, brava,  and  to  the  whole  company,  bravi .
=== DEV/DOZ baboon
```


## [2026-09-05T05:52:51.934Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2900,2935p' incoming/ARY/ARY_pages.txt; echo \"--- page tag\"; awk 'NR<=2920 && /\\[pdf page/ {n=$0} END{print n}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-05T05:52:55.739Z] TOOL RESULT

```
روسی ((551۸): ان 235 نقحلاه
چکد (280): ان 63 (857۸0) :0/0075
برهمی (80[78(11۸01): 1 7 (87۸0) +7
اسلرا کی (5].01۸/0): پا ان برهان قاطع : ۱۹۷
یادداشت: أ
ُایستادن" و زمان‌های گوناگون آن در اکثر زبان‌های هند و اروپایی معنی خود راکم و پیش حفظ کرده‌اند و اشتقاق ا
همه‌ی آنها از واجریشه‌های هند و اروپایی این فهرست است.
| گس سروالی اسر ی ۷686
اوستایی (4587۷): 6 و38۸7 ,82 چکه (ط220): 1۲
پپلوی (تماتلهم: ۰ ۸826 م۸۳ لیترانی (4۸1۸2ا 777 ): ‎٩‏ ,85
کردی (080157): 8۸ پروسی کهن (۷/فا۳۸/55 010): ۱1:1
3 مانسکريي, (87/7/شک): 2
ارمتی (45(/100(ه) یا ۰< ۸3 ب8۸ پسگشت‌ها 5
گرتیکه (00770): ۳۱" 2۸ 8 ۶0080
آلمانی کهن ((520/۸ 0ات صا): 0 (۲178) :2 2/(ع ماد
۸ ,لا8] 3 013 0
اسلاوی کهن (ع۲1ها5 نات 0ا0): برهان قاطم: (ابا) ۷۶
320 فرهنگ معین : ۳۳۶
لهستانی (۳0(1./8): 2۸ :
[pdf page 101]
۲ / بابا (واژه‌ی کودکانه به چم"پدر")
یادداشت:
معین اين واجریشه در برخی زبان‌های هند و اروپایی: با» برای؛ سپس.
کردی (62/5[4): ۸3۸ لهستانی (7ل5ا۳0): 7170
برنانی (07655): ۸ چکه (لل525): 717۸
لاتین (۸7120ل): ۸ ب28۳۸ پسگشت‌ها کیت یت
فرانسه (4ل۳8(/0): 7/۸۸ زر ۳
اسپانیایی (5۳۸۸/]977): ۳/۸ 3 (7۸71838) ۸0
پرتغالي (۳0870010238): 7۸ برهان قاطع + ۲۱
| جم‌انگلیس سروازی اش ۷۵
اوستایی (4۷887۸(۷): ایتالیایی (۵ل7۸): ۷0
۸ ا۷۸17 ,۷۸70 ۷۸2۵ رومانی (80۸۸(۷۵): ۷7 ۱
پهلری (۲7شاللمهه): اه پر تغالی (۳0/70183): ۷0
کردی (28015]4)). 2 گرتیکه (007710): 5
بلوچی (/1ع/ل8۸): زر ایسلندی کهن (/(1۸/ 5۸010۸ صاه):
آفغانی (پشتو) (470[7۸۷1): را ۷
--- page tag
[pdf page 101]
```


## [2026-09-05T05:53:59.218Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o 'BRAVE [a-zA-Z-]*' AHD_watkins1985.txt | head -3; grep -o 'BRAVO[ _]*[a-zA-Z-]*' AHD_watkins1985.txt | head -3; grep -o 'RHUBARB [a-zA-Z-]*' AHD_watkins1985.txt | head -3; grep -o 'BABOON[ _]*[a-zA-Z-]*' AHD_watkins1985.txt | head -3"
}
```


### [2026-09-05T05:53:59.304Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:01:29.828Z] TOOL CALL #45: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk75.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_BARBAT = \"https://en.wiktionary.org/wiki/بربط\"\nW_BARBITOS = \"https://en.wiktionary.org/wiki/βάρβιτος\"\nE_BABOON = \"https://www.etymonline.com/word/baboon\"\nE_BRAVE = \"https://www.etymonline.com/word/brave\"\nE_RHUBARB = \"https://www.etymonline.com/word/rhubarb\"\nE_BARB = \"https://www.etymonline.com/word/barbarian\"\nW_BALA = \"https://en.wiktionary.org/wiki/balalaika\"\nW_BALARU = \"https://en.wiktionary.org/wiki/балалайка\"\nA_BARBAT = \"https://abadis.ir/fatofa/بربط/\"\nW_BABU = \"https://en.wiktionary.org/wiki/बाबू\"\n\nPOK_NOTE = (\"POK_01.txt, form-feed leaf 100 = printed pp. 91-92: 'bāba- Schallwort, Lallwort für \"\n            \"unartikuliertes undeutliches Reden; ebenso bal-bal-, bar-bar- mit vielfachen Dissimilationen' \"\n            \"and, under 'Mit -r-': 'ai. barbara-ḥ \\\"stammelnd\\\", Pl. Bezeichnung nichtarischer Völker, \"\n            \"gr. βάρβαρος \\\"nicht griechisch, von unverständlicher Sprache\\\" (woraus lat. barbarus)'.\")\nWLD_NOTE = (\"WLD_Bd2_pages.txt lines 6875-6920 = Bd. II pp. 106-107: the same entry in its older form — \"\n            \"'*balbal- (babal-; bambal-…)' … 'Mit -r-: ai. barbara-ḥ „stammelnd, pl. Bezeichnung nichtarischer \"\n            \"Völker“, gr. βάρβαρος … woraus lat. barbarus'. Pokorny's 'WP. II 107' points here.\")\nAHD_NOTE = (\"AHD_watkins1985.txt line 317: 'baba-. Root imitative of unarticulated or indistinct speech; also a \"\n            \"child's nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. \"\n            \"2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. … \"\n            \"6. Russian balalaika … 8. Greek barbaros, non-Greek, foreign, rude (< \\\"one who speaks incomprehensibly\\\"): \"\n            \"(BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babū, father: BABU. [Pok. baba- 91.]' — Nourai's AHD:1507 is \"\n            \"this appendix entry (the 1975 New College appendix runs pp. 1505-1550 and baba- stands at its head).\")\nOEW_NC = {\"ref\": \"OEW:22\", \"status\": \"not_checked\",\n          \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org (djvu.txt returns 401); refs_online.json records no readable copy.\"}\n\ndef oew(): return dict(OEW_NC)\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Baba, Barbarah, Balbarah\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE (echoic) *baba- 'nursery/imitative word for indistinct speech and for relatives', with the reduplicated variants *bal-bal- and *bar-bar- (Pokorny 91; Watkins/AHD baba-)\",\n  \"note\": \"The root box is right in substance. Pokorny I 91-92 has exactly this entry — 'bāba- Schallwort, Lallwort für unartikuliertes undeutliches Reden; ebenso bal-bal-, bar-bar- mit vielfachen Dissimilationen' — and Walde-Pokorny II 106-107 the same, so Nourai's three headwords 'Baba, Barbarah, Balbarah' are the three variants of ONE imitative base, not three roots; the language label 'Indo-European' is defensible only in the weak sense in which echoic words are 'Indo-European' (they are re-created in each branch rather than inherited, which is why Pokorny prints them without an asterisk and Watkins without a laryngeal). Two refinements. (a) 'Barbarah' and 'Balbarah' are not reconstructed proto-forms but the attested Sanskrit words barbara- 'stammering; pl. the non-Aryan peoples' and balbalā-karoti 'he stammers'; Nourai's gloss 'people who speak a non-Aryan language' is the Sanskrit sense of barbara-, transferred to the root box. (b) The root note 'these words may be related to the root \\\"Pa: to protect, feed\\\"' has no support: no source connects the echoic *baba- with PIE *peh2- 'protect, feed' (Pok. 787), and Pokorny keeps them apart. Structural point about this page: on the printed page (p. 45) the Latin box hangs off the Greek box, not off the root — see node #4.\",\n  \"note_fa\": \"ریشهٔ این نمودار در واقع یک «واژهٔ آوایی/کودکانه» است نه ریشه‌ای صرفی: پوکورنی (ص ۹۱-۹۲) آن را چنین می‌آورد: bāba- واژهٔ آوایی و کودکانه برای سخنِ نامفهوم، و گونه‌های مضاعف آن bal-bal- و bar-bar-؛ والده-پوکورنی (ج ۲ ص ۱۰۶-۱۰۷) نیز همین را دارد. بنابراین سه سرواژهٔ نورایی (Baba، Barbarah، Balbarah) سه ریشهٔ جداگانه نیستند، بلکه سه گونهٔ یک ستاک آوایی‌اند؛ افزون بر این «barbara-» و «balbala-» صورت‌های ضبط‌شدهٔ سنسکریت‌اند نه صورت بازسازی‌شدهٔ هندواروپایی، و معنی «مردمی که به زبان غیرآریایی سخن می‌گویند» معنیِ همان واژهٔ سنسکریت است. یادداشت نورایی که این واژه‌ها شاید با ریشهٔ «Pa: نگاه داشتن، خوراک دادن» پیوند داشته باشند در هیچ منبعی تأیید نمی‌شود و پوکورنی این دو را از هم جدا می‌داند. در مجموع خودِ ریشه و معنای آن درست است.\",\n  \"sources\": [E_BARB],\n  \"ref_check\": [\n    {\"ref\": \"OEW:22\", \"status\": \"not_checked\", \"note\": \"Shipley, The Origins of English Words (1984): archive.org copies are lending-only (djvu.txt 401); no readable copy per refs_online.json. Nourai's whole page is built on Shipley's 'baba' article.\"},\n    {\"ref\": \"AHD:1507\", \"status\": \"supports\", \"note\": AHD_NOTE}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Bd. I pp. 91-92 (POK_01.txt leaf 100)\", \"stance\": \"supports\", \"note\": POK_NOTE},\n    {\"src\": \"WLD\", \"where\": \"Bd. II pp. 106-107 (WLD_Bd2_pages.txt ll. 6875-6920)\", \"stance\": \"supports\", \"note\": WLD_NOTE},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4221 s.v. babble; l. 4427 s.v. barbaric; l. 5340 s.v. booby\", \"stance\": \"supports\", \"note\": \"Klein operates with exactly Nourai's three variants: 'the I.-E. imitative base *bab-' (babble), 'the related imitative base *balb-' (booby, L. balbus), 'the related imitative base *barb-, \\\"to stammer\\\", whence Gk. βάρβαρος' (barbaric).\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 101] = printed p. 100\", \"stance\": \"supports\", \"note\": \"Aryanpur has the root entry «بابا (واژه‌ی کودکانه به چم \\\"پدر\\\")» with Kurdish, Polish, Latin, French, Spanish, Portuguese cognates and a Borhan-e Qate' page reference — an independent modern Persian confirmation that this nursery word is treated as an IE-wide formation.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Greek\", \"words\": \"barbitos, barbaros\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two words of very different standing are put in one box. (a) βάρβαρος 'non-Greek, foreign, speaking unintelligibly' IS the classic reflex of the echoic base: it is a reduplication bar-bar- of the same type as Sanskrit barbara- 'stammering; pl. the non-Aryan peoples', first in Homer's βαρβαρόφωνος (Il. 2.867 of the Carians) and then the standard Greek word for Medes and Persians after the Persian wars; Pokorny 91, Walde-Pokorny II 107, Klein s.v. barbaric and Etymonline all give this. Confirmed. (b) βάρβιτος / βάρβιτον, the deep-toned lyre of Anacreon, Sappho and Alcaeus, does NOT belong here. Its -it- suffix is not Greek, and Wiktionary (following Beekes, EDG 201) says 'uncertain, probably from Phrygian'; Chantraine likewise treats it as a loan from a non-Greek language of Asia Minor. The similarity to βάρβαρος is accidental, and no lexicon derives barbitos from the imitative root. Nourai's arrow root -> barbitos is therefore disputed, while root -> barbaros is confirmed; the node takes the worse verdict.\",\n  \"derivation_fa\": \"در این خانه دو واژهٔ کاملاً متفاوت کنار هم آمده است. یکی βάρβαρος «ناـیونانی، بیگانه، کسی که نامفهوم سخن می‌گوید» که به‌راستی بازتاب همان ستاک آوایی است: صورتی مضاعف از bar-bar- همانند barbara- در سنسکریت، نخست در «باربارُفونوس» هومر (ایلیاد ۲/۸۶۷ دربارهٔ کاریان) و سپس نام رایج یونانیان برای مادها و پارسیان؛ پوکورنی ۹۱، والده-پوکورنی ج۲ ص۱۰۷ و کلاین همین را می‌گویند و این بخش درست است. دیگری βάρβιτος، نام سازی زهی و بم‌آوا نزد آناکرئون و سافو، که به این ریشه ربطی ندارد: پسوند -it- یونانی نیست و ویکی‌واژه به پیروی از بیکس (فرهنگ ریشه‌شناختی یونانی، ص ۲۰۱) آن را «نامعلوم، احتمالاً فریگی» می‌داند و شانترن نیز وام‌واژه‌ای از زبان‌های آسیای صغیر می‌شمارد. پس شباهت آن به βάρβαρος تصادفی است و ادعای نورایی دربارهٔ barbitos را پژوهش امروزی نمی‌پذیرد؛ چون بدترین حکم بر خانه حاکم است، این گره «رد شده» ثبت می‌شود.\",\n  \"sources\": [W_BARBITOS, E_BARB],\n  \"ref_check\": [\n    {\"ref\": \"OEW:22\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 lending-only; could not read p. 22. Note that Shipley is a popular discursive dictionary, not a technical one, and is the likeliest source of the barbitos/barbaros conflation.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 92 (POK_01.txt leaf 100)\", \"stance\": \"partial\", \"note\": \"'gr. βάρβαρος „nicht griechisch, von unverständlicher Sprache“ (woraus lat. barbarus)' — barbaros yes; βάρβιτος does not appear anywhere in the entry.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 107\", \"stance\": \"partial\", \"note\": \"Same: 'gr. βάρβαρος … woraus (lat. barbarus)'; no barbitos.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4427 s.v. barbaric\", \"stance\": \"partial\", \"note\": \"'Gk. βάρβαρος, \\\"non-Greek, foreign, barbarous\\\", which is cogn. with OI. barbaraḥ, \\\"stammering (designation of the non-Aryan nations)\\\", from the I.-E. imitative base *barb-'. Klein has no entry deriving barbitos from this base.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. baba-, sense 8\", \"stance\": \"partial\", \"note\": \"'Greek barbaros, non-Greek, foreign, rude (< \\\"one who speaks incomprehensibly\\\"): (BARBARIAN), BARBARISM, BARBAROUS' — barbaros only.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"barbut\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian barbut, written blbwt' in Book Pahlavi, 'lyre, lute', is real and is exactly what MacKenzie's Concise Pahlavi Dictionary p. 17 prints: 'barbut [blbwt' | N ~] lyre'. Its source is Greek βάρβιτος, borrowed in the Hellenistic/Parthian period (Seleucid and later Greek cultural presence in Iran, 3rd c. BCE onward), Greek -os being dropped as in other Greek loans in Middle Persian and Greek -i- rendered by Pahlavi -u- before the labial (blbwt' with l for r is merely the Aramaic-based orthography, not a sound change). Mo'in says the same in his etymological footnote to Borhan-e Qate' p. 249 (continued on p. 250): 'پهلوی barbut از یونانی …', and Wiktionary derives Persian بربط from Middle Persian barbut 'from Ancient Greek bárbitos', citing MacKenzie 1971 p. 17. So the arrow Greek -> Pahlavi is confirmed; what is wrong is one step up, since barbitos itself is not from the imitative root (node #1).\",\n  \"derivation_fa\": \"«barbut» فارسی میانه (در خط پهلوی blbwt') به معنی «چنگ/بربط» واژه‌ای واقعی است و مکنزی در فرهنگ کوچک پهلوی (ص ۱۷) دقیقاً همین را می‌آورد: barbut [blbwt'] «lyre». خاستگاه آن یونانی βάρβιτος است که در دورهٔ هلنی و اشکانی به ایران راه یافته؛ پایانهٔ یونانی -os افتاده و -i- یونانی پیش از لب‌واک به -u- بدل شده است (نوشتنِ l به‌جای r تنها قرارداد خط پهلوی است نه دگرگونی آوایی). معین نیز در حاشیهٔ ریشه‌شناختی خود بر برهان قاطع ص ۲۴۹ (دنبالهٔ حاشیه در ص ۲۵۰) می‌نویسد «پهلوی barbut از یونانی …»، و ویکی‌واژه هم به استناد مکنزی همین را دارد. پس این پیوند (یونانی ← پهلوی) درست است؛ اشکال یک پله بالاتر، در انتساب خودِ barbitos به ریشهٔ آوایی، است.\",\n  \"sources\": [W_BARBAT, A_BARBAT],\n  \"ref_check\": [\n    {\"ref\": \"BQT:249\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 469 = printed p. 249 carries the headword بربط ('نام سازست مشهور، و بعضی گویند بربط ساز عود است، و آن طنبور … باشد کاسه بزرگ و دستهٔ کوتاه') with a footnote marker; the footnote itself is printed on p. 250 under 'بقیهٔ [حاشیهٔ] صفحهٔ ۲۴۹' and reads (OCR leaf 470) 'پهلوی barbut از یونانی …، کلمهٔ یونانی بعدها در زبانهای فرنگی … گردیده (رک: مجلهٔ موسیقی …)'. That is precisely Nourai's Greek > Pahlavi arrow.\"},\n    {\"ref\": \"MON:497\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang-e Farsi entry (read via abadis.ir, which reproduces it): 'بربط (بَ بَ) [معر.] (اِ.) عود، از آلات موسیقی شبیه تار که کاسه‌اش بزرگ‌تر و دسته‌اش کوتاه‌تر است' — the word and gloss are Nourai's, but the dictionary's origin tag there is [معر.] 'Arabicised', not 'Pahlavi < Greek'; the Greek etymology is in Mo'in's Borhan footnote, not in the Farhang entry. (The local MON OCR is the 2-vol Adena reprint with different pagination, so p. 497 of the 6-vol edition could not be located directly.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p. 17 (PHD.txt l. 252; PHD_mackenzie.txt l. 1500)\", \"stance\": \"supports\", \"note\": \"'barbut [blbwt' | N ~] lyre'; and the English-Pahlavi index (PHD.txt l. 2691) 'lyre barbut, kennār'.\"},\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'barbu|barbat'\", \"stance\": \"silent\", \"note\": \"Nyberg's Pahlavi glossary (which covers only the texts of his Manual) has no entry for barbut.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 249 + footnote continued p. 250\", \"stance\": \"supports\", \"note\": \"See ref_check: Mo'in's footnote 'پهلوی barbut از یونانی …'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"barbat «بربط»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian بربط barbat 'a short-necked lute, the ancestor of the ʿūd' continues Middle Persian barbut directly: MP final -ut is lowered to NP -at, and the word is written with Arabic ṭ (بربط instead of *بربت) because it was re-borrowed in Arabic dress — Arabic took barbaṭ from Middle Persian in the early Islamic centuries (the barbaṭ players of the Sasanian court, Bārbad of Jahrom among them, are the reason the instrument is named in every Persian poet), and the Arabicised spelling came back into Persian, which is why Mo'in tags the entry [معر.]. Nourai's Hafez line (بدانسان سوخت چون شمعم که بر من / صراحی گریه و بربط فغان کرد) is a genuine attestation. One competing account should be named: Dehkhoda reports the old native explanation bar 'breast' + bat 'duck', i.e. 'duck-breast', from the shape of the sound-box; this is a folk etymology of the Islamic-period lexicographers, not accepted by MacKenzie, Mo'in's own footnote, or Wiktionary, which keep the Greek route.\",\n  \"derivation_fa\": \"«بربط» در فارسی نو دنبالهٔ مستقیم barbut فارسی میانه است: -ut پایانی به -at بدل شده و املای آن با «ط» (نه «ت») از آنجاست که این واژه در دورهٔ اسلامی از راه عربی بازگشته است؛ عربی barbaṭ را از فارسی میانه گرفت (نوازندگان بربط دربار ساسانی، از جمله باربد جهرمی، سبب حضور پیوستهٔ این واژه در شعر فارسی‌اند) و صورت معرّب دوباره به فارسی راه یافت — به همین سبب معین در فرهنگ خود آن را «[معر.]» نشانه‌گذاری کرده است. بیت حافظ که نورایی آورده («بدان‌سان سوخت چون شمعم که بر من / صراحی گریه و بربط فغان کرد») شاهدی درست است. در برابر این، دهخدا ریشه‌شناسی کهنِ «بر (سینه) + بط (مرغابی)» یعنی «سینهٔ مرغابی» را (به سبب شکل کاسهٔ ساز) نقل می‌کند که ریشه‌شناسی عامیانهٔ فرهنگ‌نویسان دورهٔ اسلامی است و مکنزی، حاشیهٔ خودِ معین و ویکی‌واژه آن را نمی‌پذیرند. ادعای نورایی در این گره درست است.\",\n  \"sources\": [W_BARBAT, A_BARBAT],\n  \"ref_check\": [\n    {\"ref\": \"MON:497\", \"status\": \"partial\", \"note\": \"Mo'in (via abadis.ir): 'بربط (بَ بَ) [معر.] (اِ.) عود، از آلات موسیقی شبیه تار که کاسه‌اش بزرگ‌تر و دسته‌اش کوتاه‌تر است' — supports word, pronunciation and gloss ('a musical instrument'); the origin tag given there is 'Arabicised', the Greek/Pahlavi line being in Mo'in's Borhan footnote instead.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 249 (BQT_v1_pages.txt leaf 469)\", \"stance\": \"supports\", \"note\": \"'بربط … نام سازست مشهور، و بعضی گویند بربط ساز عود است، و آن طنبور … کاسه بزرگ و دستهٔ کوتاه' — the entry Nourai cites, with Mo'in's Pahlavi/Greek footnote.\"},\n    {\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ معین s.v. بربط\", \"stance\": \"partial\", \"note\": \"'[معر.] عود، از آلات موسیقی شبیه تار …'; the same page's Dehkhoda section gives the folk etymology 'بر (سینه) + بط (مرغابی)'.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'barbat|barbut|barbit'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no article on barbat.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt, grep 'barbat|barbut|barbit'\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien likewise has nothing on this word.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p. 17\", \"stance\": \"supports\", \"note\": \"'barbut [blbwt' | N ~] lyre' — the '| N ~' explicitly equates the New Persian word with the Middle Persian one.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"barbaria; barbarus; rheu-barbarum\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"First a structural correction: in the printed book (p. 45) the Latin box is NOT attached to the root spine but hangs from the Greek box — the elbow that feeds it descends from the bottom-left corner of the Greek box, exactly like the elbow that feeds the Pahlavi box. The JSON gives it parent 0; that is an extraction error, and Nourai's own drawing (Greek barbaros -> Latin barbarus) is the correct one, since Latin barbarus is a straight loan from Greek βάρβαρος taken over in the 2nd c. BCE with the Hellenising vocabulary (Plautus already has barbarus of things Italian, as seen through Greek eyes). barbaria 'a foreign country, savagery' is then a Latin derivative in -ia, whence Barbary. The third form is a different matter: rheubarbarum is Medieval Latin, not classical, and it is a re-shaping of Greek ῥᾶ βάρβαρον 'foreign rha (rhubarb)'; only the second element belongs to this root, the first being Greek ῥῆον / ῥᾶ, itself from Persian rēwand 'rhubarb' (Klein s.v. rhubarb, Rheum; hence Nourai's cross-reference to root 'Eres 1', i.e. the river Rha/Volga). So: two words confirmed, the third real but mislabelled as Latin and only half-relevant.\",\n  \"derivation_fa\": \"نخست یک نکتهٔ ساختاری: در صفحهٔ چاپی (ص ۴۵) خانهٔ «لاتین» به ستون ریشه وصل نیست، بلکه مانند خانهٔ «پهلوی» از گوشهٔ پایینِ خانهٔ «یونانی» آویخته است؛ در فایل استخراجی به‌اشتباه فرزند ریشه ثبت شده است. نقشهٔ خودِ نورایی درست است: barbarus لاتین وام‌واژه‌ای است از βάρβαρος یونانی که در سدهٔ دوم پیش از میلاد همراه واژگان یونانی‌مآب وارد لاتین شد (پلاؤتوس آن را دربارهٔ چیزهای ایتالیایی، از دید یونانیان، به کار می‌برد) و barbaria صورت مشتق لاتین با پسوند -ia است. اما rheubarbarum لاتینِ کلاسیک نیست، بلکه لاتینِ سده‌های میانه و بازساختِ ῥᾶ βάρβαρον یونانی «ریوندِ بیگانه» است؛ تنها جزء دوم آن به این ریشه مربوط است و جزء نخست از ῥῆον یونانی و آن از «رِیوند» فارسی می‌آید (کلاین ذیل rhubarb و Rheum). پس دو واژه پذیرفتنی و واژهٔ سوم درست ولی با برچسب زبانی نادرست است؛ حکم: با احتیاط پذیرفتنی.\",\n  \"sources\": [E_BARB, E_RHUBARB],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. baba- sense 8 lists the Greek word and the English derivatives BARBARIAN, BARBARISM, BARBAROUS but does not print the Latin forms; the Watkins index has no RHUBARB at all (grep 'RHUBARB' in AHD_watkins1985.txt: no hit), because AHD treats rhubarb's first element as a separate, non-IE item.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4427 (barbaric), l. 4431 (Barbary), l. 32823 (rhubarb)\", \"stance\": \"supports\", \"note\": \"'barbaric — OF. barbarique, fr. L. barbaricus, fr. Gk. βαρβαρικός, fr. βάρβαρος'; 'Barbary — OF. Barbarie, fr. L. barbaria, \\\"a foreign country\\\", fr. barbarus'; 'rhubarb … fr. ML. rheubarbarum. The first element … derives fr. L. rheum, fr. Gk. ῥῆον, ultimately fr. Pers. rewend … Cp. the ML. form rhabarbarum, which comes fr. Gk. ῥᾶ βάρβαρον, lit. \\\"foreign rhubarb\\\"'.\"},\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 92\", \"stance\": \"supports\", \"note\": \"'gr. βάρβαρος … (woraus lat. barbarus)' — Pokorny too makes Latin barbarus a loan FROM Greek, i.e. the arrow the printed page draws.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 107\", \"stance\": \"supports\", \"note\": \"Same wording: 'gr. βάρβαρος „nicht griechisch …“, woraus (lat. barbarus)'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt l. 29010\", \"stance\": \"supports\", \"note\": \"'… fr. Lat. barbarus orig. \\\"foreign, a foreigner\\\", REW 945' — Buck's article on 'brave/wild' takes Latin barbarus as the base of the Romance forms.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"English\", \"words\": \"barbarian, barbarous, Barbara, rhubarb\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All four are Latin-mediated. barbarian is Greek βάρβαρος > L. barbarus > MedL. barbarinus / OF barbarin, with English -ian substituted (early 15c.); barbarous is Latin barbarus with -ous for -us (Klein s.v.); Barbara is the Latin feminine of barbarus, 'the foreign woman', spread as a saint's name (Klein l. 4426: 'L., prop. fem. of barbarus … fr. Gk. βάρβαρος'); rhubarb is ME rubarbe from MF reubarbe from ML rheubarbarum 'foreign rha', the plant reaching medieval Europe from China and Tibet by way of Russia — which is why it was 'foreign'; the spelling with -h- is an 18th-c. latinisation. Nothing here is doubtful.\",\n  \"derivation_fa\": \"هر چهار واژه از راه لاتین به انگلیسی رسیده‌اند: barbarian از βάρβαρος یونانی ← barbarus لاتین ← barbarinus لاتینِ میانه/barbarin فرانسهٔ کهن با پسوند انگلیسی -ian (اوایل سدهٔ پانزدهم)؛ barbarous همان barbarus لاتین با جانشینی پسوند -ous؛ Barbara صورت مؤنث لاتینِ barbarus یعنی «زن بیگانه» که به‌عنوان نام قدیسه رواج یافت (کلاین)؛ و rhubarb از rubarbe انگلیسی میانه ← reubarbe فرانسهٔ میانه ← rheubarbarum لاتینِ سده‌های میانه «ریوندِ بیگانه»، چون این گیاه از چین و تبت و از راه روسیه به اروپا می‌رسید. «h» در املای امروزی افزودهٔ سدهٔ هجدهم است. ادعای نورایی در این گره درست است.\",\n  \"sources\": [E_BARB, E_RHUBARB],\n  \"ref_check\": [oew()],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt ll. 4426-4431, 32823\", \"stance\": \"supports\", \"note\": \"Entries barbarian, barbaric, barbarism, barbarous, Barbara, Barbary and rhubarb, all traced to Gk. βάρβαρος through Latin, exactly as the box has them.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (AHD_watkins1985.txt ll. 1276-1278)\", \"stance\": \"partial\", \"note\": \"'BARBARIAN baba-  BARBARISM baba-  BARBAROUS baba-' — the appendix covers three of the four; RHUBARB and the name Barbara are not indexed there.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt (Concise Skeat), s.v. barbarous / rhubarb\", \"stance\": \"supports\", \"note\": \"Skeat's concise dictionary refers barbarous to Gk. βάρβαρος (cross-referred from 'Bauble … Barbarous'), the standard account.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Russian\", \"words\": \"balalayka\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Russian балалайка is a real word (first recorded in the 18th c.) for the triangular three-stringed lute, and the mainstream etymology does put it in this echoic family: Wiktionary derives it from a dialectal балабайка, from an onomatopoeic stem балабай- plus the diminutive -ка, comparing балаболить 'to chatter', балакать 'to talk, chatter', балагурить 'to jest'; Watkins/AHD prints 'Russian balalaika, balalaika (imitative of the sound): BALALAIKA' under baba-, and Klein reports Berneker's derivation from Russ. balabolit'. Pokorny himself lists 'russ. balákat' \\\"schwätzen\\\", balamút \\\"Schwätzer\\\"' under bāba-. Two reservations keep this from 'confirmed': (a) the connection is by comparison with an imitative family, not by a sound-law chain, so it is a plausible rather than a demonstrable descent from PIE; (b) Lokotsch no. 198 derives Russian балалайка from a Tatar balalaika 'lute', making it an oriental loanword rather than a Slavic imitative formation — a minority view today, but it is the one specialist treatment of the word in the local library.\",\n  \"derivation_fa\": \"«بالالایکا» واژه‌ای اصیل در روسی (نخستین ضبط‌ها از سدهٔ هجدهم) برای سازی زهی و سه‌سیمه با کاسهٔ مثلثی است و ریشه‌شناسی رایج آن را در همین خانوادهٔ آوایی می‌گذارد: ویکی‌واژه آن را از گونهٔ گویشی балабайка و از ستاک آوایی балабай- به‌همراه پسوند تصغیر -ка می‌داند و با балаболить «وراجی کردن» و балакать «گپ زدن» می‌سنجد؛ واتکینز/AHD نیز ذیل baba- می‌آورد «روسی balalaika (تقلید آوا)». پوکورنی هم balákat' و balamút روسی را ذیل همین ریشه یاد می‌کند. با این حال دو نکته مانع از حکم قطعی است: نخست آنکه این پیوند بر پایهٔ سنجش خانوادهٔ آوایی است نه زنجیرهٔ قانون‌های آوایی؛ دوم آنکه لوکوچ (شمارهٔ ۱۹۸) балалайка روسی را وام‌واژه‌ای از تاتاری balalaika «عود» می‌داند، یعنی خاستگاهی ترکی نه اسلاوی. بنابراین «با احتیاط پذیرفتنی».\",\n  \"sources\": [W_BALARU, W_BALA],\n  \"ref_check\": [\n    {\"ref\": \"AHD:100\", \"status\": \"supports\", \"note\": \"The New College Edition's body page 100 (alphabetically the b-a-l range) is not in the local library, but the Appendix that goes with it, AHD_watkins1985.txt s.v. baba- sense 6, reads 'Russian balalaika, balalaika (imitative of the sound): BALALAIKA' — i.e. AHD does place the word under this root, which is what the arrow claims.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt ll. 4303-4306 s.v. balalaika\", \"stance\": \"supports\", \"note\": \"'balalaika … — Russ. balalaika, which, according to Erich Berneker … is rel. to Russ. balabolit', \\\"to chatter, babble\\\", from the I.-E. imitative base *balb-, whence also L. balbus'.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 198 (LKT.txt l. 669)\", \"stance\": \"contradicts\", \"note\": \"'198. Tat. balalaika: \\\"Laute\\\"; hieraus russ. balalaika, klr. balabaika, serb. balalajka … dtsch. Balalaika. [Gorjajew 10.]' — Lokotsch makes the Russian word a Tatar loan, not an inherited imitative formation.\"},\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 92\", \"stance\": \"partial\", \"note\": \"Under bāba- Pokorny lists 'die slav. Sippe von russ. balákath \\\"schwätzen\\\", balamút \\\"Schwätzer, Kopfverdreher\\\"' — the family, though not balalaika itself.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt l. 15151\", \"stance\": \"silent\", \"note\": \"Webster's New Twentieth Century vol. 1 has the headword BALALAIKA but the OCR of the entry carries no etymology.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"bâlâlâykâ «بالالایکا»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian بالالایکا is a 20th-century loan of the Russian instrument name, taken over unchanged (Russian balalájka > Pers. bālālāykā, the final -ka kept because Persian has no reason to reanalyse it as a suffix). The route is direct Russian-Persian contact — the Russian presence in northern Iran, Russian-trained military bands and, above all, translated writing about European music — not through French or English, which is why the Persian form has -ay- (Russ. -ай-) rather than the -ai- of English balalaika. The word is a name for the foreign instrument only; it never denoted anything Persian, exactly as Nourai's gloss says.\",\n  \"derivation_fa\": \"«بالالایکا» وام‌واژه‌ای است از روسی (балалайка) که در سدهٔ چهاردهم خورشیدی و بی‌هیچ دگرگونی آوایی وارد فارسی شده است؛ پایانهٔ -کا نگاه داشته شده چون در فارسی پسوند شناخته‌شده‌ای نیست تا حذف شود. راه ورود آن تماس مستقیم روسی-فارسی است (حضور روس‌ها در شمال ایران، دسته‌های موسیقی نظامی و نوشته‌های ترجمه‌شده دربارهٔ موسیقی اروپایی) نه از راه فرانسه یا انگلیسی؛ گواه آن همان -ای- (=ай روسی) در صورت فارسی است. این واژه در فارسی تنها نام همان ساز بیگانه است، درست همان‌گونه که نورایی معنی کرده است.\",\n  \"sources\": [W_BALARU],\n  \"ref_check\": [\n    {\"ref\": \"VOP:84\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vāžehā-ye orupāyi dar fārsi (1371/1992): refs_online.json records no digital copy anywhere (archive.org, ketabnak, noorlib all searched, re-searched 2026-09); purchase only.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt / MON_part2.txt, grep 'بالالایکا'\", \"stance\": \"silent\", \"note\": \"Mo'in's Farhang (2-vol reprint OCR) has no entry for بالالایکا — the loan is too recent/too marginal for it.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep 'بالالایکا'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary of Persian does not list the word.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 198\", \"stance\": \"partial\", \"note\": \"Documents the spread of the Russian word into other languages ('frz. la balaleïka, dtsch. Balalaika'), the same kind of modern borrowing as the Persian one, but does not mention Persian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"English\", \"words\": \"balalaika\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English balalaika is a straight 19th-century borrowing of Russian балалайка (first English attestations in travel writing on Russia; the instrument became widely known in the West with V. V. Andreyev's balalaika orchestras from the 1880s). Wiktionary: 'From Russian балала́йка (balalájka)'; Klein s.v. balalaika, 'Russ. balalaika'. No intermediate language is involved, and Nourai's arrow Russian -> English is right; only the further ascent to the imitative root carries the reservations noted at node #6.\",\n  \"derivation_fa\": \"«balalaika» انگلیسی وام‌واژه‌ای مستقیم از روسی балалайка در سدهٔ نوزدهم است (نخست در سفرنامه‌های روسیه، و سپس با ارکسترهای بالالایکای واسیلی آندریف از دههٔ ۱۸۸۰ در غرب شناخته شد). ویکی‌واژه: «از روسی балала́йка»؛ کلاین نیز همین را دارد. هیچ زبان واسطی در میان نیست و پیکان نورایی (روسی ← انگلیسی) درست است؛ تنها تردید، همان است که در گرهٔ ۶ دربارهٔ پیوند با ریشهٔ آوایی گفته شد.\",\n  \"sources\": [W_BALA],\n  \"ref_check\": [\n    {\"ref\": \"AHD:100\", \"status\": \"supports\", \"note\": \"Body page not in the local library; the accompanying Watkins appendix (AHD_watkins1985.txt s.v. baba- 6) prints 'Russian balalaika … : BALALAIKA', i.e. AHD's own account is Russian > English under this root, as drawn.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4303 s.v. balalaika\", \"stance\": \"supports\", \"note\": \"'balalaika, n., a Russian stringed instrument with a triangular body. — Russ. balalaika …'.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt l. 15151\", \"stance\": \"silent\", \"note\": \"Headword present, etymology not legible in the OCR.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 198\", \"stance\": \"partial\", \"note\": \"Lists the western European forms taken from Russian; consistent with a Russian > English loan, though Lokotsch's own source for the Russian word is Tatar.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Old French\", \"words\": \"babine\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Old/Middle French babine 'the pendulous lip of an animal, esp. of an ape' is a real word of imitative origin, built on the same bab- of babiller 'to prattle', bavarder, bave — so its ascent from the root box is sound. What is only plausible is its role as the ancestor of baboon: Klein (s.v. baboon) says Old French babuin/babouin is 'a blend of babine, \\\"the pendulous lip of certain animals, esp. monkeys\\\" (the baboon has prominent lips), and baboue, \\\"wry, ugly face\\\"', citing Bloch-Wartburg p. 49; Etymonline gives only baboue 'grimacing' plus the alternative 'imitative of an ape's babbling cries'; Skeat and Webster print 'origin uncertain'. So babine is one of two candidate bases, not the established one.\",\n  \"derivation_fa\": \"babine در فرانسهٔ کهن و میانه به معنی «لب آویختهٔ جانوران، به‌ویژه میمون» واژه‌ای واقعی و آواگونه است و بر همان ستاک bab- ساخته شده که در babiller «وراجی کردن» و bave دیده می‌شود؛ پس پیوند آن با ریشهٔ این نمودار درست است. آنچه تنها «با احتیاط پذیرفتنی» است، نقش آن به‌عنوان خاستگاه baboon است: کلاین صورت فرانسهٔ کهن babuin/babouin را «آمیزه‌ای از babine و baboue (چهرهٔ کج و زشت)» می‌داند (به استناد بلوخ-وارتبورگ ص ۴۹)، حال آنکه اتیمولوژی‌آنلاین تنها baboue را می‌آورد و اسکیت و وبستر «خاستگاه نامعلوم» نوشته‌اند. پس babine یکی از دو نامزد است نه پایهٔ قطعی.\",\n  \"sources\": [E_BABOON],\n  \"ref_check\": [oew()],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4225 s.v. baboon\", \"stance\": \"supports\", \"note\": \"'ME. baboin, fr. OF. babuin, babouin …, a blend of babine, \\\"the pendulous lip of certain animals, esp. monkeys\\\" (the baboon has prominent lips), and baboue, \\\"wry, ugly face\\\"; both babine and baboue are of imitative origin. See Bloch-Wartburg, DELF., p.49.'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt l. 1266 s.v. Baboon\", \"stance\": \"partial\", \"note\": \"'F. babouin … Law L. babewynus, a baboon (a.d. 1295). Origin uncertain.'\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4221 s.v. babble\", \"stance\": \"supports\", \"note\": \"The imitative base is explicit: 'from the I.-E. imitative base *bab- … F. babiller, \\\"to stutter, stammer\\\"; cp. babe, baboon, bauble' — i.e. Klein files babine/baboon under the same base as the root box.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"English\", \"words\": \"baboon\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"English baboon is attested from c. 1400 (ME babewyn, baboin) and is a loan of Old French babuin/babouin, which in the 13th c. meant 'gaping figure, gargoyle; simpleton' before it meant 'ape'; Medieval Latin babewynus is recorded 1295 (Skeat). The step from French to English is certain. What is not certain is the French word's own base: Klein's blend of babine + baboue (Nourai's route through babine), Etymonline's baboue 'grimacing' or direct imitation of an ape's babbling, and Skeat's and Webster's 'origin unknown' are all on the table; Lokotsch no. 1365 goes further and derives It. babuino and Eng. baboon from Arabic maimūn 'monkey' (with m > b), which Etymonline reverses ('Arabic maimun probably is from the European words'). Verdict plausible: the English word does come from French babuin, and that word is very likely of this imitative family, but the specific parent babine is one hypothesis among several.\",\n  \"derivation_fa\": \"«baboon» انگلیسی از حدود ۱۴۰۰ م. (صورت‌های babewyn، baboin) ضبط شده و وام‌واژه‌ای است از babuin/babouin فرانسهٔ کهن که در سدهٔ سیزدهم معنی «چهرهٔ دهان‌گشوده، ناودان‌سرِ کلیسا؛ ساده‌لوح» داشت و سپس «میمون» شد؛ صورت لاتینِ میانهٔ babewynus در ۱۲۹۵ م. ثبت است. گام فرانسه ← انگلیسی قطعی است، اما پایهٔ خودِ واژهٔ فرانسه قطعی نیست: کلاین آن را آمیزهٔ babine و baboue می‌داند (همان راهی که نورایی برگزیده)، اتیمولوژی‌آنلاین baboue یا تقلید مستقیم آوای میمون را ترجیح می‌دهد، اسکیت و وبستر «نامعلوم» می‌نویسند، و لوکوچ (شمارهٔ ۱۳۶۵) آن را از «میمون» عربی می‌گیرد. پس: با احتیاط پذیرفتنی.\",\n  \"sources\": [E_BABOON],\n  \"ref_check\": [oew()],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4225\", \"stance\": \"supports\", \"note\": \"See node #9: Klein's blend etymology, with babine as one component.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt l. 1266\", \"stance\": \"partial\", \"note\": \"'Origin uncertain.'\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt l. 14475\", \"stance\": \"partial\", \"note\": \"'bab-oon', n. [ME. babewyne; OFr. babuin, baboon, origin of name unknown.]'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1365 (LKT.txt l. 3166)\", \"stance\": \"contradicts\", \"note\": \"'Ar. maimūn \\\"Affe\\\" … ferner [mit Wechsel von m zu b] it. babuino; engl. baboon \\\"Affe\\\"' — an Arabic source instead of a French imitative one.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt, s.v. baboon\", \"stance\": \"silent\", \"note\": \"The Funk & Wagnalls vol. 1 OCR carries the headword only in compounds (e.g. 'cheek-pouch, as of a baboon'); the etymology line did not survive the scan.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Italian\", \"words\": \"bambino\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The word is right, the gloss is not. Italian bambino means 'baby, little child' and is the diminutive of bambo 'simple, childish' — 'It., \\\"baby\\\", dimin. of bambo, \\\"simple\\\", which is of imitative origin' (Klein l. 4345); Watkins/AHD prints 'Italian bambo, child, simpleton: BAMBINO' under baba-, so the ascent from the root box is confirmed. But Nourai's gloss, 'originally meant a wild and savage man; later changed to a brave and courageous man', is not the history of bambino at all: it is the history of Italian BRAVO ('orig. meaning \\\"wild, savage\\\"', Klein s.v. brave). The printed page (p. 45) really does read this way, so this is the book's own error, not the extraction's — the whole Italian-French-English sub-branch has been built on the wrong Italian lemma. Modern scholarship keeps bambino and bravo entirely apart.\",\n  \"derivation_fa\": \"خودِ واژه درست است، معنی آن نه. «bambino» در ایتالیایی «کودک، نوزاد» است و مصغّر bambo «ساده، کودکانه» و از خانوادهٔ واژه‌های آواگونه است (کلاین؛ و واتکینز ذیل baba- می‌آورد «ایتالیایی bambo، کودک، ساده‌لوح: BAMBINO»)، پس پیوند آن با ریشهٔ این نمودار درست است. اما معنایی که نورایی داده — «در اصل به معنی مرد وحشی و درنده‌خو، سپس دلیر و شجاع» — تاریخِ bambino نیست، بلکه تاریخِ bravo ایتالیایی است. صفحهٔ چاپی کتاب (ص ۴۵) نیز همین را دارد، پس خطا از کتاب است نه از خوانش اسکن؛ و بر پایهٔ همین خطا کل شاخهٔ ایتالیایی-فرانسوی-انگلیسی روی سرواژهٔ نادرست بنا شده است. پژوهش امروزی bambino و bravo را دو واژهٔ جدا می‌داند.\",\n  \"sources\": [E_BRAVE],\n  \"ref_check\": [oew()],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4345 s.v. bambino; l. 5561 s.v. brave\", \"stance\": \"contradicts\", \"note\": \"'bambino, n., a little child … — It., \\\"baby\\\", dimin. of bambo, \\\"simple\\\", which is of imitative origin' versus 'brave, adj. — F., fr. It. bravo, orig. meaning \\\"wild, savage\\\", fr. L. barbarus' — the gloss Nourai attaches to bambino is Klein's gloss of bravo.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. baba- sense 3 and index l. 1276\", \"stance\": \"partial\", \"note\": \"'3. Italian bambo, child, simpleton: BAMBINO' and 'BAMBINO baba-' — the word belongs to the root, with the 'child' sense only; the index has no entry for BRAVE or BRAVO under any root.\"},\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 91\", \"stance\": \"partial\", \"note\": \"'ital. babbo \\\"Vater\\\"' and the bam-b- variants are listed under bāba-, supporting the Italian nursery words but saying nothing about a 'savage man' sense.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"French\", \"words\": \"bravo\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"French bravo (interjection, borrowed from Italian in the 18th c., first in the opera house; the adjective brave is earlier, 15th c.) does not come from Italian bambino. Its source is Italian bravo, and the standard accounts derive that from Latin barbarus — Klein: 'brave, adj. — F., fr. It. bravo, orig. meaning \\\"wild, savage\\\", fr. L. barbarus, \\\"foreigner\\\" (through the intermediate forms *brabarus, *brabus)'; Buck (SYN p. 1090 area, l. 29010) likewise 'fr. Lat. barbarus orig. \\\"foreign, a foreigner\\\", REW 945'; Funk & Wagnalls 'prob. < L. barbarus; see barbarous'. Etymonline prefers a different source again (Medieval Latin bravus 'cutthroat', with Latin pravus 'crooked, depraved'), calling the barbarus connection 'less likely' and suspecting 'a confusion of two or more words'; Skeat says flatly 'Etym. unknown; none of the explanations are satisfactory'. Under every one of these accounts the arrow drawn here is wrong: bravo belongs, if anywhere on this page, under the Latin barbarus box (node #4), not under bambino.\",\n  \"derivation_fa\": \"«bravo» فرانسوی (شبه‌جملهٔ تحسین، وام‌گرفته از ایتالیایی در سدهٔ هجدهم و نخست در فضای اپرا؛ صفت brave کهن‌تر است، سدهٔ پانزدهم) از bambino ایتالیایی نمی‌آید. خاستگاه آن bravo ایتالیایی است و شرح‌های معیار آن را از barbarus لاتین می‌گیرند: کلاین می‌نویسد «brave از فرانسه، از bravo ایتالیایی که در اصل «وحشی، درنده» بوده، از barbarus لاتین از راه صورت‌های میانی *brabarus و *brabus»؛ باک و فرهنگ فانک و واگنالز نیز همین را دارند. در برابر، اتیمولوژی‌آنلاین bravus لاتینِ میانه و pravus لاتین «کج، تباه» را ترجیح می‌دهد و پیوند با barbarus را «کم‌احتمال‌تر» می‌خواند، و اسکیت می‌نویسد «ریشه نامعلوم است و هیچ‌یک از توضیح‌ها بسنده نیست». بر پایهٔ هر یک از این نظرها پیکانِ کشیده‌شده نادرست است: جای bravo در این صفحه — اگر جایی داشته باشد — زیر خانهٔ barbarus لاتین (گرهٔ ۴) است نه زیر bambino. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [E_BRAVE],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own in the book (refs = None); the branch's references are those of the Italian box (OEW:22) and of the English box (AHD; OEW).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt ll. 5561-5563 (brave, bravo), l. 5486 (brab)\", \"stance\": \"contradicts\", \"note\": \"'brave, adj. — F., fr. It. bravo, orig. meaning \\\"wild, savage\\\", fr. L. barbarus, \\\"foreigner\\\" (through the intermediate forms *brabarus, *brabus); with change of meaning from \\\"wild\\\" to \\\"courageous\\\"'; 'bravo, n., brigand. — It. bravo, fr. L. barbarus.' No mention of bambino.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt l. 29010\", \"stance\": \"contradicts\", \"note\": \"'… sense > It. bravo > Fr. brav[e]), fr. Lat. barbarus orig. \\\"foreign, a foreigner\\\", REW 945' — the Romance chain runs from barbarus, not from bambino.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt l. 2227 s.v. Bravo\", \"stance\": \"partial\", \"note\": \"'F. brave … The same as Ital., Span., and Port. bravo. Etym. unknown; none of the explanations are satisfactory.'\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt l. 48963, 48974 s.v. bravo\", \"stance\": \"contradicts\", \"note\": \"'[F., < It. or Sp., bravo, brave, wild; prob. < L. barbarus; see barbarous.]'\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Persian\", \"words\": \"brâvo «براوو»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian براوو is a modern loan of French bravo, taken over in the late Qajar/Pahlavi period along with the rest of the French theatrical and school vocabulary (the French-medium Dar al-Fonun and the Iranian stage of the 1920s-30s are the obvious channels). The Persian spelling with two waw (بـراوو) renders French [bravo] with a final -o that Persian writes ـو, and the initial cluster br- is kept unbroken, as in other direct French loans (برنز bronz, بروشور boroshur). Nourai's arrow French -> Persian is right; only its parent, the Italian box, is wrong (node #12).\",\n  \"derivation_fa\": \"«براوو» وام‌واژه‌ای نو از bravo فرانسوی است که در اواخر دورهٔ قاجار و در دورهٔ پهلوی، همراه با دیگر واژگان تئاتری و مدرسه‌ای فرانسوی، وارد فارسی شده است (دارالفنون فرانسه‌زبان و صحنهٔ نمایش ایران در دههٔ ۱۳۰۰ آشکارترین راه‌های ورود آن‌اند). املای فارسی با دو واو، صورت [bravo] فرانسوی را می‌نمایاند و خوشهٔ آغازین br- بی‌شکستن نگاه داشته شده است، مانند دیگر وام‌واژه‌های مستقیم فرانسوی (برنز، بروشور). پیکان «فرانسوی ← فارسی» درست است؛ آنچه نادرست است خانهٔ مادرِ فرانسوی، یعنی «bambino ایتالیایی»، است (گرهٔ ۱۲).\",\n  \"sources\": [E_BRAVE],\n  \"ref_check\": [\n    {\"ref\": \"VOP:87\", \"status\": \"not_checked\", \"note\": \"Moshiri's dictionary of European words in Persian has no digital copy of any kind (refs_online.json, re-searched 2026-09); the page could not be read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt, grep براوو\", \"stance\": \"silent\", \"note\": \"No entry for براوو in the Mo'in OCR — the interjection is treated as a foreign word and is not lemmatised.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt, grep براوو\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary does not carry it.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 5563 s.v. bravo, interj.\", \"stance\": \"supports\", \"note\": \"'bravo, interj., well done!; n., the shout \\\"bravo\\\". — It. bravo, \\\"the brave man\\\", used in applauding actors, etc.' — the theatrical use that Persian, like French and English, borrowed.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\", \"words\": \"brave, bravo\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The language chain is right but the parent word is wrong. English brave is a late-15th-c. loan of French brave 'splendid, valiant', itself from Italian bravo; English bravo as an exclamation is 1761, straight from Italian (the noun bravo 'hired killer' is older, 1590s). None of this passes through bambino: Klein takes Italian bravo from Latin barbarus through *brabarus, *brabus, Buck the same, Funk & Wagnalls 'prob. < L. barbarus', while Etymonline prefers Medieval Latin bravus / Latin pravus and Skeat declares the etymology unknown. It is also worth recording that Nourai's own citation fails here: the Watkins/AHD appendix, which he cites as 'AHD', has no BRAVE or BRAVO entry under baba- or any other root (grep of AHD_watkins1985.txt finds neither word in the index), precisely because AHD does not consider brave to be of Indo-European descent in this sense.\",\n  \"derivation_fa\": \"زنجیرهٔ زبان‌ها درست است ولی واژهٔ مادر نادرست. «brave» انگلیسی وام‌واژه‌ای از brave فرانسوی (اواخر سدهٔ پانزدهم) است و آن خود از bravo ایتالیایی می‌آید؛ «bravo» به‌عنوان شبه‌جملهٔ تحسین در ۱۷۶۱ م. مستقیماً از ایتالیایی گرفته شده است. هیچ‌یک از این‌ها از bambino نمی‌گذرد: کلاین و باک bravo ایتالیایی را از barbarus لاتین می‌گیرند، فرهنگ فانک و واگنالز «احتمالاً از barbarus لاتین» می‌نویسد، اتیمولوژی‌آنلاین bravus/pravus لاتین را ترجیح می‌دهد و اسکیت ریشه را نامعلوم می‌داند. افزون بر این، ارجاع خودِ نورایی در اینجا درست درنمی‌آید: در پیوست ریشه‌های هندواروپایی واتکینز/AHD نه BRAVE هست و نه BRAVO (جست‌وجو در متن نمایه هیچ‌کدام را نمی‌یابد)، زیرا AHD این واژه را از تبار هندواروپایی نمی‌شمارد. پس این گره را پژوهش امروزی رد می‌کند.\",\n  \"sources\": [E_BRAVE],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"AHD_watkins1985.txt: the index lists BAMBINO, BABBLE, BABE, BABY, BABU, BALALAIKA, BARBARIAN, BARBARISM, BARBAROUS and BOOBY under baba-, but grep for 'BRAVE'/'BRAVO' in the whole appendix returns nothing — AHD does not derive brave/bravo from this (or any) IE root.\"},\n    {\"ref\": \"OEW\", \"status\": \"not_checked\", \"note\": \"Shipley 1984 not readable (lending-only).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt ll. 5561-5563\", \"stance\": \"contradicts\", \"note\": \"'brave, adj. — F., fr. It. bravo … fr. L. barbarus … See barbarian and cp. brab' — Italian bravo, not bambino, and via the Latin box of this very page.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt l. 29010\", \"stance\": \"contradicts\", \"note\": \"The Romance sense-history 'It. bravo > Fr. brave' from Lat. barbarus.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt ll. 2226-2228\", \"stance\": \"partial\", \"note\": \"'Bravo. (F.) F. brave … Etym. unknown; none of the explanations are satisfactory.'\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt ll. 48963, 48974\", \"stance\": \"contradicts\", \"note\": \"'[F., < It. or Sp., bravo, brave, wild; prob. < L. barbarus; see barbarous.]'\"}\n  ]\n})\n\nN.append({\n  \"id\": 15, \"lang\": \"Hindustani\", \"words\": \"bâbŭ\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Hindi/Urdu बाबू bābū is real and does belong to this nursery family: Wiktionary derives it from Proto-New-Indo-Aryan *bābba + the Middle Indo-Aryan suffix -uka-, 'imitative of baby talk', and Watkins/AHD prints 'Hindi bābū, father: BABU' as sense 9 of baba-. So the arrow root -> Hindustani is confirmed. Nourai's gloss is a little off: the word means 'father, papa' and, as a title, 'sir, Mr' — a term of respect prefixed or suffixed to a name, and in Bengal from the 19th c. 'native clerk who writes English'. Hobson-Jobson ('Beng. and H. Bābū … Properly a term of respect attached to a name, like Master or Mr.') and Whitworth ('Bengali bābu, perhaps from the Sanskrit pitṛ, a father') both give the Sanskrit derivations as guesses; those guesses are now abandoned in favour of the baby-talk origin, which is exactly Nourai's root.\",\n  \"derivation_fa\": \"«bābū» در هندی و اردو (बाबू) واژه‌ای واقعی و از همین خانوادهٔ کودکانه است: ویکی‌واژه آن را از *bābba در هندوآریایی نوِ آغازین با پسوند -uka- هندوآریایی میانه می‌داند و «تقلید زبان کودکانه» می‌خواند، و واتکینز/AHD نیز ذیل baba- می‌آورد «هندی bābū، پدر: BABU». پس پیوند ریشه ← هندوستانی درست است. تنها معنی‌ای که نورایی داده اندکی نادقیق است: این واژه «پدر، بابا» و در کاربرد لقبی «آقا، جناب» است که به نام کسان می‌افزایند، و از سدهٔ نوزدهم در بنگال «منشی بومی انگلیسی‌دان» نیز معنی می‌دهد. هابسن-جابسن و ویتورث ریشهٔ سنسکریت (pitṛ / vapra) را تنها به‌گمان آورده‌اند و امروز همان خاستگاه کودکانه پذیرفته است.\",\n  \"sources\": [W_BABU],\n  \"ref_check\": [oew()],\n  \"consulted\": [\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. BABOO (HJB.txt ll. 2390 ff.)\", \"stance\": \"partial\", \"note\": \"'BABOO, s. Beng. and H. Bābū [Skt. vapra, \\\"a father\\\"]. Properly a term of respect attached to a name, like Master or Mr. … the word has [come] often to signify \\\"a native clerk\\\" who writes English.' — the gloss, with a Sanskrit guess for the origin.\"},\n    {\"src\": \"AID\", \"where\": \"Whitworth, Anglo-Indian Dictionary p. 27 (AID.txt l. 688)\", \"stance\": \"partial\", \"note\": \"'Baboo. [Bengali, bābu, perhaps from the Sanskrit pitri, a father.] A term of respect formerly applied in upper India to the younger sons of a rāja …'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. baba- sense 9\", \"stance\": \"supports\", \"note\": \"'9. Hindi bābū, father: BABU.'\"},\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 91\", \"stance\": \"silent\", \"note\": \"Pokorny's bāba- entry lists Greek, Latin, Italian, Albanian, English, Swedish, German, Lithuanian and Slavic nursery words but no Indo-Aryan bābū.\"}\n  ]\n})\n\nN.append({\n  \"id\": 16, \"lang\": \"Persian\", \"words\": \"bâb 3 «باب ۳ ( بابو )»\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The Persian word exists but the borrowing from Hindustani is not supported — and it is contradicted by the very reference Nourai cites. Mo'in's own entry reads 'بابو [قس. باب] (اِ.) پدر، بابا؛ بزرگ قلندران و درویشان؛ به معنی بابا که در اوایل اسماء برای شفقت … افزایند'، i.e. 'compare bāb', a Persian nursery word for 'father', used as an affectionate title before names and as the title of the head of the qalandars and dervishes; and his entry for باب itself reads '[= بابا - بابو] (اِ.) پدر، بابا، اب'. In other words Mo'in makes bāb / bābā / bābū one native Persian family, not an Indian loan. That is also the natural conclusion: بابا is attested in Persian from the earliest New Persian texts (and MP has the same nursery formation), the Persian and the Indo-Aryan words are parallel creations from the same babbling syllable, and if anything the honorific use travelled with Persian as the chancery language of Muslim India rather than the other way round. Nourai's own chart note ('compare with the Persian word bâbâ:father — see root Pa') half-admits this. Verdict: the word and its meaning are right, the arrow Hindustani -> Persian is disputed. The compound بابوالخیر in the extra field is a name/title of the same formation.\",\n  \"derivation_fa\": \"واژهٔ فارسی هست، اما وام‌گیری آن از هندوستانی پشتوانه ندارد و درست همان مرجعی که نورایی به آن ارجاع داده خلافش را می‌گوید. معین در فرهنگ خود می‌نویسد: «بابو [قس. باب] (اِ.) پدر، بابا. بزرگ قلندران و درویشان. به معنی بابا که در اوایل اسماء برای شفقت … افزایند» و ذیل «باب» نیز «[= بابا - بابو] (اِ.) پدر، بابا، اب». یعنی معین «باب/بابا/بابو» را یک خانوادهٔ فارسیِ بومی می‌داند نه وام‌واژه‌ای هندی. این نتیجه طبیعی هم هست: «بابا» از کهن‌ترین متن‌های فارسی نو گواه دارد، صورت فارسی و صورت هندوآریایی هر دو ساخته‌های موازی از همان هجای کودکانه‌اند، و اگر جابه‌جایی‌ای رخ داده باشد کاربرد لقبی آن با زبان فارسی — زبان دیوانی هند اسلامی — به هند رفته است نه برعکس. خودِ یادداشت نورایی («با واژهٔ فارسی بابا: پدر بسنجید؛ رک. ریشهٔ Pa») نیمی از این را می‌پذیرد. پس معنی و ضبط درست است، ولی پیکان «هندوستانی ← فارسی» را پژوهش امروزی رد می‌کند. ترکیب «بابوالخیر» نیز از همین ساخت است.\",\n  \"sources\": [W_BABU],\n  \"ref_check\": [\n    {\"ref\": \"MON:430\", \"status\": \"contradicts\", \"note\": \"MON_part1.txt l. 19647 (2-vol Adena reprint, p. 334 of that edition; the 6-vol pagination Nourai cites could not be matched directly): 'بابو: [قس. باب] (اِ.) پدر، بابا. بزرگ قلندران و درویشان. به معنی بابا که در اوایل اسماء برای شفقت با مجرد تلقیب افزایند و گویند.' and l. 19574 'باب: [= بابا - بابو] (اِ.) پدر، بابا، اب.' Mo'in derives the word from Persian bāb/bābā and gives no Indian source; his lexicon marks foreign origins with bracketed tags ([هند.], [ع.], [فر.]) and there is none here.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt ll. 19574, 19591, 19647\", \"stance\": \"contradicts\", \"note\": \"See ref_check; also 'بابا: [= باب - بابو] (اِ.) پدر؛ باب، اب. پدربزرگ … عنوان عارفان و …' — one native family.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', headwords باب / بابا (BQT_v1)\", \"stance\": \"partial\", \"note\": \"Borhan has بابا as a Persian word of address for elders and holy men, with no foreign tag; it does not treat بابو as an Indian import.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt [pdf page 101] = printed p. 100\", \"stance\": \"contradicts\", \"note\": \"Aryanpur files Persian «بابا (واژه‌ی کودکانه به چم \\\"پدر\\\")» directly under the Indo-European nursery root, with Kurdish, Latin, French, Spanish and Portuguese parallels — i.e. as a native formation, not a loan from Hindustani.\"},\n    {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. BABOO\", \"stance\": \"partial\", \"note\": \"Documents the Indian word's own history and its Anglo-Indian career; says nothing about it being lent to Persian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 17, \"lang\": \"Germanic\", \"words\": \"\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"An empty pass-through box: Nourai posits an unnamed Germanic stage between the root and English baby/babe/babble. That is a reasonable placeholder — Pokorny p. 91 lists a Germanic set under bāba- ('engl. baby \\\"Kind\\\", schwed. mdartl. babbe \\\"Kind, kleiner Junge\\\", mhd. bābe, bōbe \\\"Alte, Mutter\\\"') and Klein an even fuller one for the babble family ('ON. babba, Swed. babbla, Norw. bable, LG. babbeln, Du. babbelen, G. babbeln, \\\"to prattle\\\"'). It is only plausible rather than confirmed because no proto-Germanic form can be reconstructed for an echoic word of this kind: the continental and English forms are parallel nursery creations rather than reflexes of one inherited etymon, and Watkins accordingly starts the English words at Middle English, not at Germanic.\",\n  \"derivation_fa\": \"این خانه‌ای است تهی و گذرا: نورایی میان ریشه و واژه‌های انگلیسی baby/babe/babble مرحله‌ای ژرمنیِ بی‌نام گذاشته است. چنین جای‌گیری بی‌پایه نیست — پوکورنی در ص ۹۱ مجموعه‌ای ژرمنی ذیل bāba- می‌آورد («انگلیسی baby، سوئدی گویشی babbe کودک، آلمانی میانه bābe/bōbe پیرزن، مادر») و کلاین فهرست کامل‌تری برای خانوادهٔ babble («ایسلندی کهن babba، سوئدی babbla، هلندی babbelen، آلمانی babbeln»). ولی «قطعی» نیست، زیرا برای واژه‌ای آواگونه از این دست نمی‌توان صورت ژرمنیِ آغازین بازسازی کرد: صورت‌های قاره‌ای و انگلیسی آفرینش‌های موازی کودکانه‌اند نه بازتاب یک ستاک موروثی، و به همین سبب واتکینز آغازِ واژه‌های انگلیسی را «انگلیسی میانه» می‌گیرد نه ژرمنی.\",\n  \"sources\": [E_BARB],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. baba-: the English words are started from Middle English ('1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY'), so the appendix supports the material but not an intermediate Germanic node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 91\", \"stance\": \"supports\", \"note\": \"'engl. baby \\\"Kind\\\", schwed. mdartl. babbe \\\"Kind, kleiner Junge\\\" …, mhd. bābe, bōbe \\\"Alte, Mutter\\\"' — a Germanic group under the root.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p. 106\", \"stance\": \"supports\", \"note\": \"Same group, with 'ahd. Buobo, ags. Bofa Mannsname' added; and under *balbal-: 'nhd. babbeln, päppeln, engl. babble, norw. bable, schwed. babbla, aisl. babba \\\"schwatzen\\\"'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 4221 s.v. babble\", \"stance\": \"supports\", \"note\": \"'whence also ON. babba, Swed. babbla, Norw. bable, LG. babbeln, Du. babbelen, G. babbeln, \\\"to prattle\\\"'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 18, \"lang\": \"English\", \"words\": \"baby, babe, babble\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three are the English members of the family and are correctly placed. babble is Middle English babelen (c. 1200), matching Dutch babbelen, Low German babbeln, Swedish babbla, Old Norse babba, and Latin babulus 'babbler' — Klein files it 'from the I.-E. imitative base *bab-'; babe is ME babe (13th c.), itself a nursery word, and baby is its diminutive in -y (Klein: 'baby, n. — Dimin. of babe'). Watkins/AHD gives exactly this list under baba-: 'Middle English babelen, to babble: BABBLE. Middle English babe, babi, baby: BABE, BABY.' The one caveat, already made at node #17, is that such words are re-created in each generation rather than inherited by sound law — but that is a caveat about the nature of the root, not about the placement of these three words.\",\n  \"derivation_fa\": \"هر سه واژه اعضای انگلیسی همین خانواده‌اند و درست جای گرفته‌اند. «babble» از babelen انگلیسی میانه (حدود ۱۲۰۰ م.) است و با babbelen هلندی، babbeln آلمانیِ پست، babbla سوئدی، babba ایسلندی کهن و babulus لاتین «وراج» هم‌خانواده است؛ کلاین آن را «از ستاک آواگونهٔ هندواروپایی *bab-» می‌داند. «babe» صورت انگلیسی میانه و خود واژه‌ای کودکانه است و «baby» مصغّر آن با پسوند -y. واتکینز/AHD دقیقاً همین فهرست را ذیل baba- می‌آورد. تنها احتیاطی که در گرهٔ ۱۷ گفته شد این است که چنین واژه‌هایی در هر نسل از نو ساخته می‌شوند و از راه قانون‌های آوایی به ارث نمی‌رسند؛ ولی این نکته دربارهٔ سرشت ریشه است نه دربارهٔ جای این سه واژه. ادعای نورایی درست است.\",\n  \"sources\": [E_BARB],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. baba-, senses 1-2: '1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY'; index (l. 1276) 'BABBLE baba- BABE baba- … BABY baba-'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt ll. 4221-4226 (babble, babe, baby)\", \"stance\": \"supports\", \"note\": \"'babble … — ME. babelen, from the I.-E. imitative base *bab-'; 'babe, n. — ME., of imitative origin'; 'baby, n. — Dimin. of babe.'\"},\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 91\", \"stance\": \"supports\", \"note\": \"'engl. baby \\\"Kind\\\"' under bāba-, and 'engl. babble' under the balbal- variant on p. 91-92.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt ll. 1542, 1856 (Bauble, Blab, s.v. Babble)\", \"stance\": \"supports\", \"note\": \"Skeat cross-refers bauble and blab to Babble as an imitative formation ('Prov[incial] uttering of indistinct sounds').\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt l. 14477 s.v. baby\", \"stance\": \"supports\", \"note\": \"'bā'by, n. … [dim. of babe.]'\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 75,\n  \"book_page\": 45,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry]\n}\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-75.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk75.py && python3 -m json.tool data/verification/page-75.json > /dev/null && echo JSON-OK && python3 tools/verify_check.py 75"
}
```


### [2026-09-05T06:01:33.968Z] TOOL RESULT

```
ok 18
JSON-OK
nodes verified: 18/18
node verdicts: {'disputed': 5, 'confirmed': 8, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'not_checked': 10, 'supports': 4, 'partial': 4, 'not_found': 1, 'contradicts': 1}
books consulted: {'partial': 20, 'supports': 24, 'silent': 11, 'contradicts': 11} | by book: {'KLN': 14, 'POK': 7, 'SKT': 6, 'AHD': 4, 'MON': 4, 'LKT': 4, 'WEB': 4, 'WLD': 3, 'BQT': 3, 'SYN': 3, 'ARY': 3, 'FSD': 3, 'PHD': 2, 'HJB': 2, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'AID': 1}
```


## [2026-09-05T06:01:41.677Z] TOOL CALL #46: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg75.png data/verification/sources/refs/ocr/BOOK/75.png && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg75_greeklatin.png data/verification/sources/refs/ocr/BOOK/75_greek_latin_arrow.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -4 && git status --short | head"
}
```


### [2026-09-05T06:01:41.801Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
 M data/verification/sources/web/index.jsonl
?? data/verification/page-75.json
?? data/verification/sources/web/057e68e9bb3bcd09.txt
?? data/verification/sources/web/0af573ddd8850565.txt
?? data/verification/sources/web/4cbbccb28279c822.txt
?? data/verification/sources/web/7eebd4293cc12d9c.txt
?? data/verification/sources/web/a302e613963e0e45.txt
?? data/verification/sources/web/bad8b3940952dbd0.txt
?? data/verification/sources/web/c73ee63573ce953a.txt
?? data/verification/sources/web/ea212d86c574a93e.txt
```


## [2026-09-05T06:02:00.857Z] AGENT

Page 75 (book p. 45, root **Baba, Barbarah, Balbarah**) is verified: `/home/sfmqrb/git/rishe/data/verification/page-75.json`. `verify_check.py 75` → 18/18 nodes, **0 PROBLEM lines**.

**Verdicts** — root: confirmed. Nodes: 8 confirmed, 5 plausible, 5 disputed.

**Disputed**
- #1 Greek `barbitos, barbaros` — *barbaros* is the genuine reflex (Pok. 91, WLD II 107, Klein), but βάρβιτος is not: Wiktionary/Beekes EDG 201 "uncertain, probably from Phrygian"; no lexicon puts the lyre-name under the imitative root.
- #11 Italian `bambino` — word is right (Klein: dim. of *bambo* 'simple'; AHD baba- §3), but Nourai's gloss "originally a wild and savage man… later brave" is the history of Italian *bravo*. Printed page confirms: the book's own error.
- #12 French `bravo` ← bambino — wrong parent; Klein, Buck (SYN l. 29010) and Funk & Wagnalls derive It. *bravo* from L. *barbarus* (*brabarus, *brabus); Etymonline prefers ML *bravus*/L. *pravus*. Belongs under the Latin box (#4).
- #14 English `brave, bravo` — same wrong parent; and Nourai's own "AHD" citation fails: BRAVE/BRAVO appear nowhere in the Watkins appendix index.
- #16 Persian `bâb 3 (بابو)` ← Hindustani — contradicted by his own reference: Mo'in has "بابو [قس. باب] پدر، بابا؛ بزرگ قلندران و درویشان" and "باب [= بابا - بابو]", i.e. a native Persian nursery family, no Indian tag.

**Extraction error for the owner to fix**: node #4 (Latin) has `"parent": 0`, but on the printed page (p. 45) the Latin box hangs off the **Greek** box — its elbow descends from the Greek box's bottom-left exactly like the Pahlavi box's. Parent should be **1**. Nourai's drawing is the correct one (L. *barbarus* ← Gk. βάρβαρος, as Pokorny/WLD/Klein all say). Page images saved to `data/verification/sources/refs/ocr/BOOK/75.png` and `75_greek_latin_arrow.png`.

**Best find on the Iranian branch**: BQT:249 checks out — Mo'in's footnote (continued on p. 250) reads "پهلوی barbut از یونانی …", matched by MacKenzie p. 17 "barbut [blbwt'] lyre" and Wiktionary; Dehkhoda's *bar* 'breast' + *bat* 'duck' is a folk etymology. MON:497 is only partial (Mo'in's Farhang tags بربط "[معر.]").

Ref checks: 4 supports, 4 partial, 1 not_found, 1 contradicts, 10 not_checked (OEW = Shipley lending-only; VOP = Moshiri, no digital copy anywhere). 10 web pages archived via `fetch_source.py`.
