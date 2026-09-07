# Verification process log — verify-page-388


## [2026-09-07T20:46:26.980Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 388 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-388.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-388.json. Write /home/sfmqrb/git/rishe/data/verification/page-388.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 388` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:46:28.854Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:46:29.566Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:46:29.580Z] TOOL RESULT

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


## [2026-09-07T20:46:30.419Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-388.txt"
}
```


### [2026-09-07T20:46:30.441Z] TOOL RESULT

```
1	=== PDF page 388 (book page 358) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pekw : to cook  (refs POK:798)
4	#1 (parent #0) [Avestan] refs=POK:798; BQT:370; SYN:336; FFD:40 | pax, pač, pačaiti : to cook ; -pâka : a suffix referring to the cook. ; nasu-pâka : corpse burner ☞Nek 1
5	  #2 (parent #1) [Pahlavi] refs=SNS:137; FFD:40 | puxtag : cooked ; paz : cook
6	    #3 (parent #2) [Persian] refs=BQT:370; AEF:195; IEC:920 | poxtan «پختن» : to cook, bake ; bâ, vâ «ـ با ، ـ وا» : suffixes referring to the cook or how something is cooked. | extra: پزیدن ، پز
7	نانوا ، شوربا ، سپیدبا ، سیکبا ، ناربا
8	#4 (parent #0) [Latin] refs=AHD | coquere : to cook, ripen ; bis-coctus : twice cooked bread ☞Dwo
9	  #5 (parent #4) [English] refs=None | cook, cuisine, kiln, kitchen
10	  #6 (parent #4) [French] refs=AHD:135 | bescuit : a thin cracker
11	    #7 (parent #6) [Persian] refs=MON:626 | bîskŭît «بیسکویت» : biscuit
12	    #8 (parent #6) [English] refs=None | biscuit
13	  #9 (parent #4) [Arabic] refs=AHD:65 | al-birqŭq : early ripening (plum)
14	    #10 (parent #9) [English] refs=AHD:65 | apricot
15	#11 (parent #0) [Greek] refs=AHD:1059 | peptein : to cook ; pepôn : a large melon (edible only when ripe)
16	  #12 (parent #11) [French] refs=None | pompon : pumpkin
17	    #13 (parent #12) [English] refs=None | pumpkin
18	
```


## [2026-09-07T20:46:33.807Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-388.json",
 "description": "Read source JSON page 388"
}
```


### [2026-09-07T20:46:33.845Z] TOOL RESULT

```
{
  "pdf_page": 388,
  "book_page": 358,
  "entries": [
    {
      "root": {
        "name": "Pekw",
        "lang": "Indo-European",
        "refs": "POK:798",
        "gloss": "to cook"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:798; BQT:370; SYN:336; FFD:40",
          "words": [
            {"translit": "pax, pač, pačaiti", "gloss": "to cook", "script": null},
            {"translit": "-pâka", "gloss": "a suffix referring to the cook.", "script": null},
            {"translit": "nasu-pâka", "gloss": "corpse burner", "script": null, "see": ["Nek 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:137; FFD:40",
          "words": [
            {"translit": "puxtag", "gloss": "cooked", "script": null},
            {"translit": "paz", "gloss": "cook", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:370; AEF:195; IEC:920",
          "words": [
            {"translit": "poxtan", "gloss": "to cook, bake", "script": "پختن"},
            {"translit": "bâ, vâ", "gloss": "suffixes referring to the cook or how something is cooked.", "script": "ـ با ، ـ وا"}
          ],
          "script_extra": "پزیدن ، پز\nنانوا ، شوربا ، سپیدبا ، سیکبا ، ناربا",
          "note": null,
          "quote": {
            "text": "گر برای شوربایی بر در اینها روی - اوّلت سیکبا دهند از چهره آنگه شوربا",
            "poet": "Khâqânî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "coquere", "gloss": "to cook, ripen", "script": null},
            {"translit": "bis-coctus", "gloss": "twice cooked bread", "script": null, "see": ["Dwo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cook, cuisine, kiln, kitchen", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:135",
          "words": [
            {"translit": "bescuit", "gloss": "a thin cracker", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:626",
          "words": [
            {"translit": "bîskŭît", "gloss": "biscuit", "script": "بیسکویت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "biscuit", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 4,
          "lang": "Arabic",
          "refs": "AHD:65",
          "words": [
            {"translit": "al-birqŭq", "gloss": "early ripening (plum)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD:65",
          "words": [
            {"translit": "apricot", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1059",
          "words": [
            {"translit": "peptein", "gloss": "to cook", "script": null},
            {"translit": "pepôn", "gloss": "a large melon (edible only when ripe)", "script": null}
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
            {"translit": "pompon", "gloss": "pumpkin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "pumpkin", "gloss": null, "script": null}
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


## [2026-09-07T20:46:35.849Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SYN','FFD','SNS','AEF','IEC','AHD','MON','WLD','KLN','HRN','HUB','PHD','NYB','BRT','CHEUNG','ARY','SKT','FSD','WEB','LKT','PLA','FVQ','AFM']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T20:46:37.119Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
```


## [2026-09-07T20:46:43.285Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SYN','FFD','SNS','AEF','IEC','AHD','MON']:\n    print('=====',k)\n    print(json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\""
}
```


## [2026-09-07T20:46:43.908Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-07T20:46:44.699Z] TOOL RESULT

```
===== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
===== BQT
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
===== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
===== FFD
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
===== SNS
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
===== AEF
{
 "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
 "kind": "catalog",
 "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
 "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "none online; proxy via HRN/HUB. || RE-SEARCH 2026-09: still catalogue/purchase only (Open Library record; iketab second-hand; digikala dkp-3058984 for the 2015 ed.). Publisher of the 2015 ed. is مهرافروز."
}
===== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
===== MON
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
```


### [2026-09-07T20:46:44.745Z] TOOL RESULT

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
```


## [2026-09-07T20:47:06.135Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full pekw ===\"; grep -n -i \"lemma: pek\" POK_full.txt | head -20\necho \"=== POK_03 (p798 => leaf ~798-762..766 = 32-36) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=32 && NR<=38 {print \"----LEAF\",NR-1; print substr($0,1,1500)}' POK_03.txt | head -120"
}
```


## [2026-09-07T20:47:07.095Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins pekw ===\"; grep -n \"^pek\" AHD_watkins1985.txt | head; echo; grep -n -A25 \"^pek\\^w-\\|^pekw-\\|^pek·\" AHD_watkins1985.txt | head -60"
}
```


### [2026-09-07T20:47:07.404Z] TOOL RESULT

```
=== POK_full pekw ===
=== POK_03 (p798 => leaf ~798-762..766 = 32-36) ===
----LEAF 31
 hi-faih  ,Betrug'  ist  Nomen  postverbale;
arm.  asr,  Gen.  asu  , Schaf  wolle.  Fließ',  asvei  , wollig'  {^poku-\-r,  mit  a aus  0  in  offener  Anlautsilbe) ;  gr.  tt^xw  (=  lit.  pe§ü),  niv.Tü)  (=  lat.  pectö, ahd.  fehtan),  Ttsr/.rEo)  ,kämme,  schere',  rci-Aog  n.  ,Fließ,  Wolle',  Tiöxog  m.; ,Fließ',  xTfi/g,  Y.Tev6g  ,Kamm'  (aus  schwundst.  *7rx'r£v-;  lat.  pecten)-,
alb.  pile  , Werkzeug  zum  Flachskämmen,  -hecheln'  (*pekla) ;  lat.  pectö, -ere,  pexl  ,kämmen',  pecten,  -inis  ,Kamm',  umbr.  petenata  ,pectinatam'; ahd.  as.  fehtan,  ags.  feohtan  , fechten' ;  ahd.  as.  fahs,  ags.  feax  ,(Haupt)- haar',  aisl. /aa?  ,Mähne'  (*-poJc-s-o-,  vgl.  den  es-St.  ney-og),  aisl.  fcer,  aschwed. fär  ^Schaf^  {^fahaz  =  Ttöyiog),  aschwed.  fcet  (*fahti-)  ,Wolle,  Fließ',  ags. feht  ,Fließ',  ndl.  vacht  f.  , Wolle,  Schur',  ags.  fihl  ,pannus';  lit.  pesü, pesti  ,rupfen,  an  den  Haaren  zausen',   Iter.  pasyti,  susijpeUi  ,sich  raufen'.
Hierher  wohl  ai.  paks-man-  n.  ,Augenwimpern,  Haar',  paks-malä-  ,mit starken  Augenwimpern,  dichthaarig'  av.  pasna-  n.  ,Augenlid',  vgl.  in  nicht so  spezialisierter  Bed.  np.  pasm  ,Wolle'.
WP.  II  16  f.,  WH.  II  269  f.,  270  ff.,  Trautmann  217,  Specht  KZ  68,  205  ff.
798  '
pek^-  ,kochen';  Partiz.  pek^-to-  .gekocht^;  pek'i-ti-  ,das  Kochen',  peicM-^er^^ pok^o-s  ,Koch^ Ai.  pdcati,   av.  pacaiti  ,kocht,   bäckt,   brät'   (=  lat. 
----LEAF 32
  *peHi  , backen'  in  serb.  pecem,  peci  ds.,   " usw. ;    aksl.  pek^   , Hitze',   pot^   ,Schweiß'   (*pokto-),  pestb    ,Ofen',   peStera    I ,Höhle,  Ofen'  usw.;   toch.  AB  päk-  ,zum  Reifen  bringen,  kochen',  Partiz.  ^ Pass.  B  pepakßu]  A  pukäl,  B  pikul  ,Jahr'  (=  ,Reife'). WP.  II  17  f.,  WH.  I  270  f.,  Trautmann  211  f.
I.  pel-,  pelo-,  ple-  ,gießen,  fließen,  aufschütten,  füllen,  einfüllen^;  auch ,schwimmen,  fließen  machen,  fliegen,  flattern'  und  ^schütteln,  schwin- gen, zittern  (machen)';  nominal:  pel  (Gen.  Pei-es)  und  Peii-s  ,Burg' (,aufgeschütteter  Wall');  pl-no-,  ple-no-,  ple-ro-  ,voll',  pl-no-tä ,Fülle',  pl-tö-,  ple-to-  ^gefüllt',  pJ-ti-,  ple-mn  ,das  Füllen';  pelu , Menge',  Pclu-  ,viel'.
A.  Arm.  heium  ,ich  gieße  aus'  (*pel-nu-mi)^  zeium  (*z-heium)  ,lasse strömen',  Pass.  ,fließe  über';
cymr.  llanw  m.  ,Flut',  Verbalnom.  llanw,  llenim  ,Füllen,  Fließen',  mbret. lanoj  lanv  Flut',  corn.  lanwes  , Fülle'  (^pkn-uo-)',
lit.  trans.  pilü,  pilti  ,gießen,  schütten,  aufschütten,  füllen',  intrans. ,fließen',  lett.  piUt  ,tröpfeln',  pile  ,Tropfen',  pilt  ,tröpfeln',  pali  ,Über- schwemmung',  lit.  afhpalas  {*ant-palas)  ,Aufwasser  auf  dem  Eise';  russ. vodo-poh{je),  pol{n)o-vodt>je  »Hochwasser',  kslov.  poh  ,Schöpfgefäß*.
799
ß,  pel  ;Burg^  in  ai.  pör,  Gen.  purds  ,Burg-^  Stadt^,  pura-  n.j  jünger puri-j  i?^^^  ^s.,
----LEAF 33
e'  (ursprüngl.  fiirtXriiiL,  der  Nasal  aus  Tti^iTtQriui)^  Fut. nkrjaü),  Aor.  fcXfjro  , füllte  sich*,  TtXrjd-o)  ,bin  voll,  fülle  mich',  nXrj^og  n., ion.  TtXri&'ög  , Menge',  rcXr^d-vo)  ,bin  oder  werde  voll,  schwelle  an'  (:  lat. plebes),  7tXria(.Lr)  ,Flut',  nXrjGixovrj  ,Anfüllung,  Sättigung',  ftXrjafj.Log  ,leicht füllend,  sättigend*,  TtX^^ia  , Füllung'  Hes.  ( :  lat.  pleminäre  , anfüllen') ;  hom. ftXsLog,  att.  TtXatjg,  ion.  nXsog  ,voll'  (*7rAi;-[i]o-g;  =  arm.  li?),  TtXtjQrjg ,voll',  7iX7]q6ü)  , mache  voll'  (von  *7tX7]Q0-g  =  lat.  plerus,  vgl.  arm.  lir  , Fülle', i-St.);  7tXi^-f.LVQa,  -livQig  f.   ,Flut',  zu  iitqu)  S.  742;
alb.  plot  ,voll'  (*ple-t'Os) ]  auch  pjel  , zeuge,  gebäre'?  intrans.  ,voll  = schwanger  sein'  ?  ?  mit  Formans  -go-  hierher  plok,  plogu  , Haufe'  (*ple'go-  ? vgl.  ahd.  folc  , Haufe,  Kriegshaufe,  Volk',  ags.  folc  , Schar,  Heer,  Volk', aisl.  folk  , Schar,  Volk'  als  *pl-go-  oder  *peld-go-);
lat.  pleö^  -ere  meist  com-pleö,  im-pleö  , fülle',  Partiz.  Pass.  (com) pletus  ] plenus  jVoll',  umbr.  plener  ,plenis' ;  plerus,  -a,  -um  ,zum  größten  Teile', plerusque,  plerlque  ,eine  große  Anzahl,  sehr  viel,  am  meisten';  plebes,  -ei und  -i,  plebs,  -is  »Volksmenge;  die  Masse  des  Volkes  im  Gegensatz  zu den   Adeligen'    (*pledhues),   manipulus  ,eine   Handvoll;    Bündel;   Hanteln
800  I
der  Turner;  Soldatena
----LEAF 34
Superl.  ursprüngl.  *7rAi5[t]wv  >  ^^fW  {*pleisön) :  nlalarog  (^phisto-)^  das durch  Einfluß  von  *nXeXg  ,mehr'  (*pleis  =  air.  lla)  uüd  des  Kompar.  zu fcXetazog  wurde;  aus  einem  idg.  *pleu-es-  , Überfluß,  große  Menge'  wurde sekundär  der  gr.  Kompar.  n.  TtXeov,  wozu  der  achäische  Nom.  PL  TtXieg neugebildet  wurde ;  ebenso  wurde  alat.  plous,  lat.  plus  zum  Kompar.,  und mit  plls-  (alter  Kompar.  *ple-ies-  in  alat.  pleores,  und  *pleis-  im  Superl. pllsimd)  zu  *plois-  kontaminiert,  woraus  lat.  plürimus  , meist'  (alt  ploiriime^ plouruma,  plusima)-  vgl.  Benveniste  Origines  1,  54  f.,  Schwyzer  Gr.  Gr.  1, 537  f.,  E.-M.2  783;
air.  il  ,viel'  (=  got.  filu),  lla  ,plus,  plures'  {*pU-is)\  acymr.  Haus,  ncymr. lliaws  ,multitudo'  (ple-iös-tu-s  oder  -to-) ;
got.  filu  adv.  Neutrum  m.  Gen.  (altes  Subst.)  als  Ersatz  von  gr.  7toX{fg, auch  ,sehr;  um  vieles  (beim  Komp.)',  ähnlich  in  den  andern  germ.  Sprachen: ahd.  as.  filu,  filo,  ags.  fela,  feala,  feola  ,viel,  sehr',  aisl.  figl-  ,viel',  n. ,Menge';  Komp.  Sup.  aisl.  fleiri,  fleistr  ,mehr,  meist'  {*ph-is-,  -isto-,  av. fraeUa-) ;
lit.  pilus  ,im  Überfluß'.
E.  pel-ed-  in  gr.  TtXdöog  n.  »Feuchtigkeit,  Fäulnis',  nXadagög  , feucht', nXaddü),  -äv  ,naß  sein';  ahd. /ec^iVöw,  t\M.  flattern,  ahd.  fledar-müs  »Fleder- maus*; lett.  peldet  ,sc\iw'immQn',  peldeties  ,ha.äeii' ,  peldin�
----LEAF 35
nd*  und  , Ahorn'   sowie westgerm,  *följan   (ahd.  fuolen,    mhd.  füelen,    ags.  fcelan   usw.)   , fühlen' gehören,  auch  mnd.  vlader  , Ahorn',  vladarn  , flattern'.
WP.  II  63 ff.,  WH.  320  f.,  322  f.,  327  f.,  Trautmann  218;  die  Wörter unter  G.  könnten  auch  zu  2.  pel-  gehören;   hierher  auch  pleu-  ,fließen*.
2  a.  pel-f  pelo-  :  plä-  , stoßend  oder  schlagend  in  Bewegung  setzen,  treiben'.
Lat.  pellö  (wohl  aus  '^pel-nö),  -ere,  pepuli,  *pultus  (,vorausgesetzt  von pultäre  , stoßen'),  pulsus  (nach  perculsus :  percello)  , stoßend  oder  schlagend in  Bewegung  setzen,  forttreiben',  pulsus,  -üs  , Schlag',  umbr.  af-peltu .appellitö,  admovetö',  lat.  öpilio  {*oui-pilio)  , Schafhirt'  (,Schaftreiber') Pales  , Hirtengöttin' ;  appellö,  -äre  ,anreden';
air.  ad-ella  (*pel-nä-t)   ,besucht'   (=  lat.  appellat),   di-ella   , weicht   ab' das  Futur,  zu  agid  , treibt'  :  eblaid  (^pi-pläseti)  und  die  brit.  Konjunktive mit  el-  (oben   S.  307);    air.   lae   ,Tag'  (^pläiom),    ursprüngl.   *, Wendung' über  aksl.  popeh  , Asche'  s.  unter  2  b.  pel-;
wohl  auf  einem  c?-Präs.  *pel-d-ö  beruhen:  ahd.  anafalz  m.,  ags.  anßlte n.  ,Ambos',  ags.  feit,  m.,  ahd.  ßlz  m.  ,Filz'  (*,gestampfte  Wollmasse'), Sihä.  falzan  , anfügen,  anlegen',  nhd.  falzen  »zusammenlegen';
eine  spez.  gr.  Bed. -Entwicklung  , anstoßen'  =  ,sich  nähern,  nahe'  wohl in  
----LEAF 36
.. ds.,   apr.  pelwo  f.  und  lett.  pelvas  f.  PL  ds.;    aksl.  plävy  f.  PL  ,fyvqov^^^ klr.  polöva  ds.  usw.;
mit  i2-Formans:  lat.  pollen,  -inis  ,sehr  feines  Mehl,  Staubmehl'  (ZZ  aus  n. Ausgleichung  einer  Flexion  *polen,  *polnes)]  pollenta  f.  , Gerstengraupen*; hierher  auch  apr.  pelanne  f.  , Asche',  lit.  pelenaX  m.  PL,  lett.  pelni  ds., wozu  apr.  pelanno  f.  ,Herd',  lit.  pelene  ,Herd';  3ipr.  pUeynis  , Staubasche*, lit.  pUnys  f.  PL  ,FlockascheS  lett.  plene  , weiße  Asche  auf  Kohlen' ;  s.  S.  805;
ohne  n-Formans,  aber  mit  Redupl.  russ.  pepel,  aksl.  usw.  popeh  ,Asche*, am  ehesten  als  , zerstoßenes,  zermalmtes'  zu  2  a.  pel-  ,pellens,  pultäre'.
WP.  II  60,  WH.  II  331,  388,  Trautmann  212  f.,  225;  wohl  zu  2.  pel ,stoßen*.
3  a.  pel-  , falten* ;  p^l-to-  ,Falte',  duei-plo-  , zweifach*.
a.  plo'  als  2.  Kompositionsglied  in  Adj.  wie  gr.  ä-7tl6g  , einfach*,  ÖL-TtXög, öIttXcc^  ,zweifach'  (vgl.  arm.  hai  ,Ma,V),  lat.  simplus,  duplus,  duplex,  triplus, duplex  ,ein-,  zwei-,  dreifach',  umbr.  dupla  ,duplas',  tuplak  Akk.  Sg.  n. ,duplicem',  tripler  ,triplis' ;  mir.  dlahul  , doppelt'  (* duei-plo-)]  got.  twei-fls , Zweifel',  ahd.  zvifal  .zweifelhaft',  m.  , Zweifel',  wohl  auch  av.  hifra-  n. »Vergleich,  Ähnlichkeit',  im  Gr.  daneben  die  Umbildungen  des  Typus äTtXöog  (zu  nXovg)  und  ion.  diTiXi^aiog',  ferner  mit  alter  ^Ableitg.  
----LEAF 37
 Wampe,  Wamme';  afries.  ^^mewe  ,Haut',  Sigs.  ßlmen  , Häutchen';  hierher mit  ir-Erweit.  germ.  *felh-  , bergen'  in  got.filhan  usw.  »verbergen,  begra- ben', aisl.  fela  »verbergen,  übergeben',  ags.  f Solan  , anhängen,  eintreten* ; "mit  gramm.  Wechsel  got.  fulgins  , verborgen',  aisl.  folgenn  ds. ;  germ. hifelhan  , an  vertrauen,  bergen*  in  ags.  be-feolan,  ahd.  bi-fel(a)han,  mhd. bevelkany  nhd.  befehlen.
Mit  n-Formantien:  gr.  nsXXäg  Akk.  PI.  , Häute*,  neXXo-Q&cpog  ,pellärius', lat.  pelLis  ,Fell*,  ahd.  fei,  -lies,  ags.  feil,  aisl.  fjall  n.  ,Haut',  got.  prütsfill , Aussatz' ;  (lat.  pellinus  ,aus  Fell'  =  ahd.  fillln,  ags.  feilen  ,ledern'); mit  andern  Wurzelstufen  aksl.  pelena,  russ.  pelend  , Windel,  Tuch,  Hülle' (vgl.  ohne  n-Formans  russ.  pekka  ds.)  und  russ.  plend  (für  pUnd),  sloven. plena,  öech.  plena,  plina  ds.,  lit.  pUne,  jplenis  , Häutchen*,  apr.  pleynis , Hirnhaut' ;
lat.  palla  , langes  Obergewand  der  Frauen,  Vorhang',  pallium  , Bettdecke, bes.  ein  weiter  Überwurf  der  Griechen',  vielleicht  aus  *par(u)lä(?),  Lw. aus  gr.  (pccQog  , Mantel*  ?
Mit  t-Formans :  a.!.  pata-  m.  , Stück  Zeug,  Laken,  Gewand',  patdla  n. , Hülle,  Decke,  Schleier,  Membrane',  gr.  rteXtij  ,leichter  Schild';  aksl. 'plathno  , Leinwand'.
Mit  u-Formantien :  gr.  in,i-7TXo\jF^og  ,die  Netzhaut  um  die  Gedärme';  lit. pUvZ  f.  , feine  dünne  Haut',
```


### [2026-09-07T20:47:07.463Z] TOOL RESULT

```
=== AHD watkins pekw ===
```


## [2026-09-07T20:47:14.108Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==32' POK_03.txt | sed -n '1,60p'"
}
```


## [2026-09-07T20:47:14.241Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pek\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-07T20:47:15.422Z] TOOL RESULT

```
 hi-faih  ,Betrug'  ist  Nomen  postverbale;
