# Verification process log — verify-page-397


## [2026-09-14T00:49:49.396Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 397 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-397.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-397.json. Write /home/sfmqrb/git/rishe/data/verification/page-397.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 397` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:50.385Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T00:49:51.438Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:51.454Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T00:49:51.939Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-397.txt"
}
```


### [2026-09-14T00:49:51.958Z] TOOL RESULT

```
1	=== PDF page 397 (book page 367) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 3 : opposite, against, in front of, strike. Related to the Indo-European root "Per 1".  (refs POK:815-818)  PART 2
4	#1 (parent #0) [Avestan / Old Persian] refs=AEF:336 | paiti-jathra : anti-toxin ☞Gwhen 2 | NOTE: KLN:169 derives the first part from the Indo-European root "Pa:protect" but HUB:36 and MON:648 do not agree with him.
5	  #2 (parent #1) [Persian] refs=AEF:334; MON:648; FVF:50 | pâdzahr «پادزهر (پازهر)» : antitoxin
6	    #3 (parent #2) [Arabic] refs=FVF:50 | bezoar
7	      #4 (parent #3) [English] refs=AHD:1520 | bezoar
8	#5 (parent #0) [Avestan / Old Persian] refs=FSF:107; BQT:374; KNT:194 | paiti-grab, pati-grab : to accept ☞Ghrebh ; paiti-ar, pati-ara : challenge, fight ☞Er 1 ; paity-âra : against progress, enemy, ugly ☞Er 1 ; pati-kara : form against, body ☞Kwer
9	  #6 (parent #5) [Pahlavi] refs=FSF:107; BQT:374; MON | padiraftan : accept ; patirak : to fight, confront ; patyârak : ugly ; patkar : body, bundle
10	    #7 (parent #6) [Persian] refs=BQT; HRN; MON | pazîroftan «پذیرفتن» : accept ; pazîreh «پذیره» : confront ; patyâreh «پتیاره ، پتیره» : ugly ; paykar «پیکر (پیکره)» : image, statue
11	    #8 (parent #6) [Sogdian] refs=SOD:311 | ptkr`k : image
12	#9 (parent #0) [Latin] refs=AHD | premere : to strike or press against ; pressuss : press, pressure
13	  #10 (parent #9) [French] refs=None | 
14	    #11 (parent #10) [Persian] refs=MON |  | extra: پرس ، کمپرس
15	    #12 (parent #10) [English] refs=AHD | press, compress, print, express
16	
```


## [2026-09-14T00:49:55.188Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-397.json",
 "description": "Read page 397 source JSON"
}
```


### [2026-09-14T00:49:55.235Z] TOOL RESULT

```
{
  "pdf_page": 397,
  "book_page": 367,
  "entries": [
    {
      "root": {
        "name": "Per 3",
        "lang": "Indo-European",
        "refs": "POK:815-818",
        "gloss": "opposite, against, in front of, strike. Related to the Indo-European root \"Per 1\"."
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "AEF:336",
          "words": [
            {"translit": "paiti-jathra", "gloss": "anti-toxin", "script": null, "see": ["Gwhen 2"]}
          ],
          "note": "KLN:169 derives the first part from the Indo-European root \"Pa:protect\" but HUB:36 and MON:648 do not agree with him.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AEF:334; MON:648; FVF:50",
          "words": [
            {"translit": "pâdzahr", "gloss": "antitoxin", "script": "پادزهر (پازهر)"}
          ],
          "note": null,
          "quote": {"text": "مبادا که گستاخ باشی به دهر - یکی زهر یابد یکی پای زهر", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVF:50",
          "words": [
            {"translit": "bezoar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:1520",
          "words": [
            {"translit": "bezoar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FSF:107; BQT:374; KNT:194",
          "words": [
            {"translit": "paiti-grab, pati-grab", "gloss": "to accept", "script": null, "see": ["Ghrebh"]},
            {"translit": "paiti-ar, pati-ara", "gloss": "challenge, fight", "script": null, "see": ["Er 1"]},
            {"translit": "paity-âra", "gloss": "against progress, enemy, ugly", "script": null, "see": ["Er 1"]},
            {"translit": "pati-kara", "gloss": "form against, body", "script": null, "see": ["Kwer"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "FSF:107; BQT:374; MON",
          "words": [
            {"translit": "padiraftan", "gloss": "accept", "script": null},
            {"translit": "patirak", "gloss": "to fight, confront", "script": null},
            {"translit": "patyârak", "gloss": "ugly", "script": null},
            {"translit": "patkar", "gloss": "body, bundle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT; HRN; MON",
          "words": [
            {"translit": "pazîroftan", "gloss": "accept", "script": "پذیرفتن"},
            {"translit": "pazîreh", "gloss": "confront", "script": "پذیره"},
            {"translit": "patyâreh", "gloss": "ugly", "script": "پتیاره ، پتیره"},
            {"translit": "paykar", "gloss": "image, statue", "script": "پیکر (پیکره)"}
          ],
          "note": null,
          "quote": {"text": "پذیره شدش دیو را جنگجوی - سپه را چو روی اندر آمد به روی", "poet": "Ferdowsî"}
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Sogdian",
          "refs": "SOD:311",
          "words": [
            {"translit": "ptkr`k", "gloss": "image", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "premere", "gloss": "to strike or press against", "script": null},
            {"translit": "pressuss", "gloss": "press, pressure", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "MON",
          "words": [],
          "script_extra": "پرس ، کمپرس",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "press, compress, print, express", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:49:58.026Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AEF','FVF','FSF','SOD','KNT','BQT','MON','HRN','HUB','AHD','POK','KLN','PHD','NYB','WLD','IEC','SYN','BRT','CHEUNG','ARY','SKT','WEB','FSD','PLA','AFM','LKT','DEV']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T00:49:59.278Z] TOOL RESULT

```
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
```


## [2026-09-14T00:50:36.840Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && ls data/verification/page-39*.json"
}
```


### [2026-09-14T00:50:36.892Z] TOOL RESULT

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
----
data/verification/page-39.json
```


## [2026-09-14T00:50:37.422Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:50:37.469Z] TOOL RESULT

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
```


## [2026-09-14T00:50:40.966Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"per-4\\|per-1\\|per-2\\|per-3\" POK_full.txt | head -40"
}
```


### [2026-09-14T00:50:41.013Z] TOOL RESULT

```
16935:deesse : Portuguese deusa ' goddess '. [see Root / lemma: per-2\ to go over; over]. 
40520:shepherd '? About gr. np£apu(; "old' see below per-3. 
66350:References: WP. II 48, WH. II 288; compare above S. 819 Mitte {per-3, per-g-). 
66465:See also: extension from per-1. 
66569:Root / lemma: per-1, pera- : pre-, preu- 
66577:Root / lemma: per-1, pere- : pre-, preu- : to drizzle, sprinkle, jet, derived from Root / 
66631:Root / lemma: per-2 
66947:Root / lemma: per-2. B. per-, pera- 
67039:Root / lemma: per-2: C. per-, pera- 
67071:Root / lemma: per-2. D. per- 
67075:Note: (as fera 'gebare' in einstiger reiationsliip to per-2: C "allot') 
67102:Root / lemma: per-2. E. per- 
67128:Root / lemma: per-3, per-g- 
67196:Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 
69138:See also: s. per-2S. 813 f. 
79685:Root / lemma: sper-2(g-) 
79718:Root / lemma: sper-3 
80182:Note: probably with sp(h)er-V twitch ' identical, also with per-1, above S. 809 f.
```


## [2026-09-14T00:50:41.772Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"proti\\|prети\\|preti\" POK_full.txt | head -30"
}
```


### [2026-09-14T00:50:41.825Z] TOOL RESULT

```
24895:(from *fra-iPya-, *pro-itios^\he the gone away, the departed ', compare Old Indie preti-\. " 
63553:eyes and mouth)' ( *proti, *eni+ ok"-\ compare Slavic nicb under *ni- 'low, mean'), ghrtacTt 
66919:h. preti, proZ/'compared with, entgegen, against', partly in sense of remuneration; preti- 
66926:Lesbian npoq (compare TTp6a(a)aj 'vorwarts' from *protid, np6a9£(v) 'from vorn'), 
66929:hin; by (in SchwiJren)', 'from - her, from'; Latin pretium ' value, worth, price of a thing' 
66930:(Neutr. eines Adj. *pretios), compare Old Indie /JAa/z-as-'gleichkommen', aprata {siem 
66935:Church Slavic protiVb, protivg "entgegen', Kashubian procinr, wruss. preci, poln. przeciw 
68746:Note: through das Adv.-forms -//(compare *proti- : *pro above S. 815 f.) from *po (see 
80256:sprout, spray'; Old Icelandic sprotixx\. 'young sprout in a tree, Stecken', Old High German 
91805:together with dem relationship from Old Indie /0/'a//"gegen': Latin pretium^as Gegenwert
```


## [2026-09-14T00:50:45.246Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66890,66950p' POK_full.txt"
}
```


### [2026-09-14T00:50:45.293Z] TOOL RESULT

```
Old Church Slavic p/io/rb" residual, remaining', proceMv. "Aoinov, igitur' {*prokJom)\ 

auf ein *prd-ko- Qoes back bret. a-Aao/r'vorwarts, voran, prior ', cymr. (y)rhawg^au\ 
lange', with ProklisenkiJrzung: bret. rak, corn, rag, cymr. A^a^ 'before'. 

pro-uo-. in Old Indie /0/'ai/5/7a-"(vorwarts) willing, inclined, abschijssig', n. "slope, heap, 
mound '; about Latin pronussee above; gr. npavrjc;, hom. npnvnq "vorwarts willing, 
inclined' after Leumann Homer. Worter 77 f. from *TTpo-avr|^ 'face ahead'; with other 
meaning Old High German fro, Old Saxon frao. Old English frea^ master, mister' {*frawan- 
), Gothic frauja^masier, mister' (Old Icelandic FreyrQH to o-stem has changed). Old 
Saxon frd/o6s.. Old Icelandic /^ej^5 'mistress; name the goddess'. Old High German 
frouwa'\N\ie, woman'; besides Old Saxon frua. Middle Low German fruwe^\N\ie, woman' 
from *frdwdn, Indo Germanic *prd-uo-, das also in Attic irpcopa (Latin loanword prora) 
'Schiffsvorderteil' (npwFaipa-, -apja Indo Germanic *prdu-ria); perhaps Latin provincia, if 
auf a *prduidn ^rwasiex, mister, power, rule' being based on; Old Bulgarian pravt 'right, 
right' ('*gradaus'); 

with the same forms, but as Lithuanian p/'r-masl\rst' from "pe/'a- 'shaped', Indo 
Germanic pera-£/o- in: Old \nd'\c purva-, Avestan paurva-, pourva-, ap. paruva-^ihe 
vordere, fruhere' (Old Indie purvya-, Avestan paouruya- paoirya-, ap. /OamK/Ka 'prior', then 
'primus'), alb. yoare 'first', para^yof; Old Church Slavic yO/Tji/byO/ibi/b 'the first'; probably 
also die base from Old English forwost, forwest^ihe first'. 

Note: 

Phonetically alb pare^ first ' : Tocharian A y05/wa/ 'first' (with -/after the other ordinal 
numbers) and Tocharian B parwe (^ parwe) 'earlier, first' 

h. preti, proZ/'compared with, entgegen, against', partly in sense of remuneration; preti- 
os^ equal in '. 



Old \n6\c prat/ {\n Iran, through yOa/Z/verdrangt) prefix 'against, back etc' preposition 
'against' etc.; gr. hom. irpoTi (Cretan nopri reconverted with metathesis), Ionian Attic 
Lesbian npoq (compare TTp6a(a)aj 'vorwarts' from *protid, np6a9£(v) 'from vorn'), 
pamphyl. rrepTi (reconverted with metathesis from *np£Ti), Aeolic npsq. Adv. 'yet in 
addition, moreover', prefix, preposition 'against - toward, to, against', 'an', 'after a Bereich 
hin; by (in SchwiJren)', 'from - her, from'; Latin pretium ' value, worth, price of a thing' 
(Neutr. eines Adj. *pretios), compare Old Indie /JAa/z-as-'gleichkommen', aprata {siem 
*pratay-) ' without Entgelt, free', Avestan paraska {*prt-ska) 'price or value, worth ', Old 



Church Slavic protiVb, protivg "entgegen', Kashubian procinr, wruss. preci, poln. przeciw 
"against' (also in sense of exchange relation); Latvian preteic. 

i. pors6(d}. Armenian a/'by, an, besides', verbal prefix and preposition; in addition araj 
"Vorderseite, beginning ', arajin 'first'; gr. noppu), nopau) (Pind.) 'vorwarts' = Latin porro 
"vorwarts, fiJrder'; through ihren o-vocalism auffallige formation. 

References: WP. II 29 ff., EM.2 754 f., 801 , 808 ff., 811 f., WH. II 283 ff., 351 , 364 ff., 
Trautmann 214 f., 220, 229 f., 230 ff., Schwyzer Gr. Gr. 2, 491 ff., 499 ff., 505 ff., 508 ff., 
541 f.,543ff.,654ff. 
Page(s): 810-816 

Root / lemma: per-2. B. per-, pera- 

Meaning: to carry over, bring; to go over, travel
```


## [2026-09-14T00:50:45.848Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67128,67200p' POK_full.txt"
}
```


### [2026-09-14T00:50:45.896Z] TOOL RESULT

```
Root / lemma: per-3, per-g- 

Meaning: to hit 

Material: Aryan only with /-formants: Old Indie prt-, prtana l\g\r\t, struggle, fight', Avestan 

peret-, pasa/7a 'fight, struggle, battle', paratamna^6\e miteinander Kampfenden', paiti- 

paratata ^bekampit'] 

Armenian har/'\ schlug' (Aor. to present harkanem, see below), harac^yu\v\us'\ orot 
"thunder', c»/'c»/5/77'donnere'; 

alb. yO/ies'haue ab, low, base; cut, bite', Aor. preva, me pret^es kijmmert myself, is mir 
angelegen', pr/tem'\Ner6e geschnitten; scratch myself; kijmmere myself um etwas'; 

Latin premo, -ere, pressi, pressum "push, press', prelum 'Presse, Kelter' ( *pres-lom); 
root pr-em- {\N\Vr\ durativem -em-) and pr-es- as gr. rpsfju) 'tremble: rpeu)' {*tresd) ds.; 

Lithuanian per/u, pe/Y/'with dem Badequast hit, jemanden bathe; hit', Latvian peru, pert 
ds.; Lithuanian yO//Y/5, Latvian yO/r/s'Badestube'; 

Old Church Slavic perg, pbrat/'\r\\t, esp. with dem Blauel hit, wash', Serbo-Croatian 
perem, prat/^\NasW; ablaut. Old Church S\a\/'\c ptrjg, *pbret/" contendere' , sg-pbrja, sb- 
porb fight', Czech pru, pr/t/ se ' quarreV and Old Church Slavic *pbrg, *pert/"\n russ. pru, 
pratb, peretb 'press, urge, press, push', naporb ' shove ' etc.. Old Russian pbrtb 
'Badestube'; 

pe/g'-; Armenian harkanem {prg-) 'hit, zerhaue (wood), falle (tree), slay, fight '; Old Irish 
orcaid. Middle Irish o/zy^/ic/'erschlagt, slays, verwiJstet'; Middle Irish cymr. 0/77'Morden, 
Zersioren' { *fPprg-no- od. -na)\ abret. treorgam 'perforo', org/at 'caesar' (= caesor), gall, 
o/ye 'occide', PN Orgeto-rTx, different about Celtic org-s. Lewis-Pedersen 387 (to Hittite 
harganu-' destroy'; compare das Old Irish verbal noun orcunirom *orgena)\ perhaps here 
Old Indie Parjanya- rain- and Gewittergott; see be\o\N perk"u-s. 

References: WP. II 42 f., WH. II 288, Trautmann 215; 
See also: further to perg-1. 



Page(s): 818-819 



Root / lemma: persna, -snT-, -sno- 

Meaning: heel 

Material: Old Indie parsni-i., Avestan pasna-u. "calcaneus '; gr. nTspvri f.; Latin pernai. 

{*persna) "Hinterkeule, Schweineschinken, thigh, leg', /Oe/77/s 'quick, fast' (with the 

calcaneus); Gothic fafrsna. Old Saxon fersna. Old High German /fe/'sa/75 "calcaneus ' 

{* persna). Old English fiersini. ds. {*persni-)\ Hittite pars/na{\eg. parsna) "thigh, hip ', pars- 

(a)nai-^ crouch ' (auf den Oberschenkein). 

References: WP. II 50 f., WH. II 289 f., Pedersen Hittite 258. 

Page(s): 823 

Root / lemma: pers- 

Meaning: to drizzle, sprinkle; dust, ashes 

Note: 

Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 

pera-. pre- preu-: to drizzle, sprinkle, jet < Root/ lemma: *(s)p(h)ereg- (s)p(h)erag-, 

(s)p(h)reg- {nasaXxzedi spreng^ : to rush, hurry; to scatter, sprinkle.
```


## [2026-09-14T00:51:01.050Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD per ===\"; grep -n \"^per-\\|per-4\\|per-3\\|to strike\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T00:51:01.103Z] TOOL RESULT

```
<persisted-output>
Output too large (49.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/beyyzfnbi.txt

Preview (first 2KB):
=== AHD per ===
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source
...
</persisted-output>
```


## [2026-09-14T00:51:02.609Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT jaθra ===\"; grep -n -i \"ja0ra\\|jaθra\\|jathra\\|jaGra\" BRT.txt | head -20; echo \"=== BRT paiti-jan ===\"; grep -n -i \"paiti\\.jan\\|paitijan\\|paiti-jan\" BRT.txt | head -20"
}
```


### [2026-09-14T00:51:02.673Z] TOOL RESULT

```
=== BRT jaθra ===
=== BRT paiti-jan ===
9981:nSmSni  aeSam  drujinqm  .  .  paiti.janaiti*'' Yt.4. 7.  3)  Med.  a)  II  'sich  wehren gegen  --,  bekämpfen',  mit  Akk.:  pärst^ martiy^  ^duraiyapiy  kacä  pitrsil^  hama- ram  (sd.)  patiyajatä  (3SPrM.)"  D.  ti. 4.  b)  'sich  wehren  um  — ,  kämpfen um  — ',  mit  kala  und  Abt.:  ya'ia  nä taxmö  . .  kus.kqm.bfr?tal  kam  laität  (sd.) . .  paiti.ynita  (3SOM.)  Yt.  13. 67.
```


## [2026-09-14T00:51:09.845Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in HRN.txt HUB.txt; do echo \"=== $f ===\"; grep -n -i \"zahr\\|pâdzahr\\|padzahr\\|bezoar\" $f | head -20; done"
}
```


### [2026-09-14T00:51:10.876Z] TOOL RESULT

```
=== HRN.txt ===
2714:273. päzehr 'Gegengift, Bezoar.
5776:halb* ; bei. zahr mächtig (293).
5982:phlv. zahr 'Gift* (Men.), arm. LW. zahr,
5983:kurd. zahr, zäir, zur 'Gift' ; af/. bei. (297) LW. zahr,
5985:phlv. "^zahrak und identisch mit zehr 'Gift* nach
20913:zahr 678.
=== HUB.txt ===
1194:273. Die altere Form pddzahr siehe bei Vullers s. v.
1195:pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
1196:*Gegengift' Shk. 261. Auf dieses padzahr (das aber
1210:pddzahr *6egengift'; np. padas 'Vergeltung' = phi. pa^-
2485:in deraselben Dialect auch zu zahr, zahra werden
2490:zahr 'Gift' = kurd. mhr, iar (ZDM6. 38, 72, 107), zah'r
2492:(wie ohne Weiteres fiir zahr gelesen werden kann) auf
2494:leite zahra *6alle* (bal. LW. zahrak *Gallenblase') mittelst
2496:natiirlichste ist, wahrend NOldeke dem Worte zahr^
2499:um zahr = zahra auf ap. "^zartor- = "^zartaka- gelb'
2500:zuriickfiihren zu k5nnen. Eine Neubildung ist zahra
4656:ap. *hazahra-, zd. hazafira^, skr. sahasra^\ BaArflm = phi.
4668:*Gegenantwort' Nebenform zu paiti- ist): np. pazahr =
4669:podzahr (bei Vullers und Polak, Persien II, 275) *Gegen-
5264:'Nacken', garm Varm', gustardan *ausbreiten', mar *Zahr,
6107:sufnCLr *Zahr, Sumurdan 'zahlen', phi. mmurtan, ap. -smar^
6846:^patsaxv (s. § 10) ; pozahr neben padzahr = paz. podazahar
6847:(d. i. padzahr) 'Gegengift' (s. § 10 und oben p. 36); pOdds
6934:Parsenwortern vor und somit ist np. zahra 'Galle = phi.
6935:zahrak ZPGl. 10, 2 v. u. nicht auf ap. zartaka- zurttckzu-
```


## [2026-09-14T00:51:11.031Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN bezoar ===\"; grep -n -i \"bezoar\" KLN_1966.txt KLN_1971.txt SKT.txt LKT.txt DEV.txt DOZ.txt | head -30"
}
```


### [2026-09-14T00:51:11.105Z] TOOL RESULT

```
=== KLN bezoar ===
DOZ.txt:919:dat Kichardson expeller of poison vertaalt. De bezoar
DEV.txt:837:Bezoard.  Esp.  bezonr,  bezaar,  bezar;  portug.  bezoar.  De l'arabe  y^)^!^  bâdizahr  ou  yû^U  bâzahr,  venant  du  persan y^Vib  pâd-zehr,  qui  signifie  littéralement  chasse -poison.  Be- zoar a  été  employé  chez  nos  anciens  auteurs,  non-seule- ment dans  son  sens  propre  :  r^  Lapidem  bezaar  magnae  vir- tutis  et  pretii^w,  inais  encore  dans  le  sens  général  do contre-poison,  ainsi  qu'on  le  voit  dans  ces  passages  d'Am- broise  Paré  cités  par  M.  Littré  :  ç^  Son  bezahar  ou  contre- poison est  le  suc  de  mélisse. . .  D'autant  qu'en  parlant  des signes  de  chacun  venin  à  part,  nous  avons  nommé  son antidote  bezahar,  il  faut  savoir  ce  que  veut  dire  ce  mot  : les  antidotes  ou  contre-poisons  ont  esté  appelés  par  les Arabes  en  leur  langue  bezahar,  c'est-a-dire  en  leur  ba- ragouin, conservateur  de  la  vie;  de  là  est  venu  que tous  antidotes  et  contre-poisons  par  excellence  ont  été  ap- pelles bezarfhca.  )•>
DEV.txt:840:Le  mot  s'est  introduit  dans  nos  langues  par  les  livres de  médecine  arabes  :  crLapidem  bezoarticum,  de  cujus efficacissima  vi  adversus  venena  Arabes  prœsertim,  vete- res  eliam  et  juniores  medici  tam  multa  retulerunt  admi- randa,^  dit  Gaspare  de  los  Reyes\  qui  cite  en  même temps  un  grand  nombre  d'écrivains  arabes,  tels  que  ç^Rha- zis,  Abenzoar.  Mesue,  Haly  Abbas,  Avicennew,  etc.  parmi ceux  qui  ont  traité  ce  sujet.
DEV.txt:841:'Lui-même  y  a  consacré  vingt  pages  in- A".  J'en  tire  les lignes  suivantes  à  cause  de  la  suggestion  étymologique qui  parait  s'y  trouver  :  ^(Lapides  bezoartici)  qui  frequen- tiores  et  communiores  sunt,  in  ventriculis  animalium  quo- rumdam  Indorum  generantur,  quœ  caprae  magnitudinem superant  et  ad  cervorum  figuram  proxime  accedunt,  unde cervicapra}  communiter  appellantur,  et  a  Persis  Pazan  vo- cantur,  et  ipsum  lapidem  Pazaar,  quod  antidotum  sonat, aut  veneni  remedium  ''^.  ?'  Inutile  de  dire  que  Pazaar,  c'est- à-dire  Padzehr,  et  Pazan  n'ont  entre  eux  aucun  rapport. Ce  dernier  nom  a  passé  dans  la  nomenclature  zoologique française  :  paseng,  chèvre  égagre,  et  pazan,  nom  donné mal  à  propos  par  BufFon  à  l'antilope  oryx.  Dans  Meninski, ij'^li  ou  (j^b  hazen,  pazen  est  simplement  :  ctcornutus,  qui mœcham  babetw;  mais  Richardson  traduit  avec  raison par  c^goat  of  mountain??,  chèvre  de  montagne.  Il  y  a  plus de  trois  cents  ans  qu'Ambroise  Paré  avait  fait  mention  de  ce ruminant  :  <t  Une  espèce  de  bouc  appelé  en  langue  persicque pazainv,  dans  un  passage  dont  celui  de  Gaspare  de  los Reyes  semble  une  traduction.
DEV.txt:3060:Bezoar,  hisp.  voy.  Bézoard.
LKT.txt:3674:160.5.  Pers.  pädzähr: 'Gegengift,  Bezoar'  [päzähr  Horn  NpEt
LKT.txt:3677:S.  62,  Nr.  273  oder  'Gift  antreibend'  aus päd,  s.  hier  Nr.  1604,  und  zähr  'Gift', ebenda  S.  150,  Nr.  678];  man  versteht darunter  hauptsächlich  gewisse  harte Abscheidungen  aus  tierischen  Körpern, denen  die  Wiriiung  von  Gegengiften  zu- geschrieben wird,  insbesondere  aus  dem Magen  einer  Wildziege  in  der  pers.  Pro- vinz Lar.  Hieraus  ar.  bädizahr,  bäzahr und  nach  magribinischer  Aussprache  mit Imäla  [a  >  e]  bezahr,  woraus  die  Ärzte des  MA.  die  ihre  Kunst  den  Westarabern verdankten,  mlat.  bezoar  machten:  sp. bezaar,  sj).  pg.  kat.  bezoar,  frz.  bezoar, it.  bezzoar,  bezzoarre,  belzuar;  engl,  be- zonr,  ndl.  bezoar  'Ziegenstein  im  Magen der  Wiederkäuer',  dtsch.£f2;oar'Gemsen- kugel'.  Im  Russ.  wurde  bezar,  bezuj sowie  daraus  abgeleitet  zaberzat  Bezeich- nung eines  Edelsteins  [vgl.  Zapiski  der Oriental.  Sektion  der  Kais.  Russ.  Ar- chäol.  Ges.  XIV.  1.  Lieferung:  K.  Ino- strantzew,  Über  zwei  allrussische  Be- zeichnungen für  Edelstein].  [DE  239/240. Dozy  Oost  25/26.  Eguilaz  345.  Devic DEt  68/69.    Hobson-Jobson  40/41.
LKT.txt:5765:besehein  j.  2210 Beteigetize  St.  695 Betel  2149 betucht  j.  267 Betuchter  j.  267 Betuecliter  j.  267 Bezoar  1605 Bisam  293 ii/Mse  1647 Boback  181 ß��c/i^r  j.  180 Bombasin  16 17 Bonze  331 Borax  356 Boretsch  13 Borretsch  13 £os  j.  184  a Bronze  1657 Burnus  365 Burrich  13 5?<sa  376 Buxkin  324
LKT.txt:7425:halascius  151 balsatnum  293 bambagium  1617 Barabbas  220 ftarca  2148 harracanus  250 basilica  (vena)  262 bezoar  1605 birrus  365 bisamutn  293 bombacium  1617 borrago  13 bronzium  1657 brundisinum  Caes)  1657 brunitius  1657 buccina  347 burgns  362 burrus  365
LKT.txt:7492:bezoar  1605
LKT.txt:8067:bezoar  1605
LKT.txt:10056:bezoar  1605
SKT.txt:1743:cIo<e.  A.S.  bt',  preBx  (see  Be-);  and ■O'rri^n,  to  accuse.  Cf.  Icel.  mr^a  (for ITJ;^7<>).  to  Klaoder.  Swed,  riya^  to  discover; O.  Iries.  iiwrogiat  to  accuse;  Golh. u/rifA- JtiH,  to  accase ;  G.  rv^a,  to  censure.  B. These  are  ciusal  verl«,  from  the  $b,  seen  in Goth,  wrchs,  accusation,  led.  rJ^, a  slander. Boy,  a  governor.  (Turk.)  Turk,  big  (i>ron. nearly  as  bay),  a  lord,  prince. Beyond.  (E-)  Sec  Yon. Besel,  the  part  of  a  ring  in  which  the stone  is  set.  (?.)  Also  spell  basil:  it  also means  a  sloping  edge.  — O.  F.  t>iiri.  mod.  F. bUeaH,  a  bezel,  basil,  slant,  sloped  edpe. Cf.  Span,  bixel,  the  slanting  edge  of  a  look- ing-glass; Low  L.  bisaiur,  'lapis  cni  duo sunt  anguli ; '  Ducange.  (Perhaps  from  L. bis,  double ;  and  a/a,  a  wing?) Beaomr,  a  stone.  (F.  -  i*ort.  -  Pers.) O.  F.  bitaar,  F.  b^xaard.  —  Port,  besaar (Brachct).  —  Per*.  fnid-%ahr^  bezoar;  lit *  poisoD-expcHcr.*  from  its  supposcfi  virtue, —  Per^./zi*/,  expelling;  and  «Mr,  poison. Bi-,  prefix.  (L.)  In  bi-as,  the  prefix  is F.,  but  of  L,  origin.  — L.  bi-,  put  for  dui'^ twice.  — I...  duo,  two.  So  also  Gk.  2i-,  Skt dvi.    See  Two.
KLN_1966.txt:4878:bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon
KLN_1966.txt:4880:Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘counterpoison,  bezoar  stone’, lit.  ‘protecting  (against)  poison’,  fr.  pad,  ‘pro¬ tecting,  guarding;  guardian,  lord,  master’,  and zahr,  ‘poison’.  For  the  first  element  see  padi- shah.  The  second  element  is  rel.  to  Pers.  zehre, ‘gall,  bile’,  Pahlavi  zahr,  ‘poison’,  Avestic  zara-, ‘gall,  bile’,  and  cogn.  with  Gk.  yoXf],  ‘gall,  bile’. See  choler.
KLN_1966.txt:7507:choledocho-,  combining  form  meaning  ‘contain¬ ing  bile’.  —  See  prec.  word, choler,  n.  —  ME.  coler,  colere,  fr.  OF.  colere  (F. colire),  ‘choler,  anger',  fr.  L.  cholera,  fr.  Gk. yoXepa,  'bilious  diarrhea,  cholera’,  fr.  yolrh  also y6Xo c,  ‘gall,  bile’,  which  is  rel.  to  y'k'joc,  ‘greenish- yellow  color’,  yko^eiv,  ‘to  be  green’,  yluicib', ‘greenish-yellow,  pale  green,  green,  fresh’,  and cogn.  with  Avestic  zara-,  ‘gall,  bile’,  L.  fel, OSlav.  zluci,  Russ,  zelc.’,  Lith.  tulzis  (metathesis for  *zultis ),  Lett,  zults,  OE.  gealla,  galla,  ‘gall, bile’,  fr.  I.-E.  base  *ghel-,  *ghel-,  ‘to  shine;  yel¬ low,  yellowish  green,  green’.  See  yellow  and  cp. gall,  ‘bile’.  Cp.  also  next  word,  Chloe,  Chlorella, chlorine,  Chloris,  and  the  second  element  in melancholy,  Chrysochloris,  Echinochloa.  Cp.  also the  second  element  in  bezoar. cholera,  n.  —  L.  cholera,  fr.  Gk.  xoXepa,  ‘bilious diarrhea’,  fr.  yoTcq,  ‘gall,  bile'.  See  prec.  word, choleraic,  adj.,  related  to,  or  resembling,  cholera. —  Formed  from  prec.  word  with  suff.  -ic. choleric,  adj.  —  MF.  (=  F.)  choleriqtie,  fr.  L. cholericus,  fr.  Gk.  yokepixo^,  fr.  ydkipdi,  (see choler  and  -ic) :  first  used  by  Chaucer. Derivatives:  choieric-ly,  adv.,  choieric-ness,  n. cholesterine,  n.,  cholesterol.  —  See  next  word and  chem.  suff.  -ine.
KLN_1966.txt:26912:padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referred  to.  Cp.  also  the  first  ele¬ ment  in  bezoar.  For  the  second  element  see  shah. Cp.  pashah.
KLN_1971.txt:29055:bezoar, n., orig. a term for antidote ; later used 
KLN_1971.txt:29058:antidotal properties. — F. bezoard, fr. Sp. be- 
KLN_1971.txt:29062:badzahr, padzahr, ‘counterpoison, bezoar stone*, 
KLN_1971.txt:45889:the second element in bezoar. 
KLN_1971.txt:171031:ment in bezoar. For the second element see shah.
```


## [2026-09-14T00:51:29.054Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 1185-1215 ===\"; sed -n '1185,1215p' HUB.txt; echo \"=== HUB 4660-4675 ===\"; sed -n '4660,4675p' HUB.txt; echo \"=== HRN 2705,2725 ===\"; sed -n '2705,2725p' HRN.txt"
}
```


### [2026-09-14T00:51:29.111Z] TOOL RESULT

```
=== HUB 1185-1215 ===
(bei Vullers auch bargm^ was falsch ist) erwahnt
werden, das nach arab. fari^n, arm. parken *Wall-
graben* (Agathang. und Levond p. 60, 7) auf phi.
*parkEn zuriickgeht.
271. Np. para *Bruchstiick, Stiick' gehSrt weder zu skr.
para^ *das Letzte, Ausserste, Ende* noch zu zd. para-
'Schuld' (ZPGl.). Horn stellt es jetzt zu lat. j>ar« =
*^«- KZ. 33, 443.
3*— 36 —
273. Die altere Form pddzahr siehe bei Vullers s. v.
pazahr, Polak, Persien II, 375, paz. 'pad{a)zah(a)r
*Gegengift' Shk. 261. Auf dieses padzahr (das aber
*6egen-gift' bedeutet) sowie auf padsdh *Konig' stiitzen
die pers. Lex. falscblich ihr pad 'Schiitzer (s. Nr. 265).
274. Zu pas *Wache, Nachtwache' vgl. Nr. 341: pahra^
Skr. pdtra- (Rgv. 1, 121, 1 nach Say. = pdtar 'Be-
schiitzer !) bleibt besser weg.
274 bis jfp pasaoct im Uiiterschied von paz. phi. pasaxt
Shk. 262 - 263, Gl. and Ind. 103 etc. miisste aus ^patsaxf
entstanden sein, wie pasCtxt aus patsCixt,
275. Neben dem gewohnlichen phi. pasaxv (61. and Ind.
p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
haufig) ein phi. *pasaxv anzusetzen, jenes aus *patsaxv,
dieses aus *patsaQcv (vgl. Sirm, patasxani 'Antwort').
Dieses pdt (aus ap. *pCitiy) liegt noch vor in np. paz.
pddzahr *6egengift'; np. padas 'Vergeltung' = phi. pa^-
ddhisn ; np. bddafrah, lies padafrah Tergeltung, Strafe',
paz. padafrah, phi. patafrds; phi. patrazm Yatk. i.
Zar. 66, Anm. 61 = arm. paterazm *Krieg, Kampf,
Schlacht' (vgl. np. razm *Kampf ') , entsprechend im
Avesta paiti in paitivaka- = *Gegen-rede, Erwiederung
=== HUB 4660-4675 ===
Fiir a&r = ahr ist schon in alter Zeit unregelmassig
ir eingetreten in ArdaSfr, arm. Artasir (sassanid.), phi.
Artaxslr^ alter arm. ArtaSSs, alter phi. ArtaxSa^r etc., siehe
§ 96, b.
§ 10. Ap. a ist nur scheinbar zu mp. np. a geworden,
in Wahrheit war a schon im Altpersischen vorhanden in:
a) den Kompositis mit pa-, pad-, phi. pat- = ap.
*pati', Nebenform zu pati- (wie zd. paiti- in paitivoJca-
*Gegenantwort' Nebenform zu paiti- ist): np. pazahr =
podzahr (bei Vullers und Polak, Persien II, 275) *Gegen-
gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
phi. pasaxv (Pandnama p. 99), gew6hnlich geschrieben pasaxv,
arm. patasxani *Antwort', ap. *pati8a(h)uvan- ; np. pasaxt
*bereit' aus "^patsaxt?, aber paz. phi. nur pasaxta, pasaxtak;
np. padsdh {padsa M u waf f aq p. 4, Z. 6 u. s.w.) 'Konig = phi.
pataxsa oder patax$(a)h; np. (parsisch) padas, pOdOsn
=== HRN 2705,2725 ===
schreiben), Metrum: Xeflfi
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün— 62 ~
271. päre ^ück, Teil'.
ai. pärd- *das Letzte' ; (^w, para- SchulaX?) ^) ; phlv.
pärak 'Stück; Geschenk (behufs Bestechung)', AV.
272. päzen *Bergziege*, päzen,
phlv. pacm (Bund.) ; bei. pädin, n. päsin 'Ziegenbock,
männliche wilde Ziege* (290).
273. päzehr 'Gegengift, Bezoar.
paiti + zehr (s. zehr No. 678).
274. päs 'Schutz*, pasban^ päsTden,
aw. pädra- 'Schutz'; phlv. pas (Bund.), pOspäti, vd.
13 (77); ai. pätra-.
274*»^* päsäyt 'bereit'.
paiti + sagten (s. No. 688) ; phlv. pasa/tan^ pasaxtak
(AV.).
phlv. palsäytan könnte auf die Praeposition pa (tipa)
deuten, doch vergl. phlv. j^^^^X (No. 275).
275. päsu% 'Antwort'.
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
```


## [2026-09-14T00:51:30.300Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT patikara ===\"; grep -n -i \"patikara\\|patiy\\b\" KNT.txt | head -20; echo \"=== SOD ptkr ===\"; grep -n \"ptkr\" SOD.txt | head -20"
}
```


### [2026-09-14T00:51:30.363Z] TOOL RESULT

```
=== KNT patikara ===
1197:pli ghu- in ОР patiy-azbayam Ч proclaimed’, Av. root zba-, Skt. pres. hudyatt.
1579:The ethnic Pátisuvaris (to patiy ?).
1638:$133. Encursis is a frequent phenomenon in OP. The enclities are the following: Pronouns: Ist sg. асе. -md, gen. -maty, abl. -ma. 2d sg. gen. -taiy. За sg. acc. -йт, gen. -Saiy, abl. -$a; pl. acc. -&$, gen. -Sàm. acc. -dum; pl. acc. -di$. pl. aec. -àà (dubious; only in avabasa-lé DB 4.72), Coordinating conjunctions: -eà ‘and’, -vë ‘or’. Postpositions: d, patiy; both also as separate words before or after their nouns. Adverbs and particles: -am, -kavy, -ciy, -dty, never separately. -apiy, -paliy both also separately. Miscellaneous: уа in mátya DB 4.43, 48, 71; yadatya XPh 35f (miswritten yadàya XPh 39), cf. yada : tya XPh 29. müm, elsewhere orthotone, in mātyamäm DB 1.52. rádiy in avahya-radiy DB 1.6f, etc.; also separ- ately. Double enclisis: mé-tya-mém DB 1.52; rauca- pati-vd,, DB .1:207 aatpati-mé DNb 20; avā-
1654:nai-mà, nai-maty, nai-$im, nat-pati-mà, pali-maty, iyat-Saty, imat-vd, yadi-patiy, yadi-và, [us}i-ca; similarly in phrasal compounds, pati-padem, ni-padiy. By analogy, naty-di§ DB 4.73, 78.
1678:Prep. patiy, but pati-padam; party, but pari- barümiy; prefix ni- (not found separately in OP) in ni-padiy, ni-rasdtiy.
1685:ПІ. Final - before initial 4- keeps the writing ay’; the script does not show whether the -i is consonantized before the vowel, since it has no machinery for the distinction; but pati- never becomes *pa&iy- (= pašy-) in compounds, though -ty- becomes OP -8(i)y-: patiy-dvahyaiy, patiy- Giga", palty-ajald; pariy-ait(1y), niy-apatsam, viy- alarayam. |
2269:Ending in -ї: apiy (also enclitic), uparty, -diy, patiy (also enclitic).
2396:pIE *ei-ti ‘he goes’, OP ату, Skt. éti; *i-te ‘go ye’, OP -itä in ратайа, Skt. itá; *7-dhi ‘go thou’, OP -idiy in paridiy, Skt. iht; imf. *é&-m ‘I went’, OP -dyam (for -am, 407.1) in nij-äyam [up]- üyam, Skt. dyam; imf. 3d sg. ОР а (on -S, $228.IIT) and atiy-ãiš; imf. 3d pl. with the- matic vowel from Ist sg., OP -йуа” in apariy- йуа”, -ài$a" (on -&а", 4282.1) in patiy-disa’, mid, dyad from *4-dya7ta.
2404:„ рту. *g*hn-dhi, OP jadiy, Skt. jaht; so alko 2d pi, imv. *o*hn-le, OP jata, and 3d sg. imf. mid. *egthn-lo, OP patiy-ajalà| imf. *eg*hen-m, OP ajanam, Skt. áhanam (with antevocalic de- velopment of m, $07.11), whence with the- matic vowel 3d рі. OP -ajana" in avajana* and perhaps the restored subjunctive 3d pl. i-Janá"tty.
2469:pAr. *kSaja- m Skt. kgáyati ‘he possesses’, OP imf. patiy-arsayaty ‘I ruled over’, ріс. zsayamna ‘ruling’; unless this is rather pIE *g52-e- ($214) to *gbé- seen in Gk. xéxrquae Ч possess’.
2520:OP avah-ya- in imf. patiy-avahyaiy ‘I appealed for help’, to stem in Av. avah- ‘help’.
2584:III. The sigmatic aorist similarly remodeled its 3d pl. from -sat (< -s-nt) to -san(t); thus in ОК, s-aorist €\vo-av ‘they loosed’, whence strong aorist &o-cay ‘they gave’, and (late Greek) thematic éhaBo-cav ‘they took’. So also in OP, the -san j spread to some verhs,! being regularly -ha^ after a _ and -ša” after 1: abaraha^ alongside abara”, patiy- dia", opt. pass. yadiyaisa*, and with extension of — -ša” to the position after a, adurujtyasa", akuna- vasa” alongside akunava*.
2590:rat, (thematic) феру déperat. In OP we have pres. naniyaiy (= Skt. mdnye), patiy-avahyaty, and valrtaiyary (for -tayaty, §48; = Skt. varlaye). The same -at 15 found as primary ending of non-the- matic stems in Avestan and Indic, but there are no OP examples.
2591:III. This -at was used in Aryan also as second- ary ending in thematic imperfects, as in Skt. dmanye, OP amaniyary; OP ayadaw, apayaty, ham-adárayavy, ham-ataxsary, patiy-axrSayaiy.
2599:II. The secondary ending was pIE -io, as in Gk. ёферєто, Skt. dbharata; this is seen in OP ud- араай (Gk. &érero, Skt. épatata), anayatà (Skt. dnayaia), amariyata, früámáyalà, agarbüyatà, agau- bata, ham-ataxsatd, dyasatd, |a|h[yat]à, adalrayat|a, [ат]аоаій, passive akunavayatd, perhaps aor. (h)amarmalà and perf. pass. cazr[zyala] or [claxr|iyata]; non-thematie remade to thematic, avarnavaté and aisiata; non-thematic aor. akula (Skt. dkria) and imf. patiy-ajatd (Skt. dhata).
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
2694:E. Expressing time within which: DB 4.4f Һатаћуду Sarda in one and the same year’; from this use came the use of the genitive харо, DB 1.20, in a riming pair with acc. rauca and enclitic patiy, to indicate time when,
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2705:B. Expressing place to which, with prep. уйй ‘as far as’, in DSf 32 abara yata Bābiraw ‘carried as far as Babylon’, 34 у010 Сй {уа ‘as far as Susa’; perhaps also, because of the idea of motion which seems to be in the verbs, in gátavà avástáyam (DB 1.62f), güfavü niyaSadayam (РМа 36), maškđuvā avükanam (DB 1.86), uzmayà-patiy (DB 2.76, etc.).
2728:E, Н); -patiy (see E); ласа (вее F).
=== SOD ptkr ===
17864:=>ptkrnt-,  'nkr'nt- 
18517:1651  'sptkrmy   M  jlTj^lf  «ai  f  U*i  jfdJ* 
45231:5607  my6ny  ptkrnt'k   B  *j^f*Ja3  ia^j  jl  o^  j'  °^J> 
59679:patkara(k)  ^ptkV,  ptq>ry,  ptkr>k 
59685:patkare   ©ace.  -w;  ob.  -y  ^ptkr'k,  ptqry, 
59687:ptkrq 
59742:7730  ptkr'k   B,  S  JL  <jj> 
59743:patkare   (ptkr>y)  ©<OP  patikara  ©ace. 
59745:ptkr*w\  pi.  -t   ^ptk'r*,  ptk'r'kh,  ptq>ry,  ptqry 
59749:KG  475,  583;  ptkryw,  SCE  87;  Dhy.  120; 
59751:ptkr'kw,  Dhy.  29,  143;  KG  631;  ptkr'yU  Dhy. 
59753:139,  151,  219;  ptkr'yk  ?  TSP  2.646  n  pi 77 
59755:7731  ptkr'nt-  -*  ptkrnt- 
59757:7732  ptkr'st-   S  jj^ 
59759:patkraste   ©pt.  St.;  inf.  -y  =»ptkrnt- 
59765:7733  ptkr'y  =»  ptkr'k,  ptqry 
59767:7734  ptkrq   M,  S  JL,  ^ 
59768:patkare   (ptkry(y),  ptqryy)  ©pi.  ob.  ptqrqtyy 
59772:pi.  ptkryu  Krab.  Insc.  17.12;  W  Lii  54721, 
59776:7735  ptkrnt-    B  o*_s.iO>J'*J»
```


## [2026-09-14T00:51:49.971Z] TOOL CALL #17: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T00:51:49.981Z] TOOL RESULT

```


```