arm.  asr,  Gen.  asu  , Schaf  wolle.  Fließ',  asvei  , wollig'  {^poku-\-r,  mit  a aus  0  in  offener  Anlautsilbe) ;  gr.  tt^xw  (=  lit.  pe§ü),  niv.Tü)  (=  lat.  pectö, ahd.  fehtan),  Ttsr/.rEo)  ,kämme,  schere',  rci-Aog  n.  ,Fließ,  Wolle',  Tiöxog  m.; ,Fließ',  xTfi/g,  Y.Tev6g  ,Kamm'  (aus  schwundst.  *7rx'r£v-;  lat.  pecten)-,
alb.  pile  , Werkzeug  zum  Flachskämmen,  -hecheln'  (*pekla) ;  lat.  pectö, -ere,  pexl  ,kämmen',  pecten,  -inis  ,Kamm',  umbr.  petenata  ,pectinatam'; ahd.  as.  fehtan,  ags.  feohtan  , fechten' ;  ahd.  as.  fahs,  ags.  feax  ,(Haupt)- haar',  aisl. /aa?  ,Mähne'  (*-poJc-s-o-,  vgl.  den  es-St.  ney-og),  aisl.  fcer,  aschwed. fär  ^Schaf^  {^fahaz  =  Ttöyiog),  aschwed.  fcet  (*fahti-)  ,Wolle,  Fließ',  ags. feht  ,Fließ',  ndl.  vacht  f.  , Wolle,  Schur',  ags.  fihl  ,pannus';  lit.  pesü, pesti  ,rupfen,  an  den  Haaren  zausen',   Iter.  pasyti,  susijpeUi  ,sich  raufen'.
Hierher  wohl  ai.  paks-man-  n.  ,Augenwimpern,  Haar',  paks-malä-  ,mit starken  Augenwimpern,  dichthaarig'  av.  pasna-  n.  ,Augenlid',  vgl.  in  nicht so  spezialisierter  Bed.  np.  pasm  ,Wolle'.
WP.  II  16  f.,  WH.  II  269  f.,  270  ff.,  Trautmann  217,  Specht  KZ  68,  205  ff.
798  '
pek^-  ,kochen';  Partiz.  pek^-to-  .gekocht^;  pek'i-ti-  ,das  Kochen',  peicM-^er^^ pok^o-s  ,Koch^ Ai.  pdcati,   av.  pacaiti  ,kocht,   bäckt,   brät'   (=  lat.  coquö^   cymr.  poh{ aXh.pjek,  ^hg,  pelcg,  vgl  auch  lit.  Jcepü)-,  Fut.  pähsyaii:  gT.  nsipw)]  Supi^; paktum  =  lat.    coctum^    aksl.   peUh]   Partiz.   paktd-    (=    gr.    TtsTVTÖQ,    l^t^ coctuSj    cymr.   poeth),   ai.   pdcyate   ,reift',  pakvd-   ^gekocht,   reif',  jpa/cii-  f/ ,das  Kochen,  gekochtes  Gericht'  (=  gr.  n:hptg,  lat.  cocti-ö,  abg.  pes^t,  apr. pectis)j  paktdr-  ,(ier   Kochende'   (=  lat.    coctor,   fem.   gr.  nsrtTQia),  pakd^ m.  ,das  Kochen,  Backen,  Reifen',  av.  nasu-päka-  ,Leichen  (teile)  kochend verbrennend';    arm.    wahrscheinlich    Äac   ,Brot'   als    *pok'^-ti-]   gr.    TceoGfo  " att.  TrfTTü)   ,koche,  verdaue'   {*peky:io)j    ^o-Präs.  fisTiTco]   rcexpig  f.  Kochen';     I 7teTt(j)Vj    -ovog    ,reif'    (f.   nertSLQa    nach    jx'nov  iTtiSLQo),    nörtavov    , Gebäck, Kuchen';  umgestelltes    *k^opos   in   äQto-'AOnog   (neben    dQTo-Ttonog)    ,Brot-^ bäcker';  alb.  pjek  ,ich  backe';   lat.  coquö,  -ere  ,kochen'  (ital.  kelt.  Assim.  " von   *pek]^ö    zu  *k"ek1tö),    coquus  ,Koch'  ( :  ägTO-xörtog),   coqulna    , Küche', als  osk.-umbr.  Lw.  poplna]   cymr.  pobi  (o  aus  e),   com.  pohas,   bret.  pibi ,backen',  bret.  pohet  , gebacken',  cymr.  poeth  {*k^ek^-tos)  ,heiß',  bret.  'poaz  • ,gekocht',  mcymr.  poburies   ,Bäckerin',  coru.  peber^  bret.  pober  ,Bäcker';  ' air.  cuchtar  , Küche'  aus  lat.  coctüra  ds. ;  ags.  ä-figen  ,geröstet';    lit.  (um- II gestellt)  kepü,  kepti,  lett.   cepu^   cept  , backen,   braten',   ceplis   ,Backofen'; ohne  Umstellung   apr.  pectis  , Ofenschaufel'  =  aksl.  peHh  ,Ofen,    Höhle'; lit.  pektas  ,gebraten*,  aksl.  *pekg,
```


### [2026-09-07T20:47:15.462Z] TOOL RESULT

```
<persisted-output>
Output too large (31.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/bri1rkv5t.txt

Preview (first 2KB):
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
...
</persisted-output>
```


## [2026-09-07T20:47:22.162Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pekv-\\|pek”-\\|pekw-\\|pek“-\" AHD_watkins1985.txt | head -20\necho \"=== context ===\"\ngrep -n -B2 -A12 \"To cook\" AHD_watkins1985.txt | grep -n -i -m40 \"cook\" | head -20"
}
```


### [2026-09-07T20:47:22.234Z] TOOL RESULT

```
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1306:BISCUIT dwo-, pekw- BISHOP spek- BISHOPRIC reg-! BISON weis-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1713:KILN pekw-
1718:KIRK keue-2 KIRTLE_ sker-1 KISHKE (8)keu- Kiss kus- KITCHEN pekw- KITH gndé-
2077:PEOPLE populus PEPO pekw-
2078:PEPPER pippali PEPSIN pekw- PEPTIC pekw- PEPTONE pekw- PER per!
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2140:Puc’ ped-1 PUGILISM peuk- PUGIL STICK peuk- PUGNACIOUS peuk- PUISNE apo-, gene- PUKKA pekw- PULICIDE plou- PULLET pau- PULLEY kwel-1 PULMONARY pleu- PULSATE pel-6 PULSE! pel-6 PULSE? pel-1 PULVERIZE pel-1 PUMICE (s)poi-mo- PUMPKIN pekw- PUNCH? penk¥e PUNCHEON! peuk- PUNCTUATE peuk- PUNCTURE peuk- PUNGENT peuk- PUNISH kWej-1 PUNITORY kvei-1 PUNKA peg- PUNT! pent-
2155:QUIRE! kwetwer- QUITCH GRASS gWel- QUITTOR pekw- QUODLIBET kWo-, leubh- QUONDAM kWo-
2184:RICH reg-1 RICOTTA pekw-
=== context ===
3:335:bher-3. Bright, brown. 1. Suffixed variant form *bhri-no- in Germanic *briinaz in: a. Old English briin, brown: BROWN; b. Middle Dutch bruun (> Dutch bruin), brown: BRUIN; Cc. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. Reduplicated form *bhibhru-, *bhebhru-, “the brown animal,” beaver, in Germanic *bebruz in Old English be(o)for, beaver: BEAVER!. 3. Ger- manic *ber6, “the brown animal,” bear, in Old English bera, bear: BEAR?. 4. Germanic *bernuz in Old Norse bjérn (stem ber-), bear: BERSERKER. [Pok. 5. bher- 136.] bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: FRY}. [Pok. 6. bher- 137.] bherdh-. To cut. 1. Zero-grade form *bhrdh- in Germanic *burd-, plank, board, table, in: a. Old English bord, board: BOARD; STARBOARD; b. Old Norse bordh (> Swedish bord), board, table: SMORGASBORD; c. Old French borde, hut, and bort, border: BORDELLO, BORDER. 2. Possibly Latin forfex, a pair of scissors: FORFICATE. [Pok. bheredh- 138.]
12:344-bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
19:828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffixed form “pel-ko- probably in Ger- manic *falkén-, falcon (< “gray bird”), in: a. Old French girfaut, gyrfalcon: GYRFALCON; b. Late Latin falcé, falcon (but Germanic *falkén- is also possibly from the Late Latin): FALCON. 3. Suffixed extended form *peli- wo- in: a. Greek pelios, dark: PELOPS; b. o-grade form *poli-wo- in Greek polios, gray: POLIOMYELITIS. 4. Per- haps Greek pelargos (< *pelawo-argos), stork (< “black- white bird”; argos, white; see arg-); PELARGONIUM. [Pok. 6. pel- 804.] pel-3. To fold. 1. Extended o-grade form *polt- in Ger- manic *falthan, *faldan in: a. Old English fealdan, faldan, to fold: FoLD!; b. Old High German faldan, to fold: FALTBOAT; Cc. Germanic compound “*faldistélaz, “folding stool” (*stdlaz, stool; see sta-), in Medieval Latin compound faldistolium, folding chair: FALDSTOOL;
```


## [2026-09-07T20:47:38.818Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT nasu-paka ===\"; grep -n \"nasu-pāka\\|nasupāka\\|nasu-paka\\|nasu-p\" BRT.txt | head -10\necho \"=== BRT pačaiti / pac ===\"; grep -n \"pačaiti\\|pacaiti\" BRT.txt | head -10\necho \"=== BRT paka ===\"; grep -n -i \"^pāka\\|-pāka\" BRT.txt | head -10"
}
```


### [2026-09-07T20:47:38.903Z] TOOL RESULT

```
=== BRT nasu-paka ===
=== BRT pačaiti / pac ===
10842:•  j.  xSäfhya-'*  n.  'Nacht-,  Abendmahl': vispa'.ibyS  saslim  baraiti  fsd.)  ätari'  .  , yasbyü  aim  *hampacaiti  'ttimca  süirim'a (sd.)  Y.62.7.
26434:•  ').  süirya-  n.  'FrUhmahl,  -stück':  yaHbyS afm  (näml.  ätarl)  kamfpacaiti  xlsfitlmca 'rJmca  "denen  er  das  Nacht-  und  das Frtihmahl  kocht"  Y.6'2.  7; —  «jff/n  (sd.) "rJtn  is»mnS  Vt.  14.  20.
=== BRT paka ===
```


## [2026-09-07T20:47:39.544Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf 360 (p336) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==361' SYN.txt | head -60"
}
```


### [2026-09-07T20:47:40.768Z] TOOL RESULT

```
=== SYN leaf 360 (p336) ===
v, plesiv calvo OE aie ee Boh. _lysy, pleSivy, pleSaty chau ME alled, calou Pol. lysy ; ean ek NE bald Russ. lysyj, pleSivyj ? a ue aa ite ee khalati-, munda- mi O calo Vv. kaurva- maol MHG kal pe NHG kahl m
the root *maz- ‘cut off, hew’, in Goth. maitan ‘hew, cut’, ON meita ‘cut’, etc. Walde-P. 2.222. Otherwise Stokes 204.
4. ON skalli (sb. ‘a baldhead’), adj. skollotir, Dan. skaldet, Sw. skallig, perh. fr. s-form of the root in Lat. calvus, ete. (above, 2). Ernout-M. 137. Falk-Torp 980 (but combined with the following).
OF calu, ME calouh (NE callow), Du. kaal (LG kal > Sw. kal), OHG kalo, MHG kal, NHG kahl: ChSl. golu ‘naked’, etc. (4.99). Walde-P. 1.537 f. Berneker 325f. Combined by some with Lat. calvus, etc. (above, 2) on the basis of IE variant initial k/g, or even as loanword from it (cf. Walde-P. 1.538).
ME balled, NE bald (cf. also Dan. beldet ‘bald, callow’, of birds), prob. fr. ball ‘white spot’ on the forehead (in spite of the fact that this is not quotable as early as balled), this (whether or not through Celtic) : Grk. ¢adapés, etc. (above, 1). Walde-P. 2.175. Falk-Torp 123. NED s.v.
5. Lith. plikas, Lett. pliks (also ‘naked’), ChSl. plévii, SCr. plesiv, Boh. plesivy, plegaty, Russ. plesivyj (also Lith. pleikas ‘bald spot’, Lett. plaikums ‘spot’) : Lith. plynas ‘plain, even, smooth’, plyné ‘plain, open field’, Norw. dial. flein ‘bald, naked’, Sw. dial. flen ‘naked’, but further root connection dub. Walde-P. 2.93. Mihl.-Endz, 3.344. Falk-Torp 235.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
318 SELECTED INDO-EUROPEAN SYNONYMS
Lett. katls ‘bald, naked, bare’: Ir. coil ‘thin, slender’, W., Corn. cul ‘lean, narrow’. Walde-P. 1.455.
6. ChSI. viiz-lysti, Boh. lysy, Pol. zysy, Russ. lysyj : Skt. rucant- ‘bright, shining’, IE *leuk-, beside *leuk- in Lat. liz ‘light’, ete. Walde-P. 2.411. Berne- ker 752.
ChSl. plévt, above, 5.
SCr. éelav, fr. Turk. kel id. (ef, above, 2, Rum. chel).
7, Skt. khalati-, Av. kaurva- - Lat. calyus, above, 2
Skt. munda- ‘with shaven head’ (also ‘hornless, blunt’), perh.: Skt. 7d- ‘crush, rub’, etc. Walde-P. 2.288 (287),
4.94 LAME Grk. _ xwAds Goth. halts Lith. raiSas, Slubas NG xourcés ON halir (lami) Lett. _tizls, klibs, slums Lat.  claudus Dan. halt, lam ChSl. chromit It. zoppo, ranco Sw. halt, lam SCr. — hrom, Sepav Fy. botteur OE healt (lama) Boh. chromy, kulhavy yy Sp. cojo ME shalt, lame Pol. chromy, kulawy Rum.  schiop NE lame (halt) Russ. chromoj Ir. bacach, losc Du. kreupel, lam, mank Skt. grona-, srama-, pai- NIr. — bacach OHG _halz (lam) gu-, ete. W. cloff MHG lam, halz, hinlende Av. By hhe Br. kamm NHG  lahm, hinkend
The words listed are those used pri- marily for ‘lame’ in the leg or foot (as in NE he is lame), but most of them are or were also used for ‘lame’ in wider sense, ‘crippled’ in any limb.
They are from diverse notions such as ‘
```


## [2026-09-07T20:47:51.007Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN leaf ~378-380 ===\"; for n in 378 379 380; do echo \"--- NR=$n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | grep -o \"3[0-9][0-9] SELECTED\\|SELECTED INDO-EUROPEAN SYNONYMS\\|5\\.2[0-9] [A-Z]*\\|COOK\" | head; done"
}
```


## [2026-09-07T20:47:52.183Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Leichen ===\"; grep -n -i \"nasu\" BRT.txt | head -20\necho \"=== BRT pak ===\"; grep -n \"^pak-\\|paka-\\|pak-\" BRT.txt | head -20"
}
```


### [2026-09-07T20:47:52.198Z] TOOL RESULT

```
=== SYN leaf ~378-380 ===
--- NR=378
COOK
--- NR=379
SELECTED INDO-EUROPEAN SYNONYMS
5.21 COOK
5.22 BOIL
5.23 ROAST
5.24 BAKE
--- NR=380
COOK
```


### [2026-09-07T20:47:52.260Z] TOOL RESULT

```
=== BRT Leichen ===
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2551:spjmm  taropi^w)m{'&&.)  dastccvai  °tal-  kelterler Ä,.,  ..aber  (die.)  die  ungekelter- sqm  Syachnanqm  ästäraiti  "wenn  einer  ,.,  ten  . ,"  V.  Ij.  43;  — ■  yesi  nöit  sänö  . .  ^ta»- . .  solches  Thun?"  V.  jj,  ao;  —  yaica  vao-  hqtn  astqm  .  ,  barptit?m  frajasqn  "sonst cät  . .  aSaoa  (sd.)  ..  *havanli  (sd)  -tuhe  könnten  Hunde  .,  die  Knochen  verschlep- ryao'knaAe  .  .  V, /j, I3f.;  —  foa  iristaAe  psa"  V-6.46;  T,—yat ..Strim  natuplhm tatiüm  ovaMsta  . .  "tahe  ^aöinahe  , ,  V.  frajasqn  .  .  ava  °tim  nasupiknn  lanaeta 8. 100;  —  ä^ravamm  yaoida'i^ö  (sd.)  . .  . .  apa  'tarn  disiam  (sd.)  baray^n  apa  -t?m Hahmiii  natre  ".  .  einem  solchen  Mann  aa/jnjni  (iariy;'«  "wenn  (sie)  ..  auf  leichen- (der  purifizirtj"  V.p. 37— 39.  4)  auf  kochendes  Feuer  stossen  ..,  den  Leichen-
2560:drw^  .  .  'tat  nasul"''  pinnäne  yä  .  .  V.  Gen.'*:  °(.a  ..  aitihä  z^mä  V.j.18,  6.7, 10. 1;  —  -tat  bansma  yat  paiti  apim  .  .jiV.S,  16.12.  2)  'dann,  so'  a)  hmier  ytzi: S.joi?).  b)  substantivisch:  'tattlvayö\yezi  anhat  upaStm  va  ..  'ua  ..  altä ..  yat  K  asti  ,  .  Y.2j,5;  — D  "/«*  ty<^^vasträ  fraca  ktrantaytn  .  .  V.7.12;  N. iariam    ava*    risam    ..    D.  (J-S;    —    äat  26.  b)  hinter  _yfl/:  Hat  yat  hr! frä  vayS
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
3024:auch    Aka  Manah,    Vohu  Mattah    besiegt  j  über  mit  Flecken  bedeckt':  druxi yä  nasus
3636:•  j.  apäxtara-,  apIx^Ära-  Adj.  'rück- wärts, hinten  gelegen'  sva.  'nördlich'*^: Harat  haca  nafmst  'tara^byB  haca  naf- maiibya  fradvarat  aarö  mainyus  V.  ig.  i ; H.  2.25,  FrW.  70.42;  —  druxs  ya  nasus upaJvqsaid  'Xraäbyö  nalmaäbyB  V.  7.  s 8. 16;  —  °W''  apanasythe  "im  Norden sollst  du  verschwinden"  SrB.j.
3705:•  j.  aipi  tä  adv.-artige  Verb,  'hernach, darauf:  mqnaym  b.l  .  .  aipi  ta  nasuf zga'^aite  ya>a  .,  V.^.46.
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
3880:•  J.  ainrLvarana-  m.  'Bedeckung,  Beklei- dung': up^mii  [aite]  statri^ta),  anlama  °na also  druxs  yä  nasus  fräsnaoili  "zu  oberst das  Lager,  das  äusserste  Kleidungsstück erreicht  .  ."  V.j.ioC?)'*.
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
4282:•  j.  an-aiwi)Tiixta  Adj.  (fem.  'ia-)  'nicht angenagt,  ange&essen':  yezi  aisa  nasus  °ta sanö  v3  kjr^s.x^arS  (sd.)  V.7.29.
4303:•  j.  an-aiwi5.x''ar«8'a-  Adj.  (fem,  -iJa-) 'zum  Genuss  ungeeignet,  ungeniessbar' : vtsprm  ä  ahmät  alsa  ä/s  ayaoidya  (sd.) ";jo  yavat  aisa  nasus  niibtrsta  V. Ö.31.
6076:—  'sähe  paiti  mq^rfm  'sähe  paiti  fra-  manarihäY.4ß.  10;  —  '/ahya  yäsa  (sd.) sasiim  V.  4.  43  (s.  a);  —  'fa  i-iyaca  Vyt  a^m  Y.54.  i;  —ySais'sMt  nipSrfhi  (sd.) 75;  —  yS  'sili  hr>jyqsl>mS  (sd.)  R  /;  —  manasut  vohn  V.28.  11.  3)  im  jAwr.: airyamarum  isfm . ,  matistim  'saht  srava-  hs  aiwyiixsayatB  hadü  'Saia  vasträca  .  . tthqm  Y.54'3;  —  'iahe  myazdanqm  Vr.  Y.  3<?.  4;  —  yöi.äim  hanhana  (sd.)  'säca ^■3;  —  y^i  til/'rat  (sd.)  aurö  mainyus  frSriticaH.8.i; —  •/«lä""  nmtaahana.. dahlm 'sähe rauh fus  Yt.13.TT,  —  haoma..  yaorum  (sd.)  äste  V,4.45;  —  ahunm haÜTm^a  'sa/ie  xi'r  (sd.)  ahi  Y.  10.  4^  — \mazdqm   yS    'sähe    apanöJ?mS  yS    'sähe
6780:•  j.  a-huta-  Adj,  'nicht  ausgepresst',  vom ,  '^"'  "■  •  das  was  unter  den  G.  den  ^Ä. Haoma:  mit  haomö  hul5  axtis  .  .  nöit  enthält  .  ."  ti.46;  —  'z-aiffm  g.l>qm  V. *nasus.ava.hrjiö  (sA.)  ava  alte  ahuia yaiia  34-I-6,  Vr.2.7,  14.0,  Vd./2;  —  'i-ai/yä ?a%wars  anzavB  Y.6.^3.  S''^>aya  hatidstä  yazamaide  \. 34.16,  Vr.
6838:ia*aAf  (sd.)    'stats  asaons  »des  S.,    des , '""  i^**")  ^^f'^a  yasn>m  anasUya-ia  data
6946:. .  nasUin  pacät  V,  16.  ij,       *pairi.aejastarS
7237:/ay  (sd.) :  drsgvä  akät  *a  syqs  '*'  manatghö Y.  47-  5 ;  —  y!fi  vanhsus  3  mananAö lyeinti  Y. 3(^.3.  a)  verdoppelt:  vanAsus ä  zl  a  iiianav A3  sydntiYt.  11.12.  4)gAw. mit  Dat.,  nur  unmittelbar  hinter  dem  3i- Dat  der  <i-Stämme,  dessen  Bedeutung  da- durch nicht  verändert  wird :  /rlnpmna  (sd.) ahuräi  3  Y.  3p.  5;  —  yezT  AlH  d3t  .. aAurS .  .yavöi  vlspai  «'"  AvatpA/vTm  (sd.) Y.5J.1;  4;  —  at  m3  .  .  mazöi  magai  a paitTJiänata  Y.  25. 1 1 ;  —  xSmävatqm  vah- mäi  a  Y.^ff.io;  53.2;  —  at  töi  übe  .  . x'an^äi  3  Y.  34.11;  —  dazda  (sd.)  .  . syaohananqm  mazd3i  xfäitrimca  aAurai 3  Y.-jy.is;  —  auch  beim  Jt'-Inf,;  pasBs vJrlng.  ./rada'iai  (sd.)  a  45.9.  5)  gAw. mit  Instr.,  nur  unmittelbar  hinter  dem i3j7-Instr.  aus  Pron.  in  den  adv.-artigen Verbindungen  anais  3,  tat/  a,  yäis  a; sbes.  ni)  Praev.'*'    (mit    'Aar-,    ^kar-,
7483:•  j.  *ä-stärayantiin "  Absol.,  mit  asti 'er  versetzt  in  den  Zustand  der  Sündig- keit': mit  sps.hnts  . .  nasul  nar^iit  näit *ästaraynti  yeüca  aite  nasävs  yit  spS.hr^- taca  . .  nasus  narsm  'tTm  äuhä^*'^  ". .  und wenn  diese  Leichenteile,  ein  von  Hunden verschleppter  .  .  Leichenteil  Jemanden sündig  machen  würde  .  ."  V.  i.jf.
7575:I  •  j.  Shitay-  f  'Befleckung,  Veninreinigung, j  Makel':  p>r>tte  'lim  ya  äili  ätrfni  apftn zqm  gqm  urvarä  V.  //.  9 ;  —  nSit  aotS  välH I  nsit  ganmS  rWit  axtü  . .  nöit  'tti  dafvB.- data  Yt  10. 50;  —  nasyäti . .  akmal  haca I  nmäiiät  'ti!  Y.  ro.  7 ;  —  csat . .  a^a  druxs \y:l    nasuf  axiUa  *pavitiea  °tiia  /räsnaoili V.  5. 2  7 ;  —  paiiiitätSe  ayaiyh  püifyä  'fya (GS.)  ya  artrS  matnyui/rakfrmtai  V.  20. 3. Vgl.  ähila-  imd  anähila-  No.  3.  —   Pü. ;   ähö- kenün,    erl.   (lU  V.  j):    aiSrih,    (lu    V.  //): awzärif);  (lu  V.  20):  Shokemiär  (Adj.!). g.  dhiiäyä:  s.  hä{yy. ].  ähilä  P.  26:  lies  äxUi. j.  Shu  N.  4S:  lies  ä  Aü;  s.  ä  No.  6.
7829:mit  /r>l,  frB  i)  'erreichen,  treffen':  nsit gdüahe  .  .  tbalxB  frqstißna  (sd.)  fräsnu- y,lt  Yti/.  s;  —  cvat  antar?  *rurSus  aisa druxs  yä  nasu/  ax/i^a  .  .  fräsnaotti  V. J.27;  28;  —  ye%i  nsii  Aarv^rvm  baraiti aztaöa  hi  vfspä  hSirÜTl  fräsnaotti  ".  .  so trifft  er  damit  alle  Weiber"  (?)  V. />  19; —  nSit  ahyä  mä  ahris  (sd.)  syad^anäis frösyaii*    Y.46.8.  2)    'herzu-,    hinzu-
=== BRT pak ===
3675:•  j.  apänk-  :  apak-  Adj.  (fem.  apacl-)  'nach hinten,  rückwärts  gewendet':  "^//(NSf)" vazaili  arstiS  yqm  . .  "rückwärts  fliegt  die Lanze,  die  . ."  Yt.  10.  ao.  a)  NSm. als  Adv.'>:  °Pq^  ^avS  damayäti  "nach hinten  (auf  den  Rücken)  fesselt  er  ihre Hände"  Vt.70. 48.  b)  IS.  als  Adv. 'zurück': *'pasa^'>  vi  *zamar?  ana  duye*  {%A.)\i.i. 2g;  —  uzg?r>pt3mHt  saa'^pm  -pasa  apa.- j^anvainti  (sd^  Yt  14.46.
14831:•  j,  pak-  V.  Ttochen'.    Praes.  2  paca-.
15928:paka-
15951:•  j.  paka-  Adj.  'kochend'.
15952:KompE.  —  Zum  V.  pak-.  —  ai.  'päki'  Adj., mp,  'päk,  np.  'bä,  'vi.
25087:rapaka-
25112:•  j.  rapaka-  Adj.  'eine  Stiitze  bildend für  -,  im  Dienst  stehend  von  — '  (Gen.): a^  (näml.  daxmS)  sJ  asti  daibaitqtn  'AS vupsm  a  oAmOi  yat  alfa  *gainti/ tipaioAa- aüti  (sd.)  V.7."s6.'
26811:•  j.  spaka-  Adj.  'hundeartig,  Hunds*'; aHaam  •kanam  kahrpunanam  (sd.)  V. 14.  S-
26904:•  j.  'spä-  V.  'iacere'',  abicere'.  Praes.  17 spaya-,  j-Aor.  i  ipak-. —  PPfP.  'spata-, PFP.  pfkwa--''>.
29557:AbleiL  aus  hi-apak-  r.,  S  'OO  a.  a.  —  Pii. : Itanssltr.,  mit  der  Erl.:  niisak  'Harn';  vgL  lu
```