## [2026-09-14T00:51:52.212Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN zahr 678 ===\"; sed -n '5975,5995p' HRN.txt; echo \"=== HUB zahr ===\"; sed -n '2480,2505p' HUB.txt; echo \"=== SOD page for 7730 ===\"; grep -n \"7730  ptkr\\|7730 ptkr\" SOD_pages.txt | head; "
}
```


### [2026-09-14T00:51:52.287Z] TOOL RESULT

```
=== HRN zahr 678 ===
677. zih 'Bogensehne*.
Käs. zeh, ze,
aw. jyd' 'Bogensehne; Sehne* (yt. 10, 70, Geldner,
KZ. 30, 514); ai. i^a-.
kurd. zih 'Bogensehne*; af/. za-l^ bei. j%y (177).
Urform von zih ist "^jtjaka-,
678. zehr 'Gift*, zehre 'Galle*.
phlv. zahr 'Gift* (Men.), arm. LW. zahr,
kurd. zahr, zäir, zur 'Gift' ; af/. bei. (297) LW. zahr,
np. zehre 'Galle' aus aw. *zartaka- ('gelb'), ^zad^raka-,
phlv. "^zahrak und identisch mit zehr 'Gift* nach
Nöldeke, Pers. Stud. I, 38, gegen Justi und
Hübschmann's sonst sehr ansprechende Erklärung
des letzteren aus aw. ^Jadra-, ai. Viatra- 'Mittel zum
Tödten* (Kurd. Spiranten, S. 21 bezw. ZDMG. 38, 424).
Und aw. zaras[ca (ZPGl.), das doch sicher 'Galle', gr.
X^^Vy ist?
679. :iiyän 'Schaden'.
aw. zyana- 'Schaden*; phlv. zi(y)an (talm. Nr"»T;
mand. Xi"»NT) ; skr. (Brähm.) jfydna- 'Bedrückung'.
LW. kurd. af/. ziyän; bei. ziyänl (307); oss. ziän,
=== HUB zahr ===
678. Gegen Noldeke's Deutung ist einzuwenden, dass ap.
^zarta- und *zartaka- im Neup. zu zard und zarda
werden mussten und auch geworden sind, vgl. Nr. 656:
zard gelb', zarda *6alle' (bal. LW. zard gelb*, zardd
*Eidotter , zarddi *6alle*), dass sie mithin nicht zugleich
in deraselben Dialect auch zu zahr, zahra werden
konnten. Der Ubergang von ap. ri m np. rd ist laut-
gesetzlich, derjenige von rt in hr findet sich nur in
gewissen rituellen WSrtern, die nicht neupersisch sind,
wie ich im zweiten Theile zeigen werde. Ich fiihre daher
zahr 'Gift' = kurd. mhr, iar (ZDM6. 38, 72, 107), zah'r
Socin, kurd. Samml. II, p. 311, arm. LW. iahr, phi. mhr
(wie ohne Weiteres fiir zahr gelesen werden kann) auf
*ja&ra- = skr. ^hatra- 'Mittel zum TOdten zuriick und
leite zahra *6alle* (bal. LW. zahrak *Gallenblase') mittelst
des Suffixes a (= phi. ak) davon ab, was doch das
natiirlichste ist, wahrend NOldeke dem Worte zahr^
das sich nur in der Bedeutung 'Gift' nachweisen lasst,
als urspriingliche Bedeutung 'Galle' zuschreiben muss,
um zahr = zahra auf ap. "^zartor- = "^zartaka- gelb'
zuriickfiihren zu k5nnen. Eine Neubildung ist zahra
'Galle' so wie so fiir nicht mehr vorhandenes ''^zdr =
zd. zaras(6a) = x^^^^^ X^^Vf d. GaUe etc.
680. In den Nachtragen bemerkt Horn sehr richtig, dass
np. ztr 'hoch, hohe Stimme, hellste Saite' (= arm. zU
Sopran") mit f (nicht B) zu sprechen und also von
=== SOD page for 7730 ===
25966:7730 ptkr'k B, S                                 JL <jj>         7742 ptkryty ^p'sy       M                       Mc* J^
26035:7730 ptkr'k B,S                                J^><J*         7742 ptkryty Vsy         M                       <Uc
```


## [2026-09-14T00:51:58.565Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=25966 && /\\[pdf page/ {p=$0; n=NR} END{}' SOD_pages.txt >/dev/null; sed -n '1,26000p' SOD_pages.txt | grep -n \"\\[pdf page\" | tail -3; echo ---; sed -n '25960,25975p' SOD_pages.txt"
}
```


### [2026-09-14T00:51:59.705Z] TOOL RESULT

```
---
7729 ptkntw S                                    j£*\g <f>v
     patk(o)ntu ? (ptkyn)                                        7741 ptqrystJn C                     (jL-^L^OU-jK;      ttj&j
                                                                      patkarestan ©ob. -y
      guilty                                                          idol temple
      Anc. Lett. 4.3; BBB p89.763; GMS 148                             BSTi 234, 242, 279

7730 ptkr'k B, S                                 JL <jj>         7742 ptkryty ^p'sy       M                       Mc* J^
     patkare (ptkr>y) ©<OP patikara ©ace.
       ptkr*w\ pi. -t ^ptk'r*, ptk'r'kh, ptq>ry, ptqry                 idolatry
                                                                       patkarct/i-spase     ^ptqry-sp'sy, sp'sy
     image
      TSP 6.135; SCE 90, 94, 22a, BSTBL, Dhy. 17 etc.;                 Sogdica. pl5.12, 13
        KG 475, 583; ptkryw, SCE 87; Dhy. 120;                   7743 ptkry(y) =* ptkrq
        ptkr'kw, Dhy. 29, 143; KG 631; ptkr'yU Dhy.
                                                                 7744 ptqryy =* ptkrq
        139, 151, 219; ptkr'yk ? TSP 2.646 n pi 77
```


## [2026-09-14T00:52:01.214Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD pat ===\"; grep -n \"padīr\\|patkar\\|pahikar\\|patyārag\\|patyārak\\|paytāg\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"patkar\\|patyārak\\|patyārag\\|padīrift\\|patīrift\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T00:52:01.289Z] TOOL RESULT

```
=== PHD pat ===
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:709:acceptance padīrišn.
PHD.txt:1361:consult pahikardan.
PHD.txt:1371:contend with pahikar-.
PHD.txt:1531:defeat pahikar-, stówénidan.
PHD.txt:2085:Gemini D6-pahikar.
PHD.txt:2377:image nigārag, pahikar.
PHD.txt:3121:picture pahikar, nigārag.
PHD.txt:3338:reception padīrišn.
PHD.txt:4615:pattügih pattüg paywastan paywastag pattüdan pahikar 1-2pahikar- pahikardan pahikāf- pahikāftan pahikob- pahikoftan pahikar pahikaf- pahikafián pahikaftan payrastan payrog pahrmāh- pahrmāhāgīh pahrmāhišn paymāy- paymānīgīh paymānīg
PHD.txt:4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
PHD.txt:5418:dópahikar
PHD_mackenzie.txt:2011:dol-pahikar [dwptkll N du-paikar] astr. Gemini.
PHD_mackenzie.txt:3917:padiran                           63                       pahikardan
PHD_mackenzie.txt:3971: pahikar [ptk)!1 M phyk»T, N paykiir] struggle, battle, dispute.
PHD_mackenzie.txt:3972: Ipahikar- [p"tk)!.] fight, contend with, defeat.
PHD_mackenzie.txt:3973: pahikardan, 2pahikar- [ptk)l-tn ] request, claim, consult.
PHD_mackenzie.txt:6017:   pesgiih.                                 pahikar, razm, P padrazm; do -
PHD_mackenzie.txt:6194:claim pahikardan.                        commission gumardan.
=== NYB ===
3053:patkaritan
3059:patkar [ptkly, Prth ptkr]image ŠPrs: 3. 14. Prth:4. — OP pati-kara-; MPrs phykr; Arm. lw. patker ; Syr. Talm. lw. ptakrä ‘an idol’, Mand. lw. patikrä; NP paikar.
3062:patkarit [—-yt'] altercation, quarrel 572. patkäritan [~-ytn'] to dispute, to dis-
4919:pati-kara: patkar
5674:pdk’r: patkaritan
6073:phyk"r: patkar
6075:phykr: patkar
7302:paigàr: patkar
7306:paikar: patkar
```


## [2026-09-14T00:52:16.537Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"padīrag[^.]*\\.\\|petyārag[^.]*\\.\\|patyārag[^.]*\\.\" PHD.txt | head -10; echo \"=== NYB padirag/patyarak ===\"; grep -n \"patyārak\\|patyārag\\|ptydlk\\|padirak\\|patirak\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-14T00:52:16.601Z] TOOL RESULT

```
737:petyārag.
1816:petyāragīh.
2824:petyārag.
=== NYB padirag/patyarak ===
394:of; o pattākēh ~ to appear 513, 1081; 6 patirak ~ to meet 8%. 731.20-21, ete.; 6 en kustak rón towards this district 715; — with hac: from 184 ete. [hac ... be 6 ... ~ to be converted from... to... PR 945]; hac ... ywvatük away from 747-8, 7667; — with pat: on (a path) ibd. ; — with prev.: andar — to come forth, to appear 87?5; to be handed down 10818-19; — apāc ~ to become again 104?*; apdc 6 to return to 5) (v. bälist). 818-19, 914, 12]9-10; hac ... apāc ~ to return from 991; — apar ~ to shoot up 9573-4; to be allotted to 98*; apértar apar āyēt ku surpas- ses 641%; — hac varten beron be ämat got off the chariot 20?3; (coursers) ke pat róc-6 70  frasang bē āyēnd- (h)b who are always riding a dis- tance of 70 parasangs in one day 6! (v.s.v. h-); hān<i>druž (be) āyēt the space which the Drug will cover 96?3, 9818; bé + the pres. of ~ regularly denotes the fut.: 24"; if the vb. takes the prep. 6 the order is always be 6: 9725, 985-6, 9912-13, 1046-7; — fröt ~ to come down, to descend (hac...6...) 104°; — ul ~ to rise 86°; šuhr pat post ul āmat the sperm rose to the skin 547°. — āmatan < *ā-gmatanai from à + Av. (493 sqq.) OP gam-, cf OP (par)ägmata- ‘gone forth’; äy- < à + Av. (147 sqq.) OP ay-; MPrs ’mdn ”y-; Paz. NP dmadan dy-. This vb. is characteristic of the SW dialects, as against NW āgatan,
1758:hae [MN ; hc 619] prep., with -c: MN-c = hac-ic; not with an encl. pron. (as to haciš, hacisan v.s. v. hactš); the original sense ‘accompanying, with’ (Skr sacā) is still transparent in ~ ... hämisi (g. v.) ‘together with’, but the meaning ‘from, of’ prevails since the OIr period. 1. Local: hàn yam ... hac dast i Artaxser 6 damik opast 92°; api-š hecak hac cah ul hixt 155; hakar hac asp bē nisinam 27?; hac star püdak tai mah pädak 93"; hac dar ētšān bagän namäc burt from the gate-way (i.e., halting at the entrance, from this place) I rendered adoration to His Majesty. P1:4; — figurative, with a great many vbs. and idioms, the sense of ‘from, of’ being more or less transparent. akahé- nitan, āšnūtan, pursitan, x"āstan, dast šustan hac ete., v. the individual ws.; — origin: ke cihr (Prth Shr) hac yazatān (Prth y’ztn) whose origin is from the gods, of divine origin HajB: 2.4 (HajA: 2.4). SPrs: 5-6 (yazdān) (SPrth: 5). P1: 2.4 (yazdàn) ; "Apasči... à hac Haran ŠPrs: 9; hac tohmak + Dārāt būt 18, etc. — 2. tem- poral: hac im róc from today onwards, henceforth 9"; hac im réc tdi 3 roc within three days 51%; hac rahikehv [lsykyhy] ever since my youth 1282-5; ete. — 3. after a v. n. it expresses the subj. of the act: patirak zanišn + hac ganäk menoi on the point of being slain by the Evil Spirit 46°-§; zanisn i devàn hac han i 0$ xvarrah the demons being slain by his divine splendour 461?; freftakeh + hac dēvān de- ception by-the demons 461; 4513-14; ete. —
2135:ka [MT], with encl. ’MT-m = ’MT-t = ka-t, °MT-š = ka-š ete.: 'MT-e = ka-c: A. conj. when, as, while; because; though, whilst; if; that. 1. temporal: standard type of period referring to the past: Pāpak ka-š hàn saxtan āšnūt kas fréstit by P. when by him this word was heard a man was sent = when P. heard this he sent a man 21!; passim; if con- taining an encl. pron. the apodosis is introduced a) by adak + encl., e. g. api-n ka én tigr vist adak-in . . . vist and when We shot this arrow, We shot it ... HajB: 4-6; 545-5; — b) by api- + encl., e. g. ka hac star frac būt api-š ... guft kū then he said 60?*; — c) by the independent forms of the enclitics: am, at, aš, aman, atān, ašān: hän étén amavandeh + ka zivandak bit hom am bit that great vigour which was mine when I was alive 345-6; ka giyāk-ē päh i gospandan vēnēnd ašān avd sahét when they see somewhere a flock of sheep it will seem astonishing to them 9724-25; — the apodosis may be introduced by adak alone (v. this w.); by pas (914-*); by andar han in the meantime (561°); — ka ... apāc àyet aš Kat-Xosroi bē 6 patirak āyēt ka pat vài našast ēstēt when he comes back he will
2785:8 [L, ^'w'; KN] či [LH; LH-y 104; ‘L-y 34%, 528-19] prep. to, with vbs. of motion; temporal: until; the sign of the indir. obj. (2277-5 perhaps the sign of the dir. obj. according to Prth. usage); — combined with other prepositions: andar 6, tài 6, or with an adv.: bē 6, fräc o, nazd 6; — governing a subst. or an adv. and forming with them compound pre- positions and adverbs: 6 berön, 6 nazdik, O pasth, 6 patirak, o peš (frac 6 peš, andar 6 peš); in a frame prep.: 6... rón; v. these ws.; — prev.: 6 druž früc mat the drug came to the place 5715-16; jn this case the ideogr. KN is common: 348 twice. 6521, 9422. — The form LH = 67 as a prep. 1612. 4210, 4424-25, 5617, — 6 cannot govern an encl. pron.; if such a pron. is affixed to the prep. it always belongs to the governed subst.: 6-š zäyısn until his birth 44!2; frāc ör-Sän deh vénam I foresee for their country 504; — in certain cases 6 is replaced by the adv. avis (g. v.). — Represents both Av. (163) ava, OP ava, and Av. (180 sqq.) avi, ao; MPrthPrs ’w; Paz. ó. The ideogr. KN originally rep- resented MIr (MPrthPrs) 6h < Av. (171 sq.) avada, OP avadä ‘thus’; in BP, having lost its final -%, it is used as 6, but chiefly
3033:patirak [ptylk'] a meeting: bam-é i hac ~ + (a light produced by the meeting of...) a light reflected from, a reflexion of 11218; — mostly combined with a vb. of motion: 0 ~ āmatan to meet 84. 731-2! ete. ;
3571:-š encl. pron., cas. obl. of the pers. pron. 3d p. sg.; regularly attached to the first w. of the sentence, preferably to particles: api-š, adak-iš, be-š, cigon-aš, ka-š, etc., or to a pron., v. ce, 2, ké, sometimes to a w. in the interior of the sentence (406, v.s.v. pat-frācēh; 48°. 914, v. below); if it is attached to a subst. it never depends on it as its poss., but refers to another w. in the sentence; it is never governed by a prep. (single exception 54%, v. s. v. apar); it has an independent form aš (g. v.). It expresses 1. the gen. his, her, its: api-š bar xrat and its fruit is Wisdom 6613; fravahr i Zartuxst api-$ tan gohr Z.’s fra- vashi and his corporeal substance 4226-27; 4-$ his, her, its: tāt matan 1-š 0... 4714; — 2. for, to him (ete.): apt-š... 6 patirak āyēnd go to meet him 741-2; api-š vát-ic hayyār bavet 25°; — 3. dir. obj.: api-š nod be barem 3915; ka-š vir royét x"arét he who believes in it eats 1002; (he said) ku-"'$ man be 6 vahist ne hilom” 3425 (dir. speech aš); — 4. the agent, passim: cigon- aš dit as soon as by him was seen 19!?; ka-š hàn saxtan āšnūt 2219; Pourušāsp hac Zartuzšt, pat višopišn i haciš, -(a)š škujt tarsenit P. was terribly frightened by him (the Karap) because of Z. that he should suffer destruction by him 488-9; still unexplained is the construction in api-š ... šamšēr HDWN-yt' (commonly for pres. girét) u tak BYDWN.x, (com- monly for kunēt, but cf hištan) 2220-21, — Proleptically, anticipating a subst.: cigon- aš dit kanicak as soon as she, the girl, saw 15°; adak-iš mčnit Pouruščisp kü then he, P., thought 40%; api-§ guft, apar apäc vast, Pourušāsp and he, P., returning said 5117-18; — anaphorical, taking up a
5002:paiti-lar-: patirak
5260:paiti-lar: patirak
6069:pdyrg: patirak
```


## [2026-09-14T00:52:19.088Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT paityara ===\"; grep -n -i \"paityara\\|paiti\\.ara\\|paityära\\|paitidra\" BRT.txt | head -10; echo \"=== BRT paiti-grab ===\"; grep -n -i \"paiti\\.gsrsw\\|paiti\\.grab\\|patigrab\" BRT.txt | head -10; echo \"=== BRT patikara ===\"; grep -n -i \"patikara\\|paiti\\.kara\" BRT.txt | head -10"
}
```


### [2026-09-14T00:52:19.180Z] TOOL RESULT

```
=== BRT paityara ===
=== BRT paiti-grab ===
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
14913:patigrabanä-  828
=== BRT patikara ===
12384:matum  .  .:  interfeci  et  (eos)  qui .  .  erant" Bh.  i.  13;  —  patikaram  didiy  'yaiy  manä ga'äium  ii7rB"(!(j'"simuIacruni3pecta{eorum) qui  . .  portant"  D.  6.  4.  11)  2ur   An-
12782:—  ya/iiy  imSm  dipim  vainlhy  imaivä patikara  naiydi!  (fi^n.)  vikanäky  utämaiy yava  taumä  aAatiy paritarahidii'Sii.4-f^',
12783:—  yadiy  imäm  dipim  imaiva  patikara vaimiAy  vikanahidtl  utamaiy  yävä  taumä  ; akatiy  naiydis  parikaräky  '^.4.\T,  — ■ paiikaram  dldiy  tyaiy  inanä  gä'isum  bari^- tiy    ava'äiä  xinäsähidii^'^  (APm.)   D.  ö.  4;
13260:i)  'sehen,  hinsehen  auf  — ,  beschauen': patikaram  didiy  (2SIA-)'*  tyaty  mani gj'ium  bar^tiy  D.  6.  4;  —  spasö  .  .  are aipi  (sd.)  dai'Aantö  (NP.)''  .  .  ydi  .  .  Yt. ro.  45;  —  lakrpa-  avavatam  sraya  yaia dilayatam  (GP.)"  sao'sö  (sd.)  YL  /;. 1 1,  z)  'im  .\uge  behalten,  beobachten': tarn  dastqm  yä  hatqm  (Sp.  268  o.)  rahistti .  .  irrrimKi/  ux'nlis  ^aoianil  >rM  datdyat {■^YtK^'''^  mahyh  i:7rft'//(sd.)"dieReligion.T werden  sie  sie  mit  den  Worten  und  dem Tun  der  Frommei^ebenheit  richtig  be- obachten .  ."  Y.44.10.  3)  'Jemandes Acht  haben,  sich  kümmern  um— '(Gen.): mit  ?r3s.vaca  sarim  (GP.;  sd.)  didqs(^%^
21108:•  p.  ya'diy,  j.  ye8i'>,  yei8i'>  Konjn. I)  II  zeitlich 'zu  der  Zeit  als' ;  viyaxnakya\  3.-ai\i\\X, mähyn  14  raucabii  'kakaiä  äka'  y  uda- patatä  Bh./.  II.  II)  bedingend  'wenn, sofern';  i)  mit  (fiitur.)  Konj.,  a)  vor  dem Hauptsatz:  II  y  kürj'  pärsj'  patc^  aha- tty ..  siyätis  .  .  nirasstiy  .  ■  D.  5. 3;  — y  av(^a  *maniyähay  .  .  imam  pärsatn käram  pädiy  D.  5. 3;  —  y  imäm  dipim vainaAy  . .  uta  parikarähidil  J'urJ'mazda %uv3m  daufta  blyä^Bh. 4.  16;  17,10,11;! —  *(^(  sL.aSe  vacS  ustime  urvaese  gayehe /ramrai'3i{aS.)  pairt  te  tanava . .  urvamm . . Y.  7/.  ig;  —  im  Nachsatz  steht  «Sa:  °i%i zT  kvari  nUii  uzuxsyeiti  aha  datva  vTsph minnänta  "wenn  (einmal)  die  Sonne  nicht aufgehen  wird,  dann  werden  die  D.  alles zu  nichte  machen"  Yt  6.  3.  a)  ||  mit ^•^«/(^(sd.)  'wenn  etwa':  ^yadipatiy  *'ma- niyähay:  ciyJ'karam  (sd.)  .  .  patikaram dldiy  D.  6.  4.  b)  U  hinter  dem  Haupt- satz: martiy^  ky(^  draujaitJ'  ahatiy  avam *^u/iasata>n    pars3    y     avada    *mam-
```


## [2026-09-14T00:52:27.580Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"patikara\\|patikar\\|sculpture\" KNT.txt | head -20"
}
```


### [2026-09-14T00:52:27.628Z] TOOL RESULT

```
55:THE INSCRIPTION AND SCULPTURES OF DARIUS THE GREAT AT BEHISTAN Copyrighted by George С. Cameron, by whose courtesy tt appears here
122:І The Inscription and Sculptures of Darius the Great at Behistan.............. II The Gold Tablet of Hamadan ПІ The Daiva Inscription of Xerxes
270:KT = {L. W. King and R. C. Thompson,] The Sculptures and Inscription of Darius the
1786:Passives: ha™-dugd- ‘im-pressed’ = ‘inscription’; pati-kara- ‘made thereto’ = ‘sculptured figure’; asa-bara- ‘horse-borne’.
3295:DB = Dans, BeursTAN: The inscription of Behistan, trilingual, is inscribed on the face of a gorge in the cliff rising on the left-hand side of the main caravan route from Baghdad to Teheran, about 65 miles before reaching Hamadan. Here, at the height of about 225 feet (obliquely 322 feet) above the road, the last 100 feet being steep and difficult, rock-climbing—the final portion being in part cut smooth by Darius's orders, to prevent access by vandals—sculptures and accompanying inscriptions are engraved in the natural rock. The panel of the sculptures contains at the left the standing figure of Darius, with two attendants behind him; his right foot is firmly planted on the prostrate figure of Gaumata. Beyond Gaumata stand m line the captive rebels, 9 in number, with hands tied behind their backs and a rope around their necks linking them together. Above, there is a figure of the God Ahuramazda. The inscrip- tions in OP, Elam., and Akk. occupy the free parts of the panel and its lower margin, as well as the spaces below, to right, to left, and diagonally below to the left. These have suffered both from erosion by water torrents and by limestone in- crustations deposited by water in and over the engraved characters. Further damage was suffered
3297:by the sculptures 3n both World Wars, when soldiers marching past on the highway below used the figures as targets for potshots.
3298:Behistan is a much used but not recorded spell- ing which is intermediate between the OP *baga- siána— Place of the God’, for which Greek has Baytoravoy (Diodorus 2.13), and the Behistin of the medieval Arabic Geographers, the Modern Persian Bisitiin or Bisulün (or even Bistiin, with- out the anaptyctic vowel; understood by popular etymology as ‘without columns’). The inscription was first reached and copied by Lieutenant (after- ward Major General Sir) Henry C. Rawlinson in 1836-47; again in 1908, by Professor A. V. Wil- liams Jackson of Columbia University, who was able to make only a partial examination, but did make the first photographs taken from the narrow ledge below the inscriptions; by L. W. King and R. C. Thompson of the British Museum in 1904; and finally by Professor George G. Cameron of ihe University of Michigan in 1948, who made a thorough examination of the entire inscription, including the Elamite text to the right of the sculptured panel, which had previously been pro- nounced completely illegible.
3299:The Great Inscription: the OP text is in 5 columns, beneath the panel of sculptures; con- taining 96, 98, 92, 92, 36 lines respectively. Col- umn 5 is at the right and isa later addition. The Elam. text is in two copies; опе copy, in 4 columns totaling 323 hnes, stands to the right of the sculp- tures, the final addition to which has cut into the first column (this is the supposedly illegible in- scription, formerly dubbed ‘supplementary texts’, now for the first time read by Cameron). The second Elamite copy is in 3 columns, to the left of the OP text; containing 81, 85, 94 lines re- spectively, the equivalent of the first 4 OP col- umns, to the end of §69. A short column of 10 lines, in the upper left of the sculptured panel, is the Elam. equivalent of OP §70. The Akk. text is in a single column, running past an obtuse- angled corner so as to cover two faces of the rock to the left of the sculptured panel, and translates OP §1-§69; it contains 112 lines (lines 1-35 on front face only, lines 36-112 on the two faces of the rock).
3305:Rawlinson, JRAS vols. 10-11 (1846, 1849); vol. 12, i-civ (1851). Jn. JAOS 24.77-95 (1903) = Persia Past and Present 186-212 (1906). KT, The Sculptures and Inscriptions of Darius the Great on the Rock of Behistün in Persia (London, 1907). Tm., The Behistan Inscription of King Darius (Vanderbilt Univ. Studies I, Nashville, 1908). Wb. and WBang, Die Altpersischen Keilinschrif- ten in Umschrift und Übersetzung, fasc. 1 pp. 4-5, 12-33 (Leipzig 1893), fasc. 2 pp. x-xvi (Leip- zig 1908). Tm., Ancient Persian Lexicon and Texts 2-36 (Nashville 1908). А. Hoffmann-Kutschke, Die аір. Keilinschriften d. Grosskónigs Dáraja- wausch d. Ersten am Berge Bagistin, bei Behistun (Stuttgart, Kohlhammer 1908 and 1909). Wb. Die Keilinschriften der Achimeniden xi-xiv, 8-79 (Leipzig 1911). FM EPereira, Iserig&o de Dario o Grande, Rei da Persia, no Rochedo de Bisutun (Coimbra 1913). Shapurji Kavasji Hodivala, Cuneiform Inscriptions transcribed into Sanskrit and Avestan: Behistan Inscriptions, in JCOI 19.58-158 (1931). FWKonig, Relief und Inschrift des Königs Dareios I am Felsen von Bagistan (Leiden 1938). Sen, OPI 2-88 (1941). GGCam- eron, Life May 23 1949 pp. 149-52, National Geographic Magazine (shortly to appear), Jour- nal of Cuneiform Studies (shortly to appear).
3363:XPe = Xerxes, Persepouis x: Trilingual, in duplicate (see below), each version 4 lines, with slightly differing line-divisions in OP; ea on a post of the north door, above the. sculptured figure of the king; eb on a post of the east door, also above the king’s figure. There are also numerous other copies of this inscription inside and outside the doors and windows, frequently in one-line and two-line arrangements (Cameron’s data). Tm.
3453:scription mentioned the sculptured figure in the doorway below, with a prayer to Ahuramazda for protection; but further reconstruction is a3 yet impossible. Not ali the Fragments given in Herafeld’s Plate belong to the same inscription; one such fragment contains clearly the word »}182{ya “n the palace’.
3861:71 ām : adam ; niyapaisam : imaiva : patikarà : mátya : vikandhy : yàvà : u
3863:73 diy : imam : dipim : vainühy : imaiv& : patikarà : naiydis : vikanahy : uta
3871:77 yafiya : yadiy : imam : dipim : imaiva : patikarà : vaināhy : vikanah*dis : ut 78 ataiy : уйуй : tauma : ahatiy : natydiš : paribaráhy : Auramazdátaiy : jatà : b 79 iyā : ut&taiy : taumd : mà : biyá : uta : tya : kunav&hy : avataiy : Auramazd
3922:have inscribed, or these sculptures, do thou not —$
3925:$66. 472—6. Saith Darius the King: If Шоц. 4 shalt behold this inscription or these sculptures, 2 | (and) shalt not destroy them and shalt protect i1 them as long as unto thee there is strength, may |
3927:ily be unto thee in abundance, and may thou live —.] long, and what thou shalt do, that may Ahura- 4} mazda make successful for thee! : 867. 476-80, Saith Darius the King: If thou — . shalt behold this inscription or these sculptures, —. (and) shalt destroy them and shalt not protect `} them as long as unto thee there is strength, may — } » Ahuramazda be а smiter unto thee, and may family not be unto thee, and what thou shalt do, * that for thee may Ahuramazda utterly destroy! — - $68. 4.80-6. Saith Darius the King: These are | the men who were there at the time when I slew Gaumata the Magian who called himself Smerdis; at that time these men cooperated as my follow- _ ers: Intaphernes by name, son of Vayaspara, a Persian; Otanes by name, son of Thukhra, a Per-
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4114:$4. 30-47. Saith Darius the King: Ahuramazda, when hesaw thisearth m commotion, thereafter be- stowed it upon me, made me king; I am king. By the favor of Ahuramazda I put it down in its place; what 1 said to them, that they did, as was my desire. If now thou shalt think that “How many are the countries which King Darius held?” look at the sculptures (of those) who bear the throne, then shalt thou know, then shall it become known to thee: the spear of a Persian man has gone forth far; then shall it become known to thee: a Persian man has delivered battle far indeed from Persia.
4338:1 imam : palikaram : Dárayavaus : XŠ : niyadtdya : cartanaiy : +++... 2 ...++-++na : Dirayavaum : XSyam AM: pälwv : ulà : tya : kartam TRANSLATION OF D$n: This sculpture Darius the King commanded to make; ... Darius the
```


## [2026-09-14T00:52:28.642Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"paiti\\.gr\\|grab-\\|g3r3w\" BRT.txt | head -20"
}
```


### [2026-09-14T00:52:28.693Z] TOOL RESULT

```
10400:•  j.    garapta-    Adj,    (fem.    'lä-),    VVlP.:\aAur3m    Tim  Yt.  70.25;  —  tattuATs'  Tii s.  grab-.  (näml  fravasays)  Yt.  /J.30.
10405:'grab-  3
10436:•  j-,  g.,  p.  'grab-  V.  'greifen'.  Praes. i  grab-,  11%  g^rminä'^,  15  girißa-*'"'^ , 23  garb.tya-,  gSun'aya-'^,  24  gSurvaya-'^, <)-^  24 ^3r?mbaya-'^,2T g)r3bya-,gpr)uya-^'>; Perf  I  jagaurv-*^,  jayaurv-^^,  ftgaurv-^^, 2  jag»r»b-.  —  PPf P.  g^r^ta-'');  Inf.  gfnbqm.
10452:'grab-  mit  ham
10467:5*9  'grab-  Noten  —  yzar-  mit  aiwi  530
10472:geschr.;  S  i^^S.  39.  —  »)  S  5J  H.  —  3)  Stall  [  j-  .f™":  s.  unter  ^grab-.
10487:.   j,    'grab-    (Fassung  uzw.  von  Wortern,        _  p^..  t„nsskr.,    erL.:  /.Fw-f  'Geschenk.  Be-
10508:Ei.f  —  mp.'(Pü.)  grm<,  np.  7rtrr'.  —  ')  Oder   yiaroutJs    (IP.    als    NP.)    * antari.ar»o)m ■,^0«.  (S  268.  37);  ob  zum  V.  grab-t  .  -^rt/«,^^^  V.J.  19.
14928:Eig.  'receplaculum',  zum  V.  grab-.  —  ai.  vgl. praligraAana-  n.  —  ')  Es  könnte  'nä  auch NPn.  »ein.
15590:Nach  Pü.  zum  V.  grab-;  also  'girimby''!  — Pa.;  fratam  kac  dahmän  ke  apar  glrlt pätixiäh
29346:•  j.  han-gnt^-amna-  Adj.,  PPM.:  s. grab-.
```


## [2026-09-14T00:52:36.123Z] TOOL CALL #25: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KNT','SOD','FSF','AEF','FVF','BQT','MON','POK','AHD']:\n    print(k, json.dumps(d[k],ensure_ascii=False)[:900]); print()\n\""
}
```


### [2026-09-14T00:52:37.212Z] TOOL RESULT

```
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Dony

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
```


## [2026-09-14T00:52:48.379Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==210' KNT.txt | grep -n -i \"patikara\\|patis\\|pati\" | head -10; echo \"=== check leaf ===\"; awk 'BEGIN{RS=\"\\f\"} NR==210' KNT.txt | head -5"
}
```


### [2026-09-14T00:52:49.405Z] TOOL RESULT

```
=== check leaf ===
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
Táravà- sb. ‘Tarava’, a town in Persia; Elam. -F-ra-ü-ma, АКК. ta-ar-ma-. Тато nsf. DB 3.22.
```


## [2026-09-14T00:52:49.543Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -io \"bezoar[^.]*\\.\" AHD_watkins1985.txt | head; echo \"=== gwhen ===\"; grep -n -o \"gwhen-[^|]\\{0,900\\}\" AHD_watkins1985.txt | head -4"
}
```


### [2026-09-14T00:52:50.495Z] TOOL RESULT

```
545:BEZOAR.
812:BEZOAR.
=== gwhen ===
```


## [2026-09-14T00:52:54.330Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \".\\{300\\}BEZOAR.\\{80\\}\" AHD_watkins1985.txt | head -4"
}
```


## [2026-09-14T00:52:55.698Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"patikara- sb\\|patikara-  sb\\|patikara- \" KNT.txt | head; echo \"---leaf scan---\"; awk 'BEGIN{RS=\"\\f\"} /patikara- / {print NR\": \"substr($0,1,120)}' KNT.txt | head"
}
```


### [2026-09-14T00:52:55.842Z] TOOL RESULT

```
545:dard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form 
812:atin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector
```


### [2026-09-14T00:52:56.885Z] TOOL RESULT

```
5277:kara- sb. ‘doer, maker’, as 2d element of cpd.: deriv. of kar- ($82, §143.1); found in avükara-, ciyükara-, düraniyakara-, zürakara-,  hakara-, hamaranakara-, and with passive meaning, 'thing made’, in patikara- (cf. Bv. Gr. $289).
5632:patikara- sb. ‘picture, (sculptured) likeness’: .
---leaf scan---
203: om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2).
акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47.
akun
219: with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $1
```


## [2026-09-14T00:53:18.041Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1",
 "prompt": "Give the full etymology given for Persian پادزهر (pādzahr): what elements, what Middle Persian form, and any descendants (Arabic, Spanish, English bezoar)."
}
```


## [2026-09-14T00:53:19.110Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1",
 "prompt": "Under the Persian section, give the etymology of زهر zahr 'poison' (Middle Persian, Proto-Iranian, PIE root, cognates)."
}
```


### [2026-09-14T00:53:23.495Z] TOOL RESULT

```
# Etymology of Persian زهر (zahr) 'poison'

Based on the Wiktionary entry, here's the etymological chain:

**Middle Persian origin:** The word derives from "zʾhl" in Middle Persian, meaning "poison, venom."

**Earlier ancestry:** The entry does not provide information about Proto-Iranian forms, PIE roots, or cognates in other language families. It only traces the word back to Middle Persian, stopping short of deeper historical linguistic connections.

The page does show extensive **descendants** across many languages (Turkish, Armenian, Bengali, Hindustani, Uyghur, and others), demonstrating the word's influence through Persian expansion, but the ancestral etymology beyond Middle Persian is not documented in this source.
```


### [2026-09-14T00:53:23.914Z] TOOL RESULT

```
# Etymology of Persian پادزهر (pādzahr)

**Middle Persian Form:** The word derives from Middle Persian *pʾtzhl* (pādzahr), meaning "bezoar, antidote."

**Compositional Elements:** By surface analysis, it combines:
- *پاد* (pād-, "anti-") 
- *زهر* (zahr, "poison, venom")

**Notable Descendants:**

The term traveled across languages through trade and cultural exchange:

- **Arabic:** Multiple forms including بَازَهْر (bāzahr) and بَادِزَهْر (bādizahr)
- **Spanish:** Old Spanish *bezahar* → Modern Spanish *bezaar*
- **English:** *bezoar* and *bezoard* (via French or Spanish)
- **European languages:** French *bézoard*, Italian *bezoar*, Portuguese *bezoar*, Swedish *besoar*
- **South Asian languages:** Hindi बेज़ार (bezār), Urdu بیزار (bezār)
- **Ottoman/Turkish:** *panzehir*

The widespread adoption reflects historical importance of bezoars in traditional medicine and pharmacology.
```


## [2026-09-14T00:53:27.543Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bezoar",
 "prompt": "Full etymology of 'bezoar': route through French/Spanish/Medieval Latin/Arabic/Persian, forms and dates."
}
```


## [2026-09-14T00:53:28.859Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/press",
 "prompt": "Etymology of 'press' (verb and noun): Old French, Latin pressare/premere, and the PIE root cited. Also what it says about 'print', 'express', 'compress' if mentioned."
}
```


### [2026-09-14T00:53:31.982Z] TOOL RESULT

```
# Etymology of Bezoar

The word **bezoar** entered English in the 1540s, referring to "a stone used as an antidote against poison." It traveled through Medieval Latin from Arabic *bazahr*, which derived from Persian *pad-zahr* meaning "counter-poison."

The Persian term breaks down as:
- *pad* = "protecting, guardian, master" (from Iranian roots)
- *zahr* = "poison" (from Old Iranian)

By the 1570s, the meaning expanded to include "a concoction from solid matter found in the stomachs and intestines of ruminants," which was believed to possess antidotal properties. The word's journey illustrates medieval Europe's absorption of medical and pharmaceutical knowledge from Persian and Arabic sources, reflecting the prominence of these traditions in early modern medicine.
```


### [2026-09-14T00:53:34.825Z] TOOL RESULT

```
# Etymology of "Press"

## Noun Origins
The noun "press" (c. 1300) derives from Old French *presse*, meaning "a crowd, throng" or "wine or cheese press," which came from Latin *pressare*. The sense of "machine for printing" emerged in the 1530s, later extending to "journalists collectively" by 1921.

## Verb Origins
**Press (v.1)** - Early 14c., from Old French *presser* ("squeeze, press upon"), derived from Latin *pressare*, a frequentative of *premere* meaning "to press, hold fast, cover, crowd, compress." This traces to the PIE root *\*per-* "to strike."

**Press (v.2)** - 1570s, meaning "force into service" (military/naval), altered from *prest* through association with press (v.1). It stems from Latin *praestare* ("to stand out, provide"), from *prae-* "before" + *stare* "to stand" (PIE *\*sta-*).

## Related Terms
While the page doesn't detail "print," "express," or "compress" extensively, it notes that "express" (late 14c.) similarly derives from Latin *exprimere*, literally "to press out," sharing the same Latin root *premere*.
```


## [2026-09-14T00:53:46.334Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT paitii ===\"; grep -n \"paitiiara\\|paitiiär\\|paitiiar\\|paitiara\" BRT.txt | head -10; echo \"=== HRN pazir ===\"; grep -n -i \"pezir\\|paziruft\\|pezTruftan\\|peikar\\|paikar\\|patyare\\|patyär\" HRN.txt | head -20"
}
```


### [2026-09-14T00:53:46.399Z] TOOL RESULT

```
=== BRT paitii ===
4951:Satzes  'jedoch':  *k!ra  .  .  *a^st»im  fiaiti.- bamt?  antarf  (sd.)  aAuna  *airyamana *Sy^mcit  a°  vilcim  gii^anqm  asrutpm  (sd.) paitiiarS  aratufris  N.  10^.
5971:mit  ä  dnwS,  4  a;  yezi  näil  paitiiaraiti *%rl  vs  äsäiti  ayar»jiräjö  (sd.)  vä  vastryä£ N.  69;  ^2,  43,  <V?,  log'''.
12559:(ND,)F.  _3g;  —  cvat  na  *mt?>na  alsmahe (sd.)  paitiiarS  ratufriii  yaha  vansnahe kihrpahe  äSus  (NS,)  ".  •  (so  gross)  als  der Oberarm  eines  Mannesleibes"  N.  S06;  F. 14"-
16988:—  tä  (aimi. /ravasays)  el  starsta^  'möhu saoyä  Yt.  y.  a  7 ;  —  ys  'maca  ^frastfrinte gSulca  paitiiaraiti  ti.6o;6o;  —  %risum 'ma  frastjritmyA  paitila  hü  a^wansm  Yt. 12.  3;  —  ys  .  .  rapiUwiftfin  . .  fräyasäite
18975:•  j,  'n«inah-  n.  'Darlehen':  yS  natre  n»- mataAgnte  nBit  'mS  paitiiaraiti  täyus 'mariAs  bavaiti  AazaaAa  ivms.baraA£  "wer einem  Darleiher  das  Darlehen  nicht  wieder- gibt, wird  zu  einem  Dieb  des  Darlehens, zu  einem  Räuber  am  Darlehnsgeber"  V, 4.1.
21418:—  fi-avalayJ  siaomi  sbayemi  (sd.)  ufyemi yazamaide  nmänyS..  Y.17.18; — vtspalca alte  afts.h3g»t{^A^ . .  (sbayemi)  yasamadalea Y.  7/.  1 1 ;  —  yat  zaota  ahunm  mazdqm yassiti  *mal?>näi  barysmqn  paitiiarsit amiis  spmts  yasäiti  ..  "wenn  der  Z.  das Gebet  an  AhM.  spricht,  soll  er  .  .;  wenn er  das  Gebet  an  die^^.^.  spricht, , ,"  N.  70  »;
27526:yasamaide  hävauämm  .  ,  Slravaxstm  .  , |G.j.s;  V,5,57,58;  —  vUäi  v!  anusa ipmtä  staotä  Uä  zbitä  . .  Y.14. 1 ";  Vr. 5.1; —  stofftarxa  'tanca  tiatania  Yt.j. i;  —  az3m  ..  'ta  rlrJ/ (Sp.  1327  o.) slaotanqm  yesnyanam  frasrao%r3mca  .  . fräyastlnüa  Vr.j.  7;  —  tum  tta  akra^m *sactasie  (Sp.  1607  o.)  *  'V1.3.  7;  — ya^a dis  atpm  y5  °ta  itva^ayemi  vi%vä  a^qm yasn»mca  vahmimca  . ,  Vr.  Jr.  1 9 ;  —  kaha 'la  xsata  vala  SfS  .  .  yazätte  Y,  6^.  9; 9,  Yt5.  131,  so.  120;  —  bfr7Z3in  barät  'la väiim  Aisbmra  pasia  banstna  Yt/7.61; 10. 137,  138;  —  dayata  . .  aps  ttiäva- yaia  '^re  yeztmnai  ahmaktm^a  maxda- yamanqm  fräyatsmnattam  .  .  Y.6S.  12; 2,  39.30;  —  hana^a  tu  tum  taj  mtcd^m ya^  'ta  hanayamnS  ättha  frayB.kumatB  . . Y. 55.30;  —  ar?dvT  .,  -5«  (statt  Gen.) väHm  paitiimarfmna  Yt  5.113;  —  daAmd •la  tanupiriia  (sd.)  upa.sraotarl!  N.jS; 3g^;  — surunaoiti  *'tai1  upa.sraotaraiiqm (sd.)nöit upa.sra0tarB  •tarB{GS.)'ta  raiufris N.  27;  2/';  ~  Si  '/arI{GS.)  iairim  ai^Aai myatdahe  *ayqn?  (ya/)  *ga%asca  fratrsva- yaiti  vantnca  af3he  (Sp.  108  m.)  *astvaite paiti.ähaySt  aka  ratul  '"Was  ist  das  Amt des  Z.  am  Tag  des  My."}'  'Dass  er  die G.  vorträgt  und  der  Gemeinde  auf  ihren Gesang  mit  <£iia  ratus  (msv.)  antwortet'" N.  72;  —  aat  *atravaxiahe  (sd-,  oämL  kai- rim  arahaf)  yat  . .  •Prälat  väcim  paiti.- aiaya^  H.  J3 ; — yaha  ahB  vairyS  'tä  frä ml  mrOt! . .  a%a  ratus  aiäi^^  kaca  fra aidva  vjtva  mraotü  "y.  a.  v.  soll  der  Z. aufsagen  . .  a.  r.  a.  h.  soll  der  wissende Gläubige  (sva.  die  Gemeinde,  s.  Sp.  250  0.) aufsagen"  V.J.  25;  25**,  N.jj*; —  kä^a 'ta  ga'ha  frasravayäilii  *>iaänlF.vacastasta (sd.)  *mahmya  vaca  sardkvstri  mana "'wie  soll  der  Z.  die  G.  vortragen?"  In der  (ersten)  Halbstrophe  (jeweils)  mit mittelstarker  Stimme  im  £<ir-i2^»jVnschen Zeitmass'"  N.j_j; — yat'ta  ahurtm  masdqm yazäiti  *mao^näi  barasmqn  paitiiareii  N. J0;~'ta  g}ui*paityapöis(%A.) paoiryO  */ra- »harsitti.  "/J-iyi; — yezica  *a!fe  ratavd  *ana- iaxta(sd.)*para.iyayanti  °ta  viipf.ratu^toais (sd.)  *ra!%wayeiii  N.  80;  —  'ta  *^anahaxtS parayat  dahistäi  arivacasttmäi  saoknm ralxsaiti  "ein  nichtqualifizirter  Z.  soll  weg- gehen und  das  Z.-Amt  einem  Überlassen, der  .  ."  N.  i¥o;    —    cvaiti    naram    *iaxlö
=== HRN pazir ===
```


## [2026-09-14T00:53:49.097Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86",
 "prompt": "Give the etymology of Persian پذیرفتن (pazir(o)ftan) 'to accept': Middle Persian form, Old Iranian prefix and root, Proto-Iranian reconstruction, cognates."
}
```


### [2026-09-14T00:53:53.910Z] TOOL RESULT

```
# Etymology of Persian پذیرفتن (paziróftan)

**Middle Persian Form:**
The word derives from Middle Persian padīriftan, with the prefix and root elements *padīr-*.

**Old Iranian Components:**
According to the source, this comes from a Proto-Iranian compound combining *pati-* (a prefix) with *grab-* meaning "to grab."

**Proto-Iranian Reconstruction:**
The root *grab-* traces back to Proto-Indo-European *gʰrebʰ-*, which had the sense of seizing or grasping.

**Cognates:**
Related forms appear across Indo-European languages, including Sanskrit gṛhṇāti and gṛbhṇāti (both meaning "he seizes") and Proto-Germanic *grab- (ancestor of English "grab").

This etymological path demonstrates how the concept of "accepting" developed from the more concrete meaning of physical seizure or grasping in ancient language roots.
```


## [2026-09-14T00:54:05.079Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN iruftan ===\"; grep -n \"iruftan\\|Iruftan\\|ruftan\" HRN.txt | head -10; echo \"=== HRN peiker ===\"; grep -n -i \"peiker\\|peikSr\\|pa/kar\\|paikSr\" HRN.txt | head -10; echo \"=== HRN patyare ===\"; grep -n -i \"petyare\\|patyare\\|petyär\" HRN.txt | head"
}
```


### [2026-09-14T00:54:05.155Z] TOOL RESULT

```
=== HRN iruftan ===
=== HRN peiker ===
3398:361. peiker *Bild'.
13242:peiker 361.
=== HRN patyare ===
138:wie bade/räh (No. 154), pädOs (No. 265»»*«), petyare (No. 284),
1995:np. but in dieselbe Kategorie wie gStl^ ätes, petyäre
2791:284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
```


## [2026-09-14T00:54:07.265Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1",
 "prompt": "Etymology of Persian پیکر (peykar) 'figure, image, body': Middle Persian form, Old Persian patikara-, elements pati + kar, and any cognates (Sogdian, Armenian)."
}
```


### [2026-09-14T00:54:11.885Z] TOOL RESULT

```
# پیکر (Peykar) - Etymology and Meanings

Based on the Wiktionary entry, **پیکر** is a Persian word with several meanings:

## Primary Definitions
The term translates to:
- Face, countenance
- Form, figure, model
- Portrait, likeness
- Body
- Idol-temple

## Etymology
The word traces back through ancient languages. According to the source, it derives from "Middle Persian form, Old Persian patikara-, elements pati + kar" and is connected to Proto-Iranian origins. The etymology shows connections to Armenian **պատկեր** (patker), which borrowed the term from Iranian languages.

## Linguistic Presence
**پیکر** appears across multiple modern languages including Persian, Chagatai, Kurdish, Turkish, and Russian, indicating its historical linguistic influence throughout the region.