## [2026-09-07T20:48:02.806Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"nasu.p[äa]k\\|nasup[äa]k\" BRT.txt | head -10\necho \"=== around 14831 ===\"; sed -n '14820,14840p' BRT.txt\necho \"=== around 15945 ===\"; sed -n '15925,15960p' BRT.txt"
}
```


### [2026-09-07T20:48:02.881Z] TOOL RESULT

```
16827:mit  avi  und  ava  \)  'etwas  hinzubringen zu  — '  (Akk.):  yB  atr?m  nasupakim  dai- tlm  gatüm    avi    ava.baraiti
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
=== around 14831 ===
j.  pa(>i%ya  N.  ig:  lies  paairya  (LSf).
•  j.  "paoS  F.  jo,  angebl.  'fauüg,  stinkend'". Pü. :  fütak.  —  ')  Der  Verfertigcr  des  F.  ist dazu  gekommen,  indem  er  das  mit  pülaktum übersetzte  pasHsla-  (sd.)  in  paas  =  pÜtai  und jÄ"  ^  tum  zerlegte!
•  j.  paoiiäta-  Adj.,  'der  fauligste,  stin- kendste': daeväis  .  .  Af!tqm  '/Jis'  Y.12.4; —  vtspanqm  *aasUm  *'hmca ''  yai  >rrfat daoiatahum  F.  40.
Supcrl.  aus  einer  Basis  ar.  *paas-,  zum  V. pav:  —  Vg\.  "paus.  —  Vä.:  pülaitum.  — ')  Hds.  paeis>sl°\
•  j.  "Atuaoiyu  (sd)  paloha"  N. /.
j,  paitiul  N.  66:  lies  pUiai. y  paUihnUm    N.  /j:    MtS  paitis' ;    s.  'a«-, Sp.  30  m.
•  j.  *'pairauarätä.x«t  ^.44- Pü.:  fehlt.
j.  pais5.tami!  N.  44:  liet  f^lSj:
dby  Google
8i9
pak'
•  j,  pak-  V.  Ttochen'.    Praes.  2  paca-.
'kochen',  durch  Sieden,  Backen,  Braten zum  Essen  zubereiten:  saa^ri  hw  uzha- raym  ..pasBm  Ml pa'aym  airyä  äairihavS Yt  8.  58;  —  Med.  reflex.:  azJm  . .  yim i^airi  k»ns3spB  ayanha  pjtttm  palata  V. p.ii.
mit  frä  'etwas  verkochen  zu  . .'  (Akk.) : ya%Bii  p^^rahe  . ,  fra  naHtm  (sd.)  nasum palat  \.i6.iT.
mit  Aam  ä.a<n%.:  yalily^  aim  (näml.  atarl) hqm*paiaili  xiäfnimla  tüiflmca  (sd.)  Y. 62.T,  —  nasBm  ham.pa^an  nasBm  hSvayan  \ (sd.)V.Ä73.
■t.  fiacaä,    np.  fazad.    —    Pü. :  fiuxlan '
')   Wegen    dei  u  s.  Hbu.  KZ.  27.  107;
FusuDg  Saleuakk*  GlcPh.  /.  30g  ist  m
vertländlich.
pat-  Noten  8ao
mit  ara  i)  'herabfallen':  s.  Inf.  2)  in rftfßdscher  Art  Tiinab-,  hinzugehen  zu  — ' {avi  mit  Akk.):  äat  ava.paiat  Jraarase  . , avi  xrays  veurukahm  Yt  ig.  58,
=== around 15945 ===
dby  Google
885
pazdav-
paka-
886
5.  3)  'verscheuchen':  yai  mqm  iura (sd.)  pasdayanta  .  .  naotaraca  Yt  J".  55;
Za  einem  Praes.  3  n.  ^pa-zda-ti ;  %.  "thaii- und  BtHL.  ZDMG.  JO.  686.  —  Pfi.:  transsltr. (paid^nil),  mit  der  Erl.;  kus  dost  Aae pas  Skä/rl (s.  noch  syazg;  No.  3).
•  j.  pazdav-  m,  Name  schädlicher  Klein- tiere, etwa  'Käfer,  Made' :  baevan  'dunam gäks.varttanqm  (sd.)  ava.JanySl  V.  14.  6,
np.  vgl.  paidak  'Kommilbe',  Ob  daiu  ai. /fifoi-m.  EN.  —  PB.:  pind,  ob  ♦/"ä"''''*?
•  j.  "^"paSna-  m.  "Hinsehen  auf  — ';  nur LS.  'in  conspectu,  angesichts',  mit  a)  Gen. und  b)  Akk.:  a)  'ne  varsis  pisinankB  YL 5-37)  49;  —  ""'  <^P^  däityayh  Yt. 5.112, 17.29,17.61.  b)  °tte  äpsm  frazdänaom Yt.  j.  108.
KompE.  (s.  mpcaHaia-\  —  Zum  V.  sfas-, S  83.  a.  —  O  NA.  hat  pasne;  aber  F  i,  E 1 haben  durchaus,  J  [o,  PI  1  fast  überall  /.
•  j.  'paSna-  n,  'Augenlid':  'nsm  F.^d. Vgl.  ai.  päkfman-  n.  'Augenwimpern';  np. pdim  'Wolle';  e.  dazu  Zufitza  Gült.  1S9, Hbm.  PSt.43.  —  Ya.%pS!  i  fah»  (woiu  liurd. pac  i  cam  'Augenlid',  ZDMG.  3S.  55  lU  ver- gleichen).
•  j.,  g.,  p.  'pä(y)- V.  'hüten'.  Praes.  ipa-: pa-'^,  a  pHya-,  T  päpay,  fj  paya-,  °fya-'>; j-A  0  r.  1  päA-.  —  PPfP.  fiata-;  Inf.  psi,  pü  e, *patayal-ca,  pä%räi,  'fyethyai.
i)  'hüten,  schützen,  schirmen':  arh  . . xlü%rTl  hupStS  timS  ya  uitrS  p3iH*v^airiS Yt  14. 12;  — pairi^wd  bavaiti  panth  yim .  .  paiti  Aog.  ~S;  —  avatsqmca  pahü phntS  yim  isMti  ..Yt  10.  4$; —  ahwum vairim  tattütn  paiti  V.r/.3;  Yt._j.3;  — ttr^m  afur<^mazdä  patuv  utamaiy  xsa- ^•^am  X.1.4;  4,  2.3,^.3',  4.3,  7.3,  Am.4, Ao.  1. 4.  a)  'behüten,  beschützen  vor  — '
{pairi  oder  iaca  mit  Abi,):  päta  (»P.) tiB  tbisyantat  pairi  SrB.j;  F. /o;  —  ^imaiii dahyäum  c^urt^mazdä  patuv  haca  hainäya D.^3;  6.^.  2)  'abhalten,  abwehren von  — ,  es  verwehren,  dass  . .',  mit  Abi. oder  abL  Inf,:  ta  .  .  yä  Tm  Aujyatui/ (sd.) payat  {3SKA.)  fiHt  duzjyatnis  Y.  46.%;  — at  tSng  är)gvä  . .  pat  gh  frörftöis'isA.)  Y. 46.  \;  —  %waAya  mqhranS  dstim yi  Js  pat dar^säf(sd.)  alahyä  Y.js.  13,  3)  'wahr- nehmen, sich  angelegen  sein  lassen,  sorgen für  -'  (Akk.):  piahake  (aSKj-AorM.) aahuhwftnca  ratuhwim&t  Yt  Ä  1;  — !'  imam  parsam  käram  padty  yadiy  kar<^ parst^  pata*  ahatiy  "(so)  sorge  fiir  das
persische  Heer;  wenn  fUr  das  persische Heer  gesorgt  ist,  . ."  D.5. 3. mit  a:  s.  afya^yai  Inf. mit  patiy,  paiti  i)  I  Med,  'sich  hüten, .ich  in  Acht  nehmen  vor  — '  {haca  mit Abi,):  ha?a  draug^  darSam  poHpayt^uvä Bh.4-5-  a)  Med.  'sich  vorsehen  gegen  — , sich  zu  decken  suchen  gegen  -'  (Akk.): ya'^a  na  snaihi/  asne  niymal^m  paiti.- ■ainöii . .  aval paiti.papayamnB  *vlovä  . . '.  21.  3)  Med.  'sich  (einer  Sache)  ver- sehen, (es)  ahnen',  absolut:  na^a  mainyu paitipaite  "und  nicht  versieht  er  sich  des im  Geist"  Ytro.  19.
mit  \/r3  und]^  nX  'schützen,  Schutz gewähren  vor  — '  (pairi  mit  Abi.):  \frä\^ \a  uvaiibya  ahubya  uvaiibya  nS  akubya ipayi  (Opt.)  '*  .  .  pairi  .  .   mahrkat  Y.
mit  an) 'hüten,  schlitzen':  sraosim  ..yB nipaiti  mazdä  damqn  .  .  ys  vUp»m  aküm ..  pnhua  maiki/a  nipaiti  Y.57. 16;  — azftn  bsii..nipayani  vispa  voha  Ytj.Sg; — lam  ta  daiühavB  mpahi  Yt.ro.78.  a)  'be- hUten,  beschützen  vor  — '  (pairi  oder  parB mit  AbL):  nipaysis  mallm  urva%»m  .  . aurva%at  parB  Yli,  24;  —  uvaiibya  nS ahubya  nipaya  (Opt)'^  ..  pairi .,  moAr/tat YL  10. 93^*;  —  faf  iij  /i}tr0  nipätü  pairJ . . Ibaisauhat  Y.5Ä  2.  2)  'in  Obhut,  Ver-
wahr geben':  tatca  .  .  %wahmT  3  *dqm (sd)  nipauhl  (iSKjAorM.)  manS  vohB  .. Y.45>io**i — y^  ais  asim  ttipäahl manasca vokB  yavaitaiti  "der  ich  darum  das  rechte Tun  in  Verwahr  geben  will  und  das  gute Denken  flir  immer"  Y.  18. 1 1  *'.
ai.  pAli,  pähi,  fäsati,  pAntak;   ap.  päyad,  'bäd.
—  S.  noch  päA-  (piiy\  —  Pü. :  päyüan,  päaa- kih  karlan,  Npö.  (lU  Y.  ja.  13,  46.  A):  dir kardan,  —  ')  pa.  vor  dem  y  des  Opt. :  payä.
—  ')  Nur  im  Inf.  äfyniyäi.  fya-  ist  die  regel- rechte Kompositions  form  lu  paya-  (mit  a  aus urldg.  A;    IF-  7.  70.    —    J>  Vgl.  Yl,  to.  93.
frä  ist  Wiederholung  aus  dem  Vorhergehen- den, wie  auch  die  Stellung  von  aSa  (sd.,  No.  5) ausweist.  —  «  Vgl,  V.57.  2S  und  No.  3.  — 5)  S.  iSt.  unter  dam-,  daidar-  and  pairigae'i.a:
•  j,  'pa{y)-  i)  Adj.  "hütend,  schützend, schirmend'.  2)  n.  'Schutz,  Schirm'.  DS. pdf  als  Inf.  sbes.
KompE. ;  Ableit.  {s.  fiavaa/.).  —  Zum  'V.pä(yy.
—  ai.  -pa-  Adj.
•  j.  paka-  Adj.  'kochend'.
KompE.  —  Zum  V.  pak-.  —  ai.  'päki'  Adj., mp,  'päk,  np.  'bä,  'vi.
db,Google
887
päta-
•  P-  (.  i-)  päta-  Adj.,  PPfP.:  s.  'päiy)-. KompE.
•  j.  %wqm  tat  upaxbaya  y3i  pStayas£a nipätayJi  mhtshtmla  Miarfca  (soll  heissen) "darum  ruf  ich  dich  an,  dass  du  schützest und  beschützest  Sonne  und  Mond"  VyL  43.
Verbindung  von  fä°  und  ni-fä'  wie  Yl  /aSo.
•  j.  patar-  m.  'Hüter,  Schützer,  Schinner', von  Göttern :  'ta  nqma  ahmt  (näml.  AhM.) Yt/.i3;  —  /fiw'näml.  Mi^ra)  maskanahe °/a  nipata  ahi  adruzqm  Yt.  10. 80;  — haom^m  . .  'tsrftn  tanuye  baire  Yt  14. 57.
KompE.  —  Zam  V.  p^yY-  —  ai.  pätir-  m., rp.  ^fl'(?);  llBM.  PSl.  35.  —  Va.:  päspän.
```


## [2026-09-07T20:48:16.158Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 336 (leaf ~378) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==379' SYN.txt | sed -n '1,40p'"
}
```


### [2026-09-07T20:48:17.380Z] TOOL RESULT

```
=== SYN 336 (leaf ~378) ===
 Falk-Torp 747.
5. Av. raé0wa- etym.? Barth. 1482 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
336
5.21 COOK (vb.) 5.22 BOIL Grk.  xésow (naryetpet) aw NG payetpebw Bpatw Lat.  coquere coquere It. cocere lessare Fr. cuire faire boutllir Sp. cocer, cocinar, guisar _cocer, hervir Rum. alt, coace fierbe Ir. fo-no- berbaim Nir. = futnim beirbhim, bruithim W. coginto berwi Br. poaza (darevi) birvi Goth. .... ote ON matbiia sj00a, vella Dan. lave mad, koge koge Sw. tillaga, koka koka OE gegearwian stopan, wiellan ME coke sethe, boile NE cook boil Du. koken, bereiden koken OHG  kochon stodan, kochin MHG kochen kochen, sieden NHG  kochen kochen Lith. virli virlt Lett. varit varit ChSl._ variti varilt SCr.  kuhatt varili, kuhatt Bob. _varili varilt Pol. = warzy¢ warzyé Russ. varit’ varit’ Skt. pac-, ¢ra- pac-, ¢rd- Av. pat pat-
5.21. Words for ‘cook’, that is, gen-
5.23 ROAST, FRY 5.24 BAKE
draw, dpvye, gayw Ynrva; myavifo lorrére, frigere, assdre
arrostire; friggere rélir; frire
érrdw, técow
Yyvw
coquere, torrére (in furnd)
cocere (in forno)
cuire (au four)
eral terms for preparing food by the use of heat, covering boiling, roasting, bak- ing, etc., belong mostly to an inherited group representing an IE *pekv-. The forms of this root in Indo-Iranian, Tocharian, Greek, and Latin have the general meaning ‘cook’ (also ‘ripen’ fruit in Skt., Grk., Toch.; in Lat. also ‘prepare anything by heat’, as ‘bake’ (bricks), but in Balto-Slavic (also Alb.) are specialized to ‘roast, bake’ (Russ. only ‘bake’, as also W., Br.), and in several languages are used most com- monly for ‘boil’ (conversely ‘boil’ for ‘cook’ in Balto-Slavic).
With the spread of the Roman art of cookery, the Lat. derivs. coguus ‘a cook’ and coguina ‘kitchen’ were widely bor-
asar; fretr cocer (en horno) Srige, praji coace (in cuptor) (fo-no-) fo-no- rostaim, grioscaim Suinim rhostio, crasu; ffrio pobi, crasu rosta; frita poba steikja baka
stege bage
steka baka bra@dan, hyrstan bacan rosle; frye bake
roast; fry bake roosten, braden bakken brdtan, harstan, rdstan backan braten, resten backen braten, résten backen keptt, spirgintt kept
cept cept
pestt, praziti pesli
peti, przilt pect
pect, smazili pect
piec, smazyé, prazyé piec
Zarit’ pec’
pac-, bhrajj- pac-
pat- pac-
rowed in Celtic and Gmc., and through the latter in Slavic; much less widely the verb coquere and mostly in the sense of ‘boil’. But in some cases new verbs for ‘cook’ were formed from the noun.
Some languages have no distinctive general word for ‘cook’, but use the more specific terms for ‘boil’, ‘roast’, etc., a8 the case may be, or in a phrase like ‘cook a meal’ use words meaning ‘prepare, make ready’, some of these latter being almost specialized in this direction.
1. IB *peke-. Walde-P. 2.17f. Er nout-M. 218f. Walde-H. 1.270f.
Skt. pac-, Av. paé- ‘cook’; Toch. pak- ‘cook’ (SSS 448); Grk. éoo, Att. mér7w, méx7w, fut. mayo ‘cook, bake’; Lat. coquere, with its derivs. (below); Br. poba, W. pobi ‘bake,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
» (formed to the pple. meer iS poeth ‘hot’, Lat. . Lith. kepti, ChSl.
general Balto-Slavic
;, etc. pekas ea Alb. pjéké ‘bake, roast, ’
ripen ve > It. cocere, Fr. cuire, cer _ coace (esp. ‘bake’; ae Sp. or token (> Dan. koge
```


## [2026-09-07T20:48:18.323Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD puxtan/pac ===\"; grep -n \"puxtan\\|pu\\[x\\]tan\\|paz-\\|pačēn\\|pac-\" PHD.txt | head -20\necho \"=== PHD puxtag ===\"; grep -n \"puxtag\\|pxt\" PHD.txt | head -20\necho \"=== NYB pac ===\"; grep -n \"pu\\?xtan\\|pačītan\\|paz\\b\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:48:18.391Z] TOOL RESULT

```
=== PHD puxtan/pac ===
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
4640:pafšīr- pafšīrišnīh pafšīrišn paz- pa(č)čēn pa(č)čībāy- pa(č)čībāgīh pašēmānīh pašēmān pišīz paššing pašn pašom paššinj- paššinjīdan paššinjag pašm pašmēn pašt paštag pad- petyārag pattāy-
=== PHD puxtag ===
=== NYB pac ===
562:apa-zāyītan pz'dytn'] v. apazütan.
565:apazónikéh possession of overflowing spiritual blessings, or gifts, a quality characteristic of Zartuxšt's homestead 502, with the gl. apazon thac ke veš bavet ke mat ke-c rasét? from whom, among those who have come and who are to come, does more (spiritual) in- crease issue [than from Z.’s birthplace]? probably a quotation; — heavenly nature, of Zartuxst 5375. 11019.
566:apa-zütan ["pzwtn'], apa-zāyītan [’pz’dy- tn'], apazäy- ['pz?d-], to increase, to augment, pt. = pret. pass. 3d p. sg. apa- züt 109%, apazäyit ['pz'dt'] 925. — < *abi-jav-, in SW with api- substituted for abi- (v. s. v. apa-) < abi-+ Av. (504) !gav- ‘to procure’; MPrth "bgwdn *bg*w- ‘to increase, to add to’, ?bg^w ‘increase’; Arm lw. augut ‘profit’; — OP caus. abi- jävaya- ‘to add’; MPrs pres. ’bzw- intr., ’bz’y- trans. ‘to increase’; Paz. awazūdan awazüed. Henning, A-H III Gloss. s. v. ’bgwdn; Benveniste, JA 228, 1936, 203- 204; Ghilain 76.
1649:gavakéh [gwb’kyh] increase, growth 109. — From Av. (504) !gav-, v. s. v. apazütan; Bailey, ZP 83 sq.
1698:göspand [gwspnd; KYN?] cattle in gen- eral, but esp. small cattle, sheep and goats, as distinguished from horses and cows, coll. 381%. 3916 ete., pl. cas. rect. 9417.20, 10416; pl. cas. obl. —-än 1” [KYN^-n'] 45%. 802. 861%, 893. 905-6, 943. 9724. 981, 1028; — apazär-göspand v. apazür. — Av. (506) gaospenta-; Paz. gospand, NP gospand, gosfand.
2535:mčnči [mdnwd: thus the FrP] A. adj. heavenly, celestial, immaterial, ideal (in the Platonic sense), always placed before the subst.: ~ ästisneh 3871, ~ kamakéh 4022, ~ venišneh 1105, v. these ws.; ~ astéh heavenly peace 561%; ~ tag 4 den 561°, v. tag; — often with the ending -€ before the headw.: ~-é xrat the Heav- enly Wisdom (personified) 68~77, passim ; 7-6 asn-xrat 76144; ~-é€ + a long series of abstract virtues 8514-18 ‘heavenly, of heavenly origin’; ~-é dätistän 171%, — B. subst. 1. pers.: immaterial, spiritual be- ing: apazönik ~ Ohurmazd 3985; ganäk (v. this w.) ~ the Evil Spirit, Ahriman;
2782:nók [nwk'] new 518; 112??? v. apazār; adv.: ~ zätän newborn 124; anew, again
2884:pahlom [p’hlwm, inser. p'lswmy], pāšom [p’swm] 1. noble, elevated, exalted, fore- most: Sühpuhr ... martan ~ foremost among man 15!? = P2:5 (p’lswmy). — 2. sublime, blessed, paradisiae, of Garod- màn and the heavenly world 3115. 325 [p'šwm]. 8916; of those bringing about the fraškart 105%. 1067! [p’swm]; ~ dēstēh i 6 yazdčin blessed friendship with the gods 5511; of ahläyeh 598; sup. ~-tom apazär i crat the most sublime power of Wisdom 89?" (~-tar Mx 151), — Not to be combined with fratom (g. v.) From *pardama-, orig. ‘Parthian’, an adj. derived from Par0a(va)- (Gr IIdp0ot) in the same way as Av. (710) dahyuma- from dahyu- and (1661) zantuma- from zantu-, cf also (1566) the name of the people Sairima-. In Achaemenian time there are proper names such as (in Bab. cuneiform) Par-ta- a- ma, Pa-ar-ta-am-mu (Holma, NKt 35 n. 1, after Tallqvist) Hence in the Bible, with the Hebr. pl. ending, partemim ‘the nobles’ at the Babylonian and Per- sian (historically: the Parthian) court: Esth. 13. 6%. Dan. 13. Parthians constitu- ting the highest social class in Parthian-
5519:’bgwdn, ’bg’w- apazütan
6433:awazāišn: apazāyišn
6435:awazūdan, -zāed: apazū- tan
6437:awazūnī: apazönik
```


## [2026-09-07T20:48:30.255Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 475 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==476' IEC.txt | head -30"
}
```


### [2026-09-07T20:48:31.512Z] TOOL RESULT

```
=== IEC leaf 475 ===
ght; W nôs, Br. noz, pl. nosiu, f.; Cor. nos; OCS oos Cz. noc, npl. noci; Latv. nakts, gp: nakéu. Cons.stem in Vedic nak, m.; Gk. nux; Alb. natë, pl: net; cf. nádje “in the morn- ing; Go. nahts £.; OHG naht, npl. id., gp: nahto; OE niht (fr. *nekt- or *nequt-); ON. nátt, nótt; Cz. veliko-noce, pl. (great nights? = *Easter); Li. naktis, gp naktü. Cf. also Go.
` nakts ‘by night’: OLat. nox, id. and Italo-Alb.
nesé (*tomorrow', fr. *noktjo ?). Vedic nak- tam, n. ‘night unexplained, except as an ar- chaic adverb > noun, see noktím
noktiom, -noktiom, adv. & collective of type nokt-, see above Gk. cf. meso-nüktion; Lat. tri-, aequi-noc- tium; MHG ein-nehte; ON javn-nsetti; cf. also OCz. noci “by night’; Blg. noščė, wd: Li. nakcià beside nákti, id.
noktiór (noktór) “by night, the evening be- fore; next night Per. cf. nahar ‘breakfast’; Gk. cf. nüktor “by
851
night; Alb. nesër, dial. nestër ‘tomorrow’; Lat. cf. noctur-nus ‘nocturnal; W neithiwr and neithwyr “last night’; Br. neizcer, neizür, neichur, id.; Cor. nyhewer, id.
nokeio ‘injure, kil. See neK- (1) Skt. na$áyami ‘destroy’; OPer. cf. -na0ayatiy, 3s. ‘injures’; Lat. noceo, -ere, v. ‘harm’; Li. cf. nasle, f. ‘widow’
noKus ‘bearing, burden, weight; weighing, oppressive’. Cf. neK- (2) Hitt. nakkus & nakkis “heavy, difficult, impor- tant; W (?) nog, m. ‘stoppage’; OCS (and com. Sl.) -nosü (vü-nosü, iz-nosü) (convey- ance’; Li. oaëus adj. ‘productive’; cf. našta, f. burden, weight, produce’; Latv. nasta, f. id.
nóm-, long o-gde form of nem- (2). WP II, 330. Cf. nomos (1) below Per. nàme "book epistle’; Gk. cf. nómáo (1) ‘share’; Li. náoma, f. rent beside nàomoju, oti “let, hire out; Latv. noma, f., nomåju, at, as Li.
nõmn-, nómen- (form of ono-mnm, q.v.) “name”. Aphetic in Skt. naman, n.; OPer. nàman-; Per. nàm; Oss. nom, pl. námtà, Dig. non, pl. nändtä; Du. cf. noemen, v. ‘to name’; Fris. neame, id. (A type *nomo(n) is represented in Go. (and general Gmc.) namo, etc. Cf. ang, ono). WP I, 132
nomos (1) “part, share, division, decision. Cf. nem- (2) Vedic námah ‘pasture’; Per. cf. name "book epistle’; Gk. nomós, nomé, m.f. ‘pasture; abode; district; nómos, m. “law, custom": Lat. cf. numerus, 1, m. ‘number’; Li. namai, mpl. ‘house’; Latv. nams, m. id. (and 'scullery). WP II, 330
nomos, is (2) 'turn, bend'. Cf. nemo and nemos (1) Skt. cf. namráh ‘crooked’; Gk. nomeis, pl. ‘ribs of ship’
nondh- (nndh-) “press, swell, drive’. Cf. WP II, 316 and nnt- (nont-) Per. cf. (z-gde?) nad “increase, abundance"; Hitt. cf. nannahi, v. ‘drive, march’; OCS noZdo, noditi, v. ‘thrust, force’; Pol. cf. nedza, Cz. nouze, R nuždà ‘misery, need'; cf. also
nokeió — noruos, à
10
15
20
25
30
35
40
45
852
(if w. *-n-) Vedic nàdhamanah ‘importunate’; nadhitáh ‘oppressed, needy’. (For OHG nen- den “dare”, ge-nindan, sv. “be eager”, and ON nenna "be keen on, woo', see nnt-)
(noqu-, ultimate theme of type *noktis, *nokts, q. v. and cf. nqu-, nqut- Cf. Hitt. nekuc-; Gk. nukheüo “watch through the night; nukhth-émeron, n. "a day and a night', and the vocalism of nüx 'night'; Li. nakvinti, inf. “put up for the night; nakvyne *night's lodging")
nor- (1) “penetration; inside; interior; depth’. Cf. nið, enor-, ner- (2), nerteros. WP IT, 333 OCS norü, m. “den, hole, cave, nest’; nora, norja, f. id.; R norà, f. ‘burrow’; Ukr. norà, f. “hole; source, spring’; Li. náras *diver-bird', cf. naroms, adv. “under water; narüs, adj. “Table to sink”
nor- (2) “join, joint Per. narà ‘partition wall (?); Sw. nara, f. 'car- penter's nail; Li. narys, gs: -io, m. “joint, link, member’; Latv. naris ‘fetter on horse's leg; fetlock'; nàrs (with syntactical length), m. 'vice, clamp'
nor- (3) (?) “narrow, close’. Gmc. fr. *nor- quos in view of Finn. LW, but see noruos (2) below Oss. cf. nárág ‘narrow’; OS naru, OE nearu “narrow, close, strict; OE nearu, gs. we, s. ‘danger’; Finn. (LW) narka, adj. ‘narrow’; Li. (?) narávas, m. (archa
```


## [2026-09-07T20:48:31.670Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB pox ===\"; grep -n \"poxtan\\|puxtan\\|pōxtan\\|pac-\\|paz-\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB2 ===\"; grep -n \"pwhtn\\|pwxtn\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-07T20:48:31.743Z] TOOL RESULT

```
=== NYB pox ===
1520:framän [plm'n'] order, command 12). 11310 ete.; ~ būt hac... + inf. it was ordained, decreed by ... that 3611-13; ~ dätan to issue orders, to order 191 ete. passim; ~ patigraftan to comply with an order 38!; — be spoxtan to disregard, disobey an order 3? (cf 12"); v. also
5856:‘sprhm: spram ‘spwr: spurr ‘spwryg: spurrik ‘spwxt: spoxtan ‘spyd-: spét ‘spyd-pr: parr
6807:spih(a)r, spahir: spihr sp6z-: spoxtan
7403:sipoxtan: spoxtan
=== NYB2 ===
3498:spöxtan [spwhtn'] spož- [spwe-] to throw, to drive 2974-%; bg ~ to defy, to dis- regard 3? (cf spož-kar); to drive out 66". — Prth: Arm. lw. spuž-em ‘to postpone, to delay, to procrastinate’; MPrs (lw.) *spwxt (A-H I); Paz. pres. spož-; NP sipoatan svpoz-.
```


## [2026-09-07T20:48:43.332Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^peqõ\\|^peqō\\|^peq-\\|pequo\\|peqo\\|poqos\\|^peqtos\\|^peqtis\" IEC.txt | head -20\necho \"---\"; grep -n \"poxtan\\|paz-\\|'cook'\" IEC.txt | grep -n -i \"cook\" | head -20"
}
```


### [2026-09-07T20:48:43.407Z] TOOL RESULT

```
12617:peKu ‘small farm-animal for shearing, head of cattle’. Cf. peKo, etc. Skt. pá$u, pasúh, n & m ‘head of cattle’; Av. pasus, m. id.; Oss. fís, Dig. fus, s. ‘sheep’ be- side fos, s. (cattle, fr. *peKu-); OLat. pecu, pl: -ua, n. “cattle, sheep’; Lat. pecus, gs: -oris, n. id., Umb. pequo, pl. ‘small farm-animals'; Go. Tabu, n. ‘money’, OHG fëho, fihu, OS
12681:pendó — pequo, ið
12692:pequios, om, à Alb. pjékull, f. *mudbrick; Lat. coculum *kettle; firewood'; Latv. pekle, f. “glow, heat'; cf. Li. (metath.) képalas, m. ‘loaf; Latv. ceplis *baking-oven'; tile-firing'; OCS and com. SI. peklo ‘hell. Cf. pequo
12697:pequos (poqu-) (1) ‘cooking’, etc.; ‘cooked, baked, roasted, ripe’. Cf. pequó Skt. pakváh, adj. (&cooked', etc. -kv- unusual); Per. cf. pacak ‘dried dung’; Arm. (vowel am- big.) hac "bread (fr. *pequtis?); Gk. cf. pépon, n. ‘darling’ beside Myc. a(r)to-poqo- ‘baker’; Alb. pjekë, f. ‘roast’; Lat. (vowel ambig.) co- quus, gs: -1, m. (cook; OCS pekü, m. ‘heat, glow'; Blg. pek, m. id.; Li. cf. kep-, cpds.
12698:pequos, à, om (2) *neat, attractive; pet, dar- ling'. (Same as (1)?) Skt. cf. (+-8-) pakah ‘young, artless; young child or animal, pet'; Gk. pépon, n. ‘pet’; Lat. (ambig.) pecülium (“private possession'. Infl. (?) of type peKu, q.v.); (LW in Alb. pekül, m. ‘darling, favourite); Per. (?) pak “pure, clean’; Cz. péče, OCz. peka, péCé, f. “care, attention'; R cf. o-péka, id. (Uncertainly w. nasal infix: Pol. piekny, Cz. pěkný *pretty?)
12699:pequtis ‘baking, cooking, roasting, ripen- ing’. Cf. pequo and next Skt. paktíh, f. id.; Gk. pépsis, f. id.; Lat. cf. prae-cox, gs: -cocis & -coquis ‘prematurely ripe; OCS (and com. Sl.) pesti, f. “oven; Arm. cf. hac, i-st. ‘bread’; Li. cf. inf. képti (w. metath.) ‘to bake’; Latv. cept, id. beside cepetis, s. ‘roast’
12702:pequos (poqu-) — peri (per, per-)
---
```


## [2026-09-07T20:48:48.122Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12676,12706p' IEC.txt"
}
```


### [2026-09-07T20:48:48.169Z] TOOL RESULT

```
penos, us (food; protection'. (Semantics of OCS xrana in both senses. Cf. also dopon-). WP II, 25 Per. cf. panah ‘refuge, protection’; Gk. (z-gde) cf. -pne in óm-pné, f. ‘corn, food"; Lat. penus, gs: -oris & -üs, m. also penum, penu, n. ‘food — supply; Gmc. as a Lat. LW in fenea 'barley- groats, porridge'; cf. also Lat. pin-guis, adj. (fat, coarse, fruitful', fr. *pen-gui-, cf. gui-, etc.); Li. pénas, m. “food; Den, Eti, v. ‘feed’
penque ‘five’; penqutis ‘group of five Sk. pañča; Av. pañča; Per. panj (pang); OPer. cf. pa(n)Ca-; Oss. fondz; Tokh. A pä, B pàn-; Arm. hing, gs: hngi, i-st.; Myc. (?) pe(n)gato- (said of a chariot); Gk. pénte, cpds. penta-; Cypr. peísei; Alb. péns, pesë; Lat. quinque (w. assimilated conss.); Osc. pump-; Gaul. pinpe- (in pinpe-donum ‘cinquefoil’, for *pimpe- dulon, beside pinpe-tos "DÉI pempe-, id.; Mir cóic, Ir. cúic, cúig (with assim. conss.); OBr. pimp; Br. pemp; W pump; Cor. pymp; Go. Dmt OE fif; OHG fimf, finf; Du. vijf; ON fimm beside fimt, f. col. ‘fivesome’; OCS cf. peti (and com. Sl.) (*fivesome', hence *five); Li. penki; Latv. pieci, id. WP IT, 25ff.
penqueros 'fivesome'. Cf. penque Arm. cf. hinger-ord ‘fifth’; Osc. pumperias, fpl.; Gall-Lat. *pe(m)peracium Ca shrub’ (?). Misspelt peper-?); MIr. cóicer, m.; Ir. cúigear, m.; OHG (and com. Gmc.) fingar (finger. Here?); Li. penkeri (fivesome'; OCS cf. pẹ- torü, id. (fr. *penqutero-) beside petero, id.
penqutis ‘set of five’. Cf. penque, etc. Skt. panktíh, £.; Osc. cf. pomtis, adv. 'quin- quies’; ON fimt, f.; OCS peti (and com. SI. "Deet: Li. cf. penkti, adj. f. “fifth” beside pen- ketas, m. 'fivesome
penqutos “fifth” S kt. cf. pacata, f. 'fivesome'; Tokh. B pinkte, pinkce “fifth”; Gk. pémptos, id.; Alb. i pésté, id.; OLat. quinctus, Lat. quintus, id.; MIr. coíced id.; Ir. cf. cüigeadh, m. “fifth, as a frac- tion’; OBr. pimphet; W pummed; Br. pemped, pempved; Cor. pumpes, id.; Go. fimfta-, cpds.
pendó — pequo, ið
15
20
25
30
35
40
45
920
id.; OHG fimfto; ON fimti; OCS petyj (and com. Sl.); Li. peñktas, id.; Latv. cf. piekt- in piekt-diena (“fifth-day” i.e. “Friday”); beside piektais “fifth?
pent- ‘go, track, trace, seek, proceed; foot- print, heel; back'. WP IT, 27. Cf. pont- Oss. fándín, v. "want Tänd Dig. fändä, s. ‘desire’; fándág ‘road’; Gk. cf. pémpo (Csend', if for *pent-squo, see sequo); Go. finpan, v. (find and com. Gmoc.); MHG vinden, id. cf. vinde, sf. ‘find’; OS cf. bi-, undar-findan, v. ‘search, explore’; OE findan, sv. 3. ‘find, meet, arrange, consider’; ON finna, v. “find”; R pjà- tit, v. ‘send back, repe? beside OCS peta, f. "heel R pjatà, Cz. pata, f. id. and OCS petíno ‘spur’; R opjat, Cz. z-pét ‘back’; R pjatnó, n. ‘spot, stain’; Li. péntis, gs: -ies, f. *butt-end; heel; pa-? “crust of bread'; pentinas, m. (spur: OCS petino); at-pent, -pentai, -pefic ‘back, again’; Latv. piets, gs. id. /back-edge — of axe’; piete, f. id.; cf. also piesis footstep’, for *pents-)
pequios, om, à Alb. pjékull, f. *mudbrick; Lat. coculum *kettle; firewood'; Latv. pekle, f. “glow, heat'; cf. Li. (metath.) képalas, m. ‘loaf; Latv. ceplis *baking-oven'; tile-firing'; OCS and com. SI. peklo ‘hell. Cf. pequo
pequmn- (pequno-) “baking, firing, cooking; cooked, etc. See next Skt. pakvannam, n. ‘cooked food'; pacanah, adj. “cooking-'; Gk. pémma, n. ‘cooked food, cake’; pépanos, adj. ‘ripe’; Alb. i pjékém, i pjékun, adj. ‘roasted, baked, cooked, ripe’; Cz. pecen, gs: pecnu, m. ‘batch’; pečen, adj. pp. “baked'; Li. (metath.) kepimas, m. “bak- ing’; kepinys, gs. -io, m. “baked food’;
pequó, ið "bake, cook, roast, open. WP II, 18 Skt. pácami, v., pakváh, adj. id.; Av. pač- ‘boil; burn’; Per. pazidan, pp: puxte ‘cook’; Oss. ficin, Dig. ficun, v. ‘cook, roast; Tokh. AB pak-, B pákw-, as Skt.; Hitt. cf. sam-pukki, s. ‘gruel’; Gk. péptó, pésso, v. as Skt., peptós, adj. ‘cooked, baked, ripe’; Alb. pjek, aor: poqa, v. ‘bake, ripen’; Lat. coquo, ére, v. as Skt.; Osc. Umb. *pop- (in the Lat. LW popina, f. ‘cook- shop’: Lat. coquina); Br. pibi, pp: pobet, v.
921
as Skt.; W pobi, id.; Cor. pobas, inf., 3s. fut. pep, v. id.; OCS peko, pesti (and com. SL), id.; Li. (metath.) kepü, képti, id.; Latv. cepu, cept, v. id.
pequos (poqu-) (1) ‘cooking’, etc.; ‘cooked, baked, roasted, ripe’. Cf. pequó Skt. pakváh, adj. (&cooked', etc. -kv- unusual); Per. cf. pacak ‘dried dung’; Arm. (vowel am- big.) hac "bread (fr. *pequtis?); Gk. cf. pépon, n. ‘darling’ beside Myc. a(r)to-poqo- ‘baker’; Alb. pjekë, f. ‘roast’; Lat. (vowel ambig.) co- quus, gs: -1, m. (cook; OCS pekü, m. ‘heat, glow'; Blg. pek, m. id.; Li. cf. kep-, cpds.
pequos, à, om (2) *neat, attractive; pet, dar- ling'. (Same as (1)?) Skt. cf. (+-8-) pakah ‘young, artless; young child or animal, pet'; Gk. pépon, n. ‘pet’; Lat. (ambig.) pecülium (“private possession'. Infl. (?) of type peKu, q.v.); (LW in Alb. pekül, m. ‘darling, favourite); Per. (?) pak “pure, clean’; Cz. péče, OCz. peka, péCé, f. “care, attention'; R cf. o-péka, id. (Uncertainly w. nasal infix: Pol. piekny, Cz. pěkný *pretty?)
pequtis ‘baking, cooking, roasting, ripen- ing’. Cf. pequo and next Skt. paktíh, f. id.; Gk. pépsis, f. id.; Lat. cf. prae-cox, gs: -cocis & -coquis ‘prematurely ripe; OCS (and com. Sl.) pesti, f. “oven; Arm. cf. hac, i-st. ‘bread’; Li. cf. inf. képti (w. metath.) ‘to bake’; Latv. cept, id. beside cepetis, s. ‘roast’
pequtos (poqutos) ‘cooked, baked, roasted, ripened’. Cf. pequð, etc. Skt. cf. (inf.) paktum (‘to cook’, etc.); pača- táh, pp. (“cookeď’, etc.); Per. puxte, id.; Gk. peptós, adj. id.; It.-Alb. i pjekté, id.; Lat. (assim. consonants) coctus, adj. id.; W (assim. cons.) poeth, adj. ‘hot; Br. poaz, adj. ‘cooked’; Cor. poth, adj. ‘scorching’; Li. (metath.) kép- tas, pp. ‘cooked, fried, roast; Latv. cf. cepe- tis, s. ‘roast’. Cf. (?) Arm. amet, Let ‘solid’, fr. *som-pequtis?)
per, per-, see peri. WP II, 30 An intensive px. in Lat. per-bonus, etc.; W er- glyw ('attentive', cf. clyw, s. ‘hearing’, to *Kleu-, etc.); OHG firi- in firi-wiz, -wizzi, n. ‘portent; curiosity’; OS firi-wit, id.; Li. per- aükstas, etc.
pequos (poqu-) — peri (per, per-)
20
25
30
35
```


## [2026-09-07T20:48:58.254Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD pdf page 45 (printed 40) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==45' incoming/FFD/FFD_pages_faseng.txt | head -40\necho \"=== FFD grep puxtan ===\"; grep -n \"pu[xh]tan\\|paz-\\|pačaiti\" incoming/FFD/FFD_pages_faseng.txt | head"
}
```


## [2026-09-07T20:48:59.167Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS grep pac/puxt ===\"; grep -n \"pu[xh]t\\|paz\\b\\|pačitan\\|pactan\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T20:48:59.510Z] TOOL RESULT

```
=== FFD pdf page 45 (printed 40) ===
awk: cannot open "incoming/FFD/FFD_pages_faseng.txt" (No such file or directory)
=== FFD grep puxtan ===
ugrep: warning: incoming/FFD/FFD_pages_faseng.txt: No such file or directory
```


### [2026-09-07T20:48:59.560Z] TOOL RESULT

```
=== SNS grep pac/puxt ===
5862:                                                        .*-*-    :   puxtag :»»*>'*         •
15891:pexak 143/6                puxtag 137/4                      raftar 225/12          rfistaglh 234/16
```


## [2026-09-07T20:49:04.654Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5850,5875p' SNS_pages.txt\necho \"=== find FFD ===\"; ls incoming/ 2>/dev/null; find . -iname \"*FFD*\" | head"
}
```


### [2026-09-07T20:49:04.719Z] TOOL RESULT

```
                                                3                         :   ^-j 'j*)'* o-      1
                                                                                                     )
                                                                                                                                          .^uw,^^,^ :parda2Sd; w^ ^
try                                  UjtiMtfUtaUti'j                                                                                        Uc^UtebMU                           »tj




                                                         ^m«S           p.        119

                                                                                                                                               *
                                                                                                                                                                         -t/ts
                                                        .*-*-    :   puxtag :»»*>'*         •




                                TA/T^      (GJVPE.      64) /pac         :   L / 1-          j
                                                                                                                                                       •o-^'J^.jIji :fraz:0"
                                                                                                                             (Aim. 974)fra->^ fra-/fra-:t-
                                                                                       Xwtu
                                 iAiWb.    897)p3sav/paratu                   :        L.             ^^'j.,^^,,,, nQn fraz:                                        ^^
             WIT** -T\/1T^                (J? J >** -^jr** '^'^ J»)          <J<   (0


                                                                                                                  •t/H«*         IWVtfrf.tWWf/lri l., wwr
=== find FFD ===
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
./incoming/FFD
./ocr/FFD
./incoming/FFD/FFD_pages.txt
./incoming/FFD/FFD_asmaneketab.pdf
./incoming/FFD/FFD_pages.txt.pages
```


## [2026-09-07T20:49:09.736Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==45' incoming/FFD/FFD_pages.txt | head -50"
}
```


### [2026-09-07T20:49:11.011Z] TOOL RESULT

```
[pdf page 45]
0 11 ان دار
بیوسیدن

( بیوسید» ماده ماضی جعلٍ است. از مادهٌ مضارع ساخته شده است.

: بیوس < فارسی میانه 02789 < ایرانی باستان 0211-0809-8*. برای 2 -> آرای. 041
پیشوتد فعلی است.

4-8 صورت اصلی ۳۵9 است. 4 پیش از ۶ به 5 بدل و در آن ادغام شده است. 5
برای ساختن مادهٌ آغازی از ريشه به کار رفته است. ريشةٌ 0304 به معنی «بوی بردن»
است. واژةٌ «بوی» فارسی دری از 210 گرفته شده است.

پادن, پاییدن

پاد <ج فارسی میانه 034 « ایرانی باستان 03-12*. برای 18 -> آراست. ریشهٌ ۳3 به
معنی «پاییدن» است.

پای < فارسی میانه 03 < ایرانی باستان 03-72*. 8 نشانه‌ای بود که از ريشه ماده
می‌ساخته است.

«پاد» از رواج افتاده و «پایید»» مادهٌ ماضی جعلی» به جای آن به کار می‌رود.

پالودن

پالود < فارسی میانه 0310 «ایرانی باستان 0272-40-18*. برای 2 آراست. 1022
پیشوند فعلی است. 5 صورت ضعیف ريشةٌ 42۷ است» به معنی «دویدن». خود
«دویدن» هم از ريشةٌ 42 آمده است.

پالای < فارسی میانه 0818 < ایرانی باستان 8/ر08۳۵-439-8*. 24 نشانه‌ای بود
برای ساختن مادةٌ مضارع. از ريشه» 43 صورت بالاندةٌ ریشهٌ 49۷ است. [
ی چخت ۰
پخت < فارسی میانه 001 « ایرانی باستان 2-12م*. برای 1۵ -> آراست. 081
صورت اصلی 02۵5 است» 1 پیش از ۲ به # بدل شده است.
پز< فارسی میانه 022 < ایرانی‌باستان -022*.برای 2 -> آرای.2 به‌جای آمده‌است.
```


## [2026-09-07T20:49:17.080Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 586 590 594 598; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -25; done"
}
```


### [2026-09-07T20:49:18.357Z] TOOL RESULT

```
=== leaf 586 ===
هایست ۰ بر وزن داست ء بمعنی بقا
وثبات کرد و باینده مائد؟ .9
بای ستو د- با ای قرشت مضوم‌پواو
و رای بیقطةٌ زده» تاسازست؛وآن کمینه تین
سازها باشد . ۱
پایسته » بروزن‌دانته. بقا کردموپاینده
و دایمی وگو ند ۱ . 3
پای ستتن - کنابه ازفوت واستواری
پای شیب بائین‌فرشتتحتانی‌رسده
و بیای ابجد زده تام‌عقبه‌ایست بجهت رمی‌جمرات
که عگ از اعمال حج‌است :
وتوقف کردن باشد .
(۱) خم ۳ : وسول .
٩‏ رك : یایستن.
بود نو شرع برتواند داشت
دین نیامد ز دست تابودست .
6
پای فشردن - .کنابد از استواری
و بات قدم ورزیدن باشد - و کنابه‌اژاستاد کی
کردن در سودا هم حست .
پایگاد » بستی‌یکار است. وآن‌مردی
باشد که چون تحصیلدار بجابی آبد او زر از
را تیز گویند .
پایگاه بروزن جایگاه ؛ معروف‌است
که کفش کن و صف نعال- وجای منوران باشد
=== leaf 590 ===
پایه حوص - بنتح حای بی نقطه | همیشه و پبوسته و جاوبد و دام و جاوبد بودن
سکون واه و صاد نقطه دار . کنانه از جای هم هت ؟ .
و انام برکث دیزان را گوشد - و کنایه از
ایام پیری هم هست. و با زای فارحی هم اعدم
, اس :۹
هاقیفن * » بروزن ساییهن . بمضنی‌دو پایین پرستی - کنابه از اطات
نظر داشتن و چشم برنداشنن باشد - و بمنی | وبندکی و خدمتکاری باشد .
ومتزلت باشد .
بیان دوم
در بای فارسی با بای فارسی مشتمل بر پنج ات
۳ پرا کنده کردن باشد ب 9
لیلسی ‏ بنتح ارل و سکون ثانی و لام
مصموم ۷ می‌نقطه رده فربی داشد که از بان
خداث و دوغن و دوشاب سا ند ۰ ء ی کونند
اشکنه ای باشد که از دوغن وپیاز بردغن بربان
کرده وآب ونان خشات سار ند ۰
فیلیبا اه با بای فارسی بروزنده سیماه
بلغت زند ویازند (۲) جامه وقبارا گونند.
مك - بکر اول بر وزن خشتك »
خوشه کوچك ازخرما و انگور باشد. و یاره ای
ازخوشه را نیز گوبند.
بلفت زند و پازند (۱) پر را کوبند که درمقابل
حجوان است 1 ۱
لمر لش « بروزن اندیشده .عنی پرشان
۱ .. پی يك بوسه کرد پايةٌ حوض بسی کشتم تو دل دربا نکردی . خاقانی‌شروانی.
=== leaf 594 ===
آیان ششم
در بای فارسی باخای نقطه دار مشتمل بر بست و سه لفت
م4 بفتح اول,سکون‌ئانی» بمعنی‌خوش دیگر - وبفتح اول بمعنی پهن و پخش باشد؟ا
ویه باشد » وان بممنی په‌په وخوئ‌خونی | مثلآنکه چیزی در زیرپای آدمی‌با حیوان‌دبگر
استد ]را بعربی‌بخ بخ‌خوانندوطوبی لكومرحبابكت | ا هرزبر چیزی دیگر پهن‌شده باشد گویندهپخت
توا ریت ین اد اس هبارق 1 شد و پخش کردبد:9 .»
کویند « چهاریخ است ت» یمنی چهار پولو است پخته جوش ۰ , بضم‌اول و جیم بروزن
وبکس اول کلمه ایست که سکه وکربه را بدان | کهنه بوش, شراییراگوبند که آنرابادوایی چند
برانند و دور کنند » و باين معتی بفتح اول حم . جوشالیده باشتد » و آن چنان است که شیر
درست است چه با سطبخ قافیه کرده‌اندا , انگور نفیس را با گوشت بر فربه دردیگ هکنند
اتیت ع یکرارل وبای فارسی,آست | وباقی ادوبه را ثم کوفنه در کیسه کنند ودردیگه :
که شخصی انگشنان خود را درزیر بفل دیگری ] اندازند وبجوشانند با کوشت مپراشود» بعد ازآن
بنوعی حرکت دهد کهآن شش بخنده افئد؟ . | صاف کرده بنوشند .
بت « نم اول وسکون الی وفوفانی: بخته خود » نم اول و خا وواو
ماضی پختن است ولگه را بزگوینه سلقً عمدوله و رای بی نقطهٌ ساکن » کدا و کدابی
خواه اسب برکسی زند و خواه آدم و حیوادات | کننده را گویند ‏ و یممنی داماد هم آحده است
درمیان فری‌میدانی چه‌باشد پخپخو در هری پخلوچه گوبند ازصفیر واز کبیر
۱ ۱ بازی‌ساحب فرهنک منظومه. «لت نامه».
۴ - رك : پختن . ۴ - کیلکی یز  .۳22‏ ۵ - لبز از انباع و مزاوجة
بخت است : ۱
وفت است کز فراق نو وز سوز اندرون آتش‌در افکنم بهمهرخت وپخت خوش .
«حافط مصحح زو ی ۱۹۷ تن وحاشه».
۵ پاشن ی اول » پهلوی ۳۱06120 » اوستا و سانسکریت 26 (طبخ). کردی
0 , افتایی 0208۷۷1 , استی ‏ ۲1605 , 1610] , بلوچی 0۵688 . 029۳28 , وخی
0 , شغئی و سریکلی 0628۳0 : ارمنی 2۳۷04 (ران خوله ی «امشق ۷۸۵ کیلکی
=== leaf 598 ===
پر قتتکاد ۱ سباعان بالفکنیدوبرای
قرشت زده ؛ بستی فبول کننده و فرماببردار
وهقر و معترفی باشد .
فد فلقی» بروزن دد جردن » بمعنی‌فبول
کردن و اعتراف نمودن باشد ۴ .
فد لته » بروزن دل برده: بمعنی‌افرار
واعتراف کرده و قبول نموده باشد ۴ .
فیرح بی +زن وزیس ۰ قبول کننده را
کوینن - وامرباینممنی‌هم‌هست,منی‌قبولکن ۴ .
پدیر | ۴ بر وزن اصیر اه روان‌شو نده
و پیش رونده - و سخن‌شنونده وفرمانبرداروقبول
کنندهرا کومند,چه پذیرابی بمعلنی فرمان‌برداری
باشد - و بمعنی هیولی نیز بنظر آمده است که
در برابر صورت است ۵ - و نضیر مفبول حم
هست که‌فبول کرده شده‌باشد.- وبمعئی پیشواز(۱)
واستقبال هم گفته‌اود ۹
پذپرش ۱ ه تم اول و کر رابع
)۱ چش : پشوا.
وسکون شین نقطه دار پسعنی قبول و فرمان -
برداری باشد .
ماضی پذیرفتن است عنی فول کرد؟ 3
پذبر فتکار با کاف بالف کشیده
و برای قرشت زده » بمعنی فرمان بردار - وقبول
کننده - و مقر و معثرف باشدب و سردار ورش .
سفید قوم را نیز کوبند۷ .
```


## [2026-09-07T20:49:35.731Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 592 593 594 595 596; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -oE \"^[0-9]{3}$|[۰-۹]{3}|بقیه در صفحه[^\\n]*|^[0-9]{3}\" | head -5; done\necho \"=== full leaf 594 tail ===\"; awk 'BEGIN{RS=\"\\f\"} NR==595' BQT_v1_pages.txt | tail -20"
}
```


### [2026-09-07T20:49:37.267Z] TOOL RESULT

```
=== leaf 592 ===
۰۱۲
۰۲۸
۲۸۹
۱۸۲
=== leaf 593 ===
۳۷۰
=== leaf 594 ===
۱۹۷
۷۸۵
=== leaf 595 ===
۳۷۸
=== leaf 596 ===
۵۱۸
۲۸۷
۰۱۸
۱۸۷
۱۹۰
=== full leaf 594 tail ===
اتیت ع یکرارل وبای فارسی,آست | وباقی ادوبه را ثم کوفنه در کیسه کنند ودردیگه :
که شخصی انگشنان خود را درزیر بفل دیگری ] اندازند وبجوشانند با کوشت مپراشود» بعد ازآن
بنوعی حرکت دهد کهآن شش بخنده افئد؟ . | صاف کرده بنوشند .
بت « نم اول وسکون الی وفوفانی: بخته خود » نم اول و خا وواو
ماضی پختن است ولگه را بزگوینه سلقً عمدوله و رای بی نقطهٌ ساکن » کدا و کدابی
خواه اسب برکسی زند و خواه آدم و حیوادات | کننده را گویند ‏ و یممنی داماد هم آحده است
درمیان فری‌میدانی چه‌باشد پخپخو در هری پخلوچه گوبند ازصفیر واز کبیر
۱ ۱ بازی‌ساحب فرهنک منظومه. «لت نامه».
۴ - رك : پختن . ۴ - کیلکی یز  .۳22‏ ۵ - لبز از انباع و مزاوجة
بخت است : ۱
وفت است کز فراق نو وز سوز اندرون آتش‌در افکنم بهمهرخت وپخت خوش .
«حافط مصحح زو ی ۱۹۷ تن وحاشه».
۵ پاشن ی اول » پهلوی ۳۱06120 » اوستا و سانسکریت 26 (طبخ). کردی
0 , افتایی 0208۷۷1 , استی ‏ ۲1605 , 1610] , بلوچی 0۵688 . 029۳28 , وخی
0 , شغئی و سریکلی 0628۳0 : ارمنی 2۳۷04 (ران خوله ی «امشق ۷۸۵ کیلکی
مها 0۵2 رد : ابا (آنی) ؛ طبخ کردن » بش ترم کردن .
بقیه ازسفحة ۳۹٩‏
۵ 0 - نم اول مخفف پوچ» پوك. میان نهی :
هستم ز شر چونار ز داله بتیرمه وزخیر پچ میانه چواندر بهار سیر.
سوژلی سمرفندی. «لفت نامه»۰
```


## [2026-09-07T20:49:52.973Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v3 شوربا ===\"; grep -n \"شوربا\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== v3 سکبا/سیکبا ===\"; grep -n \"سیکبا\\|سکبا\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head -10\necho \"=== v4 نانوا ===\"; grep -n \"نانوا\\|نانبا\" incoming/BQT/BQT_v4_pages.txt | head -10\necho \"=== v4 ناربا ===\"; grep -n \"ناربا\" incoming/BQT/BQT_v4_pages.txt | head -5\necho \"=== v3 سپیدبا ===\"; grep -n \"سپیدبا\\|سپیدبای\" incoming/BQT/BQT_v3_pages.txt | head -5"
}
```


### [2026-09-07T20:49:53.109Z] TOOL RESULT

```
=== v3 شوربا ===
7496:شوربا است که آب گوشت پشته باشد .
7547:‎sd ٩‏ شوربا ‎dy -۶* Ae)‏ سلحشور . ‎oN‏ از: شور ۳* ش(اسم‌مصدر).
7553:رك: شورباج ورك: الطبیخ ص۲۸ .
7924:وعلاج باشد . کویند - ریم اول و تحتانی مجهول » شوربا
14346:مانند جاروپ بندند و بدان ‎OT‏ وآهار و شوربا
=== v3 سکبا/سیکبا ===
incoming/BQT/BQT_v4_pages.txt:8893:و خارخك را هم گنته‌اند و آن خاری است مه نسکبا؟ - بنتح اول » آتی عس را
=== v4 نانوا ===
7688:که درزمینهای نمناك روید؛ وبسنی کوبنداقحوان | کاند تا بخواب روند۷ - و مخفف نانوا هم‌هست.
7725:۹ ر3 : نانوا. ۴ < بانخواء (همم.) ۴ - «نان ونمکدان شکتن ۰
7744:* نافوا - بسکون سوم *< نانبا « فولرس ]] ۶۱۲۸۹ » از : نان وا ( پسوند پا
7747:سوی نانوا شد سبك با عنان بدان شاخ زرین ازوخواست نان
13113:( نانپا) آید , قی: کردی نان پان 804278 - 280 (نانواخانه) * ژابا ص ۶۱۹ » وظ. اژین‌فبیل
=== v4 ناربا ===
5348:بممتی‌زنارباشد وآن رشته اشت که کفار بر کردن | بسیاری هت وازآن سوراخهاآوازهای گوا کون
18370:خوریرا کویند - ودوغواص را نیز گفته‌اند که وم | ودینارباشد .
=== v3 سپیدبا ===
```


## [2026-09-07T20:50:00.813Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v4 7740-7750 ===\"; sed -n '7740,7750p' incoming/BQT/BQT_v4_pages.txt\necho \"=== v4 13105-13120 ===\"; sed -n '13105,13120p' incoming/BQT/BQT_v4_pages.txt\necho \"=== v3 7540-7560 ===\"; sed -n '7540,7560p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-07T20:50:00.885Z] TOOL RESULT

```
=== v4 7740-7750 ===
بمنی کودیی که برقفرات پشت است, ومثل گودی میان دوکفل فربه اسب ...؟ وهمین صحیح‌است
(ر3 : مازن) ر3 : ناو4 . ‎٩‏ - رك4 : ناویدن . *- در رشیدی آمده است . از :
- تلو (هم.) ۳+ آنیدن (پسوند مصدر متمدی ) » متعدی « ناویدن » (ع.م.)

* نافوا - بسکون سوم *< نانبا « فولرس ]] ۶۱۲۸۹ » از : نان وا ( پسوند پا
قی *کردی 038 - 228 ( بان پزخانه ) « ژابا ی 2۱۹ > ؛ پزنده و فروشندة نان :

سوی نانوا شد سبك با عنان بدان شاخ زرین ازوخواست نان

بدو تانوا کفت کرا بها تدانم , نیارمش کردن رها . . .

=== v4 13105-13120 ===
وابردن « بفتح بای ایجد بر وزن وا هم هت ۱۴

۱ -قی : تهرانی ۷2 ( در تداول زنان » بهنگام اظهار تعجب ).

۴ < باز (ه.م.) پیشوند قعل. رك : اسشق ص *۲4 ۰ ۴ همان پیشرند قل
است که قبلا مذکور شد .

۴ -رك : وان . یزرا از با #پان ) صورت پسوند در تأنوا
( نانپا) آید , قی: کردی نان پان 804278 - 280 (نانواخانه) * ژابا ص ۶۱۹ » وظ. اژین‌فبیل
است : پیشوا ۰ ۱ - ظ. برساختهٌ فرقه‌آذرکیوان . ۷ - شکل لپجه‌یی‌است که در
بیتی از میرنظمی‌آمده « اسشق ۱۶۷ + کبری ۷2۸17208 ( سخن گفتن).کاشانی ش81۷۵ ۰
کردی ۷۵۹10 « اسشق ۰۶۱۶۷۲ خواداری ۷8188 (کفتن) « سألنامة کلپایگان 4۷ رك: واج»
واژه . ورك : واتگر. ۸ -رك : جهانگیری » رشیدی ؛ ورك : والگر .

: - ‏-ظ. از: وا ( ۳ باز [ کعاد] )۳ تر ( تقضیلی ). رك : وا‎ ٩

=== v3 7540-7560 ===

‏کس له بیند که تشنگان حجاز ‏ بلب آب شور کرد آیند . * کلتان ۳۷ ۰.

‏۷ - تا ‎alg‏ زلفك شوریده را بخط ‎past‏ فتاد گرد همه شهر شور وشر .
ءمار؟ مزوری «لفت فری ۰.۰۱4۳ ۸ -(عر)مالح (بکسرسوم) » بمعنی شور(لمکین)وآب‌شوره
و مالج (بفتح‌سوم) ممرب ماله (گلکاران) است .

‎sd ٩‏ شوربا ‎dy -۶* Ae)‏ سلحشور . ‎oN‏ از: شور ۳* ش(اسم‌مصدر).

‏* فورالدی وفورالیدن - ‎ee‏ اول وفتح دال , از: ‎satya) Gash gull base‏
مصدری متمدی) [ُرك : خوریدن] بهیجان آوردن | تحريك کردن 6 ابچاد آشو بکردن.

‏شور با - از : شور ‎LA eb)‏ (آش) , ممرب ‎OT‏ شوریاج (ه.م.) وشوربه «لفس» .
رك: شورباج ورك: الطبیخ ص۲۸ .

[pdf page 99]
شورء

شود ۵ - با میم وح رکت مجهول,بمنی
کوه باشد و بعربی جبل خوانند.
```


## [2026-09-07T20:50:40.104Z] TOOL CALL #31: Bash

```json
{
 "command": "pdftoppm -f 388 -l 388 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg388 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg388.png"
}
```


### [2026-09-07T20:50:42.140Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66598 Sep  7 16:50 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg388.png
```


## [2026-09-07T20:50:44.855Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg388.png"
}
```


### [2026-09-07T20:50:45.378Z] TOOL RESULT

```

```


## [2026-09-07T20:50:45.375Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T20:51:12.303Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN apricot ===\"; grep -n -o \"apricot[^|]\\{0,700\\}\" KLN_1966.txt | head -3\necho \"=== KLN biscuit ===\"; grep -n -o \"biscuit, n[^|]\\{0,500\\}\\|bis-cuit[^|]\\{0,400\\}\" KLN_1966.txt | head -3\necho \"=== KLN pumpkin ===\"; grep -n -o \"pumpkin[^|]\\{0,600\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-07T20:51:13.783Z] TOOL RESULT

```
=== KLN apricot ===
3240:apricot,  n.  —  F.  abricot,  fr.  Port,  albricoque  fr. Arab.  al-barqdq  fr.  al-,  ‘the’,  and  upamixiov, Grecized  form  oih.  praecoquum,  ‘apricot’,  neut. of  praecoquus  =  praecox,  ‘early  ripe’,  for which  see  precocious.  See  also  cook.  For  the interchangeability  of -c  (=  -k)  and  -t  cp.  havoc (fr.  OF.  havot),  bat  (fr.  orig.  bakke),  and  the words  milt  and  milk ,  ‘milt  of  fishes  .
4539:apricot  (from  orig.  apricock),  havoc  (fr. OF.  havot),  and  the  English  words  milt  and  milk, ‘milt  of  fishes'.
9092:apricot,  bis¬ cuit,  concoct,  cotta,  culinary,  decoct,  dyspepsia, kiln,  kitchen,  melon,  pepo,  pepsin,  peptic,  preco¬ cious,  pucka,  pumpkin,  quittor,  terra  cotta,  and the  second  element  in  crumpet,  drupe. Derivatives:  cook,  tr.  and  intr.  v.,  cook-er,  n., cook-ery,  n.
=== KLN biscuit ===
=== KLN pumpkin ===
7790:pumpkin  (bot.)  — OF.  citrole  (earlier  form  of  citrouille),  fr.  Olt. citruolo  (It.  cetriolo),  a  diminutive  formed  fr. Late  L.  citrium,  ‘a  kind  of  gourd’,  fr.  L.  citrus. See  Citrus  and  cp.  next  word.
9092:pumpkin,  quittor,  terra  cotta,  and the  second  element  in  crumpet,  drupe. Derivatives:  cook,  tr.  and  intr.  v.,  cook-er,  n., cook-ery,  n.
16479:pumpkin’.  See  cucurbit, gourde,  n.,  the  monetary  unit  of  Haiti.  —  F. gourde,  prop.  fern,  of  the  adjective  gourd,  ‘numb, stiff,  heavy’,  fr.  L.  gurdus,  ‘dull’,  which  is  of Iberian  origin.  Accordingly  gourde  prop,  de¬ notes  ‘a  heavy  or  thick  coin’.  Cp.  next  word, gourdy,  adj.,  swollen  in  the  legs  (veter.)  —  OF. gourdi,  ‘benumbed,  swollen’,  pp.  of  gourdir, fr.  gourd.  See  prec.  word  and  -y  (representing F.  -/).
```


## [2026-09-07T20:51:14.291Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT barqūq/aprikose ===\"; grep -n -i -o \"barq[uūa]q[^|]\\{0,500\\}\\|Aprikose[^|]\\{0,400\\}\" LKT.txt | head -5\necho \"=== AFM برقوق ===\"; grep -n \"برقوق\" AFM_pages.txt | head -5\necho \"=== PLA برقوق ===\"; grep -rn \"برقوق\" incoming/PLA/*.txt 2>/dev/null | head -3; ls incoming/PLA/ | head"
}
```


### [2026-09-07T20:51:15.760Z] TOOL RESULT

```
=== LKT barqūq/aprikose ===
751:Aprikose  mismas  (s.  hier  Nr.  1471) heißt];  hieraus  sp.  albaricoque,  alber- coque,  pg.  albricoqtie,  alboquorque,  prov. aubricot,  frz.  abricot,  it.  albicocco,  al- bercocco,   siz.  varcoccu;  engl,  apricot.
754:Aprikose,  schwed. aprikos;  russ.  abrikos,  öech.  aprikozn. —  Ferner  infolge  Betonung  der  ersten Silbe  mit  romanischem  Suffix  sp.  cilber- chigo,  it.  albergese  'Art  Pfirsich  oder Aprikose'  [dagegen  DEFREMERY  in JAs  (1869)  I,  531,  wohl  ohne  Grund]. [Dozy  Oost  1—4.  DE  67/68.  Hobson- Jobson  33.  Devic  DEt  2/3.  ML  6712. Kluge  20.
1428:Aprikose  und  Verwandte,  s.  hier unter  harkük  Nr.  247];  hieraus  russ. orjuk  [über  den  Wechsel  von  i  und  u im  Tk.  s.  hier  Nr.  526  u.  552  Ende] 'trockene  Aprikosen',  urjuk  'gelbe  Eier- pOaume'.    [Gorjajew  241.
2415:Aprikose,  Malum  armeniacum';  hieraus bulg.  kajsij,  serb.  kajcija  'Aprikose,  Apri- kosenbaum'; rum.  cais  'Aprikosenbaum', cai'sa 'Aprikose',  caisiü  'aprikosenfarben'. [Bern  SlEtWb  469.
3396:Aprikose',  doch  auch  'Pflau- me' [Lammens  Faruk  Nr.  1284];  hieraus mit  ar.  Art.  und  folijender  Assimilation pg.  ameixa,  amexa  'PHaume',  it.  amos- cino,  [mit  häufigem  Wechsel  von  m  und b]  abostno  'Pflaumenbaum'.  [DE  189. Eguilaz  258  (jedoch  aus  lat.  myxa,  gr. \i\)la  abgeleitet!).
=== AFM برقوق ===
=== PLA برقوق ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-07T20:51:28.359Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 740-760 ===\"; sed -n '745,760p' LKT.txt\necho \"=== KLN biscuit ===\"; grep -n -o \"bis.\\{0,3\\}cuit[^|]\\{0,400\\}\" KLN_1966.txt | head -5\necho \"=== KLN pompon/pepon ===\"; grep -n -o \"pompon[^|]\\{0,300\\}\\|pepon[^|]\\{0,300\\}\" KLN_1966.txt | head -8"
}
```


### [2026-09-07T20:51:29.853Z] TOOL RESULT

```
=== LKT 740-760 ===
[Aus  pers.  bar  'Last'  Horn  NpEt  S.  36, Nr.  156  und  gtr  s.  hier  Nr.  158]  'Last- pferd'. Hieraus  bind,  und  daraus  anglo- ind.  bargeer  'Soldat  der  irregulären Kavallerie,  der  nicht  Eigentümer  seines Pferdes  und  seiner  Waffen  ist,  welche vielmehr  der  Regierung  gehören'.  — Im  vulg.  tk.  verderbt  zu  bejgir  oder begir  'Lastpferd',  hieraus  rum.  beghir 'Pferd'.    [Hobson-Jobson  69.
245.  Pers.  bäri:
'Wenigstens'  [aus  pers.  bär  'Mal'  Horn NpEt  S.  36,  Nr.  157  und  i  der  Einheit, also:  'ein  Mal'],  ebenso  tk.  barg  und bar  gm;  hieraus  rum.  barem,  barim  'we- nigstens', bulg.  serb.  bare  'wenigstens, dennoch'.  [Mikl  SlEtWb  7.  Bern  SlEt- Wb 44.
246.  Hiud.  bari-bibi:
[Aus  bind,  ban,  fem.  zu  barä  'groß', und  hlbl  'Frau,  Dame']  'große  Dame'; im  angloind.  ist  das  Wort  zur  Bezeich- nung der  Dame  geworden,  die  bei  einer Gesellschaft  den  Vorsitz  verlangt:  hirra- beebee.  [Hobson-Jobson
247.  Ar.  barkfik:
[Aus  dem  lat.  praecocium  'das  F'rühreife' über  gr.  rrpaiKÖKKiov,  irpaiKÖKia,  upeKÖK- Kia,  ß^piKOKKa,  s.  Lammens  Färük  S.  364 Anm.;  das  ar.  Wort  hat  übrigens  die Bedeutung  'Pflaume'  erhalten,  während die  Aprikose  mismas  (s.  hier  Nr.  1471) heißt];  hieraus  sp.  albaricoque,  alber- coque,  pg.  albricoqtie,  alboquorque,  prov. aubricot,  frz.  abricot,  it.  albicocco,  al- bercocco,   siz.  varcoccu;  engl,  apricot.
21
[Ar.  barnija.
ndl.  abrikoos,  dtsch.  Aprikose,  schwed. aprikos;  russ.  abrikos,  öech.  aprikozn. —  Ferner  infolge  Betonung  der  ersten Silbe  mit  romanischem  Suffix  sp.  cilber- chigo,  it.  albergese  'Art  Pfirsich  oder Aprikose'  [dagegen  DEFREMERY  in JAs  (1869)  I,  531,  wohl  ohne  Grund]. [Dozy  Oost  1—4.  DE  67/68.  Hobson- Jobson  33.  Devic  DEt  2/3.  ML  6712. Kluge  20.
248.  Ar.  barnija:
Topf,  Krug  aus  Glas',  auch  burmja [wohl  aus  pers.  bärm  'Gefäß'  Horn  Np S.  48,  Nr.  209].  Hieraus  die  roinan. Gefafsnamen  sp.  albornia,  sp.  p.tr.  berne- gal, kat.  atbiirnia,  siz.  burnia,  altit. vernicato,  venez.  vernicale,  genues  rer- nigau,  brünia,  prov.  hernigau.  [L)E  73. GrSVociSic  229.  Eguilaz  116.  ML  1048 und  1222.  ,
249.  Ar.  barräda:
'Gefäß  mit  2  Henkeln,  um  darin  Wasser abzukühlen'  [vom  Vh.  barrada  'kalt, kühl  machen'  s.  hier  Nr.  241];  hieraus mit  ar.  Art.  sp.  albarrada  'Wand  aus trockenen  Steinen',  pg.  albarrada  'Vase für  Rosen  oder  andere  Blumen'  [in dieser  Bedeutung  wohl  Kontamination mit  ar.  warräda  aus  ward  'Rose'], 'Mauer  aus  losen,  also  trockenen  Steinen' [Constancio  Dicc  43  c].    [DE  68/69.
250.  Ar.  bnrrakäu:
'Grober  Stoff  oder  Mantel  daraus'  [Wohl aus  Kamelhaar,  vgl.  Dozy  DV  68  sq.); hieraus  mlat.  barracänus,  frz.  harracan 'grober  Stoff',  bouracan,  sp.  kat.  barra- gan,  sp.  pg.  barragana,  it.  baracane; engl,  huckram  [mit  Angleichung  an  buck, das  auch  im  Stotfnamen  bucJtskin  vor- liegt], barchant,  ndl.  barkan,  mhd.  bar- chät,  dtsch.  Barchent,  Berkan;  russ. barham  'Samt',  barakun,  barkan  'Bar- chent'; klr.  barchat  'Samt',  barakan 'Art  Wollstoff';  poln.  barakan,  poln. cech.  barchan  'Barchent'.  [Dozy  Oost  24. DE  237.  ML  941.  Kluge  38.  Gorja- jew  12.  Bern  SlETWb  44.  Lammens Rem  55/56.
=== KLN biscuit ===
5064:biscuit,  n.  —  F.  biscuit,  fr.  L.  bis  cactus,  ‘twice cooked’  (whence  also  It.  biscotto),  fr.  bis, ‘twice’  (see  prec.  word),  and  coctus,  pp.  of  co- quere,  ‘to  cook’.  See  cook,  n.,  and  cp.  bisque, bise,  n.,  a  dry  and  cold  north  wind.  —  F.,  fr. Frankish  *bisa,  which  is  rel.  to  OHG.  bisa,  G. Bise,  ‘bise’,  OHG.  bisdn,  ‘to  run  about’  (said of  cattle  atta
5067:biscuit.
9092:bis¬ cuit,  concoct,  cotta,  culinary,  decoct,  dyspepsia, kiln,  kitchen,  melon,  pepo,  pepsin,  peptic,  preco¬ cious,  pucka,  pumpkin,  quittor,  terra  cotta,  and the  second  element  in  crumpet,  drupe. Derivatives:  cook,  tr.  and  intr.  v.,  cook-er,  n., cook-ery,  n.
9519:biscuit.  — Fr.  earlier  crakenel,  metathesis  of  F.  craquelin, ‘cracknel’,  fr.  MDu.  crakelinc  (Du.  krakeling), fr.  craken,  ‘to  crack’.  See  crack, cracovienne,  n.,  a  Polish  dance.  —  F.  (short  for danse  cracovienne,  fit.  ‘a  Cracow  danse’),  fem. of  cracovien,  ‘of  Cracow’,  fr.  Cracovie,  ‘Cracow’, fcracy,  combining  form  meaning  a  certain  type of  ‘rule’  or  ‘governmen
30203:biscuit  baked  in  the  form  of  a  twisted ring.  —  G.  Brezel,  fr.  MHG.  brezel,  prezel,  fr. OHG.  brezitella,  brecedela,  fr.  Eccles.  L.  *bra- chitella,  dimin.  formed  fr.  *brachitum,  ‘any¬ thing  baked  in  the  form  of  twisted  arms’,  fr.  L. brachium,  ‘arm’;  cp.  ML.  bracidelli  (pi.),  It, bracciatello,  OProven?.  brassadel.  See  brace,  n. and  dimin.  suff.  -el.
=== KLN pompon/pepon ===
29567:pompon,  n.,  an  ornament  of  feathers.  —  F.,  prob. of  imitative  origin.
30995:pompon,  fr.  L.  peponem,  acc.  of pepd,  ‘mel¬ on,  pumpkin’,  fr.  Gk.  ttstccov,  ‘melon’,  prop, ‘cooked  by  the  sun,  ripe’,  from  the  stem  of niiczziv,  ‘to  cook'  (see  peptic  and  cook) ;  so  call¬ ed  because  it  is  not  eaten  until  it  is  quite  ripe, pun,  n.,  a  play  upon  wor
```


## [2026-09-07T20:51:44.146Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '30990,30997p' KLN_1966.txt\necho \"=== KLN kiln/kitchen/cuisine ===\"; grep -n -o \"kiln,  n[^|]\\{0,300\\}\\|kitchen,  n[^|]\\{0,300\\}\\|cuisine,  n[^|]\\{0,300\\}\" KLN_1966.txt | head -5\necho \"=== SKT pumpkin/apricot/biscuit ===\"; grep -n -o \"PUMPKIN[^|]\\{0,300\\}\\|APRICOT[^|]\\{0,300\\}\\|BISCUIT[^|]\\{0,300\\}\" SKT.txt | head -6"
}
```


## [2026-09-07T20:51:44.432Z] TOOL CALL #37: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:51:45.667Z] TOOL RESULT

```
Derivatives:  pulvinate-ly,  adv.,  pulvinat-ion,  n. pulvinus,  n.,  the  cushionlike  base  of  a  petiole  (hot.) —  L.  pulvinus,  ‘cushion,  pillow,  elevation’,  of uncertain  origin.  Cp.  pulvinar,  pulvinate,  pulvil¬ lus.  Cp.  also  pillow.
pulwar,  n.,  a  kind  of  light  river  boat  used  in Bengal  (India).  —  Hind,  palwar. puma,  n.,  the  cougar.  —  Sp.,  fr.  Quechua. pumice,  n.,  porous  volcanic  rock  used  as  an  abra- *  sive.  —  ME.  pomis,  fr.  OF.  pomis  (also  ponce, whence  F.  ponce),  fr.  Late  L.  pdmicem,  acc.  of pomex,  prop,  a  dialectal  (prob.  Oscan)  form  of L.  pumex,  ‘pumice  stone’,  which  is  rel.  to  spuma, ‘foam’ ;  see  foam  and  cp.  pounce,  ‘a  fine  powder’, spume.  It.  pomice,  Sp.  pomez.  Port .  pomes,  ‘pum¬ ice  stone’,  also  derive  fr.  Late  L.  pdmicem.  E. pumice  has  been  assimilated  in  form  to  Latin piimicem.
Derivatives:  pumice,  tr.  v.,  pumic-ed,  adj., pumic-er,  n.
pumiceous,  adj.,  of  the  nature  of,  or  resembling, pumice.  —  L.  piimiceus,  ‘of  pumice  stone’,  fr. pumex,  gen.  piimicis.  See  prec.  word  and  -ous. pummel,  n.  and  v.  —  A  var.  of  pommel, pump,  n.,  a  device  for  raising  water.  —  ME. pompe,  pumpe,  fr.  MDu.  pompe,  fr.  Sp.-Port. bomba,  ‘pump’,  which  is  of  imitative  origin.  Cp. pompier.
Derivatives :  pump,  tr.  and  intr.  v.,  pump-er,  n. pump,  n.,  a  kind  of  low  shoe.  —  Prob.  meaning orig.  ‘a  shoe  used  for  pomp’,  fr.  LG.  pump, ‘pomp’,  fr.  L ,pompa  \  see  pomp.  For  sense  devel¬ opment  cp.  G.  Pumphose,  ‘knickerbocker’,  orig. ‘trousers  worn  on  festive  occasions’, pumpernickel,  n.,  Westphalian  dark  rye  bread.  — G.,  orig.  an  abusive  word  compounded  of pum- pern,  ‘to  break  wind’  and  Nickel,  ‘bumpkin’, prop,  a  shortened  form  of  the  PN.  Nicolas.  See Nicholas  and  cp.  nickel.
pumpkin,  n.  —  Fr.  earlier  pompion,  pumpion,  fr. MF.  pompon,  fr.  L.  peponem,  acc.  of pepd,  ‘mel¬ on,  pumpkin’,  fr.  Gk.  ttstccov,  ‘melon’,  prop, ‘cooked  by  the  sun,  ripe’,  from  the  stem  of niiczziv,  ‘to  cook'  (see  peptic  and  cook) ;  so  call¬ ed  because  it  is  not  eaten  until  it  is  quite  ripe, pun,  n.,  a  play  upon  words.  —  Prob.  shortened fr.  It.  puntiglio,  ‘a  fine  point’,  dimin.  of  L.  punc- tum,  ‘point’;  see  point,  n.,  and  cp.  punctilio.  For sense  development  cp.  F.  pointe,  ‘conceit,  witty phrase,  quip’,  and  pointe  d'une  epigramme,  E. point  of  an  epigram.
Derivatives:  pun,  intr.  and  tr.  v.,  punn-er,  n., pun-ter,  n.
puna,  n.,  a  desert  region.  —  Sp.,  fr.  Quechua. punch,  n.,  a  tool.  —  Shortened  fr.  puncheon. Derivatives:  punch,  v.  (q.v.),  punch-y,  adj., punch-i-ness,  n.
=== KLN kiln/kitchen/cuisine ===
9878:cuisine,  n.,  the  kitchen;  style  of  cooking.  —  F., ‘kitchen’,  fr.  Late  L.  cocina,  a  var.  of  coquina, ‘kitchen’,  fr.  coquere,  ‘to  cook’.  See  cook  and cp.  kitchen.
20681:kiln,  n.,  a  large  oven.  —  ME.  kilne,  kulne,  fr.  OE. cylene,  cylne,  fr.  L.  culina,  ‘kitchen  .  See culinary.
20733:kitchen,  n.  —  ME.  kuchene,  kichene,  kichen,  fr. OE.  cycene,  fr.  L.  cucina  [whence  also  It.  cucina, OProven?.  cozina,  F.  cuisine,  Sp.  cocina,  and MDu.  cokene  (Du.  keuken),  OHG.  chuhhina (MHG.  kitchen,  kiiche,  G.  Kiiche),  Dan.  kjek- ken],  dissimilated  var.  of  L.  coquina,  ‘ki
=== SKT pumpkin/apricot/biscuit ===
```


### [2026-09-07T20:51:45.673Z] TOOL RESULT

```


```


## [2026-09-07T20:51:53.941Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%AE%D8%AA%D9%86",
 "prompt": "Give the full Persian etymology of پختن (poxtan/puxtan): Middle Persian form, Proto-Iranian, Proto-Indo-European root, present stem paz-, and any cited sources."
}
```


## [2026-09-07T20:51:54.915Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/apricot",
 "prompt": "Give the full etymology chain of \"apricot\": Latin praecoquum/praecox, Greek, Arabic al-barquq, Spanish/Catalan/Portuguese, French, English dates."
}
```


### [2026-09-07T20:51:58.914Z] TOOL RESULT

```
# Persian Etymology of پختن (poxtan/puxtan)

**Present stem:** پز (paz)

**Etymology chain:**
The word descends from Proto-Indo-Iranian *páčati, which comes from Proto-Iranian *pačati, ultimately tracing to the Proto-Indo-European root *pekʷ- meaning "to cook, become ripe."

**Source attribution:**
According to the Etymological Dictionary of the Iranian Verb (Cheung, 2007), this verb's lineage follows this documented path through ancient language families.

**Related cognates** across Iranian languages include Mazanderani, Baluchi, Northern Kurdish, and Yaghnobi forms, demonstrating the root's widespread presence in the language family.

The dictionary notes the verb retains meanings encompassing culinary preparation: to cook, bake, broil, make ready, and ripen.
```


### [2026-09-07T20:52:01.349Z] TOOL RESULT

```
# Etymology Chain of "Apricot"

**Latin Origin (c. 1st-2nd century):**
The root is Latin "(mālum) praecoquum," meaning "early-ripening (fruit)." This derives from "praecoquis" (early-ripe), combining "prae" (before) with "coquere" (to ripen/cook).

**Greek Intermediary:**
Byzantine Greek "berikokkia" transmitted the Latin term through trade routes.

**Arabic Development:**
The word became Arabic "al-birquq," representing the fruit's presence in Middle Eastern cultures.

**Romance Language Adaptations:**
Portuguese borrowed it as "albricoque," while Catalan developed "abercoc." These Iberian forms reflected regional trade patterns.

**French Refinement:**
The French form "abricot" eventually influenced the final English spelling.

**English Adoption (1550s):**
English initially borrowed the Catalan form as "abrecock" around the 1550s, which was subsequently "assimilated to French abricot." The fruit itself arrived in England in 1524, though the word's standardization came later. By 1906, "apricot" also became established as a color name.

This chain reveals how a Mediterranean fruit's name traveled through multiple linguistic and commercial networks before reaching English.
```


## [2026-09-07T20:52:07.988Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pek%CA%B7-",
 "prompt": "Give the reconstructed PIE root, its gloss, the derived terms (Avestan, Sanskrit, Latin, Greek), and which references are cited (Pokorny page, LIV)."
}
```


## [2026-09-07T20:52:08.547Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pumpkin",
 "prompt": "Full etymology of pumpkin: pompion, Middle French pompon, Latin pepo/peponem, Greek pepon, and dates."
}
```


### [2026-09-07T20:52:13.821Z] TOOL RESULT

```
# Proto-Indo-European Root *pekʷ-

## Reconstructed Root
**\*pekʷ-** (imperfective)

## Gloss
The root has three main meanings:
1. To crack, crush, or pulverize grain/foodstuff (possibly original Anatolian sense)
2. To cook
3. To ripen

## Key Derived Terms

**Avestan:** 𐬞𐬁𐬐𐬀 (pāka, "cook")

**Sanskrit:** पक्व (pakva); पच्यते (pácyate)

**Latin:** coquus ("cook"); coctus; coctiō

**Ancient Greek:** πέψῐς (pépsĭs); πεπτός (peptós); πέμμᾰ (pémmă)

## References Cited

- **Pokorny (1959):** Page 798 in *Indogermanisches etymologisches Wörterbuch*
- **LIV (2001):** Page 468 in *Lexikon der indogermanischen Verben* (Rix, ed.)
- **Beekes (2010):** Pages 1180-1181 in *Etymological Dictionary of Greek*
```


### [2026-09-07T20:52:51.026Z] TOOL RESULT

```
# Pumpkin Etymology

The word "pumpkin" has a fascinating linguistic journey. It first appeared in English during the 1640s as an alteration of earlier forms like *pompone* and *pumpion* (1540s). These came from French *pompon*, which derived from Latin *peponem*, ultimately tracing back to Greek *pepon*.

The Greek root likely meant "ripe," stemming from *peptein* meaning "to cook." This connects to the Proto-Indo-European root *pekw-, which encompasses concepts of cooking and ripening. The modern English "-kin" suffix was added, possibly because speakers mistook the Latin "-on" ending as a diminutive form.

Interestingly, Thomas Harriot documented that Algonquin peoples called the fruit *macòcqwer*, which produced the now-obsolete English term *macock* (1610s).

Beyond its botanical definition, American vernacular adopted "pumpkin" figuratively in the 19th century to describe either "a stupid, self-important person" or conversely, "a person or matter of importance."
```


## [2026-09-07T20:52:57.654Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA",
 "prompt": "What does Wiktionary say about the Persian word بیسکویت — etymology (borrowed from French biscuit?), pronunciation, meaning?"
}
```


## [2026-09-07T20:52:59.502Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%82%D9%88%D9%82",
 "prompt": "Give the Arabic etymology of برقوق (barqūq): what is it borrowed from (Greek praikokkion, Latin praecoquum)? What does it mean (plum/apricot)? Any Persian entry?"
}
```


### [2026-09-07T20:53:02.044Z] TOOL RESULT

```
Based on the Wiktionary page provided, here's what's documented about the Persian word بیسکویت:

**Meaning:** The entry defines it simply as a "biscuit."

**Pronunciation:** The transliteration given is "biskuit."

**Etymology:** The page does not include etymological information. While the word's form suggests a borrowing from European languages (likely French or English "biscuit"), Wiktionary does not explicitly state this on the displayed content.

**Language Classification:** It's categorized as a Persian noun and lemma, filed under the "Foods" category.

The page is notably sparse in linguistic detail—it's essentially a stub entry without pronunciation guides, usage examples, or etymological notes beyond the transliteration.
```


### [2026-09-07T20:53:05.697Z] TOOL RESULT

```
# Etymology of برقوق (barqūq)

**Borrowing Source:**
The word is "Borrowed from Classical Syriac ܒܰܪܩܽܘܩܳܐ (barqūqā), from Byzantine Greek βερικοκκῐ́ᾱ (berikokkĭ́ā, 'apricot tree'), from Ancient Greek βερίκοκκον (beríkokkon)."

The ultimate origin traces back through Latin praecoquus and Greek sources, ultimately deriving from Proto-Indo-European roots related to "cooking" (*pekʷ-).

**Meanings:**
The term has multiple regional meanings in Arabic:
- Primarily: plums
- In West Yemen, al-Andalus, Sicily, Mauritania, and Western Sahara: apricots
- In Mauritania and Western Sahara: peaches

**Persian Entry:**
The provided Wiktionary content does not include a Persian entry for this word. The document only covers Arabic, Moroccan Arabic, and South Levantine Arabic.
```


## [2026-09-07T20:53:12.558Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/biscuit",
 "prompt": "Full etymology of biscuit: Old French bescuit, Medieval Latin bis coctus / panis biscoctus, dates, and the sense 'twice-cooked bread'."
}
```


## [2026-09-07T20:53:14.944Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for بیسکویت? Give the origin tag (e.g. [فر.]) and the definition, plus any Dehkhoda note on its origin."
}
```


### [2026-09-07T20:53:17.565Z] TOOL RESULT

```
# Etymology of Biscuit

The word "biscuit" originates from the concept of twice-baked bread. According to etymological sources, it comes from Old French *bescuit*, which derives from Medieval Latin *biscoctum*, literally meaning "twice-baked." This traces back to Latin *(panis) bis coctus*, or "(bread) twice-baked."

The term was respelled in the early 19th century from the earlier form *bisket* (dating to the 16th century). The word's evolution also shows influence from cognate Italian *biscotto*, which shares the same "twice-baked" root.

**Key dates:**
- Early 14c.: *besquite*
- 12c.: Old French *bescuit*
- Early 19c.: Modern spelling "biscuit"
- 1818: U.S. sense emerges describing "small, round soft bun"

The dual-baking process was practical for preservation, making biscuits ideal for long voyages and storage before modern refrigeration.
```


### [2026-09-07T20:53:20.086Z] TOOL RESULT

```
# Farhangi Mo'in Definition of بیسکویت

According to the **Farhangi Mo'in** section, the entry includes:

**Origin tag:** [ فر. ] (French)

**Definition:** "نوعی شیرینی که خشک و کم وزن است" (a type of confection that is dry and lightweight)

There is no additional Dehkhoda note on its origin provided in this section. However, the Daneshname-ye Omumi (General Encyclopedia) section offers etymological context, explaining that the term derives from Latin *bis* (twice) and *coquere* (baked), literally meaning "twice-baked," referring to its traditional preparation method of initial baking followed by slow drying in an oven.
```


## [2026-09-07T20:53:37.445Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D8%AE%D8%AA%D9%86' --note 'page 388, root Pekw, node 3: Persian poxtan etymology (MP, PIr *pačati, PIE *pekw-, Cheung 2007)' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/apricot' --note 'page 388, root Pekw, nodes 9-10: apricot < Arabic al-birquq < Byz.Gk berikokkia < Lat. praecoquum' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pek%CA%B7-' --note 'page 388, root Pekw: PIE *pekw- \"to cook, ripen\", Pokorny 798, LIV 468' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/pumpkin' --note 'page 388, nodes 11-13: pumpkin < pompion < MFr pompon < L peponem < Gk pepon' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://www.etymonline.com/word/biscuit' --note 'page 388, nodes 6,8: biscuit < OFr bescuit < ML biscoctum, L (panis) bis coctus' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%82%D9%88%D9%82' --note 'page 388, node 9: Arabic barquq < Syriac barquqa < Byz Gk berikokkia' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA/' --note 'page 388, node 7: Mo in tags بیسکویت [فر.] = French loan' 2>&1 | tail -3\ncd /home/sfmqrb/git/rishe && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA' --note 'page 388, node 7: Persian بیسکویت entry (stub)' 2>&1 | tail -3"
}
```


### [2026-09-07T20:53:42.401Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/61f7ba78027f7ecd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ead39423c7c4b5fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb8531f22abbf083.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/daecb17339ea7bc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/237a83a89bd8f0b2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d753e3822ba7e693.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bf8434786ba1805c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/642fdf125149b64d.txt
```


## [2026-09-07T20:53:50.441Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN puxtan ===\"; grep -n -o \"puxtan[^|]\\{0,300\\}\\|pu[hx]tan[^|]\\{0,300\\}\\|pazad[^|]\\{0,200\\}\" HRN.txt | head -5\necho \"=== HRN pukhtan persian ===\"; grep -n \"پختن\" HRN.txt | head -5\necho \"=== HUB ===\"; grep -n -o \"puxtan[^|]\\{0,300\\}\\|paz[^a-z][^|]\\{0,150\\}\" HUB.txt | head -5\necho \"=== CHEUNG pac ===\"; grep -n -o \"\\*pak[^|]\\{0,400\\}\\|paz-[^|]\\{0,200\\}\" CHEUNG.txt | head -6"
}
```


### [2026-09-07T20:53:51.906Z] TOOL RESULT

```
=== HRN puxtan ===
=== HRN pukhtan persian ===
=== HUB ===
99:paz. awastan = phi. dpustan 'pregnant* Shk. p. 234.
119:paz. evar 'certain , evarth 'certainty', evarik certain
172:paz. amexta 'mixture' Shk. p. 248, phi. gumext,
194:paz. apar = phi. apar (Min. Gl. p. 18,
196:paz. apardan, apurdan^) 'to
=== CHEUNG pac ===
18906:paz- ‘to cook; to ripen; (dial.) ‘to digest, defecate’, Bal. patk/pac- 
41351:paz-, 286
```


## [2026-09-07T20:53:54.810Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18885,18930p' CHEUNG.txt"
}
```


### [2026-09-07T20:53:54.869Z] TOOL RESULT

```
Y Av. pacat (V 16.17), 3pl. ҮАУ. pacan (V 8.73), OPT. 3pl. ҮАУ. pacaiion (Yt 8.58, rep.) 

*MIDDLE PERSIAN: MMP pwx- (pret. stem) ‘to cook’ = DMMPP: 288a 

Inf.: MMP pwxtn 


*PARTHIAN: pc- ‘to cook = Ghilain: - | DMMPP: 260b, 288a 

Partic.: pres. “pcg ‘cook’, perf. pass. pwxt 

*KHOTANESE: pajs- (pas-) ‘to cook’, pach- (pas-) ‘to be cooked, digested’ || (+ 
*pari-) LKh. parvach- (parvas-) ‘to ripen’ || (+ *ui-) gvas- ‘to be digested’ = SGS: 
65, 63, 75, 32 

*SOGDIAN: BSogd. (?)рс-, CSogd. pc- ‘to cook, boil’ 

Pres.: IND. 3sg. BSogd. ’pcty, 3р1. BSogd. pc nt; Impf.: IND. 3sg. CSogd. pc’; Inf.: pret. BSogd. pwyt’ 
*CHORESMIAN: pc- ‘to cook’, ps- (pass./intr.) ‘to be cooked, become ripe’ 
= Samadi: 138 f. 

*NWIR: NP puxtan/paz- ‘to cook; to ripen; (dial.) ‘to digest, defecate’, Bal. patk/pac- 
‘to boil, cook’, past, passit/pass- ‘to ripen (of dates)’, Zaz. pewtis/pewZen-, Abz. 
powa/pec-, poc-, Abyan. päya/paj-, Anar. -ipex/ (impv.) ipez, Ham. petän/pej-, Nn. 
paxte/pez-, Qohr. päda/pic-, pac- ‘to cook’, Khuns. pez-/pet ‘to ripen; to cook’, 
Sang. (ppp.) be-piZé, Shamerz. bá-petá, Sorkh. (ppp.) pat, Lasg. Ба -pizoe ‘cooked’ 
*NEIR: Oss. I. fycyn/fyx(t), D. ficun/funxt ‘to boil, be boiled; to bake, be baked’, 
Yghn. pac-/pásta ‘to cook, bake’, Sh. pis-/päxt, Yghn. püxs-/püxta (inch.) ‘to be 


*pad 287 


boiled, ripen, etc.’, Wa. pacé-/past ‘to ripen, be cooked’, Rosh. péj-/poxt, Bart. 
pēj-/püxt, Ishk. pac-/pex(t) Wa. pac-/pact (caus.) ‘to boil, cook’, Yghn. 
püxsón-/püxsónta (sec. caus.-inch.) “о cook, bake’, Pash. pox (m.), paxá (f.) ‘ripe, 
cooked’ (*paxua-), paxláy ‘cooking’ || (+ *pati- ?) Sang, padbis-/padbext (inch.) ‘to 
pine, waste (from heat); to be purged, defecate’ 

*MISC: Par. p&c-/phök, Orm. biZ-/puxók ‘to cook’ = biZ-/biZók, puxók 

*SANSKRIT: pac ‘to cook, bake’ (RV+) = EWAia II: 64 

«PIE *pek"- ‘to cook, bake’ = LIV: 468 | Pok.: 798 

*IE COGNATES: Gr. néooo, лётто ‘I bake, cook, ripen’, Lat. coquö ‘I cook’, OCS
```


## [2026-09-07T20:54:01.271Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18865,18890p' CHEUNG.txt\necho \"=== ARY پختن ===\"; grep -rn \"پختن\" incoming/ARY/*.txt 2>/dev/null | head -5; ls incoming/ARY/ 2>/dev/null | head"
}
```


### [2026-09-07T20:54:01.366Z] TOOL RESULT

```
*NWIR: NP näzidan ‘to dissemble (as lovers); counterfeit, feign, coquet, etc.’, Gz. 
naz-/naza ‘to caress’, NP пах ‘glory, glorification; pride; coquetry, playfulness; 
delicacy’, NP nazan ‘sporting, toying (as lovers)’ 

*MISC: Arm. (LW) nazim ‘I act proudly, coquettishly, caress’, nazeli ‘lordly, 
worthy’, Georg. (LW) nazi ‘delicate beauty’ 

The root seems to be denominal: no IE etymology can be cited. 


*PIE— > LIV: — | Pok.: 
*REFERENCES: DKS: 180a, 451b; WIM II/1: 80; Gharib: 234 


*pat ‘to cook’ 

*AVESTAN: YAv. pac- ‘to cook’ || (+ *fra-) ‘to boil away’ || (+ *ham-) ‘to cook’ 
= Liste: 32 

Pres. them.: IND. 3sg. YAv. ham.pacaiti (Y 62.7), INJ. med. 3sg. YAv. pacata (Y 9.11. rep.), SUBJ. 3sg. 
Y Av. pacat (V 16.17), 3pl. ҮАУ. pacan (V 8.73), OPT. 3pl. ҮАУ. pacaiion (Yt 8.58, rep.) 

*MIDDLE PERSIAN: MMP pwx- (pret. stem) ‘to cook’ = DMMPP: 288a 

Inf.: MMP pwxtn 

=== ARY پختن ===
incoming/ARY/ARY_pages.txt:4561:پختن» پخت / ۱۵۷
incoming/ARY/ARY_pages.txt:9230:۱ بازگشت به: گرپختن.
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-07T20:54:06.905Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"پختن\" incoming/ARY/ARY_pages.txt | head -20\necho \"---- context of first hits ----\"; sed -n '4555,4570p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-07T20:54:06.969Z] TOOL RESULT

```
4561:پختن» پخت / ۱۵۷
9230:۱ بازگشت به: گرپختن.
---- context of first hits ----
3 داریا برهان قاطم + ۳۶۶
انگلیسی (0لقاا8۸/0)«شاید) ‏ 80002
یادداشت.
۱- این واجریشه با واجربشه هند و اروپایی -۳11* ,-۳۸7* (۳* (به چم "خوراکد" و "پرورد") خویشی نزدیکه
[pdf page 156]
ی ۱
پختن» پخت / ۱۵۷
دارد (واژه‌های انگلیسی ۲000 ,۳8810 و واژه‌ی آلمانی ۳۲7۳۳8188۲ از اين واجریشه آمده‌اند).
۲ معنی واژه‌های ژرمنی و لاتین این فهرست: خوراکك دام.
۳ معنی واژه یونانی این فهرست: گله» شبان؛ گرسفند پاء
اوستایی (/89742): ۰ ]2۸6117 2۸۳ آلمانی کهن ((02701 104 ط[0): ۱
پارسی باستان (7ل۳8۳874 0ا0): 007 0 ,)2 ۱
۱ ۰ 8850718 آلمانی (2۷م: ۳۵۵۷ ,۵5 ۱
پهلری (1ماتل۸ط): ۳۸0 انگلیسی کهن (8۸01/30 0۵12)از لاتین)
اوستی (0598776): ۰ 310171۸ ,ات5161 درن
کردی (80/5ل): 20 انگلیسی (0ل5لا8(70): 00
```


## [2026-09-07T20:54:13.512Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /pdf page 156/,/pdf page 158/' incoming/ARY/ARY_pages.txt | head -60"
}
```


### [2026-09-07T20:54:14.837Z] TOOL RESULT

```
[pdf page 156]
ی ۱
پختن» پخت / ۱۵۷
دارد (واژه‌های انگلیسی ۲000 ,۳8810 و واژه‌ی آلمانی ۳۲7۳۳8188۲ از اين واجریشه آمده‌اند).
۲ معنی واژه‌های ژرمنی و لاتین این فهرست: خوراکك دام.
۳ معنی واژه یونانی این فهرست: گله» شبان؛ گرسفند پاء
اوستایی (/89742): ۰ ]2۸6117 2۸۳ آلمانی کهن ((02701 104 ط[0): ۱
پارسی باستان (7ل۳8۳874 0ا0): 007 0 ,)2 ۱
۱ ۰ 8850718 آلمانی (2۷م: ۳۵۵۷ ,۵5 ۱
پهلری (1ماتل۸ط): ۳۸0 انگلیسی کهن (8۸01/30 0۵12)از لاتین)
اوستی (0598776): ۰ 310171۸ ,ات5161 درن
کردی (80/5ل): 20 انگلیسی (0ل5لا8(70): 00
بلو چی (71حتاملم8): ۸6 ,۶۸۹۸6 دانمارکی (57//(م0): ۳005
افغانی (پشتر) (//۷4۲۵/۸: با۳۸3۸۲ سرئدی (3178015[7): 00
تخاری ۸4 (۸ [(۸ل7۸لظ70): 2 هلندی (لل07). 0
نخاری 8(۰8 ۵ 70727۸)+ ۱/۹ اسلاوی کهن (514۲7۳ بل نالا 00):
سانسکریت (54۸/5707): 23۸
۸۲۸۸ ,۶۵6۸7 لهستانی (54ل۳07): 2
ارمنی (۵04ا۸(48۸): 7 روسی (891407/): 5 7807
بونانی (02520): چکه (ل۲280): 2
58 ۳۵55572 ,23781 بلفاری کهن (7(ملمتاناه): 20
لاین ‎ :)700(‏ صربی (1427ق887): اد نی
5 ,۲001585 ,کتاتا00 اسلواکی 5-0740): اش
۹ فرات (:0/ق6: ,60181308 ب85اا6 یترانی (مانمنابم: ۳۸۸۹ ,7000
اسپانیایی (33/(//88:. 00613۸ ,0068 ایرلندی کهن 17/577 صا0):
ایتالیایی ((۸ته7): 0 ۸ ,۷۷8۷ ۱
رومانی ((8۷/۸4۸(14): اد ناه ولزی (7ل8ا8): 0 708
پرتغالی (۳07700295): ۰ ۲۵718۳۸ پرتونی (/87670): 0۸7۸
ایسلندی کهن 5۳4/01047107 )+ آلبانی (/14مهقلم: ۳
هه ای
ساکسونی کهن (/(54200 0ا0): 0

[pdf page 157]
۵۸ بدا
پسگشت‌ها زان 13339 ناه
8 00ص همم 00/5
0۱۳۵8 7 4 (00۵) . ۹ و اقلا
3 رقطانت) :ما08 برهان قاطع : ۱ ی
8 (۲۵) :18 2نق ۸۸۸

یادداشت.

معلی این واژه در ارمنی: ران خوکك.
اوستایی (/4۷8874): ۳۸ ایسلدی کهن (010۸2نی5 صاه):
پارسی باستان (لفای۶2۶ ۰:۵2 ۴1۳۸۸ ۱:۱3
پهلوی (1ا7ل۳۸): نورس کهن (۸0785 0): را ابا

,]۴ ,۳17۸۹ ,812۸3 ساکسونی کهن (542000 ۰:02 ۲۸0۸

اوستی (0558716): ,۲102 فریزی کهن (۷لفادلغ7 صان): ند زود را
کردی (080[54): 3 دا آلمانی کهن (028۸4۸۸ 10/4 صا0):

بلوچی (0241ا.ا8): 8 ,71717 ,۲17 3 دبا
افغانی (پشتو) (۸۳0/۸1): شا آلمانی (/08/0/۸): ند ابا
تخاری ۸ (۸ 4( 7۸ل70). ۳۸ انگلیسی کهن (معنا800 ام 1۸08
تخاری 8 (8 ۸(۷ل7۸ل/70): 3 د ۱2۲۸ انگلیسی (0ق5لا0/(ت): ندز ابا اد ]
سانسکریت (84۸/۶۹//7): ۰ ۳118۸ بال۳172 دانمارکی (0۸۸۷18]4): 3۸30
ارمتی (۸/2۸1۸۷): ماش سرئدی (878015/7): 1۸38
یونانی (05510): 3 لدن ۱ نروژی (4(۷ا۵ ۵/08۳8 ۲۸۲ ,3۸33
لائین (۸710ل): ۳ هلندی (7ل007): ۷۸۵8۸
```


## [2026-09-07T20:54:27.285Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW coquo ===\"; grep -n -o \"coquo[^|]\\{0,400\\}\" LEW_1910.txt | head -3\necho \"=== SKT cook ===\"; grep -n -o \"Cook, to [^|]\\{0,300\\}\\|Apricot[^|]\\{0,300\\}\\|Pumpkin[^|]\\{0,300\\}\\|Biscuit[^|]\\{0,300\\}\" SKT.txt | head -6\necho \"=== FSD apricot ===\"; grep -n -o \"apricot[^|]\\{0,300\\}\" FSD_vol1.txt | head -3"
}
```


### [2026-09-07T20:54:28.746Z] TOOL RESULT

```
=== LEW coquo ===
=== SKT cook ===
1825:Biscuit.  (F.-L.)     See  Oook.
=== FSD apricot ===
10121:apricot
22436:apricot* plam,  n.  A   narrow,  Chinese  tree  (Ami/pdGfusrimoniQ.orlts somewhat  astringently  flavored  durable  fruit:  Introduced  in the  United  States  about  1SS0,  and  cultivated  on  the  Pacific coast.  Its  fruit  is  fiat,  grooved,  and  from  1   to  2   inches long,  with  a   smooth  bro
22436:apricot.—  Japanese  a.,  a   tree  (P.  mume)  like  the common  apricot,  having  narrower  and  longer-pointed  leaves and  small  yellow  hard-  and  dry-fleshed  fruit  clinging  to  the pitted  stone  and  of  little  value:  cultivated  In  Japan  for  its fragrant  flowers,  and  recently  introduc
```


## [2026-09-07T20:54:33.802Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"COOK[^|]\\{0,350\\}\\|APRICOT[^|]\\{0,350\\}\\|PUMPKIN[^|]\\{0,350\\}\\|Pumpion[^|]\\{0,250\\}\" SKT.txt | head -8\necho \"---\"; grep -n -i -o \"apricot\\.[^|]\\{0,300\\}\" SKT.txt | head -3\necho \"--- cook ---\"; grep -n -i -o \"cook\\. *(L[^|]\\{0,300\\}\" SKT.txt | head -3"
}
```


### [2026-09-07T20:54:35.190Z] TOOL RESULT

```
---
21934:apricot.    (Arab.) def  art     Sec  Al-  (.0.
--- cook ---
```


## [2026-09-07T20:54:39.938Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i -o \"Apricot[^|]\\{0,400\\}\" SKT.txt | head -6\necho \"=== 1820-1830 ===\"; sed -n '1823,1828p' SKT.txt"
}
```


### [2026-09-07T20:54:41.407Z] TOOL RESULT

```
21934:apricot.    (Arab.) def  art     Sec  Al-  (.0.
21946:apricot,  ar-tich4
23470:apricot
=== 1820-1830 ===
Bird.  (E>  M.  E.  briJ  (the  r  being shifted);  A.S.  brii/J,  a  bird.csp.  the  yotuig of  birds.     Perhaps  allied  to  Brood.
Birth.  (E.)     Sec  Bear  (i).
Biscuit.  (F.-L.)     See  Oook.
Bisect.  (L)     Sec  Beoant.
Bishop.  (L. -Gk.>     Sec  Soopa.
Bismuth,  a  melal.  (G.)  G.  bismuth\ albo  Si|m:1i  wismmt,  wi^smui^  tuiisMUth. Orii^in  uncertain.
```


## [2026-09-07T20:55:07.093Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/WLD/ 2>/dev/null | head; echo \"---\"; find . -iname \"WLD*\" | head"
}
```


### [2026-09-07T20:55:07.152Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
---
./WLD_band3.txt
./incoming/WLD
./incoming/WLD/WLD_Bd2_pages.txt
./incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf
./incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf
./incoming/WLD/WLD_Bd1_pages.txt
./incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt
./incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt
```


## [2026-09-07T20:55:12.730Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"nasu.p[äa]k\\|peq\\^u\\|coquo\\b\" incoming/WLD/WLD_Bd2_pages.txt | head -10\necho \"=== search page 17 area ===\"; grep -n \"pacaiti\\|paca-ti\\|pekʷ\\|peq-\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T20:55:12.789Z] TOOL RESULT

```
1126: einfaltig*", s. Boisacq 769 a 1),        av. nasu-paka~ „Leichen(teile) kochend, ver-
=== search page 17 area ===
1119:     Ai- pdcati.,             pacaiti ,,kocht, backt. brat** (=lat. coqiio^ cymv. pobi., alb.
```


## [2026-09-07T20:55:15.471Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1110,1140p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T20:55:15.518Z] TOOL RESULT

```
KZ. 35, 594 widerspricht lautlich und in der Bed.                                 — Nichts mit pechis hat
ai       paltsd- m. „Achsel, Pliigel,                  Seite“ usw. zu tun.              Lit.   bei   Wiedemann
aaO.,         s.   u. pdg-   „AchseP‘).
     Ygl. Curtius 163, Pickl^ 78, 473, III^ 225, Zupitza Gutt. 189 (Lit.), Ost-
 hoff Par. I 215ff. (Lit.), Palk-Torp u.faar, faks (Lit.), Tf. LEWb.^ ^x.pecu,
pecten^ pectus.


 pequ- „Kochen"\
     Ai- pdcati.,             pacaiti ,,kocht, backt. brat** (=lat. coqiio^ cymv. pobi., alb.
pjelc.,       abg.           vgl. auch lit. kepii)) ini. paksyaii: gr. nsipco', aor. conj.j^aZ;^-
 o-t: gr. ejiE'ipa^ lat. coxi', ^\xp. paktum       = lat. codim., abg. pedh; Ptc. paktd-{—
 gr. TiETixog,        lat.   coctns., cymr. poeth)^ ai. pdeyate ,,reift*S pakic'^ ..gekocht,
 reif*% pakti-          f.   .,das Kochen, gekochtes Gericht** (=^ gr. jiEipig, lat. cocti-u,
 ahg.pesth^ apr.jJectis)^ ^^*^ar-„derKochende’* (~ lat. cocior^ fern. gr. TiETuqtai)^
pakd- m.             .,das   Kochen, Backen, Reifen** (aber nicht pakd- ^ganz jung,
 einfaltig*", s. Boisacq 769 a 1),        av. nasu-paka~ „Leichen(teile) kochend, ver-
 brennend^*; arm. wahrscheinlich hac „Brot^* als "^poq^-ti- (Charpentier IF. 25,
 241      ;
              kaum z\x pa-sco.,               pa- ..Yieh weiden'^);      gr. Jteooco; att. jihroy „koche,
 verdaue''           (f'peq'^Jo.        ai.   pdeyate). ^'o-Praes,    tietitco,   utetzcov,    -ovog   ,,reif*’    (f.

 TiETiEiga         nach jiicov      :   nieiQa),   nonavov „Geback, Kuchen“; umgestelltes ^(^o-
pos   (vgl. lit. kepu) mit diss. Entlabialisierung des     (Solmsen, Sbornik,
 Portunatov; s. Brugmann I- 873, Brugmann Thumb. GrGr.^ 137) in doro-
 xoTiog (neben aoxo-noTiog) .,BrotbackeP* (iiber xeTtxd ETixa Hes. s. vielmehr      *



 Bois. 84a 1); alb. (G. Meyer BB. 8. 185.                        Wb. 341) pjek „ich backe‘^; toch.
 ’B.pyepaksii ..gekocht'^: lat. corpio, -ere ,,kochen^* (ital. kelt. A.ss. von p>eq^o
```


## [2026-09-07T20:56:03.366Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-07T20:56:03.401Z] TOOL RESULT

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


## [2026-09-07T21:01:25.580Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-388.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pek%CA%B7-\"\nWPOX = \"https://en.wiktionary.org/wiki/%D9%BE%D8%AE%D8%AA%D9%86\"\nEAPR = \"https://www.etymonline.com/word/apricot\"\nEBIS = \"https://www.etymonline.com/word/biscuit\"\nEPUM = \"https://www.etymonline.com/word/pumpkin\"\nWBAR = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%82%D9%88%D9%82\"\nWBIS = \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA\"\nABIS = \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%B3%DA%A9%D9%88%DB%8C%D8%AA/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan\",\n \"words\": \"pax, pač, pačaiti; -pâka; nasu-pâka\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\n  \"The Avestan verb is pac- (Bartholomae enters it as the root pak-, present stem paca-): \"\n  \"3sg. subj. pacāt̰ (V 16.17), 3pl. pacan (V 8.73), 3pl. opt. pacaiiən (Yt 8.58), med. pacata (Y 9.11), \"\n  \"compounded ham.pacaiti 'cooks together' (Y 62.7). It continues PIE *pekʷ-e-ti with the regular Iranian \"\n  \"outcome of the labiovelar: *kʷ > č before a front vowel (paca-), *kʷ > k elsewhere (root pak-, ppl. *pakta-). \"\n  \"The verbal adjective -pāka- 'cooking' (o-grade *pokʷo-, the same formation as Lat. coquus and Gk. -kopos in \"\n  \"arto-kopos 'baker') occurs only as a second member of compounds, e.g. nasu-pāka- of the fire that consumes \"\n  \"corpses, Walde-Pokorny II 17 'Leichen(teile) kochend, verbrennend' — nasu- 'corpse' is from PIE *neḱ-, \"\n  \"which is why the chart cross-refers to Nek 1; 'corpse burner' is a loose but acceptable rendering. \"\n  \"PROBLEM: the first form printed in the box, 'pax', is not an Avestan word. No Avestan pax is attested; \"\n  \"the x-stem belongs to the participle *paxta- (< *pakta-, k > x before t), which is Old Iranian and is the \"\n  \"preform of MP puxt, not an Avestan citation form. The printed page 358 shows 'pax, pač, pačaiti', so the \"\n  \"JSON is faithful and the odd form is Nourai's own (he seems to have mixed the participial stem into the \"\n  \"list of present forms).\"\n ),\n \"derivation_fa\": (\n  \"فعل اوستایی pac- «پختن» است (بارتولومه آن را زیر ریشهٔ pak- با ستاک حال paca- آورده): pacāt̰ در وندیداد ۱۶٫۱۷، \"\n  \"pacan در وندیداد ۸٫۷۳، pacaiiən در یشت ۸٫۵۸ و ham.pacaiti در یسنا ۶۲٫۷. این صورت‌ها دنبالهٔ *pekʷ-e-ti \"\n  \"هندواروپایی آغازین‌اند: لب‌کامی *kʷ در ایرانی پیش از واکهٔ پیشین به č و در جای دیگر به k بدل شده است. \"\n  \"صفت فعلی pāka- «پزنده» (از درجهٔ o یعنی *pokʷo-) تنها در ترکیب‌ها می‌آید، مانند nasu-pāka- که والده-پوکورنی \"\n  \"(ج ۲ ص ۱۷) آن را «سوزانندهٔ لاشه» معنی کرده است؛ nasu- «لاشه» از *neḱ- است و ارجاع نورایی به Nek 1 درست است. \"\n  \"اما صورت «pax» در آغاز جعبه واژهٔ اوستایی نیست؛ ستاک x-دار به صفت مفعولی *paxta- (از *pakta-، ابدال k به x پیش از t) \"\n  \"تعلق دارد که ایرانی باستان است و پیش‌صورتِ puxt فارسی میانه است، نه صورتی اوستایی. صفحهٔ چاپی ۳۵۸ خودِ «pax» را \"\n  \"دارد، پس این خطای چاپی/سهو خودِ کتاب است نه خطای خوانش اسکن.\"\n ),\n \"error_in\": \"book\",\n \"book_prints\": \"pax, pač, pačaiti\",\n \"correct_form\": \"pak- / pac-, pačaiti (Av.); *paxta- is Old Iranian, not Avestan\",\n \"sources\": [W, WPOX],\n \"ref_check\": [\n  {\"ref\": \"POK:798\", \"status\": \"supports\",\n   \"note\": \"Pokorny IEW 798 (POK_03.txt, form-feed leaf 31/32): \\\"pekʷ- ,kochen'; Partiz. pekʷ-to- ,gekocht'… Ai. pácati, av. pacaiti ,kocht, bäckt, brät' (= lat. coquō…)\\\" and, in the same entry, \\\"av. nasu-pāka- ,Leichen(teile) kochend verbrennend'\\\" — both of Nourai's Avestan items are on the cited page.\"},\n  {\"ref\": \"BQT:370\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' ed. Mo'in vol. 1 printed p.370 (BQT_v1_pages.txt leaf 594, identified by the footnote continuation «بقیه از صفحهٔ ۳۶۹»): Mo'in's footnote s.v. پختن reads «پهلوی puxtan، اوستا و سانسکریت pac (طبخ)» followed by Kurdish, Pashto, Ossetic, Balochi, Wakhi, Shughni and Armenian cognates. Confirms Av. pac-, not pax.\"},\n  {\"ref\": \"SYN:336\", \"status\": \"supports\",\n   \"note\": \"Buck, Selected Synonyms, printed p.336 (SYN.txt leaf 379), §5.21 COOK: \\\"belong mostly to an inherited group representing an IE *pekʷ- … Skt. pac-, Av. pač- 'cook'; Toch. pak- …; Lat. coquere\\\"; the table row 'Av.' gives pač- for 5.21–5.24.\"},\n  {\"ref\": \"FFD:40\", \"status\": \"partial\",\n   \"note\": \"Abolghasemi, ماده‌های فعل‌های فارسی دری, printed p.40 (pdf 45, FFD_pages.txt): «پخت < فارسی میانه puxt < ایرانی باستان *paxta-… صورت اصلی pakta است، k پیش از t به x بدل شده است. پز < فارسی میانه paz < ایرانی باستان *pača-». The book gives Old Iranian, not Avestan, forms — it supports the reconstruction but is not a source for an Avestan 'pax'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 819 s.v. pak-; col. 886 s.v. paka-\", \"stance\": \"supports\",\n   \"note\": \"\\\"j. pak- V. 'kochen'. Praes. 2 paca-\\\" with the citations Yt 8.58, V 9.11, V 16.17, Y 62.7 and the note \\\"ai. pácati… Pü.: puxtan\\\"; and \\\"j. paka- Adj. 'kochend'. KompE. — Zum V. pak-. — ai. °pāki- Adj., mp. °pāk, np. °bā, °vā.\\\" No entry pax anywhere in the Altiranisches Wörterbuch.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II p. 17 s.v. pequ- 'Kochen'\", \"stance\": \"supports\",\n   \"note\": \"\\\"Ai. pácati, pacaiti ,kocht, bäckt, brät' (= lat. coquo, cymr. pobi, alb. pjek…)\\\" and \\\"av. nasu-paka- ,Leichen(teile) kochend, verbrennend'\\\" (incoming/WLD/WLD_Bd2_pages.txt lines 1119, 1126).\"},\n  {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 286-287 s.v. *pač 'to cook'\", \"stance\": \"supports\",\n   \"note\": \"\\\"AVESTAN: YAv. pac- 'to cook' || (+ *fra-) 'to boil away' || (+ *ham-) 'to cook'\\\", with the same attestations; \\\"PIE *pekʷ- 'to cook, bake' = LIV: 468 | Pok.: 798\\\". Cheung knows no Avestan pax.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"puxtag; paz\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"MacKenzie's Concise Pahlavi Dictionary has \\\"pōxtan, paz- [pwhtn', pc- | M pwxtn, N ~] cook, bake\\\": the \"\n  \"past stem puxt/pōxt goes back to Old Iranian *paxta- (< *pakta-, with k > x before t, exactly as Av. -pāka- \"\n  \"keeps the k), and the present stem paz- to *pača- with the regular Middle Persian lenition of intervocalic \"\n  \"č > z. puxtag is that past stem plus the adjectival/participial suffix -ag, 'cooked'; it is the form used in \"\n  \"the Zoroastrian legal text Šāyast nē-šāyast, which is why Nourai cites Tavoosi's glossary of that text. \"\n  \"Manichaean MP spells the two stems pwx-/pwxtn and Parthian pc-/pwxt (Cheung, DMMPP 288a).\"\n ),\n \"derivation_fa\": (\n  \"مکنزی در فرهنگ کوچک پهلوی می‌آورد: «pōxtan, paz- [pwhtn', pc-] پختن، نان پختن». ستاک گذشتهٔ puxt/pōxt از \"\n  \"ایرانی باستان *paxta- (خود از *pakta- با ابدال k به x پیش از t) و ستاک حال paz- از *pača- با نرم‌شدن \"\n  \"č میان‌واکه‌ای به z در فارسی میانه به دست آمده است. puxtag همان ستاک گذشته به‌علاوهٔ پسوند صفت‌ساز -ag \"\n  \"به معنی «پخته» است و در متن شایست نه‌شایست به‌کار رفته، و برای همین نورایی واژه‌نامهٔ طاووسی را یاد کرده است. \"\n  \"در فارسی میانهٔ مانوی pwx-/pwxtn و در پارتی pc-/pwxt نوشته شده است. ادعای نورایی درست است.\"\n ),\n \"sources\": [WPOX],\n \"ref_check\": [\n  {\"ref\": \"SNS:137\", \"status\": \"supports\",\n   \"note\": \"Tavoosi, Vazhe-name-ye Šāyast nē-šāyast: the back index (SNS_pages.txt line 15891) reads \\\"puxtag 137/4\\\", and the entry itself is visible in the OCR at line 5862, \\\"puxtag … /pac\\\" with a reference (GJVPE 64). Persian OCR of this scan is poor but the Latin transliteration and the page/line reference 137/4 match Nourai's SNS:137 exactly.\"},\n  {\"ref\": \"FFD:40\", \"status\": \"supports\",\n   \"note\": \"Abolghasemi p.40 (pdf 45): «پخت < فارسی میانه puxt … پز < فارسی میانه paz < ایرانی باستان *pača-» — both Pahlavi stems that Nourai's box gives.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.69 s.v. pōxtan\", \"stance\": \"supports\",\n   \"note\": \"\\\"poxtan, paz- [APPWN-tn' < A √pḥ; pwhtn', pc- | M pwxtn, N ~] cook, bake\\\" and the cross-reference \\\"paz-, v. poxtan\\\" (PHD.txt line 547/4640). MacKenzie normalises the vowel as ō where Nourai writes u; the consonant history is the same.\"},\n  {\"src\": \"NYB\", \"where\": \"A Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\",\n   \"note\": \"grep of NYB_vol2_glossary.txt for puxtan / pōxtan / pwhtn' / paz- returns only spōxtan 'to drive out' — Nyberg's glossary covers only the texts he prints, and the verb 'to cook' does not occur in them.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"EDIV p.286 s.v. *pač\", \"stance\": \"supports\",\n   \"note\": \"\\\"MIDDLE PERSIAN: MMP pwx- (pret. stem) 'to cook' = DMMPP: 288a; Inf.: MMP pwxtn. PARTHIAN: pc- 'to cook' … perf. pass. pwxt.\\\"\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"poxtan «پختن»; bâ, vâ «ـ با ، ـ وا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"NP پختن poxtan/puxtan is the direct continuation of MP puxtan, past stem puxt, present stem پز paz-; the \"\n  \"secondary infinitive پزیدن pazidan printed in the box is built on that present stem and is registered by Mann \"\n  \"(IEC 920 s.v. pequō: \\\"Per. pazidan, pp: puxte 'cook'\\\"). The suffixes ـبا -bā / ـوا -vā continue Av. -pāka- \"\n  \"through MP -pāk: Bartholomae's own entry on paka- ends \\\"mp. °pāk, np. °bā, °vā\\\", the sequence -āk- being \"\n  \"lenited to -āg- > -ā(v)- and the initial p- voiced to b- after a vowel in composition. Mo'in analyses the \"\n  \"compounds the same way: نانوا nānvā 'baker' «< نانبا … از: نان + وا (پسوند با)» (Borhan vol. 4), and شوربا \"\n  \"šorbā «از: شور + با (آش)» 'salt broth' (vol. 3), beside سپیدبا (white broth), سیکبا (vinegar broth, sik/serkeh \"\n  \"+ bā, Arabicised as سکباج sikbāj) and ناربا (pomegranate broth); the Khāqānī couplet quoted in the box uses \"\n  \"sikbā and šorbā together.\"\n ),\n \"derivation_fa\": (\n  \"«پختن» فارسی نو دنبالهٔ مستقیم puxtan فارسی میانه است؛ ستاک گذشته puxt و ستاک حال «پز» paz-. مصدر «پزیدن» که \"\n  \"در جعبه آمده مصدری ثانوی است که بر ستاک حال ساخته شده و مان (فرهنگ تطبیقی هندواروپایی، ص ۹۲۰ ذیل pequō) آن را \"\n  \"«Per. pazidan, pp: puxte» ثبت کرده است. پسوندهای «ـبا» و «ـوا» دنبالهٔ -pāka- اوستایی از راه -pāk فارسی میانه‌اند؛ \"\n  \"خودِ بارتولومه در پایان مدخل paka- می‌نویسد: «mp. °pāk, np. °bā, °vā»، یعنی p آغازینِ جزء دوم پس از واکه به b \"\n  \"نرم شده و -āk- به -āg- و سپس به -ā(و) بدل شده است. معین نیز در حاشیهٔ برهان قاطع همین را می‌گوید: «نانوا < نانبا … \"\n  \"از: نان + وا (پسوند با)» و «شوربا: از شور + با (آش)»؛ سپیدبا، سیکبا (سرکه/سیک + با، معرّبِ آن سکباج) و ناربا نیز \"\n  \"از همین ساخت‌اند. ادعای نورایی درست است.\"\n ),\n \"sources\": [WPOX, W],\n \"ref_check\": [\n  {\"ref\": \"BQT:370\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.370 (BQT_v1_pages.txt leaf 594; the footnote block ends «بقیه از صفحهٔ ۳۶۹», fixing the page). Mo'in's numbered footnote to پختن: «پهلوی puxtan، اوستا و سانسکریت pac (طبخ). کردی pêtin، افغانی …، اسـتی fitsun/fikun، بلوچی pačag/pažag، وخی …، شغنی و سریکلی …، ارمنی …». Covers poxtan; the -bā/-vā suffix is treated by Mo'in elsewhere (vols 3-4, see consulted).\"},\n  {\"ref\": \"AEF:195\", \"status\": \"not_checked\",\n   \"note\": \"Khaleqi Motlaq's Asās-e Eštteqāq-e Fārsi (the Persian translation of Horn's Grundriss) is not online (refs_online.json: catalogue only). Its proxies HRN.txt and HUB.txt were grepped for puxtan / pazad / پختن and return nothing under those spellings, so the page could not be checked.\"},\n  {\"ref\": \"IEC:920\", \"status\": \"supports\",\n   \"note\": \"Mann, An Indo-European Comparative Dictionary, printed p.920 (IEC.txt lines 12697ff., the running head '920' sits between the pent- and pequō entries): \\\"pequō, iō 'bake, cook, roast, ripen'. WP II, 18 … Av. pač- 'boil; burn'; Per. pazidan, pp: puxte 'cook'\\\"; p.921 s.v. pequtos adds \\\"Per. puxte\\\". Exactly the Persian forms of Nourai's box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 886 s.v. paka-\", \"stance\": \"supports\",\n   \"note\": \"\\\"j. paka- Adj. 'kochend'. KompE. — Zum V. pak-. — ai. °pāki- Adj., mp. °pāk, np. °bā, °vā.\\\" Bartholomae himself derives the New Persian suffixes -bā and -vā from Av. -pāka-, which is precisely Nourai's arrow.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 4 s.v. نانوا (BQT_v4_pages.txt line 7744) and vol. 3 s.v. شوربا (BQT_v3_pages.txt line 7547)\", \"stance\": \"supports\",\n   \"note\": \"«* نانوا - بسکون سوم < نانبا < فولرس II ۱۲۸۹، از: نان + وا (پسوند با) … کردی nān-pān (نانواخانه)»; «شوربا - از: شور + با (آش)، معرّب آن شورباج و شوربه». Mo'in's own footnotes give the -bā/-vā compounds of Nourai's box.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur Kashani, p.157 s.v. پختن، پخت\", \"stance\": \"supports\",\n   \"note\": \"A full IE cognate table under the headword «پختن، پخت» (Avestan, Old Persian, Pahlavi, Ossetic, Kurdish, Balochi, Pashto, Tocharian A/B, Sanskrit, Armenian, Greek, Latin, the Romance and Germanic reflexes incl. English cook, Slavic, Baltic, Celtic, Albanian), with برهان قاطع among the cited sources (incoming/ARY/ARY_pages.txt, pdf pages 156-157).\"},\n  {\"src\": \"CHEUNG\", \"where\": \"EDIV p.287 s.v. *pač\", \"stance\": \"supports\",\n   \"note\": \"\\\"NWIR: NP puxtan/paz- 'to cook; to ripen'…\\\", with Bal. patk/pac-, Zaz. pewtiš/pewžen-, Oss. fycyn/fyx(t), Yaghnobi pac-/pásta etc.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Latin\",\n \"words\": \"coquere; bis-coctus\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Lat. coquō, coquere 'to cook, ripen' comes from *pekʷō by the Italo-Celtic assimilation of the initial *p- to \"\n  \"the following labiovelar (*pekʷō > *kʷekʷō), the change Pokorny states explicitly ('ital. kelt. Assim. von \"\n  \"*pekʷō zu *kʷekʷō'); hence also ppl. coctus < *kʷokʷtos (= Skt. paktá-, Gk. peptós), coquus 'cook', coquīna \"\n  \"'kitchen'. bis coctus 'twice-cooked' is not classical Latin as a lexeme: it is the medieval phrase (pānis) \"\n  \"bis coctus, Medieval Latin biscoctum, coined for the twice-baked ship's bread, whence It. biscotto and OFr. \"\n  \"bescuit. Nourai's cross-reference '☞Dwo' for bis- is right: bis < OLat. duis < *dwis, from *dwo- 'two'.\"\n ),\n \"derivation_fa\": (\n  \"coquere لاتین «پختن، رساندن» از *pekʷō آمده است، با همگونی ایتالیک-سلتیِ p آغازین با لب‌کامیِ پس از آن \"\n  \"(*pekʷō > *kʷekʷō)؛ پوکورنی همین را می‌گوید: «ital. kelt. Assim. von *pekʷō zu *kʷekʷō». از همین ریشه است \"\n  \"coctus (صفت مفعولی، هم‌ریشه با paktá- سنسکریت و peptós یونانی)، coquus «آشپز» و coquīna «آشپزخانه». \"\n  \"امّا bis coctus واژه‌ای کلاسیک نیست؛ ترکیبی است از لاتین میانه، (pānis) bis coctus «نانِ دوبار پخته»، که برای \"\n  \"نان خشکِ کشتی ساخته شد و biscotto ایتالیایی و bescuit فرانسهٔ کهن از آن آمده‌اند. ارجاع نورایی به Dwo نیز درست \"\n  \"است، چون bis از duis کهن و آن از *dwis «دوبار» است.\"\n ),\n \"sources\": [W, EBIS],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins' appendix, s.v. pekʷ- (AHD_watkins1985.txt line 828): \\\"pekʷ-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kʷekʷ- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. [Pok. pekʷ- 798.]\\\" Nourai cites AHD without a page here and the appendix entry carries the whole Latin branch of his chart.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.798\", \"stance\": \"supports\",\n   \"note\": \"\\\"lat. coquō, -ere ,kochen' (ital. kelt. Assim. von *pekʷō zu *kʷekʷō), coquus ,Koch' (: ἀρτο-κόπος), coquīna ,Küche', als osk.-umbr. Lw. popīna\\\".\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II pp. 17-18 s.v. pequ-\", \"stance\": \"supports\",\n   \"note\": \"\\\"lat. coquio, -ere ,kochen' (ital. kelt. Ass. von peqʷo…)\\\"; sup. paktum = lat. coctum; Ptc. paktá- = lat. coctus.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. biscuit; s.v. cook\", \"stance\": \"supports\",\n   \"note\": \"\\\"biscuit, n. — F. biscuit, fr. L. bis coctus, 'twice cooked' (whence also It. biscotto), fr. bis, 'twice', and coctus, pp. of coquere, 'to cook'.\\\" (KLN_1966.txt line 5064).\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"English\",\n \"words\": \"cook, cuisine, kiln, kitchen\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"None of the four is inherited: all are Latin words taken into English at different dates, so the chart's \"\n  \"Latin→English arrow is a borrowing arrow. OE cōc 'cook' (whence ME cook) is an early Germanic loan of Vulgar \"\n  \"Latin cocus (classical coquus); OE cycene > ME kichene > kitchen is from Vulgar Latin cucina, a dissimilated \"\n  \"variant of coquīna; OE cylene, cylne > ME kilne > kiln is from Lat. culīna 'kitchen, cooking-stove' (itself a \"\n  \"dialectal by-form of coquīna); cuisine is a much later (18th-c.) borrowing of French cuisine < Late Latin \"\n  \"cocina. Watkins lists exactly COOK, CUISINE, (CULINARY), KILN, KITCHEN under the assimilated Latin form.\"\n ),\n \"derivation_fa\": (\n  \"هیچ‌یک از این چهار واژه ارثی نیست؛ همه در دوره‌های گوناگون از لاتین به انگلیسی وام گرفته شده‌اند، پس پیکان \"\n  \"«لاتین ← انگلیسی» در اینجا پیکان وام‌گیری است. cōc انگلیسی کهن (> cook) وام‌واژه‌ای کهن از cocus لاتین عامیانه \"\n  \"(کلاسیک: coquus) است؛ cycene انگلیسی کهن > kichene > kitchen از cucina لاتین عامیانه، گونهٔ ناهمگون‌شدهٔ coquīna؛ \"\n  \"cylene > kilne > kiln از culīna لاتین «آشپزخانه، اجاق»؛ و cuisine وامی بسیار متأخرتر (سدهٔ هجدهم) از فرانسهٔ \"\n  \"cuisine < cocina لاتین پسین است. واتکینز در پیوست ریشه‌های هندواروپایی دقیقاً همین چهار واژه را ذیل صورت \"\n  \"همگون‌شدهٔ لاتین آورده است. ادعای نورایی درست است.\"\n ),\n \"sources\": [W],\n \"ref_check\": [\n  {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n   \"note\": \"The box carries no refs= of its own; the branch is covered by the AHD citation on the parent Latin node, whose Watkins entry names COOK, CUISINE, (CULINARY), KILN, KITCHEN.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.vv. cuisine, kiln, kitchen, cook\", \"stance\": \"supports\",\n   \"note\": \"\\\"cuisine, n. … — F., 'kitchen', fr. Late L. cocina, a var. of coquina, 'kitchen', fr. coquere\\\" (line 9878); \\\"kiln, n. … — ME. kilne, kulne, fr. OE. cylene, cylne, fr. L. culina, 'kitchen'\\\" (line 20681); \\\"kitchen, n. — ME. kuchene, kichene, kichen, fr. OE. cycene, fr. L. cucina … dissimilated var. of L. coquina\\\" (line 20733); Klein's cook entry lists the whole family \\\"apricot, biscuit, concoct, cotta, culinary, decoct, dyspepsia, kiln, kitchen, melon, pepo, pepsin, peptic, precocious, pucka, pumpkin, quittor, terra cotta\\\" (line 9092).\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins s.v. pekʷ- and the index (KILN pekʷ-, KITCHEN pekʷ-, CUISINE pekʷ-, cook pekʷ-)\", \"stance\": \"supports\",\n   \"note\": \"The index lines of the 1985 edition list KILN, KITCHEN, CUISINE, CULINARY and cook all under pekʷ- (AHD_watkins1985.txt lines 1713, 1718, 1402, 1394).\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. Biscuit ('See Cook')\", \"stance\": \"partial\",\n   \"note\": \"Skeat's own cook entry is badly OCRed in SKT.txt, but the cross-references that survive (\\\"Biscuit. (F.-L.) See Cook.\\\", line 1825) show the same grouping of the family under cook.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"French\",\n \"words\": \"bescuit\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Old French bescuit (12th c.; also bescoit, ModFr. biscuit) is the calque-compound bes- + cuit, i.e. Lat. bis \"\n  \"'twice' + coctus 'cooked' (OFr. cuit < coctum), rendering Medieval Latin (pānis) biscoctus, the twice-baked \"\n  \"hard bread baked for ships and armies — hence Nourai's gloss 'a thin cracker'. English took it as besquite \"\n  \"(early 14th c.). It. biscotto and Sp. bizcocho are the same formation.\"\n ),\n \"derivation_fa\": (\n  \"bescuit فرانسهٔ کهن (سدهٔ دوازدهم؛ گونه‌های bescoit و biscuit امروزی) ترکیبی است از bes- + cuit، یعنی bis لاتین \"\n  \"«دوبار» + coctus «پخته» (cuit فرانسهٔ کهن از coctum)، و برگردانِ (pānis) biscoctus لاتین میانه است: نان سختِ \"\n  \"دوبارپخته که برای کشتی و لشکر می‌پختند — و معنای «ترد و نازک» که نورایی داده از همین‌جاست. انگلیسی آن را در \"\n  \"آغاز سدهٔ چهاردهم به‌صورت besquite گرفت. biscotto ایتالیایی و bizcocho اسپانیایی نیز همین ساخت‌اند. ادعای \"\n  \"نورایی درست است.\"\n ),\n \"sources\": [EBIS],\n \"ref_check\": [\n  {\"ref\": \"AHD:135\", \"status\": \"partial\",\n   \"note\": \"The page number belongs to the 1975/76 AHD New College Edition, which is not open online (only lending copies), so p.135 itself could not be read; the same dictionary's IE-roots appendix (Watkins) does list BISCUIT under pekʷ- (AHD_watkins1985.txt lines 828 and 1306, 'BISCUIT dwo-, pekʷ-'), which is the substance of the arrow, and p.135 is where 'biscuit' falls alphabetically in that edition.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. biscuit\", \"stance\": \"supports\",\n   \"note\": \"\\\"biscuit, n. — F. biscuit, fr. L. bis coctus, 'twice cooked' (whence also It. biscotto), fr. bis, 'twice' (see prec. word), and coctus, pp. of coquere, 'to cook'. See cook, n., and cp. bisque.\\\" (KLN_1966.txt line 5064).\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Biscuit\", \"stance\": \"supports\",\n   \"note\": \"\\\"Biscuit. (F.-L.) See Cook.\\\" — Skeat files it as a French word of Latin origin belonging to the coquere family (SKT.txt line 1825).\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Persian\",\n \"words\": \"bîskŭît «بیسکویت»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Persian بیسکویت biskuit is a modern (late Qajar / early 20th-c.) loan straight from French biscuit, taken in \"\n  \"with the European pastry trade; the spelling with و + ی for the French /ɥi/ of -cuit and the final ت for the \"\n  \"unpronounced French -t betray a written French model rather than English 'biscuit'. Mo'in's dictionary tags \"\n  \"the word [فر.], i.e. French, and defines it «نوعی شیرینی که خشک و کم‌وزن است».\"\n ),\n \"derivation_fa\": (\n  \"«بیسکویت» وام‌واژه‌ای نو (اواخر قاجار و آغاز سدهٔ چهاردهم خورشیدی) و مستقیماً از biscuit فرانسه است که همراه \"\n  \"شیرینی‌پزی فرنگی وارد شد. املای آن با «وی» برای /ɥi/ فرانسوی در -cuit و «ت» پایانی برای t نانوشتهٔ فرانسوی \"\n  \"نشان می‌دهد که الگو، صورت نوشتاری فرانسه بوده است نه biscuit انگلیسی. معین این واژه را با نشانهٔ [فر.] یعنی \"\n  \"فرانسوی آورده و «نوعی شیرینی که خشک و کم‌وزن است» معنی کرده است. ادعای نورایی درست است.\"\n ),\n \"sources\": [ABIS, WBIS, EBIS],\n \"ref_check\": [\n  {\"ref\": \"MON:626\", \"status\": \"partial\",\n   \"note\": \"Mo'in's six-volume Farhang-e Fārsi is not online (refs_online.json: only the 2-vol Adena condensation, with different pagination), so p.626 could not be opened. The entry text itself is reproduced on abadis.ir under 'فرهنگ معین': «[ فر. ] نوعی شیرینی که خشک و کم وزن است» — the [فر.] tag is exactly Nourai's claim (French source), only the page is unverified.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. بیسکویت, via abadis.ir\", \"stance\": \"supports\",\n   \"note\": \"origin tag «[ فر. ]» (French) with the gloss «نوعی شیرینی که خشک و کم وزن است»; the same page's encyclopaedic section adds that the word is Latin bis + coquere 'twice-baked'.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. biscuit\", \"stance\": \"supports\",\n   \"note\": \"confirms that the donor form is French biscuit < L. bis coctus, i.e. the French word (not the Italian biscotto or English pronunciation) is what Persian reproduces.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"English\",\n \"words\": \"biscuit\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"English borrowed the French word twice over: ME besquite/bisquite (early 14th c.) directly from OFr. bescuit, \"\n  \"then the spelling was re-Frenchified in the early 19th c. from the earlier phonetic bisket (16th-18th c.) to \"\n  \"the modern biscuit, which is why the spelling is French but the pronunciation /ˈbɪskɪt/ is not.\"\n ),\n \"derivation_fa\": (\n  \"انگلیسی این واژه را دوبار از فرانسه گرفت: نخست در آغاز سدهٔ چهاردهم به‌صورت besquite/bisquite از bescuit \"\n  \"فرانسهٔ کهن، و سپس در آغاز سدهٔ نوزدهم املای آن را از bisket (که تلفظ واقعی را نشان می‌داد) دوباره به شکل \"\n  \"فرانسویِ biscuit برگرداندند؛ به همین سبب املا فرانسوی است ولی تلفظ /bɪskɪt/ فرانسوی نیست. ادعای نورایی درست است.\"\n ),\n \"sources\": [EBIS],\n \"ref_check\": [\n  {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n   \"note\": \"No refs= on this box; the parent French node cites AHD:135, and Watkins' index does list 'BISCUIT dwo-, pekʷ-'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. biscuit\", \"stance\": \"supports\",\n   \"note\": \"\\\"biscuit, n. — F. biscuit, fr. L. bis coctus…\\\" — Klein derives the English word from French, as the chart draws it (KLN_1966.txt line 5064).\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Biscuit\", \"stance\": \"supports\",\n   \"note\": \"\\\"Biscuit. (F.-L.) See Cook.\\\" — labelled a French word of Latin origin.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"Arabic\",\n \"words\": \"al-birqŭq\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Arabic البرقوق al-barqūq / al-birqūq (al- is the article) does go back to Lat. (mālum) praecoquum \"\n  \"'early-ripening (fruit)', praecox = prae 'before' + coquere — so the ultimate source in the chart is right — \"\n  \"but not directly: Latin praecoquum was hellenised as Gk. πραικόκκιον / βερίκοκκον, and Arabic took it from \"\n  \"Byzantine Greek, Wiktionary via Classical Syriac ܒܪܩܘܩܐ barqūqā < Byz.Gk. βερικοκκία 'apricot tree'; Lokotsch \"\n  \"no. 247 states the same route ('Ar. barkūk: aus dem lat. praecocium… über gr. πραικόκκιον'). The chart's \"\n  \"single Latin→Arabic arrow therefore compresses two intermediaries. Nourai's gloss '(plum)' is well taken: \"\n  \"Lokotsch notes the Arabic word came to mean 'Pflaume' while the apricot is mišmiš, and Wiktionary gives \"\n  \"'plums' as the main sense with 'apricots' only in Yemen, al-Andalus, Sicily and the Maghrib. The vocalisation \"\n  \"birqūq is the one Etymonline prints; Klein and Lokotsch write barqūq, which is the standard form.\"\n ),\n \"derivation_fa\": (\n  \"«البرقوق» عربی (با ادات تعریف ال-) سرانجام به (mālum) praecoquum لاتین «میوهٔ زودرس» می‌رسد — praecox از prae \"\n  \"«پیش» و coquere — پس اصلِ زنجیره در نمودار درست است، ولی راه آن مستقیم نیست: صورت لاتینی نخست در یونانی به \"\n  \"πραικόκκιον/βερίκοκκον درآمد و عربی آن را از یونانی بیزانسی گرفت؛ ویکی‌واژه واسطهٔ سریانی کلاسیک barqūqā را \"\n  \"می‌افزاید و لوکوچ (شمارهٔ ۲۴۷) نیز همین راه را می‌گوید. بنابراین یک پیکانِ «لاتین ← عربی» دو واسطه را حذف کرده \"\n  \"است. معنی «آلو» که نورایی داده درست است: در بیشتر جهان عرب برقوق «آلو» است و زردآلو «مشمش» خوانده می‌شود. \"\n  \"ضبط birqūq از اتیمانلاین است و کلاین و لوکوچ barqūq می‌نویسند که صورت معیار است. با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [WBAR, EAPR],\n \"ref_check\": [\n  {\"ref\": \"AHD:65\", \"status\": \"partial\",\n   \"note\": \"p.65 of the 1975/76 New College Edition (where 'apricot' falls alphabetically) is not open online; Watkins' appendix in the same dictionary does list APRICOT under pekʷ- (AHD_watkins1985.txt lines 828, 1253 'APRICOT pekʷ-'), and the AHD entry for apricot is the standard source for the Latin→Greek→Arabic→Romance chain. The claim is supported, the page unverifiable.\"}\n ],\n \"consulted\": [\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 247, Ar. barkūk\", \"stance\": \"partial\",\n   \"note\": \"\\\"247. Ar. barkūk: [Aus dem lat. praecocium 'das Frühreife' über gr. πραικόκκιον, πραικόκια, πρεκόκκια, βερικοκκα, s. Lammens Fārūk S. 364 Anm.; das ar. Wort hat übrigens die Bedeutung 'Pflaume' erhalten, während die Aprikose mišmiš heißt]; hieraus sp. albaricoque … frz. abricot … engl. apricot.\\\" Same ultimate origin as Nourai, but with Greek as the intermediary.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. apricot\", \"stance\": \"partial\",\n   \"note\": \"\\\"apricot, n. — F. abricot, fr. Port. albricoque, fr. Arab. al-barqūq, fr. al- 'the', and πραικόκκιον, Grecized form of L. praecoquum, 'apricot', neut. of praecoquus = praecox, 'early ripe'… See also cook.\\\" (KLN_1966.txt line 3240) — again Greek between Latin and Arabic, and barqūq not birqūq.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n   \"note\": \"grep of AFM_pages.txt for برقوق returns nothing — Addi Shir collects Persian loans in Arabic and does not treat this Graeco-Latin one.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"English\",\n \"words\": \"apricot\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"English did get the word from Arabic al-barqūq, but through Iberian Romance and French, not directly: \"\n  \"Andalusi Arabic al-barqūq gave Port. albricoque / Sp. albaricoque / Catalan abercoc, and English first has \"\n  \"abrecock, apricock (1550s, the fruit itself reaching England in 1524), later assimilated in spelling to Fr. \"\n  \"abricot, whence modern apricot. The initial a- of the English word is the remnant of the Arabic article al-. \"\n  \"The chart's direct Arabic→English arrow is thus true of the ultimate source but silent about the Iberian and \"\n  \"French stages, and about the -ck > -t substitution that Klein remarks on.\"\n ),\n \"derivation_fa\": (\n  \"انگلیسی این واژه را از «البرقوق» عربی گرفته است، امّا نه بی‌واسطه: صورت اندلسیِ al-barqūq در پرتغالی albricoque، \"\n  \"در اسپانیایی albaricoque و در کاتالان abercoc شد و انگلیسی نخست abrecock/apricock را در دههٔ ۱۵۵۰ به کار برد \"\n  \"(خودِ میوه در ۱۵۲۴ به انگلستان رسید) و سپس املای آن را با abricot فرانسه همسان کرد و apricot امروزی پدید آمد. \"\n  \"«a» آغازینِ واژه بازماندهٔ ادات تعریف عربی «ال» است. پس پیکان مستقیم «عربی ← انگلیسی» دربارهٔ سرچشمه درست است \"\n  \"ولی مرحله‌های ایبریایی و فرانسوی و نیز ابدال -ck به -t را نادیده گرفته است. با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [EAPR, WBAR],\n \"ref_check\": [\n  {\"ref\": \"AHD:65\", \"status\": \"partial\",\n   \"note\": \"Same as the parent node: the 1976 New College page 65 is not open online; Watkins' index in the same dictionary has 'APRICOT pekʷ-' and the appendix entry lists APRICOT among the Latin coquere derivatives, so the substance of the citation checks out.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. apricot\", \"stance\": \"partial\",\n   \"note\": \"\\\"F. abricot, fr. Port. albricoque, fr. Arab. al-barqūq…\\\" plus \\\"For the interchangeability of -c (= -k) and -t cp. havoc (fr. OF. havot), bat…\\\" — Klein routes the English word through Portuguese and French (KLN_1966.txt line 3240).\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 247\", \"stance\": \"partial\",\n   \"note\": \"\\\"hieraus sp. albaricoque, albercoque, pg. albricoque … prov. aubricot, frz. abricot, it. albicocco … engl. apricot\\\" — English is listed at the end of the Romance chain, not directly after Arabic.\"},\n  {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. apricot\", \"stance\": \"silent\",\n   \"note\": \"the entries found in FSD_vol1.txt (lines 10121, 22436) are the botanical senses ('apricot plum', 'Japanese apricot'); the OCR of the etymology bracket of the main entry is not legible, so F&W adds nothing here.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11,\n \"lang\": \"Greek\",\n \"words\": \"peptein; pepôn\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Gk. πέσσω / Att. πέττω 'I cook, digest' is from *pekʷ-yō; beside it stands the σκ-less thematic πέπτω, whose \"\n  \"infinitive πέπτειν is the citation form used by AHD and Klein and by Nourai here. πέπων, -ονος 'ripe, \"\n  \"mellow' is the same root with the -ων suffix; used with σίκυος 'gourd, cucumber', σίκυος πέπων meant the \"\n  \"gourd eaten only when fully ripe, and πέπων alone became the name of the melon (Lat. pepō, -ōnis). Nourai's \"\n  \"gloss 'a large melon (edible only when ripe)' reproduces Klein's wording almost exactly ('so called because \"\n  \"it is not eaten until it is quite ripe').\"\n ),\n \"derivation_fa\": (\n  \"πέσσω (آتیک πέττω) «می‌پزم، گوارش می‌کنم» از *pekʷ-yō است و در کنار آن صورت πέπτω قرار دارد که مصدر آن \"\n  \"πέπτειν همان صورتی است که فرهنگ AHD و کلاین و نورایی به کار برده‌اند. πέπων «رسیده، نرم» از همان ریشه با \"\n  \"پسوند -ων است؛ در ترکیب σίκυος πέπων «کدوی رسیده» و سپس به‌تنهایی نام خربزه شد (لاتین pepō). معنایی که \"\n  \"نورایی داده — «خربزهٔ بزرگ که تنها پس از رسیدن خوردنی است» — تقریباً عین عبارت کلاین است. ادعای نورایی درست است.\"\n ),\n \"sources\": [W, EPUM],\n \"ref_check\": [\n  {\"ref\": \"AHD:1059\", \"status\": \"partial\",\n   \"note\": \"p.1059 of the 1975/76 New College Edition (the 'pepo/pumpkin' stretch of the alphabet) is not open online. Watkins' appendix in the same dictionary carries the claim: \\\"2. Greek pepon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN.\\\" (AHD_watkins1985.txt line 828) — both of Nourai's Greek words with his glosses.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"IEW p.798\", \"stance\": \"supports\",\n   \"note\": \"\\\"gr. πέσσω, att. πέττω ,koche, verdaue' (*pekʷi̯ō), i̯o-Präs. πέπτω; πέψις f. ,Kochen'; πέπων, -ονος ,reif' (f. πέπειρα…), πόπανον ,Gebäck, Kuchen'.\\\"\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. pumpkin\", \"stance\": \"supports\",\n   \"note\": \"\\\"…fr. L. peponem, acc. of pepō, 'melon, pumpkin', fr. Gk. πέπων, 'melon', prop. 'cooked by the sun, ripe', from the stem of πέπτειν, 'to cook' (see peptic and cook); so called because it is not eaten until it is quite ripe.\\\" (KLN_1966.txt line 30995).\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. II p. 17\", \"stance\": \"supports\",\n   \"note\": \"\\\"gr. πέσσω, att. πέπτω ,koche, verdaue' (*peqʷi̯o, ai. pácyate). i̯o-Praes. πέπτω, πέπων, -ονος ,reif'\\\".\"}\n ]\n})\n\nnodes.append({\n \"id\": 12,\n \"lang\": \"French\",\n \"words\": \"pompon\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"The form is Middle French pompon (also popon, pepon) 'melon, pumpkin', 16th c. — a real word, and the \"\n  \"immediate source of English pompion/pumpion — but it does not come straight from Greek: it continues Lat. \"\n  \"pepōnem, acc. of pepō 'melon', which is itself the Greek loanword πέπων. So the chart's Greek→French arrow \"\n  \"skips the Latin stage that both Klein and Etymonline give. It should also be kept apart from the homophonous \"\n  \"modern French pompon 'tuft of feathers/wool', which Klein files separately as 'prob. of imitative origin'; \"\n  \"the modern French words for pumpkin are potiron and citrouille.\"\n ),\n \"derivation_fa\": (\n  \"صورت مورد بحث pompon فرانسهٔ میانه (و گونه‌های popon و pepon) به معنی «خربزه، کدوحلوایی» در سدهٔ شانزدهم است — \"\n  \"واژه‌ای واقعی و سرچشمهٔ بی‌واسطهٔ pompion/pumpion انگلیسی — امّا مستقیماً از یونانی نیامده است: دنبالهٔ peponem \"\n  \"لاتین (حالت مفعولی pepō «خربزه») است که خود وام‌واژه‌ای از πέπων یونانی است. پس پیکان «یونانی ← فرانسه» در \"\n  \"نمودار مرحلهٔ لاتین را — که هم کلاین و هم اتیمانلاین می‌آورند — حذف کرده است. نیز باید آن را از pompon \"\n  \"فرانسویِ امروزی به معنی «منگوله» جدا داشت که کلاین آن را واژه‌ای آوابنیاد و جدا می‌داند؛ کدوحلوایی در فرانسهٔ \"\n  \"امروز potiron یا citrouille است. با احتیاط پذیرفتنی است.\"\n ),\n \"sources\": [EPUM],\n \"ref_check\": [\n  {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n   \"note\": \"No refs= on this box; the parent Greek node cites AHD:1059, whose Watkins entry puts PUMPKIN under Greek peptein/pepon but says nothing about the French form.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. pumpkin\", \"stance\": \"partial\",\n   \"note\": \"\\\"pumpkin, n. — Fr. earlier pompion, pumpion, fr. MF. pompon, fr. L. peponem, acc. of pepō, 'melon, pumpkin', fr. Gk. πέπων\\\" (line 30995) — Middle French pompon confirmed, but with Latin between it and Greek. Klein's separate entry \\\"pompon, n., an ornament of feathers. — F., prob. of imitative origin\\\" (line 29567) shows the modern French homonym is a different word.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann p.920 s.v. pequō / pequos\", \"stance\": \"partial\",\n   \"note\": \"Mann lists \\\"Gk. cf. pépon, n.\\\" and the Latin reflexes under pequos but has no French entry; the Romance forms are treated as Latin continuations, not Greek ones.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13,\n \"lang\": \"English\",\n \"words\": \"pumpkin\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"English pompion / pumpion (1540s) from MFr. pompon was altered in the 1640s to pumpkin by replacing the final \"\n  \"syllable with the native diminutive suffix -kin (as in napkin, bumpkin), the -on of the French/Latin word \"\n  \"having apparently been felt as a diminutive already. The chart's French→English arrow is correct; only the \"\n  \"intermediate English form pompion is left out.\"\n ),\n \"derivation_fa\": (\n  \"صورت انگلیسیِ pompion/pumpion (دههٔ ۱۵۴۰) از pompon فرانسهٔ میانه گرفته شد و در دههٔ ۱۶۴۰ هجای پایانی آن با \"\n  \"پسوند تصغیر بومی -kin (مانند napkin و bumpkin) جایگزین شد و pumpkin پدید آمد؛ گویا -on فرانسوی/لاتینی را نیز \"\n  \"پسوند تصغیر پنداشته بودند. پیکان «فرانسه ← انگلیسی» درست است و تنها حلقهٔ میانیِ pompion در نمودار نیامده است. \"\n  \"ادعای نورایی درست است.\"\n ),\n \"sources\": [EPUM],\n \"ref_check\": [\n  {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n   \"note\": \"No refs= on this box; the branch's only citation is AHD:1059 on the Greek node, and Watkins' index does have 'PUMPKIN pekʷ-' (AHD_watkins1985.txt line 2140).\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"s.v. pumpkin\", \"stance\": \"supports\",\n   \"note\": \"\\\"pumpkin, n. — Fr. earlier pompion, pumpion, fr. MF. pompon…\\\" (line 30995); Klein also lists pumpkin among the derivatives of cook (line 9092).\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins index, 'PUMPKIN pekʷ-'\", \"stance\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 2140 files PUMPKIN under pekʷ-, and the appendix entry puts it in the Greek peptein group.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Pekw\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *pekʷ- 'to cook, ripen'\",\n \"note\": (\n  \"Pokorny IEW 798: \\\"pekʷ- ,kochen'; Partiz. pekʷ-to- ,gekocht'; pekʷ-ti- ,das Kochen', pekʷ-ter-, pokʷo-s \"\n  \",Koch'\\\"; Watkins/AHD \\\"pekʷ-. To cook, ripen. [Pok. pekʷ- 798]\\\"; LIV 468. The reconstruction, the language \"\n  \"label (Indo-European) and the gloss 'to cook' are all correct; the root's second sense 'ripen', which \"\n  \"Pokorny, Watkins and Buck all record, is what the Greek (pepōn 'ripe' > melon) and the Arabic/Latin \"\n  \"(praecoquum 'early-ripening' > apricot) branches of this chart actually depend on, so Nourai's one-word gloss \"\n  \"is thinner than his own tree needs. One flaw on the page: the Avestan box heads its forms with 'pax', which \"\n  \"is not an Avestan word (see node 1) — the printed page has it, so it is the book's slip, not the extraction's. \"\n  \"Otherwise every arrow on the page is sound; the Arabic and the two Romance arrows compress one intermediary \"\n  \"each (Greek/Syriac for al-barqūq, Iberian Romance + French for apricot, Latin pepō for French pompon).\"\n ),\n \"note_fa\": (\n  \"ریشهٔ هندواروپاییِ آغازینِ *pekʷ- «پختن، رسیدن» است؛ پوکورنی (ص ۷۹۸) آن را «kochen» با صفت مفعولی *pekʷ-to- و \"\n  \"نام‌فعل *pekʷ-ti- و نامِ کنندهٔ *pokʷo-s «آشپز» می‌آورد، واتکینز «to cook, ripen» و LIV ص ۴۶۸ همین را. \"\n  \"بازسازی، برچسب زبانی و معنای «to cook» هر سه درست‌اند؛ امّا معنای دومِ ریشه یعنی «رسیدن» — که پوکورنی و \"\n  \"واتکینز و باک هر سه ثبت کرده‌اند — همان چیزی است که شاخهٔ یونانی (πέπων «رسیده» > خربزه) و شاخهٔ لاتین/عربی \"\n  \"(praecoquum «زودرس» > زردآلو) بر آن استوارند، پس معنای تک‌واژه‌ایِ نورایی از آنچه درخت خودش نیاز دارد تنگ‌تر است. \"\n  \"یک لغزش در صفحه هست: جعبهٔ اوستایی با «pax» آغاز می‌شود که واژهٔ اوستایی نیست (نگاه کنید به گرهٔ ۱)؛ چون صفحهٔ \"\n  \"چاپی نیز همین را دارد، خطای کتاب است نه خطای خوانش اسکن. جز آن همهٔ پیکان‌ها درست‌اند و تنها سه پیکان \"\n  \"(عربی، زردآلو، و pompon فرانسوی) هر یک یک واسطه را حذف کرده‌اند.\"\n ),\n \"sources\": [W, WPOX],\n \"ref_check\": [\n  {\"ref\": \"POK:798\", \"status\": \"supports\",\n   \"note\": \"Pokorny, IEW p.798 (POK_03.txt, the page number '798' is printed in the text at the end of leaf 31): \\\"pekʷ- ,kochen'; Partiz. pekʷ-to- ,gekocht'; pekʷ-ti- ,das Kochen', pekʷ-ter-, pokʷo-s ,Koch'. Ai. pácati, av. pacaiti ,kocht, bäckt, brät' (= lat. coquō, cymr. pobi, alb. pjek…)… WP. II 17 f.\\\" The cited page is exactly the root entry.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pekʷ- (p.53 of the standalone ed.)\", \"stance\": \"supports\",\n   \"note\": \"\\\"pekʷ-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kʷekʷ- in Latin coquere… 2. Greek pepon, ripe: PEPO. 3. Greek peptein… 5. Sanskrit pakva-, ripe: PUKKA. [Pok. pekʷ- 798.]\\\" (AHD_watkins1985.txt line 828).\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II p.17 s.v. pequ- 'Kochen'\", \"stance\": \"supports\",\n   \"note\": \"the entry Pokorny himself refers to ('WP. II 17 f.'): \\\"pequ- ,Kochen'. Ai. pácati, pacaiti ,kocht, bäckt, brät' (= lat. coquo, cymr. pobi, alb. pjek, abg. …)\\\" with av. nasu-paka- and gr. πέσσω (incoming/WLD/WLD_Bd2_pages.txt lines 1119ff.).\"},\n  {\"src\": \"SYN\", \"where\": \"Buck 1949, printed p.336, §5.21 COOK\", \"stance\": \"supports\",\n   \"note\": \"\\\"Words for 'cook' … belong mostly to an inherited group representing an IE *pekʷ-. The forms of this root in Indo-Iranian, Tocharian, Greek, and Latin have the general meaning 'cook' (also 'ripen' fruit in Skt., Grk., Toch.)… 1. IE *pekʷ-. Walde-P. 2.17f. … Skt. pac-, Av. pač- 'cook'; … Lat. coquere, with its derivs.\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, printed p.920-921 s.vv. pequō, pequos, pequtis, pequtos\", \"stance\": \"supports\",\n   \"note\": \"\\\"pequō, iō 'bake, cook, roast, ripen'. WP II, 18\\\" with Skt. pácāmi, Av. pač-, Per. pazidan/puxte, Gk. péptō/péssō, Lat. coquō; and \\\"pequos (poqu-) (1) 'cooking'… Gk. cf. pépon\\\".\"}\n ],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 388,\n \"book_page\": 358,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-388.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-388.py"
}
```


### [2026-09-07T21:01:27.134Z] TOOL RESULT

```
written
```


## [2026-09-07T21:01:31.142Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-388.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 388"
}
```


### [2026-09-07T21:01:32.617Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'transcription_suspect': 1, 'confirmed': 9, 'plausible': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'partial': 6, 'not_checked': 5}
books consulted: {'supports': 25, 'silent': 3, 'partial': 7} | by book: {'KLN': 10, 'WLD': 3, 'CHEUNG': 3, 'SKT': 3, 'BRT': 2, 'POK': 2, 'AHD': 2, 'LKT': 2, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'ARY': 1, 'MON': 1, 'AFM': 1, 'FSD': 1, 'IEC': 1}
```


## [2026-09-07T21:01:37.196Z] TOOL CALL #61: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ | head -20; ls data/verification/sources/refs/ocr/BOOK/ 2>/dev/null | head -5"
}
```


### [2026-09-07T21:01:37.260Z] TOOL RESULT

```
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
100.png
101.png
102.png
103.png
104.png
```


## [2026-09-07T21:01:41.237Z] TOOL CALL #62: Bash

```json
{
 "command": "cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg388.png data/verification/sources/refs/ocr/BOOK/388.png && ls -la data/verification/sources/refs/ocr/BOOK/388.png && git status --short | head"
}
```


### [2026-09-07T21:01:41.354Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66598 Sep  7 17:01 data/verification/sources/refs/ocr/BOOK/388.png
```


## [2026-09-07T21:01:45.242Z] TOOL CALL #63: Bash

```json
{
 "command": "git status --short --untracked-files=all -- data/verification/page-388.json data/verification/sources/refs/ocr/BOOK/388.png; echo \"exit=$?\"; git check-ignore -v data/verification/page-388.json data/verification/sources/refs/ocr/BOOK/388.png"
}
```


### [2026-09-07T21:01:46.450Z] TOOL RESULT

```
exit=0
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/388.png
```


## [2026-09-07T21:01:50.423Z] TOOL CALL #64: Bash

```json
{
 "command": "git status --short | head -20; echo \"---\"; git ls-files --error-unmatch data/verification/page-388.json 2>&1 | head -2"
}
```


### [2026-09-07T21:01:50.503Z] TOOL RESULT

```
---
data/verification/page-388.json
```


## [2026-09-07T21:01:55.107Z] TOOL CALL #65: Bash

```json
{
 "command": "git log --oneline -2 -- data/verification/page-388.json; echo \"---\"; git diff --stat HEAD -- data/verification/page-388.json; echo \"---size---\"; wc -c data/verification/page-388.json; git show HEAD:data/verification/page-388.json | wc -c"
}
```


### [2026-09-07T21:01:55.239Z] TOOL RESULT

```
20ccb89 Verify page 386 (Peig/piseh, pišeh, neveštan, paint, picture, file)
---
---size---
52987 data/verification/page-388.json
52987
```


## [2026-09-07T21:02:03.032Z] TOOL CALL #66: Bash

```json
{
 "command": "git show HEAD:data/verification/page-388.json | head -c 400; echo; echo \"=== md5 ===\"; git show HEAD:data/verification/page-388.json | md5sum; md5sum data/verification/page-388.json; echo \"=== HEAD is ===\"; git rev-parse --short HEAD; git log --oneline -1"
}
```


### [2026-09-07T21:02:03.122Z] TOOL RESULT

```
{
  "pdf_page": 388,
  "book_page": 358,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Pekw",
      "verdict": "confirmed",
      "modern_form": "PIE *pekʷ- 'to cook, ripen'",
      "note": "Pokorny IEW 798: \"pekʷ- ,kochen'; Partiz. pekʷ-to- ,gekocht'; pekʷ-ti- ,das Kochen', pekʷ-ter-, pokʷo-s ,Koch'\"; Watkins/AHD \"p
=== md5 ===
bd20515cedea7d22cc0f4f42c4b94dd7  -
bd20515cedea7d22cc0f4f42c4b94dd7  data/verification/page-388.json
=== HEAD is ===
20ccb89
20ccb89 Verify page 386 (Peig/piseh, pišeh, neveštan, paint, picture, file)
```


## [2026-09-07T21:02:32.243Z] AGENT

Done. Verification written, checker clean.

**Page 388 (book p. 358) — root `Pekw` (PIE \*pekʷ- "to cook, ripen"), 1 entry, 13 nodes**

Checker output: `nodes verified: 13/13` · node verdicts: 9 confirmed, 3 plausible, 1 transcription_suspect · root: confirmed · ref checks: 8 supports / 6 partial / 5 not_checked · 0 PROBLEM lines.

Key reference findings (all quoted in the JSON):
- **POK:798** verified verbatim (root + `av. pacaiti` + `av. nasu-pāka-`); **SYN:336** = Buck §5.21 COOK, verified on the printed page; **IEC:920** = Mann s.v. `pequō` with "Per. pazidan, pp: puxte"; **FFD:40** verified (پخت < MP puxt < OIr \*paxta- < \*pakta-; پز < MP paz); **SNS:137** verified via the glossary index "puxtag 137/4"; **BQT:370** verified as Mo'in's footnote s.v. پختن (page fixed by the «بقیه از صفحهٔ ۳۶۹» catch-line, BQT_v1 leaf 594).
- **Bartholomae col. 886** is the decisive source for node 3: "j. paka- Adj. 'kochend' … mp. °pāk, np. °bā, °vā" — Nourai's -با/-وا suffix arrow is Bartholomae's own; Mo'in confirms نانوا < نانبا and شوربا = شور + با (Borhan vols 3–4).
- AHD page numbers (65, 135, 1059) are 1976 New College pages, not open online → marked `partial`, with Watkins' appendix (APRICOT / BISCUIT / PUMPKIN under pekʷ-) checked instead. AEF:195 and MON:626 not accessible (`not_checked`), MON substance confirmed via abadis (Mo'in tags بیسکویت «[فر.]»).

Flagged items:
- **transcription_suspect — node #1, Avestan "pax"**: no such Avestan form; the x-stem belongs to Old Iranian \*paxta- (> MP puxt), not to Avestan. `error_in: "book"` — the printed page 358 shows "pax, pač, pačaiti", so the extraction is faithful and this is Nourai's own slip. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/388.png` (that dir is gitignored).
- **plausible #9 (Arabic al-birqŭq)**: ultimate Latin praecoquum is right, but Arabic took it from Byzantine Greek (Wiktionary adds Syriac barqūqā); Klein and Lokotsch no. 247 both insert Greek. Also standard vocalisation is *barqūq* (Etymonline does print "al-birquq", so not a transcription error).
- **plausible #10 (English apricot)**: reached English via Ibero-Romance (albricoque/abercoc → abrecock 1550s) and French abricot, not directly from Arabic.
- **plausible #12 (French pompon)**: Middle French pompon is real but continues Latin pepōnem, not Greek directly; also distinct from modern Fr. pompon "tuft".

No extraction errors found — the JSON matches the printed page on every form, including the Persian script extras (پزیدن، پز; نانوا، شوربا، سپیدبا، سیکبا، ناربا) and the Khāqānī couplet.

Eight web pages archived via `fetch_source.py` (Wiktionary \*pekʷ-, پختن, برقوق, بیسکویت; Etymonline apricot/biscuit/pumpkin; abadis Mo'in).