The word's journey from Old Persian through Middle Persian to modern Persian demonstrates how vocabulary persists and spreads across language families over centuries.
```


## [2026-09-14T00:54:14.085Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 361 ===\"; sed -n '3390,3410p' HRN.txt; echo \"=== HRN 284 ===\"; sed -n '2785,2800p' HRN.txt"
}
```


### [2026-09-14T00:54:14.139Z] TOOL RESULT

```
=== HRN 361 ===
de Lagarde, Ges. Abh. 74; Nöldeke, Tabari-
Übers. 448, Note 2, vergl. auch Denkschr. WAW.
Band 38, 14.
360. peikär, peigär *Kampf'.
aw. *paitikära' vergl. paiti.akerenaot (vd. 2, 6);
phlv. patkär 'Kampf (z. B. vd. 5 (33) GL), patkäritan
'Köcher, (z. B. vd. 4 (137)), patkärok (AV.).
arm. LW. payUar *Kampf' .
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
=== HRN 284 ===
283. päyi;^ 'Herbst*.
phlv. pätej^ päz. pädez 'Herbst'.
oss. fäzzäg 'Herbst' (269) (?); sar. pij 'Herbst'.
Fr. Müller nimmt (WZKM. 5, 261) als Grund-
form ein ap. '^patidaiza-y aw. ^paitidaeza- 'Anhäufung,
Sammlung, Emdte' an.
284. petyäre 'Unglück' etc. (Vis und Rämin, Seite 81,
Vers 5 v. u.).
aw. paitt/ara- 'Gegenschöpfung'; phlv. patyardk,
püyärak (Men., K 43).
285. pulten 'kochen, Praes. pez-em^ pezamden,
g. pa/tmün, P<^yß (= np. ptixt^) ; Käs. patSn, pa^te-
man; mäz. pa/ta,
aw. skr. [/^pac- 'kochen' ; phlv. pu^tan^ pazem, pazBt
(PPGl.), pazämlnUan (Bund., Men.).
kurd. patin 'kochen', bepiz; afy. pa/avul; oss. d. ficun^
```


## [2026-09-14T00:54:28.938Z] TOOL CALL #39: Bash

```json
{
 "command": "ls site/pages/397.jpg 2>/dev/null; pdftoppm -f 397 -l 397 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg397 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg397.png"
}
```


### [2026-09-14T00:54:30.896Z] TOOL RESULT

```
site/pages/397.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 72433 Sep 13 20:54 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg397.png
```


## [2026-09-14T00:54:33.270Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg397.png"
}
```


### [2026-09-14T00:54:33.831Z] TOOL RESULT

```

```


## [2026-09-14T00:54:33.824Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:54:55.605Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD leaf ===\"; awk 'NR<=25966 && /\\[pdf page [0-9]+\\]/{m=$0} END{print m}' SOD_pages.txt; echo \"=== KNT patikara page ===\"; awk 'BEGIN{RS=\"\\f\"} /patikara- sb/{print \"leaf(1-based)=\"NR}' KNT.txt"
}
```


### [2026-09-14T00:54:56.710Z] TOOL RESULT

```
=== SOD leaf ===

=== KNT patikara page ===
leaf(1-based)=219
```


## [2026-09-14T00:54:57.057Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF 107 ===\"; grep -n \"\\[pdf page 10[5-9]\\]\\|\\[pdf page 11[0-5]\\]\" FSF_pages.txt | head; echo \"=== FSF patyare ===\"; grep -n \"پتیاره\\|پذیره\\|پیکر\" FSF_pages.txt | head -10"
}
```


### [2026-09-14T00:54:57.186Z] TOOL RESULT

```
=== FSF 107 ===
=== FSF patyare ===
1777:                                            ‫‪- ۲‬دشمن را پذیره شدن برای نبرد به‬
2210:‫یکی گرزۀ گاو پیکر به دست‬                                             ‫شایستث زیبندی سزاوار برای‪:‬‬
3892: ‫یکی گرگ پیکر درفشی به دست‪.‬‬                     ‫به مه بر سر وه بیج برشتنگ سخت‬
4904: ‫به کرسی زر پیکرش برنشاند‬                       ‫سخن از بلندی و پستی در ميان است نه‬
5041:‫که هنوز بوی شیر می‌دهند شگفت است‬                                ‫بساطی بیفکند پیکر به زر‬
5578:        ‫گهر بافته پیکر و بوم زر‬
5621:                                                     ‫همه گوهرش پیکر و‬
6283:                                              ‫=اسخ؛ پتیاره [] = پت ی‬
6723:‫پتیاره در دو بیت شاهد زیر از شاهنامه‬                  ‫تو پایی همی این همه کشورا‬
6728: ‫پتیاره‬                                    ‫‪۱۳۲‬‬
```


## [2026-09-14T00:55:09.544Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==219' KNT.txt | head -c 2500"
}
```


### [2026-09-14T00:55:10.430Z] TOOL RESULT

```
with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam
```


## [2026-09-14T00:55:21.721Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | head -3; echo ---; awk 'NR<=25966 && /page/{m=NR\": \"$0} END{print m}' SOD_pages.txt | head -c 300"
}
```


### [2026-09-14T00:55:23.341Z] TOOL RESULT

```
---
3736:    Sredneiranskije Jazyki. Eds. V. I. Abaev; V. I.                 additional pages dated spring thru July 1969.)
```


## [2026-09-14T00:55:23.375Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/proti",
 "prompt": "What does this page say: the reconstruction *proti / *preti, its meaning, its relation to the root *per-, and descendants in Indo-Iranian (Sanskrit prati, Avestan paiti, Old Persian patiy) and Greek/Latin?"
}
```


### [2026-09-14T00:55:24.629Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:55:29.925Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=25966{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line:\",n}' SOD_pages.txt"
}
```


### [2026-09-14T00:55:30.944Z] TOOL RESULT

```
formfeeds before line: 377
```


## [2026-09-14T00:55:31.610Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/pati",
 "prompt": "Etymology and meaning of Proto-Iranian *pati: what PIE form is it from, descendants (Avestan paiti, Old Persian patiy, Middle Persian pad/pād, Persian pā(d)-)?"
}
```


### [2026-09-14T00:55:32.651Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:55:37.117Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Wiktionary Proto-Indo-European *proti \"against\" Avestan paiti Old Persian patiy reconstruction"
}
```


### [2026-09-14T00:55:41.858Z] TOOL RESULT

```
Web search results for query: "Wiktionary Proto-Indo-European *proti "against" Avestan paiti Old Persian patiy reconstruction"

Links: [{"title":"Reconstruction:Proto-Indo-Iranian/Áryas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%81ryas"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Wiktionary:Requested entries (Proto-Indo-European) - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Wiktionary:Requested_entries_(Proto-Indo-European)"},{"title":"Proto-Indo-Iranian religion","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_religion"},{"title":"Proto-Indo-European desiderative","url":"https://en.wikipedia.org/wiki/Proto-Indo-European_desiderative"},{"title":"Introduction to Old Iranian - The Linguistics Research Center","url":"https://lrc.la.utexas.edu/eieol/aveol/0"}]

The search results don't contain specific information about the Proto-Indo-European root *proti "against" or its Avestan (paiti) and Old Persian (patiy) cognates. The results provide general information about Avestan and Old Persian languages but don't include the specific etymological reconstruction you're looking for.

To find this information, you might want to:
1. Search directly on Wiktionary for the Proto-Indo-European *proti entry
2. Look for etymological dictionaries specializing in Proto-Indo-European reconstructions
3. Search for specific linguistic works on Proto-Indo-European prepositions and their cognates

Would you like me to perform a different search with adjusted terms to find this specific reconstruction?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T00:55:52.096Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v1_pages.txt | sed -n '1,3p'; echo \"=== پتیاره ===\"; grep -n \"پتیاره\" BQT_v1_pages.txt | head -5; echo \"=== پذیره ===\"; grep -n \"پذیره\" BQT_v1_pages.txt | head -5; echo \"=== پادزهر ===\"; grep -n \"پادزهر\\|پازهر\" BQT_v1_pages.txt | head -5"
}
```


### [2026-09-14T00:55:52.189Z] TOOL RESULT

```
=== پتیاره ===
24031:وپارسی باستان(جنبیدن ورفتن) بنابراین پتیاره و پتیارك (پهلوی) لغة بمعنی جند رونده و برخلاف
=== پذیره ===
=== پادزهر ===
1993:پار با؛ پازهر . ابوالعانی :
1997:پاژیر » پازهر . میر نظمی : _ ۱
29904:تریاق فارسی » پازهر را کون .
29911:پازهر را گوبند وممرب آن ترباقاست سوافیونرا
```


## [2026-09-14T00:55:57.178Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24015,24040p' BQT_v1_pages.txt; echo \"=== leaf ===\"; awk 'NR<=24031{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt; grep -c \"\" BQT_v1_pages.txt"
}
```


### [2026-09-14T00:55:58.069Z] TOOL RESULT

```
بافتهٌ ابرمشمی منقش کار هندوستانرا گونند.
چیاده 4 بایلی حطی بروزن همواره.
بمعنيآفت وبلا وزشت» ومهیب ونازبا باشد ٩‏
وشرهندکی رایز گویند وبمعنی شدت‌وسختی
هم‌آمده | هه مکر وحیله وفرب و دغارا
یز گفته اند -- و آ شوب و شور و غوغا را حم
۳۹
لشبر ه- بر وزن کنیره » هر چیز که
مکروه طبیمت باشد ٩٩‏ .
ب مننهی -
۱ ء ازیت بمعنی وی (< ۴
که چنن خوانده "یسنی. باريك بیزه « لت نامه > .
* لت نامه » . - امروزه 0654 گوند. ۵ - رك: هرگو . ۱ رك :دوازو لغت نامه.
۲ - نز ینواز » در پهلوی 084۷2626 از اوستا )081 + ۷۷36 (کفتن) بمعتی جواب
آمده. درپهلوی تورفان080۷732 «اونوالا +مو» .۰۱۲‏ ۸ - پپلوی0۵0۷47۵1. 0102727۵
از اوستا 09109272 (ضد آفرنش) * اسشق ۰۲۸4 مشتقاز ۳91 ( ضد) + ۵۲ ارستابی
وپارسی باستان(جنبیدن ورفتن) بنابراین پتیاره و پتیارك (پهلوی) لغة بمعنی جند رونده و برخلاف
رفتار کننده ۶ فاب ۱ : ۲۸۹ ح » . شهرسنانی گوید : «ومما اخبی به زرادشت فی کاب « زند
وستا» قال: سبظهر فیآخرالزمان رجل اسمه اشبدزیکا (هوشبدر) ومعناه «الرجل العالم » زین -
المالم بالدین والمدل شم بظهرفی زمانه «بتیاره» فیوفم ال فة فی‌امره و هلکه عشرین سنة » « ملل
7 رتنص ۱۸۲*.
_ جهانی برآن جنگ نظارء بود
که آن اژدها طرفه پتباره بود ۰ فردوسی
طوصیاشت ۱ص ۱۳ »
۰ رك : پتباره .
( بر هان اطع )» بفتح اول و سکون ثانی » بممنی
=== leaf ===
592
32486
```


## [2026-09-14T00:56:12.677Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'END{}{n+=gsub(/\\f/,\"\")} END{print \"total ff:\",n}' BQT_v1_pages.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False)[900:2200])\""
}
```


### [2026-09-14T00:56:13.842Z] TOOL RESULT

```
total ff: 776
om/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages
```


## [2026-09-14T00:56:27.371Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for پادزهر — especially any bracketed origin tag (e.g. [په.]) or Pahlavi/Avestan form, and the definition. Also quote the لغت‌نامه دهخدا etymology note if present."
}
```


### [2026-09-14T00:56:33.191Z] TOOL RESULT

```
# پادزهر (Antidote)

## Farhang-e Mo'in Entry

According to the فرهنگ معین dictionary:

> "(زَ) (اِمر.) نوشدارو، هر دارویی که برای دفع سمّ به کار می رود."

This identifies پادزهر as any medication used to counteract poison.

## Etymology (Dehkhoda Dictionary)

The لغت‌نامه دهخدا provides the etymological foundation:

> "( از: پات پهلوی ، ضد. مقابل + زهر، سم )"

The word combines the Pahlavi element *pāt* (meaning "counter/against") with *zahr* (meaning "poison/venom"), literally signifying "poison-antidote."

## Related Terms

Synonyms include: پاد، پازهر، تریاک، تریاق (theriac)

The term entered European languages as "bezoar," originally referring to stones believed to possess antitoxic properties.
```


## [2026-09-14T00:56:44.406Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW premo ===\"; grep -n -o \"premo.\\{0,600\\}\" LEW_1910.txt | head -3; echo \"=== LAT premo ===\"; grep -n -o \"premo.\\{0,400\\}\" LAT.txt | head -3"
}
```


## [2026-09-14T00:56:45.246Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/print",
 "prompt": "Etymology of 'print' (noun and verb): Old French preinte/preindre, Latin premere, dates."
}
```


### [2026-09-14T00:56:45.430Z] TOOL RESULT

```
=== LEW premo ===
=== LAT premo ===
17703:premo et sous somnus. Pour expriner la notion de "dornir",
26937:premo en face de pressus) de la
32748:premo eius die Maximus
```


### [2026-09-14T00:56:51.372Z] TOOL RESULT

```
# Etymology of "Print"

## Noun (c. 1300)
The word originated from Old French *preinte*, derived from *preindre* "to press, crush," which traces back to Latin *premere* "to press, hold fast, cover, crowd, compress." The term initially meant "impression, mark made by impression upon a surface."

The meaning evolved significantly over time: "printed publication" appeared by the 1560s, "printed lettering" by the 1620s, and "picture or design from a block or plate" by the 1660s.

## Verb (mid-14c.)
The verb *prenten* emerged in the mid-14th century with the sense of "make an impression, press upon or into." By the 1510s, it acquired the meaning "run off on a press, make a copy or copies by impression."

## Key Semantic Development
The word's journey reflects technological and cultural shifts—from simple impression-making through printing presses to photography (1851 for the verb, 1853 for the noun) and even fingerprint recording (1952).

Interestingly, the original Old French term also entered Middle Dutch and other Germanic languages, demonstrating its widespread adoption across medieval Europe.
```


## [2026-09-14T00:56:58.547Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26930,26945p' LAT.txt; echo \"=== KLN page markers near bezoar ===\"; sed -n '4860,4885p' KLN_1966.txt | grep -n -o \"^.\\{0,80\\}\" | head -30"
}
```


### [2026-09-14T00:56:59.694Z] TOOL RESULT

```
patriae) Diu.3,4 ]-,80 [ IuppiterJ puer lactens fortunae in gremio sedens,
mammam appetens. - Atteste depuis Enn.; usuel. - les dial. italiens
a^ridionaux ont conservi gremia au sens de "gerbe", M.l.3860; d'autres
dialectes ont gremium "giron", M.I.38O1.
On rapproche lit. granatas "asseabl^e, tas" (si le aot n 1 est pas
emprunt 4 au slave), et sl. gromada "tas"; skr. granah "groupe d'hoaaes,
village"; peut-etre v. isl. kremia "presser", v.h.a .krimman "courber,
tordre". Forae elargie en -en- {cf. premo en face de pressus) de la
racine *ger~, de gr.it/YE0pto "j 1 asseable", etc., qui figure aussi dans
lat. grex.gressus
5°4
gressus: v. gradus, gradior.
grex, gregis m.(f£n. dans Lucii, et Lucr.): d^signe une r^union
d'aninaux ou d'individua de meme eapoce, le troupeau en tant que
betail se disant pecus ; cf. Cic., Phil.3,13,31, greges armentorum re¬
liquique pecoris. En particulier "troupe de con^diens, conpagnie".
=== KLN page markers near bezoar ===
1:betwixt,  prep,  and  adv.  —  ME.  betwixe,  fr.  OE. betweox,  betweohs,  betw
2:Beulah,  fern.  PN.  —  Heb.  be'iildn,  ‘married  wom¬ an’,  fern.  pp.  of  bd
3:beurre,  n.,  butter.  —  F.,  ‘butter’,  fr.  earlier  burre, fr.  L.  butyrum,
4:beurre,  n.,  any  kind  of  pear  with  soft  flesh.  —  F., pp.  of  beurrer, 
5:bevel,  n.,  inclination  of  a  surface.  —  OF.  "baivel (whence  F.  beveau, 
6:Derivatives:  bevel,  tr.  v.  bevel(l)-ed,  adj.,  be- vel(l)-er,  n.
7:beverage,  n.  —  OF.  bevrage,  bovrage  (F.  breu- vage),  fr.  beivre,  boivr
8:bevue,  n.,  error,  blunder.  —  F.  bevue,  ‘blunder, mistake,  slip’,  fr.  O
9:166
10:169
11:see’,  fr.  L.  videre,  ‘to  see’.  See  vision  and  cp. words  there  referre
12:bevy,  n.,  i)  a  flock  of  birds;  2)  a  company,  esp.  of women.  —  F.  b
13:bewilder,  tr.  v.  —  Formed  fr.  be-  and  wilder. Derivatives:  bewilder-ed,
14:bewitch,  tr,  v.  —  Formed  fr.  be-  and  witch. Derivatives:  bewitch-ed,  a
15:bewray,  tr.  v.,  to  reveal,  divulge  ( archaic )  — ME.  bewreien,  bewreyen
16:bezant,  n.,  a  gold  coin.  —  Orig.  ‘coin  of  Byzan¬ tium’,  fr.  OF.  besa
17:bezel,  n.,  a  sloping  edge.  —  OF.  bezel  (F.  biseau ), ‘a  sloping  edge,
18:bezesteen,  n.,  a  bazaar.  —  Pers.  bezestan,  formed fr.  bez  (whence  Arab
19:bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  fou
20:I
21:Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘count
22:bezonian,  n.,  knave,  rascal.  —  Formed  with  suff. -ian,  fr.  It.  bisogno
23:bezzle,  tr.  v.,  to  plunder,  consume;  intr.  v.,  to revel  (dial.  English
24:bezzo,  n.,  name  of  a  small  Venetian  silver  coin.  — It.,  fr.  G.  Batz,
25:Bhaga,  n.,  a  god  of  wealth  (Vedic  mythol.)  — OI.  Bhagah,  lit.  ‘allott
26:Bhagavad-Gita,  the  celebrated  dialogue  between Krishna  and  Arjuna  inserte
```


## [2026-09-14T00:57:14.881Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n -o \"preti.\\{0,200\\}\" WLD_Bd2_1927_dli_106624_djvu.txt | head -5; echo \"=== per- schlagen ===\"; grep -n -o \"per-.\\{0,120\\}schlagen.\\{0,200\\}\" WLD_Bd2_1927_dli_106624_djvu.txt | head -5"
}
```


## [2026-09-14T00:57:15.952Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"premo.\\{0,300\\}\" IEC.txt | head -5; echo \"=== IEC preti ===\"; grep -n -o \"\\bpreti.\\{0,200\\}\" IEC.txt | head -5"
}
```


### [2026-09-14T00:57:18.467Z] TOOL RESULT

```
2504:pretij proti „gegeniiber, entgegen, gegen“, z. T. im Sinne des Entgelts: 
2525:pretiba „Gegen- 
2527:pretium „Wert, Preis einer Sache“ (Keutr. 
5749:pretig- 
5753:pretith-) .,8pruhen‘\ — Da6 ai. 
=== per- schlagen ===
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,200}
 exceeds complexity limits___/
```


### [2026-09-14T00:57:19.566Z] TOOL RESULT

```
=== IEC preti ===
12772:pretium ‘price’ and Pol. preciw, prp. ‘against. Cf. also R poperëk ‘across’; Ukr. v-po-perek *athwart")
13473:preti- (pretiom, ia) “against, opposed to, compared to; comparison, equivalent Cf. proti. WP II, 38 Skt. (ambig.) práti, prp. (against, fr. *preti or *proti: Hom. proti, id.); Tokh. cf. pratim, B pratin, s
13473:pretium, n. ‘price,
13483:pretis, m. “in- termediary'; Old Germanic in LLat. fredus, fritus, s. *peanalty'; Pol. przeciw, prp. ‘against’; Latvian pret, preti, pretim, prp. “against, oppo- site to'
```


## [2026-09-14T00:57:27.014Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"\\*GRAB.\\{0,400\\}\" CHEUNG.txt | head -3; echo \"=== padir ===\"; grep -n -o \"padīr.\\{0,200\\}\" CHEUNG.txt | head -5"
}
```


## [2026-09-14T00:57:27.841Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n -o \"premo.\\{0,250\\}\" WLD_Bd2_1927_dli_106624_djvu.txt | head -4"
}
```


### [2026-09-14T00:57:28.130Z] TOOL RESULT

```
=== padir ===
```


### [2026-09-14T00:57:29.054Z] TOOL RESULT

```
2786:premo), naporh ,.StoS'\ poln. poprzec ,,schieben'‘, wruss. po- 
2842:premo, pressi, pressum „drucken", prelnm 
2861:premo gewertet werden (s. auch
```


## [2026-09-14T00:57:31.580Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '2820,2870p' WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T00:57:31.629Z] TOOL RESULT

```
thronende Donnergott'' zu perq^o- „Eiche“, s. dagegen Wiedemann und 
Liden aaO.). Sollte ai. parjdnya-li „der Regen- und Gewittergott" dei 
gleichen Anschauung „Donnergott" entspringen, miiBte die Form der Wz.- 
variante perg- zugeteilt werden (nicht Erweichung aus "^parcanya- nach 
Grafimann, Zimmer, J. Schmidt KZ, 25, 77, L. v. Schroder IP. 31, I92f.), 
doch steht auch Yer wand tsch aft mit ir. arg „Tropfen“, cymr. eira „Schnee" 
zur Erwagung (Pick II^ 18; s. sper-g-), 

perg-: arm, „schlage, priigle, zerhaue (Holz), falle (Baume), 

erschlage, tote, kampfe"; air. org[a)im „schlage, erschlage, tote; verwiiste, 
beschadige, verletze" (Pormenbestand bei Pedersen KG. 11 587 ff.), inir. orn 
„Morden", Zerstoren" {'^'[p\org-no- od. -rih) braucht nicht nach Liden als por- 
no-, na die kiirzere Wzf. per- widerzuspiegeln), abret. treorgam „perforo'S 
orgiat „caesar“ d. i. „qui caedit, interfector", gall, orge „occide" (CGIL. Y, 
376, 29), gall. Orgeto-rtx MK (Lit. bei Liden). — Abg. pr^gnqti, „bersten% 
poln. pierzgnqc ds., nicht als „zerschlagen werden" hieher, sondern wohl 
zu ai. sphurjati „bricht hervor' usw. (z. B. Persson Beitr. 418. — Hingegen 
reihen sich als „abgeschlagener Stamm, Pflock" die nominalen Sippen 
27erg- und prong- „Stange, Stamm" an, s. d. 

Mit der Bed.-Farbung des russ. prn (s. o.) wohl hieher (Pay KZ. 43, 154, 
s. dazu Hartmann Gl. 4, 378) Idii^premo, pressi, pressum „drucken", prelnm 
j.Presse, Kelter" {^premslom oder eher preslom)\ die hier paradigmatisch 
vereinigten lat. Wzformen und pres- scheinen ein altes Yerhaltnis 

wie gr. : Tpe[c]G> widerzuspiegeln, wenigstens ist es bisher (s. Yf. 

LEWb.2 s. V.) nicht gelungen, eine der beiden lat. Stammformen glaubhaft 
als Umbildung nach irgendwelchen Mustem zu deuten. Ein unsicherer 
Yersuch, prem- und pres- auch im Slav, wiederzufinden, bei Jokl Jagic- 
Festschrift 48 Iff., einerseits abg. (usw.) „Hirse" (sei „Quetschfrucht", 
vgL abg. phsenka „Weizen", russ. pseyio „Hirse" u. '-^pais- ..zerstampfen", 
lat. milium, gr. 2 A£)dvr^ u. mel- „molere"; zu bestimmt widerspricht Bruckner 
KZ. 42, 333); andererseits russ. prjdda „grune Kolbenhirse" (ware "^prem-cl-; 
von Bruckner KZ. 42, 360 f. als ,, Springer" zu ksl. prqdati „springen", russ. 
vosprjanufh „aufspringen" gestellt, nicht einleuchtend), russ. prud „I)aram, 
Teich" (wohl jj'^Sand-, Schotteraufwurf", vgl. :) slov. prod „Schotter", pro- 
dec „Sand“ sabidum : ^/.’a/co: kaum „Sand" als „springend — wirbelnd" 
zu prqdati „springen"). — Mnd. premen „drucken, stopfen", ndl. pramen 
j.driicken", mhd. preme^en ,,zahmen" darf nicht nach Palk-Torp u. brernse II 
als eine idg. Anlautdublette neben lat. premo gewertet werden (s. auch 
u. sper- „drehen"). 



44 


perek (perk-, prek-, pjk-)
```


## [2026-09-14T00:57:32.445Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grab\\b\\|grab-\\|garb\" CHEUNG.txt | head -10"
}
```


### [2026-09-14T00:57:32.495Z] TOOL RESULT

```
3235:‘to grasp, grab’ (Sundermann 1984: 177) 
3321:/(#)sk’aft (sk’avd) ‘to carry, drag (quickly); to grab’, Wa. skaf- ‘to slip, shift to’ || (+ 
3333:*PIE ? *k(e)H»p- ( *kap-) ‘to grab, stick to’? = LIV: 344 f. | Pok.: 527 ff. 
3335:*IE COGNATES: Gr. karnıo ‘I grab; I snap, swallow’, Lat. capio ‘I take’, Goth. hafjan 
8589:*grabH ‘to grab, seize, take’ 
8591:*AVESTAN: grab- (garab-) ‘to grab, seize, take’ || (+ *a-) ‘to grab (to)’ || (+ *uz-) "to 
8608:*OLD PERSIAN: grab- ‘to seize (as possesion), seize (as prisoner)’ — Kent: 183b 
8656:consider, take (for), regard as; to grab’ ( *grbaja-), yfs- (intr./inch.) ‘to be silent, keep 
8680:the trigger’, D. ergzevun/ergavd ‘to hit the target; to grab, seize’, Yghn. yirrw- ‘to 
8690:«PIE *g'rebH;- ‘to grab, seize’. 0 This is the most often cited reconstruction. It is
```


## [2026-09-14T00:57:37.881Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8589,8660p' CHEUNG.txt | grep -n -i \"pati\\|padīr\\|pdyr\\|MIDDLE PERSIAN\\|PARTHIAN\\|SOGDIAN\" | head -20"
}
```


### [2026-09-14T00:57:37.951Z] TOOL RESULT

```
33:*MIDDLE PERSIAN: MMP gyr-, BMP gyl- (OHDWN-) /gir-/ ‘to take, seize’ || (+ 
34:*pati-) MMP pdyr- ‘to take, receive, accept’, BMP ptgyl- (MKBLWN-) /padir-/ ‘to 
38:Partic.: perf. pass. MMP "gryptg, MMP grypt, grypt, gryft, gryft || (+ *pati-) Pres.: IND. 1sg. MMP 
39:pdyr’m, MMP pdyrym, 3sg. MMP pdyryd, BMP ptglyt /padiréd/, 3р1. MMP pdyrynd, MMP pdyrnd, 
40:BMP ptglynd /padirend/, SUBJ. jee MMP pdyr’y, 3sg. MMP pdyr’d, 1р1. MMP pdyr’m, 3pl. MMP 
41:pdyr’nd, IMPV. 2sg. MMP pdyr, 2pl. MMP pdyryd; Partic.: perf. pass. MMP pdyryft, pdyrypt; Inf.: 
42:MMP pdyrptn, BMP ptglptn /padiriftan/ 
44:*PARTHIAN: gyrw- ‘to take, seize’, grysp- (pass./inch.) ‘to be taken, be held’ || (+ 
46:(+ *pati-) pdgyrw- ‘to receive; take’ = Ghilain: 79, 89 | DMMPP: 170a f., 102a, 
52:|| (+ *pati-) Pres.: IND. 35р. “pdgyrwyd, 3р1. pdgyrwynd, SUBJ. 2sg. "pdgyrw, pdgyrw’h, pdgyrw’h, 3sg. 
57:*SOGDIAN: SSogd. (yrB- BSogd. yrf-, CSogd. yrb-, MSogd. yrß- ‘to take, 
59:zyrwDs- (pass./inch.) ‘to be raised (?) || (+ *pati-) SSogd. ptyr(y)B-, BSogd. ptyrB-, 
63:yrBty, etc. || (+ *pati-) Pres.: IND. 3sg. BSogd. ptyrBty, SUBJ. 1sg. pcyrB’n, 3sg. BSogd. ptyrB’t, OPT.
```


## [2026-09-14T00:57:56.334Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%85%D9%BE%D8%B1%D8%B3/",
 "prompt": "Quote the فرهنگ معین and دهخدا entries for کمپرس: is it marked as a French loanword (فر.) and what does it mean? Also any note on پرس."
}
```


### [2026-09-14T00:58:01.731Z] TOOL RESULT

```
# Analysis of کمپرس Entries

**Marked as French Loanword:**
Yes, both entries mark it as French (فر.). The فرهنگ معین explicitly shows: "(کُ پْ رِ ) [ فر. ]"

**Meaning According to فرهنگ معین:**
"تکه پارچة خیسی که روی قسمت زخم شده یا ملتهب بیمار می گذارند" — a piece of wet cloth placed on a patient's wounded or inflamed area.

**Meaning According to دهخدا:**
The entry provides multiple definitions including "پارچه ای آغشته به آب گرم یا سرد که بر روی عضوی از بدن گذارند" — cloth soaked in warm or cold water applied to a body part, particularly for medical purposes.

**Regarding "پرس":**
The term "پرس" does not appear in this dictionary entry. The word shown is "کمپرس" (compress), which derives from the French word "compress."
```


## [2026-09-14T00:58:10.159Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=6723{n+=gsub(/\\f/,\"\")} END{print \"ff:\",n}' FSF_pages.txt; sed -n '6715,6735p' FSF_pages.txt"
}
```


### [2026-09-14T00:58:11.267Z] TOOL RESULT

```
ff: 139
‫اوستایی یعنی «آر» به معنی رفتن است؛ و‬                  ‫سر خویش گیرکوسی رامپای‬
 ‫پائیتی آر رویهمرفته یعنی‪ :‬خلاف رونده‪:‬‬                 ‫(‪)۳-۱۰۴۱-۵۷۱۲‬‬

 ‫منافق‪ .‬دشمن‪ .‬پهلوی پتیارک («بند هش‬                    ‫(معنای «مپای» از مصراع «مکن هیچگونه‬
 ‫یوستی ‪-۸۹‬وست ‪-‬هصوگ )‪۲٩‬‏ «پهلوی‬                                        ‫بهمادر نگاه» روشن است)‬
‫‪“Opposition”-Patyûrak,‬‬     ‫‏‪Le Liver de‬‬                                  ‫(دقیقی ‪:)۶-۷۲۱-۱۹۸‬‬
     ‫‏‪Zoroastre. F. Rosenberg, p. XXI‬‬                             ‫ریگست پیش اندرا‬    ‫زار‬
                                                                                       ‫کبه ک‬
‫پتیاره در دو بیت شاهد زیر از شاهنامه‬                  ‫تو پایی همی این همه کشورا‬
 ‫درست به همان معنای اوستایی و پهلوی‬                                           ‫(اسدی ‪:)۸۸۲-۶۳‬‬
       ‫بکار رفته است‪ .‬منوچهر می‌گوید‪:‬‬                        ‫زبان را بپای از بداندیش و دوست‬
            ‫بجستم ز سلم و ز تور سترگ‬                   ‫که نزدیک‌تر دشمن سرت اوست‬
 ‫همان کین ایرج نیای بزرگ‬                                                       ‫(ناصر ‪:)۰۰۲-۷۱‬‬
 ‫پتیاره‬                                    ‫‪۱۳۲‬‬


                         ‫(ناصر ‪:)۶۸۳-۰۱‬‬                          ‫جهان ویژه کردم ز پتیارها‬
             ‫از عامه خاص هست بسی بدتر‬            ‫بسی شهر کردم بسی بارها‬
 ‫زین صعب‌تر چه باشد پتیاره؟‬                       ‫(‪)۱-۷۴۲-۲۳۶۱‬‬
 ‫(‪:)۷۹۲-۹۲‬‬                                              ‫چنین گفت کان کو چنین باره کرد‬
          ‫دو چشم من چنین پتیاره دیده‬              ‫نه از بسهر پیکار پتیاره کرد‬
```


## [2026-09-14T00:58:18.920Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پذیرفتن\\|پیکر\\|پتیاره\\|پادزهر\" ARY_pages.txt | head -10"
}
```


### [2026-09-14T00:58:18.979Z] TOOL RESULT

```
4283:۸ | پاده پٌد (به چم "مخالف» *ضد* مثلاً در واژه‌ی *پادزهر*)
4318:یونانی (078870): 7 207 فرهنگ معین + ۷ (پادزهر) ۶۴۸
9815:"پادزهر"88102۸77) نیز از واژه‌ی فارسی "پادزهر گرفته شده است (5168۸7 :53-59)
```


## [2026-09-14T00:58:22.909Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '4275,4325p' ARY_pages.txt; echo \"=== 9810 ===\"; sed -n '9805,9820p' ARY_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=4318 && /\\[pdf page/{m=$0} END{print m}' ARY_pages.txt"
}
```


### [2026-09-14T00:58:23.919Z] TOOL RESULT

```
: اسلاری کهن (ع۲1شا5 ل#6تالل) صا0): برهان قاطع : ۳۴۳
۷0۸
اوستایی (4۸897۸7): 3 اقغانی (پشتر) (/4۳0۸(۷): 25۸
پارسی‌باستان (/288514 00): ۳0 تخاری ۸ (۸ ۸(۷ل ۰:07 ]۳8۸ ,88
پپلری (7ماتلمه): 0 ,۳2 ,8۸0 تخاری 8 (2 [(21ت7070): ۰ 2۸۹8۵ ,8۸
اوستی (08557/6): ۳۸2 سانسکریت (54۸/50/7):
کردی (820/5)): 8 ,8۸ ۳ ,8م 2۸0 و 12
[pdf page 147]
۸ | پاده پٌد (به چم "مخالف» *ضد* مثلاً در واژه‌ی *پادزهر*)
ارمنی (47(482714۷): 077 نروژی (۵/07775054/۷): 707
پونانی (076274): 58 ,80115 هلندی (1ع007): ۷07
لانین (7100مل): 85 ,55 اسلاوی کهن (16 مرو 07ات0 طلم):
فرائسه (4ل0/ق73): 0 ی مک ۳
اسپانیایی (8۳۸۸13): ادا لینرانی (۵2ا(هل17 7 ): ‎0٩‏
‏ایتالیایی (۷لشاله7): رانا تونی (لتی) (/7۲14۸): ۳0۸
رومانی (/(۸/۸(۵): 3 ایرلندی کهن (للدل#ز صا0): 3
پرتغالی (۳077012285): 2 آلبانی (4/۷مقلم): ۳07
گونیکه (0077710): 108 هتیت (717717): ۷ ۳۸7۸
آیسلندی کهن (نف 70/۸7 شک طا0).

۱ دا پسگشت‌ها خرس

نورس کهن (۸0۸۵2 0): 078 0 2080820
ساکسونی کهن (540000 010): 137 ,007 8 (۳۵0۵7) تا ما ان
فریزی کهن (51(۷ل۲# صا0): ۴۸07 7 (۳180) بان ۱۰۳ او
آلمانی کهن (0270142 ۲1067 صا0): ,7107 5 (۲007) دام ی
آلمانی ((4۸ل057): ناد 23244 8۸
انگلیسی کهن (تلدلا8(0 صا0): ۳/07 8 (۲007) :05
انگلیسی (5ا.ا6۸/0): 007 0 (۲۵0۵7) +547
دانمارکی (0۸(//54): 00 برهان قاطع + ۱ ۳۳۴
سرئدی (8175015/7): 07

یادداشت.

معنی این واژه در زبان‌های لیترانی و لنونی: جای پا؛ رد پا

معنی این واژه در زبان‌های ایرلندی کهن؛ زیر» تخت. ۳۳( ۷

ام انگلیسی سرواژهی فارجش ی ۱8۷3
اوستایی (۸75374): ۳۸1 پسگشت‌ها 1,335
پارسی پاستان زا( ک/۳8 ان 8۸3 [ 840 موم
پهلری (4۲1ا(۳۸): ۰ ,8 ر8۸7 1 (0(7858)) :ههام25
سانسکریت (54(/58/7): ۳7 2 (۲7110075ه) :۸۷۸5/28
یونانی (078870): 7 207 فرهنگ معین + ۷ (پادزهر) ۶۴۸
لبترانی (/۸2/1۸تا774ار). ۳1 لفت نامه دهخدا : ۵۳۹
[pdf page 148]
پادسپات. (مثلاً در / ۱۳۴۹
اوستایی (4۲897۸/۷): -۳۸171 ۳۸71181 انگلیسی کهن (بل8لا200 ط/0):
پارسی باستان :(۳8781(۷ صراه) (از فرانسه کهن) 006
-۳۸7 ,2۸013817۸۸ انگلیسی (8(/07./54): 20
پهلری(۳۸7541): ۳۸013832۷ , -820 اسلاوی کهن (۲72ما5 ال صاه).
=== 9810 ===

بلو چی (71لع( ال 8۸): 72۸78 :0 ما تذل اماط 778 0۶
افغانی (پشتو) (/70/۸۸): 72۸1 1 (0۷553)
ار نی ((/(8(/5): 2۸71۳ ,2۸37۴ 9 (80150) 0
لهستانی (5/-۳0)(شاید) شا ۷ 2 برهان قاطع + ۱.۷۴

یادداشت,

واژه‌ی انگلیسی 81520۸4 (فرانسه: (81220۸147) پرتغالی:؛ چ8152.0۸؛ اسپانیایی: ۹1224۸18 عربی
[pdf page 332]
"پادزهر"88102۸77) نیز از واژه‌ی فارسی "پادزهر گرفته شده است (5168۸7 :53-59)
اوستایی (ر۸۲2۹: -20۸0۷1 بقلل2 2۷ یونانی (06526): 311۸0
پهلری (1۸7ل(۳۸): ۸۷ ,و71۷۸
اوستی (05355776): 7 ,ما2 پسگشت‌ها 5
کردی ([00-7015: 72۸0 را 1 نا
بلوچی (للتامله8): ال ۱ :۸/۸۲2/215
=== pdf page tag ===
[pdf page 147]
```


## [2026-09-14T00:59:14.833Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"per-4\\?\\. To strike.\\{0,500\\}\" AHD_watkins1985.txt | head -3; echo ===; grep -n -o \"PRESS.\\{0,200\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-14T00:59:15.959Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-14T00:59:18.795Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"To strike\\. Variant\\|per-.\\{0,40\\}To strike.\\{0,400\\}\" AHD_watkins1985.txt | head -3; grep -n -o \"premere.\\{0,300\\}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-09-14T00:59:21.805Z] TOOL RESULT

```
844:per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root fo
844:premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of
```


## [2026-09-14T00:59:26.318Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"per-1\\..\\{0,700\\}\" AHD_watkins1985.txt | head -2"
}
```


### [2026-09-14T00:59:27.501Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:59:29.632Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"proti.\\{0,250\\}\" AHD_watkins1985.txt | head -4"
}
```


### [2026-09-14T00:59:30.770Z] TOOL RESULT

```
839:proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Ful
```


## [2026-09-14T00:59:40.839Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg397.png data/verification/sources/refs/ocr/BOOK/397.png && ls -la data/verification/sources/refs/ocr/BOOK/397.png"
}
```


### [2026-09-14T00:59:40.936Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72433 Sep 13 20:59 data/verification/sources/refs/ocr/BOOK/397.png
```


## [2026-09-14T00:59:46.362Z] TOOL CALL #72: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1\" \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86\" \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1\"; do python3 tools/fetch_source.py \"$u\" --note \"page 397, root Per 3: Persian padzahr/zahr/paziroftan/paykar etymologies\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T00:59:49.191Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/089166b172e71633.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cdc38016c37eaee5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c77d42bed1b12610.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5093977aaf0d949.txt
```


## [2026-09-14T00:59:53.393Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/bezoar\" \"https://www.etymonline.com/word/press\" \"https://www.etymonline.com/word/print\" \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1/\" \"https://abadis.ir/fatofa/%DA%A9%D9%85%D9%BE%D8%B1%D8%B3/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 397, root Per 3: bezoar / press / print chain; Mo'in+Dehkhoda padzahr, kompres\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T00:59:58.266Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6d735b18286ee472.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/612c50562dc2478c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/507c77a5610d13b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/907e5371d9de1b8d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f040a03928897add.txt
```


## [2026-09-14T01:00:00.609Z] TOOL CALL #74: Bash

```json
{
 "command": "sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-14T01:00:00.648Z] TOOL RESULT

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


## [2026-09-14T01:01:14.085Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"press,  n\\..\\{0,300\\}\" KLN_1966.txt | head -2; grep -n -o \"Press,.\\{0,300\\}\" SKT.txt | head -2"
}
```


### [2026-09-14T01:01:15.233Z] TOOL RESULT

```
8510:press,  n.  —  F.  compresse ,  fr,  OF.  compresser. See  compress,  v.
10118:press,  n.  —  ME.  cipres,  cypres,  fr.  OF.  cipres (F.  cypresse),  fr.  Late  L.  cypressus,  fr.  Gk.  xu- 7rapia<jo9,  which  prob.  derives  fr.  Heb.  gipher, name  of  the  tree  of  whose  wood  the  ark  was made  (see  Gen.  6 : 14).  Cp.  gopher  and  see  Hehn- Schrader,  Kulturpflanzen  und  H
```


## [2026-09-14T01:01:15.946Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%B3/",
 "prompt": "Quote the فرهنگ معین entry/entries for پرس: which origin tag(s) does it give (e.g. [فر.] French, [روس.]) and what meanings?"
}
```


### [2026-09-14T01:01:20.599Z] TOOL RESULT

```
# فرهنگ معین Entry for پرس

According to the فرهنگ معین dictionary section, the word پرس has the following origins and meanings:

**Origin tags:**
- **(پَ)** - (اِ.) Persian origin
- **(~.)** **[فر.]** - French origin
- **(پُ)** - (اِمص.) Persian origin
- **(پِ رِ)** **[فر.]** - French origin

**Meanings by origin:**

From Persian: "پرده، حجاب" (curtain, veil) and "پرسیدن، پرسش" (asking, question)

From French: "سهم غذا مخصوص یک نفر" (a designated food portion for one person) and "دستگاه فشار" (a pressure device used in heavy and light industries, a clamp/press)
```


## [2026-09-14T01:01:26.717Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"press,  tr\\. v\\..\\{0,320\\}\\|print,  n\\..\\{0,320\\}\" KLN_1966.txt | head -4; grep -n -o \"Print,.\\{0,250\\}\\|Press ([^)]*)\\..\\{0,250\\}\" SKT.txt | head -3"
}
```


### [2026-09-14T01:01:27.792Z] TOOL RESULT

```
18965:print,  n.  —  ME.  empreynte,  fr.  OF.  empreinte. See  imprint,  v.
26141:print,  n.,  a  separate  reprint  of  an  article.  — Coined  by  Skeat  fr.  off  and  print,  as  loan  trans¬ lation  of  G.  Separatabdruck.
30284:print,  n.  —  ME.  prente,  preinte,  printe,  ‘impres¬ sion  mark’,  fr.  OF.  preinte,  priente,  prop.  fem. pp.  used  as  a  noun,  fr.  priembre,  preindre  (F. preindre),  ‘to  stamp,  impress’,  fr.  L .  premere,  ‘to press’.  See  press,  ‘to  squeeze’, print,  tr.  and  intr.  v.  —  ME.  prenten,  preenten, printen,
30284:print,  n. Derivatives: print-able,  adj., print-ed,  adj., print¬ er,  n.,  print-ing,  n.
```


## [2026-09-14T01:06:57.983Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write397.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\ndata = {\n \"pdf_page\": 397,\n \"book_page\": 367,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Per 3\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"two PIE lemmas: (a) the preposition *proti / *preti 'against, opposite, toward' (a derivative of *per-1 'forward, through'), Pok. per-2 §h, pp. 810-816; (b) *per- 'to strike' with the extensions *prem-/*pres-, Pok. 3. per- 818-819 = Watkins per-5\",\n   \"note\": \"Nourai's 'Per 3: opposite, against, in front of, strike' merges two entries of Pokorny, and his page span POK:815-818 straddles exactly the join: pp. 815-816 are the tail of per-2, whose section h is 'preti, proti \\\"compared with, entgegen, against\\\"' (the source of Skt. prati, Gk. proti/pros, Av. paiti, OP patiy), while p. 818 begins 'per-3, per-g- Meaning: to hit', where Latin premo, pressi, pressum stands. So the Iranian paiti- branch (nodes 1-8) and the Latin premere branch (nodes 9-12) do NOT go back to one root in modern handbooks. The lumping is not arbitrary, however: Watkins's per-1 entry ends 'Other possibly related forms are grouped under per-2, per-3, per-4, per-5', so a connection is left open; and Kent (p. 194) derives OP patiy from pIE *poti while explicitly comparing *proti. 'Related to the Indo-European root Per 1' is therefore right for the first sense, and the gloss 'strike' is right for the second; only the claim that they are one root is over-stated.\",\n   \"note_fa\": \"نورایی زیر یک عنوان «Per 3» دو ریشهٔ جداگانهٔ هندواروپایی آغازین را یکی گرفته است: نخست حرف‌اضافهٔ *proti/*preti «در برابر، ضدِّ» که خود مشتق از ریشهٔ *per-1 «به پیش، از میان» است (پوکورنی، صص ۸۱۰–۸۱۶، بخش h) و در سنسکریت práti، یونانی proti/pros، اوستایی paiti و پارسی باستان patiy بازمانده دارد؛ دوم ریشهٔ *per- «زدن، کوفتن» با گسترش‌های *prem-/*pres- (پوکورنی ۸۱۸–۸۱۹) که لاتینی premere از آن است. ارجاع POK:815-818 درست همین دو صفحه‌گستره را در بر می‌گیرد و نشان می‌دهد که نویسنده آگاهانه دو مدخل پیاپی پوکورنی را یکجا آورده است. واتکینز (AHD) نیز پیوند احتمالی این دو را نفی نمی‌کند، پس ادعای نورایی «با احتیاط پذیرفتنی» است، نه نادرست و نه دقیقاً مطابق مرجع‌های امروزی.\",\n   \"sources\": [\"https://www.etymonline.com/word/press\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:815-818\", \"status\": \"partial\", \"note\": \"POK_full.txt: the entry 'Root / lemma: per-2 ... h. preti, proti \\\"compared with, entgegen, against\\\" ... Old Indic prati (in Iran, through paiti verdrangt) prefix \\\"against, back\\\"' ends 'Page(s): 810-816'; the next relevant lemma is 'Root / lemma: per-3, per-g- Meaning: to hit ... Latin premo, -ere, pressi, pressum \\\"push, press\\\" ... Page(s): 818-819'. Nourai's span thus covers both, but Pokorny keeps them apart.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"per-2 pp. 810-816 (§h preti/proti); per-3 pp. 818-819\", \"stance\": \"partial\", \"note\": \"'h. preti, proti \\\"compared with, entgegen, against\\\"' vs. 'per-3, per-g- Meaning: to hit ... Latin premo' — two separate lemmas.\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II (Walde-Pokorny) s.v. preti/proti and s.v. per- 'schlagen'\", \"stance\": \"partial\", \"note\": \"WLD_Bd2 line 2504 'preti, proti \\\"gegenüber, entgegen, gegen\\\", z. T. im Sinne des Entgelts'; separately, under per-/perg- 'schlagen': 'lat. premo, pressi, pressum \\\"drucken\\\", prelum \\\"Presse, Kelter\\\"'.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, per-1 and per-5\", \"stance\": \"partial\", \"note\": \"per-1: '*proti in Greek pros, against, toward, near, at ... Other possibly related forms are grouped under per-2, per-3, per-4, per-5 [Pok. 2. A. per 810]'; per-5: 'To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus) [Pok. 3. per- 818]'.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann, s.v. *preti-\", \"stance\": \"supports\", \"note\": \"'preti- (pretiom, ia) \\\"against, opposed to, compared to\\\" ... Cf. proti. WP II, 38. Skt. (ambig.) práti ... Hom. proti'.\"},\n     {\"src\": \"KNT\", \"where\": \"p. 194 s.v. patiy\", \"stance\": \"supports\", \"note\": \"'patiy adv., prep., prefix: Av. paiti, Gk. (dial.) poti, pIE *poti, cf. pIE *proti in Skt. prati, Gk. Hom. proti, classical pros'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"paiti-jathra\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The compound itself is unattested: neither Bartholomae's Altiranisches Woerterbuch nor Kent knows an Avestan *paiti-jaθra-; it is the Old Iranian prototype reconstructed backwards from Middle Persian pādzahr. Both halves are sound. Av. paiti / OP patiy 'against, back, toward' is the Iranian form of PIE *proti/*poti (Kent p. 194), and Old Persian had a lengthened by-form *pāti- beside pati- (Huebschmann, Persische Studien §10: 'Dieses pāt (aus ap. *pātiy) liegt noch vor in np. paz. pādzahr \\\"Gegengift\\\"'), which gives MP pāt-/pād-. The second element is *jaθra- 'means of killing, poison' < *gʷhn̥-tro-, root *gʷhen- 'to strike, kill' — Huebschmann no. 679 'Ich führe daher zahr \\\"Gift\\\" ... auf *jaθra- = skr. hatra- \\\"Mittel zum Tödten\\\" zurück', and Watkins s.v. gʷhen-: 'Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR'. So the arrow root -> paiti-jaθra and the cross-reference to Gwhen 2 are both right in substance; the form is a reconstruction, not an attested Avestan word, and should carry an asterisk. Nourai's NOTE is also justified: Klein p. 169 glosses pād 'protecting, guarding' and Watkins files the same pād under *pā- 'to protect' (*pā-ti-), whereas Horn no. 273, Huebschmann p. 36 and Dehkhoda derive it from paiti- 'against'.\",\n     \"derivation_fa\": \"«پادزهر» در اصل ترکیبی ایرانی باستان است، ولی خودِ صورت *paiti-jaθra- در اوستا و پارسی باستان گواهی نشده و بازسازی است؛ نشانهٔ ستاره می‌خواهد. جزء نخست paiti اوستایی / patiy پارسی باستان «در برابر، ضدِّ» است (کنت، ص ۱۹۴) که هوبشمان (بند ۱۰) صورت کشیدهٔ *pāti- آن را در پارسی باستان می‌نهد و همین به فارسی میانهٔ pāt-/pād- و پیشوند «پاد ـ» فارسی نو رسیده است. جزء دوم *jaθra- «ابزار کشتن، زهر» است از ریشهٔ هندواروپایی *gʷhen- «زدن، کشتن» (هوبشمان بند ۶۷۹: zahr از *jaθra- برابر سنسکریت hatra-؛ واتکینز نیز zahr را زیر *gʷhn̥-tro- می‌آورد). یادداشت خود نورایی هم درست است: کلاین «پاد» را «نگهدارنده» گرفته، اما هرن (بند ۲۷۳)، هوبشمان (ص ۳۶) و دهخدا («از: پاتِ پهلوی، ضد، مقابل + زهر») آن را همان paiti «ضد» می‌دانند؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1\", \"https://en.wiktionary.org/wiki/%D8%B2%D9%87%D8%B1\", \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1/\"],\n     \"ref_check\": [\n       {\"ref\": \"AEF:336\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi (the Persian version of Horn/Huebschmann) is not online (refs_online.json: 'Not online (searched archive.org, ketabnak, noorlib, web)'). Its model, Horn no. 273, is checked below and supports the arrow.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"no. 273, p. 62\", \"stance\": \"supports\", \"note\": \"'273. pāzehr \\\"Gegengift, Bezoar\\\". paiti + zehr (s. zehr No. 678).' — exactly Nourai's analysis.\"},\n       {\"src\": \"HUB\", \"where\": \"p. 36 (no. 273) and §10; no. 679\", \"stance\": \"supports\", \"note\": \"p. 36: 'Auf dieses padzahr (das aber \\\"Gegen-gift\\\" bedeutet) sowie auf padsāh \\\"König\\\" stützen die pers. Lex. fälschlich ihr pad \\\"Schützer\\\"'; §10: 'Dieses pāt (aus ap. *pātiy) liegt noch vor in np. paz. pādzahr'; no. 679: zahr < '*jaθra- = skr. hatra- \\\"Mittel zum Tödten\\\"'.\"},\n       {\"src\": \"KLN\", \"where\": \"vol. I p. 169 s.v. bezoar; p. 1141 s.v. padishah\", \"stance\": \"contradicts\", \"note\": \"'ult. fr. Pers. badzahr, padzahr, \\\"counterpoison\\\", lit. \\\"protecting (against) poison\\\", fr. pad, \\\"protecting, guarding; guardian, lord, master\\\"' — Klein takes the first element as 'protect' (and under padishah relates it to OPers. pati 'master', PIE *poti-), not as the preposition 'against'.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pā- (§5) and gʷhen- (§4)\", \"stance\": \"partial\", \"note\": \"'Suffixed form *pā-ti- in Iranian *pāti- in Persian pād, protecting against: BEZOAR' — supports the second element (*gʷhn̥-tro- > zahr) but files pād under *pā- 'protect', like Klein.\"},\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, cols. under paiti-\", \"stance\": \"silent\", \"note\": \"Bartholomae has many paiti- compounds (e.g. paiti.jan- 'sich wehren gegen, bekämpfen', with OP patiy-ajatā, col. ~882) but no entry *jaθra- and no paiti-jaθra-; grep 'ja0ra/jathra' in BRT.txt returns nothing.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"pâdzahr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"MP pādzahr, written p'tzhl, is glossed by MacKenzie (Concise Pahlavi Dictionary p. 63) 'pādzahr [p'tzhl | N pa(d)zahr] bezoar, antidote'; Pāzand has pad(a)zah(a)r (Shikand-gumānīg Wizār 261, cited by Huebschmann p. 36). NP پادزهر pādzahr is the direct continuation, with the by-form پازهر pāzahr/pāzehr (loss of -d- in the cluster -dz-), which is the shape Horn lemmatises (no. 273) and which Ferdowsi uses in the distich quoted on the page ('یکی زهر یابد یکی پای زهر', with the folk-etymological spelling پای‌زهر). Meaning: literally 'counter-poison' > 'antidote', and from the 13th c. onward also the concretion (gastrolith) of the wild goat of Lār credited with antidotal power.\",\n     \"derivation_fa\": \"«پادزهر» دنبالهٔ مستقیم فارسی میانهٔ pādzahr (نوشتهٔ p'tzhl) است که مکنزی آن را «پادزهر، ضدّ سم» معنی کرده و در پازند نیز pad(a)zah(a)r آمده است. در فارسی نو گونهٔ کوتاه‌شدهٔ «پازهر» (با افتادن د در خوشهٔ ـدز) رواج یافت و همین صورت است که هرن (بند ۲۷۳) سرواژه کرده و در بیت فردوسیِ همین صفحه به‌صورت «پای‌زهر» (به ریشه‌شناسی عامیانه) آمده است. معنی تحت‌اللفظی «ضدّ زهر» است و سپس به سنگِ معدهٔ بزِ کوهی لارستان که پادزهر می‌پنداشتند نیز گفته شد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1\", \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AF%D8%B2%D9%87%D8%B1/\"],\n     \"ref_check\": [\n       {\"ref\": \"AEF:334\", \"status\": \"not_checked\", \"note\": \"Asas-e Eshteqaq-e Farsi not available online; its source Horn no. 273 supports (see consulted).\"},\n       {\"ref\": \"MON:648\", \"status\": \"partial\", \"note\": \"The page number is right: Aryanpur's index (ARY_pages.txt, pdf p. 147, s.v. the prefix پاد) cites 'فرهنگ معین (پادزهر) ۶۴۸'. The online text of Mo'in (abadis.ir/fatofa/پادزهر) gives only '(زَ) (اِمر.) نوشدارو، هر دارویی که برای دفع سمّ به کار می‌رود' without the Latin-script etymology of the print edition, so the wording of Mo'in's own note could not be read.\"},\n       {\"ref\": \"FVF:50\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi: only on noorlib/ketabnak behind a JS viewer/login (refs_online.json), not fetchable here.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 63\", \"stance\": \"supports\", \"note\": \"'pādzahr [p'tzhl | N pa(d)zahr] bezoar, antidote' — the spelling p't (not p'y) shows pād- < *pāti-.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 273\", \"stance\": \"supports\", \"note\": \"'pāzehr \\\"Gegengift, Bezoar\\\". paiti + zehr'.\"},\n       {\"src\": \"HUB\", \"where\": \"p. 36 and §10\", \"stance\": \"supports\", \"note\": \"'Die ältere Form pādzahr siehe bei Vullers s. v. pazahr ... paz. pad(a)zah(a)r \\\"Gegengift\\\" Shk. 261'.\"},\n       {\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf p. 147 (s.v. پاد)\", \"stance\": \"supports\", \"note\": \"'پاد (به چم «مخالف»، «ضد» مثلاً در واژه‌ی «پادزهر»)' — Aryanpur, an independent modern Persian cross-check, takes پاد as 'against'.\"},\n       {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. پادزهر; لغت‌نامهٔ دهخدا same page\", \"stance\": \"supports\", \"note\": \"Dehkhoda: '(از: پات پهلوی، ضد، مقابل + زهر، سم)' — i.e. Pahlavi pāt 'against' + zahr, Nourai's analysis verbatim.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"bezoar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The borrowing into Arabic is real but the form given is not the Arabic one. Arabic took the Persian compound as بادِزَهْر bādizahr, commonly shortened to بازَهْر bāzahr (Klein, s.v. bezoar: 'fr. Arab. bādizāhr, often shortened into bāzahr (see Freytag, Lexicon Arabico-Latinum, I, 79a and b)'); the word travels with the Arabic medical corpus (Rhazes, Avicenna, Ibn Zuhr). Lokotsch no. 1605 spells out the rest: 'Hieraus ar. bādizahr, bāzahr und nach magribinischer Aussprache mit Imāla [a > e] bezahr, woraus die Ärzte des MA ... mlat. bezoar machten'. So 'bezoar' is the Maghribi/Latinised shape, not an Arabic headword; the chart should read bāzahr / bādizahr, with bezahr as the Maghribi pronunciation. The printed page (p. 367) really does say 'bezoar' here, so this is the book's shorthand, not an extraction slip.\",\n     \"derivation_fa\": \"عربی این ترکیب فارسی را به‌صورت «بادِزَهر» و کوتاه‌شدهٔ آن «بازَهر» وام گرفت (کلاین به نقل از فرهنگ فرایتاگ، ج۱ ص۷۹) و از راه پزشکی‌نامه‌های عربی (رازی، ابن‌سینا، ابن‌زهر) به اروپا رسید. لوکوچ (شمارهٔ ۱۶۰۵) می‌افزاید که تلفظ مغربی با امالهٔ a>e صورت bezahr را پدید آورد و از همان، لاتینی میانه bezoar ساخته شد. بنابراین آنچه نورایی در خانهٔ «عربی» نوشته (bezoar) صورت لاتینی/مغربی است نه سرواژهٔ عربی؛ صورت درست عربی «بازهر / بادزهر» است. اصلِ وام‌گیری درست است، اما ضبط واژه در این خانه دقیق نیست.\",\n     \"sources\": [\"https://www.etymonline.com/word/bezoar\"],\n     \"ref_check\": [\n       {\"ref\": \"FVF:50\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari's dictionary of Persian words in Arabic is not accessible online (noorlib viewer/ketabnak login).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"vol. I p. 169 s.v. bezoar\", \"stance\": \"supports\", \"note\": \"'F. bezoard, fr. Sp. bezoar (cp. Port. bezuar), fr. Arab. bādizāhr, often shortened into bāzahr ... ult. fr. Pers. badzahr, padzahr'.\"},\n       {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1605\", \"stance\": \"supports\", \"note\": \"'Pers. pädzähr \\\"Gegengift, Bezoar\\\" ... Hieraus ar. bädizahr, bäzahr und nach magribinischer Aussprache mit Imäla [a > e] bezahr, woraus ... mlat. bezoar ... sp. bezaar, sp. pg. kat. bezoar, frz. bezoar, it. bezzoar ... engl. bezoar'.\"},\n       {\"src\": \"DEV\", \"where\": \"Devic p. 68-69 s.v. Bézoard\", \"stance\": \"supports\", \"note\": \"'Esp. bezonr, bezaar, bezar; portug. bezoar. De l'arabe bādizahr ou bāzahr, venant du persan pād-zehr, qui signifie littéralement chasse-poison.'\"},\n       {\"src\": \"DOZ\", \"where\": \"Dozy, Oosterlingen p. 25-26 (s.v. bezoar)\", \"stance\": \"partial\", \"note\": \"Dozy discusses the word and Richardson's rendering 'expeller of poison' ('dat Richardson expeller of poison vertaalt. De bezoar ...'), i.e. the same Persian source, with the meaning debate about pād.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"bezoar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English bezoar is first recorded in the 1540s as 'a stone used as an antidote against poison', from Medieval Latin bezoar (the Latinisation of Maghribi Arabic bezahr), reinforced by Spanish bezaar/bezoar and French bézoard; by the 1570s it denotes the concretion found in the stomach of ruminants (Etymonline; Klein; Skeat: 'Bezoar, a stone. (F. - Port. - Pers.) O.F. bezaar, F. bézoard. - Port. bezaar. - Pers. pād-zahr, bezoar; lit. \\\"poison-expeller\\\"'). The chain Persian > Arabic > Sp./Med.Lat. > Fr./Eng. drawn by Nourai is the standard account; his chart merely skips the Romance stage between 'Arabic' and 'English'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی bezoar نخستین بار در دههٔ ۱۵۴۰ م. به معنی «سنگِ پادزهر» ثبت شده و از لاتینی میانهٔ bezoar (لاتینی‌شدهٔ صورت مغربیِ bezahr) و با پشتیبانی اسپانیایی bezaar و فرانسهٔ bézoard وارد انگلیسی شده است؛ از دههٔ ۱۵۷۰ به سنگِ معدهٔ نشخوارکنندگان هم گفته شد. اسکیت نیز می‌نویسد: «از فارسی pād-zahr، تحت‌اللفظی بیرون‌رانندهٔ زهر». زنجیرهٔ فارسی ← عربی ← اسپانیایی/لاتینی میانه ← فرانسه/انگلیسی همان است که نورایی کشیده، جز آنکه حلقهٔ رومانس را در نمودار نیاورده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/bezoar\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD:1520\", \"status\": \"partial\", \"note\": \"In the American Heritage IE-roots appendix BEZOAR is cited twice, but under other roots than Nourai's Per: under pā- ('Suffixed form *pā-ti- in Iranian *pāti- in Persian pād, protecting against: BEZOAR') and under gʷhen- ('Suffixed zero-grade form *gʷhn̥-tro- in Persian zahr, poison: BEZOAR') — checked in AHD_watkins1985.txt (the 1985 Watkins reprint of the same list; the 1975 New College appendix runs pp. 1505-1550, so p. 1520 falls inside it). The English word and its Persian source are confirmed; the root assignment to 'Per' is not.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"vol. I p. 169\", \"stance\": \"supports\", \"note\": \"'bezoar, n., orig. a term for antidote; later used for concoctions found in the stomach or intestines of certain animals'.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Bezoar\", \"stance\": \"supports\", \"note\": \"'Bezoar, a stone. (F. - Port. - Pers.) O.F. bezaar, F. bézoard. - Port. bezaar. - Pers. pād-zahr, bezoar; lit. \\\"poison-expeller\\\", from its supposed virtue'.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1605 (index: 'Bezoar 1605')\", \"stance\": \"supports\", \"note\": \"gives the whole European spread from mlat. bezoar, incl. 'engl. bezoar'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"paiti-grab, pati-grab; paiti-ar, pati-ara; paity-âra; pati-kara\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four Old Iranian compounds are genuine formations on paiti-/pati- 'against, toward, back'. (1) paiti-grab-/pati-grab-: Av. and OP grab- 'to seize' (Kent p. 183b 'grab- to seize'; Bartholomae s.v. grab- 'greifen'); the prefixed compound is guaranteed for OP by the Parthian town name Patigrabanā- (Kent p. 195: 'from pati- + root grab- + suffix'), and Cheung reconstructs the verb *pati-grabH- for the 'receive, accept' sense. (2) paiti-ar-/pati-ar-: paiti + ar- 'to move, go' — Avestan paitiiaraiti 'goes against, withstands' (Vd. 4.1 'yō naire nəmatəbənte nōit ... paitiiaraiti' of not returning a loan, Bartholomae s.v. nəmah-). (3) paitiiāra- 'counter-movement, counter-creation, adversary' is the noun of the same compound (Horn no. 284 'aw. paitiāra- \\\"Gegenschöpfung\\\"'). (4) pati-kara- 'what is made against (a model), likeness': OP patikara- 'picture, (sculptured) likeness', DNa 41 patikarā didiy 'look at the sculptures', DB 4.71-78, DSn 1 (Kent p. 195 'pati- + kara- to root kar-'; kara- 'made', §143.V) — the cross-reference to Kwer (*kʷer- 'to make') is correct.\",\n     \"derivation_fa\": \"هر چهار ترکیب، ساخت‌های اصیل ایرانی باستان با پیشوند paiti-/pati- «در برابر، به‌سوی، باز» است. ۱) paiti-grab- از ستاک grab- «گرفتن» (کنت ص ۱۸۳؛ بارتولومه ذیل grab-)، که وجود آن در پارسی باستان با نام شهر Patigrabanā در بیستون گواهی می‌شود (کنت ص ۱۹۵: «از pati- + ستاک grab- + پسوند»). ۲) paiti-ar- از ar- «رفتن، جنبیدن»؛ صورت فعلی اوستایی paitiiaraiti «در برابر می‌رود، مقاومت می‌کند» در وندیداد ۴٫۱ آمده است. ۳) paitiiāra- اسمِ همان ترکیب است، «آفرینشِ مقابل، دشمن» (هرن بند ۲۸۴). ۴) pati-kara- در پارسی باستان «پیکره، نگاره» است (کتیبهٔ نقش رستم: patikarā didiy «به پیکره‌ها بنگر») از pati- + kara- «ساخته» از ستاک kar- «کردن»؛ پس ارجاع نورایی به ریشهٔ *kʷer- درست است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86\", \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"FSF:107\", \"status\": \"supports\", \"note\": \"Noushin, Vazhe-namak, s.v. پتیاره: 'اوستایی یعنی «آر» به معنی رفتن است؛ و پائیتی‌آر رویهمرفته یعنی: خلاف رونده: منافق. دشمن. پهلوی پتیارک' (FSF_pages.txt line ~6715). NB the printing scanned here carries this on printed p. 132, not 107 — the scan's edition differs from Nourai's (refs_online.json flags the edition as unidentified).\"},\n       {\"ref\": \"BQT:374\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p. 374 (BQT_v1_pages.txt, 592nd form-feed page; offset ≈ 218 for this scan), footnote 8 to پتیاره: 'پهلوی patyārak, patyārāk از اوستا paitiyāra (ضد آفرینش) ... مشتق از paiti (ضد) + ar اوستایی و پارسی باستان (جنبیدن و رفتن) بنابراین پتیاره و پتیارک (پهلوی) لغةً بمعنی چند رونده و برخلاف رفتار کننده'.\"},\n       {\"ref\": \"KNT:194\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, LEXICON pp. 194-195 (leaf 219 of KNT.txt, the marker 'LEXICON 195' stands inside it): 'patiy adv., prep., prefix ... prior element in nouns patikara-, Patigrabanā-'; 'patikara- sb. \\\"picture, (sculptured) likeness\\\": ... pati- + kara- to root kar-'; 'Patigrabanā- ... from pati- + root grab- + suffix'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"pp. 183b, 194-195\", \"stance\": \"supports\", \"note\": \"see ref_check; also 'Passives: ... pati-kara- \\\"made thereto\\\" = \\\"sculptured figure\\\"' (p. 49, §143.V).\"},\n       {\"src\": \"BRT\", \"where\": \"AiW s.v. grab-, paiti.jan-, and the verb forms paitiiaraiti (Vd. 4.1, N. 69)\", \"stance\": \"supports\", \"note\": \"'j-, g., p. grab- V. \\\"greifen\\\"' with pres. gərəβnā-, girəβa-; and 'yō naire nəmataβənte nōit ... paitiiaraiti' 'wer einem Darleiher das Darlehen nicht wiedergibt' (paiti + ar-).\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *grabH\", \"stance\": \"supports\", \"note\": \"'*grabH \\\"to grab, seize, take\\\" ... AVESTAN: grab- (garab-) ... OLD PERSIAN: grab- \\\"to seize\\\" — Kent: 183b ... PIE *gʰrebH- \\\"to grab, seize\\\"', with '(+ *pati-)' forms listed for MP/Parthian/Sogdian.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.vv. patkar, patirak\", \"stance\": \"supports\", \"note\": \"'patkar ... OP pati-kara-'; index 'paiti-ar-: patirak'.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"padiraftan; patirak; patyârak; patkar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The four Middle Persian words are correctly filiated to the Old Iranian compounds of node 5, but two of the glosses are Nourai's own. padīriftan, pres. padīr- (Book Pahlavi ptgl-ptn', ideogram MKBLWN-tn'; Manichaean MP pdyr-yptn) 'to receive, accept' = *pati-grab-, with the regular Middle Persian change of intervocalic/postvocalic -gr- > -ẟr-/-dr- and the -ft- infinitive from *grb-ta- (MacKenzie p. 63; Cheung s.v. *grabH '(+ *pati-) MMP pdyr- \\\"to take, receive, accept\\\", BMP ptgyl- /padīr-/ ... Inf. MMP pdyrptn, BMP ptglptn /padīriftan/'). patirak [ptylk'] is not a verb and not primarily martial: Nyberg glosses it 'a meeting', used with verbs of motion, 'ō patirak āmatan \\\"to meet\\\"'; the 'fight' word is the separate MP pahikār/patkār 'struggle, battle, dispute' (MacKenzie p. 63; Horn no. 360 peikār). patyārag/petyārag 'adversary, adversity' (MacKenzie) < Av. paitiiāra-. patkar/pahikar [ptkl, Manich. phykr] is 'picture, image' (MacKenzie p. 63; Nyberg 'patkar ... image ... OP pati-kara-; NP paikar'); the chart's gloss 'body, bundle' matches no dictionary — 'body' is the later New Persian sense of پیکر and 'bundle' appears to be Nourai's own addition (the printed page does read 'patkar : body, bundle', so this is the book, not the extraction).\",\n     \"derivation_fa\": \"هر چهار واژهٔ فارسی میانه درست به ترکیب‌های ایرانی باستانِ گرهٔ پیشین بازبسته شده‌اند، ولی دو معنی از آنِ خودِ نورایی است. padīriftan (ستاک حال padīr-) «پذیرفتن، دریافت کردن» از *pati-grab- است؛ چونگ صورت‌های مانوی pdyr- و پهلویِ کتابی ptgl-ptn' را می‌آورد. اما patirak در پهلوی اسم است به معنی «پیشوازْ رفتن، رویارویی» (نیبرگ: ō patirak āmatan «به پیشواز رفتن») و واژهٔ «نبرد» در پهلوی pahikār/patkār است (مکنزی؛ هرن بند ۳۶۰). patyārag «دشمن، آفت» از اوستایی paitiiāra- است، و patkar/pahikar «نگاره، پیکره» (مکنزی؛ نیبرگ: «از pati-kara- پارسی باستان»). معنیِ «تن، بسته» که نورایی برای patkar آورده در هیچ فرهنگ پهلوی نیست — «تن» معنی متأخّرِ «پیکر» در فارسی نو است. پس زنجیرهٔ اشتقاق درست، اما گلاس‌ها نادقیق است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"FSF:107\", \"status\": \"supports\", \"note\": \"Noushin s.v. پتیاره gives 'پهلوی پتیارک' with the Avestan analysis paiti + ar- (quoted at node 5).\"},\n       {\"ref\": \"BQT:374\", \"status\": \"supports\", \"note\": \"Mo'in's footnote to پتیاره: 'پهلوی patyārak, patyārāk از اوستا paitiyāra' (quoted at node 5).\"},\n       {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"cited without a page; the online text of Mo'in (vajehyab/abadis) omits the Latin-script Pahlavi forms of the print edition, so the specific claim could not be located.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 63, 65\", \"stance\": \"partial\", \"note\": \"'padīriftan, padīr- [MKBLWN-tn' ...; ptgl-ptn' | M pdyr-yptn, N paδiruftan] receive, accept'; 'pahikar [ptkl | M phykr, N paykar] picture, image'; 'pahikār [ptk'l | M phyk'r, N paykār] struggle, battle, dispute'; 'petyārag' — i.e. supports the forms but not the glosses 'to fight' for patirak and 'body, bundle' for patkar.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.vv. patkar, patirak\", \"stance\": \"partial\", \"note\": \"'patkar [ptkly, Prth ptkr] image ... OP pati-kara-; MPrs phykr; Arm. lw. patker; Syr. Talm. lw. ptakrā \\\"an idol\\\", Mand. lw. patikrā; NP paikar'; 'patirak [ptylk'] a meeting: ... ō patirak āmatan \\\"to meet\\\"' — 'meeting', not 'fight'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"s.v. *grabH, Middle Persian section\", \"stance\": \"supports\", \"note\": \"'(+ *pati-) MMP pdyr- \\\"to take, receive, accept\\\", BMP ptgyl- (MKBLWN-) /padīr-/ ... Inf.: MMP pdyrptn, BMP ptglptn /padīriftan/'.\"},\n       {\"src\": \"HRN\", \"where\": \"nos. 284, 360, 361\", \"stance\": \"supports\", \"note\": \"'284. petyāre ... phlv. patyārak, pāyārak'; '360. peikār, peigār \\\"Kampf\\\" ... phlv. patkār'; '361. peiker \\\"Bild\\\". ap. patikara- \\\"Bild\\\"; phlv. patkar (Bund.)'.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Persian\",\n     \"words\": \"pazîroftan; pazîreh; patyâreh; paykar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four continue the Pahlavi forms of node 6. پذیرفتن paẕīruftan/pazīroftan < MP padīriftan: MP postvocalic -d- became the early New Persian spirant ẟ, written ذ (and pronounced z since roughly the 12th c.), so pad-īr- > paẕīr-; the present stem پذیر- continues MP padīr- (Wiktionary, with Cheung's MMP pdyr-). پذیره paẕīra < MP padīrag/patirak 'a meeting': in classical Persian 'پذیره شدن' is 'to go out to meet', either to welcome or, as in the Ferdowsi distich quoted on the page ('پذیره شدش دیو را جنگجوی'), to confront in battle — so the chart's gloss 'confront' is one of its two uses. پتیاره/پتیره patyāra < MP patyārag < Av. paitiiāra-; the semantic road runs 'adversary, counter-creation' > 'calamity, monster' > 'hideous, ugly', which is why Borhan-e Qate' defines it 'آفت و بلا و زشت و مهیب' (p. 374). پیکر paykar < MP pahikar/patkar < OP patikara-: the MP cluster -hk-/-tk- yields NP -yk- (cf. paykār < pahikār), giving 'image, statue, figure' and then 'body'.\",\n     \"derivation_fa\": \"هر چهار واژه دنبالهٔ صورت‌های پهلویِ گرهٔ پیشین‌اند. «پذیرفتن» از padīriftan فارسی میانه است؛ دالِ پس از واکه در فارسی نو به ذال (ذِ معجمه) بدل شده و از سدهٔ ششم به بعد «ز» تلفظ شده است، پس pad-īr- > پذیر-. «پذیره» از padīrag/patirak پهلوی «پیشواز» است؛ در فارسی کلاسیک «پذیره شدن» هم «به استقبال رفتن» است و هم «به رویارویی و نبرد رفتن»، چنان‌که در بیت فردوسیِ همین صفحه. «پتیاره» از patyārag پهلوی و آن از paitiiāra- اوستایی است و راه معنایی‌اش «دشمن/آفرینشِ مقابل ← بلا و دیو ← زشت» است؛ برهان قاطع هم آن را «آفت و بلا و زشت و مهیب» معنی کرده است. «پیکر» از pahikar/patkar پهلوی و آن از patikara- پارسی باستان است؛ خوشهٔ ـhk-/-tk در فارسی نو به ـyk بدل شده (چنان‌که پیکار < pahikār). ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%D8%B0%DB%8C%D8%B1%D9%81%D8%AA%D9%86\", \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 374 s.v. پتیاره: 'بمعنی آفت و بلا و زشت و مهیب و ناز[یبا] باشد', with Mo'in's etymological footnote (quoted at node 5).\"},\n       {\"ref\": \"HRN\", \"status\": \"supports\", \"note\": \"Horn nos. 284 (petyāre < aw. paitiāra-), 360 (peikār), 361 ('peiker \\\"Bild\\\". ap. patikara- \\\"Bild\\\"; phlv. patkar; arm. LW. patker').\"},\n       {\"ref\": \"MON\", \"status\": \"not_checked\", \"note\": \"no page cited; Mo'in's print etymologies are not in the online text.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"HRN\", \"where\": \"nos. 284, 361\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n       {\"src\": \"PHD\", \"where\": \"MacKenzie p. 63\", \"stance\": \"supports\", \"note\": \"gives the New Persian outcomes explicitly: 'padīriftan ... | N paδiruftan', 'pahikar ... | N paykar'.\"},\n       {\"src\": \"FSF\", \"where\": \"Vazhe-namak s.v. پتیاره (printed p. 132 of this scan)\", \"stance\": \"supports\", \"note\": \"'پتیاره در دو بیت شاهد زیر از شاهنامه درست به همان معنای اوستایی و پهلوی بکار رفته است' — Noushin documents the Shahnameh usage.\"},\n       {\"src\": \"MON\", \"where\": \"abadis.ir / فرهنگ معین\", \"stance\": \"silent\", \"note\": \"the online Mo'in text for these headwords carries definitions but no etymology, so it neither supports nor contradicts.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Sogdian\",\n     \"words\": \"ptkr`k\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The word is exactly as cited: Gharib no. 7730 'ptkr'k B, S — patkarē ... image', with variants ptk'r', ptk'r'kh, ptq'ry, ptqry and attestations in TSP 6.135, SCE 90, 94, Dhyāna 17 etc.; a derivative ptqrystn 'idol temple' (no. 7741) and ptkryty-šp'sy 'idolatry' (no. 7742) stand beside it. What is wrong is the direction of the arrow: Sogdian is a sister of Middle Persian, not its daughter, so ptkr'k cannot descend from Pahlavi patkar. Gharib herself marks the entry '< OP patikara', i.e. either an inherited Old Iranian *pati-kara-ka- or a loan from Old/Middle Persian chancery usage — the same source as the Parthian ptkr, Armenian patker, Syriac/Talmudic ptakrā and Mandaic patikrā listed by Nyberg. The node should hang from the Old Iranian box (node 5), not from Pahlavi.\",\n     \"derivation_fa\": \"خودِ واژه درست نقل شده است: قریب (شمارهٔ ۷۷۳۰) «ptkr'k = patkarē، نگاره، تصویر» با گونه‌های ptq'ry و ptkr'yk و مشتق‌هایی چون ptqrystn «بتکده». ایراد کار در جهتِ پیکان است: سغدی خواهرِ فارسی میانه است نه دخترِ آن، پس ptkr'k نمی‌تواند از patkar پهلوی گرفته شده باشد. قریب خود در برابر این مدخل نوشته «< OP patikara»، یعنی یا میراثِ مستقیم ایرانی باستان *pati-kara-ka- است یا وام از پارسی (باستان/میانه) در کاربرد دیوانی؛ همان سرچشمه‌ای که ptkr پارتی، պատկեր ارمنی، ptakrā سریانی و patikrā مندایی از آن آمده‌اند. این گره باید از خانهٔ ایرانی باستان (گرهٔ ۵) آویخته می‌شد.\",\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"SOD:311\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry '7730 ptkr'k B, S — patkarē (ptkr'y) © < OP patikara ... image. TSP 6.135; SCE 90, 94; Dhy. 17 etc.'. The page number checks out: the entry stands on the 377th form-feed page of SOD_pages.txt and the scan's printed page = leaf - 66, i.e. printed p. 311 exactly as Nourai cites.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SOD\", \"where\": \"no. 7730 (printed p. 311), with 7741 ptqrystn, 7742 ptkryty-šp'sy\", \"stance\": \"partial\", \"note\": \"supports the Sogdian word and its meaning but marks it '< OP patikara', i.e. not from Pahlavi.\"},\n       {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. patkar\", \"stance\": \"partial\", \"note\": \"'patkar [ptkly, Prth ptkr] image ... OP pati-kara-; MPrs phykr; Arm. lw. patker; Syr. Talm. lw. ptakrā; Mand. lw. patikrā' — lists the other Middle Iranian and borrowed forms as parallel reflexes of the Old Persian word.\"},\n       {\"src\": \"KNT\", \"where\": \"p. 195 s.v. patikara-\", \"stance\": \"supports\", \"note\": \"'patikara- sb. \\\"picture, (sculptured) likeness\\\"' — the Old Persian source Gharib points to.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Latin\",\n     \"words\": \"premere; pressuss\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"premere is right: Latin premō, -ere, pressī, pressum 'to press, hold fast, crowd, compress', from the extended forms *prem-/*pres- of PIE *per- 'to strike' (Pokorny 'per-3, per-g- Meaning: to hit ... Latin premo, -ere, pressi, pressum \\\"push, press\\\", prelum \\\"Presse, Kelter\\\" (*pres-lom)', pp. 818-819; Watkins per-5 '[Pok. 3. per- 818]'). The second word, printed 'pressuss', is not a Latin form: the book means the perfect passive participle pressus, -a, -um (n. pressum), which is the base of the frequentative pressāre and of the noun pressūra 'pressure' — Watkins spells it out, 'Latin premere (past participle pressus)'. I checked the printed page (pdf p. 397 = book p. 367, image saved to data/verification/sources/refs/ocr/BOOK/397.png): the book itself prints 'pressuss : press, pressure', so this is Nourai's misprint, faithfully extracted. Note also that this Latin node belongs to Pokorny's per-3 'to hit', a different lemma from the *proti of nodes 1-8.\",\n     \"derivation_fa\": \"صورت premere درست است: لاتینی premō, -ere, pressī, pressum «فشردن، کوفتن» از گسترش‌های *prem-/*pres- ریشهٔ هندواروپایی *per- «زدن» (پوکورنی، مدخل per-3 صص ۸۱۸–۸۱۹؛ واتکینز per-5). اما واژهٔ دوم که در کتاب «pressuss» چاپ شده صورتی لاتینی نیست؛ مقصود اسم مفعولِ pressus (خنثی pressum) است که پایهٔ pressāre و pressūra «فشار» است. تصویر صفحهٔ چاپی (ص ۳۶۷ کتاب) را دیدم: خودِ کتاب «pressuss» دارد، پس خطای چاپی کتاب است نه خطای خوانشِ اسکن. افزون بر این، این شاخهٔ لاتینی به مدخل per-3 «زدن» پوکورنی تعلق دارد، نه به *proti که شاخهٔ ایرانی از آن است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"pressuss\",\n     \"correct_form\": \"pressus\",\n     \"sources\": [\"https://www.etymonline.com/word/press\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 per-5: 'To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS, PRESSURE, PRINT; APPRESSED, COMPRESS, DEPRESS, EXPRESS, IMPRESS, (IMPRINT), OPPRESS, REPRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.]' — supports premere and gives the correct participle pressus.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"per-3, per-g- pp. 818-819\", \"stance\": \"supports\", \"note\": \"'Latin premo, -ere, pressi, pressum \\\"push, press\\\", prelum \\\"Presse, Kelter\\\" (*pres-lom); root pr-em- (with durativem -em-) and pr-es-'.\"},\n       {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II p. 43-44\", \"stance\": \"supports\", \"note\": \"'lat. premo, pressi, pressum \\\"drucken\\\", prelum \\\"Presse, Kelter\\\" (*premslom oder eher *preslom); die hier paradigmatisch vereinigten lat. Wzformen prem- und pres-'.\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. gremium (cross-reference)\", \"stance\": \"partial\", \"note\": \"'Forme élargie en -en- (cf. premo en face de pressus)' — Ernout-Meillet's own citation form of the participle is pressus.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins per-5\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box standing for the Old/Modern French stage: Latin pressāre (frequentative of premere) > Old French presser 'to squeeze, press upon' and the deverbal noun presse 'crowd, throng; wine or cheese press' (c. 1300 in English), while Latin premere itself gave OF preindre/priembre, whose feminine past participle preinte 'impression' underlies English print (Klein s.v. print). French compresse, compresser continue Latin compressāre/comprimere, and expresser/exprimer Latin exprimere. These are the forms borrowed onward by English (node 12) and, much later, by Persian (node 11).\",\n     \"derivation_fa\": \"این خانه تهی است و تنها حلقهٔ فرانسه را نشان می‌دهد: از لاتینی pressāre (فعل تکراری از premere) فرانسهٔ کهن presser «فشردن» و اسمِ presse «ازدحام؛ دستگاه فشار» پدید آمد، و از خودِ premere صورت preindre فرانسهٔ کهن که اسم مفعول مؤنث آن preinte «نقش، اثر» سرچشمهٔ print انگلیسی است (کلاین). همچنین compresse/compresser از comprimere و exprimer از exprimere لاتینی است. همین صورت‌های فرانسوی‌اند که به انگلیسی (گرهٔ ۱۲) و بسیار دیرتر به فارسی (گرهٔ ۱۱) وام داده شده‌اند. حلقهٔ نموداری درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/press\", \"https://www.etymonline.com/word/print\"],\n     \"ref_check\": [\n       {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the book (refs=None).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.vv. print, compress\", \"stance\": \"supports\", \"note\": \"'print, n. — ME. prente, preinte, printe, \\\"impression mark\\\", fr. OF. preinte, priente, prop. fem. pp. used as a noun, fr. priembre, preindre (F. preindre), \\\"to stamp, impress\\\", fr. L. premere, \\\"to press\\\"'; 'compress, n. — F. compresse, fr. OF. compresser'.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Press\", \"stance\": \"supports\", \"note\": \"Skeat likewise routes English press through Old French presser from Latin pressāre, frequentative of premere.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Persian\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The box has no transliteration, only the Persian script پرس ، کمپرس. Both are 20th-century French loans, not inherited words: پرس (peres) 'press machine' < French presse, and کمپرس (kompres) 'compress, wet dressing' < French compresse. Mo'in tags both as French: 'پرس (پِ رِ) [فر.] دستگاه فشار' (and a second پرس [فر.] 'سهم غذا مخصوص یک نفر', from French portion-usage in restaurants), 'کمپرس (کُ پْ رِ) [فر.] تکه پارچهٔ خیسی که روی قسمت زخم شده یا ملتهب بیمار می‌گذارند'. They entered Persian with European medicine and industry from the late Qajar period, mostly through French technical vocabulary. Note the irony the chart implies but does not state: پرس and پادزهر/پیکر would be relatives only if Nourai's amalgamated root were right.\",\n     \"derivation_fa\": \"در این خانه تنها صورت فارسی «پرس ، کمپرس» آمده است. هر دو وام‌واژهٔ سدهٔ چهاردهم خورشیدی از فرانسه‌اند، نه واژهٔ موروثی: «پرس» از presse فرانسوی «دستگاه فشار» و «کمپرس» از compresse «پارچهٔ خیس که بر زخم نهند». معین هر دو را با برچسب [فر.] آورده است. این واژه‌ها با پزشکی و صنعت اروپایی از اواخر دورهٔ قاجار و بیشتر از راه فرانسه وارد فارسی شده‌اند. ادعای نورایی (وام‌گیری از فرانسه) درست است.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%85%D9%BE%D8%B1%D8%B3/\", \"https://abadis.ir/fatofa/%D9%BE%D8%B1%D8%B3/\"],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in (read via abadis.ir/fatofa): 'کمپرس (کُ پْ رِ) [فر.] تکه پارچهٔ خیسی که روی قسمت زخم شده یا ملتهب بیمار می‌گذارند'; 'پرس (پِ رِ) [فر.] دستگاه فشار' — the tag [فر.] is Mo'in's own mark for a French loan. No page is cited by Nourai; in the print edition such words stand in vol. 4 (foreign words).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.vv. پرس، کمپرس\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for پرس/کمپرس as headwords returns nothing — Aryanpur treats inherited vocabulary, not modern European loans.\"}\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"press, compress, print, express\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are Latin-via-French words on premere. press (n. c. 1300 'crowd, throng'; v. early 14c.) < Old French presse/presser < Latin pressāre, frequentative of premere; the sense 'printing machine' is from the 1530s and 'journalists collectively' from 1921. print (n. c. 1300 'impression, mark') < Old French preinte, fem. pp. of preindre < premere; verb prenten mid-14c. compress (late 14c.) < Old French compresser / Late Latin compressāre, from com- + premere (participle compressus). express (late 14c.) < Latin exprimere 'to press out', ex- + premere. Watkins lists exactly this set under per-5: 'PRESS, PRESSURE, PRINT; ... COMPRESS, DEPRESS, EXPRESS ...'.\",\n     \"derivation_fa\": \"هر چهار واژه از راه فرانسه از لاتینی premere آمده‌اند: press (اسم از حدود ۱۳۰۰ م. «ازدحام»، فعل از اوایل سدهٔ چهاردهم) از فرانسهٔ کهن presse/presser و آن از pressāre لاتینی؛ print از preinte فرانسهٔ کهن (اسم مفعول مؤنث preindre < premere)؛ compress از compresser فرانسهٔ کهن و لاتینی comprimere/compressāre؛ express از exprimere لاتینی «بیرون فشردن». واتکینز نیز همین مجموعه را زیر per-5 آورده است: PRESS, PRESSURE, PRINT; COMPRESS, DEPRESS, EXPRESS. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/press\", \"https://www.etymonline.com/word/print\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins per-5: 'Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS, PRESSURE, PRINT; APPRESSED, COMPRESS, DEPRESS, EXPRESS, IMPRESS, (IMPRINT), OPPRESS, REPRESS, (REPRIMAND), SUPPRESS.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.vv. print, compress\", \"stance\": \"supports\", \"note\": \"'print, n. — ME. prente, preinte, printe ... fr. OF. preinte ... fr. L. premere, \\\"to press\\\"'; 'compress, n. — F. compresse, fr. OF. compresser'.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Press\", \"stance\": \"supports\", \"note\": \"English press from Old French, ultimately Latin premere.\"},\n       {\"src\": \"POK\", \"where\": \"per-3 p. 818\", \"stance\": \"supports\", \"note\": \"the Latin base premo/pressum is Pokorny's own material for this lemma.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-397.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/write397.py && python3 -m json.tool data/verification/page-397.json > /dev/null && echo JSON-OK && python3 tools/verify_check.py 397"
}
```


### [2026-09-14T01:06:59.427Z] TOOL RESULT

```
ok
JSON-OK
nodes verified: 12/12
node verdicts: {'plausible': 4, 'confirmed': 7, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'not_checked': 7, 'partial': 2, 'supports': 11}
books consulted: {'supports': 32, 'contradicts': 1, 'partial': 7, 'silent': 3} | by book: {'KLN': 5, 'HRN': 4, 'PHD': 3, 'MON': 3, 'SKT': 3, 'NYB': 3, 'HUB': 2, 'AHD': 2, 'BRT': 2, 'ARY': 2, 'LKT': 2, 'KNT': 2, 'CHEUNG': 2, 'POK': 2, 'DEV': 1, 'DOZ': 1, 'FSF': 1, 'SOD': 1, 'WLD': 1, 'LAT': 1}
```


## [2026-09-14T01:07:21.285Z] AGENT

Verified PDF page 397 (book p. 367), root **Per 3** — one entry, 12 nodes. Output: `/home/sfmqrb/git/rishe/data/verification/page-397.json`; `verify_check.py 397` → 12/12 nodes, **0 PROBLEM lines**.

Verdicts: root plausible; nodes 7 confirmed, 4 plausible, 1 transcription_suspect. Ref checks: 11 supports, 2 partial, 7 not_checked. 9 web pages archived via fetch_source.py; page image copied to `data/verification/sources/refs/ocr/BOOK/397.png`.

- **transcription_suspect — #9 Latin "pressuss"**: no such Latin form; the participle is *pressus* (n. *pressum*), base of *pressāre/pressūra*. Checked the printed page: the book itself prints "pressuss" → `error_in: book`, extraction faithful.
- **Root (plausible)**: Nourai fuses two Pokorny lemmas — per-2 §h *preti/*proti "against" (pp. 810-816, source of Av. paiti / OP patiy, nodes 1-8) and per-3 "to hit" (pp. 818-819, Latin premo, nodes 9-12). His span POK:815-818 straddles exactly that join. Watkins leaves a link open ("other possibly related forms…"), so defensible but not any modern handbook's picture.
- **#1 (plausible)**: *paiti-jaθra- is unattested — a back-reconstruction from MP pādzahr; both halves check out (Horn 273 "pāzehr: paiti + zehr"; Hübschmann §10 ap. *pāti-; Hübschmann 679 zahr < *jaθra- = Skt. hatra-). His NOTE is right: Klein p.169 and Watkins put pād under *pā- "protect"; Horn/Hübschmann/Dehkhoda under paiti- "against".
- **#3 (plausible)**: the Arabic word is بادزهر/بازهر (bādizahr/bāzahr); "bezoar" is the Maghribi-imāla→Medieval-Latin shape (Lokotsch 1605, Klein, Devic). The book does print "bezoar" in the Arabic box.
- **#6 (plausible)**: forms right, two glosses wrong — MP *patirak* is a noun "a meeting" (Nyberg), not "to fight" (that is pahikār/patkār); *patkar* is "picture, image" (MacKenzie, Nyberg), not "body, bundle" (the book's own gloss).
- **#8 (plausible)**: Gharib no. 7730 ptkr'k confirms the word and Nourai's SOD:311 is the exact printed page, but Gharib marks it "< OP patikara" — Sogdian is a sister of Pahlavi, so the Pahlavi→Sogdian arrow is genealogically wrong.

No extraction errors found: JSON matches the printed page throughout (including "pressuss", "body, bundle", Arabic "bezoar"). Two useful page confirmations: KNT:194 = Kent's *patiy*/*patikara-*/*Patigrabanā-* lexicon page; BQT:374 = Mo'in's footnote deriving پتیاره from paiti + ar-. FSF:107 supports but sits on p. 132 in the scan we have (different printing).
